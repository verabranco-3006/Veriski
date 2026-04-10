---
title: Retrospective-SEV3-Internal Users Count
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4352933946/Retrospective-SEV3-Internal+Users+Count
confluence_space: RKB
confluence_page_id: 4352933946
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV3-Internal Users Count

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV3

Teams:&nbsp;trueBlueIdentity Core
#### 🕐 Timestamps
Started At:&nbsp;trueBlueJuly 17 10:52 AM WEST

Mitigated At:&nbsp;trueYellowAugust 12  8:58 AM WEST

Resolved At:&nbsp;trueGreenAugust 12 10:08 AM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/719-internal-users-count-c8667c1d-d08b-4e60-820c-bebfce241be0)
[Pagerduty incident](https://outsystems.pagerduty.com/incidents/Q0KYKTYKF249ES)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3036985)

#### Summary
----------------------------------------------**CONSIDERATIONS BEFORE PERFORMING THE ESCALATION TO R&amp;D (MANDATORY)**
None of the below points should be overlooked. Failure to do so may imply unnecessary effort.* * *
Ensure the ticket has been **categorized**, otherwise, the R&amp;D escalation will go unnoticed and not be worked on!**1.** For **Incidents**, the **IMAX** was consulted **beforehand** on which:- No incident models were found for the reported symptoms **OR**
- The incident model did not solve the issue **OR**
- The next step indicated in the Incident Model is an escalation to R&amp;D.
**2.** For **Questions**, the ChatODC on the **Slack channel** didn't return an acceptable answer.
**3.** Any other requests that explicitly indicate an R&amp;D escalation is needed.
**4**. **Incident impact assessment** was based on the **prioritization scoring matrix**.* * ***R&amp;D ESCALATION FORM**
Section comments can be removed for R&amp;D easier interpretation.**ISSUE DESCRIPTION AND HOW TO REPRODUCE**- The customer **National University of Singapore (Duke-NUS Medical School)** is reporting that the end-users counted in the subscription page is not tally with the end-users in the list.
- There are 345 users on the list, and 103 users counted in the subscription, and the last change was made more than a week ago.**IMPACT ON THE CUSTOMER**
Brief description of the impact on the customer/development team/other, including:- Currently, there is no direct impact on their live app or the end users, but they are concerned about why is there a discrepancy.**TROUBLESHOOTING STEPS &amp; WORKAROUND**
- Refer to tenant portalt.**TECH DATA OR ANY OTHER RELEVANT INFO**
**National University of Singapore (Duke-NUS Medical School)**
Ring: ga
Tenant Id: 9c85fb7c-58b0-4058-960b-ecf4a5d45c24
Tenant Prefix: dukenus
Region: ap-southeast-1
NUJ.CCV.B19.UNP.EVZ.Q3B.F9E.QOU_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 RetrospectiveinfoDetails
**Ring:** ga
**System-wide impact:**&nbsp; 
**Tenant ID:** 9c85fb7c-58b0-4058-960b-ecf4a5d45c24
**Tenant Prefix:** dukenus
**Routing Error Code:** N/A
**Product Area:** Phoenix::Phoenix Portal::Users &amp; access - Users
### Impact:### Investigation and troubleshooting findings:### Resolution:## Tasks performed during incident resolution:
&nbsp;
## Executive Summary
[Guidelines](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4144496679/Incident+Retrospectives+-+Playbook#STEP-3---Write-the-Executive-Summary)
## Root Causes 
[Guidelines](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4144496679/Incident+Retrospectives+-+Playbook#STEP-1---Perform-the-Root-Cause-Analysis)

If the customer needs formal RCA, please fill out the following field with the document URL

[Please follow these instructions and place the RCA URL in the field below.](https://docs.google.com/document/d/13rXmBsOJh73nV2D6Z17SIBGBu2HOTWty5ddsvU000JM/edit#heading=h.bqxasxszr5q)

RCA URL

&lt;Place the URL of the customer RCA here if you have created one&gt;
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/719-internal-users-count-c8667c1d-d08b-4e60-820c-bebfce241be0)

**Date**

**Source**

**User**

**Event**
July 17  9:17 AM WESTwebRootly
created an alert via
July 17  9:17 AM WESTwebRootly
Rootly created this incident
July 17  9:17 AM WESTwebRootly
In triage date has been set to July 17  9:17 AM WEST
July 17 10:52 AM WESTwebCl&aacute;udia Rezende
Incident has been started
July 17 10:54 AM WESTwebCl&aacute;udia Rezende
Teams has been added: ALM Consoles
July 17 11:13 AM WESTwebCl&aacute;udia Rezende
Hello, 
Based on the provided screenshot  the values ​​really don't match.  The  subscription console is an asset from ALM consoles Team .  I will redirect this support to them so they can analyze it better and check the endpoint that returns the values.
July 17 11:14 AM WESTwebCl&aacute;udia Rezende
Teams has been removed: ODC Governance
July 17 11:17 AM WESTwebJo&atilde;o SemedoJo&atilde;o Semedo has been assigned as EngineerJuly 17 11:36 AM WESTwebJo&atilde;o SemedoSend ZenDesk private comment has been set: Hello support team,  On the subscription page can you please send us a screenshot of the end-users tab, for us to confirm if this tenant has any domain.  If this tenant does not have any custom domains we need to verify this information with theseus team.  If there is any custom domain for this tenant,&nbsp; the customer can cross those domains with the users that are on the users list and understand If they match.  
If they are still discrepancies&nbsp; we also need to verify this information with theseus team.  Kind regards,&nbsp;  
ODC teamJuly 17 11:36 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hello support team,  On the subscription page can you please send us a screenshot of the end-users tab, for us to confirm if this tenant has any domain.  If this tenant does not have any custom domains we need to verify this information with theseus team.  If there is any custom domain for this tenant,&nbsp; the customer can cross those domains with the users that are on the users list and understand If they match.  
If they are still discrepancies&nbsp; we also need to verify this information with theseus team.  Kind regards,&nbsp;  
ODC team
July 17 11:36 AM WESTwebRootlySend ZenDesk private comment has been unsetJuly 17 11:36 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

July 17 12:54 PM WESTwebRootlyZendesk Private Comment has been set: ----------------------------------------------**Update to R&amp;D**- Hi team, here's the picture:- ![](https://www.outsystems.com/SupportPortal/DownloadAmazon.aspx?FileName=1721213897000__1721213896867.png&amp;TicketGUID=c39f3f85-8f06-4d4c-a079-6f7d0b1f63f6)- Let me know if you are able to see it.__July 17 12:54 PM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**- Hi team, here's the picture:- ![](https://www.outsystems.com/SupportPortal/DownloadAmazon.aspx?FileName=1721213897000__1721213896867.png&amp;TicketGUID=c39f3f85-8f06-4d4c-a079-6f7d0b1f63f6)- Let me know if you are able to see it.__
July 17  2:48 PM WESTwebJo&atilde;o SemedoSwarm has been set: TheseusJuly 17  2:48 PM WESTwebRootly[PagerDuty Incident](https://outsystems.pagerduty.com/incidents/Q0KYKTYKF249ES) has been created.
📧 Notified Marco Martins by email.&nbsp;&nbsp;📲 Notified Marco Martins by push notification.  (via Android)July 17  2:49 PM WESTwebRootly
Marco Martins acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q0KYKTYKF249ES). (via Website)
July 17  2:52 PM WESTwebJo&atilde;o Semedo
Hi team, we clarified that the user doesn&rsquo;t have any custom domains, and since we don&rsquo;t have the tools to undestand the root cause for the user discrepancy. I&rsquo;m assigning this issue to your team
July 17  2:53 PM WESTwebJo&atilde;o Semedo
Teams has been removed: ALM Consoles
July 17  2:55 PM WESTwebMarco MartinsSend ZenDesk private comment has been set: Hello Global Support,  This is a known issue that we are currently working on to fix, once we have this fixed and the change reaches GA, we'll get back to you.  Kind regards,  
Theseus TeamJuly 17  2:55 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hello Global Support,  This is a known issue that we are currently working on to fix, once we have this fixed and the change reaches GA, we'll get back to you.  Kind regards,  
Theseus Team
July 17  2:55 PM WESTwebRootlySend ZenDesk private comment has been unsetJuly 17  2:56 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

July 17  3:54 PM WESTwebRootlyZendesk Private Comment has been changed to: ------------------------------------------------ This notification was sent from Zendesk Support ticket #3036985 to all linked JIRA issues by Gon&ccedil;alo Cruz. --**Update to R&amp;D**
Hi Miguel,I filtered the users by active users and the count was exactly the same._&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_July 17  3:54 PM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
------------------------------------------------ This notification was sent from Zendesk Support ticket #3036985 to all linked JIRA issues by Gon&ccedil;alo Cruz. --**Update to R&amp;D**
Hi Miguel,I filtered the users by active users and the count was exactly the same.__
July 17  4:58 PM WESTwebJames Waller
Teams has been added: Identity Core
July 18  3:17 PM WESTwebJo&atilde;o Semedo
Jo&atilde;o Semedo has been unassigned from Engineer
July 22 10:28 AM WESTwebMarco Martins
As it turns out this is an Identity issue, so we'll move this to them (the JIRA RDINC-27239 has already been moved to Identity, so we are just updating this here and in pagerduty)
July 22 10:28 AM WESTwebMarco Martins
Teams has been removed: Neo Platform Theseus
July 22 10:29 AM WESTwebRootly
Delegated to EP for Platform Identity Core by Marco Martins through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q0KYKTYKF249ES)
July 22 10:29 AM WESTwebRootly
Jorge Mar&iacute;n acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q0KYKTYKF249ES). (via Website)
July 30  9:42 AM WESTwebJorge Marin
Similar to https://rootly.com/account/incidents/629-wrong-external-user-numbers-on-odc
We dont see an immediate reason for the count to be wrong. There is one thing that could explain it and that is the &quot;last_login&quot; showed in Portal when filtering users is not the same as the &quot;last_login&quot; used by the count process. The count process checks the last login to the production environment, while the portal shows the last login across all tenant/environments.
July 30  9:42 AM WESTwebJorge Marin
Similar to https://rootly.com/account/incidents/629-wrong-external-user-numbers-on-odc
We dont see an immediate reason for the count to be wrong. There is one thing that could explain it and that is the &quot;last_login&quot; showed in Portal when filtering users is not the same as the &quot;last_login&quot; used by the count process. The count process checks the last login to the production environment, while the portal shows the last login across all tenant/environments.
August 1 11:40 AM WESTwebPatr&iacute;cia SobreiraSend ZenDesk private comment has been set: Hello Support Team,  We think that there was some miscommunication/confusion about Count Users requirements, so let's start over again :)  
&nbsp;  
The requirements/information that we R&amp;D have (and had) to implement this are on this [HLD](https://outsystemsrd.atlassian.net/wiki/spaces/RDSD/pages/3362422812/ODC+Telemetry+and+Entitlement+Usage+Architecture+Direction#How-to-calculate-Active-End-Users):  The calculation of Active Users will rely on:*   End Users (users with access to applications)
*   **If the user is active and has ever logged in to a specific app/environment**
*   The result must be separated by internal vs external
*   ODC must be able to store the definition of internal email domains per tenant.Note: Bullet 2 meaning if the user login once at 3 years ago he is an active user (example).  This must be clear for you support and costumer. Can you please reach out&nbsp; PM [@Daniel Ara&uacute;jo](https://outsystems.slack.com/team/UUZRBHKA5) to understand where is this information is available for costumers? Also additional functional clarifications we also ask to be put to the PM [@Daniel Ara&uacute;jo](https://outsystems.slack.com/team/UUZRBHKA5).  Note: We had some previous tickets requesting clarifications already [RDINC-20320](https://outsystemsrd.atlassian.net/browse/RDINC-20320?focusedCommentId=1104476).  Please let us know if we can help in anything else,  
Identity Core TeamAugust 1 11:40 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hello Support Team,  We think that there was some miscommunication/confusion about Count Users requirements, so let's start over again :)  
&nbsp;  
The requirements/information that we R&amp;D have (and had) to implement this are on this [HLD](https://outsystemsrd.atlassian.net/wiki/spaces/RDSD/pages/3362422812/ODC+Telemetry+and+Entitlement+Usage+Architecture+Direction#How-to-calculate-Active-End-Users):  The calculation of Active Users will rely on:*   End Users (users with access to applications)
*   **If the user is active and has ever logged in to a specific app/environment**
*   The result must be separated by internal vs external
*   ODC must be able to store the definition of internal email domains per tenant.Note: Bullet 2 meaning if the user login once at 3 years ago he is an active user (example).  This must be clear for you support and costumer. Can you please reach out&nbsp; PM [@Daniel Ara&uacute;jo](https://outsystems.slack.com/team/UUZRBHKA5) to understand where is this information is available for costumers? Also additional functional clarifications we also ask to be put to the PM [@Daniel Ara&uacute;jo](https://outsystems.slack.com/team/UUZRBHKA5).  Note: We had some previous tickets requesting clarifications already [RDINC-20320](https://outsystemsrd.atlassian.net/browse/RDINC-20320?focusedCommentId=1104476).  Please let us know if we can help in anything else,  
Identity Core Team
August 1 11:40 AM WESTwebRootlySend ZenDesk private comment has been unsetAugust 1 11:40 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

August 12  8:58 AM WESTwebJorge Marin
Incident has been mitigated
August 12 10:08 AM WESTwebRootly
The Global Support team marked this incident as closed in ZenDesk.
August 12 10:08 AM WESTwebRootly
Incident has been resolved
August 12 10:08 AM WESTwebRootlyZenDesk Event Type has been set: solved