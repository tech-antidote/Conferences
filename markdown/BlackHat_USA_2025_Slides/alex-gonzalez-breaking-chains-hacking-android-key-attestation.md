---
title: "Breaking Chains Hacking Android Key Attestation"
speakers: ["Alex Gonzalez"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Alex Gonzalez_Breaking Chains Hacking Android Key Attestation.pdf"
pages: 34
sha256: "05461e5459c4b16c6fdf8b7881460118455f9bce5e28bf314d98e48a70f02541"
text_chars: 13066
ocr_pages: 6
has_ocr: true
redacted_secrets: 0
ocr_confidence: 91.4
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:03:24Z"
---
# Breaking Chains Hacking Android Key Attestation

**Speakers:** Alex Gonzalez  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Alex Gonzalez_Breaking Chains Hacking Android Key Attestation.pdf` (34 pages)


## Slide 1

# Breaking Chains: Hacking Android Key Attestation

Alex Gonzalez

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
AUGUST 6-7, 2025
MANDALAY BAY / LAS VEGAS
Breaking Chains: Hacking Android Key
Attestation
Alex Gonzalez
```

## Slide 2

## Introduction

#### **Alex Gonzalez**

Senior Red Team Engineer dubfr33/dubfree dubfr33 linkedin/in/alex-gonzalez-63b01426b

#BHUSA @BlackHatEvents

## Slide 3

## Agenda

Background Android Key Attestation Bot Fraud/Abuse Use Case Common PKI Issues Certificate Extension PKI Issue Root Cause Analysis Closing Remarks

#BHUSA @BlackHatEvents

## Slide 4

## Background

- Targeting a service with a bot fraud/abuse problem

   - Bot service providers operating in various cloud service providers

   - Automating API calls to beat out legitimate users

- Implemented app and key attestation

   - Means to attest traffic sources from a physical device

- Initial disruption but lead to bot TTP shift

   - Introduction of the 0-day market

- FraudSec campaign objectives

   - Emulate bot service provider

#BHUSA @BlackHatEvents

## Slide 5

## Android Key Attestation

- App Attestation !== Key Attestation

- App Attestation (SafetyNet/Play Integrity)

   - Establishes a mobile apps integrity

      - Signed/Official App Store version

      - Rooted device/bootloader checks

      - Hooking/Swizzling checks

      - Calls a Google API to retrieve a verdict (JWT)

- Key Attestation

   - Verifies that a key is stored in secure hardware

      - Ensures keys can’t be extracted from the device (Android Keystore)

      - Calls an Android OS API to retrieve verdict (PKI/X.509 certificates)

#BHUSA @BlackHatEvents

## Slide 6

## Android Keystore

- Two types of secure storage

   - Trusted Execution Environment (TEE)

      - Utilizes ARM TrustZone

      - Virtualizes processor to create secure environment

      - Separate OS, kernel driver, userspace lib for IPC

   - Secure Element (SE)

      - Hardware Security Module (HSM)

      - Separate chip typically connected via serial interface

- Two main security protections

   - Prevents key extraction

      - Cryptographic material never leaves secure hardware

   - Key use authorizations

      - Keys are scoped to the app and for specific use cases

Trusty TEE OS Diagram

TEEGRIS OS Diagram #BHUSA @BlackHatEvents

## Slide 7

## Android Key Attestation PKI

- No CA, Google distributes key-pair to manufacturer

- Manufacturer injects key-pair into TEE/SE (keybox)

- Developer utilizes KeyStore API in their app to create key-pair, fetch certificate chain, send certificate chain to their server for validation

- Utilize attested key based on implementation (typically signing sensitive requests)

Key Attestation PKI Diagram

#BHUSA @BlackHatEvents

## Slide 8

## Verifying Hardware-Backed Key Pairs

- Chain of trust

   - Root certificate is signed by Google

   - Each certificate in chain signed by predecessor

- Certificate revocation list

- Extracting attestation extension data

   - OID 1.3.6.1.4.1.11129.2.1.17

- Verifying attestation extension data

   - attestationChallenge (nonce), SecurityLevel, RootOfTrust, VerifiedBootState

- At a high level

   - Validate a X.509 certificate chain

   - Parse custom OID extension and validate metadata

#BHUSA @BlackHatEvents

## Slide 9

## X.509 Certificates

- 3+ X.509 certificates

- Root is signed by Google

   - TEE/SE injected key-pair

- Intermediate certificates

   - Contains OIDC certificates issued extension (1.3.6.1.4.1.11129.2.1.30)

- Leaf certificate

   - Corresponding certificate for app key-pair

   - Contains OIDC attestation extension (1.3.6.1.4.1.11129.2.1.17)

   - Contains attestationChallenge (nonce)

Decoded Leaf Certificate

Decoded Attestation Extension

#BHUSA @BlackHatEvents

## Slide 10

## Previous Public Research

- Obtain access to (extract) keys stored in TEE/SE

   - TEE hacking

      - Samsung TEEGRIS vulns

      - BH 2019: Breaking Samsung's ARM TrustZone

   - Custom ROM community

      - Flash your own keybox

   - SE hacking

🤷

      - None

- Break the PKI trust model (Focus of this research)

   - Create keys claiming to be stored in TEE/SE

🤷

- None

Samsung TrustZone Exploit Chain

Leaked Keybox Example

#BHUSA @BlackHatEvents

## Slide 11

## Bot Fraud/Abuse Use Case

- User logs into app

- App creates key-pair/attestation cert chain

- Sends cert chain to validation server

- Validation server responds with key ID (pointer to pub key)

- Requests to sensitive APIs are signed with attested key-pair

   - HTTP Message Signatures (RFC 9421)

#BHUSA @BlackHatEvents

## Slide 12

## Common PKI Issues

Certificate Chain Trust Certificate Revocation List Hard-coded Certificate

#BHUSA @BlackHatEvents

## Slide 13

## Certificate Chain Trust

- Chain of trust

   - Root certificate is signed by Google

   - Each certificate in chain signed by predecessor

- Create an insecure EC key pair

   - Not stored in TEE/SE

- Create forged X.509 leaf certificate

   - Signed by EC key pair

   - Forged OIDC attestation extension

Google Root Intermediate Leaf Google Root Intermediate Leaf Forged Leaf

   - Spoofing bootloader status, security level (TEE/SE), etc.

- Tack custom leaf certificate on the end of legit chain

#BHUSA @BlackHatEvents

## Slide 14

## Forging Our Own X.509 Certificates

Forge X.509 Certificate w/ Attestation Extension

Forge Attestation Extension

HTTP Request Sending Forged Cert Chain

#BHUSA @BlackHatEvents

## Slide 15

## Signing Our Own Requests

JSON Output With Generated Private Key

Create and Sign Forged HTTP Request

HTTP Request Forged and Signed

HTTP Response Forged and Signed Successful

#BHUSA @BlackHatEvents

## Slide 16

## Certificate Revocation List

- List of revoked certificates

- Google maintains their own CRL

- CA’s and Android device manufactures

   - Similar threat model

- Big market for leaked keyboxes

Compromised  Forged Forged
Root Intermediate Leaf

   - TEE 0-days leak Google certs

   - Firmware leaks

- Access to private key off device

   - No need to reprogram TEE

Leaked Nubia Manufacturer Keybox

- Mint your own cert chains

#BHUSA @BlackHatEvents

## Slide 17

## Hard-Coded Certificate

- Android 7 and older devices

   - No hardware attestation support

- Non-Google Play certified devices

   - Manufacturer mints their own root

- AOSP builds

   - Trusty TEE OS keybox

- Access to private key off device

   - Mint your own cert chains

Hardcoded  Forged Forged
Root Intermediate Leaf

Legacy Hardcoded Attestation Private Key

AOSP Trust TEE Keybox

#BHUSA @BlackHatEvents

## Slide 18

### Certificate Extension PKI Issue (sslstrip)

- BlackHat 2009

   - New Tricks For Defeating SSL in Practice (moxie@)

- Browsers weren’t validating Basic Constraints extension

- Valid leaf certificate could create and sign a leaf for any domain

   - Any valid SSL certificate owner can impersonate any domain

   - No ”Untrusted Site” browser errors

   - Defeating SSL

X.509 Certificate Chain Extension Issue on SSL PKI

#BHUSA @BlackHatEvents

## Slide 19

## Basic Constraints (RFC 5280)

- Identifies whether subject is CA (can issue child certs)

   - cA

- Declares maximum depth of valid cert path

   - pathLenConstraint

RFC 5280 Basic Constraints Extension

Decoded Key Attestation Intermediate Certificate

#BHUSA @BlackHatEvents

## Slide 20

### Certificate Extension PKI Issue (Android)

- Extend a legitimate key attestation cert chain

- Forged leaf cert must be embedded with insecure public key

   - Key pair generated outside of the TEE/SE

- Sign the forged leaf cert with legitimate leaf cert

   - Aside from extension validation, we’d have a valid chain of trust

- Easy for the browser PKI use case because keypairs are accessible

Google Root Intermediate Leaf Forged Leaf

   - Use PEM file on filesystem to sign forged certificate

- Android we don’t have access to the key material

   - Stored in TEE/SE

- Let’s write an Android app J

#BHUSA @BlackHatEvents

## Slide 21

## Modified Key Attestation Android App

Key Attestation Debug App

Creating Forged Leaf Certificate

Exfil Certificate Chain and Private Key

#BHUSA @BlackHatEvents

STDOUT Exfil

## Slide 22

## Using Exfiltrated Chain and Keys

HTTP Request Sending Forged Cert Chain

HTTP Response Forged Cert Chain Success

#BHUSA @BlackHatEvents

## Slide 23

## Root Cause Analysis (2024)

- Android key attestation library 👀

   - <u>https://github.com/google/android-key-attestation</u>

- Released in 2016

- Tagged as a production library

- Maintained in parity with developer documentation

- <u>https://developer.android.com/privacy-and-security/security-keyattestation</u>

- Caution about certificate extension attacks

Android Key Attestation Documentation

#BHUSA @BlackHatEvents

## Slide 24

## Android Key Attestation Library

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 96/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
) Code of conduct License Security
roid Key Attestation Library
This library uses the ASN.1 parser to extract information from an Android attestation data structure
to verify that a key pair has been generated in a hardware-protected environment of an Android device. It is
maintained in tandem with Android's key attestation capabilities and is meant for production use.
This repository contains a sample code that shows how to validate an Android attestation certificate chain
outside the Android framework. This is the recommended best practice, since if the Android device is rooted or
otherwise compromised, on-device validation of the attestation may be inaccurate.
The entry point into the is
For more details, see the documentation and the guide at
```

## Slide 25

## Library Server Code

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
black hat
ted path to x s rgument
it.printin
ttestation
out.printin
eymaster Sec
tri
his meai e attestation
at they are in f
```

