---
title: "Recording PCAPs from Stingrays With a $20 Hotspot"
speakers: ["Cooper Quintin"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33/Cooper Quintin -Recording PCAPs from Stingrays With a $20 Hotspot.pdf"
pages: 51
sha256: "ead0fcb738bf02a0351f13e2dcb404e8be4dbb7b89a082f3ec482b04c307a015"
text_chars: 25184
ocr_pages: 9
has_ocr: true
redacted_secrets: 0
ocr_confidence: 87.7
ocr_unreliable_blocks: 5
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:57:32Z"
---
# Recording PCAPs from Stingrays With a $20 Hotspot

**Speakers:** Cooper Quintin  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33/Cooper Quintin -Recording PCAPs from Stingrays With a $20 Hotspot.pdf` (51 pages)


## Slide 1

<Location **<location, date>** , date>DEF CON 33

# **Detecting Fake 4G Base Stations for $20 with Rayhunter**

Cooper Quintin - Senior Staff Technologist - EFF Will Greenberg - Senior Staff Technologist - EFF oopsbagel - Rayhunter Maintainer DEF CON 33 - August 2025

## Slide 2

<Location **<location, date>** , date>DEF CON 33

# **Intro**

- **Cooper Quintin (he/him)** – Senior Staff Technologist

- – At EFF for 10 years

   - Privacy Badger, malware, SLS, Threat Lab, phones

- **oopsbagel (nieźle/toveri)** – Rayhunter Maintainer

- – ECE, software development, both kinds of SRE, netsec, cloudsec

- – Does not work for EFF

## Slide 3

<Location **<location, date>** , date>DEF CON 33

# **Shout Out**

**Will Greenberg**

● **Co-creator of this research** ● **Couldn’t be here** ● **Please give him a round of applause**

## Slide 4

<Location **<location, date>** , date>DEF CON 33

# **Stingray AKA IMSI Catcher AKA Cell-Site Simulator**

## Slide 5

<Location **<location, date>** , date>DEF CON 33

# **Previous Efforts to Detect CSS**

## Slide 6

<Location **<location, date>** , date>DEF CON 33

## Slide 7

<Location **<location, date>** , date>DEF CON 33

# **Goals**

**1. Determine how how often CSS are being used. 2. Determine what kind of attacks modern CSS use. 3. Figure out if we can detect modern CSS reliably.**

## Slide 8

<Location **<location, date>** , date>DEF CON 33

# **How Often are CSS Being Used**

**• Foreign Spies** – <u>IMSI Catchers in DC</u>

**• Cyber Mercenaries** – NSO Group <u>https://www.amnestyusa.org/wp-content/uploads/2020/06/Moro cco-NSO-Group-report.pdf</u>

## Slide 9

<Location **<location, date>** , date>DEF CON 33

# **How Often are CSS Being Used**

- **ICE/DHS - hundreds of times per year** irm

   - <u>https://www.aclu.org/news/immigrants-rights/ice-records-confirm</u> -that-immigration-enforcement-agencies-are-using-invasive-cell-p <u>hone-surveillance-devices/</u>

- **Local law enforcement**

   - Fontana, CA police dept. used theirs > 300 times in 2022-2023

      - Have purchased three cell site simulators

   - Santa Bernardino PD - 231 times in 2017

      - <u>https://www.eff.org/deeplinks/2019/05/eff-asks-san-bernardino-court-rev iew-device-search-and-cell-site-simulator</u>

## Slide 10

<Location **<location, date>** , date>DEF CON 33

# **Law Enforcement with CSS**

**<u>Atlas of Surveillance</u>**


> Recovered by OCR — confidence 83/100 on the text kept, 57/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Law Enforcement with CSS
Calgary
Vancouver
Seattle
Ottawa
° 3’ York
€ Francisco °
oe Dallas °
Monterrey er
MEXICO Havana
Atlas of Surveillance
```

## Slide 11

<Location **<location, date>** , date>DEF CON 33

**How Often are CSS Being Used**

**• Crime!**

– <u>https://commsrisk.com/paris-imsi-catcher-mistaken-for-bomb-wa s-actually-used-for-health-insurance-sms-phishing-scam/</u>

## Slide 12

<Location **<location, date>** , date>DEF CON 33

# **How do 4G CSS Work**

- **What are the vulns next gen CSS are taking advantage of?**

**<u>Gotta catch em all whitepaper by Advisory Board member Yomna</u>**

## Slide 13

<Location **<location, date>** , date>DEF CON 33

# **Pre-Authentication Vulnerabilities**

- **4G has a glass jaw**

- **• Even though the UE authenticates the tower there are still several messages that it sends, receives, and trusts before authentication happens or w/o authentication**

- **• This is the weak spot in which the vast majority of 4G attacks happen.**

- **• Even downgrade attacks!**

## Slide 14

<Location **<location, date>** , date>DEF CON 33

Hus **<u>Insecure Connection Bootstrapping in Cellular Networks:The Root of All Evil - Hussein et al 2019</u>**

## Slide 15

<Location **<location, date>** , date>DEF CON 33

Here
there be
dragons

Hus **<u>Insecure Connection Bootstrapping in Cellular Networks:The Root of All Evil - Hussein et al 2019</u>**

## Slide 16

<Location **<location, date>** , date>DEF CON 33

# **Doesn’t 5G Fix This Whole Problem?**

**No, not really. 5G can be jammed. Or turned off.**

**Source: Group2000 - Lima 5g Cellpro**

## Slide 17

<Location **<location, date>** , date>DEF CON 33

# **Previous Detection Methods 2G Only**

## Slide 18

<Location **<location, date>** , date>DEF CON 33


> Recovered by OCR — confidence 66/100 on the text kept, 68/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Crocodile Hunter Tools ~ Cells Enadebs Combined Project: dreamforce
° oo 905.8246687890075 1 12 100% 2019-11-21 123448 2019-11-21 14:25:25
32038 311-480 10755488962169992 8 8 20% 2019-11-21 125721 2019-11-21 14:36:20
```

## Slide 19

<Location **<location, date>** , date>DEF CON 33

# **Problems**

● **Too expensive** ● **Too hard to set up** ● **Difficult to interpret the results for laypersons**

## Slide 20

<Location **<location, date>** , date>DEF CON 33

# **Can we do better? Yes!**

### **Introducing Rayhunter!**

- **Runs on a $20 mobile hotspot**

- ● **Easy(ish) to install**

- **Simple UI**

- **Written in Rust so it’s** **trendy memory safe!**

- **A quick note on the name**

   - It’s the only thing we could come up with that wasn’t already trademarked

## Slide 21

<Location **<location, date>** , date>DEF CON 33

# **Web UI**


> Recovered by OCR — confidence 93/100 on the text kept, 92/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
ELECTRONIC
FRONTIER
Current Recording
ID: 1751059952
1004 Bytes
Start: 6/27/25, 2:32:32 PM PDT
Last Message: 6/27/25, 2:32:55 PM PDT
Started
1750890454 6/25/25, 3:27:34 PM PDT
1750890452 6/25/25, 3:27:32 PM PDT
1750888234 6/25/25, 2:50:34 PM PDT
1750888216 6/25/25, 2:
PM PDT
Web UI
Last Message
6/27/25, 2:32:29 PM PDT
NIA
6/25/25, 3:27:23 PM PDT
6/25/25, 2:50:27 PM PDT
System Information
Rayhunter Version 0.4.0
Report Issue €) Docs [
Storage 62% used (132.5M used / 82.3M available)
Memory (RAM) Free: 4.4M, Used: 155.5M
Size
10.28 MB
0 Bytes
122.62 KB
2.44 KB
ZIP Analysis
2 warnings
0 warning
```

## Slide 22

<Location **<location, date>** , date>DEF CON 33

# **Rayhunter Project Goals**

- **Determine in real time whether CSS are being used to surveil free speech activities**

- ● **Get lots of people using it to determine extent of CSS use**

- **Get a clearer picture of CSS use outside the US**

- ● **Get data about exploits CSS are actually using in the wild**

- **Clear up FUD and more accurate threat modeling for activists**

## Slide 23

<Location **<location, date>** , date>DEF CON 33

# **How Rayhunter works**

● **Consumes the Qualcomm Diag protocol** ● **Captures the traffic going between device and base station (pcap)** ● **Looks for anomalies**

● **Reports to user via screen (user can also download pcap)**

**From a user perspective: Turn it on, put it in your pocket, and go about your day**

## Slide 24

<Location **<location, date>** , date>DEF CON 33

# **Parsing frames**

**.pcap file GSMTAP Unparsed + headers frames**

**Unparsed /dev/diag frames .qmdl file**

**Parsing & Heuristics**

## Slide 25

<Location **<location, date>** , date>DEF CON 33

# **What hardware do we support?**

**Orbic RC400L**

**Wingtech CT2MHS01 T-Mobile TMOHS1**

**TP-Link M7350**

(Celeste port by untitaker)

**PinePhone PinePhone Pro**

## Slide 26

<Location **<location, date>** , date>DEF CON 33

# **What does Rayhunter run on today?**

- **Qualcomm MDM modems**

   - **Rayhunter needs 5-20MB of RAM**

- mdm9x07

   - **Logs need low MBs of storage**

- mdm9650

   - **Devices with a fb display are best**

- Integrated Cortex-A7 (A5) core

- ○ (Open Embedded) Linux 3.18

   - **LEDs are okay**

   - **Helpful if busybox has telnetd**

- Android USB gadget functionality

## Slide 27

<Location **<location, date>** , date>DEF CON 33

**What hardware** **_could_ we support?**

**… ALL the devices**

## Slide 28

<Location **<location, date>** , date>DEF CON 33

**Why is it hard to find IMSI Catchers Threat Hunting, is it art or science? There are SO MANY false positives …**

## Slide 29

<Location **<location, date>** , date>DEF CON 33

# **Heuristics So Far**

- **2G Downgrade**

   - This is the attack used by crimeware IMSI catchers, necessary if you want to send content / inject

   - Monitor the SIB6/7 for downgrade attacks

   - Hasn’t been detected in the US yet

- Problematic in countries where 2g is still a thing

- ● **Null Cipher Use**

   - Check if the base station suggests null ciphers

   - Good for content interception / injection

## Slide 30

<Location **<location, date>** , date>DEF CON 33

# **Heuristics So Far**

- **Incomplete SIB Chains** ○ Developers are lazy!

   - Take IMSI Catchers tend to only send the necessary SIB messages

- **IMSI Attach (Device IMSI is requested)** ○ Look for IMSI/IMEI requested in NAS messages without authentication.

   - This one is our problem child - hard to get right

   - ○ But we know its used by commercial IMSI catchers!

## Slide 31

<Location **<location, date>** , date>DEF CON 33

# **Problems with the IMSI Attach Heuristic**

- **IMSI Attach happens sometimes for legit reasons** ○ Roaming when there are no towers in your home PLMN

- ○ Attach on first startup in a long time

- **A better test! IMSI Request -> No Auth -> Detach** ○ Wallet inspector attack

   - But this happens sometimes for “legit reasons” still

## Slide 32

<Location **<location, date>** , date>DEF CON 33

## **Commercial IMSI Catcher Attack Testing - CAPE**


> Recovered by OCR — confidence 87/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
San == DEF CON 33
Commercial IMSI Catcher Attack Testing - CAPE
| Info |IMSI |IMEISV | ARFCN |cellidentity | trackingArea |
Paging (1 PaqingRacord)
Paging (1 PagingRecord)
Paging (1 PagingRecord)
SystemInformation [ SIB2 SIB3 ]
SystemInformationBlockType1
Tracking area update request
RRCConnectionRequest
RRCConnectionSetup
RRCConnectionSetupComplete, Tracking area update request
DLInformationTransfer, Identity request
Identity request
Identity response |
ULInformationTransfer, Identity response a.
DLInformationTransfer, Tracking area update reject (ILL.
Tracking area update reject (Illegal UE)
RRCConnectionRelease [cause=other]
SystemInformation [ SIB2 SIB3 ]
SystemInformationBlockTypel
```

## Slide 33

<Location **<location, date>** , date>DEF CON 33

## **Commercial IMSI Catcher Attack Testing - CAPE**


> Recovered by OCR — confidence 91/100 on the text kept, 90/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Commercial IMSI Catcher Attack Testing - CAPE
4 pcaps rayhunter-check -p 2_diff_tac_cause_3.pcap
INFO [rayhunter_check] Analyzers:
INFO [rayhunter_check] - Identity (IMSI or IMEI) requested in suspicious manner (v2): Tests whether the ME sends an Identity Request NAS message without either an associated atta
accept message
INFO [rayhunter_check] - Connection Release/Redirected Carrier 2G Downgrade (v1): Tests if a cell releases our connection and redirects us to a 2G cell.
INFO [rayhunter_check] LTE SIB 6/7 Downgrade (v1): Tests for LTE cells broadcasting a SIB type 6 and 7 which include 2G/3G frequencies with higher priorities.
INFO [rayhunter_check] Null Cipher (v1): Tests whether the cell suggests using a null cipher (EEA0)
INFO [rayhunter_check] NAS Null Cipher Requested (v1): Tests whether the MME requests to use a null cipher in the NAS security mode command
INFO [rayhunter_check] - Incomplete SIB (v1): Tests whether a SIB1 message contains a full chain of followup sibs
INFO [rayhunter_check] **** Beginning analysis of 2_diff_tac_cause_3.pcap
WARN [rayhunter_check] 2_diff_tac_cause_3.pcap: WARNING (Severity: High) - 1980-01-26 05:46:22.182570 +00:00 SIB1 scheduling info list was malformed (packet 108)
WARN [rayhunter_check] 2_diff_tac_cause_3.pcap: WARNING (Severity: High) - 1980-01-26 05:46:22.182688 +00:00 SIB1 scheduling info list was malformed (packet 110)
WARN [rayhunter_check] 2_diff_tac_cause_3.pcap: WARNING (Severity: High) - 1980-01-26 05:46:22.182688 +00:00 SIB1 scheduling info list was malformed (packet 111)
WARN [rayhunter_check] 2_diff_tac_cause_3.pcap: WARNING (Severity: High) - 1980-01-26 05:46:22.183072 +00:00 Disconnected after Identity Request without Auth Accept (frame 121)
WARN [rayhunter_check] 2_diff_tac_cause_3.pcap: WARNING (Severity: High) - 1980-01-26 05:46:22.183411 +00:00 SIB1 scheduling info list was malformed (packet 123)
INFO [rayhunter_check] 2_diff_tac_cause_3.pcap: 350 messages analyzed, 5 warnings, 1 messages skipped
```

## Slide 34

<Location **<location, date>** , date>DEF CON 33

# **In the Field - Turks and Caicos**

### **Courtesy of ZeroChaos**


> Recovered by OCR — confidence 91/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
In the Field - Turks and Caicos
INFO - 2025-06-07 21:22:06.
INFO — 2025-06-08 00:22:28.
WARNING (Severity: High) -
WARNING (Severity: High) -
INFO — 2025-06-08
WARNING (Severity:
INFO — 2025-06-08
WARNING (Severity:
INFO — 2025-06-08
WARNING (Severity:
INFO — 2025-06-08
WARNING (Severity:
INFO — 2025-06-09
WARNING (Severity:
INFO — 2025-06-09
WARNING (Severity:
2025-06-09
09:22:14.
High) -
High) —
21:22:35.
High) -
23:46:25.
High) -
09:22:42.
High) -
10:43:40.
High) -
23:49:13.
117 +00:00
411 +00:00
2025-06-08
206 +00:00
2025-06-08
536 +00:00
2025-06-08
448 +00:00
2025-06-08
574 +00:00
2025-06-08
220 +00:00
2025-06-09
258 +00:00
2025-06-09
@8:46:57.462
12:20:30.716
21:22:34.877
10:43:39.567
23:49:13.069
Courtesy of ZeroChaos
after Identity Request without Auth Accept
after Identity Request without Auth Accept
+00:0@ Identity requested without Attach Request
after Identity Request without Auth Accept
+00:0@ Identity requested without Attach Request
after Identity Request without Auth Accept
+00:0@ Identity requested without Attach Request
after Identity Request without Auth Accept
+00:00 Identity requested without Attach Request
after Identity Request without Auth Accept
+00:0@ Identity requested without Attach Request
after Identity Request without Auth Accept
+00:0@ Identity requested without Attach Request
after Identity Request without Auth Accept
+00:0@ Identity requested without Attach Request
after Identity Request without Auth Accept
+00:0@ Identity requested without Attach Request
ity Request without Auth Accept
```

## Slide 35

<Location **<location, date>** , date>DEF CON 33

# **In the Field - Turks and Caicos**

### **Courtesy of ZeroChaos**


> Recovered by OCR — confidence 92/100 on the text kept, 83/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
: WARNING
+ WARNING
+ WARNING
: WARNING
+ WARNING
: WARNING
+ WARNING
: WARNING
: WARNING
+ WARNING
In the Field - Turks and Caicos
(Severitv:
High)
High)
High)
High)
High)
High)
High)
High)
High)
High)
High)
High)
High)
High)
High)
High)
High)
High)
High)
High)
2025-06-10
2025-06-10
2025-06-10
2025-06-10
2025-06-10
2025-06-10
2025-06-10
2025-06-10
2025-06-10
2025-06-10
2025-06-10
2025-06-10
2025-06-10
2025-06-10
2025-06-10
2025-06-10
2025-06-10
2025-06-10
2025-06-10
2025-06-10
14:21:55.975
14:22:06.562
14:44:15.245
14:45:15.717
14:45:26.340
14:45:36.852
14:45:47.430
15:42:52.250
15:43:02.816
15:43:13.335
15:43:24.007
15:43:34.513
15:56:28.342
15:56:38.885
15:56:49.612
15:57:03.956
15:57:14.478
16:10:07.127
16:10:18.090
Cou rtesy of ZeroChaos
+00:00
+00:00
+00:00
+00:00
+00:00
+00:00
+00:00
+00:00
+00:00
+00:00
+00:00
+00:00
+00:00
+00:00
+00:00
+00:00
+00:00
+00:00
+00:00
+00:00
@@ NAS
NAS Security
NAS Security
NAS Security
NAS Security
NAS Security
NAS Security
NAS Security
NAS Security
NAS Security
NAS Security
NAS Security
NAS Security
NAS Security
NAS Security
NAS Security
NAS Security
NAS Security
NAS Security
NAS Security
NAS Security
mode
mode
mode
mode
mode
mode
mode
mode
mode
mode
mode
mode
mode
mode
mode
mode
mode
mode
mode
mode
command
command
command
command
command
command
command
command
command
command
command
command
command
command
command
command
command
command
command
command
requested
requested
requested
requested
requested
requested
requested
requested
requested
requested
requested
requested
requested
requested
requested
requested
requested
requested
requested
requested
null
null
null
null
null
null
null
null
null
null
null
null
null
null
null
null
null
null
null
null
cipher(packet
cipher(packet
cipher(packet
cipher(packet
cipher(packet
166851)
166877)
167483)
167591)
167612)
167633)
167654)
167675)
170505)
170526)
170547)
170568)
170589)
171416)
171442)
171463)
171484)
171505)
172263)
172289)
Securitv mode command reauested null cinher(nacket 172321)
```

## Slide 36

<Location **<location, date>** , date>DEF CON 33

# **In the Field - Chicago**

### **Courtesy of Ryan**


> Recovered by OCR — confidence 94/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
WARN
WARN
WARN
WARN
WARN
WARN
WARN
WARN
WARN
WARN
WARN
WARN
WARN
WARN
WARN
WARN
WARN
WARN
WARN
WARN
WARN
WARN
Lrayhunter_check]
[rayhunter_check]
[rayhunter_check]
[rayhunter_check]
[rayhunter_check]
[rayhunter_check]
[rayhunter_check]
[rayhunter_check]
[rayhunter_check]
[rayhunter_check]
[rayhunter_check]
[rayhunter_check]
[rayhunter_check]
[rayhunter_check]
[rayhunter_check]
[rayhunter_check]
[rayhunter_check]
[rayhunter_check]
[rayhunter_check]
[rayhunter_check]
[rayhunter_check]
[rayhunter_check]
1746544340. qmd1:
1746544340. qmd1:
In the Field - Chicago
Courtesy of Ryan
High) -
High) -
High) -
High) -
High) -
High) -
High) -
High) -
High) -
High) -
High) -
High) -
High) -
High) -
High) -
High) -
High) -
High) -
High) -
High) -
High) -
High) -
2025-05-06
2025-05-06
2025-05-06
2025-05-06
2025-05-06
2025-05-06
2025-05-06
2025-05-06
2025-05-06
2025-05-06
2025-05-06
2025-05-06
2025-05-06
2025-05-06
2025-05-06
2025-05-06
2025-05-06
2025-05-06
2025-05-06
2025-05-06
2025-05-06
2025-05-06
17:15:02.598
17:16:21.876
17:17:05.607
17:17:31.074
17:22:00.123
17:23:06.593
17:24:00.435
17:25:04,431
17:37:51.056
17:38:09.060
17:41:41.630
17:42:32.237
+00:00
+00:00
+00:00
+00:00
+00:00
+00:00
+00:00
+00:00
+00:00
+00:00
+00:00
+00:00
+00:00
+00:00
+00:00
+00:00
+00:00
+00:00
+00:00
+00:00
+00:00
+00:00
after
after
after
after
after
after
after
after
after
after
after
after
after
after
after
after
after
after
after
after
after
after
Identity
Identity
Identity
Identity
Identity
Identity
Identity
Identity
Identity
Identity
Identity
Identity
Identity
Identity
Identity
Identity
Identity
Identity
Identity
Identity
Identity
Identity
Request
Request
Request
Request
Request
Request
Request
Request
Request
Request
Request
Request
Request
Request
Request
Request
Request
Request
Request
Request
Request
Request
without
without
without
without
without
without
without
without
without
without
without
without
without
without
without
without
without
without
without
without
without
without
Auth
Auth
Auth
Auth
Auth
Auth
Auth
Auth
Auth
Auth
Auth
Auth
Auth
Auth
Auth
Auth
Auth
Auth
Auth
Auth
Auth
Auth
Accept
Accept
Accept
Accept
Accept
Accept
Accept
Accept
Accept
Accept
Accept
Accept
Accept
Accept
Accept
Accept
Accept
Accept
Accept
Accept
Accept
Accept
(frame
(frame
(frame
(frame
(frame
(frame
(frame
(frame
(frame
(frame
(frame
(frame
(frame
(frame
(frame
(frame
(frame
(frame
(frame
(frame
(frame
(frame
1036)
1056)
1078)
1100)
1121)
1141)
1159)
1179)
1204)
1224)
1250)
1275)
1303)
1327)
1352)
1373)
1397)
1425)
1464)
1482)
1518)
1542)
```

## Slide 37

<Location **<location, date>** , date>DEF CON 33

# **In the Field - Penn Station - NYC**

### **Courtesy of Alliraine**


> Recovered by OCR — confidence 92/100 on the text kept, 90/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
INFO
WARN
WARN
WARN
WARN
WARN
WARN
INFO
WARN
WARN
WARN
WARN
INFO
[rayhunter_check]
[rayhunter_check]
[rayhunter_check]
[rayhunter_check]
[rayhunter_check]
[rayhunter_check]
[rayhunter_check]
[rayhunter_check]
[rayhunter_check]
[rayhunter_check]
[rayhunter_check]
[rayhunter_check]
[rayhunter_check]
[rayhunter_check]
[rayhunter_check]
[rayhunter_check]
In the Field - Penn Station - NYC
see Beginning analysis of
1746553345-2.qmd1:
1746553345-2.qmd1:
1746553345-2.qmd1:
1746553345-2.qmd1:
: High)
High)
(Severity: High)
(Severity: High)
: High)
High)
High)
1746553345-2.qmd1
- 2025-05-07
2025-05-07
- 2025-05-07
- 2025-05-07
- 2025-05-07
- 2025-05-07
- 2025-05-07
INFO — 2025-05-07 23:14:47.870 +00:00
(Severity: High)
High)
High)
High)
High)
High)
16638 messages analyzed,
Courtesy of Alliraine
— 2025-05-07
2025-05-07
2025-05-07
2025-05-07
- 2025-05-07
13 warnings,
22:46:07.027 +00:00
22:51:02.685 +00:00
22:52:43.567 +00:00
6.714 +00:00
23:13:23.503 +00:00
after
after
after
after
after
after
after
Identity request happened without auth
23:14:54.907 +00:00
5.402 +00:00
6.438 +00:00
9.688 +00:00
51.864 +00:00
23:29:31.928 +00:00
299 messages skipped
after
after
after
after
after
after
Identity Request
Identity Request
Identity Request
Identity Request
Identity Request
Identity Request
Identity Request
request followup
Identity Request
Identity Request
Identity Request
Identity Request
Identity Request
Identity Request
without
without
without
without
without
Auth Accept
Auth Accept
Auth Accept
Auth Accept
Auth Accept
without Auth Accept
without Auth Accept
(frame 14646)
without Auth Accept
without Auth Accept
without Auth Accept
without Auth Accept
without Auth Accept
without Auth Accept
(frame
(frame
(frame
(frame
(frame
(frame
(frame
(frame
(frame
(frame
(frame
(frame
(frame
13411)
13572)
13601)
13743)
13760)
13797)
14530)
14650)
14830)
14972)
15218)
15235)
15279)
```

