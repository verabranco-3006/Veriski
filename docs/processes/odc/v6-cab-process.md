---
title: V6 - CAB Process
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/EEO/pages/5828477154/V6+-+CAB+Process
confluence_space: EEO
confluence_page_id: 5828477154
last_synced: 2026-04-09
owner: Process Engineering
---

# V6 - CAB Process

**Version Control - **Current Version - 6.0 / Release Date -   

Next Release Planned - TBD

Please check the Vera Branco 

 Inês Matos 

**Change Reviewers**

- 
Responsible for reviewing and either agreeing with the proposed Change or provided their educated reasons for disagreeing with it.

- 
Responsible for advising the Change Approvers on the best course of action regarding their technical expertise, according to the defined vectors

- 
Provide feedback and recommendations for improvement

- 
Perform the preliminary review of all Root Cause analyses produced as a consequence of emergency changes together with the Change Requesters

:triangular_flag_on_post:1f6a9🚩#FFBDAD
**READ ME - Reviewers may oppose the approval of a change request. **

Opposition by a reviewer, on its own, does not prevent an approver from going forward with the Change. 

However, Change Reviewers may choose to hierarchically escalate the change by commenting in the RFC. In that situation, a higher-level discussion must be had, and the Change Requester needs to also trigger escalation within their organization.

