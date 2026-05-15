# Ops Review — Speaking Notes
*Intro framing + slides 3 (Method 2) and 6 (Method 3) · 2026-05-14*

Copy these into the Google Slides speaker notes pane. Roughly 60–90 seconds each.

---

## Intro / framing (use on the transition slide before slide 3)

A different shape this week. Our retrospective and Change Management data will go out offline — you'll have it in your inboxes ahead of the next cycle. We're using today's slot differently.

We want to bring you a high-level view of the top methods in Process Engineering's V2MOM. Our goal is to accelerate organizational change management on the work we're driving, and to minimize the impact on your teams when these changes start landing. The way we do that is by sharing our goals in advance — so the direction is visible, the trade-offs are surfaced, and we can shape the path together before any of it shows up as a process change you're absorbing.

Two methods today. Method 2 — Transform Change Management. Method 3 — Incident Response Resilience.

---

## Slide 3 — Method 2: Transform Change Management

**Open**

Method 2 is how we close what we call the Invisible Risk Surface. Every approved change today can fan out into multiple manual mutations on production rings. Last year, 731 RFCs produced 992 manual mutations — a 1.35x multiplier on what one approval actually authorizes. Each of those executions skips the SDLC's confidence checks because the approval happens upstream.

**Pillars**

We're attacking that across three pillars.

**Pipeline Integrity** unifies the Change Catalog and locks accountability across the four CM roles. The segregation of duties we have today created an unintended gap — no single role is fully equipped to assess risk end-to-end. We're closing that.

**Standard Promotion** is the path for mature Normal changes to graduate to Standards through a discovery ritual and lifecycle automation. The intent is that routine work flows through automation, not through SRE toil.

**CFR Correlation** links failures to the asset-version that caused them. CFR stops being a number we caveat every time, and becomes a number Engineering Leadership can act on.

**Success measures**

Our targets: a 30% reduction in review-and-approval lead time — today's baseline is 45 hours. 60% of changes routed through the Standard track. 90% CFR correlation accuracy. And less than 5% of changes happening outside the catalog.

What this looks like operationally: every change traces to a catalog article; each role has sharp scope and a refusal mechanism; standards run through automation; CFR is a signal we trust; and audit evidence becomes a query, not a manual reconciliation.

**Close**

The unblocker is Pipeline Integrity — without the catalog, nothing else downstream lands safely. Laura is in flight on the Foundations work: we've collapsed 1,800 raw operation types into 26 categories and 61 mapped operations. The reviewer validation ask is already in motion, kicked off this week.

---

## Slide 6 — Method 3: Incident Response Resilience

**Open**

Method 3 is about resilience. Not just responding faster — classifying cleaner, responding transparently, and learning systematically. Today we have gaps on all three axes. Alerts that should be incidents never get formally declared. System-wide incidents close without proper communications. And retrospectives stretch into months, so by the time action items land, the context is gone.

**Pillars**

Three pillars.

**Classify Intake** gives Service Incidents and Support Cases their own operating models. Two new framings we want to land here. First, we want to separate real Service Incidents from Support Cases — each carries different ownership and different OLAs. Second, we want a defined alert-to-incident path so we can formally declare false negatives. Today, alerts get worked silently through Jira comments instead of triggering the coordinated mobilization an incident requires. This pillar covers M3.3 — Triage — and M3.6 — Event Management.

**Govern Response** is about operational visibility during an incident. Failure Management Governance and Status Page Governance — so every system-wide incident has the right comms posture, internal and external. M3.1 and M3.2.

**Close the Loop** is the learning system. Team-led retrospectives and Problem Management. Recurring failures convert into structural fixes, not stale action items. M3.4 and M3.5.

**Success measures**

Our targets: 30-minute public MTTA. Triage accuracy above 80%. Problem coverage above 90%. Average RCA lead time of 14 days — versus today's 72 days.

What this looks like operationally: Service Incidents and Support Cases each have a defined operating model and clear OLAs; alerts have a path to declaration with no silent false negatives; the Status Page reflects every system-wide incident lifecycle; retros are team-led and closed within target lead time; and Problem Management closes the loop on what's recurring.

**Close**

The leverage points are Classify Intake and Close the Loop. If we get triage and learning right, the rest follows. M3.3 is already in flight under Inês, M3.4 Problem Management is in progress, and M3.5 Retrospective Transformation has the new team-led model defined. We'll come back with the deeper measurement story when the empirical work is ready to land.

---

## Optional backup numbers (only if asked)

**Method 2:**
- 731 RFCs → 992 manual mutations on production rings (2025, 1.35x; 1.38x for Normal Changes)
- 2026 trajectory exceeds 1,140
- Review + approval lead time: 18h review + 27h approval = 45h
- 70.59h average "Implementing" status after the change is actually done

**Method 3:**
- 44% of system-wide incidents had zero internal comms (Oct 2025 – Jan 2026)
- 21 of 39 never received a "Resolved" update
- Only 7% followed the full lifecycle (Investigating → Identified → Monitoring → Resolved)
- 72-day average retrospective lead time (11d to assign Commander + 64d to draft and approve)
- 63% of retros reviewed by just 2 people
