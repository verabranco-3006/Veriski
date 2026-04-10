---
title: Retrospective-SEV3-Work flow "Decision" and "Fetch more data - service action" giving runtime time error with no error description
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4333600902/Retrospective-SEV3-Work+flow+Decision+and+Fetch+more+data+-+service+action+giving+runtime+time+error+with+no+error+description
confluence_space: RKB
confluence_page_id: 4333600902
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV3-Work flow "Decision" and "Fetch more data - service action" giving runtime time error with no error description

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV3

Teams:&nbsp;trueBlueBackend Runtime
#### 🕐 Timestamps
Started At:&nbsp;trueBlueJuly 11  1:48 PM WEST

Mitigated At:&nbsp;trueYellowAugust 5  1:38 PM WEST

Resolved At:&nbsp;trueGreenAugust 5  1:38 PM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/699-work-flow-decision-and-fetch-more-data-service-action-giving-runtime-time-error-with-no-error-description-76670426-0f48-4438-8569-e52dcc0198b0)
[Pagerduty incident](https://outsystems.pagerduty.com/incidents/Q1E2BX55X6T4HA)

[Slack channel](https://slack.com/app_redirect?channel=C07CDCHM83B&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3033143)

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

Rui Garcia
#### Summary
----------------------------------------------**CONSIDERATIONS BEFORE PERFORMING THE ESCALATION TO R&amp;D (MANDATORY)**
None of the below points should be overlooked. Failure to do so may imply unnecessary effort.* * *
Ensure the ticket has been **categorized**, otherwise, the R&amp;D escalation will go unnoticed and not be worked on!**1.** For **Incidents**, the **IMAX** was consulted **beforehand** on which:- No incident models were found for the reported symptoms **OR**
- The incident model did not solve the issue **OR**
- The next step indicated in the Incident Model is an escalation to R&amp;D.
**2.** For **Questions**, the ChatODC on the **Slack channel** didn't return an acceptable answer.
**3.** Any other requests that explicitly indicate an R&amp;D escalation is needed.
**4**. **Incident impact assessment** was based on the **prioritization scoring matrix**.* * ***R&amp;D ESCALATION FORM**
Section comments can be removed for R&amp;D easier interpretation.**ISSUE DESCRIPTION AND HOW TO REPRODUCE**- The customer is running into a few issues associated with Workflows, all of which are occurring on the same node:- The customer is trying to use a Service Action to fetch data to determine a limit, and when they do, they run into an error in that node, but the error does not generate any logs, and the traces are equally vague, but they seem to indicate that the issue does not lie in the Service Action itself:- ![](https://supportoutsystems.zendesk.com/attachments/token/JDAgw7xsF4wlXxaBMQu1Pv16D/?name=image.png)- ![](https://supportoutsystems.zendesk.com/attachments/token/s2wftVk13MGaP0mN726hNVSYf/?name=image.png)- They've tried to change it to a simply dynamic condition that checks for the value of the previous node, but it throws an error with no further information shared about it:- ![](https://supportoutsystems.zendesk.com/attachments/token/CryM4ug38xLnpwIszGdQp0QSy/?name=image.png)- ![](https://supportoutsystems.zendesk.com/attachments/token/cjbsZ2ofdSSrHxh4vOcAhPjEc/?name=image.png)- In case this helps, the activity definition key is 6b1476b6-bb68-4ba7-b7e1-d318b227cdbc.**IMPACT ON THE CUSTOMER**- The customer is in the process of testing out workflows and they don't know how to correct this, but this is not a blocker for them.**TROUBLESHOOTING STEPS &amp; WORKAROUND**- Given the currently limited documentation on this feature and the absence of information on these errors, we were unable to do much to try to troubleshoot this.
- Also, please know that we used &quot;Phoenix Portal &gt; Apps&quot; as a categorization given that workflows isn't available yet, and it is our understanding that this is also under your scope.**TECH DATA OR ANY OTHER RELEVANT INFO**- Ring: ea
- Tenant Id: 356f454c-2370-476f-afba-9943374831da
- Tenant Prefix: headfitted
- Region: ap-southeast-1_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 RetrospectiveinfoDetails
**Ring:** ea
**System-wide impact:**&nbsp; No
**Tenant ID:** 356f454c-2370-476f-afba-9943374831da
**Tenant Prefix:** headfitted
**Routing Error Code:** N/A
**Product Area:** Phoenix::Phoenix Portal::Apps
### Impact:
Localized issues while running workflows.
### Investigation and troubleshooting findings:
Original ask was related with a bug that affected the access to expression values from a Human Activity CloseOn Event parameters from the following activities.

Second ask is related to a breaking change in the contract between the Process and the supporting Application (missing parameter value in the Service Action).
### Resolution:
First issue was addressed and eventually rolled out.

Second issue is the expected behavior. However, issue's visibility ought to be improve so that customers can easily identify the offending pattern.
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/699-work-flow-decision-and-fetch-more-data-service-action-giving-runtime-time-error-with-no-error-description-76670426-0f48-4438-8569-e52dcc0198b0)

**Date**

**Source**

**User**

**Event**
July 11  1:01 PM WESTwebRootly
created an alert via
July 11  1:01 PM WESTwebRootly
Rootly created this incident
July 11  1:01 PM WESTwebRootly
In triage date has been set to July 11  1:01 PM WEST
July 11  1:48 PM WESTwebJo&atilde;o Ros&aacute;rioJo&atilde;o Ros&aacute;rio has been assigned as EngineerJuly 11  1:48 PM WESTwebJo&atilde;o Ros&aacute;rio
Incident has been started
July 11  2:36 PM WESTwebJo&atilde;o Ros&aacute;rioSwarm has been set: Backend RuntimeJuly 11  2:36 PM WESTwebRootly[PagerDuty Incident](https://outsystems.pagerduty.com/incidents/Q1E2BX55X6T4HA) has been created.
📧 Notified Rui Garcia by email.&nbsp;&nbsp;📱 Notified Rui Garcia by SMS.&nbsp;&nbsp;📧 Notified Rui Garcia by email.July 11  2:38 PM WESTwebRootly
Rui Garcia acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q1E2BX55X6T4HA). (via Phone)
July 11  2:43 PM WESTwebRootly[Slack Channel](https://slack.com/app_redirect?channel=C07CDCHM83B&amp;team=T041063TZ) has been createdJuly 11  2:43 PM WESTwebJo&atilde;o Ros&aacute;rioSwarm has been set: Extended RuntimeJuly 11  2:43 PM WESTwebJo&atilde;o Ros&aacute;rioSwarm has been unset: Backend RuntimeJuly 11  2:43 PM WESTwebRootly
Pagerduty Integrations added Pedro Pita as responder in [PagerDuty](https://outsystems.pagerduty.com/incidents/Q1E2BX55X6T4HA)
July 11  2:47 PM WESTwebRootly
Pedro Pita joined this [PagerDuty](https://outsystems.pagerduty.com/incidents/Q1E2BX55X6T4HA) incident.
July 11  2:47 PM WESTwebRootly
Pedro Pita acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q1E2BX55X6T4HA). (via Phone)
July 11  4:11 PM WESTwebRui GarciaSend ZenDesk private comment has been set: Hello, Global Support.First of all, thank our customer for providing feedback about the early stages of this new capability: Workflows.The issue affecting the execution of the Decision Activity is a known issue.
When the Input Parameter value of a Close On Event associated with an Human Activity that ran before is used somewhere, the Workflow executor is unable to access its value.
That's the reason why the first attempt of running the Decision node in Process Instance 10 failed. He have an issue for that: [https://outsystemsrd.atlassian.net/browse/RRCT-5817](https://outsystemsrd.atlassian.net/browse/RRCT-5817)
In the issue, the value is used in an Automatic Activity, but the access pattern is similar.
In the logs we see something like:&gt; _Unable to obtain value for variable 3d03a271-082b-4e40-92e3-152fa7551209, 38079ba5-8891-499a-ba7a-b41284f13974, 8a594da1-1217-468e-9b8f-d975262cd859._Subsequent retries of the same activity instance failed because the Workflow Executor is not ready yet to handle activity execution retries.
In retries the error changes to:&gt; _23505: duplicate key value violates unique constraint &quot;osidx_osrem_activity_event_id_process_id&quot;_
The automatic retry is still being developed by the team.While we don't address this issue, customers won't be able to run that pattern successfully.July 11  4:11 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hello, Global Support.First of all, thank our customer for providing feedback about the early stages of this new capability: Workflows.The issue affecting the execution of the Decision Activity is a known issue.
When the Input Parameter value of a Close On Event associated with an Human Activity that ran before is used somewhere, the Workflow executor is unable to access its value.
That's the reason why the first attempt of running the Decision node in Process Instance 10 failed. He have an issue for that: [https://outsystemsrd.atlassian.net/browse/RRCT-5817](https://outsystemsrd.atlassian.net/browse/RRCT-5817)
In the issue, the value is used in an Automatic Activity, but the access pattern is similar.
In the logs we see something like:&gt; _Unable to obtain value for variable 3d03a271-082b-4e40-92e3-152fa7551209, 38079ba5-8891-499a-ba7a-b41284f13974, 8a594da1-1217-468e-9b8f-d975262cd859._Subsequent retries of the same activity instance failed because the Workflow Executor is not ready yet to handle activity execution retries.
In retries the error changes to:&gt; _23505: duplicate key value violates unique constraint &quot;osidx_osrem_activity_event_id_process_id&quot;_
The automatic retry is still being developed by the team.While we don't address this issue, customers won't be able to run that pattern successfully.
July 11  4:11 PM WESTwebRootlySend ZenDesk private comment has been unsetJuly 11  4:11 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

July 11  4:23 PM WESTwebRui GarciaRui Garcia has been assigned as EngineerJuly 11  4:23 PM WESTwebJo&atilde;o Ros&aacute;rio
Teams has been removed: ALM Consoles
July 11  4:28 PM WESTwebRui Garcia
Teams has been removed: Extended Runtime
July 11  4:46 PM WESTwebRootlyZendesk Private Comment has been set: ------------------------------------------------ This notification was sent from Zendesk Support ticket #3033143 to all linked JIRA issues by Gon&ccedil;alo Silva. --**Update to R&amp;D**
Hey Ruy,Thanks for the help, we'd be happy too but Global Support doesn't have access to Rootly; we understand there's an ongoing issue preventing rootly communications from reaching zendesk, so would it be possible to copy-paste your update into the Jira in the meantime?Thanks in advance!__July 11  4:46 PM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
------------------------------------------------ This notification was sent from Zendesk Support ticket #3033143 to all linked JIRA issues by Gon&ccedil;alo Silva. --**Update to R&amp;D**
Hey Ruy,Thanks for the help, we'd be happy too but Global Support doesn't have access to Rootly; we understand there's an ongoing issue preventing rootly communications from reaching zendesk, so would it be possible to copy-paste your update into the Jira in the meantime?Thanks in advance!__
July 12  6:31 PM WESTwebRootly
Rui Garcia marked the incident as resolved through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q1E2BX55X6T4HA). (via Website)
July 29 12:57 PM WESTwebRootlyZendesk Private Comment has been changed to: ------------------------------------------------ This notification was sent from Zendesk Support ticket #3033143 to all linked JIRA issues by Ricardo Moreira. --**Update to R&amp;D**- Hello TeamThe customer reports that they have the same error exactly when adding extra data in a node and when it tries to return values.Please verify the attached pictures.Attachment - image.pngAttachment - image.pngAttachment - image.pngIs this related to the same reported error?_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;__Attachments_1722250589000000000__HandleEventAsnc.JPG1722250596000000000__WF_Error.JPG1722250600000000000__ww_design.JPGJuly 29 12:57 PM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
------------------------------------------------ This notification was sent from Zendesk Support ticket #3033143 to all linked JIRA issues by Ricardo Moreira. --**Update to R&amp;D**- Hello TeamThe customer reports that they have the same error exactly when adding extra data in a node and when it tries to return values.Please verify the attached pictures.Attachment - image.pngAttachment - image.pngAttachment - image.pngIs this related to the same reported error?___Attachments_1722250589000000000__HandleEventAsnc.JPG1722250596000000000__WF_Error.JPG1722250600000000000__ww_design.JPG
August 5  1:38 PM WESTwebRui Garcia
Incident has been resolved
August 5  1:38 PM WESTwebRui GarciaSystem-wide impact has been set: NoAugust 5  1:38 PM WESTwebRui GarciaImpact has been set: Localized issues while running workflows.August 5  1:38 PM WESTwebRui GarciaInvestigation and troubleshooting findings has been set: Original ask was related with a bug that affected the access to expression values from a Human Activity CloseOn Event parameters from the following activities.
Second ask is related to a breaking change in the contract between the Process and the supporting Application (missing parameter value in the Service Action).August 5  1:38 PM WESTwebRui GarciaResolution has been set: First issue was addressed and eventually rolled out.
Second issue is the expected behavior. However, issue's visibility ought to be improve so that customers can easily identify the offending pattern.