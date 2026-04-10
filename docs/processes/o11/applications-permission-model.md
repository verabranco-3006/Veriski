---
title: Applications permission model
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/3018326225/Applications+permission+model
confluence_space: RCP
confluence_page_id: 3018326225
last_synced: 2026-04-09
owner: Process Engineering
---

# Applications permission model

Here are a few &ldquo;did you know&rdquo; things that can be useful to you in the future (they were to me):
## Espaces
- 
There is a legacy mode for permissions validation that changes how epaces interactions are allowed/disallowed. The legacy is true or false depending if there is a LifeTime instance connected to the environment or not

- 
Using legacy mode we check user espaces &ldquo;general&rdquo; configuration and granted security level for the current module, and which is higher is the security level used.

- 
If not using legacy mode, we use use applications &ldquo;general&rdquo; configuration and granted security level for the application of the current module, and the more specific permission configuration is used.

- 
The code that fetches user permissions is in `AuthorizationGrantsBuilder.cs`