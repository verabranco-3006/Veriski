# Global Support & Engineering Workshop
## Presentation Content Outline

**Date:** March 30-31, 2026
**Audience:** VP Engineering, VP Global Support, VP-1s (Process Engineering, SRE, Service Management, Service Delivery)
**Goal:** Align on challenges and strategic decision-making between GS and Engineering

---

## Slide 1: Title Slide

**Title:** Global Support & Engineering Strategic Alignment Summit

**Subtitle:** Bridging Collaboration for Better Customer Outcomes

**Date:** March 30-31, 2026
**Presenters:** [Your names here]

---

## Slide 2: Workshop Goals & Agenda

### Workshop Goals
- Align on current challenges impacting GS-Engineering collaboration
- Create shared understanding of organizational structure
- Make strategic decisions on key topics
- Define clear next steps and ownership

### Summit Schedule

**Monday, March 30**
- **10:00–12:00** — Introduction & Challenges
  - Engineering & Product Organization Overview
  - Challenge #1: Customer Communications Ownership
  - Challenge #2: RCA Communication to Customers
  - Challenge #3: Swarming at SEV-1/SEV-2 Incidents

- **14:00–16:00** — Align Possible Solutions
  - Challenge #4: Service Incidents vs Support Cases Paradigm
  - Challenge #5: RCA Ownership and Collaboration
  - Challenge #6: System-Wide Impact Communication
  - Discussion: Possible Solutions & Trade-offs

**Tuesday, March 31**
- **15:30–17:00** — Strategic Alignment
  - Decisions & Commitments
  - Next Steps & Ownership
  - Follow-up Cadence

---

## Slide 3: Engineering & Product Organization

### Value Streams Structure

**How Engineering is Organized:**
- **15 Active Value Streams** — each led by VP-1 or senior leaders
- Value Streams own product areas end-to-end
- Teams within Value Streams focus on specific capabilities
- Cross-Value Stream collaboration on platform capabilities

**15 Active Value Streams:**

| Value Stream | Leaders | Focus Area |
|--------------|---------|------------|
| **O11** | Carlos Soares, Bruno Batista, Pedro Oliveira | OutSystems 11 Platform |
| **PaaS** | Marta Nobre, Anand Santhanam, Dan Iorg, Miguel João | Platform as a Service |
| **Cloud Platform** | Dan Iorg, Renato Armani, João Valentim | Cloud Infrastructure |
| **Web & Mobile Apps** | Hélder Marques, Hugo Gonçalves, Vitor Oliveira, Luís Silva, Mariana Bexiga, Hector Guerra | Web & Mobile Development |
| **Agentic Apps & Data** | Sandro Cantante, Rahul Kumar, Vivek Mano, Sudharshan Krishnamurthy, Tito Moreira, Joel Alexandre | AI-powered Applications & Data |
| **AI DevX** | João Ascensão, Emily Saforrian, Paulo Cunha, Inês Munhá | AI Developer Experience |
| **ALM** | Filipa Sousa, Rui Santos, Rui Eugénio, André Vieira | Application Lifecycle Management |
| **Identity** | Nuno Batista, Jon Branch, Rui Couto, Nuno Parreira | Identity & Access Management |
| **Unification** | João Romão, Ricardo Ferreira, Marco Jorge, João Batista | Platform Unification |
| **Production Engineering** | Pedro Charola, Ricardo Silva | Production Operations & SRE |
| **Release Engineering** | London Cole Summers, João Brandão | Release Management |
| **Quality Engineering** | Vijay Bolleddu | Quality Assurance |
| **Solutions** | HuaSheng Su, Gonçalo Borrêga, Jean-Baptiste Minchelli, Francisco Menezes, Liam Doyle | Solutions Engineering |
| **Evaluation & Community** | Andreia Mesquita, Marco Jorge, Ângela Dinis, Ricardo Neto | Customer Evaluation |
| **Vanguard** | Acácio Porta Nova | Innovation & Future Tech |

