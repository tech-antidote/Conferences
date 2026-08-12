---
title: "Breaching the Perimeter via Cloud Synchronized Browser Settings"
speakers: ["Edward Prior"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2023"
edition: "Europe"
year: 2023
source_pdf: "Black Hat Europe 2023 slides/Edward Prior_Breaching the Perimeter via Cloud Synchronized Browser Settings.pdf"
pages: 58
sha256: "e872d1fc3268924c989d4deb3be06a1fac675e77cc80149ca2a4c68ccfda40d4"
text_chars: 21758
ocr_pages: 23
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:11:50Z"
---
# Breaching the Perimeter via Cloud Synchronized Browser Settings

**Speakers:** Edward Prior  
**Conference:** Black Hat Europe 2023  
**Source:** `Black Hat Europe 2023 slides/Edward Prior_Breaching the Perimeter via Cloud Synchronized Browser Settings.pdf` (58 pages)

## Slide 1

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Diack hat
DECEMBER 4-7
EXCEL LONDON / UK
#BHEU @BlackHatEvents
```

## Slide 2

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
plaek hat
Breaching the Perimeter via Cloud
Synchronized Browser Settings
Edward Prior
#BHEU @BlackHatEvents
```

## Slide 3

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **Cracking the perimeter**

User Credentials

## Slide 4

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **Cracking the perimeter**

Steal Data
VPN Data Repos
Remotely
User  Business  Malware
Mail Servers Code Exec
Credentials Infra Phishing
Compromis
Compromis
e External  Cloud Infra Code Exec
e Cloud Infra
Service

## Slide 5

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **Malicious Links**

What is the worst thing that can happen when a malicious link is clicked?

## Slide 6

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **Malicious Links**

What is the worst thing that can happen when a malicious link is clicked?

- Credential phishing

## Slide 7

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **Malicious Links**

What is the worst thing that can happen when a malicious link is clicked?

- Credential phishing  User interaction

## Slide 8

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **Malicious Links**

What is the worst thing that can happen when a malicious link is clicked?

- Credential phishing  User interaction

- Malware download

## Slide 9

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **Malicious Links**

What is the worst thing that can happen when a malicious link is clicked?

- Credential phishing  User interaction

- Malware download  User interaction

## Slide 10

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **Malicious Links**

What is the worst thing that can happen when a malicious link is clicked?

- Credential phishing  User interaction

- Malware download  User interaction

- Cross-Site Request Forgery

## Slide 11

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **Malicious Links**

What is the worst thing that can happen when a malicious link is clicked?

- Credential phishing  User interaction

- Malware download  User interaction

- Cross-Site Request Forgery  Context

## Slide 12

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **Malicious Links**

What is the worst thing that can happen when a malicious link is clicked?

- Credential phishing  User interaction

- Malware download  User interaction

- Cross-Site Request Forgery  Context

- Browser Exploits

## Slide 13

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **Malicious Links**

What is the worst thing that can happen when a malicious link is clicked?

- Credential phishing  User interaction

- Malware download  User interaction

- Cross-Site Request Forgery  Context

- Browser Exploits  Context

## Slide 14

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

**Todays Goal** Demonstrate how cloud sync gives immense context to an attacker, and the tools to trigger remote payloads unavailable without sync.

## Slide 15

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **Whoami**

- Edward Prior

- @JankhJankh

- Robotics -> Machine Learning -> Pentester/Red Teamer

- OSCP, OSCE, CRTE, ETC.

- 12 CVEs

- CTF Challenge Designer for AIV@DEF CON

## Slide 16

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **Outline**

- Sync Introduction

- Case Studies

- Vuln Demos

- Prevention and Detection

- Automated Emulation

## Slide 17

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **Intro to Cloudsync**

Cloudsync is a feature in every browser to allow for a consistent state between devices.

## Slide 18

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **Intro to Cloudsync**

Cloudsync is a feature in every browser to allow for a consistent state between devices.

Features:

- Synced Settings, Extensions, Passwords, history, and user data

- • Periodically pulls updates from a server

## Slide 19

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **Likelihood of compromise**

- M365

- Google Business Suite

• Personal browser accounts

## Slide 20

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **Case Studies**

All case studies assume a cloud synchronised account on a corporate device has been compromised, and that the browser is being used regularly. Each case study was conducted against a fully patched Chrome, Edge, and Firefox browser.

## Slide 21

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **Case Study 1: Passive Actions**

## Slide 22

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **Case Study 1: Passive Actions**

## Slide 23

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **Case Study 1: Passive Actions**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
CASE STUDIES
Case Study 1: Passive Actions
1 saved passwords
Add password
Website | Username Password Health TL
admin Secretpassword1 S ess
"NON_UNIQUE_! :
"ORIGINATOR_CACHE_ GUID": "”
"ORIGINATOR _CLIENT_ITEM_ID":
"PARENT_ID"
"SERVER_DEFINED_UNIQUE_TAG"
"SPECIFICS": {
’
```

## Slide 24

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **Case Study 1: Passive Actions**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
CASE STUDIES
Case Study 1: Passive Actions
1 saved passwords
Add password
Website | Username Password Health TL
admin Secretpassword1 S ess
"NON_UNIQUE_! :
"ORIGINATOR CACHE GUID": "”
"ORIGINATOR _CLIENT_ITEM_ID”:
"PARENT_ID"
’
"SERVER DEFINED UNIQUE TAG”
"SPECIFICS": {
TITLE TO SECRET SITE</a
```

## Slide 25

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **Case Study 1: Passive Actions**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
CASE STUDIES
Case Study 1: Passive Actions
@ Edge
1 saved passwords
Add password About Data Sync Node Browser
Refresh | Last refresh time: 26/11/2023, 9:18:46 pm
Autofill Title Autofill
Username Password Health N @ - ID null
Autonill Custom Data Modification Time null
Autofill Profiles Parent r
Is Folder true
Type Autofill
External ID null
admin Secretpassword1
Bookmarks
Collection
“NON _UNIQUE_NAME": “cardnumber | 42424242424242", pene es
“ORIGINATOR CACHE GUID": "", ean “now + vautofinn*,
“ORIGINATOR_CLIENT_ITEM_ID": "",
“PARENT_ID": a Edge Hub App Usage
“SERVER_DEFINED_UNIQUE_TAG": Edge Wallet
“SPECIFICS”: {
“autofill": {
"name": “cardnumber",
™ usage t imestamp" : [ History Delete Directives
"13340874180000000" % Nigori
Extension settings
Extensions
Passwords
"value": “42424242424242" preferences
Send Tab To Self
Sessions
Typed URLs
2024&CVV=142&sameadr r title= TI
i" target self i 1uto el referre >TITLE TO SECRET SITE</a>
User Consents
Web Apps
```

## Slide 26

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **Case Study 1: Passive Actions**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
CASE STUDIES
Case Study 1: Passive Actions
Profiles / Passwords
& Try the new management experience in Wallet
Offer to save passwords
Automatically save passwords
Autofill passwords
```

## Slide 27

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **Case Study 2: Forced Navigation**

## Slide 28

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **Case Study 2: Forced Navigation**

## Slide 29

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **Case Study 2: Forced Navigation**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
CASE STUDIES
Case Study 2: Forced Navigation
Bw] Chromel
e Chrome Home TheBrowserby Google Features ~ Safety
Microsoft 365
```

## Slide 30

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **Case Study 3: File Directives**

## Slide 31

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **Case Study 3: File Directives**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Case Study 3: File Directives
2 @ Problem loading page x +
@ file://///192.168.18.128/index.html
Access to the file was denied
The file at ///192.168.18.128/index.html is not readable.
* It may have been removed, moved, or file permissions may be preventing access.
NTLMv2-SSP Client : 197.168.18.129
NTLMv2-SSP Username : .\User
NTLMv2-SSP Hash : User::.:62ec61be6fd3f441: 7I
8271E:61601600000600000008067A3DAB3FBD960162BC599FA/7SES8O7AE
00510001001E00570049004E00200054004400530054004D003 7004
00570049004E002000540044005300540040003700460041005400-
662E604C604F0043004160406000300140044004300470051007Eb0.
0044004300470051002E004C004F00430041004CO0070008 008067!
```

## Slide 32

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **Case Study 3: File Directives**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
CASE STUDIES
Case Study 3: File Directives
2 @® Problem loading page x + " Index of C:\Users\ x +
@ file://///192.168.18.128/index.html Pe € > GC O File | C/Users/ ex &# Oa
Index of C:\Users\
[parent directory]
Access to the file was denied ame Sas
Default
The file at ///192.168.18.128/index.html is not readable. Default User
Jankh
e It may have been removed, moved, or file permissions may be preventing access.
Try Again
NTLMv2-SSP Client
NTLMv2-SSP Username
NTLMv2-SSP Hash
```

## Slide 33

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **Case Study 3: File Directives**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
CASE STUDIES
Case Study 3: File Directives
@® Problem loading page x a
@ file://///192.168.18.128/index.html
Access to the file was denied
The file at ///192.168.18.128/index.html is not readable.
e It may have been removed, moved, or file permissions may be preventing access.
Try Again
NTLMv2-SSP Client
NTLMv2-SSP Username
NTLMv2-S5SP Hash
oe a8
ae
Index of C:\Users\ x +
€ > GC OO File | C/Users/ ex &# Oa
Index of C:\Users\
[parent directory]
Name Size
All Users
Default
Default User
Jankh
Date Modified
5 3:41:31 PM
File Edit Selection Find View Goto Tools Project Preferences Help
—P oprefsjs x
187 user_pref("services.sync.engine.prefs.modified", false);
188 user_pref("services.sync.forms.lastSync", "1701480680.58") ;
189 user_pref("services.sync.forms.syncID", “vKek61Zw-HO2") ;
function user_pref(datal, data2){
}(datal1)
7(data2)
< t src="file:///
C: \Users\User \AppData \Roaming\Mozilla\Firefox\Profiles\@khijcto.default-release\prefs.js"><
nan}
```

## Slide 34

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **Case Study 4: Protocol Handlers**

## Slide 35

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **Case Study 4: Protocol Handlers**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
CASE STUDIES
Case Study 4: Protocol Handlers
i} Microsoft — Cloud, Computers, A x |
'S ia : t www.microsoft.com
Introducing the new Bing, yt This site is trying to open Java(TM) Web Launcher.
Ask real questions. Get complete answei A website wants to open this application.
Microsoft Microsoft 365 Teams
a www.microsoft.com,
Introducing the new Bing, your Al-powered search engine.
Ask real questions. Get complete Chat and create
Do you want to run this application?
Microsoft Mic
Name: Notepad
Publisher: Oracle America, Inc
Location: https://docs.oracle.com
This application will run with unrestricted access which may put your computer and personal
information at risk. Run this application only if you trust the location and publisher above.
Do not show this again for apps from the publisher and location above
```

## Slide 36

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **Case Study 5: Malicious Extensions**

## Slide 37

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **Case Study 5: Malicious Extensions**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
CASE STUDIES
Case Study 5: Malicious Extensions
© \] QO id_rsa x
CGC A
@ File
b3BlbnNzaCirZxktd7jEAAAAABG5vbmUAAAAE bm9uZQAAAAAL
NhAAAAAWEAAQAAAYEAQmZTUJLp/pOwV6Kt2FznAuQw7ny3Ft
t+uk2LkFsUhShIo6Md9Q42F9ZM+MmVwILXIP81tTcoaMdGve@
Wg8irVrBUkb8xk/UJtwqi2RIPu0y3iU46EWzt3GaQgNzF7n;
OgEf9C91DgFFetdmfIKkXEy64gKhdjz3aLETNZULEWSCMRb:
LXiHJw3YpBoUnhxXr@s3K9VYItHCOS289PuP16UL9QR5VCDh
ZRR1fcki76QIFXKPVLy/C6RjZmqIDp74i8KSIU2F8eaGOrr
UbKcGRx6gpYd64NDIJ IAAUCtMZIJ 3hS6C88QIHNdoBz@VG6xXq;
/nDs3WFCaAu61ds19dngOK1rJb3DL2ndpYThk+2HAAAFkDz
EAAAGBAPZmU1Iy6f6dMFeirdn85wLkMO58txes JWQZ4KHEy’
YSKOJHFUONHFWTPJI1cCS1yD/IbU3KGJHRr9MArZDVWPXbz:
/MZP1CbcKotkSD7jst4l00hFs7dxmkIDc3+5+2K3dhZfAc6
RXrXZnySpFxMuulCoxY892tREZcINRMEgjEWyRUaN2RaMN7
FIJ4VE9LNyVVWCLRwjktvPT7j5e1C/UEeVQg4Sa0SgZU+Qr Et
CBVyj1S8vwukY2ZqiA6e+IvCkiFNn/NGhjq619Gx6eGSOV6
HeuDQySAAFArTGSd4UugvPECBzXaAc9FRuL60@NoPCdOM65«
utXbNFXZ4DipayW9wy9p3aWE4ZPt hwAAAAMBAAEAAAGBAMK:
2N7t1kjUBpOyBd+PPxeSxiZMfrWwEQkH@+7ILJeX1QDOHxTW
IK59voQ@0yBSp5B4/02aLu+gbfQz8/ivZaLUKrG4ZW/KGhit
C:/Users/User/.ssh/id_rsa
This page says
id_rsa:PGhObWwgeG1sbnM9IlmhOdHA6Ly93d3cudzMub3JnLzE5OTkv
eGhObWwiPjxoZWFkP)xtZXRhl
G5hbWU9ImNvbG9yLXNjaGVtZSIgY29udGVudD0ibGInaHQgZGFyayl
glz48L2hIYWQ+PGJvZHk+PHByZ
SBzdHIsZTOid29yZC1 3cmFwOiBicmVhay13b3JkOyB3aGl0ZS1zcGFjZTo
gcHJILXdyYXA7Ij4tLSOtl
UJFROIOIE9QRUSTUOggUFIJVkKFURSBLRVktLSOtLQpiMOJs¥m50emFD
MXJaWGt0ZGpFQUFBQUFCRzV2Y
m1VQUFBQUVibTI1WIFBQUFBQUFBQUFCQUFBQmx3QUFBQWRE6Yz)
ndGNuCk50QUFBQUF3RUFBUUFBQVIFQ
TItWIRVakxwL3Awd1Y2S3QyZnpuQXxVRdzdueTNGNndsWkJuZ29jVExJ
Z2NCRZBCdHFNcIkKK3VrMkxrR
rpwZDdVcjITtj04n/zbr/yLjshctPXFvvSoRjKZHDK3xJAimjvsxp/Xb+mOxuzPWS6PHHF
NGc7TLvCt1g29zywWwjpCuiZpRYJzXDWmay8uXaTJz/Wkwn1Pm3zWn9SDaQTdkmrCYHVcqy
Xo0jq8UZJ xyOyNPAj xsuH4kF5@npTAUKUUW29CNU2RVSOAF51/ttLdgqFD1263es/QARiHRF
NNe+JbUME+BuQywZZfRquuKg+Ho6Zj5xYSAyD2i0dFItOJ9VHCrUT1Yk18pAFnGaNXxF96W
JISwjzpHyexkcWdYkW9ywh8ji2qk7jpR1X21bTSk@hywBujCliOreVIfgqgOJGasQemMQAA
```

## Slide 38

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **Summary Of Case Studies**

- Information Theft

- Full control of victim URLs

- Auth coercion

- Viewing local and remote files

- The ability to trigger external applications

## Slide 39

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **Attacks**

## Slide 40

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **Forced Password Theft in Edge**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ATTACKS
Forced Password Theft in Edge
Offer to save passwords
w Microsoft Edge to si
utomatically save passwords
Autofill passwords
n Microsoft Edge to automat
More settings Vv
www.facebook.com
f Q Search Facebook Saved password automatically
Microsoft Edge will save this password to your
Microsoft account
s& Stoy Stunsen Create Story auhdiaudsid|
Share a photo or write something,
7 Castles Place, Melba,
Australian Capital Territory
2615
raywhitecanberr
es Find friends
LS) Feeds s What's on your mind, Stoy?
@ Groups
om.au
Live video (a Photo/video © Feeling/activity @ Limit 1 ry
imit 1 per person
```

## Slide 41

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **Sensitive File Theft via Extensions**

Malicious User is sent to Extension Reads User is redirected User starts browser C:/Users/User/.ssh the page and to their homepage. /id_rsa exfiltrates data

## Slide 42

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **Sensitive File Theft from Share Drive**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ATTACKS
Sensitive File Theft from Share Drive
+
windev2308eval
https
[parent directory]
Name Size Date modified
screensavers 29/10/2023, 07:27:0
vpnsetup. bat 22B 29/10/2023, 07:33:
vpnsetup.ps1 34B 29/10/2023, 07:33:
x £0
oR)
vpnsetup.bat
vpnsetup.ps1
```

## Slide 43

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **Sensitive File Theft from Share Drive**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ATTACKS
Sensitive File Theft from Share Drive
\\192.168.18.128\demoshare x =e
S aN g @ > Network > 192.168.18.128 > demoshare Search demoshare Q
@ New WN. Sort C3 Details
} Home
A Gallery © test.html
@ Roy - Personal |
€ > GA @ File | 192.168.18.128/d
Test Share Drive Exfiltration
Q tpy © Default levels ¥ @7
accessibility.typeaheadfind.flashBar
e
app.installation.timestamp
133408090843795707
```

## Slide 44

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **Malware Dropping Via XSS**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ATTACKS
Malware Dropping Via XSS
@ How to update - Google Chro x +
€ Cf :~google.com.au/intl/en_au/chrome/update,
ing Sta //google.com/ //google.com/ ported . —
® Getting Started @ https://google.com/1 https://google.com/2 Imported From Fire. ] ChromeUpdate.exe
Chrome Home TheBrowserby Google Features v Safety v
Google uses cookies to deliver its services, to personalise ads, and to analyse traffic. You can adjust your privacy controls anytime in your Google sett
Chrome keeps you up
to date
Chrome updates happen in the background automatically —
keeping you running smoothly and securely with the latest features.
Ok, got it
```

