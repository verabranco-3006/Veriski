---
title: Working with logging
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/3015311529/Working+with+logging
confluence_space: RCP
confluence_page_id: 3015311529
last_synced: 2026-04-09
owner: Process Engineering
---

# Working with logging

Here are a few &ldquo;did you know&rdquo; things that can be useful to you in the future (they were to me):

- 
When you search for &quot;Starting log&quot; in OSTraces and you will find one or more lines saying `***** Starting log *****` 

- 
These lines tell you when the service was (re)started

- 
Following that lines (if the debug level is active) there are a bunch of `Settings:'x' is being accessed from x with value of 'x'` lines. You can use those to know the platform configuration at that moment

- 
If the log file is locked when OS services start, it writes the logs to a temporary log file with a GUID prefix to the configured log file name