---
title: Retrospective-SEV4-AOs Counting
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4286513254/Retrospective-SEV4-AOs+Counting
confluence_space: RKB
confluence_page_id: 4286513254
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV4-AOs Counting

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV4

Teams:&nbsp;trueBlueNeo Platform Theseus
#### 🕐 Timestamps
Started At:&nbsp;trueBlueJuly 16 10:34 AM WEST

Mitigated At:&nbsp;trueYellowJuly 16 10:38 AM WEST

Resolved At:&nbsp;trueGreenJuly 16 10:38 AM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/558-aos-counting)
[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3021334)

#### 🧑&zwj;🚒 Incident Rolestrue
**Stakeholder**

Rodrigo Silva

**Engineer**

Guilherme Rolo
#### Summary
----------------------------------------------**CONSIDERATIONS BEFORE PERFORMING THE ESCALATION TO R&amp;D (MANDATORY)**
None of the below points should be overlooked. Failure to do so may imply unnecessary effort.* * *
Ensure the ticket has been **categorized**, otherwise, the R&amp;D escalation will go unnoticed and not be worked on!**1.** For **Incidents**, the **IMAX** was consulted **beforehand** on which:- No incident models were found for the reported symptoms **OR**
- The incident model did not solve the issue **OR**
- The next step indicated in the Incident Model is an escalation to R&amp;D.
**2.** For **Questions**, the ChatODC on the **Slack channel** didn't return an acceptable answer.
**3.** Any other requests that explicitly indicate an R&amp;D escalation is needed.
**4**. **Incident impact assessment** was based on the **prioritization scoring matrix**.* * ***R&amp;D ESCALATION FORM**
Section comments can be removed for R&amp;D easier interpretation.**ISSUE DESCRIPTION AND HOW TO REPRODUCE**- They want to understand why the AO count increases from what was shown on 4th June to what is shown on 10th June- Will attach the screenshot
- They have reviewed the code changes and configurations made during the mentioned period.
- They have verified that no new modules or significant functionalities have been added that would justify the increase.**IMPACT ON THE CUSTOMER**- They are unable to plan their development.**TROUBLESHOOTING STEPS &amp; WORKAROUND**
n/a**TECH DATA OR ANY OTHER RELEVANT INFO**
Ring: ga
Tenant Id: 6908339c-fc68-4824-92f4-581d0cd49d6d
Tenant Prefix: valentech
Region: us-east-1
SYG.MS2.N9D.JDW.VBZ.I66.WS0.LNS_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 RetrospectiveinfoDetails
**Ring:** ga
**System-wide impact:**&nbsp; No
**Tenant ID:** 6908339c-fc68-4824-92f4-581d0cd49d6d
**Tenant Prefix:** valentech
**Routing Error Code:** N/A
**Product Area:** Phoenix::Phoenix Portal::Subscription
### Impact:
Customer facing wrong number of AOs consumed
### Investigation and troubleshooting findings:
Customer inquired why the &quot;DataGrid&quot; Forge component was counting as AOs since they couldn't find the amount of AO's it consumes in Forge public website
### Resolution:
We just clarified that this component consumes 22 AOs and asked them to confirm it was ok, however the customer didn't reply anymore.
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/558-aos-counting)

**Date**

**Source**

**User**

**Event**
June 13  7:34 AM WESTwebRootly
created an alert via
June 13  7:34 AM WESTwebRootly
Rootly created this incident
June 13  7:34 AM WESTwebRootly
In triage date has been set to June 13  7:34 AM WEST
June 28  4:17 PM WESTwebRodrigo Silva
Teams has been added: Neo Platform Theseus
June 28  4:18 PM WESTwebRodrigo SilvaRodrigo Silva has been assigned as StakeholderJuly 5  1:03 AM WESTwebRootlyZenDesk Event Type has been set: solvedJuly 5  1:03 AM WESTwebRootly
The Global Support team marked this incident as closed in ZenDesk.
July 16 10:34 AM WESTwebRodrigo SilvaGuilherme Rolo has been assigned as EngineerJuly 16 10:34 AM WESTwebRodrigo Silva
Incident has been started
July 16 10:38 AM WESTwebRodrigo Silva
Incident has been resolved
July 16 10:38 AM WESTwebRodrigo SilvaSystem-wide impact has been set: NoJuly 16 10:38 AM WESTwebRodrigo SilvaImpact has been set: Customer facing wrong number of AOs consumedJuly 16 10:38 AM WESTwebRodrigo SilvaInvestigation and troubleshooting findings has been set: Customer inquired why the &quot;DataGrid&quot; Forge component was counting as AOs since they couldn't find the amount of AO's it consumes in Forge public websiteJuly 16 10:38 AM WESTwebRodrigo SilvaResolution has been set: We just clarified that this component consumes 22 AOs and asked them to confirm it was ok, however the customer didn't reply anymore.