**Governance ID -** \[PE-STRAT-03\] 

**Current Version -** 1.0

**Release Date -** <custom data-type="date" data-id="id-0">4/4/2026</custom>

**Status -**  <custom data-type="status" data-id="id-1">Work in progress</custom>

---

**Table of Contents**

---

## Method 1: AI Transformation

### M1.1a: AI Adoption Rate

**Metric:** % of team members actively using AI tools in weekly workflows

**Definition:** Weekly active usage of AI tools (Claude Code, Koda) tracked via survey or platform analytics

**Target:** 100% by end of Q2 2026

**Owner:** <custom data-type="mention" data-id="id-2">@Vera Branco</custom> 

---

### M1.2b: Time Savings Through AI Augmentation

**Metric:** Average hours per week saved through AI augmentation

**Definition:** Self-reported time savings via quarterly survey measuring productivity gains from AI tool usage. Requires baseline establishment.

**Target:** 2-4 hours/week per team member by Q2 2027

**Owner:** <custom data-type="mention" data-id="id-3">@Vera Branco</custom> 

**Key Opportunities Identified:**

* **Operations Review prep:** Currently 2 days × 3 people (Laura, Inês, Vera) = 6 person-days every 2 weeks. Significant time sink that AI can reduce through data aggregation, trend analysis, and report generation.
* With new reorg, more similar reviews expected → amplifies time savings potential

**Current AI Usage:**

* Claude Code for centralizing initiative context

---

### M1.3a: Process Automation Delivery (for Engineering Teams)

**Metric:** Number of automation solutions delivered from blueprint to production deployment

**Definition:** Count of automation solutions for PE-managed processes that complete the full cycle: Blueprint validated → Pilot deployed to production → Usage validated. Tracks both planning (blueprints) and execution (deployment with usage confirmation).

**Target:**

* 3-5 blueprints validated by Q3 2026
* ≥ 1 deployed to production with usage validation by Q2 2027

**Owner:** <custom data-type="mention" data-id="id-4">@Paulo Alves Monteiro</custom> 

**Scope:** Automation solutions for processes PE provides to Engineering teams

**Focus:** Building automation for others (higher priority than internal PE workflows)

**Examples:**

* RFC automated validation and quality checks (M2.4 automation candidate flagging)
* Event Management alert classification and filtering (M3.4 series)
* Retrospective quality assessment automation (M3.6 maturity scoring)
* Change-to-incident correlation engine (M2.5 CFR correlation)
* Problem Management workflow automation (M3.2, M3.7)

**Measurement Approach:**

* Track automation candidates through pipeline: Identified → Blueprint → Pilot → Production
* Success = At least 1 goes all the way from blueprint to validated production usage
* 3-5 at blueprint stage shows healthy pipeline for post-V2MOM execution

**Note:** Primary priority - focus here first before M1.2a internal patterns

---

## Method 2: Transform Change Management

### M2.1: Change Lead Time Reduction 

**Metric:** % reduction in mean time from RFC Creation to Implementation for Normal Changes

**Baseline:** 16 days (H2 2025 validated)

**Target:** -30% by Q2 2027 (11 days)

**Intermediate Milestones:**

* Q3 2026: 15 days (-6%)
* Q4 2026: 14 days (-12%)
* Q1 2027: 12 days (-25%)
* Q2 2027: 11 days (-30%)

**Owner:** <custom data-type="mention" data-id="id-5">@Laura Ferreira</custom> 

**Data Source:** Jira RFC project, customfield_18619 (Implementation Timestamp)

**Process Gaps:**

* **Implementation timestamp accuracy** - relies on manual field population by implementers
* **Outlier handling** - need protocol for extreme cases (max was 6114 hours in baseline)
* **Change scope variations** - lead time affected by change complexity, not just process efficiency

---

### M2.2: Standard Change Promotion Rate — REQUIRES IN-DEPTH REVIEW

**Metric:** % increase in volume of changes transitioned from Normal to Standard

**Target:** +50% increase by Q2 2027

**Owner:** <custom data-type="mention" data-id="id-6">@Laura Ferreira</custom> 

**Data Source:** Jira Change Catalog + Change Management project

**Process Gaps:**

* **Baseline data availability** - need H2 2024 Standard Change execution count
* **Change Catalog maturity** - requires complete Change Catalog Registry
* **Promotion criteria** - need clear framework for promoting Normal → Standard
* **Tracking mechanism** - need Jira field to track when/why changes promoted

