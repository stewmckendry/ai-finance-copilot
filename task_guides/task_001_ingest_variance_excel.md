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

## 🔁 MCP Features
- Register using `@mcp.tool`
- Use logger for parsing events
- Write prompt config to `app/prompts/variance_ingest.yaml`
- Load config or schema from MCP resource if needed

## ✅ Done When
- File is parsed and validated into row list
- Prompts loaded via helper
- CLI + test pass with MCP transport

## 🧪 Test
- Path: `tests/data/test_variance_excel.py`
- Input: `samples/sample_variance.xlsx`

## 🔐 Privacy
- Run locally only, no external data push