---
title: Retrospective-SEV3-Error logs, when log error is set to No
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4334780431/Retrospective-SEV3-Error+logs+when+log+error+is+set+to+No
confluence_space: RKB
confluence_page_id: 4334780431
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV3-Error logs, when log error is set to No

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV3

Teams:&nbsp;trueBlueBackend Runtime
#### 🕐 Timestamps
Started At:&nbsp;trueBlueAugust 5  2:00 PM WEST

Mitigated At:&nbsp;trueYellowAugust 5  2:00 PM WEST

Resolved At:&nbsp;trueGreenAugust 5  2:00 PM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/679-error-logs-when-log-error-is-set-to-no)
[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3030563)

#### Summary
----------------------------------------------**ISSUE DESCRIPTION AND HOW TO REPRODUCE**- REST exceptions cannot be filtered from logs even if we implement exception handling mechanism set to **not** log messages.![](https://supportoutsystems.zendesk.com/attachments/token/RBnZwKhpY4PyrfZyX2aDnJAwV/?name=image.png)![](https://supportoutsystems.zendesk.com/attachments/token/8ZGzKwM9iYGuupHGCD88cbdMO/?name=image.png)![](https://supportoutsystems.zendesk.com/attachments/token/qJ5X7lKZ9LQfY0Repsi6ccRM5/?name=image.png)
- OML attached.**IMPACT ON THE CUSTOMER**- Production;
- Log pollution - customer expects to have error response codes from their consumed APIs and wants to filter out these exceptions from the logs, but cannot.**TROUBLESHOOTING STEPS &amp; WORKAROUND**- Tried to set response code to 200 in **OnAfterResponse**, but that doesn't have any effect.**TECH DATA OR ANY OTHER RELEVANT INFO**
N/A_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 RetrospectiveinfoDetails
**Ring:** ga
**System-wide impact:**&nbsp; No
**Tenant ID:** 1d37dc36-3f96-49bc-8c98-3e0c97c9cf4a
**Tenant Prefix:** ovam
**Routing Error Code:** N/A
**Product Area:** Phoenix::Application Runtime::Logging and Tracing
### Impact:
Already solved here: [https://outsystemsrd.atlassian.net/browse/RDINC-26551](https://outsystemsrd.atlassian.net/browse/RDINC-26551)
### Investigation and troubleshooting findings:
Already solved here: [https://outsystemsrd.atlassian.net/browse/RDINC-26551](https://outsystemsrd.atlassian.net/browse/RDINC-26551)
### Resolution:
Already solved here: [https://outsystemsrd.atlassian.net/browse/RDINC-26551](https://outsystemsrd.atlassian.net/browse/RDINC-26551)
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/679-error-logs-when-log-error-is-set-to-no)

**Date**

**Source**

**User**

**Event**
July 5  3:54 PM WESTwebRootly
created an alert via
July 5  3:54 PM WESTwebRootly
Rootly created this incident
July 5  3:54 PM WESTwebRootly
In triage date has been set to July 5  3:54 PM WEST
July 9 10:08 AM WESTwebRootlyZenDesk Event Type has been set: solvedJuly 9 10:08 AM WESTwebRootly
The Global Support team marked this incident as closed in ZenDesk.
August 5  2:00 PM WESTwebRui Garcia
Incident has been started
August 5  2:00 PM WESTwebRui Garcia
Incident has been resolved
August 5  2:00 PM WESTwebRui GarciaSystem-wide impact has been set: NoAugust 5  2:00 PM WESTwebRui GarciaImpact has been set: Already solved here: https://outsystemsrd.atlassian.net/browse/RDINC-26551August 5  2:00 PM WESTwebRui GarciaInvestigation and troubleshooting findings has been set: Already solved here: https://outsystemsrd.atlassian.net/browse/RDINC-26551August 5  2:00 PM WESTwebRui GarciaResolution has been set: Already solved here: https://outsystemsrd.atlassian.net/browse/RDINC-26551