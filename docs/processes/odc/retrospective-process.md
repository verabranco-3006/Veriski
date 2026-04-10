---
title: Retrospective Process
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4696212894/Retrospective+Process
confluence_space: RKB
confluence_page_id: 4696212894
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective Process

**Version Control - **Current Version - 4.0 / Release Date -    

Next Release Planned - To be defined

Please read the **Process Release Notes** page to check what will change. 

**Table of Contents**
12falsecirclelisttrue# What is a Retrospective?
A Retrospective is a **blame-free**, detailed description, of exactly what went wrong to cause an incident, along with a list of steps to take to prevent a similar incident from occurring again in the future.

During this whole lifecycle, it is important to assume from the very beginning that every team and employee acted with the **best intentions** based on the information they had at the time. Instead of identifying&mdash;and punishing&mdash;whoever screwed up, the blameless mindset focuses on **improving performance and product quality moving forward**.

It is hard, most of the time, but it is vital to promote a safe space for the Engineers to share all the relevant details that lead to the incident, without fear of repercussions.

# Scope and Applicability
Retrospectives of **incidents with system-wide impact **will be led by **the SRE Team, acting as RCA Commanders **- they will ensure that all the stakeholders are involved to discuss and analyze the incident and understand its root causes.

After the Retrospective is reviewed and approved in the formal readout, the SRE Team will hand it over to **Process Engineering** to follow up on action plan completion. 

As incidents have different impacts, we will need to be more formal for incidents with system-wide impact to be prepared to have RCA reports as customer deliverables. However, the main purpose will always be to **understand the cause** and **draw improvement opportunities** from the incident.

So if we are confident that we will benefit from executing Retrospectives for** incidents without system-wide impact**, we do recommend following the same flow as for the incidents with system-wide impact.

# Jira Workflow for Retrospectives
Retrospective reports will be managed inside the **Incident** Issue type of RDINC Jira Project in a specific tab of the issue called ***Retrospective.** *

As stated above, incidents have different impacts, we will need to be more formal for **incidents with system-wide impact **to be prepared to have RCA reports as customer deliverables. 

The process will follow the workflow represented below. All the transitions of the **Retrospective** workflow should be done manually by the team managing the Retrospective execution.

**Retrospective**

Retrospective In progressBlue  

Retrospective is **being worked** on by the teams.

Retrospective completedGreen  

All activities of Retrospective** are completed** and all the relevant information is identified.

**Root Cause is identified** and all the** improvement opportunities / bugs** have been noted down and linked to the RDINC.

The RDINC should stay in this status until all the **linked blocking **tasks are completed.

ClosedGreen  

**All the improvement actions **identified in the Retrospective and linked to the RDINC have been **delivered into Production.**

**Jira Field**

**Description**
#### RCA/Post Mortem URL
Link to the Retrospective document

For **incidents with system-wide impact**, the field will be automatically populated by Rootly.
#### Reviewer
The person who reviewed the Retrospective.
#### Approver
The person who approved the Retrospective.
#### Root Cause Categorization
Clustering of root causes. Possible values are:

- 
Infrastructure issues

- 
Application issues

- 
Deployment issues

- 
Security Issues

- 
Operational Issues

- 
Configuration issues

- 
Missing feature 

- 
Customer issue

- 
Tests failed

