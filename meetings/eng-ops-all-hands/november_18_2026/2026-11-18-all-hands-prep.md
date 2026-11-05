# Eng Ops All Hands — Nov 18, 2026 — Prep

**Status:** **PE is not on the Nov 18 agenda.** The agenda was defined without a PE intervention. The SRE collaboration topic below is parked for a future all hands — the narrative and examples are kept here as a starting point.

**Format:** shared session with all of Salman's staff. PE gets one short intervention, not a slot per agenda section. One topic, told well.

**Thread from September:** we closed on *"we would rather come back to a future all hands and go properly deep on one."* With a short slot, we can't go deep. We can show that one seam got closed with a partner team.

---

## The two options

Both are cross-team stories, which fits a room where every leader in Salman's staff is present. The partner team is the protagonist as much as we are.

### Option 1 · Transforming Change Management, with SRE

- **Story:** segregation of duties left nobody equipped to assess risk end-to-end. We are redesigning the four roles (requester, reviewer, approver, implementer) so each one owns a clear part of the risk.
- **Receipts:** change catalog **~1,800 → 61** operation types (M2.1). Role accountability model (M2.2). CFR measurement (M2.5).
- **Partner:** SRE as implementers and the largest population of requesters.
- **Strength:** touches most people in the room every week. Concrete before/after.
- **Risk:** M2.2 started July. Need to confirm what is live vs. designed, otherwise it reads as a plan, not a result. The GS ↔ SRE transition initiative is on hold, so keep it out.
- **Presenter candidate:** Laura, with an SRE counterpart.

#### Narrative draft — Option 1

**The hook:** two teams, two different pains, same destination. Neither team waited for the other, and the result fits together.

**1 · Two pains, one year ago**
- PE saw a governance problem. Segregation of duties left nobody equipped to assess risk end-to-end, and audit evidence was a manual reconciliation. We put it in the V2MOM as Method 2.
- SRE saw a toil problem. Too much of their week went into executing manual changes. They decided to build a GitOps pipeline to automate most of them.

**2 · Same destination**
When we put the two side by side, the goals matched:
- Keep Standard / Normal / Emergency. Change the mechanism, not the model.
- Take SRE out of manual execution. SRE builds and reviews the platform instead of running each change.
- Standard changes become self-service: PR merged, pipeline executes.
- Governance gets lighter, not heavier. Controls come from how the work runs, not from steps added on top.
- Audit becomes a query. The Git log is the evidence.
- Approvers own the risk they sign for. Teams own their operational scripts.

**3 · How they fit**
- PE defines **what** a change is: catalog article, roles, promotion criteria, failure correlation.
- SRE built **how** it runs: PR, pipeline, execution.
- The catalog article is the workflow definition. The PR review is the accountability check. The merge is the lifecycle step.

**3b · What working together looks like — concrete examples**

Two or three real examples, each one sentence: what we did together and what changed. This is what makes the story credible. **To confirm with the team and Charola. The vault doesn't hold current examples.**

| Candidate | What to confirm |
|---|---|
| Joint alignment of the two strategies: PE governance model and SRE GitOps proposal reviewed side by side, gaps resolved together | Which of the five gaps were closed, and how (e.g., catalog article points to the versioned workflow file) |
| A catalog article that became a pipeline workflow: a standard change that used to be manual RFC + SRE execution, now PR → merge → executed | Name one real change type, before/after (time, steps, who's involved) |
| Reviewer and implementer roles mapped onto the PR flow: risk check as an explicit PR step, refusal moved to SRE at workflow-definition time | Is it live or designed? |
| Reviewer framework stress-tested with SRE (Charola, Brandão) | Did it happen? What changed as a result? |
| Shared evidence: Git log + workflow runs as SOC 2 evidence, feeding CFR correlation | Has audit used it yet? |

Format for each on stage: *"[Change type] used to take [X steps / Y days] with SRE executing by hand. Today it's a PR, [owner] approves, the pipeline runs it, and the evidence is already there."*

**4 · What it means for the room**
- For engineering teams: fewer manual steps, faster standard changes, no evidence chasing.
- For SRE: less toil, more time on reliability.
- For leadership: governance and audit evidence without a slower path to production.

**Close:** one line crediting SRE by name (Charola and team), then one line on what comes next.

**Needs before Nov 18:**
- One or two current numbers, e.g. % of changes now running through the pipeline, catalog size (~1,800 → 61), lead time trend.
- Confirm Charola wants to co-present or be credited.
- Keep it under the slot length. Section 2 can shrink to three bullets if time is tight.

### Option 2 · Security Incident Response and Vulnerability Management, with Security (Mythos)

- **Story:** Security used to hand Engineering a dashboard and expect everything fixed regardless of risk. We built one connected process, from threat to closure, with Security, risk-based and predictable for Engineering.
- **Receipts:** Day-0 emergency response process (v7.0). Unification Release 6: P0 invokes Incident Response, risk-based validation, AI priority scoring. PE leads **Pillar H** in Mythos Phase 2.
- **Partner:** Security (Marcia, Rhett, WS owners).
- **Strength:** Mythos is a company program and visible to ELT. Ties 2026 progress to 2027 in one story.
- **Risk:** Mythos will likely be covered by Salman or Marcia elsewhere in the session. We need a PE angle that doesn't repeat them. Phase 2 portfolio depends on the October ELT outcome. Confirm before saying anything about 2027.
- **Presenter candidate:** Vera with a Security counterpart (Rhett or Marcia).

### Choice

**Option 1 — SRE collaboration on Change Management.** Two teams solving different pains and landing on the same model is a cross-team story that works for the whole staff. Option 2 kept as a fallback if the slot changes.

---

## Questions for this afternoon

| # | Question |
|---|---|
| 1 | Agree on the SRE topic and the narrative structure |
| 2 | Who presents from PE (Laura?), and does Charola co-present? |
| 3 | What is the one number we lead with? |
| 4 | What is live today vs. still in design? We only claim what is live. |

## Still to ask Patrícia

| # | Question |
|---|---|
| 1 | How many minutes do we have? Slides or verbal? |
| 2 | What other topics are in the session? Is SRE presenting GitOps separately? |
| 3 | Content deadline and dry run date |
| 4 | One session or two for time zones? |

---

## Decision

**Nov 18:** no PE intervention — agenda defined without us. #decision

**For a future all hands:**

- **Topic:** Cross-team collaboration with SRE — Transforming Change Management (PE governance + SRE GitOps)
- **Presenter(s):**
- **Partner:** SRE (Charola)
- **Structure:**
- **Next steps:**

---

*Sources: `2026-09-08-all-hands-prep.md`, `initiatives/active/v2mom_execution/m2.2_roles_accountability/_initiative.md`, `initiatives/active/out_of_strategy/vulnerability_exposure_unification/_initiative.md`, `initiatives/active/out_of_strategy/mythos_phase_2/_initiative.md`, `initiatives/active/out_of_strategy/day0_vulnerability/_initiative.md`.*
