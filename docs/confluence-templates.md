---
title: Confluence Page Templates (EEO Space)
space: EEO — Process Engineering
last_updated: 2026-04-30
owner: Vera Branco
---

# Confluence Page Templates — EEO Space

Authoritative structure for any page Vera asks me to create or draft for the **Process Engineering (EEO)** Confluence space. Every page in this space — including project charters — must follow the **Page Template wrapper** below. Specialised page types (e.g. Project Charter) layer their own sections under the wrapper.

Source templates:
- [Template] - Page on the space — https://outsystemsrd.atlassian.net/wiki/spaces/EEO/pages/5914460179
- [Template] Project Charter — https://outsystemsrd.atlassian.net/wiki/spaces/EEO/pages/4778164500
- "Read more" reference page — https://outsystemsrd.atlassian.net/wiki/spaces/EEO/pages/5801377846

---

## 1. Page Template Wrapper (applies to ALL pages)

Every page starts with this header block, in this exact order:

```
**Governance ID -** [ID of the document if applicable]

**Current Version -** 1.0

**Release Date -** <date macro>

**Status -** <status macro: Work in Progress | Approved Document | Deprecated/archived>

Please read the following page for more details - <smartlink to https://outsystemsrd.atlassian.net/wiki/spaces/EEO/pages/5801377846>

---

**Table of Contents**

---

<page-specific content starts here>
```

Notes:
- `Status` uses Confluence status macros, not plain text. Show all three options inline so reviewers can flip between them, with the active one first.
- The two `---` rules wrap the **Table of Contents** macro (the auto-generated one, not a manual list).
- The smartlink is always to page **5801377846**.

---

## 2. Project Charter (specialised page)

Used for the **Discover phase** of process design. Sits under the Page Template wrapper above.

After the wrapper's TOC divider, charter content uses these H3 sections:

```
### Overview

* **Key Stakeholders**:
  _(Primary individuals or teams involved in or affected by this project.)_
* **Objective**:
  _(Purpose or goal of this project.)_

---

### Current Problem Statement

* **Problem Description**:
  _(Briefly describe the current problem. Identify the root cause._
  _List or map the key steps in the current way of working._
  _Key problems, inefficiencies, frustrations.)_
* **Tools and Systems Used**:
  _(Tools, systems, or software supporting the current solution.)_
* **Performance Metrics**:
  _(Metrics used to measure the process. Include current performance if known.)_

---

### Opportunities for Improvement

* **Improvement Areas**:
  _(Aspects of the actual solution with the most potential for improvement.)_
* **Risks or Constraints**:
  _(Risks or limitations that might impact the redesign. Include a mitigation plan.)_

---

### Research and Benchmarking _(optional)_

* **Industry Best Practices**:
  _(Known best practices for similar processes. Reference Mendix, Meta, Spotify, Netflix, Talkdesk, etc.)_
* **Comparative Metrics**:
  _(How does the current solution compare to benchmarks or competitors?)_
```

Notes:
- Sections are H3 (`###`), not H2.
- Each section is followed by a horizontal rule (`---`).
- Section content is bulleted with **bold labels** and italicised guidance text in parentheses.
- "Research and Benchmarking" is **optional** — drop it when not relevant.
- Adjust which sub-bullets apply per problem; not every charter needs every field. The wrapper headers (Governance ID through TOC) are non-negotiable.

---

## 3. Defaults to use when drafting

When Vera asks me to draft a page or a project charter and doesn't specify, default to:

| Field | Default |
|---|---|
| Governance ID | leave as `[ID of the document if applicable]` placeholder |
| Current Version | `1.0` |
| Release Date | today's date |
| Status | `Work in Progress` (active), with `Approved Document` and `Deprecated/archived` shown as inactive options |
| Smartlink target | `5801377846` |

---

## 4. Format selection when calling Confluence MCP

Use `contentFormat: "markdown"` for reading, but for **writing** structured pages prefer the HTML format — it preserves panels, status macros, smartlinks, and the TOC macro, which markdown drops.
