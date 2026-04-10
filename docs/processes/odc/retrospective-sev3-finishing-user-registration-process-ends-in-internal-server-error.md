---
title: Retrospective-SEV3-Finishing user registration process ends in internal server error
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4356636690/Retrospective-SEV3-Finishing+user+registration+process+ends+in+internal+server+error
confluence_space: RKB
confluence_page_id: 4356636690
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV3-Finishing user registration process ends in internal server error

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV3

Teams:&nbsp;trueBlueClient Runtime
#### 🕐 Timestamps
Started At:&nbsp;trueBlueJuly 22  8:56 AM WEST

Mitigated At:&nbsp;trueYellowAugust 13  8:14 AM WEST

Resolved At:&nbsp;trueGreenAugust 13  8:14 AM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/740-finishing-user-registration-process-ends-in-internal-server-error)
[Slack channel](https://slack.com/app_redirect?channel=C07EAJX38F2&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3038244)

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

David Pires
#### Summary
----------------------------------------------**CONSIDERATIONS BEFORE PERFORMING THE ESCALATION TO R&amp;D (MANDATORY)**
None of the below points should be overlooked. Failure to do so may imply unnecessary effort.* * *
Ensure the ticket has been **categorized**, otherwise, the R&amp;D escalation will go unnoticed and not be worked on!**1.** For **Incidents**, the **IMAX** was consulted **beforehand** on which:- No incident models were found for the reported symptoms **OR**
- The incident model did not solve the issue **OR**
- The next step indicated in the Incident Model is an escalation to R&amp;D.
**2.** For **Questions**, the ChatODC on the **Slack channel** didn't return an acceptable answer.
**3.** Any other requests that explicitly indicate an R&amp;D escalation is needed.
**4**. **Incident impact assessment** was based on the **prioritization scoring matrix**.* * ***R&amp;D ESCALATION FORM**
Section comments can be removed for R&amp;D easier interpretation.**ISSUE DESCRIPTION AND HOW TO REPRODUCE**
The scenario is like this:-The customer has a way of creating users, where other users can invite people to the app.- Inside the server logic,
1) they call the StartUserRegistration action and
2) send an invitation with the verification code to the reported email address and
3) log the email address in a extended table of Users (with UserId as primary key).- When following the link in the invitation, users are asked to set a new password after which the FinishUserRegistration action is called.
- When the verification code is expired (beyond the 15 mins), the user is getting this vague error- ![](https://supportoutsystems.zendesk.com/attachments/token/eUm7BW1KOaxtrbHKReM5gPKP5/?name=image.png)**IMPACT ON THE CUSTOMER**
Normal.**TROUBLESHOOTING STEPS &amp; WORKAROUND**- We can see a few occurrences of this error in the customer Portal:
- ![](https://supportoutsystems.zendesk.com/attachments/token/ozHlF46jiSf3TgbIdV6kHnNic/?name=image.png)- Stack:
- `OS-CLRT-40100 - Error getting temporary password`
`POST /Service2PotatoWeb/moduleservices/users/registration - 500`
- `at dr.&lt;anonymous&gt; (https://service2-dev.outsystems.app/Service2PotatoWeb/scripts/outsystems-communication__5qqkdLIMsjBn97G3BeBMaQ.js?5qqkdLIMsjBn97G3BeBMaQ:1:47543) at s (https://service2-dev.outsystems.app/Service2PotatoWeb/scripts/outsystems-communication__5qqkdLIMsjBn97G3BeBMaQ.js?5qqkdLIMsjBn97G3BeBMaQ:1:379) at i.invoke (https://service2-dev.outsystems.app/Service2PotatoWeb/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:26029) at r.run (https://service2-dev.outsystems.app/Service2PotatoWeb/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:21220) at https://service2-dev.outsystems.app/Service2PotatoWeb/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:15930 at i.invokeTask (https://service2-dev.outsystems.app/Service2PotatoWeb/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:26647) at r.runTask (https://service2-dev.outsystems.app/Service2PotatoWeb/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:21972) at g (https://service2-dev.outsystems.app/Service2PotatoWeb/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:28692)`- When looking into the Identity Logs, I find the following error:Error\tTraceID = | Body = Failed to Self Register User with email: m***4@trader.nl - error OS-ID-BIZ-40052[&hellip;]The action token with id :2ffdf576-17fb-4bff-a7ca-8e48a3df4f6d is already expired- We can also see in the grafana dashboard- https://outsystems.grafana.net/d/cdeqzn1jj77cwe/general-troubleshooting?orgId=1&amp;var-ring=ga&amp;var-tenant=083a4a6e-f4b9-4358-b568-485ea1c99217&amp;var-application=All&amp;var-cluster=All&amp;var-cluster_old=All&amp;var-severity=All&amp;var-runtime=All&amp;var-filter=&amp;var-exclude=&amp;var-region=eu-central-1&amp;var-traceDuration=All&amp;var-environment=All&amp;var-regionShort=ga-eu-ce-1-01&amp;var-tenant_prefix=service2&amp;var-module_name=&amp;from=1721378700000&amp;to=1721378939000- ![](https://supportoutsystems.zendesk.com/attachments/token/lpw83lvfH5H28vfqZu4A8uODD/?name=image.png)- The action token is already expired.- Upon testing on a sample application on our end, we were able to confirm that, when using a verification code that was already expired, all attributes of the structure &quot;FinishUserRegistrationFailureReason&quot; are &quot;false&quot;, so this may be the reason why:
- ![](https://supportoutsystems.zendesk.com/attachments/token/QXEycYr3VDNbQ5d2blbjJlNzF/?name=image.png) ![](https://supportoutsystems.zendesk.com/attachments/token/9SgcWIQKIgFcc0TrEhoz4Ozpe/?name=image.png)
- ![](https://supportoutsystems.zendesk.com/attachments/token/uhf0s3iFVNqUU4acjdNukXGHt/?name=image.png)- Our expectation is that one of the attributes of the &quot;FinishUserRegistrationFailureReason&quot; structure to return true, specifically &quot;InvalidVerificationCode&quot;, so that the end user an be appropriately informed.**TECH DATA OR ANY OTHER RELEVANT INFO****Ring**: ga
**Tenant Id**: 083a4a6e-f4b9-4358-b568-485ea1c99217
**Tenant Prefix**: service2
**Region**: eu-central-1_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 RetrospectiveinfoDetails
**Ring:** ga
**System-wide impact:**&nbsp; 
**Tenant ID:** 083a4a6e-f4b9-4358-b568-485ea1c99217
**Tenant Prefix:** service2
**Routing Error Code:** OS-CLRT
**Product Area:** -
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/740-finishing-user-registration-process-ends-in-internal-server-error)

**Date**

**Source**

**User**

**Event**
July 22  4:31 AM WESTwebRootly
created an alert via
July 22  4:31 AM WESTwebRootly
Rootly created this incident
July 22  4:31 AM WESTwebRootly
In triage date has been set to July 22  4:31 AM WEST
July 22  4:41 AM WESTwebRootly
This incident was instantiated in Jira: RDINC-27470. Please work the incident using Rootly
July 22  5:31 AM WESTwebRootly
This incident was instantiated in Jira: RDINC-27470. Please work the incident using Rootly
July 22  8:56 AM WESTwebDavid Pires
Incident has been started
July 22 10:04 AM WESTwebDavid Pires
Detected that call to endpoint to create new user temporary password, doesn't return the expected error for invalid code
July 22 11:16 AM WESTwebDavid Pires
To detected if the verification code is invalid, we check for codes: &quot;OS-ID-BIZ-40001&quot;,&quot;OS-ID-BIZ-40051&quot;,&quot;OS-ID-BIZ-50047&quot;,&quot;OS-ID-BIZ-40415&quot;,&quot;OS-ID-BIZ-40052&quot;,
But now, identity returns the error code: &quot;OS-ID-BIZ-40401&quot;
July 22 11:18 AM WESTwebDavid Pires
Teams has been added: Identity Business
July 22 11:18 AM WESTwebDavid Pires
Teams has been removed: Client Runtime
July 23 11:23 AM WESTwebRootly[Slack Channel](https://slack.com/app_redirect?channel=C07EAJX38F2&amp;team=T041063TZ) has been createdJuly 23  3:41 PM WESTwebLoredana-Gabriela NegoitaLoredana-Gabriela Negoita has been assigned as EngineerJuly 23  4:11 PM WESTwebLoredana-Gabriela NegoitaSend ZenDesk private comment has been set: Hello team,  Can you please provide the full email of the user to us?  We were performing some tests on our side and it worked fine. From Identity Business side, the 40052 error behaved as expected, but Client Runtime said the error displayed in the UI was generated by a User NotFound. We were not able to find the NotFound errors for the user that reported this.  For Client Runtime, they were able to replicate the NotFound, but now with a retry everything worked. So could you please ask the customer to retry while we are still investigating this?  Thank you!July 23  4:11 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hello team,  Can you please provide the full email of the user to us?  We were performing some tests on our side and it worked fine. From Identity Business side, the 40052 error behaved as expected, but Client Runtime said the error displayed in the UI was generated by a User NotFound. We were not able to find the NotFound errors for the user that reported this.  For Client Runtime, they were able to replicate the NotFound, but now with a retry everything worked. So could you please ask the customer to retry while we are still investigating this?  Thank you!
July 23  4:11 PM WESTwebRootlySend ZenDesk private comment has been unsetJuly 23  4:11 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

July 25  9:47 AM WESTwebLoredana-Gabriela NegoitaSend ZenDesk private comment has been set: Hello team,One thing that is not clear to us is if this client is blocked in any way.
If they use a valid verification code, are they able to register?In the meantime, we confirmed everything works as expected on Identity Business side and we will be moving the ticket to Client Runtime.Best regardsJuly 25  9:47 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hello team,One thing that is not clear to us is if this client is blocked in any way.
If they use a valid verification code, are they able to register?In the meantime, we confirmed everything works as expected on Identity Business side and we will be moving the ticket to Client Runtime.Best regards
July 25  9:47 AM WESTwebRootlySend ZenDesk private comment has been unsetJuly 25  9:47 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

July 25  9:49 AM WESTwebLoredana-Gabriela Negoita
So as discussed in the meeting, we are going to move this ticket to Client Runtime. The customer retried on their side and as seen in the logs, they are receiving the expected error: https://outsystems.grafana.net/explore?schemaVersion=1&amp;panes=%7B%22u61%22:%7B%22datasour[&hellip;]from%22:%22now-24h%22,%22to%22:%22now%22%7D%7D%7D&amp;orgId=1
https://outsystems.grafana.net/explore?schemaVersion=1&amp;panes=%7B%22u61%22:%7B%22datasour[&hellip;]2from%22:%22now-2d%22,%22to%22:%22now%22%7D%7D%7D&amp;orgId=1
July 25  9:50 AM WESTwebLoredana-Gabriela Negoita
Teams has been added: Client Runtime
July 25  9:50 AM WESTwebLoredana-Gabriela Negoita
Teams has been removed: Identity Business
July 25  1:57 PM WESTwebRootlyZendesk Private Comment has been set: ----------------------------------------------**Update to R&amp;D**
Hi again team,All right, let me try to clear up the confusion, since I believe a lot of noise was introduced in this incident.There is nothing wrong with the user registration: users are able to complete the registration if the code is still valid, and fail when the code is expired (past 15 minutes).The point here is that, when the registration fails because of an expired verification code, the failure reason **InvalidVerificationCode** does not seem to be correctly filled with **True**. Thus, the customer cannot determine what was the failure reason and cannot present users with a message indicating that the code expired and that they must retry - this is what is 'blocking' them.Furthermore, they claim that they had previously developed and tested the flow under the assumption that the failure reason **InvalidVerificationCode** would return **True** as expected, but we cannot vouch for just their word here, there's no evidence.Nevertheless, it does seem counter-intuitive that there is such a failure reason if it's not going to be set to **True** when the verification code is expired (is this not an invalid code?).Hoping that makes more sense now, and apologies for the confusion.Let us know your thoughts!Cheers,
Jo&atilde;o Neves__July 25  1:57 PM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
Hi again team,All right, let me try to clear up the confusion, since I believe a lot of noise was introduced in this incident.There is nothing wrong with the user registration: users are able to complete the registration if the code is still valid, and fail when the code is expired (past 15 minutes).The point here is that, when the registration fails because of an expired verification code, the failure reason **InvalidVerificationCode** does not seem to be correctly filled with **True**. Thus, the customer cannot determine what was the failure reason and cannot present users with a message indicating that the code expired and that they must retry - this is what is 'blocking' them.Furthermore, they claim that they had previously developed and tested the flow under the assumption that the failure reason **InvalidVerificationCode** would return **True** as expected, but we cannot vouch for just their word here, there's no evidence.Nevertheless, it does seem counter-intuitive that there is such a failure reason if it's not going to be set to **True** when the verification code is expired (is this not an invalid code?).Hoping that makes more sense now, and apologies for the confusion.Let us know your thoughts!Cheers,
Jo&atilde;o Neves__
July 25  3:14 PM WESTwebDavid PiresSend ZenDesk private comment has been set: Hey team  
Thanks for the clarification, we have identified the problem. There was a change on how we are reading the error response and we are not setting the **InvalidaVerificationCode** to **True**. We will release the fix today, and I'll let you know when it reaches the client tenant.July 25  3:14 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hey team  
Thanks for the clarification, we have identified the problem. There was a change on how we are reading the error response and we are not setting the **InvalidaVerificationCode** to **True**. We will release the fix today, and I'll let you know when it reaches the client tenant.
July 25  3:14 PM WESTwebRootlySend ZenDesk private comment has been unsetJuly 25  3:14 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

July 25  3:14 PM WESTwebDavid PiresDavid Pires has been assigned as EngineerJuly 31  2:59 AM WESTwebRootlyZendesk Private Comment has been changed to: ----------------------------------------------**Update to R&amp;D**
Dear R&amp;D,To follow-up on your previous comms,&gt; _Hey team_
&gt;
&gt;
&gt;
&gt; _Thanks for the clarification, we have identified the problem. There was a change on how we are reading the error response and we are not setting the **InvalidaVerificationCode** to **True**. We will release the fix today, and I'll let you know when it reaches the client tenant._Can you let us know if the fixes had reached the client's tenant? May we know whether Support can check this (i.e. whether the fix is deployed) in one of the Grafana dashboards?Thank you,_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_July 31  2:59 AM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
Dear R&amp;D,To follow-up on your previous comms,&gt; _Hey team_
&gt;
&gt;
&gt;
&gt; _Thanks for the clarification, we have identified the problem. There was a change on how we are reading the error response and we are not setting the **InvalidaVerificationCode** to **True**. We will release the fix today, and I'll let you know when it reaches the client tenant._Can you let us know if the fixes had reached the client's tenant? May we know whether Support can check this (i.e. whether the fix is deployed) in one of the Grafana dashboards?Thank you,__
July 31  2:59 AM WESTwebRootlyZendesk Private Comment has been changed to: ------------------------------------------------ This notification was sent from Zendesk Support ticket #3038244 to all linked JIRA issues by Zaman Akbar Mohamed-Akbar. --**Update to R&amp;D**
Dear R&amp;D,To follow-up on your previous comms,&gt; _Hey team_
&gt;
&gt; &gt; &gt; &gt; _Thanks for the clarification, we have identified the problem. There was a change on how we are reading the error response and we are not setting the **_InvalidaVerificationCode **_to_** True_**. We will release the fix today, and I'll let you know when it reaches the client tenant._Can you let us know if the fixes had reached the client's tenant? May we know whether Support can check this (i.e. whether the fix is deployed) in one of the Grafana dashboards?Thank you,_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_July 31  2:59 AM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
------------------------------------------------ This notification was sent from Zendesk Support ticket #3038244 to all linked JIRA issues by Zaman Akbar Mohamed-Akbar. --**Update to R&amp;D**
Dear R&amp;D,To follow-up on your previous comms,&gt; _Hey team_
&gt;
&gt; &gt; &gt; &gt; _Thanks for the clarification, we have identified the problem. There was a change on how we are reading the error response and we are not setting the **_InvalidaVerificationCode **_to_** True_**. We will release the fix today, and I'll let you know when it reaches the client tenant._Can you let us know if the fixes had reached the client's tenant? May we know whether Support can check this (i.e. whether the fix is deployed) in one of the Grafana dashboards?Thank you,__
July 31  9:37 AM WESTwebDavid PiresSend ZenDesk private comment has been set: Hey team,The fix should reach the client's tenant by Tuesday. In any case, I'll let you know as soon as it's deployed.July 31  9:37 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hey team,The fix should reach the client's tenant by Tuesday. In any case, I'll let you know as soon as it's deployed.
July 31  9:37 AM WESTwebRootlySend ZenDesk private comment has been unsetJuly 31  9:37 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

July 31  9:39 AM WESTwebDavid PiresSend ZenDesk private comment has been set: To add to my previous response, the dashboard is https://outsystems.grafana.net/goto/MlbdsV9Sg?orgId=1 and the version to looking for is v17.1522.0July 31  9:39 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
To add to my previous response, the dashboard is https://outsystems.grafana.net/goto/MlbdsV9Sg?orgId=1 and the version to looking for is v17.1522.0
July 31  9:39 AM WESTwebRootlySend ZenDesk private comment has been unsetJuly 31  9:39 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

August 12 10:31 AM WESTwebCarlos XavierSend ZenDesk private comment has been set: Hi Support,  The version with the fix is already in GA. Can you please ask the customer to republish the app and confirm that the issue is fixed?  Best regards,  
Carlos XavierAugust 12 10:31 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hi Support,  The version with the fix is already in GA. Can you please ask the customer to republish the app and confirm that the issue is fixed?  Best regards,  
Carlos Xavier
August 12 10:31 AM WESTwebRootlySend ZenDesk private comment has been unsetAugust 12 10:31 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

August 13  8:14 AM WESTwebRootly
The Global Support team marked this incident as closed in ZenDesk.
August 13  8:14 AM WESTwebRootly
Incident has been resolved
August 13  8:14 AM WESTwebRootlyZenDesk Event Type has been set: solved