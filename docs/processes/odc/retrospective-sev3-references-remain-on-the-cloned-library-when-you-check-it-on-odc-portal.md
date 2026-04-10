---
title: Retrospective-SEV3-References remain on the cloned library when you check it on ODC portal.
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4286808158/Retrospective-SEV3-References+remain+on+the+cloned+library+when+you+check+it+on+ODC+portal.
confluence_space: RKB
confluence_page_id: 4286808158
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV3-References remain on the cloned library when you check it on ODC portal.

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV3

Teams:&nbsp;trueBlueNeo Platform Theseus
#### 🕐 Timestamps
Started At:&nbsp;trueBlueJuly 16 10:30 AM WEST

Mitigated At:&nbsp;trueYellowJuly 16 10:33 AM WEST

Resolved At:&nbsp;trueGreenJuly 16 10:33 AM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/627-references-remain-on-the-cloned-library-when-you-check-it-on-odc-portal)
[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3027421)

#### 🧑&zwj;🚒 Incident Rolestrue
**Stakeholder**

Rodrigo Silva

**Engineer**

Miguel Piedade
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
- The customer reported an unexpected behaviour happening when they cloned a library. The cloned library is showing that they have a reference when the cloned library shouldn't have any references as it is not referenced by any app.**IMPACT ON THE CUSTOMER**
Brief description of the impact on the customer/development team/other, including:
- This issue was actually escalated to R&amp;D and solved in JIRA https://outsystemsrd.atlassian.net/browse/RDINC-24478, and it is only causing a visual impact.**TROUBLESHOOTING STEPS &amp; WORKAROUND**
- We are reaching out to R&amp;D to request if the side effects of the ghost reference on the ODC portal can be improved?**TECH DATA OR ANY OTHER RELEVANT INFO**
**Sumitomo Heavy Industries, Ltd.**
Ring: ga
Tenant Id: d3a0f377-08a9-45e5-8693-9c0e37455e3d
Tenant Prefix: shi
Region: ap-northeast-1
20G.WGX.9A2.9PZ.FYO.FW6.GUY.HXE_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 RetrospectiveinfoDetails
**Ring:** ga
**System-wide impact:**&nbsp; No
**Tenant ID:** d3a0f377-08a9-45e5-8693-9c0e37455e3d
**Tenant Prefix:** shi
**Routing Error Code:** N/A
**Product Area:** Phoenix::Phoenix Portal::External Logic
### Impact:
Customer got bad information on the Portal
### Investigation and troubleshooting findings:
When we clone libs the public elements maintained the same keys.
### Resolution:
The SQL query was fixed in AVS
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/627-references-remain-on-the-cloned-library-when-you-check-it-on-odc-portal)

**Date**

**Source**

**User**

**Event**
June 26 10:38 AM WESTwebRootly
created an alert via
June 26 10:38 AM WESTwebRootly
Rootly created this incident
June 26 10:38 AM WESTwebRootly
In triage date has been set to June 26 10:38 AM WEST
June 27 10:08 AM WESTwebRootlyZendesk Private Comment has been set: ----------------------------------------------**Update to R&amp;D**
- Detail additional findings or any questions/concerns that may be important for R&amp;D to be aware of.
Hi Team,Our SA Satoru Yamaguchi confirmed that the issue still persists.Here is the screen recording of the issue in his SA ODC Demo environment.- IssueOfLibraryReference.mp4Looking forward to your update.Thanks in advance,__June 27 10:08 AM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:

June 28  4:20 PM WESTwebRodrigo Silva
Teams has been added: Neo Platform Theseus
June 28  4:20 PM WESTwebRodrigo SilvaRodrigo Silva has been assigned as StakeholderJuly 16 10:30 AM WESTwebRodrigo SilvaMiguel Piedade has been assigned as EngineerJuly 16 10:30 AM WESTwebRodrigo Silva
Incident has been started
July 16 10:33 AM WESTwebRodrigo Silva
Incident has been resolved
July 16 10:33 AM WESTwebRodrigo Silva
Severity has been changed to SEV3
July 16 10:33 AM WESTwebRodrigo SilvaSystem-wide impact has been set: NoJuly 16 10:33 AM WESTwebRodrigo SilvaImpact has been set: Customer got bad information on the PortalJuly 16 10:33 AM WESTwebRodrigo SilvaInvestigation and troubleshooting findings has been set: When we clone libs the public elements maintained the same keys.July 16 10:33 AM WESTwebRodrigo SilvaResolution has been set: The SQL query was fixed in AVS