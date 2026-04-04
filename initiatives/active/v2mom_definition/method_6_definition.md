# Method 6: Operational Excellence & Sustainability

**Purpose:** Ensure consistent delivery of ongoing Process Engineering operational tasks while maintaining capacity for transformation work

**Scope:** Core operational activities that sustain process governance, compliance, and day-to-day engineering support

---

## Rationale

Process Engineering's transformation agenda (Methods 1-5) requires dedicated capacity, but the team must simultaneously maintain critical operational tasks that keep the organization running. This method explicitly acknowledges operational capacity consumption and establishes measurements to ensure operational excellence doesn't erode during transformation phases.

**Target Capacity Allocation:**
- Operational Tasks (M6): 30% of total capacity
- Transformation (M1-M5): 70% of total capacity

**Reporting Logic:** Each submethod has a dedicated epic in Jira. All operational tasks are logged as issues under the relevant epic (e.g., CAB preparation logged under 6.1 epic, Operations Review prep logged under 6.1 epic, audit requests logged under 6.2 epic).

**Note on Ad-Hoc Support:** Operational consultation and ad-hoc process guidance are absorbed into Submethod 6.1 (Governance) rather than being tracked separately, avoiding positioning the team as a "service desk" while still providing necessary support.

---

## Submethods

### Submethod 6.1: Process Governance, CAB Orchestration & RCA Facilitation

**Objective:** Maintain effective change governance through monthly CAB operations, process reviews, and retrospective facilitation

**Activities:**
- Monthly CAB facilitation and RFC review
- CAB prep work (agenda creation, RFC pre-review, material preparation)
- CAB decision documentation and communication
- Monthly governance reviews (Change, Incident, Problem Management)
- Operations Review preparation and coordination
- **RCA orchestration and participation** (team-led retrospectives as per Retrospective Transformation model - M3.3)
- High-stake retrospective governance (coordinating retrospective process for complex/critical incidents)
- Process adherence monitoring and exception handling
- Governance reporting for leadership
- Ad-hoc process guidance and consultation to Engineering teams (absorbed here, not separately measured)
- Internal quarterly team performance retrospectives

**Success Criteria:**
- Monthly CAB operates efficiently (low prep time, high first-pass approval)
- Monthly governance reviews completed on schedule
- RCA orchestration support provided for mandatory retrospectives
- Process adherence issues identified and addressed proactively
- High-stake retrospectives coordinated effectively

**Owner:** Inês Matos (CAB & governance), team rotation for RCA facilitation

**Jira Epic:** Submethod 6.1 - Process Governance & CAB
**Reporting:** All tasks logged under this epic (CAB prep, Operations Review prep, high-stake retrospective coordination, etc.)

---

### Submethod 6.2: Audit & Compliance Sustainment

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

**Owner:** Laura Ferreira

**Jira Epic:** Submethod 6.2 - Audit & Compliance
**Reporting:** All audit requests logged as tasks under this epic

---

### Submethod 6.3: Documentation & Knowledge Management

**Objective:** Maintain accurate, current process documentation to enable self-service

**Activities:**
- Process framework documentation maintenance (Change, Incident, Problem, Failure Management)
- Runbook and operational guide updates
- Standards and policy documentation
- Tool usage guides (Jira workflows, Confluence templates)
- Documentation reviews (quarterly or triggered by process changes)
- Knowledge base organization and searchability improvements

**Success Criteria:**
- Critical documentation reviewed and updated within 6 months
- Documentation accuracy validated through user feedback
- Self-service adoption increases

**Owner:** Laura Ferreira

**Jira Epic:** Submethod 6.3 - Documentation & Knowledge Management
**Reporting:** All documentation tasks logged under this epic

---

### Submethod 6.4: Measurement Infrastructure Operations

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

**Owner:** Paulo Alves Monteiro

**Jira Epic:** Submethod 6.4 - Measurement Infrastructure Ops
**Reporting:** All measurement infrastructure tasks logged under this epic

---

### Submethod 6.5: Continuous Improvement Backlog

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

**Jira Epic:** Submethod 6.5 - Continuous Improvement Backlog
**Reporting:** All improvement backlog tasks logged under this epic

---

## Measurements

### M6.1: Operational Capacity Allocation (Overall Method 6)

**Metric:** % of story points completed on operational tasks (M6) vs transformation work (M1-M5)

**Definition:** Track story points delivered on operational activities vs transformation initiatives using existing Jira epic structure

**Target:**
- Operational Tasks (M6): ~30% of total story points
- Transformation (M1-M5): ~70% of total story points

