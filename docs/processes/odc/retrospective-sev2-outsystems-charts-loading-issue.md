---
title: Retrospective-SEV2-Outsystems charts loading issue
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4370268388/Retrospective-SEV2-Outsystems+charts+loading+issue
confluence_space: RKB
confluence_page_id: 4370268388
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV2-Outsystems charts loading issue

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV2

Teams:&nbsp;trueBlueUi Components
#### 🕐 Timestamps
Started At:&nbsp;trueBlueAugust 9 12:52 AM WEST

Mitigated At:&nbsp;trueYellowAugust 9 12:36 PM WEST

Resolved At:&nbsp;trueGreenAugust 19  7:03 PM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/850-outsystems-charts-loading-issue)
[Pagerduty incident](https://outsystems.pagerduty.com/incidents/Q0IBWG5HK3UZD2)

[Slack channel](https://slack.com/app_redirect?channel=C07G3KNCD2R&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3045914)

#### 🧑&zwj;🚒 Incident Rolestrue
**Commander**

Gon&ccedil;alo Martins

**Engineer**

Giuliana Silva
#### Summary
----------------------------------------------**ISSUE DESCRIPTION AND HOW TO REPRODUCE**- The loading animation in the OutSystems chart sometimes persists indefinitely, often when the list is empty, but also even after data has been successfully fetched and fed into the chart. This results in the data not being displayed as expected to the end user**IMPACT ON THE CUSTOMER**- This is affecting End-Users intermittently and they get blocked until the refresh of the application.**TROUBLESHOOTING STEPS &amp; WORKAROUND**- So far, from an occurrence where they shared a HAR file as well, we could see several 404s related to highcharts scripts among other errors in the cloudfront
- https://outsystems.grafana.net/d/cdeqzn1jj77cwe/general-troubleshooting?var-filter=&amp;var-exclude=&amp;var-ring=ga&amp;var-tenant=02c77b3a-7976-40e9-9d5a-24ee25c02bea&amp;var-cluster=$__all&amp;var-severity=Error&amp;var-runtime=$__all&amp;var-traceDuration=$__all&amp;var-region=eu-central-1&amp;var-environment=$__all&amp;var-regionShort=ga-eu-ce-1-01&amp;var-tenant_prefix=bluekern&amp;var-application=866ff104-d81a-4500-b7c1-3f996997ab90&amp;var-cluster_old=$__all&amp;var-module_name=managementreportingnhood&amp;from=2024-08-07T13:00:00.000Z&amp;to=2024-08-07T15:35:59.000Z&amp;timezone=browser- ![](https://supportoutsystems.zendesk.com/attachments/token/RVAE2xrzQL5qY8UQUllq90dzy/?name=image.png)- ![](https://supportoutsystems.zendesk.com/attachments/token/KTH5bGusv3wRb77ekVp2VejI5/?name=image.png)
- They have a condition for the disable loading animation property similar to this:DataAction2.Out1.Empty and DataAction2.IsDataFetched- We could get the same behavior with the same condition, but when setting it directly to false we could get the infinite loading animation. With or without DisableLoadingAnimation set to false, we get different behavior on the first load than if we use a toggle to show some data.  When we are under similar conditions as the customer, we get a blank chart (rather than the &quot;no data to display&quot; text), and if we set it to False, we get the infinite loading animation.
- If it is set to False, then it should at least stop the animation once the data is loaded into the chart- Here: (public access, disable animation currently set to false instead of the condition so the loading animation should be infinite) https://gs-sandbox-ga-eu-01-dev.outsystems.app/SandApp/Case3045914- We would like to understand why this could be happening to suggest a possible way to fix it to the customer, they have opened another case with some issues with these widgets related to loading the content, and I personally (offtopic) also had some issues where only the legends were visible but not the actual chart (but the HTML tags were the chart should be are there), so it seems unstable sometimes
- (We couldn't access the customer application on the browser because they display their client's data, even in development it seems... just to let you know)**TECH DATA OR ANY OTHER RELEVANT INFO**
The customer attached a video:- 1723038403000000000__OutSystemsCharts-loading-issue.mp4
Omls attached:- SandApp.oml (my take)
- management reporting nhood Chart Loading Issue.oml (customers app) -&gt; ScreenBlocks_Finance &gt; ThirdParty_ReceivablesAndPayablesHar File from the customer:- case_2.harRing: ga
Tenant Id: 02c77b3a-7976-40e9-9d5a-24ee25c02bea
Tenant Prefix: bluekern
Region: eu-central-1
HBW.WTB.KPW.SNX.JHH.KYT.JIB.WOU_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_Attachment(s):
SandApp.oml - https://supportoutsystems.zendesk.com/attachments/token/rUxC9AzFDLpnTIG6wKxPCVMIb/?name=SandApp.omlmanagement reporting nhood Chart Loading Issue.oml - https://supportoutsystems.zendesk.com/attachments/token/6x7eSahYZMq4Nqz5UgkjI2MQ3/?name=management+reporting+nhood+Chart+Loading+Issue.oml
## 📝 RetrospectiveinfoDetails
**Ring:** ga
**System-wide impact:**&nbsp; 
**Tenant ID:** 02c77b3a-7976-40e9-9d5a-24ee25c02bea
**Tenant Prefix:** bluekern
**Routing Error Code:** N/A
**Product Area:** Phoenix::Application Runtime::Starter Apps::OutSystems Charts
### Impact:### Investigation and troubleshooting findings:### Resolution:## Tasks performed during incident resolution:
&nbsp;
## Executive Summary
[Guidelines](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4144496679/Incident+Retrospectives+-+Playbook#STEP-3---Write-the-Executive-Summary)
## Root Causes 
[Guidelines](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4144496679/Incident+Retrospectives+-+Playbook#STEP-1---Perform-the-Root-Cause-Analysis)

If the customer needs formal RCA, please fill out the following field with the document URL

[Please follow these instructions and place the RCA URL in the field below.](https://docs.google.com/document/d/13rXmBsOJh73nV2D6Z17SIBGBu2HOTWty5ddsvU000JM/edit#heading=h.bqxasxszr5q)

RCA URL

&lt;Place the URL of the customer RCA here if you have created one&gt;
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/850-outsystems-charts-loading-issue)

**Date**

**Source**

**User**

**Event**
August 9 12:34 AM WESTwebRootly
created an alert via
August 9 12:34 AM WESTwebRootly
Rootly created this incident
August 9 12:34 AM WESTwebRootly
In triage date has been set to August 9 12:34 AM WEST
August 9 12:34 AM WESTwebRootly[Slack Channel](https://slack.com/app_redirect?channel=C07G3KNCD2R&amp;team=T041063TZ) has been createdAugust 9 12:34 AM WESTwebRootly
Ring: ga
System-wide impact:  
Tenant ID: 02c77b3a-7976-40e9-9d5a-24ee25c02bea
Tenant Prefix: bluekern
Routing Error Code: N/A
Product Area: Phoenix::Application Runtime::Starter Apps::OutSystems Charts
August 9 12:34 AM WESTwebRootly[PagerDuty Incident](https://outsystems.pagerduty.com/incidents/Q0IBWG5HK3UZD2) has been created.
📧 Notified Rafaela Al&eacute;xis by email.&nbsp;&nbsp;📲 Notified Rafaela Al&eacute;xis by push notification.  (via iPhone)August 9 12:34 AM WESTwebRootlyRafaela Al&eacute;xis has been assigned as EngineerAugust 9 12:35 AM WESTwebRootly
Rafaela Al&eacute;xis acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q0IBWG5HK3UZD2). (via Phone)
August 9 12:44 AM WESTwebRootly
This incident was instantiated in Jira: RDINC-28226. Please work the incident using Rootly
August 9 12:52 AM WESTwebRafaela Al&eacute;xis
Incident has been started
August 9 12:52 AM WESTwebRootly
Pagerduty Integrations acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q0IBWG5HK3UZD2). (via Phone)
August 9  1:05 AM WESTwebRafaela Al&eacute;xisSend ZenDesk private comment has been set: Hi team,After looking at the ticket, I don't think this is a severity 2 since it doesn't always happen and is not a critical issue. Also, this seems to be a problem with the OutSystems Charts which is an asset from the UI Components team and has nothing to do with the portal teams.August 9  1:05 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hi team,After looking at the ticket, I don't think this is a severity 2 since it doesn't always happen and is not a critical issue. Also, this seems to be a problem with the OutSystems Charts which is an asset from the UI Components team and has nothing to do with the portal teams.
August 9  1:05 AM WESTwebRootlySend ZenDesk private comment has been unsetAugust 9  1:05 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

August 9  1:34 AM WESTwebRootly
This incident was instantiated in Jira: RDINC-28226. Please work the incident using Rootly
August 9  9:14 AM WESTwebGon&ccedil;alo MartinsGon&ccedil;alo Martins has been assigned as CommanderAugust 9  9:14 AM WESTwebGon&ccedil;alo MartinsGiuliana Silva has been assigned as EngineerAugust 9 12:32 PM WESTwebGon&ccedil;alo Martins
After looking at the ticket, I agree this is not a severity 2 since it doesn't always happen, is not a critical issue (not even a common use case) and it has a workaround.
To review and fix it in the product we've created the task ROU-11000 (for future reference on release notes) but we can't provide an ETA besides saying it will be off by the end of Q3 2024.In terms of mitigation and workaround, the customer can enclose the Chart on an If statement looking at DataAction2.IsDataFetched and in this case it will always work as expected (find the image attached).
[ChartsLoadingWorkaround.PNG](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDI4MTY4LCJwdXIiOiJibG9iX2lkIn19--aabd6e1b647fde2375a4219b4116dc322f4c8e80/ChartsLoadingWorkaround.PNG)August 9 12:36 PM WESTwebGon&ccedil;alo Martins
Incident has been mitigated
August 9  5:23 PM WESTwebRootlyZendesk Private Comment has been set: ----------------------------------------------**Update to R&amp;D**
- For this incident there is discussion of a workaround. I will share workaround with customer and ask for confirmation if whether they have been able to implement the pattern successfully.__August 9  5:23 PM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
- For this incident there is discussion of a workaround. I will share workaround with customer and ask for confirmation if whether they have been able to implement the pattern successfully.__
August 19  7:03 PM WESTwebRootly
The Global Support team marked this incident as closed in ZenDesk.
August 19  7:03 PM WESTwebRootly
Incident has been resolved
August 19  7:03 PM WESTwebRootlyZenDesk Event Type has been set: solved