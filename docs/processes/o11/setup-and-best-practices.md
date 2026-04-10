---
title: Setup and Best Practices
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/819527883/Setup+and+Best+Practices
confluence_space: RCP
confluence_page_id: 819527883
last_synced: 2026-04-09
owner: Process Engineering
---

# Setup and Best Practices

Some information might be outdated/deprecated

First of all, be sure you have read all the documentation regarding Support Cases in R&amp;D:

- 
Support Cases in Jira 

- 
Communication in Support Cases 

- 
Support Cases Priorities and OLAs 

- 
Creating a defect from Support Cases 

Even if you already know these documents, it is always worth reviewing them before starting your Support rotation.
## Machine Setup
To be effective while working on support cases you may need to have some tools installed on your machine. Please check the list below and ensure you have the necessary tools setup on your machine.

- 
**Excel**

- 
It is often necessary to open large excel files with logs from the customer in order to troubleshoot problems. If you have Visual Studio installed, you can have a license for Excel. Find the procedure to unlock this on this page.

- 
**Switch to O10** 

- 
Some issues are reported in O10 and require troubleshooting in your local machine and/or create a QF. In order to do so you need to have b10_0 repository on your machine and switch installed and setup (check this page for instructions).

- 
**Support Sandboxes**: 

- 
This tool allows the creation of one or more machines in a specific version. This is very useful to try and reproduce the problem in a specific version and to validate quick-fixes. **These machines should only be used in the context of support cases** and their access is currently restricted to old members of the Quick Response Team. You can find how to use this tool [here](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/341803166/Support+Sandboxes). 

