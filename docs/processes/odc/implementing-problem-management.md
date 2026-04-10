---
title: Implementing Problem Management
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/5036841027/Implementing+Problem+Management
confluence_space: RKB
confluence_page_id: 5036841027
last_synced: 2026-04-09
owner: Process Engineering
---

# Implementing Problem Management

Version Control - Current Version - 1.0 / Release Date - 

**Table of Contents**
16falsenonelisttrue## Problem Statement
The current Incident Response process was initially designed from an &ldquo;always green&rdquo; perspective. This means that issues must be investigated and fixed, regardless of severity.&nbsp;

However, these two years of process execution have shown that there are scenarios in which teams may decide to postpone incorporating a permanent solution by providing documentation of known errors to support troubleshooting future incident occurrences or even choosing not to fix them. 

Despite the existence of** known errors **produced ad-hoc by some teams (example [here](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/3653502020/Known+Problems+Runbooks+For+Global+Support))), their **lack of visibility **makes Support teams troubleshoot the same issue multiple times causing a waste of time and effort over topics that were already covered and documented before and whose context can be transmitted to the customer right away.

## Impact   
Due to this way of working, several critical problems arise:
- 
Incidents reported by customers are opened for longer times than the targets defined - increased MTTR.

- 
Customers not able to find the issues provided in the Release notes - compromised customer experience.

- 
Unnecessary on-calls for Engineering - increased costs.

## What is Problem Management?
The main purpose of Problem Management is **to reduce the likelihood and impact of incidents by identifying their actual and potential causes, and managing workarounds and known errors.**

The scope of this procedure is applicable to the **Global Support Teams **and** R&amp;D Teams.**

Problem Management Procedure can be found on &ldquo;[OS Policies](https://drive.google.com/file/d/14Rn3d0gSpCH4vHh2RbJySvPFL9HHlwMr/view?usp=sharing)&rdquo; and is available to all company.

**Definitions and concepts related with Problem Management**

- 
**Problem Record** - Jira issue that represents a Problem. It is used to work problems, register all their information, and track their progress.

- 
**Root Cause **- It represents the original or underlying cause behind an incident or Problem.

- 
**Known-error **- This refers to a documented Problem, with a known root cause and a workaround.

## High-Level Solution Proposed
Similar to what happened in O11, we will implement a **Problem Management** practice in ODC Engineering that will serve as an abstraction layer for all product issues, whether **product bugs** or **vulnerabilities. **

This will provide Global Support and other stakeholders, such as the Security Team, **visibility over the progress** of any related bug raised to fix a problem or security vulnerability.

The successful implementation of this solution will also allow OutSystems to **provide visibility** to our customers about the status of **known issues** affecting their journey, without compromising their current experience, and promote the **autonomy **of our Support lines in troubleshooting any problems reported by our customers.

From an **execution point of view**, this solution will use an existing Jira project - [R&amp;D Problem Management](https://outsystemsrd.atlassian.net/jira/software/c/projects/RPM/boards/2251) - that will be managed by Engineering Teams.

- 
R&amp;D teams are responsible for fixing the reported issues and to report on process progress.

- 
Once a Problem Record is fixed, release notes must be produced and publicly displaced to the customers.

## Solution Details 
Through Problem Management, we provide customer visibility and traceability for issues that might affect them, and it also works as a known error database for both R&amp;D and Global Support teams.

The created Problem Records (ODC RPMs) will serve as information aggregators, primarily contributing to the following goals:

- 
Track progress over tasks to fix confirmed **Security Vulnerabilities**

- 
Provide **Customer-facing** information

- 
Maintain an **Internal Database of known errors**, which includes proactive creation of Root Cause Analysis, particularly for Vulnerabilities.

For more details, please refer to Streamline Vulnerability Management in ODC .

We are adopting a phased roll-out approach for the **ODC Problem Records**. The core concept is to use these Jira issues as central information hubs, linking bugs and changes directly to them.

### When should Problem Records be created?
As mentioned before, one of the main goals of creating an ODC Problem Record (**ODC RPM**) is to provide visibility to any relevant stakeholders who are or could be affected by an issue within ODC.

As such, a** Problem Record **should be created when there is a need:

- 
To provide traceability of a Problem (either by customer request or proactively)

- 
To inform other teams internally that a problem exists.

As examples:

- 
A **Vulnerability **was found and visibility about it must be given the following Streamline Vulnerability Management in ODC.

- 
**Documentation-related** problems are registered to record documentation updates and provide visibility.

- 
An **Incident** has been recovered, and **Bugs** have been identified but not fixed during Incident Recovery.