**Rationale:**
- Target: 70% transformation capacity enables significant V2MOM progress while maintaining operational excellence
- If Operational > 35%: Transformation slows, V2MOM at risk
- If Operational < 25%: Operational quality degrades, governance gaps emerge
- Sweet spot: ~30% operational allows both operational excellence and transformation progress
- Story points = relative effort, good proxy for capacity without manual time tracking overhead

**Measurement Logic:**
- Each submethod already has dedicated Jira epics
- Team estimates and tracks story points as normal
- Aggregate completed story points by epic/method quarterly
- Calculate: `(M6 Story Points / Total Story Points) × 100`

**Breakdown by Submethod (Target Allocation):**
- 6.1 Process Governance & CAB: 12-15% (monthly CAB + governance reviews + Operations Review prep + high-stake retrospectives + ad-hoc consultation)
- 6.2 Audit & Compliance: 5-10% (variable by audit season)
- 6.3 Documentation & Knowledge: 3-5%
- 6.4 Measurement Infrastructure Ops: 3-5%
- 6.5 Continuous Improvement Backlog: 2-4%

**Baseline:** To be established Q1 2026 (analyze Q4 2025 story points by epic)

**Expected Trend:**
- Q1 2026: 40-45% Operational (high due to audit season, FedRAMP prep baseline work)
- Q2 2026: 32-35% Operational (transformation ramp-up, audits complete)
- Q3-Q4 2026: ~30% Operational (sustainable operating rhythm achieved, target met)

**Calibration:**
- Quarterly team retrospective question: "Do story points by epic accurately reflect our capacity allocation, or is significant work happening outside Jira?"
- If significant untracked work exists (e.g., Slack consultations, ad-hoc support, meetings), supplement with quarterly capacity estimate

**Limitations & Mitigations:**
- **Limitation:** Story points don't capture all work (ad-hoc consultations, urgent support, meetings)
- **Mitigation:** All operational tasks logged as Jira issues under submethod epics; if untracked work becomes significant, add quarterly retrospective capacity check
- **Limitation:** Story points = relative effort, not exact time
- **Mitigation:** Acceptable trade-off for zero ongoing tracking overhead; story points are good enough for V2MOM capacity planning

**SMART Assessment:** ✓ SMART - Clear metric (%), measurable via existing Jira data, target defined, achievable without additional overhead, relevant to capacity planning

---

### M6.2: Process Orchestration Effectiveness (CAB & RCA) (Submethod 6.1)

**Metric:** Multiple metrics tracking governance and retrospective orchestration

**Definition:** Track CAB and RCA orchestration effectiveness to ensure governance and retrospective facilitation don't become capacity bottlenecks

**Target (Q2 2027, quarterly tracking):**
- CAB Prep Time: < 4 hours per session
- First-Pass Approval Rate: > 85%
- RCA Orchestration Coverage: > 90%

**Rationale:**
- CAB is monthly recurring event (10-15% of team capacity including prep and follow-up)
- RCA orchestration (team-led retrospectives per M3.3 Retrospective Transformation) requires PE facilitation support
- Inefficient CAB/RCA preparation/execution consumes excessive capacity
- High first-pass approval indicates good pre-meeting RFC quality
- High RCA orchestration coverage ensures mandatory retrospectives receive PE facilitation support

**Measurement Logic:**

**M6.2a: CAB Prep Time**
- Track: Time spent preparing for monthly CAB (RFC pre-review, agenda creation, material prep)
- Target: < 4 hours per CAB session
- Measurement: Manual time logging or Jira worklog

**M6.2b: First-Pass Approval Rate**
- Track: % of RFCs approved on first CAB review (no rework/re-submission needed)
- Target: > 85%
- Numerator: RFCs approved at CAB without rework requests
- Denominator: Total RFCs reviewed at CAB
- Calculation: `(RFCs Approved First Review / Total RFCs Reviewed) × 100`

**M6.2c: RCA Orchestration Coverage**
- Track: % of mandatory retrospectives with PE facilitation/orchestration support
- Target: > 90%
- Numerator: Mandatory retrospectives with PE orchestration/participation
- Denominator: Total mandatory retrospectives
- Calculation: `(RCAs with PE Support / Total Mandatory RCAs) × 100`
- **Context:** Covers team-led retrospective model from Retrospective Transformation (M3.3) where PE facilitates collaborative RCA sessions

**Baseline:** To be established Q2 2026 (CAB metrics from historical data, RCA orchestration from M3.3 implementation)

**Owner:** Vera Branco (executed in rotation across team)

