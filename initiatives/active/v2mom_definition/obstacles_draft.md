# V2MOM Obstacles - Draft

**Date:** 2026-04-02
**Purpose:** Define key obstacles/barriers to achieving V2MOM Vision through Methods

---

## Framework for Obstacles

Obstacles should be:
1. **Real barriers** - actual challenges you expect to face
2. **Specific** - clear enough to address
3. **Honest** - acknowledge real risks
4. **Connected to Methods** - align with what you're trying to achieve

---

## Draft Obstacles

### Obstacle 1: Fixed-Date Regulatory Pressure

**Description:** FedRAMP deadlines (Method 1) create a non-negotiable surge in design and documentation effort during Q2 2026, consuming capacity and potentially delaying other transformation work.

**Impact:**
- M1 (FedRAMP): Risk of delays in 3PAO readiness
- M6 (Sustainability): Q2 operational capacity spikes to 40%+ vs 30% target
- M2-M5: Transformation work competes with FedRAMP urgency

**Mitigation:**
- Explicit capacity allocation (M6.1) with quarterly tracking
- Clear prioritization: M1 takes precedence in Q2 2026
- Pre-plan M2-M5 work to avoid FedRAMP collision

**Method alignment:** M1, M6

---

### Obstacle 2: AI & Automation Skill Gap

**Description:** Transitioning to "AI-First" and "Process as Code" (Method 5) requires the team to rapidly master AI @ Product platform, AI tool usage, and automation design while maintaining current operations—creating a steep learning curve with no formal training program.

**Impact:**
- M5.1 (AI Enablement): Risk of slow adoption or superficial AI usage
- M5.3 (Process Industrialization): Pilot skill deployment may miss Q4 2026 target
- M2 (Change): Automation discovery relies on AI capability
- Team burnout from learning + operating simultaneously

**Mitigation:**
- Budget 30-35% capacity for M5 (AI enablement, learning time, experimentation)
- Start with narrow pilot scope (M5.3b) to build confidence
- Weekly AI experimentation sessions (M5.1) for peer learning
- Accept "good enough" v1.0 for pilot skill

**Method alignment:** M5, M2

---

### Obstacle 3: Stakeholder Adoption & Trust in Automated Governance

**Description:** Shifting from human reviews to AI-driven, system-enforced logic (Methods 2, 3, 5) requires absolute stakeholder confidence in technical data and automation. Lack of trust risks regression to manual approvals, negating velocity and scalability gains.

**Impact:**
- M2 (Change): Reviewer empowerment and CFR correlation may face resistance
- M3 (Incident): Triage automation and alert validation may be second-guessed
- M5.3 (Process Industrialization): Engineering teams may not adopt PE Skills
- Credibility risk if automation produces incorrect results

**Mitigation:**
- Transparency in automation logic (M4: metric lineage, documentation)
- Validate automation accuracy before full deployment (pilot skills, CFR correlation testing)
- Gradual rollout with human oversight initially
- Communication: position as "augmentation" not "replacement"
- Build trust through M4 (metrics literacy, self-service governance)

**Method alignment:** M2, M3, M5, M4

---

### Obstacle 4: Metric Trust & Data Fragmentation

**Description:** Fragmented data entry across Jira projects and lack of automated links between logs and version control risk diluting CPTO Metric accuracy (Method 4). If stakeholders don't trust metrics, data-driven decision-making fails.

**Impact:**
- M4 (Metrics): Risk of low adoption or stakeholder skepticism
- M2 (Change): CFR correlation accuracy depends on data quality
- M6 (Capacity): Story point tracking unreliable if data inconsistent
- Executive decisions based on flawed data = credibility crisis

**Mitigation:**
- M4.2: Robust data models and validation logic
- M4.3: Metric lineage documentation for transparency
- M4.1: Stakeholder sign-off on metric definitions
- Baseline validation period (Q1 2026) before reporting
- Monthly data quality reviews

**Method alignment:** M4, M2, M6

---

### Obstacle 5: Career Framework Acceptance & Retention Risk

**Description:** Introducing a career framework (M5.2) raises expectations for advancement and compensation. If advancement is blocked by budget/headcount constraints or framework doesn't resonate with team, retention risk increases instead of decreases.

**Impact:**
- M5.2 (Career Development): Framework becomes demotivating if no one advances
- M5.2d (Retention): Attrition if expectations unmet
- M5.1/M5.3: Talent loss disrupts AI enablement and automation work
- Organizational capability building fails if people leave

**Mitigation:**
- Be transparent: framework defines competencies, not guarantees advancement
- Focus on skill development regardless of promotion timing
- Explore lateral moves if vertical advancement blocked
- Quarterly career conversations to manage expectations
- Celebrate competency growth, not just promotions

**Method alignment:** M5

---

### Obstacle 6: Capacity Constraints & Transformation vs Operations Balance

**Description:** Transformation work (M1-M5) requires sustained 70% capacity allocation, but operational tasks (M6) have unpredictable surges (audit season, CritSits, urgent support). Risk of either operational degradation or transformation stagnation.

**Impact:**
- M6 (Sustainability): Operational capacity exceeds 35% = transformation slows
- M1-M5: Delayed milestones due to operational firefighting
- Team burnout from sustained high-intensity work
- Quality degradation in either operations or transformation

**Mitigation:**
- M6.1: Quarterly capacity tracking with course correction
- Explicit capacity targets: 30% operational, 70% transformation
- Protect transformation time: dedicated focus blocks, say "no" to non-essential operational asks
- Self-service documentation (M6.3) to reduce ad-hoc consultation burden
- Automation (M5.3) to reduce M6 operational load over time

