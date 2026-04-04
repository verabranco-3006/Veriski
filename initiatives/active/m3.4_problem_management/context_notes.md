# Problem Management - Context & Process Notes

**Purpose:** Capture context and process details for Problem Management integration with Incident Response and V2MOM measurements
**Date Created:** April 4, 2026
**Related V2MOM Metric:** M3.2 - Action Item Plan Closure Rate

---

## Context from GS Workshop (March 2026)

### Problem Management Dual Purpose

**Goal 1 (Internal):** Track action item lifecycle completion after incident resolution

**Goal 2 (External):** Customer-facing artifact to share progress with customers

---

## Current State - Action Item Tracking

### Current Process Flow
1. Retrospective completed
2. Each team with action items creates those items in their own Jira projects
   - Mix of item types: stories, tech improvements, etc.
3. Action items linked to original RDINC incident artifact

### Current Challenge: Governance
- **Problem:** Action items scattered across multiple team projects → hard to govern completion in structured way
- **Impact:** No centralized visibility or enforcement mechanism for action item completion

---

## Problem Management Integration Challenges

### Goal 1 Implementation (Track Action Item Completion)
**Same governance problem as current RDINC approach:**
- Action items will still be scattered across team projects
- Problem record creation doesn't solve centralized tracking

**Additional challenge:**
- Assigning ownership of Problem record to ensure completion
- Who owns the Problem ticket? Original incident team? Cross-functional coordinator?

### Goal 2 Implementation (Customer-Facing Artifact)
**Status:** ✓ Mechanism already implemented
- No additional challenges identified for customer-facing progress reporting

---

## Open Questions for Implementation Design

1. **Governance Model:** How to track action items across multiple team projects?
   - Option A: Centralized Problem Management project where all action items are created?
   - Option B: Federated model with automated aggregation/reporting?
   - Option C: Mandatory linking to Problem ticket with automated status roll-up?

2. **Ownership Assignment:** Who owns the Problem record?
   - Incident Commander?
   - Value Stream leader?
   - Process Engineering?
   - Rotational ownership model?

3. **Enforcement Mechanism:** How to ensure action item completion is governed?
   - Automated reminders?
   - Operations Review visibility?
   - SLA/OLA enforcement?

---

## Problem Management Process (To Be Added)

*User will provide additional Problem Management process documentation to be compiled here.*

---

## Related V2MOM Metrics

### M3.2: Action Item Plan Closure Rate
- **Metric:** % of High/Critical post-mortem action items closed within OLA/Deadline
- **Target:** > 80% by Q2 2027
- **Owner:** Inês Matos
- **Challenge:** Implementation requires solving governance problem described above

---

## Next Steps

1. **Receive Problem Management process documentation** from user
2. **Compile complete process** in this document
3. **Design implementation approach** that addresses governance challenges
4. **Define measurement mechanism** for M3.2 that works with chosen governance model

---

*Last updated: 2026-04-04*
