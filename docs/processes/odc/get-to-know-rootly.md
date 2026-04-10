---
title: Get to know Rootly
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4141482165/Get+to+know+Rootly
confluence_space: RKB
confluence_page_id: 4141482165
last_synced: 2026-04-09
owner: Process Engineering
---

# Get to know Rootly

**Version Control - **Current Version - 6.0 / Release Date -    

Next Release Planned - TBD

Please read the **Process Release Notes** page to check what will change. 

**This process applies to teams onboarded on Rootly ONLY**

Please check** **Rollout Strategy and Plan ** **

**Table of Contents**
# Why Rootly?
Rootly will become the **single source of truth** regarding Incident Response. The issues should contain all the information needed for **traceability purposes** - decisions made, steps done to troubleshoot, people involved in incident recovery, and recovery steps. 

You can manage incidents in Rootly using both Rootly UI and Slack. 

**Kick-off incidents fast**

**Automated &amp; consistent response**

**Learning from incidents**

Automatically jump into a dedicated Slack channel, all the tools provided, and incident responders and stakeholders in one place. 

Step-by-step guidance for any incident responder experience. You&rsquo;ll never wonder what to do next.

Every incident is an unplanned investment opportunity. We&rsquo;ll help you close the loop and unveil deeper insight, trends, and patterns you might have missed.

**Note about the Rollout Stage of Rootly**

During the rollout stage of Rootly, Jira incidents will be created to ensure quicker rollback and handover between teams working in Rootly and teams working in Jira. 

