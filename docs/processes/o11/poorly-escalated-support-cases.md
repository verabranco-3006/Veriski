---
title: Poorly escalated support cases
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/1230111701/Poorly+escalated+support+cases
confluence_space: RCP
confluence_page_id: 1230111701
last_synced: 2026-04-09
owner: Process Engineering
---

# Poorly escalated support cases

If your team receives a poorly escalated support case, please give feedback to support about it. The feedback must address the following points:

- 
Number of the incident

- 
Why this shouldn&rsquo;t have reached R&amp;D

For feedback regarding **L3 Support level** the point of contact is **Jo&atilde;o Tavares**
For feedback regarding **L2 Support level **the points of contact are **Diogo Santos**, **Tiago Garcia, S&eacute;rgio Pinho **and **Raoul Nystedt (APAC)**

## How to identify if a support case was poorly escalated or not
- 
If it didn&rsquo;t pass by a L3 Escalation Engineer1,2

1 Special cases
This is a rule that applies to the majority of the product areas. 

However there are some assets like OMAS that don&rsquo;t require this to be true. This also applies to some EAP features. 

Giving feedback to support when the reason of the poorly escalated case is solely the &ldquo;It did not pass by L3&ldquo; should be made by the team, that has full context on how the support of the feature is done.

To give an example of a L1 escalation direct to R&amp;D that can or cannot be considered a poorly escalated case:

- 
**Cannot,** if this is the first time asking for this information. Knowing what versions of .Net are support by the platform is something that we at R&amp;D can answer but probably no one in support can

- 
**Can, **if this information was already shared with support and they failed to check internally that this information was already provided.

The example shared above depict the importance of this feedback being given by the team, that has full context of the feature, and that identifying if the case as poorly escalated should be done case by case.

2 Check if a support case had input from an L3 Escalation Engineer
To check if a support ticket had input from an L3 EE there are some clues you might find in the communications, at Zendesk Support tab

*(Official) Have the number of escalations*

*(Official) Have the &ldquo;Escalating to L3 due to ...&ldquo;. This means the case is with L3 now*

*(Unofficial) Messages like*

- 
No proper troubleshoot was made before the escalation

- 
Didn&rsquo;t troubleshoot or debug a platform oml

- 
Didn&rsquo;t debug javascript code from a mobile or reactive app

- 
Didn&rsquo;t collect platform logs

Example
In this example of an escalation what support didn&rsquo;t mention and also didn&rsquo;t do in the incident, qualifying it as a poorly escalated case:

- 
No mention to the general log about slow extensions and if the authentication.xif is really the one that is taking the time

- 
No extension logs

- 
Since this is a system component the code is available for support to see and to add more logs to profile the methods. In the case it even hints to not knowing how to troubleshoot the extension.

- 
The support engineer didn&rsquo;t check the problem management page

- 
The escalation text is incomprehensible

- 
In these cases think of sharing the feedback with the Escalation Engineer also.