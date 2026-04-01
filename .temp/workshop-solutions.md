# Global Support & Engineering Workshop - Solution Tracking

**Workshop Dates:** March 30-31, 2026

**Purpose:** Track problem statements, impacts, and proposed solutions for GS-Engineering alignment challenges

**Slidedeck for the Workshop:** https://docs.google.com/presentation/d/1pj-5kVmiR4jErRKJxZT7mGKcsL6o674XL69IlCSyVlU/edit?slide=id.g141f332568c_0_101#slide=id.g141f332568c_0_101

---

## Challenge #1 — Operating Models to Handle Customer Disruptions

### Problem Statement

Service incidents and support cases are conflated in the current escalation model.

- Severity models between Engineering and GS are not aligned
- There is no formal alignment on when/how to involve Engineering in CritSits
- No formal process or alignment to deliver the 5-day SLA RCAs for CritSits
- Lack of clarity on how to engage Engineering during weekends if needed

### Impact Description

**On Customers:** Potential delays and suboptimal experience for Premium Support customers during the highest stake moments, leading to dissatisfaction with the service and potentially increasing the risk of Premium Support churn.

**On Engineering & SRE:** Confused Reporting and Metric Misalignment - The process fails to clearly differentiate between a customer support case and a true service incident (system-wide issue).

### Workshop Outcomes

**What we agree on:**
- ✅ Separate the models for service incidents from Support Cases

**What we are NOT agreeing on:**
- ❌ There is no agreement on the Engineering coverage for handling high-urgent support cases
- ❌ GS requirement - Support Cases coverage 24x7 on Engineering for high and urgent escalated support cases

**Parking Lot:**
- 🅿️ CritSit definition - moved to Challenge #7 for Engineering Leadership discussion

### Decisions Needed

- [ ] Define clear separation between Service Incidents and Support Cases (AGREED - to be documented)
- [ ] Define Engineering coverage model for high/urgent support cases (NO AGREEMENT - requires escalation)
- [ ] Resolve 24x7 coverage requirement for support cases

---

## Challenge #2 — Inconsistent Customer Communication on O11

### Problem Statement

SRE continues to manage customer communications during incident response and request fulfillment for O11.

### Impact Description

**On Customers:** Inconsistent communication quality, unclear single point of contact

**On SRE:** Time spent on customer-facing activities instead of technical resolution, role confusion

### Workshop Outcomes

**What we agree on:**
- ✅ Communication handover to Global Support (timeline to be agreed upon)

**What needs alignment:**
- 🔄 Timeline for transition with clear milestones
- 🔄 Training and documentation support needed from SRE

### Decisions Needed

- [ ] GS commits to owning customer communications for O11 incidents and request fulfillment (AGREED)
- [ ] Define and agree on timeline for transition
- [ ] Establish training and documentation requirements

---

## Challenge #3 — Missing Collaborative Learning from Incidents and Support Cases

### Problem Statement

At this point Post-mortems/RCAs are not consistently delivered via collaboration between GS and SRE/Engineering. Instead, mainly due to operational misalignment and pressure, it's siloed.

