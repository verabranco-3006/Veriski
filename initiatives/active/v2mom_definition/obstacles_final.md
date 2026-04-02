# V2MOM Obstacles - Final

**Date:** 2026-04-02
**Purpose:** Define key obstacles/barriers to achieving V2MOM Vision through Methods

---

## Obstacle 1: Regulatory Deadlines & Capacity Constraints

**Description:** FedRAMP deadlines create non-negotiable capacity surges during Q2 2026, consuming substantial design and documentation effort. Simultaneously, transformation work (M1-M5) requires sustained 70% capacity allocation while operational tasks (M6) have unpredictable surges from audit season, CritSits, and urgent support. This dual pressure risks either operational degradation or transformation stagnation.

**Impact:**
- M1 (FedRAMP): Risk of delays in 3PAO readiness
- M6 (Sustainability): Q2 operational capacity spikes to 40%+ vs 30% target
- M1-M5: Transformation milestones delayed due to operational firefighting
- Team burnout from sustained high-intensity work
- Quality degradation in either operations or transformation

**Mitigation:**
- M6.1: Quarterly capacity tracking with course correction
- Explicit capacity targets: 30% operational, 70% transformation
- Clear prioritization: M1 takes precedence in Q2 2026
- Protect transformation time: dedicated focus blocks, say "no" to non-essential operational asks
- Self-service documentation (M6.3) to reduce ad-hoc consultation burden
- Automation (M5.3) to reduce M6 operational load over time

**Method alignment:** M1, M6, M2-M5

---

## Obstacle 2: AI Skill Gap & Platform Maturity

**Description:** Transitioning to "AI-First" and "Process as Code" (Method 5) requires the team to rapidly master AI @ Product platform, AI tool usage, and automation design while maintaining current operations—creating a steep learning curve with no formal training program. Compounding this challenge, the AI @ Product platform and Process as Code capabilities are emerging/immature, with platform limitations, lack of documentation, or technical issues potentially delaying industrialization work.

**Impact:**
- M5.1 (AI Enablement): Risk of slow adoption or superficial AI usage
- M5.3 (Process Industrialization): Pilot skill deployment may miss Q1 2027 target
- M5.3d (Technical Capability): Team certification blocked by platform immaturity
- M5.3c (Backlog Readiness): Blueprints may not translate if platform constraints unknown
- M2 (Change): Automation discovery relies on AI capability
- Team burnout from learning + operating simultaneously
- Wasted effort if platform architecture changes mid-flight

**Mitigation:**
- Budget 30-35% capacity for M5 (AI enablement, learning time, experimentation)
- Start with narrow pilot scope (M5.3b) to test platform early and build confidence
- Weekly AI experimentation sessions (M5.1) for peer learning
- Accept "good enough" v1.0 for pilot skill
- Close collaboration with AI @ Product team
- Accept platform limitations: work within constraints, don't wait for perfection
- Document platform gaps for future advocacy
- Budget contingency: if platform not ready, defer M5.3 to next V2MOM cycle

**Method alignment:** M5, M2

---

## Obstacle 3: Data Quality & Trust in Automated Governance

**Description:** Shifting from human reviews to AI-driven, system-enforced logic (Methods 2, 3, 5) requires absolute stakeholder confidence in technical data and automation. Fragmented data entry across Jira projects and lack of automated links between logs and version control risk diluting CPTO Metric accuracy (Method 4). If stakeholders don't trust metrics or automation produces incorrect results, data-driven decision-making fails and teams regress to manual approvals—negating velocity and scalability gains.

**Impact:**
- M4 (Metrics): Risk of low adoption or stakeholder skepticism
- M2 (Change): Reviewer empowerment and CFR correlation may face resistance or accuracy issues
- M3 (Incident): Triage automation and alert validation may be second-guessed
- M5.3 (Process Industrialization): Engineering teams may not adopt PE Skills
- M6 (Capacity): Story point tracking unreliable if data inconsistent
- Executive decisions based on flawed data = credibility crisis
- Credibility risk if automation produces incorrect results

**Mitigation:**
- M4.2: Robust data models and validation logic
- M4.3: Metric lineage documentation for transparency
- M4.1: Stakeholder sign-off on metric definitions
- Baseline validation period (Q1 2026) before reporting
- Monthly data quality reviews
- Validate automation accuracy before full deployment (pilot skills, CFR correlation testing)
- Gradual rollout with human oversight initially
- Communication: position as "augmentation" not "replacement"
- Build trust through M4 (metrics literacy, self-service governance)

**Method alignment:** M4, M2, M3, M5, M6

---

## Obstacle 4: Cross-Organizational Dependencies & Alignment

**Description:** Success depends on collaboration with teams beyond Process Engineering (GS, SRE, Engineering teams, AI @ Product platform team). Misalignment, competing priorities, or delays from dependencies can block progress. Workshop findings already documented GS/Engineering alignment challenges, confirming this as a known risk area.

**Impact:**
- M1 (FedRAMP): Requires GS and SRE collaboration for operational model
- M3 (Incident): Retrospective transformation needs SRE and Value Stream Leader buy-in
- M5.3 (Process Industrialization): Depends on AI @ Product platform maturity and team availability
- M2 (Change): Reviewer empowerment needs CAB and Engineering alignment
- Delays from external team dependencies can cascade across multiple methods

**Mitigation:**
- Trusted Partnership value: position as enabler, not controller
- Early stakeholder engagement (workshop model)
- Clear RACI for cross-team initiatives
- Regular alignment check-ins with key partners
- Flexibility: adjust scope if dependencies block progress
- Build relationships proactively, not reactively when blocked

**Method alignment:** M1, M2, M3, M5

---

## Obstacle 5: Career Framework Adoption & Talent Retention

**Description:** Introducing a career framework (M5.2) raises expectations for advancement and compensation. If advancement is blocked by budget/headcount constraints or the framework doesn't resonate with the team, retention risk increases instead of decreases. Talent attrition disrupts AI enablement, automation work, and organizational capability building—undermining the entire transformation.

**Impact:**
- M5.2 (Career Development): Framework becomes demotivating if no one advances
- M5.2d (Retention): Attrition if expectations unmet
- M5.1/M5.3: Talent loss disrupts AI enablement and automation work
- Organizational capability building fails if people leave
- Loss of institutional knowledge and momentum across all methods

**Mitigation:**
- Be transparent: framework defines competencies, not guarantees advancement
- Focus on skill development regardless of promotion timing
- Explore lateral moves if vertical advancement blocked
- Quarterly career conversations to manage expectations
- Celebrate competency growth, not just promotions
- Link career development to meaningful stretch assignments and learning opportunities

**Method alignment:** M5

---

## Obstacles Summary Table

| # | Obstacle | Primary Methods Impacted | Risk Level | Mitigation Status |
|---|----------|-------------------------|------------|-------------------|
| 1 | Regulatory Deadlines & Capacity Constraints | M1, M6, M2-M5 | High | Planned (capacity allocation) |
| 2 | AI Skill Gap & Platform Maturity | M5, M2 | High | In progress (M5.1 training) |
| 3 | Data Quality & Trust in Automated Governance | M4, M2, M3, M5, M6 | Medium-High | In progress (M4.2 data models, validation) |
| 4 | Cross-Organizational Dependencies & Alignment | M1, M2, M3, M5 | Medium | In progress (workshops, partnerships) |
| 5 | Career Framework Adoption & Talent Retention | M5 | Medium | Requires management |

---

**Last Updated:** 2026-04-02
