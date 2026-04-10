---
title: Retrospective-SEV3-Mismatched anonymous define() module trying to redirect to URL or just navigating to other screen
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4312531118/Retrospective-SEV3-Mismatched+anonymous+define+module+trying+to+redirect+to+URL+or+just+navigating+to+other+screen
confluence_space: RKB
confluence_page_id: 4312531118
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV3-Mismatched anonymous define() module trying to redirect to URL or just navigating to other screen

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV3

Teams:&nbsp;trueBlueClient Runtime
#### 🕐 Timestamps
Started At:&nbsp;trueBlueJuly 1  3:49 PM WEST

Mitigated At:&nbsp;trueYellowJuly 10  3:22 PM WEST

Resolved At:&nbsp;trueGreenJuly 26 11:43 AM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/651-mismatched-anonymous-define-module-trying-to-redirect-to-url-or-just-navigating-to-other-screen)
[Jira issue](https://outsystemsrd.atlassian.net/browse/RDINC-26151)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3024149)

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

Pedro Quintas
#### Summary
&lt;hr&gt;
&lt;p class=&quot;redcarpet&quot;&gt;&lt;strong&gt;ISSUE DESCRIPTION AND HOW TO REPRODUCE&lt;/strong&gt;&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Errors &lt;code&gt;Mismatched anonymous define() module&lt;/code&gt; when trying to navigate away from a page that contains blocks that load third-party scripts.&lt;/li&gt;
&lt;li&gt;Can be reproduced here: &lt;a target=&quot;_blank&quot; href=&quot;https://gs-sandbox-ga-eu-01-dev.outsystems.app/CLICKDOCPrototype/&quot;&gt;https://gs-sandbox-ga-eu-01-dev.outsystems.app/CLICKDOCPrototype/&lt;/a&gt;&lt;ul&gt;
&lt;li&gt;Simply click the &lt;strong&gt;FINDEN&lt;/strong&gt; button.&lt;/li&gt;
&lt;/ul&gt;
&lt;/li&gt;
&lt;/ul&gt;
&lt;p class=&quot;redcarpet&quot;&gt;&lt;strong&gt;IMPACT ON THE CUSTOMER&lt;/strong&gt;&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Development;&lt;/li&gt;
&lt;li&gt;There is a workaround - use &lt;code&gt;window.location.href&lt;/code&gt; to redirect to other pages, this does not trigger the errors.&lt;/li&gt;
&lt;li&gt;Not sure how to integrate these third-party scripts without running into conflicts with &lt;strong&gt;RequireJS&lt;/strong&gt;.&lt;/li&gt;
&lt;/ul&gt;
&lt;p class=&quot;redcarpet&quot;&gt;&lt;strong&gt;TROUBLESHOOTING STEPS &amp; WORKAROUND&lt;/strong&gt;&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;By debugging the code when the exception is thrown, I was able to find three instances of &lt;code&gt;define()&lt;/code&gt; on three separate files (1 file is part of &lt;strong&gt;Resources&lt;/strong&gt;, 2 files are externally located on other websites);&lt;/li&gt;
&lt;li&gt;Note also that all of these references belong to a library &lt;strong&gt;SDK Wrapper&lt;/strong&gt;, not to the main app itself:&lt;ul&gt;
&lt;li&gt;Starting with the local file, found in one of the scripts loaded in Resources - &lt;code&gt;pako.min.js&lt;/code&gt;:
&lt;img width=&quot;100%&quot; src=&quot;https://supportoutsystems.zendesk.com/attachments/token/E7rsgDgz3bfeqxADLOtwABCbF/?name=image.png&quot;&gt;
&lt;/li&gt;
&lt;li&gt;Removed this script by commenting the line where it is referenced in &lt;code&gt;clickdoc-sdk-js-index.esm.js&lt;/code&gt;:
&lt;img width=&quot;100%&quot; src=&quot;https://supportoutsystems.zendesk.com/attachments/token/oiyyec4wIxSieaq5iobgQZdmz/?name=image.png&quot;&gt;
&lt;/li&gt;
&lt;li&gt;Now for the external files, found via debugging:&lt;/li&gt;
&lt;li&gt;
&lt;code&gt;papaparse.min.js&lt;/code&gt;:
&lt;img width=&quot;100%&quot; src=&quot;https://supportoutsystems.zendesk.com/attachments/token/DDZKFbKVIZrncNYMdMzxxGmaC/?name=image.png&quot;&gt;
&lt;img width=&quot;100%&quot; src=&quot;https://supportoutsystems.zendesk.com/attachments/token/Ruz6t3Jfy5raBl5a7TdeI7EtI/?name=image.png&quot;&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;code&gt;tv4.min.js&lt;/code&gt;:
&lt;img width=&quot;100%&quot; src=&quot;https://supportoutsystems.zendesk.com/attachments/token/TW8MH8JheDrQaJ2RziL3PqZDN/?name=image.png&quot;&gt;
&lt;img width=&quot;100%&quot; src=&quot;https://supportoutsystems.zendesk.com/attachments/token/ehwTUwf2sSGLxtZizA3weYsAN/?name=image.png&quot;&gt;
&lt;/li&gt;
&lt;li&gt;Removed the two above by commenting the &lt;strong&gt;OnInitialize&lt;/strong&gt; JS node of the &lt;strong&gt;CGM_SDK&lt;/strong&gt; block (&lt;strong&gt;SDK Wrapper&lt;/strong&gt; lib):
&lt;img width=&quot;100%&quot; src=&quot;https://supportoutsystems.zendesk.com/attachments/token/4U4pwUKGPb1Wxhcvnd4UoDxDh/?name=image.png&quot;&gt;
&lt;/li&gt;
&lt;/ul&gt;
&lt;/li&gt;
&lt;li&gt;Finally, got no errors and page redirects successfully.&lt;ul&gt;
&lt;li&gt;However, I'm not sure how to guide customer into using these third-party scripts, how can they integrate it along RequireJS (if at all supported/possible)?&lt;/li&gt;
&lt;/ul&gt;
&lt;/li&gt;
&lt;li&gt;Also, in the end I republished the old version of the app where the errors are reproduced, but feel free to reach out to me if you need access to the Global Support sandbox where this is published.&lt;/li&gt;
&lt;/ul&gt;
&lt;p class=&quot;redcarpet&quot;&gt;&lt;strong&gt;TECH DATA OR ANY OTHER RELEVANT INFO&lt;/strong&gt;
&lt;br&gt;Ring: ga
&lt;br&gt;Tenant Id: 0e21d816-7778-4ee6-998c-1dea3a8eb4be
&lt;br&gt;Tenant Prefix: idg-cgm
&lt;br&gt;Region: eu-central-1&lt;/p&gt;&lt;p class=&quot;redcarpet&quot;&gt;&lt;em&gt;&lt;! do not remove this line, this will be used to the trigger&lt;/em&gt; Technical Support::Send to R&amp;D - ODC &lt;em&gt;#trigger_send_to_r&amp;d_odc !&gt;&lt;/em&gt;&lt;/p&gt;
## 📝 RetrospectiveinfoDetails
**Ring:** ga
**System-wide impact:**&nbsp; 
**Tenant ID:** 0e21d816-7778-4ee6-998c-1dea3a8eb4be
**Tenant Prefix:** idg-cgm
**Routing Error Code:** OS-CLRT
**Product Area:** -
### Impact:
Customers can't use third party scripts that define an anonymous AMD module.
### Investigation and troubleshooting findings:### Resolution:
There was a workaround that was shared with the customer
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
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/651-mismatched-anonymous-define-module-trying-to-redirect-to-url-or-just-navigating-to-other-screen)

