🤖 Codex Agent Guide: ai-finance-copilot

Welcome to the **Codex Agent workspace** for the Finance Analyst Co-Pilot.
This file provides instructions, standards, and practices for agents contributing to this codebase.

---

## 🗂️ Repo Structure

| Folder               | Purpose                                     |
|----------------------|---------------------------------------------|
| `app/data/`          | Budget and actuals importers, recon tools   |
| `app/analysis/`      | Variance calculations, fund forecasting     |
| `app/narratives/`    | Narrative generation and LLM prompts        |
| `app/queries/`       | Conversational budget query tools           |
| `app/interface/`     | CLI or UI interaction logic                 |
| `app/prompts/`       | YAML-based LLM prompt templates             |
| `app/resources/`     | MCP-accessible config and metadata          |
| `scripts/`           | CLI utilities and tool test runners         |
| `task_guides/`       | Task instructions and review reports        |
| `tests/`             | Unit tests for each component               |

## 🔁 Naming Conventions

- Task prompts: `task_guides/task_<ID>_<desc>.md`
- Review reports: `task_guides/reports/task_<ID>_<desc>_report.md`
- Module names reflect function: `variance.py`, `narratives.py`, etc.

## ✅ Agent Checklists

Agents should consult `task_guides/review_checklist.md` before submitting.

Each task should include:
- Input/output specification
- Test with mock or isolated data
- Sample output or log line
- Summary of implementation
- Key design decisions and trade-offs

## 📦 Requirements

Install all packages with:
```bash
pip install -r requirements.txt
```

Update `requirements.txt` with any new packages required by your code.
Update `.env-example` with any new required environment variables.

## 🤝 Coordination

Agents are expected to:
- Use `main` or sandbox branch assigned to their task
- Commit only their assigned files
- Link work to task prompts in `task_guides/`

---

## 🧱 Development Standards

To ensure quality and consistency:

- Use **FastMCP** (https://github.com/modelcontextprotocol/python-sdk) for tool orchestration.
- Use `gemini` via Google’s Python SDK for LLM calls.
- Define **prompts in YAML** files in `app/prompts/`, load using helper.
- Define MCP **resources** in `app/resources/` for config/schema.
- Reuse shared helpers for parsing, logging, and I/O.
- Modularize functionality into logical Python modules.
- Use `logger` to track progress and handle errors.
- Add header comment to each file with its purpose, deployment and test commands.
- Place scripts for testing tools or agents in `scripts/`, named by task or function.