# M3.5 — Event Management & Alert Validation
*Initiative Tracker*

## Overview

**V2MOM Alignment:** Method 3.5 — Reduce Incident Response Noise by Establishing Event Management & Alert Validation

**Jira Epic:** RSA-738

**Owner:** Inês Matos

**Collaborators:** SRE (alert owners), Development teams (alert creators), Process Engineering (framework & governance)

**Status:** Planning

**Started:** 2026-04-04

**Target Completion:** Q2 2027 (phased rollout Q2 2026 - Q2 2027)

---

## Jira Tracking

All sub-initiatives and tasks will be tracked under:
- **Epic:** [RSA-738](https://outsystemsrd.atlassian.net/browse/RSA-738)
- **Project:** RSA (Reliability & Service Assurance)

## Problem Statement

Currently in the Incident Response project (RDINC), we collect two types of artifacts:

1. **Customer-reported incidents** - Support cases escalated by Global Support
2. **Alerts** - Both system-wide impact alerts and service-specific SLO alerts created by Development teams

**Issue:** Both artifact types are subject to the same analysis and incident response treatment, but alerts can have **false positives** that don't actually require incident response attention.

**Impact:**
- Incident response noise reduces effectiveness
- False positives delay response to real incidents
- Alert quality remains unaddressed without feedback loop
- Unclear separation between alert validation and incident declaration

## Goal

Establish **Event Management** as a formal practice to:

1. **Separate alert intake from incident intake**
2. **Review and validate alerts** before triggering full incident response
3. **Filter false positives** to reduce noise and improve incident response efficiency
4. **Create formal practice** of event management that can trigger incident response only when alert review confirms it's needed

## Success Criteria

By Q2 2027, Event Management practice should achieve:

1. **100% alert coverage** (M3.4a) - All alerts go through validation
2. **>85% validation accuracy** (M3.4) - Validation decisions match actual outcomes
3. **>70% false positive filtering** (M3.4c) - Catching majority of false positives
4. **<15 min review time** (M3.4d) - Fast validation without delaying real incidents
5. **Reduced RDINC noise** - Fewer false positive incidents reaching incident response
6. **Improved alert quality** - Feedback loop drives better monitoring

## Key Decisions

*To be documented as decisions are made during implementation*

## Integration with Other Method 3 Submethods

**Submethod 3.1: Customer Communication Excellence**
- Event Management validation determines if status page communication needed
- System-wide impact alerts validated by Event Management may trigger status page posts (M3.1)

**Submethod 3.2: Triage & Incident Declaration**
- Event Management acts as pre-triage for alerts, separate from customer-reported incident triage
- Validated alerts handed off to triage with enriched context
- Supports triage accuracy (M3.3) by reducing false positive incidents

**Submethod 3.3: Retrospective Transformation**
- False positive patterns identified in Event Management inform RCA discussions
- Monitoring gaps identified during incidents feed back to alert validation criteria

**Submethod 3.4: Problem Management**
- Recurring false positive patterns may generate Problem records for systemic alert tuning
- Alert quality improvement tracked through Problem Management lifecycle

---

## Tasks

Tasks will be created in Jira under Epic RSA-738 by Inês.

### Q2 2026: Practice Definition
- [ ] Define Event Management validation criteria framework
- [ ] Design RDINC integration (separate intake channel, validation workflow)
- [ ] Identify pilot scope (which alert types to start with)
- [ ] Determine validation ownership model (SRE on-call, dedicated team, or hybrid)
- [ ] Document validation process and handoff protocols
- [ ] Define false positive feedback loop mechanism

### Q3 2026: Pilot & Baseline
- [ ] Establish baseline metrics (M3.4b - alert volume by source and outcome)
- [ ] Execute pilot with subset of alerts
- [ ] Measure coverage (M3.4a)
- [ ] Track false positive identification rate (M3.4c)
- [ ] Measure event review lead time (M3.4d)
- [ ] Refine validation criteria based on pilot learnings
- [ ] Document false positive patterns

### Q4 2026: Scale & Optimize
- [ ] Expand to 100% alert coverage (M3.4a target)
- [ ] Optimize validation process for <15 min review time (M3.4d target)
- [ ] Achieve >70% false positive identification rate (M3.4c target)
- [ ] Full RDINC integration operational
- [ ] Implement feedback loop to alert owners

### Q1-Q2 2027: Accuracy & Continuous Improvement
- [ ] Measure validation accuracy retrospectively (M3.4 target: >85%)
- [ ] Validate feedback loop effectiveness (alert quality improvements)
- [ ] Optimize based on accuracy data
- [ ] Document learnings and best practices

## Work Log

### 2026-04-04
**Submethod Design & Documentation**
- Created M3.5 submethod definition for V2MOM
- Documented Event Management practice context and implementation notes
- Defined measurement framework (M3.4 + M3.4a-d)
- Created initiative folder structure

## Links

- Context notes: `initiatives/active/m3.5_event_management/context_notes.md`
- Working plan: `initiatives/active/m3.5_event_management/plan.md`
- V2MOM measurements summary: `initiatives/active/v2mom_definition/v2mom_measurements_summary.md`
- GS workshop outcomes: `log/daily/2026-04-01.md`

## Risks & Dependencies

**Risks:**
- Validation ownership unclear - may cause delays in practice adoption
- Integration complexity with RDINC could slow pilot phase
- Alert owners may resist feedback loop if not framed as quality improvement
- Validation delays could impact real incident response times

**Dependencies:**
- RDINC project structure and workflow
- SRE/Development team collaboration on alert validation criteria
- Monitoring tool integrations (PagerDuty, Grafana, etc.)
- Jira workflow for alert intake separate from incident intake

**Mitigations:**
- Define ownership model in Q2 2026 practice definition phase
- Pilot approach (Q3 2026) validates integration before full scale
- Target <15 min review time (M3.4d) to prevent incident response delays
- Frame feedback loop as service quality improvement, provide actionable tuning recommendations

## Next Steps

1. **Q2 2026:** Begin practice definition phase
   - Define validation criteria framework
   - Identify pilot scope (alert types to start with)
   - Determine validation ownership model
   - Design RDINC integration approach
2. **Align with stakeholders:** SRE leadership, Development teams, Process Engineering

---

## Confluence Format (V2MOM Submethod)

**Copy-paste ready format for V2MOM Confluence page:**

### Submethod 3.5: Event Management & Alert Validation

**Owner:** Inês Matos

**Objective:** Establish formal Event Management practice to validate alerts before triggering incident response, filtering false positives and ensuring incident response resources focus on genuine customer-impacting events.

**Problem Statement:** Currently, RDINC collects both customer-reported incidents and alerts (system-wide, service-specific SLO alerts). Both receive the same incident response treatment, but alerts frequently have false positives consuming incident response capacity without customer impact.

**Scope:**
- Alert intake and categorization (system-wide, service-specific SLO, custom Development team alerts)
- Validation framework (criteria, workflow, handoff to incident response)
- RDINC integration (separate alert intake, validation before incident response activation)
- Feedback loop (false positive patterns, alert tuning recommendations)

**Phasing:**
- **Q2 2026:** Practice definition - validation criteria, RDINC integration design, pilot scope
- **Q3 2026:** Pilot & baseline - collect data (M3.4b), pilot validation, measure foundational metrics
- **Q4 2026:** Scale & optimize - 100% coverage (M3.4a), <15 min review time (M3.4d), >70% false positive identification (M3.4c)
- **Q1-Q2 2027:** Accuracy measurement - >85% validation accuracy (M3.4), continuous improvement

**Success Criteria (Q2 2027):**
- 100% alert coverage through validation (M3.4a)
- >85% validation accuracy (M3.4)
- >70% false positive identification (M3.4c)
- <15 min average review time (M3.4d)
- Reduced incident response noise
- Improved alert quality via feedback loop

**Measurements:** M3.4 (formal), M3.4a-d (foundational)

---

*Last updated: 2026-04-04*
