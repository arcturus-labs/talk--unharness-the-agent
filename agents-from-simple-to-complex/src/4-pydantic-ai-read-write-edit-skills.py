from pathlib import Path

from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai_harness.filesystem import FileSystem
from pydantic_ai_skills import SkillsCapability

load_dotenv(Path(__file__).resolve().parents[2] / ".env")


def main(user_prompt: str) -> None:
    project_root = Path(__file__).resolve().parents[1]

    file_tools = FileSystem(root_dir=project_root).get_toolset().filtered(
        lambda _ctx, tool_def: tool_def.name in {"read_file", "write_file", "edit_file"}
    )

    agent = Agent(
        "anthropic:claude-haiku-4-5",
        name="read_write_edit_skills_agent",
        instructions="You are a helpful assistant. Be concise.",
        toolsets=[file_tools],
        capabilities=[
            SkillsCapability(directories=[project_root / "skills"]),
        ],
    )

    result = agent.run_sync(user_prompt)
    print(f"-----------------------\nResponse: {result.output}")


if __name__ == "__main__":
    main(input("Prompt: "))
