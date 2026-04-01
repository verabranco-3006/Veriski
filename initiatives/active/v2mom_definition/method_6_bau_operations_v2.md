# Method 6: Operational Excellence & Sustainability

**Purpose:** Ensure consistent delivery of ongoing Process Engineering operations while maintaining capacity for transformation work

**Scope:** Core operational activities that sustain process governance, compliance, and day-to-day engineering support

---

## Rationale

Process Engineering's transformation agenda (Methods 1-5) requires dedicated capacity, but the team must simultaneously maintain critical BAU operations that keep the organization running. This method explicitly acknowledges BAU capacity consumption and establishes measurements to ensure operational excellence doesn't erode during transformation phases.

---

## Submethods

### Submethod 6.1: Process Governance & CAB Orchestration

**Objective:** Maintain effective change governance through monthly CAB operations and process reviews

**Activities:**
- Monthly CAB facilitation and RFC review
- CAB prep work (agenda creation, RFC pre-review, material preparation)
- CAB decision documentation and communication
- Monthly governance reviews (Change, Incident, Problem Management)
- Process adherence monitoring and exception handling
- Governance reporting for leadership

**Success Criteria:**
- Monthly CAB operates efficiently (low prep time, short meetings, high first-pass approval)
- Monthly governance reviews completed on schedule
- Process adherence issues identified and addressed proactively

**Owner:** Laura Ferreira (CAB facilitation)

---

### Submethod 6.2: Operational Support & Consultation

**Objective:** Provide responsive process guidance and support to Engineering teams

**Activities:**
- Ad-hoc consultation requests (process interpretation, escalation guidance)
- Policy interpretation and clarification
- Escalation support for complex cases
- Cross-team coordination for process-related issues
- Tool usage guidance (Jira workflows, Confluence templates)

**Success Criteria:**
- Fast response times to consultation requests
- Engineering teams unblocked quickly
- Self-service resources reduce consultation volume over time

**Owner:** Process Engineering team (rotational coverage)

---

### Submethod 6.3: Audit & Compliance Sustainment

**Objective:** Ensure timely delivery of audit evidence and ongoing compliance monitoring

**Activities:**
- Audit evidence collection and packaging (SOC2, FedRAMP, ISO, internal audits)
- Control validation and testing
- Audit interview preparation and participation
- Compliance monitoring (regulatory requirements, policy adherence)
- Remediation tracking for audit findings

**Success Criteria:**
- All audit requests fulfilled on-time
- Zero audit findings related to process evidence gaps
- Compliance posture maintained between audit cycles

**Owner:** Process Engineering team (assigned per audit cycle)

---

### Submethod 6.4: Documentation & Knowledge Management

**Objective:** Maintain accurate, current process documentation to enable self-service and reduce consultation burden

**Activities:**
- Process framework documentation maintenance (Change, Incident, Problem, Failure Management)
- Runbook and operational guide updates
- Standards and policy documentation
- Tool usage guides (Jira, Confluence workflows)
- Documentation reviews (quarterly or triggered by process changes)
- Knowledge base organization and searchability improvements

**Success Criteria:**
- Critical documentation reviewed and updated within 6 months
- Documentation accuracy validated through user feedback
- Self-service adoption increases, consultation volume decreases

**Owner:** Process Engineering team (shared ownership with rotation)

---

### Submethod 6.5: Measurement Infrastructure Operations

**Objective:** Sustain V2MOM measurement infrastructure built in Method 4

**Activities:**
- Dashboard maintenance and troubleshooting (M1-M5 dashboards)
- Data quality monitoring for V2MOM metrics
- Ad-hoc reporting requests from leadership
- Metrics definition support for other teams
- Data pipeline monitoring (Jira queries, API integrations)
- Measurement documentation updates

**Success Criteria:**
- Dashboards remain operational and accurate
- Data quality issues identified and resolved proactively
- Leadership reporting requests fulfilled within agreed timelines

**Owner:** Paulo Alves Monteiro (metrics infrastructure)

---

### Submethod 6.6: Continuous Improvement Backlog

**Objective:** Triage and address process improvement opportunities not covered by transformation initiatives (M1-M5)