**Status:** Laura Ferreira to review feasibility and baseline availability

---

### M2.3: Manual Resilience Identification

**Metric:** % of reviewed Normal RFCs flagged as "Automation Candidate"

**Target:** <20% by Q1 2027

**Expected Trend:**

* Q2 2026: 30-40% (baseline, learning period)
* Q3 2026: 25-35% (protocol stabilized)
* Q4 2026: 20-30% (early automations implemented)
* Q1 2027: <20% (sustained automation)

**Owner:** <custom data-type="mention" data-id="id-7">@Laura Ferreira</custom> 

**Data Source:** Jira RFC project (custom field required)

**Process Gaps:**

* **Custom field creation** - need "Reviewer Decision Reason" field added to Jira
* **Review protocol** - Laura must create rigorous criteria for identifying automation candidates
* **Reviewer training** - CAB reviewers need training on flagging criteria
* **False positive validation** - need quarterly validation mechanism (sample 20 RFCs)
* **Integration with automation pipeline** - need link between flagged RFCs and M5.3a (Process Automation Delivery)

---

### M2.4: CFR Correlation Accuracy ✓ FORMAL V2MOM METRIC

**Metric:** % of incidents where automated correlation correctly identifies asset-version change responsible

**Target:** >90% by Q4 2026

**Owner:** <custom data-type="mention" data-id="id-8">@Paulo Alves Monteiro</custom> 

**Data Source:** Correlation Engine + Jira RDINC (RCA findings)

**Process Gaps:**

* **Correlation engine doesn't exist yet** - Paulo must build (Submethod 2.5)
* **Correlation methodology undefined** - need timing windows, confidence scoring (Submethod 2.4)
* **Collection method TBD** - to be defined aligned with correlation mechanism implementation
* **Validation process TBD** - monthly spot-check approach to be defined
* **RCA quality variance** - not all RCAs have clear root cause identification
* **Multi-asset scenarios** - correlation complexity when multiple changes involved

---

## Method 3: Incident Response Resilience

### Submethod 3.1: Failure Management Governance

**Note:** No measurements currently linked to this submethod.

---

### Submethod 3.2: Status Page Governance & OLA Compliance

### M3.1: Public MTTA (Status Page) ✓ FORMAL V2MOM METRIC

**Metric:** Mean time from system-wide impact declaration to first external status page post

**Target:** <30 minutes by Q3 2026

**Expected Trend:**

* Q2 2026: 20-30 min (baseline with new process)
* Q3 2026: <30 min
* Q4 2026+: <20 min (optimization)

**Owner:** <custom data-type="mention" data-id="id-9">@Inês Matos</custom> 

**Data Source:** Rootly (declaration) + statuspage.io API (external post)

**Context:** Revised per GS workshop (March 2026) - IC Leader removed, GS can declare system-wide impact, GS Service Controllers curate incident updates and post to external status page

**Process Gaps:**

* **No Jira field to filter external posts** - can't distinguish system-wide incidents that were posted externally
* **Multi-system timestamp tracking** - declaration in Rootly, post in statuspage.io, incident in Jira RDINC
* **API integration needed** - statuspage.io API not currently integrated for timestamp extraction
* **Service Controller logging** - if API not available, need manual process for Service Controllers to log timestamps
* **Incident linkage** - need consistent incident ID across Rootly, RDINC, statuspage.io

---

### M3.2: Action Item Plan Closure Rate ✓ FORMAL V2MOM METRIC

**Metric:** % of High/Critical post-mortem action items closed within OLA/Deadline

**Target:** >80% by Q2 2027

**Owner:** <custom data-type="mention" data-id="id-10">@Inês Matos</custom> 

**Data Source:** Jira Problem Management project (action item tracking)

**Context:** Aligned per GS workshop (March 2026) - Problem Management as the ultimate mechanism for:

1. Action item lifecycle tracking post-incident resolution
2. Customer-facing progress reporting

**Process Gaps:**

* **Problem Management project doesn't exist yet** - need Jira project creation with workflow
* **Action item tracking mechanism** - how to link action items from RCA to Problem Management project?
* **OLA/Deadline definition** - need clear criteria for setting deadlines per action item priority/complexity
* **Ownership accountability** - who drives action item closure? (IC? VS Leader? PE? Engineering team?)
* **Progress visibility for customers** - how to share progress externally without exposing internal JIRA?

