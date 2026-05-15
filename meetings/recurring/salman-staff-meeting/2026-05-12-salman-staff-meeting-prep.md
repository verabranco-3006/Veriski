# Salman Staff Meeting — Prep
*Tuesday, 2026-05-12 · 11:00–12:00*

**Attendees:** Salman Malik, Anabela Cesário, Pedro Charola Alves, Paulo Garcia (declined — OoO), Vera Branco

**⚠️ REMINDER: Check if AI Companion is on to record the call content**

---

## Context Since Last Meeting (May 5)

- **Axos #1 — Maestro action items closure:** Confirmed via Nuno Ferreira. Both committed follow-ups exist: **RBST-3358** (Application Image Cleanup, led by Build Services) and **RDMAST-2638** (remove silent record-deletion logic on customer GET). Closes the open item Charola flagged.
- **Axos #3 — BCDR / off-hours drill:** Already shared with Salman and the group where we stand on BCDR. Orchestration starting with Pedro Neves (Paulo's team). Position taken: we need homework on BCDR before pulling stakeholders in.
- **Mythos Readiness Taskforce** *(top priority — next month)* — Marcia Xavier's task force framing captured (9 workstreams). PE contributes **Stream 4 (Accelerated Response & Containment)** with Glenn Frye; joint walkthrough being scheduled with Mitch O'Donnell + TJ Moore to land the boundary between Vulnerability Mgmt, Exposure Mgmt and Security Incident Response. **Flagging to Salman as PE's top priority for the next month.**
- **V2MOM Method 2 (Change Management)** — Reviewer Slack message drafted and parked in `#odc_change_management_reviewers` ready to send (Foundations + 1,800 → 26 → 61 operation-types data story + concrete validation ask).

---

## Open Action Items (from prior meetings)

