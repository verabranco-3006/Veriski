---
title: Cost Anomaly Management Process
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/5423302839/Cost+Anomaly+Management+Process
confluence_space: RKB
confluence_page_id: 5423302839
last_synced: 2026-04-09
owner: Process Engineering
---

# Cost Anomaly Management Process

none## Problem Statement
FinOps team currently performs a **recurring manual task**: analyzing emails they regularly receive about anomalies detected in our AWS services. When a relevant anomaly is identified, the team documents it in a Confluence page** **for further investigation and resolution. Often, these anomalies are **redirected to an external team** better suited to analyze and address the issue. In such cases, FinOps team waits for the external team&rsquo;s analysis and resolution, which **frequently requires them to send reminders and request status updates**.

### Impact
This manual process results in significant challenges, particularly **high manual effort **and **limited visibility**. For instance, it's difficult to understand the **current status** of each anomaly documented in the Confluence table (it may be outdated). This also leads to a complete **absence of historical data**, making it difficult to analyze trends, identify recurring issues, or even understand the resolution timeframes. Furthermore, communication with external teams relies on **Slack messages that can easily get lost or overlooked**, leading to delays and additional follow-up.

## Solution Proposed
To address these challenges, we are implementing a **structured anomaly tracking system** within Jira by creating a **new, dedicated project**. This will ensure every registered anomaly has its own record, making the **information easily searchable**. All communication with other teams regarding these anomalies will now happen directly within the Jira issues, providing **complete transparency and an audit trail**. This setup also allows us to **extract valuable metrics** and **introduce automation capabilities**, streamlining the entire process.

High Level Process