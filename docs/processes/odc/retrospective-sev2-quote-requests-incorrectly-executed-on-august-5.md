---
title: Retrospective-SEV2-Quote requests incorrectly executed on August 5
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4369908324/Retrospective-SEV2-Quote+requests+incorrectly+executed+on+August+5
confluence_space: RKB
confluence_page_id: 4369908324
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV2-Quote requests incorrectly executed on August 5

## 📘 Overview
Author:&nbsp;Rootlytrue

Severity:&nbsp;SEV2Redtrue

Teams:&nbsp;SreBluetrue&nbsp;Data Fabric EngineBluetrue&nbsp;Data Fabric ClientsBluetrue
#### 🕐 Timestamps
Started At:&nbsp;August 6  9:48 AM WESTBluetrue

Mitigated At:&nbsp;August 20  1:03 AM WESTYellowtrue

Resolved At:&nbsp;August 20  1:03 AM WESTGreentrue
#### 🔗 Links
[Incident Page](https://rootly.com/account/incidents/827-quote-requests-incorrectly-executed-on-august-5-999bc7f3-376d-42a8-95f9-c281f1ab2b74)

[Pagerduty incident](https://outsystems.pagerduty.com/incidents/Q3ZE3UGMH3ASIA)

[Slack channel](https://slack.com/app_redirect?channel=C07G1L2NTDX&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3045268)

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

Balasundaram Natarajan

**Subject Matter Expert**

Bruno Coelho

**Stakeholder**

Zaman Akbar
#### Summary
----------------------------------------------**CONSIDERATIONS BEFORE PERFORMING THE ESCALATION TO R&amp;D (MANDATORY)**None of the below points should be overlooked. Failure to do so may imply unnecessary effort.* * *
Ensure the ticket has been **categorized**, otherwise, the R&amp;D escalation will go unnoticed and not be worked on!**1.** For **Incidents**, the **IMAX** was consulted **beforehand** on which:- No incident models were found for the reported symptoms **OR**
- The incident model did not solve the issue **OR**
- The next step indicated in the Incident Model is an escalation to R&amp;D.
**2.** For **Questions**, the ChatODC on the **Slack channel** didn't return an acceptable answer.
**3.** Any other requests that explicitly indicate an R&amp;D escalation is needed.
**4**. **Incident impact assessment** was based on the **prioritization scoring matrix**.* * ***R&amp;D ESCALATION FORM**
Section comments can be removed for R&amp;D easier interpretation.**ISSUE DESCRIPTION AND HOW TO REPRODUCE**- On August 5, there were 2 requests to generate quotes that returned empty documents.
- This was observed in the error logs
- ![](https://supportoutsystems.zendesk.com/attachments/token/6f6DDbALIEg0dVw9LjUsB1Qha/?name=image.png)OS-BERT-60407 - [500] Could not execute the specified command: HTTP 503: Service Unavailable no healthy upstream**IMPACT ON THE CUSTOMER**- High. This had happened in the Production Stage.
- The impact is that these quotes are sent to OutSystems customers and when this error happens, the request returned empty documents.
- The customer is worried the issue might happen re-occur and wants to know why this happened.
**TROUBLESHOOTING STEPS &amp; WORKAROUND**- The 2 errors on August 5th:- ![](https://supportoutsystems.zendesk.com/attachments/token/6f6DDbALIEg0dVw9LjUsB1Qha/?name=image.png)
- The timeframe of the errors in UTC- Aug 05, 2024, 07:36:59 AM UTC
Aug 05, 2024, 07:36:10 AM UTC- And we can track the process that had errors at that time: [here]- ![](https://supportoutsystems.zendesk.com/attachments/token/WxRzrDyh1ycPDrB6nM8KLVFmb/?name=image.png)
- Both look the same:- ![](https://supportoutsystems.zendesk.com/attachments/token/wbGuaWyiR7oHwod2HMDBa9lO8/?name=image.png)- and- ![](https://supportoutsystems.zendesk.com/attachments/token/NHjNR1aH0CoXdAM9MHrc4Lghu/?name=image.png)
- General Dashboard, the data action returned a 250 on both occasions:- ![](https://supportoutsystems.zendesk.com/attachments/token/wzZXumhjNDhit7JBy9esnrQCd/?name=image.png)
- Also the stack of the error log:at System.Data.CData.ApachePhoenix.ApachePhoenixCommand.ExecuteDataReader(CommandBehavior behavior) at System.Data.CData.ApachePhoenix.ApachePhoenixCommand.ExecuteReader(CommandBehavior behavior) at OutSystems.DatabaseProvider.QueryEngine.Driver.QueryEngineCommand.ExecuteReader(CommandBehavior behavior) at OutSystems.DatabaseProvider.QueryEngine.Driver.QueryEngineCommand.ExecuteDbDataReader(CommandBehavior behavior) at OutSystems.DatabaseProvider.QueryEngine.Driver.QueryEngineCommand.&lt;&gt;c__DisplayClass59_0.&lt;ExecuteDbDataReaderAsync&gt;b__0() at System.Threading.Tasks.Task`1.InnerInvoke() at System.Threading.ExecutionContext.RunInternal(ExecutionContext executionContext, ContextCallback callback, Object state)--- End of stack trace from previous location --- at System.Threading.ExecutionContext.RunInternal(ExecutionContext executionContext, ContextCallback callback, Object state) at System.Threading.Tasks.Task.ExecuteWithThreadLocal(Task&amp; currentTaskSlot, Thread threadPoolThread)--- End of stack trace from previous location --- at OutSystems.HubEdition.DatabaseAbstractionLayer.Internal.Db.Implementations.Command.ExecuteReaderAsync(String description, Boolean isApplication, Boolean skipLog, Boolean applyTransformationsToParameters, CancellationToken cancellationToken) at OutSystems.HubEdition.DatabaseAbstractionLayer.Internal.Db.Implementations.Command.ExecuteReaderAsync(String description, Boolean isApplication, Boolean skipLog, Boolean applyTransformationsToParameters, CancellationToken cancellationToken) at OutSystems.HubEdition.DatabaseAbstractionLayer.Internal.Db.Implementations.Command.ExecuteReaderAsync(String description, Boolean isApplication, Boolean skipLog, Boolean applyTransformationsToParameters, CancellationToken cancellationToken) at OutSystems.HubEdition.DatabaseAbstractionLayer.Internal.Db.Implementations.Command.ExecuteReaderAsync(String description, Boolean isApplication, Boolean skipLog, Boolean applyTransformationsToParameters, CancellationToken cancellationToken) at OutSystems.Internal.Db.DatabaseAccessProviderExtensions.ExecuteQueryAsync[TDatabaseServices,T](IDatabaseAccessProvider`1 provider, DbCommand cmd, GenericRecordList`1 rl, String description, Boolean transformParameters, Boolean skipLog, CancellationToken cancellationToken) at OutSystems.Internal.Db.DatabaseAccessProviderExtensions.ExecuteQueryAsync[TDatabaseServices,T](IDatabaseAccessProvider`1 provider, DbCommand cmd, GenericRecordList`1 rl, String description, CancellationToken cancellationToken) at ssODCQuoteGenerator.Actions.FuncActionGetQuoteDataToPrint.datasetGetQuoteById(IRequestContext requestContext, Int32 maxRecords, IterationMultiplicity multiplicity, String qpstId, CancellationToken cancellationToken) at ssODCQuoteGenerator.Actions.FuncActionGetQuoteDataToPrint.datasetGetQuoteById(IRequestContext requestContext, Int32 maxRecords, IterationMultiplicity multiplicity, String qpstId, CancellationToken cancellationToken)attributes_exception_type&nbsp;: OutSystems.Application.ErrorHandling.DatabaseException- Searching the trace shows basically the same:- ![](https://supportoutsystems.zendesk.com/attachments/token/etFTZg3mQv36QQDmax5jOVTk7/?name=image.png)
- Around the first occurrence, we can see these warnings in the K8s events, not sure if are related to the autoscale and made the service unavailable for a short period...- App requests dashboard- ![](https://supportoutsystems.zendesk.com/attachments/token/bCCaN9qvJadURqccG46DnNT24/?name=image.png)event_firstTimestamp&nbsp;2024-07-15T07:00:52Z&nbsp;event_involvedObject_apiVersion&nbsp;autoscaling/v2&nbsp;event_involvedObject_kind&nbsp;HorizontalPodAutoscaler- This error message seems to be very similar to what is explained in this IMAX entry- https://globalsupport.outsystemsenterprise.com/IMAX/VisualizeIncidentModel?IncidentModelVersionId=5090- And the past ticket #2983836- From the IMAX, it seems the issue might temporary happen when there is a deployment to **os-queryengine-controller-manager** service.- We checked for this in the Grafana Dashboard:-- https://outsystems.grafana.net/d/JkQGOx74z/services-deployment-global-view?orgId=1&amp;refresh=5m&amp;var-service=os-queryengine-controller-manager&amp;var-search=&amp;var-service_prefix=outsystems-&amp;var-negative_ring=$__all&amp;var-positive_ring=$__all&amp;var-sortServiceVariableBash=&amp;from=2024-08-03T16:00:00.000Z&amp;to=2024-08-06T15:59:59.000Z- However in the GA ring, the deployment was done like about 8 hours earlier to the time of  the incident.- The incident occurred on 15:36 (UTC +8), but the deployment was on 07:36 (UTC +8) - the screenshot below is UTC + 8- ![](https://supportoutsystems.zendesk.com/attachments/token/zZl1wOlqZiidGFbiCbDf1EY24/?name=image.png)- However looking into the 2nd Dashboard on the Data Fabric --&gt; Query Engine as explained in the above IMAX entry- https://outsystems.grafana.net/d/B8fujKKVz/query-engine?var-ring=ga&amp;var-container=outsystems-queryengine-service&amp;var-environment=3fd0a607-f7b7-4773-afb8-3a5731da0c42&amp;from=2024-08-04T16:00:00.000Z&amp;to=2024-08-05T15:59:59.000Z- We can see a dip in the liveness probe in that time frame- ![](https://supportoutsystems.zendesk.com/attachments/token/MSApND4lhgedGz9NDxRVtO4ys/?name=image.png)- This is more likely a reason that caused the error- But we don't know why the dip took place at that timeframe.- We also checked that there is no Scale-to-zero occurred during that timeframe- https://outsystems.grafana.net/d/cdeqzn1jj77cwe/general-troubleshooting?var-filter=&amp;var-exclude=&amp;var-ring=ga&amp;var-tenant=f4248c7c-5784-4166-a25f-acf30b9b652e&amp;var-cluster=$__all&amp;var-severity=Warning&amp;var-severity=Error&amp;var-severity=Critical&amp;var-runtime=$__all&amp;var-traceDuration=$__all&amp;var-region=us-east-1&amp;var-environment=$__all&amp;var-regionShort=ga-us-east-1-01&amp;var-tenant_prefix=apps&amp;var-application=$__all&amp;var-cluster_old=$__all&amp;var-module_name=&amp;from=2024-08-05T07:15:00.000Z&amp;to=2024-08-05T07:59:59.000Z&amp;timezone=browser- ![](https://supportoutsystems.zendesk.com/attachments/token/gHDzFKO8OusVdF0JgMn3EyNz0/?name=image.png)- Additionally we found a similar past RnD escalation- https://outsystemsrd.atlassian.net/browse/RDINC-25550- However, although the error seems same, the reason doesn't appear to apply in this current case.- (In the old RnD escalation, it was due to scale-to-zero happening in the **DEV** stage only).- We seek your help to understand why this error occurred in the Production stage for this customer. Thank you.**TECH DATA OR ANY OTHER RELEVANT INFO**
Ring: ga
Tenant Id: f4248c7c-5784-4166-a25f-acf30b9b652e
Tenant Prefix: apps
Region: us-east-1
WU0.921.JC5.QPA.2Y7.3JP.3V5.U74_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 Retrospective### Details
**Ring:** ga
**System-wide impact:**&nbsp; 
**Tenant ID:** f4248c7c-5784-4166-a25f-acf30b9b652e
**Tenant Prefix:** apps
**Routing Error Code:** OS-BERT
**Product Area:** -
### Impact:
Query Engine was down due to a new deployment being made and Pod Evictions. 
### Investigation and troubleshooting findings:
The errors occurred because at the time that those requests were made, Query Engine service was being updated to a newer version. During that upgrade, there was a temporary outage but the service recovered after a couple of minutes. We can see that in [this](https://outsystems.grafana.net/d/B8fujKKVz/query-engine?var-ring=ga&amp;amp;amp;var-container=outsystems-queryengine-service&amp;amp;amp;var-environment=3fd0a607-f7b7-4773-afb8-3a5731da0c42&amp;amp;amp;from=2024-08-04T16:00:00.000Z&amp;amp;amp;to=2024-08-05T15:59:59.000Z&amp;amp;var-container=outsystems-queryengine-service&amp;amp;var-environment=3fd0a607-f7b7-4773-afb8-3a5731da0c42&amp;amp;from=2024-08-05T06:01:54.270Z&amp;amp;to=2024-08-05T07:52:20.029Z&amp;var-container=outsystems-queryengine-service&amp;var-environment=fad5c7a2-78b7-488a-959f-06cddfb6c518&amp;var-environment=74c98b52-cb79-4464-86ff-2c1f54aa4194&amp;var-environment=cc6f4cb6-b43f-4839-8531-4f75a7f03b5b&amp;from=2024-08-04T23:00:00.000Z&amp;to=2024-08-05T22:59:59.000Z&amp;refresh=30s) Dashboard  

 That happened not only becasue of the deploy of a new version, but also because the istio proxy sidecar pods were being DRAINED. That can be seen in [this](https://outsystems.grafana.net/explore?schemaVersion=1&amp;panes=%7B%22gh6%22:%7B%22datasource%22:%22grafanacloud-outsystemstest-logs%22,%22queries%22:%5B%7B%22datasource%22:%7B%22type%22:%22loki%22,%22uid%22:%22grafanacloud-outsystemstest-logs%22%7D,%22editorMode%22:%22code%22,%22expr%22:%22%7Bring%3D~%5C%22ga%5C%22,%20k8s_namespace_name%3D~%5C%22fad5c7a2-78b7-488a-959f-06cddfb6c518%7C74c98b52-cb79-4464-86ff-2c1f54aa4194%7Ccc6f4cb6-b43f-4839-8531-4f75a7f03b5b%5C%22,%20job%3D%5C%22fluentbit%5C%22%7D%20%5Cr%5Cn%7C%20json%20level%3D%5C%22level%5C%22,%20log%3D%5C%22log%5C%22,%20logger%3D%5C%22logger%5C%22,%20environment%3D%5C%22outsystems_tenant_key%5C%22,%20exception%3D%5C%22exception%5C%22,%20pod%3D%5C%22kubernetes.pod_name%5C%22,%20image%3D%5C%22kubernetes.container_image%5C%22%20,%20version%3D%5C%22service_version%5C%22%5Cr%5Cn%7C%20logfmt%20%5Cr%5Cn%7C%20line_format%20%60%7B%7B__timestamp__%20%7C%20date%20%5C%222006-02-01%2015:04:05%5C%22%20%7D%7D%20-%20%7B%7B.environment%20%7C%20trunc%2036%20%7D%7D%20-%20%7B%7B.log%7D%7D%60%22,%22maxLines%22:2000,%22queryType%22:%22range%22,%22refId%22:%22A%22%7D%5D,%22range%22:%7B%22from%22:%221722841200000%22,%22to%22:%221722848399000%22%7D%7D%7D&amp;orgId=1) logs. 

This led to the pods being evicted. You can see that in [these](https://outsystems.grafana.net/explore?schemaVersion=1&amp;panes=%7B%22gh6%22:%7B%22datasource%22:%22grafanacloud-outsystemstest-logs%22,%22queries%22:%5B%7B%22datasource%22:%7B%22type%22:%22loki%22,%22uid%22:%22grafanacloud-outsystemstest-logs%22%7D,%22editorMode%22:%22code%22,%22expr%22:%22%7Bring%3D~%5C%22ga%5C%22,%20k8s_namespace_name%3D~%5C%22fad5c7a2-78b7-488a-959f-06cddfb6c518%7C74c98b52-cb79-4464-86ff-2c1f54aa4194%7Ccc6f4cb6-b43f-4839-8531-4f75a7f03b5b%5C%22,%20job%3D%5C%22fluentbit%5C%22%7D%20%5Cr%5Cn%7C%20json%20level%3D%5C%22level%5C%22,%20log%3D%5C%22log%5C%22,%20logger%3D%5C%22logger%5C%22,%20environment%3D%5C%22outsystems_tenant_key%5C%22,%20exception%3D%5C%22exception%5C%22,%20pod%3D%5C%22kubernetes.pod_name%5C%22,%20image%3D%5C%22kubernetes.container_image%5C%22%20,%20version%3D%5C%22service_version%5C%22%5Cr%5Cn%7C%20logfmt%20%5Cr%5Cn%7C%20line_format%20%60%7B%7B__timestamp__%20%7C%20date%20%5C%222006-02-01%2015:04:05%5C%22%20%7D%7D%20-%20%7B%7B.environment%20%7C%20trunc%2036%20%7D%7D%20-%20%7B%7B.log%7D%7D%60%22,%22maxLines%22:2000,%22queryType%22:%22range%22,%22refId%22:%22A%22%7D%5D,%22range%22:%7B%22from%22:%221722841200000%22,%22to%22:%221722848399000%22%7D%7D%7D&amp;orgId=1) logs.
### Resolution:
The system was back online after 5 minutes. In this situations, we just have to wait and confirm that the system is able to start up correctly. 
## Tasks performed during incident resolution:
&nbsp;
## Executive Summary
Query Engine had a new version being deployed on the 5th of August. While this happened, Kubernetes also drained some istio proxy sidecar pods led to the eviction of the Query Engine pods. This is common when a Query Engine version is being deployed. 

After a few minutes, the pods had started up, but, unfortunately there was some downtime that the client noticed and created an Incident due to this. 

[Guidelines](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4144496679/Incident+Retrospectives+-+Playbook#STEP-3---Write-the-Executive-Summary)
## Root Causes 
- 
Drainage of Istio Proxy

- 
Pod Eviction

- 
Query Engine only as 1 pod and PDB cannot be 0. 

[Guidelines](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4144496679/Incident+Retrospectives+-+Playbook#STEP-1---Perform-the-Root-Cause-Analysis)

If the customer needs formal RCA, please fill out the following field with the document URL

[Please follow these instructions and place the RCA URL in the field below.](https://docs.google.com/document/d/13rXmBsOJh73nV2D6Z17SIBGBu2HOTWty5ddsvU000JM/edit#heading=h.bqxasxszr5q)

RCA URL

&lt;Place the URL of the customer RCA here if you have created one&gt;
## ⌛ Timeline
[View on Rootly](https://rootly.com/account/incidents/827-quote-requests-incorrectly-executed-on-august-5-999bc7f3-376d-42a8-95f9-c281f1ab2b74)

**Date**

**Source**

**User**

**Event**

August 6  9:20 AM WEST

web

Rootly

created an alert via

August 6  9:20 AM WEST

web

Rootly

Rootly created this incident

August 6  9:20 AM WEST

web

Rootly

In triage date has been set to August 6  9:20 AM WEST

August 6  9:20 AM WEST

web

Rootly

[Slack Channel](https://slack.com/app_redirect?channel=C07G1L2NTDX&amp;team=T041063TZ) has been created

August 6  9:20 AM WEST

web

Rootly

Ring: ga
System-wide impact:  
Tenant ID: f4248c7c-5784-4166-a25f-acf30b9b652e
Tenant Prefix: apps
Routing Error Code: OS-BERT
Product Area: -

August 6  9:20 AM WEST

web

Rootly

[PagerDuty Incident](https://outsystems.pagerduty.com/incidents/Q3ZE3UGMH3ASIA) has been created.

📱 Notified Balasundaram Natarajan by SMS.

&nbsp;&nbsp;

📧 Notified Balasundaram Natarajan by email.

&nbsp;&nbsp;

📞 Notified Balasundaram Natarajan by phone.

August 6  9:20 AM WEST

web

Rootly

Balasundaram Natarajan has been assigned as Engineer

August 6  9:23 AM WEST

web

Rootly

Balasundaram Natarajan acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q3ZE3UGMH3ASIA). (via Website)

August 6  9:30 AM WEST

web

Rootly

This incident was instantiated in Jira: RDINC-28098. Please work the incident using Rootly

August 6  9:42 AM WEST

slack

balasundaram.natarajan

this is from us-east-1, no SLO level impact

[image.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDI1MTU5LCJwdXIiOiJibG9iX2lkIn19--64a61c19a302d5b333e16b12f46d0b24db3f9be3/image.png)

[image.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDI1MTYwLCJwdXIiOiJibG9iX2lkIn19--14556859d44f60da8a9c6d31a463b94927d9183d/image.png)

August 6  9:48 AM WEST

web

Balasundaram Natarajan

Incident has been started

August 6  9:48 AM WEST

web

Rootly

Pagerduty Integrations acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q3ZE3UGMH3ASIA). (via Website)

August 6 10:20 AM WEST

web

Rootly

This incident was instantiated in Jira: RDINC-28098. Please work the incident using Rootly

August 6 10:27 AM WEST

web

Rui Garcia

Global Support analysis is pretty much on point. I&rsquo;ll just summarize it here.Customer has runtime errors in production while execution queries to External Database. There are two occurrences at Aug 05, 2024, 07:36:10 and 07:36:59 UTC.If we look at an example trace, we can see the error was fast. In the logs we have the errorCould not execute the specified command: HTTP 503: Service Unavailable no healthy upstreamwhich suggests the services that support the query execution where not up.In Kubernetes Event logs we can observe the auto-scaling moments:
- At 07:34:37.450, outsystems-queryengine-service-6d97799f9c was scaled down from 1 to 0.
- At 07:36:38.719, outsystems-queryengine-service-fbf477449 was scaled up from 0 to 1.
Using the service logs we can see the service only finished the startup at 07:37:06.576. This time period encompasses both failed request and explains why the request couldn&rsquo;t be handled.If this service is meant to be setup with scale to zero in production environment, then Query Engine Provider must be scale-to-zero aware, and tolerate 503 failures with a retry mechanism with enough time for the service to come back up and handle the request.If this is not meant to be setup with scale to zero, then we just probably fix the configuration so the service is readily available when needed.As this asset is owned, by Data Fabric Team, I&rsquo;m reassigning the case for further follow up.

August 6 10:27 AM WEST

web

Rui Garcia

Teams has been added: [Data Fabric Engine](/account/teams/data-fabric-engine/status)&nbsp;&nbsp;[Data Fabric Clients](/account/teams/data-fabric-clients/status)

August 6 10:27 AM WEST

web

Rui Garcia

Teams has been removed: [Backend Runtime](/account/teams/backend-runtime/status)

August 6 10:28 AM WEST

web

Balasundaram Natarajan

Swarm has been set: Data Fabric Engine

August 6 10:29 AM WEST

web

Rootly

Pagerduty Integrations added Akula Anudeep as responder in [PagerDuty](https://outsystems.pagerduty.com/incidents/Q3ZE3UGMH3ASIA)

August 6 10:29 AM WEST

web

Rootly

Akula Anudeep joined this [PagerDuty](https://outsystems.pagerduty.com/incidents/Q3ZE3UGMH3ASIA) incident.

August 6 10:29 AM WEST

web

Rootly

Akula Anudeep acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q3ZE3UGMH3ASIA). (via Website)

August 6 10:46 AM WEST

web

Balasundaram Natarajan

Bruno Coelho has been assigned as Subject Matter Expert

August 6 10:50 AM WEST

slack

Akula Anudeep

Hello guys, from the logs here: [https://outsystems.grafana.net/d/6-jtZX07z/kubernetes-events?orgId=1&amp;var-datasource_logs[&hellip;]from=2024-08-05T07:34:33.000Z&amp;to=2024-08-05T07:59:59.000Z](https://outsystems.grafana.net/d/6-jtZX07z/kubernetes-events?orgId=1&amp;var-datasource_logs=grafanacloud-outsystemstest-logs&amp;var-ring=ga&amp;var-stamp=runp-ga-us-east-1-01&amp;var-level=$__all&amp;var-search=3fd0a607-f7b7-4773-afb8-3a5731da0c42&amp;from=2024-08-05T07:34:33.000Z&amp;to=2024-08-05T07:59:59.000Z). Looks like the issue is with the `outsystems-queryengine-service`, the Query Engine team from Data Fabric I mean

August 6 11:36 AM WEST

web

Bruno Coelho

The errors occurred because at the time that those requests were made, Query Engine service was being updated to a newer version. During that upgrade there was a temporary outage but the service recovered after a couple of minutes.
https://outsystems.grafana.net/d/B8fujKKVz/query-engine?var-ring=ga&amp;var-container=outsystems-queryengine-service&amp;var-environment=3fd0a607-f7b7-4773-afb8-3a5731da0c42&amp;from=2024-08-04T16:00:00.000Z&amp;to=2024-08-05T15:59:59.000Z&amp;var-container=outsystems-queryengine-service&amp;var-environment=3fd0a607-f7b7-4773-afb8-3a5731da0c42&amp;from=2024-08-05T06:01:54.270Z&amp;to=2024-08-05T07:52:20.029Z

August 6 12:12 PM WEST

web

Vasco Gomes

Send ZenDesk private comment has been set: At the moment Query Engine cannot scale to 0, so currently this is a limitation on our Design.  
We have an initiative that is going to be started in this PI to address this limitation (Cost Optimization). Still, until that is made, every time that a new version is deployed, it can introduce downtime to clients.

August 6 12:12 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:
At the moment Query Engine cannot scale to 0, so currently this is a limitation on our Design.  
We have an initiative that is going to be started in this PI to address this limitation (Cost Optimization). Still, until that is made, every time that a new version is deployed, it can introduce downtime to clients.

August 6 12:12 PM WEST

web

Rootly

Send ZenDesk private comment has been unset

August 6 12:12 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:

August 6 12:16 PM WEST

web

Bruno Coelho

Send ZenDesk private comment has been set: The errors occurred because at the time that those requests were made, Query Engine service was being updated to a newer version. During that upgrade there was a temporary outage but the service recovered after a couple of minutes.

August 6 12:16 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:
The errors occurred because at the time that those requests were made, Query Engine service was being updated to a newer version. During that upgrade there was a temporary outage but the service recovered after a couple of minutes.

August 6 12:16 PM WEST

slack

Rootly

MESSAGE SENT FROM R&amp;D: The errors occurred because at the time that those requests were made, Query Engine service was being updated to a newer version. During that upgrade there was a temporary outage but the service recovered after a couple of minutes.

August 6 12:16 PM WEST

web

Rootly

Send ZenDesk private comment has been unset

August 6 12:16 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:

August 7  8:49 AM WEST

web

Balasundaram Natarajan

Send ZenDesk private comment has been set: Hi
Hope the answer is given for the why issue occured. pl confirm if this ticket can be closed

August 7  8:49 AM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:
Hi
Hope the answer is given for the why issue occured. pl confirm if this ticket can be closed

August 7  8:49 AM WEST

web

Rootly

Send ZenDesk private comment has been unset

August 7  8:49 AM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:

August 12  7:40 AM WEST

web

Balasundaram Natarajan

Send ZenDesk private comment has been set: Kindly pl confirm if this ticket can be closed

August 12  7:40 AM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:
Kindly pl confirm if this ticket can be closed

August 12  7:40 AM WEST

web

Rootly

Send ZenDesk private comment has been unset

August 12  7:40 AM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:

August 12 10:38 AM WEST

web

Balasundaram Natarajan

Zaman Akbar has been assigned as Stakeholder

August 20  1:03 AM WEST

web

Rootly

The Global Support team marked this incident as closed in ZenDesk.

August 20  1:03 AM WEST

web

Rootly

Incident has been resolved

August 20  1:03 AM WEST

web

Rootly

ZenDesk Event Type has been set: solved