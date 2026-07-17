# pydantic-ai-reviewer

A standalone version of the candidate-screening agent from:

- `talk--english-the-language-of-ai/backend/app/services/ai_reviewer.py`

It keeps the same core shape:

- `AIReviewer` as a Pydantic AI agent
- `SkillsCapability` pointed at a local `skills/` directory
- a `get_linkedin_profile` tool backed by local markdown fixtures
- a runnable `__main__` that screens a Doug Turnbull example application

## Run

From this directory:

```bash
uv run python -m pydantic_ai_reviewer
```

`__main__` automatically loads `.env` from the example root via `python-dotenv`.

`ANTHROPIC_API_KEY` is required. If it is missing, the program exits immediately with a clear error.

When you run it, it prints the agent event stream first, then the final structured output, then the stored application updates.