**Activities:**
- Process improvement request triage (assess scope, prioritize)
- Quick fixes and minor enhancements (low-effort, high-impact)
- Technical debt management (Jira cleanup, template updates, automation fixes)
- Tool administration (permissions, project setup, workflow maintenance)
- Process exception handling and resolution

**Success Criteria:**
- Improvement backlog remains manageable (not growing faster than throughput)
- High-impact quick wins delivered regularly
- Technical debt doesn't accumulate to critical levels

**Owner:** Vera Branco (backlog prioritization)

---

## Measurements

### M6.1: BAU Capacity Allocation (Overall Method 6)

**Metric:** % of story points completed on BAU operations (M6) vs transformation work (M1-M5)

**Definition:** Track story points delivered on BAU activities vs transformation initiatives using existing Jira epic structure

**Target:**
- BAU (M6): 40-50% of total story points
- Transformation (M1-M5): 50-60% of total story points

**Rationale:**
- If BAU > 50%: Transformation stalls, V2MOM at risk
- If BAU < 40%: Operational quality degrades, governance gaps emerge
- Sweet spot: 40-50% BAU allows both operational excellence and transformation progress
- Story points = relative effort, good proxy for capacity without manual time tracking overhead

**Measurement Logic:**
- Each submethod already has dedicated Jira epics
- Team estimates and tracks story points as normal
- Aggregate completed story points by epic/method quarterly
- Calculate: `(M6 Story Points / Total Story Points) × 100`

**Breakdown by Submethod (Target Allocation):**
- 6.1 Process Governance & CAB: 8-10% (monthly CAB + governance reviews)
- 6.2 Operational Support & Consultation: 8-10%
- 6.3 Audit & Compliance: 10-15% (variable by audit season)
- 6.4 Documentation & Knowledge: 5-8%
- 6.5 Measurement Infrastructure Ops: 3-5%
- 6.6 Continuous Improvement Backlog: 4-6%

**Implementation:**
- **Data Source:** Jira story points by epic
- **Collection Method:**
  - Query completed issues per quarter grouped by epic/method
  - JQL examples:
    ```jql
    # M6 BAU story points
    project = PE AND "Epic Link" IN (M6.1_epic, M6.2_epic, M6.3_epic, M6.4_epic, M6.5_epic, M6.6_epic)
    AND resolved >= startOfQuarter() AND resolved <= endOfQuarter()

    # M1-M5 Transformation story points
    project = PE AND "Epic Link" IN (M1_epics, M2_epics, M3_epics, M4_epics, M5_epics)
    AND resolved >= startOfQuarter() AND resolved <= endOfQuarter()
    ```
  - Export to spreadsheet or Power BI for calculation
  - Supplemental: Quarterly capacity retrospective (5 min/person) to validate story points reflect reality
- **Frequency:** Quarterly reporting (no ongoing manual tracking needed)
- **Owner:** Vera Branco (team capacity management)
- **Dashboard:** Capacity Allocation Dashboard
  - Primary: BAU % vs Transformation % by quarter (target band: 40-50% BAU)
  - Breakdown: Story points by submethod (6.1-6.6) and method (M1-M5)
  - Trend: Quarter-over-quarter capacity shift
  - Jira gadget: "Story Points by Epic" stacked bar chart

**Baseline:** To be established Q1 2026 (analyze Q4 2025 story points by epic)

**Expected Trend:**
- Q1 2026: 55-60% BAU (high due to audit season, FedRAMP prep baseline work)
- Q2 2026: 45-50% BAU (transformation ramp-up, audits complete)
- Q3-Q4 2026: 40-45% BAU (sustainable operating rhythm achieved)

**Calibration:**
- Quarterly team retrospective question: "Do story points by epic accurately reflect our capacity allocation, or is significant work happening outside Jira?"
- If significant untracked work exists (e.g., Slack consultations, ad-hoc support), supplement with quarterly capacity estimate

**Limitations & Mitigations:**
- **Limitation:** Story points don't capture all work (ad-hoc consultations, urgent support, meetings)
- **Mitigation:** If untracked work is significant, add quarterly retrospective capacity check
- **Limitation:** Story points = relative effort, not exact time
- **Mitigation:** Acceptable trade-off for zero ongoing tracking overhead; story points are good enough for V2MOM capacity planning

**SMART Assessment:** ✓ SMART - Clear metric (%), measurable via existing Jira data, target band defined, achievable without additional overhead, relevant to capacity planning

