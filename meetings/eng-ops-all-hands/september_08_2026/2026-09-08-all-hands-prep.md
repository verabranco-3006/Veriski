# Product & Engineering Ops All Hands — Speaker Notes

**Tue Sep 8, 16:00 WEST · Wed Sep 9, 09:00 WEST · ~4 min · 3 slides**

**Structure:** who we are as leaders → how that shapes our strategy (the bridge) → the one thing to remember.

> **Synced to the Google Slides deck, Sep 7 export.** Wording below matches what is on the slides. Three things in the deck need a fix before the dry run — see *Deck fixes* at the foot of this file.

---

# Slide 1 — Who we are as leaders

*~1 min 55* — **no roll-call here.** Slide 1 no longer shows the team, so it states the number and moves on. The four names are said on slide 3, on the faces.

> Three years ago, when we pitched the name of this team for the first time, we were asked what our biggest achievement had been. The answer we gave was: **creating bridges and common ground** — with Global Support, and across R&D. That is still the answer, and it is still the job. The bridges just got a lot longer.
>
> Let me tell you where the bridge habit comes from, because this is not a job I fell into. **I am a mechanical engineer by training** — and that training does not switch off. I look at a queue at the airport and I start redesigning it. Same thing in the cafeteria — I sense improvement from a distance. My family will tell you how exhausting this can be. I want the best possible thing built with the least possible waste, and I cannot leave a system alone once I can see the slack in it.
>
> Which is why I should say this out loud: **process engineering is not a metaphor we borrowed.** It is a real engineering discipline. On a factory floor, the process engineer is the one who designs the conveyor belt, so it makes the same good thing every time — at volume, without hurting anybody — and then never stops tuning it. **Scale. Risk. Repeatability. And a feedback loop that never closes.**
>
> That is exactly this job. The conveyor belt we are designing is **how R&D changes and recovers** — at scale, fast, with risk managed and outcomes predictable. Same discipline, different factory.
>
> **And we are four people** — for all of R&D, on both platforms. At that ratio you have to be exact about what the job is, and it comes down to one line — our vision: **move fast, and know it will hold.** This organization is already fast; nobody needs help going faster. What is hard is **knowing it will hold** when it does — and four people cannot mandate that. So **trust is the operating model here, not a nicety:** a process only works if the people running it find it useful.
>
> Which is why **the things I hold this team to sound like engineering, not management.** Four of them, and you can hold me to all four.
>
> **First — diagnostics, not verdicts.** Metrics and compliance are instrumentation. They tell us where the system strains. They are not a verdict on the team running it, and we will not use them as one.
>
> **Second — tolerances, not instructions.** A process is not a set of instructions. It is **flexibility with guidance** — it tells you what has to hold and leaves you the room to decide how you get there. You know the bar, and you own hitting it. That is the whole trade: we are explicit about what good looks like, you stay in charge of how it gets done.
>
> **Third — if it doesn't carry load, it comes out.** The hardest question in our own team meetings is not *how do we do this* — it is *why are we doing this at all.* We challenge the value of our own work, constantly. And the bar is not whether a process was followed. It is whether it made something hold that would otherwise have broken — **for the system as a whole, not for one team's number.** Nothing survives here because it is policy, or because we have always done it. If we cannot show the outcome, we should be dropping it — and sometimes we do.
>
> **Fourth — zero surprises. Not zero problems.** And this is the one I hold hardest. **Transparency and humbleness are not negotiable in this team.** We will get things wrong — we do. What I will not accept is you finding out from somewhere else. When a process of ours fails, you hear it from us before you hear it from an audit. And no process change lands on your team without you having heard it from us first.
>
> And one thing that follows from all four: I ask my team for urgency constantly, but I do not believe in a process that only holds when people are at their limit. **If it needs heroics to hold, we designed it wrong.**

---

# Slide 2 — How that shapes our strategy

*~1 min 25* — four beats: one seam explained, the other two named, the alignment point plus the two moves, one example. The seams are on the slide, so nothing here describes what the room can already read.

