---
title: [Standard] Asset Resources Increase Request
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/5401313419/Standard+Asset+Resources+Increase+Request
confluence_space: RKB
confluence_page_id: 5401313419
last_synced: 2026-04-09
owner: Process Engineering
---

# [Standard] Asset Resources Increase Request

## 1. Summary
In the context of Incident Response and Serviceability, a common problem arises when asset owners fail to follow up on resource consumption promptly, or there is a sudden increase in usage, or even due to unexpected bugs or patterns that can reveal an existing issue.

This issue may result in OOMKilled events (out-of-memory) or even CPU Throttling, which, depending on the asset, can lead to unavailability and significant impact.

**Increasing **such Kubernetes requests or limits is a change that should have no adverse effect:
- 
The asset is already experiencing instability/unavailability;

- 
It implies no Downtime (as it respects Pod Disruption Budget and HA settings);

- 
Such overrides are &ldquo;temporary&rdquo; and will be overridden after proper analysis from the team.

**IMPORTANT**: The RFCs cannot be closed before the post-implementation tasks are done.
## 2. General Information
**Change Type**

Standard

**Approved Normal RFC**

*Applicable only for Standard Changes*

RFC-3614ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Change Risk**

Low

**Downtime Involved **

No

**Rollback Available**

Yes

**Implementation Team**

SRE

**Component(s)/Asset(s)**

Flux components (HelmRelease / Kustomizations)

Deployments, Statefulset, or CronJobs

**Impact Description**

&ldquo;Restarts asset&rdquo; with a different set of resource configurations, following the configured PDBs, to recover serviceability.
## 3. Pre-requisites### Inputs for execution- 
List of affected clusters

- 
List of assets that need a change in the resources:
- 
Asset Type:
- 
Deployment

- 
Daemonset

- 
Statefulset

- 
Cron Job

- 
Asset Identification
- 
Name

- 
Namespace

- 
Container

- 
New values for resources (`requests` and `limits`)
- 
must be an increase

- 
Process to stop reconciliation, one per asset of the list above:
- 
Suspend HelmRelease

- 
Suspend Flux using Annotations

The inputs can be provided in a table like the following one (example):

**Clusters**

**Asset type**

**Name**

**Namespace**

**Container**

**Resource new values**

**How to stop reconciliation**

ngs-ga-eu-central-1-01

Statefulset

nats

nats-hub

nats
yaml
Suspend HelmRelease

- 
Name: `nats-hub-helm-release`

- 
Namespace: `flux-system`

ngs-ga-eu-central-1-01

Deployment

karpenter

karpenter-system

karpenter
yaml
Suspend Flux using Annotation

- 
Name: `core-stack-deploy-apps-karpenter`

- 
Namespace: `flux-system`

### Technical requirements
- 
Access in clusters as PowerUser

- 
neoctl / kubectl / k9s / flux (cli) to proceed with the changes

### Communication
- 
No communication is needed as the resource change of Deployment/StatefulSet does not bring downtime, as they change the values respecting a rollout (one by one)

### Expected duration
10 min per cluster
## 4. Implementation Plan### Implementation actions
Execute the following steps for each cluster in the list.
#### Connect to the cluster
Use `neoctl` to connect to the cluster.
#### Stopping asset reconciliation
According to the type of process to execute the reconciliation:

**Type**

**Command**

HelmRelease
 \
  -n ]]>
Flux using Annotations
  \
  -n  \
  kustomize.toolkit.fluxcd.io/reconcile=disabled]]>#### Change resources
According to the resource type, execute one of the following commands.

The script `k8s_patch_resources.sh` source code is available at [https://github.com/OutSystems/ice-scripts/tree/main/shell](https://github.com/OutSystems/ice-scripts/tree/main/shell).

But you can also download from here:

**Asset Type**

**Command**

Deployment
bash" \
  --namespace "" \
  --container "" \
  --cpu-request "" \
  --cpu-limit "" \
  --mem-request ""
  --mem-limit ""]]>
Statefulset
bash" \
  --namespace "" \
  --container "" \
  --cpu-request "" \
  --cpu-limit "" \
  --mem-request ""
  --mem-limit ""]]>
Cron Job
bash" \
  --namespace "" \
  --container "" \
  --cpu-request "" \
  --cpu-limit "" \
  --mem-request ""
  --mem-limit ""]]>
Daemonset
bash" \
  --namespace "" \
  --container "" \
  --cpu-request "" \
  --cpu-limit "" \
  --mem-request ""
  --mem-limit ""]]>### Testing and validation plan
Check if the pods are being created with the new values.
### Rollback plan#### Option A: Revert the values changed
Running the change resources command, setting the previous values.
#### Option B: resume the reconciliation
Execute one of the following commands

**Type**

**Command**

HelmRelease
 \
  -n ]]>
Flux using Annotations
  \
  -n  \
  kustomize.toolkit.fluxcd.io/reconcile-]]>
Next, force the Flux Kustomization reconcile:
 -n ]]>## 5. Post Implementation 
After the team fixes the bug on the asset and the new release reaches the affected ring, we need to allow the Helm Release or the Flux Kustomization to apply the new values.

For that, you need to reverse the suspension of the reconciliations:

**Type**

**Command**

HelmRelease
 \
  -n ]]>
Flux using Annotations
  \
  -n  \
  kustomize.toolkit.fluxcd.io/reconcile-]]>## 6. Other
- 
Be aware that the annotation `kustomize.toolkit.fluxcd.io/reconcile=disabled` will cause drift in the event of a new release of the asset.

## 7. Useful links/Related articles