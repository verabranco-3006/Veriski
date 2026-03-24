---
skill_name: prep1o1
title: Prep 1:1
description: Prepares a 1:1 meeting with context, action items, wins, and talking points
---

# Prep 1:1

This skill prepares you for a 1:1 by pulling together context about the person, open action items, recent wins, and feedback — then generates a prep document.

## Instructions

Ask me:

1. Who's the 1:1 with?

After I answer, gather context from these sources:

### Person Note
- Read `people/@[Person Name].md` if it exists
- If no person note exists, tell me and offer to create one after the 1:1

### Action Items
- Search all files in `log/daily/`, `log/weekly/`, and `meetings/` for open action items (`- [ ]`) that mention the person's name
- Include any tasks tagged with their name or team

### Recent Wins & Feedback
- Search `log/daily/` and `log/weekly/` for wins (`- [w]`) or feedback (`- [!]`) mentioning the person
- Search `meetings/` for any notes from previous 1:1s with them

### Team Context
- Check `teams/` for any files related to their team
- Check `initiatives/active.md` for initiatives they're involved in

### Goals Context
- Read `goals/90_day.md` to identify priorities that connect to this person's work

Present what you found, then ask:

2. Anything specific you want to discuss or follow up on?

After I answer, generate the prep document and output it directly (don't save to a file). Format:

```markdown
# 1:1 Prep — @[Person Name]
*[Date]*

## Context
[Brief summary of their current situation — role, team, what they're working on]

## Open Action Items
[All open tasks involving them, with source file references]
*If none found: "No open action items found."*

## Recent Wins & Feedback
[Any wins or feedback documented about them]
*If none found: "Nothing documented recently."*

## Talking Points
- [Derived from action items, recent context, and my specific topics]
- [Connect to 90-day goals where relevant]

## Questions to Ask
- [2-3 suggested questions based on context — career, blockers, team dynamics]

## Notes
[Empty section to fill during the meeting]
```

After showing the prep, ask:

3. Want me to save this to `meetings/raw/[date]-1o1-[name].md`?

## After the Meeting (Direct Reports Only)

Check if this person is a direct report by looking at their person file for `Reports to: Vera Branco`. If they are a direct report, after the prep document is created or after the meeting, ask:

4. Ready to create the OutPerform note? Share your meeting notes or key discussion points.

After they provide the meeting notes, generate an OutPerform-formatted note following this structure:

```markdown
**1:1 with [Person Name] — [Date in format: Month DD, YYYY]**

**Key Outcomes:** [1-2 sentence summary of the main decisions, shifts, or agreements from this 1:1]

**[Topic 1 Header]:**
[2-4 sentences describing the first major discussion topic and any decisions or insights]

**[Topic 2 Header]:**
[2-4 sentences describing the second major discussion topic and any decisions or insights]

**[Topic 3 Header]:**
[2-4 sentences describing additional topics as needed]

**Context:** [1-2 sentences providing relevant background — how long they've been on the team, current role, what they're working on, or any relevant situational context]

**Next Steps:**
- [Action item with owner] - [Owner name]
- [Action item with owner] - [Owner name]
- [Continue for all next steps identified]
```

### OutPerform Note Guidelines:

- **Key Outcomes:** Should capture the most important decision, shift, or agreement from the meeting
- **Topic Headers:** Use 2-4 descriptive headers that capture the main themes discussed (e.g., "Managing Onboarding Pressure", "Asking for Help Earlier", "Collaborative Work with Inês", "Career Direction Clarity", "Team Enablement Initiative")
- **Topic Content:** Each topic should be 2-4 sentences describing what was discussed and any outcomes
- **Next Steps:** Clear action items with owner names, formatted as bullet points with dashes
- **Tone:** Professional, direct, focused on outcomes and patterns
- **Length:** Keep each section concise — this is a summary for the record, not a transcript

After generating the OutPerform note, ask:

5. Want me to add this to `people/@[Person Name].md` under their 1:1 History section?

If they say yes, add the OutPerform note to their person file under `## 1:1 History` (create the section if it doesn't exist), and update the `*Last updated:*` date at the top of the file.

## Tips

- If the person note doesn't exist, that's a signal — create one after the 1:1
- Prioritize action items that are overdue or recurring
- Connect talking points back to 90-day goals when possible
- Suggest questions that go beyond status updates — ask about blockers, growth, team health
- Keep the prep scannable — this should take 2 minutes to read before walking into the meeting
- The OutPerform note (for direct reports) should focus on key themes and outcomes, not be a transcript
- OutPerform notes should capture patterns (e.g., "Laura only asks for help when stress is high")
- Always include Next Steps with clear ownership in OutPerform notes
