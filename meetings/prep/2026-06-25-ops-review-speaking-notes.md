# Ops Review — Speaking Notes
**Date:** June 25, 2026
**Time limit:** 4 minutes
**Source:** [Confluence report](https://outsystemsrd.atlassian.net/wiki/spaces/EEO/pages/6514638948/June+25+2026) (prepared by Laura)

---

## Opening — context (20 sec)

Each RFC generates on average nearly 2 production ring executions. 50 RFCs = 98 actual production deployments. That's the real risk exposure number. The 1.96 ratio is consistent with prior periods — so this isn't a new pattern, but in a high-volume period it amplifies everything.

---

## Finding 1 — Incident-Driven Rate (45 sec)

Incident-driven RFC rate hit 42%. That's 4 consecutive rises and we've crossed the 35% alert threshold. 21 of 50 RFCs were reactive — 4 Emergency, 13 Normal, 4 Standard.

This is structural: incident load translates directly into reactive change volume. The lever isn't controlling RFC behavior — it's reducing incidents. 

---

## Finding 2 — Emergency misuse (50 sec)

4 Emergency changes — above our <3 threshold. Compliance at 50%: RFC-5069 and RFC-5157 were legitimate. RFC-5157 is the model — OSALL scope, written approval, 3-day lead time, SLO breach. That's how Emergency should work.

The problem is RFC-5077 and RFC-5099 — both SRE Delta, both customer-specific domain fixes, no system-wide impact in either case.

RFC-5077 (RDINC-84588, GA ring) has no valid rationale for Emergency — customer-specific operation, no system-wide scope, no documented justification for the track used.

RFC-5099 (RDINC-84936, OSALL ring) is a different incident with the same behavior: 404 errors, 4 days later, different environment. It should have been a Normal Change — but was submitted as Emergency because of a Jira login issue that prevented submitting it correctly. That's a workaround for a tooling problem, not a compliance failure, but it exposes a gap: when the process breaks down, teams default to Emergency as the path of least resistance.

Two separate incidents, same behavior, same fix. Neither justified Emergency. 


---

## Numbers to have ready if challenged

| Metric | Value | Threshold |
|--------|-------|-----------|
| Total RFCs | 50 (+72%) | — |
| Incident-driven rate | 42% | <35% |
| Emergency count | 4 | <3 |
| Emergency compliance | 50% (2/4) | >95% |
| Standard Change % | 34% | >60% target |
| Fast Track % | 10% | <5% |
