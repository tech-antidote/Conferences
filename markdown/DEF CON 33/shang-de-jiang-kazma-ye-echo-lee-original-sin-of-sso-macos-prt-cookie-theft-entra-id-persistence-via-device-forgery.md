---
title: "Original Sin of SSO macOS PRT Cookie Theft & Entra ID Persistence via Device Forgery"
speakers: ["Shang-De Jiang Kazma Ye Echo Lee"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33/Shang-De Jiang Kazma Ye Echo Lee - Original Sin of SSO macOS PRT Cookie Theft & Entra ID Persistence via Device Forgery.pdf"
pages: 78
sha256: "7b26ad7646d0ae903f921d3d6499f024b311458c7c7f79670f9cc07c9ec124e8"
text_chars: 22128
ocr_pages: 22
has_ocr: true
redacted_secrets: 0
ocr_confidence: 90.7
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T07:14:24Z"
---
# Original Sin of SSO macOS PRT Cookie Theft & Entra ID Persistence via Device Forgery

**Speakers:** Shang-De Jiang Kazma Ye Echo Lee  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33/Shang-De Jiang Kazma Ye Echo Lee - Original Sin of SSO macOS PRT Cookie Theft & Entra ID Persistence via Device Forgery.pdf` (78 pages)


## Slide 1

**Original Sin of SSO: macOS PRT Cookie Theft & Entra ID Persistence via Device Forgery**

Shang-De ‘John’ Jiang Kazma Ye

Echo Lee

## Slide 2

### $ whoami

Shang-De ‘John’ Jiang (@SecurityThunder) Deputy Director of Research at UCCU Hacker Co-Founder Blog: HackerPeanutJohn Speaker at the following technical conferences: BlackHat USA, CodeBlue, HITCON , HITB, TROOPERS, Sans Blue Team Summit …

2

## Slide 3

#### **A lots of service! You need SSO**

3


> Recovered by OCR — confidence 82/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
A lots of service! You need SSO
Microsoft Lists app
From sources across the web
OneDrive v oF Outlook v i Microsoft Teams v
kb Excel v Ee Microsoft Intune v “n Microsoft 365 v
Microsoft Forms v Microsoft Stream Vv ne Microsoft Power Pl... v
A Microsoft Azure v
>. Power Automate v
Microsoft Planner v is Microsoft Sway v
PowerPoint Vv lw | Word Vv
```

## Slide 4

#### SSO token generate in Windows OS

LSASS
Cloud AP:
aadcloudap
CreateSSOCookie
TPM
PRT Session Key

4

## Slide 5

#### **PRT Can Exchange Everything We Wanted**

TPM
∞ hrs
15 mins
24 hrs
24/28 hrs

5


> Recovered by OCR — confidence 90/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
PRT Can Exchange Everything We Wanted
TPM
Token
= ; Microsoft Lists app
Access
Token 24/28 hrs
```

## Slide 6

#### **Browser SSO on Windows**

Chrome
PRT Cookie
BrowserCore.exe LSASS
MicrosoftAccount
TokenProvider.dll
Cloud AP:
Nonce
aadcloudap
CreateSSOCookie
GetCookieInfoForUri
call number , payload
LsaCallAuthenticationPackage

Ref : https://i.blackhat.com/Asia-24/Presentations/Asia-24-Chudo-Bypassing-Entra-ID-Conditional-Access-Like-APT.pdf

6

## Slide 7

#### **Abuse Browser SSO on Windows**

A
RequestAAD LSASS
RefreshToken
Cloud AP:
aadcloudap
B
CreateSSOCookie
GetCookieInfoForUri
BAADTokenBroker LsaCallAuthenticationPackage C

Ref: https://i.blackhat.com/Asia-24/Presentations/Asia-24-Chudo-Bypassing-Entra-ID-Conditional-Access-Like-APT.pdf

7

## Slide 8

#### **The PRT Cookie includes user identity + linked device information**

8


> Recovered by OCR — confidence 92/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
The PRT Cookie includes
user identity + linked device information
Single sign-on Flow
Challenge Request
. [ Nonce + PRT + Session Key ] Calc
Device > PRT Cookie Entra ID
>
Refresh Token, Access Token
```

## Slide 9

**The PRT Cookie includes PRT Cookie From Device Can Include MFA Claim + Device Claim user identity + linked device information**

9


> Recovered by OCR — confidence 94/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Single sign-on Flow
Challenge Request
Nonce
[ Nonce + PRT + Session Key ] Calc
Device > PRT Cookie
Refresh Token, Access Token
Entra ID
```

## Slide 10

#### **Today’s Objectives: From PRT Cookie to Persistence**

Steal PRT Cookie from macOS

Establish Long-Term Persistence & Compliance Security Requirement

Convert temporary access into a permanent foothold by forging a new device in Entra ID. Use the token's embedded MFA and Device claims to defeat most Conditional Access policies Goal: Access Critical Resources

Impersonate the user to gain unrestricted access to data in Azure and Microsoft 365

10

## Slide 11

## PRT Cookie Theft on macOS

11

## Slide 12

### $ whoami

🥷 Kazma Ye University Student in Taiwan 🇹🇼 Leader @ CTF Team B33F50UP Cybersecurity Researcher @ Founder of Taiwan Security Club & NCKUCTF 1st Place AIS3 EOF | 3rd Place WorldSkills Cybersecurity 10th Place HITCON CTF (1st in Taiwan) Talks @ TROOPERS25, DEF CON 33, RomHack

12

## Slide 13

#### Why Steal macOS PRT Cookies?

Many organizations use Intune as MDM for both Windows and macOS Conditional Access supported on macOS for Zero Trust enforcement Existing research and detections focus mostly on Windows Lack of research on macOS attack surface and exploitation paths

13

## Slide 14

#### How macOS use similar mechanism?

14


> Recovered by OCR — confidence 88/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
How macOS use similar mechanism?
L_| | Learn Discover v Product documentation v Development languages Y __ Topics v
Microsoft Intune Product documentation v Learn Intune Developer resources Y Troubleshooting Resources v
\é Filter by title Learn / Microsoft Intune / Intune service / Intune user help / (*) Ask Learn
- oven Enroll your macOS device using the
Device enrollment overview Company Portal app
What information can my organization see?
Microsoft Intune user help
Get Intune Company Portal 04/24/2025
Update Intune Company Portal
Set up secure, remote access to work emails, files, and apps on your personal Mac. This article
Add device password, PIN, or passcode : .
describes how to install the Company Portal app, enroll your Mac for work, and get
Install mobile threat defense app troubleshooting help
> Android device management
```

## Slide 15

#### Company Portal on macOS

Ref: https://youtu.be/awckSIpCPMg?si=18uS-Ot0jNSeMpUs

15


> Recovered by OCR — confidence 92/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
15
Company Portal on macOS
Platform SSO and Microsoft
Apps and Safari
|
Platform SSO
Intune (SSO extension)
?
Entra ID
Ref: https://youtu.be/awckS|pCPMg?si=18uS-Ot0/NSeMpUs
```

## Slide 16

#### Main Structure of Company Portal

**Company Portal**

**Mac SSO Framework ADAuthentication Extension Broker MacOS Plugins AutofillExtension MacOS BrowserCore Resources**

16

## Slide 17

#### Browser SSO on Windows

Chrome
PRT Cookie
BrowserCore.exe LSASS
MicrosoftAccount
TokenProvider.dll
Nonce Cloud AP:
aadcloudap
CreateSSOCookie
GetCookieInfoForUri
call number , payload
LsaCallAuthenticationPackage

Ref : https://i.blackhat.com/Asia-24/Presentations/Asia-24-Chudo-Bypassing-Entra-ID-Conditional-Access-Like-APT.pdf

17

## Slide 18

#### Browser SSO Flow on macOS

**Chrome PRT Cookie**

**BrowserCore Company Portal Nonce AppSSOAgent Mac SSO ADAuthentication Extension BrokerMacOS**

18

## Slide 19

#### Three Techniques We Discovered

Headless Browser-Based Native Messaging Abuse Bypassed BrowserCore’s parent process check Direct SSO Invocation via Apple’s API

19

## Slide 20

### Headless Browser-Based Native Messaging Abuse

20

## Slide 21

#### BrowserCore on macOS

Microsoft SSO Chrome extension

21


> Recovered by OCR — confidence 86/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
21
BrowserCore on macOS
Microsoft SSO Chrome extension
Console Performance
> chrome. runtime. sendNativeMessage(
“com.microsoft.browsercore"
Sources Network
® background.js w Y Filter
method: "GetCookies",
sender: "https://login.microsoft.com",
uri: "https://login.microsoftonline.com/common/oauth2/v2.0/authorizea"
function (response) {
if (chrome.runtime.lastError) {
BrowserCore:
} else {
console. log("Response:", response);
}
}
< undefined
Response: w {response: Array(2)} i
» response: (2) [{..}, {..}]
» [[Prototype]]: Object
Memory
Application
(AppSSOCore) [com.apple.AppSSO:SOClient] -[SOClient perf
ationOptions = {
"msg_protocol_ver" = 4;
“parent_process_bundle_identifier" = "com.google.Chrome";
“parent_process_localized_name" = "Google Chrome";
"parent_process_teamId" = EQHXZ8MB8AV;
payload = "{\"method\":\"GetCookies\",\"sender\":\"https://1lo
```

## Slide 22

#### Headless Browser Method Condition

Victim must be logged into desktop session

Headless browser ≠ no GUI dependencies Only works on official Chrome, Edge

22

## Slide 23

#### Three Techniques We Discovered

⚠ Headless Browser-Based Native Messaging Abuse Requires Specific Environment Conditions

Bypassed BrowserCore’s parent process check Direct SSO Invocation via Apple’s API

23

## Slide 24

### Bypassed BrowserCore’s Parent Process Check

24

## Slide 25

#### BrowserCore Parent Check

**BrowserCore**

**runningApplication Get .app parent process info Launch or not WithProcessIdentifier() Get bundle & team ID codesign -dv Bundle + Team ID → Hash Check against whitelist**

25

## Slide 26

#### What are Team ID and Bundle ID?

Team ID is embedded in the Apple Developer certificate Bundle ID appears in both Info.plist and binary’s code signature Bundle ID is just a string for identification

Attackers can fake Bundle ID, but not Team ID

26

## Slide 27

#### Security Identifier (SID) on Windows

27

Ref: https://i.blackhat.com/Asia-24/Presentations/Asia-24-Chudo-Bypassing-Entra-ID-Conditional-Access-Like-APT.pdf

## Slide 28

#### Two Different Callers in SSO Flow

Caller of BrowserCore
A browser (e.g. Chrome, Edge)
Parent in the parent process checked
Caller of AppSSOAgent
BrowserCore (or a similar implementation by third-party vendors)
Requires CS_VALID or CS_DEBUGGED to retrieve the caller’s Team ID

28

## Slide 29

#### Attack Strategy

1. Create payload.bin with the crafted request

2. Build a fake codesign binary that mimics Chrome’s signature

3. Develop a .app to act as a running application

4. Launch BrowserCore with the fake app as its parent and set PATH=/tmp to redirect the codesign check to our fake binary

29

## Slide 30

#### Screenshots of our First POC 💥

30


> Recovered by OCR — confidence 89/100 on the text kept, 64/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
30
Screenshots of our First POC *
E® = ~/macos-prt-theft/MacPRThief
[+]
[+]
[+]
[+]
[+]
[+]
./MacPRThief.sh YOURNONCEVALUE
Removing quarantine attributes...
Creating fake codesign...
Creating payload...
Launching FakeChrome as the parent process...
FakeChrome launched. Waiting for BrowserCore...
BrowserCore finished. Waiting for response...
kdzaVJfczBHSk1
cURRaUFYT LE1RH
W1tTDRnQUEiLCI
FeFpOVXkxUGNtZ
bFBUTnpTMLhKRE
kSLFFQLwvd1FNT
QLFBRGdnRUJBSV
2xBVWNZMWowb1J
aVFobD11Z2Nick
UJFZ@VBQUFBREF
ZwdEt@QTNDaGRp
Eoxd LByUGpFWFQ
tzS2hsTLhMNXZR
```

## Slide 31

31

## Slide 32

#### **We Patch the BrowserCore**

32


> Recovered by OCR — confidence 84/100 on the text kept, 59/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
We Patch the BrowserCore
./BrowserCore_patched /tmp/pay load.bin |
Services.AuthorizationError Code=-6000 \"(null)\" UserInto= {NSUnderlyin
gError=0x600003d10060 {Error Domain= M
```

## Slide 33

#### **When we launch it via LLDB**

33


> Recovered by OCR — confidence 94/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
33
When we launch it via LLDB
Preparing sso ext request...
Sending sso ext request...
Waiting for sso ext response...
SSO ext response received.
}] Sending response...
```

## Slide 34

#### Log Diff

❌ Fail:

✅ Success:

34


> Recovered by OCR — confidence 86/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
34
Log Diff
x Fail:
bundleIdentifier: SecTaskCopySigningIdentifier() failed, falling back to man
bundleIdentifier: proc_pidpath() with PID 3324 path: <private>
ntUtils _pathForPid:] 3324 -> /Users/kingkazma/Documents/prt_lab/BrowserCore |
Utils] +[SOAge
Utils] +[SOAgentUtils _pathForPid:] 4794 -> /Users/kingkazma/Document
Utils] 4794: microsa om. browserMessagingHost is managed: NO
ppSSO:SOUtils§ teamIdentifier: UBF8T346G9, Jerror: (null)
```

