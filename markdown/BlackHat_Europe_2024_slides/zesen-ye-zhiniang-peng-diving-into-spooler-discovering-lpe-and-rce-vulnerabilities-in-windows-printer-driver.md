---
title: "Diving into Spooler Discovering LPE and RCE Vulnerabilities in Windows Printer Driver"
speakers: ["ZeSen Ye", "Zhiniang Peng"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2024"
edition: "Europe"
year: 2024
source_pdf: "BlackHat_Europe_2024_slides/ZeSen Ye & Zhiniang Peng_Diving into Spooler Discovering LPE and RCE Vulnerabilities in Windows Printer Driver.pdf"
pages: 71
sha256: "7e4196ef294fea4b75fcb59680f05909a86e6eb855118679749122af538304f8"
text_chars: 22782
ocr_pages: 8
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T22:47:41Z"
---
# Diving into Spooler Discovering LPE and RCE Vulnerabilities in Windows Printer Driver

**Speakers:** ZeSen Ye, Zhiniang Peng  
**Conference:** Black Hat Europe 2024  
**Source:** `BlackHat_Europe_2024_slides/ZeSen Ye & Zhiniang Peng_Diving into Spooler Discovering LPE and RCE Vulnerabilities in Windows Printer Driver.pdf` (71 pages)


## Slide 1

Diving into Spooler: Discovering LPE and RCE Vulnerabilities in Windows Printer Driver

Zesen Ye @ Cyber-Kunlun Dr. Zhiniang Peng <u>@HUST</u> & <u>Cyber-Kunlun</u>

## Slide 2

#### Whoami

Zhiniang Peng <u>@edwardzpeng</u> Associate Professor @ <u>HUST</u> Security Researcher <u>@Cyber-Kunlun</u>

PhD in Cryptography, Work in Defensive & Offensive security Published many research in both Industry & Academia More about me: <u>https://sites.google.com/site/zhiniangpeng HUST：Huazhong University of Science and Technology Cyber-Kunlun：World-Leading Vulnerability Research in China</u>

## Slide 3

#### Some of My Bugs

CVE-2018-20694,CVE-2018-20746,CVE-2018-20693,CVE-2018-20692,CVE-2018-20696,CVE-2018-20689,CVE-2018-20690,CVE-2018-10812,CVE-2019-6184,CVE-2019-6186,CVE-2 019-6487,CVE-2019-1253,CVE-2019-1292,CVE-2019-1317,CVE-2019-1340,CVE-2019-1342,CVE-2019-1374,CVE-2019-8162,CVE-2019-1474,CVE-2019-18371,CVE-2019-18370,CV E-2020-0616,CVE-2020-0635,CVE-2020-0636,CVE-2020-0638,CVE-2020-0641,CVE-2020-0648,CVE-2020-0697,CVE-2020-0730,CVE-2020-3808,CVE-2020-0747,CVE-2020-0753,C VE-2020-0754,CVE-2020-0777,CVE-2020-0780,CVE-2020-0785,CVE-2020-0786,CVE-2020-0789,CVE-2020-0794,CVE-2020-0797,CVE-2020-0800,CVE-2020-0805,CVE-2020-0808, CVE-2020-0819,CVE-2020-0822,CVE-2020-0835,CVE-2020-0841,CVE-2020-0844,CVE-2020-0849,CVE-2020-0854,CVE-2020-0858,CVE-2020-0863,CVE-2020-0864,CVE-2020-0865 ,CVE-2020-0868,CVE-2020-0871,CVE-2020-0896,CVE-2020-0897,CVE-2020-0899,CVE-2020-0900,CVE-2020-0934,CVE-2020-0935,CVE-2020-0936,CVE-2020-0942,CVE-2020-094 4,CVE-2020-0983,CVE-2020-0985,CVE-2020-0989,CVE-2020-1000,CVE-2020-1002,CVE-2020-1010,CVE-2020-1011,CVE-2020-1029,CVE-2020-1068,CVE-2020-1077,CVE-2020-10 84,CVE-2020-1086,CVE-2020-1090,CVE-2020-1094,CVE-2020-1109,CVE-2020-1120,CVE-2020-1121,CVE-2020-1123,CVE-2020-1124,CVE-2020-1125,CVE-2020-1131,CVE-2020-1 134,CVE-2020-1137,CVE-2020-1139,CVE-2020-1144,CVE-2020-1146,CVE-2020-1151,CVE-2020-1155,CVE-2020-1156,CVE-2020-1157,CVE-2020-1158,CVE-2020-1163,CVE-20201164,CVE-2020-1165,CVE-2020-1166,CVE-2020-1184,CVE-2020-1185,CVE-2020-1186,CVE-2020-1187,CVE-2020-1188,CVE-2020-1189,CVE-2020-1190,CVE-2020-1191,CVE-2020 -1196,CVE-2020-1199,CVE-2020-1201,CVE-2020-1204,CVE-2020-1209,CVE-2020-1211,CVE-2020-1217,CVE-2020-1222,CVE-2020-1231,CVE-2020-1233,CVE-2020-1235,CVE-202 0-1244,CVE-2020-1257,CVE-2020-1264,CVE-2020-1269,CVE-2020-1270,CVE-2020-1273,CVE-2020-1274,CVE-2020-1276,CVE-2020-1277,CVE-2020-1278,CVE-2020-1282,CVE-20 20-1283,CVE-2020-1304,CVE-2020-1305,CVE-2020-1306,CVE-2020-1307,CVE-2020-1309,CVE-2020-1312,CVE-2020-1317,CVE-2020-1337,CVE-2020-1344,CVE-2020-1346,CVE-2 020-1347,CVE-2020-1352,CVE-2020-1356,CVE-2020-1357,CVE-2020-1360,CVE-2020-1361,CVE-2020-1362,CVE-2020-1364,CVE‑2020‑5957,CVE-2020-1366,CVE-2020-1372,CVE-2 020-1373,CVE-2020-1375,CVE-2020-1385,CVE-2020-1392,CVE-2020-1393,CVE-2020-1394,CVE-2020-1399,CVE-2020-1404,CVE-2020-1405,CVE-2020-1424,CVE-2020-1427,CVE2020-1441,CVE-2020-0518,CVE-2020-1461,CVE-2020-1465,CVE-2020-1472,CVE-2020-1474,CVE-2020-1475,CVE-2020-1484,CVE-2020-1485,CVE-2020-1511,CVE-2020-1512,CVE -2020-0516,CVE-2020-1516,CVE-2020-1517,CVE-2020-1518,CVE-2020-1519,CVE-2020-1521,CVE-2020-1522,CVE-2020-1524,CVE-2020-1528,CVE-2020-1538,CVE-2020-8741,CV E-2020-1548,CVE-2020-1549,CVE-2020-1550,CVE-2020-1552,CVE-2020-1590,CVE-2020-1130,CVE-2020-16851,CVE-2020-16852,CVE-2020-1122,CVE-2020-1038,CVE-2020-1708 9,CVE-2020-16853,CVE-2020-16879,CVE-2020-16900,CVE-2020-16980,CVE-2020-17014,CVE-2020-17070,CVE-2020-17073,CVE-2020-17074,CVE-2020-17075,CVE-2020-17076,C VE-2020-17077,CVE-2020-17092,CVE-2020-17097,CVE-2020-17120,CVE-2021-1649,CVE-2021-1650,CVE-2021-1651,CVE-2021-1659,CVE-2021-1680,CVE-2021-1681,CVE-2021-1 686,CVE-2021-1687,CVE-2021-1688,CVE-2021-1689,CVE-2021-1690,CVE-2021-1718,CVE-2021-1722,CVE-2021-24072,CVE-2021-24077,CVE-2021-3750,CVE-2021-24088,CVE-20 21-26869,CVE-2021-26870,CVE-2021-26871,CVE-2021-26885,CVE-2021-28347,CVE-2021-28351,CVE-2021-28436,CVE-2021-28450,CVE-2021-31966,CVE-2021-34527,CVE-202142321,CVE-2021-36970,CVE-2021-38657,CVE-2021-40485,CVE-2021-41366,CVE-2021-42294,CVE-2021-42297,CVE-2021-43216,CVE-2021-43223,CVE-2021-43248,CVE-2022-218 35,CVE-2022-21837,CVE-2022-21878,CVE-2022-21881,CVE-2022-21888,CVE-2022-21971,CVE-2022-21974,CVE-2022-21992,CVE-2022-23285,CVE-2022-23290,CVE-2022-24454, CVE-2022-29108,CVE-2022-24547,CVE-2022-23270,CVE-2022-26930,CVE-2022-29103,CVE-2022-29113,CVE-2022-38036,CVE-2022-35793,CVE-2022-35755,CVE-2022-35749,CV E-2022-35746,CVE-2022-34690,CVE-2022-21980,CVE-2022-22050,CVE-2022-22024,CVE-2022-22022,CVE-2022-30226,CVE-2022-30157,CVE-2022-29108,CVE-2022-21999,CVE-2 023-21683,CVE-2023-21684,CVE-2023-21693,CVE-2023-21801,CVE-2023-23403,CVE-2023-23406,CVE-2023-23413,CVE-2023-24856,CVE-2023-24857,CVE-2023-24858,CVE-2023 -24863,CVE-2023-24865,CVE-2023-24866,CVE-2023-24867,CVE-2023-24907,CVE-2023-24868,CVE-2023-24909,CVE-2023-24870,CVE-2023-24872,CVE-2023-24913,CVE-2023-24 876,CVE-2023-24924,CVE-2023-24883,CVE-2023-24925,CVE-2023-24884,CVE-2023-24926,CVE-2023-24885,CVE-2023-24927,CVE-2023-24886,CVE-2023-24928,CVE-2023-24887 ,CVE-2023-24929,CVE-2023-28243,CVE-2023-28296,CVE-2023-29366,CVE-2023-29367,CVE-2023-32017,CVE-2023-32039,CVE-2023-32040,CVE-2023-32041,CVE-2023-32042,CV E-2023-32085,CVE-2023-35296,CVE-2023-35302,CVE-2023-35306,CVE-2023-35313,CVE-2023-35323,CVE-2023-35324,CVE-2023-36898,CVE-2023-36792,CVE-2023-36704,CVE-2 023-36418,CVE-2023-36395,CVE-2023-36393,CVE-2023-35624,CVE-2023-21683,CVE-2023-29366,CVE-2023-46138,CVE-2023-42820,CVE-2023-42819,CVE-2024-21426,CVE-2024 -29156,CVE-2024-26198,CVE-2024-21435,CVE-2024-21329,CVE-2024-21384,CVE-2024-20691,CVE-2024-21433,CVE-2024-20694,CVE-2024‑0087,CVE-2024-0088,CVE-2024-3006 0,CVE-2024-29989,CVE-2024-38077,CVE-2024-38024,CVE-2024-38023,CVE-2024-38076,CVE-2024-38074,CVE-2024-38073,CVE-2024-35261,CVE-2024-38072,CVE-2024-38071,C VE-2024-38015,CVE-2024-43467,CVE-2024-43455,CVE-2024-38231,CVE-2024-38258,CVE-2024-43454,CVE-2024-38263,CVE-2024-38260,CVE-2024-38228,CVE-2024-43495,CVE2024-43470,CVE-2024-38225, CVE-2024-43467,CVE-2024-38097,CVE-2024-38262,CVE-2024-43583C

## Slide 4

#### Whoami

Zesen Ye

Security Researcher <u>@Cyber-Kunlun</u> Focus on Fuzzing & Windows Applications MSRC MVR in 2022 ~ 2024

<u>Cyber-Kunlun：World-Leading Vulnerability Research</u> The largest vulnerability research lab in China Mission: To secure the digital world through cutting-edge vulnerability insights

## Slide 5

##### Agenda

1. Introduction

2. New Attack Surface – Windows Printer Driver Rendering

3. Dive into the XPS Format

4. Vulnerability in Resource Parsing

5. Vulnerability in XML Parsing

6. Vulnerability in Third-Party Driver

7. Mitigations

8. Summary

## Slide 6

Introduction

## Slide 7

### Print Spooler

A Windows Service Spools print jobs

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Print Spooler
A Windows Service Spools print jobs
File Action View
<2 Be om Print Spooler Properties (Local Computer)
Services (Local) Sanesloc General LogOn Recovery Dependencies
Print Spooler Name Servicename:  EEEEIEY
Parental Controls
, Payments and NFC/SE Manager
, Peer Name Resolution Protocol Description
the service Display name Print Spooler
the service ‘This service spools print jobs and handles interaction a
with the printer. If you tum off this service, you won't
, Peer Networking Grouping fo aaaepes veacucemsas
v
Tee soopte print jobs and Peer Networking Identity Manager Paths to executable:
hadi Pssermsivwah the aitaee iieteeren caer Host CAWINDOWS \System32\spoolsv.exe
'erformance Logs lerts
Beobleto pintorsecyor pide” UR Ehone Sica. Satetee: = ae
, Plug and Play
. PNRP Machine Name Publication Service
, Portable Device Enumerator Service Service status: Running
. Power
& Print Spooler
, Printer Extensions and Notifications You can specify the start parameters that apply when you start the service
PrintWorkflow_30546bc from here.
}, Problem Reports and Solutions Control Pane|
Stop
, Program Compatibility Assistant Service
, Quality Windows Audio Video Experience
Radio Management Service
. Realtek Audio Universal Service |
, Recommended Troubleshooting Service Enables aut. Manual
, Remote Access Auto Connection Manager Creates aco Manual
\ Extended A Standard /
```

## Slide 8

Spooling

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Spooling
Document A
Desktop
Papercut”
Document B Spooling
Document C
Tablet
```

