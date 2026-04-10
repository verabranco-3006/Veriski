---
title: [TEMPLATE] [Standard/Normal/Emergency] Document a New Change
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/3801350783/TEMPLATE+Standard+Normal+Emergency+Document+a+New+Change
confluence_space: RKB
confluence_page_id: 3801350783
last_synced: 2026-04-09
owner: Process Engineering
---

# [TEMPLATE] [Standard/Normal/Emergency] Document a New Change

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

This Change is part of the [https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/3798631729](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/3798631729).
## 1. Summary
*&lt;Provide a brief overview of what this change aims for. Also, highlight any details that might be worth referencing before anything else, even before moving forward with the change.&gt;*

*e.g. This operation to Restore a Database of a production environment may be required following a Disaster Recovery operation.*

*&lt;Please bear in mind that using this operation on an environment X also impacts other environments.&gt;*
## 2. General Information
**Change Type**

*&lt;Standard, Normal, Emergency&gt;*

**Approved Normal RFC**

*Applicable only for Standard Changes*

*&lt;Jira link of the Normal Request for Change submitted to approve the promotion of this change from Normal to Standard Change&gt;*

**Change Risk**

*&lt;Low, Medium, High&gt; *Risk Matrix Calculation 

**Downtime Involved **

*&lt;Yes, No&gt; &lt;Time Window: 1h, 2h&gt;*

**Rollback Available**

*&lt;Yes, No&gt;*

**Implementation Team**

*&lt;e.g. Identity&gt;*

**Component(s)/Asset(s)**

*&lt;e.g. Keycloak&gt;*

**Impact Description**

*&lt;Any impact that the change might bring.&gt; *
## 3. Pre-requisites### Inputs for execution
- 
*&lt;List any inputs that must be considered before moving forward.*

- 
*e.g. identify if the targeted environment is the correct one;*

- 
&hellip;&gt;

### Technical requirements
- 
*&lt;List any technical requirements to make the changes.*

- 
*e.g. validate if the targeted platform has the necessary access rights and permissions;*

- 
*&hellip;&gt;*

### Communication
- 
*&lt;List any critical communications and people that must be informed about the change (the overall organization, the team, the Global Support team, the alarmistic team, and/or even the customers), and how it will be communicated.*

- 
*Example of Communication:*

- 
*Effective Implementation Date: [Date]*

- 
*Downtime Expected: [Time Window, Start and End Date]*

- 
*What is changing: [Explain the details of the change, including any relevant processes, systems, or procedures that will be affected.]*

- 
*Why is it changing: [Explain the reasons behind the change and the expected benefits.]*

- 
*How it affects you: [Describe how this change may impact individuals or teams, and provide any necessary instructions or resources.]*

- 
*&hellip;&gt;*

### Expected duration
*&lt;State how much time on average this change takes, e.g. from the initial commit date to the repository to the moment when the change becomes active in each ring.&gt;*

## 4. Implementation Plan### Implementation actions
*&lt;Step-by-step implementation guide for the change. Include details like tasks, responsible parties, and completion dates, if applicable.*
- 
*e.g. go to X and do Y,*

- 
*&hellip;*

- 
*&hellip;&gt;*

### Testing and validation plan
*&lt;Specify the testing process for the change and any techniques or methodologies that might be used e.g. manual, automated, or exploratory testing, etc. List the criteria used to validate the success of the change.&gt;*
### Rollback plan
*&lt;Establish a clear and tested rollback plan in case the change causes unforeseen issues. This plan should allow for a quick and controlled return to the previous state.&gt;*
## 5. Post Implementation 
*&lt;State here all the actions that might need to be performed after change implementation.*
*e.g. the steps that verify that the change was successful and that everything is functioning as expected after its implementation.&gt;*
## 6. Other
- 
&hellip;

- 
&hellip;

## 7. Useful links/Related articles
- 
&hellip;

- 
&hellip;