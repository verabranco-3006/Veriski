# Problem Management Integration — Working Plan

*This is the working document for strategy, design, and implementation notes.*

---

## Current State

**Context from GS Workshop (March 2026):**

Problem Management identified as dual-purpose mechanism:
1. **Internal:** Track action item lifecycle completion after incident resolution
2. **External:** Customer-facing artifact to share progress with customers

### Current Process Flow

1. Retrospective completed (after incident resolution)
2. Each team with action items creates those items in their own Jira projects
   - Mix of item types: stories, tech improvements, backlog items, etc.
3. Action items linked to original RDINC incident artifact

### Current Challenge: Governance

**Problem:** Action items scattered across multiple team projects → hard to govern completion in structured way

**Impact:**
- No centralized visibility of action item status
- No enforcement mechanism for action item completion
- Difficult to measure closure rates (M3.2 metric)
- Customer-facing progress reporting requires manual aggregation
- Action items can be deprioritized without visibility

---

## Target State

**New Model: Formal Problem Management Process**

### Problem Management Dual Purpose

**Purpose 1 (Internal):** Action Item Lifecycle Tracking
- Centralized tracking of all action items from retrospectives
- Governance mechanism to ensure completion
- Visibility into action item status across team projects
- Enforcement of OLA/deadlines for High/Critical items
- Enables M3.2 measurement (closure rate tracking)

**Purpose 2 (External):** Customer-Facing Artifact
- Problem record as single source of truth for customer communication
- Progress updates on remediation actions
- GS can share Problem record status with customers
- Transparency on commitment vs. delivery

### Problem Management Scope

**When Problem Management Required (Mandatory Criteria - To Be Defined):**
- All incidents posted to external status page?
- All High/Critical severity incidents?
- Customer-impacting incidents?
- Incidents with recurrence patterns?
- [To be finalized in Q2 2026]

**Out of Scope:**
- Incidents that don't meet mandatory criteria
- Action items that are immediate fixes (completed during incident)
- Low-priority improvements without customer impact

---

## Implementation Phasing

### Q2 2026: Process Definition

**Objectives:**
- Define Problem Management process and mandatory criteria
- Design governance model for action item tracking
- Define Problem record ownership model
- Document workflows and OLA framework

**Deliverables:**
1. **Mandatory Criteria Document**
   - Which incidents require Problem records
   - Triggers for Problem Management activation
   - Exclusion criteria

2. **Problem Record Ownership Model**
   - Who owns the Problem record? (Incident Commander / Value Stream leader / Process Engineering / Rotational)
   - Accountability structure for action item completion
   - Escalation path for stalled Problem records

3. **Governance Model Design**
   - How to track action items across multiple team projects
   - Centralized vs. federated approach
   - Automated aggregation/reporting mechanisms
   - Enforcement mechanisms (reminders, Operations Review visibility, SLA/OLA)

4. **Process Documentation**
   - Problem record creation workflow (who, when, what)
   - Action item linking requirements
   - OLA/deadline framework for High/Critical items
   - Customer-facing artifact requirements (GS collaboration)
   - Closure criteria and handoff

5. **Integration with Retrospective Transformation (M3.3)**
   - How Problem Management follows RCA completion
   - Handoff from team-led retrospective to Problem Management
   - Action item identification and prioritization

### Q3 2026: Pilot & Implementation

**Objectives:**
- Execute pilot with subset of incidents
- Validate governance model
- Test customer-facing artifact with GS
- Refine process based on learnings

**Pilot Scope (To Be Defined):**
- Start with status page incidents (clear customer impact)
- 4-6 weeks minimum for meaningful data
- Test governance model across multiple value streams
- Validate Problem record ownership model

**Deliverables:**
- Pilot execution report with learnings
- Governance model validation (action item tracking effectiveness)
- Customer-facing artifact validation (GS feedback)
- Refined process documentation
- Problem record creation workflow finalized

### Q4 2026: Scale & Measurement

**Objectives:**
- Roll out to all mandatory incidents
- Achieve M3.7 target (>90% coverage)
- Establish baseline for M3.2 (action item closure rate)
- Full governance mechanism operational

**Deliverables:**
- >90% of mandatory incidents have Problem records (M3.7 target)
- Baseline action item closure rate established (M3.2)
- Operations Review integration (Problem Management visibility)
- Full governance mechanism operational (reminders, tracking, enforcement)
- Customer-facing artifact in use by GS

### Q1-Q2 2027: Optimization

**Objectives:**
- Optimize action item closure rate toward >80% target (M3.2)
- Continuous improvement based on closure data
- Refine enforcement mechanisms

**Deliverables:**
- >80% closure rate for High/Critical action items (M3.2 target by Q2 2027)
- Continuous improvement roadmap
- Refined enforcement mechanisms
- Best practices documentation

---

## Governance Model Options

