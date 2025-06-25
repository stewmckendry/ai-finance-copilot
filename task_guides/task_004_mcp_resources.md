# 🧩 Task 004: MCP Resources Registry

## 🎯 Objective
Expose common config, schema, or metadata files as formal MCP resources.

## 🧠 Spec Reference
> "Resources MUST be registered under `resource://...`, return MIME-typed payloads, and be discoverable via capability declaration."
> — [MCP Spec §3.4](https://modelcontextprotocol.io/specification/2025-06-18#resource)

## 📁 Files
- Resources path: `app/resources/**`
- Loader: `app/resources/load.py`
- Server: `scripts/register_config_resource.py`
- Tests: `tests/resources/test_loader.py`

## 🔧 Features
- `resolve_resource_uri(uri)` resolves to absolute path
- `load_resource_yaml(uri)` loads and parses YAML
- Use `@mcp.resource(...)` to expose a named config

## ✅ Done When
- Config exposed as `resource://config/azure_sql`
- Registered via FastMCP server
- Declares capabilities: `resources: { listChanged: false, subscribe: false }`
- Loadable via MCP `readResource()`

## 🧪 Test
- Call `read_resource("resource://config/azure_sql")`
- Assert `url` key in YAML returned

## 🛠 Example
```python
@mcp.resource("config://azure_sql", mime_type="text/yaml")
def get_config():
    path = resolve_resource("resource://config/azure_sql")
    return open(path).read()
```