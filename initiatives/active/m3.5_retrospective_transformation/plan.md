# Retrospective Process Transformation — Working Plan

*This is the working document for strategy, design, and implementation notes.*

---

## Current State

**Problems Identified (João Rodrigues):**
- Analysis is volunteer-based or enforced — no middle ground
- We don't invest in analysis when we should
- Dimensions of analysis are left out

**Current Model:**
- SRE leads retrospectives
- Teams participate but don't own
- Focus on output (what happened) vs outcome (what changed)
- Inconsistent analysis depth

---

## Target State

**New Model: Team-Led, Collaborative Retrospectives**

### Ownership & Roles (CONFIRMED)
- **Lead:** Team with asset causing the incident
- **Reviewers:** Engineering Managers (NEW)
- **Approvers:** Value Stream Leaders (maintained)
- **Collaborators:**
  - Process Engineering (framework, governance)
  - Quality (testing gaps, quality metrics)
  - SRE (reliability patterns, infrastructure)
  - Other impacted teams

### Approach (CONFIRMED)
- **Offline-first:** No mandatory readouts
- **AI/Koda-assisted auditing:** Ensure RCA quality based on framework TBD
- **Quality assurance:** Framework-based evaluation of RCA completeness and depth

### Guiding Principles
Based on:
- Production Readiness Checklist (primary reference)
- Reliability Platform principles

### Narrative Shift
- **From:** Output-focused (timeline, root cause)
- **To:** Outcome-focused (what we learned, what changed, how we prevented recurrence)

### Message to Teams
- Less bureaucracy, more autonomy
- Focus on outcomes instead of outputs
- Collaborative process between all involved teams

---

## Operations Review Evolution

**Current:** Retrospective completion tracked as output metric

**Future:** Analytics drive discussions per value stream:
- **Detection Ratio:** How fast did we detect the issue?
- **SLO Coverage:** Was this failure covered by SLOs?
- **RCA Lead Time:** How quickly did we complete root cause analysis?
- **RCA Quality:** How thorough and actionable was the analysis?

**Enablement Required:**
- Process Engineering + SRE enable value streams and managers
- Create value stream-specific analytics dashboards
- Train managers on using data to drive improvement

---

## Retrospective Framework (Draft)

### When Required (Mandatory Ritual)
- All incidents impacting customers (system-wide or significant)
- Incidents with recurrence patterns
- Near-misses with high potential impact
- [TO DEFINE with SRE and Inês]

### Structure

**1. Context Setting** (Asset-owning team)
- What happened (timeline)
- Customer impact
- Asset/system involved

**2. Analysis** (Collaborative)
- Detection: How did we find out? (detection ratio)
- Response: How did we respond? (MTTA, communication)
- Root cause: Why did it happen?
- Contributing factors

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

## Roles & Responsibilities

### Asset-Owning Team
- Leads the retrospective
- Provides context and timeline
- Owns action items for their systems

### Process Engineering
- Facilitates (neutral party)
- Ensures framework adherence
- Tracks completion and quality
- Identifies cross-team patterns

### Quality
- Identifies testing gaps
- Suggests quality improvements
- Tracks quality metrics related to incident

### SRE
- Provides infrastructure context
- Suggests reliability improvements
- Reviews SLO/monitoring coverage

---

## Auditing Mechanism (Draft)

**What We Track:**
- Retrospective completion (yes/no)
- Completion timeline (within X days of incident resolution)
- Action item closure rate
- Quality score (outcome-focused vs output-focused)

**How We Track:**
- Operations Review dashboard per value stream
- Automated alerts for overdue retrospectives
- Quarterly review of action item closure rates

**Escalation Path:**
- Overdue retrospectives → Value stream manager notified
- Low action item closure → Process Engineering + value stream manager align
- Quality concerns → Spot-check and coaching

---

## Implementation Approach

### Phase 1: Design & Proposal (March - April 13, 2026)
- **Owner:** Process Engineering (Vera + Inês)
- **Activities:**
  - Document new collaborative model with confirmed roles (Lead: teams, Reviewers: EMs, Approvers: VS Leaders)
  - Develop quality framework for RCA evaluation (AI/Koda-assisted)
  - Create outcome-focused retrospective template
  - Define metrics per area (# incidents, detection ratio, RCA lead time)
- **Alignment:** João Rodrigues takes proposal to Product Leadership
- **Milestone:** Week of April 13, 2026 — Present to VS Leaders & Engineering Managers

### Phase 2: Pilot & Enablement (Q2-Q3 2026)
- Select 2-3 pilot value streams
- Run pilot retrospectives with coaching (offline-first approach)
- Brown Bag sessions to teach RCA best practices
- Train all value stream managers and engineering managers on new model
- Establish AI/Koda-assisted auditing mechanisms

### Phase 3: Full Rollout & Optimization (Q3-Q4 2026)
- Roll out to all teams
- Track metrics per area (incidents, detection ratio, RCA lead time)
- Integrate with Operations Review
- Refine framework based on feedback
- Automate quality checks where possible

---

## Open Questions

**Resolved:**
- ✓ Ownership model: Teams lead, EMs review, VS Leaders approve
- ✓ Approach: Offline-first (no mandatory readouts)
- ✓ Quality assurance: AI/Koda-assisted auditing

**Still To Define:**
1. **Quality framework specifics:** What criteria will AI/Koda use to evaluate RCA quality?
2. **Mandatory retrospective criteria:** All incidents? Threshold based on severity/impact?
3. **Timeline expectations:** How quickly after incident resolution should RCA be completed?
4. **Pilot value streams:** Who are the early adopters for pilot phase?
5. **Tooling integration:** How does AI/Koda auditing integrate with existing tools (Jira/Confluence)?
6. **Metrics baseline:** What are current detection ratio, RCA lead time benchmarks per area?
7. **Brown Bag content:** What RCA best practices will be taught in enablement sessions?

---

## Notes from Meetings

### 2026-03-12 — Retrospective Process Review
- SRE leadership aligned on team-led model
- Emphasis on enabling value streams, not dictating process
- Narrative recreation needed: outcome over output
- Operations Review will use analytics to drive discussions
- Process Engineering + SRE partnership critical for enablement

### 2026-03-13 — Inês's Follow-Up Notes
**Tracking:** [Slack #retrospective-transformation](https://outsystems.enterprise.slack.com/archives/C0AL7MA0KBL)

**Confirmed decisions:**
- Roles defined: Teams lead, EMs review, VS Leaders approve
- Offline-first approach (no mandatory readouts)
- AI/Koda-assisted quality auditing
- Production Readiness Checklist as reference
- Metrics to track: # incidents, detection ratio, RCA lead time

**Key milestone:** Week of April 13, 2026 — Present new model to VS Leaders & Engineering Managers

**Next actions:**
- Process Engineering: Start proposal development
- João Rodrigues: Align with Product Leadership
- Develop quality framework for AI/Koda auditing
- Plan Brown Bag sessions for RCA best practices

---

*Last updated: 2026-03-13*
