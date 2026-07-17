from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from .enums import UpdateActor, UpdateType


@dataclass
class Company:
    name: str
    siteUrl: str
    size: str


@dataclass
class JobOpening:
    title: str
    seniorityLevel: str
    department: str
    subDepartments: list[str]
    jobDescription: str
    company: Company


@dataclass
class ApplicationUpdate:
    timestamp: datetime
    actor: UpdateActor
    update_type: UpdateType
    internal_notes: str
    correspondence: str
    recruiter_id: str | None = None


@dataclass
class Application:
    id: str
    firstName: str
    lastName: str
    email: str
    mobile: str
    bio: str
    linkedinUrl: str
    region: str
    jobOpening: JobOpening
    updates: list[ApplicationUpdate] = field(default_factory=list)


class InMemoryApplicationService:
    def __init__(self, application: Application) -> None:
        self._application = application

    async def get_application(self, application_id: str) -> Application:
        if application_id != self._application.id:
            raise KeyError(f"Unknown application_id: {application_id}")
        return self._application

    async def add_update(
        self,
        application_id: str,
        actor: UpdateActor,
        update_type: UpdateType,
        internal_notes: str,
        correspondence: str,
        recruiter_id: str | None,
    ) -> None:
        if application_id != self._application.id:
            raise KeyError(f"Unknown application_id: {application_id}")

        self._application.updates.append(
            ApplicationUpdate(
                timestamp=datetime.now(timezone.utc),
                actor=actor,
                update_type=update_type,
                internal_notes=internal_notes,
                correspondence=correspondence,
                recruiter_id=recruiter_id,
            )
        )

    @property
    def application(self) -> Application:
        return self._application


def example_application() -> Application:
    return Application(
        id="app-doug-turnbull-001",
        firstName="Doug",
        lastName="Turnbull",
        email="doug@example.com",
        mobile="+1-555-0101",
        bio=(
            "Search relevance engineer and educator focused on information retrieval, "
            "hybrid search, learning to rank, and LLM-powered search systems."
        ),
        linkedinUrl="https://www.linkedin.com/in/softwaredoug/",
        region="Charlottesville, Virginia, United States",
        jobOpening=JobOpening(
            title="Principal Search / AI Engineer",
            seniorityLevel="Principal",
            department="ENGINEERING",
            subDepartments=["ENG_DATA", "ENG_BACKEND"],
            jobDescription=(
                "We are hiring a principal-level engineer to lead search relevance, hybrid retrieval, "
                "LLM-powered search quality, evaluation systems, and production ranking infrastructure. "
                "Strong experience with information retrieval, machine learning, Python, experimentation, "
                "and technical leadership is required."
            ),
            company=Company(
                name="Arcturus Labs",
                siteUrl="https://arcturuslabs.example.com",
                size="11-50",
            ),
        ),
        updates=[
            ApplicationUpdate(
                timestamp=datetime(2025, 7, 1, 15, 0, tzinfo=timezone.utc),
                actor=UpdateActor.HUMAN_RECRUITER,
                update_type=UpdateType.REQUEST_AI_SCREEN,
                internal_notes="Initial recruiter pass: promising fit for search relevance leadership. Requesting AI screen.",
                correspondence="",
                recruiter_id="recruiter-001",
            )
        ],
    )
