---
title: "Beyond the Ceremony The 2026 Passkey Attack Surface"
speakers: ["Matteo Giordano"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: null
source_pdf: "DEF CON 34/DEF CON 34 - Matteo Giordano - Beyond the Ceremony The 2026 Passkey Attack Surface - v2.pdf"
pages: 100
sha256: "6e80a68dc4aa61a0e0fa1e3592941484c14766bab04abff73b2e68d265423f66"
text_chars: 55493
ocr_pages: 46
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:26:59Z"
---
# Beyond the Ceremony The 2026 Passkey Attack Surface

**Speakers:** Matteo Giordano  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Matteo Giordano - Beyond the Ceremony The 2026 Passkey Attack Surface - v2.pdf` (100 pages)


## Slide 1

## Beyond the Ceremony **The 2026 Passkey Attack Surface**

Matteo Giordano

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
VIL
SECURE
Beyond the Ceremony
The 2026 Passkey Attack Surface
Matteo Giordano
```

## Slide 2

**2**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
AV
Authenticator
fe...»
[se
```

## Slide 3

**3**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
AV
Public
On
Authenticator
(Frrvate] )
esl
```

## Slide 4

**4**

## Slide 5

**5**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
AV
RP
Public
Lot
Client
—
Authenticator
( . \
NY preset]
ee,
a,
```

## Slide 6

**6**

## Slide 7

**7**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
-.. 14)
Private
On J
rivate
On |
Authenticator n
[s)
Client 1
Client 2
Client n
AV
```

## Slide 8

**8**

## Slide 9

**9**

## Slide 10

**10**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
fo)
=
Authenticator n
rivate
an
L, /T! od]
rae]
aun
L Ondo
z
```

## Slide 11

**11**

### **I'm not here with the scariest bug**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
I’m not here with the scariest bug
papers
CVEs
blog posts
talks
PoCs
threads
\
J
VA
WA
AV
V
ONE MAP
Let's give them a home
ay
```

## Slide 12

**12**

### **whoami**

matteo@defcon ~ % whoami --verbose
PublicKeyCredential {
id:          "matteo-giordano",
rpId:        "anvilsecure.com",
userHandle:  "AppSec, offensive research, AI security, Italy",
authData: {
flags: {
UserPresence: true, �� I'm here
UserVerification: true, �� trust me, right?
},
signCount: 0 �� first DEF CON talk.
},
attestation: { fmt: "none" }
}

Don't trust an identity just because the ceremony looked clean. So don't trust mine.

## Slide 13

**13**

### **Passkeys already won-ish**

- **2025**

   - over 1B people have activated a passkey

   - ~15B accounts support them

   - <u>↗ FIDO World Passkey Day 2025</u>

- **2026**

   - ~5B in active use

   - 68% of orgs deploying passkeys for workforce auth

   - <u>↗ FIDO State of Passkeys 2026</u>

## Slide 14

**14**

### **But they almost never run alone**

- Only ~30% of orgs use passkeys as the **PRIMARY** method

- ~57% still lean on a **phishable** one

## Slide 15

**15**

**"Passkeys Are Not Broken, The Conversation About Them Often Is."**

<u>↗ Nishant Kaushik, FIDO CTO, Sept 2025</u>

## Slide 16

**16**

### **It's everything else**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
It’s everything else
AV
enrollment
PEBKAC
CEREMONIES
client
REGISTRATION / AUTHENTICATION
sign > verify > sealed, proven,
phishing-resistant
relying party
recovery
hybrid
transport
Cloud
sync
16
```

## Slide 17

**17**

### **What else?**

- **Six** components, from metal to cloud

- Every passkey attack lives somewhere on this map

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
What else?
AV
1. AUTHENTICATOR /
PROTOCOL
2. Hybrid TRANSPORT
3. CLIENT
6. USER RECOVERY
5. CLOUD SYNC
4. RELYING PARTY
« Six components, from meta/to cloud
¢ Every passkey attack lives somewhere on this map
17
```

## Slide 18

**Ceremonies** Quick refresh

## Slide 19

**19**

