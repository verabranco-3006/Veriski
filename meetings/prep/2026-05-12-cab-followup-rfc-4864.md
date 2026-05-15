# CAB Follow-up — RFC-4864 (Spacelift Governance Catalog)

**Date:** 12-May-2026 (offline alignment closing discussion started in CAB on 07-May-2026)
**RFC:** [RFC-4864](https://outsystemsrd.atlassian.net/browse/RFC-4864)
**Catalog (source of truth):** [\[Standard\] Spacelift Governance](https://outsystemsrd.atlassian.net/wiki/spaces/RRE/pages/6250790958/Standard+Spacelift+Governance)
**CAB Owner:** Vera Branco
**Requester / Lead:** Leandro Galrinho (Release Engineering Alpha)
**Approver:** João Brandão
**Reviewers contributing:** Fernando Alexandre, Hélder Marques, Gavin Behr, Arturo Riter, Rui Eugénio, Vera Branco

---

## Context

RFC-4864 was tabled at the CAB on 07-May-2026 to align on the Spacelift Governance catalog. The discussion continued offline in [#odc_cab_approvals](https://outsystems.enterprise.slack.com/archives/C0617T4EV3R) between 07-May-2026 and 12-May-2026. The CAB scheduled for 12-May-2026 was cancelled — alignment was reached offline and Leandro consolidated the outcomes into the catalog document.

The catalog (linked above) is now the source of truth. The numbering below mirrors the catalog, not the working numbering used during the Slack threads.

---

## Decisions — Spacelift Governance Catalog (12 change types)

All 12 change types follow the same workflow: SRFC → PR against `spacelift-admin-stack` → Spacelift proposed plan reviewed → merge → RFC closed. The Implementation Team is **Release Engineering Alpha** for assets outside Base Spacelift, and the **Owner Team** for assets inside Base Spacelift (the requester executes themselves).

| # | Change Type | Classification |
|---|---|---|
| 1 | Provision New Spacelift Stacks | **Standard** (ODC and non-ODC) |
| 2 | Edit Existing Spacelift Stack | **Standard for non-ODC.** ODC follows the [Normal procedure](https://outsystemsrd.atlassian.net/wiki/spaces/RRE/pages/6361055454) — hidden side-effects on the next run after the edit |
| 3 | Delete Spacelift Stack | **Standard** (ODC and non-ODC) — procedure requires disabling `protect_from_deletion` first in a separate PR |
| 4 | Provision New Spacelift Spaces | **Standard** (ODC and non-ODC) |
| 5 | Delete Spacelift Space | **Standard** (ODC and non-ODC) — Spacelift enforces empty-space precondition |
| 6 | Add New Spacelift Context or Environment Variable | **Standard** (ODC and non-ODC) — net-new resources only |
| 7 | Update / Remove Spacelift Context / Variable, or Assign Context to Stack | **Standard for non-ODC.** ODC follows the [Normal procedure](https://outsystemsrd.atlassian.net/wiki/spaces/RRE/pages/6361383025) — affects every attached stack on next run |
| 8 | Add Spacelift Terraform Module | **Standard** (ODC and non-ODC) |
| 9 | Update or Delete Spacelift Terraform Module | **Standard for non-ODC.** ODC follows the [Normal procedure](https://outsystemsrd.atlassian.net/wiki/spaces/RRE/pages/6362038472) |
| 10 | Onboard New Team via Base Spacelift Module | **Standard** (ODC and non-ODC) — module-driven, auto-assigns Power User scope to the team's own space |
| 11 | Update Base Spacelift Onboarding Module Defaults | **Standard** — affects only the admin stacks created by the onboarding module, not customer infrastructure |
| 12 | Worker Stack Configuration Change | **Standard** — worst case is no workers running stacks; no production infra is mutated by the change itself |

**Pattern:** the three change types with an ODC carve-out (2, 7, 9) are those where the operation can mutate state used by other stacks / runs on a subsequent execution. Everything else is Standard regardless of scope.

---

## Process decision — RFC ownership when Release Engineering executes for another team

This was the standout question raised during the offline discussion.

- **The requesting team owns the RFC.** Release Engineering is the implementer (for assets outside Base Spacelift) or supports the team's own execution (for assets inside Base Spacelift).
- Release Engineering can help the requester write the RFC — implementation plan, rollback procedure — but ownership stays with the requester.
- The **catalog article is the generic procedure description**, reusable across teams. Each specific RFC instantiates the catalog with its own inputs.
- Release Engineering is effectively the **last-level reviewer at execution time** — by the time the RFC reaches them, CAB has already validated it.
- Over time, repeat-requester teams will gain autonomy to author their own RFCs without help.

This principle is codified in the catalog under "How Release Engineering Works with Requesting Teams" and "ODC vs. Non-ODC Assets".

---

## Quorum & sign-off

- All change types have at least **two reviewers** in agreement. Vera's sign-off on 10-May-2026 closed the gap on the change types that previously had only one.
- Reactions on each thread in #odc_cab_approvals record the per-reviewer agreement (auditable).
- Approver: João Brandão.

---

## Next steps

| # | Action | Owner | Status |
|---|---|---|---|
| 1 | Update the Spacelift Governance catalog with the agreed classifications + new change types (Edit, Delete, Module update/delete carve-outs, Base Spacelift onboarding, Worker stack) | Leandro Galrinho | **Done** — catalog last updated 15-May-2026 |
| 2 | Repost catalog link in #odc_cab_approvals for designated reviewer sign-off | Leandro Galrinho | Pending |
| 3 | Designated reviewer signs off on the catalog | Vera Branco to nominate | Pending |
| 4 | Approval transition on RFC-4864 | João Brandão | Pending |
| 5 | Attach this summary to RFC-4864 as a comment for audit | Vera Branco | Today |

---

## RFC-4864 comment (ready to paste into Jira)

> **CAB follow-up — alignment closed offline on 12-May-2026. Catalog updated and ready for sign-off.**
>
> The discussion started at the CAB meeting on 07-May-2026 continued in #odc_cab_approvals between 07-May-2026 and 12-May-2026. The CAB scheduled for 12-May-2026 was cancelled — alignment reached offline. The decisions are consolidated in the [Spacelift Governance catalog](https://outsystemsrd.atlassian.net/wiki/spaces/RRE/pages/6250790958/Standard+Spacelift+Governance) (12 change types).
>
> **Classification summary:**
> - **Standard for both ODC and non-ODC:** Provision Stacks (1), Delete Stack (3), Provision Spaces (4), Delete Space (5), Add Context/Variable (6), Add Terraform Module (8), Onboard Team via Base Spacelift (10), Update Base Spacelift Onboarding Defaults (11), Worker Stack Configuration Change (12).
> - **Standard for non-ODC; Normal for ODC** (carve-out due to side-effects on subsequent runs / attached stacks): Edit Existing Stack (2), Update/Remove Context-Variable / Attach Context (7), Update/Delete Terraform Module (9). Each ODC variant has its own Normal-change document linked from the catalog.
>
> **Process — RFC ownership:** the requesting team owns the RFC. Release Engineering is the implementer (or supports the team's own execution for Base Spacelift assets) and the last-level reviewer at execution time. The catalog article is the generic procedure; each RFC instantiates it with specific inputs. Codified in the catalog under "How Release Engineering Works with Requesting Teams" and "ODC vs. Non-ODC Assets".
>
> **Quorum:** All change types have at least two reviewers in agreement. Per-thread reactions in #odc_cab_approvals record the sign-offs. Reviewers contributing: Fernando Alexandre, Hélder Marques, Gavin Behr, Arturo Riter, Rui Eugénio, Vera Branco.
>
> **Next:** designated-reviewer sign-off on the consolidated catalog, then approval by João Brandão. Approver to confirm on this ticket.

---

## Thread references

- [Catalog working thread — Type 5 (working numbering): Add or Update Spacelift Policies](https://outsystems.slack.com/archives/C0617T4EV3R/p1778170323359269?thread_ts=1778170323.359269)
- [Catalog working thread — Type 6 (working numbering): Add or Update Spacelift Terraform Modules](https://outsystems.slack.com/archives/C0617T4EV3R/p1778170332913709?thread_ts=1778170332.913709)
- [Catalog working thread — Type 7 (working numbering): Onboard New Team via Base Spacelift Module](https://outsystems.slack.com/archives/C0617T4EV3R/p1778170343534729?thread_ts=1778170343.534729)
- [Catalog working thread — Type 8 (working numbering): Update Base Spacelift Onboarding Module Defaults](https://outsystems.slack.com/archives/C0617T4EV3R/p1778170352360249?thread_ts=1778170352.360249)
- [Catalog working thread — Type 9 (working numbering): Worker Stack Configuration Change](https://outsystems.slack.com/archives/C0617T4EV3R/p1778170360406849?thread_ts=1778170360.406849)
- [Catalog working thread — Type 10 (working numbering): Update Existing Spacelift Stack](https://outsystems.slack.com/archives/C0617T4EV3R/p1778232888720909?thread_ts=1778232888.720909)
- [Catalog working thread — Deletion operations](https://outsystems.slack.com/archives/C0617T4EV3R/p1778232916951429?thread_ts=1778232916.951429)
- [Main thread — quorum, RFC ownership, CAB cancellation](https://outsystems.slack.com/archives/C0617T4EV3R/p1778236242365439?thread_ts=1778236242.365439)
