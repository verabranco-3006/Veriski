---
title: Support Cases in Jira
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/726204911/Support+Cases+in+Jira
confluence_space: RCP
confluence_page_id: 726204911
last_synced: 2026-04-09
owner: Process Engineering
---

# Support Cases in Jira

For&nbsp; R&amp;D Incident Management, R&amp;D uses a Jira issue type called **Support Case**, so every time we mention JIRA issue in this document we are only referring to those of Support Case type.

# **What does a Support Case look like in Jira?**
This is how a Support Case looks like in Jira. We have two main blocks on the issue.&nbsp;The one on the left hand side, with the **General **tab and the one on the right hand side, with** Details** tab.

**1**

**Project name**

It helps on identifying the team who is responsible by the Support Case

**2**

**Jira key**

Jira code used to identify issues - Support Cases - you can always use the key to report and data search purposes.

**3**

**Summary**

It will help you get quick context of the Support Case.

**4**

**Linked Issues**

You can attach other Jira issues (problems, bugs, etc) to ensure nobody loses traceability on what is being done to solve the Support Case.

**5**

**Support Case Status**

It indicates what is the stage of the Support Case at the moment - you can see more details about Support Case status [here](https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/726204911/Support+Cases+in+Jira#Support-Case-Status).

**6**

**Reporter**

The **Reporter** usually is a member from Global Support, since the process of Incident Management @ R&amp;D is initiated with the handover of the Support ticket from Global Support to R&amp;D.

**7**

**Assignee**

The **Assignee** is the R&amp;D Team member assigned to work on the Support Case. It is his responsibility to give valuable updates to Global Support about the progress of the case.

**8**

**OLA Status and OLA Info**

It indicates what is the status regarding OLA performance. It could have the following states:

OK - Warning - Broken

The **OLA Info** will vary according to the OLA Status and it will help you to understand what is the time limit defined for the OLA status at the moment.

You can find more information about OLA Status and Info [here](https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/726335741/Support+Case+Priorities+and+OLAs#OLA-information-in-Jira)

**9**

**Zendesk Product Classification New**

It is the Product Area with which the Support Cases were classified. This is where the **symptom manifested** and not the root-cause.

**10**

**OS Product**

OS Product which the incident refers to (Neo or OS11)

**11**

**Zendesk Activation Code**

Activation code of the customer reporting the incident

**12**

**Priority**

It is the priority given to the Support Case by Global Support.

This is automatically synchronized with the priority in the Zendesk ticket and R&amp;D cannot change it by itself.&nbsp;

## **Zendesk Support Jira Plugin**
If you open the tab **Zendesk Support** at the lower right side of the Support Case** **Details tab, you are able to see some important information related to the Incident handed-over to R&amp;D.
- 
**Ticket ID** - It is the ID created on Zendesk Side. It is useful to search on [Support Portal](https://extranetinternalapps-prd.outsystems.net/SP360_CustomerTicket_UI/), if needed.
- 
E.g., you can use the Ticket ID in the url as follows: [https://extranetinternalapps-prd.outsystems.net/SP360_CustomerTicket_UI/CustomerTicket_Detail?TicketITSMId=2517703](https://extranetinternalapps-prd.outsystems.net/SP360_CustomerTicket_UI/CustomerTicket_Detail?TicketITSMId=2517703)

- 
**Organization** - The customer that reported the Incident to Global Support

- 
**Assignee** - It is the Global Support agent assigned to the Support Ticket

- 
**Customer Segment - **The market segment associated to the customer who reported the case (Tier 1, Tier 2 or Tier 3)

- 
**Status - **The **status of the support ticket** from Global Support Side. It is not necessarily the same as the Jira Support Case.

Zendesk Support Jira Plugin is also the tool we used to communicate in a formal manner with Support, using **Add Comment to all linked tickets**.

### **How can I find more information about the Support Case?**
You can check for extra context and **what customer **is reporting as well as supporting files (i.e. logs, traces, omls, etc.) using **Zendesk Support tab. **

In the bottom of the Support Case, if you select on the Activity Tab, **Zendesk Support** tab** **you will see:

- 
Public communications, made between OutSystems and the Customer, tagged as Public Reply, in white background

- 
Internal communications, made between OutSystems teams, tagged as Internal NoteYellow, in yellow background

Global Support does both Public and Internal Communications and R&amp;D is only able to do Internal Communications. 

You will be able to find Support Cases attached files as well.

You can also check the [**Support Portal**](https://www.outsystems.com/spp_customerticket_ui/customertickets_list.aspx) and use the Support ticket number on the **Search** field. 

Be aware that sometimes, Support Portal does not contain details on files attached. Please double check this information using **Zendesk Support** tab.

**Support Cases live in the Support Incidents board in each team&rsquo;s project**

This is a **Kanban board** and has **three swim lanes** (Urgent, High and Everything Else) with the** six possible columns/states**.

The idea with the swim lanes is to **segregate the highest priority cases** (Urgent and High swim lanes) from the lower priority cases (Everything else swim lane that comprises Normal and Low priority cases).

There are **no sprints or any other check points** for Support Cases, the **issues disappear from this board** when they are in status **Done **with no activity for more that **2 days**.
# Support Case Status
**JIRA Support Case Status**

**Description**

BACKLOG 

New Support Case escalated by Support, not yet assigned to a R&amp;D team member.

assigned  

This status is valid in two distinct situations:
- 
Support Case reserved for a R&amp;D team member - whenever the case is new and a team member assigns the issue from the issues available in the backlog.&nbsp; 

- 
Support Case already worked by a R&amp;D team member - whenever an issue was in a pending state (Waiting for SupportBlue) or marked as resolved (DoneGreen) by the R&amp;D team and Support sends a notification.

Work In ProgressBlue  

Support Case is being worked by a R&amp;D team member.

Waiting for SupportBlue 

Support Case that is pending information from the Support team.

Waiting internalBlue  

Support Case that is pending information from internal teams or tasks: regressions, other R&amp;D teams, third party (Oracle, Microsoft), etc..

DoneGreen  

Support Case R&amp;D team believes is done.

For e.g., situations such as:

- 
Workaround/Quickfix sent

- 
Replied scenario is: not supported / by design / not a platform issue

Or whenever original Zendesk ticket is marked as Solved by Support team.

 **S*****tory Points Spent** *and* **R&amp;D Account** *fields are mandatory

 ***Support Improvements** *checkbox* *field is not mandatory but its filing is highly recommendable 

- 
Feature Request

- 
Non-Supported Component

- 
Documentation already addressed this

- 
Information provided by Support *to R&amp;D *was insufficient

- 
Support was not able to attend the customer due to insufficient documentation

- 
Support cannot troubleshoot due to insufficient tools

# Support Cases Status Workflow
- 
Support Case always start in **Backlog **state until a member of the R&amp;D team picks it up (changing to **Assigned **state).&nbsp;

- 
While a case is being worked by a R&amp;D team member, the issue must be in **Work In Progress **state. However, a team member should not have more than one issue in this state (the remaining assigned cases should either be in a pending state** Waiting Internal **/ **Waiting for Support** or **Assigned **waiting to be worked on again).

- 
Whenever a case needs more information from Support, its state should be in **Waiting for Support**. If there is a need to synchronize with another R&amp;D team, there is an external dependency (e.g. Oracle) or a fix needs to be validated in Regressions, the case should be in **Waiting Internal **status.

- 
When all the work from R&amp;D side is completed (workaround/quickfix provided or issue replied with no follow-up work), the case is marked as **Done**.

- 
If a support case is in a pending state **&nbsp;Waiting Internal **/ **Waiting for Support **or marked as** Done**, and Support sends a notification then the issue switches to **Assigned **state **automatically**.

- 
Finally, if an issue is moved to another team&rsquo;s project, then the issue switches to **Backlog **state and the assignee is set to **Unassigned**.

Learn more about Communication with Support here