> So what does that turn into? Look at how work actually moves here. **Take an incident.** Global Support owns the customer relationship. SRE owns the system — what is broken, and what it actually affects. Both accountabilities are real, both teams are doing their part, and neither of them is wrong. **Two strong shores.** But the question in the middle — *what does the customer know right now?* — cannot be answered from either shore alone. And during an incident, that picture moves by the minute.
>
> Same shape between Security and Engineering. Same between SRE and the team that owns the code. **Three examples, not the list** — pick almost any two teams in this room and there is a seam like this between them.
>
> So the hard part here was never accountability — **it is alignment.** Two right answers becoming one agreement, and then holding. **That gap is the work, and it is ours.** Two moves: we **build the bridge**, then we **make it hold** — codified so a system can execute it, and measured when the traffic gets heavy.
>
> **One example, already in production.** SRE was writing the postmortems for incidents other teams owned — so the people who could prevent the next one were not the ones learning from the last. That has moved to the teams who own the asset, and the writing did not move with it: the data gets pulled, the analysis gets drafted and scored, the owning team reviews and approves. **The learning moved. The work did not.**
>
> There is more behind it — and it does not fit in four minutes. We would rather **come back to a future all hands and go properly deep on one** than skate across all four now.

**Into slide 3:**

> A bridge is invisible when it works. You only notice it when it is not there. So let me leave you with the one thing worth remembering.

---

# Slide 3 — The one thing to remember

*~50 seconds* — the roll-call moved here from slide 1, where the photos now are.

> If you remember one thing about Process Engineering, make it this. **We own the space between teams.**
>
> You own your shore — your operations, your tools, your decisions. Those stay yours, and they are what this whole thing rests on. What we build is the crossing, and **whether it holds is ours.**
>
> *(gesture at the pylon)* And that is us. Not on either shore — the structure in the middle, holding the span up.
>
> **These are the four people who do it.** Inês, on Incident, Problem and Deployment Failures. Laura, on Change Management. Paulo, on metrics and AI industrialization. And me, on Compliance and Security.
>
> So if you find yourself standing between two teams with a question neither side can answer alone, that is not friction you have to live with. That is the space between teams. **Come find us.**

---

## Optional expansions

Nothing here is on a slide, and none of it leaves a gap if cut. Add only if the leadership block runs short — in this order.

> **1 · A second example: the codifying move** *(+20s, after the postmortem beat)* — The other half is codifying, because what good looks like should not depend on who happens to be on shift. The change catalog held around **1,800** *(one thousand eight hundred)* raw operation types; we collapsed it into **61** *(sixty-one)* articles, mapped one to one. That is what a standard actually costs, and it only ever gets paid if a team owns it end to end.
>
> **2 · Holding ourselves to it** *(+15s, after either example)* — And we hold our own work to the same bar. Root cause analysis used to take us **88 days.** Today it takes about **22** — that is what the AI work bought us. Our goal is **10.** We are not there yet, and that gap is exactly the work.
>
> **3 · Credit the partners** *(+8s, before the "more next time" line)* — Not one of these was Process Engineering working alone. Every one has a named partner, and most of them are in this room.
>
> **4 · Security** *(+20s)* — We wrote the emergency response process for AI-speed vulnerabilities: hours, not weeks. We are unifying that emergency path with standard vulnerability management into one framework, so Engineering gets a risk-based queue it can act on instead of a volume it cannot. Security defines what risk matters, Engineering owns the fix, and we own the process between them so neither side is guessing.
>
> **5 · The AI roadmap** *(+25s)* — And that is a roadmap, not a one-off. Next: a bot the teams can simply *ask* process questions instead of hunting through Confluence. A reviewer agent for Change Control. And the two we are most interested in — an agent that reads the manual changes coming through and tells us which ones are worth automating, and one that flags process deviations while they are still cheap to fix instead of at audit. **That is the process starting to watch itself.**
>
> **6 · Why now — the traffic is getting heavier** *(+15s, at the end of slide 2)* — Because the traffic is getting heavier. AI compresses every cycle we have: vulnerabilities get weaponized in hours instead of weeks, code ships faster than the governance around it was ever designed for. Speed does not break organizations. **Unmanaged handoffs at speed break organizations.** *(Cut from the main line to shorten slide 2 — this is the first thing to add back if you have the seconds, because it is the "why now".)*
>
> **7 · The seam in more detail** *(+10s, inside the first beat)* — SRE is not the one talking to the customer. Support is not the one watching the system. It only works if the two stay in sync.
>
> **8 · Ohno** *(+10s)* — Taiichi Ohno said we cannot progress if we are satisfied with what we have. That is the job description. **Best home is slide 1**, straight after *"and then never stops tuning it"* — it belongs to the factory-floor image, and it lands harder there than bolted onto the RCA figure on slide 2.

