---
title: Support Case Distribution Inside R&D
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/726171771/Support+Case+Distribution+Inside+R+D
confluence_space: RCP
confluence_page_id: 726171771
last_synced: 2026-04-09
owner: Process Engineering
---

# Support Case Distribution Inside R&D

A Support Case escalated to R&amp;D will be **handled by the team that owns the Product Area** that is apparently at fault.

We say **apparently** because we may **not be sure the root cause of the reported issue** before we work the Support Case. 

So the following can happen:
- 
Customer reports an error while doing a **lifetime** staging, no more information is available, so it will be handled by the **O11 Consoles **team.

- 
When investigating the issue the O11 Consoles team realizes the issue is actually a **compilation** issue so the case is reassigned to the **O11 Platform Backend **team.

- 
When analyzing the compilation issues, the O11 Platform Backend team realizes it is caused by a **corrupt OML** so the case is finally assigned to the **IDE** team.

This is an **extreme scenario** when not enough information is provided on the Support Case escalation to allow for the correct assignment of a R&amp;D team.** In most cases there should not be more than 1 team reassign**.

In the image we can see that:

- 
**Technical Support** works on **Zendesk**

- 
**R&amp;D** works on **Jira**

- 
There is an **integration** between the two tools

- 
**Escalations** **to R&amp;D** are done by **creating a Jira issue** in the project &ldquo;**R&amp;D Support Cases**&rdquo;

- 
The **first assignment to an R&amp;D team project** is done by **one of the developers** in Support Rotation** **in **R&amp;D**.

- 
**Reassignments between team projects** is done by the **developer **in Support Rotation on that **team**.

# Notification for Support Cases distribution
There is no need to be constantly checking the [**R&amp;D Support Cases**](https://outsystemsrd.atlassian.net/secure/RapidBoard.jspa?projectKey=RDSC&amp;rapidView=1006) project for Support Cases to be distributed.

No notifications outside **Business Hours** (9 AM - 6 PM, Lisbon time)

- 
For **each Support Case** that is created in the [**R&amp;D Support Cases**](https://outsystemsrd.atlassian.net/secure/RapidBoard.jspa?projectKey=RDSC&amp;rapidView=1006) project, **a message** **is sent** to the public slack channel [**#rd-support-cases-distribution**](https://outsystems.slack.com/archives/CR2GQUX1Q)

- 
If the Support Case is not assigned to any team within a **1-business-hour period**, a notification is sent to the public channel through** Automation for Jira**

- 
You should use the **#rd-support-cases-distribution** channel to **discuss to which team** the Support Case should be assigned to

- 
Developers use the   emoji to give visibility when a case is being analyzed for distribution 

- 
When a decision is reach and a case assigned, developers usually use the team&rsquo;s logo emoji (or the closest emoji they can find) to let others know the assigned team 

- 
If the Support Case remains team-unassigned after **1 day**, an email will be sent to the **Dev Managers**, notifying them about the situation. 

- 
The Dev Manager will receive an e-mail **everyday**, until the Support Case is team-assigned. 

# How to choose the right team?
- 
Check the **Product Area** defined by Support, but also read the **description**

- 
**Support Cases** are classified with the Product Area where the **symptom** manifested, **not with the root-cause** Product Area

- 
Support may not be able to classify with more than a 1st tier Product Area, **by reading the description you may be able to do better**

- 
**Don&rsquo;t over guess** it though, in the example above from the description we can understand that it is &ldquo;/Application Runtime/Logic Execution/Integrations/SAP&rdquo;, but it is not always possible

# Use PACA
You don&rsquo;t need to know all Product Areas and team associations by heart.

Use [**PACA**](https://engineering.outsystems.net/PACA/) to search for Product Areas and find their owner team.
# How to reassign Support Cases to another team&rsquo;s project?
In order to handover a support case to another team, in **Jira** you have to follow the following steps:

- 
https://drive.google.com/open?id=1--KWLTX68DM11YuNsdizxQq4LB7fdlpc 

- 
When changing project leave all field mappings empty.

- 
The assignee is removed and the status is set to &ldquo;Backlog&rdquo; automatically.

When moving a support case to another team&rsquo;s project, keep in mind that the OLA will not reset.

Continue reading about how to manage Support Rotations here.