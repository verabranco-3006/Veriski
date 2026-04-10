---
title: Failure Management
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/5445779471/Failure+Management
confluence_space: RKB
confluence_page_id: 5445779471
last_synced: 2026-04-09
owner: Process Engineering
---

# Failure Management

none## Problem Statement
Currently, different use cases - such as customer incidents, alerts, SLO breaches, manually created incidents and failures - are all managed within a single Jira project, [**RDINC project**](https://outsystemsrd.atlassian.net/jira/software/c/projects/RDINC/boards/2269)**, ** using the same ***Incident***** **issue type. The only way to differentiate between these critical scenarios is through ***labels** *added during issue creation.

## Impact
This reliance on labels creates significant problems:

- 
**Data Inconsistency:** Labels are an unstructured and inconsistent method for distinguishing issues, which makes it extremely difficult to validate, filter, or reliably generate accurate data and metrics. This directly impacts our ability to manage the response and analyze trends, making the process **risk-prone**.

- 
**Overly Complex Automation:** We must maintain several complex automation rules that are solely dependent on labels to handle the different use cases.

- 
**Inadequate Field Management:** Many existing Jira fields within RDINC Project are not relevant for all the different *Incident* types, leading to confusion and unnecessary noise.

## High-Level Solution Proposed
To address the current use cases lying in the RDINC Project, the **deployment failures on Pegasus** **will now be reported in a different Jira Project**:

- 
**For Incidents and Alerts - **keep these issue types within the current RDINC Project and split into two different issue types:

- 
**Incidents - **to address customer reported, incidents created manually by teams, and SLO breaches.

- 
**Alerts - **to address alerts coming from alerting tools such as Grafana and Nobl9

&nbsp;

- 
**For Deployment Failures -** these issues will be migrated into a completely new Jira project - [RDODCF - ODC CD Failures](https://outsystemsrd.atlassian.net/jira/software/c/projects/RDODCF/boards/3099) - to cover all the use cases.

This separation will allow us to create tailored workflows, automation, and required fields for two fundamentally different response processes.

### What is expected from each team?
*Pegasus *automatically creates Jira issues of the ***Failure*** type for every failure occuring in any lifecycle stage. These are logged in the new Jira project: [RDODCF - ODC CD Failures](https://outsystemsrd.atlassian.net/jira/software/c/projects/RDODCF/boards/3099).

Each issue is automatically assigned to the responsible team based on ownership data from **Backstage**. Teams are expected to:
- 
**Analyze the issue:** Investigate and identify the accurate Root Cause.
*Priority Note:* Failures created for ***positive Rings ***- `ring-ga`, `ring-ea` and `ring-osall` - should be addressed with higher priority.

- 
**Create Action Items:** **Define relevant tasks** to address and fix the underlying problem within your team's scope.

- 
**Report External issues: **If the root cause is external to your team (e.g., categorized as **Infrastructure** or a **Dependency**), it **MUST** be reported to the respective owner teams (e.g., Platform Engineering for infra; the relevant service owners for dependencies) to ensure the issue is addressed at the source.
 To ensure data accuracy, please read more about how to **correctly categorize** the Failure Root Cause here.

notedf5680610dba
This Jira Filter can be used to check all the Failures that require invetigation: 
[RDODCF - Open Failures](https://outsystemsrd.atlassian.net/issues/?filter=53241&amp;atlOrigin=eyJpIjoiMjExM2NmMzZkZWQ1NGU2NTllMDkxMzIwZTFmOWNjMjgiLCJwIjoiaiJ9)

This Jira Filter can be used to check all the Failures that require invetigation: 
RDODCF - Open Failures

**It is critical that teams analyze and close assigned Failures promptly.** Maintaining a clean backlog is vital for our system health and governance:

- 
**Accountability:** Ensures every failure is tracked from detection through to root cause analysis and resolution.

- 
**Process Governance:** Timely closure allows us to learn from failures while the context is fresh, effectively preventing recurrence.

- 
**System Stability:** High-quality data helps us identify broader patterns (whether infrastructure or code-related), allowing us to prioritize the right stability improvements.

When Failures remain open for too long, it becomes difficult to distinguish between what has been resolved and what still requires attention, leading to a loss of visibility into our real operational state.

More information about this Jira project here: What does an ODC CD Failure look like in Jira?