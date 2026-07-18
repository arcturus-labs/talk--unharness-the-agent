import json
from collections.abc import AsyncIterable

from pydantic_ai.messages import (
    DeferredToolRequestsEvent,
    DeferredToolResultsEvent,
    EnqueuedMessagesEvent,
    FinalResultEvent,
    FunctionToolCallEvent,
    FunctionToolResultEvent,
    OutputToolCallEvent,
    OutputToolResultEvent,
    PartDeltaEvent,
    PartEndEvent,
    PartStartEvent,
)

RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"

C_THINKING = "\033[35m"
C_TEXT = "\033[32m"
C_TOOL_CALL = "\033[33m"
C_TOOL_RESP = "\033[34m"
C_HEADER = "\033[1;37m"
C_META = "\033[90m"
C_FINAL = "\033[96m"

TRUNCATE_AT = 500


def color(c: str, text: str) -> str:
    return f"{c}{text}{RESET}"


def truncate(text: str, limit: int = TRUNCATE_AT) -> str:
    if len(text) <= limit:
        return text
    return text[:limit] + color(DIM, f"… [{len(text) - limit} chars omitted]")


def _fmt_args(raw_args: object) -> str:
    if isinstance(raw_args, str):
        try:
            raw_args = json.loads(raw_args)
        except Exception:
            return raw_args
    if isinstance(raw_args, dict):
        parts = ", ".join(f"{k}={json.dumps(v, ensure_ascii=False)}" for k, v in raw_args.items())
        return f"({parts})"
    return repr(raw_args)


def _fmt_tool_result(content: object) -> str:
    if content is None:
        return color(C_META, "(no direct content)")
    if isinstance(content, (dict, list)):
        return json.dumps(content, indent=2, ensure_ascii=False)
    text = str(content)
    return truncate(text)


def _fmt_event(event: object) -> str | None:
    if isinstance(event, PartStartEvent):
        return None

    if isinstance(event, PartDeltaEvent):
        delta_kind = getattr(event.delta, "part_delta_kind", type(event.delta).__name__)
        text = getattr(event.delta, "content_delta", None) or getattr(event.delta, "text_delta", None)
        if delta_kind == "thinking":
            return color(C_THINKING, text or "") if text else None
        if delta_kind == "text":
            return None
        return None

    if isinstance(event, PartEndEvent):
        return None

    if isinstance(event, FunctionToolCallEvent):
        part = event.part
        return color(C_TOOL_CALL, f"⚙ tool_call: {part.tool_name}{_fmt_args(part.args)}")

    if isinstance(event, FunctionToolResultEvent):
        part = event.part
        return color(C_TOOL_RESP, f"↩ tool_response: {part.tool_name}\n{_fmt_tool_result(part.content)}")

    if isinstance(event, OutputToolCallEvent):
        part = event.part
        return color(C_TOOL_CALL, f"⚙ output_tool_call: {part.tool_name}{_fmt_args(part.args)}")

    if isinstance(event, OutputToolResultEvent):
        return color(C_TOOL_RESP, "↩ output_tool_result")

    if isinstance(event, EnqueuedMessagesEvent):
        return color(C_META, f"[enqueued messages: {len(event.messages)}]")

    if isinstance(event, DeferredToolRequestsEvent):
        return color(C_META, "[deferred tool requests]")

    if isinstance(event, DeferredToolResultsEvent):
        return color(C_META, "[deferred tool results]")

    if isinstance(event, FinalResultEvent):
        return None

    return color(C_META, repr(event))


def print_prompt(prompt: str) -> None:
    print(color(C_HEADER, f"\n{'─' * 70}"))
    print(color(C_HEADER, "PROMPT"))
    print(color(C_HEADER, f"{'─' * 70}"))
    print(prompt)


def make_event_stream_printer():
    printed_header = False

    async def print_event_stream(_ctx: object, events: AsyncIterable[object]) -> None:
        nonlocal printed_header
        if not printed_header:
            print(color(C_HEADER, f"\n{'─' * 70}"))
            print(color(C_HEADER, "AGENT TRACE"))
            print(color(C_HEADER, f"{'─' * 70}\n"))
            printed_header = True
        async for event in events:
            rendered = _fmt_event(event)
            if rendered:
                print(rendered)

    return print_event_stream


def print_response(output: str) -> None:
    print(color(C_HEADER, f"\n{'─' * 70}"))
    print(color(C_HEADER, "FINAL RESPONSE"))
    print(color(C_HEADER, f"{'─' * 70}"))
    print(color(C_FINAL, output))