## Slide 45

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **Malware Dropping Via DOM Modification**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ATTACKS
alware Dropping Via DOM Modification
€ > CG  & google.com.su
chrome
button.chr-cta_button.chr-cta_b
utton--blue.show
```

## Slide 46

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **RCE via Protocol Handler Vuln**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ATTACKS
RCE via Protocol Handler Vuln
@ Untitled x +
CC @ ms-msdt:test&calc
@ Getting Started @ https://googlecom/1 G ht
Open Windows Command Processor?
A website wants to open this application.
Open Windows Command Processor
```

## Slide 47

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **Leveraging Credentials and Context**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ATTACKS
Leveraging Credentials and Context
Oo
Ga
C2 Import favorites
@ New tat
SE Microsoft Start
Dal ~ Recent
Yesterday - Friday, No
Microsoft account
1 saved passwords
Website J Username Password Health
admin etpassword1
```

## Slide 48

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **Leveraging Credentials and Context**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ATTACKS
Leveraging Credentials and Context
© (ts) al Apache Tomcat/9.0.82
Es |
G Aa
Calculator
Standard 59
Home Doc Find Help
Apache T APACHE
Server Status
Manager App
Host Manager
Developer ¢
Tomcat Setup Servlet Specifications
First Web Appli Tomcat Versions
Managing Getting Help
For security, aq , FAQ and Mailing Lists
```

