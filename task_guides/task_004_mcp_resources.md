# 🧩 Task 004: MCP Resources Registry

## 🎯 Objective
Expose common YAML config, schema, or metadata files as addressable MCP resources.

## 📁 Files
- Resources path: `app/resources/**`
- Loader: `app/resources/load.py`
- Tests: `tests/resources/test_loader.py`

## 🔧 Features
- `resolve_resource_uri(uri)` → absolute path (supports `resource://config/foo`, etc.)
- `load_resource_yaml(uri)` → parsed object from YAML

## 🧠 Lessons from T002
- Define the default path root in `db.py`, reuse in loader
- Support both `.yaml` and `.yml` fallback extensions
- Fail gracefully with missing file

## ✅ Done When
- Resource loader supports any URI
- Used by at least one MCP tool (e.g. T002)
- Configurable default root = `app/resources/`

## 🧪 Test
- Load working resource
- Assert expected fields (e.g. `url` in DB config)
- Check behavior on bad URI or file not found