### **Registration**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Registration
Relying Party
SERVER
(1) Auth request
(2) challenge, user info, RP info
(9) attestationObject,
clientDataJSON
Client
19
Authenticator
Au
v |
(9) attestationObject,
clientDataJSON
‘2
(10) verify as per [1]
and add credentials to
its storage
AV
(wus
zxr4j4chroMme
CHfamunronw
(5) hash(clientDataJSON),
user info,
RP info, RP ID
(8) attestationObject
(4) clientDataJSON = {
challenge,
RP origin,
"webauthn.create"
»
»
(6) is User near?
(6.1) can User unlock?
(6.2) Creates the key pair
scoped to the RP ID
(7) attestationObject = {
hash(RP ID),
flags = [
UserPresence,
UserVerification,
Attested cred data,
Extension data
1,
credential ID,
public Key in CBOR,
AAGUID,
initial sig counter,
extensions
```

## Slide 20

**20**

### **Authentication**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Authentication
Relying Party
SERVER
(1) Auth request
(2) challenge
(9) authenticatorData +
signature +
clientDataJSON
Client
va) a
Wu
(9) authenticatorData +
signature +
clientDataJSON
C
(10) verify as per [1]
and add credentials to
its storage
AV
CaaS
Zzr4crwome
AMnALToawW
20
Authenticator
(5) hash(clientDataJSON) ,
RP ID
(8) authenticatorData
+ signature
(4) clientDataJSON = {
challenge,
RP origin,
"webauthn.get"
»
»)
(6) is User near?
(6.1) can User unlock?
(7) authenticatorData = {
hash(RP ID),
flags = [
UserPresence,
UserVerification,
Attested cred data,
Extension data
1,
initial sig counter,
extensions
3
(7.1) Signs the
authenticatorData
concatenated with the hash
of the clientDataJSON
```

## Slide 21

**21**

### **Outer layers**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Outer layers
AV
BEFORE the ceremony
Registration
bootstrap —__>
"how'd you prove
you, to enroll?"
Passkey Ceremonies
AFTER the ceremony
Session binding
the cookie it mints
"bound to what?"
Password-manager
handoff
21
```

## Slide 22

**22**

### **Our map**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Our map
AV
1. AUTHENTICATOR /
PROTOCOL
2. Hybrid TRANSPORT
3. CLIENT
6. USER RECOVERY
5. CLOUD SYNC
4. RELYING PARTY
22
```

## Slide 23

**23**

### **Two planes**

- Pick one actor, go deep.

   - A pentester or red-teamer.

- Mint CVEs / 0days and POCs

- Find out what was actually shipped following a methodology.

## Slide 24

**The attack surface** metal to cloud

## Slide 25

# **1. Authenticator and Protocol**

Researcher's turf

## Slide 26

**26**

### **You are here**

**1/5 PROTOCOL** /  auth ·  transport ·  client ·  relying party ·  sync ·  user

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
You are here
AV
1. AUTHENTICATOR /
PROTOCOL
——|_ 2. Hybrid TRANSPORT
_—_—_> 3. CLIENT
6. USER RECOVERY
5. CLOUD SYNC
<< 4. RELYING PARTY
Engagement
4/5
PROTOCOL / auth - transport - client - relying party - sync - user
26
```

## Slide 27

**27**

### **WebAuthn + CTAP**

###### **WHO**

- protocol designers and academics

- FIDO Alliance, W3C

###### **WHAT**

- prove the ceremony resists replay, MitM, forgery

- keep its privacy properties, endpoints assumed honest

###### **HOW**

- symbolic model checkers (ProVerif, Tamarin)

- hand-built computational proofs

- grab the specs, and go down the rabbit-holes

**2/5**

**PROTOCOL** /  auth ·  transport ·  client ·  relying party ·  sync ·  user

## Slide 28

**28**

### **The protocol holds**

- Computational proofs against forgery and replay

   - <u>↗ Barbosa et al. (CRYPTO 2021)</u>

   - <u>↗ Bindel, Cremers, Zhao (IEEE S&P 2023)</u>

   - Revisited recently as <u>↗ Barbosa et al. (PoPETs 2025)</u>

- Studies on vertical aspects

   - Attestation soundness by <u>↗ Bindel, Gama, Guasch, Ronen, ASIACRYPT 2023</u>

**3/5**

**PROTOCOL** /  auth ·  transport ·  client ·  relying party ·  sync ·  user

## Slide 29

**29**

### **CTAP**

**4/5 PROTOCOL** /  auth ·  transport ·  client ·  relying party ·  sync ·  user

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
AV
CTAP
Client
a
e B
B R
O
A
U W
Aslae
TT
R
NY
USB /NFC/ BLE
seeeectteee [ra ivate
Authenticator
(Treste] rivate
a rivate
as ivate
anita
4/5
PROTOCOL / auth - transport - client - relying party - sync - user
29
```

## Slide 30

**30**

### **CTRAPS**

CI1 - factory reset

AC1 - credential deletion

CI2 - user tracking

- <u>CTRAPS paper (Casagrande and Antonioli, EuroS&P 2025)</u> - <u>↗ DEF CON 33 talk</u>

- Toolkit: ↗ <u>github.com/Skiti/CTrAPs</u>

**5/5**

**PROTOCOL** /  auth ·  transport ·  client ·  relying party ·  sync ·  user

## Slide 31

**31**

### **Not all authenticators are equal**

**PLATFORM** (TPM, Secure Enclave) **ROAMING** (key, phone) **FIRST-PARTY** iOS keychain, Windows Hello Apple / Google phone **THIRD-PARTY** Microsoft Authenticator YubiKey, Bitwarden

**hardware** = secure-element backed

**software** = could fake user-pres / user-verif

**1/3**

protocol / **AUTH** ·  transport ·  client ·  relying party ·  sync ·  user

## Slide 32

**32**

### **Hardware authenticators under attack**

##### **WHAT**

##### **HOW**

- extract the private key ◆ <u>↗ Ninjalab: Titan</u>

   - side-channel (EM/power to ECDSA nonce)

      - <u>↗ EUCLEAK (ePrint)</u>

- clone the authenticator ◆ <u>↗ Ninjalab: EUCLEAK</u>

- fault injection

   - <u>↗ NDSS 2024</u>

- invasive probing (decap, microprobing)

   - <u>↗ Ledger Donjon</u>

- firmware and supply-chain analysis

   - <u>↗ NDSS 2024</u>

**2/3**

protocol / **AUTH** ·  transport ·  client ·  relying party ·  sync ·  user

## Slide 33

**33**

### **Software authenticators' anarchy**

"The following passkey providers have not implemented User Verification in a spec-compliant manner."↗ <u>passkeys.dev, known issues</u>

**3/3**

protocol / **AUTH** ·  transport ·  client ·  relying party ·  sync ·  user

## Slide 34

**2. Hybrid transport** Cross-Device Authentication (CDA) BLE + WebSocket, or BLE-only

## Slide 35

**35**

### **You are here**

**1/5** protocol /  auth · **TRANSPORT** ·  client ·  relying party ·  sync ·  user

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
You are here
AV
1. AUTHENTICATOR /
PROTOCOL
——|_2. Hybrid TRANSPORT
6. USER RECOVERY
5. CLOUD SYNC
Engagement
protocol
3. CLIENT
4. RELYING PARTY
4/s
auth - TRANSPORT . client
relying party
sync
user
35
```

## Slide 36

**36**

### **Co-location vs intent**

**2/5**

protocol /  auth · **TRANSPORT** ·  client ·  relying party ·  sync ·  user

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Co-location vs intent
AV
3. Reads the QR
1. Shows a QR Code
— 2. Scan w/ camera——>
4. BLE
"we are near!"
6. Logged in
5. Tap + Sign
2/5
protocol / auth - TRANSPORT . client - relying party - sync
user
36
```

## Slide 37

**37**

**3/5**

protocol /  auth · **TRANSPORT** ·  client ·  relying party ·  sync ·  user

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
AV
"we are near!"
BLE distance
protocol
3/5
auth - TRANSPORT . client - relying party - sync - user
37
```

## Slide 38

**38**

**PoC**

**Attacker's laptop**

Victim's laptop

Demo: "Phishing for Passkeys" - M. Kuckuk, ↗ inovex 2025

**4/5** protocol /  auth · **TRANSPORT** ·  client ·  relying party ·  sync ·  user

## Slide 39

**39**

### **Still open in 2026**

- **HiPass** measured the QR relay: 100% over 300 trials, 65s QR window across 10 major RPs (↗ <u>Kim et al., IEEE Access 2025)</u>

- **FIDO URI intent injection** : fixed in mobile browsers, but a father of the mobile FIDO-URI attack class (CVE-2024-9956, ↗ <u>Righi 2025)</u>

- Proximity still stops **remote** attackers: PoisonSeed relayed remotely and failed at BLE (↗ <u>Expel retraction)</u>

- Co-located, it's workable: plant BLE boxes in range, offices/airports/conferences (↗ <u>Kniep 2025)</u>

- **No RP-side tell** : through CTAP 2.3 (Feb 2026), an RP still can't distinguish a relayed hybrid ceremony from a real one (↗ <u>FIDO spec)</u>

**5/5**

protocol /  auth · **TRANSPORT** ·  client ·  relying party ·  sync ·  user

## Slide 40

**3. Client** and Client-Side attacks

## Slide 41

**41**

### **You are here**

**1/7** protocol /  auth ·  transport · **CLIENT** ·  relying party ·  sync ·  user

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
You are here
AV
1. AUTHENTICATOR /
PROTOCOL
——>|_ 2. Hybrid TRANSPORT
6. USER RECOVERY
5. CLOUD SYNC
Engagement
3. CLIENT
4. RELYING PARTY
protocol
4/7
auth - transport - CLIENT
relying party
sync
user
41
```

## Slide 42

### **Own the front door**

###### **WHO**

- browser vendors (Chrome, Firefox, Safari)

- extension devs (password managers)

- high-assurance RPs (fintech, gov)

###### **WHAT**

- UI transparency + userconsent awareness

- WebAuthn API override (activeTab)

- piggybacking

- risk-based-auth bypass resilience

###### **HOW**

- extension fuzzing (PoC malicious extensions)

- browser instrumentation (hook the API)

protocol /  auth ·  transport · **CLIENT** ·  relying party ·  sync ·  user

**42**

**2/7**

## Slide 43

**43**

#### **Attacker JavaScript forged a live Gmail passkey**

◆ ↗
attacker.passkey.tool
◆ ↗ Passkey Raider
◆ ...
◆ ↗ Passkey Editor

Demo: SquareX, "Passkeys Pwned" - DEF CON 33 2025 (↗ <u>sqrx.com/passkeys-pwned)</u>

**3/7**

protocol /  auth ·  transport · **CLIENT** ·  relying party ·  sync ·  user

## Slide 44

**44**

### **Signed Assertion Hijacking**

↗ Marek Toth, "DOM-based Extension Clickjacking", DEF CON 33 2025

**4/7**

protocol /  auth ·  transport · **CLIENT** ·  relying party ·  sync ·  user

## Slide 45

**45**

### **DOM-based Extension Clickjacking**

1. The attacker **finds XSS** on a server **where passkeys are used**

2. **Inject** JS **malware**

   1. **Redirect signed assertion** to attacker's controller server

**5/7**

protocol /  auth ·  transport · **CLIENT** ·  relying party ·  sync ·  user

## Slide 46

**46**

### **DOM-based Extension Clickjacking**

- **Hide passkey dialog** UI injected by password manager ( **uses DOM-based extension clickjacking technique** )

**6/7**

protocol /  auth ·  transport · **CLIENT** ·  relying party ·  sync ·  user

## Slide 47

**47**

### **DOM-based Extension Clickjacking**

4. The **victim** visits the URL with XSS vulnerability and **clicks once**

5. The attacker obtains the signed challenge

6. The **attacker sends the signed assertion** from their server **to the auth server**

**7/7**

protocol /  auth ·  transport · **CLIENT** ·  relying party ·  sync ·  user

## Slide 48

**4. Relying party**

## Slide 49

**49**

### **You are here**

**1/37** protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
You are here
AV
1. AUTHENTICATOR /
PROTOCOL
——_ 2. Hybrid TRANSPORT
6. USER RECOVERY
5. CLOUD SYNC
Engagement
S 3. CLIENT
protocol
—_— 4. RELYING PARTY
4/37
auth - transport - client - RELYING PARTY - sync - user
49
```

## Slide 50

**50**

### **On a high level**

- Trigger the ceremonies and analyze.

- Tampering, tampering, tampering

   - Fuzzing

   - Monkey tests, checklists

   - More nuanced assumptions

- <u>↗ Jannett et al., "State of Passkeys," 2026</u>

   - Actively tested 103 RPs

   - 103 vulnerable to at least one server-side attack.

   - 18 critical, 53 high.

**2/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

## Slide 51

**51**

### **Decoding problem**

Google SSO 75.2%, navigator.credentials-only 82.3%, known JS lib 18.6% ↗ <u>Census: Bhardwaj & Sastry, PAM 2026</u>

**3/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

## Slide 52

**52**

###### **Microsoft**

```
mysignins.microsoft.com
```

```
POST /api/post/newfido
Content-Type: form-urlencoded
```

```
canary=b0f2c1a9���
```

- `&clientDataJson=eyJ0eXBlIjo��`

- `&attestationObject=o2NmbXRkcG��`

- `&credentialId=3EHSf9K2mQ�� &credentialDeviceType=multiDevice &credentialBackedUp=true &transports=internal,hybrid`

- `&extensions=eyJjcmVkUHJv��`

###### **GitHub**

```
github.com
```

```
POST /u2f/trusted_devices
Content-Type: multipart/form-data
```

```
------WebKitFormBoundary���
Content-Disposition: form-data;
name="response"
```

```
{"id":"3EHSf9K2mQ��",
```

- `"type":"public-key",`

```
"response":{
```

- `"clientDataJSON":"eyJ0��`

- `"attestationObject":"o2N��`

```
},
```

```
"clientExtensionResults":{}}
```

###### **Google**

```
myaccount.google.com
```

```
POST /_/���/batchexecute
Content-Type: form-urlencoded
```

```
f.req=[[["GtmsU","[null,null,
null,"eyJ0eXBlIjoi��",
```

```
"o2NmbXRkcGFj��",
["internal"],null,1,1]",
null,"generic"]]]
```

- `&at=AFehe7k9dQ��`

- `�� idx 3 = clientDataJSON`

- `�� idx 4 = attestationObject`

```
------WebKitFormBoundary���--
```

###### **FLAT FORM FIELDS**

`position:` ~10 flat form params `decode: URL-encoded + Base64URL`

###### **MULTIPART + NESTED JSON**

`position:` spec field names, nested `decode: JSON + Base64URL`

###### **POSITIONAL ARRAYS**

`position:` fields by index in a blob `decode: URL-encoded + Base64URL`

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

**4/37**

## Slide 53

### **Decoded fields**

```
{
```

- `"clientDataJSON": {`

- `"type": "webauthn.get",`

You want:

- `"challenge": "zYJx-8mHw8wK7vC4qRseSJrDCd01yKIfZk_njXEOoeuQD7CuKUoQ2frvV0NBoJiVZSBgjUYy8vGb-0Lq-BS1wA",`

- `"origin": "https:��webauthn.io",`

- `"crossOrigin": false`

- `},`

- `"authenticatorData": {`

- `"rpIdHash": "74A6EA9213C99C2F74B22492B320CF40262A94C1A950A0397F29250B60841EF0",`

- `"flags": {`

- `"userPresent": true,`

- `"userVerified": true,`

- `"backupEligible": false,`

- `"backupState": false,`

- `"attestedCredentialData": false,`

- Traffic detection

   - across vendor wrappers

- Every field decoded: ◆ clientDataJSON

   - authenticatorData

   - signature

   - userHandle

**53**

- `"extensionDataIncluded": false`

- `},`

- `"signCount": 42`

- `},`

- `"signature": "304402207BC3E1F0A2D4C6980B5E3F1A2C4D6E8F0A1B2C3D4E5F60…DDEEFF02",`

- `"userHandle": "6D617474656F2D67696F7264616E6F"`

- `}`

**5/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

## Slide 54

**54**

### **Passkey Editor**

You have:

- Ceremony traffic detection

   - Registration/Authentication/Option

   - Fits every vendor

- Fields decoding:

   - clientDataJSON

   - attestationObject

   - authData

   - COSE key

   - ...

**6/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

## Slide 55

**55**

**7/37** protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Passkey Editor
Profiles Guide © About
Profiles
Profile: webauthn.io (Duo py_webauthn)
© Default (SimpleWebAuthn / generic) [not active]
@ webauthn.io (Duo py_webauthn)
3 passkeys-debugger.io (Next.js action) [not active]
© passkeys.io (Hanko) [not active]
© demo.yubico.com {not active]
@ webauthn.lubu.ch [auto-plant] [re-sign]
Add
Copy
Delete
Restore built-ins
AV
Enabled [_] Auto-plant ["] Auto re-sign
id: webauthn.io name: webauthn.io (Duo py_webauthn)
host match: EXACT ~  webauthn.io
default signing alg: EdDSA(-8) ~ plant attestation: None v
Registration
verify URL: CONTAINS v | /registration/verification method: POST
clientDataJSON O path regex _response.response.clientDataJSON © Auto © Raw ©) Base64 () Base64URL [} URL encoded webauthn.create decoded >
attestationObject O path regex response.response.attestationObject O Auto © Raw ©) Base64 () Base64URL [| URL encoded fmt=none - Ed25519 key decoded >
authenticatorData O path regex _response.response.authenticatorData © Auto © Raw ©) Base64 () Base64URL [| URL encoded UP UV AT: signCount 1 decoded >
credentialld O path © regex © Auto © Raw © Base64 ©) Base64URL [] URLencoded decoded >
Authentication
verify URL: CONTAINS v | /authentication/verification method: POST
clientDataJSON O path © regex | response.response.clientDataJSON © Auto © Raw ©) Base64 ©) Base64URL [_) URL encoded webauthn.get decoded >
authenticatorData O path © regex | response.response.authenticatorData © Auto © Raw © Base64 ©) Base64URL [_) URL encoded UP UV - signCount 2 decoded >
signature © path © regex  response.response.signature © Auto © Raw ©) Base64 (©) Base64URL [| URL encoded £d25519 - 64B decoded >
userHandle © path © regex | response.response.userHandle © Auto © Raw ©) Base64 () Base64URL [] URL encoded 37B - “webauthnio-asdadsada..." decoded >
credentialld © path © regex | response.rawld © Auto © Raw ©) Base64 () Base64URL [| URL encoded 328 - 893025b4e178... decoded >
Sample bodies
Registration body (paste the reg-verify request body):
{
“defcon34",
{
TALtOF4snCezIL1FNoc loQw3Ez4vDkLQIkxrqURt8Q",
ATALtOF4snCezIL1FNoc Lo@w3Ez4vDkLQIkxrqURt8Q",
2
“attestationObject": "o2NmbXRkbm9uZWdhdHRTdG100GhhdXRoRGFOYViBdKbqkhPJnC90siSSsyDPQCYq IMGpUKAS f yk LC2CEHvBFAAAAAQECAwQFBgc IAQIDBAUGBwgAI IkwJ bTheLJwnsyC9RTaHJ aNMNxM—Lw5SCOCJMa6 LEDfEpA
EBAycgBiFYIP8CuPmFEgEleDHT vdI5hBJwS2K3FKP2f—e130HLC_2u",
“clientDataJSON": “eyJ@eXBLIjoid2ViYXV@aG4uY3J LYXRLIiwiY2hhbGx Lbmd LI j oiSmV2VTBETm5 rUnRCOULsTnJiRO1vYmFMZGFTNmJSeUJha2tta3p IVEtyVFNQRZhCQk5 YWHBRSDFDU3NDY INORkJaTONDGFFtY@ LmMUE@anIrQ
VUGZHciLCJvcmlnawW4i0iJodHRwczovL3dLYmF1dGhuLmlv1iwiY3Jvc3NPcm\lnawW4i0mZhbHNLfQ",
Authentication body (paste the auth-verify request body):
TALtOF4snCezIL1FNoclo@w3Ez4vDkLQTkxrqURt8Q",
iTALtOF4snCezIL1FNocloOw3Ez4vDkLQIkxrqURt8Q",
2{
“authenticatorData": “dKbgkhPJnC90siSSsyDPQCYq\MGpUKAS fyk LC2CEHVAFAAAAAg" ,
“clientDataJSON": “eyJ0eXBLLjoid2ViYXVOaG4uZ2VOLiwiYZhhbGx Lbmd LI j oiZORGMTRZAE1iV kySGVwdV9PSOLPYZzdCR3BZSkc4Z3dEd2d fNXpWM LpNOFNKanFNa1dScGN4RnRkdFNXZESkZOFJOF pyWC1ydVRCdm1KcOJXcO1ka
nciLCJvcmlnaW4i0iJodHRwczovL3dLYmF 1dGhuLmlvIiwiY3Jvc3NPcmlnaW4iOmZhbHN1fQ" ,
"signature": "xMqa0xhmJ_68vH4KiUMougIZ1FGnJeVvvFVkUvJhRwGn9N-j S9Woa99BTY51-V5711U0G5MJ6_@ADJDFF80rDQ",
Check Prettify JSON Save profile all 8 configured field(s) extract cleanly
7/37
protocol / auth - transport - client - RELYING PARTY . sync - user
55
```

## Slide 56

**56**

**8/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
AV
Profiles Guide About
Profiles
© Default (SimpleWebAuthn / generic) [not active]
@ webauthn.io (Duo py_webauthn)
O passkeys-debugger.io (Next.js action) [not active]
© passkeys.io (Hanko) [not active]
© demo.yubico.com [not active]
@ webauthn.lubu.ch [auto-plant] [re-sign]
Add
Copy
Delete
Restore built-ins
8/37
protocol / auth - transport - client - RELYING PARTY . sync - user
56
```

## Slide 57

**57**

**9/37** protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
AV
id: webauthn.io name: webauthn.io (Duo py_we
host match: EXACT v
webauthn.io
default signing alg: EdDSA(-8) ~ _ plant attestation: None
9/37
protocol / auth - transport - client - RELYING PARTY . sync - user
57
```

## Slide 58

**58**

**10/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Registration
verify URL: CONTAINS v__ /registration/verification method: POST
clientDataJSON © path ©) regex response.response.clientDataJSON }
attestationObject O path ©) regex response.response.attestationObject r]
authenticatorData O path ©) regex response.response.authenticatorData 4
credentialld O path ©) regex }
Authentication
10/37
protocol / auth - transport - client - RELYING PARTY . sync - user
```

## Slide 59

**59**

**11/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
AV
Authentication
verify URL: CONTAINS v __ /authentication/verification method: POST
clientDataJSON O path ©) regex response.response.clientDataJSON (e)
authenticatorData O path ©) regex response.response.authenticatorData (eo)
signature O path ©) regex response.response.signature (e]
userHandle O path ©) regex response.response.userHandle (e]
credentialld O path ©) regex response.rawld
Sample bodies ra]
11/37
protocol / auth - transport - client - RELYING PARTY . sync - user
59
```

## Slide 60

**60**

**12/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
o0o0°0
o0000
~) Base64URL [| URL encoded} weba
Base64URL | | URL encoded] fmt=n
Base64URL [ | URL encoded]UP U\
Base64URL [_) URLencoded} de
Base64URL | | URL encoded|weba
Base64URL [| URL encoded]UP U)
Base64URL | | URL encoded} Ed25!
—) Base64URL [ | URL encoded]37B -
~) Base64URL [| URL encod: B -
12/37
protocol / auth - transport - client - RELYING PARTY . sync - user
```

