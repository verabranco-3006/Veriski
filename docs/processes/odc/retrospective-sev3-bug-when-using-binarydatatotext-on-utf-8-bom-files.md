---
title: Retrospective-SEV3-Bug when using BinaryDataToText on UTF-8 bom files.
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4336648367/Retrospective-SEV3-Bug+when+using+BinaryDataToText+on+UTF-8+bom+files.
confluence_space: RKB
confluence_page_id: 4336648367
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV3-Bug when using BinaryDataToText on UTF-8 bom files.

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV3

Teams:&nbsp;trueBlueExtended Runtime&nbsp;trueBlueIde Group&nbsp;trueBlueIde Group
#### 🕐 Timestamps
Started At:&nbsp;trueBlueAugust 5  2:04 PM WEST

Mitigated At:&nbsp;trueYellowAugust 6  1:43 PM WEST

Resolved At:&nbsp;trueGreenAugust 6  1:43 PM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/824-bug-when-using-binarydatatotext-on-utf-8-bom-files)
[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3038737)

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

Rafael Duarte
#### Summary
----------------------------------------------**ISSUE DESCRIPTION AND HOW TO REPRODUCE**
Customer reports an issue with the `BinaryDataToText` action where the behavior differs based on whether the encoding parameter is explicitly set to &quot;utf-8&quot; or omitted (which should default to &quot;utf-8&quot;). Additionally, there is a discrepancy in how the output is displayed in the debugger, so in reality are 2 situations that might be related:- Encoding Parameter Behavior:- When the encoding is explicitly set to &quot;utf-8&quot; in the `BinaryDataToText` action, there are no issues.- When the encoding parameter is omitted (which defaults to &quot;utf-8&quot;), the behavior changes, leading to issues.- Expected behavior: Both explicitly setting &quot;utf-8&quot; and omitting the encoding (defaulting to &quot;utf-8&quot;) should result in the same behavior.
- Debugger Inconsistency:- When debugging, the value of `BinaryDataToText` does not show the zero-width non-breaking space (BOM).- This was verified by copying the value from the debugger into Visual Studio Code.- However, when performing a `Split_string` operation (splitting on new lines) on the output of `BinaryDataToText`, the BOM/ZWNBS does appear.- Expected behavior: The debugger should accurately represent the output of `BinaryDataToText`.**IMPACT ON THE CUSTOMER**
Normal, still in development phase of the application.**TROUBLESHOOTING STEPS &amp; WORKAROUND**
Customer provide us the documentation where they report the situation in detail:- Behavior.pdf
We also pick their application and test the behavior with the removal of UTF8 of the action:- https://gs-sandbox-ga-eu-01-dev.outsystems.app/AdviseursPortaal/?_ts=638584531138130889&amp;_waitForClient=true
- ![](https://supportoutsystems.zendesk.com/attachments/token/7g0IlZ2cB2S4wVqSYqfDMxaOt/?name=image.png)
According to our public docs:- https://success.outsystems.com/documentation/outsystems_developer_cloud/outsystems_language_and_elements/libraries/binarydata/
- https://success.outsystems.com/documentation/11/reference/outsystems_apis/binarydata_api/#BinaryDataToText![](https://supportoutsystems.zendesk.com/attachments/token/gL1kL597e9Cy0bdjK0uS7i0fL/?name=image.png)
- although it doesn't refer the BOM, there is no valid justification to present to the customer due to the details below:
- https://www.unicode.org/faq/utf_bom.html#bom5
Q: Can a UTF-8 data stream contain the BOM character (in UTF-8 form)? If yes, then can I still assume the remaining UTF-8 bytes are in big-endian order?
Yes, UTF-8 can contain a BOM. However, it makes _no_ difference as to the endianness of the byte stream. UTF-8 always has the same byte order. An initial BOM is _only_ used as a signature &mdash; an indication that an otherwise unmarked text file is in UTF-8. Note that some recipients of UTF-8 encoded data do not expect a BOM. Where UTF-8 is used_ transparently_ in 8-bit environments, the use of a BOM will interfere with any protocol or file format that expects specific ASCII characters at the beginning, such as the use of &ldquo;#!&rdquo; of at the beginning of Unix shell scripts._ _[AF]- https://learn.microsoft.com/en-us/globalization/encoding/unicode-standard![](https://supportoutsystems.zendesk.com/attachments/token/WNFi0d07EcLzBa0R5BUgYWzyq/?name=image.png)Also, in a past case but not related to csv, #2955214 but in regards to JSON file, instead of CSV, our statement:&gt; We have confirmed that the JSON file provided is encoded with UTF-8-BOM which is not a supported format. As section 8.1 of RFC-7159 (https://www.rfc-editor.org/rfc/rfc7159#section-8.1) mentions, the byte order mark (BOM) is illegal in JSON. This is why the platform does not support this type of encoding either. If you save the file with the encoding UTF-8, removing the byte order mark, there will be no error when deserializing it.
&gt;
&gt; However, we don't know if the same behavior is expected.Due to that, as a workaround, we suggest the possible solution on the forum would at least the customer?![](https://supportoutsystems.zendesk.com/attachments/token/ZZXY6IYR4gwVgELGiQiBvcRxX/?name=image.png)- https://www.outsystems.com/forums/discussion/37973/specific-file-type-and-encoding/#- Since this component is also present in ODC:- ![](https://supportoutsystems.zendesk.com/attachments/token/jx9F0oWmRX87NvYK2sR8BuOQw/?name=image.png)- However, customer doesn't seem interested.
Due to that, we would like to request help to:- Does the `BinaryDataToText` action is expected to show different behaviors when the encoding parameter is explicitly set versus omitted?
- Does the debugger should reflect the presence of BOM/ZWNBS in the `BinaryDataToText` output?**TECH DATA OR ANY OTHER RELEVANT INFO**
Ring: ga
Tenant Id: c988378a-93fa-4884-9eb9-43d53708e42f
Tenant Prefix: veldsink
Region: eu-central-1
R3L.0LG.MUB.6GP.33S.YUE.26R.G0D
App POC -&gt; https://gs-sandbox-ga-eu-01-dev.outsystems.app/AdviseursPortaal/?_ts=638584531138130889&amp;_waitForClient=true
apps oml -&gt; CustomerAPP.zip_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_
## 📝 RetrospectiveinfoDetails
**Ring:** ga
**System-wide impact:**&nbsp; 
**Tenant ID:** c988378a-93fa-4884-9eb9-43d53708e42f
**Tenant Prefix:** veldsink
**Routing Error Code:** N/A
**Product Area:** Phoenix::Application Runtime::Logic Flows
### Impact:
Customer has issue with text encoding, spending development time troubleshooting and finding issue with System Action.
### Investigation and troubleshooting findings:### Resolution:
Workaround available, follow-up action item created to address system action issue.
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/824-bug-when-using-binarydatatotext-on-utf-8-bom-files)

