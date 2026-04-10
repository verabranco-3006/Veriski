---
title: Retrospective-SEV4-Tooltip not working
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4363124771/Retrospective-SEV4-Tooltip+not+working
confluence_space: RKB
confluence_page_id: 4363124771
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV4-Tooltip not working

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV4

Teams:&nbsp;trueBlueUi Components

Types:&nbsp;trueBlueCustomer Escalated
#### 🕐 Timestamps
Started At:&nbsp;trueBlueAugust 13  8:34 PM WEST

Mitigated At:&nbsp;trueYellowAugust 14 11:07 PM WEST

Resolved At:&nbsp;trueGreenAugust 14 11:07 PM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/878-tooltip-not-working-4032b642-518e-41e8-baea-834fb6b5730d)
[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3045080)

#### 🧑&zwj;🚒 Incident Rolestrue
**Commander**

Gon&ccedil;alo Martins

**Engineer**

Jo&atilde;o Manuel Ferreira
#### Summary
----------------------------------------------**CONSIDERATIONS BEFORE PERFORMING THE ESCALATION TO R&amp;D (MANDATORY)**None of the below points should be overlooked. Failure to do so may imply unnecessary effort.* * *
Ensure the ticket has been **categorized**, otherwise, the R&amp;D escalation will go unnoticed and not be worked on!**1.** For **Incidents**, the **IMAX** was consulted **beforehand** on which:- No incident models were found for the reported symptoms **OR**
- The incident model did not solve the issue **OR**
- The next step indicated in the Incident Model is an escalation to R&amp;D.
**2.** For **Questions**, the ChatODC on the **Slack channel** didn't return an acceptable answer.
**3.** Any other requests that explicitly indicate an R&amp;D escalation is needed.
**4**. **Incident impact assessment** was based on the **prioritization scoring matrix**.* * ***R&amp;D ESCALATION FORM**
Section comments can be removed for R&amp;D easier interpretation.**ISSUE DESCRIPTION AND HOW TO REPRODUCE**
Customer is attempting to implement tool tip patterns on a screen in their app.
https://oyzer-dev.outsystems.app/PowerTalent/RecruiterCockpit
Username - mebomi3732@foraro.com
Pass - Qaz123456789For their tool tips it is not possible to get them to pop up when hovering over the elements where the user has added their tooltips. I attempted to recreate the reported scenario and was able to reproduce by adding the DEPRECATED_Tooltip from the Outsystems UI library. When having both the Deprecated and current pattern the tooltips did not show up. Removing the deprecated pattern and republishing the app seemed to fix the problem. However once I shared this workaround with the customer it seems that they were still not able to get their ToolTip to show.![](https://supportoutsystems.zendesk.com/attachments/token/h1El7sSAijuMWZYIOptrVqHJR/?name=image.png)https://supportoutsystems.zendesk.com/attachments/token/h1El7sSAijuMWZYIOptrVqHJR/?name=image.pngI also have captured a HAR file when reproducing the reported error.
https://www.outsystems.com/SupportPortal/DownloadAmazon.aspx?TicketGUID=ec9bb09a-fd27-458a-807f-3b938fe3def9&amp;FileName=1723571998321_oyzer-dev.outsystems.app.har#hideThe tooltip is applied to a link in the table above.**IMPACT ON THE CUSTOMER**
Brief description of the impact on the customer/development team/other, including:
- Stage where the problem is happening (Development / QA / Production); DEV
- Frequency of the problem; Always, tooltip appears to be broken
- Business impact or/and development impact; LOW**TROUBLESHOOTING STEPS &amp; WORKAROUND**
- What are the most relevant findings and hypotheses from our analysis so far?
After recreating the condition by adding DEPRECATED patterns I thought that it was related to the fact that the customer had the DEPRECATED method consumed in their app. However after removing the deprecated Tooltip pattern the issue persists.
- What workaround was tried so far, if any, and how did they impact the reported behavior?
Removing DEPRECATED Tooltips, setting the onstart property to false did not correct what is occurring with ToolTip.
- Was this case discussed previously with anyone from R&amp;D? If so with whom and which R&amp;D team?- If it is related, or there is a possibility of being related, to an already existing RDINC, please specify it.**TECH DATA OR ANY OTHER RELEVANT INFO**
- Tenant ID or Activation Code where the problem is occurring.
03091d41-4e72-41c0-9a7f-b99cdb139a65
- OutSystems revisions of the components involved (mandatory). This includes for example revision of ODC Studio or Forge Supported Plugins.
Outsystems UI 2.19.1
- Diagnostics report (mandatory for ODC Studio-related issues).
- All technical files or data, including OMLs.
This is a link to my sample app, the tool tips work here adding DEPRECATED Tooltip will break
https://www.outsystems.com/SupportPortal/DownloadAmazon.aspx?TicketGUID=ec9bb09a-fd27-458a-807f-3b938fe3def9&amp;FileName=1723571300830_Tooltips.oml#hide
Customer app- Error stacks, screenshots, or any other files like error logs or traces._&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 RetrospectiveinfoDetails
**Ring:** ga
**System-wide impact:**&nbsp; No
**Tenant ID:** 03091d41-4e72-41c0-9a7f-b99cdb139a65
**Tenant Prefix:** oyzer
**Routing Error Code:** N/A
**Product Area:** Phoenix::Application Runtime::Starter Apps::OutSystems UI
### Impact:
N.A.
### Investigation and troubleshooting findings:
The malfunctioning in the reported use case is due to a bad coding practice in the customer's application that is unsupported and will likely lead to more issues with OutSystems UI components. Specifically, the customer's app includes a custom script in the &quot;LayoutSideMenuCustom&quot; layout block, which contains a script from a different version of OutSystems UI. As a result, the app is loading two different framework versions, causing conflicts and repeated object definitions&mdash;this is highly problematic.
### Resolution:
Nothing on the OutSystems UI side. The action item will be on the customer to remove the second version of the script
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/878-tooltip-not-working-4032b642-518e-41e8-baea-834fb6b5730d)

