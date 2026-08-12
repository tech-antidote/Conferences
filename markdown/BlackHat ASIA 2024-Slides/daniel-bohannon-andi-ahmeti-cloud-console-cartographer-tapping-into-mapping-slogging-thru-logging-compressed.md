---
title: "Andi Ahmeti- Cloud Console Cartographer Tapping Into Mapping  Slogging Thru Logging"
speakers: ["Daniel Bohannon"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2024"
edition: "ASIA"
year: 2024
source_pdf: "BlackHat ASIA 2024-Slides/Daniel Bohannon _ Andi Ahmeti- Cloud Console Cartographer Tapping Into Mapping  Slogging Thru Logging_compressed.pdf"
pages: 108
sha256: "c5846aa42bc7940db06cd6aca643321d3859efc84b2a37d949c98c19be152b00"
text_chars: 56894
ocr_pages: 39
has_ocr: true
redacted_secrets: 30
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:01:05Z"
---
# Andi Ahmeti- Cloud Console Cartographer Tapping Into Mapping  Slogging Thru Logging

**Speakers:** Daniel Bohannon  
**Conference:** Black Hat ASIA 2024  
**Source:** `BlackHat ASIA 2024-Slides/Daniel Bohannon _ Andi Ahmeti- Cloud Console Cartographer Tapping Into Mapping  Slogging Thru Logging_compressed.pdf` (108 pages)


## Slide 1

ASIA 2024

**Cloud Console Cartographer Tapping Into Mapping > Slogging Thru Logging**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ip pikeachat
PERMISO ASIA 2024
Cloud Console Cartographer
Tapping Into Mapping > Slogging Thru Logging
```

## Slide 2

- **Introduction**

- • **Cloud Logs for Defenders** • **PROBLEM: Noisy Console Logs** • **SOLUTION: Mapping for Clarity** • **Tool Demo + Release**

## Slide 3

**ANDI AHMETI** ASSOCIATE THREAT RESEARCHER Kosovo

@SecEagleAnd1 andi-ahmeti Permiso-io-tools/ **CloudGrappler**

## Slide 4

**DANIEL BOHANNON** PRINCIPAL THREAT RESEARCHER USA

(5 yrs) (2 yrs)

@daniel **h** bohannon daniel **h** bohannon danielbohannon/ **Invoke-Obfuscation** / **Invoke-CradleCrafter** / **Invoke-DOSfuscation** / **Revoke-Obfuscation**

## Slide 5

## **Role of Logs in Threat Hunting & IR**

- Logs = ~~=~~ Visibility

- Enable (if not by default)

- Forward to secondary location

- Process further:

   - Aggregate

- Correlate

- Search for malicious activity

## Slide 6

## **On Prem vs Cloud Logs** _(Dat_ _~~a~~ source, not storage location)_

- Host & network logs

- Native logging vs aftermarket products

- Extremely granular: • E.g. process arguments, image loads, process memory, registry modifications, DNS lookups, network connections, logon types, file writes, **file content** “

- • Numerous fin er rints” in g p

- user/attacker activity

## Slide 7

## **On Prem vs Cloud Logs** _(Dat_ _~~a~~ source, not storage location)_

- Determined by cloud provider

      - –

      - Control plan ~~e~~ management

      - –

      - Data pl ~~a~~ ne usage

   - Delay in log generation

   - Retention limits (if not forwarded)

- **Introduction**

- • Far less granular / more abstracted

- •• **Cloud Logs for Defenders** “ Fewer fin er rints g p ” in user/attacker

- • **PROBLEM: Noisy Console Logs** activity

• **SOLUTION: Mapping for Clarity**

• **Tool Demo + Release**

## Slide 8

- **Introduction**

- • **Cloud Logs for Defenders** • **PROBLEM: Noisy Console Logs** • **SOLUTION: Mapping for Clarity** • **Tool Demo + Release**

## Slide 9

## **– Cloud Log Example** **~~s~~ Creating a User**

```
{{
"eventTime":"2024-04-01T13:33:37.0000000Z",
"category":"UserManagement",
"userIdentity": { ... },
"result":"success",
"eventSource":"iam.amazonaws.com","activityDisplayName":"Add user",
"eventName":"CreateUser",
"activityDateTime":"2024-04-01T13:33:37.1234567Z",
"awsRegion":"us-east-1","loggedByService":"Core Directory",
"userAgent":"AWS Internal","operationType":"Add",
"requestParameters": {"initiatedBy": {},
"userName":"krileva""targetResources": [
},{
"responseElements": {"id":"db014773-feed-acdc-beef-133337c0ffee",
"user": {"displayName":null,
"arn":"arn:aws:iam::200802171337:user/krileva","type":"User",
"userName":"krileva",
"userPrincipalName":"krileva@permiso.io",
"path":"/","groupType":null,
"userId":"AIDA12345678ABCDEFGHI","modifiedProperties": [ { ... } ]
"createDate":"Apr 1, 20241:33:37 PM"
}
}
],
},
"additionalDetails": [],
"readOnly":false,
"eventType":"Add user",
"eventType":"AwsApiCall",
"createdDateTime":"2024-04-01T13:33:37.1234567Z",
"sessionCredentialFromConsole":"true"
}"fullName":"Core_Directory:UserManagement:Add_user"
}
```

## Slide 10

## **– Cloud Log Querying API vs Forwarded**

- API

   - PRO: Least delayed

   - CON: Limited retention (AWS = 90 da ~~y~~ s, Azure = 30 days)

200802171337

## Slide 11

## **– Cloud Log Querying API vs Forwarded**

- API

   - PRO: Least delayed

   - CON: Limited retention (AWS = 90 da ~~y~~ s, Azure = 30 days)

- Forwarded

   - PRO: Unlimited storage

   - PRO: No API throttling

   - PRO: Easier consumption by other tools

   - CON: Missing event metadata

   - CON: Add’l monitoring

## Slide 12

## **Definition: Console**

```
{
"eventSource":"signin.amazonaws.com",
"eventName":"ConsoleLogin",
...
"eventType":"AwsConsoleSignIn"
}
```

## Slide 13

## **Console Usage in the Wild**

- Threat actors

   - -

   - L ~~U~~ CR 1

      - -

      - ~~a~~ ka GUI vil

   - -

   - L ~~U~~ CR 3

      - 0

      - aka Scattered Spider, Roasted ktapus, -

      - UNC3944, STO ~~R~~ M 0875 (Octo Tempest)

## Slide 14

## **Console Usage in the Wild**

- Threat actors

   - -

   - L ~~U~~ CR 1

      - -

      - ~~a~~ ka GUI vil

   - -

   - L ~~U~~ CR 3

      - 0

      - aka Scattered Spider, Roasted ktapus, -

      - UNC3944, STO ~~R~~ M 0875 (Octo Tempest) `sts:GetFederationToken`

## Slide 15

Users | IAM | Global
Log

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
BB) Users | 1AM | Global
<€< G (_ https://us-east-1.console.aws.amazon.com/iam/home?region=us-east-2#/.. QA’ vy
Identity and Access =X JAM > Users
Management (IAM)
Q Search 1AM Users (3) into
An IAM user is an identity with long-term credentials that is used to interact with AWS in an account.
|Q Search
Dashboard
¥ Access management Cl) Username «| Path
User grou
o Andi Ahmeti /
Users
Roles
Daniel_Bohannon
Policies
Identity providers
No_Permissions
Account settings ——
```

## Slide 16

## **Log**

No_Permissions @ 2008-0217-1337 **SHQIPERMISO1337….**

SHQIPERMISO1337 SHQIPERMISO1337

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
A Users - Microsoft Azure
© https://portal.azure.com/#view/Microsoft_AAD_UsersAndTenants/UserManagementMenuBlade/.. AS @Q AY
a Users
permiso.io ~ Microsoft Entra ID
:
& Allusers
@ Audit logs
D Sign-in logs
% Diagnose and solve problems
& Deleted users
w
+ New user L Download users B Bulk operations V () Refresh & Manage view “ Delete
®
¥ Aas
2 users found
[-] _ Display name t
O ® Andi Ahmeti
im @ Daniel Bohannon
B
User principal name fl User type
andiahmeti@permiso.io [\ Member
daniel.bohannon@permis.... [Member
On-premises sy...
No
No
Identities
SHQIPERMISO13371
SHQIPERMISO1337)
```

## Slide 17

## **Log**

No_Permissions @ 2008-0217-1337 **SHQIPERMISO1337….** SHQIPERMISO1337 SHQIPERMISO1337

SHQIPERMISO1337

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
©) https://portal.azure.com/#view/Microsoft_AAD_UsersAndTenants/UserManagementMenuBlade/.. 3 @ AY Wy cp
,)
HQIPERMISO1337.
a Users
permiso.io ~ Microsoft Entra ID
« + New user L Download users B Bulk operations V () Refresh & Manage view “ Ww Delete
& Allusers (0) ive Di i i B
Autos F Add iter
D Sign-in logs 2 users found
% Diagnose and solve problems O Display name fT User principal name tl. User type On-premises sy... Identities
Manage Oj ® Andi Ahmeti andiahmeti@permiso.io [FY Member No SHQIPERMISO1337I
& Deleted users im @ Daniel Bohannon daniel.bohannon@permis... [Member No SHQIPERMISO13371
Password reset
& User settings
&% Bulk operation results
Troubleshooting + Support
```

## Slide 18

## **Log**

No_Permissions @ 2008-0217-1337 **SHQIPERMISO1337….**

SHQIPERMISO1337 SHQIPERMISO1337

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
©) https://portal.azure.com/#view/Microsoft_AAD_UsersAndTenants/UserManagementMenuBlade/.. 3 @ AY Wy cp
,)
HQIPERMISO1337.
a Users
permiso.io ~ Microsoft Entra ID
« a New user L Download users B Bulk operations V () Refresh & Manage view Y Ww Delete
& Allusers (0) ive Di i i B
Autos F Add iter
D Sign-in logs 2 users found
% Diagnose and solve problems O Display name fT User principal name tl. User type On-premises sy... Identities
Manage Oj ® Andi Ahmeti andiahmeti@permiso.io [FY Member No SHQIPERMISO1337I
& Deleted users im @ Daniel Bohannon daniel.bohannon@permis... [Member No SHQIPERMISO1337\
© Password reset
& User settings
2% Bulk operation results
Troubleshooting + Support
```

## Slide 19

**Log**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
<3
wae
4 ite
GN
qi
oS
ore
NOY.
NO
```

## Slide 20

**Log**

## Slide 21

- **Introduction**

- **Cloud Logs for Defenders**

- • **PROBLEM: Noisy Console Logs** • **SOLUTION: Mapping for Clarity** • **Tool Demo + Release**

## Slide 22

• **Introduction**

• **Cloud Logs for Defenders**

• **PROBLEM: Noisy Console Logs** • **SOLUTION: Mapping for Clarity** • **Tool Demo + Release**

## Slide 23

## Slide 24

## **– – No Permissions 1** **~~/~~ 3 Console Home**

Console Home | Console Home
No_Permissions @ 2008-0217-1337
servicecatalog:ListApplications
ce:GetCostAndUsage

## Slide 25

## **– – No Permissions 1** **~~/~~ 3 Console Home**

Console Home | Console Home
No_Permissions @ 2008-0217-1337
servicecatalog:ListApplications
ce:GetCostAndUsage

## Slide 26

## **– – No Permissions 1** **~~/~~ 3 Console Home**

Console Home | Console Home
No_Permissions @ 2008-0217-1337
servicecatalog:ListApplications
ce:GetCostAndUsage

## Slide 27

## **– – No Permissions 2** **~~/~~ 3 IAM Dashboard**

IAM | Global
No_Permissions @ 2008-0217-1337
servicecatalog:ListApplications
ce:GetCostAndUsage
iam:GetAccountSummary
iam:ListAccountAliases
200802171337:u
200802171337:user/
iam:ListMFADevices
200802171337:u
iam:ListAccessKeys
200802171337:u

## Slide 28

## **– – No Permissions 2** **~~/~~ 3 IAM Dashboard**

IAM | Global No_Permissions @ 2008-0217-1337 _servicecatalog:ListApplications ce:GetCostAndUsage iam:ListAccountAliases_ 200802171337:u _iam:GetAccountSummary_ 200802171337:user/ _iam:ListMFADevices iam:ListAccessKeys_ 200802171337:u

200802171337:u

## Slide 29

200802171337:u

## **– – No Permissions 2** **~~/~~ 3 IAM Dashboard**

200802171337:user/

IAM | Global No_Permissions @ 2008-0217-1337 200802171337:u _servicecatalog:ListApplications ce:GetCostAndUsage_ 200802171337:u _iam:ListAccountAliases iam:GetAccountSummary iam:ListMFADevices iam:GetAccountSummary iam:ListAccessKeys_ 200802171337:u

## Slide 30

200802171337:u

## **– – No Permissions 2** **~~/~~ 3 IAM Dashboard**

200802171337:user/

IAM | Global No_Permissions @ 2008-0217-1337 200802171337:u _servicecatalog:ListApplications ce:GetCostAndUsage_ 200802171337:u _iam:ListAccountAliases iam:GetAccountSummary iam:ListMFADevices iam:ListAccessKeys_ 200802171337:u _iam:GetAccountSummary_

## Slide 31

## **– – No Perm** **~~i~~ ssions 3/3 IA** **~~M~~ Users**

Users | IAM | Global
No_Permissions @ 2008-0217-1337
servicecatalog:ListApplications
ce:GetCostAndUsage
iam:ListAccountAliases
iam:ListUsers
iam:GetAccountSummary
200802171337
200802171337 iam:ListMFADevices
iam:ListAccessKeys
iam:GetAccountSummary

## Slide 32

– –
No Perm i ssions  3/3  IA M  Users
Users | IAM | Global
No_Permissions @ 2008-0217-1337
servicecatalog:ListApplications
ce:GetCostAndUsage
iam:ListAccountAliases
iam:GetAccountSummary
200802171337
200802171337 iam:ListMFADevices
iam:ListAccessKeys
iam:GetAccountSummary
iam:ListUsers

## Slide 33

– –
No Perm i ssions  3/3  IA M  Users
Users | IAM | Global
No_Permissions @ 2008-0217-1337
200802171337
200802171337

iam:ListUsers

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
} No Permissions - 3/3 - IAM Users
@ 0 oO Users | IAM | Global x + |
CG ( _ https://us-east-1.console.aws.amazon.com/iam/home?region=us-east-
Identity and Access =X 1AM > Users
Management (IAM) 8
Q Search JAM Users (0) info CG aE
An IAM user is an identity with long-term credentials that is used to interact with AWS in an account.
Q Search 1 co)
Dashboard
User name a | Path vy | Groups ¥ | Lastactivity v | MFA y | Password
¥ Access management
User groups iam:ListUsers
Users Access denied
aales You don't have permission to To request access, copy the following text and send it to your AWS
administrator. Learn more about troubleshooting access denied errors. {a}
Policies
Identity providers User: arn:awstiam::200802171337:user/No_Permissions Copy
Account settings Service: iam
Action: ListUsers
¥ Access reports On resource(s): arn:aws:iam::200802171337:user/
Access Analyzer Context: no identity-based policy allows the iam:
External access
Unused access
Analyzer settings
Credential report
Organization activity
Service control policies (SCPs)
Related consoles
IAM Identity Center [3
AWS Organizations [4
@) Cloudshelt —_ Feedback Privacy Terms Cookie preferences
```

## Slide 34

– –
No Perm i ssions  3/3  IA M  Users
Users | IAM | Global
No_Permissions @ 2008-0217-1337
{
"Version": "2012-10-17",
"Statement": [
{
"Sid": "VisualEditor0",
"Effect": "Allow",
"Action": " iam:ListUsers ",
"Resource": "*"
}
200802171337
]
200802171337
}

## Slide 35

– –
No Perm i ssions  3/3  IA M  Users
Users | IAM | Global
No_Permissions @ 2008-0217-1337
{
"Version": "2012-10-17",
"Statement": [
{
"Sid": "VisualEditor0",
"Effect": "Allow",
"Action": " iam:ListUsers ",
"Resource": "*"
}
200802171337
200802171337 ]
200802171337
}
Andi_Ahmeti

## Slide 36

## **– Console Mapping IAM Users**

iam:ListUsers
?
?
?
?
?

## Slide 37

_iam:ListUsers ? ? ? ? ?_

## **– Console Mapping IAM Users**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
} Console Mapping - IAM Users
“Open the Hood”
of Console Logs
¢ Full Permissions
* New Environment
(per service)
¢ Excel Spreadsheet
¢« Lots of Coffee
```

## Slide 38

## **– Console Mapping IAM Users**

A

B

C

iam:ListUsers ? ? ? ? ?

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Console Mapping - IAM Users
B Users (3) into [S| octece — (RERRUEERY
‘An IAM user is an identity with lang-term credentials that is used to interact with AWS in an account,
Q Search <1> ©
Oo User name a Path v Groups ¥ Last activity v MFA OV Password
@ Access @ Acces
Andi_Ahmeti Access deni Access |
O Andi Ahmet! é denied denied mi s denied cae
(Chee c ; @ Access @ Acces
‘An IAM user is an identity with long-term credentials that is used to interact with AWS in an account. a) Daniel_Bohannon / denied @ Access denied sdanied @ Access:
Q Search <1 e Access Acces
0 No_Permissions / ® ‘ ® Access denied ® @ Access:
SS denied s denied
User name a Path Vv Groups 7 Last activity v MFA Ov Password
Access denied
You don't have permission to jam:ListUsers. To request access, copy the following text and send it to your AWS es
administrator. Learn more about troubleshooting access denied errors. [3
User: arn:aws:iam::200802171337:user/No_Permissions | G copy Cc a erases eer)
Service: iam Users (3) into CG Delete
Action: ListUsers ‘An IAM user is an identity with long-term credentials that Is used to Interact with AWS in an account,
On resource(s): arn:aws:iam:: 200802171337 :user/
‘ 4 Q Search <1> ©
Context: no identity-based policy allows the iam:ListUsers action
Oo User name a Path v Groups ¥ Last activity v MFA OV Password
——————
O — Andi_Ahmeti / 1 - - - \
Oo Daniel_Bohannon fp 1 - - - |
O —__No_Permissions / 0 @ 5 hours ago Virtual -
```

## Slide 39

**A**

**B**

**C**

## **– Console Mapping IAM Users**

iam:ListUsers ? ? ? ? ?

iam:ListUsers

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
} Console Mapping - IAM Users
A | eventTime = eventNameFull = userAgent = requestParameters = errorCode =
| 2024-03-18 04:13:37.0000 iam:ListUsers AWS Internal AccessDenied
```

## Slide 40

iam:ListUsers ? ? ? ? ?

## **– Console Mapping IAM Users**

|**A**||
|---|---|
||iam:ListUsers|
|**B**||
||iam:ListUsers|
||iam:GetLoginProfile|
|**C**|iam:GetLoginProfile|
||iam:GetLoginProfile|
||iam:ListSigningCertificates|
||iam:ListSigningCertificates|
||iam:ListSigningCertificates|
||iam:ListMFADevices|
||iam:ListMFADevices|
||iam:ListMFADevices|
||iam:ListGroupsForUser|
||iam:ListGroupsForUser|
||iam:ListGroupsForUser|
||iam:ListAccessKeys|
||**iam:**Ge**tAccessKey**LastUsed
Lis
s|
||**iam:**Ge**tAccessKey**LastUsed
Lis
s|

## Slide 41

iam:ListUsers ? ? ? ? ?

## **– Console Mapping IAM Users**

A
iam:ListUsers
B
iam:ListUsers
iam:GetLoginProfile
C iam:GetLoginProfile
iam:GetLoginProfile
iam:ListSigningCertificates
iam:ListSigningCertificates
iam:ListSigningCertificates
iam:ListMFADevices
iam:ListMFADevices
iam:ListMFADevices
iam:ListGroupsForUser
iam:ListGroupsForUser
iam:ListGroupsForUser
iam:ListAccessKeys
iam: GeLis tAccessKey sLastUsed
iam: GeLis tAccessKey sLastUsed

## Slide 42

iam:ListUsers ? ? ? ? ?

## **– Console Mapping IAM Users**

### **A**

### **B**

### **C**

iam:ListUsers
iam:ListUsers
iam:GetLoginProfile
iam:ListSigningCertificates
iam:ListMFADevices
iam:ListGroupsForUser
iam: Ge ListAccessKeys LastUsed
iam:GetAccessKeyLastUsed

## Slide 43

## **– Console Mapping IAM Users**

A iam:ListUsers
iam:ListUsers
?
?
CB ?
iam:ListUsers
?
?
iam:GetLoginProfile
iam:ListSigningCertificates
iam:ListMFADevices
iam:ListGroupsForUser
iam:ListAccessKeys
iam:GetAccessKeyLastUsed
iam:GetAccessKeyLastUsed

## Slide 44

## **– Console Mapping IAM Users**

A

**CB**

iam:ListUsers
iam:ListUsers
iam:GetLoginProfile
iam:ListSigningCertificates
iam:ListMFADevices
iam:ListUsers
iam:ListGroupsForUser
iam:ListAccessKeys
iam:GetLoginProfile
iam:ListSigningCertificates
iam:ListMFADevices
iam:ListGroupsForUser
iam:ListAccessKeys
iam:GetAccessKeyLastUsed
iam:GetAccessKeyLastUsed

## Slide 45

## **~~–~~ Console Mapping IAM Users**

**A**

**CB**

iam:ListUsers
iam:ListUsers
iam:ListUsers $this.AnchorEvents
iam:GetLoginProfile
iam:GetLoginProfile
iam:ListSigningCertificates
iam:ListSigningCertificates
iam:ListMFADevices $this.RequiredEvents
iam:ListMFADevices
iam:ListGroupsForUser
iam:ListGroupsForUser
iam:ListAccessKeys
iam:ListAccessKeys
iam:GetAccessKeyLastUsed $this.OptionalEvents
iam:GetAccessKeyLastUsed
iam:GetAccessKeyLastUsed

## Slide 46

## **~~–~~ Console Mapping OptionalEvents (Background)**

#### `ConsoleHome`

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Console Mapping -
ConsoleHome
eventTime =
eventNameFull
userAgent
(Background)
requestParameters
| 2024-03-18 04:19:43.0000
2024-03-18 04:19:43.0000
| 2024-03-18 04:19:43.0000
2024-03-18 04:19:43.0000
2024-03-18 04:19:43.0000
2024-03-18 04:19:43.0000
2024-03-18 04:19:44.0000
2024-03-18 04:19:44.0000
2024-03-18 04:19:44.0000
2024-03-18 04:19:44.0000
2024-03-18 04:19:44.0000
2024-03-18 04:19:44.0000
2024-03-18 04:19:44.0000
ec2:DescribeRegions
health:DescribeEventAggregates
health:DescribeEventAggregates
health:DescribeEventAggregates
health:DescribeEventAggregates
notifications:ListNotificationHubs
ce:GetCostAndUsage
ce:GetCostForecast
health:DescribeEventAggregates
health:DescribeEventAggregates
health:DescribeEventAggregates
health:DescribeEventAggregates
servicecatalog-appregistry:ListApplications
Mozilla/5.0 (Macintosh; Intel ...
health.amazonaws.com
Mozilla/5.0 (Macintosh; Intel ...
Mozilla/5.0 (Macintosh; Intel ...
health.amazonaws.com
Mozilla/5.0 (Macintosh; Intel ...
Mozilla/5.0 (Macintosh; Intel ...
Mozilla/5.0 (Macintosh; Intel ...
AWS Internal
Mozilla/5.0 (Macintosh; Intel ...
health.amazonaws.com
AWS Internal
Mozilla/5.0 (Macintosh; Intel ...
{"regionSet":{},"allRegions":true}
{"filter":{"eventStatusCodes":["open","
{"filter":{"eventStatusCodes":["open"],
{"filter":{"startTimes":[{"from":"Mar 11|
{"filter":{"startTimes":[{"from":"Mar 1
{"Filter":{"Not":{"Or":[{"Dimensions":{"Values";
{"Filter":{"Not":{"Or":[{"Dimensions":{"Values'
{"filter":{"eventStatusCodes":["open","upcoming
{"filter":{"eventStatusCodes":["open"],"startTi
{"filter":{"eventStatusCodes":["open"],"startTj
{"filter":{"startTimes":[{"from":"Mar 11, 2024
{"maxResults":"100"}
```

## Slide 47

## **~~–~~ Console Mapping OptionalEvents (Background)**

#### `ConsoleHome`

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Console Mapping -
'ConsoleHome
| eventTime = eventNameFull
(Background)
userAgent requestParameters
2024-03-18 04:19:43.0000 ec2:DescribeRegions
2024-03-18 04:19:44.0000
| 2024-03-18 04:19:44.0000
ce:GetCostAndUsage
ce:GetCostForecast
2024-03-18 04:19:44.0000
2024-03-18 04:19:43.0000 health:DescribeEventAggregates
| 2024-03-18 04:19:43.0000
2024-03-18 04:19:44.0000 health:DescribeEventAggregates
| 2024-03-18 04:19:44.0000 health:DescribeEventAggregates
| 2024-03-18 04:19:44.0000 health:DescribeEventAggregates
2024-03-18 04:19:44.0000 health:DescribeEventAggregates
servicecatalog-appregistry:ListApplications
notifications:ListNotificationHubs
Mozilla/5.0 (Macintosh; Intel ... {"regionSet":{},"allRegions":true}
Mozilla/5.0 (Macintosh; Intel ...
Mozilla/5.0 (Macintosh; Intel ...
{"Filter":{"Not":
{"Filter":{"Not":{"Or":[{"Dimensions":{"}
Or":[{"Dimensions":{"
Mozilla/5.0 (Macintosh; Intel ... {"maxResults":"100"}
health.amazonaws.com {"filter":{"startTimes":[{"from":"Mar 1
Mozilla/5.0 (Macintosh; Intel ...
AWS Internal {"filter":{"eventStatusCodes":["open","upcoming
Mozilla/5.0 (Macintosh; Intel ... {"filter":{"eventStatusCodes":["open"],"startTi
health.amazonaws.com {"filter":{"eventStatusCodes":["open"],"startTj
AWS Internal {"filter":{"startTimes":[{"from":"Mar 11, 2024
```

## Slide 48

## **~~–~~ Console Mapping OptionalEvents (Background)**

#### `ConsoleHome`

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Console Mapping -
'ConsoleHome
| eventTime =
eventNameFull
userAgent =
(Background)
requestParameters
2024-03-18 04:19:43.0000 ec2:DescribeRegions
2024-03-18 04:19:44.0000
| 2024-03-18 04:19:44.0000
ce:GetCostAndUsage
ce:GetCostForecast
2024-03-18 04:19:44.0000 servicecatalog-appregistry:ListApplications
eventTime = eventNameFull
Mozilla/5.0 (Macintosh; Intel ...
Mozilla/5.0 (Macintosh; Intel ...
Mozilla/5.0 (Macintosh; Intel ...
Mozilla/5.0 (Macintosh; Intel ...
userAgent
{"regionSet":{},"allRegions":true}
{"Filter":{"Not":
{"Filter":{"Not":{"Or":[{"Dimensions":{"}
Or":[{"Dimensions":{"
{"maxResults":"100"}
requestParameters
2024-03-18 04:19:43.0000
| 2024-03-18 04:19:43.0000
health:DescribeEventAggregates
health:DescribeEventAggregates
2024-03-18 04:19:43.0000 health:DescribeEventAggregates
2024-03-18 04:19:43.0000 health:DescribeEventAggregates
2024-03-18 04:19:43.0000
2024-03-18 04:19:44.0000
notifications:ListNotificationHubs
health:DescribeEventAggregates
2024-03-18 04:19:44.0000 health:DescribeEventAggregates
| 2024-03-18 04:19:44.0000 health:DescribeEventAggregates
2024-03-18 04:19:44.0000 health:DescribeEventAggregates
health.amazonaws.com
Mozilla/5.0 (Macintosh; Intel ...
Mozilla/5.0 (Macintosh; Intel ...
health.amazonaws.com
Mozilla/5.0 (Macintosh; Intel ...
AWS Internal
Mozilla/5.0 (Macintosh; Intel ...
health.amazonaws.com
AWS Internal
{"filter":{"eventStatusCodes":["open","upcoming
{"filter":{"eventStatusCodes":["open"],"startTi
{"filter
"{"startTimes":[{"from":"Mar 11, 2024 4
{"filter":{"startTimes":[{"from":"Mar 11, 2024,
{"filter":{"eventStatusCodes":["open","upco
{"filter":{"eventStatusCodes":["open"],"start
{"filter":{"eventStatusCodes":["open"],"start
{"filter":{"startTimes":[{"from":"Mar 11, 2024 4
```

## Slide 49

## **~~–~~ Console Mapping OptionalEvents (Background)**

#### `ConsoleHome`

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
} Console Mapping - (Background)
eventTime = eventNameFull = userAgent = requestParameters
2024-03-18 04:19:43.0000 ec2:DescribeRegions Mozilla/5.0 (Macintosh; Intel ... {"regionSet":{},"allRegions":true}
2024-03-18 04:19:44.0000 ce:GetCostAndUsage Mozilla/5.0 (Macintosh; Intel ... {"Filter":{"Not":{"Or":[{"Dimensions":{"
2024-03-18 04:19:44.0000 ce:GetCostForecast Mozilla/5.0 (Macintosh; Intel ... {"Filter":{"Not":{"Or":[{"Dimensions":{"
2024-03-18 04:19:44.0000 servicecatalog-appregistry:ListApplications Mozilla/5.0 (Macintosh; Intel ... {"maxResults":"100"}
```

## Slide 50

**~~–~~ Console Mapping OptionalEvents (Context)**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
(Context)
; Console Mapping -
PIPANEB AGE
SVERYVTHENO_ BAGEL
```

## Slide 51

## **~~–~~ Console Mapping OptionalEvents (Context)**

AdministratorAccess/andi.ahmeti@permiso.io
200802171337 AKIA[REDACTED:aws-access-key-id] - Active
AKIA[REDACTED:aws-access-key-id] - Active

## Slide 52

## **~~–~~ Console Mapping OptionalEvents (Context)**

200802171337

AKIA[REDACTED:aws-access-key-id] - Active

AKIA[REDACTED:aws-access-key-id] - Active AdministratorAccess/andi.ahmeti@permiso.io

## Slide 53

## **~~–~~ Console Mapping OptionalEvents (Context)**

AdministratorAccess/andi.ahmeti@permiso.io

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
} Console Mapping - (Context)
| © © © Gi Everything_Bagel|IAM|Globs x | +
<€< G ( _ https://us-east-1.console.aws.amazon.com/iam/home?region=us-east-2#/ A tt
Identity and Access =X Permissions Groups (7) Tags (5) Security credentials Access Advisor ®
Management (IAM) — 9S
Q Search AM User groups membership (1) Add user to groups
Auser group is a collection of IAM users. Use groups to specify permissions for a collection of users. A user can be a member of up to 10 groups at a time.
Group name a | Attached policies (7 v
Dashboard
newUserGroupWith3PoliciesAdded AmazonEC2SpotFleetTaggingRole, AWSQuickSightListlAM an...
¥ Access management
User groups
Users
Roles
Policies
Identity providers
Account settings
¥ Access reports
Access Analyzer
External access
Unused access
Analyzer settings
Credential report
Organization activity
Service control policies (SCPs)
Related consoles
IAM Identity Center
AWS Organizations [4
```

## Slide 54

## **~~–~~ Console Mapping OptionalEvents (Context)**

||AdministratorAccess/andi.ahmeti@permiso.io|
|---|---|
|AKIA[REDACTED:aws-access-key-id]||
|AKIA[REDACTED:aws-access-key-id]||

## Slide 55

## **~~–~~ Console Mapping OptionalEvents (Context)**

AdministratorAccess/andi.ahmeti@permiso.io
200802171337
200802171337
AKIA[REDACTED:aws-access-key-id]

## Slide 56

200802171337

## **~~–~~ Console Mapping OptionalEvents (Context)**

200802171337
AdministratorAccess/andi.ahmeti@permiso.io
AKIA[REDACTED:aws-access-key-id]
AKIA[REDACTED:aws-access-key-id]

APKAPERSHENDETJEMIQ1 APKAPERSHENDETJEMIQ2

## Slide 57

## **AKIA[REDACTED:aws-access-key-id]** **~~–~~ Console Mapping OptionalEvents (Context)**

||AdministratorAccess/andi.ahmeti@permiso.io|
|---|---|
|APKAPERSHENDETJEMIQ1||
|APKAPERSHENDETJEMIQ2||
|APKAPERSHENDETJEMIQ3||
|APKAPERSHENDETJEMIQ4||
|APKAPERSHENDETJEMIQ5||
|Everything_Bagel-at-200802171337||
|Everything_Bagel-at-200802171337_||
|Everything_Bagel+1-at-200802171337||

## Slide 58

## **~~–~~ Console Mapping OptionalEvents (Context)**

|APKAPERSHENDETJEMIQ1|AdministratorAccess/andi.ahmeti@permiso.io|
|---|---|
|APKAPERSHENDETJEMIQ2||
|APKAPERSHENDETJEMIQ3||
|APKAPERSHENDETJEMIQ4||
|APKAPERSHENDETJEMIQ5||
|Everything_Bagel-at-200802171337||
|Everything_Bagel-at-200802171337_||
|Everything_Bagel+1-at-200802171337||
|SHQIP1FUN2ME3MIRE4VONE5SE6KURRE7||

## Slide 59

## **~~–~~** S ~~H~~ QIP1FUN2ME3MIRE4VONE5SE6KURRE7 **Console Mapping OptionalEvents (Context)**

Plain_Bagel | IAM | Global
AdministratorAccess/andi.ahmeti@permiso.io
200802171337

## Slide 60

## **~~–~~** S ~~H~~ QIP1FUN2ME3MIRE4VONE5SE6KURRE7 **Console Mapping OptionalEvents (Context)**

Plain_Bagel | IAM | Global AdministratorAccess/andi.ahmeti@permiso.io 200802171337

## Slide 61

**~~–~~ Console Mapping OptionalEvents (Context)**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
} Console Mapping - (Context)
Permissions Groups Tags Security credentials Access Advisor
eventTime = eventNameFull = userAgent = requestParameters =
2024-03-18 04:21:20.0000 iam:GetUser AWS Internal {"userName":"Plain_Bagel"}
2024-03-18 04:21:20.0000 iam:ListMFADevices AWS Internal {"userName":"Plain_Bagel"}
2024-03-18 04:21:20.0000 iam:ListUserTags AWS Internal {"userName":"Plain_Bagel"}
2024-03-18 04:21:20.0000 iam:ListUserPolicies AWS Internal {"userName":"Plain_Bagel"}
2024-03-18 04:21:20.0000 iam:ListAttachedUserPolicies AWS Internal {"userName":"Plain_Bagel"}
2024-03-18 04:21:20.0000 iam:ListPolicies AWS Internal {"maxltems":1000,"onlyAttached":false}
2024-03-18 04:21:24.0000 iam:ListPolicies AWS Internal {"maxitems":1000,"marker":"AAI1zjUVInJUxBcsOtgybPoPxBF...
2024-03-18 04:21:21.0000 iam:GetLoginProfile aws-internal/3 aws-sdk-java/... {"userName":"Plain_Bagel"}
2024-03-18 04:21:21.0000 access-analyzer:ListPolicyGenerations aws-internal/3 aws-sdk-java/... {"principalArn":"arn:aws:iam::200802171337:user/Plain_Bagel"}
2024-03-18 04:21:20.0000 iam:ListAccessKeys AWS Internal {"userName":"Plain_Bagel"}
2024-03-18 04:21:21.0000 iam:ListAccessKeys aws-internal/3 aws-sdk-java/... {"userName":"Plain_Bagel"}
```

## Slide 62

**~~–~~ Console Mapping OptionalEvents (Context)**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
} Console Mapping -
(Context)
Permissions Groups Tags Security credentials Access Advisor
eventTime = eventTime = eventNameFull = userAgent = requestParameters =
2024-03-18 04:21:20.0000 2024-03-18 04:24:43.0000 iam:GetUser AWS Internal {"userName":"Everything_Bagel"}
2024-03-18 04:21:20.0000 2024-03-18 04:24:43.0000 iam:ListMFADevices AWS Internal {"userName":"Everything_Bagel"}
2024-03-18 04:21:20.0000 2024-03-18 04:24:43.0000 iam:ListUserTags AWS Internal {"userName":"Everything_Bagel"}
2024-03-18 04:21:20.0000 2024-03-18 04:24:43.0000 iam:ListUserPolicies AWS Internal {"userName":"Everything_Bagel"}
2024-03-18 04:21:20.0000 2024-03-18 04:24:43.0000 iam:ListAttachedUserPolicies AWS Internal {"userName":"Everything_Bagel"}
2024-03-18 04:21:20.0000 2024-03-18 04:24:43.0000 iam:GetPolicy AWS Internal {"policyArn":"arn:aws:iam::aws:policy/AdministratorAccess"}
2024-03-18 04:21:24.0000 2024-03-18 04:24:43.0000 iam:ListGroupPolicies AWS Internal {"groupName":"customGroup2"}
2024-03-18 04:21:21.0000 2024-03-18 04:24:43.0000 iam:ListAttachedGroupPolicies AWS Internal {"groupName":"customGroup2"}
2024-03-18 04:21:21.0000
2024-03-18 04:21:20.0000
2024-03-18 04:21:21.0000
2024-03-18 04:24:43.0000
2024-03-18 04:24:43.0000
2024-03-18 04:24:43.0000
2024-03-18 04:24:44.0000
2024-03-18 04:24:44.0000
2024-03-18 04:24:44.0000
2024-03-18 04:24:45.0000
2024-03-18 04:24:45.0000
iam:GetLoginProfile
access-analyzer:ListPolicyGenerations
iam:ListAccessKeys
iam:ListAccessKeys
iam:GetAccessKeyLastUsed
iam:GetAccessKeyLastUsed
iam:GetAccessKeyLastUsed
iam:GetAccessKeyLastUsed
aws-internal/3 aws-sdk-java/...
aws-internal/3 aws-sdk-java/...
AWS Internal
aws-internal/3 aws-sdk-java/...
AWS Internal
AWS Internal
aws-internal/3 aws-sdk-java/...
aws-internal/3 aws-sdk-java/...
{"userName":"Everything_Bagel"}
{"principalArn":"arn:aws:iam::200802171337:user/Everything_Bagel"}
{"userName":"Everything_Bagel"}
{"userName":"Everything_Bagel"}
{"accessKeyld":"AKIA[REDACTED:aws-access-key-id]"}
{"accessKeyld":"AKIA[REDACTED:aws-access-key-id]"}
{"accessKeyld":"AKIA[REDACTED:aws-access-key-id]"}
{"accessKeyld":"AKIA[REDACTED:aws-access-key-id]"}
```

## Slide 63

**~~–~~ Console Mapping OptionalEvents (Context)**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
} Console Mapping -
(Context)
Permissions Groups Tags Security credentials Access Advisor
eventTime = eventTime = eventNameFull = userAgent = requestParameters =
2024-03-18 04:21:20.0000 2024-03-18 04:24:43.0000 iam:GetUser AWS Internal {"userName":"Everything_Bagel"}
2024-03-18 04:21:20.0000 2024-03-18 04:24:43.0000 iam:ListMFADevices AWS Internal {"userName":"Everything_Bagel"}
2024-03-18 04:21:20.0000 2024-03-18 04:24:43.0000 iam:ListUserTags AWS Internal {"userName":"Everything_Bagel"}
2024-03-18 04:21:20.0000 2024-03-18 04:24:43.0000 iam:ListUserPolicies AWS Internal {"userName":"Everything_Bagel"}
2024-03-18 04:21:20.0000 2024-03-18 04:24:43.0000 iam:ListAttachedUserPolicies AWS Internal {"userName":"Everything_Bagel"}
2024-03-18 04:21:20.0000 2024-03-18 04:24:43.0000 iam:GetPolicy AWS Internal {"policyArn":"arn:aws:iam::aws:policy/AdministratorAccess"}
2024-03-18 04:21:24.0000 2024-03-18 04:24:43.0000 iam:ListGroupPolicies AWS Internal {"groupName":"customGroup2"}
2024-03-18 04:21:21.0000 2024-03-18 04:24:43.0000 iam:ListAttachedGroupPolicies AWS Internal {"groupName":"customGroup2"}
2024-03-18 04:21:21.0000
2024-03-18 04:21:20.0000
2024-03-18 04:21:21.0000
2024-03-18 04:24:43.0000
2024-03-18 04:24:43.0000
2024-03-18 04:24:43.0000
2024-03-18 04:24:44.0000
2024-03-18 04:24:44.0000
2024-03-18 04:24:44.0000
2024-03-18 04:24:45.0000
2024-03-18 04:24:45.0000
iam:GetLoginProfile
access-analyzer:ListPolicyGenerations
iam:ListAccessKeys
iam:ListAccessKeys
iam:GetAccessKeyLastUsed
iam:GetAccessKeyLastUsed
iam:GetAccessKeyLastUsed
iam:GetAccessKeyLastUsed
aws-internal/3 aws-sdk-java/...
aws-internal/3 aws-sdk-java/...
AWS Internal
aws-internal/3 aws-sdk-java/...
AWS Internal
AWS Internal
aws-internal/3 aws-sdk-java/...
aws-internal/3 aws-sdk-java/...
{"userName":"Everything_Bagel"}
{"principalArn":"arn:aws:iam::200802171337:user/Everything_Bagel"}
{"userName":"Everything_Bagel"}
{"userName":"Everything_Bagel"}
{"accessKeyld":"AKIA[REDACTED:aws-access-key-id]"}
{"accessKeyld":"AKIA[REDACTED:aws-access-key-id]"}
{"accessKeyld":"AKIA[REDACTED:aws-access-key-id]"}
Keyld":"AKIA[REDACTED:aws-access-key-id]"}
```

## Slide 64

**~~–~~ Console Mapping OptionalEvents (Context)**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
} Console Mapping -
(Context)
Permissions Groups Tags Security credentials Access Advisor
eventTime = eventTime = eventNameFull = userAgent = requestParameters =
2024-03-18 04:21:20.0000 2024-03-18 04:24:43.0000 iam:GetUser AWS Internal {"userName":"Everything_Bagel"}
2024-03-18 04:21:20.0000 2024-03-18 04:24:43.0000 iam:ListMFADevices AWS Internal {"userName":"Everything_Bagel"}
2024-03-18 04:21:20.0000 2024-03-18 04:24:43.0000 iam:ListUserTags AWS Internal {"userName":"Everything_Bagel"}
2024-03-18 04:21:20.0000 2024-03-18 04:24:43.0000 iam:ListUserPolicies AWS Internal {"userName":"Everything_Bagel"}
2024-03-18 04:21:20.0000 2024-03-18 04:24:43.0000 iam:ListAttachedUserPolicies AWS Internal {"userName":"Everything_Bagel"}
2024-03-18 04:21:20.0000 2024-03-18 04:24:43.0000 iam:GetPolicy AWS Internal {"policyArn":"arn:aws:iam::aws:policy/AdministratorAccess"}
2024-03-18 04:21:24.0000 2024-03-18 04:24:43.0000 iam:ListGroupPolicies AWS Internal {"groupName":"customGroup2"}
2024-03-18 04:21:21.0000 2024-03-18 04:24:43.0000 iam:ListAttachedGroupPolicies AWS Internal {"groupName":"customGroup2"}
2024-03-18 04:21:21.0000
2024-03-18 04:21:20.0000
2024-03-18 04:21:21.0000
2024-03-18 04:24:43.0000
2024-03-18 04:24:43.0000
2024-03-18 04:24:43.0000
2024-03-18 04:24:44.0000
2024-03-18 04:24:44.0000
2024-03-18 04:24:44.0000
2024-03-18 04:24:45.0000
2024-03-18 04:24:45.0000
iam:GetLoginProfile
access-analyzer:ListPolicyGenerations
iam:ListAccessKeys
iam:ListAccessKeys
iam:GetAccessKeyLastUsed
iam:GetAccessKeyLastUsed
iam:GetAccessKeyLastUsed
iam:GetAccessKeyLastUsed
aws-internal/3 aws-sdk-java/...
aws-internal/3 aws-sdk-java/...
AWS Internal
aws-internal/3 aws-sdk-java/...
AWS Internal
AWS Internal
aws-internal/3 aws-sdk-java/...
aws-internal/3 aws-sdk-java/...
{"userName":"Everything_Bagel"}
{"principalArn":"arn:aws:iam::200802171337:user/Everything_Bagel"}
{"userName":"Everything_Bagel"}
{"userName":"Everything_Bagel"}
{"accessKeyld":"AKIA[REDACTED:aws-access-key-id]"}
{"accessKeyld":"AKIA[REDACTED:aws-access-key-id]"}
{"accessKeyld":"AKIA[REDACTED:aws-access-key-id]"}
{"accessKeyld":"AKIA[REDACTED:aws-access-key-id]"}
```

## Slide 65

**~~–~~ Console Mapping OptionalEvents (Context)**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
} Console Mapping -
(Context)
Permissions Groups Tags Security credentials Access Advisor
eventNameFull = eventNameFull =
iam:GetUser iam:GetUser
iam:ListMFADevices
iam:ListUserTags
iam:ListUserPolicies
iam:ListAttachedUserPolicies
iam:ListPolicies
iam:ListPolicies
iam:GetLoginProfile
access-analyzer:ListPolicyGenerations
iam:ListAccessKeys
iam:ListAccessKeys
iam:ListMFADevices
iam:ListUserTags
iam:ListUserPolicies
iam:ListAttachedUserPolicies
iam:GetPolicy
iam:ListGroupPolicies
iam:ListAttachedGroupPolicies
iam:GetLoginProfile
access-analyzer:ListPolicyGenerations
iam:ListAccessKeys
iam:ListAccessKeys
iam:GetAccessKeyLastUsed
iam:GetAccessKeyLastUsed
iam:GetAccessKeyLastUsed
iam:GetAccessKeyLastUsed
```

## Slide 66

**~~–~~ Console Mapping OptionalEvents (Context)**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
} Console Mapping - (Context)
Permissions Groups Tags Security credentials Access Advisor
eventNameFull = eventNameFull =
iam:GetUser iam:GetUser
iam:ListMFADevices iam:ListMFADevices
iam:ListUserTags iam:ListUserTags
iam:ListUserPolicies iam:ListUserPolicies
iam:ListAttachedUserPolicies iam:ListAttachedUserPolicies
iam:ListPolicies iam:GetPolicy
iam:ListPolicies iam:ListGroupPolicies
iam:ListAttachedGroupPolicies
iam:GetLoginProfile iam:GetLoginProfile
access-analyzer:ListPolicyGenerations access-analyzer:ListPolicyGenerations
iam:ListAccessKeys jiam:ListAccessKeys
iam:ListAccessKeys iam:ListAccessKeys
iam:GetAccessKeyLastUsed
iam:GetAccessKeyLastUsed
iam:GetAccessKeyLastUsed
iam:GetAccessKeyLastUsed
```

## Slide 67

**~~–~~ Console Mapping OptionalEvents (Context)**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
} Console Mapping -
iam:ListPolicies
(Context)
Permissions Groups Tags Security credentials Access Advisor
eventNameFull = eventNameFull =
iam:GetUser iam:GetUser
iam:ListMFADevices
iam:ListUserTags
iam:ListUserPolicies
iam:ListAttachedUserPolicies
iam:GetLoginProfile
access-analyzer:ListPolicyGenerations
iam:ListAccessKeys
iam:ListAccessKeys
iam:ListMFADevices
iam:ListUserTags
iam:ListUserPolicies
iam:ListAttachedUserPolicies
iam:GetLoginProfile
access-analyzer:ListPolicyGenerations
iam:ListAccessKeys
iam:ListAccessKeys
iam:GetPolicy
iam:ListGroupPolicies
iam:ListAttachedGroupPolicies
iam:GetAccessKeyLastUsed
```

## Slide 68

**~~–~~ Console Mapping OptionalEvents (Context)**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
} Console Mapping -
iam:ListPolicies
(Context)
iam:ListGroupPolicies
iam:ListAttachedGroupPolicies
iam:GetAccessKeyLastUsed
Permissions Groups Tags Security credentials Access Advisor
iam:GetPolicy
eventTime = eventNameFull = userAgent = requestParameters =
2024-03-18 04:23:04.0000 iam:ListAccessKeys AWS Internal {"userName":"Plain_Bagel"}
2024-03-18 04:23:04.0000 iam:ListSigningCertificates AWS Internal {"userName":"Plain_Bagel"}
2024-03-18 04:23:04.0000 iam:ListSSHPublicKeys AWS Internal {"userName":"Plain_Bagel"}
2024-03-18 04:23:04.0000 iam:ListServiceSpecificCredentials AWS Internal {"userName":"Plain_Bagel","serviceName":"cassandra.amazonaw...
2024-03-18 04:23:04.0000 iam:ListServiceSpecificCredentials AWS Internal {"userName":"Plain_Bagel","serviceName":"codecommit.amazona...
eventTime = eventNameFull = userAgent = requestParameters =
2024-03-18 04:25:29.0000 iam:ListAccessKeys AWS Internal {"userName":"Everything_Bagel"}
2024-03-18 04:25:29.0000 iam:ListSigningCertificates AWS Internal {"userName":"Everything_Bagel"}
2024-03-18 04:25:29.0000 iam:ListSSHPublicKeys AWS Internal {"userName":"Everything_Bagel"}
2024-03-18 04:25:29.0000 iam:ListServiceSpecificCredentials AWS Internal {"userName":"Everything_Bagel","serviceName":"cassandra.ama...
2024-03-18 04:25:29.0000 iam:ListServiceSpecificCredentials AWS Internal {"userName":"Everything_Bagel","serviceName":"codecommit.am...
2024-03-18 04:25:29.0000
2024-03-18 04:25:29.0000
iam:GetAccessKeyLastUsed
iam:GetAccessKeyLastUsed
aws-internal/3 aws-sdk-java/...
aws-internal/3 aws-sdk-java/...
{"accessKeyld":"AKIA[REDACTED:aws-access-key-id]"}
{"accessKeyld":"AKIA[REDACTED:aws-access-key-id]"}
```

## Slide 69

**~~–~~ Console Mapping OptionalEvents (Context)**

## Slide 70

**~~–~~ Console Mapping OptionalEvents (Context)**

## Slide 71

**~~–~~ Console Mapping OptionalEvents (Context)**

## Slide 72

**CLI vs Console**

## Slide 73

**CLI vs Console**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
vs Console
bash-3.2$
bash-3.2$ aws iam create-user --user-name krileva
{
aws
"User": {
"Path": "/",
"UserName": "krileva",
"UserId": "AIDA12345678ABCDEFGHI",
"Arn": H :iam: :200802171337:user/krileva",
2024-03-22T03: 48:59+00: 00"
}
bash-3.2$ aws iam create-access-key --user-name krileva
{
"AccessKey": {
"UserName": "krileva",
"AccessKeyId": "AKIA[REDACTED:aws-access-key-id]",
"Status": "Active",
"SecretAccessKey": "SHQIP1337PunaEshteShendet4U+po+iRedacted",
"CreateDate": "2024-03-22T03:49:17+00:00"
}
}
bash-3.2$
bash-3.2$ aws iam attach-user-policy --user-name krileva \
> --policy-arn arn:aws: aws:policy/AdministratorAccess
bash-3.2$
```

## Slide 74

## **CLI vs Console**

**1** **2 3**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
vs Console
bash-3.2$
bash-3.2$ aws iam create-user --user-name krileva
{
aws
"User": {
"Path": "/",
"UserName": "krileva",
"UserId": "AIDA12345678ABCDEFGHI",
"Arn": H :iam: :200802171337:user/krileva",
2024-03-22T03: 48:59+00: 00"
}
bash-3.2$ aws iam create-access-key --user-name krileva 2
{
"AccessKey": {
"UserName": "krileva",
"AccessKeyId": "AKIA[REDACTED:aws-access-key-id]",
"Status": "Active",
"SecretAccessKey": "SHQIP1337PunaEshteShendet4U+po+iRedacted",
"CreateDate": "2024-03-22T03:49:17+00:00"
}
}
bash-3.2$
bash-3.2$ aws iam attach-user-policy --user-name krileva \
> --policy-arn arn:aws: aws:policy/AdministratorAccess
bash-3.2$
```

## Slide 75

## **CLI vs Console**

**1 2 3**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
vs Console
aws bash=3-28 eventNameFull = requestParameters =
bash-3.2$ aws iam create-user --user-name krileva 5 7 antes be
{ iam:CreateUser {"userName":"krileva"}
"User": { iam:CreateAccessKey {"userName":"krileva"}
"Path":
"UserName "krileva", iam:AttachUserPolicy {"userName":"krileva","policyArn":"arn:aws:iam::aws:policy/AdministratorAccess"}
"UserId": "AIDA12345678ABCDEFGHI",
"Arn": “arn:aws:iam: :200802171337:user/krileva",
"CreateDate": "2024-03-22T03:48:59+00:00" eventCount: = userAgent =
}
} 1 aws-cli/2.13.0 Python/3.11.4 Darwin/22.6.0 source/arm64 prompt/off command iam.create-user
1 aws-cli/2.13.0 Python/3.11.4 Darwin/22.6.0 source/arm64 prompt/off command iam.create-access-key
bash-3.2$
bash-3.2$ aws iam create-access-key --user-name krileva
{ 1 aws-cli/2.13.0 Python/3.11.4 Darwin/22.6.0 source/arm64 prompt/off command iam.attach-user-policy
"AccessKey": {
"UserName": "krileva",
"AccessKeyId": "AKIA[REDACTED:aws-access-key-id]",
"Status": "Active",
"SecretAccessKey": "SHQIP1337PunaEshteShendet4U+po+iRedacted",
"CreateDate": "2024-03-22T03:49:17+00:00"
}
}
bash-3.2$
bash-3.2$ aws iam attach-user-policy --user-name krileva \
> --policy-arn arn:aws:iam::aws:policy/AdministratorAccess
bash-3.2$
```

## Slide 76

## **CLI vs Console**

1

**1 2 3**

**1 2 3**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
vs Console
bash-3.2$
bash-3.2$ pytho
iam_client.create_user(UserName=krileva)
{'Arn': ‘arn:aws:iam: :200802171337:user/krileva',
'CreateDate': datetime.datetime(2024, 3, 22, 4, 52, 49, tzinfo=tzutc()),
‘Path': '/',
'UserId': 'AIDA12345678ABCDEFGHI'
'UserName': 'krileva'}
iam_client.create_access_key(UserName=krileva)
{'AccessKeyId': 'AKIA[REDACTED:aws-access-key-id]',
'CreateDate': datetime.datetime(2024, 3, 22, 4, 52, 49, tzinfo=tzutc()),
'SecretAccessKey': 'SHQIP1337PunaEshteShendet4U+po+iRedacted'
'Status': 'Active',
'UserName': 'krileva'}
iam_client.attach_user_policy(UserName=krileva, PolicyArn=arn:aws: iam: :aws
:policy/AdministratorAccess)
bash-3.2$
import boto3
from pprint import pprint
efine IAM client
iam_client = boto3.client('iam')
# Spe sername for new IAM User
username = ‘krileva‘
# fy policy ARN to add to newly cre IAM User
policyArn = "“arn:aws: iam: :aws:policy/AdministratorAccess"
# Create IAM User
response iam_client.create_user(UserName=username)
print(f"\niam_client.create_user(UserName={username})\n")
pprint (response['User'])
# Create Acce for newly created IAM User
response = iam_client.create_access_key(UserName=username)
print(f"\niam_client.create_access_key(UserName={username})\n")
pprint (response['AccessKey'])
# At i to y created IAM r 3
response = iam_client.attach_user_policy(UserName=username, PolicyArn=policyArn)
print(f"\niam_client.attach_user_policy(UserName={username}, PolicyArn={policyArn})\n")
```

## Slide 77

## **CLI vs Console**

**1 2 3**

**1 2 3**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
vs Console
eventCount = userAgent
3 Boto3/1.28.27 md/Botocore#1.31.27 ua/2.0 os/macos#22.6.0 md/arch#arm64 lang/python#3.11.4 md/pyimpl#CPython cfg/retry-mode#legacy Botocore/1.31.27
Hl
eventNameFull requestParameters
bash-3.2$
bash-3.2$ python3
iam:CreateUser {"userName":"krileva"}
iam_client.create_user(UserName=krileva) iam:CreateAccessKey {"userName":"krileva"}
{'Arn': ‘arn:aws:iam: :200802171337:user/krileva', iam:AttachUserPolicy {"userName":"krileva","policyArn":"arn:aws:iam::aws:policy/AdministratorAccess"}
'CreateDate': datetime.datetime(2024, 3, 22, 4, 52, 49, tzinfo=tzutc()),
'Path': '/',
'UserId': 'AIDA12345678ABCDEFGHI', Sue eee
'UserName': 'krileva'} from pprint import pprint
iam_client.create_access_key(UserName=krileva) 2 # Define IAM client
boto3.client(‘'iam')
{'AccessKeyId': 'AKIA[REDACTED:aws-access-key-id]',
'CreateDate': datetime.datetime(2024, 3, 22, 4, 52, 49, tzinfo=tzutc()),
'SecretAccessKey': 'SHQIP1337PunaEshteShendet4U+pot+iRedacted',
'Status': 'Active',
'UserName': 'krileva'}
username
y
iam_client.attach_user_policy(UserName=krileva, PolicyArn=arn:aws: iam: :aws 11 policyArn = "“arn:aws:i
:policy/AdministratorAccess)
# Create IAM User
bash-3.2$ response = iam_client.create_user(UserName=username)
print(f"\niam_client.create_user(UserName={username})\n")
pprint (response['User'])
# Create Access Key for newly created IAM User
response = iam_client.create_access_key(UserName=username)
print(f"\niam_client.creat ccess_key(UserName={username})\n")
pprint (response['
```

## Slide 78

## **CLI vs Console**

Users | IAM | Global
No_Permissions @ 2008-0217-1337

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
BB Users | 1AM | Global
© https://us-east-1.console.aws.amazon.com/iam/home?region=us-east-2#/.. Q A’ yy
Identity and Access =X 1AM > Users
Management (IAM)
| Q Search am Users (3) info
An IAM user is an identity with long-term credentials that Is used to interact with AWS in an account.
ja Search
Dashboard
‘Y Access management User name Groups ¥ Last activity
User groups
Andi.
thers Andi_Ahmeti
et elt
Policies Daniel_Bohannon
Identity providers
No_Permissions
Account settings —_—_——S
¥ Access reports
Access Analyzer
External access
Unused access
Analyzer settings
Credential report
Organization activity
```

## Slide 79

## **CLI vs Console**

ConsoleHome
13
SearchBar
1
IAM Dashboard

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
eventNameFull userAgent requestParameters
2024-03-22 04:54:52.0000 servicecatalog-appregistry:ListApplications Mozilla/5.0 (Macintosh; Intel ... {"maxResults":"100"}
2024-03-22 04:54:52.0000 _notifications:ListNotificationHubs Mozilla/5.0 (Macintosh; Intel ...
2024-03-22 04:54:52.0000 _health:DescribeEventAggregates health.amazonaws.com {"filter":{"eventTypeCategories":["scheduledChange...
2024-03-22 04:54:52.0000 health:DescribeEventAggregates illa/5. i ; a {"filter":{"startTimes":[{"from":"Mar 15, 2
2024-03-22 04: 4:52.0000 health:DescribeEventAggragates Mozilla/5.0 (Macintosh; Intel one ("filter:("startTimes “from":"Mar 15, 2024 4:54:65...
2024-03-22 04:54:52.0000 health:DescribeEventAggregates Mozilla/5.0 (Macintosh; Intel ... {"filter":{"startTimes":[{"from":"Mar 15, 2024 4:54:5...
2024-03-22 04:54:52.0000 health:DescribeEventAggregates health.amazonaws.com {"filter":{"startTimes":[{"from":"Mar 15, 2024, 4:54:5...
2024-03-22 04:54:52.0000 health:DescribeEventAggregates health.amazonaws.com {"filter":{"startTimes":[{"from":"Mar 15, 2024, 4:54:5...
2024-03-22 04:54:53.0000 health:DescribeEventAggregates AWS Internal {"filter":{"eventStatusCodes":["open","upcoming"
2024-03-22 04:54:53.0000 health:DescribeEventAggregates AWS Internal {"filter":{"startTimes":[{"from":"Mar 15, 2024 4:54:5...
2024-03-22 04:54:53.0000 ec2:DescribeRegions Mozilla/5.0 (Macintosh; Intel ... {"regionSet":{},"allRegions":true}
2024-03-22 04:54:53.0000 _—ce:GetCostForecast Mozilla/5.0 (Macintosh; Intel... _{"Filter":{"Not":{"Or":[{"Dimensions":{"Key":"RECOR...
2024-03-22 04:54:53.0000 _—_ce:GetCostAndUsage Mozilla/5.0 (Macintosh; Intel ... {"Filter":{"Not":{"Or":[{"Dimensions":{"Key":"RECOR...
SearchBar
```

## Slide 80

## **CLI vs Console**

SearchBar
1 13
IAM_Dashboard
8
IAM_Users
18

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Console
SearchBar
eventTime =
eventNameFull
resource-explor
IAM_Dashboard
eventTime =
2024-03-22 04:55:06.0000
2024-03-22 04:55:06.0000
2024-03-22 04:55:06.0000
2024-03-22 04:55:06.0000
2024-03-22 04:55:06.0000
2024-03-22 04:55:06.0000
2024-03-22 04:55:06.0000
2024-03-22 04:55:06.0000
IAM_Users
eventNameFull
organizations:DescribeOrganization
notifications:ListNotificationHubs
iam:ListMFADevices
iam:ListAccountAliases
iam:ListAccessKeys
iam:GetAccountSummary
health:DescribeEventAggregates
health:DescribeEventAggregates
__userAgent
Mozilla/5.0 (Macintosh; Intel ...
userAgent
AWS Internal
Mozilla/5.0 (Macintosh; Intel ...
AWS Internal
AWS Internal
AWS Internal
AWS Internal
AWS Internal
AWS Internal
requestParameters
GGREGATOR"}
requestParameters
{"userName":"No_Permissions"}
{"userName":"No_Permissions"}
{"filter":{"eventStatusCodes":["open","upcoming"],"
{"filter":{"startTimes":[{"from":"Mar 15, 2024 4:5:
```

## Slide 81

**8**

## **CLI vs Console**

IAM_Users
18

13

1

```
IAM_Users_CreateUser_Step1
```

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
» IAM_Users
eventTime =
eventNameFull
userAgent
requestParameters
2024-03-22 04:55:29.0000
2024-03-22 04:55:30.0000
2024-03-22 04:55:30.0000
2024-03-22 04:55:30.0000
2024-03-22 04:55:32.0000
2024-03-22 04:55:32.0000
2024-03-22 04:55:32.0000
2024-03-22 04:55:32.0000
2024-03-22 04:55:32.0000
2024-03-22 04:55:32.0000
2024-03-22 04:55:33.0000
2024-03-22 04:55:33.0000
2024-03-22 04:55:33.0000
2024-03-22 04:55:34.0000
2024-03-22 04:55:34.0000
2024-03-22 04:55:34.0000
iam:ListUsers
iam:GetLoginProfile
iam:GetLoginProfile
iam:GetLoginProfile
iam:ListSigningCertificates
iam:ListSigningCertificates
iam:ListSigningCertificates
iam:ListMFADevices
iam:ListMFADevices
iam:ListMFADevices
iam:ListGroupsForUser
iam:ListGroupsForUser
iam:ListGroupsForUser
iam:ListAccessKeys
iam:ListAccessKeys
iam:ListAccessKeys
AWS Internal
aws-internal/3 aws-sdk-java/...
aws-internal/3 aws-sdk-java/...
aws-internal/3 aws-sdk-java/...
aws-internal/3 aws-sdk-java/...
aws-internal/3 aws-sdk-java/...
aws-internal/3 aws-sdk-java/...
aws-internal/3 aws-sdk-java/...
aws-internal/3 aws-sdk-java/...
aws-internal/3 aws-sdk-java/...
aws-internal/3 aws-sdk-java/...
aws-internal/3 aws-sdk-java/...
aws-internal/3 aws-sdk-java/...
aws-internal/3 aws-sdk-java/...
{"maxltems":1000}
{"userName":"Andi_Ahmeti"}
{"userName":"Daniel_Bohannon"}
{"userName":"No_Permissions"}
{"userName":"Andi_Ahmeti"}
{"userName":"Daniel_Bohannon"}
{"userName":"No_Permissions"}
{"userName":"Andi_Ahmeti"}
{"userName":"Daniel_Bohannon"}
{"userName":"No_Permissions"}
{"userName":"Andi_Ahmeti"}
{"userName":"Daniel_Bohannon"}
{"userName":"No_Permissions"}
{"userName":"Andi_Ahmeti"}
{"userName":"Daniel_Bohannon"}
{"userName":"No_Permissions"}
d":"AKIA[REDACTED:aws-access-key-id]"}
IAPERSHENDETJEMIQ2"}
```

## Slide 82

**8**

## **CLI vs Console**

#### `IAM_Users_CreateUser_Step1`

#### `IAM_Users_CreateUser_Step1B (attach policy)`

**4**

15

**18 13 1**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Console
» IAM_Users_CreateUser_Step1
eventTime — eventNameFull = _suserAgent requestParameters
2024-03-22 04:55:46.0000 sso:DescribeRegisteredRegions AWS Internal ||
2024-03-22 04:55:46.0000 organizations:ListDelegatedAdministrators AWS Internal —
2024-03-22 04:55:46.0000 organizations:DescribeOrganization AWS Internal
2024-03-22 04:55:46.0000 _iam:GetAccountPasswordPolicy AWS Internal |
IAM_Users_CreateUser_Step1B (attach policy)
eventTime =
2024-03-22 04:56:23.0000
2024-03-22 04:56:23.0000
2024-03-22 04:56:23.0000
2024-03-22 04:56:23.0000
2024-03-22 04:56:24.0000
2024-03-22 04:56:24.0000
2024-03-22 04:56:24.0000
2024-03-22 04:56:25,0000
eventNameFull
iam:ListPolicies
iam:ListGroups
iam:GetGroup
iam:GetGroup
iam:ListPolicies
iam:ListAttachedGroupPolicies
iam:ListAttachedGroupPolicies
iam:ListPolicies
userAgent =
AWS Internal
AWS Internal
aws-internal/3 aws-sdk-java/...
aws-internal/3 aws-sdk-java/...
AWS Internal
aws-internal/3 aws-sdk-java/...
requestParameters
{"maxltems":1000,"onlyAttached":false}
{"maxitems":1000}
{"groupName":"customGroup1"}
{"groupName":"customGroup2"}
{"maxltems":1000,"marker":"AFB1SALqql7Kp/vCL!
{"groupName":"customGroup1"}
{"groupName":"customGroup2"}
{"scope":"AWS","onlyAttached":false,"pathPrefix":"/"}
“,"onlyAttached":false,"pathPrefix":"/"}
-200802171337:policy/Per...
```

## Slide 83

```
IAM_Users_CreateUser_Step1
```

## **CLI vs Console**

#### `IAM_Users_CreateUser_Step1B (attach policy)`

IAM_Users_CreateUser_Step2

15

3

18 13
4 1
8

## Slide 84

## **CLI vs Console**

#### `IAM_Users_CreateUser_Step2`

#### `IAM_Users_SPECIFICUSER_Permissions`

3 18 13
4 1

15 8

**10**

```
IAM_Users_SPECIFICUSER_CreateAccessKey
```

## Slide 85

## **CLI vs Console**

IAM_Users_SPECIFICUSER_CreateAccessKey
1 3 18 13
10 4 1
15 8

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Console
* IAM_Users_SPECIFICUSER_CreateAccessKey
eventTime = eventNameFull = _userAgent = requestParameters
2024-03-22 04:58:57.0000 iam:CreateAccessKey AWS Internal {"userName":"krileva"}
```

## Slide 86

## **CLI vs Console**

3 18 13
10 4 1
1 15 8

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Console
nN
= *\
28
AWS Internal
2 aws-internal/3 aws-sdk-java/1.12.676 Linux/5.10.210-178.852.amzn2int.x86_64 OpenJDK_64-Bit_Server_VM/17.0.10+9-LTS java/1.8.0_402 vendor/N/A cfg/retry-mode/standard
25 —_ aws-internal/3 aws-sdk-java/1.12.679 Linux/5.10.210-178.852.amzn2int.x86_64 OpenJDK_64-Bit_Server_VM/17.0.10+9-LTS java/1.8.0_402 vendor/N/A cfg/retry-mode/standard
5 aws-internal/3 aws-sdk-java/1.12.679 Linux/5.10.210-178.855.amzn2int.x86_64 OpenJDK_64-Bit_Server_VM/17.0.10+9-LTS java/1.8.0_402 vendor/N/A cfg/retry-mode/standard
health.amazonaws.com
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0
```

## Slide 87

## **CLI vs Console**

3 18 13
10 4 1
73
1 15 8
events

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Console
A. eventCount userAgent
ss)
28 AWS Internal
2 aws-internal/3 aws-sdk-java/1.12)676]Linux/6.10.210-1 amzn2int.x86_64 OpenJDK_64-Bit_Server_VM/17.0.10+9-LTS java/1.8.0_402 vendor/N/A cfg/retry-mode/standard
aws-internal/3 aws-sdk-java/1.12 679 Linux/5.10.210-17! mzn2int.x86_64 OpenJDK_64-Bit_Server_VM/17.0.10+9-LTS java/1.8.0_402 vendor/N/A cfg/retry-mode/standard
aws-internal/3 aliens ie Reno 8 855 amzn2int.x86_64 OpenJDK_64-Bit_Server_VM/17.0.10+9-LTS java/1.8.0_402 vendor/N/A cfg/retry-mode/standard
health.amazonaws.com
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0
```

## Slide 88

## **CLI vs Console**

3 3 73
events events events

## Slide 89

## **Worst Case Scenarios**

**n** **~~=~~ 3**

#### `IAM_Users`

iam:ListUsers **1** **~~<u>1</u>~~** iam:GetLoginProfile **+ +** iam:ListSigningCertificates iam:ListMFADevices **~~=~~ 5n** 5(3 ~~)~~ = **<u>15</u> 18** iam:ListGroupsForUser **+ +** iam:ListAccessKeys iam:GetAccessKeyLastUsed **n** ~~3~~ = **<u>2</u>** iam:GetAccessKeyLastUsed **[0,2 ]** [0,2( )]

## Slide 90

## **Worst Case Scenarios**

**1+5n+ n [0,2 ]**

`IAM_Users` **n=** **~~2~~ 0**

1+5 20 + ~~0~~ 2 20 = **141** ( ) [ , ( )] **n=** **~~5~~ 0** 1+5 50 + ~~0~~ 2 50 = **351** ( ) [ , ( )] **n=** **~~1~~ 00** 1+5 100 100 = **701** ( )+[ ~~0~~ ,2( )]

## Slide 91

# **Worst Case Scenarios 1+5n+ n [0,2 ] + 21 4n**

#### **n=** **~~1~~ 00** `S3_Buckets`

21+4 ~~1~~ 00 **421** ( )=

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
} Worst Case Scenarios
Page size
© 100 buckets
S3_Buckets
eventNameFull = eventCount = dcount_buckets = buckets =
s3:ListBuckets 2 0 0
s3:GetStorageLensConfiguration 1 0 o
s3:GetStorageLensConfiguration 1 0 if]
s3:GetStorageLensDashboardDatainternal 2 0 oO
ec2:DescribeRegions 1 o oO
health:DescribeEventAggregates 2 0 if]
notifications:ListNotificationHubs 1 0 0
$3:GetAccountPublicAccessBlock 11 0 i]
s3:ListAccessPoints 100 100 ["bureki","doner","gjevrek","golden_eagle"....
s3:GetBucketPolicyStatus 100 100 ["bureki","doner","gjevrek","golden_eagle",...
s3:GetBucketPublicAccessBlock 100 100 ["bureki","doner","gjevrek","golden_eagle"....
s3:GetBucketAcl 100 100 ["bureki","doner","gjevrek","golden_eagle"....
21
421
\
```

## Slide 92

## **… In Summary**

**#Aggregation**

## Slide 93

## **… In Summary**

#### `IAM_Users_CreateUser`

IAM_Users

**#Aggregation**

```
Background_Events
```

```
IAM_Users_SPECIFICUSER_CreateAccessKey
```

## Slide 94

## **… In Summary**

#### `IAM_Users_CreateUser`

```
IAM_Users
```

• **Introduction**

• **Cloud Logs for Defenders** • **PROBLEM: Noisy Console Logs#Aggregation**

`Background_Events` • **SOLUTION: Mapping for Clarity** `IAM_Users_SPECIFICUSER_CreateAccessKey` • **Tool Demo + Release**

## Slide 95

## **… In Summary**

`IAM_Users_CreateUser IAM_Users` • **Introduction** • **Cloud Logs for Defenders** • **PROBLEM: Noisy Console Logs#Aggregation** `Background_Events` • **SOLUTION: Mapping for Clarity** `IAM_Users_SPECIFICUSER_CreateAccessKey` • **Tool Demo + Release**

## Slide 96

## **… In Summary**

IAM_Users_CreateUser
IAM_Users
• Introduction
• Cloud Logs for Defenders
• PROBLEM: Noisy Console Logs#Aggregation
Background_Events
• SOLUTION: Mapping for Clarity
IAM_Users_SPECIFICUSER_CreateAccessKey
• Tool Demo + Release

## Slide 97

## **… In Summary**

IAM_Users_CreateUser
IAM_Users
• Introduction
• Cloud Logs for Defenders
• PROBLEM: Noisy Console Logs#Aggregation
Background_Events
• SOLUTION: Mapping for Clarity
IAM_Users_SPECIFICUSER_CreateAccessKey
• Tool Demo + Release

## Slide 98

- **Introduction**

- • **Cloud Logs for Defenders** • **PROBLEM: Noisy Console Logs** • **SOLUTION: Mapping for Clarity** • **Tool Demo + Release**

## Slide 99

**-** **~~–~~ 2 Pass Approach Labels + Signals**

iam:ListUsers iam:GetLoginProfile iam:ListSigningCertificates iam:ListMFADevices iam:ListGroupsForUser iam:ListAccessKeys iam:GetAccessKeyLastUsed

```
$this.AnchorEvents
$this.RequiredEvents
$this.OptionalEvents
```

## Slide 100

## **Signal Definition**

```
([LabelType]::IAM_Users) {
```

```
$this.Service='IAM'
```

```
$this.Name='Clicked IAM->Users'
```

```
$this.Summary='Clicked IAM->Users which displays all IAM Users in paged format.'
```

```
$this.Url='https://{{awsRegion}}.console.aws.amazon.com/iamv2/home?region={{awsRegion}}#/users'
$this.AnchorEvents=@('iam:ListUsers')
```

```
$this.RequiredEvents=@(
```

```
'iam:GetLoginProfile',
```

```
'iam:ListAccessKeys',
```

```
'iam:ListGroupsForUser',
```

```
'iam:ListMFADevices',
```

```
'iam:ListSigningCertificates',
```

```
'iam:ListUsers'
```

```
)
```

```
# iam:GetAccessKeyLastUsedonly executed if 1+ IAM Users with 1+ Access Keys are defined.
$this.OptionalEvents=@('iam:GetAccessKeyLastUsed')
# Current mapping scenario generates events over longer-than-normal timespan, so increasing
```

```
# default lookback/lookahead values when aggregating nearby events surrounding AnchorEvents.
$this.LookbackInSeconds=5
```

```
$this.LookaheadInSeconds=35
```

```
}
```

## Slide 101

## **Pass #1 Label Assi** **~~g~~ nment (Per Event)**

```
'ListUsers' {
# E.g. {"maxItems":1000}
if(
$requestParametersStr-ceq'{"maxItems":1000}'-and `
$userAgentFamily-eq [UserAgentFamily]::AWS_Internal
)
{
[LabelType]::IAM_BrowserRefresh
[LabelType]::IAM
[LabelType]::IAM_Users_CreateUser_Step2
[LabelType]::IAM_Users
[LabelType]::IAM_UserGroups
[LabelType]::IAM_Users_CreateUser
}
}
```

## Slide 102

## **– Pass #2 Signal Evalu** **~~a~~ tion (Grouped Events)**

- Iterate over all events w/Labels

- Stop at each Anchor event

- Test each Label for current Anchor event: • Gather nearby unmapped events with same Label

   - If gathered events match current Label’s ~~-~~

   - Signal definition > create Signal object

   - Else try next Label

## Slide 103

## **Add’l Cool Tricks & Capabilities**

- Modification of Signal names, summaries & URLs based on data extracted from all related events

- • Each Signal contains dictionary of extracted data

- Signal lookback scenarios for:

   - Modifying previous Signals

   - Changing Label for current Signal

- Merging previous Signals

- Extracting data from previous Signals to be used in current Signal

## Slide 104

- **Introduction**

- **Cloud Logs for Defenders**

- • **PROBLEM: Noisy Console Logs** • **SOLUTION: Mapping for Clarity** • **Tool Demo + Release**

## Slide 105

**DEMO + Public Tool Release**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
oO
no
fo]
2
)
~
re)
Le)
2
re)
=)
QO.
+
O
=
eel
a)
```

## Slide 106

## **Black Hat Sound Bytes**

**1. Threat actors continue to use interactive console UIs** (instead of CLIs) throughout many stages of the attack lifecycle

**2. Configure the necessary cloud logging options** for retention, forwarding & querying capabilities required to detect & analyze suspicious console session logs

**3. Use Cloud Console Cartographer** , a brand new open-source framework to automatically translate 1000’s of events to 10’s of mapped “clicks” performed by users in interactive console sessions

## Slide 107

Thanks for your time!

## Slide 108

ANDI DANIEL
AHMETI BOHANNON
andi-ahmeti danielhbohannon
@SecEagleAnd1 @danielhbohannon
C
https://github.com/Permiso-io-tools/ CloudConsoleCartographer
C

C
