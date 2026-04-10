---
title: Retrospective-SEV3-[ODC] Addressing the problem of the upper limit of the number of apps registered in Apps scope.
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4283138197/Retrospective-SEV3-+ODC+Addressing+the+problem+of+the+upper+limit+of+the+number+of+apps+registered+in+Apps+scope.
confluence_space: RKB
confluence_page_id: 4283138197
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV3-[ODC] Addressing the problem of the upper limit of the number of apps registered in Apps scope.

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV3

Teams:&nbsp;trueBlueOdc Governance
#### 🕐 Timestamps
Started At:&nbsp;trueBlueJuly 15 10:13 AM WEST

Mitigated At:&nbsp;trueYellowJuly 15 11:28 AM WEST

Resolved At:&nbsp;trueGreenJuly 15 11:28 AM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/670-odc-addressing-the-problem-of-the-upper-limit-of-the-number-of-apps-registered-in-apps-scope)
[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3031890)

#### Summary
----------------------------------------------**R&amp;D ESCALATION FORM****ISSUE DESCRIPTION AND HOW TO REPRODUCE**- Toyota reported us that they're unable to assign more than 10 app roles to their Organization users, which is something that they are used to do in O11 and they need for their current and future app management- error message: **You've reached the 10-role limit for the Apps scope. To assign a new role, unassign one first.****IMPACT ON THE CUSTOMER**- No apps in Prod but affecting their team planning/management**TROUBLESHOOTING STEPS &amp; WORKAROUND**- no workaround
- replicated the issue in global support sandbox![](https://supportoutsystems.zendesk.com/attachments/token/3DTsRrl3rq05zeEc1dbsb1xBt/?name=image.png)
- no reference for this currently in public doc- https://success.outsystems.com/documentation/outsystems_developer_cloud/user_management/roles/- https://success.outsystems.com/documentation/outsystems_developer_cloud/user_management/#organization-and-app-roles
- there is no further tickets with the same message on our side**TECH DATA OR ANY OTHER RELEVANT INFO****OutSystems Developer Cloud Platform **License
Ring: ga
Tenant Id: b3353abd-884b-4189-bf35-7b652186e3fd
Tenant Prefix: tico
Region: ap-northeast-1
RLH.ANE.3PQ.DRW.LHQ.KDM.PI0.WOU
support_level_8x5
Ends in 2025-03-31Thank you
_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 RetrospectiveinfoDetails
**Ring:** ga
**System-wide impact:**&nbsp; 
**Tenant ID:** b3353abd-884b-4189-bf35-7b652186e3fd
**Tenant Prefix:** tico
**Routing Error Code:** N/A
**Product Area:** Phoenix::Phoenix Portal::Users &amp; access - Users
### Impact:
Expectable user experience. Not being able to assign more than 10 org app roles. 
### Investigation and troubleshooting findings:### Resolution:
Updated the documentation
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/670-odc-addressing-the-problem-of-the-upper-limit-of-the-number-of-apps-registered-in-apps-scope)

**Date**

**Source**

**User**

**Event**
July 4  2:41 PM WESTwebRootly
created an alert via
July 4  2:41 PM WESTwebRootly
Rootly created this incident
July 4  2:41 PM WESTwebRootly
In triage date has been set to July 4  2:41 PM WEST
July 15 10:13 AM WESTwebCatarina Gon&ccedil;alves
Incident has been started
July 15 11:23 AM WESTwebCatarina Gon&ccedil;alvesSend ZenDesk private comment has been set: Thank you for bringing this to our attention and informing us that this limitation is not documented in the public documentation.With 11 app roles, it is possible to reach a limit that we have atm. More details can be found at this confluence page [https://outsystemsrd.atlassian.net/wiki/spaces/RDSD/pages/3602219326/Maximum+roles+per+user](https://outsystemsrd.atlassian.net/wiki/spaces/RDSD/pages/3602219326/Maximum+roles+per+user)We will request an update to the public documentation to include information about the 10 app roles limitation.For internal use, please note that this is the link to the VM that will unlock this limitation:  
[https://outsystemsrd.atlassian.net/browse/RPOR-19956](https://outsystemsrd.atlassian.net/browse/RPOR-19956)  
The support team can monitor this link to know when the limitation will no longer exist.Thank youJuly 15 11:23 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Thank you for bringing this to our attention and informing us that this limitation is not documented in the public documentation.With 11 app roles, it is possible to reach a limit that we have atm. More details can be found at this confluence page [https://outsystemsrd.atlassian.net/wiki/spaces/RDSD/pages/3602219326/Maximum+roles+per+user](https://outsystemsrd.atlassian.net/wiki/spaces/RDSD/pages/3602219326/Maximum+roles+per+user)We will request an update to the public documentation to include information about the 10 app roles limitation.For internal use, please note that this is the link to the VM that will unlock this limitation:  
[https://outsystemsrd.atlassian.net/browse/RPOR-19956](https://outsystemsrd.atlassian.net/browse/RPOR-19956)  
The support team can monitor this link to know when the limitation will no longer exist.Thank you
July 15 11:23 AM WESTwebRootlySend ZenDesk private comment has been unsetJuly 15 11:23 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

July 15 11:28 AM WESTwebCatarina Gon&ccedil;alves
Incident has been resolved
July 15 11:28 AM WESTwebCatarina Gon&ccedil;alvesImpact has been set: Expectable user experience. Not being able to assign more than 10 org app roles. July 15 11:28 AM WESTwebCatarina Gon&ccedil;alvesResolution has been set: Updated the documentation