---
title: [Standard/Normal] Enable Launch Darkly Feature Toggle in ODC
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/5017010352/Standard+Normal+Enable+Launch+Darkly+Feature+Toggle+in+ODC
confluence_space: RKB
confluence_page_id: 5017010352
last_synced: 2026-04-09
owner: Process Engineering
---

# [Standard/Normal] Enable Launch Darkly Feature Toggle in ODC

This change applies to every ODC team using Launch Darkly feature toggles.
## 1. Summary
The feature toggles in Launch Darkly allow the teams to enable a specific part of the code/feature remotely at a given moment, making these changes available for the affected customers/rings/geos.

Most of these feature toggle changes have low risk and impact because the code was previously promoted through the SDLC regular process and tested with automated tests, according to the existing team practices. In these scenarios, no RFC is required, and the team can perform the change directly in Launch Darkly, ensuring that the toggle is enabled progressively through the rings.

However, there are some exceptions where an RFC is required, and this article aims to optimize the RFC creation, since the steps to enable a feature toggle are always the same.

**Are you wondering when to create an RFC to enable a feature toggle in Launch Darkly and/or whether you should create a Standard or Normal request? **
*Check **this document** for more details.*
## 2. General Information
**Change Type**

*Standard*

**Approved Normal RFC**

RFC-2492ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Change Risk**

*Low*

**Downtime Involved **

*No*

**Rollback Available**

*Yes*

**Implementation Team**

*Release Engineering*

**Component(s)/Asset(s)**

*ODC*

**Impact Description**

*No impact antecipated*
## 3. Pre-requisites### Inputs for execution
- 
Launch Darkly project &lt;e.g. unified-experience&gt;

- 
Project&rsquo;s environment &lt;e.g. Production&gt;

- 
Feature toggle identifier &lt;e.g. TG_CFGC_Enable_CSPScreen&gt;

- 
Enable conditions (Ring, Geo, Tenant)

### Technical requirements
- 
*Access to Launch Darkly project and environment identified in the inputs section*

### Communication
- 
*Notify the team via RFC comment or Slack Channel*

### Expected duration
*N/A*
## 4. Implementation Plan### Implementation actions- 
Go to the feature toggle page in Launch Darkly

- 
Enable targeting rules, if disabled

- 
Add a new custom rule or edit an existing rule, if it already exists

- 
Depending on the use case, choose one of the options below:
- 
Add/edit rule for a specific ring
- 
Description: &lt;Ring X&gt;

- 
Context kind: user

- 
Attribute: Ring

- 
Operator: is one of

- 
Possible values: -3, -2, -1, 1, 2, 3

- 
These values should be set as `str` (click on top of the value to switch types between `num` and `str`)

- 
Add/edit rule for a specific tenant
- 
Description: &lt;TenantPrefix&gt;

- 
Context kind: user

- 
Attribute: TenantId (or TenantPrefix)

- 
Operator: is one of

- 
Values: (include the TenantId or TenantPrefix correspondent to the customer)

- 
Change default rule to False

### Testing and validation plan
Testing of these capabilities, hidden behind a feature toggle, should occur during the pipeline execution, which should test the asset both with and without the new capability.

Optionally, there can be manual validation performed by the owner team to confirm that the feature is already enabled as per the specified conditions.

### Rollback plan- 
Go to the feature toggle page in Launch Darkly

- 
Revert the steps executed in the implementation plan, which can include:
- 
Disable the targeting rules

- 
Remove the whole rule that was added

- 
Remove the added values: Ring, TenantId, or TenantPrefix for existing rules

## 5. Post Implementation 
*N/A*
## 6. Other
N/A
## 7. Useful links/Related articles
- 
[Standard] Enable Launch Darkly feature toggles in ODC Consoles 

- 
Launch Darkly Feature Toggles Change Management