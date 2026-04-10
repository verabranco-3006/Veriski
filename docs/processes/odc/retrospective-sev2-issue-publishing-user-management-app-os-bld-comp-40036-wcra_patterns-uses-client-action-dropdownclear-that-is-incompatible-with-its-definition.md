---
title: Retrospective-SEV2-Issue publishing User Management App (OS-BLD-COMP-40036 : 'WCRA_Patterns' uses client action 'DropdownClear' that is incompatible with its definition
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4277141629/Retrospective-SEV2-Issue+publishing+User+Management+App+OS-BLD-COMP-40036+WCRA_Patterns+uses+client+action+DropdownClear+that+is+incompatible+with+its+definition
confluence_space: RKB
confluence_page_id: 4277141629
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV2-Issue publishing User Management App (OS-BLD-COMP-40036 : 'WCRA_Patterns' uses client action 'DropdownClear' that is incompatible with its definition

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV2

Teams:&nbsp;trueBlueSre&nbsp;trueBlueCompiler Services
#### 🕐 Timestamps
Started At:&nbsp;trueBlueJuly 1 10:53 AM WEST

Mitigated At:&nbsp;trueYellowJuly 10  4:34 PM WEST

Resolved At:&nbsp;trueGreenJuly 10  4:34 PM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/649-issue-publishing-user-management-app-os-bld-comp-40036-wcra_patterns-uses-client-action-dropdownclear-that-is-incompatible-with-its-definition)
[Pagerduty incident](https://outsystems.pagerduty.com/incidents/Q0RGL26ND277BS)

[Slack channel](https://slack.com/app_redirect?channel=C07AK85D528&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3028984)

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

Matthew Hooper

**Stakeholder**

Nuno Bento
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
&lt;li&gt;When attempting to publish the application &quot;User Management&quot;, our colleague is being met with the following errors:&lt;/li&gt;
&lt;/ul&gt;&lt;ol&gt;
&lt;li&gt;&lt;code&gt;'WCRA_Patterns' uses client action 'DropdownClear' that is incompatible with its definition in app or library 'OutSystemsUI'. Consider refreshing dependencies from 'WCRA_Patterns' to 'OutSystemsUI'. (OS-BLD-COMP-40036)&lt;/code&gt;&lt;/li&gt;
&lt;li&gt;&lt;code&gt;The Build operation failed due to a problem in the producer WCRA_Patterns. Please try to republish it before retrying the operation. (OS-BLD-BLD-50001)&lt;/code&gt;&lt;/li&gt;
&lt;li&gt;&lt;code&gt;An error has occurred while building the application (OS-DPL-42202)&lt;/code&gt;&lt;/li&gt;
&lt;/ol&gt;&lt;ul&gt;
&lt;li&gt;This has started to occur since they removed all dependencies of &quot;WCRA_Patterns&quot; from &quot;User Management&quot;; the only way to mitigate it is to add the dependencies back (even though they're not being used at all):&lt;/li&gt;
&lt;li&gt;&lt;p class=&quot;redcarpet&quot;&gt;&lt;img width=&quot;100%&quot; src=&quot;https://supportoutsystems.zendesk.com/attachments/token/1k98WeeQHHZPVSVJHLP3suC1a/?name=image.png&quot;&gt;&lt;/p&gt;&lt;/li&gt;
&lt;li&gt;&lt;p class=&quot;redcarpet&quot;&gt;Weirdly enough, even when they have removed all dependencies of &quot;WCRA_Patterns&quot; from &quot;User Management&quot;, it still appears as a producer incorrectly:&lt;/p&gt;&lt;/li&gt;
&lt;li&gt;&lt;p class=&quot;redcarpet&quot;&gt;&lt;img width=&quot;100%&quot; src=&quot;https://supportoutsystems.zendesk.com/attachments/token/Ik1UVRBt7FVEZTEPU3tY9SmvR/?name=image.png&quot;&gt;&lt;/p&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;p class=&quot;redcarpet&quot;&gt;&lt;strong&gt;IMPACT ON THE CUSTOMER&lt;/strong&gt;&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;They need to deploy updates of the app to QA and Production this week, and they're unwilling to do so with the unused dependencies added as it impacts an impersonation feature they're performing in QA, so right now this is blocking that deployment process.&lt;/li&gt;
&lt;/ul&gt;
&lt;p class=&quot;redcarpet&quot;&gt;&lt;strong&gt;TROUBLESHOOTING STEPS &amp; WORKAROUND&lt;/strong&gt;&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;We came across OS-BLD-COMP-40036/37/38 Runbook (&lt;a target=&quot;_blank&quot; href=&quot;https://outsystemsrd.atlassian.net/wiki/spaces/RDCMOC/pages/3881173332/OS-BLD-COMP-40036+37+38+Runbook&quot;&gt;https://outsystemsrd.atlassian.net/wiki/spaces/RDCMOC/pages/3881173332/OS-BLD-COMP-40036+37+38+Runbook&lt;/a&gt;) which initially seemed relevant, but the fact that this issue only occues when all references have been removed make those steps incompatible, so we haven't been able to suggest much to mitigate this, as there may be a product issue involved.&lt;/li&gt;
&lt;/ul&gt;
&lt;p class=&quot;redcarpet&quot;&gt;&lt;strong&gt;TECH DATA OR ANY OTHER RELEVANT INFO&lt;/strong&gt;&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Ring: ga&lt;/li&gt;
&lt;li&gt;Tenant Id: 7a6b652e-728d-4329-a6f4-998aff1eb508&lt;/li&gt;
&lt;li&gt;Tenant Prefix: wcra&lt;/li&gt;
&lt;li&gt;Region: us-east-1&lt;/li&gt;
&lt;/ul&gt;
&lt;p class=&quot;redcarpet&quot;&gt;&lt;em&gt;&lt;! do not remove this line, this will be used to the trigger&lt;/em&gt; Technical Support::Send to R&amp;D - ODC &lt;em&gt;#trigger_send_to_r&amp;d_odc !&gt;&lt;/em&gt;&lt;/p&gt;
## 📝 RetrospectiveinfoDetails
**Ring:** ga
**System-wide impact:**&nbsp; No
**Tenant ID:** 7a6b652e-728d-4329-a6f4-998aff1eb508
**Tenant Prefix:** wcra
**Routing Error Code:** OS-BLD-COMP
**Product Area:** -
### Impact:
It is being observed in just one tenant.
### Investigation and troubleshooting findings:
Build process was working as expected. Issue is actually with the UX of library versioning confusing the customer.
### Resolution:
N/A
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/649-issue-publishing-user-management-app-os-bld-comp-40036-wcra_patterns-uses-client-action-dropdownclear-that-is-incompatible-with-its-definition)

**Date**

**Source**

**User**

**Event**
July 1 10:50 AM WESTwebRootly
created an alert via
July 1 10:50 AM WESTwebRootly
Rootly created this incident
July 1 10:50 AM WESTwebRootly
In triage date has been set to July 1 10:50 AM WEST
July 1 10:50 AM WESTwebRootly[Slack Channel](https://slack.com/app_redirect?channel=C07AK85D528&amp;team=T041063TZ) has been createdJuly 1 10:51 AM WESTwebRootly
Ring: ga
System-wide impact:  
Tenant ID: 7a6b652e-728d-4329-a6f4-998aff1eb508
Tenant Prefix: wcra
Routing Error Code: OS-BLD-COMP
Product Area: -
July 1 10:51 AM WESTwebRootly[PagerDuty Incident](https://outsystems.pagerduty.com/incidents/Q0RGL26ND277BS) has been created.
📲 Notified Joel Carvalho by push notification.  (via Android)July 1 10:51 AM WESTwebRootlyJoel Filipe Carvalho has been assigned as EngineerJuly 1 10:53 AM WESTwebJoel Filipe Carvalho
Incident has been started
July 1 10:53 AM WESTwebRootly
Pagerduty Integrations acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q0RGL26ND277BS)
July 1 11:47 AM WESTslackJoel Carvalho
This issue is tenant related and is not causing a system-wide impact.
July 1 11:50 AM WESTwebJoel Filipe Carvalho
Summary has been changed to 

&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;

&nbsp;&nbsp;
&nbsp;&nbsp;**CONSIDERATIONS BEFORE PERFORMING THE ESCALATION TO R&amp;D (MANDATORY)**
&nbsp;&nbsp;
None of the below points should be overlooked. Failure to do so may imply unnecessary effort.

&nbsp;&nbsp;
&nbsp;&nbsp;
Ensure the ticket has been **categorized**, otherwise, the R&amp;D escalation will go unnoticed and not be worked on!
&nbsp;&nbsp;
&nbsp;&nbsp;**1.** For **Incidents**, the **IMAX** was consulted **beforehand** on which:

&nbsp;&nbsp;

&nbsp;&nbsp;- No incident models were found for the reported symptoms **OR**
&nbsp;&nbsp;

&nbsp;&nbsp;- The incident model did not solve the issue **OR**
&nbsp;&nbsp;

&nbsp;&nbsp;- The next step indicated in the Incident Model is an escalation to R&amp;D.

&nbsp;&nbsp;**2.** For **Questions**, the ChatODC on the **Slack channel** didn't return an acceptable answer.

&nbsp;&nbsp;**3.** Any other requests that explicitly indicate an R&amp;D escalation is needed.

&nbsp;&nbsp;**4**. **Incident impact assessment** was based on the **prioritization scoring matrix**.

&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;

&nbsp;&nbsp;
&nbsp;&nbsp;**R&amp;D ESCALATION FORM**
&nbsp;&nbsp;
Section comments can be removed for R&amp;D easier interpretation.
&nbsp;&nbsp;
&nbsp;&nbsp;**ISSUE DESCRIPTION AND HOW TO REPRODUCE**&nbsp;&nbsp;

&nbsp;&nbsp;

&nbsp;&nbsp;- When attempting to publish the application &quot;User Management&quot;, our colleague is being met with the following errors:

&nbsp;&nbsp;
&nbsp;&nbsp;
- &nbsp;&nbsp;`'WCRA_Patterns' uses client action 'DropdownClear' that is incompatible with its definition in app or library 'OutSystemsUI'. Consider refreshing dependencies from 'WCRA_Patterns' to 'OutSystemsUI'. (OS-BLD-COMP-40036)`&nbsp;&nbsp;
- &nbsp;&nbsp;`The Build operation failed due to a problem in the producer WCRA_Patterns. Please try to republish it before retrying the operation. (OS-BLD-BLD-50001)`&nbsp;&nbsp;
- &nbsp;&nbsp;`An error has occurred while building the application (OS-DPL-42202)`&nbsp;&nbsp;

- This has started to occur since they removed all dependencies of &quot;WCRA_Patterns&quot; from &quot;User Management&quot;; the only way to mitigate it is to add the dependencies back (even though they're not being used at all):
- &nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;
- &nbsp;&nbsp;
Weirdly enough, even when they have removed all dependencies of &quot;WCRA_Patterns&quot; from &quot;User Management&quot;, it still appears as a producer incorrectly:
&nbsp;&nbsp;
- &nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;

&nbsp;&nbsp;**IMPACT ON THE CUSTOMER**&nbsp;&nbsp;

- They need to deploy updates of the app to QA and Production this week, and they're unwilling to do so with the unused dependencies added as it impacts an impersonation feature they're performing in QA, so right now this is blocking that deployment process.

&nbsp;&nbsp;**TROUBLESHOOTING STEPS &amp; WORKAROUND**&nbsp;&nbsp;

- We came across OS-BLD-COMP-40036/37/38 Runbook ([https://outsystemsrd.atlassian.net/wiki/spaces/RDCMOC/pages/3881173332/OS-BLD-COMP-40036+37+38+Runbook](https://outsystemsrd.atlassian.net/wiki/spaces/RDCMOC/pages/3881173332/OS-BLD-COMP-40036+37+38+Runbook)) which initially seemed relevant, but the fact that this issue only occues when all references have been removed make those steps incompatible, so we haven't been able to suggest much to mitigate this, as there may be a product issue involved.

&nbsp;&nbsp;**TECH DATA OR ANY OTHER RELEVANT INFO**&nbsp;&nbsp;

- Ring: ga
- Tenant Id: 7a6b652e-728d-4329-a6f4-998aff1eb508
- Tenant Prefix: wcra
- Region: us-east-1

&nbsp;&nbsp;*&nbsp;&nbsp; Technical Support::Send to R&amp;D - ODC #trigger_send_to_r&amp;d_odc !&gt;&nbsp;&nbsp;*&nbsp;&nbsp;
&nbsp;&nbsp;July 1 11:50 AM WESTwebJoel Filipe Carvalho
Teams has been added: CompilerServices
July 1 11:50 AM WESTwebJoel Filipe CarvalhoSystem-wide impact has been set: NoJuly 1 11:50 AM WESTwebJoel Filipe CarvalhoImpact has been set: It is being observed in just one tenant.July 1 11:57 AM WESTwebJo&atilde;o Lu&iacute;s AlmeidaJo&atilde;o Lu&iacute;s Almeida has been assigned as EngineerJuly 1 12:05 PM WESTwebJo&atilde;o Lu&iacute;s AlmeidaSend ZenDesk private comment has been set: Hello team,A correction on the message I had sent through Jira,
The &quot;User Management&quot; application is still consuming &quot;WCRA_Patterns&quot;, through &quot;Common Libraries&quot;.
That is, &quot;User Management&quot; consumes &quot;Common Libraries&quot; which in turn consumes &quot;WCRA_Patterns&quot;.Since there's an available workaround and no indication of a product issue, could we please review the priority?Best regards,
Jo&atilde;o Lu&iacute;s AlmeidaJuly 1 12:05 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hello team,A correction on the message I had sent through Jira,
The &quot;User Management&quot; application is still consuming &quot;WCRA_Patterns&quot;, through &quot;Common Libraries&quot;.
That is, &quot;User Management&quot; consumes &quot;Common Libraries&quot; which in turn consumes &quot;WCRA_Patterns&quot;.Since there's an available workaround and no indication of a product issue, could we please review the priority?Best regards,
Jo&atilde;o Lu&iacute;s Almeida
July 1 12:05 PM WESTwebRootlySend ZenDesk private comment has been unsetJuly 1 12:05 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

July 1 12:06 PM WESTwebJoel Filipe CarvalhoSwarm has been set: Compiler ServicesJuly 1 12:06 PM WESTwebRootly
Pagerduty Integrations added Matt Hooper as responder in [PagerDuty](https://outsystems.pagerduty.com/incidents/Q0RGL26ND277BS)
July 1 12:08 PM WESTwebRootly
Matt Hooper joined this [PagerDuty](https://outsystems.pagerduty.com/incidents/Q0RGL26ND277BS) incident.
July 1 12:38 PM WESTslackmatthew.hooper
So I've been speaking with @Gon&ccedil;alo Silva from global support about this issue, we agreed that this is an issue with the way their app is referencing directly/indirectly different revisions of Patterns, some of which have incompatible references with OSUI. He is communicating this to the customer as a &quot;workaround&quot; although it is not really a workaround since the platform is behaving as expected, the customer is just confused about how to resolve the validation errors they are getting in the IDE.
July 1 12:45 PM WESTwebJo&atilde;o Lu&iacute;s AlmeidaMatthew Hooper has been assigned as EngineerJuly 8 11:25 AM WESTwebMatthew HooperNuno Bento has been assigned as StakeholderJuly 10  3:36 PM WESTwebRootlyZenDesk Event Type has been set: solvedJuly 10  3:37 PM WESTwebRootly
The Global Support team marked this incident as closed in ZenDesk.
July 10  4:34 PM WESTwebMatthew Hooper
Incident has been resolved
July 10  4:34 PM WESTwebMatthew HooperInvestigation and troubleshooting findings has been set: Build process was working as expected. Issue is actually with the UX of library versioning confusing the customer.July 10  4:34 PM WESTwebMatthew HooperResolution has been set: N/A