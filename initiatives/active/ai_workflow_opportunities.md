# AI-Augmented Workflow Opportunities for Process Engineering

**Purpose:** Capture AI use case opportunities for both internal PE workflows and processes provided to Engineering teams
**Date Created:** April 4, 2026
**Related V2MOM Metrics:** M5.1a (AI Adoption), M5.1b (Workflow Documentation), M5.1c (Time Savings)

---

## Context

**Goal:** Document ≥5 AI-augmented workflow patterns by Q2 2027 (M5.1b)

**Scope:**
1. **Internal PE workflows** - How PE team uses AI for their own work
2. **Processes for Engineering teams** - How AI augments processes PE provides to teams

**Target time savings:** 2-4 hours/week per team member by Q2 2027 (M5.1c)

---

## Current State

### Already Using AI
- **Claude Code:** Centralizing initiative context
- **Skills:** `/prep1o1`, `/morning`, `/daily-wrap-up` for personal productivity

### Current Time Sinks Identified
**Operations Review Preparation:**
- **Current:** 2 days × 3 people (Laura, Inês, Vera) = 6 person-days every 2 weeks
- **Problem:** Manual data aggregation, trend analysis, report generation
- **With new reorg:** More similar reviews expected → amplifies need for automation

---

## AI Opportunity Areas

### 1. Operations Review Preparation (HIGHEST ROI)

**Current Process:**
- Every 2 weeks: Laura, Inês, Vera spend 2 days preparing
- Pull data from multiple sources (Jira, dashboards, Confluence)
- Analyze trends manually
- Generate presentation materials
- Review and align on messaging

**AI Augmentation Opportunity:**
- Automated data aggregation from Jira/dashboards
- Trend identification and pattern recognition
- Draft narrative summaries
- Generate presentation outline
- Highlight exceptions and anomalies

**Estimated Time Savings:** 50-70% reduction → 3-4 person-days saved per cycle

**Implementation Approach:**
- Create `/ops-review-prep` skill
- Integrate with Jira, Power BI, Confluence
- Template-based report generation
- Human review and refinement

**Related Metrics:** M5.1c (time savings)

---

### 2. Data Analysis & Trend Identification (HIGH IMPACT)

**Current Process:**
- Manual Jira queries for incident/RFC/change trends
- Excel analysis for patterns
- Time-consuming pattern identification across datasets

**AI Augmentation Opportunity:**
- Natural language queries: "Show me RFC trends by category for Q1"
- Automated pattern recognition across incidents/changes
- Correlation analysis (e.g., changes → incidents)
- Exception detection

**Use Cases:**
- RFC volume and lead time trends (M2.1)
- Incident pattern analysis (M3 metrics)
- Change failure correlation (M2.5)
- Event Management alert patterns (M3.4)

**Estimated Time Savings:** 2-3 hours/week per analyst

**Related Metrics:** M2.1, M2.5, M3.4, M3.6

---

### 3. Meeting Preparation (HIGH IMPACT)

**Current Process:**
- Manually review person files, past 1:1 notes, action items
- Prepare talking points for staff meetings, skip-levels
- Context switching to gather information from multiple sources

**AI Augmentation Opportunity:**
- `/prep1o1` skill already exists for 1:1s
- Extend to staff meetings, skip-levels, prep-skip-level
- Auto-aggregate context from people files, initiatives, recent work
- Generate discussion agenda with priorities

**Estimated Time Savings:** 1-2 hours/week

**Current Skills:** `/prep1o1`, `/prep-skip-level`, `/staff-prep` already available

---

### 4. RFC Review & Automation Candidate Identification (HIGH IMPACT - Laura)

**Current Process:**
- CAB prep: Review Normal RFCs manually
- Assess risk/impact
- Identify automation candidates (M2.4)
- Read through change details and history

**AI Augmentation Opportunity:**
- Summarize RFC content and context
- Identify similar past RFCs
- Flag automation candidates based on criteria (repetitive, manual steps, frequency)
- Risk assessment support
- Generate CAB review notes

**Estimated Time Savings:** 2-3 hours/week (Laura)

**Related Metrics:** M2.4 (Manual Resilience Identification)

**Implementation Approach:**
- Create `/rfc-review` skill
- Integration with RFC Jira project
- Automation candidate flagging logic
- Link to M2.4 measurement

---

### 5. Incident & Retrospective Analysis (MEDIUM-HIGH IMPACT - Inês)

**Current Process:**
- Pre-RCA: Gather incident context from multiple sources
- Review incident timeline manually
- Identify patterns with past incidents
- Prepare for retrospective session

**AI Augmentation Opportunity:**
- Automated incident timeline generation
- Pre-RCA context aggregation (what happened during incident)
- Pattern matching with historical incidents
- Support M3.6 maturity assessment preparation (stoplight on capability pillars)
- Draft retrospective outline

**Estimated Time Savings:** 1-2 hours/week (Inês)

**Related Metrics:** M3.5 (RCA Completion), M3.6 (Maturity Assessment)

**Implementation Approach:**
- Create `/pre-rca-prep` skill
- Pull data from RDINC, Rootly, Slack incident channels
- Generate capability pillar assessment (detection, troubleshooting, recovery, compliance)
- Identify gaps for RCA discussion focus