## Slide 38

<Location **<location, date>** , date>DEF CON 33

**In the Field - No Kings Protests**

## Slide 39

<Location **<location, date>** , date>DEF CON 33

# **Many More**

● **We have several more results that are more ambiguous than this.** ● **Embassies** ● **DNC** ● **Various cities!**

## Slide 40

<Location **<location, date>** , date>DEF CON 33

# **Still lots to do**

- **More testing with simulated attack environments**

- ● **User Testing**

- ● **UI Improvements**

- ● **More Heuristics**

● **International testing and support of all ITU regions**

## Slide 41

<Location **<location, date>** , date>DEF CON 33

**Let’s take Rayhunter global…**

## Slide 42

<Location **<location, date>** , date>DEF CON 33

**ITU Region 1, 2, …3?**

● **A slide!**

**<u>https://efforg.github.io/rayhunter/supported-devices.html</u>**

## Slide 43

<Location **<location, date>** , date>DEF CON 33

# **Adding a new device**

**1. Select a Qualcomm based device**

**2. Root the device**

   - a. Almost all binaries run as root

   - b. Vendors often have hidden unlock methods

   - c. Root password is often oelinux123

**3. Start with headless mode, ensure Rayhunter gets useful data from /dev/diag**

**4. Add display support using our generic_framebuffer module**

