---
title: [Normal] Delete asset wrongly deployed higher than -2
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/5065869347/Normal+Delete+asset+wrongly+deployed+higher+than+-2
confluence_space: RKB
confluence_page_id: 5065869347
last_synced: 2026-04-09
owner: Process Engineering
---

# [Normal] Delete asset wrongly deployed higher than -2

This Change is part of the [https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/3798631729](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/3798631729).
## 1. Summary
In the context of Self Hosted there is a new Development Unit called shregistratoinunit.
It got promoted into rings higher than -2 by mistake (it was not blocked yet by the &ldquo;Athena Stop&rdquo; command when the dev gate was removed). Therefore 8 versions got accidentally promoted until GA before we blocked the pipeline.

We want:
- 
to ban all those 8 versions that got deployed, preventing them to be deployed again automatically into higher rings.

- 
to delete the asset from every ring where it got deployed higher than -2 (test)

We are still in development phase, so the final version will be a different one.

It is a new asset, **ONLY **used in the Self Hosted functionality that still in development phase, so there won&rsquo;t be any impact in any of those rings.
## 2. General Information
**Change Type**

Normal

**Approved Normal RFC**

*Applicable only for Standard Changes*

*&lt;Jira link of the Normal Request for Change submitted to approve the promotion of this change from Normal to Standard Change&gt;*

**Change Risk**

Low* *Risk Matrix Calculation 

**Downtime Involved **

No

**Rollback Available**

No

**Implementation Team**

SDLC

**Component(s)/Asset(s)**

shregistratoinunit

**Impact Description**

It is a new asset, **ONLY **used in the Self Hosted functionality that still in development phase, so there won&rsquo;t be any impact in any of those rings.
## 3. Pre-requisites### Inputs for execution
- 
None

### Technical requirements
- 
None

### Communication
- 
 (PaaS Value Stream leader)

- 
 (Eng. Manager)

- 
 (PO/VM coordinator)

- 
 (Product Owner)

### Expected duration
*It should be SDLC team who says how long it may take.*

## 4. Implementation Plan### Implementation actions- 
to delete the asset from every ring where it got deployed higher than -2 (test) and remove it from the gitops repos in all necessary rings

### Testing and validation plan
Not needed
### Rollback plan
Not needed
## 5. Post Implementation 
Not needed
## 6. Other
- 
Not needed

## 7. Useful links/Related articles
- 
Slack conversation: [https://outsystems.slack.com/archives/C02FDRXNER0/p1745241207253529](https://outsystems.slack.com/archives/C02FDRXNER0/p1745241207253529)