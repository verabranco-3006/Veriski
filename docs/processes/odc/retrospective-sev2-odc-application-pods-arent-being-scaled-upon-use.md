---
title: Retrospective-SEV2-ODC - Application pods aren't being scaled upon use
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4298604547/Retrospective-SEV2-ODC+-+Application+pods+aren+t+being+scaled+upon+use
confluence_space: RKB
confluence_page_id: 4298604547
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV2-ODC - Application pods aren't being scaled upon use

## 📘 Overview
Author:&nbsp;Rootlytrue

Severity:&nbsp;SEV2Redtrue

Teams:&nbsp;Global RoutingBluetrue&nbsp;SreBluetrue
#### 🕐 Timestamps
Started At:&nbsp;July 19 11:21 AM WESTBluetrue

Mitigated At:&nbsp;July 19 12:42 PM WESTYellowtrue

Resolved At:&nbsp;July 19  1:58 PM WESTGreentrue
#### 🔗 Links
[Incident Page](https://rootly.com/account/incidents/738-odc-application-pods-aren-t-being-scaled-upon-use)

[Pagerduty incident](https://outsystems.pagerduty.com/incidents/Q0PAWCZN3AX1C6)

[Slack channel](https://slack.com/app_redirect?channel=C07D3GXPTFF&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3038783)

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

Henrique Santos
#### Summary
----------------------------------------------**CONSIDERATIONS BEFORE PERFORMING THE ESCALATION TO R&amp;D (MANDATORY)**
None of the below points should be overlooked. Failure to do so may imply unnecessary effort.* * *
Ensure the ticket has been **categorized**, otherwise, the R&amp;D escalation will go unnoticed and not be worked on!**1.** For **Incidents**, the **IMAX** was consulted **beforehand** on which:- No incident models were found for the reported symptoms **OR**
- The incident model did not solve the issue **OR**
- The next step indicated in the Incident Model is an escalation to R&amp;D.
**2.** For **Questions**, the ChatODC on the **Slack channel** didn't return an acceptable answer.
**3.** Any other requests that explicitly indicate an R&amp;D escalation is needed.
**4**. **Incident impact assessment** was based on the **prioritization scoring matrix**.* * ***R&amp;D ESCALATION FORM**
Section comments can be removed for R&amp;D easier interpretation.**ISSUE DESCRIPTION AND HOW TO REPRODUCE**- All across the EA ring, applications in the Development Stage are completely inaccessible; when customers try to load them, they get &quot;no healthy upstream&quot;:
- ![](https://supportoutsystems.zendesk.com/attachments/token/FOP3dDcDowIXiuYpZ3lrmxEMl/?name=image.png)- Usually, this would be related to scale to zero and would be gone in a few seconds/minutes, however, it seems that for many hours (12+), there have been no scale-ups of apps in the EA Ring:
- Harmony Innosoft- ![](https://supportoutsystems.zendesk.com/attachments/token/jMr7qhlim6KwrAIvRL51wsBU2/?name=image.png)
- HONU SRL:- ![](https://supportoutsystems.zendesk.com/attachments/token/QSm6PMLjCl0qunEbZLPCu2N0G/?name=image.png)- If we look at a very particular example, we can see that the last time the pod was up for an application was at 7 PM (UTC) yesterday (July 18th):
- ![](https://supportoutsystems.zendesk.com/attachments/token/5iZSrFHphupgbyBZjNXXktO2B/?name=image.png)**IMPACT ON THE CUSTOMER**- As far as we know, this is affecting every single application in the Development stage of a Ring in EA. So far, only customers in the EA-Central-1 region have reported this, but it's unclear to us if this is due to APAC/AMER being outside business hours, or if this is truly isolated to EA-Central-1 region.**TROUBLESHOOTING STEPS &amp; WORKAROUND**- None was performed given the widespread nature of this issue.**TECH DATA OR ANY OTHER RELEVANT INFO**- So far, this has already been reported by 4 different tenants:- Case: 3038761- Ring: ea- Tenant Id: 0bdbd1b0-e150-4db9-ab25-65d3e8256118- Tenant Prefix: harmonygroup- Region: eu-central-1- #3038735- Ring: ea- Tenant Id: 2b229f48-76a4-47e0-9ca8-86d069172240- Tenant Prefix: synobsys- Region: eu-central-1- #3038772- Ring: ea- Tenant Id: 5167f99c-5c3a-4b76-af38-d3ad8877f7da- Tenant Prefix: ntt-data- Region: eu-central-1- #3038726- Ring: ea- Tenant Id: 05dd8920-7593-42b3-90d5-442e8555430d- Tenant Prefix: honu- Region: eu-central-1_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 Retrospective### Details
**Ring:** ea
**System-wide impact:**&nbsp; Yes
**Tenant ID:** N/A
**Tenant Prefix:** N/A
**Routing Error Code:** OS-CLRT
**Product Area:** -
### Impact:
Applications deployed in `rundev-ea-eu-ce-1-01` would not be scaled from zero since around 05:38 UTC on July 19th. This timestamp was defined based on the lack of logs from the running `keda-istio-external-scaler` pod from this point onwards.

This means that there was no further logic being applied, so:

- 
Applications that were scaled to zero would not be scaled if there was a request to them after this timestamp;

- 
Applications that were already scaled (i.e. had requests to them before) possibly were still working until one hour after the last use before this timestamp, as we presume that Keda would apply the cooldown period of 1 hour and delete the application pod. This was not possible to fully confirm;

- 
We are not sure if new app deployments were successful as the application pod would be created and at least exist during the one hour cooldown period.

### Investigation and troubleshooting findings:
The `keda-istio-external-scaler` pod that was running when the incident was raised in `rundev-ea-eu-ce-1-01` was created at 03:21 UTC and, according to the logs, was working normally until 05:38 UTC, where it stopped showing any logs regarding service activity. Only logs for containerized tests were still on-going and the pod&rsquo;s CPU and memory resources were not near the resource limits.
We did not find any further error logs on the pod.

The `keda-operator` pod that was the leader at this time was showing getting metrics error from the `keda-istio-external-scaler` endpoint, where it would get a timeout. According to the logs, this specific error started at 05:39:20 UTC.

What was observed while the incident was on-going was that Keda would not scale from zero application pods that were receiving requests after 05:39:20 UTC and at least some application pods that existed at 05:39:20 UTC were scaled down at most one hour after, which is the defined cooldown period.

At this point, it seemed that the  `keda-operator` could not communicate with `keda-istio-external-scaler` and `keda-istio-external-scaler` stopped processing Istio metrics.
### Resolution:
SRE was requested to recreate the `keda-istio-external-scaler` pod in the `rundev-ea-eu-ce-1-01` cluster and the scale to zero functionality started working immediately after the new pod was created, as new applications pods were being created, there were log messages on `keda-istio-external-scaler` and the `keda-operator` leader pod was no longer had logs showing issues retrieving metrics from `keda-istio-external-scaler`.
## Tasks performed during incident resolution:
- 
&nbsp;Restarting (i.e. deleting the existing) `keda-istio-external-scaler` pod in the cluster.

## Executive Summary
[Guidelines](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4144496679/Incident+Retrospectives+-+Playbook#STEP-3---Write-the-Executive-Summary)

On July 19th between 05:39:20 UTC and 12:18 UTC, requests done to the majority of applications hosted in `rundev-ea-eu-ce-1-01` (Development stage, Ring +2 EA - EU) would fail. 
This was caused by the fact that the component (&ldquo;Keda&rdquo;) responsible for scaling applications from 0 replicas to 1 replica when a request was done to them was not performing as expected.

This was solved at the time by restarting the &ldquo;keda-istio-external-scaler&ldquo; component, which is used by &ldquo;Keda&ldquo; to retrieve the request metrics for each application to know when to scale them. Nevertheless, &ldquo;Keda&ldquo; was expected to scale all applications to 1, as a fallback mechanism as it couldn&rsquo;t retrieve request metrics, but it did not do so.

After the incident, &ldquo;Keda&ldquo; memory resources were increased for this cluster and others with more usage and this issue did not happen anymore.
We believe that the main root cause was the lack of memory on &ldquo;Keda&ldquo;. Nevertheless, we are following-up with more investigation on &ldquo;keda-istio-external-scaler&ldquo; in order to make it more resilient to these faults from &ldquo;Keda&ldquo;.
## Root Causes 
[Guidelines](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4144496679/Incident+Retrospectives+-+Playbook#STEP-1---Perform-the-Root-Cause-Analysis)

If the customer needs formal RCA, please fill out the following field with the document URL

[Please follow these instructions and place the RCA URL in the field below.](https://docs.google.com/document/d/13rXmBsOJh73nV2D6Z17SIBGBu2HOTWty5ddsvU000JM/edit#heading=h.bqxasxszr5q)

RCA URL

&lt;Place the URL of the customer RCA here if you have created one&gt;

In the aftermath of this event, we proceeded to investigate what could have caused this issue. While the investigation was on-going, there were actually two similar incidents detected on July 25th in `rundev-ea-eu-ce-1-01` and `rundev-ea-us-east-1-01`.
As the root causes seemed the same, we focused on the details from these last incidents. From here we noticed that, when the issue happened, in all occurrences, the `keda-istio-external-scaler` pod would have the following behavior:

- 
The Proxies connected metric would go up:

- 
The Ingested Metrics rate goes to zero, which means that it is not [going up](https://github.com/OutSystems/keda-istio-external-scaler/blob/main/pkg/counter/service.go#L61):

- 
The Removed metrics counter stays still, which means that it is not [being increased](https://github.com/OutSystems/keda-istio-external-scaler/blob/main/pkg/counter/service.go#L120):

- 
No &ldquo;service is active&rdquo; logs:

- 
The CPU usage goes down a bit and the memory usage starts going up:

Also, we did notice that, in these two clusters, the `keda-operator` pods had several restarts and the leader one would always have high memory usage and eventually restart:

Interestingly enough, when `keda-istio-external-scaler` was not responding, the memory usage on the leader Keda operator pod would go down (hence the low memory phase in the picture above).

As the next action items, we did the following:

- 
Created [an alert ](https://outsystems.grafana.net/alerting/grafana/ddsu9vmf8hpmod/view)that proactively warns us if Keda-istio-external-scaler is not ingesting metrics, which seemed to be an indicator of the issue;

- 
Requested ICE to increase the memory of Keda operator to avoid Keda operator restarts - RDICE-3624ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

- 
This fix was installed in EA in August 6th 2024.

After this incident and 2 occurrences that happened, we have not had any occurrence of this issue anymore. 

Additionally, after reviewing this issue, we understood that Keda was also not operating as expected as all application ScaledObjects have a fallback replicas, which means all applications in those clusters should have scaled to 1 ([docs](https://keda.sh/docs/2.14/concepts/scaling-deployments/#fallback)) as Keda was failing to retrieve metrics, as indicated in the logs, until `keda-istio-external-scaler` started responding again:

We did a [simple test in -3](https://outsystemsrd.atlassian.net/browse/RDGRS-706?focusedCommentId=1187729) in order to validate that Keda was respecting the fallback replica count, by making `keda-istio-external-scaler` unavailable. In this, we observed that Keda did act as expected and scaled all applications to 1.
As such, we have reason to believe that, at the time of the incident, Keda was not able to use the fallback replicas, as it was constantly restarting, therefore it would lose count of the `failureThreshold` and not go into fallback mode.

In sum, we believe that the main root cause was the lack of memory resources on `keda-operator`, that may have caused the `keda-istio-external-scaler`&rsquo;s erratic behavior and the fallback mechanism to not be triggered.
Nevertheless, we are following-up on RDGRS-841ef8955cb-cb21-32a7-b692-01ace42388d6System Jira in order to try to replicate the behavior that was observed and make `keda-istio-external-scaler` more resilient to these failures from `keda-operator`.

## ⌛ Timeline
[View on Rootly](https://rootly.com/account/incidents/738-odc-application-pods-aren-t-being-scaled-upon-use)

**Date**

**Source**

**User**

**Event**

July 19 11:20 AM WEST

web

Rootly

created an alert via

July 19 11:20 AM WEST

web

Rootly

Rootly created this incident

July 19 11:20 AM WEST

web

Rootly

In triage date has been set to July 19 11:20 AM WEST

July 19 11:20 AM WEST

web

Rootly

[Slack Channel](https://slack.com/app_redirect?channel=C07D3GXPTFF&amp;team=T041063TZ) has been created

July 19 11:21 AM WEST

web

Rootly

Ring: -
System-wide impact:  
Tenant ID: N/A
Tenant Prefix: N/A
Routing Error Code: OS-CLRT
Product Area: -

July 19 11:21 AM WEST

web

Rootly

[PagerDuty Incident](https://outsystems.pagerduty.com/incidents/Q0PAWCZN3AX1C6) has been created.

📧 Notified David Pires by email.

&nbsp;&nbsp;

📧 Notified David Pires by email.

&nbsp;&nbsp;

📲 Notified David Pires by push notification.  (via Android)

July 19 11:21 AM WEST

web

Rootly

David Pires has been assigned as Engineer

July 19 11:21 AM WEST

web

David Pires

Incident has been started

July 19 11:21 AM WEST

web

Rootly

Pagerduty Integrations acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q0PAWCZN3AX1C6). (via Api)

July 19 11:27 AM WEST

web

David Pires

Swarm has been set: Backend Runtime

July 19 11:27 AM WEST

web

Rootly

Pagerduty Integrations added Rui Garcia as responder in [PagerDuty](https://outsystems.pagerduty.com/incidents/Q0PAWCZN3AX1C6)

July 19 11:27 AM WEST

web

Rootly

Pagerduty Integrations added Rui Garcia as responder in [PagerDuty](https://outsystems.pagerduty.com/incidents/Q0PAWCZN3AX1C6)

July 19 11:29 AM WEST

web

Rootly

Rui Garcia joined this [PagerDuty](https://outsystems.pagerduty.com/incidents/Q0PAWCZN3AX1C6) incident.

July 19 11:30 AM WEST

web

David Pires

Rui Garcia has been assigned as Engineer

July 19 11:33 AM WEST

web

Rootly

Delegated to EP for Neo BackendRuntime by David Pires through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q0PAWCZN3AX1C6)

July 19 11:34 AM WEST

web

Rootly

Rui Garcia acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q0PAWCZN3AX1C6). (via Api)

July 19 11:40 AM WEST

web

David Pires

Teams has been removed: [Client Runtime](/account/teams/client-runtime/status)

July 19 11:47 AM WEST

slack

Henrique Santos (hqs)

here's what I've found so far:
In fact, the keda-istio service on `rundev-ea-eu-ce-1-01` [stopped outputting logs](https://outsystems.grafana.net/goto/mf1PzHuIg?orgId=1) related to scaling at around 05:30. This is not the case for the other 2 rundev stamps in EA (us-east-1 and eu-ce-1), as both appear to be working fine.I jumped in the cluster in read only and didn't see any issue in the pods related to Keda, however when looking at the Keda operator logs, I see several errors. When [searching for this error](https://outsystems.grafana.net/goto/rthCzNuSR?orgId=1) in Grafana, it seems that Keda is having issues getting a metric and it matches the timeframe on the keda-istio-scaler service

[image.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDEzODM1LCJwdXIiOiJibG9iX2lkIn19--26d97f2cf2bb83d0a2b7f4f7cea14077c6f6e63d/image.png)

[image.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDEzODM2LCJwdXIiOiJibG9iX2lkIn19--f89a25af9d3b1d126be4597e048933a7f44bff86/image.png)

[image.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDEzODM3LCJwdXIiOiJibG9iX2lkIn19--c9b698bf36ddf6a845eff961155af8d4d73b0db6/image.png)

[image.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDEzODM4LCJwdXIiOiJibG9iX2lkIn19--288be312ae9dae148e484d5a5874caa6bff554f5/image.png)

July 19 11:54 AM WEST

web

Henrique Santos

Teams has been added: [Global Routing](/account/teams/global-routing/status)

July 19 11:55 AM WEST

web

Rui Garcia

Henrique Santos has been assigned as Engineer

July 19 11:58 AM WEST

web

Rui Garcia

Teams has been removed: [Backend Runtime](/account/teams/backend-runtime/status)

July 19 11:59 AM WEST

web

Rootly

Delegated to Global Routing Policy 1 by Rui Garcia through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q0PAWCZN3AX1C6)

July 19 11:59 AM WEST

web

Rootly

Henrique Santos acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q0PAWCZN3AX1C6). (via Api)

July 19 12:07 PM WEST

slack

Henrique Santos (hqs)

although I have no suspicion on what may have happened, as I'm not knowledgeble on this. I will swarm with SRE to restart the keda-istio-scaler pod

July 19 12:07 PM WEST

web

Rootly

Zendesk Private Comment has been set: ------------------------------------------------ This notification was sent from Zendesk Support ticket #3038783 to all linked JIRA issues by Gon&ccedil;alo Silva. --**Update to R&amp;D**
Hey team! A new Tenant in the EA Ring has also reported this, here's its information:- Zendesk Case: 3038805- Ring: ea- Tenant Id: 3313c749-2159-4df2-98e2-f29dbf73263e- Tenant Prefix: creetionodc- Region: eu-central-1Looking forward to an update from you; if there's any info you need from us, let us know!Best regards,__

July 19 12:07 PM WEST

web

Rootly

NEW MESSAGE FROM GLOBAL SUPPORT:
------------------------------------------------ This notification was sent from Zendesk Support ticket #3038783 to all linked JIRA issues by Gon&ccedil;alo Silva. --**Update to R&amp;D**
Hey team! A new Tenant in the EA Ring has also reported this, here's its information:- Zendesk Case: 3038805- Ring: ea- Tenant Id: 3313c749-2159-4df2-98e2-f29dbf73263e- Tenant Prefix: creetionodc- Region: eu-central-1Looking forward to an update from you; if there's any info you need from us, let us know!Best regards,__

July 19 12:08 PM WEST

web

Rootly

NEW MESSAGE FROM GLOBAL SUPPORT:
------------------------------------------------ This notification was sent from Zendesk Support ticket #3038783 to all linked JIRA issues by Gon&ccedil;alo Silva. --**Update to R&amp;D**
Hey team! A new Tenant in the EA Ring has also reported this, here's its information:- Zendesk Case: 3038805- Ring: ea- Tenant Id: 3313c749-2159-4df2-98e2-f29dbf73263e- Tenant Prefix: creetionodc- Region: eu-central-1Looking forward to an update from you; if there's any info you need from us, let us know!Best regards,__

July 19 12:10 PM WEST

web

Henrique Santos

Send ZenDesk private comment has been set: Hello Global Support,We have detected an issue with the Scale to zero functionality in the rundev cluster in eu-central-1.
The other regions appear to be okay, so please let us know if there are any reports regarding the other 2 regions.In the meantime, we are investigating and we will try to mitigate this as soon as possible.

July 19 12:10 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:
Hello Global Support,We have detected an issue with the Scale to zero functionality in the rundev cluster in eu-central-1.
The other regions appear to be okay, so please let us know if there are any reports regarding the other 2 regions.In the meantime, we are investigating and we will try to mitigate this as soon as possible.

July 19 12:10 PM WEST

web

Rootly

Send ZenDesk private comment has been unset

July 19 12:10 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:

July 19 12:10 PM WEST

web

Henrique Santos

Swarm has been set: SRE

July 19 12:10 PM WEST

web

Henrique Santos

Swarm has been unset: Backend Runtime

July 19 12:10 PM WEST

web

Rootly

Pagerduty Integrations added Miguel Saraiva Afonso as responder in [PagerDuty](https://outsystems.pagerduty.com/incidents/Q0PAWCZN3AX1C6)

July 19 12:11 PM WEST

web

Rootly

Miguel Saraiva Afonso joined this [PagerDuty](https://outsystems.pagerduty.com/incidents/Q0PAWCZN3AX1C6) incident.

July 19 12:11 PM WEST

web

Rootly

Miguel Saraiva Afonso acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q0PAWCZN3AX1C6). (via Api)

July 19 12:20 PM WEST

slack

Henrique Santos (hqs)

SRE restarted the pod at 12:18 UTC. The new pod is already showing &quot;service active&quot; logs, which indicate that it is functioning. Let's wait a few minutes to confirm this behavior

[image.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDEzODU3LCJwdXIiOiJibG9iX2lkIn19--55937d223d9118e4fb7c7e8a7f23c96b36e10510/image.png)

July 19 12:30 PM WEST

web

Henrique Santos

Send ZenDesk private comment has been set: Hello Global Support,We have performed the mitigation of restarting the service that took care of the scaling.
On our side, it appears that the scale to zero functionality is working now normally.Could you please verify on your side as well and provide us feedback?Thank you,
Henrique Santos | Global Routing

July 19 12:30 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:
Hello Global Support,We have performed the mitigation of restarting the service that took care of the scaling.
On our side, it appears that the scale to zero functionality is working now normally.Could you please verify on your side as well and provide us feedback?Thank you,
Henrique Santos | Global Routing

July 19 12:30 PM WEST

web

Rootly

Send ZenDesk private comment has been unset

July 19 12:30 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:

July 19 12:34 PM WEST

slack

Henrique Santos (hqs)

for reference, we see new application pods running. When the service was restarted, it seems that several application pods were deployed, possibly due to metrics in queue.Again, in the keda-istio-scaler we still see recent &quot;service is active&quot; and &quot;received event&quot; logs. In the Keda operator, we no longer see the continuous getting metrics errors and it appears that there are normal reconcile logs

[image.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDEzODY2LCJwdXIiOiJibG9iX2lkIn19--cdff9677a9777ecec2a019a8e81f23e76510e9b0/image.png)

[image.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDEzODY3LCJwdXIiOiJibG9iX2lkIn19--3316d8b549dbd010d70065fa1b374f7e4d943036/image.png)

[image.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDEzODY4LCJwdXIiOiJibG9iX2lkIn19--f7f424ef82f0a864b41a3520db547076eae699bc/image.png)

[image.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDEzODY5LCJwdXIiOiJibG9iX2lkIn19--7f48e8cff846661088b05ff313bddf791418a227/image.png)

July 19 12:42 PM WEST

web

Henrique Santos

Incident has been mitigated

July 19  1:31 PM WEST

slack

Henrique Santos (hqs)

After one hour, the keda-istio-scaler continues to output &quot;service is active&quot; and &quot;received event&quot; logs.Regarding the applications pods, I grabbed the URL of 2 apps, one being one the long running pods to make sure they were used. Both are still running and we do see some pods being terminated after one hour, but there are other that still continue, so we have proof that the scale to zero functionality is working as expected.As such, will deem the incident resolved and we will proceed with the investigation on what happened

[image.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDEzOTA2LCJwdXIiOiJibG9iX2lkIn19--1e2d3a10e16614f662661eac9af4cd18be086b45/image.png)

[image.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDEzOTA3LCJwdXIiOiJibG9iX2lkIn19--728918bb291912f3fb2ef532bfd7b1cac07c4512/image.png)

July 19  1:58 PM WEST

web

Henrique Santos

Incident has been resolved

July 19  1:58 PM WEST

web

Henrique Santos

System-wide impact has been set: Yes

July 19  1:58 PM WEST

web

Henrique Santos

Impact has been set: Applications deployed in &quot;rundev-ea-eu-ce-1-01&quot; would not be scaled from zero since around 05:38 UTC. This timestamp was defined based on the lack of logs from &quot;keda-istio-external-scaler&quot; from this point onwards.
This means that there was no further logic being applied, so:
- Applications that were scaled to zero would not be scaled if there was a request to them after this timestamp;
- Applications that were already scaled (i.e. had requests to them before) possibly were still working until one hour after the last use before this timestamp, as we presume that Keda would apply the cooldown period of 1 hour and delete the application pod.

July 19  1:58 PM WEST

web

Henrique Santos

Investigation and troubleshooting findings has been set: The &quot;keda-istio-external-scaler&quot; pod that was running during this time was created at 03:21 UTC and, according to the logs, was working normally until 05:38 UTC, where it stopped showing any logs regarding service activity. Only logs for containerized tests were still on-going and the pod resources were not near the limits.
We did not find any errors on the podThe Keda-operator was showing getting metrics error from the &quot;keda-istio-external-scaler&quot; endpoint, where it would get a timeout. According to the logs, this specific error started at 05:39:20 UTC.In sum, it seems that the &quot;keda-istio-external-scaler&quot; was unreachable by keda-operator and keda-istio-scaler stopped processing metrics, possibly because Istio was not able to reach it as well (this is pending confirmation)No further relevant evidence was found until now. We will continue investigating.

July 19  1:58 PM WEST

web

Henrique Santos

Resolution has been set: SRE was requested to recreate the &quot;keda-istio-external-scaler&quot; pod in the &quot;rundev-ea-eu-ce-1-01&quot; and the scale to zero functionality started working immediately after the new pod was created, as new applications pods were being created, there were log messages on keda-istio-external-scaler and the keda-operator was no longer had logs showing issues retrieving metrics from keda-istio-external-scalerThis is the first time that the team knows about an issue like this and this has been deployed and in use for several months without any recent modifications. We will investigate this further.

July 19  1:58 PM WEST

web

Henrique Santos

Ring has been set: ea

July 19  1:58 PM WEST

web

Henrique Santos

Ring has been unset: -

July 19  1:58 PM WEST

web

Rootly

Pagerduty Integrations marked the incident as resolved through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q0PAWCZN3AX1C6). (via Api)