# Product BCDR Leadership — Engineering & Operations Mandate
*Initiative Tracker*

**Scope clarification (top-level):** This initiative is about **Product BCDR** — continuity and recovery for the platforms (ODC + O11). It is **not** company-wide BCDR (corporate IT, office continuity, HR, business operations). Those domains sit with other parts of the company (Corporate IT / Security / Legal). E&O's claim is on the product layer, where it has the operational levers.

## Overview

**V2MOM Alignment:** TBD — likely M3 (Incident Response Resilience) or M6 (Operational Excellence). To be confirmed once scope is defined.

**Source:** Mandate from Salman (2026-05-06)

**Working assumption (internal):** Engineering & Operations is the natural home for **Product BCDR** specifically — the platforms it operates (ODC + O11). E&O does not own the whole company BCDR strategy; only the product slice. PE drives the work as part of the department. This is a working hypothesis to validate with Salman — **not something to surface explicitly until E&O's role is agreed first.**

**Sequencing rule:** First decide what role E&O plays in **Product** BCDR. PE's role inside E&O is a downstream conversation, not the opening one. Company-wide BCDR ownership is out of scope for this conversation.

**Lead (operational):** Vera Branco

**Status:** Scoping

**Timeline:** Q2 2026 — scope and stakeholder kickoff. Execution timeline TBD.

**Why private (for now):** Scope is undefined, role is unclear (lead vs. own), and the question about PE's mandate is sensitive until aligned with Salman. Promote to shared `initiatives/` once scope is firm.

---

## Scope

**In scope:** Product BCDR — continuity and recovery of the platforms operated by E&O (ODC + O11). Includes platform recovery objectives, runbooks, drills, backup posture, status communication, and the operational governance around them.

**Out of scope:** Company-wide BCDR (corporate IT, office continuity, HR, business operations). These domains have other owners. We are not signing up for them and should not let scope drift there.

**Output Expected:** TBD — depends on Salman alignment.

**Anchors (now confirmed):**
- Product BCDR strategy exists (SOC 2-era, platform-focused) — **known to need review**
- 3 drill retros from last year (2 ODC, 1 O11) — covers data-loss scenarios only, all product-side
- This is not greenfield: it's a refresh + operationalize + broaden mandate within the product slice

**Likely scope shape (to confirm with Salman):**
- Refresh the Product BCDR strategy (RTO/RPO, scope, assumptions, current vs. target state)
- Operationalize: cadence, ownership, exercise calendar, discoverability in PE catalog
- Broaden drill coverage beyond data-loss (region failure, identity, KMS, account compromise)
- Make it cross-cloud (ODC + O11) by design, not by exception

---

## Open Questions

### For Salman (BLOCKING — resolve before any stakeholder outreach)

**Sequence the questions deliberately. Land E&O's role first; PE's role inside E&O comes later.**

1. **What role does Engineering & Operations play in Product BCDR?**
   - Scope is limited to product/platform continuity (ODC + O11). Company-wide BCDR is not what we're claiming.
   - Three options for E&O's role within product:
     - Department of accountability — E&O owns the product BCDR outcome end-to-end
     - Department of execution — E&O delivers against a product BCDR strategy owned elsewhere (e.g., Security, Compliance, Architecture)
     - Department of coordination — E&O convenes the product teams, but accountability is distributed
   - This is the framing question. Everything else flows from it.

2. **Is Product BCDR vs. Company BCDR a clean line we both agree on?** Confirm Salman shares the framing — that we are scoping to the platform layer only and not absorbing corporate continuity.

3. **What is the trigger for this ask now?** (Audit finding? Recent incident? Compliance gap? Strategic priority?) — shapes urgency and scope.

4. **What does success look like in 6 months?** — concrete output Salman expects.

5. **Cross-cloud scope:** ODC + O11 by design — confirm.

### Downstream questions (raise after E&O's role is settled — NOT in the first conversation)

