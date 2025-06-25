# 🛠️ Task 008: MCP Tool Metadata & Discovery

## 🎯 Objective
Align our MCP tools with the full requirements of MCP Spec §server/tools:
- Tool registration metadata
- Server capabilities declaration
- Client discovery and test

## 🧠 Spec Reference
> “Servers that support tools MUST declare the `tools` capability… tools MUST be returned by `tools/list`… and MAY be invoked using `tools/call`.”
> — MCP Spec §server/tools (https://modelcontextprotocol.io/specification/2025-06-18/server/tools)

## 📁 Files
- Tools: `app/data/*.py`, `app/analysis/*.py`
- Server: update FastMCP init in `scripts/*`
- Tests: `tests/tools/test_discovery.py`

## 🔧 Requirements
- Add `tools: { listChanged: false }` to MCP capabilities
- For each `@mcp.tool(...)`, provide:
  - `name`, `description`, and JSON `inputSchema`
  - Optional: `destructiveHint`, `readOnly`, `examples`
- Ensure tools return structured types or `ToolOutput`
- Register tools using structured metadata blocks if needed

## ✅ Done When
- `tools/list` returns all tools with proper metadata
- Client can discover and call `fetchBudgetData`, `reconcileBudgetVsActual`, etc.
- Test simulates discovery + call with mock input

## 🧪 Tests
- `list_tools()` and `call_tool(name, args)` with FastMCP client
- Validate JSON structure and output

## 📌 Notes
- Use `ToolInput`, `ToolOutput` if type-hinting complex inputs
- Important for LLM chaining and interface integration