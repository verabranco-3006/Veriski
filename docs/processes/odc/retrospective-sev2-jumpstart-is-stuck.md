---
title: Retrospective-SEV2-Jumpstart is stuck
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4390748372/Retrospective-SEV2-Jumpstart+is+stuck
confluence_space: RKB
confluence_page_id: 4390748372
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV2-Jumpstart is stuck

## 📘 Overview
Author:&nbsp;Rootlytrue

Severity:&nbsp;SEV2Redtrue

Teams:&nbsp;Runtime Data ModelBluetrue&nbsp;SreBluetrueCMCPBlueMaestroBlue  

Types:&nbsp;Customer EscalatedBluetrue
#### 🕐 Timestamps
Started At:&nbsp;August 28  9:48 AM WESTBluetrue

Mitigated At:&nbsp;August 28 11:41 AM WESTYellowtrue

Resolved At:&nbsp;August 28 12:18 PM WESTGreentrue
#### 🔗 Links
[Incident Page](https://rootly.com/account/incidents/940-jumpstart-is-stuck)

[Pagerduty incident](https://outsystems.pagerduty.com/incidents/Q1VCLFV92W4Q7I)

[Slack channel](https://slack.com/app_redirect?channel=C07JSAC24AH&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3054269)

Related RFCs:
- 
RFC-1370ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

- 
RFC-1373ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

#### 🧑&zwj;🚒 Incident Rolestrue
**Commander**

Tiago Oliveira

**Engineer**

Balasundaram Natarajan
#### Summary
**ISSUE DESCRIPTION AND HOW TO REPRODUCE**

- Our solution architect is unable to publish their app onto **https://sgjs.outsystems.dev** and received an error **OS-RDBE-GEN-50000** on ODC Studio IDE. - [Link](https://outsystems.grafana.net/d/o2_h2-Bnz/publish-service-1cp-by-tenant?var-interval=$__auto&amp;var-ring=ga&amp;var-region=ap-southeast-1&amp;var-stamp=plat-ga-ap-se-1-01&amp;var-tenant=$__all&amp;var-exclude_tenant=$__all&amp;from=now-12h&amp;to=now) 

**IMPACT ON THE CUSTOMER**

- The OutSystems Singapore Jumpstart event that was scheduled today was impacted heavily and was stuck midway due to the error. - [https://www.outsystems.com/events/jump-start/apac/singapore/](https://www.outsystems.com/events/jump-start/apac/singapore/)

**TROUBLESHOOTING STEPS &amp; WORKAROUND**

- One of the trace in which we can see errors on this tenant seem related to the OSADMIN password: [Link](https://outsystems.grafana.net/d/A1YJOsa7z/1cp-logs?orgId=1&amp;var-ring=ga&amp;var-level=Warning&amp;var-level=Error&amp;var-service=Publish.Service&amp;var-service=Database.Job&amp;var-service=Database.Script.Executor&amp;var-service=DatabaseEvent.Service&amp;var-traceId=00f8d5ab-7e48-4569-9185-e7e6983c8d8b&amp;from=2024-08-27T07:32:35.853Z&amp;to=2024-08-28T07:32:35.854Z)

- Based on this [past ticket](https://outsystemsrd.atlassian.net/browse/RDINC-19690) #2975277 #3008337 | we are requesting help from R&amp;D to check if there is an issue with the tenants itself or any of the components.

**TECH DATA OR ANY OTHER RELEVANT INFO**

- Tenant ID (mandatory): 1859d705-cfaf-4b60-9eda-996ddf3815e2

- Stage ID (mandatory): Development / 8a506740-8c67-40d3-91f8-f297367697e0

- Application Key (mandatory if appl.):  0839d251-ea6b-421b-bc4c-e173eace3457

- Timeline with start and end date/hour (mandatory): Aug 28, 2024, 12:03 PM UTC +8

- Grafana dashboards (adjusted to timeline/tenant/environment/service): [Dashboard](https://outsystems.grafana.net/d/o2_h2-Bnz/publish-service-1cp-by-tenant?var-interval=$__auto&amp;var-ring=ga&amp;var-region=ap-southeast-1&amp;var-stamp=plat-ga-ap-se-1-01&amp;var-tenant=$__all&amp;var-exclude_tenant=$__all&amp;from=now-12h&amp;to=now)
## 📝 Retrospective### Details
**Ring:** ga
**System-wide impact:**&nbsp;No
**Tenant ID:** 1859d705-cfaf-4b60-9eda-996ddf3815e2
**Tenant Prefix:** sgjs
**Routing Error Code:** N/A
**Product Area:** Phoenix::Application Runtime::Database access
### Impact:
A single new tenant could not deploy its applications.
### Investigation and troubleshooting findings:
It was found that the tenant provisioning failed, still we provided access to the failing tenant to the client.
### Resolution:
Rotating user passwords and retriggering shared apps deployment was enough.
## Tasks performed during incident resolution:
**Ticket:** RFC-1370ef8955cb-cb21-32a7-b692-01ace42388d6System Jira  

**Date:** 

- 
Logs confirmed the users password rotation failed, so a manual rotation was triggered.

**Ticket:** RFC-1373ef8955cb-cb21-32a7-b692-01ace42388d6System Jira  

**Date:** 

- 
SAS mistakenly took the process as successful, when it was not, so a maneuver was made in order to force the deployment retrigger.

## Executive Summary
On  09:31 AM WEST, we received [a ticket](https://rootly.com/account/incidents/940-jumpstart-is-stuck) reporting that a recently created tenant could not deploy any application. This tenant was actually for an event (Jumpstart) so the time to fix was critical.

Immediately after receiving the info from SRE team (), Runtime Data Model team () found error logs showing that the users password rotation, a mandatory step in tenant provisioning, was never successful.

At 10:36 AM, while RDM team was working to fix the first issue, it requested Maestro&rsquo;s team () to join because the tenant should never have been made available, and we expected Sample Data deployment to have failed as well, meaning redeploying was most likely necessary.

After rotating the users' passwords at 10:49 AM and retriggering the publications at 11:11 AM, which led to the redeployment of Sample Data at 11:40 AM, the tenant was finally ready for a new deployment.

At 12:18PM we have confirmation that 1CPs were finally working.
## Root Causes 
After the analysis of the incident, it was determined that the root cause was that the deployments are triggered after the database is created - not after the database bootstrap is complete, which led to deployments trying to run on a database still warming-up.

It was expected that SAS (Shared Apps Service) fails in this scenario, so a re-run from CMCP later on (when the database bootstrap is complete) is usually enough. For this particular scenario, though, SAS led to believe the deployment was successful and, for that reason, CMCP took the tenant provision as successful. 

This erroneous behavior of SAS was not directly caused by a bug in the service itself, but rather by a bug in another service, PS (Publish Service). This bug in PS occurred under very specific conditions, where multiple retries to publish an application triggered consecutive 1CP operations. In one case, a 1CP operation was incorrectly marked as successful. As a result, SAS mistakenly believed the installation was successful and stopped attempting to install the problematic application. This led SAS to mark the installation as complete, which in turn caused CMCP to mark the tenant provisioning as successful.
## ⌛ Timeline
[View on Rootly](https://rootly.com/account/incidents/940-jumpstart-is-stuck)

Full timeline
**Date**

**Source**

**User**

**Event**

August 28  9:31 AM WEST

web

Rootly

created an alert via

August 28  9:31 AM WEST

web

Rootly

Rootly created this incident

August 28  9:31 AM WEST

web

Rootly

In triage date has been set to August 28  9:31 AM WEST

August 28  9:31 AM WEST

web

Rootly

Access Zendesk ticket (VPN) has been set: https://extranetinternalapps-prd.outsystems.net/TKT_CustomerTicket_UI/CustomerTicket_Detail?TicketITSMId=3054269

August 28  9:31 AM WEST

web

Rootly

[Slack Channel](https://slack.com/app_redirect?channel=C07JSAC24AH&amp;team=T041063TZ) has been created

August 28  9:31 AM WEST

web

Rootly

Ring: ga
System-wide impact:  
Tenant ID: 1859d705-cfaf-4b60-9eda-996ddf3815e2
Tenant Prefix: sgjs
Routing Error Code: OS-RDBE
Product Area: -

August 28  9:31 AM WEST

web

Rootly

[PagerDuty Incident](https://outsystems.pagerduty.com/incidents/Q1VCLFV92W4Q7I) has been created.

📱 Notified Balasundaram Natarajan by SMS.

&nbsp;&nbsp;

📧 Notified Balasundaram Natarajan by email.

&nbsp;&nbsp;

📞 Notified Balasundaram Natarajan by phone.

August 28  9:31 AM WEST

web

Rootly

Balasundaram Natarajan has been assigned as Engineer

August 28  9:32 AM WEST

web

Rootly

Balasundaram Natarajan acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q1VCLFV92W4Q7I). (via Phone)

August 28  9:41 AM WEST

web

Rootly

This incident was instantiated in Jira: RDINC-29230. Please work the incident using Rootly

August 28  9:48 AM WEST

web

Balasundaram Natarajan

Incident has been started

August 28  9:48 AM WEST

web

Rootly

Pagerduty Integrations acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q1VCLFV92W4Q7I). (via Phone)

August 28  9:48 AM WEST

slack

balasundaram.natarajan

there is no system wide impact on 1 click publish on ap-southeast-1

[image.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDM5ODczLCJwdXIiOiJibG9iX2lkIn19--fa3661c969b0ebf48d646b526193dafebe4bc838/image.png)

August 28  9:52 AM WEST

slack

balasundaram.natarajan

errors from grafana 1cp logs [https://outsystems.grafana.net/d/A1YJOsa7z/1cp-logs?orgId=1&amp;var-ring=ga&amp;var-level=Warnin[&hellip;]vice=Publish.Service&amp;var-service=Database.Jo&amp;var-traceId=](https://outsystems.grafana.net/d/A1YJOsa7z/1cp-logs?orgId=1&amp;var-ring=ga&amp;var-level=Warning&amp;var-level=Error&amp;var-service=Publish.Service&amp;var-service=Database.Jo&amp;var-traceId=)```Unable to read tenant cr 0d8c201c-efaa-4ebb-9257-94ece48a48d4 
at OutSystems.Publish.Connectors.KubernetesClients.K8sFacade.GetTenantInfo(Guid tenantId) in /src/src/OutSystems.Publish.Connectors/KubernetesClients/K8sFacade.cs:line 97at OutSystems.Publish.DataAccess.DbVersion.DbVersionResolver.GetTenantDbVersion(Guid tenantId) in /src/src/OutSystems.Publish.DataAccess/DbVersion/DbVersionResolver.cs:line 18at OutSystems.Publish.DataAccess.Repository.DataReplicator.MapPrimaryAndSecondaryDbOpenConn(Guid tenantId, CancellationToken cancellationToken) in /src/src/OutSystems.Publish.DataAccess/Repository/DataReplicator.cs:line 126at OutSystems.Publish.DataAccess.Repository.DataReplicator.ExecuteWithFallback[T](Guid tenantId, Func`3 execute, Boolean rollbackIfFailure, CancellationToken cancellationToken) in /src/src/OutSystems.Publish.DataAccess/Repository/DataReplicator.cs:line 102at OutSystems.Publish.DataAccess.Repository.DataReplicator.Read[T](Guid tenantId, Func`3 read, CancellationToken cancellationToken)at OutSystems.Publish.DataAccess.Repository.ApplicationProcessRepository.Filter(Guid tenantId, ApplicationProcessQueryFilter filter, IResou```

August 28 10:01 AM WEST

web

Tiago Oliveira

Tiago Oliveira has been assigned as Commander

August 28 10:15 AM WEST

slack

Thiago Chaves Campos (thc)

Standard [RFC created](https://outsystemsrd.atlassian.net/browse/RFC-1370) in order to force password rotation for failing database users.

August 28 10:31 AM WEST

slack

Thiago Chaves Campos (thc)

osAdmin password rotated, 1CPs will most probably succeed from this point on

August 28 10:31 AM WEST

slack

balasundaram.natarajan

osadmin-v2 secret is rotated on rundev / EnvID: 8a506740-8c67-40d3-91f8-f297367697e0

August 28 10:31 AM WEST

web

Rootly

This incident was instantiated in Jira: RDINC-29230. Please work the incident using Rootly

August 28 10:49 AM WEST

web

Thiago Campos

Send ZenDesk private comment has been set: 

We have unlocked the users, so the deployments should work, so the ticket is partially mitigated. Still, sample data should be redeployed as well, and we're currently working on that.

August 28 10:49 AM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:

We have unlocked the users, so the deployments should work, so the ticket is partially mitigated. Still, sample data should be redeployed as well, and we're currently working on that.

August 28 10:49 AM WEST

web

Rootly

Send ZenDesk private comment has been unset

August 28 10:49 AM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:

August 28 10:51 AM WEST

slack

Thiago Chaves Campos (thc)

Users password have been dealt with, so deployments should work.

August 28 11:06 AM WEST

slack

tiago.oliveira

[https://outsystemsrd.atlassian.net/browse/RFC-1373](https://outsystemsrd.atlassian.net/browse/RFC-1373)
@balasundaram.natarajan RFC above ☝️

August 28 11:12 AM WEST

slack

balasundaram.natarajan

```removed the annotation for the stuck env
kubectl get  Environment 8a506740-8c67-40d3-91f8-f297367697e0
NAME                                   DISPLAYNAME   PURPOSE       TENANT                                 STATE
8a506740-8c67-40d3-91f8-f297367697e0   Development   Development   1859d705-cfaf-4b60-9eda-996ddf3815e2   Ready
~&gt; kubectl annotate Environment 8a506740-8c67-40d3-91f8-f297367697e0 -n default [sharedassets.outsystemscloud.com/publication-status-](http://sharedassets.outsystemscloud.com/publication-status-)[environment.platform.outsystemscloud.com/8a506740-8c67-40d3-91f8-f297367697e0](http://environment.platform.outsystemscloud.com/8a506740-8c67-40d3-91f8-f297367697e0) annotated
~&gt; ```

August 28 11:16 AM WEST

slack

tiago.oliveira

Waiting for the retry from SAS that should take 30min.
ETA 11:40.

August 28 11:35 AM WEST

slack

tiago.oliveira

For reference, this is the bug that caused the rotation to fail initially:
[https://outsystemsrd.atlassian.net/browse/RPLAT-2663](https://outsystemsrd.atlassian.net/browse/RPLAT-2663)The TF Runners in GA are slow to run, so the database took more time to get created and bootstrapped.
For that reason, the secret rotation failed to set the password and stopped retrying after some time.

August 28 11:40 AM WEST

slack

Guilherme Candido

[https://outsystemsrd.atlassian.net/browse/RDMAST-1568](https://outsystemsrd.atlassian.net/browse/RDMAST-1568)

August 28 11:41 AM WEST

web

Tiago Oliveira

Incident has been mitigated

August 28 11:42 AM WEST

web

Thiago Campos

Send ZenDesk private comment has been set: 

Sample data deployment [finished successfully](https://outsystems.grafana.net/d/A1YJOsa7z/1cp-logs?orgId=1&amp;var-ring=ga&amp;var-level=$__all&amp;to=now&amp;var-service=$__all&amp;var-traceId=4c80698b-4dba-43f3-b75a-f02bb1afdf8d&amp;from=2024-08-28T09:40:25.913Z). The issue should be totally mitigated now.

August 28 11:42 AM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:

Sample data deployment [finished successfully](https://outsystems.grafana.net/d/A1YJOsa7z/1cp-logs?orgId=1&amp;var-ring=ga&amp;var-level=$__all&amp;to=now&amp;var-service=$__all&amp;var-traceId=4c80698b-4dba-43f3-b75a-f02bb1afdf8d&amp;from=2024-08-28T09:40:25.913Z). The issue should be totally mitigated now.

August 28 11:42 AM WEST

web

Rootly

Send ZenDesk private comment has been unset

August 28 11:42 AM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:

August 28 11:43 AM WEST

slack

Thiago Chaves Campos (thc)

The issue should be totally mitigated now.

August 28 12:18 PM WEST

web

Rootly

The Global Support team marked this incident as closed in ZenDesk.

August 28 12:18 PM WEST

web

Rootly

Incident has been resolved

August 28 12:18 PM WEST

web

Rootly

ZenDesk Event Type has been set: solved
## 📝 Follow Up Items
[View on Rootly](https://rootly.com/account/incidents/940-jumpstart-is-stuck#nav-action-items)

**Summary**

**Priority**

**Status**

**Assignee**

**Links**

We need to understand why a 1CP operation finished successfully when it should not have. https://outsystemsrd.atlassian.net/browse/RDMAST-1568

HighRed

OpenBlue

Maestro

RDMAST-1568ef8955cb-cb21-32a7-b692-01ace42388d6System Jira

 

We need to understand why RDM alarm did not trigger for the password rotation.

MediumYellowtrue

OpenBluetrue

RDM

RPLAT-2750ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

We should understand if we can build a way for SAS to immediately process a retry without waiting 30min. MTTR delayed.

LOWBlue

DiscardedRed

Maestro

Reason: This was a corner case scenario. Creating a feature for this won&rsquo;t add much value, once usually 30 mins is enough - in tenant provisioning processes.

We should avoid starting deployments while the Database bootstrap is not finished. 

LowBlue  

DISCARDEDRed  

RDM &amp; CMCP

Reason: This would ultimately lead to duplicate checks that should get in sync, which could increase entropy and risks. SAS as a last-barrier seems enough, as the bug there was fixed.