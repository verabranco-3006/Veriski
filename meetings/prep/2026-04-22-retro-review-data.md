# Retrospective Review Data — April 22, 2026
**Population:** All RDINCs with Retrospective Needed = Yes
**Data snapshot:** 2026-04-22 (dry run v3 — Power BI DAX as source of truth)
**Backlog cutoff:** Solved incidents resolved ≤ April 20 (2 days before ops review)

---

## Key findings

### 1. Action Item Discipline Is Eroding — RPM Owns 20 Items With Zero Due Dates

Of 85 open action items across 21 teams, RPM holds the largest share (20 items, 24%) — and every single one lacks a due date. Without due dates, these items are invisible to overdue tracking and will never surface in alerts. RPOR (15 items, 3 overdue, 4 missing due dates) and RDASS (4 items, all 4 overdue) round out the top concern areas.

| Metric | Value |
|--------|-------|
| Open action items (not Done) | 85 |
| Overdue | 18 (21.2%) |
| No due date | 34 (40.0%) |
| **Alert threshold** | **> 5 overdue** |

**Why it matters:** 40% of open action items have no due date — they can't be tracked, can't trigger alerts, and create a false sense of progress. The 18 overdue items include some dating back to 2021 (RDPIM-2167, 1,600 days overdue). The improvement cycle is broken for these items.

**What we're doing about it:** M3.5 (Retrospective Transformation, Ines) is redesigning the retro model to push accountability to R&D teams. The team distribution data gives us a clear picture of which teams need follow-up on action item hygiene.

### 2. Lead Times Signal a Slow Process — 89 Days Average, 130 Days for Action Items

The average retrospective takes 89 days end-to-end. Action items take an additional 130 days to complete after the retro is done. Combined, an incident's improvement cycle can stretch to 7+ months.

| Metric | Days |
|--------|------|
| Avg retrospective leadtime | 88.9 |
| Time to start retro | 21.1 |
| Time to complete retro | 70.3 |
| Time to complete action items | 129.7 |
| **Alert threshold** | **> 60 days avg leadtime** |

**Why it matters:** If it takes 3 months to complete a retro and another 4 months for action items, the improvement arrives 7 months after the incident. By then, the context is cold and the urgency is gone. The 21-day average to even start a retro suggests initial momentum is reasonable, but the 70-day completion time indicates bottlenecks in the review/approval chain.

### 3. Population Is Stable but Heavily Concentrated in "Completed" Status

93 of 112 active retros (83%) sit in "Retrospective Completed" — meaning the retro was approved but action items haven't all been delivered. Only 3 are in backlog, 13 in progress, and 3 in pending stages.

| Metric | Value |
|--------|-------|
| Total RETROSPECTIVE_NEEDED = Yes | 174 |
| Active (excl. Closed, Cancelled, Troubleshooting) | 112 |
| Retrospective Completed | 93 (83.0%) |
| Retrospective Closed | 56 |
| Excluded (Cancelled + Troubleshooting In Progress) | 6 |

**Why it matters:** The bottleneck isn't in doing retros — teams complete them. The bottleneck is in closing the loop on action items. 93 retros are waiting for action items to be delivered. Combined with finding #1 (34 items with no due date, 18 overdue), the "last mile" of the retro process is where discipline breaks down.

### 4. Commander Assignment — 50% Unassigned in Active Pipeline

3 of 6 retros in the active pipeline (In Backlog + In Progress + Pending) have no Commander assigned.

| Metric | Value |
|--------|-------|
| Retros needing Commander (Backlog + In Progress + Pending) | 6 |
| With Commander | 3 (50.0%) |
| Without Commander | 3 (50.0%) |
| **Alert threshold** | **> 40%** |

**Why it matters:** Commanders drive the retro to completion. Half the active pipeline has no owner. While the absolute number is small (6 retros), the rate signals a gap in the intake process.

### 5. Root Cause Distribution — Application and Infrastructure Issues Dominate

Application issues (54, 31%) and Infrastructure issues (50, 29%) account for 60% of all root causes. Configuration issues (37, 21%) round out the top 3.

---

## Metrics

### Retro population snapshot

| RETROSPECTIVE_STATUS | Count | % of Active | Previous | Change |
|---------------------|-------|-------------|----------|--------|
| In Backlog | 3 | 2.7% | — | — |
| Retrospective In Progress | 13 | 11.6% | — | — |
| Pending Review | 2 | 1.8% | — | — |
| Pending Approval | 1 | 0.9% | — | — |
| Retrospective Completed | 93 | 83.0% | — | — |
| **Active total** | **112** | — | — | — |
| Retrospective Closed | 56 | — | — | — |
| Cancelled | 3 | — | — | — |
| Troubleshooting In Progress | 3 | — | — | — |
| **Grand total (Retro Needed = Yes)** | **174** | — | — | — |

