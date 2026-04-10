---
title: Retrospective-SEV3-Mobile packages from iOS and Android disappeared
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4271800472/Retrospective-SEV3-Mobile+packages+from+iOS+and+Android+disappeared
confluence_space: RKB
confluence_page_id: 4271800472
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV3-Mobile packages from iOS and Android disappeared

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV3

Teams:&nbsp;trueBlueMobile Core
#### 🕐 Timestamps
Started At:&nbsp;trueBlueJuly 3 10:06 AM WEST

Mitigated At:&nbsp;trueYellowJuly 9 10:27 AM WEST

Resolved At:&nbsp;trueGreenJuly 9 10:27 AM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/660-mobile-packages-from-ios-and-android-disappeared)
[Jira issue](https://outsystemsrd.atlassian.net/browse/RDINC-26347)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3020647)

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

Tiago Pereira
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
- A paragraph detailing the issue or question.- The issue seems to occur spontaneously, but the client has tried to generate a mobile application, but the Android and iOS packages disappeared as shown in the picture below:- ![](https://supportoutsystems.zendesk.com/attachments/token/7wsOYNyAzssFuDiYaHWaMINak/?name=image.png)- ![](https://supportoutsystems.zendesk.com/attachments/token/UhquMUMmacSj6bLgnFpkxeI2V/?name=image.png)**IMPACT ON THE CUSTOMER**
Brief description of the impact on the customer/development team/other, including:
- Stage where the problem is happening (Development / QA / Production); **Dev and Test stage**
- Frequency of the problem; **Fairly random**
- Business impact or/and development impact: **The client stated the following - B2C application without a package we can not make the go-live.****TROUBLESHOOTING STEPS &amp; WORKAROUND**
- What are the most relevant findings and hypotheses from our analysis so far?
**-So far, we haven't been able to determine anything. After checking the client's application and trace logs, nothing was logged for the past 7 days regarding the Ayming Collect app. Seems like the application was removed from their ODC portal. Furthermore, when checking the application that was built and tested on the GS sandbox, no logs were reported based on the disappearance.**
- What workaround was tried so far, if any, and how did they impact the reported behavior?
**-The workaround from the following IMAX was implemented:** **https://globalsupport.outsystemsenterprise.com/IMAX/VisualizeIncidentModel?IncidentModelVersionId=5247**
**However, seems like the issue is still present.**
- Was this case discussed previously with anyone from R&amp;D? If so with whom and which R&amp;D team? **No.**
- If it is related, or there is a possibility of being related, to an already existing RDINC, please specify it. Seems similar to RDINC-22763**TECH DATA OR ANY OTHER RELEVANT INFO**
- Tenant ID or Activation Code where the problem is occurring. **33003270-ef13-47c6-90a3-7b7674c8b10e**
- OutSystems revisions of the components involved (mandatory). This includes for example revision of ODC Studio or Forge Supported Plugins. N/A
- Diagnostics report (mandatory for ODC Studio-related issues). N/A
- All technical files or data, including OMLs.
- Error stacks, screenshots, or any other files like error logs or traces:- ![](https://supportoutsystems.zendesk.com/attachments/token/UhquMUMmacSj6bLgnFpkxeI2V/?name=image.png)
- We also reviewed the following Grafana logs to see if there was anything logged:- https://outsystems.grafana.net/d/cdgg5feb0g6bkd/publish-deploy-mabs?orgId=1&amp;from=now-30d&amp;to=now&amp;var-ring=ga&amp;var-tenant=33003270-ef13-47c6-90a3-7b7674c8b10e&amp;var-application=9aca747a-8e4a-48db-907a-694f3796811e&amp;var-region=All&amp;var-stamp=All&amp;var-mobile_platform=All- I also checked the Grafana logs for the Sandapp Mobile application deployed:- https://outsystems.grafana.net/d/cdeqzn1jj77cwe/general-troubleshooting?orgId=1&amp;var-ring=ga&amp;var-tenant=494dbe13-397f-4c12-8c64-7e005b39c81b&amp;var-application=d8b797d8-3465-442d-a8d7-421a73a534a5&amp;var-cluster=All&amp;var-cluster_old=All&amp;var-severity=All&amp;var-runtime=All&amp;var-filter=&amp;var-exclude=&amp;var-region=eu-central-1&amp;var-traceDuration=All&amp;var-environment=All&amp;var-regionShort=ga-eu-ce-1-01&amp;var-tenant_prefix=gs-sandbox-ga-eu-01&amp;var-module_name=&amp;from=1719242521503&amp;to=1719847321503- However, I did not see anything mentioned for June 27th, 2024 at 12:01 PM.- Although, I believe that could be because of the logging limit for Grafana.- Did the same for the client's application, Ayming Collect for June 10th, 2024:- https://outsystems.grafana.net/d/cdeqzn1jj77cwe/general-troubleshooting?orgId=1&amp;var-ring=ga&amp;var-tenant=33003270-ef13-47c6-90a3-7b7674c8b10e&amp;var-application=9aca747a-8e4a-48db-907a-694f3796811e&amp;var-cluster=All&amp;var-cluster_old=All&amp;var-severity=All&amp;var-runtime=All&amp;var-filter=&amp;var-exclude=&amp;var-region=eu-central-1&amp;var-traceDuration=All&amp;var-environment=All&amp;var-regionShort=ga-eu-ce-1-01&amp;var-tenant_prefix=collect-ayming&amp;var-module_name=AymingCollect&amp;from=1717992000000&amp;to=1718035199000- Same issue as above with Grafana._&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 RetrospectiveinfoDetails
**Ring:** ga
**System-wide impact:**&nbsp; 
**Tenant ID:** 33003270-ef13-47c6-90a3-7b7674c8b10e
**Tenant Prefix:** collect-ayming
**Routing Error Code:** N/A
**Product Area:** Phoenix::Phoenix Portal::Apps::Mobile::Building
### Impact:
All builds prior to June 21st were being filtered out.
### Investigation and troubleshooting findings:### Resolution:
For the ticket resolution, any build performed after June 21st isn't affected, which seems enough for what the customer was blocked.

Nevertheless, NAOS 1.15.2 fixes this entirely.
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/660-mobile-packages-from-ios-and-android-disappeared)

**Date**

**Source**

**User**

**Event**
July 2  9:47 PM WESTwebRootly
created an alert via
July 2  9:47 PM WESTwebRootly
Rootly created this incident
July 2  9:47 PM WESTwebRootly
In triage date has been set to July 2  9:47 PM WEST
July 2  9:57 PM WESTwebRootly
This incident was instantiated in Jira: RDINC-26347. Please work the incident using Rootly
July 2 10:47 PM WESTwebRootly
This incident was instantiated in Jira: RDINC-26347. Please work the incident using Rootly
July 3 10:06 AM WESTwebTiago Pereira
Incident has been started
July 3 10:06 AM WESTwebTiago PereiraTiago Pereira has been assigned as EngineerJuly 3 11:50 AM WESTwebTiago PereiraSend ZenDesk private comment has been set: Hello team,  Given the symptoms shared, we were able to pinpoint what caused the reported issue. The issue started to happen on **June 21st around 9am**, when **NAOS v1.14.1** reached GA.  That version included a change on the native mobile builds listing, which made all builds prior to **June 21st** to be filtered out. However, after that point, the issue doesn&rsquo;t happen anymore and this matches what the customer shared: they only encountered the issue once, since this won&rsquo;t happen with any build performed after June 21st.  We apologize for the inconvenience this might have caused. Feel free to reach us for further clarifications.  Best regards,  
Tiago PereiraJuly 3 11:50 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hello team,  Given the symptoms shared, we were able to pinpoint what caused the reported issue. The issue started to happen on **June 21st around 9am**, when **NAOS v1.14.1** reached GA.  That version included a change on the native mobile builds listing, which made all builds prior to **June 21st** to be filtered out. However, after that point, the issue doesn&rsquo;t happen anymore and this matches what the customer shared: they only encountered the issue once, since this won&rsquo;t happen with any build performed after June 21st.  We apologize for the inconvenience this might have caused. Feel free to reach us for further clarifications.  Best regards,  
Tiago Pereira
July 3 11:50 AM WESTwebRootlySend ZenDesk private comment has been unsetJuly 3 11:50 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

July 3  4:50 PM WESTwebRootlyZenDesk Event Type has been set: solvedJuly 3  4:50 PM WESTwebRootly
The Global Support team marked this incident as closed in ZenDesk.
July 9 10:27 AM WESTwebTiago Pereira
Incident has been resolved
July 9 10:27 AM WESTwebTiago PereiraImpact has been set: All builds prior to June 21st were being filtered out.July 9 10:27 AM WESTwebTiago PereiraResolution has been set: For the ticket resolution, any build performed after June 21st isn't affected, which seems enough for what the customer was blocked.
Nevertheless, NAOS 1.15.2 fixes this entirely.