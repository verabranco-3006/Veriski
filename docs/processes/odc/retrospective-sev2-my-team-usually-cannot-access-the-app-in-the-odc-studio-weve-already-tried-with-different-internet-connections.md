---
title: Retrospective-SEV2-My team usually cannot access the app in the ODC Studio. We've already tried with different internet connections.
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4278976775/Retrospective-SEV2-My+team+usually+cannot+access+the+app+in+the+ODC+Studio.+We+ve+already+tried+with+different+internet+connections.
confluence_space: RKB
confluence_page_id: 4278976775
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV2-My team usually cannot access the app in the ODC Studio. We've already tried with different internet connections.

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV2

Teams:&nbsp;trueBlueNeo Platform Theseus
#### 🕐 Timestamps
Started At:&nbsp;trueBlueJuly 11 12:32 PM WEST

Mitigated At:&nbsp;trueYellowJuly 11 12:36 PM WEST

Resolved At:&nbsp;trueGreenJuly 11 12:36 PM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/551-my-team-usually-cannot-access-the-app-in-the-odc-studio-we-ve-already-tried-with-different-internet-connections-13b7c0b6-0cb8-4dcf-8fc8-72aab25f2ebf)
[Slack channel](https://slack.com/app_redirect?channel=C077DTBNJDB&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3017804)

#### 🧑&zwj;🚒 Incident Rolestrue
**Stakeholder**

Rodrigo Silva

**Engineer**

Marco Martins
#### Summary
----------------------------------------------**CONSIDERATIONS BEFORE PERFORMING THE ESCALATION TO R&amp;D (MANDATORY)**
None of the below points should be overlooked. Failure to do so may imply unnecessary effort.* * *
Ensure the ticket has been **categorized**, otherwise, the R&amp;D escalation will go unnoticed and not be worked on!**1.** For **Incidents**, the **IMAX** was consulted **beforehand** on which:- No incident models were found for the reported symptoms **OR**
- The incident model did not solve the issue **OR**
- The next step indicated in the Incident Model is an escalation to R&amp;D.
**2.** For **Questions**, the ChatODC on the **Slack channel** didn't return an acceptable answer.
**3.** Any other requests that explicitly indicate an R&amp;D escalation is needed.
**4**. **Incident impact assessment** was based on the **prioritization scoring matrix**.* * ***R&amp;D ESCALATION FORM**
Section comments can be removed for R&amp;D easier interpretation.**ISSUE DESCRIPTION AND HOW TO REPRODUCE**- They are unable to open any apps in the ODC Studio- ![](https://www.outsystems.com/SupportPortal/DownloadAmazon.aspx?TicketGUID=db973726-66bf-44d6-8235-132c5ce310b8&amp;FileName=1718072809000000000__1718072807837.png)**IMPACT ON THE CUSTOMER**
Brief description of the impact on the customer/development team/other, including:
- Stage where the problem is happening (Development / QA / Production);- Development
- Frequency of the problem;- Ongoing
- Business impact or/and development impact;- Affecting deadlines **and first release in 2 weeks****TROUBLESHOOTING STEPS &amp; WORKAROUND**
In order to mitigate the issue, they have tried to delete the content:'C:\Users\NghiaDNP1\AppData\Local\Temp\7884d578-b074-4639-ada3-0b90cdb3d0ea.txt'After that, they tried to open ODC Studio again.- Next step suggested (Try one at a time)1. Delete all folders in your %localappdata%\OutSystems folder that starts with &quot;ODCStudio&quot; and retry;
2. Delete all folders in your %localappdata%\OutSystems folder that starts with &quot;ODCStudio&quot;, Uninstall ODC Studio, and install the newest version (in a different folder)
3. Use an uninstalling tool that removes all the data from the ODC Studio installation (including all folders and Registry Keys) (e.g. Revo Uninstall Portable), Install the Service Studio again, and retry- They have used the following free tool available online: Revo Uninstaller - Portable version:
- Uninstall the ODC Studio
- After uninstalling the Service search all files and registry keys (advance search) and delete all of them
- Issue persist.
- Diagnostic report shared- 1d0970ae-2e8d-4988-acc5-35cecc79d55c.txt**TECH DATA OR ANY OTHER RELEVANT INFO**
Ring: ga
Tenant Id: f4474c75-7296-4072-b445-307a8cff0db1
Tenant Prefix: izi
Region: eu-central-1
VP0.EXN.OTN.IUL.SFM.2MQ.NIW.ATS_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 RetrospectiveinfoDetails
**Ring:** ga
**System-wide impact:**&nbsp; 
**Tenant ID:** f4474c75-7296-4072-b445-307a8cff0db1
**Tenant Prefix:** izi
**Routing Error Code:** N/A
**Product Area:** Phoenix::Service Studio::Applications List
### Impact:
Customer reported that they weren't able to open their App.
### Investigation and troubleshooting findings:
We checked the logs on AVS and everything looked good! Then we activated the S3 logs to understand if it was an issue to download the App (OML) from S3 and requested the customer to try again. But they haven't replied anymore.
### Resolution:
Nothing was done to solve the &quot;problem&quot; since the customer dind't reply anymore.
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/551-my-team-usually-cannot-access-the-app-in-the-odc-studio-we-ve-already-tried-with-different-internet-connections-13b7c0b6-0cb8-4dcf-8fc8-72aab25f2ebf)

**Date**

**Source**

**User**

**Event**
June 11  4:05 AM WESTwebRootly
created an alert via
June 11  4:05 AM WESTwebRootly
Rootly created this incident
June 11  4:05 AM WESTwebRootly
In triage date has been set to June 11  4:05 AM WEST
June 11  4:05 AM WESTwebRootly[Slack Channel](https://slack.com/app_redirect?channel=C077DTBNJDB&amp;team=T041063TZ) has been createdJune 11  4:06 AM WESTwebRootly
Ring: ga
System-wide impact:  
Tenant ID: f4474c75-7296-4072-b445-307a8cff0db1
Tenant Prefix: izi
Routing Error Code: N/A
Product Area: Phoenix::Service Studio::Applications List
June 12 12:05 PM WESTwebRodrigo Silva
Teams has been added: Neo Platform Theseus
June 12 12:06 PM WESTwebRodrigo SilvaMarco has been assigned as EngineerJune 12 12:07 PM WESTwebRodrigo SilvaRodrigo has been assigned as StakeholderJune 12 12:08 PM WESTwebRodrigo Silva
Marco has been unassigned from Engineer
June 12 12:14 PM WESTwebRodrigo SilvaMarco Martins has been assigned as EngineerJune 13  8:44 AM WESTwebRootlyZendesk Private Comment has been set: ----------------------------------------------**Update to R&amp;D**
Hey team,The customer has gotten back to us informing us that they were assigned a new laptop by their company yesterday, and even in this new laptop, the issue persists. They've also shared a new screenshot of their connection speed for reference:![](https://supportoutsystems.zendesk.com/attachments/token/7sMPA6ay2fbJKtv2itIqYa1kq/?name=1718262699000000000__Screenshot+2024-06-13+141053.png)Hope this helps in narrowing down the issue, and let us know if you need anything from us.Best regards,__June 13  8:44 AM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:

June 13  8:44 AM WESTwebRootlyZendesk Private Comment has been changed to: ------------------------------------------------ This notification was sent from Zendesk Support ticket #3017804 to all linked JIRA issues by Gon&ccedil;alo Silva. --**Update to R&amp;D**
Hey team,The customer has gotten back to us informing us that they were assigned a new laptop by their company yesterday, and even in this new laptop, the issue persists. They've also shared a new screenshot of their connection speed for reference:Attachment - 1718262699000000000__Screenshot2024-06-13141053.pngHope this helps in narrowing down the issue, and let us know if you need anything from us.Best regards,_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_June 13  8:44 AM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:

July 3 12:05 PM WESTwebRootlyZenDesk Event Type has been set: solvedJuly 3 12:05 PM WESTwebRootly
The Global Support team marked this incident as closed in ZenDesk.
July 11 12:32 PM WESTwebRodrigo Silva
Incident has been started
July 11 12:36 PM WESTwebRodrigo Silva
Incident has been resolved
July 11 12:36 PM WESTwebRodrigo SilvaImpact has been set: Customer reported that they weren't able to open their App.July 11 12:36 PM WESTwebRodrigo SilvaInvestigation and troubleshooting findings has been set: We checked the logs on AVS and everything looked good! Then we activated the S3 logs to understand if it was an issue to download the App (OML) from S3 and requested the customer to try again. But they haven't replied anymore.July 11 12:36 PM WESTwebRodrigo SilvaResolution has been set: Nothing was done to solve the &quot;problem&quot; since the customer dind't reply anymore.