**Integration with Other Metrics:**
- **M2.3 (RFC Rejection Velocity):** Faster pre-CAB rejection improves first-pass approval rate
- **M2.4 (Manual Resilience):** Automating repetitive changes reduces CAB RFC volume
- **M2.1 (Change Lead Time):** Efficient CAB reduces RFC processing time
- **M3.3 (Retrospective Transformation):** RCA orchestration coverage measures PE facilitation support for team-led retrospectives
- **M3.5 (RCA Completion Rate):** RCA orchestration enables completion of mandatory retrospectives
- **M3.6 (Maturity Assessment):** PE facilitation supports maturity assessment during retrospectives

**SMART Assessment:** ✓ SMART - Multiple clear metrics (time, %), measurable, targets defined, relevant to capacity optimization and retrospective transformation support

---

### M6.3: Audit Request Fulfillment Rate (Submethod 6.2)

**Metric:** % of audit evidence and compliance requests fulfilled within agreed deadline

**Definition:** Track on-time delivery of audit-related requests to ensure compliance obligations are met

**Target:** > 95% on-time fulfillment by Q2 2027

**Rationale:**
- Audit season creates unpredictable operational tasks load spikes (10-15% capacity)
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

**Baseline:** To be established Q1 2026 from Q4 2025 audit request history (if tracked)

**Integration with Other Methods:**
- **M1 (FedRAMP):** FedRAMP audit support becomes operational tasks post-authorization (Q3 2026+)
- **M2-M5:** Audit requests for transformation initiatives tracked here

**SMART Assessment:** ✓ SMART - Clear metric (%), measurable, target defined, relevant to compliance obligations

---

### M6.4: Dashboard Operational Availability (Submethod 6.4)

**Metric:** % of V2MOM dashboards operational and accurate (data quality validated)

**Definition:** Track availability and accuracy of measurement infrastructure built in Method 4

**Target:** > 98% dashboard availability (operational with accurate data) by Q2 2027

**Rationale:**
- Method 4 builds measurement infrastructure; Method 6.4 sustains it
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

**Baseline:** To be established Q2 2026 (after Method 4 dashboards deployed)

**Integration with Method 4:**
- M4 creates dashboards (project work)
- M6.4 sustains dashboards (operational tasks)

**SMART Assessment:** ✓ SMART - Clear metric (%), measurable, target defined, relevant to measurement infrastructure reliability

---

## Capacity Planning Model

### Quarterly Capacity Allocation Targets

Based on M6.1 tracking, target capacity allocation for Process Engineering team:

| Category | Target % | Q1 2026 (Est) | Q2 2026 (Goal) | Q3-Q4 2026 (Goal) |
|----------|----------|---------------|----------------|-------------------|
| **Operational Tasks (M6)** | **~30%** | **40%** | **32%** | **30%** |
| 6.1 CAB & Governance | 12-15% | 20% | 15% | 13% |
| 6.2 Audit & Compliance | 5-10% | 12% | 10% | 8% |
| 6.3 Documentation | 3-5% | 3% | 3% | 4% |
| 6.4 Measurement Ops | 3-5% | 2% | 2% | 3% |
| 6.5 Improvement Backlog | 2-4% | 1% | 1% | 1% |
| Untracked/Buffer | 2-3% | 2% | 1% | 1% |
| **Transformation (M1-M5)** | **~70%** | **60%** | **68%** | **70%** |

**Key Insights:**
- **Q1 2026:** Audit-heavy season (SOC2, FedRAMP prep) drives 40% operational load
  - CAB & Governance (6.1): 20% capacity (monthly CAB + Operations Review prep + high-stake retrospectives + ad-hoc consultation)
  - Audit & Compliance (6.2): 12% capacity
  - Documentation, Measurement Ops, Backlog: 6% combined
  - Transformation work: 60%

- **Q2 2026:** Transition to balanced load as audits complete
  - CAB & Governance: 15% (normal monthly rhythm)
  - Audit drops to 10% (post-audit monitoring)
  - Operational Tasks: 32% total
  - Transformation ramps up to 68%

- **Q3-Q4 2026:** Target sustainable rhythm achieved
  - Operational Tasks: 30% (efficient operations, target met)
  - CAB & Governance: 13% (optimized monthly CAB + governance routines)
  - Audit: 8% (baseline sustainment)
  - Transformation: 70% (full capacity for M1-M5 delivery)

---

## Operational Optimization Strategies

To achieve and maintain ~30% operational target:

### 1. CAB Efficiency Improvements (Submethod 6.1 → M6.2)
- **Strategy:** Reduce prep time via standardized templates, pre-screening automation
- **Impact:** Target 13% capacity (down from 20% in Q1)
- **Enablers:**
  - M2.3 (RFC Rejection Velocity): Fast pre-CAB rejection reduces CAB load
  - M2.4 (Manual Resilience): Automation candidates identified, reducing RFC volume
  - Standardized CAB prep checklist and templates