**Date**

**Source**

**User**

**Event**
August 13  7:00 PM WESTwebRootly
created an alert via
August 13  7:00 PM WESTwebRootly
Rootly created this incident
August 13  7:00 PM WESTwebRootly
In triage date has been set to August 13  7:00 PM WEST
August 13  7:21 PM WESTwebGon&ccedil;alo MartinsGon&ccedil;alo Martins has been assigned as CommanderAugust 13  7:21 PM WESTwebGon&ccedil;alo MartinsJo&atilde;o Manuel Ferreira has been assigned as EngineerAugust 13  8:34 PM WESTwebGon&ccedil;alo Martins
Incident has been started
August 13  8:36 PM WESTwebGon&ccedil;alo MartinsSend ZenDesk private comment has been set: Hello team,  
We will need access to the customer's oml to look into the code of the screen whose link was shared since we are not being able to replicate such behaviour.  
Thank youAugust 13  8:36 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hello team,  
We will need access to the customer's oml to look into the code of the screen whose link was shared since we are not being able to replicate such behaviour.  
Thank you
August 13  8:36 PM WESTwebRootlySend ZenDesk private comment has been unsetAugust 13  8:36 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

August 13  8:41 PM WESTwebGon&ccedil;alo MartinsSend ZenDesk private comment has been set: Hello team.  
Sorry would like to know if the screen that was shared uses the Deprecated Tooltip or the new one.  
Also, we can observe that the console is logging errors that can impact the load of all Javascript.  ![image.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDMwNTc4LCJwdXIiOiJibG9iX2lkIn19--6877b4e7a5321f0643c9e84ed32fb67c68d24ad6/image.png)image.png 192.6 KBHas the screen been isolated as is without any extra dependencies?August 13  8:41 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hello team.  
Sorry would like to know if the screen that was shared uses the Deprecated Tooltip or the new one.  
Also, we can observe that the console is logging errors that can impact the load of all Javascript.  ![image.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDMwNTc4LCJwdXIiOiJibG9iX2lkIn19--6877b4e7a5321f0643c9e84ed32fb67c68d24ad6/image.png)image.png 192.6 KBHas the screen been isolated as is without any extra dependencies?
August 13  8:41 PM WESTwebRootlySend ZenDesk private comment has been unsetAugust 13  8:41 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

