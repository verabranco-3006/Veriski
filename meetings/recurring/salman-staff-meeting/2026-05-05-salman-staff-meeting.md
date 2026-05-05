# Salman weekly staff meeting
*2026-05-05*

## Attendees
- Salman Malik, Anabela Cesário, Pedro Charola, Paulo Garcia, Vera Branco

## Notes

### Topic: Axos follow-ups (on the agenda — Salman explicitly asked to discuss #3 today)

**Email thread summary** — "Axos follow-ups", started by Salman 2026-05-01
To: Arul, Pedro Charola, Paulo Garcia, Vera (Luis Blando bcc)
12 messages through 2026-05-04

#### Background (Salman, 2026-05-01)

Salman and Luis Blando off a call with **Kevin Hearn, SVP of App Dev at Axos Bank** — big OS sponsor. Follow-up to a couple of outages that shook Axos's confidence (threads Woodson forwarded). Axos looking at expansion from ~$600K ARR to **~$3–5M over 4–5 yrs**. They run critical trading apps on ODC — high liability exposure, not pushing liability onto us, but need to trust we're well-architected and well-monitored.

---

#### #1 — "A container broke in ODC" (Kevin: "we picked it up before you did")

**Charola's analysis (2026-05-04):** Compiled overall analysis of all Axos ODC incidents escalated to Engineering — [Google Doc](https://docs.google.com/document/d/1RHU4kopE8duRXML8AJneW0rSd26TEdrdZKXiheyWGcc/edit?tab=t.0).

Likely incident — confirmed by Paulo Garcia: **#3320800** ([Zendesk](https://supportoutsystems.zendesk.com/agent/tickets/3320800)) / **RDINC-77425** (which is actually a GS RCA request, not an incident).

**Executive summary of the outage:**
- **2026-03-23** — Axos prod endpoint `AX_SignUpVerification_Service` fully down for **~3h 50min**
- Symptoms: persistent 503 on exposed API, application missing from ODC Portal deployment dropdown, portal showing nonsense deployment date `1990-01-01`
- **Not detected by OS internal monitoring — Axos discovered and reported it themselves via support ticket**
- Root cause: bug in **Asset Portfolio Service (APS)** owned by **Maestro team** — silently deleted deployment records from platform DB → build pipeline image-cleanup job removed associated container images from ECR → live K8s pods referencing deleted images → `ImagePullBackOff` on restart, no recovery
- Only mitigation: full redeploy from ODC Portal (no self-service re-push without new deployment)
- Bug fix shipped to GA via **RDMAST-2634**
- Two follow-up improvements committed to (mentioned on RDINC-77425):
  1. Proactive alerting for this class of failure
  2. Redesign image cleanup mechanism — event-driven instead of record-driven
- **Neither has a confirmed delivery date on record. Charola could not find any JIRA items on Maestro's board for these.** May exist in another format — needs confirmation.
- SRE not involved at the time — incident initially deemed customer-specific and resolved autonomously by GS. Maestro has no embedded SRE; Charola will link his team to Maestro.

**Salman's follow-up question:** Have we updated testing/monitoring to catch this class of bug? Do we have a queue/backlog mechanism so new testing or monitoring requirements get developed?

**Charola's response (split of work):**
- Testing → QA input needed; Arul to follow up with Vijay
- Monitoring → should be action on Maestro's backlog; Charola will link his team to Maestro

