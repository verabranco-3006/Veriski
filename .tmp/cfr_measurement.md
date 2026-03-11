none

* * *

## **Problem Statement**

We are currently utilizing the _**Deployment Failure Rate**_(DFR) metric to monitor the technical reliability of our Continuous Integration/Continuous Delivery (CI/CD) pipeline. While DFR effectively tracks interruptions during the deployment _process_ itself (e.g., build errors or infrastructure timeouts), it fails to capture the true **post-release stability** and the resulting **business impact** of successful deployments that introduce flaws.

**We lack a standardized, outcome-oriented metric to quantify how often a code change, once deployed, leads to a significant failure, incident, or service degradation** in the production environment requiring immediate corrective action.

This gap prevents us from having an objective view of our system's reliability, obscuring the true cost of poor quality and hindering data-driven decisions regarding necessary investments in automated testing, code health, and engineering processes.

## **Solution Proposed**

To address this, we propose adopting the **DORA**( _DevOps Research and Assessment_) metric - `Change Failure Rate (CFR)` as a key measure of software delivery quality, enabling data-driven decisions to improve stability and effectiveness across our SDLC. Moving to the **Change Failure Rate (CFR)** is essential to shift our focus from merely monitoring the deployment _activity_ to measuring the **quality of the change artifact** and its impact on the customer experience.

CFR measures the percentage of changes deployed to production or released to customers that result in a degraded service and subsequently necessitate remediation. **It represents the proportion of deployments that introduced instability.**

### **Why?**

Measuring and understanding CFR allows a **more effective risk management within deployment strategies.** Accurately knowing the rate at which changes lead to production issues, and understanding the nature of these issues, enables organizations to strike a more informed balance between delivery speed (measured by metrics like Deployment Frequency and Lead Time for Changes) and stability:

- A consistently low CFR can build confidence, potentially encouraging more frequent, smaller deployments, as the inherent risk per deployment is demonstrably low.

- A high CFR clearly signals that current processes may be too risky, requiring stronger pre-deployment checks, stricter testing, or safer rollout strategies.


While your current metric, **Deployment Failure Rate**, is useful for monitoring the reliability of your CI/CD pipeline (e.g., failures due to infrastructure errors or timeouts), the **Change Failure Rate** offers a far more critical and business-relevant perspective:

| <p local-id="1995b2fe-906d-471e-8e3c-9076106b9986"><strong>Deployment Failure Rate</strong></p><p local-id="86887b07-584c-4980-88ef-f93d8bb29e9c">(what we have)</p>                                                                                                                                                                                         | <p local-id="6012a281-3a3d-4d3e-aa49-f1ba3db3b9df"><strong>Change Failure Rate</strong></p><p local-id="92b16acc-217d-4cc9-949d-1ab48f077b90">(what we want to have)</p>                                                                                                                                                                                                                                                                                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <p local-id="fc8c64f4-a597-4d22-bd9f-eb6a3e78f18a">Percentage of deployments that fail.</p><p local-id="7bcc942a-0ad3-4d07-be00-ddf65fa1c9ab">E.g. of failures: pipeline errors, failed builds/test, Helm/Kubernetes deployment errors.</p><p local-id="2ec1e6c7-bffd-4b08-af5a-90a855444d99"><code>Failed deployments &divide; Total deployments</code></p> | <p local-id="a287d071-e3bb-4bdf-9411-237a01e06196">Percentage of changes (code, configuration, infrastructure) that lead to a failure in the production environment, requiring some form of remediation (rollback, hotfix, patch).</p><p local-id="971f7cb1-36fe-486f-b608-d09fd345acfb">E.g., service outage, performance degradation, bug requiring a quick fix or rollback.&nbsp;</p><p local-id="7a245e10-011a-47a7-8167-5b4e31b1bf0d"><code>Failed changes &divide; Total changes deployed</code></p> |
| <p local-id="948493f0-6544-41d2-90c2-f51d713c5fb5">It primarily shows the health and efficiency of our Continuous Integration/Continuous Deployment (CI/CD) pipeline.</p>                                                                                                                                                                                    | <p local-id="fa40f810-b013-4163-88f9-fc67b553572c">It reflects the overall stability and reliability of our software and the effectiveness of our development and testing practices.&nbsp;<br />Understand the impact of our work on our users.</p>                                                                                                                                                                                                                                                        |
| <p local-id="3d6f4c5c-99ef-45dc-8fb1-b03a9579fdcf">Typical Goal:</p><p local-id="3d052651-2096-44c5-828b-aae5a6c7827c">Low failure in automation/pipelines (near 0%)</p>                                                                                                                                                                                     | <p local-id="e3df66b7-4387-47ab-96fb-5fe0f24d78a3">Typical Goal:</p><p local-id="4e0d86a1-e814-4040-9806-7c5b1899cae1">DORA benchmark: Elite teams keep CFR between 0&ndash;15%</p>                                                                                                                                                                                                                                                                                                                        |

### **How?**

To measure the CFR, we will consider these types of Event sources:

- **Change Events**:

  - **Asset changes** \- every asset version deployed or rolled back in a ring following the standard ODC delivery lifecycle.

  - **RFC changes** \- a manual change performed in a ring and associated with an asset, registered in the [RFC project](https://outsystemsrd.atlassian.net/jira/software/c/projects/RFC/boards/2191).



    What is considered a _**Change**_?

    - RFC in “Completed” status

    - Change Category != “Fast Track” \| “Rollback” \| “Promote to Standard”

    - Rings = "ring-osall" \| "ring-ea" \| "ring-ga"

    - Change Event will have the timestamp of the “Implementation Date”

- **Failure Events**:

  - **Incidents** \- an incident that may happen after a change is performed, which is registered in the [RDINC project](https://outsystemsrd.atlassian.net/jira/software/c/projects/RDINC/boards/2269).



    What is considered a _**Failure**_:

    - RDINC in _Solved_ status

    - Incident Type= “Customer Reported” \| “System-wide” \| “Internal”

    - Root Cause Categorization != Customer issue

    - Rings = "ring-osall" \| "ring-ea" \| "ring-ga"

    - Failure Event will have the timestamp of the RDINC creation

The calculation of the CFR is done by the following formula:

( `Number of failed changes` / `Total number of changes` ) x 100

- **Tools and Systems Used**:

  _Jira Change Management Events (RFC project), Jira Incident Response Events (RDINC Project)._
