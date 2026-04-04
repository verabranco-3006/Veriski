# M3.4 — Problem Management Integration
*Initiative Tracker*

## Overview

**V2MOM Alignment:** Method 3.4 — Problem Management for Action Item Lifecycle & Customer Communication

**Jira Epic:** RSA-860

**Owner:** Inês Matos

**Collaborators:** GS (customer communication), Development teams (action item execution), Process Engineering (governance & tracking)

**Status:** Planning

**Started:** 2026-04-04

**Target Completion:** Q4 2026

---

## Jira Tracking

All sub-initiatives and tasks will be tracked under:
- **Epic:** [RSA-860](https://outsystemsrd.atlassian.net/browse/RSA-860)
- **Project:** RSA (Reliability & Service Assurance)

## Problem Statement

From GS workshop (March 2026), Problem Management has dual purpose:

**Goal 1 (Internal):** Track action item lifecycle completion after incident resolution

**Goal 2 (External):** Customer-facing artifact to share progress with customers

### Current Challenge: Action Item Governance

**Current Process:**
1. Retrospective completed
2. Each team creates action items in their own Jira projects (stories, tech improvements, etc.)
3. Action items linked to original RDINC incident artifact

**Problem:** Action items scattered across multiple team projects → hard to govern completion in structured way

**Impact:**
- No centralized visibility or enforcement mechanism for action item completion
- Difficult to track closure rates
- Customer-facing progress reporting lacks consolidated view
- M3.2 measurement (Action Item Plan Closure Rate) difficult to implement

## Goal

Establish formal Problem Management process that:

1. **Tracks action item lifecycle** post-incident resolution with centralized governance
2. **Provides customer-facing artifact** to share progress on remediation actions
3. **Enables M3.2 measurement** (>80% closure rate for High/Critical action items)
4. **Solves governance challenge** of action items scattered across team projects

## Success Criteria

By Q4 2026:

1. **>90% Problem Management coverage** (M3.7) - mandatory incidents have Problem records created
2. **Problem record ownership model defined** - clear accountability for action item completion
3. **Governance mechanism operational** - centralized visibility and enforcement for action item closure
4. **Customer-facing artifact working** - GS can share progress with customers via Problem records
5. **M3.2 measurement enabled** - can track closure rate for High/Critical action items

By Q2 2027:

6. **>80% action item closure rate** (M3.2) - High/Critical items closed within OLA/Deadline

## Key Decisions

*To be documented as decisions are made during implementation*

### Open Design Decisions (Q2 2026)

1. **Governance Model:** How to track action items across multiple team projects?
   - Option A: Centralized Problem Management project where all action items are created
   - Option B: Federated model with automated aggregation/reporting
   - Option C: Mandatory linking to Problem ticket with automated status roll-up

2. **Ownership Assignment:** Who owns the Problem record?
   - Incident Commander?
   - Value Stream leader?
   - Process Engineering?
   - Rotational ownership model?

3. **Enforcement Mechanism:** How to ensure action item completion is governed?
   - Automated reminders?
   - Operations Review visibility?
   - SLA/OLA enforcement?

## Tasks

Tasks will be created in Jira under Epic RSA-860 by Inês.

### Q2 2026: Process Definition
- [ ] Define Problem Management criteria (which incidents require Problem records)
- [ ] Design governance model for action item tracking across team projects
- [ ] Define Problem record ownership model
- [ ] Document Problem Management process (creation, tracking, closure)
- [ ] Define enforcement mechanism for action item completion
- [ ] Establish OLA/deadline framework for High/Critical action items

### Q3 2026: Pilot & Implementation
- [ ] Execute pilot with subset of incidents
- [ ] Create Problem records for pilot incidents
- [ ] Test governance model (action item tracking, visibility, enforcement)
- [ ] Validate customer-facing artifact with GS
- [ ] Refine process based on pilot learnings
- [ ] Document Problem record creation workflow

### Q4 2026: Scale & Measurement
- [ ] Roll out to all mandatory incidents
- [ ] Achieve >90% coverage (M3.7 target)
- [ ] Establish baseline for action item closure rate (M3.2)
- [ ] Integrate with Operations Review for visibility
- [ ] Full governance mechanism operational

### Q1-Q2 2027: Optimization
- [ ] Optimize action item closure rate toward >80% target (M3.2)
- [ ] Continuous improvement based on closure data
- [ ] Refine enforcement mechanisms as needed

## Work Log

### 2026-04-04
**Initiative Setup & Documentation**
- Created M3.4 Problem Management initiative folder structure
- Documented dual purpose from GS workshop (action item tracking + customer-facing artifact)
- Identified governance challenge and open design decisions
- Aligned with V2MOM metrics (M3.2, M3.7)

## Links

- Context notes: `initiatives/active/m3.4_problem_management/context_notes.md`
- V2MOM measurements summary: `initiatives/active/v2mom_definition/v2mom_measurements_summary.md`
- GS workshop outcomes: `log/daily/2026-04-01.md` (7 challenges documented)

## Risks & Dependencies

**Risks:**
- Governance model unclear - may cause adoption delays
- Problem record ownership unclear - risk of abandoned Problem tickets
- Action items still scattered across team projects - difficult to enforce centralized tracking
- Teams may resist centralized governance if perceived as bureaucracy

**Dependencies:**
- Retrospective Transformation (M3.3) - Problem Management follows RCA completion
- GS collaboration for customer-facing artifact requirements
- Development team buy-in for Problem record ownership and action item completion
- Jira workflow design for Problem records
- OLA/deadline framework definition

**Mitigations:**
- Define ownership model in Q2 2026 practice definition phase
- Pilot approach (Q3 2026) validates governance model before full scale
- Frame as quality assurance and customer communication improvement, not compliance theater
- Start with mandatory criteria (e.g., all status page incidents) to build adoption gradually
- Leverage Operations Review visibility to drive accountability

## Next Steps

1. **Q2 2026:** Begin practice definition phase
   - Define mandatory Problem Management criteria
   - Design governance model for action item tracking
   - Define Problem record ownership model
   - Document Problem Management process
2. **Align with stakeholders:** GS (customer communication), Value Stream leaders (ownership), Process Engineering (governance)
3. **Integrate with M3.3:** Ensure Problem Management follows Retrospective Transformation model

---

*Last updated: 2026-04-04*