## Slide 61

**61**

**13/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ou
‘Sample bodies
Registration
verify URL: CONTAINS v __ /registration/verification method: POST
clientDataJSON O path ©) regex | response.response.clientDataJSON O Auto (© Raw ©) Base64 (©) Base64URL [ | URL encoded]webauthn.create decoded >
attestationObject O path © regex | response.response.attestationObject O Auto © Raw ©) Base64 (©) Base64URL [ | URL encoded} fmt=none - Ed25519 key decoded >
authenticatorData O path ©) regex response.response.authenticatorData O Auto © Raw ©) Base64 (©) Base64URL [ | URL encoded} UP UV AT: signCount 1 decoded >
credentialld O path © regex O Auto © Raw © Base64 () Base64URL [) URLencoded| decoded >
Authentication
verify URL: CONTAINS y¥  /authentication/verification method: POST
clientDataJSON O path ©) regex | response.response.clientDataJSON O Auto © Raw ©) Base64 (©) Base64URL [| URL encoded} webauthn.get decoded >
authenticatorData © path © regex response.response.authenticatorData © Auto © Raw ©) Base64 () Base64URL [| URL encoded} UP UV - signCount 2 decoded >
signature O path © regex | response.response.signature O Auto © Raw ©) Base64 (©) Base64URL [| URL encoded} Ed25519 - 64B decoded > (10 }
userHandle O path © regex response.response.userHandle O Auto © Raw (©) Base64 () Base64URL [ | URL encoded} 37B - “webauthnio-asdadsada..." decoded >
O path ©) regex | response.rawld © Auto © Raw ©) Base64 () Base64URL [| URL encoded} 32B - 893025b4e178... decoded >
Registration body (paste the reg-verify request body):
{
“username": "“defcon34",
{
TALtOF4snCezIL1FNoc lo@w3Ez4vDkLQIkxrqURt8Q",
AiTALtOF4snCezIL1FNoc LoQw3Ez4vDkLQIkxrqURt8Q",
“response": {
“attestationObject": “o2NmbXRkbm9uZWdhdHRTdG1@0GhhdXRoRGFOYViBdKbqkhPJnC90siSSsyDPQCYq LMGpUKAS f yk LC2CEHVBFAAAAAQECAwQFBgc IAQ IDBAUGBwgAIIkwJ bTheLJwnsyC9RTaHJ aNMNxM—Lw5C@CJMa6 LEbTEpA
EBAycgBiFYIP8CuPmFEgE1eDHTvdI5hBJwS2K3FKP2f—el30HLC_2u",
“clientDataJSON": "“eyJ@eXB11joid2ViYxXVOaG4uY3J LYXRLLiwiY2hhbGx Lbmd 11 j oiSmV2VTBETm5 rUnRCOULsTnJ iR@1vYmFMZGFINm)SeUJha2tta3p LVEtyVFNQR2hCQk5 YWHBRSDFDU3NDY INORkJaTDNDGFFtY@ LmMUE@anlrQ
VUGZHciLCJvcm1naW4i0iJodHRwczovL3dlY¥mF1dGhuLmlvIiwiY3Jvc3NPcmlnawW4iOmZhbHNLfQ",
Authentication body (paste the auth-verify request body):
{
TALtOF4snCezIL1FNoc lo@w3Ez4vDkLQIkxrqURt8Q",
iTA1tOF4snCezIL1FNocloO@w3Ez4vDkLQIkxrqUuRtsQ",
Hae §
“authenticatorData": "“dKbqkhPJnC90siSSsyDPQCYq LMGpUKAS fyk LC2CEHVAFAAAAAG",
“clientDataJSON": "“eyJ@eXB11joid2ViYxXV@aG4uZ2VOI iwiY2hhbGx Lbmd11j oiZORGMTR2aE1iV LkySGVwdV9PS@ LPYzdCR3BZSkc4Z3dEd2d fNXpWM LpNOFNKanFNaldScGN4RnRkdFNXZESKZOFIJOFpyWClydVRCdm1Kc@JXcO1lka
nciLCJvcm1lnaW4i0iJodHRwczovL3dlYmF1dGhuLmlvIiwiY3Jvc3NPcm\lnaW4i0mZhbHNLfQ",
“signature”: “xMqa0xhmJ a
Check Prettify JSON Save profile all 8 configured field(s) extract cleanly
AV
13/37
protocol / auth - transport - client - RELYING PARTY . sync - user
61
```

## Slide 62

**62**

### **Tamper + re-sign**

- Edit any field, re-encode in place

- Any edit breaks the signature

   - re-plant the key

   - re-sign on passthrough

**14/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

## Slide 63

**63**

**15/37** protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
AV
Relying Party '
SERVER Client Authenticator
ee |
<— forged (1) Auth request (rR) —
(2) challenge, user info, RP info P
— forged >
(5) hash(clientDataJSON) ,
user info,
RP info, RP ID
(6) is User near?
(6.1) can User unlock?
(6.2) Creates the key pair
scoped to the RP ID
(7) attestationObject = {
(8) attestationObject hash(RP ID),
flags = [
UserPresence,
UserVerification,
Attested cred data,
Extension data
(3) navigator .credentials.create
(9) attestationObject,
clientDataJSON
ZzqAHSe
“Au
<— forged ——
a
(10) verify as per [1]
and add credentials to
its storage
zr4cprnome
AMnNnALonw
1,
LS credential ID,
public Key in CBOR,
AAGUID,
initial sig counter,
extensions
[
(vv
Plant new key
Resign w/ new key
(4) clientDataJSON = {
challenge,
RP origin,
"webauthn. create"
15/37
protocol / auth - transport - client - RELYING PARTY . sync - user
63
```

## Slide 64

**64**

### **Not the first tool**

◆ <u>↗ webauthn-cbor</u> decodes only, no attacks.

- <u>↗ passkey-scanner</u> passive detection.

- ◆ <u>↗ passkey-raider</u> tampers, but by hand. ◆ <u>↗ Burp_FIDO2</u> handles wrappers, rough on production traffic. ◆ <u>↗ Grafneter, Passt</u> -the-Passkey open-sourced at Black Hat this week. ◆ <u>↗ Passkeys.Tools (Jannet)t</u> emulates browser AND authenticator, tampers every field at scale

- **Passkey Editor's lane:** Burp-native, attack dropdown live across Intercept, history, and Repeater, auto re-sign on passthrough, decoding paired with tampering.

**16/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

## Slide 65

**65**

### **clientDataJSON**

Raw HTTP request

Passkey Editor

**17/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

## Slide 66

**66**

### **challenge**

**18/37** protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
challenge
SEED
Pretty Raw Hex Passkey Editor R Swe
Attacks» @% Wrap
Flags: @ uP @ uv [| BE () BS
{
"clientDataJSON": {
“type”: "webauthn.get",
"challenge": "evil_challenge",
"origin": "https://webauthn. io",
“crossOrigin": false,
“other_keys_can_be_added_here": "do not compare clientDataJSON against a template.
See https://goo.gl/yabPex"
,
“authenticatorData": {
“rpIdHash": "74A6EA9213C99C2F74B22492B320CF40262A94C1A950A0397F29250B60841EFO",
“extensions”: {},
“signCount": 2,
"flags": {
“userPresent": true,
“userVerifi true,
“backupEligible": false,
“backupState": false,
“attestedCredentialData": false,
“extensionDataIncluded": false
},
“attestedCredentialData": {}
},
"signature":
“4C0944C43B98FD85B7131C127173B4FE2C6F095C876106BBB1EAC6DC326AF3F7B5B0D4F4867C56BCFE7OBBDC
ODB6AQ0A41BEFD50BF868D4A60018656FFOECFOF”
+
18/37
AV protocol / auth - transport - client - RELYING PARTY . sync - user
```

## Slide 67

**67**

### **origin + rpIdHash**

origin

rpIdHash

**19/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
origin + rpldHash
Pretty Raw Hex Passkey Editor
Attacks~  [@ Wrap
Flags: @ uP @ uv [| BE () BS
{
“clientDataJSON": {
"type": "webauthn.get",
“challenge”:
"g_c7EstEOZpRh20H4KPASg2bQ7t3wIAONISalal5UwJu LYLnyIpBidcy9gSHNPsdCaj 4e4wzuRQSOMgNU-tRmA",
"origin": "https: //evil.defcon34.xyz",
“crossOrigin": false,
“other_keys_can_be_added_here": "do not compare clientDataJSON against a template.
See https://goo.gl/yabPex"
“authenticatorData": {
“rpIdHash": "74AGEA9213C99C2F74B22492B320CF40262A94C1A950A0397F29250B60841EFO",
“extensions”: {},
“signCount": 2,
"flags": {
“userPresent": true,
“userVerified": true,
“backupEligible": false,
“backupState": false,
“attestedCredentialData": false,
“extensionDataIncluded": false
}
“attestedCredentialData": {}
},
“signature”:
“1AF21C1F86B8C216576A09A4575E89BB97A875E4D2A3C4AA2FB4FD20DB6E10DE43938FC12AF1AQFD83DCC704
E£5401D7E3F3542C19472822BEA251454E6CO960A"
}
origin
AV
Pretty Raw Hex Passkey Editor
Attacks ~ @ Wrap
Flags: @ UP @ UV (] BE [] BS
{
“clientDataJSON": {
"type": "webauthn.get",
“challenge”:
"SnFcY_gy4P0——D3ueYA6PrxBH56Euw_3BcEj Bahj tm9tQq8Yk8JNAeDfxN47a4wgp3yNfwPcEySw8axZXhMigaA",
“origin”: "https://webauthn. io",
“crossOrigin": false
},
“authenticatorData": {
“rpIdHash": "@@AGEA9213C99C2F74B22492B320CF40262A94C1A950A0397F29250B60841EFO",
"extensions": {},
“signCount": 2,
"flags": {
“userPresent": true,
“userVerified": true,
“backupEligible": false,
“backupState": false,
“attestedCredentialData": false,
“extensionDataIncluded": false
},
“attestedCredentialData": {}
},
“signature”:
"396EBFCC02B229F152413D4F2EBC30AE7815E4EBA939EAB38A2871F52F962153A81E207D9FFB38181B1EE208
60736655A547320DC10732961492BA548E8F4COCc”
}
rpldHash
19/37
protocol / auth - transport - client - RELYING PARTY . sync - user
67
```

## Slide 68

**68**

### **Over-scoping the RPid**

**20/37** protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Over-scoping the RPid
AV
rpld = example.com
(but only app.example.com valid for *.example.com |——>]  customerl.example.com —forges>} customer2.example.com
needed)
cross-origin
ACCOUNT
TAKE
OVER
protocol
auth - transport
20/37
client - RELYING PARTY - sync
user
68
```

## Slide 69

**69**

### **Dangling Allowlist Domain**

**21/37** protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
AV
Dangling Allowlist Domain
/well-known/webauthn
allowlist
(a.com, b.com, patner.com)
partner.com LAPSES
—_
attacker buys it @ 10 Slvr | >
attacker origin now
TRUSTED
cross-origin
ACCOUNT
TAKE
OVER
protocol / auth - transport
21/37
client - RELYING PARTY - sync
user
69
```

## Slide 70

**70**

### **attestationObject and authenticatorData**

**22/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

## Slide 71

**71**

**23/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ATTESTATION OBJECT
“fmt*: “packed* “attSumt*: ... “authData™: ...
AUTHENTICATOR DATA
32 bytes 1 byte 4 bytes (big-endian uint32) variable length variable length if present (CBOR)
RP ID hash FLAGS COUNTER ATTESTED CRED. DATA EXTENSIONS
cn iaseoaieoen u y
If Basic or Privacy CA:
If ECDAA:
AV
ED AT 0 O 0O
ae os
UV
1
O UP
14
7
0
—————_ >.-+———~.
AAGUID
L (CREDENTIAL ID
CREDENTIAL PUBLIC KEY
16 bytes
2 bytes LENGTH L
(variable length)
ATTESTATION STATEMENT (in "packed" attestation statement format)
“alg: ...
Males scs
ORS. cas
Sig ss cs:
ROCs acs
“ecdaaKeyld*: ...
protocol / auth - transport - client - RELYING PARTY - sync -
variable length (COSE_Key)
23/37
user
71
```

## Slide 72

**72**

**24/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
AV
ATTESTATION OBJECT
“fmt: “packed“
“attSumt: ...
“authData™: ...
_————d
i
i AUTHENTICATOR DATA
i 32 bytes 1 byte 4 bytes (big-endian uint32) variable length variable length if present (CBOR)
RP ID hash FLAGS COUNTER ATTESTED CRED. DATA EXTENSIONS
H rr ' ° .
H ED AT 0 0 ©O UV O UP A the t t
Po utnentication
' AAGUID L |CREDENTIAL ID | CREDENTIAL PUBLIC KEY
i 16 bytes 2bytes  LENGTHL variable length (COSE_Key)
H (variable length)
ATTESTATION STATEMENT (in "packed" attestation statement format)
If Basic or Privacy CA: “alg: ... “sig: ... “xSe"s o.
IfECDAA: = “alg*: ... “sig: ... “ecdaaKeyld™: ...
24/37
protocol / auth - transport - client - RELYING PARTY . sync - user
72
```

## Slide 73

**73**

**25/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ATTESTATION OBJECT
“fmt*: “packed “attSumt*: ... “authData™: ...
i
i AUTHENTICATOR DATA
i 32 bytes 1 byte 4 bytes (big-endian uint32) variable length variable length if present (CBOR)
RP ID hash FLAGS COUNTER ATTESTED CRED. DATA EXTENSIONS
—_—a@—-—_—~ C 7
H T T T T T T
| mario cower] Authentication
7
—. OC [7
AAGUID L_ |CREDENTIAL ID | CREDENTIAL PUBLIC KEY
16 bytes 2 bytes LENGTH L variable length (COSE_Key)
(variable length)
\ = J
ATTESTATION STATEMENT (in "packed" attestation statement format)
If Basic or Privacy CA: “alg*: ... “sig: ... “xSe":
IfECDAA: = “alg**: ... “sig: ... “ecdaaKeyld*: ...
SJ
25/37
protocol / auth - transport - client - RELYING PARTY . sync - user
```

## Slide 74

**74**

### **signature**

**26/37** protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
signature
AV
Pretty Raw Hex Passkey Editor R Swe
Attacks + Wrap
Flags: @ uP @ uv [| BE () BS
{
"clientDataJSON": {
“type”: "webauthn.get",
"challenge":
“SnFcY_gy4P0——D3ueYA6P rxBHS6EuwW_3BcEj Bahj tm9tQq8Yk8 JNAeDTxN47a4wgp3yNfwPcEySw8axZXhMiga",
“origin”: "https://webauthn. io",
“crossOrigin": false
},
“authenticatorData": {
“rpIdHash": "74A6EA9213C99C2F74B22492B320CF40262A94C1A950A0397F29250B60841EFO",
"extensions": {},
“signCount": 2,
“flags”: {
“userPresent": true,
“userVerified": true,
“backupEligible": false,
“backupState": false,
“attestedCredentialData": false,
“extensionDataIncluded": false
},
“attestedCredentialData": {}
},
"signature":
"585F37FDF8B02D37B69490DF81D684D895 1BB65EA5F39E13F5843E9E67C37A5926F8A09902D9FEGEG831BFAD
951C6145F5BA365188E64E3C348DA3285EEGEEO4"
}
26/37
protocol / auth - transport - client - RELYING PARTY .
sync - user
74
```

## Slide 75

**75**

### **alg**

**27/37** protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
AV
alg
Pretty Raw Hex Passkey Editor R Swe
Attacks ~ Wrap
Signing algorithm: RS256 (-257) ~ |Attestation: None v [266 key planted]
Flags: M UP @ Uv [) BE [) BS
{
"clientDataJSON": {
"type": "webauthn.create",
“challenge”: "jdrVAViggNSwIpX3MX6QtnmQJgNoCVxwwLCFles—6F9ThLq_LFAKw4co1BQ3n_XquOmbcA9fsfU_7qGHQVga2w",
“origin”: "https://webauthn. io",
“crossOrigin": false
},
“attestationObject": {
“attestationStatement": {
“format”: "none"
,
“authenticatorData": {
“rpIdHash": "74A6EA9213C99C2F74B22492B320CF40262A94C1A950A0397F29250B60841EFO",
"extensions": {},
“signCount": 1,
"flags": {
“userPresent": true,
“userVerified rue,
“backupEligible": false,
“backupState": false,
“attestedCredentialData": true,
“extensionDataIncluded": false
},
“attestedCredentialData": {
“aaguid": "01020304-0506-0708-0102-030405060708",
cosekey
"A401030339010020590100B104054256CE44CECCC357B8A1444DB2A1698C8D37AC992B52ED79B33 1AF43BED77844651D3959EC15CFE38F6552F
234AFEDFC5D7AF5F79E067136BFC335C6272FC2FF8A8EA58849E9DF31EA2D27C9F0908D47DDD7FDDD781FD2F8CB51ED@BC8058994522A4C13A41
331B85C037DDBAAED47775A401488E6D5E3823466724D22C6F6BAF274F7B6A8C8EB9660ECCD0BB14530818CE850A553A87A87 7A2B1C3A88695D7
A@A319FD6AB26113D7F59CFEEFD2D6725FA9BD3BD2D5CFB0568E7 0F31FCDFEBCA7FCDD1C2EAF4B46C44FD1D7A8269080D9A4A1DB3FAE649E1073
4D4729386160C39FC12B660B611765B9C45BC9E9ED548110766221D9C42906A2273CAEF2143010001"
i
“credentialId": "755A521FCEF1ABC93EA6CODDC6B54FAB4CDED7E102DCB4F@9B416C29180AA3CD"
+
},
“fmt":
}
}
"none"
protocol / auth - transport - client - RELYING PARTY . sync - user
27/37
75
```

## Slide 76

**77**

### **credentialId**

**29/37** protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
AV
credentialld
Pretty Raw Hex Passkey Editor & 5 in
Attacks + Wrap
Signing algorithm: RS256 (-257) - Attestation: None v RS256 key planted
Flags: @ UP @ Uv [) BE [] BS
{
"clientDataJSON": {
"type": "webauthn.create",
“challenge”: "jdrVAViggNSwIpX3MX6QtnmQJgNoCVxWwLCFles—6F9ThLq_LFAKw4co1BQ3n_XquOmbcA9fsfU_7qGHQVga2w",
“origin”: "https://webauthn. io",
“crossOrigin": false
},
“attestationObject": {
“attestationStatement": {
“format”: "none"
},
“authenticatorData": {
“rpIdHash": "74A6EA9213C99C2F74B22492B320CF40262A94C1A950A0397F29250B60841EF0",
"extensions": {},
“signCount": 1,
"flags": {
“userPresent": true,
“userVerified": true,
“backupEligible": false,
“backupState": false,
“attestedCredentialData": true,
“extensionDataIncluded": false
},
“attestedCredentialData": {
“aaguid": "01020304-0506-0708-0102-030405060708",
“coseKey": {
"keyType": "RSA",
"algorithm": "RS256",
"raw":
"A4010303390100205901009EEAC616434B9A4603B286B10089427B1CA3A4C7C8F599A1909A07D4CO8E7 FB038E0244894450F5 129EFEGEOOBAS4
70862E87DA611255CAQ064CB6BAAC891E336FEC6C9D4A04A04F77ODBBF7E5831C078B87 10B3434F4C5DEASACF42F853C81BE1E215FF9ECA1FBAS
2F730163778E2F6AF5F65D66A20C2CEC5S8EF6B4E399B2A7CA7856C8F6E6E838CO6F8884C5E66966D75CBEGDA49035AE2BA3FC7A88D5F6A93557E
1E£23E0B13B3C8C0E47CE9A4D9791E0181456177ED790100A7D77723A00A56ECE30FB58A8483B20B1F2230A0A4577DEE35797844C6EOFF3BBDE61
COE27COF5373EEA0278F2D72147B3D5 10C22DF8369EOEBFF9E617511934D1DC76BBB3F 32143010001"
i"
“credentialId": "7AF8A5FDCADE7627" |
}
},
“fmt": "none"
+
}
29/37
protocol / auth - transport - client - RELYING PARTY . sync -
user
77
```

## Slide 77

**78**

### **signCount**

**30/37** protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
signCount
Pretty Raw Hex Passkey Editor Q 5s i=
RP evil Auth
Attacks Wrap
Flags: uP uv |) BE [) BS
12 12 {
“clientDataJSON": {
13 13 “type": "webauthn.get",
“challenge”:
1 q "SnFcY_gy4P0——D3ueYA6P rxBH5S6EuW_3BcEjBahj tm9tQq8Yk8JNAeDfxN47a4wgp3yNfwPcEySw8axZXhMiga",
14 “origin”: "https://webauthn. io",
15 “crossOrigin": false
},
15 “authenticatorData": {
18 1 “rpIdHash": "74A6EA9213C99C2F74B22492B320CF40262A94C1A950A0397F29250B60841EF0",
S "extensions":
“signCount": 13333337,
x "flags": {
“userPresent": true,
“userVerified": true,
* “backupEligible": false,
“backupState": false,
“attestedCredentialData": false,
“extensionDataIncluded": false
},
1 14] 1 4] ; “attestedCredentialData": {}
2 O “signature” :
“D3EBS4B0EF 8A3A07F8B20A00197DABC9C75F43C02857503AA4E5CE18DF883E9637 8CDOEGD6FD5FEB5522135E
77FDA173BDE16AE256986197BDEA26CE22B6ABOF"
21 }
30/37
AV protocol / auth - transport - client - RELYING PARTY . sync - user
```

## Slide 78

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ @ vB Websuthn.ic x +
€ >» G  % webauthn.io bas & a ©
WebAuthn.io
A demo of the WebAuthn specification
hk
example_username
Register Authenticate
Advanced Settings
ik {0 Elements Console Application WebAuthnX Sources >> @ 8 2 xX
Enable virtual authenticator environment
7 Authenticator 90e32 @ active Remove
uuID ec3e8453-ec81-4fee-820c-f f2fe9190e32
Protocol ctap2
Transport internal
Supports resident keys Yes
Supports large blob No
Supports user verification Yes
Supports hmac-secret No
Supports hmac-secret-me No
Credentials
ID Is Resi... RPID User Handle Signature Cou... Actions
No credentials. Try calling navigator.credentials.create() from your website.
New authenticator
We
Burp Suite Profe 2 21 d to Am Ventures, In:
tor ®@-~ 2
latch and replace ro Proxy settings
decific extensions Search Q @ filteron @ :
Edited Status code Notes Length MIME type Extension Title TS =P Cookies
Jentication/verification 200 Authentication - webauthn.io 418 JSON Y —-54,184,242.104 _sessionid=1fr4kc...
Yentication/options 200 Options - webauthn.io 611 JSON Y __54.184.242.104
t ification 200 Registration - webauthn.io 316 JSON Y_54.184.242.104
| Response GQ== a
& in = Pretty Raw Hex Render = 3
| 1 HTTP/2 200 OK 8
| 2 Alt-Svc: h3=":443"; ma=2592000 |
2zvceuolw 3 Content-Type; application/json
4 Cross-Origin-Opener-Policy: same-origin
5 Date: Fri, 17 Jul 2026 18:25:11 GMT B
Mac OS X 1@_15_7) AppleWebKit/537.36 (KHTML, 6 Referrer-Policy: same-origin
5 7 Server: Caddy Zz
*;v="150", "Google Chrome"; v="150" 8 Server: gunicorn 2.
9 X-Content-Type-Options: nosniff 8
10 X-Frame-Options: DENY
11 Content-Length: 18
12
13 {
“verified": true
Pf6VSrttwzh4",
grtPf6VSrttwzh4",
FOYViBdKbgkhPJnC9Gs iSSsyDPQCYq IMGpUKAS fyk LC2CEHV f~
EU aaa a ae
YPb8Sn4QxH3", DEM O #1
viY2hhbGx Lomd LI j oi cVFSZWhsRURXaWV4VHUWwQnY 4aV9Kd1
KE@TXhiSFVGRj J LZG1wbnVMYUg2b2RNaVRSczZJSnZ4aEFNc
§GhuLmLvLiwiY3Jvc3NPcmLnaWaiOmZhbHNUfQ", Decode
3IFFIQZFPGR_LkyChiNXtpCBb1g9vxKfhDEfc", Pla nt
1C2CFHVRFAAAAAOAAAAAAAAAAAAAAAAAAAAAATND 51n7.1Z Re = S | g n
| PP Ohightights ©) {} ¢ > | Search ®
XL
toy
@ Memory: 194.7MB of 8.00GB
```

