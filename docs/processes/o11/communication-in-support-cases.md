---
title: Communication in Support Cases
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/731840559/Communication+in+Support+Cases
confluence_space: RCP
confluence_page_id: 731840559
last_synced: 2026-04-09
owner: Process Engineering
---

# Communication in Support Cases

Our communication serves the following purposes:

- 
**Bridge the gap** between **Support **knowledge and **your **own on a given topic

- 
Provide additional **troubleshooting **steps

- 
Provide **Solutions**

- 
Ensure the **next person on rotation** on your team,** can continue **your work without having to ask you for context or read previous communications.

###  Communication tips

**READ ME** 

Highlight in your response **information that must not be shared with the customer** and is only for Support to know.

On the top of each Support Case, you can find a disclaimer to remind you about this topic.

###  Communication to Global Support Template
You should use the **following template** in your communications with Support:

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

 **THIS SHOULD NOT BE SHARED WITH THE CUSTOMER **

**Only for Global Support Consumption**

Below this line, you can share information that should only be used by Global Support as knowledge to improve the initial troubleshooting on their side, before the handover, and should NOT be shared with the customers. 

# How to communicate with Global Support?
All communication regarding the incident (Support Case) should be made using the **Add Comment to all linked tickets** button on the **Zendesk Support** panel on the right side. 

By doing this, you **will reset the OLA** of the incident &rarr; read more about it [here](https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/726335741/Support+Cases+Priorities+and+OLAs#When-are-OLAs-active-and-how-to-reset-them%3F).

It is really important to use this tool to communicate with Global Support agents working on the case with the customer.&nbsp;

Otherwise, the **communication flow** between Global Support and R&amp;D will be broken and **information **might get lost on the way and compromising everyone&rsquo;s **efficiency** on resolving the incident to the customer  

Global Support is responsible to use Zendesk Jira Support Plugin as well to respond to all linked Jira issues.

The is **no autosave** in this box, so write your communications elsewhere, notepad++ or google docs before. Also, you can check [**here**](https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/731840559/Communication+in+Support+Cases#%E2%9C%8D--How-to-send-a-complex-messages%3F) how to send **complex communications** using this integration.

##  **WARNING**
When you are writing the comments on the issue you are working on, you **MUST NOT** use **&ldquo;Send as a Public Reply&rdquo;**. 

Messages written with this option checked **will be sent directly to our customers** and, by doing so, **we can compromise the confidentiality** of our product by revealing sensitive information.

The messages switched between both parties will be available as **Jira Comments**, as you can see in the picture below.

You can see all the communications changed between Global Support and R&amp;D, on **Comments** tab and **Zendesk Support **tab.

You will notice that on Zendesk, the communications with a yellow backgroundYellow are **internal **and, therefore** not visible for the customer**. 

###   How to send a complex messages?
Zendesk Support Plugin allows you to send simple text messages or messages formatted using [Markdown](https://www.markdownguide.org/).

If you want to send a complex message, where you can use indentation, bullets and other formatting rules, you can follow two paths:

- 
Use the** Jira Comments** tab, then **ask to Global Support **to check your comments using **Zendesk Support Plugin** - this causes the message to look good in Jira but not in Zendesk, and Global Support agents will need to copy the contents from Jira to Zendesk; 

- 
Use Markdown directly on the Zendesk tab - this will cause the message to look good on Zendesk and good enough on Jira, while avoiding that Global Support agents have to copy it.

This way, Support Case communication workflow between R&amp;D and Global Support will not be broken.

# How to communicate within R&amp;D?
Communication between R&amp;D Teams is also very important and must be effective and clear.

- 
To avoid **communication breakdowns** as the leading cause of errors and time-wasting

- 
To **smooth the transition** between R&amp;D Software Engineers

- 
To** improve knowledge management** about Incident Management on the R&amp;D Side

- 
To ensure** information is not lost** and is easy to find when needed

###  Shift Report - What information can be included?
- 
A list of **relevant ongoing activities** for that particular incident

- 
**Troubleshooting steps** performed so far

- 
A list of what you believe the **next steps** would be to resolve the incident

- 
Other **important notes** you believe will help the next engineer in rotation (slack messages, e-mails, stakeholders involved)

###  How often should be updated?
Every time you have **valuable information** to add to the resolution of the Incident.

Keep in mind ***why we are doing this*****?** - to ensure incoming R&amp;D Software Engineer will be updated on your work without losing time and context.

When leaving Support Rotation for the **Vacation** period

When your rotation shift **is completed**

When working on an Incident **continuously** every **2 days**

To do so, you must use **Jira Comments** and **tag the team members that will ensure the next support rotation period **and other relevant stakeholders (if needed).

You can use the following template. 
### **  **Shift Report Template 
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

Learn more about **Support Cases priorities** and **OLAs** here.