---

### M3.3: Triage Accuracy (Framework Validation) ✓ FORMAL V2MOM METRIC

**Metric:** % of tickets correctly categorized at intake (Service Incident vs Support Case)

**Target:** >80% by Q2 2027

**Owner:** <custom data-type="mention" data-id="id-11">@Inês Matos</custom> 

**Data Source:** Jira RDINC + SRE validation feedback

**Context:** Aligned per GS workshop (March 2026) - GS can declare service incidents, confirmed by SRE during initial troubleshooting. Metric stress tests framework accuracy to enable refinement, particularly for GS-declared incidents.

**Process Gaps:**

* **"Correct categorization" validation** - how to track SRE confirmation/disagreement? (Jira field? Status change? Comment analysis?)
* **Validation timing** - when does SRE confirm? (during troubleshooting? at resolution? retrospectively?)
* **GS empowerment without 24x7 engineering coverage** - no agreement yet on engineering coverage for high-urgent support cases, but GS empowered to declare incidents
* **Framework refinement trigger** - what accuracy threshold triggers framework review/update?
* **Edge cases** - ambiguous situations where both Service Incident and Support Case could apply

---

### M3.7: Problem Management Coverage ✓ FORMAL V2MOM METRIC

**Metric:** % of mandatory incidents with Problem records created

**Target:** >90% by Q4 2026

**Owner:** <custom data-type="mention" data-id="id-12">@Inês Matos</custom> 

**Data Source:** Jira RDINC + Problem Management project

**Context:** Aligned per GS workshop (March 2026) - Problem Management as mechanism for action item tracking and customer communication. Measures adoption of new Problem Management process.

**Process Gaps:**

* **Mandatory criteria undefined** - what triggers Problem creation? (all status page incidents? High/Critical? customer-impacting?)
* **Problem Management project doesn't exist** - need Jira project creation with workflow
* **Retrospective-to-Problem workflow** - no clear handoff process from RCA to Problem creation
* **Ownership model** - who creates Problem record? (Engineering team? PE? RCA owner? IC?)
* **Dual purpose complexity** - Problem serves both action tracking (internal) and customer-facing artifact (external)

**Status:** Inês Matos leading M3.4 initiative (Epic RSA-860). Governance model TBD in Q2 2026.

---

### M3.4: Alert Validation Accuracy (Event Management) ✓ FORMAL V2MOM METRIC

**Metric:** % of alerts correctly validated and filtered before triggering full incident response

**Target:** >85% by Q2 2027

**Owner:** Inês Matos

**Data Source:** Event Management validation log + incident outcome retrospective

**Context:** Establish formal Event Management practice to review alerts, validate if alert requires incident response, and filter false positives before full incident response is triggered.

**Phasing:** Practice definition Q2 2026 → Pilot & Baseline Q3 2026 → Scale Q4 2026 → Accuracy measurement Q1-Q2 2027

**Process Gaps:**

* **Event Management practice doesn't exist** - need practice definition in Q2 2026
* **Validation framework undefined** - criteria for alert validation, triage, escalation
* **RDINC integration complexity** - separate intake for alerts vs customer-reported incidents
* **Validation ownership unclear** - SRE on-call? Dedicated team? PE rotation?
* **Retrospective validation workload** - comparing validation decisions to actual outcomes requires manual review
* **Accuracy measurement timing** - when is "actual outcome" known? (incident resolution? RCA completion?)

**Status:** <custom data-type="mention" data-id="id-13">@Inês Matos</custom> leading initiative (Epic RSA-738). Practice definition Q2 2026, pilot Q3 2026.

---

### M3.4a: Event Management Coverage ✓ FOUNDATIONAL METRIC

**Metric:** % of alerts processed through formal Event Management practice

**Target:** 100% by Q4 2026

**Owner:** <custom data-type="mention" data-id="id-14">@Inês Matos</custom> 

**Data Source:** Alert source systems (PagerDuty, Grafana) + Event Management log

**Process Gaps:**

* **Alert source diversity** - system-wide alerts, service SLO alerts, custom alerts from Dev teams
* **Alert ingestion mechanism** - how do alerts flow into Event Management for validation?
* **Coverage tracking** - need denominator (all alerts fired) and numerator (alerts validated)
* **Alert source integration** - need data feeds from PagerDuty, Grafana, other monitoring tools

