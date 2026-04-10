---
title: Retrospective-SEV2-Sub-ticket of #3049034 (Request for Support leaders (from Product))
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4366073870/Retrospective-SEV2-Sub-ticket+of+3049034+Request+for+Support+leaders+from+Product
confluence_space: RKB
confluence_page_id: 4366073870
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV2-Sub-ticket of #3049034 (Request for Support leaders (from Product))

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV2

Teams:&nbsp;trueBlueRuntime Data Model&nbsp;trueBlueSre

Types:&nbsp;trueBlueCustomer Escalated
#### 🕐 Timestamps
Started At:&nbsp;trueBlueAugust 16  8:44 AM WEST

Mitigated At:&nbsp;trueYellowAugust 16  9:21 AM WEST

Resolved At:&nbsp;trueGreenAugust 16  9:21 AM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/894-sub-ticket-of-3049034-request-for-support-leaders-from-product)
[Pagerduty incident](https://outsystems.pagerduty.com/incidents/Q1X0XIP76OBPEN)

[Slack channel](https://slack.com/app_redirect?channel=C07HKHUPSUR&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3049103)

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

Joana Barradas
#### Summary
----------------------------------------------**CONSIDERATIONS BEFORE PERFORMING THE ESCALATION TO R&amp;D (MANDATORY)**None of the below points should be overlooked. Failure to do so may imply unnecessary effort.* * *
Ensure the ticket has been **categorized**, otherwise, the R&amp;D escalation will go unnoticed and not be worked on!**1.** For **Incidents**, the **IMAX** was consulted **beforehand** on which:- No incident models were found for the reported symptoms **OR**
- The incident model did not solve the issue **OR**
- The next step indicated in the Incident Model is an escalation to R&amp;D.
**2.** For **Questions**, the ChatODC on the **Slack channel** didn't return an acceptable answer.
**3.** Any other requests that explicitly indicate an R&amp;D escalation is needed.
**4**. **Incident impact assessment** was based on the **prioritization scoring matrix**.* * ***R&amp;D ESCALATION FORM**
Section comments can be removed for R&amp;D easier interpretation.**ISSUE DESCRIPTION AND HOW TO REPRODUCE**- As was discussed internally, we need to increase the ACU limit to 48 for our customer PT. Niaga Nusa Abadi (9YR.DOG.TCY.ZD7.SZR.TCX.RDN.QOU),- Currently, they are using 32 ACUs (instead of the standard 16 ACUs) so that they can accommodate new users in ODC.
- The ask now is to further increase those 32 ACUs to 48 as soon as possible; this scale-up is being done on a temporary basis.
- The reason for this is that, over the past few days, Professional Services have brought some gains in terms of performance but they are at 500 users and they need to add 1500 next week.
- Even with the optimizations, it will not be enough.- This scale-up has already been approved by Andy Pemberton:
- ![](https://supportoutsystems.zendesk.com/attachments/token/8sbaJuzdLBcOKK3juTmgab6Tt/?name=image.png)**IMPACT ON THE CUSTOMER**- This customer may continue facing other critical issues in production without this scale-up.**TROUBLESHOOTING STEPS &amp; WORKAROUND**- N/A**TECH DATA OR ANY OTHER RELEVANT INFO**- Ring: ga
- Tenant Id: d51a905c-4f3c-4e7b-83e3-1989c87cfeff
- Tenant Prefix: nna
- Region: ap-southeast-1_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 RetrospectiveinfoDetails
**Ring:** ga
**System-wide impact:**&nbsp; No
**Tenant ID:** N/A
**Tenant Prefix:** N/A
**Routing Error Code:** N/A
**Product Area:** Phoenix::Application Runtime::Database access
### Impact:
Application is slow due to low code logic.
### Investigation and troubleshooting findings:
N/A
### Resolution:
We've increased the max ACUs to 48.
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/894-sub-ticket-of-3049034-request-for-support-leaders-from-product)

**Date**

**Source**

**User**

**Event**
August 16  8:40 AM WESTwebRootly
created an alert via
August 16  8:40 AM WESTwebRootly
Rootly created this incident
August 16  8:40 AM WESTwebRootly
In triage date has been set to August 16  8:40 AM WEST
August 16  8:40 AM WESTwebRootly[Slack Channel](https://slack.com/app_redirect?channel=C07HKHUPSUR&amp;team=T041063TZ) has been createdAugust 16  8:40 AM WESTwebRootly[PagerDuty Incident](https://outsystems.pagerduty.com/incidents/Q1X0XIP76OBPEN) has been created.
📧 Notified Joana Barradas by email.&nbsp;&nbsp;📱 Notified Joana Barradas by SMS.&nbsp;&nbsp;📲 Notified Joana Barradas by push notification.  (via Android)August 16  8:40 AM WESTwebRootlyJoana Barradas has been assigned as EngineerAugust 16  8:40 AM WESTwebRootly
Ring: -
System-wide impact:  
Tenant ID: N/A
Tenant Prefix: N/A
Routing Error Code: N/A
Product Area: Phoenix::Application Runtime::Database access
August 16  8:42 AM WESTwebRootly
Joana Barradas acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q1X0XIP76OBPEN). (via Phone)
August 16  8:44 AM WESTwebJoana Barradas
Incident has been started
August 16  8:44 AM WESTwebRootly
Pagerduty Integrations acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q1X0XIP76OBPEN). (via Phone)
August 16  8:47 AM WESTwebJoana BarradasSwarm has been set: SREAugust 16  8:47 AM WESTwebRootly
Pagerduty Integrations added Dhruv Desai as responder in [PagerDuty](https://outsystems.pagerduty.com/incidents/Q1X0XIP76OBPEN)
August 16  8:47 AM WESTwebRootly
Dhruv Desai joined this [PagerDuty](https://outsystems.pagerduty.com/incidents/Q1X0XIP76OBPEN) incident.
August 16  8:49 AM WESTslackJoana Barradas
RFC to be executed: [https://outsystemsrd.atlassian.net/browse/RFC-1326](https://outsystemsrd.atlassian.net/browse/RFC-1326)
August 16  8:53 AM WESTslackDhruv Desai
Current Status
[image.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDMyNTYzLCJwdXIiOiJibG9iX2lkIn19--d5ba8ba0bce6a1476e4e3e53e4be0f7766a6fb50/image.png)August 16  8:58 AM WESTslackDhruv Desai
Executed the command```dhruv.desai@OS-FVFH30V9Q05P ~ % aws eks update-kubeconfig --region ap-southeast-1 --name runp-ga-ap-se-1-01
Updated context arn:aws:eks:ap-southeast-1:169351544280:cluster/runp-ga-ap-se-1-01 in /Users/dhruv.desai/.kube/config
dhruv.desai@OS-FVFH30V9Q05P ~ % 
dhruv.desai@OS-FVFH30V9Q05P ~ % kubectl annotate --overwrite Environment d0c3e7f9-5de9-4090-a422-2cdf0e1e84ec [runtimedb.outsystemscloud.com/max-acu='48.0](http://runtimedb.outsystemscloud.com/max-acu='48.0)'
[environment.runtime.outsystemscloud.com/d0c3e7f9-5de9-4090-a422-2cdf0e1e84ec](http://environment.runtime.outsystemscloud.com/d0c3e7f9-5de9-4090-a422-2cdf0e1e84ec) annotated
dhruv.desai@OS-FVFH30V9Q05P ~ % ```
August 16  9:09 AM WESTslackDhruv Desai
Re-run the command again removing Quotes```dhruv.desai@OS-FVFH30V9Q05P ~ % kubectl annotate --overwrite Environment d0c3e7f9-5de9-4090-a422-2cdf0e1e84ec [runtimedb.outsystemscloud.com/max-acu=48](http://runtimedb.outsystemscloud.com/max-acu=48)[environment.runtime.outsystemscloud.com/d0c3e7f9-5de9-4090-a422-2cdf0e1e84ec](http://environment.runtime.outsystemscloud.com/d0c3e7f9-5de9-4090-a422-2cdf0e1e84ec) annotated
dhruv.desai@OS-FVFH30V9Q05P ~ % 
dhruv.desai@OS-FVFH30V9Q05P ~ % kubectl annotate --list Environment d0c3e7f9-5de9-4090-a422-2cdf0e1e84ec                                              
[runtimedb.outsystemscloud.com/performance-insights-enabled=true](http://runtimedb.outsystemscloud.com/performance-insights-enabled=true)[tenant-provisioning.outsystemscloud.com/last-change-date=2024-03-05T18:22:13.398230](http://tenant-provisioning.outsystemscloud.com/last-change-date=2024-03-05T18:22:13.398230)[nats2crd.outsystemscloud.com/headers={&quot;environmentId&quot;:&quot;d0c3e7f9-5de9-4090-a422-2cdf0e1e84ec&quot;,&quot;operation_id&quot;:&quot;6305473f-a0c3-49b3-8580-48ab5af1a7ec&quot;,&quot;stamp&quot;:&quot;runp-ga-ap-se-1-01&quot;,&quot;traceparent&quot;:&quot;00-9a2da7b563fc87cd30c8346bf6a2155e-af543c6012ae6248-01&quot;,&quot;type&quot;:&quot;ResourceApply&quot;}](http://nats2crd.outsystemscloud.com/headers={%22environmentId%22:%22d0c3e7f9-5de9-4090-a422-2cdf0e1e84ec%22,%22operation_id%22:%226305473f-a0c3-49b3-8580-48ab5af1a7ec%22,%22stamp%22:%22runp-ga-ap-se-1-01%22,%22traceparent%22:%2200-9a2da7b563fc87cd30c8346bf6a2155e-af543c6012ae6248-01%22,%22type%22:%22ResourceApply%22})[nats2crd.outsystemscloud.com/last-send-status={&quot;conditions&quot;:[{&quot;lastTransitionTime&quot;:&quot;2024-08-16T08:07:13Z&quot;,&quot;message&quot;:&quot;observe](http://nats2crd.outsystemscloud.com/last-send-status={%22conditions%22:[{%22lastTransitionTime%22:%222024-08-16T08:07:13Z%22,%22message%22:%22observe) in progress. msg: terraform run in progress&quot;,&quot;observedGeneration&quot;:1,&quot;reason&quot;:&quot;Reconciling&quot;,&quot;status&quot;:&quot;Unknown&quot;,&quot;type&quot;:&quot;DatabaseReady&quot;},{&quot;lastTransitionTime&quot;:&quot;2024-08-08T09:56:08Z&quot;,&quot;message&quot;:&quot;resource is ready&quot;,&quot;observedGeneration&quot;:1,&quot;reason&quot;:&quot;Ready&quot;,&quot;status&quot;:&quot;True&quot;,&quot;type&quot;:&quot;ExternalLibraryReady&quot;},{&quot;lastTransitionTime&quot;:&quot;2024-08-12T09:39:06Z&quot;,&quot;message&quot;:&quot;resource is ready&quot;,&quot;observedGeneration&quot;:1,&quot;reason&quot;:&quot;Ready&quot;,&quot;status&quot;:&quot;True&quot;,&quot;type&quot;:&quot;NetworkReady&quot;},{&quot;lastTransitionTime&quot;:&quot;2024-08-13T00:26:50Z&quot;,&quot;message&quot;:&quot;Outputs written: v0.18.113@sha256:58e79a77d5d325580d98609c8f098d98284690916c46aa054be3681f6d8c0332&quot;,&quot;observedGeneration&quot;:1,&quot;reason&quot;:&quot;TerraformOutputsWritten&quot;,&quot;status&quot;:&quot;True&quot;,&quot;type&quot;:&quot;WorkspaceReady&quot;},{&quot;lastTransitionTime&quot;:&quot;2023-12-14T13:16:35Z&quot;,&quot;message&quot;:&quot;Basic environment infrastructure ready&quot;,&quot;observedGeneration&quot;:1,&quot;reason&quot;:&quot;InfrastructureCreatedSuccessfully&quot;,&quot;status&quot;:&quot;True&quot;,&quot;type&quot;:&quot;InfrastructureReady&quot;},{&quot;lastTransitionTime&quot;:&quot;2024-05-17T19:04:19Z&quot;,&quot;message&quot;:&quot;resource is ready&quot;,&quot;observedGeneration&quot;:1,&quot;reason&quot;:&quot;Ready&quot;,&quot;status&quot;:&quot;True&quot;,&quot;type&quot;:&quot;WorkflowReady&quot;}],&quot;state&quot;:&quot;Ready&quot;,&quot;workspace&quot;:{},&quot;workspaces&quot;:[{&quot;id&quot;:&quot;ws-6jAdDQV7eKbs1TAw&quot;,&quot;outputs&quot;:{&quot;aws_os_app_role_arn&quot;:&quot;arn:aws:iam::169351544280:role/env-d0c3e7f9-5de9-4090-a422-2cdf0e1e84ec-app&quot;,&quot;aws_os_db_access_role_arn&quot;:&quot;arn:aws:iam::169351544280:role/env-d0c3e7f9-5de9-4090-a422-2cdf0e1e84ec-db-access&quot;}}]}
[nats2crd.outsystemscloud.com/replyTo=provision.worker.environment.mgt-ea-us-east-1-01.runp.prd.update.d0c3e7f9-5de9-4090-a422-2cdf0e1e84ec](http://nats2crd.outsystemscloud.com/replyTo=provision.worker.environment.mgt-ea-us-east-1-01.runp.prd.update.d0c3e7f9-5de9-4090-a422-2cdf0e1e84ec)[runtimedb.outsystemscloud.com/enhanced-monitoring-enabled=true](http://runtimedb.outsystemscloud.com/enhanced-monitoring-enabled=true)[runtimedb.outsystemscloud.com/max-acu=48](http://runtimedb.outsystemscloud.com/max-acu=48)
dhruv.desai@OS-FVFH30V9Q05P ~ % ```Runtime DB team will update runbook
August 16  9:11 AM WESTslackDhruv Desai
Post Implementation
[image.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDMyNTY3LCJwdXIiOiJibG9iX2lkIn19--be59d31e066459ec4553344d7c28c8fa6bc3bb25/image.png)August 16  9:18 AM WESTwebJoana BarradasSend ZenDesk private comment has been set: Hello Support,  I would like to inform you that the max ACUs have already been changed to 48.&nbsp;  
This change will be rolled back on August 30th so that the max ACUs will return to 16.  Best regard,  
Joana BarradasAugust 16  9:18 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hello Support,  I would like to inform you that the max ACUs have already been changed to 48.&nbsp;  
This change will be rolled back on August 30th so that the max ACUs will return to 16.  Best regard,  
Joana Barradas
August 16  9:18 AM WESTwebRootlySend ZenDesk private comment has been unsetAugust 16  9:18 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

August 16  9:19 AM WESTwebRootly
Dhruv Desai marked the incident as resolved through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q1X0XIP76OBPEN). (via Website)
August 16  9:21 AM WESTwebJoana Barradas
Incident has been resolved
August 16  9:21 AM WESTwebJoana BarradasSystem-wide impact has been set: NoAugust 16  9:21 AM WESTwebJoana BarradasImpact has been set: Application is slow due to low code logic.August 16  9:21 AM WESTwebJoana BarradasInvestigation and troubleshooting findings has been set: N/AAugust 16  9:21 AM WESTwebJoana BarradasResolution has been set: We've increased the max ACUs to 48.August 16  9:21 AM WESTwebJoana BarradasRing has been set: gaAugust 16  9:21 AM WESTwebJoana BarradasRing has been unset: -