# Staff Meeting — 2026-04-16

**Attendees:** Vera, Inês, Laura, Paulo

**⚠️ REMINDER: Check if AI Companion is on to record the call content**

---

## Context Since Last Meeting

**V2MOM (April 10-17):**
- V2MOM refinement continued — execution table drafted with all 28 submethods mapped to Jira epics
- Trusted Partnership value description updated to include customer-centricity (action item from last meeting)
- Removed 101 retrospective files from docs, moved Confluence temp files — housekeeping done
- M3.3 epic corrected from RSA-728 to RSA-728 in execution draft
- Effort estimations still TBD for Methods 1, 3.5, 5, 6
- **Method 1 measurements:** All validated except M1.2a and M1.2b (to discuss this meeting)

**Initiatives:**
- Change Management GS-SRE Transition: Problem statement updated with impact data from Ana Peixoto (15.5h avg CAB approval, 26 RFCs outside catalog). Message to Messias/Miranda/Rosa drafted, pending send.
- Escalation on Engineering Coverage for Support Cases: Meeting with Charola and João Rodrigues held/scheduled — follow-up pending conversation with Charola

**Other:**
- V2MOM definition close to complete — measurements and execution table need final review
- DL from last meeting: team to review measurements by Thursday, formal submission by Friday

---

## Open Action Items (from previous meeting)

- [x] Vera: Update V2MOM — include customer centricity in Values → **done** (Trusted Partnership updated)
- [x] Vera: Restructure V2MOM methods — drop FedRAMP, move AI Transformation to Method 1 → **done**
- [x] Vera: Meeting with António Valiente re: FedRAMP and PE involvement → **done**
- [ ] Team: Review V2MOM measurements and provide feedback — DL Thursday April 16 → **due tomorrow**
- [ ] Vera: Formal V2MOM submission — DL Friday April 17 → **due Friday**
- [x] Paulo: Present draft AI operating model + roadmap of opportunities → **done** — presented on dedicated sync, approach agreed

---

## Carried Forward (not covered last meeting)

### 1. V2MOM Measurements Deep Dive (M2.2, M4.3, M4.4)

DL was set for team review but the three open measurements were not discussed in detail.

**M2.2: Standard Change Promotion Rate (Laura)**
- Metric: % increase in volume of changes transitioned from "Normal" to "Standard" track
- Target: +50% increase by Q2 2027
- Ask: Is this metric feasible to track? Do we have baseline data? Does the target make sense?

**M4.3: Dashboard Adoption Rate (Paulo)**
- Metric: % of target audience actively using dashboards (monthly active users)
- Target: >75% by Q4 2026
- Ask: Do we have dashboard analytics to track this? Is this realistic?

**M4.4: Metric Data Quality Score (Paulo)**
- Metric: % of metrics passing monthly data quality validation checks
- Target: >98% by Q4 2026
- Ask: What role does PE play in metrics governance vs data quality ownership?

### 2. V2MOM Structure Assessment

Methods were restructured (FedRAMP dropped, AI promoted) but the broader question remains: based on the full measurement review, are there gaps in V2MOM coverage? Topics to add, remove, or reorganize?

### 3. Individual V2MOM Derivation — Remaining Items

Vision & Values decided (shared). Still open:
- Methods: How do individual methods relate to team methods? Direct assignments or custom?
- Measures: Individual measures roll up to team measures — how?
- Obstacles: Individual vs team — how much duplication?
- Template or guidance for the team on how to write individual V2MOMs

### ~~4. Scaling R&D Team Engagement with Process Engineering~~ ✅ DONE

Completed: Shared message welcoming Paulo formally to the team, explained front door protocol and areas of expertise of each team member.

### 4. Operating Model for ProcessEngineering_Internal GitHub Repository

**Vera's proposal:**
- All PE work documentation (not personal notes) goes in repo
- Commits: End of milestone or end of day
- PRs: Required for major changes, direct commit for minor updates
- All team members can commit, PR reviews by Vera or designated reviewer

**Outcome needed:**
- [ ] Agreement on content scope and commit/PR workflow
- [ ] Document operating model in repo README

---

## Running Topics

### Internal AI Augmentation Roadmap (M1.2a / M1.2b)

**Context:** M1.2a (AI-Augmented Workflow Documentation) is documented on Confluence and validated by the team as a useful use case. All Method 1 measurements validated except M1.2a and M1.2b — need to finalize these.

**Discussion points:**

1. **Roadmap prioritization:**
   - Top priority candidate: Ops Review — shipping this faster would have immediate impact
   - What other use cases should we prioritize?
   - Brainstorm with team on highest-value AI augmentation opportunities