**Key Support Touchpoints:**
- **Production Engineering** → SRE collaboration, incident response, change management
- **Quality Engineering** → Quality assurance processes, testing standards
- **Release Engineering** → Change management coordination, deployment orchestration
- **O11 & Cloud Platform** → Platform-level incident escalation

---

## Slide 4: Challenge #1 — Customer Communications Ownership

### The Problem
SRE continues to manage customer communications during incident response and request fulfillment. This has been an ongoing conversation for 1+ years with no meaningful progress.

### Impact
- **On Customers:** Inconsistent communication quality, unclear single point of contact
- **On SRE:** Time spent on customer-facing activities instead of technical resolution, role confusion
- **On GS:** Lack of ownership over basic support scope that exists in every other platform (O11, ODC)

### Current State
- SRE manages customer communications during incidents and change requests
- GS has not transitioned to owning this scope despite 1+ year of discussions
- This is standard practice for ODC — basic support scope
- **The situation is now unacceptable**

### Proposed Solution
GS takes full ownership of customer communications at incident response time and request fulfillment time. This is basic support scope and how we already operate on ODC.

### What We Need to Decide
- [ ] GS commits to owning customer communications for incidents and request fulfillment
- [ ] Timeline for transition (with clear milestones)
- [ ] Training and documentation support needed from SRE

---

## Slide 5: Challenge #2 — RCA Communication to Customers

### The Problem
Engineering is constantly pulled in to lead RCA calls with customers. The premise is "we build the product" — but with that logic, Tech Support shouldn't exist either, as they don't build the product.

### Impact
- **On Customers:** Delays in receiving RCA communications, inconsistent experience
- **On Engineering:** Time spent on customer-facing communication instead of product improvements
- **On GS:** Lack of accountability for customer-facing functions that are core to support

### Current State
- RCAs are completed and agreed upon internally
- Engineering is expected to lead customer-facing RCA calls
- **Communicating RCAs has no technical challenges** — this is a support function, not an engineering one

### Proposed Solution
GS owns communicating RCAs to customers. Engineering provides technical content and context. GS handles customer-facing delivery.

### What We Need to Decide
- [ ] GS commits to owning RCA communication to customers
- [ ] Clear handoff process: Engineering provides RCA content, GS delivers to customer
- [ ] Timeline for implementation

---

## Slide 6: Challenge #3 — Swarming at SEV-1/SEV-2 Incidents

### The Problem
GS escalates through process without formal warm hand-over. No effective collaboration during severe incidents. Many times, GS doesn't escalate an incident — just the change they want SRE to execute.

### Impact
- **On Customers:** Increased response times, poor expectation management, worse outcomes during critical incidents
- **On SRE:** Lack of coordination, unclear context, reactive execution without understanding the full picture
- **On GS:** Claims lack of cloud knowledge but doesn't engage in collaborative resolution

### Current State
- GS escalates via ticket/process — no warm hand-over
- Sometimes L1 escalates directly to SRE (should be L3 → SRE)
- GS requests changes without escalating the actual incident
- **No effective collaboration during critical moments**

### Proposed Solution
**Flip the script:** Swarm as soon as GS assesses severity and confirms customer impact. Work together as a team until resolution.
- SEV-1/SEV-2 incidents trigger immediate collaboration between L3 and SRE
- Formal warm hand-over with context and coordination
- Stop escalating just "changes" — escalate the incident, collaborate on the solution

### What We Need to Decide
- [ ] Define swarming protocol for SEV-1/SEV-2 incidents (L3 + SRE collaboration)
- [ ] Establish warm hand-over process with clear context sharing
- [ ] Commit to escalating incidents (not just changes) with full collaboration

---

## Slide 7: Challenge #4 — Service Incidents vs Support Cases Paradigm

### The Problem
Service incidents and support cases are conflated in the current escalation model. High-priority support cases are automatically routed to SRE using severity mapping (Urgent/High → SEV1/SEV2), regardless of actual system-wide impact. This forces SRE to validate each escalation and hand-over non-systemic issues back to product teams, creating organizational drag and resource waste.

