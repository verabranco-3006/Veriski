---
title: Retrospective-SEV3-Resources from Library seems to be unavailable
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4307943526/Retrospective-SEV3-Resources+from+Library+seems+to+be+unavailable
confluence_space: RKB
confluence_page_id: 4307943526
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV3-Resources from Library seems to be unavailable

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV3

Teams:&nbsp;trueBlueClient Runtime
#### 🕐 Timestamps
Started At:&nbsp;trueBlueJuly 17  8:55 AM WEST

Mitigated At:&nbsp;trueYellowJuly 17  9:18 AM WEST

Resolved At:&nbsp;trueGreenJuly 24 11:25 AM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/715-resources-from-library-seems-to-be-unavailable)
[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3035703)

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

David Pires
#### Summary
----------------------------------------------**CONSIDERATIONS BEFORE PERFORMING THE ESCALATION TO R&amp;D (MANDATORY)**
None of the below points should be overlooked. Failure to do so may imply unnecessary effort.* * *
Ensure the ticket has been **categorized**, otherwise, the R&amp;D escalation will go unnoticed and not be worked on!**1.** For **Incidents**, the **IMAX** was consulted **beforehand** on which:- No incident models were found for the reported symptoms **OR**
- The incident model did not solve the issue **OR**
- The next step indicated in the Incident Model is an escalation to R&amp;D.
**2.** For **Questions**, the ChatODC on the **Slack channel** didn't return an acceptable answer.
**3.** Any other requests that explicitly indicate an R&amp;D escalation is needed.
**4**. **Incident impact assessment** was based on the **prioritization scoring matrix**.* * ***R&amp;D ESCALATION FORM**
Section comments can be removed for R&amp;D easier interpretation.**ISSUE DESCRIPTION AND HOW TO REPRODUCE**- Customer is trying to create a new Library to integrate TinyMCE into ODC but they are facing issues while using the library into other app as the &quot;resources&quot; from the Library app seems to not be reachable.
- Hereafter the error from the browser inspector:**![](https://www.outsystems.com/SupportPortal/DownloadAmazon.aspx?TicketGUID=d67fe0a6-f9bd-4ff4-809f-34cbd770d5ef&amp;FileName=1720777795000000000__1720777795011.png)**- And here is the configuration into the Library app:**![](https://www.outsystems.com/SupportPortal/DownloadAmazon.aspx?TicketGUID=d67fe0a6-f9bd-4ff4-809f-34cbd770d5ef&amp;FileName=1720777839000000000__1720777839302.png)****IMPACT ON THE CUSTOMER**
Normal, its impacting their new feature development.**TROUBLESHOOTING STEPS &amp; WORKAROUND**- TinyMCE is a third party javascript Wysiwyg that requires additional resources to run not only the theme that was used to explain the issue.- All these resources have the problem- ![](https://www.outsystems.com/SupportPortal/DownloadAmazon.aspx?TicketGUID=d67fe0a6-f9bd-4ff4-809f-34cbd770d5ef&amp;FileName=1720793605000000000__1720793605342.png)- Link to the Test app in the customer env (the app and library also attached to this escalation)- https://antenovi-dev.outsystems.app/Test/TinyMCE- And here the errors raised by the app (via the browser inspector)- ![](https://www.outsystems.com/SupportPortal/DownloadAmazon.aspx?TicketGUID=d67fe0a6-f9bd-4ff4-809f-34cbd770d5ef&amp;FileName=1721030676000000000__1721030675692.png)- We were also able to replicate with the customer's app in our sandbox.- The Deploy Action seems to be set correctly- ![](https://supportoutsystems.zendesk.com/attachments/token/CXvWG1TJfBkaFl1tEtaiDNvlA/?name=image.png)- We would like to seek R&amp;D's help in this matter and how the customer can proceed with this.**TECH DATA OR ANY OTHER RELEVANT INFO**
**Ring**: ga
**Tenant Id:** 29874171-8818-436c-879e-083859f7d79d
**Tenant Prefix:** antenovi
**Region:** eu-central-1
ZOS.RD3.ULN.KBJ.OEA.UPO.1UI.AOUAttached is the OMLs_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_Attachment(s):
TinyMCE.oml - https://supportoutsystems.zendesk.com/attachments/token/iEk2nXCSac4il29jR9kIDWZrH/?name=TinyMCE.omlTest.oml - https://supportoutsystems.zendesk.com/attachments/token/yEjU8KCNb6HMQY6HVzcmNrndc/?name=Test.oml
## 📝 RetrospectiveinfoDetails
**Ring:** ga
**System-wide impact:**&nbsp; 
**Tenant ID:** 29874171-8818-436c-879e-083859f7d79d
**Tenant Prefix:** antenovi
**Routing Error Code:** N/A
**Product Area:** Phoenix::Application Runtime::Resources
### Impact:
Client couldn't load resources in runtime
### Investigation and troubleshooting findings:### Resolution:
Explain how resources work in runtime, and point client to the right approach
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/715-resources-from-library-seems-to-be-unavailable)

**Date**

**Source**

**User**

**Event**
July 17  7:23 AM WESTwebRootly
created an alert via
July 17  7:23 AM WESTwebRootly
Rootly created this incident
July 17  7:23 AM WESTwebRootly
In triage date has been set to July 17  7:23 AM WEST
July 17  7:33 AM WESTwebRootly
This incident was instantiated in Jira: RDINC-27237. Please work the incident using Rootly
July 17  8:23 AM WESTwebRootly
This incident was instantiated in Jira: RDINC-27237. Please work the incident using Rootly
July 17  8:55 AM WESTwebDavid Pires
Incident has been started
July 17  9:16 AM WESTwebDavid PiresSend ZenDesk private comment has been set: Hey team,Looking at the prints and by trying it in my machine, I see that it is trying to load the resources from the scripts folder: [antenovi-dev.outsystems.app/Test/scripts/plugins/anchor/plugin.min.js](https://antenovi-dev.outsystems.app/Test/plugins/anchor/plugin.min.js) but the resources files must be loaded from the root folder, so in this example the url is&nbsp;[antenovi-dev.outsystems.app/Test/plugins/anchor/plugin.min.js](https://antenovi-dev.outsystems.app/Test/plugins/anchor/plugin.min.js). You can try to access this link directly to check that it is working.July 17  9:16 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hey team,Looking at the prints and by trying it in my machine, I see that it is trying to load the resources from the scripts folder: [antenovi-dev.outsystems.app/Test/scripts/plugins/anchor/plugin.min.js](https://antenovi-dev.outsystems.app/Test/plugins/anchor/plugin.min.js) but the resources files must be loaded from the root folder, so in this example the url is&nbsp;[antenovi-dev.outsystems.app/Test/plugins/anchor/plugin.min.js](https://antenovi-dev.outsystems.app/Test/plugins/anchor/plugin.min.js). You can try to access this link directly to check that it is working.
July 17  9:16 AM WESTwebRootlySend ZenDesk private comment has been unsetJuly 17  9:16 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

July 17  9:18 AM WESTwebDavid Pires
Incident has been mitigated
July 17  2:54 PM WESTwebRita TinocoDavid Pires has been assigned as EngineerJuly 18 12:27 AM WESTwebRootlyZendesk Private Comment has been set: ----------------------------------------------**Update to R&amp;D**- Thanks for the information.
- May we know how the customer can re-mediate this? Thank you.__July 18 12:27 AM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**- Thanks for the information.
- May we know how the customer can re-mediate this? Thank you.__
July 18 12:27 AM WESTwebRootlyZendesk Private Comment has been changed to: ------------------------------------------------ This notification was sent from Zendesk Support ticket #3035703 to all linked JIRA issues by Zaman Akbar Mohamed-Akbar. --**Update to R&amp;D**- Thanks for the information.
- May we know how the customer can re-mediate this? Thank you._&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_July 18 12:27 AM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
------------------------------------------------ This notification was sent from Zendesk Support ticket #3035703 to all linked JIRA issues by Zaman Akbar Mohamed-Akbar. --**Update to R&amp;D**- Thanks for the information.
- May we know how the customer can re-mediate this? Thank you.__
July 23 10:17 AM WESTwebRootly[Slack Channel](https://slack.com/app_redirect?channel=C07EA9M0MK2&amp;team=T041063TZ) has been createdJuly 23  3:11 PM WESTwebDavid PiresSend ZenDesk private comment has been set: Hey team,  
Client needs to change their custom code to load resources from the root path. Currently the user is trying to load from&nbsp;[antenovi-dev.outsystems.app/Test/scripts/\[resource-path\]](https://antenovi-dev.outsystems.app/Test/plugins/anchor/plugin.min.js) but the resources files must be loaded from the root folder, so in this example the url it should be [antenovi-dev.outsystems.app/Test/plugins/\[resource-path\]](https://antenovi-dev.outsystems.app/Test/plugins/anchor/plugin.min.js)July 23  3:11 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hey team,  
Client needs to change their custom code to load resources from the root path. Currently the user is trying to load from&nbsp;[antenovi-dev.outsystems.app/Test/scripts/\[resource-path\]](https://antenovi-dev.outsystems.app/Test/plugins/anchor/plugin.min.js) but the resources files must be loaded from the root folder, so in this example the url it should be [antenovi-dev.outsystems.app/Test/plugins/\[resource-path\]](https://antenovi-dev.outsystems.app/Test/plugins/anchor/plugin.min.js)
July 23  3:11 PM WESTwebRootlySend ZenDesk private comment has been unsetJuly 23  3:11 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

July 24  6:13 AM WESTwebRootlyZenDesk Event Type has been set: solvedJuly 24  6:13 AM WESTwebRootly
The Global Support team marked this incident as closed in ZenDesk.
July 24 11:25 AM WESTwebDavid Pires
Incident has been resolved
July 24 11:25 AM WESTwebDavid PiresImpact has been set: Client couldn't load resources in runtimeJuly 24 11:25 AM WESTwebDavid PiresResolution has been set: Explain how resources work in runtime, and point client to the right approach