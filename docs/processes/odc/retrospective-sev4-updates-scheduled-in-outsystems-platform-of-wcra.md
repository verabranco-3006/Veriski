---
title: Retrospective-SEV4-Updates scheduled in OutSystems Platform of WCRA
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4371841247/Retrospective-SEV4-Updates+scheduled+in+OutSystems+Platform+of+WCRA
confluence_space: RKB
confluence_page_id: 4371841247
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV4-Updates scheduled in OutSystems Platform of WCRA

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV4

Teams:&nbsp;trueBlueBuild Services
#### 🕐 Timestamps
Started At:&nbsp;trueBlueAugust 20  1:41 PM WEST

Mitigated At:&nbsp;trueYellowAugust 20  1:44 PM WEST

Resolved At:&nbsp;trueGreenAugust 20  1:44 PM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/687-updates-scheduled-in-outsystems-platform-of-wcra)
[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3033494)

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
- WCRA Admins received multiple emails on systems patching and updates:- RRCT-5465
- RRCT-5585
- RRCT-5689
- RRCT-5727
- RRCT-5651
- They received the first notification in March 2024 and have been receiving these emails (regarding the same updates) continuously until July 5, 2024.
- These notifications have raised a concern for them, and now they are wondering: Are updates failing, causing them to be rescheduled?**IMPACT ON THE CUSTOMER**
- There is no impact on the business as these patches and updates are executed automatically.
- Nevertheless, the frequency of the notifications they received for the same updates concerns them.
- The customer is now clarifying the action they need to take if the updates fail (for example; do they need to republish their app, etc?)**TROUBLESHOOTING STEPS &amp; WORKAROUND**
- NA**TECH DATA OR ANY OTHER RELEVANT INFO**- Customer: WCRA
- Ring: ga
- Tenant Id: 7a6b652e-728d-4329-a6f4-998aff1eb508
- Tenant Prefix: wcra
- Region: us-east-1
- AC: CHU.8Z6.KIU.GFQ.3H3.OIO.X8F.AUT_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 RetrospectiveinfoDetails
**Ring:** ga
**System-wide impact:**&nbsp; No
**Tenant ID:** 7a6b652e-728d-4329-a6f4-998aff1eb508
**Tenant Prefix:** wcra
**Routing Error Code:** N/A
**Product Area:** Phoenix::Patching::Application Patching
### Impact:
The apps failing are due to similar reasons: each application depends on an entity that is no longer exposed in a certain External Connection. 
### Investigation and troubleshooting findings:
More details here: [https://outsystemsrd.atlassian.net/browse/RDINC-26726?focusedCommentId=1160492](https://outsystemsrd.atlassian.net/browse/RDINC-26726?focusedCommentId=1160492)
### Resolution:
Remove the  2 affected applications:

DB Sandbox

RM Test
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/687-updates-scheduled-in-outsystems-platform-of-wcra)

**Date**

**Source**

**User**

