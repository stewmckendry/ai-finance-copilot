# 🧾 Task 002: Fetch Budget Data from Azure SQL

## 🎯 Objective
Build `fetchBudgetData(period)` to retrieve data from a read-only Azure SQL database.

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
- Use `pyodbc` or `sqlalchemy` with read-only connection string
- Include fallback to local SQLite for testing

## 📁 File
- Path: `app/data/azure_sql.py`

## 🧠 Notes
- Use config file for connection params
- Log query and response stats

## ✅ Done When
- Returns dict of structured data
- Supports CLI run + test case

## 🧪 Test
- Path: `tests/data/test_azure_sql.py`
- Mock DB or stub with SQLite fallback