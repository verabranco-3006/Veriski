---
title: Retrospective-SEV2-While deploying core application getting 'An error has occurred while executing SQL scripts'
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4224352416/Retrospective-SEV2-While+deploying+core+application+getting+An+error+has+occurred+while+executing+SQL+scripts
confluence_space: RKB
confluence_page_id: 4224352416
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV2-While deploying core application getting 'An error has occurred while executing SQL scripts'

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV2

Teams:&nbsp;trueBlueNeo Platform Runtime Data Model
#### 🕐 Timestamps
Started At:&nbsp;trueBlueJune 12  5:02 AM WEST

Mitigated At:&nbsp;trueYellowJune 12 11:00 AM WEST

Resolved At:&nbsp;trueGreenJune 12 11:00 AM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/555-while-deploying-core-application-getting-an-error-has-occurred-while-executing-sql-scripts)
[Pagerduty incident](https://outsystems.pagerduty.com/incidents/Q0DL4158E2KY56)

[Slack channel](https://slack.com/app_redirect?channel=C077PJQE6BD&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3020943)

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

Shashank Mahadev
#### Summary
----------------------------------------------**CONSIDERATIONS BEFORE PERFORMING THE ESCALATION TO R&amp;D (MANDATORY)**
None of the below points should be overlooked. Failure to do so may imply unnecessary effort.* * *
Ensure the ticket has been **categorized**, otherwise, the R&amp;D escalation will go unnoticed and not be worked on!**1.** For **Incidents**, the **IMAX** was consulted **beforehand** on which:- No incident models were found for the reported symptoms **OR**
- The incident model did not solve the issue **OR**
- The next step indicated in the Incident Model is an escalation to R&amp;D.
**2.** For **Questions**, the ChatODC on the **Slack channel** didn't return an acceptable answer.
**3.** Any other requests that explicitly indicate an R&amp;D escalation is needed.
**4**. **Incident impact assessment** was based on the **prioritization scoring matrix**.* * ***R&amp;D ESCALATION FORM**
Section comments can be removed for R&amp;D easier interpretation.**ISSUE DESCRIPTION AND HOW TO REPRODUCE**
The customer is not able to deploy an app from DEV to Production stage.- Name of APP:- **HTStudio_Core**- This is the error in the Deployment logs- ![](https://supportoutsystems.zendesk.com/attachments/token/T61Wdrr2wPyz7TskxVOGTv4P5/?name=image.png)An error has occurred while executing SQL scripts: SQL script execution error. update or delete on table &quot;MasterType&quot; violates foreign key constraint &quot;osfrk_alurleniubw_maste_5ezj5v3lqv_ul2_maste_5ezjje1qowcc81_mad&quot; on table &quot;Master&quot; (OS-RDBE-GEN-50010)An error has occurred while migrating the database (OS-DPL-50204)**IMPACT ON THE CUSTOMER**- High.
- The customer can't deploy an application from DEV to production due to some changes in a static entity causing a foreign key constraint.**TROUBLESHOOTING STEPS &amp; WORKAROUND**- Looking at the Deployment logs- ![](https://supportoutsystems.zendesk.com/attachments/token/oHHLlm8l4gt6k6nr9UntSEmrd/?name=image.png)- It seems that the error was happening since atleast Revision 266 of the HTStudio_Core app. This error occurred on May 8th- ![](https://supportoutsystems.zendesk.com/attachments/token/HB8e2snsFzmmvmJb7SRds0Wbm/?name=image.png)May 08, 2024, 07:43:38 PM&nbsp;An error has occurred while executing SQL scripts: SQL script execution error. update or delete on table &quot;MasterType&quot; violates foreign key constraint &quot;osfrk_alurleniubw_maste_5ezj5v3lqv_ul2_maste_5ezjje1qowcc81_mad&quot; on table &quot;Master&quot; (OS-RDBE-GEN-50010)&nbsp;May 08, 2024, 07:43:38 PM&nbsp;An error has occurred while migrating the database (OS-DPL-50204)- The previous successful deployment of HTStudio_Core app to Production was Revision 244 deployed on April 29th.- After that, every time they tried to deploy this app, they are getting the same error message as above.- I proceeded to open ODC Studio to compare the Revision 244 (successful deployed to Prod) and Revision 266 (Not able to deploy to Prod)- I can see this difference- ![](https://supportoutsystems.zen...
## 📝 RetrospectiveinfoDetails
**Ring:** ga
**System-wide impact:**&nbsp; No
**Tenant ID:** 8aa96ba2-4fcb-42b3-83e8-b9f5b1d84e3c
**Tenant Prefix:** citiustech
**Routing Error Code:** OS-RDBE
**Product Area:** -
### Impact:
Customer unable to deploy application to production stage, with an error executing database scripts. The customer wants to go live with this production soon.
### Investigation and troubleshooting findings:
- 
- Internal Update **

It seems that the changes the customer is trying to apply to production directly conflict with the data that is present there at the moment. I don't see any product defect at the moment and the reported seems to be the expected behaviour. Customer is requesting help further analysing what data is being violated by this constraint.

In order to do that, we can suggest the customer to create and deploy a new screen, only available for their internal team (so authorization needs to be setup in that regard) which can give them visibility of the records currently present in the Master entity which could be affected by the change being currently deployed. This should be done before doing any change to the application's model such as change the delete rule protection, since that could end up deleting also data on Master entity which could not be what the customer wants.

Since it seems that there are many revisions in between the current application in Dev versus Production, and in order to unblock their deployment, we can suggest as a workaround that the customer doesn't delete this record at the moment, and deploy a revision of the application still with the record CUseCaseTypeOfSolution in the static entity MasterType. This way, all other changes can be pushed to production while the customer better analyses their data in that environment.

Something for us to analyse internaly and improve is the error message. We have already a few tickets regarding improving error messages with the logical names for the tables and foreign keys. This will help customers be more autonomous troubleshooting these types of incidents. Will need to better analyse this specific message later on and link action items on our side to improve this.

- 
- Next Steps **

- Update Global Support with the workaround suggestion.

### Resolution:
With the provided guidance from R&amp;D, customer was able to find the offending data and is now able to proceed with the deployment of the application.

Jira ticket marked as solved.
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/555-while-deploying-core-application-getting-an-error-has-occurred-while-executing-sql-scripts)

**Date**

**Source**

**User**

**Event**
June 12  4:40 AM WESTwebRootly
created an alert via
June 12  4:40 AM WESTwebRootly
Rootly created this incident
June 12  4:40 AM WESTwebRootly
In triage date has been set to June 12  4:40 AM WEST
June 12  4:40 AM WESTwebRootly[Slack Channel](https://slack.com/app_redirect?channel=C077PJQE6BD&amp;team=T041063TZ) has been createdJune 12  4:40 AM WESTwebRootly[PagerDuty Incident](https://outsystems.pagerduty.com/incidents/Q0DL4158E2KY56) has been created.
📲 Notified Shashank. K.B by push notification.  (via iPhone)June 12  4:40 AM WESTwebRootly
Ring: ga
System-wide impact:  
Tenant ID: 8aa96ba2-4fcb-42b3-83e8-b9f5b1d84e3c
Tenant Prefix: citiustech
Routing Error Code: OS-RDBE
Product Area: -
June 12  4:40 AM WESTwebRootlyShashank Mahadev has been assigned as EngineerJune 12  4:43 AM WESTwebRootly
Shashank. K.B acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q0DL4158E2KY56). (via Website)
June 12  5:02 AM WESTwebShashank Mahadev
Incident has been started
June 12  5:02 AM WESTwebRootly
Pagerduty Integrations acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q0DL4158E2KY56). (via Website)
June 12  5:06 AM WESTslackmariana.cabeda
Taking a first look into the incident it seems to be an expected error when the change is violating a FK constraint. From the incident description it seems that the changes being applied are indeed related with a static entity that has a FK to a table with a protect rule, which seems to be the case.
Currently checking the previous communication between support and the customer to understand what was already discussed and attempted.
June 12  5:21 AM WESTslackmariana.cabeda**Internal note**
It seems that global support was able to see, through the application changes between revisions, that a record with a relationship to the main entity has been deleted. This can cause the error observed during deployment and in order to allow the customer to better understand the impacts of any change, we would recommend for the customer to analyse this record's relationship with the Master entity.
In order to see the data in production, the customer can create and deploy a change in their application, giving their team access to a back-office screen (only available to their development team) where they can create a table (which could already be filtered by the deleted record) to give them visibility on the data that is being violated by this new application deployment.
This way, the customer can evaluate whether they can safely delete that data or if they need to adjust their application.A first workaround for them to be able to get this revision to production could also be reverting just the change that deletes this record and pushing the remainder changes to production.
Will now update the ticket with this information to global support.June 12  5:28 AM WESTslackmariana.cabeda
Note to be analysed later on with internal team helping us setup rootly: I was not added to this channel automatically, we need to review why that happened.
June 12  5:46 AM WESTwebMariana Cabeda
Summary has been changed to 

&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;**CONSIDERATIONS BEFORE PERFORMING THE ESCALATION TO R&amp;D (MANDATORY)**
None of the below points should be overlooked. Failure to do so may imply unnecessary effort.

Ensure the ticket has been **categorized**, otherwise, the R&amp;D escalation will go unnoticed and not be worked on!
&nbsp;&nbsp;
&nbsp;&nbsp;**1.** For **Incidents**, the **IMAX** was consulted **beforehand** on which:

- No incident models were found for the reported symptoms **OR**&nbsp;&nbsp;
- The incident model did not solve the issue **OR**&nbsp;&nbsp;
- The next step indicated in the Incident Model is an escalation to R&amp;D.
**2.** For **Questions**, the ChatODC on the **Slack channel** didn't return an acceptable answer.
**3.** Any other requests that explicitly indicate an R&amp;D escalation is needed.
**4**. **Incident impact assessment** was based on the **prioritization scoring matrix**.

&nbsp;&nbsp;**R&amp;D ESCALATION FORM**
Section comments can be removed for R&amp;D easier interpretation.
&nbsp;&nbsp;
&nbsp;&nbsp;**ISSUE DESCRIPTION AND HOW TO REPRODUCE**
The customer is not able to deploy an app from DEV to Production stage.

- &nbsp;&nbsp;
Name of APP:- **HTStudio_Core**&nbsp;&nbsp;
&nbsp;&nbsp;
- &nbsp;&nbsp;
This is the error in the Deployment logs

- &nbsp;&nbsp;&nbsp;&nbsp;

An error has occurred while executing SQL scripts: SQL script execution error. update or delete on table &quot;MasterType&quot; violates foreign key constraint &quot;osfrk_alurleniubw_maste_5ezj5v3lqv_ul2_maste_5ezjje1qowcc81_mad&quot; on table &quot;Master&quot; (OS-RDBE-GEN-50010)An error has occurred while migrating the database (OS-DPL-50204)
&nbsp;&nbsp;

&nbsp;&nbsp;**IMPACT ON THE CUSTOMER**&nbsp;&nbsp;

- High.
- The customer can't deploy an application from DEV to production due to some changes in a static entity causing a foreign key constraint.

&nbsp;&nbsp;**TROUBLESHOOTING STEPS &amp; WORKAROUND**&nbsp;&nbsp;

- &nbsp;&nbsp;
Looking at the Deployment logs

- &nbsp;&nbsp;&nbsp;&nbsp;
- It seems that the error was happening since atleast Revision 266 of the HTStudio_Core app. This error occurred on May 8th
- &nbsp;&nbsp;&nbsp;&nbsp;

May 08, 2024, 07:43:38 PM&nbsp;An error has occurred while executing SQL scripts: SQL script execution error. update or delete on table &quot;MasterType&quot; violates foreign key constraint &quot;osfrk_alurleniubw_maste_5ezj5v3lqv_ul2_maste_5ezjje1qowcc81_mad&quot; on table &quot;Master&quot; (OS-RDBE-GEN-50010)&nbsp;May 08, 2024, 07:43:38 PM&nbsp;An error has occurred while migrating the database (OS-DPL-50204)
&nbsp;&nbsp;
- &nbsp;&nbsp;
The previous successful deployment of HTStudio_Core app to Production was Revision 244 deployed on April 29th.

- After that, every time they tried to deploy this app, they are getting the same error message as above.

&nbsp;&nbsp;
- &nbsp;&nbsp;
I proceeded to open ODC Studio to compare the Revision 244 (successful deployed to Prod) and Revision 266 (Not able to deploy to Prod)

- I can see this difference
- ![]([https://supportoutsystems.zen](https://supportoutsystems.zen)...

&nbsp;&nbsp;

&nbsp;&nbsp;June 12  5:46 AM WESTwebMariana Cabeda
Teams has been removed: SRE
June 12  5:46 AM WESTwebMariana CabedaSystem-wide impact has been set: NoJune 12  5:46 AM WESTwebMariana CabedaImpact has been set: Customer unable to deploy application to production stage, with an error executing database scripts. The customer wants to go live with this production soon.June 12  5:46 AM WESTwebMariana CabedaInvestigation and troubleshooting findings has been set: ** Internal Update **It seems that the changes the customer is trying to apply to production directly conflict with the data that is present there at the moment. I don't see any product defect at the moment and the reported seems to be the expected behaviour. Customer is requesting help further analysing what data is being violated by this constraint.In order to do that, we can suggest the customer to create and deploy a new screen, only available for their internal team (so authorization needs to be setup in that regard) which can give them visibility of the records currently present in the Master entity which could be affected by the change being currently deployed. This should be done before doing any change to the application's model such as change the delete rule protection, since that could end up deleting also data on Master entity which could not be what the customer wants.Since it seems that there are many revisions in between the current application in Dev versus Production, and in order to unblock their deployment, we can suggest as a workaround that the customer doesn't delete this record at the moment, and deploy a revision of the application still with the record CUseCaseTypeOfSolution in the static entity MasterType. This way, all other changes can be pushed to production while the customer better analyses their data in that environment.Something for us to analyse internaly and improve is the error message. We have already a few tickets regarding improving error messages with the logical names for the tables and foreign keys. This will help customers be more autonomous troubleshooting these types of incidents. Will need to better analyse this specific message later on and link action items on our side to improve this.** Next Steps **
- Update Global Support with the workaround suggestion.June 12  6:02 AM WESTwebMariana CabedaSend ZenDesk private comment has been set: Hello Support, thanks for reaching out to us with this issue.I&rsquo;ve been analysing the information shared as well as previous communication with the customer and It seems that the changes the customer is trying to apply to production directly conflict with the data that is present there at the moment. We don't see any product defect at the moment and what is reported seems to be the expected behaviour. In order to allow the customer to better understand what data is being violated, I suggest that a new screen is developed and deployed, serving as a back-office access for the team to access data of the Master entity in order to provide visibility on the data that is currently being violated by this constraint in production. This screen should only be available and visible to the internal team for this troubleshoot.As for a workaround that will make the customer able to deploy to production, and considering there are many revisions that are trying to be pushed at once, we suggest for the customer to defer deleting the static record CUseCaseTypeOfSolution in the static entity MasterType. If this is indeed the change that is blocking the deployment to production, keeping this record will unblock the customer while the investigation by the customer proceeds in order to analyse if any data should be removed in the Master table.On our side, we will create an action item to better improve this error message in the future. We would like to provide visibility on the actual names of the entities being affected in order to allow customers to be more autonomous troubleshooting these types of incidents. As soon as that action item is created, it will be linked in the Jira ticket incident.Feel free to reach back out in case there are any more questions.Thank you,
Mariana CabedaJune 12  6:02 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hello Support, thanks for reaching out to us with this issue.I&rsquo;ve been analysing the information shared as well as previous communication with the customer and It seems that the changes the customer is trying to apply to production directly conflict with the data that is present there at the moment. We don't see any product defect at the moment and what is reported seems to be the expected behaviour. In order to allow the customer to better understand what data is being violated, I suggest that a new screen is developed and deployed, serving as a back-office access for the team to access data of the Master entity in order to provide visibility on the data that is currently being violated by this constraint in production. This screen should only be available and visible to the internal team for this troubleshoot.As for a workaround that will make the customer able to deploy to production, and considering there are many revisions that are trying to be pushed at once, we suggest for the customer to defer deleting the static record CUseCaseTypeOfSolution in the static entity MasterType. If this is indeed the change that is blocking the deployment to production, keeping this record will unblock the customer while the investigation by the customer proceeds in order to analyse if any data should be removed in the Master table.On our side, we will create an action item to better improve this error message in the future. We would like to provide visibility on the actual names of the entities being affected in order to allow customers to be more autonomous troubleshooting these types of incidents. As soon as that action item is created, it will be linked in the Jira ticket incident.Feel free to reach back out in case there are any more questions.Thank you,
Mariana Cabeda
June 12  6:02 AM WESTwebRootlySend ZenDesk private comment has been unsetJune 12  6:02 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

June 12  6:04 AM WESTslackmariana.cabeda
A message was sent to Global Support with a workaround proposal as well as more information on how the customer can further analyse which data is violating this constraint.
Will now move the Jira ticket to &quot;Waiting for Customer&quot; status.
June 12 10:36 AM WESTwebHenrique Fonseca
Teams has been added: Neo Platform RuntimeDataModel
June 12 11:00 AM WESTwebMariana Cabeda
Incident has been resolved
June 12 11:00 AM WESTwebMariana CabedaResolution has been set: With the provided guidance from R&amp;D, customer was able to find the offending data and is now able to proceed with the deployment of the application.
Jira ticket marked as solved.June 12 11:00 AM WESTwebRootly
The retrospective document created can be checked here: 
June 12 11:00 AM WESTwebRootly
Pagerduty Integrations marked the incident as resolved through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q0DL4158E2KY56). (via Api)
June 12  2:08 PM WESTwebRootlyZenDesk Event Type has been set: solvedJune 12  2:08 PM WESTwebRootly
The Global Support team marked this incident as closed in ZenDesk.
June 18  1:07 PM WESTwebRootly
The retrospective document created can be checked here: 
## 📝 Follow Up Items[View on Rootly](https://rootly.com/account/incidents/555-while-deploying-core-application-getting-an-error-has-occurred-while-executing-sql-scripts#nav-action-items)

**Summary**

**Priority**

**Status**

**Assignee**

**Links**
Note to be analysed later on with internal team helping us setup rootly: I was not added to this channel automatically, we need to review why that happened.trueYellowMediumtrueBlueOpenAction item to runtime data model team &bull; Something for us to analyse internaly and improve is the error message. We have already a few tickets regarding improving error messages with the logical names for the tables and foreign keys. This will help customers be more autonomous troubleshooting these types of incidents. Will need to better analyse this specific message later on and link action items on our side to improve this.trueYellowMediumtrueBlueOpen