---
title: Retrospective-SEV3-Output parameter from JS node with wrong value
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4267999250/Retrospective-SEV3-Output+parameter+from+JS+node+with+wrong+value
confluence_space: RKB
confluence_page_id: 4267999250
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV3-Output parameter from JS node with wrong value

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV3

Teams:&nbsp;trueBlueClient Runtime
#### 🕐 Timestamps
Started At:&nbsp;trueBlueJuly 5  9:06 AM WEST

Mitigated At:&nbsp;trueYellowJuly 8  8:50 AM WEST

Resolved At:&nbsp;trueGreenJuly 8  8:50 AM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/667-output-parameter-from-js-node-with-wrong-value)
[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3030761)

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

Carlos Xavier
#### Summary
----------------------------------------------**CONSIDERATIONS BEFORE PERFORMING THE ESCALATION TO R&amp;D (MANDATORY)**
None of the below points should be overlooked. Failure to do so may imply unnecessary effort.* * *
Ensure the ticket has been **categorized**, otherwise, the R&amp;D escalation will go unnoticed and not be worked on!**1.** For **Incidents**, the **IMAX** was consulted **beforehand** on which:- No incident models were found for the reported symptoms **OR**
- The incident model did not solve the issue **OR**
- The next step indicated in the Incident Model is an escalation to R&amp;D.
**2.** For **Questions**, the ChatODC on the **Slack channel** didn't return an acceptable answer.
**3.** Any other requests that explicitly indicate an R&amp;D escalation is needed.
**4**. **Incident impact assessment** was based on the **prioritization scoring matrix**.* * ***R&amp;D ESCALATION FORM**
Section comments can be removed for R&amp;D easier interpretation.**ISSUE DESCRIPTION AND HOW TO REPRODUCE**- The customer has a JavaScript node which contains an input parameter of Object type, and, inside that node, they do:$parameters.Output = JSON.stringify(Object.values($parameters.JSONResult));- Their Output var is text.- If they do console.log($parameters.Output ), they receive in the browser console the string properly.- Otherwise, their result is different when they use that output vars to deserialize JSON with the JSONDeserialize function.- When they just add breakpoint and try to see the value, they  could see the variable output is missing some quotes in some properties, but, their console.log() shows that their object is not missing anything.- Even trying to use Replace function from OutSystems doesn't help.![](https://supportoutsystems.zendesk.com/attachments/token/2M3wYIe6xK0qnktEsplyipLwN/?name=image.png)![](https://supportoutsystems.zendesk.com/attachments/token/ox4E0WhYeXCIiBcXjW3MBmM4h/?name=image.png)- Video of the replication attached.- https://drive.google.com/file/d/1qu8wBCuzNwsulVHNVYMOC02ksHd0Kiya/view  (also attached)**IMPACT ON THE CUSTOMER**- Normal. Its affecting their development work.**TROUBLESHOOTING STEPS &amp; WORKAROUND**- We were able to reproduce the behavior stated by the customer.- https://idg-cgm-dev.outsystems.app/CLICKDOCPrototype/SearchResults?Specialty=Allergologie&amp;Place=Allergologie%20-%20Koblenz
- Here are the steps to replicate the issue as demonstrated in the customer's video:- The customer is working with a library called &quot;SDK Wrapper&quot;.- This Library is being consumed by the application **CLICKDOC Prototype**.- In this library, within the Block &quot;SDK_Function&quot; we add a breakpoint in the Javascript node &quot;RemoveFirstChildObject&quot;- In this action is where the customer `console.log($parameters.Output )` the Output.- ![](https://supportoutsystems.zendesk.com/attachments/token/dEFTpiDSd0MmXMEqNe2IoRUdZ/?name=image.png)- Then we need to start debugging by selecting the application **CLICKDOC Prototype** as the entry app.- In the browser, select &quot;Allergologie&quot; and then &quot;Allergologie - Koblenz&quot; from the dropdown menu, and click the button. &quot;FINDEN&quot;- ![](https://supportoutsystems.zendesk.com/attachments/token/5qEmFRMp5y6rBnCqXHFz8jBBj/?name=Captura+de+pantalla+2024-07-03+164441.png)-- ![](https://supportoutsystems.zendesk.com/attachments/token/UMSMjScgXkY07M67wwzWkdayE/?name=Captura+de+pantalla+2024-07-03+164600.png)- ![](https://supportoutsystems.zendesk.com/attachments/token/JK6vQ3ToSnSF3Lg3p5unW39a1/?name=Captura+de+pantalla+2024-07-03+164748.png)- ![](https://supportoutsystems.zendesk.com/attachments/token/FHnxFuDjqo7e5WQLMjWjSlcsV/?name=Captura+de+pantalla+2024-07-03+164913.png)- We also attempted to replicate the issue with a simple in the ODC Sandbox.- https://gs-sandbox-ga-eu-01-dev.outsystems.app/Teste/JBKM3030761- The output in the browser console- ![](https://supportoutsystems.zendesk.com/attachments/token/x5OMKfEsREukPX91DEMLiAJeK/?name=image.png)- {&quot;my_text&quot;:&quot;test_2024-07-04 15:00:52&quot;,&quot;my_number&quot;:52,&quot;my_date&quot;:&quot;2024-07-03T16:00:00.000Z&quot;}- Meanwhile in the de-serializing the object- ![](https://supportoutsystems.zendesk.com/attachments/token/Szu0NrD3J9GvxUBDEaYkVOYfH/?name=image.png)- Serialize &gt; Deserialize: test_2024-07-04 15:00:52, 52, 2024-07-04\n\n JSON.stringify &gt; Deserialize: , 0, 1900-01-01- JSON De-serialize- test_2024-07-04 15:00:52, 52, 2024-07-04- Object De-serialize- , 0, 1900-01-01**TECH DATA OR ANY OTHER RELEVANT INFO**
Ring: ga
Tenant Id: 0e21d816-7778-4ee6-998c-1dea3a8eb4be
Tenant Prefix: idg-cgm
Region: eu-central-1
1LK.H3C.JQY.IG4.8OJ.I1U.6CQ.KZ4_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_Attachment(s):
theObject.txt - https://supportoutsystems.zendesk.com/attachments/token/dNC84tja1d0yNUvgojnySh9vb/?name=theObject.txtSDK Wrapper.oml - https://supportoutsystems.zendesk.com/attachments/token/dD4Yii68XIJ8SdZBxtRt78V0z/?name=SDK+Wrapper.omlCLICKDOC Prototype.oml - https://supportoutsystems.zendesk.com/attachments/token/O0NtbDBhrv45oYTWz0NbJ8aJl/?name=CLICKDOC+Prototype.oml
## 📝 RetrospectiveinfoDetails
**Ring:** ga
**System-wide impact:**&nbsp; 
**Tenant ID:** 0e21d816-7778-4ee6-998c-1dea3a8eb4be
**Tenant Prefix:** idg-cgm
**Routing Error Code:** N/A
**Product Area:** Phoenix::Application Runtime::Logic Flows
### Impact:
Customer was unable to deserialize a JSON into a structure
### Investigation and troubleshooting findings:
The customer was trying to deserialize a JSON that was not compatible with the desired structure. Not a bug.
### Resolution:
They customer may either:

- Adapt the JSON so that it matches the desired structure
- Change the desired data type to one that matches the JSON

## Tasks performed during incident resolution:
&nbsp;
## Executive Summary
[Guidelines](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4144496679/Incident+Retrospectives+-+Playbook#STEP-3---Write-the-Executive-Summary)
## Root Causes 
[Guidelines](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4144496679/Incident+Retrospectives+-+Playbook#STEP-1---Perform-the-Root-Cause-Analysis)

If the customer needs formal RCA, please fill out the following field with the document URL

[Please follow these instructions and place the RCA URL in the field below.](https://docs.google.com/document/d/13rXmBsOJh73nV2D6Z17SIBGBu2HOTWty5ddsvU000JM/edit#heading=h.bqxasxszr5q)

RCA URL

&lt;Place the URL of the customer RCA here if you have created one&gt;
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/667-output-parameter-from-js-node-with-wrong-value)

**Date**

**Source**

**User**

**Event**
July 4  9:11 AM WESTwebRootly
created an alert via
July 4  9:11 AM WESTwebRootly
Rootly created this incident
July 4  9:12 AM WESTwebRootly
In triage date has been set to July 4  9:11 AM WEST
July 4  9:22 AM WESTwebRootly
This incident was instantiated in Jira: RDINC-26432. Please work the incident using Rootly
July 4 10:12 AM WESTwebRootly
This incident was instantiated in Jira: RDINC-26432. Please work the incident using Rootly
July 4 11:14 PM WESTwebRui Garcia
Teams has been added: Client Runtime
July 4 11:14 PM WESTwebRui Garcia
Teams has been removed: Backend Runtime
July 5  9:06 AM WESTwebCarlos Xavier
Incident has been started
July 5  9:06 AM WESTwebCarlos XavierCarlos Xavier has been assigned as EngineerJuly 5  9:08 AM WESTwebCarlos XavierSend ZenDesk private comment has been set: Hi Support,  The invalid JSON you are getting by copying the value from the IDE seems to be because the IDE is escaping the double quotes (\`&quot;\`) by using two double quotes (\`&quot;&quot;\`) and is not related with what is happening in runtime.  The problem the customer is facing seems to be related with the fact that the JSON they are providing to the JSON Deserialize node does not match the structure of the desired Data Type. You can see the JSON they are providing represents a list of objects. It starts with a \`\[\` character, which denotes an array. However, the Data Type they have on the JSON Deserialize node is an &quot;AvailableSlots&quot; structure and not a list. This structure has an attribute &quot;Slots&quot; of type &quot;AvailableSlot List&quot;. In order to fix this, the customer has two options:*   Change the JSON value to represent an object equivalent to the &quot;AvailableSlots&quot; structure
*   Change the Data Type on the JSON Deserialize node to be &quot;AvailableSlot List&quot;Can you please ask the customer to do one of these changes and check if everything works that way?  Best regards,  
Carlos XavierJuly 5  9:08 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hi Support,  The invalid JSON you are getting by copying the value from the IDE seems to be because the IDE is escaping the double quotes (\`&quot;\`) by using two double quotes (\`&quot;&quot;\`) and is not related with what is happening in runtime.  The problem the customer is facing seems to be related with the fact that the JSON they are providing to the JSON Deserialize node does not match the structure of the desired Data Type. You can see the JSON they are providing represents a list of objects. It starts with a \`\[\` character, which denotes an array. However, the Data Type they have on the JSON Deserialize node is an &quot;AvailableSlots&quot; structure and not a list. This structure has an attribute &quot;Slots&quot; of type &quot;AvailableSlot List&quot;. In order to fix this, the customer has two options:*   Change the JSON value to represent an object equivalent to the &quot;AvailableSlots&quot; structure
*   Change the Data Type on the JSON Deserialize node to be &quot;AvailableSlot List&quot;Can you please ask the customer to do one of these changes and check if everything works that way?  Best regards,  
Carlos Xavier
July 5  9:08 AM WESTwebRootlySend ZenDesk private comment has been unsetJuly 5  9:08 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

July 6  2:34 PM WESTwebRootlyZenDesk Event Type has been set: solvedJuly 6  2:34 PM WESTwebRootly
The Global Support team marked this incident as closed in ZenDesk.
July 8  8:50 AM WESTwebCarlos Xavier
Incident has been resolved
July 8  8:50 AM WESTwebCarlos XavierImpact has been set: Customer was unable to deserialize a JSON into a structureJuly 8  8:50 AM WESTwebCarlos XavierInvestigation and troubleshooting findings has been set: The customer was trying to deserialize a JSON that was not compatible with the desired structure. Not a bug.July 8  8:50 AM WESTwebCarlos XavierResolution has been set: They customer may either:
- Adapt the JSON so that it matches the desired structure
- Change the desired data type to one that matches the JSON