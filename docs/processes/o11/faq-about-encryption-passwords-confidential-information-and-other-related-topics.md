---
title: FAQ about encryption, passwords, confidential information and other “related” topics
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/2675933544/FAQ+about+encryption+passwords+confidential+information+and+other+related+topics
confluence_space: RCP
confluence_page_id: 2675933544
last_synced: 2026-04-09
owner: Process Engineering
---

# FAQ about encryption, passwords, confidential information and other “related” topics

This document contains a list of frequently asked questions regarding the way our product deals with encryption. It should provide answers to most questions that we get asked.

**This document and any of its contents are restricted and cannot be shared with the customer!**

If you need to share any of the contents of this document with a customer, please reach out to R&amp;D in #rd-o11-public, state the use case and ask for explicit permission.
# 
Generic questions## How does OutSystems deal with confidential information, such as user passwords and confidential settings?
Everything that you need to know around those topics can be found in this [official forum post](https://www.outsystems.com/forums/discussion/16666/secure-confidential-information).
## Can you share details about the metamodel where passwords/confidential settings/whatever is stored?
No.
## Which kind of information is stored in RabbitMQ? What information will be leaked if an attacker gains access to the RabbitMQ credentials?
RabbitMQ is used as a cache invalidation mechanism and it does not store any database data. RabbitMQ may store partial application information, but this will depend on the exact application and how it is developed. If customers are concerned about this, they should enable the [RabbitMQ Management plugin](https://success.outsystems.com/Support/Enterprise_Customers/Maintenance_and_Operations/Cache_Invalidation_in_OutSystems_11/RabbitMQ_management_and_troubleshooting) as stated in our official documentation and verify the kind of data that is being stored.
# Passwords## How are user passwords stored at rest?
User passwords are salted and hashed before being stored in the DB. Each password has its own salt, which is a 32 bytes random number. Salts are generated using a random number generator, seeded with a source of high-entropy, which generates secure random numbers when the password is stored in the DB for the first time.

User passwords are stored in the DB using a mechanism that relies on the algorithm version, the password&rsquo;s salt, the computed password hash and some limiters that ease our parsing.
## Does each user have a unique salt?
Yes.

* From ** : This depends on how the question is made.*
*While &quot;technically&quot; is unique since it's random each time, I would interpret this question as &quot;if I manage to copy a known password hash from a user to another, would I be able to login as that second user?&quot;. The answer would be yes.*

*In the past (actually,&nbsp;the current Users module has this really bad implemented, do not recommend it) there was an option to also salt the password with the Username. That would be a (bad) way to also make it unique on top of the random salt.*
## Where does OutSystems store each password&rsquo;s salt?
It is stored together with the hashed password in the database.
## Which hashing algorithm does the OutSystems Platform use?
OutSystems Platform uses SHA512 for hashing. Check [https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/325582887/Cryptography+algorithms+and+keys](https://www.google.com/url?q=https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/325582887/Cryptography%2Balgorithms%2Band%2Bkeys&amp;sa=D&amp;source=editors&amp;ust=1628604427032468&amp;usg=AOvVaw1lQVc-4TsnM3-xTbLSXF-l).
## Can you share further details?
No.

* From ** : SHA512 is enough to make it deterministic. Not much else to share.*
# Confidential settings
What does OutSystems consider a confidential setting?

Database credentials (both for the platform database and any external database integration), email server password, module &ldquo;Run As&rdquo; credentials, SOAP/REST consume credentials, etc.
## How does OutSystems deal with confidential settings and where are they stored?
Confidential settings are encrypted with a secret key generated during the platform installation and stored in a private file in the server.

These settings are stored using a mechanism that relies on the algorithm version, an initialization vector (IV), generated using a secure random number generator seeded with a source of high-entropy for the algorithm, the encrypted setting and some limiters that eases our parsing.

Connection strings for databases, be it the platform or an external one, are stored in .config files (ex: machine.config). The full connection string is encrypted, encoded using Base64 and stored in the file.
## Does each confidential setting have a unique IV?
Yes.
## Where does OutSystems store each confidential setting&rsquo;s IV?
It is stored together with the confidential setting, both in the database and some .config files.
## Which encryption algorithms does the OutSystems Platform use?
OutSystems Platform uses AES-128 in **CBC** mode and **PKCS7** padding mode for encryption. AES-256 is also used.
## Can you disclose where AES-128 or AES-256 is used?
No.
## If an attacker gains access to the database, will the attacker be able to decrypt the confidential settings?
In order to decrypt a confidential setting, the attacker will also need to gain access to the secret key, which is stored in the file system.
## Can you share further details?
No.
# Cryptography## Does OutSystems implement their own cryptography?
No. OutSystems uses both SHA-512 for hashes and AES for encryptions. We use the libraries provided by .Net Framework.
## How does OutSystems perform the encryption, and when/how does the decryption apply to the processes?
Encryption is done when the encrypted parameter is defined or has its value changed. When the platform is installed, we generate a key that is unique per environment, and from there we calculate the encryption key. Decryption is done at runtime when the encrypted value is used, either by the services of the platform or by the application runtime.
# Security Scans## The JQuery version used by the OutSystems Platform has vulnerabilities. When do you plan to upgrade the jQuery version?
Some tools can falsely flag OutSystems applications with security vulnerabilities. You can check more about that in our [official documentation](https://success.outsystems.com/Support/Enterprise_Customers/Troubleshooting/FALSE_POSITIVE_-_jquery-ui-dialog_flagged_as_a_potentially_vulnerable_library). Since the platform makes no use of the closeText UI Dialog parameter the platform is not vulnerable even though JQueryUI is (this will change after RPM-447).

We will not update the JQuery version used by the OutSystems Platform. Instead, we are porting the fixes to any security vulnerabilities that affect the OutSystems Platform to the versions we use.
## .config files have &ldquo;password&rdquo; entries for email, REST and SOAP integrations that are being consumed (for example) and they are empty. Does it mean that we are using an empty password? Does it mean there is no authentication being done?
Regarding email, these credentials are for the external email server that OutSystems is configured to use. If you have not entered any such credentials, they will be empty. That does not mean that the external email server is insecure, it just means that the platform is not configured to use any email server.

Regarding REST and SOAP consumption, OutSystems respects whatever authentication mechanism is in place by whatever software is exposing the REST and SOAP endpoints. If the endpoints are being exposed by another OutSystems application, the developer can set those endpoints to require appropriate authentication. If the endpoints are being exposed by an external system, it is up to the system to define appropriate authentication mechanisms that must be respected by anyone consuming their API.

OutSystems allows developers to define the credentials for consumed REST and SOAP APIs at development time, and also to change the effective value of these credentials at runtime. This allows an application to have the same code in development and production environments, with the only difference being the credentials that are used.

If the entries related to credentials for REST and SOAP consume are empty in the .config files, this means that the application is using whatever credentials were entered during development time.
## Can we remove those empty password entries from .config files?
No.
## Security scan detected that some endpoints do not have CSRF tokens
Debugging endpoints are only used for debugging. Debugging is turned off by default in production environments. It's a feature to be used mostly on non-production environments and only in very dire circumstances should it be used on production environments. As such, these endpoints do not need CSRF protection. This is a false positive.

More details here: R11PIT-246ef8955cb-cb21-32a7-b692-01ace42388d6System JIRA .