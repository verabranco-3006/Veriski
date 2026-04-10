---
title: Retrospective-SEV2-Azure IdP Group mapping not working
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4333273222/Retrospective-SEV2-Azure+IdP+Group+mapping+not+working
confluence_space: RKB
confluence_page_id: 4333273222
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV2-Azure IdP Group mapping not working

## 📘 Overview
Author:&nbsp;Rootlytrue

Severity:&nbsp;SEV2Redtrue

Teams:&nbsp;Identity CoreBluetrue
#### 🕐 Timestamps
Started At:&nbsp;August 5 12:16 PM WESTBluetrue (wrong check JIRA)

Mitigated At:&nbsp;August 5 12:19 PM WESTYellowtrue (wrong check JIRA)

Resolved At:&nbsp;August 5 12:19 PM WESTGreentrue (wrong check JIRA)
#### 🔗 Links
[Incident Page](https://rootly.com/account/incidents/631-azure-idp-group-mapping-not-working)

[Pagerduty incident](https://outsystems.pagerduty.com/incidents/Q1PB3GHPM21O2H)

[Slack channel](https://slack.com/app_redirect?channel=C079FH9FC95&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3019784)

[Jira ticket](https://outsystemsrd.atlassian.net/browse/RDINC-25811)

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

Rui Garcia
#### Summary
----------------------------------------------**ISSUE DESCRIPTION AND HOW TO REPRODUCE**
The customer in QA authentication via External IDP Azure/entra doesn't work, however, it worked a few weeks ago according to the customer.
The main issue at this point is that authentication is not working at all via Azure having the following errors:- https://interprenet-test.outsystems.app/auth/realms/07eef547-a7ce-47b7-a5f7-51dd92416ec1/login-actions/first-broker-login?client_id=client_runtime&amp;tab_id=PAMf4my9W-0- ![](https://supportoutsystems.zendesk.com/attachments/token/nQHBhXuDovB2wc1hBkkrJzM0s/?name=image.png)**IMPACT ON THE CUSTOMER**
High, blocking enrollment of users on QA to test the app for going live on August 1st.**TROUBLESHOOTING STEPS &amp; WORKAROUND**- This error doesn't seem to appear on Identity, however, other errors/warnings are associated every time the login fails at CR:- https://outsystems.grafana.net/d/cdeqzn1jj77cwe/general-troubleshooting?orgId=1&amp;var-ring=ga&amp;var-tenant=6c7e9bc8-f289-4140-9383-c9a75b88f6ef&amp;var-application=eb393d1e-8482-47a2-8a5f-bb79f00b5274&amp;var-application=a987ff0d-8239-4af1-8ee2-ccbb187a0d48&amp;var-cluster=runnp&amp;var-cluster_old=All&amp;var-severity=Warning&amp;var-severity=Error&amp;var-severity=Critical&amp;var-runtime=All&amp;var-filter=&amp;var-exclude=&amp;var-region=us-east-1&amp;var-traceDuration=All&amp;var-environment=All&amp;var-regionShort=ga-us-east-1-01&amp;var-tenant_prefix=interprenet&amp;var-module_name=&amp;from=1719410400000&amp;to=1719413999000- ![](https://supportoutsystems.zendesk.com/attachments/token/cRqfEAoWaCwQTXuMliWH3ENUa/?name=image.png)- os_default_id not available, fallback to cognito- No identity provider configurations found for type &quot;cognito&quot;.- At the identity level, I didn't detect anything unusual by searching either by tenantid, realm or providerID:- https://outsystems.grafana.net/d/cdh4sw1jvc8aof/identity-logs?orgId=1&amp;var-rings=ga&amp;var-regionShort=us-east-1&amp;var-severity=Error&amp;var-severity=Warning&amp;var-severity=Information&amp;var-severity=Debug&amp;var-search=07eef547-a7ce-47b7-a5f7-51dd92416ec1&amp;from=1719410400000&amp;to=1719413999000- Tenandid -&gt; 6c7e9bc8-f289-4140-9383-c9a75b88f6ef- realm -&gt;07eef547-a7ce-47b7-a5f7-51dd92416ec1- providerID -&gt; 3c16af09-7fd9-4f97-8f7e-c4b72c36cd07- Seeing that authentication is not working at QA at all for any users we suspect that something at Azure might be misconfigured, so we went to all configurations:- Redirect URLs were double check since the enterprise application is the same for all stages so if it works on DEv should work on QA cause the groups, etc is all the same:- ![](https://supportoutsystems.zendesk.com/attachments/token/3NH7ScyjD23WjjMfFollFZNa3/?name=image.png)- ![](https://supportoutsystems.zendesk.com/attachments/token/VUePoRMTClufb1jE3Pr9wvnu3/?name=image.png)- We detect nothing unusual with configurations we have on our tenant for Dev and QA also so we compare everything and everything seems to fit:- We also double-check the sign-in logs on Azure and they return a success from the Azure side- We test a sample app and the behavior is the same- We did the traditional unassign and assign IDP from the Stage but the error persists between our call with a customer.Detect some situations with this endpoint, especially on Frist-broken-login with a recent bug detected and very recently, but don't know it would be related for sure:- https://outsystemsrd.atlassian.net/issues/?jql=text%20~%20%22first-broker-login%22
- ![](https://supportoutsystems.zendesk.com/attachments/token/GlIhu8dGpaha9jrwrEVfCfmM1/?name=image.png)Would like to request to Identity team in order understand if we have indeed an issue on our side, because, the azure configurations are the same as DEV so doesnt make much sense not working on QA, if R&amp;D needs any more info please let us know.**TECH DATA OR ANY OTHER RELEVANT INFO**
Ring: ga
Tenant Id: 6c7e9bc8-f289-4140-9383-c9a75b88f6ef
Tenant Prefix: interprenet
Region: us-east-1
JXF.PKP.QNT.AVE.O1B.JNY.0AY.QOU_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 Retrospective### Details
**Ring:** ga
**System-wide impact:**&nbsp; 
**Tenant ID:** 6c7e9bc8-f289-4140-9383-c9a75b88f6ef
**Tenant Prefix:** interprenet
**Routing Error Code:** N/A
**Product Area:** Phoenix::Application Runtime::Access management::Authorization
### Impact:
Failed logins for users who already logged in via an IdP that was first enabled then disabled then re-enabled.
### Investigation and troubleshooting findings:### Resolution:
- 
Workaround: Asked customer to create a second IdP with the exact same configuration as the old one. Users were able to login again. The new IdP worked just for the sake of being new.

- 
Reverted change that introduced the bug.

## Tasks performed during incident resolution:
&nbsp;Investigation

Linked to an existing already reported bug

Suggested remediation
## Executive Summary
[Guidelines](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4144496679/Incident+Retrospectives+-+Playbook#STEP-3---Write-the-Executive-Summary)

- 
What was the actual problem?

- 
Customer unable to login with their configured third party idp

- 
What was the real impact on OutSystems and Customers?

- 
One specific customer complained they couldnt login with third party idp

- 
The bug already existed and would have affected other customers

- 
What were the Root causes of the incident?

- 
A new feature removed the need for recreating Keycloak configuration, which caused internal Keycloak users not to be deleted. Then Keycloak logic needs to link accounts that seem similar but we dont allow that flow to avoid showing the customer internal Keycloak pages that are irrelevant. This turned into an &quot;unexpected error happened&quot; page

- 
What actions will be taken to avoid reoccurrence?

- 
Fix the bug RDPIDT-2379ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

## Root Causes 
[Guidelines](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4144496679/Incident+Retrospectives+-+Playbook#STEP-1---Perform-the-Root-Cause-Analysis)

New realm update behavior doesn't delete users (as replays did). This causes Keycloak to require linking between these existing users and new IdPs. But we don't have a page for that, so Keycloak just shows the &quot;unexpected error happens&quot; page.

- 
Users couldn't log in via a specific IdP - Because Keycloak would present an &quot;unexpected error happened&quot; page

- 
Because Keycloak required the user to be linked to the IdP

- 
Because that IdP had been deleted and re-created in Keycloak

- 
Because that IdP had been enabled then disabled in Portal

- 
Because the user already existed in Keycloak

- 
Because the new realm update behavior does not delete users from Keycloak

If the customer needs formal RCA, please fill out the following field with the document URL

[Please follow these instructions and place the RCA URL in the field below.](https://docs.google.com/document/d/13rXmBsOJh73nV2D6Z17SIBGBu2HOTWty5ddsvU000JM/edit#heading=h.bqxasxszr5q)

RCA URL

&lt;Place the URL of the customer RCA here if you have created one&gt;
## ⌛ Timeline
[View on Rootly](https://rootly.com/account/incidents/631-azure-idp-group-mapping-not-working)

**Date**

**Source**

**User**

**Event**

June 26  4:31 PM WEST

web

Rootly

created an alert via

June 26  4:31 PM WEST

web

Rootly

Rootly created this incident

June 26  4:31 PM WEST

web

Rootly

In triage date has been set to June 26  4:31 PM WEST

June 26  4:31 PM WEST

web

Rootly

[Slack Channel](https://slack.com/app_redirect?channel=C079FH9FC95&amp;team=T041063TZ) has been created

June 26  4:31 PM WEST

web

Rootly

[PagerDuty Incident](https://outsystems.pagerduty.com/incidents/Q1PB3GHPM21O2H) has been created.

📱 Notified Rui Garcia by SMS.

&nbsp;&nbsp;

📧 Notified Rui Garcia by email.

&nbsp;&nbsp;

📧 Notified Rui Garcia by email.

June 26  4:31 PM WEST

web

Rootly

Ring: ga
System-wide impact:  
Tenant ID: 6c7e9bc8-f289-4140-9383-c9a75b88f6ef
Tenant Prefix: interprenet
Routing Error Code: N/A
Product Area: Phoenix::Application Runtime::Access management::Authorization

June 26  4:31 PM WEST

web

Rootly

Rui Garcia has been assigned as Engineer

June 26  4:32 PM WEST

web

Rootly

Rui Garcia acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q1PB3GHPM21O2H)

June 26  4:40 PM WEST

web

Rootly

Delegated to EP for Platform Identity Business by Rui Garcia through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q1PB3GHPM21O2H)

June 26  4:41 PM WEST

web

Rootly

Samuel Jesus acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q1PB3GHPM21O2H). (via Phone)

June 26  4:42 PM WEST

web

Rui Garcia

Teams has been added: [Identity Business](/account/teams/identity-business/status)

June 26  4:42 PM WEST

web

Rui Garcia

Teams has been removed: [Backend Runtime](/account/teams/backend-runtime/status)

June 26  5:32 PM WEST

web

Rootly

Delegated to EP for Platform Identity Core by Samuel Jesus through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q1PB3GHPM21O2H)

June 26  5:33 PM WEST

web

Rootly

Michael Vaz acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q1PB3GHPM21O2H). (via Phone)

July 4  9:41 AM WEST

web

Rootly

ZenDesk Event Type has been set: solved

July 4  9:41 AM WEST

web

Rootly

The Global Support team marked this incident as closed in ZenDesk.

July 4 12:11 PM WEST

web

Rootly

The Global Support team marked this incident as closed in ZenDesk.

July 10  9:54 AM WEST

web

Vera Branco

This incident was worked in Jira due to an error from the team. In Jira, this incident is already in Post Mortem stage. https://outsystemsrd.atlassian.net/browse/RDINC-25811 

July 17  1:38 PM WEST

web

James Waller

Teams has been added: [Identity Core](/account/teams/identity-core/status)

July 17  1:38 PM WEST

web

James Waller

Teams has been removed: [Identity Business](/account/teams/identity-business/status)

August 5 12:16 PM WEST

web

Jorge Marin

Incident has been started

August 5 12:16 PM WEST

web

Rootly

Pagerduty Integrations acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q1PB3GHPM21O2H). (via Phone)

August 5 12:19 PM WEST

web

Jorge Marin

Incident has been resolved

August 5 12:19 PM WEST

web

Jorge Marin

Impact has been set: Failed logins for users who already logged in via an IdP that was first enabled then disabled then re-enabled.

August 5 12:19 PM WEST

web

Jorge Marin

Resolution has been set: - Workaround: Asked customer to create a second IdP with the exact same configuration as the old one. Users were able to login again. The new IdP worked just for the sake of being new.- Reverted change that introduced the bug.