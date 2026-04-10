---
title: Retrospective-SEV1-Production Data Corrupted!
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4349558916/Retrospective-SEV1-Production+Data+Corrupted
confluence_space: RKB
confluence_page_id: 4349558916
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV1-Production Data Corrupted!

## 📘 Overview
Author:&nbsp;Rootlytrue

Severity:&nbsp;SEV1Redtrue

Teams:&nbsp;Runtime Data ModelBluetrue&nbsp;SreBluetrue
#### 🕐 Timestamps
Started At:&nbsp;August 9 10:53 AM WESTBluetrue

Mitigated At:&nbsp;August 9 10:54 AM WESTYellowtrue

Resolved At:&nbsp;August 9 10:54 AM WESTGreentrue
#### 🔗 Links
 [Incident Page](https://rootly.com/account/incidents/789-production-data-corrupted-33788658-0268-47c0-be53-911421dc9270)

 [Pagerduty incident](https://outsystems.pagerduty.com/incidents/Q2TDTVT329TT2V)

 [Slack channel](https://slack.com/app_redirect?channel=C07FQ01UGCQ&amp;team=T041063TZ)

 [Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3043478)

Related Emergency RFCs:
- 
RFC-1274ef8955cb-cb21-32a7-b692-01ace42388d6System Jira

- 
RFC-1273ef8955cb-cb21-32a7-b692-01ace42388d6System Jira

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

Joel Filipe Carvalho
#### Summary
**CONSIDERATIONS BEFORE PERFORMING THE ESCALATION TO R&amp;D (MANDATORY)**

None of the below points should be overlooked. Failure to do so may imply unnecessary effort.Ensure the ticket has been **categorized**, otherwise, the R&amp;D escalation will go unnoticed and not be worked on! **1.** For **Incidents**, the **IMAX** was consulted **beforehand** on which:- No incident models were found for the reported symptoms **OR** - The incident model did not solve the issue **OR** - The next step indicated in the Incident Model is an escalation to R&amp;D.**2.** For **Questions**, the ChatODC on the **Slack channel** didn't return an acceptable answer.**3.** Any other requests that explicitly indicate an R&amp;D escalation is needed.**4**. **Incident impact assessment** was based on the **prioritization scoring matrix**.

**R&amp;D ESCALATION FORM**

- Since the only people able to do a restore and analyse if it's necessary is R&amp;D:- https://outsystemsrd.atlassian.net/wiki/spaces/CloudKB/pages/4168122403/ODC+Database+Restore- For RCA, we cannot commit to a resolution but we can try to provide possibilities- Once again, only R&amp;D can provide this, this is due to our limited access as support

**ISSUE DESCRIPTION AND HOW TO REPRODUCE**

The JCDAIR Web application in Production has encountered a critical issue following the deployment of a new feature that added sorting by datetime on the Overtime page. Specifically, this deployment led to an unexpected data corruption where all data recorded for July was incorrectly overridden to reference a specific set of data from May. This erroneous data replacement has compromised the integrity of the records To reproduce the issue, the following steps were undertaken in the Production environment:1. A new sorting feature on the datetime field was implemented and deployed on the Overtime page 2. Upon deployment, users observed that all July entries were replaced with identical data from MayThis problem does not appear to manifest in the Development environment, indicating it may be specific to Production data or configurations ![](https://supportoutsystems.zendesk.com/attachments/token/v04U7F5J9HciUXNodZZTJsc6T/?name=image.png)![](https://supportoutsystems.zendesk.com/attachments/token/2ULzIY9fMeWAMDGmQ2Gup8gpu/?name=image.png) The customer is now requesting for a database restoration to be performed and eventually an investigation on why the behaviour occured:- **JCDAIR Web** - **today 1 Aug 10.20am UTC +8 

**IMPACT ON THE CUSTOMER**

The problem occurs in the Production stage and is ongoing. It affects over 20 users who rely on accurate overtime records, impacting business operations by preventing the recording of overtime correctly. The incident is critical as it directly affects operational data integrity 

**TROUBLESHOOTING STEPS &amp; WORKAROUND**

Initial analysis suggests the issue arose from a recent deployment that included sorting on a datetime field. No immediate workaround has been successful in resolving the data corruption. The incident was discussed briefly with internal support but not escalated to an R&amp;D team yet, no RDINC too

**TECH DATA OR ANY OTHER RELEVANT INFO**

Ring: ga Tenant Id: f87de3f3-46ca-4061-801a-b13c3a51796b _&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 Retrospective### Details
**Ring:** ga
**System-wide impact:**&nbsp; No
**Tenant ID:** f87de3f3-46ca-4061-801a-b13c3a51796b
**Tenant Prefix:** jcdecaux-sg
**Routing Error Code:** N/A
**Product Area:** Phoenix::Application Runtime::Database access
### Impact:
A single customer reported data corruption in the production Runtime database after a new deployment.
### Investigation and troubleshooting findings:
It was discovered that the data was corrupted by an error in the application logic and was unrelated with any Product defect.
### Resolution:
Database restore was performed to the customer. The corruption of the data was caused by applicational logic which the customer agreed to then improve.
## Tasks performed during incident resolution:
**Ticket:** RFC-1274ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Date:** 

- 
Analysis of the change that caused the alleged data corruption. The database scripts for this application deployment were retrieved where we were able to confirm that no platform change had caused such behaviour.

**Ticket:** RFC-1273ef8955cb-cb21-32a7-b692-01ace42388d6System Jira  

**Date:** 

- 
Following the customer request, R&amp;D and SRE proceeded with the database restoration to the requested time.

## Executive Summary
On  4:13AM, an Incident ([#789](https://rootly.com/account/incidents/789-production-data-corrupted-33788658-0268-47c0-be53-911421dc9270)) was opened for OutSystems where the customer reported that after a simple change to production, their data for a specific month had been overridden and, as such, they were requesting clarification on why that occurred along with a database restoration to a time previous to that deployment.

- 
Another Incident ([RDINC-27935](https://outsystemsrd.atlassian.net/browse/RDINC-27935)) was created to handle exclusively the database restore. It was later merged into the original ticket where both the root cause of the corruption was handled along with the database restore.

The incident was later escalated to SRE (through Rootly) and R&amp;D (through Jira/Pager Duty) though two separate tools, on  8:05 AM.

At that time, Runtime Data Model team started the analysis on the issue (despite it being assigned to SRE team on Rootly). The first identified action was to validate if indeed the new deployment could have caused undesired changes (confirm if the Platform had generated code incorrectly) and for that an ERFC ([RFC-1274](https://outsystemsrd.atlassian.net/browse/RFC-1274)) was created, to fetch the generated database scripts. From there, we were able to confirm that nothing was wrongly generated and applied into the database. The only changes were the ones the customer did want to promote.

After further investigation between Runtime Data Model, SRE and Global Support, we were able to understand that the problem resided in the logic on the application implementation and no Product defect caused the data corruption. Still, the customer required for the data to be restored and with SRE we proceeded with that execution on , 5:21 PM ([RFC-1273](https://outsystemsrd.atlassian.net/browse/RFC-1273)). At this time, the incident was mitigated.

On  the customer confirmed the database restore procedure had concluded successfully and agreed to pursue the application changes suggested by Global Support in order to not corrupt the data again.
## Root Causes 
After the analysis of the incident, it has been determined that the root cause of the perceived data corruption was due to an applicational bug which caused the data to be incorrectly stored in the database.
## ⌛ Timeline
[View on Rootly](https://rootly.com/account/incidents/789-production-data-corrupted-33788658-0268-47c0-be53-911421dc9270)
Detailed timeline (it is quite extensive hence the collapsible item)
**Date**

**Source**

**User**

**Event**

August 1  4:13 AM WEST

Zendesk

Zendesk

Incident ([#789](https://rootly.com/account/incidents/789-production-data-corrupted-33788658-0268-47c0-be53-911421dc9270)) was opened by the Customer

August 1  8:28 AM WEST

web

Rootly

created an alert via

August 1  8:28 AM WEST

web

Rootly

Rootly created this incident

August 1  8:28 AM WEST

web

Rootly

In triage date has been set to August 1  8:28 AM WEST

August 1  8:29 AM WEST

web

Rootly

[Slack Channel](https://slack.com/app_redirect?channel=C07FQ01UGCQ&amp;team=T041063TZ) has been created

August 1  8:29 AM WEST

web

Rootly

Ring: ga System-wide impact:   Tenant ID: f87de3f3-46ca-4061-801a-b13c3a51796b Tenant Prefix: jcdecaux-sg Routing Error Code: N/A Product Area: Phoenix::Application Runtime::Database access

August 1  8:29 AM WEST

web

Rootly

[PagerDuty Incident](https://outsystems.pagerduty.com/incidents/Q2TDTVT329TT2V) has been created.

📧 Notified Balasundaram Natarajan by email.

&nbsp;&nbsp;

📞 Notified Balasundaram Natarajan by phone.

&nbsp;&nbsp;

📱 Notified Balasundaram Natarajan by SMS.

August 1  8:29 AM WEST

web

Rootly

Balasundaram Natarajan has been assigned as Engineer

August 1  8:29 AM WEST

web

Rootly

Balasundaram Natarajan acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q2TDTVT329TT2V). (via Website)

August 1  8:40 AM WEST

web

Balasundaram Natarajan

Incident has been started

August 1  8:40 AM WEST

web

Rootly

Pagerduty Integrations acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q2TDTVT329TT2V). (via Website)

August 1  8:51 AM WEST

web

Rootly

Pagerduty Integrations added Pedro Miguel Cardoso as responder in [PagerDuty](https://outsystems.pagerduty.com/incidents/Q2TDTVT329TT2V)

August 1  8:52 AM WEST

web

Rootly

Pedro Miguel Cardoso joined this [PagerDuty](https://outsystems.pagerduty.com/incidents/Q2TDTVT329TT2V) incident.

August 1 10:03 AM WEST

web

Rootly

Pedro Miguel Cardoso has been assigned by Pagerduty Integrations through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q2TDTVT329TT2V)

August 1 10:05 AM WEST

web

Rootly

Pedro Miguel Cardoso acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q2TDTVT329TT2V). (via Website)

August 1 10:22 AM WEST

web

Hugo Araujo

Teams has been added: [RuntimeDataModel](https://outsystemsrd.atlassian.net/account/teams/runtimedatamodel/status)

August 1 10:44 AM WEST

web

Balasundaram Natarajan

Summary has been changed to 

&nbsp;&nbsp;`&nbsp;&nbsp;`

`&nbsp;&nbsp;CONSIDERATIONS BEFORE PERFORMING THE ESCALATION TO R&amp;D (MANDATORY)`
`None of the below points should be overlooked. Failure to do so may imply unnecessary effort.`

`&nbsp;&nbsp;`

`Ensure the ticket has been categorized, otherwise, the R&amp;D escalation will go unnoticed and not be worked on! `
- 
`For Incidents, the IMAX was consulted beforehand on which:`

- 
`No incident models were found for the reported symptoms OR&nbsp;&nbsp;`

- 
`The incident model did not solve the issue OR&nbsp;&nbsp;`

- 
`The next step indicated in the Incident Model is an escalation to R&amp;D.2. For Questions, the ChatODC on the Slack channel didn't return an acceptable answer.3. Any other requests that explicitly indicate an R&amp;D escalation is needed.4. Incident impact assessment was based on the prioritization scoring matrix.`

`&nbsp;&nbsp;R&amp;D ESCALATION FORM&nbsp;&nbsp;`

- 
`&nbsp;&nbsp;`

`Since the only people able to do a restore and analyse if it's necessary is R&amp;D:`

- 
`&nbsp;&nbsp;`ODC Database Restore `&nbsp;&nbsp;`

`&nbsp;&nbsp;`

- 
`&nbsp;&nbsp;`

`For RCA, we cannot commit to a resolution but we can try to provide possibilities`

- 
`Once again, only R&amp;D can provide this, this is due to our limited access as support`

`&nbsp;&nbsp;`

`&nbsp;&nbsp;ISSUE DESCRIPTION AND HOW TO REPRODUCE`
`The JCDAIR Web application in Production has encountered a critical issue following the deployment of a new feature that added sorting by datetime on the Overtime page. Specifically, this deployment led to an unexpected data corruption where all data recorded for July was incorrectly overridden to reference a specific set of data from May. `
`This erroneous data replacement has compromised the integrity of the records `
`To reproduce the issue, the following steps were undertaken in the Production environment:`
- 
`A new sorting feature on the datetime field was implemented and deployed on the Overtime page`

- 
`Upon deployment, users observed that all July entries were replaced with identical data from May`

`This problem does not appear to manifest in the Development environment, indicating it may be specific to Production data or configurations `
`&nbsp;&nbsp;`

`The customer is now requesting for a database restoration to be performed and eventually an investigation on why the behaviour occured:`

- 
`&nbsp;&nbsp;JCDAIR Web&nbsp;&nbsp;`

- 
`*today 1 Aug 10.20am UTC +8 *&nbsp;&nbsp;`

`&nbsp;&nbsp;IMPACT ON THE CUSTOMER`
`The problem occurs in the Production stage and is ongoing. It affects over 20 users who rely on accurate overtime records, impacting business operations by preventing the recording of overtime correctly. `
`The incident is critical as it directly affects operational data integrity `
`&nbsp;&nbsp;TROUBLESHOOTING STEPS &amp; WORKAROUND`
`Initial analysis suggests the issue arose from a recent deployment that included sorting on a datetime field. No immediate workaround has been successful in resolving the data corruption. The incident was discussed briefly with internal support but not escalated to an R&amp;D team yet, no RDINC too `
`&nbsp;&nbsp;TECH DATA OR ANY OTHER RELEVANT INFO`
`Ring: ga `
`Tenant Id: f87de3f3-46ca-4061-801a-b13c3a51796b `
`&nbsp;&nbsp;&lt;! do not remove this line, this will be used to the trigger Technical Support::Send to R&amp;D - ODC #trigger_send_to_r&amp;d_odc !&gt;&nbsp;&nbsp;`

`&nbsp;&nbsp;`&nbsp;&nbsp;

August 1 10:44 AM WEST

web

Balasundaram Natarajan

System-wide impact has been set: No

August 1 10:44 AM WEST

web

Balasundaram Natarajan

Impact has been set: its a single customer issue due to the change in their application . not sure if the db still corrupted

August 1 10:44 AM WEST

web

Balasundaram Natarajan

Investigation and troubleshooting findings has been set: its a single customer issue due to the change in their application

August 1 11:06 AM WEST

slack

acacio.nova

To leave it in writing: if we end up going forward with the database rollback, I want to be the reviewer of that RFC.

August 1 11:11 AM WEST

web

Hugo Araujo

Send ZenDesk private comment has been set: Hey team,  Thanks for participating in the discussion.  As we had the chance to share with you in our Zoom call, these should be the next steps:*   On the engineering side, we are currently validating the SQL scripts created for each production-published application version.*   We can also validate the options we have in case a Database Restore is necessary. *   On the Global Support side, what we expect is a new assessment of the Incident, more precisely, what exactly is occurring and what are the customer expectations.*   We strongly suspect that what is being reported didn't happen, and it needs to be validated.*   At the same time, we need to understand what are the customer expectations regarding the next steps. The Data corruption happened a few hours ago already and doing a total restore means they would lose data, for instance.Besides that, it would be interesting to check the OML files to understand if the customer might have some kind of logic that is updating record information and, eventually, causing this situation to occur.  Thanks in advance

August 1 11:11 AM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D: Hey team,  Thanks for participating in the discussion.  As we had the chance to share with you in our Zoom call, these should be the next steps:*   On the engineering side, we are currently validating the SQL scripts created for each production-published application version.*   We can also validate the options we have in case a Database Restore is necessary. *   On the Global Support side, what we expect is a new assessment of the Incident, more precisely, what exactly is occurring and what are the customer expectations.*   We strongly suspect that what is being reported didn't happen, and it needs to be validated.*   At the same time, we need to understand what are the customer expectations regarding the next steps. The Data corruption happened a few hours ago already and doing a total restore means they would lose data, for instance.Besides that, it would be interesting to check the OML files to understand if the customer might have some kind of logic that is updating record information and, eventually, causing this situation to occur.  Thanks in advance

August 1 11:11 AM WEST

web

Rootly

Send ZenDesk private comment has been unset

August 1 11:11 AM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D: 

August 1 11:15 AM WEST

slack

balasundaram.natarajan

Retrieve SQL Scripts from S3 RFC-1274ef8955cb-cb21-32a7-b692-01ace42388d6System Jira  is done

August 1 11:16 AM WEST

slack

acacio.nova

I don't see a basic question in the support case: *did you try to rollback the app to the version before the &quot;whatever sort&quot; was introduced? @joao.pita.neves*

August 1  1:35 PM WEST

web

Rootly

Zendesk Private Comment has been set: ----------------------------------------------**Update to R&amp;D** Hi team,Official update here:- For context, there are two entities, **Attendance** and **Overtime**, where **Overtime** references **Attendance** twice.- Attendance:![](https://supportoutsystems.zendesk.com/attachments/token/XVxZS7ded2JbzX9EJ6A6RXkid/?name=image.png)- Overtime:![](https://supportoutsystems.zendesk.com/attachments/token/xQu5j4aspQai9NifijhNxm8wf/?name=image.png) - After discussing further with the customer, we have concluded that the problem is not that the date times have changed on the Attendance attribute, but rather the **AttendanceId** references in the **Overtime** entity, thus affecting only the **GetOvertimes** aggregate result.![]([https://supportoutsystems.zendesk.com/attachments/token/TUnFlLvxHwl0z6eJsiZzoPXWM/?name=image.png](https://supportoutsystems.zendesk.com/attachments/token/TUnFlLvxHwl0z6eJsiZzoPXWM/?name=image.png)) - However, none of these references are ever updated. In fact, the only updates to the **Overtime** entity only change the **OvertimeStatusId** attribute, keeping all other attributes the same:![](https://supportoutsystems.zendesk.com/attachments/token/43aaddxIYWqIl40BoS0OZA24U/?name=image.png)![]([https://supportoutsystems.zendesk.com/attachments/token/joijDBRDsV6DWlo65WP3Q56Wr/?name=image.png](https://supportoutsystems.zendesk.com/attachments/token/joijDBRDsV6DWlo65WP3Q56Wr/?name=image.png))Now, after further analyzing, we found something interesting that could explain this behavior (but we would have to test it):- The second update above comes from the **UpdateOvertimeApproval** server action, which is triggered from a client-side form update:![](https://supportoutsystems.zendesk.com/attachments/token/wnEs0y6kXBXaKGV5PdJiHVIwE/?name=image.png) - Now, these inputs for the Attendance In/Out are both disabled, but they are fed by another aggregate **GetAttendances** which has no filters or sorts, and no relationship with the selected **Overtime** record:![](https://supportoutsystems.zendesk.com/attachments/token/p23Rs9BRePBr8eSY9yqtyGV6J/?name=image.png) - My question is, when this form opens, which **Attendance** is shown on the dropdown? Since it has no connection to the selected Overtime, it should be a random attendance, right?![]([https://supportoutsystems.zendesk.com/attachments/token/ELYAgnBt7iFkg6wsnYm8R9akJ/?name=image.png](https://supportoutsystems.zendesk.com/attachments/token/ELYAgnBt7iFkg6wsnYm8R9akJ/?name=image.png)) - And then, even if it is not changing explicitly (since it's disabled), does its value automatically carry over to the SelectedOvertime.AttendanceInId variable?- If it does, then this is likely the cause of the changes - we found a lot of recent uses of this action:![](https://supportoutsystems.zendesk.com/attachments/token/KRuUiF9Vdid8xeQnjkwfp71Ua/?name=image.png)* * *With that said, even after explaining all of this to the customer, the potential impacts of the current application logic, the potential impacts of the database restore (data loss), the customer still wants to pursue the database restore.- They changed the desired time of the database restore (minus 20 minutes): **August 1st, 2 AM UTC.**On my side, I will attempt to test this suspicion in a sample app and will update later.Thanks for your cooperation, everyone.Jo&atilde;o Neves__

August 1  1:35 PM WEST

web

Rootly

NEW MESSAGE FROM GLOBAL SUPPORT: ----------------------------------------------**Update to R&amp;D** Hi team,Official update here:- For context, there are two entities, **Attendance** and **Overtime**, where **Overtime** references **Attendance** twice.- Attendance:![](https://supportoutsystems.zendesk.com/attachments/token/XVxZS7ded2JbzX9EJ6A6RXkid/?name=image.png)- Overtime:![](https://supportoutsystems.zendesk.com/attachments/token/xQu5j4aspQai9NifijhNxm8wf/?name=image.png) - After discussing further with the customer, we have concluded that the problem is not that the date times have changed on the Attendance attribute, but rather the **AttendanceId** references in the **Overtime** entity, thus affecting only the **GetOvertimes** aggregate result.![]([https://supportoutsystems.zendesk.com/attachments/token/TUnFlLvxHwl0z6eJsiZzoPXWM/?name=image.png](https://supportoutsystems.zendesk.com/attachments/token/TUnFlLvxHwl0z6eJsiZzoPXWM/?name=image.png)) - However, none of these references are ever updated. In fact, the only updates to the **Overtime** entity only change the **OvertimeStatusId** attribute, keeping all other attributes the same:![](https://supportoutsystems.zendesk.com/attachments/token/43aaddxIYWqIl40BoS0OZA24U/?name=image.png)![]([https://supportoutsystems.zendesk.com/attachments/token/joijDBRDsV6DWlo65WP3Q56Wr/?name=image.png](https://supportoutsystems.zendesk.com/attachments/token/joijDBRDsV6DWlo65WP3Q56Wr/?name=image.png))Now, after further analyzing, we found something interesting that could explain this behavior (but we would have to test it):- The second update above comes from the **UpdateOvertimeApproval** server action, which is triggered from a client-side form update:![](https://supportoutsystems.zendesk.com/attachments/token/wnEs0y6kXBXaKGV5PdJiHVIwE/?name=image.png) - Now, these inputs for the Attendance In/Out are both disabled, but they are fed by another aggregate **GetAttendances** which has no filters or sorts, and no relationship with the selected **Overtime** record:![](https://supportoutsystems.zendesk.com/attachments/token/p23Rs9BRePBr8eSY9yqtyGV6J/?name=image.png) - My question is, when this form opens, which **Attendance** is shown on the dropdown? Since it has no connection to the selected Overtime, it should be a random attendance, right?![]([https://supportoutsystems.zendesk.com/attachments/token/ELYAgnBt7iFkg6wsnYm8R9akJ/?name=image.png](https://supportoutsystems.zendesk.com/attachments/token/ELYAgnBt7iFkg6wsnYm8R9akJ/?name=image.png)) - And then, even if it is not changing explicitly (since it's disabled), does its value automatically carry over to the SelectedOvertime.AttendanceInId variable?- If it does, then this is likely the cause of the changes - we found a lot of recent uses of this action:![](https://supportoutsystems.zendesk.com/attachments/token/KRuUiF9Vdid8xeQnjkwfp71Ua/?name=image.png)* * *With that said, even after explaining all of this to the customer, the potential impacts of the current application logic, the potential impacts of the database restore (data loss), the customer still wants to pursue the database restore.- They changed the desired time of the database restore (minus 20 minutes): **August 1st, 2 AM UTC.**On my side, I will attempt to test this suspicion in a sample app and will update later.Thanks for your cooperation, everyone.Jo&atilde;o Neves__

August 1  2:23 PM WEST

web

Henrique Fonseca

Joel Filipe Carvalho has been assigned as Engineer

August 1  2:30 PM WEST

slack

tiago.oliveira

RFC-1273ef8955cb-cb21-32a7-b692-01ace42388d6System Jira  RFC for the Restore Execution Approved, waiting of SRE to start Execution

August 1  2:45 PM WEST

web

Rootly

Zendesk Private Comment has been changed to: ----------------------------------------------**Update to R&amp;D** Hi team,Just regarding my hypothesis, I have tested in a sample app and could not replicate - the form assumes the correct values; so it's still unknown what caused what.That leaves us with no further items other than standing by for the database restore.Thanks again, team.Jo&atilde;o Neves_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_

August 1  2:45 PM WEST

web

Rootly

NEW MESSAGE FROM GLOBAL SUPPORT: ----------------------------------------------**Update to R&amp;D** Hi team,Just regarding my hypothesis, I have tested in a sample app and could not replicate - the form assumes the correct values; so it's still unknown what caused what.That leaves us with no further items other than standing by for the database restore.Thanks again, team.Jo&atilde;o Neves__

August 1  3:27 PM WEST

slack

tiago.oliveira

SRE started the execution of the restore.

August 1  4:08 PM WEST

slack

tiago.oliveira

Restore of Database completed. We will now move ahead with deploying the correct backend of each app.

August 1  4:28 PM WEST

slack

tiago.oliveira

Restore of Applications Backend revisions completed. Proceeding to validate if no errors are occurring.

August 1  5:13 PM WEST

slack

tiago.oliveira

Terraform plan shows no signs of DB recreation, only expected changes (labels and maintenance window). Enabling reconcile.

August 1  5:18 PM WEST

slack

tiago.oliveira

Terraform reconcilation enabled, and successfully completed. Restore process is completed.

August 1  5:19 PM WEST

slack

Dhruv Desai

RFC where there is all execution details : RFC-1273ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

August 1  5:22 PM WEST

slack

tiago.oliveira

@joao.pita.neves &bull; Restoration was completed at `Aug 1st 2024, 3:28:00PM UTC`; &bull; Validations completed at `Aug 1st 2024, 4:19:00PM UTC`; Can you reach out to the customer, for them to validate? 1. Database was restored to `Aug 1st 2024, 2:00:00AM UTC` 2. 1 App (`JCDAIRWeb`) was deployed to the version matching at `Aug 1st 2024, 2:00:00AM UTC`

August 2  1:34 PM WEST

web

Rootly

The Global Support team marked this incident as closed in ZenDesk.

August 2  1:34 PM WEST

web

Rootly

Incident has been resolved

August 2  1:34 PM WEST

web

Rootly

ZenDesk Event Type has been set: solved

August 2  1:37 PM WEST

web

Rootly

Zendesk Private Comment has been changed to: ----------------------------------------------**Update to R&amp;D** Hi team,For reference, spoke with the customer on the phone and they were not in the best health, so they haven't yet had time to correct the data or anything to figure out if they still need our assistance or not.Nevertheless, the database restore is all good.We agreed, as suggested by them, to close the ticket and they would reach back out to us if they still require assistance.Thanks for everything and have a nice weekend! Jo&atilde;o Neves_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_

August 2  1:37 PM WEST

web

Rootly

NEW MESSAGE FROM GLOBAL SUPPORT: ----------------------------------------------**Update to R&amp;D** Hi team,For reference, spoke with the customer on the phone and they were not in the best health, so they haven't yet had time to correct the data or anything to figure out if they still need our assistance or not.Nevertheless, the database restore is all good.We agreed, as suggested by them, to close the ticket and they would reach back out to us if they still require assistance.Thanks for everything and have a nice weekend! Jo&atilde;o Neves__

August 2  2:41 PM WEST

slack

pedro.miguel.cardoso

The secrets for the restored environment were rotated

August 9 10:53 AM WEST

web

Miguel Afonso

Incident has been started

August 9 10:53 AM WEST

web

Rootly

Pagerduty Integrations acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q2TDTVT329TT2V). (via Website)

August 9 10:54 AM WEST

web

Mariana Cabeda

Incident has been resolved

August 9 10:54 AM WEST

web

Mariana Cabeda

Resolution has been set: Database restore was performed to the customer. The corruption of the data was caused by applicational logic.
## 📝 Follow Up Items
[View on Rootly](https://rootly.com/account/incidents/789-production-data-corrupted-33788658-0268-47c0-be53-911421dc9270?tab=follow_ups)

Considering no product defects have been identified over the course of this incident, the next follow-up items are related with detected procedural issues which we would like to highlight and ensure action items are created and properly executed.

**Summary**

**Jira Ticket**

**Assignee**

**Links**

Long time for incident to be escalated from Global Support. Considering the customer requested a database restore, every time between the initial request and the escalation moment would be time for the database to continue to evolve and that data to be lost.

- 
This would be important regardless of the problem being in the application or a Product defect.

N/A

 

ODC Database Restore 

Three tools showed different teams assigned:
- 
Rootly (official tool): SRE assigned;

- 
Jira: assigned to Backend Runtime team;

- 
PagerDuty: assigned to Runtime Data model team (after Backend Runtime re-assigned it).

This is the result of having multiple overlapping tools. There is an ongoing discussion on how to go forward. Right now this is what 's planned: RDR-247ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

 

Confusion in the process to automatically assign SEV1 incidents to SRE before engaging with R&amp;D team:

- 
SRE seemed to be assigned to more than 1 SEV1 ticket at a time, which doesn&rsquo;t seem correct;

- 
Runtime Data Model team was aiding SRE to troubleshoot the issue and was requested to open an RFC ticket (which should have been opened by SRE to start the troubleshoot, since it was the team assigned).

RDPEN-575ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

 

Include the secret rotation as part of the database restore automated runbook.

RDR-248ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

SRE

[https://outsystems.slack.com/archives/C07FQ01UGCQ/p1722606192293879?thread_ts=1722530612.458289&amp;cid=C07FQ01UGCQ](https://outsystems.slack.com/archives/C07FQ01UGCQ/p1722606192293879?thread_ts=1722530612.458289&amp;cid=C07FQ01UGCQ) 

Delete database snapshot and instance after the restore.

RPLAT-2656ef8955cb-cb21-32a7-b692-01ace42388d6System Jira

 

[https://outsystems.slack.com/archives/C07FQ01UGCQ/p1722529542799499?thread_ts=1722529191.129049&amp;cid=C07FQ01UGCQ](https://outsystems.slack.com/archives/C07FQ01UGCQ/p1722529542799499?thread_ts=1722529191.129049&amp;cid=C07FQ01UGCQ) 

Align the SEV1 Definition with the classification of a DR.
If an incident is classified as SEV1, we should consider it a Disaster and always move ahead with the restore (which in this case took several hours to decide).
If we do not consider it a Disaster, we should not consider it a SEV1.

RPLAT-2747ef8955cb-cb21-32a7-b692-01ace42388d6System Jira