**Event**
July 9  5:20 AM WESTwebRootly
created an alert via
July 9  5:20 AM WESTwebRootly
Rootly created this incident
July 9  5:20 AM WESTwebRootly
In triage date has been set to July 9  5:20 AM WEST
July 16 10:42 AM WESTwebRootlyZendesk Private Comment has been set: ----------------------------------------------**Update to R&amp;D**
- Detail additional findings or any questions/concerns that may be important for R&amp;D to be aware of.Dear Team,The customer reached out again about the scheduled update with the same RRCT:- RRCT-5585
- RRCT-5465
- RRCT-5689
- RRCT-5727
- RRCT-5651
On top of that, they received a notification of the completion of the updates on Monday, July 15, 2024, with an empty document attached to the email.They were wondering what is the content of the document.Can you kindly advise, what is the content of the document and why they keep on receiving notifications for their app to be updated for the same RRCT?We look forward to your feedback.Best regards,__July 16 10:42 AM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
- Detail additional findings or any questions/concerns that may be important for R&amp;D to be aware of.Dear Team,The customer reached out again about the scheduled update with the same RRCT:- RRCT-5585
- RRCT-5465
- RRCT-5689
- RRCT-5727
- RRCT-5651
On top of that, they received a notification of the completion of the updates on Monday, July 15, 2024, with an empty document attached to the email.They were wondering what is the content of the document.Can you kindly advise, what is the content of the document and why they keep on receiving notifications for their app to be updated for the same RRCT?We look forward to your feedback.Best regards,__
July 16 10:42 AM WESTwebRootlyZendesk Private Comment has been changed to: ------------------------------------------------ This notification was sent from Zendesk Support ticket #3033494 to all linked JIRA issues by Shaharuddin Mohd Shah. --Update to R&amp;D- Detail additional findings or any questions/concerns that may be important for R&amp;D to be aware of.Dear Team,The customer reached out again about the scheduled update with the same RRCT:
RRCT-5585
RRCT-5465
RRCT-5689
RRCT-5727
RRCT-5651
On top of that, they received a notification of the completion of the updates on Monday, July 15, 2024, with an empty document attached to the email.They were wondering what is the content of the document.Can you kindly advise, what is the content of the document and why they keep on receiving notifications for their app to be updated for the same RRCT?We look forward to your feedback.Best regards,&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment #trigger_update_r&amp;d_odc !&gt;July 16 10:42 AM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
------------------------------------------------ This notification was sent from Zendesk Support ticket #3033494 to all linked JIRA issues by Shaharuddin Mohd Shah. --Update to R&amp;D- Detail additional findings or any questions/concerns that may be important for R&amp;D to be aware of.Dear Team,The customer reached out again about the scheduled update with the same RRCT:
RRCT-5585
RRCT-5465
RRCT-5689
RRCT-5727
RRCT-5651
On top of that, they received a notification of the completion of the updates on Monday, July 15, 2024, with an empty document attached to the email.They were wondering what is the content of the document.Can you kindly advise, what is the content of the document and why they keep on receiving notifications for their app to be updated for the same RRCT?We look forward to your feedback.Best regards,
July 18  2:09 AM WESTwebRootlyZendesk Private Comment has been changed to: ----------------------------------------------**Update to R&amp;D**
- Detail additional findings or any questions/concerns that may be important for R&amp;D to be aware of.Hi Team,The customer again received a conflicting email notification that said the Required Update to your app has started, and the next email notification said that we scheduled (Development : Jul 29, 2024, 06:25 AM (UTC)) another required update for the same RRCT:- RRCT-5585
- RRCT-5465
- RRCT-5689
- RRCT-5727
- RRCT-5651![](https://supportoutsystems.zendesk.com/attachments/token/BVoBk9plf8FnzVca8M0HVOUCi/?name=image.png)Are the updates scheduled for July 29 a new update?We look forward to your feedback.Thank you in advance for your assistance._&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_July 18  2:09 AM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
- Detail additional findings or any questions/concerns that may be important for R&amp;D to be aware of.Hi Team,The customer again received a conflicting email notification that said the Required Update to your app has started, and the next email notification said that we scheduled (Development : Jul 29, 2024, 06:25 AM (UTC)) another required update for the same RRCT:- RRCT-5585
- RRCT-5465
- RRCT-5689
- RRCT-5727
- RRCT-5651![](https://supportoutsystems.zendesk.com/attachments/token/BVoBk9plf8FnzVca8M0HVOUCi/?name=image.png)Are the updates scheduled for July 29 a new update?We look forward to your feedback.Thank you in advance for your assistance.__
July 18  2:09 AM WESTwebRootlyZendesk Private Comment has been changed to: ------------------------------------------------ This notification was sent from Zendesk Support ticket #3033494 to all linked JIRA issues by Shaharuddin Mohd Shah. --Update to R&amp;D- Detail additional findings or any questions/concerns that may be important for R&amp;D to be aware of.Hi Team,The customer again received a conflicting email notification that said the Required Update to your app has started, and the next email notification said that we scheduled (Development : Jul 29, 2024, 06:25 AM (UTC)) another required update for the same RRCT:
RRCT-5585
RRCT-5465
RRCT-5689
RRCT-5727
RRCT-5651Are the updates scheduled for July 29 a new update?We look forward to your feedback.Thank you in advance for your assistance.&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment #trigger_update_r&amp;d_odc !&gt;July 18  2:10 AM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
------------------------------------------------ This notification was sent from Zendesk Support ticket #3033494 to all linked JIRA issues by Shaharuddin Mohd Shah. --Update to R&amp;D- Detail additional findings or any questions/concerns that may be important for R&amp;D to be aware of.Hi Team,The customer again received a conflicting email notification that said the Required Update to your app has started, and the next email notification said that we scheduled (Development : Jul 29, 2024, 06:25 AM (UTC)) another required update for the same RRCT:
RRCT-5585
RRCT-5465
RRCT-5689
RRCT-5727
RRCT-5651Are the updates scheduled for July 29 a new update?We look forward to your feedback.Thank you in advance for your assistance.
July 25  4:48 AM WESTwebRootlyZendesk Private Comment has been changed to: ----------------------------------------------**Update to R&amp;D**
- Detail additional findings or any questions/concerns that may be important for R&amp;D to be aware of.Hi Team,The customer has deleted the 2 affected applications:1. **DB Sandbox**
2. **RM Test**Since the update is scheduled for July 29, 2024, the customer is asking if anything needs to be done on their end.Looking forward to your feedback.With kind regards,_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_July 25  4:48 AM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
- Detail additional findings or any questions/concerns that may be important for R&amp;D to be aware of.Hi Team,The customer has deleted the 2 affected applications:1. **DB Sandbox**
2. **RM Test**Since the update is scheduled for July 29, 2024, the customer is asking if anything needs to be done on their end.Looking forward to your feedback.With kind regards,__
July 25  4:49 AM WESTwebRootlyZendesk Private Comment has been changed to: ------------------------------------------------ This notification was sent from Zendesk Support ticket #3033494 to all linked JIRA issues by Shaharuddin Mohd Shah. --Update to R&amp;D- Detail additional findings or any questions/concerns that may be important for R&amp;D to be aware of.Hi Team,The customer has deleted the 2 affected applications:
DB Sandbox
RM TestSince the update is scheduled for July 29, 2024, the customer is asking if anything needs to be done on their end.Looking forward to your feedback.With kind regards,&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment #trigger_update_r&amp;d_odc !&gt;July 25  4:49 AM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
------------------------------------------------ This notification was sent from Zendesk Support ticket #3033494 to all linked JIRA issues by Shaharuddin Mohd Shah. --Update to R&amp;D- Detail additional findings or any questions/concerns that may be important for R&amp;D to be aware of.Hi Team,The customer has deleted the 2 affected applications:
DB Sandbox
RM TestSince the update is scheduled for July 29, 2024, the customer is asking if anything needs to be done on their end.Looking forward to your feedback.With kind regards,
August 1  3:08 PM WESTwebRootlyZenDesk Event Type has been set: solvedAugust 1  3:08 PM WESTwebRootly
The Global Support team marked this incident as closed in ZenDesk.
August 20  1:41 PM WESTwebSara Gon&ccedil;alves
Teams has been added: BuildServices
August 20  1:41 PM WESTwebSara Gon&ccedil;alves
Teams has been removed: Maestro
August 20  1:41 PM WESTwebSara Gon&ccedil;alves
Incident has been started
August 20  1:44 PM WESTwebSara Gon&ccedil;alves
Incident has been resolved
August 20  1:44 PM WESTwebSara Gon&ccedil;alvesSystem-wide impact has been set: NoAugust 20  1:44 PM WESTwebSara Gon&ccedil;alvesImpact has been set: The apps failing are due to similar reasons: each application depends on an entity that is no longer exposed in a certain External Connection. August 20  1:44 PM WESTwebSara Gon&ccedil;alvesInvestigation and troubleshooting findings has been set: More details here: https://outsystemsrd.atlassian.net/browse/RDINC-26726?focusedCommentId=1160492August 20  1:44 PM WESTwebSara Gon&ccedil;alvesResolution has been set: Remove the  2 affected applications:
DB Sandbox
RM Test