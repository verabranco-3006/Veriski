---
skill_name: staff-prep
title: Staff Meeting Prep
description: Prepare for leadership team or staff meetings with context, agenda, and decisions needed
---

# Staff Meeting Prep

This skill manages the full lifecycle of your weekly staff meeting: prep, notes, and summary.

## Usage

```
/staff-prep              → Generate prep for this week's meeting
/staff-prep wrap-up      → After meeting: generate Slack summary and update master doc
```

---

## Source of Truth

The master doc lives at:
`meetings/recurring/staff-meeting/recurring-staff-meeting.md`

Weekly prep files go in:
`meetings/recurring/staff-meeting/YYYY-MM-DD-staff-meeting-prep.md`

Raw meeting notes (if captured separately) go in:
`meetings/raw/YYYY-MM-DD-staff-meeting.md`

---

## Mode 1: Prep (default)

### What to read

1. `meetings/recurring/staff-meeting/recurring-staff-meeting.md` — master doc with carried forward topics, running topics, open action items, parking lot
2. The most recent prep file in `meetings/recurring/staff-meeting/` — to see what was/wasn't covered last time
3. `initiatives/_dashboard.md` — active initiative status
4. Recent daily notes from `log/daily/` (past 5 days) — what's changed since last meeting
5. `goals/90_day.md` — current priorities
6. `teams/health_tracker.md` (if it exists) — team health overview
7. `decisions/decision_log.md` (if it exists) — pending decisions

### What to ask

One question at a time, wait for response:

1. Any specific topics or decisions you want to add this week?
2. Anything happening in the org that needs addressing? (Reorgs, incidents, launches, morale)

### What to generate

Create the prep file at `meetings/recurring/staff-meeting/YYYY-MM-DD-staff-meeting-prep.md`:

```markdown
# Staff Meeting Prep — YYYY-MM-DD

**Attendees:** Vera, Inês, Laura, Paulo

**⚠️ REMINDER: Check if AI Companion is on to record the call content**

---

## Context Since Last Meeting

[Gather new context from daily notes, initiative updates, and any relevant developments since the last staff meeting. Include key work accomplished, decisions made outside the meeting, and status changes on initiatives.]

## Open Action Items (from previous meeting)

[Pull from master doc — ALL items still open with owners and deadlines. Mark status: pending, in progress, or blocked. Ask Vera for status on any item that's past its deadline.]

## Carried Forward (not covered last meeting)

[Pull from master doc's "Carried Forward" section AND from the previous prep file's "Not Covered" section. For each topic, include the full discussion points and outcome needed — don't just list titles, bring the substance so the team can pick up where they left off.]

## Running Topics

[Pull from master doc — ongoing topics that need recurring attention. Include any updates since last discussed.]

## New Topics

### [Topic — most important first]
**Goal:** [Decision, alignment, or information share]
**Context:** [Brief background]
**Ask:** [Specific ask of the group]

## Initiative Updates

[Quick status from _dashboard.md — one line per active initiative]

---

## Meeting Notes

*Add notes during the meeting below*

### Topics Discussed


### Decisions Made


### Not Covered — Carry Forward


### New Action Items

```

### Rules

- Put the hardest topic first — energy is highest at the start
- Every agenda item must have a clear "ask" — no topics without purpose
- Keep to 3-5 agenda items max — more than that and nothing gets depth
- Connect topics to 90-day goals when possible
- Always include the "Meeting Notes" section at the bottom — this is where notes go during the meeting

---

## Mode 2: Wrap-up (`/staff-prep wrap-up`)

Run this after the meeting, once notes have been added to the prep file.

### What to read

1. The current week's prep file in `meetings/recurring/staff-meeting/`
2. `meetings/recurring/staff-meeting/recurring-staff-meeting.md` — master doc
3. `writing_style.md` — for the Slack summary

### What to do

**Step 1: Generate Slack summary**

Read `writing_style.md` and draft a Slack message for the team channel. Format:

```
[Staff Meeting | YYYY-MM-DD]
Hello team :wave:

**Topics discussed:**
- [Topic]: [One-line conclusion or decision]
- [Topic]: [One-line conclusion or decision]

**Action items:**
- [ ] [Action] — @Owner [deadline if any]
- [ ] [Action] — @Owner [deadline if any]

**Pending for next meeting:**
- [Topic not covered]
- [Topic not covered]
```

Rules for the Slack summary:
- Follow writing_style.md — use my openers, closings, phrases
- Keep it scannable — one line per topic, no paragraphs
- Action items must have an owner
- No fake enthusiasm, no filler

Show the draft and ask if I want to adjust before posting.

**Step 2: Update master doc**

After Slack summary is approved, update `recurring-staff-meeting.md`:

1. **Key Decisions & Patterns** — add this week's decisions under a new date header
2. **Open Action Items** — remove completed items, add new ones from meeting
3. **Running Topics** — remove topics that were resolved, keep active ones
4. **Carried Forward** — update with topics not covered this week
5. **Previous Meetings** — add link to this week's prep file and raw notes (if they exist)

---

## Tips

- The prep file doubles as the meeting notes file — no need to create a separate raw notes file unless preferred
- Speed matters during the meeting — keep notes as fragments, clean up during wrap-up
- The master doc is the single source of truth between meetings — everything flows from and back to it
- If a topic has been carried forward for 3+ meetings, flag it as at risk of being dropped