---

### M3.4b: Alert Volume & Classification Baseline ✓ FOUNDATIONAL METRIC

**Metric:** Monthly alert volume by source and outcome

**Target:** Baseline established Q3 2026, ongoing monitoring

**Owner:** <custom data-type="mention" data-id="id-15">@Inês Matos</custom> 

**Data Source:** Alert sources + Event Management log

**Process Gaps:**

* **Alert categorization schema** - need consistent taxonomy for alert types, sources, outcomes
* **Outcome classification** - categories: Triggered incident / False positive / Auto-resolved
* **Baseline data collection** - need pilot data from Q3 2026 to establish patterns

---

### M3.4c: False Positive Identification Rate ✓ FOUNDATIONAL METRIC

**Metric:** % of alerts identified as false positives by Event Management review

**Target:** Baseline Q3 2026, >70% identification rate by Q4 2026

**Owner:** <custom data-type="mention" data-id="id-16">@Inês Matos</custom> 

**Data Source:** Event Management validation log

**Process Gaps:**

* **False positive definition** - what qualifies as "false positive" vs "resolved before escalation"?
* **Identification criteria** - how to distinguish false positive during validation (vs retrospectively)?
* **Alert quality feedback loop** - need mechanism to report false positives back to alert owners
* **SRE/Dev team collaboration** - alert tuning requires Development team engagement

---

### M3.4d: Event Review Lead Time ✓ FOUNDATIONAL METRIC

**Metric:** Mean time from alert received to Event Management validation decision

**Target:** <15 minutes by Q4 2026

**Owner:** Inês Matos

**Data Source:** Alert timestamp + Event Management validation log

**Process Gaps:**

* **On-call validation availability** - 15 min target requires 24/7 coverage or fast response
* **Validation complexity** - some alerts may require investigation before decision
* **Delay tolerance** - balance speed vs accuracy (fast validation might miss nuances)

---

### M3.5: RCA Completion Rate & Lead Time ✓ FORMAL V2MOM METRIC

**Metric:** % of mandatory retrospectives completed within SLA + Average RCA lead time

**Target:** >90% completion rate and <14 days RCA lead time by Q2 2027

**Owner:** <custom data-type="mention" data-id="id-17">@Inês Matos</custom> 

**Data Source:** Jira RDINC + RCA project

**Context:**

* Retrospective Transformation - Team-led model
* Aligned per GS workshop (March 2026) - All status page incidents require RCA

**Process Gaps:**

* **RCA completion tracking** - need link between RDINC incident and RCA completion status
* **14-day SLA enforcement** - need automated alerts for approaching deadline
* **Team-led model dependency** - relies on engineering teams owning RCA, not PE driving
* **PE orchestration role** - PE facilitates but doesn't own (who tracks completion?)
* **Mandatory criteria enforcement** - all status page incidents require RCA (how to validate this?)

---

### M3.6: Incident Response Maturity Assessment ✓ FORMAL V2MOM METRIC

**Metric:** Average incident response maturity score across defined capability pillars

**Target:** >4.0/5.0 average maturity score by Q2 2027

**Owner:** <custom data-type="mention" data-id="id-18">@Inês Matos</custom> 

**Data Source:** Stoplight assessment (Green/Yellow/Red) of team performance

**Definition:** Assessment of team performance across incident response capability pillars (detection, troubleshooting, recovery, process compliance) based on what was/wasn't done during incident response. Pre-RCA assessment drives collaborative retrospective session focused on gaps.

**Purpose:**

1. Maturity assessment - evaluate team preparedness and incident response capability
2. RCA session focus - drive collaborative retrospective toward gaps (yellow/red pillars)
3. Coaching prioritization - identify which teams need support
4. Documentation quality - AI/Koda produces output, but quality measured by team maturity, not document quality

**Context:** Retrospective Transformation - Shift from output (what happened) to outcome (how well we responded and what to improve)

**Process Gaps:**

* **Assessment framework undefined** - need capability pillars defined with clear criteria (Green/Yellow/Red)
* **Who performs assessment?** - PE? Engineering team? IC? Collaborative?
* **Assessment timing** - during incident? immediately after? before RCA session?
* **Scoring consistency** - need calibration across teams/assessors (inter-rater reliability)
* **Baseline establishment** - what's current average maturity? (Q2 2026 baseline needed)
* **Coaching trigger** - what score triggers PE coaching/support? (Red pillars? Multiple yellow?)

