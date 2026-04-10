---
title: Retrospective-SEV3-Can't access subscription info page, there is an error loading the data (OS-CORE-HOST-50001). It has been like this all day
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4307419422/Retrospective-SEV3-Can+t+access+subscription+info+page+there+is+an+error+loading+the+data+OS-CORE-HOST-50001+.+It+has+been+like+this+all+day
confluence_space: RKB
confluence_page_id: 4307419422
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV3-Can't access subscription info page, there is an error loading the data (OS-CORE-HOST-50001). It has been like this all day

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV3

Teams:&nbsp;trueBlueNeo Platform Theseus
#### 🕐 Timestamps
Started At:&nbsp;trueBlueJuly 16 10:41 AM WEST

Mitigated At:&nbsp;trueYellowJuly 24 12:47 PM WEST

Resolved At:&nbsp;trueGreenJuly 24 12:47 PM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/709-can-t-access-subscription-info-page-there-is-an-error-loading-the-data-os-core-host-50001-it-has-been-like-this-all-day)
[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3036809)

#### 🧑&zwj;🚒 Incident Rolestrue
**Stakeholder**

Rodrigo Silva

**Engineer**

Guilherme Rolo
#### Summary
----------------------------------------------**R&amp;D ESCALATION FORM**
Section comments can be removed for R&amp;D easier interpretation.**ISSUE DESCRIPTION AND HOW TO REPRODUCE**
Customers are unable to go to their subscription page.![](https://supportoutsystems.zendesk.com/attachments/token/3fqLUS4xwojZyo2HF9HEHX4be/?name=image.png)**IMPACT ON THE CUSTOMER**
Unable to check their subscription usage.**TROUBLESHOOTING STEPS &amp; WORKAROUND**
N/A**TECH DATA OR ANY OTHER RELEVANT INFO**
Ring: ea
Tenant Id: 5167f99c-5c3a-4b76-af38-d3ad8877f7da
Tenant Prefix: ntt-data
Region: eu-central-1
GBA.VP0.WLD.9HU.MCO.ESI.UPO.AUT_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 RetrospectiveinfoDetails
**Ring:** ea
**System-wide impact:**&nbsp; 
**Tenant ID:** 5167f99c-5c3a-4b76-af38-d3ad8877f7da
**Tenant Prefix:** ntt-data
**Routing Error Code:** N/A
**Product Area:** Phoenix::Phoenix Portal::Subscription
### Impact:
It was not possible to see the subscription page
### Investigation and troubleshooting findings:### Resolution:
There was a migration in Entitlement Service, and part of the new process was not working as intended. It has now been fixed.
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/709-can-t-access-subscription-info-page-there-is-an-error-loading-the-data-os-core-host-50001-it-has-been-like-this-all-day)

**Date**

**Source**

**User**

**Event**
July 15  5:36 PM WESTwebRootly
created an alert via
July 15  5:36 PM WESTwebRootly
Rootly created this incident
July 15  5:36 PM WESTwebRootly
In triage date has been set to July 15  5:36 PM WEST
July 16  9:30 AM WESTwebLaura Huysamen
Teams has been added: Neo Platform Theseus
July 16  9:32 AM WESTwebLaura Huysamen
Entitlement Service threw a null-reference exception. (e.g.  15-07-202413:50:15). Needs further investigation.https://outsystems.grafana.net/explore?schemaVersion=1&amp;panes=%7B%22ty3%22:%7B%22datasource%22:%22grafanacloud-outsystemstest-logs%22,%22queries%22:%5B%7B%22refId%22:%22A%22,%22expr%22:%22%7Bring%3D~%5C%22ea%5C%22,%20service_name%3D~%5C%22Entitlement.Service%5C%22%7D%20%7C~%20%5C%22%5C%22%20%7C%20json%20%5Cr%5Cn%22,%22editorMode%22:%22code%22,%22queryType%22:%22range%22,%22datasource%22:%7B%22type%22:%22loki%22,%22uid%22:%22grafanacloud-outsystemstest-logs%22%7D%7D%5D,%22range%22:%7B%22from%22:%221721051302749%22,%22to%22:%221721051499198%22%7D%7D%7D&amp;orgId=1
July 16 10:27 AM WESTwebRodrigo SilvaRodrigo Silva has been assigned as StakeholderJuly 16 10:27 AM WESTwebRodrigo SilvaGuilherme Rolo has been assigned as EngineerJuly 16 10:41 AM WESTwebGuilherme Rolo
Incident has been started
July 16 12:06 PM WESTwebGuilherme Rolo
Created https://outsystemsrd.atlassian.net/browse/RDPSTT-1992
July 16  2:36 PM WESTwebJo&atilde;o Semedo
Teams has been removed: Neo DevExperience DeliveryAutomation
July 18 11:07 AM WESTwebRootlyZendesk Private Comment has been set: ----------------------------------------------**Update to R&amp;D**
Hey team,We're sharing this update to let you know that this issue has been reported on more than one Tenant and, as such, we've needed to create a casr on our end to centralize all troubleshooting, and rootly doesn't support transfer across zendesk cases. You're welcome to close this rootly and share all new updates on Rootly 723.Thanks!__July 18 11:07 AM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
Hey team,We're sharing this update to let you know that this issue has been reported on more than one Tenant and, as such, we've needed to create a casr on our end to centralize all troubleshooting, and rootly doesn't support transfer across zendesk cases. You're welcome to close this rootly and share all new updates on Rootly 723.Thanks!__
July 24 10:48 AM WESTwebRootlyZenDesk Event Type has been set: solvedJuly 24 10:48 AM WESTwebRootly
The Global Support team marked this incident as closed in ZenDesk.
July 24 12:47 PM WESTwebGuilherme Rolo
Incident has been resolved
July 24 12:47 PM WESTwebGuilherme RoloImpact has been set: It was not possible to see the subscription pageJuly 24 12:47 PM WESTwebGuilherme RoloResolution has been set: There was a migration in Entitlement Service, and part of the new process was not working as intended. It has now been fixed.