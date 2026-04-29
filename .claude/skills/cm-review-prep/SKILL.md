---
skill_name: cm-review-prep
title: Change Management Review Prep
description: Prepare the Change Management section for the bi-weekly Operations Review — Power BI data analysis, narrative, and trend comparison
---

# Change Management Review Prep

Prepares the Change Management section of Process Engineering's contribution to the bi-weekly Operations Review.

## Usage

```
/cm-review-prep                → Prepare CM data for the next Ops Review
/cm-review-prep [start] [end]  → Specify custom review period (YYYY-MM-DD)
```

---

## Context

Change Management data comes from the **RFC Jira project**, fed into the **ODC Change Management** Power BI semantic model. The Power BI report is the source of truth — it's what stakeholders see.

**Process documentation:** [Change Management Process (V6)](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/3862331705/Change+Management+Process)

**Power BI report:** [ODC Change Management Dashboard](https://app.powerbi.com/groups/me/apps/3a45f9da-1b76-4e56-8d53-f5ecca33e50c/reports/449e7964-c785-47c4-b17b-b1a4fbcc2d9b/33cb60d0853417cd4e37?ctid=1e7930e6-1ca4-40df-ac06-adabc2b139a3&experience=power-bi) — the **Operations Review** page is the source of truth for headline volumes. All numbers on the Confluence report must reconcile to this page's tooltip values.

**Operations Review page scope (locked):** RFCs created in window with at least one production-ring execution (ring+1/osall, ring+2/ea, ring+3/ga). Excludes Cancelled. Match this scope in all DAX queries — do NOT use unfiltered RFC_DISTINCT counts.

**Power BI report with date filter** (append to URL):
```
&filter=Calendar/Date ge YYYY-MM-DD and Calendar/Date le YYYY-MM-DD
```

### RFC vs Change Execution

A critical distinction in the process:

- **RFC (Request for Change)** — the Jira issue, the authorization record. One per change request. Types: Standard (pre-approved), Normal (CAB-approved), Emergency (system-wide incidents only).
- **Change Execution** — each discrete deployment or configuration action performed within a specific Ring. One RFC can produce multiple executions (one per ring impacted).

**Why this matters:** Every ring touched introduces fresh risk and requires distinct deployment actions, validation steps, and rollback windows. Metrics must report both views:
- **RFC count** — authorization volume (how many changes were requested)
- **Change Execution count** — operational volume (how many deployment events actually happened)

In the data model: `RFC_DISTINCT` = one row per RFC, `RFC_RINGS` = one row per change execution (RFC x Ring). "Ring not assigned" entries are typically Standard Changes deployed through the SDLC pipeline.

### Change types

| Type | Risk | Approval | When |
|------|------|----------|------|
| **Standard** | Low/Medium, pre-approved | Initial CAB approval for catalog entry, then no further approval | Code via SDLC pipeline, or catalog-documented operations |
| **Normal** | Medium+, not urgent | CAB review and approval required | Non-pre-approved changes, rollbacks to older versions, fast tracks |
| **Emergency** | Critical, urgent | Expedited written approval (no verbal-only) | System-wide incidents only. Must link to RDINC. Mandatory retrospective. |

### Other key concepts

- **Fast Tracks** — rushed deployments skipping bake periods. Last resort. Submitted as Normal Changes. VS Leaders can block.
- **Rollbacks** — revert to previous version. Automatic rollbacks (deployment/test/bake failure) don't need RFC. Manual rollbacks need Normal RFC. Exception: Emergency RFC for system-wide impact outside working hours.
- **Change Catalog** — documented operations with pre-approved Standard status. Teams maintain their own catalogs.

**Data source priority:**
1. **Playwright** → Power BI report (read the charts — same visuals stakeholders see)
2. **DAX queries** → drill into specific numbers when charts aren't enough
3. **Jira RFC** → fallback if Power BI is unavailable

---

## Step 1: Determine review period

- Ops Review is bi-weekly on Thursdays
- **End date** = Ops Review date minus 2 days (Tuesday) — allows data to settle before analysis
- **Start date** = End date minus 15 days
- Example: Ops Review Thursday April 30 → end date April 28, start date April 13
- Ask: "The next Ops Review is Thursday [DATE]. Review period: [START_DATE] to [END_DATE] (15 days, 2-day freeze). Correct?"
- Wait for confirmation
- If custom dates provided via args, use those instead

## Step 2: Gather previous context

Read the most recent Ops Review Confluence report to get previous CM metrics for trend comparison.

1. Use `mcp__claude_ai_Atlassian__searchConfluenceUsingCql`:
   - CQL: `ancestor = 5316116528 AND type = page ORDER BY created DESC`
   - Space: EEO
2. Read the page with `mcp__claude_ai_Atlassian__getConfluencePage` (markdown format)
3. Extract previous CM metrics: incident-driven RFC rate, Normal Planned %, Fast Track %, Emergency count, ring distribution

## Step 3: Collect current data

### Primary: Power BI report via Playwright

Navigate to the Power BI report and take accessibility snapshots of each relevant page/tab to read the chart data.

**Pre-check:** Navigate to the report URL and take a snapshot. If the page shows a login/SSO page instead of the report, tell the user: "Power BI requires browser authentication. Please log in at the URL and retry." Skip to DAX queries as secondary source.

1. Use `mcp__playwright__browser_navigate` to open the report URL
2. Wait 5-6 seconds with `mcp__playwright__browser_wait_for` for the report to fully render
3. Take `mcp__playwright__browser_snapshot` — check if the snapshot contains report content or a login page
4. If not authenticated: log as data gap, proceed to DAX queries
5. **Set the date range** using the Between slicer (two textbox inputs in the header):
   ```
   mcp__playwright__browser_fill_form with fields:
   - Start date textbox (label contains "Data de início"): value "DD-MM-YYYY" (e.g., "13-04-2026")
   - End date textbox (label contains "Data de fim"): value "DD-MM-YYYY" (e.g., "28-04-2026")
   ```
   Then press Enter with `mcp__playwright__browser_press_key` and wait 4 seconds for the report to refresh.
6. Take a new snapshot and verify the slicer shows the correct dates
7. Read chart values, navigate between report pages/tabs using `mcp__playwright__browser_click`

**Date format:** The slicer uses DD-MM-YYYY format (Portuguese locale).

**What Playwright reads (charts only):** The snapshot captures chart shapes, axis values, legend entries, and stacked bar proportions. The accessibility tree exposes data point values as `option` elements (e.g., `option "17"`). For authoritative volumes, **always confirm via tooltips** (next step).

**Tooltip validation (REQUIRED for Ops Review page):**

After taking the snapshot, hover over each headline data point with `mcp__playwright__browser_hover` to surface the tooltip — then take a follow-up snapshot and grep for the `alert` element. Tooltips disclose the underlying RFC count, execution count, and grouping context that resolves the RFC-level vs execution-level ambiguity.

```
mcp__playwright__browser_hover → target the chart segment ref
mcp__playwright__browser_snapshot → save with descriptive filename
Grep "alert.*\[ref=e\d+\]:" → tooltip text appears here
```

Hover at minimum:
1. Largest bar in **RFC Risk Classification** → confirms RFC-level volume (e.g., `Contagem de ISSUE_KEY 17`)
2. Largest bar in **# Change Execution per RFC type** → confirms execution-level volume
3. **Fast Track** segment in **Changes by Category Reason** → tooltip discloses BOTH `#RFCs` and `#Change Executions` (e.g., `#RFCs 6, #Change Executions 13`)
4. Normal Planned bar in **How RFCs are being used** → tooltip shows `# Changes Linked to Incidents X, # Changes Not Linked to Incidents Y` (RFC-level)

**Operations Review page chart guide (locked April 2026 fine-tuning):**

| Chart | Level | Tooltip discloses | Use for |
|-------|-------|------------------|---------|
| RFC Risk Classification | **RFC** | `Contagem de ISSUE_KEY` | Total RFC volume by type x risk |
| # Change Execution per RFC type | **Execution** | Execution count per ring x type | Operational volume, ring distribution |
| % RFCs used to fix Incidents (headline tile) | **RFC** | Percentage of total RFCs | Incident-driven rate (e.g., 23.40% = 11/47) |
| How RFCs are being used | **RFC** | `# Changes Linked to Incidents`, `# Changes Not Linked` | Incident vs planned by type |
| Changes by Category Reason | **Mixed (% on Execution)** | Both `#RFCs` AND `#Change Executions` | Fast Track count + execution share |
| Emergency Changes and Incidents | RFC | — | Emergency volume + linkage |
| Linked Incidents (table) | — | — | Emergency compliance check (system-wide impact) |

### Secondary: DAX queries for drill-down

Connect to the ODC Change Management semantic model for specific numbers the charts don't surface.

**Connection:**
```
ConnectFabric → workspace: "[Engineering] Process Engineering [BIZ]", semanticModelName: "ODC Change Management"
```
Connection name: `Fabric-%5BEngineering%5D%20Process%20Engineering%20%5BBIZ%5D-ODC Change Management`

**Available DAX queries (use as needed, not all required):**

**Volume overview — RFC count vs Change Execution count:**
```dax
EVALUATE
ROW(
    "Total RFCs", COUNTROWS(RFC_DISTINCT),
    "Total Change Executions", COUNTROWS(RFC_RINGS),
    "Executions with Ring", CALCULATE(COUNTROWS(RFC_RINGS), RFC_RINGS[RING] <> "Ring not assigned"),
    "Ring not assigned", CALCULATE(COUNTROWS(RFC_RINGS), RFC_RINGS[RING] = "Ring not assigned")
)
```
> "Ring not assigned" = typically Standard Changes via SDLC pipeline.

**RFC volume by type** (counts RFCs, not executions):
```dax
EVALUATE
SUMMARIZECOLUMNS(
    RFC_DISTINCT[ISSUE_TYPE],
    "Count", COUNTROWS(RFC_DISTINCT)
)
```

**Incident-driven RFC rate** (pre-built measures, RFC-level):
```dax
EVALUATE
ROW(
    "Changes Linked to Incidents", [# Changes Linked to Incidents],
    "% Fixing Incidents", [% Changes Fixing Incidents],
    "Changes Not Linked", [# Changes Not Linked to Incidents],
    "Total Created", [# RFCs Created],
    "Changes Approved", [# Changes Approved],
    "Ongoing", [Changes On Going]
)
```

**Risk classification** (RFC-level):
```dax
EVALUATE
SUMMARIZECOLUMNS(
    RFC_DISTINCT[CHANGE_RISK],
    "Count", COUNTROWS(RFC_DISTINCT)
)
ORDER BY [Count] DESC
```

**Ring distribution** (Change Execution-level — one row per RFC x Ring):
```dax
EVALUATE
SUMMARIZECOLUMNS(
    RFC_RINGS[RING],
    "Count", COUNTROWS(RFC_RINGS)
)
ORDER BY [Count] DESC
```
> This counts **change executions**, not RFCs. One RFC touching 3 rings = 3 executions.

**Status distribution** (RFC-level):
```dax
EVALUATE
SUMMARIZECOLUMNS(
    RFC_DISTINCT[STATUS_NAME],
    "Count", COUNTROWS(RFC_DISTINCT)
)
ORDER BY [Count] DESC
```

**Change category** (RFC-level — also identifies Fast Tracks):
```dax
EVALUATE
SUMMARIZECOLUMNS(
    RFC_DISTINCT[CHANGE_CATEGORY],
    "Count", COUNTROWS(RFC_DISTINCT)
)
ORDER BY [Count] DESC
```
> `CHANGE_CATEGORY` maps to Jira `customfield_17424`. Values include: Change Configuration, Change Infrastructure, Restart, Other Write Operation, **Fast Track**, Retry, Customer Request. Fast Track count and % come directly from this field.

**Fast Track detail** (RFC-level — list all Fast Track RFCs):
```dax
EVALUATE
SELECTCOLUMNS(
    FILTER(RFC_DISTINCT, RFC_DISTINCT[CHANGE_CATEGORY] = "Fast Track"),
    "Key", RFC_DISTINCT[ISSUE_KEY],
    "Summary", RFC_DISTINCT[SUMMARY],
    "Type", RFC_DISTINCT[ISSUE_TYPE],
    "Risk", RFC_DISTINCT[CHANGE_RISK],
    "Created", RFC_DISTINCT[CREATED_DATE]
)
ORDER BY [Created] DESC
```

**Change type x usage** (incident-driven vs planned, RFC-level):
```dax
EVALUATE
SUMMARIZECOLUMNS(
    RFC_DISTINCT[ISSUE_TYPE],
    RFC_DISTINCT[Is Linked to Incident],
    "Count", COUNTROWS(RFC_DISTINCT)
)
ORDER BY RFC_DISTINCT[ISSUE_TYPE]
```
> `Is Linked to Incident` is a calculated column. Cross-tab shows which change types are being used for incident response vs planned operations. Emergency Changes should only be linked to incidents.

**Emergency detail** (compliance check — list all ERFCs):
```dax
EVALUATE
SELECTCOLUMNS(
    FILTER(RFC_DISTINCT, RFC_DISTINCT[ISSUE_TYPE] = "Emergency Change"),
    "Key", RFC_DISTINCT[ISSUE_KEY],
    "Summary", RFC_DISTINCT[SUMMARY],
    "Risk", RFC_DISTINCT[CHANGE_RISK],
    "Category", RFC_DISTINCT[CHANGE_CATEGORY],
    "Created", RFC_DISTINCT[CREATED_DATE]
)
ORDER BY [Created] DESC
```
> Cross-reference with `INCIDENTS_LINKED_CHANGES` to verify system-wide impact linkage.

**Emergency compliance — linked incidents with system-wide impact:**
```dax
EVALUATE
SELECTCOLUMNS(
    INCIDENTS_LINKED_CHANGES,
    "RFC", INCIDENTS_LINKED_CHANGES[ISSUE_KEY],
    "Incident", INCIDENTS_LINKED_CHANGES[LINKED_ISSUE_KEY],
    "System-Wide Impact", INCIDENTS_LINKED_CHANGES[SYSTEM_WIDE_IMPACT],
    "Incident Type", INCIDENTS_LINKED_CHANGES[INCIDENT_TYPE]
)
```
> Emergency RFCs without a linked system-wide-impact incident are non-compliant.

**Lead time — Normal Changes only (M2.1):**
```dax
EVALUATE
ROW(
    "Avg Lead Time (Days)", CALCULATE(AVERAGE(RFC_DISTINCT[LEADTIME (Days)]), RFC_DISTINCT[ISSUE_TYPE] = "Normal Change"),
    "Median Lead Time (Days)", CALCULATE(MEDIAN(RFC_DISTINCT[LEADTIME (Days)]), RFC_DISTINCT[ISSUE_TYPE] = "Normal Change"),
    "Max Lead Time (Days)", CALCULATE(MAX(RFC_DISTINCT[LEADTIME (Days)]), RFC_DISTINCT[ISSUE_TYPE] = "Normal Change"),
    "Normal RFC Count", CALCULATE(COUNTROWS(RFC_DISTINCT), RFC_DISTINCT[ISSUE_TYPE] = "Normal Change")
)
```
> `LEADTIME (Days)` is a calculated column on RFC_DISTINCT (creation to resolution). Filter to Normal Changes for M2.1 tracking. Baseline: 16 days (H2 2025). Target: 11 days (-30%).

**Lead time — time-in-status breakdown (Normal Changes):**
```dax
EVALUATE
ROW(
    "Avg Submitted to CAB (hrs)", CALCULATE(AVERAGE(RFC_DISTINCT[TIME_IN_SUBMITTED_TO_CAB_IN_HOURS]), RFC_DISTINCT[ISSUE_TYPE] = "Normal Change"),
    "Avg Approved by CAB (hrs)", CALCULATE(AVERAGE(RFC_DISTINCT[TIME_IN_APPROVED_BY_CAB_HOURS]), RFC_DISTINCT[ISSUE_TYPE] = "Normal Change"),
    "Avg Implementing (hrs)", CALCULATE(AVERAGE(RFC_DISTINCT[TIME_IN_IMPLEMENTING_IN_HOURS]), RFC_DISTINCT[ISSUE_TYPE] = "Normal Change"),
    "Avg Reviewed Ready (hrs)", CALCULATE(AVERAGE(RFC_DISTINCT[TIME_IN_REVIEWED_READY_FOR_APPROVAL_IN_HOURS]), RFC_DISTINCT[ISSUE_TYPE] = "Normal Change"),
    "Avg Draft (hrs)", CALCULATE(AVERAGE(RFC_DISTINCT[TIME_IN_DRAFT_IN_HOURS]), RFC_DISTINCT[ISSUE_TYPE] = "Normal Change")
)
```
> Shows where time is spent in the workflow. Helps identify bottleneck stages for M2.1 lead time reduction.

**Period filtering:**
Key date columns: `RFC_DISTINCT[CREATED_DATE]`, `RFC_DISTINCT[RESOLVED_DATE]`, `Calendar[Date]`

Two patterns depending on the query type:

**For SUMMARIZECOLUMNS** — pass a filter table as an argument (CALCULATE wrapping SUMMARIZECOLUMNS fails):
```dax
EVALUATE
SUMMARIZECOLUMNS(
    RFC_DISTINCT[ISSUE_TYPE],
    FILTER(ALL(RFC_DISTINCT[CREATED_DATE]), RFC_DISTINCT[CREATED_DATE] >= DATE(YYYY,M,D) && RFC_DISTINCT[CREATED_DATE] <= DATE(YYYY,M,D)),
    "Count", COUNTROWS(RFC_DISTINCT)
)
```

**For ROW with pre-built measures** — wrap each measure in its own CALCULATE (CALCULATE wrapping ROW fails):
```dax
EVALUATE
ROW(
    "Metric1", CALCULATE([Measure1], RFC_DISTINCT[CREATED_DATE] >= DATE(YYYY,M,D), RFC_DISTINCT[CREATED_DATE] <= DATE(YYYY,M,D)),
    "Metric2", CALCULATE([Measure2], RFC_DISTINCT[CREATED_DATE] >= DATE(YYYY,M,D), RFC_DISTINCT[CREATED_DATE] <= DATE(YYYY,M,D))
)
```

**For ROW with COUNTROWS** — same pattern, CALCULATE inside each expression:
```dax
EVALUATE
ROW(
    "Total RFCs", CALCULATE(COUNTROWS(RFC_DISTINCT), RFC_DISTINCT[CREATED_DATE] >= DATE(YYYY,M,D), RFC_DISTINCT[CREATED_DATE] <= DATE(YYYY,M,D))
)
```

**For SELECTCOLUMNS/FILTER** — use inline filter predicates:
```dax
FILTER(RFC_DISTINCT, RFC_DISTINCT[CREATED_DATE] >= DATE(YYYY,M,D) && RFC_DISTINCT[CREATED_DATE] <= DATE(YYYY,M,D))
```

### Fallback: Jira

```
project = RFC AND created >= "[START_DATE]" AND created <= "[END_DATE]" ORDER BY created DESC
```

## Step 4: Analyze

**Analysis Vectors:**

| Vector | Metric level | What to report | Alert threshold | V2MOM link |
|--------|-------------|---------------|-----------------|------------|
| Volume overview | Both | Total RFCs vs Total Change Executions. Ratio shows operational amplification. | -- | -- |
| RFC volume by type | RFC | Standard vs Normal vs Emergency breakdown | -- | -- |
| Incident-Driven RFC Rate | RFC | % of RFCs linked to incidents | > 35% | -- |
| Normal Planned Usage | RFC | % of Normal Changes for planned ops ("Shadow SDLC") | > 60% | M2.1 |
| Fast Track Usage | **Execution + RFC** | Report BOTH: (a) % of executions with CHANGE_CATEGORY = "Fast Track" — this is what the dashboard surfaces; (b) distinct RFC count for follow-up. Tooltip on Fast Track segment in "Changes by Category Reason" gives both numbers. | > 5% (execution level) | M2.2 |
| Emergency Volume | RFC | Count + system-wide impact compliance | > 3 per period | -- |
| Emergency Compliance | RFC | ERFCs without linked system-wide-impact incident | Any non-compliant | -- |
| Change Type x Usage | RFC | % distribution of Standard/Normal/Emergency by usage: incident-driven vs planned operations | -- | -- |
| Lead Time (Normal) | RFC | Mean/median days from creation to resolution for Normal Changes | > 16 days (baseline) | M2.1 |
| Lead Time Breakdown | RFC | Time-in-status by workflow stage (bottleneck identification) | -- | M2.1 |
| First-Pass Approval | RFC | % approved without rework (status transition proxy) | < 85% | M6.2b |
| Ring Distribution | Execution | Volume per ring (should decrease toward GA) | GA > OSALL | -- |
| Risk Classification | RFC | Low Risk % + paradoxes (Low Risk + Emergency) | Any paradox | -- |

**Narrative structure for each finding:**

1. **What the data shows** -- the metric and its value
2. **How it compares** -- trend vs previous periods (use table format)
3. **Why it matters** -- the risk, compliance, or operational implication
4. **What we're doing about it** -- link to V2MOM initiative or action item
5. **What we need from you** (if applicable) -- specific ask to Value Stream Leaders

## Step 5: Generate output

Save to `meetings/prep/YYYY-MM-DD-cm-review-data.md`:

```markdown
# Change Management Review Data -- [DATE]
**Review period:** [START_DATE] to [END_DATE]
**Scope:** RFCs created in window with at least one production-ring execution (ring+1/osall, ring+2/ea, ring+3/ga). Excludes Cancelled. Matches Operations Review dashboard.
**Total RFCs (RFC level, tooltip-confirmed):** X (Y Standard, Z Normal, W Emergency)
**Total Production-Ring Executions (Execution level, tooltip-confirmed):** X (Y Standard, Z Normal)

> Source of truth: ODC Change Management Power BI report > Operations Review page. All headline numbers below reconcile to that page's tooltip values.

---

## Key findings

1. [Finding with narrative -- What + Trend + Why + Action]
2. [Finding with narrative]
3. [Finding with narrative]

## Metrics

### RFC volume by type

| Type | Count | % | Previous | Change |
|------|-------|---|----------|--------|
| Standard | X | Y% | Z | +/-N |
| Normal | X | Y% | Z | +/-N |
| Emergency | X | Y% | Z | +/-N |

### Incident-Driven RFC Rate

| Metric | Value |
|--------|-------|
| Linked to incidents | X (Y%) |
| Not linked | X |
| Approved | X |
| Ongoing | X |

### Risk Classification

| Risk | Count | % |
|------|-------|---|
| Low | X | Y% |
| Medium | X | Y% |
| High | X | Y% |

### Ring Distribution

| Ring | Count | % |
|------|-------|---|
| ring+3/ga | X | Y% |
| ring+2/ea | X | Y% |
| ring+1/osall | X | Y% |
| ... | ... | ... |

### Change Category

| Category | Count | % |
|----------|-------|---|
| [Top categories] | X | Y% |

### Lead Time — Normal Changes (M2.1)

| Metric | Value |
|--------|-------|
| Mean lead time (days) | X |
| Median lead time (days) | X |
| Max lead time (days) | X |
| Normal RFC count | X |

### Lead Time — Workflow Breakdown (Normal Changes)

| Stage | Avg Hours |
|-------|-----------|
| Draft | X |
| Submitted to CAB | X |
| Approved by CAB (wait) | X |
| Reviewed Ready for Approval | X |
| Implementing | X |

### Trend comparison

| Metric | V2MOM | [Period -2] | [Period -1] | Current | Target | Change |
|--------|-------|-------------|-------------|---------|--------|--------|
| Normal Lead Time (days) | M2.1 | X | Y | Z | 11 days | +/-N |
| Standard Change % (RFC level) | M2.4 | X% | Y% | Z% | >60% | +/-pp |
| Emergency Accuracy | M2.5 | X% | Y% | Z% | >95% | +/-pp |
| Incident-Driven RFC Rate | — | X% | Y% | Z% | <35% | +/-pp |
| Normal Planned % | M2.2a proxy | X% | Y% | Z% | — | +/-pp |
| Fast Track % (execution level) | M2.2 | X% | Y% | Z% | <5% | +/-pp |
| Fast Track count (RFCs / Executions) | M2.2 | X/Y | X/Y | X/Y | — | +/- |
| Emergency count | — | X | Y | Z | <3 | +/-N |

## Compliance signals

- Emergency without system-wide impact: [list or "None"]
- Risk paradoxes (Low Risk + Emergency): [list or "None"]
- Fast Track usage: [count and context]

## What's going well

- [Positive signals]
```

Return: "CM review data ready at `meetings/prep/YYYY-MM-DD-cm-review-data.md`. Run `/ops-review-prep` to combine with retro data into the full prep."

## Step 6: Update running metrics log

Append the current period's data to `initiatives/active/m6.1_cab_process_reviews/metrics/cm-review-metrics.md`.

1. Read the existing log file
2. Add a new row to each running metrics table with the current period's values:
   - **Volume table:** Total RFCs, Standard, Normal, Emergency, Executions, Ring assigned, Ring not assigned
   - **V2MOM-Aligned Metrics table:** Normal Lead Time, Standard %, Emergency Accuracy, First-Pass Approval %, Incident-Driven Rate, Normal Planned %, Fast Track %, Fast Track Count
   - **Risk Distribution table:** Low, Medium, High counts and %
   - **Ring Distribution table:** all rings + Production %
   - **Change Category table:** all categories with counts and %
3. Update the **Alert Status** table with current values and status indicators
4. Add any new **Data Gaps** discovered during this run
5. Update the `Last updated` timestamp at the bottom

The log provides trend data for future runs — no more dependency on Confluence extraction for historical metrics.

---

## Power BI Model Schema

**ODC Change Management** -- 27 tables, 33 measures

Key tables:
- `RFC_DISTINCT` (30 cols): ISSUE_KEY, SUMMARY, STATUS_NAME, CREATED_DATE, RESOLVED_DATE, ISSUE_TYPE, CHANGE_RISK, CHANGE_CATEGORY, OPERATION_TYPE, CHANGE_CATEGORY, REVIEWER, APPROVER, ASSIGNEE, REPORTER, Is Linked to Incident (calculated)
- `RFC_RINGS`: ISSUE_KEY, RING
- `RFC_TEAMS`: ISSUE_KEY, TEAMS
- `RFC_LABELING`: ISSUE_KEY, LABELS
- `INCIDENTS_LINKED_CHANGES`: ISSUE_KEY, LINKED_ISSUE_KEY, SYSTEM_WIDE_IMPACT, INCIDENT_TYPE
- `Calendar`: shared date dimension

Time-in-status columns on RFC_DISTINCT: TIME_IN_DRAFT_IN_HOURS, TIME_IN_SUBMITTED_TO_CAB_IN_HOURS, TIME_IN_APPROVED_BY_CAB_HOURS, TIME_IN_IMPLEMENTING_IN_HOURS, TIME_IN_CHANGE_APPROVED_IN_HOURS, TIME_IN_CHANGE_IMPLEMENTED_IN_HOURS, TIME_IN_REVIEWED_READY_FOR_APPROVAL_IN_HOURS
Calculated columns: `LEADTIME (Days)` (creation to resolution), `Aging (days)`, `Aging (Groups)`, `Is Linked to Incident`

---

## Tips

- Prefer Playwright reading of the Power BI report -- it matches what stakeholders see
- **Always tooltip-validate the headline volumes** -- the accessibility snapshot exposes data point values, but tooltips are the only authoritative source for the underlying RFC and execution counts
- **Always call out the metric level explicitly** (RFC level vs Execution level) -- the Operations Review dashboard mixes both denominators on the same page. The Confluence report and prep file must label every metric to avoid trend confusion
- Use DAX for drill-down only (specific RFCs, emergency compliance detail, paradox detection)
- Always show trend data -- a single data point means nothing without context
- Flag compliance signals explicitly -- Emergency misuse, ring distribution inversion, Fast Track spikes are audit-relevant
- Connect findings to V2MOM initiatives -- PE is actively working on root causes, not just reporting
- This skill produces data analysis and narrative (markdown tables + text), not chart visuals -- Power BI is the visual layer, dashboard screenshots for slides are a manual step

## Known data gaps

- **M2.4 Standard Change % denominator** -- not formally locked. Default to RFC-level (Standard RFCs / Total RFCs) for Confluence reporting and label it accordingly. Pending decision before next Ops Review.
- **M2.1 Normal lead time baseline** (16 days) does not match current Operations Review scope (Normal-only avg ~1.79 days for production-ring + ex-Cancelled). Baseline likely covers a different cohort -- align with M2.1 owner.
- **Trend back-fills** -- Apr 16 and earlier figures from Confluence may have used a different scope. Apples-to-apples comparison requires re-running prior periods with the locked production-ring + ex-Cancelled scope.
- **First-Pass Approval (M6.2b)** -- definition agreed but Jira field/transition not implemented. No tracking yet.