---

## Method 4: Strategic Metrics Orchestration

### M4.1: Executive Metric Literacy ✓ FORMAL V2MOM METRIC

**Metric:** % of Leadership/End-Users who can correctly interpret calculation logic and navigate dashboards

**Target:** >85% by Q2 2026

**Owner:** <custom data-type="mention" data-id="id-19">@Paulo Alves Monteiro</custom> 

**Data Source:** Survey-based assessment (quarterly literacy assessments with ≥80% pass criteria)

**Process Gaps:**

* **Target audience definition** - who qualifies as "Leadership/End-Users"? (CPTO? Engineering leads? Product? All?)
* **Assessment mechanism** - post-training quiz? survey? interactive session?
* **Pass criteria clarity** - what does "≥80% pass" mean? (score on quiz? comprehensive understanding?)
* **Training delivery** - how/when is training provided? (onboarding? quarterly? on-demand?)
* **Literacy maintenance** - one-time or recurring assessment?

---

### M4.2: Documentation Lineage Coverage ✓ FORMAL V2MOM METRIC

**Metric:** % of CPTO metrics with full technical and functional lineage documentation

**Target:** 100% by Q3 2026

**Owner:** <custom data-type="mention" data-id="id-20">@Paulo Alves Monteiro</custom> 

**Data Source:** Metrics Library documentation repository

**Process Gaps:**

* **"Full lineage" definition** - what components required? (data sources, calculation logic, transformations, ownership?)
* **CPTO metrics inventory** - need complete list of metrics in scope
* **Documentation format/template** - where/how documented? (Confluence? Data catalog? Both?)
* **Maintenance process** - how to keep lineage updated when metrics change?
* **Quality validation** - who validates lineage documentation is complete/accurate?

---

### M4.3: Dashboard Adoption Rate — REQUIRES PAULO REVIEW

**Metric:** % of target audience actively using dashboards (monthly active users)

**Target:** >75% by Q4 2026

**Owner:** <custom data-type="mention" data-id="id-21">@Paulo Alves Monteiro</custom> 

**Data Source:** Dashboard analytics (Grafana, Power BI, Jira dashboards)

**Process Gaps:**

* **Dashboard analytics tracking** - do our dashboard platforms support usage tracking?
* **"Active usage" definition** - what qualifies? (monthly view? weekly? interaction vs passive viewing?)
* **Target audience identification** - who are the intended users per dashboard?
* **Dashboard infrastructure** - need dashboards built first before adoption can be measured

**Status:** Paulo Alves Monteiro to review feasibility and infrastructure requirements

---

### M4.4: Metric Data Quality Score — REQUIRES PAULO REVIEW

**Metric:** % of metrics passing monthly data quality validation checks

**Target:** >98% by Q4 2026

**Owner:** <custom data-type="mention" data-id="id-22">@Paulo Alves Monteiro</custom> 

**Data Source:** Data quality validation checks (automated + manual)

**Process Gaps:**

* **Data quality standards undefined** - what are the criteria? (completeness, accuracy, timeliness thresholds?)
* **PE role scope question** - is PE responsible for metric calculation or just governance framework?
* **Data ownership model** - who owns data quality for each metric? (metric owner? PE? data team?)
* **Validation automation** - need automated checks for data quality, not manual spot-checks
* **Quality scoring methodology** - how to aggregate quality across multiple metrics?
* **Acceptable refresh thresholds** - what's "timely" for each metric type?

**Status:** Paulo Alves Monteiro to review PE role and metric scope

---

### M4.5: 2027 Strategic Metrics Blueprint ✓ FORMAL V2MOM METRIC

**Metric:** Completion of strategic metrics blueprint for 2027

**Target:** Blueprint completed and signed off by Q4 2026

**Owner:** <custom data-type="mention" data-id="id-23">@Paulo Alves Monteiro</custom> 

**Data Source:** Blueprint document + stakeholder sign-off

**Purpose:** Prepare future measurement capability and ensure 2027 metrics are planned proactively rather than reactively

**Process Gaps:**

* **Stakeholder identification** - who signs off? (CPTO leadership? Specific personas?)
* **Blueprint format undefined** - Confluence doc? Presentation? Interactive prototype?
* **Trigger for 2027 planning** - what drives metric definition? (CPTO strategy? Business priorities? Regulatory?)
* **Detail level unclear** - high-level concepts vs implementation-ready specs?
* **Review/approval process** - sequential reviews? Workshop? Iterative refinement?

