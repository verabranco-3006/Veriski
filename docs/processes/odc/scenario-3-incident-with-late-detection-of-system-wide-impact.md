---
title: SCENARIO 3 - Incident with late detection of system-wide impact
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4977459722/SCENARIO+3+-+Incident+with+late+detection+of+system-wide+impact
confluence_space: RKB
confluence_page_id: 4977459722
last_synced: 2026-04-09
owner: Process Engineering
---

# SCENARIO 3 - Incident with late detection of system-wide impact

**Version Control - **Current Version - 1.0 /  Release Date -  

**Table of Contents**
13falsecirclelisttrue# Incident with late detection of system-wide impact
**Incidents with System-wide Impact - **1 or more region(s) partially (&gt;1 tenant) or fully affected or the potential to escalate to these proportions. This causes an impact on developers and/or end-users.

#### What does late detection of system-wide impact mean?
Late detection of system-wide impact could happen if, during the initial troubleshooting performed on an incident initially reported without system-impact, **the risk of system-wide impact increases**. This could happen due to another customer reporting an incident with similar symptoms or through an SLO burndown event. 

## Incident Recovery
If the resolution is not identified during the initial diagnosis stage, Global Support must escalate to Development Teams to continue the impact assessment. 

In this case, a Jira Incident will be created on the ODC R&amp;D Incidents Jira project.

- 
The initial Status of the incident is TEam Assigned   

- 
The incident is marked with `jira_escalated` label

- 
The incident will be assigned on the field *Teams*, to the Team owning the Product Area / Error Code reported

### Initial Troubleshooting
Development Teams must start troubleshooting, using the information provided by Global Support. To indicate the beginning of troubleshooting, the incident must progress to the status TROUBLESHOOTING in ProgressBlue and the On-Call Engineer must be assigned, using the field *Assignee*.

:raised_back_of_hand:1f91a🤚#B3F5FF
**MANUAL TASK -  Status Progression**

The Incident should be moved from TEam Assigned  to TROUBLESHOOTING in ProgressBlue  
:raised_back_of_hand:1f91a🤚#B3F5FF
**MANUAL TASK -  Designate an Assignee**

An Assignee must be assigned through the field *Assignee*.

### How to swarm with the SRE Team?** ** 
If the Development Team **suspects system-wide impact**, must **immediately summon** the SRE Team so they can diagnose and confirm the impact and trigger the incident declaration, if necessary. 
how_to_add_sre_jira

This action will automatically create a Rootly incident, linked to the Jira issue, assigned initially to the Development Team. It will also page the SRE Team. In this case, a **Slack Channel** will be created to mobilize everyone needed.
:raised_back_of_hand:1f91a🤚#B3F5FF
**MANUAL TASK - Summon the SRE Team**

To swarm with the SRE Team, you must add the `SRE Global` to the field *Teams.*

Alternatively, you can page SRE directly through Slack.

how_to_page_teams
### Incident Declaration
SRE will immediately assist the Development Team with troubleshooting to confirm the system-wide impact.

   If the SRE team **denies** the system-wide impact, they will hand over the incident to the Development Team owning the error code/product area of the reported symptom. The Team will continue to work on the incident in Jira. 

From this moment forward, **SCENARIO 1** is activated. 
SCENARIO 1 - Incident without system-wide impact:arrows_counterclockwise:1f504🔄#B3F5FF
**AUTOMATIC TASK - Team Assignment**

The Development Team will be assigned to a Jira Incident, through the field *Teams *and the incident will be displayed in the Development Teams backlog.

 

  If the SRE Team **confirms** the system-wide impact of the incident, an event will be logged on the Slack Channel and trigger a communication motion to important stakeholders. A Communication Lead will be assigned to the incident.

In this scenario, the SRE Team will take the role of **Incident Commander** and will swarm with any Development Team to help move forward with incident troubleshooting.

### How to engage with Global Support?
While the incident is being handled as an incident **without system-wide impact**, the Development Teams should provide regular updates to Global Support to ease their job of managing customer expectations. 

When the incident is declared by the SRE Team **with system-wide impact**, the SRE Team will handle communication with Global Support. Development Teams will be consulted to align on what to communicate and ask for. 

If extra information is needed from the customer, Development Teams must engage with Global Support Agents to get the required information.

