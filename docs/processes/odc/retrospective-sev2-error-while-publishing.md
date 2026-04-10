---
title: Retrospective-SEV2-Error while publishing
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4281696422/Retrospective-SEV2-Error+while+publishing
confluence_space: RKB
confluence_page_id: 4281696422
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV2-Error while publishing

## 📘 Overview
Author:&nbsp;Rootlytrue

Severity:&nbsp;SEV2Redtrue

Teams:&nbsp;Model Bluetrue
#### 🕐 Timestamps
Started At:&nbsp;July 2  2:38 PM WESTBluetrue

Mitigated At:&nbsp;July 12  2:06 PM WESTYellowtrue

Resolved At:&nbsp;July 12  2:06 PM WESTGreentrue
#### 🔗 Links
[Incident Page](https://rootly.com/account/incidents/658-error-while-publishing)

[Pagerduty incident](https://outsystems.pagerduty.com/incidents/Q1T9SU3IMEBPN1)

[Slack channel](https://slack.com/app_redirect?channel=C07AH8TLJHL&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3030502)

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

Nuno Rego
#### Summary
----------------------------------------------**CONSIDERATIONS BEFORE PERFORMING THE ESCALATION TO R&amp;D (MANDATORY)**
None of the below points should be overlooked. Failure to do so may imply unnecessary effort.* * *
Ensure the ticket has been **categorized**, otherwise, the R&amp;D escalation will go unnoticed and not be worked on!**1.** For **Incidents**, the **IMAX** was consulted **beforehand** on which:- No incident models were found for the reported symptoms **OR**
- The incident model did not solve the issue **OR**
- The next step indicated in the Incident Model is an escalation to R&amp;D.
**2.** For **Questions**, the ChatODC on the **Slack channel** didn't return an acceptable answer.
**3.** Any other requests that explicitly indicate an R&amp;D escalation is needed.
**4**. **Incident impact assessment** was based on the **prioritization scoring matrix**.* * ***R&amp;D ESCALATION FORM**
Section comments can be removed for R&amp;D easier interpretation.**ISSUE DESCRIPTION AND HOW TO REPRODUCE**- When attempting to publish an application, our customer is being met with the following error:- `Http Error Code: 500 - Internal Server Error. Title: Unable to load ESpace from input Oml`- `Error Code: OS-APPS-50004`- `Detail: Unable to load ESpace from input Oml`- `TraceId: 00-be6325ba77e9cd2002f266aa26472b84-a8fe9f422818649d-01`- This is occurring when attempting to publish a new revision of the &quot;Clinical Trials Solution&quot; app (we've included it in attachments).**IMPACT ON THE CUSTOMER**- This is blocking development on this application as they're completely unable to publish it, hence High/Sev-2 priority is appropriate.**TROUBLESHOOTING STEPS &amp; WORKAROUND**- We had a case in the past (it never reached you) where another customer successfully mitigated this exact error by republishing an older version of the affected application with a dummy change. That was not effective in this customer's case.- By using the Trace ID, we also got this result (https://outsystems.grafana.net/explore?schemaVersion=1&amp;panes=%7B%22ko7%22:%7B%22datasource%22:%22grafanacloud-outsystemstest-traces%22,%22queries%22:%5B%7B%22refId%22:%22A%22,%22datasource%22:%7B%22type%22:%22tempo%22,%22uid%22:%22grafanacloud-outsystemstest-traces%22%7D,%22queryType%22:%22traceql%22,%22limit%22:20,%22tableType%22:%22traces%22,%22query%22:%22be6325ba77e9cd2002f266aa26472b84%22%7D%5D,%22range%22:%7B%22from%22:%221719909000000%22,%22to%22:%221719909540000%22%7D%7D%7D&amp;orgId=1), but it is difficult to understand. The error seems to be occurring in the step to load the eSpace in the Application Versioning Service, however I'm not sure what we can do with this information.- Can you help us understand what's causing this and how to address it, both right now and for future occurrences?**TECH DATA OR ANY OTHER RELEVANT INFO**- Ring: ga
- Tenant Id: 7aa1ea7a-8e70-4dd6-84a3-e0c152a6c929
- Tenant Prefix: cr-digital
- Region: eu-central-1_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 Retrospective### Details
**Ring:** ga
**System-wide impact:**&nbsp; 
**Tenant ID:** 7aa1ea7a-8e70-4dd6-84a3-e0c152a6c929
**Tenant Prefix:** cr-digital
**Routing Error Code:** OS-APPS
**Product Area:** Model
### Impact:
The customer was unable to publish his app.
### Investigation and troubleshooting findings:
The problem was caused due to the Model API not loading the referrers fragment when the &lsquo;read only&rsquo; and &lsquo;skip upgrades&rsquo; flags are set, which is how AVS loads models.
### Resolution:
The customer had to wait for a new GA version to be promoted before he could publish his App.
## Tasks performed during incident resolution:
- 
Attempted to recover the model;

- 
Fixed the underlying issue in RDMST-3024ef8955cb-cb21-32a7-b692-01ace42388d6System Jira ;

## Executive Summary
On July 2nd at 2:13 PM (WEST) the customer submitted a support ticket reporting that he was unable to publish his app. Investigation concluded that a version of AVS that consumed a more recent version of Model API (&gt;13.579.0) no longer had this issue. This version reached GA in the 12th of July, unblocking the publish operation for this specific App.

This situation represents a downtime of the development environment of about 10 days.

From a technical perspective, the problem was caused due to the Model API not loading the referrers fragment when the &lsquo;read only&rsquo; and &lsquo;skip upgrades&rsquo; flags are set, which is how AVS loads models.

As a consequence of this incident, we have determined to:

- 
We need to figure out why &gt;13.579.0 fixes the problem, but should we? Maybe it&rsquo;s a big investment.

- 
Let&rsquo;s investigate this if it happens again.

## Root Causes 
- 
✅ Model API not loading the referrers fragment when the &lsquo;read only&rsquo; and &lsquo;skip upgrades&rsquo; flags are set, which is how AVS loads models;

- 
Addressed in [https://github.com/OutSystems/OutSystems.Model/pull/1652](https://github.com/OutSystems/OutSystems.Model/pull/1652) ;

[Guidelines](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4144496679/Incident+Retrospectives+-+Playbook#STEP-1---Perform-the-Root-Cause-Analysis)

If the customer needs formal RCA, please fill out the following field with the document URL

[Please follow these instructions and place the RCA URL in the field below.](https://docs.google.com/document/d/13rXmBsOJh73nV2D6Z17SIBGBu2HOTWty5ddsvU000JM/edit#heading=h.bqxasxszr5q)

RCA URL

&lt;Place the URL of the customer RCA here if you have created one&gt;
## ⌛ Timeline
[View on Rootly](https://rootly.com/account/incidents/658-error-while-publishing)

**Date**

**Source**

**User**

**Event**

July 2  2:13 PM WEST

web

Rootly

created an alert via

July 2  2:13 PM WEST

web

Rootly

Rootly created this incident

July 2  2:13 PM WEST

web

Rootly

In triage date has been set to July 2  2:13 PM WEST

July 2  2:13 PM WEST

web

Rootly

[Slack Channel](https://slack.com/app_redirect?channel=C07AH8TLJHL&amp;team=T041063TZ) has been created

July 2  2:14 PM WEST

web

Rootly

[PagerDuty Incident](https://outsystems.pagerduty.com/incidents/Q1T9SU3IMEBPN1) has been created.

📧 Notified Ricardo Duarte by email.

&nbsp;&nbsp;

📲 Notified Ricardo Duarte by push notification.  (via Android)

&nbsp;&nbsp;

📱 Notified Ricardo Duarte by SMS.

&nbsp;&nbsp;

📞 Notified Ricardo Duarte by phone.

July 2  2:14 PM WEST

web

Rootly

Ring: ga
System-wide impact:  
Tenant ID: 7aa1ea7a-8e70-4dd6-84a3-e0c152a6c929
Tenant Prefix: cr-digital
Routing Error Code: OS-APPS
Product Area: -

July 2  2:14 PM WEST

web

Rootly

Ricardo Duarte has been assigned as Engineer

July 2  2:14 PM WEST

web

Rootly

Ricardo Duarte acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q1T9SU3IMEBPN1). (via Phone)

July 2  2:38 PM WEST

web

Ricardo Duarte

Incident has been started

July 2  2:38 PM WEST

web

Rootly

Pagerduty Integrations acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q1T9SU3IMEBPN1). (via Phone)

July 2  2:42 PM WEST

web

Ricardo Duarte

Teams has been added: [Model ](/account/teams/model/status)

July 2  2:42 PM WEST

web

Ricardo Duarte

Teams has been removed: [Neo Platform Theseus](/account/teams/neo-platform-theseus/status)

July 2  2:47 PM WEST

web

Ricardo Duarte

Nuno Rego has been assigned as Engineer

July 2  

2:47&rarr;6:20 PM 

WEST

R&amp;D

⚙ Investigating ⚙

- 
Unable to reproduce in IDE

- 
Unable to reproduce in Model API

July 2  6:20 PM WEST

R&amp;D

R&amp;D Requested that the customer cut and paste the aggregate that was in the original stack trace before publishing.

We're still investigating the possible root cause which might take a while given that we are not able to reproduce the issue even with customer's model. However, we were able to determine that the issue is being caused by a possible fault in an algorithm that accounts for a resulting type of an aggregate called 'GetCtrColabStudies'. Would it be possible to ask the user to cut this aggregate, paste it and then attempt to publish his app again?

July 3  9:39 AM WEST

web

Support

The proposed workaround did not work

Hey team, the customer tried the suggested workaround and, unfortunately, it wasn't successful

!Here's the OML file after they applied these steps in case it'll help: Clinical Trials Solution With test Fix.omlLet us know if you need anything else from us or the customer. Thanks in advance

July 3  11:24 AM WEST

R&amp;D

We attempted to recover the model.

We are still investigating. We've applied a recovery procedure to the customer's model and we've linked it in JIRA with the name &quot;1719913255000000000__Clinical Trials Solution_Error_Recovered.oml&quot;. May we ask the customer to attempt to publish that version?

In the case that it does not work we have the theory that we might not be able to reproduce because the model we have does not have refreshed dependencies. Could we confirm with the user if he could send us a version of the app after its dependencies are, indeed, refreshed?

July 3  1:28 PM WEST

web

Support

The recovered model had issues during load in ODC Studio

The customer is unable to load the OML provided; when they try, they get the following error:! Here's a text file with the full error message: Unrecoverable exception.txt. 

We tried opening the file and got the exact same error; how can the customer load this file to understand if publishing it will mitigate this issue? Thanks again for the help!

July 3  2:10 PM WEST

R&amp;D

We apologized and continued investigating.

Please relay our apologies to the customer. We'll investigate this issue as it may be related with the original problem, which is good news. I'll let you know when we have more information.

July 3  4:45 PM WEST

R&amp;D

We recovered the app again &ndash;  this time ensuring the load worked &ndash; and sent the model to the customer to see if he was unblocked.

We think we might've successfully recovered the app, can you ask the customer to attempt to publish the oml file linked with the name &quot;Clinical Trials Solution (Recovered).oml&quot;?

The recovery uncovered an issue in an inline mapping of the &quot;CreateEmailUserPass&quot; execute node of the &quot;Create_EmailUserPass&quot; server action. In doing that a new validation error appeared in the app prompting the user to fill a valid expression for the attribute 'Id', in that same execute action node.
Please let us know if this unblocks the customer.

July 4 09:13 AM WEST

Support

The issue persisted.

Unfortunately, even after fixing the &quot;ID&quot; field of the &quot;CreateEmailUserPass&quot; node, the issue persists; as we can see in the screenshot, they filled it in with &quot;NullIdentifier()&quot;, can you confirm if this was a valid expression?

July 4 2:04 PM WEST

R&amp;D

Whilst investigating, we asked again for a version of the app with updated dependencies.

We're still investigating. A while back we reached out to ask if the user could provide us with a version of his app after refreshing all dependencies, would this be possible?

July 4  3:12 PM WEST

web

Support

We received the updated Model

Hey team! Here's the OML file after the user performed a check for dependency updates: 1720032588495_Clinical Trials Solution (Recovered and Dependency Checks Done).oml We've also attached it to the jira manually just in case.Let us know if you need anything else from us

July 4  4:21 PM WEST

R&amp;D

We sent the recovered version of the updated model over to support.

We've just linked a recovered version of the app that the customer sent named &quot;Clinical Trials Solution (Updated Dependencies &amp; Recovered).oml&quot;. Please relay to the customer that he should attempt to publish it. In the case that it does not work we might have to look into the producers of that app. We are grateful for their patience and hope they understand we are prioritizing this incident within the team making sure we unblock them as soon as possible.

July 4  4:37 PM WEST

Support

Support said they tried to publish in their tenant and it failed with the customer&rsquo;s error. This was the first time we figured out we could test this internally.

We tried publishing the latest revision &quot;Clinical Trials Solution (Updated Dependencies &amp; Recovered).oml&quot; on our own sandbox and we got the exact same error that the customer has been getting from the beginning; is it still worth it to share it with the customer in the off-chance that they will no longer get the error, or is it more likely that they'll continue to get this error, as we just did? If so, let us know what you'll need from us regarding the app's producers.

July 4  5:23 PM WEST

R&amp;D

We started investigating a bit more as we could now reproduce the issue reliably in ODC Studio

We're still investigating. With the help of Gon&ccedil;alo Silva we were able to reliably reproduce the issue locally and we've made some progress in understanding the possible problems that might be at play here, even if we don't fully understand, yet, how to provide a workaround. It seems that ODC Studio is forcing a recalculation of the referrer information in the App. This recalculation seems to lead to a wrongful state. When the App is published ODC's package versioning system fails to load the App's referrer information because of that. Our current goal is to understand where this recalculation is occurring and why it is leading to wrong state.
We'll keep you posted.

July 8  4:40 PM WEST

R&amp;D

We figured out an updated model api version did not have this problem and updated support as to when this issue should no longer occur.

We're still investigating on how to provide a workaround.
It seems that this issue no longer occurs in the EA version of ODC. We expect that, if all goes well, this version will be promoted to GA next Thursday the 11th of July, before 9 Am (UTC/GMT+1).

In the meantime we were able to conclude that the issue stems from the way we handle the loading of an App using a very specific configuration, which is the way how our ODC Version Management service does it. What happens here is that we are not loading the referrer information from the model but calculating it on demand during the load itself. Due to this missing information we crash explicitly as the load mechanism is instantiating the App's aggregates with their calculated resulting types and requiring the old ones to be deleted (accessing referrer information that does not exist, hence the crash).

We'll keep working on a possible workaround. In the meantime please inform the customer about the possibility of a fix next Thursday.

July 9 7:48 AM 

R&amp;D

Created task to fix root cause
RDMST-3024ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

July 11 10:05 AM WEST

R&amp;D

There were some infrastructure issues that delayed the update.

The new version was not promoted to GA yet (some infrastructure issues). It is currently being promoted as we speak. We'll let you know when it is available as we'll test it with the customer's model to ensure a higher degree of certainty that the problem is indeed fixed.
Please relay our apologies to the customer. We are working hard to get this out as soon as possible.

July 11 3:19 PM WEST

R&amp;D

More infrastructure issues.

Unfortunately, even after retrying, there was a failure to promote the new GA version due to an unrelated issue. We are working with the ODC Cloud Services teams to help solve this as soon as possible. Apologies for the delay.

July 12 7:34 AM

R&amp;D

Root cause fix merged

[https://github.com/OutSystems/OutSystems.Model/pull/1652](https://github.com/OutSystems/OutSystems.Model/pull/1652) 

July 12 9:54 PM WEST

R&amp;D

The update reached GA 🎉

The new version already reached GA. I attempted to publish the oml in the tenant you provided us and we no longer get that error. Can you ask the customer to try to publish?

July 12 11:44 AM WEST

web

Rootly

ZenDesk Event Type has been set: solved

July 12 11:44 AM WEST

web

Rootly

The Global Support team marked this incident as closed in ZenDesk.

July 12  2:06 PM WEST

web

Nuno Rego

Incident has been resolved

July 12  2:06 PM WEST

web

Nuno Rego

Impact has been set: Customer was unblocked

July 12  2:06 PM WEST

web

Nuno Rego

Resolution has been set: The customer had to wait for a new GA version to be promoted before he could publish his App.