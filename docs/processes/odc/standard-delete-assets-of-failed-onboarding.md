---
title: [Standard] Delete assets of failed onboarding
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4896915527/Standard+Delete+assets+of+failed+onboarding
confluence_space: RKB
confluence_page_id: 4896915527
last_synced: 2026-04-09
owner: Process Engineering
---

# [Standard] Delete assets of failed onboarding

To request Emergency/Normal Product Infrastructure Changes [ODC + other services] please follow the work instructions. 

[https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/3862331705/Change+Management+Process#Record-Request-for-Changes](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/3862331705/Change+Management+Process#Record-Request-for-Changes) 

## 1. Summary
Delete assets that were not automatically deleted after undeploy of app-editor and workflow-editor

*No other apps/environments will be affected since this from an in progress onboarding*
## 2. General Information
**Change Type**

*Standard*

**Approved Normal RFC**

*Applicable only for Standard Changes*

*&lt;Jira link of the Normal Request for Change submitted to approve the promotion of this change from Normal to Standard Change&gt;*

**Change Risk**

*Low*

**Downtime Involved **

*No*

**Rollback Available**

*No*

**Implementation Team**

*Morpheus*

**Component(s)/Asset(s)**

*workflow editor, app editor*

**Impact Description**

*No impact since this comes from a failed onboarding and assets need to be deleted*
## 3. Pre-requisites### Inputs for execution
In Account: 324616802078
Resources to delete
	- delete content of s3 bucket web-editors-plat-test-us-east-1-01
	- delete CRs CloudServiceAccount: outsystems-app-editor e outsystems-workflow-editor
	- delete CRs ObjectStore: web-editors-plat-test-us-east-1-01
### Technical requirements
- 
*&lt;List any technical requirements to make the changes.*

- 
*e.g. validate if the targeted platform has the necessary access rights and permissions;*

- 
*&hellip;&gt;*

### Communication
- 
*N/A*

### Expected duration
*N/A*

## 4. Implementation Plan### Implementation actions
*N/A*
### Testing and validation plan
*N/A*
### Rollback plan
*N/A*
## 5. Post Implementation 
*N/A*