**From May 5:**
- [ ] Sentry — align with SRE/GS on installation split (low-risk → GS; full installment → SRE) and automation path
- [ ] Book session with Márcia Xavier on CISO's Sentry product review
- [ ] Schedule BCDR + outage testing meeting *(today's agenda — frames the homework first)*
- [ ] Schedule Operations Review format meeting *(today's agenda — leverage Anabela's presence)*

**From April 28:**
- [ ] Vera: catch up on AI podcasts
- [x] Vera: add "apagão" scenario to BCDR scenario list *(folds into BCDR homework below)*
- [x] Vera: start preparing Salman staff meetings — this prep doc closes it
- [ ] Define structure for AI Enablement Days (SRE/GS) — format, duration, scope, logistics

---

## New Topics

### 1. BCDR — confirm Eng&Ops' role before pulling stakeholders in

**Goal:** Land Salman's read on Eng&Ops' expected role on Product BCDR before we go wider. We need homework first.

**Context:**
- Current ODC BCDR strategy was drafted late 2022 to sustain the SOC2 Attestation drill. Used tactically last year for two drills (deleted tenant in ODC, deleted DB in O11) — both in-hours.
- Team agreed the 2022 strategy needs review to align with current product architecture.
- Not aware of an equivalent BCDR document for O11.
- Axos #3 is the immediate trigger — but it sits inside a broader gap.

**Ask — confirm or open floor on the role of Eng&Ops on Product BCDR:**
- **(a) Lead strategy execution** — someone else owns the strategy, we drive delivery and process
- **(b) Own and execute** — we define what BCDR looks like across ODC + O11 and run it
- **(c) Coordinate** — convene and govern, but ownership stays with Cloud / Architecture

**Primary stakeholder list (for when we're ready to convene):**

| Area | Stakeholders |
|---|---|
| ODC | Pedro Charola Alves, Renato Armani (Cloud Platform), João Valentim (ODC Architecture), João Rodrigues / Ebenezer Schubert (ODC Engineering / AI Group) |
| O11 | Pedro Charola Alves, Carlos Sousa / Bruno Batista (O11 Cloud + O11 Engineering Group), Ricardo Soeiro (O11 Architecture) |
| Support | Paulo Garcia |
| Security | Márcia Xavier (or delegate) |
| PM | Someone from Pedro Girão's team |

**Outcome needed:** Salman's pick on (a/b/c), or his framing of how he wants Eng&Ops positioned. Until that's clear, no stakeholder meeting goes out.

---

### 2. Operations Review — format conversation, with Anabela in the room

**Goal:** Start the format conversation today since Anabela is here — leverage the moment, don't wait for a separate meeting.

**Context:**
- Ops Review is currently managed only for ODC, by Anabela's team under Bruno Fernandes — they're a must in any redesign.
- Already named in the skip-level: current perception is a "blaming meeting", not a learning/accountability mechanism.
- Gaps surfaced from the last review (April 30): missing O11 representation, uneven preparedness across presenting groups (some bring root causes + action plans, others bring Jira dumps they can't explain).

**Ask — start small, in this order:**
1. **Goals** — what do we want this forum to drive?
2. **Outcomes** — what does success look like (decisions made? actions tracked? signals surfaced?)
3. **Scope** — ODC only, or ODC + O11?
4. **Format** — what changes given the answers above?
5. **Alignment with VS Leaders** for both O11 and ODC once we have a draft

**Outcome needed:** agreement to use today's slot to define goals + outcomes + scope; then a separate working session with Anabela / Bruno Fernandes to land format and propose to VS Leaders.

---

### 3. Mythos Readiness Taskforce — flag PE involvement as top priority for the next month

**Goal:** Tell Salman directly that PE's top priority for the next month is the Mythos Readiness Taskforce. Set expectations on capacity reallocation before he hears about it elsewhere.

**Context:**
- Marcia Xavier's task force, 9 workstreams. PE contributes **Stream 4 — Accelerated Response & Containment** with Glenn Frye.
- Joint walkthrough being scheduled with Mitch O'Donnell + TJ Moore to land the boundary between Vulnerability Mgmt, Exposure Mgmt and Security Incident Response — process/coordination triggers are not clear today.
- João Rodrigues likely ODC lead.
- Emergency Response Process v0 draft already created (two paths: immediate mitigation vs contain-then-mitigate; declaration step + tiger team activation as open questions).

**Ask:**
- Acknowledge this is top priority and will pull PE focus over the next month
- Confirm reporting line for Mythos work — through PE V2MOM, through Marcia, or both?
- Surface any signals he's heard from CISO side that should shape Stream 4 scope

**Outcome needed:** Salman aligned that Mythos Readiness is PE's #1 focus for the month; clarity on reporting cadence.

---

### 4. Data Governance — Charola likely raises this

**Goal:** Be ready to respond when the topic comes up. Don't lead it.

**Context:** The lack of Data Governance is surfacing through the context lake work. Charola is likely to bring it. Worth listening for what specifically he's hit — quality, ownership, access, lineage, or something else — before positioning PE.

**Potential PE angle (only if asked):**
- Process governance ≠ data governance, but the broken continuous-improvement loop and the "data → present → next slide" pattern at Ops Review are downstream symptoms of the same gap
- M3.3 work already exposes where data quality breaks triage decisions (SEV calibration finding) — concrete case study if useful

---


## Meeting Notes

### Topics Discussed

**DR Readiness**
- Framed by Salman as a proposal to understand operational readiness, using the kind of concern raised by Axos Bank as the example case
- Sits adjacent to the BCDR conversation Vera prepped — broader framing than off-hours response drill

**Product Leadership Team outcome — 3-year AI-business plan**
- Outcome of the Product Leadership Team: build a 3-year plan of new AI-business ideas

**Salman's V2MOM — M6: Budgeting & cost management**
- Method 6 needs to include all of Anabela's budgeting/financial concerns reflected on Anabela's M7 - Optimize CPTO Investment Strategy & Financial Execution
- Needs to translate how the **Rule of 60** will be percolated and operated across the org
- Charola: investigate if **cost per tenant** is the right metric
- Anabela + Pedro Charola: need to build a plan to find extra help to manage the cost management topic (capacity gap acknowledged)

**AI Enablement — split into two methods**
- Decision to separate AI Enablement into two distinct methods:
  - **(1) Internal:** enabling our own teams and our own execution models
  - **(2) Full org:** enabling the broader org (e.g., AI @ Product — already led by Anabela)

---

### Decisions Made

- AI Enablement to be structured as **two separate methods** (internal teams vs full org enablement)
- Salman's M6 will absorb Anabela's budgeting vectors and operationalize the Rule of 60

---

### Not Covered — Carry Forward

*Confirm with Vera what landed vs what didn't from the prep:*

- **BCDR (a/b/c) role question** — DR Readiness was discussed, but did Salman explicitly pick a role for Eng&Ops (lead / own / coordinate)? If not, carry forward.
- **Mythos Readiness Taskforce flag** — was PE's top-priority-for-next-month framing landed with Salman?
- **Ops Review format conversation with Anabela** — did the goals/outcomes/scope discussion happen, or was it crowded out by V2MOM topics?
- **Data Governance (Charola)** — Charola raised cost-per-tenant metric uncertainty; not clear if the broader Data Governance / context lake topic was opened.
- **Sentry alignment** (SRE vs GS installation split + Márcia Xavier CISO product review session)

---

### New Action Items

- [ ] **Anabela:** Schedule deep-dive session with Finance on budget/process
- [ ] **Anabela + Pedro Charola:** Plan to find extra help for cost management
- [ ] **Salman:** Share his V2MOM with the team
- [ ] **Salman:** Restructure AI Enablement method into two methods in PE V2MOM (internal teams + full- product org enablement)
- [ ] **Open:** Confirm whether cost per tenant is the right metric (Charola, with Anabela, with the help of Adolfo)
- [ ] **Open:** How does Rule of 60 percolate operationally — needs framing to the teams

