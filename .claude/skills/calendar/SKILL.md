---
skill_name: calendar
title: Calendar View
description: View today's or this week's calendar from Google Calendar
---

# Calendar View

View your Google Calendar schedule parsed into a clean markdown table with conflict detection and focus time estimates.

## Usage

```
/calendar          → today's schedule
/calendar today    → today's schedule
/calendar week     → this week's schedule
```

## Instructions

### Step 1: Fetch events from Google Calendar

**Primary — Google Calendar MCP:**

Use the `claude.ai Google Calendar` MCP server tools to fetch calendar events.

- **today** → list events with `timeMin` = today 00:00 and `timeMax` = today 23:59 (ISO 8601 with timezone)
- **week** → `timeMin` = Monday of current week, `timeMax` = Friday end of day

**Fallback — Playwright (if MCP is not authenticated or unavailable):**

- **today** → navigate to `https://calendar.google.com/calendar/u/0/r/day`
- **week** → navigate to `https://calendar.google.com/calendar/u/0/r/week`

Use `mcp__playwright__browser_navigate` to open the URL. Wait 3 seconds for the page to load using `mcp__playwright__browser_wait_for`. Then take an accessibility snapshot with `mcp__playwright__browser_snapshot` (NOT a screenshot). Events appear as button elements with text like: `"9:30 AM to 10 AM, Meeting Name, Organizer Name, Accepted, No location, Color: Grape"`

### Step 2: Parse events

For each event, extract:
- **Time range** — start and end time
- **Event name** — the meeting title/summary
- **RSVP status** — Accepted, Tentative, Declined, or Not responded
- **Location** — meeting room, video link, or empty
- **Organizer** — who created the event

**SKIP these entries** — do not include in the active events table:
- "Working location" buttons (Playwright only)
- Lunch blocks or meals
- Focus time / Do not disturb blocks
- All-day events that are informational (holidays, OOO notices)

**Track separately:**
- Declined events → list in a "Declined" section
- Tentative events → mark with :warning: in the status column

**Detect conflicts:**
- Compare all active (non-declined) event time ranges
- If any two events overlap, flag them as a conflict

### Step 3: Output as markdown

For each day, output:

```
### [Day of week], [Month] [Day], [Year]

| Time | Event | Status |
|------|-------|--------|
| 09:30–10:00 | Meeting Name | Accepted |
| 10:00–11:00 | Another Meeting | :warning: Tentative |
...

**Conflicts:** [list overlapping events, or "None"]
**Declined:** [list declined events, or "None"]
```

Use 24h format. Use en-dash (–) for time ranges.

### Step 4: Add summary

After all days, add:

```
**Summary:**
- Active events: [count] (excluding declined, focus time, lunch)
- Meeting hours: [total hours]
- Estimated focus time: [hours] ([list gaps ≥ 30 min])
```

Focus time = gaps between meetings that are at least 30 minutes, within working hours (9 AM – 6 PM).

## Tips

- **Prefer MCP** — try Google Calendar MCP first. If it returns an auth error or is unavailable, fall back to Playwright.
- If using Playwright and the browser is not authenticated to Google, tell the user to log in manually and retry.
- If the Playwright snapshot is empty or shows a login page, say so clearly — don't guess at events.
- For week view, organize events by day with a section header per day.
- Keep output clean and scannable — this feeds into `/morning` and daily planning.