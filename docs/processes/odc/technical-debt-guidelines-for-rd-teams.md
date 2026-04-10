---
title: Technical Debt - Guidelines for R&D Teams
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/5223776327/Technical+Debt+-+Guidelines+for+R+D+Teams
confluence_space: RKB
confluence_page_id: 5223776327
last_synced: 2026-04-09
owner: Process Engineering
---

# Technical Debt - Guidelines for R&D Teams

none
## **When to create Tech Debt Issues?**
Creating Technical Debt issues in Jira is crucial for **effective management**. It's also important to **monitor the state of Technical Debt across R&amp;D teams**. To ensure full visibility, each team member should proactively log these items in the designated Jira project.

The &quot;when&quot; can vary, but generally, you should create a Tech Debt issue:
- 
**During a Sprint/development cycle:** If the team decides to take a shortcut to meet a deadline, release an MVP, or achieve a critical short-term goal.

- 
**During code reviews:** If a code review reveals an area that could be improved, is difficult to maintain, or deviates from best practices, but it's not a critical bug blocking current work.

- 
**During bug fixing or new feature development:** Often, developers encounter areas that are messy, hard to understand, or introduce unnecessary complexity.

- 
**When a dependency becomes outdated:** As libraries and frameworks evolve, older versions can become security risks or create compatibility issues.

- 
**When new best practices emerge:** Over time, what was considered good practice might be superseded by better approaches, requiring a refactor.

- 
**Performance bottlenecks:** If a part of the system is performing poorly due to underlying architectural or code choices, but it's not a full outage.

- 
**Security vulnerabilities:** Discovering a non-critical security flaw that requires refactoring or a specific fix.

- 
**Lack of documentation:** If crucial parts of the system lack sufficient documentation, making it hard for new team members or for future maintenance.

- 
**Action items from Incident Retrospectives:** If an Incident occurred due to a systemic weakness, a workaround, or a quick fix that needs a proper long-term solution.

- 
**Team reflections:** Teams might identify areas of inefficiency in their processes, tools, or codebase during regular Retrospectives that manifest as technical debt.

The key is to **document it promptly** so it doesn't get forgotten, can be prioritized, and contributes to a transparent &quot;health&quot; view of our product.

&nbsp;
### Is it Tech Debt? A Quick Checklist for Developers
To make it easy for a software developer to determine if a particular issue is **Tech Debt**, here's a list of Yes/No questions. If **at least one** of these questions is answered with &quot;Yes,&quot; then it's considered Tech Debt.

**Question**

**Yes**

**No**

Does addressing this issue **improve the maintainability, scalability, or performance** of the existing codebase without adding new user-facing features?

&nbsp;

&nbsp;

Was this issue created by a past decision or **shortcut that prioritized speed of delivery** over long-term code health or best practices?

&nbsp;

&nbsp;

Was this implemented as a **quick fix or temporary solution**?

&nbsp;

&nbsp;

Is this issue causing **recurring problems, bugs, increased effort for future development, or impeding the team's** ability to deliver new features efficiently?

&nbsp;

&nbsp;

Does this issue involve **outdated technologies, libraries, or architectural patterns** that are no longer supported or are becoming an obstacle?

&nbsp;

&nbsp;

Is the code not covered by **automated tests or difficult to test**?

&nbsp;

&nbsp;

&nbsp;
## **How to create Tech Debt Issues?**
**Filling out a few key fields accurately** will provide valuable information about their origin, impact, and nature of Tech Debt affecting our product. This improved visibility will** empower teams to better prioritize and manage their Technical Debt**.

&nbsp;

Here's the guideline we're proposing to achieve that:

  - This means that&rsquo;s a ***mandatory rule*** because it's the only way we can create a shared dashboard for all teams to monitor their &ldquo;Tech Debt backlog health&rdquo;, and also gain a true overview across our product.

- 
 Create the issue in your **team&rsquo;s Jira Project.**

- 
 Use the ***Issue Type***** &ldquo;Tech Investment&rdquo;**.

- 
We know that sometimes you may need to perform research to understand how to proceed with the implementation. If you want to create a specific issue for that in your backlog, please use the **&ldquo;Spike&rdquo; Issue Type **(in this case, make sure you follow the next step).

- 
 Assign the ***R&amp;D Account***** &ldquo;Debts &amp; Acceleration&rdquo;** to the issue.

