---
skill_name: ops-review-prep
title: Operations Review Prep
description: Prepare Process Engineering's contribution to the bi-weekly Operations Review — combines retro and CM data, generates narrative, and publishes Confluence report
---

# Operations Review Prep

Orchestrates the full preparation for Process Engineering's bi-weekly Operations Review contribution.

## Usage

```
/ops-review-prep              → Full prep (runs retro + CM + merge + Confluence)
/ops-review-prep wrap-up      → After meeting: update action items and publish final report
```

**Individual domain skills (can be run independently):**
```
/retro-review-prep            → Retrospective data only
/cm-review-prep               → Change Management data only
```

---

## Context

**What is Operations Review?**

A bi-weekly meeting (Thursdays) where cross-functional teams review operational health across engineering practices. Attendees include SRE, Product Ops, Process Engineering, Release Engineering, Quality, and Value Stream Leaders.

**Process Engineering presents three things:**

1. **Retrospective outcomes** -- population health (RETROSPECTIVE_STATUS breakdown), lead times, action item health by team, overdue items, root cause distribution, commander gaps. Data sourced from Power BI (source of truth for volumes) + DAX drill-down + Jira for detail only.
2. **Change Management outcomes** -- metrics, patterns, compliance signals from the last 15 days
3. **PE roadmap callouts** (as needed) -- initiative rollouts, process changes, announcements for Value Stream Leaders

**Supporting materials:**

- Confluence report page: one per Ops Review, lives under `EEO > Operations Review` space
- Preparation deck: [Google Slides](https://docs.google.com/presentation/d/1RtmVn5nREsRVYg6m6l7XaPXX7outFGVbKnnIMyPjqtc/edit)
- Operations Review deck: [Google Slides](https://docs.google.com/presentation/d/12lxWvZ24Xw1cAPs7XcX7lGgnDN2p86NnKZsnGu18vVA/edit)
- Process Review Scorecard: [Power BI](https://app.powerbi.com/groups/24c7a4b4-f5b6-4977-a972-2fc01644ebc6/scorecards/93fbc79d-57af-49de-a8df-1b3a438b9f78?ctid=1e7930e6-1ca4-40df-ac06-adabc2b139a3&experience=power-bi)

**Confluence space:** `EEO` (spaceId: 1856242996), parent page ID: 5316116528

---

## Narrative Philosophy

Operations Review should drive **accountability and continuous improvement**, not blame. PE's contribution must:

1. **Lead with patterns, not problems** -- frame data as signals that reveal systemic opportunities, not individual failures
2. **Connect to action** -- every data point raised must link to either a V2MOM initiative, an action item, or a recommendation
3. **Speak to Value Stream Leaders** -- they are the primary audience. Frame findings as "what this means for your teams" not "what your teams did wrong"
4. **Show trajectory** -- always include trend data (current vs previous periods) so people see direction, not just snapshots
5. **Close the loop** -- reference what was raised in previous Ops Reviews and what changed since then

The tone is: "Here's what the data tells us, here's what we're doing about it, here's where we need your help."

---

## Mode 1: Prep (default)

### Step 1: Determine review period

- Default: the 15 calendar days ending on the day before the next Thursday
- Ask: "The next Ops Review is Thursday [DATE]. The review period is [START_DATE] to [END_DATE]. Correct?"
- Wait for confirmation before proceeding

### Step 2: Create Jira tracking task (M6.1)

Create a task under the M6.1 epic (RSA-882) to track this ops review preparation as BAU activity.

Use `mcp__claude_ai_Atlassian__createJiraIssue`:
- Project: RSA
- Issue type: Task
- Summary: `Ops Review Prep — [MONTH DAY, YEAR]` (e.g., `Ops Review Prep — May 1, 2026`)
- Description: `Preparation for the [DATE] Operations Review. Review period: [START_DATE] to [END_DATE].`
- Parent/Epic: RSA-882

Store the created issue key (e.g., `RSA-XXX`) — it will be referenced in later steps and closed at the end.

### Step 3: Run domain skills

Run both domain skills to collect and analyze data. Each skill uses the review date differently:

1. **`/retro-review-prep [OPS_REVIEW_DATE]`** -- produces `meetings/prep/YYYY-MM-DD-retro-review-data.md`. Uses the ops review date to calculate the backlog cutoff (Solved incidents resolved ≥ 2 days before). Retros are a **population snapshot** — no date period, just the full active population at that point in time.
2. **`/cm-review-prep [START_DATE] [END_DATE]`** -- produces `meetings/prep/YYYY-MM-DD-cm-review-data.md`. Uses the review period to filter RFCs created/resolved within the window.

If either skill's output already exists (from a prior independent run), read it instead of re-running.

### Step 4: Ask for PE roadmap callouts

Ask: "Any PE roadmap updates or announcements for this Ops Review? (e.g., initiative rollouts, process changes, policy updates)"

Wait for response.

### Step 5: Merge into prep document

Read both domain output files and merge into the unified prep document.

Save to `meetings/prep/YYYY-MM-DD-ops-review-prep.md`:

```markdown
# Ops Review Prep -- [DATE]
**Review period:** [START_DATE] to [END_DATE]

---

## Retrospective Data

[Content from retro-review-data.md -- key findings, metrics (population by RETROSPECTIVE_STATUS, commander assignment, lead times, root cause distribution, action item health + team distribution, overdue detail), trends]

---

## Change Management Data

[Content from cm-review-data.md -- key findings, metrics, trends, compliance signals]

---

## PE Roadmap Callouts

[Announcements, rollouts, or process changes for Value Stream Leaders]

---

## Action Items for Process Engineering

- [ ] [Action from this review]

---

## Talking Points

[3-5 bullet points for verbal delivery during the meeting -- the key messages to land]
```

### Step 6: Generate Confluence report

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

### Step 7: Close Jira tracking task

After Confluence publish is confirmed, transition the M6.1 tracking task (created in Step 2) to Done.

Use `mcp__claude_ai_Atlassian__transitionJiraIssue`:
- Issue key: the `RSA-XXX` key from Step 2
- Transition to: Done

Add a comment to the task with a link to the Confluence page and a one-line summary (e.g., "Published. 53 RFCs, 0 Emergency, incident-driven rate at 20.75%.").

---

## Mode 2: Wrap-up (`/ops-review-prep wrap-up`)

Run after the meeting.

### What to read

1. The prep file at `meetings/prep/YYYY-MM-DD-ops-review-prep.md`
2. Any notes added during the meeting

### What to do

1. **Update action items** -- add new action items from the meeting to the prep file
2. **Update Confluence page** -- if the published page needs corrections or additions based on meeting discussion
3. **Log patterns** -- if any recurring theme emerged, flag for `memory.md` update
4. **Update initiative trackers** -- if any finding connects to an active initiative, add a note to the relevant `_initiative.md`

---

## Tips

- Always show trend data -- a single data point means nothing without context
- Lead with the narrative, support with numbers -- the Confluence page has the raw data, the verbal delivery should tell the story
- Flag compliance signals explicitly -- Emergency misuse, ring distribution inversion, Fast Track spikes are audit-relevant
- Connect findings to V2MOM initiatives -- this shows PE is not just reporting, but actively working on the root causes
- Keep the Confluence report factual and data-driven -- save opinions and recommendations for verbal delivery
- The report should be useful for offline consumption -- stakeholders who miss the meeting should still get value from reading it
