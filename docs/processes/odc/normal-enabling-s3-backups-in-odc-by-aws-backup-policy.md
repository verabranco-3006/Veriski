---
title: [Normal] Enabling S3 backups in ODC by AWS Backup policy
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/5150312127/Normal+Enabling+S3+backups+in+ODC+by+AWS+Backup+policy
confluence_space: RKB
confluence_page_id: 5150312127
last_synced: 2026-04-09
owner: Process Engineering
---

# [Normal] Enabling S3 backups in ODC by AWS Backup policy

To request Emergency/Normal Product Infrastructure Changes [ODC + other services] please follow the work instructions. 

[https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/3862331705/Change+Management+Process#Record-Request-for-Changes](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/3862331705/Change+Management+Process#Record-Request-for-Changes) 

This Change is part of the ODC Change Catalog .
## 1. Summary
In ODC, S3 backups are enabled via an AWS Backup policy. Following RFC-2910, a policy was created that backs up S3 buckets based on tag **os:engr:compositions:vault-backups = true**, for any account that is added to the policy. 
The predefined mechanism for adding accounts to the policy is via their branch in the OU (Organization Unit) tree. 

Using this catalog entry requires providing:

- 
A list of 1 or more OU to which the policy will be extended;

- 
A re-assessment of the risks, namely cost.

## 2. General Information
**Change Type**

Normal

**Change Risk**

**VARIABLE** [cost] *(specified in each RFC)* * *Risk Matrix Calculation 

**Downtime Involved **

No

**Rollback Available**

Yes

**Implementation Team**

SRE

**Component(s)/Asset(s)**

S3 buckets 

**Impact Description**

Activating these backups will incur **VARIABLE** costs for backing up storage. *(specified in each RFC)*
## 3. Pre-requisites### Inputs for execution
- 
Deployment of the stacksets that create the vault for the S3 backups and the IAM roles in each account. This needs to be requested to IAM, and the ticket number must be indicated in the RFC.

### Technical requirements
- 
*Administrator* access to AWS account 387229418815 (master account for AWS Backup for ODC)

- 
Read-only access to the AWS accounts being included in the backup policy (required to confirm backup status)

### Communication
- 
To be managed by the PM of the requesting area (determined via RFC requester)

### Expected duration
The actual implementation will take 2 hours. Then it will require daily validation of the state of the backups until all buckets are in state Completed.

## 4. Implementation Plan### Implementation actions- 
Access AWS console and perform SSO to account 387229418815

- 
Access the AWS backup service, and navigate to My Organization =&gt; Backup policies

- 
Identify policy with name **ODC_S3_Backup** and ID **p-897ouvltim**, and open it;

- 
**Take a screenshot of the pre-existing OU added to the policy and attach it to the RFC. This will be needed in case of rollback.**

- 
Click &ldquo;Attach&rdquo; in the Targets section

- 
Select the OU specified in the RFC

### Testing and validation plan- 
In the AWS console, log in an account specified in the RFC

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
Identify policy with name **ODC_S3_Backup** and ID **p-897ouvltim**, and open it;

- 
Remove the target OU specified in the RFC;

- 
Confirm the remaining OU are the ones in the screenshot taken in step 4 of the implementation process.

## 5. Post Implementation 
Backups can take some time to conclude, so status of backups needs to be checked in the console, until all buckets show their backup in state **Completed**.
## 6. Other
- 
n/a