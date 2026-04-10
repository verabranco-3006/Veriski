---
title: Retrospective-SEV3-Publish fails with error OS-DPL-50205 for all devs, application can no longer be changed
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4333043982/Retrospective-SEV3-Publish+fails+with+error+OS-DPL-50205+for+all+devs+application+can+no+longer+be+changed
confluence_space: RKB
confluence_page_id: 4333043982
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV3-Publish fails with error OS-DPL-50205 for all devs, application can no longer be changed

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV3

Teams:&nbsp;trueBlueModel 
#### 🕐 Timestamps
Started At:&nbsp;trueBlueAugust 5 11:22 AM WEST

Mitigated At:&nbsp;trueYellowAugust 5 11:29 AM WEST

Resolved At:&nbsp;trueGreenAugust 5 11:29 AM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/803-publish-fails-with-error-os-dpl-50205-for-all-devs-application-can-no-longer-be-changed)
[Slack channel](https://slack.com/app_redirect?channel=C07FHCZ6YLS&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3043619)

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

Nuno Rego
#### Summary
----------------------------------------------**R&amp;D ESCALATION FORM****ISSUE DESCRIPTION AND HOW TO REPRODUCE**- The customer is unable to publish NABO_CS in ODC Studio because he is facing the following error:
**An internal server error occurred! (OS_BLD_COMP_50000)**
**An error has occurred while building the application (OS_DPL_50205)**
- Customer steps:&gt; We have tried the following with no success
&gt;
&gt; 1. Export the NABO_CS application .oml file (attached)
&gt;
&gt; 2. Delete NABO_CS application in ODC portal
&gt;
&gt; 3. Restart ODC Studio
&gt;
&gt; 4. Import NABO_CS
&gt;
&gt; 5. Publish NABO_CS
&gt;
&gt; The error still occurs
&gt;
&gt; We have also tried
&gt;
&gt; 1. Clone the NABO_CS application
&gt;
&gt; 2. Export the cloned application
&gt;
&gt; 3. Delete the NABO_CS application
&gt;
&gt; 4. Import the cloned application. Rename it to NABO Core.
&gt;
&gt; 5. Publish the cloned application
&gt;
&gt; The error still occurs. Also the cloned application still publishes as NABO_CS.
&gt;
&gt; Our workaround is as follows, however it has the downside that we lose all data from NABO_CS.
&gt;
&gt; 1. Create a new application NABO CS (a space instead of an underscore)
&gt;
&gt; 2. Copy everything from NABO_CS into NABO CS
&gt;
&gt; 3. Replace all dependencies (created by copying) from NABO_CS to entities internal to the new application NABO CS.
&gt;
&gt; 4. Publish the new application NABO CS.
&gt;
&gt; 5. Wire up dependent application to the new application NABO CS.- The same situation occurred in another application (Nabo_Test) which was later published upon the customer reverting the changes to a previous version, which is not the focus of this ticket![](https://supportoutsystems.zendesk.com/attachments/token/VSByeR0DtMO4Zc93dLHKhVijj/?name=image.png)
**IMPACT ON THE CUSTOMER**- It sometimes affects the Development work&gt; The impact this is having, is that when this issue does happen, we have to redo the work. Yesterday we lost all our data in the dev environment. Now that we realise this could continue happening, it will slow down our development velocity. Our project is on a tight deadline.**TROUBLESHOOTING STEPS &amp; WORKAROUND**- workaround described above by the customer with the downside of loosing data or reverting the changes by using a previous revision as the customer is already aware of.
- Still, there doesn't seem to be any plausible justification in regards to being unable to publish the NABO_CS application, which we were unable to publish in our sandbox
NABO_CS_revision4_lastrevision.oml
NABO CS_revision4_lastrevision.oml![](https://supportoutsystems.zendesk.com/attachments/token/DGrFpxbTx6lIc6ZDxGwYxizZv/?name=inlineImage.png)![](https://supportoutsystems.zendesk.com/attachments/token/tkxRuJOUxYhrhFkjRMyL9Pk8C/?name=inlineImage.png) ![](https://supportoutsystems.zendesk.com/attachments/token/luf4mmqh29Nh5qkOOUA9FCAW5/?name=inlineImage.png)- Additionally, we would like to share that the customer shared the following with us in regards to their app NABO_Test, which may be or may not be related:&gt; Also, it looks like there are sometimes error messages which are not immediately appearing in True Change until you click on the affected element.
&gt;
&gt; In the below screenshot we think the highlighted item is what caused the server build error.
&gt;
&gt; Can you confirm this is the issue?
&gt;
&gt; ![](https://www.outsystems.com/SupportPortal/DownloadAmazon.aspx?FileName=1722580505000__1722580502805.png&amp;TicketGUID=897ff663-3f8b-48d5-8c75-2e76d0a6be3a)**TECH DATA OR ANY OTHER RELEVANT INFO**
Ring: ga
Tenant Id: ccffb600-8cf6-4d37-a9c7-102aa19157f7
Tenant Prefix: knose
Region: ap-southeast-2
IEC.T30.4P9.L0C.44O.TH5.54D.FSX
support_level_8x5
Ends in 2027-06-23**Request to RD:** Why are we unable to publish the NABO_CS and what is the reason for the error to occur? Thank you_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 RetrospectiveinfoDetails
**Ring:** ga
**System-wide impact:**&nbsp; No
**Tenant ID:** ccffb600-8cf6-4d37-a9c7-102aa19157f7
**Tenant Prefix:** knose
**Routing Error Code:** OS-BLD-COMP
**Product Area:** -
### Impact:
Customer was unable to publish
### Investigation and troubleshooting findings:
Corrupt model
### Resolution:
Recreate 'Execute Server Action' node.
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/803-publish-fails-with-error-os-dpl-50205-for-all-devs-application-can-no-longer-be-changed)

**Date**

**Source**

**User**

**Event**
August 2  4:44 PM WESTwebRootly
created an alert via
August 2  4:44 PM WESTwebRootly
Rootly created this incident
August 2  4:44 PM WESTwebRootly
In triage date has been set to August 2  4:44 PM WEST
August 2  5:44 PM WESTwebRootly
This incident was instantiated in Jira: RDINC-27992. Please work the incident using Rootly
August 5 11:21 AM WESTwebNuno Rego
Teams has been added: Model 
August 5 11:21 AM WESTwebNuno Rego
Teams has been removed: BuildServices
August 5 11:22 AM WESTwebNuno RegoNuno Rego has been assigned as EngineerAugust 5 11:22 AM WESTwebNuno Rego
Incident has been started
August 5 11:23 AM WESTwebRootly[Slack Channel](https://slack.com/app_redirect?channel=C07FHCZ6YLS&amp;team=T041063TZ) has been createdAugust 5 11:29 AM WESTwebNuno Rego
Incident has been resolved
August 5 11:29 AM WESTwebNuno RegoSystem-wide impact has been set: NoAugust 5 11:29 AM WESTwebNuno RegoImpact has been set: Customer was unable to publishAugust 5 11:29 AM WESTwebNuno RegoInvestigation and troubleshooting findings has been set: Corrupt modelAugust 5 11:29 AM WESTwebNuno RegoResolution has been set: Recreate 'Execute Server Action' node.