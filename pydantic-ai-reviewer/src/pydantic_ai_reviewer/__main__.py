from __future__ import annotations

import asyncio
import json
import os
from collections.abc import AsyncIterable
from dataclasses import asdict, is_dataclass

from dotenv import load_dotenv
from pydantic_ai.messages import (
    DeferredToolRequestsEvent,
    DeferredToolResultsEvent,
    EnqueuedMessagesEvent,
    FinalResultEvent,
    FunctionToolCallEvent,
    FunctionToolResultEvent,
    ModelResponseStreamEvent,
    OutputToolCallEvent,
    OutputToolResultEvent,
    PartDeltaEvent,
    PartEndEvent,
    PartStartEvent,
)

from .ai_reviewer import AIReviewer
from .models import InMemoryApplicationService, example_application


def require_anthropic_api_key() -> str:
    load_dotenv()
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise SystemExit(
            "ANTHROPIC_API_KEY is required. Add it to pydantic-ai-reviewer/.env and run again."
        )
    return api_key


def format_event(event: object) -> str:
    if isinstance(event, PartStartEvent):
        part_kind = getattr(event.part, "part_kind", type(event.part).__name__)
        return f"PART_START index={event.index} kind={part_kind}"
    if isinstance(event, PartDeltaEvent):
        delta_kind = getattr(event.delta, "part_delta_kind", type(event.delta).__name__)
        text = getattr(event.delta, "content_delta", None) or getattr(event.delta, "text_delta", None)
        return f"PART_DELTA index={event.index} kind={delta_kind} text={text!r}"
    if isinstance(event, PartEndEvent):
        part_kind = getattr(event.part, "part_kind", type(event.part).__name__)
        return f"PART_END index={event.index} kind={part_kind}"
    if isinstance(event, FinalResultEvent):
        return f"FINAL_RESULT tool_name={event.tool_name!r} tool_call_id={event.tool_call_id!r}"
    if isinstance(event, FunctionToolCallEvent):
        return f"FUNCTION_TOOL_CALL\n{json.dumps(asdict(event), indent=2, default=str)}"
    if isinstance(event, FunctionToolResultEvent):
        return f"FUNCTION_TOOL_RESULT\n{json.dumps(asdict(event), indent=2, default=str)}"
    if isinstance(event, OutputToolCallEvent):
        return f"OUTPUT_TOOL_CALL\n{json.dumps(asdict(event), indent=2, default=str)}"
    if isinstance(event, OutputToolResultEvent):
        return f"OUTPUT_TOOL_RESULT\n{json.dumps(asdict(event), indent=2, default=str)}"
    if isinstance(event, EnqueuedMessagesEvent):
        return f"ENQUEUED_MESSAGES count={len(event.messages)}"
    if isinstance(event, DeferredToolRequestsEvent):
        return f"DEFERRED_TOOL_REQUESTS\n{json.dumps(asdict(event), indent=2, default=str)}"
    if isinstance(event, DeferredToolResultsEvent):
        return f"DEFERRED_TOOL_RESULTS\n{json.dumps(asdict(event), indent=2, default=str)}"
    if isinstance(event, ModelResponseStreamEvent):
        return f"MODEL_RESPONSE_STREAM\n{json.dumps(asdict(event), indent=2, default=str)}"
    if hasattr(event, "model_dump"):
        return f"{type(event).__name__}\n{json.dumps(event.model_dump(mode='json'), indent=2)}"
    if is_dataclass(event):
        return f"{type(event).__name__}\n{json.dumps(asdict(event), indent=2, default=str)}"
    return repr(event)


def make_event_stream_printer():
    printed_header = False

    async def print_event_stream(_ctx: object, events: AsyncIterable[object]) -> None:
        nonlocal printed_header
        if not printed_header:
            print("Agent event stream:\n")
            printed_header = True
        async for event in events:
            print(format_event(event))

    return print_event_stream


async def main() -> None:
    require_anthropic_api_key()

    application = example_application()
    service = InMemoryApplicationService(application)
    reviewer = AIReviewer()

    output = await reviewer.review(
        application.id,
        service,
        event_stream_handler=make_event_stream_printer(),
    )

    print("\nAI reviewer output:\n")
    print(json.dumps(output.model_dump(mode="json"), indent=2))

    print("\nStored application updates:\n")
    for update in service.application.updates:
        print(json.dumps({
            "timestamp": update.timestamp.isoformat(),
            "actor": update.actor.value,
            "update_type": update.update_type.value,
            "internal_notes": update.internal_notes,
            "correspondence": update.correspondence,
            "recruiter_id": update.recruiter_id,
        }, indent=2))


if __name__ == "__main__":
    asyncio.run(main())
