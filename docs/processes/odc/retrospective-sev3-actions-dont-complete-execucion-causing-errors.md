---
title: Retrospective-SEV3-Actions don't complete execucion causing errors
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4334780835/Retrospective-SEV3-Actions+don+t+complete+execucion+causing+errors
confluence_space: RKB
confluence_page_id: 4334780835
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV3-Actions don't complete execucion causing errors

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV3

Teams:&nbsp;trueBlueBackend Runtime
#### 🕐 Timestamps
Started At:&nbsp;trueBlueJuly 12 12:50 AM WEST

Mitigated At:&nbsp;trueYellowAugust 5  8:53 PM WEST

Resolved At:&nbsp;trueGreenAugust 5  8:53 PM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/704-actions-don-t-complete-execucion-causing-errors)
[Pagerduty incident](https://outsystems.pagerduty.com/incidents/Q1ZRB8ODSMNYVY)

[Slack channel](https://slack.com/app_redirect?channel=C07C6BM9CAG&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3035285)

#### Summary
&lt;hr&gt;
&lt;p class=&quot;redcarpet&quot;&gt;&lt;strong&gt;CONSIDERATIONS BEFORE PERFORMING THE ESCALATION TO R&amp;D (MANDATORY)&lt;/strong&gt;
&lt;br&gt;None of the below points should be overlooked. Failure to do so may imply unnecessary effort.&lt;/p&gt;
&lt;hr&gt;
&lt;p class=&quot;redcarpet&quot;&gt;Ensure the ticket has been &lt;strong&gt;categorized&lt;/strong&gt;, otherwise, the R&amp;D escalation will go unnoticed and not be worked on!&lt;/p&gt;&lt;p class=&quot;redcarpet&quot;&gt;&lt;strong&gt;1.&lt;/strong&gt; For &lt;strong&gt;Incidents&lt;/strong&gt;, the &lt;strong&gt;IMAX&lt;/strong&gt; was consulted &lt;strong&gt;beforehand&lt;/strong&gt; on which:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;No incident models were found for the reported symptoms &lt;strong&gt;OR&lt;/strong&gt;
&lt;/li&gt;
&lt;li&gt;The incident model did not solve the issue &lt;strong&gt;OR&lt;/strong&gt;
&lt;/li&gt;
&lt;li&gt;The next step indicated in the Incident Model is an escalation to R&amp;D.
&lt;strong&gt;2.&lt;/strong&gt; For &lt;strong&gt;Questions&lt;/strong&gt;, the ChatODC on the &lt;strong&gt;Slack channel&lt;/strong&gt; didn't return an acceptable answer.
&lt;strong&gt;3.&lt;/strong&gt; Any other requests that explicitly indicate an R&amp;D escalation is needed.
&lt;strong&gt;4&lt;/strong&gt;. &lt;strong&gt;Incident impact assessment&lt;/strong&gt; was based on the &lt;strong&gt;prioritization scoring matrix&lt;/strong&gt;.&lt;/li&gt;
&lt;/ul&gt;&lt;hr&gt;
&lt;p class=&quot;redcarpet&quot;&gt;&lt;strong&gt;R&amp;D ESCALATION FORM&lt;/strong&gt;
&lt;br&gt;Section comments can be removed for R&amp;D easier interpretation.&lt;/p&gt;&lt;p class=&quot;redcarpet&quot;&gt;&lt;strong&gt;ISSUE DESCRIPTION AND HOW TO REPRODUCE&lt;/strong&gt;&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Customer reporting multiple errors in their application, Uniflow&lt;/li&gt;
&lt;li&gt;The screens not working correctly as expected and the actions are not completing execution resulting in errors:&lt;ul&gt;
&lt;li&gt;&lt;img width=&quot;100%&quot; src=&quot;https://supportoutsystems.zendesk.com/attachments/token/wuwvZQhHgwPBvIiaF3wheB8IV/?name=1720696834000000000__ErroCommunication.png&quot;&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/li&gt;
&lt;/ul&gt;
&lt;p class=&quot;redcarpet&quot;&gt;&lt;strong&gt;IMPACT ON THE CUSTOMER&lt;/strong&gt;
&lt;br&gt;Brief description of the impact on the customer/development team/other, including:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Urgent, this is happening to a application in Production stage and affecting end users.&lt;/li&gt;
&lt;/ul&gt;
&lt;p class=&quot;redcarpet&quot;&gt;&lt;strong&gt;TROUBLESHOOTING STEPS &amp; WORKAROUND&lt;/strong&gt;&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Customer shared the steps to reproduce the error:&lt;ol&gt;
&lt;li&gt;Enter in Application&lt;/li&gt;
&lt;li&gt;Click in &quot;Uniflow&quot;&lt;/li&gt;
&lt;li&gt;Click in &quot;Solicita&ccedil;&otilde;es&quot;&lt;/li&gt;
&lt;li&gt;Filter number 14196&lt;/li&gt;
&lt;li&gt;Click in &quot;Ver detalhes&quot;&lt;/li&gt;
&lt;li&gt;Wait some seconds and the error appears:&lt;/li&gt;
&lt;li&gt;&lt;img width=&quot;100%&quot; src=&quot;https://supportoutsystems.zendesk.com/attachments/token/Kap5Vzd1rnLdhRm8Jy7hs4Dps/?name=1720725874000000000__Reproduction.png&quot;&gt;&lt;/li&gt;
&lt;/ol&gt;
&lt;/li&gt;
&lt;li&gt;Test user credentials:&lt;ul&gt;
&lt;li&gt;Login: &lt;a target=&quot;_blank&quot; href=&quot;ctrindal@emeal.nttdata.com&quot;&gt;ctrindal@emeal.nttdata.com&lt;/a&gt;
Password: Password2024
Link to acess: &lt;a target=&quot;_blank&quot; href=&quot;https://unileverbr.outsystems.app/Suppliers/Login&quot;&gt;https://unileverbr.outsystems.app/Suppliers/Login&lt;/a&gt;
&lt;/li&gt;
&lt;/ul&gt;
&lt;/li&gt;
&lt;li&gt;We were able to reproduce the issue following the credentials and steps to replicate:&lt;ul&gt;
&lt;li&gt;&lt;img width=&quot;100%&quot; src=&quot;https://supportoutsystems.zendesk.com/attachments/token/3f8WLAad2X1CcTp96Vp9Fz0U4/?name=image.png&quot;&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/li&gt;
&lt;li&gt;Get case action is pending and then fails:&lt;ul&gt;
&lt;li&gt;&lt;img width=&quot;100%&quot; src=&quot;https://supportoutsystems.zendesk.com/attachments/token/XVym3sejCYVJQy0Ft8nTS1HBV/?name=image.png&quot;&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/li&gt;
&lt;li&gt;Logs during the time of our attempts to replicate the issue:&lt;ul&gt;
&lt;li&gt;&lt;a target=&quot;_blank&quot; href=&quot;https://outsystems.grafana.net/d/cdeqzn1jj77cwe/general-troubleshooting?orgId=1&amp;amp;var-ring=ga&amp;amp;var-tenant=f23827c7-93d2-4764-a997-9f26697f6075&amp;amp;var-application=All&amp;amp;var-cluster=runp&amp;amp;var-cluster_old=All&amp;amp;var-severity=Error&amp;amp;var-runtime=All&amp;amp;var-filter=&amp;amp;var-exclude=&amp;amp;var-region=us-east-1&amp;amp;var-traceDuration=All&amp;amp;var-environment=All&amp;amp;var-regionShort=ga-us-east-1-01&amp;amp;var-tenant_prefix=unileverbr&amp;amp;var-module_name=&amp;amp;from=1720728614246&amp;amp;to=1720739414246&quot;&gt;https://outsystems.grafana.net/d/cdeqzn1jj77cwe/general-troubleshooting?orgId=1&amp;amp;var-ring=ga&amp;amp;var-tenant=f23827c7-93d2-4764-a997-9f26697f6075&amp;amp;var-application=All&amp;amp;var-cluster=runp&amp;amp;var-cluster_old=All&amp;amp;var-severity=Error&amp;amp;var-runtime=All&amp;amp;var-filter=&amp;amp;var-exclude=&amp;amp;var-region=us-east-1&amp;amp;var-traceDuration=All&amp;amp;var-environment=All&amp;amp;var-regionShort=ga-us-east-1-01&amp;amp;var-tenant_prefix=unileverbr&amp;amp;var-module_name=&amp;amp;from=1720728614246&amp;amp;to=1720739414246&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p class=&quot;redcarpet&quot;&gt;StackTrace respectively: (at .266 and then .235)&lt;/p&gt;
&lt;p class=&quot;redcarpet&quot;&gt;CommunicationException: CommunicationException: POST screenservices/Uniflow/MainFlow/UniflowRequestDetail/DataActionGetCase - 503 at co (&lt;a href=&quot;https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-runtime-core__1KlKlKCJPL84gC1yps95Bw.js?1KlKlKCJPL84gC1yps95Bw:8:58339&quot;&gt;https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-runtime-core__1KlKlKCJPL84gC1yps95Bw.js?1KlKlKCJPL84gC1yps95Bw:8:58339&lt;/a&gt;) at &lt;a href=&quot;https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-runtime-core__1KlKlKCJPL84gC1yps95Bw.js?1KlKlKCJPL84gC1yps95Bw:8:57882&quot;&gt;https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-runtime-core__1KlKlKCJPL84gC1yps95Bw.js?1KlKlKCJPL84gC1yps95Bw:8:57882&lt;/a&gt; at o (&lt;a href=&quot;https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-runtime-core__1KlKlKCJPL84gC1yps95Bw.js?1KlKlKCJPL84gC1yps95Bw:1:1037&quot;&gt;https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-runtime-core__1KlKlKCJPL84gC1yps95Bw.js?1KlKlKCJPL84gC1yps95Bw:1:1037&lt;/a&gt;) at i.invoke (&lt;a href=&quot;https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:26029&quot;&gt;https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:26029&lt;/a&gt;) at r.run (&lt;a href=&quot;https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:21220&quot;&gt;https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:21220&lt;/a&gt;) at &lt;a href=&quot;https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:15930&quot;&gt;https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:15930&lt;/a&gt; at i.invokeTask (&lt;a href=&quot;https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:26647&quot;&gt;https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:26647&lt;/a&gt;) at r.runTask (&lt;a href=&quot;https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:21972&quot;&gt;https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:21972&lt;/a&gt;) at g (&lt;a href=&quot;https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:28692)ExtraStack:&quot;&gt;https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:28692)ExtraStack:&lt;/a&gt; Error: POST screenservices/Uniflow/MainFlow/UniflowRequestDetail/DataActionGetCase - 503 at dr. (&lt;a href=&quot;https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-communication__5qqkdLIMsjBn97G3BeBMaQ.js?5qqkdLIMsjBn97G3BeBMaQ:1:47543&quot;&gt;https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-communication__5qqkdLIMsjBn97G3BeBMaQ.js?5qqkdLIMsjBn97G3BeBMaQ:1:47543&lt;/a&gt;) at Generator.next () at s (&lt;a href=&quot;https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-communication__5qqkdLIMsjBn97G3BeBMaQ.js?5qqkdLIMsjBn97G3BeBMaQ:1:379&quot;&gt;https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-communication__5qqkdLIMsjBn97G3BeBMaQ.js?5qqkdLIMsjBn97G3BeBMaQ:1:379&lt;/a&gt;) at i.invoke (&lt;a href=&quot;https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:26029&quot;&gt;https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:26029&lt;/a&gt;) at r.run (&lt;a href=&quot;https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:21220&quot;&gt;https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:21220&lt;/a&gt;) at &lt;a href=&quot;https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:15930&quot;&gt;https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:15930&lt;/a&gt; at i.invokeTask (&lt;a href=&quot;https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:26647&quot;&gt;https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:26647&lt;/a&gt;) at r.runTask (&lt;a href=&quot;https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:21972&quot;&gt;https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:21972&lt;/a&gt;) at g (&lt;a href=&quot;https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:28692&quot;&gt;https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:28692&lt;/a&gt;)&lt;/p&gt;
&lt;p class=&quot;redcarpet&quot;&gt;Error: Fetch POST Error - 503 at dr. (&lt;a href=&quot;https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-communication__5qqkdLIMsjBn97G3BeBMaQ.js?5qqkdLIMsjBn97G3BeBMaQ:1:47481&quot;&gt;https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-communication__5qqkdLIMsjBn97G3BeBMaQ.js?5qqkdLIMsjBn97G3BeBMaQ:1:47481&lt;/a&gt;) at s (&lt;a href=&quot;https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-communication__5qqkdLIMsjBn97G3BeBMaQ.js?5qqkdLIMsjBn97G3BeBMaQ:1:379&quot;&gt;https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-communication__5qqkdLIMsjBn97G3BeBMaQ.js?5qqkdLIMsjBn97G3BeBMaQ:1:379&lt;/a&gt;) at i.invoke (&lt;a href=&quot;https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:26029&quot;&gt;https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:26029&lt;/a&gt;) at r.run (&lt;a href=&quot;https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:21220&quot;&gt;https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:21220&lt;/a&gt;) at &lt;a href=&quot;https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:15930&quot;&gt;https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:15930&lt;/a&gt; at i.invokeTask (&lt;a href=&quot;https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:26647&quot;&gt;https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:26647&lt;/a&gt;) at r.runTask (&lt;a href=&quot;https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:21972&quot;&gt;https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:21972&lt;/a&gt;) at g (&lt;a href=&quot;https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:28692&quot;&gt;https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:28692&lt;/a&gt;)&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p class=&quot;redcarpet&quot;&gt;Collected HAR file:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;unileverbr.outsystems.app.har&lt;/li&gt;
&lt;/ul&gt;
&lt;/li&gt;
&lt;/ul&gt;
&lt;p class=&quot;redcarpet&quot;&gt;&lt;strong&gt;TECH DATA OR ANY OTHER RELEVANT INFO&lt;/strong&gt;&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Tenant ID:f23827c7-93d2-4764-a997-9f26697f6075&lt;/li&gt;
&lt;li&gt;Activation code: G5R.OL7.46W.672.16A.ZN2.ERD.06V&lt;/li&gt;
&lt;li&gt;Affected app OML:&lt;ul&gt;
&lt;li&gt;1720724215504_Uniflow.oml&lt;/li&gt;
&lt;/ul&gt;
&lt;/li&gt;
&lt;/ul&gt;
&lt;p class=&quot;redcarpet&quot;&gt;&lt;em&gt;&lt;! do not remove this line, this will be used to the trigger&lt;/em&gt; Technical Support::Send to R&amp;D - ODC &lt;em&gt;#trigger_send_to_r&amp;d_odc !&gt;&lt;/em&gt;&lt;/p&gt;&lt;p class=&quot;redcarpet&quot;&gt;Attachment(s):
&lt;br&gt;unileverbr.outsystems.app.har - &lt;a href=&quot;https://supportoutsystems.zendesk.com/attachments/token/HP38xtIF8atmopi9WQ6y0J0G5/?name=unileverbr.outsystems.app.har1720724215504_Uniflow.oml&quot;&gt;https://supportoutsystems.zendesk.com/attachments/token/HP38xtIF8atmopi9WQ6y0J0G5/?name=unileverbr.outsystems.app.har1720724215504_Uniflow.oml&lt;/a&gt; - &lt;a href=&quot;https://supportoutsystems.zendesk.com/attachments/token/y4ZA6kPu13VoPIqBk8gPFy5bc/?name=1720724215504_Uniflow.oml&quot;&gt;https://supportoutsystems.zendesk.com/attachments/token/y4ZA6kPu13VoPIqBk8gPFy5bc/?name=1720724215504_Uniflow.oml&lt;/a&gt;&lt;/p&gt;
## 📝 RetrospectiveinfoDetails
**Ring:** ga
**System-wide impact:**&nbsp; No
**Tenant ID:** f23827c7-93d2-4764-a997-9f26697f6075
**Tenant Prefix:** unileverbr
**Routing Error Code:** OS-CLRT
**Product Area:** -
### Impact:
The application became unresponsive. The issue was introduced by a low code change.
### Investigation and troubleshooting findings:
Solved in [https://outsystemsrd.atlassian.net/browse/RDINC-26859](https://outsystemsrd.atlassian.net/browse/RDINC-26859)
### Resolution:
Solved in [https://outsystemsrd.atlassian.net/browse/RDINC-26859](https://outsystemsrd.atlassian.net/browse/RDINC-26859)
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/704-actions-don-t-complete-execucion-causing-errors)

**Date**

**Source**

**User**

**Event**
July 12 12:44 AM WESTwebRootly
created an alert via
July 12 12:44 AM WESTwebRootly
Rootly created this incident
July 12 12:44 AM WESTwebRootly
In triage date has been set to July 12 12:44 AM WEST
July 12 12:44 AM WESTwebRootly[Slack Channel](https://slack.com/app_redirect?channel=C07C6BM9CAG&amp;team=T041063TZ) has been createdJuly 12 12:44 AM WESTwebRootly
Ring: ga
System-wide impact:  
Tenant ID: f23827c7-93d2-4764-a997-9f26697f6075
Tenant Prefix: unileverbr
Routing Error Code: OS-CLRT
Product Area: -
July 12 12:44 AM WESTwebRootly[PagerDuty Incident](https://outsystems.pagerduty.com/incidents/Q1ZRB8ODSMNYVY) has been created.
📲 Notified Pedro Quintas by push notification.  (via Android)&nbsp;&nbsp;📲 Notified Pedro Quintas by push notification.  (via Android)&nbsp;&nbsp;📧 Notified Pedro Quintas by email.July 12 12:44 AM WESTwebRootlyPedro Quintas has been assigned as EngineerJuly 12 12:45 AM WESTwebRootly
Pedro Quintas acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q1ZRB8ODSMNYVY)
July 12 12:50 AM WESTwebPedro Quintas
Incident has been started
July 12 12:50 AM WESTwebRootly
Pagerduty Integrations acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q1ZRB8ODSMNYVY). (via Mobile)
July 12 12:56 AM WESTwebPedro Quintas
The 503 status code indicates that the backend is unavailable. Moving this to the Backend Runtime team for further analysis.
July 12 12:57 AM WESTwebPedro QuintasSwarm has been set: Backend RuntimeJuly 12 12:57 AM WESTwebRootly
Pagerduty Integrations added Eduardo Tavares as responder in [PagerDuty](https://outsystems.pagerduty.com/incidents/Q1ZRB8ODSMNYVY)
July 12 12:57 AM WESTwebRootly
Pagerduty Integrations added Eduardo Tavares as responder in [PagerDuty](https://outsystems.pagerduty.com/incidents/Q1ZRB8ODSMNYVY)
July 12 12:57 AM WESTwebPedro Quintas
Teams has been removed: Client Runtime
July 12 12:57 AM WESTwebPedro Quintas
Pedro Quintas has been unassigned from Engineer
July 12 12:58 AM WESTwebRootly
Eduardo Tavares joined this [PagerDuty](https://outsystems.pagerduty.com/incidents/Q1ZRB8ODSMNYVY) incident.
July 12 12:59 AM WESTwebRootly
Delegated to EP for Neo BackendRuntime by Pedro Quintas through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q1ZRB8ODSMNYVY)
July 12  1:00 AM WESTwebRootly
Eduardo Tavares acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q1ZRB8ODSMNYVY). (via Mobile)
July 12  3:09 AM WESTslackEduardo Tavares (eta)
Hello Support.Upon examining the logs for a specific interval on July 11th between 15:00 and 16:00 (UTC+1), certain endpoints were successfully executed for the same application and pod, while a specific endpoint consistently returned a 503 UH no_healthy_upstream error from Istio logs.The following endpoints were executed without any issues:
&bull; /Uniflow/screenservices/Uniflow/MainFlow/InputFileWidget/DataActionGetCaseFiles2
&bull; /Uniflow/screenservices/Uniflow/MainFlow/Taskbox/DataActionGetCaseStatuses
However, the following endpoint experienced failures:
&bull; /Uniflow/screenservices/Uniflow/MainFlow/UniflowRequestDetail/DataActionGetCase
In the provided screenshots, it can be observed that during this whole interval, the application only had one replica (pod): 97374c87-ed95-4910-95d6-b28b98a22c20-f5d6947b4-ch9wj.This suggests that while the same replica successfully served endpoints DataActionGetCaseFiles2 and DataActionGetCaseStatuses, it was unable to serve DataActionGetCase.To further investigate this matter, having access to the OML for the application would be beneficial. It might help us identify any distinct patterns that differentiate the successful endpoints from the failed one, leading to some insight into how the application is generated for each case.For reference, please find the Istio logs at: [https://outsystems.grafana.net/goto/7iD-mL_IR?orgId=1](https://outsystems.grafana.net/goto/7iD-mL_IR?orgId=1)
and the Application logs at: [https://outsystems.grafana.net/goto/ZM-aiYlIg?orgId=1](https://outsystems.grafana.net/goto/ZM-aiYlIg?orgId=1)Thank you.
[image.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDA5NDI3LCJwdXIiOiJibG9iX2lkIn19--8e58e43f4a122917854e08965ddfa5ad6f83a50f/image.png)[image.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDA5NDI4LCJwdXIiOiJibG9iX2lkIn19--62b63eb2fdbf1d023d4a8bdae63235a66f71ba9d/image.png)[image.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDA5NDI5LCJwdXIiOiJibG9iX2lkIn19--5274d93ec695fab4d7cd7f313a3ec4517cfe4517/image.png)July 12  3:11 AM WESTwebEduardo TavaresSend ZenDesk private comment has been set: Hello, Global Support.
Please check my comment in the Rootly incident Slack channel.
Thank you.July 12  3:11 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hello, Global Support.
Please check my comment in the Rootly incident Slack channel.
Thank you.
July 12  3:11 AM WESTwebRootlySend ZenDesk private comment has been unsetJuly 12  3:11 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

July 12  3:56 AM WESTwebRootlyZendesk Private Comment has been set: ----------------------------------------------**Update to R&amp;D**Hello team,Attaching again OML for the affected application for further troubleshooting purpose.- 1720724215504_Uniflow.omlWe will wait for your next steps.Thank you as always.__July 12  3:56 AM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**Hello team,Attaching again OML for the affected application for further troubleshooting purpose.- 1720724215504_Uniflow.omlWe will wait for your next steps.Thank you as always.__
July 12  3:56 AM WESTwebRootlyZendesk Private Comment has been changed to: ------------------------------------------------ This notification was sent from Zendesk Support ticket #3035285 to all linked JIRA issues by Sugan Krishnan. --**Update to R&amp;D**Hello team,Attaching again OML for the affected application for further troubleshooting purpose.- 1720724215504_Uniflow.omlWe will wait for your next steps.Thank you as always._&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;__Attachments_1720724215504_Uniflow.omlJuly 12  3:56 AM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
------------------------------------------------ This notification was sent from Zendesk Support ticket #3035285 to all linked JIRA issues by Sugan Krishnan. --**Update to R&amp;D**Hello team,Attaching again OML for the affected application for further troubleshooting purpose.- 1720724215504_Uniflow.omlWe will wait for your next steps.Thank you as always.___Attachments_1720724215504_Uniflow.oml
July 12  9:20 AM WESTwebEduardo TavaresSend ZenDesk private comment has been set: Hello Support.Upon examining the logs for a specific interval on July 11th between 15:00 and 16:00 (UTC+1), certain endpoints were successfully executed for the same application and pod, while a specific endpoint consistently returned a 503 UH no_healthy_upstream error from Istio logs.The following endpoints were executed without any issues:- /Uniflow/screenservices/Uniflow/MainFlow/InputFileWidget/DataActionGetCaseFiles2
- /Uniflow/screenservices/Uniflow/MainFlow/Taskbox/DataActionGetCaseStatusesHowever, the following endpoint experienced failures:- /Uniflow/screenservices/Uniflow/MainFlow/UniflowRequestDetail/DataActionGetCaseIn the provided screenshots, it can be observed that during this whole interval, the application only had one replica (pod): 97374c87-ed95-4910-95d6-b28b98a22c20-f5d6947b4-ch9wj.This suggests that while the same replica successfully served endpoints DataActionGetCaseFiles2 and DataActionGetCaseStatuses, it was unable to serve DataActionGetCase.To further investigate this matter, having access to the OML for the application would be beneficial. It might help us identify any distinct patterns that differentiate the successful endpoints from the failed one, leading to some insight into how the application is generated for each case.For reference, please find the Istio logs at: [https://outsystems.grafana.net/goto/7iD-mL_IR?orgId=1](https://outsystems.grafana.net/goto/7iD-mL_IR?orgId=1)
and the Application logs at: [https://outsystems.grafana.net/goto/ZM-aiYlIg?orgId=1](https://outsystems.grafana.net/goto/ZM-aiYlIg?orgId=1)Thank you.Hello Support.Upon examining the logs for a specific interval on July 11th between 15:00 and 16:00 (UTC+1), certain endpoints were successfully executed for the same application and pod, while a specific endpoint consistently returned a 503 UH no_healthy_upstream error from Istio logs.The following endpoints were executed without any issues:- /Uniflow/screenservices/Uniflow/MainFlow/InputFileWidget/DataActionGetCaseFiles2
- /Uniflow/screenservices/Uniflow/MainFlow/Taskbox/DataActionGetCaseStatusesHowever, the following endpoint experienced failures:- /Uniflow/screenservices/Uniflow/MainFlow/UniflowRequestDetail/DataActionGetCaseIn the provided screenshots, it can be observed that during this whole interval, the application only had one replica (pod): 97374c87-ed95-4910-95d6-b28b98a22c20-f5d6947b4-ch9wj.This suggests that while the same replica successfully served endpoints DataActionGetCaseFiles2 and DataActionGetCaseStatuses, it was unable to serve DataActionGetCase.To further investigate this matter, having access to the OML for the application would be beneficial. It might help us identify any distinct patterns that differentiate the successful endpoints from the failed one, leading to some insight into how the application is generated for each case.For reference, please find the Istio logs at: [https://outsystems.grafana.net/goto/7iD-mL_IR?orgId=1](https://outsystems.grafana.net/goto/7iD-mL_IR?orgId=1)
and the Application logs at: [https://outsystems.grafana.net/goto/ZM-aiYlIg?orgId=1](https://outsystems.grafana.net/goto/ZM-aiYlIg?orgId=1)Thank you.July 12  9:20 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hello Support.Upon examining the logs for a specific interval on July 11th between 15:00 and 16:00 (UTC+1), certain endpoints were successfully executed for the same application and pod, while a specific endpoint consistently returned a 503 UH no_healthy_upstream error from Istio logs.The following endpoints were executed without any issues:- /Uniflow/screenservices/Uniflow/MainFlow/InputFileWidget/DataActionGetCaseFiles2
- /Uniflow/screenservices/Uniflow/MainFlow/Taskbox/DataActionGetCaseStatusesHowever, the following endpoint experienced failures:- /Uniflow/screenservices/Uniflow/MainFlow/UniflowRequestDetail/DataActionGetCaseIn the provided screenshots, it can be observed that during this whole interval, the application only had one replica (pod): 97374c87-ed95-4910-95d6-b28b98a22c20-f5d6947b4-ch9wj.This suggests that while the same replica successfully served endpoints DataActionGetCaseFiles2 and DataActionGetCaseStatuses, it was unable to serve DataActionGetCase.To further investigate this matter, having access to the OML for the application would be beneficial. It might help us identify any distinct patterns that differentiate the successful endpoints from the failed one, leading to some insight into how the application is generated for each case.For reference, please find the Istio logs at: [https://outsystems.grafana.net/goto/7iD-mL_IR?orgId=1](https://outsystems.grafana.net/goto/7iD-mL_IR?orgId=1)
and the Application logs at: [https://outsystems.grafana.net/goto/ZM-aiYlIg?orgId=1](https://outsystems.grafana.net/goto/ZM-aiYlIg?orgId=1)Thank you.Hello Support.Upon examining the logs for a specific interval on July 11th between 15:00 and 16:00 (UTC+1), certain endpoints were successfully executed for the same application and pod, while a specific endpoint consistently returned a 503 UH no_healthy_upstream error from Istio logs.The following endpoints were executed without any issues:- /Uniflow/screenservices/Uniflow/MainFlow/InputFileWidget/DataActionGetCaseFiles2
- /Uniflow/screenservices/Uniflow/MainFlow/Taskbox/DataActionGetCaseStatusesHowever, the following endpoint experienced failures:- /Uniflow/screenservices/Uniflow/MainFlow/UniflowRequestDetail/DataActionGetCaseIn the provided screenshots, it can be observed that during this whole interval, the application only had one replica (pod): 97374c87-ed95-4910-95d6-b28b98a22c20-f5d6947b4-ch9wj.This suggests that while the same replica successfully served endpoints DataActionGetCaseFiles2 and DataActionGetCaseStatuses, it was unable to serve DataActionGetCase.To further investigate this matter, having access to the OML for the application would be beneficial. It might help us identify any distinct patterns that differentiate the successful endpoints from the failed one, leading to some insight into how the application is generated for each case.For reference, please find the Istio logs at: [https://outsystems.grafana.net/goto/7iD-mL_IR?orgId=1](https://outsystems.grafana.net/goto/7iD-mL_IR?orgId=1)
and the Application logs at: [https://outsystems.grafana.net/goto/ZM-aiYlIg?orgId=1](https://outsystems.grafana.net/goto/ZM-aiYlIg?orgId=1)Thank you.
July 12  9:20 AM WESTwebRootlySend ZenDesk private comment has been unsetJuly 12  9:20 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

July 12 10:23 AM WESTwebRootlyZendesk Private Comment has been changed to: ----------------------------------------------**Update to R&amp;D**
Hello Eduardo and team,Thank you for your feedback and help.We attached the oml on a communication, but it seems is send as text, we discussed with rootly team and as workaround would be to use Jira:![](https://supportoutsystems.zendesk.com/attachments/token/SysZW50KURlh7KNryS3SeHVBr/?name=image.png)
Nevertheless, will leave the url to download -&gt; https://supportoutsystems.zendesk.com/attachments/token/y4ZA6kPu13VoPIqBk8gPFy5bc/?name=1720724215504_Uniflow.omlAnything feel free to reach me.Best regards,_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_July 12 10:23 AM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
Hello Eduardo and team,Thank you for your feedback and help.We attached the oml on a communication, but it seems is send as text, we discussed with rootly team and as workaround would be to use Jira:![](https://supportoutsystems.zendesk.com/attachments/token/SysZW50KURlh7KNryS3SeHVBr/?name=image.png)
Nevertheless, will leave the url to download -&gt; https://supportoutsystems.zendesk.com/attachments/token/y4ZA6kPu13VoPIqBk8gPFy5bc/?name=1720724215504_Uniflow.omlAnything feel free to reach me.Best regards,__
July 12 10:24 AM WESTwebRootlyZendesk Private Comment has been changed to: ------------------------------------------------ This notification was sent from Zendesk Support ticket #3035285 to all linked JIRA issues by Cristiano Costa. --**Update to R&amp;D**
Hello Eduardo and team,Thank you for your feedback and help.We attached the oml on a communication, but it seems is send as text, we discussed with rootly team and as workaround would be to use Jira:Attachment - image.png
Nevertheless, will leave the url to download -&gt; https://supportoutsystems.zendesk.com/attachments/token/y4ZA6kPu13VoPIqBk8gPFy5bc/?name=1720724215504_Uniflow.omlAnything feel free to reach me.Best regards,_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;__Attachments_1720724215504_Uniflow.omlJuly 12 10:24 AM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
------------------------------------------------ This notification was sent from Zendesk Support ticket #3035285 to all linked JIRA issues by Cristiano Costa. --**Update to R&amp;D**
Hello Eduardo and team,Thank you for your feedback and help.We attached the oml on a communication, but it seems is send as text, we discussed with rootly team and as workaround would be to use Jira:Attachment - image.png
Nevertheless, will leave the url to download -&gt; https://supportoutsystems.zendesk.com/attachments/token/y4ZA6kPu13VoPIqBk8gPFy5bc/?name=1720724215504_Uniflow.omlAnything feel free to reach me.Best regards,___Attachments_1720724215504_Uniflow.oml
July 12 11:26 AM WESTwebEduardo TavaresSend ZenDesk private comment has been set: Hello Global Support.After conducting a thorough examination of the errors, our team discovered that the failed requests stem from the application being unavailable during specific intervals.We have identified that a recursive implementation in the Get_UserName function, which ultimately leads to a stack overflow, is the cause of these outages.We have observed that the customer has deployed more revisions of the application since the problem occurred, suggesting that the problematic behavior may have been addressed.Please, verify with the customer whether the aforementioned information is accurate.For more details on this matter, please refer to the following link:
[https://outsystems.grafana.net/goto/RF3v3L_SR?orgId=1](https://outsystems.grafana.net/goto/RF3v3L_SR?orgId=1)The specific issue can be found at ssUniflow.ScreenServices.Uniflow_MainFlow_UniflowRequestDetail_ScreenModel+ and ssUniflow.Actions.ActionGet_UserName.Thanks.July 12 11:26 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hello Global Support.After conducting a thorough examination of the errors, our team discovered that the failed requests stem from the application being unavailable during specific intervals.We have identified that a recursive implementation in the Get_UserName function, which ultimately leads to a stack overflow, is the cause of these outages.We have observed that the customer has deployed more revisions of the application since the problem occurred, suggesting that the problematic behavior may have been addressed.Please, verify with the customer whether the aforementioned information is accurate.For more details on this matter, please refer to the following link:
[https://outsystems.grafana.net/goto/RF3v3L_SR?orgId=1](https://outsystems.grafana.net/goto/RF3v3L_SR?orgId=1)The specific issue can be found at ssUniflow.ScreenServices.Uniflow_MainFlow_UniflowRequestDetail_ScreenModel+ and ssUniflow.Actions.ActionGet_UserName.Thanks.
July 12 11:26 AM WESTwebRootlySend ZenDesk private comment has been unsetJuly 12 11:26 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

July 13 12:45 PM WESTwebRootlyZenDesk Event Type has been set: solvedJuly 13 12:45 PM WESTwebRootly
The Global Support team marked this incident as closed in ZenDesk.
July 14  9:05 PM WESTwebEduardo TavaresSend ZenDesk private comment has been set: Hello Global Support.Considering the findings from our team's troubleshooting, we suggest lowering the severity of this case to Normal. Given it's a behavior introduced by the customer's logic.July 14  9:05 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hello Global Support.Considering the findings from our team's troubleshooting, we suggest lowering the severity of this case to Normal. Given it's a behavior introduced by the customer's logic.
July 14  9:05 PM WESTwebRootlySend ZenDesk private comment has been unsetJuly 14  9:05 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

July 16  8:53 AM WESTwebEduardo TavaresSend ZenDesk private comment has been set: Hello Global Support.Did you manage to see my last comment? Regarding lowering the severity of this case to Normal?Thanks.July 16  8:53 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hello Global Support.Did you manage to see my last comment? Regarding lowering the severity of this case to Normal?Thanks.
July 16  8:53 AM WESTwebRootlySend ZenDesk private comment has been unsetJuly 16  8:53 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

July 16  4:06 PM WESTwebEduardo Tavares
Summary has been changed to 

&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;

&nbsp;&nbsp;
&nbsp;&nbsp;**CONSIDERATIONS BEFORE PERFORMING THE ESCALATION TO R&amp;D (MANDATORY)**
&nbsp;&nbsp;
None of the below points should be overlooked. Failure to do so may imply unnecessary effort.

&nbsp;&nbsp;
&nbsp;&nbsp;
Ensure the ticket has been **categorized**, otherwise, the R&amp;D escalation will go unnoticed and not be worked on!
&nbsp;&nbsp;
&nbsp;&nbsp;**1.** For **Incidents**, the **IMAX** was consulted **beforehand** on which:

&nbsp;&nbsp;

&nbsp;&nbsp;- No incident models were found for the reported symptoms **OR**
&nbsp;&nbsp;

&nbsp;&nbsp;- The incident model did not solve the issue **OR**
&nbsp;&nbsp;

&nbsp;&nbsp;- The next step indicated in the Incident Model is an escalation to R&amp;D.

&nbsp;&nbsp;**2.** For **Questions**, the ChatODC on the **Slack channel** didn't return an acceptable answer.

&nbsp;&nbsp;**3.** Any other requests that explicitly indicate an R&amp;D escalation is needed.

&nbsp;&nbsp;**4**. **Incident impact assessment** was based on the **prioritization scoring matrix**.

&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;

&nbsp;&nbsp;
&nbsp;&nbsp;**R&amp;D ESCALATION FORM**
&nbsp;&nbsp;
Section comments can be removed for R&amp;D easier interpretation.
&nbsp;&nbsp;
&nbsp;&nbsp;**ISSUE DESCRIPTION AND HOW TO REPRODUCE**&nbsp;&nbsp;

&nbsp;&nbsp;

&nbsp;&nbsp;- Customer reporting multiple errors in their application, Uniflow

&nbsp;&nbsp;- The screens not working correctly as expected and the actions are not completing execution resulting in errors:
&nbsp;&nbsp;
&nbsp;&nbsp;

- &nbsp;&nbsp;&nbsp;&nbsp;

&nbsp;&nbsp;

&nbsp;&nbsp;

&nbsp;&nbsp;**IMPACT ON THE CUSTOMER**
&nbsp;&nbsp;
Brief description of the impact on the customer/development team/other, including:

&nbsp;&nbsp;

&nbsp;&nbsp;- Urgent, this is happening to a application in Production stage and affecting end users.

&nbsp;&nbsp;

&nbsp;&nbsp;
&nbsp;&nbsp;**TROUBLESHOOTING STEPS &amp; WORKAROUND**&nbsp;&nbsp;

&nbsp;&nbsp;

&nbsp;&nbsp;- Customer shared the steps to reproduce the error:
&nbsp;&nbsp;
&nbsp;&nbsp;
- Enter in Application
- Click in &quot;Uniflow&quot;
- Click in &quot;Solicita&ccedil;&otilde;es&quot;
- Filter number 14196
- Click in &quot;Ver detalhes&quot;
- Wait some seconds and the error appears:
- &nbsp;&nbsp;&nbsp;&nbsp;

- Test user credentials:
&nbsp;&nbsp;

- Login: [ctrindal@emeal.nttdata.com](ctrindal@emeal.nttdata.com)
Password: Password2024
Link to acess: [https://unileverbr.outsystems.app/Suppliers/Login](https://unileverbr.outsystems.app/Suppliers/Login)

- We were able to reproduce the issue following the credentials and steps to replicate:
&nbsp;&nbsp;

- &nbsp;&nbsp;&nbsp;&nbsp;

- Get case action is pending and then fails:
&nbsp;&nbsp;

- &nbsp;&nbsp;&nbsp;&nbsp;

- Logs during the time of our attempts to replicate the issue:
&nbsp;&nbsp;

- &nbsp;&nbsp;[https://outsystems.grafana.net/d/cdeqzn1jj77cwe/general-troubleshooting?orgId=1&amp;var-ring=ga&amp;var-tenant=f23827c7-93d2-4764-a997-9f26697f6075&amp;var-application=All&amp;var-cluster=runp&amp;var-cluster_old=All&amp;var-severity=Error&amp;var-runtime=All&amp;var-filter=&amp;var-exclude=&amp;var-region=us-east-1&amp;var-traceDuration=All&amp;var-environment=All&amp;var-regionShort=ga-us-east-1-01&amp;var-tenant_prefix=unileverbr&amp;var-module_name=&amp;from=1720728614246&amp;to=1720739414246](https://outsystems.grafana.net/d/cdeqzn1jj77cwe/general-troubleshooting?orgId=1&amp;var-ring=ga&amp;var-tenant=f23827c7-93d2-4764-a997-9f26697f6075&amp;var-application=All&amp;var-cluster=runp&amp;var-cluster_old=All&amp;var-severity=Error&amp;var-runtime=All&amp;var-filter=&amp;var-exclude=&amp;var-region=us-east-1&amp;var-traceDuration=All&amp;var-environment=All&amp;var-regionShort=ga-us-east-1-01&amp;var-tenant_prefix=unileverbr&amp;var-module_name=&amp;from=1720728614246&amp;to=1720739414246)&nbsp;&nbsp;

- 
&nbsp;&nbsp;
StackTrace respectively: (at .266 and then .235)

&nbsp;&nbsp;
CommunicationException: CommunicationException: POST screenservices/Uniflow/MainFlow/UniflowRequestDetail/DataActionGetCase - 503 at co ([&nbsp;&nbsp;](https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-runtime-core__1KlKlKCJPL84gC1yps95Bw.js?1KlKlKCJPL84gC1yps95Bw:8:58339)&nbsp;&nbsp;[https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-runtime-core__1KlKlKCJPL84gC1yps95Bw.js?1KlKlKCJPL84gC1yps95Bw:8:58339](https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-runtime-core__1KlKlKCJPL84gC1yps95Bw.js?1KlKlKCJPL84gC1yps95Bw:8:58339)) at [&nbsp;&nbsp;](https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-runtime-core__1KlKlKCJPL84gC1yps95Bw.js?1KlKlKCJPL84gC1yps95Bw:8:57882)&nbsp;&nbsp;[https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-runtime-core__1KlKlKCJPL84gC1yps95Bw.js?1KlKlKCJPL84gC1yps95Bw:8:57882](https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-runtime-core__1KlKlKCJPL84gC1yps95Bw.js?1KlKlKCJPL84gC1yps95Bw:8:57882) at o ([&nbsp;&nbsp;](https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-runtime-core__1KlKlKCJPL84gC1yps95Bw.js?1KlKlKCJPL84gC1yps95Bw:1:1037)&nbsp;&nbsp;[https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-runtime-core__1KlKlKCJPL84gC1yps95Bw.js?1KlKlKCJPL84gC1yps95Bw:1:1037](https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-runtime-core__1KlKlKCJPL84gC1yps95Bw.js?1KlKlKCJPL84gC1yps95Bw:1:1037)) at i.invoke ([&nbsp;&nbsp;](https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:26029)&nbsp;&nbsp;[https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:26029](https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:26029)) at r.run ([&nbsp;&nbsp;](https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:21220)&nbsp;&nbsp;[https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:21220](https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:21220)) at [&nbsp;&nbsp;](https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:15930)&nbsp;&nbsp;[https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:15930](https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:15930) at i.invokeTask ([&nbsp;&nbsp;](https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:26647)&nbsp;&nbsp;[https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:26647](https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:26647)) at r.runTask ([&nbsp;&nbsp;](https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:21972)&nbsp;&nbsp;[https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:21972](https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:21972)) at g ([&nbsp;&nbsp;](https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:28692)ExtraStack:)&nbsp;&nbsp;[https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:28692)ExtraStack:](https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:28692)ExtraStack:) Error: POST screenservices/Uniflow/MainFlow/UniflowRequestDetail/DataActionGetCase - 503 at dr. ([&nbsp;&nbsp;](https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-communication__5qqkdLIMsjBn97G3BeBMaQ.js?5qqkdLIMsjBn97G3BeBMaQ:1:47543)&nbsp;&nbsp;[https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-communication__5qqkdLIMsjBn97G3BeBMaQ.js?5qqkdLIMsjBn97G3BeBMaQ:1:47543](https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-communication__5qqkdLIMsjBn97G3BeBMaQ.js?5qqkdLIMsjBn97G3BeBMaQ:1:47543)) at Generator.next () at s ([&nbsp;&nbsp;](https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-communication__5qqkdLIMsjBn97G3BeBMaQ.js?5qqkdLIMsjBn97G3BeBMaQ:1:379)&nbsp;&nbsp;[https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-communication__5qqkdLIMsjBn97G3BeBMaQ.js?5qqkdLIMsjBn97G3BeBMaQ:1:379](https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-communication__5qqkdLIMsjBn97G3BeBMaQ.js?5qqkdLIMsjBn97G3BeBMaQ:1:379)) at i.invoke ([&nbsp;&nbsp;](https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:26029)&nbsp;&nbsp;[https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:26029](https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:26029)) at r.run ([&nbsp;&nbsp;](https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:21220)&nbsp;&nbsp;[https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:21220](https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:21220)) at [&nbsp;&nbsp;](https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:15930)&nbsp;&nbsp;[https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:15930](https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:15930) at i.invokeTask ([&nbsp;&nbsp;](https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:26647)&nbsp;&nbsp;[https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:26647](https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:26647)) at r.runTask ([&nbsp;&nbsp;](https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:21972)&nbsp;&nbsp;[https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:21972](https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:21972)) at g ([&nbsp;&nbsp;](https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:28692)&nbsp;&nbsp;[https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:28692](https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:28692))

&nbsp;&nbsp;
Error: Fetch POST Error - 503 at dr. ([&nbsp;&nbsp;](https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-communication__5qqkdLIMsjBn97G3BeBMaQ.js?5qqkdLIMsjBn97G3BeBMaQ:1:47481)&nbsp;&nbsp;[https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-communication__5qqkdLIMsjBn97G3BeBMaQ.js?5qqkdLIMsjBn97G3BeBMaQ:1:47481](https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-communication__5qqkdLIMsjBn97G3BeBMaQ.js?5qqkdLIMsjBn97G3BeBMaQ:1:47481)) at s ([&nbsp;&nbsp;](https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-communication__5qqkdLIMsjBn97G3BeBMaQ.js?5qqkdLIMsjBn97G3BeBMaQ:1:379)&nbsp;&nbsp;[https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-communication__5qqkdLIMsjBn97G3BeBMaQ.js?5qqkdLIMsjBn97G3BeBMaQ:1:379](https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-communication__5qqkdLIMsjBn97G3BeBMaQ.js?5qqkdLIMsjBn97G3BeBMaQ:1:379)) at i.invoke ([&nbsp;&nbsp;](https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:26029)&nbsp;&nbsp;[https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:26029](https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:26029)) at r.run ([&nbsp;&nbsp;](https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:21220)&nbsp;&nbsp;[https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:21220](https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:21220)) at [&nbsp;&nbsp;](https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:15930)&nbsp;&nbsp;[https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:15930](https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:15930) at i.invokeTask ([&nbsp;&nbsp;](https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:26647)&nbsp;&nbsp;[https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:26647](https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:26647)) at r.runTask ([&nbsp;&nbsp;](https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:21972)&nbsp;&nbsp;[https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:21972](https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:21972)) at g ([&nbsp;&nbsp;](https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:28692)&nbsp;&nbsp;[https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:28692](https://unileverbr.outsystems.app/Uniflow/scripts/outsystems-logger__mL1v58gc7ZxLSwhXzfMuJQ.js?mL1v58gc7ZxLSwhXzfMuJQ:7:28692))

&nbsp;&nbsp;

&nbsp;&nbsp;- 
&nbsp;&nbsp;
Collected HAR file:

&nbsp;&nbsp;

&nbsp;&nbsp;- unileverbr.outsystems.app.har

&nbsp;&nbsp;

&nbsp;&nbsp;
&nbsp;&nbsp;
&nbsp;&nbsp;

&nbsp;&nbsp;**TECH DATA OR ANY OTHER RELEVANT INFO**&nbsp;&nbsp;

&nbsp;&nbsp;

&nbsp;&nbsp;- Tenant ID:f23827c7-93d2-4764-a997-9f26697f6075

&nbsp;&nbsp;- Activation code: G5R.OL7.46W.672.16A.ZN2.ERD.06V

&nbsp;&nbsp;- Affected app OML:
&nbsp;&nbsp;
&nbsp;&nbsp;

- 1720724215504_Uniflow.oml

&nbsp;&nbsp;

&nbsp;&nbsp;

&nbsp;&nbsp;*&lt;! do not remove this line, this will be used to the trigger* Technical Support::Send to R&amp;D - ODC *#trigger_send_to_r&amp;d_odc !&gt;*&nbsp;&nbsp;
&nbsp;&nbsp;
Attachment(s):

&nbsp;&nbsp;
unileverbr.outsystems.app.har - [&nbsp;&nbsp;](https://supportoutsystems.zendesk.com/attachments/token/HP38xtIF8atmopi9WQ6y0J0G5/?name=unileverbr.outsystems.app.har1720724215504_Uniflow.oml)&nbsp;&nbsp;[https://supportoutsystems.zendesk.com/attachments/token/HP38xtIF8atmopi9WQ6y0J0G5/?name=unileverbr.outsystems.app.har1720724215504_Uniflow.oml](https://supportoutsystems.zendesk.com/attachments/token/HP38xtIF8atmopi9WQ6y0J0G5/?name=unileverbr.outsystems.app.har1720724215504_Uniflow.oml) - [&nbsp;&nbsp;](https://supportoutsystems.zendesk.com/attachments/token/y4ZA6kPu13VoPIqBk8gPFy5bc/?name=1720724215504_Uniflow.oml)&nbsp;&nbsp;[https://supportoutsystems.zendesk.com/attachments/token/y4ZA6kPu13VoPIqBk8gPFy5bc/?name=1720724215504_Uniflow.oml](https://supportoutsystems.zendesk.com/attachments/token/y4ZA6kPu13VoPIqBk8gPFy5bc/?name=1720724215504_Uniflow.oml)&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;July 16  4:06 PM WESTwebEduardo Tavares
Severity has been changed from SEV1 to SEV3
July 16  4:06 PM WESTwebEduardo TavaresImpact has been set: The application became unresponsive. The issue was introduced by a low code change.August 5  8:53 PM WESTwebRui Garcia
Incident has been resolved
August 5  8:53 PM WESTwebRui GarciaSystem-wide impact has been set: NoAugust 5  8:53 PM WESTwebRui GarciaInvestigation and troubleshooting findings has been set: Solved in https://outsystemsrd.atlassian.net/browse/RDINC-26859August 5  8:53 PM WESTwebRui GarciaResolution has been set: Solved in https://outsystemsrd.atlassian.net/browse/RDINC-26859August 5  8:53 PM WESTwebRootly
Pagerduty Integrations marked the incident as resolved through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q1ZRB8ODSMNYVY). (via Api)