## Slide 35

#### **How AppSSOAgent Validates its Parent**

**SecTaskCopyIdentifier() csops_task() csops_audittoken() csops_internel() Case Team ID CS_VALID || CS_DEBUGGED**

**AppSSOAgent**

**User Space darling-security/SecTask.c**

**Kernel Space darwin-xnu/kern_proc.c**

35

## Slide 36

☹

#### Actually...

36


> Recovered by OCR — confidence 95/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
36
Actually...®
exec
Developer Tools Access
Developer Tools Access is trying to take
control of another process.
Touch ID or enter your password to
allow this.
T
— csrutil status
System Integrity Protection status: disabled.
```

## Slide 37

#### Two Different Callers in SSO Flow

Caller of BrowserCore
A browser (e.g. Chrome, Edge)
Parent in the parent process check — and this is the part we patched
Caller of AppSSOAgent
BrowserCore (or a similar implementation by third-party vendors)
Requires CS_VALID or CS_DEBUGGED to retrieve the caller’s Team ID

37

## Slide 38

#### Three Techniques We Discovered

⚠ Headless Browser-Based Native Messaging Abuse Requires Specific Environment Conditions

✅ Bypassed BrowserCore’s parent process check Direct SSO Invocation via Apple’s API

38

## Slide 39

39


> Recovered by OCR — confidence 94/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
39
Not in Browser Whitelist
In Browser Whitelist
Team ID Match
(UBF8T346G9)
```

