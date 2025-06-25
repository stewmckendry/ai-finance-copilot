"""Database helpers for Azure SQL and SQLite.

Purpose: Provide engine and session creation with query logging.
Deployment: Used by data tools to connect to DB.
Test: pytest tests/data/test_azure_sql.py
"""

from __future__ import annotations
import logging
import os
from pathlib import Path
from typing import Any, Iterable

from app.resources.load import resolve_resource

import yaml
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker, Session

logger = logging.getLogger(__name__)

CONFIG_URI = "resource://config/azure_sql"
PAGE_SIZE = 500


def resolve_resource_uri(uri: str) -> Path:
    """Resolve a ``resource://`` URI using :func:`app.resources.load.resolve_resource`."""
    return resolve_resource(uri)

def load_config(uri: str = CONFIG_URI) -> dict[str, Any]:
    """Load YAML config from a ``resource://`` URI or filesystem path."""
    path = resolve_resource_uri(uri)
    if path.exists():
        with open(path) as f:
            return yaml.safe_load(f) or {}
    return {}


def get_engine(url: str | None = None) -> Engine:
    """Return SQLAlchemy engine, resolving ``resource://`` URLs when provided.

    If ``url`` is not supplied, environment variables ``SQLITE_URL`` or
    ``AZURE_SQL_URL`` are used. Otherwise configuration is loaded from
    ``resource://config/azure_sql``.
    """
    if url and url.startswith("resource://"):
        cfg = load_config(url)
        url = cfg.get("url")
    if url is None:
        url = os.getenv("SQLITE_URL") or os.getenv("AZURE_SQL_URL")
        if not url:
            cfg = load_config()
            url = cfg.get("url")
    logger.debug("Creating engine for %s", url)
    engine = create_engine(url, pool_pre_ping=True, echo=False)
    return engine


def get_session(engine: Engine | None = None) -> Session:
    if engine is None:
        engine = get_engine()
    SessionLocal = sessionmaker(bind=engine)
    return SessionLocal()


def paginate(session: Session, query) -> Iterable[Any]:
    offset = 0
    while True:
        chunk = session.execute(query.limit(PAGE_SIZE).offset(offset)).scalars().all()
        if not chunk:
            break
        logger.debug("Fetched %s records", len(chunk))
        for row in chunk:
            yield row
        offset += PAGE_SIZE
