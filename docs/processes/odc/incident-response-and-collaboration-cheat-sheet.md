---
title: Incident Response and Collaboration Cheat Sheet
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/3772022804/Incident+Response+and+Collaboration+Cheat+Sheet
confluence_space: RKB
confluence_page_id: 3772022804
last_synced: 2026-04-09
owner: Process Engineering
---

# Incident Response and Collaboration Cheat Sheet

12falsedefaultlisttrue# Immediate Support## **Paging Teams**: How to page any R&amp;D team for immediate assistancehow_to_page_teams
**Valid scenarios**

- 
Paging a Development Team in the context of an incident

- 
You are not sure how to proceed but still require assistance from a Development Team or someone

[**To page SRE in the context of an Incident, proceed with this method.**](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/3772022804/Incident+Response+and+Collaboration+Cheat+Sheet#Paging-SRE%3A-How-to-page-SRE-for-immediate-assistance)

In Slack (any conversation), use the following command to trigger the page form: /rootly page

**Alert Urgency** must be set to **HIGH** to ensure the team is paged.

**Fill out the form:**

- 
**What&rsquo;s the Problem? **Brief description of why you are requesting assistance

- 
**Who do you want to notify? **Select a team or a person

- 
**Alert Urgency? **Select **High **to guarantee the person/team is paged

- 
**Description: **Include any additional instructions, like an incident link, slack channel, or a zoom link

Type or paste something here to turn it into an excerpt.

## **Paging SRE**: How to page SRE for immediate assistancehow_to_add_sre_jira
**Valid scenarios**

- 
Any Incident in the RDINC project (*i.e. Customer reported, SLOs, Manually created*)

- 
Emergency RFCs

- 
Starting **October 9, 2025**, the SRE team will be paged **only for Emergency RFCs**.

### Rootly Paging
This option immediately pages the SRE on-call.

- 
Slack Command: 

- 
Alert Urgency: **High**

- 
Who do you want to Notify? **SRE**

### Jira Incident (Sev1 or Sev2)
- 
In an open Jira Incident (RDINC), add `SRE Global` to the Teams - This will immediately page SRE and will automatically create a slack channel for the incident

- 
In case the team is already added and if you require further assistance from SRE, page the SRE on-call using the Slack command above.

## **On-Call Engineers**: Check who is on-call for specific teamswho_is_on_call
Type or paste something here to turn it into an excerpt.In Slack (any conversation), use the following command to trigger the page form: 
# Incident Response## Manual Incidents: How to create a manual incident
Use the following form to create an Incident on the ODC R&amp;D Incidents Jira project.

- 
The initial Status of the incident is Backlog   

The incident must be handled as a regular incident, abiding by the same rules described in the section

 What does an ODC Incident look like in Jira? 
[https://outsystemsrd.atlassian.net/jira/software/c/projects/RDINC/forms/form/direct/259426148991099/10600](https://outsystemsrd.atlassian.net/jira/software/c/projects/RDINC/forms/form/direct/259426148991099/10600)# Other Requests## 
Reliability system / tool (e.g. Rootly, Nobl9)
All requests for help with a reliability system shall be made through [**this portal**](https://outsystemsrd.atlassian.net/servicedesk/customer/portal/31)[.](https://outsystems.slack.com/archives/C03GUL6N2TH/p1741775938259919)

## Other inquiries
Requests that fall out of the above categories should be submitted through the [**#rd-sre-odc-public**](https://outsystems.slack.com/archives/C071A8MKD6X) slack channel.