### Option A: Centralized Problem Management Project

**Approach:**
- All action items created in centralized "Problem Management" Jira project
- No action items in team projects (or duplicate/link only)
- Problem record owns all action items directly

**Pros:**
- Centralized visibility and control
- Easy to measure closure rates
- Clear governance and enforcement

**Cons:**
- Teams lose flexibility in their own backlogs
- May be perceived as bureaucratic
- Potential resistance from teams

**Feasibility:** Medium - requires significant process change

---

### Option B: Federated Model with Automated Aggregation

**Approach:**
- Action items created in team projects (current state)
- Mandatory linking to Problem record
- Automated aggregation/reporting rolls up status to Problem record

**Pros:**
- Teams maintain autonomy in their own projects
- Less disruptive to current workflows
- Leverages existing team processes

**Cons:**
- Complex automation required
- Relies on teams linking correctly
- Harder to enforce completion

**Feasibility:** High - least disruptive, but requires automation investment

---

### Option C: Hybrid Model (Recommended - To Be Validated)

**Approach:**
- **High/Critical action items:** Created in centralized Problem Management project
- **Normal/Low priority:** Created in team projects with mandatory linking to Problem record
- Problem record tracks all action items via direct ownership or automated roll-up

**Pros:**
- Governance for high-priority items
- Team autonomy for lower-priority improvements
- Balances control and flexibility

**Cons:**
- Requires defining priority thresholds
- Still needs some automation for federated items
- Teams must understand which model to use

**Feasibility:** High - pragmatic balance

---

## Problem Record Ownership Model

### Option 1: Incident Commander Ownership
**Owner:** Person who led the incident response

**Pros:**
- Clear accountability from incident through action completion
- Incident Commander has context on root cause and remediation

**Cons:**
- IC may not have authority over action item execution (different teams)
- IC may move on to other priorities after incident closure

---

### Option 2: Value Stream Leader Ownership
**Owner:** Value Stream leader whose systems caused the incident

**Pros:**
- Authority to enforce action item completion within value stream
- Strategic ownership aligns with operational accountability

**Cons:**
- Multiple value streams may be involved (who owns?)
- Value Stream leaders may delegate without clear handoff

---

### Option 3: Process Engineering Ownership
**Owner:** Process Engineering team (rotational)

**Pros:**
- Neutral party with governance mandate
- Ensures consistent enforcement across value streams

**Cons:**
- PE lacks authority to enforce team action items
- Risk of becoming "Process Police" rather than enablers
- May not scale with high Problem record volume

---

### Option 4: Rotational Ownership (Recommended - To Be Validated)
**Owner:** Rotates based on incident characteristics
- Value Stream leader for single-value-stream incidents
- Incident Commander for cross-functional incidents
- Process Engineering for high-stake/cross-org incidents

**Pros:**
- Flexibility to assign accountability appropriately
- Scales across different incident types

**Cons:**
- Requires clear criteria for ownership assignment
- Potential confusion if criteria unclear

---

## Enforcement Mechanisms

### 1. Automated Reminders
- Weekly reminders to Problem record owner on overdue action items
- Escalation reminders to Value Stream leaders after X weeks overdue
- Automated notifications when action items approach OLA deadline

### 2. Operations Review Visibility
- Problem Management dashboard per value stream
- Action item closure rate tracked and visible to leadership
- Overdue Problem records flagged in Operations Review discussions

### 3. OLA/Deadline Enforcement
- High/Critical action items must have defined OLA/deadline
- Overdue action items escalated to Value Stream leader
- Quarterly review of closure rates per value stream

### 4. Quarterly Governance Review
- Process Engineering reviews Problem Management health
- Identifies patterns of stalled action items
- Coaching/support for value streams with low closure rates

---

## Customer-Facing Artifact Requirements

### What GS Needs (To Be Refined with GS Input)

1. **Problem Record Visibility**
   - GS can access Problem record for customer-impacting incidents
   - Problem record shows action item status (planned, in progress, completed)
   - Clear ownership and expected completion dates

2. **Progress Updates**
   - Ability to share progress with customers
   - Timestamp tracking (action item committed → completed)
   - Narrative summary of remediation work

3. **Completion Notification**
   - GS notified when all action items completed
   - Ability to close loop with customer on commitments

4. **Customer Communication Templates**
   - Standard language for sharing Problem record status
   - Privacy/security considerations (what can be shared externally)

---

## Integration with Retrospective Transformation (M3.3)

**Handoff from RCA to Problem Management:**

1. **Retrospective Completion** (M3.3)
   - Team-led retrospective identifies action items
   - Action items documented in RCA output

2. **Problem Record Creation** (M3.4)
   - **Trigger:** Retrospective completed + incident meets mandatory criteria
   - **Owner:** Assigned based on ownership model
   - **Content:** Problem record created with reference to RCA and action items

