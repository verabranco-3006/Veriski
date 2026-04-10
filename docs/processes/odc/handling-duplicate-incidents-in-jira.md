---
title: Handling Duplicate Incidents in Jira
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/5662933168/Handling+Duplicate+Incidents+in+Jira
confluence_space: RKB
confluence_page_id: 5662933168
last_synced: 2026-04-09
owner: Process Engineering
---

# Handling Duplicate Incidents in Jira

**Version Control - **Current Version - 9.0 /  Release Date - 

When an **incident is identified as a duplicate of an existing one**, a few steps must be followed to ensure the team avoids duplicating work and to prevent counting the same incident multiple times in our metrics:
- 
**Link the newest incident to the original (oldest) incident**

- 
Open the newest incident.

- 
Click **&ldquo;Link work item&rdquo;**.

- 
Choose **&ldquo;is duplicated by&rdquo;** as the link type.

- 
Enter the Jira ID of the original (oldest) incident.

- 
**Keep the original (oldest) incident unchanged**

No updates are required in the original ticket. All work should continue on that primary incident.

- 
**Close the newest incident as a duplicate**

- 
Transition the duplicate issue to `Cancelled`.

- 
In the ***Cancellation Reason*** field, select **&ldquo;Duplicated&rdquo;**.
More information can be provided in the *Comment* section: