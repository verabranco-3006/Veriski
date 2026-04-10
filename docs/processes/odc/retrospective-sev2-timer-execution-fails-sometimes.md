---
title: Retrospective-SEV2-Timer execution fails sometimes
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4333633728/Retrospective-SEV2-Timer+execution+fails+sometimes
confluence_space: RKB
confluence_page_id: 4333633728
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV2-Timer execution fails sometimes

## 📘 Overview
Author:&nbsp;Rootlytrue

Severity:&nbsp;SEV2Redtrue

Teams:&nbsp;Backend RuntimeBluetrue
#### 🕐 Timestamps
Started At:&nbsp;July 10 11:46 AM WESTBluetrue

Mitigated At:&nbsp;August 5  1:22 PM WESTYellowtrue

Resolved At:&nbsp;August 5  1:22 PM WESTGreentrue
#### 🔗 Links
[Incident Page](https://rootly.com/account/incidents/681-timer-execution-fails-sometimes)

[Pagerduty incident](https://outsystems.pagerduty.com/incidents/Q1808319JB6F95)

[Slack channel](https://slack.com/app_redirect?channel=C07BANT5E2Y&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3032356)

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

Rui Garcia
#### Summary
----------------------------------------------**ISSUE DESCRIPTION AND HOW TO REPRODUCE**- The customer is reporting that in their production environment, their timer **Timer_CheckCutoffTimes** has been failing several times with the error message: **an error occured while trying to run the Application container is not started after timeout.****IMPACT ON THE CUSTOMER**- This timer is meant to run every five minutes and is responsible for checking on the DB if there is a certain event that should be triggered and it is not supposed that it delays more than 5 minutes, which is the scheduled interval for the time to run
- There is no specific pattern regarding the times this timer fails, it can happen 2 times in less than one hour, and also 1 occurrence after 5 five hours of the previous one**TROUBLESHOOTING STEPS &amp; WORKAROUND**-  We can see a noticeable pattern each time the timer fails with that message- https://outsystems.grafana.net/d/cdeqzn1jj77cwe/general-troubleshooting?orgId=1&amp;var-ring=ga&amp;var-tenant=e6311047-7f8a-4d1b-aab5-2ded0cd72892&amp;var-application=53cb525d-8a57-454c-8ae0-35153cb35c58&amp;var-cluster=runp&amp;var-cluster_old=All&amp;var-severity=All&amp;var-runtime=All&amp;var-filter=&amp;var-exclude=&amp;var-region=eu-central-1&amp;var-traceDuration=All&amp;var-environment=All&amp;var-regionShort=ga-eu-ce-1-01&amp;var-tenant_prefix=bertus&amp;var-module_name=BTrackData&amp;from=1720173000000&amp;to=1720174019000- ![](https://supportoutsystems.zendesk.com/attachments/token/l9EMNapcs61uXBCSr5ToJYnIi/?name=image.png)
- In this example, the timer should have started at 4, and after several failed health checks saying that the DatabaseStartupProbeTask status is unhealthy, it eventually failed at 4:02 and stopped trying to execute- ![](https://supportoutsystems.zendesk.com/attachments/token/HQDzxLvDBQ3vdBGMqQwYdMX6r/?name=image.png)
- Same occurrence and pattern here- https://outsystems.grafana.net/d/cdeqzn1jj77cwe/general-troubleshooting?orgId=1&amp;var-ring=ga&amp;var-tenant=e6311047-7f8a-4d1b-aab5-2ded0cd72892&amp;var-application=53cb525d-8a57-454c-8ae0-35153cb35c58&amp;var-cluster=runp&amp;var-cluster_old=All&amp;var-severity=All&amp;var-runtime=All&amp;var-filter=&amp;var-exclude=&amp;var-region=eu-central-1&amp;var-traceDuration=All&amp;var-environment=All&amp;var-regionShort=ga-eu-ce-1-01&amp;var-tenant_prefix=bertus&amp;var-module_name=BTrackData&amp;from=1720171500000&amp;to=1720172759000- ![](https://supportoutsystems.zendesk.com/attachments/token/Kr2or6ElnPR4Xvs4OuYjDNLHF/?name=image.png)- ![](https://supportoutsystems.zendesk.com/attachments/token/bzT00By9GDcBJoVANuV5rhLNA/?name=image.png)
- We can see that both can start with a different error, rather a NATS connection (with error message Resource temporarily unavailable) or an error with the database connection (with the error message The operation has timed out.)- ![](https://supportoutsystems.zendesk.com/attachments/token/3WPM1baZFWh30KEgoFsRd3q5J/?name=image.png)- ![](https://supportoutsystems.zendesk.com/attachments/token/skYHH2AJNb04RNEEKY4Ba8Pxv/?name=image.png)* * *- Another occurrence with the same pattern,- https://outsystems.grafana.net/d/cdeqzn1jj77cwe/general-troubleshooting?orgId=1&amp;var-ring=ga&amp;var-tenant=e6311047-7f8a-4d1b-aab5-2ded0cd72892&amp;var-application=53cb525d-8a57-454c-8ae0-35153cb35c58&amp;var-cluster=runp&amp;var-cluster_old=All&amp;var-severity=All&amp;var-runtime=All&amp;var-filter=&amp;var-exclude=&amp;var-region=eu-central-1&amp;var-traceDuration=All&amp;var-environment=All&amp;var-regionShort=ga-eu-ce-1-01&amp;var-tenant_prefix=bertus&amp;var-module_name=BTrackData&amp;from=1720133700000&amp;to=1720134239000- ![](https://supportoutsystems.zendesk.com/attachments/token/zcvTxz8QMybx9IPQpilct4Kvh/?name=image.png)- ![](https://supportoutsystems.zendesk.com/attachments/token/1UxiE3rRmaFsNpbj62drUFt5Y/?name=image.png)* * *- About the first occurrence listed in this note, we can see that the timer that checked the status had an issue connection to NATS, but nothing else too relevant:- https://outsystems.grafana.net/d/Ok_fGn1nz/timer-jobs?orgId=1&amp;var-severity=All&amp;var-cluster=runp-ga-eu-ce-1-01&amp;var-timer=timer-c4b05ee2d0385d55267a4ed07e56823753704fe16c39d2&amp;from=1720173468247&amp;to=1720173836714&amp;panelState=%7B%22logs%22%3A%7B%22id%22%3A%22A_1718614279574488600_6b77332%22%7D%7D- ![](https://supportoutsystems.zendesk.com/attachments/token/Z31UyKNGqRIz3YAhJPGWdkIkb/?name=image.png)- A case related to these errors in the portal was related to scale to 0, but in this case, as far as is understood and also as seen in the keda scaler, scale to 0 is still deactivated in GA Prod stage- https://outsystemsrd.atlassian.net/browse/RDINC-12038- Why is the DatabaseStartupProbeTask unhealthy? And the SettingsStartupProbeTask degraded?**TECH DATA OR ANY OTHER RELEVANT INFO**
Ring: ga
Tenant Id: e6311047-7f8a-4d1b-aab5-2ded0cd72892
Tenant Prefix: bertus
Region: eu-central-1
AC: HBW.XZ2.Z1D.OSX.LSU.UTO.NZR.QTS_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 Retrospective### Details
**Ring:** ga
**System-wide impact:**&nbsp; No
**Tenant ID:** e6311047-7f8a-4d1b-aab5-2ded0cd72892
**Tenant Prefix:** bertus
**Routing Error Code:** N/A
**Product Area:** Phoenix::Application Runtime::Logic Flows
### Impact:
Timers aren't running on schedule (with precise accuracy).
### Investigation and troubleshooting findings:
Expected behavior. Due to the architecture nature, failures are expected, delays and retries ensure the logic eventually runs, but the schedule may not always be met (at a near second precision).
### Resolution:
Suggested customer logic to be made more resilient and specially idempotent so it can tolerate the execution environment characteristics. 
## Tasks performed during incident resolution:
&nbsp;
## Executive Summary
[Guidelines](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4144496679/Incident+Retrospectives+-+Playbook#STEP-3---Write-the-Executive-Summary)

On July 5th, 2024, Customer requested an explanation about errors during the execution of Timers. Investigation concluded that some occasions, errors caused Timer execution to be retried and therefore be delayed from a few seconds to a few minutes. No timer failed to execute, it just didn&rsquo;t run precisely on the schedule that was configured for.

Impact is relative. Timers still run, but our customer logic assumed the schedule would always be met therefore the business logic was not as resilience as it should, causing delays in the Business case from 1 day to 1 week.

From a technical perspective, the problem was caused by the network layer of Timer Pods not being available immediately. This delay caused the startup probe to fail, which led to further delays. Delays such as these are expected and the architecture of the solution tolerates and resists against them. That&rsquo;s the reason why the Timer logic is executed a seconds/minutes after it was scheduled.

As a consequence of the incident, we have determined to:

- 
Short term: improve the startup probe logic to be more resilience and recover quickly. This would enable an even faster recovery time and possibly prevent timeout errors. Backend Runtime backlog issue: [[RRCT-5900] Improve startup probe recovery time when there are fast failures on test connection. - JIRA (atlassian.net)](https://outsystemsrd.atlassian.net/browse/RRCT-5900)

## Root Causes 
[Guidelines](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4144496679/Incident+Retrospectives+-+Playbook#STEP-1---Perform-the-Root-Cause-Analysis)

- 
Some delays are expected due to the nature of the architecture. Timer execution is an async process, and there are multiple component involved that may add time to the process causing the Timer business logic to start later than scheduled.

- 
Cluster may not have enough resources (no nodes available);

- 
Pod may start but take too long to pull images (throttled);

- 
Apps may start but may take a while to be able to use the network;

- 
Startup probe is a *check-once* kind of process. When it fails, it keeps the result until the process is restarted. When the network is not ready (somewhat common in Jobs), this check will fail fast and won&rsquo;t attempt any retries, causing an apparently unnecessary 60 second delay. Timer Executor then times out and a new attempt is made on the executor side.

If the customer needs formal RCA, please fill out the following field with the document URL

[Please follow these instructions and place the RCA URL in the field below.](https://docs.google.com/document/d/13rXmBsOJh73nV2D6Z17SIBGBu2HOTWty5ddsvU000JM/edit#heading=h.bqxasxszr5q)

RCA URL

&lt;Place the URL of the customer RCA here if you have created one&gt;
## ⌛ Timeline
[View on Rootly](https://rootly.com/account/incidents/681-timer-execution-fails-sometimes)

**Date**

**Source**

**User**

**Event**

July 5  7:03 PM WEST

web

Rootly

created an alert via

July 5  7:03 PM WEST

web

Rootly

Rootly created this incident

July 5  7:03 PM WEST

web

Rootly

In triage date has been set to July 5  7:03 PM WEST

July 5  7:03 PM WEST

web

Rootly

[Slack Channel](https://slack.com/app_redirect?channel=C07BANT5E2Y&amp;team=T041063TZ) has been created

July 5  7:04 PM WEST

web

Rootly

[PagerDuty Incident](https://outsystems.pagerduty.com/incidents/Q1808319JB6F95) has been created.

📱 Notified Rui Garcia by SMS.

&nbsp;&nbsp;

📧 Notified Rui Garcia by email.

&nbsp;&nbsp;

📧 Notified Rui Garcia by email.

July 5  7:04 PM WEST

web

Rootly

Ring: ga
System-wide impact:  
Tenant ID: e6311047-7f8a-4d1b-aab5-2ded0cd72892
Tenant Prefix: bertus
Routing Error Code: N/A
Product Area: Phoenix::Application Runtime::Logic Flows

July 5  7:04 PM WEST

web

Rootly

Rui Garcia has been assigned as Engineer

July 5  7:05 PM WEST

web

Rootly

Rui Garcia acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q1808319JB6F95). (via Phone)

July 5  7:14 PM WEST

web

Rootly

This incident was instantiated in Jira: RDINC-26556. Please work the incident using Rootly

July 5  8:04 PM WEST

web

Rootly

This incident was instantiated in Jira: RDINC-26556. Please work the incident using Rootly

July 10 11:46 AM WEST

web

Rui Garcia

Incident has been started

July 10 11:46 AM WEST

web

Rootly

Pagerduty Integrations acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q1808319JB6F95). (via Phone)

July 11  5:43 AM WEST

web

Rootly

Zendesk Private Comment has been set: ----------------------------------------------**Update to R&amp;D**Hello team,Thank you for your detailed response.However, customer still have a concern regarding the feedback shared:&gt; This timer runs every 5 minutes to check if there are any operations scheduled for the next 5 minutes. So when it runs at, say, 13:00, it checks if there's anything scheduled between 13:01 and 13:05. In this example, if the timer execution is delayed due to the reasons explained above until after 13:05, it will fail to successfully process the tasks that were scheduled between 13:01 and 13:05. Due to the business rules involved, this might mean that those tasks will only be processed anywhere between 1 day and 1 week later.Kindly assist in validating the concern above.Thank you as always.__

July 11  5:43 AM WEST

web

Rootly

NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**Hello team,Thank you for your detailed response.However, customer still have a concern regarding the feedback shared:&gt; This timer runs every 5 minutes to check if there are any operations scheduled for the next 5 minutes. So when it runs at, say, 13:00, it checks if there's anything scheduled between 13:01 and 13:05. In this example, if the timer execution is delayed due to the reasons explained above until after 13:05, it will fail to successfully process the tasks that were scheduled between 13:01 and 13:05. Due to the business rules involved, this might mean that those tasks will only be processed anywhere between 1 day and 1 week later.Kindly assist in validating the concern above.Thank you as always.__

July 11  5:43 AM WEST

web

Rootly

Zendesk Private Comment has been changed to: ------------------------------------------------ This notification was sent from Zendesk Support ticket #3032356 to all linked JIRA issues by Sugan Krishnan. --**Update to R&amp;D**Hello team,Thank you for your detailed response.However, customer still have a concern regarding the feedback shared:&gt; This timer runs every 5 minutes to check if there are any operations scheduled for the next 5 minutes. So when it runs at, say, 13:00, it checks if there's anything scheduled between 13:01 and 13:05. In this example, if the timer execution is delayed due to the reasons explained above until after 13:05, it will fail to successfully process the tasks that were scheduled between 13:01 and 13:05. Due to the business rules involved, this might mean that those tasks will only be processed anywhere between 1 day and 1 week later.Kindly assist in validating the concern above.Thank you as always._&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_

July 11  5:43 AM WEST

web

Rootly

NEW MESSAGE FROM GLOBAL SUPPORT:
------------------------------------------------ This notification was sent from Zendesk Support ticket #3032356 to all linked JIRA issues by Sugan Krishnan. --**Update to R&amp;D**Hello team,Thank you for your detailed response.However, customer still have a concern regarding the feedback shared:&gt; This timer runs every 5 minutes to check if there are any operations scheduled for the next 5 minutes. So when it runs at, say, 13:00, it checks if there's anything scheduled between 13:01 and 13:05. In this example, if the timer execution is delayed due to the reasons explained above until after 13:05, it will fail to successfully process the tasks that were scheduled between 13:01 and 13:05. Due to the business rules involved, this might mean that those tasks will only be processed anywhere between 1 day and 1 week later.Kindly assist in validating the concern above.Thank you as always.__

July 12  6:32 PM WEST

web

Rootly

Rui Garcia marked the incident as resolved through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q1808319JB6F95). (via Website)

July 22  7:03 PM WEST

web

Rootly

ZenDesk Event Type has been set: solved

July 22  7:03 PM WEST

web

Rootly

The Global Support team marked this incident as closed in ZenDesk.

August 5  1:22 PM WEST

web

Rui Garcia

Incident has been resolved

August 5  1:22 PM WEST

web

Rui Garcia

System-wide impact has been set: No

August 5  1:22 PM WEST

web

Rui Garcia

Impact has been set: Timers aren't running on schedule (with precise accuracy).

August 5  1:22 PM WEST

web

Rui Garcia

Investigation and troubleshooting findings has been set: Expected behavior. Due to the architecture nature, failures are expected, delays and retries ensure the logic eventually runs, but the schedule may not always be met (at a near second precision).

August 5  1:22 PM WEST

web

Rui Garcia

Resolution has been set: Suggested customer logic to be made more resilient and specially idempotent so it can tolerate the execution environment characteristics.