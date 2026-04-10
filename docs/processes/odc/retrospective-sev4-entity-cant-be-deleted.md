---
title: Retrospective-SEV4-Entity can't be deleted
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4392124724/Retrospective-SEV4-Entity+can+t+be+deleted
confluence_space: RKB
confluence_page_id: 4392124724
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV4-Entity can't be deleted

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV4

Teams:&nbsp;trueBlueRuntime Data Model
#### 🕐 Timestamps
Started At:&nbsp;trueBlueAugust 20  4:10 PM WEST

Mitigated At:&nbsp;trueYellowAugust 28  6:04 PM WEST

Resolved At:&nbsp;trueGreenAugust 28  6:04 PM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/759-entity-can-t-be-deleted)
[Slack channel](https://slack.com/app_redirect?channel=C07HQ7QCWV8&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3011443)

#### Summary
----------------------------------------------**R&amp;D ESCALATION FORM**
Section comments can be removed for R&amp;D easier interpretation.**ISSUE DESCRIPTION AND HOW TO REPRODUCE**
Whenever the customer tries to delete the WeclappSyncProcess table it results in a database error:An error has occurred while executing SQL scripts: SQL script execution error. constraint &quot;osfrk_2lg0sdh_xuq_wecla_zoa2b7ct5ee0_wecla_zoaxcva8s773_weclnid&quot; of relation &quot;WeclappSyncProcess&quot; does not exist (OS-RDBE-GEN-50010)&nbsp;An error has occurred while executing SQL scripts: SQL script execution error. constraint &quot;osfrk_2lg0sdh_xuq_wecla_zoa2b7ct5ee0_wecla_zoaxcva8s773_weclnid&quot; of relation &quot;WeclappSyncProcess&quot; does not exist (OS-RDBE-GEN-50010)- We were able to remove any relationship between the tables and still the errors occurs:![](https://supportoutsystems.zendesk.com/attachments/token/hRB9bsqgBJwu22u3seTNPVfvR/?name=image.png)- We need help understanding what's going on.**IMPACT ON THE CUSTOMER**- No impact, the customer no longer uses this app but wants to know why this happens.**TROUBLESHOOTING STEPS &amp; WORKAROUND**- We tried to remove any reference but it's still not possible to delete and publish.**TECH DATA OR ANY OTHER RELEVANT INFO**
Ring: ga
Tenant Id: 240decb9-055a-4f0d-937a-946e6abcec1c
Tenant Prefix: scaleits
Region: eu-central-1
JGS.WV5.TWS.5OQ.OZY.UJU.ZLW.GTS_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_Attachment(s):
The One - Old (2).oml - https://supportoutsystems.zendesk.com/attachments/token/BBYcDuaFt1gOIAHNMymvJzUAh/?name=The+One+-+Old+%282%29.oml
## 📝 RetrospectiveinfoDetails
**Ring:** ga
**System-wide impact:**&nbsp; 
**Tenant ID:** 240decb9-055a-4f0d-937a-946e6abcec1c
**Tenant Prefix:** scaleits
**Routing Error Code:** OS-RDBE
**Product Area:** -
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/759-entity-can-t-be-deleted)

**Date**

**Source**

**User**

**Event**
July 25  6:05 PM WESTwebRootly
created an alert via
July 25  6:05 PM WESTwebRootly
Rootly created this incident
July 25  6:05 PM WESTwebRootly
In triage date has been set to July 25  6:05 PM WEST
August 19  5:59 PM WESTwebRootlyZendesk Private Comment has been set: ----------------------------------------------**Update to R&amp;D**
- Hello TeamA new Rootly with ID #901 was created since this is affecting more customers.Please respond on that one and discard the current Rootly.Kind regards__August 19  5:59 PM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
- Hello TeamA new Rootly with ID #901 was created since this is affecting more customers.Please respond on that one and discard the current Rootly.Kind regards__
August 20  4:07 PM WESTwebRootly[Slack Channel](https://slack.com/app_redirect?channel=C07HQ7QCWV8&amp;team=T041063TZ) has been createdAugust 20  4:10 PM WESTwebAnt&oacute;nio Caeiro
Incident has been started
August 20  4:11 PM WESTwebAnt&oacute;nio CaeiroSend ZenDesk private comment has been set: Hello support team,  
can you validate if the customer still has this error,&nbsp;  
I no longer seem to have logs for this case for this tenant  example:  https://outsystems.grafana.net/explore?schemaVersion=1&amp;panes=%7B%22a1r%22:%7B%22datasource%22:%22grafanacloud-outsystemstest-logs%22,%22queries%22:%5B%7B%22datasource%22:%7B%22type%22:%22loki%22,%22uid%22:%22grafanacloud-outsystemstest-logs%22%7D,%22editorMode%22:%22code%22,%22expr%22:%22%7Bring%3D%5C%22ga%5C%22,%20service\_name%3D%5C%22Database.Script.Executor%5C%22,%20stamp%3D~%5C%22rundev-ga-eu-ce-1-01%7Crunp-ga-eu-ce-1-01%7Crunnp-ga-eu-ce-1-01%5C%22%7D%20%5Cr%5Cn%20%20%20%20%7C%20json%20%7C%20severity%21%3D%60Information%60%5Cr%5Cn%20%20%20%20%7C%3D%20%60240decb9-055a-4f0d-937a-946e6abcec1c%60%22,%22maxLines%22:1000,%22queryType%22:%22range%22,%22refId%22:%22A%22%7D%5D,%22range%22:%7B%22from%22:%221721430000000%22,%22to%22:%221721948399000%22%7D%7D%7D&amp;orgIAugust 20  4:11 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hello support team,  
can you validate if the customer still has this error,&nbsp;  
I no longer seem to have logs for this case for this tenant  example:  https://outsystems.grafana.net/explore?schemaVersion=1&amp;panes=%7B%22a1r%22:%7B%22datasource%22:%22grafanacloud-outsystemstest-logs%22,%22queries%22:%5B%7B%22datasource%22:%7B%22type%22:%22loki%22,%22uid%22:%22grafanacloud-outsystemstest-logs%22%7D,%22editorMode%22:%22code%22,%22expr%22:%22%7Bring%3D%5C%22ga%5C%22,%20service\_name%3D%5C%22Database.Script.Executor%5C%22,%20stamp%3D~%5C%22rundev-ga-eu-ce-1-01%7Crunp-ga-eu-ce-1-01%7Crunnp-ga-eu-ce-1-01%5C%22%7D%20%5Cr%5Cn%20%20%20%20%7C%20json%20%7C%20severity%21%3D%60Information%60%5Cr%5Cn%20%20%20%20%7C%3D%20%60240decb9-055a-4f0d-937a-946e6abcec1c%60%22,%22maxLines%22:1000,%22queryType%22:%22range%22,%22refId%22:%22A%22%7D%5D,%22range%22:%7B%22from%22:%221721430000000%22,%22to%22:%221721948399000%22%7D%7D%7D&amp;orgI
August 20  4:11 PM WESTwebRootlySend ZenDesk private comment has been unsetAugust 20  4:11 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

August 21  7:26 PM WESTwebRootlyAccess Zendesk ticket (VPN) has been set: https://extranetinternalapps-prd.outsystems.net/TKT_CustomerTicket_UI/CustomerTicket_Detail?TicketITSMId=3011443August 28  6:04 PM WESTwebRootly
Incident has been resolved
August 28  6:04 PM WESTwebRootlyZenDesk Event Type has been set: solvedAugust 28  6:04 PM WESTwebRootly
The Global Support team marked this incident as closed in ZenDesk.