---
title: Baseline for tenant payloads provisioning
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/5677809751/Baseline+for+tenant+payloads+provisioning
confluence_space: RKB
confluence_page_id: 5677809751
last_synced: 2026-04-09
owner: Process Engineering
---

# Baseline for tenant payloads provisioning

# Awareness
From December 2025, the Tenant Lifecycle Team will be in charge of the tenant provisioning and deletion requests in the [Neo Tenant Provisioning](https://outsystemsrd.atlassian.net/jira/software/c/projects/RDTC/boards/1671) board.

The tenant provisioning will be carried out by a member of the TLC team through API requests using Insomnia (take a look at the document CMCP | Calling the Tenant provisioning API with Insomnia to learn how to use TLC APIs over Insomnia) and after activating the PIMs below:

Tenant on ring:

**DEV **= [SGIA_SSO_AWS-SSO_ODC_Tenant_Lifecycle](https://portal.azure.com/#view/Microsoft_Azure_PIMCommon/ActivationMenuBlade/~/aadgroup)

**TEST **= [SGIA_SSO_AWS-SSO_Phoenix_ring-minus2_PowerUser](https://portal.azure.com/#view/Microsoft_Azure_PIMCommon/ActivationMenuBlade/~/aadgroup)

**STAGE **= [SGIA_SSO_AWS-SSO_Phoenix_ring-minus1_PowerUser](https://portal.azure.com/#view/Microsoft_Azure_PIMCommon/ActivationMenuBlade/~/aadgroup)

To create a tenant following the approach above, a payload must be defined and below we will provide some baselines to be used.

The baselines **MUST** be updated according to the information defined by the requestor, such as [ Name, Prefix, Geo, Region, Admin Email and Name, Deployment Type, List of Environments and their characteristics such as Geo, Region, and Purpose ]
# Baseline for tenant payloads

 Keeping in mind that before using the desired payload to the TLC API POST **/api/v2/tenants**, replace the information according to the request (such as &ldquo;tenant ring&ldquo;, &ldquo;tenant prefix&ldquo;, &ldquo;admin name and email&ldquo;)!

## What about the block `features` in the payloads that follow?
Inside the `tenant` and `environments` blocks, you will see the block `features`.

The current available features are listed at API Changes - Entitlements Support 

Simplified tenant for development only760
- 
**Description:** Simplified tenant for development only

- 
**Deployment:** oscloud

- 
**Environments:** 1 (Development)

- 
**Highlighted Features:**

- 
maxAppsPerTenant: 50

- 
migrationsEnabled: true

- 
Simple and fast configuration

- 
**Use Case:** Quick testing, local development, prototyping

- 
**Payload**:

Tenant with multiple environments covering the entire development760
- 
**Deployment:** oscloud

- 
**Environments:** 3 (Development, NonProduction, Production)

- 
**Highlighted Features:**

- 
maxAppsPerTenant: 100

- 
migrationsEnabled: true

- 
supportLevel: level2

- 
**Use Case:** Complete CI/CD testing, validation of promotion between environments

- 
**Payload**:

Tenant with hybrid deployment (oscloud + on-premises)760
- 
**Deployment:** hybrid ⚠️

- 
**Environments:** 2 (Development, Production)

- 
**Edition:** OutSystems Developer Cloud Trial

- 
**Highlighted Features:**

- 
maxAppsPerTenant: 50

- 
migrationsEnabled: false

- 
Valid until: 2025-12-31

- 
**Use Case:** Hybrid deployment testing, validation of connectivity between cloud and on-premises

- 
**Payload**:

Tenant with premium features enabled760
- 
**Deployment:** oscloud

- 
**Environments:** 3 (Development, NonProduction, Production)

- 
**Highlighted Features:**

- 
maxAppsPerTenant: 200

- 
appSecurityPlus: true ✨

- 
privateGateway: true ✨

- 
supportLevel: level3

- 
subscriptionGracePeriod: 30 days

- 
**Use Case:** Premium features testing, advanced security validation

- 
**Payload**:

Trial tenant with 90-day limit760
- 
**Deployment:** oscloud

- 
**Environments:** 1 (Development)

- 
**Edition:** OutSystems Developer Cloud Trial

- 
**Highlighted Features:**

- 
maxAppsPerTenant: 10

- 
migrationsEnabled: false

- 
Period: 2024-12-12 to 2025-03-12 (90 days)

- 
**Use Case:** Trial expiration testing, limits validation

- 
**Payload**:

Tenant in European region760
- 
**Deployment:** oscloud

- 
**Region:** eu-west-1 🇪🇺

- 
**Geo:** EU

- 
**Environments:** 3 (Development, NonProduction, Production)

- 
**Highlighted Features:**

- 
maxAppsPerTenant: 100

- 
migrationsEnabled: true

- 
supportLevel: level2

- 
**Use Case:** Multi-region testing, GDPR and European compliance validation

- 
**Payload**:

Tenant with multiple portfolios760
- 
**Portfolios: **2 (Cloud, Hybrid)

- 
**Environments:** 5 (3 Development, 1 NonProducton, 1 Production)

- 
**Edition:** OutSystems Developer Cloud Trial

- 
**Highlighted Features:**

- 
maxAppsPerTenant: 10

- 
migrationsEnabled: false

- 
Period: 2024-12-12 to 2025-03-12 (90 days)

- 
**Use Case:** Trial expiration testing, limits validation

- 
**Payload**: