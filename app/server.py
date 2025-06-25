"""FastMCP server exposing finance tools and resources.

Purpose: startup entrypoint registering budget tools and Azure SQL config.
Deployment: run ``python -m app.server`` for local stdio server.
"""

from __future__ import annotations

from fastmcp import FastMCP
from fastmcp.tools import Tool
from fastmcp.prompts.prompt import PromptMessage

from app.prompts.load import load_prompt_template

from app.data.azure_sql import fetch_budget_data
from app.resources.load import resolve_resource

capabilities = {
    "resources": {"listChanged": False, "subscribe": False},
    "prompts": {"listChanged": False},
}

mcp = FastMCP()

# Register tool using metadata from @mcp_tool decorator
registration = getattr(fetch_budget_data, "_mcp_tool_registration", {})
if registration:
    tool = Tool.from_function(fetch_budget_data, **registration)
else:
    tool = Tool.from_function(fetch_budget_data)

mcp.add_tool(tool)


@mcp.prompt("variance_summary", description="Draft a narrative summary of budget variance")
def prompt_variance_summary(data: dict):
    """Render the variance summary prompt."""
    return load_prompt_template("variance_summary", data=data)


@mcp.prompt("variance_dm", description="Explain variance implications for DM")
def prompt_variance_dm(summary: str):
    """Render the deputy minister explanation prompt."""
    return load_prompt_template("variance_dm", summary=summary)


@mcp.prompt("variance_workflow", description="Multi-step variance briefing")
def prompt_variance_workflow(data: str):
    """Run the variance workflow chain."""
    return load_prompt_template("variance_workflow", data=data)


@mcp.resource("config://azure_sql", name="Azure SQL Config", mime_type="text/yaml")
def get_azure_sql_config() -> str:
    """Return the Azure SQL configuration YAML."""
    path = resolve_resource("resource://config/azure_sql")
    return open(path, "r").read()


if __name__ == "__main__":
    mcp.run("stdio")
