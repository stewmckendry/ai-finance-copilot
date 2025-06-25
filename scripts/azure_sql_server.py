"""FastMCP server exposing finance tools and config resource.

Deployment: ``PYTHONPATH=. fastmcp run scripts/azure_sql_server.py:server --transport stdio``
Test: ``pytest -q``
"""

from app.server import mcp as server

if __name__ == "__main__":
    server.run("stdio")
