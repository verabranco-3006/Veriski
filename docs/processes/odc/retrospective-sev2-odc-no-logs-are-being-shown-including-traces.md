---
title: Retrospective-SEV2-ODC - No logs are being shown including traces
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4323180612/Retrospective-SEV2-ODC+-+No+logs+are+being+shown+including+traces
confluence_space: RKB
confluence_page_id: 4323180612
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV2-ODC - No logs are being shown including traces

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV2

Teams:&nbsp;trueBlueSre&nbsp;trueBlueAnalytics
#### 🕐 Timestamps
Started At:&nbsp;trueBlueJuly 31 10:28 AM WEST

Mitigated At:&nbsp;trueYellowJuly 31 10:29 AM WEST

Resolved At:&nbsp;trueGreenJuly 31 10:29 AM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/777-odc-no-logs-are-being-shown-including-traces-47bb7883-fe89-401c-bcb6-4dd77e3d1f68)
[Pagerduty incident](https://outsystems.pagerduty.com/incidents/Q05HZJUK7SI401)

[Slack channel](https://slack.com/app_redirect?channel=C07F1NLNGPK&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3042542)

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

Karthik k
#### Summary
----------------------------------------------**R&amp;D ESCALATION FORM**
Section comments can be removed for R&amp;D easier interpretation.**ISSUE DESCRIPTION AND HOW TO REPRODUCE**
Customer are having the error OS-MONS-50302![](https://supportoutsystems.zendesk.com/attachments/token/xjjO5ZA6adqbQrWDbCKey8LZd/?name=image.png)This happens with all stages, including production.We've recently had a similar situation regarding the logs so we don't know if the fix also contributed for this error.**IMPACT ON THE CUSTOMER**
- Some customers report this as sev3 however, we have reports where the customer noticed this error because they are troubleshooting their development. Additionally this also happens in Production making users unable to understand if there's any on-going issue. Following our internal form, this will be set as sev2**TROUBLESHOOTING STEPS &amp; WORKAROUND**
We were able to replicate this error in our Sandbox that is in GA.**TECH DATA OR ANY OTHER RELEVANT INFO**
Ring: ga
Tenant Id: 398a3a52-e8fb-47dc-beb6-ec1b9f6c38df
Tenant Prefix: nordnet
Region: eu-central-1
IFY.2GP.T9R.D26.YDW.7OS.XUZ.QOU&amp;Ring: ea
Tenant Id: bcdd20fe-ef31-4465-a009-e8850471415c
Tenant Prefix: joaoleitaodemos
Region: eu-central-1
4NK.VO5.HCO.EJY.5HS.RVV.TAE.QUT&amp;Ring: ga
Tenant Id: 6b0f5f2d-90c2-4880-8c72-b3fcb3dfd11f
Tenant Prefix: agoria
Region: eu-central-1
BNT.OPA.6BN.NUB.BQT.U4Q.3UX.WOU_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 RetrospectiveinfoDetails
**Ring:** -
**System-wide impact:**&nbsp; 
**Tenant ID:** N/A
**Tenant Prefix:** N/A
**Routing Error Code:** OS-MONS
**Product Area:** -
### Impact:
LOW
### Investigation and troubleshooting findings:
Secrets created as part of secret rotation was not updated in cache 
### Resolution:
Restarting of pods helped clear the cache and get new secrets
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/777-odc-no-logs-are-being-shown-including-traces-47bb7883-fe89-401c-bcb6-4dd77e3d1f68)

**Date**

**Source**

**User**

**Event**
July 30 11:46 AM WESTwebRootly
created an alert via
July 30 11:46 AM WESTwebRootly
Rootly created this incident
July 30 11:46 AM WESTwebRootly
In triage date has been set to July 30 11:46 AM WEST
July 30 11:46 AM WESTwebRootly[Slack Channel](https://slack.com/app_redirect?channel=C07F1NLNGPK&amp;team=T041063TZ) has been createdJuly 30 11:46 AM WESTwebRootly
Ring: -
System-wide impact:  
Tenant ID: N/A
Tenant Prefix: N/A
Routing Error Code: OS-MONS
Product Area: -
July 30 11:47 AM WESTwebRootly[PagerDuty Incident](https://outsystems.pagerduty.com/incidents/Q05HZJUK7SI401) has been created.
📧 Notified Karthik by email.&nbsp;&nbsp;📲 Notified Karthik by push notification.  (via Android)&nbsp;&nbsp;📲 Notified Karthik by push notification.  (via Android)&nbsp;&nbsp;📲 Notified Karthik by push notification.  (via Android)July 30 11:47 AM WESTwebRootlyKarthik k has been assigned as EngineerJuly 30 11:47 AM WESTwebRootly
Karthik acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q05HZJUK7SI401). (via Mobile)
July 30 11:56 AM WESTwebRootly
This incident was instantiated in Jira: RDINC-27842. Please work the incident using Rootly
July 30 12:38 PM WESTwebRootly
Karthik added Vindhya as responder in [PagerDuty](https://outsystems.pagerduty.com/incidents/Q05HZJUK7SI401)
July 30 12:39 PM WESTwebRootly
Vindhya joined this [PagerDuty](https://outsystems.pagerduty.com/incidents/Q05HZJUK7SI401) incident.
July 30 12:42 PM WESTwebRootly
Delegated to Data Platform Team by Karthik through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q05HZJUK7SI401)
July 30 12:42 PM WESTwebRootly
Vindhya acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q05HZJUK7SI401). (via Mobile)
July 30 12:46 PM WESTwebRootly
This incident was instantiated in Jira: RDINC-27842. Please work the incident using Rootly
July 30  1:02 PM WESTwebRootly
Vindhya added Joel Carvalho as responder in [PagerDuty](https://outsystems.pagerduty.com/incidents/Q05HZJUK7SI401)
July 30  1:04 PM WESTwebRootly
Joel Carvalho joined this [PagerDuty](https://outsystems.pagerduty.com/incidents/Q05HZJUK7SI401) incident.
July 30  1:36 PM WESTwebRootly
Vindhya marked the incident as resolved through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q05HZJUK7SI401)
July 30  3:02 PM WESTwebRootlyZendesk Private Comment has been set: ------------------------------------------------ This notification was sent from Zendesk Support ticket #3042542 to all linked JIRA issues by Ricardo Moreira. --**Update to R&amp;D**- Hello TeamWe're receiving some updates that the logs are visible again.
Can you confirm if you performed any action? We didn't receive any communication.Kind regards__July 30  3:03 PM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
------------------------------------------------ This notification was sent from Zendesk Support ticket #3042542 to all linked JIRA issues by Ricardo Moreira. --**Update to R&amp;D**- Hello TeamWe're receiving some updates that the logs are visible again.
Can you confirm if you performed any action? We didn't receive any communication.Kind regards__
July 30  3:03 PM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
------------------------------------------------ This notification was sent from Zendesk Support ticket #3042542 to all linked JIRA issues by Ricardo Moreira. --**Update to R&amp;D**- Hello TeamWe're receiving some updates that the logs are visible again.
Can you confirm if you performed any action? We didn't receive any communication.Kind regards__
July 31 10:01 AM WESTwebHenrique Fonseca
Teams has been added: SRE
July 31 10:28 AM WESTwebVindhya G
Incident has been started
July 31 10:29 AM WESTwebVindhya G
Incident has been resolved
July 31 10:29 AM WESTwebVindhya GImpact has been set: LOWJuly 31 10:29 AM WESTwebVindhya GInvestigation and troubleshooting findings has been set: Secrets created as part of secret rotation was not updated in cache July 31 10:29 AM WESTwebVindhya GResolution has been set: Restarting of pods helped clear the cache and get new secrets