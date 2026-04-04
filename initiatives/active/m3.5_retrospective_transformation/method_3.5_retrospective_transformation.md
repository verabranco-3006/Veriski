# Method 3 - Submethod 3.5: Retrospective Transformation

**Owner:** Inês Matos

**Jira Epic:** RSA-881

---

## V2MOM Summary

**Summary:** Transform Incident Learning by Establishing Team-Led Outcome-Focused Retrospectives

**Description:** Shift retrospective ownership from SRE to asset-owning teams, establishing collaborative model with quality framework that focuses on outcomes (what changed, what we learned) rather than outputs (what happened).

---

## Objective

Transform retrospectives from SRE-led to team-led practice, establishing operational accountability and shifting from output-focused (what happened) to outcome-focused (what changed and what we learned) analysis.

---

## Problem Statement

Current retrospective process is inconsistent:
- Analysis is volunteer-based or enforced — no structured framework
- We don't invest in analysis when we should
- Key dimensions of analysis are left out
- SRE leads retrospectives but teams don't own the learning
- Focus on timeline/root cause (output) rather than learning/improvement (outcome)

This creates accountability gaps and prevents organizational learning from incidents.

---

## Scope

### In Scope
1. **Practice design:** Define team-led collaborative retrospective model
2. **Ownership model:** Teams with assets causing incidents lead retrospectives
3. **Quality framework:** AI/Koda-assisted auditing based on Production Readiness Checklist
4. **Completion tracking:** Ensure retrospectives happen within SLA
5. **Maturity assessment:** Measure incident response capability across teams
6. **Enablement:** Train value stream managers and engineering teams on new model
7. **Operations Review evolution:** Analytics-driven discussions per value stream

### Out of Scope
- PE facilitation/orchestration execution (covered in M6.2c)
- Problem Management and action item tracking (covered in Submethod 3.4)
- Status page communication and external stakeholder management (covered in Submethod 3.1)
- Event Management and alert validation (covered in Submethod 3.6)

---

## Target State

### Team-Led Collaborative Retrospective Model

**Ownership & Roles:**
- **Lead:** Team with asset causing the incident (operational accountability)
- **Reviewers:** Engineering Managers
- **Approvers:** Value Stream Leaders
- **Collaborators:**
  - Process Engineering (framework, governance, facilitation)
  - Quality (testing gaps, quality metrics)
  - SRE (reliability patterns, infrastructure)
  - Other impacted teams

**Approach:**
- **Offline-first:** No mandatory readouts (less bureaucracy, more autonomy)
- **AI/Koda-assisted auditing:** Automated quality evaluation based on framework
- **Framework-based:** Production Readiness Checklist as primary reference

**Narrative Shift:**
- **From:** Output-focused (timeline, root cause)
- **To:** Outcome-focused (what we learned, what changed, how we prevented recurrence)

---

## Retrospective Framework

### When Required (Mandatory)
- All incidents posted to external status page
- High/Critical incidents with customer impact
- Incidents with recurrence patterns
- Near-misses with high potential impact

### Structure

**1. Context Setting** (Asset-owning team)
- What happened (timeline)
- Customer impact
- Asset/system involved

**2. Analysis** (Collaborative)
- **Detection:** How did we find out? (detection ratio)
- **Response:** How did we respond? (MTTA, communication)
- **Root cause:** Why did it happen?
- **Contributing factors:** What else contributed?

**3. Outcomes** (What changed)
- Action items with owners
- Process improvements
- Technical improvements
- Monitoring/alerting improvements

**4. Learning** (Pattern identification)
- What did we learn?
- Similar incidents in the past?
- Preventable in the future?

---

## Operations Review Evolution

**From:** Retrospective completion tracked as binary output metric

**To:** Analytics drive discussions per value stream:
- **Detection Ratio:** How fast did we detect the issue?
- **SLO Coverage:** Was this failure covered by SLOs?
- **RCA Lead Time:** How quickly did we complete root cause analysis?
- **RCA Quality:** How thorough and actionable was the analysis?

**Enablement:**
- Process Engineering + SRE enable value streams and managers
- Value stream-specific analytics dashboards
- Train managers on using data to drive improvement

---

## Measurements

### M3.5: RCA Completion Rate & Lead Time
**Metric:** % of mandatory retrospectives completed within SLA + Average RCA lead time

**Target:** >90% completion rate and <14 days RCA lead time by Q2 2027

**Rationale:** Ensures retrospectives happen consistently and timely (team-led model execution)

---

### M3.6: Incident Response Maturity Assessment
**Metric:** Average incident response maturity score across defined capability pillars

**Target:** >4.0/5.0 average maturity score by Q2 2027

**Rationale:** Measures team capability and preparedness, drives outcome-focused retrospectives by assessing "how well we responded" vs "what happened"

**Approach:**
- Stoplight assessment (Green/Yellow/Red) of team performance across capability pillars (detection, troubleshooting, recovery, process compliance)
- Pre-RCA assessment drives collaborative retrospective session focused on gaps (yellow/red areas)
- AI/Koda produces maturity assessment, quality measured by team capability improvement

**Purpose:**
1. **Maturity assessment:** Evaluate team preparedness and incident response capability
2. **RCA session focus:** Drive collaborative retrospective toward gaps (yellow/red pillars)
3. **Coaching prioritization:** Identify which teams need support
4. **Outcome shift:** Focus on "how well we responded" not just "what happened"

