---
title: FAQ Troubleshooting Solution Publish
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/4546855114/FAQ+Troubleshooting+Solution+Publish
confluence_space: RCP
confluence_page_id: 4546855114
last_synced: 2026-04-09
owner: Process Engineering
---

# FAQ Troubleshooting Solution Publish

# Table of contents61falseTable of contentsnonelisttrue# Frequently Asked Questions## Is the issue related to the Solution Publish C# migration initiative?
Performing the following analysis will help you determining the probability of the issue being related to these specific changes: 
- 
Is the VM2 toggle enabled?
- 
Enabled for all on-prem customers since 11.26.0, enabled for all cloud customers since 11.23.1

- 
When in doubt, this message in General logs will tell you it&rsquo;s running VM2: *Running feature '5e61abe6-94d1-5cd3-88ed-4c627b5c0f83' - 2*
- 
Please note this message will be removed once [R11BRT-1127](https://outsystemsrd.atlassian.net/browse/R11BRT-1127) it&rsquo;s done

- 
Does it happen during one of the affected steps?
- 
Impact Analysis

- 
Preparing Extensions

- 
Preparing Database

- 
Associating Dependencies

- 
Compiling Modules

- 
Compiling Dependencies

- 
Gathering Dependencies

- 
Preparing Deploy

- 
Impact Analysis

- 
Deploying

- 
Does the issue happen specifically in one of the new classes (not in the subsequent Compiler Service methods that also executed for the old publish)?
- 
SolPublishService

- 
SolutionPublication

- 
SolutionPublishOrchestrator 

- 
Was the issue previously identified in [https://outsystemsrd.atlassian.net/wiki/x/-gFX6g](https://outsystemsrd.atlassian.net/wiki/x/-gFX6g)?

- 
Can you still reproduce the issue if you roll back to the old Solution Publish? Can be done by executing the following query **and restarting the Compiler Service afterwards**:
- 
`INSERT INTO OSSYS_FM_FEATURE (NAME,OVERRIDE_VALUE) VALUES ('5e61abe6-94d1-5cd3-88ed-4c627b5c0f83', 0);`

Reference: [https://outsystemsrd.atlassian.net/wiki/spaces/RDO11PC/pages/3738992888/Global+Support+Knowledge+Transfer#Troubleshooting](https://outsystemsrd.atlassian.net/wiki/spaces/RDO11PC/pages/3738992888/Global+Support+Knowledge+Transfer#Troubleshooting).
## Make &ldquo;solution is currently being published&rdquo;/&ldquo;application is currently being published&rdquo; message go away
TL:DR Restart `OutSystems Deployment Controller Service` (aka Compiler Service)

Solution publish locks are managed in memory by Compiler Service. If you end up in the unfortunate situation where your solution gets indefinitely locked and you are certain that it&rsquo;s not being published (for example, it crashed violently) or you just want all the locks gone, you just need to restart the Compiler Service to implicitly release all locks (a new empty in-memory dictionary will be used once the service starts).

Reference: [https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/3188228271/What+is+Solution+Publish+and+what+makes+it+tick#Solution-locks-and-unlocks](https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/3188228271/What+is+Solution+Publish+and+what+makes+it+tick#Solution-locks-and-unlocks) 
## How can I get the publish report URL of previous publications?### If the latest publish report is what you need
You should be able to get into the publish report, with all its output messages, for the last publication of any given solution through Service Center. Just look for the following message, in the Solution edit screen: *Last Solution publish report available. Click here to check.*
### If you want any other publish report
This can be obtained using the `OSSYS_ASYNC_OP_STATE` table, where you&rsquo;ll find a `RETURN_URL` column containing the publish report URL.

Reference: [https://outsystemsrd.atlassian.net/wiki/x/F4CeEgE](https://outsystemsrd.atlassian.net/wiki/x/F4CeEgE) 
## How do I know the state of any given solution publish?
If checking the last publish report mentioned on the previous question is not an option, then you can query the  `OSSYS_SOL_PUB_PLAN` and `OSSYS_SOL_PUB_PLAN_EXT` tables, assuming you have a SolutionPubId.
sql]]>
Reference: [https://outsystemsrd.atlassian.net/wiki/x/F4CeEgE](https://outsystemsrd.atlassian.net/wiki/x/F4CeEgE) 
## Can I inspect the contents of an OSP/OAP file?
Yes, OSP and OAP files are ZIP files. You can just open them, for instance, with 7zip and extract it&rsquo;s contents. There you&rsquo;ll find a Minefest.xml file and all the OML and XIF files bundled with the solution file.

Manifest.xml will tell you things like:

- 
`HubServerVersion`, as the platform version that created the file

- 
Solution `UID` (aka solution `SS_KEY`)

- 
Configured database connections and database catalog names for each module in the source platform

- 
etc

Reference: [https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/3188228271/What+is+Solution+Publish+and+what+makes+it+tick#What-is-a-OSP-file](https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/3188228271/What+is+Solution+Publish+and+what+makes+it+tick#What-is-a-OSP-file) 
## How can I get the timestamp in every message of the publish report?- 
In SC, go to SC&rsquo;s site properties
- 
https://&lt;domain&gt;/ServiceCenter/eSpace_Edit.aspx?EspaceId=1

- 
Set `DebugPerfShowUI` site property to `True` 
- 
**Not **`DebugPerf` - that&rsquo;s a deprecated setting

- 
Following publications should have a timestamp prefix on every message, like this:

### Where&rsquo;s the code responsible for this?
- 
In SC, in `Utils_MessageQueue` server action.

- 
In C#, in [SolutionPublishMessageBroker.cs](https://github.com/OutSystems/Platform/blob/26f34d3302e1eabd7b41d677de4cf1e7f7d073d1/HubServer/Server/Infrastructure/OutSystems.Server.Infrastructure/MessageBrokers/SolutionPublishMessageBroker.cs#L34-L61).   

Reference:

- 
[https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/2676818171/Resource+Index#Product-Areas](https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/2676818171/Resource+Index#Product-Areas) 

- 
[https://outsystemsrd.atlassian.net/wiki/x/kAF9wg](https://outsystemsrd.atlassian.net/wiki/x/kAF9wg)