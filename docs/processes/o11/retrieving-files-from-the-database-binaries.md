---
title: Retrieving files from the Database binaries.
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/3701408076/Retrieving+files+from+the+Database+binaries.
confluence_space: RCP
confluence_page_id: 3701408076
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrieving files from the Database binaries.

## Context
Here you will find scripts to help you retrieve files directly from the DB tables. This has been proven useful to retrieve deleted versions of modules or even large solutions in the following cases
R11PT-404ef8955cb-cb21-32a7-b692-01ace42388d6System JIRA and R11PT-422ef8955cb-cb21-32a7-b692-01ace42388d6System JIRA.
## Scripts
First of all, these are PowerShell scripts that you can simply run on your PS command line that are ready to connect to SQL Server databases.

In order to use these scripts you just have to edit the variables for the database connection information ($server, $database, $username, and $password) and the directory where the file will be saved ($dirPath/filePath).

Then edit the other variables depending on the script:

- 
Single Espace Version by EspaceID (edit $espaceID and $espaceVersion)
 

- 
Multiple Espace Versions from a certain date onwards (edit $espaceID and $beginningDate)
 

- 
Solution Download (edit $solutionPackId)