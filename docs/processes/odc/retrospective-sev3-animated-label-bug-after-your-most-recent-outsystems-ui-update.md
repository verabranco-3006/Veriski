---
title: Retrospective-SEV3-Animated Label Bug after your most recent Outsystems UI update
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4262756416/Retrospective-SEV3-Animated+Label+Bug+after+your+most+recent+Outsystems+UI+update
confluence_space: RKB
confluence_page_id: 4262756416
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV3-Animated Label Bug after your most recent Outsystems UI update

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV3

Teams:&nbsp;trueBlueUi Components
#### 🕐 Timestamps
Started At:&nbsp;trueBlueJuly 3 10:00 PM WEST

Mitigated At:&nbsp;trueYellowJuly 3 10:02 PM WEST

Resolved At:&nbsp;trueGreenJuly 3 10:02 PM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/665-animated-label-bug-after-your-most-recent-outsystems-ui-update)
[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3029414)

#### 🧑&zwj;🚒 Incident Rolestrue
**Commander**

Gon&ccedil;alo Martins

**Engineer**

Bernardo Cardoso
#### Summary
----------------------------------------------**ISSUE DESCRIPTION AND HOW TO REPRODUCE:**- The client reported the following:- _Hey there, I found a bug in the recent OutSystems UI library update. After approving the update, I noticed that labels in drop-down fields were not active on the initial page load. I managed to fix it by adjusting the logic. The labels are not active anymore if they are already populated. Check out the video for more details and please investigate the issue further_:- https://www.loom.com/share/67a6b3afec25419991d75b1eb92c63da- https://www.loom.com/share/cfd1f59606bb46069cbe5b62ebf6736c- https://www.loom.com/share/174becd0b3434d3c85d51f616cb5acbd**IMPACT ON THE CUSTOMER**
Brief description of the impact on the customer/development team/other, including:- Stage where the problem is happening (Development / QA / Production);- Development Stage
- Frequency of the problem:- Frequent.
- Business impact or/and development impact:- This is delaying their development activity**TROUBLESHOOTING STEPS &amp; WORKAROUND:**- What are the most relevant findings and hypotheses from our analysis so far?- The client provided the following videos explaining the issue and their workaround:- https://www.loom.com/share/67a6b3afec25419991d75b1eb92c63da- https://www.loom.com/share/cfd1f59606bb46069cbe5b62ebf6736c- https://www.loom.com/share/174becd0b3434d3c85d51f616cb5acbd
- What workaround was tried so far, if any, and how did they impact the reported behavior?- No workaround has been implemented on our end. However, the client did provide the following explanation for their workaround:- https://www.loom.com/share/174becd0b3434d3c85d51f616cb5acbd- The client was able to create a simple app showcasing the issue:- https://dlmc-dev.outsystems.app/Consulting/Screen1- Furthermore, we were able to reproduce the issue internally:- https://gs-sandbox-ga-eu-01-dev.outsystems.app/AnimatedLabelBug/Screen1?_ts=638554515052545076
- Was this case discussed previously with anyone from R&amp;D? If so with whom and which R&amp;D team?- No.
- If it is related, or there is a possibility of being related, to an already existing RDINC, please specify it.- Might be related to RDINC-22670. However, this also seems related to ROU-4903/RPM-4946.**TECH DATA OR ANY OTHER RELEVANT INFO:**- Tenant ID or Activation Code where the problem is occurring:- 92b1e03a-6049-4312-8099-b1ba91765f23
- OutSystems revisions of the components involved (mandatory). This includes for example revision of ODC Studio or Forge Supported Plugins.- OutSystems UI to version 2.19.1
- Diagnostics report (mandatory for ODC Studio-related issues).- N/A
- All technical files or data, including OMLs.- Test application to reproduce the issue:- https://gs-sandbox-ga-eu-01-dev.outsystems.app/AnimatedLabelBug/Screen1?_ts=638554515052545076- Simple application from the client:- https://dlmc-dev.outsystems.app/Consulting/Screen1
- Error stacks, screenshots, or any other files like error logs or traces.- N/A_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 RetrospectiveinfoDetails
**Ring:** ga
**System-wide impact:**&nbsp; No
**Tenant ID:** 92b1e03a-6049-4312-8099-b1ba91765f23
**Tenant Prefix:** dlmc
**Routing Error Code:** N/A
**Product Area:** Phoenix::Application Runtime::Starter Apps::OutSystems UI
### Impact:
Only UI when having Animated Labels on prefilled inputs. 

No functionality is lost, only a visual issue.
### Investigation and troubleshooting findings:### Resolution:
This was already known since it was detected in O11 (and on a forum post), being already fixed under the task code ROU-10851 and will be included in the next release 2.19.2 - no ETA at this moment we can share.
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/665-animated-label-bug-after-your-most-recent-outsystems-ui-update)

**Date**

**Source**

**User**

**Event**
July 3  8:32 PM WESTwebRootly
created an alert via
July 3  8:32 PM WESTwebRootly
Rootly created this incident
July 3  8:32 PM WESTwebRootly
In triage date has been set to July 3  8:32 PM WEST
July 3  8:42 PM WESTwebRootly
This incident was instantiated in Jira: RDINC-26406. Please work the incident using Rootly
July 3  9:32 PM WESTwebRootly
This incident was instantiated in Jira: RDINC-26406. Please work the incident using Rootly
July 3  9:56 PM WESTwebGon&ccedil;alo MartinsGon&ccedil;alo Martins has been assigned as CommanderJuly 3  9:56 PM WESTwebGon&ccedil;alo MartinsBernardo Cardoso has been assigned as EngineerJuly 3 10:00 PM WESTwebGon&ccedil;alo Martins
Incident has been started
July 3 10:00 PM WESTwebGon&ccedil;alo Martins
This was already known since it was detected in O11 (and on a forum post), being already fixed under the task code ROU-10851 and will be included in the next release 2.19.2 - no ETA at this moment we can share.
July 3 10:02 PM WESTwebGon&ccedil;alo Martins
Incident has been resolved
July 3 10:02 PM WESTwebGon&ccedil;alo MartinsSystem-wide impact has been set: NoJuly 3 10:02 PM WESTwebGon&ccedil;alo MartinsImpact has been set: Only UI when having Animated Labels on prefilled inputs. 
No functionality is lost, only a visual issue.July 3 10:02 PM WESTwebGon&ccedil;alo MartinsResolution has been set: This was already known since it was detected in O11 (and on a forum post), being already fixed under the task code ROU-10851 and will be included in the next release 2.19.2 - no ETA at this moment we can share.