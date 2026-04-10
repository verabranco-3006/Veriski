---
title: Memory troubleshooting
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/2968256824/Memory+troubleshooting
confluence_space: RCP
confluence_page_id: 2968256824
last_synced: 2026-04-09
owner: Process Engineering
---

# Memory troubleshooting

# Tools
WinDbg

[Jetbrains dotMemory](https://www.jetbrains.com/dotmemory/) - Needs a DotUltimate license

[.Net Memory Profiler](https://memprofiler.com/) - Needs a license

[DebugDiag2](https://www.microsoft.com/en-us/download/details.aspx?id=103453)

[OutSystems.HeapWalker](https://github.com/OutSystems/OutSystems.HeapWalker)

## Related documentation
Performance and Memory troubleshooting (covers above tools overview) - [https://docs.google.com/presentation/d/1wupykFuaV-jrqqa5WCKzvsZw1Qfi2aL07LFCFHTG23o/edit?usp=sharing](https://docs.google.com/presentation/d/1wupykFuaV-jrqqa5WCKzvsZw1Qfi2aL07LFCFHTG23o/edit?usp=sharing) 

Performance and Memory troubleshooting Recording - [https://outsystems.zoom.us/rec/share/GcxY0A5TdX6AsrYShSYSRl_nyRuj1gFFRDdmP_JD8wmW8ISLv-LOpbol9TuLMt6a.fvLIRNdsG7XnnFgU](https://outsystems.zoom.us/rec/share/GcxY0A5TdX6AsrYShSYSRl_nyRuj1gFFRDdmP_JD8wmW8ISLv-LOpbol9TuLMt6a.fvLIRNdsG7XnnFgU)
## Where to start
DebugDiag2 is probably the best one to start since it gives a report with an overview of the information about memory, threads, and object usage. It won&rsquo;t be very helpful in complex cases but can give some clues to the problems.

Then ideally move on to either dotMemory or .Net Memory Profiler. If no license for them is available try the HeapWalker for insights.

If not possible to find the necessary information, move to WinDbg &hellip; it&rsquo;s the most powerful one, but requires a lot of context on how to interpret the results and knowledge about the available commands.

## What to look for
Here are some tips on what to pay attention to in each of the tools, but depends completely on the particular issue being troubleshot.

### dotMemory
## Support Cases examples
**What's wrong?**

**Issue**

**Main steps to troubleshoot it**

**What did we learn?**

Customer unable to publish solutions.

R11PBT-880ef8955cb-cb21-32a7-b692-01ace42388d6System JIRA 

Analyze the Dynatrace reports, thread and memory dumps where crutial.

Also a [document regarding .Net garbage collection](https://docs.google.com/document/d/1Wt6JIKBJiyDUgokQNhjT9xSFvRW9e2vYYJFKXklLCOc/edit#heading=h.ujtsl151eb68) turned out to be very important for the resolution of this case.

Several steps where made to mitigate the customer&rsquo;s problem:

- 
Make the Controller machine a Pure Controller installation.

- 
Consider reducing the memory of the Pure Controller machine, if possible to keep the amount of CPUs.

- 
Change the GC Mode to server by adding &lt;gcServer enabled=&quot;true&quot; /&gt; in the CompilerService.exe.config inside the &lt;runtime&gt; section. Restart the service after.

By reducing the memory of the server it forces the .Net to garbage collect since it has less memory available.