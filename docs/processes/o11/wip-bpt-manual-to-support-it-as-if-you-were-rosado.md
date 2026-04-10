---
title: [WIP] BPT: Manual to support it as if you were Rosado
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/2989293996/WIP+BPT+Manual+to+support+it+as+if+you+were+Rosado
confluence_space: RCP
confluence_page_id: 2989293996
last_synced: 2026-04-09
owner: Process Engineering
---

# [WIP] BPT: Manual to support it as if you were Rosado

## Before you start: overall context on how it works

On enqueue:

- 
When the Process has a Launch On property defined on a database operation

The database table where the operation is associated with a specific process has another specific database table whose name has the OSEVT prefix and it is followed by that specific table name e.g. OSEVT_D4O_INSPECTION.

When the module where the process lives is published, we introduce the necessary information on that mentioned table. 

There is also a trigger that is created on the original table (OSUSR_D4O_INSPECTION) that basically inserts a new record on OSSYS_BPM_EVENT_QUEUE table j(using the data that was registered in the OSEVT_D4O_INSPECTION table) when the operation associated with the process occurs. 

On dequeue:

From time to time, there&rsquo;s a timer checking the contents of the OSSYS_BPM_EVENT_QUEUE table to detect if there&rsquo;s something to run.

When the time comes, it calls the dequeue method. This method will call the Dequeue_ossys_Event stored procedure that will return the list of events to process. For each one of the events in that list, we will create an EventJob or LightEventJob object.

**Relevant database tables:**

**Relevant files:**

(Platform repo) JobFactory.cs

(Platform repo) LightEventJob.cs

(Platform repo) EventJob.cs

&hellip;

**Relevant parameters:**

For normal BPT Events:

For Light BPT Events:

- 
Global Setting (OSSYS_PARAMETER)

- 
BPT.EnableLightProcessExecution** **(default: **False**)

- 
Espace Setting (OSSYS_ESPACE_CONFIGURATION)

- 
BPT.EnableLightProcessExecution** **(default: **False**)

- 
Scheduler Settings (OSSYS_PARAMETER)

- 
Scheduler.NumberOfThreadsForLightEvents (default: 20)

- 
Scheduler.DelayBetweenExecutionsForLightEventsMs (default: 10 ms)

- 
Scheduler.DelayBetweenDbLightEventPollingMs (default: 500 ms)

- 
Scheduler.NumberOfJobsPerThreadForEvents (default: 4)

- 
Scheduler.MaxNumberOfConsumerThreadsInDevelopmentMachines (default: 4)

- 
Scheduler.LightProcessBackoffMaxDays (default: 30)

### Normal BPT Events vs Light Events#### Why?
Some customers were already exhausting the integer max value for processes and activity instances. 
#### The solution
Create simple events (must have a single automatic activity) that don&rsquo;t need to create processes or activity instances to avoid increasing the current id value. As a bonus, they have a much higher throughput than normal BPT events.

More info here: [https://docs.google.com/presentation/d/15CDdTOjcshUe9Fu60U9x1AY9HsCHyYD_hUWgb0xtP28/](https://docs.google.com/presentation/d/15CDdTOjcshUe9Fu60U9x1AY9HsCHyYD_hUWgb0xtP28/)  
## Avoid having enormous tables and how to delete them?
## How to restart scheduler
(taken from R11PBT-121ef8955cb-cb21-32a7-b692-01ace42388d6System JIRA )

The recommended procedure is to perform a safe shutdown of the machine:

- 
Disable the Execute Timers, etc. settings for the FE in Service Center;

- 
Go to Monitoring, Environment Health, click Detail in the Scheduler column and row for that FE, and wait until there are no active threads (all with status Idle, Sleeping or Disabled).

If no downtime is desired with respect to the processing of Processes, Timers, and Emails, one of the other front ends should have these settings enabled for this duration. After the restart, the designated front end can be again set as the only one with the settings enabled.

The customer can't stop the Scheduler in the middle of BPT execution otherwise it may have some unexpected impact. The Scheduler doesn't recover the event execution as it doesn't know where the execution stopped (and what was executed already). Repeating it can lead to executing the same code twice and it may not be acceptable. More recent versions of the platform already have some logs that provide information to the user about the occurrence of stopped events in these circumstances.
## Timeouts and retries
(taken from R11PBT-633ef8955cb-cb21-32a7-b692-01ace42388d6System JIRA)
### (WIP) Is there any retry mechanism for Human Activities similar to what we have for Automatic Activities?
Yes. The Human Activities actually do retry the execution when the exceptions occur. In the monitoring tab of Service Center, if you select the process, then the instance in error and then the Human Activity, you can actually see that it has a Next Run scheduled (before the retry). The On Ready callback should be executed again in the retries if the activity persists in the Ready state
## Changing the sequence cache value
## How to adapt the BPT parameters (or disable frontend as in R11PBT-326ef8955cb-cb21-32a7-b692-01ace42388d6System JIRA ) when the BPT is barely used
## Support cases examples
**What's wrong?**

**Issue**

**Main steps to troubleshoot it**

**What did we learn?**

Customer was unable to delete data from BPT tables

R11PBT-614ef8955cb-cb21-32a7-b692-01ace42388d6System JIRA

- 
R&amp;D has a script to delete the data that always worked before and was also failing here (deleting 0 rows) so, we tried to understand which part of the script could be returning empty data and ended up by causing 0 rows to be deleted. So, we asked support to run the parts of the script that could be returning empty results to see what data we could get

- 
Support just told us all the queries were returning empty. Looking at the error from Error Log, it was possible to understand which was the action that was causing issues from BPT API and Support suggested to extract the queries the API was using and try to run these separately to understand where the problem was

- 
We were executing these queries one by one using the same parameters as the customer and we were able to understand that it was failing just in the first set of rows

- 
We looked at these rows and understood that something weird was in the data: we knew that, **when the PARENT_PROCESS_ID and PARENT_ACTIVITY_ID attributes are null (from OSSYS_BPM_PROCESS), the TOP_PROCESS_ID needs to have the same value as the ID attribute of the same row** and this wasn't happening. So we manually fixed these null values and repeated the delete process and it worked!

**Context**

The action Process_BulkDelete of BPT API, and both scripts that remove processes manually (for MSSQL and Oracle) have a similar patter. Summarizing, it is:
- 
They identify the processes to be removed.

- 
They remove circular references setting to NULL the field PARENT_ACTIVITY_ID

- 
They remove child processes

- 
They remove circular references setting to NULL the field TOP_PROCESS_ID

- 
They remove the parent processes

**Cause**

The described issue can be caused by one of the two following situations:

- 
The customer ran Process_BulkDelete, but it wasn't completed (for any reason), and it was interrupted in some point between step 4 and 5. 

- 
The customer ran the script provided by Support, but it wasn't completed (for any reason), and it was interrupted in some point between step 4 and 5. Probably this is not the case because the customer shouldn't have the script before pinging Support.

So, in the future, when the PARENT_PROCESS_ID and PARENT_ACTIVITY_ID attributes are null (from OSSYS_BPM_PROCESS), the TOP_PROCESS_ID needs to have the same value as the ID attribute of the same row. We need to pay attention to these values next time this issue happens

 

R11PBT-121ef8955cb-cb21-32a7-b692-01ace42388d6System JIRA 

R11PBT-99ef8955cb-cb21-32a7-b692-01ace42388d6System JIRA