2. **Time savings expectations (M1.2b):**
   - What time savings do we expect per use case?
   - How do we measure and track these?

3. **M1.2a measurement definition:**
   - What does "documented on Confluence and validated by the team" look like as a measurable target?

4. **Paulo's AI operating model + roadmap** (action item from last meeting)

**Outcome needed:**
- [ ] Validate M1.2a and M1.2b measurements
- [ ] Agreed priority order for AI augmentation use cases
- [ ] Expected time savings targets per use case
- [ ] Confirm Ops Review as top priority

---

## Initiative Updates

| Initiative | Status | Owner |
|------------|--------|-------|
| Problem & Bug Management Governance (M3.4) | In Progress | Inês / Vera |
| Retrospective Transformation (M3.5) | Active | Inês |
| Event Management (M3.6) | Active | TBD |
| Change Management GS/SRE Transition | Active — problem statement updated with impact data | TBD |
| ODC Process Assistant (M5.3) | In Progress | Vera / Paulo |

---

## Meeting Notes

### Topics Discussed

**New Initiatives & Incoming Work**

1. **O11 Swarming between SRE + GS** — One of the outcomes of the GS+R&D workshop. After conversation with Charola, we need to align on the expected role of Process Engineering with O11 processes. Also a topic to discuss with Salman, based on the historical context of this team.

2. **Day-0 Vulnerability Response** — Initiative led by Security Team (potential DRI: Mitch O'Donnell). Goal: faster response, engagement and coordination from the moment a critical vulnerability is detected. Problem statement still to be detailed. Tiago Ribeiro asked PE to work with Security on this, but they will lead the topic. Need an initiative tracker on our side (Jira included).

**Retrospective Transformation (M3.5)**

- Announcing today on Ops Review the change in the retrospective model together with the elimination of the Internal Communication Lead role (outcome of the GS workshop).
- Need to engage fast with Ricardo Silva and Kevin Tek from SRE to plan both rollouts.
- Ultimate goal: have Rootly triggering the retrospective skill on the incident channel. Needs to be checked with Kevin Tek on feasibility.

**Method 4 — Data & Metrics**

- Paulo handed over to Ricardo Almeida (Data Team) any topic related to CPTO V2MOM. No hard changes expected.
- Diogo Bargas (Data Team) is addressing Change Failure Rate changes together with Vitor Rolo (Release Team).

**Method 2 — Change Management (Laura)**

- Laura progressing on the analysis for M2.1. Next steps defined — she will apply the lenses defined in the meeting with Brandão/Tiago Oliveira.
- Will start working with Thiago Campos on the reviewers framework.
- AI Opportunity identified: agent to review changes. Consider rolling out the agent at the same time as the framework to compare results.

**Method 1 — AI Transformation (Paulo)**

- Paulo presented the operating model on the dedicated sync. Team agreed on the approach.
- Next steps (after Paulo returns from vacation): session with key champions to share the initiative and the proposed roadmap, get feedback on other potential opportunities.
- Vera will share the launch message to release the first skill and communicate what we intend to do on this method with broader audience. Validate message with Tiago Oliveira.

**Method 5 — Internal Operating Models (Vera)**

- Vera will work on internal operating models over the next couple of weeks to ensure the team naturally uses koda to feed Confluence and Jira.

### Decisions Made

- Retrospective model change + ICL role elimination to be announced at Ops Review today
- Paulo's AI operating model approach approved by team
- Day-0 vulnerability response: PE will support but Security leads

### Not Covered — Carry Forward

- V2MOM Measurements Deep Dive (M2.2, M4.3, M4.4)
- V2MOM Structure Assessment
- Individual V2MOM Derivation
- Operating Model for ProcessEngineering_Internal repo

### New Action Items

- [ ] Inês: Engage with Ricardo Silva and Kevin Tek (SRE) to plan retrospective transformation + ICL elimination rollout
- [ ] Inês: Check with Kevin Tek on Rootly triggering retrospective skill on incident channel
- [ ] Vera: Create initiative tracker for Day-0 Vulnerability Response (Jira + repo)
- [ ] Vera: Discuss O11 process role with Salman Malik
- [ ] Vera: Share Method 1 launch message (validate with Tiago Oliveira first)
- [ ] Vera: Work on internal operating models for koda → Confluence/Jira (Method 5)
- [ ] Laura: Apply analysis lenses from Brandão/Tiago Oliveira meeting to M2.1
- [ ] Laura: Start working with Thiago Campos on reviewers framework
- [ ] Paulo (after vacation): Session with key champions for AI operating model feedback

