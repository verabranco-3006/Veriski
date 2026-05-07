# O11RDINC — Project Configurations

**Date:** 2026-05-07
**Time:** 15:00–15:30
**Attendees:** Vera Branco, Luís Rosa

## Status

- Jira project created
- Connection with Rootly granted
- Rootly workflows still to configure (e.g., Sev1 created → trigger Rootly behavior)
- Severity mechanism: align with ODC (same model)

## Baseline Fields for GS → R&D Escalation (per Rosa)

- Activation Code
- Environment

> Open: who defines the full field set required to escalate from GS to R&D? Baseline above is a starting point, not the final list.

## Swarming Mechanism — Initial Ideas

- Escalation automatically triggers a Slack channel and/or Zoom call link to start swarming
- Severity logic mirrors ODC

## Open Questions / Dependencies

- **Messias Peralta + Tiago Garcia** — blocked on both for clarity across Rootly workflow rules, implementation/test ownership, and the broader escalation flow. No distinction of who owns what; the work moves once the pair unblocks.
- **Field definition owner** — who is responsible for the GS → R&D escalation field set in Jira? Baseline (Activation Code, Environment) is a starting point, not the final list.

## Action Items

- [ ] Vera — follow up with Messias Peralta and Tiago Garcia to unblock Rootly rules + escalation flow
- [ ] Vera — clarify ownership for the Jira field definition (GS → R&D escalation)

## Initiative Tracking

This work is tracked in ProcessEngineering_Internal workspace:
`ProcessEngineering_Internal/initiatives/active/ir-comms-gs-sre-transition/_initiative.md`
