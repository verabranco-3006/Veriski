# V2MOM 2026 - Refined SMART Measurements & Implementation

**Date:** March 10, 2026
**Purpose:** Refine all V2MOM measurements to be SMART (Specific, Measurable, Achievable, Relevant, Time-bound) and define implementation approach

---

## Method 1: O11 FedRAMP Operational Enablement

### M1.1: 3PAO Design Integrity ✓ SMART

**Metric:** Number of process-related findings classified as "Deficient" or "Non-Compliant" during formal 3PAO assessment

**Definition:** Process-related findings from Knox 3PAO assessment in "Management" and "Operational" control families

**Target:** 0 findings by end of Q2 2026 (audit window)

**Measurement Logic:** Review formal Assessment Report sections: "Management" and "Operational" control families

**Implementation:**
- **Data Source:** 3PAO Assessment Report (delivered by Knox)
- **Collection Method:** Manual extraction from Assessment Report post-audit
- **Frequency:** One-time measurement post-3PAO audit
- **Owner:** Vera Branco
- **Dashboard:** Not applicable (one-time external audit result)

**SMART Assessment:** ✓ Complete - Binary outcome, clear timeline, measurable

---

### M1.2: Control Adherence (First Customer) ✓ SMART

**Metric:** % of tickets and actions for first FedRAMP customer adhering to operational frameworks and OLAs during first 60 days of production

**Definition:** Compliance rate for all incident, change, and problem tickets for first FedRAMP customer

**Target:** > 95% during first 60 production days (Q3 2026)

**Measurement Logic:** Automated Jira reporting filtered by first customer project, tracking OLA breaches and mandatory evidence attachments

**Implementation:**
- **Data Source:** Jira (FedRAMP customer project)
- **Collection Method:** Automated dashboard query
  - Filter: Project = [First FedRAMP Customer]
  - Timeframe: First 60 days from production go-live
  - Numerator: Tickets WITH all mandatory fields + evidence + OLA adherence
  - Denominator: Total tickets created
- **Frequency:** Daily monitoring during 60-day window, weekly reporting
- **Owner:** Vera Branco
- **Dashboard:** Jira Governance Dashboard (create custom filter + gadget)
- **Automation:** Jira Automation rule to flag non-compliant tickets in real-time

**SMART Assessment:** ✓ Complete - Specific timeframe (60 days), measurable (%), clear target

---

### M1.3: Training Certification Rate ✓ SMART

**Metric:** % of designated FedRAMP Support Group completing mandatory process certification before audit window

**Definition:** Training completion rate for all staff designated as "FedRAMP Support Group"

**Target:** 100% by end of Q2 2026 (before audit window)

**Measurement Logic:** Compare "Designated FedRAMP Staff" roster against "Course Completed" records in LMS

**Implementation:**
- **Data Source:** LMS (Learning Management System) + FedRAMP Staff Roster
- **Collection Method:**
  - Maintain FedRAMP Staff Roster in Confluence or Jira
  - Track completion via LMS course enrollment/completion reports
  - Cross-reference roster vs. completion records
- **Frequency:** Weekly tracking during Q1-Q2 2026
- **Owner:** Vera Branco
- **Dashboard:** LMS completion dashboard or manual tracking spreadsheet
- **Automation:** LMS email reminders for incomplete certifications

**SMART Assessment:** ✓ Complete - Clear population, measurable, time-bound

---

## Method 2: Transform Change Management

### M2.1: Change Lead Time Reduction ✓ SMART - BASELINE VALIDATED

**Metric:** % reduction in mean time from "RFC Creation" to "Implementation" for Normal Changes

**Definition:** Average lead time for Normal Changes compared to H2 2025 validated baseline

**Baseline (H2 2025):** 16 days average (382 hours) - Validated from 117 completed RFCs

**Target:** -30% reduction by Q1 2027 → **11 days** (11.2 days target)

**Intermediate Milestones:**
- Q2 2026: 15 days (-6% vs baseline)
- Q3 2026: 14 days (-12% vs baseline)
- Q4 2026: 12 days (-25% vs baseline)
- Q1 2027: 11 days (-30% vs baseline)

**Measurement Logic:**
- Calculation: `Implementation Timestamp - Created Date` for all Completed RFCs
- Comparison: Current quarter average vs. H2 2025 baseline (16 days)
- Result: % reduction achieved

**Implementation:**
- **Data Source:** Jira RFC project (Project Key: RFC, Issue Type: "Request For Change")
- **Collection Method:**
  - Query: Status = Completed AND customfield_18619 (Implementation Timestamp) is populated
  - Calculate: Average lead time per quarter
  - Fields needed: Created date, Implementation Timestamp (customfield_18619)
  - Sample size: All completed RFCs in period
- **Frequency:** Quarterly measurement, monthly progress tracking
- **Owner:** Laura Ferreira
- **Dashboard:** Jira custom report or Power BI dashboard
  - Metric: `(Current Quarter Avg - 16 days) / 16 days * -100`
  - Visualization: Trend line showing progression toward 11-day target
- **Automation:** Scheduled Jira query to export lead time data quarterly

**Data Validation:**
- H2 2025 sample: 117 completed RFCs analyzed
- Average: 16 days (382 hours)
- Range: 0 hours (min) to 6114 hours (max - outliers for investigation)

**SMART Assessment:** ✓ Complete - Baseline validated, specific targets, measurable (%), time-bound with milestones

---

### M2.2: Standard Change Promotion Rate ✓ SMART

**Metric:** % increase in volume of changes transitioned from "Normal" to "Standard" track

**Definition:** Growth in number of Standard Change executions compared to baseline

**Target:** +50% increase by Q1 2027

**Measurement Logic:** Track number of unique Change Models classified as "Standard" and their execution frequency

**Implementation:**
- **Data Source:** Jira Change Catalog Registry + Change Management project
- **Collection Method:**
  - Baseline: Count of Standard Change executions in 2024 H2
  - Track: Count of Standard Change executions per quarter in 2026
  - Calculation: `(2026 Qn Standard Changes - Baseline) / Baseline * 100`
- **Frequency:** Quarterly measurement
- **Owner:** Laura Ferreira
- **Dashboard:** Change Catalog Registry report (Confluence + Jira query)
- **Automation:** Jira filter for `Change Type = Standard` + count per quarter

**SMART Assessment:** ✓ Complete - Clear baseline, measurable, time-bound

**Refinement Suggestion:** Track both # of unique Standard Change Models AND # of executions (two separate metrics)

---

### M2.3: RFC Rejection Velocity ✓ SMART

**Metric:** Mean time to reject incomplete or non-compliant RFCs

**Definition:** Average time from RFC submission to "Rejected/Needs Info" status for failed RFCs

**Target:** < 40 minutes by end of Q2 2026

**Measurement Logic:** Measure time elapsed between "RFC Submission" and "Rejected/Needs Info" status change

**Implementation:**
- **Data Source:** Jira Audit Logs (Change Management project)
- **Collection Method:**
  - Filter RFCs with Status History: Created → Rejected OR Created → Needs Info
  - Calculate: `Status Change Timestamp - Created Timestamp`
  - Aggregate: Mean time across all rejected RFCs per month/quarter
- **Frequency:** Monthly tracking
- **Owner:** Laura Ferreira
- **Dashboard:** Jira custom report or automation email
- **Automation:** Jira Automation rule to timestamp rejection + scheduled query for average calculation

**SMART Assessment:** ✓ Complete - Specific metric (mean time), clear target (40 min), measurable

**Refinement Suggestion:** Define current baseline (e.g., if current is 2 hours, target progression: Q1: <90 min, Q2: <40 min)

---

### M2.4: Manual Resilience Identification ✓ SMART

**Metric:** % of reviewed Normal RFCs flagged as "Automation Candidate"

**Definition:** Percentage of Normal RFCs reviewed by CAB where the reviewer identifies the change as repetitive, manual, or automatable

**Target:** < 20% by Q1 2027

