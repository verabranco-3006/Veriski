---
title: Retrospective-SEV3-Sub-ticket of #3039874 (jwksUrl is not updated when editing identity provider)
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4334977202/Retrospective-SEV3-Sub-ticket+of+3039874+jwksUrl+is+not+updated+when+editing+identity+provider
confluence_space: RKB
confluence_page_id: 4334977202
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV3-Sub-ticket of #3039874 (jwksUrl is not updated when editing identity provider)

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV3

Teams:&nbsp;trueBlueOdc Governance
#### 🕐 Timestamps
Started At:&nbsp;trueBlueAugust 5  5:30 PM WEST

Mitigated At:&nbsp;trueYellowAugust 5  5:37 PM WEST

Resolved At:&nbsp;trueGreenAugust 5  5:37 PM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/822-sub-ticket-of-3039874-jwksurl-is-not-updated-when-editing-identity-provider)
[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3045018)

#### Summary
----------------------------------------------**ISSUE DESCRIPTION AND HOW TO REPRODUCE**- Basically the issue is that, after creating an identity provider with an incorrect discovery endpoint, or if the `jwksUrl` changes afterwards for some reason, the only way to update this on our side is to recreate the identity provider (delete -&gt; create) rather than just editing and saving it.- This results in login errors on the client side because there is a mismatch of the **key Ids (kids)** found in the **jwks Url:**![](https://supportoutsystems.zendesk.com/attachments/token/eulQ5FsJMHzkV9bUP1aqCykJ5/?name=image.png)
- This had already been escalated and discussed with R&amp;D in the context of another ticket - RDINC-20337 - and R&amp;D claimed to have made changes to this behavior.![](https://supportoutsystems.zendesk.com/attachments/token/VuLdX9Al9wcPlNYG2Eky8dAPT/?name=image.png)
- However, checking the current ODC Portal logic, seems no changes were made to the `jwksUrl` logic (I'd like someone to prove me wrong on this one, but that's what it seems to me):- From ODC Portal, when saving an already existing identity provider (after editing), we still do send to the Identity API the same `jwksUrl` that was set previously:![](https://supportoutsystems.zendesk.com/attachments/token/deSkFlVYPju9MVo2OVDj2MECt/?name=image.png)- Part of this IdP configuration structure is the `jwksUrl`, for which we find no references anywhere, so it doesn't look like it is validated or changed, so it sends the same value that was already present in the configuration:![](https://supportoutsystems.zendesk.com/attachments/token/xoAoMJdQkxQOY6gcdanxp89Np/?name=image.png)- There's still the chance that Identity automatically checks for new `jwksUrl` but I can't be sure of that, considering these errors still occur even after editing and saving the identity provider configuration (does not fetch the updated `jwksUrl` from the discovery endpoint).**IMPACT ON THE CUSTOMER**- Already resolved by recreating the identity provider, but it's not the first time this happens.
- This results in the generic error `Unexpected error when authenticating with identity provider`**TROUBLESHOOTING STEPS &amp; WORKAROUND**
N/A**TECH DATA OR ANY OTHER RELEVANT INFO**- Escalated to ODC Governance team since this was the team that had actions made in the context of the previous escalation - RDINC-20337 - but feel free to assign or discuss with Identity team as well._&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 RetrospectiveinfoDetails
**Ring:** -
**System-wide impact:**&nbsp; No
**Tenant ID:** N/A
**Tenant Prefix:** N/A
**Routing Error Code:** N/A
**Product Area:** Phoenix::Phoenix Portal::Users &amp; access - Users
### Impact:
There is no actual impact since the issue was already fixed. 
### Investigation and troubleshooting findings:### Resolution:
The original fix was to not set the jwks url at portal end, in order to identity fetch the newest one from the well-known, every time a provider in saved from ODC portal
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/822-sub-ticket-of-3039874-jwksurl-is-not-updated-when-editing-identity-provider)

**Date**

**Source**

**User**

**Event**
August 5 11:31 AM WESTwebRootly
created an alert via
August 5 11:31 AM WESTwebRootly
Rootly created this incident
August 5 11:31 AM WESTwebRootly
In triage date has been set to August 5 11:31 AM WEST
August 5 12:23 PM WESTwebTelmo Martins
Teams has been added: Identity Business
August 5 12:23 PM WESTwebTelmo Martins
Teams has been removed: ODC Governance
August 5 12:24 PM WESTwebTelmo Martins
Hello Identity Biz team. Can you kindly assist. When we save an existing provider, if identity keep the same well-known data or retrieves the latest urls again from the well-known doc.
Regards.
August 5 12:34 PM WESTwebTelmo Martins
Teams has been added: ODC Governance
August 5 12:35 PM WESTwebTelmo Martins
We're still checking at our end, because we might send the jwksUrl in the payload, causing this.
August 5  2:24 PM WESTwebTelmo Martins
Teams has been removed: Identity Business
August 5  4:14 PM WESTwebTelmo Martins
hello
this bug was already fix a few months ago.
We doublecheck confirmed that currently it keeps working as expected and we just need to edit and save the IdP in order to the new jwks url from the well-known be used.
August 5  5:30 PM WESTwebTelmo Martins
Incident has been started
August 5  5:37 PM WESTwebTelmo Martins
Incident has been resolved
August 5  5:37 PM WESTwebTelmo MartinsSystem-wide impact has been set: NoAugust 5  5:37 PM WESTwebTelmo MartinsImpact has been set: There is no actual impact since the issue was already fixed. August 5  5:37 PM WESTwebTelmo MartinsResolution has been set: The original fix was to not set the jwks url at portal end, in order to identity fetch the newest one from the well-known, every time a provider in saved from ODC portal