---
title: Retrospective-SEV3-ODC - Deployment cannot proceed because required version information is missing
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4372627610/Retrospective-SEV3-ODC+-+Deployment+cannot+proceed+because+required+version+information+is+missing
confluence_space: RKB
confluence_page_id: 4372627610
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV3-ODC - Deployment cannot proceed because required version information is missing

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV3

Teams:&nbsp;trueBlueMaestro
#### 🕐 Timestamps
Started At:&nbsp;trueBlueJuly 10 12:42 PM WEST

Mitigated At:&nbsp;trueYellowAugust 20  1:37 PM WEST

Resolved At:&nbsp;trueGreenAugust 20  1:37 PM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/693-odc-deployment-cannot-proceed-because-required-version-information-is-missing)
[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3034558)

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

Tiago Cardoso
#### Summary
----------------------------------------------**ISSUE DESCRIPTION AND HOW TO REPRODUCE**
Customers are experiencing deployment issues because application versions are missing in previous tenants. It seems that the versions have disappeared.![](https://supportoutsystems.zendesk.com/attachments/token/RGZo6ObcK3MUxqrm45TSitnpd/?name=image.png)![](https://supportoutsystems.zendesk.com/attachments/token/jRPyiun7G2SkarVVrFVdEuQQa/?name=image.png)**IMPACT ON THE CUSTOMER**
When creating a new revision and publish it, the customer is able to see the previous version again.**TROUBLESHOOTING STEPS &amp; WORKAROUND**
Deploy the apps again throughout the tenants.**TECH DATA OR ANY OTHER RELEVANT INFO**- Ring: ga
- Tenant Id: fa222c80-3359-4c16-a2cd-ccdebdbd3b9d
- Tenant Prefix: neways
- Region: eu-central-1&amp;- Ring: ga
- Tenant Id: a98b924f-6c69-4ab1-8fb4-52ea5d5da885
- Tenant Prefix: qurator
- Region: eu-central-1
- SUD.LFU.YOX.QIS.QTQ.BHX.DDJ.WOU_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 RetrospectiveinfoDetails
**Ring:** ga
**System-wide impact:**&nbsp; No
**Tenant ID:** N/A
**Tenant Prefix:** N/A
**Routing Error Code:** N/A
**Product Area:** -
### Impact:
APS is a new service and in order to bootstrap the deployment data we had a job that ran periodically. In EU CENTRAL 1 the job overwhelmed AVS resulting in an error state that deleted some records from APS. 
### Investigation and troubleshooting findings:
We already removed the job ([https://outsystemsrd.atlassian.net/browse/RDMAST-1491](https://outsystemsrd.atlassian.net/browse/RDMAST-1491)) but the damage was already done. So to workaround this the customers need to do 1cp and deploy the affected apps to the next stages.
### Resolution:
The fix was done here: [https://outsystemsrd.atlassian.net/browse/RDMAST-1524](https://outsystemsrd.atlassian.net/browse/RDMAST-1524)
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/693-odc-deployment-cannot-proceed-because-required-version-information-is-missing)

**Date**

**Source**

**User**

**Event**
July 10 11:20 AM WESTwebRootly
created an alert via
July 10 11:20 AM WESTwebRootly
Rootly created this incident
July 10 11:21 AM WESTwebRootly
In triage date has been set to July 10 11:20 AM WEST
July 10 12:10 PM WESTwebRootlyZendesk Private Comment has been set: ----------------------------------------------**Update to R&amp;D**
- Hello TeamPlease use the Rootly case ID 693 instead of the 689 as we had to open a new one due to multiple reports of the same issue. 693 is covering all customers while 689 is related to a single customer.Thank you.__July 10 12:10 PM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
- Hello TeamPlease use the Rootly case ID 693 instead of the 689 as we had to open a new one due to multiple reports of the same issue. 693 is covering all customers while 689 is related to a single customer.Thank you.__
July 10 12:21 PM WESTwebJo&atilde;o Ros&aacute;rio
Teams has been added: Maestro
July 10 12:24 PM WESTwebJo&atilde;o Ros&aacute;rio
It seems to be the same as the https://rootly.com/account/incidents/689-warning-regard-non-existing-producer-app-while-deploying-across-stages-despite-app-availability however the customer already deployed the app to all stages and the issue is no longer happening.
July 10 12:42 PM WESTwebJo&atilde;o Ros&aacute;rio
Incident has been started
July 10 12:42 PM WESTwebJo&atilde;o Ros&aacute;rio
Teams has been added: ALM Consoles
July 10 12:43 PM WESTwebJo&atilde;o Ros&aacute;rioJo&atilde;o Ros&aacute;rio has been assigned as EngineerJuly 10 12:54 PM WESTwebRootlyZendesk Private Comment has been changed to: ----------------------------------------------**Update to R&amp;D**
- Hello TeamPlease don't close the cases without communicating to us what was done.One of the customer is specifically asking what occurred for the old versions to disappear. We can't close this problem just because the customer found a workaround.Additionally, since this is a visual bug, please create a fix and link it to this RDINC specifically so that we can track it.Regards,_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_July 10 12:54 PM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
- Hello TeamPlease don't close the cases without communicating to us what was done.One of the customer is specifically asking what occurred for the old versions to disappear. We can't close this problem just because the customer found a workaround.Additionally, since this is a visual bug, please create a fix and link it to this RDINC specifically so that we can track it.Regards,__
July 10 12:55 PM WESTwebRootlyZendesk Private Comment has been changed to: ------------------------------------------------ This notification was sent from Zendesk Support ticket #3034558 to all linked JIRA issues by Ricardo Moreira. --**Update to R&amp;D**- Hello TeamPlease don't close the cases without communicating to us what was done.One of the customer is specifically asking what occurred for the old versions to disappear. We can't close this problem just because the customer found a workaround.Additionally, since this is a visual bug, please create a fix and link it to this RDINC specifically so that we can track it.Regards,_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_July 10 12:55 PM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
------------------------------------------------ This notification was sent from Zendesk Support ticket #3034558 to all linked JIRA issues by Ricardo Moreira. --**Update to R&amp;D**- Hello TeamPlease don't close the cases without communicating to us what was done.One of the customer is specifically asking what occurred for the old versions to disappear. We can't close this problem just because the customer found a workaround.Additionally, since this is a visual bug, please create a fix and link it to this RDINC specifically so that we can track it.Regards,__
July 10  2:04 PM WESTwebJo&atilde;o Ros&aacute;rioTiago Cardoso has been assigned as EngineerJuly 10  2:06 PM WESTwebJo&atilde;o Ros&aacute;rio
Assigning to Maestro for them to understand why Asset Portfolio Service isn't providing the respective information for the ODC Portal.
July 10  2:28 PM WESTwebTiago CardosoSend ZenDesk private comment has been set: Hello team can you please check if this is still happening?July 10  2:28 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

Hello team can you please check if this is still happening?July 10  2:28 PM WESTwebRootlySend ZenDesk private comment has been unsetJuly 10  2:28 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

July 10  4:50 PM WESTwebJo&atilde;o Ros&aacute;rio
Teams has been removed: ALM Consoles
July 10  4:56 PM WESTwebTiago CardosoSend ZenDesk private comment has been set: Hello Team,
We figured what happened, APS is a new service and in order to bootstrap the deployment data we had a job that ran periodically. In EU CENTRAL 1 the job overwhelmed AVS resulting in an error state that deleted some records from APS. We already removed the job last week([Jira](https://outsystemsrd.atlassian.net/browse/RDMAST-1491)) but the damage was already done. So to workaround this the costumers need to do 1cp and deploy the affected apps to the next stages.
We are working on a fix so that the costumers don't need to rely on this workaround ([Jira](https://outsystemsrd.atlassian.net/browse/RDMAST-1524))July 10  4:56 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

Hello Team,
We figured what happened, APS is a new service and in order to bootstrap the deployment data we had a job that ran periodically. In EU CENTRAL 1 the job overwhelmed AVS resulting in an error state that deleted some records from APS. We already removed the job last week([Jira](https://outsystemsrd.atlassian.net/browse/RDMAST-1491)) but the damage was already done. So to workaround this the costumers need to do 1cp and deploy the affected apps to the next stages.
We are working on a fix so that the costumers don't need to rely on this workaround ([Jira](https://outsystemsrd.atlassian.net/browse/RDMAST-1524))July 10  4:56 PM WESTwebRootlySend ZenDesk private comment has been unsetJuly 10  4:56 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

July 10  5:02 PM WESTwebTiago CardosoSend ZenDesk private comment has been set: Hello Team,
We figured what happened, APS is a new service and in order to bootstrap the deployment data we had a job that ran periodically. In EU CENTRAL 1 the job overwhelmed AVS resulting in an error state that deleted some records from APS. We already removed the job last week([Jira](https://outsystemsrd.atlassian.net/browse/RDMAST-1491)) but the damage was already done. So to workaround this the costumers need to do 1cp and deploy the affected apps to the next stages.
We are working on a fix so that the costumers don't need to rely on this workaround ([Jira](https://outsystemsrd.atlassian.net/browse/RDMAST-1524))July 10  5:02 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

Hello Team,
We figured what happened, APS is a new service and in order to bootstrap the deployment data we had a job that ran periodically. In EU CENTRAL 1 the job overwhelmed AVS resulting in an error state that deleted some records from APS. We already removed the job last week([Jira](https://outsystemsrd.atlassian.net/browse/RDMAST-1491)) but the damage was already done. So to workaround this the costumers need to do 1cp and deploy the affected apps to the next stages.
We are working on a fix so that the costumers don't need to rely on this workaround ([Jira](https://outsystemsrd.atlassian.net/browse/RDMAST-1524))July 10  5:02 PM WESTwebRootlySend ZenDesk private comment has been unsetJuly 10  5:02 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

July 16 12:14 PM WESTwebRootlyZenDesk Event Type has been set: solvedJuly 16 12:14 PM WESTwebRootly
The Global Support team marked this incident as closed in ZenDesk.
August 20  1:37 PM WESTwebSara Gon&ccedil;alves
Incident has been resolved
August 20  1:37 PM WESTwebSara Gon&ccedil;alvesSystem-wide impact has been set: NoAugust 20  1:37 PM WESTwebSara Gon&ccedil;alvesImpact has been set: APS is a new service and in order to bootstrap the deployment data we had a job that ran periodically. In EU CENTRAL 1 the job overwhelmed AVS resulting in an error state that deleted some records from APS. August 20  1:37 PM WESTwebSara Gon&ccedil;alvesInvestigation and troubleshooting findings has been set: We already removed the job (https://outsystemsrd.atlassian.net/browse/RDMAST-1491) but the damage was already done. So to workaround this the customers need to do 1cp and deploy the affected apps to the next stages.August 20  1:37 PM WESTwebSara Gon&ccedil;alvesResolution has been set: The fix was done here: https://outsystemsrd.atlassian.net/browse/RDMAST-1524August 20  1:37 PM WESTwebSara Gon&ccedil;alvesRing has been set: gaAugust 20  1:37 PM WESTwebSara Gon&ccedil;alvesRing has been unset: -