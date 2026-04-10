---
title: Database
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/3021668676/Database
confluence_space: RCP
confluence_page_id: 3021668676
last_synced: 2026-04-09
owner: Process Engineering
---

# Database

## Support cases examples
**What's wrong?**

**Issue**

**Main steps to troubleshoot it**

**What did we learn?**

Customer enabled system versioning on a specific table and couldn't revert it

R11PBT-616ef8955cb-cb21-32a7-b692-01ace42388d6System JIRA

- 
Create a module with an entity and publish - Execute the scripts the customer used in a local machine referring the entity that was created in the module of the previous step - Try to publish the module again to reproduce the issue the customer complained about - Find a way to revert the changes (stack overflow :D) - Publish the module again and see it went well

Customer is experiencing poor performance on Server start, due to it taking a long time validating the License.

R11PBT-615ef8955cb-cb21-32a7-b692-01ace42388d6System JIRA 

Since this is FICO, no easy way to reproduce. We troubleshooted the case based on all the kindly provided information from the customer.

The one thing I learned from troubleshooting this case is, as obvious it might sound, that in the customers environment the network quality can play an important role when it comes to performance, and performance is quite a common topic in Support cases.

This is the only customer we offer support to in Linux stack (though we might offer support to other customer that are still in Linux stack, as a best effort we could do) and so we have this script that we can provide to the customer for them to execute and so we can double-check the customer's environment network quality.
 $LOGFILE
echo "$(date) - I/O Performance Test for $(hostname)" >> $LOGFILE
echo "********************************************************************************" >> $LOGFILE
echo "Measuring network performance between server and database server"
DATABASEHOST=$(cat $OUTSYSTEMS_HOME/server.hsconf | grep "" -f2 | cut -d "> $LOGFILE
​
echo "Sending ping packets to $(hostname) 20 times"
echo $(ping -c 20 $DATABASEHOST) >> $LOGFILE]]>
The script pings the database several times, taking the connection credentials from the config in Platform installation folder, and measures the time the roundtrip took.

However, this only works in Linux stack, so a good idea could be coming up with something we could use in Windows.

Customer is not able to establish a connection to a MySQL external database

R11PBT-873ef8955cb-cb21-32a7-b692-01ace42388d6System JIRA 

Ask for the MySQL version and verify if it&rsquo;s a supported one.

Systems requirements can be found [here](https://success.outsystems.com/Documentation/11/Setup_and_maintain_your_OutSystems_infrastructure/Setting_Up_OutSystems/OutSystems_system_requirements#mysql-database).