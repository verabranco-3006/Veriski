---
title: Retrospective-SEV3-Error trying to update a forge component
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4297818113/Retrospective-SEV3-Error+trying+to+update+a+forge+component
confluence_space: RKB
confluence_page_id: 4297818113
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV3-Error trying to update a forge component

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV3

Teams:&nbsp;trueBlueOdc Governance
#### 🕐 Timestamps
Started At:&nbsp;trueBlueJuly 10 10:54 AM WEST

Mitigated At:&nbsp;trueYellowJuly 19  9:13 AM WEST

Resolved At:&nbsp;trueGreenJuly 19  9:13 AM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/664-error-trying-to-update-a-forge-component)
[Slack channel](https://slack.com/app_redirect?channel=C07B6UQ7UE6&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3030723)

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

Jo&atilde;o Jaime
#### Summary
----------------------------------------------**R&amp;D ESCALATION FORM****ISSUE DESCRIPTION AND HOW TO REPRODUCE**- OutSystems Professional Expert colleague is unable to update the Template_BDD Framework in Forge, the same has been replicated by me in Global Support sandbox**IMPACT ON THE CUSTOMER**- Blocking the update in Forge without major impact, no current deadline
- This may affect other customers as well**TROUBLESHOOTING STEPS &amp; WORKAROUND**- checked what is the documentation available
- https://success.outsystems.com/documentation/outsystems_developer_cloud/building_apps/forge/submit_assets_to_forge/&gt; - Assets must be versioned except for App Templates that are versioned by Forge. Versioning assets is slightly different for apps and libraries.- in O11 doc https://success.outsystems.com/documentation/11/building_apps/user_interface/reuse_ui/create_a_custom_application_template/, there is a reference to the requirement of having a description
- replicated the error by clicking update on the my assets submitted to Forge![](https://supportoutsystems.zendesk.com/attachments/token/nKoWLMpjkKSJOHUTwh3hG77z5/?name=image.png)&gt; We're sorry, at the moment, we can't check which apps are installed
&gt;
&gt; Tagged revision not found for application with key 'c919c8b8-a0ab-4746-9228-982715e9927b'. Please check that a revision of the application was tagged (OS-APPS-40405)- checked the app template in their tenant that they want to update:![](https://supportoutsystems.zendesk.com/attachments/token/L5ttUSG9h8F1Xv6M6WACTYgwQ/?name=image.png)
- checked the app template in Forge:![](https://supportoutsystems.zendesk.com/attachments/token/P98hLXRzvkzHUYVClmn3eTOSw/?name=image.png)
- both app templates above have the reference attributes fulfilled, however, the version that app template that they trying to upload has the revision 6 while the app template in Forge has the revision 62. Probably not related but we were unable to find any relevant documentation that could clarify if this matter would impact**TECH DATA OR ANY OTHER RELEVANT INFO**
Ring: ea
Tenant Id: 82efc85c-94e8-4bd7-a0cd-c0dd0f558e6a
Tenant Prefix: professionalservices
Region: eu-central-1
LUM.MOU.1GF.BHV.DJY.PBD.P2V.GTS
support_level_8x5Additional request/question:- What are the requirements to update/submit App Templates to Forge?_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 RetrospectiveinfoDetails
**Ring:** ea
**System-wide impact:**&nbsp; 
**Tenant ID:** 82efc85c-94e8-4bd7-a0cd-c0dd0f558e6a
**Tenant Prefix:** professionalservices
**Routing Error Code:** OS-APPC
**Product Area:** -
### Impact:
Error trying to update a forge component
### Investigation and troubleshooting findings:
Requested more information to the customer
### Resolution:
Customer didn't reply to our questions
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/664-error-trying-to-update-a-forge-component)

**Date**

**Source**

**User**

**Event**
July 3  4:28 PM WESTwebRootly
created an alert via
July 3  4:28 PM WESTwebRootly
Rootly created this incident
July 3  4:28 PM WESTwebRootly
In triage date has been set to July 3  4:28 PM WEST
July 5  1:54 PM WESTwebRootly[Slack Channel](https://slack.com/app_redirect?channel=C07B6UQ7UE6&amp;team=T041063TZ) has been createdJuly 10 10:54 AM WESTwebLu&iacute;s Carvalho
Teams has been added: ODC Governance
July 10 10:54 AM WESTwebLu&iacute;s Carvalho
Teams has been removed: ALM Consoles
July 10 10:54 AM WESTwebLu&iacute;s CarvalhoJo&atilde;o Jaime has been assigned as EngineerJuly 10 10:54 AM WESTwebLu&iacute;s Carvalho
Incident has been started
July 12  1:03 AM WESTwebRootlyZenDesk Event Type has been set: solvedJuly 12  1:03 AM WESTwebRootly
The Global Support team marked this incident as closed in ZenDesk.
July 19  9:11 AM WESTwebAnt&oacute;nio Rodrigues
https://outsystemsrd.atlassian.net/browse/RDINC-26399automatically closed, no follow up by the customer
July 19  9:13 AM WESTwebAnt&oacute;nio Rodrigues
Incident has been resolved
July 19  9:13 AM WESTwebAnt&oacute;nio RodriguesImpact has been set: Error trying to update a forge componentJuly 19  9:13 AM WESTwebAnt&oacute;nio RodriguesInvestigation and troubleshooting findings has been set: Requested more information to the customerJuly 19  9:13 AM WESTwebAnt&oacute;nio RodriguesResolution has been set: Customer didn't reply to our questions