**Outstanding on #1:**
- Monitoring: why didn't we detect this — *with Charola*
- Testing: what was done to strengthen quality — *Arul to follow up w/ Vijay/QA*
- The two Maestro action items — *Vera asked by Charola to confirm if logged/planned.* **Confirmed via Nuno Ferreira (Maestro):**
  1. **Application Image Cleanup** — to be led by **Build Services** — [RBST-3358](https://outsystemsrd.atlassian.net/browse/RBST-3358)
  2. **Remove root-cause logic that was silently deleting records on customer GET to an endpoint** — [RDMAST-2638](https://outsystemsrd.atlassian.net/browse/RDMAST-2638)

---

#### #2 — Cloudflare WAF outage (ticket 3332746, "Apw application not loading on Production")

**Charola met w/ Nuno Silva (GS), Nick Ceballos (Security), Bruno Batista (Eng), Pedro Oliveira (PM):**
- Cloud Security has now ensured all Cloudflare CIDR blocks won't be blocked (contrary to what the RCA said — only the specific reported CIDR had been done)
- Other follow-ups (not directly customer-facing for Axos): improve brute-force protection at O11 Cloud, expand the non-blocking mechanism to other known CDN / reverse-proxy providers

---

#### #3 — Reaction speed on critical outages (Vera's item)

- Axos nervous: even with Premium Support, doubt we'd react fast enough on critical platform outages
- Salman's idea: run a drill — simulate outage at 3am on a weekend, measure whether we meet expectations
- Salman: *"this may be analogous to the testing we need to do for full disaster recovery albeit much tighter in scope. Let's discuss in our Tuesday staff with Paulo Garcia."*
- **Charola's view:** *"me, Paulo Garcia and Vera need to talk to come up with a plan."*

**Vera's reply (2026-05-01):** We've never run a similar coordination/mobilization scenario off-hours. Last year's BCDR drills tested 2 scenarios (deleted tenant in ODC, deleted DB in O11) — both in-hours. Agreed it deserves a one-off coordinated end-to-end test including off-hours condition.


#### Prep — talking points for today

- Confirm trio (Vera + Charola + Paulo Garcia) as the working group on #3 — schedule the follow-up
- Frame as **off-hours response drill**, distinct from full BCDR (tighter scope, response-time focus)
- Open questions to surface in today's meeting:
  - Scope: customer-specific drill (Axos) vs generic critical-customer pattern?
  - Trigger: surprise simulation vs scheduled?
  - Participants: SRE on-call + GS on-call + PE coordination — anyone else?
  - Success criteria: time-to-acknowledge, time-to-engage SRE, time-to-customer-comms
  - Cadence: one-off proof point vs recurring drill series?
  - Connection to broader BCDR program — fold this in or run as separate motion?
  - Apagão scenario (open from 2026-04-28) — fold into same drill series or keep separate?

#### Also relevant for me to flag

- Charola's ask on **Maestro action items** (#1) — accept/clarify scope. Likely lives at the intersection of Failure Management (M3.1, Inês) and how we track post-incident commitments. This is a concrete instance of the broken continuous-improvement loop I raised in the skip-level prep ("findings don't systematically convert into actions teams execute and PE can track").
- Pattern worth naming: **monitoring gap + missing JIRA tracking of committed follow-ups** is exactly the failure mode PE exists to close.

---

### Topic: Operations Review — format (to add to agenda if there's time)

**Goal:** Align with Salman, Charola, Anabela, and Paulo Garcia on the Operations Review format — what we want it to be, what it shouldn't be, and what changes to make next.

**Context:**
- Bi-weekly meeting PE co-leads with SRE, Quality, Release Engineering, Product Ops
- Last one delivered 2026-04-30 — PE contributed retrospective + Change Management sections
- Already raised in the skip-level prep with Salman: current perception is a "blaming meeting", not a learning/accountability mechanism
- What PE is doing today: streamlining its own participation in the meeting
- Visible gaps in the Operations Review itself:
  - Missing important team representatives (e.g., O11)
  - Uneven level of preparedness across presenting groups — some come well prepared with findings, root causes, and action plans supported by the data they own; others come with long lists of Jira tickets and dashboards with data they're not able to explain

**Ask:**
- Salman's read on the current format and where he sees it landing in his mandate
- Whether to use this forum to make targeted format changes, or push to a separate working session with the co-leads
- Concrete next step: who owns the format proposal, by when

---

## Meeting Notes — what was discussed

### 1) Sentry — Workleap & customers

- Sentry installation in some customers is done by SRE today
- Needs more alignment between SRE and Global Support — installation must be as automated as possible
- Path forward:
  - Installation could be done by **Global Support** if the **risk is low** and the **customer fills in all the pre-requisites**
  - The **full installment** requires SRE to move capacity to execute parts of the process
- **CISO has plans to review Sentry as a product**

### 3) BCDR and outage testing (Axos #3)

- Agreed: a separate meeting will be set up to cover BCDR and outage testing

### 4) Operations Review

- Agreed: a separate meeting will be set up to cover the Operations Review format

## Action Items

- [ ] Sentry — work with SRE / Global Support on the alignment of who installs what (low-risk vs full installment) and automation path
- [ ] Track CISO's plan to review Sentry as a product - book a dedicated session with Márcia Xavier
- [ ] Schedule the BCDR + outage testing meeting
- [ ] Schedule the Operations Review format meeting

