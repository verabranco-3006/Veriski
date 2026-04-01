**Workshop Dates:** March 30-31, 2026

**Purpose:** Track problem statements, impacts, and proposed solutions for GS-Engineering alignment challenges

**Slidedeck for the Workshop:** https://docs.google.com/presentation/d/1pj-5kVmiR4jErRKJxZT7mGKcsL6o674XL69IlCSyVlU/edit?slide=id.g141f332568c_0_101#slide=id.g141f332568c_0_101

---

## Challenge #1 — Service Incidents vs Support Cases Paradigm

### Problem Statement

Service incidents and support cases are conflated in the current escalation model. High-priority support cases are automatically routed to SRE using severity mapping (Urgent/High → SEV1/SEV2), regardless of actual system-wide impact. This forces SRE to validate each escalation and hand-over non-systemic issues back to product teams, creating organizational drag and resource waste.

### Impact

- **On Engineering:** Wasted resources pulling highly specialized SRE staff into non-systemic issues during recovery and aftermath (complex retrospectives for what should be standard Problem Management)
- **On SRE:** Staff exhaustion from over-escalation, diverted from critical system stability work
- **On Organization:** Misalignment of expectations across stakeholders due to ambiguity in ownership and urgency definitions. Confused reporting and misalignment — single MTTR metric blurs system stability issues with customer-specific support cases

### Proposed Solutions

_To be defined during workshop_

### Decisions Needed

- [ ] Define clear separation between Service Incidents and Support Cases
- [ ] Establish validation process for system-wide impact assessment
- [ ] Clarify ownership model and escalation criteria

---

## Challenge #2 — Customer Communications Ownership

### Problem Statement

SRE continues to manage customer communications during incident response and request fulfillment for O11.

### Impact

- **On Customers:** Inconsistent communication quality, unclear single point of contact
- **On SRE:** Time spent on customer-facing activities instead of technical resolution, role confusion

### Proposed Solutions

_To be defined during workshop_

### Decisions Needed

- [ ] GS commits to owning customer communications for incidents and request fulfillment
- [ ] Timeline for transition (with clear milestones)
- [ ] Training and documentation support needed from SRE

---

## Challenge #3 — Learning Together

### Problem Statement

Combined challenge addressing RCA communication and collaboration. GS delivers RCAs on cloud incidents either without alignment with SRE/Engineering or simply sends the RCA over. They pick and choose based on unknown criteria. One-sided approach that prevents organizational learning.

### Impact

- **On Customers:** Incomplete or inaccurate RCAs, delays in receiving RCA communications, inconsistent experience
- **On Engineering:** Blindsided by RCAs we didn't contribute to, constantly pulled in to lead RCA calls with customers
- **On GS:** Lack of accountability for customer impact portions and customer-facing functions that are core to support

### Proposed Solutions

_To be defined during workshop_

### Decisions Needed

- [ ] Define clear ownership: Engineering owns technical analysis, GS owns customer impact and delivery
- [ ] Establish collaboration model for RCA creation
- [ ] GS commits to owning RCA communication to customers
- [ ] Commit to joint accountability for quality RCAs

---

## Challenge #4 — Swarming at SEV-1/SEV-2 Incidents

### Problem Statement

GS escalates through process without formal warm hand-over. No effective collaboration during severe incidents. Many times, GS doesn't escalate an incident, most of the times in O11 — just the change they want SRE to execute. Operational ownership is blurred, GS makes decisions on production changes without alignment with SRE/Engineering - who are the actual accountables and responsibles for it.

### Impact

- **On Customers:** Increased response times, poor expectation management, worse outcomes during critical incidents
- **On SRE:** Lack of coordination, unclear context, reactive execution without understanding the full picture

### Proposed Solutions

_To be defined during workshop_

### Decisions Needed

- [ ] Define swarming protocol for SEV-1/SEV-2 incidents (L3 + SRE collaboration)
- [ ] Establish warm hand-over process with clear context sharing
- [ ] Commit to escalating incidents (not just changes) with full collaboration

---

## Challenge #5 — System-Wide Impact Communication

### Problem Statement

System-wide incidents are failing to communicate effectively—to Engineering internally and to customers externally. The current IC Leader model (VS/EM) creates role redundancy and delays, while SRE already holds the full technical context needed for updates.

### Impact

- **On Engineering:** Role redundancy and toil—VS/EM pulled into on-call for IC Leader role, creating inefficient dependency and communication overhead
- **On SRE:** Forced to coordinate through VS/EM intermediaries when they already hold the full technical context needed for updates
- **On Customers:** Direct impact on External Status Page updates due to internal communication failures, information vacuum on root cause identification

### Proposed Solutions

_To be defined during workshop_

### Decisions Needed

- [ ] Remove VS/EM as IC Leader—SRE owns incident communication directly
- [ ] Commit to Internal Status Page visibility for all system-wide incidents
- [ ] GS owns External Status Page updates based on incident lifecycle
- [ ] Enforce complete lifecycle communication

---

## Challenge #6 — Customer Support Level Entitlement

### Problem Statement

_To be provided by Global Support_

### Impact

_To be defined during workshop_

### Proposed Solutions

_To be defined during workshop_

### Decisions Needed

- [ ] TBD

---

## Challenge #7 — Severities Alignment

### Problem Statement

_To be provided by Global Support_

### Impact

_To be defined during workshop_

### Proposed Solutions

_To be defined during workshop_

### Decisions Needed

- [ ] TBD

---

## Challenge #8 — Resolution Times

### Problem Statement

_To be provided by Global Support_

### Impact

_To be defined during workshop_

### Proposed Solutions

_To be defined during workshop_

### Decisions Needed

- [ ] TBD

---

## Challenge #9 — Status Page

### Problem Statement

_To be provided by Global Support_

### Impact

_To be defined during workshop_

### Proposed Solutions

_To be defined during workshop_

### Decisions Needed

- [ ] TBD

---

## Challenge #10 — Monitoring

### Problem Statement

_To be provided by Global Support_

### Impact

_To be defined during workshop_

### Proposed Solutions

_To be defined during workshop_

### Decisions Needed

- [ ] TBD

---

## Challenge #11 — Premium Support

### Problem Statement

_To be provided by Global Support_

### Impact

_To be defined during workshop_

### Proposed Solutions

_To be defined during workshop_

### Decisions Needed

- [ ] TBD

---

## Decisions & Action Items

### Decisions Made

_To be captured during workshop_

1.
2.
3.
4.
5.

### Action Items

| Action | Owner | Timeline | Status |
|--------|-------|----------|--------|
|        |       |          |        |
|        |       |          |        |
|        |       |          |        |

### Follow-up

- Next checkpoint:
- Documentation location:
- Status review cadence:

---

**Last Updated:** 2026-03-30
**Owners:** Vera Branco (Process Engineering), [VP Global Support TBD]
