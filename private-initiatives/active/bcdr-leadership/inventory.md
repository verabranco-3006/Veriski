# Product BCDR Current State Inventory
*Working document — homework with Paulo Garcia + Pedro Charola Alves*

**Scope:** Product BCDR only — continuity and recovery for the platforms (ODC + O11). Company-wide BCDR (corporate IT, office, HR) is explicitly **out of scope** and not part of this inventory.

**Purpose:** Capture what Product BCDR-related artifacts, practices, and ownership exist today across ODC and O11. Don't try to define what BCDR *should* be — just inventory what *is*. Gaps and ambitions come after.

**How to use this:** Walk through each section in the homework session. Fill what we know, mark what we don't. Anything we cannot answer between Vera + Paulo + Charola is a stakeholder question for later.

---

## 0. Anchor documents (known)

**BCDR Strategy (SOC 2 attestation):**
- [BCDR Strategy doc (Google Docs)](https://docs.google.com/document/d/1jFwjQU_AEhOAtSyqkNp3ezJ3PJxl7rzOkDd57CmtcgY/edit?tab=t.0#heading=h.gjdgxs)
- Authored at time of SOC 2 attestation
- **Status: needs review.** Not just "is it current" — known to require a refresh. This is now a concrete deliverable of this initiative, not just background reading.
- **Action:** read end-to-end, extract RTO/RPO targets, scope, and assumptions into this inventory. Flag what's stale, what's missing, what's still valid. Cross-check against the public SLA commitments (Section 1).

**Public customer commitments (SLA page):**
- [OutSystems SLA page](https://www.outsystems.com/legal/success/support-terms-and-service-level-agreements-sla-of-the-outsystems-software/) — last updated 2025-06-30
- Defines RTO/RPO and uptime by product (O11 Cloud, ODC Platform, ODC Launch) and tier (8x5, 24x7 no HA, 24x7 with HA)
- Force majeure carve-out: multi-AZ failure is out of contractual scope
- See Section 1 for full breakdown

**Drill retrospectives (3 from last year):**
| # | Drill | Cloud | Link |
|---|-------|-------|------|
| 1 | Tenant deletion recovery — soft delete | ODC | [Retrospective](https://outsystemsrd.atlassian.net/wiki/x/VYArOwE) |
| 2 | Tenant deletion recovery — hard delete | ODC | [Retrospective](https://outsystemsrd.atlassian.net/wiki/spaces/RDTF/pages/5518721025/Tenant+Deletion+Recovery+-+Hard+Delete+-+Retrospective) |
| 3 | Database deletion restore | O11 | [Retrospective](https://outsystemsrd.atlassian.net/wiki/spaces/RDTF/pages/5952340149/Restore+Database+delete+-+Retrospective) |

**Action:** pull findings and unaddressed action items from all three retros — these are the most recent empirical evidence of our BCDR posture.

---

## 1. Recovery objectives (RTO / RPO)

**Public commitments to customers** — published in the [OutSystems SLA page](https://www.outsystems.com/legal/success/support-terms-and-service-level-agreements-sla-of-the-outsystems-software/) (last updated 2025-06-30):

### Uptime SLAs (monthly)

| Product | Tier | Monthly uptime |
|---------|------|----------------|
| O11 Cloud | 8x5 (included) | 99.50% |
| O11 Cloud | Extended/Premium 24x7, no HA | 99.95% |
| O11 Cloud | Extended/Premium 24x7, with HA | 99.90% |
| Developer Cloud (ODC) Launch Edition | 8x5 | 99.90% |
| Developer Cloud (ODC) Launch Edition | Extended/Premium 24x7, no HA | 99.95% |
| Developer Cloud (ODC) Launch Edition | Extended/Premium 24x7, with HA | 99.90% |

### RTO / RPO commitments

| Product | Tier | RTO | RPO |
|---------|------|-----|-----|
| O11 Cloud | 8x5 | 24 h | 24 h |
| O11 Cloud | Ext./Premium 24x7, no HA | 12 h | 24 h |
| O11 Cloud | Ext./Premium 24x7, with HA | **15 min** | **1 min** |
| ODC Platform Edition | 8x5 | 30 min | 15 min |
| ODC Platform Edition | Ext./Premium 24x7, no HA | 12 h | 24 h |
| ODC Platform Edition | Ext./Premium 24x7, with HA | **15 min** | **1 min** |

**RTO definition (per the page):** *"The maximum possible interval of time between the moment of a disaster and the moment where the system is back up."*

**Force majeure carve-out (verbatim):** *"The OutSystems platform system design is not prepared to recover from a failure of multiple availability zones and therefore such events are considered force majeure."* — multi-AZ failure is **explicitly out of contractual scope.**

### Service credits

- 10% credit: uptime 99.0-99.49% (8x5) or 99.5-99.94% (Ext./Premium without HA)
- 25% credit: uptime <99.0%
- Claim window: customer must request within **30 days** of month end

### Planned maintenance

- ≥2 business days advance notice
- O11 Cloud: maintenance can be rescheduled at customer request
- ODC: continuous "Evergreen" updates, designed for zero downtime

---

### Implications for BCDR strategy

1. **RTO/RPO is contractual, not aspirational.** The strategy refresh must align to these public commitments (or escalate explicitly if it cannot).
2. **HA-tier commitments are aggressive:** 15 min RTO / 1 min RPO. Drills must validate we can actually hit these — none of the 3 drills last year measured against this bar.
3. **ODC base tier (8x5) is tighter than O11 base tier:** 30 min vs 24 h RTO. This is a divergence we should understand — by design or accident?
4. **Multi-AZ failure is the explicit boundary.** Anything beyond single-AZ is force majeure today. Worth questioning whether that boundary is still the right one, or whether the next strategy refresh should expand.
5. **Service credits are cheap insurance for OutSystems.** The financial pressure for BCDR investment doesn't come from credits — it comes from churn and reputation. Frame the strategy refresh accordingly.

### Questions

- Does the SOC 2 BCDR strategy doc reflect these published commitments, or are they out of sync?
- Have any of the 3 drills measured against the 15-min RTO / 1-min RPO bar?
- Customers on the HA tier — how many, what's the volume, what's the operational stake?
- Force majeure carve-out: when was that boundary set, is it still defensible?

---

## 2. Backup capabilities

*What we back up, how, and how recovery has been validated.*

**Found in PE docs:**
- `docs/processes/odc/normal-initial-rollout-of-s3-backups-for-odc.md`
- `docs/processes/odc/normal-enabling-s3-backups-in-odc-by-aws-backup-policy.md`
- `docs/processes/odc/normal-expand-scope-of-aws-backup-policy-for-s3-backups-to-all-aws-accounts-in-production-rings.md`
- `docs/processes/odc/normal-extending-s3-backups-to-odc-forge.md`

These are change records, not a backup strategy doc. Strategy likely lives elsewhere (Confluence, Cloud team docs).

| Layer | What is backed up | Frequency | Retention | Tested? | Owner |
|-------|-------------------|-----------|-----------|---------|-------|
| RDS | | | | | |
| S3 | | | | | |
| Tenant data | | | | | |
| Configuration / IaC | | | | | |
| Secrets / KMS | | | | | |
| Code / artifacts | | | | | |

**Questions:**
- Where is the canonical backup strategy document?
- What's the difference between ODC and O11 backup posture?
- Last successful restore test — when, what scope?

---

## 3. Recovery runbooks

*Documented playbooks for specific failure modes.*

**Known (from prior PE work):**
- Hard delete recovery plan — referenced in the permanent tenant deletion drill (Dec 2025)
- *Add others as we find them*

| Failure mode | Runbook location | Last reviewed | Last exercised | Owner |
|--------------|------------------|---------------|----------------|-------|
| Permanent tenant deletion (hard delete) | | | Dec 2025 (drill) | |
| RDS data corruption | | | | |
| Region failure | | | | |
| Account compromise | | | | |
| Mass S3 data loss | | | | |
| KMS key loss | | | | |
| Identity provider outage | | | | |
| | | | | |

**Questions:**
- Is there a master list of recovery runbooks anywhere?
- Which failure modes have NO runbook today?

---

## 4. DR exercises and drills

*What's been tested in the last 12-24 months.*

**Known (3 drills run last year — links in Section 0):**

| Exercise | Date | Scope | Cloud | Outcome | Findings | Action plan status |
|----------|------|-------|-------|---------|----------|-------------------|
| Tenant deletion recovery — soft delete | 2025 | Tenant data recovery | ODC | | | |
| Tenant deletion recovery — hard delete | Dec 2025 | Tenant data recovery (post-Viamanta) | ODC | | | |
| Database deletion restore | 2025 | Database recovery | O11 | | | |

**Coverage observation:** 2 of 3 drills were ODC, 1 was O11. Both clouds are exercised — but only on data-loss scenarios. Other failure modes (region failure, identity outage, KMS loss, mass S3 loss, account compromise) appear untested.

**Questions:**
- Is there a DR exercise calendar or just ad-hoc?
- Who owns scheduling — Stability Task Force? Cloud teams? PE?
- Action items from the 3 retros — are they closed, in flight, or stalled?
- What's the cadence target going forward (annual, biannual, quarterly)?

---

## 5. Incident response coverage

*BCDR overlap with incident response.*

**Found in PE docs:**
- `docs/processes/odc/incident-response-process.md`
- `docs/processes/odc/scenario-1-incident-without-system-wide-impact.md`
- `docs/processes/odc/scenario-2-incident-with-system-wide-impact.md`
- O11 ODC Escalation Bridge (`special-procedure-o11-odc-escalation-bridge.md`)

**Coverage check:**
- Does the IR process explicitly trigger BCDR procedures for tier-1 events?
- Is there a defined "this is a continuity event, not just an incident" threshold?
- Who declares a BCDR event vs. a regular SEV-1?

---

## 6. Communication and status

*Customer-facing and internal communication during continuity events.*

**Found in PE docs:**
- Status page governance (M3.2 — currently in design)
- `docs/processes/odc/notify-internal-communications-leader-upon-incident-declaration.md`
- `docs/processes/odc/action-guide-for-internal-communications-leader.md`

**Questions:**
- Does the status page strategy account for region-wide or platform-wide loss?
- Internal comms playbook for prolonged outage?

---

## 7. Compliance touchpoints

*Where BCDR shows up in audits.*

| Standard | Control area | Evidence we provide today | Owner |
|----------|--------------|---------------------------|-------|
| SOC 2 | Availability / continuity | | |
| ISO 27001 | A.17 Business continuity | | |
| PCI | | | |
| HIPAA | | | |

**Questions:**
- What BCDR evidence has been requested in past audits?
- Where did we struggle to produce it?
- Casey Greenstreet / TJ Moore — any open BCDR-flavored asks?

---

## 8. Ownership today (informal map)

*Who actually does BCDR work today, even without the title.*

| Area | Who runs it today | ODC | O11 |
|------|-------------------|-----|-----|
| Backup operations | | | |
| Recovery runbooks | | | |
| Drill execution | | | |
| Customer continuity commitments | | | |
| Compliance evidence | | | |
| Cross-cloud coordination | | | |

---

## 9. Tooling

*What tools support BCDR today.*

| Capability | Tool | Coverage gap |
|------------|------|--------------|
| Backup orchestration | AWS Backup (ODC, partial) | |
| Recovery automation | | |
| Runbook automation | | |
| DR test orchestration | | |
| Status page | | |

---

## 10. Cross-cloud divergence

*Where ODC and O11 differ — to flag for stakeholder discussion later, not to resolve here.*

| Dimension | ODC posture | O11 posture | Impact of divergence |
|-----------|-------------|-------------|---------------------|
| Cloud architecture | Multi-tenant SaaS | | |
| Backup approach | | | |
| Customer commitments | | | |
| Maturity of runbooks | | | |

---

## 11. Initial gaps (running list)

*Capture as we go. These become input to the one-pager.*

- BCDR strategy exists but lives in a SOC 2-era Google Doc — not discoverable as part of the PE process catalog. **Known:** needs review. Refresh is in scope for this initiative.
- Drill coverage is data-loss-only (3 drills, all about tenant/database deletion). No drills for region failure, identity outage, KMS loss, or account compromise.
- No published DR exercise calendar — drills appear ad-hoc rather than scheduled.
- Backup change records exist in PE catalog, but no consolidated backup *strategy* doc in PE space.
- Status of action items from the 3 drill retros is unclear.
- *Add as we find them*

---

## 12. What we need from stakeholders later

*Questions we cannot answer between Vera + Paulo + Charola — defer to the right owner.*

- *Add as we go*

---

## Session log

### Pre-session reading (before homework with Paulo + Charola)
- [ ] BCDR Strategy doc (SOC 2) — extract RTO/RPO targets, scope, assumptions
- [ ] Drill 1 retro — soft delete (ODC)
- [ ] Drill 2 retro — hard delete (ODC)
- [ ] Drill 3 retro — DB deletion restore (O11)
- [ ] Status of action items from each retro

### Session 1 — TBD (Vera + Paulo Garcia + Pedro Charola Alves)
- Agenda: walk this inventory top to bottom, fill what we can, mark what we cannot
- Output: gap list + stakeholder questions + draft positioning for one-pager

---

*Last updated: 2026-05-06*
