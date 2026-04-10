---
title: How to deal with Security Vulnerabilities
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/5036639693/How+to+deal+with+Security+Vulnerabilities
confluence_space: RKB
confluence_page_id: 5036639693
last_synced: 2026-04-09
owner: Process Engineering
---

# How to deal with Security Vulnerabilities

none

[ODC Problem Records (ODC RPMs)](https://outsystemsrd.atlassian.net/jira/software/c/projects/RPM/boards/2251) will be used to **track the progress** of any action needed to fix the **Security Vulnerability **identified, and [Vulnerability Records (VULs)](https://outsystemsrd.atlassian.net/jira/software/c/projects/VUL/boards/1449) will be used to **track and manage exploitation risks**. 

Read [https://outsystemsrd.atlassian.net/wiki/x/WYC9BgE](https://outsystemsrd.atlassian.net/wiki/x/WYC9BgE) for more context on this need.

At this moment, ODC Problem Management will handle:

- 
[Customer Reported Vulnerabilities](https://outsystemsrd.atlassian.net/wiki/spaces/EEO/pages/4408049753/Streamline+Vulnerability+Management+in+ODC#Use-Case-A---Customer-Reported-Vulnerabilities)

- 
[Self-Reported Vulnerabilities](https://outsystemsrd.atlassian.net/wiki/spaces/EEO/pages/4408049753/Streamline+Vulnerability+Management+in+ODC#Use-Case-B---Self-Reported-Vulnerabilities)

# What is a Security Vulnerability?
Expand to read more about Security Vulnerabilites
Security Vulnerabilitiestrue
# Who can report a Security Vulnerability?
https://outsystemsrd.atlassian.net/wiki/spaces/EEO/pages/4519526443/ODC+Problem+Records+ORPMs+creation#When-and-by-whom-can-a-Problem-Record-be-created%3F  

# Process Flow for Vulnerability Management## 1. Vulnerability Identification
Regardless of its category (Customer Reported or Self-Reported vulnerabilities), the vulnerability must be acknowledged and tracked after being **identified** to guarantee we protect our customers and OutSystems from someone exploiting that vulnerability. 
###   Vulnerability detected by R&amp;D
R&amp;D may find vulnerabilities to fix during daily activities such as developing, analyzing or testing.

**In ODC, R&amp;D teams register and report a Vulnerability to be fixed by:**

- 
Creating a new issue in [**RPM Jira Project**](https://outsystemsrd.atlassian.net/jira/software/c/projects/RPM/boards/2251)** (issue type = &ldquo;ODC Problem&rdquo;) **

- 
Marking it as a Security Vulnerability (field **&quot;*****Is it a Security Vulnerability?*****&quot; = &quot;Yes&quot;**)

- 
If the team responsible for the vulnerability is known, fill it in the **&ldquo;Teams&rdquo;** field. If not, select the **PSIRT **team in that field.

(Note that when creating a Security Vulnerability, the *&ldquo;Impact&rdquo;* field will always be set to &ldquo;High&rdquo;.)

This way, PSIRT (Product Security Incident Response Team) will have the proper visibility to:

- 
Validate whether it is a vulnerability or not;

- 
Classify the severity of that vulnerability if the previous is true.

In case R&amp;D detects a possible security vulnerability under the **Incident Response** Postmortem&rsquo;s scope, the respective ODC RPM should be created, marked as a vulnerability, and linked with the ODC Incident (RDINC Jira ticket).

As per the&nbsp;Vulnerability Management Procedure*&nbsp;*for issues reported by R&amp;D, **R&amp;D is free to prioritize and fix the issue based on the ****Vulnerability Prioritization and Fixing**** for ODC**. However, the PSIRT risk analysis might impact the required priority for the issue.&nbsp;

On the other hand, if you are unsure of the priority you should give to the issue, request help from anyone from PSIRT.&nbsp;
###   Vulnerability detected by Customer
When a **potential Security Vulnerability **is detected by Customers/Partners via Incident, the Support Agent in charge of that issue should **open an ODC Problem Record via Zendesk**, **mark it as a Security Vulnerability** (field *&ldquo;Is it a Security Vulnerability?&rdquo;* = &ldquo;Yes&rdquo;) **and assign it to PSIRT** (field *&ldquo;Teams&rdquo; = &ldquo;PSIRT&rdquo;*), so the vulnerability can be analyzed by that team.

(Note that when creating a Security Vulnerability, the *&ldquo;Impact&rdquo;* field will always be set to &ldquo;High&rdquo;.)

In case the Problem originates from an **Incident**, both issues (ODC RPM and RDINC Jira tickets) should be linked.

While PSIRT analyzes the problem, the Incident ticket must be kept open. After the Security Vulnerability is confirmed, PSIRT must assign it to the corresponding R&amp;D team (**updating *****Teams *****field**). [PACA for ODC](https://engineering.outsystems.net/paca/ProductAreasListTree.aspx) can be used to obtain this information. 

In this case, all the communication between Global Support and R&amp;D, through the ODC RPM, must be done using the &ldquo;Zendesk Support&rdquo; area for Comments in the Jira issue. This way, the Support Agent will be notified when a comment is added in the Problem Record.
###   Vulnerability detected by Security Team
When a **new Security Vulnerability **is identified, the Security Team should **create a new ODC Problem Record and mark it as a Security Vulnerability** (*'field Is it a Security Vulnerability?'* = &ldquo;Yes&rdquo;), for traceability purposes.

(Note that when creating a Security Vulnerability, the *&ldquo;Impact&rdquo;* field will always be set to &ldquo;High&rdquo;.)

When possible, PSIRT team should assign the new ODC RPM issue to the corresponding team (**update *****Teams *****field**). [PACA for ODC](https://engineering.outsystems.net/paca/ProductAreasListTree.aspx) can be used to obtain this information. 
###   Automatic creation of the issue in the *VUL ODC* project
**Automation In Place**
Regardless of the vulnerability source, when:

- 
the ODC Problem Record is marked as a vulnerability (*'Is it a Security Vulnerability?'* = &ldquo;Yes&rdquo;)
AND

- 
has no VUL linked issues yet,

**a Jira issue type VUL will be automatically created at **[Vulnerability Management Project](https://outsystemsrd.atlassian.net/jira/software/c/projects/VUL/boards/1449) **and linked with the ODC RPM issue**.

This way PSIRT has instant visibility over it in the board acting as the central source of vulnerabilities and reports, and for tracking progress on both the security and development sides.
### **How does the PSIRT get notified about a new Reported Security Vulnerability?**
When a Problem Record is created and marked as a Security Vulnerability, a new Vulnerability Issue is automatically created and visible on the PSIRT [https://outsystemsrd.atlassian.net/jira/software/c/projects/VUL/boards/1449](https://outsystemsrd.atlassian.net/jira/software/c/projects/VUL/boards/1449).

This will give PSIRT visibility to validate whether or not it is a vulnerability, and classify it.

The **Problem Record project** will act as a central source of vulnerabilities and reports, and track progress on both the security and development sides.
## 2. Vulnerability ClassificationStage 2
true

 If the Vulnerability ***Criticality ***turns out to be **High or Critical**, PSIRT will change the Problem Record ***Priority ***to **Urgent**.

 See the Full Vulnerability Classification process description.
## 3. Vulnerability Remediation (Risk Assessment + Plan &amp; Fix)Stages 3 &amp; 4
 See the Full Vulnerability Remediation process description.
## 4. Vulnerability Release (Fix Release + Publish Security Bulletin)Stage 5
  See the Full Vulnerability Release process description.