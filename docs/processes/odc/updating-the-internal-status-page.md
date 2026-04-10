---
title: Updating the Internal Status Page
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/5344100671/Updating+the+Internal+Status+Page
confluence_space: RKB
confluence_page_id: 5344100671
last_synced: 2026-04-09
owner: Process Engineering
---

# Updating the Internal Status Page

noneupdate internal status page - 1
Rootly&rsquo;s [**Internal Status Page**](https://docs.rootly.com/configuration/status-pages) feature will be used to **share internal communications about the status and progress of incident resolution**. This page will allow Product Leadership and Field Teams to follow real-time updates, key developments, and the closure of critical incidents in a centralized, internal-only location.
## Updating the Internal Status Page for the first time
When the message **&ldquo;Update Internal Status Page w/ System-Wide Incident&rdquo;** appears in the Incident Slack channel, the **Internal Communications Leader** (a representative from the Team most affected by the incident) can update the Incident's Internal Status Page to share relevant information with Product Leadership and Field Teams: 

This message is **pinned** in the Incident Slack channel for easy access via the &quot;Pins&quot; tab.

note
This should be done for the first time as soon as sufficient context about the impact and affected assets is gathered. 

Learn more about **when to update the Internal Status Page** during incident resolution here: [https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/5344100671/Updating+the+Internal+Status+Page#When%3F](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/5344100671/Updating+the+Internal+Status+Page#When%3F) 

This should be done for the first time as soon as sufficient context about the impact and affected assets is gathered. 

Learn more about **when to update the Internal Status Page** during incident resolution here: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/5344100671/Updating+the+Internal+Status+Page#When%3F 

Clicking the `'Update Internal Status Page'` **button **opens a pop-up window titled **&ldquo;Update Status Page&rdquo;**.

As this is the first message that will be shared in the Status Page, fill in the fields with the following data:

- 
**Status page* **: select *Internal System Status Page (Private)*

- 
**Status page template** [optional]: Here, you can:

- 
Select *[Template] Investigating Status - *This will add a [template](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/5344100671/Updating+the+Internal+Status+Page#Existing-Templates%5BhardBreak%5D) to the ***Message*** field. **Please do not forget to update the template by replacing the placeholder information with the actual details of the incident.**

- 
*Or, leave it empty *- In this case, **no template** will be added to the ***Message*** field.

- 
**Public Title* **: A title for the communication, that will appear in the *Internal status page*.

- 
**Status* **: The status of the Incident resolution. In this case, it should be *Investigating*.

- 
**Message**: The message to be shared in the Internal Status Page. If a template was selected before, it will appear here.

- 
**Notify subscribers **[optional]: It should be checked, as we want everyone that subscribes to *Internal status page* updates to be notified about this message.

***mandatory fields**

Once the `'Submit'`** button** is clicked, a message with the communication that was sent and a link to the Internal Status Page will appear in the Slack channel:

## Accessing the Internal Status Page
 [Rootly - Internal Status Page](https://rootly.com/account/status-pages/internal-status-page/private) 

If you have access to multiple environments in *Rootly*, ensure you are logged in to the **OutSystems-Prod** environment to view the Internal Status Page.

If you are not logged in to this environment, you will see a **404 Error** message.

### **From Slack**
- 
**When the Internal Status Page is updated**

A message (or two, if you are the Internal Communication Leader), will appear in the incident Slack channel whenever the Internal Status Page is updated. By clicking the **&ldquo;Internal Status Page&rdquo; link** in the message, anyone can access it:

- 
**From Bookmarks**

You can also access the Internal Status Page at any time through the ***Bookmarks ***section:

It will redirect you to the Incident Status Page, where you will see the last message shared for each Incident.
Internal Status Page
update internal status page - 2
From this page, you can:

- 
Access the Rootly Incident Page, by clicking the **Communication title**

- 
[Subscribe to updates](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/5344100671/Updating+the+Internal+Status+Page#Subscribing-to-Status-Page-updates), by clicking the `'Subscribe to updates'` button

### **From Rootly**
The Internal Status Page can also be accessed via Roolty, using the `'View Status Page'`** button**, under the **&ldquo;Status Page&rdquo; tab** in the Rootly Incident page:

Using this link, you will have access to **all the communications** that were done through the Status Page for **that specific Incident**:

## Updating the Internal Status Page during Incident resolution
### **When?**
The communication cadence for incident updates will be closely tied to key transitions in the incident response execution plan. These transitions are reflected in the available statuses on the status page: **Investigating, Identified, Monitoring, and Resolved.**

We recommend communicating at the following stages:

- 
**Investigating:** As soon as sufficient context about the impact and affected assets is gathered.

- 
**Identification:** Once the root cause of the incident has been identified and the impact confirmed.

- 
**Monitoring:** As soon as recovery actions have been implemented.

- 
**Resolution:** When the incident has been fully resolved.

The number of impacted customers and their time zones can, and should, also be taken into account when deciding the appropriate timing for communications.

### **How?**
**Whenever an update on incident resolution needs to be communicated, **a new message should be shared via the **Internal Status Page**. This can be done in 3 ways:
- 
Clicking the `'Update Internal Status Page'` **button** on the **&ldquo;Update Internal Status Page w/ System-Wide Incident&rdquo; **Slack message again, and follow the [same process](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/5344100671/Updating+the+Internal+Status+Page#Updating-the-Internal-Status-Page-for-the-first-time).

- 
Using the `/rootly statuspage` **command **in this same Slack channel will **open the &ldquo;Update status page&rdquo; pop-up window.**

- 
Through Rootly, using the `'Add to Status Page'`** button**, under the **&ldquo;Status Page&rdquo; tab** in the Incident page:

 For all scenarios, a similar pop-up window will appear, allowing the user to write the message to share. 

Remember to update the ***Status Page Template***** **field if you want a template to be added to the &ldquo;Message&rdquo; field. Also, update the ***Status ***field so that everyone understands which resolution phase the incident is in when reading the message.

## Incident Communication Templates

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

update internal status page - 3## Subscribing to Status Page updates
- 
Navigate to the Internal Status Page.

- 
Click on `'Subscribe to updates'` button. (image 1)

- 
Choose your notification method. (image 2)

- 
**Email:** This is the most common option. You'll enter your email address.

- 
**SMS/Text Message:** You'll enter your phone number.

- 
**RSS**: Get updates in an RSS news reader, no email or SMS required.

- 
**Slack:** Subscribe to updates in a specific Slack channel. - This doesn&rsquo;t work.

- 
Click `&lsquo;Subscribe&rsquo;` button.

image 1

image 2