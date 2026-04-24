---
skill_name: retro-review-prep
title: Retrospective Review Prep
description: Prepare the Retrospective section for the bi-weekly Operations Review — retro population health, action item tracking, and trend analysis
---

# Retrospective Review Prep

Prepares the Retrospective section of Process Engineering's contribution to the bi-weekly Operations Review.

## Usage

```
/retro-review-prep    → Prepare retro data for the next Ops Review
```

---

## Context

### Retrospective population

All incidents with **Retrospective Needed = Yes** (`customfield_17293`) in the RDINC Jira project. The review tracks the full active population — not a date-bounded window.

**Backlog cutoff:** Only include Solved incidents resolved **≥ 2 days before the ops review date**. Recently solved incidents haven't had time to start a retro — including them inflates the backlog count and creates noise.

**Status meanings (retro lifecycle):**

Jira tracks 4 statuses. Power BI's `RETROSPECTIVE_STATUS` (calculated column in `OTHER_PROPERTIES`) splits "Retrospective In Progress" into 3 sub-stages based on Reviewer/Approver fields. **Report using RETROSPECTIVE_STATUS (7 values), not Jira status (4 values).**

| RETROSPECTIVE_STATUS (DAX value) | Jira Status | Retro Stage | Meaning |
|---------------------|-------------|-------------|---------|
| In Backlog | Solved | Backlog | Incident resolved, retro needed but not started. **Only include if resolved ≥ 2 days before the ops review date.** |
| Retrospective In Progress | Retrospective In Progress | In Progress | Retro actively being worked (5-Whys, RCA) |
| Pending Review | Retrospective In Progress | Pending Review | Retro submitted, waiting for Reviewer |
| Pending Approval | Retrospective In Progress | Pending Approval | Retro reviewed, waiting for Approver |
| Retrospective Completed | Retrospective Completed | Completed | Retro approved, action items may still be open |
| Retrospective Closed | Closed | Closed | All action items delivered to production |
| Cancelled | — | Excluded | Retro cancelled — exclude from active population |
| Troubleshooting In Progress | — | Excluded | Incident still being troubleshot — exclude from retro population |

> **Active population** = In Backlog + Retrospective In Progress + Pending Review + Pending Approval + Retrospective Completed. Exclude Cancelled and Troubleshooting In Progress from all counts.

**Roles:** Commander, Reviewer, Approver. **RCA method:** 5-Whys.

### Action items

Action items are **linked issues** on RDINC tickets. Primary link type is "is reviewed by" but discipline varies — other link types may also be legitimate action items.

**Exclude:** RFCs linked with "is blocked by" — these are recovery actions (incident blocked by RFC execution), not retro action items. Exclude all RFC-type linked issues.

**Track per action item:** Assignee, due date, progress via **Jira status category** (To Do, In Progress, Done) — action items live across multiple projects with different workflows.

### Data sources

**Power BI semantic model:** Retrospectives

