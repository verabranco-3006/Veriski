---
title: Retrospective-SEV1-Recurring timeout during peak hours which resulting 3 modules unusable
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4283662477/Retrospective-SEV1-Recurring+timeout+during+peak+hours+which+resulting+3+modules+unusable
confluence_space: RKB
confluence_page_id: 4283662477
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV1-Recurring timeout during peak hours which resulting 3 modules unusable

## 📘 Overview
Author:&nbsp;Rootlytrue

Severity:&nbsp;SEV1Redtrue

Teams:&nbsp;Runtime Data ModelBluetrue&nbsp;SreBluetrue
#### 🕐 Timestamps
Started At:&nbsp;June 25  3:09 PM WESTBluetrue

Mitigated At:&nbsp;July 25 10:07 AM WESTYellow

Resolved At:&nbsp;July 25 10:07 AM WESTGreen
#### 🔗 Links
 [Incident Page](https://rootly.com/account/incidents/624-recurring-timeout-during-peak-hours-which-resulting-3-modules-unusable)

 [Pagerduty incident](https://outsystems.pagerduty.com/incidents/Q20VBDHWZ4SVS7)

 [Slack channel](https://slack.com/app_redirect?channel=C079L1SN4VB&amp;team=T041063TZ)

 [Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3020616)

Related Emergency RFCs:
- 
RFC-1083ef8955cb-cb21-32a7-b692-01ace42388d6System Jira  

- 
RFC-1145ef8955cb-cb21-32a7-b692-01ace42388d6System Jira  

- 
RFC-1201ef8955cb-cb21-32a7-b692-01ace42388d6System Jira

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

Mariana Cabeda
#### Summary
**ISSUE DESCRIPTION AND HOW TO REPRODUCE**

- Database overloaded during peak hours (8-12 AM UTC+1) resulting in timeouts across multiple apps.

**IMPACT ON THE CUSTOMER**

- Production.
- Customer is from Indonesia, so their working hours are typically from 2-11 AM UTC+1.
- This is mostly affecting them during the end-of-day operations - e.g. when their users synchronize day sales - resulting in timeout errors across multiple apps and general slowness.

**TROUBLESHOOTING STEPS &amp; WORKAROUND**

- Below is the number of the most common database errors found:![](https://supportoutsystems.zendesk.com/attachments/token/tYIgJpMQBu9PpsZDR3q4XmzW8/?name=image.png)- Dashboard link- Backend Runtime logs link (June 25th)- App health during these periods goes down significantly:![](https://supportoutsystems.zendesk.com/attachments/token/fUtcRdpeMQHYzUDcQLsZluiAF/?name=image.png)- We have also found this dashboard which shows they have been riding the database to the ground (CPU 100%) for the past 15 days (15 days is the cutoff):![](https://supportoutsystems.zendesk.com/attachments/token/2Oe2I3mRGO2fJMKDz2ZMqgU6j/?name=image.png)
- Now, they are questioning whether or not the infrastructure can scale and handle their traffic - while this is a tricky question, as they may have poorly optimized queries and logic, it is also difficult for us to offer assistance, considering the database side is mostly black box for Global Support.- In O11, we would benefit from Performance Insights for such incidents, which could potentially and very likely indicate underperforming queries, but in this case we have our hands tied.

- Can you help us?

**TECH DATA OR ANY OTHER RELEVANT INFO**

- A few traces from different errors (all queries to internal entities, no external connections): - ``Error opening connection to the database: The operation was canceled.\nNot retrying because connection will not succeed unless the cause of the failure is corrected``

- Trace- `Error opening connection to the database, Retrying... The connection pool has been exhausted, either raise 'Max Pool Size' (currently 20) or 'Timeout' (currently 15 seconds) in your connection string.`- Trace- `Timeout during reading attempt`- Trace_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 Retrospective### Details
**Ring:** ga
**System-wide impact:** No
**Tenant ID:** d51a905c-4f3c-4e7b-83e3-1989c87cfeff
**Tenant Prefix:** nna
**Routing Error Code:** N/A
**Product Area:** Phoenix::Application Runtime::Database access::Entities
### Impact:
Slow queries and re-occurring timeouts when accessing the customers production database mainly during peak hours.
### Resolution:
Several actions were performed such as increasing the database limits, reviewing app logic and suggesting performance improvements.
## Tasks performed during incident resolution:
**Ticket:** RFC-1083ef8955cb-cb21-32a7-b692-01ace42388d6System Jira

**Date:** 

- 
Enabled Performance Insights for the affected database, allowing for the team to have visibility over its behavior and troubleshoot the low performant queries.

- 
Runtime Data Model team and Global Support reviewed the application logic, based on the least performant queries identified though AWS Performance Insights in order to provide guidance to the customer on how to improve the performance of their application.

**Ticket:** RFC-1137ef8955cb-cb21-32a7-b692-01ace42388d6System Jira

**Date:** 

- 
Scaled up the database infrastructure, increasing the maximum ACUs from 16 to 32.

**Ticket:** RFC-1145ef8955cb-cb21-32a7-b692-01ace42388d6System Jira

**Date:** 

- 
Ran statistics on the database in order to better understand the datamodel, all relations between tables as well as sizes of tables and associated indexes.

**Ticket:** RFC-1201ef8955cb-cb21-32a7-b692-01ace42388d6System Jira

**Date:** 

- 
Requested direct access to the customer production DB in order to execute a query plan for misbehaving queries, with the goal of obtaining more information that would help us optimize the customer application.

## Executive Summary
On , an incident ([RDINC-25749](https://outsystemsrd.atlassian.net/browse/RDINC-25749)) was created for OutSystems where the customer reported database exhaustion during peak hours. In those moments, they would observe their database was unable to respond to requests. The ones that were handled, would take a long time to complete.

Investigation concluded that inefficient implementation of queries in the application were causing these problems. R&amp;D and Global Support teams worked closely during the analysis of the customer database, suggesting some improvement actions as well as scaling up the database in order to minimize the impact for this customer during peak ours in their production environment while the application was improved. 

- 
From this troubleshoot, we were able to identify several issues with queries generated by aggregates (e.g. missing indexes, usage of aggregating functions in filters). For one occasion, Studio even provided performance warnings explaining possible improvements that were ignored by the customer. Follow-up actions were created for the team to analyse how to better provide visibility for the customer of these type of problems.

This situation was redirected to Professional Services department that would then proceed with the analysis of the identified low performant queries and help the customer navigating the appropriate changes in order to enable a performant and error-free application.

However, this situation has proven and raised the team&rsquo;s awareness on some improvements that we would like to highlight and ensure the creation of the necessary action items to prevent such problems to occur in the future, such as:

- 
Global Support not having access to Performance Insights;

- 
Performance Insights not being enabled by default in all databases;

- 
Global Support is not autonomous to execute statistical queries in the databases.

For each of these items, several action items have been created and documented in the section [https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4283662477/Retrospective-SEV1-Recurring+timeout+during+peak+hours+which+resulting+3+modules+unusable#%F0%9F%93%9D-Follow-Up-Items](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4283662477/Retrospective-SEV1-Recurring+timeout+during+peak+hours+which+resulting+3+modules+unusable#%F0%9F%93%9D-Follow-Up-Items). 

As a consequence of the incident, we have determined to:

- 
Short term: temporarily increase the customer&rsquo;s database ACUs in order to ease the unavailability issues [DONE];

- 
With RFC-1137ef8955cb-cb21-32a7-b692-01ace42388d6System Jira, the database of the customer was scaled-up. This scale-up operation will be reverted as soon as we have confirmation the customer has overcame the reported issues.

- 
Medium/long term: customer application is updated to increase queries performance [BEING FOLLOWED UP WITH THE CUSTOMER, no more items pending from R&amp;D nor Global Support].

## Root Causes
In terms of root causes, we can split it into two separate topics and draw the respective root causes:
- 
Root cause of the behavior reported by the customer:
- 
Applicational inefficiencies in the queries performed;

- 
Root cause of the need for the Emergency RFCs:
- 
Global Support is unable to be autonomous troubleshooting database performance issues;

- 
Runtime Data Model team is unable to be autonomous troubleshooting database performance issues;

- 
Customer is unable to be autonomous troubleshooting database performance issues;

For each of these root causes, action items have been identified and documented in the section [https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4283662477/Retrospective-SEV1-Recurring+timeout+during+peak+hours+which+resulting+3+modules+unusable#%F0%9F%93%9D-Follow-Up-Items](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4283662477/Retrospective-SEV1-Recurring+timeout+during+peak+hours+which+resulting+3+modules+unusable#%F0%9F%93%9D-Follow-Up-Items).
## ⌛ Timeline
[View on Rootly](https://rootly.com/account/incidents/624-recurring-timeout-during-peak-hours-which-resulting-3-modules-unusable)
Detailed timeline
**Date**

**Source**

**User**

**Event**

June 25  3:08 PM WEST

web

Rootly

created an alert via

June 25  3:08 PM WEST

web

Rootly

Rootly created this incident

June 25  3:08 PM WEST

web

Rootly

In triage date has been set to June 25  3:08 PM WEST

June 25  3:08 PM WEST

web

Rootly

[Slack Channel](https://slack.com/app_redirect?channel=C079L1SN4VB&amp;team=T041063TZ) has been created

June 25  3:08 PM WEST

web

Rootly

Ring: ga System-wide impact:   Tenant ID: d51a905c-4f3c-4e7b-83e3-1989c87cfeff Tenant Prefix: nna Routing Error Code: N/A Product Area: Phoenix::Application Runtime::Database access::Entities

June 25  3:08 PM WEST

web

Rootly

[PagerDuty Incident](https://outsystems.pagerduty.com/incidents/Q20VBDHWZ4SVS7) has been created.

📧 Notified Mariana Cabeda by email.

📲 Notified Mariana Cabeda by push notification.  (via Android)

📱 Notified Mariana Cabeda by SMS.

📞 Notified Mariana Cabeda by phone.

June 25  3:08 PM WEST

web

Rootly

Mariana Cabeda has been assigned as Engineer

June 25  3:09 PM WEST

web

Rootly

Mariana Cabeda acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q20VBDHWZ4SVS7). (via Phone)

June 25  3:09 PM WEST

web

Mariana Cabeda

Incident has been started

June 25  3:09 PM WEST

web

Rootly

Pagerduty Integrations acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q20VBDHWZ4SVS7). (via Phone)

June 25  3:28 PM WEST

slack

mariana.cabeda

We are analysing some of the dashboards on database load as well as some of the long-running queries executed (using backend runtime traces). In the meantime, we'll also enable performance insights.  I'm currently creating the RFC for it.

June 25  3:54 PM WEST

slack

mariana.cabeda

Emergency RFC created and approved in order to enable Performance Insights and Enhanced Monitoring for this database: RFC-1083ef8955cb-cb21-32a7-b692-01ace42388d6System Jira  In the meantime, we'll continue to analyse with the current logs and traces to see if we can already get a sense of what is happening and report when we have more information.

June 25  4:40 PM WEST

slack

mariana.cabeda

From an initial investigation our suspicion is that we could have a non-performant query (or set of queries) being improperly created causing these performance issues. However, we will only be able to confirm this after Performance Insights is enabled which we've already [requested.In](http://requested.In) the meantime, we have quickly analysed 3 of the queries that we could see take a long time executing in the database though backend traces as well as checking their implementation using the OMLs provided in the incident. For two of them, they don't immediately see anything concerning. However, one of the queries, related with `CallPlanDetail` entity, could benefit from having an index associated with the attribute `CallplanReffNo`.Will rely this information back to Global Support in case it can be of any help while we wait for Performance Insights to be enabled.

June 25  4:42 PM WEST

web

Tiago Oliveira

Swarm has been set: SRE

June 25  4:42 PM WEST

web

Rootly

Pagerduty Integrations added Filipe Seixeira as responder in [PagerDuty](https://outsystems.pagerduty.com/incidents/Q20VBDHWZ4SVS7)

June 25  4:42 PM WEST

web

Mariana Cabeda

Send ZenDesk private comment has been set: Hello Support, From an initial investigation our suspicion is that we could have a low-performant query (or set of queries) being improperly created causing these performance issues. However, we will only be able to confirm this after Performance Insights is enabled which we've already [requested.In](http://requested.In) the meantime, we have quickly analysed 3 of the queries that we could see take a long time executing in the database though backend traces as well as checking their implementation using the OMLs provided in the incident. For two of them, they don't immediately see anything concerning. However, one of the queries, related with CallPlanDetail entity, could benefit from having an index associated with the attribute CallplanReffNo.We will reply back again once we have Performance Insights enabled.

June 25  4:42 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D: Hello Support, From an initial investigation our suspicion is that we could have a low-performant query (or set of queries) being improperly created causing these performance issues. However, we will only be able to confirm this after Performance Insights is enabled which we've already [requested.In](http://requested.In) the meantime, we have quickly analysed 3 of the queries that we could see take a long time executing in the database though backend traces as well as checking their implementation using the OMLs provided in the incident. For two of them, they don't immediately see anything concerning. However, one of the queries, related with CallPlanDetail entity, could benefit from having an index associated with the attribute CallplanReffNo.We will reply back again once we have Performance Insights enabled.

June 25  4:42 PM WEST

web

Rootly

Send ZenDesk private comment has been unset

June 25  4:42 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D: 

June 25  4:42 PM WEST

web

Rootly

Filipe Seixeira joined this [PagerDuty](https://outsystems.pagerduty.com/incidents/Q20VBDHWZ4SVS7) incident.

June 25  5:17 PM WEST

slack

mariana.cabeda

Performance Insights have been enabled, we now need to have another event of spikes and performance degradation in order to be able to troubleshoot the issue any further. Will update Global Support with this information along with details on how support can engage directly with SRE in order to autonomously continue this troubleshoot.

June 25  5:49 PM WEST

web

Mariana Cabeda

Send ZenDesk private comment has been set: Hello Support, Can you please check my last comment in the Jira issue? RDINC-25749ef8955cb-cb21-32a7-b692-01ace42388d6System Jira  you, Mariana Cabeda

June 25  5:49 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D: Hello Support, Can you please check my last comment in the Jira issue? RDINC-25749ef8955cb-cb21-32a7-b692-01ace42388d6System Jira  you, Mariana Cabeda

June 25  5:49 PM WEST

web

Rootly

Send ZenDesk private comment has been unset

June 25  5:49 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D: 

June 25  7:50 PM WEST

web

Tiago Oliveira

Send ZenDesk private comment has been set: Hi Support, Can you also ask for the &quot;NNA Report Service&quot; app OML? At this point, most of the queries running are coming from a timer in this other app.Cheers, Tiago Oliveira

June 25  7:50 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D: Hi Support, Can you also ask for the &quot;NNA Report Service&quot; app OML? At this point, most of the queries running are coming from a timer in this other app.Cheers, Tiago Oliveira

June 25  7:50 PM WEST

web

Rootly

Send ZenDesk private comment has been unset

June 25  7:50 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D: 

June 25  8:17 PM WEST

web

Tiago Oliveira

Send ZenDesk private comment has been set: Hi Support,We have add a possible cause, but that we cannot validate until usage goes back up. It may be worth sharing with the customer, as they know better their app, to check if the suggestion is doable, and if there might be operations with similar patterns during peak-hours.Please check RDINC-25749ef8955cb-cb21-32a7-b692-01ace42388d6System Jira , Tiago Oliveira

June 25  8:17 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D: Hi Support,We have add a possible cause, but that we cannot validate until usage goes back up. It may be worth sharing with the customer, as they know better their app, to check if the suggestion is doable, and if there might be operations with similar patterns during peak-hours.Please check RDINC-25749ef8955cb-cb21-32a7-b692-01ace42388d6System Jira , Tiago Oliveira

June 25  8:17 PM WEST

web

Rootly

Send ZenDesk private comment has been unset

June 25  8:17 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D: 

June 26 10:25 AM WEST

web

Rootly

Zendesk Private Comment has been set: ----------------------------------------------**Update to R&amp;D** Hi team,The errors just started for today, as you can see from this link.Database average CPU is at 100% since 9.50 UTC+1, as we can also see here.Can we check Performance Insights now to see the greater offenders?Thanks in advance! Jo&atilde;o Neves__

June 26 10:25 AM WEST

web

Rootly

NEW MESSAGE FROM GLOBAL SUPPORT: 

June 26 11:22 AM WEST

web

Mariana Cabeda

Send ZenDesk private comment has been set: Hello Support, Can you check my last comment in the Jira issue? RDINC-25749ef8955cb-cb21-32a7-b692-01ace42388d6System Jira  you, Mariana Cabeda

June 26 11:22 AM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D: Hello Support, Can you check my last comment in the Jira issue? RDINC-25749ef8955cb-cb21-32a7-b692-01ace42388d6System Jira  you, Mariana Cabeda

June 26 11:22 AM WEST

web

Rootly

Send ZenDesk private comment has been unset

June 26 11:22 AM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D: 

June 28  1:18 PM WEST

web

Mariana Cabeda

Send ZenDesk private comment has been set: Hello Support, Can you please check my last comment in the Jira issue? RDINC-25749ef8955cb-cb21-32a7-b692-01ace42388d6System Jira  you, Mariana Cabeda

June 28  1:18 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D: Hello Support, Can you please check my last comment in the Jira issue? RDINC-25749ef8955cb-cb21-32a7-b692-01ace42388d6System Jira  you, Mariana Cabeda

June 28  1:18 PM WEST

web

Rootly

Send ZenDesk private comment has been unset

June 28  1:19 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D: 

July 2 12:10 PM WEST

web

Rootly

Zendesk Private Comment has been changed to: ----------------------------------------------**Update to R&amp;D** Hello!The field team met with the client today to discuss the possibility of increasing the DB from the current 16 ACUs to 32.From the feedback we have received from the client, the improvements have already been made to just one app, and they are continuing their efforts to ensure that the improvements we suggest are also replicated for the other apps. On top of this, the client also showed his commitment during today's meeting that he would do this and send these improvements to PRD still this week. At the same time, the client expects the number of users to triple (3x more).We've also had the opportunity to review DB's current metrics over the last 24 and the scenario continues to be worrying (although expectable, considering that improvements will still be made over this week).Taking into account the sensitive (escalated) situation of this client, combined with the pressure we currently have on DB, the field team asked us (approved by Paulo Garrudo) to proceed with the expansion from the current 16 ACUs to 32. As there is currently no procedure for doing this on our part, we are turning to you to analyze and proceed with it.If I can help in any way, please don't hesitate.We look forward to hearing from you.S&eacute;rgio Pinho_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_

July 2 12:10 PM WEST

web

Rootly

NEW MESSAGE FROM GLOBAL SUPPORT: 

July 2 12:11 PM WEST

web

Rootly

Zendesk Private Comment has been changed to: ------------------------------------------------ This notification was sent from Zendesk Support ticket #3020616 to all linked JIRA issues by S&eacute;rgio Pinho. --**Update to R&amp;D** Hello!The field team met with the client today to discuss the possibility of increasing the DB from the current 16 ACUs to 32.From the feedback we have received from the client, the improvements have already been made to just one app, and they are continuing their efforts to ensure that the improvements we suggest are also replicated for the other apps. On top of this, the client also showed his commitment during today's meeting that he would do this and send these improvements to PRD still this week. At the same time, the client expects the number of users to triple (3x more).We've also had the opportunity to review DB's current metrics over the last 24 and the scenario continues to be worrying (although expectable, considering that improvements will still be made over this week).Taking into account the sensitive (escalated) situation of this client, combined with the pressure we currently have on DB, the field team asked us (approved by Paulo Garrudo) to proceed with the expansion from the current 16 ACUs to 32. As there is currently no procedure for doing this on our part, we are turning to you to analyze and proceed with it.If I can help in any way, please don't hesitate.We look forward to hearing from you.S&eacute;rgio Pinho_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_

July 2 12:11 PM WEST

web

Rootly

NEW MESSAGE FROM GLOBAL SUPPORT: 

July 2  7:23 PM WEST

web

Tiago Oliveira

Send ZenDesk private comment has been set: **Hi team, **Letting you know that the override to 32ACUs max has been applied successfully.Cheers, Tiago Oliveira

July 2  7:23 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D: **Hi team, **Letting you know that the override to 32ACUs max has been applied successfully.Cheers, Tiago Oliveira

July 2  7:23 PM WEST

web

Rootly

Send ZenDesk private comment has been unset

July 2  7:23 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D: 

July 3 12:55 PM WEST

web

Rootly

Zendesk Private Comment has been changed to: ----------------------------------------------**Update to R&amp;D**- Following yesterday's improvements of database resources (increase in ACUs) we can see positive effects:- No signs of errors like before, even during peak hours (below includes peak from July 2nd for comparison):![]([https://supportoutsystems.zendesk.com/attachments/token/SUzovMsomyN7GbF1m08L8qUOV/?name=image.png](https://supportoutsystems.zendesk.com/attachments/token/SUzovMsomyN7GbF1m08L8qUOV/?name=image.png))- Database ACU consumption and CPU utilization also show a big improvement (you can see the ACU limit was raised and the CPU utilization went significantly):![]([https://supportoutsystems.zendesk.com/attachments/token/p1a59tudyUCqLZQsopRiB5zoq/?name=image.png](https://supportoutsystems.zendesk.com/attachments/token/p1a59tudyUCqLZQsopRiB5zoq/?name=image.png)) ![]([https://supportoutsystems.zendesk.com/attachments/token/Kz5cdPMGbLG8uyOiRxr62ZPuW/?name=image.png](https://supportoutsystems.zendesk.com/attachments/token/Kz5cdPMGbLG8uyOiRxr62ZPuW/?name=image.png))- However, this matched with the suggested improvements to the queries (use of **ToUpper/ToLower** functions), so we cannot confirm based on these graphs alone whether those improvements had significant impacts.- Can **Backend Runtime** help us again by checking Performance Insights to see if the top queries have changed?_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_

July 3 12:55 PM WEST

web

Rootly

NEW MESSAGE FROM GLOBAL SUPPORT: 

July 3  7:08 PM WEST

web

Tiago Oliveira

Swarm has been unset: SRE

July 3  7:08 PM WEST

web

Tiago Oliveira

Swarm has been set: SRE

July 3  7:08 PM WEST

web

Rootly

Pagerduty Integrations added Jason Crews as responder in [PagerDuty](https://outsystems.pagerduty.com/incidents/Q20VBDHWZ4SVS7)

July 3  7:11 PM WEST

web

Rootly

Tiago Oliveira added Pedro Miguel Cardoso as responder in [PagerDuty](https://outsystems.pagerduty.com/incidents/Q20VBDHWZ4SVS7)

July 3  7:12 PM WEST

web

Rootly

Pedro Miguel Cardoso joined this [PagerDuty](https://outsystems.pagerduty.com/incidents/Q20VBDHWZ4SVS7) incident.

July 3  7:12 PM WEST

web

Rootly

Pedro Miguel Cardoso acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q20VBDHWZ4SVS7). (via Phone)

July 3  7:16 PM WEST

web

Rootly

Jason Crews joined this [PagerDuty](https://outsystems.pagerduty.com/incidents/Q20VBDHWZ4SVS7) incident.

July 4 11:24 AM WEST

web

Rootly

Zendesk Private Comment has been changed to: ----------------------------------------------**Update to R&amp;D**Hi team,Thanks for the provided updates.We still need your help, though: how can we decipher this information and provide concrete suggestions to the customer?Below are our worries:- We can see the top queries, but we have no way to pinpoint which aggregates they correspond to.- In O11, we had the option to include the origin of the query as a comment: [https://success.outsystems.com/documentation/11/monitoring_and_troubleshooting_apps/trace_executed_queries_back_to_your_outsystems_applications/-](https://success.outsystems.com/documentation/11/monitoring_and_troubleshooting_apps/trace_executed_queries_back_to_your_outsystems_applications/-) Could this be an option in ODC in the future? It would definitely help for this type of case.- Without execution plans, how can we infer what the actions should be for a given query? E.g. what index to create/drop, or what else could be improved?- From the output files provided by Pedro Cardoso, please bear in mind that we have close to zero experience with PostgreSQL databases, considering our current level of access (none) and that this is only our first case regarding database performance.- In other words, we're not sure what conclusions we should take from those files, if any.- For example, for the index overlap suggestion, it's not something we should suggest lightly without concrete backing evidence, since removing indexes at this point not only takes development and rollout time from the customer, but it can also potentially decrease performance if we are not sure what we are removing - while we bought some time with the recent ACUs increase, we are still riding very close to the limit, so we could be risking another outage.- [https://outsystems.grafana.net/d/I6ZUsIF4z/rds-database-metrics-instances?orgId=1&amp;var-datasource=-XaQwHL4k&amp;var-region=ap-southeast-1&amp;var-dbinstanceidentifiers=env-d0c3e7f9-5de9-4090-a422-2cdf0e1e84ec-az1&amp;var-period=1m&amp;from=1720076400000&amp;to=1720090799000_](https://outsystems.grafana.net/d/I6ZUsIF4z/rds-database-metrics-instances?orgId=1&amp;var-datasource=-XaQwHL4k&amp;var-region=ap-southeast-1&amp;var-dbinstanceidentifiers=env-d0c3e7f9-5de9-4090-a422-2cdf0e1e84ec-az1&amp;var-period=1m&amp;from=1720076400000&amp;to=1720090799000_)&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_

July 4 11:24 AM WEST

web

Rootly

NEW MESSAGE FROM GLOBAL SUPPORT: 

July 14 12:38 PM WEST

web

Rootly

Jason Crews acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q20VBDHWZ4SVS7). (via Phone)

July 15 10:07 AM WEST

web

Rootly

ZenDesk Event Type has been set: solved

July 15 10:07 AM WEST

web

Rootly

The Global Support team marked this incident as closed in ZenDesk.

July 15 11:24 AM WEST

web

Ant&oacute;nio Caeiro

Incident has been resolved

July 15 11:24 AM WEST

web

Ant&oacute;nio Caeiro

Impact has been set: slow  queries on client database

July 15 11:24 AM WEST

web

Ant&oacute;nio Caeiro

Resolution has been set: several actions performed, like changing ACU, review current index, review app logic

July 15 11:24 AM WEST

web

Rootly

Pagerduty Integrations marked the incident as resolved through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q20VBDHWZ4SVS7)
## 📝 Follow Up Items
[View on Rootly](https://rootly.com/account/incidents/624-recurring-timeout-during-peak-hours-which-resulting-3-modules-unusable#nav-action-items)

**Summary**

**Root Cause item**

**Jira Ticket**

**Assignee**

**Links**

Customer is helped though OutSystems (by Professional Services) analysing the application and suggesting performance improvements.

1.a)

N/A

N/A

Global Support should be able to Swarm with SRE.

2.a)

RSA-519ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

 

[https://outsystems.slack.com/archives/C079L1SN4VB/p1719511328160049](https://outsystems.slack.com/archives/C079L1SN4VB/p1719511328160049)

Global support should be able to map physical table names to logical entity names. RDMMS could store the logical table name in the table comments so that it could be fetched from the DB.

2.a)

RPLAT-2645ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

[https://outsystems.slack.com/archives/C079L1SN4VB/p1720109972148899](https://outsystems.slack.com/archives/C079L1SN4VB/p1720109972148899) 

Grant necessary permissions to Global Support team to access Performance Insights, Data API and S3 files for ODC accounts.

This will allow Global Support to autonomously troubleshoot these type of issues without the need to request any information from SRE nor R&amp;D.

2.a)

RPLAT-2649ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

 

[https://outsystems.slack.com/archives/C079L1SN4VB/p1719511326114309](https://outsystems.slack.com/archives/C079L1SN4VB/p1719511326114309)  

Create runbooks explaining how to troubleshoot a performance issue for an ODC application in order to share it with Global Support team.

2.a)

RPLAT-2597ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

Have query plans automatically enabled/logged for slow queries, allowing for faster troubleshoot.

This allows both R&amp;D and Global Support to not require further RFCs to run query plans.

2.a)

2.b)

RPLAT-2625ef8955cb-cb21-32a7-b692-01ace42388d6System Jira

 RPLAT-2594ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

[https://outsystems.slack.com/archives/C079L1SN4VB/p1720110265879489](https://outsystems.slack.com/archives/C079L1SN4VB/p1720110265879489) 

Have Performance Insights enabled in all databases by default.

This allows both R&amp;D and Global Support to not require further RFCs to enable performance insights.

2.a)

2.b)

RPLAT-2568ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

RPLAT-2581ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

RPLAT-2636ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

 

[https://outsystems.slack.com/archives/C079L1SN4VB/p1719332454915479](https://outsystems.slack.com/archives/C079L1SN4VB/p1719332454915479) 

Enable Data API in all runtime databases.

2.a)

2.b)

RPLAT-2595ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

Customer is able to have visibility over the database state and pressure to troubleshoot low performant queries.

2.c)

RPLAT-2670ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

 

Studio warnings that suggested performance improvements ignored by customer. We should analyse how to provide higher visibility of these warnings and also evaluate which other improvements can be suggested.

2.c)

RPLAT-2671ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

 

RDINC-25749ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

Emergency RFC approval didn&rsquo;t trigger SRE.

N/A

RDPEN-541ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

 

[https://outsystems.slack.com/archives/C079L1SN4VB/p1719330174488899](https://outsystems.slack.com/archives/C079L1SN4VB/p1719330174488899) 

In order to complete the ERFC, delete the `pg_admin` pod from the cluster as per [this comment](https://outsystemsrd.atlassian.net/browse/RFC-1201?focusedCommentId=1159748).

N/A

RFC-1201ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

 / SRE

In order to complete the ERFC, revert the database scaleup by  as per [this comment](https://outsystemsrd.atlassian.net/browse/RFC-1137?focusedCommentId=1164612).

N/A

RFC-1137ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

 / SRE

Disable performance insights and enhanced monitoring for this database.

N/A

N/A, we will not pursue disabling performance insights in this database since we will want to have it enabled by default for all environments.

N/A

[https://outsystems.slack.com/archives/C079L1SN4VB/p1719332399401309](https://outsystems.slack.com/archives/C079L1SN4VB/p1719332399401309)