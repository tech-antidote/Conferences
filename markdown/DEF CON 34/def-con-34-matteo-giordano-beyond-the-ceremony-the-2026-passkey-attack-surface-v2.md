---
title: "Beyond the Ceremony The 2026 Passkey Attack Surface"
speakers: ["Matteo Giordano"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: 2026
source_pdf: "DEF CON 34/DEF CON 34 - Matteo Giordano - Beyond the Ceremony The 2026 Passkey Attack Surface - v2.pdf"
pages: 100
sha256: "6e80a68dc4aa61a0e0fa1e3592941484c14766bab04abff73b2e68d265423f66"
text_chars: 45053
ocr_pages: 43
has_ocr: true
redacted_secrets: 0
ocr_confidence: 86.5
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:41:37Z"
---
# Beyond the Ceremony The 2026 Passkey Attack Surface

**Speakers:** Matteo Giordano  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Matteo Giordano - Beyond the Ceremony The 2026 Passkey Attack Surface - v2.pdf` (100 pages)


## Slide 1

## Beyond the Ceremony **The 2026 Passkey Attack Surface**

Matteo Giordano


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
VIL
SECURE
Beyond the Ceremony
The 2026 Passkey Attack Surface
Matteo Giordano
```

## Slide 2

**2**

## Slide 3

**3**

## Slide 4

**4**

## Slide 5

**5**


> Recovered by OCR — confidence 86/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
RP
Public
Client
—
Authenticator
NY preset]
```

## Slide 6

**6**

## Slide 7

**7**


> Recovered by OCR — confidence 89/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Private
On J
rivate
Authenticator n
Client 1
Client 2
Client n
```

## Slide 8

**8**

## Slide 9

**9**

## Slide 10

**10**

## Slide 11

**11**

### **I'm not here with the scariest bug**


> Recovered by OCR — confidence 93/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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
V
ONE MAP
Let's give them a home
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
UserPresence: true,   I'm here
UserVerification: true,   trust me, right?
},
signCount: 0   first DEF CON talk.
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


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
It’s everything else
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


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
What else?
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


> Recovered by OCR — confidence 93/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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
(9) attestationObject,
clientDataJSON
(10) verify as per [1]
and add credentials to
its storage
(5) hash(clientDataJSON),
user info,
RP info, RP ID
(8) attestationObject
(4) clientDataJSON = {
challenge,
RP origin,
"webauthn.create"
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


> Recovered by OCR — confidence 93/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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
Wu
(9) authenticatorData +
signature +
clientDataJSON
(10) verify as per [1]
and add credentials to
its storage
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
(7.1) Signs the
authenticatorData
concatenated with the hash
of the clientDataJSON
```

## Slide 21

**21**

### **Outer layers**


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Outer layers
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


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Our map
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


> Recovered by OCR — confidence 87/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
You are here
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


> Recovered by OCR — confidence 82/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CTAP
Client
B R
O
A
U W
R
NY
USB /NFC/ BLE
Authenticator
a rivate
as ivate
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


> Recovered by OCR — confidence 93/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
You are here
1. AUTHENTICATOR /
PROTOCOL
——|_2. Hybrid TRANSPORT
6. USER RECOVERY
5. CLOUD SYNC
Engagement
protocol
3. CLIENT
4. RELYING PARTY
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


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Co-location vs intent
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


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
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


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
You are here
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


> Recovered by OCR — confidence 86/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
You are here
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

\```
mysignins.microsoft.com
\```

\```
POST /api/post/newfido
Content-Type: form-urlencoded
\```

\```
canary=b0f2c1a9 
\```

- `&clientDataJson=eyJ0eXBlIjo `

- `&attestationObject=o2NmbXRkcG `

- `&credentialId=3EHSf9K2mQ  &credentialDeviceType=multiDevice &credentialBackedUp=true &transports=internal,hybrid`

- `&extensions=eyJjcmVkUHJv `

###### **GitHub**

\```
github.com
\```

\```
POST /u2f/trusted_devices
Content-Type: multipart/form-data
\```

\```
------WebKitFormBoundary 
Content-Disposition: form-data;
name="response"
\```

\```
{"id":"3EHSf9K2mQ ",
\```

- `"type":"public-key",`

\```
"response":{
\```

- `"clientDataJSON":"eyJ0 `

- `"attestationObject":"o2N `

\```
},
\```

\```
"clientExtensionResults":{}}
\```

###### **Google**

\```
myaccount.google.com
\```

\```
POST /_/ /batchexecute
Content-Type: form-urlencoded
\```

\```
f.req=[[["GtmsU","[null,null,
null,"eyJ0eXBlIjoi ",
\```

\```
"o2NmbXRkcGFj ",
["internal"],null,1,1]",
null,"generic"]]]
\```

- `&at=AFehe7k9dQ `

- `  idx 3 = clientDataJSON`

- `  idx 4 = attestationObject`

\```
------WebKitFormBoundary --
\```

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

\```
{
\```

- `"clientDataJSON": {`

- `"type": "webauthn.get",`

You want:

- `"challenge": "zYJx-8mHw8wK7vC4qRseSJrDCd01yKIfZk_njXEOoeuQD7CuKUoQ2frvV0NBoJiVZSBgjUYy8vGb-0Lq-BS1wA",`

- `"origin": "https: webauthn.io",`

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


> Recovered by OCR — confidence 81/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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
Enabled [_] Auto-plant ["] Auto re-sign
id: webauthn.io name: webauthn.io (Duo py_webauthn)
host match: EXACT ~ webauthn.io
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
signature © path © regex response.response.signature © Auto © Raw ©) Base64 (©) Base64URL [| URL encoded £d25519 - 64B decoded >
userHandle © path © regex | response.response.userHandle © Auto © Raw ©) Base64 () Base64URL [] URL encoded 37B - “webauthnio-asdadsada..." decoded >
credentialld © path © regex | response.rawld © Auto © Raw ©) Base64 () Base64URL [| URL encoded 328 - 893025b4e178... decoded >
Sample bodies
Registration body (paste the reg-verify request body):
{
“defcon34",
{
Authentication body (paste the auth-verify request body):
Check Prettify JSON Save profile all 8 configured field(s) extract cleanly
7/37
protocol / auth - transport - client - RELYING PARTY . sync - user
55
```

## Slide 56

**56**

**8/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
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


> Recovered by OCR — confidence 84/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
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


> Recovered by OCR — confidence 77/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Registration
verify URL: CONTAINS v__ /registration/verification method: POST
clientDataJSON © path ©) regex response.response.clientDataJSON }
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


