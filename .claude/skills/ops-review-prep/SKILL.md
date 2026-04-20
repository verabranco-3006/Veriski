---
skill_name: ops-review-prep
title: Operations Review Prep
description: Prepare Process Engineering's contribution to the bi-weekly Operations Review — data analysis, narrative, and Confluence report
---

# Operations Review Prep

This skill prepares Process Engineering's contribution to the bi-weekly Operations Review meeting.

## Usage

```
/ops-review-prep              → Prepare for the next Ops Review
/ops-review-prep wrap-up      → After meeting: update action items and publish final report
```

---

## Context

**What is Operations Review?**

A bi-weekly meeting (Thursdays) where cross-functional teams review operational health across engineering practices. Attendees include SRE, Product Ops, Process Engineering, Release Engineering, Quality, and Value Stream Leaders.

**Process Engineering presents three things:**

1. **Retrospective outcomes** — metrics, backlog health, key findings from the last 15 days
2. **Change Management outcomes** — metrics, patterns, compliance signals from the last 15 days
3. **PE roadmap callouts** (as needed) — initiative rollouts, process changes, announcements for Value Stream Leaders

**Supporting materials:**

- Confluence report page: one per Ops Review, lives under `EEO > Operations Review` space
- Preparation deck: [Google Slides](https://docs.google.com/presentation/d/1RtmVn5nREsRVYg6m6l7XaPXX7outFGVbKnnIMyPjqtc/edit)
- Operations Review deck: [Google Slides](https://docs.google.com/presentation/d/12lxWvZ24Xw1cAPs7XcX7lGgnDN2p86NnKZsnGu18vVA/edit)
- Retrospective Management Dashboard: [Power BI](https://app.powerbi.com/groups/me/apps/3a45f9da-1b76-4e56-8d53-f5ecca33e50c/reports/51c81030-b36b-4d75-a348-2ab5e4dff49a/e92ea0cac0e60f2d54a8?ctid=1e7930e6-1ca4-40df-ac06-adabc2b139a3&experience=power-bi)
- Process Review Scorecard: [Power BI](https://app.powerbi.com/groups/24c7a4b4-f5b6-4977-a972-2fc01644ebc6/scorecards/93fbc79d-57af-49de-a8df-1b3a438b9f78?ctid=1e7930e6-1ca4-40df-ac06-adabc2b139a3&experience=power-bi)

**Data sources:**

- Jira RDINC project (retrospective/incident data) → fed into Power BI dashboards
- Jira RFC project (change management data) → fed into Power BI dashboards
- Power BI Service (cloud dashboards) — the source of truth for visual data shared with stakeholders

**Confluence space:** `EEO` (spaceId: 1856242996), parent page ID: 5316116528

---

## Narrative Philosophy

Operations Review should drive **accountability and continuous improvement**, not blame. PE's contribution must:

1. **Lead with patterns, not problems** — frame data as signals that reveal systemic opportunities, not individual failures
2. **Connect to action** — every data point raised must link to either a V2MOM initiative, an action item, or a recommendation
3. **Speak to Value Stream Leaders** — they are the primary audience for PE's section. Frame findings as "what this means for your teams" not "what your teams did wrong"
4. **Show trajectory** — always include trend data (current vs previous periods) so people see direction, not just snapshots
5. **Close the loop** — reference what was raised in previous Ops Reviews and what changed since then

The tone is: "Here's what the data tells us, here's what we're doing about it, here's where we need your help."

---

## Mode 1: Prep (default)

### Step 1: Determine review period

- Default: the 15 calendar days ending on the day before the next Thursday
- Ask: "The next Ops Review is Thursday [DATE]. The review period is [START_DATE] to [END_DATE]. Correct?"
- Wait for confirmation before proceeding

### Step 2: Gather previous context

Read the most recent Ops Review Confluence report to establish baselines for trend comparison:

1. Use `mcp__claude_ai_Atlassian__searchConfluenceUsingCql` to find the latest report:
   - CQL: `ancestor = 5316116528 AND type = page ORDER BY created DESC`
   - Space: EEO
2. Read the most recent page with `mcp__claude_ai_Atlassian__getConfluencePage` (markdown format)
3. Extract the key metrics from the previous report for trend comparison:
   - Retrospective: active backlog count, unassigned Commanders, average lead time
   - Change Management: incident-driven RFC rate, Normal Planned %, Fast Track %, Emergency count, ring distribution

### Step 3: Collect current data

**Option A: Power BI (preferred — when MCP server is available)**

Use the Power BI MCP server tools to query the published datasets on Power BI Service:
- Retrospective Management Dashboard: backlog metrics, lead times, status distribution
- Change Management Dashboard: RFC volumes, type distribution, ring distribution, risk classification

**Option B: Jira queries (fallback)**

Use `mcp__claude_ai_Atlassian__searchJiraIssuesUsingJql` to pull data from Jira directly.

**Retrospective data (RDINC project):**

Query active retrospectives:
```
project = RDINC AND "Retrospective Status" is not EMPTY AND "Retrospective Status" not in (Closed, Done, "Not Applicable") ORDER BY created DESC
```

Extract:
- Total active retrospective count
- Count without Commander assigned
- Count pending review (waiting for Reviewer)
- Lead time distribution (days from creation to current status)

**Change Management data (RFC project):**

Query RFCs created in review period:
```
project = RFC AND created >= "[START_DATE]" AND created <= "[END_DATE]" ORDER BY created DESC
```

Extract:
- Total RFC count by type (Standard, Normal, Emergency)
- Incident-linked RFCs (linked to RDINC issues)
- Fast Track usage count
- Ring distribution per execution
- Risk classification distribution
- System-wide impact classification for Emergencies

**Option C: Manual input**

If neither Power BI nor Jira queries return usable data, prompt the user:
- "Please share the key numbers from the Power BI dashboards. I need: [list of metrics]"

### Step 4: Ask for PE roadmap callouts

Ask: "Any PE roadmap updates or announcements for this Ops Review? (e.g., initiative rollouts, process changes, policy updates)"

Wait for response.

### Step 5: Generate the analysis

For each section, apply the analysis vectors below.

**Retrospective Analysis Vectors:**

| Vector | What to report | Alert threshold |
|--------|---------------|-----------------|
| Backlog volume | Active count + trend vs previous | Increase > 10% |
| Commander assignment | Count without Commander + % of total | > 40% unassigned |
| Lead time | Average days from creation to close | > 60 days |
| Review bottleneck | Count pending review with no Reviewer | > 5 stalled |
| Throughput | Closed in period vs new in period | Net increase |

**Change Management Analysis Vectors:**

| Vector | What to report | Alert threshold | V2MOM link |
|--------|---------------|-----------------|------------|
| Incident-Driven RFC Rate | % of RFCs used for incidents | > 35% | — |
| Normal Planned Usage | % of Normal Changes for planned ops ("Shadow SDLC") | > 60% | M2.1 |
| Fast Track Usage | % of changes using Fast Track | > 5% | M2.2 |
| Emergency Volume | Count + system-wide impact compliance | > 3 per period | — |
| Emergency Classification | RFCs marked Emergency without system-wide impact | Any non-compliant | — |
| Ring Distribution | Execution volume per ring (should decrease toward GA) | GA > OSALL | — |
| Risk Classification | Low Risk % + paradoxes (Low Risk + Emergency) | Any paradox | — |

**Narrative structure for each finding:**

1. **What the data shows** — the metric and its value
2. **How it compares** — trend vs previous periods (use table format)
3. **Why it matters** — the risk, compliance, or operational implication
4. **What we're doing about it** — link to V2MOM initiative or action item
5. **What we need from you** (if applicable) — specific ask to Value Stream Leaders

### Step 6: Generate outputs

**Output 1: Local prep document**

Save to `meetings/prep/YYYY-MM-DD-ops-review-prep.md`:

```markdown
# Ops Review Prep — [DATE]
**Review period:** [START_DATE] to [END_DATE]

---

## Retrospective Data

[Analysis with metrics, trends, and narrative per vector]

### Key findings
- [Finding 1]
- [Finding 2]

### Trend comparison

| Metric | Previous | Current | Change |
|--------|----------|---------|--------|
| Active backlog | X | Y | +/-Z |
| Unassigned Commanders | X | Y | +/-Z |
| Avg lead time (days) | X | Y | +/-Z |

---

## Change Management Data

**Period:** [START_DATE] to [END_DATE] | **Total RFCs:** X (Y Standard, Z Normal, W Emergency)

[Analysis with metrics, trends, and narrative per vector]

### Key findings
1. [Finding with narrative — What + Trend + Why + Action]
2. [Finding with narrative]
3. [Finding with narrative]

### Trend comparison

| Metric | [Period -2] | [Period -1] | Current | Change |
|--------|-------------|-------------|---------|--------|
| Incident-Driven RFC Rate | X% | Y% | Z% | +/-pp |
| Normal Planned % | X% | Y% | Z% | +/-pp |
| Fast Track % | X% | Y% | Z% | +/-pp |
| Emergency count | X | Y | Z | +/-N |

### What's going well
- [Positive signals]

---

## PE Roadmap Callouts

[Announcements, rollouts, or process changes for Value Stream Leaders]

---

## Action Items for Process Engineering

- [ ] [Action from this review]

---

## Talking Points

[3-5 bullet points for verbal delivery during the meeting — the key messages to land]
```

**Output 2: Confluence report draft**

Generate the Confluence page content matching the established format (see previous reports). Include:
- Supporting Materials section with dashboard links
- Retrospective Data section with narrative
- Change Management Data section with narrative and tables
- PE Roadmap callouts (if any)
- Action items section

Ask: "Ready to publish to Confluence? I'll create the page under the Operations Review space."

If approved, use `mcp__claude_ai_Atlassian__createConfluencePage` to publish:
- Space: EEO (spaceId: 1856242996)
- Parent page: 5316116528
- Title: `[DATE]` (e.g., `[April 30, 2026]`)
- Format: matches previous reports

---

## Mode 2: Wrap-up (`/ops-review-prep wrap-up`)

Run after the meeting.

### What to read

1. The prep file at `meetings/prep/YYYY-MM-DD-ops-review-prep.md`
2. Any notes added during the meeting

### What to do

1. **Update action items** — add new action items from the meeting to the prep file
2. **Update Confluence page** — if the published page needs corrections or additions based on meeting discussion
3. **Log patterns** — if any recurring theme emerged, flag for `memory.md` update
4. **Update initiative trackers** — if any finding connects to an active initiative, add a note to the relevant `_initiative.md`

---

## Power BI Integration (Enhancement — Priority)

**Status:** Pending setup

The skill should use Power BI Service (cloud) dashboards as the primary data source. This requires:

1. **Remote MCP server:** `https://api.fabric.microsoft.com/v1/mcp/powerbi`
   - Needs Power BI admin to enable tenant setting: "Users can use the Power BI Model Context Protocol server endpoint (preview)"
   - Uses HTTP transport with Azure AD authentication
   - Connects to published datasets on Power BI Service

2. **What it enables:**
   - Direct DAX queries against the published datasets (same data stakeholders see)
   - Visual consistency — data matches what's on the shared dashboards
   - No manual data entry or Jira query approximations

3. **To configure (once admin enables it):**
   ```
   claude mcp add powerbi-remote --transport http https://api.fabric.microsoft.com/v1/mcp/powerbi
   ```

4. **Fallback chain:** Power BI Service → Jira direct queries → manual input

**Action needed:** Request Power BI admin to enable the MCP server tenant setting.

---

## Tips

- Always show trend data — a single data point means nothing without context
- Lead with the narrative, support with numbers — the Confluence page has the raw data, the verbal delivery should tell the story
- Flag compliance signals explicitly — Emergency misuse, ring distribution inversion, Fast Track spikes are audit-relevant
- Connect findings to V2MOM initiatives — this shows PE is not just reporting, but actively working on the root causes
- Keep the Confluence report factual and data-driven — save opinions and recommendations for verbal delivery
- The report should be useful for offline consumption — stakeholders who miss the meeting should still get value from reading it
