from __future__ import annotations

import asyncio
import os

from dotenv import load_dotenv

from .ai_reviewer import AIReviewer
from .event_logging import make_event_stream_printer, print_review_input, print_review_output
from .models import example_application


def require_anthropic_api_key() -> None:
    load_dotenv()
    if not os.environ.get("ANTHROPIC_API_KEY"):
        raise SystemExit(
            "ANTHROPIC_API_KEY is required. Add it to pydantic-ai-reviewer/.env and run again."
        )


async def main() -> None:
    require_anthropic_api_key()

    reviewer = AIReviewer()
    application = example_application()
    print_review_input(application)
    output = await reviewer.review(
        application,
        event_stream_handler=make_event_stream_printer(),
    )
    print_review_output(output)


if __name__ == "__main__":
    asyncio.run(main())
