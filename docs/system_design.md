# 🧱 System Design: Finance Analyst Co-Pilot

## Overview
The Co-Pilot is a modular, AI-powered reporting system for public sector finance teams. It integrates data ingestion, structured reasoning, narrative generation, and compliance-oriented output logging.

## 🧠 Architecture Diagram (Textual)

```
User --> Web UI --> FastMCP Interface -->
    [Agent A] Data Agent
        - fetchBudgetData (CSV, Excel, PDF, Azure SQL read-only)
        - parseVarianceSpreadsheet
        - parsePDFReports

    [Agent B] Analysis Agent
        - reconcileBudgetVsActual
        - identifyUnspentFunds
        - forecastYearEnd

    [Agent C] Narrative Agent
        - draftVarianceNarrative
        - styleNarrative
        - respondToQuery

    [Agent D] Submission Agent
        - commitDraftReport
        - logActivity
        - exportPDF

    --> Output: PDF | Notion | GitHub
```

## 🗃️ Data Sources
- Excel/CSV exports from IFIS/ERP
- Public PDF reports (Toronto/Ontario budgets)
- Read-only Azure SQL DB mirroring ERP data
- Manual uploads or email attachments

## 🧩 Components
| Component         | Description                                     |
|------------------|-------------------------------------------------|
| `FastMCP Server` | Orchestrates tool calls, routing, context       |
| `Tool Modules`   | Python functions implementing MCP tools         |
| `SQLite DB`      | Simulated budget + actuals + variance store     |
| `Frontend`       | Review interface, log viewer, approval actions  |
| `MCP Resources`  | Exposed configs, prompts, and schema            |
| `Prompt Registry`| YAML + MCP-native prompt definitions            |

## 🔐 Security & Privacy
- Local tool execution for sensitive data
- Full audit logs (tool calls, inputs, reasoning)
- Optional auth for data access, tool use

## 🔁 Workflow Lifecycle
1. User uploads files or initiates analysis
2. Data Agent ingests and normalizes inputs
3. Analysis Agent computes key metrics
4. Narrative Agent drafts summaries and QA answers
5. Submission Agent packages outputs, logs reasoning
6. User reviews, approves, and shares outputs

## 🧪 Test Infrastructure
- CLI tool for tool testing (`transport=stdio`)
- Preloaded inputs for Toronto-style variance report
- Logs of tool calls and LLM decisions

## 🧱 Future Enhancements
- MCP HTTP/SSE transport
- Prompt registry and agent prompt discovery
- Cancel/progress lifecycle support
- Auto-refresh from shared drives
- Real-time budget chat assistant

---
System reflects Model Context Protocol (MCP) principles: modularity, prompt/resource separation, lifecycle traceability, and human-in-the-loop.