---

## Method 5: Team Performance & Development

### M5.1a: Operating Model Effectiveness

**Metric:** Team operating model operational with consistent execution

**Definition:** Composite assessment: weekly team meetings follow defined structure, individual V2MOMs tracked with visible progress, incoming work managed through defined backlog process.

**Target:** Operating model fully operational by end of Q2 2026, sustained throughout V2MOM period

**Owner:** <custom data-type="mention" data-id="id-24">@Vera Branco</custom> 

---

### M5.2a: Performance Alignment Coverage

**Metric:** % of team members with individual goals mapped to V2MOM and OutPerform criteria defined per rating level

**Definition:** Each team member has documented goals connected to specific V2MOM measurements with clear descriptions of what "Meets", "Exceeds", and "Outstanding" look like.

**Target:** 100% by end of Q2 2026 (reviewed quarterly)

**Owner:** <custom data-type="mention" data-id="id-25">@Vera Branco</custom>  

---

### M5.3a: Individual Development Plan Execution

**Metric:** % of team members with active Individual Development Plans executing quarterly milestones

**Definition:** Percentage of team members with IDPs who complete planned quarterly development activities

**Target:** 100% by end of Q2 2026 (quarterly tracking thereafter)

**Owner:** <custom data-type="mention" data-id="id-26">@Vera Branco</custom>  

---

### M5.3b: Team Engagement (eNPS)

**Metric:** Employee Net Promoter Score (eNPS) for Process Engineering team

**Definition:** Team engagement measured via Office Vibe eNPS or informal assessment mechanisms. Small team size (3 people) prevents direct eNPS visibility to manager, requiring indirect measurement or informal pulse checks.

**Target:** Positive eNPS score (>0) by Q2 2027, trending toward >20 (favorable)

**Owner:** <custom data-type="mention" data-id="id-27">@Vera Branco</custom>  

**Note:** Consider implementing informal assessment mechanisms (e.g., quarterly pulse checks, 1:1 engagement discussions) given small team size constraints with Office Vibe reporting

---

### M5.4a: Career Framework Completion

**Metric:** Completion of formal career framework for Business Process Analyst role family

**Definition:** Framework document completed, reviewed, and approved by People Team and CPTO

**Target:** Framework completed and approved by Q4 2026

**Owner:** <custom data-type="mention" data-id="id-28">@Vera Branco</custom>  

---

## Method 6: Operational Excellence & Sustainability

### M6.1: Operational Capacity Allocation

**Metric:** % of team capacity allocated to transformation work vs operational tasks

**Target:** Transformation 50-60%, Operational tasks 40-50% by Q2 2027 (quarterly tracking)

**Owner:** <custom data-type="mention" data-id="id-29">@Vera Branco</custom> 

**Data Source:** Jira story points by epic category

**Process Gaps:**

* **Time tracking discipline** - requires team to log time consistently (worklog, calendar, or time tracking tool)
* **Transformation vs operational classification** - clear criteria needed for categorizing work
* **Tracking mechanism** - Jira worklog? calendar review? dedicated time tracking tool?
* **Work type boundaries** - where does CAB prep fit? (operational) RFC review? (operational) automation design? (transformation)
* **Gaming risk** - team may over-allocate time to transformation for metric compliance

---

### M6.2: Process Orchestration Effectiveness (CAB & RCA)

**Metric:** Multiple metrics tracking governance and retrospective orchestration

**Components:**

* **M6.2a:** CAB Prep Time <4 hours per session
* **M6.2b:** First-Pass Approval Rate >85%
* **M6.2c:** RCA Orchestration Coverage >90%

**Target:** Q2 2027 (quarterly tracking)

**Owner:** <custom data-type="mention" data-id="id-30">@Vera Branco</custom>  (executed in rotation across team)

**Context:** Covers both CAB orchestration (Submethod 6.1) and Retrospective Transformation facilitation (team-led RCA model with PE orchestration support)

**Data Sources:**

* M6.2a: Time tracking (manual or Jira worklog)
* M6.2b: Jira RFC project (status transitions)
* M6.2c: RCA facilitation log + RDINC project

**Process Gaps:**

**M6.2a - CAB Prep Time:**

