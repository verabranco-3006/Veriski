---
title: Retrospective-SEV3-Calculating datetime in the past go's wrong
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4356342094/Retrospective-SEV3-Calculating+datetime+in+the+past+go+s+wrong
confluence_space: RKB
confluence_page_id: 4356342094
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV3-Calculating datetime in the past go's wrong

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV3

Teams:&nbsp;trueBlueData Fabric Clients

Types:&nbsp;trueBlueCustomer Escalated
#### 🕐 Timestamps
Started At:&nbsp;trueBlueAugust 13  8:17 AM WEST

Mitigated At:&nbsp;trueYellowAugust 13  1:41 PM WEST

Resolved At:&nbsp;trueGreenAugust 13  1:41 PM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/871-calculating-datetime-in-the-past-go-s-wrong)
[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3048236)

#### 🧑&zwj;🚒 Incident Rolestrue
**Commander**

Z&eacute; Perdigao

**Engineer**

Kusum Madgaonkar
#### Summary
----------------------------------------------**R&amp;D ESCALATION FORM****ISSUE DESCRIPTION AND HOW TO REPRODUCE**- Customer is trying to calculate date time in the past using CurrDateTime - 1 hours and want to use this as filter in a aggregate.
- They were doing this like with O11 by using addHours(currdatetime(), -1) (image1)Test query failed with the following error:Unable to execute query. ERROR: operator is not unique: - unknown Hint: Could not choose a best candidate operator. You might need to add explicit type casts.Condition use: If(FilerByCreateDateTime = 0, True, ExceptionHandlerLogging.CreateDatime &gt;= AddHours(CurrDateTime(),-FilterByCreatedDateTime))- Initially we believe that the customer was mixing data types
- Then we requested help from our team who shared that this might be a possible bug since when replacing the value directly, it works. (image 37 and 38)**IMPACT ON THE CUSTOMER**
No impact at this stage**TROUBLESHOOTING STEPS &amp; WORKAROUND**
We were able to find a workaround for the customer.
At this stage, we just want to understand if this is indeed a bug to proceed with the ticket closure.
If it is, please share with us the JIRA link so that we can track the fix.**TECH DATA OR ANY OTHER RELEVANT INFO**
Ring: ga
Tenant Id: eb278f09-e7e0-404a-8a7d-00946ca8d165
Tenant Prefix: npsdriven
Region: eu-central-1
Y1R.LRU.RW4.P3N.KCN.ZHR.X0W.WOU_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_Attachment(s):
Calculate1.png - https://supportoutsystems.zendesk.com/attachments/token/x2Z3xkXx6eoFbThRy6eKYxEFD/?name=Calculate1.pngimage (37).png - https://supportoutsystems.zendesk.com/attachments/token/DhJgxvMrBXSsDHlnn58ByeWy5/?name=image+%2837%29.pngimage (38).png - https://supportoutsystems.zendesk.com/attachments/token/XlWKYBLAJTCTmUzaLFffKOgQz/?name=image+%2838%29.png
## 📝 RetrospectiveinfoDetails
**Ring:** ga
**System-wide impact:**&nbsp; 
**Tenant ID:** eb278f09-e7e0-404a-8a7d-00946ca8d165
**Tenant Prefix:** npsdriven
**Routing Error Code:** N/A
**Product Area:** Phoenix::ODC Studio::Data Access and Manipulation::Aggregates::Preview Data
### Impact:### Investigation and troubleshooting findings:### Resolution:## Tasks performed during incident resolution:
&nbsp;
## Executive Summary
[Guidelines](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4144496679/Incident+Retrospectives+-+Playbook#STEP-3---Write-the-Executive-Summary)
## Root Causes 
[Guidelines](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4144496679/Incident+Retrospectives+-+Playbook#STEP-1---Perform-the-Root-Cause-Analysis)

If the customer needs formal RCA, please fill out the following field with the document URL

[Please follow these instructions and place the RCA URL in the field below.](https://docs.google.com/document/d/13rXmBsOJh73nV2D6Z17SIBGBu2HOTWty5ddsvU000JM/edit#heading=h.bqxasxszr5q)

RCA URL

&lt;Place the URL of the customer RCA here if you have created one&gt;
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/871-calculating-datetime-in-the-past-go-s-wrong)

**Date**

**Source**

**User**

**Event**
August 12  3:28 PM WESTwebRootly
created an alert via
August 12  3:28 PM WESTwebRootly
Rootly created this incident
August 12  3:28 PM WESTwebRootly
In triage date has been set to August 12  3:28 PM WEST
August 12  3:39 PM WESTwebZ&eacute; PerdigaoZ&eacute; Perdigao has been assigned as CommanderAugust 12  3:39 PM WESTwebZ&eacute; PerdigaoKusum Madgaonkar has been assigned as EngineerAugust 13  8:17 AM WESTwebKusum Madgaonkar
Incident has been started
August 13 12:22 PM WESTwebKusum MadgaonkarSend ZenDesk private comment has been set: Hello Global Support Team  After analyzing the issue we found that O11 and runtime doesn't throw typecast error as .NET driver is being used there but in case of Data preview typecaste error is thrown as JDBC driver is used here. We have created a bug https://outsystemsrd.atlassian.net/jira/software/c/projects/RDCIST/boards/1311?selectedIssue=RDCIST-2300 to fix this issue. Since we have other high priority work in this sprint will take this up in coming sprint. Also currently until this issue is resolved the workaround for the customer will be typecasting or using the literal value (not using dynamic parameter in the AddHours built in function).  Thank you.August 13 12:22 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hello Global Support Team  After analyzing the issue we found that O11 and runtime doesn't throw typecast error as .NET driver is being used there but in case of Data preview typecaste error is thrown as JDBC driver is used here. We have created a bug https://outsystemsrd.atlassian.net/jira/software/c/projects/RDCIST/boards/1311?selectedIssue=RDCIST-2300 to fix this issue. Since we have other high priority work in this sprint will take this up in coming sprint. Also currently until this issue is resolved the workaround for the customer will be typecasting or using the literal value (not using dynamic parameter in the AddHours built in function).  Thank you.
August 13 12:22 PM WESTwebRootlySend ZenDesk private comment has been unsetAugust 13 12:22 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

August 13  1:18 PM WESTwebZ&eacute; PerdigaoSend ZenDesk private comment has been set: Hi team, did the customer accept the Workaround/fix provided? Since we have provided a workaround and a ticket to fix the issue, can we close this ticket?August 13  1:18 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hi team, did the customer accept the Workaround/fix provided? Since we have provided a workaround and a ticket to fix the issue, can we close this ticket?
August 13  1:18 PM WESTwebRootlySend ZenDesk private comment has been unsetAugust 13  1:18 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

August 13  1:41 PM WESTwebRootly
The Global Support team marked this incident as closed in ZenDesk.
August 13  1:41 PM WESTwebRootly
Incident has been resolved
August 13  1:41 PM WESTwebRootlyZenDesk Event Type has been set: solved