3. **Action Item Tracking** (M3.4)
   - Action items created in appropriate Jira projects
   - Linked to Problem record
   - OLA/deadlines assigned for High/Critical items

4. **Governance & Closure** (M3.4)
   - Problem record owner tracks action item completion
   - Enforcement mechanisms active (reminders, visibility, escalation)
   - Problem record closed when all action items completed or waived

---

## Measurement Framework

### M3.2: Action Item Plan Closure Rate (FORMAL V2MOM METRIC)
**Metric:** % of High/Critical post-mortem action items closed within OLA/Deadline

**Definition:** On-time closure rate for action items tracked via Problem Management process

**Target:** >80% by Q2 2027

**Collection Method:**
- Track action items from Problem records
- Filter for High/Critical priority
- Compare closure date to OLA/deadline
- Calculate % closed on-time vs. total

**Challenge:** Implementation requires solving governance problem (action items scattered across projects)

### M3.7: Problem Management Coverage (FORMAL V2MOM METRIC)
**Metric:** % of mandatory incidents with Problem records created

**Definition:** Percentage of incidents meeting Problem Management criteria that have corresponding Problem records created

**Target:** >90% by Q4 2026

**Collection Method:**
- Identify incidents meeting mandatory criteria (e.g., status page incidents)
- Check if Problem record exists
- Calculate % with Problem records vs. total mandatory incidents

**Purpose:** Measures adoption of Problem Management process

---

## Open Questions

### Resolved
- ✓ Dual purpose confirmed: Action item tracking + customer-facing artifact

### Still To Define

**Process Design:**
1. **Mandatory criteria:** Which incidents require Problem Management? (All status page incidents? High/Critical only? Customer-impacting?)
2. **Governance model:** Centralized vs. federated vs. hybrid? (Option C hybrid recommended but needs validation)
3. **Ownership model:** Who owns Problem record? (Option 4 rotational recommended but needs validation)
4. **Priority thresholds:** What defines High/Critical action items requiring OLA/deadline?
5. **OLA/deadline framework:** What are standard OLAs for High/Critical action items? (2 weeks? 4 weeks? Case by case?)

**Integration & Tooling:**
6. **Jira workflow:** What workflow states for Problem records? (Open → In Progress → Resolved → Closed?)
7. **Automation requirements:** What automation needed for federated action item aggregation?
8. **RDINC integration:** How does Problem Management integrate with existing RDINC workflow?
9. **GS tooling:** How does GS access Problem records for customer communication?

**Measurement & Governance:**
10. **Baseline metrics:** What are current action item completion rates (if measurable)?
11. **Closure criteria:** When can a Problem record be closed? (All action items done? Partial completion allowed?)
12. **Waiver process:** Can action items be waived/deprioritized? If so, by whom?
13. **Escalation path:** What happens to stalled Problem records? Who escalates?

---

## Success Metrics Summary

By Q4 2026:
- ✓ >90% Problem Management coverage (M3.7) - mandatory incidents have Problem records
- ✓ Problem record ownership model operational
- ✓ Governance mechanism functional (centralized visibility, enforcement)
- ✓ Customer-facing artifact working (GS can share progress)

By Q2 2027:
- ✓ >80% action item closure rate (M3.2) - High/Critical items closed within OLA

---

## Risks & Mitigation Strategies

**Risk 1: Governance model unclear**
- **Impact:** Medium - may cause adoption delays
- **Mitigation:** Define governance model in Q2 2026 practice definition, validate in Q3 2026 pilot

**Risk 2: Problem record ownership unclear**
- **Impact:** High - risk of abandoned Problem tickets
- **Mitigation:** Define ownership model with clear accountability, test in pilot before full rollout

**Risk 3: Action items still scattered across team projects**
- **Impact:** High - difficult to enforce centralized tracking
- **Mitigation:** Hybrid model (Option C) balances governance for critical items with team autonomy

**Risk 4: Teams resist centralized governance**
- **Impact:** Medium - perceived as bureaucracy
- **Mitigation:** Frame as quality assurance and customer communication, not compliance theater; involve teams in design

**Risk 5: Low action item closure rates**
- **Impact:** Medium - M3.2 target at risk
- **Mitigation:** Enforcement mechanisms (reminders, Operations Review visibility, escalation), coaching for low-performing value streams

**Risk 6: Customer-facing artifact doesn't meet GS needs**
- **Impact:** Medium - Goal 2 (external) not achieved
- **Mitigation:** Co-design with GS, validate in pilot before full rollout

---

## Notes from Planning

### 2026-04-04 — Initial Design
- Documented Problem Management dual purpose from GS workshop
- Identified governance challenge (action items scattered across projects)
- Defined open questions for Q2 2026 practice definition phase
- Created initiative folder structure
- Aligned with V2MOM metrics (M3.2, M3.7)

---

*Last updated: 2026-04-04*