---

## ⚠️ Length audit — the script is about twice the slot

Measured word counts, at a deliberate presentation pace of **150 wpm** (your style is full sentences, explaining rather than declaiming — not a 180 wpm delivery):

| Slide | Words | At 150 wpm | Target for a 4-min slot |
|---|---|---|---|
| 1 — Who we are as leaders | **691** | **4:36** | ~250 words · 1:40 |
| 2 — How that shapes our strategy | 310 | 2:04 | ~250 words · 1:40 |
| 3 — The one thing to remember | 139 | 0:56 | ~120 words · 0:50 |
| **Total** | **1,140** | **7:36** | **~620 words · 4:10** |

**Slide 2 was not the problem — slide 1 is.** It carries 61% of the words. The four commitments plus the coda alone are ~330 words (2:12), which is over half the entire slot, and every one of them is already written on the slide in a single line.

**Where the ~500 words have to come from:**

| Block | Now | Cut to | How |
|---|---|---|---|
| Three years ago / bridges | 55 | 40 | Trim to the answer and "the bridges just got longer" |
| Mechanical engineer origin | 95 | 60 | Keep the airport; drop the cafeteria **or** the family line, not both |
| Not a metaphor / conveyor belt | 75 | 50 | Cut "It is a real engineering discipline" — the next sentence proves it |
| Same discipline, different factory | 35 | 25 | Fine as is, minor trim |
| Four people / vision / trust | 80 | 55 | Already compressed once; drop "nobody needs help going faster" |
| **The four commitments** | **285** | **90** | **The big one — see below** |
| Heroics coda | 45 | 20 | Keep only *"if it needs heroics to hold, we designed it wrong"* |

### The four commitments, compressed (~90 words instead of 285)

The slide already carries the explanation for each. Name it, add one clause, move on:

> **First — diagnostics, not verdicts.** Metrics tell us where the system strains. They are not a verdict on the team running it.
>
> **Second — tolerances, not instructions.** You get what has to hold, and the room to decide how. You know the bar; you own hitting it.
>
> **Third — if it doesn't carry load, it comes out.** We challenge the value of our own work first, and the bar is not whether a process was followed — it is whether it held something that would otherwise have broken. **For the system, not for one team's number.**
>
> **Fourth — zero surprises. Not zero problems.** This is the one I hold hardest. We will get things wrong; what I will not accept is you finding out from somewhere else. **If it needs heroics to hold, we designed it wrong.**

That is **-195 words ≈ -80 seconds** and nothing is lost that the room cannot read off the slide. The full versions above stay in this file as the reference for what each commitment actually means — useful for Q&A, not for the four minutes.

---

## Timing and the cut

| Slide | As written | With the compressions above | First to cut beyond that |
|---|---|---|---|
| 1 — Who we are as leaders | **4:36** | ~1:40 | The cafeteria aside, then the third commitment |
| 2 — How that shapes our strategy | 2:04 | ~1:40 | The postmortem example (~30s) |
| 3 — The one thing to remember | 0:56 | ~0:50 | The roll-call of names — the faces are on screen either way. **Never the claim or the close.** |

**Total as written: ~7:36. With the compressions: ~4:10.** The earlier "~4:25 as written" figure in this file was wrong — it was estimated by eye rather than counted. Do not add any optional expansion until the compressions are applied and you have timed yourself out loud once.

**The two personal beats are the ones Salman asked for.** The **mechanical engineering origin** (~35s) and **"transparency and humbleness are not negotiable"** closing slide 1 (~20s). If you have to cut one, cut the closing beat and keep the origin story — it is the one that earns the definition line rather than asserting it, and it is the more personal of the two. **Don't cut both**; the ask was explicit.

**Trimming the origin story without losing it.** The airport-queue line and "my family will tell you it is exhausting" are the warmth, not the argument — drop them first (~10s) and it still works: *"I am a mechanical engineer by training, and that training does not switch off. I want the best possible thing built with the least possible waste. Which is why I should say this out loud: process engineering is not a metaphor we borrowed…"*

**Hard floor if you are cut to two minutes:** the vision and the four commitments from slide 1, the *two strong shores* beat and the two moves from slide 2, and all of slide 3.

**Where the team is introduced.** Slide 1 no longer shows the four of you, so it no longer names you — it states **"Four people. For all of R&D, on both platforms"** and moves straight to the vision. The names land on **slide 3**, on the faces, at the pylon: *"These are the four people who do it."* That is the better place for them anyway — a roll-call in the first thirty seconds is a status report, and the same four names arriving under *we own the space between teams* reads as the answer to who does that.

