"""FastMCP server exposing the parse_variance tool.

Deployment: ``PYTHONPATH=. fastmcp run scripts/variance_server.py:server --transport stdio``
Test: ``pytest -q``
"""

from app.data.variance_excel import mcp as server

if __name__ == "__main__":
    server.run()
