---
title: Retrospective-SEV2-Suspected incorrect count of AOs
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4326064207/Retrospective-SEV2-Suspected+incorrect+count+of+AOs
confluence_space: RKB
confluence_page_id: 4326064207
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV2-Suspected incorrect count of AOs

## 📘 Overview
Author:&nbsp;Rootlytrue

Severity:&nbsp;SEV2Redtrue

Teams:&nbsp;Neo Platform TheseusBluetrue
#### 🕐 Timestamps
Started At:&nbsp;JuNE 20th 05:17 AM WESTBlue

Mitigated At:&nbsp;July 23th 11:32 AM WESTYellow

Resolved At:&nbsp;July 26th 08:38 AM WESTGreen
#### 🔗 Links
[Incident Page on Rootly](https://rootly.com/account/incidents/591-suspected-incorrect-count-of-aos-26fc94f6-9746-4d67-9720-06a9644085d4)

[Incident on Jira](https://outsystemsrd.atlassian.net/browse/RDINC-25522)

[Slack channel](https://slack.com/app_redirect?channel=C0790QZ68H2&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3024976)

#### 🧑&zwj;🚒 Stakeholders
Participants

     

Reviewers

  

Approval Date

TBD
## Executive Summary
**Issue Overview:**  
On June 20th, 2024, at 8:30 AM (UTC), Lingnan University submitted Support ticket [#3024976](https://supportoutsystems.zendesk.com/agent/tickets/3024976) (Zendesk) and [RDINC-25522](https://outsystemsrd.atlassian.net/browse/RDINC-25522) (Jira), reporting a sudden drop in their AO (Application Objects) total count from 146 out of 150 to 106&mdash;a decrease of 40 AOs. Investigations revealed that a bug was introduced in the calculation method after a new feature to display detailed AO counts per asset was released on June 14th, 2024. This bug failed to account for Entities from External Connections used by the customer's applications and libraries.

**Customer Impact:**  
While this issue did not affect the customer&rsquo;s development experience, it did impact their purchasing decisions. Lingnan University was in the process of acquiring additional AO packages, which they paused due to the discrepancy in their AO count.

**Root Cause Analysis:**  
The problem originated from the new Detailed View of AOs feature, which introduced a different calculation method per asset. This new method did not align with the existing total count calculation, resulting in two different methods being used simultaneously. Upon internal review by the Theseus team, the discrepancy between the two methods was identified. It was decided to adopt the detailed view per asset as the standard method. However, after the customer raised concerns, it was discovered that the new method did not include Entities from External Connections, leading to the reduced count observed by the customer.

**Corrective Actions:**  
In response to the incident, it was decided to reinstate the count of Entities from External Connections in the final AO total. However, during discussions with the Product Management (PM) team, it was realized that the original method definition was also flawed ([as implemented a while ago](https://outsystemsrd.atlassian.net/browse/RDPSTT-989)). The initial method definition counted all individual references to External Entities, even if the same entity was referenced by multiple assets, instead of only once, regardless of how many times an asset referenced them. 

The agreed-upon rule now is to count all Entities from an External Connection only once, even if referenced by multiple applications or libraries.

Given that the original method definition didn&rsquo;t represent the count as intended, it was decided to proactively communicate the upcoming changes to all affected customers with External Connections configured in production. An internal analysis identified 23 affected customers. A report with the updated AO counts was sent to the Field team to inform these customers of the impending change. The new calculation method was officially released in General Availability (GA) on July 26th, 2024.
## 📝 Retrospective### Details
**Ring:** ga
**System-wide impact:**&nbsp; Yes
**Tenant ID:** ec0d5d97-275d-429b-866f-d873ace203d3
**Tenant Prefix:** lingnan
**Routing Error Code:** N/A
**Product Area:** Phoenix::Phoenix Portal::Subscription
### **Impact:**
The AOs counting was incorrect from the user's perspective. They were putting sales of more AOs packages on hold.

**Investigation and Findings:**

It was discovered that External Entities weren't being counted.

In some cases, these Entities may have been double-counted.

The calculation logic has been changed to ensure that External Entities are no longer counted on app/lib consumers but instead counted from all External Connections where any entity is referenced.

**Resolution:**

The entire counting system was rebuilt, incorporating a new definition of how to count External Entities in agreement with PMs.

Communication was sent about the changes to the customer and public documentation was updated in the portal.
## Tasks performed during incident resolution

**Summary:** Analyse to understand why the AOs count dropped RDPSTT-1947ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 
**Assignee:**  
**Due Date:** 2024-jun-27
**Status:**doneGreentrue

**Summary:** Hotfix to correct the calculation method RDPSTT-1917ef8955cb-cb21-32a7-b692-01ace42388d6System Jira  
**Assignee:**  
**Due Date:** 2024-jun-20
**Status:**doneGreentrue

**Summary:** Data analysis to identify the customers impacted if the new calculation method
**Assignee:**  
**Due Date:** 2024-jul-4
**Status:**doneGreentrue

## Root Causes 

- 
**Why was there an initial mismatch?**
The initial mismatch existed because the total count took into consideration the External Entities for the count whereas the Detailed AOs view per asset did not consider them.

- 
**Why did we change the Total count so it would be equal to the sum of the assets' AOs in the detailed view?**
We did this because after validating in the negative rings, they were always matching, thus we were led to believe that the sum of the AOs counts in the detailed view would match the total count. This assumption was wrong because the external entities were overlooked.

- 
**Why was there no follow-up to understand why there was a difference between the sum of the report and the AO total?**
There was no follow-up because the detailed view per asset had the correct AOs count. We assumed the original total count was incorrect because it had no other value to compare against. In this case, since we had the total AO count with a specific value and the sum per asset with another value, we assumed the sum was correct since it had been confirmed that the detailed view per asset was correct. (Guilherme Rolo confirmed with Pedro Louro and Margarida Figueiro (POs), that the Detailed view count was correct).

- 
**Why did we assume the original total count was wrong?**
We weren&rsquo;t fully aware of the impact this change could have, it hadn&rsquo;t been properly documented, the tests that were done didn&rsquo;t consider a scenario where apps/libs had External Entities, and this should have been escalated to PMs beforehand to be confirmed, before being changed since it is pricing-related.

- 
**Why wasn&rsquo;t the counting rule properly tested with unit and/or component tests? **

- 
It had some tests, that validated the original counting rule agreement, and it had curated data that didn&rsquo;t expose this issue after the change.

- 
**Why wasn&rsquo;t the calculation rule properly documented?**

- 
It had been documented in an HLD when it was originally done, but cumulative changes were added as new features, without a proper definition, only being tracked in Jiras.

## Improvement opportunities
- 
Given the significance of AOs in pricing, it's crucial to have comprehensive documentation that covers all possible use cases, nuances, and details. During the incident analysis, it became evident that while many people had partial knowledge of AOs, no one had a complete understanding. This lack of comprehensive knowledge from Product Mangement (PMs) hindered both debugging efforts and the development of a proper fix. 

- 
Whenever the counting rule needs to be changed, there should be a common agreement among product managers to ensure we don't end up in a situation with differing opinions.

- 
We should track all the changes requested and implemented in the calculation rule.

- 
Additionally, the concept of External Entities should be abstracted within the Entitlement Job, as they are treated as AOs. Although External Entities were initially stored in a different table due to their distinct source (referenced element vs. application object), the service itself should not be aware of these differences. By consolidating all AOs in a single table, future changes or additions would automatically be included without requiring code modifications, thereby reducing the risk of overlooking them in the count.

## 📝 Follow Up Items
**Summary**

**Priority**

**Status**

**Assignee**

**Links**

Consolidating tables

MediumYellowtrue

DoneGreen

Theseus Team

Done during the migration from Postgres to DynamoDB

Update internal documentation

 

MediumYellowtrue

DoneGreen

 

[https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/3610378975/Entitlement+Job#AOs-calculation](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/3610378975/Entitlement+Job#AOs-calculation)

Update [Public documentation](https://success.outsystems.com/support/licensing/application_objects/)

MediumYellowtrue

In ProgressYellowtrue

 

[PR](https://github.com/OutSystems/docs-support-internal/pull/696/files) 

Create a Tracking page to document changes in the counting rules

LowBlue

DoneGreen

 

AO's Decision Page 
## ⌛ Timeline
[View on Rootly](https://rootly.com/account/incidents/591-suspected-incorrect-count-of-aos-26fc94f6-9746-4d67-9720-06a9644085d4)

**Date**

**User**

**Event**

June 20  5:17 AM WEST

Customer

Support case [#3024976](https://supportoutsystems.zendesk.com/agent/tickets/3024976) was submitted arguing about AOs discrepancy from 146 to 106

June 20  5:39 AM WEST

Global Support (GS)

Global Support started investigating the case with the info provided by the customer

June 20  5:39 AM WEST

Global Support (GS)

Global Support responded to the customer confirming that the current amount of 106 AOs was correct and asked for evidences that the amount should be 146

June 20  6:08 AM WEST

Customer Success Manager (CSM)

Sylvia Lee, CSM provided more details about the criticality of the problem, stating that it was causing major roadblock in expansion of more AO packages &amp; renewal license with OutSystems

June 20  6:08 AM WEST

Global Support (GS)

Global Support after some analysis using Compass noticed that the decrease in the amount of AOs started in Jun 14th

June 20  8:28 AM WEST

Global Support (GS)

Global Support replied to the customer saying that evidences confirmed the decrease on the number of AOs, and that further internal analysis would be initiated

June 20  8:28 AM WEST

Global Support (GS)

Global Support scalated the incident to R&amp;D

June 20  10:36 AM WEST

R&amp;D Theseus team

Asked to Global Support why this incident was considered as a SEV2 since other similar incidents were SEV4

June 20  10:36 AM WEST

Global Support (GS)

Global Support replied explaining the urgency on the customers retention &amp; renew

June 20  19:44 PM WEST

R&amp;D Theseus team

Confirmed that on Jun 14th there was a new release in GA which introduced a bug in the calculation method that was not considering the External Entities referenced by the customer apps/libs, hence the drop in their AOs count

June 20  19:44 PM WEST

Global Support (GS)

Global Support replied to the customer explaining the issue and that a fix was on the way

June 20  22:15 PM WEST

 (Chief of Staff)

An internal communication was sent to the SMTs and CPTO explaining the problem, a list of impacted customers and a timeline to get a corrective release in GA

June 24  18:07 PM WEST

 (PO)

Started a slack channel with relevant people + PMs to confirm how the External Entities should be counted to be included in the hotfix

June 25  19:13 PM WEST

[Slack channel](https://outsystems.slack.com/archives/C079HE875T5/p1719339199001679?thread_ts=1719328227.613279&amp;cid=C079HE875T5)

After some consideration, this group of people got a final decision on how to calculate the External Entities

June 26  11:18 AM WEST

[Slack Channel](https://outsystems.slack.com/archives/C079HE875T5/p1719397126954539?thread_ts=1719328227.613279&amp;cid=C079HE875T5)

After some consideration, this group of people made the final decision to release the fix with a feature toggle off until the Field Team communicates with affected customers.

June 26  22:50 PM WEST

 (GS)

Updated the incident with the most recent plan to manage the GS Agents expectations

June 28  09:32 AM WEST

 

Update the slack group saying that a communication was sent to Carlos Alves and Andy Pemberton (Field leaders), who suggested a deep analysis about the impact of the fix on the 23 customers

July 2  10:06 AM WEST

 

A deep analysis was started based on metrics to identify the impact on each customer once the fix is turned ON in GA

July 4  11:37 AM WEST

 

The result of the analysis was shared with  with the details of the impact on each customer

July 10  10:28 AM WEST

 

[Confirmed](https://outsystems.slack.com/archives/C079HE875T5/p1720603721291369) that the report with the impact on customers was shared with the Field team

July 18  10:28 AM WEST

 

The date (July 25th) to turn the fix ON in GA was settle

July 23  11:31 AM WEST

Global Support (GS)

The customer was updated that the AOs count should appears correct to them on the Friday of July 26th

July 23  11:32 AM WEST

Global Support (GS)

The Global Support team marked this incident as Solved in ZenDesk.

July 25  11:50 AM WEST

R&amp;D Theseus team

Confirmed the Fix was enabled in GA.

July 26  08:38 AM WEST

R&amp;D Theseus team

Confirmed that the Job calculated the AOs successfuly