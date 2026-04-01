# Change Management Skills - AI Automation Opportunities

**Purpose:** Identify opportunities to create Claude skills that help engineering teams execute the Change Management process more efficiently in ODC.

**Owner:** Vera Branco
**Date:** March 24, 2026

---

## Overview

This document outlines potential Claude Code skills to streamline Change Management workflows, reduce friction, improve compliance, and support the V2MOM 2026 goals:
- **M2.1:** Reduce lead time from RFC creation to implementation (target: 11 days)
- **M2.2:** Increase Standard Change promotion rate (+50%)
- **M2.3:** Improve Change Failure Rate tracking through asset-to-incident correlation

---

## Skill Opportunities by Category

### 1. RFC Lifecycle Management

#### `/rfc-create` — Guide engineers through RFC creation
**Purpose:** Reduce RFC creation errors and improve completeness upfront

**Capabilities:**
- Provide templates for Normal, Standard, Emergency changes
- Auto-populate required fields based on operation type
- Suggest catalog article based on description
- Pre-flight validation (all required info before submission)

**Impact:** Fewer incomplete RFCs, faster CAB reviews, reduced back-and-forth

---

#### `/rfc-status` — Check RFC status and next actions
**Purpose:** Provide visibility into RFC progress and reduce status inquiry overhead

**Capabilities:**
- Show current stage in workflow
- List pending approvals/reviews
- Calculate lead time vs. target (11-day goal)
- Alert if stuck > X days

**Impact:** Engineers self-serve status, identify bottlenecks early

---

#### `/rfc-prep-review` — Prepare RFC for CAB review
**Purpose:** Ensure RFCs are review-ready before CAB meeting

**Capabilities:**
- Checklist: all evidence attached, fields populated
- Risk assessment completion check
- Identify appropriate reviewers (segregation of duties)
- Generate review summary for CAB

**Impact:** Faster CAB approvals, fewer deferrals due to incomplete info

---

#### `/rfc-implement-checklist` — Implementation guidance
**Purpose:** Guide implementation and ensure evidence collection

**Capabilities:**
- Step-by-step runbook retrieval from catalog
- Evidence collection reminders
- Post-implementation validation steps
- Auto-transition to "Implemented" with timestamp

**Impact:** Consistent implementations, complete evidence trail

---

### 2. Operation Type & Catalog Management

#### `/catalog-search` — Find catalog articles/runbooks
**Purpose:** Faster discovery of operation procedures

**Capabilities:**
- Search by keywords, operation type, service
- Show most frequently used articles for similar changes
- Link to runbook documentation
- Suggest tags/categorization

**Impact:** Reduced time to find correct procedure, standardized operations

---

#### `/operation-classify` — Classify operation type
**Purpose:** Improve operation type consistency and accuracy

**Capabilities:**
- Analyze RFC description and suggest operation type
- Map to existing catalog article
- Flag if new operation type (needs documentation)
- Show similar past RFCs for reference

**Impact:** Better data quality, easier trend analysis, catalog cleanup

---

#### `/runbook-validate` — Validate runbook completeness
**Purpose:** Ensure runbooks are complete and up-to-date

**Capabilities:**
- Check if runbook exists for operation type
- Identify missing steps or unclear instructions
- Suggest standardization opportunities
- Flag outdated runbooks (not used in X months)

**Impact:** Higher quality runbooks, proactive maintenance

---

### 3. Standard Change Promotion

#### `/standard-candidate` — Identify Standard Change candidates
**Purpose:** Accelerate Standard Change promotion to hit +50% growth target

**Capabilities:**
- Analyze completed Normal RFCs for patterns
- Calculate success rate, frequency, risk level
- Suggest which Normal changes could become Standard
- Generate promotion proposal with evidence

**Impact:** Data-driven Standard Change promotion, faster approvals

---

#### `/standard-promote` — Promote Normal to Standard Change
**Purpose:** Guide promotion process with proper documentation

**Capabilities:**
- Guide through promotion criteria
- Generate required documentation
- Create Standard Change model in catalog
- Track pre-approval process

**Impact:** Streamlined promotion workflow, consistent documentation

---

### 4. Shadow Change Detection & Compliance

#### `/shadow-detect` — Detect potential shadow changes
**Purpose:** Identify changes happening outside RFC process

**Capabilities:**
- Scan deployment logs vs. RFC tickets
- Flag deployments without corresponding RFC
- Identify teams with highest shadow rate
- Generate compliance report

**Impact:** Close compliance gap, eliminate shadow changes

---

#### `/change-evidence` — Evidence collection assistant
**Purpose:** Ensure complete evidence for each change

**Capabilities:**
- Checklist of required evidence per change type
- Auto-attach deployment logs, test results
- Screenshot/artifact upload guidance
- Validate evidence completeness

