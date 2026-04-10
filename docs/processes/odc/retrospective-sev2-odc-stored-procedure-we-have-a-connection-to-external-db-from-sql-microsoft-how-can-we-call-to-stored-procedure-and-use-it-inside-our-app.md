---
title: Retrospective-SEV2-ODC STORED PROCEDURE - We have a connection to external db from sql microsoft , how can we call to Stored procedure and use it inside our app.
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4333731924/Retrospective-SEV2-ODC+STORED+PROCEDURE+-+We+have+a+connection+to+external+db+from+sql+microsoft+how+can+we+call+to+Stored+procedure+and+use+it+inside+our+app.
confluence_space: RKB
confluence_page_id: 4333731924
last_synced: 2026-04-09
owner: Process Engineering
---

# Retrospective-SEV2-ODC STORED PROCEDURE - We have a connection to external db from sql microsoft , how can we call to Stored procedure and use it inside our app.

## 📘 Overview
Author:&nbsp;trueGreyRootly

Severity:&nbsp;trueRedSEV2

Teams:&nbsp;trueBlueExtended Runtime
#### 🕐 Timestamps
Started At:&nbsp;trueBlueAugust 5 11:42 AM WEST

Mitigated At:&nbsp;trueYellowAugust 5 11:43 AM WEST