## Slide 49

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **Desktop Credential Compromise**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
: Desktop Credential Compromise
NTLMv2-SSP Client
: 192.168.18.129
NTLMv2-SSP Username : .\User
NTLMv2-SS5P Hash : User::.:62ec6ibe6fd3f441: 7!
8271E:0101000000000000806 7A3DAB3FBD90162BC599FA/5E807AC
06510001001E90570049004E06020D0054004400530054004D003 700
0057004900456002000540044005300540040003700460041005400:
002E004C004F00430041004C000300140044004300470051002E00:
600440043004 70051002E004C004F00430041004C008 70008008067:
PS C:\Users\User\Desktop\hashcat-6.1.1> .\hashcat.exe -a 0 -m $600 .\hash.txt .\rockyou.txt -w 3 -O
hashcat (v6.1.1) starting...
OpencL API (Opencl 2.1 AMD-APP (3516.0)) - Platform #1 [Advanced Micro Devices, Inc.]
* Device #1: Ellesmere, 8128/8192 MB (6745 MB allocatable), 32McU
Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 27
Hashes: 1 BLpee ES: 1 unique digests, 1 unique salts
piemaps: 16 bits, 65536 entries, OxO000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1
Applicable optimizers applied;
* Optimized-Kernel
* Zero-Byte
* Not-Iterated
* single-Hash
* Single-Salt
Watchdog: Temperature abort trigger set to 90c
Host memory required for this attack: 626 MB
Dictionary cache hit:
* Filename..: .\rockyou.txt
* Passwords.: 14345042
* Bytes.....: 139927340
* Keyspace..: 14345042
USER: : . :62ec61be6fd3f441: 7fad17e80b2bb6146ede37a40548271e : 0101000000000000806 7a3dab3fbd90162bc599fa
2d00540044005 30054004d00370046004100540049004c00040034005 70049004e002d0054004400530054004d003700460'
00030014004a004300470051002e004c004F00430041004c00050014004a004300470051002e004c004F00430041004c000
00000100000000200000a74a588690d6960504aa1d55f090070980ea44ea4615 Sbbe709a8c885673a3F60a0010000000000)
0032002€003100360038002e00310038002e003100320038000000000000000000: Password1
```

## Slide 50

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **RCE via WinRM Request Forgery**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ATTACKS
RCE via WinRM Request Forgery
© 0 O Not Found
CG A G) _ localhost:5985
fa Calculator
= Standard 59
Not Found
HTTP Error 404. The requested resource is not found.
```

