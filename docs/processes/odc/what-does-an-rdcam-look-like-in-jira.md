---
title: What does an RDCAM look like in Jira?
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/5423202728/What+does+an+RDCAM+look+like+in+Jira
confluence_space: RKB
confluence_page_id: 5423202728
last_synced: 2026-04-09
owner: Process Engineering
---

# What does an RDCAM look like in Jira?

13falsenonelisttrue## Jira Workflow for Anomalies
Anomalies will be managed inside the [RDCAM - R&amp;D Cost Anomaly Management](https://outsystemsrd.atlassian.net/browse/RDCAM) Jira Project, using the ***Anomaly ***issue type.

 A new Anomaly can be created manually, inside this project, or automatically, through a Zapier automation.

After creation, all anomalies follow the same Jira workflow:
#### Threshold defined for Anomaly creation
Only anomalies that meet these filter criteria should be created in the Jira project:

totalImpact &gt; $100
OR
totalImpactPercentage &gt; 20%
OR
Duration &gt; 2 days

**Handling Recurring Anomalies: Updating Existing Jira Issues**

If an email is received regarding an anomaly that has already been identified and for which a Jira issue was previously created (i.e., with an Anomaly ID that is already known), a new Jira issue will not be created for that same anomaly. The existing Jira issue will be (automatically) updated with the new values, and the new email will be attached to it. Previous emails related to that same anomaly will also remain attached to that Jira issue for historical purposes.

**Jira Status**

**Description**

New

The process begins with the creation of a Jira issue (Anomaly), which can be:

- 
Manual: Anomalies are logged manually when identified through data analysis.

- 
Automated Creation: Anomalies are automatically created when a new email from Amazon AWS is received.

*Note: Not all anomalies are logged in the Jira project. They must meet predefined **thresholds **to be created.*

under investigationBlue

The Anomaly is being investigated by the Assignee, that belongs to FinOps Team.

- 
Transition From: &quot;New&quot;, once a team member begins working on the issue.

pending externalBlue

The Anomaly is being investigated by other teams (e.g., development, operations teams).

The issue is temporarily on hold for FinOps team.

- 
Transition From: &quot;Under Investigation&quot;, when the issue is escalated to other teams.

in resolutionBlue

The external team is actively working on resolving the Anomaly.

- 
Transition From: &quot;Pending External&quot;, when the external team starts actively resolving the issue.

in reviewBlue

At this stage, FinOps team reviews the external team's Anomaly analysis and/or resolution before closing the issue.

- 
Transition From:

- 
&ldquo;In Resolution&rdquo;, when the external team finishes their work.

- 
&ldquo;Pending External Teams&rdquo;, when the external team has no actions to perform.

closedGreen

The Anomaly has been investigated and successfully resolved, or it has been determined that no resolution is necessary.

- 
Transition From:

- 
&quot;Under Investigation&quot;, if the issue was automatically created, and it should be rejected.

- 
&quot;In Review,&quot; once the FinOps team has reviewed the analysis and resolution (when applicable).

## **Jira Issue Fields**
For each *Anomaly *issue, it's crucial to have the following fields populated:

**Field**

**Description**

**Observations**

**Summary ***

A concise title that represents the Anomaly.

Anomalies created by *Zapier*, follow the following template:
`AWS Cost Anomaly detected in &lt;Service Impacted&gt; on &lt;Anomaly Start Date&gt;`

Always mandatory

**Description ***

A brief explanation that clearly represents the Anomaly.

Anomalies created by *Zapier *copy the entire email body into the Jira Description, transforming it into a user-friendly format.

Always mandatory

**Reporter ***

Person responsible for creating the issue.

Always mandatory

**Assignee**

Person that is currently responsible for the issue.

It can be empty when the issue is created (*New *status). Mandatory when moving to any other status.

**Teams ***

The team(s) currently responsible for the issue.

Always mandatory. 

Defaults to the &ldquo;FinOps Team&rdquo; when the issue is created.

**OS Product**

The product(s) affected by the Anomaly, if applicable.
Options: ODC, O11, O11 + ODC

**Service Impacted ***

The Service impacted by the anomaly.

Always mandatory

**Account(s) Impacted**

The Account(s) impacted by the anomaly.

To be filled based on root cause analysis.

Text field.

Use ',' to separate multiple values.

**Start Date**

The date the anomaly was detected.

Date field

**End Date**

The date the anomaly was last detected.

Date field

**Anomaly ID**

The unique Anomaly ID.

Text Field

**Anomaly Duration (days)**

Duration of the anomaly.

For anomalies created by *Zapier*, this value is calculated based on the Start and End dates.

Numeric Field

**Daily Cost Impact ($) ***

Daily cost of the anomaly.

Always mandatory.

Numeric Field.

**Total Cost Impact ($) ***

Daily cost of the anomaly.

Always mandatory.

Numeric Field.

**Priority ***

The priority of the Anomaly.

Options: Urgent, High, Normal, Low

By default, it is &ldquo;Normal&rdquo;.

Always mandatory

**Root Cause**

Indicates the root cause of the Anomaly.

Select list with the options:

- 
Increased usage due to customer

- 
Vendor pricing changes

- 
Bug

- 
Test

- 
Infrastructure changes

- 
New feature

Mandatory when moving the issue to *Closed, with Final Status = &lsquo;Resolved&rsquo; or 'Accepted'.*

**Findings**

Key Findings from the Investigation, from FinOps or external teams.

**Final Status**

Field to complement how the issue was closed.

- 
**Resolved **- External team did the work to resolve the cause of anomaly.

- 
**Accepted **- The anomaly was expected to happen due to root cause and accepted. 
It is usually applied when an issue transitions from *Pending External Team Investigation* to *In Review*.

- 
**Duplicated** - Duplicated anomaly.

- 
**False Positive **- Used for anomalies that are classified as temporary spikes and one offs after quick investigation by FinOps team. 
It is usually applied when an issue transitions from *Under Investigation* to *Closed*.

Mandatory when moving the issue to *Closed*.

**Justify Status Decision**

Text field to justify the decision to close the issue.

Mandatory if closed with &ldquo;Accepted&rdquo; or &ldquo;False Positive&rdquo;.

- 
**mandatory when creating the issue**

## **Assign an Anomaly to an external team**
After an initial analysis of the anomaly by the FinOps team (status under investigationBlue), if the anomaly also needs to be investigated and subsequently resolved by an external team, the ***Teams *****field** should be updated to also reflect the team that will be responsible for continuing the issue's analysis and resolution. The ***Assignee *****field** should also be updated to reflect the person from the external team who will be responsible for the issue. If the exact person isn't known at that moment, the Team Leader, for example, can be assigned and updated later.

At that moment, the Jira issue should be **moved by the FinOps team to status** pending externalBlue.

There may be cases where an **Anomaly needs to be resolved by multiple teams**. In such cases, the ***Teams***** **field can include more than one team, and also each team may create sub-tasks to manage their work on their own boards. The Anomaly can only move from in resolutionBlue to in reviewBlue once all assigned teams have completed their work.

## **See Anomalies issues in Teams boards**
The best way to do this is to **update the team's Jira Board filter**, to also collect the Anomalies assigned to that team.

To do this, go to *&quot;Configure Board&quot;* on the team board, and update the board filter in *&quot;Edit filter query&quot; *(you will need permissions to complete this action). You should add something like: ***project = RDCAM AND Teams in (&quot;&lt;Team_Name&gt;&quot;)***. You may also need to map the *&ldquo;Pending External&rdquo;* status to one of your board&rsquo;s columns.

The team has the option to **create a new board for Anomalies** within their Jira project.

## **My team received an Anomaly issue. What now?**
When an anomaly is assigned to your team, it should be in pending externalBlue status, and the ***Teams** ***field **should display your team's name. You should then **assign the issue to the person responsible for it** within your team.

If, after investigation, your team decides that no action is needed for the anomaly, move the Jira issue to in reviewBlue status and **reassign it to FinOps team**. Before doing so, document your main conclusions in the ***Findings *****field**. In this scenario, the ***Final Status***** field** should be set to `Accepted`, and the ***Justify Status Decision*** **field **must be filled in with the reason for that decision.

If the anomaly needs to be resolved, move it to in resolutionBlue status. In the ***Findings** ***field**, record the key conclusions from your analysis and resolution efforts. This should include details such as the reason for the cost deviation, the actions taken to resolve it, and any relation to ongoing initiatives. In that case, the ***Final Status***** field** should be set to `Resolved`.

Once the analysis and/or resolution is complete, fill in **field *****Root Cause***. Afterwards, **move the issue to status **in reviewBlue.

## **How to close an Anomaly issue?**
The **FinOps team** is responsible for moving an Anomaly issue to the closedGreen status, and there are two ways they can do so:
- 
**When it&rsquo;s in the **under investigationBlue **status** &ndash; the FinOps team may decide, after an initial assessment, that further analysis is unnecessary. This typically occurs when the anomaly was expected due to a known root cause or resulted from a temporary spike. In this case, the issue can be closed with the ***Final Status*** **field **set to `Accepted` or `False Positive`.
It may also happen that the anomaly is identified as a duplicate of an existing one. In that case, it should be closed with the ***Final Status*** **field **set to `Duplicated`. [See Cost Anomaly Management Process ]

- 
**When it&rsquo;s** **in the **in reviewBlue **status** &ndash; If, after reviewing the analysis or fix performed by the external team, the FinOps team determines the anomaly can be closed.
In this case, the issue can be closed with the ***Final Status*** **field **set to:

- 
`Resolved` &ndash; if an action was taken to fix the anomaly;

- 
`Accepted` &ndash; if the anomaly was expected to happen due to root cause and accepted.

Whenever an anomaly is closed as `Accepted` or `False Positive`, the ***Justify Status Decision*** **field **must be filled in with the reason for that decision.

## How to deal with duplicated Anomalies
If you notice that **an anomaly is a duplicate of an existing one**, there are a few actions to take to avoid duplicate work for the team:
- 
**Keep the oldest anomaly as is** and mark the newest one as a duplicate by selecting `Duplicated` in the ***Final Status*** field.

- 
**Clearly fill in the *****Justify Status Decision***** field**, mentioning the Jira ID of the original anomaly (e.g., *&ldquo;This is a duplicate of RDCAM-XXX&rdquo;).*

- 
**Link the original (oldest) anomaly** in the new anomaly:
- Click **&ldquo;Add related work&rdquo; **:

- Select **&ldquo;is duplicated by&rdquo;** and add the Jira ID of the original anomaly:
- 
**Close the newest anomaly.**