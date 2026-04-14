# Message: Change Management GS-SRE Alignment

**To:** Messias Peralta, Ricardo Miranda, Luís Rosa
**Date:** 2026-04-13
**Channel:** Slack DM / Group message

---

Hi team! :slightly_smiling_face:

Following the GS+R&D Workshop (March 30-31), Ana Peixoto and Pedro Neves raised concerns about the change management and request fulfillment transition between SRE and Global Support. I believe this needs alignment between us before we move forward with GS.

**Context:**

Since the June 2025 transition, GS has been managing customer communication for SRE-executed service requests. The current model requires Jira artifact representation for pre-approved changes, which is creating operational friction. Windows system updates (11.40 / 11.40.1) are currently blocked because they cannot be marked as standard/pre-approved changes without this artifact.

The original plan assumed Rootly-Jira integration would automate ticket creation from Zendesk, but this is not viable — Rootly cannot derive the full context needed from Zendesk tickets.

**Impact data from Ana Peixoto (across 26 RFCs):**

- **~15.5 hours average CAB approval time** — significant delay before GS can proceed with execution, some requests extend well beyond this
- **All 26 changes were logged outside the catalog** — agents are not following any defined work instructions
- **Execution friction:** GS agents must create a Jira ticket → place Zendesk on hold → wait 15+ hours for approval → resume and execute. This context switching prolongs resolution time
- **Scale concern:** With increasing volume, this approval delay combined with forced Jira logging impacts execution throughput and system update timeliness
- **Broader scope:** This also impacts other changes not yet updated to "Pre-Approved", such as "End Environment" and "End Infrastructure" operations

**Our position as Process Engineering:**

We need to get records and documentation in the right place to meet compliance requirements, but we cannot promote toil through manual operations like manual artifact logging. The goal is operational efficiency without compromising process control — fully aligned with the desired state from the workshop (GS autonomy, catalog automation through Cloud Backoffice, SRE involvement only when cloud changes are needed for incident recovery).

**What we need to align on:**

1. System of record — does it need to be Jira, or can Zendesk meet the compliance requirements?
2. Pre-approved change execution model — who owns what during troubleshooting?
3. Tooling — Rootly-Jira integration isn't delivering. Do we fix it, adjust the process, or revisit the Jira artifact requirement?

I've documented the full problem statement in Confluence: https://outsystemsrd.atlassian.net/wiki/spaces/EEO/pages/6188138563

Can we find 30 minutes this week to align? I'd love to get your thoughts before GS triggers the broader working session with all stakeholders.
