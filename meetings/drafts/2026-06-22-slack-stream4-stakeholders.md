[Stream 4 | Day-0 Emergency Response — Process & Implementation Design ready for review] :shield:

Hi team! :slightly_smiling_face:

We've completed a significant update to the Day-0 emergency response process and the Jira implementation design this week. Here's what's ready for your review:

**What changed**
- Track 1 / Track 2 replaced by named sections: **Technical Triage** and **Communication Layer** — cleaner framing, same intent
- Day-0 classification criteria formalised, aligned to CISA BOD 26-04
- Jira workflow redesigned: **single Exposure artifact** replaces the Triage + Fix two-ticket model — same workflow for standard and Day-0 cases, fields drive the branching
- XMAN closure model defined: `Contained` is a milestone (Time to Containment captured), ticket stays open through Phase 2, MTTR = Closed − Declaration for both paths

**What we need from you**
- Review the process and flag anything that doesn't match your operational reality
- Validate the open questions assigned to you in the Open Questions document


**Where to review**
- Process v0.7: https://outsystemsrd.atlassian.net/wiki/spaces/EEO/pages/6400573923/Emergency+Vulnerability+Response+Process
- Open questions: https://outsystemsrd.atlassian.net/wiki/spaces/EEO/pages/6474203689/To-Be+-+XMAN+Jira+Project

What do you think? Happy to walk through it together if it's easier than async. :rocket:
