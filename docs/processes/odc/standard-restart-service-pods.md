---
title: [Standard] Restart service pods
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/5161910323/Standard+Restart+service+pods
confluence_space: RKB
confluence_page_id: 5161910323
last_synced: 2026-04-09
owner: Process Engineering
---

# [Standard] Restart service pods

# Summary
This change involves the manual restart of a specific service&rsquo;s pods, potentially needed because some inconsistency or bug has appeared in that service that has caused the pods to act erratically or otherwise have caused them to stop working properly, but not enough to the point that Kubernetes attempts to restart them itself.
## General Information
**Change Type**

STANDARDBlue

**Change Risk**

LOWBlue

**Downtime Involved**

No

**Rollback Available**

No

**Implementation Team**

SRE

**Component(s)/Asset(s)**

Applicable for any Service

**Impact Description**

No impact expected

**RFC Example**

RFC-2712ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 
## Pre-requisites
- 
In the RFC that will be created the following information will be present:

- 
AWS Account to use (which stamp)

- 
K8s Deployment name whose pods we want to restart

### Technical requirements
- 
Make sure to double check the deployment whose pods we are restarting is the one associated to the service we want to restart

### Communication
- 
No communication needed.

### Expected duration
15 minutes.
## Implementation Plan### Implementation actions- 
In conjunction with the information given about the service that needs restarting and in which stamp it is present, follow this runbook to restart the service pods &rarr; Restart service pods 

### Testing and validation plan
We&rsquo;ll be able to track if the restart was successful by the last kubectl command we run.
### Rollback plan
This plan doesn&rsquo;t need a rollback. If we delete a pod by restarting the deployment it belongs to, a new one will emerge and take its place automatically.
## Post Implementation
We&rsquo;ll be able to track and monitor the new service pods depending on the service that was restarted. The team requesting the restart should point to the respective dashboard. 

For example, if Data Fabric teams are making the request, the Dashboards will be the following : 

- 
Query Engine [Dashboard](https://outsystems.grafana.net/d/B8fujKKVz/query-engine)

- 
Data Bridge [Dashboard](https://outsystems.grafana.net/d/_FSmCeqnz/data-bridge?orgId=1&amp;from=now-3h&amp;to=now&amp;timezone=browser&amp;var-ring=dev&amp;var-container=outsystems-databridge-service&amp;var-cluster=$__all&amp;refresh=5s)

- 
Nats2Avatica [Dashboard](https://outsystems.grafana.net/d/IJ2_noe7k/nats2avatica?orgId=1&amp;from=now-3h&amp;to=now&amp;timezone=browser&amp;var-ring=dev&amp;var-container=outsystems-nats2avatica-service&amp;var-cluster=$__all)

- 
Query Engine Scaler [Dashboard](https://outsystems.grafana.net/d/ee8h9xw11slc0e/query-engine-scaler)

We need to check the respective service to validate that its functioning has indeed gone back to normal.