## Slide 9

##### Printer Spooler

Add, remove and configure printer Spool high-level function calls into printer jobs Receive and schedule printer jobs for printing

Localspl.dll
(locally)
RPC
Applications Spoolsv.exe
Win32spl.dll
(remotely)

## Slide 10

##### Previous research

Evil Printer: How To Hack Windows Machines With Printing Protocol - Zhipeng Huo and Chuanda Ding

A Decade After Stuxnet's Printer Vulnerability: Printing is Still the Stairway to Heaven - PELEG HADAR and TOMER BAR

Diving in to Spooler: Discovering LPE and RCE Vulnerabilities in Windows Printer - Zhiniang Peng, Xuefeng Li and Lewis Lee

Windows Security Research: A Practical Guide for Beginners to find 0 days - Oliver Lyak

## Slide 11

### Print Spooler is hot in Cyber Security

1. The Spooler used to run with high privileges and load code from the network which is prone to security issues

2. Print bugs account for 9% of all Windows cases reported to <u>.</u>

Microsft according to <u>MSRC blog</u>

3.  A lot Exploited vuls in Spooler in the pasts years

4.  Stuxnet, PrintNightmare ……

## Slide 12

##### Exploited vuls in the pasts years

MS10-061 （Stuxnet） CVE-2020-1048（PrintDemon） CVE-2021-34527（PrintNightmare） Remote Code Execution Elevation of Privilege Remote Code Execution …… CVE-2020-1030 CVE-2021-1675（PrintNightmare） CVE-2022-41073 Elevation of Privilege Remote Code Execution Elevation of Privilege

