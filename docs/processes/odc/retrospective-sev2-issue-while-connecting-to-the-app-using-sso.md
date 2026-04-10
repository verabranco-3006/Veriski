---
title: Retrospective-SEV2-Issue while connecting to the app using SSO
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4335337622/Retrospective-SEV2-Issue+while+connecting+to+the+app+using+SSO
confluence_space: RKB
confluence_page_id: 4335337622
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV2-Issue while connecting to the app using SSO

## 📘 Overview
Author:&nbsp;Rootlytrue

Severity:&nbsp;SEV2Redtrue

Teams:&nbsp;Identity CoreBluetrue&nbsp;Global RoutingBluetrue
#### 🕐 Timestamps
Started At:&nbsp;July 10 12:58 PM WESTBluetrue

Mitigated At:&nbsp;August 5  4:33 PM WESTYellowtrue

Resolved At:&nbsp;August 5  4:33 PM WESTGreentrue
#### 🔗 Links
[Incident Page](https://rootly.com/account/incidents/694-issue-while-connecting-to-the-app-using-sso)

[Pagerduty incident](https://outsystems.pagerduty.com/incidents/Q32584LJ9KYEFE)

[Slack channel](https://slack.com/app_redirect?channel=C07C6APEATB&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3030585)

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

Pedro Quintas
#### Summary
----------------------------------------------**ISSUE DESCRIPTION AND HOW TO REPRODUCE**
Customer having a error &quot;upstream request timeout&quot; affecting end-user experience severely affected since most of the times they need to proceed with multiple attempts to log in with the Identity Provider.- ![](https://supportoutsystems.zendesk.com/attachments/token/RL7oe2jze40ekWooeajXGUt8R/?name=image.png)**IMPACT ON THE CUSTOMER**
High, was urgent however, due to a functional update we are adjusting to High, but is affecting all stages.**TROUBLESHOOTING STEPS &amp; WORKAROUND**
Since this affects all stages we ask creds to customer for dev and replicate the situation:- To replicate use this creds and link -&gt; _https://axione-dev.outsystems.app/STITCH/Login_). -&gt;**user **: _ppr-solypse.collab -&gt;_**password **: _pMI$UaeZcpYTmjTZXc?3_
- _To share the full investigation a week ago:_- Just replicated in the first access:- ![](https://supportoutsystems.zendesk.com/attachments/token/Wq90oEtmxKLrSPNGZD7qIxKE0/?name=image.png)- Seems the error comes from the endpoint:- https://axione-dev.outsystems.app/auth/realms/395aab41-dfb8-4671-84c7-48246dd8cbdd/broker/612de050-8098-438a-9266-0f29d6e854e8/endpoint?state=qrJXQhwCfiZsuWFoJMNdHS247-N3ybjwQ2podrdfT5Y.oTxps0qoGqk.R8eZrB7JQG-COZhPE-QxNw&amp;session_state=50775f18-c329-4e31-b452-483374981e13&amp;code=ec9cab07-6735-4d0c-bb51-48a9fb2dd1ca.50775f18-c329-4e31-b452-483374981e13.323d65cf-e960-4a35-b834-1b1d3e28ef60- When we redirect to our endpoint:- ![](https://supportoutsystems.zendesk.com/attachments/token/NIPIAWYRlTlfyY0ZfUqKgf7X1/?name=image.png)- Retrying again the login works:- ![](https://supportoutsystems.zendesk.com/attachments/token/pJzmTJpiUuSca5jhp1r8VfMsW/?name=image.png)- Replicated at 2024-07-02T15:35:02- ![](https://supportoutsystems.zendesk.com/attachments/token/rWYlsFnHliSMqhcyh9cS34NDu/?name=image.png)- Not the same error previously present:- However the same at CF level:- ![](https://supportoutsystems.zendesk.com/attachments/token/HX5Hu7FEAZwYEdEVSBerK73FU/?name=image.png)- https://outsystems.grafana.net/d/6-6x5IF4k/cloudfront-logs?orgId=1&amp;var-environment=prod&amp;var-data_source=MWYvlds7z&amp;var-host=axione-dev.outsystems.app&amp;var-method=All&amp;var-status_code=All&amp;var-edge_response_type=All&amp;var-search=&amp;var-plat_s3=s3%2Flogs-plat-edge-ue1-prod-rn-cloudrd-os&amp;var-run_s3=s3%2Flogs-run-edge-ue1-prod-rn-cloudrd-os&amp;var-cus_s3=s3%2Flogs-cus-edge-ue1-prod-rn-cloudrd-os- Matching my IP Address on the CF- ![](https://supportoutsystems.zendesk.com/attachments/token/vcqkWwRoaKRT6Ctex0lKOQrrM/?name=image.png)- type=&quot;IDENTITY_PROVIDER_LOGIN_ERROR&quot;, realmId=&quot;395aab41-dfb8-4671-84c7-48246dd8cbdd&quot;, clientId=&quot;client_runtime&quot;, userId=&quot;null&quot;, ipAddress=&quot;2001:818:e2cb:1900:f0c6:6ae3:f66a:6076&quot;, error=&quot;identity_provider_login_failure&quot;, code_id=&quot;3f5e60f7-61a3-49ba-b78e-d0bf7b1104d2&quot;- User ID seems to have come as Null from the provider.- Further looking in the same trace of the errors we have 2 segments:- ![](https://supportoutsystems.zendesk.com/attachments/token/1kx8pZUXmDmXc0NoFA5zo5Y7A/?name=image.png)- Connect to oauth.axione.fr:443 [oauth.axione.fr/109.74.90.118] failed: Connection timed out- We are receiving timeouts from the IDP on the IP/DNS oauth.axione.fr/109.74.90.118
At this point I ask the customer to talk with the provider to understand the performance of the IDP if was responding in a acceptable time, they send us a dashboard where requests were not taking more than 1.5s, however, doesn't said much, since i also requested the IDP logs, not provided:- ![](https://supportoutsystems.zendesk.com/attachments/token/5r661CBThKpmZySBst5sbnQBR/?name=image.png)Today, i did a second analysis, Replicate again at 11:40 today July 10. On CF the same pattern:- ![](https://supportoutsystems.zendesk.com/attachments/token/5ZdcwsX29NIybou0kp38ZI9nU/?name=image.png)
Same situation on IDentity side:![](https://supportoutsystems.zendesk.com/attachments/token/P9wjDEXYiM7QhAD5AbGcbZPYG/?name=image.png)- ![](https://supportoutsystems.zendesk.com/attachments/token/RaTIv9CHsabuXvC8tzGT7nYd8/?name=image.png)
Even that prior to my replication there was a user that replicate also in DEV:- ![](https://supportoutsystems.zendesk.com/attachments/token/i5tTjo7LUsuPuLjkKhl4SUbqu/?name=image.png)I think the IDP is taking more time to respond and after 10s/15s +/- we receive the 504 and the upstream request timeout error page, however, cannot understand if this error is from the network infrastructure of customer or ours, and would like to understand that and:- Does the investigation makes sense? Can we drill down more? Since the traces on identity don't seem to work on our dashboards since no results appear?
- if the timeout is on our side, can it be increase since i assume is the keycloak one?Any questions please let me know, also im redirecting to Identity team, however, based on investigation of timeout, maybe BE should also join (just a guess)**TECH DATA OR ANY OTHER RELEVANT INFO**
Ring: ga
Tenant Id: 65825faf-35f3-4158-b5a5-9b12424a846d
Tenant Prefix: axione
Region: eu-central-1
E6B.U0T.CSS.PID.4RY.ILN.BYZ.GOU- DEV ID PROVIDER ID -&gt;612de050-8098-438a-9266-0f29d6e854e8 DEV
- PRD -&gt; 15bcacb5-6da3-4b07-b58e-9c686882a983
- PRD Well know -&gt; https://oauth.axione.fr/realms/axione/.well-known/openid-configuration
- Realm -&gt; 395aab41-dfb8-4671-84c7-48246dd8cbdd_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 Retrospective### Details
**Ring:** ga
**System-wide impact:**&nbsp; 
**Tenant ID:** 65825faf-35f3-4158-b5a5-9b12424a846d
**Tenant Prefix:** axione
**Routing Error Code:** N/A
**Product Area:** Phoenix::Application Runtime::Access management::Authentication
### Impact:
Customer not able to reliably log in with their third party idp
### Investigation and troubleshooting findings:
Identity Core team looked into the internal Keycloak error logs and Gloo logs noticing their external third party idp was taking too long to reply and the operation timed out.
### Resolution:
Looks like a problem on their side. We suggested Global support to suggest the customer to give other well established third party idps a try and see if they could reproduce their issue (Azure AD, Google, Facebook). Also suggested to setup their idp in some testing pages that will help them understand if the latency was on their side or was a problem with OutSystems products.
## Tasks performed during incident resolution:
&nbsp;Log investigation.
## Executive Summary
[Guidelines](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4144496679/Incident+Retrospectives+-+Playbook#STEP-3---Write-the-Executive-Summary)

Customer complained of not being able to reliably log in with their third party idp. Identity Core team confirmed the timeouts and pointed at their external endpoint taking too long to reply, hence the error.
## Root Causes 
[Guidelines](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4144496679/Incident+Retrospectives+-+Playbook#STEP-1---Perform-the-Root-Cause-Analysis)

- 
Their external idp was not fast enough, taking more than 15 seconds to send a reply to OutSystems services, effectively timing out the login intents.

If the customer needs formal RCA, please fill out the following field with the document URL

[Please follow these instructions and place the RCA URL in the field below.](https://docs.google.com/document/d/13rXmBsOJh73nV2D6Z17SIBGBu2HOTWty5ddsvU000JM/edit#heading=h.bqxasxszr5q)

RCA URL

&lt;Place the URL of the customer RCA here if you have created one&gt;
## ⌛ Timeline
[View on Rootly](https://rootly.com/account/incidents/694-issue-while-connecting-to-the-app-using-sso)

**Date**

**Source**

**User**

**Event**

July 10 12:52 PM WEST

web

Rootly

created an alert via

July 10 12:52 PM WEST

web

Rootly

Rootly created this incident

July 10 12:52 PM WEST

web

Rootly

In triage date has been set to July 10 12:52 PM WEST

July 10 12:52 PM WEST

web

Rootly

[Slack Channel](https://slack.com/app_redirect?channel=C07C6APEATB&amp;team=T041063TZ) has been created

July 10 12:52 PM WEST

web

Rootly

Ring: ga
System-wide impact:  
Tenant ID: 65825faf-35f3-4158-b5a5-9b12424a846d
Tenant Prefix: axione
Routing Error Code: N/A
Product Area: Phoenix::Application Runtime::Access management::Authentication

July 10 12:52 PM WEST

web

Rootly

[PagerDuty Incident](https://outsystems.pagerduty.com/incidents/Q32584LJ9KYEFE) has been created.

📧 Notified Pedro Quintas by email.

&nbsp;&nbsp;

📲 Notified Pedro Quintas by push notification.  (via Android)

&nbsp;&nbsp;

📲 Notified Pedro Quintas by push notification.  (via Android)

July 10 12:52 PM WEST

web

Rootly

Pedro Quintas has been assigned as Engineer

July 10 12:52 PM WEST

web

Rootly

Pedro Quintas acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q32584LJ9KYEFE). (via Mobile)

July 10 12:58 PM WEST

web

Pedro Quintas

Incident has been started

July 10 12:58 PM WEST

web

Rootly

Pagerduty Integrations acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q32584LJ9KYEFE). (via Mobile)

July 10  1:02 PM WEST

slack

pedro.quintas

All of the issues seem to be related with identity endpoints, the Client Runtime isn't loaded when things go wrong, so it doesn't seem to be involved. Moving this to Identity Core for further investigation.

July 10  1:02 PM WEST

web

Rootly

This incident was instantiated in Jira: RDINC-26777. Please work the incident using Rootly

July 10  1:03 PM WEST

web

Pedro Quintas

Swarm has been set: Identity Core

July 10  1:03 PM WEST

web

Rootly

Pagerduty Integrations added Rodrigo Bernardo as responder in [PagerDuty](https://outsystems.pagerduty.com/incidents/Q32584LJ9KYEFE)

July 10  1:03 PM WEST

web

Pedro Quintas

Teams has been removed: [Client Runtime](/account/teams/client-runtime/status)

July 10  1:04 PM WEST

web

Rootly

Rodrigo Bernardo joined this [PagerDuty](https://outsystems.pagerduty.com/incidents/Q32584LJ9KYEFE) incident.

July 10  1:04 PM WEST

web

Rootly

Rodrigo Bernardo acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q32584LJ9KYEFE). (via Mobile)

July 10  1:52 PM WEST

web

Rootly

This incident was instantiated in Jira: RDINC-26777. Please work the incident using Rootly

July 10  9:42 PM WEST

web

Yang Yang

Send ZenDesk private comment has been set: Team,
I just reproduced it. From the [log](https://outsystems.grafana.net/d/jWPxVFZVk4/identity-logs?orgId=1&amp;var-rings=ga&amp;var-region=eu-central-1&amp;var-regionShort=All&amp;var-cluster=id-ga-eu-ce-1-01&amp;var-severity=Error&amp;var-search=&amp;from=1720642669057&amp;to=1720642682261) It looks like their IdP timed out
and in past 24 hours there were lots of them (see Keycloak section in this [log](https://outsystems.grafana.net/d/jWPxVFZVk4/identity-logs?orgId=1&amp;var-rings=ga&amp;var-region=eu-central-1&amp;var-regionShort=All&amp;var-cluster=id-ga-eu-ce-1-01&amp;var-severity=Error&amp;var-search=timed%20out&amp;from=1720583552283&amp;to=1720643357689), all for oauth.axione.fr:443)
Can you follow up with customer to double check their IdP?

July 10  9:42 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:
Team,
I just reproduced it. From the [log](https://outsystems.grafana.net/d/jWPxVFZVk4/identity-logs?orgId=1&amp;var-rings=ga&amp;var-region=eu-central-1&amp;var-regionShort=All&amp;var-cluster=id-ga-eu-ce-1-01&amp;var-severity=Error&amp;var-search=&amp;from=1720642669057&amp;to=1720642682261) It looks like their IdP timed out
and in past 24 hours there were lots of them (see Keycloak section in this [log](https://outsystems.grafana.net/d/jWPxVFZVk4/identity-logs?orgId=1&amp;var-rings=ga&amp;var-region=eu-central-1&amp;var-regionShort=All&amp;var-cluster=id-ga-eu-ce-1-01&amp;var-severity=Error&amp;var-search=timed%20out&amp;from=1720583552283&amp;to=1720643357689), all for oauth.axione.fr:443)
Can you follow up with customer to double check their IdP?

July 10  9:42 PM WEST

web

Rootly

Send ZenDesk private comment has been unset

July 10  9:42 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:

July 11  9:50 AM WEST

web

Rootly

Zendesk Private Comment has been set: ----------------------------------------------**Update to R&amp;D**
Hello team,Thank for your investigation and confirm our suspicious, however, would be possible to confirm also my questions:- Can we drill down more? Since the traces on identity don't seem to work on our dashboards since no results appear?- What i mean is that, this trace on example does have more details?- ![](https://supportoutsystems.zendesk.com/attachments/token/E4dVL4hrUH6E7cGJ7rOlOQSN5/?name=image.png)- because doesn't seem to work on our General trace dashboard.
- Also, the timeout or request on our side, can it be increase? Since I assume is the keycloak one? To maintain the TCP connection open for longer, or it was to be on IDP side?__

July 11  9:51 AM WEST

web

Rootly

NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
Hello team,Thank for your investigation and confirm our suspicious, however, would be possible to confirm also my questions:- Can we drill down more? Since the traces on identity don't seem to work on our dashboards since no results appear?- What i mean is that, this trace on example does have more details?- ![](https://supportoutsystems.zendesk.com/attachments/token/E4dVL4hrUH6E7cGJ7rOlOQSN5/?name=image.png)- because doesn't seem to work on our General trace dashboard.
- Also, the timeout or request on our side, can it be increase? Since I assume is the keycloak one? To maintain the TCP connection open for longer, or it was to be on IDP side?__

July 11  9:51 AM WEST

web

Rootly

Zendesk Private Comment has been changed to: ------------------------------------------------ This notification was sent from Zendesk Support ticket #3030585 to all linked JIRA issues by Cristiano Costa. --**Update to R&amp;D**
Hello team,Thank for your investigation and confirm our suspicious, however, would be possible to confirm also my questions:- Can we drill down more? Since the traces on identity don't seem to work on our dashboards since no results appear?- What i mean is that, this trace on example does have more details?- Attachment - image.png- because doesn't seem to work on our General trace dashboard.
- Also, the timeout or request on our side, can it be increase? Since I assume is the keycloak one? To maintain the TCP connection open for longer, or it was to be on IDP side?_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_

July 11  9:51 AM WEST

web

Rootly

NEW MESSAGE FROM GLOBAL SUPPORT:
------------------------------------------------ This notification was sent from Zendesk Support ticket #3030585 to all linked JIRA issues by Cristiano Costa. --**Update to R&amp;D**
Hello team,Thank for your investigation and confirm our suspicious, however, would be possible to confirm also my questions:- Can we drill down more? Since the traces on identity don't seem to work on our dashboards since no results appear?- What i mean is that, this trace on example does have more details?- Attachment - image.png- because doesn't seem to work on our General trace dashboard.
- Also, the timeout or request on our side, can it be increase? Since I assume is the keycloak one? To maintain the TCP connection open for longer, or it was to be on IDP side?__

July 11  1:27 PM WEST

web

Yang Yang

Send ZenDesk private comment has been set: Hi Team,
Thanks for the followup. Regarding your questions:1. We are aware that KC trace is not carried to Grafana. We have ticket on our side to tackle that
2. Regarding time out value. The default timeout of http client in KC is 60 sec. It is possible to increase it via some configuration. However when I look at Gloo access log of those failure ( [https://outsystems.grafana.net/d/E6xvxTJnz/gloo-access-logs?orgId=1&amp;var-ring=ga&amp;var-meth[&hellip;]1720583552000&amp;to=1720643357000&amp;var-stamp=id-ga-eu-ce-1-01](https://outsystems.grafana.net/d/E6xvxTJnz/gloo-access-logs?orgId=1&amp;var-ring=ga&amp;var-method=All&amp;var-status_code=5.%2A&amp;var-search=65825faf-35f3-4158-b5a5-9b12424a846d&amp;from=1720583552000&amp;to=1720643357000&amp;var-stamp=id-ga-eu-ce-1-01)), It looks like it timed out  on Gloo around 15 sec. So It looks like we have our own networking rules. Can you check with Global Routing Team to confirm that? If that's the case increase timeout on KC side won't help this scenario

July 11  1:27 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:
Hi Team,
Thanks for the followup. Regarding your questions:1. We are aware that KC trace is not carried to Grafana. We have ticket on our side to tackle that
2. Regarding time out value. The default timeout of http client in KC is 60 sec. It is possible to increase it via some configuration. However when I look at Gloo access log of those failure ( [https://outsystems.grafana.net/d/E6xvxTJnz/gloo-access-logs?orgId=1&amp;var-ring=ga&amp;var-meth[&hellip;]1720583552000&amp;to=1720643357000&amp;var-stamp=id-ga-eu-ce-1-01](https://outsystems.grafana.net/d/E6xvxTJnz/gloo-access-logs?orgId=1&amp;var-ring=ga&amp;var-method=All&amp;var-status_code=5.%2A&amp;var-search=65825faf-35f3-4158-b5a5-9b12424a846d&amp;from=1720583552000&amp;to=1720643357000&amp;var-stamp=id-ga-eu-ce-1-01)), It looks like it timed out  on Gloo around 15 sec. So It looks like we have our own networking rules. Can you check with Global Routing Team to confirm that? If that's the case increase timeout on KC side won't help this scenario

July 11  1:27 PM WEST

web

Rootly

Send ZenDesk private comment has been unset

July 11  1:27 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:

July 11  2:49 PM WEST

web

Rootly

Zendesk Private Comment has been changed to: ----------------------------------------------**Update to R&amp;D**
Hello team,Thank you for the update.Looking at your investigation of gloo timeout and HAR file of replications, indeed the 15s match:- ![](https://supportoutsystems.zendesk.com/attachments/token/bYAiK9SHwZfVc4XAUAqYVtFmf/?name=image.png)
- ![](https://supportoutsystems.zendesk.com/attachments/token/cqR2RnmRUnNy69UFObcZknbxT/?name=image.png)And looking at this doc from R&amp;D -&gt; https://outsystemsrd.atlassian.net/wiki/spaces/RDCCPC/pages/2956034228/Gloo+EAS+Timeouts![](https://supportoutsystems.zendesk.com/attachments/token/DxMqV0oYmXAoGZ6d9Qylry17Q/?name=image.png)- Indeed we have the UT flag! And matches what are we seeing on the error for the end user, and also the same doc confirms the TO of 15s:
- ![](https://supportoutsystems.zendesk.com/attachments/token/ws549xE8vaPGN9hgtrEqsQM1m/?name=image.png)Due to that we will be engaging GR to followup, however, the Jira/rootly was to be passed on your side.Thank you again for the help._&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_

July 11  2:49 PM WEST

web

Rootly

NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
Hello team,Thank you for the update.Looking at your investigation of gloo timeout and HAR file of replications, indeed the 15s match:- ![](https://supportoutsystems.zendesk.com/attachments/token/bYAiK9SHwZfVc4XAUAqYVtFmf/?name=image.png)
- ![](https://supportoutsystems.zendesk.com/attachments/token/cqR2RnmRUnNy69UFObcZknbxT/?name=image.png)And looking at this doc from R&amp;D -&gt; https://outsystemsrd.atlassian.net/wiki/spaces/RDCCPC/pages/2956034228/Gloo+EAS+Timeouts![](https://supportoutsystems.zendesk.com/attachments/token/DxMqV0oYmXAoGZ6d9Qylry17Q/?name=image.png)- Indeed we have the UT flag! And matches what are we seeing on the error for the end user, and also the same doc confirms the TO of 15s:
- ![](https://supportoutsystems.zendesk.com/attachments/token/ws549xE8vaPGN9hgtrEqsQM1m/?name=image.png)Due to that we will be engaging GR to followup, however, the Jira/rootly was to be passed on your side.Thank you again for the help.__

July 11  2:50 PM WEST

web

Rootly

Zendesk Private Comment has been changed to: ------------------------------------------------ This notification was sent from Zendesk Support ticket #3030585 to all linked JIRA issues by Cristiano Costa. --**Update to R&amp;D**
Hello team,Thank you for the update.Looking at your investigation of gloo timeout and HAR file of replications, indeed the 15s match:- Attachment - image.png
- Attachment - image.pngAnd looking at this doc from R&amp;D -&gt; https://outsystemsrd.atlassian.net/wiki/spaces/RDCCPC/pages/2956034228/GlooEASTimeoutsAttachment - image.png- Indeed we have the UT flag! And matches what are we seeing on the error for the end user, and also the same doc confirms the TO of 15s:
- Attachment - image.pngDue to that we will be engaging GR to followup, however, the Jira/rootly was to be passed on your side.Thank you again for the help._&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_

July 11  2:50 PM WEST

web

Rootly

NEW MESSAGE FROM GLOBAL SUPPORT:
------------------------------------------------ This notification was sent from Zendesk Support ticket #3030585 to all linked JIRA issues by Cristiano Costa. --**Update to R&amp;D**
Hello team,Thank you for the update.Looking at your investigation of gloo timeout and HAR file of replications, indeed the 15s match:- Attachment - image.png
- Attachment - image.pngAnd looking at this doc from R&amp;D -&gt; https://outsystemsrd.atlassian.net/wiki/spaces/RDCCPC/pages/2956034228/GlooEASTimeoutsAttachment - image.png- Indeed we have the UT flag! And matches what are we seeing on the error for the end user, and also the same doc confirms the TO of 15s:
- Attachment - image.pngDue to that we will be engaging GR to followup, however, the Jira/rootly was to be passed on your side.Thank you again for the help.__

July 12  2:00 PM WEST

web

Yang Yang

Send ZenDesk private comment has been set: Hi Team,
Please let us know the update from GR team and advise what we should do with support ticket. It is on our board but my team is not doing anything at this point.....

July 12  2:00 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:
Hi Team,
Please let us know the update from GR team and advise what we should do with support ticket. It is on our board but my team is not doing anything at this point.....

July 12  2:00 PM WEST

web

Rootly

Send ZenDesk private comment has been unset

July 12  2:00 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:

July 12  5:33 PM WEST

web

Yang Yang

Swarm has been set: Global Routing and Security

July 12  5:33 PM WEST

web

Yang Yang

Swarm has been unset: Identity Core

July 12  5:33 PM WEST

web

Rootly

Pagerduty Integrations added Kiran Malsetty as responder in [PagerDuty](https://outsystems.pagerduty.com/incidents/Q32584LJ9KYEFE)

July 12  5:34 PM WEST

web

Rootly

Kiran Malsetty joined this [PagerDuty](https://outsystems.pagerduty.com/incidents/Q32584LJ9KYEFE) incident.

July 12  6:13 PM WEST

slack

Henrique Santos (hqs)

hey everyone! regarding the 15 seconds, it can be explained:in [here](https://docs.solo.io/gloo-edge/latest/reference/cheatsheets/timeouts/#virtualservice-crd), we confirm that Gloo's default timeout is 15 seconds for any route. For example, for platform, I know that teams set their own increased timeouts and the same happens in runtime.
I took a look at id-dev at a random tenant/environment routetable and I don't see any timeout being set, so this justifies the 15 second timeout.If you want increase the timeout, you'll have to change these routetables (don't know how they are created) to add the timeout. [Example from AVS from Platform](https://github.com/OutSystems/OutSystems.ApplicationVersioning.Service/blob/main/dist/outsystems-applicationversioning-service/templates/gloo-route-table.yaml#L18)
Beware that there are 3 relevant setting `timeout` `perTryTimeout` and `numRetries` - this is explained in [https://outsystemsrd.atlassian.net/wiki/spaces/RA/pages/3487761527/HowTo+Track+Requests+With+Grafana#Timeouts](https://outsystemsrd.atlassian.net/wiki/spaces/RA/pages/3487761527/HowTo+Track+Requests+With+Grafana#Timeouts)

July 12  6:48 PM WEST

web

Yang Yang

Send ZenDesk private comment has been set: Hi Team,
After check with GRS team, we can increase the timeout of Gloo route from 15s to 60s ( would need to engage SRE team on that) but that would NOT solve customer's issue because in our Keycloak log It shows the IdP frequently timed out at 60s. And to increase that we would need to create a user story to do it. Please advise how you want to proceed?

July 12  6:48 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:
Hi Team,
After check with GRS team, we can increase the timeout of Gloo route from 15s to 60s ( would need to engage SRE team on that) but that would NOT solve customer's issue because in our Keycloak log It shows the IdP frequently timed out at 60s. And to increase that we would need to create a user story to do it. Please advise how you want to proceed?

July 12  6:48 PM WEST

web

Rootly

Send ZenDesk private comment has been unset

July 12  6:48 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:

July 16  3:34 PM WEST

web

Rootly

Zendesk Private Comment has been changed to: ----------------------------------------------**Update to R&amp;D**
Hello team,First thank you both teams for the help so far.So we went to a call to a customer, and we are aligned on the same investigation, where indeed the IDP timeouts, however, we have some catches, however, would need GR team help:- Customer doesn't see slow requests on their side and inside the Infra, so they suspect the time spent might be lost on some hop between from our infra to theirs (Their infra on Frankfurt and IDP on France).- On this point, we would like to understand if it is possible to have some more detail and traceability on the request from our pod (I assume the key cloak pod until their IDP)
- Also, since customer is heavily affected and end users, we must exhaust our possibilities on them, I was reading the information from GR team regarding the timeout, customer is still interested if that can be increase to at least reduce the number of timeouts- Can we increase on their infra/only QA stage this gloo timeout to 30s?Best regards,_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_

July 16  3:34 PM WEST

web

Rootly

NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
Hello team,First thank you both teams for the help so far.So we went to a call to a customer, and we are aligned on the same investigation, where indeed the IDP timeouts, however, we have some catches, however, would need GR team help:- Customer doesn't see slow requests on their side and inside the Infra, so they suspect the time spent might be lost on some hop between from our infra to theirs (Their infra on Frankfurt and IDP on France).- On this point, we would like to understand if it is possible to have some more detail and traceability on the request from our pod (I assume the key cloak pod until their IDP)
- Also, since customer is heavily affected and end users, we must exhaust our possibilities on them, I was reading the information from GR team regarding the timeout, customer is still interested if that can be increase to at least reduce the number of timeouts- Can we increase on their infra/only QA stage this gloo timeout to 30s?Best regards,__

July 16  3:34 PM WEST

web

Rootly

Zendesk Private Comment has been changed to: ------------------------------------------------ This notification was sent from Zendesk Support ticket #3030585 to all linked JIRA issues by Cristiano Costa. --**Update to R&amp;D**
Hello team,First thank you both teams for the help so far.So we went to a call to a customer, and we are aligned on the same investigation, where indeed the IDP timeouts, however, we have some catches, however, would need GR team help:- Customer doesn't see slow requests on their side and inside the Infra, so they suspect the time spent might be lost on some hop between from our infra to theirs (Their infra on Frankfurt and IDP on France).- On this point, we would like to understand if it is possible to have some more detail and traceability on the request from our pod (I assume the key cloak pod until their IDP)
- Also, since customer is heavily affected and end users, we must exhaust our possibilities on them, I was reading the information from GR team regarding the timeout, customer is still interested if that can be increase to at least reduce the number of timeouts- Can we increase on their infra/only QA stage this gloo timeout to 30s?Best regards,_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_

July 16  3:34 PM WEST

web

Rootly

NEW MESSAGE FROM GLOBAL SUPPORT:
------------------------------------------------ This notification was sent from Zendesk Support ticket #3030585 to all linked JIRA issues by Cristiano Costa. --**Update to R&amp;D**
Hello team,First thank you both teams for the help so far.So we went to a call to a customer, and we are aligned on the same investigation, where indeed the IDP timeouts, however, we have some catches, however, would need GR team help:- Customer doesn't see slow requests on their side and inside the Infra, so they suspect the time spent might be lost on some hop between from our infra to theirs (Their infra on Frankfurt and IDP on France).- On this point, we would like to understand if it is possible to have some more detail and traceability on the request from our pod (I assume the key cloak pod until their IDP)
- Also, since customer is heavily affected and end users, we must exhaust our possibilities on them, I was reading the information from GR team regarding the timeout, customer is still interested if that can be increase to at least reduce the number of timeouts- Can we increase on their infra/only QA stage this gloo timeout to 30s?Best regards,__

July 17  8:42 AM WEST

web

Rootly

NEW MESSAGE FROM GLOBAL SUPPORT:
------------------------------------------------ This notification was sent from Zendesk Support ticket #3030585 to all linked JIRA issues by Cristiano Costa. --**Update to R&amp;D**
Hello team,First thank you both teams for the help so far.So we went to a call to a customer, and we are aligned on the same investigation, where indeed the IDP timeouts, however, we have some catches, however, would need GR team help:- Customer doesn't see slow requests on their side and inside the Infra, so they suspect the time spent might be lost on some hop between from our infra to theirs (Their infra on Frankfurt and IDP on France).- On this point, we would like to understand if it is possible to have some more detail and traceability on the request from our pod (I assume the key cloak pod until their IDP)
- Also, since customer is heavily affected and end users, we must exhaust our possibilities on them, I was reading the information from GR team regarding the timeout, customer is still interested if that can be increase to at least reduce the number of timeouts- Can we increase on their infra/only QA stage this gloo timeout to 30s?Best regards,__

July 17  8:42 AM WEST

web

Rootly

NEW MESSAGE FROM GLOBAL SUPPORT:
------------------------------------------------ This notification was sent from Zendesk Support ticket #3030585 to all linked JIRA issues by Cristiano Costa. --**Update to R&amp;D**
Hello team,First thank you both teams for the help so far.So we went to a call to a customer, and we are aligned on the same investigation, where indeed the IDP timeouts, however, we have some catches, however, would need GR team help:- Customer doesn't see slow requests on their side and inside the Infra, so they suspect the time spent might be lost on some hop between from our infra to theirs (Their infra on Frankfurt and IDP on France).- On this point, we would like to understand if it is possible to have some more detail and traceability on the request from our pod (I assume the key cloak pod until their IDP)
- Also, since customer is heavily affected and end users, we must exhaust our possibilities on them, I was reading the information from GR team regarding the timeout, customer is still interested if that can be increase to at least reduce the number of timeouts- Can we increase on their infra/only QA stage this gloo timeout to 30s?Best regards,__

July 17 12:12 PM WEST

web

Rootly

Zendesk Private Comment has been changed to: ----------------------------------------------**Update to R&amp;D**
Hello team,
Thank you for the reply and feedback.
And regarding my other part of the communication:
_**Also, since customer is heavily affected and end users, we must exhaust our possibilities on them, I was reading the information from GR team regarding the timeout, customer is still interested if that can be increase to at least reduce the number of timeouts**_- _**Can we increase on their infra/only QA stage this gloo timeout to 30s?**_
We kindly wait for your feedback.
Best regards,_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_

July 17 12:12 PM WEST

web

Rootly

NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
Hello team,
Thank you for the reply and feedback.
And regarding my other part of the communication:
_**Also, since customer is heavily affected and end users, we must exhaust our possibilities on them, I was reading the information from GR team regarding the timeout, customer is still interested if that can be increase to at least reduce the number of timeouts**_- _**Can we increase on their infra/only QA stage this gloo timeout to 30s?**_
We kindly wait for your feedback.
Best regards,__

July 17  1:17 PM WEST

web

Yang Yang

Send ZenDesk private comment has been set: Hi Team,
There are currently discussion going on If we should increase Gloo timeout. I'll keep you posted. Thanks.

July 17  1:17 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:
Hi Team,
There are currently discussion going on If we should increase Gloo timeout. I'll keep you posted. Thanks.

July 17  1:17 PM WEST

web

Rootly

Send ZenDesk private comment has been unset

July 17  1:17 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:

July 17  8:21 PM WEST

web

Yang Yang

Send ZenDesk private comment has been set: Hi Team,
After further discussion and consideration, we decide NOT to increase the Gloo timeout. Because this won't help the situation. We correlated the Gloo Access log ( [https://outsystems.grafana.net/explore?schemaVersion=1&amp;panes=%7B%226xk%22%3A%7B%22dataso[&hellip;]2000%22%2C%22to%22%3A%221720643357000%22%7D%7D%7D&amp;orgId=1](https://outsystems.grafana.net/explore?schemaVersion=1&amp;panes=%7B%226xk%22%3A%7B%22datasource%22%3A%22grafanacloud-outsystemstest-logs%22%2C%22queries%22%3A%5B%7B%22datasource%22%3A%7B%22type%22%3A%22loki%22%2C%22uid%22%3A%22grafanacloud-outsystemstest-logs%22%7D%2C%22editorMode%22%3A%22code%22%2C%22expr%22%3A%22%7Bstamp%3D%7E%5C%22id-ga-eu-ce-1-01%5C%22%2C+k8s_namespace_name%3D%5C%22kube-gloo-system%5C%22%7D%5Cn%21%3D+%5C%22%2Fenvoy-hc%5C%22%5Cn%7C%7E+%5C%2265825faf-35f3-4158-b5a5-9b12424a846d%5C%22%5Cn%7C+json+%5Cn%7C+line_format+%5C%22%7B%7B.log%7D%7D%5C%22+%5Cn%7C+pattern+%60%5B%3Caccesslog_start_time%3E%5D+%5C%22%3Caccesslog_method%3E+%3Caccesslog_path%3E+%3Caccesslog_protocol%3E%5C%22+%3Caccesslog_response_code%3E+%3Caccesslog_response_flags%3E+%3Caccesslog_bytes_received%3E+%3Caccesslog_bytes_sent%3E+%3Caccesslog_duration%3E+%3Caccesslog_service_duration%3E+%5C%22%3Caccesslog_x_forward_for%3E%5C%22+%5C%22%3Caccesslog_user_agent%3E%5C%22+%5C%22%3Caccesslog_user_id%3E%5C%22+%5C%22%3Caccesslog_tenant_id%3E%5C%22+%5C%22%3Caccesslog_req_id%3E%5C%22+%5C%22%3Caccesslog_cf_id%3E%5C%22+%5C%22%3Caccesslog_authority%3E%5C%22+%5C%22%3Caccesslog_upstream_host%3E%5C%22+%5C%22%3Caccesslog_customer_ip%3E%5C%22%60%5Cn%7C+kubernetes_container_name%3D%5C%22gateway-proxy%5C%22+and+stream%3D%5C%22stdout%5C%22+and+accesslog_response_code%3D%7E%5C%225.*%5C%22+and+accesslog_method%3D%7E%5C%22.*%5C%22%5Cn%7C+line_format+%5C%22%7B%7B.accesslog_start_time%7D%7D%5C%5Ct%7B%7B.accesslog_method%7D%7D%5C%5Ct%7B%7B.accesslog_response_code%7D%7D%5C%5Ct%7B%7B.accesslog_response_flags%7D%7D%5C%5Ct%7B%7B.accesslog_duration%7D%7D%5C%5Ct%7B%7B.accesslog_x_forward_for%7D%7D%5C%5Ct%7B%7B.accesslog_customer_ip%7D%7D%5C%5Ct%7B%7B.accesslog_tenant_id%7D%7D%5C%5Ct%7B%7B.accesslog_cf_id%7D%7D%5C%5Ct%7B%7B.accesslog_path%7D%7D%5C%5Ct%7B%7B.accesslog_user_id%7D%7D%5C%22%22%2C%22queryType%22%3A%22range%22%2C%22refId%22%3A%22A%22%7D%5D%2C%22range%22%3A%7B%22from%22%3A%221720583552000%22%2C%22to%22%3A%221720643357000%22%7D%7D%7D&amp;orgId=1) ) and Keycloak timeout Error log ( [https://outsystems.grafana.net/explore?schemaVersion=1&amp;panes=%7B%22fgu%22%3A%7B%22dataso[&hellip;]2283%22%2C%22to%22%3A%221720643357689%22%7D%7D%7D&amp;orgId=1](https://outsystems.grafana.net/explore?schemaVersion=1&amp;panes=%7B%22fgu%22%3A%7B%22datasource%22%3A%22grafanacloud-outsystemstest-logs%22%2C%22queries%22%3A%5B%7B%22datasource%22%3A%7B%22type%22%3A%22loki%22%2C%22uid%22%3A%22grafanacloud-outsystemstest-logs%22%7D%2C%22editorMode%22%3A%22code%22%2C%22expr%22%3A%22%7Bk8s_namespace_name%3D%7E%5C%22keycloak-.*%5C%22%2C+ring%3D%5C%22ga%5C%22%2C+stamp%3D%7E%5C%22.*.*.*%5C%22%7D%5Cn%7C%7E+%5C%22timed+out%5C%22%5Cn%7C%7E%5C%22oauth.axione.fr%5C%22%5Cn%7C+json%5Cn%7C+kubernetes_container_name%3D%5C%22keycloak%5C%22%5Cn%7C+label_format+sev%3D%60%7B%7B+if+contains+%5C%22ERROR%5C%22+%28upper+.level%29+%7D%7DError%7B%7Belse+if+contains+%5C%22WARN%5C%22+%28upper+.level%29+%7D%7DWarning%7B%7Belse+if+contains+%5C%22INFO%5C%22+%28upper+.level%29+%7D%7DInformation%7B%7Belse+if+contains+%5C%22DEBUG%5C%22+%28upper+.level%29+%7D%7DDebug%7B%7Belse%7D%7D%7B%7B.level%7D%7D%7B%7Bend%7D%7D%60%5Cn%7C+label_format+cluster%3D%60%7B%7B.k8s_namespace_name+%7C+trimPrefix+%5C%22keycloak-cluster-%5C%22%7D%7D%60%5Cn%7C+label_format+traceid%3D%60%7B%7B.mdc_trace_id+%7C+substr+0+5%7D%7D%60%5Cn%7C+label_format+pod%3D%60%7B%7B.kubernetes_labels_statefulset_kubernetes_io_pod_name+%7C+trimPrefix+%5C%22keycloak-%5C%22%7D%7D%60%5Cn%7C+sev%3D%7E%5C%22Error%5C%22%5Cn%7C+line_format+%60%5B%7B%7B.stamp%7D%7D%5D+%5Bcluster%3A+%7B%7B.cluster%7D%7D%5D+%5Bpod%3A+%7B%7B.pod%7D%7D%5D+%5Btrace%3A+%7B%7B.traceid%7D%7D%5D+%7B%7B.log%7D%7D%60%22%2C%22queryType%22%3A%22range%22%2C%22refId%22%3A%22A%22%7D%5D%2C%22range%22%3A%7B%22from%22%3A%221720583552283%22%2C%22to%22%3A%221720643357689%22%7D%7D%7D&amp;orgId=1) ) and it indicates all requests timed out on Gloo also timed out in Keycloak ( you can also change to the recent time period to see they still match ) That means change Gloo timeout value won't help because they will still time out in Keycloak.We are open to discuss if there are any other ways we can help to unblock the situation for customer. Let us know. Thanks.

July 17  8:21 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:
Hi Team,
After further discussion and consideration, we decide NOT to increase the Gloo timeout. Because this won't help the situation. We correlated the Gloo Access log ( [https://outsystems.grafana.net/explore?schemaVersion=1&amp;panes=%7B%226xk%22%3A%7B%22dataso[&hellip;]2000%22%2C%22to%22%3A%221720643357000%22%7D%7D%7D&amp;orgId=1](https://outsystems.grafana.net/explore?schemaVersion=1&amp;panes=%7B%226xk%22%3A%7B%22datasource%22%3A%22grafanacloud-outsystemstest-logs%22%2C%22queries%22%3A%5B%7B%22datasource%22%3A%7B%22type%22%3A%22loki%22%2C%22uid%22%3A%22grafanacloud-outsystemstest-logs%22%7D%2C%22editorMode%22%3A%22code%22%2C%22expr%22%3A%22%7Bstamp%3D%7E%5C%22id-ga-eu-ce-1-01%5C%22%2C+k8s_namespace_name%3D%5C%22kube-gloo-system%5C%22%7D%5Cn%21%3D+%5C%22%2Fenvoy-hc%5C%22%5Cn%7C%7E+%5C%2265825faf-35f3-4158-b5a5-9b12424a846d%5C%22%5Cn%7C+json+%5Cn%7C+line_format+%5C%22%7B%7B.log%7D%7D%5C%22+%5Cn%7C+pattern+%60%5B%3Caccesslog_start_time%3E%5D+%5C%22%3Caccesslog_method%3E+%3Caccesslog_path%3E+%3Caccesslog_protocol%3E%5C%22+%3Caccesslog_response_code%3E+%3Caccesslog_response_flags%3E+%3Caccesslog_bytes_received%3E+%3Caccesslog_bytes_sent%3E+%3Caccesslog_duration%3E+%3Caccesslog_service_duration%3E+%5C%22%3Caccesslog_x_forward_for%3E%5C%22+%5C%22%3Caccesslog_user_agent%3E%5C%22+%5C%22%3Caccesslog_user_id%3E%5C%22+%5C%22%3Caccesslog_tenant_id%3E%5C%22+%5C%22%3Caccesslog_req_id%3E%5C%22+%5C%22%3Caccesslog_cf_id%3E%5C%22+%5C%22%3Caccesslog_authority%3E%5C%22+%5C%22%3Caccesslog_upstream_host%3E%5C%22+%5C%22%3Caccesslog_customer_ip%3E%5C%22%60%5Cn%7C+kubernetes_container_name%3D%5C%22gateway-proxy%5C%22+and+stream%3D%5C%22stdout%5C%22+and+accesslog_response_code%3D%7E%5C%225.*%5C%22+and+accesslog_method%3D%7E%5C%22.*%5C%22%5Cn%7C+line_format+%5C%22%7B%7B.accesslog_start_time%7D%7D%5C%5Ct%7B%7B.accesslog_method%7D%7D%5C%5Ct%7B%7B.accesslog_response_code%7D%7D%5C%5Ct%7B%7B.accesslog_response_flags%7D%7D%5C%5Ct%7B%7B.accesslog_duration%7D%7D%5C%5Ct%7B%7B.accesslog_x_forward_for%7D%7D%5C%5Ct%7B%7B.accesslog_customer_ip%7D%7D%5C%5Ct%7B%7B.accesslog_tenant_id%7D%7D%5C%5Ct%7B%7B.accesslog_cf_id%7D%7D%5C%5Ct%7B%7B.accesslog_path%7D%7D%5C%5Ct%7B%7B.accesslog_user_id%7D%7D%5C%22%22%2C%22queryType%22%3A%22range%22%2C%22refId%22%3A%22A%22%7D%5D%2C%22range%22%3A%7B%22from%22%3A%221720583552000%22%2C%22to%22%3A%221720643357000%22%7D%7D%7D&amp;orgId=1) ) and Keycloak timeout Error log ( [https://outsystems.grafana.net/explore?schemaVersion=1&amp;panes=%7B%22fgu%22%3A%7B%22dataso[&hellip;]2283%22%2C%22to%22%3A%221720643357689%22%7D%7D%7D&amp;orgId=1](https://outsystems.grafana.net/explore?schemaVersion=1&amp;panes=%7B%22fgu%22%3A%7B%22datasource%22%3A%22grafanacloud-outsystemstest-logs%22%2C%22queries%22%3A%5B%7B%22datasource%22%3A%7B%22type%22%3A%22loki%22%2C%22uid%22%3A%22grafanacloud-outsystemstest-logs%22%7D%2C%22editorMode%22%3A%22code%22%2C%22expr%22%3A%22%7Bk8s_namespace_name%3D%7E%5C%22keycloak-.*%5C%22%2C+ring%3D%5C%22ga%5C%22%2C+stamp%3D%7E%5C%22.*.*.*%5C%22%7D%5Cn%7C%7E+%5C%22timed+out%5C%22%5Cn%7C%7E%5C%22oauth.axione.fr%5C%22%5Cn%7C+json%5Cn%7C+kubernetes_container_name%3D%5C%22keycloak%5C%22%5Cn%7C+label_format+sev%3D%60%7B%7B+if+contains+%5C%22ERROR%5C%22+%28upper+.level%29+%7D%7DError%7B%7Belse+if+contains+%5C%22WARN%5C%22+%28upper+.level%29+%7D%7DWarning%7B%7Belse+if+contains+%5C%22INFO%5C%22+%28upper+.level%29+%7D%7DInformation%7B%7Belse+if+contains+%5C%22DEBUG%5C%22+%28upper+.level%29+%7D%7DDebug%7B%7Belse%7D%7D%7B%7B.level%7D%7D%7B%7Bend%7D%7D%60%5Cn%7C+label_format+cluster%3D%60%7B%7B.k8s_namespace_name+%7C+trimPrefix+%5C%22keycloak-cluster-%5C%22%7D%7D%60%5Cn%7C+label_format+traceid%3D%60%7B%7B.mdc_trace_id+%7C+substr+0+5%7D%7D%60%5Cn%7C+label_format+pod%3D%60%7B%7B.kubernetes_labels_statefulset_kubernetes_io_pod_name+%7C+trimPrefix+%5C%22keycloak-%5C%22%7D%7D%60%5Cn%7C+sev%3D%7E%5C%22Error%5C%22%5Cn%7C+line_format+%60%5B%7B%7B.stamp%7D%7D%5D+%5Bcluster%3A+%7B%7B.cluster%7D%7D%5D+%5Bpod%3A+%7B%7B.pod%7D%7D%5D+%5Btrace%3A+%7B%7B.traceid%7D%7D%5D+%7B%7B.log%7D%7D%60%22%2C%22queryType%22%3A%22range%22%2C%22refId%22%3A%22A%22%7D%5D%2C%22range%22%3A%7B%22from%22%3A%221720583552283%22%2C%22to%22%3A%221720643357689%22%7D%7D%7D&amp;orgId=1) ) and it indicates all requests timed out on Gloo also timed out in Keycloak ( you can also change to the recent time period to see they still match ) That means change Gloo timeout value won't help because they will still time out in Keycloak.We are open to discuss if there are any other ways we can help to unblock the situation for customer. Let us know. Thanks.

July 17  8:21 PM WEST

web

Rootly

Send ZenDesk private comment has been unset

July 17  8:21 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:

July 18  2:22 PM WEST

web

Rootly

NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
Hello team,
Thank you for the reply and feedback.
And regarding my other part of the communication:
_**Also, since customer is heavily affected and end users, we must exhaust our possibilities on them, I was reading the information from GR team regarding the timeout, customer is still interested if that can be increase to at least reduce the number of timeouts**_- _**Can we increase on their infra/only QA stage this gloo timeout to 30s?**_
We kindly wait for your feedback.
Best regards,__

July 18  2:22 PM WEST

web

Rootly

NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
Hello team,
Thank you for the reply and feedback.
And regarding my other part of the communication:
_**Also, since customer is heavily affected and end users, we must exhaust our possibilities on them, I was reading the information from GR team regarding the timeout, customer is still interested if that can be increase to at least reduce the number of timeouts**_- _**Can we increase on their infra/only QA stage this gloo timeout to 30s?**_
We kindly wait for your feedback.
Best regards,__

July 18  3:12 PM WEST

web

Rootly

Zendesk Private Comment has been changed to: ----------------------------------------------**Update to R&amp;D**
Hello team,
Thank you for the update and investigation, so according to your investigation, and let me see if I understand it correctly:
Basically from my understanding, we get the timeout on gloo of 15s, that in this example happens at 2024-07-10 06:29:42.680, however, we get the timeout on keycloak at 2024-07-10 06:31:32.135 meaning that even that when gloo cut the request, (and the end user sees the UT page) the response from IDP is not happening and is return roughly 2min after on keycloak as a timeout: Attachment - image.png- Just to make sure we understand this to convey to the customer.
Regarding other ways, if R&amp;D has any other suggestions we are open also to discuss, but we are also going to reinforce that this is indeed an issue on their side.Best regards,_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_

July 18  3:12 PM WEST

web

Rootly

NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
Hello team,
Thank you for the update and investigation, so according to your investigation, and let me see if I understand it correctly:
Basically from my understanding, we get the timeout on gloo of 15s, that in this example happens at 2024-07-10 06:29:42.680, however, we get the timeout on keycloak at 2024-07-10 06:31:32.135 meaning that even that when gloo cut the request, (and the end user sees the UT page) the response from IDP is not happening and is return roughly 2min after on keycloak as a timeout: Attachment - image.png- Just to make sure we understand this to convey to the customer.
Regarding other ways, if R&amp;D has any other suggestions we are open also to discuss, but we are also going to reinforce that this is indeed an issue on their side.Best regards,__

July 18  3:50 PM WEST

web

Jorge Marin

Send ZenDesk private comment has been set: Confirmed it indeed looks like their endpoint didnt return a response in time (15s timeout).
As an engineer, I would suggest them trying to setup another IDP (Azure AD, Linkedin, Apple, etc) and see if they have the same problem as with their custom IDP.
It is expected those IDPs work just fine, in which case it reinforces the idea of their IDP not returning a response in time.Maybe they can also try their third party idp from a tool external to OutSystems and see if they experience the same timeouts. For example they could try [https://oidcdebugger.com/](https://oidcdebugger.com/) or [https://psteniusubi.github.io/oidc-tester/authorization-code-flow.html](https://psteniusubi.github.io/oidc-tester/authorization-code-flow.html)Regarding regions, Keycloak is in eu-central-1 (Frankfurt) and their servers ([oauth.axione.fr/109.74.90.118](http://oauth.axione.fr/109.74.90.118)) seems to be located in France. There should be no good reason for network latency.

July 18  3:50 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:
Confirmed it indeed looks like their endpoint didnt return a response in time (15s timeout).
As an engineer, I would suggest them trying to setup another IDP (Azure AD, Linkedin, Apple, etc) and see if they have the same problem as with their custom IDP.
It is expected those IDPs work just fine, in which case it reinforces the idea of their IDP not returning a response in time.Maybe they can also try their third party idp from a tool external to OutSystems and see if they experience the same timeouts. For example they could try [https://oidcdebugger.com/](https://oidcdebugger.com/) or [https://psteniusubi.github.io/oidc-tester/authorization-code-flow.html](https://psteniusubi.github.io/oidc-tester/authorization-code-flow.html)Regarding regions, Keycloak is in eu-central-1 (Frankfurt) and their servers ([oauth.axione.fr/109.74.90.118](http://oauth.axione.fr/109.74.90.118)) seems to be located in France. There should be no good reason for network latency.

July 18  3:50 PM WEST

web

Rootly

Send ZenDesk private comment has been unset

July 18  3:50 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:

July 29  9:27 AM WEST

web

Jorge Marin

Send ZenDesk private comment has been set: Confirmed it indeed looks like their endpoint didnt return a response in time (15s timeout).&nbsp;  
As an engineer, I would suggest them trying to setup another IDP (Azure AD, Linkedin, Apple, etc) and see if they have the same problem as with their custom IDP.&nbsp;  
It is expected those IDPs work just fine, in which case it reinforces the idea of their IDP not returning a response in time.Maybe they can also try their third party idp from a tool external to OutSystems and see if they experience the same timeouts. For example they could try [https://oidcdebugger.com/](https://oidcdebugger.com/) or [https://psteniusubi.github.io/oidc-tester/authorization-code-flow.html](https://psteniusubi.github.io/oidc-tester/authorization-code-flow.html)Regarding regions, Keycloak is in eu-central-1 (Frankfurt) and their servers ([oauth.axione.fr/109.74.90.118](http://oauth.axione.fr/109.74.90.118)) seems to be located in France. There should be no good reason for network latency.

July 29  9:27 AM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:
Confirmed it indeed looks like their endpoint didnt return a response in time (15s timeout).&nbsp;  
As an engineer, I would suggest them trying to setup another IDP (Azure AD, Linkedin, Apple, etc) and see if they have the same problem as with their custom IDP.&nbsp;  
It is expected those IDPs work just fine, in which case it reinforces the idea of their IDP not returning a response in time.Maybe they can also try their third party idp from a tool external to OutSystems and see if they experience the same timeouts. For example they could try [https://oidcdebugger.com/](https://oidcdebugger.com/) or [https://psteniusubi.github.io/oidc-tester/authorization-code-flow.html](https://psteniusubi.github.io/oidc-tester/authorization-code-flow.html)Regarding regions, Keycloak is in eu-central-1 (Frankfurt) and their servers ([oauth.axione.fr/109.74.90.118](http://oauth.axione.fr/109.74.90.118)) seems to be located in France. There should be no good reason for network latency.

July 29  9:27 AM WEST

web

Rootly

Send ZenDesk private comment has been unset

July 29  9:27 AM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:

August 5  4:33 PM WEST

web

Jorge Marin

It has been aligned between Support and Identity teams (cc/ Francisco Oliveira) that we can close this issue on our side given the customer is taking long to reply

August 5  4:33 PM WEST

web

Jorge Marin

Incident has been resolved

August 5  4:33 PM WEST

web

Jorge Marin

Impact has been set: Customer not able to reliably log in with their third party idp

August 5  4:33 PM WEST

web

Jorge Marin

Resolution has been set: Looks like a problem on their side