# 🧾 Task 002: Fetch Budget Data from Azure SQL

## 🎯 Objective
Build `fetchBudgetData(period)` to retrieve data from a read-only Azure SQL database using MCP features.

## 🔍 Input
- `period`: fiscal month or quarter (e.g. `2024-Q3`)

## 📤 Output
- Dictionary of budget and actuals per account
- Matches schema: `budgets`, `actuals`, `transactions`

## 🔧 Tool Spec
```python
@mcp_tool("fetchBudgetData")
def fetch_budget_data(period: str) -> dict:
    ...
```

## ⚙️ Tech
- Use `pyodbc` or `sqlalchemy` with secure, read-only connection string
- Optionally fallback to SQLite if not configured

## 📁 File
- Path: `app/data/azure_sql.py`

## 🔁 MCP Features
- Register with `@mcp.tool`
- Connection string as MCP `resource://config/azure_sql`
- Log query results with `logger`

## ✅ Done When
- Returns dict of structured data
- CLI and test run with MCP transport

## 🧪 Test
- Path: `tests/data/test_azure_sql.py`
- Use local mock or SQLite fallback for test mode

## 🔐 Privacy
- Read-only SQL access
- No writes or destructive actions
- Local test mode enabled