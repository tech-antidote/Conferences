---
title: "DriveThru Car Hacking Fast Food, Faster Data Breach"
speakers: ["Alina Tan", "George Chen", "Chee Peng Tan", "Ri-Sheng Tan", "Penelope Chua", "Benjamin Cao"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2025"
edition: "ASIA"
year: 2025
source_pdf: "Black Hat Asia 2025 Slides/Alina Tan & George Chen & Chee Peng Tan & Ri-Sheng Tan & Penelope Chua & Benjamin Cao_DriveThru Car Hacking Fast Food, Faster Data Breach.pdf"
pages: 43
sha256: "da63743605dc95aa9de418347fe53c70a60e841e2f3786e8422fc5ccf71c256e"
text_chars: 19036
ocr_pages: 1
has_ocr: true
redacted_secrets: 0
ocr_confidence: 90.4
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T01:39:53Z"
---
# DriveThru Car Hacking Fast Food, Faster Data Breach

**Speakers:** Alina Tan, George Chen, Chee Peng Tan, Ri-Sheng Tan, Penelope Chua, Benjamin Cao  
**Conference:** Black Hat ASIA 2025  
**Source:** `Black Hat Asia 2025 Slides/Alina Tan & George Chen & Chee Peng Tan & Ri-Sheng Tan & Penelope Chua & Benjamin Cao_DriveThru Car Hacking Fast Food, Faster Data Breach.pdf` (43 pages)


## Slide 1

# **DriveThru Car Hacking Fast Food, Faster Data Breach**

Speakers: Alina Tan, George Chen Contributors: Chee Peng Tan, Ri-Sheng Tan, Penelope Chua, Benjamin Cao

#BHAS @BlackHatEvents

## Slide 2

### Speakers

Alina Tan

George Chen

Car Person

Lego Person

#BHAS @BlackHatEvents

## Slide 3

### Contributors

Chee Peng Tan

Penelope Chua

Ri-Sheng Tan

Benjamin Cao

#BHAS @BlackHatEvents

## Slide 4

## Teaser

#BHAS @BlackHatEvents

## Slide 5

### Background

Dashcams have become a necessary accessory for car ownership. Out of every 10 cars, at least 8 are installed with dashcams.

In Singapore, IROAD dashcams emerge as the most popular, making up nearly half of the dashcams found in our research, with 70mai coming in second, representing about one-tenth of the data.

**Many dashcams share similar hardware and even possibly software.**

Dongguan Electronics –
Developed Mobile
applications for handling
OEM Makers for
Wifi connections to
several continental
dashcams
car brands
IROAD and GNET –
Similar Manufacturers
Thinkware
Blackvue

#BHAS @BlackHatEvents

## Slide 6

### Collecting 1k+ Dashcam SSIDs

Brand “X”

_Dashcam Brand Distribution (*Based on Discoverable SSIDs)_

Marauder

Tested over 2 dozen models
across 15 brands

#BHAS @BlackHatEvents

## Slide 7

### Models

Brand “X”

We bought 20 dashcams as our initial training data set to build our tool, which we then use to test on 40 participants’ dashcams.

_Count of Models_

#BHAS @BlackHatEvents

## Slide 8

### Technique: DriveThru Hacking

discover
connect
bypass Extending  wardriving  to
mute access dashcams and
stream media files into an
auth
LLM pipeline for insights.
dump
sabotage
extract
process
insights

#BHAS @BlackHatEvents

## Slide 9

### Attack Flow

|**Dashcam Model***
**Highlight**|**Attack Stage**|
|---|---|
|J|**1**
**Discover**– dashcam SSIDs|
|J, K, E, F, H, P|**2**
**Connect**– using default/fixed/common passwords (fallback→traditional cracking of handshake captures)|
|J, K, E, F, H, P, C|**3**
**Bypass**– device registration or physical pairing|
|C|**4**
**Mute**– dashcam sounds during the attack (if applicable)|
|all|**5**
**Authenticate** – file storage services using hardcoded credentials found in APKs/firmware (if applicable)|
|B, O|**6**
**Dump** – all videos, audio, meta data such as GPS data|
|K, G, L|**7**
**Sabotage** – change configurations such as disabling recording, deleting footage, or sabotaging the car battery|
|I|**8**
**Extract** – key video frames containing landmarks and road signs to infer point-in-time location (if GPS data isn’t available)|
|I|**9**
**Process**– and transcribe audio, identifying background music and summarizing key conversations via LLM|
|I, M|**10**
**Insights** – generated using driving routes, lifestyle patterns, and conversational topics, presenting them to the car owner at the
end of the drivethru|

*a brand can have multiple models

#BHAS @BlackHatEvents

## Slide 10

#### 1. Dashcam SSID Discovery

**Dashcam: J**

DriveThru Hacker Scans Connects

Extract #BHAS @BlackHatEventsProcess Insights

Auth Dump Sabotage

Discover Connect Bypass

Mute

## Slide 11

#### 2. Connect via Default Passwords

Unique
no
Dashcam D
8 lower letters exactly
1 (Random)1 11 Changed? Common?
yes
yes yes no
yes
2 dozen models
Common
Default
15 brands Unique? Editable?
password Default
no, same for all no, fixed
DriveThru
14 4 (Fixed)4
Hacker
•
Default password
anyone can connect
•
Fixed password
to these dashcams’
•
Common password
networks perpetually
In scope
Out-of-scope
Discover Connect Bypass Mute Auth Dump Sabotage Extract #BHAS @BlackHatEventsProcess Insights

## Slide 12

#### 2. Connect via Default Passwords

<u>Internal Domain Name</u>

**Dashcam: J, K, E, F, H, P**

> #BHAS @BlackHatEventsProcess Insights

Connect

Sabotage Extract

Discover

Bypass

Mute

Auth

Dump

## Slide 13

#### 3. Bypass Device Pairing - #1

This is how device pairing on Dashcam C’s app looks like

**Dashcam: C**

Sabotage Extract #BHAS @BlackHatEventsProcess Insights

Connect

Discover

Bypass

Mute

Auth

Dump

## Slide 14

#### 3. Bypass Device Pairing - #1

**Dashcam: C**

But if we skip this and connect directly to the http server

Dump Sabotage Extract #BHAS @BlackHatEventsProcess Insights

Discover Connect Bypass

Mute

Auth

## Slide 15

#### 3. Bypass Device Pairing - #2

**Dashcam: J, K, E, F, H, P (Fixed passwords)**

Device pairing requires the physical pushing of the WiFi button, which then “unlocks” the dashcam for pairing.

The dashcam then remembers the MAC address of the trusted device/phone.

Attack:

1. Obtain MAC address of trusted device via ARP scanning

2. Spoofing that MAC address

Auth

> #BHAS @BlackHatEventsProcess Insights

Discover Connect

Sabotage

Bypass

Mute

Dump

Extract

## Slide 16

#### 3. “Bypass” Device Pairing - #3

**Dashcam: J, K, E, F, H, P (Fixed passwords)**

prompt user for pairing

“Press the WiFi button to register the smartphone”

DriveThru Hacker

Dump Sabotage Extract #BHAS @BlackHatEventsProcess Insights

Discover Connect

Bypass

Mute

Auth

## Slide 17

#### 4. Muting Voice Guidance

**Dashcam: C**

If hacking activity triggers dashcam voice over, we can mute it temporarily during the attack via an additional API call.

Extract #BHAS @BlackHatEventsProcess Insights

Discover Connect

Dump Sabotage

Bypass

Mute

Auth

## Slide 18

#### 5. Authentication against Services

|Dashcam Models / Ports|FTP|Telnet|http & proxy|RPC|RTSP|API|TCP|Video|Audio|ADB|
|---|---|---|---|---|---|---|---|---|---|---|
|A (4 x budget cams)|21||80, 8080||554, 8080|80, 3333|8081||||
|B|||80|||7777|53|7778|7779||
|O|||80|||7777|53|7778|7779||
|D|||80|111|||||||
|C|||80||554|80|||||
|G|||80||554|80|||||
|L||23|80||554|80|||||
|M||23||111|554||53||||
|I|21||||554||||||
|E|21||||9092||9091||||
|F|||||9092||9091||||
|H|||||9092||9091||||
|J|||||9092||9091||||
|P|||||9092||9091||||
|K|||80, 8080||8554|||||5037|

Credentials found in APKs: **FTP, Telnet, API, RTSP**

Dump Sabotage Extract #BHAS @BlackHatEventsProcess Insights

Discover Connect Bypass Mute

Auth

## Slide 19

#### 6. Dump out Video, Audio, GPS

Dashcam: B, O
lists files for ‘Drive’, ‘Event’, ‘Park’, ‘Photo’
returns list of files
7777
sends byte sequences 1 – 14 to open  API
ports 7778 (video) & 7779 (audio)
DriveThru
Hacker sends video 7778
Video
sends audio 7779
Audio
merge video & audio
Discover Connect Bypass Mute Auth Dump Sabotage Extract #BHAS @BlackHatEventsProcess Insights

## Slide 20

#### 7. Sabotage and PWNZ Remotely

1. Create web shell

**Dashcam: K**

3. Execute commands (RCE)

4. Crack root 2. Upload web shell password

Dump Sabotage Extract #BHAS @BlackHatEventsProcess Insights

Discover Connect Bypass

Mute

Auth

## Slide 21

#### 7. Sabotage and PWNZ Remotely

Change URLs

Disable battery protection to sabotage car battery

Mute

Change “fixed” password

**Dashcam: K**

Reverse shell

BRICKED : (

Sabotage Extract #BHAS @BlackHatEventsProcess Insights

Discover Connect

Bypass

Auth

Dump

## Slide 22

#### 7. Sabotage and PWNZ Remotely

Dashcam: G
Unauthenticated Upload
Discover Connect Bypass Mute Auth Dump Sabotage Extract #BHAS @BlackHatEventsProcess Insights

## Slide 23

#### 7. Sabotage and PWNZ Remotely

**Dashcam: Q**

DoS

Auth Dump Sabotage Extract #BHAS @BlackHatEventsProcess Insights

Discover Connect

Bypass

Mute

## Slide 24

#### 7. Sabotage and PWNZ Remotely

Credentials found in Firmware **Dashcam: L** Root dd jefferson

Discover Connect Bypass Mute Auth Dump Sabotage Extract #BHAS @BlackHatEventsProcess Insights

## Slide 25

#### 8. Extract Road Signs and Detect Location

1. Extract video frames with timestamp

2. Detect road signs from frames

   3. Apply OCR and extract text

4. Process with OpenAI for GPS coordinates

Extract #BHAS @BlackHatEventsProcess Insights

Discover Connect

Sabotage

Bypass

Mute

Auth

Dump

## Slide 26

#### 9. Process Video & Audio via LLM

**1. Shazam** used to identify songs in audio

```
STICKY
KISS OF LIFE
```

**2. OpenAI Whisper** used for transcription

**3. OpenAI** used to summarize insights in text and comic form

Extract #BHAS @BlackHatEventsProcess Insights

Discover Connect

Dump Sabotage

Bypass

Mute

Auth

## Slide 27

#### 10. Insights

Discover Connect Bypass Mute Auth Dump Sabotage Extract #BHAS @BlackHatEventsProcess Insights

> Text below was recovered by OCR (confidence 90/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
10. Insights
ty OVERALL INSIGHTS
~ Expansion into Europe scheduled for Q3. - New product line focusing on renewable energy. -
Partnership discussions with top five tech firms. - Strategic investment in Ri-driven analytics. -
Confidential talks on potential merger with rival.
```

## Slide 28

### Hacking 40 Participants’ Dashcams

#BHAS @BlackHatEvents

## Slide 29

### Insight Dashboard – Participant X

1

Dataset 2: Participant #2

Dashcam owner conversing with his family members, discussing their upcoming plans for Ramadan. The car drove from Yishun to Ang Mo Kio.

#BHAS @BlackHatEvents

## Slide 30

### Insight Dashboard – Participant Y

2

Dataset 3: Participant #3 Dashcam owner appears to have been listening to the news, summarizing world events. The car drove from Clementi to HarbourFront.

#BHAS @BlackHatEvents

## Slide 31

### Participants-Hacking Results

|**Participant #**|**Count**|**Dashcam Model(s)**|**Hacking Result**|**Key Reason**|
|---|---|---|---|---|
|11|1|J|Successful|Owner’s phone was connected|
|1, 3, 4, 5, 13,
14, 18, 19, 24,
26|10|I, G, A, B, C, Q|Successful|Same config and model as our training dashcams|
|2, 6, 8, 9, 12,
16, 21-23, 25,
31, 33, 34, 40|14|J, Q, S, T, Q, X, Y, Z|Failed|Script broke because of model or configuration
differences|
|7, 27, 29, 32,
35, 37-39|8|J, N, U, W, E, H|Failed|Owner's phone was not connected|
|10, 15, 17, 20,
28, 30, 36|7|V, A, C, M|Failed|Default password was changed|

#### Exploitability: 11/40*

*based on selected brands in scope

#BHAS @BlackHatEvents

## Slide 32

#### Cloud – It Gets Better

T&C “By sharing your Live View, you can let other users vicariously experience the excitement and pleasure of driving all over the world…”

Feed 1 Car owner in front: Can I use your cashcard? I’ll pay you back, mine doesn’t work.

Dashcam owner helps and says no need to pay back, then drives home into his garage (landed property) where his house and address is visible.

###### **Dashcam: D**

Feed 2 A private hire picks up tourists from neighboring country.

They talked between themselves on that evening’s chicken rice dinner but were afraid of putting on weight and started sharing related tips including certain digestion and slimming products and how it #BHAS @BlackHatEvents worked on their common contacts.

## Slide 33

### Hacking Approach

“client-side documentation”
APK
“server-side documentation”
Firmware
nmap
New Dashcam Desktop  Proxy
Black Box
X App? no App? no
Automation
Manual Probe
Script X
yes
yes
Script
Sniff
Robustness
against
Variations
Test on
Participants
#BHAS @BlackHatEvents

#BHAS @BlackHatEvents

## Slide 34

### Vulnerability Summary

|**Visible Market Share of**
**Brands on SG Roads***|**Tested Dashcam**
**Model(s)**|**Main Exploited Vulnerability**|**Criteria for Compromise**|
|---|---|---|---|
|~48.6%|J, K, N, P|||
|~6.7%|H|**Bass device reistration/airin (device level)**|**Paired device needs to be connected**to|
|~5.6%|E|**yp  gpg**|dashcam network|
|~3.0%|F|||
|~4.4%|D|All files exposed via**unauthenticated http**|Default 8-char lower-case alphabetical
password to be**cracked from handshake**|
|~12.5%|C|Bypass**app pairing (app level)**||
|~2.6%|B, O|All files exposed via unauthenticated custom ports||
|~2.6%|M|**Pairing can be bypassed**when connected via
**unauthenticated telnet (network level)**||
|~2.3%|I|All files exposed via**FTP**that’s authenticated with
plaintext password from APK|**Password needs to be default**/common|
|<2.0%|A|All files exposed via**unauthenticated FTP**and custom
ports||
|<0.5%
<0.5%|G
L|All files exposed via unauthenticated http||

* only selected models of each brand are tested; it’s possible that vulnerabilities differ for other models.

#BHAS @BlackHatEvents

## Slide 35

### Manufacturer Disclosure

Brand “X” acknowledged accepted mitigated fixing fixing informed informed informed informed informed informed informed

Out of 15 brands: ----------------------------------------------------------------------------------------dedicated security email inbox: 1 generic contact email/form: 11 no ways of contact: 3 budget cams (brandless) ----------------------------------------------------------------------------------------ack: 5 (1 mitigated, 2 fixing) implementing psirt/vdp/bb: 1

#BHAS @BlackHatEvents

## Slide 36

### Assigned CVEs

|**Brands/Stage**|**Connect**|**Bypass**|**Auth**|**Dump**|**Upload**|**Sabotage**|**Priv Esc / Sniff**|
|---|---|---|---|---|---|---|---|
|Marbella|CVE-2025-30125||CVE-2025-30124|CVE-2025-30127||CVE-2025-30126||
|70mai|Pending|CVE-2025-30112|Pending|Pending|Pending|Pending|Pending|
|BlackVue|||CVE-2025-2355||Pending|Pending|CVE-2025-2356|
|GNET|CVE-2025-30139|CVE-2025-30142|CVE-2025-30137|CVE-2025-30141||CVE-2025-30138|CVE-2025-30140|
|YI Smart Dash Cam||||CVE-2024-56897||||
|I-Drive|CVE-2025-1878|CVE-2025-1880|CVE-2025-1879|CVE-2025-1881||CVE-2025-1882||
|IROAD X, Q series|CVE-2025-2341|CVE-2025-2343,
Pending|CVE-2025-2342,
CVE-2025-30108|CVE-2025-2344||CVE-2025-2345|CVE-2025-2346|
|IROAD FX series||CVE-2025-2347||CVE-2025-2348|CVE-2025-2350|CVE-2025-30133,
CVE-2025-30135|CVE-2025-2349,
CVE-2025-30131|
|HikVision|Pending||Pending|Pending|||Pending|
|Thinkware|CVE-2025-2120|CVE-2025-2119|CVE-2024-53614||CVE-2025-2121|CVE-2025-2122||
|”Brand X”|CVE-2025-30115|CVE-2025-30114|CVE-2025-30113|CVE-2025-30116||CVE-2025-30117||
|Audi|CVE-2025-30118||CVE-2025-2555|CVE-2025-2556||CVE-2025-2557||
|ROADCAM|||CVE-2025-30123|||||
|SAFECAM|||Pending|||||

#BHAS @BlackHatEvents

## Slide 37

### Lateral Movement

1 2
Perform analysis on the
Establishing the
mobile application
connection between the
provided by the OEM
dash camera and perform
manufacturer
MiTM

3 4
Inject malicious exploit  Perform lateral movement
and compromise  towards the vehicular
infotainment system network once
infotainment system is
compromised

#BHAS @BlackHatEvents

## Slide 38

### Lateral Movement

1 2 3 4
Access infotainment
Obtain root privilege to
system to exploit
upload modified firmware
vulnerabilities
Spoof connectivity of the  Initiate a MiTM Wi-Fi
dashcam to the phone  connection through the
Issue CAN commands to  Perform lateral movement
app app
the vehicle (i.e. remote  to access the CAN
start) network
Issue CAN commands to
ECU

#BHAS @BlackHatEvents

## Slide 39

### Key Problems & Processes

##### **<u>Unique structured connection process</u>**

Some dashcam manufacturers expose the SSID, however a unique structured connection process is in place to prevent 1 2 data from being exposed to the public 3 4 **<u>Weak device pairing</u>** Some manufacturers allow connection to dashcams without going through the device-pairing flow

##### **<u>Lack of secure protocols</u>**

Some manufacturers allow the usage of SSID and password change, however, insecure protocols are exposed as part of the running services

**<u>Lack of firmware updates and security patches</u>** As opposed to traditional computers, firmware and security updates are infrequent and not common for dashcams

#BHAS @BlackHatEvents

## Slide 40

### Recommendations for Securing Dashcams

##### **<u>Adopt secure-by-design and secure-by-default principles</u>**

Some dashcam models restrict changing default passwords, posing a security risk despite having a structured connection process. Manufacturers should adopt a Secure-by-Design approach by:

- Ensuring users can set strong and unique passwords.

- Preventing unauthorized remote pairing through encryption and challenge-response mechanisms.

- Usage of Secure APIs – Ensuring only authorised clients connect to the server using API keys.

Secure authentication protocols

Encryption

Firmware updates

##### **<u>Attack surface reduction</u>**

- Reducing attack surface areas such as exposure of SSIDs to the public (i.e. switching it to non broadcast).

- Perform threat modelling by identifying the possibilities of different attack scenarios.

##### **<u>Secure Authentication and encryption practices</u>**

- Usage of proper authentication and encryption protocols (i.e. passwords are properly hashed and don’t appear in plain text).

Secure-by-Design/Secure-by-Default

Attack surface reduction

Privacy

- Certificate based pairing.

#BHAS @BlackHatEvents

## Slide 41

### Recommendations for Securing Dashcams

##### **<u>Dashcams connected to cloud – Connected dashcams (Privacy concerns)</u>**

- Connected dashcams that are connected to cloud should have built-in security protocols instead of allowing anyone to stream or access the web page freely.

- Consider implementation of 2 factor authentication to access data stored in cloud.

- Consider implementation of TLS 1.2/1.3 or even mTLS between server and client authentication.

##### **<u>Firmware updates</u>**

- Manufacturers can consider delivering firmware updates via the app through OTA using secure protocols or allowing firmware updates to be available on websites for authenticated consumers to download and update the firmware via USB connectivity.

- Firmware updates can often be prompted through the phone application itself to inform consumers that there are firmware updates related to security vulnerabilities.

##### **<u>Bug Bounty/Vulnerability Disclosure Program (VDP)</u>**

Secure authentication protocols

Encryption

Firmware updates

Secure-by-Design/Secure-by-Default

Attack surface reduction

Privacy

- Manufacturers should consider providing a dedicated email address for reporting vulnerabilities. Additionally, implementing a bug bounty program or a Vulnerability Disclosure Program (VDP) can further enhance the security of their products.

#BHAS @BlackHatEvents

## Slide 42

### Potential Partnerships and Next Steps

Identify Attack Vectors Analyze vulnerabilities in firmware, weak authentication, and remote exploits

Simulate & Test Exploits Conduct penetration testing and real-world security assessments

Develop Mitigation Strategies Implement encryption, secure pairing, and stronger authentication methods

Collaborate with Stakeholders

Work with manufacturers, regulators, and wider cybersecurity community

Security of dashcams are often overlooked, and to advance research on dashcam security, we hope to **establish potential partnerships with OEM, automotive manufacturers, regulators, and the wider cybersecurity community** to strengthen the overall security posture of vehicles and ensure a safer and resilient automotive ecosystem.

Our next steps include **analysing and testing out attack vectors** that could allow dashcams to serve as entry points for vehicle-wide cyber threats, **developing mitigation strategies such as intrusion detection systems** , and **proposing security frameworks that align with security design principles** .

Implement & Monitor Security Enhancements Deploy intrusion detection systems and regulatory compliance measures

#BHAS @BlackHatEvents

## Slide 43

# **DriveThru Car Hacking Black Hat Asia Sound Bytes – Key Takeaways:**

1. Dashcams are easy targets: private conversations & routes can be compromised within minutes 2. Adopt secure-by-design: build security into products and ensure seamless patch delivery post-shipping

3. Security through collaboration: VDP, BB, & PSIRT help manufacturers identify vulnerabilities earlier

info@heatsecuritylabs.com

#BHAS @BlackHatEvents
