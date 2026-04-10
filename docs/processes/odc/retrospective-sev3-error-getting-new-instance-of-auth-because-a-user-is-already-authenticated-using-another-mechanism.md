---
title: Retrospective-SEV3-Error getting new instance of auth because a user is already authenticated using another mechanism
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4389208401/Retrospective-SEV3-Error+getting+new+instance+of+auth+because+a+user+is+already+authenticated+using+another+mechanism
confluence_space: RKB
confluence_page_id: 4389208401
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV3-Error getting new instance of auth because a user is already authenticated using another mechanism

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV3

Teams:&nbsp;trueBlueIdentity Core
#### 🕐 Timestamps
Started At:&nbsp;trueBlueJuly 16 11:53 AM WEST

Mitigated At:&nbsp;trueYellowAugust 8 12:07 PM WEST

Resolved At:&nbsp;trueGreenAugust 8 12:07 PM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/710-error-getting-new-instance-of-auth-because-a-user-is-already-authenticated-using-another-mechanism)
[Pagerduty incident](https://outsystems.pagerduty.com/incidents/Q3FQ0U7YMVC38K)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3030712)

#### Summary
----------------------------------------------**ISSUE DESCRIPTION AND HOW TO REPRODUCE**- What is the issue the customer is describing/experiencing?- An end-user is unable to access the applications in Production. due to &quot;error getting new instance of auth because a user is already authenticated using another mechanism&quot;
- Specify which application(s) / database/front-end is affected (high-level use case)- All apps in production.
- When was the issue first observed? Was there any action/change on that feature?- Since at least May (#3010137)
- How often is the issue observed?- Persistently.Only 1 user can replicate, however, we will elaborate on the troubleshooting section.**IMPACT ON THE CUSTOMER**
Normal, temporary since user is on vacations however user is a developer and tester**TROUBLESHOOTING STEPS &amp; WORKAROUND**
Basically the affected user Thomas, IT manager cannot access any of our applications, it was a user register via portal who has ever used the built-in provider,
As a workaround we suggest delete the user, and recreated on login, but did not took effect.- Affected user Thomas Machtenlinckx -&gt; 0306cbbc-9a20-4808-be7e-fa02740d9ae0 (new user id after recreation)
- In the past we saw similar errors where:- https://supportoutsystems.zendesk.com/agent/tickets/2820222 -&gt; RDINC-9329-&gt; in this case was a bug due to built in also be activated with External IDP, disabling built in fix the issue, however, in this case customer has already disable:- ![](https://supportoutsystems.zendesk.com/attachments/token/0YSAEOXwK64MPiitP2rEGjBOZ/?name=image.png)
- https://supportoutsystems.zendesk.com/agent/tickets/3010137- Same situation as previously JIRA
- In this customer case, app was published on July 11 and stage also on that day, so the issue shouldn't be the same:- ![](https://supportoutsystems.zendesk.com/attachments/token/lFSfJMw8LgqLDIZpbsSriXHHZ/?name=image.png)
- On the logs after the error we are seeing a failing to get some endpoints with status 499:- ![](https://supportoutsystems.zendesk.com/attachments/token/3ZW8ZZXy93AXku8xffusrOqGf/?name=image.png)- ![](https://supportoutsystems.zendesk.com/attachments/token/jtRXgOoujY26Uu77YXYhPWYYc/?name=image.png)
- On another time frame, same situation:- ![](https://supportoutsystems.zendesk.com/attachments/token/J1haPeHmWmyQc5It3Z2Xk2Nr9/?name=image.png)- in theory 499 status means that the client/user closed the connection before the server answered the request to always a specific endpoint:- https://vgd-odc-dev.outsystems.app/VGDAppRelations/moduleservices/users/userinfosyncLooking at CF level:- nothing:- https://outsystems.grafana.net/d/6-6x5IF4k/cloudfront-logs?orgId=1&amp;var-environment=prod&amp;var-data_source=MWYvlds7z&amp;var-host=&amp;var-method=All&amp;var-status_code=All&amp;var-edge_response_type=All&amp;var-search=VGDAppRelations%2Fmoduleservices%2Fusers%2Fuserinfosync&amp;var-plat_s3=s3%2Flogs-plat-edge-ue1-prod-rn-cloudrd-os&amp;var-run_s3=s3%2Flogs-run-edge-ue1-prod-rn-cloudrd-os&amp;var-cus_s3=s3%2Flogs-cus-edge-ue1-prod-rn-cloudrd-os&amp;from=1720090793000&amp;to=1720090919000
In the HAR file we can only see the endpoint being used on a variable assignment but never called.- ![](https://supportoutsystems.zendesk.com/attachments/token/76PUx5v7PFzE7tR6JcRJ0gQnC/?name=image.png)On identity side also didn't detect nothing:
https://outsystems.grafana.net/d/cdh4sw1jvc8aof/identity-logs?orgId=1&amp;var-rings=ga&amp;var-regionShort=All&amp;var-severity=Error&amp;var-severity=Warning&amp;var-severity=Information&amp;var-severity=Debug&amp;var-search=f904a224-560a-4cd6-a4ac-31306816508c&amp;from=1720090785000&amp;to=1720090820000**Customer also shared a video and har file:**- Recording 2024-07-02 163141.mp4
- They are starting off in a different site- ![](https://supportoutsystems.zendesk.com/attachments/token/KACc9NgWScMJLBbnQp6JiPvlK/?name=image.png)- And then, they click one of the buttons, which goes to the ODC app - VGDAppRelations- ![](https://supportoutsystems.zendesk.com/attachments/token/R9dhcCjcxxJuI44Kl3LNikZEf/?name=image.png)- And over here, they get the error- ![](https://supportoutsystems.zendesk.com/attachments/token/yyAOA5fMuVaiRaRE5oIxbGb60/?name=image.png)- vgd-odc.outsystems.app.harWe would like to start reaching back end since our investigation shows some suspicious on the 499 HTTP status and trace, and understand why in a universe of 250 external users with same configs this was is the only affected.**TECH DATA OR ANY OTHER RELEVANT INFO**
Ring: ga
Tenant Id: 7d7e6e65-4fe3-46a0-a5ab-239b7971ad60
Tenant Prefix: vgd-odc
Region: eu-central-1
O7X.7WR.GEU.7YB.OZR.PME.VET.AUT_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 RetrospectiveinfoDetails
**Ring:** ga
**System-wide impact:**&nbsp; 
**Tenant ID:** 7d7e6e65-4fe3-46a0-a5ab-239b7971ad60
**Tenant Prefix:** vgd-odc
**Routing Error Code:** N/A
**Product Area:** Phoenix::Application Runtime::Logic Flows::Server Actions
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/710-error-getting-new-instance-of-auth-because-a-user-is-already-authenticated-using-another-mechanism)

**Date**

**Source**

**User**

**Event**
July 16 10:41 AM WESTwebRootly
created an alert via
July 16 10:41 AM WESTwebRootly
Rootly created this incident
July 16 10:41 AM WESTwebRootly
In triage date has been set to July 16 10:41 AM WEST
July 16 10:51 AM WESTwebRootly
This incident was instantiated in Jira: RDINC-9329. Please work the incident using Rootly
July 16 11:31 AM WESTwebRui Garcia
Handing this over to Client Runtime team, because Backend Runtime takes no part in the Logic flow.
The error in endpoint userinfosync is a consequence of the previous failure.
July 16 11:33 AM WESTwebRui Garcia
Teams has been added: Client Runtime
July 16 11:33 AM WESTwebRui Garcia
Teams has been removed: Backend Runtime
July 16 11:41 AM WESTwebRootly
This incident was instantiated in Jira: RDINC-27208. Please work the incident using Rootly
July 16 11:53 AM WESTwebDavid Pires
Incident has been started
July 16 11:54 AM WESTwebDavid PiresDavid Pires has been assigned as EngineerJuly 16 12:06 PM WESTwebDavid PiresSend ZenDesk private comment has been set: Hey team,  
Reading the logs, the error happens because the user is trying to login with the wrong idp. This can happen if there's an error in customer logic or if there's some misconfigured browser cache. Since this only happens to one user, looks like a problem on his session. Can you ask the user to try to login using an anonymous session?July 16 12:06 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hey team,  
Reading the logs, the error happens because the user is trying to login with the wrong idp. This can happen if there's an error in customer logic or if there's some misconfigured browser cache. Since this only happens to one user, looks like a problem on his session. Can you ask the user to try to login using an anonymous session?
July 16 12:06 PM WESTwebRootlySend ZenDesk private comment has been unsetJuly 16 12:06 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

July 16 12:08 PM WESTwebDavid PiresSwarm has been set: Identity CoreJuly 16 12:08 PM WESTwebRootly[PagerDuty Incident](https://outsystems.pagerduty.com/incidents/Q3FQ0U7YMVC38K) has been created.
📲 Notified Rodrigo Bernardo by push notification.  (via iPhone)&nbsp;&nbsp;📧 Notified Rodrigo Bernardo by email.&nbsp;&nbsp;📲 Notified Rodrigo Bernardo by push notification.  (via iPhone)&nbsp;&nbsp;📲 Notified Rodrigo Bernardo by push notification.  (via iPhone)July 16 12:08 PM WESTwebRootly
Rodrigo Bernardo acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q3FQ0U7YMVC38K). (via Slack)
July 16  3:34 PM WESTwebDavid Pires
Teams has been removed: Client Runtime
July 16  3:35 PM WESTwebDavid Pires
David Pires has been unassigned from Engineer
July 29 10:22 AM WESTwebJorge MarinSend ZenDesk private comment has been set: From David Pires:  
Reading the logs, the error happens because the user is trying to login with the wrong idp. This can happen if there's an error in customer logic or if there's some misconfigured browser cache. Since this only happens to one user, looks like a problem on his session. Can you ask the user to try to login using an anonymous session?July 29 10:22 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
From David Pires:  
Reading the logs, the error happens because the user is trying to login with the wrong idp. This can happen if there's an error in customer logic or if there's some misconfigured browser cache. Since this only happens to one user, looks like a problem on his session. Can you ask the user to try to login using an anonymous session?
July 29 10:22 AM WESTwebRootlySend ZenDesk private comment has been unsetJuly 29 10:22 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

August 8 12:07 PM WESTwebRootly
The Global Support team marked this incident as closed in ZenDesk.
August 8 12:07 PM WESTwebRootly
Incident has been resolved
August 8 12:07 PM WESTwebRootlyZenDesk Event Type has been set: solvedAugust 27  7:04 PM WESTwebRootly
The Global Support team marked this incident as closed in ZenDesk.