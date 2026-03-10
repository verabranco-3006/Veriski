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

**Target:** -30% reduction by end of Q4 2026 → **11 days** (11.2 days target)

**Intermediate Milestones:**
- Q1 2026: 15 days (-6% vs baseline)
- Q2 2026: 14 days (-12% vs baseline)
- Q3 2026: 12 days (-25% vs baseline)
- Q4 2026: 11 days (-30% vs baseline)

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

**Target:** +50% increase by end of Q4 2026

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

**Target:** < 20% by end of Q4 2026

**Rationale:**
- Lower % over time indicates successful automation implementation (fewer repetitive manual changes)
- Provides data-driven input for automation backlog (M6.x Process as Code)
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
- **M6.2 (Process as Code Blueprints):** Flagged candidates become blueprint use cases
- **M6.3 (2027 Backlog):** Prioritized candidates become backlog items
- **M6.4 (Pilot Success Rate):** Automation candidates become pilot projects

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
- **Risk:** Identification without implementation → **Mitigation:** Integration with M6.x, monthly prioritization, close the loop with reviewers

**SMART Assessment:** ✓ Complete - Measurable (%), clear baseline approach, validation mechanisms, integration with V2MOM

---

### M2.5: CFR Correlation Accuracy ✓ SMART

**Metric:** % of Incidents where automated correlation system correctly identifies the specific asset-version change responsible for the failure

**Definition:** Accuracy rate of asset-version-to-incident correlation, validated against RCA findings

**Target:** > 90% by end of Q4 2026

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
- **M6.x (Process as Code):** Automation candidates with higher CFR justify automation investment
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

**Target:** < 30 minutes by end of Q4 2026

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

**Target:** > 80% by end of Q4 2026

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

**Target:** > 80% by end of Q4 2026

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

### M3.4: Alert Validation Accuracy - **MISSING TARGET**

**Metric:** % of alerts correctly validated and filtered before reaching Engineering

**Definition:** % of alerts where "Validated as Incident" flag matches actual outcome

**Target:** **> 85% by end of Q4 2026** (PROPOSED)

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

## Method 4: Strategic Metrics Orchestration

### M4.1: Executive Metric Literacy ✓ SMART

**Metric:** % of Leadership/End-Users who can correctly interpret calculation logic and navigate dashboards

**Definition:** Comprehension rate from quarterly literacy assessments

**Target:** > 85% by end of Q4 2026

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

## Method 5: Unified Platform Governance - **NEW MEASUREMENTS**

### M5.1: Platform Gap Closure Rate (NEW)

**Metric:** % of identified O11/ODC process gaps closed by end of quarter

**Definition:** Closure rate of process gaps identified during O11/ODC audit

**Target:** 100% of High priority gaps closed by Q3 2026, 80% of Medium by Q4 2026

**Measurement Logic:** Track gap closure status from initial audit through remediation

**Implementation:**
- **Data Source:** Gap Analysis Report (Confluence) + Remediation Tracker (Jira)
- **Collection Method:**
  - Q1: Complete O11/ODC gap audit → Create gap registry (Confluence)
  - Classify gaps by priority: High, Medium, Low
  - Create Jira tickets for each gap (Issue Type = "Process Gap")
  - Track: `(Closed Gaps / Total Gaps by Priority) * 100`
- **Frequency:** Quarterly measurement
- **Owner:** Vera Branco
- **Dashboard:** Jira dashboard filtering Process Gap tickets by Priority + Status
- **Automation:** Scheduled Jira query for gap closure rate by priority

**SMART Assessment:** ✓ SMART - Specific gaps, measurable (%), time-bound by priority

---

### M5.2: Platform SLA Parity Achievement (NEW)

**Metric:** % of incident/change SLAs harmonized across O11 and ODC platforms

**Definition:** % of process SLAs with identical definitions and thresholds across both platforms

**Target:** 100% by end of Q3 2026

**Measurement Logic:** Compare SLA definitions and thresholds across platforms, track harmonization

**Implementation:**
- **Data Source:** SLA Registry (Confluence) tracking O11 vs ODC SLAs
- **Collection Method:**
  - Create SLA Registry with columns: Process, SLA Name, O11 Threshold, ODC Threshold, Status (Aligned/Misaligned)
  - For each SLA: Compare definitions and thresholds
  - Aligned: O11 threshold = ODC threshold AND definition identical
  - Calculation: `(Aligned SLAs / Total SLAs) * 100`
- **Frequency:** Quarterly measurement
- **Owner:** Vera Branco
- **Dashboard:** Confluence SLA Registry with status tracking
- **Automation:** Manual tracking (no automation initially)

**SMART Assessment:** ✓ SMART - Clear comparison criteria, measurable, target defined

