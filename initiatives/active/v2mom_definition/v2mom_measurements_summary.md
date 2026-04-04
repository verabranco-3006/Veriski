# V2MOM 2026 - Measurements Summary

**Purpose:** High-level overview of all V2MOM measurements for review and decision-making
**Date:** April 4, 2026
**V2MOM Period:** Q2 2026 - Q1 2027

---

## Method 1: O11 FedRAMP Operational Enablement

### M1.1: 3PAO Design Integrity ✓ FORMAL V2MOM METRIC

**Metric:** Number of process-related findings classified as "Deficient" or "Non-Compliant" during formal 3PAO assessment

**Definition:** Process-related findings from Knox 3PAO assessment in "Management" and "Operational" control families

**Target:** 0 findings by end of Q3 2026 (audit window)

**Owner:** Vera Branco

---

### M1.2: Control Adherence (First Customer) ✓ FORMAL V2MOM METRIC

**Metric:** % of tickets and actions for first FedRAMP customer adhering to operational frameworks and OLAs during first 60 days of production

**Definition:** Compliance rate for all incident, change, and problem tickets for first FedRAMP customer

**Target:** > 95% during first 60 production days (Q4 2026)

**Owner:** Vera Branco

---

## Method 2: Transform Change Management

### M2.1: Change Lead Time Reduction ✓ FORMAL V2MOM METRIC

**Metric:** % reduction in mean time from "RFC Creation" to "Implementation" for Normal Changes

**Definition:** Average lead time for Normal Changes compared to H2 2025 validated baseline (16 days)

**Target:** -30% reduction by Q2 2027 (11 days target)

**Intermediate Milestones:**
- Q3 2026: 15 days (-6%)
- Q4 2026: 14 days (-12%)
- Q1 2027: 12 days (-25%)
- Q2 2027: 11 days (-30%)

**Owner:** Laura Ferreira

---

### M2.2: Standard Change Promotion Rate — REQUIRES IN-DEPTH REVIEW

**Metric:** % increase in volume of changes transitioned from "Normal" to "Standard" track

**Definition:** Growth in number of Standard Change executions compared to baseline

**Target:** +50% increase by Q2 2027

**Owner:** Laura Ferreira

---

### M2.3: Manual Resilience Identification ✓ FORMAL V2MOM METRIC

**Metric:** % of reviewed Normal RFCs flagged as "Automation Candidate"

**Definition:** Percentage of Normal RFCs reviewed by CAB where the reviewer identifies the change as repetitive, manual, or automatable

**Target:** < 20% by Q1 2027

**Expected Trend:**
- Q2 2026: 30-40% (baseline, learning period)
- Q3 2026: 25-35% (protocol stabilized)
- Q4 2026: 20-30% (early automations implemented)
- Q1 2027: <20% (sustained automation)

**Owner:** Laura Ferreira

---

### M2.4: CFR Correlation Accuracy ✓ FORMAL V2MOM METRIC

**Metric:** % of Incidents where automated correlation system correctly identifies the specific asset-version change responsible for the failure

**Definition:** Accuracy rate of asset-version-to-incident correlation, validated against RCA findings

**Target:** > 90% by Q4 2026

**Owner:** Paulo Alves Monteiro

**Note:** Collection method and validation process to be defined aligned with correlation mechanism implementation

---

## Method 3: Incident Response Resilience

### Submethod 3.1: Failure Management Governance

**Note:** No measurements currently linked to this submethod.

---

### Submethod 3.2: Status Page Governance & OLA Compliance

### M3.1: Public MTTA (Status Page) ✓ FORMAL V2MOM METRIC

**Metric:** Mean time from system-wide impact declaration to first external status page post

**Definition:** Average time from system-wide impact declaration (by GS or SRE) to first public customer communication on status.outsystems.com (posted by GS Service Controllers after curating incident updates from Incident Commander)

**Target:** < 30 minutes by Q3 2026

