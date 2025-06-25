"""Resource resolution helpers.

Purpose: resolve resource:// URIs within ``app/resources``.
Deployment: Imported by DB helpers and MCP server.
"""

from __future__ import annotations
from pathlib import Path

RESOURCE_ROOT = Path(__file__).resolve().parent


def resolve_resource(uri: str) -> Path:
    """Return absolute path for a ``resource://`` URI or local path."""
    if uri.startswith("resource://"):
        relative = uri[len("resource://") :]
        path = RESOURCE_ROOT / relative
        if path.is_dir():
            return path
        if not path.suffix:
            path = path.with_suffix(".yaml")
        return path
    return Path(uri)
