---
title: Measuring Change Failure Rate
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/5458165963/Measuring+Change+Failure+Rate
confluence_space: RKB
confluence_page_id: 5458165963
last_synced: 2026-04-09
owner: Process Engineering
---

# Measuring Change Failure Rate

13falsenonelisttrue## **Problem Statement**
We are currently utilizing the*** Deployment Failure Rate ***(DFR) metric to monitor the technical reliability of our Continuous Integration/Continuous Delivery (CI/CD) pipeline. While DFR effectively tracks interruptions during the deployment *process* itself (e.g., build errors or infrastructure timeouts), it fails to capture the true **post-release stability** and the resulting **business impact** of successful deployments that introduce flaws. 

**We lack a standardized, outcome-oriented metric to quantify how often a code change, once deployed, leads to a significant failure, incident, or service degradation** in the production environment requiring immediate corrective action.

This gap prevents us from having an objective view of our system's reliability, obscuring the true cost of poor quality and hindering data-driven decisions regarding necessary investments in automated testing, code health, and engineering processes. 

## **Solution Proposed**
To address this, we propose adopting the **DORA **(*DevOps Research and Assessment*) metric - `Change Failure Rate (CFR)` as a key measure of software delivery quality, enabling data-driven decisions to improve stability and effectiveness across our SDLC. Moving to the **Change Failure Rate (CFR)** is essential to shift our focus from merely monitoring the deployment *activity* to measuring the **quality of the change artifact** and its impact on the customer experience.

CFR measures the percentage of changes deployed to production or released to customers that result in a degraded service and subsequently necessitate remediation. **It represents the proportion of deployments that introduced instability.**

### **Why?**
Measuring and understanding CFR allows a **more effective risk management within deployment strategies.** Accurately knowing the rate at which changes lead to production issues, and understanding the nature of these issues, enables organizations to strike a more informed balance between delivery speed (measured by metrics like Deployment Frequency and Lead Time for Changes) and stability:

- 
A consistently low CFR can build confidence, potentially encouraging more frequent, smaller deployments, as the inherent risk per deployment is demonstrably low.

- 
A high CFR clearly signals that current processes may be too risky, requiring stronger pre-deployment checks, stricter testing, or safer rollout strategies.

While your current metric, **Deployment Failure Rate**, is useful for monitoring the reliability of your CI/CD pipeline (e.g., failures due to infrastructure errors or timeouts), the **Change Failure Rate **offers a far more critical and business-relevant perspective:

**Deployment Failure Rate**

(what we have)

**Change Failure Rate**

(what we want to have)

Percentage of deployments that fail.

E.g. of failures: pipeline errors, failed builds/test, Helm/Kubernetes deployment errors.

`Failed deployments &divide; Total deployments`

Percentage of changes (code, configuration, infrastructure) that lead to a failure in the production environment, requiring some form of remediation (rollback, hotfix, patch).

E.g., service outage, performance degradation, bug requiring a quick fix or rollback.&nbsp;

`Failed changes &divide; Total changes deployed`

It primarily shows the health and efficiency of our Continuous Integration/Continuous Deployment (CI/CD) pipeline.

It reflects the overall stability and reliability of our software and the effectiveness of our development and testing practices.&nbsp;
Understand the impact of our work on our users.

Typical Goal:

Low failure in automation/pipelines (near 0%)

Typical Goal:

DORA benchmark: Elite teams keep CFR between 0&ndash;15%

  
### **How?**
This chapter defines the methodology and data sources used to calculate our Change Failure Rate. CFR is calculated by dividing the number of **Failure Events** by the total number of **Change Events** within the same reporting period.

#### **Change Events:**
We track two primary sources of change to capture both automated and manual interventions.

- 
**Asset Changes:** Every asset version deployed or rolled back in a ring following the standard ODC delivery lifecycle.

- 
**RFC Changes:** Manual changes performed in a ring and associated with an asset, registered in the [**RFC project**](https://outsystemsrd.atlassian.net/jira/software/c/projects/RFC/boards/2191).

What is considered a ***Change***?

For a manual change to be counted in the metric, it must meet the following:

- 
**Status:** Must be in `Completed` status.

- 
**Excluded Categories:** Must **not** be categorized as `Fast Track`, `Rollback`, or `Promote to Standard`.

- 
**Environments (rings):** Limited to `ring-osall`, `ring-ea`, or `ring-ga`.

- 
**Timestamp:** The event is recorded based on the `Implementation Date`.

#### **Failure Events**:
Failure events are identified through the **RDINC** project. These represent incidents triggered by a specific change.

What is considered a** *****Failure*****?**

To be classified as a failure, an incident must meet **all** of the following requirements:

- 
**Project **: Registered in the [RDINC project](https://outsystemsrd.atlassian.net/jira/software/c/projects/RDINC/boards/2269) as an incident occurring after a change is performed. 

- 
**Resolution Status:** Must have reached a final or near-final state: `Solved`, `Retrospective In Progress`, `Retrospective Completed` or `Closed`.

- 
**Incident Type**: Must be classified as: `Customer Reported`, `System-wide SLO trigger`, `Service Specific SLO`, `Internal`.

- 
**Affected Environments (Rings)**: Only incidents affecting `ring-osall`, `ring-ea` or `ring-ga`.

- 
**Root Cause Categorization**: Must be **different **from `Customer issue` and `Self Recovered`.

- 
**Reporting Window:** The status changed within the `last 15 days`.

- 
**Timestamp:** The failure is logged based on the **RDINC Creation Date**.

- 
**Data Filtering:** Must **not** contain the label `CFR-processed` (to ensure only new, unique data is analyzed).

&nbsp;

The calculation of the CFR is done by the following formula:

( `Number of failed changes` / `Total number of changes` ) x 100