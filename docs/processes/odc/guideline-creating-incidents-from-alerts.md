---
title: [Guideline] - Creating Incidents from alerts
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/3691446464/Guideline+-+Creating+Incidents+from+alerts
confluence_space: RKB
confluence_page_id: 3691446464
last_synced: 2026-04-09
owner: Process Engineering
---

# [Guideline] - Creating Incidents from alerts

**Version Control - **Current Version - 1.0  / Release Date -    

Next Release Planned -  TBD   

Please read the [**Process Release Notes**](#) page to check what will change. 

**Table of Contents**
# How to create incidents on Jira from Grafana Alerts?
**On Grafana:**
- 
On each alerting rule, add the following labels:

- 
alertingtool = moogsoft

- 
severity

- 
severity = critical - corresponding to a P2 issue, **or **

- 
severity = error - corresponding to a P2 issue **or**

- 
severity = warning - corresponding to a P3 issue **or**

- 
severity = info - corresponding to a P3 issue

- 
team=name of your team

**On PagerDuty:**
- 
Create services on PagerDuty for each service you have been monitored on Grafana (check [here](https://support.pagerduty.com/docs/services-and-integrations) the specifics on how to create a Service on PagerDuty). 

:light_bulb_on:atlassian-light_bulb_on:light_bulb_on:#FFFAE6
**BEST PRACTICE**

We do recommend creating as many services on PagerDuty as assets/services you have on Grafana being monitored.

Doing this isolates each service/asset and promotes easier information maintenance and service handover to other teams if needed.

- 
Go to PagerDuty &gt; Integrations &gt; Jira Cloud

- 
Select on the checkbox **Select PagerDuty Service** the name of the service you created on Grafana and on the checkbox **Select a Jira Project** the &ldquo;Neo R&amp;D Incidents&rdquo; using [Jira Cloud Extension](https://identity.pagerduty.com/global/authn/authentication/PagerDutyGlobalLogin/subdomain)

- 
Then click on** Connect Jira Project** blue bottom to connect the service to the RDINC Jira Project

- 
Fill the Configuration Name field with **&ldquo;*****&lt;Service Name&gt; Alerts*****&ldquo;**

- 
Select the option ***Incident*** on Jira Issue Type field* *

- 
Select the option ***Automatic** *in* *Create Issues Mode field to create Jira Incidents automatically from PagerDuty

- 
Check the flag Sync Notes and select the account as **&ldquo;*****Pagerduty Integrations*****&rdquo; **- this setup will synch comments between tools

- 
Map PagerDuty statuses to Jira Statuses:

- 
*Triggered Status* on PagerDuty to *Team Assigned*

- 
*Acknowledged Status* to *Troubleshooting In Progress*

- 
*Resolved Status* to *Solved*

- 
Map PagerDuty priorities to Jira priorities:

- 
*P1* on PagerDuty is *Urgent*

- 
*P2* on PagerDuty is *High*

- 
*P3* on PagerDuty is *Normal*

- 
*P4* on PagerDuty is *Low*

- 
Map the following PagerDuty Attributes to Jira Issue Field Names:

- 
*Incident Title* to *Summary*

- 
*Incident Description* to *Description*

- 
*Teams available* to *Teams*

- 
*Constant Value* to *Labels* and enter the following label `triggered_alerts`

**On Slack:**

On [#rd-observability-eng-ops](https://outsystems.slack.com/archives/C013ZRU697D) slack channel create a support ticket to integrate Moogsoft with Grafana, PagerDuty, and then PagerDuty with Slack sharing the following:

- 
team label value from Grafana

- 
service name/ID created on PagerDuty

- 
slack channel name/ID that you want to receive those incidents

**Notifications on your team&rsquo;s channel**

If your team wants to be notified of these incidents on your team&rsquo;s slack channel, you just need to do this request on   [#rd-jira-confluence-support](https://outsystems.slack.com/archives/C0151C6C2BA)
# Managing incidents on Jira
These incidents will appear on Jira on the [Triggered Alerts Incidents](https://outsystemsrd.atlassian.net/jira/software/c/projects/RDINC/boards/1947) Jira board of RDINC Jira Project.

This board will show an overview of all the incidents labeled as `triggered_alerts`.

### **Fields Automation on Triggered Alerts Incidents**
The following fields will be filled automatically during incident creation:

- 
*Core User Journey* set up to* Not affecting any Core Journey*

- 
*Detected by alarms* set up to *Yes* by default

- 
*Workaround available* set up to *No* by default