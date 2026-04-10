---
title: Solution Publish database tables
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/4607344663/Solution+Publish+database+tables
confluence_space: RCP
confluence_page_id: 4607344663
last_synced: 2026-04-09
owner: Process Engineering
---

# Solution Publish database tables

# Context
The goal of this document is to provide awareness of what are the tables related to Solution Publish and how they can be used.
# Tables## OSSYS_SOL_PUB_PLAN
Created at the beginning of the publication. Contains the following data:

- 
**ID**

- 
**SolutionPubId**

- 
**State **- Current &quot;phase&quot; of the publish (ex: ImpactAnalysis, Compile, Deploy, ...)

- 
SC's `Solution_Publish_State` static entity

- 
**StartInstant **- Machine DateTime where this entry was created (beginning of the publish)

- 
**EndInstant **- Machine DateTime where publish was marked as &quot;done&quot;, &quot;erroraborted&quot; or &quot;licenseaborted&quot; 

- 
**PendingCommand **- Used to help the orchestration coordination with user interaction. SC's Solution_Publish_Plan_Command static entity:

- 
1=Abort;

- 
2=Continue;

- 
3=None;

- 
4=Suspend.

- 
**IsLifeTimePlan **- Published started by a LT staging

- 
**SummaryMessage **- May contain a summary message once the mobile apps finish being processed

## OSSYS_SOL_PUB_PLAN_EXT
Extension of `OSSYS_SOL_PUB_PLAN` can be obtained by joining plan&rsquo;s `ID` with ext&rsquo;s `SOLUTIONPUBLISHPLANID`. Contains the following data:

- 
**ID**

- 
**SolutionPublishPlanId**