**After requesting** information from Global Support:
:raised_back_of_hand:1f91a🤚#B3F5FF
**MANUAL TASK - Status Progression**

The Incident should be moved from TROUBLESHOOTING in ProgressBlue to Waiting for Customer.

Once the **customer replied**, Global Support will analyze the information provided and will reach out to the Development Teams again to proceed with troubleshooting.
:arrows_counterclockwise:1f504🔄#B3F5FF
**AUTOMATIC TASK - Status Progression**

When the customer replied, the status of the incident will change from Waiting for Customer  to Troubleshooting in progressBlue.

There are two methods to engage with Global Support, both using **Jira Zendesk Integration**:

**(1) Add Comment to all linked tickets** button on the **Zendesk Support** panel on the right side of the Incident

**(2)** Using **Zendesk Support** on the **Activity Tab** at the bottom of the Incident

#### **WARNING - Please Read Me**:rotating_light:1f6a8🚨#FFEBE6
**READ ME**

Since Global Support is responsible for communicating directly with customers, the Assignee must be extra careful and ** NOT** **ACTIVATE** the **&ldquo;Send as a Public Reply&rdquo;** flag.

Messages written with this option checked **will be sent directly to customers** and, by doing so, **sensitive and confidential information might be shared with customers.**

### Recovery Measures
The primary goal during an incident is to **minimize customer impact** as quickly as possible. This means focusing on restoring service, not on fixing the underlying problem.

With that in mind, your first step should always be to figure out what options you have to mitigate the problem as fast as possible:
- 
**Identify the Faulty Asset(s)**

- 
**Does a Rollback restore the system to normal operation?**

- 
**Consider other mitigations**

Before acting, you must have a clear idea of what's causing the problem.

The first step is to identify the **faulty asset(s)** - the specific application, service, or component where the issue is originating.

You don't need to know the complete root cause or the exact line of code that's broken. Simply identifying the source of the problem is enough to move to the next step.

With the faulty asset(s) identified, the first course of action should be to consider a **rollback**, in order to restore the system to a normal, functional state.

Ask these questions:

- 
**Is it possible to rollback the asset(s)?**

- 
**What is the risk associated with a rollback?**

If the rollback is feasible and the risk is acceptable, proceed with it immediately. This aligns with an **incident resolution mindset**, where the priority is to solve the negative impact to customers, not to fix the bug itself.

If a rollback is not possible or the risk is too high, only then should you **explore other mitigation strategies**.

Read more about rollback operations here: Change Management Process.

The** ****Change Management**** **process can be triggered as a recovery mechanism. If the SRE Team involvement is needed, you must create the corresponding Requests for Change and assign them to the `SRE Global` team.
:raised_back_of_hand:1f91a🤚#B3F5FF
**MANUAL TASK - Create Change Management Artifacts**

- 
 Standard Request for Change - [[Form]](https://outsystemsrd.atlassian.net/jira/software/c/projects/RFC/forms/form/direct/6/12582)

- 
 Normal Request for Change - [[Form]](https://outsystemsrd.atlassian.net/jira/software/c/projects/RFC/forms/form/direct/2/12523)

- 
 Emergency Request for Change - [[Form]](https://outsystemsrd.atlassian.net/jira/software/c/projects/RFC/forms/form/direct/3/12524)

:raised_back_of_hand:1f91a🤚#B3F5FF
**MANUAL TASK - Assign a Change to the SRE Team**

To trigger the SRE Team, you must add the `SRE Global` to the field *Teams* on the Change Management artifacts created.

#### Traceability of Recovery Measures
Recovery measures must be linked to the RDINC Jira issue using the **Linked Issues** Jira capability* &ldquo;is blocked by&rdquo;*.

Additionally, other recovery measures such as bugs can be reported and used as a recovery mechanism, if included on the SDLC pipeline and propagated through the rings.

When the SRE Team confirms the symptoms are no longer manifesting, the SRE Team will mark the incident as Resolved.
:arrows_counterclockwise:1f504🔄#B3F5FF
**AUTOMATIC TASK -  Status Progression**

The Incident will be moved from TROUBLESHOOTING in ProgressBlue to solvedGreen  

## Moving to the Retrospective Stage
For incidents **with system-wide impact**, the Retrospective stage **is mandatory**. This stage can be initiated following the guidelines below.
V2 - Retrospective Process