# Change Management — Running Metrics Log

Accumulated CM metrics across Ops Review periods. Enables reliable trend analysis and V2MOM tracking without depending on Confluence extraction.

**Updated by:** `/cm-review-prep` skill (Step 6)
**Source of truth:** This file for trends. Individual prep files (`meetings/prep/YYYY-MM-DD-cm-review-data.md`) for detail.

---

## V2MOM Alignment

Maps each CM metric reported in Ops Review to its V2MOM measurement. Includes measures not yet trackable — status indicates readiness.

| V2MOM ID | Measurement | Target | CM Metric Used | Tracking Status |
|----------|-------------|--------|----------------|-----------------|
| **M2.1** | Change Lead Time Reduction | -30% (11 days) from 16-day baseline | Normal Change lead time (days) — `LEADTIME (Days)` filtered to Normal Changes | ⚠️ PARTIAL — column exists but needs validation against baseline methodology |
| **M2.2a** | Manual Resilience Identification | <20% flagged as automation candidate by Q1 2027 | Normal Planned % (proxy — high planned % suggests automation candidates) | ⚠️ PROXY — custom Jira field required for direct measurement |
| **M2.2b** | RFC Submission Quality Rate | TBD | First-Pass Approval Rate (proxy — M6.2b) | ❌ NOT YET — needs Jira workflow definition for "returned for rework" |
| **M2.2c** | Approver Risk Accountability Rate | TBD | — | ❌ NOT YET — needs Jira risk sign-off field |
| **M2.2d** | Implementer Rejection Rate | TBD | — | ❌ NOT YET — needs catalog + Jira rejection workflow |
| **M2.3** | CFR Correlation Accuracy | >90% by Q4 2026 | — | ❌ NOT YET — correlation engine not built |
| **M2.4** | Standard Change Growth Rate | >60% by Q2 2027 | Standard % of total RFCs | ✅ TRACKABLE |
| **M2.5** | Emergency Classification Accuracy | >95% by Q2 2027 | Emergency RFCs with correct system-wide impact linkage | ✅ TRACKABLE (when Emergency volume > 0) |
| **M2.6** | Change Catalog Completeness | TBD | — | ❌ NOT YET — catalog does not exist |
| **M2.7** | Uncatalogued Operations Rate | <5% by Q1 2027 | — | ❌ NOT YET — catalog does not exist |
| **M6.2b** | First-Pass Approval Rate | >85% | Approved without rework — status transition analysis | ⚠️ PARTIAL — definition agreed, Jira field tracking TBD |
| — | Incident-Driven RFC Rate | <35% (alert threshold) | % RFCs linked to incidents | ✅ TRACKABLE (operational health, no V2MOM ID) |
| — | Fast Track Usage | <5% (alert threshold, M2.2 related) | % RFCs with CHANGE_CATEGORY = "Fast Track" | ✅ TRACKABLE |
| — | Emergency Volume | <3 per period (alert threshold) | Emergency RFC count | ✅ TRACKABLE |

---

## Running Metrics

### Volume

| Period | Total RFCs | Standard | Normal | Emergency | Total Executions | Executions w/ Ring | Ring Not Assigned |
|--------|:----------:|:--------:|:------:|:---------:|:----------------:|:------------------:|:-----------------:|
| Apr 16, 2026 | — | — | — | 6 | — | — | — |
| **Apr 30, 2026** | **53** | **24** | **29** | **0** | **162** | **162** | **0** |

### V2MOM-Aligned Metrics

