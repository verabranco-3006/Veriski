---
title: How to handle and troubleshoot FICO support cases
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/3069182460/How+to+handle+and+troubleshoot+FICO+support+cases
confluence_space: RCP
confluence_page_id: 3069182460
last_synced: 2026-04-09
owner: Process Engineering
---

# How to handle and troubleshoot FICO support cases

Table of contents13false# Ultimate Goal
*Ensure that whoever needs to deal with a FICO support case, from Global Support to R&amp;D, will have a lot of information handy and in an easy to find place.*
# Why?
Fair Isaac Corporation (FICO) is a *special* *customer*, which has acquired extended support for OutSystems 10 in Java until 2027 October 2026. We have created a specific product line for them (do not ignore the contents in that page), based on a very old product version, and not many people have context about it.

Furthermore, FICO runs the OutSystems Platform on Linux, Java, JBoss and Oracle. Many people in the company are not proficient in these technologies, so troubleshooting these support cases becomes harder for such people.

**We want to make that troubleshooting easier and reduce the amount of time it takes to unlock the customer**. Ultimately, we want to reduce the number of FICO support cases escalated to R&amp;D.

This document contains a short history of the [FICO cases we have addressed in the recent past](https://outsystemsrd.atlassian.net/jira/software/c/projects/R11PBT/issues/?jql=issuetype+%3D+%22Support+Case%22+and+labels+IN+%28FICO%29+ORDER+BY+created+ASC) and how they were addressed, as well as tips on how to troubleshoot similar cases.

FICO Background
***FICO is an Independent Software Vendor (ISV) - what does that mean for us?***

As far as OutSystems is concerned, FICO is an [Independent Software Vendor (ISV)](https://blog.hubspot.com/marketing/independent-software-vendor) and they *sell* the OutSystems platform to their own customers. In order to do so, they go through a *white labelling* process, as described below.

**When FICO opens a support case, they are doing so on behalf of their customers.** Let&rsquo;s keep that in mind, because it is very important.

When we ask FICO to get some details from the environment, they need to get them from their customer&rsquo;s environment - this adds significant delays to the process. Furthermore, since the people opening the support case are not the ones facing the issue, everything that is said on a support case needs to go through a chain of people on FICO&rsquo;s side, and these people may or may not have the right skills to understand what we are asking them to do - this increases the potential of a *broken telephone* coming into play.

It is very important that our communication is as clear as possible, with as **many detailed instructions** as we can give them - otherwise, we will just be wasting time on back and forth conversations.

***White labelling - what is it?***

This is the process through which the OutSystems platform and tools get *branded* with FICO&rsquo;s color schema and names. ServiceCenter screens go from red/white to blue/white and ServiceStudio becomes *Application Designer*, for example, among a few other changes.

*Why is this important?*

- 
OutSystems **only** ships vanilla binaries, without any such customizations;

- 
With every platform version, OutSystems ships a set of resources and documents that allow FICO to *white label* the product - they have used this process several times in the past;

- 
These *white labelling* resources are an output of the build process.

What do we know about FICO's installations of the OutSystems Platform? What about their database?
***Automated installations***

As an ISV, FICO relies on automated installations to install the platform for their customers. They have developed a FASt script to do so. This script is **not supported** by us and we only support installations that follow our installation checklist.

*Why is this important?*

We&rsquo;ve had cases in the past where the script caused some file/directory permissions and ownership to be different from what we expect them to be when the installation process follows our installation checklist. This ends up breaking our platform. As an example, consider RPLAT-710ef8955cb-cb21-32a7-b692-01ace42388d6System Jira, which was only solved after several calls with the customer and involving Global Support and R&amp;D, where we had to adjust the permissions and ownership of files and directories one by one.

In some scenarios, their installation script puts the directories under `/opt/outsystems/platform` or `&lt;jboss installation&gt;` in different partitions, which is not supported:

- 
The platform installation directory and everything under it **must be** on the same partition

- 
The JBoss installation directory and everything under it **must be** on the same partition

- 
The platform installation and the JBoss installation **can be** on the same or different partitions

While there is no *good* technical reason that would prevent their multiple partitions scenario from working, it is one that we do not validate. Furthermore, different partitions may have different network latency, which will impact the way the platform works and its performance.

In other scenarios, their script was not updated to deal with the migration from JBoss 6.4 to JBoss 7.x and they had issues installing SSL certificates and claimed that it was our fault - proper SSL configuration is, and always has been, a responsibility of the customer.

***Operating System, JDK, Application Server, Database***

Their installations are either on-premise or in their private cloud. Either way, this is always seen as on-premise for us.

**Their Operating System is Red Hat Enterprise Linux (RHEL).** We currently support RHEL 6 and RHEL 7. We know that RHEL 8 also works, but we haven&rsquo;t released official support for it - RHEL 8 is not officially supported by us at this time.

**Their JDK is OpenJDK 8**, which is supported until May 2026. We intend to add support to OpenJDK 17 at a later stage, but we do not have any concrete plans/dates to do so at the moment.

**Their application server is JBoss EAP.** In the past they used JBoss 6.4 and they have started migrating to JBoss 7.x. Please note that this migration requires setting up new machines, and **in-place upgrades from OutSystems with JBoss 6.4 to OutSystems with JBoss 7.x are not supported.**

**Their database is always Oracle.** In the past it used to be Oracle 12c and they have started migrating to Oracle 19c. Depending on the particular FICO customer that we are talking about, we have learned from previous support cases that their database can be one of the following:

- 
Single Oracle database

- 
AWS Oracle RDS with Multi-AZ

- 
Oracle RAC with multiple nodes (using a `tnsnames.ora` configuration file)

- 
Oracle RAC with multiple nodes (using a `CNAME` record that points to one node at any moment and, when the node fails, points at another node)

- 
Oracle RAC with multiple nodes and an active-active scenario using GoldenGate to synchronize them (as described in [this document](https://drive.google.com/file/d/1Kv4Yra8NOgmJqLZ9x41PM5RczGiBF2oh/view))

- 
It is important to know that this solution was **only validated for a specific platform version**

- 
if FICO hits product problems in different versions on their active-active setup, they must ask for the newer versions to be certified (and they probably need to *pay* our Professional Services to do the new certifications)

- 
It is important to know that this active-active scenario is only supported for FICO

***Auto-scale mechanisms***

Some of FICO&rsquo;s customers may have AWS Autoscale mechanisms in place, which add/remove frontend servers as it detects higher/lower loads. This became evident in RQR-1183ef8955cb-cb21-32a7-b692-01ace42388d6System Jira, but we do not know if this still happens or not. 
What do we need to know about the FICO-specific product line? Where can we find the code and binaries?
Due to the nature of how FICO uses our product, FICO has several versions of the platform server installed on their customers' environments, with 10.0.1005.2 being one of the most common ones. They also have versions 9.1.*. All of those versions are no longer supported and any support case that arrives for them should be addressed by providing workarounds, if any exist.

They have recently (end of 2021, beginning of 2022) started migrating those installations to their official product line (versions 10.0.1050.0-10.0.105x.x so far), and this is the only line that is supported.

***FICO-specific product line***

It is important to understand that **platform server 10.0.1050.0** (and any subsequent version on the [FICO-specific product line](#)) uses the **same code as platform server 10.0.1023.0**, with just the necessary changes to address security vulnerabilities and add support for Oracle 19c and JBoss 7.

Prior to this version, some parts of the platform server Java code would be translated from their counterparts in C#, while other parts of the code would be written directly in Java. **For the FICO-specific product line, all platform server code is written in Java and **[**is available in SVN**](https://srvptsvn.domain.outsystems.com/svn/rd/platform/branches/b10_FICO).

**The majority of the platform code has been stable for a very long time before 10.0.1023.0 and it was not changed for any of the 10.0.105x.x versions.** As an example of what we mean by the code being stable, let&rsquo;s look at the [official release notes for the platform server](https://success.outsystems.com/Support/Release_Notes/10/Platform_Server). Between versions 10.0.1005.2 - one version that is quite common for FICO to use - and 10.0.1023.0 - the version on which the FICO-specific product line is based - we can see that there were only a few bug fixes and a few security vulnerabilities being addressed. **If everything was working properly on 10.0.1005.2, it is very likely that it will still be working just as well in versions 10.0.105x.x. **This is also true for questions related to performance.

If FICO asks us to provide the release notes between 10.0.1005.2 and 10.0.105x.x, we must tell them to read the official release notes from 10.0.1005.2 to 10.0.1023.0, then continue with the release for their specific product line.

***Binaries and release notes for these FICO-specific product line versions***

**All of the FICO-specific versions released so far are General Availability for FICO only.** Since this product line is FICO-specific, we cannot make those binaries public in our [*yum*](http://yum.outsystems.net/10.0/index.html) repository. If we were to make such versions public, they would be available for every customer and not just FICO. Instead, we put the binaries and release notes in [Google Drive](https://drive.google.com/drive/u/0/folders/1gfEt2jnyBaPPV20GCwBewg--YD3nPAIH) and share each version-specific directory with a set of people from FICO.

***Creating test machines with FICO-specific product line versions***

It is not possible to automatically use *RegressionRequester* to ask for such machines. It is also not possible to use *Global Support sandboxes*. The only way to have access to such machines is to use VirtualBox or create EC2 and RDS instances and follow the installation checklist, which is available together with the binaries.

 has developed a set of Bakery scripts that can automate a lot of these tasks, so it is worth chatting with him about the topic first.
# Motivation
Recently we received support cases from FICO that reported similar performance issues which had similar troubleshooting processes. Those cases had one thing in common: FICO was reporting **performance issues after upgrading from 10.0.1005.2 to 10.0.105x.x, going from JBoss 6 to JBoss 7 and from Oracle 12c to Oracle 19c**. We thought that creating a document about those cases would reduce the amount of effort required to answer similar cases in the future.

We also noticed that in past support cases, only a few FICO support cases actually required some degree of product knowledge, but a lot of them required *sysadmin* or/and *DBA* skills.

With that in mind, we decided to create a body of knowledge with the ultimate goal of troubleshooting FICO support cases in an easier way.
# Dealing with FICO support cases
So, you&rsquo;ve received a FICO support case. Now what?

The first thing you need to do is add the FICO label to the *Labels* field in Jira. Doing so will allow us to easily reference them in the future.

Go through this document carefully and check if the symptoms are similar to any of the ones that we have found in the past. If they are, the odds are high that the issue can be addressed in the same way it was addressed before and it is worth trying. If the symptoms aren&rsquo;t similar, they might be close enough that the information in this document still applies.

It is your responsibility to keep this document updated with the findings from future cases. Please add an entry at the bottom of the following section for each new support case that arrives and follow the same approach we did for the past cases we&rsquo;ve already added here. If you develop other troubleshooting mechanisms, please also add them to this document.
## Past support cases and how we addressed them### Intellectual Property (IP) issues
**Support case: **RQR-98ef8955cb-cb21-32a7-b692-01ace42388d6System Jira

**Reported symptoms**

- 
FICO needed to switch the target Activation Code associated with some modules

**Troubleshooting steps**

- 
Open ServiceStudio in debug mode

- 
Make changes

- 
Return changed OMLs to customer

**Additional information**

- 
**This was not a product problem**

- 
This needs to be done directly by R&amp;D, as there are no tools available for the operation

### Environment going down frequently
**Support case: **RQR-160ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Reported symptoms**

- 
Dev2 environment &ldquo;goes down&rdquo; very frequently

- 
In this case, by &ldquo;goes down&rdquo; what they really mean is that publish start to fail and they need to restart services to continue publishing.

**Troubleshooting steps**

- 
Global Support correctly identified threads in a deadlock state

- 
R&amp;D produced a quick-fix version for the issue and backported the fix to the main line of the product

**Additional information**

- 
N/A

### Unable to login to Lifetime as it displays admin does not have role
**Support case: **RQR-706ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Reported symptoms**

- 
After performing a fresh installation of Lifetime in a dedicated Lifetime environment, customer wasn't able to login with the *admin* account

- 
They were getting the error: *admin doesn't have a role*.

**Troubleshooting steps**

- 
Global Support went through the ServiceCenter logs and identified what was causing the problem

- 
Global Support went through the ServiceCenter and LifeTime code, identified why the problem was happening and provided a fix on LifeTimeEngine OML

- 
R&amp;D produced a quick-fix version for the issue and backported the fix to the main line of the product

**Additional information**

- 
N/A

### Security finding - session remains active after user is set inactive in the DB
**Support case: **RQR-792ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Reported symptoms**

- 
User session remains active after the user is set as inactive in the DB

**Troubleshooting steps**

- 
Check the code and identify the frequency at which sessions are removed from the database (10m, not configurable)

- 
After discussing some proposal of solutions with Global Support, R&amp;D implemented an example workaround that the customer could apply to their applications

**Additional information**

- 
**This was not a product problem**, just something they wanted to do differently

### CPU increase during high-load spikes, servers stop responding
**Support case: **RQR-895ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Reported symptoms**

- 
During high load spikes, the CPU usage increases dramatically at the same time that a high number of GC events take place.

- 
From that moment onward, the servers stop responding to requests, which has direct impact on the End-Users experience

**Troubleshooting steps**

- 
Global Support and R&amp;D analysed the thread and heap dumps, understood that it could be a similar issue to something that had been previously reported in RQR-837ef8955cb-cb21-32a7-b692-01ace42388d6System Jira

- 
A Jira issue was created to follow up on the issue as a bug 

**Additional information**

- 
N/A

### Performance issue - slowness in the DB server leading to timeouts on their app
**Support case: **RQR-1096ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Reported symptoms**

- 
They experienced a major slowdown in an application responsible for processing credit

- 
While the app didn't actually crash, the response time for the credit app was timing out and there's was high CPU usage on the DB

**Troubleshooting steps**

- 
Global Support asked for an AWR report and identified that the issue was being caused by queries to the session database

- 
Further investigation allowed Global Support to find a few product bugs

- 
R&amp;D provided a Factory Configuration snippet that addressed part of the issue

- 
A fix was later added to the product

**Additional information**

- 
N/A

### End-Users are experiencing heavy slowness on their applications
**Support case: **RQR-1183ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Reported symptoms**

- 
End-Users are experiencing heavy slowness on their applications

- 
High database CPU usage

- 
OSSYS_PARAMETER was with an unusual size, having more than 150k records

- 
After deleting the unused Front-End records and restarting, the issue stopped occurring

**Troubleshooting steps**

- 
Global Support analyzed logs and checked the AppDynamics metrics and compared outage periods with normal functioning periods

- 
R&amp;D asked for the sessions that were locked

- 
R&amp;D asked for thread-dumps of the servers when the issue was occurring

- 
R&amp;D asked for the screen, general and error logs

- 
Global support asked for STATSPACK

**Additional information**

- 
They had an auto-scale mechanism that adds/removes frontends as needed, which is why there were so many entries in OSSYS_PARAMETER

- 
**This does not seem to be a product problem, just a problem of their setup**

- 
**Case closed without further explanation**

### DB timeout during publish leaves inconsistent data in multi-tenant entities and disabled triggers
**Support case: **RQR-1423ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Reported symptoms**

- 
A DB timeout occurs during publish that changes many rows in the database

- 
There is inconsistent data in multi-tenant entities

- 
Triggers are left disabled

**Troubleshooting steps**

- 
Global Support managed to reproduce the timeout issue

- 
R&amp;D managed to reproduce the &ldquo;triggers left disabled&rdquo; issue

- 
Global Support and R&amp;D identified the workaround of increasing the timeout of update queries in configuration tool, as well as updating the entity in the database and enabling triggers manually

- 
R&amp;D explained why it happened, a fix was added to the product at a later stage

**Additional information**

- 
N/A

### 3 vulnerabilities detected in penetration test
**Support case: **RQR-1721ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Reported symptoms**

- 
Customer detected that their applications were vulnerable to host-header injection, version disclosure and back-button browsing

**Troubleshooting steps**

- 
Global support checked in previous support cases where these vulnerabilities were already addressed and provided the same solution

- 
Global support suggested a configuration using Factory Configuration (changes to web.xml)

- 
Global support reproduced the issue on one of their sandboxes

- 
R&amp;D suggested an approach of changing their application&rsquo;s *OnBeginWebRequest*

**Additional information**

- 
**This did not seem to be a product problem at first, it seemed that FICO was asking for guidance on how to develop their applications**

- 
A fix ended up being developed for one of the vulnerabilities

### 3 in 1: Configuration Tool removed some session tables and they were not recreated after; some queries over BPT tables taking too long; invalid tenant error in JBoss logs 
**Support case: **RQR-1832ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Reported symptoms**

- 
After running configuration tool and answering *Yes* to the question about recreating the session database, some tables were deleted and not recreated afterwards

- 
Some queries over BPT tables taking too long

**Troubleshooting steps**

- 
Global Support correctly split the case into three issues, as they happened at the same time, but were not the same problem

- 
Check the configuration tool code to understand what it does: drop tables, create tables

**Additional information**

- 
We suspect that they had a user with permissions to drop tables but not create them, but this suspicion was never confirmed

- 
**This was not a product problem, just a problem of their setup**

- 
**Case closed without further explanation**

### Customer detected different performance when using *basicfile* and *securefile* for Oracle
**Support case: **RQR-1946ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Reported symptoms**

- 
Customer was seeing different settings in different environments, which was causing differences in performance at time of deletion - wanted to know where we set this

**Troubleshooting steps**

- 
Global Support identified that *securefile* is the default since Oracle 12c

- 
Global Support identified that the platform uses *basicfile*

- 
R&amp;D clarified that *securefile* is the default since Oracle 12c, but it is only supported on Automatic Segment Space Management (ASSM) tablespaces and when Oracle Database 11g compatibility mode turned off

- 
R&amp;D clarified that the platform does not set this attribute and that it is controlled by the Oracle Engine

**Additional information**

- 
**This was not a product problem, just a problem of their setup**

- 
**Case closed without further explanation**

### Customer wanted to know how to upgrade their active-active setup without downtime
**Support case: **RQR-2189ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Reported symptoms**

- 
N/A

**Troubleshooting steps**

- 
Global Support shared documentation for upgrades without downtime

- 
R&amp;D validated that the proposed upgrade process would work, suggested some changes where applicable

**Additional information**

- 
**This was not a product problem, just them asking for instructions on how to do that operation in their active-active setup**

- 
This active-active setup was a one-off project that our Professional Services sold them, we&rsquo;ve had several cases because of this setup

- 
**Case closed without further explanation**

### Customer wanted us to adapt our Okta connector, but they were using somebody else&rsquo;s
**Support case: **RLIT-3561ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Reported symptoms**

- 
Customer reported that Okta would be ending support and provisioning capabilities for OutSystems

- 
Customer wanted us to adapt our connector

**Troubleshooting steps**

- 
Tell customer to use the appropriate mechanism

**Additional information**

- 
**This was not a product problem,** customer was using an unsupported component that happened to be called Outsystems (yes, with a lowercase s), but it was not created by us

- 
**Case closed without further explanation**

### Security scan detected some vulnerabilities in some of the 3rd-party libraries shipped with the platform
**Support case: **RPLAT-225ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Reported symptoms**

- 
Their security scan detected vulnerabilities in 3rd party libraries that we ship with the platform

**Troubleshooting steps**

- 
Upgrade the libraries

- 
Produce new binaries, validate, release

**Additional information**

- 
The list was just too long for us to understand if the vulnerabilities impacted the platform or not

- 
It was *easier* to upgrade the existing libraries, but we could not go to the latest versions due to the amount of changes this would account for

### Deployment Controller not starting after upgrading JBoss from 6.4.16 to 6.4.23
**Support case: **RPLAT-234ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Reported symptoms**

- 
Customer reported that Deployment Controller stopped working after they updated JBoss version

- 
Error logs were showing `java.lang.NoClassDefFoundError` exceptions

**Troubleshooting steps**

- 
Global Support and customer came up with a workaround of copying some jars to platform libs folder

- 
That workaround was consider problematic by R&amp;D, as it would cause jar hell

- 
R&amp;D suggested a clean installation of JBoss 6.4.23, instead of an upgrade - to rule out file permissions and any side effects from FICO trying to fix the issue on their own by copying *random *files to platform folders

**Additional information**

- 
Under normal circumstances doing a similar *minor* upgrade, should never cause any OutSystems service to stop working

- 
Customer was using an unsupported Operating System version

- 
**This was not a product problem,** it was likely a side effect of the way they upgraded the JBoss server (and potential subsequent operations that they did not tell us about)

- 
**Case closed without further explanation**

### Security scan detected some vulnerabilities in some of the 3rd-party libraries shipped with the platform
**Support case: **RPLAT-474ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Reported symptoms**

- 
Their security scan detected vulnerabilities in 3rd party libraries that we ship with the platform

**Troubleshooting steps**

- 
Upgrade the libraries

- 
Produce new binaries, validate, release

**Additional information**

- 
It was not clear how these vulnerabilities would affect the platform, or even if they would affect the platform and customer applications, but we upgraded the libraries nonetheless

### Production environment in active-active setup was down after license errors
**Support case: **RPLAT-557ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Reported symptoms**

- 
One data center was down after some license errors

- 
There were inconsistencies in the database

**Troubleshooting steps**

- 
Understand which operations they were doing and if these operations were following the active-active scenario that we have defined for them

- 
Understand if tables were synchronized between each of the active-active nodes

- 
Provide detailed instructions on how to achieve their objectives

**Additional information**

- 
**This was not a product problem, it was a problem with their active-active setup**

- 
This active-active setup was a one-off project that our Professional Services sold them, we&rsquo;ve had several cases because of this setup

### Security scan detected some vulnerabilities in some of the 3rd-party libraries shipped with the platform
**Support case: **RPLAT-626ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Reported symptoms**

- 
Their security scan detected vulnerabilities in 3rd party libraries that we ship with the platform

**Troubleshooting steps**

- 
Upgrade the libraries

- 
Clarify that one library had already been updated and that they needed to republish the consumers of an extension in order for it to work

- 
Produce new binaries, validate, release

**Additional information**

- 
It was not clear how these vulnerabilities would affect the platform, or even if they would affect the platform and customer applications, but we upgraded the libraries nonetheless

### Application query taking too long to execute after upgrade
**Support case: **R11PBT-40ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Reported symptoms**

- 
A given application query became much slower than what it was before

- 
This happened after they upgraded to JBoss 7 and Oracle 19c

**Troubleshooting steps**

- 
State that such differences are not expected

- 
Ask for AWR/STATSPACK before and after the upgrade

- 
Look at the query that the customer is complaining about, check their execution plan and amount of records involved

- 
Validate if it makes sense to rebuild indexes or defrag the involved tables

- 
Should have been troubleshooted using one of the generic troubleshooting mechanisms described later in this page

**Additional information**

- 
This is one of those cases where they report that an application query is slower after the upgrade

- 
Given that this is an application query, we must be very clear that they need to involve their DBA on the topic - it is not our responsibility to help them develop performant queries

- 
As we mentioned before, there were no changes to our code that could be seen as the reason for this to happen

- 
**This was not a product problem,** it was likely something on their database that needed tweaking

- 
**Case closed without further explanation**

### Unable to publish Factory Configuration after the upgrade to 10.0.1052.0
**Support case: **R11PBT-43ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Reported symptoms**

- 
Publish failing due to some foreign key violation related to zones

**Troubleshooting steps**

- 
Identify the code (in Java, not C# as Global Support did) involved in that foreign key

- 
Check if default zone ID site property in ServiceCenter is empty, if it isn&rsquo;t set it to empty

**Additional information**

- 
N/A

### Question about separating OSSYS_ and OSUSR_ into different servers, with different replication strategies, in their active-active setup
**Support case: **R11PBT-62ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Reported symptoms**

- 
Customer wanted to separate the system and application tables into different servers 

**Troubleshooting steps**

- 
State that this is not supported for O10.

**Additional information**

- 
**This was not a product problem**, just something they wanted to do differently

- 
This active-active setup was a one-off project that our Professional Services sold them, we&rsquo;ve had several cases because of this setup

### Failing to upgrade to 10.0.1052.0 using an (unsupported) in-place installation
**Support case: **RPLAT-710ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Reported symptoms**

- 
Getting `java.lang.NoClassDefFoundError` exceptions while running configuration tool

**Troubleshooting steps**

- 
Validate and fix file and directories permissions

- 
Answer questions regarding why we need a new machine

**Additional information**

- 
**Customer ignored our installation checklist instructions and decided to install JBoss on an existing machine, instead of using a new one**

- 
**This was not a product problem, just a problem of their setup**

- 
**Case closed without further explanation**

### Application query timeout in active-active scenario
**Support case: **R11PBT-110ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Reported symptoms**

- 
Query running on some nodes executes forever, query running on other nodes hits a timeout after 110 seconds

**Troubleshooting steps**

- 
Ensure that the configuration on both environments is the same

- 
Running the same platform server version

- 
Running the same application version

- 
`/etc/.java/.systemPrefs/outsystems/prefs.xml` with the same configurations regarding timeouts on both nodes

- 
Ensure that database characteristics (specs) are the same

- 
Check if they have any custom timeouts in code/extensions

- 
Check that the execution plan is the same on both nodes

- 
Should have been troubleshooted using one of the generic troubleshooting mechanisms described later in this page

- 
This would have removed the platform from the equation sooner

- 
Ask the customer to engage with Oracle directly

**Additional information**

- 
This active-active setup was a one-off project that our Professional Services sold them, we&rsquo;ve had several cases because of this setup

- 
This is one of those cases where they report that an application query is slower 

- 
Given that this is an application query, we must be very clear that they need to involve their DBA on the topic - it is not our responsibility to help them develop performant queries

- 
As we mentioned before, there were no changes to our code that could be seen as the reason for this to happen

- 
**This was not a product problem,** it was likely something on their database that needed tweaking

- 
**Case closed without further explanation**

### Customer asking for a quick-fix for a low priority security vulnerability
**Support case: **R11CT-148ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Reported symptoms**

- 
N/A

**Troubleshooting steps**

- 
Produce quick-fix, validate, deliver

**Additional information**

- 
**Customer refused to upgrade to a more recent platform server version, where several urgent/high priority vulnerabilities, as well as the low priority one, had been addressed**

### Customer asking for the binaries for a specific version in their product line
**Support case: **R11PBT-146ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Reported symptoms**

- 
N/A

**Troubleshooting steps**

- 
Ask them for a list of FICO email addresses to which we should share the binaries

- 
Share the [directory with the requested version](https://drive.google.com/drive/u/0/folders/1gfEt2jnyBaPPV20GCwBewg--YD3nPAIH) in Google Drive with those addresses, set them as viewers

- 
Do not share the top-level directory with all versions!

**Additional information**

- 
N/A

### Publish and deploy operations taking too long
**Support case: **R11PBT-150ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Reported symptoms**

- 
Publishing a solution takes a lot of time, is much faster on their lab

**Troubleshooting steps**

- 
Check the collect_stats, and namely the GC dumps, to understand if there is any memory issue

- 
Go through the deployment controller logs and its code and check what the platform server is doing

- 
From the log messages, we should be able to understand which queries/operations are being performed by the platform

- 
From the timestamps of the log messages, we should be able to get an approximate measure of the time such operations are taking

- 
Once we identify some specific queries/operations and are able to understand the time they are taking, we should try to move this to one of the generic troubleshooting mechanisms described later in this page

**Additional information**

- 
**This was a long-running case for a platform version (9.1) that was no longer supported**

- 
After a massive 1 year of back and forth following extensive and diverse troubleshooting paths, we **did not find any evidence that this was a product problem**, and all of the evidence that we found pointed towards this being a problem with their I/O, network, database or all of them

- 
As an example, we found queries that went from a few seconds in their lab to several minutes in the customer&rsquo;s infrastructure

- 
The customer was very reluctant in sharing the data with us, but they seemed to expect us to solve the issue without said data

- 
Customer kept comparing environments with different characteristics and amounts of data, expecting the results to be the same or similar among them

- 
**Case was closed from R&amp;D side when we had exhausted our troubleshooting capabilities - we could only find *****probable *****evidence that this was an infrastructure issue**

### Customer getting errors on the configuration tool after upgrading to 10.0.1052.0
**Support case: **R11PBT-168ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Reported symptoms**

- 
Errors running configuration tool after upgrading

- 
Error logs were showing `java.lang.NoClassDefFoundError` exceptions

- 
Error logs showing ORACLE exceptions

**Troubleshooting steps**

- 
Ensure they are not doing an upgrade in-place

- 
Validate folder and file permissions and ownership (just as in other cases)

- 
Change the password of the user in the database, then run configuration tool and use the same password

- 
Remove connection string entries from `/etc/.java/.systemPrefs/outsystems/prefs.xml`, and rerun Configuration Tool

**Additional information**

- 
**Customer ignored our installation checklist instructions and decided to install JBoss on an existing machine, instead of using a new one**

- 
**This was not a product problem, just a problem of their setup**

- 
**Case closed without further explanation**

### Questions about running FE and Controllers in different versions after an upgrade and about separating OSSYS_ and OSUSR_ data
**Support case: **R11PBT-171ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Reported symptoms**

- 
N/A

**Troubleshooting steps**

- 
Global Support checked the checklist for version 10.0.1053.0, which was the one the customer was migrating to

- 
R&amp;D recommended the customer to use the latest version available to FICO, since it includes several security fixes

- 
Clarified the customer questions and warn them to the fact the architecture they&rsquo;re thinking of was never validated and/or isn&rsquo;t supported nor recommended by us

**Additional information**

- 
**This was not a product problem**

### Customer asks for hotfix in an older version than the latest one 
**Support case: **R11DT-460ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Reported symptoms**

- 
RPM-1189 was only fixed on version 10.0.1115.0. However, the customer wants to update to PS Version 10.0.1053.1, where the fix isn&rsquo;t available.

**Troubleshooting steps**

- 
It was agreed that we would provide to the customer a fix for the RPM

- 
Produce new binaries, validate, release

**Additional information**

- 
N/A

### Customer requests to grant access of a release to a list of emails
**Support case: **R11PBT-190ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Reported symptoms**

- 
N/A

**Troubleshooting steps**

- 
Access granted

**Additional information**

- 
**This was not a product problem**

### Out of memory errors during JBoss service startup
**Support case: **R11PIT-337ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Reported symptoms**

- 
Out of memory errors during JBoss service startup.

- 
Services taking a long time to start (more than 20 minutes) or not starting at all.

- 
Full CPU and memory usage during these services' startup.

- 
Full Garbage Collection is continuously triggered.

- 
Open file counts keep increasing indefinitely.

**Troubleshooting steps**

- 
Analyzed the memory dump, server log and garbage collector logs

- 
From the GC logs we saw that a lot of GCs happening which means memory is under pressure, and the system wants heap and can't have it

**Additional information**

- 
**This was not a product problem, this is just how JBoss works and there is nothing we can do about it (when it needs more memory we need to configure it to have more memory).**

- 
**Case closed without further explanation**

- 
In hindsight, this case was the same as R11PIT-431ef8955cb-cb21-32a7-b692-01ace42388d6System Jira, which we received some time later, but this specific case actually had useful memory dumps 

### JBoss start time is much higher after upgrade
**Support case: **R11PIT-431ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Reported symptoms**

- 
JBoss startup time is much higher than before (20 min vs 5 min)

**Troubleshooting steps**

- 
Analyzed GC logs, identified they were trying different combinations of flags and validated each of them

- 
Suggested to remove some flags

- 
Asked the customer to enable SWAP, customer denied

- 
Tell the customer that JBoss 7.3 was not supported (it wasn&rsquo;t supported in that version), asked them to use JBoss 7.2 - unfortunately, problem persisted

- 
Analyzed new GC logs and memory dumps

- 
Asked the customer for their factory, ensure that they send the non-ISV protected one

- 
Created a lab to try and reproduce the issue, tweaked some memory parameters to see if it would make things better - identified that it was a JBoss issue

- 
Provided a script that mitigates the problem, by changing the way JBoss starts

- 
Reiterated that the JBoss start time is not platform dependent, it is the time it takes for JBoss to deploy the applications

- 
RedHat provided a patch, test the patch, share the patch with the customer 

**Additional information**

- 
Even though we kept asking them to provide us with memory dumps taken while the issue was happening, all of the memory dumps they sent were captured after the problem - this actually made them useless for us to troubleshoot the issue (and that&rsquo;s why we had to create a lab)

- 
**This was not a product problem, it was a problem with JBoss**

- 
As soon as we identified that this was not a product problem, customer should have opened a case with RedHat, but it had to be OutSystems doing so

- 
RedHat would have picked up the issue much easily than us

- 
Customer kept pushing us towards updates, but these updates could only be provided by RedHat

- 
In hindsight, this case was the same as R11PIT-337ef8955cb-cb21-32a7-b692-01ace42388d6System Jira, but at the time we did not understand it was the same root problem stated differently

### NewDate() built-in function returns wrong dates under certain scenarios
**Support case: **R11PBT-441ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Reported symptoms**

- 
For some dates, the function returns a date with the wrong day

- 
When directly translated to the SQL statement the issue does not occur, the issue only happens in normal logic

**Troubleshooting steps**

- 
Tried in a machine with a time zone that implements Daylight Saving Time (DST) at the 00:00 hours

- 
Use the NewDate for the specific dates when the DST changes - validate that it causes the expected behaviour to happen

**Additional information**

- 
Provided a workaround, but not fixed as this is a non-critical issue with an easy workaround

- 
Fixing this could lead to breaking changes for environments that do not observe the same timezone

### Customer is not able to install Service Center from the controller node using the Configuration tool
**Support case: **R11PIT-474ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Reported symptoms**

- 
Customer gets the following error: Unable to contact Outsystems Deployment Controller Service

- 
When restarting Deployment Controler Service, it shows [Warning] instead of [OK]: Starting OutSystems Deployment Controller Service [WARNING]

**Troubleshooting steps**

- 
Look at the logs

- 
Deployment attempt of ServiceCenter, failed on ping validation

- 
Look at the iptables

- 
There are missing redirect rules

- 
Increase log level of os.deployment.service.properties on the frontend node

- 
Usage of a tool that lists the content of the RMI, to understand if it&rsquo;s working as intended

**Additional information**

- 
**This does not seem to be a product problem, just a problem of their setup**

- 
**Case closed without further explanation**

### Unavailability after an &quot;AWS Multi-AZ RDS Oracle DB Instance Failover event&quot;
**Support case: **R11PBT-470ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Reported symptoms**

- 
Customer had their production application(s) become unavailable for 60-120 minutes, after an &quot;AWS Multi-AZ RDS Oracle DB Instance Failover event&quot;.

**Troubleshooting steps**

- 
Global support could not reproduce the issue since they did not have the respective platform version

- 
The binaries for this and other FICO-specific versions are available in [Google Drive](https://drive.google.com/drive/u/0/folders/1gfEt2jnyBaPPV20GCwBewg--YD3nPAIH)

- 
R&amp;D stated that this was caused by a DB failover, and since there is no automatic way of cleaning the existing established DB connection pool, it will require an application service restart.

- 
This also means that this is not a platform limitation, this is just how Java connections pools work. The Platform does not know when a failover occurs. This means that in fact when a failover event happens, there has to be an application restart. 

- 
Even tough this was not suported, we took the time to try a workaround that the customer found in StackOverflow without success.

**Additional information**

- 
**This was not a product problem.**

### Prod Slowness
**Support case: **R11PBT-478ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Reported symptoms**

- 
Customer is reporting performance issues during their business hours that are affecting some of their servers.

**Troubleshooting steps**

- 
Global Support could not replicate the error.

- 
R&amp;D suggested that the customer either simplifies the logic present in the applications or increases the **OutSystems.HubEdition.RequestTimeout **key value, requests don&rsquo;t take so long and timeout.

- 
If none of these mitigations helped, the customer should scale their environment horizontally.

**Additional information**

- 
**This was not a product problem, since contention is happening at the application server-side, on JBoss.**

- 
**Case closed without further explanation**

### Service Center URL inaccessible for 30-60 mins
**Support case: **R11PBT-522ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Reported symptoms**

- 
The service center got unavailable for ~60 minutes.

**Troubleshooting steps**

- 
Global Support could not replicate the problem.

- 
R&amp;D associated this issue with a similar support case already solved.

- 
Also provided several hypotheses and mitigations for this specific situation, but since the customer didn&rsquo;t reply it was not possible to pinpoint what was the reason why it was happening or if it was fixed with our suggestions. 

**Additional information**

- 
**This was not a product problem.**

- 
**Case closed without further explanation**

### Post controller restart certificate license details taking more time.
**Support case: **R11PBT-615ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Reported symptoms**

- 
The customer is observing a delay in the license being read as &quot;valid&quot; by the platform.

**Troubleshooting steps**

- 
Global Support was not able to replicate the issue.

- 
R&amp;D pinpointed the problem as the retrieval of the OML files binary data taking too much time after a server restart.

- 
R&amp;D analyzed the AWR reports and build an application to test the retrieval times of the OML binary files, they both pointed to a network problem.

- 
Customer kept insisting that it was a product problem even though SQLplus showed that the retrieval of data from the FE server to the Database was taking way too much time.

- 
Global Support agreed with our conclusions and passed on the information to the customer that the problem was on their infrastructure.

- 
R&amp;D ultimately [built a laboratory](https://docs.google.com/document/d/10RNNIuqK5JTPBSS-P9sdJ3IvqY9Pb86QjxARhJGpTTQ/edit) with both 10.0.1005.2 and 10.0.1054.2 versions to prove that there are no changes in performance from one version to the other - therefore it must be a problem of their network or/and database. 

**Additional information**

- 
**This was not a product problem, since they had a network latency problem that was delaying the requests to the database.**

- 
**Even though we provided multiple proofs that the problem is on the customer side, the case has not been closed yet.**

### JBoss 6 and JBoss 7 start-up times
**Support case: **R11PIT-589ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Reported symptoms**

- 
Customer is reporting increased start-up times of JBoss in one of their infrastructures after the upgrade to JBoss 7.

**Troubleshooting steps**

- 
Global Support did not have access to the platform version to perform tests.

- 
The binaries for this and other FICO-specific versions are available in [Google Drive](https://drive.google.com/drive/u/0/folders/1gfEt2jnyBaPPV20GCwBewg--YD3nPAIH)

- 
R&amp;D followed up with RedHat and provided a patch that mitigates the main problem, keeping in mind that the times will never be comparable with the previous version and in fact, can be higher.

- 
R&amp;D provided some mitigation options such as trying to tune the Java VM parameters or memory, or to use a different garbage collection algorithm.

**Additional information**

- 
**This was not a product problem, just them asking why the startup time is slower for JBoss 7.**

- 
This should be asked directly to RedHat since it is a JBoss problem.

### Cannot access some SC pages against 1 DB in an Active-Active configuration
**Support case: **R11PBT-703ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Reported symptoms**

- 
Error when accessing an eSpace details page on Service Center (any module).

**Troubleshooting steps**

- 
Global Support could not replicate the error in Oracle.

- 
R&amp;D detected, by analyzing the logs, that there was a problem with the synchronization of the databases and advised the customer to check with their DBA to fix the issue.

**Additional information**

- 
**This was not a product problem.**

### ADOReader Datareader performance
**Support case: **R11PBT-718ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Reported symptoms**

- 
Customer is reporting that one of their queries is slow after updating to PS 10.0.1054.2 from PS 10.0.1005.2.

**Troubleshooting steps**

- 
Global Support analyzed the logs and some database metrics.

- 
R&amp;D stated that the code regarding the retrieval queries was not changed and that even though the oracle driver was changed the performance was not compromised.

- 
Customer kept insisting that it was a product problem even though SQLplus showed that the retrieval of data from the FE server to the Database was taking way too much time.

- 
R&amp;D ultimately [built a laboratory](https://docs.google.com/document/d/10RNNIuqK5JTPBSS-P9sdJ3IvqY9Pb86QjxARhJGpTTQ/edit) with both 10.0.1005.2 and 10.0.1054.2 versions to prove that there are no changes in performance from one version to the other - therefore it must be a problem of their network or/and database. 

**Additional information**

- 
**This was not a product problem, since they had a network latency problem that was delaying the requests to the database.**

### JBoss connectivity issue
**Support case: **R11PIT-659ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Reported symptoms**

- 
Customer is experiencing issues on DeploymentService because connectivity to JBoss is failing

**Troubleshooting steps**

- 
Global Support confirmed the error started occurring after upgrading only JBoss

- 
Global Support also pinpointed the issue as a connectivity problem.

- 
R&amp;D suggested the customer change the **standalone-outsystems.xml **configuration file and republishing the factory to stabilize it.

**Additional information**

- 
**This was not a product problem, the root cause was a problematic certificate that they were using.**

### JBoss was killed in all frontend servers
**Support case: **R11PIT-695ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Reported symptoms**

- 
The customer is facing an outage of the application after the JBoss process is killed with an &quot;**Out of memory: Kill process 1415 (java) score 773 or sacrifice child**&quot; message.

**Troubleshooting steps**

- 
Global Support could not reproduce the problem

- 
After analyzing the logs R&amp;D suggested the customer either increase physical memory or to
increase/add swap

**Additional information**

- 
**This was not a product problem, since it was the operating system that was killing JBoss.**

- 
The customer should have contacted with RedHat directly.

- 
**Case closed without further explanation**

### log4j vulnerability
**Support case: **R11PBT-846ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Reported symptoms**

- 
Customer has raised concern that the OutSystems 10 platform is still using the log4j version 1.2.17, which is already obsolete since it reached its end of life last August 2015.

**Troubleshooting steps**

- 
Global Support reached R&amp;D through slack

- 
Global Support shared with the customer the assessment of the library&rsquo;s vulnerabilities

- 
R&amp;D reiterated that the fact of the library being obsolete is not a problem and that it reserves the right, to decide which libraries will be upgraded or not

**Additional information**

- 
**This was not a product problem, just them asking why are we using a certain version of a library.**

### Applications downtime for 15 minutes, throwing 503 errors
**Support case: **R11PBT-893ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Reported symptoms**

- 
Applications were down for 15 minutes, throwing 503 errors

**Troubleshooting steps**

- 
Global Support found previous similar cases, but that path lead to nowhere, as in this case the customer did not have multiple DB nodes

- 
Checked the collect_stats.zip for the controller, however there were no relevant entries before the event

- 
From the logs, we noticed that there were no requests to the customer&rsquo;s applications during that timeframe, nor successful nor failed. We only saw requests to Service Center.

- 
R&amp;D asked if we could get logs and Deployment Controller Service thread dumps for the relevant timeframe (May 20 21:00 to 21:15 UTC)

- 
R&amp;D asked customer to check with Amazon if there were any failures that could impact their RDS during that time

- 
This could be RDS itself or DNS that resolves RDS calls or any other relevant cloud component that could affect connections between the Deployment Controller Service and the Database;

- 
R&amp;D asked customer to provide us with the STATSPACK for the relevant timeframe (since they do not have AWR enabled), starting 30 minutes before and ending 30 minutes after;

- 
R&amp;D asked customer to retrieve information from Performance Insights from the RDS;

- 
R&amp;D asked customer to check if there are configurations on the Load Balancer to check if Service Center is alive and if so, what is the time interval between polls.

- 
We noticed a pattern of three different IPs requesting the Homepage of SC every 30 seconds. A failure on SC should not create unavailability of a customer&rsquo;s application, so the Load Balancer should be probing a customer&rsquo;s application that is installed in all the servers instead.

**Additional information**

- 
There were no logs or thread dumps for the timeframe where the problem happened

- 
**This was not a product problem, they were asking for an RCA of why it happened**

- 
**Case closed without further explanation**

### Delay loading some pages/static resources
**Support case: **R11PIT-774ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Reported symptoms**

- 
Customer reported that some &ldquo;first&rdquo; accesses to some pages took long time to load.

- 
Customer sent chrome har browser reports with network evidences, and said that issue occurred more frequently on ErrorLogs page and after a &ldquo;delete cache&rdquo; from browser

**Troubleshooting steps**

- 
We analyzed the har files with chrome diagnostic tools (F12 network panel) and saw that on the reported scenario even static resources were taking longer than usual being served.

- 
We analyzed server configurations (standalone-outsystems.xml) sent, and noticed a lot of customizations.

- 
We sent a list of possible things to validate

- 
Turn off http2

- 
Separate mq into separate jboss instance

- 
collect gc logs

- 
remove services that are not necessary

Eventually customer replied that turning off http2 solved the issue

**Additional information**

- 
Since customer was using old JBoss version (7.2.7), we suggested them to upgrade to newest Jboss version 7.4.5 and validate if that solves the problem, and if not, to pursue the issue directly with RedHat about their http2 implementation.

- 
**This was not a product problem.**

### &ldquo;No such method&rdquo; error associated with the FasterXML/Jackson library
**Support case: **R11PIT-948ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Reported symptoms**

- 
Customer was obtaining a &ldquo;No such method&rdquo; error associated with the FasterXML/Jackson library. 

- 
This only happened on one of the servers, but not on others

- 
Support determined that customer was using an extension with a jackson library version - 2.12.3(jackson).

- 
Support suspected on jar hell, and asked why this was happening on one node and not other, and what would be the workaround

**Troubleshooting steps**

- 
Support basically did the troubleshoot and correctly assessed that the problem was related with a jar hell

**Additional information**

- 
We explained that the observed behaviour is consistent with jar hell. We can have servers working and non working depending on order of classloading on each server.

We also explained to avoid the jar hell, extensions that were using other versions of jackson libraries should use same version as the platform server.

### JBoss 7 fails to start because there are `.war.failed` files in the deployment folder
**Support case: **R11BRT-420ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Reported symptoms**

- 
Some modules on FICO's client are failing to be deployed (ending up with a `.war.failed` file in the deployments folder) after a JBoss restart

- 
FICO claims that this issue only occurs on 10.0.1054.2 while no such issue occurs on 10.0.1005.x

**Troubleshooting steps**

- 
Checked if they had enabled the deployment scanner - they did

- 
Enabled the deployment scanner on a JBoss machine

- 
Manually created an empty `.war.failed` file in the deployments folder

- 
Restarted JBoss, reproduced the problem

**Additional information**

- 
They have enabled the [Deployment Scanner configuration](https://docs.jboss.org/author/display/AS7/Deployment%20Scanner%20configuration.html) in their JBoss configuration file - this is not the default configuration provided by OutSystems nor is such configuration required in order for the OutSystems platform to operate;

- 
They are using [marker files](https://access.redhat.com/documentation/en-us/jboss_enterprise_application_platform/6.2/html/administration_and_configuration_guide/reference_for_deployment_scanner_marker_files1) - the OutSystems platform does not generate or use any marker files under any circumstances and it only uses APIs to perform the deployments

- 
They are hitting an [identified JBoss bug](https://bugzilla.redhat.com/show_bug.cgi?id=1169239) - this is the exact same bug that Global Support already identified, which was apparently fixed in JBoss 6.4.1, but it seems that it was never fixed for JBoss 7

- 
Asked them to pursue the issue directly with RedHat

- 
**This was not a product problem**

### &ldquo;Too many constants, the constant pool for X would exceed 65536 entries&rdquo; runtime error when accessing a page
**Support case: **R11BRT-438ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Reported symptoms**

- 
When opening the application, they get the runtime error described above

- 
Errors only happen on first access

- 
Errors did not happen in 10.0.1005.2 version

- 
Customer application/screen complexity is huge, GS and TSM already suggested refactoring, customer says they can&rsquo;t do it

**Troubleshooting steps**

- 
Tried to deploy their module to check the generated code - failed because of missing dependencies

- 
Explained miss conceptions about code generation and code compilation

- 
Explained that we changed the code generation due to bug and vulnerability fixes, which added more constants to the pool - this combined with the complexity of their application/screen leads to the problem

- 
Referred to the JVM specification as a way for the customer to understand the kind of elements that count towards the constant pool limit

**Additional information**

- 
The issue is triggered by a combination of two factors: their application/screen complexity and a limitation in the underlying technology (Java)

- 
Reinforced the need to refactor the customer application

- 
**This was not a product problem**

### JBoss restart run into &quot;java.lang.OutOfMemoryError: GC overhead limit exceeded&quot;
**Support case:** R11BRT-892ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Reported symptoms**

- 
When restarting JBoss, they run into the error above

- 
Error occurring in JBoss 7.4.7 and 7.4.14, with platform server 10.0.1056 (latest available at the time)

**Troubleshooting steps**

- 
Check logs

- 
Understand that the problem only happens when JBoss is restarted and it is loading the applications, which means that the applications had already been deployed there to begin with - this pretty much says it is not an OutSystems problem

**Additional information**

- 
Suggested that the customer open a support case with RedHat

- 
**This does not seem to be a product problem**

### Deployment operation gets stuck during publication in random nodes, causing JBoss and the Deployment Service to fail
**Support cases: **R11BRT-1021ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

R11BRT-1171ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Reported symptoms**

- 
While doing a publish on a farm scenario, the deployment operation would succeed for some nodes and fail for other nodes - this would happen in a non-deterministic way, failing and succeeding on different nodes every time;

- 
Deployment Service would eventually stop being responsive

- 
There were errors in JBoss logs about failed deployments

**Troubleshooting steps**

- 
Looking at the logs;

- 
At first this looked like it was caused by some RedHat instability, so we asked customer to engage with RedHat;

- 
Global Support, RedHat and FICO managed to collect thread dumps where the evidence pointed to the thread being stuck on `FixMemoryLeaks` code, which is provided by an extensibility point and included in `web.xml` when it is being generated

- 
Turned on new logs, to ensure threads were really being stuck where RedHat claimed

- 
Give them a jar file to put in connectors directory, which removes that `FixMemoryLeaks` code from the generated files

- 
Give them a .sh file to remove the relevant lines from `web.xml` files of running applications

**Additional information**

- 
The `FixMemoryLeaks` code was added several years ago as an attempt to address some memory leaks detected in a previous version of JBoss. It was kept in the product, as we believed it was more beneficial than harmful.

- 
We will need to rethink that code for an upcoming version of the product

### Cannot Synchronize Application Changes because there is an error synchronizing users
**Support case: **R11CT-3242ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Reported symptoms**

- 
Sync environment doesn&rsquo;t end because of error: `Error creating or updating user Pramod Muthanna (pramodmuthanna@fico.com) in Test2: A user already exists with the username 'pramodmuthanna@fico.com'.`

- 
Application Versions in LifeTime are not updated.

**Troubleshooting steps**

- 
Look at the Users table of LifeTime and affected environments and compare the External_Id of users failing the synchronization. External_Id should be the same for the same username. If not, the error above will fail.

**Additional information**

- 
To overcome the problem, clear the External_Id of affected users so that the match will be done by username. When synchronizing in this way, the External_Id will be updated correctly.

### Occasional CPU and memory spikes when GC is running, system becomes irresponsive
**Support case: **R11BRT-1379ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

**Reported symptoms**

- 
Memory and CPU going up at random times during day

- 
Production environment becomes irresponsive

- 
Restarting services solves the issue until it happens again

- 
Platform code did not change, application code did not change

**Troubleshooting steps**

- 
Check logs, ps files

- 
Disable all monitoring tools that the customer has on their environment (Dynatrace, Crowdstrike, Splunk, BMC Performance Manager for Servers, Rapid7 and who knows what else)

- 
Collect and analyse thread/memory dumps when the issue is happening

- 
Customer and Global Support analysed thread and memory dumps, detected which objects were taking the most memory

- 
Pinpointed application problem, which started to show after some input changed (decimal value being used without the logic being prepared for that)

**Additional information**

- 
Unsupported version 10.0.1005.2, case should have been dealt with at best-effort, but there was internal interference that made its priority raise to high.

- 
Reinforced the need to change the customer application

- 
**This was not a product problem**

## Template for future entries in this document### Support case one-line summary
**Support case: &lt;Jira link&gt;**

**Reported symptoms**

- 

**Troubleshooting steps**

- 

**Additional information**

- 
N/A

# Generic troubleshooting strategies
Most of the strategies in this section consider and **take advantage of the fact that the platform server code is quite stable for a long time and has not changed significantly.** Following these strategies will allow us to break the &ldquo;it&rsquo;s a platform problem, prove that it isn&rsquo;t&rdquo; endless cycle that FICO cases tend to fall into after a few interactions. It will also put us in a position where we have the upper hand, which shifts the power balance of these conversations towards us, allowing us to state things like &ldquo;it&rsquo;s not a platform problem, so let&rsquo;s look at something else in your installation&rdquo;.

Let&rsquo;s keep in mind that FICO **always** wants to setup a call with OutSystems engineers to go through their issues, so knowing that it is likely not a product problem will clearly help us define our troubleshooting path.
## Always check that FICO sent what we asked from them
This may seem obvious, but it is worth reinforcing. Since FICO opens the support cases on behalf of their customers and they need to ask their customers to retrieve what we asked for, it is likely that sometimes they will provide us with wrong/incomplete information. As we stated earlier, **it is of utmost importance that we send them as many detailed instructions as we can regarding the things they need to collect.**

In the past, we&rsquo;ve had cases where we asked them to send us more information and:

- 
they gathered information from some other environment; **OR**

- 
they gathered information in the wrong time frame (or timezone); **OR**

- 
they redacted information that we needed to troubleshoot the issue.

It is important that they send us what we ask, otherwise we are just doing rounds of ping-pong to get the right information about the case.
## If you must look at code, always look at the right code
As stated in the `What do we need to know about the FICO-specific product line? Where can we find the code and binaries?` collapsible section at the top of this document:

- 
For versions 10.0.105x.x, all the code is written in Java;

- 
For all other versions, some of the code is translated from C#, some code is written in Java;

In the past, we&rsquo;ve had cases where people decided to look at the C# code and made potentially wrong inferences from there. We must avoid that.
## If DB operations are slow, always ask for statistics, fragmentation, and AWR/STATSPACK reports
We can&rsquo;t troubleshoot DB issues if we don&rsquo;t know what is going on inside the DB.

If they report an issue after a DB upgrade, then statistics and fragmentation are good starting points to start the investigation.

In the past, we&rsquo;ve had cases where the problem was caused by an application query or by an application pattern that causes the query to run too many times.
### Database statistics
Sample message, to be adapted as needed:

We are trying to understand the cause behind the database slowness.

Since database objects change very frequently, it is important to keep statistics updated regularly. It is also very important to update dictionaries and object statistics after they upgrade their database.

We would like to know if their DB statistics need to be updated. As such, we would like their DBA to execute the following query and return the result to us:
sql
After running the above query, we ask that that their DBA runs the following query. For each command you can see that we left comments with instructions that we recommend for them to follow:
sql '');]]>### Table fragmentation
Sample message, to be adapted as needed:

We are trying to understand the cause behind the database slowness.

Since adding and removing records to the database can lead to database fragmentation, it is important to check for it regularly and fix it when applicable.

We would like to know if the tables used by the reported slow queries are experiencing some fragmentation. As such, we would like their DBA to update statistics and afterwords execute the following query, **for each table involved in the query that is reported slow**:
sql parts as appropriate for the customer

select
  owner,
  table_name,
  num_rows,
  blocks,
  avg_row_len,
  round(( blocks *  ) / 1024, 2) sizeMB,
  round(( num_rows * avg_row_len / 1024 / 1024 ), 2) actualSizeDataMB,
  (round( blocks * , 2)/1024 - round(( num_rows * avg_row_len / 1024 / 1024 ), 2)) freeSpaceMB,
  (round(( num_rows * avg_row_len / 1024 / 1024 ), 2) * 100)/ case (round(( blocks * ), 2) / 1024) when 0 then 1 else (round(( blocks * ), 2) / 1024) end percentage

from
  dba_tables

where
  owner = 'OSADMIN_0007R1'
  and table_name = 'OSUSR_CTK_OMSAASR1_T7103'

order by
  freeSpaceMB desc
;]]>
If the fragmentation is higher than 30%, their DBA needs to repair it. The commands to defrag the table depend on the indexes created on this table (function-based indexes per instance). So their DBA should be able to decide how to defrag the table.
### AWR/STATSPACK report
Sample message, to be adapted as needed:

We are trying to understand the cause behind the database slowness.

Please ask the customer for an AWR/STATSPACK report (if they are running a RAC, we need a report per instance) from before the issue happens until they stop experiencing the problem. Or if the problem doesn&rsquo;t stop occurring, until 20-30 minutes have passed since they started experiencing the problem.

Their DBA should know how to retrieve such a report.
## If DB operations are slow, any troubleshooting queries must be run from the application server, not on the database
Running queries directly in the database server does not reflect the same conditions as calling it over the network. The former only requires the data to be retrieved from the database. The latter also requires that the data be serialized, transferred through the network and serialized again on the client application (the OutSystems Platform, for example). If there is significant network latency, the latter will be significantly slower than the former. 

In the past, we&rsquo;ve had cases where the customer kept comparing measurements of query time on the database and measurements of query time on the application server. Such tests and any conclusions coming from them are invalid. [This document](https://www.outsystems.com/forums/discussion/15702/tip-performance-of-query-in-outsystems-platform-slower-than-running-in-database/#) contains information that the customer may find useful to understand what they need to account for when running such tests.

We have used three methods to run troubleshooting queries: **test OML, SQL*Plus and SQLcl**. You can use whatever method you think is more appropriate and you need to keep in mind that the SQL*Plus and SQLcl methods will completely remove the platform code from the equation, as they execute the query via JDBC driver. If the query is slow using such methods, it&rsquo;s enough proof that this is not a product problem.

All of these methods have been used in previous support cases to prove that the customer was not facing a platform problem.
### Running a troubleshooting query from the application server via a test OML
Creating a test OML provides the customer with a rapid way to test a given query. In short, this is what we need to do in such an OML:
- 
Take note of the current time

- 
Execute the query

- 
Read the contents of the query into some variables

- 
Take note of current time 

- 
Put contents of the query on the screen or in a log

- 
Calculate elapsed time

This process will allow us to measure the time it takes to execute the query and retrieve the resulting data over the network. The last step ensures that the optimizer will not play tricks on us and that the query will effectively load the data. If we need millisecond precision, we can use the [DateUtils forge component](https://www.outsystems.com/forge/component-overview/674/dateutils).
#### Example OML used in a previous support case
We prepared an OML file that the customer can publish in their environment and test the retrieval time of the OML_FILE column into their frontend server.

After publishing this OML file, the customer should open the application in a browser and there they will see the list of rows in the OSSYS_ESPACE_VERSION table. For each row, there is a button that will retrieve the OML binary data from the database and will output the elapsed time (in seconds) and the size of the OML.

As they already should know the sizes from the query they run previously, we suggest that they pick the biggest and smallest entries in the database for this test. The biggest entries will let us know what are the worst case scenarios for this kind of query, and the smallest ones will help us identify a baseline for their database performance. For instance, they can test retrieving the items with the ID 1, 39637, 39047, 36873, 39007 and 38927, and send us back the obtained results.

This OML is writing the results into general logs, so we kindly ask the customer to send them after running the tests.

In case the results aren&rsquo;t significantly slow, it will be useful if they send us the results within and outside the timeframe where the issue is happening. We believe that the performance issue will happen every time, within and outside the referred timeframe. But in case we are wrong, it will be useful to compare the times of both scenarios and check if the issue happens at least during those first 20 minutes after the restart.

The screen they will obtain will be similar to the following screenshots:
### Running a troubleshooting query from the application server/controller via SQL*Plus
Another way for the customer to test a given query is for them to execute the generated query via SQL*Plus. This will allow the customer to run the query without having the platform in the way, which is a good way to understand if the problem is related with the platform. In short, this is what we will need to do:
- 
Identify the query that we want to run

- 
Write the query in a script

- 
Run the script

- 
Take note of the current time

- 
Read the contents of the script and write them into a file

- 
Take note of the current time

- 
Calculate elapsed time

This process will allow us to measure the time it takes to execute the query and retrieve the resulting data over the network, but not including the time it takes for the platform to process the data.
#### Example SQL*Plus strategy used in a previous support case
In order to find out the times of retrieving some binaries directly from the database, we created a script in **SQL Plus**. This script was intended to find out if there was any abnormal latency when retrieving data from the database from the controller.

To remove the process of rendering the data on the screen, which may consume a lot of time, the script writes the data directly into a file.

The script provided here has the Service Center ID as the default **espace_id**:

Steps to run this script:

1. Place this file in the Controller server

2. Connect to the database using sqlplus.

3. Run the command **@download **(do not copy/paste the content of this document into sqlplus - this will produce different behaviour).

4. The results will be present in the results.sql file.

The elapsed time will not show the time to render the data on the screen and thus help us to draw conclusions.
### Running a troubleshooting query from the application server/controller via SQLcl
Similarly to SQL*Plus, SQLcl provides another way for the customer to test a given query. This will allow the customer to run the query without having the platform in the way, which is a good way to understand if the problem is related with the platform. In short, this is what we will need to do:
- 
Identify the query that we want to run

- 
Write the query in a file

- 
Run the SQLcl with the file as input

- 
The file will run the query, retrieve the data and calculate the elapsed time

This process will allow us to measure the time it takes to execute the query and retrieve the resulting data over the network, but not including the time it takes for the platform to process the data.
#### Example SQLcl strategy used in a previous support case
Regarding the application to test latency, to test the issue in similar conditions as the platform we suggest that their DBA uses SQLcl in their frontend server, connected to the affected database. Here are the steps to do that:

- We are providing them with the zip file, so they can download it and run it on their frontend:

- Download and extract the zip contents to a folder

- In this folder there is an SQL script file, named saasresponsetest.sql, that will allow them to run the same query the platform is running and measure the elapsed time

- We need to ensure that the query is run against the right table. To do this run the following query:
sql
- Open the SQL file and modify:

`&lt;name of the schema&gt;` with their database schema name

`&lt;insert_table_name&gt;` with the actual table name obtained from the previous query

`???` with the desired ApplicationId to be tested

- Open the console in the extracted location, where you should have a &ldquo;sqlcl&rdquo; folder and the saasresponsetest.sql file

- Run the following commands:
bash/@:/ @saasresponsetest.sql]]>
- After the command execution, a new file will be created in the same directory, with the name result.txt.

- Open the file, and in the bottom a &ldquo;Elapsed: xx:xx:xx.xxx&rdquo; line which represents the elapsed time executing the query

We kindly ask that the customer runs several tests for known problematic applications, if there are any more problematic than the others, and send us back the output files.