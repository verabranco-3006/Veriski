---
title: [Normal] Extending S3 backups to ODC Forge
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/5141364968/Normal+Extending+S3+backups+to+ODC+Forge
confluence_space: RKB
confluence_page_id: 5141364968
last_synced: 2026-04-09
owner: Process Engineering
---

# [Normal] Extending S3 backups to ODC Forge

To request Emergency/Normal Product Infrastructure Changes [ODC + other services] please follow the work instructions. 

[https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/3862331705/Change+Management+Process#Record-Request-for-Changes](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/3862331705/Change+Management+Process#Record-Request-for-Changes) 

This Change is part of the ODC Change Catalog .
## 1. Summary
In RFC-2910 we have deployed S3 backups to the Platform Stamp, safeguarding customer IP in the process. In this process, we are extending the S3 backups to the Forge Stamp, which include all Forge assets that are created and exposed by our customers, as well as the ones produced by our teams.

These backups are specific to the Forge stamp, in US/East (Virginia), for Ring +3/GA. This hosts the Forge for all positive rings (+1/Community, +2/EA and +3/GA).

## 2. General Information
**Change Type**

Normal

**Approved Normal RFC**

*Applicable only for Standard Changes*

*&lt;Jira link of the Normal Request for Change submitted to approve the promotion of this change from Normal to Standard Change&gt;*

**Change Risk**

Low [cost]* *Risk Matrix Calculation 

**Downtime Involved **

No

**Rollback Available**

Yes

**Implementation Team**

SRE

**Component(s)/Asset(s)**

S3 buckets in Forge stamp

**Impact Description**

Activating these backups will incur costs for backing up storage. Given the low size (&asymp; 100GB), the estimate is less than 100 USD/month.
## 3. Pre-requisites### Inputs for execution
- 
Deployment of the stacksets that create the vault for the S3 backups in each account, and the IAM roles - IAM ticket #TBD. These will be used by the centralized AWS policy running in account 387229418815, and have been tested and implemented previously in RFC-2910 for a different (bigger) set of S3 buckets;

### Technical requirements
- 
*Administrator* access to AWS account 387229418815 (master account for AWS Backup for ODC) - granted to SRE Alpha team

- 
Read-only access to Ring3 AWS accounts via PIM (required to confirm backup status)

### Communication
- 
ODC leadership to be informed once the backups are started, and once they are in sync (meaning: we are covered) [Ac&aacute;cio + Tiago Garcia]

### Expected duration
The actual implementation will take 2 hours. Then it will require daily validation of the state of the backups until all buckets are in state Completed.

## 4. Implementation Plan### Implementation actions- 
Access AWS console and perform SSO to account 387229418815

- 
Access the AWS backup service, and navigate to My Organization =&gt; Backup policies

- 
Identify policy with name **ODC_S3_Backup** and ID **p-897ouvltim**, and open it;

- 
Click &ldquo;Attach&rdquo; in the Targets section

- 
Select the OU **ODC_Prod_Customer =&gt; Ring 3 =&gt; Forge_Stamp**

### Testing and validation plan- 
In the AWS console, login as account 452996290923 (ring +3, Forge Stamp, us-east-1/Virginia)

- 
Access the AWS Backup service

- 
Locate the Backup vault S3Backups

- 
Under Backup plans, locate the backup plan s3backupplan

- 
Confirm that the objects are backing up (some might already be concluded)

### Rollback plan- 
Access AWS console and perform SSO to account 387229418815

- 
Access the AWS backup service, and navigate to My Organization =&gt; Backup policies

- 
Identify policy with name ODC_S3_Backup and ID p-897ouvltim, and open it;

- 
Remove from target **ODC_Prod_Customer =&gt; Ring 3 =&gt; Forge_Stamp**

## 5. Post Implementation 
Backups should be quick to conclude (less than 2 hours), so status of backups needs to be checked in the console, until all buckets show up in state Completed.
## 6. Other
- 
n/a