---
title: Retrospective-SEV3-Unable to rename attributes in entities - ODC
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4272030018/Retrospective-SEV3-Unable+to+rename+attributes+in+entities+-+ODC
confluence_space: RKB
confluence_page_id: 4272030018
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV3-Unable to rename attributes in entities - ODC

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV3

Teams:&nbsp;trueBlueRuntime Data Model
#### 🕐 Timestamps
Started At:&nbsp;trueBlueJuly 9  4:30 PM WEST

Mitigated At:&nbsp;trueYellowJuly 9  4:32 PM WEST

Resolved At:&nbsp;trueGreenJuly 9  4:32 PM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/612-unable-to-rename-attributes-in-entities-odc)
[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3022014)

#### Summary
----------------------------------------------**CONSIDERATIONS BEFORE PERFORMING THE ESCALATION TO R&amp;D (MANDATORY)**
None of the below points should be overlooked. Failure to do so may imply unnecessary effort.* * *
Ensure the ticket has been **categorized**, otherwise, the R&amp;D escalation will go unnoticed and not be worked on!**1.** For **Incidents**, the **IMAX** was consulted **beforehand** on which:- No incident models were found for the reported symptoms **OR**
- The incident model did not solve the issue **OR**
- The next step indicated in the Incident Model is an escalation to R&amp;D.
**2.** For **Questions**, the ChatODC on the **Slack channel** didn't return an acceptable answer.
**3.** Any other requests that explicitly indicate an R&amp;D escalation is needed.
**4**. **Incident impact assessment** was based on the **prioritization scoring matrix**.* * ***R&amp;D ESCALATION FORM**
The issue involves an inability to reuse previously deleted attribute names due to database schema constraints in the ODC platform. The customer attempts to rename an attribute to a previously used name results in a deployment error, stating that reusing deleted attribute names is not supported.- We are aware of the RDINC-12233 referring this issue
- We have here additional comment and guidance after the customer came with an additional question- Can you provide the current status and any progress updates on the initiative related to RDINC-12233, which involves handling deleted attribute names?- Given that creating a new column results in data loss, what methods do you recommend for customers to safely copy and preserve data from a deleted column to a newly created column?**ISSUE DESCRIPTION AND HOW TO REPRODUCE**- Create an entity and add an attribute.
- Deploy the changes.
- Delete the attribute and deploy again.
- Attempt to reuse the deleted attribute's name and deploy, which triggers the error.**IMPACT ON THE CUSTOMER**
The issue occurs in the development stage, affecting the customer's ability to progress with application modifications. The problem arises frequently during schema changes.**TROUBLESHOOTING STEPS &amp; WORKAROUND**
Initial troubleshooting identified that this behavior is by design within the ODC platform, preventing attribute name reuse after deletion to avoid conflicts.A suggested workaround involves creating a new entity to bypass schema restrictions, but this leads to potential data loss.- **Previous Discussions Existence**: The support team already discussed with the R&amp;D team regarding ticket RDINC-12233 which addresses similar issues.
- Potentially related to RDINC-12233, awaiting confirmation on current status and any ongoing initiatives to address this limitationNow the customer is seeking some info concerning the two above mentioned questions.**TECH DATA OR ANY OTHER RELEVANT INFO**
Tenant Id: f0d67e99-3f25-4b54-8916-6c4ee8f3d54c
Tenant Prefix: np
Region: ap-southeast-2For reference:![](https://www.outsystems.com/SupportPortal/DownloadAmazon.aspx?FileName=1718235468000__1718235468009.png&amp;TicketGUID=bdb8d4aa-ed98-47c3-ba4a-d56aa197e909)_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 RetrospectiveinfoDetails
**Ring:** ga
**System-wide impact:**&nbsp; 
**Tenant ID:** f0d67e99-3f25-4b54-8916-6c4ee8f3d54c
**Tenant Prefix:** np
**Routing Error Code:** N/A
**Product Area:** Phoenix::Application Runtime::Database access::Entities
### Impact:
The client can't rename attributes but this was expected.
### Investigation and troubleshooting findings:### Resolution:
N/A
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/612-unable-to-rename-attributes-in-entities-odc)

**Date**

**Source**

**User**

**Event**
June 24  2:23 AM WESTwebRootly
created an alert via
June 24  2:23 AM WESTwebRootly
Rootly created this incident
June 24  2:23 AM WESTwebRootly
In triage date has been set to June 24  2:23 AM WEST
July 3  4:02 AM WESTwebRootlyZenDesk Event Type has been set: solvedJuly 3  4:02 AM WESTwebRootly
The Global Support team marked this incident as closed in ZenDesk.
July 9  4:30 PM WESTwebJoana Barradas
Incident has been started
July 9  4:32 PM WESTwebJoana Barradas
Incident has been resolved
July 9  4:32 PM WESTwebJoana BarradasImpact has been set: The client can't rename attributes but this was expected.July 9  4:32 PM WESTwebJoana BarradasResolution has been set: N/A