## Slide 13

### Spooler Vulnerability Types

Path Redirection Attacks(Symbol Link): Exmaple:CVE-2020-1048,... Path Traversal: Exmaple:CVE-2020-1300,... Arbitrary Dll Loading: Exmaple:PrintNightmare,... Memory Corruption: Exmaple:CVE-2021-24077, …

…

## Slide 14

##### PrintNightmare

Computer B
Computer A
RpcAddP rinterDriver
Crafted Remote RPC Call
Print Spooler
LoadLibrary
Evil.dll

More story about PrintNightmare:

Diving in to Spooler: Discovering LPE and RCE Vulnerabilities in Windows Printer Zhiniang Peng, Xuefeng Li and Lewis Lee

## Slide 15

##### After PrintNightmare

In 2022, Microsoft fixed 36 vulnerabilities for Print Spooler.

Microsft’s fix Broken Print Spooler for many times.

## Slide 16

##### Mitigation after PrintNightmare

Block path redirection attacks

Block arbitrary DLL Loading

## Slide 17

Is Spooler secure after all the fix?

Let’s dive into Spooler,Again!

## Slide 18

The New Attack Surface Windows Printer Driver Rendering

## Slide 19

##### New attack surface

###### Review the Architecture from MSDN

Complex?
Rendering?
Bugs!

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
New attack surface
Review the Architecture from MSDN
Complex?
i ?
Rendering? Bugs!
mapping p Bag: fe
it ¥ . it \
DevModeMap Printer Config wut
oct} Rooeweiee ek {GPo/PPD}
uavascript
iu L 4
Bidi Extension
heen Bidiedension |,
avaSeript)
```

## Slide 20

Print example
Let’s print a document
Rendering
Office Docmuents Printer Driver Printer

##### Print example

Let’s print a document

## Slide 21

Details
GDI Application （User Mode） Spooler （System Mode）
Driver
RPC
Microsoft XPS
XPS Spool
Document Converter
Doc XPS
Rendering
XPS -> Printer Control Language

## Slide 22

##### V3 print driver & V4 print driver

V3 mode V4 mode
     GDI Application        GDI Application
         Spoolsv.exe
       Spoolsv.exe
(V3 printer driver)
 printfilterpipelinesvc.exe
(V4 printer driver)
V3 mode :  a crash in rendering will DOS entire spooler service.
V4 mode :  a crash in rendering will restart printfilterpipelinesvc.exe

## Slide 23

Q: What Rendering Issue Impacts?

A: LPE & RCE

## Slide 24

###### LPE Attack Scenario (Medium2System)

Computer A (Medium user)

Computer A (System service)

Malicious XPS Print API

printer driver

## Slide 25

###### RCE Attack Scenario (RCE over SMB)

Computer B
Computer A
Malicious XPS
Print API
Shared
SMB
printer driver

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
RCE Attack Scenario (RCE over SMB)
Computer A Computer B
] Py Malicious XPS = | —
Print API : —_7
SMB Shared
printer driver
```