## Slide 40

40

## Slide 41

### Direct SSO Invocation via Apple’s API

41

## Slide 42

#### **Four SSO Methods**

Browser Native Message

Passkey Credential Operation
General SSO Extension Request
Cookie SSO Acquisition

**Check Bundle & Team ID Check Bundle & Team ID**

**Check Only Bundle ID Check Only Bundle ID**

42

## Slide 43

#### **Cookie SSO Acquisition**

**edgeBundleIds (13)**

**thirdPartyBrowserBundleIds (16)**

**nonNativeBrowserBundleIds (10)**

43


> Recovered by OCR — confidence 93/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
43
Cookie SSO Acquisition
°
°
°
°
¢ Bundle IDs:
com.microsoft.edgemac (Edge Stable)
com.microsoft.edgemac.Beta (Edge Beta)
com.microsoft.edgemac.Dev (Edge Dev)
com.microsoft.edgemac.Canary (Edge Canary)
com.google.Chrome (Google Chrome)
org.mozilla. firefox (Mozilla Firefox)
com.apple.Safari (Safari)
com.opera.Opera (Opera)
com. brave.Browser (Brave)
com. yandex. browser (Yandex)
com.microsoft.edgemac.Enterprise (Edge Enterprise)
com.microsoft.edgemac.Nightly (Edge Nightly)
com.microsoft.edgemac.Preview (Edge Preview)
com.microsoft.edgemac.Test (Edge Test)
com.microsoft.edgemac.Experimental (Edge Experimental)
com.microsoft.edgemac.Staging (Edge Staging)
com.microsoft.edgemac.Production (Edge Production)
com.microsoft.edgemac.Release (Edge Release)
com.microsoft.edgemac.Alpha (Edge Alpha)
com.microsoft.edgemac.BetaChannel (Edge Beta Channel)
com.microsoft.edgemac.DevChannel (Edge Dev Channel)
com.microsoft.edgemac.CanaryChannel (Edge Canary Channel)
com.microsoft.edgemac.StableChannel (Edge Stable Channel)
com.microsoft.edgemac.NightlyChannel (Edge Nightly Channel)
com.microsoft.edgemac.PreviewChannel (Edge Preview Channel)
com.microsoft.edgemac.TestChannel (Edge Test Channel)
com.microsoft.edgemac.ExperimentalChannel (Edge Experimental Channel)
com.microsoft.edgemac.InternalChannel (Edge Internal Channel)
com.microsoft.edgemac.StagingChannel (Edge Staging Channel)
com.microsoft.edgemac.ProductionChannel (Edge Production Channel)
com.microsoft.edgemac.ReleaseChannel (Edge Release Channel)
com.microsoft.edgemac.AlphaChannel (Edge Alpha Channel)
```

## Slide 44

#### **Here Comes our Second POC**

44


> Recovered by OCR — confidence 87/100 on the text kept, 51/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
44
Here Comes our Second POC
2025-07-24 11:57:39.639 macprt_directcall[62850:4995978] [RESULT] {
"device_headers" = (
{
header = {
“tenant_id" =
}
“prt_headers" = (
{
header =
zcWhraUcSeFFCQLLIY@IRUVRCSUVRa@VOVEozTW5Ma1ldVUWtnRFpZWHcxREFVQmdzcWhraUcSeFFCQLLJYONBUUZCSUVDUVZNd@V3WUxLb1pJaHZj VUFRVONIQWNFQKFTQKFURXdEUV LKS29aSWh2Y@5BUUVMQ
```