### Impact
- **On Customers:** Confused reporting and misalignment — single MTTR metric blurs system stability issues with customer-specific support cases
- **On Engineering:** Wasted resources pulling highly specialized SRE staff into non-systemic issues during recovery **and** aftermath (complex retrospectives for what should be standard Problem Management)
- **On SRE:** Staff exhaustion from over-escalation, diverted from critical system stability work
- **On Organization:** Misalignment of expectations across stakeholders due to ambiguity in ownership and urgency definitions

### Current State
- Support cases automatically escalate to SRE based on severity mapping (Urgent/High → SEV1/SEV2)
- SRE must validate every escalation to confirm system-wide impact
- If no system-wide impact → SRE hands over to product teams, but damage is done (resources mobilized, processes triggered)
- GS can declare "Major Incident" for high-priority cases **without** SRE validation
- Same MTTR metric used for system stability and customer experience issues

### Proposed Solution
**Separate two distinct motions with clear triggers, ownership, and metrics:**

**Service Incidents 🔥**
- **Trigger:** SLO breaches or customer reports confirmed by SRE as system-wide impact
- **Ownership:** SRE Team
- **Platform:** Rootly
- **Metrics:** Engineering MTTR, Engineering MTTA
- **Coverage:** 24x7 SRE On-Call
- **Follow-up:** Retrospective Process, Problem Management, Continuous Improvement

**Support Cases 🧑**
- **Trigger:** Support cases escalated to Product Teams or incidents handed over by SRE (no system-wide impact confirmed)
- **Ownership:** Global Support (Product Teams act as L4)
- **Platform:** Jira
- **Metrics:** Escalation Ratio, Escalation Lead Time, Engineering Lead Time (since escalation), Red Button activation
- **Coverage:** 8x5 (with Red Button activation by GS)
- **Follow-up:** Problem Management, Bug Fixing

**Critical Change:** GS must **stop declaring Major Incidents for unvalidated incidents** unless confirmed by Engineering. This reverses current practice and ensures mobilization of Engineering teams happens **only** for validated Service Incidents.

### Transition Protocols ("Hand-shake" between motions)

**Support Case → Service Incident (Escalation):**
- GS flags potential system-wide impact in Zendesk
- SRE performs validation check
- If confirmed → Support Case linked to new Service Incident in Rootly, ownership shifts to SRE

**Service Incident → Support Case (Demotion/Hand-over):**
- SRE determines no system-wide impact
- Service Incident closed in Rootly with "No System Impact" resolution
- Warm hand-over to Product Engineering via Jira with all SRE findings

### What We Need to Decide
- [ ] Adopt Service Incident vs Support Case separation with distinct metrics
- [ ] GS stops declaring Major Incidents without Engineering validation
- [ ] Define clear escalation heuristics: what qualifies as "system-wide impact"
- [ ] Establish warm hand-over protocol for incident demotion/escalation transitions

---

## Slide 8: Challenge #5 — RCA Ownership and Collaboration

### The Problem
GS delivers RCAs on cloud incidents either without any alignment with SRE/Engineering or simply sends the RCA over. They pick and choose based on unknown criteria. One-sided approach.

### Impact
- **On Customers:** Incomplete or inaccurate RCAs, lack of technical depth where needed
- **On Engineering:** Blindsided by RCAs we didn't contribute to, or stuck doing the entire RCA alone
- **On GS:** Lack of accountability for customer impact portions, no shared ownership

### Current State
- GS delivers RCAs on cloud incidents with no collaboration
- No clear criteria for when to engage SRE/Engineering
- Process-driven approach: "sending tickets over the fence"
- **No collaboration, no accountability**

### Proposed Solution
Collaborate on RCAs with clear ownership:
- **Engineering/SRE:** Own the product/technical part of the RCA (root cause, technical analysis)
- **GS:** Own customer impact, timeline, customer-facing moments, and delivery
- **Collaboration and accountability are key** — not strict processes and ticket hand-offs