- 
Self Recovered

  **Quick-tip:** Check [here](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4696212894/Retrospective+Process#Categorize-the-Root-Cause) some tips to pick the most accurate root cause.

# Retrospective documents and artifacts## Incidents with system-wide impact
Retrospectives will be led by the **SRE Team**, acting as[ ](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/edit-v2/4696211543#Roles-%26-Responsibilities)**Retrospective Commanders**. They will coordinate with Value Stream Leaders owning assets impacted by the incident.

Retrospective documents will be automatically generated and added to the Jira incident in the field **RCA/Post Mortem URL.**

The **targeted** timelines for the Incident Retrospective to be performed are the following:

- 
**2 business days** after Incident resolution - Executive Summary

- 
This document will be shared with the Senior Management Team, with the customers impacted, and on the OutSystems Status page (if applicable)

- 
**5 business days** after Incident Resolution - Internal Retrospective document completed

- 
**8 business** **days **after Incident Resolution - Internal Retrospective formally reviewed and approved

- 
**10** **Business days** after Incident Resolution - Customer-facing Retrospective ready (if requested)

## Incidents without system-wide impact
Development Teams can decide to proceed with Retrospectives for incidents without system-wide impact by automatically generating a Retrospective document and filling in **Generate RCA document from Rootly** with YES. 

The Retrospective link must be added to the **RCA/Post Mortem URL** field on the Jira Incident. 

This will only be possible if the incident is on SOLVEDGreen status.

:raised_back_of_hand:1f91a🤚#FFFAE6
**MANUAL TASK on Jira incident**     

When the incident is mitigated, the Jira issue should be moved from SOLVEDGreen to Retrospective IN PROGRESSBlue to initiate the Retrospective Stage, **manually**.

## Templates
For **other incidents or events** without a retrospective document created by design, the following template must be used.

Retrospective Template - [https://docs.google.com/document/d/13rXmBsOJh73nV2D6Z17SIBGBu2HOTWty5ddsvU000JM/edit?tab=t.0#heading=h.98ecttweohwt](https://docs.google.com/document/d/13rXmBsOJh73nV2D6Z17SIBGBu2HOTWty5ddsvU000JM/edit?tab=t.0#heading=h.98ecttweohwt)  

Please make a copy of the template with the following standard title and marked as **Internal** Document.

After review and approval, the Retrospective document will be moved to the centralized repository,   the status of the document will change to **Approved** and the document will be locked for future editions.

 

# Retrospective stages and tasks
When analyzing an incident and performing a Retrospective, keep in mind Process, People, and Tooling dimensions as well as the **DORA metrics** - it will guide the team in identifying root causes and improvement opportunities.
## Investigation
Once the service is recovered and services are back to normal conditions, we need to understand what were the causes that led to this incident and how can we prevent it from happening again.

To do this, we should investigate the incident and identify:

- 
Which services were affected by the incident

- 
Which alarms were triggered, if any, or could have led to the incident (e.g troubleshooting dashboards, customers reporting)

- 
How did the team detect the incident and how did they know something wrong was happening 

- 
How the customers were impacted (e.g journeys affected - deployments, runtime, authentication)

- 
How the affected services are impacting the intended customer experience

- 
The actions taken by the team to reestablish service

### **Complete the incident timeline**
With this information, your team should be able to build a** detailed timeline** of the incident which is a complete real-time record of the incident. 

It can include manual entries (chat), consolidated records of pages, alerts, and acknowledgments, and automatic system updates (for example, notification that someone has changed the severity level of an incident or marked it as resolved).

:clock1:1f550🕐#DEEBFF
**Incident Timelines and Why They Matter**

Incident timelines are a single view of what happened, when, and sometimes why&mdash;information that can save teams hours upon hours during the Retrospective review and can also contribute to a more robust root cause assessment, to prevent the incident from happening again. 

 **Timeline Example**

To guide you through the concepts of process on this playbook, consider the scenario a customer reported that an error occurred while deploying the application:&nbsp; Publish process stopped working.

After some investigation, the team realized that a disruption on a Dynamo table happened that impacted 1CP Process, for a particular customer. 

Below is a detailed timeline of the events:

**Date and hour**

**Event**

3-Oct-2022 - 14:20

Disruption: DynamoDB table was deleted, by a generic user

3-Oct-2022 -14:30

(#78688) Alarm was raised on Ring +1 &ldquo;Alert on Ring osall: CMS - Resource not found OSALL|EA|GA&rdquo; on Theseus&rsquo;s alert channel

3-Oct-2022 -14:41

Client Nikola Tesla created the ticket #2723693 in the Support Portal as Urgent (SEV-1)

3-Oct-2022 -14:48

The incident was assigned to Delivery Automation team

3-Oct-2022 -15:25

Alarm (#78694 on Pager duty)&nbsp; was raised on Ring +1 for Issues with Publish with error rate &gt; 30% (High priority)

Alarm (#78695 on Pager duty)&nbsp; was raised on Ring +1 for Issues with Publish with error rate &gt; 20% (Low priority)

3-Oct-2020 -15:34

Maestro team was notified on the slack channel #rd-maestro-team of the existence of incident RDINC-3522 on JIRA and corresponding PD incident #52781 by Marie Curie

3-Oct-2020 - 16:00

Galileo Galilei delegated the issue to Theseus after finding out the error came when calling Configuration Management Service owned by Theseus Team

3-Oct-2020 - 16:05

Galileo Galilei provides an update via PagerDuty reinforcing: &ldquo;Publish service is calling CMS which is not finding some configs. Theseus will handle it.&rdquo;

3-Oct-2020 - 16:40

Charles Darwin execute the DB Recovery using this Runbook.

3-Oct-2020 - 17:00

Charles Darwin from Theseus Team marked the Jira ticket as &ldquo;Solved&rdquo; and informed the customer Nikola Tesla.

*&ldquo;Hello Nikola Tesla,*

*We were able to identify the cause of your issue and we were able to recover.*

*As we believe this reply will resolve the presented issue, we will tentatively mark the present ticket as solved.*

*Nonetheless, should this issue persist, you will still be able to reopen the ticket just by replying to this message.*

*Kind regards,*

*The ODC Team&rdquo;*

After reading the incident timeline, it is possible to identify:

- 
Decisions made

- 
People involved and notified

- 
Alarms generated

- 
Steps taken to service recovery

- 
Tooling triggered

- 
Communications made with internal stakeholders and the customer

### **Write the Executive Summary**
A good Executive Summary should follow the *&ldquo;Communicate to be understood&rdquo;* rule and should answer the following questions:

- 
What was the actual problem?

- 
What was the real impact on OutSystems and Customers? 

- 
What were the Root causes of the incident?

- 
What actions will be taken to avoid reoccurrence? 

Example of a good Executive Summary

### **Identify the findings**
With the timeline complete, now it is time to identify the **Findings** of the incident - which are the results of the investigation performed on the process, the system, or the service during the incident lifecycle. 

Findings could be represented by situations where:

- 
The service did not react as expected

- 
The process was not properly executed or failed

- 
People did not coordinate as expected through incident recovery

- 
Tooling failed during the incident response

Using the same scenario presented on the timeline, we can identify some of the situations described above:

 **Findings Example**

**Findings**

**Finding 1 - **The incident was assigned initially to a team that did not own the affected service.

**Finding 2 - **Service Delivery Managers were not triggered to play the role of Incident Commanders to coordinate incident recovery.

**Finding 3 - **Generic users are capable of deleting Dynamo DB tables.

## Root Cause Analysis### **Perform Root Cause Analysis**
With all the relevant findings identified, your team is able to proceed to the most important step of the Retrospective - the** Root Cause Analysis (RCA)** - a technique practiced in Lean Management that allows you to achieve *Kaizen* (Continual Improvement in Japanese).

The most common method** **applied to perform Root Cause Analysis is **The 5-Whys - **this [method](https://kanbanize.com/lean-management/improvement/5-whys-analysis-tool) uses a series of questions to understand the layers of a problem. The idea is that each time why is asked, the answer given becomes the fundamental of the next why until the source of the problem is found.

For each of the findings identified, the 5-Whys analysis helps identify the ***root cause*** of the problem. Note that there are two levels of root causes:

- 
Technically, why did the misbehavior manifest;

- 
Non-technically, why did we get to the situation where the misbehavior occurred;

Both will be mixed while running the root cause analysis.

The idea of  5-Whys is to do the exercise in a **tree-fashion**. At the end of the exercise, **picking up the leaves** will give better insights into what caused the issue and needs to be changed - at a technical and non-technical level.

The questions to be asked, whenever looking at a node in a tree, are variations of:

- 
***why did this happen? ***(leading to a well-understood problem - depth)

- 
***why is this a problem? ***(opening-up for ramifications of the problem - width)

Root cause of a problem is usually **the last *****why** *resulting from the 5-Whys exercise.

Some best practices you can follow:

- 
Mark the **Dead-Ends**: branches of the root cause tree that are not actionable  

- 
Mark **STOP Conditions**: they happen when the only answer to **why** is &ldquo;because that was the decision&rdquo;.  Typically the actual root cause is one or two levels up.

- 
Bear in mind that multiple branches may lead to the **same conclusion**. 

####  Root Cause Analysis Example
Let&rsquo;s go back to our example to understand how the findings identified and the 5-Whys method will help us identify the root causes and promote continual improvement of our services and processes.

**What did we find?**

**Finding 1 - **The incident was assigned initially to a team that did not own the affected service.

**Why 1**

Global Support Agent categorizes the incident according to the product area with the highest impact (&ldquo;deployments to production&rdquo;)&nbsp;

**Why 2**

According to Global Support initial diagnosis, the incident was happening in Service Studio (not able to publish the app) and in Portal (not able to deploy to production)

**Why 3**

Global Support Agent was not enabled to categorize the incident according to the error code.

**ROOT CAUSE OF THE FINDING 1**

The Global Support Agent does not know how to use information from the error code to categorize the incident to the right Product Area.

In **Finding 1**, the root cause is related to process enablement - the teams involved are not properly trained to execute the process as it is defined. 

**What did we find?**

**Finding 3 - **Generic users are capable of deleting Dynamo DB tables.

**Why 1**

Dynamo DB does not validate the users accessing the information.

**Why 2**

There is a bug on our product that allows access to table deletion. 

** ROOT CAUSE OF THE FINDING 3**

There is a bug on the product that needs to be correct to block the access to generic users to table properties.

In **Finding 3**, the root cause is related to a bug found on the product that allowed a table to be deleted for a generic user.

### **Categorize the Root Cause**
After completing the root cause analysis, you will be asked to select the major cause on the field** *****Root Cause Categorization***. 

Find below some tips on how to identify what could be the main root cause of the incident you are analyzing. The most common causes of a product like ODC could be:

**Infrastructure Issues**

**Application Issues**

**Deployment Issues**

- 
**AWS Service Outages:** Disruptions in core AWS services like EC2, RDS, S3, or Lambda.

- 
**Kubernetes Cluster Issues:** Problems with the Kubernetes control plane, worker nodes, or network configurations.

- 
**Network Connectivity:** Issues with network connectivity between components, VPC configuration errors, or firewall rules.

- 
**Resource Constraints:** Insufficient CPU, memory, or disk space, leading to performance degradation or failures.

- 
**Code Defects:** Bugs in the Runtime and Platform Service code, including logic errors, security vulnerabilities, or performance bottlenecks.

- 
**Configuration Errors:** Incorrect configuration of application settings, database connections, or external services.

- 
**Dependency Issues:** Problems with third-party libraries or services, such as outdated versions or compatibility issues.

- 
**Data Corruption:** Data integrity issues, such as accidental deletion, corruption, or inconsistencies.

- 
**Deployment Failures:** Errors during the deployment process, such as failed deployments or rollback issues.

- 
**Configuration Drift:** Changes to the configuration that deviate from the desired state.

- 
**Deployment Timing:** Issues related to deployment timing, such as overlapping deployments or conflicts.

**Security Issues**

**Operational Issues**

**Configuration Issues**

- 
**Security Breaches:** Unauthorized access to systems or data.

- 
**Vulnerability Exploits:** Exploitation of known vulnerabilities in the application or infrastructure.

- 
**DDoS Attacks:** Distributed denial-of-service attacks overwhelming the system.

- 
**Human Error:** Mistakes made by Outsystems operators or developers, such as misconfigurations or accidental deletions.

- 
**Monitoring Failures:** Ineffective monitoring or alerting, leading to late detection of issues.

- 
**Backup Failures:** Issues with backup and restore processes, leading to data loss.

- 
**Incorrect settings:** Mistakes in configuration files or dashboards

- 
**Missing configurations:** Overlooked or absent configurations.

- 
**Version mismatches** Incompatible versions of software or dependencies.

- 
**Security misconfigurations:** Weak or incorrect security settings

- 
**Deployment configuration errors:** Problems with deployment scripts or tools.

**Missing Feature**

**Customer Issue**

**Tests failed**

The incident was caused due some features not being included in the product

The incident was caused by problems on the customer side, not lying within the product.

To be used in Ring Promotion Incidents, due to a failure of a test.

## Action Plan Definition### **Define the action plan**
To ensure continuous improvement of our product and our processes. we need to properly record and track the improvement opportunities you'll find while executing Retrospectives - this way, we will act to prevent **the incident from reoccurring** and the **process from failing** again.

**Each finding** should have an action plan to address its root cause - the action plan should contain **action items**, and each item should have a **due date** and an **owner**.

The **action items** could be:

- 
 **Bugs &rarr;** each team can create the bugs that need to be corrected according to **Bug Escape guidelines**

- 
 **Tech Improvements &rarr;** Each team can create the tech improvement issues on their boards

- 
 **Improvement Actions &rarr;** Process-related findings that will be managed by Process Engineering Team.

Besides the aforementioned issue types, you can create other issue types to be linked to the incident and to address the root causes identified (e.g. stories, initiatives, etc). The **Linked Issues** Jira capability* *`&ldquo;is reviewed by&rdquo;` should be used for that.

 **Action Plan Example**

Let&rsquo;s now define the action plans for the findings of the example we have been using for Finding 1 and Finding 3.

**Finding 1 - **The incident was assigned initially to a team that did not own the affected service.

**ROOT CAUSE**

The Global Support Agent does not know how to use information from the error code to categorize the incident to the right Product Area.

**ACTION PLAN**

**Owner**

**Due Date**

**  [Improvement Action 1] **&nbsp;- Train Global Support Team on how to use Error Codes to diagnose and assignment of ticket to the right team.

Global Support

December

**  [Improvement Action 2] **&nbsp;- Create the process of updating error codes missing on the product

R&amp;D Process Team

Next PI

**Finding 3 - **Generic users are capable of delete Dynamo DB tables.

**ROOT CAUSE**

There is a bug on the product that needs to be correct to block the access to generic users to table properties.

**ACTION PLAN**

**Owner**

**Due Date**

**  [Bug 1] **&nbsp;- Unlock the access to generic users to table properties.

R&amp;D ODC Team 

Next PI

**  [Story 1] - **Create a backup plan for Dynamo DB

R&amp;D ODC Team 

Next PI

## Review &amp; Approval### **Manage Retrospective Readout**
Once the Retrospective document draft is completed, a formal readout will be booked by the Retrospective Follow-Up Lead, executed by the Process Engineering Team ( )- to ensure the document is reviewed, completed, and approved by the Retrospective Approver. 

ODC Value Stream leaders and Engineering Experts - the Retrospective Board - will be all invited to the Readout.

 Readouts will have an expected duration of **45 minutes**. We recommend the following: 

- 
15 minutes to present the outcomes of the Retrospective &rarr; Retrospective Commander and Team

- 
15 to 20 minutes to address questions &rarr; Retrospective Board

- 
10 minutes to set final considerations on the Retrospective and next steps

### **Review the Retrospective Document**
During the Readout, the Retrospective Commander must present the Retrospective document, starting by providing a small context, based on the Executive Summary, followed by the findings and their root causes. There is no need to go through the entire timeline unless any relevant event is worth mentioning. 

The Retrospective Follow-Up Lead must ensure that a formal Reviewer and Approver are assigned before the beginning of the Readout and the session must be recorded and added to the Incident ticket, as a comment. 

### **Implement Feedback**
During the presentation, the Retrospective Board will ask questions and provide feedback - any feedback must be implemented before the formal review and approval.

### **Accept the review**
Once all feedback has been implemented, the Retrospective Commander must engage with the designated Retrospective Reviewer to complete the final review. To formalize acceptance of the Retrospective, the Reviewer should set the ***Reviewed?*** field in the Jira Incident&rsquo;s *Retrospectives* tab to** &lsquo;Yes&rsquo;**.
note514081ca-eb1f-42ea-acaa-7015fd950b62
**The Reviewer should mark all comments in the document as resolved** before marking it as ***Reviewed ***(if they are satisfied with the responses), except in specific cases where they want the Approver to make a final decision. In those cases, **for each open comment, the Reviewer should clearly explain why it is not being closed** and what action or response they expect from the Approver before sending the document for approval.

When the document is ready for approval, **the Approver** should review all unresolved comments and either **mark them as resolved** if the responses are acceptable or request additional clarification or context. The document should be approved only once all pending points have been addressed or consciously accepted, and all comments are marked as resolved.

**The Reviewer should mark all comments in the document as resolved** before marking it as ***Reviewed ***(if they are satisfied with the responses), except in specific cases where they want the Approver to make a final decision. In those cases, **for each open comment, the Reviewer should clearly explain why it is not being closed** and what action or response they expect from the Approver before sending the document for approval.

When the document is ready for approval, **the Approver** should review all unresolved comments and either **mark them as resolved** if the responses are acceptable or request additional clarification or context. The document should be approved only once all pending points have been addressed or consciously accepted, and all comments are marked as resolved.

The role of Retrospective Reviewer must be played by highly experienced senior R&amp;D Subject Matter Experts in topics such as Quality, Reliability, Security, Architecture, Costs, and Operations. 

Find below the last approved list of Retrospective Reviewers.

**Reviewers**

 

 

 

 

 

  

 

 

 

 

 

### **Approve the Retrospective Document**
Once the review is accepted, the Retrospective Approver must set the ***Approved?*** field in the Jira Incident&rsquo;s Retrospectives tab to **&lsquo;Yes&rsquo;**.
note04f590e1-d9e4-4018-9d14-81edf7a95a11
When the document is ready for approval, **the Approver** should review all unresolved comments and either **mark them as resolved** if the responses are acceptable or request additional clarification or context. 

The document should be approved only once all pending points have been addressed or consciously accepted, and all comments are marked as resolved.

When the document is ready for approval, **the Approver** should review all unresolved comments and either **mark them as resolved** if the responses are acceptable or request additional clarification or context. 

The document should be approved only once all pending points have been addressed or consciously accepted, and all comments are marked as resolved.

The role of Retrospective Approver must be taken by the Value Stream Leader or Engineering Manager for the asset most impacted by the Incident. Please find below the list of potential Retrospective Approvers.

**Value Streams / Enablement Streams (detailed ****here****)**

***Release Engineering***

 

*Fallback - * 

***Cloud Platform***

*Fallback - *  

***AI***

 

*Fallback - *  

***Insights and Analytics***

 

*Fallback - *  

***Morpheus***

  

*Fallback - *  

***Low-Code AI***

 

*Fallback - * 

***Self-hosted (PaaS)***

 

*Fallback - * 

***Data &amp; Integrations***

 

*Fallback - * 

***App Dev***

 

*Fallback -  * 

 ***Identity***

 

*Fallback -  * 

***ALM***

 

*Fallback - * 

***Mobile***

 

*Fallback - * 

***Migrations***

 

*Fallback - * 

***Security Area***
 

*Fallback - *

***SRE***

 

*Fallback -*  

***Monitor &amp; Observability***

 

*Fallback -*  

***Tenant Lifecycle***

 

*Fallback -*  

***Evaluation &amp; Community***

 

*Fallback - *

:raised_back_of_hand:1f91a🤚#FFFAE6
**MANUAL TASK on Jira incident** 

Once the Retrospective is **approved**, then the Incident should be moved from retrospective IN PROGRESSBlue to retrospective COmpletedGreen. This action will be performed by the Process Engineering Team ( )

## Follow-up### **Monitor Retrospective Action Items &amp; track Recovery Measures**
To keep track of Jira incidents and their corresponding **action items**, each action item created (a bug, an improvement action) should be linked to the RDINC Jira issue using the **Linked Issues** Jira capability* *`&ldquo;is reviewed by&rdquo;`.

**Action items Due Date**

It is mandatory to set a due date for the action item. Please find on your Jira issue the field **Due Date** and fill it in with the date agreed on the retrospective readout.

After the Retrospective is reviewed and approved in the formal readout, the Retrospective Commander will hand it over to **Process Engineering** (  ) to follow up on action plan completion. 

The team will track action items completion, by performing regular checks on each incident and their action items progress. If needed, the team will engage directly with assignees to understand and align on any change in priority.
:raised_hand:270b✋#FFFAE6
**MANUAL TASK on Jira incident**     

Once all the **actions items are completed**, the incident should be moved from retrospective COmpletedGreen to ClosedGreen, **manually**.

Below find how an incident will look like once the **Retrospective is complete** and all the action items are linked to the incident, using the **Linked Issues** Jira capability* *`&ldquo;is reviewed by&rdquo;`. 

**Recovery Measures** such as bugs, requests for changes, or any tasks performed **during** the Incident Recovery stage must also be linked to the RDINC Jira issue using the **Linked Issues** Jira capability* *`&ldquo;is blocked by&rdquo;`, as shown below. 

### **Elaborate the Customer-Facing Retrospective**
Occasionally, a customer may request a formal Retrospective or Root Cause Analysis (RCA) to understand the origin of an incident. These requests are typically initiated through Global Support, with **L3 being accountable for drafting the response**. Depending on the specific requirements, this can take the form of a formal RCA document or a simplified summary of findings.

If additional technical context is required, L3 may collaborate with R&amp;D teams via the corresponding RDINC issue. Before the final information is shared with the customer, Global Support must submit the draft to the Legal team for review and approval.