---

### 6. Metrics Report Generation (HIGH IMPACT)

**Current Process:**
- Monthly/quarterly metric reports
- Manually pull data from multiple dashboards
- Write narrative summaries
- Identify trends and insights
- Format for stakeholders

**AI Augmentation Opportunity:**
- Automated report generation from dashboard data
- Narrative summaries of trends
- Exception highlighting (metrics off-target)
- Stakeholder-specific views
- Draft executive summaries

**Estimated Time Savings:** 1-2 hours/week

**Related Metrics:** M4.5 (Stakeholder Satisfaction)

---

### 7. Documentation Writing & Updates (MEDIUM IMPACT)

**Current Process:**
- Writing process documentation
- Updating existing procedures
- Maintaining Confluence pages
- Ensuring consistency across documents

**AI Augmentation Opportunity:**
- Draft documentation from bullet points or conversation
- Update existing docs with new information
- Generate process flowcharts/diagrams
- Consistency checks across related docs
- Version control and change tracking

**Estimated Time Savings:** 1-2 hours/week

---

### 8. Compliance & Audit Documentation (MEDIUM IMPACT - Seasonal)

**Current Process:**
- Preparing audit evidence
- Gathering documentation from Jira/Confluence
- Formatting for auditors
- Cross-referencing requirements

**AI Augmentation Opportunity:**
- Automated evidence collection
- Document generation for auditors
- Gap analysis against control requirements
- Evidence mapping to control families

**Estimated Time Savings:** 4-8 hours during audit season (concentrated benefit)

**Related Metrics:** M6.3 (Audit Request Fulfillment)

---

### 9. Action Item Tracking & Follow-up (LOW-MEDIUM IMPACT)

**Current Process:**
- Tracking action items across initiatives
- Checking status with owners
- Following up on overdue items
- Reporting progress

**AI Augmentation Opportunity:**
- Automated status aggregation from Jira
- Draft follow-up messages
- Progress summaries
- Risk flagging for blocked items

**Estimated Time Savings:** 1 hour/week

**Related Metrics:** M3.2 (Action Item Closure via Problem Management)

---

## Processes Provided to Engineering Teams

### 10. Change Management Automation (See change_management_skills_opportunities.md)

**Opportunity Areas:**
- Automated RFC quality checks
- Standard Change template generation
- Change impact assessment
- Post-implementation validation
- CFR correlation support (M2.5)

**Estimated Impact:** Reduce RFC lead time (M2.1), improve Standard Change promotion (M2.2)

---

### 11. Event Management Alert Validation

**Opportunity Areas:**
- Automated alert classification
- False positive pattern recognition
- Alert context enrichment
- Validation decision support

**Related Metrics:** M3.4 series (Event Management)

---

### 12. Incident Response Playbooks

**Opportunity Areas:**
- Context-aware playbook suggestions
- Automated troubleshooting guides
- Recovery procedure generation
- Escalation path recommendations

**Related Metrics:** M3.1 (MTTA), M3.6 (Maturity Assessment)

---

## Prioritization for M5.1b (≥5 Patterns to Document)

### Recommended Top 5 Patterns (Highest ROI)

1. **Operations Review Preparation** - Highest time savings, clear use case
2. **RFC Review & Automation Candidate Identification** - Directly supports M2.4
3. **Incident & Retrospective Analysis** - Supports M3.5, M3.6
4. **Data Analysis & Trend Identification** - Broad applicability across metrics
5. **Metrics Report Generation** - Supports M4.5, stakeholder communication

**Rationale:**
- Mix of internal PE work (1, 4, 5) and processes for teams (2, 3)
- Clear measurement connection to V2MOM metrics
- High time savings potential (2-4 hours/week target)
- Feasible to implement within V2MOM timeframe

---

## Implementation Approach

### Phase 1 (Q2-Q3 2026): Foundation
- Establish baseline time tracking (M5.1c)
- Pilot top 3 patterns with team
- Document initial patterns (start M5.1b)
- Gather feedback and refine

### Phase 2 (Q4 2026-Q1 2027): Scale
- Expand to 5+ documented patterns (M5.1b target)
- Train team on AI-augmented workflows
- Measure time savings (M5.1c)
- Achieve 100% adoption (M5.1a)

### Phase 3 (Q2 2027): Optimize
- Refine patterns based on usage
- Expand to additional use cases
- Validate time savings target achieved
- Share learnings with broader Engineering

---

## Success Metrics

By Q2 2027:
- **M5.1a:** 100% team adoption by Q2 2026 ✓
- **M5.1b:** ≥5 documented AI-augmented workflow patterns
- **M5.1c:** 2-4 hours/week time savings per team member

**Key Success Indicator:** Operations Review prep time reduced by 50-70% (from 6 person-days to <2 person-days)

---

## Next Steps

1. **Team Discussion:** Review opportunities and prioritize top 5 patterns
2. **Baseline Establishment:** Track current time spent on prioritized workflows (Q2 2026)
3. **Pilot Implementation:** Start with Operations Review prep (highest ROI)
4. **Documentation:** Create workflow pattern documentation as we implement
5. **Measurement:** Quarterly time savings survey (M5.1c)

---

*Last updated: 2026-04-04*