**Date**

**Source**

**User**

**Event**
August 5 12:15 PM WESTwebRootly
created an alert via
August 5 12:15 PM WESTwebRootly
Rootly created this incident
August 5 12:15 PM WESTwebRootly
In triage date has been set to August 5 12:15 PM WEST
August 5 12:25 PM WESTwebRootly
This incident was instantiated in Jira: RDINC-28054. Please work the incident using Rootly
August 5  1:15 PM WESTwebRootly
This incident was instantiated in Jira: RDINC-28054. Please work the incident using Rootly
August 5  2:04 PM WESTwebRui Garcia
Incident has been started
August 5  2:04 PM WESTwebRui GarciaRui Garcia has been assigned as EngineerAugust 5  8:37 PM WESTwebRui Garcia
Teams has been added: Extended Runtime&nbsp;&nbsp;IDEGroup&nbsp;&nbsp;IDE Group
August 5  8:37 PM WESTwebRui Garcia
Teams has been removed: Backend Runtime
August 5  8:38 PM WESTwebRui Garcia
Assigning to Rafael as on-call for Extended Runtime.
I believe we can say the primary issue is the misbehavior of the extension even though there isn't much more to do other than release a fix.
August 5  8:39 PM WESTwebRui GarciaRafael Duarte has been assigned as EngineerAugust 5  8:48 PM WESTwebRui Garcia
There are two issues reported in this Incident.The first one is related with the runtime behavior of System Extension Action BinaryDataToText. When the Encoding input parameter is left empty it exhibits one behavior (incorrect), but when the same input parameter is filled with &quot;UTF-8&quot; it exhibits another (the correct one).As System Extensions are owned by Extended Runtime Team, I&rsquo;m reassigning the incident to the team for a proper follow up.The second one is related with the Debugger experience and how special characters are displayed in the UI. In the escalation an inconsistency is highlighted: the output of BinaryDataToText does display BOM/ZWNBSP characters while the output of String_Split does. Unfortunately, I&rsquo;m unable to reproduce the reported inconsistency. Notice the example where there is a ZWNBSP before the namespace word in all 3 debugger listed variables (the output of BinaryDataToText, and both the Current and the List[0] of the output of String_Split):Copying those values from ODC Studio to a Text Editor (Notepad++ with option Enabled to display Non-Printing Characters) we can confirm the characters are actually there, they simply aren&rsquo;t being displayed:This means the evaluation of those variables from ODC Studio to runtime is consistent and actually matches the runtime behavior. ODC Studio then renders the value as it should (notice we also don&rsquo;t display CR and LF explicitly and instead we interpret them and end-of-lines, otherwise there would be only a single line on those values). Maybe there&rsquo;s room for both alternatives in the IDE UX, like an advanced mode to have access to some kind of Raw version of the Text? I&rsquo;m adding IDE Team to assess this feedback and provide their view on the matter.
August 6 11:10 AM WESTwebRafael Duarte
Action Item - Follow-up: https://outsystemsrd.atlassian.net/browse/RTAFB-7908 has been added.
August 6  1:40 PM WESTwebRafael Duarte
Follow-up action item to fix the incorrect behavior has been created.
August 6  1:41 PM WESTwebRafael Duarte
Marking issue as solved as customer is not blocked.
August 6  1:43 PM WESTwebRafael Duarte
Incident has been resolved
August 6  1:43 PM WESTwebRafael DuarteImpact has been set: Customer has issue with text encoding, spending development time troubleshooting and finding issue with System Action.August 6  1:43 PM WESTwebRafael DuarteResolution has been set: Workaround available, follow-up action item created to address system action issue.## 📝 Follow Up Items[View on Rootly](https://rootly.com/account/incidents/824-bug-when-using-binarydatatotext-on-utf-8-bom-files#nav-action-items)

**Summary**

**Priority**

**Status**

**Assignee**

**Links**
https://outsystemsrd.atlassian.net/browse/RTAFB-7908trueYellowMediumtrueBlueOpen