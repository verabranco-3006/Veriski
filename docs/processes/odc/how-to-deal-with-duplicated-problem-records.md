---
title: How to deal with duplicated Problem Records?
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/5036639805/How+to+deal+with+duplicated+Problem+Records
confluence_space: RKB
confluence_page_id: 5036639805
last_synced: 2026-04-09
owner: Process Engineering
---

# How to deal with duplicated Problem Records?

In case the **R&amp;D finds a duplicated ODC Problem Record (ODC RPM)** **by another one already existent**, there are a few actions that need to be taken to avoid double work from the team.

Here are a few things to keep in mind **when a duplicated RPM is found**:
- 
Keep the **oldest problem record as is** and **mark the newest problem record** as duplicated: choose the JIRA issue **status &ldquo;Closed&rdquo;** and select the option **&ldquo;Duplicated&rdquo;** in the **Status Reason List **field.

- 
Clearly fill in the field **Justify Status Reason,** mentioning the Problem ID of the Problem Record from which this one is duplicated (e.g.: *This is a duplicate of RPM-XXX&rsquo;*)

- 
**Link** the original/oldest Problem Record as **duplicated by** in the closed RPM:

First, click &ldquo;Link issue&rdquo;:

Then select &ldquo;is duplicated by&rdquo; and add the Jira ID:

This will also allow our customers to have visibility on the Support Portal of both the duplicated and the original ODC RPM where the investigation will be conducted.