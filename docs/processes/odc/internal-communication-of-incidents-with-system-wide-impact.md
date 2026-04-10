---
title: Internal Communication of Incidents with System-Wide Impact
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/5344100368/Internal+Communication+of+Incidents+with+System-Wide+Impact
confluence_space: RKB
confluence_page_id: 5344100368
last_synced: 2026-04-09
owner: Process Engineering
---

# Internal Communication of Incidents with System-Wide Impact

**Version Control - **Current Version - 1.0 -    
internal status page
**Table of Contents**
12falsenonelisttrue# Problem Statement
Global Support cannot own internal communications for ODC system-wide impact incidents, as they are an external facing team.

**Current Process - **[RAPID for Status Page with the context.](https://docs.google.com/document/d/1-b0M2Eya04bA6NwY7FvPzInkrjjmhGL391p0K4Z_2uE/edit?tab=t.0#heading=h.7qs032krg7d6)

- 
SRE owns Incident handling

- 
Global Support owns communication on incidents:

- 
Internally - Field teams &amp; Product leadership

- 
Externally - Status Page (broad audience) and Support Portal (individual customers)

**Impact**: 

- 
R&amp;D Teams being deviated from their core responsibilities within Incident Response to provide updates to Global Support, and also being asked to tailor communication to a more customer-facing lingo.

- 
Global Support acts as an intermediary, passing information from R&amp;D to stakeholders, which leads to inefficient information transfer.

# Proposed Solution
The creation of a new role: ***Internal Communications Leader***, responsible for all internal communication for Product Leadership and Field Teams.

This role will be assumed by a representative from the **Team** most affected by the incident. This could be the Engineering Manager, Team Lead, Value Stream Leader or another senior team member.
## Expected Outcomes
- 
**Focused R&amp;D:** R&amp;D teams can remain focused on investigation and resolution, minimizing distractions related to crafting and tailoring broad communication.

- 
**Engineering on control: **Engineering will have greater control over the level of technical detail shared outside the group, reducing speculation and confusion.

- 
**Company-Wide Awareness:** OutSystems will be promptly informed about the incident, its scope, and the actions being taken to resolve it, enabling the company to take appropriate actions such as informing customers and or triggering other special protocols.

## Roles and Responsibilities
**Role**

**Executed by**

**Responsibilities**

**Incident Commander**

SRE Team

**Overall management and resolution** of the incident, making strategic and operational decisions.

- 
Declare the system-wide impact of an incident

- 
Push the Internal Communications Leader to the Incident Team

- 
Manage the technical part of incident resolution (coordination and mobilization)

**Internal Communications Leader**

Team representative

**Managing the flow of information** **to all internal stakeholders**, ensuring clarity and consistency.

- 
Review and publish the initial internal communication to outside Product  group

- 
Manage subsequent updates to the incident status

- 
Shield the Incident Response team from outside inputs, ensuring focus on incident resolution

**Customer-Facing Communication Team**

Global Support (Service Controllers)

**Managing the flow of information** **to all external stakeholders**, ensuring clarity and consistency.

- 
Create and publish external communication based on internal communication updates

- 
Manage customer expectations

## High-Level Process
[[Lucid Chart Diagram](https://lucid.app/lucidchart/1d1d7b4c-0070-4dfa-b094-f408ebc3b27d/edit?viewport_loc=-4764%2C-356%2C6652%2C3060%2CipWcRgdKVAU-&amp;invitationId=inv_224533ce-c8a3-40c6-9240-f096393da555)]

The communication process will consist of 3 communication moments:
### **#1 moment - communicate within Product Group (Product + Engineering)**
- 
**Expected Outcomes:**

- 
Engineering leadership is fully aware of the situation in real time to coordinate and allocate resources efficiently. 

- 
Leaders understand the severity, scope, and potential impact to guide decision-making.

- 
**When: **System-wide impact confirmed by SRE (Incident Declared) 

- 
**How: **[#product-leadership-incidents-alerts](https://outsystems.slack.com/archives/C07T5FPL08L) slack channel

- 
**Who:** SRE acting as Incident Commanders

- 
**What: **Nature of the incident, estimated impact (services impacted, rings, regions, criticality)

### **#2 moment - communicate within OutSystems (outside Product Group)**
- 
**Expected Outcomes:**

- 
The whole company is informed about the incident, its scope, and current actions, preventing speculation and confusion.

- 
Employees are aware of the criticality of the situation, allowing them to take appropriate actions (e.g., informing customers, pausing work on non-essential tasks).

- 
**When:**

- 
In the early stages of investigation, when impact is confirmed, the issue is isolated, and the team is about to start the execution of the response plan.

- 
During the incident lifecycle, when relevant updates are worth sharing with the group.

- 
**How:** (Private) Internal Status Page (Rootly)

- 
**Who:** A representative from the Team responsible for the area most affected by the incident (Engineering Managers, Value Stream Leaders, &hellip;), acting as Internal Communications Leaders, in collaboration with the Incident Commander.

- 
**What: **Incident summary, what&rsquo;s being done to resolve, estimated time for resolution or next check-in, workarounds, if applicable. Information that can be shared on the External Status Page.

### **#3 moment - communicate to outside OutSystems (External Status Page)**
- 
**Expected Outcomes:**

- 
Customers are kept informed about the status of the incident, reducing their frustration and increasing their trust in OutSystems.

- 
External stakeholders (customers, partners) understand the nature of the incident and how OutSystems is addressing it.

- 
**When:** If the incident meets the agreed [criteria](https://docs.google.com/document/d/1-b0M2Eya04bA6NwY7FvPzInkrjjmhGL391p0K4Z_2uE/edit?tab=t.0#heading=h.2iule67t21no) - after the team has started to investigate and isolate the issue, but is still within the early stages of resolution. 

- 
**How:** External Status page [https://status.outsystems.com/](https://status.outsystems.com/) 

- 
**Who:** Global Support customer-facing teams (Service Controllers). They should rely on the information already shared on the Internal Status Page, and contact the Internal Communications Leader if some clarification is needed.

- 
**What: **Clear description of the issue (what's happening, what&rsquo;s impacted), what actions are being taken to resolve it, a timeline or ETA for resolution (if available), regular updates, acknowledging the ongoing effort to restore service.

## Onboard the Internal Communications Leader
When triggering the declaration process, the SRE Team will be able to identify the services impacted and, with that information, they will be able to onboard the representative from the Team responsible for the area most affected by the incident to join the Incident Team.

They must be able to work together to understand the real impact and to define what will be shared to trigger [communication moment #2](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/5344100368/RSA-633+Internal+Communication+of+Incidents+with+System-Wide+Impact#%232-moment---communicate-within-Outsystems-(outside-Product-Group)). 

Templates will be provided to ease the communication.

## Internal Status Page
To accelerate the internal communication motion, the Process Engineering team is collaborating with the SRE Team to leverage the Rootly [Internal Status Page](https://docs.rootly.com/configuration/status-pages) feature.

## Continuous Improvement
Process Engineering team will ensure the monitoring of the Internal Communication Process rollout, by:

- 
Being present in the Incident's Slack channels.

- 
Ensuring messaging is clear, accurate, and empathetic, with a focus on managing frustration and maintaining transparency during incident handling.

- 
Providing real-time feedback and including it as insights in Incident Retrospectives.

- 
Confirming updates are appropriate and effectively convey OutSystems' commitment to resolving the issue swiftly.

- 
Gathering feedback from Eng. Managers, VS Leaders in 1:1 interviews.

- 
Understand, in Incident Retrospectives, if the Status Page was effectively used to share information about incident resolution.

## Implementation Plan 
[[Lucid chart]](https://lucid.app/lucidchart/1d1d7b4c-0070-4dfa-b094-f408ebc3b27d/edit?viewport_loc=5911%2C-64%2C3266%2C1330%2CM.UcGb9pIQMD&amp;invitationId=inv_224533ce-c8a3-40c6-9240-f096393da555)

The SRE Team will lead the technical implementation of this solution into two main vectors:
- 
Paging and mobilizing the designated Internal Communications Leader as soon as a system-wide incident is declared.

- 
Configuring the Internal Status Page with the features needed.

Most of the effort will be allocated to discovery for vector 1. 

The rollout plan will include the technical implementation by the SRE Team and enablement, adoption, and continuous monitoring by the Process Engineering Team.

The expected due date of rollout is **September 22**, and Process Engineering will continuously monitor the rollout until October 31. 

Type or paste something here to turn it into an excerpt.

# Process Version History
1st:  - 1 Escalation Policy per Value Stream. 1st Responder: Value Stream Leader / 2nd responder: His fallback 

2nd:  - 1 Escalation Policy per Value Stream, with the availability of using the On-Call schedules from the teams.

3rd: - 1 Escalation Policy per Team.