---
title: "EDR = Erase Data Remotely, By Cooking An Unforgettable (Byte) Signature Dish"
speakers: ["Tomer Bar", "Shmuel Cohen"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/Tomer Bar & Shmuel Cohen_EDR = Erase Data Remotely, By Cooking An Unforgettable (Byte) Signature Dish.pdf"
pages: 80
sha256: "f3c1ab433047d972a15981edd499f649ad80e910db42c1125ffe3a3bb5545c4e"
text_chars: 31632
ocr_pages: 37
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:25:41Z"
---
# EDR = Erase Data Remotely, By Cooking An Unforgettable (Byte) Signature Dish

**Speakers:** Tomer Bar, Shmuel Cohen  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Tomer Bar & Shmuel Cohen_EDR = Erase Data Remotely, By Cooking An Unforgettable (Byte) Signature Dish.pdf` (80 pages)


## Slide 1

LABS

**EDR = E** rase **D** ata **R** emotely by cooking unforgettable (byte) signature dish

Tomer Bar

Shmuel Cohen

## Slide 2

# **Tomer Bar**

###### **VP of Security Research @ SafeBreach**

- **This talk is SafeBreach’s 10th talk** at **Black Hat USA**

- 20 years experience in security research

- Main focus in APT and vulnerability research

- ● Presented at many global security conferences Such as: Black Hat USA 2020, DEFCON 28-30

- Qualified to speak 3 talks at Black Hat, DEFCON 2023

2

## Slide 3

## **Shmuel Cohen**

###### **Security Researcher @ SafeBreach**

- 5 years experience in cybersecurity

- Main focus in vulnerability research

- Former malware researcher specialized In APT groups LABS

3

## Slide 4

###### Agenda

● Research Goal and approach

● Discover the vulnerability - Step by step description

● Attack vectors

●Lessons learned, Vendor response, Github, Q&A

4

## Slide 5

Context - our recent year EDR’s Arbitrary delete vulnerabilities

●First EDR Research - **Aikido** Misleading Defender to delete the wrong signature by using Junction and TOCTOU attack

5

## Slide 6

Context - our recent year EDR’s Arbitrary delete vulnerabilities

●Second EDR Research - **Defender-Pretender** Take over the EDR by updating the signature’s database. The added custom signature deleted all legit files.

Local attacks **Remote attacks**

6

## Slide 7

###### Research Goal -  Trigger False Positives

OMG It’s Taylor Swift

7

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Research Goal - Trigger False Positives
OMG It’s Taylor Swift
Windows
Defender
```

## Slide 8

###### Research Goal -  Trigger False Positives

**It’s The Devil! Destroy it**

8

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Research Goal - Trigger False Positives
It’s The Devil!
Destroy it
©
Windows
Defender |
```

## Slide 9

Teaser

**What will you say if we can remotely delete critical files over the internet, Pre-authentication, Exploit multiple vulnerable Security controls both on Windows and Linux from your Fully patched servers**

Byte signature do bites

9

## Slide 10

###### The Challenges

Byte signature 2 engine are considered as the most trusted and accurate  layer

1

Remote ~~1~~ 2 Triggering

FP is a known issue and most 3 <u>were already been</u> fixed

10

## Slide 11

##### Step 1

Extracting EDR’s Byte-Signatures

## Slide 12

###### Black Box Approach

12

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Black Box Approach
Black Box
INPUT OUTPUT
Input is converted
into output
```

## Slide 13

13

###### Windows Defender signature hunting

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Windows Defender signature hunting
microsoft:infected size:200-
microsoft:infected size:200-
FILES 20/3.61K
131F95C510C819465FA1797F 6CCACFOD494AAAFF46FA3EAC73AE63FFBDFD8267
(a) %2Fhome%2Fazureuser%2Fclamav-scans2Fclamav-testfile
text attachment _via-tor
275A021B8FB6489E54047 1899F 7DB90 1663FC695EC2FEZAZC 453BAABF6S 1 FOF
@ © eicar.com-30630
text known-distributor attachment — via-tor
2546DCFFCSAD854D4DDC64FBF@5687 1 CD5AGQF247 1CB7A5BFD4AC23B6ESEEDAD
© @ © eicar_com.zip
Zip attachment —via-tor
381EE 12E67A5C026528129A264844E7F 10291 143652F 38E465872A3BEC572C9
© @ © Ii-test-eicar.cnd
javascript direct-cpu-clock-access
B86F2572F538B9893648GA9729AAAF73020F 4A3E0233DAF582061439A8359C58
analysis. log. 1nk
Ink cve-2010-2568 exploit
9360941105226B7C5A15CECAF42298759GA8870C8EQ95E 1CAR27227304 1 ABGE7
C:\Users\user\AppData\Local \Temp\23774625. bat
javascript
Detections
56 / 63
65 / 68
61/65
21/61
46 /62
29/60
Sort by
Size
69B
68B
184B
92B
198B
13
```

## Slide 14

###### First Signature Example

14

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
First Signature Example
1 4 © 14 security vendors and no sandboxes flagged this file as malicious (Ey Py
/59
186830672901 fceabe228a09f9eb42fc7c459e448a42299c088b072c09002aff 2020-09-10 13:57:53 UTC D
Debunkio.vbs 2 years ago
-
create-ole direct-cpu-clock-access run-file send-keys vba
%X Community Score V
DETECTION DETAILS BEHAVIOR CONTENT TELEMETRY COMMUNITY
Security vendors’ analysis on 2020-09-10T13:57:53UTC v
Ad-Aware © Trojan.Joke.PXP ALYac © Trojan.Joke.PXP
Arcabit © Trojan.Joke.PXP Baidu © VBS.Trojan.BadJoke.d
BitDefender © Trojan.Joke.PXP Emsisoft © Trojan.Joke.PXP (B)
eScan © Trojan.Joke.PXP GData © Trojan.Joke.PXP
MAX © Malware (ai Score=88) [ Microsoft © Joke:VBS/Trier.A ]
NANO-Antivirus © Trojan.Script.Agent.dbvrvq Rising © Joke. Trier!8.167A (TOPIS:E0:WQAItE6Ks
Sangfor Engine Zero © Malware Trellix (FireEye) © Trojan.Joke.PXP
```

## Slide 15

How to manually minimize a signature ?

- Example, let’s assume entire malicious file content is : “XABCY”

- Remove “X”, write “ABCY” to disk -> detection   -> “X” is <u>not</u> part of the signature

- ● Remove “A”, write “BCY” to disk -> no detection -> “A” is part of the signature

- Remove “B”, write “ACY” to disk -> no detection -> “B” is part of the signature

- Remove “C”, write “ABY” to disk -> no detection -> “C” is part of the signature

- Remove “Y”, write “ABC” to disk -> detection      -> “Y” is <u>not</u> part of the signature

   - The signature is “ABC”

15

## Slide 16

###### Windows Defender signature  - Joke:VBS/Trier.A

- Set wshShell=wscript.CreateObjectdo wscript.sleep wshshell.sendkeysloop

- ● Alert level: medium -> only manual operations -> File is not deleted

16

## Slide 17

Windows Defender Byte Signatures

## Slide 18

###### Windows Defender  - RTFM

18

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Windows Defender - RTFM
class MSFT_MpThreat : BaseStatus
{
string SchemaVersion = 1.0.0.0";
sint64 ThreatID;
string ThreatName;
uint8  SeverityID; )
uint8 CategoryID;
uint8 TypeID;
uint32 RollupStatus;
string Resources[];
boolean DidThreatExecute = false;
boolean IsActive = false;
Learn / Windows / Customize / Desktop customizations / ©
ThreatSeverityDefaultAction
Article + 12/17/2020 + 2 minutes to read + 4 contributors 4 Feedback
ThreadSeverityDefaultAction configures the default action to be taken for a threat alert that Microsoft Defender takes.
Microsoft Defender is an application that can prevent, remove, and quarantine malware (malicious software) and spyware.
Child Elements
Setting Description
Low Specifies the default action to take for threat alert identified as Low.
Moderate Specifies the default action to take for threat alert identified as Moderate.
High Specifies the default action to take for threat alert identified as High.
Severe Specifies the default action to take for threat alert identified as Severe.
```

## Slide 19

###### Windows Defender  - RTFM

19

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Windows Defender - RTFM
CAutoScan: :ActibnStringFromID(enum tagMPTHREAT_ACTION)
jz short loc_149012435| loc_14001243E:
lea rax, aClean 3 "Clean"
evere cetn
?ActionStringFromID@CAutoScan@@AEAAP!
Article - 12/17/2020 + 2 minutes to read + 5 contributors
al ca
Severe specifies the automatic remediation action taken for detected threats with a Severe alert level. 14001242c}_ |1oc_140012435:
lea rax, aQuarantine ; “Quarantine”
retn
———
Values ———
4001242C:
rax, aRemove 3 "Remove"
1 Clean the detected threat.
2 Quarantine the detected threat.
3 Remove the detected threat. -
6 Allow the detected threat.
8 Allow the user to determine the action to take with the detected
threat.
| Do not take any action.
10 Block the detected threat.
NULL Apply action based on the update definition. This is the default
value.
```

## Slide 20

###### Windows Defender - RTFM

20

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Windows Defender - RTFM
class MSFT_MpThreatDetection : BaseStatus
{
string DetectionID;
sint64 ThreatID;
string ProcessName;
string DomainUser;
uints DetectionSourceTypeID;
string Resources[];
DateTime InitialDetectionTime;
DateTime LastThreatStatusChangeTime;
DateTime RemediationTime;
uints CurrentThreatExecutionStatusID;
uints ThreatStatusID;
sint32 ThreatStatusErrorCode;
uints CleaningActionID;
string AMProductVersion = tatusID;
boolean ActionSuccess = false;
Uint32 [ AdditionalactionsBitMask;
None (0)
FullScanRequired (4)
RebootRequired (8)
FullScanAndRebootRequired (12)
ManualStepsRequired (16)
FullScanAndManualStepsRequired (20)
RebootAndManualStepsRequired (24)
FullScanAndRebootAndManualStepsRequired (28)
OfflineScanRequired (32768)
FullScanAndOfflineScanRequired (32772)
RebootAndOfflineScanRequired (32776)
FullScanAndRebootAndOfflineScanRequired (32780)
ManualStepsAndOfflineScanRequired (32784)
FullScanAndManualStepsAndOfflineScanRequired (32788)
RebootAndManualStepsAndOfflineScanRequired (32792)
FullScanAndRebootAndManualStepsAndOfflineScanRequired (32796 )
```

## Slide 21

###### Windows Defender signature  - Trojan:JS/Recycled.A

- <script>=document.all('recycled')function {}()

- Alert level: **Severe**

21

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Windows Defender signature - Trojan:JS/Recycled.A
e <script>=document.all('recycled')function {}()
Windows Security - o PB 2ret- Not
File Edit Format View Help
e Alert level: Severe oO Virus Rabreat proteetian <script>=document.all(‘recycled’)function {}()
Protection for your device against threats.
9g & Current threats
R Threats found. Start the recommended actions.
@
Trojan:JS/Recycled.A 5
al zanoj20e2 4:23 (Active) severe Tr ‘ojanJS/! Recycled.A S
: evere
i: Action options: 24/10/2022 4:23 (Active)
@ @ Quarantine
A Oypenats Action options:
© Allow on device 7
0) soe detail @) Quarantine
O Remove
O Allow on device
See details
```

## Slide 22

###### Windows Defender signature  - Trojan:JS/Recycled.A

22

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Windows Defender signature - Trojan:JS/Recycled.A
( 3 Firewalls are turned off. Your device may be vulnerable. Yy
| 24/10/2022 4:25
Threat found - action needed. Gan Fe
24/10/2022 4:25
Detected: Trojan:JS/Recycled.A
Status: Active
Active threats have not been remediated and are running on your device.
Date: 24/10/2022 4:25
Details: This program is dangerous and executes commands from an attacker.
Affected items:
containerfile: C:\Users\Safebreach\Desktop\3\333333333333q.txt
file: C:\\Users\Safebreach\Desktop\3\333333333333q.txt->(SCRIPTOO00)
file: C:\Users\Safebreach\Desktop\3\333333333333a.txt->(SCRIPTOO00)
```

## Slide 23

Automatic Signature generation Selecting the “best” signature

## Slide 24

###### Automatic Minimal Signature Generation

- We downloaded all 3.6K files from the original VT query

- Develop a python tool to minimize the binaries into minimal signature as possible

Automatic Minimize

24

## Slide 25

###### Automatic Minimal Signature Generation

- We found 130 unique signatures

25

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Automatic Minimal Signature Generation
e We found 130 unique signatures
@)
EvilSignature Times
{autorun]shellexecute=.exeaction=Openfoldertoviewfile 990
L avcAqa"» a” FA A Aq a—% i+04e" 10:i4-2A 266
115
<FRAME SRC=http:www.searchvity.com/<html> 110
<?phpeval(S_POST[ 80
cdDrivestartwscript"\."exit 77
PKa™¥a™ | 64
aC, ELFa”»a”2a"2 a’»>a? x@ @ @8sa™2 a“2 @ 4 24
X50!P%@AP[4\PZX54(P*)7CC)7}SEICAR-STANDARD-ANTIVIRUS-TEST-FILE! SH+H * 17
<%evalrequest("")%> 14
<?phpeval(S_REQUEST[ 13
25
```

## Slide 26

###### Signature Limitations: how to select the best signature?

**Selecting the best signature:** **LESS is MORE**

Minimum Limitations =

1. Minimum special characters 2. Minimum length

###### **LESS is MORE**

26

## Slide 27

###### Signature Limitations: how to select the best signature

###### minimum special types signatures

27

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Signature Limitations: how to select the best signature
minimum special types signatures
special |length — |EvilSignature
O2|WDVPIVAIO
15 {\rtfi{\shpf\sp
23|//brembotembo.com/2.dat
NIN INI oO)
26|frompynput.keyboardstr(key
X50! PR@AP[4\PZX54(P*)7CC)7}$EICAR-STANDARD-ANTIVIRUS -TEST-FILE! $H+H*™
The file is a legitimate DOS program, and produces sensible results when run (it prints the
message .EICAR-STANDARD-ANTIVIRUS-TEST-FILE!)
It is also short and simple — in fact, it consists entirely of printable ASCII characters, so that it can
easily be created with a regular text editor. Any anti-virus product that supports the EICAR test file
should detect it in any file providing that the file starts with the following 68 characters, and is
exactly 68 bytes long
```

## Slide 28

###### Signature Limitations: how to select the best signature

###### Shortest signatures with minimum special types

28

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Signature Limitations: how to select the best signature
Shortest signatures with minimum special types
special
llength
EvilSignature
Ni oO
92
15|{\rtf1{\shp{\sp
23
WDVPIVAIQEFQW7zRCUF pYNTQoUF4pNONDKTA9JEVIQOFSL\
//brembotembo.com/2.dat
26
frompynput.keyboardstr(key
51
//operasanpiox.bravepages.com/20190614890563891.xIs
WIN |hM 1h
27
cdDrivestartwscript"\."exit
28
```

## Slide 29

Signature Limitations: how to select the best signature

- {\rtf1{\shp{\sp

- Alert level: Severe File was quarantined automatically

29

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Signature Limitations: how to select the best signature
e {\rtf1{\shp{\sp aiaaie
¢ Alert level: Severe UO Virus & threat protection
File was quarantined automatically Protection for your device against threats.
& Current threats
Threats found. Start the recommended actions.
| cve-2 txt - Notepad
: ” ? Exploit:097M/CVE-2010-3333.PB eeyerel ON
File Edit Format View Help 24/10/2022 4:36 (Active)
{\rtf1{\shp{\sp} Action options:
@) Quarantine
O Remove
O Allow on device
See details
```

## Slide 30

Step 2 Manually embed the signature In Legit File

## Slide 31

###### Failed First attempt

Legit file (non PE)

Legit file (non PE)
RTF signature

31

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Failed First attempt
Legit file (non PE)
RTF signature
FIRST
ATTEMPT
IN
LEARNING
{\rtf1{\shp{\sp
31
```

## Slide 32

Faster Automatic Minimal Signature Generation

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Faster Automatic Minimal Signature Generation
hResult = scanner->Scan(NULL, sample.data, sample.size, &scanResult) ; ]
if (hResult == S_OK)
{
(# (scanResult.IsMalware)
cout << "original is Malware" << endl;
else
{
cout << "original is Benign,exit" << endl;
return;
}
}
for (i = 0; i < sample.size; i++)
{
buffer[i] = 'Z';
sample.data = (BYTE*)buffer;
hResult = scanner->Scan(NULL, sample.data, sample.size, &scanResult);
if (hResult == S_OK)
{
if (scanResult.IsMalware)
{
cout << "[+] Defender verdict: Malware. minimized byte until offset: " << i <<endl;
```

## Slide 33

###### Faster Automatic Minimal Signature Generation

MZ MAGIC

PE

Offsets 0x140 - 0xD0F0 contains ‘Z’ only

###### E_lfanew 0x120

###### 250 bytes signature

33

till file’s end - only ‘Z’

## Slide 34

Faster Automatic Minimal Signature Generation

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Faster Automatic Minimal Signature Generation
Z<.
atizZZ r¢ 2-Zz gez
r 4 at
v4
zZ
2 z 2722 272.
Operation did not complete successfully because the file ed e Z 12 2
| contains a virus or potentially unwanted software, Zz > Z Zz
4 z Ze
= = z 3
ox .
L
©) cutput_from_amsi_minimize.txt - Notepad = o x
File Edit Format View Help
MZZZZZZZZZ. ZZZZ2Z2Z2Z2Z2Z22Z2Z. ZZZZZ. ZZ22ZZ ZZZZZZZZZZ 0 '2Z2Z2Z22Z222222222Z22Z222Z22Z221Z ZZZZZ. ZZZ2ZZ ZZZZZ ZZZZZ '2Z2Z2222Z22222222222222122222222222212222 «
Z2Z2Z222222222222222 2222222222222 2222222222222 2222222222222 222222222222 2222222222222 2222222222222 2222222222222 222222222222 22222222222222222222i
Z2Z22Z22222222222222222222222 2222222222222 2222222222222 2222222222222 2222222222222 2222222222222 2222222222222 2222222222222 2222222222222 2222222222222 2222222222222 22222 22222222222721
Z Z Z Z Z Z Z. Z Z Z Z ZZZZ. ZZZZ. ZZZZ. Z Z Z Z Z Z Z Z. Z Z. Z Z ZZZZ. ZZZZ. ZZZZZi
222222222222227Z: Z2Z2ZZ: 2227: 2227: ZZZZ; 2227; Z2ZZZZ. 22222222222222222222222222222222222727. 2227; ZZZZ. 2227: 2227: Z2ZZZZ. Z22Z2Z222222227i
22222222222222222222222 2222222222222 2222222222222 2222222222222 2222222222222 2 2222222222222 2222222222222 2222222222222 2222222222222 2222222222222 2222222222 2222222222222222222222721
22222222222222222222222222222222222222222222222222222222. '2ZZ2ZZ. '2Z2ZZ. '2Z2ZZ. '2Z22222222222222222222222 2222222222222 2222222222222 2222222222222 '2Z2ZZ. '2Z2ZZ. ri
Zz Z Z 22222 22222 22222 22222 Z Z Z Z Z Z Z 22222 22222 22222 22222 Z Z Z
Z2Z2Z222222222222222 2222222222222 2222222222222 2222222222222 2222222222222 2222222222222 22222222222 22222 2222222222221
2Z2Z222222222222222 2222222222222 2222222222222 2222222222222 2222222222222 2222222222222 2222222222222 AAA A A222 2222222222222 222222222222222221
Zz 222. 222222222222 2222222222222222222. 222. 722. 222. 222. 722. 222222222222 222222222222 Zz. 222. 222. 722. 722.
Z Z Z Z. ZZZZ Z. vA Z. va ZZ Z. ZZ Z Z. va Z z z 222222:
VITTTITITIVITITITAITITAITTITITTITITATTTITITAITITITITITITTITITITITITITTITTITITITITITIVITAITITITTITIITITIITIITITIVATITITITIIITITIVIVAITITITVITAITITITIITIVIIITIITITITIVITIIITITIIIIT
```

## Slide 35

###### PE Files

###### Executable legit file

Mimikatz signature
Mimikatz signature

35

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
PE Files
Executable legit file
Mimikatz signature
SASA
0000
2500
3100
3800
7700
7300
0056
0044
0020
6174
6572
616D
496E
6574
7377
SAG4
OOFO
7800
7500
7800
5a00
004B
0031
0045
6500
6544
7665
456E
446F
5365
6F72
Mimikatz signature
8606 0063 395A SEOO 0000
0022 1244 OFBE 4404 4F00
3B00 2500 7800 SD00 2D00
2D00 2500 7500 2D00 2500
2D00 2500 7700 SA00 4000
2D00 2500 7700 SA00 2E00
0049 0057 0049 OOSF 004D
OOSF 0030 OOS5SF 0043 0052
004E 0054 0049 0041 004c
0011 0053 616D 456E 756D
6F6D 6169 GE73 496E 5361
7200 4D65 6DE6F 7279 0013
7S56D 6572 6174 6555 7365
6D61 696E 0065 0002 0049
7276 6572 5472 7573 7450
6473 4765 7400 0000 0000
0000
SBOO
2500
3000
2500
2500
0053
0045
0053
6572
6D53
0053
7273
SF4E
6173
SASA
BAAGT COA werelese
Brace irs NAG Boys eal Ey
K Poe Snkene See aed Serbs
a ei
8.x.-.%.w.Z.@.%.
er nn a re 8
so -Kii 8b. cM-8
Vite 06 SCORE
-D.E.N.T.I.A.L.S3
- €....SamEnumer
ateDomainsInSams
erver.Memory...S
amEnumerateUsers
InDomain.e...I_N
etServerTrustPas
swordsGet..... ZZ
35
```

## Slide 36

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

36

## Slide 37

Challenge 3 - Attack Vectors implant the signatures in legit files

## Slide 38

###### Implant signature - achieve remote deletion of logs

1. Send HTTP POST request Including signature

2. Signature is written to log file

3. Defender deletes the log 38

## Slide 39

LOGS Remote deletion of Windows Web Server Logs **CVE-2023-24860**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Remote deletion of Windows Web Server Logs
CVE-2023-24860
_i
i
= fide
00=00=3 00F8 oo
```

## Slide 40

###### Remote Deletion of Windows Web Server Logs - Demo

40

## Slide 41

###### Remote Deletion of Windows Web Server Logs

Barking dog **starts to** bite… :) WORKED !!! Defender detect IIS log file as an RTF exploit

41

## Slide 42

###### Remote Deletion of Linux Web Server Logs

The Web server’s market share

42

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Remote Deletion of Linux Web Server Logs
The Web server’s market share
Nginx
Apache
Cloudflare Server
LiteSpeed
Microsoft-IIS
Node.js
Google Servers
Envoy
ET 34.20%
31.4%
ME 21.6%
ME 12.3%
ME 5.9%
M2.1%
1.0%
0.4%
42
```

## Slide 43

###### Remote Deletion of Linux Web Server Logs

43

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Remote Deletion of Linux Web Server Logs
ABILITY TO EXECUTE
CHALLENGERS
@ Trend Micro
@ SentneiOne
@ McAfee
EST @
Firetye @ a
@ Cisco
Broadcom (Symantec)
@ Cybereason
Bitdefender @ Pee GQ spersky
@ BiackBery (Cyiance) @
OO Frinct
‘Check Point Software Technologies
Panda Security, e
NICHE PLAYERS VISIONARIES
COMPLETENESS OF VISION ad As of May 2021 © Gartner, Inc
43
```

## Slide 44

###### EvilSignature DataBase

44

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
EvilSignature DataBase
© oanaounnkwne
1
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
[Filter Filter [Filter Filter Filter Filter Filter lI
<?="$ GET[]"; Windows Microsoft Defender 13 9 False False
{\rtfl{\shp{\sp Windows Microsoft Defender 15 2 False True
<?phpeval($_GET[ Windows Microsoft Defender 16 6 False False
Gif89a\r\n<?php Linux Kaspersky 16 4 True True
:a\r\nstartgoto Linux Kaspersky 16 3 True True
<%eval request(" Linux Kaspersky 16 5 True True
<?php @eval($_POST[ Linux Kaspersky 19 8 True True
<?phpsystem($_POST[ Windows Microsoft Defender 19 6 False False
<%EVAlreQUesT(™)%> Windows Microsoft Defender 19 6 False False
<%EvalreQUesT("")%> Windows Microsoft Defender 19 6 False False
<%evalrequest("")%> Windows Microsoft Defender 19 6 False False
<%evalrequest(")%> Windows Microsoft Defender 19 6 False False
<%evalrequEst("")%> Windows Microsoft Defender 19 6 False False
<%evalrEquEst("")%> Windows Microsoft Defender 19 6 False False
<eval_r(Request("")> Windows Microsoft Defender 20 6 False False
cmd /c rd /s/qc:\\ Linux Kaspersky 20 4 False False
<?phpeval($_REQUEST Windows Microsoft Defender 20 6 False False
<iframe name=twitter Windows Avast 20 3 False False
<?php system($_POST[" Linux Kaspersky 21 8 True True
<?phpsystem($_REQUEST[ Windows Microsoft Defender 22 6 False False
<?phppassthru(getenv(" Windows Microsoft Defender 22 4 False False
rundlI32 mouse,disable Linux Kaspersky 22 2 True True
//brembotembo.com/2.dat Windows Microsoft Defender 23 2 False False
open 210..81.exe\r\nbye Windows AVG 23 3 False True
<iframe name=Twitterlgar Windows AVG 24 3 False False
44
```

## Slide 45

###### Automatic Minimal EvilSignature generation - Linux

AVAST + AVG AVG

Trend Micro

Others: Palo Alto, CrowdStrike, SentinelOne

Relay on By default only works in ML only scan the Don't use files With byte beginning of signatures predefined the file extensions

45

## Slide 46

###### Automatic Minimal EvilSignature generation - AV

One EvilSignature to rule the all

● Kaspersky ● Windows Defender

46

## Slide 47

### LOGS

##### Remote deletion of Linux Web Server Logs

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
00E=00E=a
ares === =] =
40 re yt
of Ero So r—) Sesi00 =
of
oe 1H |
el
0 eS
```

## Slide 48

###### Remote Deletion of Linux Web Server Logs - Ngnix Demo

48

## Slide 49

###### Remote Deletion of Windows Web Server Logs

###### ● The Web server’s market share

49

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Remote Deletion of Windows Web Server Logs
e The Web server’s market share
g Nginx
7) Apache
Cloudflare Server
LiteSpeed
Google Servers
Envoy
EE 34.25%
ET 31.4%
ET 21.6%
MEN 12.3%
ME 5.9%
@2.1%
11.0%
| 0.4%
49
```

## Slide 50

Windows - FTP - Remote Deletion of Filezilla server logs

50

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Windows - FTP - Remote Deletion of Filezilla server logs
word.
HackTool:Win32/Mikatz!dha
Alert level: High
Status: Active
Date: 02/11/2022 8:55
Category: Tool
Details: This program has potentially unwanted behavior.
Learn more
Affected items:
file: C:\Program Files\FileZilla Server\Logs\filezilla-server.log
OK
rtualPr
© Windows Security
Windows Security
Actions needed in Microsoft Defender
Micr A
50
```

## Slide 51

###### Remote deletion of local mailbox - Mozilla ThunderBird

- Send mail to victim with a subject with the EvilSignature

51

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Remote deletion of local mailbox - Mozilla ThunderBird
e Send mail to victim with a subject with the EvilSignature
& Inbox
GetMessages ~ # Write @ Tag © | ti Quick Filter
SP | BuUnresd Gy Starred 8 Contact @ Tog: B Attachment
kab Subject
Add-MemberNoteProperty-NameVirtualProtect-Value$VirtualP rotect33
© Windows Security
Windows Security
O Threat quarantined Actions needed in Microsoft Defender
20/11/2022 3:10 bed
Detected: HackTool:Win32/Mikatz!dha Dismiss
Status: Quarantined
Quarantined files are in a restricted area where they can't harm your device. They will be removed automatically.
Date: 20/11/2022 3:11
Details: This program has potentially unwanted behavior.
Affected items:
file: C:\Users\Safebreach\AppData\Roaming\Thunderbird\Profiles\gz8udxy6.default-release\ImapMail
\imap.gmail.com\INBOX
```

## Slide 52

###### Local - Unprivileged deletion of Windows event log f i le

corrupted msi with

version info includes the signature

Application.evtx is deleted

52

## Slide 53

Remote - Deletion of Windows event log f i le

Failed SMB login attempts, the username includes signature            Security.evtx remotely deleted

53

## Slide 54

###### Remote - Remote Deletion of Windows event log f i le

54

## Slide 55

###### Windows Defender - Delete Windows Defender detection logs

**Self cannibalism** - Defender deletes its own detection logs :)

55

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Windows Defender - Delete Windows Defender detection logs
Self cannibalism - Defender deletes its own detection logs :)
Date: 02/11/2022 1:47 HackToolWin32/Mikatz!dha
Details: This program has potentially unwanted
behavior. Alert level: High
Status: Active
: Date: 21/11/2022 0:17
Affected items: Category: Tool
Details: This program has potentially unwanted behavior.
containerfile: C:\playground\12.msi Learn more
5 ca 5 Affected items:
containerfile: c\P rog ramData\Microsoft containerfile: C:\ProgramData\Microsoft\Windows Defender\Scans\History
\Windows Defender\Scans\History\Service \Service\DetectionHistory\18\E2AA9560-9748-45FD-B6EA-9FFB8F3C4E42
- - tainerfile: C:\ProgramData\Microsoft\Windows Defender\Support
\DetectionHistory $HiGLog Sat ae Hebe
\22\64BA29BD-70EC-400A-854A-61 2ABD9022 file: C:\ProgramData\Microsoft\Windows Defender\Scans\History\Service
AB \DetectionHistory\18\E2AA9560-9748-45FD-B6EA-9FFB8F3C4E42-
>(UTF-16LE)
z ra) . file: C:\ProgramData\Microsoft\Windows Defender\Support
containerfile: C:\ProgramData\Microsoft WA Lg 3001 0onD SHebillog. SUT GLE)
\Windows Defender\Scans\History\Service
\Detections.log ok
```

## Slide 56

###### Windows Defender - Self cannibalism demo

56

## Slide 57

###### EvilSignature - Collateral damage - 2nd phase - Splunk

###### All rivers flow to the sea

57

## Slide 58

###### Domino Effect - Splunk

- All rivers flow to the sea … all logs flow to Splunk

58

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Domino Effect - Splunk
e All rivers flow to the sea
On-
Premises
Private
Cloud
Public
Goud
26
Services
a qo Santen é
Location
Networks
wis a.
Desktops >
Storage ¢
Telecoms
bid ime
Shopping
ig]
Web ca dent
Clickstreams —
Smartphones
and Devices
Security & GPS
Packaged
Applications
Messaging
all logs flow to Splunk
Custom
Applications
@
Meters
Databases
=
reece
i i
fee,
Monitor Report Custom’ —_ Developer
and alert and dashboards Platform
analyze
splunk
References — Coded fields, mappings, aliases
Dynamic information — Stored in non-traditional formats
Environment al context — Human maintained files, documents
System /application — Available only using application request
intelligence /analytics — indicators, anomaly, research, white /blackist
```

## Slide 59

###### EvilSignature - Collateral damage - 2nd phase - Splunk Manually adding log file, the filename includes the EvilSignature

59

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
EvilSignature - Collateral damage - 2nd phase - Splunk
Manually adding log file, the filename includes the EvilSignature
(G wdows30_sser_ prev.
D | BS besin spunk
Set Source Type
ce] 127.004
Add Data
Event
Backdoor:PHP/Remoteshell.B
Alert level: Severe
Status: Active
Date: 08/11/2022 12:36
Category: Backdoor
Details: This program provides remote access to the com,
on.
Learn more
fected items:
file: C:\Program Files\Splunk\var\lib\splunk\defaultdb\db}
\hot_v1_0\rawdata\0
HackTool:SH/PythonKeylogger.B
Alert level: High
Status: Active
Date: 08/11/2022 12:26
Category: Tool
Details: This program has potentially unwanted behavior.
Learn more
Affected items:
file: C:\Program Files\Splunk\var\run\splunk\dispatch
\1667939169.19\indexpreview.csv
file: C:\Program Files\Splunk\var\run\splunk\dispatch
\1667939169.19\info.csv
file: C:\Program Files\Splunk\var\run\splunk\dispatch 59
\1667939169.19\status.csv
```

## Slide 60

###### EvilSignature - Collateral damage - 2nd phase - Splunk

###### ● Splunk collect windows security event logs

60

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
EvilSignature - Collateral damage - 2nd phase - Splunk
e Splunk collect windows security event logs
EventType=0
ComputerName=DESKTOP-6655UUR
Show all 61 lines
Event Actions ¥
Type ~ Field
Selected Y host¥
¥) source ¥
¥ sourcetype ¥
Event Account_Domain v
Account_Name ¥
Value
DESKTOP-6655UUR
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
60
```

## Slide 61

VMWARE - Permanent Denial Of Service

## Slide 62

###### VMWARE - Permanent Denial Of Service

● VMX file contains the configuration data of the guest VM and it’s necessary for the machine to boot up.

62

## Slide 63

###### VMWARE - Permanent Denial Of Service

63

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
VMWARE - Permanent Denial Of Service
john@john-virtual-machine: ~/Desktop
$ vmware-rpctool "info-set guestinfo.detailed.data <%eval request('a')%>"f
```

## Slide 64

###### VMWARE - Permanent Denial Of Service

64

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
VMWARE - Permanent Denial Of Service
john@john-virtual-machine: ~/Desktop
$ vmware-rpctool "info-set guestinfo.detailed.data <%eval request('a')%>"
VMware Workstation unrecoverable error: (vcpu-1)
Failed to reopen dictionary after renaming “C:\Users\Shmuel
\Pocuments\Virtual Machines\Ubuntu 64-bit - Eset32\Ubuntu
64-bit - Eset32. vmx~" to "C:\Users\Shmuel\Documents Virtual
Machines \Ubuntu 64-bit - Eset32\Ubuntu 64-bit -
Eset32.vmx": Error (2)
Alog file is available in "C: \Users\Shmuel\Documents \Virtual
Machines \Ubuntu 64-bit - Eset32\vmware.log™.
You can request support.
To collect data to submit to VMware support, choose “Collect
Support Data™ from the Help menu.
You can also run the “vm-support” script in the Workstation
folder directly.
We will respond on the basis of your support entitlement.
OK
```

## Slide 65

###### VMWARE - Permanent Denial Of Service

65

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
P vware - Permanent Denial Of Service
BUT WAIT
'
THERE'S MORE!
```

## Slide 66

###### VMWARE - Permanent Denial Of Service - Demo

66

## Slide 67

Remote deletion of Production Databases

## Slide 68

###### Remote Deletion of Web Server DataBase - MariaDB

1. Register a new user in a website The user name is the signature

2. Signature is written to backend DB

3. Defender deletes the entire DB.

68

## Slide 69

###### Remote Deletion of Web Server DataBase - MARIADB DEMO

69

## Slide 70

###### Most popular databases worldwide as of August 2022

https://www.statista.com/statistics/809750/worldwide-popularity-ranking-database-management-system

70

## Slide 71

###### Remote Deletion of Web Server DataBase - MySQL - Linux

71

## Slide 72

###### **We were able to remotely delete four different databases**

72

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
We were able to oe delete four different databases
PostgreSQL
My * & @ Boori
1,260.8
1,202.85
72
SQLite
```

## Slide 73

Remote deletion of Browser files in the victim’s computer surfing to a Malicious Web

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Remote deletion of Browser files in the victim's
computer surfing to a Malicious Web
2s
ce)
```

## Slide 74

###### Remote deletion of Browser f i les

###### 1. The browser send HTTP request

2. The server returns the signature in the body of the response

3. The browser logs the response to its own DB, Defender deletes the Browsers DB.

74

## Slide 75

###### Remote deletion of Browser files: Chrome History & Web Data

75

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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
Status: Active r
fault\H
Date: 24/10/2022 17:00 \Default\History
Category: Backdoor
Details: This program provides remote access to the computer it i OK
on.
Learn more
© Windows Security
Affected items:
Windows Security containerfile: C:\Users\Safebreach\AppData\Local\Google\Chrome\User
Data\Default\Sessions\Session_133111283883861 13
Actions needed in Microsoft Defender file: C:\Users\Safebreach\AppData\Local\Google\Chrome\User Data
¢ \Default\Sessions\Session_13311128388386113->(SCRIPTO000)
[ce C:\Users\Safebreach\AppData\Local\Google\Chrome\User Data ]
\Default\Web Data
OK
Dismiss
75
```

## Slide 76

###### Future work - the sky is not the limit

76

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Future work - the sky is not the limit
Microsoft Defender for Cloud
Secure your hybrid-cloud and multicloud workloads
H @
Amazon EKS Amazon EC2
© ©
Azure DNS Key Vault
i @ | a }->
Servers Azure Network Resource
vMssS Layer Manager Kubernetes L
a DP br
> = ® © Gg
© Fs »9
App Services Azure K8s Blob Storage File Storage Maria OB Cosmos DB
So DU SB
Unmanaged Azure SQL MySQL Postgres Unmanaged
KBs sQu sQu
Unmanaged Unmanaged
Kubernetes SQL
oO we &
: On-premises =
3 Kubernetes  SQLServers Servers
Google Compute ©
5) oO GKE Clusters
&
The Sky is net the Limit
It's just the Beginning
76
```

## Slide 77

###### The Problem of False Positives in Signature Based Detection

- The devil is red, older, male, fictional …

- But he has unique tail and horns

- Love letter malware is vbs textual script file

- ● My sql Database file has unique structure

- **It should never be detected as vbs malware!**

## Slide 78

###### Vendor Response

Microsoft: released a fix to the vulnerability: CVE-2023-24860 We reported that the fix is not complete Microsoft classified it as “moderate DOS”, didn’t fix the rest of attack vectors.

Kaspersky: did not release a fix: “This case is can’t be classified as a security vulnerability… We are planning some improvements to mitigate this issue”.

78

## Slide 79

###### GitHub - **EDRaser**

**EDRaser https://github.com/SafeBreach-Labs/EDRaser**

79

## Slide 80

###### LABS

#### **Thank you!**

Tomer Bar

Shmuel Cohen
