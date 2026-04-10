---
title: Retrospective-SEV2-Cloudfront throwing 403 errors during Security Test
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4262692941/Retrospective-SEV2-Cloudfront+throwing+403+errors+during+Security+Test
confluence_space: RKB
confluence_page_id: 4262692941
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV2-Cloudfront throwing 403 errors during Security Test

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV2

Teams:&nbsp;trueBlueSre&nbsp;trueBlueGlobal Routing
#### 🕐 Timestamps
Started At:&nbsp;trueBlueJuly 5 12:55 PM WEST

Mitigated At:&nbsp;trueYellowJuly 5  2:08 PM WEST

Resolved At:&nbsp;trueGreenJuly 5  2:08 PM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/676-cloudfront-throwing-403-errors-during-security-test)
[Pagerduty incident](https://outsystems.pagerduty.com/incidents/Q0OOEIAGB6FKP0)

[Slack channel](https://slack.com/app_redirect?channel=C07B6M80WSW&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3030704)

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

Joel Filipe Carvalho
#### Summary
&lt;hr&gt;
&lt;p class=&quot;redcarpet&quot;&gt;&lt;strong&gt;ISSUE DESCRIPTION AND HOW TO REPRODUCE&lt;/strong&gt;
&lt;br&gt;A customer is running into Cloudfront errors during a security test, we don't have the method of testing however, Success team is gathering those details.
&lt;br&gt;According to Customer Success team, they indicate is that they are running the tests from a set of IPs and after a while these IPs are blocked for dozens of minutes, so they cannot continue to run their tests.
&lt;br&gt;The request form the customer is to whitelist the IPs from which they are running the tests so that they are not blocked as they are going through the test.&lt;/p&gt;&lt;p class=&quot;redcarpet&quot;&gt;&lt;strong&gt;IMPACT ON THE CUSTOMER&lt;/strong&gt;
&lt;br&gt;High, blocked customer from performing the test, the customer has scheduled a new test run for July 15th to 18th (requested in ticket #3028432) and would like to understand how we can test the execution before they try to do the test again - every time they run these failed tests they have expensive consultants' time wasted.&lt;/p&gt;&lt;p class=&quot;redcarpet&quot;&gt;&lt;strong&gt;TROUBLESHOOTING STEPS &amp; WORKAROUND&lt;/strong&gt;
&lt;br&gt;To be clear to R&amp;D team, we perform our investigation based on the reported 403 errors by the customer and we start:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Customer has the default and custom domain:&lt;ul&gt;
&lt;li&gt;&lt;img width=&quot;100%&quot; src=&quot;https://supportoutsystems.zendesk.com/attachments/token/NWH0rosJRLC2mcXbFB2vGPHsI/?name=image.png&quot;&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/li&gt;
&lt;li&gt;Based on that, we check where the tests took place using this dashboard:&lt;ul&gt;
&lt;li&gt;&lt;a target=&quot;_blank&quot; href=&quot;https://outsystems.grafana.net/d/bdgf0fb2hcrnke/cloudfront-requests-per-ip-address?orgId=1&amp;amp;var-distribution=All&amp;amp;var-host=vki-test.outsystems.app&amp;amp;var-client_ip=&amp;amp;var-plus5m=1709297700&amp;amp;from=1719874800000&amp;amp;to=1719961199000&quot;&gt;https://outsystems.grafana.net/d/bdgf0fb2hcrnke/cloudfront-requests-per-ip-address?orgId=1&amp;amp;var-distribution=All&amp;amp;var-host=vki-test.outsystems.app&amp;amp;var-client_ip=&amp;amp;var-plus5m=1709297700&amp;amp;from=1719874800000&amp;amp;to=1719961199000&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;The default domain doesn't have many request on July 2 but custom domain yes:&lt;/li&gt;
&lt;li&gt;
&lt;img width=&quot;100%&quot; src=&quot;https://supportoutsystems.zendesk.com/attachments/token/EL8pcmiWJSopa5LqVLe8QdMTV/?name=image.png&quot;&gt;&lt;ul&gt;
&lt;li&gt;portal-qa.vki.at&lt;/li&gt;
&lt;li&gt;&lt;img width=&quot;100%&quot; src=&quot;https://supportoutsystems.zendesk.com/attachments/token/K3kIS7N2BMCBCXQObisxOf8OE/?name=image.png&quot;&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/li&gt;
&lt;/ul&gt;
&lt;/li&gt;
&lt;li&gt;With that we understand the custom domain was used, customer said that a subset of IP's were used, however, we don't believe it per this graph where the IP has a huge recurrence:&lt;ul&gt;
&lt;li&gt;109.70.98.162&lt;/li&gt;
&lt;/ul&gt;
&lt;/li&gt;
&lt;li&gt;Due to that we proceed our analysis to check why this IP was having 270k requests, and some were blocked during that day, specially during 7am to 13pm +/-&lt;ul&gt;
&lt;li&gt;&lt;a target=&quot;_blank&quot; href=&quot;https://outsystems.splunkcloud.com/en-US/app/e9ead269be9f433d8ecf621a1ca52f14/search?earliest=1719792000&amp;amp;latest=now&amp;amp;q=search%20index%3Daws_firewall_manager%20httpSourceName%3DCF%20AND%20action%3D%22BLOCK%22%20%22httpRequest.clientIp%22%3D%22109.70.98.162%22&amp;amp;display.page.search.mode=smart&amp;amp;dispatch.sample_ratio=1&amp;amp;workload_pool=standard_perf&amp;amp;display.general.type=events&amp;amp;display.visualizations.charting.chart=line&amp;amp;display.page.search.tab=events&amp;amp;display.prefs.statistics.count=50&amp;amp;sid=1720179678.6433054&quot;&gt;https://outsystems.splunkcloud.com/en-US/app/e9ead269be9f433d8ecf621a1ca52f14/search?earliest=1719792000&amp;amp;latest=now&amp;amp;q=search%20index%3Daws_firewall_manager%20httpSourceName%3DCF%20AND%20action%3D%22BLOCK%22%20%22httpRequest.clientIp%22%3D%22109.70.98.162%22&amp;amp;display.page.search.mode=smart&amp;amp;dispatch.sample_ratio=1&amp;amp;workload_pool=standard_perf&amp;amp;display.general.type=events&amp;amp;display.visualizations.charting.chart=line&amp;amp;display.page.search.tab=events&amp;amp;display.prefs.statistics.count=50&amp;amp;sid=1720179678.6433054&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;We started to see the number of events blocked:&lt;/li&gt;
&lt;li&gt;&lt;img width=&quot;100%&quot; src=&quot;https://supportoutsystems.zendesk.com/attachments/token/FsX0Xh1rZXsmwEwPEs4nmjJbv/?name=image.png&quot;&gt;&lt;/li&gt;
&lt;li&gt;By seeing such amount it seems was detected 23 rules of requests blocked:&lt;ul&gt;
&lt;li&gt;&lt;img width=&quot;100%&quot; src=&quot;https://supportoutsystems.zendesk.com/attachments/token/GrwmtdkP16yrZMHi6HXEJleZ3/?name=image.png&quot;&gt;&lt;/li&gt;
&lt;li&gt;Based on that we compile those results in Splunk Chart to see all the 23 rules:&lt;ul&gt;
&lt;li&gt;&lt;a target=&quot;_blank&quot; href=&quot;https://outsystems.splunkcloud.com/en-US/app/e9ead269be9f433d8ecf621a1ca52f14/search?earliest=1719792000&amp;amp;latest=now&amp;amp;q=search%20index%3Daws_firewall_manager%20httpSourceName%3DCF%20AND%20action%3D%22BLOCK%22%20%22httpRequest.clientIp%22%3D%22109.70.98.162%22%7C%20timechart%20count%20by%20ruleGroupList%7B%7D.terminatingRule.ruleId%20limit%3D30&amp;amp;display.page.search.mode=smart&amp;amp;dispatch.sample_ratio=1&amp;amp;workload_pool=standard_perf&amp;amp;display.general.type=visualizations&amp;amp;display.visualizations.charting.chart=line&amp;amp;display.page.search.tab=visualizations&amp;amp;display.prefs.statistics.count=50&amp;amp;display.events.fields=%5B%22host%22%2C%22source%22%2C%22sourcetype%22%2C%22ruleGroupList%7B%7D.terminatingRule.ruleId%22%5D&amp;amp;sid=1720179813.6434232&quot;&gt;https://outsystems.splunkcloud.com/en-US/app/e9ead269be9f433d8ecf621a1ca52f14/search?earliest=1719792000&amp;amp;latest=now&amp;amp;q=search%20index%3Daws_firewall_manager%20httpSourceName%3DCF%20AND%20action%3D%22BLOCK%22%20%22httpRequest.clientIp%22%3D%22109.70.98.162%22%7C%20timechart%20count%20by%20ruleGroupList%7B%7D.terminatingRule.ruleId%20limit%3D30&amp;amp;display.page.search.mode=smart&amp;amp;dispatch.sample_ratio=1&amp;amp;workload_pool=standard_perf&amp;amp;display.general.type=visualizations&amp;amp;display.visualizations.charting.chart=line&amp;amp;display.page.search.tab=visualizations&amp;amp;display.prefs.statistics.count=50&amp;amp;display.events.fields=%5B%22host%22%2C%22source%22%2C%22sourcetype%22%2C%22ruleGroupList%7B%7D.terminatingRule.ruleId%22%5D&amp;amp;sid=1720179813.6434232&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;img width=&quot;100%&quot; src=&quot;https://supportoutsystems.zendesk.com/attachments/token/RhfjGIjauUlpEaTB2m6MeW9mi/?name=image.png&quot;&gt;&lt;/li&gt;
&lt;li&gt;Customer said that when performing the tests they were getting some minutes where the requests were blacklist due to the amount, however, we don't think IP get blacklisted for that reason.&lt;/li&gt;
&lt;/ul&gt;
&lt;/li&gt;
&lt;/ul&gt;
&lt;/li&gt;
&lt;/ul&gt;
&lt;/li&gt;
&lt;li&gt;At this point we had a call with several persons including (Rui Covelo, Joao Valentim, GS (including me) Daniel Lourenco e Francisco Freire) to discuss this situation)&lt;ul&gt;
&lt;li&gt;And we would like your help on several points:&lt;/li&gt;
&lt;li&gt;Until this points is our analysis valid? We don't think requests are being blocked by the amount, but due to the patterns of attack.&lt;/li&gt;
&lt;li&gt;Does indeed exist more IP's doing the test, or only this one as we suspect?&lt;/li&gt;
&lt;li&gt;If the IP is not being blocked by rate limiting(we suspect not), is being backlisted due to the nature of the requests + the number of requests being made. So to say, why the IP gets blocked for some time, is this happening in our rules?&lt;/li&gt;
&lt;li&gt;We are getting more details on the tests to understand if they are being made currently with you help, but at this point we don't have them, however, currently is there any pattern they might be doing incorrectly?
Feel free to reach me directly.&lt;/li&gt;
&lt;/ul&gt;
&lt;/li&gt;
&lt;/ul&gt;
&lt;p class=&quot;redcarpet&quot;&gt;&lt;strong&gt;TECH DATA OR ANY OTHER RELEVANT INFO&lt;/strong&gt;
&lt;br&gt;Ring: ga
&lt;br&gt;Tenant Id: 46e2496a-5095-4f6f-86a1-5e660542c75c
&lt;br&gt;Tenant Prefix: vki
&lt;br&gt;Region: eu-central-1
&lt;br&gt;R0X.TSZ.ITI.MKS.ZYO.VHD.LDZ.AUT&lt;/p&gt;&lt;p class=&quot;redcarpet&quot;&gt;&lt;em&gt;&lt;! do not remove this line, this will be used to the trigger&lt;/em&gt; Technical Support::Send to R&amp;D - ODC &lt;em&gt;#trigger_send_to_r&amp;d_odc !&gt;&lt;/em&gt;&lt;/p&gt;
## 📝 RetrospectiveinfoDetails
**Ring:** ga
**System-wide impact:**&nbsp; No
**Tenant ID:** 46e2496a-5095-4f6f-86a1-5e660542c75c
**Tenant Prefix:** vki
**Routing Error Code:** N/A
**Product Area:** Phoenix::Application Runtime::Networking
### Impact:
It is being observed in just one tenant.
### Investigation and troubleshooting findings:### Resolution:
This is an expected behavior and also this should not be a Sev since accordingly to confluence document ([https://outsystemsrd.atlassian.net/wiki/spaces/CloudKB/pages/3506897056/ODC+-+Severity+Assessment](https://outsystemsrd.atlassian.net/wiki/spaces/CloudKB/pages/3506897056/ODC+-+Severity+Assessment)) 
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/676-cloudfront-throwing-403-errors-during-security-test)

**Date**

**Source**

**User**

**Event**
July 5 12:54 PM WESTwebRootly
created an alert via
July 5 12:54 PM WESTwebRootly
Rootly created this incident
July 5 12:54 PM WESTwebRootly
In triage date has been set to July 5 12:54 PM WEST
July 5 12:54 PM WESTwebRootly[Slack Channel](https://slack.com/app_redirect?channel=C07B6M80WSW&amp;team=T041063TZ) has been createdJuly 5 12:54 PM WESTwebRootly
Ring: ga
System-wide impact:  
Tenant ID: 46e2496a-5095-4f6f-86a1-5e660542c75c
Tenant Prefix: vki
Routing Error Code: N/A
Product Area: Phoenix::Application Runtime::Networking
July 5 12:54 PM WESTwebRootly[PagerDuty Incident](https://outsystems.pagerduty.com/incidents/Q0OOEIAGB6FKP0) has been created.
📲 Notified Joel Carvalho by push notification.  (via Android)July 5 12:54 PM WESTwebRootlyJoel Filipe Carvalho has been assigned as EngineerJuly 5 12:55 PM WESTwebJoel Filipe Carvalho
Incident has been started
July 5 12:55 PM WESTwebRootly
Pagerduty Integrations acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q0OOEIAGB6FKP0). (via Api)
July 5  1:04 PM WESTwebRootly
This incident was instantiated in Jira: RDINC-26544. Please work the incident using Rootly
July 5  1:08 PM WESTslackJoel Carvalho
This issue is tenant related and is not causing a system-wide impact.
July 5  1:15 PM WESTwebJoel Filipe Carvalho
Summary has been changed to 

&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;

&nbsp;&nbsp;
&nbsp;&nbsp;**ISSUE DESCRIPTION AND HOW TO REPRODUCE**
&nbsp;&nbsp;
A customer is running into Cloudfront errors during a security test, we don't have the method of testing however, Success team is gathering those details.

&nbsp;&nbsp;
According to Customer Success team, they indicate is that they are running the tests from a set of IPs and after a while these IPs are blocked for dozens of minutes, so they cannot continue to run their tests.

&nbsp;&nbsp;
The request form the customer is to whitelist the IPs from which they are running the tests so that they are not blocked as they are going through the test.
&nbsp;&nbsp;
&nbsp;&nbsp;**IMPACT ON THE CUSTOMER**
&nbsp;&nbsp;
High, blocked customer from performing the test, the customer has scheduled a new test run for July 15th to 18th (requested in ticket #3028432) and would like to understand how we can test the execution before they try to do the test again - every time they run these failed tests they have expensive consultants' time wasted.
&nbsp;&nbsp;
&nbsp;&nbsp;**TROUBLESHOOTING STEPS &amp; WORKAROUND**
&nbsp;&nbsp;
To be clear to R&amp;D team, we perform our investigation based on the reported 403 errors by the customer and we start:

&nbsp;&nbsp;

&nbsp;&nbsp;- Customer has the default and custom domain:
&nbsp;&nbsp;
&nbsp;&nbsp;

- &nbsp;&nbsp;&nbsp;&nbsp;

- Based on that, we check where the tests took place using this dashboard:
&nbsp;&nbsp;

- &nbsp;&nbsp;[https://outsystems.grafana.net/d/bdgf0fb2hcrnke/cloudfront-requests-per-ip-address?orgId=1&amp;var-distribution=All&amp;var-host=vki-test.outsystems.app&amp;var-client_ip=&amp;var-plus5m=1709297700&amp;from=1719874800000&amp;to=1719961199000](https://outsystems.grafana.net/d/bdgf0fb2hcrnke/cloudfront-requests-per-ip-address?orgId=1&amp;var-distribution=All&amp;var-host=vki-test.outsystems.app&amp;var-client_ip=&amp;var-plus5m=1709297700&amp;from=1719874800000&amp;to=1719961199000)&nbsp;&nbsp;
- The default domain doesn't have many request on July 2 but custom domain yes:
- 
- portal-qa.vki.at
- &nbsp;&nbsp;&nbsp;&nbsp;

&nbsp;&nbsp;

&nbsp;&nbsp;

- With that we understand the custom domain was used, customer said that a subset of IP's were used, however, we don't believe it per this graph where the IP has a huge recurrence:
&nbsp;&nbsp;

- 109.70.98.162

- Due to that we proceed our analysis to check why this IP was having 270k requests, and some were blocked during that day, specially during 7am to 13pm +/-
&nbsp;&nbsp;

- &nbsp;&nbsp;[https://outsystems.splunkcloud.com/en-US/app/e9ead269be9f433d8ecf621a1ca52f14/search?earliest=1719792000&amp;latest=now&amp;q=search%20index%3Daws_firewall_manager%20httpSourceName%3DCF%20AND%20action%3D%22BLOCK%22%20%22httpRequest.clientIp%22%3D%22109.70.98.162%22&amp;display.page.search.mode=smart&amp;dispatch.sample_ratio=1&amp;workload_pool=standard_perf&amp;display.general.type=events&amp;display.visualizations.charting.chart=line&amp;display.page.search.tab=events&amp;display.prefs.statistics.count=50&amp;sid=1720179678.6433054](https://outsystems.splunkcloud.com/en-US/app/e9ead269be9f433d8ecf621a1ca52f14/search?earliest=1719792000&amp;latest=now&amp;q=search%20index%3Daws_firewall_manager%20httpSourceName%3DCF%20AND%20action%3D%22BLOCK%22%20%22httpRequest.clientIp%22%3D%22109.70.98.162%22&amp;display.page.search.mode=smart&amp;dispatch.sample_ratio=1&amp;workload_pool=standard_perf&amp;display.general.type=events&amp;display.visualizations.charting.chart=line&amp;display.page.search.tab=events&amp;display.prefs.statistics.count=50&amp;sid=1720179678.6433054)&nbsp;&nbsp;
- We started to see the number of events blocked:
- &nbsp;&nbsp;&nbsp;&nbsp;
- By seeing such amount it seems was detected 23 rules of requests blocked:
- &nbsp;&nbsp;&nbsp;&nbsp;
- Based on that we compile those results in Splunk Chart to see all the 23 rules:
- &nbsp;&nbsp;[https://outsystems.splunkcloud.com/en-US/app/e9ead269be9f433d8ecf621a1ca52f14/search?earliest=1719792000&amp;latest=now&amp;q=search%20index%3Daws_firewall_manager%20httpSourceName%3DCF%20AND%20action%3D%22BLOCK%22%20%22httpRequest.clientIp%22%3D%22109.70.98.162%22%7C%20timechart%20count%20by%20ruleGroupList%7B%7D.terminatingRule.ruleId%20limit%3D30&amp;display.page.search.mode=smart&amp;dispatch.sample_ratio=1&amp;workload_pool=standard_perf&amp;display.general.type=visualizations&amp;display.visualizations.charting.chart=line&amp;display.page.search.tab=visualizations&amp;display.prefs.statistics.count=50&amp;display.events.fields=%5B%22host%22%2C%22source%22%2C%22sourcetype%22%2C%22ruleGroupList%7B%7D.terminatingRule.ruleId%22%5D&amp;sid=1720179813.6434232](https://outsystems.splunkcloud.com/en-US/app/e9ead269be9f433d8ecf621a1ca52f14/search?earliest=1719792000&amp;latest=now&amp;q=search%20index%3Daws_firewall_manager%20httpSourceName%3DCF%20AND%20action%3D%22BLOCK%22%20%22httpRequest.clientIp%22%3D%22109.70.98.162%22%7C%20timechart%20count%20by%20ruleGroupList%7B%7D.terminatingRule.ruleId%20limit%3D30&amp;display.page.search.mode=smart&amp;dispatch.sample_ratio=1&amp;workload_pool=standard_perf&amp;display.general.type=visualizations&amp;display.visualizations.charting.chart=line&amp;display.page.search.tab=visualizations&amp;display.prefs.statistics.count=50&amp;display.events.fields=%5B%22host%22%2C%22source%22%2C%22sourcetype%22%2C%22ruleGroupList%7B%7D.terminatingRule.ruleId%22%5D&amp;sid=1720179813.6434232)&nbsp;&nbsp;
- &nbsp;&nbsp;&nbsp;&nbsp;
- Customer said that when performing the tests they were getting some minutes where the requests were blacklist due to the amount, however, we don't think IP get blacklisted for that reason.

&nbsp;&nbsp;

&nbsp;&nbsp;

- At this point we had a call with several persons including (Rui Covelo, Joao Valentim, GS (including me) Daniel Lourenco e Francisco Freire) to discuss this situation)
&nbsp;&nbsp;

- And we would like your help on several points:
- Until this points is our analysis valid? We don't think requests are being blocked by the amount, but due to the patterns of attack.
- Does indeed exist more IP's doing the test, or only this one as we suspect?
- If the IP is not being blocked by rate limiting(we suspect not), is being backlisted due to the nature of the requests + the number of requests being made. So to say, why the IP gets blocked for some time, is this happening in our rules?
- We are getting more details on the tests to understand if they are being made currently with you help, but at this point we don't have them, however, currently is there any pattern they might be doing incorrectly?
Feel free to reach me directly.

&nbsp;&nbsp;

&nbsp;&nbsp;

&nbsp;&nbsp;**TECH DATA OR ANY OTHER RELEVANT INFO**
&nbsp;&nbsp;
Ring: ga

&nbsp;&nbsp;
Tenant Id: 46e2496a-5095-4f6f-86a1-5e660542c75c

&nbsp;&nbsp;
Tenant Prefix: vki

&nbsp;&nbsp;
Region: eu-central-1

&nbsp;&nbsp;
R0X.TSZ.ITI.MKS.ZYO.VHD.LDZ.AUT
&nbsp;&nbsp;
&nbsp;&nbsp;*&lt;! do not remove this line, this will be used to the trigger* Technical Support::Send to R&amp;D - ODC *#trigger_send_to_r&amp;d_odc !&gt;*&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;

&nbsp;&nbsp;July 5  1:15 PM WESTwebJoel Filipe Carvalho
Teams has been added: Global Routing
July 5  1:15 PM WESTwebJoel Filipe CarvalhoSystem-wide impact has been set: NoJuly 5  1:15 PM WESTwebJoel Filipe CarvalhoImpact has been set: It is being observed in just one tenant.July 5  1:16 PM WESTwebJoel Filipe CarvalhoSwarm has been set: Global Routing and SecurityJuly 5  1:16 PM WESTwebRootly
Pagerduty Integrations added Guilherme Reis as responder in [PagerDuty](https://outsystems.pagerduty.com/incidents/Q0OOEIAGB6FKP0)
July 5  1:17 PM WESTwebRootly
Guilherme Reis joined this [PagerDuty](https://outsystems.pagerduty.com/incidents/Q0OOEIAGB6FKP0) incident.
July 5  1:37 PM WESTslackguilherme.reis
Hello team, here are my findings:
&bull; First of all I would like to understand, since this is not causing any potencial service lost since it is a customer testing from a unique IP, why this is a SEV2 incident? ([severity document for reference](https://outsystemsrd.atlassian.net/wiki/spaces/CloudKB/pages/3506897056/ODC+-+Severity+Assessment))
&bull; The customer has been blocked by the FW managed rules that prevents attacks like SQL Injection and other which are deployed by a central managed FW that is managed by Security team.
&bull; We also have a public document that clearly states that the customers can do Load Testing and Penetration tests but **we do not turn off anything for them to do it** -&gt; [https://success.outsystems.com/support/security/load_and_penetration_tests_on_outsystems_cloud/](https://success.outsystems.com/support/security/load_and_penetration_tests_on_outsystems_cloud/)
&bull; Regarding the question, &quot;do the IP go into a blacklist when blocked by those rules?&quot;, we do not have visibility on that, so please reach Security Team since they are own those rules3
[image.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDA1ODEzLCJwdXIiOiJibG9iX2lkIn19--59cac425516250ed890b164280ed04135199ad86/image.png)July 5  1:37 PM WESTwebGuilherme Reis
Hello team, here are my findings:
First of all I would like to understand, since this is not causing any potencial service lost since it is a customer testing from a unique IP, why this is a SEV2 incident? (severity document for reference -&gt; https://outsystemsrd.atlassian.net/wiki/spaces/CloudKB/pages/3506897056/ODC+-+Severity+Assessment)
The customer has been blocked by the FW managed rules that prevents attacks like SQL Injection and other which are deployed by a central managed FW that is managed by Security team.
We also have a public document that clearly states that the customers can do Load Testing and Penetration tests but we do not turn off anything for them to do it -&gt; https://success.outsystems.com/support/security/load_and_penetration_tests_on_outsystems_cloud/ (image attached)
Regarding the question, &quot;do the IP go into a blacklist when blocked by those rules?&quot;, we do not have visibility on that, so please reach Security Team since they are own those rules
[Screenshot 2024-07-05 at 13.36.34.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDA1Nzk5LCJwdXIiOiJibG9iX2lkIn19--7540cdac3450371b801fe53cc7e1f0e32155e8f3/Screenshot%202024-07-05%20at%2013.36.34.png)July 5  1:54 PM WESTwebRootly
This incident was instantiated in Jira: RDINC-26544. Please work the incident using Rootly
July 5  2:08 PM WESTwebGuilherme Reis
Incident has been resolved
July 5  2:08 PM WESTwebGuilherme ReisResolution has been set: This is an expected behavior and also this should not be a Sev since accordingly to confluence document (https://outsystemsrd.atlassian.net/wiki/spaces/CloudKB/pages/3506897056/ODC+-+Severity+Assessment)