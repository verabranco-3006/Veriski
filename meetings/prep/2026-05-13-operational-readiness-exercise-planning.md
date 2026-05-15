# Operational Readiness Exercise — Planning Prep
*Wed 2026-05-13 · 16:00–16:30 · Vera + Charola + Pedro Neves (Paulo Garcia OOO)*

**Jira Epic:** [RSA-939](https://outsystemsrd.atlassian.net/browse/RSA-939) (assigned to Vera)

---

## Context

**Source.** Mandate from Salman, triggered by Axos Bank concerns on operational readiness. Framed in his 2026-05-05 staff meeting as understanding operational readiness using the Axos concern as the example case. Reinforced on 2026-05-12: PE coordinates, GSSA orchestrates, Cloud Platform owns the technical scenario design.

**What's been said so far.**

- Salman's framing: "this may be analogous to the testing we need to do for full disaster recovery albeit much tighter in scope."
- Charola's view: "me, Paulo Garcia and Vera need to talk to come up with a plan."
- Charola's working scenario: break authentication on a single tenant.
- Vera's position so far: we've never run a similar coordination/mobilization scenario off-hours. Last year's BCDR drills tested 2 scenarios (deleted tenant in ODC, deleted DB in O11) — both in-hours.

**Adjacent, not the same.** This exercise is the first concrete artifact under a broader Product BCDR refresh (tracked in `private-initiatives/active/bcdr-leadership/`). Don't let it drift into BCDR strategy territory — separate track.

---

## Scenario to refine

Charola's draft: **break authentication on a single tenant.**

Three follow-ups before it's a scenario, not a placeholder:

1. **Which auth layer?** Keycloak signing key, identity broker, session store, token issuer — they exercise different muscles.
2. **What does "break" mean operationally?** Rotate to invalid key, null a record, expire all sessions, block the endpoint.
3. **Why single tenant?** Isolation for safety, or does the scenario lose teeth at that scope? Single-tenant break only exercises tenant-isolated detection; a platform-wide auth issue exercises something else entirely.

**Alternative scenarios worth listing (so we know we picked, not defaulted):**

- Cert / signing-key expiry
- DB credential rotation failure
- Regional failover or partial AZ degradation
- Rate-limit storm / dependency saturation

---

## Anchor questions for the 30-minute meeting

1. **What muscle are we testing?** Detection, escalation, mitigation, comms, recovery. Pick 2 max — trying to test all five at once produces noise, not learning.
2. **Is single-tenant break-auth the right scenario, or a placeholder?** Tie back to Axos's actual concern.
3. **Announced, partially announced, or blind?** First exercise → recommend announced. Blind only after the announced flow is clean.
4. **Which off-hours window? Which on-call rotation is in scope?**
5. **Stop-the-bus authority and abort thresholds?** Exercise director (not on-call) calls start and abort. Real-customer-impact threshold defined.
6. **Success criteria?** MTTA / MTTR targets, pass/fail per muscle being tested.

---

## Watch-outs

- **Pedro Neves pattern:** defensive positioning surfaces under pressure ("GSSA cannot operate due to PE" framing in March 1:1). Frame as joint problem-solving, not a PE-driven mandate.
- **Paulo Garcia OOO.** Anything that needs Support input gets flagged for async follow-up, not decided in the room.
- **Scope creep into BCDR.** This is an exercise, not the strategy. Strategy refresh lives in the BCDR initiative.
- **Don't ship a stunt.** One exercise is a stunt. A cadence is a program. Land this as the first artifact of a recurring rhythm, not a one-off.

---

## Roles

| Role | Owner |
|------|-------|
| Coordination | PE (Vera) |
| Orchestration | GSSA (Pedro Neves, Paulo Garcia's org) |
| Technical scenario design | Cloud Platform (Pedro Charola Alves) |
| Support input | Paulo Garcia (informed; OOO today) |
| Sponsor | Salman Malik |

---

## Pre-flight deliverables (what we need before the exercise runs)

- One-page scenario design (scope, success criteria, abort conditions, comms plan)
- Pre-mortem walk-through with all parties
- Rollback validated in lower environment
- Comms templates pre-drafted (status page draft + customer comms; unsent unless real impact)
- Sign-off from accountable VS Leader

---

## Outcome needed from today

1. **Scenario refined** (or decision to swap it for a stronger candidate).
2. **Owners assigned per prep workstream** (scenario design, comms, on-call coordination, rollback validation).
3. **Next checkpoint date** committed.
4. **Follow-up async with Paulo Garcia** on Support's read on the scenario before next checkpoint.

---

## Open thread for Vera (don't surface in the room unless asked)

- **Cadence question.** Salman's framing was "a drill" (singular). Worth pushing for a recurring rhythm here, or wait until after the first run lands? Lean: float the cadence question lightly, commit after the first run.
- **Apagão scenario** (from April 28 staff meeting) — fold into the same drill series, or keep separate? Defer until first scenario is locked.
- **Vera's homework on previous exercises.** Vera to share context on the prior in-hours drills (deleted tenant ODC, deleted DB O11) — captured in `inbox.md` for follow-up.

---

## Links

- Jira Epic: [RSA-939](https://outsystemsrd.atlassian.net/browse/RSA-939)
- Adjacent initiative: `private-initiatives/active/bcdr-leadership/_initiative.md`
- Salman staff 2026-05-05 (where #3 framing originated): `meetings/recurring/salman-staff-meeting/2026-05-05-salman-staff-meeting.md`
- Salman staff 2026-05-12 (PE coordination confirmed): `meetings/recurring/salman-staff-meeting/2026-05-12-salman-staff-meeting-prep.md`