**5. Add an installer module**

   - a. Unlocking and installing over telnet instead of adb is preferred

## Slide 44

<Location **<location, date>** , date>DEF CON 33

|**Interesting**|**userspace binaries**|
|---|---|
|**Binary**|**Description**|
|qcmap_web_cgi|Web request logic (may contain RCEs)|
|qcmap_auth|Web authentication logic (may also contain
RCEs)|
|qcmap_web_client|More web request logic (believe it or not,
may contain more RCEs)|
|atfwd_daemon|Undocumented AT commands (you’ll never
guess what those may contain…)|
|boot_hsusb_composition|USB mode switching (enable ADB, after
you get RCE)|

## Slide 45

<Location **<location, date>** , date>DEF CON 33

# **Solving problems with Rust**

### **Before**

### **After**

- **gcc, glibc required**

- **Rust bindings to C libs**

- ● **Overcomplicated toolchain**

- **Install via shell scripts and one Rust binary to unlock adb on the Orbic**

- ● **Needed upstream adb**

- ● **No NAS parsing**

- **musl target**

- ● **llvm linker**

- **Pure Rust libraries only**

- **Only need what you get from rustup**

- ● **Portable statically-linked installer**

- ● **Uses just-enough adb_client**

- ● **Pure Rust NAS parser generated from pycrate**