## Slide 45

#### Three Techniques We Discovered

⚠ Headless Browser-Based Native Messaging Abuse

Requires Specific Environment Conditions

✅ Bypassed BrowserCore’s parent process check

✅ Direct SSO Invocation via Apple’s API

45

## Slide 46

PRT Cookie survives only 15 minutes… How can we achieve persistence?

46

## Slide 47

### **$ whoami**

Tung-Lin ‘Echo’ Lee (@iflywithoutwind) Cyber Security Researcher at Speaker at the following technical conferences: FIRST, ROOTCON, HITCON ENT

47

## Slide 48

#### **The Need for Persistence & How to Achieve It**

Why Persistence is Needed ?

PRT Cookie is only valid for a few minutes

How to Achieve Persistence? Abusing device join scenarios Attacker could generate their own PRT Cookie from new device for persistence & bypass conditional access **Registering a new (fake) device requires an access token without a deviceId claim**

48

## Slide 49

#### **Bypassing Conditional Access**

**Require multifactor authentication**

Tokens issued through passwordless authentication also contain the **mfa claim**

To register a WHfB key (Platform Credential on macOS) requires token contain the **ngcmfa claim**

Indicates recent (~10 mins) MFA was performed **Require device to be marked as compliant**

**Pytune** can get the job done (macOS is not supported for now)