---

### M5.3: Unified Dashboard Uptime (EXISTING - ADD DETAIL)

**Metric:** % uptime for Unified Operational Visibility Dashboard

**Definition:** Availability of unified dashboard for executive consumption

**Target:** > 99.5% uptime (< 3.65 hours downtime per month)

**Measurement Logic:** Monitor dashboard availability and data refresh success rate

**Implementation:**
- **Data Source:** Dashboard hosting platform (Power BI Service, Tableau, etc.)
- **Collection Method:**
  - Monitor: Dashboard page load success + data refresh success
  - Downtime: Time when dashboard unavailable OR data >6 hours stale
  - Calculation: `(Available Time / Total Time) * 100`
- **Frequency:** Monthly measurement, real-time monitoring
- **Owner:** Vera Branco + Paulo Alves Monteiro
- **Dashboard:** Power BI Service monitoring + alerting
- **Automation:** Built-in platform monitoring (Power BI Service health metrics)

**SMART Assessment:** ✓ SMART - Specific metric (uptime %), clear target, measurable

---

### M5.4: Cross-Platform Compliance Score (NEW)

**Metric:** % of RFC submissions meeting unified compliance standards across both O11 and ODC

**Definition:** Compliance rate with harmonized RFC criteria and risk scoring

**Target:** > 90% by end of Q4 2026

**Measurement Logic:** Track RFC compliance with unified standards post-harmonization

**Implementation:**
- **Data Source:** Jira Change Management (both O11 and ODC projects)
- **Collection Method:**
  - Post-harmonization (after M5.2 complete): Track RFCs against unified checklist
  - Compliant RFC: Meets all mandatory criteria for unified standard (evidence, risk score, approvals)
  - Calculation: `(Compliant RFCs / Total RFCs) * 100`
- **Frequency:** Quarterly measurement (start after M5.2 completion in Q3)
- **Owner:** Vera Branco + Laura Ferreira
- **Dashboard:** Jira dashboard tracking RFC compliance by platform
- **Automation:** Jira Automation rules to flag non-compliant RFCs

**SMART Assessment:** ✓ SMART - Measurable compliance (%), clear target, time-bound

---

## Method 6: Process as Code Industrialization - **NEW MEASUREMENTS**

### M6.1: AI Platform Skill Certification Rate (NEW)

**Metric:** % of PE team members completing AI @ Product platform certification

**Definition:** Completion rate for technical upskilling on AI @ Product framework

**Target:** 100% by end of Q2 2026

**Measurement Logic:** Track training completion and skill assessment results

**Implementation:**
- **Data Source:** Training Registry + AI @ Product certification program
- **Collection Method:**
  - Define PE team roster (current: 4 people - Vera, Inês, Laura, Paulo)
  - Track completion of:
    - AI @ Product framework training
    - Pilot integration task (hands-on skill check)
  - Certification criteria: Training complete + successful pilot task
  - Calculation: `(Certified Team Members / Total PE Team) * 100`
- **Frequency:** Monthly tracking during Q1-Q2
- **Owner:** Vera Branco
- **Dashboard:** Training registry spreadsheet or Confluence page
- **Automation:** Manual tracking (certification program managed externally)

**SMART Assessment:** ✓ SMART - Clear population (PE team), binary certification, time-bound

---

### M6.2: Process as Code Blueprint Completion Rate (NEW)

**Metric:** % of high-impact automation candidates with completed "Process as Code" blueprints

**Definition:** Completion rate of technical blueprints for prioritized automation use cases

**Target:** 100% of Q1-identified candidates have blueprints by end of Q3 2026

**Measurement Logic:** Track blueprint creation status from use case identification to blueprint delivery

**Implementation:**
- **Data Source:** Use Case Registry (Confluence) + Blueprint Repository
- **Collection Method:**
  - Q1: Identify automation candidates from Incident, Change, Problem workflows
  - Prioritize: High-impact use cases (top 10-15)
  - Track blueprint status: Not Started, In Progress, Complete
  - Blueprint complete criteria: Technical design, AI @ Product integration approach, success criteria defined
  - Calculation: `(Complete Blueprints / Total Identified Use Cases) * 100`
- **Frequency:** Quarterly measurement
- **Owner:** Vera Branco (delegation to team)
- **Dashboard:** Confluence page with blueprint status tracker
- **Automation:** Manual tracking

**SMART Assessment:** ✓ SMART - Clear deliverable (blueprint), measurable (%), time-bound

---

### M6.3: 2027 Backlog Refinement Score (EXISTING - ADD DETAIL)

**Metric:** % of strategic blueprints converted to ready-to-code technical backlog items