**Expected Trend:**
- Q2 2026: 20-30 min (baseline with new process)
- Q3 2026: <30 min
- Q4 2026+: <20 min (optimization)

**Owner:** Inês Matos + GS Service Controllers

**Context:** Revised per GS workshop (March 2026) - IC Leader removed, GS can declare system-wide impact, GS Service Controllers curate incident updates and post to external status page

---

### M3.2: Action Item Plan Closure Rate ✓ FORMAL V2MOM METRIC

**Metric:** % of High/Critical post-mortem action items closed within OLA/Deadline

**Definition:** On-time closure rate for action items tracked via Problem Management process. Problem Management serves as the follow-up mechanism for action item lifecycle after incident resolution and provides customer-facing artifact to share progress with customers.

**Target:** > 80% by Q2 2027

**Owner:** Inês Matos

**Context:** Aligned per GS workshop (March 2026) - Problem Management as the ultimate mechanism for: 1) action item lifecycle tracking post-incident resolution, 2) customer-facing progress reporting

---

### Submethod 3.3: Triage Models & Operational Accountability

### M3.3: Triage Accuracy (Framework Validation) ✓ FORMAL V2MOM METRIC

**Metric:** % of tickets correctly categorized at intake (Service Incident vs Support Case)

**Definition:** % of incidents where initial classification (particularly GS-declared service incidents) is confirmed by SRE during initial troubleshooting. Measures accuracy of Service Incident vs Support Case separation framework designed with SRE and GS.

**Target:** > 80% by Q2 2027

**Owner:** Inês Matos

