# Salman Staff Meeting — Prep & Notes
*Tuesday, 2026-05-26 · 11:00–12:00 · In-person, Hulk room*

**Attendees:** Salman Malik, Anabela Cesário, Pedro Charola Alves, Paulo Garcia, Vera Branco

**⚠️ REMINDER: Check if AI Companion is on to record the call**

---

## Context Since Last Meeting (May 12)

- **WS 4.1 Kickoff Workshop (week of May 19):** Glenn Frye led the O11 Response Modernization session with Carlos Sousa, Bruno Batista, Ricardo Garrido, Pedro Charola. O11 layer map done. Key finding: containment-first is the only realistic Day-0 response — fleet-wide patching is too slow at every layer. Legal/MSA constraint (customer approval required outside 4h maintenance window) is the biggest blocker across the board. Force majeure review flagged as urgent. Pedro Charola has direct actions from this workshop.
- **BCDR / Eng&Ops role question (from May 12):** Salman didn't explicitly pick (a/b/c). Still open.
- **Ops Review format meeting (agreed May 5):** Was this scheduled?
- **Salman's V2MOM sharing (action from May 12):** Still pending.
- **RSA-939 — Operational Readiness Exercise:** Held from yesterday (Monday) pending Salman alignment. Vera to share context on previous exercises and trace a plan.

---

## Open Action Items

**From May 12:**
- [ ] Anabela: Schedule deep-dive with Finance on budget/process
- [ ] Anabela + Pedro Charola: Plan for extra help on cost management
- [ ] Salman: Share V2MOM with team
- [ ] Salman: Restructure AI Enablement method into two (internal teams + full org)
- [ ] Open: Confirm cost per tenant as the right metric (Charola + Anabela + Adolfo)
- [ ] Open: Rule of 60 operational percolation — needs framing for the teams

**From May 5:**
- [ ] Sentry — align SRE/GS on installation split (low-risk → GS; full → SRE) + automation path
- [ ] Book session with Márcia Xavier on CISO's Sentry product review
- [ ] Schedule BCDR + outage testing meeting
- [ ] Schedule Operations Review format meeting

---

## Topics to Raise

### 1. RSA-939 — Operational Readiness Exercise

**Goal:** Get Salman's framing before moving. This connects directly to the BCDR/Axos #3 thread (off-hours drill agreed May 5) and to the Day-0 posture work.

**Context:** Previous exercises ran in-hours (deleted tenant in ODC, deleted DB in O11 — 2025 BCDR drills). RSA-939 is about what an operational readiness exercise should look like next: what to test, what success looks like, and who's in the room.

**Ask:** What's Salman's expectation — is this a drill for Eng&Ops coordination specifically, or a broader readiness check? Where does this land relative to the BCDR homework we agreed in May 5?

---

### 2. Mythos / Day-0 WS 4.1 — update

**Goal:** Keep Salman current on WS 4.1 workshop findings. Surface the one gap that needs his level to resolve.

**What happened:** Glenn Frye ran the O11 layer map workshop. The analysis is done. Strategic direction endorsed: containment-first (WAF is the fastest lever; fleet-wide patching is measured in weeks to months, not hours). No formal IR protocol exists for O11 today — ODC/Rootly is the proposed foundation.

**The gap that needs Salman's org:** War room / situation room — who has pre-authorized decision authority to act without a chain of approvals during a Day-0? This can't be left undefined when the legal/MSA review happens.

**Don't lead this — let Charola bring what he has from the workshop first.** Add the war room gap if it doesn't come up naturally.

---

### 3. Ops Review format — check if meeting was scheduled

**Goal:** Close the loop on a May 5 action item. If not scheduled, restart.

**Context:** Agreed in May 5 to run a separate meeting to define Ops Review goals, outcomes, and scope. Anabela is here — leverage the moment if it hasn't happened.

---

## Watch

- Don't expand RSA-939 scope before Salman frames the ask
- If Charola brings Data Governance / cost-per-tenant again, listen before positioning PE
- Salman's V2MOM still not shared — if not raised by him, ask directly

---

## Meeting Notes

### Topics Discussed

1. **Process map and architecture** — discussed (no further detail captured)

2. **Projects we are running** — Anabela will share a PoC with Salman to answer this use case

3. **Weekend Case with Entel** — [RDINC-83329](https://outsystemsrd.atlassian.net/browse/RDINC-83329), led by Mariana Cabeda

4. **ONE Conference** — discussed (no further detail captured)

5. **AI Costs** (Anabela) — modeling the costs we are incurring to strategize next year through sustainability lens

---

### Decisions Made

- Cloud cost optimization: Salman to speak with Paulo Silva; Paulo Garcia to manage the follow-through

---

### Not Covered — Carry Forward

- **RSA-939 — Operational Readiness Exercise** — not raised; carry to next staff meeting
- **Mythos / WS 4.1 update** — not raised; carry to next staff meeting
- **BCDR role (a/b/c)** — still no explicit answer from Salman
- **Ops Review format meeting** — not raised; still unscheduled
- **Salman's V2MOM sharing** — still pending

---

### New Action Items

- [ ] **Salman:** Speak with Paulo Silva on cloud cost optimization
- [ ] **Paulo Garcia:** Manage the cloud cost optimization follow-up with Paulo Silva
- [ ] **Anabela:** Share PoC with Salman on "projects we are running" use case
- [ ] **Vera:** Raise RSA-939 at next staff meeting
- [ ] **Paulo Garcia:** Align on a forum to present the outcomes of the GS+Engineering March Workshop to Salman