> Active = all statuses except Retrospective Closed, Cancelled, and Troubleshooting In Progress.
> No previous period data — retro section not presented on April 16.

### Commander assignment (In Backlog + In Progress + Pending)

| Metric | Count | % |
|--------|-------|---|
| Retros needing Commander (Backlog + In Progress + Pending) | 6 | — |
| With Commander | 3 | 50.0% |
| Without Commander | 3 | 50.0% |

### Lead times

| Metric | Days | Previous | Change |
|--------|------|----------|--------|
| Avg retrospective leadtime | 88.9 | — | — |
| Time to start retro | 21.1 | — | — |
| Time to complete retro | 70.3 | — | — |
| Time to complete action items | 129.7 | — | — |

### Root cause distribution

| Category | Count | % | Previous % | Change |
|----------|-------|---|------------|--------|
| Application issues | 54 | 31.2% | — | — |
| Infrastructure issues | 50 | 28.9% | — | — |
| Configuration issues | 37 | 21.4% | — | — |
| Deployment issues | 16 | 9.2% | — | — |
| Operational Issues | 9 | 5.2% | — | — |
| (blank) | 6 | 3.5% | — | — |
| Tests failed | 1 | 0.6% | — | — |
| Missing feature | 1 | — | — | — |

### Action item health

| Metric | Count |
|--------|-------|
| Action Items Created | 502 |
| Action Items Concluded | 442 |
| Open (not Done) | 85 |
| Overdue (past due date) | 18 |
| Past Due — To Do | 14 |
| Past Due — In Progress | 3 |
| No Due Date | 34 |
| On Due | 30 |
| Completeness % | 88.0% |

> Note: DAX pre-built measures show 17 overdue (14 To Do + 3 In Progress), but the detail query returned 22 overdue items. Difference likely due to measure counting at retro level vs item level, or filter context differences.

### Action items by team (open, not Done)

| Team (Project) | Total | To Do | In Progress | Overdue | No Due Date |
|----------------|-------|-------|-------------|---------|-------------|
| RPM | 20 | 19 | 1 | 0 | **20** |
| RPOR | 15 | 7 | 8 | 3 | 4 |
| RDPIDT | 7 | 6 | 1 | 0 | 1 |
| RDICE | 5 | 4 | 1 | 1 | 4 |
| RDPIB | 5 | 5 | 0 | 0 | 0 |
| RPLAT | 5 | 5 | 0 | 0 | 0 |
| RDASS | 4 | 4 | 0 | **4** | 0 |
| RDSPT | 3 | 3 | 0 | **3** | 0 |
| RCQA | 3 | 2 | 1 | 1 | 1 |
| RSA | 3 | 2 | 1 | 2 | 0 |
| RDODCP | 3 | 3 | 0 | 2 | 1 |
| RDMAST | 2 | 2 | 0 | 0 | 0 |
| RDPEN | 2 | 1 | 1 | 1 | 0 |
| Others (8 teams, 1 each) | 8 | 7 | 1 | 1 | 3 |
| **Total** | **85** | **70** | **15** | **18** | **34** |

> Team derived from Jira project prefix of linked issue key. RPM = all 20 items missing due dates. RDASS = all 4 items overdue.

### Throughput (since last review — Apr 8 to Apr 22)

| Metric | Count |
|--------|-------|
| New incidents in backlog (Solved ≤ Apr 20) | Not available (no Jira query in v3) |
| Retros closed (all action items done) | Not available |
| Net backlog change | Not available |

> Throughput requires comparing current population against previous period. No previous retro data exists (section not presented Apr 16).

### Trend comparison

| Metric | Previous (Apr 16) | Current (Apr 22) | Change |
|--------|-------------------|-------------------|--------|
| Active retros | — | 112 | — |
| In Backlog | — | 3 | — |
| Retrospective Completed | — | 93 | — |
| Unassigned Commanders | — | 3 of 6 (50%) | — |
| Avg leadtime (days) | — | 88.9 | — |
| Overdue action items | — | 18 | — |
| Action item completeness % | — | 88.0% | — |

> No previous period data available for trends — retro section not presented on April 16. This is the baseline.

---

## Overdue action items (detail)

