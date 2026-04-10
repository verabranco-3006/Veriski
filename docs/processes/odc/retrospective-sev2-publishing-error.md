---
title: Retrospective-SEV2-Publishing error
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4310302870/Retrospective-SEV2-Publishing+error
confluence_space: RKB
confluence_page_id: 4310302870
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV2-Publishing error

## 📘 Overview
Author:&nbsp;Rootlytrue

Severity:&nbsp;SEV2Redtrue

Teams:&nbsp;SreBluetrue&nbsp;Client RuntimeBluetrue
#### 🕐 Timestamps
Started At:&nbsp;July 23 10:21 AM WESTBluetrue

Mitigated At:&nbsp;July 25 10:33 AM WESTYellowtrue

Resolved At:&nbsp;July 25 10:33 AM WESTGreentrue
#### 🔗 Links
[Incident Page](https://rootly.com/account/incidents/744-publishing-error)

[Pagerduty incident](https://outsystems.pagerduty.com/incidents/Q0IGQK4NI1F6JR)

[Slack channel](https://slack.com/app_redirect?channel=C07DC80FMQE&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3039832)

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

Tiago M. Pereira
#### Summary

**CONSIDERATIONS BEFORE PERFORMING THE ESCALATION TO R&amp;D (MANDATORY)**
None of the below points should be overlooked. Failure to do so may imply unnecessary effort.
Ensure the ticket has been **categorized**, otherwise, the R&amp;D escalation will go unnoticed and not be worked on!
**1.** For **Incidents**, the **IMAX** was consulted **beforehand** on which:- No incident models were found for the reported symptoms **OR**
- The incident model did not solve the issue **OR**
- The next step indicated in the Incident Model is an escalation to R&amp;D.**2.** For **Questions**, the ChatODC on the **Slack channel** didn't return an acceptable answer.**3.** Any other requests that explicitly indicate an R&amp;D escalation is needed.**4**. **Incident impact assessment** was based on the **prioritization scoring matrix**.**R&amp;D ESCALATION FORM**
Section comments can be removed for R&amp;D easier interpretation.
**ISSUE DESCRIPTION AND HOW TO REPRODUCE**
- The customer is experiencing an issue where, upon attempting to publish their apps (Sandbox DEX and CronosUI Website), a generic error message appears, indicating a failure in the publishing process.
**IMPACT ON THE CUSTOMER**
Brief description of the impact on the customer/development team/other, including:
- Development
- Ongoing
- The customer is experiencing a blockage when trying to publish their apps that prevents them from making any changes to the application.
**TROUBLESHOOTING STEPS &amp; WORKAROUND**
- We were able to reproduce the error the customer stated.- 1CP Grafana Logs- https://outsystems.grafana.net/d/o2_h2-Bnz/publish-service-1cp-by-tenant?orgId=1&amp;var-ring=osall&amp;var-region=us-east-1&amp;var-stamp=plat-osall-us-east-1-01&amp;var-tenant=fae0814c-7560-49cc-886f-6b4eccb6709f&amp;var-exclude_tenant=All&amp;var-interval=%24__auto_interval_interval&amp;from=1721587890731&amp;to=1721674290731- Click the Publish button on **Sandbox DEV** application.![](https://supportoutsystems.zendesk.com/attachments/token/nL6k8aMvGw0XoRuQvYG3uIDoR/?name=image.png)![](https://supportoutsystems.zendesk.com/attachments/token/9NyLx6lXrzvbVKGQe0FuJ7EsK/?name=image.png)
![](https://supportoutsystems.zendesk.com/attachments/token/KeWBdPuatYh87ixtHdLuoUWtS/?name=image.png)
TraceId error logs:
https://outsystems.grafana.net/d/A1YJOsa7z/1cp-logs?orgId=1&amp;var-ring=osall&amp;var-level=Error&amp;var-level=Warning&amp;to=1721674994678&amp;var-service=All&amp;var-traceId=942833e710a3db55eedea1b976b5a2cb&amp;from=1721588012839
2024-07-22 18:22:53.350 Error Frontend.Build.Worker Unhandled exception in Worker
attributes_exception_stacktrace at System.Diagnostics.Process.WaitForExitAsync(CancellationToken cancellationToken)
at OutSystems.Frontend.PostProcessing.Tasks.ESBuildTask.InnerRun(IEnumerable`1 target) in /repo/src/Frontend/OutSystems.Frontend.PostProcessing/Tasks/ESBuildTask.cs:line 57 at OutSystems.Frontend.PostProcessing.Tasks.BaseBundleTask.Run(IEnumerable`1 target) in /repo/src/Frontend/OutSystems.Frontend.PostProcessing/Tasks/BaseBundleTask.cs:line 40
at OutSystems.Frontend.PostProcessing.FrontendPostProcess.Run(IEnumerable`1 files) in /repo/src/Frontend/OutSystems.Frontend.PostProcessing/FrontendPostProcess.cs:line 36 at OutSystems.Frontend.Worker.Application.Tasks.PostProcess.PostProcessTask.Run(Input input, IMessageBroker messageBroker, CancellationToken cancellationToken) in /repo/src/Frontend/OutSystems.Frontend.Worker.Application/Tasks/PostProcess/PostProcessTask.cs:line 82 at OutSystems.Build.Orchestration.Abstractions.AbstractBuildTask`2.Execute(TI input, IMessageBroker messageBroker, CancellationToken cancellationToken)
at OutSystems.Frontend.Worker.Application.Tasks.FrontendProcessGeneratedArtifactTask.InnerRun(Input input, IMessageBroker messageBroker, CancellationToken cancellationToken) in /repo/src/Frontend/OutSystems.Frontend.Worker.Application/Tasks/FrontendProcessGeneratedArtifactTask.cs:line 65
at OutSystems.Build.Orchestration.Abstractions.AbstractBuildTask`2.Execute(TI input, IMessageBroker messageBroker, CancellationToken cancellationToken) in /repo/src/BuildSDK/Orchestration/OutSystems.Build.Orchestration.Abstractions/AbstractBuildTask.cs:line 54
at OutSystems.Build.Orchestration.BaseOrchestrator.PostProcess(BuildRequestedEvent buildRequestedEvent, CompilationUnit compilationUnit, Output downloadProducersOutput, Output initializeWorkspaceOutput, Output pullProducersOutput, Output generateCodeOutput, CancellationToken cancellationToken) in /repo/src/BuildSDK/Orchestration/OutSystems.Build.Orchestration/BaseOrchestrator.cs:line 177
at OutSystems.Build.Orchestration.BaseOrchestrator.Run(BuildRequestedEvent buildRequestedEvent, CancellationToken cancellationToken) in /repo/src/BuildSDK/Orchestration/OutSystems.Build.Orchestration/BaseOrchestrator.cs:line 107
at OutSystems.Build.Worker.BuildTaskEventHandler.CallOrchestrator(BuildRequestedEvent request, IServiceScope scope, CancellationToken cancellationToken) in /repo/src/BuildSDK/BuildWorker/OutSystems.Build.Worker/BuildTaskEventHandler.cs:line 168
at OutSystems.Build.Worker.BuildTaskEventHandler.InnerHandle(BuildRequestedEvent request, CancellationToken token) in /repo/src/BuildSDK/BuildWorker/OutSystems.Build.Worker/BuildTaskEventHandler.cs:line 106
![](https://supportoutsystems.zendesk.com/attachments/token/UcTwGgG2QfoKiVkSw3It22OV1/?name=image.png)- Click the Publish button on **CronosUI Website** application.![](https://supportoutsystems.zendesk.com/attachments/token/LCxU3u92PsMriQbpA7AAVRIvt/?name=image.png)![](https://supportoutsystems.zendesk.com/attachments/token/ddtOwoKJnlRMgLzLGno8F9Mfk/?name=image.png)
![](https://supportoutsystems.zendesk.com/attachments/token/NQcDsNrqwvbfJdt6HRw4mtyk8/?name=image.png)
TraceId error logs:
https://outsystems.grafana.net/d/A1YJOsa7z/1cp-logs?orgId=1&amp;var-ring=osall&amp;var-level=Error&amp;var-level=Warning&amp;to=1721675027504&amp;var-service=All&amp;var-traceId=4a799d925a2f33338f5763005f14efb0&amp;from=1721588012839
2024-07-22 18:25:36.560 Error Frontend.Build.Worker Unhandled exception in Worker
attributes_exception_stacktrace at System.Diagnostics.Process.WaitForExitAsync(CancellationToken cancellationToken)
at OutSystems.Frontend.PostProcessing.Tasks.ESBuildTask.InnerRun(IEnumerable`1 target) in /repo/src/Frontend/OutSystems.Frontend.PostProcessing/Tasks/ESBuildTask.cs:line 57 at OutSystems.Frontend.PostProcessing.Tasks.BaseBundleTask.Run(IEnumerable`1 target) in /repo/src/Frontend/OutSystems.Frontend.PostProcessing/Tasks/BaseBundleTask.cs:line 40
at OutSystems.Frontend.PostProcessing.FrontendPostProcess.Run(IEnumerable`1 files) in /repo/src/Frontend/OutSystems.Frontend.PostProcessing/FrontendPostProcess.cs:line 36 at OutSystems.Frontend.Worker.Application.Tasks.PostProcess.PostProcessTask.Run(Input input, IMessageBroker messageBroker, CancellationToken cancellationToken) in /repo/src/Frontend/OutSystems.Frontend.Worker.Application/Tasks/PostProcess/PostProcessTask.cs:line 82 at OutSystems.Build.Orchestration.Abstractions.AbstractBuildTask`2.Execute(TI input, IMessageBroker messageBroker, CancellationToken cancellationToken)
at OutSystems.Frontend.Worker.Application.Tasks.FrontendProcessGeneratedArtifactTask.InnerRun(Input input, IMessageBroker messageBroker, CancellationToken cancellationToken) in /repo/src/Frontend/OutSystems.Frontend.Worker.Application/Tasks/FrontendProcessGeneratedArtifactTask.cs:line 65
at OutSystems.Build.Orchestration.Abstractions.AbstractBuildTask`2.Execute(TI input, IMessageBroker messageBroker, CancellationToken cancellationToken) in /repo/src/BuildSDK/Orchestration/OutSystems.Build.Orchestration.Abstractions/AbstractBuildTask.cs:line 54
at OutSystems.Build.Orchestration.BaseOrchestrator.PostProcess(BuildRequestedEvent buildRequestedEvent, CompilationUnit compilationUnit, Output downloadProducersOutput, Output initializeWorkspaceOutput, Output pullProducersOutput, Output generateCodeOutput, CancellationToken cancellationToken) in /repo/src/BuildSDK/Orchestration/OutSystems.Build.Orchestration/BaseOrchestrator.cs:line 177
at OutSystems.Build.Orchestration.BaseOrchestrator.Run(BuildRequestedEvent buildRequestedEvent, CancellationToken cancellationToken) in /repo/src/BuildSDK/Orchestration/OutSystems.Build.Orchestration/BaseOrchestrator.cs:line 107
at OutSystems.Build.Worker.BuildTaskEventHandler.CallOrchestrator(BuildRequestedEvent request, IServiceScope scope, CancellationToken cancellationToken) in /repo/src/BuildSDK/BuildWorker/OutSystems.Build.Worker/BuildTaskEventHandler.cs:line 168
at OutSystems.Build.Worker.BuildTaskEventHandler.InnerHandle(BuildRequestedEvent request, CancellationToken token) in /repo/src/BuildSDK/BuildWorker/OutSystems.Build.Worker/BuildTaskEventHandler.cs:line 106
![](https://supportoutsystems.zendesk.com/attachments/token/Jymud7sqSgTwv1tf32L0ncPEJ/?name=image.png)- Today 07/22/2024 there was another incident reported in the same tenant where a customer was experiencing publishing issues on different applications. #3039610
- However, the error code and messages were different.![](https://supportoutsystems.zendesk.com/attachments/token/I80WoxZgCTgdfnEw6Z3TqxWZZ/?name=image.png) ![](https://supportoutsystems.zendesk.com/attachments/token/Z6OvHUbtTExSxsDDSi9ack64b/?name=image.png)
- Also, the customer confirmed that they were are able to publish after some time.
- It was mentioned that there was a rollback of the outsystems-externallibrary-worker-service. RDINC-27493- https://outsystemsrd.atlassian.net/browse/RFC-1230- https://outsystems.slack.com/archives/C02FDRXNER0/p1721654857728809With this in mind, we would like to confirm if this new incident is also related to RDINC-27493 and possible mitigation steps for the customer to be able to publish again.
**TECH DATA OR ANY OTHER RELEVANT INFO**
- Ring: osall
- Tenant Id: fae0814c-7560-49cc-886f-6b4eccb6709f
- Tenant Prefix: extranet
- Region: us-east-1
- DMN.GTF.J1V.N02.OHY.ZDO.UBL.WTS
- CronosUI Website Revision 1153.oml
- Sandbox DEX Revision 3897.oml
_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 Retrospective### Details
**Ring:** osall
**System-wide impact:**&nbsp; No
**Tenant ID:** fae0814c-7560-49cc-886f-6b4eccb6709f
**Tenant Prefix:** extranet
**Routing Error Code:** OS-BLD-BLD
**Product Area:** -
### Impact:
It is being observed in just one tenant.
### Investigation and troubleshooting findings:
We are progressively rolling out the Removal RequireJS through the rings and on the last step, we enabled the feature flag on ring OSALL (+1), where the identified problems were found.

The investigation was quite self-explanatory since the generated code was affected by this rollout to ring OSALL.
### Resolution:
Because the ring OSALL was affected with the enablement of the Feature Toggle for the removal of RequireJS, the resolution started with the creation of an RFC [https://outsystemsrd.atlassian.net/browse/RFC-1236](https://outsystemsrd.atlassian.net/browse/RFC-1236)

Due to some problems in the SDLC team's pipelines, the rollback didn't occur and the version that disabled the feature flag on the affected ring reached ring OSALL and ended up fixing the issue.
## Tasks performed during incident resolution:
&nbsp;
## Executive Summary
[Guidelines](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4144496679/Incident+Retrospectives+-+Playbook#STEP-3---Write-the-Executive-Summary)

On July 22 9:34 PM WEST, Customer submitted a Support ticket RDINC-27503ef8955cb-cb21-32a7-b692-01ace42388d6System Jira reporting that they were unable to publish their application.

On July 23 12:42:29 PM WEST, the ticket got assigned to the Client Runtime team and we started analysing the issue.

The investigation concluded that the changes in the generated code from the RequireJS removal introduced a bug that would break the 1CP whenever the application generated a lot of warnings while being published.

This was related to a change that the Client Runtime did here ([https://github.com/OutSystems/OutSystems.Build.Job/pull/3855/files#diff-c89258e79cb6bb1fea01f1b1b579c1c62ae5bb3959c9db1a96b4b044b0059cf4R136](https://github.com/OutSystems/OutSystems.Build.Job/pull/3855/files#diff-c89258e79cb6bb1fea01f1b1b579c1c62ae5bb3959c9db1a96b4b044b0059cf4R136)) which removed any limit to show the logs from the ESbuild bundler execution.

As a consequence of the incident, we have determined that a rollback in ring +1 (OSALL) was required. We had a RFC [RFC-1236: Rollback outsystems-frontend-build-worker-service to v17.1488.0 in ring 1 (aka OSALL)APPROVED BY CAB](https://outsystemsrd.atlassian.net/browse/RFC-1236) which got approved and then we also asked for the SDLC to rollback the version of the service to the v17.1488.0 in that same ring - [https://outsystems.slack.com/archives/C02FDRXNER0/p1721740089502369](https://outsystems.slack.com/archives/C02FDRXNER0/p1721740089502369) **Connect your Slack account**. At the same time the team also reverted the changes in the Build.Job repository - [https://github.com/OutSystems/OutSystems.Build.Job/pull/3928](https://github.com/OutSystems/OutSystems.Build.Job/pull/3928) **Connect your Github account** and all the versions from v17.1491.0 to v17.1506.0 were banned with help from @alfred [https://outsystems.slack.com/archives/C0147J20TNY/p1721733178674539](https://outsystems.slack.com/archives/C0147J20TNY/p1721733178674539) **Connect your Slack account**.

Unfortunately (or fortunately), the fix reached the ring +1 before the rollback was made, solving the issue from the customer.

## Root Causes 
[Guidelines](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4144496679/Incident+Retrospectives+-+Playbook#STEP-1---Perform-the-Root-Cause-Analysis)

- 
Progressive rollout of the RequireJS removal reached ring +1 (OSALL).

- 
A bug in the ESBuild execution was making it impossible to publish the application

If the customer needs formal RCA, please fill out the following field with the document URL

[Please follow these instructions and place the RCA URL in the field below.](https://docs.google.com/document/d/13rXmBsOJh73nV2D6Z17SIBGBu2HOTWty5ddsvU000JM/edit#heading=h.bqxasxszr5q)

RCA URL

&lt;Place the URL of the customer RCA here if you have created one&gt;
## ⌛ Timeline
[View on Rootly](https://rootly.com/account/incidents/744-publishing-error)

**Date**

**Source**

**User**

**Event**

July 22  9:34 PM WEST

web

Rootly

created an alert via

July 22  9:34 PM WEST

web

Rootly

Rootly created this incident

July 22  9:34 PM WEST

web

Rootly

In triage date has been set to July 22  9:34 PM WEST

July 22  9:34 PM WEST

web

Rootly

[Slack Channel](https://slack.com/app_redirect?channel=C07DC80FMQE&amp;team=T041063TZ) has been created

July 22  9:34 PM WEST

web

Rootly

Ring: osall
System-wide impact:  
Tenant ID: fae0814c-7560-49cc-886f-6b4eccb6709f
Tenant Prefix: extranet
Routing Error Code: OS-BLD-BLD
Product Area: -

July 22  9:34 PM WEST

web

Rootly

[PagerDuty Incident](https://outsystems.pagerduty.com/incidents/Q0IGQK4NI1F6JR) has been created.

📲 Notified Jason Crews by push notification.  (via iPhone)

&nbsp;&nbsp;

📲 Notified Jason Crews by push notification.  (via iPhone)

July 22  9:34 PM WEST

web

Rootly

Jason Crews has been assigned as Engineer

July 22  9:34 PM WEST

web

Rootly

Jason Crews acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q0IGQK4NI1F6JR). (via Mobile)

July 23 10:18 AM WEST

web

Henrique Fonseca

Joel Filipe Carvalho has been assigned as Engineer

July 23 10:21 AM WEST

web

Joel Filipe Carvalho

Incident has been started

July 23 10:21 AM WEST

web

Rootly

Pagerduty Integrations acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q0IGQK4NI1F6JR). (via Mobile)

July 23 11:40 AM WEST

slack

Joel Carvalho

Looking at the 24h of the day where the tenant experienced the issue (2024-07-22 00:00:00 to 2024-07-23 00:00:00).
The issue is on OSALL ring. From the dashboard, we can see a total of 95 errors (78% of total 1CP) for this tenant. When we select all tenants for the same ring and region, we still have the same 95 error count (57% of total 1CP from all tenants).

[image.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDE1NzM4LCJwdXIiOiJibG9iX2lkIn19--1a9ef6cb78ec9d53a8eb1cd83ba3d93c27d43c97/image.png)

[image.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDE1NzM5LCJwdXIiOiJibG9iX2lkIn19--006058d5c2334c2bc1cf7e78228d8a2f9d33c836/image.png)

July 23 11:44 AM WEST

slack

Joel Carvalho

We did had some 1CP successful rate burn noted on the SLO for GA on this region, nearing the end of the day, and it does not seem to either correlate the time or impact as in OSALL.
The incident is tenant related and it did not correlate with any system-wide impacting issue.

July 23 12:24 PM WEST

web

Joel Filipe Carvalho

Summary has been changed to 

&nbsp;&nbsp;`&nbsp;&nbsp;`

`&nbsp;&nbsp;CONSIDERATIONS BEFORE PERFORMING THE ESCALATION TO R&amp;D (MANDATORY)`
`None of the below points should be overlooked. Failure to do so may imply unnecessary effort.`

`&nbsp;&nbsp;`

Ensure the ticket has been categorized, otherwise, the R&amp;D escalation will go unnoticed and not be worked on!

`&nbsp;&nbsp;1. For Incidents, the IMAX was consulted beforehand on which:`

- 
`No incident models were found for the reported symptoms OR&nbsp;&nbsp;`

- 
`The incident model did not solve the issue OR&nbsp;&nbsp;`

- 
`The next step indicated in the Incident Model is an escalation to R&amp;D.2. For Questions, the ChatODC on the Slack channel didn't return an acceptable answer.3. Any other requests that explicitly indicate an R&amp;D escalation is needed.4. Incident impact assessment was based on the prioritization scoring matrix.`

`&nbsp;&nbsp;R&amp;D ESCALATION FORM`
Section comments can be removed for R&amp;D easier interpretation.

`&nbsp;&nbsp;ISSUE DESCRIPTION AND HOW TO REPRODUCE`
- The customer is experiencing an issue where, upon attempting to publish their apps (Sandbox DEX and CronosUI Website), a generic error message appears, indicating a failure in the publishing process.

`&nbsp;&nbsp;IMPACT ON THE CUSTOMER`
Brief description of the impact on the customer/development team/other, including:

- Development

- Ongoing

- The customer is experiencing a blockage when trying to publish their apps that prevents them from making any changes to the application.

`&nbsp;&nbsp;TROUBLESHOOTING STEPS &amp; WORKAROUND`
`- We were able to reproduce the error the customer stated.`

- 
`&nbsp;&nbsp;`

`1CP Grafana Logs`

- 
`&nbsp;&nbsp;`[https://outsystems.grafana.net/d/o2_h2-Bnz/publish-service-1cp-by-tenant?orgId=1&amp;amp;var-ring=osall&amp;amp;var-region=us-east-1&amp;amp;var-stamp=plat-osall-us-east-1-01&amp;amp;var-tenant=fae0814c-7560-49cc-886f-6b4eccb6709f&amp;amp;var-exclude_tenant=All&amp;amp;var-interval=%24__auto_interval_interval&amp;amp;from=1721587890731&amp;amp;to=1721674290731](https://outsystems.grafana.net/d/o2_h2-Bnz/publish-service-1cp-by-tenant?orgId=1&amp;amp;var-ring=osall&amp;amp;var-region=us-east-1&amp;amp;var-stamp=plat-osall-us-east-1-01&amp;amp;var-tenant=fae0814c-7560-49cc-886f-6b4eccb6709f&amp;amp;var-exclude_tenant=All&amp;amp;var-interval=%24__auto_interval_interval&amp;amp;from=1721587890731&amp;amp;to=1721674290731)`&nbsp;&nbsp;`

`&nbsp;&nbsp;`

- 
`&nbsp;&nbsp;`

`Click the Publish button on Sandbox DEV application.`

`&nbsp;&nbsp;`

`&nbsp;&nbsp;`

`&nbsp;&nbsp;`
TraceId error logs:

`&nbsp;&nbsp;`[https://outsystems.grafana.net/d/A1YJOsa7z/1cp-logs?orgId=1&amp;amp;var-ring=osall&amp;amp;var-level=Error&amp;amp;var-level=Warning&amp;amp;to=1721674994678&amp;amp;var-service=All&amp;amp;var-traceId=942833e710a3db55eedea1b976b5a2cb&amp;amp;from=1721588012839](https://outsystems.grafana.net/d/A1YJOsa7z/1cp-logs?orgId=1&amp;amp;var-ring=osall&amp;amp;var-level=Error&amp;amp;var-level=Warning&amp;amp;to=1721674994678&amp;amp;var-service=All&amp;amp;var-traceId=942833e710a3db55eedea1b976b5a2cb&amp;amp;from=1721588012839)
2024-07-22 18:22:53.350 Error Frontend.Build.Worker Unhandled exception in Worker

attributes_exception_stacktrace at System.Diagnostics.Process.WaitForExitAsync(CancellationToken cancellationToken)

at OutSystems.Frontend.PostProcessing.Tasks.ESBuildTask.InnerRun(IEnumerable1 target) in /repo/src/Frontend/OutSystems.Frontend.PostProcessing/Tasks/ESBuildTask.cs:line 57 at OutSystems.Frontend.PostProcessing.Tasks.BaseBundleTask.Run(IEnumerable1 target) in /repo/src/Frontend/OutSystems.Frontend.PostProcessing/Tasks/BaseBundleTask.cs:line 40

at OutSystems.Frontend.PostProcessing.FrontendPostProcess.Run(IEnumerable1 files) in /repo/src/Frontend/OutSystems.Frontend.PostProcessing/FrontendPostProcess.cs:line 36 at OutSystems.Frontend.Worker.Application.Tasks.PostProcess.PostProcessTask.Run(Input input, IMessageBroker messageBroker, CancellationToken cancellationToken) in /repo/src/Frontend/OutSystems.Frontend.Worker.Application/Tasks/PostProcess/PostProcessTask.cs:line 82 at OutSystems.Build.Orchestration.Abstractions.AbstractBuildTask2.Execute(TI input, IMessageBroker messageBroker, CancellationToken cancellationToken)

at OutSystems.Frontend.Worker.Application.Tasks.FrontendProcessGeneratedArtifactTask.InnerRun(Input input, IMessageBroker messageBroker, CancellationToken cancellationToken) in /repo/src/Frontend/OutSystems.Frontend.Worker.Application/Tasks/FrontendProcessGeneratedArtifactTask.cs:line 65

at OutSystems.Build.Orchestration.Abstractions.AbstractBuildTask`2.Execute(TI input, IMessageBroker messageBroker, CancellationToken cancellationToken) in /repo/src/BuildSDK/Orchestration/OutSystems.Build.Orchestration.Abstractions/AbstractBuildTask.cs:line 54

at OutSystems.Build.Orchestration.BaseOrchestrator.PostProcess(BuildRequestedEvent buildRequestedEvent, CompilationUnit compilationUnit, Output downloadProducersOutput, Output initializeWorkspaceOutput, Output pullProducersOutput, Output generateCodeOutput, CancellationToken cancellationToken) in /repo/src/BuildSDK/Orchestration/OutSystems.Build.Orchestration/BaseOrchestrator.cs:line 177

at OutSystems.Build.Orchestration.BaseOrchestrator.Run(BuildRequestedEvent buildRequestedEvent, CancellationToken cancellationToken) in /repo/src/BuildSDK/Orchestration/OutSystems.Build.Orchestration/BaseOrchestrator.cs:line 107

at OutSystems.Build.Worker.BuildTaskEventHandler.CallOrchestrator(BuildRequestedEvent request, IServiceScope scope, CancellationToken cancellationToken) in /repo/src/BuildSDK/BuildWorker/OutSystems.Build.Worker/BuildTaskEventHandler.cs:line 168

at OutSystems.Build.Worker.BuildTaskEventHandler.InnerHandle(BuildRequestedEvent request, CancellationToken token) in /repo/src/BuildSDK/BuildWorker/OutSystems.Build.Worker/BuildTaskEventHandler.cs:line 106

`&nbsp;&nbsp;``&nbsp;&nbsp;`

- 
`Click the Publish button on CronosUI Website application.`

`&nbsp;&nbsp;`

`&nbsp;&nbsp;`
TraceId error logs:

`&nbsp;&nbsp;`[https://outsystems.grafana.net/d/A1YJOsa7z/1cp-logs?orgId=1&amp;amp;var-ring=osall&amp;amp;var-level=Error&amp;amp;var-level=Warning&amp;amp;to=1721675027504&amp;amp;var-service=All&amp;amp;var-traceId=4a799d925a2f33338f5763005f14efb0&amp;amp;from=1721588012839](https://outsystems.grafana.net/d/A1YJOsa7z/1cp-logs?orgId=1&amp;amp;var-ring=osall&amp;amp;var-level=Error&amp;amp;var-level=Warning&amp;amp;to=1721675027504&amp;amp;var-service=All&amp;amp;var-traceId=4a799d925a2f33338f5763005f14efb0&amp;amp;from=1721588012839)
2024-07-22 18:25:36.560 Error Frontend.Build.Worker Unhandled exception in Worker

attributes_exception_stacktrace at System.Diagnostics.Process.WaitForExitAsync(CancellationToken cancellationToken)

at OutSystems.Frontend.PostProcessing.Tasks.ESBuildTask.InnerRun(IEnumerable1 target) in /repo/src/Frontend/OutSystems.Frontend.PostProcessing/Tasks/ESBuildTask.cs:line 57 at OutSystems.Frontend.PostProcessing.Tasks.BaseBundleTask.Run(IEnumerable1 target) in /repo/src/Frontend/OutSystems.Frontend.PostProcessing/Tasks/BaseBundleTask.cs:line 40

at OutSystems.Frontend.PostProcessing.FrontendPostProcess.Run(IEnumerable1 files) in /repo/src/Frontend/OutSystems.Frontend.PostProcessing/FrontendPostProcess.cs:line 36 at OutSystems.Frontend.Worker.Application.Tasks.PostProcess.PostProcessTask.Run(Input input, IMessageBroker messageBroker, CancellationToken cancellationToken) in /repo/src/Frontend/OutSystems.Frontend.Worker.Application/Tasks/PostProcess/PostProcessTask.cs:line 82 at OutSystems.Build.Orchestration.Abstractions.AbstractBuildTask2.Execute(TI input, IMessageBroker messageBroker, CancellationToken cancellationToken)

at OutSystems.Frontend.Worker.Application.Tasks.FrontendProcessGeneratedArtifactTask.InnerRun(Input input, IMessageBroker messageBroker, CancellationToken cancellationToken) in /repo/src/Frontend/OutSystems.Frontend.Worker.Application/Tasks/FrontendProcessGeneratedArtifactTask.cs:line 65

at OutSystems.Build.Orchestration.Abstractions.AbstractBuildTask`2.Execute(TI input, IMessageBroker messageBroker, CancellationToken cancellationToken) in /repo/src/BuildSDK/Orchestration/OutSystems.Build.Orchestration.Abstractions/AbstractBuildTask.cs:line 54

at OutSystems.Build.Orchestration.BaseOrchestrator.PostProcess(BuildRequestedEvent buildRequestedEvent, CompilationUnit compilationUnit, Output downloadProducersOutput, Output initializeWorkspaceOutput, Output pullProducersOutput, Output generateCodeOutput, CancellationToken cancellationToken) in /repo/src/BuildSDK/Orchestration/OutSystems.Build.Orchestration/BaseOrchestrator.cs:line 177

at OutSystems.Build.Orchestration.BaseOrchestrator.Run(BuildRequestedEvent buildRequestedEvent, CancellationToken cancellationToken) in /repo/src/BuildSDK/Orchestration/OutSystems.Build.Orchestration/BaseOrchestrator.cs:line 107

at OutSystems.Build.Worker.BuildTaskEventHandler.CallOrchestrator(BuildRequestedEvent request, IServiceScope scope, CancellationToken cancellationToken) in /repo/src/BuildSDK/BuildWorker/OutSystems.Build.Worker/BuildTaskEventHandler.cs:line 168

at OutSystems.Build.Worker.BuildTaskEventHandler.InnerHandle(BuildRequestedEvent request, CancellationToken token) in /repo/src/BuildSDK/BuildWorker/OutSystems.Build.Worker/BuildTaskEventHandler.cs:line 106

`&nbsp;&nbsp;``&nbsp;&nbsp;`

- 
`Today 07/22/2024 there was another incident reported in the same tenant where a customer was experiencing publishing issues on different applications. #3039610`

- 
However, the error code and messages were different.

`&nbsp;&nbsp;`

- 
`Also, the customer confirmed that they were are able to publish after some time.`

- 
`&nbsp;&nbsp;`

`It was mentioned that there was a rollback of the outsystems-externallibrary-worker-service. RDINC-27493`

- 
`&nbsp;&nbsp;`[https://outsystemsrd.atlassian.net/browse/RFC-1230](https://outsystemsrd.atlassian.net/browse/RFC-1230)`&nbsp;&nbsp;`

`&nbsp;&nbsp;`

- 
`&nbsp;&nbsp;`

`&nbsp;&nbsp;`[https://outsystems.slack.com/archives/C02FDRXNER0/p1721654857728809](https://outsystems.slack.com/archives/C02FDRXNER0/p1721654857728809)`&nbsp;&nbsp;`

`&nbsp;&nbsp;`

With this in mind, we would like to confirm if this new incident is also related to RDINC-27493 and possible mitigation steps for the customer to be able to publish again.

`&nbsp;&nbsp;TECH DATA OR ANY OTHER RELEVANT INFO`
- Ring: osall

- Tenant Id: fae0814c-7560-49cc-886f-6b4eccb6709f

- Tenant Prefix: extranet

- Region: us-east-1

- DMN.GTF.J1V.N02.OHY.ZDO.UBL.WTS

- CronosUI Website Revision 1153.oml

- Sandbox DEX Revision 3897.oml

`&nbsp;&nbsp;&lt;! do not remove this line, this will be used to the trigger Technical Support::Send to R&amp;D - ODC #trigger_send_to_r&amp;d_odc !&gt;&nbsp;&nbsp;`

`&nbsp;&nbsp;`&nbsp;&nbsp;

July 23 12:24 PM WEST

web

Joel Filipe Carvalho

Teams has been added: [Maestro](/account/teams/maestro/status)

July 23 12:24 PM WEST

web

Joel Filipe Carvalho

System-wide impact has been set: No

July 23 12:24 PM WEST

web

Joel Filipe Carvalho

Impact has been set: It is being observed in just one tenant.

July 23 12:24 PM WEST

web

Joel Filipe Carvalho

Investigation and troubleshooting findings has been set: (check timeline)

July 23 12:27 PM WEST

web

Joel Filipe Carvalho

Diogo Rolo has been assigned as Engineer

July 23 12:42 PM WEST

web

Joel Filipe Carvalho

Summary has been changed to 

&nbsp;&nbsp;`&nbsp;&nbsp;`

`&nbsp;&nbsp;CONSIDERATIONS BEFORE PERFORMING THE ESCALATION TO R&amp;D (MANDATORY)`
None of the below points should be overlooked. Failure to do so may imply unnecessary effort.

Ensure the ticket has been categorized, otherwise, the R&amp;D escalation will go unnoticed and not be worked on!

`&nbsp;&nbsp;1. For Incidents, the IMAX was consulted beforehand on which:`

- 
`No incident models were found for the reported symptoms OR&nbsp;&nbsp;`

- 
`The incident model did not solve the issue OR&nbsp;&nbsp;`

- 
`The next step indicated in the Incident Model is an escalation to R&amp;D.2. For Questions, the ChatODC on the Slack channel didn't return an acceptable answer.3. Any other requests that explicitly indicate an R&amp;D escalation is needed.4. Incident impact assessment was based on the prioritization scoring matrix.`

`&nbsp;&nbsp;R&amp;D ESCALATION FORM`
Section comments can be removed for R&amp;D easier interpretation.

`&nbsp;&nbsp;ISSUE DESCRIPTION AND HOW TO REPRODUCE`
- The customer is experiencing an issue where, upon attempting to publish their apps (Sandbox DEX and CronosUI Website), a generic error message appears, indicating a failure in the publishing process.

`&nbsp;&nbsp;IMPACT ON THE CUSTOMER`
Brief description of the impact on the customer/development team/other, including:

- Development

- Ongoing

- The customer is experiencing a blockage when trying to publish their apps that prevents them from making any changes to the application.

`&nbsp;&nbsp;TROUBLESHOOTING STEPS &amp; WORKAROUND`
`- We were able to reproduce the error the customer stated.`

- 
`&nbsp;&nbsp;`

`1CP Grafana Logs`

- 
`&nbsp;&nbsp;`[https://outsystems.grafana.net/d/o2_h2-Bnz/publish-service-1cp-by-tenant?orgId=1&amp;amp;var-ring=osall&amp;amp;var-region=us-east-1&amp;amp;var-stamp=plat-osall-us-east-1-01&amp;amp;var-tenant=fae0814c-7560-49cc-886f-6b4eccb6709f&amp;amp;var-exclude_tenant=All&amp;amp;var-interval=%24__auto_interval_interval&amp;amp;from=1721587890731&amp;amp;to=1721674290731](https://outsystems.grafana.net/d/o2_h2-Bnz/publish-service-1cp-by-tenant?orgId=1&amp;amp;var-ring=osall&amp;amp;var-region=us-east-1&amp;amp;var-stamp=plat-osall-us-east-1-01&amp;amp;var-tenant=fae0814c-7560-49cc-886f-6b4eccb6709f&amp;amp;var-exclude_tenant=All&amp;amp;var-interval=%24__auto_interval_interval&amp;amp;from=1721587890731&amp;amp;to=1721674290731)`&nbsp;&nbsp;`

`&nbsp;&nbsp;`

- 
`&nbsp;&nbsp;`

`Click the Publish button on Sandbox DEV application.`

`&nbsp;&nbsp;`

`&nbsp;&nbsp;`

`&nbsp;&nbsp;`
TraceId error logs:

`&nbsp;&nbsp;`[https://outsystems.grafana.net/d/A1YJOsa7z/1cp-logs?orgId=1&amp;amp;var-ring=osall&amp;amp;var-level=Error&amp;amp;var-level=Warning&amp;amp;to=1721674994678&amp;amp;var-service=All&amp;amp;var-traceId=942833e710a3db55eedea1b976b5a2cb&amp;amp;from=1721588012839](https://outsystems.grafana.net/d/A1YJOsa7z/1cp-logs?orgId=1&amp;amp;var-ring=osall&amp;amp;var-level=Error&amp;amp;var-level=Warning&amp;amp;to=1721674994678&amp;amp;var-service=All&amp;amp;var-traceId=942833e710a3db55eedea1b976b5a2cb&amp;amp;from=1721588012839)
2024-07-22 18:22:53.350 Error Frontend.Build.Worker Unhandled exception in Worker

attributes_exception_stacktrace at System.Diagnostics.Process.WaitForExitAsync(CancellationToken cancellationToken)

at OutSystems.Frontend.PostProcessing.Tasks.ESBuildTask.InnerRun(IEnumerable1 target) in /repo/src/Frontend/OutSystems.Frontend.PostProcessing/Tasks/ESBuildTask.cs:line 57 at OutSystems.Frontend.PostProcessing.Tasks.BaseBundleTask.Run(IEnumerable1 target) in /repo/src/Frontend/OutSystems.Frontend.PostProcessing/Tasks/BaseBundleTask.cs:line 40

at OutSystems.Frontend.PostProcessing.FrontendPostProcess.Run(IEnumerable1 files) in /repo/src/Frontend/OutSystems.Frontend.PostProcessing/FrontendPostProcess.cs:line 36 at OutSystems.Frontend.Worker.Application.Tasks.PostProcess.PostProcessTask.Run(Input input, IMessageBroker messageBroker, CancellationToken cancellationToken) in /repo/src/Frontend/OutSystems.Frontend.Worker.Application/Tasks/PostProcess/PostProcessTask.cs:line 82 at OutSystems.Build.Orchestration.Abstractions.AbstractBuildTask2.Execute(TI input, IMessageBroker messageBroker, CancellationToken cancellationToken)

at OutSystems.Frontend.Worker.Application.Tasks.FrontendProcessGeneratedArtifactTask.InnerRun(Input input, IMessageBroker messageBroker, CancellationToken cancellationToken) in /repo/src/Frontend/OutSystems.Frontend.Worker.Application/Tasks/FrontendProcessGeneratedArtifactTask.cs:line 65

at OutSystems.Build.Orchestration.Abstractions.AbstractBuildTask`2.Execute(TI input, IMessageBroker messageBroker, CancellationToken cancellationToken) in /repo/src/BuildSDK/Orchestration/OutSystems.Build.Orchestration.Abstractions/AbstractBuildTask.cs:line 54

at OutSystems.Build.Orchestration.BaseOrchestrator.PostProcess(BuildRequestedEvent buildRequestedEvent, CompilationUnit compilationUnit, Output downloadProducersOutput, Output initializeWorkspaceOutput, Output pullProducersOutput, Output generateCodeOutput, CancellationToken cancellationToken) in /repo/src/BuildSDK/Orchestration/OutSystems.Build.Orchestration/BaseOrchestrator.cs:line 177

at OutSystems.Build.Orchestration.BaseOrchestrator.Run(BuildRequestedEvent buildRequestedEvent, CancellationToken cancellationToken) in /repo/src/BuildSDK/Orchestration/OutSystems.Build.Orchestration/BaseOrchestrator.cs:line 107

at OutSystems.Build.Worker.BuildTaskEventHandler.CallOrchestrator(BuildRequestedEvent request, IServiceScope scope, CancellationToken cancellationToken) in /repo/src/BuildSDK/BuildWorker/OutSystems.Build.Worker/BuildTaskEventHandler.cs:line 168

at OutSystems.Build.Worker.BuildTaskEventHandler.InnerHandle(BuildRequestedEvent request, CancellationToken token) in /repo/src/BuildSDK/BuildWorker/OutSystems.Build.Worker/BuildTaskEventHandler.cs:line 106

`&nbsp;&nbsp;``&nbsp;&nbsp;`

- 
`Click the Publish button on CronosUI Website application.`

`&nbsp;&nbsp;`

`&nbsp;&nbsp;`
TraceId error logs:

`&nbsp;&nbsp;`[https://outsystems.grafana.net/d/A1YJOsa7z/1cp-logs?orgId=1&amp;amp;var-ring=osall&amp;amp;var-level=Error&amp;amp;var-level=Warning&amp;amp;to=1721675027504&amp;amp;var-service=All&amp;amp;var-traceId=4a799d925a2f33338f5763005f14efb0&amp;amp;from=1721588012839](https://outsystems.grafana.net/d/A1YJOsa7z/1cp-logs?orgId=1&amp;amp;var-ring=osall&amp;amp;var-level=Error&amp;amp;var-level=Warning&amp;amp;to=1721675027504&amp;amp;var-service=All&amp;amp;var-traceId=4a799d925a2f33338f5763005f14efb0&amp;amp;from=1721588012839)
2024-07-22 18:25:36.560 Error Frontend.Build.Worker Unhandled exception in Worker

attributes_exception_stacktrace at System.Diagnostics.Process.WaitForExitAsync(CancellationToken cancellationToken)

at OutSystems.Frontend.PostProcessing.Tasks.ESBuildTask.InnerRun(IEnumerable1 target) in /repo/src/Frontend/OutSystems.Frontend.PostProcessing/Tasks/ESBuildTask.cs:line 57 at OutSystems.Frontend.PostProcessing.Tasks.BaseBundleTask.Run(IEnumerable1 target) in /repo/src/Frontend/OutSystems.Frontend.PostProcessing/Tasks/BaseBundleTask.cs:line 40

at OutSystems.Frontend.PostProcessing.FrontendPostProcess.Run(IEnumerable1 files) in /repo/src/Frontend/OutSystems.Frontend.PostProcessing/FrontendPostProcess.cs:line 36 at OutSystems.Frontend.Worker.Application.Tasks.PostProcess.PostProcessTask.Run(Input input, IMessageBroker messageBroker, CancellationToken cancellationToken) in /repo/src/Frontend/OutSystems.Frontend.Worker.Application/Tasks/PostProcess/PostProcessTask.cs:line 82 at OutSystems.Build.Orchestration.Abstractions.AbstractBuildTask2.Execute(TI input, IMessageBroker messageBroker, CancellationToken cancellationToken)

at OutSystems.Frontend.Worker.Application.Tasks.FrontendProcessGeneratedArtifactTask.InnerRun(Input input, IMessageBroker messageBroker, CancellationToken cancellationToken) in /repo/src/Frontend/OutSystems.Frontend.Worker.Application/Tasks/FrontendProcessGeneratedArtifactTask.cs:line 65

at OutSystems.Build.Orchestration.Abstractions.AbstractBuildTask`2.Execute(TI input, IMessageBroker messageBroker, CancellationToken cancellationToken) in /repo/src/BuildSDK/Orchestration/OutSystems.Build.Orchestration.Abstractions/AbstractBuildTask.cs:line 54

at OutSystems.Build.Orchestration.BaseOrchestrator.PostProcess(BuildRequestedEvent buildRequestedEvent, CompilationUnit compilationUnit, Output downloadProducersOutput, Output initializeWorkspaceOutput, Output pullProducersOutput, Output generateCodeOutput, CancellationToken cancellationToken) in /repo/src/BuildSDK/Orchestration/OutSystems.Build.Orchestration/BaseOrchestrator.cs:line 177

at OutSystems.Build.Orchestration.BaseOrchestrator.Run(BuildRequestedEvent buildRequestedEvent, CancellationToken cancellationToken) in /repo/src/BuildSDK/Orchestration/OutSystems.Build.Orchestration/BaseOrchestrator.cs:line 107

at OutSystems.Build.Worker.BuildTaskEventHandler.CallOrchestrator(BuildRequestedEvent request, IServiceScope scope, CancellationToken cancellationToken) in /repo/src/BuildSDK/BuildWorker/OutSystems.Build.Worker/BuildTaskEventHandler.cs:line 168

at OutSystems.Build.Worker.BuildTaskEventHandler.InnerHandle(BuildRequestedEvent request, CancellationToken token) in /repo/src/BuildSDK/BuildWorker/OutSystems.Build.Worker/BuildTaskEventHandler.cs:line 106

`&nbsp;&nbsp;``&nbsp;&nbsp;`

- 
`Today 07/22/2024 there was another incident reported in the same tenant where a customer was experiencing publishing issues on different applications. #3039610`

- 
However, the error code and messages were different.

`&nbsp;&nbsp;`

- 
`Also, the customer confirmed that they were are able to publish after some time.`

- 
`&nbsp;&nbsp;`

`It was mentioned that there was a rollback of the outsystems-externallibrary-worker-service. RDINC-27493`

- 
`&nbsp;&nbsp;`[https://outsystemsrd.atlassian.net/browse/RFC-1230](https://outsystemsrd.atlassian.net/browse/RFC-1230)`&nbsp;&nbsp;`

`&nbsp;&nbsp;`

- 
`&nbsp;&nbsp;`

`&nbsp;&nbsp;`[https://outsystems.slack.com/archives/C02FDRXNER0/p1721654857728809](https://outsystems.slack.com/archives/C02FDRXNER0/p1721654857728809)`&nbsp;&nbsp;`

`&nbsp;&nbsp;`

With this in mind, we would like to confirm if this new incident is also related to RDINC-27493 and possible mitigation steps for the customer to be able to publish again.

`&nbsp;&nbsp;TECH DATA OR ANY OTHER RELEVANT INFO`
- Ring: osall

- Tenant Id: fae0814c-7560-49cc-886f-6b4eccb6709f

- Tenant Prefix: extranet

- Region: us-east-1

- DMN.GTF.J1V.N02.OHY.ZDO.UBL.WTS

- CronosUI Website Revision 1153.oml

- Sandbox DEX Revision 3897.oml

`&nbsp;&nbsp;&lt;! do not remove this line, this will be used to the trigger Technical Support::Send to R&amp;D - ODC #trigger_send_to_r&amp;d_odc !&gt;&nbsp;&nbsp;`

`&nbsp;&nbsp;`&nbsp;&nbsp;

July 23 12:42 PM WEST

web

Joel Filipe Carvalho

Teams has been added: [Client Runtime](/account/teams/client-runtime/status)

July 23 12:42 PM WEST

web

Joel Filipe Carvalho

Teams has been removed: [Maestro](/account/teams/maestro/status)

July 23 12:42 PM WEST

web

Joel Filipe Carvalho

Tiago Pereira has been assigned as Engineer

July 23 12:44 PM WEST

web

Joel Filipe Carvalho

Tiago M. Pereira has been assigned as Engineer

July 23 12:47 PM WEST

web

Tiago M. Pereira

Send ZenDesk private comment has been set: Hello team,  The Client Runtime team analyzed the issues you mentioned and here is what we got from our analysis:We are progressively rolling out the Removal RequireJS through the rings and on the last step, we enabled the feature flag on ring OSALL (+1), where the identified problems were found. As the next step, we will rollback to solve and unblock the customer.&nbsp;  Here is the RFC [https://outsystemsrd.atlassian.net/browse/RFC-1236](https://outsystemsrd.atlassian.net/browse/RFC-1236)  Let us know if you have any additional questions,  Best regards,Tiago Pereira

July 23 12:47 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:
Hello team,  The Client Runtime team analyzed the issues you mentioned and here is what we got from our analysis:We are progressively rolling out the Removal RequireJS through the rings and on the last step, we enabled the feature flag on ring OSALL (+1), where the identified problems were found. As the next step, we will rollback to solve and unblock the customer.&nbsp;  Here is the RFC [https://outsystemsrd.atlassian.net/browse/RFC-1236](https://outsystemsrd.atlassian.net/browse/RFC-1236)  Let us know if you have any additional questions,  Best regards,Tiago Pereira

July 23 12:47 PM WEST

web

Rootly

Send ZenDesk private comment has been unset

July 23 12:47 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:

July 23 12:50 PM WEST

slack

Joel Carvalho

Just for the record on Rootly timeline, the related RDINC for this case is [https://outsystemsrd.atlassian.net/browse/RDINC-27503](https://outsystemsrd.atlassian.net/browse/RDINC-27503)
Related RFC: [https://outsystemsrd.atlassian.net/browse/RFC-1236](https://outsystemsrd.atlassian.net/browse/RFC-1236)

July 23  1:40 PM WEST

web

Rootly

Zendesk Private Comment has been set: ----------------------------------------------**Update to R&amp;D**
- Thank you team.Let us know when the rollback is done to share with Juliana.Kind regards__

July 23  1:40 PM WEST

web

Rootly

NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
- Thank you team.Let us know when the rollback is done to share with Juliana.Kind regards__

July 24 11:32 AM WEST

web

Tiago M. Pereira

Send ZenDesk private comment has been set: Hello team,  
I just wanted to let you know that the fix is now in ring OSALL and a republish of the application is required to solve the issue.  Best regards,  
Tiago Pereira

July 24 11:32 AM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:
Hello team,  
I just wanted to let you know that the fix is now in ring OSALL and a republish of the application is required to solve the issue.  Best regards,  
Tiago Pereira

July 24 11:32 AM WEST

web

Rootly

Send ZenDesk private comment has been unset

July 24 11:32 AM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:

July 24  3:36 PM WEST

web

Tiago M. Pereira

Investigation and troubleshooting findings has been changed to: We are progressively rolling out the Removal RequireJS through the rings and on the last step, we enabled the feature flag on ring OSALL (+1), where the identified problems were found.
The investigation was quite self-explanatory since the generated code was affected by this rollout to ring OSALL.

July 24  3:37 PM WEST

web

Tiago M. Pereira

Resolution has been set: Because the ring OSALL was affected with the enablement of the Feature Toggle for the removal of RequireJS, the resolution started with the creation of an RFC https://outsystemsrd.atlassian.net/browse/RFC-1236
Due to some problems in the SDLC team's pipelines, the rollback didn't occur and the version that disabled the feature flag on the affected ring reached ring OSALL and ended up fixing the issue.

July 25 10:23 AM WEST

web

Rootly

ZenDesk Event Type has been set: solved

July 25 10:23 AM WEST

web

Rootly

The Global Support team marked this incident as closed in ZenDesk.

July 25 10:33 AM WEST

web

Tiago M. Pereira

Incident has been resolved