## Slide 79

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
¢ v — & Websuthn.io x 1
webauthn.io
WebAuthn.io
A demo of the WebAu
example_username
Register
Advanced Settings
[0 Elements Console Application WebAut
Enable virtual authenticator environment
@ Authenticator b05e4
uuID 81ae6ab8-ee35-4ea9-a2ea-ae)
Protocol ctap2
Transport internal
Supports resident keys Yes
Supports large blob No
Supports user verification Yes
Supports hmac-secret No
Supports hmac-secret-mc No
Credentials
ID Is Resident RP ID U
No credentials. Try calling navigator.cre¢
New authenticator
Bese
Target Proxy Repeater Extensions
Passkey Editor
Profiles Guide About
Passkey Editor
Burp Suite Professional v2026.6 - 2026-06-21 - licensed to Anvil Ventures, Inc
@- 28
Profile: webauthn.io
@ Default (SimpleWebAuthn / generic)
@ webauthn.io
Github [not active]
Add
Copy
Delete
Restore built-ins
Event log (15)® All issues
Enabled Auto-plant Auto re-sign
id: webauthn.io name: webauthn.io
host match: EXACT ¥  webauthn.io
default signing alg: EdDSA(-8) - _ plant attestation: None v
Registration
verify URL: CONTAINS v  /registration/verification method: POST
clientDataJSON © path regex response.response.clientDataJSON © Auto Raw Base64 Base64URL URLencoded decoded »
attestationObject O path regex response.response.attestationObject © Auto Raw Base64 Base64URL URL er »
authenticatorData O path regex response.response.authenticatorData O Auto Raw Base64 Base64URL URL er >
credentialld O path regex O Auto Raw Base64 Base64URL URL encoded decoded »
Authentication
verify URL: CONTAINS ~  /authentication/verification method: POST
clientDataJSON © path regex response.response.clientDataJSON O Auto Raw Base64 Base64URL URL er »
authenticatorData © path regex _response.response.authenticatorData © Auto Raw Base64 Base64URL URL encoded decoded »
signature O path regex response.response.signature O Auto Raw Base64 Base64URL URL encoded decoded >
userHandle © path regex response.response.userHandle O Auto Raw Base64 Base64URL URL encoded decoded >
credentialld O path regex response.rawid O Auto Raw Base64 Base64URL URL er ,
Sample bodies
Registration body (paste the reg-verify request body):
{"username":"defcon", "response": {"id":"2n_nWdkL1NO901dCNGw3ZCTY 7NORqrtPf6V5rttwzh4","rawId":"2n_nldk1NO901dCNGw3zCTY7NORgrtPféVSrttwzh4", "response" :{"attestationObje
ct": "o2NmbXRkbm9uZWdhdHRTdG1@0GhhdXRoRGFOYViBdKbgkhPInC9OsiSSsyDPQCYq LNGpUKAS f yk \C2CEHVBFAAAAAQAAAAAAAAAAAAAAAAAAAAAAIND_51nZJZTTvTtXQj RSN8Bwk202Tkaq7T3—Lea7bcM4epAEBA
ycgBiFYIBy iVEZvCBXyUNnzxkfy5MgoY j V7aQgW9YPb8Sn4QxH3", “clientDataJSON" :“eyJ@eXBLI joid2ViYXV@aG4uY3J LYXRLI iwi YZhhbGx Lbmd LI j oicVFSZWhSRURxaWV4VHUwQnY4aV9Kd190d03ZWLBkVHB
ZdzdrQXY4LXFLWUZLMU1PbXE@TXhiSFVGRj J LZG1wbnVMYUg2b2RNaVRSczZJSnZ4aEFNCVEALCJvcminaW4i0iJodHRwczovL3d1YmF1dGhuLmlvIiwiY3Jvc3NPcmLnaW4iOmZhbHN1fQ", "transports": ["nfc"],
“publickeyAlgorithm":-8,"publickey":"MCow8QYDK2VWwAyEAHKIURMBIF fJQ2fPGR_LkyChiNXtpCBb1g9vxKfhDEfc", "authenticatorData": "dKbqkhPJnC90s iSSs yDPQCYq LMGpUKAS f yk LC2CEHVBFAAA
AAQAAAAAAAAAAAAAAAAAAAAAAIND_51nZJZTTVTtXQ j RSNBWk20zTkaq7T3~Lea7bcM4epAEBAycgBiFYIBy iVEZVCBXyUNnzxk fy 5MgoY j V7aQgWSYPb8Sn4QxH3"}, "type" :"public-key", "clientExtensionRe
sults":{"credProps":{"rk":true}}, “authenticatorAttachment":"“cross-platform"}} ~ >)
DEMO #1
Authentication body (paste the auth-verify request body):
tu defcon", "response": {"id":"2n_nWdk11NO901dCNGw32CTY7NORqrtPT6V5Srttw2h4","rawId":"2n_nWdk11N0901dCNGw3zCTY7N
ta": "dKbqkhPJnC9@siSSsyDPQCYq LMGpUKAS fyk LC2CEHVAFAAAAAg" , "clientDataJSON” : "eyJ@eXB1Ijoid2ViYxV@aG4uZ2VOliwiY2nhbGx Lbmd U
tc3Npa2po0GdoRj AtTFAZVESSTE1YV@53aDNs cE1LVDhnRkd@QUJma2hESmJ fTUFZa@JEbGciLCJvcm\(naW4 i0i JodHRwczovL 3d1YmF1dGhuLmlvIiwiY3;
ajhqDvaDfHCg_kNgZ8Tzc6RnUGKC7 v6 j fM2cyAzA2jukZciDJovLMqJTvSJ1eoXKLIgVAq9AwdjgDg", “userHandLe" :"d2ViYXV@aG5 pby1kZWZjb24"}
},“authenticatorAttachment":"cross-platform"}}
AUTO
mode
Check Prettify JSON Save profile
XL J
@ Memory: 388.6MB of 8.00GB “iv
```

## Slide 80

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
e¢ ’ ©) Account security
< > CG 23 github.com/settings/security
= q) Settings
matteo-giordano-defcon (ma
Your personal account
A Public profile
8 Account
& Appearance
tr Accessibility
Q Notifications
Access
6 Billing and licensing »
& Emails
| © Password and
authentication
(P) Sessions
& SSH and GPG keys
@ Credentials
Organizations
® Enterprises
(© Moderation v
Code, planning, and automation
G Repositories
& Codespaces
@ Packages
& Copilot v
& Pages
© Saved replies
Security
Dae «BR es
Target Proxy Repeater Extensions
Passkey Editor
Profiles Guide About
Profiles
Burp Suite Professional v2026.6 - 2026-06-21 - licensed to Anvil Ventures, Inc
Passkey Editor
Profile: Github
@- 28
@ Default (SimpleWebAuthn / generic)
© webauthn.io [not active]
@ Github
Add
Copy
Sign i Delete
Restore built-ins
Go
Sig
Qa
Ap
Sig
Two-fé
Two-|
your)
Event log (13) All issues
Enabled
id: github
host match; EXACT v _ github.com
Auto-plant Auto re-sign
name: Github
default signing alg: ES256 (-7) Y plant attestation: None v
Registration
verify URL: CONTAINS v  /u2f/trusted_devices method: POST
clientDataJSON path © regex "clientDataJSON":"(**}+)" Auto () Raw ©) Base64 © Base64URL URL er »
attestationObject path © regex "attestationObject":"(*"]+)" Auto Raw Base64 © B B4URL URL er >
authenticatorData © path ©) regex O Ato Raw Base64 B: URL URL er »
credentialld path © regex “rawld*:"((*"}+)" Auto Raw Base64 © S4URL URL er »
Authentication
verify URL: CONTAINS y  /session method: POST
clientDataJSON path © regex %22clientDataJSON%22%3A%22(%]+)%22 Auto _) Raw Base64 © Base64URL URL er »
authenticatorData path © regex %22authenticatorData%22%3A%22(" %]}+)%22 Auto Raw Base64 © Base64URL URL encoded decoded >
signature path © regex %22signature%22%3A%22(%]+)%22 Auto (©) Raw ©) Base64 © Base64URL || URL er decoded »
userHandle >) path © regex %22userHandle%22%3A%22((0%]+)%22 Auto () Raw ©) Base64 © Base64URL |) URLencoded decoded >
credentialld © path © regex %22rawld%22%3A%22( %]+)%22 Auto Raw Base64 © Base64URL URL er »
Sample bodies
Registration body (paste the reg-verify request body):
aoo--- WebKitFormBoundaryFt LLB LmkKBUEZTOzJ
Content-Disposition: form-data; name="authenticity_token"
8JuWgKqopK3oy7v0501uHdacwz_X15yfil5_dE9j4SZnDC7R7VOiBMgCONTbs81ZSh_—Ugj Voha0Qjm09xdDRA
—WebKitFormBoundaryFtULBUmK8UEZTOzJ
Content-Disposition: form-data; name="response”
{"type": "public-key", "id":"Tjhj@zM4Ze3Ak] JTBObktKpJbU8", “rawId" :"Tjhj@zM4Ze3AkJIJTBObktKpJbUS","authenticatorAttachment”
@eXB11j oid2ViYXVOaG4uY3J LYXRLIiwiY¥2hhbGx Lbmd 11j oiaFk1bWLAMkZpanRGUUhWe LFCcOtoTVRQCGZ2N2ImbO@53QVYXR1IHQNOx4WSIsIm9yawWdpbi|
ul jpmYwWxzZxo",“attestationObject":"o2NmbXRkbm9uZWdhdHRTdG100GhhdXRORGFOYV iYOUusAIGASHGB Lj oOVOwJ vVx8NmnZI j c2Ddj mxOudxZWBd|
Authentication body (paste the auth-verify request body):
authenticity_token=4BCkleAvf7Gx74hakELcxN8swj 2K5eED_Qa1A8pG7y4dgMCZUAByxAhnKWyWOGNSCi f BpsKKMSPFQc 1qwqHEGQ&webauthn_re|
%22%3A%22T j hj O2M4Ze3AkIITBObKtKp J bUB%22%2C%22 rawId%22%3A%22T} hj @2M4Ze3Ak) JTBObKtKpIbUB*22%2C%22authent icatorAt tachment
ientDataJSON%22%3A%22eyJ0eXBLIj 0id2ViYXVOaG4uZ2VOI iwi YZhhbGx Lbmd LI j oAWESFdUxtUVVOTVpEUXZpVnltwb2g0Z09G0S ImdWtRUGtRdnF j MH
SIsImNyb3NzT3JpZ2 ul j pmYWxzZSwib3RoZXJ fa2V5c19j YWS fY¥mVfYWRKZWRfaGVyZSI6ImRvIGSvdCBjb21wYXJ LIGNSaWVudERhdGFKUOSOIGFnYW lu
hYLBLeCI9%22%2C422authent icatorDatas22%3A%220USAIGAHGS 1 j OOVOwJVVxBNMnZI j C2Dd j mxOu@xZWAGAAAAAAS22%2C%22s ignatures22%3A%
Ze2ALEASGP6VEPtHSh4Yk-QOSDZM7dn2PS@KHDUWLKU99eI 1f0%22%2C%22userHand Le%22%3A%22ERYW-OUGd rnxCkuQkwAM40cuiP1UZEHLE_i7qdYK4}
2&7D%2C%22c LientExtens ionResults%22%3A%7B%70%7D&webauthn-condit ional=false&javascript-support=trueswebauthn-support=sup}
_to=htt ps&3A%2F%2F github. coms2F login&allow_signup=&client_id=Sintegration=&required_field_49d6=Gt imestamp=1784330483124)
58bal4eclec961f05384142834180a651a2
Check Prettify JSON Save profile
X
DEMO #2
Attack the
Registration
@ Memory: 350.1MB of 8.00GB “ov
```

