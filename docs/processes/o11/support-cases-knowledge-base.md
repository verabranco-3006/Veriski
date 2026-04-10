---
title: Support Cases Knowledge Base
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/4564025473/Support+Cases+Knowledge+Base
confluence_space: RCP
confluence_page_id: 4564025473
last_synced: 2026-04-09
owner: Process Engineering
---

# Support Cases Knowledge Base

This page serves as a knowledge base of support cases where there is the need to keep track of any special context for a given customer. The goal is to keep the information on a centralized place, so anyone picking up a support case of the same customer in the future may have the background context at hand.
It&rsquo;s organized by AC, in the format *&ldquo;Customer Name (Activation Code)&rdquo;* and inside each customer the latest updates are placed at the top, identified with the date of the update contents.

Santander Totta SA (8RV.WLK.3CO.BL2.IQC.MNO.QJ3.GUT)### 11st Oct 2024#### Support case
R11BRT-1389ef8955cb-cb21-32a7-b692-01ace42388d6System Jira   
#### 
TL;DR
This customer is now on an **unsupported scenario**, because they are using PS 11.30.0 with a **downgraded Oracle driver **(19.14.0).
#### 
Context
After the customer updated their three On-Premises Environments from Platform Server version 11.23 to 11.30, they started to get the `{{Oracle.ManagedDataAccess.Client.OracleException (0x80004005): Connection request timed out at OracleInternal.ConnectionPool.PoolManager}}3.Get` error and the CPU of the frontends went almost at 100%. 
The **customer is using Oracle Exadata** (Oracle Database 19c EE Extreme Perf Release 19.0.0.0.0 - Production Version 19.22.0.0.0 running on an Oracle Exadata X9), which seems to use two DB nodes behind some sort of load balancer.
They tested the following scenarios to isolate the problem
- 
PS 11.30 + Oracle driver 19.23.0 + multiple nodes in Exadata DB = problems

- 
PS 11.30 + Oracle driver 19.23.0 + single node in Exadata DB = no problem

- 
PS 11.30 + Oracle driver 19.14.0 (with security vulnerability) + multiple nodes in Exadata DB = no problems

For reference:

- 
PS 11.23 ships with Oracle.ManagedDataAccess 19.14.0;

- 
PS 11.25 ships with Oracle.ManagedDataAccess 19.21.0;

- 
PS 11.30 ships with Oracle.ManagedDataAccess 19.23.0.

The driver downgrade was only intended to be a test to isolate the root cause, but despite our warnings in several messages (example [here](https://outsystemsrd.atlassian.net/browse/R11BRT-1389?focusedCommentId=1192934)) they decided to remain on scenario 3, which is not supported and has known security vulnerabilities.
#### 
Other important comments
Shift report:** **[https://outsystemsrd.atlassian.net/browse/R11BRT-1389?focusedCommentId=1194381](https://outsystemsrd.atlassian.net/browse/R11BRT-1389?focusedCommentId=1194381) 

Last communication from R&amp;D: [https://outsystemsrd.atlassian.net/browse/R11BRT-1389?focusedCommentId=1196655](https://outsystemsrd.atlassian.net/browse/R11BRT-1389?focusedCommentId=1196655)