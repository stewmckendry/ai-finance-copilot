"""Tests for FastMCP prompt registry."""

import pathlib
import sys

import asyncio

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))

from app.server import mcp


def test_prompts_list() -> None:
    prompts = asyncio.run(mcp._mcp_list_prompts())
    names = {p.name for p in prompts}
    assert "variance_summary" in names
    variance = next(p for p in prompts if p.name == "variance_summary")
    assert variance.description.startswith("Draft")


def test_prompts_get() -> None:
    result = asyncio.run(
        mcp._mcp_get_prompt(
            "variance_summary",
            {"data": '{"dept": "A", "variance": "over"}'}
        )
    )
    assert result.description.startswith("Draft")
    assert result.messages[0].role == "user"
    assert "dept'" in result.messages[-1].content.text

    chain = asyncio.run(
        mcp._mcp_get_prompt(
            "variance_workflow",
            {"data": '{"dept": "A", "variance": "over"}'}
        )
    )
    assert len(chain.messages) > 2
