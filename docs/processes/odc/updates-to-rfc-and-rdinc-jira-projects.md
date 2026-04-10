---
title: Updates to RFC and RDINC Jira Projects
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/5458198681/Updates+to+RFC+and+RDINC+Jira+Projects
confluence_space: RKB
confluence_page_id: 5458198681
last_synced: 2026-04-09
owner: Process Engineering
---

# Updates to RFC and RDINC Jira Projects

none
To** measure the *****Change Failure Rate***, we need to update our RFC and RDINC Jira projects to ensure the required data is collected.

From the **RFC project**, we will gather the following information:

- 
**Which **changes qualify as actual changes?

- 
**Which **asset was changed?

- 
**Where **was the change applied?

- 
**When **was the change made?

From the **RDINC project**, we will gather the following information:

- 
**Which **asset caused the incident?

- 
**Where **was the incident found?

- 
**When** did the incident happen?

The following tables show the changes we will make in each project to collect this data, as well as other pending changes that we will address at the same time.

:warning:26a0⚠️#FFFAE6
To ensure the accuracy and reliability of this crucial metric, it is **mandatory** that **specific fields** are filled out **accurately** and **completely**.

## RFC updates
**Current**

**New**

**Notes**

---

**Create **new ***Change Category*** field:

- 
Mandatory on issue creation 

- 
Single selection

- 
Options:

- 
Fast Track

- 
Rollback

- 
Promote to Standard

- 
Restart

- 
Retry

- 
Change Configuration

- 
Change Infrastructure

- 
Other Read-only Operation

- 
Other Write Operation

- 
Customer Request

Identify the changes that will be included in the metric.

V6 - What does an ODC Request for Change look like in Jira? 

***Affected Services (List)***

**Replace **by ***Impacted Asset(s) ***field.

- 
Mandatory when :

- 
 Standard RFC : moving to ***Implementing***

- 
 Normal RFC : moving to ***Submitted to CAB***

- 
 Emergency RFC: moving to ***Change Approved***

- 
Multi selection

- 
Keep the list updated with all assets

- 
Replace &quot;Other Services&quot; and &ldquo;NA&rdquo; by **&ldquo;Asset Missing&rdquo;**

New field added: `Specify Missing Asset`, that should be filled when &ldquo;Asset Missing&rdquo; is selected.

- 
this validation will happen on workflow transition together with the ***Impacted Asset(s)*** field validation.

Identify the assets that were changed.

Keep &ldquo;Affected Services (list)&rdquo; as a non-editable field for historical reasons. It will be hidden when empty, which means it will not appear for new RFCs.

***Rings***

**Keep **this field:

- 
Make it mandatory on issue creation

Identify where the change was applied.

***Category Reason for Change***

**Keep **this field, but:

- 
Make it mandatory on issue creation

V6 - What does an ODC Request for Change look like in Jira? 
## RDINC updates
**Current**

**New**

**Details**

***Ring***

**Replace **by ***Rings ***field:

- 
Mandatory when moving to solvedGreen

- 
Multi-selection

- 
Sync with Rootly &ldquo;*Ring*&rdquo; field for incidents that involve the SRE team

The rings affected by the incident.

Keep &ldquo;Ring&rdquo; as a non-editable field for historical reasons. It will be hidden when empty, which means it will not appear for new RDINCs.

**---**

**Add **new ***Incident Type*** field:

- 
Automatically filled by an automation

- 
Mandatory when moving to troubleshooting in progressBlue

- 
Single selection

- 
Options:

- 
Customer Reported

- 
Alert

- 
Internal

- 
System-wide SLO Trigger

- 
Service Specific SLO

Filled automatically by an automation, based on *Labels*.

A validation exists when moving an issue to SolvedGreen, to check if it is filled.

***Affected Services (List)***

**Replace **by ***Impacted Asset(s) ***field.

- 
Mandatory when moving to solvedGreen

- 
Exceptions: 

- 
When ***Incident Type = Alert***

- 
When ***Root Cause Categorization = Customer Issue***

- 
Multi selection

- 
Keep the list updated with all assets

- 
Replace &quot;Other Services&quot; and &ldquo;NA&rdquo; by **&ldquo;Asset Missing&rdquo;**

New field added: `Specify Missing Asset`, that should be filled when &ldquo;Asset Missing&rdquo; is selected.

- 
this validation will happen on workflow transition together with the ***Impacted Asset(s)*** field validation.

The assets that caused the issue.

Keep &ldquo;Affected Services (list)&rdquo; as a non-editable field for historical reasons. It will be hidden when empty, which means it will not appear for new RDINCs.

***Root Cause Categorization***

**Keep **this field, but:

- 
Make it mandatory when moving the issue to solvedGreen

- 
Exception: 

- 
When ***Incident Type = Alert***

***Findings***

**Keep **this field, but:

- 
Remove the requirement for it to be mandatory.

Sync with Rootly &ldquo;*Investigation and troubleshooting findings*&rdquo; field for incidents that involve the SRE team.

***Recovery***

**Rename **this field to ***Resolution***, and:

- 
Remove the mandatory requirement for this field.

- 
Add **workaround **information here.

Sync with the Rootly &ldquo;*Resolution*&rdquo; field for incidents that involve the SRE team.

***Workaround***

**Delete **this field.

***Impact***

**Keep **this field, but:

- 
Remove the requirement for it to be mandatory.

Sync with Rootly &ldquo;*What is the Impact?*&rdquo; field for incidents that involve the SRE team.

**---**

**Add **cancelledGreen status to workflow.

It is possible to move to that status from TEAM ASSIGNED , waiting for customer and TROUBLESHOOTING IN PROGRESSBlue.

**---**

**Add **new ***Cancellation Reason***** **field: 

- 
mandatory when moving to cancelledGreen

- 
selection list

- 
single-selection

Options:
**False positive** - the alert or incident did not represent a real issue.
**Duplicated** - another incident already covers the same event.
**Test / Simulation** - the incident was part of a test, drill, or exercise.
**Created by Mistake** - the incident was opened in error or accidentally.

When choosing the **Duplicated** reason, you must link the incident to the one it duplicates.

R&amp;D only transitions RDINCs to *Solved* in Jira after they have been marked *Solved* in Zendesk.

**R&amp;D is now empowered to move a customer-reported incident to *****Solved ***once they are confident in the proposed solution and have filled the required Jira fields (***Rings**, **Impacted Asset(s)**, **Root Cause Categorization***).
Global Support will be informed once the RDINC status is updated.

When an **Incident is moved to Solved in Zendesk**, the associated RDINC is moved to Solved.

When an Incident is moved to *Solved* in Zendesk, Jira attempts to move the associated RDINC to *Solved*. 
If it cannot do so because the mandatory fields are not filled in (***Rings**, **Impacted Asset(s)**, **Root Cause Categorization***), an alert message appears in the RDINC (under the *Incident Information* tab), and a comment is posted notifying the assignee that these fields must be completed to close the ticket.

When an **Incident is moved to Resolved in Rootly**, the associated RDINC is moved to Solved.

When an Incident is moved to *Resolved* in Rootly, Jira attempts to move the associated RDINC to *Solved*. 
If it cannot do so because the mandatory fields are not filled in (***Rings**, **Impacted Asset(s)**, **Root Cause Categorization***), an alert message appears in the RDINC (under the *Incident Information* tab), and a comment is posted notifying the assignee that these fields must be completed to close the ticket.