---

### M6.2: CAB Orchestration Effectiveness (Submethod 6.1)

**Metric:** CAB operational efficiency measured by preparation time, meeting duration, and decision quality

**Definition:** Track CAB effectiveness to ensure governance doesn't become capacity bottleneck

**Target:**
- Average CAB prep time < 2 hours per meeting (Q4 2026)
- Average CAB duration ≤ 30 minutes (Q4 2026)
- RFC first-pass approval rate > 85% (Q4 2026)

**Rationale:**
- CAB is weekly recurring capacity sink (10-12% of team capacity)
- Inefficient CAB preparation/execution consumes excessive capacity
- High first-pass approval indicates good pre-meeting RFC quality
- Shorter meetings with maintained quality = efficient governance

**Measurement Logic:**

**M6.2a: CAB Prep Time**
- Track: Time spent preparing for weekly CAB (RFC pre-review, agenda creation, material prep)
- Target: < 2 hours per CAB session
- Measurement: Manual time logging or Jira worklog

**M6.2b: CAB Duration**
- Track: Actual meeting duration (start to end)
- Target: ≤ 30 minutes per CAB session
- Measurement: Calendar time or meeting recording timestamps

**M6.2c: First-Pass Approval Rate**
- Track: % of RFCs approved on first CAB review (no rework/re-submission needed)
- Target: > 85%
- Numerator: RFCs approved at CAB without rework requests
- Denominator: Total RFCs reviewed at CAB
- Calculation: `(RFCs Approved First Review / Total RFCs Reviewed) × 100`

**Implementation:**
- **Data Source:** CAB meeting logs + Jira RFC project
- **Collection Method:**
  - CAB facilitator logs prep time and meeting duration weekly (Confluence CAB log or Jira)
  - Jira: Track RFCs by review outcome (Approved First Time, Needs Rework, Rejected)
  - Quarterly aggregate and trend analysis
- **Frequency:** Weekly tracking, quarterly reporting
- **Owner:** Laura Ferreira (CAB facilitator)
- **Dashboard:** CAB Efficiency Dashboard
  - Prep time trend by week/quarter (target line at 2 hours)
  - Meeting duration trend (target line at 30 min)
  - First-pass approval rate trend (target line at 85%)
  - Capacity impact: Total weekly CAB hours (prep + meeting) trend

**Baseline:** To be established Q1 2026 from historical CAB data (if available)

**Integration with Other Metrics:**
- **M2.3 (RFC Rejection Velocity):** Faster pre-CAB rejection improves first-pass approval rate
- **M2.4 (Manual Resilience):** Automating repetitive changes reduces CAB RFC volume
- **M2.1 (Change Lead Time):** Efficient CAB reduces RFC processing time

**SMART Assessment:** ✓ SMART - Multiple clear metrics (time, %), measurable, targets defined, relevant to capacity optimization

---

### M6.3: Consultation Request Response Time (Submethod 6.2)

**Metric:** Mean time to provide initial response to ad-hoc consultation requests from Engineering teams

**Definition:** Track responsiveness to process guidance requests to ensure teams aren't blocked

**Target:** < 24 hours initial response time by Q4 2026

**Rationale:**
- Engineering teams depend on Process Engineering for guidance
- Delayed responses create blockers and reduce team autonomy
- Fast initial response (even if full resolution takes longer) reduces friction
- Measures "service level" of Process Engineering team to internal customers

**Measurement Logic:**
- **Start:** Request received (Slack message, Jira ticket, email, meeting request)
- **End:** Initial response provided (acknowledgment + ETA or direct answer)
- **Calculation:** `(Response Timestamp - Request Timestamp)` in hours
- **Aggregate:** Mean response time per quarter

**Scope:**
- **Include:** Process guidance, escalation support, policy interpretation, tooling questions, ad-hoc consultations
- **Exclude:** Formal project requests (those route to M1-M5 work), scheduled meetings

**Implementation:**
- **Data Source:** Consultation tracking (Jira "PE Consultation" project or Slack-based tracking)
- **Collection Method:**
  - Option A: Create "PE Consultation" Jira project
    - Issue type: Consultation Request
    - Fields: Request Date, Response Date, Category (Process/Tool/Audit/Policy/Other), Requester, Outcome
    - Calculate response time per request, aggregate quarterly
  - Option B: Manual tracking in Confluence table (lighter weight)
    - Weekly: Team logs consultation requests and response times