> Recovered by OCR — confidence 77/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Authentication
verify URL: CONTAINS v __ /authentication/verification method: POST
clientDataJSON O path ©) regex response.response.clientDataJSON (e)
authenticatorData O path ©) regex response.response.authenticatorData (eo)
signature O path ©) regex response.response.signature (e]
userHandle O path ©) regex response.response.userHandle (e]
credentialld O path ©) regex response.rawld
Sample bodies ra]
protocol / auth - transport - client - RELYING PARTY . sync - user
59
```

## Slide 60

**60**

**12/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user


> Recovered by OCR — confidence 71/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
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


> Recovered by OCR — confidence 77/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
‘Sample bodies
Registration
verify URL: CONTAINS v __ /registration/verification method: POST
clientDataJSON O path ©) regex | response.response.clientDataJSON O Auto (© Raw ©) Base64 (©) Base64URL [ | URL encoded]webauthn.create decoded >
attestationObject O path © regex | response.response.attestationObject O Auto © Raw ©) Base64 (©) Base64URL [ | URL encoded} fmt=none - Ed25519 key decoded >
authenticatorData O path ©) regex response.response.authenticatorData O Auto © Raw ©) Base64 (©) Base64URL [ | URL encoded} UP UV AT: signCount 1 decoded >
credentialld O path © regex O Auto © Raw © Base64 () Base64URL [) URLencoded| decoded >
Authentication
verify URL: CONTAINS y¥ /authentication/verification method: POST
clientDataJSON O path ©) regex | response.response.clientDataJSON O Auto © Raw ©) Base64 (©) Base64URL [| URL encoded} webauthn.get decoded >
authenticatorData © path © regex response.response.authenticatorData © Auto © Raw ©) Base64 () Base64URL [| URL encoded} UP UV - signCount 2 decoded >
signature O path © regex | response.response.signature O Auto © Raw ©) Base64 (©) Base64URL [| URL encoded} Ed25519 - 64B decoded > (10 }
userHandle O path © regex response.response.userHandle O Auto © Raw (©) Base64 () Base64URL [ | URL encoded} 37B - “webauthnio-asdadsada..." decoded >
O path ©) regex | response.rawld © Auto © Raw ©) Base64 () Base64URL [| URL encoded} 32B - 893025b4e178... decoded >
Registration body (paste the reg-verify request body):
{
“username": "“defcon34",
{
“response": {
“attestationObject": “o2NmbXRkbm9uZWdhdHRTdG1@0GhhdXRoRGFOYViBdKbqkhPJnC90siSSsyDPQCYq LMGpUKAS f yk LC2CEHVBFAAAAAQECAwQFBgc IAQ IDBAUGBwgAIIkwJ bTheLJwnsyC9RTaHJ aNMNxM—Lw5C@CJMa6 LEbTEpA
Authentication body (paste the auth-verify request body):
{
“authenticatorData": "“dKbqkhPJnC90siSSsyDPQCYq LMGpUKAS fyk LC2CEHVAFAAAAAG",
Check Prettify JSON Save profile all 8 configured field(s) extract cleanly
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


> Recovered by OCR — confidence 90/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Relying Party '
SERVER Client Authenticator
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
(9) attestationObject,
clientDataJSON
“Au
<— forged ——
(10) verify as per [1]
and add credentials to
its storage
1,
LS credential ID,
public Key in CBOR,
AAGUID,
initial sig counter,
extensions
Plant new key
Resign w/ new key
(4) clientDataJSON = {
challenge,
RP origin,
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


> Recovered by OCR — confidence 82/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
challenge
Pretty Raw Hex Passkey Editor R Swe
{
"clientDataJSON": {
"challenge": "evil_challenge",
"origin": "https://webauthn. io",
“crossOrigin": false,
“other_keys_can_be_added_here": "do not compare clientDataJSON against a template.
See https://goo.gl/yabPex"
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
"signature":
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


> Recovered by OCR — confidence 84/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
origin + rpldHash
Pretty Raw Hex Passkey Editor
{
“clientDataJSON": {
“challenge”:
“crossOrigin": false,
“other_keys_can_be_added_here": "do not compare clientDataJSON against a template.
See https://goo.gl/yabPex"
“authenticatorData": {
“rpIdHash": "74AGEA9213C99C2F74B22492B320CF40262A94C1A950A0397F29250B60841EFO",
“signCount": 2,
"flags": {
“userPresent": true,
“userVerified": true,
“backupEligible": false,
“backupState": false,
“attestedCredentialData": false,
“extensionDataIncluded": false
“attestedCredentialData": {}
},
origin
Pretty Raw Hex Passkey Editor
Attacks ~ @ Wrap
{
“clientDataJSON": {
"type": "webauthn.get",
“crossOrigin": false
“authenticatorData": {
"extensions": {},
“signCount": 2,
"flags": {
“userPresent": true,
“userVerified": true,
“backupEligible": false,
“backupState": false,
“attestedCredentialData": false,
“extensionDataIncluded": false
“attestedCredentialData": {}
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


> Recovered by OCR — confidence 86/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Over-scoping the RPid
rpld = example.com
(but only app.example.com valid for *.example.com |——>] customerl.example.com —forges>} customer2.example.com
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


> Recovered by OCR — confidence 88/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Dangling Allowlist Domain
/well-known/webauthn
allowlist
(a.com, b.com, patner.com)
partner.com LAPSES
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


> Recovered by OCR — confidence 89/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ATTESTATION OBJECT
AUTHENTICATOR DATA
32 bytes 1 byte 4 bytes (big-endian uint32) variable length variable length if present (CBOR)
RP ID hash FLAGS COUNTER ATTESTED CRED. DATA EXTENSIONS
If Basic or Privacy CA:
If ECDAA:
UV
1
O UP
14
7
AAGUID
L (CREDENTIAL ID
CREDENTIAL PUBLIC KEY
16 bytes
2 bytes LENGTH L
(variable length)
ATTESTATION STATEMENT (in "packed" attestation statement format)
“ecdaaKeyld*: ...
protocol / auth - transport - client - RELYING PARTY - sync -
variable length (COSE_Key)
23/37
user
```

