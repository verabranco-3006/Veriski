# Q3 Planning — Pending Jira Updates

*Captured during Q3 planning session on 2026-06-24. Execute in batch after session.*

---

## RSA-886 — M5.1 Operating Model

- [ ] Add task: **Knowledge redundancy plan** — define method backup ownership for each team member (lightweight, one owner per method as backup). Not blocking Q3 start.

---

## RSA-958 — E2E Delivery Excellence (Out-of-Strategy)

- [ ] Create epic in Jira under RSA-958 if not yet created
- [ ] Set quarter: Q3 2026
- [ ] Set owner: Vera Branco
- [ ] Add label or flag: **out-of-strategy** — runs alongside V2MOM commitments at partial allocation
- [ ] Add description: 12-week discovery initiative. Q3 delivers two outputs: (1) current-state map of the delivery chain across specialist tracks and PDLC phases; (2) controlling mechanism design proposal for Q+1 implementation. See discovery plan for full scope.
- [ ] Link to stakeholders: Salman Malik (sponsor), Ric Pruss (Architecture)
- [ ] Add dependency note: capacity viability depends on M3.3 task ownership decision (RSA-728) — if 5 tasks stay with Vera, RSA-958 pace is at risk

### Task breakdown — pending scope validation (2026-06-25 alignment meeting with Salman + Ric)

Do not create in Jira until scope is confirmed. Once validated, create as stories under RSA-958.

| # | Task | SP |
|---|------|----|
| T1 | QE discovery interview (Kenneth Krause / Chris Curtis) | 5 |
| T2 | Reliability discovery interview — SRE + Architecture (Pedro Charola + Ric Pruss) | 5 |
| T3 | Supportability / GS discovery interview (lead TBD) | 5 |
| T4 | Release Engineering discovery interview (Joao Brandao) | 5 |
| T5 | Security discovery interview (Marcia Xavier) | 5 |
| T6 | Dev teams session 1 (Tiago Oliveira + TBD) | 5 |
| T7 | Dev teams session 2 (value stream TBC) | 5 |
| T8 | Cross-track synthesis — current-state map + scored gap list | 8 |
| T9 | Define minimum viable signal set | 5 |
| T10 | Data availability and feasibility assessment | 5 |
| T11 | Controlling mechanism design proposal | 8 |
| | **Total** | **61 SP** |

- Derived initiative score: **8 (Strategic)**
- Capacity read: ~5 SP/week across 12 weeks = ~40% of net focus capacity at partial allocation
- Context-switching penalty not included — add based on concurrent P-phase items at quarter planning

---

## RSA-949 — Move to M1.2 and assign

RSA-949 ("Design skill to plan Jira tasks per PE-OM-03 effort estimation procedure") is currently under M5.1 (RSA-886). It belongs to M1.2.

- [ ] Change epic link from RSA-886 → RSA-890 (M1.2)
- [ ] Assign to Vera Branco (or confirm Paulo owns it — decision pending)
- [ ] Confirm 5 SP estimate already in description — set as story points field if not already set

---

## RSA-822 — M1.3 Q3 Tasks (new scope needed)

All existing M1.3 tasks are Completed. M1.3 needs a new Q3 task list.

- [ ] Wait for Paulo's task proposal (ask: July 3 meeting)
- [ ] Once proposed, create tasks under RSA-822 with SP estimates
- [ ] Ensure Inês and Laura are assigned to at least one M1.3 task each in Q3

---

## RSA-891 — M5.2 Performance & OutPerform Alignment

- [ ] Update epic description: scope is (1) define OutPerform rubric per person — what Exceeding / Spot On / Not There Yet means against their individual V2MOM goals; (2) run regular tracking cadence aligned to team V2MOM measurements.
- [ ] Add dependency link: RSA-891 depends on RSA-886 M5.1 measurement readiness before cadence can run.
- [ ] Transition status from Backlog → In Design (rubric definition starting end of Q2).

---

## Method 2 — M2.1 · M2.2 · M2.5

### RSA-776, RSA-779 (M2.1) — Confirm SP estimates

- [ ] Verify RSA-776 "Review ODC Change Catalog (NORMAL)" has SP set — expected 5 SP
- [ ] Verify RSA-779 "Identify and review runbooks" has SP set — expected 5 SP
- [ ] Verify RSA-783 "Link team catalogs to centralized CM" has SP set
- [ ] Verify RSA-785 "Define Catalog Article Management process" has SP set
- [ ] Verify RSA-788 "Set up monitoring and iteration processes" has SP set

### RSA-785 (M2.1) — Confirm Q3 sequencing anchor

RSA-785 is the Q3 primary deliverable for M2.1. All M2.2 tasks that depend on catalog content (RSA-906, 907, 909, 911) are blocked on it.

- [ ] Confirm RSA-785 has Laura as assignee
- [ ] Add blocking link: RSA-785 blocks RSA-906, RSA-907, RSA-909, RSA-911

### RSA-905–RSA-912 (M2.2) — SP review

Laura has allocated capacity per task — needs confirmation SP field is set in Jira (not just in epic description).

