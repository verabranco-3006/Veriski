---
title: How to deal with rejected Security Vulnerabilities?
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/5036639914/How+to+deal+with+rejected+Security+Vulnerabilities
confluence_space: RKB
confluence_page_id: 5036639914
last_synced: 2026-04-09
owner: Process Engineering
---

# How to deal with rejected Security Vulnerabilities?

When creating a new ODC Problem Record (ODC RPM) that is a potential Security Vulnerability, a new issue is created in the VUL Jira project, waiting to be analyzed by the PSIRT (Product Security Incident Response Team).

After this analysis, the team may consider that it is not a Security Vulnerability and therefore rejects the vulnerability (move the VUL Jira issue to *Rejected*). When that happens, the corresponding RPM will be automatically moved to *Closed *status, with &ldquo;Status Reason List*&rdquo; = Rejected*. The &ldquo;Justify status decision*&rdquo; *RPM field, that is mandatory in this transition, will be filled with the same information written in the VUL &ldquo;Reason not to be considered a vulnerability&rdquo; field.

Note that although the Problem is not actually a Security Vulnerability, R&amp;D may need to fix something related to the detected issue. If this is the case, the **RPM Jira issue can be reopened, and the &ldquo;*****Is it a Security Vulnerability?*****&ldquo; field updated to &ldquo;*****No*****&rdquo;**. In this case, the Support team will be notified about it.