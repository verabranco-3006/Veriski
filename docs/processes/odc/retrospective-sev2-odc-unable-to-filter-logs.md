---
title: Retrospective-SEV2-ODC - Unable to filter logs
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4307518284/Retrospective-SEV2-ODC+-+Unable+to+filter+logs
confluence_space: RKB
confluence_page_id: 4307518284
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV2-ODC - Unable to filter logs

## 📘 Overview
Author:&nbsp;Rootlytrue

Severity:&nbsp;SEV2Redtrue

Teams:&nbsp;AI Insight consoleBlue
#### 🕐 Timestamps
Started At:&nbsp;July 24  8:15 PM WESTBluetrue

Mitigated At:&nbsp;July 24  8:48 PM WESTYellowtrue

Resolved At:&nbsp;July 24  8:48 PM WESTGreentrue
#### 🔗 Links
[Incident Page](https://rootly.com/account/incidents/756-odc-unable-to-filter-logs)

[Pagerduty incident](https://outsystems.pagerduty.com/incidents/Q2NGALIYB50IKR)

[Slack channel](https://slack.com/app_redirect?channel=C07EL2J03HN&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3040744)

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

Cl&aacute;udia Rezende
#### Summary
----------------------------------------------**ISSUE DESCRIPTION AND HOW TO REPRODUCE**
- Repeated errors affect the date filter in the ODC Portal Logs.
- Each time the customer opens the filter or clicks the &quot;Apply&quot; button, they receive multiple OS-MONC-GEN-60001 errors, making the feature unusable.
- Currently, the customer can only view logs for the date saved in the cache, making it impossible to see logs from different dates.
- For example, when attempting to filter by a specific time range or preset periods (e.g., last 7 days, 14 days), the system only displays logs from the last time the customer accessed them, preventing the review of logs![](https://supportoutsystems.zendesk.com/attachments/token/GG28ozlowIGvgjeN7NNayMfND/?name=image.png)**IMPACT ON THE CUSTOMER**
Brief description of the impact on the customer/development team/other, including:
- Development, QA, Production
- Ongoing.
- Significantly impacts development, as customers are unable to effectively review logs and troubleshoot issues based on error logs from presets or specific dates.
- This problem makes the ODC Portal logs feature nearly unusable, as customers cannot access logs from different dates, appearing like the system is stuck.**TROUBLESHOOTING STEPS &amp; WORKAROUND**- Managed to replicate the problem highlighted by the customer on ticket #3040658
- Examined the customer's screenshot showing logs from Jul 24, 2024, 12:40 PM to 2:27 PM. (Customer is in the Lisbon UTC +1 timezone).![](https://supportoutsystems.zendesk.com/attachments/token/ilf54aMkq9cYaJ05oCMUseATt/?name=1721835553000000000__Captura+de+ecr%C3%A3+2024-07-24+142739.png)- We reproduce the issue on the application SalesAI application.
- Reproduced the issue filtering the logs of the app mentioned by the customer SalesAI.![](https://supportoutsystems.zendesk.com/attachments/token/CFbNHO1tvLpQu9HfU1ZO8wJp1/?name=Captura+de+pantalla+2024-07-24+101844.png)- Grafana logs on the Portal 02 tenant show the error at the same time we replicated it seven times (10:18 UTC -6 / 16:18 UTC).https://outsystems.grafana.net/d/cdeqzn1jj77cwe/general-troubleshooting?orgId=1&amp;var-ring=ga&amp;var-tenant=cf242ec4-02ac-4a33-b54c-cb5005cad42c&amp;var-application=70082eed-6d98-437e-b4f0-9af69ce6b83e&amp;var-application=1f22e6b8-36c6-4a35-83c9-01b4fa6732ce&amp;var-cluster=All&amp;var-cluster_old=All&amp;var-severity=Warning&amp;var-severity=Error&amp;var-runtime=All&amp;var-filter=&amp;var-exclude=&amp;var-region=us-east-1&amp;var-traceDuration=All&amp;var-environment=All&amp;var-regionShort=ga-us-east-1-01&amp;var-tenant_prefix=odc-portal-live-02&amp;var-module_name=&amp;from=1721828310713&amp;to=1721839110714![](https://supportoutsystems.zendesk.com/attachments/token/YsMiEhBwxvPogxkr0EstQ8d3e/?name=Captura+de+pantalla+2024-07-24+102114.png)attributes_exception_messageCannot read properties of null (reading 'addEventListener')attributes_exception_stacktracemonitoring.GeneralException: Cannot read properties of null (reading 'addEventListener')at https://extranet.outsystems.dev/monitoring/scripts/monitoring.logs.controller__Glp4RyKpcpXEXbA1ktVzg.js?Glp4RyK+pcpXEXbA1ktVzg:59:7at s (https://extranet.outsystems.dev/monitoring/scripts/outsystems-logger__DA6QJ7ofCz43gspUnGPyPg.js?DA6QJ7ofCz43gspUnGPyPg:7:81817)at i.invoke (https://extranet.outsystems.dev/monitoring/scripts/outsystems-logger__DA6QJ7ofCz43gspUnGPyPg.js?DA6QJ7ofCz43gspUnGPyPg:7:26029)at r.run (https://extranet.outsystems.dev/monitoring/scripts/outsystems-logger__DA6QJ7ofCz43gspUnGPyPg.js?DA6QJ7ofCz43gspUnGPyPg:7:21220)at t.with (https://extranet.outsystems.dev/monitoring/scripts/outsystems-logger__DA6QJ7ofCz43gspUnGPyPg.js?DA6QJ7ofCz43gspUnGPyPg:1:97328)at t.with (https://extranet.outsystems.dev/monitoring/scripts/outsystems-logger__DA6QJ7ofCz43gspUnGPyPg.js?DA6QJ7ofCz43gspUnGPyPg:1:12179)at t.startActiveSpan (https://extranet.outsystems.dev/monitoring/scripts/outsystems-logger__DA6QJ7ofCz43gspUnGPyPg.js?DA6QJ7ofCz43gspUnGPyPg:7:57009)at nd.startActiveSpan (https://extranet.outsystems.dev/monitoring/scripts/outsystems-logger__DA6QJ7ofCz43gspUnGPyPg.js?DA6QJ7ofCz43gspUnGPyPg:7:81919)at t.InstrumentationFactory.startActiveSpan (https://extranet.outsystems.dev/monitoring/scripts/outsystems-logger__DA6QJ7ofCz43gspUnGPyPg.js?DA6QJ7ofCz43gspUnGPyPg:7:99100)at Object.ui as startActiveSpan**TECH DATA OR ANY OTHER RELEVANT INFO**We have 2 customers reporting this issue at this moment.Ring: osall
Tenant Id: fae0814c-7560-49cc-886f-6b4eccb6709f
Tenant Prefix: extranet
Region: us-east-1
DMN.GTF.J1V.N02.OHY.ZDO.UBL.WTSRing: ga
Tenant Id: e6311047-7f8a-4d1b-aab5-2ded0cd72892
Tenant Prefix: bertus
Region: eu-central-1
HBW.XZ2.Z1D.OSX.LSU.UTO.NZR.QTSAlso, we were able to confirm that in our sandbox environment, this issue is also occurring.
https://gs-sandbox-ga-eu-01.outsystems.dev/apps/
R1Q.Q6R.8UC.FPN.PN3.QRS.UKV.QOU_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 Retrospective### Details
**Ring:** GA
**System-wide impact:**&nbsp; No
**Tenant ID:** N/A
**Tenant Prefix:** N/A
**Routing Error Code:** OS-MONC
**Product Area:** -
### Impact:
User cannot filter the app logs using the filters. Can only see logs using the default settings (last 12 hours)
### Investigation and troubleshooting findings:### Resolution:
There was a change related to NDS on the Monitoring console, and a new version of the console was pushed to the live tenant and ga ring.

To fix the issue, an old version of the NDS (Neo Design System library) was published that didn&rsquo;t have the problem of the more recent version.
## Tasks performed during incident resolution:
&nbsp;
## Executive Summary
[Guidelines](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4144496679/Incident+Retrospectives+-+Playbook#STEP-3---Write-the-Executive-Summary)

On July 26th at 8 PM, the customer submitted a Support ticket &quot;ODC - Unable to filter logs&quot; #756 reporting an issue on Logs that the users cannot select a period different from the one already chosen by default.

The users can see the logs and traces, but only for the selected period by default. 

The error appears when opening the date picker component to select the period we want to filter.
We got an error by simply opening and clicking outside the element.

The team responsible for the console (AI Insight Console team) had already identified the issue, fixed it, and opened an RFC to bypass the soak time. They warned us about this problem, and it had already been pushed to the live tenant.

To fix the issue, they had to publish an old version of the NDS (Neo Design System library) that didn&rsquo;t have the problem of the more recent version.

[Normal] Bypass Soak Period to release a fix in GA for Monitoring Console 
## Root Causes 
[Guidelines](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4144496679/Incident+Retrospectives+-+Playbook#STEP-1---Perform-the-Root-Cause-Analysis)

There was an issue with the data picker component in the latest version of NDS (the NDS team is already aware) that was updated in the Monitoring console.

If the customer needs formal RCA, please fill out the following field with the document URL

[Please follow these instructions and place the RCA URL in the field below.](https://docs.google.com/document/d/13rXmBsOJh73nV2D6Z17SIBGBu2HOTWty5ddsvU000JM/edit#heading=h.bqxasxszr5q)

RCA URL

N/A
## ⌛ Timeline
[View on Rootly](https://rootly.com/account/incidents/756-odc-unable-to-filter-logs)

**Date**

**Source**

**User**

**Event**

July 24  8:04 PM WEST

web

Rootly

created an alert via

July 24  8:04 PM WEST

web

Rootly

Rootly created this incident

July 24  8:04 PM WEST

web

Rootly

In triage date has been set to July 24  8:04 PM WEST

July 24  8:04 PM WEST

web

Rootly

[Slack Channel](https://slack.com/app_redirect?channel=C07EL2J03HN&amp;team=T041063TZ) has been created

July 24  8:05 PM WEST

web

Rootly

Ring: -
System-wide impact:  
Tenant ID: N/A
Tenant Prefix: N/A
Routing Error Code: OS-MONC
Product Area: -

July 24  8:05 PM WEST

web

Rootly

[PagerDuty Incident](https://outsystems.pagerduty.com/incidents/Q2NGALIYB50IKR) has been created.

📲 Notified Claudia Rezende by push notification.  (via Android)

July 24  8:05 PM WEST

web

Rootly

Cl&aacute;udia Rezende has been assigned as Engineer

July 24  8:08 PM WEST

web

Rootly

Claudia Rezende acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q2NGALIYB50IKR). (via Phone)

July 24  8:15 PM WEST

web

Cl&aacute;udia Rezende

Incident has been started

July 24  8:15 PM WEST

web

Rootly

Pagerduty Integrations acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q2NGALIYB50IKR). (via Phone)

July 24  8:47 PM WEST

web

Cl&aacute;udia Rezende

Send ZenDesk private comment has been set: This error is already identified and should be fixed in a few hours.

July 24  8:47 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:
This error is already identified and should be fixed in a few hours.

July 24  8:47 PM WEST

web

Rootly

Send ZenDesk private comment has been unset

July 24  8:47 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:

July 24  8:48 PM WEST

web

Cl&aacute;udia Rezende

Incident has been resolved

July 24  8:48 PM WEST

web

Cl&aacute;udia Rezende

System-wide impact has been set: No

July 24  8:48 PM WEST

web

Cl&aacute;udia Rezende

Impact has been set: user can not filter the app logs

July 24  8:48 PM WEST

web

Cl&aacute;udia Rezende

Resolution has been set: Bug was fixed.