- **Frequency:** Monthly tracking, quarterly reporting
- **Owner:** Vera Branco (team responsiveness)
- **Dashboard:** Consultation Response Tracker
  - Primary: Response time trend by month/quarter (target line at 24 hours)
  - Breakdown by category: Which types of requests take longest? (Process, Tool, Audit, etc.)
  - Volume trend: Requests per quarter (capacity planning signal)
  - Self-service indicator: % of requests resolved via documentation link vs direct consultation

**Baseline:** To be established Q1 2026 (pilot tracking for 1 month to validate approach)

**Expected Trend:**
- Q1 2026: 36-48 hours (baseline, no formal SLA in place)
- Q2 2026: 24-36 hours (team awareness + prioritization practices)
- Q3-Q4 2026: < 24 hours (TARGET - responsive service achieved)

**Supporting Metrics:**
- **Consultation volume:** Total requests per quarter (capacity planning input)
- **Self-service rate:** % of requests resolved via documentation vs direct consultation (measures documentation effectiveness from 6.4)
- **Repeat requester rate:** % of requests from same teams/people (indicates training or documentation gaps)

**SMART Assessment:** ✓ SMART - Clear metric (hours), measurable, target defined, achievable, relevant to service quality

---

### M6.4: Audit Request Fulfillment Rate (Submethod 6.3)

**Metric:** % of audit evidence and compliance requests fulfilled within agreed deadline

**Definition:** Track on-time delivery of audit-related requests to ensure compliance obligations are met

**Target:** > 95% on-time fulfillment by Q4 2026

**Rationale:**
- Audit season creates unpredictable BAU load spikes (10-15% capacity)
- Late audit responses create organizational compliance risk
- Explicit tracking ensures audit support doesn't derail transformation work
- Enables capacity planning for future audit cycles

**Measurement Logic:**
- **Numerator:** Audit requests delivered by agreed deadline
- **Denominator:** Total audit requests received
- **Calculation:** `(On-Time Deliveries / Total Requests) × 100`

**Scope:**
- **Audit types:** SOC2, FedRAMP, ISO, internal audits
- **Request types:** Evidence collection, control validation, process documentation, audit interviews, remediation evidence
- **Deadline:** Agreed SLA with auditor or internal stakeholder (document per request in tracker)

**Implementation:**
- **Data Source:** Audit Request Tracker (Jira or Confluence)
- **Collection Method:**
  - Create "Audit Request" issue type in Jira OR Confluence tracking table
  - Track per request: Request Date, Audit Type (SOC2/FedRAMP/ISO/Internal), Requester, Deadline, Completion Date, Owner, Status
  - Flag: On-Time (Yes/No) calculated automatically
  - Quarterly aggregate: On-time rate, average lead time, capacity consumption
- **Frequency:** Monthly tracking (during audit seasons), quarterly reporting
- **Owner:** Process Engineering team (rotational or assigned per audit)
- **Dashboard:** Audit Fulfillment Tracker
  - Primary: On-time rate trend by quarter (target line at 95%)
  - Average lead time: Request to delivery in days
  - Volume by audit type: SOC2, FedRAMP, ISO, Internal
  - Capacity impact: Hours spent on audit support per quarter
  - Upcoming requests: Early warning for capacity planning

**Baseline:** To be established Q1 2026 from Q4 2025 audit request history (if tracked)

**Integration with Other Methods:**
- **M1 (FedRAMP):** FedRAMP audit support becomes BAU post-authorization (Q3 2026+)
- **M2-M5:** Audit requests for transformation initiatives tracked here

**SMART Assessment:** ✓ SMART - Clear metric (%), measurable, target defined, relevant to compliance obligations

---

### M6.5: Process Documentation Currency (Submethod 6.4)

**Metric:** % of critical process documentation reviewed and updated within the last 6 months

**Definition:** Track documentation freshness to ensure operational guides remain accurate and trustworthy

**Target:** > 80% of critical docs current (reviewed/updated in last 6 months) by Q4 2026

