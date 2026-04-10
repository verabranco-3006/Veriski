---
title: Retrospective-SEV1-[DEMO] Sev-1 Incident to Showcase Rootly
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4228579487/Retrospective-SEV1-+DEMO+Sev-1+Incident+to+Showcase+Rootly
confluence_space: RKB
confluence_page_id: 4228579487
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV1-[DEMO] Sev-1 Incident to Showcase Rootly

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV1

Teams:&nbsp;trueBlueSre&nbsp;trueBlueNeo Platform Theseus
#### 🕐 Timestamps
Started At:&nbsp;trueBlueJune 19 11:35 AM WEST

Mitigated At:&nbsp;trueYellowJune 19  4:01 PM WEST

Resolved At:&nbsp;trueGreenJune 19  4:01 PM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/586-demo-sev-1-incident-to-showcase-rootly)
[Confluence page](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4227793027)

[Pagerduty incident](https://outsystems.pagerduty.com/incidents/Q2LC8ZHMVQHJ2X)

[Slack channel](https://slack.com/app_redirect?channel=C078TDALWSF&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3024645)

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

Filipe Seixeira
#### Summary
----------------------------------------------**CONSIDERATIONS BEFORE PERFORMING THE ESCALATION TO R&amp;D (MANDATORY)**
None of the below points should be overlooked. Failure to do so may imply unnecessary effort.* * *
Ensure the ticket has been **categorized**, otherwise, the R&amp;D escalation will go unnoticed and not be worked on!**1.** For **Incidents**, the **IMAX** was consulted **beforehand** on which:- No incident models were found for the reported symptoms **OR**
- The incident model did not solve the issue **OR**
- The next step indicated in the Incident Model is an escalation to R&amp;D.
**2.** For **Questions**, the ChatODC on the **Slack channel** didn't return an acceptable answer.
**3.** Any other requests that explicitly indicate an R&amp;D escalation is needed.
**4**. **Incident impact assessment** was based on the **prioritization scoring matrix**.* * ***R&amp;D ESCALATION FORM**
Section comments can be removed for R&amp;D easier interpretation.**ISSUE DESCRIPTION AND HOW TO REPRODUCE**
- A paragraph detailing the issue or question.
- If available, the steps that must be taken to reproduce the issue under discussion.**IMPACT ON THE CUSTOMER**
Brief description of the impact on the customer/development team/other, including:
- Stage where the problem is happening (Development / QA / Production);
- Frequency of the problem;
- Business impact or/and development impact;**TROUBLESHOOTING STEPS &amp; WORKAROUND**
- What are the most relevant findings and hypotheses from our analysis so far?
- What workaround was tried so far, if any, and how did they impact the reported behavior?
- Was this case discussed previously with anyone from R&amp;D? If so with whom and which R&amp;D team?
- If it is related, or there is a possibility of being related, to an already existing RDINC, please specify it.**TECH DATA OR ANY OTHER RELEVANT INFO**
- Tenant ID or Activation Code where the problem is occurring.
- OutSystems revisions of the components involved (mandatory). This includes for example revision of ODC Studio or Forge Supported Plugins.
- Diagnostics report (mandatory for ODC Studio-related issues).
- All technical files or data, including OMLs.
- Error stacks, screenshots, or any other files like error logs or traces._&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 RetrospectiveinfoDetails
**Ring:** ga
**System-wide impact:**&nbsp; Yes
**Tenant ID:** 494dbe13-397f-4c12-8c64-7e005b39c81b
**Tenant Prefix:** gs-sandbox-ga-eu-01
**Routing Error Code:** OS-BERT
**Product Area:** -
### Impact:
Runtime application is down
### Investigation and troubleshooting findings:
Found all the information throught the slo
### Resolution:
We executed the RFC by restarting the pods, the service is now recovered and the apps in runtime are now up and running as expected
## Tasks performed during incident resolution:
**Summary:**[https://outsystemsrd.atlassian.net/browse/RFC-XXX](https://outsystemsrd.atlassian.net/browse/RFC-XXX)

**Status:**trueBlueopen

&nbsp;
## Executive Summary
[Guidelines](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4144496679/Incident+Retrospectives+-+Playbook#STEP-3---Write-the-Executive-Summary)
## Root Causes 
[Guidelines](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4144496679/Incident+Retrospectives+-+Playbook#STEP-1---Perform-the-Root-Cause-Analysis)

If the customer needs formal RCA, please fill out the following field with the document URL

[Please follow these instructions and place the RCA URL in the field below.](https://docs.google.com/document/d/13rXmBsOJh73nV2D6Z17SIBGBu2HOTWty5ddsvU000JM/edit#heading=h.bqxasxszr5q)

RCA URL

&lt;Place the URL of the customer RCA here if you have created one&gt;
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/586-demo-sev-1-incident-to-showcase-rootly)

**Date**

**Source**

**User**

**Event**
June 19 11:24 AM WESTwebRootly
created an alert via
June 19 11:24 AM WESTwebRootly
Rootly created this incident
June 19 11:24 AM WESTwebRootly
In triage date has been set to June 19 11:24 AM WEST
June 19 11:24 AM WESTwebRootly[Slack Channel](https://slack.com/app_redirect?channel=C078TDALWSF&amp;team=T041063TZ) has been createdJune 19 11:25 AM WESTwebRootly[PagerDuty Incident](https://outsystems.pagerduty.com/incidents/Q2LC8ZHMVQHJ2X) has been created.
📲 Notified Filipe Seixeira by push notification.  (via Android)&nbsp;&nbsp;📞 Notified Filipe Seixeira by phone.&nbsp;&nbsp;📲 Notified Filipe Seixeira by push notification.  (via Android)June 19 11:25 AM WESTwebRootlyFilipe Seixeira has been assigned as EngineerJune 19 11:25 AM WESTwebRootly
Ring: ga
System-wide impact:  
Tenant ID: 494dbe13-397f-4c12-8c64-7e005b39c81b
Tenant Prefix: gs-sandbox-ga-eu-01
Routing Error Code: OS-BERT
Product Area: -
June 19 11:25 AM WESTwebRootly
Filipe Seixeira acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q2LC8ZHMVQHJ2X). (via Mobile)
June 19 11:35 AM WESTwebMiguel Afonso
Incident has been started
June 19 11:35 AM WESTwebRootly
Pagerduty Integrations acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q2LC8ZHMVQHJ2X). (via Mobile)
June 19 11:56 AM WESTwebMiguel AfonsoSystem-wide impact has been set: YesJune 19 11:56 AM WESTwebMiguel AfonsoImpact has been set: Runtime application is downJune 19 11:56 AM WESTwebMiguel AfonsoInvestigation and troubleshooting findings has been set: Found all the information throught the sloJune 19 11:56 AM WESTslackVera Branco
After the zoom call, we decided to move with plan A - create a Request for Change (RFC-XXXX).
June 19 12:06 PM WESTslackhenrique.fonseca
After a zoom call we decided to create an RFC
June 19 12:10 PM WESTwebMiguel AfonsoSend ZenDesk private comment has been set: We are executing the RFCJune 19 12:10 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
We are executing the RFC
June 19 12:10 PM WESTwebRootlySend ZenDesk private comment has been unsetJune 19 12:10 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

June 19 12:11 PM WESTwebMiguel AfonsoSwarm has been set: TheseusJune 19 12:11 PM WESTwebRootly
Pagerduty Integrations added Laura Huysamen as responder in [PagerDuty](https://outsystems.pagerduty.com/incidents/Q2LC8ZHMVQHJ2X)
June 19 12:12 PM WESTwebRootly
Laura Huysamen joined this [PagerDuty](https://outsystems.pagerduty.com/incidents/Q2LC8ZHMVQHJ2X) incident.
June 19 12:12 PM WESTwebRootly
Laura Huysamen acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q2LC8ZHMVQHJ2X). (via Mobile)
June 19  3:59 PM WESTslackhenrique.fonseca
We executed the RFC by restarting the pods, the service is now recovered and the apps in runtime are now up and running as expected.
June 19  4:00 PM WESTwebHenrique FonsecaSend ZenDesk private comment has been set: We executed the RFC by restarting the pods, the service is now recovered and the apps in runtime are now up and running as expectedJune 19  4:00 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
We executed the RFC by restarting the pods, the service is now recovered and the apps in runtime are now up and running as expected
June 19  4:00 PM WESTwebRootlySend ZenDesk private comment has been unsetJune 19  4:00 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

June 19  4:01 PM WESTwebHenrique Fonseca
Incident has been resolved
June 19  4:01 PM WESTwebHenrique FonsecaResolution has been set: We executed the RFC by restarting the pods, the service is now recovered and the apps in runtime are now up and running as expectedJune 19  4:01 PM WESTwebRootly
Pagerduty Integrations marked the incident as resolved through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q2LC8ZHMVQHJ2X). (via Api)
June 19  4:01 PM WESTwebRootly[Confluence Page](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4228251784) has been createdJune 19  4:01 PM WESTwebRootly
The retrospective document created can be checked here: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4228251784
June 19  4:14 PM WESTwebRootly[Confluence Page](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4227793027) has been createdJune 19  4:14 PM WESTwebRootly
The retrospective document created can be checked here: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4227793027
## 📝 Follow Up Items[View on Rootly](https://rootly.com/account/incidents/586-demo-sev-1-incident-to-showcase-rootly#nav-action-items)

**Summary**

**Priority**

**Status**

**Assignee**

**Links**
We need to improve this runbooktrueYellowMediumtrueBlueOpen