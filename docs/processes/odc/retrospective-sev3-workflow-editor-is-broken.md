---
title: Retrospective-SEV3-Workflow editor is broken
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4309484016/Retrospective-SEV3-Workflow+editor+is+broken
confluence_space: RKB
confluence_page_id: 4309484016
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV3-Workflow editor is broken

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV3

Teams:&nbsp;trueBlueWorkflow Editor
#### 🕐 Timestamps
Started At:&nbsp;trueBlueJuly 23 11:31 AM WEST

Mitigated At:&nbsp;trueYellowJuly 25  2:30 PM WEST

Resolved At:&nbsp;trueGreenJuly 25  2:30 PM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/736-workflow-editor-is-broken)
[Slack channel](https://slack.com/app_redirect?channel=C07DA25HXHA&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3038568)

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

Teresa Marcelino
#### Summary
**CONSIDERATIONS BEFORE PERFORMING THE ESCALATION TO R&amp;D (MANDATORY)**
None of the below points should be overlooked. Failure to do so may imply unnecessary effort.Ensure the ticket has been **categorized**, otherwise, the R&amp;D escalation will go unnoticed and not be worked on!
**1.** For **Incidents**, the **IMAX** was consulted **beforehand** on which:- No incident models were found for the reported symptoms **OR**
- The incident model did not solve the issue **OR**
- The next step indicated in the Incident Model is an escalation to R&amp;D.**2.** For **Questions**, the ChatODC on the **Slack channel** didn't return an acceptable answer.**3.** Any other requests that explicitly indicate an R&amp;D escalation is needed.**4**. **Incident impact assessment** was based on the **prioritization scoring matrix**.**R&amp;D ESCALATION FORM**
Section comments can be removed for R&amp;D easier interpretation.
**ISSUE DESCRIPTION AND HOW TO REPRODUCE**
- Our Solution Architect, Maria Martins, is not able to modify, create or delete the SimpleApproval Workflow from her tenant
- Try to make nay changes to **https://mariamartinsdemos.outsystems.dev/workfloweditor/open?id=5fb8f12c-b204-4f21-9c23-38dcdaa6ecdc**
**IMPACT ON THE CUSTOMER**
Brief description of the impact on the customer/development team/other, including:
- The release to GA is Monday, July 23, 2024, and our SA need to test the Workflow to be able to handle inquiries from the customer
**TROUBLESHOOTING STEPS &amp; WORKAROUND**
- Accessed the tenant and tested the SimpleApproval Workflow.
- It works for me but Maria is not able to make any changes. It seems that Maria does not have the access right.
**TECH DATA OR ANY OTHER RELEVANT INFO**
- **mariamartinsdemos.outsystems.dev**
Ring: ea
Tenant Id: e22024e7-47bb-41d4-9af0-8c37b5789dc0
Tenant Prefix: mariamartinsdemos
Region: ap-southeast-1
K0Y.EVB.W6T.QKZ.3T1.MXD.JLJ.QOU
_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 RetrospectiveinfoDetails
**Ring:** ea
**System-wide impact:**&nbsp; No
**Tenant ID:** e22024e7-47bb-41d4-9af0-8c37b5789dc0
**Tenant Prefix:** mariamartinsdemos
**Routing Error Code:** N/A
**Product Area:** Phoenix::Phoenix Portal::Apps
### Impact:
The user is unblocked
### Investigation and troubleshooting findings:
From the logs for this session (97edb402-434b-4c1a-9ab9-338ca6766139), we detected errors related to attempts to delete objects that do not exist in the workflow. These errors do not explain the user's inability to edit and modify the workflow.
### Resolution:
After analyzing with the reporter (internal tenant), we were able to use the same workSession ID and try to replicate the issue. Through this same analysis, we identified that the user was not blocked but was experiencing latency issues, which explains why the user assumed they could not edit. Therefore, it was possible to jointly modify and publish the reported workflow. We will internally analyze what improvements we can make in terms of latency.
## Tasks performed during incident resolution:
&nbsp;
## Executive Summary
[Guidelines](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4144496679/Incident+Retrospectives+-+Playbook#STEP-3---Write-the-Executive-Summary)
## Root Causes 
[Guidelines](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4144496679/Incident+Retrospectives+-+Playbook#STEP-1---Perform-the-Root-Cause-Analysis)

If the customer needs formal RCA, please fill out the following field with the document URL

[Please follow these instructions and place the RCA URL in the field below.](https://docs.google.com/document/d/13rXmBsOJh73nV2D6Z17SIBGBu2HOTWty5ddsvU000JM/edit#heading=h.bqxasxszr5q)

RCA URL

&lt;Place the URL of the customer RCA here if you have created one&gt;
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/736-workflow-editor-is-broken)

**Date**

**Source**

**User**

**Event**
July 19  4:44 AM WESTwebRootly
created an alert via
July 19  4:44 AM WESTwebRootly
Rootly created this incident
July 19  4:44 AM WESTwebRootly
In triage date has been set to July 19  4:44 AM WEST
July 19  9:52 AM WESTwebJo&atilde;o SemedoTeresa Marcelino has been assigned as EngineerJuly 19  3:14 PM WESTwebRootly[Slack Channel](https://slack.com/app_redirect?channel=C07DA25HXHA&amp;team=T041063TZ) has been createdJuly 19  7:01 PM WESTwebTeresa Marcelino
Teams has been added: Workflow Editor
July 19  7:01 PM WESTwebTeresa Marcelino
Teams has been removed: ALM Consoles
July 23 11:31 AM WESTwebTeresa Marcelino
Incident has been started
July 25  8:40 AM WESTslackteresa.marcelino
During the Zoom call with the reporter of the incident, we noticed that the incident is no longer impacting them. The reporter was able to perform actions in the workflow, including publishing. The only thing detected was a significant delay between executing actions and the respective refresh on the front end, which might explain the initially reported problem.
July 25  8:52 AM WESTwebTeresa Marcelino
Summary has been changed to 

&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;**CONSIDERATIONS BEFORE PERFORMING THE ESCALATION TO R&amp;D (MANDATORY)**
None of the below points should be overlooked. Failure to do so may imply unnecessary effort.
&nbsp;&nbsp;
Ensure the ticket has been **categorized**, otherwise, the R&amp;D escalation will go unnoticed and not be worked on!

&nbsp;&nbsp;**1.** For **Incidents**, the **IMAX** was consulted **beforehand** on which:

- No incident models were found for the reported symptoms **OR**&nbsp;&nbsp;
- The incident model did not solve the issue **OR**&nbsp;&nbsp;
- The next step indicated in the Incident Model is an escalation to R&amp;D.**2.** For **Questions**, the ChatODC on the **Slack channel** didn't return an acceptable answer.**3.** Any other requests that explicitly indicate an R&amp;D escalation is needed.**4**. **Incident impact assessment** was based on the **prioritization scoring matrix**.

&nbsp;&nbsp;**R&amp;D ESCALATION FORM**
Section comments can be removed for R&amp;D easier interpretation.

&nbsp;&nbsp;**ISSUE DESCRIPTION AND HOW TO REPRODUCE**
- Our Solution Architect, Maria Martins, is not able to modify, create or delete the SimpleApproval Workflow from her tenant

- Try to make nay changes to **&nbsp;&nbsp;[https://mariamartinsdemos.outsystems.dev/workfloweditor/open?id=5fb8f12c-b204-4f21-9c23-38dcdaa6ecdc](https://mariamartinsdemos.outsystems.dev/workfloweditor/open?id=5fb8f12c-b204-4f21-9c23-38dcdaa6ecdc)&nbsp;&nbsp;**
&nbsp;&nbsp;**IMPACT ON THE CUSTOMER**
Brief description of the impact on the customer/development team/other, including:

- The release to GA is Monday, July 23, 2024, and our SA need to test the Workflow to be able to handle inquiries from the customer

&nbsp;&nbsp;**TROUBLESHOOTING STEPS &amp; WORKAROUND**
- Accessed the tenant and tested the SimpleApproval Workflow.

- It works for me but Maria is not able to make any changes. It seems that Maria does not have the access right.

&nbsp;&nbsp;**TECH DATA OR ANY OTHER RELEVANT INFO**
- **mariamartinsdemos.outsystems.dev**
Ring: ea

Tenant Id: e22024e7-47bb-41d4-9af0-8c37b5789dc0

Tenant Prefix: mariamartinsdemos

Region: ap-southeast-1

K0Y.EVB.W6T.QKZ.3T1.MXD.JLJ.QOU

&nbsp;&nbsp;*&lt;! do not remove this line, this will be used to the trigger* Technical Support::Send to R&amp;D - ODC *#trigger_send_to_r&amp;d_odc !&gt;*&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;July 25  8:52 AM WESTwebTeresa MarcelinoSystem-wide impact has been set: NoJuly 25  8:52 AM WESTwebTeresa MarcelinoImpact has been set: The user is unblockedJuly 25  8:52 AM WESTwebTeresa MarcelinoInvestigation and troubleshooting findings has been set: From the logs for this session (97edb402-434b-4c1a-9ab9-338ca6766139), we detected errors related to attempts to delete objects that do not exist in the workflow. These errors do not explain the user's inability to edit and modify the workflow.July 25  2:30 PM WESTwebTeresa Marcelino
Incident has been resolved
July 25  2:30 PM WESTwebTeresa MarcelinoResolution has been set: After analyzing with the reporter (internal tenant), we were able to use the same workSession ID and try to replicate the issue. Through this same analysis, we identified that the user was not blocked but was experiencing latency issues, which explains why the user assumed they could not edit. Therefore, it was possible to jointly modify and publish the reported workflow. We will internally analyze what improvements we can make in terms of latency.