[List of Change Reviewers](https://outsystemsrd.atlassian.net/wiki/spaces/EEO/pages/5828477154/V6+-+CAB+Process#Change-Reviewers-&amp;-Advisors) 

**Change Approvers **

- 
Approve requests for changes, previously reviewed that impact their services

[List of Change Approvers](https://outsystemsrd.atlassian.net/wiki/spaces/EEO/pages/5828477154/V6+-+CAB+Process#Change-Approvers) 

# High-Level Procedure
CAB Procedure is initiated as soon as a Request for Change is submitted by a Change Requester, through the creation of a Normal or Emergency Request for Change.
## Rules of Engagement for Offline CAB
Request for Changes will be displayed in the [#odc_cab_approvals](https://outsystems.slack.com/archives/C0617T4EV3R) slack channel when transitioned to Submitted to CAB status.

:warning:atlassian-warning#FFBDAD
**Time-Optimization Golden Rule**

Offline reviewing must be prioritized for all the changes - please use the [#odc_cab_approvals](https://outsystems.slack.com/archives/C0617T4EV3R) and the thread created for each Request for Change to discuss and ask for any missing details.

Final decisions and revelant discussion elements **must be formalized on Jira**.

The following engagement rules are applied to each RFC thread:

- 
Mark the RFC with  - the RFC is reviewed and ready for approval by the Change Approver

- 
Mark the RFC with  - the RFC is approved by a Change Approver

 
## Reviewing a Request for Change
Change Reviewers are responsible for reviewing and either agreeing with the proposed Change or providing their educated reasons for disagreeing with it.
### Reviewers initial assignment  
The initial assignment of Reviewers is done using a [**round-robin**](https://confluence.atlassian.com/automation070/smart-assign-jira-issues-load-balancing-round-robin-and-more-1014664568.html) mechanism in Jira. The assignment will trigger then a Slack notification on [#odc_cab_approvals](https://outsystems.slack.com/archives/C0617T4EV3R) tagging the reviewer selected by the automation.

It is the **assigned Change Reviewer&rsquo;s** responsibility to:

- 
Perform initial assessment of the RFC

- 
Reassign, by updating the &ldquo;Reviewer&rdquo; field in the RFC, if needed.

- 
Tag the newly assigned Reviewer on the Slack thread to keep everyone informed

This automation **does not consider segregation of duties** - Change Reviewers are still accountable to check if it is possible to review the change taking this principle into consideration.

Reviewers&rsquo; **reassignment will not trigger** a new slack notification of the RFC.

It is the accountability and responsibility of the **Change Requester** to ensure there is a review and approval of the submitted RFC.

After reviewing the Request for Change, Change Reviewers should follow the following mandatory steps on Normal Requests for Changes in Jira.

### Categorizing the Reason for a Change
***STEP 1 - ***On** the General Tab**, review the ***Change Category*** field to ensure it is correctly selected.

- 
Fast Track

- 
Rollback

- 
Promote to Standard

- 
Restart

- 
Retry

- 
Change Configuration

- 
Change Infrastructure

- 
Other Read-only Operation

- 
Other Write Operation

***STEP 2 - ***On the **CAB Review** tab, confirm the name as ***Change Reviewer*** - The person who reviewed the Request for Change.

  If the Change Reviewer decides the Request needs to be reviewed within the formal CAB Meeting, then the field ***Need further discussion in CAB Meeting?*** should be flagged, and the RFC will be added to the CAB Agenda.

*** STEP 3 - ***Move the Jira Normal Request for Change from Submitted to CAB to REVIEWED - READY FOR APPROVALBluestatus.
## Approving a Request for Change
Change Approvers are responsible for approving requests for changes, previously reviewed that impact their services.

To approve the Request for Change, Change Approvers should follow the following mandatory steps on Normal Requests for Changes in Jira, on the tab **CAB Review**:

***STEP 1 - ***Mark the name as ***Change Approver*** - The person who approved the Request for Change.

***STEP 2 - ***Move the Jira Normal Request for Change from REVIEWED - READY FOR APPROVALBlue to APPROVED BY CABGreen  status, to approve the change or from REVIEWED - READY FOR APPROVALBlue  to REJECTED BY CAB.  

 If the Change Approver decides to **reject** a Request for Change, a ***Reason to Reject*** must be provided, using the corresponding field on the Request for Change.

# CAB Constituency## Change Reviewers &amp; Advisors
Change Reviewers **are requested to perform a formal review** through Jira comments if the risk vector they own is classified as Medium, High, or Unknown risk.

**Reviewers**

**Advisors**

Hélder Marques

**Compliance &amp; Security **

 Diogo Paulo  

Rui Covelo 

Rui Eugénio 

Casey Greenstreet

Rodrigo Silva 

Acácio Porta Nova  

Fernando Alexandre 

  

Himanshu Pandey 

**Cost &amp; Market Fit**

Rui Garcia  

Tusiime Ndyajunwoha 

Srinivasa Reddy Kasu 

Pedro Charola Alves  

Ramamurti Subramanian 

**Architecture**

Ricardo Filipe Martins 

João Valentim 

Thiago Campos

Miguel João 

Mariana Cabeda 

Pedro Nunes  

Gavin Behr 

 Pedro Cardoso  

Arturo Riter 

Chris Carter  

## Change Approvers
Change Approvers can approve both Normal and Emergency Request for Changes. CAB Approvers can only delegate hierarchically the approval of Normal Requests for Changes.

The Value Stream Engineering Lead is the minimum hierarchical level to approve Emergency Changes. Engineering Leads can formally delegate to other Leaders within the Value Stream (UX, PM, Architecture, Team Leads).

A request should be formalized by posting a message on [#odc_cab_approval](https://outsystems.slack.com/archives/C0617T4EV3R) channel, tagging [Process Engineering](https://outsystemsrd.atlassian.net/people/team/b3750437-12b9-468f-bdc4-57ece5994dc5) (Vera Branco Inês Matos ) team. 

CAB_Constituency
**Value Stream**

**VS Leader**

**Fallback**

**Cloud Platform**

Renato Armani 

Tiago Oliveira 

**Migrations**

João Lopes Batista 

Filipe Rodrigues 

**PaaS**

Anand Yashwanth Kumar Santhanam 

 

PaaS Services/RDO - Laura Huysamen 

Self-hosted - Sérgio Almeida 

Tenant LifeCycle - Marco Alves 

João Rodrigues  

**Agentic Apps &amp; Data**

Sudharshan Krishnamurthy 

Hugo Gaspar Srinivasa Reddy Kasu Marco Coimbra Allan Zhang 

**AI**

João Ascensão 

Kapil Jaisinghani 

Pedro Resende

Ambarish Kumar 

**ALM**

Rui Santos 

Sara Gonçalves

**Identity**

Nuno Parreira 

Francisco Oliveira 

**Mobile**

Vitor Oliveira 

Luís Raposo Silva 

**Morpheus**

Miguel Rebelo 

Bruno Cunha e Silva 

**Release Engineering**

João Brandão 

João Figueira Gomes 

**SRE &amp; Monitoring &amp; Observability**

Pedro Charola Alves 

SRE - Tiago Garcia Nishit Dalal 

M&amp;O - Messias Peralta 

**Evaluation &amp; Community **

Ricardo Neto 

Type or paste something here to turn it into an excerpt.

# The CAB Meeting
The CAB Meeting will be held **once a month.**

note3882a3ec-b497-4f46-998b-6f74a0fdbfed
Besides the fixed CAB Constituency, CAB meetings should include at least **one representative from all groups being affected by the changes** on the agenda. 

Besides the fixed CAB Constituency, CAB meetings should include at least **one representative from all groups being affected by the changes** on the agenda. 

 

**Before the CAB meeting:**

- 
The Change Requester should have documented the change on the Change Catalog and attached it to the Request for Change (RFC) in Jira to be analyzed.

- 
CAB Owner should share the agenda by labeling each RFC to be analyzed using the *Labels* field in each RFC with the following standard `CAB-YYYY-MM-DD`

- 
CAB Owwer should summon the CAB, through the **DL_R&amp;D Change Management **([change.management@outsystems.com](mailto:change.management@outsystems.com)), and the representatives of areas impacted by the changes in the agenda

**During the CAB meeting:**

- 
The CAB Owner should lead the CAB group through each HighYellow  and URGENTRed  priority Request for Changes submitted for approval

- 
Change Reviewers and Change Approvers should review each RFC and raise potential risks on the Impact Assessment done initially by the Change Requesters (see **Impact Assessment** tab in the Jira Request for Change)

- 
Change Approvers should decide upon the implementation of each RFC, according to the risk assessment and the review made by the Change Reviewers. The decision should be logged on Jira using the status of Approved by CAbBlue or REJECTED by CAb  

- 
If REJECTED by CAb  &rarr; Reason for Rejection should be provided

**After the CAB meeting:**

- 
CAB Owner should share which changes were approved and rejected within the pre-determined mailing list, highlighting potential risks and downtimes expected, if any using the CAB Meeting Logs.

- 
Change Assignees should plan the changes accordingly

- 
Change Assignees should provide regular status on the RFC

- 
CAB Owner should share any improvements detected in the Change Management process to ensure continual improvement