## Slide 26

###### RCE Attack Scenario (RCE over RDP)

Computer A Computer B
RDP client
printer driver
2.use RDP channel to connect Printer
3.use print api to request print
1.Connect to A’s RDP

## Slide 27

Dive into the XPS Format

## Slide 28

###### Open XML Paper Specification

Hex XML
| Ascii
50 4B 03 04 | PK.. extract
view binrary
XPS
ZIP Magic number
Resource

## Slide 29

###### Open XML Paper Specification

1.fpage

<Path> <Path.Fill> <SolidColorBrush Color="#0000FF" /> </Path.Fill> <Path.Data> <PathGeometry> <PathFigure StartPoint="10,10" IsClosed="true"> <PolyLineSegment Points="50,200 100,40 150,200 200,10 100,105" /> </PathFigure> </PathGeometry> </Path.Data> </Path>

###### content

render

## Slide 30

##### How to print

**GDI Print API** .docx / .pdf / .html -> .xps -> spooler

**XPS Print API** .xps -> spooler

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
How to print
e .
| | .docx / .pdf / .html > .xps > spooler
XPS Print API SBS ALE
4
¥ ¥
XPS Print API SAS
|
v ¥
| -xpsS — spooler
```

## Slide 31

How to use XPS Print API

XPS Viewer, but it was deprecated by Microsoft

## Slide 32

##### How to use XPS Print API

Make our Application as the harness:

HRESULT StartXpsPrintJob( [in]  LPCWSTR            printerName, [in]  LPCWSTR            jobName, [in]  LPCWSTR            outputFileName, [in]  HANDLE             progressEvent, [in]  HANDLE             completionEvent, [in]  UINT8              *printablePagesOn, [in]  UINT32             printablePagesOnCount, [out] IXpsPrintJob       **xpsPrintJob, [out] IXpsPrintJobStream **documentStream, [out] IXpsPrintJobStream **printTicketStream );

Local: Microsoft PS Class Driver Remote: \\smb\Microsoft PS Class Driver

IStream::Read(XPS file stream)

## Slide 33

Vulnerability in Resource Parsing

## Slide 34

###### ODTTF (Obfuscated OpenType Font)

XPS supports the use of custom embedded fonts to promote diversity, but obfuscation is required

for i in range(16):
real_header[i]   = obf_header[i]    ^ key[15-i]
real_header[i+16]= obf_header[i+16] ^ key[15-i]
deobfuscate
key.odtff key.tff

## Slide 35

##### Font

Many researches on fonts before, so we won't dive into the structure of fonts here

We primarily referred to "One font vulnerability to rule them all #1: Introducing the BLEND vulnerability." Posted by Mateusz Jurczyk of Google Project Zero

## Slide 36

CVEs in Parsing Font

Microsoft Printer Driver Remote Code Execution Vulnerability CVE-2023-21684 CVE-2023-21801 CVE-2023-23403 CVE-2023-24876

Microsoft Printer Driver Information Disclosure Vulnerability CVE-2023-21693 CVE-2023-24857 CVE-2023-24858 CVE-2023-24865 CVE-2023-24866

## Slide 37

##### Case 1

CVE-2023-24863 Microsoft PostScript and PCL6 Class Printer Driver Information Disclosure Vulnerability

It is an out-of-bounds-read vulnerability in TrueType Parsing

The offset was not checked during the parsing of the glyf table

The unique point here is the crash call stack：

1. msvcrt!memcpy+0x92

2. MSxpsPCL6!cmnStreamBuffered::write+0x85

## Slide 38

##### Case 1

Print to File
Printer Command Language file
cmnStreamBuffered::write
%-12345X@PJL COMMENT MSxpsPCL6
…
out-of-bounds  …
glyph data memcpy
buffer
glyph data out-of-bounds buffer

###### Information Leak!

## Slide 39

##### Case 2

CVE-2023-23403 Microsoft PostScript and PCL6 Class Printer Driver Remote Code Execution Vulnerability

It is an out-of-bounds-write vulnerability in OpenType Parsing The CFF table contains a Compact Font Format (CFF) font representation and is structured according to Adobe Technical Note #5176: “The Compact Font Format Specification

Any check?

## Slide 40

##### Case 2

After testing, we found here had no check

MSxpsPCL6!cmnCFF::cmnCFF+0x6da: mov     qword ptr [rax+rcx*8],r9 ds:00000282`9383e000=????????????????