## Slide 81

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Burp Suite Prof ional v2026.6 - 2026-06-21 - licensed to Anvil Ventures, inc
@ ~ QQ) SignintoGitHub-GitHub x +
@®. 28
€ > G_— & github.com/login Gx
eh
oO
(=)
ce © Proxy settings
O Drop ® Open browser (Q) :
Sign in to GitHub
Username or email address
l ,
Password oO matteo-giordano-defcon
Passkey - Apple Passwords
[0 Use Passkey from Another Device
a | © Manage Passwords and Passkeys... On
or
&y Continue with passkey G
G Continue with Google
© Continue with Apple Intercept is off
m ies If you tum Intercept on, messages between Burp's browser and your target servers are held here.
New to GitHub? Create an account This enables you to analyze and modify these messages, before you forward them.
Lea mere
DEMO #3
Attack the
Sign in
Ss y)
e Terms Privacy Docs Contact GitHub Support Manage cookies Do not share my personal information @® Memory: 374.7MB of 8.00GB +1
```

## Slide 82

**84**

### **Even the big players**

- <u>CVE-2026-46419</u> (Yubico java-webauthn-server, the reference RP library): returns success for a credential owned by a different user in 2FA / non-discoverable flows.

- <u>CVE-2025-26788</u> (StrongKey FIDO Server): treats non-discoverable as discoverable and doesn't bind the assertion to the initiating username, so substitute your own credId and sign in as the victim.

- <u>CVE-2024-12225 (Quarkus, CVSS 9.1): leftover default register/login endpoints</u> stay reachable, yielding a login cookie for any username.

- <u>CVE-2025-12150 and CVE-2026-6856 (Keycloak): attestation-policy bypass via</u>

- fmt:none, and an AAGUID-allowlist bypass via packed self-attestation.

**36/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

## Slide 83

**85**

### **Checklist + Creativity**

###### **Checklist**

- signature verified

- credId bound to one user

- UV honored

- UP honored

- origin allowlist (exact)

- crossOrigin rejected

- rpIdHash = sha256(rpId)

- challenge fresh + session-bound

- type create vs get

- COSE alg allowlist

- userHandle validated

- credId length 16-1023

###### **Creativity**

   - rpId over-scoping

   - dangling Related-Origin (/.well-known/webauthn)

   - clickjacking / framing (register)

   - enrollment step-up

   - CSRF on register

   - admin-API / Entra enrollment

   - post-compromise persistence

   - recovery downgrade

   - mixed-mode fallback (password / TOTP)

   - post-ceremony session binding

   - credential-management authz

   - leftover default endpoints

- duplicate credId rejected

- signCount checked

- fmt:none empty

- AAGUID allowlist

- BE/BS coherent

- Token Binding rejected

**37/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user

## Slide 84

**5. Cloud sync**

## Slide 85

**87**

### **You are here**

**1/5** protocol /  auth ·  transport ·  client ·  relying party · **SYNC** ·  user

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
You are here
AV
1. AUTHENTICATOR /
PROTOCOL
———|>|_ 2. Hybrid TRANSPORT
6. USER RECOVERY
<——
5. CLOUD SYNC
Engagement
protocol
3. CLIENT
4. RELYING PARTY
4/5
auth - transport - client - relying party - SYNC - user
87
```

