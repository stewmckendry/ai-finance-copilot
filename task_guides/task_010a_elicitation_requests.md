# 🧠 Task 010a: MCP Elicitation Requests

## 🎯 Objective
Enable user input requests via `elicitation/create`, allowing structured clarification mid-task.

## 📘 Spec Reference
> "Servers that support user prompts SHOULD use `elicitation/create`… providing a schema, description, and example inputs.”  
> — MCP Spec §client/elicitation: https://modelcontextprotocol.io/specification/2025-06-18/client/elicitation

## 📁 Files
- Usage: `app/analysis/forecast.py`, `app/interface/ask_user.py`
- Request builder: `app/elicitation/schema.py`
- Server config: `scripts/elicitation_server.py`

## 🔧 Requirements
- Declare capability:
```python
capabilities = {"elicitation": {"supportsForms": True}}
```
- Construct `elicitation/create` payload:
```json
{
  "schema": {"type": "object", "properties": {"department": {"type": "string"}}},
  "description": "Which department should we analyze?",
  "examples": [{"department": "Health"}]
}
```
- Handle returned input and route to next step

## ✅ Done When
- Tool issues an elicitation request
- User-supplied value is received and used

## 🧪 Tests
- Simulate form-style input roundtrip
- Validate input schema and result parsing

## 📌 Use Cases
- Ask user to pick target program
- Collect missing parameters like fiscal date range