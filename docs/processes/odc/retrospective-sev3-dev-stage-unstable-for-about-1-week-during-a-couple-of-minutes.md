---
title: Retrospective-SEV3-Dev stage unstable for about 1 week during a couple of minutes
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4335468545/Retrospective-SEV3-Dev+stage+unstable+for+about+1+week+during+a+couple+of+minutes
confluence_space: RKB
confluence_page_id: 4335468545
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV3-Dev stage unstable for about 1 week during a couple of minutes

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV3

Teams:&nbsp;trueBlueBackend Runtime
#### 🕐 Timestamps
Started At:&nbsp;trueBlueAugust 5  1:56 PM WEST

Mitigated At:&nbsp;trueYellowAugust 5  1:56 PM WEST

Resolved At:&nbsp;trueGreenAugust 5  1:56 PM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/596-dev-stage-unstable-for-about-1-week-during-a-couple-of-minutes)
[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3019135)

#### Summary
----------------------------------------------**CONSIDERATIONS BEFORE PERFORMING THE ESCALATION TO R&amp;D (MANDATORY)**
None of the below points should be overlooked. Failure to do so may imply unnecessary effort.* * *
Ensure the ticket has been **categorized**, otherwise, the R&amp;D escalation will go unnoticed and not be worked on!**1.** For **Incidents**, the **IMAX** was consulted **beforehand** on which:- No incident models were found for the reported symptoms **OR**
- The incident model did not solve the issue **OR**
- The next step indicated in the Incident Model is an escalation to R&amp;D.
**2.** For **Questions**, the ChatODC on the **Slack channel** didn't return an acceptable answer.
**3.** Any other requests that explicitly indicate an R&amp;D escalation is needed.
**4**. **Incident impact assessment** was based on the **prioritization scoring matrix**.* * ***R&amp;D ESCALATION FORM**
Section comments can be removed for R&amp;D easier interpretation.**ISSUE DESCRIPTION AND HOW TO REPRODUCE**- In DEV they get a &quot;No healthy upstream&quot; message on any application.
- They noticed this every day around the same time around 3:45 to 4:00 PM West (UTC +1)
- When it occurs after 5 minutes it is back to normal.**IMPACT ON THE CUSTOMER**- Normal - This is impacting testing in the development environment, it is slowing the ability to complete dev testing.- Final sprint Monday, June 10th in prep for a July and August go-live of new features.**TROUBLESHOOTING STEPS &amp; WORKAROUND**- We found the error message:OS-BERT-60407 - [500] Could not execute the specified command: HTTP 503: Service Unavailable no healthy upstreamat System.Data.CData.ApachePhoenix.ApachePhoenixCommand.ExecuteDataReader(CommandBehavior behavior)&nbsp; at System.Data.CData.ApachePhoenix.ApachePhoenixCommand.ExecuteReader(CommandBehavior behavior)&nbsp; at OutSystems.DatabaseProvider.QueryEngine.Driver.QueryEngineCommand.ExecuteReader(CommandBehavior behavior)&nbsp; at OutSystems.DatabaseProvider.QueryEngine.Driver.QueryEngineCommand.ExecuteDbDataReader(CommandBehavior behavior)&nbsp; at OutSystems.DatabaseProvider.QueryEngine.Driver.QueryEngineCommand.&lt;&gt;c__DisplayClass59_0.&lt;ExecuteDbDataReaderAsync&gt;b__0()&nbsp; at System.Threading.Tasks.Task`1.InnerInvoke()&nbsp; at System.Threading.ExecutionContext.RunInternal(ExecutionContext executionContext, ContextCallback callback, Object state)&nbsp;--- End of stack trace from previous location ---&nbsp; at System.Threading.ExecutionContext.RunInternal(ExecutionContext executionContext, ContextCallback callback, Object state)&nbsp; at System.Threading.Tasks.Task.ExecuteWithThreadLocal(Task&amp; currentTaskSlot, Thread threadPoolThread)&nbsp;--- End of stack trace from previous location ---&nbsp; at OutSystems.HubEdition.DatabaseAbstractionLayer.Internal.Db.Implementations.Command.ExecuteReaderAsync(String description, Boolean isApplication, Boolean skipLog, Boolean applyTransformationsToParameters, CancellationToken cancellationToken)&nbsp; at OutSystems.HubEdition.DatabaseAbstractionLayer.Internal.Db.Implementations.Command.ExecuteReaderAsync(String description, Boolean isApplication, Boolean skipLog, Boolean applyTransformationsToParameters, CancellationToken cancellationToken)&nbsp; at OutSystems.HubEdition.DatabaseAbstractionLayer.Internal.Db.Implementations.Command.ExecuteReaderAsync(String description, Boolean isApplication, Boolean skipLog, Boolean applyTransformationsToParameters, CancellationToken cancellationToken)&nbsp; at OutSystems.HubEdition.DatabaseAbstractionLayer.Internal.Db.Implementations.Command.ExecuteReaderAsync(String description, Boolean isApplication, Boolean skipLog, Boolean applyTransformationsToParameters, CancellationToken cancellationToken)&nbsp; at OutSystems.Internal.Db.DatabaseAccessProviderExtensions.ExecuteQueryAsync[TDatabaseServices,T](IDatabaseAccessProvider`1 provider, DbCommand cmd, GenericRecordList`1 rl, String description, Boolean transformParameters, Boolean skipLog, CancellationToken cancellationToken)&nbsp; at OutSystems.Internal.Db.DatabaseAccessProviderExtensions.ExecuteQueryAsync[TDatabaseServices,T](IDatabaseAccessProvider`1 provider, DbCommand cmd, GenericRecordList`1 rl, String description, CancellationToken cancellationToken)&nbsp; at ssPortalExposureAdjustment.ScreenServices.PortalExposureAdjustment_MainFlow_ExposureAdjustment_ScreenModel.datasetGetExpoAdjProcessSummary(IRequestContext requestContext, Int32 maxRecords, IterationMultiplicity multiplicity, Int32 qpinVIEW_OS_EXPO_ADJ_SUMMARY_AssignedToContactId, String qpstVIEW_OS_EXPO_ADJ_SUMMARY_MemberId, String qpstVIEW_OS_EXPO_ADJ_SUMMARY_PolicyYear, Int32 qpinCurrCXPUserId, Boolean qpboEmpty, String qpstVIEW_OS_EXPO_ADJ_SUMMARY_ReportingUnitFlag, String qpstVIEW_OS_EXPO_ADJ_SUMMARY_ReportingUnitRequiredFlag, String qpstVIEW_OS_EXPO_ADJ_SUMMARY_MemberType, Boolean qpboIsCompleted, Boolean qpboIsInProgress, Boolean qpboIsNotStarted, Boolean qpboIsProcessing, Boolean qpboIsRevisionsRequested, Boolean qpboIsSubmitted, Boolean qpboIsDevModeOn, String qpstTableSort, CancellationToken cancellationToken)&nbsp; at ssPortalExposureAdjustment.ScreenServices.PortalExposureAdjustment_MainFlow_ExposureAdjustment_ScreenModel.datasetGetExpoAdjProcessSummary(IRequestContext requestContext, Int32 maxRecords, IterationMultiplicity multiplicity, Int32 qpinVIEW_OS_EXPO_ADJ_SUMMARY_AssignedToContactId, String qpstVIEW_OS_EXPO_ADJ_SUMMARY_MemberId, String qpstVIEW_OS_EXPO_ADJ_SUMMARY_PolicyYear, Int32 qpinCurrCXPUserId, Boolean qpboEmpty, String qpstVIEW_OS_EXPO_ADJ_SUMMARY_ReportingUnitFlag, String qpstVIEW_OS_EXPO_ADJ_SUMMARY_ReportingUnitRequiredFlag, String qpstVIEW_OS_EXPO_ADJ_SUMMARY_MemberType, Boolean qpboIsCompleted, Boolean qpboIsInProgress, Boolean qpboIsNotStarted, Boolean qpboIsProcessing, Boolean qpboIsRevisionsRequested, Boolean qpboIsSubmitted, Boolean qpboIsDevModeOn, String qpstTableSort, CancellationToken cancellationToken)- Per the information we have, it seems that the issue faced could be a side effect of Scale to 0 however not sure since the scale-ups do not match with the occurrences where they said to have faced the **&quot;**No healthy upstream&quot; messages.1. On 6th June, the occurrence was 3:45 and 4:00 PM (Portugal Time) however the scale-up was more than 10 mins ago:![](https://supportoutsystems.zendesk.com/attachments/token/hmyL2jSWAzoYN19K46MVtYAlA/?name=image.png)2. On 7th June, the occurrence was 14h50 PM (Portugal Time) and once again, the scale-up was around 30 minutes ago:![](https://supportoutsystems.zendesk.com/attachments/token/oDtpSDBfMQ28TINcMMtuQk1j8/?name=image.png)3. On 11th June, the occurrence was at 14h50 PM and the scale-up before:![](https://supportoutsystems.zendesk.com/attachments/token/Sdr66n40hRCrw7QhAngTtLnOY/?name=image.png)- **Could you assist and confirm if this is related to the scale-to-zero?****TECH DATA OR ANY OTHER RELEVANT INFO**- Ring: ga
- Tenant Id: 7a6b652e-728d-4329-a6f4-998aff1eb508
- Tenant Prefix: wcra
- Region: us-east-1
- CHU.8Z6.KIU.GFQ.3H3.OIO.X8F.AUT_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 RetrospectiveinfoDetails
**Ring:** ga
**System-wide impact:**&nbsp; No
**Tenant ID:** 7a6b652e-728d-4329-a6f4-998aff1eb508
**Tenant Prefix:** wcra
**Routing Error Code:** OS-BERT
**Product Area:** -
### Impact:
Already solved in: [https://outsystemsrd.atlassian.net/browse/RDINC-25550](https://outsystemsrd.atlassian.net/browse/RDINC-25550)
### Investigation and troubleshooting findings:
Already solved in: [https://outsystemsrd.atlassian.net/browse/RDINC-25550](https://outsystemsrd.atlassian.net/browse/RDINC-25550)
### Resolution:
Already solved in: [https://outsystemsrd.atlassian.net/browse/RDINC-25550](https://outsystemsrd.atlassian.net/browse/RDINC-25550)
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/596-dev-stage-unstable-for-about-1-week-during-a-couple-of-minutes)

**Date**

**Source**

**User**

**Event**
June 20  3:41 PM WESTwebRootly
created an alert via
June 20  3:41 PM WESTwebRootly
Rootly created this incident
June 20  3:41 PM WESTwebRootly
In triage date has been set to June 20  3:41 PM WEST
June 21 12:58 AM WESTwebRootlyZendesk Private Comment has been set: ----------------------------------------------**Update to R&amp;D**
- Detail additional findings or any questions/concerns that may be important for R&amp;D to be aware of.Hi Team,This is the Grafana link that you requested:https://outsystems.grafana.net/d/cdeqzn1jj77cwe/general-troubleshooting?orgId=1&amp;var-ring=ga&amp;var-tenant=7a6b652e-728d-4329-a6f4-998aff1eb508&amp;var-application=All&amp;var-cluster=All&amp;var-cluster_old=All&amp;var-severity=Error&amp;var-runtime=All&amp;var-filter=&amp;var-exclude=&amp;var-region=us-east-1&amp;var-traceDuration=All&amp;var-environment=All&amp;var-regionShort=ga-us-east-1-01&amp;var-tenant_prefix=wcra&amp;var-module_name=&amp;from=1718064000000&amp;to=1718113259000![](https://supportoutsystems.zendesk.com/attachments/token/oAFVewwggEIOFJSGFu56GKz6L/?name=image.png)__June 21 12:58 AM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:

June 21 12:58 AM WESTwebRootlyZendesk Private Comment has been changed to: ------------------------------------------------ This notification was sent from Zendesk Support ticket #3019135 to all linked JIRA issues by Shaharuddin Mohd Shah. --**Update to R&amp;D**- Detail additional findings or any questions/concerns that may be important for R&amp;D to be aware of.Hi Team,This is the Grafana link that you requested:https://outsystems.grafana.net/d/cdeqzn1jj77cwe/general-troubleshooting?orgId=1&amp;var-ring=ga&amp;var-tenant=7a6b652e-728d-4329-a6f4-998aff1eb508&amp;var-application=All&amp;var-cluster=All&amp;var-cluster_old=All&amp;var-severity=Error&amp;var-runtime=All&amp;var-filter=&amp;var-exclude=&amp;var-region=us-east-1&amp;var-traceDuration=All&amp;var-environment=All&amp;var-regionShort=ga-us-east-1-01&amp;var-tenant_prefix=wcra&amp;var-module_name=&amp;from=1718064000000&amp;to=1718113259000Attachment - image.png_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_June 21 12:58 AM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:

July 2  5:05 PM WESTwebRootlyZenDesk Event Type has been set: solvedJuly 2  5:05 PM WESTwebRootly
The Global Support team marked this incident as closed in ZenDesk.
July 8  4:44 PM WESTwebRootly
The Global Support team marked this incident as closed in ZenDesk.
August 5  1:56 PM WESTwebRui Garcia
Incident has been started
August 5  1:56 PM WESTwebRui Garcia
Incident has been resolved
August 5  1:56 PM WESTwebRui GarciaSystem-wide impact has been set: NoAugust 5  1:56 PM WESTwebRui GarciaImpact has been set: Already solved in: https://outsystemsrd.atlassian.net/browse/RDINC-25550August 5  1:56 PM WESTwebRui GarciaInvestigation and troubleshooting findings has been set: Already solved in: https://outsystemsrd.atlassian.net/browse/RDINC-25550August 5  1:56 PM WESTwebRui GarciaResolution has been set: Already solved in: https://outsystemsrd.atlassian.net/browse/RDINC-25550