49

## Slide 50

#### **Persistence Flow**

Get a Token without deviceId ➜ ➜ Find a way to re-authenticate via MFA (Get ngcmfa claim token) ➜ ✅ ROADtools Register a new (fake) device ➜ Make new (fake) device pass Device Compliance ✅ Pytune ➜ ✅ ROADtools Register new WHfB key

50

## Slide 51

#### **Related Issues that have been fixed**

###### Get a Token without deviceId

➜ **Use SSO tokens for device registration**

Find a way to re-authenticate via MFA (Get ngcmfa claim token) **mfa claim transfer to PRT after registration** ➜

Other related issue

Device overwriting via device ticket

Add new WHFB keys via “searchableDeviceKey” property

“ngcmfa” is not required to provision a key via device registration service

**Ref : https://dirkjanm.io/**

51

## Slide 52

#### **Persistence Flow**

**Get a Token without deviceId** Find a way to re-authenticate via MFA ➜ (Get ngcmfa claim token) ➜ ✅ ROADtools Register a new (fake) device ➜ Make new (fake) device pass Device Compliance ✅ Pytune ➜ ✅ ROADtools Register new WHfB key

52

## Slide 53

#### **Get a Token without deviceId**

###### **Phishing**

**Reset Password**

**Upside:** Does not require compromising the device **Downside:** unreliable

