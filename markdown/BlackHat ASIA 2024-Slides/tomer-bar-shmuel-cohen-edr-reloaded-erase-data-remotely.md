---
title: "EDR Reloaded Erase Data Remotely"
speakers: ["Tomer Bar", "Shmuel Cohen"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2024"
edition: "ASIA"
year: 2024
source_pdf: "BlackHat ASIA 2024-Slides/Tomer Bar & Shmuel Cohen-EDR Reloaded Erase Data Remotely.pdf"
pages: 94
sha256: "47900341bfe506176cb9423f86989a192f0b85abb42d9e49def98912fb879a49"
text_chars: 34672
ocr_pages: 37
has_ocr: true
redacted_secrets: 0
ocr_confidence: 87.8
ocr_unreliable_blocks: 0
vision_verified_blocks: 3
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:53:30Z"
---
# EDR Reloaded Erase Data Remotely

**Speakers:** Tomer Bar, Shmuel Cohen  
**Conference:** Black Hat ASIA 2024  
**Source:** `BlackHat ASIA 2024-Slides/Tomer Bar & Shmuel Cohen-EDR Reloaded Erase Data Remotely.pdf` (94 pages)


## Slide 1

**EDR =  E** rase **D** ata **R** emotely

Tomer Bar

Shmuel Cohen

## Slide 2

# **Tomer Bar**

###### **VP of Security Research @ SafeBreach**

- **This talk is SafeBreach’s 15th talk** at **Black Hat**

- 20 years experience in security research

- ● Main focus in APT and vulnerability research

- ● Presented at many global security conferences Such as: Black Hat USA 2020,2023, DEFCON 28-31…

2

## Slide 3

## **Shmuel Cohen**

###### **Security Researcher @ SafeBreach**

- 6 years experience in cybersecurity

- Main focus in vulnerability research

- Former malware researcher specialized In APT groups LABS

3

## Slide 4

###### Agenda

- Research Goal and approach

- Discover the vulnerability CVE-2023-24860

- Attack vectors

- CVE-2023-36010 (CVE-2023-24860 bypass)

- CVE-2023-36010 bypass + special bonus

4

●Lessons learned, Vendor response, Github, Q&A

## Slide 5

###### Research Goal - Trigger False Positives

OMG It’s Taylor
Swift

5


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Research Goal - Trigger False Positives
OMG It’s Taylor
Swift
Windows
Defender
```

## Slide 6

Research Goal - Trigger False Positives

**It’s The Devil! Destroy it**

6


> Recovered by OCR — confidence 93/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Research Goal - Trigger False Positives
It’s The Devil!
Destroy it
Windows
Defender
|
```

## Slide 7

###### Teaser

**What will you say if we can remotely delete critical files over the internet, Pre-authentication, Exploit multiple vulnerable Security controls both on Windows and Linux from your Fully patched servers**

Byte signature do bites

7

## Slide 8

###### The Challenges

Byte signature 2 engine are considered as the most trusted and accurate  layer

1

Remote ~~1~~ 2 Triggering

FP is a known issue and most 3 <u>were already been</u> fixed

8

## Slide 9

Step 1 Extracting EDR’s Byte-Signatures

## Slide 10

###### Black Box Approach

10


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Black Box Approach
Black Box
INPUT OUTPUT
Input is converted
into output
```

## Slide 11

11

###### Windows Defender signature hunting


> Recovered by OCR — confidence 87/100 on the text kept, 59/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Windows Defender signature hunting
microsoft:infected size:200-
microsoft:infected size:200-
FILES 20/3.61K
] @ © eicar.com-30638
javascript
Detections
61/65
21/61
46 /62
Sort by ~
Size
69B
68B
184B
198B
94B
11
```

## Slide 12

###### How to manually minimize a signature ?

- Example, let’s assume entire malicious file content is : “XABCY”

- ● Remove “X”, write “ABCY” to disk -> detection -> “X” is not part of the signature

- Remove “A”, write “BCY” to disk -> no detection -> “A” is part of the signature

- Remove “B”, write “ACY” to disk -> no detection -> “B” is part of the signature

- Remove “C”, write “ABY” to disk -> no detection -> “C” is part of the signature

- Remove “Y”, write “ABC” to disk -> detection

   - -> “Y” is not part of the signature

- The signature is “ABC”

12

## Slide 13

Windows Defender Byte Signatures

## Slide 14

###### Windows Defender  - RTFM

14


> Recovered by OCR — confidence 94/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Windows Defender - RTFM
class MSFT_MpThreat : BaseStatus
{
string SchemaVersion = 1.0.0.0";
sint64 ThreatID;
string ThreatName;
uint32 RollupStatus;
string Resources[];
boolean DidThreatExecute = false;
boolean IsActive = false;
Learn / Windows / Customize / Desktop customizations / @
ThreatSeverityDefaultAction
Article + 12/17/2020 + 2 minutes to read + 4 contributors Feedback
ThreadSeverityDefaultAction configures the default action to be taken for a threat alert that Microsoft Defender takes.
Microsoft Defender is an application that can prevent, remove, and quarantine malware (malicious software) and spyware.
Child Elements
Setting Description
Low Specifies the default action to take for threat alert identified as Low.
Moderate Specifies the default action to take for threat alert identified as Moderate.
High Specifies the default action to take for threat alert identified as High.
Severe Specifies the default action to take for threat alert identified as Severe.
```

## Slide 15

###### Windows Defender  - RTFM

15


> Recovered by OCR — confidence 89/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
WI Nn d OWS Defe Nn d er - RT F M CAutoScan: :ActipnStringFromID(enum tagMPTHREAT_ACTION)
sub edx, 1
jz short loc_140012435 loc_14001243E:
Article - 12/17/2020 + 2 minutes to read - 5 contributors
Severe specifies the automatic remediation action taken for detected threats with a Severe alert level. 14001242c} | 1oc_140012435:
lea rax, aQuarantine ; “Quarantine”
retn
Values z
rax, aRemove
1 Clean the detected threat.
2 Quarantine the detected threat.
3 Remove the detected threat. :
6 Allow the detected threat.
8 Allow the user to determine the action to take with the detected
threat.
9 Do not take any action.
10 Block the detected threat.
NULL Apply action based on the update definition. This is the default
value.
```

## Slide 16

Automatic Signature generation Selecting the “best” signature

## Slide 17

###### Automatic Minimal Signature Generation

- We downloaded all 3.6K files from the original VT query

- Develop a python tool to minimize the binaries into minimal signature as possible

Automatic Minimize

17

## Slide 18

###### Automatic Minimal Signature Generation

- We found 130 unique signatures

18


> Recovered by OCR — confidence 83/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Automatic Minimal Signature Generation
e We found 130 unique signatures
EvilSignature Times
[autorun]shellexecute=.exeaction=Openfoldertoviewfile 990
115
<FRAME SRC=http:www.searchvity.com/<html> 110
<?phpeval(S POST[ 80
cdDrivestartwscript"\."exit 77
PKa™¥a™ | 64
<evalrequest("")%> 14
<?phpeval(S_REQUEST[ 13
18
```

## Slide 19

###### Signature Limitations: how to select the best signature?

**Selecting the best signature: LESS is MORE**

Minimum Limitations =

1. Minimum special characters

2. Minimum length

###### **LESS is MORE**

19

## Slide 20

###### Signature Limitations: how to select the best signature

Shortest signatures with minimum special types

20


> Recovered by OCR — confidence 92/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Signature Limitations: how to select the best signature
Shortest signatures with minimum special types
special
length
EvilSignature
a3
//brembotembo.com/?.dat
26
//operasanpiox.bravepages.com/20190614890563891.xls
a7
cdDrivestartwscript"\."exit
20
```

## Slide 21

Signature Limitations: how to select the best signature

● {\rtf1{\shp{\sp

● Alert level: Severe File was quarantined automatically

21


> Recovered by OCR — confidence 92/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Signature Limitations: how to select the best signature
e Alert level: Severe QO Virus & threat protection
File was quarantined automatically Protection for your device against threats.
Q Current threats
Threats found. Start the recommended actions.
i) cve-2010-3333.txt - Notepad
File Edit Format View Help 24/10/2022 4:36 (Active)
{\rtf1{\shp{\sp} Action options:
@) Quarantine
O Remove
O Allow on device
See details
```

## Slide 22

Step 2

Manually embed the signature In Legit File

## Slide 23

###### Failed First attempt

Legit file (non PE)
RTF signature

Legit file (non PE)

23

## Slide 24

Faster Automatic Minimal Signature Generation


> Recovered by OCR — confidence 90/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Faster Automatic Minimal Signature Generation
Result = scanner->Scan(NULL, sample.data,
sample.size, &scanResult); ]
if (hResult == S_OK)
{
if (scanResult.IsMalware)
cout << "original is Malware" << endl;
else
{
cout << "original is Benign,exit" << endl;
return;
}
}
{
buffer[i] = 'Z';
hResult = scanner->Scan (NULL,
if (hResult == S_OK)
{
if (scanResult.IsMalware)
{
cout << "[+] Defender
sample.data,
verdict:
Malware.
sample.size, &scanResult);
minimized byte until
offs
t:
"<< i
<<endl;
```

## Slide 25

###### PE Files

###### Executable legit file

###### Mimikatz signature

Mimikatz signature

25


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 87/100 on the text kept, 79/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
PE Files

Executable legit file
[folder/file icon diagram with a callout box labeled] Mimikatz signature [pointing into the hex dump]

Mimikatz signature

5A5A 5A64 8606 0063 395A 5E00 0000 0000   ZZZd†..c9Z^.....
0000 00F0 0022 1244 0FB6 4404 4F00 5B00   ...ð.".D.¶D.O.[.
2500 7800 3B00 2500 7800 5D00 2D00 2500   %.x.;.%.x.].-.%.
3100 7500 2D00 2500 7500 2D00 2500 3000   1.u.-.%.u.-.%.0.
3800 7800 2D00 2500 7700 5A00 4000 2500   8.x.-.%.w.Z.@.%.
7700 5A00 2D00 2500 7700 5A00 2E00 2500   w.Z.-.%.w.Z...%.
7300 004B 0049 0057 0049 005F 004D 0053   s..K.I.W.I._.M.S
0056 0031 005F 0030 005F 0043 0052 0045   .V.1._.0._.C.R.E
0044 0045 004E 0054 0049 0041 004C 0053   .D.E.N.T.I.A.L.S
0020 6500 0011 0053 616D 456E 756D 6572   . e....SamEnumer
6174 6544 6F6D 6169 6E73 496E 5361 6D53   ateDomainsInSamS
6572 7665 7200 4D65 6D6F 7279 0013 0053   erver.Memory...S
616D 456E 756D 6572 6174 6555 7365 7273   amEnumerateUsers
496E 446F 6D61 696E 0065 0002 0049 5F4E   InDomain.e...I_N
6574 5365 7276 6572 5472 7573 7450 6173   etServerTrustPas
7377 6F72 6473 4765 7400 0000 0000 5A5A   swordsGet.....ZZ
```

## Slide 26

###### NON-PE Files

Windows Defender
Non PE file PE file
0
Get scanned
MZ
4030
Does  NOT
Get scanned
get scanned
…
…
…
EOF - 4030
Get scanned
EOF
EOF

26

## Slide 27

Challenge 3 - Attack Vectors implant the signatures in legit files

## Slide 28

###### Implant signature - achieve remote deletion of logs

1. Send HTTP POST request Including signature

2. Signature is

written to log file

3. Defender deletes the log 28

## Slide 29

LOGS Remote deletion of Windows Web Server Logs **CVE-2023-24860**

## Slide 30

###### Remote Deletion of Windows Web Server Logs - Demo

30

## Slide 31

###### Remote Deletion of Windows Web Server Logs

Barking dog **starts to** bite… :) WORKED !!! Defender detect IIS log file as an RTF exploit

31

## Slide 32

###### Remote Deletion of Linux Web Server Logs

The Web server’s market share

32


> Recovered by OCR — confidence 89/100 on the text kept, 66/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Remote Deletion of Linux Web Server Logs
The Web server's market share
Nginx
Apache
Cloudiflare Server
LiteSpeed
Microsoft-IIs
Node.js
Google Servers
Envoy
32
```

## Slide 33

###### Remote Deletion of Linux Web Server Logs

33


> Recovered by OCR — confidence 89/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Remote Deletion of Linux Web Server Logs
ABILITY TO EXECUTE
Check Point Software Technologies
Panda Security qy
NICHE PLAYERS
COMPLETENESS OF VISION —_—>
As of May 2021
© Gartner, inc
33
```

## Slide 34

###### EvilSignature DataBase

34


> Recovered by OCR — confidence 91/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
EvilSignature DataBase
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
signature os AV len v2 specialCharTypeCount validFileName —_validFolderName
[Filter Filter Filter Filter Filter Filter [Filter l
<?="$ GET[]’; Windows Microsoft Defender 13 9 False False
{\rtfl{\shp{\sp Windows Microsoft Defender 15 2 False True
<?phpeval($_GET[ Windows Microsoft Defender 16 6 False False
Gif89a\r\n<2php Linux Kaspersky 16 4 True True
:a\r\nstartgoto Linux Kaspersky 16 3 True True
<%eval request(" Linux Kaspersky 16 5 True True
<?php @eval($_POST[ Linux Kaspersky 19 8 True True
<?phpsystem($_POST[ Windows Microsoft Defender 19 6 False False
<%EVAlreQUesT("")%> Windows Microsoft Defender 19 6 False False
<%EvalreQUesT(™)%> Windows Microsoft Defender 19 6 False False
<%evalrequest("")%> Windows Microsoft Defender 19 6 False False
<%evalrequest(")%> Windows Microsoft Defender 19 6 False False
<%evalrequEst("")%> Windows Microsoft Defender 19 6 False False
<%evalrEquEst("")%> Windows Microsoft Defender 19 6 False False
<eval_r(Request("")> Windows Microsoft Defender 20 6 False False
cmd /crd/s/qc:\\ Linux Kaspersky 20 4 False False
<?phpeval($_REQUESTL Windows Microsoft Defender 20 6 False False
<iframe name=twitter Windows Avast 20 3 False False
<?php system($_POST[" Linux Kaspersky 21 8 True True
<?phpsystem($_REQUEST[ Windows Microsoft Defender 22 6 False False
<?phppassthru(getenv(" Windows Microsoft Defender 22 4 False False
rundll32 mouse,disable Linux Kaspersky 22 2 True True
//brembotembo.com/2.dat Windows Microsoft Defender 23 2 False False
open 210..81.exe\r\nbye Windows AVG 23 3 False True
<iframe name=Twitterigar Windows AVG 24 3 False False
34
```

## Slide 35

###### Automatic Minimal EvilSignature generation - Linux

AVAST + AVG

Trend Micro

Others: Palo Alto, CrowdStrike, SentinelOne

By default only scan files With predefined extensions

only works in the beginning of the file

Relay on ML Don't use byte signatures

35

## Slide 36

###### Automatic Minimal EvilSignature generation - AV

One EvilSignature to rule the all

● Kaspersky

● Windows Defender

36

## Slide 37

### LOGS

Remote deletion of Linux Web Server Logs

## Slide 38

###### Remote Deletion of Linux Web Server Logs - Ngnix Demo

38


> Recovered by OCR — confidence 84/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Remote Deletion of Linux Web Server Logs - Ngnix Demo
192.168.220.130
Welcome to nginx!
If you see this page, the nginx web server is successfully installed and
working. Further configuration Is required
For online documentation and support please refer to nginx.org.
Commercial support is available at nginx.co’
m.
Thank you for using nginx. John@john-virtual-machine: ~
Every ©.5s: tatl /var/log/ngtnx/access. log john-virtual-machtne: wed Nov
tatl: cannot open '/var/log/ngtnx/access.log' for reading: Operation not permitted
Command Prompt
fully sent Storage
L\desk python mali gn 138 "<script>fun
ation. href. indexof +1) ;var n substring(addr. Length, locati
38
```

## Slide 39

###### Remote Deletion of Windows Web Server Logs

- The Web server’s market share

39


> Recovered by OCR — confidence 94/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Remote Deletion of Windows Web Server Logs
e The Web server’s market share
Nginx
Apache
Cloudflare Server
LiteSpeed
Microsoft-IIs
Node.js
Google Servers
Envoy
39
```

## Slide 40

Windows - FTP - Remote Deletion of Filezilla server logs

40


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Windows - FTP - Remote Deletion of Filezilla server logs
alProt
HackTool:Win32/Mikatz!dha
Alert level: High
Status: Active
Date: 02/11/2022 8:55
Category: Tool
| Details: This program has potentially unwanted behavior.
© Windows Security
Learn more
| Windows Security
| Affected items:
needed in Microsoft Defender
| file: C:\Program Files\FileZilla Server\Logs\filezilla-server.log
OK
Dismiss
```

## Slide 41

###### Remote deletion of local mailbox - Mozilla ThunderBird

● Send mail to victim with a subject with the EvilSignature

41


> Recovered by OCR — confidence 93/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Remote deletion of local mailbox - Mozilla ThunderBird
e Send mail to victim with a subject with the EvilSignature
he b Subject
© Windows Security
Windows Security
Threat quarantined Actions needed in Microsoft Defender
20/11/2022 3:10 ae
Detected: HackTool:Win32/Mikatz!dha Dismiss
Status: Quarantined
Quarantined files are in a restricted area where they can't harm your device. They will be removed automatically.
Date: 20/11/2022 3:11
Details: This program has potentially unwanted behavior.
Affected items:
\imap.gmail.com\INBOX
```

## Slide 42

###### Local - Unprivileged deletion of Windows event log file

###### corrupted msi with

###### version info includes the signature

###### Application.evtx is deleted

42

## Slide 43

Remote - Deletion of Windows event log file

Failed SMB login attempts, the username includes signature            Security.evtx remotely deleted

43

## Slide 44

###### Remote - Remote Deletion of Windows event log file

44

## Slide 45

###### Windows Defender - Delete Windows Defender detection logs

**Self cannibalism** - Defender deletes its own detection logs :)

45


> Recovered by OCR — confidence 82/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Windows Defender - Delete Windows Defender detection logs
Self cannibalism - Defender deletes its own detection logs :)
Date: 02/11/2022 1:47 vacetotwnsoneatle
Details: This program has potentially unwanted
behavior, Alert level: High
Status: Active
Date: 21/11/2022 0:17
Affected items: Category: Tool
Details: This program has potentially unwanted behavior.
containerfile: C:’\playground\,12.msi Learn more
> . fy = Affected items:
co ntaine rfile: C\P rogra m Data\M icrosoft containerfile: C:\\ProgramData\Microsoft\Windows Defender\Scans\History
\Windows Defender\Scans\History\Service \Service\DetectionHistory\18\E2AA9560-9748-45FD-B6EA-SFFBSF3C4E42
= 7 containerfile: C:\ProgramData\Microsoft\Windows Defender\Support
\2 2\O4BA29 BD-7OEC-4004-8544-61248BD9022 file: C:\ProgramData\Microsoft\Windows Defender\Scans\History\Service
AB >(UTF-16LE)
4 a 7 file: C:\ProgramData\Microsoft\Windows Defender\Support
co ntaine rile: C\Progra mData\M icrosoft AMMPLog-20010202-121608log->(UTEA6LE)
\Windows Defender\Scans\History\Service
\Detections.log Ok
```

## Slide 46

###### Windows Defender - Self cannibalism demo

46

## Slide 47

EvilSignature - Collateral damage - 2nd phase - Splunk

###### All rivers flow to the sea

47

## Slide 48

###### Domino Effect - Splunk

● All rivers flow to the sea … all logs flow to Splunk

48


> Recovered by OCR — confidence 82/100 on the text kept, 66/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Domino Effect - Splunk
e All rivers flow to the sea ... all logs flow to Splunk
Q
Ad hoc
search
On-
Premises
Private
Goud
Public
Ontine
Web
a Services
Security
Servers GPs
location
i = Networks
Storage
Shopping
ale ca Detad
Smartphones
and Devices
Packaged
Applications
ry ape
Custom
Meters
Monitor Report Custom ” Developer
and alert and dashboards Platform
analyze
splunk
References — Coded fields, mappings aliases
System /appiiation - Available only wing apgication request
```

## Slide 49

EvilSignature - Collateral damage - 2nd phase - Splunk

###### Manually adding log file, the filename includes the EvilSignature

49


> Recovered by OCR — confidence 88/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Splunk
Manually adding log file, the filename includes the EvilSignature
Alert level: Severe
a Date: 08/11/2022 12:36
Set Source Type Category: Backdoor
y . Details: This program provides remote access to the com|
on.
Learn more
Time Event
Affected items:
file: C:\Program Files\Splunk\var\lib\splunk\defaultdb\dby
\hot_v1_0\rawdata\0
HackTool:SH/PythonKeylogger.B
Alert level: High
Status: Active
Date: 08/11/2022 12:26
Threats found Category: Tool
Details: This program has potentially unwanted behavior.
Windows Security
Learn more
Affected items:
file: C:\Program Files\Splunk\var\run\splunk\dispatch
\1667939169.19\indexpreview.csv
file: C:\Program Files\Splunk\var\run\splunk\dispatch
file: C:\Program Files\Splunk\var\run\splunk\dispatch 49
\1667939169.19\status.csv
```

## Slide 50

EvilSignature - Collateral damage - 2nd phase - Splunk

###### ● Splunk collect windows security event logs

50


> Recovered by OCR — confidence 89/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Splunk
Splunk collect windows security event logs
EventType=8
ComputerName=DESKTOP-6655UUR
Show all 61 lines
Event Actions ¥
Type “ Field
Selected |v| host +
¥| source ¥
¥| sourcetype *
Event Account_Domain *
Account_Name ¥
Value
WinEventLog:Security
WinEventLog:Security
domain
HackTool:Win32/Mikatz!dha
Alert level: High
Status: Active
Date: 08/11/2022 14:18
Category: Tool
Details: This program has potentially unwanted behavior.
Learn more
Affected items:
file: C:\Program Files\Splunk\var\lib\splunk\defaultdb\db
\hot_v1_0\rawdata\8999987
OK
Add-Member NoteProperty -Name VirtualProtect -Value $VirtualProtect
50
```

## Slide 51

VMWARE - Permanent Denial Of Service

## Slide 52

###### VMWARE - Permanent Denial Of Service

● VMX file contains the configuration data of the guest VM and it’s necessary for the machine to boot up.

52

## Slide 53

###### VMWARE - Permanent Denial Of Service

53


> Recovered by OCR — confidence 83/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
VMWARE - Permanent Denial Of Service
john@john-virtual-machine: ~/Desktop
S$ vmware-rpctool "info-set guestinfo.detailed.data <%eval request('a')x>"ff
```

## Slide 54

###### VMWARE - Permanent Denial Of Service

54


> Recovered by OCR — confidence 86/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
VMWARE - Permanent Denial Of Service
john@john-virtual-machine: ~/Desktop
$ vmware-rpctool "info-set guestinfo.detailed.data <%eval request('a')%>"
VMware Workstation unrecoverable error: (vcpu-1)
Failed to reopen dictionary after renaming "C:\Users\Shmuel
\Documents \Virtual Machines \Ubuntu 64-bit - Eset32\Ubuntu
64-bit - Eset32. vmx~" to “C:\Users\Shmuel Documents \Virtual
Machines \Ubuntu 64-bit - Eset32\Ubuntu 64-bit -
Eset32.vmx": Error (2)
A log file is available in "C:\Users\Shmuel\Documents \Virtual
You can request support.
To collect data to submit to VMware support, choose "Collect
Support Data” from the Help menu.
You can also run the “vm-support" script in the Workstation
folder directly.
We will respond on the basis of your support entitlement.
OK
```

## Slide 55

###### VMWARE - Permanent Denial Of Service

55


> Recovered by OCR — confidence 77/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
D vwware - Permanent Denial Of Service
BUT WAIT
THERE'S MORE!
```

## Slide 56

###### VMWARE - Permanent Denial Of Service - Demo

56


> Recovered by OCR — confidence 91/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
VMWARE - Permanent Denial Of Service - Demo
Windows Security
Scan options
John@john-virtual-machine: -/Desktop
@ Customised scan
Microsoft Defender Antivirus (offline scan)
Have a question?
```

## Slide 57

Remote deletion of Production Databases

## Slide 58

###### Remote Deletion of Web Server DataBase - MariaDB

1. Register a new user in a website The user name is the signature

2. Signature is written to backend DB

3. Defender deletes the entire DB.

58

## Slide 59

###### Remote Deletion of Web Server DataBase - MySQL - Linux

59


> Recovered by OCR — confidence 86/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Remote Deletion of Web Server DataBase - MySQL - Linux
John@john-virtual-machine: ~/Desktop Qo = - a x
```

## Slide 60

###### Remote Deletion of Web Server DataBase - MARIADB DEMO

60


> Recovered by OCR — confidence 75/100 on the text kept, 66/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Remote Deletion of Web Server DataBase - MARIADB DEMO
€ > S_O@ lecathost/view,php
racine Satin No connection could be made because the target machine actively refused it. in
is: 3 cog O Virus & threat protection 20.0037] 363808|mysali connect’ Shost = localhost, Suser = Feview_site, Spassword = JxSLRKGuW?, Sdatabase = eviews, Sport= 3307)
a Stack
HackTook:Win32/Mikatzidha # [Time [Memory [Function [Location
2 t Fi Alert level: High
a Status: Active Call Stack
ty Date: 18/10/2022 6:50 j#|Time [Memory [Function [Location
Ss Details: This program has potentially unwanted behavior. [2] 4.0991 | 36450-4}mysali_query( Slink = FALSE, Squery = ‘select * from user_reviews' ) Aview,php:31
oO d |An error occurred when submitting your review.
Learn more
2 Affected items:
N OK
Start actions
60
```

## Slide 61

###### Most popular databases worldwide as of August 2022

https://www.statista.com/statistics/809750/worldwide-popularity-ranking-database-management-system

61

## Slide 62

##### **We were able to remotely delete four different databases**

62


> Recovered by OCR — confidence 77/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
We were able to a delete four different databases
0 uf. QLite
Oracl 1,260.8
MySQL 1,202.85
(x) Microsot ft SOL Serv
PostgreSQ)
MongoDB
Red
16M Db.
Elasticsearch
Microso! ft Access
62
```

## Slide 63

Remote deletion of Browser files in the victim’s computer surfing to a Malicious Web


> Recovered by OCR — confidence 94/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Remote deletion of Browser files in the victim’s
computer surfing to a Malicious Web
2s
```

## Slide 64

###### Remote deletion of Browser files

1. The browser sends HTTP request

   2. The server returns the signature in the body of the response

3. The browser logs the response to its own DB,

64

Defender deletes the Browsers DB.

## Slide 65

###### Remote deletion of Browser files: Chrome History & Web Data

######

65


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Remote deletion of Browser files: Chrome History & Web Data
HackTool:Win32/Mikatz!dha
Alert level: High
Status: Active
Date: 24/10/2022 15:54
Category: Tool
Details: This program has potentially unwanted behavior.
Backdoor:PHP/Remoteshell.A Learn more
Affected items:
Alert level: Severe
[ file: C:\Users\Safebreach\AppData\Local\Google\Chrome\User Data |
Status: Active 5
Date: 24/10/2022 17:00 \Default\History
Category: Backdoor
Details: This program provides remote access to the computer it i OK
on.
Learn more
® Windows Security
Affected items:
Windows Security containerfile: C:\Users\Safebreach\AppData\Local\Google\Chrome\User
Data\Default\Sessions\Session_13311128388386113
Actions needed in Microsoft Defender file: C:\Users\Safebreach\AppData\Local\Google\Chrome\User Data
f Ba. \Default\Sessions\Session_13311128388386113->(SCRIPTO000)
; file: C:\Users\Safebreach\AppData\Local\Google\Chrome\User Data
\Default\Web Data
OK
Dismiss
65
```

## Slide 66

###### Future work - the sky is not the limit

66


> Recovered by OCR — confidence 85/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Future work - the sky Is not the limit
Microsoft Defender for Cloud
Secure your hybrid-cloud and multicloud workloads
©
Azure Network
3 ©
© &
App Services Azure K8s
Azure SQL
Azure DNS
Key Vault
Resource
Manager
Blob Storage File Storage Maria DB
So U
MySQL Postgres
Amazon EKS Amazon EC2
Unmanaged Unmanaged
Kubernetes sQu
aws
Kubernetes
SQLServers Servers
©
Google Compute ©
a) o GKE Clusters
Unmanaged Unmanaged
The Sky is net the Limit
It's just the Beginning
66
```

## Slide 67

###### Vendor Response

Microsoft: released a fix to the vulnerability: CVE-2023-24860 We reported that the fix is not complete Microsoft classified it as “moderate DOS”, didn’t fix the rest of attack vectors.

Kaspersky: did not release a fix: “This case is can’t be classified as a security vulnerability… We are planning some improvements to mitigate this issue”.

67

## Slide 68

###### Vulnerability Timeline

###### **First Report to MSRC**

**CVE-2023-24860 Patch Analysis**

**January April August 2023 2023 2023**

**68**

## Slide 69

Second report to Microsoft  - CVE-2023-24860 patch analysis

###### Unprivileged deletion of Defender detections Log file

Patched Version

**69**

## Slide 70

###### Second report to Microsoft  - CVE-2023-24860 patch analysis

###### **Fixed Attack Vectors**

**unFixed Attack vectors**

Remote deletion of Windows Event Log file Remote deletion of MySQL database

Remote deletion of IIS log file Remote deletion of Apache log file

Remote deletion of PostGRESQL database Remote deletion of MongoDB database Remote deletion of MariaDB database

Remote deletion of NGnix log file Remote Deletion of Filezilla server log file

VMware deletion of VMX file

Unprivileged deletion of Windows Event Log file

Unprivileged deletion of Defender detections Log file

Local deletion of VMware VMDK files

**70**

## Slide 71

Second report to Microsoft  - CVE-2023-24860 patch bypass

###### The Default

###### Storage

MySQL InnoDB

**71**


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 85/100 on the text kept, 85/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Second report to Microsoft  - CVE-2023-24860 patch bypass

The Default Storage M[obscured by overlapping screenshot]

Table options
Rename table to: wp_comments
[ ] Adjust privileges (i)
Table comments: (blank)
Storage Engine (i): MyISAM ▾
   CSV
   MRG_MyISAM
   SEQUENCE
   MyISAM
   MEMORY
   Aria
   InnoDB  [highlighted/selected]
   DEFAULT
PACK_KEYS: [obscured by open Storage Engine dropdown]
CHECKSUM: [ ]
DELAY_KEY_WRITE: [ ]
AUTO_INCREMENT: 2890
ROW_FORMAT: DYNAMIC ▾
[Go]

C:\playground\defender_signatures\mysql\#ib_redo0

           0001 0203 0405 0607 0809 0A0B 0C0D 0E0F   0123456789ABCDEF
0x00       0000 0006 4020 EDBD 0000 0000 01DE 4000   ....@ í½.....Þ@.
0x10       4D79 5351 4C20 382E 302E 3330 0000 0000   MySQL 8.0.30....
0x20       0000 0000 0000 0000 0000 0000 0000 0000   ................
0x30       0000 0000 0000 0000 0000 0000 0000 0000   ................
0x40       0000 0000 0000 0000 0000 0000 0000 0000   ................
0x50       0000 0000 0000 0000 0000 0000 0000 0000   ................
0x60       0000 0000 0000 0000 0000 0000 0000 0000   ................
0x70       0000 0000 0000 0000 0000 0000 0000 0000   ................
0x80       0000 0000 0000 0000 0000 0000 0000 0000   ................
0x90       0000 0000 0000 0000 0000 0000 0000 0000   ................
0xA0       0000 0000 0000 0000 0000 0000 0000 0000   ................
0xB0       0000 0000 0000 0000 0000 0000 0000 0000   ................

ALTER TABLE `table_name` ENGINE=INNODB
```

## Slide 72

###### Second report to Microsoft  - CVE-2023-24860 patch bypass

MySQL MYIASM - The default storage engine format until MySQL version 5.5.5

**72**

## Slide 73

Second report to Microsoft  - CVE-2023-24860 patch bypass MYIASM DEMO

**73**

## Slide 74

###### Second report to Microsoft  - CVE-2023-24860 patch bypass

MySQL MYIASM

WAMP **W** indows **A** pache **M** ySQL **P** HP

**74**


> Recovered by OCR — confidence 75/100 on the text kept, 63/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
lI second report to Microsoft - CVE-2023-24860 patch bypass
WAMP
Windows Apache
— MySQL PHP
MySQL MYIASM
& ry : U Virus & threat protection
q U Virus & threat protection =
7 ) Current
: ad | Alert level: High
t z Date: 18/10/2022 1:54
#3 mysql Date: 18/10/2022 2:03 Category: Tool
= tails: This program has potentially unwanted behavior.
&G review Details: This program is dangerous and exploits the computer on which it | pe TES PROS! Ps Mu ‘
= Expld
bom |2 Acti Lea more ' Affected items:
© 4 Affected items: file: C\wamp64\logs\php_error.log
i file: C:\wamp64\bin\mariadb\mariadb10.6.5\data\reviews\user_reviewMYD
| oK
on setting:
Tul
```

## Slide 75

###### Second report to Microsoft  - CVE-2023-24860 patch bypass

**Fixed Attack Vectors**

**unFixed Attack vectors**

Remote deletion of Windows **Event Log file** Remote deletion of **MySQL database**

Remote deletion of **IIS log file** Remote deletion of **Apache log file**

Remote deletion of **PostGRESQL database**

Remote deletion of **MongoDB database**

Remote deletion of **NGnix log file** Remote Deletion of **Filezilla server log file**

Remote deletion of **MariaDB database**

VMware deletion of **VMX file**

Unprivileged deletion of **Windows Event Log file**

Unprivileged deletion of **Defender detections Log file**

VMware deletion of **VMDK file**

Remote deletion of **MySQL database MYIASM 75**

**75**

## Slide 76

###### Second report to Microsoft  - CVE-2023-24860 patch bypass

**No Detection**

**Detection and deletion of benign files**

Binary Format

Textual Format

**76**

## Slide 77

Second report to Microsoft  - CVE-2023-24860 patch bypass

**77**


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Second report to Microsoft  - CVE-2023-24860 patch bypass

La Signature

Trojan:Win32/Leivion.K

      0001 0203 0405 0607 0809 1011 1213 1415   0123456789012345
0     6663 6538 3839 3030 3030 3030 3630 3839   fce8890000006089
16    6535 3331 6432 3634 3862 3532 3330 3862   e531d2648b52308b
32    3532 3063 3862 3532 3134 3862 3732 3238   520c8b52148b7228
48    3066 6237 3461 3236 3331 6666 3331 6330   0fb74a2631ff31c0
64    6163 3363 3631 3763 3032 3263 3230 6331   ac3c617c022c20c1
80    6366 3064 3031 6337 6532 6630 3532 3537   cf0d01c7e2f05257
96    3862 3532 3130 3862 3432 3363 3031 6430   8b52108b423c01d0
112   3862 3430 3738 3835 6330 3734 3461 3031   8b407885c0744a01
128   0D0A 6430 3530 3862 3438 3138 3862 3538   ..d0508b48188b58
144   3230 3031 6433 6533 3363 3439 3862 3334   2001d3e33c498b34
160   3862 3031 6436 3331 6666 3331 6330 6163   8b01d631ff31c0ac
176   6331 6366 3064 3031 6337 3338 6530 3735   c1cf0d01c738e075
192   6634 3033 3764 6638 3362 3764 3234 3735   f4037df83b7d2475
208   6532 3538 3862 3538 3234 3031 6433 3636   e2588b582401d366
224   3862 3063 3462 3862 3538 3163 3031 6433   8b0c4b8b581c01d3
240   3862 3034 3862 3031 6430 3839 3434 3234   8b048b01d0894424
256   3234 0D0A 3562 3562 3631 3539 3561 3531   24..5b5b61595a51
272   6666 6530 3538 3566 3561 3862 3132 6562   ffe0585f5a8b12eb
288   3836 3564 3638 3333 3332 3030 3030 3638   865d683332000068
304   3737 3733 3332 3566 3534 3638 3463 3737   7773325f54684c77
320   3236 3037 6666 6435 6238 3930 3031 3030   2607ffd5b8900100
336   3030 3239 6334 3534 3530 3638 3239 3830   0029c45450682980
352   3662 3030 6666 6435 3530 3530 3530 3530   6b00ffd550505050
368   3430 3530 3430 3530 3638 6561 3066 6466   4050405068ea0fdf
384   6530 6666                                  e0ff
```

## Slide 78

Second report to Microsoft  - CVE-2023-24860 patch bypass

**78**

## Slide 79

###### Vulnerability Timeline

###### **First Report CVE-2023-24860 to MSRC**

**Second Report CVE-2023-36010 Patch Bypass**

**January April 2023 2023**

**August 2023**

**December 2023**

**79**

## Slide 80

Third report to Microsoft  - CVE-2023-36010 bypass MySQL InnoDB - The patch didn't fix this attack vector

80


> Recovered by OCR — confidence 84/100 on the text kept, 65/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Third report to Microsoft - CVE-2023-36010 bypass
MySQL InnoDB - The patch didn't fix this attack vector
# Quick access
© Pictures
» This PC > Local Disk (C:) » ProgramData > Microsoft > Windows Defender » Platform - 6 earch Piatt
1 item selected
File Eat View Query Ostebese Server
MANAGEMENT
© Server status
BD chert connections
2 select * from persons2}
# Options Fite
PERFORMANCE
& Pertormance Reports
GS Pertormance Schema Setup
1 4
2 4
2
4
Automatic context help is
disabled. Use the toolbar ti
manually get help for the
current c
toggle
t position or te
utomatic help.
© Protection updates
View information about your security intelligence version, and check for
updates.
Security intelligence
Microsoft Defender Antivirus uses security intelligence to detect threats.
We try to automatically download the most recent intelligence to protect
your device against the newest threats. You can also manually check for
updates.
Security intelligence version: 1.403.474.0
Version created on: 13/12/2023 19:07
Last update: 13/12/2023 2.
© Update successful.
```

## Slide 81

###### Third report to Microsoft  - CVE-2023-36010 patch bypass

The patch fixed MySQL MYIASM remote deletion The patch implemented a whitelisting:

1. Each record starts with 0xFD

2. Each Record is 256 bytes size

First Record

Its OK,
I know this guy

Second record

**81**

## Slide 82

###### Third report to Microsoft  - CVE-2023-36010 patch bypass

Whitelist conditions:

1. Starts with 0xFD

**2. Each Record is 256 bytes size**

It's a Big guy,
I don’t know
this guy

**82**

## Slide 83

Third report to Microsoft  - CVE-2023-36010 MYISASM Patch bypass

Record 256 bytes length

Record Size bigger than 256 Including binary signature

**83**

## Slide 84

###### Third report to Microsoft  - CVE-2023-36010 bypass

|**Fixed Attack Vectors**|**unFixed Attack vectors**|
|---|---|
|Remote deletion of WindowsEvent Log file|Remote deletion ofMySQL database MYIASM+InnoDB|
|Unprivileged deletion of WindowsEvent Log file|Remote deletion ofMariaDB database|
|VMware deletion ofVMDK file|Remote deletion ofPostGRESQL database|
||Remote deletion ofMongoDB database|
||Remote deletion ofIIS log file|
||Remote deletion ofApache log file|
||Remote deletion ofNGnix log file|
||Remote Deletion ofFilezilla server log file|
||VMware deletion ofVMX file|
||Unprivileged deletion ofDefender detections Log file|

**84**

## Slide 85

###### Third report to Microsoft  - Windows Defender bypass

The patch fixed MySQL MYIASM remote deletion The patch implemented a whitelisting:

1. Each record starts with 0xFD

2. Each Record is 256 bytes size

Its OK, I know this guy

First Record

Second record

**85**

## Slide 86

###### Third report to Microsoft  - Windows Defender bypass

###### Recipe FUD

**1. 0xFD in the beginning of a known Powershell malware script.**

2. Powershell command to ignore exceptions ?

3. comment to align the size of the Powershell malware file to 256 bytes size.

Its OK, I know this guy

0xFD

**86**

**#AAAAAAAAAAA**

## Slide 87

###### Third report to Microsoft  - Windows Defender bypass

###### Recipe FUD

**1. 0xFD in the beginning of a known Powershell malware script.**

**2. Powershell command to ignore exceptions**

**3. comment to align the size of the Powershell malware file to 256 bytes size.**

**87**

## Slide 88

###### Third report to Microsoft  - Windows Defender bypass

**POWER 0XFD =** Power **F(** U) **D = Power Fully Un-Detectable**

0XFD + ignore error and continue Add comment to Align size to 256 bytes

0xFD

#AA

**88**

## Slide 89

###### Microsoft Response for Remote deletion last bypass

_“We appreciate the responsible disclosures and feedback from the security researcher Tomer Bar & and Shmuel Cohen, who reported a technique that could potentially cause data loss by injecting malicious content into files that are scanned by Microsoft Defender. We have thoroughly investigated these issues and_ **_implemented several improvements to our detection and remediation logic_** _, as well as our_ **_built-in exclusions_** _, to_ **_reduce the risk of false positives and data loss_** _._

_We also offer our customers the option to_ **_configure Defender_** _in a mode where_ **_no automatic actions are taken_** _, and all remediation actions are quarantined by default._

**_We believe that our current approach strikes a good balance between mitigating the risks and providing the functionality that our users expect from a security product._** _We will continue to look for potential improvements in future releases and welcome the ongoing feedback from the security community."_ **89**

## Slide 90

###### Microsoft Response for Generic Defender bypass

###### **<u>Windows Defender Bypass</u>**

**90**


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
l Microsoft Response for Generic Defender bypass
Windows Defender Bypass
Thank you again for submitting this issue to Microsoft.
We determined that a fix will not be released for the reported behavior.
After further investigation, your submission has been deemed to be Windows Defender bypass, not a security vulnerability as defined by Microsoft.
According to Microsofts Security Servicing Criteria for Windows, a bypass of a defense-in-depth security feature by itself does not pose a direct
risk.
This is because an attacker must also have found a vulnerability that affects a security boundary, or they must rely on additional techniques, such as social
engineering, to achieve the initial stage of a device compromise. In other words, while bypasses are important to address, they are not
necessarily considered standalone security vulnerabilities.
90
```

## Slide 91

###### Vulnerability Timeline

**First Report CVE-2023-24860 Second Report CVE-2023-36010 to MSRC Patch Bypass**

**Third Report Patch Bypass Defender bypass**

**January April 2023 2023**

**August December 2023 2023**

**January February 2024 2024 April 2024 Microsoft Response**

91

## Slide 92

###### GitHub - **EDRaser**

**EDRaser https://github.com/SafeBreach-Labs/EDRaser**

92

## Slide 93

###### Takeaways

1. Remote deletion vulnerabilities are difficult to fix especially when the security controls relays on byte signature detection

2. Security patches might be incomplete, patching should not be treated as a magic bullet and other security layers should protect against single point of failure.

3. Security patches fixing vulnerabilities in security controls might introduce bypasses and unexpected behaviors

**93**

## Slide 94

LABS

#### **Thank you!**

Tomer Bar

Shmuel Cohen
