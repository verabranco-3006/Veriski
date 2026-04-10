---
title: Retrospective-SEV2-Issue with Azure SSO Redirect in OutSystems ODC App
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4277010454/Retrospective-SEV2-Issue+with+Azure+SSO+Redirect+in+OutSystems+ODC+App
confluence_space: RKB
confluence_page_id: 4277010454
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV2-Issue with Azure SSO Redirect in OutSystems ODC App

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV2

Teams:&nbsp;trueBlueClient Runtime
#### 🕐 Timestamps
Started At:&nbsp;trueBlueJuly 3  1:39 PM WEST

Mitigated At:&nbsp;trueYellowJuly 10  2:31 PM WEST

Resolved At:&nbsp;trueGreenJuly 10  2:31 PM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/662-issue-with-azure-sso-redirect-in-outsystems-odc-app)
[Jira issue](https://outsystemsrd.atlassian.net/browse/RDINC-26382)

[Pagerduty incident](https://outsystems.pagerduty.com/incidents/Q25L3VV0G084QG)

[Slack channel](https://slack.com/app_redirect?channel=C07B8KY9X5X&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3028169)

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

Pedro Quintas
#### Summary
----------------------------------------------**ISSUE DESCRIPTION AND HOW TO REPRODUCE**- When redirecting to a different app after logging in with external provider (using **GetExternalLoginURL** and **RedirectURL**) we get an error screen:![](https://supportoutsystems.zendesk.com/attachments/token/n8IAQ8KlcEL2tPQDICL8WGj5p/?name=image.png)
- Was able to reproduce this on our sandbox and it seems an issue with the return URL when using external login:![](https://supportoutsystems.zendesk.com/attachments/token/vpKr3OU5NotNR1B69r5zXtdeT/?name=image.png)- If no **ReturnToURL** is provided, it works fine and redirects back to the app homepage.- Otherwise, if a **ReturnToURL** is provided for another app, it fails.
- Test available here: https://gs-sandbox-ga-eu-01-dev.outsystems.app/JPT_Login/Screen2- Empty redirect URL &gt; click External login &gt; complete login &gt; redirected to app homepage (which has no permissions but can be assumed success).- Redirect URL is `https://gs-sandbox-ga-eu-01-dev.outsystems.app/JPT_RestUTF` (note different app!) &gt; click External login &gt; complete login &gt; error page:![](https://supportoutsystems.zendesk.com/attachments/token/ieCkN586r5DmmVjpIEngnhTuZ/?name=image.png)![](https://supportoutsystems.zendesk.com/attachments/token/n8IAQ8KlcEL2tPQDICL8WGj5p/?name=image.png)- Redirect URL is `https://gs-sandbox-ga-eu-01-dev.outsystems.app/JPT_RestUTF` &gt; click Go to other app directly &gt; success:![](https://supportoutsystems.zendesk.com/attachments/token/XuoqtIlOgLFGH84nCNJir2J2c/?name=image.png)![](https://supportoutsystems.zendesk.com/attachments/token/oV5v5SfirnTI7K8rMioyDlDWG/?name=image.png)
- App attached to Jira.**IMPACT ON THE CUSTOMER**- Development;
- Customer migrating from O11 and is targeting the completion of this migration by 2nd week of July;
- Customer unable to redirect to different apps when logging in via external identity provider.**TROUBLESHOOTING STEPS &amp; WORKAROUND**- When using **RedirectToUrl** with just the other app URL it works without issues, it only fails when redirecting back from the external identity provider.
- Also noticed from HAR file the following:- The first redirect that occurs (result from **GetExternalLoginURL**) is the following:
`/auth?client_id=client_runtime&amp;scope=openid&amp;redirect_uri=https%3A%2F%2Fgs-sandbox-ga-eu-01-dev.outsystems.app%2FJPT_Login%2F_RedirectLogin%3Fcallback_url%3Dhttps%253A%252F%252Fgs-sandbox-ga-eu-01-dev.outsystems.app%252FJPT_RestUTF%252F&amp;response_type=code&amp;kc_idp_hint=7db6a225-ebf2-48df-b496-dae112dd186c`- If we parse this via https://www.urldecoder.org/, we get the following:
`/auth?client_id=client_runtime&amp;scope=openid&amp;redirect_uri=https://gs-sandbox-ga-eu-01-dev.outsystems.app/JPT_Login/_RedirectLogin?callback_url=https%3A%2F%2Fgs-sandbox-ga-eu-01-dev.outsystems.app%2FJPT_RestUTF%2F&amp;response_type=code&amp;kc_idp_hint=7db6a225-ebf2-48df-b496-dae112dd186c&nbsp;`- If we parse just the resulting `callback_url` via https://www.urldecoder.org/, we get the following:
`https://gs-sandbox-ga-eu-01-dev.outsystems.app/JPT_RestUTF/&amp;response_type=code&amp;kc_idp_hint=7db6a225-ebf2-48df-b496-dae112dd186c`- Note that following `/JPT_RestUTF/` we immediately get a `&amp;` without any `?` which is not correct.- In fact, accessing just https://gs-sandbox-ga-eu-01-dev.outsystems.app/JPT_RestUTF/&amp;response_type=code results in a 404 error.![](https://supportoutsystems.zendesk.com/attachments/token/iNLS67B3xTqN3ThRDFPzygUls/?name=image.png)- Whereas if we swap the `&amp;` for a `?` it works:![](https://supportoutsystems.zendesk.com/attachments/token/1JyPc9wREkjlFDfl7EKpmjX98/?name=image.png)**TECH DATA OR ANY OTHER RELEVANT INFO**
N/A_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 RetrospectiveinfoDetails
**Ring:** ga
**System-wide impact:**&nbsp; 
**Tenant ID:** 7be0a7b8-a8a6-4cea-ba7f-c95fbb11e444
**Tenant Prefix:** cpmining
**Routing Error Code:** N/A
**Product Area:** Phoenix::Application Runtime::Access management::External Authentication
### Impact:
None, what the user was trying to do is not supported.
### Investigation and troubleshooting findings:### Resolution:
Evaluated the possibility of supporting what the customer was requesting.
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/662-issue-with-azure-sso-redirect-in-outsystems-odc-app)

**Date**

**Source**

**User**

**Event**
July 3  1:10 PM WESTwebRootly
created an alert via
July 3  1:10 PM WESTwebRootly
Rootly created this incident
July 3  1:10 PM WESTwebRootly
In triage date has been set to July 3  1:10 PM WEST
July 3  1:10 PM WESTwebRootly[Slack Channel](https://slack.com/app_redirect?channel=C07B8KY9X5X&amp;team=T041063TZ) has been createdJuly 3  1:10 PM WESTwebRootly
Ring: ga
System-wide impact:  
Tenant ID: 7be0a7b8-a8a6-4cea-ba7f-c95fbb11e444
Tenant Prefix: cpmining
Routing Error Code: N/A
Product Area: Phoenix::Application Runtime::Access management::External Authentication
July 3  1:10 PM WESTwebRootly[PagerDuty Incident](https://outsystems.pagerduty.com/incidents/Q25L3VV0G084QG) has been created.
📧 Notified Rodrigo Bernardo by email.&nbsp;&nbsp;📲 Notified Rodrigo Bernardo by push notification.  (via iPhone)&nbsp;&nbsp;📲 Notified Rodrigo Bernardo by push notification.  (via iPhone)&nbsp;&nbsp;📲 Notified Rodrigo Bernardo by push notification.  (via iPhone)July 3  1:10 PM WESTwebRootlyRodrigo Andr&eacute; Bernardo has been assigned as EngineerJuly 3  1:11 PM WESTwebRootly
Rodrigo Bernardo acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q25L3VV0G084QG). (via Mobile)
July 3  1:39 PM WESTwebRodrigo Andr&eacute; Bernardo
Incident has been started
July 3  1:40 PM WESTwebRootly
Pagerduty Integrations acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q25L3VV0G084QG). (via Mobile)
July 3  1:41 PM WESTwebRodrigo Andr&eacute; BernardoSend ZenDesk private comment has been set: Hi Global Support,Can you share the HAR file, please?Thanks in advance.July 3  1:41 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hi Global Support,Can you share the HAR file, please?Thanks in advance.
July 3  1:41 PM WESTwebRootlySend ZenDesk private comment has been unsetJuly 3  1:41 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

July 3  1:41 PM WESTwebRodrigo Andr&eacute; BernardoSwarm has been set: Client RuntimeJuly 3  1:41 PM WESTwebRootly
Pagerduty Integrations added Rita Tinoco as responder in [PagerDuty](https://outsystems.pagerduty.com/incidents/Q25L3VV0G084QG)
July 3  1:47 PM WESTwebRootly
Rita Tinoco joined this [PagerDuty](https://outsystems.pagerduty.com/incidents/Q25L3VV0G084QG) incident.
July 3  3:23 PM WESTwebCarlos Xavier
Teams has been removed: Identity Core
July 3  3:23 PM WESTwebCarlos XavierCarlos Xavier has been assigned as EngineerJuly 3  4:50 PM WESTwebCarlos XavierSend ZenDesk private comment has been set: Hi Support,  We do not support redirecting to a different app from the login. All redirect URLs have their domain part stripped and are then interpreted as being URLs internal to the app. In order for the customer to achieve the intended behavior, they may instead redirect from the login to an app screen that then performs the redirect. I did a few changes to the provided OML and now the app stores the intended redirect URL in a client variable and supplies the GetExternalLoginURL action with a redirect URL to a new screen. This screen takes the redirect URL from the client variable, cleans the variable, and then performs the navigation to the intended URL. I have attached the modified OML.  We'll check if we want to be less restrictive with the redirect URLs and add somewhere in the future the possibility of redirecting to other apps in the same domain from the login redirect URL.  Let me know if you need further assistance.  Best regards,  
Carlos XavierJuly 3  4:50 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hi Support,  We do not support redirecting to a different app from the login. All redirect URLs have their domain part stripped and are then interpreted as being URLs internal to the app. In order for the customer to achieve the intended behavior, they may instead redirect from the login to an app screen that then performs the redirect. I did a few changes to the provided OML and now the app stores the intended redirect URL in a client variable and supplies the GetExternalLoginURL action with a redirect URL to a new screen. This screen takes the redirect URL from the client variable, cleans the variable, and then performs the navigation to the intended URL. I have attached the modified OML.  We'll check if we want to be less restrictive with the redirect URLs and add somewhere in the future the possibility of redirecting to other apps in the same domain from the login redirect URL.  Let me know if you need further assistance.  Best regards,  
Carlos Xavier
July 3  4:50 PM WESTwebRootlySend ZenDesk private comment has been unsetJuly 3  4:50 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

July 3  4:54 PM WESTwebCarlos XavierSend ZenDesk private comment has been set: Hi Support,  I don't think Rootly was able to attach the file... I added it to the JIRA issue: https://outsystemsrd.atlassian.net/browse/RDINC-26382  It's called \`JPT\_Login\_workaround.oml\`.  Best regards,  
Carlos XavierJuly 3  4:54 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hi Support,  I don't think Rootly was able to attach the file... I added it to the JIRA issue: https://outsystemsrd.atlassian.net/browse/RDINC-26382  It's called \`JPT\_Login\_workaround.oml\`.  Best regards,  
Carlos Xavier
July 3  4:54 PM WESTwebRootlySend ZenDesk private comment has been unsetJuly 3  4:54 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

July 9 10:12 AM WESTwebRootlyZenDesk Event Type has been set: solvedJuly 9 10:12 AM WESTwebRootly
The Global Support team marked this incident as closed in ZenDesk.
July 9 10:43 AM WESTwebPedro QuintasPedro Quintas has been assigned as EngineerJuly 10  2:23 PM WESTwebRita Tinoco
This issue is solved on Zendesk. Rootly doesn't seem to update that. Closing the ticket. Jira Link -&gt; https://outsystemsrd.atlassian.net/browse/RDINC-26382
July 10  2:31 PM WESTwebPedro Quintas
Incident has been resolved
July 10  2:31 PM WESTwebPedro QuintasImpact has been set: None, what the user was trying to do is not supported.July 10  2:31 PM WESTwebPedro QuintasResolution has been set: Evaluated the possibility of supporting what the customer was requesting.