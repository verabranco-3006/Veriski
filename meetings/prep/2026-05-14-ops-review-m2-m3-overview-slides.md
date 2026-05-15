# Ops Review — Method 2 & Method 3 Overview Slides
*Draft · 2026-05-13 for 2026-05-14 Ops Review*

Source documents:
- **M2 problem statement:** `ProcessEngineering_Internal/v2mom_definition/method_2_strategic_document.md`
- **M3 problem statement:** [Confluence PE-STRAT-05 — Incident Response Reengineering Problem Statement](https://outsystemsrd.atlassian.net/wiki/spaces/EEO/pages/5838995469)

PPTX generator: `2026-05-14-ops-review-m2-m3-slides.py` → `2026-05-14-ops-review-m2-m3-slides.pptx`

---

## SLIDE 1 — Method 2: Transform Change Management

**Owner:** Laura Ferreira · **Method Lead:** Vera Branco

### Why it exists

1. **Invisible Risk Surface** — One RFC approval fans out into N ungoverned executions on production rings, never passing the SDLC's cumulative confidence checks.
2. **Fragmented role accountability** — Requesters, Reviewers, Approvers, Implementers all hold partial authority — no end-to-end risk owner, no shared scoring framework, no refusal mechanism.
3. **CFR signal you can't act on** — RFC ↔ incident correlation is manual; lifecycle data lags reality; trust-based automation gates stay theoretical.

### What we're doing

| Sub | Focus |
|-----|-------|
| M2.1 | Artifact Centralization — single Change Catalog |
| M2.2 | CM Role Accountability — 4-role framework |
| M2.3 | Standard Promotion & Discovery |
| M2.4 | CFR Correlation — RFCs to incidents |
| M2.5 | CFR Technical Implementation |
| M2.6 | Lifecycle Automation |

### What success looks like

- Every change traces to a defined catalog article
- Each of the 4 CM roles has a sharp scope and a refusal mechanism
- Standards flow through automation; SRE shifts from operator to reliability owner
- CFR is a trusted signal Engineering Leadership acts on
- Audit evidence is a query, not a manual reconciliation

---

## SLIDE 2 — Method 3: Incident Response Resilience

**Owner:** Inês Matos · **Method Lead:** Vera Branco

### Why it exists

1. **Service Incident vs Support Case: no clear separation** — GS, SRE and Engineering apply different logic at intake. There's no shared rule for what's a Service Incident versus a Support Case — each demands its own operating model and ownership.
2. **Alerts that should be incidents stay invisible** — We can't formally declare false negatives. Alerts are worked silently through Jira comments instead of triggering the coordinated incident-response motion with the mobilization it needs.
3. **Operational silence on system-wide incidents** — System-wide incidents close without the right internal comms — often without a Resolved update. External Status Page accuracy suffers as a consequence.
4. **Retrospective backlog and stagnation** — SRE-led, capacity-constrained model. Lead times stretch into months; the reviewer pool is concentrated; action items go stale before they ship.

### What we're doing

| Sub | Focus |
|-----|-------|
| M3.1 | Failure Management Governance |
| M3.2 | Status Page Governance |
| M3.3 | Triage Models & OLAs — SI vs Support Case |
| M3.4 | Problem Management — Bug Mgmt & customer comms |
| M3.5 | Retrospective Transformation — team-led |
| M3.6 | Event Management |

### What success looks like

- Service Incidents and Support Cases each have a defined operating model and clear OLAs
- Alerts have a defined path to declaration — no silent false negatives
- Internal Status Page reflects every system-wide incident lifecycle
- Retrospectives are team-led, completed within target lead time
- Problem Management converts recurring failures into structural fixes

---

## Speaker notes — numbers parked here, not on the slides

**Method 2 — bring out only if asked:**
- 731 RFCs → 992 manual mutations on production rings in 2025 (1.35x multiplier; 1.38x for Normal). 2026 trending past 1,140.
- 45h average review + approval lead time (18h review + 27h approval).
- 70.59h average ghost time in "Implementing" after the change is done.

**Method 3 — bring out only if asked:**
- 44% of system-wide incidents had zero internal comms (Oct 2025 – Jan 2026).
- 7% followed the full lifecycle (Investigating → Identified → Monitoring → Resolved).
- 72-day average retrospective lead time.
- 63% of retros reviewed by just 2 people.

## Speaker framing

**Method 2:**
- Frame: this is about closing the Invisible Risk Surface, not "we have too many tickets".
- M2.1 is the unblocker — without the catalog, nothing else lands safely.

**Method 3:**
- Frame the cost qualitatively; only bring numbers if pressed.
- Two new framings to land:
  - **SI vs Support Case separation** — each requires its own operating model and OLAs. This is what M3.3 lands.
  - **Alert management** — we can't declare false negatives today, so signals stay invisible instead of triggering the coordinated incident response. This is what M3.6 lands.
- Leverage points: M3.3 (triage), M3.4 (problem mgmt), M3.6 (event management).
