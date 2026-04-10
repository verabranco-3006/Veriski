---
title: Retrospective-SEV3-Getting errors in aggregate when adding page input params in filter for external entities
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4375314524/Retrospective-SEV3-Getting+errors+in+aggregate+when+adding+page+input+params+in+filter+for+external+entities
confluence_space: RKB
confluence_page_id: 4375314524
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV3-Getting errors in aggregate when adding page input params in filter for external entities

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV3

Teams:&nbsp;trueBlueData Fabric Clients&nbsp;trueBlueData Fabric Engine
#### 🕐 Timestamps
Started At:&nbsp;trueBlueAugust 2 12:51 PM WEST

Mitigated At:&nbsp;trueYellowAugust 21 11:44 AM WEST

Resolved At:&nbsp;trueGreenAugust 21 11:44 AM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/750-getting-errors-in-aggregate-when-adding-page-input-params-in-filter-for-external-entities)
[Slack channel](https://slack.com/app_redirect?channel=C07E6QNQ649&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3037710)

#### 🧑&zwj;🚒 Incident Rolestrue
**Commander**

Vasco Gomes
#### Summary
I'm re-opening this, since, although the workaround worked, we are sill waiting for the Query Engine fix to reach GA (it's currently in EA), and after that Data Fabric Clients team as to go ahead with their changes also. 
We believe that this incident should be kept open because of it.**R&amp;D ESCALATION FORM**
Section comments can be removed for R&amp;D easier interpretation.**ISSUE DESCRIPTION AND HOW TO REPRODUCE**
We have a customer trying to migrate to ODC from O11, and they are having problem with a somewhat complicated aggregate filter that they use throughout their application that works fine in O11, but throws an unusual error in ODC.If(Trim(SearchText)=NullTextIdentifier() or Length(Trim(SearchText))=0 ,True,Index(ToLower(products.product_code),Trim(ToLower(SearchText)))&lt;&gt;-1 orIndex(ToLower(products.description),Trim(ToLower(SearchText)))&lt;&gt;-1)![](https://supportoutsystems.zendesk.com/attachments/token/LYmCcBSZoC8tIsj9UmagY2FBs/?name=image.png)Their database is case-sensitive, so they need the ToLower. Success suggested adjusting the code so that the Trim and ToLower on SearchText is done before the aggregate is called, but they claim this would be a lot of work based on how often this pattern is used in their app.Upon escalating to R&amp;D channels, https://outsystems.slack.com/archives/C061TN1GW/p1721655551306919, we were advised by Hugo to analyze why there is an actual error rather than a &ldquo;slow query&rdquo;.  It&rsquo;s not supposed to throw an error preparing the statement.**IMPACT ON THE CUSTOMER**
Their database is case-sensitive, so they need the ToLower. The customer insisted this is a sev2 however, it seems that a valid workaround was shared, they just don't want to optimize. So we're putting this as sev3**TROUBLESHOOTING STEPS &amp; WORKAROUND**
N/A**TECH DATA OR ANY OTHER RELEVANT INFO**
Ring: ga
Tenant Id: 6c875ad1-c24a-40d3-93bf-59a76e094051
Tenant Prefix: mitchell
Region: us-east-1
Q5F.K8I.OZ2.AM6.2PA.NZN.2W2.WIZ_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_Attachment(s):
image (24).png - https://supportoutsystems.zendesk.com/attachments/token/XbpIMV4YncP37jWE3XidWUe4A/?name=image+%2824%29.png
## 📝 Retrospective**Causes:** Bug
infoDetails
**Ring:** ga
**System-wide impact:**&nbsp; 
**Tenant ID:** 6c875ad1-c24a-40d3-93bf-59a76e094051
**Tenant Prefix:** mitchell
**Routing Error Code:** N/A
**Product Area:** Phoenix::Service Studio::Data Access and Manipulation::Aggregates::Preview Data
### Impact:### Investigation and troubleshooting findings:### Resolution:## Tasks performed during incident resolution:
**Summary:** Then the Clients team would have to change the DbProvider to use that new funcion, and update the BuildJob to use the new version of the DbProvider.

**Status:**trueBlueopen

**Summary:** @Vera Cardoso (eca) proposed implementing a custom function that works exactly as position, but with a different syntax. Something like ``CHAR_INDEX(string, string )`` . This would be on the Engine's side.

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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/750-getting-errors-in-aggregate-when-adding-page-input-params-in-filter-for-external-entities)

