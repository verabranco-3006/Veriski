---
title: What does an ODC Incident look like in Jira?
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4696212738/What+does+an+ODC+Incident+look+like+in+Jira
confluence_space: RKB
confluence_page_id: 4696212738
last_synced: 2026-04-09
owner: Process Engineering
---

# What does an ODC Incident look like in Jira?

**Version Control - **Current Version - 9.0 /  Release Date - 

Please read the **Process Release Notes** page to check what will change. 

**Table of Contents**
13falsecirclelisttrue# Jira Screens and Fields
- 
&nbsp;Jira Project: [https://outsystemsrd.atlassian.net/jira/software/c/projects/RDINC/boards/2269](https://outsystemsrd.atlassian.net/jira/software/c/projects/RDINC/boards/2269) 

## Change Failure Rate (CFR) Reporting
This project will directly contribute to the calculation of the **Change Failure Rate (CFR)** metric, which is a key indicator of the stability and quality of our deployment process.

To ensure the accuracy and reliability of this crucial metric, it is **mandatory** that **specific fields** within the Jira R&amp;D Incidents (RDINC) project issue are filled out **accurately** and **completely**. These fields are essential for correctly identifying **when an incident was caused by a recent change, linking it back to the Request for Change (RFC),** and thus classifying the change as a failure.
:warning:26a0⚠️#FFFAE6
**Accurate data entry is critical** for deriving meaningful insights and driving improvements in our Incident Response process.

### Key Fields for *CFR *Calculation
The following Jira fields are the critical data points used to calculate the Change Failure Rate:

- 
***Incident Type*****: **The source of the incident.

- 
***Impacted Asset(s)*****: **List all the assets that caused the incident.

- 
***Rings*****: **The rings that are being affected by the incident.

- 
***Root Cause Categorization*****: **Clustering of root causes.

&nbsp;

**Note**: These fields are identified in this document with &ldquo;[*** Change Failure Rate***  ]&rdquo;.

## RDINC issues main areas
&nbsp;

On the RDINC issue, we can distinguish the following main areas:

On the right-hand side is the ***Details** *area; on the left-hand side are the main tabs &mdash; ***Incident Information**, **Troubleshooting**, **Retrospective**, *and ***Feedback*** &mdash; and at the bottom is the ***Action Items*** area.

- 
***Incident Information ***tab and ***Details***** **area provide information about the ongoing incident when Global Support escalates the incident.

- 
The ***Troubleshooting ***tab will be used during **Incident Recovery** to provide useful information, such as key findings and details about the resolution.

- 
The ***Retrospective*** tab will collect the information during the **Incident Retrospective** execution.

- 
The ***Feedback*** tab will collect feedback on multiple pieces of information regarding the Incident Response process.

- 
The ***Action Items*** tab collects both the recovery measures identified during **Incident Recovery** and the action items defined during the **Incident Retrospective**.

- 
 ***Maintenance &amp; Operations ***is a tab exclusively used by the team maintaining the Jira Project for process troubleshooting purposes. No fields must be manually edited by the teams executing the process without consulting [https://outsystemsrd.atlassian.net/people/team/b3750437-12b9-468f-bdc4-57ece5994dc5](https://outsystemsrd.atlassian.net/people/team/b3750437-12b9-468f-bdc4-57ece5994dc5) (  ).

### Details Area
**Details Tab**

**RDINC field**

**Description**

**When?**

**Severity**

The **severity **of the incident - read more about Severity Levels here.

Possible values:  SEV1Red SEV2Yellow SEV3Blue SEV4

**Rings**

The rings that are being **affected **by the incident.

It is a multi-selection field.

Possible values: ring-devGreen ring-testGreen ring-stageGreen ring-osrdGreen ring-osallGreen ring-osallGreen ring-eaGreen ring-gaGreen

[*** Change Failure Rate***  ]

**Mandatory **when transitioning to solvedGreen

Exceptions: 

- 
*Incident Type = Alert*

- 
*Root Cause Categorization = Customer Issue*

**Teams**

**Teams assigned** to the case and responsible for its resolution/mitigation.

It is a multi-selection field.

**Reporter**

The person who **reported **the Incident.

A member of Global Support when the Incident is reported by the customer.

**Automatically**, at RFC creation

**Assignee**

A member of R&amp;D **responsible to work** on the Incident.

The Assignee is cleared, and the field reset every time the &ldquo;Teams&rdquo; field changes.

**Labels**

**Automatically added** by Jira automation. 

Important values to retain:

`jira_escalated` - All the incidents reported by the customer via Global Support (Customer Triggered Incidents)

`created-by-eden` / `created-by-pegasus` - All the incidents reported by SDLC (Ring Transition Incidents)

`created-by-quality` - All incidents created as a result of an end to end failure

`customer-impacted` - All the incidents that are detected internally by R&amp;D that could affect a customer (for incidents created proactively by R&amp;D)

`triggered-alerts` - All the incidents generated by alarms set on Grafana

**Priority**

It is the priority given to the Support Case, either by Global Support for customer-triggered incidents or through automation for event-triggered incidents.

For customer-triggered incidents, this is automatically synchronized with the priority in the Zendesk ticket and R&amp;D cannot change it by themselves.&nbsp;

Possible values:  UrgentRed hIGHYellow normalBlue Low

**Cancellation Reason**

The reason for canceling the incident.

Possible values:  false positiveBlue duplicatedBlue test / simulationBlue created by mistakeBlue

**Mandatory **when transitioning to cancelledGreen

### Incident Information Tab

**Incident Information Tab**

**RDINC field**

**Description**

**When?**

**Incident Type**

The **source **of the Incident.

Possible values: Customer ReportedGreen alertGreen internalGreen system-wide slo triggerGreen  service specific sloGreen  

[*** Change Failure Rate***  ]

**Automatically**, at RFC creation

**Description**

Includes:

- 
Description of the technical problem

- 
Impact of this problem to Customer

- 
What was done on the Support side for troubleshooting/attempts to workaround?

- 
What we expect from R&amp;D

- 
Technical Data

**Tenant ID**

ID of the tenant affected by the incident

**Tenant Prefix**

Prefix of the tenant affected by the incident

**Error Code**

Error Code found or reported by the customer

(This information is used to route the incident to the appropriate team based on the Error Code &lt;&gt; Owner Team mapping in PACA.)

This information is provided from Global Support.

### Troubleshooting Tab

**Troubleshooting Tab**

**RDINC field**

**Description**

**When?**

**Impacted Asset(s)**

List all the assets that caused the incident.

It is a **multi-selection** field.

[*** Change Failure Rate***  ]

**Mandatory **when transitioning to solvedGreen

Exceptions: 

- 
*Incident Type = Alert*

- 
*Root Cause Categorization = Customer Issue*

**Specify Missing Asset**

When selecting **'Asset Missing'** in the Impacted Asset(s) field, specify the **missing asset** in this field.

It will then be analyzed by the Release Engineering Team to determine whether the missing asset should be added to the Impacted Asset(s) field list.

**Mandatory **when transitioning to solvedGreen, if ***Impacted Asset(s) = Asset Missing***

**Impact**

In sync with Rootly for incidents involving the SRE team

Describe **how the customer(s) were impacted** during the incident - e.g. journeys affected (deployments, runtime, authentication), how the affected services are impacting the intended customer experience (journey).

 **Quick-tip:** identify the SLO that measures the intended experience for this journey (if there is an SLO for it).

**Recovery**

In sync with Rootly for incidents involving the SRE team

Step-by-step actions taken by the team to **solve the incident** (reestablish service).

Description of any **workaround **can be described here.

**  Quick-tip: **if you followed the runbook, please reference it.

**Findings**

In sync with Rootly for incidents involving the SRE team

By using the information of the previous fields - the impacted services, the triggers and how we detected the incident, the impact, and what we did to recover - **identify situations** where:

- 
The service did not react as expected

- 
The process was not properly executed or failed during the incident response

- 
People did not coordinate as expected through incident recovery

- 
Tooling failed during the incident response

**Slack Channel**

Slack Channel link, generated by Rootly for incidents involving the SRE team.

&nbsp;

### Retrospective Tab

**Retrospective Tab**

**RDINC field**

**Description**

**When?**

**RCA/Post Mortem URL**

Link to the Retrospective document.

For **incidents with system-wide impact**, the field will be automatically populated by Rootly.

**Mandatory** for** incidents with system-wide impact**, or when transitioning from Retrospective in ProgressBlue to Retrospective COMPLETEDGreen

**Reviewer**

The** person who reviewed** the Retrospective.

**Mandatory** for **incidents with system-wide impact **when transitioning from Retrospective in ProgressBlue to Retrospective COMPLETEDGreen

**Reviewed?**

*= Yes* , when the Retrospective document has been validated by the Reviewer.

**Mandatory** for** incidents with system-wide impact **when transitioning from Retrospective in ProgressBlue to Retrospective COMPLETEDGreen

**Approver**

The **person who approved** the Retrospective.

**Mandatory** for** incidents with system-wide impact** when transitioning from Retrospective in ProgressBlue to Retrospective COMPLETEDGreen

**Approved?**

*= Yes* , when the Retrospective document has been approved by the Approver.

**Mandatory** for** incidents with system-wide impact** when transitioning from Retrospective in ProgressBlue to Retrospective COMPLETEDGreen

**Generate RCA document from Rootly**

Teams can use this field to generate an automatic Retrospective document link. The document will be placed on **RCA/Post Mortem URL** field.

This option will only be available for incidents on SolvedGreen statuses and for **incidents without system-wide impact**.

**Root Cause Categorization**

Clustering of **root causes**. Possible values are:

- 
Infrastructure issues

- 
Application issues

- 
Deployment issues

- 
Security Issues

- 
Operational Issues

- 
Configuration issues

- 
Missing feature

- 
Customer Issue

- 
Self Recovered

- 
Tests failed

  **Quick-tip:** Check here some tips to pick the most accurate root cause.

[*** Change Failure Rate***  ]

**Mandatory** when transitioning to solvedGreen

Exceptions: 

- 
*Incident Type = Alert*

- 
*Root Cause Categorization = Customer Issue*

### Feedback Tab

**Feedback Tab**

**RDINC field**

**Description**

**How do you classify the information provided by Global Support?**

To collect feedback from the teams regarding the information provided on the escalation.

Possible values: 1 - Very Poor  2 - Below Average  3 - Average  4 - Above Average  5 - Excellent

**Was the incident assigned to the correct team?**

To collect feedback from the teams regarding the incident&rsquo;s initial assignment.

Possible values: YesGreen NoRed

**Was the R&amp;D Incident Information necessary?**

To collect feedback from the teams regarding the need for the escalation. This will help to determine concrete actions to promote Global Support autonomy.

Possible values: YesGreen NoRed

**How do you classify your interaction with Global Support?**

To globally classify the interaction with Global Support.

Possible values: 1 - Very Poor  2 - Below Average  3 - Average  4 - Above Average  5 - Excellent

**How do you classify your interaction with SRE?**

To globally classify the interaction with SRE Team.

Possible values: 1 - Very Poor  2 - Below Average  3 - Average  4 - Above Average  5 - Excellent

**You can provide more details here:**

Free text field to detail on feedback provided.