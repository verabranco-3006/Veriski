---
title: Retrospective-SEV2-I am trying to consume a rest API in ODC environment and when I pass the header param as "content-type" it is not passed as part of my request
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4333732031/Retrospective-SEV2-I+am+trying+to+consume+a+rest+API+in+ODC+environment+and+when+I+pass+the+header+param+as+content-type+it+is+not+passed+as+part+of+my+request
confluence_space: RKB
confluence_page_id: 4333732031
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV2-I am trying to consume a rest API in ODC environment and when I pass the header param as "content-type" it is not passed as part of my request

## 📘 Overview
Author:&nbsp;Rootlytrue

Severity:&nbsp;SEV2Redtrue

Teams:&nbsp;Backend RuntimeBluetrue
#### 🕐 Timestamps
Started At:&nbsp;July 10 11:46 AM WESTBluetrue

Mitigated At:&nbsp;August 5  1:25 PM WESTYellowtrue

Resolved At:&nbsp;August 5  1:25 PM WESTGreentrue
#### 🔗 Links
[Incident Page](https://rootly.com/account/incidents/661-i-am-trying-to-consume-a-rest-api-in-odc-environment-and-when-i-pass-the-header-param-as-content-type-it-is-not-passed-as-part-of-my-request)

[Pagerduty incident](https://outsystems.pagerduty.com/incidents/Q2FQ6A0Y0R123J)

[Slack channel](https://slack.com/app_redirect?channel=C07AMFYPYLE&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3030570)

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

Rui Garcia
#### Summary
----------------------------------------------**CONSIDERATIONS BEFORE PERFORMING THE ESCALATION TO R&amp;D (MANDATORY)**
None of the below points should be overlooked. Failure to do so may imply unnecessary effort.* * *
Ensure the ticket has been **categorized**, otherwise, the R&amp;D escalation will go unnoticed and not be worked on!**1.** For **Incidents**, the **IMAX** was consulted **beforehand** on which:- No incident models were found for the reported symptoms **OR**
- The incident model did not solve the issue **OR**
- The next step indicated in the Incident Model is an escalation to R&amp;D.
**2.** For **Questions**, the ChatODC on the **Slack channel** didn't return an acceptable answer.
**3.** Any other requests that explicitly indicate an R&amp;D escalation is needed.
**4**. **Incident impact assessment** was based on the **prioritization scoring matrix**.* * ***R&amp;D ESCALATION FORM**
Section comments can be removed for R&amp;D easier interpretation.**ISSUE DESCRIPTION AND HOW TO REPRODUCE**- The customer is trying to consume a rest API in ODC environment and when he pass the header param as &quot;content-type&quot;- It is not passed as part of the request- And because of this, he is not able to get proper response from the API.
- The API- https://1043917-sb1.restlets.api.netsuite.com/app/site/hosting/restlet.nl?script=1511&amp;deploy=1&amp;record={record}&amp;id={id}- Name of App they consume in:- ECB_Admin  (Attached)
- The **Content-Type** is not present in the request header- ![](https://supportoutsystems.zendesk.com/attachments/token/c2IpAa1QygCGUBhNXHBPdhBDP/?name=image.png)- The customer also says, because of this missing header, their apps in runtime accessing this particular API results in runtime errors.**IMPACT ON THE CUSTOMER**- High (Development stage)- This is a migration activity from O11 to ODC and they are blocked by this.- They have a deadline to complete this migration by next week.- If they are blocked too long, they fear they need to pay more for the O11 while this is being fixed in ODC.- As such they have insisted this case to be High.**TROUBLESHOOTING STEPS &amp; WORKAROUND**- We did a test in the ODC Sandbox portal with our simple test REST API and indeed it is as what the customer mentions.- The REST API URL in our SB- https://gs-sandbox-ga-eu-01-dev.outsystems.app//TestZamRest1/rest/RESTAPI1/RESTAPIMethod1- When I consumed this and added the request headers (Authorization and Content-Type)- https://gs-sandbox-ga-eu-01-dev.outsystems.app/TestZamConsumeRest/Screen1- ![](https://supportoutsystems.zendesk.com/attachments/token/x0PI7XnROe1puxc5kTyFj4CC4/?name=image.png)- Only the Authorization header is added- When called in the browser, these headers are present in the payload section- ![](https://supportoutsystems.zendesk.com/attachments/token/7XBt9NtRPGko1OjFuhQbnM6Yk/?name=image.png)- Meanwhile when I tested in O11, the Content-Type does appear in the Service Studio as claimed by the customer- ![](https://supportoutsystems.zendesk.com/attachments/token/Qe1QJ8smctfzVmIE8RD58bQ11/?name=image.png)- Meanwhile the response in the browser is similar as the ODC case- ![](https://supportoutsystems.zendesk.com/attachments/token/VPF5UxxFO9yRnHm9mJBgHfBb1/?name=image.png)- So there seems to be some discrepancy in this between O11 and ODC in this- and it is affecting this customer in their migration from O11 to ODC.**TECH DATA OR ANY OTHER RELEVANT INFO**
**Ring**: ga
**Tenant Id:** 6c875ad1-c24a-40d3-93bf-59a76e094051
**Tenant Prefix:** mitchell
**Region:** us-east-1
Q5F.K8I.OZ2.AM6.2PA.NZN.2W2.WIZ_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_Attachment(s):
ECB_Admin.oml - https://supportoutsystems.zendesk.com/attachments/token/6pBAlRBJZBJp8S2ipn27QyRcM/?name=ECB_Admin.oml
## 📝 Retrospective### Details
**Ring:** ga
**System-wide impact:**&nbsp; No
**Tenant ID:** 6c875ad1-c24a-40d3-93bf-59a76e094051
**Tenant Prefix:** mitchell
**Routing Error Code:** N/A
**Product Area:** Phoenix::Application Runtime::Logic Flows::Integrations::REST - Consume
### Impact:
Customer integration cannot be implemented using REST Consume oob.
### Investigation and troubleshooting findings:
Customer is trying to integrate with an API that expected content headers (specifically, Content-Type) when no Content is being sent. This goes against best practices and even though possible by the RFC, is not a common behavior.
### Resolution:
For edge cases, customers should consider integration using External Code where they can control any detail of the request being made.
## Tasks performed during incident resolution:
&nbsp;
## Executive Summary
[Guidelines](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4144496679/Incident+Retrospectives+-+Playbook#STEP-3---Write-the-Executive-Summary)

On July 2nd, 2024, Customer submitted Zendesk Incident #3030570 (RDINC-26360 in Jira, 661 in Rootly), reporting inability to implement a specific integration pattern using Rest Consume language element. Specifically, our customer is unable to set Content headers when Content/Body is not sent.

This hinders our customer ability to integrate with specific third party APIs.

From a technical perspective, this is a limitation imposed by following best practices and adhering to HTTP standards. In essence, if the is no Content present, there is not need to provide any Content header. Servers that demand otherwise are too strict and actually incorrectly implemented.

There are no action items as a consequence of this incident. The product is behaving correctly and how it was designed. Customer was suggested a workaround using External Libraries where developers have full control over the way the integration is made, which is a common workaround for very specific edge cases. Going forward, we will reevaluate the current behavior considering an increased frequency of similar feedback.
## Root Causes 
The reported behavior is the designed behavior: Rest Consume doesn&rsquo;t allow setting Content-Headers when Content is not sent (GET requests).

[Guidelines](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4144496679/Incident+Retrospectives+-+Playbook#STEP-1---Perform-the-Root-Cause-Analysis)

If the customer needs formal RCA, please fill out the following field with the document URL

[Please follow these instructions and place the RCA URL in the field below.](https://docs.google.com/document/d/13rXmBsOJh73nV2D6Z17SIBGBu2HOTWty5ddsvU000JM/edit#heading=h.bqxasxszr5q)

RCA URL

&lt;Place the URL of the customer RCA here if you have created one&gt;
## ⌛ Timeline
[View on Rootly](https://rootly.com/account/incidents/661-i-am-trying-to-consume-a-rest-api-in-odc-environment-and-when-i-pass-the-header-param-as-content-type-it-is-not-passed-as-part-of-my-request)

**Date**

**Source**

**User**

**Event**

July 3  6:30 AM WEST

web

Rootly

created an alert via

July 3  6:30 AM WEST

web

Rootly

Rootly created this incident

July 3  6:30 AM WEST

web

Rootly

In triage date has been set to July 3  6:30 AM WEST

July 3  6:30 AM WEST

web

Rootly

[Slack Channel](https://slack.com/app_redirect?channel=C07AMFYPYLE&amp;team=T041063TZ) has been created

July 3  6:30 AM WEST

web

Rootly

[PagerDuty Incident](https://outsystems.pagerduty.com/incidents/Q2FQ6A0Y0R123J) has been created.

📧 Notified Rui Garcia by email.

&nbsp;&nbsp;

📱 Notified Rui Garcia by SMS.

&nbsp;&nbsp;

📧 Notified Rui Garcia by email.

July 3  6:30 AM WEST

web

Rootly

Rui Garcia has been assigned as Engineer

July 3  6:30 AM WEST

web

Rootly

Ring: ga
System-wide impact:  
Tenant ID: 6c875ad1-c24a-40d3-93bf-59a76e094051
Tenant Prefix: mitchell
Routing Error Code: N/A
Product Area: Phoenix::Application Runtime::Logic Flows::Integrations::REST - Consume

July 3  6:32 AM WEST

web

Rootly

Rui Garcia acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q2FQ6A0Y0R123J). (via Phone)

July 3  3:44 PM WEST

web

Rootly

Zendesk Private Comment has been set: ----------------------------------------------**Update to R&amp;D**
Hi Rui, and thanks for the previous feedback.Let me start by saying that I do not wholly agree with the customer's requirement of sending the **Content-Type** header in a GET request - in fact, that's a requirement on the API they are consuming - and I totally understand why we don't set this header for such requests, and only for requests with an actual body (e.g. POST/PUT).Nevertheless, considering there are no standards/rules that prohibit or advise against using this header in GET requests, and there's nothing prohibiting GET requests from carrying a body, we arrive at an impasse - there's just an incompatibility between ODC and the consumed API.Now, considering in O11 they are able to add this header, shouldn't we perhaps shift this control over to the developer and allow them to add this header if they need it so?- If we do not plan on doing any such change, I would just like your official response to back it up.Just asking this to avoid any potential friction from a customer who could be transitioning from O11 to ODC, and to avoid assumptions on my side.Thanks in advance for your additional attention!Jo&atilde;o Neves__

July 3  3:44 PM WEST

web

Rootly

NEW MESSAGE FROM GLOBAL SUPPORT:

July 10 11:46 AM WEST

web

Rui Garcia

Incident has been started

July 10 11:46 AM WEST

web

Rootly

Pagerduty Integrations acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q2FQ6A0Y0R123J). (via Phone)

July 12  6:33 PM WEST

web

Rootly

Rui Garcia marked the incident as resolved through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q2FQ6A0Y0R123J). (via Website)

July 16 12:10 AM WEST

web

Rootly

ZenDesk Event Type has been set: solved

July 16 12:10 AM WEST

web

Rootly

The Global Support team marked this incident as closed in ZenDesk.

August 5  1:25 PM WEST

web

Rui Garcia

Incident has been resolved

August 5  1:25 PM WEST

web

Rui Garcia

System-wide impact has been set: No

August 5  1:25 PM WEST

web

Rui Garcia

Impact has been set: Customer integration cannot be implemented using REST Consume oob.

August 5  1:25 PM WEST

web

Rui Garcia

Investigation and troubleshooting findings has been set: Customer is trying to integrate with an API that expected content headers (specifically, Content-Type) when no Content is being sent. This goes against best practices and even though possible by the RFC, is not a common behavior.

August 5  1:25 PM WEST

web

Rui Garcia

Resolution has been set: For edge cases, customers should consider integration using External Code where they can control any detail of the request being made.