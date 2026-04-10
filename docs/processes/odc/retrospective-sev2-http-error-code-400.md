---
title: Retrospective-SEV2-Http Error Code : 400
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4279042077/Retrospective-SEV2-Http+Error+Code+400
confluence_space: RKB
confluence_page_id: 4279042077
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV2-Http Error Code : 400

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV2

Teams:&nbsp;trueBlueIde Group&nbsp;trueBlueNeo Platform Theseus
#### 🕐 Timestamps
Started At:&nbsp;trueBlueJuly 9  8:48 PM WEST

Mitigated At:&nbsp;trueYellowJuly 11  9:38 AM WEST

Resolved At:&nbsp;trueGreenJuly 11  9:38 AM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/691-http-error-code-400)
[Pagerduty incident](https://outsystems.pagerduty.com/incidents/Q2I23IWLVQ7W6Q)

[Slack channel](https://slack.com/app_redirect?channel=C07BLQMEAUV&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3033459)

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

Jo&atilde;o Mano
#### Summary
----------------------------------------------**ISSUE DESCRIPTION AND HOW TO REPRODUCE**- The customer's development team is encountering an HTTP 400 error (&quot;One or more validation errors occurred&quot;) when attempting to publish the application. The issue appears inconsistent, with some team members able to publish temporarily before all members faced the error again. The error specifics include: &quot;HTTP Error Code: 400- Bad Request. Title: One or more validation errors occurred. Error Code: Detail: TraceId: 00-0cff2d3645856b28ff00f3a42b09511c-66f8baa8a21f55aa-01.&quot;**IMPACT ON THE CUSTOMER**- The team is **currently** blocked from publishing the application.
- Deadline due to an upcoming Show &amp; Tell with the customer by the end of next week.
- Significant delays in development.**TROUBLESHOOTING STEPS &amp; WORKAROUND**- The customer has provided a failing and one that worked OMLs and also the diagnostic report and we can see some 404 in the GET method when searching the trace- https://outsystems.grafana.net/explore?schemaVersion=1&amp;panes=%7B%22wim%22:%7B%22datasource%22:%22grafanacloud-outsystemstest-traces%22,%22queries%22:%5B%7B%22refId%22:%22A%22,%22datasource%22:%7B%22type%22:%22tempo%22,%22uid%22:%22grafanacloud-outsystemstest-traces%22%7D,%22queryType%22:%22traceql%22,%22limit%22:20,%22tableType%22:%22traces%22,%22query%22:%22e6441ad3dbfad85b961c03281d2039d7%22%7D%5D,%22range%22:%7B%22from%22:%22now-12h%22,%22to%22:%22now%22%7D%7D%7D&amp;orgId=1- ![](https://supportoutsystems.zendesk.com/attachments/token/qnLOx1izKYGyHc1K1tqWQ4mzD/?name=image.png)
- They have already tried different networks and such, but nothing tried from their side seems to solve the issue.**TECH DATA OR ANY OTHER RELEVANT INFO**
Ring: ga
Tenant Id: 7f2219da-7e8d-46ce-8256-798bc11eec50
Tenant Prefix: eurospin
Region: eu-central-1
5V0.67P.KYP.WC8.FPJ.1L5.YKQ.05XOMLs and diagnostic reports will be attached_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_Attachment(s):
Dignostic report.txt - https://supportoutsystems.zendesk.com/attachments/token/N6SJdsQJRCGLzHoWW5JoxSKWD/?name=Dignostic+report.txt
## 📝 RetrospectiveinfoDetails
**Ring:** ga
**System-wide impact:**&nbsp; 
**Tenant ID:** 7f2219da-7e8d-46ce-8256-798bc11eec50
**Tenant Prefix:** eurospin
**Routing Error Code:** N/A
**Product Area:** Phoenix::Service Studio::Publish
### Impact:
Customer was unable to publish the app in its current state.
### Investigation and troubleshooting findings:
Customer's contained multiple large excel files making the OML larger than the 100MB limit on AVS, thus not allowing them to publish it.
### Resolution:
Customer needs to refactor the app according to best practices as having that many large files inside the app is not recommended.
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/691-http-error-code-400)

**Date**

**Source**

**User**

**Event**
July 9  7:30 PM WESTwebRootly
created an alert via
July 9  7:30 PM WESTwebRootly
Rootly created this incident
July 9  7:30 PM WESTwebRootly
In triage date has been set to July 9  7:30 PM WEST
July 9  7:30 PM WESTwebRootly[Slack Channel](https://slack.com/app_redirect?channel=C07BLQMEAUV&amp;team=T041063TZ) has been createdJuly 9  7:30 PM WESTwebRootly
Ring: ga
System-wide impact:  
Tenant ID: 7f2219da-7e8d-46ce-8256-798bc11eec50
Tenant Prefix: eurospin
Routing Error Code: N/A
Product Area: Phoenix::Service Studio::Publish
July 9  7:30 PM WESTwebRootly[PagerDuty Incident](https://outsystems.pagerduty.com/incidents/Q2I23IWLVQ7W6Q) has been created.
📧 Notified Jo&atilde;o Mano by email.&nbsp;&nbsp;📲 Notified Jo&atilde;o Mano by push notification.  (via iPhone)&nbsp;&nbsp;📲 Notified Jo&atilde;o Mano by push notification.  (via iPhone)July 9  7:30 PM WESTwebRootlyJo&atilde;o Mano has been assigned as EngineerJuly 9  7:32 PM WESTwebRootly
Jo&atilde;o Mano acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q2I23IWLVQ7W6Q). (via Mobile)
July 9  7:53 PM WESTwebJo&atilde;o ManoSend ZenDesk private comment has been set: Hello support team,
&nbsp;&nbsp;
Would it be possible to obtain the OML? From our logs it seems that we're getting a &quot;Failed to read the request form. Request body too large. The max request body size is 104857600 bytes.&quot; which indicates that the OML might be too big? I'm not currently aware of this size limitation or if this is currently documented/expected.
&nbsp;&nbsp;
Does this OML contain a lot of binary files? An OML of this size (100Mb +) is not very common from my knowledge.
&nbsp;&nbsp;
Nevertheless, this limit comes from the Application Versioning Service and it doesn't seem that there's anything we can do on the IDE side.
&nbsp;&nbsp;
As such, my recommendation is to move the issue to the Theseus team. I'll add the team and communicate with them.July 9  7:53 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

Hello support team,
&nbsp;&nbsp;
Would it be possible to obtain the OML? From our logs it seems that we're getting a &quot;Failed to read the request form. Request body too large. The max request body size is 104857600 bytes.&quot; which indicates that the OML might be too big? I'm not currently aware of this size limitation or if this is currently documented/expected.
&nbsp;&nbsp;
Does this OML contain a lot of binary files? An OML of this size (100Mb +) is not very common from my knowledge.
&nbsp;&nbsp;
Nevertheless, this limit comes from the Application Versioning Service and it doesn't seem that there's anything we can do on the IDE side.
&nbsp;&nbsp;
As such, my recommendation is to move the issue to the Theseus team. I'll add the team and communicate with them.July 9  7:53 PM WESTwebRootlySend ZenDesk private comment has been unsetJuly 9  7:53 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

July 9  7:55 PM WESTwebJo&atilde;o ManoSwarm has been set: TheseusJuly 9  7:55 PM WESTwebRootly
Pagerduty Integrations added Guilherme Alexandre Rolo as responder in [PagerDuty](https://outsystems.pagerduty.com/incidents/Q2I23IWLVQ7W6Q)
July 9  7:59 PM WESTwebRootly
Guilherme Alexandre Rolo joined this [PagerDuty](https://outsystems.pagerduty.com/incidents/Q2I23IWLVQ7W6Q) incident.
July 9  8:45 PM WESTwebJo&atilde;o ManoSend ZenDesk private comment has been set: Hello again team,
&nbsp;&nbsp;
Apologies for not noticing the OMLs in the JIRA issue.
I have confirmed that the OML indeed has more than 100mb and that is the limit that AVS accepts for the size of the OML.
&nbsp;&nbsp;
We have noticed that the OML contains a bunch of very big files (for example, a 45mb xlsx file, another 14mb xlsx file). Of course, having this many big files is&nbsp;**not recommended** and the customer should refactor the app in able to proceed with the developments.
&nbsp;&nbsp;
Thanks for the help,
Jo&atilde;o Mano.July 9  8:45 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

Hello again team,
&nbsp;&nbsp;
Apologies for not noticing the OMLs in the JIRA issue.
I have confirmed that the OML indeed has more than 100mb and that is the limit that AVS accepts for the size of the OML.
&nbsp;&nbsp;
We have noticed that the OML contains a bunch of very big files (for example, a 45mb xlsx file, another 14mb xlsx file). Of course, having this many big files is&nbsp;**not recommended** and the customer should refactor the app in able to proceed with the developments.
&nbsp;&nbsp;
Thanks for the help,
Jo&atilde;o Mano.July 9  8:45 PM WESTwebRootlySend ZenDesk private comment has been unsetJuly 9  8:45 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

July 9  8:48 PM WESTwebJo&atilde;o Mano
Incident has been started
July 9  8:48 PM WESTwebRootly
Pagerduty Integrations acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q2I23IWLVQ7W6Q). (via Mobile)
July 10  5:02 PM WESTwebRootlyZenDesk Event Type has been set: solvedJuly 10  5:02 PM WESTwebRootly
The Global Support team marked this incident as closed in ZenDesk.
July 11  9:35 AM WESTwebRootly
Jo&atilde;o Mano marked the incident as resolved through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q2I23IWLVQ7W6Q). (via Website)
July 11  9:38 AM WESTwebJo&atilde;o Mano
Incident has been resolved
July 11  9:38 AM WESTwebJo&atilde;o ManoImpact has been set: Customer was unable to publish the app in its current state.July 11  9:38 AM WESTwebJo&atilde;o ManoInvestigation and troubleshooting findings has been set: Customer's contained multiple large excel files making the OML larger than the 100MB limit on AVS, thus not allowing them to publish it.July 11  9:38 AM WESTwebJo&atilde;o ManoResolution has been set: Customer needs to refactor the app according to best practices as having that many large files inside the app is not recommended.