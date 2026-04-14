# Follow-up Message — Bug Management Governance Model Clarification

**Channel:** Slack group message (same thread — Arul, Vijay, Brandão, Inês)
**Date:** 2026-04-14

---

One clarification on the governance model for Bug Management :slightly_smiling_face:

When I mentioned "federated execution across the teams," I want to be more precise on what we mean. The model we're proposing is similar to how Incident Response works today:

- **Central project and workflow** — bugs tracked in a centralized project with a defined lifecycle, not scattered across individual team projects
- **Central governance (Quality)** — defines the bug lifecycle standards, measurements, triage criteria, and accountability model
- **Teams execute within the central framework** — development teams own the fix, but the bug record lives in the governed project so we have full visibility and traceability

The reason: if bugs stay in individual team projects, we can't track them centrally. We lose the ability to answer "how many open bugs do we have?" or "what's the average time to fix?" — which is exactly the gap we're trying to close.

There's also a scalability concern: if each team manages bugs in their own project with their own workflows, every process change requires updating every project individually. That doesn't scale. A centralized project means one place to maintain, one workflow to evolve, and consistency across all teams.

Several processes already work this way — Problem Management, Incident Response, and Change Management all operate through central projects. Bug Management should follow the same model.
