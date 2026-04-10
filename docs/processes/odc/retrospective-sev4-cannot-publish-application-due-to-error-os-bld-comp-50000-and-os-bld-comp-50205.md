---
title: Retrospective-SEV4-Cannot publish application due to error OS-BLD-COMP-50000 and OS-BLD-COMP-50205
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4327931909/Retrospective-SEV4-Cannot+publish+application+due+to+error+OS-BLD-COMP-50000+and+OS-BLD-COMP-50205
confluence_space: RKB
confluence_page_id: 4327931909
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV4-Cannot publish application due to error OS-BLD-COMP-50000 and OS-BLD-COMP-50205

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV4

Teams:&nbsp;trueBlueModel 
#### 🕐 Timestamps
Started At:&nbsp;trueBlueAugust 1  2:16 PM WEST

Mitigated At:&nbsp;trueYellowAugust 1  6:28 PM WEST

Resolved At:&nbsp;trueGreenAugust 1  6:28 PM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/760-cannot-publish-application-due-to-error-os-bld-comp-50000-and-os-bld-comp-50205)
[Slack channel](https://slack.com/app_redirect?channel=C07EVPQJ23U&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3040146)

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

Nuno Rego
#### Summary
----------------------------------------------**CONSIDERATIONS BEFORE PERFORMING THE ESCALATION TO R&amp;D (MANDATORY)**
None of the below points should be overlooked. Failure to do so may imply unnecessary effort.* * *
Ensure the ticket has been **categorized**, otherwise, the R&amp;D escalation will go unnoticed and not be worked on!**1.** For **Incidents**, the **IMAX** was consulted **beforehand** on which:- No incident models were found for the reported symptoms **OR**
- The incident model did not solve the issue **OR**
- The next step indicated in the Incident Model is an escalation to R&amp;D.
**2.** For **Questions**, the ChatODC on the **Slack channel** didn't return an acceptable answer.
**3.** Any other requests that explicitly indicate an R&amp;D escalation is needed.
**4**. **Incident impact assessment** was based on the **prioritization scoring matrix**.* * ***R&amp;D ESCALATION FORM**
Section comments can be removed for R&amp;D easier interpretation.**ISSUE DESCRIPTION AND HOW TO REPRODUCE**- error OS-BLD-COMP-50000 and OS-BLD-COMP-50205**IMPACT ON THE CUSTOMER**
Brief description of the impact on the customer/development team/other, including:
- Stage where the problem is happening (Development / QA / Production);
- Frequency of the problem;
- Business impact or/and development impact;**TROUBLESHOOTING STEPS &amp; WORKAROUND**- When reviewing our internal logs, we found the following message:Application generation failed. Details: Compilation has failed with the following errors:ScreenServices.CloneOfVerzekeringStraat_MergedApp_UIFlow1_Relatiegegevens_ScreenModel.cs(285,134): error CS0103: The name 'ssRechtsVormId' does not exist in the current contextSince the error references `Relatiegegevens_ScreenModel` from the MainFlow, we deleted this action, which allowed us to successfully publish in our sandbox environment.![](https://supportoutsystems.zendesk.com/attachments/token/hFpGwvObqqTSOUPpBVOByzcm0/?name=image.png)This led us to identify the following assignment causing the issue:![](https://supportoutsystems.zendesk.com/attachments/token/V0FAYwkFkRsWVhJCdRJZDufbi/?name=image.png)![](https://supportoutsystems.zendesk.com/attachments/token/czwhEXefWrb6RdFFgezWHUrG2/?name=image.png)When using any other integer, the publish process completes successfully.- Following that the customer updated that- The issue appears to occur when you try to map to a structure inside a structure inside a structure.- In the attached oml there are 4 structures: the SourceStructure and Structure3 (which contains two fields), Structure2 (which contains some fields plus a field of type Structure3) and Structure1 (which contains some fields plus a field of type Structure2).- In the data action I try to map a variable of type SourceStructure to one of type Structure1 and one of type Structure2. The mapping to the fields that belong to Structure3 works in the case of Structure2 but not in the case of Structure1.- SandboxAlfio2.oml**TECH DATA OR ANY OTHER RELEVANT INFO**
Ring: ga
Tenant Id: c988378a-93fa-4884-9eb9-43d53708e42f
Tenant Prefix: veldsink
Region: eu-central-1
R3L.0LG.MUB.6GP.33S.YUE.26R.G0D_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 RetrospectiveinfoDetails
**Ring:** ga
**System-wide impact:**&nbsp; No
**Tenant ID:** c988378a-93fa-4884-9eb9-43d53708e42f
**Tenant Prefix:** veldsink
**Routing Error Code:** OS-BLD-COMP
**Product Area:** -
### Impact:
User was unable to publish
### Investigation and troubleshooting findings:
[https://outsystemsrd.atlassian.net/browse/RDINC-27660?focusedCommentId=1165790](https://outsystemsrd.atlassian.net/browse/RDINC-27660?focusedCommentId=1165790)
### Resolution:
We've escalated internally to figure out a solution between the multiple software components involved (IDE, Model and Compiler)
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/760-cannot-publish-application-due-to-error-os-bld-comp-50000-and-os-bld-comp-50205)

**Date**

**Source**

**User**

**Event**
July 26  1:56 AM WESTwebRootly
created an alert via
July 26  1:56 AM WESTwebRootly
Rootly created this incident
July 26  1:56 AM WESTwebRootly
In triage date has been set to July 26  1:56 AM WEST
July 26  2:06 AM WESTwebRootly
This incident was instantiated in Jira: RDINC-27660. Please work the incident using Rootly
July 26  2:56 AM WESTwebRootly
This incident was instantiated in Jira: RDINC-27660. Please work the incident using Rootly
July 26 10:53 AM WESTwebRui Eug&eacute;nio
This is a &quot;know&quot; issue with the structure mappings code. Passing this down to Backend Runtime.
July 26 10:54 AM WESTwebRui Eug&eacute;nio
Teams has been added: Backend Runtime
July 26 10:54 AM WESTwebRui Eug&eacute;nio
Teams has been removed: CompilerServices
July 29  1:37 PM WESTwebRui Garcia
Analysis on Jira comment: https://outsystemsrd.atlassian.net/browse/RDINC-27660?focusedCommentId=1164504
July 29  1:37 PM WESTwebRui Garcia
Teams has been added: Model 
July 29  1:37 PM WESTwebRui Garcia
Teams has been removed: Backend Runtime
July 30  5:34 PM WESTwebNuno RegoNuno Rego has been assigned as EngineerJuly 31 12:22 PM WESTwebRootly[Slack Channel](https://slack.com/app_redirect?channel=C07EVPQJ23U&amp;team=T041063TZ) has been createdAugust 1  2:16 PM WESTwebNuno Rego
Incident has been started
August 1  3:07 PM WESTwebNuno RegoSend ZenDesk private comment has been set: Hello team,Can you please let me know if the customer is blocked? I am confused as that is what I understand from looking into the zendesk communications but when I see that this is marked as a SEV4 I get the idea that he is unblocked.Best regards,
Nuno RegoAugust 1  3:07 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hello team,Can you please let me know if the customer is blocked? I am confused as that is what I understand from looking into the zendesk communications but when I see that this is marked as a SEV4 I get the idea that he is unblocked.Best regards,
Nuno Rego
August 1  3:07 PM WESTwebRootlySend ZenDesk private comment has been unsetAugust 1  3:07 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

August 1  6:14 PM WESTwebRootlyZendesk Private Comment has been set: ----------------------------------------------**Update to R&amp;D**
Hello TeamThe customer is not blocked but he insisted that wants to know the cause of the error.Thus we assigned the lowest priority.Kind regards,__August 1  6:14 PM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
Hello TeamThe customer is not blocked but he insisted that wants to know the cause of the error.Thus we assigned the lowest priority.Kind regards,__
August 1  6:14 PM WESTwebRootlyZendesk Private Comment has been changed to: ------------------------------------------------ This notification was sent from Zendesk Support ticket #3040146 to all linked JIRA issues by Ricardo Moreira. --**Update to R&amp;D**
Hello TeamThe customer is not blocked but he insisted that wants to know the cause of the error.Thus we assigned the lowest priority.
Please don't close the case without giving us some info.Kind regards,_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_August 1  6:14 PM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
------------------------------------------------ This notification was sent from Zendesk Support ticket #3040146 to all linked JIRA issues by Ricardo Moreira. --**Update to R&amp;D**
Hello TeamThe customer is not blocked but he insisted that wants to know the cause of the error.Thus we assigned the lowest priority.
Please don't close the case without giving us some info.Kind regards,__
August 1  6:25 PM WESTwebNuno RegoSend ZenDesk private comment has been set: Hello team,The root cause is a bug in the communication of a couple software components in the OutSystems Platform. We've understood the problem and are now escalating it internally so that we can fix this permanently. We thank the customer for his patience.As the customer is unblocked and R&amp;D is already working internally to solve this problem we'll move this issue to done.Best regards,
Nuno RegoAugust 1  6:25 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hello team,The root cause is a bug in the communication of a couple software components in the OutSystems Platform. We've understood the problem and are now escalating it internally so that we can fix this permanently. We thank the customer for his patience.As the customer is unblocked and R&amp;D is already working internally to solve this problem we'll move this issue to done.Best regards,
Nuno Rego
August 1  6:26 PM WESTwebRootlySend ZenDesk private comment has been unsetAugust 1  6:26 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

August 1  6:28 PM WESTwebRootly
Incident has been resolved
August 1  6:28 PM WESTwebRootlySystem-wide impact has been set: NoAugust 1  6:28 PM WESTwebRootlyImpact has been set: User was unable to publishAugust 1  6:28 PM WESTwebRootlyInvestigation and troubleshooting findings has been set: https://outsystemsrd.atlassian.net/browse/RDINC-27660?focusedCommentId=1165790August 1  6:28 PM WESTwebRootlyResolution has been set: We've escalated internally to figure out a solution between the multiple software components involved (IDE, Model and Compiler)