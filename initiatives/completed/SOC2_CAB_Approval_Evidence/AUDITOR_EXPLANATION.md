# SOC2 Audit - CAB Approval Evidence

## Evidence Summary

**Total RFCs Requested:** 40
**RFCs Included in This Package:** 24
**Evidence Type:** CAB Approval Sign-Off

---

## Rationale for RFC Selection

This package contains **only Normal Request for Change tickets** (Issue Type: "Request For Change") that went through the formal Change Advisory Board (CAB) approval process.

### Issue Type Breakdown

| Issue Type | Count | CAB Approval Required? | Included in Package? |
|------------|-------|------------------------|---------------------|
| Request For Change | 24 | ✓ Yes | ✓ Yes |
| Standard Change | 13 | ✗ No (Pre-approved) | ✗ No |
| Emergency Request for Change | 1 | ✗ No (Post-review only) | ✗ No |

### Excluded RFCs and Justification

**Standard Changes (13 tickets):**
RFC-2642, RFC-3061, RFC-3139, RFC-3315, RFC-3375, RFC-3441, RFC-3497, RFC-3527, RFC-3532, RFC-3791, RFC-3865, RFC-3932, RFC-4207, RFC-4235, RFC-4263

*Justification:* Standard Changes are pre-approved change types that follow documented procedures and do not require individual CAB review and approval.

**Emergency Request for Change (1 ticket):**
RFC-4345

*Justification:* Emergency changes bypass the normal CAB approval process due to urgency and are subject to post-implementation review instead.

---

## CAB Approval Evidence Location

For each Normal RFC included in this package, CAB approval is evidenced by the explicit sign-off on the following fields:

1. **Reviewer Field** - Located in the "CAB Review" tab, shows who reviewed the change request
2. **Approver Field** - Located in the "CAB Review" tab, shows who approved the change request
3. **Decision Date** - Located in the "CAB Review" tab, shows when the approval decision was made

These fields represent the explicit sign-off from authorized personnel following the CAB review process.

---

## Included Normal RFCs (24)

1. RFC-2704 - Gain PowerUser on DEV Management Stamp only to Perform POC Cleanup
2. RFC-2713 - Remove override on Customer Production Database limits
3. RFC-2761 - Request PIM access to PowerUser in negative Rings to monitor NATS messages live
4. RFC-2839 - Request memory dumps from specific customer application
5. RFC-2901 - Pegasus - update dependencies
6. RFC-2986 - runnp-ga-me-ce-1-01 - fix nats2avativa deployment replicas
7. RFC-2993 - Delete runtime Metadata CRs without an AppDeployment (Negative Rings)
8. RFC-3134 - Debug Gloo in stamps plat-osall-us-east-1-01 and id-osall-us-east-1-01
9. RFC-3136 - Add /mentor/appgenerator* behaviour to CDN
10. RFC-3208 - Istio Upgrade to Version 1.25.3
11. RFC-3437 - Nats2crd configuration change - Singapore
12. RFC-3443 - Rollback runtime-operator to previous validated version in EA (failed bake)
13. RFC-3449 - Run Realm Replay on a specific tenant
14. RFC-3465 - Create new parameters for Agent Workbench AI Models Trials in SRE Shared Managed Account
15. RFC-3517 - Register RUNNP regions accounts DNS into the main DNS Route53 hosted zone
16. RFC-3562 - Release Engineering - Prepare Pegasus CD to send events to create jira incidents
17. RFC-3639 - [Normal] Delete NACK CRs in ring TEST
18. RFC-3640 - NATS Out o sync - runp-ga-us-east-1-01
19. RFC-3659 - Rollback changes on RFC-3524
20. RFC-3691 - [Normal] Enable redirect to AppGenerator on Mentor for ODC Portal for test tenants
21. RFC-3922 - Create SRE-managed Static Secrets for wiz-sensor (negative rings)
22. RFC-4186 - [FluxCD] Phase 1: Upgrade Flux to version 2.6.4 - Integrated Dev
23. RFC-4213 - Setting the Edition that is missing in some of tenants
24. RFC-4332 - Rollback frontend-build-worker DU v1.0.491 in ring 2 (aka EA)

---

**Prepared by:** Vera Branco, Team Lead - Process Engineering
**Date:** March 11, 2026
**Audit Period:** Q1 2025 - Q1 2026
