---
title: Retrospective-SEV2-Sub-ticket of #3019784 (Azure IdP Group mapping not working)
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4264296573/Retrospective-SEV2-Sub-ticket+of+3019784+Azure+IdP+Group+mapping+not+working
confluence_space: RKB
confluence_page_id: 4264296573
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV2-Sub-ticket of #3019784 (Azure IdP Group mapping not working)

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV2

Teams:&nbsp;trueBlueIdentity Business
#### 🕐 Timestamps
Started At:&nbsp;trueBlueJuly 2 10:04 AM WEST

Mitigated At:&nbsp;trueYellowJuly 4 12:28 PM WEST

Resolved At:&nbsp;trueGreenJuly 4 12:28 PM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/654-sub-ticket-of-3019784-azure-idp-group-mapping-not-working)
[Pagerduty incident](https://outsystems.pagerduty.com/incidents/Q33OWGUYJLJGJY)

[Slack channel](https://slack.com/app_redirect?channel=C07ALRDE74L&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3029903)

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

Francisco Magalh&atilde;es
#### Summary
----------------------------------------------**ISSUE DESCRIPTION AND HOW TO REPRODUCE**
Customer is facing current limitations with the Check Roles in another app via REST/Service Action + External IDP configuration + Group Mappings, where the common Menu is not loading since checkRoles are not working:
To reproduce:
Assigned directly to user a Role and the CheckRole via Rest returns true to the Role and Menu Appears:![](https://supportoutsystems.zendesk.com/attachments/token/pj2Mhvjjm521dgk2Rwtat9W1M/?name=image.png)![](https://supportoutsystems.zendesk.com/attachments/token/oAC46berdyvOBTcg5qbhC1gFk/?name=image.png)![](https://supportoutsystems.zendesk.com/attachments/token/1nIwzGIiV8aQTOkQ03szmWGXN/?name=image.png)Remove the enduser role directly and assign only on Group Mapping:![](https://supportoutsystems.zendesk.com/attachments/token/cUtCnV60oMVVKVZNipVopgvP2/?name=image.png)![](https://supportoutsystems.zendesk.com/attachments/token/krkNdVhd8ZNKNJzoBtHzdXoo6/?name=image.png)![](https://supportoutsystems.zendesk.com/attachments/token/un5cDomF4MsqOBnjeHbr0hZqo/?name=image.png)
The menu wont load.**IMPACT ON THE CUSTOMER**
High, blocking go live this week**TROUBLESHOOTING STEPS &amp; WORKAROUND**
We saw this pattern on the past with the escalation https://outsystemsrd.atlassian.net/browse/RDINC-22229 where we got to the conclusion that we are not supporting the action that the customer is trying to perform right now.
However, was aligned that a future support will be made, and currently we reach another customer that develop everything and now is block the go live due to this.
The workaround of assign roles to users is not acceptable since they have more than 60 roles and several users.
To replicate directly on customer infra R&amp;D can:- https://interprenet-dev.outsystems.app/AuthenticationLibrary/LandingPage- Use credentials- garcia.joao@interprenet.net
jLcwhF*@t%fs^PTjO@m2nWIbWe are engaging R&amp;D since we seek if R&amp;D meanwhile has another workaround for this type of scenarios, because changing the way of development might not be acceptable, or we might once again need the help of PM and field teams to develop something for the customer, however, we fear more and more customers use this type of architecture and we will be blocked over and over again,We also have the old POC live with a simpler scenario attached, and the symptoms might lead the case to BE but the objective is to reach ID Business, feel free to reach me for any live test on their tenant.**TECH DATA OR ANY OTHER RELEVANT INFO**
Ring: ga
Tenant Id: 6c7e9bc8-f289-4140-9383-c9a75b88f6ef
Tenant Prefix: interprenet
Region: us-east-1
JXF.PKP.QNT.AVE.O1B.JNY.0AY.QOU
support_level_8x5
Ends in 2024-08-27_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_Attachment(s):
POC Paulo.zip - https://supportoutsystems.zendesk.com/attachments/token/wyUslZCedE6qlSii3Dgympk4i/?name=POC+Paulo.zip
## 📝 RetrospectiveinfoDetails
**Ring:** ga
**System-wide impact:**&nbsp; No
**Tenant ID:** 6c7e9bc8-f289-4140-9383-c9a75b88f6ef
**Tenant Prefix:** interprenet
**Routing Error Code:** N/A
**Product Area:** Phoenix::Application Runtime::Logic Flows::Integrations::REST - Consume
### Impact:
Customer was not able to check roles that were associated with Idp claims, resulting in wrong visibility of UI elements.
### Investigation and troubleshooting findings:
The customer can only check for &quot;Idp Group Mapping&quot; roles in the app where the user is logged in. These role assignments are dynamic - not persisted in the database - and depend on the context of the logged in user.

In this case, authentication was being done in a different app than the one where the role was being checked. For that reason, the platform was always responding as if the user did not have the role.
### Resolution:
The customer has implemented a workaround that was different from the one suggested by the team. Authentication is now being done in the same app where the role is being checked.
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/654-sub-ticket-of-3019784-azure-idp-group-mapping-not-working)

**Date**

**Source**

**User**

**Event**
July 1  3:56 PM WESTwebRootly
created an alert via
July 1  3:56 PM WESTwebRootly
Rootly created this incident
July 1  3:56 PM WESTwebRootly
In triage date has been set to July 1  3:56 PM WEST
July 1  3:56 PM WESTwebRootly[Slack Channel](https://slack.com/app_redirect?channel=C07ALRDE74L&amp;team=T041063TZ) has been createdJuly 1  3:57 PM WESTwebRootly[PagerDuty Incident](https://outsystems.pagerduty.com/incidents/Q33OWGUYJLJGJY) has been created.
📧 Notified Rui Garcia by email.&nbsp;&nbsp;📧 Notified Rui Garcia by email.&nbsp;&nbsp;📱 Notified Rui Garcia by SMS.July 1  3:57 PM WESTwebRootlyRui Garcia has been assigned as EngineerJuly 1  3:57 PM WESTwebRootly
Ring: ga
System-wide impact:  
Tenant ID: 6c7e9bc8-f289-4140-9383-c9a75b88f6ef
Tenant Prefix: interprenet
Routing Error Code: N/A
Product Area: Phoenix::Application Runtime::Logic Flows::Integrations::REST - Consume
July 1  3:58 PM WESTwebRootly
Rui Garcia acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q33OWGUYJLJGJY). (via Phone)
July 1  4:07 PM WESTwebRootly
This incident was instantiated in Jira: RDINC-26172. Please work the incident using Rootly
July 1  4:08 PM WESTwebRootlyZendesk Private Comment has been set: ----------------------------------------------**Update to R&amp;D**
Forgot to meantion the REST is called when loading the menu from the library Theme to the main app to check the roles:![](https://supportoutsystems.zendesk.com/attachments/token/kh7rPdf1WMT6Ycrw9ZOvuLYMq/?name=image.png)__July 1  4:08 PM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:

July 1  4:09 PM WESTwebRootly
Delegated to EP for Platform Identity Business by Rui Garcia through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q33OWGUYJLJGJY)
July 1  4:10 PM WESTwebRootly
Francisco Magalh&atilde;es acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q33OWGUYJLJGJY). (via Phone)
July 1  4:10 PM WESTwebRootly
Francisco Magalh&atilde;es acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q33OWGUYJLJGJY). (via Phone)
July 1  4:14 PM WESTwebRui Garcia
Teams has been added: Identity Business
July 1  4:14 PM WESTwebRui Garcia
Teams has been removed: Backend Runtime
July 1  4:57 PM WESTwebRootly
This incident was instantiated in Jira: RDINC-26172. Please work the incident using Rootly
July 2 10:04 AM WESTwebFrancisco Magalh&atilde;es
Incident has been started
July 2 10:04 AM WESTwebRootly
Pagerduty Integrations acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q33OWGUYJLJGJY). (via Phone)
July 2 10:36 AM WESTwebFrancisco Magalh&atilde;esFrancisco Magalh&atilde;es has been assigned as EngineerJuly 2 10:38 AM WESTwebFrancisco Magalh&atilde;es
Identity currently doesn't support this feature, and at the moment the only workaround is the one mentioned by support, which is also stated as &quot;not acceptable&quot;.The team is working together to find a better solution, if possible.
July 2  1:27 PM WESTwebFrancisco Magalh&atilde;esSend ZenDesk private comment has been set: Hello support,As you are aware from [RDINC-22229](https://outsystemsrd.atlassian.net/browse/RDINC-22229), the list of roles is generated during the user login and is currently not persisted. Therefore, it can only be retrieved accurately for the user that is logged in the in the application making the call to `CheckAppRole`.A next phase of this feature ([RPOR-21024](https://outsystemsrd.atlassian.net/browse/RPOR-21024)) adds persistence for that &quot;dynamic link information&quot; so that it can be reported as the result of `CheckAppRole`. However, persistence only happens on login. In other words, `HasRole` will be `true` if the user had that role in the last time they logged in.The group mapping was designed with a focus on the logged in user. In this case, there is another layer of authorization, implemented in the Authentication Library, where the user is technically not logged-in in. We would like to understand if this isolation is the recommended approach.I understand it may not be acceptable to assign each role to each user. Please consider assigning each _user _to an _End-user group _containing all the necessary roles. If need be, we can involve Product Management on this, to align the expectations with the client.July 2  1:27 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hello support,As you are aware from [RDINC-22229](https://outsystemsrd.atlassian.net/browse/RDINC-22229), the list of roles is generated during the user login and is currently not persisted. Therefore, it can only be retrieved accurately for the user that is logged in the in the application making the call to `CheckAppRole`.A next phase of this feature ([RPOR-21024](https://outsystemsrd.atlassian.net/browse/RPOR-21024)) adds persistence for that &quot;dynamic link information&quot; so that it can be reported as the result of `CheckAppRole`. However, persistence only happens on login. In other words, `HasRole` will be `true` if the user had that role in the last time they logged in.The group mapping was designed with a focus on the logged in user. In this case, there is another layer of authorization, implemented in the Authentication Library, where the user is technically not logged-in in. We would like to understand if this isolation is the recommended approach.I understand it may not be acceptable to assign each role to each user. Please consider assigning each _user _to an _End-user group _containing all the necessary roles. If need be, we can involve Product Management on this, to align the expectations with the client.
July 2  1:27 PM WESTwebRootlySend ZenDesk private comment has been unsetJuly 2  1:27 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

July 4  9:39 AM WESTwebRootlyZenDesk Event Type has been set: solvedJuly 4  9:39 AM WESTwebRootly
The Global Support team marked this incident as closed in ZenDesk.
July 4 10:28 AM WESTwebRootlyZendesk Private Comment has been changed to: ----------------------------------------------**Update to R&amp;D**
Hello Francisco and all team,Apologize, but the customer close the case since they found another solution, due to that we went on a call a few minutes ago with customer that explain to us another way to achieve what they pretend.When they perform the login on Authentication Library they redirect to a landing page:- ![](https://supportoutsystems.zendesk.com/attachments/token/vylZDDIsMgC4Fa4KF4hrZuF3O/?name=image.png)
They start to fetch the userid there, and they add a client action:- ![](https://supportoutsystems.zendesk.com/attachments/token/xY2Mk0xrbzkQpf4GReHle1nKg/?name=image.png)
On this logic at high level, inside the OnAfterLogin, they have this:- ![](https://supportoutsystems.zendesk.com/attachments/token/B7ZqiU5xbv22JicM1Ji5ZMvRZ/?name=image.png)
Where they perform the role validation at server side instead of client side:- ![](https://supportoutsystems.zendesk.com/attachments/token/cuPV2cOFu7BwWe4tUO0QFOQvp/?name=image.png)
Then they serialize the Menu with the Roles that they pretend with that user to a structure:- ![](https://supportoutsystems.zendesk.com/attachments/token/Cq4aGwZmIfXeXmRq6L8UmCyx1/?name=image.png)
After that, since the menu is built on the theme library, they deserialize the information that was save on the structure at client side via custom javascript:- ![](https://supportoutsystems.zendesk.com/attachments/token/XCBRrINrdpEIHM0bWokCTDQm0/?name=image.png)
- ![](https://supportoutsystems.zendesk.com/attachments/token/FXgi8P3g6I7tJrVckZ4km3A2n/?name=image.png)- This just open doors since it made at client side to someone manipulating the Data, however, since screen have the roles the only thing and attacker can do is change the menu itself, not gaining access.- This also removes the use of RESTs, where actually customer said that gain several AOs- Im attaching for reference both omls updated- InterprenetBaseTheme_TH.oml
Authentication Library.oml
Best regards,_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_Attachment(s):
Authentication Library.oml - https://supportoutsystems.zendesk.com/attachments/token/BOIO68btGSFwlPbS3TGWMYrDf/?name=Authentication+Library.omlInterprenetBaseTheme_TH.oml - https://supportoutsystems.zendesk.com/attachments/token/SkvuBc8salcELLFIxT6blfrkG/?name=InterprenetBaseTheme_TH.omlJuly 4 10:28 AM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:

July 4 12:28 PM WESTwebFrancisco Magalh&atilde;es
Incident has been resolved
July 4 12:28 PM WESTwebFrancisco Magalh&atilde;esSystem-wide impact has been set: NoJuly 4 12:28 PM WESTwebFrancisco Magalh&atilde;esImpact has been set: Customer was not able to check roles that were associated with Idp claims, resulting in wrong visibility of UI elements.July 4 12:28 PM WESTwebFrancisco Magalh&atilde;esInvestigation and troubleshooting findings has been set: The customer can only check for &quot;Idp Group Mapping&quot; roles in the app where the user is logged in. These role assignments are dynamic - not persisted in the database - and depend on the context of the logged in user.In this case, authentication was being done in a different app than the one where the role was being checked. For that reason, the platform was always responding as if the user did not have the role.July 4 12:28 PM WESTwebFrancisco Magalh&atilde;esResolution has been set: The customer has implemented a workaround that was different from the one suggested by the team. Authentication is now being done in the same app where the role is being checked.