A special notification will be sent to the teams onboarded on [**#tmp-rootly-odc-globalchannel**](https://outsystems.slack.com/archives/C06P0SC9X3P), warning them that a new incident is available on Rootly.

# Managing incidents on Slack
One of the main advantages of using Rootly is its power to integrate automatically with Slack, especially for higher-severity incidents -** ** SEVerity 1Red  and SEVerity 2Yellow ** - ** where we want faster mobilization of engineers to resolve the incident.

Below you can check how the incident will look on the Slack Channel. The initial Slack post will be pinned automatically on the channel's top, as long as with other useful links. 

**[1] - **Useful pinned information (e.g. Playbooks, forms for Requests for Change)

**[2] - **Name of the channel

**[3] - **Engineer assigned to the Incident

**[4] - **Description of the symptoms, provided by Global Support

In the thread of the initial post, all the events will be registered as part of the **Incident timeline**.

For SEVerity 1Red or SEVerity 2Yellow  incidents, as soon as the incident is escalated to R&amp;D, a Slack Channel will be created and the On-call Engineer defined on the PagerDuty Escalation Policy will be added to the channel as the **Engineer **assigned to the case.

Any Rootly incident will notify the [**#tmp-rootly-odc-globalchannel**](https://outsystems.slack.com/archives/C06P0SC9X3P) slack channel.

Once you are added to a Rootly Incident Slack channel, there are just a few emojis you need to know to master Incident Response:
#FFFAE6
- 
 (star) - to add Tasks to Rootly Incidents

- 
 (memo) - to add Follow-ups to Rootly Incidents

- 
 (pushpin) - to add Slack conversations to Rootly Incidents

# Managing incidents on Rootly UI
Rootly also has an interface we can access via browser - the [Rootly UI](http://rootly.com). You can manage incidents in Slack or using Rootly UI. All the actions will be replicated on both sides.

 **Retrospectives** will be managed **exclusively** on Rootly UI.

You can check all of your Teams' incidents by navigating through the **Incidents page** and filtering the page by **Team**, as showcased below.

Selecting one particular Incident, the following sections can be highlighted:

**[1] - **Status of the Incident on Rootly - possible values are In triage  aCTIVERed  rESOLVEDGreen  

**[2] - **Description of the symptoms, provided by Global Support

**[3] - **Incident data - severity, teams assigned, tenant ID, tenant prefix, activation code, routing error code or product area, Zendesk ticket ID

**[4] - **Incident timeline, Tasks, Follow-ups, and Retrospective tabs

**[5] - Create Slack Channel** button

**[6] - Assign Roles** button

**[7] - Edit **incident button

**[8] - Custom Forms** button

# Managing Retrospectives
One of the selling points of Rootly is its ability to streamline Incident Retrospectives, by collecting events, both automatically and manually updated by the users, during the Incident Recovery stage and building the most complete timeline and a Retrospective document. 

The **Slack thread** of the initial Slack post will contain the **incident timeline** with all the events triggered automatically by Rootly (e.g. role assignment, fields updated) and all the events the Engineers involved decided to add during Incident troubleshooting and resolution.

**Slack conversations** will not be pinned to this thread but will become available on the incident timeline.

When clicking  **View Retrospective** button, you will be redirected to the** Rootly UI** retrospective page, where some actions will be requested to complete the **Retrospective Document**.

**[1] - **Status of the Incident on Rootly - possible values for Retrospectives are RETROSPECTIVE NOt STARTEDPurple  aCTIVE RETROSPECTIVEPurple  rEtrospective completedPurple  

**[2] -** View Retrospective - link to access the Retrospective Document

**[3] -** Retrospective steps to be performed - these steps should be performed on the Retrospective Document and status should be updated at the steps' completion.

Possible steps statuses are:

- 
***In Progress*** - for a step that is in progress

- 
***Completed ***- for a step that is completed

- 
***Skipped*** - for a step that is not mandatory and, therefore, can be skipped from the Retrospective. In this case, *&ldquo;Write the Executive Summary&rdquo;* is the only step that is not mandatory.

Once you marked the first step with a status, the Retrospective status changed from RETROSPECTIVE NOt STARTEDPurple to aCTIVE RETROSPECTIVEPurple.

Overall Retrospective completion is achieved once all the steps are marked with a final status. In this case, the Retrospective status changed from aCTIVE RETROSPECTIVEPurple to rEtrospective completedPurple.

# Rootly Incidents Workflow
The following workflow represents how Incident Recovery and Post Mortem stages of Incident Response will be represented by Rootly status. These statuses can only be checked using Rootly UI.

Incident Recovery and Post Mortem status machines are independent - you will see two statuses on Rootly UI, instead of just one. 

**Process stage**

**Jira Status**

**Description**

**Incident Recovery**

in TRIAGE  

A New incident was routed to the team that should start troubleshooting.

ACTIVERed 

The team started the incident. 

The incident is being worked on by an R&amp;D team member assigned to the incident.

Transition to the status is **manually** triggered.

RESOLVEDGreen    

The normal status of the service has been restored, so the Incident is resolved on the R&amp;D side due to one of the following reasons:

- 
Workaround/fix was provided and the Customer accepted; 

- 
Not supported / by design / not a platform issue;

- 
Zendesk ticket was marked as &lsquo;*Solved&rsquo; *by the Global Support team.

Transition to the status is **manually **triggered.

**Post Mortem**

Retrospective not startedPurple  

The team has not yet started the Retrospective.

Transition to the status is **automatically** triggered - once the incident is marked as RESOLVEDGreen.

active retrospectivePurple  

At least,** one** of the Retrospective steps is started. 

This could include marking the activity with one of the following statuses:

- 
In Progress

- 
Done

- 
Skipped

Transition to the status is **automatically** triggered.

retrospective completedPurple  

**All** the Retrospective steps are completed. 

This could include marking the activity with one of the following statuses:

- 
Done

- 
Skipped

Transition to the status is **automatically** triggered.

# Frequently Asked Questions## How to communicate with Global Support?
Communications with Global Support will be made using the green button** &ldquo;Send message to Global Support&rdquo;**, which will be displayed on the** Slack channel** every time an update is made on the incident. 

Clicking this button triggers a Rootly form where you can enter the message for Global Support. Once submitted, the message is automatically added to the Slack conversation, the incident timeline, and the **corresponding Zendesk ticket** via the Jira-Zendesk integration.

**Alternative Method:**

In the** Rootly UI**, click on **LAUNCH A CUSTOM FORM** and select **SEND MESSAGE TO GLOBAL SUPPORT** option.

## How do you deal with different teams contributing to the same Incident?
The field &ldquo;*Teams*&ldquo; must always have all the teams that contributed to the incident (whether it was in its resolution, diagnosis, ...). 

When swarming with other teams, those teams will automatically be added to that field.
## How to swarm with other teams in R&amp;D?
Swarming with other teams is highly recommended to speed up incident resolution. This action is possible, by triggering the green button **&ldquo;Swarm with other teams&rdquo;**.

Triggering this mechanism will:

- 
Page the On-Call Engineer through PagerDuty

- 
Add the On-Call Engineer to the Slack Channel

- 
Add the team to the Rootly field &ldquo;Teams&rdquo; on Rootly UI.

On** Rootly UI**, click the **LAUNCH A CUSTOM FORM** button and select the **SWARM WITH OTHER TEAMS** option.
## How to handover an incident between teams?
The same applies if the team initially assigned needs to **hand over the incident** to another team, for example, due to an initial wrong team assignment. 

In the case of a **handover between teams**, an additional step is needed, and it should be performed using Rootly UI, apart from any role reassignment performed in Slack.

The Engineer initially assigned to the Incident should replace on the field ***&ldquo;Teams&rdquo;*** their team for the team that should own the Incident instead. 

## How to add Slack conversations to the incident timeline?
During incident resolution, any relevant information, findings, and conclusions must be added to the incident timeline by reacting to each message with the  (pushpin) emoji.

Rootly will confirm the creation of the addition to the timeline by reacting to your message with .