**Rationale:**
- Outdated documentation creates operational risk and training inefficiency
- Documentation maintenance is BAU work often deprioritized under transformation pressure
- Explicit measurement ensures docs don't decay during Methods 1-5 focus
- Fresh documentation supports self-service and reduces consultation volume (M6.3)

**Measurement Logic:**
- **Critical Documentation Scope:**
  - Process frameworks (Change, Incident, Problem, Failure Management)
  - Runbooks and operational guides
  - Standards and policies
  - Compliance control documentation
  - Tool usage guides (Jira workflows, Confluence templates)
  - Training materials
- **Currency Criteria:** Last modified date within 6 months OR explicit review stamp/approval
- **Calculation:** `(Docs Current / Total Critical Docs) × 100`

**Implementation:**
- **Data Source:** Documentation registry (Confluence page list or dedicated tracker)
- **Collection Method:**
  - Maintain "Critical Documentation Registry" in Confluence
    - Columns: Doc Title, Type (Framework/Runbook/Standard/Compliance/Tool Guide), Owner, Last Review Date, Next Review Due, Status (Current/Stale)
  - Quarterly audit: Check Last Modified dates in Confluence OR review stamps
  - Calculate currency rate
  - Flag stale docs for prioritized review
- **Frequency:** Quarterly measurement
- **Owner:** Process Engineering team (shared ownership with rotation, coordinated by Vera)
- **Dashboard:** Documentation Health Tracker
  - Primary: Currency rate trend by quarter (target line at 80%)
  - Breakdown: Which doc types are stale? (Frameworks, Runbooks, Standards, etc.)
  - Upcoming reviews: Docs due for review in next quarter (planning view)
  - Review velocity: Docs reviewed per quarter (capacity indicator)

**Baseline:** To be established Q1 2026 (audit current documentation state, create registry)

**Review Cadence Recommendations:**
- **High-change areas:** Quarterly review (e.g., Change Management during M2 transformation)
- **Stable areas:** Semi-annual review (e.g., established Incident Response frameworks)
- **Compliance docs:** Review before each audit cycle (triggered reviews)
- **Post-transformation:** Review docs after Methods 1-5 initiatives complete (e.g., M3 retrospective docs after transformation)

**SMART Assessment:** ✓ SMART - Clear metric (%), measurable via Confluence metadata, target defined, achievable, relevant to operational quality

---

### M6.6: Dashboard Operational Availability (Submethod 6.5)

**Metric:** % of V2MOM dashboards operational and accurate (data quality validated)

**Definition:** Track availability and accuracy of measurement infrastructure built in Method 4

**Target:** > 98% dashboard availability (operational with accurate data) by Q4 2026

**Rationale:**
- Method 4 builds measurement infrastructure; Method 6.5 sustains it
- Dashboard downtime or data quality issues undermine V2MOM tracking
- Proactive monitoring prevents measurement blind spots
- Measures operational reliability of metrics infrastructure

**Measurement Logic:**
- **Dashboard Inventory:** List of all V2MOM dashboards (M1-M5 metrics)
  - Example: Change Lead Time Dashboard (M2.1), Public MTTA Dashboard (M3.1), CAB Efficiency Dashboard (M6.2), etc.
- **Availability Criteria:**
  - Dashboard accessible (no errors, loads within 10 seconds)
  - Data accurate (matches source systems, no stale data)
  - Visualizations render correctly
- **Weekly Check:** Automated or manual verification of each dashboard
- **Calculation:** `(Dashboards Operational / Total Dashboards) × 100`

**Scope:**
- **Include:** All V2MOM Method 1-6 dashboards
- **Exclude:** Experimental or draft dashboards not yet in production

**Implementation:**
- **Data Source:** Dashboard monitoring log (Confluence or Jira)
- **Collection Method:**
  - Maintain dashboard inventory (list of all dashboards with URLs, owners, data sources)
  - Weekly monitoring: Automated checks (if tooling available) OR manual spot-checks
  - Log issues: Dashboard name, issue type (unavailable/data quality/visualization), detected date, resolved date
  - Calculate availability rate per month/quarter
- **Frequency:** Weekly monitoring, monthly reporting, quarterly aggregate
- **Owner:** Paulo Alves Monteiro (metrics infrastructure)
- **Dashboard:** Dashboard Health Tracker (meta-dashboard)
  - Primary: Availability rate trend by month/quarter (target line at 98%)
  - Issue log: Current open issues, time to resolution
  - Breakdown: Issues by type (availability, data quality, visualization)
  - Most impacted dashboards: Which dashboards have frequent issues?