**(Kerberos) Seamless Single Sign On**

**Upside:** used across OS & join types **Downside:** May Triggers alert **Passkey in Microsoft Authenticator**

**Upside:** Keeps the noise level low **Downside:** Less than 25% of tenants have this setting enabled

53

## Slide 54

#### **Reset User Password**

**My Signins:** https://mysignins.microsoft.com/ front end logic login with Access Token login with Access Token (pwd + mfa Claim) **(only mfa Claim)** 👍 **/api/password/reset /api/password/change**

login with Access Token **(only mfa Claim) /api/password/change**

54

## Slide 55

#### **Inconsistent Logic Between Frontend & Backend**

Calling **/api/password/reset** only requires the mfa claim **(pwd claim is not required)**

**HTTP POST https://api.mysignins.microsoft.com/api/password/reset**

55

## Slide 56

#### **Get a Token without deviceId**

**Phishing**

**Reset Password**

**Upside:** Does not require compromising the device **Downside:** unreliable

**(Kerberos) Seamless Single Sign On**

**Upside:** Keeps the noise level low **Downside:** Less than 25% of tenants have this setting enabled

**Upside:** used across OS & join types **Downside:** May Triggers alert **Passkey in Microsoft Authenticator**

**Upside:**

Keeps the noise level relatively low Get a Token with mfa Claim

**Downside:**

Interactive authentication is required

56

## Slide 57

#### **Persistence Flow**

Get a Token without deviceId ➜ ✅ **Find a way to re-authenticate via MFA (Get ngcmfa claim token)** ➜ ✅ ROADtools Register a new (fake) device ➜ Make new (fake) device pass Device Compliance ✅ Pytune ➜ ✅ ROADtools Register new WHfB key

57

## Slide 58

#### **Re-authenticate via MFA**

WHfB Key enrollment token should contain the ngcmfa claim Indicates recent (~10 mins) MFA was performed

**Register New WHfB Key Re-authenticate via MFA (mfa Claim) (ngcmfa)**

58

## Slide 59

#### **Bypass NGCMFA**

Registering a new MFA method requires only the mfa claim in the token **Does not require a token with the ngcmfa claim**

**Register New WHfB Key Re-authenticate via MFA (mfa Claim) (ngcmfa)**

**Bypass**

**Register New MFA Method Register (mfa Claim) Without Re-authenticate**

59

## Slide 60

**ngcmfa Claim**

## Slide 61

Use Stolen Device Credential to Register New Device

Manipulate Auth Info with Stolen Device Credential to Register New Device

61

## Slide 62

#### **Demo: Attack Chain Overview**

**Request PRT cookie through direct SSO invocation Abusing device join scenario to achieve persistence Reset Password**

Get a Token without deviceId Register a new (fake) device (Skip) Make new device pass Device Compliance **Add MFA Method** Register new WHfB key

62

## Slide 63

# **DEMO**

63

## Slide 64

64


> Recovered by OCR — confidence 84/100 on the text kept, 38/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
adelev@AdeleVs-Virtual-Machine macprt % []
```

## Slide 65

#### **User Identity(PRT) + Strong MFA + Fake device**

**+**

**+**

65

## Slide 66

##### **PRT = Lateral Movement between Entra ID Joined Device**

https://troopers.de/troopers25/talks/afv8bw/

66


> Recovered by OCR — confidence 96/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
PRT =
Lateral Movement between Entra ID Joined Device
Hopping Accross Devices: Expanding Lateral
Movement through Pass-the-Certificate Attack
Lateral movement is one of the key factors in Red Team engagements. While various attack methods exist in Active
Directory environments, the options for lateral movement are limited in Entra ID-based environments. However,
the Pass-the-Certificate attack technique introduced by @rubin_mor in 2020 remains a valid option. Through
reverse engineering of undocumented features in Windows, we have confirmed that this technique can be
extended to multiple protocols and can be used to gain access to Entra-joined devices. In some scenarios, it is
even possible to bypass MFA restrictions to move laterally across devices.
```