**Date**

**Source**

**User**

**Event**
July 23  6:10 PM WESTwebRootly
created an alert via
July 23  6:10 PM WESTwebRootly
Rootly created this incident
July 23  6:10 PM WESTwebRootly
In triage date has been set to July 23  6:10 PM WEST
July 23  6:12 PM WESTwebRootlyZendesk Private Comment has been set: ----------------------------------------------**Update to R&amp;D**
Please ignore our last communication.**R&amp;D ESCALATION FORM**
Section comments can be removed for R&amp;D easier interpretation.**ISSUE DESCRIPTION AND HOW TO REPRODUCE**
We have a customer trying to migrate to ODC from O11, and they are having problem with a somewhat complicated aggregate filter that they use throughout their application that works fine in O11, but throws an unusual error in ODC.If(Trim(SearchText)=NullTextIdentifier() or Length(Trim(SearchText))=0 ,True,Index(ToLower(products.product_code),Trim(ToLower(SearchText)))&lt;&gt;-1 orIndex(ToLower(products.description),Trim(ToLower(SearchText)))&lt;&gt;-1)![](https://supportoutsystems.zendesk.com/attachments/token/LYmCcBSZoC8tIsj9UmagY2FBs/?name=image.png)Their database is case-sensitive, so they need the ToLower. Success suggested adjusting the code so that the Trim and ToLower on SearchText is done before the aggregate is called, but they claim this would be a lot of work based on how often this pattern is used in their app.Upon escalating to R&amp;D channels, https://outsystems.slack.com/archives/C061TN1GW/p1721655551306919, we were advised by Hugo to analyze why there is an actual error rather than a &ldquo;slow query&rdquo;.  It&rsquo;s not supposed to throw an error preparing the statement.**IMPACT ON THE CUSTOMER**
Their database is case-sensitive, so they need the ToLower. The customer insisted this is a sev2 however, it seems that a valid workaround was shared, they just don't want to optimize. So we're putting this as sev3**TROUBLESHOOTING STEPS &amp; WORKAROUND**
N/A**TECH DATA OR ANY OTHER RELEVANT INFO**
Ring: ga
Tenant Id: 6c875ad1-c24a-40d3-93bf-59a76e094051
Tenant Prefix: mitchell
Region: us-east-1
Q5F.K8I.OZ2.AM6.2PA.NZN.2W2.WIZ__July 23  6:12 PM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
Please ignore our last communication.**R&amp;D ESCALATION FORM**
Section comments can be removed for R&amp;D easier interpretation.**ISSUE DESCRIPTION AND HOW TO REPRODUCE**
We have a customer trying to migrate to ODC from O11, and they are having problem with a somewhat complicated aggregate filter that they use throughout their application that works fine in O11, but throws an unusual error in ODC.If(Trim(SearchText)=NullTextIdentifier() or Length(Trim(SearchText))=0 ,True,Index(ToLower(products.product_code),Trim(ToLower(SearchText)))&lt;&gt;-1 orIndex(ToLower(products.description),Trim(ToLower(SearchText)))&lt;&gt;-1)![](https://supportoutsystems.zendesk.com/attachments/token/LYmCcBSZoC8tIsj9UmagY2FBs/?name=image.png)Their database is case-sensitive, so they need the ToLower. Success suggested adjusting the code so that the Trim and ToLower on SearchText is done before the aggregate is called, but they claim this would be a lot of work based on how often this pattern is used in their app.Upon escalating to R&amp;D channels, https://outsystems.slack.com/archives/C061TN1GW/p1721655551306919, we were advised by Hugo to analyze why there is an actual error rather than a &ldquo;slow query&rdquo;.  It&rsquo;s not supposed to throw an error preparing the statement.**IMPACT ON THE CUSTOMER**
Their database is case-sensitive, so they need the ToLower. The customer insisted this is a sev2 however, it seems that a valid workaround was shared, they just don't want to optimize. So we're putting this as sev3**TROUBLESHOOTING STEPS &amp; WORKAROUND**
N/A**TECH DATA OR ANY OTHER RELEVANT INFO**
Ring: ga
Tenant Id: 6c875ad1-c24a-40d3-93bf-59a76e094051
Tenant Prefix: mitchell
Region: us-east-1
Q5F.K8I.OZ2.AM6.2PA.NZN.2W2.WIZ__
July 23  6:12 PM WESTwebRootlyZendesk Private Comment has been changed to: ------------------------------------------------ This notification was sent from Zendesk Support ticket #3037710 to all linked JIRA issues by Ricardo Moreira. --**Update to R&amp;D**
Please ignore our last communication.**R&amp;D ESCALATION FORM**
Section comments can be removed for R&amp;D easier interpretation.**ISSUE DESCRIPTION AND HOW TO REPRODUCE**
We have a customer trying to migrate to ODC from O11, and they are having problem with a somewhat complicated aggregate filter that they use throughout their application that works fine in O11, but throws an unusual error in ODC.If(Trim(SearchText)=NullTextIdentifier() or Length(Trim(SearchText))=0 ,True,Index(ToLower(products.product_code),Trim(ToLower(SearchText)))&lt;&gt;-1 orIndex(ToLower(products.description),Trim(ToLower(SearchText)))&lt;&gt;-1)Attachment - image.pngTheir database is case-sensitive, so they need the ToLower. Success suggested adjusting the code so that the Trim and ToLower on SearchText is done before the aggregate is called, but they claim this would be a lot of work based on how often this pattern is used in their app.Upon escalating to R&amp;D channels, https://outsystems.slack.com/archives/C061TN1GW/p1721655551306919, we were advised by Hugo to analyze why there is an actual error rather than a &ldquo;slow query&rdquo;. It&rsquo;s not supposed to throw an error preparing the statement.**IMPACT ON THE CUSTOMER**
Their database is case-sensitive, so they need the ToLower. The customer insisted this is a sev2 however, it seems that a valid workaround was shared, they just don't want to optimize. So we're putting this as sev3**TROUBLESHOOTING STEPS &amp; WORKAROUND**
N/A**TECH DATA OR ANY OTHER RELEVANT INFO**
Ring: ga
Tenant Id: 6c875ad1-c24a-40d3-93bf-59a76e094051
Tenant Prefix: mitchell
Region: us-east-1
Q5F.K8I.OZ2.AM6.2PA.NZN.2W2.WIZ_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;__Attachments_image (24).pngJuly 23  6:12 PM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
------------------------------------------------ This notification was sent from Zendesk Support ticket #3037710 to all linked JIRA issues by Ricardo Moreira. --**Update to R&amp;D**
Please ignore our last communication.**R&amp;D ESCALATION FORM**
Section comments can be removed for R&amp;D easier interpretation.**ISSUE DESCRIPTION AND HOW TO REPRODUCE**
We have a customer trying to migrate to ODC from O11, and they are having problem with a somewhat complicated aggregate filter that they use throughout their application that works fine in O11, but throws an unusual error in ODC.If(Trim(SearchText)=NullTextIdentifier() or Length(Trim(SearchText))=0 ,True,Index(ToLower(products.product_code),Trim(ToLower(SearchText)))&lt;&gt;-1 orIndex(ToLower(products.description),Trim(ToLower(SearchText)))&lt;&gt;-1)Attachment - image.pngTheir database is case-sensitive, so they need the ToLower. Success suggested adjusting the code so that the Trim and ToLower on SearchText is done before the aggregate is called, but they claim this would be a lot of work based on how often this pattern is used in their app.Upon escalating to R&amp;D channels, https://outsystems.slack.com/archives/C061TN1GW/p1721655551306919, we were advised by Hugo to analyze why there is an actual error rather than a &ldquo;slow query&rdquo;. It&rsquo;s not supposed to throw an error preparing the statement.**IMPACT ON THE CUSTOMER**
Their database is case-sensitive, so they need the ToLower. The customer insisted this is a sev2 however, it seems that a valid workaround was shared, they just don't want to optimize. So we're putting this as sev3**TROUBLESHOOTING STEPS &amp; WORKAROUND**
N/A**TECH DATA OR ANY OTHER RELEVANT INFO**
Ring: ga
Tenant Id: 6c875ad1-c24a-40d3-93bf-59a76e094051
Tenant Prefix: mitchell
Region: us-east-1
Q5F.K8I.OZ2.AM6.2PA.NZN.2W2.WIZ___Attachments_image (24).png
July 23  6:14 PM WESTwebHugo Gaspar
Teams has been added: Data Fabric Engine
July 23  6:21 PM WESTwebRootly
This incident was instantiated in Jira: RDINC-27536. Please work the incident using Rootly
July 23  7:08 PM WESTwebVasco Gomes
Incident has been started
July 23  7:11 PM WESTwebRootly
This incident was instantiated in Jira: RDINC-27536. Please work the incident using Rootly
July 23  7:22 PM WESTwebVasco GomesSend ZenDesk private comment has been set: While analysing this Incident we found a bug. We've created this [Bug](https://outsystemsrd.atlassian.net/browse/RDDFC-3008) to address this problem. Once this Bug is done the client's problem is going to be fixed. I'll keep you posted on this.July 23  7:22 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
While analysing this Incident we found a bug. We've created this [Bug](https://outsystemsrd.atlassian.net/browse/RDDFC-3008) to address this problem. Once this Bug is done the client's problem is going to be fixed. I'll keep you posted on this.
July 23  7:22 PM WESTwebRootlySend ZenDesk private comment has been unsetJuly 23  7:22 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

July 23  7:23 PM WESTwebVasco GomesVasco Gomes has been assigned as CommanderJuly 24 10:57 AM WESTwebRootly[Slack Channel](https://slack.com/app_redirect?channel=C07E6QNQ649&amp;team=T041063TZ) has been createdJuly 24 11:03 AM WESTslackjoao.ventura.abreu
The root cause is that the Calcite syntax does not support a parentheses after the `IN` of the position. The customer has a query for which the generated code is`Position(( Trim(? FROM ( Lower(?) )) ) IN (Lower(&quot;ENproducts&quot;.&quot;description&quot;) ))`when it should be```Position(( Trim(? FROM ( Lower(?) )) ) IN Lower(&quot;ENproducts&quot;.&quot;description&quot;) )```
July 24 12:33 PM WESTwebVasco GomesSend ZenDesk private comment has been set: While we are working on solving the bug, we think that there might be a workaround for the client.  
They have the following logic :*   ```If(Trim(SearchText)=NullTextIdentifier() or Length(Trim(SearchText))=0 ,True, Index(ToLower(products.product\_code),Trim(ToLower(SearchText))) &lt;&gt; -1 or Index(ToLower(products.description),Trim(ToLower(SearchText))) &lt;&gt; -1)```We believe that is the same as :&nbsp;*   ```Trim(SearchText)=NullTextIdentifier() or Length(Trim(SearchText))=0 or (ToLower(products.product\_code) like &quot;%&quot; + Trim(ToLower(SearchText)) + &quot;%&quot;) or (ToLower(products.description) like &quot;%&quot; + Trim(ToLower(SearchText)) + &quot;%&quot;).```The tests that we did gave the same results.  
Is it possible to share that with the client and see if it works as workaround for them?  
The client Use Case :![clientsUseCase.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDE2NjkyLCJwdXIiOiJibG9iX2lkIn19--d3d504b2cedaa7dad0979495462ceda3eee4695b/clientsUseCase.png)clientsUseCase.png 44.16 KB&nbsp;The workaround suggested  ![workaroundSuggested.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDE2NjkzLCJwdXIiOiJibG9iX2lkIn19--87ef8962c659287bb350f85e1fcc0050284c6ee3/workaroundSuggested.png)workaroundSuggested.png 41.5 KBJuly 24 12:33 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
While we are working on solving the bug, we think that there might be a workaround for the client.  
They have the following logic :*   ```If(Trim(SearchText)=NullTextIdentifier() or Length(Trim(SearchText))=0 ,True, Index(ToLower(products.product\_code),Trim(ToLower(SearchText))) &lt;&gt; -1 or Index(ToLower(products.description),Trim(ToLower(SearchText))) &lt;&gt; -1)```We believe that is the same as :&nbsp;*   ```Trim(SearchText)=NullTextIdentifier() or Length(Trim(SearchText))=0 or (ToLower(products.product\_code) like &quot;%&quot; + Trim(ToLower(SearchText)) + &quot;%&quot;) or (ToLower(products.description) like &quot;%&quot; + Trim(ToLower(SearchText)) + &quot;%&quot;).```The tests that we did gave the same results.  
Is it possible to share that with the client and see if it works as workaround for them?  
The client Use Case :![clientsUseCase.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDE2NjkyLCJwdXIiOiJibG9iX2lkIn19--d3d504b2cedaa7dad0979495462ceda3eee4695b/clientsUseCase.png)clientsUseCase.png 44.16 KB&nbsp;The workaround suggested  ![workaroundSuggested.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDE2NjkzLCJwdXIiOiJibG9iX2lkIn19--87ef8962c659287bb350f85e1fcc0050284c6ee3/workaroundSuggested.png)workaroundSuggested.png 41.5 KB
July 24 12:33 PM WESTwebRootlySend ZenDesk private comment has been unsetJuly 24 12:33 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

July 24 12:44 PM WESTwebJo&atilde;o Abreu
Causes has been added: Bug
July 24  3:13 PM WESTslackKatherine Batista (kbt)
The story to do the changes required to use the new function in the DbProvider is: [https://outsystemsrd.atlassian.net/browse/RDCIST-2250](https://outsystemsrd.atlassian.net/browse/RDCIST-2250)
July 25 10:26 AM WESTwebJo&atilde;o Abreu
Action Item - Task: @Vera Cardoso (eca) proposed implementing a custom function that works exactly as position, but with a different syntax. Something like ``CHAR_INDEX(string, string [, integer])`` . This would be on the Engine's side. status changed from Open &rarr; Done
July 25  4:46 PM WESTwebRootlyZendesk Private Comment has been changed to: ----------------------------------------------**Update to R&amp;D**Hello Team,
The workaround you provided works; however, please note that when sharing such queries, you should use double quotes instead of single quotes to avoid syntax errors.Trim(SearchText) = ''&nbsp;or&nbsp;(&nbsp;ToLower(Product.Description) like '%' + Trim(ToLower(SearchText)) + '%'&nbsp;or&nbsp;ToLower(Product.product_code) like '%' + Trim(ToLower(SearchText)) + '%'&nbsp;)It is crucial to share the correct information, as most of us on the 1rst line are not technical.Additionally, while the workaround functions correctly, the customer is not fully satisfied since they have similar queries in multiple places. It would require extra effort to replace all instances. Could you provide an ETA that we can communicate to the customer?_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_July 25  4:46 PM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**Hello Team,
The workaround you provided works; however, please note that when sharing such queries, you should use double quotes instead of single quotes to avoid syntax errors.Trim(SearchText) = ''&nbsp;or&nbsp;(&nbsp;ToLower(Product.Description) like '%' + Trim(ToLower(SearchText)) + '%'&nbsp;or&nbsp;ToLower(Product.product_code) like '%' + Trim(ToLower(SearchText)) + '%'&nbsp;)It is crucial to share the correct information, as most of us on the 1rst line are not technical.Additionally, while the workaround functions correctly, the customer is not fully satisfied since they have similar queries in multiple places. It would require extra effort to replace all instances. Could you provide an ETA that we can communicate to the customer?__
July 25  4:46 PM WESTwebRootlyZendesk Private Comment has been changed to: ------------------------------------------------ This notification was sent from Zendesk Support ticket #3037710 to all linked JIRA issues by Ricardo Moreira. --**Update to R&amp;D**Hello Team,
The workaround you provided works; however, please note that when sharing such queries, you should use double quotes instead of single quotes to avoid syntax errors.Trim(SearchText) = '' or ( ToLower(Product.Description) like '%' &lt;ins&gt; Trim(ToLower(SearchText)) &lt;/ins&gt; '%' or ToLower(Product.product_code) like '%' &lt;ins&gt; Trim(ToLower(SearchText)) &lt;/ins&gt; '%' )It is crucial to share the correct information, as most of us on the 1rst line are not technical.Additionally, while the workaround functions correctly, the customer is not fully satisfied since they have similar queries in multiple places. It would require extra effort to replace all instances. Could you provide an ETA that we can communicate to the customer?_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_July 25  4:46 PM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
------------------------------------------------ This notification was sent from Zendesk Support ticket #3037710 to all linked JIRA issues by Ricardo Moreira. --**Update to R&amp;D**Hello Team,
The workaround you provided works; however, please note that when sharing such queries, you should use double quotes instead of single quotes to avoid syntax errors.Trim(SearchText) = '' or ( ToLower(Product.Description) like '%'  Trim(ToLower(SearchText))  '%' or ToLower(Product.product_code) like '%'  Trim(ToLower(SearchText))  '%' )It is crucial to share the correct information, as most of us on the 1rst line are not technical.Additionally, while the workaround functions correctly, the customer is not fully satisfied since they have similar queries in multiple places. It would require extra effort to replace all instances. Could you provide an ETA that we can communicate to the customer?__
July 25  5:18 PM WESTwebVasco GomesSend ZenDesk private comment has been set: Noted about the quotes issue.The bugfix consists in 2 changes :&nbsp;*   The 1st change is already done and is already progressing through the rings. Depending on the pipelines (that we do not control) we expect it to be in GA one week from now.&nbsp;
*   The 2nd change can only be done when the 1st change reaches GA. Once the implementation is done, it also has to progress through the rings.&nbsp;At this moment, a possible ETA (that is depending on the progression through the rings, so, it's assuming that everything runs as it should), could be that it will reach GA in 3 weeks.July 25  5:18 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Noted about the quotes issue.The bugfix consists in 2 changes :&nbsp;*   The 1st change is already done and is already progressing through the rings. Depending on the pipelines (that we do not control) we expect it to be in GA one week from now.&nbsp;
*   The 2nd change can only be done when the 1st change reaches GA. Once the implementation is done, it also has to progress through the rings.&nbsp;At this moment, a possible ETA (that is depending on the progression through the rings, so, it's assuming that everything runs as it should), could be that it will reach GA in 3 weeks.
July 25  5:18 PM WESTwebRootlySend ZenDesk private comment has been unsetJuly 25  5:18 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

August 2 10:10 AM WESTwebRootly
The Global Support team marked this incident as closed in ZenDesk.
August 2 10:10 AM WESTwebRootly
Incident has been resolved
August 2 10:10 AM WESTwebRootlyZenDesk Event Type has been set: solvedAugust 2 12:51 PM WESTwebVasco Gomes
Incident has been started
August 2 12:51 PM WESTwebVasco Gomes
Summary has been changed to 

&nbsp;&nbsp;&nbsp;&nbsp;
I'm re-opening this, since, although the workaround worked, we are sill waiting for the Query Engine fix to reach GA (it's currently in EA), and after that Data Fabric Clients team as to go ahead with their changes also. 

We believe that this incident should be kept open because of it.
&nbsp;&nbsp;
&nbsp;&nbsp;**R&amp;D ESCALATION FORM**
Section comments can be removed for R&amp;D easier interpretation.
&nbsp;&nbsp;
&nbsp;&nbsp;**ISSUE DESCRIPTION AND HOW TO REPRODUCE**
We have a customer trying to migrate to ODC from O11, and they are having problem with a somewhat complicated aggregate filter that they use throughout their application that works fine in O11, but throws an unusual error in ODC.
&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;If(Trim(SearchText)=NullTextIdentifier() or Length(Trim(SearchText))=0 ,True,Index(ToLower(products.product_code),Trim(ToLower(SearchText)))&lt;&gt;-1 orIndex(ToLower(products.description),Trim(ToLower(SearchText)))&lt;&gt;-1)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;
&nbsp;&nbsp;
Their database is case-sensitive, so they need the ToLower. Success suggested adjusting the code so that the Trim and ToLower on SearchText is done before the aggregate is called, but they claim this would be a lot of work based on how often this pattern is used in their app.
&nbsp;&nbsp;
Upon escalating to R&amp;D channels, [https://outsystems.slack.com/archives/C061TN1GW/p1721655551306919](https://outsystems.slack.com/archives/C061TN1GW/p1721655551306919), we were advised by Hugo to analyze why there is an actual error rather than a &ldquo;slow query&rdquo;.  It&rsquo;s not supposed to throw an error preparing the statement.
&nbsp;&nbsp;
&nbsp;&nbsp;**IMPACT ON THE CUSTOMER**
Their database is case-sensitive, so they need the ToLower. The customer insisted this is a sev2 however, it seems that a valid workaround was shared, they just don't want to optimize. So we're putting this as sev3
&nbsp;&nbsp;
&nbsp;&nbsp;**TROUBLESHOOTING STEPS &amp; WORKAROUND**
N/A
&nbsp;&nbsp;
&nbsp;&nbsp;**TECH DATA OR ANY OTHER RELEVANT INFO**
Ring: ga

Tenant Id: 6c875ad1-c24a-40d3-93bf-59a76e094051

Tenant Prefix: mitchell

Region: us-east-1

Q5F.K8I.OZ2.AM6.2PA.NZN.2W2.WIZ
&nbsp;&nbsp;
&nbsp;&nbsp;*&lt;! do not remove this line, this will be used to the trigger* Technical Support::Send to R&amp;D - ODC *#trigger_send_to_r&amp;d_odc !&gt;*&nbsp;&nbsp;
&nbsp;&nbsp;
Attachment(s):

image (24).png - [https://supportoutsystems.zendesk.com/attachments/token/XbpIMV4YncP37jWE3XidWUe4A/?name=image+%2824%29.png](https://supportoutsystems.zendesk.com/attachments/token/XbpIMV4YncP37jWE3XidWUe4A/?name=image+%2824%29.png)&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;August 14 11:49 AM WESTwebVasco GomesSend ZenDesk private comment has been set: Hello Team!  
I just wanted to share that the reported problem was fixed and the fix is in GA (from both teams).&nbsp;  
Can you please confirm with the customer that the problem is solved?  Thank you!August 14 11:49 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hello Team!  
I just wanted to share that the reported problem was fixed and the fix is in GA (from both teams).&nbsp;  
Can you please confirm with the customer that the problem is solved?  Thank you!
August 14 11:49 AM WESTwebRootlySend ZenDesk private comment has been unsetAugust 14 11:49 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

August 21 10:04 AM WESTwebVasco GomesSend ZenDesk private comment has been set: Is there any news regarding this? The fix is already in GA. Was the client able to confirm that everything was fixed?August 21 10:04 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

Is there any news regarding this? The fix is already in GA. Was the client able to confirm that everything was fixed?August 21 10:04 AM WESTwebRootlySend ZenDesk private comment has been unsetAugust 21 10:04 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

August 21 11:43 AM WESTwebRootlyZendesk Private Comment has been changed to: ----------------------------------------------**Update to R&amp;D**
Hello teamUnfortunately, the customer does not reply to our e-mails or answer our calls.
So we can't get a confirmation from the customer, our apologies.We'll proceed with the closure of the ticket. Thank you once again for your patience.Regards,_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_August 21 11:43 AM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
Hello teamUnfortunately, the customer does not reply to our e-mails or answer our calls.
So we can't get a confirmation from the customer, our apologies.We'll proceed with the closure of the ticket. Thank you once again for your patience.Regards,__
August 21 11:44 AM WESTwebRootly
Incident has been resolved
August 21 11:44 AM WESTwebRootly
The Global Support team marked this incident as closed in ZenDesk.