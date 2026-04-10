---
title: Retrospective-SEV3-Issue when using the Count from an aggregate
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4349264048/Retrospective-SEV3-Issue+when+using+the+Count+from+an+aggregate
confluence_space: RKB
confluence_page_id: 4349264048
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV3-Issue when using the Count from an aggregate

## 📘 Overview
Author:&nbsp;trueGreyRootly

Services:&nbsp;trueBlueData Fabric Engine Services

Severity:&nbsp;trueRedSEV3

Teams:&nbsp;trueBlueData Fabric Engine
#### 🕐 Timestamps
Started At:&nbsp;trueBlueJuly 1 12:16 PM WEST

Mitigated At:&nbsp;trueYellowJuly 1 12:16 PM WEST

Resolved At:&nbsp;trueGreenAugust 9 12:57 PM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/633-issue-when-using-the-count-from-an-aggregate)
[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3025018)

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

Bruno Coelho

**Commander**

Vasco Gomes
#### Summary
----------------------------------------------**ISSUE DESCRIPTION AND HOW TO REPRODUCE**- Data mashup aggregate fails when Count is referenced (e.g. in a Pagination block):OS-BERT-60407 - [500] Could not execute the specified command: Error while preparing statement [SELECT COUNT(1) FROM (SELECT 1 as cnt FROM (&quot;runtime&quot;.&quot;postr_xveupwmmlxpugji21lyozw17&quot; &quot;ENPOSTransaction&quot; Inner JOIN &quot;28ae4f8f-34a6-4f04-8c4e-393b7fc179c6&quot;.&quot;OSUSR_4FH_VENUEPATRON&quot; &quot;ENVenuePatron&quot; ON (&quot;ENPOSTransaction&quot;.&quot;o11venuepatronid&quot; = &quot;ENVenuePatron&quot;.&quot;ID&quot;)) WHERE (&quot;ENPOSTransaction&quot;.&quot;o11venueid&quot; = ?) AND ((&quot;ENPOSTransaction&quot;.&quot;tradedate&quot; &gt;= ?) AND (&quot;ENPOSTransaction&quot;.&quot;tradedate&quot; &lt;= ?)) AND (&quot;ENVenuePatron&quot;.&quot;ISACTIVE&quot; = 1) GROUP BY &quot;ENPOSTransaction&quot;.&quot;tradedate&quot;, &quot;ENPOSTransaction&quot;.&quot;membershipid&quot;, &quot;ENPOSTransaction&quot;.&quot;o11venuepatronid&quot;) cnt]**IMPACT ON THE CUSTOMER**- Development.
- Test query in ODC Studio works without issues, but they claim not being able to continue testing out their solution without being able to use the Count.**TROUBLESHOOTING STEPS &amp; WORKAROUND**- Customer has implemented the same aggregate in two screens, one with pagination (fails), the other without pagination (success).- Including the OML in attachment for review if needed.- Not working (pagination is used):![](https://supportoutsystems.zendesk.com/attachments/token/302B0UFFNSSBYzha61V3YhC7m/?name=image.png)- Working (pagination is not used):![](https://supportoutsystems.zendesk.com/attachments/token/UquNjE2KO9lLFr6qAEiMpWjRq/?name=image.png)
- Confirmed it only happens for one of the aggregates:![](https://supportoutsystems.zendesk.com/attachments/token/23C7tOCGLzT9vAPGr4nxrxP5Y/?name=image.png)
- Inspecting a successful trace vs. a non-successful trace, I can only see a difference between the queries - the order of the GROUP BY:- Non-working:![](https://supportoutsystems.zendesk.com/attachments/token/N4s5MfssjUo47laF7HLjmVmT9/?name=image.png)- Working:![](https://supportoutsystems.zendesk.com/attachments/token/brA972q3Aed081qLirOfrBYtB/?name=image.png)- For easier visibility:![](https://supportoutsystems.zendesk.com/attachments/token/OWLXxO0H0tMWzMfKwyI0pE1be/?name=image.png)- The corresponding traces on our side:- Error trace- Successful trace
- Looking at the error trace on our side, we can see this inner exception:Unable to implement EnumerableAggregate(group=[{}], EXPR$0=[COUNT()]): rowcount = 1.0, cumulative cost = {3750073.4562499993 rows, 15682.057968750001 cpu, 1.0 io}, id = 2645150&nbsp; EnumerableMergeJoin(condition=[=($2, $3)], joinType=[semi]): rowcount = 2238.3337500000002, cumulative cost = {3750072.4562499993 rows, 13163.9325 cpu, 1.0 io}, id = 2645148&nbsp; JdbcToEnumerableConverter: rowcount = 2238.3337500000002, cumulative cost = {692308.33875 rows, 0.0 cpu, 0.0 io}, id = 2645137&nbsp; JdbcSort(sort0=[$2], dir0=[ASC]): rowcount = 2238.3337500000002, cumulative cost = {690070.005 rows, 0.0 cpu, 0.0 io}, id = 2645135&nbsp; JdbcAggregate(group=[{6, 9, 14}]): rowcount = 2238.3337500000002, cumulative cost = {687831.67125 rows, 0.0 cpu, 0.0 io}, id = 2645133&nbsp; JdbcFilter(condition=[AND(IS NOT NULL($14), =($5, ?0), &gt;=($6, ?1), &lt;=($6, ?2))]): rowcount = 22383.3375, cumulative cost = {685593.3375 rows, 0.0 cpu, 0.0 io}, id = 2645131&nbsp; JdbcTableScan(table=[[runtime, postr_xveupwmmlxpugji21lyozw17]]): rowcount = 663210.0, cumulative cost = {663210.0 rows, 0.0 cpu, 0.0 io}, id = 2617350&nbsp; JdbcToEnumerableConverter: rowcount = 10925.598750000001, cumulative cost = {3055525.7837499995 rows, 0.0 cpu, 0.0 io}, id = 2645146&nbsp; JdbcSort(sort0=[$0], dir0=[ASC]): rowcount = 10925.598750000001, cumulative cost = {3044600.1849999996 rows, 0.0 cpu, 0.0 io}, id = 2645144&nbsp; JdbcAggregate(group=[{0}]): rowcount = 10925.598750000001, cumulative cost = {3033674.5862499997 rows, 0.0 cpu, 0.0 io}, id = 2645142&nbsp; JdbcFilter(condition=[AND(=($48, true), OR(=($cor1000.o11venuepatronid, $0), =($cor1001.o11venuepatronid, $0), =($cor1002.o11venuepatronid, $0), =($cor1003.o11venuepatronid, $0), =($cor1004.o11venuepatronid, $0), =($cor1005.o11venuepatronid, $0), =($cor1006.o11venuepatronid, $0), =($cor1007.o11venuepatronid, $0), =($cor1008.o11venuepatronid, $0), =($cor1009.o11venuepatronid, $0), =($cor1010.o11venuepatronid, $0), =($cor1011.o11venuepatronid, $0), =($cor1012.o11venuepatronid, $0), =($cor1013.o11venuepatronid, $0), =($cor1014.o11venuepatronid, $0), =($cor1015.o11venuepatronid, $0), =($cor1016.o11venuepatronid, $0), =($cor1017.o11venuepatronid, $0), =($cor1018.o11venuepatronid, $0), =($cor1019.o11venuepatronid, $0), =($cor1020.o11venuepatronid, $0), =($cor1021.o11venuepatronid, $0), =($cor1022.o11venuepatronid, $0), =($cor1023.o11venuepatronid, $0), =($cor1024.o11venuepatronid, $0), =($cor1025.o11venuepatronid, $0), =($cor1026.o11venuepatronid, $0), =($cor1027.o11venuepatronid, $0), =($cor1028.o11venuepatronid, $0), =($cor1029.o11venuepatronid, $0), =($cor1030.o11venuepatronid, $0), =($cor1031.o11venuepatronid, $0), =($cor1032.o11venuepatronid, $0), =($cor1033.o11venuepatronid, $0), =($cor1034.o11venuepatronid, $0), =($cor1035.o11venuepatronid, $0), =($cor1036.o11venuepatronid, $0), =($cor1037.o11venuepatronid, $0), =($cor1038.o11venuepatronid, $0), =($cor1039.o11venuepatronid, $0), =($cor1040.o11venuepatronid, $0), =($cor1041.o11venuepatronid, $0), =($cor1042.o11venuepatronid, $0), =($cor1043.o11venuepatronid, $0), =($cor1044.o11venuepatronid, $0), =($cor1045.o11venuepatronid, $0), =($cor1046.o11venuepatronid, $0), =($cor1047.o11venuepatronid, $0), =($cor1048.o11venuepatronid, $0), =($cor1049.o11venuepatronid, $0), =($cor1050.o11venuepatronid, $0), =($cor1051.o11venuepatronid, $0), =($cor1052.o11venuepatronid, $0), =($cor1053.o11venuepatronid, $0), =($cor1054.o11venuepatronid, $0), =($cor1055.o11venuepatronid, $0), =($cor1056.o11venuepatronid, $0), =($cor1057.o11venuepatronid, $0), =($cor1058.o11venuepatronid, $0), =($cor1059.o11venuepatronid, $0), =($cor1060.o11venuepatronid, $0), =($cor1061.o11venuepatronid, $0), =($cor1062.o11venuepatronid, $0), =($cor1063.o11venuepatronid, $0), =($cor1064.o11venuepatronid, $0), =($cor1065.o11venuepatronid, $0), =($cor1066.o11venuepatronid, $0), =($cor1067.o11venuepatronid, $0), =($cor1068.o11venuepatronid, $0), =($cor1069.o11venuepatronid, $0), =($cor1070.o11venuepatronid, $0), =($cor1071.o11venuepatronid, $0), =($cor1072.o11venuepatronid, $0), =($cor1073.o11venuepatronid, $0), =($cor1074.o11venuepatronid, $0), =($cor1075.o11venuepatronid, $0), =($cor1076.o11venuepatronid, $0), =($cor1077.o11venuepatronid, $0), =($cor1078.o11venuepatronid, $0), =($cor1079.o11venuepatronid, $0), =($cor1080.o11venuepatronid, $0), =($cor1081.o11venuepatronid, $0), =($cor1082.o11venuepatronid, $0), =($cor1083.o11venuepatronid, $0), =($cor1084.o11venuepatronid, $0), =($cor1085.o11venuepatronid, $0), =($cor1086.o11venuepatronid, $0), =($cor1087.o11venuepatronid, $0), =($cor1088.o11venuepatronid, $0), =($cor1089.o11venuepatronid, $0), =($cor1090.o11venuepatronid, $0), =($cor1091.o11venuepatronid, $0), =($cor1092.o11venuepatronid, $0), =($cor1093.o11venuepatronid, $0), =($cor1094.o11venuepatronid, $0), =($cor1095.o11venuepatronid, $0), =($cor1096.o11venuepatronid, $0), =($cor1097.o11venuepatronid, $0), =($cor1098.o11venuepatronid, $0), =($cor1099.o11venuepatronid, $0)))]): rowcount = 109255.9875, cumulative cost = {3022748.9875 rows, 0.0 cpu, 0.0 io}, id = 2645140&nbsp; JdbcTableScan(table=[[28ae4f8f-34a6-4f04-8c4e-393b7fc179c6, OSUSR_4FH_VENUEPATRON]]): rowcount = 2913493.0, cumulative cost = {2913493.0 rows, 0.0 cpu, 0.0 io}, id = 2617352:- The only way the pagination affects the aggregate is it directly uses the **Count** of the results:![](https://supportoutsystems.zendesk.com/attachments/token/t7idBvZEqVq9oAJJmCK0nIQIO/?name=image.png)
- This deserves further highlight because comparing the internal traces, we can see the pagination example trace (non-working) includes an additional Count statement, which fails:- Successful (only 1 CreateCommand parent span):![](https://supportoutsystems.zendesk.com/attachments/token/F0uEy1kylwJSlj9mQsCUTdLRr/?name=image.png)- Error (2 CreateCommand parent spans):![](https://supportoutsystems.zendesk.com/attachments/token/Ostcu5KDjLxTkfuOYraoP8Qpv/?name=image.png)- Note the statement that errors out - it's related to the count:![](https://supportoutsystems.zendesk.com/attachments/token/CAAQcBonRgO18Uc7zUq6GFTV4/?name=image.png)
- There were also recent issues related with the pagination and count features, as per https://outsystems.slack.com/archives/C0787TKKSA2![](https://supportoutsystems.zendesk.com/attachments/token/xqQKdD65MUK33jG71VWuQ8S49/?name=image.png)- However, this message is from June 18th, before the customer faced and reported these issues (June 20th), so I'm not sure it is directly related, but it does seem there are issues still.**TECH DATA OR ANY OTHER RELEVANT INFO**
Ring: ga
Tenant Id: f0d67e99-3f25-4b54-8916-6c4ee8f3d54c
Tenant Prefix: np
Region: ap-southeast-2_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 Retrospective**Causes:** Bug
infoDetails
**Ring:** ga
**System-wide impact:**&nbsp; 
**Tenant ID:** f0d67e99-3f25-4b54-8916-6c4ee8f3d54c
**Tenant Prefix:** np
**Routing Error Code:** N/A
**Product Area:** Phoenix::Application Runtime::Database access::External entities
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/633-issue-when-using-the-count-from-an-aggregate)

**Date**

**Source**

**User**

**Event**
June 26  5:37 PM WESTwebRootly
created an alert via
June 26  5:37 PM WESTwebRootly
Rootly created this incident
June 26  5:37 PM WESTwebRootly
In triage date has been set to June 26  5:37 PM WEST
July 1 12:09 PM WESTwebVasco Gomes
Teams has been added: Data Fabric Engine
July 1 12:09 PM WESTwebVasco Gomes
Services has been added: Data Fabric Engine Services
July 1 12:10 PM WESTwebVasco Gomes
Causes has been added: Bug
July 1 12:15 PM WESTwebVasco GomesSend ZenDesk private comment has been set: We've completed our analysis of this incident and we found a Bug. We are going to create it and link it to the incident.  
However, there is a workaround that the client can use. The count query is automatically generated by the pagination widget and the error occurs when Query Engine tries to obtain the overall count of the query.  
There is another way to implement pagination that doesn't trigger the count query. We found a component in Forge that would temporarily solve the issue, since it also paginates the results but doesn't provide the overall count.  
The Forge Component is this one -&gt; [https://www.outsystems.com/forge/component-documentation/15862/hi-simple-pagination-odc/0](https://www.outsystems.com/forge/component-documentation/15862/hi-simple-pagination-odc/0)&nbsp;  This should be seen as a temporary solution while we solve the bug.July 1 12:15 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
We've completed our analysis of this incident and we found a Bug. We are going to create it and link it to the incident.  
However, there is a workaround that the client can use. The count query is automatically generated by the pagination widget and the error occurs when Query Engine tries to obtain the overall count of the query.  
There is another way to implement pagination that doesn't trigger the count query. We found a component in Forge that would temporarily solve the issue, since it also paginates the results but doesn't provide the overall count.  
The Forge Component is this one -&gt; [https://www.outsystems.com/forge/component-documentation/15862/hi-simple-pagination-odc/0](https://www.outsystems.com/forge/component-documentation/15862/hi-simple-pagination-odc/0)&nbsp;  This should be seen as a temporary solution while we solve the bug.
July 1 12:15 PM WESTwebRootlySend ZenDesk private comment has been unsetJuly 1 12:15 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

July 1 12:16 PM WESTwebVasco Gomes
Incident has been started
July 1 12:16 PM WESTwebVasco Gomes
Incident has been mitigated
July 1 12:19 PM WESTwebBruno Coelho
Action Item - Task: Register correlation variables for MergeJoin algorithm has been added.
July 1 12:24 PM WESTwebVasco GomesVasco Gomes has been assigned as CommanderJuly 1 12:24 PM WESTwebVasco GomesBruno Coelho has been assigned as EngineerJuly 1 12:29 PM WESTwebVasco Gomes
Action Item - Task: Register correlation variables for MergeJoin algorithm has been removed.
July 1 12:29 PM WESTwebVasco Gomes
Action Item - Follow-up: We've created the following Bug https://outsystemsrd.atlassian.net/browse/RDDFC-2939 to solve the issue has been added.
July 9  4:09 AM WESTwebRootlyZendesk Private Comment has been set: ----------------------------------------------**Update to R&amp;D**Hello team, customer responded to the workaround we have suggested and reporting that the workaround is not actually resolve the underlying issue that customer is facing:- The example provided was to be able to easily demonstrate the failure, my actual use case is to provide the total count to an API. The issue is not only using on pagination it is where ever the total count is used. See below, that fails and presents the same error:- ![](https://supportoutsystems.zendesk.com/attachments/token/8xeS4ARacLBfKvzXGeoD5eulL/?name=1720482814000000000__1720482813783.png)
- This assign statement causes the same error to occur.
- Therefore while the supplied pagination widget might work for paginating on ODC.__July 9  4:09 AM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**Hello team, customer responded to the workaround we have suggested and reporting that the workaround is not actually resolve the underlying issue that customer is facing:- The example provided was to be able to easily demonstrate the failure, my actual use case is to provide the total count to an API. The issue is not only using on pagination it is where ever the total count is used. See below, that fails and presents the same error:- ![](https://supportoutsystems.zendesk.com/attachments/token/8xeS4ARacLBfKvzXGeoD5eulL/?name=1720482814000000000__1720482813783.png)
- This assign statement causes the same error to occur.
- Therefore while the supplied pagination widget might work for paginating on ODC.__
July 9  4:09 AM WESTwebRootlyZendesk Private Comment has been changed to: ------------------------------------------------ This notification was sent from Zendesk Support ticket #3025018 to all linked JIRA issues by Sugan Krishnan. --**Update to R&amp;D**Hello team, customer responded to the workaround we have suggested and reporting that the workaround is not actually resolve the underlying issue that customer is facing:- The example provided was to be able to easily demonstrate the failure, my actual use case is to provide the total count to an API. The issue is not only using on pagination it is where ever the total count is used. See below, that fails and presents the same error:- Attachment - 1720482814000000000__1720482813783.png
- This assign statement causes the same error to occur.
- Therefore while the supplied pagination widget might work for paginating on ODC._&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_July 9  4:09 AM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
------------------------------------------------ This notification was sent from Zendesk Support ticket #3025018 to all linked JIRA issues by Sugan Krishnan. --**Update to R&amp;D**Hello team, customer responded to the workaround we have suggested and reporting that the workaround is not actually resolve the underlying issue that customer is facing:- The example provided was to be able to easily demonstrate the failure, my actual use case is to provide the total count to an API. The issue is not only using on pagination it is where ever the total count is used. See below, that fails and presents the same error:- Attachment - 1720482814000000000__1720482813783.png
- This assign statement causes the same error to occur.
- Therefore while the supplied pagination widget might work for paginating on ODC.__
August 9 12:57 PM WESTwebRootly
The Global Support team marked this incident as closed in ZenDesk.
August 9 12:57 PM WESTwebRootly
Incident has been resolved
August 9 12:57 PM WESTwebRootlyZenDesk Event Type has been set: solved## 📝 Follow Up Items[View on Rootly](https://rootly.com/account/incidents/633-issue-when-using-the-count-from-an-aggregate#nav-action-items)

**Summary**

**Priority**

**Status**

**Assignee**

**Links**
We've created the following Bug https://outsystemsrd.atlassian.net/browse/RDDFC-2939 to solve the issuetrueYellowMediumtrueBlueOpenBruno Coelho