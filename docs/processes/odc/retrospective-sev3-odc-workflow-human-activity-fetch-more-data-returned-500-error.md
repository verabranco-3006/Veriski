---
title: Retrospective-SEV3-ODC workflow human activity Fetch more data returned 500 error
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4394254384/Retrospective-SEV3-ODC+workflow+human+activity+Fetch+more+data+returned+500+error
confluence_space: RKB
confluence_page_id: 4394254384
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV3-ODC workflow human activity Fetch more data returned 500 error

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV3

Teams:&nbsp;trueBlueModel 

Types:&nbsp;trueBlueCustomer Escalated
#### 🕐 Timestamps
Started At:&nbsp;trueBlueAugust 21  2:04 PM WEST

Mitigated At:&nbsp;trueYellowAugust 29  9:10 AM WEST

Resolved At:&nbsp;trueGreenAugust 29  9:10 AM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/905-odc-workflow-human-activity-fetch-more-data-returned-500-error)
[Pagerduty incident](https://outsystems.pagerduty.com/incidents/Q2AEVMR9FYVH4U)

[Slack channel](https://slack.com/app_redirect?channel=C07HGV0DYUW&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3051213)

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

Jos&eacute; Santos
#### Summary
----------------------------------------------**ISSUE DESCRIPTION AND HOW TO REPRODUCE**
ODC workflow is throwing an error OS-CORE-HOST-50001 at console level.
The customer needs to fetch more data to get the User ID to be used in the Assign To.
In EA simply try to fetch more data on the workflow and will return the error:- ![](https://supportoutsystems.zendesk.com/attachments/token/lLUdxRLabYUnFOztkDAGv1WaX/?name=image.png)**IMPACT ON THE CUSTOMER**
High, reaching deadline of partner in order to know if ODC will be a good choice to apply for ODC license for future customer**TROUBLESHOOTING STEPS &amp; WORKAROUND**
We replicate the error on customer tenant and grab the error:- ![](https://supportoutsystems.zendesk.com/attachments/token/DKX3nXh12ENa0BWmNcnZiqfCx/?name=image.png)- Looking at error we have documentation:- https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/3845228620/Runbook+Connections+console+-+OS-CORE-HOST-50001- OS-CORE-HOST-50001 is a &ldquo;catch-all&rdquo; error code..... Because this error code means an unexpected error occurred in an external service, you can follow the recommended actions for OS-INTC-API-50001 - Unknow error calling API.- The error sees happening calling an API:-   Error: Internal Server Error at ModelServicesApiResponseProcessor.updateProperty at async ModelService.innerExecuteModelUpdate at (anonymous function) at async ChangeTrackerService.track at async ModelService.executeModelUpdate at async ModelService.dispatchObjectPropertiesUpdates [as taskHandler] at (anonymous function) at (anonymous function)- Further looking at error, we indeed have a trace:- ![](https://supportoutsystems.zendesk.com/attachments/token/fX5DrGChhVL7ETZU98wPBqk9l/?name=image.png)- We have another dash where we can look this specific traces:- https://outsystems.grafana.net/d/edrbd45jvycqod/logs-raw?var-Username=&amp;var-WebSessionId=&amp;var-WorkspaceSessionId=&amp;var-TraceId=00-a04880cb4f22c690f3bbb7d159ec101a-770c186953fbffee-01&amp;var-ProductVersion=&amp;var-search=&amp;var-ring=ea&amp;var-stamp=$__all&amp;var-level=ERROR&amp;var-level=FATAL&amp;var-level=DEBUG&amp;var-level=$__all&amp;var-level=INFO&amp;var-level=WARN&amp;from=2024-08-18T23:00:00.000Z&amp;to=2024-08-19T22:59:59.000Z&amp;timezone=browser- ![](https://supportoutsystems.zendesk.com/attachments/token/bmxAlGJyplqDDTbIAcfdcCcR6/?name=image.png)- Where we can get all details like websession etc., but is the only error no warning or info associated.- Looking internal doc -&gt; https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/3717366496/Runbook+Connections+console+-+OS-INTC-API-50001+-+Unknow+error+calling+API- We follow this path:- ![](https://supportoutsystems.zendesk.com/attachments/token/XI4PH6DlCOJloQ7Dn58xAfLzI/?name=image.png)- 00-6d10d7f1f276b9bfcc4e1a8ff7209d68-0474335359d2cc94-01- ConnectionId&quot;:&quot;0HN5SNHKO4M9E- And we have new data:- https://outsystems.grafana.net/explore?schemaVersion=1&amp;panes=%7B%220nl%22:%7B%22datasource%22:%22grafanacloud-outsystemstest-traces%22,%22queries%22:%5B%7B%22refId%22:%22B%22,%22datasource%22:%7B%22type%22:%22tempo%22,%22uid%22:%22grafanacloud-outsystemstest-traces%22%7D,%22queryType%22:%22traceql%22,%22limit%22:20,%22tableType%22:%22traces%22,%22query%22:%22a04880cb4f22c690f3bbb7d159ec101a%22%7D%5D,%22range%22:%7B%22from%22:%221724022000000%22,%22to%22:%221724108399000%22%7D%7D%7D&amp;orgId=1- Where we have a 500:- ![](https://supportoutsystems.zendesk.com/attachments/token/CZVRaCweYVjMnqwcmVnIi745M/?name=image.png)- ![](https://supportoutsystems.zendesk.com/attachments/token/5WX6lzqc0wcweZgscOvg0BYvq/?name=image.png)- We are getting a 500 to &quot;IDEServices.Server.Gateway&quot; service, and looking at CF level we have the 500:- https://outsystems.grafana.net/d/6-6x5IF4k/cloudfront-logs?orgId=1&amp;var-host=dbizodc.outsystems.dev&amp;var-search=&amp;var-environment=prod&amp;var-data_source=MWYvlds7z&amp;var-method=$__all&amp;var-status_code=5%5B0-9%5D%5B0-9%5D&amp;var-edge_response_type=$__all&amp;var-plat_s3=s3%2Flogs-plat-edge-ue1-prod-rn-cloudrd-os&amp;var-run_s3=s3%2Flogs-run-edge-ue1-prod-rn-cloudrd-os&amp;var-cus_s3=s3%2Flogs-cus-edge-ue1-prod-rn-cloudrd-os&amp;from=2024-08-18T23:00:00.000Z&amp;to=2024-08-19T22:59:59.000Z- ![](https://supportoutsystems.zendesk.com/attachments/token/cHWKi6trQEuOiNw6awwDb5F7u/?name=image.png)- However, grabbing the connection ID on Data Service Didn't find any logs:- ![](https://supportoutsystems.zendesk.com/attachments/token/c8Rd2bIegxndUnh9sNl3zWFgt/?name=image.png)To jeopardize any logic bad constructed at workflow level, I copy the producer App from customer and publish on GA, then create a Workflow exactly like customer and issue doesn't occur:- ![](https://supportoutsystems.zendesk.com/attachments/token/IunyI38V0K4OpEaDj784noA56/?name=image.png)At the customer side on EA the same workflow indeed return error- ![](https://supportoutsystems.zendesk.com/attachments/token/ZCDINp9PIbzakcr9VFrdX9Jxy/?name=image.png)With this we can conclude the issue is affecting EA but not GA, since we can see at CF level the 200 on the updateProperty on GA:- ![](https://supportoutsystems.zendesk.com/attachments/token/sD6iZukyidML5Wb9cDQrMpjS6/?name=image.png)The 500 on the code seems only a reply:- ![](https://supportoutsystems.zendesk.com/attachments/token/DaVmYDwbfagoVRGNW87kCb8VO/?name=image.png)Due to that we are escalating to R&amp;D since we think there might be a bug on EA ring, however, we also would like to know what can we do in these scenarios to know more information and guidance on how to do it.**TECH DATA OR ANY OTHER RELEVANT INFO**
Ring: ea
Tenant Id: cfbde777-cd15-47b5-b244-9f7b67989dfa
Tenant Prefix: dbizodc
Region: ap-southeast-1
ZIF.3PB.JSQ.OKK.UWA.RLF.BPH.WUT_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 RetrospectiveinfoDetails
**Ring:** ea
**System-wide impact:**&nbsp; No
**Tenant ID:** cfbde777-cd15-47b5-b244-9f7b67989dfa
**Tenant Prefix:** dbizodc
**Routing Error Code:** N/A
**Product Area:** Phoenix::Web Editors::Workflow Editor
### Impact:
User couldn't add new activity data in a human activity node
### Investigation and troubleshooting findings:
We've fixed an error on the existing arguments rebind when a new activity data is added
### Resolution:
We've fixed an error on the existing arguments rebind when a new activity data is added
## Tasks performed during incident resolution:
**Summary:** An incident has been updated!

**Status:**trueBlueopen

&nbsp;
## Executive Summary
[Guidelines](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4144496679/Incident+Retrospectives+-+Playbook#STEP-3---Write-the-Executive-Summary)
## Root Causes 
[Guidelines](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4144496679/Incident+Retrospectives+-+Playbook#STEP-1---Perform-the-Root-Cause-Analysis)

If the customer needs formal RCA, please fill out the following field with the document URL

[Please follow these instructions and place the RCA URL in the field below.](https://docs.google.com/document/d/13rXmBsOJh73nV2D6Z17SIBGBu2HOTWty5ddsvU000JM/edit#heading=h.bqxasxszr5q)

RCA URL

&lt;Place the URL of the customer RCA here if you have created one&gt;
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/905-odc-workflow-human-activity-fetch-more-data-returned-500-error)

**Date**

**Source**

**User**

**Event**
August 20  2:31 PM WESTwebRootly
created an alert via
August 20  2:31 PM WESTwebRootly
Rootly created this incident
August 20  2:31 PM WESTwebRootly
In triage date has been set to August 20  2:31 PM WEST
August 20  2:31 PM WESTwebRootly[Slack Channel](https://slack.com/app_redirect?channel=C07HGV0DYUW&amp;team=T041063TZ) has been createdAugust 20  2:31 PM WESTwebRootly
Ring: ea
System-wide impact:  
Tenant ID: cfbde777-cd15-47b5-b244-9f7b67989dfa
Tenant Prefix: dbizodc
Routing Error Code: N/A
Product Area: Phoenix::Web Editors::Workflow Editor
August 20  2:32 PM WESTwebRootly[PagerDuty Incident](https://outsystems.pagerduty.com/incidents/Q2AEVMR9FYVH4U) has been created.
📲 Notified Jos&eacute; dos Santos by push notification.  (via Android)&nbsp;&nbsp;📧 Notified Jos&eacute; dos Santos by email.August 20  2:32 PM WESTwebRootlyJos&eacute; Santos has been assigned as EngineerAugust 20  2:34 PM WESTwebRootly
Jos&eacute; dos Santos acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q2AEVMR9FYVH4U). (via Phone)
August 20  2:41 PM WESTwebRootly
This incident was instantiated in Jira: RDINC-28843. Please work the incident using Rootly
August 20  2:49 PM WESTwebRootlyZendesk Private Comment has been set: ----------------------------------------------**Update to R&amp;D**
Hello team,Apologize for message but there seems to be a bug on rootly where if there is high level bullet list the info doesn't appear so it misses part of my investigation regarding the traces:
Its between the image of R&amp;D documentation &quot;Unknown Errors&quot; and the image of Connection Id On Data Service Dashboard, in Jira is correctly set, will also report to appropriate teams.- 00-6d10d7f1f276b9bfcc4e1a8ff7209d68-0474335359d2cc94-01
- ConnectionId&quot;:&quot;0HN5SNHKO4M9E
- And we have new data:- https://outsystems.grafana.net/explore?schemaVersion=1&amp;panes=%7B%220nl%22:%7B%22datasource%22:%22grafanacloud-outsystemstest-traces%22,%22queries%22:%5B%7B%22refId%22:%22B%22,%22datasource%22:%7B%22type%22:%22tempo%22,%22uid%22:%22grafanacloud-outsystemstest-traces%22%7D,%22queryType%22:%22traceql%22,%22limit%22:20,%22tableType%22:%22traces%22,%22query%22:%22a04880cb4f22c690f3bbb7d159ec101a%22%7D%5D,%22range%22:%7B%22from%22:%221724022000000%22,%22to%22:%221724108399000%22%7D%7D%7D&amp;orgId=1- Where we have a 500:- ![](https://supportoutsystems.zendesk.com/attachments/token/CZVRaCweYVjMnqwcmVnIi745M/?name=image.png)- ![](https://supportoutsystems.zendesk.com/attachments/token/5WX6lzqc0wcweZgscOvg0BYvq/?name=image.png)- We are getting a 500 to &quot;IDEServices.Server.Gateway&quot; service, and looking at CF level we have the 500:- https://outsystems.grafana.net/d/6-6x5IF4k/cloudfront-logs?orgId=1&amp;var-host=dbizodc.outsystems.dev&amp;var-search=&amp;var-environment=prod&amp;var-data_source=MWYvlds7z&amp;var-method=$__all&amp;var-status_code=5%5B0-9%5D%5B0-9%5D&amp;var-edge_response_type=$__all&amp;var-plat_s3=s3%2Flogs-plat-edge-ue1-prod-rn-cloudrd-os&amp;var-run_s3=s3%2Flogs-run-edge-ue1-prod-rn-cloudrd-os&amp;var-cus_s3=s3%2Flogs-cus-edge-ue1-prod-rn-cloudrd-os&amp;from=2024-08-18T23:00:00.000Z&amp;to=2024-08-19T22:59:59.000Z- ![](https://supportoutsystems.zendesk.com/attachments/token/cHWKi6trQEuOiNw6awwDb5F7u/?name=image.png)__August 20  2:49 PM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
Hello team,Apologize for message but there seems to be a bug on rootly where if there is high level bullet list the info doesn't appear so it misses part of my investigation regarding the traces:
Its between the image of R&amp;D documentation &quot;Unknown Errors&quot; and the image of Connection Id On Data Service Dashboard, in Jira is correctly set, will also report to appropriate teams.- 00-6d10d7f1f276b9bfcc4e1a8ff7209d68-0474335359d2cc94-01
- ConnectionId&quot;:&quot;0HN5SNHKO4M9E
- And we have new data:- https://outsystems.grafana.net/explore?schemaVersion=1&amp;panes=%7B%220nl%22:%7B%22datasource%22:%22grafanacloud-outsystemstest-traces%22,%22queries%22:%5B%7B%22refId%22:%22B%22,%22datasource%22:%7B%22type%22:%22tempo%22,%22uid%22:%22grafanacloud-outsystemstest-traces%22%7D,%22queryType%22:%22traceql%22,%22limit%22:20,%22tableType%22:%22traces%22,%22query%22:%22a04880cb4f22c690f3bbb7d159ec101a%22%7D%5D,%22range%22:%7B%22from%22:%221724022000000%22,%22to%22:%221724108399000%22%7D%7D%7D&amp;orgId=1- Where we have a 500:- ![](https://supportoutsystems.zendesk.com/attachments/token/CZVRaCweYVjMnqwcmVnIi745M/?name=image.png)- ![](https://supportoutsystems.zendesk.com/attachments/token/5WX6lzqc0wcweZgscOvg0BYvq/?name=image.png)- We are getting a 500 to &quot;IDEServices.Server.Gateway&quot; service, and looking at CF level we have the 500:- https://outsystems.grafana.net/d/6-6x5IF4k/cloudfront-logs?orgId=1&amp;var-host=dbizodc.outsystems.dev&amp;var-search=&amp;var-environment=prod&amp;var-data_source=MWYvlds7z&amp;var-method=$__all&amp;var-status_code=5%5B0-9%5D%5B0-9%5D&amp;var-edge_response_type=$__all&amp;var-plat_s3=s3%2Flogs-plat-edge-ue1-prod-rn-cloudrd-os&amp;var-run_s3=s3%2Flogs-run-edge-ue1-prod-rn-cloudrd-os&amp;var-cus_s3=s3%2Flogs-cus-edge-ue1-prod-rn-cloudrd-os&amp;from=2024-08-18T23:00:00.000Z&amp;to=2024-08-19T22:59:59.000Z- ![](https://supportoutsystems.zendesk.com/attachments/token/cHWKi6trQEuOiNw6awwDb5F7u/?name=image.png)__
August 20  3:31 PM WESTwebRootly
This incident was instantiated in Jira: RDINC-28843. Please work the incident using Rootly
August 20  3:45 PM WESTwebJos&eacute; Santos
Incident has been started
August 20  3:45 PM WESTwebRootly
Pagerduty Integrations acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q2AEVMR9FYVH4U). (via Phone)
August 21  9:46 AM WESTwebJos&eacute; Santos
Incident is in triage
August 21 11:26 AM WESTslackteresa.marcelino**Workaround for the client:**
&bull; Open the latest revision of the workflow through the Portal.
&bull; Under the Human Activity that is currently in error, add a new Human Activity node.
&bull; Apply the same properties (display name, close on event, display screen) as the Human Activity in error.
&bull; Add the required &quot;fetch more data&quot; functionality to the new Human Activity.
&bull; Delete the Human Activity that is in error.
&bull; Confirm that client can publish the workflow and that there are no further issues.August 21  2:04 PM WESTwebTeresa Marcelino
Incident has been started
August 21  2:04 PM WESTwebRootly
Pagerduty Integrations acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q2AEVMR9FYVH4U). (via Phone)
August 21  7:26 PM WESTwebRootlyAccess Zendesk ticket (VPN) has been set: https://extranetinternalapps-prd.outsystems.net/TKT_CustomerTicket_UI/CustomerTicket_Detail?TicketITSMId=3051213August 22  1:02 PM WESTslackteresa.marcelino
On the morning of August 21st, the workaround was sent to the client. However, we have not yet received feedback from them, even after support tried to contact them this morning.
August 22  3:51 PM WESTslackteresa.marcelino
Created RFC to access workflow OML [https://outsystemsrd.atlassian.net/browse/RFC-1349](https://outsystemsrd.atlassian.net/browse/RFC-1349)
August 22  3:53 PM WESTslackteresa.marcelino
Created RFC to recover Binary files from S3 - [https://outsystemsrd.atlassian.net/browse/RFC-1349](https://outsystemsrd.atlassian.net/browse/RFC-1349)
August 22  6:56 PM WESTslackteresa.marcelino
Runbook to Create RFC to retrieve IDE.Service Session Files - [https://outsystemsrd.atlassian.net/wiki/spaces/Morpheus/pages/4381376673/Runbook+-+Create+RFC+to+retrieve+IDE.Service+Session+Files](https://outsystemsrd.atlassian.net/wiki/spaces/Morpheus/pages/4381376673/Runbook+-+Create+RFC+to+retrieve+IDE.Service+Session+Files)
August 23 10:00 AM WESTslackteresa.marcelino
Observing the logs, it seems that the user was able to test the suggested workaround, deleting the node and creating a new human activity.  [Workflow Logs](https://outsystems.grafana.net/d/edrbd45jvycqod/logs-raw?var-Username=&amp;var-WebSessionId=&amp;var-WorkspaceSessionId=&amp;var-TraceId=&amp;var-ProductVersion=&amp;var-search=cfbde777-cd15-47b5-b244-9f7b67989dfa&amp;var-ring=ea&amp;var-stamp=$__all&amp;var-level=$__all&amp;var-Filters=&amp;from=2024-08-22T23:00:00.000Z&amp;to=2024-08-23T22:59:59.000Z&amp;timezone=browser)
August 23 10:14 AM WESTslackteresa.marcelino
Client added a new automatic activity instead of a new human activity, so the workaround hasn't been applied yet
August 23 10:43 AM WESTwebRootlyZendesk Private Comment has been changed to: ----------------------------------------------**Update to R&amp;D**
Hello team,Hope everything is fine and safe.As discussed internally since we found a workaround and was already shared with costumer we agree to reassess to Normal, Sev3.
Even that costumer didn't reach us, or we were able to get them, we will proceed this way.Best regards,_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_August 23 10:43 AM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
Hello team,Hope everything is fine and safe.As discussed internally since we found a workaround and was already shared with costumer we agree to reassess to Normal, Sev3.
Even that costumer didn't reach us, or we were able to get them, we will proceed this way.Best regards,__
August 26  9:19 AM WESTwebRootlyZendesk Private Comment has been changed to: ----------------------------------------------**Update to R&amp;D**
Hello team,Hope this communication finds everyone fine.We would like to share the workaround is successfully, and the case can be reassessed (we already reassess to Sev3 on our side, however, discussing with Teresa, it seems on rootly side is not being performed, I already engage Miguel Afonso from rootly team to investigate, however, didn't have a reply yet, so maybe reassess manually on rootly on your side).Nevertheless, customer is concern about this situation, since they are very involved on this feature to present to potential customers and we would like to know the following:- Its possible to know more details about the cause of it? From the previous discussion seems there was a &quot;corruption&quot; on the node.
- Also, will be there any improvements on our side to prevent this from happening again?Best regards,_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_August 26  9:19 AM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
Hello team,Hope this communication finds everyone fine.We would like to share the workaround is successfully, and the case can be reassessed (we already reassess to Sev3 on our side, however, discussing with Teresa, it seems on rootly side is not being performed, I already engage Miguel Afonso from rootly team to investigate, however, didn't have a reply yet, so maybe reassess manually on rootly on your side).Nevertheless, customer is concern about this situation, since they are very involved on this feature to present to potential customers and we would like to know the following:- Its possible to know more details about the cause of it? From the previous discussion seems there was a &quot;corruption&quot; on the node.
- Also, will be there any improvements on our side to prevent this from happening again?Best regards,__
August 26  9:19 AM WESTwebRootlyZendesk Private Comment has been changed to: ------------------------------------------------ This notification was sent from Zendesk Support ticket #3051213 to all linked JIRA issues by Cristiano Costa. --**Update to R&amp;D**
Hello team,Hope this communication finds everyone fine.We would like to share the workaround is successfully, and the case can be reassessed (we already reassess to Sev3 on our side, however, discussing with Teresa, it seems on rootly side is not being performed, I already engage Miguel Afonso from rootly team to investigate, however, didn't have a reply yet, so maybe reassess manually on rootly on your side).Nevertheless, customer is concern about this situation, since they are very involved on this feature to present to potential customers and we would like to know the following:- Its possible to know more details about the cause of it? From the previous discussion seems there was a &quot;corruption&quot; on the node.
- Also, will be there any improvements on our side to prevent this from happening again?Best regards,_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_August 26  9:19 AM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
------------------------------------------------ This notification was sent from Zendesk Support ticket #3051213 to all linked JIRA issues by Cristiano Costa. --**Update to R&amp;D**
Hello team,Hope this communication finds everyone fine.We would like to share the workaround is successfully, and the case can be reassessed (we already reassess to Sev3 on our side, however, discussing with Teresa, it seems on rootly side is not being performed, I already engage Miguel Afonso from rootly team to investigate, however, didn't have a reply yet, so maybe reassess manually on rootly on your side).Nevertheless, customer is concern about this situation, since they are very involved on this feature to present to potential customers and we would like to know the following:- Its possible to know more details about the cause of it? From the previous discussion seems there was a &quot;corruption&quot; on the node.
- Also, will be there any improvements on our side to prevent this from happening again?Best regards,__
August 27  9:16 AM WESTwebTeresa Marcelino
Severity has been changed from SEV2 to SEV3
August 27 10:46 AM WESTslackteresa.marcelino
Request to SRE to access the Binary files from S3files:
[https://outsystemsrd.atlassian.net/servicedesk/customer/portal/31/RDSCRESM-414?created=true](https://outsystemsrd.atlassian.net/servicedesk/customer/portal/31/RDSCRESM-414?created=true)
August 27 11:32 AM WESTwebTeresa MarcelinoSend ZenDesk private comment has been set: Good morning,
We are currently investigating the issue and enhancing our test coverage to prevent a recurrence. We will provide further updates as soon as we have more information.
Thank you for your patienceAugust 27 11:32 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Good morning,
We are currently investigating the issue and enhancing our test coverage to prevent a recurrence. We will provide further updates as soon as we have more information.
Thank you for your patience
August 27 11:32 AM WESTwebRootlySend ZenDesk private comment has been unsetAugust 27 11:32 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

August 27  5:41 PM WESTslackteresa.marcelino
We were able to reproduce the issue with the client's oml locally in the human activity in error. We passed the context to model service team.
August 28 10:39 AM WESTwebTeresa Marcelino
Teams has been added: Model 
August 28 10:39 AM WESTwebTeresa Marcelino
Teams has been removed: Workflow Editor
August 29  8:50 AM WESTwebRuben MarrufoSend ZenDesk private comment has been set: Hi team! We've found the issue root cause and fixed it. The ManualIntervention node seems to have contained some activity data calling to some Service Action with parameters that was then, later on, removed. When we remove it, the arguments, which are the values that we pass to the action parameters, are kept, they are not removed with the action. This is a normal behavior in OutSystems. Then, if the user adds as activity data another Service Action, the app tries to validate the existing arguments. It was that validation that was leading to the error that the user was reporting and we have already fixed. Thanks!August 29  8:50 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hi team! We've found the issue root cause and fixed it. The ManualIntervention node seems to have contained some activity data calling to some Service Action with parameters that was then, later on, removed. When we remove it, the arguments, which are the values that we pass to the action parameters, are kept, they are not removed with the action. This is a normal behavior in OutSystems. Then, if the user adds as activity data another Service Action, the app tries to validate the existing arguments. It was that validation that was leading to the error that the user was reporting and we have already fixed. Thanks!
August 29  8:50 AM WESTwebRootlySend ZenDesk private comment has been unsetAugust 29  8:50 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

August 29  9:10 AM WESTwebRuben Marrufo
Incident has been resolved
August 29  9:10 AM WESTwebRuben MarrufoSystem-wide impact has been set: NoAugust 29  9:10 AM WESTwebRuben MarrufoImpact has been set: User couldn't add new activity data in a human activity nodeAugust 29  9:10 AM WESTwebRuben MarrufoInvestigation and troubleshooting findings has been set: We've fixed an error on the existing arguments rebind when a new activity data is addedAugust 29  9:10 AM WESTwebRuben MarrufoResolution has been set: We've fixed an error on the existing arguments rebind when a new activity data is addedAugust 29  9:10 AM WESTwebRootly
Pagerduty Integrations marked the incident as resolved through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q2AEVMR9FYVH4U). (via Api)