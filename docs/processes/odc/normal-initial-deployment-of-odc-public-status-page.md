---
title: [Normal] Initial deployment of ODC Public Status Page
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4755390544/Normal+Initial+deployment+of+ODC+Public+Status+Page
confluence_space: RKB
confluence_page_id: 4755390544
last_synced: 2026-04-09
owner: Process Engineering
---

# [Normal] Initial deployment of ODC Public Status Page

To request Emergency/Normal Product Infrastructure Changes [ODC + other services] please follow the work instructions. 

[https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/3862331705/Change+Management+Process#Record-Request-for-Changes](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/3862331705/Change+Management+Process#Record-Request-for-Changes) 
note
Please, find below the **Template to Document a New Product Infrastructure Change [ODC + other services]. **

Feel free to copy this page to your workspace and update the title not forgetting to:

- 
eliminate the [TEMPLATE] brackets,

- 
**Always** indicate the type of change [Standard/Normal/Emergency]&nbsp;in the title

- 
replace the * Document a New Change * with the title that better reflects what is the change you are documenting.

Please, find below the **Template to Document a New Product Infrastructure Change [ODC + other services]. **

Feel free to copy this page to your workspace and update the title not forgetting to:

- 
eliminate the [TEMPLATE] brackets,

- 
**Always** indicate the type of change [Standard/Normal/Emergency]&nbsp;in the title

- 
replace the * Document a New Change * with the title that better reflects what is the change you are documenting.

This Change is part of the **Site Reliability Team&rsquo;s Change Catalog.**
## 1. Summary
*OutSystems has had a public status page for long, reflecting the status of a few services (including web properties and some Platform auxiliary services, like MABS) but has naver had anything reflecting the status of one of its main product lines. This is changing now, by adding status of ODC in the public status page.*

*The change request  is regarding the way the configuration of the asset used for the status page (*[*StatusPage.IO*](http://StatusPage.IO)*) will be performed. *[*StatusPage.IO*](http://StatusPage.IO)* offers 2 methods for configuration: UI and API. Since there is no &quot;apply changes&quot; option, performing the changes via UI would mean a period of 30min-2h in which the page is in a &quot;draft state&quot;; since it's an asset that is live, this would be undesirable.*

*So the change will be performed via API, in code. The change is performed with scripts using Bruno as a tool, with some minor parts of the Change requiring use of the UI.*
## 2. General Information
**Change Type**

*Normal*

**Approved Normal RFC**

*Applicable only for Standard Changes*

*&lt;Jira link of the Normal Request for Change submitted to approve the promotion of this change from Normal to Standard Change&gt;*

**Change Risk**

*Medium *Risk Matrix Calculation 

**Downtime Involved **

*No*

**Rollback Available**

*Yes*

**Implementation Team**

*Site Reliability Engineering; Global Support*

**Component(s)/Asset(s)**

*Other Services - Public Status Page*

**Impact Description**

*Incorrect change my negatively reflect on OutSystems' image, since this is a public facing asset.*
## 3. Pre-requisites### Inputs for execution
- 
UI full access to [production status page](https://manage.statuspage.io/pages/w2l85pjbb8m3/components);

- 
API key for the production status page;

- 
UI read-only access to [test status page](https://manage.statuspage.io/pages/945lhv1b91g3/incidents) (to copy communication templates);

### Technical requirements
- 
Bruno ([www.usebruno.com](http://www.usebruno.com));

- 
Access to Google Drive files - [rollout](https://drive.google.com/file/d/1cS6Ji9npQOUTIozfws1WVKBhNMXwmFg1/view?usp=drive_link) and [rollback](https://drive.google.com/file/d/1LF5mNUAZNCWEUid53b8vADsROf8p7nTo/view?usp=drive_link) Bruno collections.

### Communication
- 
As part of the rollout plan, Product Management has a communication strategy and plan that will be managed outside of the scope of the RFC.

- 
Dan Iorg (PM) to be informed of successful rollout to trigger the communication plan.

### Expected duration
About 2 hours, from 10h to 12h on Tuesday, Jan 14.
## 4. Implementation Plan### Implementation actions- 
Take a screenshot of the Status Page at [status.outsytems.com](http://status.outsytems.com). Should look like [this](https://drive.google.com/file/d/11p3xBn6aCGgESu_mJ69lfVmLjRUfgSuQ/view?usp=drive_link);

- 
Obtain the rollout Bruno collection, extract to laptop, load it in Bruno;

- 
Open Collection settings (Developer Mode), configure the following:
- 
PAGE_ID: w2l85pjbb8m3

- 
AUTH_KEY: get from the secure repository

- 
***Gather screenshot (blur the AUTH_KEY field) and place it ***[***here***](https://drive.google.com/drive/folders/1hr41IyG1KSzMo4xPrhyCr7zjfYIOXVrB)

- 
Run the collection in Bruno:
- 
Right-click, Run

- 
Delay (in ms): 1200

- 
Run Collection

- 
***Gather screenshot of the run collection** **and place it ***[***here***](https://drive.google.com/drive/folders/1hr41IyG1KSzMo4xPrhyCr7zjfYIOXVrB)
(This will rename the existing sections, and add new ODC sections).

- 
Access the UI [here](https://manage.statuspage.io/pages/w2l85pjbb8m3/components). Reorder the components until the order is:
- 
ODC - Customer Apps and Data

- 
ODC - Platform and Portal

- 
ODC - Identity &amp; Access Management

- 
Online Community

- 
Other OutSystems Services

### Testing and validation plan
Confirm the final page looks like [this](https://drive.google.com/file/d/1bC_rN7hOUrRKXQA1bCPDVgrYUmh9dN0t/view?usp=drive_link), after expanding all fields. Ignore the logo in the sample screenshot (it says TEST, it should be a simple OutSystems logo). ***Gather screenshot of the result** **and place it ***[***here***](https://drive.google.com/drive/folders/1hr41IyG1KSzMo4xPrhyCr7zjfYIOXVrB)***.***
### Rollback plan- 
Obtain the rollback Bruno collection, extract to laptop, load it in Bruno;

- 
Open Collection settings (Developer Mode), configure the following:
- 
PAGE_ID: w2l85pjbb8m3

- 
AUTH_KEY: get from the secure repository

- 
***Gather screenshot (blur the AUTH_KEY field) and place it ***[***here***](https://drive.google.com/drive/folders/1hr41IyG1KSzMo4xPrhyCr7zjfYIOXVrB)

- 
Run the collection in Bruno:
- 
Right-click, Run

- 
Delay (in ms): 1200

- 
Run Collection

- 
***Gather screenshot of the run collection** **and place it ***[***here***](https://drive.google.com/drive/folders/1hr41IyG1KSzMo4xPrhyCr7zjfYIOXVrB)
(This will rename the existing sections, and add new ODC sections).

## 5. Post Implementation 
n/a