August 13 10:48 PM WESTwebRootlyZendesk Private Comment has been set: ----------------------------------------------**Update to R&amp;D**
- Detail additional findings or any questions/concerns that may be important for R&amp;D to be aware of.The app that was shared is not using the DEPRECATED library. I did notice the errors from the Javascript. Do you think these errors from Highcharts are breaking the execution of the other JS using in the app?
Do you still need the oml? I included text links to these OML.__August 13 10:48 PM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
- Detail additional findings or any questions/concerns that may be important for R&amp;D to be aware of.The app that was shared is not using the DEPRECATED library. I did notice the errors from the Javascript. Do you think these errors from Highcharts are breaking the execution of the other JS using in the app?
Do you still need the oml? I included text links to these OML.__
August 13 10:54 PM WESTwebRootlyZendesk Private Comment has been changed to: ----------------------------------------------**Update to R&amp;D**
- Detail additional findings or any questions/concerns that may be important for R&amp;D to be aware of.I have not been able to extract the specific screen without all of the dependencies. If you need this please let us know, this is not something I am aware to of how to perform. The user did provide us credentials to access their live application in DEV so is it neccessary?_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_August 13 10:54 PM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
- Detail additional findings or any questions/concerns that may be important for R&amp;D to be aware of.I have not been able to extract the specific screen without all of the dependencies. If you need this please let us know, this is not something I am aware to of how to perform. The user did provide us credentials to access their live application in DEV so is it neccessary?__
August 14  1:57 PM WESTwebGon&ccedil;alo MartinsSend ZenDesk private comment has been set: Hello Support.  
We continue to need the oml form the customer since we're not able to reproduce the issue and need to look into the implementation or any specific custom code as well as the error on the console not mentioned by supportAugust 14  1:57 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hello Support.  
We continue to need the oml form the customer since we're not able to reproduce the issue and need to look into the implementation or any specific custom code as well as the error on the console not mentioned by support
August 14  1:57 PM WESTwebRootlySend ZenDesk private comment has been unsetAugust 14  1:57 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

