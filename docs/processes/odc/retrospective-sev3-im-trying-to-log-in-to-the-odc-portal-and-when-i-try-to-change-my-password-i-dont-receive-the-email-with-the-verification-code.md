---
title: Retrospective-SEV3-I'm trying to log in to the ODC portal and when I try to change my password I don't receive the email with the verification code.
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4306010975/Retrospective-SEV3-I+m+trying+to+log+in+to+the+ODC+portal+and+when+I+try+to+change+my+password+I+don+t+receive+the+email+with+the+verification+code.
confluence_space: RKB
confluence_page_id: 4306010975
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV3-I'm trying to log in to the ODC portal and when I try to change my password I don't receive the email with the verification code.

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV3

Teams:&nbsp;trueBlueIdentity Business
#### 🕐 Timestamps
Started At:&nbsp;trueBlueJuly 12 11:03 AM WEST

Mitigated At:&nbsp;trueYellowJuly 24 10:28 AM WEST

Resolved At:&nbsp;trueGreenJuly 24 10:28 AM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/702-i-m-trying-to-log-in-to-the-odc-portal-and-when-i-try-to-change-my-password-i-don-t-receive-the-email-with-the-verification-code)
[Pagerduty incident](https://outsystems.pagerduty.com/incidents/Q2NTMYLCP7RU16)

[Slack channel](https://slack.com/app_redirect?channel=C07BZ5K20BF&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3034710)

#### Summary
----------------------------------------------**CONSIDERATIONS BEFORE PERFORMING THE ESCALATION TO R&amp;D (MANDATORY)**
None of the below points should be overlooked. Failure to do so may imply unnecessary effort.* * *
Ensure the ticket has been **categorized**, otherwise, the R&amp;D escalation will go unnoticed and not be worked on!**1.** For **Incidents**, the **IMAX** was consulted **beforehand** on which:- No incident models were found for the reported symptoms **OR**
- The incident model did not solve the issue **OR**
- The next step indicated in the Incident Model is an escalation to R&amp;D.
**2.** For **Questions**, the ChatODC on the **Slack channel** didn't return an acceptable answer.
**3.** Any other requests that explicitly indicate an R&amp;D escalation is needed.
**4**. **Incident impact assessment** was based on the **prioritization scoring matrix**.* * ***R&amp;D ESCALATION FORM**
Section comments can be removed for R&amp;D easier interpretation.**ISSUE DESCRIPTION AND HOW TO REPRODUCE**- An organization member of this Tenant is unable to reset their password; when they click on &quot;forgot password?&quot;, they're redirected to the correct flow, but they never receive the password reset email.- We can see in Identity Logs (https://outsystems.grafana.net/goto/GfczWflIR?orgId=1) that when she tries to reset her password, an error is thrown in the Identity Business Backend:
- `The user '24e0b5b4-747b-4b1b-b8c1-16db993aba08' doesnt have a cognito profile`- The user states that she was invited to this Tenant yesterday (July 10th), and we can confirm that an invitation email was sent at 8:34 AM (UTC) in the Identity Logs (https://outsystems.grafana.net/goto/ZUmNWflIg?orgId=1):
- `Email was successfully sent through SES to m***e@nttdata.com`- However, when she tries to accept the invitation, she's simply redirected to the login screen. And they cannot send a new invitation or re-invite her because her account is already active:
- ![](https://supportoutsystems.zendesk.com/attachments/token/10HYUlXzMIecukerh2t3Re7Nm/?name=2024_07_11_14_49_50__ODCProfile+%282%29.png)
- ![](https://supportoutsystems.zendesk.com/attachments/token/hyzdbFgoWm1r2RTaPlUzGiUc0/?name=2024_07_11_14_49_50__ODCProfile%281%29.png)**IMPACT ON THE CUSTOMER**- This user is unable to access the tenant to start working on a project, though she's the only affected user.**TROUBLESHOOTING STEPS &amp; WORKAROUND**- We've seen this pattern in cases where a customer has an external IdP configured for organization access, but this tenant does not have that, the only way to log into ODC Portal is through the built-in IdP.- Can you help us understand what's causing an error to be thrown stating that this user doesn't have a profile in Cognito? Since she was invited through ODC Portal, and her account is active, I would imagine her profile to exist in the organization, so we're having a hard time understanding what's causing this error to occur.**TECH DATA OR ANY OTHER RELEVANT INFO**- Ring: ea
- Tenant Id: 5167f99c-5c3a-4b76-af38-d3ad8877f7da
- Tenant Prefix: ntt-data
- Region: eu-central-1_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 RetrospectiveinfoDetails
**Ring:** ea
**System-wide impact:**&nbsp; No
**Tenant ID:** 5167f99c-5c3a-4b76-af38-d3ad8877f7da
**Tenant Prefix:** ntt-data
**Routing Error Code:** N/A
**Product Area:** Phoenix::Phoenix Portal::Access management
### Impact:
One developer was not able to reset the password and access the account.
### Investigation and troubleshooting findings:
The team checked the DynamoDB table, the RDS table and Cognito.

The user was not present in Cognito and as a consequence, not able to reset the password. Considering the user was created some months ago, we don't have a way to check the logs and determine the reason why the user was not created there. Everything else was correct.
### Resolution:
The customer was unblocked by getting a new user, using the same email with +1.
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/702-i-m-trying-to-log-in-to-the-odc-portal-and-when-i-try-to-change-my-password-i-don-t-receive-the-email-with-the-verification-code)

**Date**

**Source**

**User**

**Event**
July 11  5:50 PM WESTwebRootly
created an alert via
July 11  5:50 PM WESTwebRootly
Rootly created this incident
July 11  5:50 PM WESTwebRootly
In triage date has been set to July 11  5:50 PM WEST
July 11  6:02 PM WESTwebRootly[Slack Channel](https://slack.com/app_redirect?channel=C07BZ5K20BF&amp;team=T041063TZ) has been createdJuly 12 11:03 AM WESTwebAnt&oacute;nio Rodrigues
Incident has been started
July 12 12:32 PM WESTwebAnt&oacute;nio RodriguesSwarm has been set: Identity BusinessJuly 12 12:32 PM WESTwebRootly[PagerDuty Incident](https://outsystems.pagerduty.com/incidents/Q2NTMYLCP7RU16) has been created.
📲 Notified Mark Bonnot by push notification.  (via iPhone)&nbsp;&nbsp;📲 Notified Mark Bonnot by push notification.  (via iPhone)July 12 12:33 PM WESTwebRootly
Mark Bonnot acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q2NTMYLCP7RU16). (via Slack)
July 15 10:16 AM WESTwebCatarina Gon&ccedil;alves
Teams has been removed: ODC Governance
July 15  1:16 PM WESTwebMark BonnotSend ZenDesk private comment has been set: We can tell the client to unblock them that they can delete that user and re-invite themJuly 15  1:16 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
We can tell the client to unblock them that they can delete that user and re-invite them
July 15  1:16 PM WESTwebRootlySend ZenDesk private comment has been unsetJuly 15  1:16 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

July 15  2:22 PM WESTwebRootlyZendesk Private Comment has been set: ----------------------------------------------**Update to R&amp;D**
Hey team!Thanks for your input, and before we suggest that the customer delete and re-invite the user, a few considerations:- Is the cause of this issue already clear? If so, would it be possible to share those details with us? This will be beneficial to us whether this behavior is expected or not:- If the behavior is expected, understanding why and how to identify when it occurs will allow us to document this on our side and solve future cases more swiftly (without requiring your interaction).- If the behavior is not expected, it's also important to know what's causing this so that we can identify it, document and mitigate it autonomously (if possible) until the root cause is resolved.
- If the cause is not clear, will you be able to continue this investigation after the account is deleted? If so, great, if not, it may do more harm than good to solve this without an understanding of whether it may occur again to other developers.In the meantime, we also need to say that the customer has escalated the case on our side, due to the fact that the affected developer has now run out of tasks that do not depend on this organization, so she is individually blocked.I just thought of trying to unblock her by invite her email suffixed with +1 prior to the domain (mariana.santos.valente+1@nttdata.com). This may unblock her access for the time being. If this does not work, we may be forced to raise the priority of this case to High/Sev-2 based until another workaround (such as deleting the account) is proven to be successful.Thanks in advance for your help!Best ergards,__July 15  2:22 PM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
Hey team!Thanks for your input, and before we suggest that the customer delete and re-invite the user, a few considerations:- Is the cause of this issue already clear? If so, would it be possible to share those details with us? This will be beneficial to us whether this behavior is expected or not:- If the behavior is expected, understanding why and how to identify when it occurs will allow us to document this on our side and solve future cases more swiftly (without requiring your interaction).- If the behavior is not expected, it's also important to know what's causing this so that we can identify it, document and mitigate it autonomously (if possible) until the root cause is resolved.
- If the cause is not clear, will you be able to continue this investigation after the account is deleted? If so, great, if not, it may do more harm than good to solve this without an understanding of whether it may occur again to other developers.In the meantime, we also need to say that the customer has escalated the case on our side, due to the fact that the affected developer has now run out of tasks that do not depend on this organization, so she is individually blocked.I just thought of trying to unblock her by invite her email suffixed with +1 prior to the domain (mariana.santos.valente+1@nttdata.com). This may unblock her access for the time being. If this does not work, we may be forced to raise the priority of this case to High/Sev-2 based until another workaround (such as deleting the account) is proven to be successful.Thanks in advance for your help!Best ergards,__
July 15  2:22 PM WESTwebRootlyZendesk Private Comment has been changed to: ------------------------------------------------ This notification was sent from Zendesk Support ticket #3034710 to all linked JIRA issues by Gon&ccedil;alo Silva. --**Update to R&amp;D**
Hey team!Thanks for your input, and before we suggest that the customer delete and re-invite the user, a few considerations:- Is the cause of this issue already clear? If so, would it be possible to share those details with us? This will be beneficial to us whether this behavior is expected or not:- If the behavior is expected, understanding why and how to identify when it occurs will allow us to document this on our side and solve future cases more swiftly (without requiring your interaction).- If the behavior is not expected, it's also important to know what's causing this so that we can identify it, document and mitigate it autonomously (if possible) until the root cause is resolved.
- If the cause is not clear, will you be able to continue this investigation after the account is deleted? If so, great, if not, it may do more harm than good to solve this without an understanding of whether it may occur again to other developers.In the meantime, we also need to say that the customer has escalated the case on our side, due to the fact that the affected developer has now run out of tasks that do not depend on this organization, so she is individually blocked.I just thought of trying to unblock her by invite her email suffixed with 1 prior to the domain (mariana.santos.valente1@nttdata.com). This may unblock her access for the time being. If this does not work, we may be forced to raise the priority of this case to High/Sev-2 based until another workaround (such as deleting the account) is proven to be successful.Thanks in advance for your help!Best ergards,_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_July 15  2:22 PM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
------------------------------------------------ This notification was sent from Zendesk Support ticket #3034710 to all linked JIRA issues by Gon&ccedil;alo Silva. --**Update to R&amp;D**
Hey team!Thanks for your input, and before we suggest that the customer delete and re-invite the user, a few considerations:- Is the cause of this issue already clear? If so, would it be possible to share those details with us? This will be beneficial to us whether this behavior is expected or not:- If the behavior is expected, understanding why and how to identify when it occurs will allow us to document this on our side and solve future cases more swiftly (without requiring your interaction).- If the behavior is not expected, it's also important to know what's causing this so that we can identify it, document and mitigate it autonomously (if possible) until the root cause is resolved.
- If the cause is not clear, will you be able to continue this investigation after the account is deleted? If so, great, if not, it may do more harm than good to solve this without an understanding of whether it may occur again to other developers.In the meantime, we also need to say that the customer has escalated the case on our side, due to the fact that the affected developer has now run out of tasks that do not depend on this organization, so she is individually blocked.I just thought of trying to unblock her by invite her email suffixed with 1 prior to the domain (mariana.santos.valente1@nttdata.com). This may unblock her access for the time being. If this does not work, we may be forced to raise the priority of this case to High/Sev-2 based until another workaround (such as deleting the account) is proven to be successful.Thanks in advance for your help!Best ergards,__
July 16 10:15 PM WESTwebMark Bonnot
Yes if we don't delete that user and re-invite them, we can keep troubleshooting that problem.
And also yes the client can invite that user with a &quot;+1&quot; added as suffix  to their email (Note not all email provider allow for this), that would allow that user to continue their work.
July 17  9:23 AM WESTwebRootlyZendesk Private Comment has been changed to: ----------------------------------------------**Update to R&amp;D**
Hey team,As a quick update, fortunately creating a new user usign the email mariana.santos.valente1@nttdata.com has unblocked this developer, so we've dodged the need of having to raise this case's priority, or to have to delete her user. Feel free to proceed with the investigation without the pressure of an immediate workaround, and please share the details of what you found so we can document this on our end.Thanks again for your help!Best regards,_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_July 17  9:23 AM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
Hey team,As a quick update, fortunately creating a new user usign the email mariana.santos.valente1@nttdata.com has unblocked this developer, so we've dodged the need of having to raise this case's priority, or to have to delete her user. Feel free to proceed with the investigation without the pressure of an immediate workaround, and please share the details of what you found so we can document this on our end.Thanks again for your help!Best regards,__
July 17  9:24 AM WESTwebRootlyZendesk Private Comment has been changed to: ------------------------------------------------ This notification was sent from Zendesk Support ticket #3034710 to all linked JIRA issues by Gon&ccedil;alo Silva. --**Update to R&amp;D**
Hey team,As a quick update, fortunately creating a new user usign the email mariana.santos.valente1@nttdata.com has unblocked this developer, so we've dodged the need of having to raise this case's priority, or to have to delete her user. Feel free to proceed with the investigation without the pressure of an immediate workaround, and please share the details of what you found so we can document this on our end.Thanks again for your help!Best regards,_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_July 17  9:24 AM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
------------------------------------------------ This notification was sent from Zendesk Support ticket #3034710 to all linked JIRA issues by Gon&ccedil;alo Silva. --**Update to R&amp;D**
Hey team,As a quick update, fortunately creating a new user usign the email mariana.santos.valente1@nttdata.com has unblocked this developer, so we've dodged the need of having to raise this case's priority, or to have to delete her user. Feel free to proceed with the investigation without the pressure of an immediate workaround, and please share the details of what you found so we can document this on our end.Thanks again for your help!Best regards,__
July 24 10:12 AM WESTwebLoredana-Gabriela NegoitaSend ZenDesk private comment has been set: Hello team,We continued the investigation for this and we confirmed that Cognito is enabled for this tenant and new users are being created successfully there.The initial user is not present in Cognito, but considering the last login is in April, it means this user was not created in the last moth, therefor we have no way to see the logs that are erased after 30 days.Considering the new registration worked, we think it might be related with a bug that might have been already fixed (we don't have a ticket, it is just an assumption).We have no other resources to help us continue the investigation, so considering the user is unblocked with a new email, we will need to close this ticket for now and keep an eye on similar issues if they will appear again.Best regardsJuly 24 10:12 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hello team,We continued the investigation for this and we confirmed that Cognito is enabled for this tenant and new users are being created successfully there.The initial user is not present in Cognito, but considering the last login is in April, it means this user was not created in the last moth, therefor we have no way to see the logs that are erased after 30 days.Considering the new registration worked, we think it might be related with a bug that might have been already fixed (we don't have a ticket, it is just an assumption).We have no other resources to help us continue the investigation, so considering the user is unblocked with a new email, we will need to close this ticket for now and keep an eye on similar issues if they will appear again.Best regards
July 24 10:12 AM WESTwebRootlySend ZenDesk private comment has been unsetJuly 24 10:12 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

July 24 10:28 AM WESTwebLoredana-Gabriela Negoita
Incident has been resolved
July 24 10:28 AM WESTwebLoredana-Gabriela NegoitaSystem-wide impact has been set: NoJuly 24 10:28 AM WESTwebLoredana-Gabriela NegoitaImpact has been set: One developer was not able to reset the password and access the account.July 24 10:28 AM WESTwebLoredana-Gabriela NegoitaInvestigation and troubleshooting findings has been set: The team checked the DynamoDB table, the RDS table and Cognito.
The user was not present in Cognito and as a consequence, not able to reset the password. Considering the user was created some months ago, we don't have a way to check the logs and determine the reason why the user was not created there. Everything else was correct.July 24 10:28 AM WESTwebLoredana-Gabriela NegoitaResolution has been set: The customer was unblocked by getting a new user, using the same email with +1.