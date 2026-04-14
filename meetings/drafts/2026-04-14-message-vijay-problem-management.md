# Message to Meeting Participants — Problem Management Narrative & Next Steps

**Channel:** Slack group message (Arul, Vijay, Brandão, Inês)
**Date:** 2026-04-14

---

Hi team :slightly_smiling_face:

Following up on our April 10 alignment on Problem & Bug Management — I wanted to consolidate the narrative we discussed and outline next steps so we keep momentum.

**The core idea we aligned on:**

Bug Management should be a governed process that operates through Problem Management — not separate from it. Problem Management identifies the "what" and "why"; Bug Management governs the "how" and "when" of the fix. The linkage between them is what ensures customer visibility end-to-end.

**Where we are today:**

- R&D teams create and manage bugs ad-hoc with no standard process, no consistent measurements, and no visibility into the overall bug landscape
- Bugs exist disconnected from the Problem Records that originated them
- No traceability from customer incident → problem → bug fix → release note → customer notification
- The Toyota escalation was the proof point: 4 tickets where fixes were made but customers had no visibility because bugs were treated as internal items disconnected from Problem Records
- Release notes sometimes posted on individual Jira items instead of the public Problem Record artifact
- The workflow that works in O11 is not being followed structurally in ODC

**What we agreed on:**

1. **Bug Management as a central practice owned by Quality** — proper definitions and controls for tracking issues across all environments, not just production
2. **Central governance, federated execution** — Quality defines the bug lifecycle standards, measurements, and accountability model. Teams execute within their own projects
3. **Problem Management as the governance and visibility layer** — connects bugs to customer impact, enables the Problem Portal, ensures end-to-end traceability
4. **Customer visibility through Problem Management** — populate the Problem Portal, document workarounds in RPMs, push for ODC Stage 2 (customer-facing fields and status tracking)

**Next steps from the meeting:**

- @Brandão — involve Francisco for the Toyota customer enablement issue
- @Inês — will lead the process definition work for Problem Management in Q2
- @Vera — share Problem Management documentation with the group (links below) and connect Vijay with Inês

**Documentation:**
- [Problem Statement — Problem & Bug Management in ODC](https://outsystemsrd.atlassian.net/wiki/spaces/EEO/pages/6214811869/Problem+Statement+Problem+Bug+Management+in+ODC) — full narrative, current gaps, what we're proposing
- [Problem Management (R&D Knowledge Base)](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/5036841027/Problem+Management)
- [ODC Problem Management](https://outsystemsrd.atlassian.net/wiki/spaces/EEO/pages/4408049977)
- [O11 Problem Management](https://outsystemsrd.atlassian.net/wiki/spaces/EEO/pages/1261306400)

**A specific ask for @Vijay:**

From the meeting, we aligned that Bug Management is Quality's domain. What I'd like us to think about together is: what role should Quality play in Problem Management, and how should that connect with Bug Management governance?

Our view is that Bug Management needs central governance and definition — owned by Quality — with federated execution across the teams. Problem Management is the layer that connects bugs to customer impact and ensures nothing falls through the cracks. But for this to work, we need Quality actively shaping the operating model:

- How does Quality define what a well-governed bug lifecycle looks like — from creation to triage to fix to verification to release?
- What measurements should we track centrally? (open bug count, average time to fix, bug escape rate, customer-impacting bugs without release notes)
- How do we ensure teams follow the standards without turning it into bureaucracy?
- What does Quality already have in place that we should build on rather than reinvent?

Problem Management is the foundation — it provides the "what happened and why." Bug Management governance is the outcome — it ensures the "how and when" of the fix is tracked and visible. Quality defining the standards is what makes the whole chain work.

I'd like to connect you with Inês Matos, our Process Owner for Problem Management. Having your input early will make sure we design this right. 
Thanks!
