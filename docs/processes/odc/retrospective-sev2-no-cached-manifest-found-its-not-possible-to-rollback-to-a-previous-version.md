---
title: Retrospective-SEV2-No cached manifest found. It's not possible to rollback to a previous version.
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4264099913/Retrospective-SEV2-No+cached+manifest+found.+It+s+not+possible+to+rollback+to+a+previous+version.
confluence_space: RKB
confluence_page_id: 4264099913
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV2-No cached manifest found. It's not possible to rollback to a previous version.

## 📘 Overview
Author:&nbsp;Rootlytrue

Severity:&nbsp;SEV2Redtrue

Teams:&nbsp;Client RuntimeBluetrue
#### 🕐 Timestamps
Started At:&nbsp;July 2 12:33 PM WESTBluetrue

Mitigated At:&nbsp;July 4 10:24 AM WESTYellowtrue

Resolved At:&nbsp;July 4 10:24 AM WESTGreentrue
#### 🔗 Links
[Incident Page](https://rootly.com/account/incidents/657-no-cached-manifest-found-it-s-not-possible-to-rollback-to-a-previous-version)

[Pagerduty incident](https://outsystems.pagerduty.com/incidents/Q0VACKGL02WANE)

[Slack channel](https://slack.com/app_redirect?channel=C07AP62EVDH&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3030037)

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

Carlos Xavier
#### Summary
----------------------------------------------**ISSUE DESCRIPTION AND HOW TO REPRODUCE**
Customer apps are currently unusable. They are not able to open them due to a cache error that they are unable to solve
Simple access **AccessMatrix and EAS apps:**- **https://dil-dev.outsystems.app/AccessMatrix/**
- https://dil-dev.outsystems.app/AccessMatrix2/ Cloned versionNo cached manifest found. It's not possible to rollback to a previous version.
Error: No cached manifest found. It's not possible to rollback to a previous version.at Qc.ensureCachedManifest (https://dil-dev.outsystems.app/AccessMatrix2/scripts/outsystems-runtime-core__P1yYvtHhayajThffoLdxA.js?P1y_YvtHhayajThffoLdxA:8:176762)at Qc.&lt;anonymous&gt; (https://dil-dev.outsystems.app/AccessMatrix2/scripts/outsystems-runtime-core__P1yYvtHhayajThffoLdxA.js?P1y_YvtHhayajThffoLdxA:8:176438)at Generator.next (&lt;anonymous&gt;)at https://dil-dev.outsystems.app/AccessMatrix2/scripts/outsystems-runtime-core__P1yYvtHhayajThffoLdxA.js?P1y_YvtHhayajThffoLdxA:1:1184at new M (https://dil-dev.outsystems.app/AccessMatrix2/scripts/outsystems-logger__JtCooHyB5nvsZZqcmRK4sQ.js?JtCooHyB5nvsZZqcmRK4sQ:7:17428)at a (https://dil-dev.outsystems.app/AccessMatrix2/scripts/outsystems-runtime-core__P1yYvtHhayajThffoLdxA.js?P1y_YvtHhayajThffoLdxA:1:929)at Qc.innerLoadCachedManifest (https://dil-dev.outsystems.app/AccessMatrix2/scripts/outsystems-runtime-core__P1yYvtHhayajThffoLdxA.js?P1y_YvtHhayajThffoLdxA:8:176390)at Qc.&lt;anonymous&gt; (https://dil-dev.outsystems.app/AccessMatrix2/scripts/outsystems-runtime-core__P1yYvtHhayajThffoLdxA.js?P1y_YvtHhayajThffoLdxA:8:176308)at Generator.next (&lt;anonymous&gt;)at https://dil-dev.outsystems.app/AccessMatrix2/scripts/outsystems-runtime-core__P1yYvtHhayajThffoLdxA.js?P1y_YvtHhayajThffoLdxA:1:1184**IMPACT ON THE CUSTOMER**
High, blocking our partner to develop applications completely.**TROUBLESHOOTING STEPS &amp; WORKAROUND**
Customer tried some workarounds including:- Refresh and update all libraries and applications related. NOT WORKED
- Clone and run the clone. NOT WORKED
- Create a new application and copy everything to inside . WORKED FOR EAS BUT NOT FOR ACCESSMATRIX
- Currently they have two apps:  ACCESSMATRIX (original)  and ACCESSMATRIX2 (New app with all content copy inside)- The issue started exactly on Friday- Replicating the issue we can see the errors:
- OS-CLRT-60302- ![](https://supportoutsystems.zendesk.com/attachments/token/FYZQ3bqq5otUZa4Rf5uXAeOL8/?name=image.png)- This CR errors indicating problems with upgrades indeed.
- Creating a simple screen on the APP and republish doesn't fix anything, neither cloning:- ![](https://supportoutsystems.zendesk.com/attachments/token/2lkg0YKNvBmEbgwnfTVntg8Aj/?name=image.png)- Clone the app once again and after delete all screens and maintaining only the one empty with a button the error disappears, so it means that there is a screen creating constrains:- ![](https://supportoutsystems.zendesk.com/attachments/token/bn1nRNdrWBNNJU2xPYmRDRagS/?name=image.png)- Reverting the screens creates another issue with OTA:- ![](https://supportoutsystems.zendesk.com/attachments/token/lHWmiZoHGKsEJuOKuoQv1y0Kd/?name=image.png)
- At log level at CR and BE we don't see any errors:- https://outsystems.grafana.net/d/cdeqzn1jj77cwe/general-troubleshooting?orgId=1&amp;var-ring=ea&amp;var-tenant=c90c3ced-b94c-4340-83a2-38eaabbb0291&amp;var-application=All&amp;var-cluster=All&amp;var-cluster_old=All&amp;var-severity=All&amp;var-runtime=All&amp;var-filter=&amp;var-exclude=&amp;var-region=eu-central-1&amp;var-traceDuration=All&amp;var-environment=All&amp;var-regionShort=ea-eu-ce-1-01&amp;var-tenant_prefix=dil&amp;var-module_name=- We also don't see anything at CF level- https://outsystems.grafana.net/d/fdffqzyolaf40b/cloudfront-logs?orgId=1&amp;var-environment=prod&amp;var-data_source=MWYvlds7z&amp;var-host=&amp;var-method=All&amp;var-status_code=All&amp;var-edge_response_type=All&amp;var-search=dil-dev.outsystems.app&amp;var-plat_s3=s3%2Flogs-plat-edge-ue1-prod-rn-cloudrd-os&amp;var-run_s3=s3%2Flogs-run-edge-ue1-prod-rn-cloudrd-os&amp;var-cus_s3=s3%2Flogs-cus-edge-ue1-prod-rn-cloudrd-os&amp;from=now-5m&amp;to=now- Except some status 000 on some resources:- ![](https://supportoutsystems.zendesk.com/attachments/token/XbKMqgRgSEXJddty7dMyDyvRg/?name=image.png)
Even that both applications when access show different patterns of errors, we suspect that there are issues with version manager or/and access of resources and maybe a recent bug introduced on EA around Friday or Thursday?
We kindly ask R&amp;D if this is the case on this situation.**TECH DATA OR ANY OTHER RELEVANT INFO**
Ring: ea
Tenant Id: c90c3ced-b94c-4340-83a2-38eaabbb0291
Tenant Prefix: dil
Region: eu-central-1
NBI.VHO.NZL.GZG.GYY.6DM.NCO.GUT_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 Retrospective### Details
**Ring:** ea
**System-wide impact:**&nbsp; 
**Tenant ID:** c90c3ced-b94c-4340-83a2-38eaabbb0291
**Tenant Prefix:** dil
**Routing Error Code:** N/A
**Product Area:** Phoenix::Application Runtime::Logic Flows
### Impact:
Customer could not use a Splash screen on a Web App.
### Investigation and troubleshooting findings:
We replaced the axios library, which was responsible for performing client side requests, with the usage of the standard fetch API, in order to mitigate constant security reports that we were getting due to the usage of that library. That library was a bit more permissive that our current wrapper around the fetch API is, so when we get a response from the server we now ensure that the response content has the intended type.

The issue was that our resource prefetching component that is used when a web application has a splash screen configured is requesting the application files as json, when they are plain text or binary files. Axios was ignoring this incoherence but our new wrapper was not, causing the resource fetching and upgrade process to fail.
### Resolution:
We fixed our resource prefetching component to use the right response type when fetching the resources.
## Tasks performed during incident resolution:
&nbsp;
## Executive Summary
On July 2 at 4:09 AM we received an incident report #657 where the customer wasn&rsquo;t able to use his application. Investigation concluded that the issue was related with the usage of the Splash screen in a Web Application and advised the customer to remove the Splash screen from the app while the issue is not fixed.

This situation represents a inability to use a Splash screen in a Web Application.

From a technical perspective, the problem was caused by switch in the communication library to a client that is more strict. Our resource prefetching code was not strict and the process started failing. This resource prefetching implementation only runs in Web Applications with a Splash screen. Mobile applications and PWAs use other processes.

As a consequence of the incident we have:

- 
Short term: Fixed the issue by making the resource prefetching implementation strict.

## Root Causes 
We replaced the axios library by a custom wrapper around fetch API. The wrapper is more strict than axios was, which led to code that poorly specified to stop working. The tests for the feature were not validating all the parameters used in the process, which allowed this issue to escape our testing. The scenario is not a common scenario and no tested in our rings.

If the customer needs formal RCA, please fill out the following field with the document URL

[Please follow these instructions and place the RCA URL in the field below.](https://docs.google.com/document/d/13rXmBsOJh73nV2D6Z17SIBGBu2HOTWty5ddsvU000JM/edit#heading=h.bqxasxszr5q)

RCA URL

&lt;Place the URL of the customer RCA here if you have created one&gt;
## ⌛ Timeline
[View on Rootly](https://rootly.com/account/incidents/657-no-cached-manifest-found-it-s-not-possible-to-rollback-to-a-previous-version)

**Date**

**Source**

**User**

**Event**

July 2 12:09 PM WEST

web

Rootly

created an alert via

July 2 12:09 PM WEST

web

Rootly

Rootly created this incident

July 2 12:09 PM WEST

web

Rootly

In triage date has been set to July 2 12:09 PM WEST

July 2 12:10 PM WEST

web

Rootly

[Slack Channel](https://slack.com/app_redirect?channel=C07AP62EVDH&amp;team=T041063TZ) has been created

July 2 12:10 PM WEST

web

Rootly

[PagerDuty Incident](https://outsystems.pagerduty.com/incidents/Q0VACKGL02WANE) has been created.

📧 Notified Rui Garcia by email.

&nbsp;&nbsp;

📱 Notified Rui Garcia by SMS.

&nbsp;&nbsp;

📧 Notified Rui Garcia by email.

July 2 12:10 PM WEST

web

Rootly

Rui Garcia has been assigned as Engineer

July 2 12:10 PM WEST

web

Rootly

Ring: ea
System-wide impact:  
Tenant ID: c90c3ced-b94c-4340-83a2-38eaabbb0291
Tenant Prefix: dil
Routing Error Code: N/A
Product Area: Phoenix::Application Runtime::Logic Flows

July 2 12:11 PM WEST

web

Rootly

Rui Garcia acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q0VACKGL02WANE). (via Phone)

July 2 12:33 PM WEST

web

Rui Garcia

Incident has been started

July 2 12:33 PM WEST

web

Rootly

Pagerduty Integrations acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q0VACKGL02WANE). (via Phone)

July 2 12:34 PM WEST

web

Rui Garcia

Swarm has been set: Client Runtime

July 2 12:34 PM WEST

web

Rootly

Pagerduty Integrations added Rita Tinoco as responder in [PagerDuty](https://outsystems.pagerduty.com/incidents/Q0VACKGL02WANE)

July 2 12:36 PM WEST

web

Rui Garcia

Teams has been removed: [Backend Runtime](/account/teams/backend-runtime/status)

July 2 12:38 PM WEST

web

Rootly

Delegated to EP for Neo Client Runtime by Rui Garcia through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q0VACKGL02WANE)

July 2 12:40 PM WEST

web

Rootly

Rita Tinoco joined this [PagerDuty](https://outsystems.pagerduty.com/incidents/Q0VACKGL02WANE) incident.

July 2 12:43 PM WEST

web

Rootly

Rita Tinoco acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q0VACKGL02WANE). (via Phone)

July 2  1:19 PM WEST

web

Carlos Xavier

Carlos Xavier has been assigned as Engineer

July 2  1:43 PM WEST

web

Carlos Xavier

Send ZenDesk private comment has been set: Hi team,  We replaced the axios library, which was responsible for performing client side requests, with the usage of the standard fetch API, in order to mitigate constant security reports that we were getting due to the usage of that library. That library was a bit more permissive that our current wrapper around the fetch API is, so when we get a response from the server we now ensure that the response content has the intended type.  
The issue is that our resource prefetching component that is used when a web application has a splash screen configured is requesting the application files as json, when they are plain text or binary files. Axios was ignoring this incoherence but our new wrapper is not.  
In order to fix the prefetching, we created issue \[RAR-2749\](https://outsystemsrd.atlassian.net/browse/RAR-2749).  As a workaround, the customer can go to the Application Properties and set no Splash screen:  ![image.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDAzNzI0LCJwdXIiOiJibG9iX2lkIn19--22729410271169d2a6189519fe447923d22e86c4/image.png)image.png 46.08 KBLet me just say that web applications with splash screens are not a common use case. You typically don't want to prefetch all the application resources before showing the requested URL. This is a predominantly mobile pattern. Mobile applications are not affected since they use a different mechanism to preload the resources.  We'll proceed with the fix on our side.  Best regards,  
Carlos Xavier

July 2  1:43 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:
Hi team,  We replaced the axios library, which was responsible for performing client side requests, with the usage of the standard fetch API, in order to mitigate constant security reports that we were getting due to the usage of that library. That library was a bit more permissive that our current wrapper around the fetch API is, so when we get a response from the server we now ensure that the response content has the intended type.  
The issue is that our resource prefetching component that is used when a web application has a splash screen configured is requesting the application files as json, when they are plain text or binary files. Axios was ignoring this incoherence but our new wrapper is not.  
In order to fix the prefetching, we created issue \[RAR-2749\](https://outsystemsrd.atlassian.net/browse/RAR-2749).  As a workaround, the customer can go to the Application Properties and set no Splash screen:  ![image.png](https://rootly.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6NDAzNzI0LCJwdXIiOiJibG9iX2lkIn19--22729410271169d2a6189519fe447923d22e86c4/image.png)image.png 46.08 KBLet me just say that web applications with splash screens are not a common use case. You typically don't want to prefetch all the application resources before showing the requested URL. This is a predominantly mobile pattern. Mobile applications are not affected since they use a different mechanism to preload the resources.  We'll proceed with the fix on our side.  Best regards,  
Carlos Xavier

July 2  1:43 PM WEST

web

Rootly

Send ZenDesk private comment has been unset

July 2  1:43 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:

July 2  5:11 PM WEST

web

Carlos Xavier

Send ZenDesk private comment has been set: Hi Support,  The fix has been implemented and will show up in the release notes with the id RAR-2749.  I'll provide the service version number with the fix later once the preliminary validations pass and the version number is set.  Best regards,  
Carlos Xavier

July 2  5:11 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:
Hi Support,  The fix has been implemented and will show up in the release notes with the id RAR-2749.  I'll provide the service version number with the fix later once the preliminary validations pass and the version number is set.  Best regards,  
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

July 3  5:05 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:
Hi Support,  The fix is entering the rings. I'm just waiting for it to reach a ring where I can perform an end-to-end test to ensure everything is working properly. I'll update you then.  Best regards,  
Carlos Xavier

July 3  5:05 PM WEST

web

Rootly

Send ZenDesk private comment has been unset

July 3  5:05 PM WEST

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

July 4 10:24 AM WEST

web

Carlos Xavier

Incident has been resolved

July 4 10:24 AM WEST

web

Carlos Xavier

Impact has been set: Customer could not use a Splash screen on a Web App.

July 4 10:24 AM WEST

web

Carlos Xavier

Investigation and troubleshooting findings has been set: We replaced the axios library, which was responsible for performing client side requests, with the usage of the standard fetch API, in order to mitigate constant security reports that we were getting due to the usage of that library. That library was a bit more permissive that our current wrapper around the fetch API is, so when we get a response from the server we now ensure that the response content has the intended type.The issue was that our resource prefetching component that is used when a web application has a splash screen configured is requesting the application files as json, when they are plain text or binary files. Axios was ignoring this incoherence but our new wrapper was not, causing the resource fetching and upgrade process to fail.

July 4 10:24 AM WEST

web

Carlos Xavier

Resolution has been set: We fixed our resource prefetching component to use the right response type when fetching the resources.