- 
**CurrentStepId** - Current step being executed (SC's Solution_Publish_Step static entity):

- 
1: VerifySolutionConsistencyAndPermissionSettings

- 
2: UpgradeOrRefreshSolutionComponents

- 
3: PrepareWorkspace

- 
4: PerformImpactAnalysis

- 
5: PreparePublishExtensions

- 
6: UpdateeSpacesMetamodel

- 
7: AssociateeSpacesDependencies

- 
8: CompileeSpaces

- 
9: CompileeSpacesReferences

- 
10: GathereSpaceProducers

- 
11: PrepareeSpaceAndExtensionDeploy

- 
12: DeployImpactAnalysis

- 
13: DeployeSpaces

- 
14: PublishFinished

- 
**CurrentStatus** - General status of publish (SC's Solution_Publish_Unit_Status static entity):

- 
1: Aborted

- 
2: FatalError

- 
3:  Queued

- 
4: Running

- 
5: Success

- 
6: WaitingDecision

- 
7: NonFatalError

- 
**CurrentStepStartInstant **- Current step machine start DateTime

- 
**CurrentStepEndInstant **- Current step machine stop DateTime

## OSSYS_SOL_PUB_COMP
Used to store information on espaces and extensions included in a given solution publish plan to be used when a 2-step publication is resumed and when a publication is aborted (user clicks the &ldquo;Cancel&rdquo; button). This is represented by the Entity `Solution_Publish_Component`.

- 
**Id** - generated ID

- 
**Solution_Publish_Plan_Id** - FK to `OSSYS_SOL_PUB_PLAN`

- 
**Espace_Id** - FK to OSSYS_ESPACE. ID of the espace included in the solution (filled if referencing an espace; NULL if referencing an extension)

- 
**Espace_Version_Id** - FK to OSSYS_ESPACE_VERSION. ID of the espace version to be deployed (filled if referencing an espace; NULL if referencing an extension)

- 
**Extension_Id** - FK to OSSYS_EXTENSION. ID of the extension included in the solution (filled if referencing an extension; NULL if referencing an espace)

- 
**Extension_Version_Id** - FK to OSSYS_EXTENSION_VERSION. ID of the extension version to be deployed (filled if referencing an extension; NULL if referencing an espace)

- 
**Name** - Name of the espace or extension

- 
**Main_Reference** - Not used.

- 
**DeploymentId** - UUID that&rsquo;s generated during `DeployPrepareDeployEspace` CompilerService&rsquo;s method (called in [&quot;Preparing Deploy&quot; step](https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/3188228271/What+is+Solution+Publish+and+what+makes+it+tick#12.-Preparing-Deploy)). It&rsquo;s later used during `DeployFinalizeDeployEspaceSolution` CompilerService&rsquo;s method (called in [&ldquo;Deploying&ldquo; step](https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/3188228271/What+is+Solution+Publish+and+what+makes+it+tick#14.-Deploying)).

## OSSYS_ASYNC_OP_STATE
This table is generic and used for other operations other than Solution Publish, where it contains general info of the publication state (notice that records in this table may be automatically cleaned up):

- 
**ID** - generated ID: this is the same ID used for the `SolutionPubId` variable 

- 
**OperationId** - UUID of the Solution Publish operation being executed

- 
**Target_Object_SSKey** - SSKEY of the solution being published (aka SolutionUID), **except** when uploading a new solution from an OSP, in that case it is the solution PackUID

- 
**Time_Stamp** - Database time at the time of creation of the record

- 
**State** - Current state/phase of the publication:

- 
done

- 
upload

- 
licenseaborted

- 
erroraborted

- 
Check

- 
ImpactAnalysis

- 
Compile

- 
Deploy

- 
SecondStageImpactAnalysis

- 
FinalizeDeploy

- 
MobileBuild

- 
ValidateBrokenReferences

- 
**Operation_Type** - Always &ldquo;Solution Publish&rdquo; for Solution Publish operations

- 
**Return_URL** - Publish report URL, similar to this:

- 
`/ServiceCenter/Solution_Publish_Proxy.aspx?SolutionId=30&amp;SolutionVersionId=0&amp;SolutionPubId=346&amp;PackSchemaVersion=-1&amp;SolutionPublishAssetId=Solution`

## OSSYS_ASYNC_OPERATION_SODETAIL
This table is an extension of `OSSYS_ASYNC_OP_STATE` and it holds some details of the solution being published. It contains the following data:

- 
**Id** - FK to `OSSYS_ASYNC_OP_STATE`

- 
**SolutionId **- Solution database ID

- 
**SolutionVersionId **- Solution version database ID (will be 0 when publishing the running version)

- 
**PackUID **- Pack UID of the OSP being published

- 
**PackSchemaVersion **- Schema version present in the manifest file

- 
**PackPublish **- False for &ldquo;upload only&rdquo; operations

- 
**CleanPublish** - Boolean if &ldquo;Publish with full compilations&rdquo; was enabled

- 
See [https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/3188228271/What+is+Solution+Publish+and+what+makes+it+tick#CleanPublish-(a.k.a.-Publish-with-full-compilations)](https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/3188228271/What+is+Solution+Publish+and+what+makes+it+tick#CleanPublish-(a.k.a.-Publish-with-full-compilations)) 

- 
**TwoStepPublishMode** - Boolean if 2-step publish was enabled

- 
See [https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/3188228271/What+is+Solution+Publish+and+what+makes+it+tick#What-is-2-Stage-Deploy-(aka-2-step)](https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/3188228271/What+is+Solution+Publish+and+what+makes+it+tick#What-is-2-Stage-Deploy-(aka-2-step)) 

## OSSYS_ASYNC_OP_MESSAGE
This is the table used to send deliver messages to the publish report UI. It contains the following data:

- 
**ID **- generated ID

- 
**Message_Id **- not used in the context of Solution Publish

- 
**Message **- the message title to show (also used for grouping messages into collapsible sections)

- 
**Detail **- the actual message to show

- 
**HelpRef **- not used. Description in OML: Service Studio Help ID reference

- 
**ExtraInfo **- internal metadata used to hammer   behaviors through the messages processing. In Solution Publish it&rsquo;s used to detect if specific error messages are present (when its value is `brokenreference` or `oldproducer`)

- 
**Type **- Used to control how the message is shown in the UI

- 
AcceptableError: error that doesn&rsquo;t cause the publish to stop

- 
PublishStop: message that signals the publication has completed

- 
StepX: message that creates a new collapsible section

- 
StepSub: message to be included in the already created collapsible section

- 
Info

- 
Warning

- 
Error

- 
DevWarn

- 
Ok

- 
Question

- 
State

- 
TestRunning

- 
**Submitable **- not used in the context of Solution Publish

- 
**State_Id **- FK to `OSSYS_ASYNC_OP_STATE`

- 
**Read **- DEPRECATED

## OSSYS_ASYNC_OP_DBCATALOG
Used to hold the MDC configuration for each espace. It contains the following data:

- 
**Id** - generated ID

- 
**Espace_Id **- FK to `OSSYS_ESPACE`. ID of the espace being configured

- 
**Espace** - Name of the espace being configured

- 
**DBCatalogName **- Name of the catalog being configured

- 
**DBCatalog_Id** - FK to `OSSYS_DBCATALOG` 

- 
**State_Id **- FK to `OSSYS_ASYNC_OP_STATE`

## OSSYS_ASYNC_OP_LOGICALDATABASE
Used to hold the DB connections configuration for each extension. It contains the following data:

- 
**Id** - generated ID

- 
**Extension_Id **- FK to `OSSYS_EXTENSION`. ID of the extension being configured

- 
**Extension **- Name of the extension being configured

- 
**LogicalDatabase **- Name of the connection being configured

- 
**DBConnection_Id **- FK to `OSSYS_DBCONNECTION`

- 
**State_Id **- FK to `OSSYS_ASYNC_OP_STATE`