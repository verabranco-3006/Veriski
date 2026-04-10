---
title: Retrospective-SEV3-OverflowMenu failed accessibility tests
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4370268264/Retrospective-SEV3-OverflowMenu+failed+accessibility+tests
confluence_space: RKB
confluence_page_id: 4370268264
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV3-OverflowMenu failed accessibility tests

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV3

Teams:&nbsp;trueBlueUi Components
#### 🕐 Timestamps
Started At:&nbsp;trueBlueAugust 2  9:50 AM WEST

Mitigated At:&nbsp;trueYellowAugust 19  4:56 PM WEST

Resolved At:&nbsp;trueGreenAugust 19  4:56 PM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/778-overflowmenu-failed-accessibility-tests)
[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3033305)

#### Summary
----------------------------------------------**ISSUE DESCRIPTION AND HOW TO REPRODUCE**
- The customer submitted their app to an auditing company for accessibility compliance. The report included the following issues for the OverflowMenu widget from OutSystemsUI:
1. Remove the **&lt;article&gt;** tag or replace it with a generic &lt;div&gt; tag.
2. For the &lt;nav&gt; tag:a. Move this tag to encompass the entire menu.
b. Add an attribute role=&quot;navigation&quot;.
c. Add an attribute aria-label=&quot;Language selection menu&quot;.3. Structure the list of versions with &lt;ul&gt; and &lt;li&gt; tags.
4. Empty the alt attributes (such as alt=&quot;&quot;) of the images of the different flags. --&gt; fix already implemented by the customer
5. For the &lt;button&gt; tag used to open the menu:a. Replace the value of the aria-label attribute with &quot;Select language&quot;.
b. Add an attribute aria-expanded=&quot;false&quot; when the menu is collapsed.
c. Update the value of this attribute to true when the menu is expanded.d. For the &lt;i&gt; tag, remove the alt attribute and we recommend adding an aria-hidden=&quot;true&quot; attribute. --&gt; fix already implemented by the customerThey clarified that the flaws that must be fixed to comply with WCAG21 are:- the **article** element is not adapted for this usage (please see the WCAG technique: https://www.w3.org/WAI/WCAG21/Techniques/html/H88 ) - Point 1
- the use of **aria-expanded** and **aria-haspopup** on the **article** is also a flaw (please see the WCAG techniques: https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-expanded#associated_roles and https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-haspopup#associated_roles )
- the **button** element contains the tag **aria-label=&quot;Trigger the balloon&quot;** which must be translated to the selected locale. Today, the value is hardcoded in the widget (Point 4a).An additional recommendation was also made:- the **button** should be within the **nav** element, instead of the **article** element (related to point 2). Please consider the following example:![](https://supportoutsystems.zendesk.com/attachments/token/ddWqdA3s75vuxedF5JylOxe6G/?name=image.png)**IMPACT ON THE CUSTOMER**
Normal - this is in a development stage and they need to be compliant with WCAG 2.1. If a fix in this widget is not possible, they will have to create a custom menu.&gt; the project will be submitted for a new accessibility evaluation in two weeks, and it won't be given the &quot;Go&quot; for production without accessibility approval.
&gt;
&gt; If you can't provide us with a solution within two weeks, we will implement an alternative to the OutSystems UI widget &quot;OverflowMenu&quot;.**TROUBLESHOOTING STEPS &amp; WORKAROUND**- By testing a simple application with the OverflowMenu widget, we could replicate what they mentioned. However, the only problem that we noticed when using a Screen reader was the hardcoded aria-label &quot;Trigger the balloon&quot; for the button that triggers the OverflowMenu. Nevertheless, the customer says that all points besides the recommendation (button inside nav element) are considered errors and fail to comply with WCAG 2.1
- Although the **article** element doesn't seem to be affecting the correct screen reading, it is strange that this is being used for a Menu and we found no reason for this usage - we cannot change this without modifying the component
- Regarding the **aria-expanded** tag (points 5b and 5c), we see that it is always set as &quot;true&quot;. The Overflow Menu from Gmail, which seems to have been used as a template by R&amp;D at https://outsystemsrd.atlassian.net/wiki/spaces/RDMBVS/pages/3758456997/Overflow+Menu+-+Accessibility+Assessment, does have aria-expanded updated correctly - we can implement this by using Javascript inside the OnMenuToggled event of the OverflowMenu widget
- We believe that the point that mentions the use of **aria-expanded** and **aria-haspopup** inside the article element should be resolved if the article element is removed/replaced
- We also confirmed that the tag **aria-label=&quot;Trigger the balloon&quot;** is indeed hardcoded for this widget and there is no option to change it. This value will be read by the Screen Reader so it should be customizable in a simple way (e.g., attribute/property of the widget) - we can override this value inside the Initialized event of the widget. However, we had to manually set the translation according to the current locale. Not sure if this should be automatically translated or not- We need your assistance to understand if these points can be fixed on the component and, in that case, what would be the ETA. If a fix is not possible or will take a long time, do you have any possible workaround for the article element or they will have to use a custom widget?**TECH DATA OR ANY OTHER RELEVANT INFO**- Ring: ga
Tenant Id: 615db0f9-40a9-4e65-94f1-0bc57e28b22b
Tenant Prefix: ilr
Region: eu-central-1
MBJ.GXS.LV8.GCH.4TY.RID.KVI.GOU
- OutSystems UI 2.19.1
- We are attaching our sample app, 'Teste 3033305.oml', with the applied workarounds
- The customer's app with their Language selection menu is available at https://ilr-test.outsystems.app/SmartCompare/General?ContentType=0
- This customer had multiple accessibility issues related to their SmartCompare app. We have created a clone of the app to perform the workarounds, and if R&amp;D has PIM access it can be freely access and tested:![](https://supportoutsystems.zendesk.com/attachments/token/8flX8vI9x8jafdexQWz4mWE4J/?name=image.png)_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/778-overflowmenu-failed-accessibility-tests)

**Date**

**Source**

**User**

**Event**
July 30 12:42 PM WESTwebRootly
created an alert via
July 30 12:42 PM WESTwebRootly
Rootly created this incident
July 30 12:42 PM WESTwebRootly
In triage date has been set to July 30 12:42 PM WEST
July 30 12:52 PM WESTwebRootly
This incident was instantiated in Jira: RDINC-27849. Please work the incident using Rootly
July 30  1:42 PM WESTwebRootly
This incident was instantiated in Jira: RDINC-27849. Please work the incident using Rootly
July 30  2:04 PM WESTwebDavid Pires
Teams has been added: Client Runtime
July 30  2:04 PM WESTwebDavid Pires
Teams has been removed: UIComponents
July 30  2:27 PM WESTwebDavid PiresSend ZenDesk private comment has been set: Hey team,  This is the same situation as the Table one, we can't change the HTML structure without risking breaking client's apps and on top of that we are not compliant with that standard and so, this should be treated as a new feature request .July 30  2:27 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hey team,  This is the same situation as the Table one, we can't change the HTML structure without risking breaking client's apps and on top of that we are not compliant with that standard and so, this should be treated as a new feature request .
July 30  2:27 PM WESTwebRootlySend ZenDesk private comment has been unsetJuly 30  2:28 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

July 30  7:10 PM WESTwebDavid Pires
Incident has been started
July 30  7:11 PM WESTwebDavid Pires
Incident has been mitigated
July 31  2:38 PM WESTwebRootlyZendesk Private Comment has been set: ----------------------------------------------**Update to R&amp;D**
Hi team,Thanks for your efforts thus far.We acknowledge that the quickest way for the customer to be compliant with accessibility standards is to develop their own widgets/components to replace the non-compliant ones.However, I am not sure how to position ourselves going forward regarding these tickets - we are hesitant to close tickets without a clear path forward, considering there is no customer-facing problem management framework such as in O11 (RPM), which allows customers to at least keep track of the progress on such items and we can happily close the tickets.- In this case, considering we clearly claim OutSystems UI patterns are compliant with WCAG 2.1 in our documentation, and considering we have already acknowledged that we are in fact **not compliant**, how can we consider this a new feature request as opposed to a product issue?Regardless of what we call it, we need help managing expectations, both the customers' and ours - if there is no ETA and no way to track this on the customer side, we (Global Support) typically default to leaving the ticket On-hold until there is a fix (or a clear &quot;no fix required&quot; statement), and only then we close the ticket.- However, we are not sure how backlogged these items are, so we can't decide accordingly - are we currently working on or planning to work on them soon, or could they take months/years before they are fully addressed?With that said, what do you suggest we do? What are your thoughts about this rationale?Thanks in advance for your attention!
Jo&atilde;o Neves__July 31  2:38 PM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
Hi team,Thanks for your efforts thus far.We acknowledge that the quickest way for the customer to be compliant with accessibility standards is to develop their own widgets/components to replace the non-compliant ones.However, I am not sure how to position ourselves going forward regarding these tickets - we are hesitant to close tickets without a clear path forward, considering there is no customer-facing problem management framework such as in O11 (RPM), which allows customers to at least keep track of the progress on such items and we can happily close the tickets.- In this case, considering we clearly claim OutSystems UI patterns are compliant with WCAG 2.1 in our documentation, and considering we have already acknowledged that we are in fact **not compliant**, how can we consider this a new feature request as opposed to a product issue?Regardless of what we call it, we need help managing expectations, both the customers' and ours - if there is no ETA and no way to track this on the customer side, we (Global Support) typically default to leaving the ticket On-hold until there is a fix (or a clear &quot;no fix required&quot; statement), and only then we close the ticket.- However, we are not sure how backlogged these items are, so we can't decide accordingly - are we currently working on or planning to work on them soon, or could they take months/years before they are fully addressed?With that said, what do you suggest we do? What are your thoughts about this rationale?Thanks in advance for your attention!
Jo&atilde;o Neves__
August 2  9:50 AM WESTwebDavid Pires
Incident has been started
August 2  9:52 AM WESTwebDavid PiresSend ZenDesk private comment has been set: Hey team,  You are right, we do support WCAG 2.1 for OutSystems UI. But I handling the ticket for the Table (who doesn't fall under OutsystemUI) and miss that in fact, this component is part of it and should follow the WCAG 2.1 guidelines. I'll sent it to the right team, so they can follow up on itAugust 2  9:52 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hey team,  You are right, we do support WCAG 2.1 for OutSystems UI. But I handling the ticket for the Table (who doesn't fall under OutsystemUI) and miss that in fact, this component is part of it and should follow the WCAG 2.1 guidelines. I'll sent it to the right team, so they can follow up on it
August 2  9:52 AM WESTwebRootlySend ZenDesk private comment has been unsetAugust 2  9:52 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

August 2  9:59 AM WESTwebDavid Pires
Teams has been added: UIComponents
August 2  9:59 AM WESTwebDavid Pires
Teams has been removed: Client Runtime
August 2 11:01 AM WESTwebRootlyZendesk Private Comment has been changed to: ----------------------------------------------**Update to R&amp;D**
Hi team,Apologies, but I'm not sure who sent that reply from Rootly since we only get the message text on Zendesk, especially considering that there were additional responses from Gon&ccedil;alo Martins via Jira, so I'm a bit confused.In any case, does this mean that this widget will get a higher priority and will be addressed before October?Reason I ask is because the customer has their go-live on October and they are pushing for our assistance in creating an alternative widget from scratch as a workaround, and I'm still debating whether this should be our responsibility (support/R&amp;D) or if this is something to be sent to Success@Scale - your response will be very relevant for this.Thanks again!_&lt;! do not remove this line, this will be used to the trigger Rootly :: ODC ticket escalated from Global Support to R&amp;D (ODC_escalation) :: New Comment_ _#trigger_update_r&amp;d_odc !&gt;_August 2 11:01 AM WESTwebRootly
NEW MESSAGE FROM GLOBAL SUPPORT:
----------------------------------------------**Update to R&amp;D**
Hi team,Apologies, but I'm not sure who sent that reply from Rootly since we only get the message text on Zendesk, especially considering that there were additional responses from Gon&ccedil;alo Martins via Jira, so I'm a bit confused.In any case, does this mean that this widget will get a higher priority and will be addressed before October?Reason I ask is because the customer has their go-live on October and they are pushing for our assistance in creating an alternative widget from scratch as a workaround, and I'm still debating whether this should be our responsibility (support/R&amp;D) or if this is something to be sent to Success@Scale - your response will be very relevant for this.Thanks again!__
August 19  4:56 PM WESTwebRootly
The Global Support team marked this incident as closed in ZenDesk.
August 19  4:56 PM WESTwebRootly
Incident has been resolved
August 19  4:56 PM WESTwebRootlyZenDesk Event Type has been set: solved