- [ ] Verify SP set on RSA-905, RSA-906, RSA-907, RSA-908, RSA-909, RSA-910, RSA-911, RSA-912

### RSA-856 (M2.5) — Redundancy decision

Post team discussion on July 3 — one of two outcomes:

**Option A: M2.5 is redundant → close epic:**
- [ ] Transition RSA-856 from Discovery → Abandoned (or equivalent)
- [ ] Move any tasks under RSA-856 to RSA-812 (M2.4) if they exist
- [ ] Update capacity model: remove M2.5 entries for Paulo if consolidating

**Option B: M2.5 has distinct scope → define it:**
- [ ] Update RSA-856 description to clearly differentiate from RSA-812
- [ ] Create task breakdown under RSA-856 with SP estimates

---

## Method 3 — M3.2 · M3.3 · M3.5

### RSA-814 (M3.2) — Add snapshot logging task

- [ ] Create task under RSA-814: "Define and implement V2MOM measurement snapshot for Status Page governance metrics"
  - Assign: Inês Matos
  - SP: 5
  - Dependency: blocked on RSA-900 (V2MOM tracking mechanism) defining the structure
  - Description: Capture first snapshot of Status Page governance metrics against V2MOM targets. Validates that RSA-900 mechanism covers this method's measurement needs.

### RSA-728 (M3.3) — Full Jira task rebuild

Zero tasks currently under RSA-728. Tasks need to be created from the initiative file structure. **Do not create until Vera + Inês align on scope (target: by July 3).**

Tasks to create (pending alignment with Inês + O11 dependency with RSA-915):

**Sub-stream A — Triage at Intake:**
- [ ] A1 Phase 4: Stratified sample analysis (Path 2 — ticket resampling)
- [ ] A1 Phase 5: Synthesis + SEV calibration proposal
- [ ] A2: Workshop with SRE/O11 to validate triage heuristics
- [ ] A3: Design triage framework document
- [ ] A4: Calibrate thresholds and publish final model

**Sub-stream B — Service Incident Handshake (requires O11/RSA-915 alignment):**
- [ ] B1: Map current SRE → GS handshake path (align with Messias Peralta design)
- [ ] B2: Design SI confirmation criteria (involve Tiago Garcia / SRE)
- [ ] B3: Validate and roll out SI handshake protocol

**Sub-stream C — Support Case Coverage:**
- [ ] C1: Discovery — scope of Support Case OLA coverage (can start independently)
- [ ] C2: OLA design per case tier
- [ ] C3: Negotiation and roll-out

**Cross-cutting:**
- [ ] Define Triage Accuracy metric and target
- [ ] Design quarterly calibration cadence

**For each task:**
- Assign: Inês Matos
- Set SP before July 3 — Inês to estimate in session
- Epic link: RSA-728

### RSA-728 (M3.3) — O11 alignment

After Vera + Inês align, before task creation:
- [ ] Add RSA-915 as a dependency link on RSA-728 (relates to / is coordinated with)
- [ ] Tag Messias Peralta (or SRE lead) as watcher on RSA-728

### RSA-881 (M3.5) — BAU transition check

- [ ] Check open task count under RSA-881
- [ ] If tasks remain: confirm with Inês they are effort-accounted and Q3-sized
- [ ] If no tasks remain: transition RSA-881 status to BAU / In Production
- [ ] Add comment: "Q3 focus is governance cadence within Ops Review. Method transitioning to BAU."

---

## Method 4 — M4.1 · M4.2 · M4.3 · M4.4 · M4.5

### RSA-855 (M4.1) — Close completed task

- [ ] Transition RSA-855 "Support Activities" from In Progress → Done (all items in description checked off)
- [ ] Paulo to confirm no untracked items before transitioning

### RSA-843 (M4.2) — Unblock or clarify

- [ ] Add comment to RSA-843: confirm blocker (is it M2 company V2MOM metric definition still unstable, or Snowflake data access, or something else?)
- [ ] Set SP on RSA-843 (currently unset)
- [ ] If blocked: add blocking link (what is blocking it)
- [ ] If ready: transition RSA-838 (M4.2 epic) from Implementation → In Progress

### RSA-862 (M4.3) — Q3 task breakdown

Paulo to propose task breakdown before July 3.

- [ ] After Paulo confirms, create tasks under RSA-862 with SP estimates
- [ ] Include at least one AI-assisted task if applicable (e.g., "Generate metric lineage draft using AI — review and validate")
- [ ] Assign: Paulo Alves Monteiro

### RSA-863 (M4.4) — Drop or plan decision

Post July 3 team discussion:

**Option A: Drop M4.4:**
- [ ] Transition RSA-863 from On Hold → Abandoned
- [ ] Update capacity model: remove M4.4 entries for Paulo

**Option B: Plan M4.4:**
- [ ] Define scope (training materials? dashboard training sessions?)
- [ ] Create task breakdown
- [ ] Update epic status to In Design

### RSA-864 (M4.5) — Mid-quarter start

- [ ] Paulo to propose Q3 task breakdown for M4.5 before July 3
- [ ] Tasks start in August — set target start dates
- [ ] Capacity model: check if current S-phase start (Sep in shared-data.js) needs to shift to Aug

---