- 
Use the Platform Requester to make machines in specific versions: [http://engineering.outsystems.net/regressionrequester/PlatformRequest.aspx](http://engineering.outsystems.net/regressionrequester/PlatformRequest.aspx)

## Quick-fix guidelines
You can find the full detailed process in [How to release a Quick-fix](https://outsystemsrd.atlassian.net/wiki/spaces/RRT/pages/364183707/How+to+release+a+QuickFix)

When implementing a quick-fix always have in mind [Risk Management](https://docs.google.com/presentation/d/1MMtxMGguQbtOiYYRGYQ7VMIdCRaPSeNN_SpIuBXoEDk/edit#slide=id.g545bf2982a_0_236) principles along with the following guidelines:
- 
First ensure the quick-fix (QF) goes into the product
- 
[Create a product defect](https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/730595517/Creating+defect+from+Support+Cases) if there isn&rsquo;t one already created

- 
Communicate the defect id to Support so they can provide to the customer and keep track of more hits in other customers

- 
Commit to the trunk and r11_0_0 branches (**only if no stabilization is in progress!**)

- 
Ensure the QF is made on the customer's PS version
- 
Ask the Support Engineer to confirm the customer&rsquo;s version before proceeding with the QF

- 
**All QFs must have a build** even if it is &ldquo;just a modified .oml&rdquo;. Follow the process described [here](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/364183707/Create+a+Quick+Fix) to generate the build and validate the build in a regression (execute relevant tests for the fix you made)

- 
There are no QF on Service Studio, the release cycle is so small it does not justify the need for a QF

- 
Always provide crystal clear steps on how to apply the QF to Support

- 
Always provide the risk and impact of applying the QF (e.g. is it necessary to do a publish all? will it cause downtime? etc.)

## Providing custom DLLs for traces
Sometimes our product does not give us enough information for troubleshooting and it may be the case we need to provide our customer with a custom DLL to gather more information. If that is the case then please make sure to follow these guidelines:
- 
Ensure the custom DLL is generated for the customer&rsquo;s PS version
- 
Ask the Support Engineer to confirm the customer&rsquo;s version before proceeding with the DLL generation

- 
When providing the custom DLL make sure to state for which PS version it was generated for
- 
If there is a mismatch with the customer&rsquo;s version then Support can detect

- 
Even after the confirmation from point 1, mismatches can happen (e.g., the customer decided to upgrade in the meantime or test the DLL in a different environment) so do not skip this step

- 
Check obfuscation list to see if the DLL needs to be obfuscated
- 
For O10 follow the process described here

- 
For O11 follow the process described here

- 
Always test the custom DLL in a sandbox to validate whether
- 
The DLL works for the customer's version

- 
The traces give you the information you are expecting and are enough to proceed with troubleshoot

- 
Be mindful of the impact having more traces have on the customer&rsquo;s infrastructure
- 
Can it cause downtime due to resource exhaustion?

- 
Will it impact the application&rsquo;s performance and/or customer&rsquo;s end-users?

- 
If there is an impact then discuss with Support Engineer on a plan to have these traces enabled in a short period of time that gives you enough information to proceed

- 
Always give crystal clear instruction on how to install and enable the provided custom traces
- 
This includes backup and reverts steps

- 
Consider if the traces you added should be in the product for troubleshooting
- 
If so, create a task and follow the normal development process (code review, CI, etc.)

## Enabling OSTraces
OSTraces are useful to troubleshoot issues within the platform or within the generated applications. 

For instance, if you provided a custom DLL with more traces, you will most likely need to enable OSTraces in the OutSystems application you want to troubleshoot (unless the DLL is related to OutSystems service).

OutSystems provides OSTraces to the following components:

- 
Service Studio

- 
OutSystems Services

- 
Configuration Tool

- 
OutSystems applications

To enable OSTraces, follow the instructions provided in our [documentation](https://success.outsystems.com/Support/Enterprise_Customers/Troubleshooting/Change_OutSystems_Platform_logging_levels_(OSTrace)). 

For Service Studio follow the instructions below:
- 
Go to Development Environment installation folder

- 
Open file ServiceStudio.exe.config and you will find several switches in comment under `&nbsp;&lt;system.diagnostics&gt;` section

- 
Uncomment the switches you want to enable
- 
You can check ServiceStudio project and search for instances of the OSTraceSwitch class to know which switch you want to enable (or you can create a new switch if it makes sense)
- 
For e.g., in DatabaseAPIRESTClient.cs you will find the switch *DatabaseAPIRESTClient*

- 
The generated OSTraces is located at *C:\Windows\Temp\general.txt* by default so, unless this path is changed, you will need to run Service Studio in *Administrator* mode so it can write to *C:\Windows\Temp*

## [Support Dashboard](https://outsystemsrd.atlassian.net/secure/Dashboard.jspa?selectPageId=17111)

Link: [https://outsystemsrd.atlassian.net/secure/Dashboard.jspa?selectPageId=17111](https://outsystemsrd.atlassian.net/secure/Dashboard.jspa?selectPageId=17111)

The support dashboard gives an overview view of the support board. It includes:

- 
Number of cases in each of the columns of the board and how many cases are currently breaking OLA

- 
The calendar marking the days when support cases reached the Strategic Ops team

- 
List of support cases and their OLA status, order by the case that needs attention faster (either the case with broken OLA for the longest time or the case that will break the OLA sooner)

### Useful queries
- 
Need to find cases opened in Strategic Op&rsquo;s board since a specific date, use this Jira query: [https://outsystemsrd.atlassian.net/issues/?filter=32860](https://outsystemsrd.atlassian.net/issues/?filter=32860)

### Support Metrics
Please check [our documentation](https://docs.google.com/document/d/1bMn_jaT9VgAKmZTavOa6Qm7D4gboiS2BBFZhNpD_ZJg/edit?usp=sharing) on how to extract Support Metrics using PowerBi.
## Help! I&rsquo;m feeling overwhelmed!
It&rsquo;s ok! We all feel overwhelmed from time to time. Just take a deep breath and remember: **You are not alone****.** 

Support rotation does not mean you can&rsquo;t rely on your team when needed (to gather context; to discuss ideas to unblock the customer/fixes; to relay some of the work if the TC feels it is needed; etc.). And you have former QR members to assist you when needed.

Also, don&rsquo;t let OLAs get to you! They are important to guide us on how we should prioritize our support cases but don&rsquo;t get obsessed with them. 

If you must break an OLA to focus on a more important support case then break it! Just be sure to give visibility to your team so it can adapt if necessary.

Trust me, this gets easier with time  
## Q&amp;A
**Q**: If a support case with higher priority drops when I&rsquo;m already working on another support case, should I stop the one I&rsquo;m working on to pick it up?

**A**: Well, it all depends. Normally we should finish the work in our current support case before picking up a new one, to avoid losing progress or context. Nevertheless, depending on the situation and at which stage you are in the troubleshooting of the current support case or maybe you can give a quick answer or have a quick-win in the new support case, it may be worth it to switch to the new support case.

**Q**: I passed a modified version of an OML/DLL to a customer in order to overcome a problem, do I need to make that change in the product?

**A**: YES. In fact, when doing a quick-fix on an OML or creating a DLL to pass to the customer, you should commit first, wait for internal validations (CI and code review), and only after that should the OML/DLL be passed to support and the customer. Please note that if the quick-fix is for a PaaS customer and it&rsquo;s on Platform Server code, then you will need to generate a build.
## Additional Tools
You can find below some useful tools.

- 
Support Portal - **Customer Tickets**: If you need to consult an existing support ticket but do not have access to Zendesk, you can use the following link replacing *{id}* by the Zendesk ticket id:  [https://extranetinternalapps-prd.outsystems.net/SP360_CustomerTicket_UI/CustomerTicket_Detail?TicketITSMId={id}](https://extranetinternalapps-prd.outsystems.net/SP360_CustomerTicket_UI/CustomerTicket_Detail?TicketITSMId=%7Bid%7D)

We don't know how much time this URL will be available. If you know any other workaround to see Zendesk tickets, share it!