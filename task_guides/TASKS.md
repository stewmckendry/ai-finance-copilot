# 🛠️ Codex Task Plan: Finance Analyst Co-Pilot

This document outlines tasks for Codex Agents to build the MVP pipeline.

## 🔹 Agent A: Data Agent
- `task_001_ingest_variance_excel.md`: Parse IFIS-style budget vs actual spreadsheets
- `task_002_parse_budget_pdf.md`: Extract structured data from Toronto/Ontario budget PDFs
- `task_003_normalize_inputs.md`: Transform inputs into unified finance schema

## 🔹 Agent B: Analysis Agent
- `task_010_compute_variances.md`: Join budget vs actuals, compute variance % and $
- `task_011_forecast_spend.md`: Predict year-end outcome and flag unspent funds
- `task_012_flag_risks.md`: Highlight accounts with risk of overspend or lapse

## 🔹 Agent C: Narrative Agent
- `task_020_draft_variance_narrative.md`: Generate narrative for variance report
- `task_021_style_tuning.md`: Match Ontario public tone (Windsor/Toronto reports)
- `task_022_generate_QA_responses.md`: Answer finance questions ("Do we have money for X?")

## 🔹 Agent D: Submission Agent
- `task_030_export_to_pdf.md`: Render formatted report for sharing
- `task_031_push_to_git.md`: Commit outputs and logs
- `task_032_log_tool_calls.md`: Store all tool use, inputs/outputs, reasoning trace

## 🔹 Interface
- `task_040_web_frontend.md`: Build UI for review, approvals, logs
- `task_041_test_CLI.md`: CLI for tool testing

## 🧪 Test Data & Scaffolding
- `task_050_seed_sqlite.md`: Populate mock finance DB
- `task_051_sample_inputs.md`: Store PDF, Excel samples
- `task_052test_pipeline.md`: End-to-end test case with mock data

Each file will define scope, inputs, outputs, expected behavior, and test setup.