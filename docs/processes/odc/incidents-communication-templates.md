---
title: Incidents Communication Templates
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/3509553166/Incidents+Communication+Templates
confluence_space: RKB
confluence_page_id: 3509553166
last_synced: 2026-04-09
owner: Process Engineering
---

# Incidents Communication Templates

**Version Control - **Current Version - 1.0 / Release Date -  

Next Release Planned -To be Defined

Please read the [**Process Release Notes**](#) page to check what will change. 

**Table of Contents**

This page presented several template messages you can use to communicate with **Global Support**,  with other **R&amp;D Teams**, with **Security Operations Office (SOC)**, and with the **customer**,

# **Communication Guidelines and Etiquette **
On Incident Response, communication is key - following &ldquo;The Small Book of The Few Big Rules&rdquo;, please check the communication guidelines below to ensure you ***Communicate to be Understood***.

- 
**Bridge the gap** between Global Support** **or other stakeholders'** **knowledge and R&amp;D on a given topic

- 
Provide additional **troubleshooting **steps

- 
Provide **Solutions**

- 
Ensure the **next person on call** on the team **can continue **the investigation without having to ask for more context or read all the previous communications.

# How to communicate with Global Support?
You should use the **following template** in your communications with Global Support on an Incident.

**READ ME** 

Highlight in your response **information that must not be shared with the customer** and is only for Global Support to know.
### Communication to Global Support Template
**Context**

A brief explanation of the feature in question, and the steps you did to troubleshoot.

Additional information, e.g. a reply from a third-party software provider.

**Previous Troubleshooting Plan Results**

Not for the first reply, after getting information from support, report back what you could understand with it.

**Next Troubleshooting Plan**

What information do you need to be collected, and what steps do you need to be done.

Together with a description of what you want to understand.

**Workaround or Solution Proposed**

Description of the solution you found.

 **THIS INFORMATION MUST NOT BE SHARED WITH THE CUSTOMER **

**Only for Global Support Consumption**

Below this line, you can share information that should only be used by Global Support as knowledge to improve the initial troubleshooting on their side, before the handover, and should NOT be shared with the customers. 

# How to communicate within R&amp;D?
Communication between R&amp;D Teams is also very important and must be effective and clear.

- 
To avoid **communication breakdowns** as the leading cause of errors and time-wasting

- 
To **smooth the transition** between R&amp;D Software Engineers

- 
To** improve knowledge management** about Incident Response

- 
To ensure** information is not lost** and is easy to find when needed

**What information can be included?**

- 
A list of **relevant ongoing activities** for that particular incident

- 
**Troubleshooting steps** performed so far

- 
A list of what you believe the **next steps** would be to resolve the incident

- 
Other **important notes** you believe will help the next engineer in rotation (slack messages, e-mails, stakeholders involved)

**How often should be updated?**

Every time you have **valuable information** to add to the resolution of the Incident.

Keep in mind ***why we are doing this*****?** - to ensure the next R&amp;D Software Engineer on call will be updated on your work without losing time and context.

When leaving for the **Vacation** period

When your on-call period **is completed**

When working on an Incident **continuously** every **2 days**

To do so, you must use **Jira Comments** and **tag the team members that will ensure the next on-call period **and other relevant stakeholders (if needed).

You can use the following template. 

### Communication to R&amp;D Teams Template
**Steps to reproduce the problem**

You should include all steps you did to try to reproduce and understand the problem

**Next steps**

You should include the information we asked the customer and why we asked for that information

You can include also what you believe the next steps would be

**Dead ends**

You should describe here tests that you did to reproduce the problem without succeeding

You can add tests that you did to identify the root cause without succeed

**(Potential) Incident cause**

You should describe which is the cause of the problem

**Workaround/Solution proposed**

You should include the Workaround or Solution we suggested to the customer and why we proposed it

**Other Important Notes**

You should include important notes as slack conversations, important e-mail notes or other stakeholders involved

 You can also highlight in this communication what** could or not be shared with customers**.

### Communication templates for Internal Incidents
This template is to be used once an R&amp;D team detects an incident before being reported by a Customer or alarms. This will help other groups like Global Support or Customer Care to be ready to answer to any incident being reported in the meantime and to manage customer expectations if needed. 

Please mark incidents manually created with `customer-impacted` using the *Labels* field on Jira.

For more information about Labels used on Incidents, please check this page.

**Internal incident**
This incident was reported by an internal R&amp;D Team* **(TEAM HERE) ***and the goal of reporting it as an incident is to give visibility to Support Team that the issue is happening in positive rings* **(IDENTIFY RINGS AFFECTED HERE)*****.**
This way we can accelerate it's troubleshoot and react faster in case a customer reports something similar or even avoid it reaching certain positive rings such as GA.

**Team to assign the incident (in case of need for fast track by Global Support)**

Please assign this incident to team ***(TEAM HERE)***.

**Context &amp; Business Impact**
Give some context of the situation and focus on the impact, how it affects your team or other teams, what is the impact on your productivity, would this be a problem that will impact our customers or the product overall in GA.

**Description**
Describe the issue and what is really happening in the code, emphasize with attachments to showcase the issue like images, links, logs, or other necessary resources to facilitate the replication of the issue
*(If/when applicable, describe the expected outcome vs the obtained outcome)*.

**Apps Information**
*(Affected applications - name, key, and revision)*

**Is there a Workaround?**
Whenever there is a workaround, ensure the relevant information or link to respective documentation is included here.

**Additional Information**
If troubleshoot was done:

* What troubleshoot was already done?

* Which teams should the incident be assinged to?

**Otherwise:**

Add info that no troubleshoot or additional information exists and this should follow the &quot;regular&quot; support process

# How to communicate with Security Operations Center (SOC)?
If you **suspect** that the symptoms are related to a **Security Incident**, then the Security Operations Center Team (SOC) must be summoned immediately for validation. 

You should use the following template.
### Communication to Security Operations Center (SOC) template
**Why might this situation be a Security Incident?**

&lt;Explain why this affects Confidentiality, Integrity, Availability, Authenticity or any other security principle.&gt;

&nbsp;

**What is the Service(s) impacted (or potentially impacted)?**

&nbsp;

**When was the incident detected? By whom?&nbsp;**

Detected on &lt;yyyy-mm-dd hh:mm:ss&gt; by [user@outsystems.com](mailto:user@outsystems.com)

&nbsp;

**&nbsp;Would it be likely to happen again? How often? Other customers?**

**&nbsp;Were there any measures already taken to workaround or mitigate this issue?**

**&nbsp;Were Personal or Business Data impacted or breached (or potentially impacted)?**

&lt;Not Likely, Possibly, Likely, Very Likely &gt;

&nbsp;

**Next Steps**

&lt;Describe what you're doing on the support ticket or if the ticket is stalled.&gt;

# How to communicate with Customers?
**PROCEED WITH CAUTION**

This should only be used when in need and** must be aligned with other stakeholders managing the incidents.**

Bear in mind that these communications will remain **public** on Support Portal - you are replying to customers on behalf of OutSystems. Be careful **to not display sensitive information **to our customers about our product.

**More Information required from the Customer**

**How to use -** If the R&amp;D Support Agent needs more information to proceed with the investigation.

Hello ***&lt;Customer name here&gt;**,*

We have received your feature request, and will carefully evaluate it for inclusion in a future version of the product. The Product team is constantly looking for ways to improve, so we very much appreciate receiving feedback like yours!&nbsp;

As we believe this reply*** ***answers your question, we will tentatively mark the present ticket as solved. 

Kind regards,

The ODC Team

**Customer Feature Requests**

**How to use -** If a customer asks for something that you know will be/could be included in future versions of ODC

Hello ***&lt;Customer name here&gt;**,*

We have received your feature request, and will carefully evaluate it for inclusion in a future version of the product. The Product team is constantly looking for ways to improve, so we very much appreciate receiving feedback like yours!&nbsp;

As we believe this reply*** ***answers your question, we will tentatively mark the present ticket as solved. 

Kind regards,

The ODC Team

**Features not part of Customer-Developers Journeys**

**How to use -** If a customer report something related with a feature that is not yet implemented on the product

Hello ***&lt;Customer name here&gt;**,*

We have received your support case and we concluded that this feature is not included yet on the Customer-Developers Journeys shared previously by ODC Team.

We appreciate the time you are investing on ODC and we will let you know as soon as this feature is implemented. 

As we believe this reply*** ***answers your question, we will tentatively mark the present ticket as solved. 

Kind regards,

The ODC Team

**Workaround to share with the customer**

**How to use -** When the workaround is to be shared with the customer

Hello ***&lt;Customer name here&gt;***,

We've analyzed the issue you reported and reached the following conclusions:

&nbsp;***&lt;Insert conclusion 1 here&gt;***

&nbsp;***&lt;Insert conclusion N here&gt;***

As a workaround, we propose you ***&lt;Insert workaround here&gt; - be as detailed as possible to ensure the customer is able to implement and test the workaround proposed.***

We hope the instructions above help you reach your solution. We remain at your side to help with any additional questions and would like to know about the success of the workaround provided.

Kind regards,

The ODC Team

**Bug Acknowledgement **

**How to use -** When we want to inform the customer we found the root cause of the problem and what are the follow up actions on our end.

Hello*** &lt;Customer name here&gt;***,

Thank you for your patience while we investigated this issue.

After analyzing the problem, we found that the root cause seems to be a platform bug, which leads to 

***&lt;introduce explanation here&gt;***. As a follow up action, we created a bug to solve the reported issue and we expect to fix it in future versions. 

As we believe this reply*** &lt;CHOOSE ONE - will resolve the presented issue/answers your question&gt;***, we will tentatively mark the present ticket as solved.

Nonetheless,*** &lt;CHOOSE ONE - should this issue persist/should you need additional clarification&gt;,*** you will still be able to reopen the ticket just by replying to this message.

Kind regards,

The ODC Team

**Support Case closing message**

**How to use -** When the customer issue is already unblocked and you are ready to close the Support Case.

Hello*** &lt;Customer name here&gt;***,

As we believe this reply*** &lt;CHOOSE ONE - will resolve the presented issue/answers your question&gt;***, we will tentatively mark the present ticket as solved.

Nonetheless,*** &lt;CHOOSE ONE - should this issue persist/should you need additional clarification&gt;,*** you will still be able to reopen the ticket just by replying to this message.

Kind regards,

The ODC Team

# How to communicate with Product Leadership?

For incidents with system-wide impact, regular communications should be sent to Product Leadership via the Internal Status Page.

The following templates are available for use in these communications, depending on the incident&rsquo;s current status.

- 
**Investigating status**

Investigating status Template#FFFAE6
We are investigating related incidents impacting the following:
&lt;p&gt;
Impacted SLO(s): [List specific SLO names - e.g., API Availability (99.9%)]
&lt;br&gt;
Impacted Service(s): [List specific service names - e.g., User Authentication Service, Order Processing API]
&lt;br&gt;
Severity: [Specify the current severity level - e.g., Sev1, Sev2]
&lt;p&gt;
We are actively working to understand the root cause and will provide further updates as they become available.

- 
**Identified Root Cause**

Identified Root Cause Template#FFFAE6
We have identified the root cause of the related incidents impacting the following:

&lt;p&gt;

Impacted SLO(s): [List specific SLO names - e.g., API Availability (99.9%)]

&lt;br&gt;

Impacted Service(s): [List specific service names - e.g., User Authentication Service, Order Processing API]

&lt;br&gt;

Severity: [Specify the current severity level - e.g., Sev1, Sev2]

&lt;p&gt;

Root Cause: [Brief, non-technical description of the identified root cause - e.g., An issue with a recent database migration, Increased load on a specific component, A misconfiguration in the network layer]

&lt;p&gt;

Our engineering teams are now focused on implementing the fix. We will provide further updates on the resolution progress.

- 
**Monitoring status**

Monitoring status Template#FFFAE6
The fix for the related incidents impacting the following has been implemented:
&lt;p&gt;
Impacted SLO(s): [List specific SLO names - e.g., API Availability (99.9%)]
&lt;br&gt;
Impacted Service(s): [List specific service names - e.g., User Authentication Service, Order Processing API]
&lt;br&gt;
Severity: [Specify the current severity level - e.g., Sev1, Sev2]
&lt;p&gt;
Root Cause: [Brief, non-technical description of the identified root cause - e.g., An issue with a recent database migration, Increased load on a specific component, A misconfiguration in the network layer]
&lt;p&gt;
We are now closely monitoring the system to ensure stability and that the fix has fully resolved the issue. We will provide a final update once we are confident the incident has been fully resolved.

- 
**Resolved**

Resolved Template#FFFAE6
The related incidents impacting the following have now been fully resolved:
&lt;p&gt;
Impacted SLO(s): [List specific SLO names - e.g., API Availability (99.9%)]
&lt;br&gt;
Impacted Service(s): [List specific service names - e.g., User Authentication Service, Order Processing API]
&lt;br&gt;
Severity: [Specify the current severity level - e.g., Sev1, Sev2]
&lt;p&gt;
Root Cause: [Brief, non-technical description of the identified root cause - e.g., An issue with a recent database migration, Increased load on a specific component, A misconfiguration in the network layer]
&lt;p&gt;
Monitoring systems indicate that stability has been restored. We will continue to monitor performance to ensure no further issues arise. Thank you for your patience.