- 
To keep your backlog organized, it's a good practice to **create these issues under an Epic**, perhaps named &quot;Technical Debt&quot;. 
That *parent Epic* should have the *R&amp;D Account* &ldquo;Debts &amp; Acceleration&rdquo;, and the *Roadmap Type* field should be &ldquo;Architecture Debt&rdquo;, &ldquo;Tech Debt&rdquo; or &ldquo;UX Debt&rdquo; accordingly.

- 
For larger backlogs with diverse technical debt topics, consider **creating multiple Epics** **by category or component **(&ldquo;buckets&rdquo;), such as &ldquo;Quality Debt&rdquo;, &quot;Architecture Debt&quot; or &quot;Database Improvements&quot;.

- 
**Categorize by *****Type*****:**
Use ***Labels ***to indicate the type of Technical Debt. Common examples include: `architecture`, `performance`, `quality`,  `security-debt`, `tech-upgrade`.

- 
**Categorize by *****Component*****:**
Add ***Labels ***corresponding to the affected component (e.g., `auth-service`, `frontend`, `database`) to indicate where the Technical Debt is present.

- 
Consider to include a **meaningful prefix** in the issue name (e.g., the component's name) to provide immediate context without needing to open the issue.

- 
In the ***Description *****field**, try to include as much useful information as you can.

note
Example:

** Context / Background**

Explain how the technical debt came to exist.

**⚠️ Problem / Impact**

Describe what problems this debt causes.

**🛠️ Proposed Solution**

Outline a suggested path to address the debt.

🔗** Dependencies / Risks**

Note anything that may block or be affected by this work.

**✅ Acceptance Criteria**

Clearly define what &quot;done&quot; means.

Example:

💼** Context / Background**

Explain how the technical debt came to exist.

**⚠️ Problem / Impact**

Describe what problems this debt causes.

**🛠️ Proposed Solution**

Outline a suggested path to address the debt.

🔗** Dependencies / Risks**

Note anything that may block or be affected by this work.

**✅ Acceptance Criteria**

Clearly define what &quot;done&quot; means.

&nbsp;

- 
The ***Priority *****field** helps teams identify which issues to address first. 
Please refer to the following guidelines to help you choose the appropriate priority level:** **Technical Debt - Guidelines for R&amp;D Teams

&nbsp;

- 
If the technical debt originates from another Jira issue - such as a *Value Milestone* or an *Action Item from an Incident Retrospective* - **link it to the corresponding Jira issues**. This helps us understand its root cause.

- 
***Jira automations*** can help your team manage Technical Debt more efficiently.
Examples:

- 
Automatically populate the *R&amp;D Account* and the *Parent *(Epic) fields when creating a new issue with the &ldquo;Tech Investment&rdquo; issue type. 
*Note: R&amp;D Account field should already be automatically filled with &ldquo;Debts &amp; Acceleration&rdquo;.*

- 
Send an email or Slack message with a list of newly created Tech Debt issues at the end of each Sprint.

&nbsp;
## **How to prioritize Tech Debt Issues?**
This guide helps teams assign the correct **priority (Urgent, High, Normal, Low)** to Technical Debt issues based on their **impact, urgency, and strategic value**.

🔴 **Urgent**

**When to use:**

- 
Blocking a delivery, feature, or initiative

- 
Action item from a critical incident

- 
Frequently causes severe bugs/incidents

- 
Has a near-term due date

- 
Security, compliance, or CI/CD breaking issue

**Impact:** High and immediate
**Action:** Fix as soon as possible

🟠 **High**

**When to use:**

- 
Reduces team productivity significantly

- 
Related to repeated bugs or issues

- 
Prevents future roadmap work

- 
In a code area modified often

- 
Structural fix needed for stability

**Impact:** High but not blocking
**Action:** Schedule soon (next sprints)

🟡 **Normal**

**When to use:**

- 
Affects maintainability or test coverage

- 
Code is stable but messy or outdated

- 
Helpful for clarity or consistency

- 
Not blocking current work

**Impact:** Medium
**Action:** Add to tech backlog

🟢 **Low**

**When to use:**

- 
Cosmetic or style issues

- 
Legacy code rarely touched

- 
Quick wins with low impact

- 
Nice-to-have or optional improvements

**Impact:** Low
**Action:** Do when possible

 Teams may also **categorize Technical Debt issues based on priority**. For instance, using ***Labels ***such as `quick-win`, `customer-facing`, `release-blocker` can clarify the impact of these issues.

&nbsp;
## **How to allocate capacity for Tech Debt Issues?**
Allocating capacity in R&amp;D teams to address Technical Debt is key to keep long-term velocity, code quality, and developer happiness.

Below are some ideas to help embed Tech Debt work into your team&rsquo;s workflow:

**Model**

**Description**

**Frequency**

**Advantage**

**Fixed % per Sprint**

Reserve **percentage of Sprint capacity** for Tech Debt.

Every Sprint

Easy to implement, promotes regular cleanup.

**Tech Debt Rotation**

Assign **1 team member per sprint** to own Tech Debt tasks.

Every Sprint

Promotes shared responsibility and visibility.

**Quarterly Tech Debt Week/Sprint**

Block **1 week or Sprint** per quarter to focus only on Tech Debt cleanup.

Quarterly

Great for tackling bigger backlog items and reducing risk.

**Debt Budget**

Allow **1-2 tickets per sprint** as flexible Tech Debt cleanup.

Every Sprint

Encourages autonomy and responsibility.

**Free Slot Fix**

When someone is **&ldquo;free&rdquo;**,  **they're encouraged** to tackle a Tech Debt task.

Every Sprint

Promotes regular cleanup.

&nbsp;
## **Make Technical Debt visible**
Making Technical Debt visible **helps teams understand, prioritize, and manage it effectively**.

Here are some ideas for teams to apply to their Jira boards, which will help understand the size and impact of their Tech Debt backlog:

&nbsp;

- 
**Use filters in the Jira board**

Create a ***Quick Filter***, in the team&rsquo;s Jira board configurations, to display all Tech Debt issues. You can use the *Issue Type* or the *R&amp;D Account* fields in your query, for example.

With this filter activated, only Technical Debt items will be shown on the board, making them easier to identify and prioritize.

&nbsp;

If you have specific Epics for Tech Debt issues, you can also **filter by the Epic**:

&nbsp;

- 
**Have a specific board for Tech Debt issues**

A **new Jira board** can be created within the team Jira project to shows only Technical Debt issues, by filtering using fields like *Issue Type* or *R&amp;D Account*.

- 
**Make Labels visible in the Team&rsquo;s backlog**

If your team uses *Labels *to categorize Tech Debt issues by type (or for other purpose), **make the *****Labels *****field visible in the backlog** for a clearer overview of the issue types.

&nbsp;
## **Review your team Technical Debt backlog periodically**
Regularly reviewing Technical Debt is essential for **keeping it manageable and preventing it from accumulating** to a point where it significantly impacts development velocity or product quality.

Here are some ideas for teams to review their Technical Debt periodically, incorporating various approaches and cadences:

**Model**

**Description**

**Frequency**

**Advantage**

**Sprint Planning / Backlog Refinement**

Review and prioritize Tech Debt items with features/bugs.

Weekly/
Bi-weekly

Consistent reduction.  Integration into workflow.
Prioritization visibility.

**Sprint Retrospectives**

Identify new Tech Debt.
Review progress and impediments. Analyze root causes.

Bi-weekly/
Monthly

Prevention of new debt. Continuous process improvement. 
Impediment resolution

**Sprint Reviews /**
**Operational Reviews**

Showcase resolved Tech Debt to stakeholders (if relevant).
Share &quot;health&quot; metrics.

Bi-weekly/
Monthly

Stakeholders understand value. Transparency of effort. 
Feedback and recognition.

**&quot;Tech Debt Deep Dive&quot; Meeting**

Detailed Tech Debt backlog review.
Triage, categorization, and re-prioritization.

Monthly/
Quarterly

Backlog clarity. Updated priorities. Concrete action plan.

&nbsp;
## **Measure progress**
**Tracking and analyzing Tech Debt metrics with the team is essential** - it enables informed decisions about where to **invest time and resources**, and supports** continuous improvement** in the health, maintainability, and sustainability of the codebase..

To support this, the team should **periodically review key Technical Debt metrics**, such as:

- 
Number of open Tech Debt issues

- 
Number of Tech Debt issues resolved per Sprint

- 
Time spent addressing Tech Debt

- 
Ratio of Tech Debt work vs. feature work

These insights can be shared during Team Retrospectives or Planning Meetings to increase visibility, raise awareness, and justify investments in technical quality.

 And don&rsquo;t forget to **celebrate the wins**! Recognize teammates who tackle long-standing issues with **&ldquo;Tech Debt of the Month&rdquo; shoutouts** - a great way to promote a culture of continuous improvement and shared ownership.