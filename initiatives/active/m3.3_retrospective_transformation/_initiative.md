# M3.3 — Retrospective Process Transformation
*Initiative Tracker*

## Overview

**V2MOM Alignment:** Method 3.3 — Clarify Operational Accountability by Refining Triage Models & OLAs

**Jira Epic:** RSA-728 (parent initiative for all sub-tasks and tracking)

**Owner:** Inês Matos

**Collaborators:** Vera Branco (Process Engineering Lead), SRE Leadership (Pedro Charola), ODC Leadership (João Rodrigues - Value Stream Leader, key influencer), Release Engineering (João Brandão - Manager)

**Status:** Planning

**Started:** 2026-03-12

**Target Completion:** Q2 2026

---

## Jira Tracking

All sub-initiatives and tasks will be tracked under:
- **Epic:** [RSA-728](https://outsystemsrd.atlassian.net/browse/RSA-728)
- **Project:** RSA (Reliability & Service Assurance)

Tasks to be created by Inês after plan refinement.

## Problem Statement

Current retrospective process is inconsistent — analysis is based on volunteers or enforced approaches, not structured frameworks. We don't invest in analysis when we should, and we leave dimensions out. This creates accountability gaps and prevents learning from incidents.

## Goal

Transform retrospectives from SRE-led to team-led, establishing clear operational accountability and shifting from output-focused to outcome-focused analysis.

## Success Criteria

1. Retrospectives are led by teams whose assets caused incidents (operational accountability)
2. Teams collaborate with Process Engineering and Quality using established principles
3. Production Readiness Checklist and Reliability Platform guide retrospective structure
4. Operations Review analytics (detection ratio, SLO coverage, RCA lead time/quality) drive value stream discussions
5. Auditing mechanisms ensure retrospectives are conducted and tracked

## Key Decisions

**Date: 2026-03-12 — Retrospective Process Review Meeting**
- Shift from SRE-led to team-led retrospectives
- Teams with assets causing incidents own the retrospective
- Collaborative model: Process Engineering + Quality + impacted teams
- Narrative shift: outcome-based, not output-based
- Operations Review will evolve to use analytics per value stream

## Tasks

Tasks will be created in Jira under Epic RSA-728 by Inês after plan refinement.

### Planning & Design
- [ ] Document new collaborative model (team-led vs SRE-led)
- [ ] Define roles: Asset-owning team, Process Engineering, Quality, SRE
- [ ] Create retrospective principles based on Production Readiness Checklist
- [ ] Design auditing mechanisms for Operations Review tracking
- [ ] Define outcome-based metrics vs output metrics

### Enablement
- [ ] Process Engineering + SRE: Create enablement materials for value streams
- [ ] Define narrative templates (outcome-focused)
- [ ] Train value stream managers on leading retrospectives
- [ ] Pilot with 2-3 value streams

### Operations Review Integration
- [ ] Define analytics to drive discussions (detection ratio, SLO coverage, RCA lead time/quality)
- [ ] Create value stream-specific dashboards
- [ ] Update Operations Review format to support new model

### Governance
- [ ] Establish mandatory retrospective criteria (when required)
- [ ] Create auditing mechanism (tracking completion, quality)
- [ ] Define escalation path for incomplete retrospectives

## Work Log

### 2026-03-12
**Retrospective Process Review Meeting**
- Attendees: Pedro Charola (SRE Leadership), João Rodrigues (ODC Leadership, Value Stream Leader), João Brandão (Release Engineering Manager), Inês Matos (lead), Vera Branco
- Identified problems with current volunteer/enforced model
- Agreed on shift to team-led retrospectives guided by Production Readiness Checklist
- Discussed Operations Review evolution with analytics-driven discussions
- Established narrative shift requirement: outcome over output
- Action: Inês to refine plan and create Jira tasks under RSA-728

## Links

- Meeting notes: `meetings/raw/2026-03-12-retrospective-process-review.md`
- V2MOM M3.3 details: `log/daily/v2mom_measurements_refined.md` (line 887+)
- M3.3 drill-down with Inês: `meetings/raw/2026-03-09-submethod-m33-ines.md`

## Risks & Dependencies

**Risks:**
- Value stream managers may lack confidence to lead retrospectives initially
- Transition period could create confusion about ownership
- Auditing mechanisms might be perceived as bureaucracy if not properly framed

**Dependencies:**
- Production Readiness Checklist finalized
- Reliability Platform principles documented
- SRE buy-in and active collaboration during transition

**Mitigations:**
- Start with pilot value streams (early adopters)
- Process Engineering + SRE provide hands-on coaching during transition
- Frame auditing as quality assurance, not compliance theater

## Next Steps

1. **Inês:** Share detailed meeting notes from today's session
2. **Vera + Inês:** Document collaborative model and role definitions
3. **Team:** Identify pilot value streams for initial rollout
4. **Inês:** Draft outcome-based narrative template

---

*Last updated: 2026-03-12*
