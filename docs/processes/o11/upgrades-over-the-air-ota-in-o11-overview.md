---
title: Upgrades over-the-air (OTA) in O11 - Overview
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/3581411739/Upgrades+over-the-air+OTA+in+O11+-+Overview
confluence_space: RCP
confluence_page_id: 3581411739
last_synced: 2026-04-09
owner: Process Engineering
---

# Upgrades over-the-air (OTA) in O11 - Overview

References used to create this Document and Disclaimer:

This documentation proposal intends to create a centralized source of knowledge by extending the following articles and sources:

How do the over-the-air updates work 

Calculating the Hash value of Mobile resources &nbsp;

[https://success.outsystems.com/Documentation/11/Delivering_Mobile_Apps/Mobile_App_Update_Scenarios](https://success.outsystems.com/Documentation/11/Delivering_Mobile_Apps/Mobile_App_Update_Scenarios)&nbsp;

[https://docs.google.com/document/d/1vrHOaSh9_72rboG8rA-CgULw4qDI3WxPboXaP4zu2Q0/edit#heading=h.oc2dbe79ksc2](https://docs.google.com/document/d/1vrHOaSh9_72rboG8rA-CgULw4qDI3WxPboXaP4zu2Q0/edit#heading=h.oc2dbe79ksc2) &nbsp;

[https://docs.google.com/spreadsheets/d/1x6A0W342aOAge_7Z13MYBIXoBR1GQnFiywEFX_F_2Dc/edit#gid=0](https://docs.google.com/spreadsheets/d/1x6A0W342aOAge_7Z13MYBIXoBR1GQnFiywEFX_F_2Dc/edit#gid=0) &nbsp;

[https://docs.google.com/presentation/d/1WcbxTF0Jq1CKEHxEijq_cD4R_-4ye5Q8dB9xEGk6R5k/edit#slide=id.p4](https://docs.google.com/presentation/d/1WcbxTF0Jq1CKEHxEijq_cD4R_-4ye5Q8dB9xEGk6R5k/edit#slide=id.p4) &nbsp;

[https://docs.google.com/document/d/1D0SzAjUA5psuKqpvAcNAqGFZFjRTtKkE8yYG5PDnbaw/edit#heading=h.blann38he5yt](https://docs.google.com/document/d/1D0SzAjUA5psuKqpvAcNAqGFZFjRTtKkE8yYG5PDnbaw/edit#heading=h.blann38he5yt) &nbsp;

[https://docs.google.com/spreadsheets/d/1v39EEmseaFWSPOneQwrIylHPiSrlIcmX9COCuJioCYk/edit#gid=0](https://docs.google.com/spreadsheets/d/1v39EEmseaFWSPOneQwrIylHPiSrlIcmX9COCuJioCYk/edit#gid=0) 

RNMT-4913ef8955cb-cb21-32a7-b692-01ace42388d6System JIRA 
# What are Upgrades OTA?
Upgrades OTA allow Mobile Applications to receive and update their versions on Mobile devices without the need to submit those new versions to the respective store.
# Where do we use them in OutSystems?
Upgrades OTA are available for all Mobile Applications developed in Outsystems, keeping in mind the following important points:

- 
The Mobile App needs to be installed on the Mobile Device. The first installation on the device is typically performed from the respective store, but other distribution methods are available.

- 
By default, Mobile Applications are distributed with Hybrid Updates (that allow Upgrades OTA), but there is a [Technical Preview](https://success.outsystems.com/documentation/11/delivering_mobile_apps/technical_preview_configure_mobile_apps_updates_distribution/) feature that allows changing this configuration to Store-Only Updates. For more details on this configuration see [Configure Mobile Apps Updates Distribution](https://success.outsystems.com/Documentation/11/Delivering_Mobile_Apps/Technical_Preview_-_Configure_mobile_apps_updates_distribution).

There is a set of situations that require the generation of a new Build and redistribution of the App in order to have the associated changes reflected in the Mobile App. For more details on these situations see [Mobile Apps Update Scenarios](https://success.outsystems.com/Documentation/11/Delivering_Mobile_Apps/Mobile_App_Update_Scenarios).
# Overall view of the Upgrade OTA Process#### Server Side:
- 
The mobile app is published in an environment, for instance by clicking the &ldquo;1-Click Publish&rdquo; button in Service Studio or via Lifetime Deployment.

- 
After the Deployment is completed, the Frontends that are serving the requests for this mobile app should all have the new version of the app and respective resources updated.

- 
On the running folder of the mobile app, the file *precache.manifest* will contain the information used for version and integrity control during the OTA

#### Client Side:
- 
The mobile app has an internal mechanism that checks if there is a new version of the app available and an OTA upgrade is needed (these would correspond to changes on the Server side). This happens in the following events:

- 
When the application is opened on the device;

- 
When the user navigates to a different screen;

- 
When a server action is called;

The Upgrades OTA are divided into two types *Seamless upgrades* and *Attention-requiring upgrades*. For more details on the differences see [Mobile Apps Update Scenarios](https://success.outsystems.com/Documentation/11/Delivering_Mobile_Apps/Mobile_App_Update_Scenarios).
# Upgrade OTA simplified Diagram:
A simplified version of the Upgrades OTA for mobile applications OS11
# Common Issues and how to troubleshoot them
Considering that the OTA upgrade is a complex mechanism, there are some scenarios under which it may not be successful. In this section, we are describing some common issues related to this process.

Keep in mind that, if an OTA upgrade fails, the upgrade is rolled back and the application will continue running with the version that was previously cached (before the upgrade started). While this rollback allows the user to continue using the application, runtime issues may occur, for instance when calling a server action that had its structure changed (e.g., modifications in its name or in the input/output parameters).

If the OTA upgrade fails and is rolled back when some new resources were already successfully downloaded, the app will keep those, so the next time that the app tries to perform the OTA upgrade, not all resources are to be downloaded. This is possible due to the use of a checkpoint mechanism, that is triggered several times during the upgrade.

Most of the errors that will be detailed in the subsequent sections are normally observed in the Service Center Error logs.
## Timeout while downloading resources### What are the errors observed?
- 
**Aborting resources download. Failed to download resource &lt;Resource_Path&gt;?&lt;Resource_Hash&gt; with error: The request timed out**.

- 
**Upgrade failed - rolling back to the previous application version.**

### Where is this occurring and what does it mean?
- 
This scenario typically occurs in step 8 (from the previous simplified diagram) when the mobile device is using a poor network connection and/or the OTA upgrade involves downloading large resources.&nbsp;

- 
OutSystems mobile applications have a 30 seconds download timeout per resource, which means that the upgrade will fail with a timeout if a single resource takes longer than the 30s to be downloaded. This value cannot be changed.

### What is the impact of this error on the mobile application?
- 
It&rsquo;s expected that the mobile application will roll back to the previous version cached in the device. Runtime issues may occur depending on the changes introduced in the new version.

### How to overcome this issue?
- 
Reload the mobile application and this will attempt to perform the upgrade OTA again.

- 
Under this scenario, if indeed the new application published in the server includes new and heavy resources, which are consistently failing to get downloaded due to timeouts, you may prevent the issues by generating a new application package and distributing it to the end-users &ndash; the application package will already include all the needed resources.

## Downloaded resources do not match the resources listed in the *moduleinfo*### What are the errors observed?
- 
**Checksum failed for file &lt;Resource_Path&gt;?&lt;Resource_Hash&gt; Received hash: &lt;Resource_Hash&gt; | Calculated hash: &lt;Another_Hash&gt;**

- 
**Failed to store download resource &lt;Resource_Path&gt;?&lt;Resource_Hash&gt; with error: File is corrupt or invalid**.

- 
**Upgrade failed - rolling back to the previous application version.**

### Where is this occurring and what does it mean?
- 
As described in step 9, after downloading each resource from the server, the mobile application will validate whether or not the downloaded file matches the one from the &ldquo;moduleinfo&rdquo; list. To do that, it calculates the hash of the file, based on its content, and compares it with the hash associated with that file in the &ldquo;moduleinfo&rdquo;.

- 
This error means that the content of the &lt;Resource_Path&gt;?&lt;Resource_Hash&gt; downloaded doesn&rsquo;t have the expected hash and is considered corrupt.

- 
There are several reasons for this validation to fail, namely:

- 
If there are any network elements caching resources. In this scenario, the app would be expecting to download a specific resource version (from the server), but if a different version of that same resource is cached in the network interface (e.g., a Load Balancer, a CDN or a Proxy), this problem would occur;

- 
If there is any third-party component manipulating/tampering the resource (e.g., a Load Balancer, a CDN or a Proxy) before it reaches the client (e.g., mobile device), changing its content and consequently changing the value of the hash calculated by the application.&nbsp;

- 
If for some reason (e.g., failed or inconsistent deployment) the resources&rsquo; content deployed in the &ldquo;running&rdquo; folder does not match their hashes in the &ldquo;moduleinfo&rdquo;;

- 
If during the OTA upgrade a new deployment of the application is made in the server. This will cause the app to download resources that are from a newer version of the app and not from the &ldquo;moduleinfo&rdquo; that was fetched at the beginning of the OTA upgrade process.

### What is the impact of this error on the mobile application?
- 
It&rsquo;s expected that the mobile application will roll back to the previous version cached in the device. Runtime issues may occur depending on the changes introduced in the new version.

- 
Impact on the end users may vary, depending on the frequency and delta size of the upgrade OTA.&nbsp;

- 
The most critical expression of this error is when index.html is affected. index.html is the main file of the application and, if it fails to be loaded on the WebView, the application ceases to work, and usually only reinstalling the application fixes it.

### How to overcome this issue?
- 
In any of the possible causing scenarios described above, it is important to understand:

- 
What resource and resource&rsquo;s version failed to be stored, by checking the error message;

- 
What was the version of the resource listed in the &ldquo;moduleinfo&rdquo;;

- 
What version of that resource was deployed in the Frontends during that moment (you will need to get the &ldquo;running&rdquo; folder and calculate its hash);

- 
What is the hash of the same resource, if you download it directly through the browser (again, you will need to calculate its hash);

- 
Calculating the Hash value of Mobile resources 

- 
If any of the hashes above is not consistent, it will give you a hint of where the problem is. Please note that these values should be fetched &ldquo;at the same time&rdquo;, i.e. without any new deployment on the server.

- 
Based on the fact that the Received Hash and Calculated are different, the following points should be reviewed:

- 
If the Hash of a resource on a particular Frontend doesn&rsquo;t match the calculated Hash on the Error log this should mean that this frontend doesn&rsquo;t have the most updated resources:

- 
Double-check if the deployment was performed as expected in all the frontends that are serving the application. For example, if the OutSystems Deployment Service was disabled in one of the Frontends (when the deployment was performed) the respective Frontend will be serving outdated resources and it would cause this error until the correct version is deployed in all frontends.

- 
If there is any network component caching the resources, ensure that this cache is completely purged before reloading the app on the mobile device.

- 
If you have any network element or software that is tampering with the requests (e.g injecting content for monitoring purposes) disable functionality at least temporarily.

## Failed changes in the Local Storage Metamodel due to integrity checks&nbsp;### What are the errors observed?
- 
**sqlite3_step failure: UNIQUE constraint failed: &lt;LocalEntity_PhysicalTable&gt;.&lt;LocalEntity_Attribute&gt;**

- 
**Upgrade failed - rolling back to the previous application version.**

### Where is this occurring and what does it mean?
- 
This occurs when a change in the Metamodel of a Local Entity can&rsquo;t be performed due to a Local DB Integrity Check (e.g changes on the Identifier or a DataTypes) for entities that already contain Data.

- 
This affects only devices that contain data in the affected Local Entities.

### What is the impact of this error on the mobile application?
- 
The mobile application will not be upgraded and will be rolled back to the previous version cached in the device. Errors in Runtime may be expected depending on the changes introduced.

- 
The upgrade of the application resources and the upgrade of the local DB metamodel occur at the same time and only after both are successful the application is correctly upgraded.&nbsp;

### How to overcome this issue?
- 
Roll back the app version published in the environment to the previous version and reassess the changes planned.

- 
In the affected devices the following options will allow overcoming the issue:

- 
Clean the cache and data from the app.

- 
Reinstall the app.

## Changes in Local Entity Attributes data types when they have data in the Device### What are the errors observed?
- 
**Unable to upgrade attribute '&lt;DataTypeA&gt;' data type to &lt;DataTypeB&gt;:**

- 
**Unable to convert databaseValue:'&lt;Value&gt;&nbsp; (length:X)'/deserializedValue:' &lt;Value&gt; (length:X)' from type &lt;DataTypeA&gt; to &lt;DataTypeB&gt;.**

- 
**Upgrade failed - rolling back to previous application version.**

### Where is this occurring and what does it mean?
- 
This occurs when a change in the Metamodel of a Local Entity can&rsquo;t be performed because an Attribute Data Type in the Local Entity can&rsquo;t be converted into another Data Type (e.g changing an attribute data type from Binary to Text) for local entities that already contain Data.

- 
This affects only devices that contain data in the affected Local Entities.

### What is the impact of this error on the mobile application?
- 
The mobile application will not be upgraded and will be rolled back to the previous version cached in the device. Errors in Runtime may be expected depending on the changes introduced.

- 
The upgrade of the application resources and the upgrade local DB metamodel occur at the same time and only after both are successful the application is correctly upgraded.&nbsp;

### How to overcome this issue?
- 
Roll back the app version published in the environment to the previous version and reassess the changes planned.

- 
In the affected devices the following options will allow overcoming the issue:

- 
Clean the cache and data from the app.

- 
Reinstall the app.

# Less Common Errors and how to approach them:## Mobile Device Logs: Unable to find resource &lt;Resource&gt;### What are the errors observed?
- 
**Unable to find resource &lt;Resource&gt;**&nbsp;

- 
This can only be observed by checking the Mobile Device Logs.

### Where is this occurring and what does it mean?
- 
These are debugging logs that can be observed directly on the Device Logs and aren&rsquo;t sent over to Service Center.&nbsp;

- 
These occur whenever WebView requests to load some specific resource that isn&rsquo;t part of a cache frame and thus, the cache will ignore it and allow the request to follow to the remaining interested parts that may be able to respond back with content.&nbsp;

- 
Special cases of these are cordova resources, such as javascript from cordova plugins. These aren&rsquo;t to be served by a cache frame nor from the web, but they are served locally from the shell.&nbsp;

### What is the impact of this error on the mobile application?
- 
These logs are merely informative and only accessible through ADB.

- 
No impact on the End-user is expected.

### How to overcome this issue?
- 
This is just informative and no particular impact is expected based on these Errors

## Service Error Logs: Could not get InputStream while trying to get cache resource&nbsp;&nbsp;### What are the errors observed?
- 
**Could not get InputStream while trying to get cache resource**

### Where is this occurring and what does it mean?
- 
These logs mean that, while the resources are being requested by the WebView to be loaded on it, the associated file is missing on the file system. When this happens, the healing mechanism kicks in which leads us to the Healing logs appearing around the same timeframe.

- 
This is common when the Device is suffering from a lack of disk storage available.

### What is the impact of this error on the mobile application?
- 
The impact on end users depends on the outcome of the healing process. If that fails (the following error should be observed in the logs Healing resource &lt;Resouce&gt; from prebundle: FAILED), the device might be in a state where only an update from the stores could solve.

### How to overcome this issue?
- 
Check the Device Storage available.

- 
Try to reload the App.&nbsp;

- 
If the issue remains, reinstall the App from the Store

## Service Error Logs: Healing resource &lt;Resouce&gt; from prebundle: FAILED### What are the errors observed?
- 
**Healing resource &lt;Resouce&gt; from prebundle: FAILED**

### Where is this occurring and what does it mean?
- 
An attempt to heal a resource is performed by falling back to the resource present in the prebundle.

- 
There's another variant of these logs that show healing from the web instead of from prebundle. This type of log may be accompanied by checksum validation errors (&quot;File is corrupt or invalid&quot;) depending on if the version of the downloaded resource, as it is known on the server, differs from what the local version of the app expects.

### What is the impact of this error on the mobile application?
- 
This type of log is a bit worrying in the sense that they show that the application is in an invalid state and may only recover with an app store update and not an OTA.&nbsp;

### How to overcome this issue?
- 
Try to reload the application.&nbsp;

- 
If the issue remains, reinstall the App from the Store.

## Service Error Logs: Cache manifest file is corrupt or invalid### What are the errors observed?
- 
**Cache manifest file is corrupt or invalid**

### Where is this occurring and what does it mean?
- 
The &ldquo;cache manifest&rdquo; file corresponds to a local and internal representation of the native cache within the application that is not the manifest.json from prebundle or the content obtained from moduleinfo route (https://&lt;app-domain&gt;/&lt;home-eSpace&gt;/moduleservices/moduleinfo) on the server.&nbsp;

- 
This file is created on-demand by OSCache and is, essentially, a persistent state of the cache on a device at a given time.&nbsp;

- 
This can happen if this file gets corrupted for some reason, for example, a lack of disk space in the device.

### What is the impact of this error on the mobile application?
- 
The app will most likely get stuck or fail to start, particularly if this is not the first time the app is running.

### How to overcome this issue?
- 
Check the Device Storage available and reinstall the application from the Store.

## Service Error Logs: Unable to switch to cache version### What are the errors observed?
- 
**Unable to switch to cache version**

### Where is this occurring and what does it mean?
- 
The action &ldquo;switchToVersion&rdquo; is initiated by the client runtime running on the WebView that calls onto the native side to switch to a specific version/cache frame. This is triggered by the OnFinish event (Native Cache) when all application resources were cached.

- 
These errors can occur whenever the client runtime decides to call this method with a version that is not the running version on the native side. In other words, this means a state mismatch between the client runtime and the native side.&nbsp;

### What is the impact of this error on the mobile application?
- 
The mobile application will not be upgraded and will be rolled back to the previous version cached in the device. Errors in Runtime may be expected depending on the changes introduced.

### How to overcome this issue?
- 
Try to reload the App in order to trigger a new application Upgrade OTA.&nbsp;

- 
Check the Device Storage available and reinstall the App from the Store

## Service Error Logs: Failed to load cache manifest: File &lt;FilePath&gt; not found. The file was never created### What are the errors observed?
- 
**Failed to load cache manifest: File &lt;FilePath&gt; not found. The file was never created**

### Where is this occurring and what does it mean?
- 
This error occurs when the Cache Manifest file missing in the device.&nbsp;

- 
This could be caused by an error during the write operation or a prior error that resulted in not even reaching the writing step.

- 
A potential scenario that can lead to this state is by having the application attempting to perform an OTA upgrade to a new version on the server during the first run (which takes place during the Splashscreen animation, before the cache manifest file is written) but somehow getting stuck, possibly due to faulty business logic, a frontend serving the wrong upgrade information, poor network conditions (or any combination of the three).

### What is the impact of this error on the mobile application?
- 
This results in the app getting stuck on the splash screen of the application.

### How to overcome this issue?
- 
Try to reload the App in order to trigger a new application Upgrade OTA.&nbsp;

- 
Check the Device Storage available and reinstall the App from the Store

## Service Error Logs: Failed to close database cannot be closed while a transaction is in progress### What are the errors observed?
- 
**Database &lt;Local_DB_Id&gt; failed to close database cannot be closed while a transaction is in progress**

### Where is this occurring and what does it mean?
- 
This error happens when the application tries to close the database connection on window unload (when the app is closed). Sometimes when this kind of event occurs a transaction may still be happening and this error is issued.

- 
This error is just informative and its existence should not impact the application. This situation occurs more frequently in applications with complex database logic or high data volumes.

### What is the impact of this error on the mobile application?
- 
No impact on the application is expected.

### How to overcome this issue?
- 
No action necessary