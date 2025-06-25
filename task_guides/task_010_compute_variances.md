# 📊 Task 010: Compute Budget vs Actual Variances

## 🎯 Objective
Build MCP tool `reconcileBudgetVsActual(data)` to compute account-level variances.

## 📥 Input
```json
{
  "budgets": [{"account": "A", "amount_planned": 10000, ...}],
  "actuals": [{"account": "A", "amount_actual": 9000, ...}]
}
```

## 📤 Output
```json
{
  "variance": [
    {
      "account": "A",
      "variance_amount": -1000,
      "variance_pct": -10.0,
      "flag": "under"
    },
    ...
  ]
}
```

## 🔧 Tool Spec
```python
@mcp_tool("reconcileBudgetVsActual")
def reconcile_budget(data: dict) -> dict:
    ...
```

## 📁 Files
- Tool logic: `app/analysis/variance.py`
- Tests: `tests/analysis/test_variance.py`

## 🔁 MCP Features
- Use `@mcp_tool`
- Log record counts and summary stats
- Validate input format and handle missing account matches
- Document input schema as MCP resource (later)

## ✅ Done When
- Matches budgets and actuals by account
- Computes signed difference + pct
- Flags variance as `over`, `under`, or `ok`
- Passes CLI and pytest with mock data

## 🧪 Test
- Load mock data from `samples/mock_variance_input.json`
- Assert variance amounts and flags

## 📌 Notes
- Use float formatting for percent (e.g. `-12.5`) and safe divide
- Consider edge cases: zero budgets, missing actuals
- Reuse across forecasting tool later