---
title: Product Areas & Error Codes updates on ODC
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/3064627610/Product+Areas+Error+Codes+updates+on+ODC
confluence_space: RKB
confluence_page_id: 3064627610
last_synced: 2026-04-09
owner: Process Engineering
---

# Product Areas & Error Codes updates on ODC

**Version Control - **New document

Next Release Planned - Version 1.0 / Expected Release Date -   

Please read the [**Process Release Notes**](#) page to check what will change. 

**Table of Contents**

ODC customer-reported incidents team assignment relies on one of the following inputs, provided by Global Support at the moment of incident handover to R&amp;D:

- 
Product Areas - where the incident symptom is manifesting

- 
Error Codes - shared by the customer or fetched by Global Support during initial troubleshooting

Based on these inputs, it is expected the incident to reach the owner team of the Product Area or the Error Code, once the incident is escalated to R&amp;D.

## Process overview
When a change on a product area or error code is needed, the **Change Submitter** - the R&amp;D Team Lead or Product Owner - should submit the change on the corresponding PACA tree - Product Areas or Error Codes.

The PACA/Error Code change will be assessed and approved by the **Release Approver** - a Global Support team member - which is responsible for releasing a new version of the affected tree. The changes on each tree should be reflected both on:

- 
Zendesk - to display the new structure of product areas/error codes to be selected by Global Support Agents

- 
Jira/Rootly - to have a valid link between the product area/error code and the corresponding owner team to assign the incident, at the handover.

Any impacting changes in the structure could require special training and enablement needs, and if so, they will be planned and managed by the **Change Facilitator**.

**READ ME**

Before creating the product area / error code entry on the corresponding PACA tree, make sure that your team prepared the transition of the feature to be supported by Global Support. 

Please follow this article to prepare feature transitioning to Global Support - Transitioning a Feature to Global Support 

### Roles &amp; Responsibilities

**Role**

**Points of Contact**

**Responsibility**

***Change Submitter***

**R&amp;D Team Leaders and Value Stream Leaders***** **(collaborating with Product Architectures and Dev Managers, if needed)*

- 
Create/Update/Submit/Delete Product Areas/Error Codes  (CRUD operations)

- 
Propose and request the changes to the PACA structure and bring useful use cases for the analysis

- 
Transition the feature to be supported by Global Support

***Release Approver***

**Global Support Service Transition Team**

    
  

- 
Review PACA tree requests for update

- 
Release a new version of the Product Area tree

- 
Plan the date of the release

- 
Send a communication to the relevant teams to inform about the new release

- 
Approve/Discard a Product Area/Error Coce change - after a CRUD operation

- 
Evaluate the impact of the Product Areas/Error Codes changes suggested by the Change Submitters 

***Change Facilitator***

**R&amp;D Process Engineering**
 

- 
Facilitates decision taking by providing in-depth data analysis

- 
Document and design PACA related processes and workflows

- 
Support R&amp;D Teams with PACA app-related improvements

- 
Ensure the PACA changes are reflected on Jira and Zendesk

***Tool Experts***

**SRE Team**

 

**Jira Confluence Support Team**

 

**Global Support**

 

- 
Implement changes in Incident Response tools (Jira, Zendesk, Rootly)

***PACA App Owners***

**Digital**

- 
Ownership and Maintenance of PACA as an R&amp;D Internal Tool

- 
Address the problems reported at *#rd-internal-apps-team*

- 
Manage permissions

- 
Update PACA documentation on Confluence

### Expected Release Cycle
Changes on each tree will be reviewed and approved by a Change Advisory Board (CAB) led by the **Release Approver** every week on Fridays, at 10:30 AM - Lisbon time.

During the CAB meeting, if any questions were raised, the **Release Approver** could reach out to the owning team proposing the changes or use [#tmp-paca-phoenix-definition](https://outsystems.slack.com/archives/C036SAH2NQ4) to challenge the proposal near the **Experts** on the channel. In the meantime, the change will be on hold.

After the approval cycle ends, the** Change Facilitator **will ensure that changes are reflected on the tooling needed to support incident assignment (Jira and Zendesk).

### Emergency Change Requests:sos:1f198🆘#FFBDAD
Emergency changes on the PACA structure should be used as a **last resort** and in case of need, should be requested by the **Change Submitter** to the Release Approver in the [#tmp-paca-phoenix-definition](https://outsystems.slack.com/archives/C036SAH2NQ4).

The **Release Approver** and the **Change Facilitator** will then evaluate the request and act accordingly.

Please use the following template to report emergency change requests:
#FFFAE6
**EMERGENCY CHANGE REQUEST**

Hey CAB! 

Please approve the following changes on PACA:

[TIER 1 Node] &gt; [TIER 2 Node] &gt; [Tier 3 Node] &gt; [Tier 4 Node] - previously assigned to [OLD TEAM NAME according to PACA] and changing to [NEW TEAM NAME according to PACA]

**Example**

Phoenix Portal &gt; Apps &gt; Mobile &gt; Preview in devices - previously assigned to UI Components - Phoenix and changing to Consoles Unified Experience

## Manage Product Areas/Error Codes on PACA
Product Areas, Error Codes and the corresponding Owner Teams will be managed using PACA Application capabilities. 

Each team, as** Change Submitters**,** ** should be accountable for updating the information related to their assets, both Product Areas or Error Codes, using the corresponding PACA Tree:

- 
**Product Areas from Phoenix **list &rarr; to update product areas

- 
**Product Areas from ODC Error Codes** list &rarr; to update Error Codes prefixes

### Create or Update a new entry on the tree
Each Product Area/Error Code must contain the following information to be subject to approval:

- 
It **should **have a description to clarify what type of issues should be logged in that category, mapped on the field ***Description***

- 
It **must **have an Engineering team associated with it, mapped on the field ***Owner Team***

- 
The Engineering team associated with it **must match exactly** the team defined in [Engineering Organization Management (EOM)](https://applications.outsystems.app/EOM/), to guarantee the issues are properly routed to the Engineering team.

- 
The Engineering team should be active on EOM -otherwise, it will not be possible to update or create the new entry on the tree structure

- 
It **must be** categorized with a Support Scope Level, mapped on the field ***Support Scope Level***

**Supported Scope Level**

**Support Responsibilities**

**Scope Level Requirements**

Scope Level 0

Being able to execute simple screening and redirection

- 
How to identify incidents and change requests?

- 
Identify the escalation point to raise issues related to that service,

Scope Level 1

Being able to execute simple/automated troubleshooting steps/tasks

- 
All Level 0 Requirements;

- 
Know-how and when to execute the procedures for the simple troubleshooting steps or automated task, while understanding all the possible outcomes;

- 
Otherwise, issues that are not described in the procedure should be escalated.

Scope Level 2

Being able to execute simple to high complexity troubleshooting steps/tasks

- 
All Level 1 Requirements;

- 
Be familiar with the troubleshooting guidelines necessary to recover from failed procedures;

- 
Know-how on how to access and interpret the logs for that service.

- 
Ability to handle complex incidents.

### Delete an entry on the tree 
Delete operations on the product areas tree are performed at a lower frequency than the Create and Update operations. The reason for this is that a product area doesn&rsquo;t cease to exist as soon as the latest release containing it reaches its end of life.&nbsp;

**Prerequisite**: this rule is only possible if there are no open Support tickets.