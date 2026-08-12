---
title: "CTRAPS CTAP Impersonation and API Confusion Attacks on FIDO2"
speakers: ["Marco Casagrande Daniele Antonioli"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33/Marco Casagrande Daniele Antonioli - CTRAPS CTAP Impersonation and API Confusion Attacks on FIDO2.pdf"
pages: 44
sha256: "3deb97ed96924b8f261370aee87c9a6f1c503d769febf7101c8f76a6b952e960"
text_chars: 13270
ocr_pages: 9
has_ocr: true
redacted_secrets: 0
ocr_confidence: 91.3
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T07:06:26Z"
---
# CTRAPS CTAP Impersonation and API Confusion Attacks on FIDO2

**Speakers:** Marco Casagrande Daniele Antonioli  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33/Marco Casagrande Daniele Antonioli - CTRAPS CTAP Impersonation and API Confusion Attacks on FIDO2.pdf` (44 pages)


## Slide 1

**CTRAPS: CTAP Client Impersonation and API Confusion on FIDO2** _DEF CON 33_ M. Casagrande             D. Antonioli

## Slide 2

## Marco Casagrande

- Postdoc at <u>KTH (Sweden), Prof.</u> Papadimitratos ○ <u>Networked Systems Security (NSS) group</u>

- PhD at EURECOM (France), Dec 2024, Prof. Antonioli

- ●Research in Security and Privacy:

   - Proprietary protocols (fitness trackers, e-scooters, …)

   - ○ Standard protocols (BLE, Wi-Fi, NFC, FIDO2, …)

   - Mobile (Android, …)

2

## Slide 3

## Daniele Antonioli

- Asst. Prof at <u>EURECOM</u> (France) ○ <u>Software and System Security (S3) group</u>

- ●Research **security and privacy** ○ Bluetooth (BLUFFS, BLURtooth, BIAS, KNOB, …)

- ○ E-Scooters (E-Spoofer, E-Trojans, …)

- FIDO2 (CTRAPS, …)

- Web tracking (FP-tracer, …)

- …

●More at <u>https://francozappa.github.io</u>

3

## Slide 4

## CTRAPS Talk Outline

1. Introduction

2. Background and Threat Model

3. Client Impersonation (CI) Attacks and Demo 4. API Confusion (AC) Attacks and Demo 5. Vulnerabilities and Toolkit

6. Evaluation

7. Countermeasures and Disclosure

4

## Slide 5

Introduction

## Slide 6

## CTRAPS Research Paper (IEEE EuroS&P25)

<u>https://francozappa.github.io/publication/2025/ctraps/</u>

6


> Recovered by OCR — confidence 94/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CTRAPS Research Paper (IEEE EuroS&P25)
CTRAPS: CTAP Client Impersonation and API Confusion on FIDO2
Marco Casagrande
Department of Digital Security
EURECOM
Sophia Antipolis, France
marco.casagrande @ eurecom.fr
Abstract—FIDO2 is a popular technology for single-factor
and second-factor authentication. It is specified in an open
standard including the WebAuthn and CTAP application
layer protocols. We focus on CTAP which allows the com-
munication between FIDO2 clients and authenticators. No
prior work explored the CTAP Authenticator API which is
a critical protocol-level attack surface as it deals with cre-
dential creation, deletion, and management. We address this
gap by presenting the first security and privacy evaluation
of the CTAP Authenticator API. We uncover two classes of
CTAP protocol-level attacks we call CTRAPS.
Daniele Antonioli
Department of Digital Security
EURECOM
Sophia Antipolis, France
daniele.antonioli@ eurecom.fr
FIDO market to rapidly grow from USD 230.6 million in
2022 to USD 598.6 million in 2031 [6 ]. Yubico, a FIDO
authenticator market leader, sold more than 22 million
YubiKey authenticators [- 7]. This growth will continue
because of the recent industry-wide push towards single-
FIDO2 involves three entities: an authenticator that
generates and asserts possession of authentication creden-
tials (e.g., public-private key pairs), a relying party that
authenticates the user (e.g., challenge-response protocol
based on credentials), and a client who wants to authenti-
httos://francozappa.github.io/publication/2025/ctraps/
ORSHIN
```

## Slide 7

## FIDO2 Introduction

- **●Fast IDentity Online 2 (FIDO2)** ○ Open authentication standard

- ○ Resilient to _phishing (password compromise)_

- ○ _Authenticator_ : USB dongle, smartphone, …

   - _Credentials_ : key pairs used to authenticate

- **Second-factor** auth (2FA)

- Login with username, password, and Authenticator

- ● **Passwordless** auth (passkey)

   - Login with Authenticator

7

## Slide 8

## FIDO2 **Entities** and **CTAP** and **WebAuthn** Protocols

**Client**

**CTAP** (USB, NFC, or BLE) **Authenticator User (Auth)**

**WebAuthn** (TLS)

**Relying Party (RP)**

8

## Slide 9

## CTRAPS Motivation

Client
Relying Party (RP)
CTAP  (USB, WebAuthn
NFC, or BLE)
(TLS)
Auth User

- ●Focus on the security and privacy of the **CTAP** protocol ○ Attacks: CTAP Client impersonation and CTAP MitM

- ○ Impact: delete creds, track, DoS, privacy leak, …

- ○ Regardless of CTAP transport (USB, NFC, BLE)

- ○ Affect also RP (cannot login, …)

9

## Slide 10

## CTRAPS Contributions

● **8 CTAP design vulns** (V1, …,V8) ○ Affecting millions of FIDO2 devices (billions of credentials)

- **11 CTRAPS attacks**

   - 4 Client Impersonation (CI1, …, CI4)

   - 7 API Confusion MitM (AC1, …, AC7)

- Open source <u>CTRAPS toolkit</u>

   - Virtual CTAP testbed, 4 attack Clients, …

- Evaluation **exploiting 16 FIDO2 entities**

   - 6 Auth (Yubico, Feitian, …), 10 RP (Apple, Microsoft, Nvidia, …)

● Discuss **8 design fixes** compliant with FIDO2

10

## Slide 11

Background and Threat Model

## Slide 12

## FIDO2 Credentials and Authentication

- FIDO2 credentials ○ ECDSA key pairs, _sign (prikey), verify (pubkey)_

- ○ _Non-discoverable_ : enc prikey stored on RP (2FA)

- ○ _Discoverable_ : enc prikey stored on Auth (passkey)

- ○ Cred prikey encrypted with Auth master key

- ●FIDO2 auth flow

   - Make a FIDO2 cred and store cred keys

   - ○ Use Auth cred to authenticate User to RP ○ Challenge from RP, signed response from Auth

12

## Slide 13

## CTAP Introduction

- **●CTAP (Client to Authenticator Protocol)** ○ Standard AL protocol over USB, NFC, or BLE

- Client request and Auth respond

- ● _CTAP1_ (known as U2F)

   - Standardized 2FA with non-disc creds

- Authenticator API (create cred, auth cred, …)

- ● _CTAP2_ (latest v2.2)

   - Standardized passwordless with disc creds

   - Extended Authenticator API (cred tracking protection, …)

13

## Slide 14

## Focus 7 Core CTAP Authenticator APIs

EnumRpis, EmumCreds, ...

**User Verification (UV)** : eg: PIN on Client verified by Auth **User Presence (UP)** : eg: Auth and Client are in NFC range

14

## Slide 15

## CTRAPS Threat Model

Victim User
UP UV
CTAP WebAuthn Relying
Authenticator Client
Party
Attacker focuses on  CTAP
design issue,  is in  proximity
MitM
or  remote,  and  does not
CI Client
compromise Auth or Client.
15

## Slide 16

Client Impersonation (CI) Attacks and Demos

## Slide 17

## CTAP Authenticator API Call (UV, UP)

Auth and Client run
PIN/UV Auth protocol  if
API_A requires UV
UV  reusable  within a
session

UP test  if API_A
requires UP

17

## Slide 18

## CI1: Factory Reset Auth

Reset requires UP

18


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Cl,: Factory Reset Auth
Authenticator
Reset
Attacker as Client
User Presence (UP)
Deletes Master Key,
invalidating all creds
Resets data
and settings
Reset OK
Reset requires UP
18
```

## Slide 19

## DEMO CI1: Factory Reset Auth over NFC

19

## Slide 20

## CI2: Track User from Auth Credentials

GA=GetAssertion, no UV if CredProtect=off. Eg: Apple, Microsoft

20


> Recovered by OCR — confidence 92/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Cl,: Track User from Auth Credentials
GA=GetAssertion, no UV if CredProtect=off. Eg: Apple, Microsoft
Authenticator Attacker as Client
Prepares InsecureRpIdList
with CredProtect=off
GA, up=false, InsecureRpIdList
GA OK, CredIdList, UserIdList
FingerprintList =
20
```

## Slide 21

## DEMO CI2: User Tracking via Creds over NFC

21

## Slide 22

## Four Client Impersonation (CI) Attacks Summary

● **CI1** : Factory Reset Authenticator (Reset) ● **CI2** : Track User from Credentials (GetAssertion) ● **CI3** : Force Authenticator Lockout (ClientPin) ● **CI4** : Profile Authenticator (GetInfo)

22

## Slide 23

API Confusion (AC) Attacks and Demos

## Slide 24

## API Confusion (AC) Attack Technique

Runs if API_A
requires UV
Attacker confounds
API_A with API_B.
Runs if API_B
requires UP

24


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
API Confusion (AC) Attack Technique
Authenticator MitM Attacker
Client
| PIN/UV Auth: Forces UV™ valid for all APIs and RpIds
Runs if API_A
requires UV
APT_B [, UV*] APT_A [, UV*]
A
User Presence (UP) Runs if API_B
requires UP
Executes API_B
API_B OK
APT_A OK
>
>
Attacker confounds
API_A with API_B.
24
```

## Slide 25

## AC CTAP API Combinations

✓<sup>**1**</sup> : NFC ✓<sup>**2**</sup> :CredProtect=off (default)

25

## Slide 26

## AC2: Factory Reset Auth

API_A requires UP like Reset, eg: Get Assertion, Selection,...

26


> Recovered by OCR — confidence 92/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
AC,,: Factory Reset Auth
Authenticator
Reset
MitM Attacker
Client
User Presence (UP)
I
Deletes Master Key,
invalidating all creds
Resets data
and settings
Reset OK
APT_A OK
API_A requires UP like
Reset, eg: Get Assertion,
Selection,...
v
26
```

## Slide 27

## AC1: Delete Discov Creds

API_A requires UV, eg: MakeCredential, ClientPin,... Attacker calls CM=CredMgmt N times with different subcommands reusing UV

27

## Slide 28

## DEMO AC1: Delete Discov Creds over USB

28

## Slide 29

## Seven API Confusion (AC) Attacks

● **AC1** : Delete Discoverable Creds (CredMgmt) ● **AC2** : Factory Reset Authenticator (Reset) ● **AC3** : Track User from Credentials (GetAssertion) ● **AC4** : Fill Authenticator Credentials Storage (MakeCred) ● **AC5** : Force Authenticator Lockout (ClientPin) ● **AC6** : Authenticator DoS (Selection) ● **AC7** : Profile Authenticator (GetInfo)

29

## Slide 30

Vulnerabilities and Toolkit

## Slide 31

## CTRAPS Eight CTAP Design Vulns

● **V1** : Unauthenticated CTAP Client ● **V2** : No Authenticator feedback about API call ● **V3** : NFC range provides UP ● **V4** : Weak destructive APIs authorization ● **V5** : User trackable via CredId and UserId ● **V6** : Reset does not require UV ● **V7** : CredMgmt does not require UP ● **V8** : Selection is usable for DoS

31

## Slide 32

## Map CI and AC Attacks to Vulns

|Re
GA
CP
CI
CM
Re
GA
MC
CP
SE
GI|
|---|

32

## Slide 33

## CTRAPS <u>Toolkit</u>

1. Virtual CTAP testbed

2. Four attack Clients

3. CTAP Wireshark dissector

33


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CTRAPS Toolkit
1. Virtual CTAP testbed
2. Four attack Clients
3. CTAP Wireshark dissector
YubiKey 5 NFC (5.2.7)
Track Authenticator
LOGS:
Connected via NFC.
Found RP: login.microsoft.com
Credential 1/2
Credential 2/2
33
```

## Slide 34

## CTRAPS Toolkit: Virtual CTAP Testbed

- ●Virtual RP and CTAP Client ○ Tests physical Auths without breaking real systems

- ● Extending Yubico fido2-python ○ Row CTAP packets

   - Customizable Client config (UV, UP, ECDH, extensions, …)

   - ○ Templates for existing Relying Party (RpId, CredProtect, …)

34

## Slide 35

## CTRAPS Toolkit: Four Attack Clients

- ●Android app for _CI over NFC_ ○ Runs on attacker’s phone, 2cm max range (Redmi 5 Plus)

- ●Proxmark3 Lua script for _CI over NFC_ ○ Custom CTAP API over ISO14443A, 6.5cm max range

- ●Android app for _CI over NFC_

   - Runs on victim’s phone

   - Custom CTAP API over Android NFC API

- ●Electron app to simulate _AC over USB_ ○ MitM on USB HID traffic using <u>node-hid</u> lib

35

## Slide 36

# Evaluation

36

## Slide 37

## Setup: Test 6 Popular Authenticators

37


> Recovered by OCR — confidence 86/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Setup: Test 6 Popular Authenticators
Authenticator Manuf Year FVer OSF DCr
YubiKey 5 Yubico 2018 Sie) No 25
YubiKey 5 FIPS _Yubico 2021 5.4.3 No 25
Feitian K9 Feitian 2016 = 3.3.01 No 50
Solo V1 SoloKeys 2018 4.1.5 Yes 50
Solo V2 Hacker SoloKeys 2021 2.964 yes 50
OpenSK Google 2023 2.1 Yes 150
37
```

## Slide 38

## Setup: Test 10 Popular Relying Parties

Cred type, DiscWeak = discoverable and unprotected

38


> Recovered by OCR — confidence 89/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Setup: Test 10 Popular Relying Parties
Rp RplId Cred
Adobe adobe.com Disc
Apple apple.com DiscWeak
Facebook facebook.com NonDisc
GitHub github.com Disc
Hancock hancock. ink Disc
Microsoft login.microsoft.com Disc Weak
NVidia login.nvgs.nvidia.com [Disc
Synology account.synology.com Disc
Vault Vision auth.vaultvision.com Disc
Cred type, DiscWeak = discoverable and unprotected
38
```

## Slide 39

## Result: Exploit 6 Authenticators

Auths vulnerable to all CI attacks Auths vulnerable to all AC attacks n/a: not applicable as Auth does not implement Selection

39

## Slide 40

## Result: Exploit 10 Relying Parties

Cannot login and lost creds, Account trackable, Cannot login n/a: not applicable because RP does not support Disc Creds

40

## Slide 41

# Countermeasures and Disclosure

41

## Slide 42

## CTRAPS Countermeasures ( **CN** fixes **VN** )

● **C1** : Trusted CTAP Client ● **C2** : Authenticator visual feedback ● **C3** : User interaction for UP over NFC ● **C4** : Dedicated PIN for destructive APIs (CM, Re, …) ● **C5** : Dynamic and UV-protected CredId and UserId ● **C6** : Reset must require UV (on Client) ● **C7** : CredMgmt must require UP ● **C8** : Rate limiting Selection calls

42

## Slide 43

## CTRAPS Disclosure

- ●FIDO Alliance ○ Nov 2023: first contact

- May 2024: feedback, request to disclose to vendors

- ●Authenticator Vendors

   - Dec 2023: Yubico, Solo, Feitian, Google (P2/S2)

   - ○ Yubico <u>CVE-2024-35311</u> [YSA-2024-02]

- ●Relying Parties ○ Dec 2023: Microsoft, Apple

43

## Slide 44

## Grazie! Q&A

### <u>https://francozappa.github.io/publication/2025/ctraps/</u>

44


> Recovered by OCR — confidence 90/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CTRAPS: CTAP Client Impersonation and API Confusion on FIDO2
Marco Casagrande
Department of Digital Security
EURECOM
Sophia Antipolis, France
marco.casagrande@ eurecom.fr
Abstract—FIDO2 is a popular technology for single-factor
and second-factor authentication. It is specified in an open
standard including the WebAuthn and CTAP application
layer protocols. We focus on CTAP which allows the com-
munication between FIDO2 clients and authenticators. No
prior work explored the CTAP Authenticator API which i
a critical protocol-level attack surface as it deals with cre
dential creation, deletion, and management. We address thi
gap by presenting the first security and privacy evaluation
of the CTAP Authenticator API. We uncover two classes of
CTAP protocol-level attacks we call CTRAP‘
& KTH
ETENSKAP
v
$8 OCH KONST Be
Daniele Antonioli
Department of Digital Security
EURECOM
Sophia Antipolis, France
daniele.antonioli@ eurecom.fr
FIDO market to rapidly grow from USD 230.6 million in
2022 to USD 598.6 million in 2031 [0]. Yubico, a FIDO
authenticator market leader, sold more than 22 million
YubiKey authenticators [-7]. This growth will continue
because of the recent industry-wide push towards sing!
FIDO2 involves three entities: an authenticator that
generates and asserts possession of authentication creden-
tials (e.g., public-private key pairs), a relying party that
authenticates the user (e.g., challenge-response protocol
based on credentials), and a client who wants to authenti-
@ cTraPs
B fido-e
LICENSE
README.md
README 418. MIT license
ORSHIN
EURECOM
Add file
<> Code ~
12. Commits
44
```
