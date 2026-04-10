---
title: Retrospective-SEV2-[ODC Studio] Unable to publish my "connections" app.
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4329898136/Retrospective-SEV2-+ODC+Studio+Unable+to+publish+my+connections+app.
confluence_space: RKB
confluence_page_id: 4329898136
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV2-[ODC Studio] Unable to publish my "connections" app.

## 📘 Overview
Author:&nbsp;Rootlytrue

Severity:&nbsp;SEV2Redtrue

Teams:&nbsp;SreBluetrue
#### 🕐 Timestamps
Started At:&nbsp;July 31 11:52 PM WESTBluetrue

Mitigated At:&nbsp;August 1 12:43 AM WESTYellowtrue

Resolved At:&nbsp;August 2 12:07 PM WESTGreentrue
#### 🔗 Links
[Incident Page](https://rootly.com/account/incidents/785-odc-studio-unable-to-publish-my-connections-app)

[Pagerduty incident](https://outsystems.pagerduty.com/incidents/Q36WSMEWIBEJJ5)

[Slack channel](https://slack.com/app_redirect?channel=C07EK0BK7QF&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3043214)

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

Nuno Rego
#### Summary
----------------------------------------------**ISSUE DESCRIPTION AND HOW TO REPRODUCE**- The requester is having issues publishing the connections application as they are getting these errors: `OS-BLD-COMP-50000 and OS-DPL-50205`**IMPACT ON THE CUSTOMER**- This impacts the requester's ability to develop and deliver the necessary features for the current sprint**TROUBLESHOOTING STEPS &amp; WORKAROUND**- Based on the validations done so far, this issue seems pretty related to this other Jira case that I created yesterday:- https://outsystemsrd.atlassian.net/browse/RDINC-27870- Initially, it seemed that the error might have been related to https://outsystemsrd.atlassian.net/browse/RDINC-21465, but after analyzing the case again it seems like is related to the other case mentioned above, at least that is what I think, let me explain:
- Publish dashboard -&gt; https://outsystems.grafana.net/d/cdgg5feb0g6bkd/publish-deploy-mabs?orgId=1&amp;var-ring=ea&amp;var-tenant=dc3a3772-693b-4b6a-aa61-5fea3976eeb3&amp;var-mobile_platform=$__all&amp;var-region=us-east-1&amp;var-application=$__all&amp;var-stamp=$__all&amp;from=2024-07-30T20:07:35.321Z&amp;to=2024-07-31T20:07:35.321Z&amp;timezone=utc- ![](https://supportoutsystems.zendesk.com/attachments/token/QEJOw0hXHOw0Ip0oEj5c2PcK4/?name=image.png)
- If we go to the trace, we can see these failures- ![](https://supportoutsystems.zendesk.com/attachments/token/TYbWXvkDHhQzVwN2VeFrNFs7T/?name=image.png)
- Error reason logs just shows these errors: (1CP logs) -&gt; https://outsystems.grafana.net/d/A1YJOsa7z/1cp-logs?orgId=1&amp;var-ring=ea&amp;var-level=Warning&amp;var-level=Error&amp;var-service=Publish.Service&amp;var-traceId=&amp;from=2024-07-30T20:07:35.321Z&amp;to=2024-07-31T20:07:35.321ZFailed to retrieve Tenant CR---|Operation returned an invalid status code 'NotFound', response body {&quot;kind&quot;:&quot;Status&quot;,&quot;apiVersion&quot;:&quot;v1&quot;,&quot;metadata&quot;:{},&quot;status&quot;:&quot;Failure&quot;,&quot;message&quot;:&quot;tenants.platform.outsystemscloud.com \&quot;6f6999dd-8c7b-43ca-be4e-c5f5a78db2e6\&quot; not found&quot;,&quot;reason&quot;:&quot;NotFound&quot;,&quot;details&quot;:{&quot;name&quot;:&quot;6f6999dd-8c7b-43ca-be4e-c5f5a78db2e6&quot;,&quot;group&quot;:&quot;platform.outsystemscloud.com&quot;,&quot;kind&quot;:&quot;tenants&quot;},&quot;code&quot;:404}---| at k8s.Kubernetes.SendRequestRaw(String requestContent, HttpRequestMessage httpRequest, CancellationToken cancellationToken) at k8s.AbstractKubernetes.ICustomObjectsOperations_GetClusterCustomObjectWithHttpMessagesAsync[T](String group, String version, String plural, String name, IReadOnlyDictionary`2 customHeaders, CancellationToken cancellationToken) at k8s.AbstractKubernetes.k8s.ICustomObjectsOperations.GetClusterCustomObjectWithHttpMessagesAsync[T](String group, String version, String plural, String name, IReadOnlyDictionary`2 customHeaders, CancellationToken cancellationToken) at OutSystems.Publish.Connectors.KubernetesClients.K8sFacade.&lt;&gt;c__DisplayClass21_0.&lt;&lt;GetTenantCustomResource&gt;b__0&gt;d.MoveNext() in /src/src/OutSystems.Publish.Connectors/KubernetesClients/K8sFacade.cs:line 124--- End of stack trace from previous location --- at Polly.Retry.AsyncRetryEngine.ImplementationAsync[TResult](Func`3 action, Context context, CancellationToken cancellationToken, ExceptionPredicates shouldRetryExceptionPredicates, ResultPredicates`1 shouldRetryResultPredicates, Func`5 onRetryAsync, Int32 permittedRetryCount, IEnumerable`1 sleepDurationsEnumerable, Func`4 sleepDurationProvider, Boolean continueOnCapturedContext) at Polly.AsyncPolicy`1.ExecuteAsync(Func`3 action, Context context, CancellationToken cancellationToken, Boolean continueOnCapturedContext) at OutSystems.Publish.Connectors.KubernetesClients.K8sFacade.GetTenantCustomResource(String tenantId) in /src/src/OutSystems.Publish.Connectors/KubernetesClients/K8sFacade.cs:line 123- Similar to case # 3042682 (https://outsystemsrd.atlassian.net/browse/RDINC-27870)
- We can also see these similar errors as seen in the previous Jira case:- This case- ![](https://supportoutsystems.zendesk.com/attachments/token/Ua6qucTk7uRQKymzM47umtPcu/?name=image.png)- The other case- ![](https://supportoutsystems.zendesk.com/attachments/token/rxYX5pz9oSLTANLGrY8UMm0P7/?name=image.png)
- If that is the case, it was discovered a possible issue with the model, but there was not too much information for me to know which is the faulty element here...- The issue started from 4329 to 4330- Comparing these two revisions, we can see several new action and changes in a few actions as well:- ![](https://supportoutsystems.zendesk.com/attachments/token/8EtsNxJab9uCWNTNRkbYKbZPe/?name=image.png)- If this is related to the expression not being rebinded, something may have been going wrong with the model, as mentioned in the previous case, but this is something that I cannot pinpoint at this moment, and this is why the case is being escalated, as always, thank you for the assistance.Reason for the priority.- It is clear that the team was able to publish again based on the publications list (as seen in the other Jira case, if the reason is the same is not 100% certain that it will not happen again), however, we have not received any updates from their side about it to lower the priority at discretion, so we will keep the priority for now until we get an update from their side.... just proceduresReason for opening a new case- If this ends up being the same problem, we could then close this escalation and proceed with the wide incident motion to avoid new cases from being created :). But for now, I thought that the best move was to create a new case since is not certain if the cause is the same, and which action in this case, even though similar symptoms were found, sorry for any inconvenience...**TECH DATA OR ANY OTHER RELEVANT INFO**
**OutSystems Developer Cloud Platform **License
Ring: ea
Tenant Id: dc3a3772-693b-4b6a-aa61-5fea3976eeb3
Tenant Prefix: odc-portal-localdev
Region: us-east-1Omls attached:- connections-rev4329.oml
- connections-rev4330.oml_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 Retrospective### Details
**Ring:** ea
**System-wide impact:**&nbsp; No
**Tenant ID:** dc3a3772-693b-4b6a-aa61-5fea3976eeb3
**Tenant Prefix:** odc-portal-localdev
**Routing Error Code:** OS-BLD-COMP
**Product Area:** -
### Impact:
Customer was unable to publish his app.
### Investigation and troubleshooting findings:
We do not support record attributes of type 'Object', but there is no model validation that prevents publishing.
### Resolution:
Split local variable of type record into multiple variables, each one representing each of the record's attributes.
## Tasks performed during incident resolution:
- 
The known issue was quickly identified by R&amp;D and a workaround was provided to the customer.

## Executive Summary
On July 31st, at 11:49 PM, a customer submitted a support case reporting that he was unable to publish his app in the ODC Studio. The known issue was quickly identified by R&amp;D and a workaround was provided to the customer at about 12:42 AM.

This situation represented a downtime of about 57 minutes.

From a technical perspective the problem was caused due to a local variable, of record type, that contained an attribute of Object type which is not allowed in OutSystems compiler.

As a consequence of the incident, we have determined to look into the issue in the following bug:

- 
[https://outsystemsrd.atlassian.net/browse/RDMST-2505#icft=RDMST-2505](https://outsystemsrd.atlassian.net/browse/RDMST-2505#icft=RDMST-2505)  

[Guidelines](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4144496679/Incident+Retrospectives+-+Playbook#STEP-3---Write-the-Executive-Summary)
## Root Causes 
- 
[https://outsystemsrd.atlassian.net/browse/RDMST-2505#icft=RDMST-2505](https://outsystemsrd.atlassian.net/browse/RDMST-2505#icft=RDMST-2505) 

[Guidelines](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4144496679/Incident+Retrospectives+-+Playbook#STEP-1---Perform-the-Root-Cause-Analysis)

If the customer needs formal RCA, please fill out the following field with the document URL

[Please follow these instructions and place the RCA URL in the field below.](https://docs.google.com/document/d/13rXmBsOJh73nV2D6Z17SIBGBu2HOTWty5ddsvU000JM/edit#heading=h.bqxasxszr5q)

RCA URL

&lt;Place the URL of the customer RCA here if you have created one&gt;
## ⌛ Timeline
[View on Rootly](https://rootly.com/account/incidents/785-odc-studio-unable-to-publish-my-connections-app)

**Date**

**Source**

**User**

**Event**

July 31 11:49 PM WEST

web

Rootly

created an alert via

July 31 11:49 PM WEST

web

Rootly

Rootly created this incident

July 31 11:49 PM WEST

web

Rootly

In triage date has been set to July 31 11:49 PM WEST

July 31 11:49 PM WEST

web

Rootly

[Slack Channel](https://slack.com/app_redirect?channel=C07EK0BK7QF&amp;team=T041063TZ) has been created

July 31 11:49 PM WEST

web

Rootly

Ring: ea
System-wide impact:  
Tenant ID: dc3a3772-693b-4b6a-aa61-5fea3976eeb3
Tenant Prefix: odc-portal-localdev
Routing Error Code: OS-BLD-COMP
Product Area: -

July 31 11:50 PM WEST

web

Rootly

[PagerDuty Incident](https://outsystems.pagerduty.com/incidents/Q36WSMEWIBEJJ5) has been created.

📧 Notified Kishore Kamath by email.

&nbsp;&nbsp;

📲 Notified Kishore Kamath by push notification.  (via iPhone)

July 31 11:50 PM WEST

web

Rootly

Kishore Kamath has been assigned as Engineer

July 31 11:52 PM WEST

web

Kishore Kamath

Incident has been started

July 31 11:52 PM WEST

web

Rootly

Pagerduty Integrations acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q36WSMEWIBEJJ5)

July 31 11:57 PM WEST

slack

Kishore Kamath

Going through the update.. this seems to be for
Ring: ea
System-wide impact:
Tenant ID: dc3a3772-693b-4b6a-aa61-5fea3976eeb3
Tenant Prefix: odc-portal-localdev
Routing Error Code: OS-BLD-COMP

August 1 12:09 AM WEST

slack

Kishore Kamath

This is in EA and its affecting the one customer. I checked the SLOs for 1CPs for us-east-1 EA and it does not seem to be any system-wide impact.

August 1 12:22 AM WEST

slack

Kishore Kamath

@Jo&atilde;o Lu&iacute;s Almeida (lja) are you taking over this incident? It seems to be related to JIRA mentioned earlier [https://outsystemsrd.atlassian.net/browse/RDINC-21465](https://outsystemsrd.atlassian.net/browse/RDINC-21465)

August 1 12:22 AM WEST

slack

Jo&atilde;o Lu&iacute;s Almeida (lja)

Yes, I'm looking into it

August 1 12:43 AM WEST

web

Rootly

Incident has been mitigated

August 1  6:19 AM WEST

web

Rootly

ZenDesk Event Type has been set: solved

August 1  6:19 AM WEST

web

Rootly

The Global Support team marked this incident as closed in ZenDesk.

August 2 12:03 PM WEST

web

Nuno Rego

Nuno Rego has been assigned as Engineer

August 2 12:07 PM WEST

web

Nuno Rego

Incident has been resolved

August 2 12:07 PM WEST

web

Nuno Rego

System-wide impact has been set: No

August 2 12:07 PM WEST

web

Nuno Rego

Impact has been set: Customer was unable to publish his app.

August 2 12:07 PM WEST

web

Nuno Rego

Investigation and troubleshooting findings has been set: We do not support record attributes of type 'Object', but there is no model validation that prevents publishing.

August 2 12:07 PM WEST

web

Nuno Rego

Resolution has been set: Split local variable of type record into multiple variables, each one representing each of the record's attributes.