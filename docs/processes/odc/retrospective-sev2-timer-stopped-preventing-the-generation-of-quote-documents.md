---
title: Retrospective-SEV2-Timer stopped preventing the generation of quote documents
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4228022325/Retrospective-SEV2-Timer+stopped+preventing+the+generation+of+quote+documents
confluence_space: RKB
confluence_page_id: 4228022325
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV2-Timer stopped preventing the generation of quote documents

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV2

Teams:&nbsp;trueBlueNeo Platform Extended Runtime&nbsp;trueBlueSre
#### 🕐 Timestamps
Started At:&nbsp;trueBlueJune 17 10:27 PM WEST

Mitigated At:&nbsp;trueYellowJune 19  2:44 PM WEST

Resolved At:&nbsp;trueGreenJune 19  2:44 PM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/570-timer-stopped-preventing-the-generation-of-quote-documents)
[Pagerduty incident](https://outsystems.pagerduty.com/incidents/Q2VGF7CS39AYMK)

[Slack channel](https://slack.com/app_redirect?channel=C0783CLG5V5&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3023824)

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

Sam Audu
#### Summary
----------------------------------------------**ISSUE DESCRIPTION AND HOW TO REPRODUCE**- An issue caused an important timer to not stop running and from there all subsequent requests were pending, not only after 5 hours for the system to become stable again**IMPACT ON THE CUSTOMER**- This happened in the production stage. this timer created the quote pdf documents that OutSystems sends to customers for signature our Sales team in APAC could not generate the quote documents to send to our customers due to the pending requests. This unexpected issue can have a considerable impact due to the important duty of this timer; a fix/acknowledgment of this issue is necessary to guarantee the correct behavior of the platform, especially in this time due to the end of the quarter**TROUBLESHOOTING STEPS &amp; WORKAROUND**- While analyzing the situation we found the occurrence the timers were stuck and overlapping in the execution- https://outsystems.grafana.net/d/cdnz5ip93m9dsa/timer-jobs?orgId=1&amp;var-severity=All&amp;var-cluster=runp-osall-us-east-1-01&amp;var-timer=timer-b4783d223a01f0f0329424bb2775c9258a583cbf687497&amp;from=1718579289584&amp;to=1718603371496- ![](https://supportoutsystems.zendesk.com/attachments/token/NCdXwCYpQ0bjisAqaIYOKjb5b/?name=image.png)
- It came to our attention that during this whole occurrence, there was a noticeable pattern indicating some issues with NATS and Istio- When the timer execution started, NATS exceptions/warnings were raised- ![](https://supportoutsystems.zendesk.com/attachments/token/SCiSPqsqHJFFjPwPRdiITw38J/?name=image.png)- In this example, it took more than an hour for the attempt to execute to end in an error- ![](https://supportoutsystems.zendesk.com/attachments/token/uTeM2put8HtpKHDspEqOEoJ0u/?name=image.png)- Right before that error, we can see the Istio error severity log here: (https://outsystems.grafana.net/goto/_Vs_8E8Ig?orgId=1)
- Considering the stage where this happened and since the cause has not been identified yet, it's crucial to understand what went wrong and how to avoid this in the future to avoid a major impact**TECH DATA OR ANY OTHER RELEVANT INFO**
Ring: osall
Tenant Id: fae0814c-7560-49cc-886f-6b4eccb6709f
Tenant Prefix: extranet
Region: us-east-1
App name: ODC Quote Generator.
Timer name: Timer_SendPDF_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 RetrospectiveinfoDetails
**Ring:** osall
**System-wide impact:**&nbsp; No
**Tenant ID:** fae0814c-7560-49cc-886f-6b4eccb6709f
**Tenant Prefix:** extranet
**Routing Error Code:** N/A
**Product Area:** Phoenix::Application Runtime::Timers
### Impact:
As ICE is not part of our stage 1 rollout for rootly, let's close this case stating that it is being followed up in [https://outsystemsrd.atlassian.net/browse/RDINC-25402](https://outsystemsrd.atlassian.net/browse/RDINC-25402)
### Investigation and troubleshooting findings:
As ICE is not part of our stage 1 rollout for rootly, let's close this case stating that it is being followed up in [https://outsystemsrd.atlassian.net/browse/RDINC-25402](https://outsystemsrd.atlassian.net/browse/RDINC-25402)
### Resolution:
As ICE is not part of our stage 1 rollout for rootly, let's close this case stating that it is being followed up in [https://outsystemsrd.atlassian.net/browse/RDINC-25402](https://outsystemsrd.atlassian.net/browse/RDINC-25402)
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/570-timer-stopped-preventing-the-generation-of-quote-documents)

**Date**

**Source**

**User**

**Event**
June 17 10:26 PM WESTwebRootly
created an alert via
June 17 10:26 PM WESTwebRootly
Rootly created this incident
June 17 10:26 PM WESTwebRootly
In triage date has been set to June 17 10:26 PM WEST
June 17 10:26 PM WESTwebRootly[Slack Channel](https://slack.com/app_redirect?channel=C0783CLG5V5&amp;team=T041063TZ) has been createdJune 17 10:26 PM WESTwebRootly
Ring: osall
System-wide impact:  
Tenant ID: fae0814c-7560-49cc-886f-6b4eccb6709f
Tenant Prefix: extranet
Routing Error Code: N/A
Product Area: Phoenix::Application Runtime::Timers
June 17 10:26 PM WESTwebRootly[PagerDuty Incident](https://outsystems.pagerduty.com/incidents/Q2VGF7CS39AYMK) has been created.
📲 Notified Sam Audu by push notification.  (via iPhone)June 17 10:26 PM WESTwebRootlySam Audu has been assigned as EngineerJune 17 10:27 PM WESTwebRootly
Sam Audu acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q2VGF7CS39AYMK). (via Mobile)
June 17 10:27 PM WESTwebSam Audu
Incident has been started
June 17 10:27 PM WESTwebRootly
Pagerduty Integrations acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q2VGF7CS39AYMK). (via Mobile)
June 17 11:11 PM WESTslackSam Audu
We are currently do not see any impact at a system wide level, however we are investigating what do what cause the```2024-06-17 00:37:20.086	TimerExecutor_timer-b4783d223a01f0f0329424bb2775c9258a583cbf687497   	Error   	Error shutting down istio```
[image.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mzk1NDIwLCJwdXIiOiJibG9iX2lkIn19--069c4a1ff1075c0f8dd4a7c11c7a98c84c57b647/image.png)June 17 11:53 PM WESTwebSam AuduSwarm has been set: Extended RuntimeJune 17 11:53 PM WESTwebRootly
Pagerduty Integrations added Pedro Pita as responder in [PagerDuty](https://outsystems.pagerduty.com/incidents/Q2VGF7CS39AYMK)
June 17 11:54 PM WESTwebRootly
Sam Audu added Pedro Pita as responder in [PagerDuty](https://outsystems.pagerduty.com/incidents/Q2VGF7CS39AYMK)
June 17 11:54 PM WESTwebRootly
Pedro Pita joined this [PagerDuty](https://outsystems.pagerduty.com/incidents/Q2VGF7CS39AYMK) incident.
June 17 11:54 PM WESTwebRootly
Pedro Pita joined this [PagerDuty](https://outsystems.pagerduty.com/incidents/Q2VGF7CS39AYMK) incident.
June 19  2:44 PM WESTslackhenrique.fonseca
Hi @Sam Audu , @Kevin TekThanks for the investigation. Even though this didn't have any system wide impact, you were able to pinpoint some errors that were affecting the custoemr timer execution. Thanks that's the way to go.As ICE is not part of our stage 1 rollout for rootly, let's close this case stating that it is being followed up in [https://outsystemsrd.atlassian.net/browse/RDINC-25402](https://outsystemsrd.atlassian.net/browse/RDINC-25402)
June 19  2:44 PM WESTwebHenrique Fonseca
Incident has been resolved
June 19  2:44 PM WESTwebHenrique FonsecaSystem-wide impact has been set: NoJune 19  2:44 PM WESTwebHenrique FonsecaImpact has been set: As ICE is not part of our stage 1 rollout for rootly, let's close this case stating that it is being followed up in https://outsystemsrd.atlassian.net/browse/RDINC-25402June 19  2:44 PM WESTwebHenrique FonsecaInvestigation and troubleshooting findings has been set: As ICE is not part of our stage 1 rollout for rootly, let's close this case stating that it is being followed up in https://outsystemsrd.atlassian.net/browse/RDINC-25402June 19  2:44 PM WESTwebHenrique FonsecaResolution has been set: As ICE is not part of our stage 1 rollout for rootly, let's close this case stating that it is being followed up in https://outsystemsrd.atlassian.net/browse/RDINC-25402