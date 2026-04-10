---
title: What is Solution Publish and what makes it tick
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/3188228271/What+is+Solution+Publish+and+what+makes+it+tick
confluence_space: RCP
confluence_page_id: 3188228271
last_synced: 2026-04-09
owner: Process Engineering
---

# What is Solution Publish and what makes it tick

# Before you start
Solution Publish is a broad topic, that needs a massive amount of effort to be fully documented. As such, this is a continuously work in progress document. So, expect some information to be under works, and feel free to directly contribute with your knowledge by editing the document and providing feedback.
# Ultimate goal
*Ensure that whoever needs to deal with Solution Publish related tasks (being those development or support cases tasks), from Global Support to R&amp;D, will have a lot of information handy and in an easy to find place.*
# Table of contents16falsedefaultBefore you start|Ultimate goal|Table of contentslisttrue# Dealing with Solution Publish support cases
You should always have this Resource Index document in mind when requesting troubleshoot information to the customer.

Also see FAQ Troubleshooting Solution Publish for FAQ style on how to troubleshoot Solution Publish.
# Overview: what&rsquo;s a Solution
A solution is a way to compile a group of modules that later can be published together through Service Center (SC). LifeTime uses this feature when staging applications into environments. Here&rsquo;s an [example in our documentation](https://success.outsystems.com/Support/Troubleshooting/Application_lifecycle/Deploy_applications_through_Service_Center).
## What is a OSP file
OSP stands for Outsystems Solution Pack and basically is a solution of different modules/extensions (possibly from different applications).

*Info taken from [here](https://www.outsystems.com/forums/discussion/52797/differences-between-oml-and-oap-and-osp-file/#:~:text=OSP%20stands%20for%20Outsystems%20Solution,(possibly%20from%20different%20applications).).

An OSP is just a zip file that you can open with any application capable of opening zip files. The contents of these files are just a manifest file containing some meta information regarding the solution, and a folder containing all modules OML files included in the solution.

You can also use the [OSPTool](https://success.outsystems.com/Documentation/11/Setup_and_maintain_your_OutSystems_infrastructure/Setting_Up_OutSystems/Unattended_Installation_and_Upgrade/Solution_Pack_Tool_(OSPTool)_Command_Line_Reference) to upload and/or publish them, or directly do it in SC.
## What is a Version
For each solution you can create a new version anytime you want to save a snapshot of the current state of all modules included in the solution. Later, you&rsquo;ll be able to publish or download the OSP file for the &ldquo;running version&rdquo; of the solution, or for a version previously created.
## Components vs Dependencies
Components of a solution are modules that were explicitly included in the solution.

Dependencies are modules identified by the platform as dependencies of the components of the solution, which weren&rsquo;t explicitly added to the solution.

When you download an OSP file from a version you can select if you want to include dependencies in the downloaded file or not.
## Permissions
Allow to define what each user can do in the solution. Permission levels are:

- 
Read Only

- 
Download

- 
Publish

- 
Full Control

## What to expect from Solution Publish
Implemented partially on SC and partially on Compiler Service

Includes:

- 
Parallelization of tasks &ldquo;Compiling modules&rdquo;, &ldquo;Preparing Deploy&rdquo; and &ldquo;Deploying&rdquo;

- 
Two Step Support

- 
Module Level Security Validations

- 
Modules Upgrade (via SS)

- 
Process Impact Analysis

- 
Module Deployment

- 
Setup Database Catalogs

- 
Native Application Build

- 
Incompatible Reference Handling

- 
Interactive Configuration (DB)

- 
Licence Validations (AO consumption)

- 
Solution Unpack

- 
Refresh Module References

- 
Move Module Between Catalogs

- 
Compile and Publish Extensions

- 
Upgrade DB Model

- 
Associate Module Dependencies

- 
User Abortable

Does not include:

- 
Progressive Recovery

- 
Ex: a solution fails at a specific step, the user fixes the root cause of the failure, and the publication resumes from the failed step (without needing to reperform steps)

- 
Fast Error Handling

- 
Ex: current Solution Publish has some scenarios where errors may happen, and the publication gets aborted only at a later time

- 
Pluggable Code Generation

- 
Ex: customers are able to perform external integration with solution publication using web hooks

- 
Skip Unnecessary Steps

- 
Ex: publication doesn&rsquo;t try to deploy modules with no changes

# Deep dive: Solution Publish steps
The solution publish process is organized in several steps. This is what a customer sees after publishing a solution, and represents the several solution publish steps. In the sections there&rsquo;s an explanation on what each step does.
## 0. Preparation
- 
Solution Publish logic starts by locking the solution, meaning this solution cannot be published until the current publish finishes. More on this mechanism [below](#Solution-locks-and-unlocks).

- 
Runs `Security_CheckSolution` action, that iterates over the solution components and checks the permissions of the current user for each component and for the overall solution

- 
Runs `SolutionPublishPlanGetOrCreate` action, that creates a solution publish plan. This is a database entity that stores the state, start instant, end instant, the pending command, if it&rsquo;s a lifetime plan and a summary message. This information is then used to run `ContinuePublishAfterConfig` action inside `Solution_ConfirmationCallback` that continues the publish process when the platform needs to ask more information to the user in the middle of a publish.

## 1. Upgrading
Runs in `Solution_Upgrade_Logic_Go/Preparation` (interface screen preparation action).

- 
Upgrades if it&rsquo;s an external pack and if the pack schema version is different from the current platform installation (`SolutionsSchemaVersion` record in `OSSYS_PARAMETER` table)

- 
Upgrade runs `SolutionPackUpgrade` compiler service action, which upgrades to be compatible with the new solution schema, if needed

- 
An [external pack](#External-Pack) is a solution publish triggered by an upload of an OSP file (rather than publishing it from SC from an already existent solution/version). In the code, this is checked using `PackUID &lt;&gt; &quot;&quot;`

- 
For each extension in the solution, check if there&rsquo;s any that doesn&rsquo;t have any database connection configured in that factory and that should have one. If so, it will ask the user for such configuration.

- 
See if it needs multiple databases configuration and may ask the user for the configuration

- 
Checks if the factory has the [Multiple Database Catalogs (MDC)](https://success.outsystems.com/support/enterprise_customers/maintenance_and_operations/multiple_database_catalogs_and_schemas/) feature available

- 
If it&rsquo;s an external pack,: for each espace in the solution, it will ask for the catalog configuration if the factory has more than 1 catalog OR if it&rsquo;s possible to choose a catalog for that espace. (from the comments, choices are presented unless the manifest contains no catalog info and single catalog environment)

- 
If it&rsquo;s not an external pack, applies a logic similar to the one above (but it&rsquo;s done in a different action with some intermediate differences)

Prompt for extension database connection example

Prompt for MDC configuration example
## 2. Uploading
Runs in `Solution_Publish_Logic_Go_Preparation` action:

- 
Unpacks and uploads solutions if it&rsquo;s an external pack.

- 
Skips upload if it&rsquo;s not an external pack.

- 
If the solution didn&rsquo;t come from LT, runs `CheckPartialApplicationSolutionPublish` over the unpacked solution. This action &ldquo;Validates if solution includes applications that are not complete, those are not valid in docker&rdquo;.

- 
Runs `Solution_Upload` action:

- 
Checks user permissions. Depending if the asset being uploaded is an app or a solution (checks this using `SolutionPublishAsset` static entity), it will check users permissions for that application or for that solution.

- 
For each application:

- 
Runs `App_CreateOrUpdate`, which will create the application entry in the DB in case it doesn&rsquo;t exist, or updates it accordingly.

- 
If it has an URL set in the manifest file, then sets `ApplicationURL` in `ossys_App_Parameter`

- 
TODO/Note: I did not find any actual usage of this parameter. 

- 
Creates or updates forge app in the database, if it is a forge app

- 
Uploads each espace and extension to the DB. Each upload may be skipped if not needed.

- 
Ends solution publish if it&rsquo;s upload only

## 3. Verifying
Runs within `Solution_Compile` action (first compilation step):

- 
Before starting the compilation phase, runs `Solution_ValidatePlatformComponentsVersions` which checks the platform server version, SC version and deployment controller binaries version 

- 
Run `Security_CheckSolution`, which checks user privileges

- 
If it&rsquo;s trying to skip the checks or the compilation or if it&rsquo;s a RetryPlan publish: it tries to restore the previously ran solution publish. Continue if it&rsquo;s not, or if it couldn&rsquo;t restore the data.

- 
Fetched solution references details to later use and ignores hidden modules

- 
Verify security permissions of all modules.

## 4. Upgrading Modules
- 
Runs in `Solution_Compile` action

- 
Upgrades Active components that:

- 
Have a different LUV version than the platform

- 
OR the module is an espace

- 
AND `Espace_NeedsRefreshReferences(EspaceId:IntegerToIdentifier(SolutionModules.Current.ModuleDetails.ComponentId), SolutionPublish_OnlyRefreshIfBrokenReferencesParam.Value)`, based on:

- 
OnlyRefreshIfBrokenReferences is related to a setting that can be set via Factory Configuration that changes the refreshes to be only on potential broken references, reducing the amount of refreshes drastically (this was seamlessly copied from Rosado)

- 
Internally, what this method does is run a query joining the tables `OSSYS_ESPACE`, `OSSYS_ESPACE_RUNNING_PROD_VER`, `OSSYS_EXTENSION`, `OSSYS_ESPACE_REFERENCE` and `OSSYS_MODULE_PUBLICELEMENT` to compare the reference that the espace has of a certain module with the currently published version of that module. If it&rsquo;s different means it needs refreshing

- 
The comparison is made using the `COMPATIBILITY_SIGNATURE_HASH` or the `FULL_SIGNATURE_HASH`, depending if the OnlyRefreshIfBrokenReferences is `true` or `false`, respectively

- 
AND `ServerCapabilities_CanRefreshRefsInSolutionPublish`, which is only true if the machine purpose is set to Development (more about this [here](https://success.outsystems.com/Documentation/11/Setup_and_maintain_your_OutSystems_infrastructure/Setting_Up_OutSystems/Configure_your_OutSystems_environment))

- 
Run `Solution_CreateBuild` action, that creates the necessary objects to start building the artifacts in the compiler service

- 
PrepareWorkspace foreach active espace. (`PrepareEspaceCompilationWorkspace` action from compiler service). At this phase the platform checks if it can reuse past espace compilations to avoid compiling the espace again in the upcoming publish steps. Compilations executed in the context of solution publish are stored in folders created uniquely for this solution publication under the `share` folder for each espace, with the following naming `[espaceName].[SolutionId]`. Folders need to be unique to avoid issues with concurrent publications (namely using 2-step).

- 
For eSpaces that are not part of the solution, but are a reference, it tries to use the compiled running version for that espace. CompilerService checks for an existing share folder with the same name as the espace, and if it exists, it copies its contents to a newly created folder (using the naming described above).

- 
For solution components, if it&rsquo;s compiling the espace&rsquo;s running version and the espace is marked as consistent, it tries to reuse the previous results.

- 
To check if we&rsquo;re compiling the running version, it compares the `VERSION_ID` column of `OSSYS_ESPACE` with the selected VersionId to be published

- 
To check if the espace is consistent, it fetches the value in the `IS_CONSISTENT` column of `OSSYS_ESPACE` for that espace. This is a flag that should change every time the contents in the share folder are in sync with what is actually running in IIS, or when they may no longer be in sync

- 
Reusage is done based on the same principles as before. CompilerService checks for an existing share folder with the same name as the espace, and if it exists, it copies its contents to a newly created folder (using the naming described above)

- 
Check Espace Move Tables. If so, for each active espace that has a different database catalog configured than the one of the currently deployed version, runs `CheckMatchingTables`.

- 
This means that for each active espace it will look for matching tables in the destination database.

- 
If no match was found, the espace will be added to a list of `EspacesForMoveWithoutMatchingTables` for later use. Tables won&rsquo;t &ldquo;match&rdquo; if:

- 
The entity requires a physical table (this is based on a [hardcoded system tables list](https://github.com/OutSystems/Platform/blob/50e0add0994cc277bcb9af62f406255acc2c34d2/HubServer/compiler/AbstractEntity.cs#L107-L113) - almost all Entities require a physical table, including system ones)

- 
AND espace is not a library

- 
AND a table with the expected table name was not found

- 
If `NeedsConfirmationToContinueForDataMove and CanAskQuestions`, it will stop the publish here.

- 
The `NeedsConfirmationToContinueForDataMove` means that an espace with tables to move was identified.

## 5. Impact Analysis
- 
This step happens already in the new C# orchestration (under the `SolPublishService`[ ](https://github.com/OutSystems/Platform/blob/d678e758147051ddfe43feeb132ca4394b502955/HubServer/CompilerService/Services/SolutionPublish/SolPublishService.cs)and `SolutionPublication` classes [here](https://github.com/OutSystems/Platform/blob/d678e758147051ddfe43feeb132ca4394b502955/HubServer/CompilerService/Services/SolutionPublish/SolPublishService.cs#L195-L208), [here ](https://github.com/OutSystems/Platform/blob/d678e758147051ddfe43feeb132ca4394b502955/HubServer/CompilerService/Services/SolutionPublish/SolPublishService.PublishLogic.cs#L40-L65)and [here](https://github.com/OutSystems/Platform/blob/d678e758147051ddfe43feeb132ca4394b502955/HubServer/CompilerService/Services/SolutionPublish/Publication/SolutionPublication.PrepareEspaces.cs#L16-L20)).

- 
Previously to 11.26.0 for on-prem customers, and 11.23.1 for cloud, this would be executed through SC&rsquo;s `Solution_Compile` action.

- 
This step will show in the solution publish output screen only when not skipped.

- 
This step is skipped when it&rsquo;s running a 2-stage deployment and the `BPT.ImpactAnalysis.SkipFirstStageImpactAnalysis` platform setting is `true`. This setting is `false` by default. For each espace, impact analysis checks:

- 
[https://success.outsystems.com/Documentation/11/Developing_an_Application/Use_Processes_(BPT)/Upgrade_Processes](https://success.outsystems.com/Documentation/11/Developing_an_Application/Use_Processes_(BPT)/Upgrade_Processes)

- 
If there is any active process definitions for that espace, by querying the `OSSYS_BPM_PROCESS_DEFINITION` [here](https://github.com/OutSystems/Platform/blob/d678e758147051ddfe43feeb132ca4394b502955/HubServer/Server/Services/ApplicationRuntimeOperations/ApplicationRuntimeOperations.Infrastructure/Database/DBProcess.cs#L401-L412).

- 
Happens in `ProcessesImpactAnalysis.cs` `Analyse()` method [here](https://github.com/OutSystems/Platform/blob/d678e758147051ddfe43feeb132ca4394b502955/HubServer/compiler/ImpactAnalysis/ProcessesImpactAnalysis.cs#L44-L78).

- 
Runs with:

- 
For each process in the espace, if it&rsquo;s not in ProtectedESpaces (espaces that can't be opened in SS except in debug or support mode, i.e. ServiceCenter, full list can be found [here](https://github.com/OutSystems/OutSystems.RuntimeCommon/blob/master/src/OutSystems.RuntimeCommon/Constants.cs)) runs `CompareProcessScopeElements`.

- 
If it detect relevant changes in each process, or if there are GraphChanges locks the process definition.

- 
Detects which processes will suspend, for each process instance checks and generates warnings to output to the user (and logs them) based on:

- 
if old suspensions still apply

- 
New inputs

- 
Inputs that changed type

- 
New input dependencies

- 
New activity outputs

- 
Changed activity outputs

- 
New activity output dependencies

- 
Generates scripts to suspend the needed processes

- 
If Impact Analysis produces any warning or error and solution publish `CanAskQuestions` [is set to true](#CanAskQuestions-parameter), then the publication stops here and prompts the user for confirmation.

Impact Analysis stopping for confirmation example

Impact Analysis runs without stopping the publication example
## 6. Preparing Extensions
- 
This step happens already in the new C# orchestration (under the `SolPublishService`[ ](https://github.com/OutSystems/Platform/blob/d678e758147051ddfe43feeb132ca4394b502955/HubServer/CompilerService/Services/SolutionPublish/SolPublishService.cs)and `SolutionPublication` classes [here](https://github.com/OutSystems/Platform/blob/d678e758147051ddfe43feeb132ca4394b502955/HubServer/CompilerService/Services/SolutionPublish/SolPublishService.cs#L213), [here ](https://github.com/OutSystems/Platform/blob/d678e758147051ddfe43feeb132ca4394b502955/HubServer/CompilerService/Services/SolutionPublish/SolPublishService.PublishLogic.cs#L29-L38)and [here](https://github.com/OutSystems/Platform/blob/d678e758147051ddfe43feeb132ca4394b502955/HubServer/CompilerService/Services/SolutionPublish/Publication/SolutionPublication.PrepareExtensions.cs)).

- 
Previously to 11.26.0 for on-prem customers, and 11.23.1 for cloud, this would be executed through SC&rsquo;s `Solution_Compile` and `Extension_Publish` actions.

- 
For each active extension, Publishes Extensions

- 
May be skipped if it detects that the extension was already deployed. A message saying it was skipped will output to the user saying &ldquo;Extension 'X' is already deployed.&ldquo;. Based on these rules:

- 
`VersionId` to be published is the same that&rsquo;s currently published

- 
No needed Database configuration

- 
Verified through `OSSYS_ASYNC_OP_LOGICALDATABASE`

- 
Extension was published after Service Center&rsquo;s publication

- 
After each publication:

- 
Outputs a &ldquo;Missing Configuration&rdquo; when it detects not all database connections needed for this extension were configured

- 
Recalculates licensing usage limits

- 
If any errors happen it ends the solution publish

## 7. Preparing Database
- 
This step happens already in the new C# orchestration (under the `SolPublishService`[ ](https://github.com/OutSystems/Platform/blob/d678e758147051ddfe43feeb132ca4394b502955/HubServer/CompilerService/Services/SolutionPublish/SolPublishService.cs)and `SolutionPublication` classes [here](https://github.com/OutSystems/Platform/blob/d678e758147051ddfe43feeb132ca4394b502955/HubServer/CompilerService/Services/SolutionPublish/SolPublishService.cs#L220), [here ](https://github.com/OutSystems/Platform/blob/d678e758147051ddfe43feeb132ca4394b502955/HubServer/CompilerService/Services/SolutionPublish/SolPublishService.PublishLogic.cs#L90-L100)and [here](https://github.com/OutSystems/Platform/blob/d678e758147051ddfe43feeb132ca4394b502955/HubServer/CompilerService/Services/SolutionPublish/Publication/SolutionPublication.PrepareEspaces.cs#L33-L70)).

- 
Previously to 11.26.0 for on-prem customers, and 11.23.1 for cloud, this would be executed through SC&rsquo;s `Solution_Compile` and `Espace_UpdateMetamodel` actions.

- 
Updates eSpaces Metamodel

- 
For each active espace:

- 
Runs `Espace_UpdateMetamodel` action:

- 
Checks user permissions

- 
Runs `UpdateEspaceMetamodel` compiler method

- 
If is Self User Provider and it has no tenants, creates one (by default there&rsquo;s always a tenant with the same name as the espace)

- 
Sets the espace pending version in `OSSYS_ESPACE` to the version being published

- 
If any errors happen it ends the solution publish

- 
Note: this does nothing in the espaces' database. It&rsquo;s just generating the necessary scripts that will run during the deployment phase

## 8. Associating Dependencies
- 
This step happens already in the new C# orchestration (under the `SolPublishService`[ ](https://github.com/OutSystems/Platform/blob/d678e758147051ddfe43feeb132ca4394b502955/HubServer/CompilerService/Services/SolutionPublish/SolPublishService.cs)and `SolutionPublication` classes [here](https://github.com/OutSystems/Platform/blob/d678e758147051ddfe43feeb132ca4394b502955/HubServer/CompilerService/Services/SolutionPublish/SolPublishService.cs#L227), [here ](https://github.com/OutSystems/Platform/blob/d678e758147051ddfe43feeb132ca4394b502955/HubServer/CompilerService/Services/SolutionPublish/SolPublishService.PublishLogic.cs#L102-L111)and [here](https://github.com/OutSystems/Platform/blob/d678e758147051ddfe43feeb132ca4394b502955/HubServer/CompilerService/Services/SolutionPublish/Publication/SolutionPublication.PrepareEspaces.cs#L72-L84)).

- 
Previously to 11.26.0 for on-prem customers, and 11.23.1 for cloud, this would be executed through SC&rsquo;s `Solution_Compile` action.

- 
For each active espace runs `AssociateEspaceDependencies` in compiler service:

- 
If the user provider changed, apply the change in DB

- 
If `IsActive` is false, multitenant changed or espace kind changed:

- 
Updates `IsActive`, `isMultiTenant` and `EspaceKind`

- 
Deletes metamodel references of removed espace&rsquo;s Entities

- 
Adds metamodel references of new espace&rsquo;s Entities

## 9. Compiling Modules
- 
This step happens already in the new C# orchestration (under the `SolPublishService`, `SolutionPublication` and `BuildServices` classes [here](https://github.com/OutSystems/Platform/blob/d678e758147051ddfe43feeb132ca4394b502955/HubServer/CompilerService/Services/SolutionPublish/SolPublishService.cs#L235), [here ](https://github.com/OutSystems/Platform/blob/d678e758147051ddfe43feeb132ca4394b502955/HubServer/CompilerService/Services/SolutionPublish/Publication/SolutionPublication.PrepareEspaces.cs#L86-L104)and [here](https://github.com/OutSystems/Platform/blob/d678e758147051ddfe43feeb132ca4394b502955/HubServer/Server/Services/BuildService/Build.Application/BuildService.cs#L661-L717)).

- 
Note that this code is mainly shared with the Progressive Upgrades and Deploy All features

- 
Previously to 11.26.0 for on-prem customers, and 11.23.1 for cloud, this would be executed through SC&rsquo;s `Solution_Compile` action.

- 
At the very beginning of the compilation logic, Compiler Service starts by compiling info related to the modules included in the solution:

- 
Fetches all `OSSYS_APPLICATION`, `OSSYS_ESPACE` and `OSSYS_EXTENSION` metadata

- 
Fetches the most up to date espace names between `OSSYS_ESPACE` and current OML name

- 
For each active espace:

- 
Check user permissions for current espace

- 
Run Compiler Service&rsquo;s `BuildOmlWithEmptyProxiesTask` 

- 
Starts by compiling info about the current espace direct and indirect producers

- 
We call this task with `skipOml` [set to true](https://github.com/OutSystems/Platform/blob/88de1e9f47a3e09844744012273360e832b2337f/HubServer/Server/Services/BuildService/Build.Application/BuildService.cs#L699). Meaning that it will load this data from [Build cached info](https://github.com/OutSystems/Platform/blob/88de1e9f47a3e09844744012273360e832b2337f/HubServer/Server/Services/BuildService/Build.Application/Tasks/CollectEspaceProducersInformationTask.cs#L155) instead of using the OML data

- 
Note: [UseNewCompilerAPIs](https://github.com/OutSystems/Platform/blob/88de1e9f47a3e09844744012273360e832b2337f/HubServer/Server/Services/BuildService/Build.Application/ProxyCompiler.cs#L44-L56) evaluates to false (based on local *Server_UseNewCompilerAPIs* Feature Toggle). This looks like a *MyFriday's *project, that never went ahead.

- 
Loads espace OML

- 
Compiles espace with `ForEmptyProxies` configuration, meaning the following configurations are set:

- 
`EmptyProxies` is true

- 
`RegisterPluginUsage` is true

- 
`SkipDBConsistencyMessages` is true

- 
This step generates the code for each of the modules while also generating an empty proxy for every producer of each module. Supposing we have a solution with a module A consuming modules B and C, we will generate the code for A plus two empty proxies (for both producers B and C). The generated code for module A will not reference the producer&rsquo;s code directly at this point. Instead, it will reference the proxies (which are empty at this stage, but will later on be regenerated and call the producers code [see [Compile Proxies](#)]). The empty proxies creation is primarily due to the fact that we support circular dependencies. Without it, in a scenario where A consumes B and B consumes A, we wouldn&rsquo;t be able to compile A without B and vice-versa. By creating an indirection with the proxies, we are able to surpass this chicken-egg problem. More details [here](https://docs.google.com/document/d/1CiFrWkQEW87zBxdQ9FffjoWYyWFBZDVupK3UkVmVxwE/edit#).

- 
Create or update `OSSYS_ESPACE_RUNTIME` database table for that espace

- 
Set `USERPROVIDER_VERSION_ID` to null

- 
Set `outdatedUserProvider` to false

- 
Update in-memory espace info on direct and indirect producers using cached info from the `BuildOmlWithEmptyProxiesTask` run

## 10. Compiling Dependencies
- 
This step happens already in the new C# orchestration (under the `SolPublishService`, `SolutionPublication` and `BuildServices` classes [here](https://github.com/OutSystems/Platform/blob/d678e758147051ddfe43feeb132ca4394b502955/HubServer/CompilerService/Services/SolutionPublish/SolPublishService.cs#L235), [here ](https://github.com/OutSystems/Platform/blob/d678e758147051ddfe43feeb132ca4394b502955/HubServer/CompilerService/Services/SolutionPublish/Publication/SolutionPublication.PrepareEspaces.cs#L86-L104)and [here](https://github.com/OutSystems/Platform/blob/d678e758147051ddfe43feeb132ca4394b502955/HubServer/Server/Services/BuildService/Build.Application/BuildService.cs#L734-L780)).

- 
Note that this code is mainly shared with the Progressive Upgrades and Deploy All features

- 
Previously to 11.26.0 for on-prem customers, and 11.23.1 for cloud, this would be executed through SC&rsquo;s `Solution_Compile` action.

- 
For each active espace:

- 
Check user permissions for current espace

- 
Run Compiler Service&rsquo;s `BuildOmlProxiesTask`

- 
Starts by compiling info about the current espace direct and indirect producers

- 
We call this task with `skipOml` [set to true](https://github.com/OutSystems/Platform/blob/88de1e9f47a3e09844744012273360e832b2337f/HubServer/Server/Services/BuildService/Build.Application/BuildService.cs#L758). Meaning that it will load this data from [Build cached info](https://github.com/OutSystems/Platform/blob/88de1e9f47a3e09844744012273360e832b2337f/HubServer/Server/Services/BuildService/Build.Application/Tasks/CollectEspaceProducersInformationTask.cs#L155) instead of using the OML data

- 
Note: [UseNewCompilerAPIs ](https://github.com/OutSystems/Platform/blob/88de1e9f47a3e09844744012273360e832b2337f/HubServer/Server/Services/BuildService/Build.Application/ProxyCompiler.cs#L70-L75)evaluates to false (based on local *Server_UseNewCompilerAPIs* Feature Toggle). This looks like a *MyFriday's *project, that never went ahead.

- 
Compiles espace with `ForProxies` configuration, meaning the following configurations are set:

- 
`ProxiesOnly` is true

- 
At this point we already have the code generated for all modules of the solution but we are still left with an empty proxy for every producer of each module. This step basically fetches the code of each of the producers into the consumers &lsquo;bin&rsquo; directory and regenerates the proxies so they now call the producers code.

- 
If espace has a User Provider set, and is not itself:

- 
Create or update `OSSYS_ESPACE_RUNTIME` with User Provider version ID

- 
Set `outdatedUserProvider` to false

## 11. Gathering Dependencies
- 
This step happens already in the new C# orchestration (under the `SolPublishService`, `SolutionPublication` and `BuildServices` classes [here](https://github.com/OutSystems/Platform/blob/d678e758147051ddfe43feeb132ca4394b502955/HubServer/CompilerService/Services/SolutionPublish/SolPublishService.cs#L235), [here ](https://github.com/OutSystems/Platform/blob/d678e758147051ddfe43feeb132ca4394b502955/HubServer/CompilerService/Services/SolutionPublish/Publication/SolutionPublication.PrepareEspaces.cs#L86-L104)and [here](https://github.com/OutSystems/Platform/blob/d678e758147051ddfe43feeb132ca4394b502955/HubServer/Server/Services/BuildService/Build.Application/BuildService.cs#L797-L852)).

- 
Note that this code is mainly shared with the Progressive Upgrades and Deploy All features

- 
Previously to 11.26.0 for on-prem customers, and 11.23.1 for cloud, this would be executed through SC&rsquo;s `Solution_Compile` action.

- 
For each active espace:

- 
Check user permissions for current espace

- 
Run Compiler Service&rsquo;s `PullEspaceProducersTask`:

- 
Loads and maps publishing espaces dependencies

- 
Copies needed dependency files into the espaces' share folders

- 
Reference WIP document: (WIP) How pull espace producers works

- 
If previous task was successful

- 
When [CDNCLientRuntimeVersioningEnabled](https://outsystemsrd.atlassian.net/l/cp/V3JSqi08) and module being compiled is Reactive, execute `PostProcessManifestResourcesTask`. This will rename files with suffixes according to the CDN feature rules, which will ensure its cache gets updated

- 
Store build results under the `BAR` folder ([Build Artifact Repository](https://outsystemsrd.atlassian.net/wiki/spaces/CloudKB/pages/1256915742/Flexible+Upgrades+Knowledge+Transfer#The-BAR-Repository))  

- 
Add solution to the recent item list in SC:

- 
updates `OSSYS_RECENT_ITEM` table, that records the most recent actions done by the users (e.g. solution publish, editing a module/solution)

- 
Update `OSSYS_SOLUTION_PUBLISHING` table: 

- 
Add an entry with the details (e.g. name, id) of each module being published in the solution

- 
This information is used in:

- 
Solution_Confirmation screen to know what espaces have a &ldquo;data moving problem&rdquo;

- 
Several places during the publish logic to restore the list of modules to deploy when/after stopping for user interaction

- 
Compilation considered done in this step

## 12. Preparing Deploy
- 
This step happens already in the new C# orchestration (under the `SolPublishService`, `SolutionPublication` classes [here](https://github.com/OutSystems/Platform/blob/d678e758147051ddfe43feeb132ca4394b502955/HubServer/CompilerService/Services/SolutionPublish/SolPublishService.cs#L276-L282), [here ](https://github.com/OutSystems/Platform/blob/d678e758147051ddfe43feeb132ca4394b502955/HubServer/CompilerService/Services/SolutionPublish/SolPublishService.PublishLogic.cs#L122-L135)and [here](https://github.com/OutSystems/Platform/blob/d678e758147051ddfe43feeb132ca4394b502955/HubServer/CompilerService/Services/SolutionPublish/Publication/SolutionPublication.DeployModules.cs#L105-L207)).

- 
Previously to 11.26.0 for on-prem customers, and 11.23.1 for cloud, this would be executed through SC&rsquo;s `Solution_Deploy` action.

- 
When running a 2 stage deploy, if this step run already, restore the deploymentIds generated by previous Prepare Deploy step, and skip the already run logic.

- 
For each active espace:

- 
Start by loading the OML header into memory. Used for IPP (Intellectual Property Protection) validation and update the `OSSYS_ESPACE_PRODUCTINFO` database table.

- 
Validate IPP license limits if OML header contains an Activation Code, except for system components

- 
Validate License limits except for system components

- 
Validate a catalog (MDC) is associated with the module being published

- 
Update the `OSSYS_ESPACE_PRODUCTINFO` database table

- 
Execute `DeployPrepareDeployEspace` Compiler Service method:

- 
Run `CreateModuleDeployPackageTask` or `CreateAppDeployPackageTask`:

- 
This is where we pack everything the app needs in order to be deployed (binaries, static resources, java script files, etc.)

- 
Update `OSSYS_ESPACE_RUNTIME` database table flags - these are used to present warnings in the SC module page. Set module as:

- 
Not having pending configurations to be applied

- 
Not being pending compilation

- 
Not having pending security settings to be applied

- 
Update `OSSYS_SOLUTION_PUBLISHING` table: 

- 
Add an entry with the details (e.g. name, id) of each module being published in the solution

- 
This information is used in:

- 
Solution_Confirmation screen to know what espaces have a &ldquo;data moving problem&rdquo;

- 
Several places during the publish logic to restore the list of modules to deploy when/after stopping for user interaction

- 
If licensing errors occurred on previous steps, it aborts the publication.

- 
If solution is being published in 2 stage mode:

- 
Update `OSSYS_SOL_PUB_COMP` table. So we have the needed information to be later reused once the publication is resumed (stores the deploymentIds generated by Prepare Deploy).

- 
Prompt the user for confirmation to continue de publication.

## 13. Impact Analysis
- 
This step happens already in the new C# orchestration (under the `SolPublishService`[ ](https://github.com/OutSystems/Platform/blob/d678e758147051ddfe43feeb132ca4394b502955/HubServer/CompilerService/Services/SolutionPublish/SolPublishService.cs)and `SolutionPublication` classes [here](https://github.com/OutSystems/Platform/blob/d678e758147051ddfe43feeb132ca4394b502955/HubServer/CompilerService/Services/SolutionPublish/SolPublishService.cs#L276-L282), [here](https://github.com/OutSystems/Platform/blob/d678e758147051ddfe43feeb132ca4394b502955/HubServer/CompilerService/Services/SolutionPublish/SolPublishService.PublishLogic.cs#L157-L166), [here ](https://github.com/OutSystems/Platform/blob/d678e758147051ddfe43feeb132ca4394b502955/HubServer/CompilerService/Services/SolutionPublish/SolPublishService.PublishLogic.cs#L66-L88)and [here](https://github.com/OutSystems/Platform/blob/d678e758147051ddfe43feeb132ca4394b502955/HubServer/CompilerService/Services/SolutionPublish/Publication/SolutionPublication.PrepareEspaces.cs#L22-L31)).

- 
Previously to 11.26.0 for on-prem customers, and 11.23.1 for cloud, this would be executed through SC&rsquo;s `Solution_Deploy` action.

- 
This step will show in the solution publish output screen only when not skipped.

- 
Runs only when in `TwoStepMode` and didn&rsquo;t run for this publish yet.

- 
This is similar to the previous Impact Analysis, but instead of running the `ImpactAnalysis` compiler method, it will run `CompileOmlImpactAnalysisOnlyWithScripts`. This means that scripts to change the database will be generated and needed DB changes will be performed in the end if there are no errors

- 
If Impact Analysis produces any warning or error, then the publication stops here and prompts the user for confirmation.

## 14. Deploying
- 
This step happens already in the new C# orchestration (under the `SolPublishService`[ ](https://github.com/OutSystems/Platform/blob/d678e758147051ddfe43feeb132ca4394b502955/HubServer/CompilerService/Services/SolutionPublish/SolPublishService.cs)and `SolutionPublication` classes [here](https://github.com/OutSystems/Platform/blob/d678e758147051ddfe43feeb132ca4394b502955/HubServer/CompilerService/Services/SolutionPublish/SolPublishService.cs#L276-L282), [here](https://github.com/OutSystems/Platform/blob/d678e758147051ddfe43feeb132ca4394b502955/HubServer/CompilerService/Services/SolutionPublish/SolPublishService.PublishLogic.cs#L170), [here](https://github.com/OutSystems/Platform/blob/d678e758147051ddfe43feeb132ca4394b502955/HubServer/CompilerService/Services/SolutionPublish/SolPublishService.PublishLogic.cs#L182-L295), [here ](https://github.com/OutSystems/Platform/blob/d678e758147051ddfe43feeb132ca4394b502955/HubServer/CompilerService/Services/SolutionPublish/Publication/SolutionPublication.DeployModules.cs#L210-L237)and [here](https://github.com/OutSystems/Platform/blob/d678e758147051ddfe43feeb132ca4394b502955/HubServer/CompilerService/Services/SolutionPublish/Publication/SolutionPublication.DeployModules.cs#L239-L313)).

- 
Previously to 11.26.0 for on-prem customers, and 11.23.1 for cloud, this would be executed through SC&rsquo;s `Solution_Deploy` action.

- 
Except for system components: Validate that the whole solution fits in the available SU/AO

- 
// From here on, we will update the database so we enter the all or nothing section

- 
Run `SolutionUpdateDBSecondStage` compiler service method. In short, for each espace in the solution run their previously generated DB script files

- 
Abort publish on errors

- 
For each active extension run `PublishExtension_SwitchPublishedVersion` Compiler Service method. This code updates the published version in the `OSSYS_EXTENSION` database table

- 
For each active espace:

- 
ensure that espace name is updated in `OSSYS_ESPACE`

- 
run `DeployFinalizeDeployEspaceSolution` Compiler Service method that will execute `FinalizeDeploymentTask`

- 
run `MarkApplicationAsChangedAfterEspacePublish` Compiler Service method (relevant for forge application)

- 
Updates license limits consumption through `ActivationRefreshLicensedFeatures`

- 
Run `RefreshISAPIFilters` Compiler Service

- 
For each successfully deployed espace run `UpdateReferencesMetaModel` Compiler Service method

- 
At this point, we have already deployed all espaces in the solution, and we have updated their metadata in the database. So, we're able to carry out the next step:

Here, we update the information about outdated/old references/user providers of the espaces that have been successfully deployed.

## 15. Solution update and cleanup (wrap-up logic)
- 
This step happens already in the new C# orchestration (under the `SolPublishService`[ ](https://github.com/OutSystems/Platform/blob/d678e758147051ddfe43feeb132ca4394b502955/HubServer/CompilerService/Services/SolutionPublish/SolPublishService.cs)and `SolutionPublication` classes [here](https://github.com/OutSystems/Platform/blob/d678e758147051ddfe43feeb132ca4394b502955/HubServer/CompilerService/Services/SolutionPublish/SolPublishService.cs#L308) and [here](https://github.com/OutSystems/Platform/blob/d678e758147051ddfe43feeb132ca4394b502955/HubServer/CompilerService/Services/SolutionPublish/Publication/SolutionPublication.SolutionUpdateAndCleanup.cs)).

- 
Previously to 11.26.0 for on-prem customers, and 11.23.1 for cloud, this would be executed through SC&rsquo;s `Solution_Deploy` action.

- 
For each module that exists run `CheckConsumerReferencesAndUpdateRuntime` Compiler Service method

- 
Ensures consumers of published modules are marked as Outdated or Broken when applicable

- 
For each published module, raise a publish event, that notifies LT of that change

- 
If transient solution, delete it from the DB

- 
If not, update its DB info

- 
Update `OSSYS_APP_FORGE` entries (where applicable)

- 
Handle native builds: regenerate native hashes for the applications involved in the solution and will (optionally) launch the native builds where necessary.

- 
For each successfully published espace, schedule the espace timers of type &quot;WhenPublished&quot; to run 

- 
Run `DisposeBuild` of Compiler Service

# Getting into other details## Solution locks and unlocks
Each time a Solution Publish starts, the respective solution gets locked. This lock is used to avoid concurrent publications of the same solution (publish a solution that as an ongoing publication already running).

Each time a solution publication ends, either successfully or due to errors, the solution lock is released.

These locks and unlocks can be found in Service Center OML by looking for the `LockSolution` and `UnlockSolution` actions usages. These actions represent calls to CompilerService that keeps a Dictionary of active locks in memory.

Bugs in the lock/unlock system may cause a solution to get locked indefinitely even though it has no ongoing publications. A general **workaround** for this is to restart the CompilerService, as all locks will be cleared/released.

CompilerService code for this can be found in the [SolutionPublishService ](https://github.com/OutSystems/Platform/blob/b11/HubServer/Server/Services/Publish/Publish.Application/SolutionPublishService.cs)class.
## Full Compilation vs Differential Compilation
In the context of solution publishes, the difference between making a Full Compilation or not, is that in the later you are allowing the platform to detect for each module if it can reuse the compilation result of the module last publish (contained in the module&rsquo;s `share` folder) and skip its compilation phase. Otherwise, the platform will always ignore that possibility and execute a full compilation phase for the solution modules.

More information on how Solution Publish decides to reuse previous compilations bellow, in the [CleanPublish](https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/3188228271/What+is+Solution+Publish+and+what+makes+it+tick#CleanPublish-(a.k.a.-Publish-with-full-compilations)) section.

You should keep in mind that, in the context of solution publishes, when the platform doesn&rsquo;t skip the compilation phase of a module it will always make a full compilation of the module (and **not** a differential one from that previous version). This behavior is slightly different in comparison with 1CPs, where it can use Differential Compilation which is an optimization that only regenerates code for the modified elements.

Though, during the Deploying phase the solution publish will technically use Differential Compilation to generate configuration files before deploying.
### Why use Publish with full compilations
You might be wondering what&rsquo;s the use case for this [Publish with full compilations](https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/3188228271/What+is+Solution+Publish+and+what+makes+it+tick#CleanPublish-(a.k.a.-Publish-with-full-compilations)) feature. This is a failsafe option, when we want to be certain that no compilation files from previous publications get reused during the solution publication.

One case where this may happen is the following one presented in the diagram:

- 
There&rsquo;s some ModuleP1 and ModuleP2 that consume ExtensionA

- 
ModuleP1 was published when the ExtensionA was in v1

- 
In this version the extension contains 2 files `Some.dll` and `SomeOther.dll`

- 
ModuleP2 was published when the ExtensionA was in v2

- 
In this version the extension was updated to only contain `Some.dll`

- 
There&rsquo;s a ModuleC that consumes ModuleP1 and ModuleP2

- 
If we publish a solution containing *C*, *P1* and *P2*, and compilation gets skipped for *P1*, ModuleC might end up with the new `Some.dll` of ExtensionA but also still the `SomeOther.dll` file that was present in V1.

- 
Using Full Compilation, ModuleP1 will be compiled again and get the new files of ExtensionA v2, and this scenario will be avoided

Example diagram where &ldquo;Publish with full compilations&rdquo; may be useful
## Paths for Solution Publish to get called
The following image shows the possible ways solution publish can get called. Here&rsquo;s some notes about the figures in it:

- 
REST (&gt;=O9) means that LifeTime will initiate the staging using a REST endpoint when the target environment is in version 9 or above.

- 
SOAP (&lt;O9) means that LifeTime will initiate the stating using SOAP endpoints when the target environment is in a version previous to 9.

- 
SOAP (not from LT) means that the endpoint exists but there isn&rsquo;t any reference to it in LT.

- 
`Solution_Publish_InnerProxy` is a screen that is responsible for initiating the Solution Publish process. For instance, when a user hits the &ldquo;Publish&rdquo; button of a solution in the `Solution_Edit` screen, the action  `Solution_Publish` will run a redirect into that page (using the Destination action type). That page will then run a Preparation action which runs some security checks and in the end redirects to `Solution_Publish_Proxy`.

- 
`Solution_OSPConfiguration` is the screen where the user configures the database connections.

- 
`Solution_OSPConfirmation` is the screen shown when performing a data move or after the impact analysis, where the user should choose between continuing the publish or abort it.

## What are the _Optimized actions in Solution Publish SC actions
Code related with `_Optimized` actions was cleaned up since 11.21.0 in [R11PT-91](https://outsystemsrd.atlassian.net/browse/R11PT-91).

If you look in SC code there are some Solution Publish actions that are duplicated, having a *_Optimized* name suffix. These actions were created in an O11 Platform Backend initiative to improve Solution Publish performance. You can find a document on the initiative here: Solution Publish Improvements 
Currently, we are already on a rollout process to deliver this Optimized version to our customers. As soon as it gets fully rolled out, we will deprecate and delete the old code.
## What is 2-Stage Deploy (aka 2-step)
When checked, deployment is done in 2 steps. First step compiles and prepares apps, second deploys

This means that when performing a solution publish, the process stops before starting the deployment stage and waits for user input to proceed with the actual deployment.
### Related issues#### Disabling modules mid between the 2 stages
It is currently not possible to disable eSpaces included in a ongoing solution publish.

R11PBT-878ef8955cb-cb21-32a7-b692-01ace42388d6System Jira

RPM-2703ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 
#### Restarting IIS/Service Center causes a KeyNotFoundException
Fixed in `11.23.1`.

R11PT-256ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

RPM-3713ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 
#### It&rsquo;s not possible to continue into the 2nd stage once Deployment Controller Service is restarted
Fixed in `11.23.1`.

R11PT-529ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

R11PST-77ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

RPM-1886ef8955cb-cb21-32a7-b692-01ace42388d6System Jira
####  It&rsquo;s not possible to continue into the 2nd stage once Deployment Service is restarted
RPM-3330ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 
## Common solution publish troubleshooting steps
- 
If a file can&rsquo;t be accessed, check the antivirus.

- 
If you&rsquo;re having errors during the refresh dependencies step, and you don't need the dependencies to be refreshed, just create a version of the solution and just publish that version. Contrary to the running version, publishing a version won&rsquo;t create a new version with refreshed dependencies.

## How LifeTime handles staging
In it&rsquo;s core, what LifeTime (LT) does is the equivalent to a user picking some modules in a environment, add them to a solution, download the OSP file for that solution and upload that OSP file in the target environment.

- 
It does the analysis of which modules and dependencies are required to publish

- 
When you publish it tells you what will be become outdated

- 
You always select applications to stage (not modules), and then you can customize which modules will be included in the staging plan

- 
Staging steps:
- 
Select

- 
Validate

- 
Review

- 
Deploy

### What is a staging/deployment plan?
A deployment plan allows you to deploy application changes, like new features and fixes, performed in one environment to a different environment, for example from Development to QA.

* Taken from [here](https://success.outsystems.com/Documentation/11/Managing_the_Applications_Lifecycle/Deploy_Applications/Deployment_Plans)
### What is a version tag?
Tagging an application version in LifeTime means that a snapshot of the development state of the application is taken and a version number is associated to it. When deploying the application, just select the tagged version and LifeTime deploys the application in the exact development state in which it was tagged.

* Taken from [here](https://success.outsystems.com/Documentation/11/Managing_the_Applications_Lifecycle/Deploy_Applications/Tag_a_Version)
### LifeTime and 2 stage deployment
[https://success.outsystems.com/Documentation/11/Managing_the_Applications_Lifecycle/Deploy_Applications/Deploy_in_a_Short_Deployment_Window](https://success.outsystems.com/Documentation/11/Managing_the_Applications_Lifecycle/Deploy_Applications/Deploy_in_a_Short_Deployment_Window)

Be aware that, although there isn&rsquo;t an actual timeout for executing the second stage of 2-stage deployment after the first stage finished, there is a timer in Service Center &ldquo;SolutionPack_Cleanup&rdquo; that cleans up transient solutions (the kind that LifeTime uses for its deployments). This timer uses Service Center&rsquo;s site property SolutionPackHoursCache (default value is 96 hours - 4 days) to delete any transient solutions older than the value of that site property. This means that a 2-stage deployment done by LifeTime, after 1st stage is completed, the user has 4 days to complete the 2nd stage or the solution being used will be cleaned and no longer possible to be completed. The value of the site property can be changed normally as other site properties are.
### How LT and SC communicate with each other when performing a staging
All the preparation of which modules should be included in a staging (or solution publish) is done by LifeTime during the staging selection and validation phases. When the user chooses to start the staging, LT will:
- 
Tag new application versions (if any application had option &ldquo;Tag &amp; Deploy&rdquo;)

- 
Create new applications (if deploying new applications to target)

- 
Upload each of the modules included in the staging (that are not yet in the target environment)

- 
Apply any necessary settings (e.g. configuration of deployment zones)

- 
Call SC to start the publish, passing all the necessary information

- 
During publish, LT will poll SC to obtain the publish messages, so that it can show them to the users in LT

- 
It does some clean ups and more settings in the end, but those do not affect the publish.

Step 5 is where the magic happens: LT will call the Platform Services API Rest call StagingPublishWith2StepOption. This API will create the solution pack based on the modules and applications being passed to it (action SolutionPack_CreateForStaging) then it will start the publish process - it starts the publish process by calling for page Solution_Upgrade_Logic.aspx in an asynchronous way. This eventually lead to Solution_Upgrade_Logic_Go described above.

During publish, LT will poll SC to obtain the messages that result from the publish process. The messages are retrieved when the user is in Staging_Progress screen. It uses SolutionPack_GetPublishMessages SOAP Service Method to retrieve the messages (Step 6).

Looking at the messages, LT will be able to detect if Publish is stopped for some reason:

- 
There is a missing configuration that the user needs to complete before proceeding (e.g. connect an extension to a database connection)

- 
1st stage in a 2-stage publish was completed and waiting for the user to proceed.

When there is missing configuration, LifeTime will have a link for SC that the user needs to navigate to. It is not possible to configure that in LifeTime. After configuration is done and publish resumes, the user can return to LT to continue to see the publish messages or stay in Service Center and watch it from there.
### I&rsquo;ve got an error executing a staging operation. How do I know if the problem is in LT or in SC?
If the error occurs during actual solution publish, the problem is most likely in the environment side instead of LifeTime. This means after &ldquo;Analyzing impact on running business processes&rdquo;:

And before &ldquo;Synchronizing Environment&rdquo;:

There are some exceptions:

- 
the error occurs because the solution is incorrect in some way, e.g. it has a module that was added twice.

A module added twice to the solution results in errors like these:

In this case, the problem was caused by LifeTime passing the same module twice to be included in the solution. We can confirm it by taking a look at LifeTime&rsquo;s troubleshoot mechanism of Staging Report. You can  read more about this in LifeTime Troubleshoot.
## Running a solution publish in SC vs staging in LT
This workaround might be acceptable for some situations, it might not work for other scenarios:

- You will only be able to deploy the application latest version or a Solution that you had previously created and versioned in Service Center.

- You won&rsquo;t be able to deploy an application&rsquo;s tagged version - LifeTime tags aren't available in Service Center.

- If LifeTime deployment isn't working correctly due to issues in the source or the target environment, you may hit the same issues when trying to use this workaround.

Places where thing run differently if running from LT:

- 
In `Solution_Upgrade_Logic_Go/Preparation` and `Solution_Publish_Logic_Go_Preparation/Preparation` if any exception happens an `AsyncOperation_SetState` runs and sets the state to `done`

- 
There are several places where if it&rsquo;s running from LT security checks are ignored (but still run, though)

- 
The initial pack check is skipped

- 
In the end of the publish runs an Audit action

## Telemetry 
There are 3 types of tables that might help you analyzing solution publish performance in Snowflake:

- 
`SOLUTIONPUBLISH` - overall data for a whole publication

- 
SP_[something] tables - data for a specific step/section of a publication

- 
`RESERVEDATABASETABLENAMES` - holds telemetry for CompilerService&rsquo;s `ReserveDatabaseTableNamesTask`. This runs every time a module is compiled, and you can use this to obtain a list of espaces being compiled (including omlSize, key, name, &hellip;)

Solution Publish telemetry is handled in the following places:

- 
In SC&rsquo;s:

- 
`Telemetry_SolutionPublish` server action, which translates into the `SOLUTIONPUBLISH` Snowflake table

- 
`Telemetry_SolutionPublish_Step` server action, which translates into the several SP_[something] Snowflake tables

- 
In C# sent through `ExecuteMeasuredStep` method in [SolPublishService.cs](https://github.com/OutSystems/Platform/blob/26f34d3302e1eabd7b41d677de4cf1e7f7d073d1/HubServer/CompilerService/Services/SolutionPublish/SolPublishService.cs#L394-L405) 

### Remarks on the data:
- 
Telemetry prior to 11.25.0 includes inconsistent data:

- 
StartDate and EndDate may be in the future
due to US culture formatting

- 
SolutionImprovement sometimes was wrongly false

- 
Added 2-step and LT deployment bools

- 
Fixed in [R11PT-534](https://outsystemsrd.atlassian.net/browse/R11PT-534)

- 
Some relevant data you can find in all these tables:

- 
`COMPONENT_VERSION`** **gives you the PS version

- 
`DOMAIN_OPERATIONID` 

- 
Can be used to filter for specific operations

- 
Can be used to cross-reference with other tables

- 
`ENV_ACTIVATION_CODE`

- 
Some relevant data you can find in `SOLUTIONPUBLISH` table

- 
`DOMAIN_SOLUTIONKEY`

- 
`DOMAIN_SOLUTIONNAME` 

- 
`domain_modulescount`

- 
`domain_starttime`

- 
`DOMAIN_ENDTIME`

- 
`DOMAIN_DURATIONSECONDS` time difference between start and end time

- 
Note that this includes also time waiting for user input. To workaround that, we can do a join with the several SP_ tables by DOMAIN_OPERATIONID and sum each individual table time, to get a more realistic total execution time. You can find an example of this in the query below

- 
`DOMAIN_TWOSTEPMODE`

- 
`DOMAIN_FORLIFETIMEDEPLOYMENT`

- 
`domain_internalerrors`

- 
`DOMAIN_ABORTEDDUETOLICENSEVIOLATION`

- 
`DOMAIN_ABORTEDBYUSER`

- 
`DOMAIN_ABORTEDDUETOGENERICERRORS`

- 
`DOMAIN_SOLUTIONIMPROVEMENT` tells if run using C# Solution Publish

- 
`DOMAIN_SOLUTIONVM` tells what was the Migration VM toggle value

- 
Some relevant data you can find in &ldquo;SP_&rdquo; tables:

- 
`DOMAIN_DURATION`

- 
`DOMAIN_STARTTIME`

- 
`DOMAIN_ENDTIME`

- 
Some relevant data you can find in `RESERVEDATABASETABLENAMES`:

- 
`CUSTOM_OMLSIZE`

- 
`CUSTOM_ESPACEKEY`

- 
`CUSTOM_ESPACENAME`

### Query exampleSnowflake screenshots
Query example that obtains solution publish timessql '2023-10-01' --AND sp.domain_starttime  0

AND sp.event_date > '2024-07-01'
AND sp.domain_solutionvm = 2
--AND sp.domain_twostepmode = true
--AND sp.domain_operationid = '3808af02-d614-41bc-9b56-d5aad3c4a940']]>### References
Some references that might help understanding telemetry decisions and structure:

- 
[https://outsystemsrd.atlassian.net/wiki/x/4IDy2Q](https://outsystemsrd.atlassian.net/wiki/x/4IDy2Q) 

- 
[https://docs.google.com/presentation/d/1nsx2Oasf2M57zJld657fe0hVwYx08gSmEIgdeWvmnhU/edit#slide=id.g309dc52c5e6_0_199](https://docs.google.com/presentation/d/1nsx2Oasf2M57zJld657fe0hVwYx08gSmEIgdeWvmnhU/edit#slide=id.g309dc52c5e6_0_199) 

- 
[https://docs.google.com/document/d/1VhmV4dNfFsFQpmaEt662XlzdKjXBmaNtrlen6bajs_A/edit#](https://docs.google.com/document/d/1VhmV4dNfFsFQpmaEt662XlzdKjXBmaNtrlen6bajs_A/edit#)

## (Not so) Random quick definitions### COMPATIBILITY_SIGNATURE_HASH DB column
This field is calculated for each reference of a producer. It is used to determine if a producer is still compatible with a consumer. When the value doesn&rsquo;t change it means that, even if there were any signature changes, the signatures are still compatible with preexisting consumers.

For instance, changing the *Default Value* of an input of a server action won&rsquo;t cause the compatibility hash to change, but changing its *Is Mandatory* setting will. One way you&rsquo;ll notice this is through SC by visiting the edit page of a consumer espace with outdated dependencies:

- 
when a producer compatibility hash changes you&rsquo;ll see the warning *This Module has outdated dependencies that may be incompatible. You should publish it to avoid runtime errors*.

- 
otherwise the message will be *This Module has outdated dependencies. You should publish it to avoid running outdated code*.

### FULL_SIGNATURE_HASH
This field is calculated for each reference of a producer. It is used to determine if the a consumer reference was modified in the producer since it was last refreshed. This value changes every time anything changes in the referenced element. 
### Refresh references in solution publish (a.k.a. Refresh dependencies)
Example support case on this: R11PT-121ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

The *Refresh only broken dependencies* in Solution Publish Factory Configuration parameter, correspondant to the PlatformServices.OnlyRefreshIfBrokenReferences toggle in the code, determines the conditions on which we decide to refresh all references for each module, during the update components step of a solution publication.

When disabled it checks if there are any **different **signatures in the referenced elements of a consumer module and refreshes all of them (within that module) in case it finds one, which can unnecessarily increase publishing times.

However, when the parameter is enabled it only checks if there are any **incompatible **signatures in the referenced elements of a consumer module and only refreshes all of them (within that module) in case it finds one.

In essence, what this means is that when this setting is enabled we stop checking for a different signature in the module [**FULL_SIGNATURE_HASH**](https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/3188228271/What+is+Solution+Publish+and+what+makes+it+tick#FULL_SIGNATURE_HASH)** **(i.e. if the element has changed or not) and start checking to see if the change has any impact on the consumer by checking the [**COMPATIBILITY_SIGNATURE_HASH**](https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/3188228271/What+is+Solution+Publish+and+what+makes+it+tick#COMPATIBILITY_SIGNATURE_HASH-DB-column) (i.e. if due to the change on the element this is no longer compatible with the one in the consumer).

Since v11.27.0 we made this the new default behavior (issue [R11PST-33](https://outsystemsrd.atlassian.net/browse/R11PST-33)). This change shouldn&rsquo;t cause any disruption in the solution publication experience, and will overall result in better publishing times. It was documented in our breaking changes page, anyway.

This behaviour can be changed back using the most recent version of Factory Configuration application through the &ldquo;Refresh only broken dependencies in solution publish&rdquo; setting under the Platform Configurations screen.

This only happens during the solution publish operation if:

- 
Publishing the &ldquo;Current Running Version&rdquo; (publishing a specific version will skip the refresh step)

- 
AND the machine's purpose is set to Development

If the desire is to refresh all the references in all modules during the Solution publication then, the &ldquo;*Refresh only broken dependencies&rdquo;* parameter should be disabled first.
### `CleanPublish` (a.k.a. Publish with full compilations)
`CleanPublish` is a Solution Publish variable whose value is defined using the &ldquo;Publish with full compilations&rdquo; checkbox that is present in the Solution Edit screen.

This is used to prevent compilation steps from being skipped. Note that this isn&rsquo;t related in any way with dependencies or the refresh of references.

It is used in `Espace_CompileWithEmptyProxies` action. Here, if not publish with full compilations, the compilation may be skipped when:

- 
Module is not Mobile

- 
AND module is not CrossDevice (aka Reactive)

- 
AND module didn&rsquo;t change compile time configs. In `OSSYS_ESPACE_STATUS` (aka `Espace_Runtime` in SC code):

- 
`REQUIRES_COMPILATION` must be false, meaning the espace must not be flagged as needing to be compiled and published again. These are the modules that have a warning in SC saying &ldquo;This module has pending configuration changes. Republish the Module to apply them.&rdquo;

- 
`SECURITYSETTINGSCHANGED` must be false, meaning the espace must not be flagged as needing to apply new security settings. These are the modules that have a warning in SC saying &quot;Security Configurations Changed. Mobile applications Modules need to be published to use the new HSTS and/or Content Security Policy settings.&quot;

- 
AND module is marked as consistent (`IS_CONSISTENT` in `OSSYS_ESPACE` table)

### External Pack
An external pack is a solution publish triggered by the upload of an OSP file (rather than publishing it from SC from an already existent solution/version). Even when the publication output messages say &ldquo;Upload Skipped&rdquo;. A LT staging is evaluated as an External Pack.

Service Center logic determines if it&rsquo;s an External Pack based on the `PackUID` and `SolutionId` variables. In several places of Service Center we can find `if` clauses named &ldquo;External Pack?&rdquo; based on one of these conditions (or equivalent):

- 
`PackUID &lt;&gt; &quot;&quot;`

- 
`SolutionId = NullIdentifier()`

Reading the URL to where you got redirect after starting the publication will let you know what are the `PackUID` and `SolutionId` values, like this:

- 
https://[somedomain]/ServiceCenter/Solution_Publish.aspx?**PackUID=**&amp;PackSchemaVersion=-1&amp;PackPublish=False&amp;**SolutionId=22**&amp;(&hellip;)

- 
https://[somedomain]/ServiceCenter/Solution_Publish.aspx?**PackUID=def5ef41-d39b-4332-9516-fb64ec4fb7a1**&amp;PackSchemaVersion=3&amp;PackPublish=True&amp;**SolutionId=0**&amp;(&hellip;)

### CanAskQuestions parameter
WIP section - depends on [R11PT-4](https://outsystemsrd.atlassian.net/browse/R11PT-4)

This is an input parameter received by the Solution Publish SC code.

Previous research regarding how this parameter affects the logic execution can be found [here](https://docs.google.com/document/d/10LAZiSetxbppymnUkMqXfRIbjY61hFLvNW7dyJ5-UPc/edit?tab=t.0).

Goal of this parameter is to better integrate with OSPTool, by avoiding it to get stuck waiting for user input, based on this comment in SC&rsquo;s `PublishWithoutConfiguration` action:

Semantics for the FromOSPTool input parameter:

- 
True: the solution publish operation will NOT stop for impact analysis =&gt; CanStop MUST be False

- 
False: the solution publish operation will stop for impact analysis, even if the request comes from the OSPTool =&gt; CanStop will be True

The automated, i.e. non-interactive, OSPTOOL will send this parameter as TRUE.
The OSPTool with UI will send this parameter as FALSE.
# Related documents## Solution Publish
- 
How to abort a solution publish: Cancel Publish 

- 
[https://outsystemsrd.atlassian.net/wiki/x/foF8s](https://outsystemsrd.atlassian.net/wiki/x/foF8s) 

- 
[https://outsystemsrd.atlassian.net/wiki/x/yoADDwE](https://outsystemsrd.atlassian.net/wiki/x/yoADDwE) 

- 
Solution Publish database tables 

- 
Solution Publish migration to C# initiative GS KT: Global Support Knowledge Transfer 

- 
Solution Publish migration to C# initiative internal KT: [https://docs.google.com/presentation/d/1nsx2Oasf2M57zJld657fe0hVwYx08gSmEIgdeWvmnhU/edit?usp=sharing](https://docs.google.com/presentation/d/1nsx2Oasf2M57zJld657fe0hVwYx08gSmEIgdeWvmnhU/edit?usp=sharing)

- 
New Solution Publish - Architecture overview 

- 
(WIP) How pull espace producers works  

## LifeTime
- 
How to troubleshoot LifeTime: LifeTime Troubleshoot 

- 
LifeTime Troubleshoot Workshop III: [https://docs.google.com/presentation/d/15Yc4ejRyw_1ghnJed2fPTleqxmvfQjD69Pxpa5I4JNM/edit#slide=id.g233f4f83b3_0_7](https://docs.google.com/presentation/d/15Yc4ejRyw_1ghnJed2fPTleqxmvfQjD69Pxpa5I4JNM/edit#slide=id.g233f4f83b3_0_7) 

- 
LifeTime Troubleshoot Workshop II: [https://docs.google.com/presentation/d/17yaR5lJHG6etGJt4ODebosV83LZPUmNch3OjtSHYezY/edit#slide=id.g1debe2b3d6_0_0](https://docs.google.com/presentation/d/17yaR5lJHG6etGJt4ODebosV83LZPUmNch3OjtSHYezY/edit#slide=id.g1debe2b3d6_0_0)  

- 
How to setup developer machine database to run tests (SQL Server and Oracle) 

# Topics brainstorm to document next
This section is a compilation of ideas of things that we could have better documented:

- 
OSPTool

- 
[https://github.com/OutSystems/Platform/tree/b11/Commons/OSPTool](https://github.com/OutSystems/Platform/tree/b11/Commons/OSPTool) 

- 
[https://github.com/OutSystems/Platform/tree/b11/Commons/OSPTool.CommandLine](https://github.com/OutSystems/Platform/tree/b11/Commons/OSPTool.CommandLine) 

- 
[Solution Pack Tool Command Line Reference - OSPTool](https://success.outsystems.com/documentation/11/setup_outsystems_infrastructure_and_platform/setting_up_outsystems/unattended_installation_and_upgrade/solution_pack_tool_command_line_reference_osptool/)

- 
Where license checks happen

- 
`CheckAndAbortOnLicensingErrors` SC&rsquo;s server action

- 
In C#, in [SolutionPublishOrchestrator.cs](https://github.com/OutSystems/Platform/blob/26f34d3302e1eabd7b41d677de4cf1e7f7d073d1/HubServer/CompilerService/Services/SolutionPublish/SolutionPublishOrchestrator.cs#L188-L192) 

- 
When can the solution be aborted

- 
Design document: Cancel Publish 

- 
`IsAbortByUserPending` SC&rsquo;s server action

- 
In C#, in [SolPublishService.cs](https://github.com/OutSystems/Platform/blob/26f34d3302e1eabd7b41d677de4cf1e7f7d073d1/HubServer/CompilerService/Services/SolutionPublish/SolPublishService.cs#L368-L382) 

- 
Where and what modules are skipped. At least 2 potential topics here:

- 
`SolutionPublishFilterHiddenModules` SC action that ignores LifeTimeCloudConnect (LTCC), CloudConnectAgent, CloudOrchestrationAPI and RuntimeModel espaces; and CloudConnectAgent extension.

- 
Modules affected by the CleanPublish setting

- 
What is the Publish Plan and what happens every time we update it

- 
How error handling is done

- 
How to troubleshoot performance issues

- 
&ldquo;Before anything else, where did the customer tried to downgrade the Service Studio version? Was it on the server where the solution is being published or in a different machine that connects to that environment using Service Studio? Because the solution publish mechanism uses the Service Studio that is installed in that specific machine (where the solution publish is being performed) and this is the place where the version needs to be downgraded.&rdquo;

- 
(WIP) How pull espace producers works 

- 
Usage of Process Monitor and Antivirus check:

- 
R11PBT-775ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

- 
How to use debugdiag: R11PBT-445ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

- 
Broken references: R11PBT-169ef8955cb-cb21-32a7-b692-01ace42388d6System Jira 

- 
Deployment zones: Deployment Zones 

- 
How permission configuration works

- 
What are hidden modules?

- 
Model: Hidden References 

- 
Solution Publish, &ldquo;What is X and what is its impact&rdquo; candidates:

- 
What is `SkipToState`?

- 
 "" and 
(SkipToStateId = Entities.Solution_Publish_State.ImpactAnalysis or 
SkipToStateId =  Entities.Solution_Publish_State.Checks or 
SkipToStateId = Entities.Solution_Publish_State.Compile or 
SkipToStateId = Entities.Solution_Publish_State.Deploy or 
SkipToStateId = Entities.Solution_Publish_State.SecondStageImpactAnalysis or 
SkipToStateId = Entities.Solution_Publish_State.FinalizeDeploy)]]>

- 
`ReuseTablesOnMove` 

- 
`FromServiceStudio` 

- 
`SilentOverwriteVersion` 

- 
`DisableNotifications` 

- 
`ForLifetimeDeployment` 

- 
`IgnoreBrokenReferences` 

- 
`TryingToSkipUpload` 

- 
`SolutionPublishAssetId` 

- 
What is BAR service: [https://docs.google.com/document/d/1T5a0ql7N6U-Gs6A9XY3Im5262Q2RR8iCEx5qrJkzuiw/edit](https://docs.google.com/document/d/1T5a0ql7N6U-Gs6A9XY3Im5262Q2RR8iCEx5qrJkzuiw/edit) 

- 
Step-by-step (deep dive) topics:

- 
Solution_Upload / UploadEspace / Extension_Upload

- 
`App_CreateOrUpdate`: maybe detail what this does, eg. [independent modules logic](https://outsystemsrd.atlassian.net/wiki/spaces/RT/pages/2960949630/Solution+publish+quick+guide+on+uploading+apps+app+definitions+and+independent+modules+flow), name truncation, icon update, &hellip;

- 
Security_CheckSolution: detail this more? what is Security_IsManagedLocally(), HiddenSolution?, &hellip;?

- 
`Security_IsManagedLocally`: when there&rsquo;s an LT setup, user permissions are manage in LT instead of SC. This action returns true when permissions are managed at SC level, false if not (when managed in LT). This is done by checking SC&rsquo;s `SecurityManagerURL` site property, which stores the URL of the Platform being used to manage the permissions in this SC. If empty then permissions are being managed locally. 

- 
`IsHiddenSolution`: used to hide LifeTimeCloudConnector (aka LTCC) and CloudConnectAgent solutions from non-cloud administrators users

- 
`Extension_Publish` 

### LifeTime topics brainstorm
- 
Deploy now = Staging

- 
LT has tables with the state of all the connected environments

- 
LT uploads each one of the modules into the target environment, and tries to create the app there. May temporarily put applications in the independent modules app.

- 
LifeTimeCore is the lowest layer, and it&rsquo;s the one where communication with Service Center (SC) happens

- 
LifeTimeEngine calls the LifeTimeCore