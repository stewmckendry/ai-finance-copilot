"""Tests for MCP tool discovery and invocation."""

import asyncio
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))

from app.server import mcp


def test_tools_list() -> None:
    tools = asyncio.run(mcp._mcp_list_tools())
    names = {t.name for t in tools}
    assert "fetchBudgetData" in names
    assert "reconcileBudgetVsActual" in names
    assert "parseVarianceSpreadsheet" in names
    fetch_tool = next(t for t in tools if t.name == "fetchBudgetData")
    assert fetch_tool.inputSchema["type"] == "object"


def test_call_reconcile() -> None:
    sample = pathlib.Path(__file__).resolve().parents[2] / "samples" / "mock_variance_input.json"
    with open(sample) as fh:
        data = json.load(fh)

    result = asyncio.run(
        mcp._mcp_call_tool("reconcileBudgetVsActual", {"data": data})
    )
    assert result[0].text.startswith("{")

