<!-- DRY RUN DRAFT — generated 2026-05-08 by `postmortem` skill for testing purposes. NOT for Confluence publish. The canonical retrospective lives at https://outsystemsrd.atlassian.net/wiki/spaces/RPE/pages/6313214121 (owned by Laura Huysamen). -->
<!-- Page title (for Confluence, if ever published): [RDINC-78058] - Retrospective - SEV2-ODC - System-wide OSALL tenant-provisioning-success-rate -->

## 📘 Overview

Severity: **SEV2**

Teams: **SRE Global, ODC RDO, Tenant Lifecycle, ICE**

Types: **System-Wide**

Assets: **outsystems-runtimedatabase-operator**

### 🕐 Timestamps

Started At: **2026-04-01 20:01 UTC** (osall)

Mitigated At: **2026-04-02 06:11 UTC** (osall)

Resolved At: **2026-04-02 09:35 UTC** (osall)

| Metric | Value |
| --- | --- |
| **MTTA** (Mean Time To Acknowledge) | 48 min |
| **MTTM** (Mean Time To Mitigate) | 10h 10m |
| **MTTR** (Mean Time To Resolve) | 13h 34m |
| Detection lag (deployment → SLO alert) | 5h 11m |

> ⚠️ SEV2 MTTR target is < 8h. Actual MTTR exceeded target by ~5.5h, driven by the 5h11m detection lag (Finding 2) and the rollback failure that required propagating a new fix version (Finding 1).

### 🔎 Detection & Trigger

**Detection:** SLO alert — `tenant-provisioning-success-rate` on `Sys-Wide-OSALL-PaaS` fired when average burn rate exceeded 5x for 10 continuous minutes on the OSALL ring.