GS leads the customer experience, incident process, communication portion. While SRE/Engineering lead the technical root cause and improvement (making sure it doesn't happen again). There have been no collaboration within this framework.

There is also lack of Protocol to address CritSit RCAs (under Premium Support offer).

Lack of clear ownership of RCAs requested by customers on monitoring related issues.

### Impact Description

**On Customers:** Delays in receiving RCA communications, inconsistent experience, sub-optimal RCA.

**On Engineering:** We need to rebalance our time toward product development by tightening alignment between SRE, and customer expectations.

### Workshop Outcomes

**What we agree on:**
- ✅ Global Support should participate as impacted team on Retrospective process to provide their feedback
- ✅ Problem Management must be leveraged as action item follow-up mechanism
- ✅ All the incidents posted on the status page must go through an RCA

**What needs alignment:**
- 🔄 Criteria and scenarios for Service Incidents
- 🔄 OLAs for Problem Management and RCA key moments

**Next Steps:**
- 📋 Review the full operating model (Service Assurance + Process Engineering)

### Decisions Needed

- [ ] Global Support participates in Retrospectives as impacted team (AGREED)
- [ ] Problem Management as follow-up mechanism (AGREED)
- [ ] All status page incidents require RCA (AGREED)
- [ ] Define criteria and scenarios for Service Incidents
- [ ] Establish OLAs for Problem Management and RCA key moments

---

## Challenge #4 — Service Incidents Are Failing to Communicate Effectively

### Problem Statement

Time to acknowledge incidents on Status Page higher than expected.

Time to public post mortem is higher than expected.

Quality of status page communications inconsistent.

The necessity of having a VS Leader or Engineering Manager acting as the IC Leader is frequently questioned. Since the Incident Commander (SRE) already holds the full technical context required for updates, the VS/EM role is often perceived as a redundant intermediary.

### Impact Description

**On Engineering:** Role redundancy and toil—VS/EM pulled into on-call for IC Leader role, creating inefficient dependency and communication overhead

**On SRE:** Forced to coordinate through VS/EM intermediaries when they already hold the full technical context needed for updates

**On Customers:** Direct impact on External Status Page updates due to internal communication failures, information vacuum on root cause identification.

### Workshop Outcomes

**What we agree on:**
- ✅ Remove the internal communication layer from the process
- ✅ Review communication automations in place for leadership (Process Engineering + SRE)
- ✅ Create deterministic way to enable Global Support on how to declare service incidents
- ✅ A service incident can be an O11 single customer affected
- ✅ Process-wide, incident communication must be treated as first-class citizen (automated and AI'ed as possible)

**What needs alignment:**
- 🔄 Notification mechanism from Engineering to GS when there is suspects of system wide impact (incidents detected on Engineering without customer impact)

### Decisions Needed

- [ ] Remove VS/EM as IC Leader—SRE owns incident communication directly (AGREED)
- [ ] Review and improve communication automations (AGREED - Process Engineering + SRE)
- [ ] Create deterministic process for GS to declare service incidents (AGREED)
- [ ] Single customer O11 incidents can be service incidents (AGREED)
- [ ] Incident communication as first-class citizen with automation (AGREED)
- [ ] Define notification mechanism for Engineering-detected incidents without customer impact

---

## Challenge #5 — Higher Resolution Times Than Expected

### Problem Statement

The strong dependency on Engineering for ODC incident resolution means that Engineering bottlenecks directly affect GS's ability to restore service efficiently.

As the rate of cases escalated to Engineering increases, more resolution time accumulates outside GS control, driving higher MTTR.

### Impact Description

**On GS:** Increased dependency on Engineering delays incident resolution, negatively impacting SLA performance and customer confidence.

**On Engineering:** A higher volume of escalated cases creates additional load, which can further increase bottlenecks and compound MTTR across incidents.

### Workshop Outcomes

**What we agree on:**
- ✅ OLAs as a governing mechanism for commitment for Support Cases
- ✅ Global Support needs to be as enabled to resolve support cases without escalating to Engineering

**What needs alignment:**
- 🔄 Which OLAs to implement and what to ask for Engineering
- 🔄 Targets of escalation per Support Scope Level (SSL)

**Next Steps:**
- 📋 Set a regular review between Engineering and Global Support (e.g. operational review)
- 📋 Provide visibility on Global Support on releases

### Decisions Needed

- [ ] Establish OLAs as governing mechanism for Support Cases (AGREED)
- [ ] Enable GS to resolve cases without Engineering escalation (AGREED)
- [ ] Define which OLAs to implement and Engineering commitments
- [ ] Set targets of escalation per Support Scope Level (SSL)
- [ ] Schedule regular Engineering-GS operational review
- [ ] Establish release visibility mechanism for GS

**V2MOM Alignment:** Links to V2MOM 7.1 - Reduce average time to recover from customer incidents by 50% by end of 2026 (target 12 hours)

---

## Challenge #6 — Issues on O11 Operating Models to Handle Higher Severity Cloud Incidents

### Problem Statement

GS escalates through process without formal warm hand-over. No effective collaboration during severe incidents. Many times, GS doesn't escalate an incident, most of the times in O11 — just the change they want SRE to execute.

Operational ownership is blurred, GS makes decisions on production changes without alignment with SRE/Engineering - who are the actual accountables and responsibles for it.

### Impact Description

**On Customers:** Increased response times, poor expectation management, worse outcomes during critical incidents

**On SRE:** Lack of coordination, unclear context, reactive execution without understanding the full picture

### Workshop Outcomes

**What we agree on:**
- ✅ Global Support should be as autonomous as possible to solve customer problems
- ✅ A Catalog item must be fully automated through Cloud Backoffice
- ✅ An assessment on the level of automation must be shared
- ✅ SRE must be involved from the moment GS suspects that a cloud change will be needed to recover an infrastructure incident
- ✅ Swarming mechanism should be similar the one existing for ODC (to be defined)
- ✅ **Execution Issue** - Swarming process on ODC needs to be reviewed

**Risks & Concerns:**
- ⚠️ From Global Support - Potential lack of reactivity can impact Incident Response times

### Decisions Needed

- [ ] GS autonomy to solve customer problems (AGREED)
- [ ] Full automation of Catalog items through Cloud Backoffice (AGREED)
- [ ] Share assessment on level of automation (AGREED)
- [ ] SRE involvement when GS suspects cloud change needed (AGREED)
- [ ] Define swarming mechanism similar to ODC (AGREED - to be defined)
- [ ] Review and fix ODC swarming process (AGREED - execution issue identified)
- [ ] Address GS concern on reactivity vs incident response times

---

## Challenge #7 — CritSits Engagement and RCA Alignment

### Problem Statement

There is no formal alignment on when/how to involve SRE in CritSits:

- CritSits require continuous communication until resolution, which may require SRE involvement, especially in ODC
- No formal process or alignment to deliver the 5-day SLA RCAs for CritSits
- Lack of clarity on how to engage SRE during weekends if needed

### Impact Description

Potential delays and suboptimal experience for Premium Support customers during the highest stake moments, leading to dissatisfaction with the service and potentially increasing the risk of Premium Support churn.

### Workshop Outcomes

**Status:** ⏸️ **REQUIRES DEDICATED SESSION WITH ENGINEERING LEADERSHIP**

This challenge was identified as requiring a separate dedicated discussion with Engineering Leadership before solutions can be defined.

**Original Proposed Actions:**

**CritSits:**
- Align the definition of a CritSit
- Align when and how to engage SRE
- Discuss 24x7 coverage (including weekends)

**RCAs:**
- Align on how to involve SRE in RCAs, respecting the 5-day SLA
- Align on SREs participation in RCA readouts

### Decisions Needed

- [ ] **Schedule dedicated session with Engineering Leadership**
- [ ] Align definition of CritSit across GS and Engineering
- [ ] Define when and how to engage SRE for CritSits (especially ODC)
- [ ] Establish 24x7 SRE coverage model for CritSits including weekends
- [ ] Define SRE involvement protocol for CritSit RCAs with 5-day SLA
- [ ] Clarify SRE participation requirements in RCA readouts

---

## Decisions & Action Items

### Decisions Made

*To be captured as solutions are finalized*

### Action Items

| Action | Owner | Timeline | Status | Challenge |
|--------|-------|----------|--------|-----------|
| Document Service Incident vs Support Case separation | Process Engineering + GS | TBD | Not Started | #1 |
| Escalate and resolve 24x7 Engineering coverage for support cases | Engineering Leadership + GS Leadership | TBD | Not Started | #1 |
| Define O11 customer communication transition timeline | GS + SRE | TBD | Not Started | #2 |
| Review full operating model (Service Assurance + Process Engineering) | Process Engineering + Service Assurance | TBD | Not Started | #3 |
| Define criteria and scenarios for Service Incidents | Process Engineering + GS | TBD | Not Started | #3 |
| Establish OLAs for Problem Management and RCA key moments | Process Engineering + GS | TBD | Not Started | #3 |
| Review and improve communication automations | Process Engineering + SRE | TBD | Not Started | #4 |
| Create deterministic process for GS to declare service incidents | Process Engineering + GS | TBD | Not Started | #4 |
| Define notification mechanism for Engineering-detected incidents | Process Engineering + SRE + GS | TBD | Not Started | #4 |
| Define which OLAs to implement and Engineering commitments | Engineering + GS | TBD | Not Started | #5 |
| Set targets of escalation per Support Scope Level (SSL) | GS + Engineering | TBD | Not Started | #5 |
| Schedule regular Engineering-GS operational review | Engineering Leadership + GS Leadership | TBD | Not Started | #5 |
| Establish release visibility mechanism for GS | Engineering + GS | TBD | Not Started | #5 |
| Share assessment on level of Cloud Backoffice automation | SRE | TBD | Not Started | #6 |
| Define O11 swarming mechanism (similar to ODC) | SRE + GS | TBD | Not Started | #6 |
| Review and fix ODC swarming process (execution issue) | SRE + GS | TBD | Not Started | #6 |
| Address GS reactivity concerns vs incident response times | SRE + GS | TBD | Not Started | #6 |
| Schedule Engineering Leadership session on CritSits | Engineering Leadership + GS Leadership | TBD | Not Started | #7 |

### Follow-up

- **Next checkpoint:** To be scheduled - Action item owners alignment
- **Documentation location:** This Confluence page + Process Engineering documentation
- **Status review cadence:** Regular Engineering-GS operational review (to be scheduled)
- **Key escalations needed:**
  - 24x7 Engineering coverage for support cases (Challenge #1)
  - Engineering Leadership session on CritSits (Challenge #7)

---

**Last Updated:** 2026-03-31
**Owners:** Vera Branco (Process Engineering), [VP Global Support TBD]
