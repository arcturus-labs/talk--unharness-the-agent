from __future__ import annotations

from pathlib import Path
from typing import Any

from pydantic import BaseModel, Field, field_validator
from pydantic_ai import Agent, RunContext
from pydantic_ai.models import Model
from pydantic_ai.capabilities import Thinking, WebFetch, WebSearch
from pydantic_ai.models.anthropic import AnthropicModel, AnthropicModelSettings
from pydantic_ai_skills import SkillsCapability

from .enums import UpdateActor, UpdateType
from .linked_in_retriever import get_linkedin_profile as retrieve_linkedin_profile

_SKILLS_DIR = Path(__file__).resolve().parents[2] / "skills"


def _format_prior_updates_for_prompt(application: Any, max_items: int = 25) -> str:
    if not application.updates:
        return "None"

    updates_in_order = sorted(application.updates, key=lambda u: u.timestamp)
    recent = updates_in_order[-max_items:]

    docs: list[str] = []
    for idx, update in enumerate(recent, start=1):
        notes = (update.internal_notes or "").strip()
        correspondence = (update.correspondence or "").strip()
        actor = getattr(update.actor, "value", str(update.actor))
        update_type = getattr(update.update_type, "value", str(update.update_type))
        recruiter_id = update.recruiter_id or "null"

        docs.append(
            "---\n"
            f"index: {idx}\n"
            f"timestamp: {update.timestamp.isoformat()}\n"
            f"actor: {actor}\n"
            f"update_type: {update_type}\n"
            f"recruiter_id: {recruiter_id}\n"
            "---\n\n"
            "### internal_notes\n"
            f"{notes or '(none)'}\n\n"
            "### correspondence\n"
            f"{correspondence or '(none)'}\n"
        )

    return "\n\n".join(docs)


class AIReviewOutput(BaseModel):
    update_type: UpdateType
    internal_notes: str = Field(min_length=1)
    correspondence: str = Field(min_length=1)

    @field_validator("internal_notes")
    @classmethod
    def internal_notes_must_not_be_blank(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("internal_notes must be a non-empty string")
        return value

    @field_validator("correspondence")
    @classmethod
    def correspondence_must_not_be_blank(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("correspondence must be a non-empty string")
        return value


class AIReviewer(Agent[None, AIReviewOutput]):
    def __init__(self, model: Model | str | None = None, capabilities: list[Any] | None = None) -> None:
        capabilities = capabilities if capabilities is not None else [
            SkillsCapability(directories=[_SKILLS_DIR]),
            Thinking(effort="high"),
            WebSearch(),
            WebFetch(),
        ]

        super().__init__(
            model=model
            or AnthropicModel(
                "claude-sonnet-5",
                settings=AnthropicModelSettings(anthropic_thinking={"type": "adaptive"}),
            ),
            output_type=AIReviewOutput,
            capabilities=capabilities,
            instructions=(
                "You are a careful candidate-screening assistant; use the skills in the "
                "repository skills directory to make a grounded recommendation."
            ),
        )

        @self.tool
        async def get_linkedin_profile(
            ctx: RunContext[None],
            first_name: str,
            last_name: str,
            company_name: str | None = None,
            company_url: str | None = None,
            linked_in_username: str | None = None,
        ) -> str:
            """Look up the LinkedIn profile for a candidate."""
            return await retrieve_linkedin_profile(
                first_name=first_name,
                last_name=last_name,
                company_name=company_name,
                company_url=company_url,
                linked_in_username=linked_in_username,
                message_history=list(ctx.messages),
            )

    async def review(
        self,
        application_id: str,
        service: Any,
        event_stream_handler: Any | None = None,
    ) -> AIReviewOutput:
        application = await service.get_application(application_id)

        job_opening = application.jobOpening
        hiring_company = job_opening.company
        sub_departments = ", ".join(str(value) for value in job_opening.subDepartments) or "None"

        prompt = (
            f"Application ID: {application_id}\n"
            f"Candidate: first_name=\"{application.firstName}\", last_name=\"{application.lastName}\"\n"
            f"Email: {application.email}\n"
            f"Phone: {application.mobile}\n"
            f"Bio: {application.bio}\n"
            f"LinkedIn URL: {application.linkedinUrl}\n"
            f"Job opening title: {job_opening.title}\n"
            f"Job opening seniority level: {job_opening.seniorityLevel}\n"
            f"Job opening department: {job_opening.department}\n"
            f"Job opening sub-departments: {sub_departments}\n"
            f"Job opening description: {job_opening.jobDescription}\n"
            f"Hiring company: {hiring_company.name}\n"
            f"Hiring company site: {hiring_company.siteUrl}\n"
            f"Hiring company size: {hiring_company.size}\n"
            f"Candidate region: {application.region}\n"
            "\nPrior updates (chronological; later updates are last; each entry is markdown with YAML frontmatter):\n"
            f"{_format_prior_updates_for_prompt(application)}\n"
            "\nPlease screen this candidate using the screen-candidate skill."
        )

        result = await self.run(prompt, event_stream_handler=event_stream_handler)
        output: AIReviewOutput = result.output

        await service.add_update(
            application_id=application_id,
            actor=UpdateActor.AI_AGENT,
            update_type=output.update_type,
            internal_notes=output.internal_notes,
            correspondence=output.correspondence,
            recruiter_id=None,
        )
        return output
