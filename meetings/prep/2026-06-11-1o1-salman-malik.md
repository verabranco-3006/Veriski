# 1:1 Prep — @Salman Malik
*June 11, 2026 — 11:00–11:45*

## Context
SVP of Product and Engineering Operations. New to OutSystems (announced April 2026). Hired to build the operating system for Product & Engineering at scale — his org owns planning discipline, release readiness, quality enforcement, incident command, production reliability, cost transparency, and Global Support.

PE reports directly to Salman. Transition complete.

**Core message going in:** PE is not here to justify its existence. PE has been doing this for 5 years — the operating model Salman was hired to build already exists in prototype. The question is how to scale it.

---

## Talking Points

### 1. What PE is and where it stands today
- Team of 3 (Inês, Laura, Paulo) — each owning a V2MOM method
- V2MOM: 6 methods / 28 submethods, Jira-tracked, capacity model in place
- PE owns: incident response governance, change management, retrospectives, failure management, RCA
- Active wins: retrospective transformation (replaced SRE bottleneck), BCDR drills, CM Fast Track controls, Internal Status Page

### 2. Ops Review — the opportunity
- Bi-weekly meeting PE co-leads with SRE, Quality, Release Engineering, Product Ops
- Current state: perceived as a blaming meeting — teams show up defensive, not learning
- PE has diagnosed the problem and has the capability to fix it
- If Salman wants this as a quick win, PE can build the operating model: data → insight → action → verify
- Requires org-level buy-in to close the improvement cycle — PE can't fix this alone

### 3. The org challenges (be direct)
- **Continuous improvement cycle broken at the output end** — retrospectives and Ops Reviews generate findings but there's no mechanism to ensure follow-through. We enforce the front end; the back end doesn't close.
- **GS collaboration friction** — now under same org. PE needs close collaboration with Global Support. Historical dynamic has been defensive positioning over joint problem-solving. Salman's structure is the enabler to fix this.
- **No lever to drive change at team level** — PE has visibility into which teams underperform on process execution but no authority to act on it. We identify patterns; we can't compel change.
- **Capacity vs scope** — team of 3 covering all of ODC. O11 unification may expand scope. At what point does the org invest in growing PE?

### 4. O11 processes
- PE's expected role with O11 processes (outcome of GS+R&D workshop still open)
- O11 Swarming between SRE + GS — need alignment on PE involvement scope

### 5. Ops Review follow-up (May 28)
- Salman raised a topic during the May 28 Ops Review he wants to follow up on — unclear what it was
- **Need to clarify:** What specifically did he want to follow up on?

### 6. Process Ecosystem + Ric Pruss
- Salman has shown interest in the Process Ecosystem — unclear what he wants
- Ric Pruss is also involved — need to understand the context and expectations
- **Need to clarify:** What is his ask? What role does he see PE playing here? What's Ric Pruss's angle?

### 7. BCDR Controls ownership (raised by Peter Farinde)
Four controls where ownership needs to be defined:

| # | Control | Scope |
|---|---------|-------|
| 1 | Data restore testing performed at least annually to verify backup data integrity | ODC + O11 |
| 2 | Production infrastructure and databases running across at least two distinct geographic locations | ODC |
| 3 | O11 Exercise and Testing Report and Drill Plan developed, documented, tested at least annually, issues documented and resolved | ODC + O11 |
| 4 | BCDR Strategy and Plan developed for ODC, documented, tested at least annually, issues documented and resolved | O11 + ODC |

- Who owns each of these controls — PE, SRE, or joint?
- Is Salman the right person to define ownership given PE is moving to his org?

---

## Questions to Ask Salman

- What does he need from PE in the next 30/60/90 days?
- How does he see Engineering Operations taking shape — is PE the nucleus or one input?
- Cadence: 1:1 frequency, operating rhythm preferences

### 8. If time allows — Engineering Operations org setup
- Does Salman have a vision for how Engineering Operations takes shape?
- What help does he need to build it out — from PE or otherwise?
- Any early thinking on structure, headcount, or priorities for the function?

---

## Watch For
- Does he see PE as a team to absorb or a foundation to build on?
- Does he have preconceptions from other stakeholders (GSSA narrative, blame culture)?
- His leadership style: hands-on operator vs. strategic architect?

**Growth edge reminder:** Don't over-commit to new scope to impress. Show the V2MOM, show the execution, let it speak.

---

## Notes

---

## Meeting Notes
*Processed from Zoom recap — June 11, 2026*

### Key Outcomes

**Customer feedback (Axos + Entel)**
- Positive on AI and agentic direction; keynote demos landed well
- Both customers committed to staying but raised concerns: ODC reliability, log visibility, development work transparency
- Salman's framing: drive improvements from customer impact backwards, not from engineering concerns upward

**Business process mapping (new work)**
- Salman wants a comprehensive map: from customer-facing incident all the way back to product design and development
- Rick Pruss is already working on something in this space (Confluence doc → presentation for a kickoff/education meeting)
- Vera to engage Rick directly first, then coordinate a 3-way meeting (Vera + Rick + Salman)
- Scope: PDLC end-to-end — SLOs, tickets, RCAs, incidents, QA coverage — connected into one architecture
- This could become the foundation for how PE frames its value: process architecture from idea to improvement

**BCDR ownership**
- Architecture owns the product-level BCDR strategy (scenario definition)
- PE owns execution and testing
- Gap identified: no one has formally articulated the BCDR scenarios the org should design for
- Salman to raise in CPTO team chat to surface existing work and clarify ownership

**GS / Engineering friction**
- GS frequently escalates to engineering without fully owning the problem statement
- MTTR measurement is a shared pain point — linguistic and process gaps between teams
- Vera to write up the friction clearly for the upcoming workshop with Salman and Paul Garcia
- Salman's org structure (GS + PE under same roof) is the lever to fix this

**Salman's operating style (observed)**
- Starts from customer impact, works backwards — Pareto analysis approach
- Wants a clear headline vision for the org (Amazon-style "press release first")
- Plans to draft his own list of perceived problems from the last 2 months — will share with Vera for input

### Action Items

**Vera**
- [x] Engage Rick Pruss directly — message sent, waiting for reply
- [ ] Draft a joint plan with Rick for end-to-end process mapping
- [ ] Coordinate 3-way meeting: Vera + Rick + Salman
- [ ] Start drafting the business/process flow map: product idea → post-incident learning
- [ ] Write up the GS/Engineering friction (MTTR gap, problem ownership) for Salman + Paul Garcia workshop
- [ ] Prepare for and participate in Salman + Paul Garcia workshop
- [ ] Write up the MTTR/lingo gap as a standalone problem statement

**Salman**
- [ ] Draft list of perceived problems/challenges from last 2 months → share with Vera for review
- [ ] In CPTO team chat: ask if BCDR scenarios have been articulated, clarify ownership/definition

