---
title: [Standard] PowerUser to access negative rings to execute read-only operations on RDS database
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/5047713793/Standard+PowerUser+to+access+negative+rings+to+execute+read-only+operations+on+RDS+database
confluence_space: RKB
confluence_page_id: 5047713793
last_synced: 2026-04-09
owner: Process Engineering
---

# [Standard] PowerUser to access negative rings to execute read-only operations on RDS database

This runbook has the purpose to replace these:

[Standard]&nbsp;Get PowerUser access to negative rings (-2 and -1) to execute 'select' queries on RDS database 

[Standard]&nbsp;Get PowerUser access to negative rings to execute select queries on PS database
## 1. Summary
To address potential issues associated with negative rings in the Aurora v2 database for the services that depend on it, it is essential to obtain Power User permissions to effectively utilize the Data API. Each service has a designated user wich is configured with `SELECT-`only privileges.

## 2. General Information
**Change Type**

Standard

**Change Risk**

Low

**Downtime Involved **

No

**Rollback Available**

No

**Implementation Team**

Team owner of the service

**Component(s)/Asset(s)**

No change applied. ReadOnly only.

**Impact Description**

Run select queries on the Aurora v2 database.
## 3. Pre-requisites### Inputs for execution
- 
`&lt;service-database-name&gt;` (e.g. `application_versioning`, `publish`)

- 
`&lt;readonly-user-service&gt;` (e.g. `readonly-user-application-versioning-service`, `readonly-user-publish-service`)

- 
`&lt;database-instance/cluster&gt;` (e.g. `pgdb-c1d9fd63-a27f-e06f-fff8-73e75e99c436`, `pgdb-c9bf2aea-32d4-5786-9c40-64aed2b68300`)

### Technical requirements
- 
Access AWS Console with the Power User role

### Communication
N/A
### Expected Duration
N/A
## 4. Implementation Plan### Implementation actions- 
Access the AWS Console with the Power User role in the intended region

- 
Go to `Secrets Manager` search for the secret `&lt;readonly-user-service&gt;`, and copy the secret ARN

- 
Select the `Query Editor` on the RDS

- 
Select the database instance/cluster `&lt;database-instance/cluster&gt;`

- 
Select the Secret ARN copied in the step 2

- 
Enter the name of the database `&lt;service-database-name&gt;`

- 
Run the select query, e.g.: `SELECT ? FROM ? WHERE ?;`

### Testing and validation plan
N/A
### Rollback plan
N/A
## 5. Post Implementation 
N/A
## 6. Other
N/A
## 7. Useful links/Related articles
[https://outsystemsrd.atlassian.net/wiki/x/DIAYwQ](https://outsystemsrd.atlassian.net/wiki/x/DIAYwQ)

[https://outsystemsrd.atlassian.net/wiki/x/DYHVpQ](https://outsystemsrd.atlassian.net/wiki/x/DYHVpQ)

[https://outsystems-sso.awsapps.com/start/#/?tab=accounts](https://outsystems-sso.awsapps.com/start/#/?tab=accounts)

[Azure My roles | Groups](https://portal.azure.com/#view/Microsoft_Azure_PIMCommon/ActivationMenuBlade/~/aadgroup)