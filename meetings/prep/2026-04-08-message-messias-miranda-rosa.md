# Draft Message: Change Management GS-SRE Alignment

**To:** Messias Peralta, Ricardo Miranda, Luís Rosa
**Date:** 2026-04-08

---

Hi team! :slightly_smiling_face:

Following last week's GS workshop, Ana Peixoto and Pedro Neves raised concerns about the change management and request fulfillment transition between SRE and Global Support. We believe this needs alignment between both teams before we move forward.

**Context:**

Since the June 2025 transition, GS has been managing customer communication for SRE-executed service requests. The current model requires Jira artifact representation for pre-approved changes, which is creating operational friction. Windows system updates (11.40 / 11.40.1) are currently blocked because they cannot be marked as standard/pre-approved changes without this artifact. GS is also expecting an increase in volume, which makes the current manual process unsustainable.

The original plan assumed Rootly-Jira integration would automate ticket creation from Zendesk, but this is not viable — Rootly cannot derive the full context needed from Zendesk tickets.

**Desired state (from GS + Engineering Workshop):**

The workshop reached alignment on Challenge #6: GS should be as autonomous as possible to solve customer problems, catalog items must be fully automated through Cloud Backoffice, and SRE involvement is triggered when GS suspects a cloud change is needed for incident recovery.

**Our position as Process Engineering:**

We need to get records and documentation in the right place to meet compliance requirements, but we cannot promote toil through manual operations like manual artifact logging. The goal is operational efficiency without compromising process control — fully aligned with the desired state from the workshop.

**Next steps:**

This is a preliminary conversation before GS triggers a broader working session with all stakeholders. I'd love to get your thoughts on this before we bring everyone together to align on the path forward.

I've documented the problem statement in Confluence for reference: https://outsystemsrd.atlassian.net/wiki/spaces/EEO/pages/6188138563
