---
title: Retrospective Review Checklist Heuristic
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/5231280528/Retrospective+Review+Checklist+Heuristic
confluence_space: RKB
confluence_page_id: 5231280528
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective Review Checklist Heuristic

Guideline for reviewers of Retrospectives to serve as a reminder for the things we want to check as part of our review and why. 
## Responsibilities of a reviewer 
Before the Retrospective - 

- 
Review the Retrospective document and note questions either on the document or prepare them to discuss in the session 

- 
The link to the document can be found in the Jira ticket on the Retrospective tab

- 
Review the corresponding incidents and slack channels to ensure you have as much context as possible before the session

### Guidelines for the reviewer role 
- 
Be prepared - make sure you are familiar with the process

- 
Consider how you frame critique and questions to be relevant and helpful 

- 
Keep in mind that besides looking for things to be improved, there can also be things that worked well that should be emphasised (this includes the way the retrospective itself was conducted)

- 
Review the checklist below to ensure that we maximise our learning and codification of knowledge from the incidents

**What?**

**Why is this important? **

Is the Executive summary easily understandable and does it reflect and **summarise** the key findings of the retrospective? 

The executive summary will be the most read part of the retrospective and as such, should contain the key details. 

Have we done a 5 Why&rsquo;s exercise? 

5 Why&rsquo;s helps prevent shallow analysis and optimises for a deep understanding of the root causes so that we can identify actions to solve the right problems.  

Check that all of the mentioned - 

- 
changes

- 
bugs

- 
tasks 

that are part of the timeline of the incident are related in Jira. Note info here on how to correlate Recovery measures and Action items.

This allows us to track and relate with data the root causes and remediations made as part of an incident.

Check that we have covered Detection and Recovery as part of the retrospective - were we able to detect early? And did we recover in the best and fastest way? 

We may have thought about prevention in the retrospective, but it is also important to understand that we can&rsquo;t prevent everything - detection and recovery are also areas we can often identify areas of improvement.  

The timeline of the incident should cover from when the problem was introduced until when it was resolved. 

Optimise for covering all the bases of prevention and detection and recovery.

Check that all the teams that have any asset that was affected are included on the page. 

There can be additional insights and learnings that can come from affected teams.

In JIRA, the Root cause categorization should correctly reflect the root cause uncovered during the retrospective process. If it hasn&rsquo;t been captured, please update the field based on the root cause category definitions before submitting for approval. 

This can field be used in data analysis to identify patterns of root cause categories.

Check that all questions noted on the document have been answered or the feedback incorporated. 

We want to be able to reference our confluence pages as input to understanding patterns so it is important that the document reflects and incorporates all of the thought and learning that comes from the retrospective. 

Check that the Jira is mentioned in the page title.

This will make the page easily searchable if anyone wants to quickly find a retro for a specific incident.

Check information about action items.

Retrospective Process 

- 
Due Date defined

- 
Clear DRI (either Team or Person ToGo - preferably a Jira Assignee)

- 
You can use the following filter in Jira, selecting Due Date as one of the columns.

`issue in linkedIssues(&quot;RDINC-XXXXX&quot;, &quot;is reviewed by&quot;)`

### Some generic questions 
- 
Did we add alerts?

- 
Did we create bugs?

- 
Did we create an SLO if it was a system wide incident? 

- 
Have we implemented ways of preventing any similar problems in code if possible?

- 
Do we have any specific processes that could be improved?

- 
Is there anything in the way we responded that could be improved?