---
title: Activate Jira notifications in Slack
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/6088294618/Activate+Jira+notifications+in+Slack
confluence_space: RKB
confluence_page_id: 6088294618
last_synced: 2026-04-09
owner: Process Engineering
---

# Activate Jira notifications in Slack

none### Prerequisites
- 
The **Team name** in Jira and in EOM must match

###  What?
**EOM **properties are being used to **standardize notifications for team Slack channels** whenever issues (incidents, failures, etc.) are assigned to teams.

Using the ***Jira &ndash; EOM integration***, the** Slack channel **where the notification is sent is defined in team&rsquo;s EOM page.

###  Why?
Using the channel ID (instead of channel name) means teams can rename channels without breaking Jira automations. Teams can also update their notification channel directly in EOM without needing to modify Jira rules.

###  How?
Here is a reminder of what you should do to ensure everything works properly:

- 
**STEP 1 - Add &quot;Communication Manager&quot; app** to the channel where you want to receive the notifications

- 
Slack channel* 'More actions'* menu &rarr; *Open channel details *&rarr; *Integrations *&rarr; *Add an App &rarr; *Search for and add *Communication Manager*

- 
**STEP 2 - **Go to **EOM**, open your team's page and add the **Slack Channel ID** on the field ***Slack notifications channel***

- 
This should be the channel where you want to receive Jira notifications

1. To get the **Channel ID** go to:

- 
Slack channel* 'More actions'* menu &rarr; * Open channel details &rarr; Channel ID*

- 
Paste the Channel ID in the ***Slack notifications channel***, in the EOM team&rsquo;s page.

 Then, when a Jira issue is assigned to your team, a Slack notification will appear in the defined channel:

**This is a one-time setup per team.** Once configured, all Jira automations for your team will automatically use this channel. If you need to change the channel later, just update the *Slack Channel ID* in EOM.

###  Jira Projects
These Jira Projects already send notifications using this mechanism:

- 
[RDINC](https://outsystemsrd.atlassian.net/browse/RDINC) (R&amp;D Incidents) - when incidents are assigned to a team

- 
[RDODCF](https://outsystemsrd.atlassian.net/browse/RDODCF) (ODC CD Failures) when CD failures are assigned to a team

- 
[RDCAM](https://outsystemsrd.atlassian.net/browse/RDCAM) (R&amp;D Cost Anomaly Management) - when cost anomalies are assigned to your team

If you have any questions, please contact *Process Engineering team* or report in the [https://outsystems.enterprise.slack.com/archives/C03GUL6N2TH](https://outsystems.enterprise.slack.com/archives/C03GUL6N2TH) .