## Slide 46

<Location **<location, date>** , date>DEF CON 33

# **How can you get involved?**

- **Device porting**

- **GPS functionality on-device**

- **USB host mode**

- **macOS kernel driver detaching in nusb crate**

- **• adb forward in adb_client crate**

- **Windows installer troubleshooting**

- **Write an iOS companion app, or improve our Android app**

- **Keep wardriving! OpenCelliD data is often a decade old**

## Slide 47

<Location **<location, date>** , date>DEF CON 33

# **We Want Your Help!**

● **Do you know people who would be interested in field testing this?** ● **Do you know telephony experts who can help us come up with good heuristics?** ● **Do you want to distribute a bunch of these in your other networks?**

## Slide 48

<Location **<location, date>** , date>DEF CON 33

# **Advice from My Kid**

## Slide 49

<Location **<location, date>** , date>DEF CON 33

# **Acknowledgements**

- **Sangwook Bae, Ruddy Wang and CAPE for help testing and thinking about heuristics.**

- ● **Matthew Garrett for rooting the Orbic and letting us know about it and the diag protocol.**

- ● **Andy Carra from Wigle, Russ Hanneman, and Dragorn for advice and testing.**

- ● **EFF Staff and others for field testing.**

- **Gary Miller, Yoshi Kono, Alex Gantman, Subrato De, Alex Ross, and Bradley Reaves for advice and connections.**

