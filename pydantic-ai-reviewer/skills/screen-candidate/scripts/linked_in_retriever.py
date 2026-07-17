from __future__ import annotations

import re
from functools import lru_cache
from pathlib import Path

_PROFILE_DATA_DIR = Path(__file__).resolve().parent / "data" / "linked_in_profiles"
_NO_RESULT_NAMES = {"johnberryman"}


class LinkedInLookupError(Exception):
    pass


def _normalize_name(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.lower())


@lru_cache(maxsize=1)
def _profile_index() -> dict[str, Path]:
    if not _PROFILE_DATA_DIR.exists() or not _PROFILE_DATA_DIR.is_dir():
        raise LinkedInLookupError(f"LinkedIn profile data directory not found: {_PROFILE_DATA_DIR}")

    index: dict[str, Path] = {}
    for path in _PROFILE_DATA_DIR.glob("*.md"):
        index[_normalize_name(path.stem)] = path
    return index


def _lookup_profile_path(first_name: str, last_name: str) -> Path | None:
    normalized_full_name = _normalize_name(f"{first_name}{last_name}")
    if normalized_full_name in _NO_RESULT_NAMES:
        return None
    return _profile_index().get(normalized_full_name)


async def get_linkedin_profile(
    first_name: str,
    last_name: str,
    company_name: str | None = None,
    company_url: str | None = None,
    linked_in_username: str | None = None,
    message_history: list[object] | None = None,
) -> str:
    del company_name, company_url, linked_in_username, message_history

    try:
        profile_path = _lookup_profile_path(first_name, last_name)
    except LinkedInLookupError as exc:
        return f"ERROR: {exc}"

    if profile_path is None:
        return (
            f"ERROR: Could not find a LinkedIn profile for '{first_name} {last_name}'. "
            "No local profile data found."
        )

    return profile_path.read_text(encoding="utf-8")