**Trigger:** Deployment of `flux-stamp-config-core-stack v0.37.424` to OSALL as part of [RDICE-5369](https://outsystemsrd.atlassian.net/browse/RDICE-5369) — an upgrade of the OpenTofu version and tofu controller to positive rings. The new tofu controller version did not start in OSALL, leaving Terraform-dependent provisioning operations blocked.

### 🔗 Links

- [Rootly Incident Page](https://rootly.com/account/incidents/47426-your-slo-osall-tenant-creation-sucessrate-osall-tenant-creation-success-successrate-needs-attention-0dfa4bab-6614-40c7-9f56-c0d6b70bd6a4)
- [Jira Incident Page](https://outsystemsrd.atlassian.net/browse/RDINC-78058)
- [Incident Slack Channel](https://slack.com/app_redirect?channel=C0AQ8S4T8KF&team=T041063TZ)
- [GitHub PR #610 — fix(RDICE-5369): Terraform controller sidecar image](https://github.com/OutSystems/flux-stamp-config-core-stack/pull/610)
- [Grafana — Runtime Database Operator](https://outsystems.grafana.net/d/ma495t7/runtime-database-operator?orgId=1&var-ring=osall)
- [Grafana — TLC Operational Dashboard](https://outsystems.grafana.net/d/fT3aF6snzasdb/tlc-operational-dashboard)
- [Fast-track RDO 1.0.420 to OSALL +1 Ring](https://outsystemsrd.atlassian.net/wiki/pages/viewpage.action?pageId=6180274306)

### 🧑‍🚒 Incident Roles

| Role | Participant(s) |
| --- | --- |
| Incident Commander | Sam Audu (initial), Jeg Subramaniam (from 01:59 UTC Apr 2), André Rosendo (from 09:19 UTC Apr 2) |
| Engineers | Anurag Kothare (ODC RDO), Kishore Kamath (ICE), Kevin Tek, Tushita Shrivastava |
| Internal Communications Leader | Laura Huysamen, Tiago Oliveira |
| RCA participants | [TODO] |
| Retrospective Commander | Laura Huysamen |
| Reviewer | [TODO] |
| Approver | [TODO] |
| Approval Date | [TODO] |

## 📝 Retrospective

### Executive Summary

On April 1, 2026, the SLO alert for `tenant-provisioning-success-rate` fired on the OSALL ring, triggered by the deployment of `flux-stamp-config-core-stack v0.37.424` as part of [RDICE-5369](https://outsystemsrd.atlassian.net/browse/RDICE-5369) — an upgrade of the OpenTofu version and tofu controller to positive rings. The deployment was enabled in OSALL at approximately 14:50 UTC, several hours before the SLO alert fired at 20:01 UTC.

The new tofu controller version did not start in OSALL, leaving the Terraform controller with 0 running replicas. All tenant provisioning operations that required Terraform — specifically database creation and modification — were blocked, and environments became stuck in the `Reconciling on DatabaseReady` state. A monitoring alarm for "no replicas for Terraform Controller" that should have caught this had been silently broken since a prior version upgrade changed the K8s deployment name without updating the alarm configuration. As a result, the alarm did not fire when the controller went down, and the first signal was the slower SLO alert.

Only `rundev` environments were affected; no customer production environments were impacted. A rollback was attempted but failed because the new and old controller versions shared the same version number, so the deployment system could not differentiate them. A new fix version was created via [PR #610](https://github.com/OutSystems/flux-stamp-config-core-stack/pull/610) and merged at 23:47 UTC. Fix propagation took approximately 6 hours.

The incident was mitigated at 06:11 UTC on April 2 when the SLO burn rate dropped below 1x. At that point, approximately 62 `rundev` environments remained stuck in `Reconciling on DatabaseReady`. They were addressed via a self-heal mechanism deployment ([RDODCP-905](https://outsystemsrd.atlassian.net/browse/RDODCP-905)) rather than manual RFC intervention. The incident was resolved at 09:35 UTC on April 2. Total duration: approximately 13.5 hours.

### Impact

- **~62 affected `rundev` environments** stuck in `Reconciling on DatabaseReady` state at mitigation time
- **0 customer (production) environments** impacted
- New tenant provisioning in the OSALL ring was blocked for the duration of the incident

| **Tenant ID** | **Customer Name** | **Ring** | **Region** | **# Occurrences** | **Customer Reported Incident** |
| --- | --- | --- | --- | --- | --- |
| (rundev environments only) | Internal | osall | eu-central-1, us-east-1 | ~62 stuck create ops | — |

> Source: [TLC Operational Dashboard](https://outsystems.grafana.net/d/fT3aF6snzasdb/tlc-operational-dashboard)

### Communication

#### External Communication

No entry was posted to the [OutSystems Status Page](https://status.outsystems.com) during this incident. This was the correct decision — only `rundev` environments used for internal development and testing were affected; zero customer production environments were impacted, so external communication was not required. Status page history for April 1–2, 2026 contains no entries related to this incident.

#### Internal Communication

Internal communication was handled by designated Internal Communications Leaders (Laura Huysamen, Tiago Oliveira) throughout the incident.

A clear written status summary was provided mid-incident at 01:01 BST (April 2) capturing root cause, failed rollback, and next steps. This allowed the incoming Incident Commander (Jeg Subramaniam, taking over at 01:59 UTC) to ramp up without an extended briefing.

At 02:51 BST, the decision to defer manual cleanup of the 62 stuck environments to business hours via the self-heal mechanism was communicated, and ICE was released from the incident. At 03:11 BST, the alarm fix was logged as an explicit action item in the channel.

Three Incident Commander handoffs occurred over 13.5 hours (Sam Audu → Jeg Subramaniam → André Rosendo), driven by timezone coverage. Each handoff added coordination overhead — captured in Lessons Learned.

### Findings and Contributing Factors

#### Finding 1 — Tofu controller upgrade reached OSALL with no post-deployment health validation, and rollback was not possible

When `flux-stamp-config-core-stack v0.37.424` was deployed to OSALL as part of [RDICE-5369](https://outsystemsrd.atlassian.net/browse/RDICE-5369), the new tofu controller did not start. With 0 running replicas, all Terraform-dependent operations were blocked. There was no automated check to validate that the controller was running after rollout, so the failure went undetected for approximately 5 hours until the SLO alert fired.

When a rollback was attempted, it failed because the new and old controller versions shared the same version number — the deployment system could not differentiate them, forcing the team to create a new fix version and wait for full propagation.

**5 Whys:**

1. Why did tenant provisioning fail across all OSALL regions? → The Terraform controller had 0 running replicas, blocking all Terraform-dependent provisioning operations.
2. Why did the Terraform controller have 0 replicas? → The new tofu controller version deployed via `flux-stamp-config-core-stack v0.37.424` failed to start in OSALL.
3. Why did the new controller version fail to start? → [TODO: validate — suspected to be a sidecar image reference issue, since [PR #610](https://github.com/OutSystems/flux-stamp-config-core-stack/pull/610) fixed `helm/values.yaml` for the controller sidecar image; needs confirmation from ODC RDO / ICE team]
4. Why couldn't the team roll back to the previous version? → The new and old versions shared the same version number, making them indistinguishable to the deployment system.
5. Why did both versions share the same number? → [TODO: validate — needs confirmation from ICE on the versioning process for this component]

**Contributing Factors & Action Items:**

- **(CF-1a)** No automated post-deployment readiness check validated that the tofu controller was running before user-visible impact accumulated.
  - Implement post-deployment readiness validation for infrastructure controller upgrades — ODC RDO / ICE — [TODO: Create ticket]
- **(CF-1b)** Rollback was not possible because both controller versions shared the same version identifier.
  - Ensure new releases of infrastructure components have unique version identifiers to enable fast rollback — ODC RDO / ICE — [TODO: Create ticket]

**Resolution:** A fix was merged via [PR #610](https://github.com/OutSystems/flux-stamp-config-core-stack/pull/610), modifying `helm/values.yaml` to reference the correct sidecar image. The fix was deployed to OSALL and the SLO burn rate stabilized by 06:11 UTC April 2. The 62 remaining stuck environments were addressed via the [RDODCP-905](https://outsystemsrd.atlassian.net/browse/RDODCP-905) self-heal mechanism.

---

#### Finding 2 — Monitoring alarm for the Terraform Controller was silently broken, delaying detection by ~5 hours

When the controller went down, the ICE team's "no replicas for Terraform Controller" alarm did not fire. The alarm watched the old K8s deployment name, which had changed when the tofu controller version was previously upgraded as part of RDICE-5369 scope. Because the alarm was already broken before this incident, detection relied entirely on the SLO alert, which fires only after sustained burn rate accumulation — approximately 5 hours elapsed between deployment and alert.

**5 Whys:**

1. Why did the "no replicas for Terraform Controller" alarm not fire? → The alarm was configured to watch the old K8s deployment name, which had changed when the tofu controller version was upgraded.
2. Why was the alarm watching the old deployment name? → A prior upgrade as part of [RDICE-5369](https://outsystemsrd.atlassian.net/browse/RDICE-5369) changed the K8s deployment name, but the alarm configuration was not updated to match.
3. Why was the alarm not updated when the deployment name changed? → [TODO: validate — suspected because no checklist step required verification that existing alarms still reference correct resource names after infrastructure changes; needs confirmation from ICE]
4. Why was there no validation step linking alarm coverage to new resource names in upgrade checklists? → [TODO: validate — process gap suspected in change management procedure for infrastructure upgrades; needs confirmation from ICE]

**Contributing Factors & Action Items:**

- **(CF-2)** The "no replicas for Terraform Controller" alarm was broken because a prior upgrade changed the K8s deployment name without updating alarm configurations.
  - Alarm fixed as part of [RDICE-5369](https://outsystemsrd.atlassian.net/browse/RDICE-5369) follow-up.
  - Add alarm coverage validation step to infrastructure upgrade checklists: verify alarm configurations match new resource names after any naming changes — ICE — [TODO: Create ticket]

**Resolution:** The alarm was fixed as part of RDICE-5369 follow-up work. A process change to prevent similar silent alarm breakage in future upgrades is tracked as a separate action item.

---

### Action Items Summary

| **CF** | **Type** | **Action** | **Owner** | **Ticket** |
| --- | --- | --- | --- | --- |
| CF-1a | Prevent | Implement post-deployment readiness validation for infrastructure controller upgrades | ODC RDO / ICE | [TODO: Create ticket] |
| CF-1b | Prevent | Ensure unique version identifiers for infrastructure components to enable rollback | ODC RDO / ICE | [TODO: Create ticket] |
| CF-2 | Detect | Fix "no replicas for Terraform Controller" alarm to use correct deployment name | ICE | [RDICE-5369](https://outsystemsrd.atlassian.net/browse/RDICE-5369) (done) |
| CF-2 | Process | Add alarm coverage validation step to infrastructure upgrade checklists | ICE | [TODO: Create ticket] |

### 🔁 Recurrence Analysis

**Recurrence — prior incidents with related patterns identified.**

#### Same SLO (`tenant-provisioning-success-rate`, OSALL)

[RDINC-77462](https://outsystemsrd.atlassian.net/browse/RDINC-77462) (March 24, 2026 — 8 days before) fired the same SLO on the same ring. Root cause was different (Identity Operator realm creation spike, unrelated to the Terraform controller). A retrospective was completed.

One action item from that retrospective is directly relevant to this incident:

- [RDPIB-3379](https://outsystemsrd.atlassian.net/browse/RDPIB-3379) — "Establish Rollout Checklist for changes that can cause critical flow failures" — status: **Preparing Refinement** (not completed). Scope includes "Is a rollback plan in place?" and "Do we need a feature toggle?", both directly applicable to CF-1b (rollback failure) here. RDPIB-3379 was created on April 1, 2026 — the same day RDINC-78058 started.

#### Terraform controller — no running replicas pattern

The `terraform-controller`-no-replicas symptom has appeared previously:

| Incident | Ring | Date | Resolution | Notes |
| --- | --- | --- | --- | --- |
| [RDINC-68859](https://outsystemsrd.atlassian.net/browse/RDINC-68859) + 4 others | osall | Jan 25, 2026 | Still open | Cluster of 5 incidents, same component |
| [RDINC-74822](https://outsystemsrd.atlassian.net/browse/RDINC-74822) | ga | Mar 1, 2026 | Solved (5 min) | Alarm fired correctly |
| [RDINC-76310](https://outsystemsrd.atlassian.net/browse/RDINC-76310) | dev | Mar 9, 2026 | Solved | Alarm fired correctly |

The alarm worked for GA and DEV rings. In OSALL, the alarm was already broken at the time of this incident due to the deployment name change described in Finding 2.

[TODO: validate — the January 2026 OSALL incidents (RDINC-68859 cluster) are still open. Were action items created? If so, were they completed before RDINC-78058?]

### 🪞 Lessons Learned

#### What went well

- SRE on-call responded within minutes of the SLO alert and immediately engaged the RDO team.
- A clear written status summary was provided mid-incident, allowing the incoming Incident Commander to ramp up quickly.
- The decision to wait for the self-heal mechanism ([RDODCP-905](https://outsystemsrd.atlassian.net/browse/RDODCP-905)) rather than pursuing risky manual RFCs for 62 stuck environments overnight was sound.
- Internal Communications Leaders kept teams well-informed and released ICE when the risk was contained.

#### What didn't go well

- Detection delayed by ~5 hours — the "no replicas for Terraform Controller" alarm was already broken, so the first signal was the SLO alert rather than an infrastructure health alert firing immediately when the controller went down.
- Rollback path was unavailable — new and old versions shared the same version number, forcing the team to create a new fix version and wait ~6 hours for propagation rather than reverting in minutes.
- Root cause identification took approximately 2 hours after incident declaration (20:49 UTC declared → 23:02 UTC root cause identified).
- Three Incident Commander handoffs over 13 hours created coordination overhead across time zones.

#### Where we got lucky

- Only `rundev` environments were affected — existing customer environments were not impacted.
- Pre-provisioned tenants in the pool absorbed new tenant requests during the incident, preventing direct customer-visible impact.
- The incident occurred late evening UTC rather than during OSALL peak usage, limiting impact on new tenant onboarding.

## ⌛ Timeline

| **Date/Time (UTC)** | **Source** | **User** | **Event** |
| --- | --- | --- | --- |
| 2026-04-01 14:50 | Jira | Ricardo Gonçalves | 🚨 Deployment triggered — `flux-stamp-config-core-stack v0.37.424` enabled in OSALL ([RDICE-5369](https://outsystemsrd.atlassian.net/browse/RDICE-5369)) |
| 2026-04-01 20:01 | Rootly | System | 🚨 SLO alert fired — `tenant-provisioning-success-rate` burn rate ≥ 5x on OSALL |
| 2026-04-01 20:49 | Rootly | Sam Audu | 📢 Incident declared — SEV2. [Slack channel](https://slack.com/app_redirect?channel=C0AQ8S4T8KF&team=T041063TZ) |
| 2026-04-01 20:52 | Slack | Arturo Riter | 🔍 Confirmed: multiple `rundev` environments stuck in `Reconciling on DatabaseReady`, all regions |
| 2026-04-01 23:02 | Slack | Laura Huysamen | 🔍 Root cause identified — Terraform controller has 0 deployed replicas; rollback to be attempted |
| 2026-04-01 23:35 | Slack | Laura Huysamen | Rollback failed — new and old versions share same version number; new fix version being prepared |
| 2026-04-01 23:47 | GitHub | ricardomiguel-os | 🛠️ Mitigation started — [PR #610](https://github.com/OutSystems/flux-stamp-config-core-stack/pull/610) merged (fix: Terraform controller sidecar image) |
| 2026-04-02 00:01 | Slack | Kishore Kamath | Fix (`infra-core-stack DU v1.0.162`) rolling out; ~1.5h estimated propagation |
| 2026-04-02 01:59 | Rootly | Kishore Kamath | Jeg Subramaniam assigned as Incident Commander |
| 2026-04-02 02:51 | Slack | Tiago Oliveira | ~62 stuck environments identified; decision to defer manual cleanup to business hours via self-heal mechanism |
| 2026-04-02 03:11 | Slack | Tiago Oliveira | Action item logged — fix alarm for Terraform Controller (deployment name changed) |
| 2026-04-02 06:11 | Rootly | Jeg Subramaniam | ✅ Incident mitigated — SLO burn rate < 1x; system recovering |
| 2026-04-02 09:35 | Rootly | André Rosendo | ✅ Incident resolved. Total duration: ~13.5 hours |

## 🔄 Data Sources & Completeness

### ✅ Data successfully extracted

- **Jira ([RDINC-78058](https://outsystemsrd.atlassian.net/browse/RDINC-78058))** — severity, linked issues, Rootly comments, Slack channel ID, Retrospective Commander
- **Slack (#47426-sys-wide-osall-sev2-tenant-provisioning-success-rate)** — full channel history: incident start timestamp, investigation messages, root cause, rollback failure, fix status, ~62 stuck environment count, action item for alarm fix
- **GitHub ([PR #610](https://github.com/OutSystems/flux-stamp-config-core-stack/pull/610))** — fix details, merge timestamp, files changed
- **Jira ([RDICE-5369](https://outsystemsrd.atlassian.net/browse/RDICE-5369))** — trigger change, acceptance criteria, deployment comment, alert fix confirmation (2026-04-08)
- **Jira ([RFC-4739](https://outsystemsrd.atlassian.net/browse/RFC-4739), [RFC-4764](https://outsystemsrd.atlassian.net/browse/RFC-4764))** — mitigation RFCs and outcomes
- **Recurrence analysis** — RDINC searched for prior incidents with same SLO and Terraform controller pattern; [RDINC-77462](https://outsystemsrd.atlassian.net/browse/RDINC-77462) and [RDPIB-3379](https://outsystemsrd.atlassian.net/browse/RDPIB-3379) reviewed
- **Existing canonical retrospective** — [RPE page 6313214121](https://outsystemsrd.atlassian.net/wiki/spaces/RPE/pages/6313214121) (May 4, 2026, owner Inês Matos) — used as reference for already-confirmed facts in this dry-run regeneration

### ⚠️ Data still missing

- **Change Management compliance** — [TODO: validate] PR #610 was merged at 23:47 UTC April 1 during the incident. RFC-4739 and RFC-4764 were both created post-incident (April 7 and April 10). Emergency Change process requires written approval by the VS Leader (Slack or Jira comment) **before** implementation. Confirm: was VS Leader approval obtained in Slack before the PR #610 merge? If not, was a separate Emergency RFC created during the incident?
- **Rootly API** — structured incident roles and team assignments not retrieved directly; roles reconstructed from Slack messages and Jira comments
- **Grafana** — error rates and precise affected environment counts not validated against dashboards; Grafana auth not run in this dry-run. Tenant count (~62) derived from Slack messages
- **Root cause of controller startup failure** — exact reason the new tofu controller failed to start is marked [TODO: validate]; needs confirmation from ICE / RDO
- **Version number collision explanation** — why both versions shared the same identifier is marked [TODO: validate]; needs confirmation from ICE
- **[RDODCP-905](https://outsystemsrd.atlassian.net/browse/RDODCP-905)** — self-heal mechanism ticket not reviewed in this run; referenced via Slack messages only
- **January 2026 OSALL incidents** — [TODO: validate] [RDINC-68859](https://outsystemsrd.atlassian.net/browse/RDINC-68859) cluster (5 incidents, still open) — were action items created and completed before RDINC-78058?

**Estimated completeness:** ~80% — timeline and findings well-sourced; key technical root-cause details and Change Management compliance need engineering team validation.