**Rationale:**
- Lower % over time indicates successful automation implementation (fewer repetitive manual changes)
- Provides data-driven input for automation backlog (M5.x Process as Code)
- Enables tracking of "toil reduction" opportunities
- Note: Decreasing rate = success (we're eliminating manual/repetitive patterns)

**Measurement Logic:**
- **Numerator:** Count of Normal RFCs where "Reviewer Decision Reason" = "Automation Candidate" (any priority level)
- **Denominator:** Total Normal RFCs that reached "Reviewed - Ready for Approval" status
- **Calculation:** `(Automation Candidate RFCs / Total Normal RFCs Reviewed) × 100`

**Scope:**
- **Includes:** Normal RFCs only (require CAB review and approval)
- **Excludes:** Standard RFCs (already pre-approved/automated) and Emergency RFCs (different process, though can still be flagged separately for pattern analysis)

**Implementation:**

**Prerequisites (Q1 2026):**
- **Laura Ferreira must create:** Rigorous review protocol for identifying automation candidates
  - Protocol should define criteria: Frequency (repeated RFCs), Repeatability (script-like steps), Toil Factor (manual effort), Risk Reduction (automation makes it safer)
  - Training materials for CAB reviewers
  - Assessment time: Target < 3 minutes additional per RFC review

**Data Source:** Jira RFC Project (customfield required)

**Collection Method:**
1. **Add Jira custom field:** "Reviewer Decision Reason" (multi-select dropdown)
   - Location: CAB Review tab
   - Required: Yes (mandatory when transitioning to "Reviewed - Ready for Approval")
   - Options:
     - ✅ "Approved as Designed" (default)
     - 🎯 "Automation Candidate - High Priority" (immediate ROI)
     - 🎯 "Automation Candidate - Medium Priority" (near-term opportunity)
     - 🎯 "Automation Candidate - Low Priority" (long-term)
     - 🔄 "Promote to Standard Candidate" (should be in Change Catalog)
     - ⚠️ "Incomplete Evidence"
     - ⚠️ "Risk Assessment Concerns"

2. **Add conditional field:** "Automation Reasoning" (text field, multi-line)
   - Required if: "Automation Candidate" selected
   - Min length: 100 characters
   - Captures: Why automatable (frequency/repeatability/toil/risk), proposed approach, business case

3. **Jira Automation Rules:**
   - Rule 1: Require "Automation Reasoning" if candidate flagged
   - Rule 2: Alert Process Engineering team when RFC flagged
   - Rule 3: Weekly summary report of flagged RFCs
   - Rule 4: Alert reviewer if similar RFCs found in past 90 days (prompts flagging)

**Data Queries:**

Numerator (Automation Candidates):
```jql
project = RFC
AND issuetype = "Normal RFC"
AND status IN ("Reviewed - Ready for Approval", "Approved by CAB", "Rejected by CAB")
AND "Reviewer Decision Reason" ~ "Automation Candidate"
AND created >= startOfQuarter() AND created <= endOfQuarter()
```

Denominator (Total Normal RFCs Reviewed):
```jql
project = RFC
AND issuetype = "Normal RFC"
AND status IN ("Reviewed - Ready for Approval", "Approved by CAB", "Rejected by CAB")
AND created >= startOfQuarter() AND created <= endOfQuarter()
```

**Frequency:** Quarterly measurement, monthly tracking

**Owner:** Laura Ferreira (protocol implementation + CAB reviewer training)

**Dashboard:** Jira custom dashboard "M2.4 - Automation Candidate Tracking"
- **Gadget 1:** Trend line - Automation Candidate Rate by quarter (target line at 20%)
- **Gadget 2:** Breakdown by Change Category (Restart, Retry, Config, etc.) - which have highest automation rate?
- **Gadget 3:** Top 10 automation opportunities (ranked by frequency × priority)
- **Gadget 4:** Automation pipeline - Identified → Prioritized → In Progress → Implemented
- **Gadget 5:** Impact delivered - RFCs eliminated, time saved, automations implemented

**Automation:** Scheduled Jira query runs weekly to update dashboard

**Supporting Metrics:**
- **Automation Candidate Pipeline:** Track from identification to implementation
  - Total identified: Cumulative count
  - By priority: High/Medium/Low breakdown
  - Implementation rate: (Implemented / High Priority Identified) × 100 (Target: >50% within 1 year)
  - Time to automation: Days from flagging to deployment (Target: <90 days for High Priority)

- **Reviewer Calibration:** Ensure consistent flagging
  - Flagging rate by reviewer: (Flagged by Reviewer X / Total reviewed by X) × 100
  - Target: Within 10% of average (prevents over/under-flagging)
  - False positive validation: Sample 20 flagged RFCs quarterly, assess viability (Target: >80% valid)

- **Impact Metrics:** (Lagging indicators)
  - RFCs eliminated per quarter from implemented automations
  - Time saved (hours) per quarter
  - CAB review burden reduction (% fewer Normal RFCs)

**Baseline (H2 2025):**
- Retroactive analysis needed: Review sample of 50-100 Normal RFCs from H2 2025
- Manually assess using pilot criteria (frequency, repeatability, toil, risk)
- Estimated baseline: 30-40% (hypothesis based on change management patterns)
- Use to validate Q1 2026 initial measurement

**Expected Trend:**
- Q1 2026: 30-40% (baseline, learning period)
- Q2 2026: 25-35% (protocol stabilized)
- Q3 2026: 20-30% (early automations implemented)
- Q4 2026: 15-20% (TARGET - sustained automation)

**Integration with Other Metrics:**
- **M2.1 (Change Lead Time):** Automated changes reduce lead time
- **M2.2 (Standard Change Promotion):** Some candidates become Standard vs full automation
- **M2.5 (CFR Correlation):** Automated changes improve traceability
- **M5.2 (Process as Code Blueprints):** Flagged candidates become blueprint use cases

**Validation Checks:**
- **Q1 2026:** Validate baseline - manually review 50 flagged RFCs, confirm ≥80% are valid candidates
- **Quarterly:** False positive/negative analysis (sample 20 RFCs each way)
- **Quarterly:** Inter-rater reliability test (2-3 reviewers assess same 10 RFCs, target: >70% agreement)
- **Annual:** Outcome validation - Were High Priority candidates implemented? (Target: >50%)

**Common Patterns Expected:**
- **High automation potential:** Restart operations (60-80% should be automated), Retry operations (automated retry logic), Configuration changes (config-as-code)
- **Medium automation potential:** Rollbacks to older versions, Infrastructure changes, Fast tracks (indicates missing automation for urgent paths)
- **Promote to Standard (not full automation):** Changes requiring human coordination but low risk and well-documented

**Risks & Mitigations:**
- **Risk:** Reviewer fatigue (additional work) → **Mitigation:** Keep assessment <3 min, provide clear decision tree
- **Risk:** Over-flagging (false positives) → **Mitigation:** Weekly validation, provide feedback to reviewers
- **Risk:** Under-flagging (missing opportunities) → **Mitigation:** Automated alerts for repetitive patterns, quarterly spot-checks
- **Risk:** Identification without implementation → **Mitigation:** Integration with M5.x, monthly prioritization, close the loop with reviewers

**SMART Assessment:** ✓ Complete - Measurable (%), clear baseline approach, validation mechanisms, integration with V2MOM

---

### M2.5: CFR Correlation Accuracy ✓ SMART

**Metric:** % of Incidents where automated correlation system correctly identifies the specific asset-version change responsible for the failure

**Definition:** Accuracy rate of asset-version-to-incident correlation, validated against RCA findings

**Target:** > 90% by Q1 2027

**Rationale:**
- Enables accurate CFR measurement by identifying which specific asset-version caused each failure
- Replaces "last change" assumption with data-driven correlation
- Feeds accurate Change-to-Incident data for CFR calculation
- Submethods 2.4 (governance/methodology) and 2.5 (technical implementation) build the correlation system

**Measurement Logic:**
- **Validation Method:** Monthly spot-check comparing correlation engine output vs RCA findings
- **Sample:** 20 incidents/month meeting criteria
- **Scoring:** Correct (correlation matches RCA) | Incorrect (mismatch) | Indeterminate (RCA inconclusive, exclude)
- **Calculation:** `(Correct Correlations / Valid Sample) × 100` where Valid Sample = Total - Indeterminate

**Sample Selection Criteria:**
- Priority = High OR Critical
- Incident Type IN ("Customer Reported", "System-wide", "Internal")
- Root Cause Categorization != Customer Issue
- RCA Status = Completed
- Ring IN (ring-ga, ring-ea, ring-osall)

**Implementation:**

**Prerequisites (Q1-Q2 2026):**
- **Submethod 2.4:** Define correlation methodology (timing windows, multi-asset scenarios, confidence scoring)
- **Submethod 2.5:** Build correlation engine (data integration RFC/Assets/RDINC, correlation logic, Jira integration)

**Data Source:**
- Correlation Engine output (automated)
- Jira RDINC project - RCA findings (manual validation)

**Collection Method:**

JQL Query (Monthly):
```jql
project = RDINC AND status = Solved
AND priority IN (High, Critical)
AND "Incident Type" IN ("Customer Reported", "System-wide", "Internal")
AND "Root Cause Categorization" != "Customer Issue"
AND "RCA Status" = Completed
AND resolved >= startOfMonth() AND resolved <= endOfMonth()
AND "Ring" IN ("ring-ga", "ring-ea", "ring-osall")
ORDER BY resolved DESC
```

**Validation Process (per incident):**
1. Extract correlation engine output: Suspected Asset, Version, Confidence (High/Medium/Low)
2. Review RCA findings: Which asset-version did RCA identify as root cause?
3. Compare: Does correlation match RCA?
4. Score: Match/Mismatch/Indeterminate
5. Track by confidence level: High/Medium/Low should have >95%/>80%/>60% accuracy respectively

**Frequency:** Monthly measurement, quarterly reporting

**Owner:** Inês Matos (measurement) + Laura Ferreira (change data support)

**Dashboard:**
- **Primary:** Confluence validation tracker
  - Table: Incident ID, Correlation Output (Asset, Version, Confidence), RCA Finding, Match?, Notes
  - Summary: Monthly accuracy %, Trend over time
- **Secondary:** Power BI or Jira Dashboard
  - Trend line: Accuracy % by month (target line at 90%)
  - Breakdown: Accuracy by Confidence Level (High/Medium/Low)
  - False Positive Analysis: When wrong, why? (wrong asset, wrong version, timing error, multi-asset scenario)

**Automation:**
- Correlation Engine: Automated (generates suspected correlations)
- RCA Validation: Manual (human compares correlation to RCA findings)
- Tracking: Manual entry into validation tracker (could use forms for semi-automation)

**Baseline (Q4 2025):**
- **Estimated Current:** 60-70% accuracy (correct for immediate failures, wrong for delayed failures due to "last change" assumption)
- **Validation:** Retroactively analyze 50 Q4 2025 incidents comparing "last change" vs actual RCA findings

**Expected Trend:**
- Q1 2026: 60-70% (baseline with current last-change logic)
- Q2 2026: 70-80% (initial correlation engine deployed, learning phase)
- Q3 2026: 80-90% (engine refined based on false positive analysis)
- Q4 2026: >90% (TARGET - reliable correlation)

**Supporting Metrics:**
- **Correlation Coverage:** % of incidents where correlation engine provides output (Target: >95%)
- **Confidence Distribution:** Breakdown High/Medium/Low (Target: >60% High Confidence by Q4)
- **False Positive Analysis:** Categorize correlation errors
  - Wrong Asset (correlated to wrong service)
  - Wrong Version (correct asset, wrong version)
  - Timing Error (change too old/too new to be cause)
  - Multi-Change Scenario (missed multiple contributing changes)
- **CFR Recalculation Impact:** Difference between CFR with accurate correlation vs old "last change" method

**Integration with CFR:**
- Once M2.5 shows >90% accuracy, correlation engine output becomes **trusted source** for identifying "Failed Changes" in CFR formula
- Enables: Accurate CFR trending, Asset-level CFR, Change Category CFR, Team-level CFR

**Integration with Other Metrics:**
- **M2.1 (Change Lead Time):** Faster lead time shouldn't compromise quality (CFR stays low)
- **M2.4 (Manual Resilience):** Automated changes should have lower CFR than manual
- **M5.x (Process as Code):** Automation candidates with higher CFR justify automation investment
- **M3.x (Incident Response):** Accurate correlation speeds incident resolution (know exactly what to rollback)

**Validation Checks:**
- **Monthly:** Inter-reviewer reliability (2 reviewers validate 5 incidents independently, target: >90% agreement)
- **Quarterly:** Sample size adequacy, confidence calibration (are High Confidence correlations actually more accurate?)
- **Annual:** End-to-end validation (100 incidents, RCA owners confirm correlation accuracy, target: >90%)

**Common Patterns Expected:**
- **High Accuracy Scenarios:** Immediate failures (hours after deploy), single asset changed, clear symptom-to-change mapping
- **Challenges (Require Refinement):** Delayed failures (days/weeks after deploy), multiple changes to same asset, cross-asset dependencies, configuration drift

**Risks & Mitigations:**
- **Risk:** RCA quality varies → **Mitigation:** Only use completed RCAs, train reviewers to identify inconclusive RCAs, quarterly calibration
- **Risk:** Submethod 2.5 implementation delayed → **Mitigation:** Prioritize Q1 2026, measure baseline interim, pilot narrow scope first
- **Risk:** Correlation is probabilistic, not deterministic → **Mitigation:** Use confidence scoring, accept "most likely cause" for multi-factor incidents
- **Risk:** Measurement burden on Incident Response team (20 incidents × 10 min = 3-4 hours/month) → **Mitigation:** Streamline with templates, integrate into RCA process, share work with Laura

**SMART Assessment:** ✓ Complete - Measurable (%), clear validation methodology, baseline approach, confidence-level tracking, integration with CFR

---

## Method 3: Incident Response Resilience

### M3.1: Public MTTA (Status Page) ✓ SMART

**Metric:** Mean Time to post first public status page update after system-wide incident declaration

**Definition:** Average time from system-wide incident declaration to first external status page post (https://status.outsystems.com/)

**Target:** < 30 minutes by Q1 2027

**Rationale:**
- Measures customer communication speed during system-wide incidents
- Validates IC Leader process effectiveness (rolled out Sept 2024)
- Reflects end-to-end communication chain: SRE → IC Leader → Service Controllers → Customers
- Faster communication reduces customer frustration and builds trust

**Measurement Logic:**
- **Start:** System-wide incident declared by SRE (Incident Commander)
- **End:** First status update posted to https://status.outsystems.com/
- **Calculation:** `(External Status Page First Post Timestamp - Declaration Timestamp)` per incident
- **Aggregate:** Mean time across all incidents per quarter

**Scope:**
- **Includes:** Only system-wide incidents that were posted to external status page (met criteria for customer communication)
- **Excludes:** System-wide incidents that were resolved before external posting criteria met, or Internal-only incidents

**Implementation:**

**Data Sources:**

1. **Declaration Timestamp:**
   - Source: Rootly incident declaration event
   - Field: System-wide impact declaration timestamp
   - Alternative: Slack message timestamp in #product-leadership-incidents-alerts

2. **External Status Page Timestamp:**
   - Source: https://status.outsystems.com/ (statuspage.io API backend)
   - Field: First incident component update OR first "Investigating" status post timestamp
   - Requires: API integration or Service Controller manual logging

3. **Incident Identification:**
   - Source: Jira RDINC project
   - Link: RDINC ticket to Rootly incident to Status Page incident ID

**Collection Method:**

**Step 1: Identify system-wide incidents with external posts (Quarterly)**

**Current Gap:** No Jira field exists to filter incidents posted to external status page

**Short-term approach (Q1-Q2 2026):** Manual identification
1. Query all system-wide incidents from Jira:
```jql
project = RDINC
AND "Incident Type" = "System-wide"
AND resolved >= startOfQuarter() AND resolved <= endOfQuarter()
ORDER BY resolved DESC
```

2. Manually cross-reference with https://status.outsystems.com/ to identify which were posted externally
   - Check status page incident history
   - Or query statuspage.io API: Get all incidents in time range, match to RDINC IDs via title/date

**Medium-term approach (Q3 2026+):** Add Jira field
- **Create field:** "External Status Page Posted" (Yes/No checkbox or dropdown)
- **Location:** RDINC Troubleshooting or Resolution tab
- **Populated by:** Service Controllers when posting to external status page (or via automation if statuspage.io API integration built)
- **Then JQL becomes:**
```jql
project = RDINC
AND "Incident Type" = "System-wide"
AND "External Status Page Posted" = Yes
AND resolved >= startOfQuarter() AND resolved <= endOfQuarter()
```

**Long-term approach (2027):** Automation via statuspage.io API
- Automatic linkage: When Service Controller posts to status page, Jira field auto-populated
- Or: Query statuspage.io API, match incidents to Jira RDINC via metadata (incident ID, timestamps, description)

**Step 2: For each incident, extract timestamps**

Data needed per incident:
- RDINC ID
- Rootly Incident ID (link from RDINC or Slack channel)
- Declaration timestamp (from Rootly)
- External Status Page Incident ID (from status.outsystems.com)
- First external post timestamp (from statuspage.io API)

**Step 3: Calculate time per incident**
```
Time to Public Post = External Post Timestamp - Declaration Timestamp
```

**Step 4: Calculate quarterly metric**
```
M3.1 MTTA = Mean(Time to Public Post for all incidents in quarter)
```

**Frequency:** Quarterly measurement, monthly tracking

**Owner:** Inês Matos (Incident Response Lead) + Service Controllers (data validation)

**Dashboard:**
- **Primary:** Confluence tracking page or Power BI
  - Table: Incident ID, Declaration Time, External Post Time, MTTA (minutes), Status
  - Summary: Quarterly MTTA, Trend over time, Target line at 30 min
- **Secondary:** Grafana (if Rootly/Statuspage API integration built)
  - Real-time: MTTA per incident
  - Trend: MTTA by month/quarter

**Automation:**
- **Ideal:** API integration: Rootly → Statuspage.io → automated calculation
- **MVP:** Manual tracking in Confluence with data from Rootly and status page
- **Future:** Automated alerting if incident exceeds 30 min without external post

**Baseline Assessment (Q1 2026):**

**Current Data:** Sample of 10 incidents (Oct-Nov 2024) shows limited timing data:
- 4 incidents with complete data: 0 sec, 1.5 min, 5.7 min, 34 min
- Estimated average: ~10 minutes (very limited sample)

**Baseline Approach:**

**Baseline Period:** Q4 2024 + Q1 2025 (post IC Leader rollout in Sept 2024)

**Data Sources Available:**

1. **RDINC Project** — System-wide incidents with RootlyID/RootlyKey fields, Created Date, Resolved Date
2. **MIM Project** — Service Controllers log major incidents with "Status page published at" timestamp field
3. **Rootly** — System-wide declaration timestamp (pending confirmation from SRE if available via API)

**Baseline Method:**

**Step 1: Extract RDINC System-wide Incidents**

JQL Query:
```jql
project = RDINC
AND "Incident Type" = "System-wide"
AND resolved >= "2024-10-01" AND resolved <= "2025-03-31"
ORDER BY resolved DESC
```

Extract: RDINC Key, RootlyID, Created Date, Resolved Date → Export to CSV

**Step 2: Identify MIM Tickets with Status Page Data**

Option A - If RDINC-MIM link exists:
```jql
project = MIM
AND "Status page published at" IS NOT EMPTY
AND created >= "2024-10-01" AND created <= "2025-03-31"
ORDER BY created DESC
```

Extract: MIM Key, Status page published at, Linked RDINC Key

Option B - If no link: Manually cross-reference RDINC to MIM by incident date/title/description

**Step 3: Extract Declaration Timestamp**

- **Option A:** Via Rootly API (if available) — GET /incidents/{RootlyID} → extract system-wide declaration timestamp
- **Option B:** Manual extraction from Slack #product-leadership-incidents-alerts — find declaration message timestamp
- **Option C:** Use RDINC Created Date as proxy (least accurate, note assumption of minimal Rootly-Jira sync delay)

**Step 4: Match Data and Calculate MTTA per Incident**

Create spreadsheet:

| RDINC Key | RootlyID | Declaration Timestamp | MIM Key | Status Page Published At | MTTA (minutes) | Notes |
|-----------|----------|----------------------|---------|--------------------------|----------------|-------|
| RDINC-123 | 44326 | 2024-11-15 10:00:00 | MIM-2031 | 2024-11-15 10:15:00 | 15 | Complete data |

Calculate per incident: `MTTA = (Status Page Published At - Declaration Timestamp)` in minutes

Filter: Include only incidents where "Status page published at" is NOT NULL; exclude outliers > 120 min (investigate separately)

**Step 5: Calculate Baseline Metrics**

- **Primary:** Baseline MTTA = Mean(MTTA for all incidents)
- **Supporting:** Median MTTA, Min/Max MTTA, % incidents < 30 min, Sample size

**Data Completeness Assessment:**
- Target: >70% completeness (incidents with complete data / total system-wide incidents)
- Document gaps: Missing MIM tickets, missing declaration timestamps, unmatched RDINC-MIM pairs

**Validation Checks:**
- Spot-check 3-5 incidents against Slack threads
- Investigate outliers >60 min (complex incident, IC Leader unavailable, non-standard criteria)
- Verify timestamp reasonableness (declaration not before creation, not after external post)

**Implementation Timeline:**
- Week 1: Data extraction (RDINC query, MIM query, Rootly data request)
- Week 2: Data matching (RDINC-MIM, RDINC-Rootly timestamps, identify gaps)
- Week 3: Calculation and validation (MTTA per incident, baseline metrics, spot-check)
- Week 4: Documentation (baseline MTTA, data quality, gaps, mitigation plan)

**Expected Baseline Output:**
- Baseline MTTA: 15-30 min (hypothesis)
- Sample size: 10-20 incidents with complete data
- Performance distribution: % incidents <15 min, 15-30 min, >30 min
- Data completeness: % of system-wide incidents with complete timestamp data

**Expected Trend:**
- Q1 2026: 20-30 min (baseline with current process)
- Q2 2026: 18-25 min (process refinement, template improvements)
- Q3 2026: 15-20 min (IC Leader training, automation pilots)
- Q4 2026: <15 min (TARGET - optimized process)

**Supporting Metrics (Breakdown for Diagnosis):**

**M3.1a: Internal Status Page Update Time**
- **Metric:** Mean time from declaration to first Internal Status Page update
- **Measures:** IC Leader response time
- **Start:** Declaration timestamp (Rootly)
- **End:** First Internal Status Page update (Rootly - Internal Status Page)
- **Target:** < 10 minutes
- **Purpose:** Identify if delays are in IC Leader acknowledgment/response

**M3.1b: External Transformation Time**
- **Metric:** Mean time from Internal Status Page update to External Status Page post
- **Measures:** Service Controller transformation/posting time
- **Start:** Internal Status Page first update (Rootly)
- **End:** External Status Page first post (status.outsystems.com)
- **Target:** < 15 minutes
- **Purpose:** Identify if delays are in Service Controller transformation/posting

**Breakdown Analysis:**
```
M3.1 (Total) = M3.1a (IC Leader) + M3.1b (Service Controllers)
Target: < 30 min = < 10 min (IC Leader) + < 15 min (Service Controllers) + 5 min buffer
```

**Data Requirements for Breakdown:**

1. **Rootly Internal Status Page timestamps:**
   - Can Rootly API provide first internal update timestamp per incident?
   - Alternative: Parse Slack channel messages or Rootly incident timeline

2. **If data not available:**
   - Start with M3.1 (end-to-end) only
   - Add M3.1a/M3.1b when Rootly integration improved

**Integration with Other Metrics:**
- **M3.2 (Action Item Closure):** Faster communication enables faster retrospective and action item creation
- **M3.3 (Triage Accuracy):** Accurate incident classification speeds declaration and communication
- **M3.4 (Alert Validation):** Better validation reduces false alarms that trigger unnecessary communication

**Validation Checks:**

**Monthly:**
- Spot-check: Manually validate 3-5 incidents - do timestamps align with Slack/Rootly timeline?
- Outlier analysis: Any incident > 60 min? Investigate why (IC Leader unavailable? Complex incident?)

**Quarterly:**
- Data completeness: % of system-wide incidents with complete timestamp data (Target: >90%)
- Sample size: Is sample adequate? (Target: >10 incidents per quarter for reliable mean)

**Annual:**
- Process review: Are communication templates effective? IC Leader training needed? Service Controller workflow optimized?

**Common Patterns Expected:**

**Fast Communication (<10 min):**
- Clear impact scope (single region, single service)
- IC Leader immediately available
- Standard communication template used

**Delayed Communication (>30 min):**
- Complex multi-region impact (requires investigation before external post)
- IC Leader escalation (first responder unavailable, backup paged)
- Non-standard incident (requires leadership approval before external communication)
- Off-hours incident (IC Leader response time longer)

**Risks & Mitigations:**

**Risk 1: Data availability - Rootly/Statuspage.io API integration doesn't exist**
- **Impact:** Cannot measure automatically, manual tracking burden
- **Mitigation:**
  - Q1 2026: Assess API availability (Rootly + statuspage.io)
  - MVP: Manual tracking in Confluence (extract from Rootly UI + status page manually)
  - Q2 2026: Build API integration if manual process proves valuable

**Risk 2: Incident volume too low for reliable baseline**
- **Impact:** <10 incidents per quarter = high variance in mean
- **Mitigation:**
  - Use longer baseline period (2-3 quarters)
  - Track median in addition to mean (less sensitive to outliers)
  - Combine with qualitative assessment (IC Leader feedback)

**Risk 3: Communication criteria unclear**
- **Impact:** Some incidents posted immediately, others delayed due to criteria
- **Mitigation:**
  - Document external posting criteria (when to post vs when to wait)
  - Track separately: "Immediate post required" vs "Delayed post acceptable"
  - Refine target based on incident type

**Risk 4: IC Leader/Service Controller handoff unclear**
- **Impact:** Breakdown metrics (M3.1a/M3.1b) show delays but root cause unclear
- **Mitigation:**
  - Qualitative analysis: Interview IC Leaders and Service Controllers
  - Process observation: Join incident Slack channels, observe handoff
  - Template/training improvements based on findings

**Jira Control Points (Required for Measurement):**

**Q1 2026: Implement control points in RDINC project**

**Control Point 1: External Status Page Posted (Critical)**
- **Field Name:** "External Status Page Posted"
- **Field Type:** Checkbox (Yes/No) or Dropdown (Yes/No/N/A)
- **Location:** RDINC Resolution or Troubleshooting tab
- **Purpose:** Filter incidents posted to external status page
- **Populated by:** Service Controllers (manual) when posting to status.outsystems.com
- **When:** Immediately after first external status page post
- **Validation:** Required before closing incident if "Incident Type" = System-wide

**Control Point 2: Rootly Incident Link**
- **Field Name:** "Rootly Incident ID" or "Rootly Incident URL"
- **Field Type:** Text field or URL field
- **Location:** RDINC General or Links section
- **Purpose:** Link RDINC to Rootly incident for timestamp extraction
- **Populated by:** SRE team or automation (Rootly → Jira integration if available)
- **Format:** Incident ID (e.g., "44326") or full URL
- **When:** Automatically when Rootly creates RDINC, or manually during incident creation

**Control Point 3: External Status Page Incident Link**
- **Field Name:** "Status Page Incident URL" or "Status Page Incident ID"
- **Field Type:** URL field or Text field
- **Location:** RDINC Resolution tab
- **Purpose:** Link to status.outsystems.com incident for timestamp extraction
- **Populated by:** Service Controllers when posting externally
- **Format:** Full URL (e.g., "https://status.outsystems.com/incidents/m1h99thjhsdm")
- **When:** When first external post is made

**Control Point 4: Declaration Timestamp (Optional - if Rootly link insufficient)**
- **Field Name:** "System-Wide Declaration Timestamp"
- **Field Type:** DateTime field
- **Location:** RDINC Troubleshooting tab
- **Purpose:** Capture exact declaration time if Rootly API not available
- **Populated by:** SRE Incident Commander or automation
- **When:** When system-wide impact is declared
- **Alternative:** Extract from Rootly via API using Rootly Incident ID

**Control Point 5: External Post Timestamp (Optional - if statuspage.io API insufficient)**
- **Field Name:** "External Status Page First Post Timestamp"
- **Field Type:** DateTime field
- **Location:** RDINC Resolution tab
- **Purpose:** Capture exact external post time if statuspage.io API not available
- **Populated by:** Service Controllers or automation
- **When:** When first external post is made
- **Alternative:** Extract from statuspage.io API using Status Page Incident URL

**Jira Automation Rules:**

**Rule 1: Require External Status Page fields for System-wide incidents**
```
Trigger: RDINC status changed to "Resolved"
Condition: "Incident Type" = "System-wide"
Action: If "External Status Page Posted" is empty, show warning: "Please indicate if this was posted to external status page"
```

**Rule 2: Auto-populate Rootly link (if Rootly-Jira integration available)**
```
Trigger: RDINC created
Condition: Created by Rootly automation
Action: Populate "Rootly Incident ID" from incident metadata
```

**Rule 3: Alert Process Engineering when external post threshold exceeded**
```
Trigger: "External Status Page Posted" = Yes
Condition: (External Post Timestamp - Declaration Timestamp) > 30 minutes
Action: Add comment tagging Process Engineering team, send Slack notification
```

**Implementation Priority:**

**MVP (Q1 2026 - Manual tracking):**
- Control Point 1: External Status Page Posted (checkbox) - REQUIRED
- Control Point 2: Rootly Incident Link (text field) - REQUIRED
- Control Point 3: Status Page Incident Link (URL field) - REQUIRED
- Manual timestamp extraction from Rootly UI and status page

**Phase 2 (Q2 2026 - Semi-automated):**
- Add timestamp fields (Control Points 4 & 5) if APIs prove difficult
- Service Controllers manually populate timestamps
- Jira automation for validation/alerts

**Phase 3 (Q3 2026+ - Fully automated):**
- API integration: Rootly API → auto-extract declaration timestamp
- API integration: statuspage.io API → auto-extract first post timestamp
- Automated calculation of MTTA in dashboard
- Real-time alerting for threshold violations

**SMART Assessment:** ✓ Complete - Measurable (minutes), clear start/end points, baseline approach defined, breakdown metrics for diagnosis, Jira control points defined

**Action Required:**
1. Q1 2026 Week 1-2: Implement Jira control points (fields + validation rules)
2. Q1 2026 Week 3: Train Service Controllers and SRE team on populating fields
3. Q1 2026 Week 4: Baseline assessment (analyze Q4 2024 + Q1 2025 incidents manually)
4. Q2 2026: Assess API availability (Rootly + statuspage.io), build integration if available

---

### M3.2: Action Item Plan Closure Rate ✓ SMART

**Metric:** % of High/Critical post-mortem action items closed within OLA/Deadline

**Definition:** On-time closure rate for action items from system-wide impact incidents

**Target:** > 80% by Q1 2027

**Measurement Logic:** Monitor "Due Date" vs. "Closed Date" for action items linked to system-wide incidents

**Implementation:**
- **Data Source:** Jira Problem Management (Action Item tickets)
- **Collection Method:**
  - Filter: Issue Type = "Action Item" AND Linked to Incident (System-wide Impact) AND Priority IN (High, Critical)
  - On-time: `Closed Date <= Due Date`
  - Late: `Closed Date > Due Date`
  - Calculation: `(On-time Closures / Total Action Items) * 100`
- **Frequency:** Quarterly measurement, monthly tracking
- **Owner:** Inês Matos
- **Dashboard:** Jira custom dashboard with SLA tracking gadget
- **Automation:** Jira SLA tracking + scheduled report for closure rate

**SMART Assessment:** ✓ Complete - Clear criteria (on-time vs late), measurable, target defined

**Refinement Suggestion:** Define OLA/Deadline standards (e.g., High = 30 days, Critical = 14 days)

---

### M3.3: Triage Accuracy ✓ SMART

**Metric:** % of tickets correctly categorized at intake (Service Incident vs Support Case)

**Definition:** % of incidents where initial classification remains unchanged throughout lifecycle

**Target:** > 80% by Q1 2027

**Measurement Logic:** % of incidents where initial classification unchanged until resolution

**Implementation:**
- **Data Source:** Jira Transition Logs (Incident + Support projects)
- **Collection Method:**
  - Track: Incidents with Status History showing NO reclassification
  - Correct: Initial "Issue Type" = Final "Issue Type" at resolution
  - Incorrect: "Issue Type" changed during lifecycle (e.g., Incident → Support Case OR Support Case → Incident)
  - Calculation: `(Unchanged Classifications / Total Tickets) * 100`
- **Frequency:** Quarterly measurement
- **Owner:** Inês Matos
- **Dashboard:** Jira custom report querying Status History for Issue Type changes
- **Automation:** Scripted query to analyze Jira history logs for reclassification events

**SMART Assessment:** ✓ Complete - Clear logic (unchanged classification), measurable

**Refinement Suggestion:** Exclude edge cases where reclassification is intentional (e.g., during triage refinement period)

---

### M3.4: Alert Validation Accuracy ✓ SMART

**Metric:** % of alerts correctly validated and filtered before reaching Engineering

**Definition:** % of alerts where "Validated as Incident" flag matches actual outcome

**Target:** > 85% by Q1 2027

**Measurement Logic:** % of alerts where validation decision (Yes/No) matches actual outcome

**Implementation:**
- **Data Source:** Validation Practice Log (new tracking mechanism needed)
- **Collection Method:**
  - Create "Alert Validation Log" in Jira or Confluence
  - For each alert: Track validation decision (Incident = Yes, Filtered = No) + actual outcome
  - Validation correct if:
    - Validated as Incident (Yes) → Became actual incident
    - Filtered (No) → Truly non-actionable (verified post-facto)
  - Calculation: `(Correct Validations / Total Alerts Validated) * 100`
- **Frequency:** Monthly measurement (sample-based), quarterly reporting
- **Owner:** Inês Matos
- **Dashboard:** Confluence page or Jira custom project for alert tracking
- **Automation:** Integration with alerting tool (PagerDuty/Rootly) to log alerts + validation decisions

**SMART Assessment:** ⚠️ MISSING TARGET - Proposed target > 85%, needs validation mechanism

**Action Required:**
1. Define alert validation practice (who validates, when, criteria)
2. Implement Alert Validation Log (Jira project or Confluence template)
3. Pilot for 1 month to establish baseline, then set target

---

### M3.5: RCA Completion Rate & Lead Time (NEW - Retrospective Transformation)

**Metric:** % of mandatory retrospectives completed within SLA + Average RCA lead time

**Definition:**
- **Completion Rate:** % of incidents requiring retrospectives that have RCA completed
- **Lead Time:** Average time from incident resolution to retrospective completion

**Target:**
- > 90% completion rate by Q1 2027
- < 14 days RCA lead time by Q1 2027

**Rationale:**
- Validates team-led retrospective model is working (teams actually complete them)
- Measures learning loop responsiveness (faster RCA = faster learning)
- Directly supports Operations Review metrics mentioned in retrospective transformation plan
- Baseline metric for Inês's retrospective transformation success

**Measurement Logic:**
- **Mandatory retrospectives:** Incidents meeting criteria (severity, customer impact, recurrence patterns - to be defined in transformation Phase 1)
- **Completed:** Retrospective document exists and approved by Value Stream Leader
- **Lead Time:** `(Retrospective Approval Date - Incident Resolution Date)` in days
- **Calculation:** `(Approved Retrospectives / Mandatory Incidents) × 100`

**Implementation:**
- **Data Source:** Jira RDINC project + Retrospective tracker (Confluence or Jira)
- **Collection Method:**
  - Q1 2026: Define mandatory retrospective criteria (with Inês and SRE)
  - Identify incidents requiring retrospectives (based on mandatory criteria)
  - Track retrospective status: Not Started → In Progress → Review (EM) → Approved (VS Leader)
  - Calculate completion rate: `(Approved Retrospectives / Mandatory Incidents) × 100`
  - Calculate lead time: Average days from resolution to approval
- **Frequency:** Monthly tracking, quarterly reporting
- **Owner:** Inês Matos
- **Dashboard:** Operations Review dashboard per value stream
  - Completion rate trend by value stream
  - Lead time trend over quarters
  - Overdue retrospectives alert view
- **Automation:** Jira link between RDINC incidents and retrospective documents, automated alerts for overdue retrospectives

**Baseline:** To be established Q1 2026 from current SRE-led retrospective model

**Integration with Other Metrics:**
- **M3.2 (Action Item Closure):** Retrospectives generate action items tracked by M3.2
- **M3.6 (RCA Quality):** Completion is necessary but not sufficient - M3.6 measures quality
- **M3.8 (Improvement Rate):** Faster completion enables faster operational improvements

**Integration with Retrospective Transformation:**
- Aligns with Phase 2 pilot tracking (Q2-Q3 2026)
- Feeds Operations Review analytics
- Establishes baseline before full rollout in Q3-Q4
- Tracks adoption of team-led model

**SMART Assessment:** ✓ SMART - Clear deliverable (completion %), measurable (days), time-bound, aligned with transformation

---

### M3.6: RCA Quality Score (Outcome-Focused) (NEW - Retrospective Transformation)

**Metric:** Average quality score for retrospectives based on outcome-focused criteria

**Definition:** AI/Koda-assisted quality assessment measuring if retrospectives focus on outcomes (what changed) vs outputs (what happened)

**Target:** Average quality score > 4.0/5.0 by Q1 2027

**Rationale:**
- Validates narrative shift from output to outcome focus (key transformation goal)
- Ensures team-led retrospectives maintain quality without SRE facilitation
- Measures depth of analysis (not just completion checkbox)
- Enables coaching and continuous improvement
- Directly implements AI/Koda-assisted auditing mentioned in transformation plan

**Measurement Logic:**

Quality framework criteria (5-point scale per criterion):

1. **Context Setting:** Clear incident timeline and customer impact documented? (1-5)
   - 5: Complete timeline, customer impact quantified, asset/system clearly identified
   - 3: Basic timeline exists, customer impact mentioned
   - 1: Incomplete or missing context

2. **Root Cause Analysis:** Deep analysis vs surface-level? (1-5)
   - 5: Multiple contributing factors identified, root cause validated with evidence
   - 3: Root cause stated but limited supporting analysis
   - 1: Superficial or unclear root cause

3. **Outcome Focus:** Action items with owners and timelines? (1-5)
   - 5: All action items have owners, deadlines, success criteria, measurable outcomes
   - 3: Action items listed with owners but incomplete details
   - 1: Vague action items or no clear ownership

4. **Learning Captured:** Patterns identified, preventability assessed? (1-5)
   - 5: Patterns identified, similar incidents referenced, prevention strategy clear
   - 3: Some pattern discussion but limited depth
   - 1: No pattern identification or learning captured

5. **Completeness:** All sections addressed per framework? (1-5)
   - 5: All framework sections complete (Context, Analysis, Outcomes, Learning)
   - 3: Most sections complete, some gaps
   - 1: Major sections missing

**Overall RCA Quality Score:** Average across all 5 criteria

**Implementation:**
- **Data Source:** Retrospective documents (Confluence pages)
- **Collection Method:**
  - **Phase 1 (Q1-Q2 2026):** Manual quality assessment by Process Engineering using rubric
  - **Phase 2-3 (Q3-Q4 2026):** AI/Koda-assisted auditing tool (to be developed)
  - Quarterly sample: 20-30 retrospectives per value stream (statistically significant)
  - Automated scoring based on framework criteria
  - Manual spot-check validation (10% sample) to calibrate AI
  - Provide feedback to teams on quality gaps
- **Frequency:** Quarterly measurement (sample-based), monthly pilot tracking
- **Owner:** Inês Matos + Process Engineering
- **Dashboard:** Operations Review with quality trends per value stream
  - Average quality score by value stream
  - Criteria breakdown (which criteria are weakest?)
  - Trend: Quality improvement over quarters
  - Coaching priority: Teams/value streams needing support
- **Automation:** AI/Koda evaluation pipeline (Phase 2-3 implementation)

**Baseline:** To be established Q2 2026 during pilot phase

**Integration with Other Metrics:**
- **M3.5 (RCA Completion):** Completion tracked by M3.5, quality measured here
- **M3.8 (Improvement Rate):** Higher quality retrospectives should drive better improvements
- **M3.9 (Recurrence Prevention):** Better analysis should prevent repeat incidents

**Integration with Retrospective Transformation:**
- Directly implements AI/Koda-assisted auditing mentioned in transformation plan (Phase 2-3)
- Provides data for coaching and Brown Bag enablement sessions
- Tracks quality improvement through pilot and rollout phases
- Enables outcome-focused narrative shift measurement

**SMART Assessment:** ✓ SMART - Clear criteria (5-point rubric), measurable (average score), time-bound, achievable with AI/Koda tooling

---

### M3.7: Incident Detection Ratio (NEW - Retrospective Transformation)

**Metric:** % of incidents detected by proactive monitoring vs reactive customer reports

**Definition:** Detection ratio = (Proactively Detected Incidents / Total Incidents) × 100

**Target:** > 70% proactive detection by Q1 2027

**Rationale:**
- Explicitly mentioned in Operations Review evolution (retrospective transformation plan)
- Measures effectiveness of monitoring and SLO coverage
- Proactive detection = faster response, lower customer impact
- Retrospectives should drive monitoring improvements through action items
- Enables value stream-specific coaching on observability gaps

**Measurement Logic:**
- **Proactive Detection:** Incident detected by monitoring, alerts, SLO violations, internal testing BEFORE customer report
- **Reactive Detection:** Customer-reported incident (support case escalation, customer email, status page report) with NO prior alert/detection
- **Calculation:** `(Proactive Incidents / Total Incidents) × 100`

**Scope:**
- **Include:** All incidents (system-wide, localized, internal)
- **Detection source tracking:** First notification source determines detection method

**Implementation:**
- **Data Source:** Jira RDINC project
- **Collection Method:**
  - Add or use Jira field: "Detection Method" (dropdown: Proactive/Reactive)
  - Populate during incident triage (IC Leader or SRE)
  - Detection source examples:
    - **Proactive:** PagerDuty alert, Grafana alert, SLO violation, Synthetic monitoring, Internal QA testing
    - **Reactive:** Customer support case, Customer email, Twitter/social media, Status page customer report
  - Track per quarter: Count proactive vs reactive by value stream
  - Calculate detection ratio overall and per value stream
- **Frequency:** Monthly tracking, quarterly reporting
- **Owner:** Inês Matos + SRE
- **Dashboard:** Operations Review per value stream (analytics-driven)
  - Detection ratio trend by value stream
  - Comparison: Value streams with strong vs weak detection
  - Action item linkage: Did retrospective action items improve detection?
- **Automation:** Jira report filtering by detection method, automated calculation

**Baseline:** To be established Q1 2026 from historical RDINC data

**Integration with Other Metrics:**
- **M3.1 (Public MTTA):** Proactive detection enables faster customer communication
- **M3.5 (RCA Completion):** Retrospectives should include monitoring gaps analysis
- **M3.8 (Improvement Rate):** Action items targeting monitoring should improve detection ratio

**Integration with Retrospective Transformation:**
- Feeds Operations Review analytics mentioned in transformation plan
- Retrospective action items should improve this metric over time (measurable outcome)
- Enables value stream-specific coaching on monitoring gaps
- Validates SRE + team collaboration on observability improvements

**SMART Assessment:** ✓ SMART - Clear metric (%), measurable (proactive count), time-bound, relevant to observability goals

---

### M3.8: Retrospective-Driven Improvement Rate (NEW - Retrospective Transformation)

**Metric:** % of high-priority retrospective action items that demonstrate measurable improvement

**Definition:** Implementation rate for high-priority action items from retrospectives that result in measurable operational improvement within 90 days

**Target:** > 60% of high-priority action items show measurable improvement within 90 days by Q1 2027

**Rationale:**
- Closes the learning loop: Do retrospectives actually improve operations?
- Validates ROI of retrospective transformation investment
- Measures if team-led model drives accountability for action items
- Different from M3.2 (which measures on-time closure) - this measures actual impact
- Proves retrospectives aren't just documentation, they drive real change

**Measurement Logic:**
- Track high-priority action items from retrospectives
- After 90 days, assess: Did the action item result in measurable improvement?
- **Measurable improvement examples:**
  - **Incident recurrence reduced:** No similar incident in 90 days (tracked by M3.9)
  - **Detection improved:** Monitoring/alerting added, similar incidents now proactively detected (M3.7)
  - **MTTA improved:** Faster response to similar incident types (M3.1)
  - **Monitoring gap closed:** New SLO/alert created and operational
  - **Process improvement validated:** RFC/deployment process changed, measurable reduction in related incidents
- **Calculation:** `(Action Items with Demonstrated Improvement / High-Priority Action Items) × 100`

**Scope:**
- **Include:** High-priority action items only (Critical/High in Jira)
- **Evidence required:** Quantitative or qualitative evidence of improvement
- **Validation:** Process Engineering + Value Stream Leader review

**Implementation:**
- **Data Source:** Retrospective action items (Jira) + Incident data (RDINC)
- **Collection Method:**
  - Tag action items with expected outcome type (e.g., "Improve detection", "Prevent recurrence", "Reduce MTTA")
  - After 90 days: Review if outcome achieved
  - Evidence collection:
    - **No repeat incidents:** Query RDINC for similar failures in 90-day window
    - **Detection improved:** Verify new alert/SLO exists and triggered (if applicable)
    - **MTTA improved:** Compare response time for similar incidents
    - **Process change:** Verify RFC/process documentation updated and used
  - Quarterly assessment per value stream with validation
- **Frequency:** Quarterly measurement (90-day lagging window)
- **Owner:** Inês Matos
- **Dashboard:** Operations Review - "Action Item Impact" view
  - Improvement rate by value stream
  - Outcome type breakdown (which improvements are most common?)
  - High-impact examples (case studies for enablement)
- **Automation:** Semi-automated tracking with manual validation (pattern matching for recurrence, alert checks)

**Baseline:** To be established Q3 2026 (90 days after Q2 pilot retrospectives)

**Integration with Other Metrics:**
- **M3.2 (Action Item Closure):** M3.2 tracks on-time closure, M3.8 tracks actual impact
- **M3.7 (Detection Ratio):** Action items improving monitoring feed M3.7 improvement
- **M3.9 (Recurrence Prevention):** Primary evidence of improvement is no recurrence (M3.9)
- **M5.x (Process as Code):** Some action items may be automation candidates

**Integration with Retrospective Transformation:**
- Validates team-led retrospectives drive real operational improvements
- Feeds Operations Review discussion per value stream (data-driven coaching)
- Provides case studies for Brown Bag enablement sessions
- Proves ROI of transformation investment

**SMART Assessment:** ✓ SMART - Clear outcome (measurable improvement), quantifiable (%), time-bound (90 days), achievable with evidence tracking

---

### M3.9: Incident Recurrence Prevention Rate (NEW - Retrospective Transformation)

**Metric:** % of incidents where similar failure pattern doesn't repeat within 180 days after retrospective

**Definition:** Effectiveness of retrospectives in preventing repeat incidents of same root cause category

**Target:** < 15% recurrence rate by Q1 2027 (inverse metric - lower is better)

**Rationale:**
- Ultimate measure of retrospective effectiveness: Do we learn from failures?
- Validates team-led model prevents repeat mistakes
- Enables pattern identification across value streams (systemic issues)
- Directly measures learning loop closure
- Proves retrospectives aren't theater - they prevent future incidents

**Measurement Logic:**
- For each incident with completed retrospective, track if similar incident occurs within 180 days
- **Similar incident defined as:**
  - **Same root cause category** (e.g., "Configuration Error", "Deployment Failure", "Capacity Issue", "Dependency Failure")
  - AND **Same asset/service** OR **Same failure mode**
- **Recurrence:** Binary Yes/No flag if similar incident found in 180-day window
- **Calculation:** `(Incidents with Recurrence / Total Retrospectives Completed) × 100`

**Scope:**
- **Include:** All completed retrospectives with defined root cause
- **Exclude:** Retrospectives where root cause is "Unknown" or "External dependency" (outside team control)
- **Validation:** Pattern matching algorithm + manual spot-check

**Implementation:**
- **Data Source:** Retrospective tracker + RDINC incident database
- **Collection Method:**
  - Tag retrospectives with root cause pattern (structured taxonomy)
    - Examples: "Config error - Platform Server Hub", "Deployment failure - LifeTime", "Capacity - Database CPU", "Network - Load Balancer"
  - Root cause taxonomy to be defined in Phase 1 (Inês + SRE)
  - Monitor subsequent incidents within 180-day window after retrospective approval
  - Pattern matching algorithm:
    - Query RDINC for incidents matching: Same root cause category + (Same asset OR Same failure symptoms)
  - Flag recurrence if pattern match found
  - Manual validation: 20% sample to validate algorithm accuracy
  - Quarterly analysis per value stream
- **Frequency:** Quarterly measurement (180-day rolling window)
- **Owner:** Inês Matos + SRE (pattern matching and taxonomy)
- **Dashboard:** Operations Review - "Repeat Incident Tracking"
  - Recurrence rate by value stream
  - Most common repeat patterns (systemic issues requiring cross-team attention)
  - Success stories: Retrospectives that prevented recurrence
- **Automation:** Pattern matching algorithm (semi-automated with manual validation), Jira query for similar incidents

**Baseline:** To be established Q3 2026 (180 days after Q1 retrospectives)

**Integration with Other Metrics:**
- **M3.5 (RCA Completion):** Can only measure recurrence if retrospective completed
- **M3.6 (RCA Quality):** Higher quality RCA should correlate with lower recurrence
- **M3.8 (Improvement Rate):** Primary evidence of improvement is no recurrence
- **M2.5 (CFR Correlation):** Change-related incidents link to change management patterns

**Integration with Retrospective Transformation:**
- Validates retrospectives prevent repeat failures (ultimate success measure)
- Highlights value streams needing additional coaching or systemic interventions
- Identifies recurring patterns requiring cross-team solutions
- Proves learning loop is closed: Analysis → Action → Prevention

**Validation Checks:**
- **Q3 2026:** Validate root cause taxonomy with 50 sample retrospectives
- **Quarterly:** False positive/negative analysis (sample 20 flagged recurrences)
- **Quarterly:** Pattern matching accuracy (algorithm vs manual validation)

**SMART Assessment:** ✓ SMART - Clear outcome (no recurrence), measurable (%), time-bound (180 days), achievable with pattern matching

---

## Method 4: Strategic Metrics Orchestration

### M4.1: Executive Metric Literacy ✓ SMART

**Metric:** % of Leadership/End-Users who can correctly interpret calculation logic and navigate dashboards

**Definition:** Comprehension rate from quarterly literacy assessments

**Target:** > 85% by Q1 2027

**Measurement Logic:** Quarterly "Pulse" survey or quiz following training sessions

**Implementation:**
- **Data Source:** Training survey/quiz results (post-training assessment)
- **Collection Method:**
  - After each training session: Administer 5-10 question quiz on KPI interpretation
  - Questions cover: Calculation logic, threshold interpretation, dashboard navigation
  - Pass criteria: ≥ 80% correct answers
  - Aggregate: % of participants passing assessment
- **Frequency:** Quarterly (after each training cycle)
- **Owner:** Paulo Alves Monteiro
- **Dashboard:** Training registry spreadsheet or LMS results
- **Automation:** Survey tool (Forms, SurveyMonkey) to auto-calculate pass rate

**SMART Assessment:** ✓ Complete - Clear assessment method, measurable, target defined

**Refinement Suggestion:** Track by audience segment (Leadership vs End-Users) to identify gaps

---

### M4.2: Documentation Lineage Coverage ✓ SMART

**Metric:** % of CPTO metrics with full technical and functional lineage documentation

**Definition:** Coverage rate of data lineage and calculation maps in Metrics Library

**Target:** 100% by end of Q2 2026

**Measurement Logic:** Audit Metrics Library to ensure every live KPI has lineage documentation

**Implementation:**
- **Data Source:** Metrics Registry (Confluence or dedicated repository)
- **Collection Method:**
  - Maintain list of all live CPTO KPIs
  - For each KPI, verify existence of:
    - Technical lineage (data sources, transformations, DAX logic)
    - Functional documentation (business definition, calculation steps, thresholds)
  - Calculation: `(KPIs with Full Documentation / Total Live KPIs) * 100`
- **Frequency:** Monthly audit during Q1-Q2, quarterly maintenance after
- **Owner:** Paulo Alves Monteiro
- **Dashboard:** Metrics Registry with "Documentation Status" column (Complete/Incomplete)
- **Automation:** Checklist template for each KPI in Confluence

**SMART Assessment:** ✓ Complete - Binary check (documented or not), clear target (100%)

**Refinement Suggestion:** Define documentation template/standard to ensure consistency

---

## Method 5: AI-Enabled Organizational Capability

**Note:** Method 5 restructured to include three pillars: Individual AI Enablement, Career Development & Progression, and Process Industrialization

### M5.1a: AI Adoption Rate ✓ SMART

**Metric:** % of team actively using AI tools weekly in their daily workflows

**Definition:** Track weekly active usage of AI tools (Claude Code, ChatGPT, AI @ Product, etc.) by team members for work tasks

**Target:** 80%+ of team actively using AI tools weekly by Q1 2027

**Rationale:**
- AI enablement starts with adoption - tools must be used to deliver value
- Weekly usage indicates AI is integrated into daily workflows, not just experimentation
- 80% threshold accounts for learning curves and role variations
- Leading indicator for time savings and effectiveness gains

**Measurement Logic:**
- **Active Usage:** Team member uses AI tools at least 1x per week for work tasks
- **Work Tasks:** Documentation, analysis, meeting prep, problem-solving, code review, reporting
- **Calculation:** `(Team Members Using AI Weekly / Total Team Members) × 100`

**Implementation:**
- **Data Source:** Self-reported usage tracking + tool usage logs (where available)
- **Collection Method:**
  - Weekly pulse check: "Did you use AI tools for work this week? (Yes/No)"
  - Monthly survey: "Which AI tools did you use and for what?"
  - Supplemental: Claude Code usage logs, AI @ Product platform analytics
  - Track adoption trend over time
- **Frequency:** Weekly pulse, monthly deep-dive
- **Owner:** Vera Branco
- **Dashboard:** AI Adoption Tracker (Confluence or simple spreadsheet)
  - Weekly adoption rate trend
  - Most common use cases
  - Adoption by role/level

**Baseline:** To be established Q2 2026 (start of V2MOM execution)

**Expected Trend:**
- Q2 2026: 40-50% adoption (post-training ramp-up)
- Q3 2026: 60-70% adoption (workflow integration phase)
- Q4 2026: 80%+ adoption (target achieved)

**Integration with Other Metrics:**
- **M5.1b (Workflow Augmentation):** High adoption enables workflow documentation
- **M5.1c (Time Savings):** Adoption is prerequisite for measurable time savings
- **M5.3 (Process Industrialization):** Team AI literacy enables skill development

**SMART Assessment:** ✓ SMART - Clear metric (%), measurable via tracking, target defined (80%), achievable with training, relevant to AI enablement, time-bound (Q1 2027)

---

### M5.1b: AI-Augmented Workflow Documentation ✓ SMART

**Metric:** Number of core team workflows with documented AI augmentation patterns

**Definition:** Count of PE team workflows that have documented, repeatable AI usage patterns for improved efficiency or quality

**Target:** 5+ documented AI-augmented workflows by Q1 2027

**Rationale:**
- Individual AI adoption is step 1; repeatable, documented patterns are step 2
- Documented workflows enable knowledge sharing and onboarding
- Focuses AI usage on high-impact, repeatable activities
- Creates team AI playbook for sustained capability

**Measurement Logic:**
- **Core Workflows:** Meeting prep, incident analysis, RFC review, documentation writing, reporting, retrospective prep, trend analysis, CAB prep
- **Documented Pattern:** Includes workflow description, AI tool(s) used, prompts/techniques, time saved, quality improvement, usage examples
- **Minimum Quality Bar:** Pattern must be reusable by others (tested by at least 2 team members)

**Implementation:**
- **Data Source:** Team AI Playbook (Confluence)
- **Collection Method:**
  - Q2 2026: Identify candidate workflows for AI augmentation
  - Q2-Q3 2026: Team experiments with AI for these workflows
  - Q3-Q4 2026: Document proven patterns in team playbook
  - Q1 2027: Review and finalize playbook
  - Each pattern includes: workflow name, use case, AI tool, prompt template, before/after example, team feedback
- **Frequency:** Quarterly review
- **Owner:** Vera Branco (team contributions)
- **Dashboard:** Confluence AI Playbook with pattern count and usage

**Baseline:** 0 documented patterns (Q2 2026)

**Example Patterns:**
- **1:1 Meeting Prep:** Use Claude Code /prep1o1 skill to pull context
- **Incident Pattern Analysis:** Use ChatGPT to identify trends in last 30 incidents
- **CAB Prep Automation:** Use AI @ Product skill to pre-screen RFCs
- **Documentation Updates:** Use Claude Code to update process docs from meeting notes
- **Executive Reporting:** Use AI to generate executive summaries from raw data

**Integration with Other Metrics:**
- **M5.1a (AI Adoption):** Documented patterns drive adoption by lowering barrier to AI use
- **M5.1c (Time Savings):** Patterns enable measurement of consistent time savings
- **M5.3 (Process Industrialization):** Patterns inform automation blueprint priorities

**SMART Assessment:** ✓ SMART - Clear deliverable (documented pattern), measurable (count), target defined (5+), achievable, relevant to AI capability building, time-bound (Q1 2027)

---

### M5.1c: Time Savings Through AI Augmentation ✓ SMART

**Metric:** Estimated hours saved per person per week through AI tool usage

**Definition:** Average time saved by team members using AI for work tasks, measured through self-reporting and pattern analysis

**Target:** 2-4 hours/week/person saved by Q1 2027

**Rationale:**
- Time savings validate AI investment and justify continued enablement
- 2-4 hours/week = 10-20% productivity gain (meaningful but achievable)
- Focus on time saved (not just tasks completed faster) to capture quality improvements
- Creates business case for AI enablement investment

**Measurement Logic:**
- **Time Saved:** Difference between pre-AI and post-AI task completion time
- **Scope:** Time saved on tasks where AI was used (not total capacity)
- **Calculation:** Average across all team members who use AI weekly

**Implementation:**
- **Data Source:** Monthly self-reported survey + pattern-based estimates
- **Collection Method:**
  - **Self-Report (Primary):** Monthly survey: "Estimate hours saved this month using AI tools" → Calculate weekly average
  - **Pattern-Based (Supplemental):** For documented workflows, estimate time saved per usage → Aggregate across team
  - **Validation:** Quarterly calibration discussion with team (sanity check estimates)
- **Frequency:** Monthly measurement, quarterly reporting
- **Owner:** Vera Branco
- **Dashboard:** Time Savings Tracker
  - Average weekly time saved per person
  - Time saved by workflow type
  - Trend over V2MOM period

**Baseline:** 0 hours/week saved (Q2 2026 - before AI training)

**Expected Trend:**
- Q2 2026: 0-1 hour/week (training phase, minimal usage)
- Q3 2026: 1-2 hours/week (workflow integration, early patterns)
- Q4 2026: 2-3 hours/week (mature usage, documented patterns)
- Q1 2027: 3-4 hours/week (target achieved, team AI playbook mature)

**Breakdown by Activity (Estimated):**
- Meeting prep: 30-60 min/week
- Documentation writing: 30-60 min/week
- Analysis and reporting: 30-60 min/week
- Incident/RFC review: 30-60 min/week
- Misc (problem-solving, learning): 30-60 min/week

**Limitations & Mitigations:**
- **Limitation:** Self-reported estimates may be biased
- **Mitigation:** Use pattern-based estimates as cross-check; quarterly calibration discussions
- **Limitation:** Hard to measure quality improvements (only time)
- **Mitigation:** Supplemental qualitative feedback on quality gains

**Integration with Other Metrics:**
- **M5.1a (AI Adoption):** Adoption prerequisite for time savings
- **M5.1b (Workflow Augmentation):** Documented patterns enable consistent time savings
- **M6.1 (Operational Capacity):** Time savings should reduce M6 operational capacity consumption

**SMART Assessment:** ✓ SMART - Clear metric (hours/week), measurable via survey, target defined (2-4h), achievable, relevant to productivity gains, time-bound (Q1 2027)

---

### M5.2a: Career Framework Completion ✓ SMART

**Metric:** Business Process Analyst career framework documented and published

**Definition:** Complete competency model for Associate → Analyst → Senior → Principal levels with advancement criteria

**Target:** Career framework documented and published by Q3 2026

**Rationale:**
- Career clarity is foundational to development planning and retention
- AI is redefining the Business Process Analyst role - must codify expectations
- Framework enables transparent career conversations with direct reports
- Creates organizational capability asset beyond individual development

**Measurement Logic:** Binary deliverable - framework exists and is published

**Scope - Career Framework Components:**

1. **Role Levels Defined:**
   - Associate Business Process Analyst (0-2 years)
   - Business Process Analyst (2-4 years)
   - Senior Business Process Analyst (4-7 years)
   - Principal Business Process Analyst (7+ years)

2. **Competency Dimensions:**
   - Process Expertise (frameworks, governance, audit)
   - Technical Capabilities (tools, automation, data analysis)
   - AI Capabilities (AI tool usage, automation design, AI strategy)
   - Stakeholder Management (communication, influence, partnership)
   - Strategic Thinking (pattern recognition, systems thinking, organizational impact)

3. **Advancement Criteria:**
   - Expected competencies for each level
   - Demonstration criteria (how to show competency)
   - Typical time in level
   - Advancement decision process

4. **Career Paths:**
   - Individual contributor progression
   - Potential lateral moves (if applicable)
   - Skills development roadmap by level

**Success Criteria:**
- Framework documented in Confluence
- Reviewed and approved by Arul Livingston (VP)
- Socialized with direct reports
- Used in individual development plan creation

**Implementation:**
- **Data Source:** Career Framework Confluence page
- **Collection Method:**
  - Q2 2026: Draft framework with competency model
  - Q2 2026: Socialize with direct reports for feedback
  - Q3 2026: Finalize and get VP approval
  - Q3 2026: Publish to Confluence and share with team
- **Frequency:** One-time deliverable (Q3 2026)
- **Owner:** Vera Branco
- **Dashboard:** N/A (one-time deliverable)

**Baseline:** No formal career framework exists for Business Process Analysts (Q1 2026)

**Integration with Other Metrics:**
- **M5.2b (Development Plan Execution):** Framework informs individual development plans
- **M5.2c (Career Progression):** Framework defines advancement criteria
- **M5.2d (Retention):** Career clarity supports retention

**SMART Assessment:** ✓ SMART - Clear deliverable (framework), measurable (binary), target date (Q3 2026), achievable, relevant to career development

---

### M5.2b: Individual Development Plan Execution ✓ SMART

**Metric:** % of planned development actions completed quarterly per individual development plan

**Definition:** Completion rate of quarterly development milestones for each direct report

**Target:** 80%+ completion rate on quarterly development actions (measured per quarter)

**Rationale:**
- Career frameworks are meaningless without execution
- Quarterly milestones create accountability and momentum
- 80% allows for flexibility (priorities shift, unexpected work) while maintaining progress
- Measures both team commitment (Vera's coaching) and individual commitment

**Measurement Logic:**
- **Development Action:** Specific, time-bound activity to build competency (e.g., "Complete AI @ Product training", "Lead retrospective transformation pilot", "Present at brown bag")
- **Quarterly Plan:** 3-5 development actions per person per quarter
- **Completion:** Action finished within quarter or substantive progress made
- **Calculation:** `(Completed Actions / Total Planned Actions) × 100` per quarter

**Implementation:**
- **Data Source:** Individual Development Plan tracker (Confluence or spreadsheet)
- **Collection Method:**
  - Q2 2026: Create individual development plans for each direct report
  - Each plan includes: Current level, target level, quarterly milestones
  - Quarterly check-ins (1:1s) to review progress
  - Track status: Not Started, In Progress, Completed, Blocked
  - Calculate quarterly completion rate
- **Frequency:** Quarterly measurement
- **Owner:** Vera Branco (individual ownership with direct reports)
- **Dashboard:** Development Plan Tracker per person
  - Quarterly completion rate by person
  - Development action status
  - Trends over V2MOM period

**Baseline:** 0% (no development plans exist before Q2 2026)

**Expected Trend:**
- Q2 2026: N/A (plans being created)
- Q3 2026: 70-80% (initial execution, learning curve)
- Q4 2026: 80-85% (rhythm established)
- Q1 2027: 80-90% (sustained execution)

**Example Development Actions:**
- Complete AI literacy training (Q2 2026)
- Document 2 AI-augmented workflow patterns (Q3 2026)
- Lead career framework socialization session with team (Q3 2026)
- Complete AI @ Product platform certification (Q4 2026)
- Present retrospective transformation progress at staff meeting (Q4 2026)
- Deliver 1 process automation blueprint (Q1 2027)

**Integration with Other Metrics:**
- **M5.2a (Career Framework):** Framework informs development action planning
- **M5.2c (Career Progression):** Consistent execution enables career advancement
- **M5.1/M5.3:** Development actions often tied to AI enablement or process industrialization work

**SMART Assessment:** ✓ SMART - Clear metric (%), measurable per quarter, target defined (80%), achievable, relevant to career development, time-bound (quarterly)

---

### M5.2c: Career Progression Rate ✓ SMART

**Metric:** Number of team members advancing to next career level during V2MOM period

**Definition:** Count of team members who advance one level in career framework (e.g., Analyst → Senior Analyst)

**Target:** At least 1 team member advances to next career level by Q1 2027

**Rationale:**
- Career development must result in tangible advancement, not just plans
- Proves career framework is actionable, not theoretical
- Demonstrates Vera's effectiveness as people manager
- Creates positive signal for team retention and motivation

**Measurement Logic:**
- **Advancement:** Formal promotion or level change based on career framework criteria
- **Scope:** Within Process Engineering team (direct reports)
- **Criteria:** Demonstrated competencies at next level per career framework

**Implementation:**
- **Data Source:** Career level tracking + promotion records
- **Collection Method:**
  - Q2 2026: Assess current levels for each team member
  - Q3-Q4 2026: Execute development plans, assign stretch work
  - Q4 2026 or Q1 2027: Conduct advancement reviews
  - Advancement criteria: Demonstrated competencies (per M5.2a framework), manager recommendation, VP approval
- **Frequency:** Assessed at end of V2MOM period (Q1 2027)
- **Owner:** Vera Branco (with VP approval)
- **Dashboard:** Career level tracker per person

**Baseline:** Current career levels as of Q2 2026

**Target Breakdown:**
- **Minimum (Target):** 1 advancement by Q1 2027
- **Stretch:** 2 advancements by Q1 2027

**Advancement Decision Factors:**
- Competency demonstration per career framework (M5.2a)
- Development plan execution (M5.2b)
- Business impact and stakeholder feedback
- Readiness for next level responsibilities
- Budget and headcount availability

**Limitations & Mitigations:**
- **Limitation:** Advancement may be blocked by budget/headcount constraints
- **Mitigation:** Focus on competency development regardless; explore lateral moves if vertical blocked
- **Limitation:** 1-year timeframe may be short for advancement
- **Mitigation:** Target individuals already near advancement threshold

**Integration with Other Metrics:**
- **M5.2a (Career Framework):** Framework defines advancement criteria
- **M5.2b (Development Plans):** Execution prerequisite for advancement
- **M5.2d (Retention):** Career advancement opportunity supports retention

**SMART Assessment:** ✓ SMART - Clear metric (count), measurable, target defined (1+), achievable (1-year focus), relevant to career development, time-bound (Q1 2027)

---

### M5.2d: Team Retention Rate ✓ SMART

**Metric:** % of team retained year-over-year (voluntary attrition rate)

**Definition:** Percentage of team members who remain on the team from start to end of V2MOM period

**Target:** > 90% retention (voluntary attrition < 10%)

**Rationale:**
- Career development and AI enablement are retention investments
- High attrition undermines organizational capability building
- Retention validates effectiveness of M5 career development pillar
- Industry benchmark: ~15% voluntary attrition for tech roles; < 10% is strong performance

**Measurement Logic:**
- **Retention Rate:** `(Team Members at End / Team Members at Start) × 100`
- **Voluntary Attrition:** Resignations initiated by employee (not layoffs, role eliminations)
- **Scope:** Direct reports on Process Engineering team

**Implementation:**
- **Data Source:** HR records + team roster
- **Collection Method:**
  - Q2 2026: Baseline team count
  - Q1 2027: Final team count
  - Track voluntary departures during V2MOM period
  - Calculate retention rate at V2MOM end
  - Supplemental: Conduct exit interviews to understand reasons
- **Frequency:** Measured at V2MOM end (Q1 2027)
- **Owner:** Vera Branco
- **Dashboard:** Retention tracker with trend over time

**Baseline:** 100% retention as of Q2 2026 (starting point)

**Target:**
- **Target:** > 90% retention (0-1 departure acceptable for team of ~10)
- **Stretch:** 100% retention (no voluntary departures)

**Risk Factors:**
- Competing offers with higher compensation
- Lack of career advancement opportunities
- Poor manager relationship
- Burnout or work-life balance issues
- Organizational changes or uncertainty

**Retention Drivers (M5 Focus):**
- Career framework provides clear path (M5.2a)
- Individual development plans show investment (M5.2b)
- Career advancement opportunities (M5.2c)
- AI enablement increases job satisfaction and marketability (M5.1)

**Integration with Other Metrics:**
- **M5.2a-c (Career Development):** Career clarity, development, and advancement support retention
- **M5.1 (AI Enablement):** AI skills increase engagement and market value (but also flight risk if over-invested)
- **M6.1 (Operational Capacity):** Sustainable capacity allocation prevents burnout

**SMART Assessment:** ✓ SMART - Clear metric (%), measurable via HR data, target defined (> 90%), relevant to organizational capability, time-bound (Q1 2027)

---

### M5.3a: Process as Code Blueprint Readiness ✓ SMART

**Metric:** Number of validated Process as Code blueprints completed for high-impact automation candidates

**Definition:** Count of technical blueprints ready for implementation, covering process scope, inputs, logic, outputs, and integration requirements

**Target:** 3-5 validated blueprints by Q1 2027

**Rationale:**
- Blueprints are the bridge between strategy (automation vision) and execution (skill development)
- 3-5 blueprints = focused scope, achievable in V2MOM timeframe
- Blueprint validation with stakeholders ensures Engineering buy-in before development
- Creates ready-to-code backlog for post-V2MOM execution (Q2 2027+)

**Measurement Logic:**
- **Blueprint:** Technical design document for a Process as Code automation
- **Validated:** Reviewed and approved by Engineering stakeholders
- **Blueprint Components:** Process scope, inputs, logic/decision rules, outputs, integration requirements, success criteria

**Scope - Automation Candidates:**
- Change Management (RFC validation, routing, compliance checks)
- Incident Response (triage support, retrospective prep, pattern analysis)
- Problem Management (trend analysis, action item tracking)
- Operational governance (CAB prep, reporting, evidence collection)

**Blueprint Quality Criteria:**
- Clear process scope and workflow to be automated
- Defined inputs (data sources, triggers, user inputs)
- Documented logic (decision rules, validations, routing)
- Specified outputs (actions, notifications, artifacts)
- Integration requirements identified (Jira, Confluence, Slack, APIs)
- Success criteria and measurement defined
- Validated with at least 1 Engineering team

**Implementation:**
- **Data Source:** Blueprint Repository (Confluence)
- **Collection Method:**
  - Q2 2026: Discovery and prioritization of automation candidates
  - Q2-Q3 2026: Draft blueprints for top 3-5 candidates
  - Q3-Q4 2026: Validate blueprints with Engineering stakeholders
  - Q4 2026: Finalize and publish validated blueprints
  - Track blueprint status: Candidate Identified, Draft, Under Review, Validated
- **Frequency:** Quarterly tracking
- **Owner:** TBD (Technical Lead for Process Automation)
- **Dashboard:** Blueprint Tracker (Confluence)
  - Blueprint count by status
  - Validation status by Engineering stakeholder

**Baseline:** 0 blueprints (Q1 2026)

**Expected Trend:**
- Q2 2026: 3-5 candidates identified, 1-2 blueprints drafted
- Q3 2026: 3-4 blueprints drafted, 1-2 validated
- Q4 2026: 3-5 blueprints validated (target achieved)

**Integration with Other Metrics:**
- **M5.3b (Pilot Skill Deployment):** Pilot skill informs blueprint approach
- **M5.3c (Backlog Readiness):** Blueprints converted to technical backlogs
- **M5.1b (Workflow Augmentation):** Team AI workflow patterns inform automation priorities

**SMART Assessment:** ✓ SMART - Clear deliverable (blueprint), measurable (count), target defined (3-5), achievable, relevant to automation, time-bound (Q1 2027)

---

### M5.3b: Pilot Skill Deployment ✓ SMART

**Metric:** Number of pilot skills successfully deployed to production and actively used by Engineering teams

**Definition:** Count of process execution skills built on AI @ Product platform, deployed to production, and demonstrating Engineering team adoption

**Target:** At least 1 pilot skill deployed and operational by Q1 2027

**Rationale:**
- Validates team can build and ship AI @ Product skills to production
- Proves Engineering teams will adopt PE automation (demand signal)
- De-risks M5.3 execution by demonstrating capability early
- Creates blueprint template for future skills (informs M5.3a blueprints)
- Shifts from theory (training) to reality (production delivery)

**Measurement Logic:**
- **Pilot Skill:** Process execution skill built on AI @ Product platform
- **Deployed:** Skill available in production environment (not dev/test)
- **Active Usage:** At least 1 Engineering team using skill regularly (usage tracked)

**Scope - Eligible Process Workflows:**
- Incident Response (triage, RCA generation, post-mortem drafting)
- Change Management (RFC creation/validation, risk assessment)
- Problem Management (root cause analysis support, trend analysis)
- Compliance (FedRAMP evidence collection, control validation)

**Success Criteria:**
- Skill deployed to AI @ Product production environment
- Skill addresses PE-owned process executed by Engineering teams
- At least 1 Engineering team using skill (usage examples documented)
- Measurable value delivered (time saved, quality improved, compliance increased)
- Engineering team feedback collected

**Implementation:**
- **Data Source:** AI @ Product platform registry + usage logs + Engineering feedback
- **Collection Method:**
  - Q2 2026: Identify pilot skill candidate with Engineering team input
  - Q2-Q3 2026: Build, test, iterate with Engineering team
  - Q3-Q4 2026: Deploy to production
  - Q4 2026: Track usage and collect feedback
  - Track: Skill name, process addressed, deployment date, Engineering teams using, usage count, value delivered
- **Frequency:** Quarterly tracking
- **Owner:** TBD (Technical Lead for Process Automation)
- **Dashboard:** Pilot Skill Tracker (Confluence)
  - Deployment status
  - Usage metrics
  - Engineering feedback

**Baseline:** 0 PE skills deployed to production (Q1 2026)

**Risk Mitigation:**
- Start with narrow scope (single workflow, clear boundaries)
- Prioritize quick win over complex automation
- Budget 8-12 weeks for learning curve and iteration
- Partner with friendly Engineering team for co-development
- Accept "good enough" v1.0 - iterate based on feedback

**Integration with Other Metrics:**
- **M5.3a (Blueprint Readiness):** Pilot skill creates blueprint template
- **M5.3c (Backlog Readiness):** Pilot skill may become first item in backlog
- **M5.3d (Technical Capability):** Pilot skill proves team technical capability

**SMART Assessment:** ✓ SMART - Clear deliverable (pilot skill), measurable (binary + usage), target defined (1+), achievable, relevant to industrialization, time-bound (Q1 2027)

---

### M5.3c: Post-V2MOM Backlog Readiness ✓ SMART

**Metric:** % of Process as Code blueprints translated into ready-to-code technical backlogs for post-V2MOM execution

**Definition:** Completion rate of technical user stories and acceptance criteria for validated blueprints, ready for development in Q2 2027+

**Target:** 100% of validated blueprints (M5.3a) translated to technical backlogs by Q1 2027

**Rationale:**
- V2MOM focuses on blueprints and pilot; post-V2MOM is scale execution
- Backlog readiness ensures no delay when scaling automation in Q2 2027+
- Technical translation is critical: blueprint = what to build, backlog = how to build
- Demonstrates full Process as Code capability: discover → design (blueprint) → translate (backlog) → build (post-V2MOM)

**Measurement Logic:**
- **Technical Backlog:** Collection of user stories and acceptance criteria for a blueprint
- **Ready-to-Code:** Stories have clear scope, acceptance criteria, dependencies identified, effort estimated
- **Calculation:** `(Blueprints with Backlogs / Total Validated Blueprints) × 100`

**Backlog Components (per Blueprint):**
- User stories with clear scope
- Acceptance criteria for each story
- Technical dependencies identified
- Integration requirements detailed
- Effort estimates (story points or time)
- Priority and sequence defined
- Success metrics and testing approach

**Implementation:**
- **Data Source:** Technical Backlog Repository (Jira or Confluence)
- **Collection Method:**
  - Q3-Q4 2026: As blueprints are validated (M5.3a), begin backlog translation
  - Q4 2026 - Q1 2027: Complete backlog translation for all validated blueprints
  - Each backlog includes: User stories, acceptance criteria, dependencies, estimates
  - Track backlog status: Not Started, In Progress, Complete
  - Q1 2027: Review and finalize all backlogs for post-V2MOM execution
- **Frequency:** Quarterly tracking
- **Owner:** TBD (Technical Lead for Process Automation)
- **Dashboard:** Backlog Readiness Tracker
  - % of blueprints with ready-to-code backlogs
  - Total user stories ready for Q2 2027+ execution
  - Estimated effort for post-V2MOM automation delivery

**Baseline:** 0% backlog readiness (Q2 2026)

**Expected Trend:**
- Q2 2026: 0% (discovery phase)
- Q3 2026: 20-40% (early blueprints being translated)
- Q4 2026: 60-80% (most blueprints translated)
- Q1 2027: 100% (all validated blueprints ready for execution)

**Integration with Other Metrics:**
- **M5.3a (Blueprint Readiness):** Backlog translation follows blueprint validation
- **M5.3b (Pilot Skill):** Pilot skill experience informs backlog creation approach
- **M5.3d (Technical Capability):** Team technical skills enable backlog creation

**SMART Assessment:** ✓ SMART - Clear metric (%), measurable, target defined (100%), achievable, relevant to scaling automation, time-bound (Q1 2027)

---

### M5.3d: Technical Platform Capability ✓ SMART

**Metric:** Number of team members certified on AI @ Product platform capabilities

**Definition:** Count of team members who have completed AI @ Product platform training and demonstrated capability through skill deployment

**Target:** 2-3 team members certified on AI @ Product platform by Q1 2027

**Rationale:**
- Core technical team needed to deliver M5.3 automation objectives
- 2-3 certified members = sustainable capability without single point of failure
- Certification = training + demonstrated capability (not just course completion)
- Builds organizational capability beyond V2MOM period

**Measurement Logic:**
- **Certified:** Completed AI @ Product platform training AND deployed at least 1 skill to production (or contributed significantly to pilot skill)
- **Platform Capabilities:** Skills framework, MCP architecture, agent design, integration patterns, deployment processes

**Certification Criteria:**
- Completed AI @ Product platform training (if formal training exists)
- Demonstrated practical capability:
  - Deployed skill to production (solo or lead contributor), OR
  - Significant contribution to pilot skill (M5.3b), OR
  - Built and tested skill in dev environment (ready for production)
- Understands Skills framework, MCP architecture, integration patterns

**Implementation:**
- **Data Source:** Training records + skill deployment tracking
- **Collection Method:**
  - Q2-Q3 2026: Identify core technical team members for AI @ Product focus
  - Q2-Q4 2026: Provide AI @ Product training and hands-on skill development opportunities
  - Q3-Q4 2026: Team members deploy skills or contribute to pilot
  - Q1 2027: Assess certification based on training + demonstrated capability
  - Track: Team member, training completion date, skill deployment/contribution
- **Frequency:** Quarterly tracking
- **Owner:** Vera Branco (with Technical Lead)
- **Dashboard:** Technical Capability Tracker
  - Team members certified
  - Training completion status
  - Skill deployment contributions

**Baseline:** 0 team members certified (Q1 2026)

**Expected Progression:**
- Q2 2026: 1-2 members start AI @ Product training
- Q3 2026: 1-2 members certified (via pilot skill work)
- Q4 2026: 2 members certified
- Q1 2027: 2-3 members certified (target achieved)

**Integration with Other Metrics:**
- **M5.3b (Pilot Skill):** Pilot skill deployment is certification pathway
- **M5.3a/c (Blueprints/Backlog):** Certified team members create technical blueprints and backlogs
- **M5.1 (AI Enablement):** Platform capability builds on general AI literacy

**SMART Assessment:** ✓ SMART - Clear metric (count), measurable, target defined (2-3), achievable, relevant to technical capability, time-bound (Q1 2027)

---



## Method 6: Operational Excellence & Sustainability

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

**Implementation:**
- **Data Source:** Jira story points by epic
- **Collection Method:**
  - Query completed issues per quarter grouped by epic/method
  - JQL examples:
    ```jql
    # M6 BAU story points
    project = PE AND "Epic Link" IN (M6.1_epic, M6.2_epic, M6.3_epic, M6.4_epic, M6.5_epic)
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
  - Primary: Operational % vs Transformation % by quarter (target: ~30% Operational, ~70% Transformation)
  - Breakdown: Story points by submethod (6.1-6.5) and method (M1-M5)
  - Trend: Quarter-over-quarter capacity shift
  - Jira gadget: "Story Points by Epic" stacked bar chart

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

### M6.2: CAB Orchestration Effectiveness (Submethod 6.1)

**Metric:** CAB operational efficiency measured by preparation time, meeting duration, and decision quality

**Definition:** Track CAB effectiveness to ensure governance doesn't become capacity bottleneck

**Target:**
- Average CAB prep time < 4 hours per meeting (Q4 2026)
- Average CAB duration ≤ 60 minutes (Q4 2026)
- RFC first-pass approval rate > 85% (Q4 2026)

**Rationale:**
- CAB is monthly recurring event (10-15% of team capacity including prep and follow-up)
- Inefficient CAB preparation/execution consumes excessive capacity
- High first-pass approval indicates good pre-meeting RFC quality
- Shorter meetings with maintained quality = efficient governance

**Measurement Logic:**

**M6.2a: CAB Prep Time**
- Track: Time spent preparing for monthly CAB (RFC pre-review, agenda creation, material prep)
- Target: < 4 hours per CAB session
- Measurement: Manual time logging or Jira worklog

**M6.2b: CAB Duration**
- Track: Actual meeting duration (start to end)
- Target: ≤ 60 minutes per CAB session
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
  - CAB facilitator logs prep time and meeting duration monthly (Confluence CAB log or Jira)
  - Jira: Track RFCs by review outcome (Approved First Time, Needs Rework, Rejected)
  - Quarterly aggregate and trend analysis
- **Frequency:** Monthly tracking, quarterly reporting
- **Owner:** Laura Ferreira (CAB facilitator)
- **Dashboard:** CAB Efficiency Dashboard
  - Prep time trend by month/quarter (target line at 4 hours)
  - Meeting duration trend (target line at 60 min)
  - First-pass approval rate trend (target line at 85%)
  - Capacity impact: Total monthly CAB hours (prep + meeting) trend

**Baseline:** To be established Q1 2026 from historical CAB data (if available)

**Integration with Other Metrics:**
- **M2.3 (RFC Rejection Velocity):** Faster pre-CAB rejection improves first-pass approval rate
- **M2.4 (Manual Resilience):** Automating repetitive changes reduces CAB RFC volume
- **M2.1 (Change Lead Time):** Efficient CAB reduces RFC processing time
- **M3 (Incident Response):** High-stake retrospective coordination feeds M3 metrics

**SMART Assessment:** ✓ SMART - Multiple clear metrics (time, %), measurable, targets defined, relevant to capacity optimization

---

### M6.3: Audit Request Fulfillment Rate (Submethod 6.2)

**Metric:** % of audit evidence and compliance requests fulfilled within agreed deadline

**Definition:** Track on-time delivery of audit-related requests to ensure compliance obligations are met

**Target:** > 95% on-time fulfillment by Q1 2027

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

### M6.4: Dashboard Operational Availability (Submethod 6.4)

**Metric:** % of V2MOM dashboards operational and accurate (data quality validated)

**Definition:** Track availability and accuracy of measurement infrastructure built in Method 4

**Target:** > 98% dashboard availability (operational with accurate data) by Q1 2027

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
- M6.4 sustains dashboards (operational tasks)

**SMART Assessment:** ✓ SMART - Clear metric (%), measurable, target defined, relevant to measurement infrastructure reliability

---
