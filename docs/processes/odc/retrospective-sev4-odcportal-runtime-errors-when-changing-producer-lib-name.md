---
title: Retrospective-SEV4-[ODCPortal] Runtime errors when changing Producer lib name
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4321181753/Retrospective-SEV4-+ODCPortal+Runtime+errors+when+changing+Producer+lib+name
confluence_space: RKB
confluence_page_id: 4321181753
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV4-[ODCPortal] Runtime errors when changing Producer lib name

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV4

Teams:&nbsp;trueBlueBuild Services
#### 🕐 Timestamps
Started At:&nbsp;trueBlueJuly 26  4:29 PM WEST

Mitigated At:&nbsp;trueYellowJuly 30  2:40 PM WEST

Resolved At:&nbsp;trueGreenJuly 30  2:41 PM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/762-odcportal-runtime-errors-when-changing-producer-lib-name)
[Slack channel](https://slack.com/app_redirect?channel=C07DU1S7WVD&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3033886)

#### Summary
----------------------------------------------**ISSUE DESCRIPTION AND HOW TO REPRODUCE**- Changing the name of a library may lead to runtime errors because of other outdated dependencies.
- I was able to consistently reproduce this in the following scenario:![](https://supportoutsystems.zendesk.com/attachments/token/KlkY8Jp0GI0nTxmmrZQEujIJG/?name=image.png)- Green checkmark represents the changed library, which was released and then updated on the main app, while red X represents not having touched the other library.
- Steps:1. Create **Lib1** with web block **Block1** &gt; publish &gt; release.2. Create **Lib2** with web block **Block2** and include **Block1** from **Lib1** in this block (so **Block1** is nested in **Block2**) &gt; publish &gt; release.3. Create **App** &gt; consume **Lib1** and **Lib2** and use both blocks from these libraries in a screen &gt; publish.4. Change **Lib2** name to something else (e.g. **Lib2_changed**) &gt; publish &gt; release.5. Update library in **App** &gt; publish.1. Now refreshing the previously working screen should result in runtime errors.
- Currently reproducible here: https://gs-sandbox-ga-eu-01-dev.outsystems.app/JPT_App/Screen2**IMPACT ON THE CUSTOMER**- No impact, this is an edge case with low chance to occur, so we're just reporting.**TROUBLESHOOTING STEPS &amp; WORKAROUND**- Note that who reported this was Jos&eacute; Carlos Freitas (jcf) on our side and he tested this in two different rings with different results:- EA ring - **eng-ea-us-01** - runtime errors only.- Test ring (-2) - **eng-test-us-01** - publish errors:![](https://supportoutsystems.zendesk.com/attachments/token/eK89rSEQgjvWzfVd0kFgON245/?name=image.png)![](https://supportoutsystems.zendesk.com/attachments/token/KXV5WgmYCuRNkQUKOxe0RXgWU/?name=image.png)
- We then reproduced this consistently in GA sandbox tenant, with runtime errors only:- It makes sense that we get a similar behavior as EA since both Backend and Frontend build worker services are the same version:- Front-end build worker is same version:![](https://supportoutsystems.zendesk.com/attachments/token/SoivMcpQTy9GvObcyuVXsFAHM/?name=image.png)- Backend:![](https://supportoutsystems.zendesk.com/attachments/token/46ioZ9A9eVAw8OHatt3E1mMBn/?name=image.png)
- I've also noted that we are progressively rolling out the removal of **RequireJS**, which may or may not have impact on this issue, I'm not sure: https://outsystemsrd.atlassian.net/wiki/spaces/RDMBVS/pages/4065919564/Rollout+RequireJS+Removal+Phase+II+web+and+mobile
- Finally, to work around this, after following the steps described, we can do the following:- Remove **Lib1** dependency from **Lib2** &gt; publish and release &gt; add back the same dependency &gt; publish and release &gt; update library on **App**.**TECH DATA OR ANY OTHER RELEVANT INFO**
All above._&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 RetrospectiveinfoDetails
**Ring:** ea
**System-wide impact:**&nbsp; No
**Tenant ID:** dc3a3772-693b-4b6a-aa61-5fea3976eeb3
**Tenant Prefix:** odc-portal-localdev
**Routing Error Code:** N/A
**Product Area:** Phoenix::Application Runtime::UI Flows::Web Blocks
### Impact:
See incident details and timeline
### Investigation and troubleshooting findings:### Resolution:
See incident details and timeline
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/762-odcportal-runtime-errors-when-changing-producer-lib-name)

**Date**

**Source**

**User**

**Event**
July 26  4:01 PM WESTwebRootly
created an alert via
July 26  4:01 PM WESTwebRootly
Rootly created this incident
July 26  4:01 PM WESTwebRootly
In triage date has been set to July 26  4:01 PM WEST
July 26  4:28 PM WESTwebRootly[Slack Channel](https://slack.com/app_redirect?channel=C07DU1S7WVD&amp;team=T041063TZ) has been createdJuly 26  4:29 PM WESTwebTiago M. Pereira
Incident has been started
July 26  4:31 PM WESTwebTiago M. Pereira
Hello team!
The fact that:
- removing Lib1 dependency from Lib2 &gt; publish and release &gt; add back the same dependency &gt; publish and release &gt; update library on App 
solves the issue  as support team suggested, makes me believe that this is something related with the build flow itself.It looks like some process that looks for changes in the producers isn't working as expected. I'm moving this ticket to the build services team so that they can provide more details.
July 26  4:32 PM WESTwebTiago M. Pereira
Teams has been added: BuildServices
July 26  4:32 PM WESTwebTiago M. Pereira
Teams has been removed: Client Runtime
July 30  9:21 AM WESTwebDiogo Rom&atilde;o
&ndash; This notification was sent from JIRA RDINC-27705: Runtime errors after changing Library name to Zendesk Support ticket #3033886 by Diogo Rom&atilde;o. &ndash;Hello team,The team was able to reproduce the issue and deploy a new version of the OutSystems.Frontend.Build.Worker to address it: v17.1524.0
We have confirmed that the fix mitigates the problem on ring DEV.As such, we would like to request for the support case to be closed. If the runtime errors persist after the fix reaches the rings without the RequireJS Removal feature, please let us know. Thank you in advance.Best regards,
Build Services, ODC
July 30  2:40 PM WESTwebDiogo Rom&atilde;o
Incident has been mitigated
July 30  2:41 PM WESTwebDiogo Rom&atilde;o
Incident has been resolved
July 30  2:41 PM WESTwebDiogo Rom&atilde;oSystem-wide impact has been set: NoJuly 30  2:41 PM WESTwebDiogo Rom&atilde;oImpact has been set: See incident details and timelineJuly 30  2:41 PM WESTwebDiogo Rom&atilde;oResolution has been set: See incident details and timeline