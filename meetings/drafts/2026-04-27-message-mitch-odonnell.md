# Draft Message — Mitch O'Donnell
**Date:** 2026-04-27
**Channel:** Slack DM
**Context:** Scoping the Emergency Vulnerability Process (Stream 1c) before scheduling a working session

---

Hi Mitch :slightly_smiling_face:

Following Tiago's plan, I wanted to share some initial thinking on our joint deliverable — the Emergency Vulnerability Process (Stream 1c) — so we can align before jumping into a working session.

**What I see as the goal:**
A process that guides R&D teams when a day-0 vulnerability is detected — clear triggers, roles, escalation paths, and time targets. Not a replacement of the existing Vulnerability Management flow, but the emergency overlay when normal triage cadences are too slow.

**Questions I'd like us to work through together:**

*Triggers and declaration:*
- What conditions should activate this emergency process vs. the regular VUL flow? (CVSS threshold? Active exploitation? Vendor advisory?)
- Who has authority to declare a day-0 emergency?
- What information is typically available at detection time — and what gaps should we expect?

*Engineering engagement:*
- What does Security need from Engineering when this triggers, and how fast?
- What level of engagement is expected — dedicated tiger team, on-call rotation, swarming?
- Who coordinates the response — Security, Engineering, or shared?

*Interaction with existing processes:*
- How should this relate to the current VUL/RPM workflow — does it run alongside it, feed into it after containment, or replace parts of it?
- Under what conditions does a day-0 trigger an incident (RDINC)?
- Where does Exposure Management fit in?

I'd love to get your perspective on these before we schedule a session to start drafting. If you have any docs or references from the Red team side that would help me understand the current detection and response flow, that would be great too.

Let me know what works for you — happy to sync this week or early next, before the next weekly.
