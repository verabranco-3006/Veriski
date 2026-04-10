---
title: Retrospective-SEV3-Tooltip not working
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4272685100/Retrospective-SEV3-Tooltip+not+working
confluence_space: RKB
confluence_page_id: 4272685100
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV3-Tooltip not working

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV3

Teams:&nbsp;trueBlueUi Components
#### 🕐 Timestamps
Started At:&nbsp;trueBlueJuly 8  8:09 AM WEST

Mitigated At:&nbsp;trueYellowJuly 9  9:25 AM WEST

Resolved At:&nbsp;trueGreenJuly 9  9:25 AM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/683-tooltip-not-working)
[Slack channel](https://slack.com/app_redirect?channel=C07BDEV5LUB&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3032394)

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

Bernardo Cardoso

**Commander**

Gon&ccedil;alo Martins
#### Summary
&lt;hr&gt;
&lt;p class=&quot;redcarpet&quot;&gt;&lt;strong&gt;ISSUE DESCRIPTION AND HOW TO REPRODUCE&lt;/strong&gt;&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Hello team, it has been reported that after upgrading OSUI to version 2.19.1, the tooltip have stopped working as expected since it does not open properly when its StartsOpen property is set as True&lt;/li&gt;
&lt;/ul&gt;
&lt;p class=&quot;redcarpet&quot;&gt;&lt;strong&gt;IMPACT ON THE CUSTOMER&lt;/strong&gt;&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;No major impact but this behavior is unexpected and it can slow down the development&lt;/li&gt;
&lt;/ul&gt;
&lt;p class=&quot;redcarpet&quot;&gt;&lt;strong&gt;TROUBLESHOOTING STEPS &amp; WORKAROUND&lt;/strong&gt;&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;I have prepared this screen where you will be able to appreciate two different faulty scenarios, and also some normal working ones&lt;ol&gt;
&lt;li&gt;When having a normal tooltip to open OnHover, works normally&lt;/li&gt;
&lt;li&gt;When having the tooltip with &lt;code&gt;StartsOpen = True&lt;/code&gt; and Triggered by &lt;code&gt;OnClick&lt;/code&gt;, it does not work, unless you click on the third tooltip or most likely on any other with the &lt;code&gt;StartsOpen = True&lt;/code&gt;
&lt;/li&gt;
&lt;li&gt;This one has the &lt;code&gt;StartsOpen = True&lt;/code&gt;, when hovering the first time, it does not work until you get out of the element and hover again, Kinda needing to reset&lt;/li&gt;
&lt;li&gt;This one works normally when hovering &lt;code&gt;StartsOpen = True&lt;/code&gt;
&lt;/li&gt;
&lt;/ol&gt;
&lt;/li&gt;
&lt;li&gt;In the attached video you can see this behavior as well as the behavior of the elements and their styles, we can also notice that the elements with &lt;code&gt;StartsOpen = True&lt;/code&gt; has some styles that should load the tooltip opened&lt;/li&gt;
&lt;/ul&gt;
&lt;p class=&quot;redcarpet&quot;&gt;&lt;strong&gt;TECH DATA OR ANY OTHER RELEVANT INFO&lt;/strong&gt;
&lt;br&gt;Ring: ga
&lt;br&gt;Tenant Id: d2c77266-490f-4d9f-a181-2f05ba40f0b6
&lt;br&gt;Tenant Prefix: sporttv
&lt;br&gt;Region: eu-central-1
&lt;br&gt;8SV.Z26.5B4.8X1.VF0.73S.7F8.A6Z&lt;/p&gt;&lt;p class=&quot;redcarpet&quot;&gt;Sample app and link to the screen attached.
&lt;br&gt;Video Attached.&lt;/p&gt;&lt;p class=&quot;redcarpet&quot;&gt;&lt;em&gt;&lt;! do not remove this line, this will be used to the trigger&lt;/em&gt; Technical Support::Send to R&amp;D - ODC &lt;em&gt;#trigger_send_to_r&amp;d_odc !&gt;&lt;/em&gt;&lt;/p&gt;&lt;p class=&quot;redcarpet&quot;&gt;Attachment(s):
&lt;br&gt;SandApp -Tooltip issue - Screen1.oml - &lt;a href=&quot;https://supportoutsystems.zendesk.com/attachments/token/hMs6dKsThyfFR6DONTRst4SNP/?name=SandApp+-Tooltip+issue+-+Screen1.oml&quot;&gt;https://supportoutsystems.zendesk.com/attachments/token/hMs6dKsThyfFR6DONTRst4SNP/?name=SandApp+-Tooltip+issue+-+Screen1.oml&lt;/a&gt;&lt;/p&gt;
## 📝 RetrospectiveinfoDetails
**Ring:** ga
**System-wide impact:**&nbsp; 
**Tenant ID:** d2c77266-490f-4d9f-a181-2f05ba40f0b6
**Tenant Prefix:** sporttv
**Routing Error Code:** N/A
**Product Area:** Phoenix::Application Runtime::Starter Apps::OutSystems UI
### Impact:
The StartsOpen parameter no longer works in runtime and the Tooltip will always appear closed by default.
### Investigation and troubleshooting findings:
The issue is present on both O11 and ODC. 
### Resolution:
A fix will be done on the OutSystems UI, to be available on version 2.19.2.
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/683-tooltip-not-working)

**Date**

**Source**

**User**