Resolved At:&nbsp;trueGreenAugust 5 11:43 AM WEST
#### 🔗 Links[Incident Page](https://rootly.com/account/incidents/749-odc-stored-procedure-we-have-a-connection-to-external-db-from-sql-microsoft-how-can-we-call-to-stored-procedure-and-use-it-inside-our-app)
[Pagerduty incident](https://outsystems.pagerduty.com/incidents/Q0QE620HHZTRN7)

[Slack channel](https://slack.com/app_redirect?channel=C07DLKJUTU5&amp;team=T041063TZ)

[Zendesk ticket](https://supportoutsystems.zendesk.com/agent/tickets/3032972)

#### 🧑&zwj;🚒 Incident Rolestrue
**Engineer**

Rafael Seara
#### Summary
----------------------------------------------**R&amp;D ESCALATION FORM**
Section comments can be removed for R&amp;D easier interpretation.**ISSUE DESCRIPTION AND HOW TO REPRODUCE**- The customer opened the ticket querying if would be possible to use stored procedure in a ODC .
- They were able to successfully create a connection and get the entites from it but when calling the stored procedure they had the following error:- ![](https://supportoutsystems.zendesk.com/attachments/token/lBBfmjPomBPthvIHI8yDfZKwP/?name=image.png)- Checking Grafana, found the errorError in advanced query SQL1 in DataAction1 in Home in MainFlow in GviaPoc (CALL [gvia].P_GetInquiries): 3F000: schema &quot;gvia&quot; does not existPOSITION: 6. at ssGviaPoc.ScreenServices.GviaPoc_MainFlow_Home_ScreenModel.FuncDataActionDataAction1.QuerySQL1(IRequestContext requestContext, Int32 maxRecords, IterationMultiplicity multiplicity, Int32 qpinsug_zihuy, String qpstms_zehut, Int32 qpinms_tik, String qpstErrorMsgLog, Int32 qpinErrorIDLog, CancellationToken cancellationToken) at ssGviaPoc.ScreenServices.GviaPoc_MainFlow_Home_ScreenModel.FuncDataActionDataAction1.QuerySQL1(IRequestContext requestContext, Int32 maxRecords, IterationMultiplicity multiplicity, Int32 qpinsug_zihuy, String qpstms_zehut, Int32 qpinms_tik, String qpstErrorMsgLog, Int32 qpinErrorIDLog, CancellationToken cancellationToken) at ssGviaPoc.ScreenServices.GviaPoc_MainFlow_Home_ScreenModel.FuncDataActionDataAction1.QuerySQL1(IRequestContext requestContext, Int32 maxRecords, IterationMultiplicity multiplicity, Int32 qpinsug_zihuy, String qpstms_zehut, Int32 qpinms_tik, String qpstErrorMsgLog, Int32 qpinErrorIDLog, CancellationToken cancellationToken) at ssGviaPoc.ScreenServices.GviaPoc_MainFlow_Home_ScreenModel.DataActionDataAction1(IRequestContext requestContext, CancellationToken cancellationToken) at ssGviaPoc.ScreenServices.GviaPoc_MainFlow_Home_Controller.&lt;DataActionDataAction1&gt;b__11_0(String screenName, JObject screenModel, JObject inputParameters, JObject clientVariables, CancellationToken cancellationToken) at OutSystems.RESTService.Runtime.Core.Controllers.ScreenServices.ScreenServicesApiController.InnerEndpointAsync(String apiVersionHash, EndpointAsyncImplementationDelegate implementationAsync, ResponseVersionInfo responseVersionInfo, ServiceRequest requestPayload, CancellationToken cancellationToken) at OutSystems.RESTService.Runtime.Core.Controllers.ScreenServices.ScreenServicesApiController.EndpointAsync(Stream input, String apiVersionHash, EndpointAsyncImplementationDelegate implementationAsync, CancellationToken cancellationToken) OutSystems.Application.ErrorHandling.DatabaseException OS-BERT-60407- Connectivity with External DB works well.
- Application: GviaPoc.oml
- The O11 syntax to **Call a stored procedure**:To call a stored procedure you have to use some .NET native objects that you can obtain by calling the RuntimePublic.Db API methods. To obtain them, all query objects have a GetDriver&lt;ClassName&gt; method that returns the language native object.&nbsp;When using .NET native objects, make sure that you comply with:&nbsp;The database engine's specific syntax&nbsp;The specific behaviors of the driver- Following this discussion, we queried rd-ide-team https://outsystems.slack.com/archives/C4B7WDK4N/p1720483495315379.
- R&amp;D answer:&gt; In O11 this is done with Integration Studio that is not available in ODC. My first recommendation would be to check with Data Fabric if this supported natively.
&gt;
&gt; - #rd-dna-datafabric
&gt;
&gt; IF NOT Other approach would be external libraries. how could this be done:
&gt;
&gt; - Documentation -&gt; Extend your apps with external logic using custom code
&gt; - Support: #rd-odc-extended-runtime-team
&gt;
&gt; One of those solution will most likely unblock you- We then found a ticket in which our Success team explained:&gt; - To execute stored procedures in ODC, it will be done purely in C#, and no differently than it would be done in any other C# application. The only difference is that your connection string will need to use the Private Gateway that you set up in the ODC portal. When I built a sample app to test the connection, I used a function like this:
&gt;
&gt; public string GetConnectionString(bool usePrivategateway, string sqlPath, string port, string catalog, string userName, string passWord) { var privategateway = Environment.GetEnvironmentVariable(&quot;SECURE_GATEWAY&quot;) + port; //var sqlpath = &quot;successatscaleus.database.windows.net&quot;; SqlConnectionStringBuilder builder = new SqlConnectionStringBuilder(); if (usePrivategateway) { builder.DataSource = privategateway; } else { builder.DataSource = sqlPath; } builder.TrustServerCertificate = true; builder.UserID = userName; builder.Password = passWord; builder.InitialCatalog = catalog; return builder.ConnectionString; }
&gt;
&gt; - So if I passed UsePrivategateway = True, it would use `Environment.GetEnvironmentVariable(&quot;SECURE_GATEWAY&quot;) + port` instead of me passing in the the FQDN of a SQL Server.- After sharing this information the customer reported a new error:
- https://outsystems.grafana.net/explore?schemaVersion=1&amp;panes=%7B%22ypb%22:%7B%22datasource%22:%22grafanacloud-outsystemstest-logs%22,%22queries%22:%5B%7B%22refId%22:%22A%22,%22expr%22:%22%7Bring%3D%5C%22ea%5C%22%7D%20%5Cr%5Cn%7C%3D%20%5C%22b69e0d65-862e-4c1b-9e2a-47db13c70932%5C%22%5Cr%5Cn%7C%3D%20%5C%22ELRT%5C%22%5Cr%5Cn%7C%20json%5Cr%5Cn%7C%20line_format%20%5C%22%5C%22%22,%22queryType%22:%22range%22,%22datasource%22:%7B%22type%22:%22loki%22,%22uid%22:%22grafanacloud-outsystemstest-logs%22%7D,%22editorMode%22:%22code%22%7D%5D,%22range%22:%7B%22from%22:%221721720700000%22,%22to%22:%221721720819000%22%7D}}&amp;orgId=1System.PlatformNotSupportedException: Microsoft.Data.SqlClient is not supported on this platform.OutSystems.Application.ErrorHandling.ExtensionException: System.PlatformNotSupportedException: Microsoft.Data.SqlClient is not supported on this platform. at Qe (https://proceedtech-dev.outsystems.app/GviaPoc/scripts/outsystems-runtime-core__UygwShGHvpKdNMpzMbefQ.js?UygwShGHvpKdNMpzMbe+fQ:1:14887) at go (https://proceedtech-dev.outsystems.app/GviaPoc/scripts/outsystems-runtime-core__UygwShGHvpKdNMpzMbefQ.js?UygwShGHvpKdNMpzMbe+fQ:8:59050) at https://proceedtech-dev.outsystems.app/GviaPoc/scripts/outsystems-runtime-core__UygwShGHvpKdNMpzMbefQ.js?UygwShGHvpKdNMpzMbe+fQ:8:57687 at a (https://proceedtech-dev.outsystems.app/GviaPoc/scripts/outsystems-runtime-core__UygwShGHvpKdNMpzMbefQ.js?UygwShGHvpKdNMpzMbe+fQ:1:986) at i.invoke (https://proceedtech-dev.outsystems.app/GviaPoc/scripts/outsystems-logger__DA6QJ7ofCz43gspUnGPyPg.js?DA6QJ7ofCz43gspUnGPyPg:7:26029) at r.run (https://proceedtech-dev.outsystems.app/GviaPoc/scripts/outsystems-logger__DA6QJ7ofCz43gspUnGPyPg.js?DA6QJ7ofCz43gspUnGPyPg:7:21220) at https://proceedtech-dev.outsystems.app/GviaPoc/scripts/outsystems-logger__DA6QJ7ofCz43gspUnGPyPg.js?DA6QJ7ofCz43gspUnGPyPg:7:15930 at i.invokeTask (https://proceedtech-dev.outsystems.app/GviaPoc/scripts/outsystems-logger__DA6QJ7ofCz43gspUnGPyPg.js?DA6QJ7ofCz43gspUnGPyPg:7:26647) at r.runTask (https://proceedtech-dev.outsystems.app/GviaPoc/scripts/outsystems-logger__DA6QJ7ofCz43gspUnGPyPg.js?DA6QJ7ofCz43gspUnGPyPg:7:21972)- Believing the customer was not following our recommendations correctly, we shared the ticket with our Success Team who shared:&gt; First, there is a vulnerability in the SQL Client, so make sure you get the latest version of SQL Client, which has been patched. That might be one issue you are running into.
&gt;
&gt;
&gt;
&gt; This code is basically how to execute a stored procedure in C#
&gt;
&gt; using System;
&gt;
&gt; using System.Collections;
&gt;
&gt; using System.Collections.Generic;
&gt;
&gt; using Microsoft.Data.SqlClient;
&gt;
&gt;
&gt;
&gt; namespace StoredProcedure {
&gt;
&gt;
&gt;
&gt; public class StoredProcedure : IStoredProcedure{ public List&lt;Customer&gt; Exec(string username, string password, string catalog, string value, out string connectionString, out string exception) { List&lt;Customer&gt; customers = new List&lt;Customer&gt;(); SqlConnectionStringBuilder builder = new SqlConnectionStringBuilder();var privateGateway = Environment.GetEnvironmentVariable(&quot;SECURE_GATEWAY&quot;)+&quot;,1433&quot;;builder.DataSource = privateGateway; builder.UserID = username; builder.Password = password; builder.InitialCatalog = catalog; builder.TrustServerCertificate = true; connectionString = builder.ConnectionString; exception = &quot;&quot;; try{ using (SqlConnection connection = new SqlConnection(builder.ConnectionString)) { connection.Open(); string sql = &quot;EXEC GetCustomerInfo @CutomerAge = 25&quot;; using (SqlCommand command = new SqlCommand(sql, connection)) { using (SqlDataReader reader = command.ExecuteReader()) { while (reader.Read()) { Customer customer = new Customer { id = reader.GetInt32(0), name = reader.GetString(1), age = reader.GetInt32(2), address = reader.GetString(3), salary = reader.GetDecimal(4) }; customers.Add(customer); } } } } return customers; } catch (Exception e) { connectionString = builder.ConnectionString; exception = e.ToString(); return customers; } }}}
&gt;
&gt;
&gt;
&gt; For your Secure Gateway, be sure to put whatever Port you assigned using Cloud Connector, instead of 1433 as in the sample:
&gt;
&gt; `Environment.GetEnvironmentVariable(&quot;SECURE_GATEWAY&quot;)+&quot;,1433&quot;`
&gt;
&gt;
&gt;
&gt; Here is a document that goes that a more complete explanation of using Stored Procedures.&gt; ODC_ Using External Code for Stored Procedures or Connecting to Other Databases.docx- However, they got the same error exactly:
**OS-ELRT-60008 - System.PlatformNotSupportedException: System.Data.SqlClient is not supported on this platform.****C# solution**![](https://supportoutsystems.zendesk.com/attachments/token/IFVCIaOXPum2bHPKmjUTEVO5h/?name=image.png)- Customer has **Microsoft.Data.SqlClient version 5.2.1**
- Success send the ticket back to us reporting this is a product issue.![](https://supportoutsystems.zendesk.com/attachments/token/HbDRRhmXNsEe7FGH2Mu82d9MM/?name=image.png)**IMPACT ON THE CUSTOMER**
Customer is unable to deliver this PoC to the customer which require these stored procedure.
This is highly impacting their business delivery.
Set as Sev2.**TROUBLESHOOTING STEPS &amp; WORKAROUND**
N/A**TECH DATA OR ANY OTHER RELEVANT INFO**
Ring: ea
Tenant Id: 62a1f59b-0991-4d83-b84f-fd7ca51a6682
Tenant Prefix: proceedtech
Region: eu-central-1
VPE.6BP.OAD.GLO.UYT.O5R.YZP.GTS_&lt;! do not remove this line, this will be used to the trigger_ Technical Support::Send to R&amp;D - ODC _#trigger_send_to_r&amp;d_odc !&gt;_Attachment(s):
GviaPoc.oml - https://supportoutsystems.zendesk.com/attachments/token/VzlZg1QO8k5e6xr2i71HFu4Gv/?name=GviaPoc.oml2024_07_07_13_01_17__Screenshot 2024-07-07 160000.png - https://supportoutsystems.zendesk.com/attachments/token/QyX7iVRNEm1XMKkTjO3V6sxZ1/?name=2024_07_07_13_01_17__Screenshot+2024-07-07+160000.pngODC_ Using External Code for Stored Procedures or Connecting to Other Databases.docx - https://supportoutsystems.zendesk.com/attachments/token/0zQTlrr2dqIRgHZLDZZ2evmF7/?name=ODC_+Using+External+Code+for+Stored+Procedures+or+Connecting+to+Other+Databases.docx
## 📝 RetrospectiveinfoDetails
**Ring:** ea
**System-wide impact:**&nbsp; 
**Tenant ID:** 62a1f59b-0991-4d83-b84f-fd7ca51a6682
**Tenant Prefix:** proceedtech
**Routing Error Code:** OS-ELRT
**Product Area:** -
### Impact:
n/a
### Investigation and troubleshooting findings:### Resolution:
Fix provided by R&amp;D.

See [https://outsystemsrd.atlassian.net/browse/RDINC-27529](https://outsystemsrd.atlassian.net/browse/RDINC-27529)
## Tasks performed during incident resolution:
&nbsp;
## Executive Summary
[Guidelines](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4144496679/Incident+Retrospectives+-+Playbook#STEP-3---Write-the-Executive-Summary)
## Root Causes 
[Guidelines](https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4144496679/Incident+Retrospectives+-+Playbook#STEP-1---Perform-the-Root-Cause-Analysis)

If the customer needs formal RCA, please fill out the following field with the document URL

[Please follow these instructions and place the RCA URL in the field below.](https://docs.google.com/document/d/13rXmBsOJh73nV2D6Z17SIBGBu2HOTWty5ddsvU000JM/edit#heading=h.bqxasxszr5q)

RCA URL

&lt;Place the URL of the customer RCA here if you have created one&gt;
## ⌛ Timeline[View on Rootly](https://rootly.com/account/incidents/749-odc-stored-procedure-we-have-a-connection-to-external-db-from-sql-microsoft-how-can-we-call-to-stored-procedure-and-use-it-inside-our-app)

**Date**

**Source**

**User**

**Event**
July 23  4:28 PM WESTwebRootly
created an alert via
July 23  4:28 PM WESTwebRootly
Rootly created this incident
July 23  4:28 PM WESTwebRootly
In triage date has been set to July 23  4:28 PM WEST
July 23  4:28 PM WESTwebRootly[Slack Channel](https://slack.com/app_redirect?channel=C07DLKJUTU5&amp;team=T041063TZ) has been createdJuly 23  4:28 PM WESTwebRootly
Ring: ea
System-wide impact:  
Tenant ID: 62a1f59b-0991-4d83-b84f-fd7ca51a6682
Tenant Prefix: proceedtech
Routing Error Code: OS-ELRT
Product Area: -
July 23  4:44 PM WESTwebRootly[PagerDuty Incident](https://outsystems.pagerduty.com/incidents/Q0QE620HHZTRN7) has been created.
📧 Notified Rafael Seara by email.&nbsp;&nbsp;📧 Notified Rafael Seara by email.&nbsp;&nbsp;📞 Notified Rafael Seara by phone.&nbsp;&nbsp;📱 Notified Rafael Seara by SMS.&nbsp;&nbsp;📞 Notified Rafael Seara by phone.&nbsp;&nbsp;📲 Notified Rafael Seara by push notification.  (via iPhone)July 23  4:44 PM WESTwebRootlyRafael Seara has been assigned as EngineerJuly 23  4:44 PM WESTwebRootly
Rafael Seara acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q0QE620HHZTRN7). (via Mobile)
July 23  4:51 PM WESTwebVasco Gomes
Just to share that using Data Fabric it is not possible to execute a Stored Procedure in an external connection. I just replied because it is something that it was refered in the ticket.
July 23  5:07 PM WESTwebRafael Seara
It appears that the issue is related to the Microsoft.Data.SqlClient not targeting our platform correctly. The user should follow the process outlined in point 6 of this documentation:
https://success.outsystems.com/documentation/outsystems_developer_cloud/building_apps/extend_your_apps_with_external_logic_using_custom_code/external_libraries_sdk_readme/&rdquo;Once you're finished with the code, save the project and publish it. For example, right-click Solution ClassLibrary1 and click Open in Terminal. Run command dotnet publish -c Release -r linux-x64 --no-self-contained.The published code runs in a Linux container. If your library doesn't have any runtime-specific dependencies, and to simplify the process, you can publish it without specifying the runtime: dotnet publish -c Release --no-self-contained.&rdquo;A solution for using the Microsoft.Data.SqlClient targeting our platform can be found here, in a similar issue.
https://github.com/dotnet/SqlClient/issues/1423
July 28  8:08 AM WESTwebRootlyZenDesk Event Type has been set: solvedJuly 28  8:08 AM WESTwebRootly
The Global Support team marked this incident as closed in ZenDesk.
August 5 11:42 AM WESTwebRafael Duarte
Incident has been started
August 5 11:42 AM WESTwebRootly
Pagerduty Integrations acknowledged through [PagerDuty](https://outsystems.pagerduty.com/incidents/Q0QE620HHZTRN7). (via Mobile)
August 5 11:43 AM WESTwebRafael Duarte
Incident has been resolved
August 5 11:43 AM WESTwebRafael DuarteImpact has been set: n/aAugust 5 11:43 AM WESTwebRafael DuarteResolution has been set: Fix provided by R&amp;D.
See https://outsystemsrd.atlassian.net/browse/RDINC-27529