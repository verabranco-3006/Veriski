# Global Support & Engineering Workshop - Solution Tracking

**Workshop Dates:** March 30-31, 2026

**Purpose:** Track problem statements, impacts, and proposed solutions for GS-Engineering alignment challenges

---

## Challenge #1 — Customer Communications Ownership

### Problem Statement
SRE continues to manage customer communications during incident response and request fulfillment. This has been an ongoing conversation for 1+ years with no meaningful progress.

### Impact
- **On Customers:** Inconsistent communication quality, unclear single point of contact
- **On SRE:** Time spent on customer-facing activities instead of technical resolution, role confusion
- **On GS:** Lack of ownership over basic support scope that exists in every other platform (O11, ODC)

### Proposed Solutions
GS takes full ownership of customer communications at incident response time and request fulfillment time. This is basic support scope and how we already operate on ODC.

### Decisions Needed
- [ ] GS commits to owning customer communications for incidents and request fulfillment
- [ ] Timeline for transition (with clear milestones)
- [ ] Training and documentation support needed from SRE

---

## Challenge #2 — RCA Communication to Customers

### Problem Statement
Engineering is constantly pulled in to lead RCA calls with customers. The premise is "we build the product" — but with that logic, Tech Support shouldn't exist either, as they don't build the product.

### Impact
- **On Customers:** Delays in receiving RCA communications, inconsistent experience
- **On Engineering:** Time spent on customer-facing communication instead of product improvements
- **On GS:** Lack of accountability for customer-facing functions that are core to support

### Proposed Solutions
GS owns communicating RCAs to customers. Engineering provides technical content and context. GS handles customer-facing delivery.

### Decisions Needed
- [ ] GS commits to owning RCA communication to customers
- [ ] Clear handoff process: Engineering provides RCA content, GS delivers to customer
- [ ] Timeline for implementation

---

## Challenge #3 — Swarming at SEV-1/SEV-2 Incidents

### Problem Statement
GS escalates through process without formal warm hand-over. No effective collaboration during severe incidents. Many times, GS doesn't escalate an incident — just the change they want SRE to execute.

### Impact
- **On Customers:** Increased response times, poor expectation management, worse outcomes during critical incidents
- **On SRE:** Lack of coordination, unclear context, reactive execution without understanding the full picture
- **On GS:** Claims lack of cloud knowledge but doesn't engage in collaborative resolution

### Proposed Solutions
Flip the script: Swarm as soon as GS assesses severity and confirms customer impact. Work together as a team until resolution.

- SEV-1/SEV-2 incidents trigger immediate collaboration between L3 and SRE
- Formal warm hand-over with context and coordination
- Stop escalating just "changes" — escalate the incident, collaborate on the solution

### Decisions Needed
- [ ] Define swarming protocol for SEV-1/SEV-2 incidents (L3 + SRE collaboration)
- [ ] Establish warm hand-over process with clear context sharing
- [ ] Commit to escalating incidents (not just changes) with full collaboration

---

## Challenge #4 — RCA Ownership and Collaboration

### Problem Statement
GS delivers RCAs on cloud incidents either without any alignment with SRE/Engineering or simply sends the RCA over. They pick and choose based on unknown criteria. One-sided approach.

### Impact
- **On Customers:** Incomplete or inaccurate RCAs, lack of technical depth where needed
- **On Engineering:** Blindsided by RCAs we didn't contribute to, or stuck doing the entire RCA alone
- **On GS:** Lack of accountability for customer impact portions, no shared ownership

### Proposed Solutions
Collaborate on RCAs with clear ownership:

- **Engineering/SRE:** Own the product/technical part of the RCA (root cause, technical analysis)
- **GS:** Own customer impact, timeline, customer-facing moments, and delivery
- **Collaboration and accountability are key** — not strict processes and ticket hand-offs

### Decisions Needed
- [ ] Define clear ownership: Engineering owns technical analysis, GS owns customer impact and delivery
- [ ] Establish collaboration model for RCA creation (not just "send it over")
- [ ] Commit to joint accountability for quality RCAs

---

## Challenge #5 — System-Wide Impact Communication

### Problem Statement
System-wide incidents are failing to communicate effectively—to Engineering internally and to customers externally. 44% of system-wide incidents have zero communication posted. The current IC Leader model (VS/EM) creates role redundancy and delays, while SRE already holds the full technical context needed for updates.

### Impact
- **On Engineering:** Role redundancy and toil—VS/EM pulled into on-call for IC Leader role, creating inefficient dependency and communication overhead
- **On SRE:** Forced to coordinate through VS/EM intermediaries when they already hold the full technical context needed for updates
- **On Customers:** Direct impact on External Status Page updates due to internal communication failures, information vacuum on root cause identification (only 21% communicate when root cause is identified)
- **On Organization:** Operational blindness—system-wide incidents occur with no visibility on Internal Status Page, no cross-team awareness
- **On Process:** 54% of incidents never receive "Resolved" update, only 7% follow full lifecycle (Investigating → Identified → Monitoring → Resolved)

### Supporting Metrics (Oct 2025 - Jan 2026, 39 system-wide incidents)
- **44% visibility gap:** 17 incidents with zero communication
- **54% failure to close:** 21 incidents never marked "Resolved"
- **7% process compliance:** Only 7% followed complete lifecycle
- **Role redundancy:** VS/EM as IC Leader questioned—SRE already has technical context
- **Median engagement:** 1.0 update per incident (50% get zero or one update total)

### Proposed Solutions
Streamline the IC role and automate bi-directional visibility:

- **Remove redundant layer:** SRE owns incident communication directly—they already have the context
- **Automate Internal Status Page:** Engineering gets real-time visibility on system-wide incidents
- **GS owns External Status Page:** Based on incident updates, GS manages customer-facing communication and status page
- **Enforce lifecycle communication:** All phases communicated (Investigating → Identified → Monitoring → Resolved), not just retrospectives

### Decisions Needed
- [ ] Remove VS/EM as IC Leader—SRE owns incident communication directly
- [ ] Commit to Internal Status Page visibility for all system-wide incidents
- [ ] GS owns External Status Page updates based on incident lifecycle
- [ ] Enforce complete lifecycle communication (not just post-mortems)

---

## Decisions & Action Items

### Decisions Made
*To be captured during workshop*

1.
2.
3.
4.
5.

### Action Items

| Action | Owner | Timeline | Status |
|--------|-------|----------|--------|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

### Follow-up
- Next checkpoint:
- Documentation location:
- Status review cadence:

---

**Last Updated:** 2026-03-25
**Owners:** Vera Branco (Process Engineering), [VP Global Support TBD]