- **Folks at OSMOCOM, QCSuper, and Snoopsnitch for paving the way.**

- ● **Yomna for her work at EFF and elsewhere better understanding and protecting against cell site simulators.**

- **All our open source contributors! Esp. untitaker, sashanoraa, alliraine, MatejKovacic, m0veax, and everyone else!**

- **oopsbagel thanks: Abby, ahills, Aldera, Alex, Ammar, Cody Harris, daygr, Edwin’s Angels, Nathan, q, Rachel, Sharon, Tony**

- **EFF Members for supporting this work!!!**

## Slide 50

<Location **<location, date>** , date>DEF CON 33

**Thank you!**

https://github.com/efforg/rayhunter

Cooper Quintin Senior Staff Technologist <u>cooperq@eff.org</u> - bsky: @cooperq.com

Will Greenberg Senior Staff Technologist <u>willg@eff.org</u>

oopsbagel Rayhunter Maintainer <u>oopsbagel@disroot.org</u>

## Slide 51

<Location **<location, date>** , date>DEF CON 33

# **References**

**1.** **<u>https://www.eff.org/wp/gotta-catch-em-all-understanding-how-imsi-catc hers-exploit-cell-networks</u>**

**2.** **<u>https://www.google.com/url?q=https://www.documentcloud.org/docume nts/24733508-2024_ma-state-police_css-proposal_jacobs/?mode%3Ddocu ment%23document/p16/a2562758&sa=D&source=editors&ust=17540027 55410072&usg=AOvVaw2AM-eIH1FK-BOrlb9AdpZC</u>**

**3.** **<u>https://github.com/srsLTE/srsLTE</u>**

**4.** **<u>https://arxiv.org/pdf/1710.08932.pdf</u> iles/conference/woot17/woot17-paper-**

**5.** **<u>https://www.usenix.org/system/files/conference/woot17/woot17-paperpark.pdf</u>**

**6.** **<u>https://petsymposium.org/popets/2017/popets-2017-0027.pdf</u>**

**7.** **<u>https://www.sba-research.org/wp-content/uploads/publications/Dabrow skiEtAl-IMSI-Catcher-Catcher-ACSAC2014.pdf</u>**