more 48 operators
int[48] oob-write

## Slide 41

##### Color Management

Color management is supported in v4 print drivers Common resources file is ICC Profile International Color Consortium (ICC) color profiles Provide a cross-platform device profile format

## Slide 42

##### ICC Profile in XPS format

1.fpage

<Path> <Path.Fill> <SolidColorBrush Color="ContextColor /Resources/test.icc 1.0,1.000,0.000,0.000,0.000" /> </Path.Fill> <Path.Data> <PathGeometry> <PathFigure StartPoint="10,10" IsClosed="true"> <PolyLineSegment Points="50,200 100,40 150,200 200,10 100,105" /> </PathFigure> </PathGeometry> </Path.Data> </Path>

content

render

## Slide 43

##### ICC Profile

According to Specification ICC.1:2004-10 (Profile version 4.2.0.0)

Similar as Font limited public information available Requires more time for document reading and reverse engineering

## Slide 44

##### Method to Find Vulnerability

How to find vulnerabilities without reading the document

 Fuzzing

## Slide 45

###### Choose the Suitable Fuzzing Architecture

WinAFL @ Ivan Fratric
Most Common Windows Platform Fuzzing
Our attempts have not been satisfactory
Ideal Scenario for WinAFL
Harness  LoadLibrary
traget DLL
Application call target function
The Scenario of printer drvier rendering
Harness  RPC print traget
spoolsv
Application filter driver