### 2. Self-Service Documentation (Submethod 6.3)
- **Strategy:** Improve documentation quality and discoverability to enable self-service
- **Impact:** Reduce ad-hoc consultation burden absorbed in 6.1
- **Enablers:**
  - Better documentation quality and currency (6.3)
  - M4.1 (Executive Metric Literacy): Training reduces ad-hoc metric interpretation requests
  - Search optimization and documentation portal improvements

### 3. Process as Code (M5 → M6)
- **Strategy:** Automate repetitive governance tasks (e.g., RFC validation, evidence collection)
- **Impact:** Reduce capacity across multiple submethods (6.1, 6.2, 6.4, 6.5)
- **Enablers:**
  - M5.1-M5.3: Skills deployed for process execution automation
  - M2.4: Automation candidates feed M5 backlog

### 4. Training Scale (M4 → M6.1)
- **Strategy:** Scalable training reduces one-off consultation volume
- **Impact:** Fewer ad-hoc requests (absorbed in 6.1) as teams become self-sufficient
- **Enablers:**
  - M4.1: Training programs for process literacy
  - Brown Bag sessions and recorded training materials

### 5. Audit Preparation Front-loading (Submethod 6.2)
- **Strategy:** Continuous evidence collection reduces peak-season crunch
- **Impact:** Smoother capacity consumption (avoid 12% spikes in Q1)
- **Enablers:**
  - Automated evidence collection pipelines (M5)
  - Quarterly compliance reviews vs annual audit crunch
  - Evidence repository maintained year-round

---

## Integration with Other Methods

### M6 ↔ M1 (FedRAMP Enablement)
- **M1 is project work** (transformation capacity) during Q1-Q2 2026
- **M6.3 (Audit Fulfillment)** tracks FedRAMP audit support as operational tasks post-authorization (Q3 2026+)

### M6 ↔ M2 (Change Management Transformation)
- **M2.1 (Lead Time Reduction)** reduces RFC review burden on CAB → improves M6.2
- **M2.3 (Rejection Velocity)** reduces CAB load → improves M6.2
- **M2.4 (Manual Resilience)** identifies automation candidates → reduces M6.1 capacity
- **M6.2 (CAB Effectiveness)** measures operational impact of M2 improvements

### M6 ↔ M3 (Incident Response Transformation)
- **M3 transformation work** (retrospectives, RCA quality) is capacity in M1-M5
- **M6 operational tasks** cover ongoing incident process governance, triage support, ad-hoc escalation support (absorbed in 6.1)
- **6.1** includes high-stake retrospective governance for complex incidents

### M6 ↔ M4 (Metrics Orchestration)
- **M4 creates metrics infrastructure** (dashboards, lineage docs) as project work (M1-M5 capacity)
- **M6.4 (Measurement Ops)** sustains infrastructure (dashboard maintenance, data quality) as operational tasks
- **M4.1 (Training)** reduces ad-hoc metric interpretation requests → reduces 6.1 capacity

### M6 ↔ M5 (Process as Code)
- **M5 builds automation** (skills, blueprints, extension packages) as project work (M1-M5 capacity)
- **M6 operational tasks** cover ongoing tool administration, support for deployed skills (absorbed in 6.5)
- **M5 success** should reduce M6 operational load over time (automation reduces manual toil) → measurable via M6.1 trends

---

## Summary: Method 6 Measurements

| Metric | Submethod | Target | Owner | Baseline | Status |
|--------|-----------|--------|-------|----------|--------|
| M6.1: Operational Capacity Allocation | Overall M6 | 50-60% transformation, 40-50% operational tasks by Q2 2027 | Vera | Q2 2026 | Track quarterly |
| M6.2: Process Orchestration Effectiveness (CAB & RCA) | 6.1 | <4h CAB prep, >85% first-pass approval, >90% RCA orchestration by Q2 2027 | Vera (rotation) | Q2 2026 | Track quarterly |
| M6.3: Audit Fulfillment | 6.2 | >95% on-time by Q2 2027 | Laura | Q2 2026 | Track monthly |
| M6.4: Dashboard Availability | 6.4 | >98% operational by Q2 2027 | Paulo | Q2 2026 | Track weekly |

**Coverage Note:** Submethods 6.3 (Documentation & Knowledge Management) and 6.5 (Continuous Improvement Backlog) are covered by M6.1 (Operational Capacity Allocation) rather than having dedicated metrics. This approach avoids excessive measurement overhead for operational activities while maintaining visibility through overall capacity tracking.

---

**Last Updated:** 2026-04-04
