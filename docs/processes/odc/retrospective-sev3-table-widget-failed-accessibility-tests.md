---
title: Retrospective-SEV3-Table widget failed accessibility tests
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4356734994/Retrospective-SEV3-Table+widget+failed+accessibility+tests
confluence_space: RKB
confluence_page_id: 4356734994
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV3-Table widget failed accessibility tests

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV3

Teams:&nbsp;trueBlueClient Runtime
#### 🕐 Timestamps
Started At:&nbsp;trueBlueJuly 30  2:13 PM WEST

Mitigated At:&nbsp;trueYellowJuly 30  2:25 PM WEST

Resolved At:&nbsp;trueGreenAugust 13  8:15 AM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/774-table-widget-failed-accessibility-tests)
[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3034654)

#### Summary
----------------------------------------------**ISSUE DESCRIPTION AND HOW TO REPRODUCE**
They are requesting our help to do the following corrections after they received an accessibility report.- . Remove the **role=&quot;grid&quot;** attribute from the **&lt;table&gt;**.
- Use **&lt;button&gt;** elements in the sortable columns, instead of using the **&lt;div class=&quot;sortable-icon&quot;&gt;&lt;/div&gt;** element.
- At the column header **&lt;th&gt;** tag level, add an **aria-sort=&quot;descending&quot;** attribute when sorting from highest to lowest or **aria-sort=&quot;ascending&quot;** when from lowest to highest.- We didn't separate the tickets since is all related to the same table.**IMPACT ON THE CUSTOMER**
Normal, customer needs this points addressed to be complied with WCAG21**TROUBLESHOOTING STEPS &amp; WORKAROUND**- Improvements in order to be complied with:- - https://accessibilite.public.lu/fr/raweb1/glossaire.html#tableau-de-donnees-ayant-un-titre- - https://www.w3.org/WAI/WCAG21/Techniques/html/H391. Remove the **role=&quot;grid&quot;** attribute from the **&lt;table&gt;**.- Located here:- ![](https://supportoutsystems.zendesk.com/attachments/token/EbIZfgeiK4PaCq84n6aGLpc3T/?name=image.png)- Natively, when using accessibility should be disabled according to the report, however, a workaround might be using a JS to remove the class on the onReady:- ![](https://supportoutsystems.zendesk.com/attachments/token/kiFpbPrzds0sIG2hrNq5ag6kf/?name=image.png)- ![](https://supportoutsystems.zendesk.com/attachments/token/QGLRPxGkxec6CLk6unN9s0wAr/?name=image.png)- It actually works, but would be the right way? 🔨️
2. Use **&lt;button&gt;** elements in the sortable columns, instead of using the **&lt;div class=&quot;sortable-icon&quot;&gt;&lt;/div&gt;** element.- This is located on same table:- ![](https://supportoutsystems.zendesk.com/attachments/token/cpThpFKxATotJqA9DIJwhd7tg/?name=image.png)- A workaround would be to put a button and a client action to apply the sort, kinda works.- ![](https://supportoutsystems.zendesk.com/attachments/token/2WYN17P70SmVCkmhskRUMRFwl/?name=image.png)
3. At the column header **&lt;th&gt;** tag level, add an **aria-sort=&quot;descending&quot;** attribute when sorting from highest to lowest or **aria-sort=&quot;ascending&quot;** when from lowest to highest.- The attribute must only be present in the currently sorted column. When the sorted column is changed, the attribute is deleted from the old column and set in the new sorted column.- As an example of the expected HTML:- ![](https://www.outsystems.com/SupportPortal/DownloadAmazon.aspx?FileName=1721978430000__1721978431199.png&amp;TicketGUID=8a1076e0-b20d-4498-b688-cd6343df09c6)- For this I assume that adding the class manually depending on the order, however this should be natively on component.To see the issue, just access the https://ilr-test.outsystems.app/SmartCompare/Dashboard and select an option to compare:- ![](https://supportoutsystems.zendesk.com/attachments/token/sVLZUuBYkJVdipzvJQNYJMG0I/?name=image.png)We would like help on R&amp;D to understand if this should be natively applied on our Widgets since regarding this 3 points our public documentation doesn't help much. And if at least the 1st workaround could be provided.
Also, customer will have more widgets to report, since I was on call with them, and they have a 52 report with dozens of issues, however, we will try to split in different cases as much as possible, and if there is the need for that report we can try to ask the customer if it can provide.
We also create a clone of the app to perform the workarounds, and if R&amp;D has PIM access it can be freely access and tested:![](https://supportoutsystems.zendesk.com/attachments/token/8flX8vI9x8jafdexQWz4mWE4J/?name=image.png)**TECH DATA OR ANY OTHER RELEVANT INFO**
Ring: ga
Tenant Id: 615db0f9-40a9-4e65-94f1-0bc57e28b22b
Tenant Prefix: ilr
Region: eu-central-1
MBJ.GXS.LV8.GCH.4TY.RID.KVI.GOU
OMLS and depedencies: SmartCOmpare.zip_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_Attachment(s):
SmartCOmpare.zip - https://supportoutsystems.zendesk.com/attachments/token/gEuOYzPFyIo2iujz9o6JVmQ1t/?name=SmartCOmpare.zip
## 📝 RetrospectiveinfoDetails
**Ring:** ga
**System-wide impact:**&nbsp; 
**Tenant ID:** 615db0f9-40a9-4e65-94f1-0bc57e28b22b
**Tenant Prefix:** ilr
**Routing Error Code:** N/A
**Product Area:** Phoenix::Application Runtime::Starter Apps::OutSystems UI
### Impact:### Investigation and troubleshooting findings:### Resolution:## Tasks performed during incident resolution:
&nbsp;
## Executive Summary
[Guidelines](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4144496679/Incident+Retrospectives+-+Playbook#STEP-3---Write-the-Executive-Summary)
## Root Causes 
[Guidelines](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4144496679/Incident+Retrospectives+-+Playbook#STEP-1---Perform-the-Root-Cause-Analysis)

If the customer needs formal RCA, please fill out the following field with the document URL

[Please follow these instructions and place the RCA URL in the field below.](https://docs.google.com/document/d/13rXmBsOJh73nV2D6Z17SIBGBu2HOTWty5ddsvU000JM/edit#heading=h.bqxasxszr5q)

RCA URL

&lt;Place the URL of the customer RCA here if you have created one&gt;
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/774-table-widget-failed-accessibility-tests)

**Date**

**Source**

**User**

**Event**
July 29  5:00 PM WESTwebRootly
created an alert via
July 29  5:00 PM WESTwebRootly
Rootly created this incident
July 29  5:00 PM WESTwebRootly
In triage date has been set to July 29  5:00 PM WEST
July 30  2:13 PM WESTwebDavid Pires
Teams has been added: Client Runtime
July 30  2:13 PM WESTwebDavid Pires
Teams has been removed: UIComponents
July 30  2:13 PM WESTwebDavid Pires
Incident has been started
July 30  2:23 PM WESTwebDavid PiresSend ZenDesk private comment has been set: Hey team,  We are not WCAG21 compliance, and even though, some changes make sense. we can't change the HTML structure (like removing attributes or&nbsp; replacing html elements)&nbsp; without risking breaking other client's apps. In this situation the workaround would be to create a JS script (OnReady) that apply the require changes  Since we don't comply with WCAG21, this should be treated as a feature requestJuly 30  2:24 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hey team,  We are not WCAG21 compliance, and even though, some changes make sense. we can't change the HTML structure (like removing attributes or&nbsp; replacing html elements)&nbsp; without risking breaking other client's apps. In this situation the workaround would be to create a JS script (OnReady) that apply the require changes  Since we don't comply with WCAG21, this should be treated as a feature request
July 30  2:24 PM WESTwebRootlySend ZenDesk private comment has been unsetJuly 30  2:24 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

July 30  2:25 PM WESTwebDavid Pires
Incident has been mitigated
July 31  9:37 AM WESTwebRootlyZendesk Private Comment has been set: ----------------------------------------------**Update to R&amp;D**
Hello team,Thank you for the update and time.We understand that for this points we are not complied, do to that are we permit said that to customer? Also, we will be any ETA or task that we can follow?Also, customer will need at least the workaround for the 3 points to present to the reviewer entity:- Remove the **role=&quot;grid&quot;** attribute from the ****.
- Use **** elements in the sortable columns, instead of using the **&nbsp;&nbsp;** element.
- At the column header **** tag level, add an **aria-sort=&quot;descending&quot;** attribute when sorting from highest to lowest or **aria-sort=&quot;ascending&quot;** when from lowest to highest.Would be possible to confirm if the first point workaround suggest by us is ok, and remaining other points how can it be achieved?Best regards,__July 31  9:37 AM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
Hello team,Thank you for the update and time.We understand that for this points we are not complied, do to that are we permit said that to customer? Also, we will be any ETA or task that we can follow?Also, customer will need at least the workaround for the 3 points to present to the reviewer entity:- Remove the **role=&quot;grid&quot;** attribute from the **

**.
- Use **** elements in the sortable columns, instead of using the **&nbsp;&nbsp;** element.
- At the column header **** tag level, add an **aria-sort=&quot;descending&quot;** attribute when sorting from highest to lowest or **aria-sort=&quot;ascending&quot;** when from lowest to highest.Would be possible to confirm if the first point workaround suggest by us is ok, and remaining other points how can it be achieved?Best regards,__July 31  9:37 AM WESTwebRootlyZendesk Private Comment has been changed to: ------------------------------------------------ This notification was sent from Zendesk Support ticket #3034654 to all linked JIRA issues by Cristiano Costa. --**Update to R&amp;D**
Hello team,Thank you for the update and time.We understand that for this points we are not complied, do to that are we permit said that to customer? Also, we will be any ETA or task that we can follow?Also, customer will need at least the workaround for the 3 points to present to the reviewer entity:- Remove the **role=&quot;grid&quot;** attribute from the **&lt;table]**.
- Use **[button]** elements in the sortable columns, instead of using the **[div class=&quot;sortable-icon&quot;][/div]** element.
- At the column header **[th]** tag level, add an **aria-sort=&quot;descending&quot;** attribute when sorting from highest to lowest or **aria-sort=&quot;ascending&quot;** when from lowest to highest.Would be possible to confirm if the first point workaround suggest by us is ok, and remaining other points how can it be achieved?Best regards,_[! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_July 31  9:37 AM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
------------------------------------------------ This notification was sent from Zendesk Support ticket #3034654 to all linked JIRA issues by Cristiano Costa. --**Update to R&amp;D**
Hello team,Thank you for the update and time.We understand that for this points we are not complied, do to that are we permit said that to customer? Also, we will be any ETA or task that we can follow?Also, customer will need at least the workaround for the 3 points to present to the reviewer entity:- Remove the **role=&quot;grid&quot;** attribute from the **

_August 2 11:03 AM WESTwebDavid PiresSend ZenDesk private comment has been set: Hey team,  
regarding the workaround, this needs to be done using custom Javascript code.&nbsp; And as you suggested, the OnReady event is the best option. &nbsp; We can give suggestion on how to do it, but as any custom code, client must adapt to their specific needs&nbsp;  For the role table, your workaround is the best solution I can think of  For second point, I think a good alternative is to just add the role=&quot;button&quot; to the existing div, it should also fall under the WCAG spec and works with screen readers.&nbsp;  For the column header, the way sorting works for a table can vary a lot from app to app, so we don't have a good way to automatically add an aria attribute for it. The workaround is for it to be done with low code + a custom js. The client can create a dynamic sort, then on the Sort action, he can read the SortBy input to know which header he must apply the aria attributeAugust 2 11:03 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hey team,  
regarding the workaround, this needs to be done using custom Javascript code.&nbsp; And as you suggested, the OnReady event is the best option. &nbsp; We can give suggestion on how to do it, but as any custom code, client must adapt to their specific needs&nbsp;  For the role table, your workaround is the best solution I can think of  For second point, I think a good alternative is to just add the role=&quot;button&quot; to the existing div, it should also fall under the WCAG spec and works with screen readers.&nbsp;  For the column header, the way sorting works for a table can vary a lot from app to app, so we don't have a good way to automatically add an aria attribute for it. The workaround is for it to be done with low code + a custom js. The client can create a dynamic sort, then on the Sort action, he can read the SortBy input to know which header he must apply the aria attribute
August 2 11:03 AM WESTwebRootlySend ZenDesk private comment has been unsetAugust 2 11:03 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

August 7 11:36 AM WESTwebRootlyZendesk Private Comment has been changed to: ----------------------------------------------**Update to R&amp;D**
Hello team, thank you for your feedback.We will propose these actions and workarounds to customer, nevertheless, would be any improvements on our component in order for us to be complaint on these points?Best regards,_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_August 7 11:36 AM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
Hello team, thank you for your feedback.We will propose these actions and workarounds to customer, nevertheless, would be any improvements on our component in order for us to be complaint on these points?Best regards,__
August 7 11:36 AM WESTwebRootlyZendesk Private Comment has been changed to: ------------------------------------------------ This notification was sent from Zendesk Support ticket #3034654 to all linked JIRA issues by Cristiano Costa. --**Update to R&amp;D**
Hello team, thank you for your feedback.We will propose these actions and workarounds to customer, nevertheless, would be any improvements on our component in order for us to be complaint on these points?Best regards,_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_August 7 11:36 AM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
------------------------------------------------ This notification was sent from Zendesk Support ticket #3034654 to all linked JIRA issues by Cristiano Costa. --**Update to R&amp;D**
Hello team, thank you for your feedback.We will propose these actions and workarounds to customer, nevertheless, would be any improvements on our component in order for us to be complaint on these points?Best regards,__
August 7  3:59 PM WESTwebTiago M. PereiraSend ZenDesk private comment has been set: Hello support,  
Thank you for your suggestions. We will need to conduct further analysis before making any decisions. I have already escalated this information for additional review. Please **keep this matter internal** until further notice. ~  Please keep in mind that it's not certain we will implement these improvements.&nbsp;  
Thank you for your understanding.  Best Regards,  
Tiago PereiraAugust 7  3:59 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hello support,  
Thank you for your suggestions. We will need to conduct further analysis before making any decisions. I have already escalated this information for additional review. Please **keep this matter internal** until further notice. ~  Please keep in mind that it's not certain we will implement these improvements.&nbsp;  
Thank you for your understanding.  Best Regards,  
Tiago Pereira
August 7  3:59 PM WESTwebRootlySend ZenDesk private comment has been unsetAugust 7  3:59 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

August 7  4:22 PM WESTwebRootlyZendesk Private Comment has been changed to: ----------------------------------------------**Update to R&amp;D**
Hey team,Don't worry we will keep only to us until further notice.Best regards,
_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_August 7  4:22 PM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
Hey team,Don't worry we will keep only to us until further notice.Best regards,
__
August 13  8:15 AM WESTwebRootly
The Global Support team marked this incident as closed in ZenDesk.
August 13  8:15 AM WESTwebRootly
Incident has been resolved
August 13  8:15 AM WESTwebRootlyZenDesk Event Type has been set: solved