It’s challenging to write a harness to load print driver dirctly.

## Slide 46

###### Choose the Suitable Fuzzing Architecture

###### What the fuzz @ 0vercl0k

A distributed, code-coverage guided, customizable, cross-platform snapshot-based fuzzer designed for attacking user and / or kernel-mode targets running on Microsoft Windows

printfilterpipelinesvc
Initialize
Load driver
RPC
other parse code
Application spoolsv
snapshot  what the
parse Resource
fuzz fuzzer
other parse code
Uninitialize

## Slide 47

###### CVEs in ICC Parsing

Microsoft Printer Driver Remote Code Execution Vulnerability CVE-2023-23413 CVE-2023-23406 CVE-2023-24867 CVE-2023-24868 CVE-2023-24872 CVE-2023-24907 CVE-2023-24909 CVE-2023-24913 Microsoft Printer Driver Information Disclosure Vulnerability CVE-2023-24870

## Slide 48

Case 3
CVE-2023-24909 Microsoft PostScript and PCL6 Class Printer Driver
Remote Code Execution Vulnerability
Weakness: CWE-190: Integer Overflow or Wraparound
profileDescriptionTag
if length > len(src)
header length src buffer Out-of-bounds read
if length = 0xffffffff
malloc(length + 12 + 95) memcpy(src,dst,length)
Interger Overflow
Out-of-bounds write
dst buffer

