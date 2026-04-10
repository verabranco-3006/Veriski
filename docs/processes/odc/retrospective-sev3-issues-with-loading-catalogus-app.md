---
title: Retrospective-SEV3-Issues with loading 'Catalogus' app
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4371742884/Retrospective-SEV3-Issues+with+loading+Catalogus+app
confluence_space: RKB
confluence_page_id: 4371742884
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV3-Issues with loading 'Catalogus' app

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV3

Teams:&nbsp;trueBlueMaestro
#### 🕐 Timestamps
Started At:&nbsp;trueBlueJuly 19  4:40 PM WEST

Mitigated At:&nbsp;trueYellowJuly 19  4:41 PM WEST

Resolved At:&nbsp;trueGreenAugust 20  1:40 PM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/695-issues-with-loading-catalogus-app)
[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3034538)

#### Summary
----------------------------------------------**ISSUE DESCRIPTION AND HOW TO REPRODUCE**- Pod failed to launch after scale-up (scale-to-zero in Development).![](https://supportoutsystems.zendesk.com/attachments/token/84KVjHCXpSwjkc9FqiLMhyEWP/?name=image.png)![](https://supportoutsystems.zendesk.com/attachments/token/vYThU5oyT7acuZu4OtEo9gGNj/?name=image.png)- Grafana link - scale-to-zero row.
- Then after around 1 hour (probably not a coincidence) it self-recovered:![](https://supportoutsystems.zendesk.com/attachments/token/eiK1ukL32UhoTC7SxiJqnZQai/?name=image.png)**IMPACT ON THE CUSTOMER**- Development;
- Already mitigated, self-recovered after 1 hour.**TROUBLESHOOTING STEPS &amp; WORKAROUND**- Tried to explore all logs from different services and filtering out some of the pollution, we can find the following logs:- Grafana link- Scale-up started:![](https://supportoutsystems.zendesk.com/attachments/token/6RV1TdQKCQUeqrz131GCxtQN5/?name=image.png)- Deprovisioning blocked and other errors:![](https://supportoutsystems.zendesk.com/attachments/token/M0izaLxHunGejtCaEPZEcPHoX/?name=image.png)- Scaled up again after 1 hour?![](https://supportoutsystems.zendesk.com/attachments/token/UF7SSaLn9XKLPsd8y5dHJbX4s/?name=image.png)- Questions:- What caused the pod to fail launching? Is there any information/logs we are missing here?- I think this self-recovery after 1 hour is not a coincidence - I remember discussing that there is something like a health check after 1 hour that can restart unhealthy pods, but I can't find sources for this.- If this is intended, shouldn't this health check happen more often?**TECH DATA OR ANY OTHER RELEVANT INFO**
Ring: ga
Tenant Id: f2db186f-4c0f-4987-8b56-673392241338
Tenant Prefix: kbk
Region: eu-central-1_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 RetrospectiveinfoDetails
**Ring:** ga
**System-wide impact:**&nbsp; No
**Tenant ID:** f2db186f-4c0f-4987-8b56-673392241338
**Tenant Prefix:** kbk
**Routing Error Code:** N/A
**Product Area:** Phoenix::Application Runtime::Networking
### Impact:
This issue occurred because the last 1CP of the client was an error, resulting in a deployment of an application in the cluster with errors (not healthy).
### Investigation and troubleshooting findings:
We, given this failure, don't terminate the previous pod, associated with the last healthy deployment, but this doesn't guarantee the pod will be there forever, pods are ephemeral and various causes can result in their termination.

In this case it was a keda scale down to 0 replicas. When the client tried to use his application again on the dev environment keda scaled up a pod, but it was of the current deployment (a failed application deployment), which resulted on the pod not being able to start properly. 
### Resolution:
The client did an operation on the application approximately an hour after, in this case an apply configurations, but a 1CP would work as well, that returned the app to a healthy state. This gave the illusion it was a failure with keda, but in reality the application was simply not in a healthy state until the client re-published the app,
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/695-issues-with-loading-catalogus-app)

**Date**

**Source**

**User**

**Event**
July 10 12:56 PM WESTwebRootly
created an alert via
July 10 12:56 PM WESTwebRootly
Rootly created this incident
July 10 12:56 PM WESTwebRootly
In triage date has been set to July 10 12:56 PM WEST
July 11 11:48 AM WESTwebHenrique Santos
Teams has been added: Global Routing
July 19  4:40 PM WESTwebHenrique Santos
Incident has been started
July 19  4:41 PM WESTwebHenrique Santos
Incident has been mitigated
July 19  5:11 PM WESTwebHenrique Santos
First of all, we apologize for the late investigation. The team has been handling other issues and this was kept in backlog, specially taking into account that, when it was escalated, it was already solved/mitigated and there has been no updates since then.---As shown by the escalation description, [the Keda scaler panel](https://outsystems.grafana.net/goto/2bQm-NuSR?orgId=1) seems to indicate that the application was scaled at 09:14:32 UTC.Furthermore, when checking [istio-keda-external-scaler logs](https://outsystems.grafana.net/goto/Buvi-NuSR?orgId=1) for this application key (&quot;959ad838-4eaf-480e-901d-364317cf331a&quot;), we see the first &quot;service is active&quot; message at 09:14:32 and then several ones which are related to [requests that were done to the application](https://outsystems.grafana.net/goto/ytzVaNXIR?orgId=1).When looking at [Kubernetes events](https://outsystems.grafana.net/goto/mD8IaHXSg?orgId=1), [container metrics](https://outsystems.grafana.net/goto/8F9NaHuSg?orgId=1) and [pod logs](https://outsystems.grafana.net/goto/-ZcbaHuIg?orgId=1), it seems that both init containers, istio-validation and agent, were started successfully.
Unfortunately, couldn't find any logs or metrics that indicate if a specific init container is finished, but since the main containers (app and istio-proxy) did not start, then we can assume that one of the init containers did not finish.On the istio-validation one, according to the pattern (that can be observed when the situation was resolved - [logs](https://outsystems.grafana.net/goto/AzMy-NuIg?orgId=1)), it outputted the normal logs and seemed to have finished.On the agent one, although it is not my expertise, it seems that the container itself did not output stdout but when searching for the [logs for the app key](https://outsystems.grafana.net/goto/-ZcbaHuIg?orgId=1), there are some logs that  stop at &quot;Waiting for update file.&quot;. When comparing with the [successful pod later](https://outsystems.grafana.net/goto/ehZVfNXIg?orgId=1), the same message does not appear.So it seems to be that that agent init container did not finish, therefore the app container and istio-proxy did not start. Regarding the fact that it was mitigated one hour later, I have no clue, although, looking at the pod metrics and the pod name, it seems that it was a new deployment (959ad838-4eaf-480e-901d-364317cf331a-8cf4bb774-vggn8 to 959ad838-4eaf-480e-901d-364317cf331a-84c7dccdb5-lpznm) ---Since there is no further action item for the GRS team to investigation, will try to understand what team should follow up with this, I'm in doubt between Backend Runtime and Maestro (since they are owners of outsystems-applicationagent-job)
July 22  2:35 PM WESTwebHenrique SantosSend ZenDesk private comment has been set: Hey there team,  
First of all, we apologize for the long response time.  Regarding the incident, we did an initial analysis and we were able to confirm that the scale to zero functionality was working as expected, as the application pod got created when the initial requests were done.  
However, we have reason to believe that one of the init containers, application agent job, did not finish and that is possibly the reason why the pod was never ready and the application was never available.  
We can only confirm so far that there were no issues detected on the assets owned by Global Routing.  As such, the incident has been moved over to Maestro, who are already investigating this incident in order to provide a definite answer to the raised questions.July 22  2:35 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hey there team,  
First of all, we apologize for the long response time.  Regarding the incident, we did an initial analysis and we were able to confirm that the scale to zero functionality was working as expected, as the application pod got created when the initial requests were done.  
However, we have reason to believe that one of the init containers, application agent job, did not finish and that is possibly the reason why the pod was never ready and the application was never available.  
We can only confirm so far that there were no issues detected on the assets owned by Global Routing.  As such, the incident has been moved over to Maestro, who are already investigating this incident in order to provide a definite answer to the raised questions.
July 22  2:35 PM WESTwebRootlySend ZenDesk private comment has been unsetJuly 22  2:35 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

July 22  2:35 PM WESTwebHenrique Santos
Teams has been added: Maestro
July 22  2:35 PM WESTwebHenrique Santos
Teams has been removed: Global Routing
July 24 12:47 PM WESTwebRootlyZendesk Private Comment has been set: ----------------------------------------------**Update to R&amp;D**
Hi Guilherme,Thanks for the thorough explanation!- While I understand what caused this, I am not grasping why a failed deployment would be used later on when the app is scaled up for whatever reason - what is the rationale behind that? Shouldn't a failed deployment simply be discarded?
- Also, just to confirm, could this affect other stages if a deployment between stages fails?Thanks in advance for your additional attention.Kind regards,
Jo&atilde;o Neves__July 24 12:47 PM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
Hi Guilherme,Thanks for the thorough explanation!- While I understand what caused this, I am not grasping why a failed deployment would be used later on when the app is scaled up for whatever reason - what is the rationale behind that? Shouldn't a failed deployment simply be discarded?
- Also, just to confirm, could this affect other stages if a deployment between stages fails?Thanks in advance for your additional attention.Kind regards,
Jo&atilde;o Neves__
July 25  9:58 AM WESTwebRootlyZenDesk Event Type has been set: solvedJuly 25  9:58 AM WESTwebRootly
The Global Support team marked this incident as closed in ZenDesk.
August 20  1:40 PM WESTwebSara Gon&ccedil;alves
Incident has been resolved
August 20  1:40 PM WESTwebSara Gon&ccedil;alvesSystem-wide impact has been set: NoAugust 20  1:40 PM WESTwebSara Gon&ccedil;alvesImpact has been set: This issue occurred because the last 1CP of the client was an error, resulting in a deployment of an application in the cluster with errors (not healthy).August 20  1:40 PM WESTwebSara Gon&ccedil;alvesInvestigation and troubleshooting findings has been set: We, given this failure, don't terminate the previous pod, associated with the last healthy deployment, but this doesn't guarantee the pod will be there forever, pods are ephemeral and various causes can result in their termination.
In this case it was a keda scale down to 0 replicas. When the client tried to use his application again on the dev environment keda scaled up a pod, but it was of the current deployment (a failed application deployment), which resulted on the pod not being able to start properly. August 20  1:40 PM WESTwebSara Gon&ccedil;alvesResolution has been set: The client did an operation on the application approximately an hour after, in this case an apply configurations, but a 1CP would work as well, that returned the app to a healthy state. This gave the illusion it was a failure with keda, but in reality the application was simply not in a healthy state until the client re-published the app,