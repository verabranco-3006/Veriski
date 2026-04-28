# PE Process Ecosystem

*The complete map of processes governed or influenced by Process Engineering, their purpose, status, and how they connect.*

**Last updated:** 2026-04-27

---

## How to Read This Document

Processes are organized by lifecycle stage — the path from detection to customer visibility. Each process includes its purpose, current status, Jira project (where applicable), and connections to other processes.

**Status key:**
- **Governed** — process defined, documented, and actively managed by PE
- **Governance Gap** — process exists but lacks PE governance or consistent standards
- **To Establish** — process does not exist yet; identified as a gap

---

## DETECT

Processes that identify issues before or as they happen.

### Event Management

**Purpose:** Detect anomalies through alerts, SLO breaches, and monitoring signals. Provides the earliest signal that something may be wrong.

**Status:** To Stablish — monitoring owned by SRE and individual teams. PE does not govern event management directly but it feeds into processes we own (Incident Management, Failure Management).

**Jira Project:** N/A (signals come from monitoring tools — Datadog, PagerDuty/Rootly)

**V2MOM:** M3.6 (Event Management) — Not Started, owner TBD

**Connections:**
- **→ Incident Management** — alerts and SLO breaches trigger incidents (RDINC creation)
- **→ Failure Management** — deployment failures detected through monitoring feed into RDODCF

---

### Failure Management

**Purpose:** Track and govern CD pipeline failures and deployment errors. Ensures failed deployments are visible, triaged, and resolved.

**Status:** Governed — process defined, Jira project active (RDODCF)

**Jira Project:** RDODCF (R&D ODC Failures)

**V2MOM:** M3.1 (Failure Management Governance)

**Documentation:** [Failure Management](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/) | `docs/processes/odc/failure-management.md`

**Connections:**
- **→ Incident Management** — failures that impact customers escalate to incidents
- **← Change Management** — failed changes feed back into Failure Management (failed change → RDODCF)

---

## RESPOND

Processes that coordinate the response to active issues.

### Incident Management

**Purpose:** Coordinate response to customer-reported issues, system-wide outages, and manually declared incidents. The central response process — everything flows through here when customers are impacted.

**Status:** Governed — mature process with defined lifecycle, SLAs, and tooling

**Jira Project:** RDINC (R&D Incidents)

**V2MOM:** M3.3 (Triage Models & OLAs)

**Documentation:** [Incident Response Process](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/) | `docs/processes/odc/incident-response-process.md`

**Connections:**
- **← Event Management** — alerts and SLO breaches trigger incidents
- **← Failure Management** — deployment failures that impact customers escalate to incidents
- **→ Retrospectives** — system-wide incidents trigger retrospectives
- **→ Problem Management** — recurring or complex issues result in RPM creation
- **→ Status Page** — system-wide impact triggers customer communication via Status Page
- **↔ Vulnerability Management** — vulnerabilities detected during incident response are reported via RPM flagged as security vulnerability; day-0 vulnerabilities may trigger incident response

---

## PROTECT

Processes that identify, classify, and coordinate response to security threats.

### Vulnerability Management

**Purpose:** Identify, classify, and track security vulnerabilities from detection through remediation and release. Operates through a dual-project model: RPM (tracks the fix) and VUL (tracks exploitation risk). PSIRT manages classification; R&D teams own remediation.

**Status:** Governance Gap — process defined with automation (RPM → VUL auto-creation). Adoption gaps similar to Problem Management (teams bypassing the flow).

**Jira Projects:** RPM (R&D Problem Management, flagged as Security Vulnerability) + VUL (Vulnerability Management)

**Current flow:**
1. **Identification** — RPM created (by R&D, customer via Zendesk, or Security team), marked "Is it a Security Vulnerability? = Yes" → VUL auto-created in PSIRT board
2. **Classification** — PSIRT validates and classifies severity. High/Critical → Priority set to Urgent. Team assignment via PACA
3. **Remediation** — Risk assessment + plan & fix (owned by assigned R&D team)
4. **Release** — Fix release + security bulletin

**Detection sources:**
- R&D (during development, testing, or incident response)
- Customers/Partners (via Global Support → Zendesk → RPM)
- Security Team / PSIRT (scans, external advisories)

**Documentation:** [How to deal with Security Vulnerabilities](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/5036639693) | [Streamline Vulnerability Management](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/5036840855)

**Connections:**
- **→ Problem Management** — RPM is the shared artifact; vulnerability fixes tracked through RPM lifecycle
- **→ Incident Management** — vulnerabilities detected during incidents are linked (RDINC ↔ RPM)
- **→ Release Notes** — security bulletins published when fix reaches GA
- **→ Emergency Vulnerability Process** — day-0 conditions activate the emergency overlay
- **← Incident Management** — vulnerabilities discovered during incident response feed back into VUL flow

---

### Emergency Vulnerability Process

**Purpose:** The emergency overlay for when a day-0 vulnerability is detected and the regular VUL flow (weekly PSIRT triage, queue-based assignment) is too slow. Defines triggers, immediate engagement model, containment before fix, and coordination across Security and Engineering.

