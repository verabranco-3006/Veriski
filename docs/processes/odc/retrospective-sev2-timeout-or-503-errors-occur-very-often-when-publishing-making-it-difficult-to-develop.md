---
title: Retrospective-SEV2-Timeout or 503 errors occur very often when publishing, making it difficult to develop
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4290052223/Retrospective-SEV2-Timeout+or+503+errors+occur+very+often+when+publishing+making+it+difficult+to+develop
confluence_space: RKB
confluence_page_id: 4290052223
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV2-Timeout or 503 errors occur very often when publishing, making it difficult to develop

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV2

Teams:&nbsp;trueBlueNeo Platform Theseus&nbsp;trueBlueSre
#### 🕐 Timestamps
Started At:&nbsp;trueBlueJuly 10  9:46 AM WEST

Mitigated At:&nbsp;trueYellowJuly 17  9:58 AM WEST

Resolved At:&nbsp;trueGreenJuly 17  9:58 AM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/690-timeout-or-503-errors-occur-very-often-when-publishing-making-it-difficult-to-develop)
[Pagerduty incident](https://outsystems.pagerduty.com/incidents/Q3X3BRPSUFONYK)

[Slack channel](https://slack.com/app_redirect?channel=C07BNFCKEF4&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3029743)

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

Guilherme Rolo
#### Summary
----------------------------------------------**R&amp;D ESCALATION FORM**
Section comments can be removed for R&amp;D easier interpretation.**ISSUE DESCRIPTION AND HOW TO REPRODUCE**
Since July 1rst the customer has been experiencing intermittent timeouts and 503 Errors which are seriously impacting the customer development.
Errors:![](https://supportoutsystems.zendesk.com/attachments/token/pzjfzDZKRoD3r4fSzZit1SIrA/?name=image.png)![](https://supportoutsystems.zendesk.com/attachments/token/MEwt99yiWQAltMeKqrQqLPrqV/?name=image.png)At the same they've been getting other errors while developing such as sudden connection errors:![](https://supportoutsystems.zendesk.com/attachments/token/jIdWngGmEAoArTfj5ss4CAimj/?name=image.png)![](https://supportoutsystems.zendesk.com/attachments/token/25wbAuPrhae56JwRifcawd5ST/?name=image.png)![](https://supportoutsystems.zendesk.com/attachments/token/Ogg9y6xTdokCgGq0xTVVDeIi7/?name=image.png)Grafana: https://outsystems.grafana.net/d/A1YJOsa7z/1cp-logs?orgId=1&amp;var-ring=ga&amp;var-level=Error&amp;var-level=Warning&amp;to=now&amp;&amp;var-service=All&amp;var-traceId=e8564d9d-28b5-4a06-ba2f-d2e52a98a591&amp;from=1720362157428&amp;to=1720534957428https://outsystems.grafana.net/d/A1YJOsa7z/1cp-logs?orgId=1&amp;var-ring=ga&amp;var-level=Error&amp;var-level=Warning&amp;to=now&amp;&amp;var-service=All&amp;var-traceId=fc33dd6ac035c1b618c341fd333e14d6&amp;from=1720362157428&amp;to=1720534957428This seems related to the RDINC https://outsystemsrd.atlassian.net/browse/RDINC-26177We're opening a new JIRA because it was told to us that it was required being a different region and also that the issues might be different.**IMPACT ON THE CUSTOMER**
Customer development is being severely impacted due to this intermittent errors. Timeout errors have occurred continuously, and sometimes it takes more than an hour to publish.
They've escalated the ticket mentioning that this is already delaying their delivers date which was July 1rst.**TROUBLESHOOTING STEPS &amp; WORKAROUND**
No workaround available, customer needs to wait till the system is able to publish again.**TECH DATA OR ANY OTHER RELEVANT INFO**
Ring: ga
Tenant Id: 19b14cc8-6493-4286-83e2-a9b5fd8a07e0
Tenant Prefix: unikorea
Region: ap-northeast-1
CD4.81G.DLQ.AR8.1D1.U48.2QB.RN9_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 RetrospectiveinfoDetails
**Ring:** ga
**System-wide impact:**&nbsp; No
**Tenant ID:** 19b14cc8-6493-4286-83e2-a9b5fd8a07e0
**Tenant Prefix:** unikorea
**Routing Error Code:** N/A
**Product Area:** Phoenix::Service Studio::Publish
### Impact:
The tenant could not publish their application consistently
### Investigation and troubleshooting findings:### Resolution:
We manually changed AVS resources in GA since we were already aware of the issues but the fix wasn't quick enough to reach the ring
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/690-timeout-or-503-errors-occur-very-often-when-publishing-making-it-difficult-to-develop)

**Date**

**Source**

**User**

**Event**
July 9  4:10 PM WESTwebRootly
created an alert via
July 9  4:10 PM WESTwebRootly
Rootly created this incident
July 9  4:10 PM WESTwebRootly
In triage date has been set to July 9  4:10 PM WEST
July 9  4:10 PM WESTwebRootly[Slack Channel](https://slack.com/app_redirect?channel=C07BNFCKEF4&amp;team=T041063TZ) has been createdJuly 9  4:10 PM WESTwebRootly
Ring: ga
System-wide impact:  
Tenant ID: 19b14cc8-6493-4286-83e2-a9b5fd8a07e0
Tenant Prefix: unikorea
Routing Error Code: N/A
Product Area: Phoenix::Service Studio::Publish
July 9  4:10 PM WESTwebRootly[PagerDuty Incident](https://outsystems.pagerduty.com/incidents/Q3X3BRPSUFONYK) has been created.
📧 Notified Jo&atilde;o Mano by email.&nbsp;&nbsp;📲 Notified Jo&atilde;o Mano by push notification.  (via iPhone)&nbsp;&nbsp;📲 Notified Jo&atilde;o Mano by push notification.  (via iPhone)July 9  4:10 PM WESTwebRootlyJo&atilde;o Mano has been assigned as EngineerJuly 9  4:12 PM WESTwebRootly
Jo&atilde;o Mano acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q3X3BRPSUFONYK). (via Mobile)
July 9  4:20 PM WESTwebRootly
This incident was instantiated in Jira: RDINC-26754. Please work the incident using Rootly
July 9  4:33 PM WESTwebJo&atilde;o ManoSend ZenDesk private comment has been set: Hello support team,
&nbsp;&nbsp;
As the issue mentions, this seems a communications timeout issue with the APIs, so it's unlikely that it's an issue with the IDE.
&nbsp;&nbsp;
It also mentions a previous incident that was handled by the Theseus team. I've already aligned with Theseus on call agent and I'll be moving the issue to them.July 9  4:33 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

Hello support team,
&nbsp;&nbsp;
As the issue mentions, this seems a communications timeout issue with the APIs, so it's unlikely that it's an issue with the IDE.
&nbsp;&nbsp;
It also mentions a previous incident that was handled by the Theseus team. I've already aligned with Theseus on call agent and I'll be moving the issue to them.July 9  4:33 PM WESTwebRootlySend ZenDesk private comment has been unsetJuly 9  4:33 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

July 9  4:34 PM WESTwebGuilherme RoloGuilherme Rolo has been assigned as EngineerJuly 9  4:34 PM WESTwebJo&atilde;o Mano
Teams has been added: Neo Platform Theseus
July 9  4:34 PM WESTwebJo&atilde;o Mano
Teams has been removed: IDE Group
July 9  4:37 PM WESTwebRootly
Delegated to EP for Neo Platform Theseus by Jo&atilde;o Mano through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q3X3BRPSUFONYK)
July 9  4:41 PM WESTwebRootly
Guilherme Alexandre Rolo acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q3X3BRPSUFONYK). (via Mobile)
July 9  4:41 PM WESTwebRootly
Guilherme Alexandre Rolo acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q3X3BRPSUFONYK). (via Mobile)
July 9  5:05 PM WESTslackRodrigo Silva (rsl)
this one [https://outsystemsrd.atlassian.net/browse/RFC-1136](https://outsystemsrd.atlassian.net/browse/RFC-1136)
July 9  5:10 PM WESTwebRootly
This incident was instantiated in Jira: RDINC-26754. Please work the incident using Rootly
July 9  5:16 PM WESTslackGuilherme Rolo
I created a RFC so we can manually do the changes in the ring instead of having to wait until thursday:[https://outsystemsrd.atlassian.net/browse/RFC-1176](https://outsystemsrd.atlassian.net/browse/RFC-1176)
July 10  9:46 AM WESTwebGuilherme Rolo
Incident has been started
July 10  9:46 AM WESTwebRootly
Pagerduty Integrations acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q3X3BRPSUFONYK). (via Mobile)
July 10 12:07 PM WESTwebGuilherme RoloSwarm has been set: SREJuly 10 12:07 PM WESTwebRootly
Pagerduty Integrations added Filipe Seixeira as responder in [PagerDuty](https://outsystems.pagerduty.com/incidents/Q3X3BRPSUFONYK)
July 10 12:16 PM WESTwebRootly
Filipe Seixeira joined this [PagerDuty](https://outsystems.pagerduty.com/incidents/Q3X3BRPSUFONYK) incident.
July 10  1:00 PM WESTwebGuilherme RoloSend ZenDesk private comment has been set: A change has been manually applied in the tenant's region which should fix this problem.July 10  1:00 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
A change has been manually applied in the tenant's region which should fix this problem.
July 10  1:00 PM WESTwebRootlySend ZenDesk private comment has been unsetJuly 10  1:00 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

July 16  4:25 PM WESTwebRootlyZenDesk Event Type has been set: solvedJuly 16  4:25 PM WESTwebRootly
The Global Support team marked this incident as closed in ZenDesk.
July 17  9:58 AM WESTwebGuilherme Rolo
Incident has been resolved
July 17  9:58 AM WESTwebGuilherme RoloSystem-wide impact has been set: NoJuly 17  9:58 AM WESTwebGuilherme RoloImpact has been set: The tenant could not publish their application consistentlyJuly 17  9:58 AM WESTwebGuilherme RoloResolution has been set: We manually changed AVS resources in GA since we were already aware of the issues but the fix wasn't quick enough to reach the ring