"""Budget vs actual variance computation.

Purpose: MCP tool to reconcile budgets and actuals at the account level.
Deployment: part of FastMCP server or standalone CLI.
Test: ``pytest tests/analysis/test_variance.py``
"""

from __future__ import annotations

import logging
from typing import List

from fastmcp.contrib.mcp_mixin import mcp_tool

logger = logging.getLogger(__name__)


def _safe_pct(numerator: float, denominator: float) -> float:
    """Return percentage safely, avoiding divide-by-zero."""
    if denominator == 0:
        return 0.0
    return round((numerator / denominator) * 100, 2)


@mcp_tool(
    name="reconcileBudgetVsActual",
    description="Compute variances between planned and actual amounts",
    annotations={"readOnlyHint": True},
)
def reconcile_budget(data: dict) -> dict:
    """Compute account-level variance between budgets and actuals.

    ``data`` must contain lists under ``budgets`` and ``actuals`` with
    ``account`` identifiers and numeric amounts ``amount_planned`` and
    ``amount_actual`` respectively.
    """
    if not isinstance(data, dict):
        raise TypeError("Input must be a dict")

    budgets: List[dict] = data.get("budgets") or []
    actuals: List[dict] = data.get("actuals") or []

    if not isinstance(budgets, list) or not isinstance(actuals, list):
        raise ValueError("'budgets' and 'actuals' must be lists")

    logger.info("Reconciling %d budget rows and %d actual rows", len(budgets), len(actuals))

    budget_map: dict[str, dict] = {}
    for b in budgets:
        acct = b.get("account")
        if acct is None:
            raise ValueError("Budget row missing 'account'")
        if "amount_planned" not in b:
            raise ValueError("Budget row missing 'amount_planned'")
        budget_map[acct] = b

    actual_totals: dict[str, float] = {}
    for a in actuals:
        acct = a.get("account")
        if acct is None:
            raise ValueError("Actual row missing 'account'")
        if "amount_actual" not in a:
            raise ValueError("Actual row missing 'amount_actual'")
        actual_totals[acct] = actual_totals.get(acct, 0.0) + float(a.get("amount_actual", 0.0))

    variance_rows: List[dict] = []

    processed_accounts = set()

    for acct, b in budget_map.items():
        planned = float(b.get("amount_planned", 0.0))
        actual = actual_totals.get(acct, 0.0)
        variance = actual - planned
        pct = _safe_pct(variance, planned)
        flag = "ok"
        if variance > 0:
            flag = "over"
        elif variance < 0:
            flag = "under"

        variance_rows.append(
            {
                "account": acct,
                "variance_amount": variance,
                "variance_pct": pct,
                "flag": flag,
            }
        )
        processed_accounts.add(acct)

    # Handle actuals without corresponding budget
    for acct, actual in actual_totals.items():
        if acct in processed_accounts:
            continue
        variance_rows.append(
            {
                "account": acct,
                "variance_amount": actual,
                "variance_pct": 0.0,
                "flag": "over",
            }
        )

    total_variance = sum(v["variance_amount"] for v in variance_rows)
    logger.info(
        "Computed variance for %d accounts (total %.2f)",
        len(variance_rows),
        total_variance,
    )

    return {"variance": variance_rows}
