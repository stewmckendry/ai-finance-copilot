# 📘 Finance Analyst Co-Pilot: Concept Document

## 🔸 Executive Summary (for Government Officials)

Modern government departments face mounting complexity in managing budgets, tracking expenditures, and delivering timely financial insights to leadership. Financial analysts are burdened with compiling data from multiple systems, performing manual reconciliations, and drafting periodic reports—all while ensuring compliance, transparency, and responsiveness.

The **Finance Analyst Co-Pilot** is an AI-powered assistant designed to augment public sector finance teams by automating routine financial data tasks and helping analysts deliver timely, accurate insights to decision-makers. Built using the **Model Context Protocol (MCP)**, the Co-Pilot integrates multiple data sources, applies structured logic and AI reasoning, and supports human-in-the-loop workflows for verification and compliance.

The Co-Pilot will initially focus on supporting:
- **Monthly, quarterly, and year-end budget vs actual variance reporting**
- **Spend forecasting and unused fund detection**
- **Narrative drafting for internal reports and Treasury Board briefings**
- **Conversational querying of budget data (e.g., "Do we have money for this?")**

The pilot will target the Ontario public sector context, reflecting its financial systems, reporting cycles, and offline/ERP data mix.

---

## 🏧 Use Case Background

### Core Problems:
- Finance leaders frequently ask: 
  - "Do we have money for this?"
  - "Where are we against budget?"
  - "Where do we have excess funds?"
  - "What must we spend before fiscal year end?"
- Analysts spend time gathering data across:
  - **IFIS**, **Hyperion**, **SAP/Oracle**, Excel files
  - PDF briefings and council reports
- Reporting is highly manual, recurring, and deadline-driven.

### Target Users:
- Ministry/Agency Financial Analysts
- Controllers/ADM-level finance officers
- Internal audit and CoA support staff

---

## 🧐 MVP Vision

An AI co-pilot that:
1. Connects to data exports from IFIS, Excel spreadsheets, and other formats
2. Analyzes budget vs actuals and highlights variances
3. Drafts narrative summaries in the format of real Ontario variance reports
4. Supports user review and approvals
5. Logs all activity for auditability
6. Answers executive-style budget questions via natural language

---

## ⚙️ AI-Native Technical Architecture

### MCP Tool Chain (FastMCP + Gemini/GPT)

| Tool Name | Function |
|-----------|----------|
| `fetchBudgetData(period)` | Load data from simulated IFIS/ERP exports |
| `parseVarianceSpreadsheet(file)` | Ingest Excel or CSV variance data |
| `reconcileBudgetVsActual(data)` | Compute variances per account/program |
| `identifyUnspentFunds(data, cutoff_date)` | Flag at-risk budget lines |
| `draftVarianceNarrative(data)` | Generate LLM-assisted summary explanation |
| `commitDraftReport(location)` | Save to Git, Notion, or shareable file location |
| `queryBudget(question)` | Respond to natural language queries using structured financial data |

---

### Simulated Database Schema

| Table | Key Fields |
|-------|------------|
| `budgets` | id, department, account, fund, amount_planned, fiscal_year |
| `actuals` | id, account, department, amount_actual, fiscal_period |
| `variance` | id, budget_id, actual_id, variance_amount, variance_pct |
| `transactions` | id, account, date, amount, description |

---

## 🔐 Data Privacy & Local Execution
- Tools can run **locally via MCP `transport=stdio`**, preserving data privacy
- Input sources include: exported CSVs, emailed Excel files, PDFs from reports
- Logs and audit trails saved for compliance purposes

---

## 📚 Grounding in Real Artifacts
- Ontario Ministry and City variance reports (e.g. Toronto, Windsor)
- IFIS/Hyperion + Excel spreadsheet workflows
- PDF-based reporting templates from Public Accounts and variance briefings

---

## 📌 Multi-Agent Design & Tool Orchestration
This use case is a strong candidate for a **multi-agent MCP architecture**, in which different MCP agents (each hosting specific tools) can collaborate and orchestrate a complete reporting pipeline.

For example:
- **Data Agent** (Agent A): fetches and parses ERP + Excel data
- **Analysis Agent** (Agent B): computes variances, forecasts spend, flags risks
- **Narrative Agent** (Agent C): drafts reports and commentary
- **Submission Agent** (Agent D): prepares final PDF and publishes via Git or Notion

This mirrors advanced MCP research models like:
- **MCP-Zero**: Proactive toolchain discovery and composition
- **ScaleMCP**: Embedded agent memory and dynamic tool registration
- **mcp-agent**: Multi-agent lifecycle management and cross-agent tool dispatch
- **MCP Tool Chainer**: Sequential JSONPath-based tool orchestration

By structuring the Finance Co-Pilot as a team of agents with clear roles, we ensure scalability, explainability, and extensibility.

---

## 👍 Deliverables for Implementation Team

1. **FastMCP server setup** (Python)
2. **5 modular tools** as above with logging and context injection
3. **Sample SQLite database** with simulated budget/actuals
4. **PDF and spreadsheet parser prototype**
5. **Gemini or GPT integration for narrative drafting**
6. **Example run using a Toronto-style variance report as input**
7. **Interface for human review + feedback cycle**
8. **Export option: PDF/Notion report, GitHub push**

---

## ✅ Impact & Expansion Potential
- Reduces cycle time for reporting by 50%+
- Supports year-end burn-down and risk alerts
- Applicable to health, infrastructure, and education ministries
- Expandable to include CoA prep, audit readiness, and quarterly TB submissions
- Demonstrates a scalable, compliant use case of multi-agent MCP systems in Canadian public sector