**Baseline:** To be established Q2 2026 (after Method 4 dashboards deployed)

**Integration with Method 4:**
- M4 creates dashboards (project work)
- M6.6 sustains dashboards (BAU operations)

**SMART Assessment:** ✓ SMART - Clear metric (%), measurable, target defined, relevant to measurement infrastructure reliability

---

## Capacity Planning Model

### Quarterly Capacity Allocation Targets

Based on M6.1 tracking, target capacity allocation for Process Engineering team:

| Category | Target % | Q1 2026 (Est) | Q2 2026 (Goal) | Q3-Q4 2026 (Goal) |
|----------|----------|---------------|----------------|-------------------|
| **BAU Operations (M6)** | **40-50%** | **55%** | **48%** | **42%** |
| 6.1 CAB & Governance | 10-12% | 15% | 12% | 10% |
| 6.2 Consultation & Support | 8-10% | 12% | 10% | 8% |
| 6.3 Audit & Compliance | 10-15% | 18% | 15% | 12% |
| 6.4 Documentation | 5-8% | 6% | 7% | 8% |
| 6.5 Measurement Ops | 3-5% | 2% | 3% | 3% |
| 6.6 Improvement Backlog | 4-6% | 2% | 1% | 1% |
| **Transformation (M1-M5)** | **50-60%** | **45%** | **52%** | **58%** |

**Key Insights:**
- **Q1 2026:** Audit-heavy season (SOC2, FedRAMP prep) drives 55% BAU load
  - Audit & Compliance (6.3): 18% capacity
  - CAB temporarily overloaded due to audit-related changes: 15%
  - Transformation work constrained to 45%

- **Q2 2026:** Transition to balanced load as audits complete
  - Audit drops to 15% (post-audit monitoring)
  - CAB returns to normal: 12%
  - Transformation ramps up to 52%

- **Q3-Q4 2026:** Target sustainable rhythm achieved
  - BAU: 42% (efficient operations)
  - Transformation: 58% (full capacity for M1-M5 delivery)

---

## BAU Optimization Strategies

To achieve and maintain 40-50% BAU target:

### 1. CAB Efficiency Improvements (Submethod 6.1 → M6.2)
- **Strategy:** Reduce prep time via standardized templates, pre-screening automation
- **Impact:** Target 10% capacity (down from 15% in Q1)
- **Enablers:**
  - M2.3 (RFC Rejection Velocity): Fast pre-CAB rejection reduces CAB load
  - M2.4 (Manual Resilience): Automation candidates identified, reducing RFC volume
  - Standardized CAB prep checklist and templates

### 2. Self-Service Documentation (Submethod 6.4 → M6.5 → M6.3)
- **Strategy:** Improve documentation quality and discoverability to reduce consultation volume
- **Impact:** Target 8% capacity for consultation (down from 12% in Q1)
- **Enablers:**
  - M6.5: Keep docs current and trustworthy
  - M4.1 (Executive Metric Literacy): Training reduces ad-hoc metric interpretation requests
  - Search optimization and documentation portal improvements

### 3. Process as Code (M5 → M6)
- **Strategy:** Automate repetitive governance tasks (e.g., RFC validation, evidence collection)
- **Impact:** Reduce capacity across multiple submethods (6.1, 6.3, 6.6)
- **Enablers:**
  - M5.1-M5.3: Skills deployed for process execution automation
  - M2.4: Automation candidates feed M5 backlog

### 4. Training Scale (M4 → M6.2)
- **Strategy:** Scalable training reduces one-off consultation volume
- **Impact:** Fewer ad-hoc requests as teams become self-sufficient
- **Enablers:**
  - M4.1: Training programs for process literacy
  - Brown Bag sessions and recorded training materials

### 5. Audit Preparation Front-loading (Submethod 6.3)
- **Strategy:** Continuous evidence collection reduces peak-season crunch
- **Impact:** Smoother capacity consumption (avoid 18% spikes)
- **Enablers:**
  - Automated evidence collection pipelines (M5)
  - Quarterly compliance reviews vs annual audit crunch
  - Evidence repository maintained year-round

