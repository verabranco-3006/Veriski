---
title: Deploy Service
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/3016359945/Deploy+Service
confluence_space: RCP
confluence_page_id: 3016359945
last_synced: 2026-04-09
owner: Process Engineering
---

# Deploy Service

Here are a few &ldquo;did you know&rdquo; things that can be useful to you in the future (they were to me):
## &ldquo;running&rdquo; folder maintenance/cleanup
- 
There is a UseAgressiveGarbageCollect property that is used to decide which platform setting to use as &ldquo;threshold to delete in hours&rdquo;:

- 
`DeployService.DevelopmentThresholdToDeleteInHours` when development environment:

- 
GetServerPurpose() == ServerPurpose.Development

- 
`DeployService.ProductionThresholdToDeleteInHours` when production environment:

- 
GetServerPurpose() != ServerPurpose.Development

- 
`filenames.cache` and `tempFilenames.cache` (files in the running folder) are used to know which folders are the most recent ones (the ones the deployment service deployed). They should not be deleted, as such, could cause incorrect folders deletion.