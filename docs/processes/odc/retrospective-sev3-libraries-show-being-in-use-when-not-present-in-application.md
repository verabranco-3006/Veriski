---
title: Retrospective-SEV3-Libraries show being in use when not present in application.
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4331175996/Retrospective-SEV3-Libraries+show+being+in+use+when+not+present+in+application.
confluence_space: RKB
confluence_page_id: 4331175996
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV3-Libraries show being in use when not present in application.

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV3

Teams:&nbsp;trueBlueAlm Consoles
#### 🕐 Timestamps
Started At:&nbsp;trueBlueAugust 2  3:15 PM WEST

Mitigated At:&nbsp;trueYellowAugust 2  3:25 PM WEST

Resolved At:&nbsp;trueGreenAugust 2  3:25 PM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/755-libraries-show-being-in-use-when-not-present-in-application)
[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3038460)

#### Summary
----------------------------------------------**CONSIDERATIONS BEFORE PERFORMING THE ESCALATION TO R&amp;D (MANDATORY)**
None of the below points should be overlooked. Failure to do so may imply unnecessary effort.* * *
Ensure the ticket has been **categorized**, otherwise, the R&amp;D escalation will go unnoticed and not be worked on!**1.** For **Incidents**, the **IMAX** was consulted **beforehand** on which:- No incident models were found for the reported symptoms **OR**
- The incident model did not solve the issue **OR**
- The next step indicated in the Incident Model is an escalation to R&amp;D.
**2.** For **Questions**, the ChatODC on the **Slack channel** didn't return an acceptable answer.
**3.** Any other requests that explicitly indicate an R&amp;D escalation is needed.
**4**. **Incident impact assessment** was based on the **prioritization scoring matrix**.* * ***R&amp;D ESCALATION FORM**- Internal teammate Ricardo Cruz reports that it is not possible to remove a forge component from their application. I have attempt to recreate what is being reported using the same elements. When I added and removed the the same forge module it went away from the consumer list in my sample module. After checking customer application PORTAL in ODC studio we were unable to find any reference to the Forge component Session Timeout Warning. Only the cloned module is present in the app.
- ![](https://supportoutsystems.zendesk.com/attachments/token/jIINUpcMomEguBof1BTbYc6pe/?name=image.png)
- However if you check in the customer portal it shows that the app is still consumed.
- ![](https://supportoutsystems.zendesk.com/attachments/token/aZBIhiRt2RdhXxm67OR10hD12/?name=image.png)**ISSUE DESCRIPTION AND HOW TO REPRODUCE**
**Customer is reporting that libraries are shown as being used when they are not.**This behavior can happen in two scenarios:- The app or one of the consumed libraries was cloned and, at that moment, was consuming the forge component, which is the case of this incident.- The app is consuming a library that in turn consumes the forge component**IMPACT ON THE CUSTOMER**
Brief description of the impact on the customer/development team/other, including:
- Stage where the problem is happening (Development / QA / Production); Production
- Frequency of the problem; Intermittent
- Business impact or/and development impact; Causes libraries to be consumed when they are unneeded as the user has previously cloned library and stopped consuming methods from forge library**TROUBLESHOOTING STEPS &amp; WORKAROUND**
- What are the most relevant findings and hypotheses from our analysis so far? - This seems to be caused by - The app or one of the consumed libraries was cloned and, at that moment, was consuming the forge component, which is the case of this incident.
- The app is consuming a library that in turn consumes the forge component
- What workaround was tried so far, if any, and how did they impact the reported behavior? - none
- Was this case discussed previously with anyone from R&amp;D? If so with whom and which R&amp;D team? - no
- If it is related, or there is a possibility of being related, to an already existing RDINC, please specify it. RDINC-27340**TECH DATA OR ANY OTHER RELEVANT INFO**
- Tenant ID or Activation Code where the problem is occurring. **7a6b652e-728d-4329-a6f4-998aff1eb508 - CHU.8Z6.KIU.GFQ.3H3.OIO.X8F.AUT**
- OutSystems revisions of the components involved (mandatory). This includes for example revision of ODC Studio or Forge Supported Plugins.
- Diagnostics report (mandatory for ODC Studio-related issues).
- All technical files or data, including OMLs.
- Error stacks, screenshots, or any other files like error logs or traces.This case has been solved, we are just adding macro for rootly._&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 RetrospectiveinfoDetails
**Ring:** ga
**System-wide impact:**&nbsp; No
**Tenant ID:** 7a6b652e-728d-4329-a6f4-998aff1eb508
**Tenant Prefix:** wcra
**Routing Error Code:** N/A
**Product Area:** Phoenix::Phoenix Portal::Apps
### Impact:
On the ODC Portal the asset displays producers that no longer exist.
### Investigation and troubleshooting findings:
This was a known issue on the AVS service, which was already fixed on a new endpoints of /source-control/, however the Portal was still using the deprecated endpoints /applications/.
### Resolution:
On the Portal we switched to the new endpoint.
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/755-libraries-show-being-in-use-when-not-present-in-application)

**Date**

**Source**

**User**

**Event**
July 24  6:10 PM WESTwebRootly
created an alert via
July 24  6:10 PM WESTwebRootly
Rootly created this incident
July 24  6:10 PM WESTwebRootly
In triage date has been set to July 24  6:10 PM WEST
July 24  6:21 PM WESTwebRootly
This incident was instantiated in Jira: RDINC-27340. Please work the incident using Rootly
July 24  7:12 PM WESTwebRootly
This incident was instantiated in Jira: RDINC-27340. Please work the incident using Rootly
July 24  9:01 PM WESTwebRootlyZenDesk Event Type has been set: solvedJuly 24  9:01 PM WESTwebRootly
The Global Support team marked this incident as closed in ZenDesk.
August 2  3:15 PM WESTwebJo&atilde;o Ros&aacute;rio
Since the incident was resolved by using JIRA, we are closing the incident.
August 2  3:15 PM WESTwebJo&atilde;o Ros&aacute;rio
Incident has been started
August 2  3:25 PM WESTwebJo&atilde;o Ros&aacute;rio
Incident has been resolved
August 2  3:25 PM WESTwebJo&atilde;o Ros&aacute;rioSystem-wide impact has been set: NoAugust 2  3:25 PM WESTwebJo&atilde;o Ros&aacute;rioImpact has been set: On the ODC Portal the asset displays producers that no longer exist.August 2  3:25 PM WESTwebJo&atilde;o Ros&aacute;rioInvestigation and troubleshooting findings has been set: This was a known issue on the AVS service, which was already fixed on a new endpoints of /source-control/, however the Portal was still using the deprecated endpoints /applications/.August 2  3:25 PM WESTwebJo&atilde;o Ros&aacute;rioResolution has been set: On the Portal we switched to the new endpoint.