# V2MOM 2026 - Measurement Implementation Updates

**Date:** April 4, 2026
**Purpose:** Document changes to measurements based on today's review and identify implementation gaps for team discussion

---

## Changes Summary

### Removed Measurements
- **M1.3:** Training Certification Rate (moved to reference only)
- **M2.2:** Standard Change Promotion Rate (requires in-depth review)
- **M2.3:** RFC Rejection Velocity (moved to reference only)
- **M4.3:** Dashboard Adoption Rate (requires Paulo review)
- **M4.4:** Metric Data Quality Score (requires Paulo review)
- **M5.2c (old):** Career Progression Rate
- **M5.2d:** Team Retention Rate
- **M5.3b:** Pilot Skill Deployment
- **M5.3c:** Post-V2MOM Backlog Readiness
- **M5.3d:** Technical Platform Capability

### Updated Measurements
- **M4.5:** Changed from "Stakeholder Satisfaction" to "2027 Strategic Metrics Blueprint"
- **M5.1a:** Target changed to 100% by Q2 2026 (was 80% by Q4 2026)
- **M5.1b:** Clarified as internal PE workflows (SECONDARY priority)
- **M5.1c:** Requires baseline establishment in Q2 2026
- **M5.2c (new):** Team Engagement (eNPS) - replaces retention rate
- **M5.3a:** Renamed to "Process Automation Delivery (for Engineering Teams)" - PRIMARY priority, owner Paulo
- **M6.2:** Renamed to "Process Orchestration Effectiveness (CAB & RCA)" - removed CAB duration, added RCA orchestration

### Timeline Adjustments
- Most Q4 2026 targets moved to Q2 2027 (end of V2MOM period)

---

## Implementation Updates - Measurements That Changed

### M4.5: 2027 Strategic Metrics Blueprint

**Metric:** Completion of strategic metrics blueprint for 2027

**Definition:** Define and document the strategic metrics required for 2027, including calculation logic, data sources, and implementation roadmap

**Target:** Blueprint completed and signed off by stakeholders by Q4 2026

**Owner:** Paulo Alves Monteiro

**High-Level Implementation Logic:**
- Document next year's strategic metric requirements before year-end
- Include calculation formulas, data sources, dashboard mockups
- Stakeholder review and sign-off process

**Implementation Gaps / Open Questions:**
- **Who are the stakeholders** for sign-off? (CPTO leadership? Specific personas?)
- **What format** should the blueprint take? (Confluence doc? Presentation? Interactive prototype?)
- **What triggers** metric definition for 2027? (CPTO strategy? Business priorities? Regulatory changes?)
- **How detailed** should the blueprint be? (High-level concepts vs. implementation-ready specs?)
- **What's the review/approval process?** (Sequential reviews? Workshop format? Iterative refinement?)

---

### M5.1a: AI Adoption Rate

**Metric:** % of team members actively using AI tools in weekly workflows

**Target:** 100% by end of Q2 2026 (CHANGED from 80% by Q4 2026)

**Owner:** Vera Branco

**High-Level Implementation Logic:**
- Track weekly AI tool usage (Claude Code, Koda)
- Survey or platform analytics

**Implementation Gaps / Open Questions:**
- **How to measure "active usage"?** (Self-reported survey? Platform analytics? Both?)
- **What qualifies as "active"?** (Once per week minimum? Daily? Multiple times per week?)
- **Which tools count?** (Just Claude Code/Koda? Or any AI tool like ChatGPT?)
- **How to track without surveillance concerns?** (Anonymous survey? Honor system? Platform logs?)
- **What if someone travels or is OOO?** (Exclude from denominator that week? How to handle?)

---

### M5.1b: AI-Augmented Workflow Documentation

**Metric:** Number of documented AI-augmented workflow patterns for PE internal use

**Target:** ≥5 documented patterns by Q2 2027

**Owner:** Vera Branco

**High-Level Implementation Logic:**
- Document workflow patterns where AI augments internal PE work
- Examples: Operations Review prep, meeting prep, RFC review, data analysis
- **SECONDARY PRIORITY** - focus on M5.3a (Engineering teams) first

