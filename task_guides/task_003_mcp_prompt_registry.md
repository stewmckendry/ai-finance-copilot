# 🧠 Task 003: MCP Prompt Registry (Updated)

## 🎯 Objective
Fully implement prompt support per MCP Spec §server/prompts:
- register prompts with `@mcp.prompt(...)`
- support listing (`prompts/list`) and retrieving (`prompts/get`)

## 🧠 Spec Reference
> “Servers that support prompts MUST declare the `prompts` capability… Clients send `prompts/list` and `prompts/get` to interact with prompts.”  
> — MCP Spec §server/prompts (https://modelcontextprotocol.io/specification/2025-06-18/server/prompts)

## 📁 Files
- Prompts: `app/prompts/*.yaml`
- Loader: `app/prompts/load.py`
- Server: update script to include capability and registration
- Tests: `tests/prompts/test_prompts_api.py`

## 🔧 Requirements
- On server init:
  ```python
  mcp = FastMCP(...,
      capabilities={ "prompts": {"listChanged": False} }
  )
  ```
- Each prompt YAML includes:
  ```yaml
  id: variance_summary
  title: "Variance Summary"
  description: "Draft a narrative summary of budget variance"
  arguments:
    - name: data
      description: "Budget vs actual data table"
      required: true
  system: |
    ...
  user: |
    ...
  ```
- Register with:
  ```python
  @mcp.prompt("variance_summary", title="Variance Summary", description="...")
  def prompt_variance_summary(data: dict):
      return load_prompt_template(...)  # returns list of PromptMessage objects
  ```

## ✅ Done When
- `prompts/list` shows prompt metadata
- `prompts/get` returns structured messages with roles
- Passing tests: list and get work as expected

## 🧪 Tests
- Test client listing shows names/titles
- Test get returns correct messages given sample arguments