# 📊 Task 010: Compute Budget vs Actual Variances

## 🎯 Objective
Create tool `reconcileBudgetVsActual(data)` to compute variances per account, department, or program.

## 📥 Input
- Dictionary with two tables:
  - `budgets`: planned amounts
  - `actuals`: actual expenditures

## 📤 Output
- Table `variance`: variance_amount, variance_pct, flagged if over/under

## 🔧 Tool Spec
```python
@mcp_tool("reconcileBudgetVsActual")
def reconcile_budget(data: dict) -> List[dict]:
    ...
```

## 📁 File
- Path: `app/analysis/variance.py`

## 🧠 Notes
- Join on department + account
- Use consistent field names for variance_amount, variance_pct
- Flag high (>10%) or negative variances

## ✅ Done When
- Variance table produced and logged
- CLI and test runs pass

## 🧪 Test
- Path: `tests/analysis/test_variance.py`
- Uses mock budget + actuals loaded from samples