**Method alignment:** M6, M1-M5

---

### Obstacle 7: Cross-Organizational Dependencies & Alignment

**Description:** Success depends on collaboration with teams beyond Process Engineering (GS, SRE, Engineering teams, AI @ Product platform team). Misalignment, competing priorities, or delays from dependencies can block progress.

**Impact:**
- M1 (FedRAMP): Requires GS and SRE collaboration for operational model
- M3 (Incident): Retrospective transformation needs SRE and Value Stream Leader buy-in
- M5.3 (Process Industrialization): Depends on AI @ Product platform maturity
- M2 (Change): Reviewer empowerment needs CAB and Engineering alignment
- Workshop findings: GS/Eng alignment issues already documented

**Mitigation:**
- Trusted Partnership value: position as enabler, not controller
- Early stakeholder engagement (workshop model)
- Clear RACI for cross-team initiatives
- Regular alignment check-ins with key partners
- Flexibility: adjust scope if dependencies block progress

**Method alignment:** M1, M2, M3, M5

---

### Obstacle 8: Platform & Tooling Maturity

**Description:** AI @ Product platform and Process as Code capabilities are emerging/immature. Platform limitations, lack of documentation, or technical issues could delay M5.3 industrialization work.

**Impact:**
- M5.3 (Process Industrialization): Pilot skill deployment at risk
- M5.3d (Technical Capability): Team certification blocked by platform immaturity
- M5.3c (Backlog Readiness): Blueprints may not translate if platform constraints unknown
- Wasted effort if platform architecture changes mid-flight

**Mitigation:**
- Start with narrow pilot scope (M5.3b) to test platform early
- Close collaboration with AI @ Product team
- Accept platform limitations: work within constraints, don't wait for perfection
- Document platform gaps for future advocacy
- Budget contingency: if platform not ready, defer M5.3 to next V2MOM cycle

**Method alignment:** M5

---

## Obstacles Summary Table

| # | Obstacle | Primary Methods Impacted | Risk Level | Mitigation Status |
|---|----------|-------------------------|------------|-------------------|
| 1 | Fixed-Date Regulatory Pressure | M1, M6 | High | Planned (capacity allocation) |
| 2 | AI & Automation Skill Gap | M5, M2 | High | In progress (M5.1 training) |
| 3 | Stakeholder Adoption & Trust | M2, M3, M5, M4 | Medium-High | Planned (transparency, validation) |
| 4 | Metric Trust & Data Fragmentation | M4, M2, M6 | Medium | In progress (M4.2 data models) |
| 5 | Career Framework Acceptance | M5 | Medium | Requires management |
| 6 | Capacity Constraints | M6, M1-M5 | High | Planned (M6.1 tracking) |
| 7 | Cross-Organizational Dependencies | M1, M2, M3, M5 | Medium | In progress (workshops, partnerships) |
| 8 | Platform & Tooling Maturity | M5 | Medium-Low | Planned (narrow pilot) |

---

## Alternative: Condensed Version (4-5 Obstacles)

If 8 obstacles feels like too many, here's a condensed version combining related themes:

### Condensed Obstacle 1: Regulatory Deadlines & Capacity Constraints

Combines: Fixed-Date Regulatory Pressure + Capacity Constraints

*FedRAMP deadlines create non-negotiable capacity surges while transformation work requires sustained 70% capacity. Risk of operational degradation or transformation stagnation.*

---

### Condensed Obstacle 2: AI Skill Gap & Platform Maturity

Combines: AI & Automation Skill Gap + Platform & Tooling Maturity

*Transitioning to AI-First requires mastering AI @ Product platform and AI tools with no formal training program, while the platform itself is emerging/immature—creating steep learning curve and technical risk.*

---

### Condensed Obstacle 3: Trust in Automated Governance & Metric Accuracy

Combines: Stakeholder Adoption & Trust + Metric Trust & Data Fragmentation

*Shifting to system-enforced, data-driven governance requires absolute stakeholder confidence. Fragmented data and automation errors risk regression to manual approvals, negating velocity gains.*

---

### Condensed Obstacle 4: Cross-Organizational Alignment & Dependencies

Combines: Cross-Organizational Dependencies + Career Framework Acceptance (retention as dependency risk)

*Success depends on collaboration with GS, SRE, Engineering, and AI @ Product teams. Misalignment, competing priorities, or talent attrition can block progress.*

---

## Recommendations

### Option A: Use All 8 Obstacles (Comprehensive)
**Pros:**
- Thorough risk identification
- Each obstacle is specific and actionable
- Shows depth of thinking

**Cons:**
- May feel overwhelming
- Some obstacles overlap

---

### Option B: Use 4-5 Condensed Obstacles (Streamlined)
**Pros:**
- Cleaner, more digestible
- Focuses on highest-level barriers
- Standard V2MOM practice (typically 4-6 obstacles)

**Cons:**
- Loses some specificity
- May miss nuances

---

### My Recommendation: **Option B (Condensed 4 Obstacles)**

Use the 4 condensed obstacles—they capture all the themes while being more digestible for stakeholders.

**Suggested order:**
1. Regulatory Deadlines & Capacity Constraints
2. AI Skill Gap & Platform Maturity
3. Trust in Automated Governance & Metric Accuracy
4. Cross-Organizational Alignment & Dependencies

---

## Next Steps

1. Review obstacles - which resonate? Which are missing?
2. Choose: 8 detailed or 4 condensed?
3. Refine wording based on your feedback
4. Format for Confluence
5. Add to V2MOM page

What's your take on these obstacles? Should we go with the condensed version or keep them detailed?