**Date**

**Source**

**User**

**Event**
July 1 12:29 PM WESTwebRootly
created an alert via
July 1 12:29 PM WESTwebRootly
Rootly created this incident
July 1 12:29 PM WESTwebRootly
In triage date has been set to July 1 12:29 PM WEST
July 1  3:47 PM WESTwebCarlos XavierSend ZenDesk private comment has been set: Hi Support,  RequireJS does not support dynamically loading an unnamed module by adding it as a script tag. In order for the customer to load a module dynamically with requireJS they must use the \`require\` function. On the scripts that they want to use those libraries, they must do the following:  
\`\`\`  
require(\[&quot;path to the library&quot;\], function (myLibrary) {  
// make use of the library  $resolve(); // if you want the action flow to continue to the next node only after the JavaScript node finishes executing the script  
});  
\`\`\`  The customer can load multiple libraries at the same time:  
\`\`\`  
require(\[&quot;path to the lib1&quot;, &quot;path to the lib1&quot;\], function (lib1, lib2) {  
// make use of lib1 and lib2  $resolve(); // if you want the action flow to continue to the next node only after the JavaScript node finishes executing the script  
});  
\`\`\`  If the script is a Script or Resource in the application/library, its URL must be passed to the JavaScript node as an input parameter. Do not hardcode paths to application/library scripts and resources.  
\`\`\`  
// Parameter mapping on ODC Studio: MyLibPath = Scripts.MyLib.URL  
require(\[$parameters.MyLibPath\], function (MyLib) {  
// make use of MyLib  $resolve(); // if you want the action flow to continue to the next node only after the JavaScript node finishes executing the script  
});  
\`\`\`  This should allow the customer to load the scripts and use them. Let me know if you need further assistance.  Best Regards,  
Carlos XavierJuly 1  3:47 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hi Support,  RequireJS does not support dynamically loading an unnamed module by adding it as a script tag. In order for the customer to load a module dynamically with requireJS they must use the \`require\` function. On the scripts that they want to use those libraries, they must do the following:  
\`\`\`  
require(\[&quot;path to the library&quot;\], function (myLibrary) {  
// make use of the library  $resolve(); // if you want the action flow to continue to the next node only after the JavaScript node finishes executing the script  
});  
\`\`\`  The customer can load multiple libraries at the same time:  
\`\`\`  
require(\[&quot;path to the lib1&quot;, &quot;path to the lib1&quot;\], function (lib1, lib2) {  
// make use of lib1 and lib2  $resolve(); // if you want the action flow to continue to the next node only after the JavaScript node finishes executing the script  
});  
\`\`\`  If the script is a Script or Resource in the application/library, its URL must be passed to the JavaScript node as an input parameter. Do not hardcode paths to application/library scripts and resources.  
\`\`\`  
// Parameter mapping on ODC Studio: MyLibPath = Scripts.MyLib.URL  
require(\[$parameters.MyLibPath\], function (MyLib) {  
// make use of MyLib  $resolve(); // if you want the action flow to continue to the next node only after the JavaScript node finishes executing the script  
});  
\`\`\`  This should allow the customer to load the scripts and use them. Let me know if you need further assistance.  Best Regards,  
Carlos Xavier
July 1  3:47 PM WESTwebRootlySend ZenDesk private comment has been unsetJuly 1  3:47 PM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

July 1  3:49 PM WESTwebCarlos Xavier
Incident has been started
July 1  3:50 PM WESTwebCarlos XavierCarlos Xavier has been assigned as EngineerJuly 1  3:51 PM WESTwebCarlos Xavier
Summary has been changed to 

&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;

&nbsp;&nbsp;
&nbsp;&nbsp;**ISSUE DESCRIPTION AND HOW TO REPRODUCE**&nbsp;&nbsp;

&nbsp;&nbsp;

&nbsp;&nbsp;- Errors `Mismatched anonymous define() module` when trying to navigate away from a page that contains blocks that load third-party scripts.

&nbsp;&nbsp;- Can be reproduced here: [&nbsp;&nbsp;](https://gs-sandbox-ga-eu-01-dev.outsystems.app/CLICKDOCPrototype/)&nbsp;&nbsp;[https://gs-sandbox-ga-eu-01-dev.outsystems.app/CLICKDOCPrototype/](https://gs-sandbox-ga-eu-01-dev.outsystems.app/CLICKDOCPrototype/)&nbsp;&nbsp;
&nbsp;&nbsp;
&nbsp;&nbsp;

- Simply click the **FINDEN** button.

&nbsp;&nbsp;

&nbsp;&nbsp;

&nbsp;&nbsp;**IMPACT ON THE CUSTOMER**&nbsp;&nbsp;

&nbsp;&nbsp;

&nbsp;&nbsp;- Development;

&nbsp;&nbsp;- There is a workaround - use `window.location.href` to redirect to other pages, this does not trigger the errors.

&nbsp;&nbsp;- Not sure how to integrate these third-party scripts without running into conflicts with **RequireJS**.

&nbsp;&nbsp;

&nbsp;&nbsp;
&nbsp;&nbsp;**TROUBLESHOOTING STEPS &amp; WORKAROUND**&nbsp;&nbsp;

&nbsp;&nbsp;

&nbsp;&nbsp;- By debugging the code when the exception is thrown, I was able to find three instances of `define()` on three separate files (1 file is part of **Resources**, 2 files are externally located on other websites);

&nbsp;&nbsp;- Note also that all of these references belong to a library **SDK Wrapper**, not to the main app itself:
&nbsp;&nbsp;
&nbsp;&nbsp;

- Starting with the local file, found in one of the scripts loaded in Resources - `pako.min.js`:

- Removed this script by commenting the line where it is referenced in `clickdoc-sdk-js-index.esm.js`:

- Now for the external files, found via debugging:
- `papaparse.min.js`:

- `tv4.min.js`:

- Removed the two above by commenting the **OnInitialize** JS node of the **CGM_SDK** block (**SDK Wrapper** lib):

- Finally, got no errors and page redirects successfully.
&nbsp;&nbsp;

- However, I'm not sure how to guide customer into using these third-party scripts, how can they integrate it along RequireJS (if at all supported/possible)?

- Also, in the end I republished the old version of the app where the errors are reproduced, but feel free to reach out to me if you need access to the Global Support sandbox where this is published.
&nbsp;&nbsp;
&nbsp;&nbsp;

&nbsp;&nbsp;**TECH DATA OR ANY OTHER RELEVANT INFO**
&nbsp;&nbsp;
Ring: ga

&nbsp;&nbsp;
Tenant Id: 0e21d816-7778-4ee6-998c-1dea3a8eb4be

&nbsp;&nbsp;
Tenant Prefix: idg-cgm

&nbsp;&nbsp;
Region: eu-central-1
&nbsp;&nbsp;
&nbsp;&nbsp;*&lt;! do not remove this line, this will be used to the trigger* Technical Support::Send to R&amp;D - ODC *#trigger_send_to_r&amp;d_odc !&gt;*&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;July 1  3:51 PM WESTwebCarlos XavierImpact has been set: Customers can't use third party scripts that define an anonymous AMD module.July 1  3:59 PM WESTwebCarlos Xavier
Teams has been added: Client Runtime
July 4 11:37 AM WESTwebCarlos XavierSend ZenDesk private comment has been set: Hi Support,  Sorry for the delay, I answered this 3 days ago but only now did I realize the communication did not reach zendesk. I'm resending my previous communication:  Hi Support,  RequireJS does not support dynamically loading an unnamed module by adding it as a script tag. In order for the customer to load a module dynamically with requireJS they must use the \`require\` function. On the scripts that they want to use those libraries, they must do the following:  \`\`\`  
require(\[&quot;path to the library&quot;\], function (myLibrary) {  // make use of the library$resolve(); // if you want the action flow to continue to the next node only after the JavaScript node finishes executing the script  });  
\`\`\`The customer can load multiple libraries at the same time:  \`\`\`  
require(\[&quot;path to the lib1&quot;, &quot;path to the lib1&quot;\], function (lib1, lib2) {  // make use of lib1 and lib2$resolve(); // if you want the action flow to continue to the next node only after the JavaScript node finishes executing the script  });  
\`\`\`If the script is a Script or Resource in the application/library, its URL must be passed to the JavaScript node as an input parameter. Do not hardcode paths to application/library scripts and resources.  \`\`\`  
// Parameter mapping on ODC Studio: MyLibPath = Scripts.MyLib.URL  require(\[$parameters.MyLibPath\], function (MyLib) {  // make use of MyLib$resolve(); // if you want the action flow to continue to the next node only after the JavaScript node finishes executing the script  });  
\`\`\`This should allow the customer to load the scripts and use them. Let me know if you need further assistance.Best regards,  Carlos XavierJuly 4 11:37 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:
Hi Support,  Sorry for the delay, I answered this 3 days ago but only now did I realize the communication did not reach zendesk. I'm resending my previous communication:  Hi Support,  RequireJS does not support dynamically loading an unnamed module by adding it as a script tag. In order for the customer to load a module dynamically with requireJS they must use the \`require\` function. On the scripts that they want to use those libraries, they must do the following:  \`\`\`  
require(\[&quot;path to the library&quot;\], function (myLibrary) {  // make use of the library$resolve(); // if you want the action flow to continue to the next node only after the JavaScript node finishes executing the script  });  
\`\`\`The customer can load multiple libraries at the same time:  \`\`\`  
require(\[&quot;path to the lib1&quot;, &quot;path to the lib1&quot;\], function (lib1, lib2) {  // make use of lib1 and lib2$resolve(); // if you want the action flow to continue to the next node only after the JavaScript node finishes executing the script  });  
\`\`\`If the script is a Script or Resource in the application/library, its URL must be passed to the JavaScript node as an input parameter. Do not hardcode paths to application/library scripts and resources.  \`\`\`  
// Parameter mapping on ODC Studio: MyLibPath = Scripts.MyLib.URL  require(\[$parameters.MyLibPath\], function (MyLib) {  // make use of MyLib$resolve(); // if you want the action flow to continue to the next node only after the JavaScript node finishes executing the script  });  
\`\`\`This should allow the customer to load the scripts and use them. Let me know if you need further assistance.Best regards,  Carlos Xavier
July 4 11:37 AM WESTwebRootlySend ZenDesk private comment has been unsetJuly 4 11:37 AM WESTwebRootly
MESSAGE SENT FROM R&amp;D:

July 9 10:43 AM WESTwebPedro QuintasPedro Quintas has been assigned as EngineerJuly 10  3:21 PM WESTwebRita Tinoco
Jira ticket -&gt; https://outsystemsrd.atlassian.net/browse/RDINC-26151We are waiting for confirmation that the workaround worked from Support team. Marking this as Mitigated, while we wait for feedback
July 10  3:22 PM WESTwebRita Tinoco
Incident has been mitigated
July 15  5:05 PM WESTwebRootlyZenDesk Event Type has been set: solvedJuly 15  5:05 PM WESTwebRootly
The Global Support team marked this incident as closed in ZenDesk.
July 26 11:43 AM WESTwebRita Tinoco
Incident has been resolved
July 26 11:43 AM WESTwebRita TinocoResolution has been set: There was a workaround that was shared with the customer