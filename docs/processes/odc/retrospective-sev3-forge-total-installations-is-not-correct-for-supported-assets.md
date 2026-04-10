---
title: Retrospective-SEV3-Forge total installations is not correct for supported assets
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4339073452/Retrospective-SEV3-Forge+total+installations+is+not+correct+for+supported+assets
confluence_space: RKB
confluence_page_id: 4339073452
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV3-Forge total installations is not correct for supported assets

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV3

Teams:&nbsp;trueBlueNeo Platform Theseus
#### 🕐 Timestamps
Started At:&nbsp;trueBlueJuly 30  1:48 PM WEST

Mitigated At:&nbsp;trueYellowAugust 6  7:10 PM WEST

Resolved At:&nbsp;trueGreenAugust 6  7:10 PM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/775-forge-total-installations-is-not-correct-for-supported-assets)
[Slack channel](https://slack.com/app_redirect?channel=C07F29J409X&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3042232)

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

Ricardo Duarte
#### Summary
----------------------------------------------**ISSUE DESCRIPTION AND HOW TO REPRODUCE**
- An internal customer reports that the &quot;/forge/v1alpha1/asset&quot; API fails to correctly report the total number of installations for supported assets.
- This issue can be demonstrated in the ODC Portal Local Dev Tenant.
- For example AI Agent builder returning only one installation despite user updates.![](https://supportoutsystems.zendesk.com/attachments/token/md81UO4vsWhlZvPRDVjUSLUDK/?name=image.png)![](https://supportoutsystems.zendesk.com/attachments/token/yVAGZHSNVVGcnb5PVQISBOtUO/?name=image.png)**IMPACT ON THE CUSTOMER**
Brief description of the impact on the customer/development team/other, including:
- Development, Test, Production
- Ongoing
- Unable to accurately asses whenever supported assets are installed or updated by users.**TROUBLESHOOTING STEPS &amp; WORKAROUND**
**-** The Slack thread of the discussion so far can be found here: https://outsystems.slack.com/archives/C02HK86CD1U/p1721309055329029
- The customer is requesting this issue be redirected to the **Theseus** and **Maestro** team for validation.![](https://supportoutsystems.zendesk.com/attachments/token/ijhOjZ6RHxorPw4OjxNqxfmFD/?name=image.png)**TECH DATA OR ANY OTHER RELEVANT INFO**- Ring: ea
- Tenant Id: dc3a3772-693b-4b6a-aa61-5fea3976eeb3
- Tenant Prefix: odc-portal-localdev
- Region: us-east-1
- O9S.CS3.32J.2KY.BVW.S0T.LK4.U6Q_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 RetrospectiveinfoDetails
**Ring:** ea
**System-wide impact:**&nbsp; No
**Tenant ID:** dc3a3772-693b-4b6a-aa61-5fea3976eeb3
**Tenant Prefix:** odc-portal-localdev
**Routing Error Code:** N/A
**Product Area:** Phoenix::Phoenix Portal::Configurations
### Impact:
The total installation counter was not correct
### Investigation and troubleshooting findings:
Total installation counter was not being done to supported assets
### Resolution:
The total installation counter  was updated to now include supported apps but not built in
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/775-forge-total-installations-is-not-correct-for-supported-assets)

**Date**

**Source**

**User**

**Event**
July 29 11:09 PM WESTwebRootly
created an alert via
July 29 11:09 PM WESTwebRootly
Rootly created this incident
July 29 11:09 PM WESTwebRootly
In triage date has been set to July 29 11:09 PM WEST
July 29 11:19 PM WESTwebRootly
This incident was instantiated in Jira: RDINC-27805. Please work the incident using Rootly
July 30 12:09 AM WESTwebRootly
This incident was instantiated in Jira: RDINC-27805. Please work the incident using Rootly
July 30 10:19 AM WESTwebCl&aacute;udia Rezende
Teams has been added: Neo Platform Theseus
July 30 10:19 AM WESTwebCl&aacute;udia Rezende
Teams has been removed: ALM Consoles
July 30 10:23 AM WESTwebCl&aacute;udia Rezende
As agreed support ticket redirected to the Theseus team for analysis.
slack: https://outsystems.slack.com/archives/C02HK86CD1U/p1721309055329029

July 30  1:46 PM WESTwebRicardo DuarteRicardo Duarte has been assigned as EngineerJuly 30  1:47 PM WESTwebRootly[Slack Channel](https://slack.com/app_redirect?channel=C07F29J409X&amp;team=T041063TZ) has been createdJuly 30  1:48 PM WESTwebRicardo Duarte
Incident has been started
August 6  7:10 PM WESTwebRicardo Duarte
Incident has been resolved
August 6  7:10 PM WESTwebRicardo DuarteSystem-wide impact has been set: NoAugust 6  7:10 PM WESTwebRicardo DuarteImpact has been set: The total installation counter was not correctAugust 6  7:10 PM WESTwebRicardo DuarteInvestigation and troubleshooting findings has been set: Total installation counter was not being done to supported assetsAugust 6  7:10 PM WESTwebRicardo DuarteResolution has been set: The total installation counter  was updated to now include supported apps but not built in