**Status:** To Establish — PE deliverable under the AI-Accelerated Vulnerability Identification and Response initiative (Stream 1c)

**Jira Epic:** [RSA-916](https://outsystemsrd.atlassian.net/browse/RSA-916)

**V2MOM:** Out of V2MOM scope

**Gaps this process addresses:**
| Gap | Current State | Day-0 Need |
|-----|--------------|------------|
| Triage cadence | PSIRT weekly meeting | Immediate activation |
| No declaration step | Everything enters the same flow | Explicit "emergency, activate now" trigger |
| No swarming / tiger team | RPM enters team backlog | Dedicated, immediate engagement |
| No containment phase | Classification → remediation | Immediate mitigation before fix exists |
| No time-to-contain SLAs | Only fix timelines | OLAs for detection → containment |
| No active exploitation protocol | Not defined | Coordinated cross-functional response |

**Connections:**
- **← Vulnerability Management** — day-0 conditions trigger this process as an escalation from the regular VUL flow
- **→ Incident Management** — day-0 may trigger formal incident response if customer impact is detected
- **→ Change Management** — emergency containment changes (hotfixes, mitigations) follow Emergency Change path
- **→ Problem Management** — once contained, the fix is tracked through the regular RPM lifecycle

---

## LEARN

Processes that extract insights from incidents and drive improvement.

### Retrospectives

**Purpose:** Conduct root cause analysis after system-wide incidents. Produce findings and action plans to prevent recurrence.

**Status:** Governed — process defined, undergoing transformation (M3.5). Current focus: ownership model (faulty asset owner), OLA targets (outcomes over outputs), recurrence measurement, automation.

**Jira Project:** Linked to RDINC (retrospective artifacts attached to incident records)

**V2MOM:** M3.5 (Retrospective Transformation) — Active

**Documentation:** [Retrospective Process](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/) | `docs/processes/odc/retrospective-process.md`

**Connections:**
- **← Incident Management** — system-wide incidents trigger retrospectives
- **→ Improvement Management** — action items and findings feed into improvement tracking
- **→ Problem Management** — retrospective findings may identify new problems requiring RPM creation

---

### Improvement Management

**Purpose:** Track action items from retrospectives and other sources through to completion. Ensure accountability for continuous improvement — findings don't just get documented, they get fixed.

**Status:** To Establish — no governed process exists. Action items from retrospectives currently have no accountability mechanism.

**V2MOM:** Not explicitly scoped (gap identified in process lifecycle analysis)

**Connections:**
- **← Retrospectives** — action items and findings feed in
- **→ Problem Management** — process improvements that address recurring problems
- **→ Bug Management** — bugs identified through retrospective findings
- **→ Change Management** — process changes and improvements requiring formal change

---

## FIX

Processes that investigate root causes and govern the fix lifecycle.

### Problem Management

**Purpose:** Investigate recurring or complex issues, document known errors and workarounds, and provide customer visibility into issue resolution. The central governance layer that connects incidents to fixes to customer communication.

**Status:** Governance Gap — process designed and documented. ODC is in Stage 1 with critical adoption gaps. O11 has a mature, customer-facing model since 2021.

**Jira Project:** RPM (R&D Problem Management)

**V2MOM:** M3.4 (Problem Management) — In Progress

**Documentation:** [Problem Management](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/5036841027) | [ODC Problem Management](https://outsystemsrd.atlassian.net/wiki/spaces/EEO/pages/4408049977) | [Implementing Problem Management](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/)

**Current state (ODC Stage 1 vs O11 mature):**

| Capability | O11 (mature) | ODC Stage 1 (current) | ODC Stage 2 (planned) |
|---|---|---|---|
| Customer-facing fields | Description, Workaround, How to confirm, Status | Release Notes only | Full customer-facing fields |
| Customer status tracking | Problem Tracking Page on Support Portal | Not available | Planned |
| Email notifications on transitions | Yes (Release Planned, Closed) | No | Planned |
| KPIs with targets | Defined (Urgent: 2w WA, 3m release) | Collect data only, no targets | Define targets |
| Bug lifecycle governance | Implicit through RPM mandatory fields | None | Not scoped |


**Adoption gaps:**
- Many incidents closed without RPM creation
- Bugs created in isolation, no RPM linkage
- Developers don't include RPM ID in commits → Release Notes not published
- Workarounds shared ad-hoc, not centralized in RPMs

**Connections:**
- **← Incident Management** — recurring/complex issues result in RPM creation
- **← Improvement Management** — process improvements feed into Problem Management
- **← Vulnerability Management** — RPM is the shared artifact for vulnerability fixes (flagged as Security Vulnerability)
- **→ Bug Management** — investigation identifies bugs; bugs created as child tasks under RPMs
- **→ Problem Portal** — known errors and workarounds published for customer visibility
- **→ Release Notes** — RPM ID in commits triggers automatic release note publication

---

### Bug Management

**Purpose:** Govern the bug lifecycle from creation through triage, prioritization, fix, verification, and release. Ensure bugs are tracked centrally with consistent measurements and accountability.

**Status:** Governance Gap — bugs currently managed ad-hoc across individual team projects with no standard process, no consistent measurements, and poor visibility into the overall bug landscape.

**V2MOM:** Not explicitly scoped (identified as a gap during Vijay alignment, April 10)

**Governance model (proposed on April 10 with Vijay, Arul, Brandão, not yet accepted):**
- **Central governance owned by Quality (Vijay)** — defines bug lifecycle standards, measurements, triage criteria, accountability model
- **Central project and workflow** — bugs tracked in a centralized project (like RDINC), not scattered across team projects. Scalability: one workflow to evolve, not N team-specific workflows.
- **Teams execute within the central framework** — development teams own the fix, but the bug record lives in the governed project
- **Mandatory linkage to Problem Management** — bugs always traceable to an RPM

**Measurements to track centrally:** open bug count, average time to fix, customer-impacting bugs without release notes, bug escape rate

**Toyota escalation as proof point:** 4 tickets where fixes were made but customers had no visibility because bugs were treated as internal items disconnected from Problem Records. Toyota reports to their Board — this is customer trust.

**Connections:**
- **← Problem Management** — investigation identifies bugs; bugs linked as child tasks under RPMs
- **← Improvement Management** — bugs identified through retrospective findings
- **→ Release Management** — fix ready for deployment enters change lifecycle

---

## DELIVER

Processes that govern how fixes and changes reach production and customers.

### Change Management

**Purpose:** Govern all manual changes to production environments through a structured lifecycle — RFCs, CAB approval, Standard/Normal/Emergency change types. Ensures changes are assessed for risk, approved appropriately, and traceable.

**Status:** Governed — mature process with defined lifecycle, CAB cadence, and change catalog. Undergoing transformation (V2MOM M2).

**Jira Project:** RFC (R&D ODC RFCs) and O11-RFC (R&D O11 RFCs)

**V2MOM:** M2 (Transform Change Management) — Laura owns

**Documentation:** [Change Management Process](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/) | `docs/processes/odc/change-management-process.md`

**Connections:**
- **← Emergency Vulnerability Process and Incident Management** — emergency containment changes follow Emergency Change path
- **← Improvement Management** — process changes and improvements requiring formal change


---

### Release Notes

**Purpose:** Customer-facing documentation of changes, fixes, and improvements deployed to production.

**Status:** Governance Gap — release notes exist but lack consistent governance. Some release notes posted on individual Jira items instead of the public Problem Record artifact. No enforced standard for when and how release notes are published.

**Connections:**
- **← Problem Management** — RPM ID in commits triggers automatic release note publication
- **← Vulnerability Management** — security bulletins published when vulnerability fix reaches GA
- **→ Problem Portal** — published release notes visible to customers through Problem Portal

---

## CUSTOMER VISIBILITY

Processes that provide customers with visibility into issues, fixes, and system status.

### Problem Portal

**Purpose:** Customer-facing view of known issues, workarounds, fix status, and resolution. Deflects repeat tickets by enabling self-service troubleshooting.

**Status:** Governed in O11 (Problem Tracking Page on Support Portal since 2021). Not yet available in ODC (Stage 2 planned).

**Connections:**
- **← Problem Management** — known errors and workarounds populate the portal
- **← Release Notes** — fix documentation visible through the portal
- **→ Incident Management** — deflects repeat tickets (feedback loop: fewer duplicate incidents)

---

### Status Page

**Purpose:** Real-time communication of system-wide impact to customers and internal stakeholders during active incidents.

**Status:** Governed — Internal Status Page operational, Public Status Page in place

**V2MOM:** M3.2 (Status Page Governance)

**Connections:**
- **← Incident Management** — system-wide impact triggers Status Page updates

---


```

---

## Source Materials

| Source | Date | Context |
|--------|------|---------|
| Process Lifecycle diagram | 2026-04-10 | `meetings/prep/2026-04-10-process-lifecycle.drawio` |
| Problem & Bug Management prep (Vijay meeting) | 2026-04-10 | `meetings/prep/2026-04-10-problem-bug-management-odc.md` |
| Bug governance clarification message | 2026-04-14 | `meetings/drafts/2026-04-14-message-vijay-bug-governance-correction.md` |
| Problem Management narrative message | 2026-04-14 | `meetings/drafts/2026-04-14-message-vijay-problem-management.md` |
| Vulnerability Management docs | Synced 2026-04-09 | `docs/processes/odc/how-to-deal-with-security-vulnerabilities.md` |
| Streamline Vulnerability Management | Synced 2026-04-09 | `docs/processes/odc/streamline-vulnerability-management.md` |
| Day-0 Vulnerability initiative | 2026-04-27 | `initiatives/active/day0_vulnerability/_initiative.md` |

---

*This is a living document. Update when processes are established, governance changes, or new interconnections are identified.*