**Definition:** Refinement completeness score for technical backlogs derived from blueprints

**Target:** 100% of blueprints have refined backlogs by end of Q4 2026

**Measurement Logic:** Assess backlog readiness using Definition of Ready criteria

**Implementation:**
- **Data Source:** Technical Backlog (Jira or AI @ Product platform backlog)
- **Collection Method:**
  - For each blueprint: Create corresponding Jira Epic/Story
  - Definition of Ready criteria:
    - User story defined
    - Acceptance criteria clear
    - Technical dependencies identified
    - Effort estimated
    - AI @ Product framework APIs/methods specified
  - Refinement score: % of criteria met per backlog item
  - Calculation: `(Backlog Items Meeting 100% DoR / Total Backlog Items) * 100`
- **Frequency:** Quarterly measurement
- **Owner:** Vera Branco
- **Dashboard:** Jira backlog view with "Refinement Status" field
- **Automation:** Jira checklist or custom field tracking DoR criteria

**SMART Assessment:** ✓ SMART - Clear criteria (DoR), measurable (%), time-bound

---

### M6.4: Automation Throughput - Pilot Success Rate (NEW)

**Metric:** % of piloted "Process as Code" automations successfully deployed to production

**Definition:** Success rate of pilot automations transitioning from PoC to production

**Target:** > 80% of pilots succeed by end of Q4 2026

**Measurement Logic:** Track pilot outcomes from initiation to production deployment

**Implementation:**
- **Data Source:** Pilot Tracker (Confluence or Jira)
- **Collection Method:**
  - For each pilot: Track lifecycle (Initiated → PoC → Testing → Production OR Failed)
  - Success criteria: Pilot reaches Production status
  - Failure criteria: Pilot abandoned or decommissioned before production
  - Calculation: `(Successful Pilots / Total Pilots Initiated) * 100`
- **Frequency:** Quarterly measurement
- **Owner:** Vera Branco
- **Dashboard:** Confluence pilot tracker with status column
- **Automation:** Manual tracking (pilot lifecycle managed manually initially)

**SMART Assessment:** ✓ SMART - Clear success definition (production deployment), measurable (%), target set

---

## Summary: Implementation Priorities

### Q1 2026 Actions
1. **Establish baselines:**
   - M3.1 Public MTTA (assess last 6 months)
   - M2.1 Change Lead Time (calculate 2024 H2 baseline)
   - M2.2 Standard Change Promotion (count 2024 H2 baseline)

2. **Create tracking mechanisms:**
   - M3.4 Alert Validation Log (Jira or Confluence)
   - M2.4 Reviewer Decision Reason field (Jira custom field)
   - M5.1 Gap Analysis Registry (Confluence + Jira)
   - M6.1 AI Platform Training Registry (Confluence)

3. **Define standards:**
   - M3.2 OLA/Deadline definitions for action items
   - M4.2 Metrics documentation template
   - M5.2 SLA Registry structure
   - M6.2 Blueprint template

### Q2 2026 Actions
1. **Deploy dashboards:**
   - M1.2 Jira Governance Dashboard (FedRAMP customer filter)
   - M2.1 Change Lead Time dashboard (Jira or Power BI)
   - M4.1 Training literacy assessment tool
   - M5.3 Unified Platform Dashboard

2. **Automate data collection:**
   - M2.3 RFC Rejection Velocity (Jira Automation)
   - M3.1 Public MTTA (Statuspage.io API integration)
   - M3.2 Action Item SLA tracking (Jira SLA)

### Q3-Q4 2026 Actions
1. **Measure and refine:**
   - All metrics operational
   - Quarterly reviews and target adjustments
   - Continuous improvement based on data

---

## Key Recommendations

1. **Prioritize baseline establishment** - Cannot measure improvement without starting point (M2.1, M2.2, M3.1)

2. **Implement data collection automation early** - Manual tracking doesn't scale (Jira Automation, API integrations)

3. **Create dedicated dashboards** - Real-time visibility drives accountability (Jira dashboards, Power BI)

4. **Define measurement standards** - Templates and checklists ensure consistency (OLAs, documentation templates, DoR)

5. **Start with high-value, low-effort metrics** - M1.3 (Training Rate), M4.2 (Documentation Coverage), M6.1 (Certification Rate) are straightforward wins

6. **Address measurement gaps immediately:**
   - M3.4 needs Alert Validation practice defined
   - M5 and M6 need tracking mechanisms created
   - All metrics need baseline assessment

---

**Next Steps:**
1. Review and validate proposed measurements with stakeholders
2. Create implementation backlog (Jira Epics for measurement infrastructure)
3. Assign owners and timelines for baseline establishment
4. Schedule monthly V2MOM measurement review cadence