---

## Integration with Other Methods

### M6 ↔ M1 (FedRAMP Enablement)
- **M1 is project work** (transformation capacity) during Q1-Q2 2026
- **M6.3 (Audit Fulfillment)** tracks FedRAMP audit support as BAU post-authorization (Q3 2026+)

### M6 ↔ M2 (Change Management Transformation)
- **M2.1 (Lead Time Reduction)** reduces RFC review burden on CAB → improves M6.2
- **M2.3 (Rejection Velocity)** reduces CAB load → improves M6.2
- **M2.4 (Manual Resilience)** identifies automation candidates → reduces M6.1 capacity
- **M6.2 (CAB Effectiveness)** measures operational impact of M2 improvements

### M6 ↔ M3 (Incident Response Transformation)
- **M3 transformation work** (retrospectives, RCA quality) is capacity in M1-M5
- **M6 BAU** covers ongoing incident process governance, triage support, ad-hoc escalation support

### M6 ↔ M4 (Metrics Orchestration)
- **M4 creates metrics infrastructure** (dashboards, lineage docs) as project work (M1-M5 capacity)
- **M6.5 (Measurement Ops)** sustains infrastructure (dashboard maintenance, data quality) as BAU
- **M4.1 (Training)** reduces ad-hoc metric interpretation requests → improves M6.3

### M6 ↔ M5 (Process as Code)
- **M5 builds automation** (skills, blueprints, extension packages) as project work (M1-M5 capacity)
- **M6 BAU** covers ongoing tool administration, support for deployed skills
- **M5 success** should reduce M6 BAU load over time (automation reduces manual toil) → measurable via M6.1 trends

---

## Summary: Method 6 Measurements

| Metric | Submethod | Target | Owner | Baseline | Status |
|--------|-----------|--------|-------|----------|--------|
| M6.1: BAU Capacity Allocation | Overall M6 | 40-50% BAU story points | Vera | Q1 2026 | Track quarterly |
| M6.2: CAB Effectiveness | 6.1 | <2h prep, ≤30min, >85% approval | Laura | Q1 2026 | Track weekly |
| M6.3: Consultation Response | 6.2 | <24 hours | Vera | Q1 2026 | Track monthly |
| M6.4: Audit Fulfillment | 6.3 | >95% on-time | Team | Q1 2026 | Track monthly |
| M6.5: Documentation Currency | 6.4 | >80% current (6mo) | Team | Q1 2026 | Track quarterly |
| M6.6: Dashboard Availability | 6.5 | >98% operational | Paulo | Q2 2026 | Track weekly |

---

## Implementation Roadmap

### Q1 2026: Baseline & Foundation
- **Week 1-2:** Define submethods in detail, create tracking mechanisms
  - Create Jira "PE Consultation" project (M6.3)
  - Create "Audit Request Tracker" (M6.4)
  - Create "Critical Documentation Registry" (M6.5)
- **Week 3-4:** Establish baselines
  - M6.1: Retroactive analysis of Q4 2025 story points by epic (Jira query)
  - M6.2: Historical CAB data analysis (prep time, duration, approval rates) from monthly CABs
  - M6.3: Pilot consultation tracking for 1 month
  - M6.4: Audit request history from Q4 2025 (if available)
  - M6.5: Audit current documentation state, create registry
- **Ongoing:** Monthly CAB logging starts (M6.2), consultation tracking starts (M6.3)

### Q2 2026: Measurement Refinement
- **Validate baselines:** Confirm Q1 measurements are accurate and sustainable
- **Dashboard deployment:** Create M6 dashboards (Capacity Allocation, CAB Efficiency, Consultation Response, etc.)
- **M6.6 baseline:** Establish dashboard availability tracking post-M4 dashboard deployment
- **Capacity reviews:** Monthly capacity allocation reviews, adjust if BAU > 50%

### Q3-Q4 2026: Optimization & Target Achievement
- **Achieve targets:** Drive toward 40-50% BAU load, optimize submethods
- **Integration validation:** Confirm M2/M5 automation reduces M6.1 BAU load
- **Self-service improvements:** Documentation enhancements (6.4) reduce consultation volume (6.3)
- **Quarterly reviews:** Assess whether sustainable operating rhythm achieved

---

**Last Updated:** 2026-04-01
