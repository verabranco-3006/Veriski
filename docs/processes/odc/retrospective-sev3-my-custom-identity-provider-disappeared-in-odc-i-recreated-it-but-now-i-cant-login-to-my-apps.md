---
title: Retrospective-SEV3-My custom identity provider disappeared in ODC, I recreated it but now I can't login to my apps.
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4310433984/Retrospective-SEV3-My+custom+identity+provider+disappeared+in+ODC+I+recreated+it+but+now+I+can+t+login+to+my+apps.
confluence_space: RKB
confluence_page_id: 4310433984
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV3-My custom identity provider disappeared in ODC, I recreated it but now I can't login to my apps.

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV3

Teams:&nbsp;trueBlueIdentity Business
#### 🕐 Timestamps
Started At:&nbsp;trueBlueJuly 25  7:57 AM WEST

Mitigated At:&nbsp;trueYellowJuly 25 12:06 PM WEST

Resolved At:&nbsp;trueGreenJuly 25 12:06 PM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/753-my-custom-identity-provider-disappeared-in-odc-i-recreated-it-but-now-i-can-t-login-to-my-apps)
[Pagerduty incident](https://outsystems.pagerduty.com/incidents/Q1AVWTW144ON5L)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3040546)

#### Summary
----------------------------------------------**R&amp;D ESCALATION FORM**
Section comments can be removed for R&amp;D easier interpretation.**ISSUE DESCRIPTION AND HOW TO REPRODUCE**
Our colleague opened the following ticket reporting that their Custom Identity Provider disappeared in ODC. They recreated it by couldn't login to the apps.
Here it seems when users start to fail with the login where the users ID's are not found: https://outsystems.grafana.net/d/cdh4sw1jvc8aof/identity-logs?orgId=1&amp;var-rings=osall&amp;var-regionShort=All&amp;var-severity=Error&amp;var-search=fae0814c-7560-49cc-886f-6b4eccb6709f&amp;from=now-2d&amp;to=nowThen he recreated the provider: https://outsystems.grafana.net/d/cdh4sw1jvc8aof/identity-logs?orgId=1&amp;var-rings=osall&amp;va[&hellip;]ae0814c-7560-49cc-886f-6b4eccb6709f%27&amp;from=now-2d&amp;to=now![](https://supportoutsystems.zendesk.com/attachments/token/gezu3TSsjWGq1GLXjPYdi4ine/?name=image.png)Here we can see the hidden IDP still working: https://outsystems.grafana.net/d/cdh4sw1jvc8aof/identity-logs?orgId=1&amp;var-rings=osall&amp;va[&hellip;]h=7eefa2bc-6b2b-4c00-8cd2-b4e8ed9985d5&amp;from=now-2d&amp;to=nowUntil Pedro configured it again:![](https://supportoutsystems.zendesk.com/attachments/token/3R9teZwip4my5AQV8B3y7hERC/?name=image.png)Around 8 AM is when the error started to occurs:
https://outsystems.grafana.net/d/cdh4sw1jvc8aof/identity-logs?orgId=1&amp;var-rings=osall&amp;var-regionShort=All&amp;var-severity=Warning&amp;var-severity=Error&amp;var-search=7eefa2bc-6b2b-4c00-8cd2-b4e8ed9985d5&amp;from=now-2d&amp;to=nowBut we can't decipher when it disappeared from the Portal.**IMPACT ON THE CUSTOMER**
Although they mentioned that it didn't work after recreating, we tried after together and it works already. They were testing immediately after the configuration thus the error. So it was reduced to sev3**TROUBLESHOOTING STEPS &amp; WORKAROUND**
Recreated the IdP**TECH DATA OR ANY OTHER RELEVANT INFO**
Ring: osall
Tenant Id: fae0814c-7560-49cc-886f-6b4eccb6709f
Tenant Prefix: extranet
Region: us-east-1
DMN.GTF.J1V.N02.OHY.ZDO.UBL.WTS_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_Attachment(s):
image (29).png - https://supportoutsystems.zendesk.com/attachments/token/WIu1Dmq6MTypNKs8teMQlLDK7/?name=image+%2829%29.pngimage (30).png - https://supportoutsystems.zendesk.com/attachments/token/SbDnXSlwlipT2UMxXCorhQcYf/?name=image+%2830%29.png
## 📝 RetrospectiveinfoDetails
**Ring:** osall
**System-wide impact:**&nbsp; No
**Tenant ID:** fae0814c-7560-49cc-886f-6b4eccb6709f
**Tenant Prefix:** extranet
**Routing Error Code:** N/A
**Product Area:** Phoenix::Phoenix Portal::Access management
### Impact:
The impact was on this current tenant and on one more tenant. It resulted in having the custom identity provider that they were using removed because it was missing some mandatory settings needed for the new database that we are migrating to. For the second tenant, we already let support know about who they are and how it can be fixed.
### Investigation and troubleshooting findings:
Considering this is OSALL and we recently performed the migration of Identity Providers from DynamoDB to RDS, we were thinking from the start it might be related to this. Investigating the logs revealed that this Identity Provider was not migrated to RDS due to missing configurations. But this Identity Provider was still in use so it caused issues for the customer. The workaround was to create the Identity Provider again.
### Resolution:
We have a task on Identity Business to improve the migration before going to EA and GA: [https://outsystemsrd.atlassian.net/browse/RDPIB-1849](https://outsystemsrd.atlassian.net/browse/RDPIB-1849)
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/753-my-custom-identity-provider-disappeared-in-odc-i-recreated-it-but-now-i-can-t-login-to-my-apps)

**Date**

**Source**

**User**

**Event**
July 24  4:05 PM WESTwebRootly
created an alert via
July 24  4:05 PM WESTwebRootly
Rootly created this incident
July 24  4:05 PM WESTwebRootly
In triage date has been set to July 24  4:05 PM WEST
July 24  4:19 PM WESTwebTelmo Martins
Teams has been added: Identity Business
July 24  4:19 PM WESTwebTelmo Martins
Teams has been removed: ODC Governance
July 24  4:20 PM WESTwebTelmo Martins
Hello Identity Biz team
Can you kindly help to check what might happened.
July 24  4:20 PM WESTwebTelmo Martins
Hello Identity Biz team
Can you kindly help to check what might happened.
July 24  4:21 PM WESTwebTelmo Martins
We already confirmed that from Portal, in that tenant, in the last seven days no provider was deleted
July 24  4:21 PM WESTwebTelmo MartinsSwarm has been set: Identity BusinessJuly 24  4:21 PM WESTwebRootly[PagerDuty Incident](https://outsystems.pagerduty.com/incidents/Q1AVWTW144ON5L) has been created.
📧 Notified Loredana Negoita by email.&nbsp;&nbsp;📱 Notified Loredana Negoita by SMS.&nbsp;&nbsp;📞 Notified Loredana Negoita by phone.July 24  4:22 PM WESTwebRootly
Loredana Negoita acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q1AVWTW144ON5L). (via Phone)
July 25  7:57 AM WESTwebLoredana-Gabriela Negoita
Incident has been started
July 25  8:30 AM WESTwebLoredana-Gabriela NegoitaSend ZenDesk private comment has been set: Hello team,  We are in a process of migrating the Identity Providers to a new database. This is done up to ring OSALL. During this migration, we enforced the settings in the new database and wrongly decided to skip the Identity Providers that were missing the settings. So it disappeared because we started reading from the new database that is not containing the old IdP.  Before continuing with the next rings, we will take this feedback and not skip this kind of Identity Providers anymore. If you have other instances of Identity Providers that disappeared, it might be due to this. We identified only one more tenant where 1 was skipped (tenant id 3082f862-8b50-4e25-9c79-7acede7da8f4).  I believe we can close this ticket now that we know the root cause and we are working on a fix.  Best regardsJuly 25  8:30 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hello team,  We are in a process of migrating the Identity Providers to a new database. This is done up to ring OSALL. During this migration, we enforced the settings in the new database and wrongly decided to skip the Identity Providers that were missing the settings. So it disappeared because we started reading from the new database that is not containing the old IdP.  Before continuing with the next rings, we will take this feedback and not skip this kind of Identity Providers anymore. If you have other instances of Identity Providers that disappeared, it might be due to this. We identified only one more tenant where 1 was skipped (tenant id 3082f862-8b50-4e25-9c79-7acede7da8f4).  I believe we can close this ticket now that we know the root cause and we are working on a fix.  Best regards
July 25  8:30 AM WESTwebRootlySend ZenDesk private comment has been unsetJuly 25  8:30 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

July 25  9:22 AM WESTwebRootlyZendesk Private Comment has been set: ----------------------------------------------**Update to R&amp;D**
- Hello teamPlease share the fix link for the issue for us to link it to the JIRA case.Cheers__July 25  9:22 AM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
- Hello teamPlease share the fix link for the issue for us to link it to the JIRA case.Cheers__
July 25  9:22 AM WESTwebRootlyZendesk Private Comment has been changed to: ------------------------------------------------ This notification was sent from Zendesk Support ticket #3040546 to all linked JIRA issues by Ricardo Moreira. --**Update to R&amp;D**- Hello teamPlease share the fix link for the issue for us to link it to the JIRA case.Cheers_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_July 25  9:22 AM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
------------------------------------------------ This notification was sent from Zendesk Support ticket #3040546 to all linked JIRA issues by Ricardo Moreira. --**Update to R&amp;D**- Hello teamPlease share the fix link for the issue for us to link it to the JIRA case.Cheers__
July 25 10:11 AM WESTwebLoredana-Gabriela NegoitaSend ZenDesk private comment has been set: Hello team,  Here is our ticket: https://outsystemsrd.atlassian.net/browse/RDPIB-1849  Thank youJuly 25 10:11 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hello team,  Here is our ticket: https://outsystemsrd.atlassian.net/browse/RDPIB-1849  Thank you
July 25 10:11 AM WESTwebRootlySend ZenDesk private comment has been unsetJuly 25 10:11 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

July 25 11:56 AM WESTwebRootlyZenDesk Event Type has been set: solvedJuly 25 11:56 AM WESTwebRootly
The Global Support team marked this incident as closed in ZenDesk.
July 25 12:06 PM WESTwebLoredana-Gabriela Negoita
Incident has been resolved
July 25 12:06 PM WESTwebLoredana-Gabriela NegoitaSystem-wide impact has been set: NoJuly 25 12:06 PM WESTwebLoredana-Gabriela NegoitaImpact has been set: The impact was on this current tenant and on one more tenant. It resulted in having the custom identity provider that they were using removed because it was missing some mandatory settings needed for the new database that we are migrating to. For the second tenant, we already let support know about who they are and how it can be fixed.July 25 12:06 PM WESTwebLoredana-Gabriela NegoitaInvestigation and troubleshooting findings has been set: Considering this is OSALL and we recently performed the migration of Identity Providers from DynamoDB to RDS, we were thinking from the start it might be related to this. Investigating the logs revealed that this Identity Provider was not migrated to RDS due to missing configurations. But this Identity Provider was still in use so it caused issues for the customer. The workaround was to create the Identity Provider again.July 25 12:06 PM WESTwebLoredana-Gabriela NegoitaResolution has been set: We have a task on Identity Business to improve the migration before going to EA and GA: https://outsystemsrd.atlassian.net/browse/RDPIB-1849