## Slide 72

**72**

**24/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user


> Recovered by OCR — confidence 80/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ATTESTATION OBJECT
“authData™: ...
i AUTHENTICATOR DATA
i 32 bytes 1 byte 4 bytes (big-endian uint32) variable length variable length if present (CBOR)
RP ID hash FLAGS COUNTER ATTESTED CRED. DATA EXTENSIONS
Po utnentication
' AAGUID L |CREDENTIAL ID | CREDENTIAL PUBLIC KEY
i 16 bytes 2bytes LENGTHL variable length (COSE_Key)
H (variable length)
ATTESTATION STATEMENT (in "packed" attestation statement format)
If Basic or Privacy CA: “alg: ... “sig: ... “xSe"s o.
24/37
protocol / auth - transport - client - RELYING PARTY . sync - user
72
```

## Slide 73

**73**

**25/37**

protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user


> Recovered by OCR — confidence 85/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ATTESTATION OBJECT
i
i AUTHENTICATOR DATA
i 32 bytes 1 byte 4 bytes (big-endian uint32) variable length variable length if present (CBOR)
RP ID hash FLAGS COUNTER ATTESTED CRED. DATA EXTENSIONS
7
AAGUID L_ |CREDENTIAL ID | CREDENTIAL PUBLIC KEY
16 bytes 2 bytes LENGTH L variable length (COSE_Key)
(variable length)
ATTESTATION STATEMENT (in "packed" attestation statement format)
If Basic or Privacy CA: “alg*: ... “sig: ... “xSe":
25/37
protocol / auth - transport - client - RELYING PARTY . sync - user
```