### What We Need to Decide
- [ ] Define clear ownership: Engineering owns technical analysis, GS owns customer impact and delivery
- [ ] Establish collaboration model for RCA creation (not just "send it over")
- [ ] Commit to joint accountability for quality RCAs

---

## Slide 9: Challenge #6 — System-Wide Impact Communication

### The Problem
System-wide incidents are failing to communicate effectively—to Engineering internally and to customers externally. 44% of system-wide incidents have zero communication posted. The current IC Leader model (VS/EM) creates role redundancy and delays, while SRE already holds the full technical context needed for updates.

### Impact
- **On Engineering:** Role redundancy and toil—VS/EM pulled into on-call for IC Leader role, creating inefficient dependency and communication overhead
- **On SRE:** Forced to coordinate through VS/EM intermediaries when they already hold the full technical context needed for updates
- **On Customers:** Direct impact on External Status Page updates due to internal communication failures, information vacuum on root cause identification (only 21% communicate when root cause is identified)
- **On Organization:** Operational blindness—system-wide incidents occur with no visibility on Internal Status Page, no cross-team awareness
- **On Process:** 54% of incidents never receive "Resolved" update, only 7% follow full lifecycle (Investigating → Identified → Monitoring → Resolved)

### Current State (Data: Oct 2025 - Jan 2026, 39 system-wide incidents)
- **44% visibility gap:** 17 incidents with zero communication
- **54% failure to close:** 21 incidents never marked "Resolved"
- **7% process compliance:** Only 7% followed complete lifecycle
- **Role redundancy:** VS/EM as IC Leader questioned—SRE already has technical context
- **Median engagement:** 1.0 update per incident (50% get zero or one update total)

### Proposed Solution
Streamline the IC role and automate bi-directional visibility:
- **Remove redundant layer:** SRE owns incident communication directly—they already have the context
- **Automate Internal Status Page:** Engineering gets real-time visibility on system-wide incidents
- **GS owns External Status Page:** Based on incident updates, GS manages customer-facing communication and status page
- **Enforce lifecycle communication:** All phases communicated (Investigating → Identified → Monitoring → Resolved), not just retrospectives

### What We Need to Decide
- [ ] Remove VS/EM as IC Leader—SRE owns incident communication directly
- [ ] Commit to Internal Status Page visibility for all system-wide incidents
- [ ] GS owns External Status Page updates based on incident lifecycle
- [ ] Enforce complete lifecycle communication (not just post-mortems)

---

## Slide 10: Decisions & Next Steps

### Decisions Made Today
1. [Decision #1]
2. [Decision #2]
3. [Decision #3]
4. [Decision #4]
5. [Decision #5]

### Next Steps

| Action | Owner | Timeline |
|--------|-------|----------|
| [Action item 1] | [Name] | [Date] |
| [Action item 2] | [Name] | [Date] |
| [Action item 3] | [Name] | [Date] |
| [Action item 4] | [Name] | [Date] |
| [Action item 5] | [Name] | [Date] |

### Follow-up
- Next workshop: [Date]
- Status check: [Date]
- Documentation: [Location]

---

## Notes for Building in Google Slides

**Design Recommendations:**
1. Use OutSystems brand colors and templates
2. Keep text minimal on slides — use visuals where possible
3. For Slide 3 (Value Streams), consider a visual org chart or grouped boxes
4. For Challenge slides, use icons or visual indicators for impact areas
5. Use consistent layout across all challenge slides
6. Consider adding backup slides with detailed data if needed

**Visual Assets Needed:**
- OutSystems logo
- Value Stream structure diagram (consider creating visual hierarchy)
- Icons for customer impact, GS impact, Engineering impact
- Decision tracking checkboxes or visual indicators

**Presentation Tips:**
- Slide 2: Set expectations for interactive discussion
- Slide 3: Keep it high-level, don't dive too deep into each Value Stream
- Slides 4-7: Focus on one challenge at a time, encourage discussion
- Slide 8: Use as working document during workshop, fill in live

---

**Created:** 2026-03-25
**Last Updated:** 2026-03-25