| Period | M2.1: Normal Lead Time (days) | M2.4: Standard % | M2.5: Emergency Accuracy | M6.2b: First-Pass Approval % | Incident-Driven Rate | Normal Planned % | Fast Track % | Fast Track Count |
|--------|:-----------------------------:|:-----------------:|:------------------------:|:-----------------------------:|:--------------------:|:----------------:|:------------:|:----------------:|
| Feb 19, 2026 | — | 32.6% | 25% (1/4) | — | — | 66.67% | — | — |
| Mar 5, 2026 | — | 32.6% | 40% (2/5) | — | — | 65.00% | — | — |
| Mar 19, 2026 | — | — | 100% (1/1) | — | — | 55.56% | — | — |
| Apr 2, 2026 | — | — | Unknown (2 ERFCs) | — | — | 64.71% | — | — |
| Apr 16, 2026 | — | 49.6% | ~67% (4/6 compliant) | — | 25.45% | 76.92% | — | — |
| **Apr 30, 2026** | **—** | **45.3%** | **N/A (0 ERFCs)** | **—** | **20.75%** | **75.86%** | **10.9%** | **6** |

### Risk Distribution

| Period | Low | Medium | High |
|--------|:---:|:------:|:----:|
| **Apr 30, 2026** | 47 (88.7%) | 5 (9.4%) | 1 (1.9%) |

### Ring Distribution (Change Executions)

| Period | ring-4/lab | ring-3/dev | ring-2/test | ring-1/stage | ring0/osrd | ring+1/osall | ring+2/ea | ring+3/ga | Production % |
|--------|:----------:|:----------:|:-----------:|:------------:|:----------:|:------------:|:---------:|:---------:|:------------:|
| **Apr 30, 2026** | 12 | 10 | 19 | 19 | 8 | 30 | 28 | 36 | 58% |

### Change Category

| Period | Change Config | Change Infra | Restart | Other Write Op | Fast Track | Retry | Customer Request |
|--------|:-------------:|:------------:|:-------:|:--------------:|:----------:|:-----:|:----------------:|
| **Apr 30, 2026** | 15 (27.3%) | 13 (23.6%) | 12 (21.8%) | 8 (14.5%) | 6 (10.9%) | 1 (1.8%) | 0 |

---

## Alert Status

| Metric | Threshold | Current Value | Status |
|--------|-----------|:-------------:|:------:|
| Incident-Driven Rate | >35% | 20.75% | 🟢 |
| Normal Planned % | >60% | 75.86% | 🔴 |
| Fast Track % | >5% | 10.9% | 🔴 |
| Emergency per period | >3 | 0 | 🟢 |
| M2.4 Standard % | >60% target | 45.3% | 🟡 below target |
| M2.5 Emergency Accuracy | >95% target | N/A | — |

---

## Data Gaps & Investigation Notes

### Lead Time (M2.1) — Needs Validation
- `LEADTIME (Days)` calculated column on RFC_DISTINCT shows avg 1.34 days, median 0 across all types (Apr 13–28)
- M2.1 baseline is 16 days for Normal Changes specifically
- Discrepancy likely because: (1) column includes Standard Changes which auto-resolve fast, (2) baseline methodology may differ from calculated column
- **Action:** Query `LEADTIME (Days)` filtered to Normal Changes only. Compare with time-in-status sum: Submitted-to-CAB (11.8h) + Approved-by-CAB (30.4h) + Implementing (41.3h) ≈ 83.5h ≈ 3.5 days for this period
- **Action:** Validate what `LEADTIME (Days)` calculates — creation to resolution? creation to implementation?

### First-Pass Approval (M6.2b) — Definition Pending
- Concept agreed: "approved without being returned for rework"
- No Jira field or status transition currently captures this
- Potential proxy: % of RFCs that go Draft → Submitted → Approved without cycling back
- **Action:** Define with Laura, implement Jira tracking

### Historical Data Gaps
- Feb 19 and Mar periods: only partial data extracted from Confluence reports
- Apr 2: Emergency compliance unknown (no validation performed)
- Pre-Apr 16: Incident-Driven Rate, Fast Track %, execution counts not available from Confluence
- **Mitigation:** This log accumulates going forward. Historical gaps won't grow.

---

*Last updated: 2026-04-24 (seeded from Apr 30 dry run data)*
