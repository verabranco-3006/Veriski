# M2 Working Session — 2026-04-18

**Attendees:** Vera Branco, Laura Ferreira
**Recurring:** Weekly (Fridays)

**⚠️ REMINDER: Check if AI Companion is on to record the call content**

---

## Context

Method 2: Transform Change Management — Laura owns this method. Regular working sessions to drive progress on submethods and measurements.

---

## Open Action Items


---

## Agenda

### 1. M2.1: Change Lead Time Reduction — Measurement Definition

**Goal:** Validate the measurement approach and discuss gaps

**Current definition:**
- Metric: % reduction in mean time from RFC Creation to Implementation for Normal Changes
- Baseline: 16 days (H2 2025 validated)
- Target: -30% by Q2 2027 (11 days)
- Intermediate milestones: Q3 2026: 15d → Q4 2026: 14d → Q1 2027: 12d → Q2 2027: 11d
- Data source: Jira RFC project, customfield_18619 (Implementation Timestamp)

**Process gaps to discuss:**
- **Implementation timestamp accuracy** — relies on manual field population by implementers. How reliable is this data today?
- **Outlier handling** — max was 6114 hours in baseline. Need protocol for extreme cases. What's the cutoff?
- **Change scope variations** — lead time affected by change complexity, not just process efficiency. Should we segment by change type?

**Ask:** Is the measurement feasible with current data quality? What needs to change to make it reliable?

---

### 2. M2.2: Standard Change Promotion Rate — Feasibility Review

**Goal:** Determine if this metric is feasible and what's needed to track it

**Current definition:**
- Metric: % increase in volume of changes transitioned from Normal to Standard
- Target: +50% increase by Q2 2027
- Data source: Jira Change Catalog + Change Management project

**Process gaps to discuss:**
- **Baseline data** — do we have H2 2024 Standard Change execution count?
- **Change Catalog maturity** — requires complete Change Catalog Registry. Where are we on this?
- **Promotion criteria** — what's the framework for promoting Normal → Standard? Does it exist?
- **Tracking mechanism** — need Jira field to track when/why changes were promoted

**Ask:** Is this metric feasible to track? Do we have baseline data? Does the +50% target make sense given current Standard Change maturity?

---

## Meeting Notes

*Add notes during the session below*

### Topics Discussed


### Decisions Made


### Not Covered — Carry Forward


### New Action Items

