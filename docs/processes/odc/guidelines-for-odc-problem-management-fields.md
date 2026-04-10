---
title: Guidelines for ODC Problem Management fields
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/5036805345/Guidelines+for+ODC+Problem+Management+fields
confluence_space: RKB
confluence_page_id: 5036805345
last_synced: 2026-04-09
owner: Process Engineering
---

# Guidelines for ODC Problem Management fields

16falsenonelisttruenote6ddda9f2-65ae-4bbf-b33c-8b9d46419f0f
***Customer-facing*** fields will be visible to customers when the RPM is linked to a Zendesk ticket. In this case, customers can view this information through the Support Portal.

***Customer-facing*** fields will be visible to customers when the RPM is linked to a Zendesk ticket. In this case, customers can view this information through the Support Portal.

## - &ldquo;Description&rdquo; field
**The &lsquo;Description&rsquo; template should appear automatically after the RPM creation.**

**Template:**

****Symptoms****

*&lt;describe all the symptoms of the issue and relevant data, such as logging&gt;*

****How to reproduce****

*&lt;describe step-by-step what is needed to reproduce the issue and all needed assets&gt;*

****Findings****

*&lt;all functional and technical findings you've gathered&gt;*

****Impact****

*&lt;describe the impact it has for the customers business or development&gt;*

*&lt;describe the impact on OutSystems, by affecting higher tier customers or company image&gt;*

****Urgency Reason****

*&lt;justify the urgency assigned to the issue considering the potential for generating additional incidents&gt;*
## - &ldquo;Release Note&rdquo; field
Since the ODC RPM is an information agglomerator, for customer-facing purposes, its respective *Release Note* must be written and disclosed when all associated Jira tasks (bugs, stories, improvements &hellip;), if any, have been completed and marked as DoneGreen/ CLOSEDGreen. At this point, it is of utmost importance to guarantee that:

- 
The ODC RPM Jira issue is only **moved to **RELEASE PLANNEDGreen** Jira Status when all the development work is completed;**

- 
**Release Notes** are written in the respective field in Jira (*Resolution *section). Please see Guidelines to write Release Notes.

ODC RPMs are well-known IDs by the customer and represent what customers can track when looking for release updates.

We have **2 scenarios** when it comes to filling in Release Notes:

**Scenario 1)**

If the **RPM Jira ID is used in the commit message** of the pull request that fixes the issue, the &ldquo;**Fix Version&rdquo; will be automatically filled, RPM will be automatically closed** **and the Release Note** **will be published** when that fix reaches GA. That Release Note should be written in the RPM *Release Note* field.

This usually happens when no child issues are created in order to solve the Problem. 

**Scenario 2)**

If the **RPM Jira ID is not used in** **the commit message** of the pull request that fixes the issue, the **RPM will not be automatically closed** **and the Release Note will not be published. **

This usually happens when one or more development tasks are created in order to solve the Problem, and the developer uses the Jira ID of those tasks.

If this is the scenario, you have 2 options:

Option A)
**Use the RPM Jira ID in the last pull request needed to solve the issue**. This way, you make sure the RPM is closed and the Release Note is published when all the fixes reach GA.

Option B)
release note published manually
**If the RPM Jira ID was not used, as a stopgap solution, the assignee must ensure that the RPM is moved to *****Closed *****when all of its child issues are closed, and open a Support Ticket to the Release Engineering team so that the Release Note can be published.**
To create this ticket, you must write your request in the Slack channel [#rd-release-engineering-support](https://outsystems.slack.com/archives/C02FDRXNER0), referring the Problem Record that contains the Release Note to publish.

In both options, the ODC RPM - as a combination of several development tasks - should contain one Release Note that gathers all the information about how the problem was fixed as a whole and not just individually (issue by issue). You can hide the Release Notes from the child issues in case you don't see any value in duplicating it. 

 If for any reason you find that a **Release Note has been forgotten** and needs to be published, a Support Ticket must be opened to Release Engineering team, asking to manually publish the Release Note.