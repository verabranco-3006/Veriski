---
title: Retrospective-SEV2-Impossible uploads, even in chunks, with ODC towards AWS S3
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4333961338/Retrospective-SEV2-Impossible+uploads+even+in+chunks+with+ODC+towards+AWS+S3
confluence_space: RKB
confluence_page_id: 4333961338
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV2-Impossible uploads, even in chunks, with ODC towards AWS S3

## 📘 Overview
Author:&nbsp;Rootlytrue

Severity:&nbsp;SEV2Redtrue

Teams:&nbsp;Backend RuntimeBluetrue
#### 🕐 Timestamps
Started At:&nbsp;August 5  5:07 AM WESTBluetrue

Mitigated At:&nbsp;August 5  1:35 PM WESTYellowtrue

Resolved At:&nbsp;August 5  1:35 PM WESTGreentrue
#### 🔗 Links
[Incident Page](https://rootly.com/account/incidents/808-impossible-uploads-even-in-chunks-with-odc-towards-aws-s3)

[Pagerduty incident](https://outsystems.pagerduty.com/incidents/Q3PY3HYWQZRX0G)

[Slack channel](https://slack.com/app_redirect?channel=C07F1BEJP6K&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3043700)

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

Rui Garcia
#### Summary
**CONSIDERATIONS BEFORE PERFORMING THE ESCALATION TO R&amp;D (MANDATORY)**None of the below points should be overlooked. Failure to do so may imply unnecessary effort.Ensure the ticket has been **categorized**, otherwise, the R&amp;D escalation will go unnoticed and not be worked on!**1.** For **Incidents**, the **IMAX** was consulted **beforehand** on which:*   No incident models were found for the reported symptoms **OR**
*   The incident model did not solve the issue **OR**
*   The next step indicated in the Incident Model is an escalation to R&amp;D. **2.** For **Questions**, the ChatODC on the **Slack channel** didn't return an acceptable answer. **3.** Any other requests that explicitly indicate an R&amp;D escalation is needed. **4**. **Incident impact assessment** was based on the **prioritization scoring matrix**.**R&amp;D ESCALATION FORM**&nbsp;  
Section comments can be removed for R&amp;D easier interpretation.**ISSUE DESCRIPTION AND HOW TO REPRODUCE***   We are aware there is a limitation in ODC to send input files to Extensions with more then 5.5Mb
*   The customer is sending binary inputs chunks, less then 5.5Mb, but ODC adds additional payload data do the inputs, increasing the payload by more 1.17Mb (It is not sure what this additional &quot;mystery&quot; input data is), and the limit of 5.5Mb is breached. (the size become 6.7 MB).
*   Apparently, to upload files in chunks with AWS S3 the minimum chunk size (except the last), is 5Mb.&nbsp;*   [https://docs.aws.amazon.com/AmazonS3/latest/userguide/qfacts.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/qfacts.html)
*   As such, the customer is sending exactly 5MB to the input to comply with the S3 requirement.
*   OutSystems then adds around 1.17Mb and the extension raises the error![?name=image.png](https://supportoutsystems.zendesk.com/attachments/token/awncYfO9B55swJaEBwmOatvQh/?name=image.png)*   OS-BERT-ELR-61301 - Post request issued by 'PutObject' failed: Input payload is too large (6.67MB), maximum allowed is 5.5MB. Input payload is too large (6.67MB), maximum allowed is 5.5MB.
*   OutSystems.Application.ErrorHandling.ExtensionException: Input payload is too large (6.67MB), maximum allowed is 5.5MB.&nbsp; at Qe ([https://gs-sandbox-ga-eu-01-dev.outsystems.app/POC\_5Mb/scripts/outsystems-runtime-core\_\_DjOvO9F4y8sbbxi8Y1JQEw.js?DjOvO9F4y8sbbxi8Y1JQEw:1:14887)](https://gs-sandbox-ga-eu-01-dev.outsystems.app/POC_5Mb/scripts/outsystems-runtime-core__DjOvO9F4y8sbbxi8Y1JQEw.js?DjOvO9F4y8sbbxi8Y1JQEw:1:14887\)%C2%A0) at vo ([https://gs-sandbox-ga-eu-01-dev.outsystems.app/POC\_5Mb/scripts/outsystems-runtime-core\_\_DjOvO9F4y8sbbxi8Y1JQEw.js?DjOvO9F4y8sbbxi8Y1JQEw:8:59889)](https://gs-sandbox-ga-eu-01-dev.outsystems.app/POC_5Mb/scripts/outsystems-runtime-core__DjOvO9F4y8sbbxi8Y1JQEw.js?DjOvO9F4y8sbbxi8Y1JQEw:8:59889\)%C2%A0) at [https://gs-sandbox-ga-eu-01-dev.outsystems.app/POC\_5Mb/scripts/outsystems-runtime-core\_\_DjOvO9F4y8sbbxi8Y1JQEw.js?DjOvO9F4y8sbbxi8Y1JQEw:8:58672](https://gs-sandbox-ga-eu-01-dev.outsystems.app/POC_5Mb/scripts/outsystems-runtime-core__DjOvO9F4y8sbbxi8Y1JQEw.js?DjOvO9F4y8sbbxi8Y1JQEw:8:58672%C2%A0) at a ([https://gs-sandbox-ga-eu-01-dev.outsystems.app/POC\_5Mb/scripts/outsystems-runtime-core\_\_DjOvO9F4y8sbbxi8Y1JQEw.js?DjOvO9F4y8sbbxi8Y1JQEw:1:986)](https://gs-sandbox-ga-eu-01-dev.outsystems.app/POC_5Mb/scripts/outsystems-runtime-core__DjOvO9F4y8sbbxi8Y1JQEw.js?DjOvO9F4y8sbbxi8Y1JQEw:1:986\)%C2%A0) at i.invoke ([https://gs-sandbox-ga-eu-01-dev.outsystems.app/POC\_5Mb/scripts/outsystems-logger\_\_DA6QJ7ofCz43gspUnGPyPg.js?DA6QJ7ofCz43gspUnGPyPg:7:26029)](https://gs-sandbox-ga-eu-01-dev.outsystems.app/POC_5Mb/scripts/outsystems-logger__DA6QJ7ofCz43gspUnGPyPg.js?DA6QJ7ofCz43gspUnGPyPg:7:26029\)%C2%A0) at r.run ([https://gs-sandbox-ga-eu-01-dev.outsystems.app/POC\_5Mb/scripts/outsystems-logger\_\_DA6QJ7ofCz43gspUnGPyPg.js?DA6QJ7ofCz43gspUnGPyPg:7:21220)](https://gs-sandbox-ga-eu-01-dev.outsystems.app/POC_5Mb/scripts/outsystems-logger__DA6QJ7ofCz43gspUnGPyPg.js?DA6QJ7ofCz43gspUnGPyPg:7:21220\)%C2%A0) at [https://gs-sandbox-ga-eu-01-dev.outsystems.app/POC\_5Mb/scripts/outsystems-logger\_\_DA6QJ7ofCz43gspUnGPyPg.js?DA6QJ7ofCz43gspUnGPyPg:7:15930](https://gs-sandbox-ga-eu-01-dev.outsystems.app/POC_5Mb/scripts/outsystems-logger__DA6QJ7ofCz43gspUnGPyPg.js?DA6QJ7ofCz43gspUnGPyPg:7:15930%C2%A0) at i.invokeTask ([https://gs-sandbox-ga-eu-01-dev.outsystems.app/POC\_5Mb/scripts/outsystems-logger\_\_DA6QJ7ofCz43gspUnGPyPg.js?DA6QJ7ofCz43gspUnGPyPg:7:26647)](https://gs-sandbox-ga-eu-01-dev.outsystems.app/POC_5Mb/scripts/outsystems-logger__DA6QJ7ofCz43gspUnGPyPg.js?DA6QJ7ofCz43gspUnGPyPg:7:26647\)%C2%A0) at r.runTask ([https://gs-sandbox-ga-eu-01-dev.outsystems.app/POC\_5Mb/scripts/outsystems-logger\_\_DA6QJ7ofCz43gspUnGPyPg.js?DA6QJ7ofCz43gspUnGPyPg:7:21972) ExtraStack:](https://gs-sandbox-ga-eu-01-dev.outsystems.app/POC_5Mb/scripts/outsystems-logger__DA6QJ7ofCz43gspUnGPyPg.js?DA6QJ7ofCz43gspUnGPyPg:7:21972\)%C2%A0ExtraStack:) PutObject**IMPACT ON THE CUSTOMER***   High. Development stage but the app they are fixing is in Production.
*   The business impact is that they are not able to upload the files.&nbsp;*   They need a workaround for this as soon as possible.**TROUBLESHOOTING STEPS &amp; WORKAROUND***   We were able to replicate the issue with the customer's POC (proof of concept) app*   [https://gs-sandbox-ga-eu-01-dev.outsystems.app/POC\_5Mb](https://gs-sandbox-ga-eu-01-dev.outsystems.app/POC_5Mb)*   Attached is the OML and the sample upload file (5 MB)
*   Using browser developer tools we can see*   The content length of the Request Header is shown 6990855 bytes which is about 6.7 MB![?name=image.png](https://supportoutsystems.zendesk.com/attachments/token/zSxVwqlyDRw3aArSlA58OQZud/?name=image.png)*   However the size of the file that was uploaded was only around 5.1 MB.
*   In the ODC portal we can see these types of logs![?name=image.png](https://supportoutsystems.zendesk.com/attachments/token/awncYfO9B55swJaEBwmOatvQh/?name=image.png)*   The logic is they use the AWS\_S3\_Connector's **PutObject**![?name=image.png](https://supportoutsystems.zendesk.com/attachments/token/eWnbZGWk27kyM888uGMt7V7JT/?name=image.png)![DownloadAmazon.aspx?TicketGUID=5ea57066-3432-4d67-b81d-b5dc27a8359e&amp;FileName=1722521160000000000__1722521159876.png](https://www.outsystems.com/SupportPortal/DownloadAmazon.aspx?TicketGUID=5ea57066-3432-4d67-b81d-b5dc27a8359e&amp;FileName=1722521160000000000__1722521159876.png)*   Just to test, even when we tried to upload smaller files (3 MB or even 100KB), we am getting a different error![?name=image.png](https://supportoutsystems.zendesk.com/attachments/token/F7G4SbYS8BXmfspPEU6jPok19/?name=image.png)*   This might be due to what the customer said -&gt; *   _To upload files in chunks with AWS S3 the minimum chunk size (except the last), is 5Mb_*   Some literature on this info...a minimum chunk size of 5MB for AWS S3..*   [https://docs.aws.amazon.com/AmazonS3/latest/userguide/qfacts.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/qfacts.html)*   3rd party site&nbsp;*   [https://uppy.io/docs/aws-s3/#:~:text=S3%20requires%20a%20minimum%20chunk,it%20to%20S3's%20minimum%20requirements](https://uppy.io/docs/aws-s3/#:~:text=S3%20requires%20a%20minimum%20chunk,it%20to%20S3's%20minimum%20requirements).![?name=image.png](https://supportoutsystems.zendesk.com/attachments/token/cYODup1pSZrp9LsDl2o6nqHBY/?name=image.png)*   We are aware of these documents*   [https://outsystemsrd.atlassian.net/wiki/spaces/RDSD/pages/3488318580/ODC+known+quotas+and+limits](https://outsystemsrd.atlassian.net/wiki/spaces/RDSD/pages/3488318580/ODC+known+quotas+and+limits)*   [https://outsystemsrd.atlassian.net/wiki/spaces/CloudKB/pages/3719987448/ODC+Known+Quotas+and+Limits](https://outsystemsrd.atlassian.net/wiki/spaces/CloudKB/pages/3719987448/ODC+Known+Quotas+and+Limits)*   [https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html)*   But since the customer has this situation of needing a minimum of 5MB for the upload, so its not clear how the above workarounds will be useful.
*   We are aware of a past case, quite similar*   [https://outsystemsrd.atlassian.net/browse/RDINC-18468](https://outsystemsrd.atlassian.net/browse/RDINC-18468)*   But, again, its not clear if it same as this they are not using any Base64 conversion.
*   As such, the main question here is, why the 5.1 MB file size is showing up as 6.7 MB size in the request and thus being rejected by ODC.*   Where does the &quot;extra&quot; size come from?*   And is there is a way for the customer to workaround this situation.**TECH DATA OR ANY OTHER RELEVANT INFO**&nbsp;  
Ring: ea&nbsp;  
Tenant Id: 3313c749-2159-4df2-98e2-f29dbf73263e&nbsp;  
Tenant Prefix: creetionodc&nbsp;  
Region: eu-central-1&nbsp;_Technical Support::Send to R&amp;D - ODC #trigger\_send\_to\_r&amp;d\_odc !&gt;__Attachment(s):  
POC\_5Mb.zip -_ [_https://supportoutsystems.zendesk.com/attachments/token/gp7XDRI0HGROwZoSZyfUOYkH7/?name=POC\_5Mb.zip_](https://supportoutsystems.zendesk.com/attachments/token/gp7XDRI0HGROwZoSZyfUOYkH7/?name=POC_5Mb.zip)
## 📝 Retrospective### Details
**Ring:** ea
**System-wide impact:**&nbsp; No
**Tenant ID:** 3313c749-2159-4df2-98e2-f29dbf73263e
**Tenant Prefix:** creetionodc
**Routing Error Code:** OS-BERT
**Product Area:** -
### Impact:
Customer is trying to develop using External Libraries sending payloads beyond the supported limit.
### Investigation and troubleshooting findings:
Everything is working as expected. This was a development question (probably shouldn't be a SEV2 to begin with).
### Resolution:
Customer as multiple workarounds to choose depending on the application use case. These workarounds will bring complexity but are necessary given the limitations imposed by the underlying technology.
## Tasks performed during incident resolution:
&nbsp;
## Executive Summary
[Guidelines](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4144496679/Incident+Retrospectives+-+Playbook#STEP-3---Write-the-Executive-Summary)

On August 1st, 2024, Customer reported being unable to use External Library Action (from an unsupported forge component) inputs larger than 5.5MB. According to our customer this prevents the S3 integration use case being developed.

Best practices mandate payloads, both requests and response should be allowed to grow indefinitely and because of that AWS Lambda imposes strict size limits. As the underlying technology supporting the External libraries feature, and are obliged to impose the same restrictions onto the OutSystems Language. This is documented along with two workarounds.

From a technical perspective, the product is behaving as designed.

Usage feedback of External Libraries regarding this limitation and issues related with large binaries in general throughout the product are already being considered in multiple initiatives for ODC. For that reason, there is no short term action identified that could improve our customer experience. Any product increment in this regard must be considered as part of a dedicated VM.
## Root Causes 
External Libraries payloads are limited to 5.5MB. This includes all External Library Action input parameter values and can result in a slightly higher value due to how the parameters and their values are internally represented/serialized.

[Guidelines](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4144496679/Incident+Retrospectives+-+Playbook#STEP-1---Perform-the-Root-Cause-Analysis)

If the customer needs formal RCA, please fill out the following field with the document URL

[Please follow these instructions and place the RCA URL in the field below.](https://docs.google.com/document/d/13rXmBsOJh73nV2D6Z17SIBGBu2HOTWty5ddsvU000JM/edit#heading=h.bqxasxszr5q)

RCA URL

&lt;Place the URL of the customer RCA here if you have created one&gt;
## ⌛ Timeline
[View on Rootly](https://rootly.com/account/incidents/808-impossible-uploads-even-in-chunks-with-odc-towards-aws-s3)

**Date**

**Source**

**User**

**Event**

August 5  5:03 AM WEST

web

Rootly

created an alert via

August 5  5:03 AM WEST

web

Rootly

Rootly created this incident

August 5  5:03 AM WEST

web

Rootly

In triage date has been set to August 5  5:03 AM WEST

August 5  5:03 AM WEST

web

Rootly

[Slack Channel](https://slack.com/app_redirect?channel=C07F1BEJP6K&amp;team=T041063TZ) has been created

August 5  5:04 AM WEST

web

Rootly

Ring: ea
System-wide impact:  
Tenant ID: 3313c749-2159-4df2-98e2-f29dbf73263e
Tenant Prefix: creetionodc
Routing Error Code: OS-BERT
Product Area: -

August 5  5:04 AM WEST

web

Rootly

[PagerDuty Incident](https://outsystems.pagerduty.com/incidents/Q3PY3HYWQZRX0G) has been created.

📧 Notified Dhruv Desai by email.

&nbsp;&nbsp;

📲 Notified Dhruv Desai by push notification.  (via iPhone)

August 5  5:04 AM WEST

web

Rootly

Dhruv Desai has been assigned as Engineer

August 5  5:04 AM WEST

web

Rootly

Dhruv Desai acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q3PY3HYWQZRX0G). (via Mobile)

August 5  5:07 AM WEST

web

Dhruv Desai

Incident has been started

August 5  5:07 AM WEST

web

Rootly

Pagerduty Integrations acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q3PY3HYWQZRX0G). (via Mobile)

August 5  5:11 AM WEST

slack

Dhruv Desai

Seems like this is not a system wide alert
As it seems like a single tenant issue
I am finding a relevant team to route this based on code : OS-BERT

August 5  5:14 AM WEST

web

Dhruv Desai

Swarm has been set: Extended Runtime

August 5  5:14 AM WEST

web

Rootly

Pagerduty Integrations added Rafael Duarte as responder in [PagerDuty](https://outsystems.pagerduty.com/incidents/Q3PY3HYWQZRX0G)

August 5  5:20 AM WEST

web

Rootly

Rafael Duarte joined this [PagerDuty](https://outsystems.pagerduty.com/incidents/Q3PY3HYWQZRX0G) incident.

August 5  5:20 AM WEST

web

Rootly

Rafael Duarte acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q3PY3HYWQZRX0G). (via Mobile)

August 5  5:29 AM WEST

web

Rafael Duarte

Summary has been changed to 

&nbsp;&nbsp;`&nbsp;&nbsp;`

`&nbsp;&nbsp;CONSIDERATIONS BEFORE PERFORMING THE ESCALATION TO R&amp;D (MANDATORY)&nbsp;&nbsp;`

`&nbsp;&nbsp;`

`None of the below points should be overlooked. Failure to do so may imply unnecessary effort.`

`&nbsp;&nbsp;`

`Ensure the ticket has been categorized, otherwise, the R&amp;D escalation will go unnoticed and not be worked on!`

`&nbsp;&nbsp;`

`&nbsp;&nbsp;1. For Incidents, the IMAX was consulted beforehand on which:`

- 
`  No incident models were found for the reported symptoms OR&nbsp;&nbsp;`

- 
`  The incident model did not solve the issue OR&nbsp;&nbsp;`

- 
`  The next step indicated in the Incident Model is an escalation to R&amp;D. 2. For Questions, the ChatODC on the Slack channel didn't return an acceptable answer. 3. Any other requests that explicitly indicate an R&amp;D escalation is needed. 4. Incident impact assessment was based on the prioritization scoring matrix.`

`&nbsp;&nbsp;R&amp;D ESCALATION FORM&nbsp;`

`Section comments can be removed for R&amp;D easier interpretation.`

`&nbsp;&nbsp;`

`&nbsp;&nbsp;ISSUE DESCRIPTION AND HOW TO REPRODUCE&nbsp;&nbsp;`

- 
`  We are aware there is a limitation in ODC to send input files to Extensions with more then 5.5Mb`

- 
`  The customer is sending binary inputs chunks, less then 5.5Mb, but ODC adds additional payload data do the inputs, increasing the payload by more 1.17Mb (It is not sure what this additional &quot;mystery&quot; input data is), and the limit of 5.5Mb is breached. (the size become 6.7 MB).`

- 
`  Apparently, to upload files in chunks with AWS S3 the minimum chunk size (except the last), is 5Mb.&nbsp;`

- 
[https://docs.aws.amazon.com/AmazonS3/latest/userguide/qfacts.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/qfacts.html)`&nbsp;&nbsp;`

`&nbsp;&nbsp;`

- 
`  As such, the customer is sending exactly 5MB to the input to comply with the S3 requirement.`

- 
`&nbsp;&nbsp;`

`  OutSystems then adds around 1.17Mb and the extension raises the error`

`&nbsp;&nbsp;`

`&nbsp;&nbsp;``&nbsp;&nbsp;`

`&nbsp;&nbsp;`

- 
`&nbsp;&nbsp;`

`  OS-BERT-ELR-61301 - Post request issued by 'PutObject' failed: Input payload is too large (6.67MB), maximum allowed is 5.5MB. Input payload is too large (6.67MB), maximum allowed is 5.5MB.`

`&nbsp;&nbsp;`

- 
`&nbsp;&nbsp;`

`  OutSystems.Application.ErrorHandling.ExtensionException: Input payload is too large (6.67MB), maximum allowed is 5.5MB.&nbsp; at Qe (`[https://gs-sandbox-ga-eu-01-dev.outsystems.app/POC_5Mb/scripts/outsystems-runtime-core__DjOvO9F4y8sbbxi8Y1JQEw.js?DjOvO9F4y8sbbxi8Y1JQEw:1:14887)](https://gs-sandbox-ga-eu-01-dev.outsystems.app/POC_5Mb/scripts/outsystems-runtime-core__DjOvO9F4y8sbbxi8Y1JQEw.js?DjOvO9F4y8sbbxi8Y1JQEw:1:14887)%C2%A0)` at vo (`[https://gs-sandbox-ga-eu-01-dev.outsystems.app/POC_5Mb/scripts/outsystems-runtime-core__DjOvO9F4y8sbbxi8Y1JQEw.js?DjOvO9F4y8sbbxi8Y1JQEw:8:59889)](https://gs-sandbox-ga-eu-01-dev.outsystems.app/POC_5Mb/scripts/outsystems-runtime-core__DjOvO9F4y8sbbxi8Y1JQEw.js?DjOvO9F4y8sbbxi8Y1JQEw:8:59889)%C2%A0)` at `[https://gs-sandbox-ga-eu-01-dev.outsystems.app/POC_5Mb/scripts/outsystems-runtime-core__DjOvO9F4y8sbbxi8Y1JQEw.js?DjOvO9F4y8sbbxi8Y1JQEw:8:58672](https://gs-sandbox-ga-eu-01-dev.outsystems.app/POC_5Mb/scripts/outsystems-runtime-core__DjOvO9F4y8sbbxi8Y1JQEw.js?DjOvO9F4y8sbbxi8Y1JQEw:8:58672%C2%A0)` at a (`[https://gs-sandbox-ga-eu-01-dev.outsystems.app/POC_5Mb/scripts/outsystems-runtime-core__DjOvO9F4y8sbbxi8Y1JQEw.js?DjOvO9F4y8sbbxi8Y1JQEw:1:986)](https://gs-sandbox-ga-eu-01-dev.outsystems.app/POC_5Mb/scripts/outsystems-runtime-core__DjOvO9F4y8sbbxi8Y1JQEw.js?DjOvO9F4y8sbbxi8Y1JQEw:1:986)%C2%A0)` at i.invoke (`[https://gs-sandbox-ga-eu-01-dev.outsystems.app/POC_5Mb/scripts/outsystems-logger__DA6QJ7ofCz43gspUnGPyPg.js?DA6QJ7ofCz43gspUnGPyPg:7:26029)](https://gs-sandbox-ga-eu-01-dev.outsystems.app/POC_5Mb/scripts/outsystems-logger__DA6QJ7ofCz43gspUnGPyPg.js?DA6QJ7ofCz43gspUnGPyPg:7:26029)%C2%A0)` at r.run (`[https://gs-sandbox-ga-eu-01-dev.outsystems.app/POC_5Mb/scripts/outsystems-logger__DA6QJ7ofCz43gspUnGPyPg.js?DA6QJ7ofCz43gspUnGPyPg:7:21220)](https://gs-sandbox-ga-eu-01-dev.outsystems.app/POC_5Mb/scripts/outsystems-logger__DA6QJ7ofCz43gspUnGPyPg.js?DA6QJ7ofCz43gspUnGPyPg:7:21220)%C2%A0)` at `[https://gs-sandbox-ga-eu-01-dev.outsystems.app/POC_5Mb/scripts/outsystems-logger__DA6QJ7ofCz43gspUnGPyPg.js?DA6QJ7ofCz43gspUnGPyPg:7:15930](https://gs-sandbox-ga-eu-01-dev.outsystems.app/POC_5Mb/scripts/outsystems-logger__DA6QJ7ofCz43gspUnGPyPg.js?DA6QJ7ofCz43gspUnGPyPg:7:15930%C2%A0)` at i.invokeTask (`[https://gs-sandbox-ga-eu-01-dev.outsystems.app/POC_5Mb/scripts/outsystems-logger__DA6QJ7ofCz43gspUnGPyPg.js?DA6QJ7ofCz43gspUnGPyPg:7:26647)](https://gs-sandbox-ga-eu-01-dev.outsystems.app/POC_5Mb/scripts/outsystems-logger__DA6QJ7ofCz43gspUnGPyPg.js?DA6QJ7ofCz43gspUnGPyPg:7:26647)%C2%A0)` at r.runTask (`[https://gs-sandbox-ga-eu-01-dev.outsystems.app/POC_5Mb/scripts/outsystems-logger__DA6QJ7ofCz43gspUnGPyPg.js?DA6QJ7ofCz43gspUnGPyPg:7:21972) ExtraStack:](https://gs-sandbox-ga-eu-01-dev.outsystems.app/POC_5Mb/scripts/outsystems-logger__DA6QJ7ofCz43gspUnGPyPg.js?DA6QJ7ofCz43gspUnGPyPg:7:21972)%C2%A0ExtraStack:)` PutObject`

`&nbsp;&nbsp;`

`&nbsp;&nbsp;IMPACT ON THE CUSTOMER&nbsp;&nbsp;`

- 
`  High. Development stage but the app they are fixing is in Production.`

- 
`  The business impact is that they are not able to upload the files.&nbsp;`

- 
`  They need a workaround for this as soon as possible.`

`&nbsp;&nbsp;`

`&nbsp;&nbsp;TROUBLESHOOTING STEPS &amp; WORKAROUND&nbsp;&nbsp;`

- 
`  We were able to replicate the issue with the customer's POC (proof of concept) app`

- 
[https://gs-sandbox-ga-eu-01-dev.outsystems.app/POC_5Mb](https://gs-sandbox-ga-eu-01-dev.outsystems.app/POC_5Mb)`&nbsp;&nbsp;`

- 
`  Attached is the OML and the sample upload file (5 MB)`

`&nbsp;&nbsp;`

- 
`&nbsp;&nbsp;`

`  Using browser developer tools we can see`

- 
`&nbsp;&nbsp;`

`  The content length of the Request Header is shown 6990855 bytes which is about 6.7 MB`

`&nbsp;&nbsp;`

`&nbsp;&nbsp;``&nbsp;&nbsp;`

`&nbsp;&nbsp;`

- 
`&nbsp;&nbsp;`

`  However the size of the file that was uploaded was only around 5.1 MB.`

`&nbsp;&nbsp;`

`&nbsp;&nbsp;`

- 
`&nbsp;&nbsp;`

`  In the ODC portal we can see these types of logs`

`&nbsp;&nbsp;`

`&nbsp;&nbsp;``&nbsp;&nbsp;`

`&nbsp;&nbsp;`

- 
`&nbsp;&nbsp;`

`  The logic is they use the AWS_S3_Connector's PutObject&nbsp;&nbsp;`

`&nbsp;&nbsp;`

`&nbsp;&nbsp;``&nbsp;&nbsp;`

`&nbsp;&nbsp;`

`&nbsp;&nbsp;``&nbsp;&nbsp;`

`&nbsp;&nbsp;`

- 
`&nbsp;&nbsp;`

`  Just to test, even when we tried to upload smaller files (3 MB or even 100KB), we am getting a different error`

`&nbsp;&nbsp;`

`&nbsp;&nbsp;``&nbsp;&nbsp;`

`&nbsp;&nbsp;`

- 
`&nbsp;&nbsp;`

`  This might be due to what the customer said -`

`&nbsp;&nbsp;`

`&nbsp;&nbsp;`

- 
`To upload files in chunks with AWS S3 the minimum chunk size (except the last), is 5Mb&nbsp;&nbsp;`

- 
`&nbsp;&nbsp;`

`  Some literature on this info...a minimum chunk size of 5MB for AWS S3..`

- 
[https://docs.aws.amazon.com/AmazonS3/latest/userguide/qfacts.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/qfacts.html)`&nbsp;&nbsp;`

- 
`&nbsp;&nbsp;`

`  3rd party site&nbsp;`

- 
`&nbsp;&nbsp;`

[https://uppy.io/docs/aws-s3/#:~:text=S3%20requires%20a%20minimum%20chunk,it%20to%20S3's%20minimum%20requirements](https://uppy.io/docs/aws-s3/#:%7E:text=S3%20requires%20a%20minimum%20chunk,it%20to%20S3's%20minimum%20requirements)`.`

`&nbsp;&nbsp;`

`&nbsp;&nbsp;``&nbsp;&nbsp;`

`&nbsp;&nbsp;`

`&nbsp;&nbsp;`

`&nbsp;&nbsp;`

- 
`&nbsp;&nbsp;`

`  We are aware of these documents`

- 
https://outsystemsrd.atlassian.net/wiki/spaces/RDSD/pages/3488318580/ODC+known+quotas+and+limits`&nbsp;&nbsp;`

- 
https://outsystemsrd.atlassian.net/wiki/spaces/CloudKB/pages/3719987448/ODC+Known+Quotas+and+Limits`&nbsp;&nbsp;`

- 
[https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html)`&nbsp;&nbsp;`

- 
`  But since the customer has this situation of needing a minimum of 5MB for the upload, so its not clear how the above workarounds will be useful.`

`&nbsp;&nbsp;`

- 
`&nbsp;&nbsp;`

`  We are aware of a past case, quite similar`

- 
[https://outsystemsrd.atlassian.net/browse/RDINC-18468](https://outsystemsrd.atlassian.net/browse/RDINC-18468)`&nbsp;&nbsp;`

- 
`  But, again, its not clear if it same as this they are not using any Base64 conversion.`

`&nbsp;&nbsp;`

- 
`&nbsp;&nbsp;`

`  As such, the main question here is, why the 5.1 MB file size is showing up as 6.7 MB size in the request and thus being rejected by ODC.`

- 
`  Where does the &quot;extra&quot; size come from?`

- 
`  And is there is a way for the customer to workaround this situation.`

`&nbsp;&nbsp;`

`&nbsp;&nbsp;TECH DATA OR ANY OTHER RELEVANT INFO&nbsp;`

`Ring: ea&nbsp;`

`Tenant Id: 3313c749-2159-4df2-98e2-f29dbf73263e&nbsp;`

`Tenant Prefix: creetionodc&nbsp;`

`Region: eu-central-1`

`&nbsp;&nbsp;`

`&nbsp;Technical Support::Send to R&amp;D - ODC #trigger_send_to_r&amp;d_odc !&gt;&nbsp;&nbsp;`

`&nbsp;&nbsp;`

`&nbsp;&nbsp;Attachment(s):`

`POC_5Mb.zip -`[&nbsp;&nbsp;*https://supportoutsystems.zendesk.com/attachments/token/gp7XDRI0HGROwZoSZyfUOYkH7/?name=POC_5Mb.zip*&nbsp;&nbsp;](https://supportoutsystems.zendesk.com/attachments/token/gp7XDRI0HGROwZoSZyfUOYkH7/?name=POC_5Mb.zip)`&nbsp;&nbsp;`

`&nbsp;&nbsp;`&nbsp;&nbsp;

August 5  5:33 AM WEST

slack

paulo.monteiro.ferreira

[https://success.outsystems.com/documentation/outsystems_developer_cloud/building_apps/ex[&hellip;]al_logic_using_custom_code/external_libraries_sdk_readme/](https://success.outsystems.com/documentation/outsystems_developer_cloud/building_apps/extend_your_apps_with_external_logic_using_custom_code/external_libraries_sdk_readme/)**Use with large binary files**

Server actions exposed by external libraries don't support input larger than 5.5MB. If a large binary file is passed as input to a server action during an app's runtime, the end-user gets an error &quot;Input payload is too large&quot;. To make use of a large binary file in custom code you can:
1. Expose the binary file in a [REST API endpoint](https://success.outsystems.com/documentation/outsystems_developer_cloud/integration_with_external_systems/exposing_rest_apis/) from your app and then implement logic in your custom code to consume the file from the endpoint.
2. Host the binary file on a file-sharing service and implement logic in your custom code to download the file from the URL.

August 5  5:47 AM WEST

web

Rafael Duarte

Rafael Duarte has been assigned as Engineer

August 5  6:08 AM WEST

web

Rafael Duarte

Hi Support,The external logic feature is correctly validating the payload size, which is &gt; 5.5MB (as per the documentation and clear set limit). 
Its behavior has  not been compromised and is working as expected.Although the original file uploaded by the customer is 5MB, we can observe, in your screenshot, that when it is indeed uploaded, the size is already over 5.5MB, there's nothing the external library feature can do at this point as it has no control over file uploads.As observed by support, when the file is uploaded, the Content-Length in the request is 6.7 MB. this happens as the file is encoded in Base64 and sent in the JSON payload of the browser request, thus increasing the file size, similar to RDINC-18468.We will continue analyzing the issue on R&amp;D and try to provide a better solution for the customer, at the moment it is important to note that there are no issues with the platform, this is the expected behavior.Kind regards R&amp;D

August 5 11:33 AM WEST

web

Rafael Duarte

Re-assigning to backend runtime to provide additional context on file upload behavior.

August 5 11:34 AM WEST

web

Rafael Duarte

Rui Garcia has been assigned as Engineer

August 5  1:11 PM WEST

web

Rui Garcia

Teams has been removed: [Extended Runtime](/account/teams/extended-runtime/status)&nbsp;&nbsp;[SRE](/account/teams/sre/status)

August 5  1:13 PM WEST

web

Rui Garcia

Send ZenDesk private comment has been set: Our customer is relying on an External Library in order to achieve a specific use case.
It is relevant to be aware that the External Libraries in ODC are executing in a different execution environment than the application that consumes it. This architecture decision was made for a number of reason, primarily security and isolation, but what this [means is that](https://success.outsystems.com/documentation/outsystems_developer_cloud/building_apps/extend_your_apps_with_external_logic_using_custom_code/external_libraries_sdk_readme/):&gt; _Each time your app calls a server action from an external library, it makes an HTTPS call to an external service that hosts and runs the custom code. As a result, the execution context of these server actions is separate from the app._
So, every time an app makes a request, it serializes all necessary context and sends that in the form a JSON encoded payload. This payload must include all parameter values. In our customer example, a Binary Data input parameter is being sent. As standard practice dictates, when a Binary Data is to be sent across a text representation it must be encoded somehow, typically, base64 encoded to ensure not data is misrepresented or lost. Unfortunately, this means the Binary Data content will grow roughly four thirds, and this is why our customer sees that increase in size. From 5MB to roughly 6.7MB (1.67MB come from the Binary Data base 64 representation, the rest comes from the remaining parameter values).
As it is [documented](https://success.outsystems.com/documentation/outsystems_developer_cloud/building_apps/extend_your_apps_with_external_logic_using_custom_code/external_libraries_sdk_readme/),&gt; _Server actions exposed by external libraries don't support inputs larger than 5.5MB. If a large binary file is passed as input to a server action during an app's runtime, the end-user gets an error &quot;Input payload is too large&quot;. To make use of a large binary file in custom code you can:_
_Expose the binary file in a _[REST API endpoint](https://success.outsystems.com/documentation/outsystems_developer_cloud/integration_with_external_systems/exposing_rest_apis/)_ from your app and then implement logic in your custom code to consume the file from the endpoint._
_Host the binary file on a file-sharing service and implement logic in your custom code to download the file from the URL._
When this hard limit is reached a different approach must be considered. The document offers two. Depending on the use case, others may be valid, for example, generating a self-signed URL and have the file content be directly upload by the application client side.
If you need further assistance on this matter, please do not hesitate.

August 5  1:13 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:
Our customer is relying on an External Library in order to achieve a specific use case.
It is relevant to be aware that the External Libraries in ODC are executing in a different execution environment than the application that consumes it. This architecture decision was made for a number of reason, primarily security and isolation, but what this [means is that](https://success.outsystems.com/documentation/outsystems_developer_cloud/building_apps/extend_your_apps_with_external_logic_using_custom_code/external_libraries_sdk_readme/):&gt; _Each time your app calls a server action from an external library, it makes an HTTPS call to an external service that hosts and runs the custom code. As a result, the execution context of these server actions is separate from the app._
So, every time an app makes a request, it serializes all necessary context and sends that in the form a JSON encoded payload. This payload must include all parameter values. In our customer example, a Binary Data input parameter is being sent. As standard practice dictates, when a Binary Data is to be sent across a text representation it must be encoded somehow, typically, base64 encoded to ensure not data is misrepresented or lost. Unfortunately, this means the Binary Data content will grow roughly four thirds, and this is why our customer sees that increase in size. From 5MB to roughly 6.7MB (1.67MB come from the Binary Data base 64 representation, the rest comes from the remaining parameter values).
As it is [documented](https://success.outsystems.com/documentation/outsystems_developer_cloud/building_apps/extend_your_apps_with_external_logic_using_custom_code/external_libraries_sdk_readme/),&gt; _Server actions exposed by external libraries don't support inputs larger than 5.5MB. If a large binary file is passed as input to a server action during an app's runtime, the end-user gets an error &quot;Input payload is too large&quot;. To make use of a large binary file in custom code you can:_
_Expose the binary file in a _[REST API endpoint](https://success.outsystems.com/documentation/outsystems_developer_cloud/integration_with_external_systems/exposing_rest_apis/)_ from your app and then implement logic in your custom code to consume the file from the endpoint._
_Host the binary file on a file-sharing service and implement logic in your custom code to download the file from the URL._
When this hard limit is reached a different approach must be considered. The document offers two. Depending on the use case, others may be valid, for example, generating a self-signed URL and have the file content be directly upload by the application client side.
If you need further assistance on this matter, please do not hesitate.

August 5  1:13 PM WEST

web

Rootly

Send ZenDesk private comment has been unset

August 5  1:13 PM WEST

web

Rootly

MESSAGE SENT FROM R&amp;D:

August 5  1:35 PM WEST

web

Rui Garcia

Incident has been resolved

August 5  1:35 PM WEST

web

Rui Garcia

System-wide impact has been set: No

August 5  1:35 PM WEST

web

Rui Garcia

Impact has been set: Customer is trying to develop using External Libraries sending payloads beyond the supported limit.

August 5  1:35 PM WEST

web

Rui Garcia

Investigation and troubleshooting findings has been set: Everything is working as expected. This was a development question (probably shouldn't be a SEV2 to begin with).

August 5  1:35 PM WEST

web

Rui Garcia

Resolution has been set: Customer as multiple workarounds to choose depending on the application use case. These workarounds will bring complexity but are necessary given the limitations imposed by the underlying technology.