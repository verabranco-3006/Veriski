---
title: [Normal] Add a region to the ODC Public Status Page
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/5407376396/Normal+Add+a+region+to+the+ODC+Public+Status+Page
confluence_space: RKB
confluence_page_id: 5407376396
last_synced: 2026-04-09
owner: Process Engineering
---

# [Normal] Add a region to the ODC Public Status Page

To request Emergency/Normal Product Infrastructure Changes [ODC + other services] please follow the work instructions. 

Change Management Process 
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
*As part of the normal lifecycle of the Status page, we may need to add regions to the existing assets in the Status Page. To simplify the process, a template for region adding (which should be updated every time the status page is changed) has been created, streamlining the addition of regions.*

*The change request is regarding the way the configuration of the asset used for the status page (*[*StatusPage.IO*](http://StatusPage.IO)*) will be performed. *[*StatusPage.IO*](http://StatusPage.IO)* offers 2 methods for configuration: UI and API. Changes should be performed via API, in code; using UI only for minor things, or changes not supported via API. *

*The change is performed with scripts using Bruno as a tool, with some minor parts of the Change requiring use of the UI.*
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
EXPECTED LOOK of the new page, in a screenshot taken from the TEST environment

### Technical requirements
- 
Bruno ([www.usebruno.com](http://www.usebruno.com));

- 
Deploy and Rollback Bruno scripts (based on the template attached to this document), already customized to the region being added, and tested in Dev and Test.
  

### Communication
- 
Communication plans, when required, will be added to the RFC.

### Expected duration
Less than 30 minutes
## 4. Implementation Plan### Implementation actions- 
Take a full screenshot of the Status Page at [http://status.outsystems.com](http://status.outsystems.com).** Attach it to the RFC**;

- 
Obtain the **Deploy** Bruno collection, extract to laptop, load it in Bruno;

- 
Open Collection settings (Developer Mode), configure the following:
- 
PAGE_ID: w2l85pjbb8m3

- 
AUTH_KEY: get from the secure repository

- 
Confirm the correct values for NEW_REGION and START_DATE (format is YYYY-MM-DD)

- 
***Gather screenshot (blur the AUTH_KEY field) and attach it to the RFC***

- 
Run the collection in Bruno:
- 
Right-click, Run

- 
Delay (in ms): 1100

- 
Run Collection

- 
***Gather screenshot of the run collection** **and attach it to the RFC.***

- 
Access the UI [here](https://manage.statuspage.io/pages/w2l85pjbb8m3/components). Reorder the newly created regions under Components &rarr; Edit, for each of the 4 groups (ODC - Customer Apps &amp; Data ; ODC - Platform and Portal ; ODC - Identity &amp; Access Management ;  Mentor) &ndash; new order must be indicated in RFC.

### Testing and validation plan
Confirm the final page looks like EXPECTED_LOOK in RFC, after expanding all fields.  ***Gather screenshot of the result** **and attach it to the RFC.***
### Rollback plan- 
Obtain the **Rollback** Bruno collection, extract to laptop, load it in Bruno;

- 
Open Collection settings (Developer Mode), configure the following:
- 
PAGE_ID: w2l85pjbb8m3

- 
AUTH_KEY: get from the secure repository

- 
***Gather screenshot (blur the AUTH_KEY field) and attach it to the RFC***

- 
Run the collection in Bruno:
- 
Right-click, Run

- 
Delay (in ms): 1200

- 
Run Collection

- 
***Gather screenshot of the run collection** **and attach it to the RFC***

- 
Confirm result is equal to the original screenshot, captured at the beginning of the procedure.

## 5. Post Implementation 
n/a