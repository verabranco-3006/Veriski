---
title: How To Run SQL Queries in Platform DBs
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/3581084337/How+To+Run+SQL+Queries+in+Platform+DBs
confluence_space: RKB
confluence_page_id: 3581084337
last_synced: 2026-04-09
owner: Process Engineering
---

# How To Run SQL Queries in Platform DBs

This document is a tutorial that describes how to run SQL queries against platform DBs associated with each tenant **in the context of a support case, for troubleshooting or remediation**. In this tutorial we will show how to activate the Data API for a particular tenant platform DB and run SQL queries in it through the AWS management console.
# Gaining access to the ring
Firstly, follow this tutorial to get AWS access for the ring where the tenant platform DB you want to run queries against is. For this tutorial we will be accessing ring -3.
# Gaining access to a specific Tenant Platform DB
Go into RDS and pick the tenant platform DB you want, for this example we will be running queries against the `ten-19c31473-c41b-4694-b761-5a96a1e89341` DB.

Once in the dedicated page for the DB, click the *&ldquo;Modify&ldquo;* option in the upper-right corner.

Afterwards scroll-down until you find the *&ldquo;Connectivity&ldquo;* section and tick the *&ldquo;Data API&ldquo;* option and press *&ldquo;Continue&ldquo;*.

On the next screen you&rsquo;ll want to pick the *&ldquo;Apply immediately&rdquo;* option followed by pressing the *&ldquo;Modify cluster&ldquo;* button.

You should receive confirmation at the top of the screen that the DB was successfully modified.

Now before we can start running queries on this DB, we need to go find a credential set we can use to authenticate when connecting to it. we can do this by going to the Secrets Manager and searching for a secret with the following format:

- 
{service}_db_params_t{tenant key without dashes}

For this tutorial I&rsquo;m going to be accessing the DB owned by AVS (Application Versioning Service) and since the tenant I am trying to access is `19c31473-c41b-4694-b761-5a96a1e89341` the secret I am searching for is:

- 
avs_db_params_t19c31473c41b4694b7615a96a1e89341

*NOTE: In-case you can&rsquo;t find an account with this particular name, for whatever reason, you can create one later on when connecting to the DB, although this isn&rsquo;t recommended.*

Once you go into the dedicated page for this secret, **take note of it&rsquo;s ARN value for later use**.

After gathering this data we can finally run queries in the DB, so go back to the dedicated page of the DB you want to run queries against and under the *&ldquo;Actions&ldquo;* dropdown, select the *&ldquo;Query&ldquo;* option.

This&rsquo;ll bring up a pop-up where you&rsquo;ll have to fill some fields:

- 
*Database username*: Here you&rsquo;ll want to select the *&ldquo;Connect with a Secrets Manager ARN&ldquo;* option.

- 
*Secrets manager ARN*: Here you&rsquo;ll want to paste the ARN that you took note of earlier in this tutorial.

- 
*Enter the name of the database*: Here you need to specify which particular database you want to connect to inside of this instance, since for this tutorial I want to run a query for the DB that belongs to AVS, I&rsquo;m setting it as *&ldquo;application_versioning&ldquo;.*

After setting all of this information simply press the *&ldquo;Connect to database&ldquo;* button.

And there you go! Now you should have access to an editor where you can run SQL queries.

**Last but not least, once you are finished with running what you need, don&rsquo;t forget to disable the *****&ldquo;Data API&ldquo;***** option for the DB you just accessed the same way you enabled it.**