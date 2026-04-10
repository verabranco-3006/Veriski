---
title: Resource Index
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/2676818171/Resource+Index
confluence_space: RCP
confluence_page_id: 2676818171
last_synced: 2026-04-09
owner: Process Engineering
---

# Resource Index

The purpose of this document is to gather and classify the different resources and information that can be provided by the **customer **when an SRE team member is dealing with a support case.

These resources, such as log files, reports, config files, are often the starting point for investigating the cases and can be crucial to resolving them. To avoid ping pong communications, the most effective way is to ask for all of them as soon as the case arrives.

The resources needed to investigate the issue can vary depending on the case, but the list provided here is a base from which to start.
## Always Ask Fornote
- 
**GeneralLogs [xlsx]**

- 
Available on: ServiceCenter &rarr; Monitoring &rarr; General &rarr; Export to excel

- 
**ErrorLogs [xlsx]**

- 
Available on: ServiceCenter &rarr;  Monitoring &rarr; Errors &rarr; Export to excel

- 
**Event Viewer logs Application [evtx]**

- 
Available on: Event Viewer &rarr;  Windows logs &rarr; Application &rarr; Save All Event As

- 
**Event Viewer logs System [evtx]**

- 
Available on: Event Viewer &rarr;  Windows logs &rarr; System &rarr; Save All Event As

- 
**Content of OSSYS_PARAMETER database table [xlsx]**

- 
Available on: ServiceCenter &rarr; Administration &rarr; Environment Configuration &rarr; Export Configuration for&nbsp;OutSystems&nbsp;Support

- 
**GeneralLogs [xlsx]**

- 
Available on: ServiceCenter &rarr; Monitoring &rarr; General &rarr; Export to excel

- 
**ErrorLogs [xlsx]**

- 
Available on: ServiceCenter &rarr;  Monitoring &rarr; Errors &rarr; Export to excel

- 
**Event Viewer logs Application [evtx]**

- 
Available on: Event Viewer &rarr;  Windows logs &rarr; Application &rarr; Save All Event As

- 
**Event Viewer logs System [evtx]**

- 
Available on: Event Viewer &rarr;  Windows logs &rarr; System &rarr; Save All Event As

- 
**Content of OSSYS_PARAMETER database table [xlsx]**

- 
Available on: ServiceCenter &rarr; Administration &rarr; Environment Configuration &rarr; Export Configuration for&nbsp;OutSystems&nbsp;Support

## Product AreasPublish
- 
**Publish Report on Service Center** [pdf]

- 
Available on: ServiceCenter publish result window -&gt; print as pdf

- 
**Compiler **issues:

- 
**CompilerService logs (**[OSTraces](https://success.outsystems.com/Support/Enterprise_Customers/Troubleshooting/Change_OutSystems_Platform_logging_levels_(OSTrace))**) **[log]

- 
Located at: %SystemDrive%\Windows\Temp\CompilerService.log by default

- 
**Thread dump of OutSystems Deployment Controller Service (CompilerService.exe)** [log]

- 
For performance issues request memory dump (requires specific flag)

- 
For concurrency issues regular thread dump is enough

- 
**CompilerService.exe.config **[config]

- 
Located at: %PlatformServerDirectory%\CompilerService.exe.config or, since PS 11.25.0, %PlatformServerDirectory%\CompilerService\CompilerService.exe.config

- 
**Deploy **issues:

- 
**DeployService logs (**[OSTraces](https://success.outsystems.com/Support/Enterprise_Customers/Troubleshooting/Change_OutSystems_Platform_logging_levels_(OSTrace))**)** [log]

- 
Located at:&nbsp;%SystemDrive%\Windows\Temp\DeployService.log by default

- 
**Thread dump of OutSystems Deployment Service (DeployService.exe)** [log]

- 
For performance issues request memory dump (requires specific flag)

- 
For concurrency issues regular thread dump is enough

- 
**DeployService.exe.config** [config]

- 
Located at: %PlatformServerDirectory%\DeployService.exe.config or, since PS 11.24.0, %PlatformServerDirectory%\DeployService\DeployService.exe.config

- 
**applicationHost.config** [config]

- 
Located at: %WinDir%\System32\inetsrv\config

- 
**IIS logs **[log]

- 
Located at: %SystemDrive%\inetpub\logs\LogFiles by default

- 
How to collect and analyze IIS Access logs 

- 
**machine.config** [config]

- 
Located at: %WinDir%\Microsoft.NET\Framework64\v4.0.30319\Config

- 
**General Performance:**

- 
Enable DebugPerfShowUI site property of Service Center before testing publish

- 
Error, General, and Integration logs unfiltered for the day of the publish [log]

- 
Module/solution published [oml or osp]

Timer/Scheduler
- 
**Scheduler logs (**[OSTraces](https://success.outsystems.com/Support/Enterprise_Customers/Troubleshooting/Change_OutSystems_Platform_logging_levels_(OSTrace))**)** [log]

- 
Located at:&nbsp; %SystemDrive%\Windows\Temp\Scheduler.log by default

- 
**Thread dump of OutSystems Scheduler Service (Scheduler.exe)** [log]

- 
For performance issues request memory dump (requires specific flag)

- 
For concurrency issues, regular thread dump is enough

- 
**Scheduler.exe.config** [config]

- 
Located at: %PlatformServerDirectory%\Scheduler.exe.config or, since PS 11.11.1, %PlatformServerDirectory%\Scheduler\Scheduler.exe.config

- 
**TimerLogs (CyclicJobLogs)** [xlsx]

- 
Available on: ServiceCenter -&gt; Monitoring -&gt; Timers -&gt; Export to excel

BPT
- 
**Content of the following database tables**:

- 
The definition of each process (**OSSYS_BPM_Process_definition**)

- 
The definition of each activity in the process (**OSSYS_BPM_Activity_Definition**)

- 
The event queue (**OSSYS_BPM_Event_Queue**)

- 
The light BPT queue (**OSSYS_BPM_Event**)

- 
The relevant process information, filtered (**OSSYS_BPM_Process**)

- 
The relevant activities information, filtered (**OSSYS_BPM_Activity**)

- 
Count&rsquo;s of all the above tables

- 
**Environment health page**:&nbsp;

- 
Available on: ServiceCenter -&gt; Monitoring -&gt; Environment health -&gt; detail of Scheduler service

Configuration Tool
- 
**ConfigurationTool logs** (enabled by default) [log]

- 
Located at:&nbsp;%SystemDrive%\Windows\Temp\ConfigurationTool.log by default

- 
**ConfigurationTool.exe.config** [config]

- 
Located at: %PlatformServerDirectory%\ConfigurationTool.exe.config

- 
**server.hsconf **[config]

- 
Located at: %PlatformServerDirectory%\server.hsconf

Runtime
- 
***running *****folder of the application** [folder]

- 
Located at: %PlatformServerDirectory%\running\%moduleFolderName%

- 
***share *****folder of the application** [folder]&nbsp;

- 
Located at: %PlatformServerDirectory%\share\%moduleName%

- 
**On browser interaction issues: **network communication export [har]

- 
Firefox: 

- 
1. Web Developer Tools &rarr; Network tab

- 
2. Click on cogwheel &rarr; Save all as HAR

- 
Chrome:

- 
1. Developer Tools &rarr; Network tab

- 
2. Right-click on the panel with the requests &rarr; Save all as HAR with content

- 
**On performance issues:** multiple thread dump of application pool [txt]

- 
**On pool stuck/crash issues:** full memory dump of application pool [dmp]

Database
- 
**GeneralLogs **(for slow query reports) [xlsx]

- 
Available on: ServiceCenter &rarr; Monitoring &rarr; General &rarr; Export to excel

- 
**Performance Counters of the DB machine** [blg]

- 
Collect: Powershell script that collects data based on Performance Counter value 

- 
Extra counters activation:Logging Performance Counters 

- 
OSThreadDump: How to use the &quot;OSThreadDump&quot; tool 

- 
**Content of related OutSystems tables** [xlsx]

- 
**Oracle Reports**

- 
Applies to: Oracle DB performance issues

- 
Available on: Ask DBAs

- 
**Information from AWS CloudWatch** (it has details on what queries were active and consuming resources)

- 
**Database version** (specially important to access if the customer is using a not supported database)

Installer/Services
- 
**Event Viewer logs Application** [evtx]

- 
Available on: Event Viewer &rarr; Windows logs &rarr; Application &rarr; Save All Event As

- 
**Event Viewer logs System** [evtx]

- 
Available on: Event Viewer &rarr; Windows logs &rarr; System &rarr; Save All Event As

- 
**Installer logs** [log]

- 
All files located at: %LOCALAPPDATA%\OutSystems\PlatformInstaller

- 
**SAML**

- 
Please use the button &quot;**Export all SAML configurations**&quot; that can be found in Users, inside tab SAML Message Logs.
When you click this button one **zip file will be created and exported, please attach this zip file to the case**.
The zip file will contain several files, namely:

- 
1 file with SAML message Logs

- 
1 file with all SAML configurations (in Users - SP Issuer, SLO/SSO Urls, NameID format)

- 
1 file with Reactive and Traditional Timeout values

- 
**server.hsconf **[config]

- 
Located at: %PlatformServerDirectory%\server.hsconf

Caching
- 
**RabbitMQ logs [log]**

- 
All logs are under %ALLUSERSPROFILE%\RabbitMQ\log

- 
**Environment variables** [xlsx]

- 
`ERLANG_HOME`

- 
`RABBITMQ_NODE_PORT`

Lifetime
- 
**Infrastructure Report**

- 
Go to `https://&lt;LifeTime_server&gt;/lifetime/troubleshoot.aspx`.

- 
Click the link **Download Infrastructure report** to save the file.

- 
**Staging Report**

- 
Access the page `https://&lt;LifeTime_server&gt;/lifetime/troubleshoot.aspx` to see the **Deployment/Staging** list.

- 
In the Stagings list, identify the staging you need to troubleshoot. You can filter by the staging date or environments.

- 
In the row of the identified staging, click the link **Download staging report** to save the file.

- 
**Users Permission Report**

- 
Go to `https://&lt;LifeTime_server&gt;/lifetime/troubleshoot.aspx`.

- 
Click the link **Download the user permissions report** to save the file.

Integration Studio- 
Open the folder: `%AppData%\OutSystems\Integration Studio` .
Alternatively, you can use `C:\Users\&lt;user_name&gt;\AppData\Roaming\OutSystems\Integration Studio` (please replace the tag &lt;user_name&gt;).

- 
Copy the `Log.txt` file and send it to us.

Platform Server logs
**Logs are not visible in console (Service Center)**

- 
Confirm fluentbit is running properly

- 
Since the fluentbit configuration files contain sensitive information, they shouldn&rsquo;t be uploaded to Zendesk/Jira - therefore, it is best to ask support to troubleshoot directly with the client
How to troubleshoot issues related to the PlatformServer logs 

- 
Integration logs relative to the timeframe where the problem is occurring

**Logs are not reaching the APM tool**

- 
Check if the logs are visible in Service Center
*If they are, the issue probably falls under the scope of the Data Platform team*

**Empty Analytics Reports**

- 
`Service Center &gt; Analytics &gt; Daily History` showing when the problem started occurring

- 
Content of the `OSSYS_CENTLOGREPORTREQ` database table

**Integration logs - REST APIs**

- 
Integration logs generated with `Full` logging level for the API(s) in question.
To obtain them, perform the following steps:

- 
In Service Center, access the page for modules that consume OR expose the API with issues

- 
Under the sections &ldquo;Exposed REST APIs&rdquo; or &ldquo;Consumed REST APIs&rdquo;, open the API&rsquo;s configuration page

- 
Change the logging level to `Full`

- 
Force a repeat of the call(s) causing issues, so that more detailed logs are generated

- 
Export/collect the logs as would be done normally

## General MetricsPerformance
- 
**Database information**

- 
CPU

- 
IOPS

- 
Memory&nbsp;

- 
**Front ends information**

- 
CPU

- 
IOPS

- 
Memory&nbsp;

- 
**Latency between the servers and the database** 

- 
ping &lt;database&gt; 

- 
traceroute &lt;database&gt;

- 
**Performance Counters of the PS machine** [blg]

- 
Collect: Powershell script that collects data based on Performance Counter value 

- 
Extra counters activation:Logging Performance Counters 

- 
OSThreadDump: How to use the &quot;OSThreadDump&quot; tool 

- 
**IIS logs **[log] (If related to Application Requests)

- 
Located at: %SystemDrive%\inetpub\logs\LogFiles by default

- 
How to collect and analyze IIS Access logs 

- 
**IntegrationsLogs **[xlsx]

- 
Available on: ServiceCenter &rarr; Monitoring &rarr; Integrations &rarr; Export to excel

- 
**ExtensionLogs **[xlsx]

- 
Available on: ServiceCenter &rarr; Monitoring &rarr; Extensions &rarr; Export to excel

- 
**MobileRequestLogs **(Screen Requests Logs) [xlsx]

- 
Available on: ServiceCenter &rarr; Monitoring &rarr; Screen Requests &rarr; Export to excel

- 
**ScreenLogs **(Traditional Web Requests Logs) [xlsx]

- 
Available on: ServiceCenter &rarr; Monitoring &rarr; Traditional Web Requests &rarr; Export to excel

- 
**Customer infrastructure with performance issues** (usually due to Anti-Virus, anti-malware, or other scanning and sniffing tools):

- 
Download and run the [https://learn.microsoft.com/en-us/sysinternals/downloads/procmon](https://learn.microsoft.com/en-us/sysinternals/downloads/procmon)

- 
Run the PowerShell script [https://drive.google.com/file/d/1ZU76o_jvUQ49zmuJJe-ZR7Gd8ANpA6Ez/view?usp=drive_link](https://drive.google.com/file/d/1ZU76o_jvUQ49zmuJJe-ZR7Gd8ANpA6Ez/view?usp=drive_link) and wait to finish

- 
If &ldquo;not digitally signed&rdquo; error occurs, execute: `Unblock-File -Path .\IOPerformanceTest.ps1`

- 
On the Process Monitor application, click in &ldquo;Save&rdquo; and save the report

- 
Send the saved report file and the *IoPerformanceTest.log* generated from the PowerShell script

**O10**

- 
**Run *****collect_stats***** **[[1]](https://www.outsystems.com/forums/discussion/12418/how-to-obtain-system-information-in-a-java-environment/)** script to look for having configurations:**

- 
prefs.xml [config]

- 
If it does not exist in the script, it can be located at */etc/.java/.systemPrefs/outsystems/prefs.xml*

- 
All of the .conf .properties and .policy files [config]

- 
These files will also be located at: /etc/outsystems

- 
Server information log [log]

- 
**GC logs [log]**

- 
Garbage Collection analysis. Useful for memory analysis when the server is exhausting its resources. You can use this [tool](https://gceasy.io/).

## Relevant Public Documentation
- 
[https://success.outsystems.com/Support/Enterprise_Customers/Troubleshooting/How_to_get_logs_for_troubleshooting_purposes](https://success.outsystems.com/Support/Enterprise_Customers/Troubleshooting/How_to_get_logs_for_troubleshooting_purposes) 

- 
[https://success.outsystems.com/Support/Enterprise_Customers/Maintenance_and_Operations/Cache_Invalidation_in_OutSystems_11/RabbitMQ_management_and_troubleshooting](https://success.outsystems.com/Support/Enterprise_Customers/Maintenance_and_Operations/Cache_Invalidation_in_OutSystems_11/RabbitMQ_management_and_troubleshooting)