---
title: Retrospective-SEV1-Support non-Latin characters on Extranet ODC tenant's database
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4201676961/Retrospective-SEV1-Support+non-Latin+characters+on+Extranet+ODC+tenant+s+database
confluence_space: RKB
confluence_page_id: 4201676961
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV1-Support non-Latin characters on Extranet ODC tenant's database

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV1

Teams:&nbsp;trueBlueNeo Platform Runtime Data Model
#### 🕐 Timestamps
Started At:&nbsp;trueBlueJune 7  3:41 PM WEST

Mitigated At:&nbsp;trueYellowJune 7  4:57 PM WEST

Resolved At:&nbsp;trueGreenJune 7  4:57 PM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/541-support-non-latin-characters-on-extranet-odc-tenant-s-database)
[Confluence page](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4202201197/Retrospective-SEV1-Support+non-Latin+characters+on+Extranet+ODC+tenant's+database)

[Pagerduty incident](https://outsystems.pagerduty.com/incidents/Q32AZCU77F7N2P)

[Slack channel](https://slack.com/app_redirect?channel=C077SAAB3B2&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3017989)

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

Joana

**Commander**

Tiago
#### Summary
----------------------------------------------**CONSIDERATIONS BEFORE PERFORMING THE ESCALATION TO R&amp;D (MANDATORY)**
None of the below points should be overlooked. Failure to do so may imply unnecessary effort.* * *
Ensure the ticket has been **categorized**, otherwise, the R&amp;D escalation will go unnoticed and not be worked on!**1.** For **Incidents**, the **IMAX** was consulted **beforehand** on which:- No incident models were found for the reported symptoms **OR**
- The incident model did not solve the issue **OR**
- The next step indicated in the Incident Model is an escalation to R&amp;D.
**2.** For **Questions**, the ChatODC on the **Slack channel** didn't return an acceptable answer.
**3.** Any other requests that explicitly indicate an R&amp;D escalation is needed.
**4**. **Incident impact assessment** was based on the **prioritization scoring matrix**.* * ***R&amp;D ESCALATION FORM**
Section comments can be removed for R&amp;D easier interpretation.**ISSUE DESCRIPTION AND HOW TO REPRODUCE**- This applications provides AI summaries, and if it uses non-Latin characters, they'll all be converted into question marks as in the example below:&gt; **Original message:**
&gt;
&gt; - Subject: ملخص المكالمة والخطوات التالية
&gt; - Body: مرحبا، شكرا على وقتك اليوم. اتفقنا على عدد من النقاط الرئيسية بما في ذلك تجديد العقد والتسعير. سنقدم الخصم المتفق عليه ونستوعب زيادة المستخدمين في العقد. نحن نتطلع إلى مواصلة الشراكة القوية بيننا. سأكون في انتظار تأكيدك. تحياتي، خالد&quot;,
&gt;
&gt; **Content stored in the BD**:
&gt;
&gt; - Subject: ???? ???????? ???????? ???????
&gt; - Body: ?????? ???? ??? ???? ?????. ?????? ??? ??? ?? ?????? ???????? ??? ?? ??? ????? ????? ????????. ????? ????? ?????? ???? ??????? ????? ?????????? ?? ?????. ??? ????? ??? ?????? ??????? ?????? ?????. ????? ?? ?????? ??????. ??????? ????**IMPACT ON THE CUSTOMER**- One of this applications' main purposes is to provide AI summaries of meetings that our colleagues from Sales have with prospects, and if any of the content is in non-latin characters, then it's really not usable. Given this scenario, for a significant set of our colleagues, this portion of the application doesn't work at all.**TROUBLESHOOTING STEPS &amp; WORKAROUND**- It's unclear to us if this behavior is expected due to the characters not being supported or if there's some unexpected behavior going on here.
- Could you help us understand if these characters are meant to be supported by the Database and what may be done to resolve this?**TECH DATA OR ANY OTHER RELEVANT INFO**- Ring: osall
- Tenant Id: fae0814c-7560-49cc-886f-6b4eccb6709f
- Tenant Prefix: extranet
- Region: us-east-1_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 RetrospectiveinfoDetails
**Ring:** osall
**System-wide impact:**&nbsp; No
**Tenant ID:** fae0814c-7560-49cc-886f-6b4eccb6709f
**Tenant Prefix:** extranet
**Routing Error Code:** N/A
**Product Area:** Phoenix::Application Runtime::Database access
### Impact:
Application runtime of one customer. One pattern not working. This is a problem with external database, so it's not a platform issue.
### Investigation and troubleshooting findings:
We are trying to replicate. With one table of type text we are able to insert and read non latin characters in edit data and application runtime.

Support team confirmed this is a problem in a external database.
### Resolution:
Supposedly the customer need to fix the external database encoding/collate
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/541-support-non-latin-characters-on-extranet-odc-tenant-s-database)

**Date**

**Source**

**User**

**Event**
June 7  3:18 PM WESTwebRootly
created an alert via
June 7  3:18 PM WESTwebRootly
Rootly created this incident
June 7  3:18 PM WESTwebRootly
In triage date has been set to June 7  3:18 PM WEST
June 7  3:18 PM WESTwebRootly[Slack Channel](https://slack.com/app_redirect?channel=C077SAAB3B2&amp;team=T041063TZ) has been createdJune 7  3:18 PM WESTwebRootly
Ring: osall
System-wide impact:  
Tenant ID: fae0814c-7560-49cc-886f-6b4eccb6709f
Tenant Prefix: extranet
Routing Error Code: N/A
Product Area: Phoenix::Application Runtime::Database access
June 7  3:18 PM WESTwebRootly[PagerDuty Incident](https://outsystems.pagerduty.com/incidents/Q32AZCU77F7N2P) has been created.
📧 Notified Joana Barradas by email.&nbsp;&nbsp;📱 Notified Joana Barradas by SMS.&nbsp;&nbsp;📲 Notified Joana Barradas by push notification.  (via Android)June 7  3:18 PM WESTwebRootlyJoana has been assigned as EngineerJune 7  3:19 PM WESTwebRootly
Joana Barradas acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q32AZCU77F7N2P). (via Phone)
June 7  3:41 PM WESTwebJoana
Incident has been started
June 7  3:41 PM WESTwebRootly
Pagerduty Integrations acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q32AZCU77F7N2P). (via Phone)
June 7  3:53 PM WESTwebJoanaJoana has been assigned as CommanderJune 7  3:53 PM WESTwebTiagoTiago has been assigned as CommanderJune 7  3:54 PM WESTwebTiago
Tiago has been unassigned from Commander
June 7  3:55 PM WESTwebJoanaTiago has been assigned as CommanderJune 7  4:08 PM WESTwebJoanaSystem-wide impact has been set: NoJune 7  4:08 PM WESTwebJoanaImpact has been set: Application runtime of one customer. One pattern not working. Still not replicatedJune 7  4:08 PM WESTwebJoanaInvestigation and troubleshooting findings has been set: We are trying to replicate. With one table of type text we are able to insert and read non latin characters in edit data and application runtime.June 7  4:13 PM WESTwebJoanaSend ZenDesk private comment has been set: Hello Support,
We try to reproduce the issue and by simply create an entity, scaffolding to a screen we are able to insert and fetch records with non latin characters.
Can you please check with the customer if that database is external?
Can you please try to reproduce the pattern and send us a simple oml?Best regards,
Joana BarradasJune 7  4:13 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hello Support,
We try to reproduce the issue and by simply create an entity, scaffolding to a screen we are able to insert and fetch records with non latin characters.
Can you please check with the customer if that database is external?
Can you please try to reproduce the pattern and send us a simple oml?Best regards,
Joana Barradas
June 7  4:13 PM WESTwebRootlySend ZenDesk private comment has been unsetJune 7  4:13 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

June 7  4:46 PM WESTslackcristiano.costa
Hey team, apologize for the radio silence, I was on call with Ricardo (customer), and the source of the problem seems the external database that might have the incorrect encoding/collate since the source already brings the &quot;?&quot; chars (prove screenshot below). Ricardo is going to reach the owners of the database/digital to correct it.
[image.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mzg5NzE2LCJwdXIiOiJibG9iX2lkIn19--9b965e7481bd117d29d33b0b4ac4228cae34c09f/image.png)June 7  4:57 PM WESTwebJoana
Incident has been resolved
June 7  4:57 PM WESTwebJoanaInvestigation and troubleshooting findings has been changed to: We are trying to replicate. With one table of type text we are able to insert and read non latin characters in edit data and application runtime.
Support team confirmed this is a problem in a external database.June 7  4:57 PM WESTwebJoanaImpact has been changed to: Application runtime of one customer. One pattern not working. This is a problem with external database, so it's not a platform issue.June 7  4:57 PM WESTwebJoanaResolution has been set: Supposedly the customer need to fix the external database encoding/collateJune 7  4:57 PM WESTwebRootly[Confluence Page](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4202201197/Retrospective-SEV1-Support+non-Latin+characters+on+Extranet+ODC+tenant's+database) has been createdJune 7  4:57 PM WESTwebRootly
The retrospective document created can be checked here: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4202201197/Retrospective-SEV1-Support+non-Latin+characters+on+Extranet+ODC+tenant's+database
June 7  4:57 PM WESTwebRootly
Pagerduty Integrations marked the incident as resolved through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q32AZCU77F7N2P). (via Api)
June 7  5:03 PM WESTwebRootly
The retrospective document created can be checked here: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4202201197/Retrospective-SEV1-Support+non-Latin+characters+on+Extranet+ODC+tenant's+database
## 📝 Follow Up Items[View on Rootly](https://rootly.com/account/incidents/541-support-non-latin-characters-on-extranet-odc-tenant-s-database#nav-action-items)

**Summary**

**Priority**

**Status**

**Assignee**

**Links**
@Vera Branco @henrique.fonseca just FYI, this incident is really poor in context for a SEV1. Should we add as part of the requirements to open a SEV1 some kind of replication or to route to Support L2 first?trueYellowMediumtrueBlueOpen