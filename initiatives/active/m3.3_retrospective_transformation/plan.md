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

### Ownership
- **Team with asset causing incident** leads the retrospective
- Collaborates with:
  - Process Engineering (framework, governance)
  - Quality (testing gaps, quality metrics)
  - SRE (reliability patterns, infrastructure)
  - Other impacted teams

### Guiding Principles
Based on:
- Production Readiness Checklist
- Reliability Platform principles

### Narrative Shift
- **From:** Output-focused (timeline, root cause)
- **To:** Outcome-focused (what we learned, what changed, how we prevented recurrence)

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

### Phase 1: Design & Pilot (Q2 2026)
- Document collaborative model
- Create retrospective template (outcome-focused)
- Select 2-3 pilot value streams
- Run pilot retrospectives with coaching

### Phase 2: Enablement (Q3 2026)
- Train all value stream managers
- Roll out to all teams
- Establish auditing mechanisms
- Integrate with Operations Review

### Phase 3: Optimization (Q4 2026)
- Review analytics (detection, SLO, RCA metrics)
- Refine framework based on feedback
- Automate tracking where possible

---

## Open Questions

1. **Criteria for mandatory retrospectives?** (All incidents? Threshold?)
2. **Timeline expectations?** (How quickly after incident resolution?)
3. **Quality scoring?** (How do we measure outcome-focus objectively?)
4. **Pilot value streams?** (Who are early adopters?)
5. **Retrospective duration?** (30 min? 60 min? Depends on complexity?)
6. **Tooling?** (Where do we run these? Confluence? Jira? Live sessions?)

---

## Notes from Meetings

### 2026-03-12 — Retrospective Process Review
- SRE leadership aligned on team-led model
- Emphasis on enabling value streams, not dictating process
- Narrative recreation needed: outcome over output
- Operations Review will use analytics to drive discussions
- Process Engineering + SRE partnership critical for enablement

*Waiting for detailed notes from Inês*

---

*Last updated: 2026-03-12*
