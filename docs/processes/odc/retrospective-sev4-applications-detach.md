---
title: Retrospective-SEV4-Applications Detach
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4394615013/Retrospective-SEV4-Applications+Detach
confluence_space: RKB
confluence_page_id: 4394615013
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV4-Applications Detach

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV4

Teams:&nbsp;trueBlueRuntime Data Model&nbsp;trueBlueSre&nbsp;trueBlueBuild Services
#### 🕐 Timestamps
Started At:&nbsp;trueBlueAugust 16  6:05 PM WEST

Mitigated At:&nbsp;trueYellowAugust 21 10:08 AM WEST

Resolved At:&nbsp;trueGreenAugust 29  1:07 PM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/700-applications-detach-f83cc049-4903-404a-a9bc-f27b855cda05)
[Pagerduty incident](https://outsystems.pagerduty.com/incidents/Q3GDB3UIWAZ7XG)

[Slack channel](https://slack.com/app_redirect?channel=C07EM19KD28&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3029159)

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

Filipe Seixeira
#### Summary
----------------------------------------------**ISSUE DESCRIPTION AND HOW TO REPRODUCE**
The customer wants to initiate the detachment process of the following applications:- Assina Portal
- Client
- Assina Core**IMPACT ON THE CUSTOMER**
Because the license has already been terminated, we now have 30 days to complete this process.**TROUBLESHOOTING STEPS &amp; WORKAROUND**
In this case, there's nothing we can do but ensure alignment in how we carry out this request.
So, according to the information available in the slack channel #tmp-detach-odc, we'll be escalating to the runtime data model team to start detach operations. The expected outcome will be similar to the following list:- The source code for each **COS_App a**pplication currently deployed in the Production stage.
- A backup of your Application data.
- Instructions on how to compile the code.**TECH DATA OR ANY OTHER RELEVANT INFO**
- Tenant ID: 62d289a9-84de-4dca-8523-bbab2a7a52fe
- Activation Code: UON.0TG.XFT.9MX.T6N.DXI.AAL.QOU_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 RetrospectiveinfoDetails
**Ring:** ga
**System-wide impact:**&nbsp; 
**Tenant ID:** 62d289a9-84de-4dca-8523-bbab2a7a52fe
**Tenant Prefix:** assinarh
**Routing Error Code:** N/A
**Product Area:** Phoenix::Application Runtime::Database access
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/700-applications-detach-f83cc049-4903-404a-a9bc-f27b855cda05)

**Date**

**Source**

**User**

**Event**
July 11  3:19 PM WESTwebRootly
created an alert via
July 11  3:19 PM WESTwebRootly
Rootly created this incident
July 11  3:19 PM WESTwebRootly
In triage date has been set to July 11  3:19 PM WEST
July 12  4:06 PM WESTwebJoana BarradasJoana Barradas has been assigned as EngineerJuly 12  4:06 PM WESTwebJoana Barradas
Runbook created:  https://outsystemsrd.atlassian.net/wiki/x/g4AK-w
We are now waiting for SRE.
July 12  4:06 PM WESTwebJoana Barradas
Incident has been started
July 16 10:08 AM WESTwebTiago OliveiraAnt&oacute;nio Caeiro has been assigned as EngineerJuly 29  5:11 PM WESTwebPedro CardosoSend ZenDesk private comment has been set: Hi team,  Can you please ask the customer to provide the following information (required in order to share the database):  *    the customer needs to provide OutSystems with the ARN of the KMS key created;
*    created and provided by the customer. That account has to be in the same region as the customer's tenant;Best regards,  
Pedro CardosoJuly 29  5:11 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hi team,  Can you please ask the customer to provide the following information (required in order to share the database):  *    the customer needs to provide OutSystems with the ARN of the KMS key created;
*    created and provided by the customer. That account has to be in the same region as the customer's tenant;Best regards,  
Pedro Cardoso
July 29  5:11 PM WESTwebRootlySend ZenDesk private comment has been unsetJuly 29  5:12 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

July 29  5:13 PM WESTwebRootly[Slack Channel](https://slack.com/app_redirect?channel=C07EM19KD28&amp;team=T041063TZ) has been createdJuly 30 10:07 AM WESTwebHugo AraujoPedro Cardoso has been assigned as EngineerAugust 5  4:26 PM WESTwebMariana CabedaSend ZenDesk private comment has been set: Hello team!&nbsp;  
We've just attempted to share the database snapshot with the indicated KMS key but we have faced the following error (image bellow).```
Specified KMS key \[arn:aws:kms:us-east-2:010438481442:key/4fc2d53e-11b9-4825-b664-2cd9a1351878\] does not exist, is not enabled or you do not have permissions to access it.
```![image.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDI0NTcxLCJwdXIiOiJibG9iX2lkIn19--fafad5a90e9710beadaa82ad88b5546df70d1133/image.png)image.png 60.49 KBWe have validated though the previous communications that the customer's key was created in region us-east-2 which differs from the region where the current database exists (**us-east-1**). We believe this could be the source of the problem and with that request for the customer to create the key in the **us-east-1** region for us to be able to proceed with the database detach operation.  
After that process is completed, please re-share the new key arn.  Thank you for the patience while we work though this detach and please feel free to reach out if any questions arise.August 5  4:26 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hello team!&nbsp;  
We've just attempted to share the database snapshot with the indicated KMS key but we have faced the following error (image bellow).```
Specified KMS key \[arn:aws:kms:us-east-2:010438481442:key/4fc2d53e-11b9-4825-b664-2cd9a1351878\] does not exist, is not enabled or you do not have permissions to access it.
```![image.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDI0NTcxLCJwdXIiOiJibG9iX2lkIn19--fafad5a90e9710beadaa82ad88b5546df70d1133/image.png)image.png 60.49 KBWe have validated though the previous communications that the customer's key was created in region us-east-2 which differs from the region where the current database exists (**us-east-1**). We believe this could be the source of the problem and with that request for the customer to create the key in the **us-east-1** region for us to be able to proceed with the database detach operation.  
After that process is completed, please re-share the new key arn.  Thank you for the patience while we work though this detach and please feel free to reach out if any questions arise.
August 5  4:26 PM WESTwebRootlySend ZenDesk private comment has been unsetAugust 5  4:26 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

August 5  4:33 PM WESTwebMariana CabedaMariana Cabeda has been assigned as EngineerAugust 5  4:35 PM WESTslackmariana.cabeda
For reference, this incident is being discussed and handled in another channel since it was related with multiple incidents and any updates will be shared in here: &lt;#C072Y1B0H9D|&gt;
August 7  7:56 AM WESTwebRootlyZendesk Private Comment has been set: ----------------------------------------------**Update to R&amp;D**
Hey team,The customer says they couldn't find the option to select a specific region for their KMS Key, so they created it as multi-region, hopefully that'll be ok.Here's the ARN:- arn:aws:kms:us-east-2:010438481442:key/mrk-cb5b458dae2e4966a4d98a4b5a262498Good luck with the snapshot and let us know if you need anything from our, or the customer's, end!Best regards,__August 7  7:56 AM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
Hey team,The customer says they couldn't find the option to select a specific region for their KMS Key, so they created it as multi-region, hopefully that'll be ok.Here's the ARN:- arn:aws:kms:us-east-2:010438481442:key/mrk-cb5b458dae2e4966a4d98a4b5a262498Good luck with the snapshot and let us know if you need anything from our, or the customer's, end!Best regards,__
August 7  7:57 AM WESTwebRootlyZendesk Private Comment has been changed to: ------------------------------------------------ This notification was sent from Zendesk Support ticket #3029159 to all linked JIRA issues by Gon&ccedil;alo Silva. --**Update to R&amp;D**
Hey team,The customer says they couldn't find the option to select a specific region for their KMS Key, so they created it as multi-region, hopefully that'll be ok.Here's the ARN:- arn:aws:kms:us-east-2:010438481442:key/mrk-cb5b458dae2e4966a4d98a4b5a262498Good luck with the snapshot and let us know if you need anything from our, or the customer's, end!Best regards,_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_August 7  7:57 AM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
------------------------------------------------ This notification was sent from Zendesk Support ticket #3029159 to all linked JIRA issues by Gon&ccedil;alo Silva. --**Update to R&amp;D**
Hey team,The customer says they couldn't find the option to select a specific region for their KMS Key, so they created it as multi-region, hopefully that'll be ok.Here's the ARN:- arn:aws:kms:us-east-2:010438481442:key/mrk-cb5b458dae2e4966a4d98a4b5a262498Good luck with the snapshot and let us know if you need anything from our, or the customer's, end!Best regards,__
August 7 10:51 AM WESTwebMariana CabedaSend ZenDesk private comment has been set: Hello team, thanks for sharing that information.We have tested and are still unable to access the key due to the region restrictions.
In order for the customer to create the KMS key in the correct region, they'll first need to activate such region in their account, change the region on their AWS account and proceed to create the new key.Here is some helpful AWS documentation that explains how to enable a new region: [https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html)We'll be waiting for the new key arn once it is created in the **us-east-1 **region.Thank you!
Mariana CabedaAugust 7 10:51 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hello team, thanks for sharing that information.We have tested and are still unable to access the key due to the region restrictions.
In order for the customer to create the KMS key in the correct region, they'll first need to activate such region in their account, change the region on their AWS account and proceed to create the new key.Here is some helpful AWS documentation that explains how to enable a new region: [https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html)We'll be waiting for the new key arn once it is created in the **us-east-1 **region.Thank you!
Mariana Cabeda
August 7 10:51 AM WESTwebRootlySend ZenDesk private comment has been unsetAugust 7 10:51 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

August 8  1:50 AM WESTwebRootlyZendesk Private Comment has been changed to: ----------------------------------------------**Update to R&amp;D**
- Detail additional findings or any questions/concerns that may be important for R&amp;D to be aware of.Hi Team,The customer has created a new one and now in the region US East 1.arn:aws:kms:us-east-1:010438481442:key/3fec223c-c954-4c3f-a7f0-c4b33f1b73bdWe look forward to your update.With best regards,_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_August 8  1:50 AM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
- Detail additional findings or any questions/concerns that may be important for R&amp;D to be aware of.Hi Team,The customer has created a new one and now in the region US East 1.arn:aws:kms:us-east-1:010438481442:key/3fec223c-c954-4c3f-a7f0-c4b33f1b73bdWe look forward to your update.With best regards,__
August 8  1:50 AM WESTwebRootlyZendesk Private Comment has been changed to: ------------------------------------------------ This notification was sent from Zendesk Support ticket #3029159 to all linked JIRA issues by Shaharuddin Mohd Shah. --Hi Team,The customer has created a new one and now in the region US East 1.arn:aws:kms:us-east-1:010438481442:key/3fec223c-c954-4c3f-a7f0-c4b33f1b73bdWe look forward to your update.With best regards,&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment #trigger_update_r&amp;d_odc !&gt;August 8  1:50 AM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
------------------------------------------------ This notification was sent from Zendesk Support ticket #3029159 to all linked JIRA issues by Shaharuddin Mohd Shah. --Hi Team,The customer has created a new one and now in the region US East 1.arn:aws:kms:us-east-1:010438481442:key/3fec223c-c954-4c3f-a7f0-c4b33f1b73bdWe look forward to your update.With best regards,
August 9 10:02 AM WESTwebMariana CabedaSend ZenDesk private comment has been set: Hello Support!  We are pleased to inform you that we have now completed the database detach procedure and the snapshot has been shared with the customer. The ARN of the shared snapshot is 'arn:aws:rds:us-east-1:008971668326:cluster-snapshot:assina-rh-database-export-05-8-2024' and will be visible in the customer's AWS account under 'RDS &gt; Snapshots &gt; Shared with me'.  In order for the customer to be able to use the shared data, we have created a guide explaining the actions that will need to be taken. The document is attached in this message and can be shared directly with the customer.  Don't hesitate to reach out in case there are further questions.  
Thank you,  
Mariana CabedaAugust 9 10:02 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hello Support!  We are pleased to inform you that we have now completed the database detach procedure and the snapshot has been shared with the customer. The ARN of the shared snapshot is 'arn:aws:rds:us-east-1:008971668326:cluster-snapshot:assina-rh-database-export-05-8-2024' and will be visible in the customer's AWS account under 'RDS &gt; Snapshots &gt; Shared with me'.  In order for the customer to be able to use the shared data, we have created a guide explaining the actions that will need to be taken. The document is attached in this message and can be shared directly with the customer.  Don't hesitate to reach out in case there are further questions.  
Thank you,  
Mariana Cabeda
August 9 10:02 AM WESTwebRootlySend ZenDesk private comment has been unsetAugust 9 10:02 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

August 9 10:03 AM WESTwebMariana Cabeda
Here is the documentation to be shared with customer in order to use the detached data (I'm unable to link it directly in Zendesk)
August 9 10:05 AM WESTwebMariana CabedaSend ZenDesk private comment has been set: Hello Support, it seems I was unable to attach the document directly through the message to Global Support but have left it attached in my last comment in Rootly. Let me know if you have any issues accessing it.  
Thanks!August 9 10:05 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hello Support, it seems I was unable to attach the document directly through the message to Global Support but have left it attached in my last comment in Rootly. Let me know if you have any issues accessing it.  
Thanks!
August 9 10:05 AM WESTwebRootlySend ZenDesk private comment has been unsetAugust 9 10:05 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

August 9 10:22 AM WESTwebMariana Cabeda
Incident has been mitigated
August 9  5:29 PM WESTwebMariana Cabeda
Action Item - Follow-up: Delete shared snapshot. has been added.
August 16  6:04 PM WESTwebTiago OliveiraSwarm has been set: Build ServicesAugust 16  6:04 PM WESTwebRootly[PagerDuty Incident](https://outsystems.pagerduty.com/incidents/Q3GDB3UIWAZ7XG) has been created.
📧 Notified Diogo Rom&atilde;o by email.August 16  6:05 PM WESTwebTiago Oliveira
Incident has been started
August 16  6:07 PM WESTwebRootly
Diogo Rom&atilde;o acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q3GDB3UIWAZ7XG). (via Website)
August 19 10:06 AM WESTwebMariana CabedaNuno Bento has been assigned as EngineerAugust 19 10:06 AM WESTwebMariana Cabeda
Updated assigned engineer since the only pending topic at the moment is regarding the access to the source code.
August 19  3:12 PM WESTwebNuno Bento
Teams has been added: SRE
August 19  3:36 PM WESTwebNuno BentoFilipe Seixeira has been assigned as EngineerAugust 19  6:53 PM WESTwebFilipe SeixeiraSend ZenDesk private comment has been set: Hello GS,Can you please ask the customer to provide their public IP, so that we can add that as a rule on the s3 bucket policy in order to allow them to download the source code.thank youAugust 19  6:53 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hello GS,Can you please ask the customer to provide their public IP, so that we can add that as a rule on the s3 bucket policy in order to allow them to download the source code.thank you
August 19  6:53 PM WESTwebRootlySend ZenDesk private comment has been unsetAugust 19  6:53 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

August 20  2:34 PM WESTwebRootlyZendesk Private Comment has been changed to: ----------------------------------------------**Update to R&amp;D**
Hey Team,The customer just got back to us with its IP address: 179.113.244.144.Thank you._&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_August 20  2:35 PM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
Hey Team,The customer just got back to us with its IP address: 179.113.244.144.Thank you.__
August 20  2:43 PM WESTwebFilipe SeixeiraSend ZenDesk private comment has been set: Thank you for providing this.
The customer is now able to download the zip file from the s3 bucket using the link [https://assina-rh-temp-bucket.s3.amazonaws.com/Assina_source_code.zip](https://assina-rh-temp-bucket.s3.amazonaws.com/Assina_source_code.zip).August 20  2:43 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Thank you for providing this.
The customer is now able to download the zip file from the s3 bucket using the link [https://assina-rh-temp-bucket.s3.amazonaws.com/Assina_source_code.zip](https://assina-rh-temp-bucket.s3.amazonaws.com/Assina_source_code.zip).
August 20  2:43 PM WESTwebRootlySend ZenDesk private comment has been unsetAugust 20  2:43 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

August 21 10:08 AM WESTwebThiago Campos
Incident has been mitigated
August 29  1:07 PM WESTwebRootly
The Global Support team marked this incident as closed in ZenDesk.
August 29  1:07 PM WESTwebRootly
Incident has been resolved
August 29  1:07 PM WESTwebRootlyZenDesk Event Type has been set: solved## 📝 Follow Up Items[View on Rootly](https://rootly.com/account/incidents/700-applications-detach-f83cc049-4903-404a-a9bc-f27b855cda05#nav-action-items)

**Summary**

**Priority**

**Status**

**Assignee**

**Links**
https://outsystemsrd.atlassian.net/browse/RPLAT-2652trueYellowMediumtrueBlueOpenTiago Oliveira