## Slide 67

#### **Effective Mitigation? (Not Quite)**

Require MFA for “Register or join devices”

Require MFA for “Register security information” Warning: New accounts without MFA enabled are subject to immediate lockout if not accessed via a Temporary Access Pass (TAP) for initial login

67

## Slide 68

#### **Beware Dead Lock!**

Warning: New accounts without MFA enabled are subject to immediate lockout if not accessed via a Temporary Access Pass (TAP) for initial login

You need pass MFA auth to Register MFA

I don’t have MFA, so I need register new one

Deny
But I don’t have MFA!!!!
!

68

## Slide 69

**Even with these CA policies. This is not enough.**

69

## Slide 70

70


> Recovered by OCR — confidence 96/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
70
Phase 1: Initial Compromise
Extract PRT Cookies with MFA
Claim
```

## Slide 71

71


> Recovered by OCR — confidence 93/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
71
Path A: Add New MFA
CA Policy Bypassed:
Policy: 'Adding MFA requires
Logic Flaw: The PRT's
existing MFA claim
satisfies the policy check.
Path B: Reset Password
Credential Check Bypassed:
UI Says: "Requires Current
Password + MFA’.
Logic Flaw: Only require PRT
with MFA.
```

## Slide 72

72


> Recovered by OCR — confidence 94/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
72
Logic Flaw: The PRT's
existing MFA claim
satisfies the policy check.
Logic Flaw: Only require PRT
with MFA.
Attacker MFA Registered
User Password Controlled
|
XS 3: Persisten
Register Attacker Device
```

## Slide 73

73


> Recovered by OCR — confidence 93/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Register Attacker Device
CA Policy Satisfied:
Policy: ‘Device registration
requires MFA’.
Condition Met: Attacker uses
the new MFA
and the new password to
registered or use PassKey
```

## Slide 74

74


> Recovered by OCR — confidence 93/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
74
requires MFA’.
Condition Met: Attacker uses
the new MFA
and the new password to
registered or use PassKey
New Device with PRT & WHfB
```

## Slide 75

#### **MSRC response**

Acknowledged & Patched: VULN-151266

This vulnerability involves the "macOS PRT Cookie" technique. Now this is fixed.

Acknowledged - No Fix Planned: VULN-148636 Upon investigation, we have determined that this is not a vulnerability. This is because we discussed the case details again and determined that **this issue requires having access to someone's device to get their PRT cookie in the first place.** At that point the user is already compromised.

75

## Slide 76

#### Defense methods for macOS PRT Cookie Theft

The vuln has fixed! Update macOS Company Portal. Following the need for continuous monitoring:

Monitor the **codesign** process; it should be running from /usr/bin.

Verify that browser executions are not being simulated by programs such as Python. Detect if a binary has the specified bundle ID (the list mentioned) but lacks a valid signature and trigger an alert.

Ensure Intune's AppPrefixAllowList and AppCookiesSSOAllowList configurations align with expected application usage within your organization.

76

## Slide 77

###### **Summary Our Talk**

PRT cookie theft on macOS is now possible. Other vendors that have implemented SSO extensions on macOS may face similar issues.

For macOS always verify the binary’s team ID, not the bundle ID. No fixed for today persistence methods. Pray for your endpoint . never been compromised and keep monitoring

MSRC responded a week ago, saying they will fix it.

Following might be help you against from persistence technique (Not Quite):

Create Conditional Access use weak criteria  such as IP/Location/UserAgent as requirement to restrict Add MFA or Join Device actions.

Monitor the new joined device and user add new MFA

77

## Slide 78

Tool release:

**Thank You** <u>https://github.com/cycraft-corp/macOS-PRT-Cookies-Theft</u>