| Retro | Action Item | Type | Status | Due Date | Days Overdue | Assignee |
|-------|------------|------|--------|----------|-------------|----------|
| RDINC-416 | RDPIM-2167 | Bug | To Do | 2021-06-12 | 1,600 | — |
| RDINC-34560 | RDPIM-3484 | Bug | To Do | 2024-12-08 | 620 | — |
| RDINC-29259 | RDPIM-3524 | Bug | To Do | 2024-09-26 | 575 | — |
| RDINC-45314 | RDODCP-55 | Tech Investment | To Do | 2025-08-31 | 236 | — |
| RDINC-37688 | RDSPT-5122 | Tech Investment | Backlog | 2025-09-30 | 206 | — |
| RDINC-43642 | RDODCP-63 | Tech Investment | To Do | 2025-09-30 | 206 | — |
| RDINC-37688 | RDSPT-5162 | Story | Backlog | 2025-09-30 | 206 | — |
| RDINC-37688 | RDSPT-5120 | Tech Investment | Backlog | 2025-09-30 | 206 | — |
| RDINC-49765 | RDPEN-1642 | Team Improvement | To Do | 2025-10-31 | 175 | Tiago Garcia |
| RDINC-35312 | RPOR-22143 | Initiative | Development | 2025-12-31 | 114 | Joao Figueira Gomes |
| RDINC-37688 | RSA-671 | Finding | New | 2025-12-31 | 114 | Vera Branco |
| RDINC-55285 | RDICE-4044 | Story | Ready for Development | 2026-01-30 | 84 | — |
| RDINC-50709 | RDODCP-308 | Spike | To Do | 2026-01-31 | 83 | — |
| RDINC-55778 | RDASS-3471 | Tech Investment | To Do | 2026-01-31 | 83 | — |
| RDINC-49765 | RSA-734 | Finding | Action Plan Definition | 2026-01-31 | 83 | Ines Matos |
| RDINC-55778 | RDASS-2965 | Tech Investment | To Do | 2026-02-28 | 55 | — |
| RDINC-55778 | RDASS-3396 | Discovery | To Do | 2026-02-28 | 55 | — |
| RDINC-41857 | RPOR-22703 | Value Milestone | Development | 2026-03-31 | 24 | Joao Figueira Gomes |
| RDINC-46156 | RPOR-22703 | Value Milestone | Development | 2026-03-31 | 24 | Joao Figueira Gomes |
| RDINC-55285 | RCQA-4936 | Spike | Backlog | 2026-03-31 | 24 | Chris Curtis |
| RDINC-55778 | RDASS-3364 | Discovery | To Do | 2026-03-31 | 24 | Karthik Kanakasabapathy |
| RDINC-52911 | RDMOT-2621 | Story | Waiting (3rd party) | 2026-04-13 | 11 | Chris Carter |

> RDINC-37688 (Pegasus Integration tests failing) has 4 overdue items across RDSPT and RSA projects — single retro driving most of the RDSPT overdue count.
> RDINC-55778 has 4 overdue items across RDASS — all Tech Investment/Discovery items.
> RPOR-22703 appears twice (linked to both RDINC-41857 and RDINC-46156) — same action item linked to two retros.

---

## Data gaps

- **Previous period baseline:** April 16 Ops Review has retro section marked "[not presented]" — no structured retro metrics exist for trend comparison. This is the first period.
- **Throughput:** New incidents and closures since last review not queried in this dry run (requires comparing against previous snapshot)
- **Power BI reports:** Playwright screenshots not captured — browser session was closed. Charts stakeholders see in the Ops Review deck are not visually confirmed.
- **Stalled retros:** Not queried in v3 — available via Jira if needed (v2 showed 90 of 109 stalled, 82.6%)
- **Closed total:** Total number of Closed retros (all-time) = 56 from DAX. Closures in period not measured.
- **Action item count discrepancy:** Pre-built measures show 17 overdue; detail query shows 22. Likely filter context difference — needs investigation.
- **Team names:** Project prefixes used instead of human-readable team names. Consider adding a mapping table in Power BI.

---

## Changes from dry run v2

| What changed | v2 | v3 | Why |
|--------------|----|----|-----|
| Data source | Jira for counts + some DAX | DAX for everything (Power BI as source of truth) | Jira counts don't match Power BI — unreliable for volumes |
| Total population | 110 (Jira) | 174 (DAX) | DAX returns full population including Closed + excluded statuses |
| Active count | 110 | 112 | Correct calculation: 174 - 56 Closed - 3 Cancelled - 3 Troubleshooting |
| RETROSPECTIVE_STATUS values | Simplified names (In Progress, Completed, Closed) | Actual DAX values (Retrospective In Progress, Retrospective Completed, Retrospective Closed) | Match what Power BI model returns |
| New statuses discovered | — | Cancelled (3), Troubleshooting In Progress (3) | Excluded from active population |
| Commander scope | 109 retros assessed | 6 retros assessed (Backlog + In Progress + Pending only) | Correct scope — Completed retros already have commander |
| Action items | Not collected | Full health + team distribution + overdue detail | DAX queries on LINKED_ISSUES table |
| Lead times | Not collected | All 4 measures populated | DAX pre-built measures with RETROSPECTIVE_NEEDED filter |
| Root cause | Not collected | Full distribution | DAX on OTHER_PROPERTIES[RCA_CATEGORY] |
| DAX filter | No filter | RETROSPECTIVE_NEEDED = "Yes" on all queries | Without it, measures return 31K+ incidents |
| Days to Due handling | — | IFERROR(VALUE()) pattern | Column is Text type with "Due Date not Available" |