## Slide 51

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **Lateral Movement**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ATTACKS
Lateral Movement
User > AppData > Local > Mozilla > Firefox > Profiles
Name Date modified Type
Quick access
9x22n1oc.default
File folder
@ OneDrive - Personal FirefoxSync
~@ This PC kzdgxsxs.default-release
File folder
yzvj2z34.EdgeSync File folder
```

## Slide 52

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **Summary of Attacks**

- Information Theft

- Full control of victim URLs

- Auth coercion

- Viewing local and remote files

- The ability to trigger external applications

- Request Forgery attacks that circumvent SOP.

- Lateral movement

## Slide 53

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **Prevention**

Disable setting sync on all browsers at a both a cloud and device level.

Harden browser settings via group policy.

<u>Decouple your password manager from your browser.</u>

Other recommendations:

- Investigate any other browsers in use in the organisation.

- Investigate if personal browser accounts are being used within the organisation.

## Slide 54

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **Detection**

Alert on anomalous logins and actions within your external services. Periodically scan your enterprise for malicious extensions. Investigate anomalous browser subprocessess. Alert on excessive network activity (port scanning).

## Slide 55

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **Automated Emulation**

## Automated emulation tool written in .NET.

Enables Sync In Malicious Browsers, and adds Periodically Opens Extension Reads a malicious the Browser the sync config to extension inform attacks Conducts malicious activity

https://github.com/JankhJankh/Syncy

## Slide 56

**Conclusion / Black Hat Europe Sound Bytes** Sync provides remote attackers with significant context into an enterprise environment, and some unique ways of leveraging that context to crack the perimeter.

## Slide 57

**Conclusion / Black Hat Europe Sound Bytes** Sync provides remote attackers with significant context into an enterprise environment, and some unique ways of leveraging that context to crack the perimeter.

Disable sync in enterprise environments.

Consider Syncy for your next attack simulation.

## Slide 58

# **Questions?**

Edward Prior at Aegis9 Socials: @JankhJankh Syncy: https://github.com/JankhJankh/Syncy Whitepaper: Available on briefing page