## Slide 49

Vulnerability in XML Parsing

## Slide 50

###### What XML do in XPS?

<Path>
<Path.Fill>
<SolidColorBrush Color="#0000FF" />
 </Path.Fill>
<Path.Data>
<PathGeometry>
<PathFigure StartPoint="10,10" IsClosed="true">
<PolyLineSegment Points="50,200 100,40 150,200
200,10 100,105" />
</PathFigure>
</PathGeometry>
</Path.Data>
</Path>

###### content

1.fpage

render

## Slide 51

##### Resources vs XML

- Binary file hard to read easy to mutate

- ● Resources file possess high versatility easy to collect corpus

- Text file

easy to read hard to mutate

- XML formats are designed specifically for software

- Direct use of XPS files is not widespread.

hard to collect corpus

## Slide 52

##### How to generate XML

Read 496-page document and create

## Slide 53

##### How to generate XML

## Slide 54

##### PrintXPS – Input Generation

XSD – XML Schema Definition

Commonly used to validate XML formats.

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
PrintXPS — Input Generation
XSD - XML Schema Definition #: CrPath ;
fa AG Path
"| 6> Path.RenderTransform (0.1
g #2) 9) > Matrixtransform ae ]
A §|) {ale matrix st.Matrix
> Path.Clip (0.1 CT-CP Geometry & |
Commonly used to validate XML formats. (BAB @ Pathccometry T Pathccomety © |
> Path.OpacityMask (0.1 TOP A |
#2| | 6> ImageBrush
B) | (PAR @ opaciy
8)8 B) ffa) @ Transform
H 3 @ Viewbox
= @ Viewport
£ @ TileMode
@ ViewboxUnits
@ ViewportUnits
fla) @ ImageSource
°F) 6> ImageBrush.Transform [0.1
B) (PB) g> matrixtransform
2
a| [212 | Cliaile movie
```

## Slide 55

##### PrintXPS – Input Generation

Use xsd to generate xml
XML Font Image
Pack
from xsd to xml
xsd
XMLs
XPS

Use xsd to generate xml

## Slide 56

##### PrintXPS – Document Repair

why?

Samples generated by xsd2xml sometimes do not meet the requirements of printer drivers

XPS

XPS

printer driver

Error-log

cmnErrorLog::Add( 2i64, 1i64, 2i64, "xamlPath::ParseDashes", "%ls[%u]: Dash array must have even number of entries; cnt: %u", v15, v26, v27);

## Slide 57

##### PrintXPS – Document Repair

It can be empowered by LLM

printer driver
Error-log
XPS
repair
496-page  LLM
Documents

## Slide 58

CVEs in parsing XML page

Microsoft Printer Driver Remote Code Execution Vulnerability CVE-2023-24883 CVE-2023-24884 CVE-2023-24885 CVE-2023-24886 CVE-2023-24887 CVE-2023-24924 CVE-2023-24925 CVE-2023-24926 CVE-2023-24927 CVE-2023-24928 CVE-2023-28243

Microsoft Printer Driver Information Disclosure Vulnerability CVE-2023-32085

## Slide 59

##### Case 4

CVE-2023-24927 Microsoft PostScript and PCL6 Class Printer Driver Remote Code Execution Vulnerability

Weakness: CWE-843: Access of Resource Using Incompatible Type ('Type Confusion')

## Slide 60

Case 4
xamlSolidColorBrush::`vftable'
<Path ...>
<Path.Stroke>
<SolidColorBrush Color=...> function1
</Path.Stroke>
</Path>
function2…
+0x1c8
xamlPath::draw xamlSolidColorBrush::draw
xamlPath::`vftable'
<Path ...>
<Path.Stroke>
Deleted  function1
</Path.Stroke>
</Path>
function2…
+0x1c8
xamlPath::draw wrong function

## Slide 61

##### Next

Microsoft fixed their documents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Next
Microsoft fixed their documents
The Manifest file
se the Wind manifest file must use
DriverConfig se rs. These are the names of the filters:
osPCL6.dll. Provide: rsion from XPS to ion from XPS to
ilters, and redistribution is not support
equired of the
Inerabilities in features soft recomm
```

## Slide 62

Is that enough?

## Slide 63

Vulnerability in Third-Party Driver

## Slide 64

###### Third-Party Printer Drivers

Some manufacturers still rely on Microsoft's discontinued drivers to assist with their printing Others have adopted their own custom drivers

## Slide 65

###### Third-Party Printer Drivers

Own custom drivers

Rely on Microsoft's

...

...

## Slide 66

CVE in HP Print Driver

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
CVE in HP Print Driver
Certain HP Print Products-Potential Remote Code Execution and/or
Elevation of Privilege with the HP Smart Universal Printing Driver
Client / Server PCs with the HP Smart Universal Printing Driver installed are potentially vulnerable to Remote Code Execution and/or Elevation of Privile -
HP Smart Universal Printing Driver that sends a print job comprised of a malicious XPS file could potentially lead to Remote Code Execution and/or Elevation of Privilege on
the PC.
roll to Resolution
Severity
High
HP Reference
HPSBPIO3975 Re
Release date
October 30,2024
Last updated
October 30,2024
Category
Print
Potential Security Impact
Potential Remote Code Execution and/or Elevation of Privilege
Relevant Common Vulnerabilities and Exposures (CVE) List
Reported by Zhiniang Peng (@edwardzpeng), devoke@HUST, white
LIST OF CVE IDS
CVEID Severity Vector
High
```

## Slide 67

## The new printer

- Windows protected print mode (requires manual activation) ● Module blocking

- Per-user XPS rendering

- Lower privileges for common spooler tasks

- Binary mitigations

All print jobs will be handled by the new process, no longer running at SYSTEM

## Slide 68

Summary

## Slide 69

## Summary

Review the old Spooler bugs.

Diving into Spooler Again, find a new attack surface.

30+ CVEs in resource parsing, XML parsing and thrid-party driver.

Will the new print spooler secure in the future?

## Slide 70

## Takeaway

You can always find new attack surfaces if you dive deep enough. Spooler is a good attack surface even after years of vulnerabilities disclosure.

Disable your spooler, if you don’t need it.

## Slide 71

# Thanks!

#BHEU   @BlackHatEvents
