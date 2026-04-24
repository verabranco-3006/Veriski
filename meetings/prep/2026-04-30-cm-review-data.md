# Change Management Review Data -- April 30, 2026
**Review period:** April 13 to April 28, 2026
**Total RFCs:** 53 (24 Standard, 29 Normal, 0 Emergency)
**Total Change Executions:** 162 (162 with ring assigned, 0 ring not assigned)

---

## Key findings

### 1. Incident-Driven RFC Rate: New Low at 20.75%

11 of 53 RFCs (20.75%) were linked to incidents — **down 4.7 pp from last period** and the lowest rate observed in the tracking window. This continues the downward trend that started in March.

| Period | Incident-Driven % | Change |
|--------|--------------------|--------|
| March 19, 2026 | -- | -- |
| April 2, 2026 | -- | -- |
| April 16, 2026 | 25.45% | -- |
| **April 30, 2026** | **20.75%** | **-4.70 pp** |

Well below the 35% alert threshold. The breakdown by change type:
- Normal Changes: 7 of 29 incident-driven (24.14%), 22 planned (75.86%)
- Standard Changes: 4 of 24 incident-driven (16.67%), 20 planned (83.33%)

**Why it matters:** Lower incident-driven rate means more of our change volume is planned work rather than reactive fixes. The question is whether planned Normal Changes are genuinely manual operations or automation candidates (see finding #2).

### 2. Normal Planned Usage: Stable at ~76% — Still Elevated

75.86% of Normal Changes are for planned operations, virtually unchanged from 76.92% last period.

| Period | Normal Planned % | Change |
|--------|------------------|--------|
| February 19, 2026 | 66.67% | -- |
| March 5, 2026 | 65.00% | -1.67 pp |
| March 19, 2026 | 55.56% | -9.44 pp |
| April 2, 2026 | 64.71% | +9.15 pp |
| April 16, 2026 | 76.92% | +12.21 pp |
| **April 30, 2026** | **75.86%** | **-1.06 pp** |

Above the 60% alert threshold for the second consecutive period. This is the "Shadow SDLC" pattern — planned work routed through Normal Changes instead of automated pipelines.

**What we're doing about it:** V2MOM Initiative M2.1 (Ensure Pipeline Integrity) — the Change Catalog consolidation will provide taxonomy to identify which planned operations are automation candidates vs inherently manual.

### 3. Emergency Volume: Zero — Dramatic Drop

No Emergency RFCs created during this period, down from 6 in the previous period (the highest in 3 months).

| Period | Emergency Count | Change |
|--------|-----------------|--------|
| February 19, 2026 | 4 | -- |
| March 5, 2026 | 5 | +1 |
| March 19, 2026 | 1 | -4 |
| April 2, 2026 | 2 | +1 |
| April 16, 2026 | 6 | +4 |
| **April 30, 2026** | **0** | **-6** |

**Why it matters:** While positive, this could be a statistical fluctuation given the short period. Worth monitoring — if the previous period's spike of 6 was an anomaly, we may be returning to baseline. No compliance checks needed this period (no ERFCs to validate).

---

## Metrics

### RFC volume by type

| Type | Count | % | Previous (Apr 16) | Change |
|------|-------|---|---------------------|--------|
| Standard | 24 | 45.3% | -- | -- |
| Normal | 29 | 54.7% | -- | -- |
| Emergency | 0 | 0% | 6 | -6 |
| **Total** | **53** | **100%** | -- | -- |

### Incident-Driven RFC Rate

| Metric | Value |
|--------|-------|
| Linked to incidents | 11 (20.75%) |
| Not linked | 42 |
| Approved | 41 |
| Ongoing | 11 |

### Change Type x Usage (Incident-Driven vs Planned)

| Type | Incident-Driven | Planned | Total | Planned % |
|------|-----------------|---------|-------|-----------|
| Normal Change | 7 | 22 | 29 | 75.86% |
| Standard Change | 4 | 20 | 24 | 83.33% |
| Emergency Change | 0 | 0 | 0 | -- |
| **Total** | **11** | **42** | **53** | **79.25%** |

### Risk Classification

| Risk | Count | % |
|------|-------|---|
| Low | 47 | 88.7% |
| Medium | 5 | 9.4% |
| High | 1 | 1.9% |

No risk paradoxes (Low Risk + Emergency) — zero Emergency Changes in period.

### Ring Distribution (Change Executions)

| Ring | Count | % |
|------|-------|---|
| ring+3/ga | 36 | 22.2% |
| ring+1/osall | 30 | 18.5% |
| ring+2/ea | 28 | 17.3% |
| ring-1/stage | 19 | 11.7% |
| ring-2/test | 19 | 11.7% |
| ring-4/lab | 12 | 7.4% |
| ring-3/dev | 10 | 6.2% |
| ring0/osrd | 8 | 4.9% |
| **Total** | **162** | **100%** |

Note: GA ring has highest execution count. Distribution across production rings (osall/ea/ga): 94 executions (58%) vs lower rings: 68 (42%).

### Status Distribution

| Status | Count | % |
|--------|-------|---|
| Completed | 26 | 49.1% |
| Implementing | 11 | 20.8% |
| Cancelled | 5 | 9.4% |
| Approved by CAB | 4 | 7.5% |
| Submitted to CAB | 3 | 5.7% |
| Draft | 2 | 3.8% |
| Reviewed - Ready for Approval | 2 | 3.8% |

### Change Category

| Category | Count | % |
|----------|-------|---|
| Change Configuration | 15 | 27.3% |
| Change Infrastructure | 13 | 23.6% |
| Restart | 12 | 21.8% |
| Other Write Operation | 8 | 14.5% |
| **Fast Track** | **6** | **10.9%** |
| Retry | 1 | 1.8% |

**Fast Track alert:** 6 Fast Tracks (10.9%) — above the 5% alert threshold (M2.2). These are rushed deployments skipping bake periods.

### Lead Time — Normal Changes (M2.1)

| Metric | Value |
|--------|-------|
| Mean lead time (days) | ⚠️ Needs validation — all-type avg was 1.34 days, needs Normal-only query |
| Median lead time (days) | — |
| Max lead time (days) | — |
| Normal RFC count | 29 |
| **M2.1 Baseline** | **16 days** |
| **M2.1 Target** | **11 days (-30%)** |

### Lead Time — Workflow Breakdown (all types, avg hours)

| Stage | Avg Hours |
|-------|-----------|
| Submitted to CAB | 11.8 |
| Approved by CAB (wait) | 30.4 |
| Implementing | 41.3 |

> Note: Time-in-status data was queried across all RFC types, not filtered to Normal only. Needs re-query for M2.1 tracking.

### Trend comparison (V2MOM aligned)

| Metric | V2MOM | Apr 2 | Apr 16 | Apr 30 (current) | Target | Change vs previous |
|--------|-------|-------|--------|-------------------|--------|--------------------|
| Normal Lead Time (days) | M2.1 | -- | -- | ⚠️ TBD | 11 days | -- |
| Standard Change % | M2.4 | -- | 49.6% | 45.3% | >60% | -4.3 pp |
| Emergency Accuracy | M2.5 | -- | ~67% | N/A (0 ERFCs) | >95% | -- |
| Incident-Driven RFC Rate | — | -- | 25.45% | 20.75% | <35% | -4.70 pp |
| Normal Planned % | M2.2a proxy | 64.71% | 76.92% | 75.86% | — | -1.06 pp |
| Fast Track % | M2.2 | -- | -- | 10.9% | <5% | -- |
| Emergency count | — | 2 | 6 | 0 | <3 | -6 |

---

## Compliance signals

- **Emergency without system-wide impact:** N/A — 0 Emergency Changes in period
- **Risk paradoxes (Low Risk + Emergency):** None
- **Fast Track usage:** 6 (10.9%) — above 5% threshold. Needs detail review (which teams, which changes)

## What's going well

- Incident-driven rate at historic low (20.75%) — reactive change volume continues to decrease
- Zero Emergency Changes — process discipline or quieter period, worth monitoring
- 49.1% of RFCs already Completed — healthy throughput
- All 162 executions have ring assignments — no "Ring not assigned" gaps

---

## Data gaps

- **Lead time (M2.1):** `LEADTIME (Days)` column queried across all types (avg 1.34 days). Needs Normal-only query to compare against 16-day baseline. Discrepancy suggests Standard Changes with near-zero lead time are pulling the average down.
- **Lead time workflow breakdown:** Time-in-status averages not filtered to Normal Changes — need re-query.
- **First-Pass Approval (M6.2b):** No tracking mechanism in place. Definition agreed but Jira field/transition not implemented.
- **Standard Change % (M2.4) trend:** Only Apr 16 data available from Confluence (49.6%). Earlier periods have total-level data only from V2MOM measurements file.
- **Previous period totals:** Apr 2 and earlier periods lack RFC/execution totals for volume trend — mitigated going forward by running metrics log (`metrics/cm-review-metrics.md`).
- **Fast Track history:** No previous period data for trend — first time tracked. Running metrics log will accumulate going forward.
