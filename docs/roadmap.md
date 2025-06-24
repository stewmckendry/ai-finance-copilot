# 🗺️ Product Roadmap: Finance Analyst Co-Pilot

## 🔍 Goal
Deliver a working MVP in 1–2 days that demonstrates an end-to-end AI co-pilot for public sector financial reporting.

---

## 🚦Phase 1: MVP Infra + Planning (Day 1)
- ✅ Define system architecture and agent roles
- ✅ Set up repo with README, AGENTS guide, task plan
- ✅ Commit example PDFs, task scaffold
- 🔜 Seed SQLite with mock finance data

## ⚙️ Phase 2: Core Pipeline (Day 1–2)
- 🔜 Build basic tools for each agent (ingest, analyze, narrate, log)
- 🔜 Chain tools into callable pipeline using FastMCP
- 🔜 Create CLI runner and stub web interface
- 🔜 Support PDF + Excel input and audit logging

## 📢 Phase 3: MVP Output & Review (Day 2)
- 🔜 Generate Toronto-style variance report
- 🔜 Enable user review and approvals
- 🔜 Publish output to Git and PDF
- 🔜 Run CLI + web demo

## ✨ Phase 4: Blog + Open Source (Day 2+)
- 🔜 Write blog post walking through system
- 🔜 Open-source codebase + sample data
- 🔜 Share lessons on multi-agent AI co-pilots in public finance

---

## 🔁 Development Practices
- Use Codex Agents to implement each tool/task
- Commit small, testable units
- Run in local-only mode for privacy
- Capture logs + reasoning traces for transparency

## 📌 Priority Features
- Variance analysis + narrative drafting
- Audit logs + human-in-the-loop review
- Public-sector tone + real input data

MVP focus: usable pipeline > perfect polish.