---

## Roles & Responsibilities

### Asset-Owning Team
- Leads the retrospective
- Provides context and timeline
- Owns action items for their systems
- Completes retrospective within SLA

### Process Engineering
- Designs and maintains retrospective framework
- Facilitates retrospectives as neutral party (execution in M6.2c)
- Ensures framework adherence
- Tracks completion and quality
- Identifies cross-team patterns
- Provides coaching and enablement

### Quality
- Identifies testing gaps during retrospectives
- Suggests quality improvements
- Tracks quality metrics related to incidents

### SRE
- Provides infrastructure context
- Suggests reliability improvements
- Reviews SLO/monitoring coverage
- Collaborates during analysis

### Engineering Managers
- Review retrospectives (new role)
- Ensure team accountability
- Support team's learning and improvement

### Value Stream Leaders
- Approve retrospectives (maintained role)
- Drive value stream-level improvement based on analytics
- Sponsor retrospective transformation within value stream

---

## Implementation Approach

### Phase 1: Design & Proposal (Q2 2026)
**Timeline:** March - April 13, 2026

**Activities:**
- Document team-led collaborative model with confirmed roles
- Develop quality framework for RCA evaluation (AI/Koda-assisted)
- Create outcome-focused retrospective template based on Production Readiness Checklist
- Define metrics per value stream (# incidents, detection ratio, RCA lead time)
- Design maturity assessment framework (capability pillars, scoring)

**Alignment:**
- João Rodrigues takes proposal to Product Leadership
- Week of April 13, 2026: Present to VS Leaders & Engineering Managers

### Phase 2: Pilot & Enablement (Q2-Q3 2026)
**Activities:**
- Select 2-3 pilot value streams (early adopters)
- Run pilot retrospectives with PE coaching (offline-first approach)
- Brown Bag sessions to teach RCA best practices
- Train value stream managers and engineering managers on new model
- Establish AI/Koda-assisted auditing mechanisms
- Collect baseline metrics (detection ratio, RCA lead time, maturity scores)

### Phase 3: Full Rollout & Optimization (Q3 2026 - Q2 2027)
**Activities:**
- Roll out to all teams
- Track metrics per value stream (incidents, detection ratio, RCA lead time, maturity)
- Integrate with Operations Review (analytics-driven discussions)
- Refine framework based on feedback
- Automate quality checks and maturity assessment where possible
- Achieve M3.5 and M3.6 targets by Q2 2027

---

## Key Success Factors

1. **Operational accountability clear:** Teams that caused incidents own retrospectives
2. **Collaborative execution:** Process Engineering, Quality, SRE work together with teams
3. **Outcome-focused narrative:** Shift from "what happened" to "what changed and what we learned"
4. **Autonomy with framework:** Less bureaucracy, more autonomy within structured framework
5. **Quality assurance automated:** AI/Koda-assisted auditing reduces manual overhead
6. **Analytics drive improvement:** Operations Review uses data per value stream, not just completion tracking
7. **Enablement investment:** Brown Bags, coaching, training ensure teams can lead effectively

---

## Dependencies

- **Production Readiness Checklist finalized** (reference framework)
- **Reliability Platform principles documented** (guiding principles)
- **SRE buy-in and collaboration** during transition
- **Value Stream Leader sponsorship** for rollout
- **AI/Koda tooling integration** for automated auditing
- **M3.4 Problem Management** (for action item tracking post-retrospective)

---

## Risks & Mitigations

| Risk | Mitigation |
|------|-----------|
| Value stream managers lack confidence to lead | Start with pilot VSs (early adopters), PE provides hands-on coaching |
| Transition creates ownership confusion | Clear role definitions, documented handoff from SRE to teams |
| Auditing perceived as bureaucracy | Frame as quality assurance for learning, automated via AI/Koda |
| Teams focus on output vs outcome | Maturity assessment drives focus on "how well we responded" |
| Retrospectives delayed or incomplete | SLA tracking, automated alerts, escalation path to VS Leaders |

---

## Open Questions for Team Discussion

1. **Quality framework specifics:** What criteria will AI/Koda use to evaluate RCA quality? (M3.6 capability pillars)
2. **Mandatory retrospective criteria:** All status page incidents? High/Critical threshold?
3. **Timeline SLA:** How quickly after incident resolution should RCA be completed? (M3.5 target: <14 days)
4. **Pilot value streams:** Who are the early adopters for pilot phase?
5. **Maturity scoring methodology:** How to score Green/Yellow/Red across capability pillars? (M3.6)
6. **Brown Bag content:** What RCA best practices will be taught in enablement sessions?
7. **Operations Review integration:** How to present analytics per value stream? Dashboard design?

---

## Relationship to Other Submethods

**Submethod 3.1 (Customer Communication):** Retrospectives focus on internal learning; 3.1 handles external status page communication

**Submethod 3.2 (Triage & Declaration):** Triage determines which incidents require retrospectives; 3.5 defines the retrospective practice

**Submethod 3.4 (Problem Management):** Retrospectives identify patterns → Problem Management tracks action items and provides customer-facing artifact

**Submethod 3.6 (Event Management):** Event Management filters false positive alerts; retrospectives analyze incidents that reached full incident response

**M6.2c (RCA Orchestration):** Submethod 3.5 defines the practice and measures completion/quality; M6.2c measures PE facilitation/orchestration execution

---

*Last updated: 2026-04-04*