## Slide 86

**88**

### **Types of Passkeys**

**2/5** protocol /  auth ·  transport ·  client ·  relying party · **SYNC** ·  user

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Types of Passkeys
AV
DEVICE-BOUND
on one device
you hold
SYNCED
SHARED
synced into a
CLOUD ACCOUNT
iCloud Keychain or
Google Password Mgr
EXPORTED
granted to other users
Apple + most 3rd party:
shared vaults
pulled out of the provider
backup/migrate
(FIDO CXF / CXP)
that device
(Secure Enclave /
TPM)
the cloud account
every account it's
shared to
weakest one wins
only the backup
file's own
password, if any
protocol / auth - transport - client - relying party - SYNC - user
Type
Trust
2/5
88
```

## Slide 87

**89**

### **The Cloud options**

- **First-party** (iCloud Keychain, Google)

   - The vendor owns the hardware, OS, and sync servers

   - keys stay inside vendor HSMs and never leave hardware.

- **Third-party** (Bitwarden, LastPass, Dashlane, 1Password)

   - to stay portable, the key decrypts into ordinary app memory

**3/5**

protocol /  auth ·  transport ·  client ·  relying party · **SYNC** ·  user

## Slide 88

**90**

### **The account still falls the old ways**

Spensky, DEF CON 33 (sync-fabric phishing PoC)

- SIM swap, ~19% of passkey account-takeover correlated (↗ <u>Prove)</u>

- Phish the login, drive a real browser as them, walk out with the passkeys (↗ <u>Spensky, DEF CON 33)</u>

- Or go deeper: VaultJacking phishes the vault PIN for the master key, decrypting every synced passkey at once (↗ <u>Brazzell, 2026)</u>

**4/5**

protocol /  auth ·  transport ·  client ·  relying party · **SYNC** ·  user

## Slide 89

**91**

### **Decoy passkeys**

- <u>↗ CASPER (Islam et al., USENIX Security 2025)</u>

   - Hides the real passkey among indistinguishable decoys

   - a key stolen from a cloud breach trips a decoy at login

   - <u>so</u> the RP detects the theft.

   - Detection, not prevention.

- <u>↗ Bicakci et al. (2026)</u>

   - Syncs only REAL ciphertext

   - the decryption key stays in the user's hardware token

   - the cloud is never trusted

   - Prevention, not detection

**5/5**

protocol /  auth ·  transport ·  client ·  relying party · **SYNC** ·  user

## Slide 90

**6. User and recovery**

## Slide 91

### **You are here**

**93**

**1/6** protocol /  auth ·  transport ·  client ·  relying party ·  sync · **USER**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
You are here
AV
1. AUTHENTICATOR /
PROTOCOL
————|> | __ 2. Hybrid TRANSPORT
6. USER RECOVERY
5. CLOUD SYNC
Engagement
protocol
3. CLIENT
4. RELYING PARTY
4/6
auth - transport - client - relying party - sync - USER
93
```

