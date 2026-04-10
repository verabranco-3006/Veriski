---
title: Retrospective-SEV2-Having issues using ODC Studio in the interface tab. Crashes with an "unrecoverable error" in several uses.
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4361420947/Retrospective-SEV2-Having+issues+using+ODC+Studio+in+the+interface+tab.+Crashes+with+an+unrecoverable+error+in+several+uses.
confluence_space: RKB
confluence_page_id: 4361420947
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV2-Having issues using ODC Studio in the interface tab. Crashes with an "unrecoverable error" in several uses.

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV2

Teams:&nbsp;trueBlueSre&nbsp;trueBlueIde Group&nbsp;trueBlueIde Group
#### 🕐 Timestamps
Started At:&nbsp;trueBlueAugust 5  8:58 PM WEST

Mitigated At:&nbsp;trueYellowAugust 6  2:58 PM WEST

Resolved At:&nbsp;trueGreenAugust 6  2:58 PM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/825-having-issues-using-odc-studio-in-the-interface-tab-crashes-with-an-unrecoverable-error-in-several-uses)
[Pagerduty incident](https://outsystems.pagerduty.com/incidents/Q2EJ4GVODMVYIU)

[Slack channel](https://slack.com/app_redirect?channel=C07FLBKSE9H&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3045237)

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

Jason Crews
#### Summary
----------------------------------------------**ISSUE DESCRIPTION AND HOW TO REPRODUCE**
- All developers are experiencing issues and crashes within the Interface Tab in ODC Studio.
- This problem affects multiple screens and prevents them from publishing.![](https://supportoutsystems.zendesk.com/attachments/token/8d3gMmT3yWs10fkgMV7xvLwF0/?name=image.png)- The customer reported that this issue began with version 1.4.17 of ODC Studio. After upgrading to version 1.4.18, the problem persists.**IMPACT ON THE CUSTOMER**
Brief description of the impact on the customer/development team/other, including:
- Development
- Ongoing
- Issue affecting all developers on several different screens blocking them from the development process.
- Additionally, this is jeopardizing the project's deadline, which is in 2 weeks.**TROUBLESHOOTING STEPS &amp; WORKAROUND**
**-** The customer was able to reproduce the issue and has provided us with a Diagnostic Report.![](https://supportoutsystems.zendesk.com/attachments/token/x0I7BSbBQbmSXrvFV6wDHD4IG/?name=image.png)- We can see the following error message from the Diagnostic Report:ServiceStudio.Presenter.RuntimeImplementation+FullStackException: Exception in thread .NET Long Running Task ---&gt; OutSystems.Model.Implementation.Oml.Referers.InvalidRefererException: Object not found: /NRWebFlows.fWtJs57lI0qCTlwkcDoxDA/NodesShownInESpaceTree.Kv+niT3pREmzDFLhaTN5yQ/Widgets.U5S12+pA00ykn9oEzdPNTg/PlaceholderArguments.6W2J2RZAuUKfFhj8S6okVw/ChildWidgets.UjqBiMkvjkO3yn2mz0gOGg/ChildPlaceholders.zKLcPwK3aUaSFYKWlJhYKQ/ChildWidgets.IHTEQ09Bt0G2MB9UWEnPyA/CustomProperties.srausRWWxE6wmx10bJczdA/ValueExpression. Object with key Kv+niT3pREmzDFLhaTN5yQ not found in collection NodesShownInESpaceTree in ServiceStudio.Model.NRFlows+WebFlow fWtJs57lI0qCTlwkcDoxDA&nbsp; at ServiceStudio.WeakReferences.CompoundKeyResolver.GetObject(CompoundKey key, AbstractObject relativeTo)&nbsp; at System.Linq.Enumerable.SelectEnumerableIterator`2.GetCount(Boolean onlyIfCheap)&nbsp; at System.Linq.EnumerableSorter`2.ComputeKeys(TElement[] elements, Int32 count)&nbsp; at System.Linq.EnumerableSorter`1.Sort(TElement[] elements, Int32 count)&nbsp; at System.Linq.OrderedEnumerable`1.GetEnumerator()+MoveNext()&nbsp; at ServiceStudio.Model.ESpace.RemoveDuplicateTypes(IEnumerable`1 types, Boolean duringCloneOrImport)&nbsp; at ServiceStudio.Model.ESpace.RemoveInvalidAnonymousTypes(Boolean duringCloneOrImport)&nbsp; at ServiceStudio.Model.ESpace.&lt;&gt;c__DisplayClass825_0.&lt;EndCommandCleanup&gt;b__1()&nbsp; at ServiceStudio.Common.Concurrency.ModelLockExtensions.&lt;&gt;c__DisplayClass2_0.&lt;DoWriteOperation&gt;b__0()&nbsp; at ServiceStudio.Common.Concurrency.ModelLockExtensions.DoWriteOperation[T](IModelLock modelLock, Func`1 func)&nbsp; at ServiceStudio.Common.Concurrency.ModelLockExtensions.DoWriteOperation(IModelLock modelLock, Action action)&nbsp; at ServiceStudio.Model.ESpace.EndCommandCleanup(Boolean wasRolledBack)&nbsp; at OutSystems.Model.Commands.Command.EndCommandCleanup(CommandExecutionContext context)&nbsp; at OutSystems.Model.Commands.Command.InnerEndCommand(CommandExecutionContext context, Action releaseCurrentCommandContext)&nbsp; at OutSystems.Model.Commands.Command.InnerSafeExecute(String description, Func`1 command, CommandExecutionContext context, Action`1 releaseCurrentCommandContext, ICommandData&amp; newCommandData)&nbsp; at OutSystems.Model.Commands.Command.&lt;&gt;c__DisplayClass69_0.&lt;SafeExecute&gt;b__1()&nbsp; at OutSystems.Model.DependenciesProviders.Execution.InnerSafeExecute[TResult](ExceptionType exceptionType, Func`2 onError, Func`1 function, PresenterContext presenterContext)&nbsp; --- End of inner exception stack trace ---&nbsp; at ServiceStudio.Presenter.RuntimeImplementation.FullStackException..ctor(Exception e)&nbsp; at prs#cpulsksw.OnException(Exception exception, ExceptionType exceptionType, PresenterContext presenterContext, Boolean presenterContextSpecific, CrashExperience crashExperience)&nbsp; at OutSystems.Model.DependenciesProviders.Execution.InnerSafeExecute[TResult](ExceptionType exceptionType, Func`2 onError, Func`1 function, PresenterContext presenterContext)&nbsp; at OutSystems.Model.Commands.Command.SafeExecute(String description, Func`1 command, CommandExecutionContext context, ICommandData&amp; newCommandData, Action onBeforeViewRefresh, Action`1 releaseCurrentCommandContext)&nbsp; at OutSystems.Model.Commands.Command.ConcurrencyManager.&lt;&gt;c__DisplayClass4_0.&lt;ExecuteSerialized&gt;b__0()&nbsp; at ServiceStudio.Common.Observability.Tracer.DoWithContext[T](String context, Func`1 func, Boolean capturePerformanceMetrics, String parentId, Dictionary`2 extraParameters, Action`1 postAction)&nbsp; at ServiceStudio.Commands.AutoRegistryCommand`3.&lt;&gt;c__DisplayClass45_0.&lt;Execute&gt;b__1()&nbsp; at OutSystems.Model.Commands.TelemetryUtils.Command(String cmdName, ICommandTarget cmdTarget, IPresenter targetPresenter, String type, ESpace eSpace, Func`1 body)&nbsp; at ServiceStudio.Commands.AutoRegistryCommand`3.Execute(ICommandTarget target, IPresenter targetPresenter)&nbsp; at ServiceStudio.Commands.Command.&lt;&gt;c__DisplayClass0_0.&lt;GetDefaultInteractionItem&gt;b__1()&nbsp; at prs#cpulskrb.prs#wsmvysou(ShortcutKey fki, IEnumerable`1 fkj, Func`3 fkk)&nbsp; at ServiceStudio.Presenter.AbstractPresenter.InnerOnKeyPressed(ShortcutKey key, Boolean checkParent, ICommandTarget overrideCommandTarget)&nbsp; at OutSystems.Model.DependenciesProviders.Execution.InnerSafeExecute[TResult](ExceptionType exceptionType, Func`2 onError, Func`1 function, PresenterContext presenterContext)&nbsp; at ServiceStudio.WebViewImplementation.Framework.AbstractViewAdapter.HandleShortcutKeyPress(ShortcutKey shortcutKey)&nbsp; at System.RuntimeMethodHandle.InvokeMethod(Object target, Span`1&amp; arguments, Signature sig, Boolean constructor, Boolean wrapExceptions)&nbsp; at System.Reflection.RuntimeMethodInfo.Invoke(Object obj, BindingFlags invokeAttr, Binder binder, Object[] parameters, CultureInfo culture)&nbsp; at Xilium.CefGlue.Common.ObjectBinding.NativeMethod.ExecuteMethod(Object targetObj, Object[] args)&nbsp; at ServiceStudio.WebViewImplementation.Framework.ContextualDispatcher.&lt;&gt;c__DisplayClass51_0`1.&lt;Post&gt;b__2()&nbsp; at ServiceStudio.WebViewImplementation.Framework.ContextualDispatcher.Execute(Frame frame, FrameAction frameAction)&nbsp; at ServiceStudio.WebViewImplementation.Framework.ContextualDispatcher.RunEventLoop()&nbsp; at ServiceStudio.WebViewImplementation.Framework.ContextualDispatcher.Run(ContextualDispatcher dispatcher)&nbsp; at ServiceStudio.WebViewImplementation.Framework.ContextualDispatcher.&lt;&gt;c__DisplayClass46_0.&lt;StartLoop&gt;b__0()&nbsp; at System.Threading.ExecutionContext.RunInternal(ExecutionContext executionContext, ContextCallback callback, Object state)&nbsp; at System.Threading.Tasks.Task.ExecuteWithThreadLocal(Task&amp; currentTaskSlot, Thread threadPoolThread)**TECH DATA OR ANY OTHER RELEVANT INFO**
- Ring: ga
- Tenant Id: 49771d54-6cbf-4530-b81a-6f19bdfab520
- Tenant Prefix: feup
- Region: eu-central-1
- 7C0.YRD.QE1.31R.W1P.KVL.1TJ.KXC
- Diagnostic Report: 2024_08_05_17_24_24__DiagnosticReport.txt_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 RetrospectiveinfoDetails
**Ring:** ga
**System-wide impact:**&nbsp; 
**Tenant ID:** 49771d54-6cbf-4530-b81a-6f19bdfab520
**Tenant Prefix:** feup
**Routing Error Code:** N/A
**Product Area:** Phoenix::ODC Studio::Publish
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/825-having-issues-using-odc-studio-in-the-interface-tab-crashes-with-an-unrecoverable-error-in-several-uses)

**Date**

**Source**

**User**

**Event**
August 5  8:57 PM WESTwebRootly
created an alert via
August 5  8:57 PM WESTwebRootly
Rootly created this incident
August 5  8:57 PM WESTwebRootly
In triage date has been set to August 5  8:57 PM WEST
August 5  8:57 PM WESTwebRootly[Slack Channel](https://slack.com/app_redirect?channel=C07FLBKSE9H&amp;team=T041063TZ) has been createdAugust 5  8:57 PM WESTwebRootly
Ring: ga
System-wide impact:  
Tenant ID: 49771d54-6cbf-4530-b81a-6f19bdfab520
Tenant Prefix: feup
Routing Error Code: N/A
Product Area: Phoenix::ODC Studio::Publish
August 5  8:57 PM WESTwebRootly[PagerDuty Incident](https://outsystems.pagerduty.com/incidents/Q2EJ4GVODMVYIU) has been created.
📲 Notified Jason Crews by push notification.  (via iPhone)&nbsp;&nbsp;📞 Notified Jason Crews by phone.&nbsp;&nbsp;📱 Notified Jason Crews by SMS.August 5  8:57 PM WESTwebRootlyJason Crews has been assigned as EngineerAugust 5  8:58 PM WESTwebRootly
Jason Crews acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q2EJ4GVODMVYIU). (via Mobile)
August 5  8:58 PM WESTwebJason Crews
Incident has been started
August 5  8:58 PM WESTwebRootly
Pagerduty Integrations acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q2EJ4GVODMVYIU). (via Mobile)
August 5  9:01 PM WESTwebJason CrewsSwarm has been set: IDE GroupAugust 5  9:01 PM WESTwebRootly
Pagerduty Integrations added Francisco Gracias as responder in [PagerDuty](https://outsystems.pagerduty.com/incidents/Q2EJ4GVODMVYIU)
August 5  9:04 PM WESTwebRootly
Francisco Gracias joined this [PagerDuty](https://outsystems.pagerduty.com/incidents/Q2EJ4GVODMVYIU) incident.
August 5  9:07 PM WESTslackjason.crews
swarming with IDE Group to identify what needs to be fixed, checking health of k8s resources for this tenant as well
August 5  9:14 PM WESTwebJason CrewsSend ZenDesk private comment has been set: Hello support,Could you please send the actual .txt file of the diagnostic report whenever you can? Thanks!August 5  9:14 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hello support,Could you please send the actual .txt file of the diagnostic report whenever you can? Thanks!
August 5  9:14 PM WESTwebRootlySend ZenDesk private comment has been unsetAugust 5  9:15 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

August 5  9:15 PM WESTslackjason.crews
this appears to be a client side issue, either in ODC Studio or in the model, reached out to support for diagnostic file to confirm
August 5  9:29 PM WESTwebFrancisco GraciasSend ZenDesk private comment has been set: Hey support team,
Building on top of the previous request:1. Indeed we need the full diagnostics report as it contains other relevant data to assist troubleshooting
2. Does the customer face this issue with other apps?
3. Can the customer share the affected OML?Since the customer reported having this issue since version 1.4.17, I've shared installers of the prior version 1.4.16.6790 in an attempt to unblock the customer:
[https://drive.google.com/drive/folders/1UlMADw4bRl_l73_em4Vj5WyRxe1kTPGi?usp=drive_link](https://drive.google.com/drive/folders/1UlMADw4bRl_l73_em4Vj5WyRxe1kTPGi?usp=drive_link)Can the customer confirm using 1.4.16.6790 fixes this unexpected error?If not, we believe the fastest way to unblock the customer is to have access to the problematic OML so we can manually fix the potentially corrupted model state that's causing the unexpected error. We would then follow-up with the fix of the root cause.Thank you in advance
Francisco GraciasAugust 5  9:29 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hey support team,
Building on top of the previous request:1. Indeed we need the full diagnostics report as it contains other relevant data to assist troubleshooting
2. Does the customer face this issue with other apps?
3. Can the customer share the affected OML?Since the customer reported having this issue since version 1.4.17, I've shared installers of the prior version 1.4.16.6790 in an attempt to unblock the customer:
[https://drive.google.com/drive/folders/1UlMADw4bRl_l73_em4Vj5WyRxe1kTPGi?usp=drive_link](https://drive.google.com/drive/folders/1UlMADw4bRl_l73_em4Vj5WyRxe1kTPGi?usp=drive_link)Can the customer confirm using 1.4.16.6790 fixes this unexpected error?If not, we believe the fastest way to unblock the customer is to have access to the problematic OML so we can manually fix the potentially corrupted model state that's causing the unexpected error. We would then follow-up with the fix of the root cause.Thank you in advance
Francisco Gracias
August 5  9:29 PM WESTwebRootlySend ZenDesk private comment has been unsetAugust 5  9:29 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

August 5  9:38 PM WESTwebRootly
Francisco Gracias acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q2EJ4GVODMVYIU). (via Mobile)
August 5 10:30 PM WESTwebRootlyZendesk Private Comment has been set: ----------------------------------------------**Update to R&amp;D**
Hello team,Thank you for your insight. I have updated the content and attached the diagnostic report .txt file to the Jira ticket.__August 5 10:30 PM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
Hello team,Thank you for your insight. I have updated the content and attached the diagnostic report .txt file to the Jira ticket.__
August 5 10:34 PM WESTwebRootlyZendesk Private Comment has been changed to: ----------------------------------------------**Update to R&amp;D**Hello Team,Thank you for the update.We will validate the mentioned steps with the customer and inform you accordingly._&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_August 5 10:34 PM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**Hello Team,Thank you for the update.We will validate the mentioned steps with the customer and inform you accordingly.__
August 5 10:56 PM WESTwebFrancisco GraciasSend ZenDesk private comment has been set: Hi support team, thank you for your response.
Since we're using Rootly I'm not sure what jira ticket you're referring to where you've attached the diagnostics report.
If possible, please share the diagnostics report in rootly or share the jira issue ticket.
Thank you once again,
FranciscoAugust 5 10:56 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hi support team, thank you for your response.
Since we're using Rootly I'm not sure what jira ticket you're referring to where you've attached the diagnostics report.
If possible, please share the diagnostics report in rootly or share the jira issue ticket.
Thank you once again,
Francisco
August 5 10:56 PM WESTwebRootlySend ZenDesk private comment has been unsetAugust 5 10:56 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

August 5 11:26 PM WESTwebRootlyZendesk Private Comment has been changed to: ----------------------------------------------**Update to R&amp;D**
Hi Team,As we don&rsquo;t have direct access to Rootly, please refer to the following Jira issue ticket as requested: https://outsystemsrd.atlassian.net/browse/RDINC-28075Best Regards,Francisco_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_August 5 11:26 PM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
Hi Team,As we don&rsquo;t have direct access to Rootly, please refer to the following Jira issue ticket as requested: https://outsystemsrd.atlassian.net/browse/RDINC-28075Best Regards,Francisco__
August 6  2:58 PM WESTwebRootly
The Global Support team marked this incident as closed in ZenDesk.
August 6  2:58 PM WESTwebRootly
Incident has been resolved
August 6  2:58 PM WESTwebRootlyZenDesk Event Type has been set: solvedAugust 14  4:06 PM WESTwebRootly
The Global Support team marked this incident as closed in ZenDesk.