August 14  4:26 PM WESTwebRootlyZendesk Private Comment has been changed to: ----------------------------------------------**Update to R&amp;D**
- Detail additional findings or any questions/concerns that may be important for R&amp;D to be aware of.My apology, I believe you need this link to customer app.
Power Talent.oml
https://www.outsystems.com/SupportPortal/DownloadAmazon.aspx?TicketGUID=ec9bb09a-fd27-458a-807f-3b938fe3def9&amp;FileName=1723649109774_Power+Talent.oml#hideI have also uploaded this oml to the Jira ticket._&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_August 14  4:26 PM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
- Detail additional findings or any questions/concerns that may be important for R&amp;D to be aware of.My apology, I believe you need this link to customer app.
Power Talent.oml
https://www.outsystems.com/SupportPortal/DownloadAmazon.aspx?TicketGUID=ec9bb09a-fd27-458a-807f-3b938fe3def9&amp;FileName=1723649109774_Power+Talent.oml#hideI have also uploaded this oml to the Jira ticket.__
August 14  4:36 PM WESTwebRootlyZendesk Private Comment has been changed to: ----------------------------------------------**Update to R&amp;D**
- Detail additional findings or any questions/concerns that may be important for R&amp;D to be aware of.Hello - If you need to download the file from rootly it appears that there are &quot;amp;&quot; being added to the link these will need to be removed and the link will allow you to download from S3 bucket. Feel free to message me if you need a further explanation.https://www.outsystems.com/SupportPortal/DownloadAmazon.aspx?TicketGUID=ec9bb09a-fd27-458a-807f-3b938fe3def9&amp;amp;FileName=1723649109774_Power+Talent.oml#hideThe links being attached are being mutated when sent to rootly or clipboard._&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_August 14  4:36 PM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
- Detail additional findings or any questions/concerns that may be important for R&amp;D to be aware of.Hello - If you need to download the file from rootly it appears that there are &quot;amp;&quot; being added to the link these will need to be removed and the link will allow you to download from S3 bucket. Feel free to message me if you need a further explanation.https://www.outsystems.com/SupportPortal/DownloadAmazon.aspx?TicketGUID=ec9bb09a-fd27-458a-807f-3b938fe3def9&amp;FileName=1723649109774_Power+Talent.oml#hideThe links being attached are being mutated when sent to rootly or clipboard.__
August 14 11:06 PM WESTwebGon&ccedil;alo MartinsSend ZenDesk private comment has been set: Hello Support,  After gaining access to the OML, it became much clearer (though still time-consuming) to confirm the suspicions we had while analyzing the issue in Chrome Dev Tools.  The malfunctioning in the reported use case is due to a bad coding practice in the customer's application that is unsupported and will likely lead to more issues with OutSystems UI components. Specifically, the customer's app includes a custom script in the &quot;LayoutSideMenuCustom&quot; layout block, which contains a script from a different version of OutSystems UI.  The script has version 2.18.1:  
&nbsp;  ![image.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDMxNTYxLCJwdXIiOiJibG9iX2lkIn19--1d35ca414c44e96b9120a1fab872aa0ca5642e07/image.png)image.png 107.84 KBand the environment have a different one:  ![image.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDMxNTY0LCJwdXIiOiJibG9iX2lkIn19--3bd1fc1f12cfdb6cc56e47fb4f0aa6f6176736a8/image.png)image.png 20.94 KBAs a result, the app is loading two different framework versions, causing conflicts and repeated object definitions&mdash;this is highly problematic.  By using Chrome's Developer Tools, one can easily see the different scripts being loaded and identify the versions involved:*   Network:  ![image.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDMxNTYyLCJwdXIiOiJibG9iX2lkIn19--7e80209a71ca10b388944509cb0615b573a99064/image.png)image.png 47.66 KB*   Sources:  ![image.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDMxNTYzLCJwdXIiOiJibG9iX2lkIn19--48a1349f36c750b29b864b818d64193b748b68f8/image.png)image.png 129.73 KBThis being said, there's nothing wrong on the OutSystems UI side but the customer will need to fix this and avoid this bad code practice.  This type of support case should be resolved by support agents before reaching R&amp;D teams. Going forward, please conduct this kind of check to prevent unnecessary escalation and ensure a smoother support process.  Best RegardsAugust 14 11:06 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hello Support,  After gaining access to the OML, it became much clearer (though still time-consuming) to confirm the suspicions we had while analyzing the issue in Chrome Dev Tools.  The malfunctioning in the reported use case is due to a bad coding practice in the customer's application that is unsupported and will likely lead to more issues with OutSystems UI components. Specifically, the customer's app includes a custom script in the &quot;LayoutSideMenuCustom&quot; layout block, which contains a script from a different version of OutSystems UI.  The script has version 2.18.1:  
&nbsp;  ![image.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDMxNTYxLCJwdXIiOiJibG9iX2lkIn19--1d35ca414c44e96b9120a1fab872aa0ca5642e07/image.png)image.png 107.84 KBand the environment have a different one:  ![image.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDMxNTY0LCJwdXIiOiJibG9iX2lkIn19--3bd1fc1f12cfdb6cc56e47fb4f0aa6f6176736a8/image.png)image.png 20.94 KBAs a result, the app is loading two different framework versions, causing conflicts and repeated object definitions&mdash;this is highly problematic.  By using Chrome's Developer Tools, one can easily see the different scripts being loaded and identify the versions involved:*   Network:  ![image.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDMxNTYyLCJwdXIiOiJibG9iX2lkIn19--7e80209a71ca10b388944509cb0615b573a99064/image.png)image.png 47.66 KB*   Sources:  ![image.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDMxNTYzLCJwdXIiOiJibG9iX2lkIn19--48a1349f36c750b29b864b818d64193b748b68f8/image.png)image.png 129.73 KBThis being said, there's nothing wrong on the OutSystems UI side but the customer will need to fix this and avoid this bad code practice.  This type of support case should be resolved by support agents before reaching R&amp;D teams. Going forward, please conduct this kind of check to prevent unnecessary escalation and ensure a smoother support process.  Best Regards
August 14 11:06 PM WESTwebRootlySend ZenDesk private comment has been unsetAugust 14 11:06 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

August 14 11:07 PM WESTwebGon&ccedil;alo Martins
Incident has been resolved
August 14 11:07 PM WESTwebGon&ccedil;alo MartinsSystem-wide impact has been set: NoAugust 14 11:07 PM WESTwebGon&ccedil;alo MartinsImpact has been set: N.A.August 14 11:07 PM WESTwebGon&ccedil;alo MartinsInvestigation and troubleshooting findings has been set: The malfunctioning in the reported use case is due to a bad coding practice in the customer's application that is unsupported and will likely lead to more issues with OutSystems UI components. Specifically, the customer's app includes a custom script in the &quot;LayoutSideMenuCustom&quot; layout block, which contains a script from a different version of OutSystems UI. As a result, the app is loading two different framework versions, causing conflicts and repeated object definitions&mdash;this is highly problematic.August 14 11:07 PM WESTwebGon&ccedil;alo MartinsResolution has been set: Nothing on the OutSystems UI side. The action item will be on the customer to remove the second version of the script