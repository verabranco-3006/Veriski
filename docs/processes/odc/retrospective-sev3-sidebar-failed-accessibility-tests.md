---
title: Retrospective-SEV3-Sidebar failed accessibility tests
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4356636719/Retrospective-SEV3-Sidebar+failed+accessibility+tests
confluence_space: RKB
confluence_page_id: 4356636719
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV3-Sidebar failed accessibility tests

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV3

Teams:&nbsp;trueBlueUi Components
#### 🕐 Timestamps
Started At:&nbsp;trueBlueJuly 29 12:44 PM WEST

Mitigated At:&nbsp;trueYellowAugust 13  8:14 AM WEST

Resolved At:&nbsp;trueGreenAugust 13  8:14 AM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/768-sidebar-failed-accessibility-tests)
[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3035222)

#### 🧑&zwj;🚒 Incident Rolestrue
**Commander**

Gon&ccedil;alo Martins

**Engineer**

Giuliana Silva
#### Summary
----------------------------------------------**CONSIDERATIONS BEFORE PERFORMING THE ESCALATION TO R&amp;D (MANDATORY)**None of the below points should be overlooked. Failure to do so may imply unnecessary effort.* * *
Ensure the ticket has been **categorized**, otherwise, the R&amp;D escalation will go unnoticed and not be worked on!**1.** For **Incidents**, the **IMAX** was consulted **beforehand** on which:- No incident models were found for the reported symptoms **OR**
- The incident model did not solve the issue **OR**
- The next step indicated in the Incident Model is an escalation to R&amp;D.
**2.** For **Questions**, the ChatODC on the **Slack channel** didn't return an acceptable answer.
**3.** Any other requests that explicitly indicate an R&amp;D escalation is needed.
**4**. **Incident impact assessment** was based on the **prioritization scoring matrix**.* * ***R&amp;D ESCALATION FORM**
Customer is reporting that when using tab navigation for sidebar elements some of their widgets are being skipped. Checking the DOM shows that the slider element is set as tabindex=-1 so it's expected that the tab behavior would skip it. However we need to know what is expected in this case.![](https://supportoutsystems.zendesk.com/attachments/token/O0bYgTeyBa3lXNmizubEwiIVJ/?name=image.png)Customer reports that in their app there are multiple elements that cannot be reliably tabbed into. For the slider it is skipped over when its attempted to be tabbed to. When setting the tabindex=0 you can with the keyboard tab to the slider and manipulate it with the keyboard.For this case the page is public facing and the use would like to be able to tab to each element and interact with it via keyboard.**ISSUE DESCRIPTION AND HOW TO REPRODUCE**
Navigating to the page https://ilr-test.outsystems.app/SmartCompare/Dashboard and clicking the conditions in the middle of the page. Choosing the button on the right &quot;Plus de Filtres&quot;of the page to open the sidebar. At this point you should try to tab through each menu item. The checkboxes can be chosen but other items will be skipped.**IMPACT ON THE CUSTOMER**
Brief description of the impact on the customer/development team/other, including:
- Stage where the problem is happening (Development / QA / Production); TEST
- Frequency of the problem; When interacting with the sidebar
- Business impact or/and development impact; Customer needs our help in implementing their patterns so that they will pass accessibility testing.**TROUBLESHOOTING STEPS &amp; WORKAROUND**
- What are the most relevant findings and hypotheses from our analysis so far?
After testing this behavior we noticed that certain widgets are not able to be tabbed to while others are.
- What workaround was tried so far, if any, and how did they impact the reported behavior?
We have verified that when changing the dom for tabindex=-1 to tabindex=0 it's possible to tab through the widgets in their natural order.
- Was this case discussed previously with anyone from R&amp;D? If so with whom and which R&amp;D team?
No
- If it is related, or there is a possibility of being related, to an already existing RDINC, please specify it.**TECH DATA OR ANY OTHER RELEVANT INFO**
- Tenant ID or Activation Code where the problem is occurring.
615db0f9-40a9-4e65-94f1-0bc57e28b22b
- OutSystems revisions of the components involved (mandatory). This includes for example revision of ODC Studio or Forge Supported Plugins.- Diagnostics report (mandatory for ODC Studio-related issues).- All technical files or data, including OMLs.
SmartCompare.oml
- Error stacks, screenshots, or any other files like error logs or traces._&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 RetrospectiveinfoDetails
**Ring:** ga
**System-wide impact:**&nbsp; 
**Tenant ID:** 615db0f9-40a9-4e65-94f1-0bc57e28b22b
**Tenant Prefix:** ilr
**Routing Error Code:** N/A
**Product Area:** Phoenix::Application Runtime::Starter Apps::OutSystems UI
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/768-sidebar-failed-accessibility-tests)

**Date**

**Source**

**User**

**Event**
July 26 11:24 PM WESTwebRootly
created an alert via
July 26 11:24 PM WESTwebRootly
Rootly created this incident
July 26 11:24 PM WESTwebRootly
In triage date has been set to July 26 11:24 PM WEST
July 26 11:34 PM WESTwebRootly
This incident was instantiated in Jira: RDINC-27718. Please work the incident using Rootly
July 27 12:24 AM WESTwebRootly
This incident was instantiated in Jira: RDINC-27718. Please work the incident using Rootly
July 29 12:06 PM WESTwebGon&ccedil;alo MartinsGon&ccedil;alo Martins has been assigned as CommanderJuly 29 12:06 PM WESTwebGon&ccedil;alo MartinsGiuliana has been assigned as EngineerJuly 29 12:44 PM WESTwebBernardo Cardoso
Incident has been started
August 13  8:14 AM WESTwebRootly
Incident has been resolved
August 13  8:14 AM WESTwebRootlyZenDesk Event Type has been set: solvedAugust 13  8:14 AM WESTwebRootly
The Global Support team marked this incident as closed in ZenDesk.