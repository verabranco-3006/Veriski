---
name: morning
description: Start your day with a structured morning routine
user-invokable: true
---

# Morning Routine

This skill helps you start your day with a structured morning routine.

## Instructions

Create today's daily note in `log/daily/` with the filename format YYYY-MM-DD.md (e.g., 2026-01-24.md).

**Morning flow:**

1. Say "Bom dia Vera"
2. Share a motivational sentence to give confidence to win the day
3. Get the 3 most important topics to work on today
4. **Show today's calendar:**
   - **Primary:** Fetch today's events using the `claude.ai Google Calendar` MCP server tools (list events for today's date range)
   - **Fallback:** If the MCP is not authenticated or unavailable, use Playwright to navigate to `https://calendar.google.com/calendar/u/0/r/day`, take an accessibility snapshot (`mcp__playwright__browser_snapshot`), and parse events from the snapshot
   - Parse each event: extract time, title, attendees, RSVP status, location
   - Skip lunch blocks, focus time, all-day informational events (holidays, OOO)
   - For each meeting with a person, check if `people/@Name.md` exists and pull recent context
   - Flag which meetings need prep (1:1s, staff meetings, skip-levels)
   - Present calendar in clean format with time, title, attendees, and prep status
   - Detect and flag any scheduling conflicts
6. Ask the following questions one at a time, wait for response before moving to the next:
   - Which initiatives or projects are you focusing on today? What are your top priorities?
   - Any specific meeting I should help you get context with?

After answers are provided, create the daily note with:
- Date and day of week as the title
- Top priorities as a checklist
- Brief context for any specific meetings

Keep the format clean and scannable.

## Tips

- Keep the greeting brief and actionable
- Focus on what matters today
- Don't overwhelm with too many tasks
- Be encouraging and supportive
- Calendar is fetched from Google Calendar via MCP — if not authenticated, prompt user to run `/mcp`
- For standalone calendar view, use `/calendar today`