**Implementation Gaps / Open Questions:**
- **What qualifies as a "documented pattern"?** (Template required? Minimum level of detail? Format?)
- **Where are patterns documented?** (Confluence? Team wiki? Knowledge base?)
- **Who validates** a pattern is complete enough to count?
- **How to prioritize** which workflows to document first?
- **How to ensure patterns are actually useful** vs. documentation for documentation's sake?

---

### M5.1c: Time Savings Through AI Augmentation

**Metric:** Average hours per week saved through AI augmentation

**Target:** 2-4 hours/week per team member by Q2 2027

**Owner:** Vera Branco

**High-Level Implementation Logic:**
- Establish baseline time for workflows in Q2 2026 (BEFORE AI augmentation)
- Quarterly surveys to measure time savings
- Key opportunity: Operations Review prep (currently 6 person-days every 2 weeks → target <2 person-days)

**Implementation Gaps / Open Questions:**
- **How to establish baseline?** (Time tracking for specific workflows? Estimates? Historical data?)
- **Which workflows to baseline?** (All workflows? Just the top 5 from M5.1b?)
- **How to measure time savings accurately?** (Self-reported? Before/after comparison? Control group?)
- **What if time savings vary by person?** (Track individually? Average across team? Normalize somehow?)
- **How to isolate AI impact** from other efficiency improvements? (Process changes, tool upgrades, learning curve?)
- **Operations Review prep measurement:** How to track prep time reduction specifically? (Manual logging? Observation?)

---

### M5.2c: Team Engagement (eNPS)

**Metric:** Employee Net Promoter Score (eNPS) for Process Engineering team

**Target:** Positive eNPS score (>0) by Q2 2027, trending toward >20 (favorable)

**Owner:** Vera Branco

**High-Level Implementation Logic:**
- Office Vibe eNPS or informal assessment mechanisms
- Small team size (3 people) prevents direct eNPS visibility to manager
- May require indirect measurement or informal pulse checks