* **Time tracking method** - manual self-reporting? Jira worklog? calendar blocking?
* **"Prep" scope definition** - RFC pre-review? agenda creation? material prep? all of above?
* **Who tracks?** - person doing prep? automated from Jira logs?

**M6.2b - First-Pass Approval Rate:**

* **"First-pass approval" definition** - approved without questions? approved without rework? how to code in Jira?
* **Distinguishing "minor questions" vs "needs rework"** - gray area in approval decisions
* **Jira field tracking** - which field captures this? (custom field needed? status transitions? comment analysis?)

**M6.2c - RCA Orchestration Coverage:**

* **"PE orchestration/facilitation" definition** - PE facilitates meeting? prepares materials? reviews output? combination?
* **"Mandatory retrospective" criteria** - all status page incidents? High/Critical only? what triggers requirement?
* **PE participation tracking** - meeting attendance? Jira field? calendar tracking? honor system?
* **Reporting mechanism** - who reports orchestration? (PE facilitator? automated from meeting invites?)
* **Rotation model** - how is RCA facilitation rotated? (round-robin? by expertise? voluntary?)

**Integration:** M6.2c aligns with M3.5 (RCA Completion Rate) and M3.6 (Incident Response Maturity Assessment)

---

### M6.3: Audit Request Fulfillment Rate

**Metric:** % of audit evidence and compliance requests fulfilled within agreed deadline

**Target:** >95% by Q2 2027

**Owner:** <custom data-type="mention" data-id="id-31">@Vera Branco</custom> 

**Data Source:** Audit request tracking (Confluence + email + Jira)

**Process Gaps:**

* **Audit request tracking mechanism** - centralized tracker? Jira tickets? email follow-up? spreadsheet?
* **"Agreed deadline" definition** - negotiated per request? standard SLA? audit timeline-driven?
* **Request volume forecasting** - how to plan capacity for audit season?
* **Evidence repository** - where is evidence stored? (Confluence? SharePoint? GRC tool?)
* **Multi-audit coordination** - SOC2, FedRAMP, ISO overlap creates competing deadlines

---

### M6.4: Dashboard Operational Availability

**Metric:** % of V2MOM dashboards operational and accurate

**Target:** >98% by Q2 2027

**Owner:** <custom data-type="mention" data-id="id-32">@Paulo Alves Monteiro</custom> 

**Data Source:** Dashboard health checks (automated monitoring + manual validation)

**Process Gaps:**

* **"Operational and accurate" definition** - what qualifies? (accessible + data correct + visualizations render?)
* **Dashboard inventory** - need complete list of V2MOM dashboards in scope
* **Health check automation** - automated monitoring for uptime, data freshness, accuracy?
* **Issue detection** - how to detect dashboard issues before users report?
* **Recovery time target** - how fast should broken dashboards be fixed? (SLA?)

---

## Summary Statistics

**Total Measurements:** 34

**By Status:**

* Formal V2MOM Metrics: 29
* Foundational Metrics: 4 (M3.4a, M3.4b, M3.4c, M3.4d)
* Requires Paulo Review: 2 (M4.3, M4.4)
* Requires Review: 1 (M2.2)

**By Method:**

* Method 1 (AI Transformation): 4 measurements (4 formal: M1.1a, M1.2a, M1.2b, M1.3a)
* Method 2 (Change Management): 5 measurements (3 formal)
* Method 3 (Incident Response): 11 measurements (7 formal + 4 foundational)
* Method 4 (Metrics Orchestration): 5 measurements (3 formal, 2 requires Paulo review)
* Method 5 (Team Performance & Development): 5 measurements (5 formal: M5.1a, M5.2a, M5.3a, M5.3b, M5.4a)
* Method 6 (Operational Excellence): 4 measurements (4 formal)

**Target Dates Distribution:**

* Q3 2026: 2 measurements
* Q4 2026: 4 measurements
* Q1 2027: 1 measurement
* Q2 2027: 23 measurements (V2MOM end)
* Quarterly tracking: 2 measurements

---

## Next Steps

1. **Review & Approve Targets:** Validate all targets and timeframes
2. **Resolve Open Items:**

    * M2.2: Complete in-depth review
    * M3.4: Pilot validation mechanism
    
3. **Implementation Planning:** Sync approved changes to detailed implementation document (v2mom_measurements_refined.md)
4. **Baseline Establishment:** Q2 2026 baseline collection for measurements without validated baselines

---