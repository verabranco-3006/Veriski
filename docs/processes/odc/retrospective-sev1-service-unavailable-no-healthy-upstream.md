---
title: Retrospective-SEV1-Service Unavailable no healthy upstream
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4374528203/Retrospective-SEV1-Service+Unavailable+no+healthy+upstream
confluence_space: RKB
confluence_page_id: 4374528203
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV1-Service Unavailable no healthy upstream

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV1

Teams:&nbsp;trueBlueData Fabric Engine
#### 🕐 Timestamps
Started At:&nbsp;trueBlueJuly 29 11:20 AM WEST

Mitigated At:&nbsp;trueYellowJuly 29  4:05 PM WEST

Resolved At:&nbsp;trueGreenAugust 21 12:10 PM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/769-service-unavailable-no-healthy-upstream)
[Pagerduty incident](https://outsystems.pagerduty.com/incidents/Q2PGW0XA7EHMGB)

[Slack channel](https://slack.com/app_redirect?channel=C07E1Q20V2T&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3041981)

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

Vera Cardoso
#### Summary
----------------------------------------------**ISSUE DESCRIPTION AND HOW TO REPRODUCE**- External connections started failing in Production with `HTTP 503: Service Unavailable no healthy upstream`![](https://supportoutsystems.zendesk.com/attachments/token/3rya2qEeFQbQVmH85f37iVTl0/?name=image.png)
- Affecting both runtime apps when accessing screens that query external connections, and also when trying to edit the connection (entities) in ODC Portal:![](https://supportoutsystems.zendesk.com/attachments/token/pWM9GrqprS3ztgd3nqh6h72Hh/?name=image.png)**IMPACT ON THE CUSTOMER**- Production; ongoing, blocks from using apps.**TROUBLESHOOTING STEPS &amp; WORKAROUND**- Looking at the Query Engine dashboard for their Production stage, we can definitely see lots of weird stuff:![](https://supportoutsystems.zendesk.com/attachments/token/Ey3sEJ0bIrnmebjWDLLf59KYQ/?name=image.png)![](https://supportoutsystems.zendesk.com/attachments/token/nFkUJwlyIOLeWOSh3ouTCBloU/?name=image.png)![](https://supportoutsystems.zendesk.com/attachments/token/l7hntG1RHXXGP8vfQszv4Vt7A/?name=image.png)
- This matches when the 503 errors started:![](https://supportoutsystems.zendesk.com/attachments/token/2fHIL1rbXTx1uTUBx2K3CuIqn/?name=image.png)
- Considering the urgency and after confirming that indeed the Query Engine pods seem to be down for this environment, we decided to quickly escalate for assistance.**TECH DATA OR ANY OTHER RELEVANT INFO**
Ring: ga
Tenant Id: ec0d5d97-275d-429b-866f-d873ace203d3
Tenant Prefix: lingnan
Region: ap-southeast-1
Environment (Production): 90f69c30-2f17-449a-9790-a3ea6c3f195e_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 RetrospectiveinfoDetails
**Ring:** ga
**System-wide impact:**&nbsp; 
**Tenant ID:** ec0d5d97-275d-429b-866f-d873ace203d3
**Tenant Prefix:** lingnan
**Routing Error Code:** N/A
**Product Area:** Phoenix::Application Runtime::Database access::External entities
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/769-service-unavailable-no-healthy-upstream)

**Date**

**Source**

**User**

**Event**
July 29 10:32 AM WESTwebRootly
created an alert via
July 29 10:32 AM WESTwebRootly
Rootly created this incident
July 29 10:32 AM WESTwebRootly
In triage date has been set to July 29 10:32 AM WEST
July 29 10:33 AM WESTwebRootly[Slack Channel](https://slack.com/app_redirect?channel=C07E1Q20V2T&amp;team=T041063TZ) has been createdJuly 29 10:33 AM WESTwebRootly
Ring: ga
System-wide impact:  
Tenant ID: ec0d5d97-275d-429b-866f-d873ace203d3
Tenant Prefix: lingnan
Routing Error Code: N/A
Product Area: Phoenix::Application Runtime::Database access::External entities
July 29 10:33 AM WESTwebRootly[PagerDuty Incident](https://outsystems.pagerduty.com/incidents/Q2PGW0XA7EHMGB) has been created.
📞 Notified Vera Cardoso by phone.July 29 10:33 AM WESTwebRootlyVera Cardoso has been assigned as EngineerJuly 29 10:33 AM WESTwebRootly
Vera Cardoso acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q2PGW0XA7EHMGB). (via Phone)
July 29 10:40 AM WESTwebRootly
Vasco Gomes marked the incident as resolved through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q2PGW0XA7EHMGB). (via Website)
July 29 11:20 AM WESTwebVasco Gomes
Incident has been started
July 29 12:37 PM WESTwebVasco Gomes
At 05:21 AM UTC all 3 stages of the Lingna client went down. At 05:35 UTC the Dev Environment recovered and at 05:40 AM UTC the PRD environment recovered, but Test Environment remained down. 
[Probes.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDE5MzcxLCJwdXIiOiJibG9iX2lkIn19--53d0509d8369a16e684e523d031abc590222eea3/Probes.png)July 29 12:55 PM WESTwebVasco GomesSend ZenDesk private comment has been set: We are actively monitoring the environments of this client and troubleshooting possible workarounds to solve the problem and we noticed that the PRD Pod was able to start up&nbsp; :  ![probes%20up.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDE5Mzc4LCJwdXIiOiJibG9iX2lkIn19--2b80bc497933c5bec50148c0ca6a1134e41aa140/probes%20up.png)probes up.png 71.4 KBWe believe at this moment that the problem was introduced to a database connection problem but we are still looking into it, since the DEV and Test environments are still down.July 29 12:55 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
We are actively monitoring the environments of this client and troubleshooting possible workarounds to solve the problem and we noticed that the PRD Pod was able to start up&nbsp; :  ![probes%20up.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDE5Mzc4LCJwdXIiOiJibG9iX2lkIn19--2b80bc497933c5bec50148c0ca6a1134e41aa140/probes%20up.png)probes up.png 71.4 KBWe believe at this moment that the problem was introduced to a database connection problem but we are still looking into it, since the DEV and Test environments are still down.
July 29 12:55 PM WESTwebRootlySend ZenDesk private comment has been unsetJuly 29 12:55 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

July 29  1:03 PM WESTwebVasco GomesSend ZenDesk private comment has been set: We've confirmed that the PRD Environment is currently up, we are seeing [Traces](https://outsystems.grafana.net/d/B8fujKKVz/query-engine?var-ring=ga&amp;var-container=outsystems-queryengine-service&amp;var-environment=90f69c30-2f17-449a-9790-a3ea6c3f195e&amp;from=now-6h&amp;to=now&amp;refresh=30s&amp;viewPanel=panel-84) succesfully :![Screenshot%202024-07-29%20at%2013.02.31.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDE5MzgyLCJwdXIiOiJibG9iX2lkIn19--34833cb4bd4c93ac20719f745c52465c5252f8c9/Screenshot%202024-07-29%20at%2013.02.31.png)Screenshot 2024-07-29 at 13.02.31.png 125.29 KBJuly 29  1:03 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
We've confirmed that the PRD Environment is currently up, we are seeing [Traces](https://outsystems.grafana.net/d/B8fujKKVz/query-engine?var-ring=ga&amp;var-container=outsystems-queryengine-service&amp;var-environment=90f69c30-2f17-449a-9790-a3ea6c3f195e&amp;from=now-6h&amp;to=now&amp;refresh=30s&amp;viewPanel=panel-84) succesfully :![Screenshot%202024-07-29%20at%2013.02.31.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDE5MzgyLCJwdXIiOiJibG9iX2lkIn19--34833cb4bd4c93ac20719f745c52465c5252f8c9/Screenshot%202024-07-29%20at%2013.02.31.png)Screenshot 2024-07-29 at 13.02.31.png 125.29 KB
July 29  1:03 PM WESTwebRootlySend ZenDesk private comment has been unsetJuly 29  1:03 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

July 29  1:37 PM WESTwebRootlyZendesk Private Comment has been set: ----------------------------------------------**Update to R&amp;D**
Hi team,They created a connection this morning to troubleshoot another support incident, and already have removed it, thus confirming your observations on the Production.They've confirmed the runtime errors in Production are resolved, so we believe we can go ahead and lower the severity of this.However, it seems there is a problem with another of the connections? `a5ad0b3b-66aa-4abe-b1ec-dbf153abd1b7`- I assumed that because for both stages we can see this message until the Avatica server is eventually stopped:![](https://supportoutsystems.zendesk.com/attachments/token/swtvmQz65ywCRnTGYxSZbRSaC/?name=image.png)
- However, in Production, we can see there was instead an error for that same connection just prior to the Query Engine finishing startup successfully:![](https://supportoutsystems.zendesk.com/attachments/token/WEeQvsKxwgakPyFn5xxl2LaAU/?name=image.png)Finally, they cannot confirm exactly which tables they are fetching from the connection (in order to test the metadata query) since they cannot open the entities from that connection in ODC Portal:![](https://supportoutsystems.zendesk.com/attachments/token/DQbYuraCJwDJYvAqyQdLBwDjq/?name=image.png)Any thoughts on this?In the meantime, I will also ask them about this other connection to see if it's also needed or not.Thank you again!Jo&atilde;o Neves__July 29  1:37 PM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
Hi team,They created a connection this morning to troubleshoot another support incident, and already have removed it, thus confirming your observations on the Production.They've confirmed the runtime errors in Production are resolved, so we believe we can go ahead and lower the severity of this.However, it seems there is a problem with another of the connections? `a5ad0b3b-66aa-4abe-b1ec-dbf153abd1b7`- I assumed that because for both stages we can see this message until the Avatica server is eventually stopped:![](https://supportoutsystems.zendesk.com/attachments/token/swtvmQz65ywCRnTGYxSZbRSaC/?name=image.png)
- However, in Production, we can see there was instead an error for that same connection just prior to the Query Engine finishing startup successfully:![](https://supportoutsystems.zendesk.com/attachments/token/WEeQvsKxwgakPyFn5xxl2LaAU/?name=image.png)Finally, they cannot confirm exactly which tables they are fetching from the connection (in order to test the metadata query) since they cannot open the entities from that connection in ODC Portal:![](https://supportoutsystems.zendesk.com/attachments/token/DQbYuraCJwDJYvAqyQdLBwDjq/?name=image.png)Any thoughts on this?In the meantime, I will also ask them about this other connection to see if it's also needed or not.Thank you again!Jo&atilde;o Neves__
July 29  1:47 PM WESTwebRootlyZendesk Private Comment has been changed to: ----------------------------------------------**Update to R&amp;D**
Hi again team,After looking into their other incident, we noticed that the recently created connection (the one that was already removed) was a duplicate of an already existing connection, which they created to attempt to troubleshoot the error that you can see on the screenshot from my previous update:An error occurred while refreshing the entity list. The entity list you are seeing was last updated on '2024-07-22 17:01:20'. You may try to refresh the list again. If this error persists, verify that your connection configuration is still valid.This error occurs when they try to refresh the connection entities. They have tried to refresh the entities because they started getting runtime errors from some of their apps.After testing the connection on ODC Portal, even without a password, we can see that the test times out for both Development and QA - which probably not by coincidence matches the stages that are still not working.I will check back with them to confirm whether the configured connection is still valid, as per the error's suggestion.Will let you know of any updates._&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_July 29  1:47 PM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
Hi again team,After looking into their other incident, we noticed that the recently created connection (the one that was already removed) was a duplicate of an already existing connection, which they created to attempt to troubleshoot the error that you can see on the screenshot from my previous update:An error occurred while refreshing the entity list. The entity list you are seeing was last updated on '2024-07-22 17:01:20'. You may try to refresh the list again. If this error persists, verify that your connection configuration is still valid.This error occurs when they try to refresh the connection entities. They have tried to refresh the entities because they started getting runtime errors from some of their apps.After testing the connection on ODC Portal, even without a password, we can see that the test times out for both Development and QA - which probably not by coincidence matches the stages that are still not working.I will check back with them to confirm whether the configured connection is still valid, as per the error's suggestion.Will let you know of any updates.__
July 29  2:18 PM WESTwebVasco GomesSend ZenDesk private comment has been set: Hello team! We've noticed that Dev Environment just got up again. They've must have removed that connection from Dev environment :![Screenshot%202024-07-29%20at%2014.17.36.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDE5NDY1LCJwdXIiOiJibG9iX2lkIn19--3214beb7547b5012938a2077c08a5a41337412b2/Screenshot%202024-07-29%20at%2014.17.36.png)Screenshot 2024-07-29 at 14.17.36.png 80.42 KBYou can see that [here](https://outsystems.grafana.net/d/B8fujKKVz/query-engine?var-ring=ga&amp;var-container=outsystems-queryengine-service&amp;var-environment=f0075236-c771-43f2-9f52-deec51fe96e5&amp;from=now-1h&amp;to=now&amp;refresh=30s&amp;viewPanel=panel-32).July 29  2:18 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hello team! We've noticed that Dev Environment just got up again. They've must have removed that connection from Dev environment :![Screenshot%202024-07-29%20at%2014.17.36.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDE5NDY1LCJwdXIiOiJibG9iX2lkIn19--3214beb7547b5012938a2077c08a5a41337412b2/Screenshot%202024-07-29%20at%2014.17.36.png)Screenshot 2024-07-29 at 14.17.36.png 80.42 KBYou can see that [here](https://outsystems.grafana.net/d/B8fujKKVz/query-engine?var-ring=ga&amp;var-container=outsystems-queryengine-service&amp;var-environment=f0075236-c771-43f2-9f52-deec51fe96e5&amp;from=now-1h&amp;to=now&amp;refresh=30s&amp;viewPanel=panel-32).
July 29  2:18 PM WESTwebRootlySend ZenDesk private comment has been unsetJuly 29  2:18 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

July 29  2:32 PM WESTwebVasco GomesSend ZenDesk private comment has been set: We have also noticed that there is a connection &quot;a5ad0b3b-66aa-4abe-b1ec-dbf153abd1b7&quot; that is present in all 3 environments and that is in a NOK state. Is the client aware of that? Can they edit a solve the connection problem?&nbsp;  
(By the errors thrown it appears to be a problem in the database side, but if the connection is not in an OK State it is good practice to be removed by the client).&nbsp;  
We don't know if this connection is similar to the other one, since the only thing that we have is the connection ID.&nbsp;  
I believe it makes sense for the client to fix the state of this connection or to remove it altogether.July 29  2:33 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
We have also noticed that there is a connection &quot;a5ad0b3b-66aa-4abe-b1ec-dbf153abd1b7&quot; that is present in all 3 environments and that is in a NOK state. Is the client aware of that? Can they edit a solve the connection problem?&nbsp;  
(By the errors thrown it appears to be a problem in the database side, but if the connection is not in an OK State it is good practice to be removed by the client).&nbsp;  
We don't know if this connection is similar to the other one, since the only thing that we have is the connection ID.&nbsp;  
I believe it makes sense for the client to fix the state of this connection or to remove it altogether.
July 29  2:33 PM WESTwebRootlySend ZenDesk private comment has been unsetJuly 29  2:33 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

July 29  3:49 PM WESTwebRootlyZendesk Private Comment has been changed to: ----------------------------------------------**Update to R&amp;D**
Hi again team,So apparently they restarted the Cloud Connector and they claim it restored both connections (Dev and QA), but now QA is not working anymore again (still times out testing connection, still same errors).- We can confirm this in the logs for QA stage:![](https://supportoutsystems.zendesk.com/attachments/token/AFC7PwlvuFZWRXowmNcAU4qLG/?name=image.png)We can also say that QA has the same connection details as Development.They also have another two connections in which the same settings are all the same except for the used schema - for both these other connections it also fails just for QA.![](https://supportoutsystems.zendesk.com/attachments/token/dKGsNY1SQDlOUvUDX1jas3s8T/?name=image.png)![](https://supportoutsystems.zendesk.com/attachments/token/he9mTAZrC8X8Di8SKaCijpfgk/?name=image.png)I'm afraid there may be some other issue we're not seeing yet.Now, the Production block was solved, and they have actually suggested we close this one and proceed with the investigation on the other ticket (for the refresh entities), but I'm afraid of the possibility this occurs again, considering the fact that the same connection works for one stage but not the other.What do you suggest we do? We can close this one, as indicated by the customer, but we'll likely reach out to you again in the context of the other ticket, via another escalation.Thanks again!
Jo&atilde;o Neves_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_July 29  3:49 PM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
Hi again team,So apparently they restarted the Cloud Connector and they claim it restored both connections (Dev and QA), but now QA is not working anymore again (still times out testing connection, still same errors).- We can confirm this in the logs for QA stage:![](https://supportoutsystems.zendesk.com/attachments/token/AFC7PwlvuFZWRXowmNcAU4qLG/?name=image.png)We can also say that QA has the same connection details as Development.They also have another two connections in which the same settings are all the same except for the used schema - for both these other connections it also fails just for QA.![](https://supportoutsystems.zendesk.com/attachments/token/dKGsNY1SQDlOUvUDX1jas3s8T/?name=image.png)![](https://supportoutsystems.zendesk.com/attachments/token/he9mTAZrC8X8Di8SKaCijpfgk/?name=image.png)I'm afraid there may be some other issue we're not seeing yet.Now, the Production block was solved, and they have actually suggested we close this one and proceed with the investigation on the other ticket (for the refresh entities), but I'm afraid of the possibility this occurs again, considering the fact that the same connection works for one stage but not the other.What do you suggest we do? We can close this one, as indicated by the customer, but we'll likely reach out to you again in the context of the other ticket, via another escalation.Thanks again!
Jo&atilde;o Neves__
July 29  4:05 PM WESTwebVasco Gomes
Incident has been mitigated
July 30 10:05 AM WESTwebVasco GomesSend ZenDesk private comment has been set: We have noticed that yesterday at 11:00PM UTC the QA environment that was down got re-established.  ![Screenshot%202024-07-30%20at%2010.02.43.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDIwMjI0LCJwdXIiOiJibG9iX2lkIn19--2817bdec81d603045ab79e770bc14ebfe168abbc/Screenshot%202024-07-30%20at%2010.02.43.png)Screenshot 2024-07-30 at 10.02.43.png 47.91 KBDo you know if they did any change with the connection?July 30 10:05 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
We have noticed that yesterday at 11:00PM UTC the QA environment that was down got re-established.  ![Screenshot%202024-07-30%20at%2010.02.43.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDIwMjI0LCJwdXIiOiJibG9iX2lkIn19--2817bdec81d603045ab79e770bc14ebfe168abbc/Screenshot%202024-07-30%20at%2010.02.43.png)Screenshot 2024-07-30 at 10.02.43.png 47.91 KBDo you know if they did any change with the connection?
July 30 10:05 AM WESTwebRootlySend ZenDesk private comment has been unsetJuly 30 10:05 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

July 30 10:52 AM WESTwebRootlyZendesk Private Comment has been changed to: ----------------------------------------------**Update to R&amp;D**
Hi team,Curiously, the customer has restarted Cloud Connector this morning and all three connections are now working, albeit with the `a5ad0b3b-66aa-4abe-b1ec-dbf153abd1b7` connection (`BANNER_SATURN`) still in NOK status.The problem remains that for this connection, they are not able to **Select/Refresh Entities -** they get the previously shared error:![](https://supportoutsystems.zendesk.com/attachments/token/DQbYuraCJwDJYvAqyQdLBwDjq/?name=image.png)
And if we attempt to Refresh, we can observe the following:- All three environments get the below messages:![](https://supportoutsystems.zendesk.com/attachments/token/GQc16Sq4U5YViEKMZ6NblgnZL/?name=image.png)
- But the **Development environment only** gets the following messages every few seconds:![](https://supportoutsystems.zendesk.com/attachments/token/xBjbNWjoyFv9IyKjMGgTAlY1m/?name=image.png)
- Until it eventually times out after 5 minutes and we receive the same error as in the first screenshot.- Direct links to environment and time interval:- Development- QA- ProductionNow, they have executed the **metadata_query.sql** against both instances (YEND - Dev/QA and PROD - Prod) and neither had any rows returned - is this expected?- For reference, they have filled the table names as expected for that connection. Attached is the query they ran.Also, they have activated verbose logging on Cloud Connector and will monitor onwards in case there are further issues.Finally, before we get lost in the troubleshooting, the customer also asked about an estimated timeline regarding the fix for the pods to not restart if the metadata refresh exceeds 5 minutes - is there any Jira issue you're tracking this on?Thanks for your assistance thus far, team!Jo&atilde;o Neves_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_Attachment(s):
lingnan_banner_saturn_metadata_query.sql - https://supportoutsystems.zendesk.com/attachments/token/XywgbABMwE58uD88M7VqhD4tb/?name=lingnan_banner_saturn_metadata_query.sqlJuly 30 10:52 AM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
Hi team,Curiously, the customer has restarted Cloud Connector this morning and all three connections are now working, albeit with the `a5ad0b3b-66aa-4abe-b1ec-dbf153abd1b7` connection (`BANNER_SATURN`) still in NOK status.The problem remains that for this connection, they are not able to **Select/Refresh Entities -** they get the previously shared error:![](https://supportoutsystems.zendesk.com/attachments/token/DQbYuraCJwDJYvAqyQdLBwDjq/?name=image.png)
And if we attempt to Refresh, we can observe the following:- All three environments get the below messages:![](https://supportoutsystems.zendesk.com/attachments/token/GQc16Sq4U5YViEKMZ6NblgnZL/?name=image.png)
- But the **Development environment only** gets the following messages every few seconds:![](https://supportoutsystems.zendesk.com/attachments/token/xBjbNWjoyFv9IyKjMGgTAlY1m/?name=image.png)
- Until it eventually times out after 5 minutes and we receive the same error as in the first screenshot.- Direct links to environment and time interval:- Development- QA- ProductionNow, they have executed the **metadata_query.sql** against both instances (YEND - Dev/QA and PROD - Prod) and neither had any rows returned - is this expected?- For reference, they have filled the table names as expected for that connection. Attached is the query they ran.Also, they have activated verbose logging on Cloud Connector and will monitor onwards in case there are further issues.Finally, before we get lost in the troubleshooting, the customer also asked about an estimated timeline regarding the fix for the pods to not restart if the metadata refresh exceeds 5 minutes - is there any Jira issue you're tracking this on?Thanks for your assistance thus far, team!Jo&atilde;o Neves__Attachment(s):
lingnan_banner_saturn_metadata_query.sql - https://supportoutsystems.zendesk.com/attachments/token/XywgbABMwE58uD88M7VqhD4tb/?name=lingnan_banner_saturn_metadata_query.sql
July 30 12:52 PM WESTwebVasco GomesSend ZenDesk private comment has been set: Regarding the connection (BANNER\_SATURN) being in a NOK status, we believe that is happening because, every interaction with that database is returning a I/O error.  
In the [Development Environment](https://outsystems.grafana.net/d/B8fujKKVz/query-engine?var-ring=ga&amp;var-container=outsystems-queryengine-service&amp;var-environment=f0075236-c771-43f2-9f52-deec51fe96e5&amp;from=now-12h&amp;to=now&amp;refresh=30s), if you check a little bit above the logs that you have shared, you can see an error :  ![error.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDIwMjU5LCJwdXIiOiJibG9iX2lkIn19--a6dbba4b00f96f24c73a3df16975d531bffacfff/error.png)error.png 157.38 KBAnd if we expand that error we can see that it is throwing an ORA-17002: I/O error :  ![expanded_error.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDIwMjYwLCJwdXIiOiJibG9iX2lkIn19--aa2f217395a8d9f8df9c8f6844092a26f208ec13/expanded_error.png)expanded\_error.png 147.8 KBThis indicates an Oracle database error (more info https://docs.oracle.com/en/error-help/db/ora-17002/?r=23ai)  
This error usually indicates that the database server terminated the connection unexpectedly. This could be due to network issues, a misconfiguration, or some other problem between the client and the server.  Since they've activated verbose logging on Cloud Connector this can give us more info on this.&nbsp;  
\--------------------------------------------------```
_Now, they have executed the_ **_metadata\_query.sql_** _against both instances (YEND - Dev/QA and PROD - Prod) and neither had any rows returned - is this expected?_
```No, it is not! The query should have returned the metadata of those tables. This indicates to us that the user that they are using might not have permissions to see the tables that they have selected.&nbsp;  
Can they confirm that the user as the correct permissions for every one of those tables?&nbsp;  
Can they run the following query (changing the 'table\_a' and 'table'b for the tables they've selected) and return the results?```
SELECT \* FROM USER\_TAB\_PRIVS WHERE OWNER = **sys\_context**(**'USERENV'**, **'CURRENT\_SCHEMA'**) AND TABLE\_NAME IN ('',) ;
```This is implied, but they have to use the user used in the connection config to run this query (and hopefully they have used it to run the metadata query).  
\-----------------------------------------```
_Finally, before we get lost in the troubleshooting, the customer also asked about an estimated timeline regarding the fix for the pods to not restart if the metadata refresh exceeds 5 minutes - is there any Jira issue you're tracking this on?_
```We thought of making that change and we can't. We can't proceed with the start of Query Engine without having the metadata refresh finished. If we did so, we could start to have runtime errors because the metadata was outdated.  
We intend to improve this process and mark the connection as Not OK if we don't get a response from the connection (if the connection is NOK, the metadata won't be fetched again) and Query Engine will be able to start up. We hope to address that story in the next sprint (we didn't created it yet).  
What we did, for now is that we increased the timeout to 10 minutes instead of 5 minutes. The issue where we did this was https://outsystemsrd.atlassian.net/browse/RDDFC-3041. We've already done the change and the change is in version [v1.233.528504](https://github.com/OutSystems/rd.datafabric.queryengine/releases/tag/v1.233.528504) which is going to progress through the rings.&nbsp;  
Ideally all the connections that are configured in Query Engine should be OK and working and the users that are used in the connection configured have to have read/write permissions for all the tables that are selected.July 30 12:52 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Regarding the connection (BANNER\_SATURN) being in a NOK status, we believe that is happening because, every interaction with that database is returning a I/O error.  
In the [Development Environment](https://outsystems.grafana.net/d/B8fujKKVz/query-engine?var-ring=ga&amp;var-container=outsystems-queryengine-service&amp;var-environment=f0075236-c771-43f2-9f52-deec51fe96e5&amp;from=now-12h&amp;to=now&amp;refresh=30s), if you check a little bit above the logs that you have shared, you can see an error :  ![error.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDIwMjU5LCJwdXIiOiJibG9iX2lkIn19--a6dbba4b00f96f24c73a3df16975d531bffacfff/error.png)error.png 157.38 KBAnd if we expand that error we can see that it is throwing an ORA-17002: I/O error :  ![expanded_error.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDIwMjYwLCJwdXIiOiJibG9iX2lkIn19--aa2f217395a8d9f8df9c8f6844092a26f208ec13/expanded_error.png)expanded\_error.png 147.8 KBThis indicates an Oracle database error (more info https://docs.oracle.com/en/error-help/db/ora-17002/?r=23ai)  
This error usually indicates that the database server terminated the connection unexpectedly. This could be due to network issues, a misconfiguration, or some other problem between the client and the server.  Since they've activated verbose logging on Cloud Connector this can give us more info on this.&nbsp;  
\--------------------------------------------------```
_Now, they have executed the_ **_metadata\_query.sql_** _against both instances (YEND - Dev/QA and PROD - Prod) and neither had any rows returned - is this expected?_
```No, it is not! The query should have returned the metadata of those tables. This indicates to us that the user that they are using might not have permissions to see the tables that they have selected.&nbsp;  
Can they confirm that the user as the correct permissions for every one of those tables?&nbsp;  
Can they run the following query (changing the 'table\_a' and 'table'b for the tables they've selected) and return the results?```
SELECT \* FROM USER\_TAB\_PRIVS WHERE OWNER = **sys\_context**(**'USERENV'**, **'CURRENT\_SCHEMA'**) AND TABLE\_NAME IN ('

',) ;
```This is implied, but they have to use the user used in the connection config to run this query (and hopefully they have used it to run the metadata query).  
\-----------------------------------------```
_Finally, before we get lost in the troubleshooting, the customer also asked about an estimated timeline regarding the fix for the pods to not restart if the metadata refresh exceeds 5 minutes - is there any Jira issue you're tracking this on?_
```We thought of making that change and we can't. We can't proceed with the start of Query Engine without having the metadata refresh finished. If we did so, we could start to have runtime errors because the metadata was outdated.  
We intend to improve this process and mark the connection as Not OK if we don't get a response from the connection (if the connection is NOK, the metadata won't be fetched again) and Query Engine will be able to start up. We hope to address that story in the next sprint (we didn't created it yet).  
What we did, for now is that we increased the timeout to 10 minutes instead of 5 minutes. The issue where we did this was https://outsystemsrd.atlassian.net/browse/RDDFC-3041. We've already done the change and the change is in version [v1.233.528504](https://github.com/OutSystems/rd.datafabric.queryengine/releases/tag/v1.233.528504) which is going to progress through the rings.&nbsp;  
Ideally all the connections that are configured in Query Engine should be OK and working and the users that are used in the connection configured have to have read/write permissions for all the tables that are selected.July 30 12:52 PM WESTwebRootlySend ZenDesk private comment has been unsetJuly 30 12:52 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

July 31  9:40 AM WESTwebRootlyZendesk Private Comment has been changed to: ----------------------------------------------**Update to R&amp;D**
Hi team!We just made some progress: it seems they forgot to change the schema when running the query.- Now that they run the query in the correct schema, they found it took over **21 minutes** (!) for a single table **SGBSTDN**, and that table alone returned **11.074 rows**!
- Looking at the resulting rows, it seems that **each column is** **duplicated 98 times**, for a total of **113 columns** (98 * 113 = 11.074). We attached the results they shared for that table: saturn_sgbstdn_metadata_query_result.xlsx- The executed query includes only the affected table **SGBSTDN** and they also removed the **ORDER BY** clause at the end to speed up the results.
- This table is also heavily used by their solution as it is the core student information table (they are a University).Looking at the query, I feel I have too little context/expertise to understand why it is returning so many duplicated records, so I have to leave that to you 😛Hope that helps, though, and thanks again!Jo&atilde;o Neves_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_July 31  9:40 AM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
Hi team!We just made some progress: it seems they forgot to change the schema when running the query.- Now that they run the query in the correct schema, they found it took over **21 minutes** (!) for a single table **SGBSTDN**, and that table alone returned **11.074 rows**!
- Looking at the resulting rows, it seems that **each column is** **duplicated 98 times**, for a total of **113 columns** (98 * 113 = 11.074). We attached the results they shared for that table: saturn_sgbstdn_metadata_query_result.xlsx- The executed query includes only the affected table **SGBSTDN** and they also removed the **ORDER BY** clause at the end to speed up the results.
- This table is also heavily used by their solution as it is the core student information table (they are a University).Looking at the query, I feel I have too little context/expertise to understand why it is returning so many duplicated records, so I have to leave that to you 😛Hope that helps, though, and thanks again!Jo&atilde;o Neves__
July 31 10:55 AM WESTwebVasco GomesSend ZenDesk private comment has been set: We've analysed the query and we ask you to ask the client to run the new metadata\_query\_v2.sql that we've uploaded to the ticket that we sent in attachment.  To explain to you, the difference is that we've replaced the first LEFT JOIN with an INNER JOIN, to remove the duplicates.  
Right now, we have just 1 metadata query, and we need that left join when we are returning the values to the API in one specific endpoint, because we have to show values even if the table is not selected (hence, the LEFT JOIN). **But**, when we are fetching the metadata in Query Engine on startup, we can substitute that LEFT JOIN for an INNER JOIN, because in that situation we just want to return the metadata for the selected tables. This is something that can be improved on our side and instead of having 1 metadata query, we can have 2 depending on when the query is &quot;called&quot;.  
Another important reference is that this query was used in the API in a initial version of Data Fabric, and it is still there only to guarantee retrocompatibility with older versions but the way the metadata is fetched currently is more efficient.&nbsp;  
This is information for Support, not for the client, since I believe it is too technical and as too much detail for them.  In summary :&nbsp;*   Ask client to run the query in attachment to see if it is quicker.
*   If it is we are going to improve the metadata query with this changeIf you have any more questions please let me know.July 31 10:55 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
We've analysed the query and we ask you to ask the client to run the new metadata\_query\_v2.sql that we've uploaded to the ticket that we sent in attachment.  To explain to you, the difference is that we've replaced the first LEFT JOIN with an INNER JOIN, to remove the duplicates.  
Right now, we have just 1 metadata query, and we need that left join when we are returning the values to the API in one specific endpoint, because we have to show values even if the table is not selected (hence, the LEFT JOIN). **But**, when we are fetching the metadata in Query Engine on startup, we can substitute that LEFT JOIN for an INNER JOIN, because in that situation we just want to return the metadata for the selected tables. This is something that can be improved on our side and instead of having 1 metadata query, we can have 2 depending on when the query is &quot;called&quot;.  
Another important reference is that this query was used in the API in a initial version of Data Fabric, and it is still there only to guarantee retrocompatibility with older versions but the way the metadata is fetched currently is more efficient.&nbsp;  
This is information for Support, not for the client, since I believe it is too technical and as too much detail for them.  In summary :&nbsp;*   Ask client to run the query in attachment to see if it is quicker.
*   If it is we are going to improve the metadata query with this changeIf you have any more questions please let me know.
July 31 10:56 AM WESTwebRootlySend ZenDesk private comment has been unsetJuly 31 10:56 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

July 31  2:51 PM WESTwebRootlyZendesk Private Comment has been changed to: ----------------------------------------------**Update to R&amp;D**
Hi again Vasco,Customer already ran the **v2** query but still had the same results - 11074 rows returned and still extremely slow.
metadata_queryv2_result.xlsxThey then took the initiative to have GPT optimize the query, to which they attached the revised version and obtained results - they are (and we as well) not sure of the correctness of the result, especially considering there are still duplicate rows.
metadata_queryv2_gpt_revised.zip
metadata_queryv2_gpt_revised_result.xlsx(all attachments added to Jira as well)Let me know your thoughts and the next steps!Jo&atilde;o Neves_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_July 31  2:51 PM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
Hi again Vasco,Customer already ran the **v2** query but still had the same results - 11074 rows returned and still extremely slow.
metadata_queryv2_result.xlsxThey then took the initiative to have GPT optimize the query, to which they attached the revised version and obtained results - they are (and we as well) not sure of the correctness of the result, especially considering there are still duplicate rows.
metadata_queryv2_gpt_revised.zip
metadata_queryv2_gpt_revised_result.xlsx(all attachments added to Jira as well)Let me know your thoughts and the next steps!Jo&atilde;o Neves__
July 31  3:29 PM WESTwebVasco GomesSend ZenDesk private comment has been set: Hello Jo&atilde;o,  
We find that odd because in our instances it was faster and without duplicates. they may have an edge case that we are not considering, and, because of this possibility,&nbsp; is it possible for the client to share their DDL with the creation of their tables so that we can analyze and better understand the specific use case?July 31  3:29 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hello Jo&atilde;o,  
We find that odd because in our instances it was faster and without duplicates. they may have an edge case that we are not considering, and, because of this possibility,&nbsp; is it possible for the client to share their DDL with the creation of their tables so that we can analyze and better understand the specific use case?
July 31  3:29 PM WESTwebRootlySend ZenDesk private comment has been unsetJuly 31  3:29 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

August 1  8:19 AM WESTwebRootlyZendesk Private Comment has been changed to: ----------------------------------------------**Update to R&amp;D**
Good morning team!Follows attached the DDL of the affected table: SGBSTDN.zip_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_August 1  8:19 AM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
Good morning team!Follows attached the DDL of the affected table: SGBSTDN.zip__
August 1  9:57 AM WESTwebRootlyZendesk Private Comment has been changed to: ----------------------------------------------**Update to R&amp;D**
Hi again team,On another note, the customer removed privileges to the affected table in the hopes that the entity refresh would complete successfully, but they still face the same error on ODC Portal.However, on our side, we can see the Query Engine errors are no longer present, which can be expected but odd at the same time since we still have errors on ODC Portal:![](https://supportoutsystems.zendesk.com/attachments/token/qHhssNGGkrnQxT4ixI0iiyKeu/?name=image.png)- Development (has additional logs, but also successful)
- ProductionI can also confirm that it now fails faster (around 1 minute) to get the ODC Portal error instead of the typical 5 minutes.What do you think may be happening? Could this be related with a conflict with metadata that we have already stored on our side?- I think this is a good point to raise awareness again to the below facts:- They only had **24 entities/tables** before errors started occurring.- After errors started occurring, the connection showed **25 entities**:![](https://supportoutsystems.zendesk.com/attachments/token/hqyVXdsoNXqe2qb5TezOxnHL8/?name=image.png)- Opening the entities screen, even with the error, it shows **48 entities** selected:![](https://supportoutsystems.zendesk.com/attachments/token/IxxUkCh724wuBVsqIla75s0rK/?name=image.png)- And if we now count the selected entities manually, there are **23 entities** in the list (the affected table no longer shows up, which matches subtracting that table from the original 24).![](https://supportoutsystems.zendesk.com/attachments/token/aHuZnxQRCh5zWKIIWJWwfnUhz/?name=image.png)_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_August 1  9:57 AM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
Hi again team,On another note, the customer removed privileges to the affected table in the hopes that the entity refresh would complete successfully, but they still face the same error on ODC Portal.However, on our side, we can see the Query Engine errors are no longer present, which can be expected but odd at the same time since we still have errors on ODC Portal:![](https://supportoutsystems.zendesk.com/attachments/token/qHhssNGGkrnQxT4ixI0iiyKeu/?name=image.png)- Development (has additional logs, but also successful)
- ProductionI can also confirm that it now fails faster (around 1 minute) to get the ODC Portal error instead of the typical 5 minutes.What do you think may be happening? Could this be related with a conflict with metadata that we have already stored on our side?- I think this is a good point to raise awareness again to the below facts:- They only had **24 entities/tables** before errors started occurring.- After errors started occurring, the connection showed **25 entities**:![](https://supportoutsystems.zendesk.com/attachments/token/hqyVXdsoNXqe2qb5TezOxnHL8/?name=image.png)- Opening the entities screen, even with the error, it shows **48 entities** selected:![](https://supportoutsystems.zendesk.com/attachments/token/IxxUkCh724wuBVsqIla75s0rK/?name=image.png)- And if we now count the selected entities manually, there are **23 entities** in the list (the affected table no longer shows up, which matches subtracting that table from the original 24).![](https://supportoutsystems.zendesk.com/attachments/token/aHuZnxQRCh5zWKIIWJWwfnUhz/?name=image.png)__
August 1 10:32 AM WESTwebVasco GomesSend ZenDesk private comment has been set: We are going to try to replicate the issue here with the DDL they have provided. I will keep you posted.&nbsp;  
Regarding the other questions that you've asked, since no error appears in Query Engine, I believe that the issue as to be analysed by Data Fabric Clients team. I will bring them into this discussion.August 1 10:32 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
We are going to try to replicate the issue here with the DDL they have provided. I will keep you posted.&nbsp;  
Regarding the other questions that you've asked, since no error appears in Query Engine, I believe that the issue as to be analysed by Data Fabric Clients team. I will bring them into this discussion.
August 1 10:32 AM WESTwebRootlySend ZenDesk private comment has been unsetAugust 1 10:32 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

August 1  3:56 PM WESTwebVasco GomesSend ZenDesk private comment has been set: Hello Support Team!&nbsp;  
I've asked the Clients team to analyse your questions and they have some doubts. Here is what they need :&nbsp;  
&quot;In order to try to understand why the number of selected entities is incorrect in the console, could you ask the customer to export an HAR and send us?  
I just need them to open the connections console and then open the entity selection screen for the BANNER\_SATURN entity.  
It&rsquo;s important that they have the Network tab open before opening the Connections console, in order for it to capture all the requests.  
In the meantime I&rsquo;ll try to find in Data Service&rsquo;s logs the reason for the metadata refresh failures.&quot;  
Can you ask that to the client, please?August 1  3:56 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hello Support Team!&nbsp;  
I've asked the Clients team to analyse your questions and they have some doubts. Here is what they need :&nbsp;  
&quot;In order to try to understand why the number of selected entities is incorrect in the console, could you ask the customer to export an HAR and send us?  
I just need them to open the connections console and then open the entity selection screen for the BANNER\_SATURN entity.  
It&rsquo;s important that they have the Network tab open before opening the Connections console, in order for it to capture all the requests.  
In the meantime I&rsquo;ll try to find in Data Service&rsquo;s logs the reason for the metadata refresh failures.&quot;  
Can you ask that to the client, please?
August 1  3:56 PM WESTwebRootlySend ZenDesk private comment has been unsetAugust 1  3:56 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

August 2  8:39 AM WESTwebRootlyZendesk Private Comment has been changed to: ----------------------------------------------**Update to R&amp;D**
Hi team,Attaching here the HAR file: lingnan.outsystems.dev.harAlso note that this we can get autonomously since we have access to the customers' tenants, so feel free to ask for more at any time if needed.Regarding the DDL for the additional tables, is it just the tables for which SGBSTDN has dependencies? Or do we need their dependencies as well, and so forth?- If it's the latter, is it safe to say that it's all the tables from this column?![](https://supportoutsystems.zendesk.com/attachments/token/5QMjyof8uqFtx4Qyy9PrKAH4t/?name=image.png)Nevertheless, customer has also requested we prioritize the runtime issue over the query engine one, since the SGBSTDN table is not strictly required for operation and they're considering having it removed to resolve the connection issues. We can address both of them, but just so you know!Thanks in advance!
Jo&atilde;o Neves_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_August 2  8:39 AM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
Hi team,Attaching here the HAR file: lingnan.outsystems.dev.harAlso note that this we can get autonomously since we have access to the customers' tenants, so feel free to ask for more at any time if needed.Regarding the DDL for the additional tables, is it just the tables for which SGBSTDN has dependencies? Or do we need their dependencies as well, and so forth?- If it's the latter, is it safe to say that it's all the tables from this column?![](https://supportoutsystems.zendesk.com/attachments/token/5QMjyof8uqFtx4Qyy9PrKAH4t/?name=image.png)Nevertheless, customer has also requested we prioritize the runtime issue over the query engine one, since the SGBSTDN table is not strictly required for operation and they're considering having it removed to resolve the connection issues. We can address both of them, but just so you know!Thanks in advance!
Jo&atilde;o Neves__
August 2  9:42 AM WESTwebRootlyZendesk Private Comment has been changed to: ----------------------------------------------**Update to R&amp;D**
Hi Vera,Attached the DDL of the tables: OracleTablesDDL.zipThank you!_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_August 2  9:42 AM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
Hi Vera,Attached the DDL of the tables: OracleTablesDDL.zipThank you!__
August 2  9:44 AM WESTwebVasco GomesSend ZenDesk private comment has been set: Hello Jo&atilde;o!  
Let me see if I understand. At this time they cannot add the new connection because of the errors right? But at the same time, if they were able to, we would have a problem getting the metadata (because it takes to long).  
Because of that, I don't quite understand the prioritisation that they are asking, since it seems that they want the error that the Data Fabric Clients team is analysing to &quot;go away&quot; and are de-prioritising the analysis that the Data Fabric Engine Team is doing with the DDL. Is this correct?August 2  9:44 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hello Jo&atilde;o!  
Let me see if I understand. At this time they cannot add the new connection because of the errors right? But at the same time, if they were able to, we would have a problem getting the metadata (because it takes to long).  
Because of that, I don't quite understand the prioritisation that they are asking, since it seems that they want the error that the Data Fabric Clients team is analysing to &quot;go away&quot; and are de-prioritising the analysis that the Data Fabric Engine Team is doing with the DDL. Is this correct?
August 2  9:45 AM WESTwebRootlySend ZenDesk private comment has been unsetAugust 2  9:45 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

August 2  9:54 AM WESTwebRootlyZendesk Private Comment has been changed to: ----------------------------------------------**Update to R&amp;D**
Hi again Vera,So they want to be able to refresh the (other) entities in that connection, thus they have already discarded the need for the table that causes the slowness in retrieving the metadata.But even in doing so, by removing the privileges of the database user to that table (and thus making it invisible for the metadata retrieval, I guess), they still get the reported error in refreshing entities.Hence, they are still blocked from refreshing the entities of that connection regardless, which is their original issue that prompted them to reach out to us.- For reference, the Sev1 originated after they tried to create a duplicate connection which caused the metadata retrieval to fail and the constant restart of the Query Engine pods, causing all sorts of runtime errors.
- Considering this last point, and that they have &quot;removed&quot; the affected table, maybe creating a duplicate connection could be an option now?Does this make more sense now? What do you think?_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_August 2  9:54 AM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
Hi again Vera,So they want to be able to refresh the (other) entities in that connection, thus they have already discarded the need for the table that causes the slowness in retrieving the metadata.But even in doing so, by removing the privileges of the database user to that table (and thus making it invisible for the metadata retrieval, I guess), they still get the reported error in refreshing entities.Hence, they are still blocked from refreshing the entities of that connection regardless, which is their original issue that prompted them to reach out to us.- For reference, the Sev1 originated after they tried to create a duplicate connection which caused the metadata retrieval to fail and the constant restart of the Query Engine pods, causing all sorts of runtime errors.
- Considering this last point, and that they have &quot;removed&quot; the affected table, maybe creating a duplicate connection could be an option now?Does this make more sense now? What do you think?__
August 2 10:29 AM WESTwebVasco GomesSend ZenDesk private comment has been set: Hello!  Another question that I have is if the client is only have problems with the metadata query with the table &quot;SGBSTDN&quot;? is the metadata query returning values quickly for all the other tables of that connection? Is the problem only with that table?August 2 10:30 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hello!  Another question that I have is if the client is only have problems with the metadata query with the table &quot;SGBSTDN&quot;? is the metadata query returning values quickly for all the other tables of that connection? Is the problem only with that table?
August 2 10:30 AM WESTwebRootlySend ZenDesk private comment has been unsetAugust 2 10:30 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

August 2 10:39 AM WESTwebVasco GomesSend ZenDesk private comment has been set: Hi Jo&atilde;o,  
I think you've answered my question in the last update that you gave. So, the metadata query takes a lot of time only fetching the metadata for the &quot;SGBSTDN&quot; table.  
I think that what you are suggesting will work, which is :&nbsp;*   Creating a new connection to the same database
*   Selecting all the tables that they want to use (without &quot;SGBSTDN&quot;)The problem that I see with it (which I don't know if it is a problem) is that if they use the other connection in their apps, they would have to change it to the new connection that they are going to create. If this isn't a problem for them, I believe that this is a possible solution.&nbsp;  In the meantime, I have shared with Data Fabric Clients team the har that you've provided.&nbsp;  
So, in summary :&nbsp;*   You can share that workaround with the client
*   In the meantime we are going to analyse the DDL to try to understand the reason why the metadata query is slow in this use-case.
*   The Data Fabric Clients team is going to analyse the HAR to try to understand the problem.&nbsp;Are you ok with this plan? Do you think anything else is needed for this incident, at this time?August 2 10:39 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hi Jo&atilde;o,  
I think you've answered my question in the last update that you gave. So, the metadata query takes a lot of time only fetching the metadata for the &quot;SGBSTDN&quot; table.  
I think that what you are suggesting will work, which is :&nbsp;*   Creating a new connection to the same database
*   Selecting all the tables that they want to use (without &quot;SGBSTDN&quot;)The problem that I see with it (which I don't know if it is a problem) is that if they use the other connection in their apps, they would have to change it to the new connection that they are going to create. If this isn't a problem for them, I believe that this is a possible solution.&nbsp;  In the meantime, I have shared with Data Fabric Clients team the har that you've provided.&nbsp;  
So, in summary :&nbsp;*   You can share that workaround with the client
*   In the meantime we are going to analyse the DDL to try to understand the reason why the metadata query is slow in this use-case.
*   The Data Fabric Clients team is going to analyse the HAR to try to understand the problem.&nbsp;Are you ok with this plan? Do you think anything else is needed for this incident, at this time?
August 2 10:39 AM WESTwebRootlySend ZenDesk private comment has been unsetAugust 2 10:39 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

August 2 10:55 AM WESTwebRootlyZendesk Private Comment has been changed to: ----------------------------------------------**Update to R&amp;D**
Hi again!I've suggested that option to the customer, they can pick it up if they want - should be the quickest path forward for them anyway.And yeah, regarding the current faulty connection, the SGBSTDN does not even show up anymore in the list of selected entities, so that's why we're seemingly out of options regarding this faulty connection.- Although, looking at the HAR file previously shared, we can see that the table is part of the **DataActionGetEntities** response - in fact, all original tables are duplicated in that response, with different Ids. But this is probably something that the team is already aware of.Plan sounds very good. I will let you know the customer's thoughts on the proposed workaround.Cheers!
Jo&atilde;o Neves_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_August 2 10:55 AM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
Hi again!I've suggested that option to the customer, they can pick it up if they want - should be the quickest path forward for them anyway.And yeah, regarding the current faulty connection, the SGBSTDN does not even show up anymore in the list of selected entities, so that's why we're seemingly out of options regarding this faulty connection.- Although, looking at the HAR file previously shared, we can see that the table is part of the **DataActionGetEntities** response - in fact, all original tables are duplicated in that response, with different Ids. But this is probably something that the team is already aware of.Plan sounds very good. I will let you know the customer's thoughts on the proposed workaround.Cheers!
Jo&atilde;o Neves__
August 2 11:14 AM WESTwebRootlyZendesk Private Comment has been changed to: ----------------------------------------------**Update to R&amp;D**
Hi again team,Just another quick update: the customer had already thought of that option as well, but they decided against it since they don't want to risk any more Production impact, which is understandable from their point-of-view.They prefer to wait for the root cause to be identified first and keep the development of the application halted._&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_August 2 11:14 AM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
Hi again team,Just another quick update: the customer had already thought of that option as well, but they decided against it since they don't want to risk any more Production impact, which is understandable from their point-of-view.They prefer to wait for the root cause to be identified first and keep the development of the application halted.__
August 2 12:06 PM WESTwebVasco GomesSend ZenDesk private comment has been set: Hello again, Jo&atilde;o,  The root cause for the PRD environment to have been down on Monday was identified already. It was because the metadata query was taking a long time and because of that Query Engine was unable to start and because the user didn't have enough privileges in all the databases.  
The reason why the metadata query was taking a long time is still unclear, and that's why we needed the DDL and are analysing it, **but** if they confirm that the metadata query is fast for all the other tables except the SGBSTDN table they won't have the same problem.&nbsp;  
As previously explained, we have implemented guardrails to prevent the same from happening again, and they are progressing through the rings.&nbsp;  
Namely we've increased the the metadata timeout value from 5 to 10 minutes and when this timeout occurs we are going to mark the connection as NOK and the pod will start up.&nbsp;  
So, in a nutshell, if they want, they can test previously the metadata query, by adding the tables that they want to select in the connection. If it is quick, they can go ahead with the workaround.&nbsp;  
If they prefer, they can wait for the guardrails to be deployed in GA.&nbsp;  If you have any question, please let me know.August 2 12:06 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hello again, Jo&atilde;o,  The root cause for the PRD environment to have been down on Monday was identified already. It was because the metadata query was taking a long time and because of that Query Engine was unable to start and because the user didn't have enough privileges in all the databases.  
The reason why the metadata query was taking a long time is still unclear, and that's why we needed the DDL and are analysing it, **but** if they confirm that the metadata query is fast for all the other tables except the SGBSTDN table they won't have the same problem.&nbsp;  
As previously explained, we have implemented guardrails to prevent the same from happening again, and they are progressing through the rings.&nbsp;  
Namely we've increased the the metadata timeout value from 5 to 10 minutes and when this timeout occurs we are going to mark the connection as NOK and the pod will start up.&nbsp;  
So, in a nutshell, if they want, they can test previously the metadata query, by adding the tables that they want to select in the connection. If it is quick, they can go ahead with the workaround.&nbsp;  
If they prefer, they can wait for the guardrails to be deployed in GA.&nbsp;  If you have any question, please let me know.
August 2 12:06 PM WESTwebRootlySend ZenDesk private comment has been unsetAugust 2 12:06 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

August 2  8:25 PM WESTwebVera Cardoso
Hi Jo&atilde;oThe script that contains the DDL for the table `SGBSTDN` has a command to alter the table and set the corresponding constraints. In this command we see a lot of `... REFERENCES SATURN. ,`. As you can see the FK is being defined just with the schema name and with an empty name for the table. I don't know how this can happen, nut we cannot create the constraints like this.
We removed all the constraint without a table from the command, and run it.
After doing that, we run the metadata query and the results where returned in less than 2 seconds.
Of course on our scenario there are a lot less of constraints to that table, neverthless I'm starting to think that there is something wrong with the definition of the constraints in that table.
August 5 12:15 PM WESTwebVasco GomesSend ZenDesk private comment has been set: Hi Jo&atilde;o  The script that contains the DDL for the table SGBSTDN has a command to alter the table and set the corresponding constraints. In this command we see a lot of ... REFERENCES SATURN. ,. As you can see the FK is being defined just with the schema name and with an empty name for the table.&nbsp;  
This happens for the following constraints :&nbsp;1.  FK10\_SGBSTDN\_INV\_STVMAJR\_CODE
2.  FK11\_SGBSTDN\_INV\_STVMAJR\_CODE
3.  FK12\_SGBSTDN\_INV\_STVMAJR\_CODE
4.  FK1\_SGBSTDN\_INV\_SOBCURR\_KEY
5.  FK1\_SGBSTDN\_INV\_SORCCON\_KEY
6.  FK1\_SGBSTDN\_INV\_SORCMJR\_KEY
7.  FK1\_SGBSTDN\_INV\_SORCMNR\_KEY
8.  FK1\_SGBSTDN\_INV\_STVACYR\_CODE
9.  FK1\_SGBSTDN\_INV\_STVAPRN\_CODE
10.  FK1\_SGBSTDN\_INV\_STVASTD\_CODE
11.  FK1\_SGBSTDN\_INV\_STVBLCK\_CODE
12.  FK1\_SGBSTDN\_INV\_STVBSKL\_CODE
13.  FK1\_SGBSTDN\_INV\_STVCAMP\_CODE
14.  FK1\_SGBSTDN\_INV\_STVCAPL\_CODE
15.  FK1\_SGBSTDN\_INV\_STVCAST\_CODE
16.  FK1\_SGBSTDN\_INV\_STVCOLL\_CODE
17.  FK1\_SGBSTDN\_INV\_STVEGOL\_CODE
18.  FK1\_SGBSTDN\_INV\_STVEMEX\_CODE
19.  FK1\_SGBSTDN\_INV\_STVGAIN\_CODE
20.  FK1\_SGBSTDN\_INV\_STVINCM\_CODE
21.  FK1\_SGBSTDN\_INV\_STVLEAV\_CODE
22.  FK1\_SGBSTDN\_INV\_STVPRAC\_CODE
23.  FK1\_SGBSTDN\_INV\_STVPREV\_CODE
24.  FK1\_SGBSTDN\_INV\_STVRATE\_CODE
25.  FK1\_SGBSTDN\_INV\_STVSCPC\_CODE
26.  FK1\_SGBSTDN\_INV\_STVSESS\_CODE
27.  FK1\_SGBSTDN\_INV\_STVSITE\_CODE
28.  FK1\_SGBSTDN\_INV\_STVSTYP\_CODE
29.  FK1\_SGBSTDN\_INV\_STVVOED\_CODE
30.  FK20\_SGBSTDN\_INV\_STVMAJR\_CODE
31.  FK2\_SGBSTDN\_INV\_SOBCURR\_KEY
32.  FK2\_SGBSTDN\_INV\_SORCCON\_KEY
33.  FK2\_SGBSTDN\_INV\_SORCMJR\_KEY
34.  FK2\_SGBSTDN\_INV\_SORCMNR\_KEY
35.  FK2\_SGBSTDN\_INV\_STVADMT\_CODE
36.  FK2\_SGBSTDN\_INV\_STVCAMP\_CODE
37.  FK2\_SGBSTDN\_INV\_STVCOLL\_CODE
38.  FK3\_SGBSTDN\_INV\_SORCMJR\_KEY
39.  FK3\_SGBSTDN\_INV\_SORCMNR\_KEY
40.  FK3\_SGBSTDN\_INV\_STVCOLL\_CODE
41.  FK4\_SGBSTDN\_INV\_SORCMJR\_KEY
42.  FK4\_SGBSTDN\_INV\_SORCMNR\_KEY
43.  FK4\_SGBSTDN\_INV\_STVDEPT\_CODE
44.  FK5\_SGBSTDN\_INV\_STVDEPT\_CODE
45.  FK6\_SGBSTDN\_INV\_STVMAJR\_CODE
46.  FK7\_SGBSTDN\_INV\_STVMAJR\_CODE
47.  FK8\_SGBSTDN\_INV\_STVMAJR\_CODE
48.  FK9\_SGBSTDN\_INV\_STVMAJR\_CODEWe removed all the constraint without a table from the command, and we ran it locally and the metadata query return the metadata results in less than 2 seconds.  
It is possible that the reason for the delay is this inconsistency with the Foreign Keys.  
Can you ask the client to take a look at this? Can they explain were those constraints are pointing and check if they are being used correctly?  ![Foreign%20Keys.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDI0MzU0LCJwdXIiOiJibG9iX2lkIn19--0245f4d622553968aaa583f3d4035cd1ca211362/Foreign%20Keys.png)Foreign Keys.png 432.71 KBAugust 5 12:15 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hi Jo&atilde;o  The script that contains the DDL for the table SGBSTDN has a command to alter the table and set the corresponding constraints. In this command we see a lot of ... REFERENCES SATURN. ,. As you can see the FK is being defined just with the schema name and with an empty name for the table.&nbsp;  
This happens for the following constraints :&nbsp;1.  FK10\_SGBSTDN\_INV\_STVMAJR\_CODE
2.  FK11\_SGBSTDN\_INV\_STVMAJR\_CODE
3.  FK12\_SGBSTDN\_INV\_STVMAJR\_CODE
4.  FK1\_SGBSTDN\_INV\_SOBCURR\_KEY
5.  FK1\_SGBSTDN\_INV\_SORCCON\_KEY
6.  FK1\_SGBSTDN\_INV\_SORCMJR\_KEY
7.  FK1\_SGBSTDN\_INV\_SORCMNR\_KEY
8.  FK1\_SGBSTDN\_INV\_STVACYR\_CODE
9.  FK1\_SGBSTDN\_INV\_STVAPRN\_CODE
10.  FK1\_SGBSTDN\_INV\_STVASTD\_CODE
11.  FK1\_SGBSTDN\_INV\_STVBLCK\_CODE
12.  FK1\_SGBSTDN\_INV\_STVBSKL\_CODE
13.  FK1\_SGBSTDN\_INV\_STVCAMP\_CODE
14.  FK1\_SGBSTDN\_INV\_STVCAPL\_CODE
15.  FK1\_SGBSTDN\_INV\_STVCAST\_CODE
16.  FK1\_SGBSTDN\_INV\_STVCOLL\_CODE
17.  FK1\_SGBSTDN\_INV\_STVEGOL\_CODE
18.  FK1\_SGBSTDN\_INV\_STVEMEX\_CODE
19.  FK1\_SGBSTDN\_INV\_STVGAIN\_CODE
20.  FK1\_SGBSTDN\_INV\_STVINCM\_CODE
21.  FK1\_SGBSTDN\_INV\_STVLEAV\_CODE
22.  FK1\_SGBSTDN\_INV\_STVPRAC\_CODE
23.  FK1\_SGBSTDN\_INV\_STVPREV\_CODE
24.  FK1\_SGBSTDN\_INV\_STVRATE\_CODE
25.  FK1\_SGBSTDN\_INV\_STVSCPC\_CODE
26.  FK1\_SGBSTDN\_INV\_STVSESS\_CODE
27.  FK1\_SGBSTDN\_INV\_STVSITE\_CODE
28.  FK1\_SGBSTDN\_INV\_STVSTYP\_CODE
29.  FK1\_SGBSTDN\_INV\_STVVOED\_CODE
30.  FK20\_SGBSTDN\_INV\_STVMAJR\_CODE
31.  FK2\_SGBSTDN\_INV\_SOBCURR\_KEY
32.  FK2\_SGBSTDN\_INV\_SORCCON\_KEY
33.  FK2\_SGBSTDN\_INV\_SORCMJR\_KEY
34.  FK2\_SGBSTDN\_INV\_SORCMNR\_KEY
35.  FK2\_SGBSTDN\_INV\_STVADMT\_CODE
36.  FK2\_SGBSTDN\_INV\_STVCAMP\_CODE
37.  FK2\_SGBSTDN\_INV\_STVCOLL\_CODE
38.  FK3\_SGBSTDN\_INV\_SORCMJR\_KEY
39.  FK3\_SGBSTDN\_INV\_SORCMNR\_KEY
40.  FK3\_SGBSTDN\_INV\_STVCOLL\_CODE
41.  FK4\_SGBSTDN\_INV\_SORCMJR\_KEY
42.  FK4\_SGBSTDN\_INV\_SORCMNR\_KEY
43.  FK4\_SGBSTDN\_INV\_STVDEPT\_CODE
44.  FK5\_SGBSTDN\_INV\_STVDEPT\_CODE
45.  FK6\_SGBSTDN\_INV\_STVMAJR\_CODE
46.  FK7\_SGBSTDN\_INV\_STVMAJR\_CODE
47.  FK8\_SGBSTDN\_INV\_STVMAJR\_CODE
48.  FK9\_SGBSTDN\_INV\_STVMAJR\_CODEWe removed all the constraint without a table from the command, and we ran it locally and the metadata query return the metadata results in less than 2 seconds.  
It is possible that the reason for the delay is this inconsistency with the Foreign Keys.  
Can you ask the client to take a look at this? Can they explain were those constraints are pointing and check if they are being used correctly?  ![Foreign%20Keys.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDI0MzU0LCJwdXIiOiJibG9iX2lkIn19--0245f4d622553968aaa583f3d4035cd1ca211362/Foreign%20Keys.png)Foreign Keys.png 432.71 KB
August 5 12:15 PM WESTwebRootlySend ZenDesk private comment has been unsetAugust 5 12:15 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

August 5  2:43 PM WESTwebVasco GomesSend ZenDesk private comment has been set: We've noticed that the PRD connection went down again, and stayed down for a period of time in the morning.![Probes.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDI0NDU2LCJwdXIiOiJibG9iX2lkIn19--332d1fe65cc87cfbc85f4369ed1d3ea6427d6d39/Probes.png)Probes.png 54.18 KBThe connection just went back up, after it was able to recover itself as it can be seen in the [logs](https://outsystems.grafana.net/d/B8fujKKVz/query-engine?var-ring=ga&amp;var-container=outsystems-queryengine-service&amp;var-environment=90f69c30-2f17-449a-9790-a3ea6c3f195e&amp;from=now-12h&amp;to=now) :![logs.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDI0NDU1LCJwdXIiOiJibG9iX2lkIn19--712e76f16414d7f448872b5b4f25984924169b53/logs.png)logs.png 188.12 KBAugust 5  2:43 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
We've noticed that the PRD connection went down again, and stayed down for a period of time in the morning.![Probes.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDI0NDU2LCJwdXIiOiJibG9iX2lkIn19--332d1fe65cc87cfbc85f4369ed1d3ea6427d6d39/Probes.png)Probes.png 54.18 KBThe connection just went back up, after it was able to recover itself as it can be seen in the [logs](https://outsystems.grafana.net/d/B8fujKKVz/query-engine?var-ring=ga&amp;var-container=outsystems-queryengine-service&amp;var-environment=90f69c30-2f17-449a-9790-a3ea6c3f195e&amp;from=now-12h&amp;to=now) :![logs.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDI0NDU1LCJwdXIiOiJibG9iX2lkIn19--712e76f16414d7f448872b5b4f25984924169b53/logs.png)logs.png 188.12 KB
August 5  2:43 PM WESTwebRootlySend ZenDesk private comment has been unsetAugust 5  2:43 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

August 6  2:33 AM WESTwebRootlyZendesk Private Comment has been changed to: ----------------------------------------------**Update to R&amp;D**
- Detail additional findings or any questions/concerns that may be important for R&amp;D to be aware of.The customer has provided us the DDL of the table SGBSTDN. Apparently this is the revised version, the previous version was done with under-privileged account, which may explain why some of the table names were not included.Attached is the file._&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_Attachment(s):
SGBSTDN_revised.zip - https://supportoutsystems.zendesk.com/attachments/token/DJotouTyoccBsgcQucLZVpKKH/?name=SGBSTDN_revised.zipAugust 6  2:34 AM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
- Detail additional findings or any questions/concerns that may be important for R&amp;D to be aware of.The customer has provided us the DDL of the table SGBSTDN. Apparently this is the revised version, the previous version was done with under-privileged account, which may explain why some of the table names were not included.Attached is the file.__Attachment(s):
SGBSTDN_revised.zip - https://supportoutsystems.zendesk.com/attachments/token/DJotouTyoccBsgcQucLZVpKKH/?name=SGBSTDN_revised.zip
August 6  2:34 AM WESTwebRootlyZendesk Private Comment has been changed to: ------------------------------------------------ This notification was sent from Zendesk Support ticket #3041981 to all linked JIRA issues by Zaman Akbar Mohamed-Akbar. --**Update to R&amp;D**- Detail additional findings or any questions/concerns that may be important for R&amp;D to be aware of.The customer has provided us the DDL of the table SGBSTDN. Apparently this is the revised version, the previous version was done with under-privileged account, which may explain why some of the table names were not included.Attached is the file._&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;__Attachments_SGBSTDN_revised.zipAugust 6  2:34 AM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
------------------------------------------------ This notification was sent from Zendesk Support ticket #3041981 to all linked JIRA issues by Zaman Akbar Mohamed-Akbar. --**Update to R&amp;D**- Detail additional findings or any questions/concerns that may be important for R&amp;D to be aware of.The customer has provided us the DDL of the table SGBSTDN. Apparently this is the revised version, the previous version was done with under-privileged account, which may explain why some of the table names were not included.Attached is the file.___Attachments_SGBSTDN_revised.zip
August 6 10:06 AM WESTwebVasco GomesSend ZenDesk private comment has been set: Hello Jo&atilde;o,  The new DDL that they sent references tables that we were not sent to us. Namely :&nbsp;*   SMRPRLE
*   SOBCURR
*   SORCCON
*   SORCMJR
*   SORCMNR
*   STVADMT
*   STVAPRN
*   STVASTD
*   STVBLCK
*   STVBSKL
*   STVCAMP
*   STVCAPL
*   STVCAST
*   STVEDLV
*   STVEGOL
*   STVEMEX
*   STVGAIN
*   STVINCM
*   STVORSN
*   STVPRAC
*   STVPREV
*   STVRESD
*   STVSCPC
*   STVSESS
*   STVSTST
*   STVTRCN
*   STVVOEDWe need all those tables to properly run the metadata query of the problematic table.August 6 10:06 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hello Jo&atilde;o,  The new DDL that they sent references tables that we were not sent to us. Namely :&nbsp;*   SMRPRLE
*   SOBCURR
*   SORCCON
*   SORCMJR
*   SORCMNR
*   STVADMT
*   STVAPRN
*   STVASTD
*   STVBLCK
*   STVBSKL
*   STVCAMP
*   STVCAPL
*   STVCAST
*   STVEDLV
*   STVEGOL
*   STVEMEX
*   STVGAIN
*   STVINCM
*   STVORSN
*   STVPRAC
*   STVPREV
*   STVRESD
*   STVSCPC
*   STVSESS
*   STVSTST
*   STVTRCN
*   STVVOEDWe need all those tables to properly run the metadata query of the problematic table.
August 6 10:06 AM WESTwebRootlySend ZenDesk private comment has been unsetAugust 6 10:06 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

August 8 11:13 AM WESTwebRootlyZendesk Private Comment has been changed to: ----------------------------------------------**Update to R&amp;D**
Hi team,Good news, the customer was able to successfully &quot;migrate&quot; to the duplicate connection without the affected table and have removed the faulty connection - so far there were no issues observed.Nevertheless, they have shared some of their concerns which we are not fully equipped to answer:1. The SGBSTDN table has been part of the BANNER_SATURN connection since the beginning, and we have never encountered any issues with it until now.
2. During our early adoption of the platform, we faced difficulties adding some tables due to foreign key constraints. It was advised to grant privileges on related tables to the DB account to resolve these issues.
3. We are concerned that similar issues may arise in the future with other tables that have similar characteristics.
4. Additionally, we are unclear why additional privileges on related tables are required for metadata retrieval to function. The table privileges were set up to limit the scope of access, and broadening these privileges for metadata retrieval in ODC does not seem like a viable solution from our perspective.Namely, we don't know what the rationale is behind broadening the privileges for the metadata retrieval to succeed - can you help us out on this?We've also reiterated with them that if they want to pursue the identification of the root cause, they must send us the additional tables from the references.Thanks again for your efforts!Jo&atilde;o Neves_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_August 8 11:13 AM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
Hi team,Good news, the customer was able to successfully &quot;migrate&quot; to the duplicate connection without the affected table and have removed the faulty connection - so far there were no issues observed.Nevertheless, they have shared some of their concerns which we are not fully equipped to answer:1. The SGBSTDN table has been part of the BANNER_SATURN connection since the beginning, and we have never encountered any issues with it until now.
2. During our early adoption of the platform, we faced difficulties adding some tables due to foreign key constraints. It was advised to grant privileges on related tables to the DB account to resolve these issues.
3. We are concerned that similar issues may arise in the future with other tables that have similar characteristics.
4. Additionally, we are unclear why additional privileges on related tables are required for metadata retrieval to function. The table privileges were set up to limit the scope of access, and broadening these privileges for metadata retrieval in ODC does not seem like a viable solution from our perspective.Namely, we don't know what the rationale is behind broadening the privileges for the metadata retrieval to succeed - can you help us out on this?We've also reiterated with them that if they want to pursue the identification of the root cause, they must send us the additional tables from the references.Thanks again for your efforts!Jo&atilde;o Neves__
August 9 10:26 AM WESTwebVasco GomesSend ZenDesk private comment has been set: Hello Jo&atilde;o!&nbsp;  Regarding the SGBSTDN what we've concluded was that it was in fact the cause for the original problem that the pods couldn't start and that was because the metadata query was taking a long time. This is a fact.  
Why did this start to happen now and not earlier we can't draw any definitive conclusions, because we can't be sure if there was any change on the table on the external connection. It could be any sort of problems, but it was probably related with privileges, since the problem &quot;got fixed&quot; once they've removed the privileges on it (as far as I know).  
Without having the full DDL on the table we cannot draw definitive conclusions on the matter, unfortunately.  
What we can and will do is create a story to analyse the impact of an user having privileges to Table A, and that table references Table B which the user does not have privileges.&nbsp;  
We will investigate this and let you know the conclusions (I have associated our ticket with the original Jira Incident).  
After that, we can problem answer your question #4.&nbsp;  Regarding this incident, I don't think there is anything else we can do (without having the DDL for the table).  Thanks for all your help, Jo&atilde;o!August 9 10:26 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hello Jo&atilde;o!&nbsp;  Regarding the SGBSTDN what we've concluded was that it was in fact the cause for the original problem that the pods couldn't start and that was because the metadata query was taking a long time. This is a fact.  
Why did this start to happen now and not earlier we can't draw any definitive conclusions, because we can't be sure if there was any change on the table on the external connection. It could be any sort of problems, but it was probably related with privileges, since the problem &quot;got fixed&quot; once they've removed the privileges on it (as far as I know).  
Without having the full DDL on the table we cannot draw definitive conclusions on the matter, unfortunately.  
What we can and will do is create a story to analyse the impact of an user having privileges to Table A, and that table references Table B which the user does not have privileges.&nbsp;  
We will investigate this and let you know the conclusions (I have associated our ticket with the original Jira Incident).  
After that, we can problem answer your question #4.&nbsp;  Regarding this incident, I don't think there is anything else we can do (without having the DDL for the table).  Thanks for all your help, Jo&atilde;o!
August 9 10:26 AM WESTwebRootlySend ZenDesk private comment has been unsetAugust 9 10:26 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

August 14 10:30 AM WESTwebVasco GomesSend ZenDesk private comment has been set: Hello Support team,  We analysed this issue a bit more and we tested the following scenario.&nbsp;  
Table A has an FK that points to Table B.  
User has privileges to Table A but not to Table B.  We checked that if a database user does not have the necessary privileges to access a table, they will not be able to view metadata information about foreign keys related to that table.  In this scenario, the refresh metadata query only shows information regarding table A. This is expected since it is only possible to access information in metadata tables ALL\_TABS\_COLS, ALL\_CONS\_COLUMNS and USER\_CONS\_COLUMNS to information regarding tables the user has access to.  We've also compared 2 scenarios to confirm if there was anything wrong with the metadata query if the user didn't had permissions to table B and we've managed to confirm that the time that the query takes is similar (~0.1s, for our tested scenario)&nbsp;  In summary, nothing fails getting the metadata if the user doesn't have priviliges on Table B.&nbsp;  
But there are some limitations because of it :&nbsp;*   FK aren&rsquo;t treated as such due to incomplete information in FK constrains.
*   Normal FK input validations not in place which can lead to query execution errors. Example:1.  User selects table A with FK to table B2.  Since user does not have permissions to table B and FK is a NUMBER(38,0) column will appear as a Text field.&nbsp;3.  Table A is added to outsystems application and is published.4.  In runtime, a User tries to create a record with incorrect input envolving letters in the FK field. Since the column was identified as text and table B is not present, the input is not validated.&nbsp;5.  Application returns in runtime error&nbsp;Because of this limitations, it is advisable that the user has privileges not only for the tables that he wants, but also for the tables that are related (through FKs and Constraints) to those tables.&nbsp;  
We will update our public documentation with this.&nbsp;  Regarding the problem that the user reported, we will wait for the DDL to be sent.August 14 10:30 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hello Support team,  We analysed this issue a bit more and we tested the following scenario.&nbsp;  
Table A has an FK that points to Table B.  
User has privileges to Table A but not to Table B.  We checked that if a database user does not have the necessary privileges to access a table, they will not be able to view metadata information about foreign keys related to that table.  In this scenario, the refresh metadata query only shows information regarding table A. This is expected since it is only possible to access information in metadata tables ALL\_TABS\_COLS, ALL\_CONS\_COLUMNS and USER\_CONS\_COLUMNS to information regarding tables the user has access to.  We've also compared 2 scenarios to confirm if there was anything wrong with the metadata query if the user didn't had permissions to table B and we've managed to confirm that the time that the query takes is similar (~0.1s, for our tested scenario)&nbsp;  In summary, nothing fails getting the metadata if the user doesn't have priviliges on Table B.&nbsp;  
But there are some limitations because of it :&nbsp;*   FK aren&rsquo;t treated as such due to incomplete information in FK constrains.
*   Normal FK input validations not in place which can lead to query execution errors. Example:1.  User selects table A with FK to table B2.  Since user does not have permissions to table B and FK is a NUMBER(38,0) column will appear as a Text field.&nbsp;3.  Table A is added to outsystems application and is published.4.  In runtime, a User tries to create a record with incorrect input envolving letters in the FK field. Since the column was identified as text and table B is not present, the input is not validated.&nbsp;5.  Application returns in runtime error&nbsp;Because of this limitations, it is advisable that the user has privileges not only for the tables that he wants, but also for the tables that are related (through FKs and Constraints) to those tables.&nbsp;  
We will update our public documentation with this.&nbsp;  Regarding the problem that the user reported, we will wait for the DDL to be sent.
August 14 10:30 AM WESTwebRootlySend ZenDesk private comment has been unsetAugust 14 10:30 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

August 21 12:10 PM WESTwebRootly
The Global Support team marked this incident as closed in ZenDesk.
August 21 12:10 PM WESTwebRootly
Incident has been resolved
August 21 12:10 PM WESTwebRootlyZenDesk Event Type has been set: solved