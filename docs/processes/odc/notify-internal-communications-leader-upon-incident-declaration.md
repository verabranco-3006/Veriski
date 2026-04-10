---
title: Notify Internal Communications Leader upon Incident Declaration
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/5344100464/Notify+Internal+Communications+Leader+upon+Incident+Declaration
confluence_space: RKB
confluence_page_id: 5344100464
last_synced: 2026-04-09
owner: Process Engineering
---

# Notify Internal Communications Leader upon Incident Declaration

notify ICL
16falsenonelisttruenote
The **Internal Communication Leader** is responsible for managing and coordinating all internal communications during a system-wide incident. Their primary goal is to ensure clarity, consistency, and timely updates across internal stakeholders.

The **Internal Communication Leader** is responsible for managing and coordinating all internal communications during a system-wide incident. Their primary goal is to ensure clarity, consistency, and timely updates across internal stakeholders.

The assignment and notification of the ***Internal Communication Leader***, following the declaration of a system-wide incident, are the **responsibility of the ****Incident Commander**** (SRE Engineer)** and occur through the following workflow:

[[Lucid chart](https://lucid.app/lucidchart/1d1d7b4c-0070-4dfa-b094-f408ebc3b27d/edit?viewport_loc=-1038%2C-13%2C3380%2C1452%2CLfFM0kbr.AZT&amp;invitationId=inv_224533ce-c8a3-40c6-9240-f096393da555)]

### 1.   System-Wide Incident is declared
🧑&zwj;💼 **Action Owner:** Incident Commander (SRE Engineer)

An incident with system-wide impact has been officially declared, by the **Incident Commander (SRE Engineer)**, impacting multiple systems or services.

### 2.  Slack Notification asking to notify Internal Communications Leader
The **Incident Commander**, that was added to the Incident Slack channel, receives a message in that channel - **&ldquo;Incident Declared - Notify Internal Communications Leader (IC Leader)&rdquo;** - instructing them to page the appropriate Team:

This message is **pinned** in the Incident Slack channel for easy access via the &quot;Pins&quot; tab.

### 3.   Identifying the impacted Team
🧑&zwj;💼 **Action Owner:** Incident Commander (SRE Engineer)

The Incident Commander is responsible for **identifying the team affected by the incident**. To determine the correct team, the SRE team will consider information available in the incident details, such as the **team owning the Service Level Objective (SLO) or service** - usually the first team involved in incident response.

 **Clicking the **`'Team Details'` **button **opens a page listing all the Teams, Value Streams, their respective VS Leaders, and Engineering Managers.

It's important to note that the **initial assessment might change**. The incident investigation may reveal that the problem originated in a different service, requiring a different Internal Communications Leader to be assigned. In that case, SRE should[** notify a new Internal Communications Leader**](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/5344100464/Notify+Internal+Communications+Leader+upon+Incident+Declaration#7.-%F0%9F%94%81-New-Internal-Communications-Leader%3F).

Value Stream Leaders and Engineering Managers are responsible for keeping the list of VS Leaders and Engineering Managers up to date, as each team&rsquo;s Escalation Policy was initially created based on that list.
**Each Value Stream Leader is accountable for determining how to assign the Internal Communications Leader role within their teams.** They have the flexibility to assume the role themselves, delegate it, set up rotation schedules, or use any other method they consider appropriate.

### 4.   Notifying and assigning the Internal Communications Leader
🧑&zwj;💼 **Action Owner:** Incident Commander (SRE Engineer)

 **Clicking the **`'Page IC Leader'` **button** opens a pop-up window to **select the Team** affected by the incident. 

Note: *EP* stands for **Escalation Policy**. It defines how *Rootly *will notify the person configured in the Escalation Policy settings for that Team.

  Select the appropriate **Team** from the dropdown, and **click the **`'Update'` **button**.

The person designated as the IC Leader for their team at that time will be notified via ***Rootly on-call***, using their configured methods (App notification, call, email, SMS).
note
All individuals within the defined escalation policies for each Team should have ***Rootly on-call*** configured, in order to receive on-call notifications from Rootly. 

It is essential that the alert is **acknowledged**. If the person notified doesn&rsquo;t acknowledge the notification, their backup will be notified, according to the ***Escalation Policy*** defined.

All individuals within the defined escalation policies for each Team should have [***Rootly on-call*** configured](/wiki/spaces/RPE/pages/5289836672/VS+Leader+Guide+to+Rootly+Alerts+for+Internal+Status+Page#Purpose%3A-Ensure-you-receive-notifications-via-your-preferred-channels-and-formats.), in order to receive on-call notifications from Rootly. 

It is essential that the alert is **acknowledged**. If the person notified doesn&rsquo;t acknowledge the notification, their backup will be notified, according to the [***Escalation Policy*** defined](/wiki/spaces/RPE/pages/5289836672/VS+Leader+Guide+to+Rootly+Alerts+for+Internal+Status+Page#Purpose%3A-Schedules-must-be-associated-with-an-Escalation-Policy.).

Once the **alert is acknowledged**, that person will:

- 
 Be added to the **Incident Slack channel**

- 
 Be assigned the role *of **Internal Communications Leader***

Notification of the on-call person to assume IC Leader role for the Backend Runtime team
### 5.  Updating the Internal Status Page 
🧑&zwj;💼 **Action Owner:** Internal Communications Leader

The **Internal Communications Leader** updates the Internal Status Page with relevant incident information. See more information here: Updating the Internal Status Page.

### 6.  Internal Status Page Subscribers are notified
All subscribers to the Internal Status Page receive updates (via email, text message, &hellip;, depending on their preferences). See more information here: Updating the Internal Status Page.

 [Rootly - Internal Status Page](https://rootly.com/account/status-pages/internal-status-page/private)

### 7.  New Internal Communications Leader?
🧑&zwj;💼 **Action Owner:** Incident Commander (SRE Engineer)

If the** Internal Communications Leader needs to be changed later**, the SRE Engineer should repeat this process from [Step 4](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/5344100464/Notify+Internal+Communications+Leader+upon+Incident+Declaration#4.-%F0%9F%93%9F--Notifying-and-assigning-the-Internal-Communications-Leader), by clicking the **button **`'Page IC Leader'` **button **again.

### 8.  Checking who the Internal Communications Leader is
At any time, it is possible to check who the **Internal Communications Leader** for a given incident is through the following platforms:

- 
**Incident Slack Channel**

- 
The name will appear directly in the **first message**:

- 
or in the pop-window that appears when the `&lsquo;Assign Roles&rsquo;` **button is clicked**:

- 
**Rootly Incident page**

- 
When clicking the `&lsquo;Assigned Roles&rsquo;`** button:**

- 
**Jira*** (automation not implemented yet)*

- 
Under the ***Troubleshooting *****tab, &ldquo;Internal Communications Leader&rdquo; field**:

Type or paste something here to turn it into an excerpt.