"""Tests for FastMCP resource registry."""

import asyncio
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))

from app.server import mcp


def test_resources_list() -> None:
    resources = asyncio.run(mcp._mcp_list_resources())
    uris = {str(r.uri) for r in resources}
    assert "config://azure_sql" in uris
    azure = next(r for r in resources if str(r.uri) == "config://azure_sql")
    assert azure.name == "Azure SQL Config"
    assert azure.mimeType == "text/yaml"


def test_read_azure_sql_config() -> None:
    contents = asyncio.run(mcp._mcp_read_resource("config://azure_sql"))
    assert contents[0].content.strip().startswith("# Azure SQL connection configuration")
