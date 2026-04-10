---
title: What does an ODC RPM look like in Jira?
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/5036804833/What+does+an+ODC+RPM+look+like+in+Jira
confluence_space: RKB
confluence_page_id: 5036804833
last_synced: 2026-04-09
owner: Process Engineering
---

# What does an ODC RPM look like in Jira?

12falsenonelisttrue# Problem Record Workflow by Status
## Meaning of each possible Jira status
 New 

UnderBlue 
INVESTIGATIONBlue 

InvestigationBlue 
COMPLETEDBlue 

release plannedBlue 

ClosedGreen 

Initial status for problem records.

Status used for problem records that are assigned and being investigated.

Problem record with no workaround and root cause found yet.

Status used for problem records that have been analyzed and:

- 
have the root cause identified;

- 
a workaround is defined, if any;

- 
new issues (Bug, Story, &hellip;) were created under the problem to solve it.

The fix has been implemented and is ready to be released. 

All the respective development tasks are DONEGreen.

Status used for problem records that have no more actions.

**Final Status **with the following options:

- 
**Fixed:** Status used for problem records that have their root cause mitigated (change implemented).

- 
**Duplicated:** duplicated problem.

- 
**Rejected:** the Problem Coordinator decided to reject the problem record e.g.: was created by mistake or it is not a problem.

- 
**Not fixed with Known Error: **being the Jira issue &ldquo;our Known Error&rdquo;.

- 
**Inconclusive Investigation:** Investigation is halted due to a lack of information to pursuit the problem record.

- 
**Waiting for Occurrences**: Only applies to O11 Problem Records, and should not be used in ODC context.

## What to do in each *Status*?Status &ldquo;Under Investigation&rdquo;760
The Problem Record is assigned (fill in the &ldquo;**Assignee**&rdquo; field) to begin its investigation, and the **&quot;Problem Description Customer Facing&quot;** has already a detailed description of the issue, that will be visible for the Customer.

