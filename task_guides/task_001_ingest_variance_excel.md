# 🧾 Task 001: Ingest IFIS/Variance Excel Files

## 🎯 Objective
Build a FastMCP-compatible tool `parseVarianceSpreadsheet(file)` that loads an Excel or CSV file representing a department’s variance report.

## 🔍 Input
- Excel file with budget, actuals, and variance columns
- Fields: department, program, account, budget, actual, variance

## 📤 Output
- List of rows as structured JSON objects
- Parsed into normalized schema: `budgets`, `actuals`, `variance`

## 📁 File
- Path: `app/data/variance_excel.py`

## 🔧 Tool Spec
```python
@mcp_tool("parseVarianceSpreadsheet")
def parse_variance(file_path: str) -> List[dict]:
    ...
```

## 🧠 Notes
- Support both `.xlsx` and `.csv`
- Include test Excel file and output sample
- Log parsing steps with `logger`

## ✅ Done When
- File is parsed and validated into row list
- Supports CLI run + test case
- Included in toolchain registry

## 🧪 Test
- Path: `tests/data/test_variance_excel.py`
- Input: `samples/sample_variance.xlsx`