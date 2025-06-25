# 🔁 Task 003b: Prompt Arguments & Multi-Step Workflows

## 🎯 Objective
Extend prompt support to:
- Handle `arguments` properly in prompt YAMLs
- Return `PromptMessage[]` from `prompts/get`
- Enable multi-step prompt workflows (toolchaining)

## 🧠 Spec Reference
> “Prompt definitions SHOULD include `arguments` to support dynamic injection. Each call to `prompts/get` MUST return a list of `PromptMessage` with roles.”
> — MCP Spec §server/prompts (https://modelcontextprotocol.io/specification/2025-06-18/server/prompts)

## 📁 Files
- Prompt definitions: `app/prompts/*.yaml`
- Prompt server: `scripts/prompts_server.py`
- Prompt utility: `app/prompts/load.py`
- Workflow engine (optional): `app/prompts/chain.py`

## 🔧 Requirements
- Add `arguments` schema to YAML:
```yaml
arguments:
  - name: data_uri
    type: string
    required: true
```
- Prompt handler must:
  - Accept args (like `data_uri`)
  - Inject args into messages
  - Return `PromptMessage[]` with role annotations

## 🔁 Workflow Support
- Define YAML with `steps:` section (optional)
- Each step references a named prompt and arguments
- Chain can be executed via `PromptChain.run()`

## ✅ Done When
- `prompts/get(name, args)` returns valid messages
- PromptMessage list includes both `system` and `user`
- (Optional) Chain demo executes multiple prompt steps

## 🧪 Test
- Load and render prompt with argument substitution
- Chain 2-step prompt using test input

## 📌 Examples
- Step 1: summarize variance data
- Step 2: explain implications to deputy minister