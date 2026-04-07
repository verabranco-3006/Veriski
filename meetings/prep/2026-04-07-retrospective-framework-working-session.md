# Working Session Prep: Retrospective Preparation Framework
## April 7, 2026 | 11:00–12:00

**Attendees:** Vera Branco, Inês Matos

**Objective:** Define the pillars of the retrospective framework, clarify Quality's involvement, and refine the operating model

---

## Agenda Topics

### 1. Framework Pillars (Maturity Assessment)

**Background:**
- M3.6 metric uses "capability pillars" for maturity assessment
- Stoplight (Green/Yellow/Red) across pillars drives retrospective focus
- Pre-RCA assessment identifies gaps → retrospective focuses on yellow/red areas

**Current draft pillars from documents:**
- Detection
- Troubleshooting
- Recovery
- Process compliance

**Discussion points:**
- Are these the right pillars? Missing any?
- Should we add: Communication, Monitoring/Alerting, Action Items?
- How granular should pillars be?
- How do pillars map to Production Readiness Checklist?
- Scoring methodology: How to rate Green/Yellow/Red per pillar?

**Proposed structure for discussion:**
```
Pillar 1: Detection & Monitoring
- Was the incident detected automatically or customer-reported?
- Did SLOs/alerts work as expected?
- Detection lead time

Pillar 2: Response & Communication
- MTTA to acknowledge and start working
- Status page communication (Public MTTA)
- Stakeholder communication

Pillar 3: Troubleshooting & Root Cause
- Time to identify root cause
- Depth of analysis
- Contributing factors identified

Pillar 4: Recovery & Resolution
- MTTR
- Service restoration approach
- Verification of recovery

Pillar 5: Prevention & Learning
- Action items identified
- Systemic fixes vs band-aids
- Pattern identification (recurrence prevention)

Pillar 6: Process Compliance
- Retrospective SLA adherence
- Documentation quality
- Problem Management integration
```

---

### 2. Quality Involvement

**Current role definition:**
- Identifies testing gaps during retrospectives
- Suggests quality improvements
- Tracks quality metrics related to incidents

**Discussion points:**
- **Scope of involvement:** Every retrospective or only specific types?
- **When does Quality join?** Pre-RCA assessment? During collaborative session? Post-analysis review?
- **Quality metrics to track:** What specific metrics should Quality bring to retrospectives?
  - Test coverage for affected areas?
  - Bug escape rate?
  - Quality gate failures?
- **Ownership:** Is Quality a mandatory collaborator or optional based on incident type?
- **Output:** What should Quality deliver as part of the retrospective?
  - Testing gap assessment?
  - Quality improvement recommendations?
  - Metrics baseline for improvement tracking?

**Proposal for discussion:**
Quality joins retrospectives when:
- Incident root cause involves quality issues (missed test cases, quality gate bypasses, test coverage gaps)
- Incident recurs (pattern suggests systemic quality gaps)
- High/Critical customer-impacting incidents (mandatory)

Quality provides:
- Test coverage analysis for affected systems
- Quality gate compliance status
- Bug escape analysis (if applicable)
- Recommendations for testing improvements

---

### 3. Operating Model

**Confirmed elements:**
- **Lead:** Team with asset causing the incident
- **Reviewers:** Engineering Managers
- **Approvers:** Value Stream Leaders
- **Collaborators:** Process Engineering, Quality, SRE, other impacted teams

**Discussion points:**

**3.1 Workflow & Handoffs**
- When does PE get involved? After incident resolution? During retrospective?
- How does the team "trigger" the retrospective process?
- Who schedules the collaborative session (if needed)?
- When does the EM review happen? Before or after approval?
- What's the escalation path for incomplete/delayed retrospectives?

**3.2 AI/Koda-Assisted Auditing**
- What does AI/Koda automate?
  - Pre-RCA maturity assessment (capability pillars)?
  - Quality framework evaluation (completeness check)?
  - Pattern identification (similar past incidents)?
- What remains human-driven?
  - Collaborative session facilitation?
  - Deep-dive root cause analysis?
  - Action item prioritization?

**3.3 Offline-First Approach**
- No mandatory readouts → asynchronous collaboration?
- How does "offline-first" work with "collaborative model"?
  - Teams write retrospective offline → reviewers comment asynchronously?
  - Or: collaborative session happens offline (meeting), then documented?
- What triggers synchronous collaboration vs async review?

**3.4 Timeline & SLA**
- M3.5 target: <14 days RCA lead time
- Breakdown needed:
  - Incident resolution → Retrospective initiated: X days?
  - Retrospective initiated → Collaborative analysis: X days?
  - Analysis → Documentation complete: X days?
  - Documentation → EM review → VS Leader approval: X days?

**Proposed workflow for discussion:**
```
1. Incident Resolved
   ↓
2. PE identifies retrospective required (based on criteria)
   → Notifies asset-owning team + assigns in Jira
   ↓
3. Team conducts pre-work (timeline, context, initial analysis)
   → AI/Koda runs pre-RCA maturity assessment (identifies gaps)
   ↓
4. PE facilitates collaborative session (if needed)
   → Focus on yellow/red pillars from maturity assessment
   → Quality + SRE + impacted teams participate
   ↓
5. Team completes retrospective documentation (outcome-focused)
   → AI/Koda validates quality framework adherence
   ↓
6. Engineering Manager reviews
   → Ensures team accountability and learning captured
   ↓
7. Value Stream Leader approves
   → Retrospective complete, action items tracked via Problem Management
```

---

### 4. Open Questions to Resolve

**Framework Pillars (M3.6):**
- [ ] Finalize capability pillars for maturity assessment
- [ ] Define Green/Yellow/Red scoring criteria per pillar
- [ ] Map pillars to Production Readiness Checklist sections

**Quality Involvement:**
- [ ] Define mandatory vs optional Quality participation criteria
- [ ] Clarify Quality's deliverables for retrospectives
- [ ] Identify Quality metrics to track per incident

**Operating Model:**
- [ ] Document detailed workflow with timelines
- [ ] Define AI/Koda automation scope vs human collaboration
- [ ] Clarify "offline-first" execution with collaborative model
- [ ] Establish escalation path for overdue retrospectives

**Tooling & Integration:**
- [ ] How does AI/Koda integrate with Jira/Confluence?
- [ ] Where is maturity assessment stored and tracked?
- [ ] How do we surface retrospective analytics in Operations Review?

---

## Next Steps After Session

1. **Inês:** Refine framework pillars and scoring criteria based on discussion
2. **Vera:** Document Quality involvement model and sync with Quality leadership
3. **Vera + Inês:** Update operating model workflow with timelines
4. **Inês:** Prepare draft for April 13 presentation to VS Leaders & Engineering Managers

---

## Context Links

- Initiative tracker: `initiatives/active/m3.5_retrospective_transformation/_initiative.md`
- Working plan: `initiatives/active/m3.5_retrospective_transformation/plan.md`
- Submethod definition: `initiatives/active/m3.5_retrospective_transformation/method_3.5_retrospective_transformation.md`
- V2MOM measurements: M3.5 (RCA Completion), M3.6 (Maturity Assessment)

---

*Presentation to VS Leaders & Engineering Managers: Week of April 13, 2026*
