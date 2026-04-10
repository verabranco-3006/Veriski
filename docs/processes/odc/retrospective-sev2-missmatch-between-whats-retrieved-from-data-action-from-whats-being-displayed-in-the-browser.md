---
title: Retrospective-SEV2-Missmatch between whats retrieved from data action from what's being displayed in the browser
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4337238097/Retrospective-SEV2-Missmatch+between+whats+retrieved+from+data+action+from+what+s+being+displayed+in+the+browser
confluence_space: RKB
confluence_page_id: 4337238097
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV2-Missmatch between whats retrieved from data action from what's being displayed in the browser

## 📘 Overview
Author:&nbsp;Rootlytrue

Severity:&nbsp;SEV2Redtrue

Teams:&nbsp;Build ServicesBluetrue
#### 🕐 Timestamps
Started At:&nbsp;August 1 8:26 pM WESTBlue

Mitigated At:&nbsp;August 2 2:03 PM WESTYellow

Resolved At:&nbsp;August 2 7:46 PM WESTGreen
#### 🔗 Links
[Incident Page](https://rootly.com/account/incidents/791-missmatch-between-whats-retrieved-from-data-action-from-what-s-being-displayed-in-the-browser)

[Pagerduty incident](https://outsystems.pagerduty.com/incidents/Q2AWAS0MWJKAKD)

[Slack channel](https://slack.com/app_redirect?channel=C07EYDFLMHU&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3043821)

#### 🧑&zwj;🚒 Incident Rolestrue
**Subject Matter Expert**

Jo&atilde;o Lu&iacute;s Almeida

**Engineer**

Jo&atilde;o Lu&iacute;s Almeida
#### Summary
----------------------------------------------**ISSUE DESCRIPTION AND HOW TO REPRODUCE**- Slack thread for context:- https://outsystems.slack.com/archives/C01056JA3N3/p1722528082587209- &amp;- https://outsystems.slack.com/archives/C0280P0R1K3/p1722532970532529
- An issue with the `GetApplications` data action, which correctly returns values from `o11Migration_CS` (O11Migration_GetApplications), including the `O11Status` and `O11_MigrationStatusODC` attributes. However, when accessing these values in `GetApplicationsOnAfterFetch`, they appear to be empty. As a result, the values from `O11Status.Label` are not being displayed in the badges as expected.**IMPACT ON THE CUSTOMER**- This issue is currently blocking the progress as they have a test party scheduled for tomorrow and an EAP release planned for next week**TROUBLESHOOTING STEPS &amp; WORKAROUND**
From support, we just took a look at the conversation in Slack and understood that the issue is being tackled now...Message from Antonio opening the case:&gt; My issue in more detail
&gt;
&gt; **We have a data action called GetApplications that is returning correctly the values from o11Migration_CS (O11Migration_GetApplications), including O11Status and O11_MigrationStatusODC attributes**
&gt; **![](https://www.outsystems.com/SupportPortal/DownloadAmazon.aspx?TicketGUID=aeb1ce77-4056-4ca4-8f75-7c04c52a6bda&amp;FileName=1722526648000000000__1722526647651.png) ![](https://www.outsystems.com/SupportPortal/DownloadAmazon.aspx?TicketGUID=aeb1ce77-4056-4ca4-8f75-7c04c52a6bda&amp;FileName=1722526921000000000__1722526920832.png)**
&gt;
&gt; **In GetApplicationsOnAfterFetch these values are empty**
&gt; **![](https://www.outsystems.com/SupportPortal/DownloadAmazon.aspx?TicketGUID=aeb1ce77-4056-4ca4-8f75-7c04c52a6bda&amp;FileName=1722526822000000000__1722526822024.png)**
&gt;
&gt; **We are expecting to view the values from O11Status.Label in this badge but since they are empty this is how its being displayed**
&gt;
&gt; **![](https://www.outsystems.com/SupportPortal/DownloadAmazon.aspx?TicketGUID=aeb1ce77-4056-4ca4-8f75-7c04c52a6bda&amp;FileName=1722527015000000000__1722527015352.png)**o11migration-831.oml**TECH DATA OR ANY OTHER RELEVANT INFO**
Ring: ea
Tenant Id: dc3a3772-693b-4b6a-aa61-5fea3976eeb3
Tenant Prefix: odc-portal-localdev
Region: us-east-1
O9S.CS3.32J.2KY.BVW.S0T.LK4.U6Q
support_level_8x5_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 Retrospective### Details
**Ring:** ea
**System-wide impact:**&nbsp; 
**Tenant ID:** dc3a3772-693b-4b6a-aa61-5fea3976eeb3
**Tenant Prefix:** odc-portal-localdev
**Routing Error Code:** OS-BLD-COMP
**Product Area:** -
### Impact:
The outputs of data actions with complex usage and structure patterns could get wrongly optimized away, that is, empty values would get returned to the client side of applications, instead of the expected values.
At the extreme, this could result to data corruption.
### Investigation and troubleshooting findings:
A regression in the Backend Build Worker was identified, when comparing the generated code of an affected application with its current vs previous service version.
### Resolution:
Affected versions of the service were banned to prevent the issue from reaching GA, and a rollback was performed on the positive rings - EA and below, through RFC-1277.
## Tasks performed during incident resolution:
- 
Ban the affected versions of the service, to prevent issue from reaching GA: [https://outsystems.slack.com/archives/C0147J20TNY/p1722534665507379](https://outsystems.slack.com/archives/C0147J20TNY/p1722534665507379)

- 
Rollback service to the last validated non-banned version in the positive rings, as mitigation: 
RFC-1277ef8955cb-cb21-32a7-b692-01ace42388d6System Jira

- 
Regression fixed in [v17.1531.0](https://github.com/OutSystems/OutSystems.Build.Job/commit/8e375f553cfa010866f2a84b66b47ec43ab0e385): (a [test](https://github.com/OutSystems/OutSystems.Build.Job/pull/4008) and [resilience](https://github.com/OutSystems/OutSystems.Build.Job/pull/3992) improvements followed later)
RBST-2404ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

## Executive Summary
[Guidelines](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4144496679/Incident+Retrospectives+-+Playbook#STEP-3---Write-the-Executive-Summary)

On August 1, 2024, at 5:01 PM WET, R&amp;D was made aware of an incoming Support ticket concerning the incorrect output of a data action at runtime. Investigation concluded that there was a regression in the backend build worker, responsible for generating the applications&rsquo; server-side code, which did not reach GA but was in effect in the remaining rings until the rollback at August 2, 2024, at 2:03 PM WET.

Outputs of data actions with complex usage and structure patterns could get wrongly optimized away, that is, empty values would get returned to the client-side of applications, instead of the expected values. At the extreme, depending on the application logic, this could result in corruption of its data. 

From a technical perspective, the problem was caused by a change in how the optimizer determines whether fields will be used by the client-side at runtime. This resulted from a change to when one of its underlying data structures could get evaluated.

As a consequence of this incident:

- 
Short term: The versions of the `outsystems-backend-build-worker-service` affected by this issue were banned, preventing them from reaching GA, and were rolled back in the remaining positive rings, as a mitigation, such that customers were required to republish affected applications. 

- 
Medium term: The team has followed up with the fix, a test to cover the regression, and improvements to the resilience to similar issues of the affected code.

## Root Causes 
[Guidelines](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4144496679/Incident+Retrospectives+-+Playbook#STEP-1---Perform-the-Root-Cause-Analysis)

The optimizer is a naturally complex component of the code generation, which is made to operate on the multitude of possible patterns in applications. A recent change to its code, not meant to affect its functionality, but rather its maintainability, had unforeseen ramifications that broke a complex usage pattern of a data action. This pattern may be seen in the [test that has since been added](https://github.com/OutSystems/OutSystems.Build.Job/pull/4008/files) to cover this regression.

If the customer needs formal RCA, please fill out the following field with the document URL

[Please follow these instructions and place the RCA URL in the field below.](https://docs.google.com/document/d/13rXmBsOJh73nV2D6Z17SIBGBu2HOTWty5ddsvU000JM/edit#heading=h.bqxasxszr5q)

RCA URL

&lt;Place the URL of the customer RCA here if you have created one&gt;
## ⌛ Timeline
[View on Rootly](https://rootly.com/account/incidents/791-missmatch-between-whats-retrieved-from-data-action-from-what-s-being-displayed-in-the-browser)

**Date**

**Source**

**User**

**Event**

August 1 6:41 PM WEST

slack ([thread](https://outsystems.slack.com/archives/C0280P0R1K3/p1722534305670959?thread_ts=1722532970.532529&amp;cid=C0280P0R1K3))

David Pires &amp; Jo&atilde;o Lu&iacute;s Almeida

R&amp;D is made of aware of the incident about to be escalated, and confirms the issue is in the backend build worker

August 1 6:51 PM WEST

#alfred-channel ([src](https://outsystems.slack.com/archives/C0147J20TNY/p1722534665507379))

Jo&atilde;o Lu&iacute;s Almeida

Banned affected service versions

August 1 7:19 PM WEST

#odc_cab_approvals

Jo&atilde;o Lu&iacute;s Almeida

Opened RFC to rollback affected service

August 1  7:38 PM WEST

web

Rootly

created an alert via

August 1 7:45 PM WEST

[RDINC-27956](https://outsystemsrd.atlassian.net/browse/RDINC-27956)

Jo&atilde;o Lu&iacute;s Almeida

Hello team,

We have identified an issue in the way data action calls are optimized.

For now we have banned the affected service versions so they don't reach GA.
And we have submitted a rollback request as a mitigation. We will let you know once it comes into effect.

August 1  8:11 PM WEST

web

Rootly

Rootly created this incident

August 1  8:11 PM WEST

web

Rootly

In triage date has been set to August 1  8:11 PM WEST

August 1  8:11 PM WEST

web

Rootly

[Slack Channel](https://slack.com/app_redirect?channel=C07EYDFLMHU&amp;team=T041063TZ) has been created

August 1  8:25 PM WEST

web

Rootly

Ring: ea
System-wide impact:  
Tenant ID: dc3a3772-693b-4b6a-aa61-5fea3976eeb3
Tenant Prefix: odc-portal-localdev
Routing Error Code: OS-BLD-COMP
Product Area: -

August 1  8:25 PM WEST

web

Rootly

[PagerDuty Incident](https://outsystems.pagerduty.com/incidents/Q2AWAS0MWJKAKD) has been created.

📲 Notified Sam Audu by push notification.  (via iPhone)

August 1  8:25 PM WEST

web

Rootly

Sam Audu has been assigned as Engineer

August 1  8:25 PM WEST

web

Rootly

Sam Audu acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q2AWAS0MWJKAKD). (via Mobile)

August 1  8:26 PM WEST

web

Sam Audu

Incident has been started

August 1  8:26 PM WEST

web

Rootly

Pagerduty Integrations acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q2AWAS0MWJKAKD). (via Mobile)

August 1  8:36 PM WEST

web

Sam Audu

Jo&atilde;o Lu&iacute;s Almeida has been assigned as Subject Matter Expert

August 2 11:07PM WEST

github

Jo&atilde;o Lu&iacute;s Almeida

Fix [8e375f553](https://github.com/OutSystems/OutSystems.Build.Job/commit/8e375f553cfa010866f2a84b66b47ec43ab0e385) was identified and merged.

August 2 12:08PM WEST

slack

Miguel Rebelo

RFC approved after internal alignment between the teams affected by the service rollback

August 2 1:41PM WEST

slack

Leandro Galrinho

Rollbacks executed

August 2  2:03 PM WEST

web

Jo&atilde;o Lu&iacute;s Almeida

Send ZenDesk private comment has been set: Hello team,The affected service has been rolled back in the positive rings (OSRD, OSALL, and EA - the issue did not reach GA).Customers will need to republish the affected applications.Best regards and our apologies for the inconvenience,
Jo&atilde;o Lu&iacute;s Almeida

August 2 2:13 PM WEST

slack

Ant&oacute;nio Rodrigues

Confirmation from affected R&amp;D teams that the issue has been resolved ([src](https://outsystems.slack.com/archives/C01056JA3N3/p1722604386113989?thread_ts=1722528082.587209&amp;cid=C01056JA3N3))

August 2  2:42 PM WEST

web

Nuno Bento

Teams has been added: [BuildServices](/account/teams/buildservices/status)

August 2  7:46 PM WEST

web

Rootly

Sam Audu marked the incident as resolved through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q2AWAS0MWJKAKD). (via Website)

August 5 10:02 AM WEST

web

Rootly

The Global Support team marked this incident as closed in ZenDesk.

August 5 10:02 AM WEST

web

Rootly

Incident has been resolved

August 5 10:02 AM WEST

web

Rootly

ZenDesk Event Type has been set: solved

August 5  2:21 PM WEST

slack

Sam Audu

Archived the Slack channel
## 📝 Follow Up Items
In the scope of the bug fix, RBST-2404ef8955cb-cb21-32a7-b692-01ace42388d6System Jira, besides adding a test to cover the regression, the team also [worked on improving](https://github.com/OutSystems/OutSystems.Build.Job/pull/3992) the resilience of the affected code to similar issues.

The team also followed up (in [this thread](https://outsystems.slack.com/archives/C063JU0M6AH/p1722598338556749) on #change_management_ama) to understand if it&rsquo;d have been possible to apply the rollback through an emergency RFC, despite it being a SEV-2. And learned that rolling back a service to its previous version is considered a standard change.