**Impact:** Complete audit trail, faster audits, SOC2/FedRAMP compliance

---

### 5. Metrics & Reporting

#### `/change-metrics` — Change Management metrics dashboard
**Purpose:** Real-time visibility into Change Management performance

**Capabilities:**
- Lead time: Creation → Implementation (vs. 11-day target)
- Standard Change promotion rate (+50% goal)
- Shadow change detection rate
- CAB approval time breakdown
- Top operation types by volume

**Impact:** Data-driven decisions, track V2MOM progress

---

#### `/cfr-analysis` — Change Failure Rate analysis
**Purpose:** Implement M2.3 - asset-to-incident correlation for CFR

**Capabilities:**
- Correlate RFC to incidents (asset-to-incident)
- Calculate CFR per operation type, team, ring
- Identify high-risk change patterns
- Suggest improvement actions

**Impact:** Accurate CFR measurement, risk reduction, targeted improvements

---

### 6. CAB Process Support

#### `/cab-prep` — Prepare for CAB meeting
**Purpose:** Streamline CAB meeting preparation

**Capabilities:**
- List all RFCs pending CAB review
- Summarize risks, impacts, approvals status
- Highlight urgent/time-sensitive changes
- Generate CAB agenda

**Impact:** Faster CAB meetings, better prepared reviews

---

#### `/reviewer-suggest` — Suggest appropriate reviewers
**Purpose:** Ensure proper segregation of duties and domain expertise

