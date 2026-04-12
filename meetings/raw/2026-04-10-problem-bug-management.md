# Problem & Bug Management Alignment — Friday, April 10, 2026

**Time:** 16:30–17:00
**Attendees:** Arul (Arulraja), Vijay, João Brandão, Inês, Vera

---

## Key Discussion Points

### Toyota Escalation & Problem Tracking Workflow
- Toyota escalation: bugs fixed but no visibility on progress or release notes
- Current workflow: support cases resolved with immediate mitigation, separate Problem Record tracks permanent fix and progress
- This workflow works in O11 but is **not being followed structurally in ODC**
- Release notes sometimes posted on individual Jira items instead of the public Problem Record artifact

### Incident Tracking & Governance Gaps
- Problem Management as a **deflection mechanism** for Global Support — helps prioritize, provides workarounds without escalating everything to engineering
- O11 allocates sprint capacity for problem management
- No explicit error budget policy (Arul mentioned this concept)
- Need to better connect bug tracking within the process ecosystem
- Problem Management as a **customer satisfaction mechanism** — referenced V2MOM M7.4

### Process Ecosystem Presentation
- Vera presented the PE process ecosystem: detection, event management, incident response, learning, fix, deliver, customer visibility
- Focus on connecting bug management and customer visibility within the ecosystem
- Brandão confirmed awareness of the process — aligning with Global Support and SRE teams
- Concern about clarifying where bug fixing fits within the ecosystem
- Need to guide teams on the complete process flow
- Some components (event management) are planned for future development — not yet defined

### Problem & Bug Management Implementation — Decisions
- **Bug Management as a central practice owned by Quality** — Vijay's domain
- Proper definitions and controls for tracking issues across all environments (not just production)
- Brandão highlighted Toyota's specific concern: missing release notes, no visibility on bug resolutions
- Problem Management identifies trends and patterns; **bug tracking stays with individual teams**
- Problem Management provides the governance and visibility layer over the bugs

---

## Agreed Next Steps

- [ ] Follow-up sessions to align on the narrative and operating model for problem management
- [ ] Vera to share documentation with Vijay
- [ ] Vera to connect Vijay with Inês Matos (current process owner) — note: meeting notes reference Henrique Fonseca, clarify current ownership
- [ ] Brandão to involve Francisco to address the customer enablement issue (Toyota)
- [ ] Define where bug management sits within the process ecosystem (Quality-owned, Problem Management-governed)

---

*Meeting date: Friday, April 10, 2026*
