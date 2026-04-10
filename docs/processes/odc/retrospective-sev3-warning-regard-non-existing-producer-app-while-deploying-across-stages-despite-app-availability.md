---
title: Retrospective-SEV3-Warning regard non existing producer app while deploying across stages despite app availability
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4275765427/Retrospective-SEV3-Warning+regard+non+existing+producer+app+while+deploying+across+stages+despite+app+availability
confluence_space: RKB
confluence_page_id: 4275765427
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV3-Warning regard non existing producer app while deploying across stages despite app availability

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV3

Teams:&nbsp;trueBlueAlm Consoles&nbsp;trueBlueMaestro
#### 🕐 Timestamps
Started At:&nbsp;trueBlueJuly 9  3:25 PM WEST

Mitigated At:&nbsp;trueYellowJuly 10 12:32 PM WEST

Resolved At:&nbsp;trueGreenJuly 10 12:32 PM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/689-warning-regard-non-existing-producer-app-while-deploying-across-stages-despite-app-availability)
[Pagerduty incident](https://outsystems.pagerduty.com/incidents/Q3QRLWDO2QNZ7T)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3033771)

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

Tiago Cardoso
#### Summary
----------------------------------------------**CONSIDERATIONS BEFORE PERFORMING THE ESCALATION TO R&amp;D (MANDATORY)**
None of the below points should be overlooked. Failure to do so may imply unnecessary effort.* * *
Ensure the ticket has been **categorized**, otherwise, the R&amp;D escalation will go unnoticed and not be worked on!**1.** For **Incidents**, the **IMAX** was consulted **beforehand** on which:- No incident models were found for the reported symptoms **OR**
- The incident model did not solve the issue **OR**
- The next step indicated in the Incident Model is an escalation to R&amp;D.
**2.** For **Questions**, the ChatODC on the **Slack channel** didn't return an acceptable answer.
**3.** Any other requests that explicitly indicate an R&amp;D escalation is needed.
**4**. **Incident impact assessment** was based on the **prioritization scoring matrix**.* * ***R&amp;D ESCALATION FORM**
Section comments can be removed for R&amp;D easier interpretation.**ISSUE DESCRIPTION AND HOW TO REPRODUCE**- When deploying applications that have references to an application called &quot;Document Archive&quot;, our customer is receiving the warning &quot;This producer doesn't exist in QA&quot;- This also occurs in Production.- When we check the overview page, the &quot;Document Archive&quot; application is indeed only in Development:
- ![](https://supportoutsystems.zendesk.com/attachments/token/cMZNMZT3NnMBch6MqOj1IhdmV/?name=image.png)- However, when we check the list of deployments, this application's 50th revision has in fact been in both QA and Production since Mat 16th, with a security patch applied a couple of weeks ago on June 26th:
- ![](https://supportoutsystems.zendesk.com/attachments/token/3v4d8tf2YEPbS2upmw2Wkzod7/?name=image.png) ![](https://supportoutsystems.zendesk.com/attachments/token/0m1cAWsWskOmpXNxX33yOQdFu/?name=image.png)**IMPACT ON THE CUSTOMER**- The impact isn't significant, as far as we understand it is limited to the false positive warning when deploying any consumer of this application.**TROUBLESHOOTING STEPS &amp; WORKAROUND**- We can't really explain or mitigate this apparent discrepancy. We thought it may be a weird behavior associated with the customer having potentially deleted the application and republished, but that's not the case either.- Weirdly enough, if I try to deploy this application, I'm allowed to deploy any of its versions (as if it was never deployed):
- ![](https://supportoutsystems.zendesk.com/attachments/token/dhbhQDz9tG2w7rEqTcltvs2Xb/?name=image.png)
- We can go as far as the final screen (we did not hit &quot;deploy now&quot; to avoid impacting the customer):
- ![](https://supportoutsystems.zendesk.com/attachments/token/2y2MGCrV0SXj3VOAxS1jMY2sK/?name=image.png)- We would expect to be unable to do this as in the example below:
- ![](https://supportoutsystems.zendesk.com/attachments/token/GKMp61gXf9QhORgRMNPm5vGbv/?name=image.png)**TECH DATA OR ANY OTHER RELEVANT INFO**- Ring: ga
- Tenant Id: fa222c80-3359-4c16-a2cd-ccdebdbd3b9d
- Tenant Prefix: neways
- Region: eu-central-1_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 RetrospectiveinfoDetails
**Ring:** ga
**System-wide impact:**&nbsp; Yes
**Tenant ID:** fa222c80-3359-4c16-a2cd-ccdebdbd3b9d
**Tenant Prefix:** neways
**Routing Error Code:** N/A
**Product Area:** Phoenix::Phoenix Portal::Deployments
### Impact:
On some places of the Portal the customer can't understand which revision is deployed on each stage and it gets a false positive when trying to deploy an app that consumes those ones.
### Investigation and troubleshooting findings:
We couldn't conclude the root case of the issue, because the customer promoted the app to all stages and we lost the chance to understand its root cause.
### Resolution:
As workaround the customer can deploy the affected app to the respective stages.
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/689-warning-regard-non-existing-producer-app-while-deploying-across-stages-despite-app-availability)

**Date**

**Source**

**User**

**Event**
July 9  3:17 PM WESTwebRootly
created an alert via
July 9  3:17 PM WESTwebRootly
Rootly created this incident
July 9  3:17 PM WESTwebRootly
In triage date has been set to July 9  3:17 PM WEST
July 9  3:21 PM WESTwebJo&atilde;o Ros&aacute;rio
Teams has been added: ALM Consoles
July 9  3:21 PM WESTwebJo&atilde;o Ros&aacute;rio
Teams has been removed: Neo DevExperience DeliveryAutomation
July 9  3:24 PM WESTwebJo&atilde;o Ros&aacute;rioJo&atilde;o Ros&aacute;rio has been assigned as EngineerJuly 9  3:25 PM WESTwebJo&atilde;o Ros&aacute;rio
Incident has been started
July 9  5:04 PM WESTwebJo&atilde;o Ros&aacute;rio
The incident is stating two issues:
1. On the Overview page, the app should be presented on all stages, because the app was already deployed on prod and test a couple of times.
2. When deploying an app that consumes the Document Archive app, on the Impact Analysis step is the impact analysis report is showing a warning where the Document Archive app is not deployed on that stage.
July 9  5:13 PM WESTwebJo&atilde;o Ros&aacute;rio
Troubleshooting the first one on https://eng-ga-us-04.outsystems.dev/
July 9  5:36 PM WESTwebJo&atilde;o Ros&aacute;rioSend ZenDesk private comment has been set: Dear support,
&nbsp;&nbsp;
While we are troubleshooting on our side, we would like to request you some extra information.
On the Overview page, can you clear the assets filter and then use the pagination of the table to search for the Document Archive app and show us the result. Thank you.
&nbsp;&nbsp;
Kind regards,
ODC teamJuly 9  5:36 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

Dear support,
&nbsp;&nbsp;
While we are troubleshooting on our side, we would like to request you some extra information.
On the Overview page, can you clear the assets filter and then use the pagination of the table to search for the Document Archive app and show us the result. Thank you.
&nbsp;&nbsp;
Kind regards,
ODC teamJuly 9  5:36 PM WESTwebRootlySend ZenDesk private comment has been unsetJuly 9  5:36 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

July 9  6:00 PM WESTwebRootlyZendesk Private Comment has been set: ----------------------------------------------**Update to R&amp;D**![](https://supportoutsystems.zendesk.com/attachments/token/NRBLxwyBWlsBYNSFyIkYmeQQG/?name=image.png)__July 9  6:00 PM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**![](https://supportoutsystems.zendesk.com/attachments/token/NRBLxwyBWlsBYNSFyIkYmeQQG/?name=image.png)__
July 9  6:00 PM WESTwebRootlyZendesk Private Comment has been changed to: ------------------------------------------------ This notification was sent from Zendesk Support ticket #3033771 to all linked JIRA issues by Ricardo Moreira. --**Update to R&amp;D**Attachment - image.png_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_July 9  6:00 PM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
------------------------------------------------ This notification was sent from Zendesk Support ticket #3033771 to all linked JIRA issues by Ricardo Moreira. --**Update to R&amp;D**Attachment - image.png__
July 10  9:39 AM WESTwebRootly[PagerDuty Incident](https://outsystems.pagerduty.com/incidents/Q3QRLWDO2QNZ7T) has been created.
📧 Notified Tiago Cardoso by email.July 10  9:47 AM WESTwebJo&atilde;o Ros&aacute;rioSwarm has been set: MaestroJuly 10  9:47 AM WESTwebRootly
Pagerduty Integrations added Tiago Cardoso as responder in [PagerDuty](https://outsystems.pagerduty.com/incidents/Q3QRLWDO2QNZ7T)
July 10  9:49 AM WESTwebRootly
Tiago Cardoso joined this [PagerDuty](https://outsystems.pagerduty.com/incidents/Q3QRLWDO2QNZ7T) incident.
July 10  9:49 AM WESTwebRootly
Tiago Cardoso acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q3QRLWDO2QNZ7T). (via Slack)
July 10  9:49 AM WESTwebRootly
Tiago Cardoso joined this [PagerDuty](https://outsystems.pagerduty.com/incidents/Q3QRLWDO2QNZ7T) incident.
July 10  9:52 AM WESTwebJo&atilde;o Ros&aacute;rio
Context: On the ODC Portal the customer is raising an issue where he can't see where a specific app is deployed on QA and Prod environments. On the deployments console the user can navigate to the Overview page and check which app revision is deployed on each stage (data source Asset Portfolio Service) and when promoting an app to an environment, on the Impact Analysis step, the report shows a warning if that app is consuming another one that isn't deployed on that environment (which I believe the Dependency service invokes Asset Portfolio Service to get the revision that he has to analyze). However on deployments history (data source Publish Service) we can see the app was already deployed several times to QA and Prod environment and the last one was made by us to apply a security patch.That said, we would like to confirm with you, if the Asset Portfolio Service is updated accord lying when a security patch is applied.
July 10 10:47 AM WESTwebJo&atilde;o Ros&aacute;rio
Looking into the backend information https://outsystems.grafana.net/d/AUicT3pVz/app-search?orgId=1&amp;var-rings=All&amp;var-appName=docum&amp;var-appKey=&amp;var-envKey=&amp;var-tenantKey=fa222c80-3359-4c16-a2cd-ccdebdbd3b9d the Document Archive app is deployed on all stages.
There may be a database mismatch the Asset Portfolio Service uses.
Maestro team is investigating the issue.
July 10 10:48 AM WESTwebJo&atilde;o Ros&aacute;rioTiago Cardoso has been assigned as EngineerJuly 10 12:05 PM WESTwebRootlyZendesk Private Comment has been changed to: ----------------------------------------------**Update to R&amp;D**
Hey team! Two quick updates we'd like to share:- After the customer deployed a new revision of the affected application (Document Archive), the new revision (51) appeared in QA so that ended up mitigating this.
- A different customer reported this same issue, so we created a case to centralize all customers affected by this in a new zendesk ticket. We have no way to migrate rootly cases between zendesk cases, so we created a new Rootly, ID 693. Please use that one for future communications about this and discard/archive or merge this case into 693.Feel free to reach out if you have any questions, and thanks for your help!_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_July 10 12:05 PM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
Hey team! Two quick updates we'd like to share:- After the customer deployed a new revision of the affected application (Document Archive), the new revision (51) appeared in QA so that ended up mitigating this.
- A different customer reported this same issue, so we created a case to centralize all customers affected by this in a new zendesk ticket. We have no way to migrate rootly cases between zendesk cases, so we created a new Rootly, ID 693. Please use that one for future communications about this and discard/archive or merge this case into 693.Feel free to reach out if you have any questions, and thanks for your help!__
July 10 12:29 PM WESTwebJo&atilde;o Ros&aacute;rio
As the customer already resolved the issue on there side and we are closing the incident and following up here https://rootly.com/account/incidents/693-odc-deployment-cannot-proceed-because-required-version-information-is-missing
July 10 12:32 PM WESTwebJo&atilde;o Ros&aacute;rio
Incident has been resolved
July 10 12:32 PM WESTwebJo&atilde;o Ros&aacute;rioSystem-wide impact has been set: YesJuly 10 12:32 PM WESTwebJo&atilde;o Ros&aacute;rioImpact has been set: On some places of the Portal the customer can't understand which revision is deployed on each stage and it gets a false positive when trying to deploy an app that consumes those ones.July 10 12:32 PM WESTwebJo&atilde;o Ros&aacute;rioInvestigation and troubleshooting findings has been set: We couldn't conclude the root case of the issue, because the customer promoted the app to all stages and we lost the chance to understand its root cause.July 10 12:32 PM WESTwebJo&atilde;o Ros&aacute;rioResolution has been set: As workaround the customer can deploy the affected app to the respective stages.