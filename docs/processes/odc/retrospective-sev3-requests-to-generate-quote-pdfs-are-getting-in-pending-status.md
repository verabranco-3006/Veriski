---
title: Retrospective-SEV3-Requests to generate quote PDFs are getting in Pending status
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4335632395/Retrospective-SEV3-Requests+to+generate+quote+PDFs+are+getting+in+Pending+status
confluence_space: RKB
confluence_page_id: 4335632395
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV3-Requests to generate quote PDFs are getting in Pending status

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV3

Teams:&nbsp;trueBlueExtended Runtime
#### 🕐 Timestamps
Started At:&nbsp;trueBlueAugust 1  9:52 PM WEST

Mitigated At:&nbsp;trueYellowAugust 5  2:53 PM WEST

Resolved At:&nbsp;trueGreenAugust 5  2:53 PM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/793-requests-to-generate-quote-pdfs-are-getting-in-pending-status)
[Pagerduty incident](https://outsystems.pagerduty.com/incidents/Q2QB8ZE7AQARRS)

[Slack channel](https://slack.com/app_redirect?channel=C07FJ7QP0JD&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3043778)

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

Sam Audu

**Stakeholder**

Rafael Duarte
#### Summary
&lt;hr&gt;
&lt;p class=&quot;redcarpet&quot;&gt;&lt;strong&gt;ISSUE DESCRIPTION AND HOW TO REPRODUCE&lt;/strong&gt;
&lt;br&gt;- The client reported that the timer Timer_SendPDF is no longer running. This prevented the client from generating PDFs.&lt;/p&gt;&lt;p class=&quot;redcarpet&quot;&gt;&lt;strong&gt;IMPACT ON THE CUSTOMER&lt;/strong&gt;&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;This prevented the client from generating quotes. The quotes being generated were left blocked and left in the pending state.&lt;/li&gt;
&lt;li&gt;This issue occurred in Production&lt;/li&gt;
&lt;li&gt;The issue only occurred once so far.&lt;/li&gt;
&lt;/ul&gt;
&lt;p class=&quot;redcarpet&quot;&gt;&lt;strong&gt;TROUBLESHOOTING STEPS &amp; WORKAROUND&lt;/strong&gt;&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;We observed that the issue was caused by the NATS service:&lt;ul&gt;
&lt;li&gt;&lt;a target=&quot;_blank&quot; href=&quot;https://outsystems.grafana.net/d/lj_Cstg4k/gen-search-trace?orgId=1&amp;amp;var-traceid=478966a7865bb14e579f2cf12043fabb&quot;&gt;https://outsystems.grafana.net/d/lj_Cstg4k/gen-search-trace?orgId=1&amp;amp;var-traceid=478966a7865bb14e579f2cf12043fabb&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;Seems like the service tried to publish several times, prevented the PDFs from being generated:&lt;/li&gt;
&lt;li&gt;&lt;a target=&quot;_blank&quot; href=&quot;https://outsystems.grafana.net/goto/HZzo-drIR?orgId=1&quot;&gt;https://outsystems.grafana.net/goto/HZzo-drIR?orgId=1&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/li&gt;
&lt;/ul&gt;
&lt;p class=&quot;redcarpet&quot;&gt;&lt;strong&gt;TECH DATA OR ANY OTHER RELEVANT INFO&lt;/strong&gt;&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;f4248c7c-5784-4166-a25f-acf30b9b652e&lt;/li&gt;
&lt;li&gt;Screenshot 2024-08-01 at 15.48.08.png&lt;/li&gt;
&lt;li&gt;Screenshot 2024-08-01 at 15.52.46.png&lt;/li&gt;
&lt;li&gt;&lt;img alt=&quot;Screenshot 2024-08-01 at 15.58.24.png&quot; width=&quot;100%&quot; src=&quot;https://supportoutsystems.zendesk.com/attachments/token/3UG7k9w6ul3xoaeyjHwhrnkfr/?name=Screenshot+2024-08-01+at+15.58.24.png&quot;&gt;&lt;/li&gt;
&lt;li&gt;&lt;a target=&quot;_blank&quot; href=&quot;https://outsystems.grafana.net/d/Ok_fGn1nz/timer-jobs?orgId=1&amp;amp;var-severity=$__all&amp;amp;var-cluster=runp-ga-us-east-1-01&amp;amp;var-timer=timer-0f5a03ba5a2c98260f4e984da0f4fe5cfdb58b0518bc68&amp;amp;from=2024-08-01T12:00:00.000Z&amp;amp;to=2024-08-01T15:59:59.000Z&amp;amp;timezone=browser&amp;amp;var-Filters=&quot;&gt;https://outsystems.grafana.net/d/Ok_fGn1nz/timer-jobs?orgId=1&amp;amp;var-severity=$__all&amp;amp;var-cluster=runp-ga-us-east-1-01&amp;amp;var-timer=timer-0f5a03ba5a2c98260f4e984da0f4fe5cfdb58b0518bc68&amp;amp;from=2024-08-01T12:00:00.000Z&amp;amp;to=2024-08-01T15:59:59.000Z&amp;amp;timezone=browser&amp;amp;var-Filters=&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a target=&quot;_blank&quot; href=&quot;https://outsystems.grafana.net/d/bddnseyxq41s0c/nats-logs?var-stampfilter=datap-ga-.%2A&amp;amp;var-ring=ga&amp;amp;from=2024-08-01T03:00:00.000Z&amp;amp;to=2024-08-01T15:59:59.000Z&amp;amp;timezone=browser&quot;&gt;https://outsystems.grafana.net/d/bddnseyxq41s0c/nats-logs?var-stampfilter=datap-ga-.%2A&amp;amp;var-ring=ga&amp;amp;from=2024-08-01T03:00:00.000Z&amp;amp;to=2024-08-01T15:59:59.000Z&amp;amp;timezone=browser&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a target=&quot;_blank&quot; href=&quot;https://outsystems.grafana.net/d/lj_Cstg4k/gen-search-trace?orgId=1&amp;amp;var-traceid=746b6f1785c61c1fe12586527cc61ff0&quot;&gt;https://outsystems.grafana.net/d/lj_Cstg4k/gen-search-trace?orgId=1&amp;amp;var-traceid=746b6f1785c61c1fe12586527cc61ff0&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a target=&quot;_blank&quot; href=&quot;https://apps.outsystems.dev/monitoring/log?fromrelated=false&amp;amp;id=pGOYDpEBQHIMNFh6kTme&amp;amp;stageid=3fd0a607-f7b7-4773-afb8-3a5731da0c42&quot;&gt;https://apps.outsystems.dev/monitoring/log?fromrelated=false&amp;amp;id=pGOYDpEBQHIMNFh6kTme&amp;amp;stageid=3fd0a607-f7b7-4773-afb8-3a5731da0c42&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a target=&quot;_blank&quot; href=&quot;https://outsystems.grafana.net/d/lj_Cstg4k/gen-search-trace?orgId=1&amp;amp;var-traceid=478966a7865bb14e579f2cf12043fabb&quot;&gt;https://outsystems.grafana.net/d/lj_Cstg4k/gen-search-trace?orgId=1&amp;amp;var-traceid=478966a7865bb14e579f2cf12043fabb&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;p class=&quot;redcarpet&quot;&gt;&lt;em&gt;&lt;! do not remove this line, this will be used to the trigger&lt;/em&gt; Technical Support::Send to R&amp;D - ODC &lt;em&gt;#trigger_send_to_r&amp;d_odc !&gt;&lt;/em&gt;&lt;/p&gt;
## 📝 RetrospectiveinfoDetails
**Ring:** ga
**System-wide impact:**&nbsp; 
**Tenant ID:** f4248c7c-5784-4166-a25f-acf30b9b652e
**Tenant Prefix:** apps
**Routing Error Code:** N/A
**Product Area:** Phoenix::Application Runtime::Timers
### Impact:
Customer is not able to run timer for 1 hour.
### Investigation and troubleshooting findings:### Resolution:
Service was able to self-heal and customer is unblocked.

A follow-up action item has been planned to address the issue.
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/793-requests-to-generate-quote-pdfs-are-getting-in-pending-status)

**Date**

**Source**

**User**

**Event**
August 1  9:51 PM WESTwebRootly
created an alert via
August 1  9:51 PM WESTwebRootly
Rootly created this incident
August 1  9:51 PM WESTwebRootly
In triage date has been set to August 1  9:51 PM WEST
August 1  9:51 PM WESTwebRootly[Slack Channel](https://slack.com/app_redirect?channel=C07FJ7QP0JD&amp;team=T041063TZ) has been createdAugust 1  9:51 PM WESTwebRootly
Ring: ga
System-wide impact:  
Tenant ID: f4248c7c-5784-4166-a25f-acf30b9b652e
Tenant Prefix: apps
Routing Error Code: N/A
Product Area: Phoenix::Application Runtime::Timers
August 1  9:51 PM WESTwebRootly[PagerDuty Incident](https://outsystems.pagerduty.com/incidents/Q2QB8ZE7AQARRS) has been created.
📲 Notified Sam Audu by push notification.  (via iPhone)August 1  9:51 PM WESTwebRootlySam Audu has been assigned as EngineerAugust 1  9:51 PM WESTwebRootly
Sam Audu acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q2QB8ZE7AQARRS)
August 1  9:52 PM WESTwebSam Audu
Incident has been started
August 1  9:52 PM WESTwebRootly
Pagerduty Integrations acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q2QB8ZE7AQARRS). (via Mobile)
August 1 10:01 PM WESTwebRootly
This incident was instantiated in Jira: RDINC-27959. Please work the incident using Rootly
August 1 10:09 PM WESTwebSam AuduPedro Pita has been assigned as Subject Matter ExpertAugust 1 10:15 PM WESTwebSam AuduSwarm has been set: Extended RuntimeAugust 1 10:15 PM WESTwebRootly
Pagerduty Integrations added Rafael Duarte as responder in [PagerDuty](https://outsystems.pagerduty.com/incidents/Q2QB8ZE7AQARRS)
August 1 10:19 PM WESTwebSam AuduRafael Duarte has been assigned as StakeholderAugust 1 10:25 PM WESTwebRafael Duarte
Teams has been added: ICE
August 1 10:51 PM WESTwebRootly
This incident was instantiated in Jira: RDINC-27959. Please work the incident using Rootly
August 2  8:43 AM WESTwebRootly
Rafael Duarte joined this [PagerDuty](https://outsystems.pagerduty.com/incidents/Q2QB8ZE7AQARRS) incident.
August 2  8:43 AM WESTwebRootly
Rafael Duarte acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q2QB8ZE7AQARRS). (via Mobile)
August 5  2:40 PM WESTwebRafael Duarte
Summary has been changed to 

&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;

&nbsp;&nbsp;
&nbsp;&nbsp;**ISSUE DESCRIPTION AND HOW TO REPRODUCE**
&nbsp;&nbsp;
- The client reported that the timer Timer_SendPDF is no longer running. This prevented the client from generating PDFs.
&nbsp;&nbsp;
&nbsp;&nbsp;**IMPACT ON THE CUSTOMER**&nbsp;&nbsp;

&nbsp;&nbsp;

&nbsp;&nbsp;- This prevented the client from generating quotes. The quotes being generated were left blocked and left in the pending state.

&nbsp;&nbsp;- This issue occurred in Production

&nbsp;&nbsp;- The issue only occurred once so far.

&nbsp;&nbsp;

&nbsp;&nbsp;
&nbsp;&nbsp;**TROUBLESHOOTING STEPS &amp; WORKAROUND**&nbsp;&nbsp;

&nbsp;&nbsp;

&nbsp;&nbsp;- We observed that the issue was caused by the NATS service:
&nbsp;&nbsp;
&nbsp;&nbsp;

- &nbsp;&nbsp;[https://outsystems.grafana.net/d/lj_Cstg4k/gen-search-trace?orgId=1&amp;var-traceid=478966a7865bb14e579f2cf12043fabb](https://outsystems.grafana.net/d/lj_Cstg4k/gen-search-trace?orgId=1&amp;var-traceid=478966a7865bb14e579f2cf12043fabb)&nbsp;&nbsp;
- Seems like the service tried to publish several times, prevented the PDFs from being generated:
- &nbsp;&nbsp;[https://outsystems.grafana.net/goto/HZzo-drIR?orgId=1](https://outsystems.grafana.net/goto/HZzo-drIR?orgId=1)&nbsp;&nbsp;

&nbsp;&nbsp;

&nbsp;&nbsp;

&nbsp;&nbsp;**TECH DATA OR ANY OTHER RELEVANT INFO**&nbsp;&nbsp;

&nbsp;&nbsp;

&nbsp;&nbsp;- f4248c7c-5784-4166-a25f-acf30b9b652e

&nbsp;&nbsp;- Screenshot 2024-08-01 at 15.48.08.png

&nbsp;&nbsp;- Screenshot 2024-08-01 at 15.52.46.png

&nbsp;&nbsp;- &nbsp;&nbsp;&nbsp;&nbsp;

&nbsp;&nbsp;- &nbsp;&nbsp;[&nbsp;&nbsp;](https://outsystems.grafana.net/d/Ok_fGn1nz/timer-jobs?orgId=1&amp;var-severity=$__all&amp;var-cluster=runp-ga-us-east-1-01&amp;var-timer=timer-0f5a03ba5a2c98260f4e984da0f4fe5cfdb58b0518bc68&amp;from=2024-08-01T12:00:00.000Z&amp;to=2024-08-01T15:59:59.000Z&amp;timezone=browser&amp;var-Filters=)&nbsp;&nbsp;[https://outsystems.grafana.net/d/Ok_fGn1nz/timer-jobs?orgId=1&amp;amp;amp;var-severity=$__all&amp;amp;amp;var-cluster=runp-ga-us-east-1-01&amp;amp;amp;var-timer=timer-0f5a03ba5a2c98260f4e984da0f4fe5cfdb58b0518bc68&amp;amp;amp;from=2024-08-01T12:00:00.000Z&amp;amp;amp;to=2024-08-01T15:59:59.000Z&amp;amp;amp;timezone=browser&amp;amp;amp;var-Filters=](https://outsystems.grafana.net/d/Ok_fGn1nz/timer-jobs?orgId=1&amp;amp;amp;var-severity=$__all&amp;amp;amp;var-cluster=runp-ga-us-east-1-01&amp;amp;amp;var-timer=timer-0f5a03ba5a2c98260f4e984da0f4fe5cfdb58b0518bc68&amp;amp;amp;from=2024-08-01T12:00:00.000Z&amp;amp;amp;to=2024-08-01T15:59:59.000Z&amp;amp;amp;timezone=browser&amp;amp;amp;var-Filters=)&nbsp;&nbsp;

&nbsp;&nbsp;- &nbsp;&nbsp;[&nbsp;&nbsp;](https://outsystems.grafana.net/d/bddnseyxq41s0c/nats-logs?var-stampfilter=datap-ga-.%2A&amp;var-ring=ga&amp;from=2024-08-01T03:00:00.000Z&amp;to=2024-08-01T15:59:59.000Z&amp;timezone=browser)&nbsp;&nbsp;[https://outsystems.grafana.net/d/bddnseyxq41s0c/nats-logs?var-stampfilter=datap-ga-.%2A&amp;amp;amp;var-ring=ga&amp;amp;amp;from=2024-08-01T03:00:00.000Z&amp;amp;amp;to=2024-08-01T15:59:59.000Z&amp;amp;amp;timezone=browser](https://outsystems.grafana.net/d/bddnseyxq41s0c/nats-logs?var-stampfilter=datap-ga-.%2A&amp;amp;amp;var-ring=ga&amp;amp;amp;from=2024-08-01T03:00:00.000Z&amp;amp;amp;to=2024-08-01T15:59:59.000Z&amp;amp;amp;timezone=browser)&nbsp;&nbsp;

&nbsp;&nbsp;- &nbsp;&nbsp;[&nbsp;&nbsp;](https://outsystems.grafana.net/d/lj_Cstg4k/gen-search-trace?orgId=1&amp;var-traceid=746b6f1785c61c1fe12586527cc61ff0)&nbsp;&nbsp;[https://outsystems.grafana.net/d/lj_Cstg4k/gen-search-trace?orgId=1&amp;amp;amp;var-traceid=746b6f1785c61c1fe12586527cc61ff0](https://outsystems.grafana.net/d/lj_Cstg4k/gen-search-trace?orgId=1&amp;amp;amp;var-traceid=746b6f1785c61c1fe12586527cc61ff0)&nbsp;&nbsp;

&nbsp;&nbsp;- &nbsp;&nbsp;[&nbsp;&nbsp;](https://apps.outsystems.dev/monitoring/log?fromrelated=false&amp;id=pGOYDpEBQHIMNFh6kTme&amp;stageid=3fd0a607-f7b7-4773-afb8-3a5731da0c42)&nbsp;&nbsp;[https://apps.outsystems.dev/monitoring/log?fromrelated=false&amp;amp;amp;id=pGOYDpEBQHIMNFh6kTme&amp;amp;amp;stageid=3fd0a607-f7b7-4773-afb8-3a5731da0c42](https://apps.outsystems.dev/monitoring/log?fromrelated=false&amp;amp;amp;id=pGOYDpEBQHIMNFh6kTme&amp;amp;amp;stageid=3fd0a607-f7b7-4773-afb8-3a5731da0c42)&nbsp;&nbsp;

&nbsp;&nbsp;- &nbsp;&nbsp;[&nbsp;&nbsp;](https://outsystems.grafana.net/d/lj_Cstg4k/gen-search-trace?orgId=1&amp;var-traceid=478966a7865bb14e579f2cf12043fabb)&nbsp;&nbsp;[https://outsystems.grafana.net/d/lj_Cstg4k/gen-search-trace?orgId=1&amp;amp;amp;var-traceid=478966a7865bb14e579f2cf12043fabb](https://outsystems.grafana.net/d/lj_Cstg4k/gen-search-trace?orgId=1&amp;amp;amp;var-traceid=478966a7865bb14e579f2cf12043fabb)&nbsp;&nbsp;

&nbsp;&nbsp;

&nbsp;&nbsp;
&nbsp;&nbsp;*&lt;! do not remove this line, this will be used to the trigger* Technical Support::Send to R&amp;D - ODC *#trigger_send_to_r&amp;d_odc !&gt;*&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;August 5  2:40 PM WESTwebRafael Duarte
Severity has been changed from SEV2 to SEV3
August 5  2:40 PM WESTwebRafael Duarte
Teams has been removed: ICE&nbsp;&nbsp;SRE
August 5  2:40 PM WESTwebRafael DuarteImpact has been set: Customer is not able to run timer for 1 hour.August 5  2:53 PM WESTwebRafael DuarteSend ZenDesk private comment has been set: Hi Support,  We have identified the root cause of the recent issue. On August 1st, there was a minor infrastructure degradation in the Kubernetes (K8s) cluster connectivity. This incident exposed a previously undetected issue within our timer executor job.  Due to this issue, the job executor remained in a running state for an extended period, as observed by the customer, without executing the timer function. During this time, the job attempted to publish internal messages without first establishing a successful connection to the message server. Had the service retried the connection to the message server, it would have eventually succeeded.  To address this, we have created a follow-up action item (RTAFB-7905) aimed at improving the timer executor job&rsquo;s resilience and ensuring it fails faster in such scenarios. This will prevent prolonged retry attempts for failed connections in the future.  Since no customers are currently impacted by this issue, we will mark it as resolved and proceed with the implementation of the follow-up action item.  If you have any questions, please reach out.Kind regards,  
R&amp;D TeamAugust 5  2:53 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hi Support,  We have identified the root cause of the recent issue. On August 1st, there was a minor infrastructure degradation in the Kubernetes (K8s) cluster connectivity. This incident exposed a previously undetected issue within our timer executor job.  Due to this issue, the job executor remained in a running state for an extended period, as observed by the customer, without executing the timer function. During this time, the job attempted to publish internal messages without first establishing a successful connection to the message server. Had the service retried the connection to the message server, it would have eventually succeeded.  To address this, we have created a follow-up action item (RTAFB-7905) aimed at improving the timer executor job&rsquo;s resilience and ensuring it fails faster in such scenarios. This will prevent prolonged retry attempts for failed connections in the future.  Since no customers are currently impacted by this issue, we will mark it as resolved and proceed with the implementation of the follow-up action item.  If you have any questions, please reach out.Kind regards,  
R&amp;D Team
August 5  2:53 PM WESTwebRootlySend ZenDesk private comment has been unsetAugust 5  2:53 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

August 5  2:53 PM WESTwebRafael Duarte
Incident has been resolved
August 5  2:53 PM WESTwebRafael DuarteResolution has been set: Service was able to self-heal and customer is unblocked.A follow-up action item has been planned to address the issue.## 📝 Follow Up Items[View on Rootly](https://rootly.com/account/incidents/793-requests-to-generate-quote-pdfs-are-getting-in-pending-status#nav-action-items)

**Summary**

**Priority**

**Status**

**Assignee**

**Links**
https://outsystemsrd.atlassian.net/browse/RTAFB-7905trueYellowMediumtrueBlueOpen