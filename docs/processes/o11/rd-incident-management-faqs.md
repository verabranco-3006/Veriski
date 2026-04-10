---
title: R&D Incident Management FAQs
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/2710568988/R+D+Incident+Management+FAQs
confluence_space: RCP
confluence_page_id: 2710568988
last_synced: 2026-04-09
owner: Process Engineering
---

# R&D Incident Management FAQs

The goal of this page is to address common questions and concerns you may have regarding the R&amp;D Incident Management process.

This page should not replace dedicated documentation pages on these topics.

If you think this page will benefit from extra information, please send your feedback directly to slack channel   [#**gs-rd-incident-management-feedback**](https://outsystems.slack.com/archives/G01NSTM816Z).
17
## **How can I choose the right team to assign the incident?**
To assign the incident to the correct team, you should use [**PACA**](https://engineering.outsystems.net/PACA/) as a source of truth to find the Owner Team of the Product Area classified on the Incident.

## **How priority of an Incident is defined?**
Global Support works with **Severity Levels** based on the impact of a given issue on the business of the customer.&nbsp; 

Severity levels of Support Tickets are chosen by the customers upon opening of the ticket and should reflect the business impact of the issue, according to the definition below.&nbsp;

The **Priority **of a Support Case is aligned with the Severity Level given by Global Support when the customer opens a support ticket. 

So, the priority is set only taking into consideration **the impact the incident has on the customer.**

Do not forget that **customers expect** the product to work even in **obscure** use cases.

**Severity Level**

**Description**

**Available for**

**Urgent**

Complete loss of service or a significant feature that is completely unavailable and no workaround exists. It does not include development issues or problems in staging environments.

Production Environments

**High**

Partial loss of service with severe impact on the business and no workaround exists.

All Environments

**Normal**

Minor loss of service. The result is an inconvenience, which may require a temporary workaround.

All Environments

**Low**

No loss of service. The result does not prevent the operation of the software.

All Environments

## **What happens when the priority of an Incident is changed?**
The priority of a Support Case is determined by Global Support and cannot be changed by any R&amp;D Member.

Although, there are a couple of situations when priority must be reviewed following a request from R&amp;D to Global Support, or vice-versa.&nbsp; Any changes in Support Case&rsquo;s priorities will affect OLAs.

  If the **priority is increased,** then the new OLA breach date will be calculated taking into account the **date** when the **priority effectively changed** by Global Support. 

   If the **priority is lowered**, then the new OLA breach date will be calculated taking into account the original handover date, as previously defined.

## **How to reset the OLAs?**
OLAs **will be reset on R&amp;D side** when R&amp;D provides an answer to Global Support using [Jira Zendesk Integration](https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/731840559/Communication+in+Support+Cases#How-to-communicate-with-Global-Support%3F), when the Incident is on the following statuses: 

- 
Backlog

- 
Assigned

- 
Work in Progress

- 
Waiting Internal

**OLAs don't break** when an Incident is on the following statuses:

- 
Waiting for Support

- 
Done

## **How to deal with duplicated Incidents on Jira?**

If, by any reason, a duplicated support case is created and linked to the Support ticket on Zendesk, the team can **ask Global Support to unlink the Jira issue** that is duplicated from the original support ticket.