## Slide 74

**74**

### **signature**

**26/37** protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user


> Recovered by OCR — confidence 83/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
signature
Pretty Raw Hex Passkey Editor R Swe
Attacks + Wrap
{
"clientDataJSON": {
“crossOrigin": false
“authenticatorData": {
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


> Recovered by OCR — confidence 82/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
alg
Pretty Raw Hex Passkey Editor R Swe
Attacks ~ Wrap
Signing algorithm: RS256 (-257) ~ |Attestation: None v [266 key planted]
{
"clientDataJSON": {
“origin”: "https://webauthn. io",
“crossOrigin": false
},
“attestationObject": {
“attestationStatement": {
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
“attestedCredentialData": {
“aaguid": "01020304-0506-0708-0102-030405060708",
cosekey
4D4729386160C39FC12B660B611765B9C45BC9E9ED548110766221D9C42906A2273CAEF2143010001"
+
},
“fmt":
}
protocol / auth - transport - client - RELYING PARTY . sync - user
27/37
75
```

## Slide 76

**77**

### **credentialId**

**29/37** protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user


> Recovered by OCR — confidence 81/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
credentialld
Pretty Raw Hex Passkey Editor & 5 in
Attacks + Wrap
Signing algorithm: RS256 (-257) - Attestation: None v RS256 key planted
{
"clientDataJSON": {
"type": "webauthn.create",
“crossOrigin": false
},
“attestationObject": {
“attestationStatement": {
},
“authenticatorData": {
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
“coseKey": {
"keyType": "RSA",
"algorithm": "RS256",
"raw":
“credentialId": "7AF8A5FDCADE7627" |
}
},
“fmt": "none"
29/37
protocol / auth - transport - client - RELYING PARTY . sync -
user
77
```

## Slide 77

**78**

### **signCount**

**30/37** protocol /  auth ·  transport ·  client · **RELYING PARTY** ·  sync ·  user


> Recovered by OCR — confidence 80/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
signCount
Pretty Raw Hex Passkey Editor Q 5s i=
RP evil Auth
Attacks Wrap
“clientDataJSON": {
13 13 “type": "webauthn.get",
“challenge”:
15 “crossOrigin": false
15 “authenticatorData": {
18 1 “rpIdHash": "74A6EA9213C99C2F74B22492B320CF40262A94C1A950A0397F29250B60841EF0",
S "extensions":
“signCount": 13333337,
x "flags": {
“userPresent": true,
“userVerified": true,
“backupState": false,
“attestedCredentialData": false,
“extensionDataIncluded": false
2 O “signature” :
21 }
30/37
AV protocol / auth - transport - client - RELYING PARTY . sync - user
```

## Slide 78


> Recovered by OCR — confidence 80/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
WebAuthn.io
A demo of the WebAuthn specification
hk
Register Authenticate
Advanced Settings
ik {0 Elements Console Application WebAuthnX Sources >> @ 8 2 xX
Enable virtual authenticator environment
7 Authenticator 90e32 @ active Remove
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
YPb8Sn4QxH3", DEM O #1
KE@TXhiSFVGRj J LZG1wbnVMYUg2b2RNaVRSczZJSnZ4aEFNc
3IFFIQZFPGR_LkyChiNXtpCBb1g9vxKfhDEfc", Pla nt
1C2CFHVRFAAAAAOAAAAAAAAAAAAAAAAAAAAAATND 51n7.1Z Re = S | g n
toy
@ Memory: 194.7MB of 8.00GB
```

## Slide 79


> Recovered by OCR — confidence 85/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
webauthn.io
WebAuthn.io
A demo of the WebAu
example_username
Register
Advanced Settings
[0 Elements Console Application WebAut
Enable virtual authenticator environment
@ Authenticator b05e4
Protocol ctap2
Transport internal
Supports resident keys Yes
Supports large blob No
Supports user verification Yes
Supports hmac-secret No
Supports hmac-secret-mc No
Credentials
No credentials. Try calling navigator.cre¢
New authenticator
Target Proxy Repeater Extensions
Passkey Editor
Profiles Guide About
Passkey Editor
Burp Suite Professional v2026.6 - 2026-06-21 - licensed to Anvil Ventures, Inc
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
default signing alg: EdDSA(-8) - _ plant attestation: None v
Registration
verify URL: CONTAINS v /registration/verification method: POST
clientDataJSON © path regex response.response.clientDataJSON © Auto Raw Base64 Base64URL URLencoded decoded »
attestationObject O path regex response.response.attestationObject © Auto Raw Base64 Base64URL URL er »
authenticatorData O path regex response.response.authenticatorData O Auto Raw Base64 Base64URL URL er >
credentialld O path regex O Auto Raw Base64 Base64URL URL encoded decoded »
Authentication
verify URL: CONTAINS ~ /authentication/verification method: POST
clientDataJSON © path regex response.response.clientDataJSON O Auto Raw Base64 Base64URL URL er »
authenticatorData © path regex _response.response.authenticatorData © Auto Raw Base64 Base64URL URL encoded decoded »
signature O path regex response.response.signature O Auto Raw Base64 Base64URL URL encoded decoded >
userHandle © path regex response.response.userHandle O Auto Raw Base64 Base64URL URL encoded decoded >
credentialld O path regex response.rawid O Auto Raw Base64 Base64URL URL er ,
Sample bodies
Registration body (paste the reg-verify request body):
DEMO #1
Authentication body (paste the auth-verify request body):
AUTO
mode
Check Prettify JSON Save profile
@ Memory: 388.6MB of 8.00GB “iv
```

## Slide 80


> Recovered by OCR — confidence 82/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
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
& SSH and GPG keys
@ Credentials
Organizations
® Enterprises
(© Moderation v
Code, planning, and automation
& Codespaces
@ Packages
& Copilot v
& Pages
© Saved replies
Security
Target Proxy Repeater Extensions
Passkey Editor
Profiles Guide About
Profiles
Burp Suite Professional v2026.6 - 2026-06-21 - licensed to Anvil Ventures, Inc
Passkey Editor
Profile: Github
@ Default (SimpleWebAuthn / generic)
© webauthn.io [not active]
@ Github
Add
Copy
Sign i Delete
Restore built-ins
Go
Sig
Ap
Sig
Two-fé
your)
Event log (13) All issues
Enabled
id: github
host match; EXACT v _ github.com
Auto-plant Auto re-sign
name: Github
default signing alg: ES256 (-7) Y plant attestation: None v
Registration
verify URL: CONTAINS v /u2f/trusted_devices method: POST
clientDataJSON path © regex "clientDataJSON":"(**}+)" Auto () Raw ©) Base64 © Base64URL URL er »
attestationObject path © regex "attestationObject":"(*"]+)" Auto Raw Base64 © B B4URL URL er >
authenticatorData © path ©) regex O Ato Raw Base64 B: URL URL er »
credentialld path © regex “rawld*:"((*"}+)" Auto Raw Base64 © S4URL URL er »
Authentication
verify URL: CONTAINS y /session method: POST
clientDataJSON path © regex %22clientDataJSON%22%3A%22(%]+)%22 Auto _) Raw Base64 © Base64URL URL er »
authenticatorData path © regex %22authenticatorData%22%3A%22(" %]}+)%22 Auto Raw Base64 © Base64URL URL encoded decoded >
signature path © regex %22signature%22%3A%22(%]+)%22 Auto (©) Raw ©) Base64 © Base64URL || URL er decoded »
userHandle >) path © regex %22userHandle%22%3A%22((0%]+)%22 Auto () Raw ©) Base64 © Base64URL |) URLencoded decoded >
credentialld © path © regex %22rawld%22%3A%22( %]+)%22 Auto Raw Base64 © Base64URL URL er »
Sample bodies
Registration body (paste the reg-verify request body):
Content-Disposition: form-data; name="authenticity_token"
Authentication body (paste the auth-verify request body):
58bal4eclec961f05384142834180a651a2
Check Prettify JSON Save profile
DEMO #2
Attack the
Registration
@ Memory: 350.1MB of 8.00GB “ov
```

## Slide 81


> Recovered by OCR — confidence 85/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Burp Suite Prof ional v2026.6 - 2026-06-21 - licensed to Anvil Ventures, inc
ce © Proxy settings
O Drop ® Open browser (Q) :
Sign in to GitHub
Username or email address
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


> Recovered by OCR — confidence 91/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
You are here
1. AUTHENTICATOR /
PROTOCOL
———|>|_ 2. Hybrid TRANSPORT
6. USER RECOVERY
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


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Types of Passkeys
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


> Recovered by OCR — confidence 93/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
You are here
1. AUTHENTICATOR /
PROTOCOL
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
