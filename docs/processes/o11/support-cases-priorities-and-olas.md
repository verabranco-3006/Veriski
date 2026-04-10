---
title: Support Cases Priorities and OLAs
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/726335741/Support+Cases+Priorities+and+OLAs
confluence_space: RCP
confluence_page_id: 726335741
last_synced: 2026-04-09
owner: Process Engineering
---

# Support Cases Priorities and OLAs

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

*copied from public OutSystems page [here]( https://success.outsystems.com/Support/Enterprise_Customers/OutSystems_Support/02_Support_ticket_severity_levels).

## **Why do we need to comply with OLAs?**
OLAs (Operational Level of Agreement) represents the **commitment** we have to our customers. Even if, on a first approach, we own it to Global Support.

Global Support is the one that handles directly the customers who face a lack of service.

To not lose money, time, and our customers&rsquo; trust **we must comply with the commitments** established with them.

OLA Monitoring is the control stage of the Incident Management process and it is active throughout the Incident lifecycle. 

## **OLA Objectives**
OLA objectives are defined under two main pillars:

- 
Service Hours

- 
Communication

The table below resumes each team&rsquo;s coverage to deal with Incident Management.

**Service Hours**

The table below resumes each team&rsquo;s coverage to deal with Incident Management.

**Team**

**Coverage**

Global Support

24 x 7

R&amp;D&nbsp;

8 x 5 (EMEA)

**Communication**

Global Support is accountable to manage all communications with the customers reporting Incidents. 

R&amp;D is accountable to communicate with Global Support the results of their investigation on the incident handed over by Global Support within the timeframes stated in the table below:

**Priority Levels**

**Communication Frequency**

**Warning notification system**

**Urgent**

Every 4 business hours

2 business hours before breach

**High**

Every 8 business hours

4 business hours before breach

**Normal**

Every 24 business hours

8 business hours before breach

**Low**

Every 40 business hours

8 business hours before breach

These OLAs represent the **expected communication frequency** between R&amp;D and Global Support when the incident is being investigated by R&amp;D.&nbsp;

## **OLA information in Jira**
**Jira Zendesk Integration** is the tool used to ensure communication between both organizations and to set all the notification systems to R&amp;D, to ensure that there is no OLA breaching.&nbsp;

OLAs are measured when **there is an action item dependent on R&amp;D**, which means that the incident on the R&amp;D side should be on the following statuses of the workflow:

- 
Backlog

- 
Assigned

- 
Work in Progress

- 
Waiting for Internal

Otherwise, the OLA will not be calculated nor breached.&nbsp;

R&amp;D can monitor the OLA Information status on Jira, based on the ***OLA Status*** and ***OLA Info** *Jira fields.

- 
*OLA Status* provides information about the status of the OLA

- 
*OLA Status* is ***OK** *when the OLA is not breached&nbsp;

- 
*OLA Status* is ***Warning*** when the OLA has reached the warning notification timeframe

- 
*OLA Status* is*** Broken ***when the OLA is breached

- 
*OLA Info* provides information about the expected time until the OLA breaches.&nbsp;

To prevent the OLAs from breaching, a notification system is set to display warning messages on *OLA Status* and *OLA Info. *Also, a color-coding mechanism is implemented on Jira, based on the information of the* OLA Status* field.

**Priority Levels**

**Warning notification system**

**Urgent**

2 business hours before breach

**High**

4 business hours before breach

**Normal**

8 business hours before breach

**Low**

8 business hours before breach

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

Find [here](https://drive.google.com/file/d/1RHe4SmshTMi3rtkpTU4woFvZ6g7YYH3F/view) the **Incident Management OLAs**.

## **Dealing with OLAs stress-free ** 

Learn some tips for when working Support Cases here.