## Slide 26

## Library Attestation Parsing Code

#BHUSA @BlackHatEvents

## Slide 27

## Target Code vs. Library Code

#BHUSA @BlackHatEvents

## Slide 28

## Security Patch without CVE

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
black hat
server/src/main/ java/con/android/example/KeyAttestat ionExample. ja
ParsedAttestationRecord parsedAttestationRecord Record(certs)
Mitigate the certificate chain extension attack. server/src/main/ java/con/google/android/attestat ion/ParsedAttestationRecord.
This changes the extraction of the attestation from the certificate chain. , :
Instead of unconditionally extracting the attestation in the leaf certificate this. teeEnforced = teeEnforced;
(if present), the code now walks up the certificate chain to the root, only
taking into account the last attestation extension it finds (i.e., the one
he root).
ToException {
This mitigates an attack in which an attacker crafts a new leaf certificate
with a seemingly good attestation and appends it to the certificate chain.
Parsedattestat ionRecord(extensionData) ;
(attestationExtensionBytes != null && attestationExtensionBytes. length != 0) {
re attestation extension dat:
```

## Slide 29

## Dependency Management Issue

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Consider publishing this package to Maven #12
About
@ Closed as not planned
Android Key Attestation validation library
eranmes 2 Assigne
From a comment on a pull request
| don't seem to have the ability to create issues in this repository so am commenting here:
Do you mind also publishing this server library into maven central? The current non-Google3 users | can find of it are all just.
directly , which will eventually drift/be stale.
tnek on Sep 16, 2
Another (maybe easier?) option that would work for us is bazelizing the con.google.android.attestation package for the
git_repository bazel rule.
If either of these aren't a priority for you, I'm happy to submit a PR doing so.
JesusMcCloud on Ar
FYI: since we depend on it, we've already
Our main motivation was to make it easily configurable and play well in any sort of back-end (be it spring, ktor, whatever)
Releases
We've also taken it upon ourselves to provide that also integrated iOS attestation.
Packages brandonweeks
@ ® drandonweeks not planned last
```

## Slide 30

## Insufficient Security Patch

Leaf First Ordering
Forged Leaf Leaf Intermediate Google Root
Root First Ordering
Google Root Intermediate Leaf Forged Leaf

#BHUSA @BlackHatEvents

## Slide 31

## Disclosure Timeline

- **19 Dec 2016 –** Key Attestation library published to GitHub

- **20 Feb 2023 –** Security patch for certificate extension attack

- **05 Sep 2024 –** Reported insufficient security patch

- **08 Nov 2024 –** Google response (Won’t Fix), library flagged for deprecation

- **26 Nov 2024 –** Updated README.md, not intended for production use

- **10 Apr 2025 –** New Key Attestation library published to GitHub

- **11 Jun 2025 –** Updated README.md, deprecated use new library

#BHUSA @BlackHatEvents

## Slide 32

## Black Hat Sound Bytes

- Android Key Attestation is in a fragmented state

- Well organized and concerted efforts to circumvent key attestation in online communities

- Effective mechanism for combatting bot fraud and abuse

- Test your own implementations with keyattestor

#BHUSA @BlackHatEvents

## Slide 33

## keyattestor

- <u>https://github.com/dubfree/keyattestor</u>

- Builds custom X.509 certificate chain payloads to test Android Key Attestation implementations

- Certificate Chain Trust

- Certificate Revocation List

- Hard-coded Certificate

- Certificate Extension

#BHUSA @BlackHatEvents

## Slide 34

Thank You!
Alex Gonzalez
#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
AUGUST 6-7, 2025
MANDALAY BAY / LAS VEGAS
Thank You!
Alex Gonzalez
#BHUSA @BlackHatEvents
```
