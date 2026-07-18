from pathlib import Path

from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai_harness.filesystem import FileSystem
from pydantic_ai_harness.shell import Shell

from event_logging import make_event_stream_printer, print_prompt, print_response

load_dotenv(Path(__file__).resolve().parents[2] / ".env")

def main(user_prompt: str) -> None:
    project_root = Path(__file__).resolve().parents[2] / "scratch_space"

    file_tools = FileSystem(root_dir=project_root).get_toolset().filtered(
        lambda _ctx, tool_def: tool_def.name in {"read_file", "write_file", "edit_file"}
    )
    shell_tools = Shell(cwd=project_root).get_toolset().filtered(
        lambda _ctx, tool_def: tool_def.name == "run_command"
    )

    agent = Agent(
        "anthropic:claude-haiku-4-5",
        name="read_write_edit_skills_agent",
        retries=3,
        instructions="You are a helpful assistant. Be concise.",
        toolsets=[file_tools, shell_tools],
    )

    print_prompt(user_prompt)
    result = agent.run_sync(user_prompt, event_stream_handler=make_event_stream_printer())
    print_response(result.output)


if __name__ == "__main__":
    main(input("Prompt: "))