**Implementation Gaps / Open Questions:**
- **How to measure eNPS for small team** given Office Vibe privacy constraints? (Manager can't see individual responses for 3-person team)
- **Alternative measurement approaches?** (Quarterly pulse checks? Anonymous surveys? 1:1 engagement discussions?)
- **What triggers action** if eNPS is negative? (Immediate intervention? Root cause analysis? Wait for trend?)
- **How to establish baseline?** (Historical Office Vibe data if available? Start fresh in Q2 2026?)
- **Quarterly vs annual measurement?** (More frequent = better signal but survey fatigue?)

---

### M5.3a: Process Automation Delivery (for Engineering Teams)

**Metric:** Number of automation solutions delivered from blueprint to production deployment

**Target:** 3-5 blueprints validated by Q2 2027, ≥1 deployed to production with usage validation by Q2 2027

**Owner:** Paulo Alves Monteiro (CHANGED from TBD)

**High-Level Implementation Logic:**
- Track automation pipeline: Identified → Blueprint → Pilot → Production
- Focus on Engineering team automation (RFC validation, Event Management, RCA support, CFR correlation, Problem Management)
- **PRIMARY PRIORITY** - build for others first, not internal PE workflows

**Implementation Gaps / Open Questions:**
- **Blueprint validation criteria:** What makes a blueprint "validated"? (Stakeholder sign-off? Technical review? Both?)
- **Production deployment definition:** What qualifies as "deployed"? (Available to all teams? Just pilot teams? Usage threshold?)
- **Usage validation approach:** How to measure usage? (Analytics? Surveys? Usage logs?)
- **Prioritization framework:** How to choose which automation candidates to blueprint first? (V2MOM metric support? Engineering team request? Impact analysis?)
- **Ownership model:** Paulo owns M5.3a but who does the technical implementation? (Paulo's capacity? Team collaboration? External support?)
- **Pilot vs production definition:** When does a pilot graduate to production? (Usage threshold? Time threshold? Quality gate?)

---

### M6.2: Process Orchestration Effectiveness (CAB & RCA)

**Metric:** Multiple metrics tracking governance and retrospective orchestration

**Components:**
- **M6.2a:** CAB Prep Time <4 hours per session
- **M6.2b:** First-Pass Approval Rate >85%
- **M6.2c:** RCA Orchestration Coverage >90% (NEW)

**Target:** Q2 2027 (quarterly tracking)

**Owner:** Vera Branco (executed in rotation across team)

**High-Level Implementation Logic:**
- Track CAB prep time (manual time logging or Jira worklog)
- Track RFC first-pass approval rate (Jira query)
- Track RCA orchestration coverage (PE facilitation for mandatory retrospectives)

**Implementation Gaps / Open Questions:**

**M6.2a - CAB Prep Time:**
- **How to track prep time?** (Manual self-reporting? Jira worklog? Calendar blocking?)
- **What activities count as "prep"?** (RFC pre-review? Agenda creation? Material preparation? All of the above?)
- **Who tracks it?** (Person doing the prep? Automated based on Jira time logs?)

**M6.2b - First-Pass Approval Rate:**
- **What is "first-pass approval"?** (Approved without any questions? Approved without rework request? How to code this in Jira?)
- **How to distinguish** "approved with minor questions" vs "needs rework"?
- **Data source:** Which Jira field tracks this? (Custom field needed? Status transitions? Comment analysis?)

**M6.2c - RCA Orchestration Coverage (NEW):**
- **What qualifies as "PE orchestration/facilitation"?** (PE facilitates the meeting? PE prepares materials? PE reviews output? Combination?)
- **What is "mandatory retrospective"?** (All status page incidents? High/Critical only? Criteria from M3.5?)
- **How to track PE participation?** (Meeting attendance? Jira field? Calendar tracking? Honor system?)
- **Who reports orchestration?** (PE person who facilitated? Automated based on meeting invites?)
- **Rotation model:** How is RCA facilitation rotated across team? (Round-robin? By expertise? Voluntary?)

---

## Action Items for Team Discussion

### Priority 1: Data Collection Mechanisms
- **M5.1a:** Decide on AI adoption measurement approach (survey vs analytics vs hybrid)
- **M5.1c:** Define baseline establishment approach for time savings
- **M5.2c:** Determine eNPS measurement approach for small team
- **M6.2c:** Define RCA orchestration tracking mechanism

### Priority 2: Definition Clarity
- **M5.1b:** Define "documented pattern" criteria and format
- **M5.3a:** Define blueprint validation criteria and production deployment definition
- **M6.2b:** Define "first-pass approval" and how to capture in Jira
- **M6.2c:** Define "mandatory retrospective" criteria and "PE orchestration" scope

### Priority 3: Ownership & Process
- **M4.5:** Identify stakeholders and review/approval process for 2027 metrics blueprint
- **M5.3a:** Clarify Paulo's role vs team collaboration for technical implementation
- **M6.2c:** Design RCA facilitation rotation model across team

### Priority 4: Baseline Establishment
- **M5.1c:** Establish time savings baseline in Q2 2026
- **M5.2c:** Establish eNPS baseline (if historical data exists) or start fresh
- **M6.2a-c:** Establish CAB and RCA baselines in Q2 2026

---

## Measurements Requiring Further Review

These measurements were flagged during review but not finalized:

### M2.2: Standard Change Promotion Rate
**Status:** Requires in-depth review
**Owner:** Laura Ferreira
**Questions:** Feasibility, baseline data availability, target reasonableness

### M4.3: Dashboard Adoption Rate
**Status:** Requires Paulo review
**Owner:** Paulo Alves Monteiro
**Questions:** Dashboard analytics tracking feasibility, infrastructure requirements

### M4.4: Metric Data Quality Score
**Status:** Requires Paulo review
**Owner:** Paulo Alves Monteiro
**Questions:** PE role in metrics governance vs data quality ownership, metric scope

---

## Next Steps

1. **Team meeting (April 10):** Review implementation gaps and open questions for M5.1a, M5.1c, M5.2c, M5.3a, M6.2c
2. **Team meeting (April 10):** Review Submethod 3.5 definition (Retrospective Transformation) - see `method_3.5_retrospective_transformation.md` for proposed scope addressing team-led model, quality framework, and maturity assessment
3. **Paulo sync:** Discuss M4.3, M4.4 feasibility and M5.3a ownership/implementation approach
4. **Laura sync:** Discuss M2.2 feasibility and baseline data
5. **Baseline establishment (Q2 2026):** Plan data collection for metrics requiring baselines
6. **Full implementation plan:** After team discussions, document detailed implementation approach for each metric

---

*Last updated: 2026-04-04*