**Never cut:** *"We own the space between teams"* and *"Come find us."*

**Why slide 2 only carries one example.** Four proof points in four minutes is a list, not an argument — and the seams are what this room needs to understand. The postmortem story is the one that lands hardest here: it is already in production, and it relieves SRE of writing other teams' analyses. **"We would rather come back and go properly deep on one"** is a promise worth making out loud — it sets up a future slot, and it is more credible than skating across all four.

**No figures are on a slide.** Every number is spoken, so you can soften, re-scope or drop any of them live — *"around 1,800"*, *"about 22"*. If `22` or `1,800 → 61` is still unconfirmed on the day, say the shape instead: *"we cut root cause time by roughly four times, and we are going after another two."*

---

## Deck fixes — before the dry run

| # | Slide | Issue | Fix |
|---|---|---|---|
| 1 | 2 | **"What stops from happening again?"** is missing a word. | → *"What stops **it** from happening again?"* Third question in the blue box. |
| 2 | 1 | **"At that ratio" has no ratio to refer to** — and the narration now leans on the number harder than before: with the roll-call gone, *"we are four people"* is the whole scale beat. The subtitle gives the surface but never the count, and the photos moved to slide 3. | Replace the line with **"Four things you can hold me to."** — see the slide 1 proposal below. **And** add the count to the subtitle: *"…outcomes predictable. **Four people**, ODC and O11, all of R&D."* The scale mismatch is the strongest fact you have and the photos no longer supply it. |
| 3 | 3 | **"Come find us" is gone from the slide.** Without it the slide states an identity; with it, the room gets an instruction — which is the whole reason this slide is last. | One line under the sub: *"Standing between two teams with a question neither side can answer alone? **Come find us.**"* It is still in the script either way, so **say it out loud regardless.** |

**Two smaller calls, your judgement:**

- **"space between the teams" → "space between teams."** Dropping *the* makes it a category rather than a specific set of teams, which is what a line built to be repeated secondhand needs. The headline is also missing its full stop while the lines above and below have one.
- **The belief lost its second half** — *"a process only works if the people running it find it useful"* is off the slide. It is the anchor the three commitments hang off. Still spoken, so nothing breaks; restore it if the right column has room.

---

## Slide 1 — proposed changes (personal, and the three commitments made visual)

`space-between-teams.html` slide 1 is **ahead of the deck** and shows all three. Nothing is added *inside* the three commitments — the work is done by what surrounds them.

**1 · Replace "At that ratio, trust is the operating model."** → **"Four things you can hold me to."**

That line no longer works: it used to follow *"Four people — ODC and O11, for all of R&D"*, which supplied the ratio. The subtitle now gives the surface but never says **four people**, and the photos moved to slide 3 — so there is no ratio on the slide to point back to. The replacement fixes the dangling reference, signposts the count (your move), and turns the three from a values list into **personal promises**. Put the accent on **me**.

**2 · Tie the three to you, with two lines.** One horizontal line from the right edge of your portrait, then one vertical line down the left side of the three commitments.

That is the whole device: *these three hang off me.* It is also the **same idiom as the bridge** on slides 2 and 3 — a support with things hanging from it — so slide 1 starts speaking the deck's visual language instead of being a text slide with a photo beside it. Thin, partial opacity: structure, not a highlight.

**3 · Under your name, two small lines.** *Team Lead*, then under a thin rule:

> **Mechanical engineer by training. Process engineer by choice.**

Nine words carrying the origin story the narration spends 35 seconds on. *By training* says the discipline is real and learned — what the subtitle already claims. *By choice* says it was not a career accident. Small and quiet: a margin note, not a headline.

**4 · The commitments, restated in engineering language — and now four of them.** Same source in `principles.md`, reworded so they read as the instincts of the engineer the origin line describes, rather than as management values.

