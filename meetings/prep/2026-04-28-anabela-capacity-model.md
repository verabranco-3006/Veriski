# Meeting Prep — Anabela Cesário
*April 28, 2026 — Capacity Model Showcase + Scalability Discussion*

---

## Goal

Showcase the PE team capacity model as a working example. Be ready to discuss how this scales to other teams, including development teams.

---

## Showcase Flow (PE Reality)

Walk Anabela through the views in order — each one answers a different question:

| View | What it answers | Key point to highlight |
|---|---|---|
| **Capacity** | Is anyone overloaded? When? | Per-person utilization over 15 months, context-switching penalty visible |
| **Roadmap** | What's happening when? | Phase-based timeline (Primary / Secondary / Waiting) per person |
| **Schedule** | How do initiatives overlap? | Concurrent work visualization, dependency awareness |
| **Measurements** | Are we on track? | V2MOM metrics tied to execution |
| **Intake** | Can we absorb new work? | Simulate adding a new initiative — shows where it fits without overloading |

**The intake simulator is the strongest selling point.** When someone asks "can your team take this on?" — instead of gut feel, you run the simulation and get a data-backed answer: "Yes, starting month X with person Y" or "No, we're at 110% until September."

---

## How the Model Works (Technical Summary)

**Core concepts:**
- **Capacity unit** — the atomic unit you plan around (for PE: individual team member)
- **Baseline** — how much a capacity unit can deliver per week (PE: 12.5 SP/week = 25 SP per 2-week cycle)
- **Phase model** — each work item per month is tagged P (Primary, full weight), S (Secondary, 40% weight), or W (Waiting, 0%)
- **Context-switching penalty** — +2 SP/week for each concurrent Primary item beyond the first
- **Utilization** — (weekly load + penalty) / baseline. Green < 80%, yellow 80-100%, red > 100%

**Data layer** (`shared-data.js`):
- Team members (4 people)
- Work items with SP estimates, method alignment, and 15-month phase assignments
- All computations derived from this single data source

---

## Scalability Questions — Prepared Answers

### "Can this work for development teams?"

Yes. The model is capacity-unit agnostic. For PE, one unit = one person. For dev teams, one unit = one squad.

| | Process Engineering | Development Team |
|---|---|---|
| Capacity unit | Individual (Inês, Laura, Paulo) | Squad (Squad Alpha, Squad Beta) |
| Baseline | 12.5 SP/week per person | X SP/week per squad (calibrated to squad velocity) |
| Work items | V2MOM methods, BAU | Features, epics, tech debt, platform work |
| Phase model | P / S / W | Same — or simplified if squads are single-threaded |

The math is identical. What changes is the input data.

### "What needs to change to support other teams?"

Three layers need to be separated:

| Layer | Current state | What's needed |
|---|---|---|
| **Engine** (computation) | Reusable as-is | No changes — phase model, utilization, intake simulation all generic |
| **Configuration** (parameters) | PE-hardcoded (12.5 SP, 4 people, 15 months) | Per-team config: baseline, team members/squads, timeline, penalty model |
| **Data** (allocations) | PE-hardcoded in shared-data.js | Per-team data file: work items, SP estimates, phase assignments |
| **Views** (UI) | PE-branded, references V2MOM methods | Generalize labels (methods → initiatives/objectives), add team selector |

**Estimated effort to make team-agnostic:** 2-3 days of focused work to decouple config from views. After that, each new team needs ~half a day to populate their data file.

### "How do dev teams assess capacity today?"

**This is a question for Anabela.** Key things to understand:

1. **What's the capacity unit?** Squad, team, pod — what do they plan around?
2. **How do they estimate?** SP, t-shirt sizes, headcount %, time-based?
3. **Do they track concurrent work?** If yes → P/S/W model applies directly. If squads are single-threaded on one initiative → model simplifies (no context-switching penalty)
4. **Who owns the allocation data?** EM, TPM, team lead?
5. **What's their planning cadence?** Quarterly? Per-PI? Monthly?

### "What about teams with different estimation units?"

The model works with any unit as long as it's consistent within a team. SP, days, headcount % — the utilization math is the same:

`utilization = (allocated load + penalty) / baseline capacity`

We'd need a normalization layer if we want cross-team comparisons.

### "Can we integrate with Jira?"

Future possibility. Today the data is manually maintained in a JS file. The natural evolution:
1. **Phase 1 (now):** Manual data file per team — low effort, fast to adopt
2. **Phase 2:** Pull SP data from Jira epics (assigned vs spent) — aligns with M6.1 (Operational Capacity Allocation)
3. **Phase 3:** Bidirectional sync — Jira as source of truth, views as the visualization layer

### "What's the value proposition for a dev team lead?"

Three things they can't do today without this:
1. **Answer "can we take this on?" with data** — intake simulation instead of gut feel
2. **See overload before it happens** — utilization heatmap shows red months 3 months out
3. **Protect the team from invisible work** — BAU, secondary contributions, context-switching all become visible in the capacity model

---

## Open Questions for the Meeting

- [ ] Does Anabela see this as a tool for her org specifically, or something broader (Engineering-wide)?
- [ ] Who would be the pilot team beyond PE? Which dev team would benefit most?
- [ ] Is there an existing capacity planning tool or process we'd be complementing or replacing?
- [ ] What's the appetite for manual data entry vs waiting for Jira integration?

---

## Notes

*To be filled during/after the meeting.*
