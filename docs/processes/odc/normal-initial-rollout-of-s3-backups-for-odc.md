---
title: [Normal] Initial rollout of S3 backups for ODC
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/5123506262/Normal+Initial+rollout+of+S3+backups+for+ODC
confluence_space: RKB
confluence_page_id: 5123506262
last_synced: 2026-04-09
owner: Process Engineering
---

# [Normal] Initial rollout of S3 backups for ODC

To request Emergency/Normal Product Infrastructure Changes [ODC + other services] please follow the work instructions. 

[https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/3862331705/Change+Management+Process#Record-Request-for-Changes](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/3862331705/Change+Management+Process#Record-Request-for-Changes) 

This Change is part of the ODC Change Catalog .
## 1. Summary
As of today, S3 buckets used in the ODC deployment architecture are not being backed up. This has multiple reasons, related to the unlikelihood of a mistaken deletion:

- 
S3 buckets have versioning enabled. This means that, in the event of a file deletion, it could simply be recovered from the version in a reasonable period;

- 
S3 buckets cannot be deleted unless they are empty. In case of human error, it would have to be a double-error (delete all files first; delete the bucket);

- 
S3 buckets are currently huge. According to an architecture [analysis](https://outsystemsrd.atlassian.net/wiki/spaces/RDSD/pages/4911530113/ODC+Data+Protection+Backups#S3-Buckets), in April 2025 the total size of the Ring +3 buckets was of about 130TB, which translates into multiple days/weeks backup time, and a cost of &asymp;&nbsp;10.000USD per month in backups alone.

Regardless, having backups of everything is always a good policy, and a recent event in which a tenant was intentionally deleted by mistake (taking with it all customer OML) shows that we need an additional layer of protection. These backups will protect against a wrongful order to eliminate S3 buckets, by giving us a period of time (15 days) to undo it.

The S3 backups will be initially for all buckets, in the Platform stamp, in all regions, for Ring +3/GA. Depending on the success of this rollout, expansion to other rings (namely +2/EA and +1/Community) will be assessed.

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

S3 buckets in Platform stamp

**Impact Description**

Activating these backups will incur costs for backing up storage, which is, on average, 5TB per tenant. Costs as of today are estimated at &asymp; 10,000USD/month, with a potential growth to &asymp; 20,000USD in one year.
## 3. Pre-requisites### Inputs for execution
- 
OK from AWS that their infrastructure will cope with the volume of the initial S3 backup ✅

- 
Deployment of the stacksets that create the vault for the S3 backups in each account, and the IAM roles - IAM ticket #3176870. These will be used by the centralized AWS policy running in account 387229418815, and have been tested as indicated in the IAM ticket;

### Technical requirements
- 
*Administrator* access to AWS account 387229418815 (master account for AWS Backup for ODC) - granted to SRE Alpha team

- 
Read-only access to Ring3 AWS accounts via PIM (required to confirm backup status)

### Communication
- 
ODC leadership to be informed once the backups are started, and once they are in sync (meaning: we are covered) [Ac&aacute;cio + Tiago Garcia]

- 

### Expected duration
The actual implementation will take 2 hours. Then it will require daily validation of the state of the backups until all buckets are in state XXX.

## 4. Implementation Plan### Implementation actions- 
Access AWS console and perform SSO to account 387229418815

- 
Access the AWS backup service, and navigate to My Organization =&gt; Backup policies

- 
Identify policy with name **ODC_S3_Backup** and ID **p-897ouvltim**, and open it;

- 
Click &ldquo;Attach&rdquo; in the Targets section

- 
Select the OU ODC_Prod_Customer =&gt; Ring 3 =&gt; Platform_Stamp

### Testing and validation plan- 
In the AWS console, login as account 216903563336 (ring +3, Platform Stamp, us-east-1/Virginia)

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
Remove from target **ODC_Prod_Customer =&gt; Ring 3 =&gt; Platform_Stamp**

## 5. Post Implementation 
Every day, status of backups needs to be checked in the console, until all buckets show up in state. Bigger accounts are us-east-1 and eu-central-1, but checks should be made to all accounts.
## 6. Other
- 
n/a