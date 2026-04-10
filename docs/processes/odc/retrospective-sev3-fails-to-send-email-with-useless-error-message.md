---
title: Retrospective-SEV3-Fails to send email with useless error message.
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4335271969/Retrospective-SEV3-Fails+to+send+email+with+useless+error+message.
confluence_space: RKB
confluence_page_id: 4335271969
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV3-Fails to send email with useless error message.

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV3

Teams:&nbsp;trueBlueBackend Runtime
#### 🕐 Timestamps
Started At:&nbsp;trueBlueAugust 5  2:01 PM WEST

Mitigated At:&nbsp;trueYellowAugust 5  2:01 PM WEST

Resolved At:&nbsp;trueGreenAugust 5  2:01 PM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/724-fails-to-send-email-with-useless-error-message)
[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3033316)

#### Summary
----------------------------------------------**ISSUE DESCRIPTION AND HOW TO REPRODUCE**
Our PM colleague Andre facing some issues where endusers were having problems reseting the password due to error
&quot;OS-BERT-00000 - Object reference not set to an instance of an object.Stack:at ssInsured.Flows.FlowEmails.Emails_PasswordReset.GetEmailContentAsync(IRequestContext requestContext, String inParamVerificationCode, CancellationToken cancellationToken)   at ssInsured.Actions.ActionDoPasswordReset(IRequestContext requestContext, String inParamEmail, CancellationToken cancellationToken)   at ssInsured.ScreenServices.Insured_Common_RecoverPasswordRequest_Controller.&lt;ActionDoPasswordReset&gt;b__11_0(String screenName, JObject screenModel, JObject inputParameters, JObject clientVariables, CancellationToken cancellationToken)   at OutSystems.RESTService.Runtime.Core.Controllers.ScreenServices.ScreenServicesApiController.InnerEndpointAsync(String apiVersionHash, EndpointAsyncImplementationDelegate implementationAsync, ResponseVersionInfo responseVersionInfo, ServiceRequest requestPayload, CancellationToken cancellationToken)   at OutSystems.RESTService.Runtime.Core.Controllers.ScreenServices.ScreenServicesApiController.EndpointAsync(Stream input, String apiVersionHash, EndpointAsyncImplementationDelegate implementationAsync, CancellationToken cancellationToken)&quot;**IMPACT ON THE CUSTOMER**
Normal, affecting only endusers that are also IT/Organization users**TROUBLESHOOTING STEPS &amp; WORKAROUND**
We know this is expected behavior from past cases and escalations:- Since test an only end user as they have on their portal:- Return true and verification code:- ![](https://supportoutsystems.zendesk.com/attachments/token/1vsbJaSJ8qB58oZxen7Onlbm7/?name=image.png)
- With an organization user like Andre:- True but undefined:- ![](https://supportoutsystems.zendesk.com/attachments/token/dVsJcmAigPXWptpn69SnPMEo0/?name=image.png)- Since no verification code the validation of email fails:- ![](https://supportoutsystems.zendesk.com/attachments/token/wYvH54h0m5B01iLmu70DM9yRy/?name=image.png)This happens as in the past seen, since and quoting- Action isn't designed to work on users that have Organization Roles; we understand that you find this to be quite unintuitive, please allow us to explain our reasoning; this is done as a security measure, because if we allowed custom logic to reset the password for ODC Organization Members, an attacker might gain administrator access to the tenant by exploiting potential flaws in this custom logic. As such, we'll reiterate that, for users that have organization roles, then their passwords should always be reset using the &quot;forgot password?&quot; option in ODC Portal's.&quot;However, Andre was quite concern since the message outcome is not friendly for developers or end users, and also will be talking to Miguel Vicente this feedback. The purpose of this case is not for troubleshoot on R&amp;D side but to pass the feedback, that we should have this in public documentation and also improvement on the output error.**TECH DATA OR ANY OTHER RELEVANT INFO**
Ring: osall
Tenant Id: 8e142b7e-7a50-47a7-99bd-0161af259251
Tenant Prefix: os-int-pm-ring1
Region: us-east-1
KAG.TEJ.YPS.IRJ.KJ8.V8L.LVS.GOU_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 RetrospectiveinfoDetails
**Ring:** osall
**System-wide impact:**&nbsp; No
**Tenant ID:** 8e142b7e-7a50-47a7-99bd-0161af259251
**Tenant Prefix:** os-int-pm-ring1
**Routing Error Code:** OS-BERT
**Product Area:** -
### Impact:
Solved here: [https://outsystemsrd.atlassian.net/browse/RDINC-27283](https://outsystemsrd.atlassian.net/browse/RDINC-27283)
### Investigation and troubleshooting findings:
Solved here: [https://outsystemsrd.atlassian.net/browse/RDINC-27283](https://outsystemsrd.atlassian.net/browse/RDINC-27283)
### Resolution:
Solved here: [https://outsystemsrd.atlassian.net/browse/RDINC-27283](https://outsystemsrd.atlassian.net/browse/RDINC-27283)
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/724-fails-to-send-email-with-useless-error-message)

**Date**

**Source**

**User**

**Event**
July 18 12:40 PM WESTwebRootly
created an alert via
July 18 12:40 PM WESTwebRootly
Rootly created this incident
July 18 12:40 PM WESTwebRootly
In triage date has been set to July 18 12:40 PM WEST
July 18 12:50 PM WESTwebRootly
This incident was instantiated in Jira: RDINC-27283. Please work the incident using Rootly
July 18  1:40 PM WESTwebRootly
This incident was instantiated in Jira: RDINC-27283. Please work the incident using Rootly
July 19 11:12 AM WESTwebRootlyZenDesk Event Type has been set: solvedJuly 19 11:12 AM WESTwebRootly
The Global Support team marked this incident as closed in ZenDesk.
August 5  2:01 PM WESTwebRui Garcia
Incident has been started
August 5  2:01 PM WESTwebRui Garcia
Incident has been resolved
August 5  2:01 PM WESTwebRui GarciaSystem-wide impact has been set: NoAugust 5  2:01 PM WESTwebRui GarciaImpact has been set: Solved here: https://outsystemsrd.atlassian.net/browse/RDINC-27283August 5  2:01 PM WESTwebRui GarciaInvestigation and troubleshooting findings has been set: Solved here: https://outsystemsrd.atlassian.net/browse/RDINC-27283August 5  2:01 PM WESTwebRui GarciaResolution has been set: Solved here: https://outsystemsrd.atlassian.net/browse/RDINC-27283