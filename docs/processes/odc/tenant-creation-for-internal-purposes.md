---
title: Tenant creation for Internal purposes
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/3130163365/Tenant+creation+for+Internal+purposes
confluence_space: RKB
confluence_page_id: 3130163365
last_synced: 2026-04-09
owner: Process Engineering
---

# Tenant creation for Internal purposes

The objective of this page is to offer a process to guide and moderate the creation of the ODC Tenants that Internal teams need, being for temporary needs (specific time-bound events or tests) or longer needs, when, for example, a team will need to have a tenant as part of the development lifecycle.

Internal tenants can only be created in negative rings. No tenant will be created in the positive ring using this process.

Every Tenant has a cost for OutSystem that will be decreased as we progress with ODC work, but it is not marginal right now, so we need to use discretion and good judgment in managing the creation of new tenants.
## Public Communication### Public Slack channel
#[neo-tenant-provisioning](https://outsystems.slack.com/archives/C03MTGZK0QJ)

Use this Slack channel for any questions regarding tenant provisioning.
## Internal Tenant Provisioning Process 
https://miro.com/app/live-embed/uXjVOpoPZoM=?boardAccessToken=IjOWpi3KCG27hA7FZsynTFRIj3beGmLQ&amp;autoplay=true
## Jira Project
[RDTC](https://outsystemsrd.atlassian.net/jira/software/c/projects/RDTC/boards/1671)
### Workflow

- 
**TO DO**: Any ticket created in the project will be in this column for EngOps to check if something else is missing.

- 
**Approval review**: A group of EngOps will review the request.

- 
**Accepted/Rejected**:  

- 
**Approved**: All tickets that have been approved will continue the flow of the tenant creation.

- 
**Rejected**: Rejected tickets, those who rejected them have to specify the reasons for the decision. Can also be marked as **Discarded** directly in the Issue.

- 
**Support**: A Zendesk ticket with the request will be created, and Support will trigger the standard tenant creation process.

- 
**Waiting to be deleted: **Tickets in this column mean that the tenants are being used, and we are waiting for the due date. Once this is reached, EngOps will reach the requestor or the DRI of that tenant to make sure we can delete it. 

- 
We can delete it: EngOps will create the Support ticket with all the required information for the deletion.

- 
We CAN&rsquo;T delete it: We will ask for the main reasons, and for another due date, so we can follow this tenant lifecycle.

- 
**Finished process**: The tenant has been created, used, and deleted correctly.

**In case of error:**

- 
We will flag the ticket to show that something is happening with that specific ticket, and EngOps will review and unblock the situation.

### Ticket creation

**Summary**: Brief explanation regarding the needs of the tenant

**Description**: The purpose of the tenant and its objective. Concrete needs and use case explanation.

**Team**: The name of the team that is requesting the tenant

**Tenant Name**: Proposal for the tenant name

**Tenant owner Email**: email of the owner

**Tenant Owner Name**: Name of the owner of the tenant

**Tenant URL prefix**: Proposal for the tenant URL (there&rsquo;s a limit of 20 characters)

**The naming convention for the tenant prefix:**

eng-&lt;ring (options: dev/test/stage/osdr/ea/ga)&gt;-&lt;Descriptive name&gt;

**Ring/Environment**: Ring where we need the tenant to be created.

**Customer Name**: Tenant&rsquo;s Owner Name(Fill it in with &ldquo;**OutSystems**&rdquo; for internal purposes)

**Geo**: Geo

**Region**: Region

**Account Name**: Always is: &ldquo;Outsystems internal&rdquo; for internal requests unless someone specifies otherwise.

**Due Date: **Until when this tenant is expected to be required. This date is used to keep track of the temporal tenants and will be used as a reminder to get in touch with the owner to understand if we can proceed with its deletion.

**ODC Edition:** Related to AO limits and usage. For internal teams, use the default &ldquo;OutSystems Developer Cloud Platform 2023&ldquo;.
## Ring Selection logic
Internal tenants can only be created in negative rings. No tenant will be created in the positive ring using this process.

Tenants in negative rings are created by the Tenant Lifecycle Team.

The TLC Team member monitors the [Neo Tenant Provisioning](https://outsystemsrd.atlassian.net/jira/software/c/projects/RDTC/boards/1671) board once per week and will create the tenants based on the instructions Baseline for tenant payloads provisioning .

For urgent tenant creation, after creating the request in the [Neo Tenant Provisioning](https://outsystemsrd.atlassian.net/jira/software/c/projects/RDTC/boards/1671) board, please post a request in the Slack channel [#rd-tenant-lifecycle](https://outsystems.enterprise.slack.com/archives/C02AB86U64F).

**Rings -3,-2,-1**: Only Dev Teams should request tenants into these rings

**Ring 1**: Evaluation Edition tenants

**Ring 2**: SA, marketing

**Ring 3**: Customers

Rings +1, +2, and +3 are not meant to be used internally, only by prospects and clients. 
These rings are customer revenue(COGS) and must not be used for testing purposes; also, testing in production can be considered a violation of SOC II.
## Operating Model - Handling Requests
The Operating Model for the Core Cloud Platform Team to handle requests can be found in this document: [[RESTRICTED] ODC Internal Tenant Provisioning - Google Docs](https://docs.google.com/document/d/1mIDLTZp71YmFPyZeBtioQW_7vz4Z_Yz1D2g655sxicM/edit#)