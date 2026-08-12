---
title: "8 Out of 10 Banks in Belgium HATE This One Weird eID RCE"
speakers: ["James Arnott"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: null
source_pdf: "DEF CON 34/DEF CON 34 - James Arnott - 8 Out of 10 Banks in Belgium HATE This One Weird eID RCE - MEDIA SERVER Belgi.pdf"
pages: 71
sha256: "40bb3a9d88cc35e526c94fe401905516b8b661c4c52c2728af24d7a10af421b1"
text_chars: 20493
ocr_pages: 5
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:22:41Z"
---
# 8 Out of 10 Banks in Belgium HATE This One Weird eID RCE

**Speakers:** James Arnott  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - James Arnott - 8 Out of 10 Banks in Belgium HATE This One Weird eID RCE - MEDIA SERVER Belgi.pdf` (71 pages)


## Slide 1

----- START DEFCON TALK ----DEF CON 34 // EID · DRIVE-BY RCE · 2M+ USERS **8 out of 10 banks in Belgium HATE this one weird eID RCE** Belgium · eIDAS · Connective Signing Extension

###### **James Arnot**

a story in three demos

@Acorn221

## Slide 2

$ WHOAMI

DEF CON 34

###### **James Arnot**

- 01 I'm the founder of Bay Area Labs, working on Am I Being Pwned specialising in browser extension security'

- 03 My background is in full stack development and doing hacky things with JS

- 02 I've been building browser extensions for over 10 years (on and off), creating one of the most used extensions for Tinder

- 04 I break browser extensions.

eID RCE — DEF CON 34

## Slide 3

01 / 03

INTRO

**01**

eID RCE — DEF CON 34

## Slide 4

02 / 03

INTRO

Common Services for Access Management

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
INTRO Q2 / 03
lg CSAM HOME WHATISCSAM? SERVICESY CONTACT
CSAM, the gateway to the services of the government
Make your life easier with CSAM. You will find yourself in a familiar and reliable environment every time you log in, designate access managers, conclude mandates
etc. Since CSAM ensures that everyone follows the same rules and makes use of generic services, it guarantees a higher and constant level of security.
CSAM OFFERS THE FOLLOWING SERVICES
2 MY DIGITAL KEYS MANAGEMENT OF ACCESS Ye = MANAGEMENT OF MANDATES
MANAGERS
Manage your digital keys to access Structure the access management of Manage all of your mandates.
the online services provided by various your company.
Belgian authorities.
Common Services for Access Management
```

## Slide 5

03 / 03

INTRO

**01**

What sits behind the card

## Slide 6

01 / THE EID

DEF CON 34

###### **So How do you log into CSAM?**

###### **Your eID!**

eID RCE — DEF CON 34

## Slide 7

DEF CON 34

01 / THE EID

###### **A compulsory national ID card for everyone over 12.**

01 02 03 04 05 Banking Government Tax returns Healthcare **Legal** services **e-signatures**

Those signatures fall under the EU's eIDAS regulation, the same legal framework across every member state.

eID RCE — DEF CON 34

## Slide 8

DEF CON 34

01 / THE EID

QUALIFIED ELECTRONIC SIGNATURE

**The same legal effect as a handwritten signature, across every EU member state.**

The highest assurance tier eIDAS recognises. Binding on contracts, mortgages, and government f i lings.

eID RCE — DEF CON 34

## Slide 9

01 / THE EID

DEF CON 34

###### **Two private keys on one chip.**

KEY 1

KEY 2

**Authentication**

**Non-repudiation**

Logging into banking and government services.

Producing legally-binding signatures.

**Both** require the same PIN.

The private keys **never leave the card** .

eID RCE — DEF CON 34

## Slide 10

01 / THE EID

02 / 08

###### **Why am I talking about eIDs?**

One red flag in a pile of 2,000

## Slide 11

02 / HOW I FOUND IT

DEF CON 34

###### **Auditing the top 2,000 extensions.**

METHOD

THE FLAG

**Static analysis + LLM triage**

###### **No origin forwarded**

Bulk-scan the manifests and JS, let the model flag the anomalies worth a human look.

The extension never tells the native host which site is talking. The binary is blind to the caller.

eID RCE — DEF CON 34

## Slide 12

DEF CON 34

02 / HOW I FOUND IT

Why am I talking about eIDs?

### **Nitro Software and their Connective Signing Extension**

Nitro Software, A Qualif i ed Trust Service Provider

eID RCE — DEF CON 34

## Slide 13

02 / HOW I FOUND IT

DEF CON 34

CONNECTIVE SIGNING EXTENSION — AT SCALE

of Belgium's largest banks **8/10** enterprise accounts **1,000+**

**60+** government agencies **2M+** extension users

eID RCE — DEF CON 34

## Slide 14

DEF CON 34

02 / HOW I FOUND IT

###### **Who's downstream of it.**

BNP Paribas ING Bank Cofidis Toyota Pirelli The Antwerp police publicly endorse the platform on Connective's own website. Over 2M total endpoints have the Connective signing extension installed.

eID RCE — DEF CON 34

## Slide 15

DEF CON 34

02 / HOW I FOUND IT

**Certified to the highest trust tier eIDAS defines.**

Qualified Trust Service Provider

EU eIDAS Trusted List

ISO 27001

SOC 2 Type II

Nitro Software Belgium.

eID RCE — DEF CON 34

## Slide 16

DEF CON 34

02 / HOW I FOUND IT

THE BLIND SPOT **The store reviews the JavaScript. The binary that does the damage is never looked at.**

eID RCE — DEF CON 34

## Slide 17

03 / HOW IT WORKS **03 How the extension works**

03 / 08

From a webpage to a smart card

## Slide 18

DEF CON 34

02 / HOW I FOUND IT

###### **Two components — and a review boundary running right between them.**

REVIEWED BY CHROME

###### **Browser extension**

native messaging

OUTSIDE REVIEW **Native host binary**

Manifest + JavaScript. Content script, service worker.

→ A standalone Windows executable. Talks to the smart-card reader.

eID RCE — DEF CON 34

## Slide 19

03 / HOW IT WORKS

DEF CON 34

One message, four hops, zero origin checks.
01 02 03 04 05
Webpage → Content script → Service worker → Native host → Smart card reader
postMessage injected bridge connectNative() APDU commands With an eID inserted
The origin is known at hop 01 — and thrown away before hop 02.

eID RCE — DEF CON 34

## Slide 20

DEF CON 34

02 / HOW I FOUND IT

###### **The message that reaches the native host carries no caller.**

● ● ● background.js · service worker

// open a channel to the installed native binary

const port = chrome.runtime. **connectNative** ("com.connective.signer");

port.postMessage({ cmd: "PKCS_GET_READERS", token }); // **↑ no origin. no referer. ever.**

eID RCE — DEF CON 34

## Slide 21

03 / HOW IT WORKS

03 / 08

**Ho2e72n34WbFHp7DqkNeYRa+6cmDrwHn/sqHmmWVvLJDTE/Ba+l0v77sxY+XqAupOLup9f767Ybuggh RPfYevpnjZRJBDNe9jwJLhM/N8SDiYtNr66ANe83cMsisNXdwszs+ao9mbVafXXLXsHzJIntWCmVc+ROdl SLgGnE4iS37/hlIwT3VHPrMwvrdKm4vhquKlI+q/9hye6m25nFWWnFlLLfDBYnW2J9+lO597gv/XUwOaU0 VJILtzEtJFm6zbEMuFukxN3wrLIRutApaOQGjRdY2A70bJTOo/KXbQhP9ET/jLVvk2EoORWJqRJI/Q0R7w waEEJOpLsnQANhZQQ==**

###### **The Activation Token**

RSA 2024 Signed Token

## Slide 22

03 / HOW IT WORKS

DEF CON 34

● ● ● decrypted payload · from the PoC

###### **How the binary validates it**

{

1 base64-decode → 256 bytes

- 2 **RSA_public_decrypt** · hardcoded 2048-bit key

- 3 strip PKCS#1 v1.5 padding → JSON

- 4 check **ttl** against the system clock

"token":    "1c3ce6b7-…-1d9f63670948", "ttl":      1642867234735, "features": 7 }

- 5 check the **features** bitmask

ttl  → 2022-01-22 16:00:34 UTC feat → 0b111 (everything) **no origin · no machine · no user**

eID RCE — DEF CON 34 · cardcomm-native-messaging v2.0.9

## Slide 23

03 / HOW IT WORKS

DEF CON 34

###### **It's RSA signature recovery — so I can't forge one. I don't need to.**

WHAT PROTECTS IT

WHAT DOESN'T

###### **A 2048-bit RSA signature**

###### **Any captured token, anywhere**

Can't mint new tokens without Connective's private key.

No origin / machine / user binding. One leaked token works everywhere.

TTL expired? sudo date 012215552022

GET_INFO needs no token at all

eID RCE — DEF CON 34

## Slide 24

DEF CON 34

03 / HOW IT WORKS

###### **One features** **bitmask gates every command.**

**bit 0 · 1** GET_READERS · READ_FILE · VERIFY_PIN · COMPUTE_SIGNATURE · COMPUTE_AUTHENTICATION

**bit 2 · 4** COMPUTE_SIGN_CHALLENGE · SELECT_MAESTRO · GET_PROCESSING_OPTIONS · READ_RECORD

GET_INFO no token required at all

check is (features & required) /= 0 — a bitwise AND, not equality

The RCE rides on PKCS_GET_READERS — a **bit-0** command. So essentially any valid token reaches code execution.

eID RCE — DEF CON 34

## Slide 25

03 / HOW IT WORKS

DEF CON 34

#### **Any site can replay the token and talk to the card.**

The extension cannot tell a bank's website apart from an attacker's page. Within the TTL, both are simply "the caller".

eID RCE — DEF CON 34

## Slide 26

DEF CON 34

03 / HOW IT WORKS

**Implicit trust, all the way down.**

ANY SITE trusts → **— is trusted by the extension** EXTENSION trusts → **— is trusted by the native host**

NATIVE HOST trusts → **— is trusted by the smart card**

A straight line from any webpage to the eID chip. Nothing is checked.

eID RCE — DEF CON 34

## Slide 27

04 / READING THE CARD **04 Reading the card**

04 / 08

PII and payment data, zero clicks

## Slide 28

DEF CON 34

04 / READING THE CARD

THE OBSTACLE

###### **I don't have a Belgian eID.**

So I can't test anything unless I build a card the extension is willing to talk to.

THE WORKAROUND

###### **A virtual eID**

A simulated card that answers the extension's expected interface. The native host can't tell it from the real chip. ESP-32 OTG Based.

eID RCE — DEF CON 34

## Slide 29

04 / READING THE CARD

DEF CON 34

###### **Get t** **ing a token to validate.**

ATTEMPT 1

###### **Roll the clock back**

The captured token was expired. Set the system clock into the past — and it validated.

ATTEMPT 2

###### **An oracle**

Then I found a way to mint a fresh, valid token outright. No clock games needed.

eID RCE — DEF CON 34

## Slide 30

04 / READING THE CARD

DEF CON 34

### **No PIN required to read the card.**

The activation token alone is suf fi cient. The PIN gates signing and authentication - never reading.

eID RCE — DEF CON 34

## Slide 31

04 / READING THE CARD

DEF CON 34

###### **What comes back, zero interaction.**

no PIN · no click · via iframe **What comes back, zero interaction.** ● ● ● card_dump.json full_name rijksregisternummer (SSN) Richard Paul Astley 69.67.21-420.69 home_address photograph ████████████ ██ [ jpeg · 140×200 ] maestro_pan valid_from / to 6703 ████ ████ ████ ██/██ → ██/██

eID RCE — DEF CON 34

## Slide 32

04 / READING THE CARD

DEF CON 34

#### **Embeddable in a hidden iframe on any page.**

The user sees an ordinary website. There is no sign their data was ever touched.

eID RCE — DEF CON 34

## Slide 33

DEF CON 34

04 / READING THE CARD

FROM A SINGLE PAGE VISIT **A complete identity-theft kit.**

The Rijksregisternummer is Belgium's national insurance number. Name + address + photo + national ID is everything you need to become someone.

eID RCE — DEF CON 34

## Slide 34

DEMO 01 / 03

● LIVE DEMO

# **01 Silent PII & Maestro exfl i**

eID RCE — DEF CON 34 · zero user interaction

## Slide 35

05 / THE PIN

05 / 08

###### **But what about the PIN?**

8 in 10 cryptographers think something went wrong

## Slide 36

05 / THE PIN

05 / 08

**Getting into the braincell(s) of the connective employee who engineered the pin system**

8 in 10 cryptographers think something went wrong

## Slide 37

DEF CON 34

05 / THE PIN

**Any site can trigger the VERIFY_PIN flow.**

Which means any site can put the official-looking PIN prompt in front of the user, whenever it wants.

eID RCE — DEF CON 34

## Slide 38

05 / THE PIN

DEF CON 34

**The dialog never says who's asking.**

Title and description are attacker-controlled.

eID RCE — DEF CON 34

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
05 / THE PIN
The dialog never says who’s
asking.
Title and description are
attacker-controlled.
eID RCE — DEF CON 34
r-
BNP Paribas Bank Login
DEF CON discount special, 1000% cashback when
you get rick rolled
Cancel OK
Be an
employee at
early stage
Connective
Let any website
request the
users pin
Let any website
control the text
inside the pin
dialog
```

## Slide 39

05 / THE PIN

DEF CON 34

**The host is killed after every message.**

The PIN typed in one message is gone by the next.

No state is maintained on the native host or the extension.

eID RCE — DEF CON 34

## Slide 40

05 / THE PIN

DEF CON 34

**The host is killed after every message.**

The PIN typed in one message is gone by the next.

No state is maintained on the native host or the extension.

eID RCE — DEF CON 34

## Slide 41

05 / THE PIN

DEF CON 34

###### **The host is killed after every message.**

● ● ● native_host lifecycle

eID RCE — DEF CON 34

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
05 / THE PIN
The host is killed after every message.
@@@ native_host lifecycle
Web page Extension Native host
postMessage: VERIFY_PIN
sendNat iveMessage(VERIFY_PIN)
Prompts user for PIN
native dialog ~ mints token
stdout: pinToken
x
process exits
postMessage: pinToken
eID RCE — DEF CON 34
Be an
employee at
early stage
Connective
Let any website
request the
users pin
Let any website
control the text
inside the pin
dialog
Cache the pin
so the user
doesn't have to
re-enter it
Make the
untrusted site
manage the state |
of the cache
```

## Slide 42

DEF CON 34

05 / THE PIN

###### **The Pin is encrypted inside of the pinToken**

● ● ● pinToken · AES-128-CBC

pinToken Z0WLa8YjezJpmDxkc0gzZlHcsHT/XEkZSpToKuxYVWLh+AAByPpJIGoAP3VlbtC0

base64 → 48 bytes 67 45 8b 6b c6 23 7b 32 69 98 3c 64 73 48 33 66 51 dc b0 74 ff 5c 49 19 4a 94 e8 2a ec 58 55 62 **e1 f8 00 01 c8 fa 49 20 6a 00 3f 75 65 6e d0 b4** /- pin ciphertext

eID RCE — DEF CON 34

## Slide 43

05 / THE PIN

###### **The whole pinToken, end to end.**

● ● ● pinToken → PIN · AES-128-CBC

base64 → 48 bytes **67** 45 **8b** 6b **c6** 23 **7b** 32 **69** 98 **3c** 64 **73** 48 **33** 66 **51** dc **b0** 74 **ff** 5c **49** 19 **4a** 94 **e8** 2a **ec** 58 **55** 62 e1 f8 00 01 c8 fa 49 20 6a 00 3f 75 65 6e d0 b4 /- pin ciphertext

Decrypted contents:

**34 32 30 36 39 80 a7 63 98 71 01 00 00**

34='4', 32='2', 30='0', 36='6', 39 = '9'

TTL: 1587399600000

Monday, 20 April 2020 at 16:20:00

Step 2: AES-128 key (bytes 0,2,4,//.,30): 67 8b c6 7b 69 3c 73 33 51 b0 ff 49 4a e8 ec 55

Step 3: Hardcoded IV in Binary

a6 a6 a6 a6 a6 a6 a6 a6 a6 a6 a6 a6 a6 a6 a6 a6

PIN **42069**

eID RCE — DEF CON 34

## Slide 44

05 / THE PIN

DEF CON 34

##### **Now attackers can phish user's pin, then replay it whenever they want**

eID RCE — DEF CON 34

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
05 / THE PIN
Now attackers can phish
user’s pin, then replay it
whenever they want
eID RCE — DEF CON 34
Be an
employee at
early stage
Connective
Let any website
request the
users pin
Let any website
control the text
inside the pin
dialog
Cache the pin
so the user
doesn't have to
re-enter it
Make the
untrusted site
manage the state
of the cache
Expose the
encrypted pin to
the untrusted site
Expose the pin
decryption key to
the untrusted site,
leaking the pin
```

## Slide 45

05 / THE PIN

DEF CON 34

### **One PIN unlocks both keys.**

The PIN is shared across authentication and non-repudiation. A single capture means login and legally-binding signatures in the victim's name.

eID RCE — DEF CON 34

## Slide 46

05 / THE PIN

DEF CON 34

###### **Relaying a live CSAM login.**

|01|**Start a CSAM login as the victim**|the federal SSO for tax, health, gov|
|---|---|---|
|02|**CSAM returns a challenge**|a nonce to be signed by the card|
|03|**COMPUTE_AUTHENTICATION →**|shared PIN + replayed pinToken; no origin check|
||**card**||
|04|**Card signs the challenge**|auth key — same PIN as signing|
|05|**Submit it → logged in as the**
**victim**|full session on their identity|

eID RCE — DEF CON 34

## Slide 47

DEMO 02 / 03

● LIVE DEMO

# **02 CSAM TAKEOVER**

eID RCE — DEF CON 34

## Slide 48

05 / THE PIN

06 / 08

**This breaks the entire ecosystem relying on eID auth and signatures**

No more secure CSAM for you

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
This breaks the
entire ecosystem a YOU WOULDN'T sr
relying on elD auth ~~ STEAY AN :
Sicieatures | ee. _ WENTITY
and signatures
No more secure CSAM for you
```

## Slide 49

06 / TO RCE **06 From LoadLibraryA to RCE**

06 / 08

A substring check, weaponised

## Slide 50

06 / TO RCE

###### **So I decompiled the rest of the native host.**

Mapping every command available for any webpage to trigger, along with the arguments

PKCS_GET_READERS **→ LoadLibraryA · RCE** COMPUTE_AUTHENTICATION → CSAM auth relay GET_CARD_DATA → PII / Maestro SIGN_HASH → pinToken

DEF CON 34

● ● ● evil.com · message to connective

window.postMessage({ cmd: 'PKCS_GET_READERS', activationToken: 'Ho2e72n34WbFHp7DqkNeYRa…' library: `C:\\evil.dll`, });

eID RCE — DEF CON 34

## Slide 51

06 / TO RCE

DEF CON 34

● ● ● native_host.exe · decompiled

**A web-controlled path, straight into LoadLibraryA.**

The PKCS_GET_READERS handler takes a library path and loads it. No allowlist. No signature. No directory restriction.

// PKCS_GET_READERS handler char* lib = json_get(msg, "library"); if (strstr(lib, ".dll")) { **LoadLibraryA** (lib);

}

eID RCE — DEF CON 34

## Slide 52

06 / TO RCE

DEF CON 34

###### **Chrome blocks .dll** **downloads.**

CHROME SEES

NATIVE HOST SEES

**…evil.dll.png**

**…evil.dll.png**

A PNG image. No download warning. No friction. Contains ".dll". Passes the check. LoadLibraryA runs it.

eID RCE — DEF CON 34

## Slide 53

06 / TO RCE

DEF CON 34

**It checks for ".dll"** **as a substring — not as the extension.**

C:\\Users\Downloads\reader **.dll**

contains ".dll" → loads ✓ (intended)

C:\\Users\Downloads\evil **.dll** .png

contains ".dll" → loads ✓ (oops)

The extension on the end of the f i lename is now irrelevant to whether it loads.

eID RCE — DEF CON 34

## Slide 54

DEF CON 34

06 / TO RCE

A PROPER POLYGLOT

###### **Frien.dllyReminder.pdf**

TO CHROME

TO WINDOWS

**A harmless PDF**

**A valid DLL**

Downloads silently, like any document.

Loads and executes via LoadLibraryA.

eID RCE — DEF CON 34

## Slide 55

DEF CON 34

06 / TO RCE

###### **How do we get the path of the DLL?**

● ● ● native_host.exe - Location

C:\Users\<user>\AppData\Local\Connective\SigningChromePlugin\

/.\/.\/.\/.\Downloads\Frien.dllyReminder.pdf

eID RCE — DEF CON 34

## Slide 56

06 / TO RCE

DEF CON 34

###### **Drive-by RCE — no clicks, no prompts, no warnings.**

> 01 **Visit the page** polyglot auto-downloads — Chrome stays silent

02 **Page sends command** PKCS_GET_READERS, path = …\Downloads\f i le

> 03 **Native host loads it** LoadLibraryA on the Downloads path

> 04 **Code executes** as the current user — full RCE

eID RCE — DEF CON 34

## Slide 57

DEMO 03 / 03

● LIVE DEMO

# **03 Full RCE, live Windows**

eID RCE — DEF CON 34 · code exec as current user

## Slide 58

07 / DISCLOSURE

07 / 08

**07 Disclosure & limitations**

What's proven, and what isn't

## Slide 59

07 / DISCLOSURE

DEF CON 34

###### **Straight about what's been proven.**

**CONFIRMED**

eID leak verified on a real Belgian card by ItsMe

**CONFIRMED**

RCE works outright — it needs no eID at all

**IN CODE**

CSAM auth relay: COMPUTE_AUTHENTICATION, shared PIN, pinToken replay

**SIMULATED**

Demos run on a virtual eID; no end-to-end test against live CSAM

eID RCE — DEF CON 34

## Slide 60

07 / DISCLOSURE

DEF CON 34

###### **Reported to Nitro and the CCB.**

FEB 26, 2026

**Notif i** **ed**

PoC + demo video of the eID leak

MAR 13, 2026

→ **First Acknowledgement of vulnerability**

JUN 1, 2026

→ **Fixed RCE + PinToken leak**

→

JUN X, 2026

**Fully Fixed**

eID RCE — DEF CON 34

## Slide 61

DEF CON 34

07 / DISCLOSURE

CCB WALL OF FAME

###### **I was added to the CCB wall of fame**

The Center for Cybersecurity Belgium

eID RCE — DEF CON 34

## Slide 62

08 / WHAT IT MEANS **08 What this means for you**

08 / 08

Takeaways

## Slide 63

08 / WHAT IT MEANS

DEF CON 34

###### **Store review finds policy violations and known malware. Not broken architecture and not vulnerabilities**

And the native messaging host sits entirely outside it. A green badge is not a security signal.

eID RCE — DEF CON 34

## Slide 64

08 / WHAT IT MEANS

DEF CON 34

###### **For organisations**

- 01 Whitelist extensions and pin versions.

- 03 Network monitoring isn't enough on its own.

- 02 Don't treat CWS badges or reviews as a security signal.

- 04 Extensions can wait on login state or delayed remote config before activating.

eID RCE — DEF CON 34

## Slide 65

08 / WHAT IT MEANS

DEF CON 34

###### **For extension developers**

**01** Validate every input from a web page. **02** Bind tokens to origins and sessions — the missing piece here.

- **03** Validate and restrict paths in native messaging.

- **04** Never trust the main world. The page is hostile.

eID RCE — DEF CON 34

## Slide 66

08 / WHAT IT MEANS

DEF CON 34

###### **This was never just a Belgian problem.**

eID is expanding across the EU under eIDAS 2.0 Any browser-based eID with native-messaging components inherits this same attack surface.

eID RCE — DEF CON 34

## Slide 67

DEF CON 34

// ----- END DEFCON TALK -----

## **Stop letting any site message your native host.**

It's a bad idea for a hundred reasons. This is what one of them looks like.

###### **James Arnot**

@Acorn221

Thanks, DEF CON. Questions →

## Slide 68

DEF CON 34

// ----- END DEFCON TALK -----

## **Shoutouts!**

- CCB

- The linux community - <u>ht</u> t <u>ps://github.com/roelderickx/connective-plugin-linux</u>

###### **James Arnot**

@Acorn221

Thanks, DEF CON. Questions →

## Slide 69

DEF CON 34

// ----- END DEFCON TALK -----

## **Shoutouts!**

connective-plugin-linux readme.md

###### **James Arnot**

@Acorn221

Thanks, DEF CON. Questions →

## Slide 70

DEF CON 34

// ----- END DEFCON TALK -----

## **Shoutouts!**

- CCB

- The linux community - <u>ht</u> t <u>ps://github.com/roelderickx/connective-plugin-linux</u> t i

- t

- - The Pico Keys project - <u>ht</u> t <u>ps://github.com/polhenarejos/pico-f</u> i <u>do</u> t

- t i

- - The NSA - <u>htps://github.com/nationalsecurityagency/ghidra</u> t

- Anthropic - Opus was very helpful here Ghidra - sonnet initially discovered the lack of origin checks

- Anonymous Belgian Friend with a real eID for the CSAM demo

- Piet De Vaere & Floor Terra

###### **James Arnot**

@Acorn221

Thanks, DEF CON. Questions →

## Slide 71

----- END DEFCON TALK -----

DEF CON 34

## **Questions?**

Linkedin ( )

###### Blog Post

###### **James Arnot**

@Acorn221
