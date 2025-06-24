"""Variance Excel ingest tool.

This module defines `parse_variance`, an MCP tool that reads Excel or CSV files
containing department variance data and returns a list of normalized rows.

Deployment: part of FastMCP server or standalone via `mcp.cli`.
Test: `pytest tests/data/test_variance_excel.py`
"""

import logging
from pathlib import Path
from typing import List, Dict

import pandas as pd
from fastmcp.server import FastMCP
from app.prompts import load_prompt

logger = logging.getLogger(__name__)

REQUIRED_COLUMNS = ["department", "program", "account", "budget", "actual", "variance"]

# FastMCP server used for registering the tool
mcp = FastMCP("Variance Parser")

# Load prompt configuration for the tool
PROMPT = load_prompt("variance_ingest")


@mcp.tool(name="parseVarianceSpreadsheet")
def parse_variance(file_path: str) -> List[Dict]:
    """Parse a variance spreadsheet and return rows as dictionaries."""
    path = Path(file_path)
    logger.info("Loading variance file", extra={"file": str(path)})
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if path.suffix.lower() in {".xlsx", ".xls"}:
        df = pd.read_excel(path)
    elif path.suffix.lower() == ".csv":
        df = pd.read_csv(path)
    else:
        raise ValueError(f"Unsupported file type: {path.suffix}")

    df.columns = [c.strip().lower() for c in df.columns]
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    df = df[REQUIRED_COLUMNS]
    rows = df.to_dict(orient="records")
    logger.info("Parsed %d rows", len(rows))
    return rows
