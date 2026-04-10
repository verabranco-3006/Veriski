---
title: Retrospective-SEV2-Partner Evoke Technologies cannot open ODC support case and is blocked from publishing a prospect demo
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4329930932/Retrospective-SEV2-Partner+Evoke+Technologies+cannot+open+ODC+support+case+and+is+blocked+from+publishing+a+prospect+demo
confluence_space: RKB
confluence_page_id: 4329930932
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV2-Partner Evoke Technologies cannot open ODC support case and is blocked from publishing a prospect demo

## 📘 Overview
Author:&nbsp;Rootlytrue

Severity:&nbsp;SEV2Redtrue

Teams:&nbsp;Ide GroupBluetrue
#### 🕐 Timestamps
Started At:&nbsp;July 30  8:07 PM WESTBluetrue

Mitigated At:&nbsp;July 31 10:12 AM WESTYellowtrue

Resolved At:&nbsp;August 2 11:15 AM WESTGreentrue
#### 🔗 Links
[Incident Page](https://rootly.com/account/incidents/780-partner-evoke-technologies-cannot-open-odc-support-case-and-is-blocked-from-publishing-a-prospect-demo)

[Pagerduty incident](https://outsystems.pagerduty.com/incidents/Q1HNFFICA3Z3RG)

[Slack channel](https://slack.com/app_redirect?channel=C07FEMQLHQ8&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3042682)

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

Nuno Rego

**Commander**

C&eacute;sar Afonso
#### Summary
----------------------------------------------**ISSUE DESCRIPTION AND HOW TO REPRODUCE**- Evoke customer is having some issues trying to publish their application which is intended to be shown to a prospective customer tomorrow July 31st
- When they try to publish their application they constantly get the known error codes: OS-BLD-COMP-50000 and OS-DPL-50205
- In the last occurrences, we can see that they were able to publish revision 1006, and after revision 1007, they have been getting the mentioned errors until now.
- Similar errors occurred on other revisions (based on the 1CP logs) but they were eventually able to publish. now they are stuck and the deadline is on top**IMPACT ON THE CUSTOMER**- This is happening in development and this affects their capabilities to have the application as expected to do the demonstration with their prospect
- ![](https://supportoutsystems.zendesk.com/attachments/token/dOWBT8J627acwiy6V2LLcESjl/?name=image.png)**TROUBLESHOOTING STEPS &amp; WORKAROUND**- In the logs, we can see several errors:
- Starting with the publish dashboard: https://outsystems.grafana.net/d/cdgg5feb0g6bkd/publish-deploy-mabs?var-ring=ea&amp;var-tenant=13376ba6-ba03-427a-a99a-de5a109b190e&amp;var-mobile_platform=$__all&amp;var-region=$__all&amp;var-application=$__all&amp;var-stamp=$__all&amp;from=2024-07-30T05:10:16.585Z&amp;to=2024-07-30T17:10:16.585Z&amp;timezone=Asia%2FSingapore
- We can see the error code and the reason OS-DPL-50205- Navigating to the reason, we can find the following error messages in multiple occasions:Failed to retrieve Tenant CR&nbsp;Operation returned an invalid status code 'NotFound', response body {&quot;kind&quot;:&quot;Status&quot;,&quot;apiVersion&quot;:&quot;v1&quot;,&quot;metadata&quot;:{},&quot;status&quot;:&quot;Failure&quot;,&quot;message&quot;:&quot;tenants.platform.outsystemscloud.com \&quot;dc3a3772-693b-4b6a-aa61-5fea3976eeb3\&quot; not found&quot;,&quot;reason&quot;:&quot;NotFound&quot;,&quot;details&quot;:{&quot;name&quot;:&quot;dc3a3772-693b-4b6a-aa61-5fea3976eeb3&quot;,&quot;group&quot;:&quot;platform.outsystemscloud.com&quot;,&quot;kind&quot;:&quot;tenants&quot;},&quot;code&quot;:404}&nbsp;StackTrace: we can see some kubernetes actions -&gt;&nbsp; at k8s.Kubernetes.SendRequestRaw(String requestContent, HttpRequestMessage httpRequest, CancellationToken cancellationToken)&nbsp; at k8s.AbstractKubernetes.ICustomObjectsOperations_GetClusterCustomObjectWithHttpMessagesAsync[T](String group, String version, String plural, String name, IReadOnlyDictionary`2 customHeaders, CancellationToken cancellationToken)&nbsp; at k8s.AbstractKubernetes.k8s.ICustomObjectsOperations.GetClusterCustomObjectWithHttpMessagesAsync[T](String group, String version, String plural, String name, IReadOnlyDictionary`2 customHeaders, CancellationToken cancellationToken)&nbsp; at OutSystems.Publish.Connectors.KubernetesClients.K8sFacade.&lt;&gt;c__DisplayClass21_0.&lt;&lt;GetTenantCustomResource&gt;b__0&gt;d.MoveNext() in /src/src/OutSystems.Publish.Connectors/KubernetesClients/K8sFacade.cs:line 124&nbsp;--- End of stack trace from previous location ---&nbsp; at Polly.Retry.AsyncRetryEngine.ImplementationAsync[TResult](Func`3 action, Context context, CancellationToken cancellationToken, ExceptionPredicates shouldRetryExceptionPredicates, ResultPredicates`1 shouldRetryResultPredicates, Func`5 onRetryAsync, Int32 permittedRetryCount, IEnumerable`1 sleepDurationsEnumerable, Func`4 sleepDurationProvider, Boolean continueOnCapturedContext)&nbsp; at Polly.AsyncPolicy`1.ExecuteAsync(Func`3 action, Context context, CancellationToken cancellationToken, Boolean continueOnCapturedContext)&nbsp; at OutSystems.Publish.Connectors.KubernetesClients.K8sFacade.GetTenantCustomResource(String tenantId) in /src/src/OutSystems.Publish.Connectors/KubernetesClients/K8sFacade.cs:line 123- We can also see some errors in the traces, making references to Nats service and many other processes to list here
- ![](https://supportoutsystems.zendesk.com/attachments/token/nErgMJvrYGDRFEupkSs7afRGv/?name=image.png)
- ![](https://supportoutsystems.zendesk.com/attachments/token/qWCuYbcSCPRHQGMkqVuwZLNsv/?name=image.png)
**TECH DATA OR ANY OTHER RELEVANT INFO**- **ODC Partner Demo **License- Ring: ea- Tenant Id:**ODC Partner Demo **License- Ring: ea- Tenant Id: 13376ba6-ba03-427a-a99a-de5a109b190e- Tenant Prefix: evoke- Region: ap-southeast-1- SWA.527.29H.6SN.TKS.EI4.2SV.64R
**Logs:**- Reason Logs - 1CP logs https://outsystems.grafana.net/d/A1YJOsa7z/1cp-logs?orgId=1&amp;var-ring=ea&amp;var-level=Warning&amp;var-level=Error&amp;var-service=Publish.Service&amp;var-traceId=&amp;from=1722316216585&amp;to=1722359416585]
- Trace - accessed from the publish dashboard: [https://outsystems.grafana.net/explore?left=%7B%22datasource%22%3A%22grafanacloud-outsystemstest-traces%22%2C%22queries%22%3A%5B%7B%22query%22%3A%2244e0a8ca2e7d520b1be09abc78553db2%22%2C%22queryType%22%3A%22traceql%22%7D%5D%7D]
**Omls** -&gt; (~15 MB each one) I will attach to the Jira case- Currently published revision (1006): Evoke University Web App rev1006.oml
- The one that started to fail afterward (1007): Evoke University Web App rev1007.oml
- Latest revision (1017, they have been doing some changes but the issue persists): Evoke University Web App latest rev1017.oml_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 Retrospective### Details
**Ring:** -
**System-wide impact:**&nbsp; No
**Tenant ID:** N/A
**Tenant Prefix:** N/A
**Routing Error Code:** N/A
**Product Area:** Phoenix::ODC Studio::Publish
### Impact:
Failure to publish
### Investigation and troubleshooting findings:
A specific expression in the customer's model is experience 'rebind' failures.
### Resolution:
Recreate the client action containing the faulty expression
## Tasks performed during incident resolution:
- 
Analyzed publish data;

- 
Identified model elements that were leading to the publish error;

- 
Provided a workaround to the customer.

## Executive Summary
On July 30th, 2024 at 7:45 pm (UTC), a partner submitted, on behalf of a customer, a support case reporting issues with the publish operation in the IDE. Investigation concluded that the problem was do due to a corrupt model. At about 10 pm (UTC) R&amp;D provided a workaround that resulted in unblocked the publish operation for the customer.

This situation represented a downtime of about 2 hours.

From a technical perspective we&rsquo;ve concluded that a given operation led to a failure in rebinding some expression elements, which then could not be handled by the compiler as they did not follow the contract set by the OutSystems metamodel.

As such, we have decided to investigate the root cause further in the following issue (that will be prioritized accordingly):

- 
RDMST-3085ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

[Guidelines](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4144496679/Incident+Retrospectives+-+Playbook#STEP-3---Write-the-Executive-Summary)
## Root Causes 
- 
RDMST-3085ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

[Guidelines](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4144496679/Incident+Retrospectives+-+Playbook#STEP-1---Perform-the-Root-Cause-Analysis)
## ⌛ Timeline
[View on Rootly](https://rootly.com/account/incidents/780-partner-evoke-technologies-cannot-open-odc-support-case-and-is-blocked-from-publishing-a-prospect-demo)

**Date**

**Source**

**User**

**Event**

July 30  7:44 PM WEST

web

Rootly

created an alert via

July 30  7:44 PM WEST

web

Rootly

Rootly created this incident

July 30  7:44 PM WEST

web

Rootly

In triage date has been set to July 30  7:44 PM WEST

July 30  7:45 PM WEST

web

Rootly

[Slack Channel](https://slack.com/app_redirect?channel=C07FEMQLHQ8&amp;team=T041063TZ) has been created

July 30  7:45 PM WEST

web

Rootly

Ring: -
System-wide impact:  
Tenant ID: N/A
Tenant Prefix: N/A
Routing Error Code: N/A
Product Area: Phoenix::ODC Studio::Publish

July 30  7:45 PM WEST

web

Rootly

[PagerDuty Incident](https://outsystems.pagerduty.com/incidents/Q1HNFFICA3Z3RG) has been created.

📧 Notified Gustavo Morais by email.

&nbsp;&nbsp;

📲 Notified Gustavo Morais by push notification.  (via Android)

July 30  7:45 PM WEST

web

Rootly

Gustavo Morais has been assigned as Engineer

July 30  7:57 PM WEST

web

Rootly

Gustavo Morais acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q1HNFFICA3Z3RG). (via Website)

July 30  8:07 PM WEST

web

Sam Audu

Incident has been started

July 30  8:07 PM WEST

web

Rootly

Pagerduty Integrations acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q1HNFFICA3Z3RG). (via Website)

July 30  8:26 PM WEST

web

Sam Audu

Carlos Freitas has been assigned as Engineer

July 30  8:29 PM WEST

slack

Sam Audu

Slack upload

[image.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDIwNjg3LCJwdXIiOiJibG9iX2lkIn19--09ea2745125fb4976a56561431085a3c1e83b3a5/image.png)

July 30  9:19 PM WEST

web

Carlos Freitas

Jo&atilde;o Lu&iacute;s Almeida has been assigned as Engineer

July 31  8:56 AM WEST

web

Nuno Bento

Teams has been added: [BuildServices](/account/teams/buildservices/status)

July 31  8:56 AM WEST

web

Nuno Bento

Teams has been removed: [IDEGroup](/account/teams/idegroup/status)

July 31 10:12 AM WEST

web

Rootly

Incident has been mitigated

July 31 12:50 PM WEST

web

Jo&atilde;o Lu&iacute;s Almeida

Teams has been added: [IDEGroup](/account/teams/idegroup/status)

July 31 12:50 PM WEST

web

Jo&atilde;o Lu&iacute;s Almeida

Teams has been removed: [BuildServices](/account/teams/buildservices/status)

July 31 12:50 PM WEST

web

Jo&atilde;o Lu&iacute;s Almeida

Gustavo Morais has been assigned as Engineer

July 31  1:46 PM WEST

web

Nuno Rego

Nuno Rego has been assigned as Engineer

July 31  1:46 PM WEST

web

Nuno Rego

C&eacute;sar Afonso has been assigned as Commander

August 2 11:13 AM WEST

web

Nuno Rego

Send ZenDesk private comment has been set: Hello team,Glad to know the workaround has unblocked the customer. Regarding the root cause: we've concluded that it was due to a failure in a 'rebind' operation in a specific expression. We've created the issue RDMST-3085 to look into it further and we'll prioritize it accordingly.As such, we'll mark this incident to solved. Thank you for your help and patience.Kind regards,
Nuno Rego

August 2 11:13 AM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:
Hello team,Glad to know the workaround has unblocked the customer. Regarding the root cause: we've concluded that it was due to a failure in a 'rebind' operation in a specific expression. We've created the issue RDMST-3085 to look into it further and we'll prioritize it accordingly.As such, we'll mark this incident to solved. Thank you for your help and patience.Kind regards,
Nuno Rego

August 2 11:13 AM WEST

web

Rootly

Send ZenDesk private comment has been unset

August 2 11:13 AM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:

August 2 11:15 AM WEST

web

Nuno Rego

Incident has been resolved

August 2 11:15 AM WEST

web

Nuno Rego

System-wide impact has been set: No

August 2 11:15 AM WEST

web

Nuno Rego

Impact has been set: Failure to publish

August 2 11:15 AM WEST

web

Nuno Rego

Investigation and troubleshooting findings has been set: A specific expression in the customer's model is experience 'rebind' failures.

August 2 11:15 AM WEST

web

Nuno Rego

Resolution has been set: Recreate the client action containing the faulty expression