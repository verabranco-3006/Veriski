---
title: Retrospective-SEV3-Enxtensibility - Can't "clear" de value
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4394319964/Retrospective-SEV3-Enxtensibility+-+Can+t+clear+de+value
confluence_space: RKB
confluence_page_id: 4394319964
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV3-Enxtensibility - Can't "clear" de value

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV3

Teams:&nbsp;trueBlueIde Group

Types:&nbsp;trueBlueCustomer Escalated
#### 🕐 Timestamps
Started At:&nbsp;trueBlueAugust 29  8:13 AM WEST

Mitigated At:&nbsp;trueYellowAugust 29  9:56 AM WEST

Resolved At:&nbsp;trueGreenAugust 29  9:56 AM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/944-enxtensibility-can-t-clear-de-value)
[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3053141)

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

Sandeep Pal
#### Summary
----------------------------------------------**ISSUE DESCRIPTION AND HOW TO REPRODUCE**
The requester has reported an issue when deleting or clearing the extensibility configurations, after publishing and reopening the app, the extensibility configurations are still there, the requester has attached a video and diagnostic reports for the analysis**IMPACT ON THE CUSTOMER**
No major impact now, it was a blocker at its moment because they needed the application package without these configs but a workaround was found by the requester**TROUBLESHOOTING STEPS &amp; WORKAROUND**
n/a I couldn't reproduce it as it worked just as expected, not sure what is happening but the requester also mentioned that it happened on other tenants and not only his
Workaround: When leaving only empty curly braces {} the issue does not happen**TECH DATA OR ANY OTHER RELEVANT INFO****Tenant ID** (mandatory)**: 34faba60-891f-4409-8584-39332e5b9123**
**Stage ID** (mandatory**):** 97b276cc-f670-4ecf-8fab-06cb45f86883
**Application Key** (mandatory if appl.)**: aaf38349-39b5-40e5-a29a-81483b659c25**
**Timeline with start and end date/hour** (mandatory)**: Reported on August 23rd at 9:39 am UTC-6****OutSystems revisions of the components involved (this includes for example revision of ODC Studio or Forge Supported Plugins)** (mandatory if appl.)**: **
1. https://www.outsystems.com/SupportPortal/DownloadAmazon.aspx?TicketGUID=13fba9e8-392c-411e-9bde-56193d5ed035&amp;FileName=1724860069262_Order+Approval+rev+5.oml#hide**Diagnostics report** (mandatory for ODC Studio-related issues)
1. https://www.outsystems.com/SupportPortal/DownloadAmazon.aspx?TicketGUID=13fba9e8-392c-411e-9bde-56193d5ed035&amp;FileName=1724860069262_1724842851000000000__delete_publish.txt#hide
2. https://www.outsystems.com/SupportPortal/DownloadAmazon.aspx?TicketGUID=13fba9e8-392c-411e-9bde-56193d5ed035&amp;FileName=1724860069262_1724842853000000000__open_again.txt#hide**Grafana dashboards** (adjusted to timeline/tenant/environment/service)**:** 1CPs https://outsystems.grafana.net/d/cdgg5feb0g6bkd/publish-deploy-mabs?var-ring=ea&amp;var-tenant=34faba60-891f-4409-8584-39332e5b9123&amp;var-mobile_platform=$__all&amp;var-region=$__all&amp;var-application=aaf38349-39b5-40e5-a29a-81483b659c25&amp;var-stamp=$__all&amp;from=2024-08-21T15:59:40.710Z&amp;to=2024-08-28T15:59:40.711Z&amp;timezone=utc**Video:** https://www.outsystems.com/SupportPortal/DownloadAmazon.aspx?TicketGUID=13fba9e8-392c-411e-9bde-56193d5ed035&amp;FileName=1724669360000000000__Extensibility.mp4_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 RetrospectiveinfoDetails
**Ring:** ea
**System-wide impact:**&nbsp; 
**Tenant ID:** 34faba60-891f-4409-8584-39332e5b9123
**Tenant Prefix:** rubensantosdemos
**Routing Error Code:** N/A
**Product Area:** Phoenix::ODC Studio::OML Save Load and Upgrade
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/944-enxtensibility-can-t-clear-de-value)

**Date**

**Source**

**User**

**Event**
August 28  5:05 PM WESTwebRootly
created an alert via
August 28  5:05 PM WESTwebRootly
Rootly created this incident
August 28  5:05 PM WESTwebRootly
In triage date has been set to August 28  5:05 PM WEST
August 28  5:05 PM WESTwebRootlyAccess Zendesk ticket (VPN) has been set: https://extranetinternalapps-prd.outsystems.net/TKT_CustomerTicket_UI/CustomerTicket_Detail?TicketITSMId=3053141August 29  8:13 AM WESTwebSandeep Pal
Incident has been started
August 29  8:15 AM WESTwebSandeep PalSandeep Pal has been assigned as EngineerAugust 29  8:50 AM WESTwebSandeep PalSend ZenDesk private comment has been set: Hi Team,
&nbsp;&nbsp;
The issue reported in this incident is being fixed under JIRA issue https://outsystemsrd.atlassian.net/browse/RDEV-7699. This should be there in the upcoming release.August 29  8:50 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

Hi Team,
&nbsp;&nbsp;
The issue reported in this incident is being fixed under JIRA issue https://outsystemsrd.atlassian.net/browse/RDEV-7699. This should be there in the upcoming release.August 29  8:50 AM WESTwebRootlySend ZenDesk private comment has been unsetAugust 29  8:50 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

August 29  9:02 AM WESTwebSandeep PalSend ZenDesk private comment has been set: Hi Team,
&nbsp;&nbsp;
The issue was in the IDE where user was not able to set empty extensibility settings and its being fixed under JIRA issue [https://outsystemsrd.atlassian.net/browse/RDEV-7699](https://outsystemsrd.atlassian.net/browse/RDEV-7699). This should be fixed in the upcoming release.August 29  9:02 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

Hi Team,
&nbsp;&nbsp;
The issue was in the IDE where user was not able to set empty extensibility settings and its being fixed under JIRA issue [https://outsystemsrd.atlassian.net/browse/RDEV-7699](https://outsystemsrd.atlassian.net/browse/RDEV-7699). This should be fixed in the upcoming release.August 29  9:02 AM WESTwebRootlySend ZenDesk private comment has been unsetAugust 29  9:02 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

August 29  9:56 AM WESTwebRootly
The Global Support team marked this incident as closed in ZenDesk.
August 29  9:56 AM WESTwebRootly
Incident has been resolved
August 29  9:56 AM WESTwebRootlyZenDesk Event Type has been set: solved