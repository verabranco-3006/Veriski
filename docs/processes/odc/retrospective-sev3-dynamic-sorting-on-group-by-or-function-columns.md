---
title: Retrospective-SEV3-Dynamic sorting on Group by or function columns
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4347658275/Retrospective-SEV3-Dynamic+sorting+on+Group+by+or+function+columns
confluence_space: RKB
confluence_page_id: 4347658275
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV3-Dynamic sorting on Group by or function columns

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV3

Teams:&nbsp;trueBlueBuild Services&nbsp;trueBlueClient Runtime&nbsp;trueBlueData Fabric Clients
#### 🕐 Timestamps
Started At:&nbsp;trueBlueJuly 24  3:18 PM WEST

Mitigated At:&nbsp;trueYellowAugust 8  2:29 PM WEST

Resolved At:&nbsp;trueGreenAugust 8  2:29 PM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/720-dynamic-sorting-on-group-by-or-function-columns)
[Pagerduty incident](https://outsystems.pagerduty.com/incidents/Q1A0CKGVCQWSSB)

[Slack channel](https://slack.com/app_redirect?channel=C07DUMJHW9L&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3035555)

#### 🧑&zwj;🚒 Incident Rolestrue
**Commander**

Z&eacute; Perdigao

**Engineer**

Pedro Rosa
#### Summary
&lt;hr&gt;
&lt;p class=&quot;redcarpet&quot;&gt;&lt;strong&gt;ISSUE DESCRIPTION AND HOW TO REPRODUCE&lt;/strong&gt;&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Not able to sort by dynamic attribute when an external entity is included in aggregate (regardless of sorting by an external attribute or not, it's just the presence of the external entity that affects this):&lt;ul&gt;
&lt;li&gt;No sort being used (test value empty), no problem:
&lt;img width=&quot;100%&quot; src=&quot;https://supportoutsystems.zendesk.com/attachments/token/ouOhnK0bWnPulPjllYzx1qkKR/?name=image.png&quot;&gt;
&lt;/li&gt;
&lt;li&gt;Fill sort test value, no results:
&lt;img width=&quot;100%&quot; src=&quot;https://supportoutsystems.zendesk.com/attachments/token/lvF1avF1qU2fPqvxUYSe9Aof1/?name=image.png&quot;&gt;
&lt;/li&gt;
&lt;li&gt;Removing external entity fixes it:
&lt;img width=&quot;100%&quot; src=&quot;https://supportoutsystems.zendesk.com/attachments/token/igSK3m9uFqvZ20PES6uv6r6VS/?name=image.png&quot;&gt;
&lt;/li&gt;
&lt;li&gt;Removed external entity from aggregate, sort works okay:
&lt;img width=&quot;100%&quot; src=&quot;https://supportoutsystems.zendesk.com/attachments/token/CzonnKi6Hi4dRPMbifIdg5ZGN/?name=image.png&quot;&gt;
&lt;img width=&quot;100%&quot; src=&quot;https://supportoutsystems.zendesk.com/attachments/token/53YMqvW4j3E37oLY95ywRB7Rm/?name=image.png&quot;&gt;
&lt;/li&gt;
&lt;li&gt;Note that the column being sorted is not related to the external entity.&lt;/li&gt;
&lt;/ul&gt;
&lt;/li&gt;
&lt;/ul&gt;
&lt;p class=&quot;redcarpet&quot;&gt;&lt;strong&gt;IMPACT ON THE CUSTOMER&lt;/strong&gt;&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Development; not able to use dynamic sorting with external entities in aggregate.&lt;/li&gt;
&lt;/ul&gt;
&lt;p class=&quot;redcarpet&quot;&gt;&lt;strong&gt;TROUBLESHOOTING STEPS &amp; WORKAROUND&lt;/strong&gt;&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;When attempting to reproduce this, we also found another potential issue when testing in our sandbox, which we'll add here. But we'll start with the customer's problem:&lt;ul&gt;
&lt;li&gt;We can find an error trace in Query Engine - Recent Errors when no results are returned in Preview Data:&lt;/li&gt;
&lt;li&gt;Error trace
&lt;img width=&quot;100%&quot; src=&quot;https://supportoutsystems.zendesk.com/attachments/token/6O5MA0MrutWqaWzRDdz2EqLR1/?name=image.png&quot;&gt;&lt;ul&gt;
&lt;li&gt;Error: &lt;code&gt;Column 'COUNTOFID' not found in any table&lt;/code&gt;
&lt;/li&gt;
&lt;/ul&gt;
&lt;/li&gt;
&lt;li&gt;Successful trace for comparison if needed&lt;/li&gt;
&lt;li&gt;Note also that there's another open escalation which originated from the same customer, and is also related with different behaviors when the external entity is included in aggregate: RDINC-27219&lt;/li&gt;
&lt;/ul&gt;
&lt;/li&gt;
&lt;li&gt;Now for the other problem we found while testing:&lt;ul&gt;
&lt;li&gt;Dynamic sorting does not work when using a &lt;strong&gt;local variable&lt;/strong&gt;, only when using an &lt;strong&gt;input variable&lt;/strong&gt;.&lt;/li&gt;
&lt;li&gt;Created an entity with two attributes, Name and Type - we're going to group and count by Type:
&lt;img width=&quot;100%&quot; src=&quot;https://supportoutsystems.zendesk.com/attachments/token/wPYgtlrUZ2Q7LmEr09ahGHMM7/?name=image.png&quot;&gt;
&lt;/li&gt;
&lt;li&gt;As you can see below, when the sort variable is a local variable and we give it a test value, it shows a warning and returns incomplete data:
&lt;img width=&quot;100%&quot; src=&quot;https://supportoutsystems.zendesk.com/attachments/token/dyR6QhUWSq2YjuHqWqVP5rDOs/?name=image.png&quot;&gt;
&lt;/li&gt;
&lt;li&gt;When we swap the sort variable to an input variable, it works as expected, both sort and data:
&lt;img width=&quot;100%&quot; src=&quot;https://supportoutsystems.zendesk.com/attachments/token/Yh0GAsuCW5xPQj8r2ODC7z8YS/?name=image.png&quot;&gt;
&lt;/li&gt;
&lt;li&gt;This affects runtime as well (when using the local variable), not sorting the data correctly, so it's not specific to Preview Data:
&lt;img width=&quot;100%&quot; src=&quot;https://supportoutsystems.zendesk.com/attachments/token/SIDuu2wzywNxSFZVy9ulXUK2t/?name=image.png&quot;&gt;
&lt;/li&gt;
&lt;/ul&gt;
&lt;/li&gt;
&lt;/ul&gt;
&lt;p class=&quot;redcarpet&quot;&gt;&lt;strong&gt;TECH DATA OR ANY OTHER RELEVANT INFO&lt;/strong&gt;
&lt;br&gt;Ring: ga
&lt;br&gt;Tenant Id: f0d67e99-3f25-4b54-8916-6c4ee8f3d54c
&lt;br&gt;Tenant Prefix: np
&lt;br&gt;Region: ap-southeast-2&lt;/p&gt;&lt;p class=&quot;redcarpet&quot;&gt;&lt;em&gt;&lt;! do not remove this line, this will be used to the trigger&lt;/em&gt; Technical Support::Send to R&amp;D - ODC &lt;em&gt;#trigger_send_to_r&amp;d_odc !&gt;&lt;/em&gt;&lt;/p&gt;
## 📝 RetrospectiveinfoDetails
**Ring:** ga
**System-wide impact:**&nbsp; No
**Tenant ID:** f0d67e99-3f25-4b54-8916-6c4ee8f3d54c
**Tenant Prefix:** np
**Routing Error Code:** N/A
**Product Area:** Phoenix::Service Studio::Data Access and Manipulation::Aggregates::Preview Data
### Impact:
The user is not able to use Dynamic sorting in aggregates when the &quot;Source&quot; of the aggregate includes an external entity.

Depending on the value passed to the dynamic sort, this may impact for data preview and runtime.
### Investigation and troubleshooting findings:
The attributes added to the dynamic sort are not being wrapped in double quotes in the generated SQL, which then makes Query Engine convert all characters to upper case and thus the attribute is not found because it does not match any of the existing attributes.

However, if we use OutSystems syntax by wrapping the attribute in square brackets ([ ]), the Build Job will correctly identify it as an attribute and wrap it in double quotes in the generated SQL.
### Resolution:
We are currently waiting for an internal solution that involves aligning several teams to define and develop a resolution. This means that Client Runtime is currently in alignments with Build Services, IDE, and TK teams.

This should be considered as a future new solution, as it has been this way at least, since O11.

Additionally, there is already a runbook to address and mitigate this issue ([https://outsystemsrd.atlassian.net/wiki/spaces/RDMBVS/pages/4317577337/Not+able+to+sort+by+dynamic+attribute+when+an+external+entity+is+included+in+aggregate](https://outsystemsrd.atlassian.net/wiki/spaces/RDMBVS/pages/4317577337/Not+able+to+sort+by+dynamic+attribute+when+an+external+entity+is+included+in+aggregate)).
## Tasks performed during incident resolution:
**Summary:** Investigate how to solve the issue

**Status:**trueGreendone

&nbsp;
## Executive Summary
[Guidelines](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4144496679/Incident+Retrospectives+-+Playbook#STEP-3---Write-the-Executive-Summary)
## Root Causes 
[Guidelines](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4144496679/Incident+Retrospectives+-+Playbook#STEP-1---Perform-the-Root-Cause-Analysis)

If the customer needs formal RCA, please fill out the following field with the document URL

[Please follow these instructions and place the RCA URL in the field below.](https://docs.google.com/document/d/13rXmBsOJh73nV2D6Z17SIBGBu2HOTWty5ddsvU000JM/edit#heading=h.bqxasxszr5q)

RCA URL

&lt;Place the URL of the customer RCA here if you have created one&gt;
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/720-dynamic-sorting-on-group-by-or-function-columns)

**Date**

**Source**

**User**

**Event**
July 17 12:51 PM WESTwebRootly
created an alert via
July 17 12:51 PM WESTwebRootly
Rootly created this incident
July 17 12:51 PM WESTwebRootly
In triage date has been set to July 17 12:51 PM WEST
July 24  3:18 PM WESTwebZ&eacute; Perdigao
Incident has been started
July 24  3:26 PM WESTwebZ&eacute; PerdigaoZ&eacute; Perdigao has been assigned as CommanderJuly 24  3:26 PM WESTwebZ&eacute; PerdigaoKaty Batista has been assigned as EngineerJuly 24  3:29 PM WESTwebZ&eacute; Perdigao
Action Item - Task: Investigate how to solve the issue has been added.
July 24  4:02 PM WESTwebZ&eacute; PerdigaoPedro Rosa has been assigned as EngineerJuly 25 12:28 PM WESTwebPedro Rosa
Summary has been changed to 

&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;

&nbsp;&nbsp;
&nbsp;&nbsp;**ISSUE DESCRIPTION AND HOW TO REPRODUCE**&nbsp;&nbsp;

&nbsp;&nbsp;

&nbsp;&nbsp;- Not able to sort by dynamic attribute when an external entity is included in aggregate (regardless of sorting by an external attribute or not, it's just the presence of the external entity that affects this):
&nbsp;&nbsp;
&nbsp;&nbsp;

- No sort being used (test value empty), no problem:

- Fill sort test value, no results:

- Removing external entity fixes it:

- Removed external entity from aggregate, sort works okay:

- Note that the column being sorted is not related to the external entity.

&nbsp;&nbsp;

&nbsp;&nbsp;

&nbsp;&nbsp;**IMPACT ON THE CUSTOMER**&nbsp;&nbsp;

&nbsp;&nbsp;

&nbsp;&nbsp;- Development; not able to use dynamic sorting with external entities in aggregate.

&nbsp;&nbsp;

&nbsp;&nbsp;
&nbsp;&nbsp;**TROUBLESHOOTING STEPS &amp; WORKAROUND**&nbsp;&nbsp;

&nbsp;&nbsp;

&nbsp;&nbsp;- When attempting to reproduce this, we also found another potential issue when testing in our sandbox, which we'll add here. But we'll start with the customer's problem:
&nbsp;&nbsp;
&nbsp;&nbsp;

- We can find an error trace in Query Engine - Recent Errors when no results are returned in Preview Data:
- Error trace

- Error: `Column 'COUNTOFID' not found in any table`

- Successful trace for comparison if needed

&nbsp;&nbsp;- Note also that there's another open escalation which originated from the same customer, and is also related with different behaviors when the external entity is included in aggregate: RDINC-27219
&nbsp;&nbsp;
&nbsp;&nbsp;
- Now for the other problem we found while testing:
&nbsp;&nbsp;

- Dynamic sorting does not work when using a **local variable**, only when using an **input variable**.
- Created an entity with two attributes, Name and Type - we're going to group and count by Type:

- As you can see below, when the sort variable is a local variable and we give it a test value, it shows a warning and returns incomplete data:

- When we swap the sort variable to an input variable, it works as expected, both sort and data:

- This affects runtime as well (when using the local variable), not sorting the data correctly, so it's not specific to Preview Data:

&nbsp;&nbsp;

&nbsp;&nbsp;

&nbsp;&nbsp;**TECH DATA OR ANY OTHER RELEVANT INFO**
&nbsp;&nbsp;
Ring: ga

&nbsp;&nbsp;
Tenant Id: f0d67e99-3f25-4b54-8916-6c4ee8f3d54c

&nbsp;&nbsp;
Tenant Prefix: np

&nbsp;&nbsp;
Region: ap-southeast-2
&nbsp;&nbsp;
&nbsp;&nbsp;*&lt;! do not remove this line, this will be used to the trigger* Technical Support::Send to R&amp;D - ODC *#trigger_send_to_r&amp;d_odc !&gt;*&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;July 25 12:28 PM WESTwebPedro RosaSystem-wide impact has been set: NoJuly 25 12:28 PM WESTwebPedro RosaImpact has been set: The user is not able to use Dynamic sorting in aggregates when the &quot;Source&quot; of the aggregate includes an external entity.
Depending on the value passed to the dynamic sort, this may impact for data preview and runtime.July 25 12:28 PM WESTwebPedro RosaInvestigation and troubleshooting findings has been set: The attributes added to the dynamic sort are not being wrapped in double quotes in the generated SQL, which then makes Query Engine convert all characters to upper case and thus the attribute is not found because it does not match any of the existing attributes.
However, if we use OutSystems syntax by wrapping the attribute in square brackets ([ ]), the Build Job will correctly identify it as an attribute and wrap it in double quotes in the generated SQL.July 25  1:41 PM WESTwebRootly[Slack Channel](https://slack.com/app_redirect?channel=C07DUMJHW9L&amp;team=T041063TZ) has been createdJuly 25  4:31 PM WESTwebPedro RosaSend ZenDesk private comment has been set: Hi Support team,  We are still investigating a way to make the dynamic sort work the same way both with and without external entities.  In the meantime, we have a workaround to share with the customer.  
When an aggregate includes an external entity, the dynamic sort needs a little help to identify the attributes in the expression.  In case they want to sort by one of the entity's attributes, they must use the following format:  
\- &quot;.&quot;  
An example with their entity and attributes:  
\- &quot;POSTransaction.Id&quot;  In case they want to sort by an aggregate function (e.g. Count()) or calculated attribute, they must use the following format:  
\- &quot;\[CustomAttributeName\]&quot;  
Using their example:  
\- &quot;\[CountOfId\]&quot;  The ASC/DESC is optional of course.  This workaround is pretty straightforward when previewing data in ODC Studio, but to make it work at runtime, some changes on the code might be required.  
For example, in the code displayed in the following image I had to add the SortBy assign node to the beginning of the automatically generated OnSort action in order to wrap the name of calculated attributes in square brackets.  
When clicking the headers of table columns associated with entity attributes, the value passed to SortBy already comes in the format ., so nothing needs to be done for those cases.  ![image.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDE3NzY2LCJwdXIiOiJibG9iX2lkIn19--e3e076427ab1d38c0c56d5bbc3fa0c9addf40c6c/image.png)image.png 189.64 KBBest regards,  
Pedro RosaJuly 25  4:31 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hi Support team,  We are still investigating a way to make the dynamic sort work the same way both with and without external entities.  In the meantime, we have a workaround to share with the customer.  
When an aggregate includes an external entity, the dynamic sort needs a little help to identify the attributes in the expression.  In case they want to sort by one of the entity's attributes, they must use the following format:  
\- &quot;.&quot;  
An example with their entity and attributes:  
\- &quot;POSTransaction.Id&quot;  In case they want to sort by an aggregate function (e.g. Count()) or calculated attribute, they must use the following format:  
\- &quot;\[CustomAttributeName\]&quot;  
Using their example:  
\- &quot;\[CountOfId\]&quot;  The ASC/DESC is optional of course.  This workaround is pretty straightforward when previewing data in ODC Studio, but to make it work at runtime, some changes on the code might be required.  
For example, in the code displayed in the following image I had to add the SortBy assign node to the beginning of the automatically generated OnSort action in order to wrap the name of calculated attributes in square brackets.  
When clicking the headers of table columns associated with entity attributes, the value passed to SortBy already comes in the format ., so nothing needs to be done for those cases.  ![image.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDE3NzY2LCJwdXIiOiJibG9iX2lkIn19--e3e076427ab1d38c0c56d5bbc3fa0c9addf40c6c/image.png)image.png 189.64 KBBest regards,  
Pedro Rosa
July 25  4:31 PM WESTwebRootlySend ZenDesk private comment has been unsetJuly 25  4:31 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

July 25  5:10 PM WESTwebPedro RosaSwarm has been set: Build ServicesJuly 25  5:10 PM WESTwebRootly[PagerDuty Incident](https://outsystems.pagerduty.com/incidents/Q1A0CKGVCQWSSB) has been created.
📧 Notified Diogo Rom&atilde;o by email.&nbsp;&nbsp;📱 Notified Diogo Rom&atilde;o by SMS.&nbsp;&nbsp;📲 Notified Diogo Rom&atilde;o by push notification.  (via Android)July 25  5:12 PM WESTwebRootly
Diogo Rom&atilde;o acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q1A0CKGVCQWSSB). (via Slack)
July 26  5:15 PM WESTwebPedro RosaSwarm has been set: Client RuntimeJuly 26  5:15 PM WESTwebPedro RosaSwarm has been unset: Build ServicesJuly 26  5:15 PM WESTwebRootly
Pagerduty Integrations added Tiago Miguel Pereira as responder in [PagerDuty](https://outsystems.pagerduty.com/incidents/Q1A0CKGVCQWSSB)
July 26  5:20 PM WESTwebRootly
Tiago Miguel Pereira joined this [PagerDuty](https://outsystems.pagerduty.com/incidents/Q1A0CKGVCQWSSB) incident.
July 29 11:31 AM WESTwebPedro Rosa
Action Item - Task: Investigate how to solve the issue status changed from Open &rarr; Done
July 30  5:17 PM WESTslacktiago.miguel.pereira
Just wanted to let you know that I have created a runbook ([link](https://outsystemsrd.atlassian.net/wiki/spaces/RDMBVS/pages/4317577337/Not+able+to+sort+by+dynamic+attribute+when+an+external+entity+is+included+in+aggregate)) for future errors like this. This should be useful until we have a final decision about the solution we want to proceed with.
I used part of the workaround that Pedro provided to the support to complete the Mitigation process in the Runbook.
July 30  5:20 PM WESTwebTiago M. PereiraSend ZenDesk private comment has been set: Hello support,  Just wanted to let you know that we have created a runbook ([link](https://outsystemsrd.atlassian.net/wiki/spaces/RDMBVS/pages/4317577337/Not+able+to+sort+by+dynamic+attribute+when+an+external+entity+is+included+in+aggregate)) for future reference in case more errors like this appear. We applied the same workaround that Pedro provided in his last message.  This should be useful until we have a final solution.  
We'll keep you updated.  Let us know if you have any additional questions,Best regards,Tiago PereiraJuly 30  5:20 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hello support,  Just wanted to let you know that we have created a runbook ([link](https://outsystemsrd.atlassian.net/wiki/spaces/RDMBVS/pages/4317577337/Not+able+to+sort+by+dynamic+attribute+when+an+external+entity+is+included+in+aggregate)) for future reference in case more errors like this appear. We applied the same workaround that Pedro provided in his last message.  This should be useful until we have a final solution.  
We'll keep you updated.  Let us know if you have any additional questions,Best regards,Tiago Pereira
July 30  5:20 PM WESTwebRootlySend ZenDesk private comment has been unsetJuly 30  5:20 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

August 7 10:03 AM WESTwebTiago M. Pereira
Hello team,To my knowledge, there is nothing blocking the ticket from being marked as solved. We are currently waiting for an internal solution that involves aligning several teams to define and develop a resolution. This means that Client Runtime is currently in alignments with Build Services, IDE, and TK teams.
This should be considered as a new solution, as it has been this way at least, since O11. 
Additionally, there is already a runbook that was shared here a week ago (https://outsystemsrd.atlassian.net/wiki/spaces/RDMBVS/pages/4317577337/Not+able+to+sort+by+dynamic+attribute+when+an+external+entity+is+included+in+aggregate).After aligning with support, we are considering this ticket as solved from our side and we will be waiting for support to mark the incident as solved.
August 8  2:29 PM WESTwebTiago M. Pereira
Incident has been resolved
August 8  2:29 PM WESTwebTiago M. PereiraResolution has been set: We are currently waiting for an internal solution that involves aligning several teams to define and develop a resolution. This means that Client Runtime is currently in alignments with Build Services, IDE, and TK teams.
This should be considered as a future new solution, as it has been this way at least, since O11.Additionally, there is already a runbook to address and mitigate this issue (https://outsystemsrd.atlassian.net/wiki/spaces/RDMBVS/pages/4317577337/Not+able+to+sort+by+dynamic+attribute+when+an+external+entity+is+included+in+aggregate).