**Context:** Aligned per GS workshop (March 2026) - GS can declare service incidents, confirmed by SRE during initial troubleshooting (Challenge #1). Metric stress tests framework accuracy to enable refinement, particularly for GS-declared incidents.

**Note:** No agreement yet on engineering 24x7 coverage for high-urgent support cases, but GS empowered to declare service incidents independently

---

### M3.5: RCA Completion Rate & Lead Time ✓ FORMAL V2MOM METRIC

**Metric:** % of mandatory retrospectives completed within SLA + Average RCA lead time

**Definition:** Completion rate for incidents requiring retrospectives and average time from incident resolution to retrospective completion. All incidents posted to external status page are subject to RCA.

**Target:** > 90% completion rate and < 14 days RCA lead time by Q2 2027

**Owner:** Inês Matos

**Context:**
- Retrospective Transformation - Team-led model
- Aligned per GS workshop (March 2026) - All status page incidents require RCA (Challenge #3)

---

### M3.6: Incident Response Maturity Assessment ✓ FORMAL V2MOM METRIC

**Metric:** Average incident response maturity score across defined capability pillars

**Definition:** Stoplight assessment (Green/Yellow/Red) of team performance across incident response capability pillars (e.g., detection, troubleshooting, recovery, process compliance) based on what was/wasn't done during incident response. Pre-RCA assessment drives collaborative retrospective session focused on gaps (yellow/red areas).

**Target:** > 4.0/5.0 average maturity score by Q2 2027

**Owner:** Inês Matos + Process Engineering

**Purpose:**
1. **Maturity assessment:** Evaluate team preparedness and incident response capability
2. **RCA session focus:** Drive collaborative retrospective toward gaps (yellow/red pillars)
3. **Coaching prioritization:** Identify which teams need support to improve incident response
4. **Documentation:** AI/Koda produces output, but quality is measured by team maturity, not document quality

**Context:** Retrospective Transformation - Shift from output (what happened) to outcome (how well we responded and what to improve)

---

### Submethod 3.4: Problem Management Integration

### M3.7: Problem Management Coverage ✓ FORMAL V2MOM METRIC

**Metric:** % of mandatory incidents with Problem records created

**Definition:** Percentage of incidents meeting Problem Management criteria that have corresponding Problem records created to track action item lifecycle and provide customer-facing artifact

**Target:** > 90% by Q4 2026

**Owner:** Inês Matos

**Context:** Aligned per GS workshop (March 2026) - Problem Management as mechanism for action item tracking and customer communication. Measures adoption of new Problem Management process.

**Note:** Requires defining mandatory criteria (e.g., all status page incidents, high/critical incidents, customer-impacting incidents). See problem_management_notes.md for detailed context.

---

### Submethod 3.5: Retrospective Transformation

### M3.5: RCA Completion Rate & Lead Time ✓ FORMAL V2MOM METRIC

**Metric:** % of mandatory retrospectives completed within SLA + Average RCA lead time

**Definition:** Completion rate for incidents requiring retrospectives and average time from incident resolution to retrospective completion. All incidents posted to external status page are subject to RCA.

**Target:** > 90% completion rate and < 14 days RCA lead time by Q2 2027

**Owner:** Inês Matos

**Context:**
- Retrospective Transformation - Team-led model
- Aligned per GS workshop (March 2026) - All status page incidents require RCA (Challenge #3)

---

### M3.6: Incident Response Maturity Assessment ✓ FORMAL V2MOM METRIC

**Metric:** Average incident response maturity score across defined capability pillars

**Definition:** Stoplight assessment (Green/Yellow/Red) of team performance across incident response capability pillars (e.g., detection, troubleshooting, recovery, process compliance) based on what was/wasn't done during incident response. Pre-RCA assessment drives collaborative retrospective session focused on gaps (yellow/red areas).

**Target:** > 4.0/5.0 average maturity score by Q2 2027

**Owner:** Inês Matos + Process Engineering

**Purpose:**
1. **Maturity assessment:** Evaluate team preparedness and incident response capability
2. **RCA session focus:** Drive collaborative retrospective toward gaps (yellow/red pillars)
3. **Coaching prioritization:** Identify which teams need support to improve incident response
4. **Documentation:** AI/Koda produces output, but quality is measured by team maturity, not document quality

**Context:** Retrospective Transformation - Shift from output (what happened) to outcome (how well we responded and what to improve)

---

### Submethod 3.6: Event Management & Alert Validation

### M3.4: Alert Validation Accuracy (Event Management) ✓ FORMAL V2MOM METRIC

**Metric:** % of alerts correctly validated and filtered before triggering full incident response

**Definition:** % of alerts where Event Management validation decision (Trigger Incident Response / False Positive) matches actual outcome. Measures accuracy of formal Event Management practice that reviews and confirms alerts before triggering incident response.

**Target:** > 85% by Q2 2027

**Owner:** Inês Matos

**Problem Statement:** Currently RDINC collects both customer-reported incidents (support case escalations) and alerts (system-wide or service-specific SLO alerts). Both receive same treatment, but alerts can have false positives that don't require incident response.

**Goal:** Establish formal Event Management practice to:
1. Review alerts (system-wide impact alerts, service-specific SLO alerts)
2. Validate if alert requires incident response
3. Filter false positives before full incident response is triggered

**Phasing:** Practice definition Q2 2026 → Pilot & Baseline Q3 2026 → Scale Q4 2026 → Accuracy measurement Q1-Q2 2027

---

### M3.4a: Event Management Coverage ✓ FOUNDATIONAL METRIC

**Metric:** % of alerts processed through formal Event Management practice

**Definition:** Percentage of total alerts that go through Event Management review process vs. alerts that still go directly to incident response

**Target:** 100% by Q4 2026

**Owner:** Inês Matos

**Purpose:** Measures adoption - ensures alerts are routed through the new practice

---

### M3.4b: Alert Volume & Classification Baseline ✓ FOUNDATIONAL METRIC

**Metric:** Monthly alert volume by source and outcome

**Definition:** Track total alerts received, categorized by:
- Source: System-wide impact alerts / Service-specific SLO alerts / Development team alerts
- Outcome: Triggered incident / False positive / Auto-resolved

**Target:** Baseline established by Q3 2026, ongoing monitoring

**Owner:** Inês Matos

**Purpose:** Understand current state - volume and distribution of alerts to inform practice design

---

### M3.4c: False Positive Identification Rate ✓ FOUNDATIONAL METRIC

**Metric:** % of alerts identified as false positives by Event Management review

**Definition:** Percentage of alerts reviewed that are correctly identified as false positives and filtered before triggering incident response

**Target:** Baseline Q3 2026, >70% identification rate by Q4 2026

**Owner:** Inês Matos

**Purpose:** Measures practice effectiveness at catching false positives

---

### M3.4d: Event Review Lead Time ✓ FOUNDATIONAL METRIC

**Metric:** Mean time from alert received to Event Management validation decision

**Definition:** Average time from alert ingestion to validation decision (Trigger Incident / False Positive / Needs Investigation)

**Target:** < 15 minutes by Q4 2026

**Owner:** Inês Matos

**Purpose:** Measures practice efficiency - validation speed to prevent delayed incident response

---

## Method 4: Strategic Metrics Orchestration

### M4.1: Executive Metric Literacy ✓ FORMAL V2MOM METRIC

**Metric:** % of Leadership/End-Users who can correctly interpret calculation logic and navigate dashboards

**Definition:** Comprehension rate from quarterly literacy assessments (post-training quiz or survey with ≥80% pass criteria)

**Target:** > 85% by end of Q2 2026

**Owner:** Paulo Alves Monteiro

**Note:** Survey-based assessment to stakeholders

---

### M4.2: Documentation Lineage Coverage ✓ FORMAL V2MOM METRIC

**Metric:** % of CPTO metrics with full technical and functional lineage documentation

**Definition:** Coverage rate of data lineage and calculation maps in Metrics Library

**Target:** 100% by Q3 2026

**Owner:** Paulo Alves Monteiro

---

### M4.3: Dashboard Adoption Rate — REQUIRES PAULO REVIEW

**Metric:** % of target audience actively using dashboards (monthly active users)

**Definition:** Percentage of intended users who access dashboards at least once per month, measured via dashboard analytics

**Target:** > 75% by Q4 2026

**Owner:** Paulo Alves Monteiro

**Note:** Assess feasibility with Paulo - requires dashboard analytics tracking

---

### M4.4: Metric Data Quality Score — REQUIRES PAULO REVIEW

**Metric:** % of metrics passing monthly data quality validation checks

**Definition:** Percentage of metrics with accurate data, no calculation errors, proper data lineage, and within acceptable refresh thresholds

**Target:** > 98% by Q4 2026

**Owner:** Paulo Alves Monteiro

**Note:** Discuss with Paulo - may require PE to have different role in metrics governance than currently expected

---

### M4.5: 2027 Strategic Metrics Blueprint ✓ FORMAL V2MOM METRIC

**Metric:** Completion of strategic metrics blueprint for 2027

**Definition:** Define and document the strategic metrics required for 2027, including calculation logic, data sources, and implementation roadmap to ensure proactive measurement capability planning

**Target:** Blueprint completed and signed off by stakeholders by Q4 2026

**Owner:** Paulo Alves Monteiro

**Purpose:** Prepare future measurement capability and ensure 2027 metrics are planned proactively rather than reactively

---

## Method 5: AI-Enabled Organizational Capability

### M5.1a: AI Adoption Rate ✓ FORMAL V2MOM METRIC

**Metric:** % of team members actively using AI tools in weekly workflows

**Definition:** Weekly active usage of AI tools (Claude Code, Koda) tracked via survey or platform analytics

**Target:** 100% by end of Q2 2026

**Owner:** Vera Branco

---

### M5.1b: AI-Augmented Workflow Documentation ✓ FORMAL V2MOM METRIC

**Metric:** Number of documented AI-augmented workflow patterns for PE internal use

**Definition:** Count of documented patterns where AI augments PE team's internal workflows (AI as co-pilot with human in the loop). Examples: Operations Review prep using Claude, meeting preparation with AI assistance, data analysis with AI support.

**Target:** ≥ 5 documented patterns by Q2 2027

**Owner:** Vera Branco

**Scope:** Internal PE team workflows - how PE uses AI tools for their own work

**Focus:** PE team capability building and productivity gains

**Examples:**
- Operations Review preparation (data aggregation, trend analysis)
- Meeting preparation (1:1s, staff meetings, context gathering)
- Data analysis and pattern identification
- Metrics report generation
- Audit documentation preparation

**Note:** Secondary priority - focus on M5.3a (Engineering teams) first, document internal patterns as PE team adopts AI naturally

---

### M5.1c: Time Savings Through AI Augmentation ✓ FORMAL V2MOM METRIC

**Metric:** Average hours per week saved through AI augmentation

**Definition:** Self-reported time savings via quarterly survey measuring productivity gains from AI tool usage. Requires baseline establishment.

**Target:** 2-4 hours/week per team member by Q2 2027

**Owner:** Vera Branco

**Key Opportunities Identified:**
- **Operations Review prep:** Currently 2 days × 3 people (Laura, Inês, Vera) = 6 person-days every 2 weeks. Significant time sink that AI can reduce through data aggregation, trend analysis, and report generation.
- With new reorg, more similar reviews expected → amplifies time savings potential

**Current AI Usage:**
- Claude Code for centralizing initiative context
- (Additional patterns to be documented in M5.1b)

---

### M5.2a: Career Framework Completion ✓ FORMAL V2MOM METRIC

**Metric:** Completion of formal career framework for Business Process Analyst role family

**Definition:** Framework document completed, reviewed, and approved by People Team and CPTO

**Target:** Framework completed and approved by Q4 2026

**Owner:** Vera Branco

---

### M5.2b: Individual Development Plan Execution ✓ FORMAL V2MOM METRIC

**Metric:** % of team members with active Individual Development Plans executing quarterly milestones

**Definition:** Percentage of team members with IDPs who complete planned quarterly development activities

**Target:** 100% by end of Q2 2026 (quarterly tracking thereafter)

**Owner:** Vera Branco

---

### M5.2c: Team Engagement (eNPS) ✓ FORMAL V2MOM METRIC

**Metric:** Employee Net Promoter Score (eNPS) for Process Engineering team

**Definition:** Team engagement measured via Office Vibe eNPS or informal assessment mechanisms. Small team size (3 people) prevents direct eNPS visibility to manager, requiring indirect measurement or informal pulse checks.

**Target:** Positive eNPS score (>0) by Q2 2027, trending toward >20 (favorable)

**Owner:** Vera Branco

**Note:** Consider implementing informal assessment mechanisms (e.g., quarterly pulse checks, 1:1 engagement discussions) given small team size constraints with Office Vibe reporting

---

### M5.3a: Process Automation Delivery (for Engineering Teams) ✓ FORMAL V2MOM METRIC — PRIORITY

**Metric:** Number of automation solutions delivered from blueprint to production deployment

**Definition:** Count of automation solutions for PE-managed processes that complete the full cycle: Blueprint validated → Pilot deployed to production → Usage validated. Tracks both planning (blueprints) and execution (deployment with usage confirmation).

**Target:**
- 3-5 blueprints validated by Q2 2027
- ≥ 1 deployed to production with usage validation by Q2 2027

**Owner:** Paulo Alves Monteiro

**Scope:** Automation solutions for processes PE provides to Engineering teams

**Focus:** Building automation for others (higher priority than internal PE workflows)

**Examples:**
- RFC automated validation and quality checks (M2.4 automation candidate flagging)
- Event Management alert classification and filtering (M3.4 series)
- Retrospective quality assessment automation (M3.6 maturity scoring)
- Change-to-incident correlation engine (M2.5 CFR correlation)
- Problem Management workflow automation (M3.2, M3.7)

**Measurement Approach:**
- Track automation candidates through pipeline: Identified → Blueprint → Pilot → Production
- Success = At least 1 goes all the way from blueprint to validated production usage
- 3-5 at blueprint stage shows healthy pipeline for post-V2MOM execution

**Note:** Primary priority - focus here first before M5.1b internal patterns

---

## Method 6: Operational Excellence & Sustainability

### M6.1: Operational Capacity Allocation ✓ FORMAL V2MOM METRIC

**Metric:** % of team capacity allocated to transformation work vs operational tasks

**Definition:** Capacity allocation measured via Jira story points by epic category (Transformation vs Operational tasks)

**Target:** Transformation 50-60%, Operational tasks 40-50% by Q2 2027 (quarterly tracking)

**Owner:** Vera Branco

---

### M6.2: Process Orchestration Effectiveness (CAB & RCA) ✓ FORMAL V2MOM METRIC

**Metric:** Multiple metrics tracking governance and retrospective orchestration

**Definition:**
- M6.2a: CAB Prep Time (time spent preparing for monthly CAB)
- M6.2b: First-Pass Approval Rate (% of RFCs approved on first review without rework)
- M6.2c: RCA Orchestration Coverage (% of mandatory retrospectives with PE facilitation/orchestration support)

**Target:**
- CAB Prep Time: < 4 hours per session
- First-Pass Approval: > 85%
- RCA Orchestration Coverage: > 90%
Target date: Q2 2027 (quarterly tracking)

**Owner:** Vera Branco (executed in rotation across team)

**Context:** Covers both CAB orchestration (Submethod 6.1) and Retrospective Transformation facilitation (team-led RCA model with PE orchestration support)

---

### M6.3: Audit Request Fulfillment Rate ✓ FORMAL V2MOM METRIC

**Metric:** % of audit evidence and compliance requests fulfilled within agreed deadline

**Definition:** On-time delivery rate for audit-related requests (SOC2, FedRAMP, ISO, internal audits)

**Target:** > 95% by Q2 2027

**Owner:** Process Engineering team

---

### M6.4: Dashboard Operational Availability ✓ FORMAL V2MOM METRIC

**Metric:** % of V2MOM dashboards operational and accurate

**Definition:** Availability and data quality of measurement infrastructure - dashboards accessible, data accurate, visualizations render correctly

**Target:** > 98% by Q2 2027

**Owner:** Paulo Alves Monteiro

---

## Summary Statistics

**Total Measurements:** 35

**By Status:**
- Formal V2MOM Metrics: 29
- Foundational Metrics: 4 (M3.4a, M3.4b, M3.4c, M3.4d)
- Requires Paulo Review: 2 (M4.3, M4.4)
- Reference Only (Not in V2MOM): 2 (M1.3, M2.3)
- Requires Review: 1 (M2.2)

**By Method:**
- Method 1 (FedRAMP): 3 measurements (2 formal)
- Method 2 (Change Management): 5 measurements (3 formal)
- Method 3 (Incident Response): 11 measurements (7 formal + 4 foundational)
- Method 4 (Metrics Orchestration): 5 measurements (3 formal, 2 requires Paulo review)
- Method 5 (AI & Capability): 7 measurements (7 formal: M5.1a, M5.1b, M5.1c, M5.2a, M5.2b, M5.2c, M5.3a)
- Method 6 (Operational Excellence): 4 measurements (4 formal)

**Target Dates Distribution:**
- Q3 2026: 4 measurements
- Q4 2026: 4 measurements
- Q1 2027: 1 measurement
- Q2 2027: 23 measurements (V2MOM end)
- Quarterly tracking: 2 measurements

---

## Next Steps

1. **Review & Approve Targets:** Validate all targets and timeframes
2. **Resolve Open Items:**
   - M2.2: Complete in-depth review
   - M3.4: Pilot validation mechanism
3. **Implementation Planning:** Sync approved changes to detailed implementation document (v2mom_measurements_refined.md)
4. **Baseline Establishment:** Q2 2026 baseline collection for measurements without validated baselines

---

*Last updated: 2026-04-04*