As an outcome of this investigation, the root cause, a workaround (if any), or a list of tasks that need to be completed to fix the problem may emerge. As soon as you have all the information you need, and you were able to proceed, fill the [Investigation section](https://outsystemsrd.atlassian.net/wiki/spaces/EEO/pages/edit-v2/4408050001#Investigation-section):

- 
Fill in the &ldquo;**Root Cause**&rdquo;, if you investigated it.

- 
Fill in the** **&ldquo;**Workaround available**&rdquo;- the answer is **&ldquo;yes&rdquo;** for problem records that have a defined and validated workaround. Otherwise, the answer is **&ldquo;no&rdquo;**.

- 
Fill in the &ldquo;**Workaround**&ldquo;,** **if there is any.

Also, add some information in the &ldquo;**Description**&rdquo;, and &ldquo;**How to confirm you're affected**&ldquo;** **fields. (Have in mind that this last one will be visible to the Customer.)

**A workaround is not a fix.** There are some use cases where there are no valid workarounds and the only option available would be, for example, to update the version in use. If this is the case, it should be clearly stated that a workaround is not available.
Status &ldquo;Investigation Completed&rdquo;760
At this stage, you have finally identified the **root cause and/or workaround**. All the findings should be registered in the respective fields (see [Investigation section](https://outsystemsrd.atlassian.net/wiki/spaces/EEO/pages/edit-v2/4408050001#Investigation-section)). It may be necessary to review the **&ldquo;Product Categorization&rdquo;** to be in line with the root cause found.

During the investigation, you may come to different conclusions:

- 
The problem is to be fixed: In this case, ensure that all necessary **development tasks** (bugs, stories, improvements &hellip;), if any, to implement the fix are created under the ODC RPM, or ensure they are linked through the &ldquo;Link Issue&rdquo; option.
**Leave the problem record in the Status &ldquo;Investigation Completed&rdquo; until all development work is &ldquo;done&rdquo;.**

You will then write the ***Release Note***, fill the ***Fix Version*** field if applicable, and move the issue to **&ldquo;Release Planned&rdquo;**, with the ***Status Reason List = Fixed*****.**

Read more information about how to write *Release Notes* here: Guidelines for ODC Problem Management fields.

- 
The problem will not be fixed or it is a duplicate. Check ***Status &ldquo;Closed&rdquo;*** information below, for more information about these 2 options.

 

note1002c3bc-805a-4a8a-a1af-11fde9bd56b0
There may be cases in which a problem is assigned to a Team and the **development tasks are shared with multiple teams**. Regardless, the problem record is always the responsibility of the team assigned to the ticket and this team must ensure that it is closed as soon as possible.

There may be cases in which a problem is assigned to a Team and the **development tasks are shared with multiple teams**. Regardless, the problem record is always the responsibility of the team assigned to the ticket and this team must ensure that it is closed as soon as possible.

Status &ldquo;Release Planned&rdquo;760
Leave the Problem Record in the Status &ldquo;Investigation Completed&rdquo; until all development work is &ldquo;done&rdquo;, and then move it to &ldquo;Release Planned&rdquo;.

Confirm the **Release Note is well written** and that &ldquo;**Fixed**&rdquo; is selected in the ***Status Reason List***.

When no more actions are needed in order to close the problem, there are currently 2 options:

- 
If you've submitted the Pull Request using the RPM Jira ID, the Release automation will handle **publishing the Release Note, fill the &ldquo;Fix Version&rdquo; field and move the RPM to &ldquo;Closed&rdquo; automatically**.

- 
If the Pull Request was done through a different Jira issue, then the **publishing the Release Note&nbsp;and transition to &ldquo;Closed&rdquo; must be done manually **:

release note published manuallytrue
Status &ldquo;Closed&rdquo;760
When the investigation is completed and/or release is published, is time to close the Problem Record. 

You need to select a **Status reason** when closing a Problem, from the available options:

- 
**&ldquo;Fixed&rdquo;**

- 
Status reason &ldquo;Fixed&rdquo; means the problem record had its root cause mitigated (change implemented). &ldquo;**Fix Versions**&rdquo; field should be filled at this time, if applicable.
A problem record is closed when all the fixes are available in GA (ring 3).

- 
**&ldquo;Not Fixed with Known Error&rdquo;**

- 
This means means the problem record did not lead to a change/fix in the product. The decision to not solve a problem should involve the Engineer Manager and/or PM, and the reason must be recorded in the &ldquo;**Justify Status Decision**&rdquo; field.

Some examples of why the problem will not be fixed: it is too risky or costly to fix; a limitation we are not willing to improve.

- 
&ldquo;**Duplicated**&rdquo;

- 
This status means the problem record is a duplicate of an already existing one. Check the following page for more information on dealing with duplicates: [https://outsystemsrd.atlassian.net/wiki/x/WoDADQE](https://outsystemsrd.atlassian.net/wiki/x/WoDADQE).

- 
&ldquo;**Rejected**&rdquo;

- 
This means after problem records are analyzed, there&rsquo;s a decision to not pursue their analysis because, for example, it was created by mistake.
It is mandatory to justify the reason for Rejected in the &ldquo;**Justify Status Decision**&rdquo; field.

- 
&ldquo;**Inconclusive Investigation**&rdquo;

- 
You may be unable to determine the root cause and, due to lack of information, the investigation must be stopped. In this scenario you should:

- 
Add the information that is missing to the &ldquo;**Root Cause**&rdquo; field, so that in future reported incidents that information is collected.

- 
Justify the reason for this conclusion in the &ldquo;**Justify Status Decision**&rdquo; field.

- 
**&ldquo;Waiting for Occurrences&rdquo;**

- 
Although this is visible, it only applies to O11 Problem Records. You should not be able to select this and proceed in ODC context.

**Note**: When an RPM is closed and linked to a customer incident, the customer will receive a notification stating that the RPM has been closed.
# ODC Problem Records Jira Fields
On the ODC RPM issue, we can distinguish these main sections:

The one on the right-hand side, with** **the ***Details*** section, the one on the left-hand side, with the main tabs - ***Problem Information***, ***Investigation*** and ***Resolution ***sections, and the bottom section, ***Action Items***.

- 
***Details***** **and ***Problem Information*** sections provide information about the ongoing problem.

- 
The ***Investigation ***section indicates the root cause of the problem, if known, and a possible workaround that helps the user handle the problem and return to productive work with minor to no delay.

- 
The ***Resolution*** section has the Release Notes and also indicates how the issue was closed.

- 
The ***Action Items*** section has all the linked issues related with the problem.

## Details section
**Details section**

**ODC RPM field**

**Description**

**Assignee **

A member of R&amp;D responsible to work on the problem.

Mandatory when moving an issue from &ldquo;New&rdquo; to &ldquo;Under Investigation&rdquo;.

**Reporter**

The person reporting the problem.

**Teams ***

Team assigned to the problem record and responsible for its resolution. [PACA ](https://engineering.outsystems.net/PACA/ProductAreasListTree.aspx)can be used to discover the owner team.

The problem record will appear in the team's problem board (you will need to update your Teams board filter for this to happen).

**Affects both Products (O11 and ODC)**

Indicates whether the problem affects both products (O11 and ODC).

**Product Categorization - ODC***

The ODC product area to which the problem relates.

**Product Categorization - O11**

The O11 product area to which the problem relates. 

It should be filled when the problem affects both products (O11 and ODC).

**Is it a Security Vulnerability? ***

Indicates if the issue is a Security Vulnerability.

**Criticality**

To be filled in only if the ODC RPM is a Security Vulnerability, by PSIRT, after the Vulnerability Classification.

**Urgency***

The fields **Urgency** and **Impact** should be filled according to here and will be used to calculate the problem **Priority **automatically.

- 
Available values for *Urgency *field: Low, Medium, High

- 
Available values for *Impact *field: Low, Medium, High

- 
If the issue is a Security Vulnerability, the *Impact *should be *High*.

 If the Vulnerability *Criticality *turns out to be High or Critical, the Problem Record *Priority* will be set* *to &ldquo;Urgent&rdquo;.

**Impact***

**Priority**
## Problem Information section

**Problem Information Section**

**ODC RPM field**

**Description**

**Details**

**Description**

A detailed description of the problem, which should include all the topics mentioned in the template.

Leave this field empty when creating the problem, and the template will be automatically added, after the ODC RPM creation, here.

**Problem Description Customer Facing**

A detailed description of the issue, visible for the Customer on the Support Portal.

Please follow the guidelines when filling this field.

Mandatory when moving an issue from &ldquo;New&rdquo; to &ldquo;Under Investigation&rdquo;.

**Zendesk Ticket IDs**

Holds list of Zendesk IDs of tickets related to JIRA issue in a comma-separated string.

## Investigation section
**Investigation Section**

**ODC RPM field**

**Description**

**Details**

**How to confirm you're affected**

Includes a short summary of the symptoms.

Please follow the guidelines when filling this field.

Mandatory when moving an issue from &ldquo;Under Investigation&rdquo; to &ldquo;Investigation Completed&rdquo;.

**Root cause**

Indicates the root cause of the problem.

It is up to the team to decide the complexity of the exercise used to determine the root cause.

Learn more about Root Cause Analysis (RCA).

Problems originated from Incidents will have their root cause determined within the scope of the Incident Response process.

Mandatory when moving an issue from &ldquo;Under Investigation&rdquo; to &ldquo;Investigation Completed&rdquo;.

**Workaround available**

Indicates whether there is a known workaround for the reported issue.

**Workaround**

A temporary solution that helps the user handle the problem and return to productive work with minor to no delay.

Please follow the guidelines when filling this field.

Mandatory when moving an issue from &ldquo;Under Investigation&rdquo; to &ldquo;Investigation Completed&rdquo;, if &ldquo;Workaround available&rdquo; is set to *Yes*.
## Resolution section
**Resolution Section**

**ODC RPM field**

**Description**

**Details**

**Release Note**

Explain what changed in the product with this problem resolution (improvement, bug fixing, or vulnerabilities that were fixed).

This description will be made public.

Please follow the guidelines when filling this field. Find some more information here: Guidelines to write Release Notes.

It is mandatory when moving the issue to &ldquo;Release Planned&rdquo;.

**Hide from Release Notes**

Define if you want the Problem Release Note to be included in the public OutSystems Release Notes page.

By default, the Release Note will be included in that document.

- 
Leave the field empty (*None *value) if you want the Release Note to be included.

- 
Select the option *Hide *if you don&rsquo;t want the Release Note to be included.

**Status Reason List**

Field to complement how the issue was closed.

Available options: 

Fixed / Duplicated / Rejected / Not fixed with Known Error / Inconclusive Investigation

**Justify Status Decision**

Text field to justify the decision to close the ODC RPM.

It is mandatory if the issue is closed as &ldquo;Rejected&rdquo; or &ldquo;Not Fixed with Known Error&rdquo;.

Please follow the guidelines when filling this field.

**Fix versions**

Version of the product where the fix is.

It is mandatory when moving the issue to &ldquo;Closed&rdquo;.

## Linked work items
To maintain a smooth RPM process and **prevent procedural errors**, the transition to the **&quot;Release Planned&quot;** status validates only critical action items. This ensures that a problem is not moved forward prematurely before its essential fixes are verified. All issues directly required for the problem's resolution (such as **Bugs **or **Development Tasks**) must be linked using the `&quot;is blocked by&quot;` link type. The RPM will be prevented from advancing until these items reach a &ldquo;**Done&rdquo;** status category.

In contrast, links such as `&quot;relates to&quot;`, typically used for **Incidents** (**RDINCs) and Vulnerabilities (VUL)**, are treated as informational only and **do not block** the workflow.

  Therefore, **ensure that the correct link type is always selected** to maintain workflow integrity and avoid unexpected blockers.