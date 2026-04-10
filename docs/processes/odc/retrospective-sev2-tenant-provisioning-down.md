---
title: Retrospective-SEV2-Tenant Provisioning Down
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4276683039/Retrospective-SEV2-Tenant+Provisioning+Down
confluence_space: RKB
confluence_page_id: 4276683039
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV2-Tenant Provisioning Down

## 📘 Overview
Author:&nbsp;trueGreyFernando Alexandre

Services:&nbsp;trueBlueNeo Cmcp Cloud Management Control Plane

Severity:&nbsp;trueRedSEV2

Teams:&nbsp;trueBlueCmcp

Types:&nbsp;trueBlueOdc Service
#### 🕐 Timestamps
Started At:&nbsp;trueBlueJuly 10  6:45 PM WEST

Mitigated At:&nbsp;trueYellowJuly 10  6:58 PM WEST

Resolved At:&nbsp;trueGreenJuly 10  6:58 PM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/696-tenant-provisioning-down)
[Pagerduty incident](https://outsystems.pagerduty.com/incidents/Q0ZODWGA35A8E0)

#### Summary
&lt;div&gt;Tenant provisioning is down due to failing NGS integration&lt;/div&gt;
## 📝 RetrospectiveinfoDetails
**Ring:** ea
**System-wide impact:**&nbsp; No
**Tenant ID:**
**Tenant Prefix:**
**Routing Error Code:**
**Product Area:**
### Impact:
The tenant provisioning API was unavailable for new requests during this incident.
### Investigation and troubleshooting findings:### Resolution:
SDLC rolled back the service automatically
## Tasks performed during incident resolution:
&nbsp;
## Executive Summary
[Guidelines](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4144496679/Incident+Retrospectives+-+Playbook#STEP-3---Write-the-Executive-Summary)
## Root Causes 
[Guidelines](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4144496679/Incident+Retrospectives+-+Playbook#STEP-1---Perform-the-Root-Cause-Analysis)

If the customer needs formal RCA, please fill out the following field with the document URL

[Please follow these instructions and place the RCA URL in the field below.](https://docs.google.com/document/d/13rXmBsOJh73nV2D6Z17SIBGBu2HOTWty5ddsvU000JM/edit#heading=h.bqxasxszr5q)

RCA URL

&lt;Place the URL of the customer RCA here if you have created one&gt;
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/696-tenant-provisioning-down)

**Date**

**Source**

**User**

**Event**
July 10  6:45 PM WESTwebFernando Alexandre
Fernando Alexandre created this incident
July 10  6:45 PM WESTwebFernando Alexandre
Started date has been set to July 10  6:45 PM WEST
July 10  6:45 PM WESTwebFernando Alexandre
Version v2.14.299 is being deployed in EA and failing to connect to NGS with Authorization Violation.
July 10  6:49 PM WESTwebFernando Alexandre
NGS Dev has error &quot;No valid account &quot;ODC_TEST&quot; for auth callout response on account &quot;AUTH&quot;: account missing&quot;, misconfiguration in ngs-permissions repository
July 10  6:50 PM WESTwebFernando Alexandre
Since entry tests failed this version will be rolled back automatically by SDLC
July 10  6:50 PM WESTwebFernando Alexandre
Types has been added: ODC Service
July 10  6:51 PM WESTwebFernando Alexandre
Services has been added: NEO CMCP Cloud Management Control Plane
July 10  6:58 PM WESTwebFernando Alexandre
Service has rolled back successully and downtime finished
July 10  6:58 PM WESTwebFernando Alexandre
Incident has been resolved
July 10  6:58 PM WESTwebFernando AlexandreSystem-wide impact has been set: NoJuly 10  6:58 PM WESTwebFernando AlexandreImpact has been set: The tenant provisioning API was unavailable for new requests during this incident.July 10  6:58 PM WESTwebFernando AlexandreResolution has been set: SDLC rolled back the service automatically