## Slide 92

### **Weaker ways in**

- SMS

- email links

- security questions

- lost device flows

- helpdesk

- OAuth device-code

**2/6 94** protocol /  auth ·  transport ·  client ·  relying party ·  sync · **USER**

## Slide 93

### **Government says it plainly**

Source: UK NCSC, Traditional and FIDO2 credentials for personal use (2026). ↗ <u>ncsc.gov.uk</u>

**3/6**

**95**

protocol /  auth ·  transport ·  client ·  relying party ·  sync · **USER**

## Slide 94

### **AiTM still works**

- <u>Push Security (2025)</u> named the class: an AiTM kit **rewrites the method-selection page** , so "passkey OR backup code" becomes just "backup code."

- <u>IOActive (2026)</u> weaponized it on Cloudflare Workers: flip the FIDO2 isDefault, or **CSS-hide the passkey** .

**4/6**

**96**

protocol /  auth ·  transport ·  client ·  relying party ·  sync · **USER**

## Slide 95

### **When the attacker is already inside**

- **<u>↗ Dafalla et al. (USENIX Security 2025)f</u>**

   - assume the attacker is **someone in your life**

   - An intimate partner, a family member

- **User** verification, not **owner** verification

   - FIDO2 never binds a passkey to the biometric that enrolled it

