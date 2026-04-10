---
title: Retrospective-SEV3-OS-BERT-00000 error is occurring again
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4336910364/Retrospective-SEV3-OS-BERT-00000+error+is+occurring+again
confluence_space: RKB
confluence_page_id: 4336910364
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV3-OS-BERT-00000 error is occurring again

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV3

Teams:&nbsp;trueBlueRuntime Data Model
#### 🕐 Timestamps
Started At:&nbsp;trueBlueAugust 6 10:17 AM WEST

Mitigated At:&nbsp;trueYellowAugust 6 10:21 AM WEST

Resolved At:&nbsp;trueGreenAugust 6 10:21 AM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/619-os-bert-00000-error-is-occurring-again)
[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3025270)

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
- A paragraph detailing the issue or question.
Customer reporting that they are facing error (**OS-BERT-00000 - 23505: duplicate key value violates unique constraint &quot;osprk_5jzhxn3ymx8_story_sjm03_b1bse27v9s90i40yt5&quot;**
) We have stated that this was fixed in RDINC-23756
- If available, the steps that must be taken to reproduce the issue under discussion.**Steps to replicate**
**Go to Sizing Made Easy app in TEST, click &quot;My BPI&quot; app, and then click on Calculate. - However currently user says reproduction is not predictable. ****IMPACT ON THE CUSTOMER**
Brief description of the impact on the customer/development team/other, including:
- Stage where the problem is happening (Development);
- Frequency of the problem; - not currently able to reproduce.
- Business impact or/and development impact; **User is from Outsystems Professional Services and has not been able to deploy changes to production or demo their app. ****TROUBLESHOOTING STEPS &amp; WORKAROUND**
- What are the most relevant findings and hypotheses from our analysis so far?
The issue was reported as fixed in **RDMMS version with the fix (v3.7.11) has been deployed in ring OSALL (+1);**
- What workaround was tried so far, if any, and how did they impact the reported behavior? - **We suggested that the user insert create dummy records to overcome this issue. This was to ensure that the entities sequences are recreated, however in this case it was not successful. **
- Was this case discussed previously with anyone from R&amp;D? If so with whom and which R&amp;D team? - NO - However there was an escalation previously RDINC-18836
- If it is related, or there is a possibility of being related, to an already existing RDINC, please specify it. YES https://outsystemsrd.atlassian.net/browse/RDINC-18836**TECH DATA OR ANY OTHER RELEVANT INFO**
- Tenant ID or Activation Code where the problem is occurring. - 82efc85c-94e8-4bd7-a0cd-c0dd0f558e6a
- OutSystems revisions of the components involved (mandatory). This includes for example revision of ODC Studio or Forge Supported Plugins.
- Diagnostics report (mandatory for ODC Studio-related issues).
- All technical files or data, including OMLs. App Sizing Made Easy.oml
- Error stacks, screenshots, or any other files like error logs or traces.
Grafana dashboard
https://outsystems.grafana.net/explore?schemaVersion=1&amp;panes=%7B%22b2u%22:%7B%22datasource%22:%22grafanacloud-outsystemstest-traces%22,%22queries%22:%5B%7B%22refId%22:%22A%22,%22datasource%22:%7B%22type%22:%22tempo%22,%22uid%22:%22grafanacloud-outsystemstest-traces%22%7D,%22queryType%22:%22traceql%22,%22limit%22:20,%22tableType%22:%22traces%22,%22query%22:%226bb3eb48d9b1f81dea839b1e11af4675%5Cr%5Cn%22%7D%5D,%22range%22:%7B%22from%22:%22now-24h%22,%22to%22:%22now%22%7D,%22panelsState%22:%7B%22logs%22:%7B%22id%22:%22A_1717510301443409700_dd25bafe%22,%22visualisationType%22:%22logs%22%7D%7D%7D%7D&amp;orgId=1
_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 RetrospectiveinfoDetails
**Ring:** ea
**System-wide impact:**&nbsp; No
**Tenant ID:** 82efc85c-94e8-4bd7-a0cd-c0dd0f558e6a
**Tenant Prefix:** professionalservices
**Routing Error Code:** OS-BERT
**Product Area:** -
### Impact:
Customer facing runtime error indicating the record being inserted was violating a constraint (incorrectly).
### Investigation and troubleshooting findings:
More details can be found in this comment: [https://outsystemsrd.atlassian.net/browse/RDINC-23734?focusedCommentId=1134182](https://outsystemsrd.atlassian.net/browse/RDINC-23734?focusedCommentId=1134182)
### Resolution:
We provided a workaround for the customer and deployed a fix.

More information here: [https://outsystemsrd.atlassian.net/browse/RDINC-23734?focusedCommentId=1134182](https://outsystemsrd.atlassian.net/browse/RDINC-23734?focusedCommentId=1134182)
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/619-os-bert-00000-error-is-occurring-again)

**Date**

**Source**

**User**

**Event**
June 24  9:54 PM WESTwebRootly
created an alert via
June 24  9:54 PM WESTwebRootly
Rootly created this incident
June 24  9:54 PM WESTwebRootly
In triage date has been set to June 24  9:54 PM WEST
June 27  2:50 PM WESTwebRootlyZenDesk Event Type has been set: solvedJune 27  2:50 PM WESTwebRootly
The Global Support team marked this incident as closed in ZenDesk.
August 5  1:57 PM WESTwebRui Garcia
Moving to RDM. Already handled and solved here: https://outsystemsrd.atlassian.net/browse/RDINC-25710
August 5  1:58 PM WESTwebRui Garcia
Teams has been added: RuntimeDataModel
August 5  1:58 PM WESTwebRui Garcia
Teams has been removed: Backend Runtime
August 6 10:16 AM WESTwebMariana Cabeda
Will need to mark the issue as active to then mark it as closed.
The incident has been handled and closed through Jira, as previously linked in the timeline.
August 6 10:17 AM WESTwebMariana Cabeda
Incident has been started
August 6 10:21 AM WESTwebMariana Cabeda
Incident has been resolved
August 6 10:21 AM WESTwebMariana CabedaSystem-wide impact has been set: NoAugust 6 10:21 AM WESTwebMariana CabedaImpact has been set: Customer facing runtime error indicating the record being inserted was violating a constraint (incorrectly).August 6 10:21 AM WESTwebMariana CabedaInvestigation and troubleshooting findings has been set: More details can be found in this comment: https://outsystemsrd.atlassian.net/browse/RDINC-23734?focusedCommentId=1134182August 6 10:21 AM WESTwebMariana CabedaResolution has been set: We provided a workaround for the customer and deployed a fix.
More information here: https://outsystemsrd.atlassian.net/browse/RDINC-23734?focusedCommentId=1134182