**Capabilities:**
- Check segregation of duties (not requester's team)
- Identify domain experts for operation type
- Show reviewer workload/availability
- Flag conflicts of interest

**Impact:** Appropriate reviews, compliance with segregation rules

---

### 7. Knowledge & Learning

#### `/change-post-mortem` — Post-implementation review
**Purpose:** Capture lessons learned and improve processes

**Capabilities:**
- Guide through lessons learned
- Update runbook if deviations occurred
- Identify process improvements
- Link to related incidents if CFR event

**Impact:** Continuous improvement, better runbooks

---

#### `/change-training` — Change Management training assistant
**Purpose:** Onboard new engineers to Change Management process

**Capabilities:**
- Explain change types, when to use each
- CAB process walkthrough
- Evidence requirements by change type
- Common mistakes and how to avoid

**Impact:** Faster onboarding, fewer mistakes, consistent understanding

---

### 8. Integration & Automation

#### `/pipeline-to-rfc` — Convert pipeline deployment to RFC
**Purpose:** Eliminate shadow changes at source by auto-creating RFCs

**Capabilities:**
- Parse CI/CD pipeline metadata
- Auto-create RFC from deployment intent
- Link deployment artifacts to RFC
- Close loop: pipeline → RFC → evidence

**Impact:** Zero shadow changes from automated deployments

---

#### `/rfc-automation-check` — Assess automation readiness
**Purpose:** Identify automation opportunities for high-volume operations

**Capabilities:**
- Identify manual steps that could be automated
- Calculate ROI for automation (frequency × time)
- Suggest Standard Change automation opportunities
- Track automation backlog

**Impact:** Long-term efficiency gains, reduced manual work

---

### 9. Emergency & Risk Management

#### `/emergency-rfc` — Emergency RFC fast-track
**Purpose:** Expedite emergency changes while maintaining compliance

**Capabilities:**
- Expedited template with hierarchy approval chain
- Risk assessment quickstart
- Post-implementation review reminder
- Convert Emergency → Normal retrospectively

**Impact:** Faster incident resolution, maintained compliance

---

## Prioritization Framework

### High Impact, Quick Win
**Recommended for immediate implementation:**

| Skill | Impact | Complexity | V2MOM Alignment |
|-------|--------|------------|-----------------|
| `/rfc-create` | High | Low | M2.1 (lead time) |
| `/catalog-search` | High | Low | M2.2 (operation clarity) |
| `/rfc-status` | High | Low | M2.1 (visibility) |
| `/change-metrics` | High | Medium | M2.1, M2.2, M2.3 (all metrics) |

**Why these first:**
- Immediate friction reduction for engineers
- Low implementation complexity
- Direct impact on V2MOM measurements
- Build momentum for broader adoption

---

### High Impact, Longer Term
**Recommended for Q2-Q3 2026:**

| Skill | Impact | Complexity | V2MOM Alignment |
|-------|--------|------------|-----------------|
| `/shadow-detect` | Very High | High | M2.3 (compliance gap) |
| `/standard-candidate` | High | Medium | M2.2 (Standard promotion) |
| `/cfr-analysis` | Very High | High | M2.3 (CFR tracking) |
| `/pipeline-to-rfc` | Very High | High | M2.3 (eliminate shadows) |

**Why these matter:**
- Address compliance and audit requirements
- Enable data-driven Standard Change promotion
- Close the loop on CFR measurement
- Require integration with multiple systems

---

### Specialized/Advanced
**Recommended for future consideration:**

| Skill | Impact | Complexity | Use Case |
|-------|--------|------------|----------|
| `/reviewer-suggest` | Medium | Medium | CAB efficiency |
| `/runbook-validate` | Medium | Medium | Documentation quality |
| `/rfc-automation-check` | Medium | Low | Long-term efficiency |
| `/change-training` | Medium | Low | Onboarding |

**When to implement:**
- After core skills are adopted
- When team asks for specific capability
- As part of continuous improvement cycle

---

## Implementation Roadmap

### Phase 1: Foundation (Q2 2026)
**Focus:** Quick wins, immediate friction reduction

**Skills to build:**
1. `/rfc-create` — Template-guided RFC creation
2. `/catalog-search` — Fast runbook discovery
3. `/rfc-status` — Self-service status checks
4. `/change-metrics` — Dashboard visibility

**Success criteria:**
- 50% of new RFCs use `/rfc-create`
- Average RFC creation time reduced by 30%
- CAB meeting prep time reduced by 40%

---

### Phase 2: Compliance & Automation (Q3 2026)
**Focus:** Shadow change elimination, Standard promotion

**Skills to build:**
1. `/shadow-detect` — Identify non-compliant changes
2. `/standard-candidate` — Data-driven promotion suggestions
3. `/operation-classify` — Improve data quality
4. `/change-evidence` — Complete audit trails

**Success criteria:**
- Shadow change rate < 5%
- Standard Change volume +30% (on track for +50%)
- 90% RFCs have complete evidence

---

### Phase 3: Intelligence & Optimization (Q4 2026)
**Focus:** CFR measurement, continuous improvement

**Skills to build:**
1. `/cfr-analysis` — Asset-to-incident correlation
2. `/pipeline-to-rfc` — Automated RFC creation
3. `/rfc-automation-check` — Identify automation opportunities
4. `/change-post-mortem` — Structured learning

**Success criteria:**
- Accurate CFR measurement per operation type
- Zero shadow changes from automated pipelines
- 3+ operations automated based on ROI analysis

---

## Next Steps

### Immediate Actions (This Week)
1. **Select 3 skills for pilot** — Recommend: `/rfc-create`, `/catalog-search`, `/change-metrics`
2. **Identify pilot team** — Choose team with high RFC volume and willingness to experiment
3. **Define success metrics** — Track adoption rate, time savings, error reduction

### Short-Term (Next 2 Weeks)
1. **Build MVP for pilot skills** — Focus on core functionality, not polish
2. **Gather feedback** — What works? What's missing? What's confusing?
3. **Iterate based on feedback** — Adjust before broader rollout

### Medium-Term (Next Quarter)
1. **Roll out successful skills** — Expand to all engineering teams
2. **Build Phase 2 skills** — Shadow detection, Standard promotion
3. **Track V2MOM progress** — Measure impact on lead time, promotion rate, CFR

---

## Alignment with Current Work

### Laura's Current Focus
These skills directly support Laura's ongoing work:
- **RFC Jira Projects Standardization** → `/rfc-create` enforces consistency
- **Operation Type Analysis** → `/operation-classify` improves data quality
- **Runbook Analysis & Centralization** → `/catalog-search`, `/runbook-validate`
- **Catalog Articles Lifecycle** → `/standard-candidate` identifies promotion opportunities

### Team V2MOM Goals
Skills directly enable measurement and improvement:
- **M2.1 (Lead Time -30%)** → `/rfc-status`, `/rfc-prep-review` reduce delays
- **M2.2 (Standard Promotion +50%)** → `/standard-candidate` drives promotions
- **M2.3 (CFR Tracking)** → `/cfr-analysis` enables accurate measurement

---

## Questions to Explore

Before finalizing implementation:

1. **Integration:** Which systems need API access? (Jira, Power BI, deployment logs, catalog)
2. **Authentication:** How do skills authenticate as user vs. service account?
3. **Data quality:** What's current state of RFC fields, operation types, catalog articles?
4. **Adoption:** What incentives drive engineers to use skills vs. manual process?
5. **Maintenance:** Who owns skill updates when process changes?

---

## Conclusion

These 20 skill opportunities represent a comprehensive approach to transforming Change Management through AI automation. By focusing on high-impact, low-complexity wins first, we can build momentum, demonstrate value, and scale to more complex integrations over time.

**Recommended starting point:** Build `/rfc-create`, `/catalog-search`, and `/change-metrics` as pilot skills in Q2 2026, measure adoption and impact, then expand based on results.

---

**Last Updated:** March 24, 2026
**Next Review:** April 15, 2026 (after pilot feedback)