**Event**
July 5 10:20 PM WESTwebRootly
created an alert via
July 5 10:20 PM WESTwebRootly
Rootly created this incident
July 5 10:20 PM WESTwebRootly
In triage date has been set to July 5 10:20 PM WEST
July 8  7:59 AM WESTwebBernardo CardosoBernardo Cardoso has been assigned as EngineerJuly 8  8:08 AM WESTwebRootly[Slack Channel](https://slack.com/app_redirect?channel=C07BDEV5LUB&amp;team=T041063TZ) has been createdJuly 8  8:09 AM WESTwebBernardo Cardoso
Incident has been started
July 8  8:30 AM WESTwebBernardo CardosoGon&ccedil;alo Martins has been assigned as CommanderJuly 8  9:24 AM WESTwebBernardo Cardoso
We can confirme this is indeed an issue on Tooltip, introduced on the OutSystems UI 2.19.1.
July 8  9:25 AM WESTwebBernardo Cardoso
We created a task on our backlog to fix this issue: https://outsystemsrd.atlassian.net/browse/ROU-10909. This will be available on the next release of OutSystems UI (no dates to share yet).
July 8  9:26 AM WESTwebBernardo Cardoso
Summary has been changed to 

&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;

&nbsp;&nbsp;
&nbsp;&nbsp;**ISSUE DESCRIPTION AND HOW TO REPRODUCE**&nbsp;&nbsp;

&nbsp;&nbsp;

&nbsp;&nbsp;- Hello team, it has been reported that after upgrading OSUI to version 2.19.1, the tooltip have stopped working as expected since it does not open properly when its StartsOpen property is set as True

&nbsp;&nbsp;

&nbsp;&nbsp;
&nbsp;&nbsp;**IMPACT ON THE CUSTOMER**&nbsp;&nbsp;

&nbsp;&nbsp;

&nbsp;&nbsp;- No major impact but this behavior is unexpected and it can slow down the development

&nbsp;&nbsp;

&nbsp;&nbsp;
&nbsp;&nbsp;**TROUBLESHOOTING STEPS &amp; WORKAROUND**&nbsp;&nbsp;

&nbsp;&nbsp;

&nbsp;&nbsp;- I have prepared this screen where you will be able to appreciate two different faulty scenarios, and also some normal working ones
&nbsp;&nbsp;
&nbsp;&nbsp;
- When having a normal tooltip to open OnHover, works normally
- When having the tooltip with `StartsOpen = True` and Triggered by `OnClick`, it does not work, unless you click on the third tooltip or most likely on any other with the `StartsOpen = True`
- This one has the `StartsOpen = True`, when hovering the first time, it does not work until you get out of the element and hover again, Kinda needing to reset
- This one works normally when hovering `StartsOpen = True`

- In the attached video you can see this behavior as well as the behavior of the elements and their styles, we can also notice that the elements with `StartsOpen = True` has some styles that should load the tooltip opened
&nbsp;&nbsp;
&nbsp;&nbsp;

&nbsp;&nbsp;**TECH DATA OR ANY OTHER RELEVANT INFO**
&nbsp;&nbsp;
Ring: ga

&nbsp;&nbsp;
Tenant Id: d2c77266-490f-4d9f-a181-2f05ba40f0b6

&nbsp;&nbsp;
Tenant Prefix: sporttv

&nbsp;&nbsp;
Region: eu-central-1

&nbsp;&nbsp;
8SV.Z26.5B4.8X1.VF0.73S.7F8.A6Z
&nbsp;&nbsp;
Sample app and link to the screen attached.

&nbsp;&nbsp;
Video Attached.
&nbsp;&nbsp;
&nbsp;&nbsp;*&lt;! do not remove this line, this will be used to the trigger* Technical Support::Send to R&amp;D - ODC *#trigger_send_to_r&amp;d_odc !&gt;*&nbsp;&nbsp;
&nbsp;&nbsp;
Attachment(s):

&nbsp;&nbsp;
SandApp -Tooltip issue - Screen1.oml - [&nbsp;&nbsp;](https://supportoutsystems.zendesk.com/attachments/token/hMs6dKsThyfFR6DONTRst4SNP/?name=SandApp+-Tooltip+issue+-+Screen1.oml)&nbsp;&nbsp;[https://supportoutsystems.zendesk.com/attachments/token/hMs6dKsThyfFR6DONTRst4SNP/?name=SandApp+-Tooltip+issue+-+Screen1.oml](https://supportoutsystems.zendesk.com/attachments/token/hMs6dKsThyfFR6DONTRst4SNP/?name=SandApp+-Tooltip+issue+-+Screen1.oml)&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;July 8  9:26 AM WESTwebBernardo CardosoImpact has been set: The StartsOpen parameter no longer works in runtime and the Tooltip will always appear closed by default.July 8  9:26 AM WESTwebBernardo CardosoInvestigation and troubleshooting findings has been set: The issue is present on both O11 and ODC. July 8  9:28 AM WESTwebBernardo CardosoSend ZenDesk private comment has been set: Hi Team,
&nbsp;&nbsp;
We confirm this is a defect on OutSystems UI and created a bug on backlog, to be added on the next release (no dates yet to share).
&nbsp;&nbsp;
Best regards,
Bernardo CardosoJuly 8  9:28 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

Hi Team,
&nbsp;&nbsp;
We confirm this is a defect on OutSystems UI and created a bug on backlog, to be added on the next release (no dates yet to share).
&nbsp;&nbsp;
Best regards,
Bernardo CardosoJuly 8  9:28 AM WESTwebRootlySend ZenDesk private comment has been unsetJuly 8  9:28 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

July 8 11:33 AM WESTwebGon&ccedil;alo Martins
Hello Team!
Just to complement  the previous information, the bug code for future reference on the release notes is ROU-10909.
July 9  9:25 AM WESTwebBernardo Cardoso
Incident has been resolved
July 9  9:25 AM WESTwebBernardo CardosoResolution has been set: A fix will be done on the OutSystems UI, to be available on version 2.19.2.