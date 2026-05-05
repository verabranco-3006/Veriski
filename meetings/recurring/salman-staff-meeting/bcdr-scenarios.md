# BCDR Scenarios — Reference List

Real-world events to consider in our DR / response-drill scenario coverage. Relevant to Salman staff #3 (off-hours response drill, Axos follow-up) and the open apagão action from 2026-04-28.

---

## Strategy Context

The current BCDR strategy was designed in 2023 to glue into the only drill we'd run at the time, in support of the initial attestation. That has been the strategy presented since.

It is built on the assumption that OutSystems splits the ODC Service to customers into multiple Service Journeys, of which the two main ones are:

1. **App Runtime** — customers have apps available in Production delivering value to their end-users
2. **Publish & Stage** — customers are creating apps and staging them through to Production (up to the point they start delivering value to their end-users)

**The current BCDR document only covers Journey 1 (App Runtime).**

Since then, BCDR has been addressed in engineering only from a tactical perspective. SRE has been investing in bringing Chaos Engineering to the table, but it still needs to be consolidated cross-org, defined, tested, and executed.

---

## Real-World Scenarios

1. **AWS outage on North Virginia (US-EAST-1)** — 2025-10-20
2. **Power blackout affecting the Iberian Peninsula** ("apagão") — 2025-04-28
3. **AWS data center strikes in Bahrain (ME-SOUTH-1) and UAE (ME-CENTRAL-1)** — March 2026
