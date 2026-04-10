---
title: [Normal] Expand scope of AWS Backup policy for S3 backups to all AWS accounts in Production rings
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/5416421396/Normal+Expand+scope+of+AWS+Backup+policy+for+S3+backups+to+all+AWS+accounts+in+Production+rings
confluence_space: RKB
confluence_page_id: 5416421396
last_synced: 2026-04-09
owner: Process Engineering
---

# [Normal] Expand scope of AWS Backup policy for S3 backups to all AWS accounts in Production rings

To request Emergency/Normal Product Infrastructure Changes [ODC + other services] please follow the work instructions. 

Change Management Process 

This Change is part of the ODC Change Catalog .
## 1. Summary
In prior change requests, an AWS Backup policy for S3 buckets has been rolled out in select AWS accounts. This was needed to ensure we had backups of pre-existing assets which were not being backed-up.

Due to new developments by Theseus, it has become clear that this scope if not sufficient. Also, development teams can use S3 compositions (an Atlas construct) to create S3 buckets in any ODC AWS account, and the expectation is that these will be backed-up if they carry the tag `os:engr:compositions:vault-backups = true` .

Theseus team had originally requested their buckets were backed up. 

But the recommendation is that all AWS accounts for all Production rings (+1/OSALL, +2/EA, +3/GA) be backed-up, with the current rules (presence of the `os:engr:compositions:vault-backups = true` tag).

The way this change is implemented is by changing the scope of the AWS Backup policy: from applying to the Platform and Forge OU within each ring, it will be changed to include all the OU for each Ring. 
Discussing with AWS, the recommendation was to attach the parent level of the OU, wait for changes to sync, and only then detach the child-level. 

No changes are expected for the existing assets.

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
Deployment of the stacksets that create the vault for the S3 backups in each account, and the IAM roles. These will be used by the centralized AWS policy running in account 387229418815, and have been tested as indicated in the IAM ticket;

### Technical requirements
- 
*Administrator* access to AWS account 387229418815 (master account for AWS Backup for ODC) - granted to SRE Alpha team

- 
Read-only access to Ring3 AWS accounts via PIM (required to confirm backup status)

### Communication
- 
No communication required for this change. An informational message that these backups exist will be shared as part of Atlas updates.

### Expected duration
The actual implementation will take 2 hours. Then it will require daily validation of the state of the backups until all buckets are backed up.

## 4. Implementation Plan### Implementation actions- 
Access AWS console and perform SSO to account 387229418815

- 
Access the AWS backup service, and navigate to My Organization =&gt; Backup policies

- 
Identify policy with name **ODC_S3_Backup** and ID **p-897ouvltim**, and open it;

- 
Click &ldquo;Attach&rdquo; in the Targets section

- 
Select the OU ODC_Prod_Customer =&gt; Ring 3

- 
Repeat steps 4-5, selecting the OU ODC_Prod_Customer =&gt; Ring 2

- 
Repeat steps 4-5, selecting the OU ODC_Prod_Customer =&gt; Ring 1

After the testing stage (days later), once all backups have synced correctly , removing the child attachments (at Platform/Forge level) will be required. A second RFC will be opened for that.

### Testing and validation plan- 
In the AWS console, login as account 216903563336 (ring +3, Platform Stamp, us-east-1/Virginia)

- 
Access the AWS Backup service

- 
Locate the Backup vault S3Backups

- 
Under Backup plans, locate the backup plan s3backupplan

- 
Confirm that the objects are backing up in the Runtime account of +3/Frankfurt (034592499062) and +3/Singapore (886047112887) regions (some might already be concluded)

### Rollback plan- 
Access AWS console and perform SSO to account 387229418815

- 
Access the AWS backup service, and navigate to My Organization =&gt; Backup policies

- 
Identify policy with name ODC_S3_Backup and ID p-897ouvltim, and open it;

- 
Remove the new targets **ODC_Prod_Customer =&gt; Ring 3, ODC_Prod_Customer =&gt; Ring 2 **and **ODC_Prod_Customer =&gt; Ring 1**

## 5. Post Implementation 
Every day, status of backups needs to be checked in the console, until all buckets show up in state concluded.

After the successful conclusion of this RFC, a new one should be opened to remove the outdated attachments at Platform stamp / forge stamp level.
## 6. Other
- 
n/a