- Within E&O, which team drives the work? (PE is the natural fit, but only ask once #1 is answered.)
- Strategy refresh — who holds the pen?
- Co-ownership model with Cloud and Support inside E&O.

### Internal questions (to work through with Paulo Garcia + Charola first)

- What BCDR artifacts already exist across ODC and O11? (runbooks, RTO/RPO targets, last DR test results, backup procedures, on-call playbooks)
- Where are the obvious gaps?
- Who actually operates BCDR today, even informally?
- What's the realistic ambition for Q2/Q3?

---

## Stakeholder List (draft — to refine after scope is clear)

**Inside E&O department (co-owners of execution):**
- Vera Branco — Process Engineering (drives the work)
- Pedro Charola Alves, Renato Armani — Cloud Platform (ODC)
- Carlos Sousa, Bruno Batista — Cloud / Engineering (O11)
- Paulo Garcia — Support
- Marcia Xavier (or delegate) — Support
- Salman — department accountability

**Internal homework group (start here, all inside E&O):**
- Vera Branco (PE)
- Paulo Garcia (Support)
- Pedro Charola Alves (Cloud)

**External stakeholders (consulted, not co-owners):**
- João Valentim — ODC Architecture
- Ricardo Soeiro — O11 Architecture
- João Rodrigues / Ebenezer Schubert — ODC Engineering / AI Group
- PM representation (Pedro Girão's team) — **defer**; only if scope includes feature/tooling gaps

**Why this split matters:** E&O members are accountable for delivering BCDR within their domains. External stakeholders have inputs (architecture decisions, engineering capacity, product trade-offs) but don't carry execution accountability. Treating them differently keeps the working group small and the broader stakeholders consulted at the right cadence.

---

## Approach

**Phase 1 — Internal homework (Vera + Paulo Garcia + Charola)**
- Align on what BCDR means in our context
- Inventory current state across ODC and O11
- Identify the 2-3 most obvious gaps
- Output: shared understanding, not a deliverable yet

**Phase 2 — Salman alignment**
- 30 min to resolve role and scope questions above
- Confirm output and timeline expectations

**Phase 3 — One-pager + stakeholder pre-read**
- Problem statement, scope in/out, proposed approach
- 3-5 questions for stakeholders to answer ahead of any meeting
- Send 48h before any group call

**Phase 4 — Stakeholder kickoff**
- Only after the one-pager is out and read
- Filter attendee list based on who is actually needed for the agreed scope

---

## Tasks

- [ ] Read existing BCDR strategy doc end-to-end; mark stale / missing / valid
- [ ] Read 3 drill retros (soft delete, hard delete, O11 DB restore); pull open action items
- [ ] Internal homework session with Paulo Garcia + Charola — current state inventory
- [ ] 30-min sync with Salman to resolve role + scope questions (with sharper framing post-homework)
- [ ] Draft v1 of one-pager (see `one-pager.md`)
- [ ] Strategy refresh — own the redraft of the BCDR strategy
- [ ] Confirm V2MOM alignment (M3 vs M6) with team
- [ ] Refine stakeholder list based on confirmed scope
- [ ] Send pre-read to stakeholders
- [ ] Hold stakeholder kickoff

---

## Work Log

### 2026-05-06
- Salman handed over BCDR + Ops Review format leadership
- Initial stakeholder list drafted (above)
- Decision: do internal homework with Paulo Garcia + Charola before broader outreach
- Open question for Salman: lead execution vs. own strategy
- Initiative captured in private-initiatives until scope is firm
- **Anchor docs identified:** SOC 2-era BCDR strategy + 3 drill retros (2 ODC, 1 O11)
- **Reframe:** not greenfield — this is refresh + operationalize + broaden
- **Decision:** strategy refresh is in scope. The existing BCDR strategy doc is known to need review.
- **Ownership framing:** BCDR sits with the Engineering & Operations department, not PE alone. Stakeholder list re-split into E&O internal (co-owners) vs. external (consulted).
- **Sequencing decision:** With Salman, anchor the conversation on E&O's role first. PE's role within E&O is a downstream conversation, not the opening one. Avoids pre-committing PE to scope before department-level accountability is settled.
- **Scope tightened:** This is **Product BCDR** only (ODC + O11 platforms). Company-wide BCDR (corporate IT, office, HR) is explicitly out of scope and not E&O's claim. Stops scope drift before it starts.

---

## Links

- Companion initiative: Ops Review format review (lower complexity, separate tracker)
- Related: M3 — Incident Response Resilience (potential alignment)
- Related: M6 — Operational Excellence Sustainability (potential alignment)

---

*Last updated: 2026-05-06*
