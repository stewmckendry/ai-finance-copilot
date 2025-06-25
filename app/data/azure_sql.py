"""Fetch budget data from Azure SQL.

Purpose: MCP tool to load budgets, actuals and transactions for a period.
Deployment: Data Agent tool registered via FastMCP.
Config: resolves ``resource://config/azure_sql`` or ``AZURE_SQL_URL`` env var.
The ``config_uri`` parameter can override the default resource path.
Test: pytest tests/data/test_azure_sql.py
"""

from __future__ import annotations
import logging
from datetime import date

from fastmcp.contrib.mcp_mixin import mcp_tool
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from app.storage import db, models

logger = logging.getLogger(__name__)


@mcp_tool(
    name="fetchBudgetData",
    description="Load budget, actual and transaction data for the given fiscal period",
    annotations={"readOnlyHint": True},
)
def fetch_budget_data(period: str, config_uri: str = "resource://config/azure_sql") -> dict:
    """Return budget and actual data for ``period`` using ``config_uri``.

    The connection string is loaded from the given MCP resource URI, falling
    back to environment variables when not found.
    """
    engine = db.get_engine(config_uri)
    session = db.get_session(engine)

    fiscal_year = period.split("-")[0]
    result = {"budgets": [], "actuals": [], "transactions": []}

    try:
        budget_query = select(models.Budget).where(models.Budget.fiscal_year == fiscal_year)
        for row in db.paginate(session, budget_query):
            result["budgets"].append({
                "department": row.department,
                "account": row.account,
                "amount_planned": float(row.amount_planned),
                "fiscal_year": row.fiscal_year,
            })

        actual_query = select(models.Actual).where(models.Actual.fiscal_period == period)
        for row in db.paginate(session, actual_query):
            result["actuals"].append({
                "department": row.department,
                "account": row.account,
                "amount_actual": float(row.amount_actual),
                "fiscal_period": row.fiscal_period,
            })

        year_prefix = f"{fiscal_year}-"
        txn_query = select(models.Transaction).where(models.Transaction.date.like(f"{year_prefix}%"))
        for row in db.paginate(session, txn_query):
            result["transactions"].append({
                "account": row.account,
                "date": row.date.isoformat() if isinstance(row.date, date) else str(row.date),
                "amount": float(row.amount),
                "description": row.description,
            })
    except SQLAlchemyError as e:
        logger.error("Database error: %s", e)
        raise
    finally:
        session.close()

    return result
