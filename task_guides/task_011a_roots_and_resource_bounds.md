# 📂 Task 011a: MCP Roots and Resource Bounds

## 🎯 Objective
Support `roots/list` so users and tools can see which directories or URIs are available for data access.

## 📘 Spec Reference
> “The roots capability declares which URI schemes or paths are accessible. Clients MAY use `roots/list` to show available data locations.”
> — MCP Spec §client/roots: https://modelcontextprotocol.io/specification/2025-06-18/client/roots

## 📁 Files
- Server entry: `scripts/roots_server.py`
- Resource config: `app/resources/config/roots.yaml`
- Root logic: `app/storage/roots.py`

## 🔧 Requirements
- Declare capability:
```python
capabilities = {"roots": {"listChanged": False}}
```
- Implement endpoint or handler for `roots/list`
- Return list of root paths (e.g. `resource://inputs/`, `resource://samples/`)
- Integrate root filtering into data ingestion tools

## ✅ Done When
- Server returns root list from config
- Tools validate paths fall under allowed roots

## 🧪 Tests
- Simulate `roots/list` call
- Attempt access outside root and fail gracefully

## 📌 Notes
- Helps tools and UIs restrict to safe paths
- Prevents server from unintentionally pulling sensitive data