---
title: Major Updates - Special Procedure
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4120510802/Major+Updates+-+Special+Procedure
confluence_space: RKB
confluence_page_id: 4120510802
last_synced: 2026-04-09
owner: Process Engineering
---

# Major Updates - Special Procedure

Major Updates on certain assets must be evaluated ahead of time, due to dependencies that are not identified.

The goal is to release a communication attached to the Change Request every time a Major Update is planned to be deployed (1 week in advance) informing the Reviewers and Cohort Leaders that the update will occur and which services will be impacted.

The update will be rolled out after approval and soak on ring -2 for at least one week (subject to change based on future soak times updates).
### How will the Major Updates be documented and communicated?- 
Major Updates will be raised as Normal Changes through a specific &lsquo;[Major Upgrades - Request for Change&rsquo; form](https://outsystemsrd.atlassian.net/jira/software/c/projects/RFCD/forms/form/direct/4/12523) created on the RFCD Project, and the automatically assigned *Reviewer *is .

The &lsquo;*Planned Date&rsquo;***** *field is only mandatory in this form and not editable in the RFC itself. 
The goal is to use the stated date in the communication sent to all the interested parties.
- 
In 2 different moments, a communication will be sent to the DL [rd.cloud.platform.notifications@outsystems.com](mailto:rd.cloud.platform.notifications@outsystems.com) and the slack channel of  [#rd-odc-dev](https://outsystems.slack.com/archives/C02DKPZK72L). The following teams should be tagged:
`@ice-team `
`@rd.cloud.management.control.plane.team `
`@grs.team `
`@observabilityengops `
`@odc.backendruntime.team `
`@odc.extendedruntime.team `
`@odc.runtimedatamodel.team `
`@odc.clientruntime.team `
`@identity-core `
`@identity-business `
`@maestro `
`@theseus.team `
`@rd-dna-datafabric-engine-team `
`@reng-team `
`@rd-management-consoles-team`

Communication sent on the RFC transition to 'Approved By CAB' status
A major update is planned to go into Ring -3 on *MM/DD/YYYY* for the following service:
*&lt;SERVICE_NAME&gt;*

Description:
*{{issue.description}}*

[CALL FOR ACTION]
Please take time to review this Request for Change (RFC), assess if your service is affected and perform any needed action on your side.

If you have any questions, please reach out to the respective team's public channel: 
ICE (#rd-ice-team), 
GRS (#rd-grs-public), 
CMCP (#rd-cloud-management-control-plane)
Communication sent on the RFC transition to 'Completed' status
The upgrade planned for *MM/DD/YYYY* was implemented. Below find the affected service and a brief description of the upgrade.
*&lt;SERVICE_NAME&gt;*

Description:
*{{issue.description}}*

If you have any questions, please reach out to the respective team's public channel: 
ICE (#rd-ice-team), 
GRS (#rd-grs-public), 
CMCP (#rd-cloud-management-control-plane)