---
title: Retrospective-SEV2-The apps pages are not loading
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4307386650/Retrospective-SEV2-The+apps+pages+are+not+loading
confluence_space: RKB
confluence_page_id: 4307386650
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV2-The apps pages are not loading

## 📘 Overview
Author:&nbsp;Rootlytrue

Severity:&nbsp;SEV2Redtrue

Teams:&nbsp;Client RuntimeBluetrue
#### 🕐 Timestamps
Started At:&nbsp;July 23 11:01 AM WESTBluetrue

Mitigated At:&nbsp;July 24  2:40 PM WESTYellowtrue

Resolved At:&nbsp;July 24  2:40 PM WESTGreentrue
#### 🔗 Links
[Incident Page](https://rootly.com/account/incidents/747-the-apps-pages-are-not-loading)

[Pagerduty incident](https://outsystems.pagerduty.com/incidents/Q1QVNLZW4KXL2P)

[Slack channel](https://slack.com/app_redirect?channel=C07DQ6VECBE&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3039826)

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

Tiago M. Pereira
#### Summary
----------------------------------------------**ISSUE DESCRIPTION AND HOW TO REPRODUCE**- The customer is experiencing an issue where they are unable to open any pages of their apps, AI4Digital and Gen AI Playgrounds, due to an error indicating that certain models are not defined.
- This issue arose after publishing the apps following a rollback of changes on the platform side. #3039610 -&gt; https://outsystemsrd.atlassian.net/browse/RDINC-27493?atlOrigin=eyJpIjoiMjU3YjkzZDk5NjJkNGRjNDk1Y2ZjMzdmOThiMzM4MzkiLCJwIjoiemVuZGVzay1qaXJhIn0 (at this point doesnt seem related)
- The error happens when trying to open these 2 apps- AI4Digital ( https://extranet-dev.outsystems.app/AI4Digital/ )- ![](https://supportoutsystems.zendesk.com/attachments/token/8ngognj5zbVXefv3qj0cposg5/?name=image.png)- Gen AI Playgrounds ( https://extranet-dev.outsystems.app/GenAIPlaygrounds/ )- ![](https://supportoutsystems.zendesk.com/attachments/token/rS4Pih8iLfpWpmgvAO9YKp8S6/?name=image.png)**IMPACT ON THE CUSTOMER**
High, affecting development of the apps, and follow up stages since its not possible to check the changes on DEV**TROUBLESHOOTING STEPS &amp; WORKAROUND**- Tried to clone the app however, the issue still remains:- ![](https://supportoutsystems.zendesk.com/attachments/token/krrBTm2TcECZ3IYZptf0DallR/?name=image.png)- We can see 500 status error to retrieve https://extranet-dev.outsystems.app/CloneforSupportAI4Digital/moduleservices/auth/configs file.
- Also seems to have some requests to oschunk files, there isn't much information about it except conversations on Slack by CR:- https://outsystems.slack.com/archives/C01056JA3N3/p1715676088798169- From my understading is resources that are bundled on s3
- Also analyzing the errors:- https://outsystems.grafana.net/d/cdeqzn1jj77cwe/general-troubleshooting?orgId=1&amp;var-ring=osall&amp;var-tenant=fae0814c-7560-49cc-886f-6b4eccb6709f&amp;var-application=All&amp;var-cluster=All&amp;var-cluster_old=All&amp;var-severity=Warning&amp;var-severity=Error&amp;var-severity=Critical&amp;var-runtime=All&amp;var-filter=&amp;var-exclude=&amp;var-region=us-east-1&amp;var-traceDuration=All&amp;var-environment=All&amp;var-regionShort=osall-us-east-1-01&amp;var-tenant_prefix=extranet&amp;var-module_name=&amp;from=1721727260000&amp;to=1721727273000- We get 500 status when loading the auth/configs endpoints:- ![](https://supportoutsystems.zendesk.com/attachments/token/nFzkGZ5CkWjmKxOhPApLLmL0x/?name=image.png)- On CF we can crosscheck the same 500:- https://outsystems.grafana.net/d/6-6x5IF4k/cloudfront-logs?orgId=1&amp;var-environment=prod&amp;var-data_source=MWYvlds7z&amp;var-host=extranet-dev.outsystems.app&amp;var-method=All&amp;var-status_code=All&amp;var-edge_response_type=All&amp;var-search=&amp;var-plat_s3=s3%2Flogs-plat-edge-ue1-prod-rn-cloudrd-os&amp;var-run_s3=s3%2Flogs-run-edge-ue1-prod-rn-cloudrd-os&amp;var-cus_s3=s3%2Flogs-cus-edge-ue1-prod-rn-cloudrd-os&amp;from=1721727262000&amp;to=1721727275000- ![](https://supportoutsystems.zendesk.com/attachments/token/7nXLCthcsNduyjDnJ7BKwLEiN/?name=image.png)- And the same on GLoo:- ![](https://supportoutsystems.zendesk.com/attachments/token/Qxogy3LFwfXzgVlEKOWLeQ0UH/?name=image.png)
- At identity level we are not seeing anything major:- https://outsystems.grafana.net/d/cdh4sw1jvc8aof/identity-logs?orgId=1&amp;var-rings=osall&amp;var-regionShort=All&amp;var-severity=Error&amp;var-severity=Warning&amp;var-severity=Information&amp;var-severity=Debug&amp;var-search=fae0814c-7560-49cc-886f-6b4eccb6709f&amp;from=1721723662000&amp;to=1721723695000
- The apps are using external IDP, however, some are not affected discussing with Alex, where Win Loss Gen AI Playground works, and there weren't major changes on AI4DigitalWe requesting help at first from CR, based on symptoms, however, we suspect its just a consequence and the issue might rely on internal communications at BE.Side note:We also tried some troubleshooting regarding this OSchunk resources, however, we didn't found much information about this, and we tried to troubleshoot based on a slack conversation with this dashboard: https://outsystems.grafana.net/explore?schemaVersion=1&amp;panes=%7B%22qcp%22:%7B%22datasource%22:%22grafanacloud-outsystemstest-logs%22,%22queries%22:%5B%7B%22refId%22:%22A%22,%22expr%22:%22%7Bring%3D%5C%22osall%5C%22,%20service_name%3D%5C%22Frontend.Build.Worker%5C%22%7D%20%7C~%20%5C%22_oschunk%5C%22%20%7C%20json%20%20%7C%20attributes_LogRecord_Scope_buildType%20%3D%5C%22Debug%5C%22%20%7C%20line_format%20%5C%22%7B%7B.body%7D%7D%5C%22%22,%22queryType%22:%22range%22,%22datasource%22:%7B%22type%22:%22loki%22,%22uid%22:%22grafanacloud-outsystemstest-logs%22%7D,%22editorMode%22:%22code%22%7D%5D,%22range%22:%7B%22from%22:%22now-3h%22,%22to%22:%22now%22%7D%7D%7D&amp;orgId=1 , however, would be possible to share with us some internal doc what in reality these resources purposes and to troubleshoot them?**TECH DATA OR ANY OTHER RELEVANT INFO**
Ring: osall
Tenant Id: fae0814c-7560-49cc-886f-6b4eccb6709f
Tenant Prefix: extranet
Region: us-east-1
DMN.GTF.J1V.N02.OHY.ZDO.UBL.WTS_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 Retrospective### Details
**Ring:** osall
**System-wide impact:**&nbsp; Yes
**Tenant ID:** fae0814c-7560-49cc-886f-6b4eccb6709f
**Tenant Prefix:** extranet
**Routing Error Code:** OS-CLRT
**Product Area:** -
### Impact:
Applications with static entities would have a runtime error making it impossible to load and have a fully operational application in runtime.
### Investigation and troubleshooting findings:
We are progressively rolling out the Removal RequireJS through the rings and on the last step, we enabled the feature flag on ring OSALL (+1), where the identified problems were found.

The investigation was quite self-explanatory since the generated code was affected by this rollout to ring OSALL.
### Resolution:
Because the ring OSALL was affected with the enablement of the Feature Toggle for the removal of RequireJS, the resolution started with the creation of an RFC [https://outsystemsrd.atlassian.net/browse/RFC-1236](https://outsystemsrd.atlassian.net/browse/RFC-1236)

Due to some problems in the SDLC team's pipelines, the rollback didn't occur and the version that disabled the feature flag on the affected ring reached ring OSALL and ended up fixing the issue.
## Tasks performed during incident resolution:
&nbsp;
## Executive Summary
[Guidelines](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4144496679/Incident+Retrospectives+-+Playbook#STEP-3---Write-the-Executive-Summary)

On July 23 11:00 AM WEST, Customer submitted a Support ticket [RDINC-27520](https://outsystemsrd.atlassian.net/browse/RDINC-27520) reporting some runtime errors when trying to open these 2 apps:

- 
AI4Digital ( [https://extranet-dev.outsystems.app/AI4Digital/](https://extranet-dev.outsystems.app/AI4Digital/) )

- 
Gen AI Playgrounds ( [https://extranet-dev.outsystems.app/GenAIPlaygrounds/](https://extranet-dev.outsystems.app/GenAIPlaygrounds/) )

These 2 errors made it impossible for the applications to run in the browser because the app would always be redirected to the error page.

The investigation concluded that the changes in the generated code from the RequireJS removal introduced a bug that would break the applications in runtime whenever they included static entities.

As a consequence of the incident, we have determined that a rollback in ring +1 (OSALL) was required. We had a RFC RFC-1236ef8955cb-cb21-32a7-b692-01ace42388d6System Jira which got approved and then we also asked for the SDLC to rollback the version of the service to the v17.1488.0 in that same ring - [https://outsystems.slack.com/archives/C02FDRXNER0/p1721740089502369](https://outsystems.slack.com/archives/C02FDRXNER0/p1721740089502369). At the same time the team also reverted the changes in the Build.Job repository - [https://github.com/OutSystems/OutSystems.Build.Job/pull/3928](https://github.com/OutSystems/OutSystems.Build.Job/pull/3928)  and all the versions from v17.1491.0 to v17.1506.0 were banned with help from @alfred [https://outsystems.slack.com/archives/C0147J20TNY/p1721733178674539](https://outsystems.slack.com/archives/C0147J20TNY/p1721733178674539).

Unfortunately (or fortunately), the fix reached the ring +1 before the rollback was made, solving the issue from the customer.
## Root Causes 
[Guidelines](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4144496679/Incident+Retrospectives+-+Playbook#STEP-1---Perform-the-Root-Cause-Analysis)

- 
Progressive rollout of the RequireJS removal reached ring +1 (OSALL).

- 
A bug in the static entities broke the runtime of the applications that used static entities.

If the customer needs formal RCA, please fill out the following field with the document URL

[Please follow these instructions and place the RCA URL in the field below.](https://docs.google.com/document/d/13rXmBsOJh73nV2D6Z17SIBGBu2HOTWty5ddsvU000JM/edit#heading=h.bqxasxszr5q)

RCA URL

&lt;Place the URL of the customer RCA here if you have created one&gt;
## ⌛ Timeline
[View on Rootly](https://rootly.com/account/incidents/747-the-apps-pages-are-not-loading)

**Date**

**Source**

**User**

**Event**

July 23 11:00 AM WEST

web

Rootly

created an alert via

July 23 11:00 AM WEST

web

Rootly

Rootly created this incident

July 23 11:00 AM WEST

web

Rootly

In triage date has been set to July 23 11:00 AM WEST

July 23 11:00 AM WEST

web

Rootly

[Slack Channel](https://slack.com/app_redirect?channel=C07DQ6VECBE&amp;team=T041063TZ) has been created

July 23 11:01 AM WEST

web

Rootly

Ring: osall
System-wide impact:  
Tenant ID: fae0814c-7560-49cc-886f-6b4eccb6709f
Tenant Prefix: extranet
Routing Error Code: OS-CLRT
Product Area: -

July 23 11:01 AM WEST

web

Rootly

[PagerDuty Incident](https://outsystems.pagerduty.com/incidents/Q1QVNLZW4KXL2P) has been created.

📧 Notified Tiago Miguel Pereira by email.

&nbsp;&nbsp;

📲 Notified Tiago Miguel Pereira by push notification.  (via Android)

&nbsp;&nbsp;

📲 Notified Tiago Miguel Pereira by push notification.  (via Android)

July 23 11:01 AM WEST

web

Rootly

Tiago M. Pereira has been assigned as Engineer

July 23 11:01 AM WEST

web

Rootly

Tiago Miguel Pereira acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q1QVNLZW4KXL2P)

July 23 11:01 AM WEST

web

Tiago M. Pereira

Incident has been started

July 23 11:01 AM WEST

web

Rootly

Pagerduty Integrations acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q1QVNLZW4KXL2P). (via Slack)

July 23 12:25 PM WEST

web

Tiago M. Pereira

Send ZenDesk private comment has been set: Hello team,The Client Runtime team analyzed the issues you mentioned and here is what we got from our analysis:  We are progressively rolling out the Removal RequireJS through the rings and on the last step, we enabled the feature flag on ring OSALL (+1), where the identified problems were found. As the next step, we will rollback to solve and unblock the customer.&nbsp;Here is the RFC [https://outsystemsrd.atlassian.net/browse/RFC-1236](https://outsystemsrd.atlassian.net/browse/RFC-1236)  The application Gen AI Playgrounds includes logic that should be replaced to embrace the [strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode):  
\- OnApplicationReady &gt; PlaygroundJSObject:```if(typeof Playground === 'undefined') {&nbsp; &nbsp; Playground = {};}
```in runtime this error is thrown **\&gt;&gt; ReferenceError: Playground is not defined  
**To fix this, the &quot;Playground&quot; should be prefixed with window.Playground, for instance. Note that the JSNodes should only include code compatible with strict mode.  Let us know if you have any additional questions,Best regards,Tiago Pereira

July 23 12:25 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:
Hello team,The Client Runtime team analyzed the issues you mentioned and here is what we got from our analysis:  We are progressively rolling out the Removal RequireJS through the rings and on the last step, we enabled the feature flag on ring OSALL (+1), where the identified problems were found. As the next step, we will rollback to solve and unblock the customer.&nbsp;Here is the RFC [https://outsystemsrd.atlassian.net/browse/RFC-1236](https://outsystemsrd.atlassian.net/browse/RFC-1236)  The application Gen AI Playgrounds includes logic that should be replaced to embrace the [strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode):  
\- OnApplicationReady &gt; PlaygroundJSObject:```if(typeof Playground === 'undefined') {&nbsp; &nbsp; Playground = {};}
```in runtime this error is thrown **\&gt;&gt; ReferenceError: Playground is not defined  
**To fix this, the &quot;Playground&quot; should be prefixed with window.Playground, for instance. Note that the JSNodes should only include code compatible with strict mode.  Let us know if you have any additional questions,Best regards,Tiago Pereira

July 23 12:25 PM WEST

web

Rootly

Send ZenDesk private comment has been unset

July 23 12:25 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:

July 23 12:41 PM WEST

web

Tiago M. Pereira

Send ZenDesk private comment has been set: Regarding the&nbsp; 500 status error to retrieve /moduleservices/auth/configs file, if the problem persists after the rollback, I would recommend asking to the Backend Runtime team and Identity teams to further investigate.

July 23 12:41 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:
Regarding the&nbsp; 500 status error to retrieve /moduleservices/auth/configs file, if the problem persists after the rollback, I would recommend asking to the Backend Runtime team and Identity teams to further investigate.

July 23 12:41 PM WEST

web

Rootly

Send ZenDesk private comment has been unset

July 23 12:41 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:

July 24 11:33 AM WEST

web

Tiago M. Pereira

Send ZenDesk private comment has been set: Hello team,  
I just wanted to let you know that the fix is now in ring OSALL and a republish of the application is required to solve the issues related to the applications AI4Digital and GenAIPlaygrounds.&nbsp;  We highly recommend that the app GenAIPlaygrounds gets updated to reflect the changes that were suggested in the previous message (the one that requires the prefix window.Playground to be compatible with the strict mode.  Finally, if the problem of the error code 500 persists, we kindly ask you to inform us so that we can later move the ticket to the Backend Runtime team so that they can provide further details.Best regards,  
Tiago Pereira

July 24 11:34 AM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:
Hello team,  
I just wanted to let you know that the fix is now in ring OSALL and a republish of the application is required to solve the issues related to the applications AI4Digital and GenAIPlaygrounds.&nbsp;  We highly recommend that the app GenAIPlaygrounds gets updated to reflect the changes that were suggested in the previous message (the one that requires the prefix window.Playground to be compatible with the strict mode.  Finally, if the problem of the error code 500 persists, we kindly ask you to inform us so that we can later move the ticket to the Backend Runtime team so that they can provide further details.Best regards,  
Tiago Pereira

July 24 11:34 AM WEST

web

Rootly

Send ZenDesk private comment has been unset

July 24 11:34 AM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:

July 24  2:24 PM WEST

web

Rootly

Zendesk Private Comment has been set: ----------------------------------------------**Update to R&amp;D**
Hello Tiago and all team,Thank you for your time and help to discuss this situation.Yesterday, went to discuss with Alex, and we apply the suggestion on GenAiPlaygrounds:- ![](https://supportoutsystems.zendesk.com/attachments/token/6iMX2KrXYp8PNc2wOvJrLnPr9/?name=image.png)
- We also change other scripts located on the app:- ![](https://supportoutsystems.zendesk.com/attachments/token/9DwjXRXMGJiJC48pKXqcvDRmd/?name=image.png)- Due to that, the application immediately workToday with the revert of the feature on OSall, we republish the AI4Digital and also worked immediately:- ![](https://supportoutsystems.zendesk.com/attachments/token/NF4xRS7UMBLUV7kO5W7HzUwI6/?name=image.png)Also, the applications started to return a 200 status to the endpoints previously that they had a 500:- ![](https://supportoutsystems.zendesk.com/attachments/token/5ZztJAJhDUczKYtbfVbcG3qud/?name=image.png)At this point we are just returning the feedback and we will mark the case as solved, once again thanks for the help.__

July 24  2:24 PM WEST

web

Rootly

NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
Hello Tiago and all team,Thank you for your time and help to discuss this situation.Yesterday, went to discuss with Alex, and we apply the suggestion on GenAiPlaygrounds:- ![](https://supportoutsystems.zendesk.com/attachments/token/6iMX2KrXYp8PNc2wOvJrLnPr9/?name=image.png)
- We also change other scripts located on the app:- ![](https://supportoutsystems.zendesk.com/attachments/token/9DwjXRXMGJiJC48pKXqcvDRmd/?name=image.png)- Due to that, the application immediately workToday with the revert of the feature on OSall, we republish the AI4Digital and also worked immediately:- ![](https://supportoutsystems.zendesk.com/attachments/token/NF4xRS7UMBLUV7kO5W7HzUwI6/?name=image.png)Also, the applications started to return a 200 status to the endpoints previously that they had a 500:- ![](https://supportoutsystems.zendesk.com/attachments/token/5ZztJAJhDUczKYtbfVbcG3qud/?name=image.png)At this point we are just returning the feedback and we will mark the case as solved, once again thanks for the help.__

July 24  2:28 PM WEST

web

Rootly

ZenDesk Event Type has been set: solved

July 24  2:28 PM WEST

web

Rootly

The Global Support team marked this incident as closed in ZenDesk.

July 24  2:33 PM WEST

web

Tiago M. Pereira

System-wide impact has been set: Yes

July 24  2:35 PM WEST

web

Tiago M. Pereira

Impact has been set: Applications with static entities would have a runtime error making it impossible to load and have a fully operational application in runtime.

July 24  2:37 PM WEST

web

Tiago M. Pereira

Investigation and troubleshooting findings has been set: We are progressively rolling out the Removal RequireJS through the rings and on the last step, we enabled the feature flag on ring OSALL (+1), where the identified problems were found.
The investigation was quite self-explanatory since the generated code was affected by this rollout to ring OSALL.

July 24  2:40 PM WEST

web

Tiago M. Pereira

Incident has been resolved

July 24  2:40 PM WEST

web

Tiago M. Pereira

Resolution has been set: Because the ring OSALL was affected with the enablement of the Feature Toggle for the removal of RequireJS, the resolution started with the creation of an RFC https://outsystemsrd.atlassian.net/browse/RFC-1236
Due to some problems in the SDLC team's pipelines, the rollback didn't occur and the version that disabled the feature flag on the affected ring reached ring OSALL and ended up fixing the issue.