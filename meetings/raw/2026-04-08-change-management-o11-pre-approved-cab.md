# Change Management O11 Pre Approved CAB Requests

**Date:** 2026-04-08
**Time:** 11:00-11:30
**Attendees:** Vera Branco, Pedro Neves, Ana Peixoto

## Discussion

**Context:** Transition of request fulfillment and change management between SRE and Global Support (implemented June 2025). GS assumed customer communication for SRE-executed requests and routes non-cataloged requests to CAB team.

**Current State:**
- Service requests logged in Zendesk by GS
- Non pre-approved changes go through Jira approval process
- GS maintains documented change records with linked case numbers
- Pre-approved changes during troubleshooting require Jira logging (per Process Owner requirement)

**Core Problem:**
Windows system updates (11.40/11.40.1) blocked — cannot be marked as standard/pre-approved changes without Jira artifact representation. Manual execution causing significant stack damage to GS team.

**Technical Blocker:**
Rootly-Jira integration not working as expected:
- Cannot close pre-approved tickets immediately after creation
- System cannot distinguish between in-progress implementations
- Original alignment (Miranda + Messias) was based on Rootly auto-creating tickets from Zendesk scope

**Compliance vs Operational Efficiency:**
- Pedro: Needs adequate system of records for RD change process compliance
- Vera: System of record doesn't need to be Jira if it meets all necessary controls — this is organizational choice, not imposed requirement
- Agreement: Current controls in CBO and other systems are audit-compliant
- Issue: Dual logging (Zendesk + Jira) creates unsustainable operational burden for GS

## Key Points

1. **System of Record Alignment Needed:** What is the actual compliance requirement vs organizational preference for Jira?
2. **Pre-approved Change Execution:** Who owns execution during troubleshooting? Support function with engineering involvement for technical decisions, or pure engineering?
3. **Automation Gap:** Manual work is unsustainable — need to automate or eliminate friction
4. **Tooling Misalignment:** Rootly-Jira integration assumptions not holding up in practice

## Decisions

- Vera to align with @Messias Peralta, @Luís Rosa, and @Ricardo Miranda before working session
- Working session next week with Ana, Pedro, and team once alignment is achieved

## Action Items
- [x] Vera - create problem statement for Messias, Luís, Ricardo alignment
- [ ] Vera - schedule alignment meeting with Messias, Luís, Ricardo
- [ ] Schedule working session with Ana, Pedro, team (post-alignment)

## Reference Links
- https://outsystemsrd.atlassian.net/wiki/x/PADTMQE
- https://outsystemsrd.atlassian.net/wiki/spaces/CloudKB/pages/5154799932/Engaging+with+SRE+for+O11

## Initiative Tracking
This work is tracked in ProcessEngineering_Internal workspace:
`ProcessEngineering_Internal/initiatives/active/change-management-gs-sre-transition/_initiative.md`
