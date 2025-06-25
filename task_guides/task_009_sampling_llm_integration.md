# ✨ Task 009: MCP Sampling + LLM Completion Integration

## 🎯 Objective
Support LLM completions by calling `sampling/createMessage` per MCP Spec §client/sampling.

## 📘 Spec Reference
> “Clients that support LLM completions MUST expose `sampling/createMessage`. Servers declare `sampling` capability and call it to receive model-generated responses.”  
> — MCP Spec: https://modelcontextprotocol.io/specification/2025-06-18/client/sampling

## 📁 Files
- Trigger: `app/narratives/generate.py`
- Prompt source: `app/prompts/*.yaml`
- Request builder: `app/prompts/sample.py`

## 🔧 Requirements
- Declare in server:
```python
capabilities = {"sampling": {"supportsStreaming": False}}
```
- Build sampling message payload using structured PromptMessage list
- Submit via `mcp.send("sampling/createMessage", payload)`
- Receive response from LLM via client

## ✅ Done When
- Tool constructs message, calls sampling
- Response is logged or used in narrative flow

## 🧪 Tests
- Sample prompt run end-to-end with mocked LLM return
- Validate message content and formatting

## 📌 Notes
- This offloads LLM calls to clients (e.g. Claude Desktop, Codex Agent)
- Enables human approval or review loop