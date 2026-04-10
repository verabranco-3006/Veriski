---
title: Retrospective-SEV2-Application Issue on iOS 15 – Blue Screen on Launch
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4263870499/Retrospective-SEV2-Application+Issue+on+iOS+15+Blue+Screen+on+Launch
confluence_space: RKB
confluence_page_id: 4263870499
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV2-Application Issue on iOS 15 – Blue Screen on Launch

## 📘 Overview
Author:&nbsp;Rootlytrue

Severity:&nbsp;SEV2Redtrue

Teams:&nbsp;Client RuntimeBluetrue
#### 🕐 Timestamps
Started At:&nbsp;July 1  7:42 AM WESTBluetrue

Mitigated At:&nbsp;July 4 10:12 AM WESTYellowtrue

Resolved At:&nbsp;July 4 10:12 AM WESTGreentrue
#### 🔗 Links
[Incident Page](https://rootly.com/account/incidents/646-application-issue-on-ios-15-blue-screen-on-launch)

[Pagerduty incident](https://outsystems.pagerduty.com/incidents/Q0TO13TV82JLP2)

[Slack channel](https://slack.com/app_redirect?channel=C07AJ99DU8L&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3029088)

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

Carlos Xavier
#### Summary
&lt;hr&gt;
&lt;p class=&quot;redcarpet&quot;&gt;&lt;strong&gt;CONSIDERATIONS BEFORE PERFORMING THE ESCALATION TO R&amp;D (MANDATORY)&lt;/strong&gt;
&lt;br&gt;None of the below points should be overlooked. Failure to do so may imply unnecessary effort.&lt;/p&gt;
&lt;hr&gt;
&lt;p class=&quot;redcarpet&quot;&gt;Ensure the ticket has been &lt;strong&gt;categorized&lt;/strong&gt;, otherwise, the R&amp;D escalation will go unnoticed and not be worked on!&lt;/p&gt;&lt;p class=&quot;redcarpet&quot;&gt;&lt;strong&gt;1.&lt;/strong&gt; For &lt;strong&gt;Incidents&lt;/strong&gt;, the &lt;strong&gt;IMAX&lt;/strong&gt; was consulted &lt;strong&gt;beforehand&lt;/strong&gt; on which:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;No incident models were found for the reported symptoms &lt;strong&gt;OR&lt;/strong&gt;
&lt;/li&gt;
&lt;li&gt;The incident model did not solve the issue &lt;strong&gt;OR&lt;/strong&gt;
&lt;/li&gt;
&lt;li&gt;The next step indicated in the Incident Model is an escalation to R&amp;D.
&lt;strong&gt;2.&lt;/strong&gt; For &lt;strong&gt;Questions&lt;/strong&gt;, the ChatODC on the &lt;strong&gt;Slack channel&lt;/strong&gt; didn't return an acceptable answer.
&lt;strong&gt;3.&lt;/strong&gt; Any other requests that explicitly indicate an R&amp;D escalation is needed.
&lt;strong&gt;4&lt;/strong&gt;. &lt;strong&gt;Incident impact assessment&lt;/strong&gt; was based on the &lt;strong&gt;prioritization scoring matrix&lt;/strong&gt;.&lt;/li&gt;
&lt;/ul&gt;&lt;hr&gt;
&lt;p class=&quot;redcarpet&quot;&gt;&lt;strong&gt;R&amp;D ESCALATION FORM&lt;/strong&gt;
&lt;br&gt;Section comments can be removed for R&amp;D easier interpretation.&lt;/p&gt;&lt;p class=&quot;redcarpet&quot;&gt;&lt;strong&gt;ISSUE DESCRIPTION AND HOW TO REPRODUCE&lt;/strong&gt;&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;
&lt;p class=&quot;redcarpet&quot;&gt;iOS app gets stuck in the splash screen for the older versions of iOS&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;The customer says the issue happens on iOS version 15.8.2&lt;/li&gt;
&lt;li&gt;In our own tests it happens even on iOS version 16.1.1&lt;/li&gt;
&lt;li&gt;Screen recording of the issue&lt;/li&gt;
&lt;li&gt;Ayming Collect Error.mp4&lt;/li&gt;
&lt;/ul&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p class=&quot;redcarpet&quot;&gt;On iOS version 17, the issue does not happen.&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Ayming Collect.mp4&lt;/li&gt;
&lt;/ul&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p class=&quot;redcarpet&quot;&gt;Name of app:- Ayming Collect&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Generated on MABS 10.&lt;/li&gt;
&lt;/ul&gt;
&lt;/li&gt;
&lt;/ul&gt;
&lt;p class=&quot;redcarpet&quot;&gt;&lt;strong&gt;IMPACT ON THE CUSTOMER&lt;/strong&gt;&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;High, as this is a critical B2C app for the customer and some of the users are using the older iOS version 15 and 16.&lt;/li&gt;
&lt;/ul&gt;
&lt;p class=&quot;redcarpet&quot;&gt;&lt;strong&gt;TROUBLESHOOTING STEPS &amp; WORKAROUND&lt;/strong&gt;&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;
&lt;p class=&quot;redcarpet&quot;&gt;We tried to install the app in an actual iPhone, but was not able to.&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a target=&quot;_blank&quot; href=&quot;https://intranet.outsystems.net/MABS/BuildDetail.aspx?BuildId=21e92bde9a925e27a31c494cc3747a4ba29db2a2&quot;&gt;https://intranet.outsystems.net/MABS/BuildDetail.aspx?BuildId=21e92bde9a925e27a31c494cc3747a4ba29db2a2&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;21e92bde9a925e27a31c494cc3747a4ba29db2a2_RequestJSON.json
service-file (5).log
AymingCollect.ipa
source (1).tar.gz&lt;/li&gt;
&lt;/ul&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p class=&quot;redcarpet&quot;&gt;As such used Sauce labs.&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;In an iPhone 12 Pro (&lt;strong&gt;iOS 16.1.1&lt;/strong&gt;)&lt;/li&gt;
&lt;li&gt;When we open the app we get this.&lt;ul&gt;
&lt;li&gt;&lt;img width=&quot;100%&quot; src=&quot;https://supportoutsystems.zendesk.com/attachments/token/SRx39dqHk5p7RkS3ZPlL9KoXN/?name=image.png&quot;&gt;&lt;/li&gt;
&lt;li&gt;Blank blue screen as reported by the customer.&lt;/li&gt;
&lt;li&gt;This is the error in the device log of Sauce labs&lt;/li&gt;
&lt;/ul&gt;
&lt;/li&gt;
&lt;/ul&gt;
&lt;p class=&quot;redcarpet&quot;&gt;04:09:45 E Ayming Collect(RunningBoardServices)[648] : Error acquiring assertion: 04:09:45 E Ayming Collect(WebKit)[648] : 0x11301c420 - ProcessAssertion::acquireSync Failed to acquire RBS assertion 'ConnectionTerminationWatchdog' for process with PID=651, error: Error Domain=RBSServiceErrorDomain Code=1 &quot;target is not running or doesn't have entitlement com.apple.runningboard.assertions.webkit&quot; UserInfo={NSLocalizedFailureReason=target is not running or doesn't have entitlement com.apple.runningboard.assertions.webkit}04:09:45 E Ayming Collect(RunningBoardServices)[648] : Error acquiring assertion: 04:09:45 E Ayming Collect(WebKit)[648] : 0x11301c480 - ProcessAssertion::acquireSync Failed to acquire RBS assertion 'WebProcess Suspended Assertion' for process with PID=651, error: Error Domain=RBSAssertionErrorDomain Code=2 &quot;Specified target process does not exist&quot; UserInfo={NSLocalizedFailureReason=Specified target process does not exist}04:11:23 E Ayming Collect(CoreHaptics)[648] : AVHapticClient.mm:446 -[AVHapticClient finish:]: ERROR: Player was not running - bailing with error Error Domain=com.apple.CoreHaptics Code=-4805 &quot;(null)&quot; for client 0x100028804:11:23 E Ayming Collect(UIKitCore)[648] : core haptics engine finished for &lt;_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x28304dab0&gt; with error: Error Domain=com.apple.CoreHaptics Code=-4805 &quot;(null)&quot;04:13:44 E Ayming Collect(RunningBoardServices)[672] : Error acquiring assertion: 04:13:44 E Ayming Collect(WebKit)[672] : 0x11201c360 - ProcessAssertion::acquireSync Failed to acquire RBS assertion 'WebProcess Suspended Assertion' for process with PID=674, error: Error Domain=RBSServiceErrorDomain Code=1 &quot;target is not running or doesn't have entitlement com.apple.runningboard.assertions.webkit&quot; UserInfo={NSLocalizedFailureReason=target is not running or doesn't have entitlement com.apple.runningboard.assertions.webkit}&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p class=&quot;redcarpet&quot;&gt;In the ODC portal logs we can see this error&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;&lt;img width=&quot;100%&quot; src=&quot;https://supportoutsystems.zendesk.com/attachments/token/8t4TAnWFv39LCQjsENdufERGJ/?name=image.png&quot;&gt;&lt;/li&gt;
&lt;li&gt;&lt;strong&gt;Failed to load cache manifest: File /var/mobile/Containers/Data/Application/B2E4DF99-5FA0-4ADD-AAB9-C925DF2E0EF8/Library/Application Support/OSNativeCache/OSCacheManifest.plist not found. The file was never created.&lt;/strong&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p class=&quot;redcarpet&quot;&gt;In an iPhone 11 (&lt;strong&gt;iOS 17.4.1&lt;/strong&gt;)&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;The app opens without any problems&lt;/li&gt;
&lt;li&gt;&lt;img width=&quot;100%&quot; src=&quot;https://supportoutsystems.zendesk.com/attachments/token/MBH25XPQSuUjESqvCPdu0ps0Y/?name=image.png&quot;&gt;&lt;/li&gt;
&lt;li&gt;This is the device logs here (filtered for errors)&lt;/li&gt;
&lt;/ul&gt;
&lt;p class=&quot;redcarpet&quot;&gt;04:19:53 E Ayming Collect(WebKit)[573] : Warning: -[BETextInput attributedMarkedText] is unimplemented04:19:54 E Ayming Collect(RunningBoardServices)[573] : Error acquiring assertion: 04:19:54 E Ayming Collect(WebKit)[573] : 0x112040600 - ProcessAssertion::acquireSync Failed to acquire RBS assertion 'WebProcess NearSuspended Assertion' for process with PID=576, error: (null)04:19:54 E Ayming Collect(WebKit)[573] : Failed to request allowed query parameters from WebPrivacy.&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p class=&quot;redcarpet&quot;&gt;In the ODC portal logs we can see this set of messages for the successful app launch.&lt;/p&gt;
&lt;h2&gt;- &lt;img width=&quot;100%&quot; src=&quot;https://supportoutsystems.zendesk.com/attachments/token/3yHZT69A9uXZ0q4RiyyAFTqaI/?name=image.png&quot;&gt;
&lt;/h2&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p class=&quot;redcarpet&quot;&gt;Searching for the error&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;&lt;em&gt;Failed to load cache manifest OSCacheManifest.plist not found. The file was never created.&lt;/em&gt;&lt;/li&gt;
&lt;li&gt;Past tickets with this error #2753471 , #2931674&lt;/li&gt;
&lt;li&gt;These are O11 tickets and the reasons seem to vary.&lt;/li&gt;
&lt;li&gt;In Confluence some relevant articles&lt;/li&gt;
&lt;li&gt;&lt;a target=&quot;_blank&quot; href=&quot;https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/3581411739/Upgrades+over-the-air+OTA+in+O11+-+Overview&quot;&gt;https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/3581411739/Upgrades+over-the-air+OTA+in+O11+-+Overview&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;a target=&quot;_blank&quot; href=&quot;https://outsystemsrd.atlassian.net/wiki/spaces/CloudKB/pages/932677743/How+do+the+over-the-air+updates+work&quot;&gt;https://outsystemsrd.atlassian.net/wiki/spaces/CloudKB/pages/932677743/How+do+the+over-the-air+updates+work&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;&lt;img width=&quot;100%&quot; src=&quot;https://supportoutsystems.zendesk.com/attachments/token/09RCfqVUwW99rL68lAqkXXvVR/?name=image.png&quot;&gt;&lt;/li&gt;
&lt;li&gt;External article&lt;/li&gt;
&lt;li&gt;&lt;a target=&quot;_blank&quot; href=&quot;https://success.outsystems.com/support/troubleshooting/application_runtime/troubleshooting_over_the_air_upgrades/failed_to_load_cache_manifest_filepath_file_not_found_the_file_was_never_created/&quot;&gt;https://success.outsystems.com/support/troubleshooting/application_runtime/troubleshooting_over_the_air_upgrades/failed_to_load_cache_manifest_filepath_file_not_found_the_file_was_never_created/&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;But again, does not seem relevant here.&lt;/li&gt;
&lt;li&gt;No IMAX entries&lt;/li&gt;
&lt;li&gt;The grafana logs don't reveal much&lt;/li&gt;
&lt;li&gt;&lt;a target=&quot;_blank&quot; href=&quot;https://outsystems.grafana.net/d/cdeqzn1jj77cwe/general-troubleshooting?orgId=1&amp;amp;from=1719799200000&amp;amp;to=1719801059000&quot;&gt;https://outsystems.grafana.net/d/cdeqzn1jj77cwe/general-troubleshooting?orgId=1&amp;amp;from=1719799200000&amp;amp;to=1719801059000&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p class=&quot;redcarpet&quot;&gt;From the portal, we can see they do have External Provider Configured&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;&lt;img width=&quot;100%&quot; src=&quot;https://supportoutsystems.zendesk.com/attachments/token/2XdnOSMdMhRX8OUmLneM8Mj3V/?name=image.png&quot;&gt;&lt;/li&gt;
&lt;li&gt;However when I opened the app, I don't think they are using External Provider to login&lt;/li&gt;
&lt;li&gt;&lt;img width=&quot;100%&quot; src=&quot;https://supportoutsystems.zendesk.com/attachments/token/xt8TR2Crz5xRzNsaduihviopo/?name=image.png&quot;&gt;&lt;/li&gt;
&lt;li&gt;It looks like they are using the standard built-in identity provider.&lt;/li&gt;
&lt;li&gt;Attached is the OML&lt;/li&gt;
&lt;li&gt;Ayming Collect.oml&lt;/li&gt;
&lt;/ul&gt;
&lt;/li&gt;
&lt;/ul&gt;
&lt;p class=&quot;redcarpet&quot;&gt;&lt;strong&gt;TECH DATA OR ANY OTHER RELEVANT INFO&lt;/strong&gt;&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Ring: ga&lt;/li&gt;
&lt;li&gt;Tenant Id: 33003270-ef13-47c6-90a3-7b7674c8b10e&lt;/li&gt;
&lt;li&gt;Tenant Prefix: collect-ayming&lt;/li&gt;
&lt;li&gt;Region: eu-central-1&lt;/li&gt;
&lt;li&gt;IKG.F4Q.FUQ.NML.PKO.XGL.K5F.AOU&lt;/li&gt;
&lt;/ul&gt;
&lt;p class=&quot;redcarpet&quot;&gt;&lt;em&gt;&lt;! do not remove this line, this will be used to the trigger&lt;/em&gt; Technical Support::Send to R&amp;D - ODC &lt;em&gt;#trigger_send_to_r&amp;d_odc !&gt;&lt;/em&gt;&lt;/p&gt;&lt;p class=&quot;redcarpet&quot;&gt;Attachment(s):
&lt;br&gt;Ayming Collect Error.mp4 - &lt;a href=&quot;https://supportoutsystems.zendesk.com/attachments/token/L8VIqoUgMbeIHabSUGGVGOMrO/?name=Ayming+Collect+Error.mp421e92bde9a925e27a31c494cc3747a4ba29db2a2_RequestJSON.json&quot;&gt;https://supportoutsystems.zendesk.com/attachments/token/L8VIqoUgMbeIHabSUGGVGOMrO/?name=Ayming+Collect+Error.mp421e92bde9a925e27a31c494cc3747a4ba29db2a2_RequestJSON.json&lt;/a&gt; - &lt;a href=&quot;https://supportoutsystems.zendesk.com/attachments/token/yeB6HAPHsN7aV4zYV94GG0mkE/?name=21e92bde9a925e27a31c494cc3747a4ba29db2a2_RequestJSON.jsonAyming&quot;&gt;https://supportoutsystems.zendesk.com/attachments/token/yeB6HAPHsN7aV4zYV94GG0mkE/?name=21e92bde9a925e27a31c494cc3747a4ba29db2a2_RequestJSON.jsonAyming&lt;/a&gt; Collect.oml - &lt;a href=&quot;https://supportoutsystems.zendesk.com/attachments/token/7EqvY8PtdKaQNJfOj3iKdsmx8/?name=Ayming+Collect.omlservice-file&quot;&gt;https://supportoutsystems.zendesk.com/attachments/token/7EqvY8PtdKaQNJfOj3iKdsmx8/?name=Ayming+Collect.omlservice-file&lt;/a&gt; (5).log - &lt;a href=&quot;https://supportoutsystems.zendesk.com/attachments/token/x5Vbjgd2uC53JyEonhX6lycy2/?name=service-file+%285%29.logAymingCollect.ipa&quot;&gt;https://supportoutsystems.zendesk.com/attachments/token/x5Vbjgd2uC53JyEonhX6lycy2/?name=service-file+%285%29.logAymingCollect.ipa&lt;/a&gt; - &lt;a href=&quot;https://supportoutsystems.zendesk.com/attachments/token/cxiAR9jydE6DxE0wv3pQNwdON/?name=AymingCollect.ipaAyming&quot;&gt;https://supportoutsystems.zendesk.com/attachments/token/cxiAR9jydE6DxE0wv3pQNwdON/?name=AymingCollect.ipaAyming&lt;/a&gt; Collect_Success.mp4 - &lt;a href=&quot;https://supportoutsystems.zendesk.com/attachments/token/RQCOjrCIiewwwJDkW5CUkgC2j/?name=Ayming+Collect_Success.mp4&quot;&gt;https://supportoutsystems.zendesk.com/attachments/token/RQCOjrCIiewwwJDkW5CUkgC2j/?name=Ayming+Collect_Success.mp4&lt;/a&gt;&lt;/p&gt;
## 📝 Retrospective### Details
**Ring:** ga
**System-wide impact:**&nbsp; 
**Tenant ID:** 33003270-ef13-47c6-90a3-7b7674c8b10e
**Tenant Prefix:** collect-ayming
**Routing Error Code:** N/A
**Product Area:** Phoenix::Application Runtime::Mobile Applications::Client Side
### Impact:
Customer can't load applications using iOS versions between iOS 15 and 16.4
### Investigation and troubleshooting findings:
There was one third-party library that contained JavaScript syntax not supported in older devices.
### Resolution:
We included third-party libraries in the transpilation process to ensure all code is made compatible with the device versions supported by the platform.
## Tasks performed during incident resolution:
&nbsp;
## Executive Summary
On June 30 at 11:32 PM we received an incident report #646 where the customer wasn&rsquo;t able to use applications on iOS versions between 15 and 16.4. Investigation concluded that the issue was with a third party library that was updated to a more recent version which contained JavaScript syntax not supported in iOS versions before 16.4.

This situation represents a inability to use applications in iOS devices prior to 16.4.

From a technical perspective, the problem was caused by a recent version of the opentelemetry-js library which contained static initialization blocks, a feature that is not supported on iOS versions prior to 16.4. This library is used by our @outsystems/logger-js project.

As a consequence of the incident we have:

- 
Short term: Fixed the issue by transpiling all third-party libraries in our @outsystems/logger-js project.

- 
Medium/Long term: Transpile all third-party libraries in all client runtime projects to avoid similar issues.

## Root Causes 
Third-party libraries were not being transpiled. This is a general practice since third-party libraries authors typically do it themselves to ensure their libraries are compatible with a good set of devices. This is not the case on the opentelemetry-js library, which seems to not be getting much attention from their authors regarding browser support.

If the customer needs formal RCA, please fill out the following field with the document URL

[Please follow these instructions and place the RCA URL in the field below.](https://docs.google.com/document/d/13rXmBsOJh73nV2D6Z17SIBGBu2HOTWty5ddsvU000JM/edit#heading=h.bqxasxszr5q)

RCA URL

&lt;Place the URL of the customer RCA here if you have created one&gt;
## ⌛ Timeline
[View on Rootly](https://rootly.com/account/incidents/646-application-issue-on-ios-15-blue-screen-on-launch)

**Date**

**Source**

**User**

**Event**

July 1  7:32 AM WEST

web

Rootly

created an alert via

July 1  7:32 AM WEST

web

Rootly

Rootly created this incident

July 1  7:32 AM WEST

web

Rootly

In triage date has been set to July 1  7:32 AM WEST

July 1  7:32 AM WEST

web

Rootly

[Slack Channel](https://slack.com/app_redirect?channel=C07AJ99DU8L&amp;team=T041063TZ) has been created

July 1  7:32 AM WEST

web

Rootly

Ring: ga
System-wide impact:  
Tenant ID: 33003270-ef13-47c6-90a3-7b7674c8b10e
Tenant Prefix: collect-ayming
Routing Error Code: N/A
Product Area: Phoenix::Application Runtime::Mobile Applications::Client Side

July 1  7:32 AM WEST

web

Rootly

[PagerDuty Incident](https://outsystems.pagerduty.com/incidents/Q0TO13TV82JLP2) has been created.

📧 Notified Tiago Miguel Pereira by email.

&nbsp;&nbsp;

📲 Notified Tiago Miguel Pereira by push notification.  (via Android)

&nbsp;&nbsp;

📲 Notified Tiago Miguel Pereira by push notification.  (via Android)

July 1  7:32 AM WEST

web

Rootly

Tiago M. Pereira has been assigned as Engineer

July 1  7:35 AM WEST

web

Rootly

Tiago Miguel Pereira acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q0TO13TV82JLP2). (via Slack)

July 1  7:42 AM WEST

web

Tiago M. Pereira

Incident has been started

July 1  7:42 AM WEST

web

Rootly

Pagerduty Integrations acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q0TO13TV82JLP2). (via Slack)

July 1  8:00 AM WEST

web

Tiago M. Pereira

Swarm has been set: Mobile Core

July 1  8:00 AM WEST

web

Rootly

Pagerduty Integrations added Tiago Alexandre Pinto Pereira as responder in [PagerDuty](https://outsystems.pagerduty.com/incidents/Q0TO13TV82JLP2)

July 1  8:05 AM WEST

slack

tiago.miguel.pereira

Taking into account that the app is opening without any issues for iOS versions 16 and 17. From what the customer says, some users with iOS version 15 are not being able to open the application. The customer also suggests that this might be an issue related with MABS 10.
I'm adding Mobile Core team to help us understanding the origin of this problem.

July 1  8:06 AM WEST

web

Rootly

Tiago Alexandre Pinto Pereira joined this [PagerDuty](https://outsystems.pagerduty.com/incidents/Q0TO13TV82JLP2) incident.

July 1  8:46 AM WEST

slack

tiago.miguel.pereira

It seems that the log &quot;target is not running or doesn't have entitlement com.apple.runningboard.assertions.webkit&quot; might be related with Cordova in iOS. More people are complaining about this in github. e.g [https://github.com/apache/cordova-ios/issues/1103](https://github.com/apache/cordova-ios/issues/1103)
From what @tiago.pinto.pereira said, this is for Mobile Runtime team.
Apparently the team doesn't exist in Rootly... However, they are already aware of this and they'll take a look

July 1 11:06 AM WEST

web

Tiago M. Pereira

Teams has been removed: [Client Runtime](/account/teams/client-runtime/status)

July 1 11:14 AM WEST

web

Tiago Pereira

The .ipa shared was signed with a Distribution Certificate (for App Store). I'm not sure how the application was installed on the Sauce Labs devices, I'm assuming it was resigned.
Nevertheless, downloaded the source code and signed the generated binary with a development certificate. Installed the app on a physical iOS 16 device and the application behaved without an issue.

July 1 12:44 PM WEST

slack

tiago.pinto.pereira

Engaged with the Mobile Runtime team. The team doesn&rsquo;t exist on Rootly (it is being fixed in the meantime), but @andre.destro is working on this. The Jira ticket is now on their side.
We confirm that the application gets stuck on iOS 15, but, contrarily to what happens on SauceLabs, on iOS 16 works correctly. We are focused on iOS 15 and to identify what might be causing the issue on that specific iOS version only.

July 1  7:37 PM WEST

web

Tiago M. Pereira

Send ZenDesk private comment has been set: Hello team,Thank you for reaching out and for all the information that was shared.The Client Runtime team analyzed the ticket and we can confirm that this issue has existed in the Client Runtime's code for a long time, making it impossible to roll back to a version that would accelerate the process of fixing the issue currently affecting the customer.This problem is related to the usage of [static initialization blocks](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Static_initialization_blocks), currently used by OpenTelemetry and other libraries required by the runtime. The issue stopped affecting our customers starting with iOS 16.4.We created a new bug [[RAR-2745](https://outsystemsrd.atlassian.net/browse/RAR-2745)] to address this issue. The bug identifier that should appear in the release notes is RAR-2745.Let us know if you have any additional questions,
Kind regards,
Tiago Pereira

July 1  7:37 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:
Hello team,Thank you for reaching out and for all the information that was shared.The Client Runtime team analyzed the ticket and we can confirm that this issue has existed in the Client Runtime's code for a long time, making it impossible to roll back to a version that would accelerate the process of fixing the issue currently affecting the customer.This problem is related to the usage of [static initialization blocks](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Static_initialization_blocks), currently used by OpenTelemetry and other libraries required by the runtime. The issue stopped affecting our customers starting with iOS 16.4.We created a new bug [[RAR-2745](https://outsystemsrd.atlassian.net/browse/RAR-2745)] to address this issue. The bug identifier that should appear in the release notes is RAR-2745.Let us know if you have any additional questions,
Kind regards,
Tiago Pereira

July 1  7:37 PM WEST

web

Rootly

Send ZenDesk private comment has been unset

July 1  7:37 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:

July 1  8:03 PM WEST

web

Tiago M. Pereira

Teams has been added: [Client Runtime](/account/teams/client-runtime/status)

July 1  8:03 PM WEST

web

Tiago M. Pereira

Teams has been removed: [Mobile Core](/account/teams/mobile-core/status)

July 1  8:18 PM WEST

web

Tiago M. Pereira

Summary has been changed to 

&nbsp;&nbsp;`&nbsp;&nbsp;`

`&nbsp;&nbsp;`

`&nbsp;&nbsp;`

`&nbsp;&nbsp;CONSIDERATIONS BEFORE PERFORMING THE ESCALATION TO R&amp;D (MANDATORY)`
`&nbsp;&nbsp;`
`None of the below points should be overlooked. Failure to do so may imply unnecessary effort.`

`&nbsp;&nbsp;`
`&nbsp;&nbsp;`

`Ensure the ticket has been categorized, otherwise, the R&amp;D escalation will go unnoticed and not be worked on!`

`&nbsp;&nbsp;`

`&nbsp;&nbsp;1. For Incidents, the IMAX was consulted beforehand on which:`

`&nbsp;&nbsp;`

- 

`&nbsp;&nbsp;`

- 
`No incident models were found for the reported symptoms OR`
`&nbsp;&nbsp;`

- 

`&nbsp;&nbsp;`

- 
`The incident model did not solve the issue OR`
`&nbsp;&nbsp;`

- 

`&nbsp;&nbsp;`

- 
The next step indicated in the Incident Model is an escalation to R&amp;D.

&nbsp;&nbsp;2. For Questions, the ChatODC on the Slack channel didn't return an acceptable answer.

&nbsp;&nbsp;3. Any other requests that explicitly indicate an R&amp;D escalation is needed.

`&nbsp;&nbsp;4. Incident impact assessment was based on the prioritization scoring matrix.`

- 

`&nbsp;&nbsp;`

`&nbsp;&nbsp;&nbsp;&nbsp;`

`&nbsp;&nbsp;`

`&nbsp;&nbsp;`

`&nbsp;&nbsp;R&amp;D ESCALATION FORM`
`&nbsp;&nbsp;`
`Section comments can be removed for R&amp;D easier interpretation.`

`&nbsp;&nbsp;`

`&nbsp;&nbsp;ISSUE DESCRIPTION AND HOW TO REPRODUCE&nbsp;&nbsp;`

`&nbsp;&nbsp;`

- 

`&nbsp;&nbsp;`

- 

`&nbsp;&nbsp;`

`iOS app gets stuck in the splash screen for the older versions of iOS`

`&nbsp;&nbsp;`

- 

`&nbsp;&nbsp;`

- 
`The customer says the issue happens on iOS version 15.8.2`

- 

`&nbsp;&nbsp;`

- 
`In our own tests it happens even on iOS version 16.1.1`

- 

`&nbsp;&nbsp;`

- 
`Screen recording of the issue`

- 

`&nbsp;&nbsp;`

- 
`Ayming Collect Error.mp4`

- 

`&nbsp;&nbsp;`

`&nbsp;&nbsp;`

- 

`&nbsp;&nbsp;`

- 

`&nbsp;&nbsp;`

`On iOS version 17, the issue does not happen.`

`&nbsp;&nbsp;`

- 

`&nbsp;&nbsp;`

- 
`Ayming Collect.mp4`

- 

`&nbsp;&nbsp;`

`&nbsp;&nbsp;`

- 

`&nbsp;&nbsp;`

- 

`&nbsp;&nbsp;`

`Name of app:- Ayming Collect`

`&nbsp;&nbsp;`

- 

`&nbsp;&nbsp;`

- 
`Generated on MABS 10.`

- 

`&nbsp;&nbsp;`

`&nbsp;&nbsp;`

- 

`&nbsp;&nbsp;`

`&nbsp;&nbsp;`

`&nbsp;&nbsp;IMPACT ON THE CUSTOMER&nbsp;&nbsp;`

`&nbsp;&nbsp;`

- 

`&nbsp;&nbsp;`

- 
`High, as this is a critical B2C app for the customer and some of the users are using the older iOS version 15 and 16.`

- 

`&nbsp;&nbsp;`

`&nbsp;&nbsp;`

`&nbsp;&nbsp;TROUBLESHOOTING STEPS &amp; WORKAROUND&nbsp;&nbsp;`

`&nbsp;&nbsp;`

- 

`&nbsp;&nbsp;`

- 

`&nbsp;&nbsp;`

`We tried to install the app in an actual iPhone, but was not able to.`

`&nbsp;&nbsp;`

- 

`&nbsp;&nbsp;`

- 
`&nbsp;&nbsp;`[&nbsp;&nbsp;](https://intranet.outsystems.net/MABS/BuildDetail.aspx?BuildId=21e92bde9a925e27a31c494cc3747a4ba29db2a2)`&nbsp;&nbsp;`[https://intranet.outsystems.net/MABS/BuildDetail.aspx?BuildId=21e92bde9a925e27a31c494cc3747a4ba29db2a2](https://intranet.outsystems.net/MABS/BuildDetail.aspx?BuildId=21e92bde9a925e27a31c494cc3747a4ba29db2a2)`&nbsp;&nbsp;`

- 

`&nbsp;&nbsp;`

- 
21e92bde9a925e27a31c494cc3747a4ba29db2a2_RequestJSON.json

service-file (5).log

AymingCollect.ipa

`source (1).tar.gz`

- 

`&nbsp;&nbsp;`

`&nbsp;&nbsp;`

- 

`&nbsp;&nbsp;`

- 

`&nbsp;&nbsp;`

`As such used Sauce labs.`

`&nbsp;&nbsp;`

- 

`&nbsp;&nbsp;`

- 
`In an iPhone 12 Pro (iOS 16.1.1)`

- 

`&nbsp;&nbsp;`

- 
`When we open the app we get this.`

- 
`&nbsp;&nbsp;`

`&nbsp;&nbsp;`

- 
`&nbsp;&nbsp;`

&nbsp;&nbsp;

- 
`&nbsp;&nbsp;`

`&nbsp;&nbsp;`

- 
`Blank blue screen as reported by the customer.`

- 
`This is the error in the device log of Sauce labs`

`&nbsp;&nbsp;`

`&nbsp;&nbsp;`

`04:09:45 E Ayming Collect(RunningBoardServices)[648] : Error acquiring assertion: 04:09:45 E Ayming Collect(WebKit)[648] : 0x11301c420 - ProcessAssertion::acquireSync Failed to acquire RBS assertion 'ConnectionTerminationWatchdog' for process with PID=651, error: Error Domain=RBSServiceErrorDomain Code=1 &quot;target is not running or doesn't have entitlement com.apple.runningboard.assertions.webkit&quot; UserInfo={NSLocalizedFailureReason=target is not running or doesn't have entitlement com.apple.runningboard.assertions.webkit}04:09:45 E Ayming Collect(RunningBoardServices)[648] : Error acquiring assertion: 04:09:45 E Ayming Collect(WebKit)[648] : 0x11301c480 - ProcessAssertion::acquireSync Failed to acquire RBS assertion 'WebProcess Suspended Assertion' for process with PID=651, error: Error Domain=RBSAssertionErrorDomain Code=2 &quot;Specified target process does not exist&quot; UserInfo={NSLocalizedFailureReason=Specified target process does not exist}04:11:23 E Ayming Collect(CoreHaptics)[648] : AVHapticClient.mm:446 -[AVHapticClient finish:]: ERROR: Player was not running - bailing with error Error Domain=com.apple.CoreHaptics Code=-4805 &quot;(null)&quot; for client 0x100028804:11:23 E Ayming Collect(UIKitCore)[648] : core haptics engine finished for &lt;_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x28304dab0&gt; with error: Error Domain=com.apple.CoreHaptics Code=-4805 &quot;(null)&quot;04:13:44 E Ayming Collect(RunningBoardServices)[672] : Error acquiring assertion: 04:13:44 E Ayming Collect(WebKit)[672] : 0x11201c360 - ProcessAssertion::acquireSync Failed to acquire RBS assertion 'WebProcess Suspended Assertion' for process with PID=674, error: Error Domain=RBSServiceErrorDomain Code=1 &quot;target is not running or doesn't have entitlement com.apple.runningboard.assertions.webkit&quot; UserInfo={NSLocalizedFailureReason=target is not running or doesn't have entitlement com.apple.runningboard.assertions.webkit}`

`&nbsp;&nbsp;`

`&nbsp;&nbsp;`

- 
&nbsp;&nbsp;
In the ODC portal logs we can see this error

&nbsp;&nbsp;

&nbsp;&nbsp;- &nbsp;&nbsp;&nbsp;&nbsp;

&nbsp;&nbsp;- &nbsp;&nbsp;**Failed to load cache manifest: File /var/mobile/Containers/Data/Application/B2E4DF99-5FA0-4ADD-AAB9-C925DF2E0EF8/Library/Application Support/OSNativeCache/OSCacheManifest.plist not found. The file was never created.**&nbsp;&nbsp;

&nbsp;&nbsp;

&nbsp;&nbsp;

`&nbsp;&nbsp;`- 
&nbsp;&nbsp;
In an iPhone 11 (**iOS 17.4.1**)

&nbsp;&nbsp;

&nbsp;&nbsp;- The app opens without any problems

&nbsp;&nbsp;- &nbsp;&nbsp;&nbsp;&nbsp;

&nbsp;&nbsp;- This is the device logs here (filtered for errors)

&nbsp;&nbsp;

&nbsp;&nbsp;
04:19:53 E Ayming Collect(WebKit)[573] : Warning: -[BETextInput attributedMarkedText] is unimplemented04:19:54 E Ayming Collect(RunningBoardServices)[573] : Error acquiring assertion: 04:19:54 E Ayming Collect(WebKit)[573] : 0x112040600 - ProcessAssertion::acquireSync Failed to acquire RBS assertion 'WebProcess NearSuspended Assertion' for process with PID=576, error: (null)04:19:54 E Ayming Collect(WebKit)[573] : Failed to request allowed query parameters from WebPrivacy.

&nbsp;&nbsp;

`&nbsp;&nbsp;`- 
&nbsp;&nbsp;
In the ODC portal logs we can see this set of messages for the successful app launch.

&nbsp;&nbsp;## - 
&nbsp;&nbsp;
&nbsp;&nbsp;

`&nbsp;&nbsp;`- 
&nbsp;&nbsp;
Searching for the error

&nbsp;&nbsp;

&nbsp;&nbsp;- &nbsp;&nbsp;*Failed to load cache manifest OSCacheManifest.plist not found. The file was never created.*&nbsp;&nbsp;

&nbsp;&nbsp;- Past tickets with this error #2753471 , #2931674

&nbsp;&nbsp;- These are O11 tickets and the reasons seem to vary.

&nbsp;&nbsp;- In Confluence some relevant articles

&nbsp;&nbsp;- &nbsp;&nbsp;[&nbsp;&nbsp;](https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/3581411739/Upgrades+over-the-air+OTA+in+O11+-+Overview)&nbsp;&nbsp;[https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/3581411739/Upgrades+over-the-air+OTA+in+O11+-+Overview](https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/3581411739/Upgrades+over-the-air+OTA+in+O11+-+Overview)&nbsp;&nbsp;

&nbsp;&nbsp;- &nbsp;&nbsp;[&nbsp;&nbsp;](https://outsystemsrd.atlassian.net/wiki/spaces/CloudKB/pages/932677743/How+do+the+over-the-air+updates+work)&nbsp;&nbsp;[https://outsystemsrd.atlassian.net/wiki/spaces/CloudKB/pages/932677743/How+do+the+over-the-air+updates+work](https://outsystemsrd.atlassian.net/wiki/spaces/CloudKB/pages/932677743/How+do+the+over-the-air+updates+work)&nbsp;&nbsp;

&nbsp;&nbsp;- &nbsp;&nbsp;&nbsp;&nbsp;

&nbsp;&nbsp;- External article

&nbsp;&nbsp;- &nbsp;&nbsp;[&nbsp;&nbsp;](https://success.outsystems.com/support/troubleshooting/application_runtime/troubleshooting_over_the_air_upgrades/failed_to_load_cache_manifest_filepath_file_not_found_the_file_was_never_created/)&nbsp;&nbsp;[https://success.outsystems.com/support/troubleshooting/application_runtime/troubleshooting_over_the_air_upgrades/failed_to_load_cache_manifest_filepath_file_not_found_the_file_was_never_created/](https://success.outsystems.com/support/troubleshooting/application_runtime/troubleshooting_over_the_air_upgrades/failed_to_load_cache_manifest_filepath_file_not_found_the_file_was_never_created/)&nbsp;&nbsp;

&nbsp;&nbsp;- But again, does not seem relevant here.

&nbsp;&nbsp;- No IMAX entries

&nbsp;&nbsp;- The grafana logs don't reveal much

&nbsp;&nbsp;- &nbsp;&nbsp;[&nbsp;&nbsp;](https://outsystems.grafana.net/d/cdeqzn1jj77cwe/general-troubleshooting?orgId=1&amp;from=1719799200000&amp;to=1719801059000)&nbsp;&nbsp;[https://outsystems.grafana.net/d/cdeqzn1jj77cwe/general-troubleshooting?orgId=1&amp;amp;amp;from=1719799200000&amp;amp;amp;to=1719801059000](https://outsystems.grafana.net/d/cdeqzn1jj77cwe/general-troubleshooting?orgId=1&amp;amp;amp;from=1719799200000&amp;amp;amp;to=1719801059000)&nbsp;&nbsp;

&nbsp;&nbsp;

&nbsp;&nbsp;

`&nbsp;&nbsp;`- 
&nbsp;&nbsp;
From the portal, we can see they do have External Provider Configured

&nbsp;&nbsp;

&nbsp;&nbsp;- &nbsp;&nbsp;&nbsp;&nbsp;

&nbsp;&nbsp;- However when I opened the app, I don't think they are using External Provider to login

&nbsp;&nbsp;- &nbsp;&nbsp;&nbsp;&nbsp;

&nbsp;&nbsp;- It looks like they are using the standard built-in identity provider.

&nbsp;&nbsp;- Attached is the OML

&nbsp;&nbsp;- Ayming Collect.oml

&nbsp;&nbsp;

&nbsp;&nbsp;
`&nbsp;&nbsp;`

`&nbsp;&nbsp;`

`&nbsp;&nbsp;TECH DATA OR ANY OTHER RELEVANT INFO&nbsp;&nbsp;`

`&nbsp;&nbsp;`

- 

`&nbsp;&nbsp;`

- 
`Ring: ga`

- 

`&nbsp;&nbsp;`

- 
`Tenant Id: 33003270-ef13-47c6-90a3-7b7674c8b10e`

- 

`&nbsp;&nbsp;`

- 
`Tenant Prefix: collect-ayming`

- 

`&nbsp;&nbsp;`

- 
`Region: eu-central-1`

- 

`&nbsp;&nbsp;`

- 
`IKG.F4Q.FUQ.NML.PKO.XGL.K5F.AOU`

- 

`&nbsp;&nbsp;`

`&nbsp;&nbsp;`

`&nbsp;&nbsp;&lt;! do not remove this line, this will be used to the trigger Technical Support::Send to R&amp;D - ODC #trigger_send_to_r&amp;d_odc !&gt;&nbsp;&nbsp;`

`&nbsp;&nbsp;`

Attachment(s):

`&nbsp;&nbsp;`
`Ayming Collect Error.mp4 - `[&nbsp;&nbsp;](https://supportoutsystems.zendesk.com/attachments/token/L8VIqoUgMbeIHabSUGGVGOMrO/?name=Ayming+Collect+Error.mp421e92bde9a925e27a31c494cc3747a4ba29db2a2_RequestJSON.json)`&nbsp;&nbsp;`[https://supportoutsystems.zendesk.com/attachments/token/L8VIqoUgMbeIHabSUGGVGOMrO/?name=Ayming+Collect+Error.mp421e92bde9a925e27a31c494cc3747a4ba29db2a2_RequestJSON.json](https://supportoutsystems.zendesk.com/attachments/token/L8VIqoUgMbeIHabSUGGVGOMrO/?name=Ayming+Collect+Error.mp421e92bde9a925e27a31c494cc3747a4ba29db2a2_RequestJSON.json)` - `[&nbsp;&nbsp;](https://supportoutsystems.zendesk.com/attachments/token/yeB6HAPHsN7aV4zYV94GG0mkE/?name=21e92bde9a925e27a31c494cc3747a4ba29db2a2_RequestJSON.jsonAyming)`&nbsp;&nbsp;`[https://supportoutsystems.zendesk.com/attachments/token/yeB6HAPHsN7aV4zYV94GG0mkE/?name=21e92bde9a925e27a31c494cc3747a4ba29db2a2_RequestJSON.jsonAyming](https://supportoutsystems.zendesk.com/attachments/token/yeB6HAPHsN7aV4zYV94GG0mkE/?name=21e92bde9a925e27a31c494cc3747a4ba29db2a2_RequestJSON.jsonAyming)` Collect.oml - `[&nbsp;&nbsp;](https://supportoutsystems.zendesk.com/attachments/token/7EqvY8PtdKaQNJfOj3iKdsmx8/?name=Ayming+Collect.omlservice-file)`&nbsp;&nbsp;`[https://supportoutsystems.zendesk.com/attachments/token/7EqvY8PtdKaQNJfOj3iKdsmx8/?name=Ayming+Collect.omlservice-file](https://supportoutsystems.zendesk.com/attachments/token/7EqvY8PtdKaQNJfOj3iKdsmx8/?name=Ayming+Collect.omlservice-file)` (5).log - `[&nbsp;&nbsp;](https://supportoutsystems.zendesk.com/attachments/token/x5Vbjgd2uC53JyEonhX6lycy2/?name=service-file+%285%29.logAymingCollect.ipa)`&nbsp;&nbsp;`[https://supportoutsystems.zendesk.com/attachments/token/x5Vbjgd2uC53JyEonhX6lycy2/?name=service-file+%285%29.logAymingCollect.ipa](https://supportoutsystems.zendesk.com/attachments/token/x5Vbjgd2uC53JyEonhX6lycy2/?name=service-file+%285%29.logAymingCollect.ipa)` - `[&nbsp;&nbsp;](https://supportoutsystems.zendesk.com/attachments/token/cxiAR9jydE6DxE0wv3pQNwdON/?name=AymingCollect.ipaAyming)`&nbsp;&nbsp;`[https://supportoutsystems.zendesk.com/attachments/token/cxiAR9jydE6DxE0wv3pQNwdON/?name=AymingCollect.ipaAyming](https://supportoutsystems.zendesk.com/attachments/token/cxiAR9jydE6DxE0wv3pQNwdON/?name=AymingCollect.ipaAyming)` Collect_Success.mp4 - `[&nbsp;&nbsp;](https://supportoutsystems.zendesk.com/attachments/token/RQCOjrCIiewwwJDkW5CUkgC2j/?name=Ayming+Collect_Success.mp4)`&nbsp;&nbsp;`[https://supportoutsystems.zendesk.com/attachments/token/RQCOjrCIiewwwJDkW5CUkgC2j/?name=Ayming+Collect_Success.mp4](https://supportoutsystems.zendesk.com/attachments/token/RQCOjrCIiewwwJDkW5CUkgC2j/?name=Ayming+Collect_Success.mp4)`&nbsp;&nbsp;`

`&nbsp;&nbsp;&nbsp;&nbsp;`&nbsp;&nbsp;

July 1  8:18 PM WEST

web

Tiago M. Pereira

Impact has been set: Customer can't load applications using iOS versions between iOS 15 and 16.4

July 2  1:34 AM WEST

web

Rootly

Zendesk Private Comment has been set: ----------------------------------------------**Update to R&amp;D**
Hi Tiago &amp; R&amp;D,Thank you for your response. I would like to ask when this [RAR-2745] will be fixed. Since this customer has users who are still on iOS 15 and iOS 16 and as such are very much affected.Or is there any workaround they can do while this is being addressed.Please let us know.Thank you,__

July 2  1:34 AM WEST

web

Rootly

NEW MESSAGE FROM GLOBAL SUPPORT:

July 2  1:34 AM WEST

web

Rootly

Zendesk Private Comment has been changed to: ------------------------------------------------ This notification was sent from Zendesk Support ticket #3029088 to all linked JIRA issues by Zaman Akbar Mohamed-Akbar. --**Update to R&amp;D**
Hi Tiago &amp; R&amp;D,Thank you for your response. I would like to ask when this &lt;RAR-2745] will be fixed. Since this customer has users who are still on iOS 15 and iOS 16 and as such are very much affected.Or is there any workaround they can do while this is being addressed.Please let us know.Thank you,_[! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_

July 2  1:34 AM WEST

web

Rootly

NEW MESSAGE FROM GLOBAL SUPPORT:

July 2 11:03 AM WEST

web

Tiago M. Pereira

Send ZenDesk private comment has been set: Hello team,  We are currently working on the fix. I'll update the incident as soon as we release the new version. As you know, the version will have to go through the rings until it reaches the ring where the customer has identified the problem.  I'll let you know as soon as we have fixed the issue.  
Best regards,  
Tiago Pereira

July 2 11:03 AM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:
Hello team,  We are currently working on the fix. I'll update the incident as soon as we release the new version. As you know, the version will have to go through the rings until it reaches the ring where the customer has identified the problem.  I'll let you know as soon as we have fixed the issue.  
Best regards,  
Tiago Pereira

July 2 11:03 AM WEST

web

Rootly

Send ZenDesk private comment has been unset

July 2 11:03 AM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:

July 2  1:22 PM WEST

web

Carlos Xavier

Carlos Xavier has been assigned as Engineer

July 2  5:11 PM WEST

web

Carlos Xavier

Send ZenDesk private comment has been set: Hi Support,  The fix has been implemented and will show up in the release notes with the id RAR-2745.  I'll provide the service version number with the fix later once the preliminary validations pass and the version number is set.  Best regards,  
Carlos Xavier

July 2  5:11 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:
Hi Support,  The fix has been implemented and will show up in the release notes with the id RAR-2745.  I'll provide the service version number with the fix later once the preliminary validations pass and the version number is set.  Best regards,  
Carlos Xavier

July 2  5:11 PM WEST

web

Rootly

Send ZenDesk private comment has been unset

July 2  5:11 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:

July 3  5:04 PM WEST

web

Carlos Xavier

Send ZenDesk private comment has been set: Hi Support,  The fix is entering the rings. I'm just waiting for it to reach a ring where I can perform an end-to-end test to ensure everything is working properly. I'll update you then.  Best regards,  
Carlos Xavier

July 3  5:04 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:
Hi Support,  The fix is entering the rings. I'm just waiting for it to reach a ring where I can perform an end-to-end test to ensure everything is working properly. I'll update you then.  Best regards,  
Carlos Xavier

July 3  5:04 PM WEST

web

Rootly

Send ZenDesk private comment has been unset

July 3  5:04 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:

July 4 10:08 AM WEST

web

Carlos Xavier

Send ZenDesk private comment has been set: Hi Support,  We finished our validations. The fix is on version 17.1467.0.  Best regards,  
Carlos Xavier

July 4 10:08 AM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:
Hi Support,  We finished our validations. The fix is on version 17.1467.0.  Best regards,  
Carlos Xavier

July 4 10:08 AM WEST

web

Rootly

Send ZenDesk private comment has been unset

July 4 10:08 AM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:

July 4 10:12 AM WEST

web

Carlos Xavier

Incident has been resolved

July 4 10:12 AM WEST

web

Carlos Xavier

Investigation and troubleshooting findings has been set: There was one third-party library that contained JavaScript syntax not supported in older devices.

July 4 10:12 AM WEST

web

Carlos Xavier

Resolution has been set: We included third-party libraries in the transpilation process to ensure all code is made compatible with the device versions supported by the platform.

July 4 10:12 AM WEST

web

Rootly

Pagerduty Integrations marked the incident as resolved through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q0TO13TV82JLP2). (via Api)