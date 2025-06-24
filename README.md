# 🧾 Finance Analyst Co-Pilot

The **Finance Analyst Co-Pilot** is an AI-powered assistant for public sector finance teams. Built using the **Model Context Protocol (MCP)**, it helps analysts streamline budget reconciliation, forecast spend, generate variance narratives, and respond to executive queries.

## 🧠 Core Capabilities

- **Variance Analysis**: Compare budgets vs actuals across periods
- **Spend Forecasting**: Detect unspent funds, predict end-of-year surpluses/deficits
- **Narrative Drafting**: Auto-generate explanatory summaries in government report formats
- **Conversational Queries**: Answer natural language questions like “Do we have money for this?”
- **Audit Trails**: Log all outputs and data flows for compliance

## 🏗️ Technical Foundation

Built using **FastMCP**, a Python implementation of the Model Context Protocol:
- Modular tools for data ingestion, analysis, narration, and interface
- Supports offline Excel, ERP (IFIS), and PDF inputs
- SQLite-based mock finance database
- Local execution with `transport=stdio` for data privacy

## 🤖 Agent Architecture

Designed for a **multi-agent setup**:
- `Data Agent`: fetches/parses Excel/ERP
- `Analysis Agent`: computes variances, forecasts
- `Narrative Agent`: drafts briefing-style summaries
- `Submission Agent`: formats and commits final outputs

## 🚀 MVP Goals

- End-to-end demo with Toronto-style report
- UI for analyst review/approval
- Codex Agent tasks with input/output specs and tests

## 📂 Repo Structure

Refer to [`AGENTS.md`](AGENTS.md) for full folder descriptions, naming conventions, and coordination guidelines.

## 🛠️ Setup

```bash
pip install -r requirements.txt
```

## 📌 Context

Initial deployment targets Ontario public sector (ministries, municipalities). Core use cases include:
- Monthly and quarterly variance reporting
- Treasury Board briefings
- Fiscal year-end spend planning

## 🔒 Privacy

Supports local-only runs for compliance-sensitive data. Designed for auditability.

## 📅 Status

Currently in MVP planning and agent task definition phase.