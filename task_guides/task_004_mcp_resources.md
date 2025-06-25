# 🧩 Task 004: MCP Resources Registry (Updated)

## 🎯 Objective
Fully implement and test MCP resource registration and discovery per MCP Spec §3.4

## 🧠 Spec Reference
> "Servers that support resources MUST declare the `resources` capability… and expose resources via URIs with MIME‑typed payloads."
> — MCP Spec §3.4 (https://modelcontextprotocol.io/specification/2025-06-18/server/resources)

## 📁 Files
- Resources: `app/resources/config/azure_sql.yaml`, etc.
- Loader: `app/resources/load.py`
- Server: e.g. `scripts/azure_sql_server.py`
- Tests: `tests/resources/test_resources_api.py`

## 🔧 Requirements
- Add capability: `resources: { listChanged: false, subscribe: false }`
- Register resource with MCP:
```python
@mcp.resource("config://azure_sql", title="Azure SQL Config", mime_type="text/yaml")
def get_azure_sql_config():
    path = resolve_resource("resource://config/azure_sql")
    return open(path).read()
```
- List + read resources using MCP client

## ✅ Done When
- Resource shows up in `resources/list`
- `read_resource("config://azure_sql")` returns full YAML
- FastMCP server exposes metadata (URI, title, MIME)

## 🧪 Tests
- Simulate client listing and reading config resource
- Validate content and headers

## 📌 Notes
- Do not require subscribe support for MVP
- Prompts or schema files may later be exposed the same way