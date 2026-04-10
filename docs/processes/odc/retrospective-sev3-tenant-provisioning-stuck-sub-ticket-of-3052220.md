---
title: Retrospective-SEV3-Tenant Provisioning stuck (Sub-ticket of #3052220)
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4390420753/Retrospective-SEV3-Tenant+Provisioning+stuck+Sub-ticket+of+3052220
confluence_space: RKB
confluence_page_id: 4390420753
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV3-Tenant Provisioning stuck (Sub-ticket of #3052220)

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV3

Teams:&nbsp;trueBlueIdentity Core

Types:&nbsp;trueBlueCustomer Escalated
#### 🕐 Timestamps
Started At:&nbsp;trueBlueAugust 28 12:45 PM WEST

Mitigated At:&nbsp;trueYellowAugust 28 12:55 PM WEST

Resolved At:&nbsp;trueGreenAugust 28 12:55 PM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/923-tenant-provisioning-stuck-sub-ticket-of-3052220-9b99623e-9a4a-49ea-a1ad-7261a9c4635f)
[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3052364)

#### Summary
----------------------------------------------**CONSIDERATIONS BEFORE PERFORMING THE ESCALATION TO R&amp;D (MANDATORY)**None of the below points should be overlooked. Failure to do so may imply unnecessary effort.* * *
Ensure the ticket has been **categorized**, otherwise, the R&amp;D escalation will go unnoticed and not be worked on!**1.** For **Incidents**, the **IMAX** was consulted **beforehand** on which:- No incident models were found for the reported symptoms **OR**
- The incident model did not solve the issue **OR**
- The next step indicated in the Incident Model is an escalation to R&amp;D.
**2.** For **Questions**, the ChatODC on the **Slack channel** didn't return an acceptable answer.
**3.** Any other requests that explicitly indicate an R&amp;D escalation is needed.
**4**. **Incident impact assessment** was based on the **prioritization scoring matrix**.* * ***R&amp;D ESCALATION FORM**
Section comments can be removed for R&amp;D easier interpretation.**ISSUE DESCRIPTION AND HOW TO REPRODUCE**
- We received a request to provision a new tenant with the following details:- Tenant Name: autorecover
- Internal Onboard Contact Name: Dhruv Desai
- OnboardContact Email (will receive the link to register as admin in the tenant): dhruv.desai@outsystems.com
- Geo: US
- Region: N. Virginia
- Prefix: autorecover
- Account: OutSystems Internal
- Ring: -3
- ODC Edition: OutSystems Developer Cloud Platform 2023
- This is the JIRA issue link: https://outsystemsrd.atlassian.net/browse/RDTC-642
-We have requested the provisioning using our Provisioning Tool and currently, the License and Cloud status is still stuck on Syncing and Waiting for confirmation![](https://supportoutsystems.zendesk.com/attachments/token/XwPFt6sS53MRETQl7gGxZPb8T/?name=image.png)
-https://www.outsystems.com/LicensingDashboard/Dashboard.aspx?ActivationCode=T32.Y3S.R44.3GX.F1H.92X.H3M.NKA- Grafana &gt; Global Support &gt; Global Support - Identify Activation Code
- ![](https://supportoutsystems.zendesk.com/attachments/token/CBqv0KkuLJj0skei7NdZz7gNK/?name=image.png)
- We do not have access to ring -3 (DEV) to check on the ODC portal**IMPACT ON THE CUSTOMER**
Brief description of the impact on the customer/development team/other, including:
- Stage where the problem is happening (Development / QA / Production); **The tenant is currently being provisioned and it is currently stuck.**
- Frequency of the problem; **Ongoing**
- Business impact or/and development impact; **This issue is delaying our SRE team to start developing****TROUBLESHOOTING STEPS &amp; WORKAROUND**
- We have checked our https://apps.outsystems.app/PortalAccessUtility/ tool, and the State is still **Creating**.![](https://supportoutsystems.zendesk.com/attachments/token/5YXxE0TpbN5KIdQYkfWgT21ej/?name=image.png)
-The Grafana &gt; Global Support &gt; Global Support - Identify Activation Code also shows that the tenant already exist
-On https://www.outsystems.com/LicensingDashboard/RequestList.aspx the License and Cloud status is still syncing and waiting for confirmation![](https://supportoutsystems.zendesk.com/attachments/token/l1seoLvZr6NorYOPt3SyC1L6h/?name=image.png)-We do not have the access to ring -3(DEV) to check their ODC portal**TECH DATA OR ANY OTHER RELEVANT INFO**- **Tenant ID** (mandatory)**: 02bc285f-2e9f-444f-9f76-d3d2108ca857**
- **Stage ID** (mandatory**):**
- **Application Key** (mandatory if appl.)**:**
- **Timeline with start and end date/hour** (mandatory)**: Starts at 2024-08-21 19:00:33 UTC**
- **OutSystems revisions of the components involved (this includes for example revision of ODC Studio or Forge Supported Plugins)** (mandatory if appl.)**:**
- **Diagnostics report** (mandatory for ODC Studio-related issues)**:**
- **Grafana dashboards** (adjusted to timeline/tenant/environment/service):- https://outsystems.grafana.net/d/-KFk87Y4k/global-support-identify-activation-code?orgId=1&amp;var-Tenant=autorecover&amp;from=now-24h&amp;to=now- ![](https://supportoutsystems.zendesk.com/attachments/token/CBqv0KkuLJj0skei7NdZz7gNK/?name=image.png)_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 RetrospectiveinfoDetails
**Ring:** dev
**System-wide impact:**&nbsp; 
**Tenant ID:** N/A
**Tenant Prefix:** N/A
**Routing Error Code:** N/A
**Product Area:** Phoenix::Tenant Provisioning::Provision
### Impact:
An internal customer was blocked while the tenant provisioning couldnt be fixed.
### Investigation and troubleshooting findings:### Resolution:
Manually send some NATS messages to unlock the tenant provisioning process.
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/923-tenant-provisioning-stuck-sub-ticket-of-3052220-9b99623e-9a4a-49ea-a1ad-7261a9c4635f)

**Date**

**Source**

**User**

**Event**
August 26 12:08 AM WESTwebRootly
created an alert via
August 26 12:08 AM WESTwebRootly
Rootly created this incident
August 26 12:08 AM WESTwebRootly
In triage date has been set to August 26 12:08 AM WEST
August 26 12:19 AM WESTwebRootly
This incident was instantiated in Jira: RDINC-28924. Please work the incident using Rootly
August 26  1:08 AM WESTwebRootly
This incident was instantiated in Jira: RDINC-28924. Please work the incident using Rootly
August 28 12:45 PM WESTwebJorge Marin
Incident has been started
August 28 12:46 PM WESTwebJorge Marin
Teams has been added: Identity Core
August 28 12:46 PM WESTwebJorge Marin
Teams has been removed: CMCP
August 28 12:54 PM WESTwebJorge MarinSend ZenDesk private comment has been set: This tenant was fixed under task https://outsystemsrd.atlassian.net/browse/RDPIDT-2598
&nbsp;&nbsp;
https://autorecover.outsystemsrd.dev/identity/.well-known/openid-configurationAugust 28 12:55 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

This tenant was fixed under task https://outsystemsrd.atlassian.net/browse/RDPIDT-2598
&nbsp;&nbsp;
https://autorecover.outsystemsrd.dev/identity/.well-known/openid-configurationAugust 28 12:55 PM WESTwebRootlySend ZenDesk private comment has been unsetAugust 28 12:55 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

August 28 12:55 PM WESTwebJorge Marin
Incident has been resolved
August 28 12:55 PM WESTwebJorge MarinImpact has been set: An internal customer was blocked while the tenant provisioning couldnt be fixed.August 28 12:55 PM WESTwebJorge MarinResolution has been set: Manually send some NATS messages to unlock the tenant provisioning process.August 28 12:55 PM WESTwebJorge MarinRing has been set: devAugust 28 12:56 PM WESTwebJorge MarinRing has been unset: -