**Power BI reports:**
1. **Stakeholder view** (shared in Ops Review): [Retrospective Summary](https://app.powerbi.com/groups/me/apps/3a45f9da-1b76-4e56-8d53-f5ecca33e50c/reports/51c81030-b36b-4d75-a348-2ab5e4dff49a/9f435651ebe7467a9e8b?ctid=1e7930e6-1ca4-40df-ac06-adabc2b139a3&experience=power-bi)
2. **Overview**: [Retrospective Overview](https://app.powerbi.com/groups/me/apps/3a45f9da-1b76-4e56-8d53-f5ecca33e50c/reports/51c81030-b36b-4d75-a348-2ab5e4dff49a/e92ea0cac0e60f2d54a8?ctid=1e7930e6-1ca4-40df-ac06-adabc2b139a3&experience=power-bi)
3. **Details**: [Retrospective Details](https://app.powerbi.com/groups/me/apps/3a45f9da-1b76-4e56-8d53-f5ecca33e50c/reports/51c81030-b36b-4d75-a348-2ab5e4dff49a/8ababcbfd423d99dfe8a?ctid=1e7930e6-1ca4-40df-ac06-adabc2b139a3&experience=power-bi)

**Retrospective process:** [Confluence — Retrospective Process](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4696212894/Retrospective+Process)

**Jira project:** RDINC

**Data source priority:**
1. **Playwright** → Power BI reports (charts stakeholders see) — **source of truth for all volume data**
2. **DAX queries** → drill into numbers charts don't surface (status distribution, lead times, action item health, commander gaps)
3. **Jira RDINC** → detail drill-down only (specific retro details, stalled retro investigation, commander names). **Never use Jira for counts** — Power BI's semantic model has different filter logic and will not match Jira query totals.

---

## Step 1: Gather previous context

1. Read `metrics/retro-review-metrics.md` for historical trend data
2. Use `mcp__claude_ai_Atlassian__searchConfluenceUsingCql`:
   - CQL: `ancestor = 5316116528 AND type = page ORDER BY created DESC`
   - Space: EEO
3. Read the most recent page with `mcp__claude_ai_Atlassian__getConfluencePage` (markdown format)
4. Extract previous retro metrics for trend comparison

## Step 2: Collect current data

### Primary: Power BI reports via Playwright

Navigate to each report and take accessibility snapshots.

1. **Stakeholder view** — summary shared in Ops Review
2. **Overview** — additional metrics
3. **Details** — individual retro data

For each report:
1. `mcp__playwright__browser_navigate` to open the URL
2. `mcp__playwright__browser_wait_for` for load
3. `mcp__playwright__browser_snapshot` to read chart values
4. `mcp__playwright__browser_click` to navigate tabs/pages

Extract: status distribution, commander assignments, lead time trends, root cause breakdown, action item health, incident volume trends.

### Secondary: DAX queries for drill-down

**Connection:**
```
ConnectFabric → workspace: "[Engineering] Process Engineering [BIZ]", semanticModelName: "Retrospectives"
```
Connection name: `Fabric-%5BEngineering%5D%20Process%20Engineering%20%5BBIZ%5D-Retrospectives`

**Status distribution (pre-built measures):**
```dax
EVALUATE
CALCULATETABLE(
    ROW(
        "Active Retrospectives", [Active Retrospectives],
        "In Progress", [Retrospectives in Progress],
        "Completed", [Retrospectives Completed],
        "Closed", [Retrospectives Closed],
        "In Backlog", [Retrospectives in Backlog],
        "Pending Review", [Retrospectives Pending Review],
        "Pending Approval", [Retrospectives Pending Approval]
    ),
    OTHER_PROPERTIES[RETROSPECTIVE_NEEDED] = "Yes"
)
```
> Pre-built measures require `RETROSPECTIVE_NEEDED = "Yes"` filter context. Cross-check the "In Backlog" count against the Jira backlog query (which applies the 2-day cutoff). If they differ, use the Jira count for reporting and note the discrepancy.

**Root cause distribution:**
```dax
EVALUATE
SUMMARIZECOLUMNS(
    OTHER_PROPERTIES[RCA_CATEGORY],
    FILTER(OTHER_PROPERTIES, OTHER_PROPERTIES[RETROSPECTIVE_NEEDED] = "Yes"),
    "Count", COUNTROWS(OTHER_PROPERTIES)
)
ORDER BY [Count] DESC
```

**Action item health (pre-built measures):**
```dax
EVALUATE
CALCULATETABLE(
    ROW(
        "Action Items Created", [# Action Items Created],
        "Action Items Concluded", [# Action Items Concluded],
        "Action Items Overdue", [Action Items Overdue],
        "Past Due To Do", [Past Due Action Items (To Do)],
        "Past Due In Progress", [Past Due Action Items (In Progress)],
        "No Due Date", [Action Items Due Date not Available],
        "On Due", [Action Items On Due],
        "Completeness %", [Action Items Completeness (%)]
    ),
    OTHER_PROPERTIES[RETROSPECTIVE_NEEDED] = "Yes"
)
```
> Pre-built measures require `RETROSPECTIVE_NEEDED = "Yes"` filter context — without it they return the full 31K+ incident population.

**Commander assignment gaps (In Backlog + In Progress only):**
```dax
EVALUATE
SUMMARIZECOLUMNS(
    "Total Needing Commander", CALCULATE(COUNTROWS(OTHER_PROPERTIES), OTHER_PROPERTIES[RETROSPECTIVE_NEEDED] = "Yes", OTHER_PROPERTIES[RETROSPECTIVE_STATUS] IN {"In Backlog", "Retrospective In Progress", "Pending Review", "Pending Approval"}),
    "No Commander", CALCULATE(COUNTROWS(OTHER_PROPERTIES), OTHER_PROPERTIES[RETROSPECTIVE_NEEDED] = "Yes", OTHER_PROPERTIES[RETROSPECTIVE_STATUS] IN {"In Backlog", "Retrospective In Progress", "Pending Review", "Pending Approval"}, ISBLANK(OTHER_PROPERTIES[RETROSPECTIVE_COMMANDER]))
)
```
> Commanders are assessed for retros in Backlog and In Progress (including Pending Review/Approval). Once Completed, the commander already did their job.

**Lead times (pre-built measures):**
```dax
EVALUATE
CALCULATETABLE(
    ROW(
        "Avg Retrospective Leadtime (Days)", [Average Retrospective Leadtime (Days)],
        "Time to Complete Retro (Days)", [Time to complete Retrospective (days)],
        "Time to Start Retro (Days)", [Time to start Retrospective (days)],
        "Time to Complete Action Items (Days)", [Time to complete Action Items (days)]
    ),
    OTHER_PROPERTIES[RETROSPECTIVE_NEEDED] = "Yes"
)
```

**Incident throughput (replace dates with since-last-review window):**
```dax
EVALUATE
ROW(
    "Created Incidents", CALCULATE(COUNTROWS(INCIDENTS_DISTINCT), INCIDENTS_DISTINCT[CREATED_DATE] >= DATE(YYYY,M,D) && INCIDENTS_DISTINCT[CREATED_DATE] < DATE(YYYY,M,D)),
    "Resolved Incidents", CALCULATE(COUNTROWS(INCIDENTS_DISTINCT), NOT ISBLANK(INCIDENTS_DISTINCT[RESOLUTION_DATE]), INCIDENTS_DISTINCT[RESOLUTION_DATE] >= DATE(YYYY,M,D) && INCIDENTS_DISTINCT[RESOLUTION_DATE] < DATE(YYYY,M,D))
)
```
> The `# Created/Solved Incidents` pre-built measures use USERELATIONSHIP and fail in DAX queries — use direct COUNTROWS instead.

**Overdue action items detail:**
> `Days to Due` is a Text column — contains "Due Date not Available" for items without a due date. Use IFERROR(VALUE()) to safely convert, and filter text entries first.

```dax
EVALUATE
var _base = ADDCOLUMNS(
    FILTER(LINKED_ISSUES,
        LINKED_ISSUES[LINKED_ISSUE_STATUS_CATEGORY] <> "Done"
        && RELATED(OTHER_PROPERTIES[RETROSPECTIVE_NEEDED]) = "Yes"
        && FIND("-", LINKED_ISSUES[LINKED_ISSUE], 1, 0) > 0),
    "DaysOverdueNum", IFERROR(VALUE(LINKED_ISSUES[Days to Due]), 999)
)
RETURN
SELECTCOLUMNS(
    FILTER(_base, [DaysOverdueNum] < 0),
    "Retro", LINKED_ISSUES[ISSUE_KEY],
    "Action Item", LINKED_ISSUES[LINKED_ISSUE],
    "Type", LINKED_ISSUES[LINKED_ISSUE_TYPE],
    "Status", LINKED_ISSUES[LINKED_ISSUE_STATUS],
    "Status Category", LINKED_ISSUES[LINKED_ISSUE_STATUS_CATEGORY],
    "Due Date", LINKED_ISSUES[LINKED_ISSUE_DUE_DATE],
    "Days Overdue", [DaysOverdueNum],
    "Assignee", LINKED_ISSUES[LINKED_ISSUE_ASSIGNE]
)
ORDER BY [Days Overdue] ASC
```

**Action items by team (open, grouped by Jira project):**
```dax
EVALUATE
var _retroItems = FILTER(
    LINKED_ISSUES,
    LINKED_ISSUES[LINKED_ISSUE_STATUS_CATEGORY] <> "Done"
    && RELATED(OTHER_PROPERTIES[RETROSPECTIVE_NEEDED]) = "Yes"
    && FIND("-", LINKED_ISSUES[LINKED_ISSUE], 1, 0) > 0
)
var _withTeam = ADDCOLUMNS(
    _retroItems,
    "Team", LEFT(LINKED_ISSUES[LINKED_ISSUE], FIND("-", LINKED_ISSUES[LINKED_ISSUE]) - 1),
    "IsOverdue", IF(IFERROR(VALUE(LINKED_ISSUES[Days to Due]), 999) < 0, 1, 0),
    "NoDueDate", IF(ISERROR(VALUE(LINKED_ISSUES[Days to Due])), 1, 0)
)
RETURN
GROUPBY(
    _withTeam,
    [Team],
    "Total", COUNTAX(CURRENTGROUP(), 1),
    "To Do", SUMX(CURRENTGROUP(), IF(LINKED_ISSUES[LINKED_ISSUE_STATUS_CATEGORY] = "To Do", 1, 0)),
    "In Progress", SUMX(CURRENTGROUP(), IF(LINKED_ISSUES[LINKED_ISSUE_STATUS_CATEGORY] = "In Progress", 1, 0)),
    "Overdue", SUMX(CURRENTGROUP(), [IsOverdue]),
    "No Due Date", SUMX(CURRENTGROUP(), [NoDueDate])
)
ORDER BY [Total] DESC
```
> Team is derived from the Jira project prefix of the linked issue key (e.g., RDPIM from RDPIM-3484). Consider adding a project-to-team-name mapping table in Power BI for readability.

### Tertiary: Jira RDINC for detail drill-down

Use `mcp__claude_ai_Atlassian__searchJiraIssuesUsingJql` **only for detail** — never for counts. Power BI is the source of truth for all volume data. Jira queries are for investigating specific retros flagged by Power BI data.

**Stalled retros (investigate specific ones):**
```
project = RDINC AND cf[17293] = "Yes" AND status in ("Retrospective In Progress", "Retrospective Completed") AND updated <= "[OPS_REVIEW_DATE - 15 days]" ORDER BY updated ASC
```

**Recently closed (since last review — confirm against Power BI):**
```
project = RDINC AND cf[17293] = "Yes" AND status = Closed AND resolved >= "[LAST_REVIEW_DATE]" ORDER BY resolved DESC
```

**Specific retro detail (when DAX flags an issue):**
```
key = RDINC-XXXXX
```

## Step 3: Analyze

| Vector | What to report | Alert threshold |
|--------|---------------|-----------------|
| Backlog health | Solved (backlog) count + trend | Increase > 10% vs previous |
| Status distribution | Full RETROSPECTIVE_STATUS breakdown (In Backlog, In Progress, Pending Review, Pending Approval, Completed). Sample retros Pending Review and Pending Approval. | > 30% stalled (no update 15+ days) |
| Commander assignment | Retros in Backlog + In Progress without Commander + % | > 40% unassigned |
| Lead time | Avg days incident to retro close | > 60 days |
| Root cause distribution | Top 3 RCA categories + trend | Single category > 50% |
| Action item health | Open, overdue, no due date, completed since last review. By status category. | > 5 overdue |
| Throughput | Closed since last review vs new incidents needing retro | Net backlog increase |

**Narrative structure per finding:**
1. **What the data shows** — metric and value
2. **How it compares** — trend vs previous (table)
3. **Why it matters** — risk, compliance, operational implication
4. **What we're doing about it** — V2MOM initiative or action
5. **What we need from you** (if applicable) — ask to Value Stream Leaders

## Step 4: Generate output

Save to `meetings/prep/YYYY-MM-DD-retro-review-data.md`:

```markdown
# Retrospective Review Data — [DATE]
**Population:** All RDINCs with Retrospective Needed = Yes
**Data snapshot:** [DATE]

---

## Key findings

### 1. [Finding title]
[Narrative]

---

## Metrics

### Retro population snapshot

| RETROSPECTIVE_STATUS | Count | % | Previous | Change |
|---------------------|-------|---|----------|--------|
| In Backlog | X | Y% | — | — |
| In Progress | X | Y% | — | — |
| Pending Review | X | Y% | — | — |
| Pending Approval | X | Y% | — | — |
| Completed | X | Y% | — | — |
| **Active total** | **X** | — | — | — |
| Closed (all done) | X | — | — | +X since last |

### Commander assignment (In Backlog + In Progress)

| Metric | Count | % |
|--------|-------|---|
| Retros needing Commander (Backlog + In Progress) | X | — |
| With Commander | X | Y% |
| Without Commander | X | Y% |

### Lead times

| Metric | Days | Previous | Change |
|--------|------|----------|--------|
| Avg retrospective leadtime | X | — | — |
| Time to start retro | X | — | — |
| Time to complete retro | X | — | — |
| Time to complete action items | X | — | — |

### Root cause distribution

| Category | Count | % | Previous % | Change |
|----------|-------|---|------------|--------|
| [Top categories] | X | Y% | — | — |

### Action item health

| Metric | Count |
|--------|-------|
| Total open (linked to active retros) | X |
| By status category: To Do | X |
| By status category: In Progress | X |
| Overdue (past due date) | X |
| Missing due date | X |
| Completed since last review | X |
| Completeness % | X% |

### Action items by team (open, not Done)

| Team (Project) | Total | To Do | In Progress | Overdue | No Due Date |
|----------------|-------|-------|-------------|---------|-------------|
| [Top teams] | X | X | X | X | X |
| **Total** | **X** | **X** | **X** | **X** | **X** |

### Throughput (since last review)

| Metric | Count |
|--------|-------|
| New incidents (Retro Needed = Yes) | X |
| Retros closed | X |
| Net backlog change | +/-X |

### Trend comparison

| Metric | Previous | Current | Change |
|--------|----------|---------|--------|
| Active backlog (Solved) | X | Y | +/-Z |
| In Progress + Completed | X | Y | +/-Z |
| Unassigned Commanders | X | Y | +/-Z |
| Avg lead time (days) | X | Y | +/-Z |
| Overdue action items | X | Y | +/-Z |
| Action item completeness % | X | Y | +/-Z pp |

## Stalled retros (no update > 15 days)

| Key | Summary | Status | Last Updated | Commander | Age (days) |
|-----|---------|--------|-------------|-----------|------------|

## Overdue action items

| Retro | Action Item | Assignee | Due Date | Days Overdue | Status Category |
|-------|------------|----------|----------|-------------|-----------------|

## Data gaps

- [Any metrics not retrieved or with quality issues]
```

## Step 5: Update running metrics log

Append current metrics to `metrics/retro-review-metrics.md`:
- Add new row to each running table
- Bold current period row
- Update alert status
- Note data gaps

Return: "Retro review data ready at `meetings/prep/YYYY-MM-DD-retro-review-data.md`. Run `/ops-review-prep` to combine with CM data into the full prep."

---

## Power BI Model Schema

**Retrospectives** — 36 tables, 61 measures

Key tables:
- `OTHER_PROPERTIES` (38 cols): ISSUE_KEY, SUMMARY, STATUS_NAME, CREATED_DATE, RESOLVED_DATE, CLOSING_DATE, RCA_CATEGORY, RETROSPECTIVE_COMMANDER, INCIDENT_COMMANDER, REVIEWER, APPROVER, IS_REVIEWED, IS_APPROVED, RETROSPECTIVE_STATUS (calculated), Retrospective Leadtime, Actions_Items_Leadtime, SEVERITY, SYSTEM_WIDE_IMPACT, RETROSPECTIVE_NEEDED, RETROSPECTIVE_COMPLETED_DATE, READOUT_DATE, LAST_UPDATE, Retrospective Aging (Days), Incident Aging (Days), Aging Group (calculated)
- `LINKED_ISSUES` (18 cols): ISSUE_KEY, LINKED_ISSUE, LINKED_ISSUE_TYPE, LINKED_ISSUE_STATUS, LINKED_ISSUE_STATUS_CATEGORY, LINKED_ISSUE_DUE_DATE, Days to Due (calculated), LINKED_ISSUE_ASSIGNE, LINKED_ISSUE_SUMMARY, LINKED_ISSUE_CREATED_DATETIME
- `INCIDENTS_DISTINCT` (25 cols): ISSUE_KEY, CREATED_DATE, RESOLUTION_DATE, SEVERITY, INCIDENT_TYPE, RING, STATUS, TEAM_NAME, E2E_FULL_RESOLUTION_TIME, RD_RESOLUTION_TIME, RD_MTTR, INCIDENT_MTTR
- `TEAMS`: ISSUE_KEY, TEAMS
- `Calendar`: shared date dimension
- Pre-built measures in `# Incidents`, `Retrospectives`, `Times Spent` tables

**Measures that fail in DAX queries** (use USERELATIONSHIP internally):
- `# Created Incidents`, `# Solved Incidents` — use direct COUNTROWS with date filters

---

## Tips

- The retro review is a **population snapshot** — always show the full active population, not a date-bounded slice
- **Backlog cutoff:** Only include Solved incidents resolved ≥ 2 days before the ops review date — recently solved ones haven't had time to start a retro
- Throughput (new/closed) uses "since last review" as the temporal window
- Prefer Playwright for Power BI reports — matches what stakeholders see
- Use DAX for drill-down (commander gaps by name, overdue item lists)
- Use Jira for what Power BI misses: stalled retro detail, action item assignees, recent comments
- Action items live across many projects — track via status category, not workflow states
- RFCs linked to RDINCs are recovery actions, not action items — exclude them
- Flag data gaps explicitly — missing due dates, unlinked items, blank RCA categories are signals
- M3.5 (Retrospective Transformation, Ines) may change this process — skill will need updating
