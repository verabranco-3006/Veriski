---
title: Performance Troubleshooting
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/3236856334/Performance+Troubleshooting
confluence_space: RCP
confluence_page_id: 3236856334
last_synced: 2026-04-09
owner: Process Engineering
---

# Performance Troubleshooting

## Tools
[Perfview](https://github.com/microsoft/perfview)
## Related documentation
Performance troubleshooting (covers above tools overview) - [https://docs.google.com/presentation/d/1wupykFuaV-jrqqa5WCKzvsZw1Qfi2aL07LFCFHTG23o/edit?usp=sharing](https://docs.google.com/presentation/d/1wupykFuaV-jrqqa5WCKzvsZw1Qfi2aL07LFCFHTG23o/edit?usp=sharing)
## Useful things to know
- 
Memory dumps can be useful when troubleshooting these kinds of cases since they can shed light on the root cause of the CPU increase.

## Support cases examples
**What's wrong?**

**Issue**

**Main troubleshooting steps**

**What did we learn?**

High CPU usage after an upgrade

R11PBT-897ef8955cb-cb21-32a7-b692-01ace42388d6System JIRA 

Analyze memory dumps.

Having two different versions in different applications together with the minimum threads configured 

in the machine.config file, exhausted the machine resources since there were always a minimum number 

of threads running, that combined with the fact that the oldest version had thread memory problems, 

caused the issue.