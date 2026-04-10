---
title: Retrospective-SEV2-I'm not able to publish
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4302667902/Retrospective-SEV2-I+m+not+able+to+publish
confluence_space: RKB
confluence_page_id: 4302667902
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV2-I'm not able to publish

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV2

Teams:&nbsp;trueBlueExtended Runtime
#### 🕐 Timestamps
Started At:&nbsp;trueBlueJuly 22  4:23 PM WEST

Mitigated At:&nbsp;trueYellowJuly 22  4:24 PM WEST

Resolved At:&nbsp;trueGreenJuly 22  4:24 PM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/742-i-m-not-able-to-publish)
[Pagerduty incident](https://outsystems.pagerduty.com/incidents/Q14SCZZWI8YNHD)

[Slack channel](https://slack.com/app_redirect?channel=C07DK43PBAQ&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3039610)

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

Rafael Seara
#### Summary
----------------------------------------------**R&amp;D ESCALATION FORM**
Section comments can be removed for R&amp;D easier interpretation.**ISSUE DESCRIPTION AND HOW TO REPRODUCE**- Colleagues from OS are unable to continue with their work on the AI4Digital app as they are unable to publish it even without performing any change.
- https://app.slack.com/client/T041063TZ/C04HL3UGKT8 Internal Digital discussion, team is blocked.Failed to generate lambda package: UnhandledApplicationError { ErrorType = Internal Server Error, SelfServiceErrorCode = OS-ELGW-50001, Message = An error occurred. We'll look into it soon. Please try again, and if the problem persists, open a support case., StatusCode = InternalServerError }&nbsp;Error obtained on ODC Studio:![](https://supportoutsystems.zendesk.com/attachments/token/qR0H4BlUH3G3KYWc9QRfqh7Sk/?name=image.png)- Grafana: https://outsystems.grafana.net/d/o2_h2-Bnz/publish-service-1cp-by-tenant?orgId=1&amp;var-ring=osall&amp;var-tenant=All&amp;var-region=us-east-1&amp;var-stamp=plat-osall-us-east-1-01&amp;var-exclude_tenant=All&amp;var-interval=$__auto_interval_interval
- Process Key: https://outsystems.grafana.net/d/A1YJOsa7z/1cp-logs?orgId=1&amp;var-ring=osall&amp;var-level=Error&amp;var-level=Warning&amp;to=now&amp;&amp;var-service=All&amp;var-traceId=4e3e2f67e675e17c40de4ed44b3df177&amp;from=1721473153556&amp;to=1721645953556
- Trace ID: https://outsystems.grafana.net/d/A1YJOsa7z/1cp-logs?orgId=1&amp;var-ring=osall&amp;var-level=Error&amp;var-level=Warning&amp;to=now&amp;&amp;var-service=All&amp;var-traceId=22969b14-daf6-4906-bedd-1068cb8002d4&amp;from=1721473153556&amp;to=1721645953556- https://outsystems.grafana.net/explore?schemaVersion=1&amp;panes=%7B%22p1u%22:%7B%22datasour[&hellip;]55030000%22,%22to%22:%221721655041000%22%7D%7D%7D&amp;orgId=1
- There seems to be connections errors of Lambda
- https://outsystems.grafana.net/d/lj_Cstg4k/gen-search-trace?orgId=1&amp;var-traceid=09ffc7562a2a2c2bb66f2ddc7eb09a31![](https://supportoutsystems.zendesk.com/attachments/token/xj6kbOBhzepDBwhoQZjzDpRdk/?name=image.png)**IMPACT ON THE CUSTOMER**
Our teams are completely blocked from working on this apps and publish them.
We already performed a detailed impact analysis and from our side, this is a Sev2**TROUBLESHOOTING STEPS &amp; WORKAROUND**
Initially we believe the apps were failing due to external logic and libraries blocking the main app, can we suggest just for test if they can release a new version and then try to publish the main app, but the issue persists.**TECH DATA OR ANY OTHER RELEVANT INFO**
Ring: osall
Tenant Id: fae0814c-7560-49cc-886f-6b4eccb6709f
Tenant Prefix: extranet
Region: us-east-1
DMN.GTF.J1V.N02.OHY.ZDO.UBL.WTS_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 RetrospectiveinfoDetails
**Ring:** osall
**System-wide impact:**&nbsp; 
**Tenant ID:** fae0814c-7560-49cc-886f-6b4eccb6709f
**Tenant Prefix:** extranet
**Routing Error Code:** OS-ELGW
**Product Area:** -
### Impact:
The outsystems-externallibrary-worker-service was rolledback.
[https://outsystemsrd.atlassian.net/browse/RFC-1230](https://outsystemsrd.atlassian.net/browse/RFC-1230)[https://outsystems.slack.com/archives/C02FDRXNER0/p1721654857728809](https://outsystems.slack.com/archives/C02FDRXNER0/p1721654857728809)

The issue is now solved.
### Investigation and troubleshooting findings:### Resolution:
The outsystems-externallibrary-worker-service was rolledback.
[https://outsystemsrd.atlassian.net/browse/RFC-1230](https://outsystemsrd.atlassian.net/browse/RFC-1230)[https://outsystems.slack.com/archives/C02FDRXNER0/p1721654857728809](https://outsystems.slack.com/archives/C02FDRXNER0/p1721654857728809)

The issue is now solved.
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/742-i-m-not-able-to-publish)

**Date**

**Source**

**User**

**Event**
July 22  3:04 PM WESTwebRootly
created an alert via
July 22  3:04 PM WESTwebRootly
Rootly created this incident
July 22  3:04 PM WESTwebRootly
In triage date has been set to July 22  3:04 PM WEST
July 22  3:04 PM WESTwebRootly[Slack Channel](https://slack.com/app_redirect?channel=C07DK43PBAQ&amp;team=T041063TZ) has been createdJuly 22  3:04 PM WESTwebRootly
Ring: osall
System-wide impact:  
Tenant ID: fae0814c-7560-49cc-886f-6b4eccb6709f
Tenant Prefix: extranet
Routing Error Code: OS-ELGW
Product Area: -
July 22  3:04 PM WESTwebRootly[PagerDuty Incident](https://outsystems.pagerduty.com/incidents/Q14SCZZWI8YNHD) has been created.
📧 Notified Helder Marques by email.&nbsp;&nbsp;📲 Notified Helder Marques by push notification.  (via Android)July 22  3:04 PM WESTwebRootlyH&eacute;lder Marques has been assigned as EngineerJuly 22  3:04 PM WESTwebH&eacute;lder MarquesRafael Seara has been assigned as EngineerJuly 22  3:08 PM WESTwebRootly
Rafael Seara has been assigned by Helder Marques through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q14SCZZWI8YNHD)
July 22  3:08 PM WESTwebRootly
Rafael Seara acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q14SCZZWI8YNHD). (via Mobile)
July 22  4:22 PM WESTwebRafael Seara
The outsystems-externallibrary-worker-service was rolledback.
https://outsystemsrd.atlassian.net/browse/RFC-1230
https://outsystems.slack.com/archives/C02FDRXNER0/p1721654857728809
The issue is now solved.
July 22  4:23 PM WESTwebRafael Seara
Incident has been started
July 22  4:23 PM WESTwebRootly
Pagerduty Integrations acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q14SCZZWI8YNHD). (via Mobile)
July 22  4:24 PM WESTwebRafael Seara
Incident has been resolved
July 22  4:24 PM WESTwebRafael SearaImpact has been set: The outsystems-externallibrary-worker-service was rolledback.
https://outsystemsrd.atlassian.net/browse/RFC-1230
https://outsystems.slack.com/archives/C02FDRXNER0/p1721654857728809
The issue is now solved.July 22  4:24 PM WESTwebRafael SearaResolution has been set: The outsystems-externallibrary-worker-service was rolledback.
https://outsystemsrd.atlassian.net/browse/RFC-1230
https://outsystems.slack.com/archives/C02FDRXNER0/p1721654857728809
The issue is now solved.