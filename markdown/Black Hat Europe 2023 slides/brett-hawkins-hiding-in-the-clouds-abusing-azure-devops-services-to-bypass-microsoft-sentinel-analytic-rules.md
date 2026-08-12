---
title: "Hiding in the Clouds Abusing Azure DevOps Services to Bypass Microsoft Sentinel Analytic Rules"
speakers: ["Brett Hawkins"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2023"
edition: "Europe"
year: 2023
source_pdf: "Black Hat Europe 2023 slides/Brett Hawkins_Hiding in the Clouds Abusing Azure DevOps Services to Bypass Microsoft Sentinel Analytic Rules.pdf"
pages: 82
sha256: "fcc431aadc9228789bca78527ee0a7a5e8a355c33a37c9f74c7c2c7f0aa1314e"
text_chars: 25869
ocr_pages: 6
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:10:34Z"
---
# Hiding in the Clouds Abusing Azure DevOps Services to Bypass Microsoft Sentinel Analytic Rules

**Speakers:** Brett Hawkins  
**Conference:** Black Hat Europe 2023  
**Source:** `Black Hat Europe 2023 slides/Brett Hawkins_Hiding in the Clouds Abusing Azure DevOps Services to Bypass Microsoft Sentinel Analytic Rules.pdf` (82 pages)


## Slide 1

Hiding in the Clouds: Abusing Azure DevOps Services to Bypass Microsoft Sentinel Analytic Rules

Brett Hawkins (@h4wkst3r) Adversary Services, IBM X-Force Red

Whitepaper :

https://www.ibm.com/downloads/cas/5JKAPVYD

## Slide 2

# Introduction

2

IBM Security / © IBM Corporation 2023

## Slide 3

### Who am I?

https://h4wkst3r.github.io

Current Role Capability Lead, Adversary Services Open-Source Tool Author SharPersist, InvisibilityCloak, SCMKit, ADOKit

Conference Speaker Black Hat, DerbyCon, Wild West Hackin’ Fest, BSides, Hackers Teaching Hackers

IBM Security / © IBM Corporation 2023

3

## Slide 4

### Research Drivers

Threat actors continuing to target DevOps

Lack of comprehensive research/tooling on attacking ADO

Adoption of Effectiveness of cloud-based default Sentinel platforms and rules for ADO services

IBM Security / © IBM Corporation 2023

4

## Slide 5

### Research Goals

Highlight Bring more importance of attention to testing default defending clouddetection rules based DevOps platforms

Inspire future DevOps research

IBM Security / © IBM Corporation 2023

5

## Slide 6

### Attendee Takeaways

How to bypass Awareness of default Sentinel privileged and rules for ADO unprivileged attacks against ADO

How to improve default Sentinel rules for ADO

IBM Security / © IBM Corporation 2023

6

## Slide 7

### What is new in this research?

Using public Testing detection rules as effectiveness of guide on defense Sentinel rules for evasion ADO

Comprehensive New methods to Discovery and approach to retrieve pipeline abuse of attacking ADO secrets that undocumented along with new bypass ADO REST API method tool (ADOKit) security controls for code recon

Abuse of authentication cookie for interacting with ADO REST API

7

IBM Security / © IBM Corporation 2023

## Slide 8

### My Perspective

### I am

− Current : Red Teamer

− Previous : Blue Teamer

I am not

−DevOps Engineer

−Software Engineer

−Cloud Engineer

−Detection Engineer

IBM Security / © IBM Corporation 2023

8

## Slide 9

### Prior Work

−Joosua Santasalo ( @SantasaloJoosua )

Links to prior work provided in whitepaper and appendix slides in this presentation

- −Sami Lamppu ( @samilamppu )

−Thomas Naunheim ( @Thomas_Live )

- −Matthew Lucas

- −Jev Suchoi ( @DevJevNL )

−Melvin Langvik ( @Flangvik )

- −Pascal Naber

IBM Security / © IBM Corporation 2023

9

## Slide 10

# Azure DevOps Services

IBM Security / © IBM Corporation 2023

10

## Slide 11

### History

2005

Team Foundation Server (TFS) TFS Server Visual Studio Team Services (VSTS)

2019

Azure DevOps (ADO) Azure DevOps Server Azure DevOps Services

IBM Security / © IBM Corporation 2023

11

## Slide 12

### Azure DevOps Server vs Azure DevOps Services

Cloud
On-Premise
Azure DevOps Server
VS
Azure DevOps Services
Research Focus

IBM Security / © IBM Corporation 2023

12

## Slide 13

### Common Terminology

Azure  Azure  Azure  Azure  Azure  Azure
Boards Repos Artifacts Boards Repos Artifacts
Team
Azure  Azure  Azure  Azure
Pipelines Test Plans Pipelines Test Plans
Team
Project Project
Azure  Azure  Azure  Azure  Azure  Azure
Team
Boards Repos Artifacts Boards Repos Artifacts
Azure  Azure  Azure  Azure
Pipelines Test Plans Pipelines Test Plans
Team
Project Project
Collection/Organization

IBM Security / © IBM Corporation 2023

13

## Slide 14

### Access and Authorization

Web Interface Access at https://dev.azure.com/{yourOrganization}

REST API Programmatic access via OAuth 2.0 or personal access tokens

IBM Security / © IBM Corporation 2023

14

## Slide 15

### REST API

###### Different scopes can be applied for below components

Agent Pools Analytics Audit Log Build
Code Entitlements Extensions Graph &
Identity
Load Test Machine Group Marketplace Notifications
Packaging Project and Team Release Security
Service Connections Settings Symbols Task Groups
Team Dashboard Test Management Tokens User Profile
Variable Groups Wiki Work Items

IBM Security / © IBM Corporation 2023

15

## Slide 16

### Project Security Groups

Build Administrators

Project Administrators

Project Valid Users

Release Administrators

Contributors

Readers

IBM Security / © IBM Corporation 2023

16

## Slide 17

### Organization/Collection Security Groups

Project Collection Administrators

Project Collection Build Administrators

Project Collection Build Service Accounts

Project Collection Service Accounts

Project Collection Project Collection Proxy Service Test Service Accounts Accounts

Project Collection Valid Users

Project-Scoped Security Users Service Groups

IBM Security / © IBM Corporation 2023

17

## Slide 18

### Logging

Auditable Event

Audit Log AzureDevOpsAuditing schema

Log Stream

IBM Security / © IBM Corporation 2023

18

## Slide 19

### Microsoft Sentinel Rules for Azure DevOps

Several open-source default rulesets for many Microsoft services

- 18 default rules for Azure DevOps

https://github.com/Azure/Azure-Sentinel

IBM Security / © IBM Corporation 2023

19

## Slide 20

# Attacking Azure DevOps Services

IBM Security / © IBM Corporation 2023

20

## Slide 21

### Initial Access

- Username/Password

- Personal Access Token (PAT)

- Authentication Cookie

IBM Security / © IBM Corporation 2023

21

## Slide 22

### Initial Access – Username/Password

IBM Security / © IBM Corporation 2023

22

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Initial Access — Username/Password
BE Microsoft
Enter password
evcccccccccccccccccs|
© user3
Forgot my password
Cc Azure DevOps
ThislsTestOrganization1 ThislsTestOrganization1
New organization Projects Myworkitems My pull requests
TestProject2
IBM Security / © IBM Corporation 2023
22
```

## Slide 23

### Initial Access – PAT

Base64 encode PAT to be used against REST API methods

IBM Security / © IBM Corporation 2023

23

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Initial Access — PAT
Base64 encode PAT to be used against
REST API methods
1BM Security / © IBM Corporation 2023
ia$
>>>
>>>
>>>
>>>
python
import base64
pat = ":" + “yourPAT"
patBytes = pat.encode("ascii")
b64Bytes = base64.b64encode(patBytes)
>>> b64PAT = b64Bytes.decode("“ascii")
>>> print (b64PAT)
EncodedPATWillBeOutputHere
>>>
curl -i -s -k -X $'GET'
-H $'User-Agent: Some User Agent’
-H $'Authorization:
-H $'Content-Type: application/json'
Basic base64EncodedPAT '
-H $'Host: dev.azure.com' $'https://dev.azure.com/YourOrganization '
23
```

## Slide 24

### Initial Access – Authentication Cookie

- UserAuthentication cookie scoped to .dev.azure.com

- Valid for 7 days by default

IBM Security / © IBM Corporation 2023

24

## Slide 25

# Reconnaissance

IBM Security / © IBM Corporation 2023

25

## Slide 26

### Reconnaissance

Type Perform via  Perform via
Web Interface? REST API?
Projects Yes Yes
Repositories No Yes
Files Yes Yes
Code Yes Yes
Users Yes Yes
Groups Yes Yes

IBM Security / © IBM Corporation 2023

26

## Slide 27

### Detections for Reconnaissance Techniques

- No Detections by default Microsoft Sentinel Rules for ADO

- Reconnaissance activities are not auditable events

- Therefore, not included in AzureDevOpsAuditing schema

IBM Security / © IBM Corporation 2023

27

## Slide 28

# Persistence

28

IBM Security / © IBM Corporation 2023

## Slide 29

### Persistence

Type Perform via  Perform via
Web Interface? REST API?
Personal Access Tokens Yes Yes
SSH Keys Yes Yes

IBM Security / © IBM Corporation 2023

29

## Slide 30

### Detections for Persistence Techniques

- No Detections by default Microsoft Sentinel Rules for ADO

- Creation of SSH Key and PAT are auditable events

- New detection rule included in this research

IBM Security / © IBM Corporation 2023

30

## Slide 31

# Privilege Escalation

IBM Security / © IBM Corporation 2023

31

## Slide 32

### Add User to Privileged Group

Add User To: Detected? Project Administrators Yes Build Administrators No Add User To: Detected? Project Collection Administrators Yes Project Collection Build No Administrators Project Collection Build Service No Accounts Project Collection Service Yes Accounts

IBM Security / © IBM Corporation 2023

32

## Slide 33

### Modify Build Pipeline

- azure-pipelines.yml file in root of repository

- Modification triggers pipeline to run

- No Detections by default Microsoft Sentinel Rules for ADO

IBM Security / © IBM Corporation 2023

33

## Slide 34

#### Compromise On-Premise Host via Self-Hosted Agent

3
Attacker C2 Infrastructure
4
1 2
Attacker Azure DevOps Services
Target Organization
IBM Security / © IBM Corporation 2023

IBM Security / © IBM Corporation 2023

34

## Slide 35

### Retrieve Build Variables and Pipeline Secrets

- Build Variable Values – Cleartext

- Pipeline Secret Values – Hidden

   - Build Variable Secrets

   - Azure Key Vault Secrets

   - Service Connection Credentials

- Secret values cannot be displayed in original form

IBM Security / © IBM Corporation 2023

35

## Slide 36

### Retrieve Build Variables and Pipeline Secrets

- Bypass security control for displaying secrets by displaying secret in different form:

   - •Halves

   - •Reverse

   - •And more

- No Detections by default Microsoft Sentinel Rules for ADO

IBM Security / © IBM Corporation 2023

36

## Slide 37

# Defense Evasion

37

IBM Security / © IBM Corporation 2023

## Slide 38

### Create Agent Pool

- Allows attacker more flexibility

   - Using agent pool owned by attacker rather than organization

- Pipeline execution would be performed in the attacker owned agent pool

IBM Security / © IBM Corporation 2023

38

## Slide 39

### Create Agent Pool

- After attacker finished with agent pool, they would then delete it to cover tracks

- Detected by “Azure DevOps Agent Pool Created Then Deleted” Sentinel rule

IBM Security / © IBM Corporation 2023

39

## Slide 40

### Disable Audit Stream

- Audit streams used to send logs to SIEM

- Attacker can disable audit stream so activities are not sent to SIEM

- Detected by “Azure DevOps Audit Stream Disabled” Sentinel rule

IBM Security / © IBM Corporation 2023

40

## Slide 41

### Reduce Log Retention

- Attacker may want to reduce evidence of malicious pipeline activity

- Lowest value to keep logs is 1 day

- Detected by “Azure DevOps Retention Reduced” Sentinel rule

IBM Security / © IBM Corporation 2023

41

## Slide 42

### Add External Package Source

- Can inject malicious packages into pipeline by adding new source

- Detected by “External Upstream Source Added to Azure DevOps Feed” Sentinel rule

IBM Security / © IBM Corporation 2023

42

## Slide 43

### REST API Abuse - Reconnaissance

Type REST API Documentation Projects https://learn.microsoft.com/en-us/rest/api/azure/devops/core/projects Repos https://learn.microsoft.com/en-us/rest/api/azure/devops/git/repositories Files https://learn.microsoft.com/en-us/rest/api/azure/devops/git/items Users https://learn.microsoft.com/en-us/rest/api/azure/devops/graph/users Groups https://learn.microsoft.com/en-us/rest/api/azure/devops/graph/groups Code https://learn.microsoft.com/en-us/rest/api/azure/devops/search

IBM Security / © IBM Corporation 2023

43

## Slide 44

### Code Reconnaissance Undocumented Method

Use of undocumented codeAdvancedQueryResults method in Search REST API

IBM Security / © IBM Corporation 2023

44

## Slide 45

### Detections for Reconnaissance REST API

- No Detections by default Microsoft Sentinel Rules for ADO

- Reconnaissance activities are not auditable events

- Therefore, not included in AzureDevOpsAuditing schema

IBM Security / © IBM Corporation 2023

45

## Slide 46

### REST API Abuse - Persistence

Personal Access Tokens and SSH Keys

- Use Contribution model with stolen cookie

- PATs cannot be used to create other PAT’s or SSH Keys

- No Detections by default Microsoft Sentinel Rules for ADO

IBM Security / © IBM Corporation 2023

46

## Slide 47

### REST API Abuse – Adding User to Group

###### Memberships REST API

• https://learn.microsoft.com/enus/rest/api/azure/devops/graph/memberships/add

IBM Security / © IBM Corporation 2023

47

## Slide 48

### REST API Abuse – Adding User to Group

###### Detected by “Azure DevOps Personal Access Token (PAT) misuse” Sentinel rule

IBM Security / © IBM Corporation 2023

48

## Slide 49

### REST API Abuse – Retrieve Pipeline Variables

###### Build Definitions REST API

- https://learn.microsoft.com/en-us/rest/api/azure/devops/build/definitions

No Detections by default Microsoft Sentinel Rules for ADO

IBM Security / © IBM Corporation 2023

49

## Slide 50

### REST API Abuse – Service Connections Info

###### Service Endpoints REST API

• https://learn.microsoft.com/enus/rest/api/azure/devops/serviceendpoint/endpoints

No Detections by default Microsoft Sentinel Rules for ADO

IBM Security / © IBM Corporation 2023

50

## Slide 51

## Bypassing and Improving Microsoft Sentinel Rules for Azure DevOps

51

IBM Security / © IBM Corporation 2023

## Slide 52

### Bypassing Default Rules

The below rules will be shown how they can be bypassed

- Azure DevOps PAT used with Browser

- Azure DevOps Personal Access Token (PAT) misuse

- Azure DevOps Pipeline modified by a new user

- New PA, PCA, or PCAS added to Azure DevOps

- Azure DevOps Administrator Group Monitoring

IBM Security / © IBM Corporation 2023

52

## Slide 53

### Azure DevOps PAT used with Browser

###### Rule Logic

Bypass

IBM Security / © IBM Corporation 2023

53

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Azure DevOps PAT used with Browser
Rule Logic
Bypass
1BM Security / © IBM Corporation 2023
AzureDevOpsAuditing
| where AuthenticationMechanism startswith "PAT"
// Look for useragents that include a redenring engine
| where UserAgent has_any ("Gecko", "WebKit", "Presto", "Trident", "EdgeHTML", "Blink")
| extend timestamp = TimeGenerated, AccountCustomEntity = ActoxUPN,
—IPCustomEntity = IpAddress
curl -i -s -k -X $'GET'
-H $'Content-Type: application/json'
-H $'User-Agent: Random User Agent '
-H $'Authorization: Basic base64EncodedPAT '
-H $'Host: dev.azure.com'
$'https://dev.azure.com/YourOrganization/ apis/projects?api-version=7.0'
53
```

## Slide 54

### Azure DevOps Personal Access Token misuse

###### Rule Logic

Bypass

IBM Security / © IBM Corporation 2023

54

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Azure DevOps Personal Access Token misuse
Rule Logic
Bypass
1BM Security / © IBM Corporation 2023
// Allowlisted UPNs should likely stay empty
let AllowlistedUpns = datatable(UPN:string) ['foo@bar.com', 'test@foo.com'];
// Operation Name parts that will alert
let HasAnyBlocklist =
ddatatable (OperationNamePart: string) ['Security.','Project.','AuditLog.','Extension.'] ;
// Distinct Operation Names that will flag
let HasExactBlocklist =
ddatatable(OperationName: string) ['Group.UpdateGroupMembership.Add','Library.ServiceCon
nectionExecuted', 'Pipelines.PipelineModified',
'Release.ReleasePipelineModified', 'Git.RefUpdatePoliciesBypassed' | ;
AzureDevOpsAuditing
| where AuthenticationMechanism startswith "PAT" and (OperationName has_any
(HasAnyBlocklist) or OperationName in (HasExactBlocklist) )
ab nel 1 23 Fd lt
curl -i -s -k -X $'PUT'
-H $'Content-Type: application/json'
-H $'User-Agent: Some User Agent’
-H $'Host: vssps.dev.azure.com'
-H $'Content-Length: 0'
-b $'X-VSS-UseRequestRouting=True; UserAuthentication=cookieValue '
I$ https: //vssps.dev.azure.com/YourOrganization/_apis/graph/memberships/userDescrip
ttor/groupDescriptor?api-version=7.0-preview.1'
54
```

## Slide 55

### Azure DevOps Pipeline modified by a new user

###### Rule Logic

Bypass

- The rule is only monitoring release pipelines

- Modify build pipeline instead

   - •Shown in multiple attacks in this research

IBM Security / © IBM Corporation 2023

55

## Slide 56

### New PA, PCA, or PCAS added to Azure DevOps

###### Rule Logic

Bypass

- Doesn’t cover Build Administrators or Project Collection Build Administrators

- Rule is doing exact match on the group names, so Build Administrator doesn’t match Build Administrator s

IBM Security / © IBM Corporation 2023

56

## Slide 57

### Azure DevOps Administrator Group Monitoring

###### Rule Logic

###### Bypass

- Won’t trigger for Project Administrator addition in default state

- Need to set MonitorAllProjects to true and/or add specific projects to ProjectsToMonitor

IBM Security / © IBM Corporation 2023

57

## Slide 58

### Improving Detection of Attacks

The below rule improvements or new rules will be shown:

Default Rule Improvements `o` Azure DevOps Personal Access Token (PAT) misuse `o` New PA, PCA, or PCAS added to Azure DevOps `o` Azure DevOps Administrator Group Monitoring

New Rule Azure DevOps Persistence Technique Detected

IBM Security / © IBM Corporation 2023

58

## Slide 59

Default Rule Improvement : Azure DevOps Personal Access Token misuse

- Rename rule to “Azure DevOps REST API misuse”

- Add authentication method of UserAuthToken cookie as well

   - This can be used to perform REST API actions in addition to PAT

IBM Security / © IBM Corporation 2023

59

## Slide 60

Default Rule Improvement : New PA, PCA, or PCAS added to Azure DevOps Update rule to detect a new user added to Build Administrators or Project Collection Build Administrators

IBM Security / © IBM Corporation 2023

60

## Slide 61

Default Rule Improvement : Azure DevOps Administrator Group Monitoring Set MonitorAllProjects to true to detect adding user to Project Administrators for any project

IBM Security / © IBM Corporation 2023

61

## Slide 62

New Rule : Azure DevOps Persistence Technique Detected Detects the creation of PAT or SSH key via web interface or REST API

IBM Security / © IBM Corporation 2023

62

## Slide 63

### New Rule : Azure DevOps Persistence Technique Detected

IBM Security / © IBM Corporation 2023

63

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
New Rule:
Azure DevOps Persistence Tec
Nnnique Detected
Ss» Azure DevOps Persistence Technique Detected
ES incident ID: 163
& Unassigned Vv New Vv Medium
Owner Status Severity
Description
This will detect the creation of SSH keys or personal access tokens to be
used as persistence.
Alert product names
© Microsoft Sentinel
Evidence
ae 7 01 AO
Events Alerts Bookmarks
4/17/2023, 6:30:56.205 ...
$2S_ServicePrincipal
TimeGenerated [UTC]
AuthenticationMechanism
ActorUPN
ActorDisplayName
lpAddress
UserAgent
OperationName
Details
2023-04-17T18:30:56.2051989Z
$2S_ServicePrincipal
user4
Token. PatCreateEvent
Personal Access Token “eAWXotZg" was created.
tO
IBM Security / © IBM Corporation 2023
63
```

## Slide 64

# ADOKit

IBM Security / © IBM Corporation 2023

64

## Slide 65

### Background

https://github.com/xforcered/ADOKit

REST API Abuse 35 Modules Conduct actions Recon, Privilege programmatically Escalation, Persistence

Authentication Open-Source Supports PAT or Available to Cookie community

IBM Security / © IBM Corporation 2023

65

## Slide 66

IBM Security / © 2023 IBM Corporation

66

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Activities aggressor-Aggressor ~ Nov3 08:35 @
>) Cobalt strike - 7 @
Cobalt Strike View Payloads Attacks Site Management Reporting Help’
rt eon<=no @®+esa
Aw Or
‘= 192.1
‘@
@
] - x64 | hawk | 10088 - x64
```

## Slide 67

# Defensive Considerations

IBM Security / © IBM Corporation 2023

67

## Slide 68

### ADOKit

YARA Rule Snort Rule C# Project Hardcoded user GUID agent string Sentinel Rules Persistence IOC’s Any auditable PAT and SSH key event with names prepended ADOKit with “ADOKit-”

IBM Security / © IBM Corporation 2023

68

## Slide 69

### Azure DevOps Services

1

2

3

Microsoft Best Practices Guide

Integrate proactive secret scanning solution

Implement Sentinel rule improvements for ADO

IBM Security / © IBM Corporation 2023

69

## Slide 70

# Conclusion

70

IBM Security / © IBM Corporation 2023

## Slide 71

###### Detection Rules and Logging

### Opportunities for Improvement

|Detection|Detection|Detection|Logging|Logging|
|---|---|---|---|---|
|Rules|Rules|Rules|||
|Trivial|Need more|Breadth of|Recon|Build|
|Bypasses|tuning and
contribution|coverage for
attacker|activities not
auditable|pipeline
auditable|
||from|lifecycle|events|events|
||community|||coverage|

IBM Security / © IBM Corporation 2023

71

## Slide 72

### Conclusion

01 02 03 Test default Securing Logging and detection rules DevOps developing and perform systems and detection rules tuning personnel is for cloud-based critical services is more important than ever

IBM Security / © IBM Corporation 2023

72

## Slide 73

### Acknowledgements

Thank You to the below people for feedback and support on this research Chris Thompson (@retBandit) John Dwyer (@TactiKoolSec) Matthew DeFir (@chefm4tt) Patrick Fussell (@capt_red_beardz) Sanjiv Kawa(@sanjivkawa)

IBM Security / © IBM Corporation 2023

73

## Slide 74

### Questions?

Twitter: @h4wkst3r

Personal Website : https://h4wkst3r.github.io Whitepaper : https://www.ibm.com/downloads/cas/5JKAPVYD

IBM Security / © IBM Corporation 2023

74

## Slide 75

### Thank you

> © Copyright IBM Corporation 2023. All rights reserved. The information contained in these materials is provided for informational purposes only, and is provided AS IS without warranty of any kind, express or implied. Any statement of direction represents IBM’s current intent, is subject to change or withdrawal, and represent only goals and objectives. IBM, the IBM logo, and [insert other IBM trademarks listed on the <u>IBM Trademarks List—and use serial commas], are trademarks or registered trademarks of International Business Machines Corporation, in the United</u> States and/or other countries. Other product and service names might be trademarks of IBM or other companies. A current list of IBM trademarks is available on <u>ibm.com/trademark.</u>

75

## Slide 76

## Slide 77

##### Appendix - References

- https://www.microsoft.com/en-us/security/blog/2023/07/14/analysis-of-storm-0558-techniques-for-unauthorizedemail-access/

- https://github.com/Cloud-Architekt/AzureAD-Attack-Defense/blob/main/ServicePrincipals-ADO.md

- https://twitter.com/SantasaloJoosua

- https://twitter.com/samilamppu

- https://twitter.com/Thomas_Live

- https://labs.withsecure.com/publications/performing-and-preventing-attacks-on-azure-cloud-environments-throughazure-devops

- https://www.devjev.nl/posts/2022/your-service-connection-credentials-are-mine/

- https://twitter.com/DevJevNL

- https://twitter.com/Flangvik

- https://flangvik.com/azure/devops/privesc/abuse/2020/10/15/from-pipeline-to-production.html

- https://www.linkedin.com/in/pascalnaber/

IBM Security / © IBM Corporation 2023

77

## Slide 78

##### Appendix - References

- https://pascalnaber.wordpress.com/2020/01/04/backdoor-in-azure-devops-to-get-the-password-of-a-serviceprincipal/

- https://www.devjev.nl/posts/2022/i-am-in-your-pipeline-reading-all-your-secrets/

- https://learn.microsoft.com/en-us/azure/devops/server/tfs-is-now-azure-devops-server?view=azure-devops

- https://learn.microsoft.com/en-us/azure/devops/user-guide/about-azure-devops-services-tfs?view=azure-devops

- https://jfrog.com/artifactory/

- https://learn.microsoft.com/en-us/azure/devops/project/navigation/glossary?view=azure-devops

- https://learn.microsoft.com/en-us/rest/api/azure/devops/?view=azure-devops-rest-7.1

- https://learn.microsoft.com/en-us/azure/devops/integrate/get-started/authentication/oauth?view=azure-devops

- https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-toauthenticate?view=azure-devops&tabs=Windows

- https://learn.microsoft.com/en-us/azure/devops/integrate/get-started/authentication/oauth?view=azuredevops#scopes

IBM Security / © IBM Corporation 2023

78

## Slide 79

##### Appendix - References

- https://learn.microsoft.com/en-us/azure/devops/organizations/security/permissions?view=azuredevops&tabs=preview-page#project-level-groups

- https://learn.microsoft.com/en-us/azure/devops/organizations/security/permissions?view=azuredevops&tabs=preview-page#collection-level-groups

- https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/azuredevopsauditing

- https://learn.microsoft.com/en-us/azure/devops/organizations/audit/auditing-events

- https://learn.microsoft.com/en-us/azure/sentinel/overview

- https://learn.microsoft.com/en-us/azure/devops/organizations/audit/auditing-streaming

- https://learn.microsoft.com/en-us/azure/sentinel/detect-threats-built-in

- https://github.com/Azure/Azure-Sentinel/tree/master/Solutions/AzureDevOpsAuditing/Analytic%20Rules

- https://ss64.com/bash/curl.html

- https://github.com/GhostPack/SharpDPAPI

- https://learn.microsoft.com/en-us/azure/devops/project/search/get-started-search?view=azure-devops#searchfeatures-usage-and-examples

IBM Security / © IBM Corporation 2023

79

## Slide 80

##### Appendix - References

- https://linux.die.net/man/1/ssh-keygen

- https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/reference/?view=azurepipelines&viewFallbackFrom=azure-devops

- https://git-scm.com/downloads

- https://learn.microsoft.com/en-us/azure/devops/pipelines/release/?view=azure-devops

- https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started/what-is-azure-pipelines?view=azure-devops

- https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/agents?view=azure-devops&tabs=browser

- https://azure.microsoft.com/en-us/products/key-vault/

- https://learn.microsoft.com/en-us/azure/devops/pipelines/library/service-endpoints?view=azure-devops&tabs=yaml

- https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/pools-queues?view=azuredevops&tabs=yaml%2Cbrowser

- https://learn.microsoft.com/en-us/azure/devops/artifacts/concepts/feeds?view=azure-devops

IBM Security / © IBM Corporation 2023

80

## Slide 81

##### Appendix - References

- https://learn.microsoft.com/en-us/rest/api/azure/devops/core/projects?view=azure-devops-rest-7.0

- https://learn.microsoft.com/en-us/azure/devops/extend/develop/contributions-overview?view=azure-devops

- https://learn.microsoft.com/en-us/rest/api/azure/devops/git/repositories?view=azure-devops-rest-7.0

- https://learn.microsoft.com/en-us/rest/api/azure/devops/git/items?view=azure-devops-rest-7.0

- https://learn.microsoft.com/en-us/rest/api/azure/devops/search/?view=azure-devops-rest-7.0

- https://learn.microsoft.com/en-us/rest/api/azure/devops/graph/users?view=azure-devops-rest-7.0

- https://learn.microsoft.com/en-us/rest/api/azure/devops/graph/groups?view=azure-devops-rest-7.0

- https://learn.microsoft.com/en-us/rest/api/azure/devops/graph/memberships/add?view=azure-devops-rest7.0&tabs=HTTP

- https://learn.microsoft.com/en-us/rest/api/azure/devops/build/definitions?view=azure-devops-rest-7.0

- https://learn.microsoft.com/en-us/rest/api/azure/devops/serviceendpoint/endpoints?view=azure-devops-rest-7.0

- https://github.com/xforcered

- https://github.com/xforcered/ADOKit

IBM Security / © IBM Corporation 2023

81

## Slide 82

##### Appendix - References

- https://yara.readthedocs.io/en/stable/writingrules.html

- https://snort.org/

- https://learn.microsoft.com/en-us/azure/devops/organizations/security/security-best-practices?view=azure-devops

- https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-devops-introduction

- https://www.ibm.com/downloads/cas/5JKAPVYD

IBM Security / © IBM Corporation 2023

82
