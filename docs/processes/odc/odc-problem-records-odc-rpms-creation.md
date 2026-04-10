---
title: ODC Problem Records (ODC RPMs) creation
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/5036639619/ODC+Problem+Records+ODC+RPMs+creation
confluence_space: RKB
confluence_page_id: 5036639619
last_synced: 2026-04-09
owner: Process Engineering
---

# ODC Problem Records (ODC RPMs) creation

none## When and by whom can a Problem Record be created?###  Global Support
After an **incident or multiple incidents that did not require R&amp;D intervention **(i.e. were not handed over to R&amp;D), the Support team may understand that further analysis is necessary due to their impact. In this case, a Problem Record should be created, and [PACA for ODC](https://engineering.outsystems.net/paca/ProductAreasListTree.aspx) should be used to forward it to the corresponding R&amp;D team.

Also, when there is a **potential Security Vulnerability**, the Support Agent should create a Problem Record, via Zendesk, so the vulnerability can be analyzed by PSIRT (Product Security Incident Response Team). 

(See https://outsystemsrd.atlassian.net/wiki/spaces/EEO/pages/4527751450/How+to+deal+with+Security+Vulnerabilities#%F0%9F%91%89--Vulnerability-detected-by-Customer for more details.)

In this case, all the communication between Global Support and R&amp;D, in the ODC RPM, must be done using the &ldquo;Zendesk Support&rdquo; area for Comments in the Jira issue. This way, the Support Agent will be notified when a comment is added in the Problem Record.
###  R&amp;D Teams
Following an **escalated incident that required R&amp;D intervention**, the R&amp;D team member assigned to that incident, along with the Eng. Manager, is responsible for making the decision whether or not to create the Problem Record, to record the analysis performed.

**In case you decide to create the Problem Record for the Incident**, please make sure Global Support is notified about it through the Jira Incident so Global Support can create a link between the Zendesk Incident ticket and the ODC Problem.

Without the correct linking between the Zendesk Incident ticket and ODC RPM issues, we lose important measures such as what is the scale of a Problem and how many cases it gave origin to.

Also, when R&amp;D finds a **potential Security Vulnerability **during daily activities, the R&amp;D Team should create a new Problem Record, so the vulnerability can be analyzed by PSIRT.

(See https://outsystemsrd.atlassian.net/wiki/spaces/EEO/pages/4527751450/How+to+deal+with+Security+Vulnerabilities#%F0%9F%91%89--Vulnerability-detected-by-R%26D for more details.)
###  Security Team
When a **new Security Vulnerability **is identified, the Security Team should create a new Problem Record for traceability purposes. [PACA for ODC](https://engineering.outsystems.net/paca/ProductAreasListTree.aspx) should be used to find the team that owns the issue.

(See https://outsystemsrd.atlassian.net/wiki/spaces/EEO/pages/4527751450/How+to+deal+with+Security+Vulnerabilities#%F0%9F%91%89--Vulnerability-detected-by-Security-Team for more details.)
## How to create a Problem Record?
Create a new Jira issue in the [Project &lsquo;R&amp;D Problem Management (RPM)'](https://outsystemsrd.atlassian.net/jira/software/c/projects/RPM/boards/2251), and select the Issue Type &ldquo;ODC Problem&rdquo;. Fill in the following fields under the tab &ldquo;***Problem Information***&rdquo;:

- 
Select, in &ldquo;**Project**&rdquo;***** : &ldquo;R&amp;D Problem Management (RPM)&ldquo;** **and** **&ldquo;**Issue type**&rdquo;***** :** **&ldquo;ODC Problem&rdquo;;

- 
Select a &ldquo;**Team**&rdquo;*** **to be assigned to the Problem record (Check the owner team in [PACA for ODC](https://engineering.outsystems.net/PACA/)) - the issue will appear in the team's board, if it is [configured ](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/edit-v2/5036639619#Assigned-for-a-team)for that;

- 
Fill in the **&ldquo;Summary&rdquo;*** with a title that is meaningful to the problem;

- 
You can leave the &ldquo;**Assignee**&rdquo; field empty;

- 
Select the &ldquo;**Product Categorization - ODC**&rdquo;*****;

- 
Answer the question &ldquo;**Is it a Security Vulnerability?**&rdquo;*****;

- 
The &ldquo;**Urgency**&ldquo;***** and &ldquo;**Impact**&rdquo;***** fields should be filled according to this matrix and will be used to calculate the Problem Priority automatically;

- 
Finally, click on &ldquo;**Create**&rdquo;.

*****mandatory

**Notes: **

- 
&ldquo;**Description**&rdquo; field is automatically filled in **after** the creation of ORPM, based on the template [here](https://outsystemsrd.atlassian.net/wiki/spaces/EEO/pages/4519493762/Guidelines+for+ODC+Problem+Management+fields#%E2%80%9CDescription%E2%80%9D-field).

- 
There may be cases in which a Problem is assigned to a Team and the **development tasks are shared with multiple teams**. Regardless, the Problem Record is always the responsibility of the team assigned to the ticket and this team must ensure that it is closed as soon as possible.

## Where can I see the created ODC Problem Records?### Assigned for a team
The best way to do this is to update the **team's Jira Board filter**, to also collect the Problems Records assigned to that team.

To do this, go to *&quot;Configure Board&quot;*, on the team board, and update the board filter in *&quot;Edit filter query&quot; *(you will need permissions to complete this action). You should add something like: ***project = RPM AND Teams in (&quot;&lt;Team_Name&gt;&quot;)***.

### All the ODC Problem Records
A [&quot;ODC Problems&quot; Board ](https://outsystemsrd.atlassian.net/jira/software/c/projects/RPM/boards/2251)was created, under RPM project, where you can check all the Problem Records opened for ODC.