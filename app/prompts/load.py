"""Prompt loading utilities.

Purpose: load YAML prompt templates and render ``PromptMessage`` objects.
Deployment: imported by server at startup to register prompts.
Test: ``pytest tests/prompts/test_prompts_api.py``
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml
from mcp.types import PromptMessage, TextContent

PROMPT_DIR = Path(__file__).parent


def load_prompt(name: str) -> dict[str, Any]:
    """Return YAML data for the given prompt name."""
    path = PROMPT_DIR / f"{name}.yaml"
    with open(path, "r", encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


def load_prompt_template(name: str, **kwargs: Any) -> list[PromptMessage]:
    """Render a YAML prompt template into ``PromptMessage`` objects."""
    data = load_prompt(name)
    messages: list[PromptMessage] = []

    def _format(value: str) -> str:
        try:
            return value.format(**kwargs)
        except Exception:
            return value

    if "system" in data:
        messages.append(
            PromptMessage(role="user", content=TextContent(type="text", text=_format(data["system"])))
        )
    if "user" in data:
        messages.append(
            PromptMessage(role="user", content=TextContent(type="text", text=_format(data["user"])))
        )
    if "assistant" in data:
        messages.append(
            PromptMessage(role="assistant", content=TextContent(type="text", text=_format(data["assistant"])))
        )
    for msg in data.get("messages", []):
        role = msg.get("role", "user")
        content = _format(msg.get("content", ""))
        messages.append(PromptMessage(role=role, content=TextContent(type="text", text=content)))

    return messages
