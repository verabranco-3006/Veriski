# Problem & Bug Management in ODC — April 10, 2026

**Time:** 16:30–17:00
**Scope:** Align on the narrative — the shift from Bug Management to Problem Management
**Context:** Toyota (TIIS) escalation as the catalyst

**Attendees:**
- **Arul Livingston** — VP (sponsor)
- **Vijay** — Head of Quality (strong advocate for Bug Management governance)
- **João Brandão** — Head of Release Management (awareness — Release Notes depend on Problem Management execution)
- **Inês Matos** — Process Owner for Problem Management (PE)
- **Vera Branco** — Team Lead, Process Engineering

---

## The Core Narrative

**Today, bugs are managed in isolation. They should be managed through Problem Management.**

The current state: R&D teams create and manage bugs ad-hoc with no standard process, no consistent measurements, and no visibility into the overall bug landscape. Bugs exist disconnected from the problems that originated them. This means:
- No traceability from customer incident → problem → bug fix → release note → customer notification
- No ability to answer "how many open bugs do we have?" or "what's the average time to fix?"
- No customer-facing visibility into whether their reported issues are being addressed

The Toyota escalation is the proof point: 4 tickets where fixes were made but customers had no visibility because bugs were treated as internal items disconnected from Problem Records.

**The shift:** Bug Management should be a governed process that operates as a by-product of Problem Management — not separate from it. Problem Management identifies the "what" and "why"; Bug Management governs the "how" and "when" of the fix. The linkage between them is what ensures customer visibility end-to-end.

---

## Why Problem Management Is the Foundation

If we adopt Problem Management properly, the downstream problems fix themselves:

| If Problem Management is adopted... | Then... |
|---|---|
| RPMs created for recurring/complex incidents | Bugs are always traceable to a Problem Record — no orphan fixes |
| Bugs linked as child tasks under RPMs | Bug lifecycle is governed through RPM workflow (can't close RPM until bugs are done) |
| RPM ID used in commits | Release Notes are published automatically when fix reaches GA |
| Customer-facing fields populated (workaround, how to confirm, status) | Customers self-serve on Problem Portal → deflects repeat tickets |
| Known Errors documented in RPM | Global Support has centralized troubleshooting database |

**Problem Management adoption is the lever. Bug Management governance is the outcome.**

---

## What ODC Has vs What ODC Needs

ODC Problem Management was designed correctly but is in **Stage 1** with critical gaps:

| Capability | O11 (mature) | ODC Stage 1 (current) | ODC Stage 2 (planned, not done) |
|---|---|---|---|
| Customer-facing fields | Description, Workaround, How to confirm, Status | Release Notes only | Full customer-facing fields |
| Customer status tracking | Problem Tracking Page on Support Portal | Not available | Planned |
| Email notifications on transitions | Yes (Release Planned, Closed) | No | Planned |
| KPIs with targets | Defined (Urgent: 2w WA, 3m release) | Collect data only, no targets | Define targets |
| Bug lifecycle governance | Implicit through RPM mandatory fields | None — bugs managed ad-hoc | Not scoped |

**The gap is not design — it's adoption and enforcement.**

---

## The Gap: What's Actually Happening

| What Should Happen | What's Actually Happening |
|---|---|
| RPMs created for recurring incidents | Many incidents closed without RPM creation |
| Bugs created as by-product of RPM investigation, linked with "is blocked by" | Bugs created in isolation, no RPM linkage |
| RPM ID in commits → automatic Release Notes | Developers don't include RPM ID → Release Notes not published |
| Customers see fix status via Problem Portal | Customers told "internal fix" with no visibility |
| Known Errors documented with workarounds | Workarounds shared ad-hoc, not centralized |

---

## Toyota Escalation — The Catalyst

Toyota shared 25 tickets across 3 categories. The relevant one here:

**Release Note Transparency Standards** — 4 tickets where fixes were made but not documented:

| Ticket | Issue | Reason Given |
|--------|-------|--------------|
| 3295446 | Chinese locale fix | "minor internal fix" |
| 3295461 | IDP auth fix | "internal incident" |
| 3283979 | External Logic network error | "internal RPM" |
| 3276495 | Role search logic fix | "UX patch" |

Toyota needs to report to their Board of Directors that this was addressed.

**Root cause:** These bugs were fixed without Problem Records. No RPM = no customer-facing Release Note = Toyota can't track the fix.

---

## What We're Proposing

### 1. Problem Management Adoption as the Priority
- RPM creation should be the default, not the exception, for recurring incidents and customer-impacting bugs
- Teams need enablement on when and how to create RPMs
- Every customer-impacting bug MUST be linked to an RPM
- PE follows up on RPM closure (already in our scope per the Retrospective process)

### 2. Bug Management as a Governed Process Under Problem Management
Bug Management should be a **separate, governed process** with:
- **Defined lifecycle:** creation → triage → prioritization → fix → verification → release
- **Measurements:** open bug count, average time to fix, customer-impacting bugs without release notes, bug escape rate
- **Accountability:** clear ownership of bugs at every stage
- **Mandatory linkage to Problem Management:** bugs always traceable to an RPM — Problem Management identifies the problem, Bug Management governs the fix

This is where PE and Quality align: Vijay's push for Bug Management governance is the same goal — the mechanism is Problem Management as the connecting layer.

### 3. Customer Visibility Through Problem Management
- Problem Portal already exists — ensure it's being populated
- Workarounds documented in RPM, not just shared in Slack/tickets
- Known Error database maintained actively
- Push for Stage 2 (customer-facing fields and status tracking)

---

## How It Works in O11 (The Reference Model)

O11 has a **mature, customer-facing Problem Management process** since 2021:

- **Problem Tracking Page** on Support Portal — customers see status, description, workaround, how to confirm they're affected
- **Email notifications** on RPM transitions (Release Planned, Closed)
- **Mandatory Release Notes** on every RPM
- **Bugs always linked** to RPMs — RPM can't close until bugs are resolved
- **Known Error database** built into the RPM lifecycle
- **Deflection mechanism:** customers self-serve → fewer repeat tickets to Global Support

ODC was built with the same RPM model but is not enforcing the same discipline. We're regressing, not progressing.

---

## Talking Points

- **The narrative shift:** We're not asking for a new process. We're asking for adoption of what was already designed. The shift is from "bugs managed in isolation by each team" to "bugs governed through Problem Management."
- **Toyota is the proof point.** 4 fixes with no customer visibility because they bypassed Problem Management. Toyota reports to their Board — this is customer trust, not just process improvement.
- **O11 already solved this.** Customer-facing Problem Management since 2021. ODC has the same design but not the same discipline.
- **Bug Management and Problem Management are two sides of the same coin.** Problem Management governs the "what and why"; Bug Management governs the "how and when." Both need governance, and the linkage is what ensures end-to-end visibility.
- **Problem Management is a deflection mechanism.** Every RPM properly documented is a potential support ticket deflected. Without it, customers open repeated tickets asking "was this fixed?"
- **Vijay's Quality push and PE's Problem Management push converge here.** Bug Management governance is achieved through proper Problem Management adoption — same goal, same mechanism.

---

## Questions to Bring

- **To Vijay:** What measurements does Quality already track on bugs that we can build on? How do we align Bug Management governance with Problem Management as the connecting layer?
- **To Inês:** Where are we on ODC Problem Management Stage 2 (customer-facing visibility)? What's blocking adoption by R&D teams?
- **To Arul:** What level of sponsorship can we expect to push Problem Management adoption across R&D?
- **To all:** Do we agree that Problem Management adoption is the foundation, and Bug Management governance follows from it?

---

*Prep generated: 2026-04-10*
