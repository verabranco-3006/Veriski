---
title: How To Access the Rings Infrastructure
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/3239608332/How+To+Access+the+Rings+Infrastructure
confluence_space: RKB
confluence_page_id: 3239608332
last_synced: 2026-04-09
owner: Process Engineering
---

# How To Access the Rings Infrastructure

This document is a tutorial that describes how to access the rings infrastructure **in the context of a support case, for troubleshooting or remediation**. In this tutorial we will show how to access the AWS account and Kubernetes cluster of the production runtime stamp in Ring +1. 
# Table of Contents# Tools
- 
[k9s](https://k9scli.io/) (other alternatives: [Octant](https://octant.dev/), [OpenLens](https://github.com/MuhammedKalkan/OpenLens))

- 
[kubectl](https://kubernetes.io/docs/tasks/tools/#kubectl)

- 
[AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

- 
neoctl ([GitHub](https://github.com/OutSystems/neoctl) or [Homebrew](https://github.com/OutSystems/homebrew-odc))

# Get Elevated Permission
We have a Privileged Identity Management (PIM) process in place that enables authorized users to get temporary privileged access to our rings, subject to elevation authorization and auditing.

[This document](https://docs.google.com/presentation/d/1zGGEDu5Ta4bnd-KXgxK-G25d1Og7VKASxtfku7Xk2AA/edit#slide=id.p) describes the steps for requesting higher privileges. If you don&rsquo;t have any eligible assignments, ask them from your Team Lead or Manager

- 
Go to [https://portal.azure.com/](https://portal.azure.com/) 

- 
After authenticating, search for &ldquo;Microsoft Entra Privileged Identity Management&rdquo; service

- 
Select &ldquo;Tasks-&gt;My roles-&gt;Groups&rdquo; on the left tree

- 
Select &ldquo;Activate-&gt;Groups&rdquo; on the left tree

- 
Select the Security Group you want to be added as a member. The name indicates the ring and permission level, &ldquo;ReadOnly&rdquo; or &ldquo;PowerUser&rdquo;.

If you don&rsquo;t see the ring/permission you need, check the assigned permissions with your Team Leader/Manager.

For requests to the IAM team you can email [rd.security.iam@outsystems.com](mailto:rd.security.iam@outsystems.com) or create a Zendesk ticket to group &ldquo;Identity &amp; Access Management (IAM)&rdquo;. 

- 
After selecting the Security Group, select Activate. 

Always specify a valid duration, ticket number and reason. The ticket number should be:

- 
Production Support Case: Zendesk ticket number

- 
Engineering Support Case: Jira issue number

- 
Engineering other: Jira issue number associated to the task you&rsquo;re working on

- 
Wait up until 3 minutes (please note that, although not frequent, it can take more time) 

# Accessing AWS Console## Using neoctl
`neoctl config aws-open &lt;ring&gt; &lt;stamp&gt;`

- 
List of rings: `neoctl config list-rings`

- 
List of stamps: `plat`, `rundev`, `runnp`, `runp`, `id`, `forge`

Example for runp in ring +1: `neoctl config aws-open plus1 runp`
## Using SSO Portal
- 
Search for the account you want in the [AWS SSO Portal](https://outsystems-sso.awsapps.com/start). Accounts list here.

- 
The account you&rsquo;re looking for might not appear right away, if this happens simply re-login in the AWS SSO Portal page.

- 
After selecting the account, click on the Permission you wish.

- 
Select &ldquo;Management Console&rdquo;. You will be redirected to the AWS management console.

# Accessing Kubernetes## Using neoctl
- 
Using `neoctl` select the stamp you want to connect:
`neoctl config use-kubeconfig &lt;ring&gt; &lt;stamp&gt;`

- 
List of rings: `neoctl config list-rings`

- 
List of stamps: `plat`, `rundev`, `runnp`, `runp`, `id`, `forge`

- 
Example for runp in ring +1: 
`neoctl config use-kubeconfig plus1 runp`

- 
Access the Kubernetes resources

- 
Via command line with `kubectl`

- 
Or visually with k9s

- 
Or OpenLens

- 
If you have OpenLens on Windows but `neoctl` on WSL, create symbolic links so that OpenLens can read the necessary configurations and credentials.

If you switch roles, you might need to reset the SSO after making sure the new role is available in the AWS SSO Portal:
`neoctl config reset-sso`
## Using kubectl
- 
Search for the account you want in the [AWS SSO Portal](https://outsystems-sso.awsapps.com/start). Accounts list here.

- 
After selecting the account, click on the Permission you wish.

If you don&rsquo;t see the Permission, try to sign out and sign in again.

- 
Select &ldquo;Command line or programmatic access&rdquo;. Follow the instructions to setup your command line environment. Select &ldquo;Option 2&rdquo;.

- 
Check the list of available AWS clusters with 
`aws eks list-clusters --region &lt;region-code&gt; --profile &lt;profile-name&gt;` 

- 
Add the one you want to connect to your kubeconfig with 
`aws eks update-kubeconfig --region &lt;region-code&gt; --name &lt;cluster-name&gt; --profile &lt;profile-name&gt;`   
Example for runp in ring +1: 
`aws eks update-kubeconfig --region us-east-1 --name runp-osall-us-east-1-01 --profile &lt;profile-name&gt;`

- 
Access the Kubernetes resources via command line with kubectl or visually with k9s.

## How to run SQL queries in Tenant Platform DBs
Refer to this document &rarr; How To Run SQL Queries in Platform DBs