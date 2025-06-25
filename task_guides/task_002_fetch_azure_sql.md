# 🧾 Task 002: Fetch Budget Data from Azure SQL

## 🎯 Objective
Build `fetchBudgetData(period)` to retrieve structured budget + actuals data from a read-only Azure SQL Server database using MCP standards.

## 📥 Input
- `period`: fiscal month or quarter (e.g. `2024-Q3`)

## 📤 Output
- Dictionary matching MCP schema:
  - `budgets`: [{ department, account, amount_planned, fiscal_year }]
  - `actuals`: [{ department, account, amount_actual, fiscal_period }]
  - `transactions`: [{ account, date, amount, description }]

## 📁 File Locations
- Tool logic: `app/data/azure_sql.py`
- DB helpers: `app/storage/db.py`
- ORM schema: `app/storage/models.py`
- SQL schema: `app/storage/schema.sql`

## 🔧 Tool Spec
```python
@mcp_tool("fetchBudgetData")
def fetch_budget_data(period: str, config_uri: str = "resource://config/azure_sql") -> dict:
    ...
```

## 🔁 MCP Features
- Use `@mcp.tool`
- Config path: `resource://config/azure_sql`
- Optional `config_uri` parameter overrides the path
- Log all DB queries
  - Falls back to `AZURE_SQL_URL` or `SQLITE_URL` environment variables

## ⚙️ Implementation Notes
- Use `SQLAlchemy` for DB access and connection pooling
- Define ORM models in `models.py`
- Write schema for those tables as `schema.sql`
- Centralize engine/session helpers in `db.py`
- Handle pagination and connection errors

## ✅ Done When
- Query returns clean, JSON-serializable dict
- Matches model schema
- Supports test fallback to SQLite

## 🧪 Test
- Path: `tests/data/test_azure_sql.py`
- Mock SQLite db w/ matching schema
- Validate correct records returned for fiscal period

## 🔐 Privacy
- No writes; read-only credential access only