**5/6**

protocol /  auth ·  transport ·  client ·  relying party ·  sync · **USER**

**97**

## Slide 96

### **Abuse scenario**

1. Alex **shares** their phone **PIN** with Billy.

2. One bathroom break later:

   - a. Billy **AirDrops** Alex's TikTok passkey to his own iPhone

   - b. **reads** every message.

3. Alex gets suspicious, **resets the password** , **enrolls** a new passkey.

4. It changes nothing.

**6/6**

protocol /  auth ·  transport ·  client ·  relying party ·  sync · **USER**

**98**

## Slide 97

**Close**

## Slide 98

**Passkeys didn't remove the attack surface. They moved it.**

**100**

## Slide 99

### **Questions?**

- Mail: **matteo.giordano@anvilsecure.com**

- LinkedIn: **linkedin.com/in/giordanomatteo/**

- Website: **matteogiordano.im**

- GitHub: **github.com/anvilsecure/passkey-editor**

- Blogposts:

   - **anvilsecure.com/blog/demystifying-passkeys-under-the-hood-the-protocol.html**

   - **anvilsecure.com/blog/demystifying-passkeys-under-the-hood-the-architecture.html**

   - **anvilsecure.com/blog/demystifying-passkeys-under-attack.html**

**101**

## Slide 100

**Beyond the Ceremony.**