| | Was | Now | From `principles.md` |
|---|---|---|---|
| 1 | Enabling, never gatekeeping | **Diagnostics, not verdicts** — *metrics and compliance are instrumentation; they show where the system strains, not who to blame.* | *metrics and compliance as diagnostic tools, not gatekeepers* |
| 2 | Accountable autonomy | **Tolerances, not instructions** — *flexibility with guidance: you know what is expected, and you own the outcome.* | *autonomy with accountability* |
| 3 | Outcomes over activities | **If it doesn't carry load, it comes out** — *we challenge the value of our own work first. What stays is what makes the system hold.* | *outcomes over activities — no excessive paper trail* |
| 4 | *(was the closing spoken beat)* | **Zero surprises, not zero problems** — *transparency and humbleness are not negotiable in this team. You hear it from us first — our gaps, and anything about to change.* | *transparency and humbleness are non-negotiable* |

**Why this is the change worth making.** All four are now in one of two forms — couplet or rule — and none of them are management phrasing.

| | Head | Form | Words |
|---|---|---|---|
| 1 | Diagnostics, not verdicts | couplet | 3 |
| 2 | Tolerances, not instructions | couplet | 3 |
| 3 | If it doesn't carry load, it comes out | rule | 7 |
| 4 | **Zero surprises, not zero problems** | couplet | 5 |

**Why #4's couplet is the strongest of the four.** *Zero surprises* alone would be a boast. The turn — **not zero problems** — is what makes it land: it concedes the failures in the same breath as it promises the disclosure, so **transparency and humbleness are both delivered in five words** without either word appearing. It is also the only line on the slide that admits something, which is what makes the other three read as confident rather than as marketing.

It also covers more ground than the *"reported, not discovered"* version it replaced: that only promised self-reporting to auditors, whereas this promises this room that **a process change will never land on their team unannounced** — their actual friction with PE, not audit findings.

> **Alternative, if you would rather it be a rule than a couplet:** **"If it surprises you, we got it wrong."** Same content, same self-accountability, and it pairs structurally with #3 (both *If X, then the failure is ours*). That would make the set two couplets and two rules — cleaner symmetry, slightly less memorable. I would keep the couplet: *not zero problems* is the part people will repeat.

> ⚠️ **Say the turn as two sentences out loud** — *"Fourth: zero surprises. Not zero problems."* The pause is what makes the second half land. Read as one breath it sounds like a qualifier; read as two it sounds like honesty.

> If you want only one couplet in the set, the one to change is **#1**, not #2 — *tolerances, not instructions* is the best expression of "flexibility with guidance" available. A non-couplet alternative for #1 is **"We measure to find the slack"**, which echoes the origin paragraph directly (*"I cannot leave a system alone once I can see the slack in it"*). ⚠️ But be careful: in an ops room, "finding the slack" can be heard as hunting for waste to cut — i.e. headcount. *Diagnostics, not verdicts* does the reassurance work without that risk, which is why I left it.

**#4 was a spoken closing beat and is now a bullet**, which is an upgrade: it was the strongest thing on slide 1 and it was invisible. The narration now runs *"Fourth — reported, not discovered. And this is the one I hold hardest…"*, so slide 1 ends on it rather than trailing off. The urgency-and-limits line (**"if it needs heroics to hold, we designed it wrong"**) follows as a coda to all four rather than being buried inside #4 — it is a different principle and it dilutes the transparency point if merged.

More importantly: the triad stops being a values list any leader could put up, and becomes **the behavioural signature of the person in the photo beside it.** The origin line, the tie and the three heads now all say the same thing — which is what makes the slide personal without adding a single sentence.

**Say the through-line out loud**, right after the origin paragraph:

> Which is why **the things I hold this team to sound like engineering, not management.** Four of them, and you can hold me to all four.

> Audience check: this is an engineering-ops room — SRE, Release Engineering, Quality Engineering. *Tolerances* and *carries load* are their vocabulary, not jargon being imported. In a non-engineering room the plain-language heads would be the safer choice.

**And the surroundings do the rest.** *"Hold me to"* makes them promises with a name attached. The tie makes them visibly **yours**. The origin line says where they came from.

> ⚠️ **"me" or "us" is a real call.** `writing_style.md` reserves "I" for facilitation and uses "we" for team work, so *"hold me to"* is a deliberate exception — on a slide titled *who we are as leaders*, the leader owning the promise is the point, and it is the most personal word available at no cost. **"Hold us to"** is the safer variant and matches the rest of the script's voice. One-word edit either way; the accent sits on that word.

> The **four V2MOM values are deliberately not on this slide.** An earlier draft paired each commitment with one of them and stood all three on a Continuous Improvement footing — accurate, but it turned the slide into a mapping exercise, and these three commitments *are* the values this room needs. The four stay in the V2MOM and the narration.
