# 🧠 Task 003: MCP Prompt Registry

## 🎯 Objective
Create a shared system for defining, loading, and registering LLM prompts using YAML and the MCP prompt API.

## 📥 Input
- YAML files in `app/prompts/` with fields: `id`, `system`, `user`

## 📤 Output
- Python helper to load prompt by ID
- Optional auto-registration to FastMCP prompt registry

## 📁 Files
- Prompts: `app/prompts/variance_summary.yaml`, etc.
- Loader: `app/prompts/load.py`

## 🔧 Example YAML
```yaml
id: variance_summary
system: |
  You are a finance analyst assistant...
user: |
  Please draft a narrative based on this variance table:
  {{ data }}
```

## 🔧 Example Loader
```python
from mcp.prompt import register_prompt_yaml

def load_prompt(id: str) -> dict:
    path = f"app/prompts/{id}.yaml"
    register_prompt_yaml(path)
    return ...  # parsed prompt object
```

## 🧠 Notes
- Prompts must be version-controlled and auditable
- Support both inline use and registration

## ✅ Done When
- `load_prompt()` returns structured prompt
- All YAMLs load and register without error

## 🧪 Test
- Add `tests/prompts/test_loader.py`
- Include at least one example prompt file