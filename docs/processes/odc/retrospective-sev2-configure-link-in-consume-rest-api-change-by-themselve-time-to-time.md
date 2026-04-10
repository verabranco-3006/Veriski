---
title: Retrospective-SEV2-Configure link in Consume REST API change by themselve (time to time)
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4357161441/Retrospective-SEV2-Configure+link+in+Consume+REST+API+change+by+themselve+time+to+time
confluence_space: RKB
confluence_page_id: 4357161441
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV2-Configure link in Consume REST API change by themselve (time to time)

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV2

Teams:&nbsp;trueBlueBackend Runtime&nbsp;trueBlueSre

Types:&nbsp;trueBlueCustomer Escalated
#### 🕐 Timestamps
Started At:&nbsp;trueBlueAugust 12 10:59 AM WEST

Mitigated At:&nbsp;trueYellowAugust 13  4:34 PM WEST

Resolved At:&nbsp;trueGreenAugust 13  4:34 PM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/865-configure-link-in-consume-rest-api-change-by-themselve-time-to-time)
[Pagerduty incident](https://outsystems.pagerduty.com/incidents/Q1QCTO5FJXK58J)

[Slack channel](https://slack.com/app_redirect?channel=C07GEEX7Z3P&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3047283)

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

Rui Garcia
#### Summary
----------------------------------------------**R&amp;D ESCALATION FORM****ISSUE DESCRIPTION AND HOW TO REPRODUCE**
The customer has the application PL Smart Move, which uses an internal library, so the end users can perform payments. To use this library it consumes a REST.
Sometimes the request fails and there is no reason for this to happen because many of the times the users are able to perform the payments successfully.![](https://supportoutsystems.zendesk.com/attachments/token/gojx6S8DaCqPHeSVqSZizoO4a/?name=image.png)![](https://supportoutsystems.zendesk.com/attachments/token/gy7OO04fM2EiWB0BCIfrRApMM/?name=image.png)The customer is not able to replicate it, it happens randomly.**IMPACT ON THE CUSTOMER**
Brief description of the impact on the customer/development team/other, including:
- development and production
- intermittent, but it is happening almost every day![](https://supportoutsystems.zendesk.com/attachments/token/x7Gf4ASDMmmk9rdU0uR2pn09a/?name=image.png)
- End users cannot pay for the orders.
- development and debug sessions cannot be completed with success.**TROUBLESHOOTING STEPS &amp; WORKAROUND**
- on the production environment if we see the URL being used it is the base URL, but the customer has set up a customer URL when the REST is being consumed.![](https://supportoutsystems.zendesk.com/attachments/token/Y63MLkIZW2PiIVzqZIrHVWrEF/?name=image.png)![](https://supportoutsystems.zendesk.com/attachments/token/pq8EZfEFg2DzCeHf7HNT11Jgh/?name=image.png)
in dev, the URL is the base URL and looking at the trace dashboard the URL is correct.![](https://supportoutsystems.zendesk.com/attachments/token/4erShmhLR9Uz0xptXm3ejSwfj/?name=image.png)![](https://supportoutsystems.zendesk.com/attachments/token/F4QQ9woRlETuJ3riSf9k20BGy/?name=image.png)- What workaround was tried so far, if any, and how did they impact the reported behavior? none, we have no workaround to provide
- Was this case discussed previously with anyone from R&amp;D? If so with whom and which R&amp;D team? - no
- If it is related, or there is a possibility of being related, to an already existing RDINC, please specify it.  - I searched but I did not find anything related.**TECH DATA OR ANY OTHER RELEVANT INFO**
- Tenant ID or Activation Code where the problem is occurring.
Ring: ga
Tenant Id: 67ce4b7d-df56-4e41-b6ff-6fbc1f1fd819
AC: PTD.PAW.ORO.S6C.AA2.TGY.XVA.GOU
production and development- All technical files or data, including OMLs.
- Error stacks, screenshots, or any other files like error logs or traces.BackendRuntime | OS-BERT-00000&nbsp; PL Smart move [Erro]&nbsp; 404 Not FoundssPLSmartmove.ScreenServices.PLSmartmove_Booking_VerifyBooking_Controller.ActionVerifyBookingDetail (PLSmartmove)at ssmPayIntegration.CcCreditCardPayment_HeadersOnBefore.ActionPostPaymentOrder3(IRequestContext requestContext, ICcCreditCardPayment_HeadersOnBeforeCallbacks _callbacks, ST_e45dfe034b9ca7384240eba6f18208e8Structure inParamRequest, CancellationToken cancellationToken)at ssmPayIntegration.Actions.ActionPaymentOrder_Create(IRequestContext requestContext, ST_e45dfe034b9ca7384240eba6f18208e8Structure inParamRequest, CancellationToken cancellationToken)at ssPLSmartmove.RsseSpacemPayIntegration.MssPaymentOrder_Create(IRequestContext requestContext, IRecord inParamRequest, CancellationToken cancellationToken)at ssPLSmartmove.Actions.ActionPaymentOrder_Create(IRequestContext requestContext, ST_e45dfe034b9ca7384240eba6f18208e8Structure inParamRequest, CancellationToken cancellationToken)at ssPLSmartmove.Actions.ActionMPayPayment(IRequestContext requestContext, String inParamOrder_Id, Decimal inParamTotalAmount, CancellationToken cancellationToken)at ssPLSmartmove.Actions.ActionVerifyBookingDetail(IRequestContext requestContext, Int64 inParamCar_Id, DateTime inParamStart_DateTime, DateTime inParamEnd_DateTime, String inParamDistance_Package, Decimal inParamTotal_Price, Decimal inParamDiscount, String inParamPrice_Type, String inParamPromotion_Code, Boolean inParamIsReqToCorp, String inParamTrip_Type, String inParamReturn_Station, String inParamCorpAbbrev, Decimal inParamDistancetocar, String inParamDestination, String inParamRerturn_Station_ID, String inParamStart_Station, String inParamStart_Station_ID, CancellationToken cancellationToken)at ssPLSmartmove.ScreenServices.PLSmartmove_Booking_VerifyBooking_Controller.b__15_0(String screenName, JObject screenModel, JObject inputParameters, JObject clientVariables, CancellationToken cancellationToken)at OutSystems.RESTService.Runtime.Core.Controllers.ScreenServices.ScreenServicesApiController.InnerEndpointAsync(String apiVersionHash, EndpointAsyncImplementationDelegate implementationAsync, ResponseVersionInfo responseVersionInfo, ServiceRequest requestPayload, CancellationToken cancellationToken)at OutSystems.RESTService.Runtime.Core.Controllers.ScreenServices.ScreenServicesApiController.EndpointAsync(Stream input, String apiVersionHash, EndpointAsyncImplementationDelegate implementationAsync, CancellationToken cancellationToken)2024-08-09 03:26:51:185trace id:` 4eb2c8a9c0ba5a770fa7026413ebacc3`general troubleshooting: https://outsystems.grafana.net/d/cdeqzn1jj77cwe/general-troubleshooting?var-filter=OS-BERT-00000&amp;var-exclude=&amp;var-ring=ga&amp;var-tenant=67ce4b7d-df56-4e41-b6ff-6fbc1f1fd819&amp;var-cluster=$__all&amp;var-severity=$__all&amp;var-runtime=$__all&amp;var-traceDuration=$__all&amp;var-region=ap-southeast-1&amp;var-environment=d2e02365-7765-4a97-b050-7d73bb4d3a08&amp;var-regionShort=ga-ap-se-1-01&amp;var-tenant_prefix=phatra-leasing&amp;var-application=3ecfc249-0777-4bd2-98ee-952e16b94084&amp;var-cluster_old=$__all&amp;var-module_name=PLSmartmove&amp;from=now-7d&amp;to=now&amp;timezone=browsertrace dev: https://outsystems.grafana.net/d/lj_Cstg4k/gen-search-trace?var-traceid=4eb2c8a9c0ba5a770fa7026413ebacc3
trace prod: https://outsystems.grafana.net/d/lj_Cstg4k/gen-search-trace?var-traceid=4eb2c8a9c0ba5a770fa7026413ebacc3&amp;from=now-30d&amp;to=now_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_Attachment(s):
mPay Integration.oml - https://supportoutsystems.zendesk.com/attachments/token/mE5y2M4TXwk4YDop737vJCPg9/?name=mPay+Integration.omlPL Smart move.oml - https://supportoutsystems.zendesk.com/attachments/token/OzgcFZVv5oualI5kdgjFzCFPt/?name=PL+Smart+move.oml
## 📝 RetrospectiveinfoDetails
**Ring:** ga
**System-wide impact:**&nbsp; 
**Tenant ID:** 67ce4b7d-df56-4e41-b6ff-6fbc1f1fd819
**Tenant Prefix:** phatra-leasing
**Routing Error Code:** OS-BERT
**Product Area:** -
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/865-configure-link-in-consume-rest-api-change-by-themselve-time-to-time)

**Date**

**Source**

**User**

**Event**
August 12 10:48 AM WESTwebRootly
created an alert via
August 12 10:48 AM WESTwebRootly
Rootly created this incident
August 12 10:48 AM WESTwebRootly
In triage date has been set to August 12 10:48 AM WEST
August 12 10:49 AM WESTwebRootly[Slack Channel](https://slack.com/app_redirect?channel=C07GEEX7Z3P&amp;team=T041063TZ) has been createdAugust 12 10:49 AM WESTwebRootly
Ring: ga
System-wide impact:  
Tenant ID: 67ce4b7d-df56-4e41-b6ff-6fbc1f1fd819
Tenant Prefix: phatra-leasing
Routing Error Code: OS-BERT
Product Area: -
August 12 10:49 AM WESTwebRootly[PagerDuty Incident](https://outsystems.pagerduty.com/incidents/Q1QCTO5FJXK58J) has been created.
📲 Notified Joel Carvalho by push notification.  (via Android)August 12 10:49 AM WESTwebRootlyJoel Filipe Carvalho has been assigned as EngineerAugust 12 10:58 AM WESTwebRootly
Filipe Seixeira acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q1QCTO5FJXK58J). (via Slack)
August 12 10:59 AM WESTwebFilipe Seixeira
Incident has been started
August 12 10:59 AM WESTwebRootly
Pagerduty Integrations acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q1QCTO5FJXK58J). (via Slack)
August 12 11:09 AM WESTslackFilipe Seixeira
As described by GS in the incident, the requests failures are not happening in a sustained way.
No visible impact on the system-wide-slos
August 12 11:14 AM WESTwebFilipe SeixeiraRui Garcia has been assigned as EngineerAugust 12 11:49 AM WESTwebRootly
This incident was instantiated in Jira: RDINC-28411. Please work the incident using Rootly
August 13  4:34 PM WESTwebRootly
The Global Support team marked this incident as closed in ZenDesk.
August 13  4:34 PM WESTwebRootly
Incident has been resolved
August 13  4:34 PM WESTwebRootlyZenDesk Event Type has been set: solved