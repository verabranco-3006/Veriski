---
title: Retrospective-SEV3-Cannot install AI Agent Builder from the forge
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4293427454/Retrospective-SEV3-Cannot+install+AI+Agent+Builder+from+the+forge
confluence_space: RKB
confluence_page_id: 4293427454
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV3-Cannot install AI Agent Builder from the forge

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV3

Teams:&nbsp;trueBlueLowcode Ai
#### 🕐 Timestamps
Started At:&nbsp;trueBlueJuly 11 12:43 PM WEST

Mitigated At:&nbsp;trueYellowJuly 18  1:33 PM WEST

Resolved At:&nbsp;trueGreenJuly 18  1:33 PM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/682-cannot-install-ai-agent-builder-from-the-forge)
[Slack channel](https://slack.com/app_redirect?channel=C07B2FBTHP0&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3032545)

#### 🧑&zwj;🚒 Incident Rolestrue
**Stakeholder**

Marco Coimbra
#### Summary
----------------------------------------------**CONSIDERATIONS BEFORE PERFORMING THE ESCALATION TO R&amp;D (MANDATORY)**
None of the below points should be overlooked. Failure to do so may imply unnecessary effort.* * *
Ensure the ticket has been **categorized**, otherwise, the R&amp;D escalation will go unnoticed and not be worked on!**1.** For **Incidents**, the **IMAX** was consulted **beforehand** on which:- No incident models were found for the reported symptoms **OR**
- The incident model did not solve the issue **OR**
- The next step indicated in the Incident Model is an escalation to R&amp;D.
**2.** For **Questions**, the ChatODC on the **Slack channel** didn't return an acceptable answer.
**3.** Any other requests that explicitly indicate an R&amp;D escalation is needed.
**4**. **Incident impact assessment** was based on the **prioritization scoring matrix**.* * ***R&amp;D ESCALATION FORM**
Section comments can be removed for R&amp;D easier interpretation.**ISSUE DESCRIPTION AND HOW TO REPRODUCE**
- The customer encounters an error every time they try to install AI Agent Builder from the Forge Tab in the ODC Portal.
- The error in question: `The application depends on library 'DateTime' with key '420e3fcf-b57d-471d-9933-4dcb1a5f41cb' and digest '06189ab6-f2dd-1c8d-40bb-430c8926070a' that is missing, please publish it before proceeding. (OS-APPS-40017)`**IMPACT ON THE CUSTOMER**
Brief description of the impact on the customer/development team/other, including:
- Development
- Ongoing
- The customer is unable to install and utilize a supported Outsystems ODC Forge component.**TROUBLESHOOTING STEPS &amp; WORKAROUND**
- We were able to reproduce the issue mentioned by the customer.
- The last installation attempt for AI Agent Builder encountered an error at 18:26 UTC on July 5, 2024.![](https://supportoutsystems.zendesk.com/attachments/token/6bTHXN1zUYeTIi9mIXhWU9VL9/?name=image.png)![](https://supportoutsystems.zendesk.com/attachments/token/DRRrcnFQBPxb85Owx7OCRlFwD/?name=image.png)**TECH DATA OR ANY OTHER RELEVANT INFO**
- Ring: ea
- Tenant Id: 285464c3-4757-4611-8a65-c0ea529a6182
- Tenant Prefix: estratusgroup
- Region: us-east-1
- YVI.8L8.MD1.X0T.H1A.9VF.NEM.H73_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 RetrospectiveinfoDetails
**Ring:** ea
**System-wide impact:**&nbsp; No
**Tenant ID:** 285464c3-4757-4611-8a65-c0ea529a6182
**Tenant Prefix:** estratusgroup
**Routing Error Code:** N/A
**Product Area:** Phoenix::Phoenix Portal::Forge::Forge Services
### Impact:
some customers could not install the latest version of AI Agent Builder from Forge
### Investigation and troubleshooting findings:
the issue was that we released a new version of the system extension DateTime without bumping its tag, which caused a mismatch between the hash in the AI Agent Builder reference to DateTime and the installed version of DateTime, causing Forge to fail the validation of the dependency
### Resolution:
A new DateTime version with a completely new hash was deployed. When it reached ring 2, the reference on AI Agent Builder was refreshed and a new version deployed to Forge
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/682-cannot-install-ai-agent-builder-from-the-forge)

**Date**

**Source**

**User**

**Event**
July 5  7:41 PM WESTwebRootly
created an alert via
July 5  7:41 PM WESTwebRootly
Rootly created this incident
July 5  7:41 PM WESTwebRootly
In triage date has been set to July 5  7:41 PM WEST
July 5  7:51 PM WESTwebRootly
This incident was instantiated in Jira: RDINC-26558. Please work the incident using Rootly
July 5  8:41 PM WESTwebRootly
This incident was instantiated in Jira: RDINC-26558. Please work the incident using Rootly
July 6 12:59 AM WESTwebRootly[Slack Channel](https://slack.com/app_redirect?channel=C07B2FBTHP0&amp;team=T041063TZ) has been createdJuly 8  5:44 PM WESTwebRootlyZendesk Private Comment has been set: ----------------------------------------------**Update to R&amp;D**
- Hello teamInstalling version 1.2.0 results in the same error.Kind regards,__July 8  5:44 PM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
- Hello teamInstalling version 1.2.0 results in the same error.Kind regards,__
July 8  5:44 PM WESTwebRootlyZendesk Private Comment has been changed to: ------------------------------------------------ This notification was sent from Zendesk Support ticket #3032545 to all linked JIRA issues by Ricardo Moreira. --**Update to R&amp;D**- Hello teamInstalling version 1.2.0 results in the same error.Kind regards,_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_July 8  5:44 PM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
------------------------------------------------ This notification was sent from Zendesk Support ticket #3032545 to all linked JIRA issues by Ricardo Moreira. --**Update to R&amp;D**- Hello teamInstalling version 1.2.0 results in the same error.Kind regards,__
July 11 12:43 PM WESTwebRodrigo Silva
Incident has been started
July 11 12:43 PM WESTwebRodrigo SilvaRicardo Duarte has been assigned as EngineerJuly 11  5:01 PM WESTslackhelder.marques
So, from our side, the issue was that we released a new version of the system extension DateTime without bumping its tag, which caused a mismatch between the hash in the AI Agent Builder reference to DateTime and the installed version of DateTime, causing Forge to fail the validation of the dependency. To mitigate the issue, a new version of the DateTime, with a completely new hash was deployed. To complete the fix, the reference on AI Agent Builder should be refreshed a new version deployed to Forge
July 16 10:39 AM WESTwebRodrigo Silva
Teams has been added: Lowcode AI
July 16 10:39 AM WESTwebRodrigo Silva
Teams has been removed: Neo Platform Theseus
July 16 10:40 AM WESTwebRodrigo SilvaMarco Coimbra has been assigned as StakeholderJuly 16 10:40 AM WESTwebRodrigo Silva
Ricardo Duarte has been unassigned from Engineer
July 16  5:47 PM WESTwebRootlyZenDesk Event Type has been set: solvedJuly 16  5:47 PM WESTwebRootly
The Global Support team marked this incident as closed in ZenDesk.
July 18  1:33 PM WESTwebMarco Coimbra
Incident has been resolved
July 18  1:33 PM WESTwebMarco CoimbraSystem-wide impact has been set: NoJuly 18  1:33 PM WESTwebMarco CoimbraImpact has been set: some customers could not install the latest version of AI Agent Builder from ForgeJuly 18  1:33 PM WESTwebMarco CoimbraInvestigation and troubleshooting findings has been set: the issue was that we released a new version of the system extension DateTime without bumping its tag, which caused a mismatch between the hash in the AI Agent Builder reference to DateTime and the installed version of DateTime, causing Forge to fail the validation of the dependencyJuly 18  1:33 PM WESTwebMarco CoimbraResolution has been set: A new DateTime version with a completely new hash was deployed. When it reached ring 2, the reference on AI Agent Builder was refreshed and a new version deployed to Forge