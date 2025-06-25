# 🧠 Task 003: MCP Prompt Registry

## 🎯 Objective
Create loader and registry for YAML-based LLM prompts using MCP conventions.

## 📁 Files
- Prompts: `app/prompts/*.yaml`
- Loader: `app/prompts/load.py`
- Tests: `tests/prompts/test_loader.py`

## 📥 Prompt Format
```yaml
id: variance_summary
system: "You are a finance assistant..."
user: "Summarize this table: {{ data }}"
```

## 🔧 Features
- `load_prompt(id: str)` loads YAML and returns `dict`
- Optionally register with MCP via `register_prompt_yaml(path)`
- Document each prompt's use case

## 🧠 Lessons from T001
- Ensure prompts are either:
  - For LLM use (and registered properly)
  - Or purely metadata (and stored as MCP resource)
- Avoid including unused prompts in tool code

## ✅ Done When
- `load_prompt()` supports structured field return
- `register_prompt_yaml()` is optional
- Loader fails gracefully if file missing

## 🧪 Test
- Include one working and one broken prompt YAML
- Test `load_prompt("variance_summary")` returns both fields