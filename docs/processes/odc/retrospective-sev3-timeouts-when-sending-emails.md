---
title: Retrospective-SEV3-Timeouts when sending Emails
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4335271938/Retrospective-SEV3-Timeouts+when+sending+Emails
confluence_space: RKB
confluence_page_id: 4335271938
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV3-Timeouts when sending Emails

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV3

Teams:&nbsp;trueBlueBackend Runtime
#### 🕐 Timestamps
Started At:&nbsp;trueBlueAugust 5  1:58 PM WEST

Mitigated At:&nbsp;trueYellowAugust 5  1:59 PM WEST

Resolved At:&nbsp;trueGreenAugust 5  1:59 PM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/642-timeouts-when-sending-emails)
[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3027702)

#### Summary
----------------------------------------------**ISSUE DESCRIPTION AND HOW TO REPRODUCE**
The customer ran into an error when sending an email a few times. (twice in same day and very similar hour) in Formulare and Kernsystem app.![](https://supportoutsystems.zendesk.com/attachments/token/uzLc4jgTws5ZeRc5X1O57lEdS/?name=image.png)**IMPACT ON THE CUSTOMER**
Normal, never happen again, but customer would like to know the reason, and also us.**TROUBLESHOOTING STEPS &amp; WORKAROUND**
At back-end errors the trace is the same, and seems 2 occurrences that point to our internal library MAILKIT- ![](https://supportoutsystems.zendesk.com/attachments/token/jcclwGffMDC3lbTcK4i78sqIu/?name=image.png)
- ![](https://supportoutsystems.zendesk.com/attachments/token/72Q6RzqKKOoIMYfhlk3iiYUpO/?name=image.png)
In one example, it seems it took 9.68s to perform the all action and timeout against SMTP and stopped at authenticating:- ![](https://supportoutsystems.zendesk.com/attachments/token/yKxBBGaOlorcB4OriEEwt5NL9/?name=image.png)At logic level, the email is sent by a service action in other module called Kernsystem:- ![](https://supportoutsystems.zendesk.com/attachments/token/VOjvmc6u6OOXkKlTNiVSgOhxy/?name=image.png)By examining the request we can see the request that took 10s was:- ![](https://supportoutsystems.zendesk.com/attachments/token/V2jWIHeIvNAFLg8WY9PSjV71v/?name=image.png)- And follow that trace we can see in details the time that library took to send the email:- ![](https://supportoutsystems.zendesk.com/attachments/token/cgyND5eK06UuJWjIz18KGG5es/?name=image.png)- https://outsystems.grafana.net/d/lj_Cstg4k/gen-search-trace?orgId=1&amp;var-traceid=8ed3df00cee44342e6e1129defac0746- Can see also on Gloo the time that request took:- https://outsystems.grafana.net/d/E6xvxTJnz/gloo-access-logs?orgId=1&amp;var-ring=ga&amp;var-stamp=All&amp;var-method=All&amp;var-status_code=All&amp;var-search=Empfehlung&amp;from=1719396520000&amp;to=1719396539000- However, cannot even narrow down why it took more than the 10s to return the timeout.* * *
We create a sample app, and replicate a similar behavior:- ![](https://supportoutsystems.zendesk.com/attachments/token/aI9g7U43DAffJ2lbsVPEQIqER/?name=image.png)- We can see a correct sending of email needs 2 more actions- ![](https://supportoutsystems.zendesk.com/attachments/token/zHsVrNva50nlKAXlYJWeupMRX/?name=image.png)- Sending Email and closing SMTP Connection
- Reducing the client timeout, was able to to replicate the same error and stack:- ![](https://supportoutsystems.zendesk.com/attachments/token/PB41bPIAzTkZbvpsTdDvw6Rkh/?name=image.png)- ![](https://supportoutsystems.zendesk.com/attachments/token/CxgvRdRjNYcKOdV5wij1FBnjI/?name=image.png)- ![](https://supportoutsystems.zendesk.com/attachments/token/s6dRUgx3GzA47SrpAroM24Md3/?name=image.png)Basically the CR timeout was not enough to send the email at back-end and cancel the operation, however, on customer example 10s should be more than enough, this is our suspicious that either:- Some service on our side was slower to perform the actions against SMTP and the CR timeout occur cancelling sub sequence actions.
- Or indeed there was a problem on SMTP that took more time than expected.We would like R&amp;D help to understand if the cause is ours, and if it is, can you tell us how to narrow even further to know the exact cause?**TECH DATA OR ANY OTHER RELEVANT INFO**
Ring: ga
Tenant Id: 366a4f03-28e6-4728-bf91-89d1f95487da
Tenant Prefix: manq
Region: eu-central-1
JCQ.D1T.JLO.D5Z.UX3.WPC.XGM.GOU_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 RetrospectiveinfoDetails
**Ring:** ga
**System-wide impact:**&nbsp; No
**Tenant ID:** 366a4f03-28e6-4728-bf91-89d1f95487da
**Tenant Prefix:** manq
**Routing Error Code:** OS-BERT
**Product Area:** -
### Impact:
Already handled and solved here: [https://outsystemsrd.atlassian.net/browse/RDINC-25934](https://outsystemsrd.atlassian.net/browse/RDINC-25934)
### Investigation and troubleshooting findings:
Already handled and solved here: [https://outsystemsrd.atlassian.net/browse/RDINC-25934](https://outsystemsrd.atlassian.net/browse/RDINC-25934)
### Resolution:
Already handled and solved here: [https://outsystemsrd.atlassian.net/browse/RDINC-25934](https://outsystemsrd.atlassian.net/browse/RDINC-25934)
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/642-timeouts-when-sending-emails)

**Date**

**Source**

**User**

**Event**
June 28 12:56 PM WESTwebRootly
created an alert via
June 28 12:56 PM WESTwebRootly
Rootly created this incident
June 28 12:56 PM WESTwebRootly
In triage date has been set to June 28 12:56 PM WEST
June 28  1:25 PM WESTwebRootly
This incident was instantiated in Jira: RDINC-25934. Please work the incident using Rootly
July 9  8:20 AM WESTwebRootlyZenDesk Event Type has been set: solvedJuly 9  8:20 AM WESTwebRootly
The Global Support team marked this incident as closed in ZenDesk.
August 5  1:58 PM WESTwebRui Garcia
Already solved here: https://outsystemsrd.atlassian.net/browse/RDINC-25934
August 5  1:58 PM WESTwebRui Garcia
Incident has been started
August 5  1:59 PM WESTwebRui Garcia
Incident has been resolved
August 5  1:59 PM WESTwebRui GarciaSystem-wide impact has been set: NoAugust 5  1:59 PM WESTwebRui GarciaImpact has been set: Already handled and solved here: https://outsystemsrd.atlassian.net/browse/RDINC-25934August 5  1:59 PM WESTwebRui GarciaInvestigation and troubleshooting findings has been set: Already handled and solved here: https://outsystemsrd.atlassian.net/browse/RDINC-25934August 5  1:59 PM WESTwebRui GarciaResolution has been set: Already handled and solved here: https://outsystemsrd.atlassian.net/browse/RDINC-25934