---
title: SCENARIO 1 - Incident without system-wide impact
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4977164930/SCENARIO+1+-+Incident+without+system-wide+impact
confluence_space: RKB
confluence_page_id: 4977164930
last_synced: 2026-04-09
owner: Process Engineering
---

# SCENARIO 1 - Incident without system-wide impact

**Version Control - **Current Version - 1.0 /  Release Date -  

**Table of Contentst**
13falsecirclelisttrue# Incident without system-wide impact
**Incidents without System-wide Impact - **A specific issue contained to 1 tenant. With partial or full disruption to developers and/or end-users.

## Incident Recovery
For incidents **reported by Customers**, Global Support will be accountable for managing the entire incident lifecycle, by logging, categorizing, prioritizing, and performing initial diagnosis.

If the resolution is not identified during the initial diagnosis stage, Global Support must escalate to Engineering.  Typically, all **Severity 3** and **Severity 4** incidents will be automatically escalated to the **Development Team** owning the symptom** **due to the **low risk** of system-wide impact.

In this case, a Jira Incident will be created on the ODC R&amp;D Incidents .

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

### How to swarm with other Development Teams?** **  
While troubleshooting, Development Teams could engage with other Development teams, if needed. To do so,  you can use the following commands from Rootly, directly on your Slack. 

how_to_page_teams:raised_back_of_hand:1f91a🤚#B3F5FF
**MANUAL TASK - Swarm with other Teams**

To swarm with other Development Teams, add the `Team` to the field *Teams.*

### How to swarm with the SRE Team?** ** 
The same applies to the SRE Team - if the SRE Team is needed for troubleshooting, the Development Team must add the `SRE Global` to the field *Teams, *on Jira. 

This action will automatically create a Rootly incident, connected with the Jira issue. It will also page the SRE Team. 

Another alternative could be to page directly the SRE Team using the command `/rootly page`.
:raised_back_of_hand:1f91a🤚#B3F5FF
**MANUAL TASK - Swarm with SRE**

Add the `SRE Global` to the field *Teams *to swarm with the SRE Team.

how_to_add_sre_jira

Alternatively, you can page the SRE Team directly, using the slack command `/rootly page` as described here - SCENARIO 1 - Incident without system-wide impact 

### How to engage with Global Support?
The Development Teams should provide regular updates to Global Support to ease their job of managing customer expectations. If extra information is needed from the customer, Development Teams must engage with Global Support Agents to get the required information.

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

Once the Development Team believes that a **solid solution plan **is defined to unblock the customer and solve the incident, the information must be shared with Global Support, so they can share it with the customer and proceed with the incident follow-up actions.
:arrows_counterclockwise:1f504🔄#B3F5FF
**AUTOMATIC TASK - Status Progression**

If the ticket is solved on Zendesk by the customer or the Support Agent, the incident will move to solvedGreen.
:arrows_counterclockwise:1f504🔄#FFEBE6
**READ ME - AUTOMATIC TASK on the Jira incident**

If, for any reason, the incident needs to be reopened by the customer, on Zendesk and R&amp;D intervention is still needed, the incident on Jira will be moved from solvedGreen to TROUBLESHOOTING in ProgressBlue, **automatically.**

This transition will happen while the ticket on Zendesk remains in any status different than Closed. 

## Moving to the Retrospective Stage
For incidents **without system-wide impact**, the Retrospective stage is **not mandatory**. Although, if the Development Team decides, this stage can be initiated following the guidelines below.
V2 - Retrospective Process