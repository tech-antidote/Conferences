---
title: "Passkeys Pwned Turning WebAuthn Against Itself"
speakers: ["Shourya Pratap Singh Jonny Lin Daniel Seetoh"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33/Shourya Pratap Singh Jonny Lin Daniel Seetoh - Passkeys Pwned Turning WebAuthn Against Itself.pdf"
pages: 44
sha256: "1f5acfb5ac95cd021797832fc2102daa78a2958c8acab9e34a6c7d5c416f0c13"
text_chars: 12149
ocr_pages: 7
has_ocr: true
redacted_secrets: 0
ocr_confidence: 90.3
ocr_unreliable_blocks: 1
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T07:13:50Z"
---
# Passkeys Pwned Turning WebAuthn Against Itself

**Speakers:** Shourya Pratap Singh Jonny Lin Daniel Seetoh  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33/Shourya Pratap Singh Jonny Lin Daniel Seetoh - Passkeys Pwned Turning WebAuthn Against Itself.pdf` (44 pages)


## Slide 1

Passkeys Pwned: Turning WebAuthn Against Itself Shourya Pratap Singh, Jonny Lin, Daniel Seetoh

## Slide 2

## About us

**Shourya Pratap Singh**

_Principal Software Engineer_

### **Jonny Lin**

_Frontend Engineer_

**Daniel Seetoh** _Senior Frontend Engineer_

**sqrx.com**

## Slide 3

## About us

#### Webmail Link-File Scanners

#### Google MV3 Vulnerabilities

#### Polymorphic Extensions

#### SWGs are Broken

#### OAuth Abuse to Hijack Extensions

#### Browser & Device Takeover via Extension

Browser-native Ransomware

**sqrx.com**

## Slide 4

## Rapid adoption of Passkeys

Created with ChatGPT

**sqrx.com**

## Slide 5

## Rapid adoption of Passkeys

<u>https://www.cnet.com/tech/microsoft-will-erase-your-passwords-in-2-weeks-what-to-do-now/ https://www.forbes.com/sites/zakdoffman/2025/06/08/google-confirms-almost-all-gmail-usersmust-upgrade-accounts/ https://www.androidpolice.com/google-passkeys-data-faster-dependable-future/ https://github.blog/security/supply-chain-security/securing-millions-of-developers-through-2fa/</u> **sqrx.com**

## Slide 6

## Why Passkeys?

WebAuthn uses asymmetric (public-key) cryptography. This has some benefits:

- Protection against phishing (signature changes based on origin)

- Not guessable (can’t brute force a digital signature easily like passwords)

- Reduced impact of data breach (nothing secret like private key is sent to servers)

**sqrx.com**

## Slide 7

## Passkeys and WebAuthn

- The implementation of passkeys relies on a set of standard specifications known as **FIDO 2** .

- **WebAuthn** is one of the FIDO 2 specifications that enables passkey support in browsers.

- Thanks to WebAuthn, the browser mediates access to authenticators where the user's passkeys are stored.

**sqrx.com**

## Slide 8

## The Password is Dead. Is the Replacement Ready?

- Passkeys = phishing-resistant, invulnerable to guesses, and… **misunderstood**

- Most sites treat WebAuthn as a magic box — but it’s still JS

- We’ll show how attackers can exploit the trust boundary in the browser

Created with ChatGPT

**sqrx.com**

## Slide 9

## WebAuthn 101

- Overall Flow

   - Registration Flow

   - ○ Authentication Flow

- Involved Parties

   - User

   - Authenticator

   - Client

   - Relying Party

**sqrx.com**

Source: https://developer.mozilla.org/en-US/docs/Web/API/Web_Authentication_API

## Slide 10

## WebAuthn 101 – Registration Flow

**sqrx.com**

Created with Mermaid Chart


> Recovered by OCR — confidence 93/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
WebAuthn 101 - Registration Flow
User (Device/Browser)
Browser/Client App Server (Backend)
Clicks "Create a passkey"
navigator.credentials.create(options)
Request new credential creation
Return credentials
Iv
"Device registered successfully!”
(Device/Browser)
Browser/Client App Server (Backend)
```

## Slide 11

## WebAuthn 101 – Registration Flow

User starts by clicking on “Create
a passkey” on a website

**sqrx.com**

Created with Mermaid Chart


> Recovered by OCR — confidence 92/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
WebAuthn 101 - Registration Flow
(Device/Browser) Browser/Client App Server (Backend)
| Clicks "Create a passkey"
User starts by clicking on “Create
a passkey” on a website
tion
Return credentials
Iv
"Device registered successfully!”
(Device/Browser)
Browser/Client App Server (Backend)
```

## Slide 12

## WebAuthn 101 – Registration Flow

Server responds with
challenge and additional
information for public key
credential creation
sqrx.com

sqrx.com

Created with Mermaid Chart

## Slide 13

## WebAuthn 101 – Registration Flow

The browser calls
navigator.credentials.create
triggering the authenticator to generate a
new key pair

**sqrx.com**

Created with Mermaid Chart

## Slide 14

## WebAuthn 101 – Registration Flow

Authenticator prompts for biometrics/PIN, generates a new key pair, stores the private key, and returns fields including

- Credential ID

- Attestation Object

   - Public Key

   - Counter

   - Flags

**sqrx.com**

Created with Mermaid Chart

## Slide 15

## WebAuthn 101 – Registration Flow

The call to navigator.credentials.create returns PublicKeyCredential

- id => b64url-encoded credential ID

- ● rawId => ArrayBuffer of credential ID ● type => “public-key” ● getClientExtensionResults => returns results of extensions requested by the server

- response => AuthenticatorAttestationResponse

   - attestationObject => CBOR-encoded of ■ fmt => format ■ authData => ArrayBuffer of ● rpIdHash ● flags ● signCount ● aaguid

         - credIdLength

         - credId

         - coseKey

      - attStmt => attestation signature and certs

   - clientDataJSON => ArrayBuffer of client data

   - getTransports => method that returns authenticator transport mechanisms

   - ○ … additional fields/methods

**sqrx.com**

Created with Mermaid Chart

## Slide 16

## WebAuthn 101 – Registration Flow

The server verifies
registration data, and
stores the public key
and other data
sqrx.com
Created with Mermaid Chart

Created with Mermaid Chart

## Slide 17

## WebAuthn 101 – Authentication Flow

**sqrx.com**

Created with Mermaid Chart


> Recovered by OCR — confidence 90/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
WebAuthn 101 - Authentication Flow
User (Devine Biearser) Browser/Client App Server (Backend)
Clicks "Sign in hes a passkey"
Request authentication options
<
navigator.credentials.get(options)
Request assertion with credentials
Return assertion data
Encode assertion data
Send authentication data
Authentication successful V
jion/JWT toke
Authenticator Browser/Client App Server (Backend)
```

## Slide 18

## WebAuthn 101 – Authentication Flow

User starts by clicking on “Sign in
with a passkey” on a website

**sqrx.com**

Created with Mermaid Chart

## Slide 19

## WebAuthn 101 – Authentication Flow

Server responds with
challenge and additional
information for public key
credential request

sqrx.com

Created with Mermaid Chart

## Slide 20

## WebAuthn 101 – Authentication Flow

The browser calls
navigator.credentials.get
triggering the authenticator to retrieve and use
existing credentials for authentication

Created with Mermaid Chart

**sqrx.com**

## Slide 21

## WebAuthn 101 – Authentication Flow

Authenticator prompts for biometrics/PIN, retrieves the private key, increments the counter, creates authenticator data, and signs the data

**sqrx.com**

Created with Mermaid Chart

## Slide 22

## WebAuthn 101 – Authentication Flow

The call to navigator.credentials.get
returns PublicKeyCredential
● id => b64url-encoded credential ID
● rawId => ArrayBuffer of credential ID
● type => “public-key”
● getClientExtensionResults => returns results of
extensions requested by the server
● response => AuthenticatorAssertionResponse
○ clientDataJSON => ArrayBuffer of client
data
○ authenticatorData => ArrayBuffer of
rpIdHash/flags/signCount/extensions
○ signature => ArrayBuffer of signature
over (authData + clientDataHash)
○ userHandle => ArrayBuffer of user ID or
null
○ … additional fields/methods

**sqrx.com**

Created with Mermaid Chart

## Slide 23

## WebAuthn 101 – Authentication Flow

The server verifies
authentication data, and
handles logging in the
user
sqrx.com

Created with Mermaid Chart

## Slide 24

Authenticator Attestation Global Unique Identifier


> Recovered by OCR — confidence 85/100 on the text kept, 81/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
passkeydeveloper.github.io/passkey-authenticator-aaguids/explorer/
Passkeys Authenticator AAGUID Explorer
Authenticator Attestation Global Unique Identifier
Include MDS authenticators
AAGUID
Filter by name. x
Icon light
ea9b8d66-4d01-1d21-3ce4-b6b48cb575d4
Google Password Manager
On
Chrome on Mac
Windows Hello
9ddd1817-af5a-4672-a2b9-3e3dd95000a9 | Windows Hello
6028b017-b1d4-4c02-b4b3-afcdafe96bb2 | Windows Hello
dd4ec289-e01d-41c9-bb89-70fa845d4bi2_| iCloud Keychain (Managed)
531126d6-6717-415c-9320-3d9aa6981239 | Dashlane
bada5566-a7aa-401f-bd96-45619a55120d | 1Password
b84e4048-15dc-4dd0-8640-14160813c8af_ | NordPass
Icon dark
```

## Slide 25

## Security Properties of WebAuthn

- Designed to be strong:

   - Public key cryptography

   - Private keys stored securely (secure enclave)

   - ○ Credentials bound to origin (anti-phishing)

   - User verification (Touch ID, Face ID)

   - Optionally attested (the authenticator can prove its model identity)

**sqrx.com**

## Slide 26

## Where Does Trust Live?

Created with ChatGPT

**sqrx.com**

## Slide 27

## Browser = Trust Anchor

- **Browser** enforces origin binding, user verification, challenge integrity

- Authenticator never sees app logic — relies on **browser** mediation

- The server validates the cryptographic result — but not how the **browser** produced that result

Created with Gemini

**sqrx.com**

## Slide 28

## Browser = Trust Anchor

Created with ChatGPT

**sqrx.com**


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Browser = Trust Anchor
WHAT IF
YOUR
YU Y BROWSER
IS LYING
TO YOU?
```

## Slide 29

## Injection Pathways

- Client side lacks a secure channel from the web app to the authenticator

   - MITB (“Man in the Browser”)

   - Injected code replaces Credentials API

- “Malicious” Browser Extension

   - Our extension hooks the Credentials API functions by overwriting **navigator.credentials.create** and **.get**

- Alternate Vectors - XSS and Friends

**sqrx.com**

## Slide 30

## The Attack Flow - Fake Registration

**sqrx.com**

Created with Mermaid Chart


> Recovered by OCR — confidence 90/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
The Attack Flow - Fake Registration
User (Device/Browser) Malicious Extension Browser/Client App Server (Backend)
Clicks "Create a passkey"|
navigator.credentials.create(options)
Fake credentials
>
Registration successful ¥
“Device registered successt
User (DevicgiBrenser) Browser/Client App Server (Backend)
```

## Slide 31

## The Attack Flow - Fake Registration

Malicious extension proxies
navigator.credentials.create
and generates the key pair, creates
the attestation object, and stores the
following fields per passkey:
- Credential ID
-
Private Key
- Counter
- Hostname
- User ID

**sqrx.com**

Created with Mermaid Chart

## Slide 32

## The Attack Flow - Forging Authentication

**sqrx.com**

Created with Mermaid Chart


> Recovered by OCR — confidence 93/100 on the text kept, 60/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
The Attack Flow - Forging Authentication
Clicks "Sign in with a passkey
Request authentication options
PublicKeyCredentialRequestOptions
navigator.credentials.get(options)
Forged signature
Send authentication data
Authentication successful ¥
(Set session/JWT token)
User Coon Malicious Extension Browser/Client App Server (Backend)
```

## Slide 33

## The Attack Flow - Forging Authentication

Malicious extension proxies
navigator.credentials.get
and retrieves the private key from
storage, increments the counter,
signs the challenge, and returns
the forged response to the server

**sqrx.com**

Created with Mermaid Chart

## Slide 34

[Demo]

## Slide 35

## Would the user be suspicious?

- The “Silent Mode”

- We can still invoke the original function, just don’t use it

- User sees legit flow: “It asked for Touch ID, must be real!”

**sqrx.com**

## Slide 36

[Demo]

## Slide 37

## But What If They’re Already Registered?

- **Fail the login intentionally** Let navigator.credentials.get() fail silently or spoof an error

- **Trigger password fallback intentionally** Spoof WebAuthn login failure → site falls back to username/password/ Then attacker steals the password via keylogging or phishing

- **Force re-registration**

Redirect user to passkey enrollment flow. As an extension can do this using chrome.tabs.update({ url: "https://account.google.com/" })

- **Phishing-style UI nudges** Inject a fake banner: “Your passkey has expired. [Click here to reset]”

**sqrx.com**

## Slide 38

[Demo]

## Slide 39

## Sharing is Caring

- Instead of just saving the passkey data locally, we can **send it to an attacker's API endpoint**

- The **attacker’s browser extension** fetches this data from the API and reconstructs the credential

- The **passkey is replayed** on the attacker's browser to authenticate as the victim

**sqrx.com**

## Slide 40

[Demo]

## Slide 41

Fixing It (or Trying To)

- Enforce a strict Content Security Policy (CSP)

- Validate x5c certificate chains and AAGUIDs using FIDO Metadata (MDS)

- Monitor and alert on unusual passkey usage patterns

- Trigger step-up MFA for:

   - New devices

   - Unfamiliar locations

   - Behavioral anomalies (e.g., timing, IP, device fingerprint)

- Lock the Client Side

**sqrx.com**

## Slide 42

For Websites: Don’t just detect XSS — prevent it from running

- Enforce a strict **Content Security Policy (CSP)**

Example: Block unsafe-inline, disallow eval()

- Enable **Trusted Types** to prevent DOM-based XSS

Example: Sanitize DOM sinks using Trusted Types

**sqrx.com**

## Slide 43

## For Users & Admins: Hardening the Browser

- Audit browser extensions

- Use browser-level security tools: ○ Chrome Enterprise / Microsoft Edge management (e.g., force-install or blocklist extensions)

- ○ Firefox ESR with admin policy templates

- Browser Security Extensions

**The browser is the new OS. Treat it like one**

**sqrx.com**

## Slide 44

# **Thank You!**

**sqrx.com sqrx.com**

**© 2024 SquareX Inc**
