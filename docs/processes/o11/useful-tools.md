---
title: Useful tools
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/3033202708/Useful+tools
confluence_space: RCP
confluence_page_id: 3033202708
last_synced: 2026-04-09
owner: Process Engineering
---

# Useful tools

Here you can find a list of several troubleshooting tools that were proven to be useful while investigating a support case.

**Tool Name**

**Description**

**Support Case**

**Useful for**

**Where to get it**

dotPeek

Standalone tool and decompiler for .NET assemblies. It converts .NET assemblies into equivalent C# code and optionally shows the underlying IL code.

R11PBT-641ef8955cb-cb21-32a7-b692-01ace42388d6System JIRA 

Getting information of a dll file like the version or the underlying IL code.

[https://www.jetbrains.com/decompiler/download/](https://www.jetbrains.com/decompiler/download/) 

klogg

Open source multi-platform GUI application to search through all kinds of text log files using regular expressions.

R11PBT-549ef8955cb-cb21-32a7-b692-01ace42388d6System JIRA 

Opening huge files that cannot be opened with text editors (like CompilerService OSTraces logs).

[https://klogg.filimonov.dev/](https://klogg.filimonov.dev/) 

Log Parser Studio

Front-end utility that features a graphical user interface, report builder and query repository for Microsoft's Log Parser application.

R11PBT-648ef8955cb-cb21-32a7-b692-01ace42388d6System JIRA 

Reading and filtering log files.

Example of query used to filter:
 '11:11:00' and time  30 
order by time]]>- 
Download and install [https://www.microsoft.com/en-us/download/details.aspx?displaylang=en&amp;id=24659](https://www.microsoft.com/en-us/download/details.aspx?displaylang=en&amp;id=24659)  

- 
Download and run [https://techcommunity.microsoft.com/t5/exchange-team-blog/introducing-log-parser-studio/ba-p/601131](https://techcommunity.microsoft.com/t5/exchange-team-blog/introducing-log-parser-studio/ba-p/601131)  (attached at the end of the blog post)

HttpLogBrowser

The tool is able to load&nbsp;web servers&nbsp;log files and display statistics on every values of fields allowing to easily filtering down the log entries with a click.

R11PBT-810ef8955cb-cb21-32a7-b692-01ace42388d6System JIRA 

Reading and filtering log files.

 [https://www.finalanalytics.com/products/httplogbrowser](https://www.finalanalytics.com/products/httplogbrowser)  

You just have to upload the log file and it will show metrics and a more readable table.

Process Explorer

Process Explorer shows you information about which handles and DLLs processes have opened or loaded

R11BRT-612ef8955cb-cb21-32a7-b692-01ace42388d6System JIRA 

Knowing which DLLs are loaded by a process. E.g. to know which DLLs are loaded by an OutSystems application, just isolate that application in an application pool, and check which DLLs are loaded by that application pool.

[https://learn.microsoft.com/en-us/sysinternals/downloads/process-explorer](https://learn.microsoft.com/en-us/sysinternals/downloads/process-explorer)