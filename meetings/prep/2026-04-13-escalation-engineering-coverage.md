# Escalation: Engineering Coverage for Support Cases

**Date:** 2026-04-13
**Attendees:** Vera Branco, Pedro Charola Alves, João Rodrigues
**Origin:** GS+R&D Workshop (March 30-31) — unresolved item requiring Engineering Leadership escalation

---

## Context

During the GS+R&D Workshop, Challenge #1 addressed the **Service Incidents vs Support Cases paradigm**. The workshop reached agreement on most operational topics, but two items had no agreement and were flagged for escalation to Engineering Leadership + GS Leadership:

1. **Engineering Coverage for Support Cases** (this meeting)
   - GS requires 24x7 Engineering coverage for high/urgent priority support cases
   - Engineering position: TBD — no agreement reached at workshop

2. **CritSits Engagement and RCA Alignment** (separate session, not in scope today)

---

## The Problem

Support cases and service incidents are conflated in the current escalation model. High-priority support cases (Urgent/High) are automatically routed to SRE via severity mapping (Urgent → SEV1, High → SEV2), regardless of whether the issue has actual system-wide impact. This forces SRE to validate and hand back non-systemic issues.

**GS expectation:** 24x7 engineering involvement on high/urgent support cases
**Current R&D coverage (O11):** 8x5 EMEA, with OLAs for communication frequency
**Current R&D coverage (ODC):** No OLAs defined
**Current GS coverage:** 24x7

---

## Current Engineering Coverage Reality

The actual engineering coverage model is unclear and inconsistent:

- **Some teams have on-call rotations**, but these engineers are usually pulled in by SRE — not directly by GS or through a defined engagement model
- **SRE acts as gatekeeper** — they decide when to involve dev teams. In some cases, SRE does not see value in engaging dev teams after hours, even when the issue is customer-impacting
- **GS is left exposed** — they still need to provide continuous support to customers on high/urgent cases to comply with the public SLA, but have no mechanism to get engineering engagement when SRE decides not to escalate
- **Net effect:** GS carries the SLA compliance burden while Engineering's involvement depends on SRE's judgment call, with no transparency or agreed criteria

---

## OLA Gap

- **O11** has defined OLAs for R&D communication frequency (e.g., every 4 business hours for Urgent, 8x5 EMEA coverage)
- **ODC has no OLAs defined** — no baseline commitment to reference or build on
- Both platforms lack clarity on the actual engagement model between GS → SRE → Dev Teams

---

## Workshop Agreements (for reference)

The workshop did reach agreement on separating the paradigm:
- **Service Incidents** = system-wide impact, SRE-owned, requires swarming
- **Support Cases** = customer-specific, engineering teams investigate, GS owns communication

What was NOT agreed: the level of engineering coverage expected for support cases.

---

## Key Questions for This Meeting

1. **What does GS actually need?** Is it 24x7 engineering resolution, or 24x7 acknowledgment/triage?
2. **What triggers engineering engagement?** All high/urgent cases, or only after GS L3 exhausts investigation?
3. **What is the realistic Engineering position?** Can we commit to anything beyond 8x5?
4. **Is the real gap about coverage hours or about engagement model?** If GS had a clear path to engage engineering effectively during business hours, would the 24x7 ask change?
5. **How does GS track SLA compliance on their side?** We need to understand how engineering's lack of after-hours engagement is concretely impacting SLA compliance — what does GS see in their records when engineering doesn't engage?

---

## PE Position

- The current severity-to-SEV mapping bypasses impact validation — not every urgent support case is a service incident
- A clear separation between service incidents and support cases (workshop agreement) should reduce the volume of false escalations
- O11 has OLAs for communication frequency but ODC has none — the engagement model needs clarity on both platforms
- Expanding to 24x7 engineering coverage for support cases is a significant resource commitment that needs data to justify (how many high/urgent cases arrive outside EMEA business hours? what % actually need engineering involvement?)

---

## Decisions Needed

- [ ] Agree on what "Engineering Coverage" means for support cases (triage vs resolution vs communication)
- [ ] Define the engagement criteria — when does a support case warrant engineering involvement?
- [ ] Position on 24x7 vs 8x5 with clear escalation paths for after-hours
- [ ] Next steps and who owns the proposal to Engineering Leadership

---

## Meeting Notes

- Definir regra que se segue — a regra eventualmente vai falhar mas temos de ter flexibilidade em sede de continuous improvement para rever a consequência de o GS apertar o botão
- A regra não pode ser definida em incident response time
- Rever a heurística que define support cases vs service incidents
- Support cases: definir regra de escalação à engenharia

**Dois passos:**
1. Definição do que vem para a engenharia (service incidents vs support cases)
2. Para onde vem dentro da engenharia (routing)

- Para casos em que não deveria ter sido escalado → tem de haver uma RCA de processo (isto tem de ser flagado nas retrospetivas)
- Definir expectativas do que a engenharia deveria esperar do support (quando escalam)

### Action Items

*Pending — follow-up with Charola needed*
