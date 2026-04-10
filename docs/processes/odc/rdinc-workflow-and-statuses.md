---
title: RDINC Workflow and Statuses
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/5600378890/RDINC+Workflow+and+Statuses
confluence_space: RKB
confluence_page_id: 5600378890
last_synced: 2026-04-09
owner: Process Engineering
---

# RDINC Workflow and Statuses

**Version Control - **Current Version - 9.0 /  Release Date - 
none## Workflow overview### Workflow diagram
### Status description
**Process stage**

**Jira Status**

**Description**

**Incident Recovery**

backlog

**A new incident** is on the R&amp;D ODC Incidents board backlog waiting to be assigned to a team.

Team Assigned

A new Incident was **assigned to an R&amp;D team**.

Troubleshooting in progressBlue

The incident is **being worked on** by an R&amp;D team member or the **incident is reopened** by the customer, via Zendesk.

waiting for Customer

The incident that is **pending information from the** **Customer** - information will be gathered and analyzed first by Global Support before sending it back to R&amp;D

SolvedGreen

The normal status of the service has been restored, so the incident is **Solved on R&amp;D side** due to one of the following reasons:

- 
Workaround/fix was provided and the Customer accepted;

- 
Ring Promotion was performed successfully

- 
Not supported / by design / not a platform issue

- 
The SRE Team marked the incident as *Resolved* in Rootly

- 
The original Zendesk ticket was marked as *Solved *by the Global Support team.

cancelledGreen  

An incident may be **cancelled **for any of the following reasons:

**False positive** &mdash; the alert or incident did not represent a real issue.
**Duplicated** &mdash; another incident already covers the same event.
**Test / Simulation** &mdash; the incident was part of a test, drill, or exercise.
**Created by Mistake** &mdash; the incident was opened in error or by accident.

**Retrospective**

Retrospective In progressBlue  

Retrospective is **being worked** on by the teams.

Retrospective completedGreen  

All activities of Retrospective** are completed** and all the relevant information is identified.

**Root Cause is identified** and all the** improvement opportunities / bugs** have been noted down and linked to the RDINC.

The RDINC should stay in this status until all the **linked blocking **tasks are completed.

ClosedGreen  

**All the improvement actions **identified in the Retrospective and linked to the RDINC have been **delivered into Production.**

### Workflow rules
When transitioning between Jira workflow statuses, certain criteria must be met, particularly regarding mandatory fields:

**From Status**

**To Status**

**Validators**

---

backlog  

***Summary and Incident Type ***fields are mandatory

Any status 

team assigned

---

Any status

troubleshooting in progressBlue

---

Any status  

waiting for costumer  

---

waiting for costumer /  troubleshooting in progressBlue  

solvedGreen  

***Rings, Impacted Asset(s) and Root Cause Categorization ***fields are mandatory

Exceptions:

- 
When ***Incident Type = Alert***

- 
When ***Root Cause Categorization = Customer Issue***, ***Impacted Asset(s)*** is not mandatory.

- 
If ***Impacted Asset(s) = Asset Missing***, ***Specify Missing Asset*** field is also mandatory.

solvedGreen  

closedGreen

---

**Incidents with system-wide impact **(`System-wide impact? = Yes`)

solvedGreen  

retrospective in progressBlue

---

retrospective in progressBlue  

retrospective completedGreen  

***RCA/Post Mortem URL, Reviewer, Reviewed?, Approver, Approved? ***fields are mandatory

retrospective completedGreen  / solvedGreen 

closedGreen

All issues linked to the current issue through any **link type must be in a Final Status**.

**Canceling an Incident**

team assigned / waiting for costumer  / troubleshooting in progressBlue  

cancelledGreen

***Cancellation Reason*** field is mandatory