---
title: Launch Darkly Feature Toggles Change Management
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/5034213417/Launch+Darkly+Feature+Toggles+Change+Management
confluence_space: RKB
confluence_page_id: 5034213417
last_synced: 2026-04-09
owner: Process Engineering
---

# Launch Darkly Feature Toggles Change Management

Currently SRE is not enabled yet to work with Launch Darkly, so the changes need to be requested to Release Engineering in the slack channel [#rd-sdlc-support](https://outsystems.slack.com/archives/C02FDRXNER0).

To perform changes in negative rings teams are autonomous: LaunchDarkly / Remote Feature Toggles Slack App 

**Normal Request Change:**

Teams can point to this generic change catalog: [Standard/Normal] Enable Launch Darkly Feature Toggle in ODC 

- 
Turning a feature toggle ON directly on a positive ring, without validating in previous rings.

- 
Turning a feature toggle ON for a specific tenant (i.e. Private EAP use case)

- 
Assuming that the feature was OFF in all the previous rings. 

- 
Turning a feature toggle OFF** **directly in Production after the bake period

**Standard Request Change: **

Teams can point to this generic change catalog: [Standard/Normal] Enable Launch Darkly Feature Toggle in ODC 

- 
Turning a feature toggle OFF during bake time of the asset that uses it. 

- 
Turning a feature toggle ON after being disabled. 

**No need for a request change, follows the **[**SDLC policy**](https://drive.google.com/file/d/1IEfgpO1DVl78Yxuu80nuQGkM1hXXuFJU/view)**:**

- 
Turning a feature toggle ON in a positive ring, after that feature being enabled in all previous rings. 

**Pre-requirements:**

- 
Ensure the code hidden behind the feature toggle was tested via SDLC process

- 
Ensure the Launch Darkly environment(s) that reflect the Production/Positive rings require approvals for changes (configuration option in LD)