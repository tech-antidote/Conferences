---
title: "A Glimpse Into The Protocol Fuzz Windows RDP Client For Fun And Profit"
speakers: ["Quan Jin", "Yingqi Shi", "Mingjia Liu", "Siyuan Liu", "Guoxian Zhong"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2024"
edition: "ASIA"
year: 2024
source_pdf: "BlackHat ASIA 2024-Slides/Quan Jin & Yingqi Shi & Mingjia Liu & Siyuan Liu & Guoxian Zhong-A Glimpse Into The Protocol Fuzz Windows RDP Client For Fun And Profit.pdf"
pages: 52
sha256: "a3db466a7479bc06489ac51d10d06381c984160d241350c9c7df82bf436ff585"
text_chars: 18242
ocr_pages: 18
has_ocr: true
redacted_secrets: 0
ocr_confidence: 87.3
ocr_unreliable_blocks: 0
vision_verified_blocks: 1
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:50:39Z"
---
# A Glimpse Into The Protocol Fuzz Windows RDP Client For Fun And Profit

**Speakers:** Quan Jin, Yingqi Shi, Mingjia Liu, Siyuan Liu, Guoxian Zhong  
**Conference:** Black Hat ASIA 2024  
**Source:** `BlackHat ASIA 2024-Slides/Quan Jin & Yingqi Shi & Mingjia Liu & Siyuan Liu & Guoxian Zhong-A Glimpse Into The Protocol Fuzz Windows RDP Client For Fun And Profit.pdf` (52 pages)


## Slide 1

A Glimpse Into The Protocol Fuzz Windows RDP Client For Fun And Profit Yingqi Shi(@Mas0nShi), Mingjia Liu(@cyberestro), Quan Jin(@jq0904) DBAPPSecurity

#BHASIA @BlackHatEvents

## Slide 2

### About Us

**Yingqi Shi Mingjia Liu** @Mas0nShi @cyberestro

**Quan Jin** @jq0904

**Guoxian Zhong** @_p01arisZ

**Siyuan Liu** @4nsw3r123

# BHASIA @BlackHatEvents

## Slide 3

### Agenda

**Motivation Introduction**

**Fuzzing**

**Case Study**

**Future**

# BHASIA @BlackHatEvents

## Slide 4

# Motivation

# BHASIA @BlackHatEvents

## Slide 5

### Motivation

- Popular Remote Access Solution

- Legacy and Longevity

- And more?

https://www.shodan.io/search?query=port%3A%223389%22

# BHASIA @BlackHatEvents

## Slide 6

### Motivation

#### • Few vulnerabilities in RDP in the past year (01/2022-09/2023)

https://msrc.microsoft.com/report/vulnerability

# BHASIA @BlackHatEvents

## Slide 7

# Introduction

# BHASIA @BlackHatEvents

## Slide 8

### RDP Overview

- RDP contains the following features

   - **Clipboard**

   - **Printer**

   - **Storage Device**

   - **Smart Card**

   - **Audio IN/OUT**

- …

# BHASIA @BlackHatEvents

## Slide 9

### RDP Client Attack

• Victims connect malicious server using mstsc.exe

# BHASIA @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
RDP Client Attack
¢ Victims connect malicious server using mstsc.exe
A Remote Desktop
|
|
Malicious RDP Server
Internal Network
```

## Slide 10

### RDP Server Attack

- Attackers take control of the RDP Server using mstsc.exe

# BHASIA @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
RDP Server Attack
e Attackers take control of the RDP Server using mstsc.exe
A. Remote Desktop
Internal Network
```

## Slide 11

## Client or Server ?

# BHASIA @BlackHatEvents

## Slide 12

### Focus on Microsoft RDP Client

- Why MS RDP Client？

   - **Clarity** (mstscax.dll, etc.)

   - **Operability** (Public APIs)

   - **Simplicity** (Compared to RDP Server)

   - **Quickly** (Learn from previous works)

# BHASIA @BlackHatEvents

## Slide 13

### Previous Works

# BHASIA @BlackHatEvents


> Recovered by OCR — confidence 85/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Previous Works
EUROPE 2019
DECEMBER 2-S, 2019
Excel LONDON, UK
Fuzzing-and_Exploiting Virtual Channels Holding the Stick
Remote Desktop Protocol for Fun.and P
ue | \ a At Both Ends \THALIUM
Or Ben-Porath & Shaked Reiner
oferta Fuzzing RDPEGFX
with what the fuzz
Colas Le Guernic, Jérémy Rubert,
and Tomme of Normandy
October 15th, 2022 I-IEXACON/
```

## Slide 14

### RDP Virtual Channel

- Virtual Channel

   - **Static Virtual Channel**

   - **Dynamic Virtual Channel**

https://www.blackhat.com/eu-19/briefings/schedule/#fuzzing-and-exploiting-virtual-channels-in-microsoft-remote-desktop-protocol-for-fun-and-profit-17789

https://www.sstic.org/media/SSTIC2022/SSTIC-actes/fuzzing_microsofts_rdp_client_using_virtual_channe/SSTIC2022-Article-fuzzing_microsofts_rdp_client_using_virtual_channels-ricotta.pdf

# BHASIA @BlackHatEvents

## Slide 15

### RDP Virtual Channel

# BHASIA @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
RDP Virtual Channel
[MS-RDPEDYC] tunnels the following protocols: The following protocols are tunneled within an [MS-RDPBCGR] static virtual channel:
* XPS Printing Virtual Channel Extension [MS-RDPEXPS] * Multiparty Virtual Channel Extension [MS-RDPEMC
* Plug and Play Devices Virtual Channel Extension [MS-RDPEPNP} * Clipboard Virtual Channel Extension [MS-RDPECLIP]
* Video Virtual Channel Extension [MS-RDPEV} * Audio Output Virtual Channel Extension [MS-RDPEA]
Audio Input Virtual Channel Extension [MS-RDPEAT * Remote Programs Virtual Channel Extension [MS-RDPERP
. omposited Remoting xtension * Dynamic Channel Virtual Channel Extension [MS-RDPEDYC
« File System Virtual Channel Extension [MS-RDPEFS
= Serial Port Virtual Channel Extension [MS-RDPESP
* Input Virtual Channel Extension [MS-RDPEI
* Print Virtual Channel Extension [MS-RDPEPC
* Video Optimized Remoting Virtual Channel Extension [MS-RDPEVOR
* Smart Card Virtual Channel Extension [MS-RDPESC]
* Virtual Channel Echo Extension [MS-RDPEECO
=» Geometry Tracking Virtual Channel Protocol Extension [MS-RDPEGT
* Display Control Virtual Channel Extension [MS-RDPEDISP]
```

## Slide 16

### RDP Virtual Channel

RDPSND
TSMF

RDPDR
…

# BHASIA @BlackHatEvents

## Slide 17

### Virtual Channel API

- WTS API

   - Open Server

   - Open Virtual Channel

   - **Write / Read Virtual Channel**

   - Close Virtual Channel

   - Close Server

   - …

https://learn.microsoft.com/en-us/windows/win32/api/wtsapi32/

# BHASIA @BlackHatEvents

## Slide 18

# Fuzzing

# BHASIA @BlackHatEvents

## Slide 19

### Open Source RDP Fuzzer

#### **rdpfuzz**

- <u>https://github.com/cyberark/rdpfuzz</u>

#### **WinAFL-RDP**

- <u>https://github.com/Team-BT5/WinAFL-RDP</u>

# BHASIA @BlackHatEvents

## Slide 20

### Fuzzing Architecture #1

• Loop

https://github.com/Team-BT5/WinAFL-RDP

# BHASIA @BlackHatEvents


> Recovered by OCR — confidence 82/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Fuzzing Architecture #1
Client Host Server Host
e Loop |
afl-fuzz.exe
| winafl. dll Trigger
Execute Send Mutation
Coverage +
l mstsc.exe | onee
| |
mstscax.dll ¢ RD Services
Target Function
Start Send Normal Message
| Loop
Ly End
https://github.com/Team-BT5/WinAFL-RDP
```

## Slide 21

### Fuzzing Architecture #2

• **Proxy**

https://github.com/cyberark/rdpfuzz

# BHASIA @BlackHatEvents


> Recovered by OCR — confidence 84/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Fuzzing Architecture #2
° Proxy Client Host Server Host
afl-fuzz.exe Send Mutation
| 4
| +
winafl.d1l WTS Sender
Execute
+
| coverage | WTSVirtualChannelWrite
mstsc.exe |
|
l mstscax.dll <———Send Mutation back to Client Host , RD Services
https://github.com/cyberark/rdpfuzz
```

## Slide 22

### Choose Fuzzer

https://github.com/Team-BT5/WinAFL-RDP

# BHASIA @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Choose Fuzzer
Client Host
afl-fuzz.exe
Coverage
I
Execute
mstsc.exe
|
Target Function
Start
Send Mutation
Loop
End
Send Normal Message
Server Host
Trigger
Once
|
RD Services
https://github.com/Team-BT5/WinAFL-RDP
```

## Slide 23

### Before Fuzzing

- **Target**

- **Seeds**

Regular Expr: **.*::OnDataReceived**

# BHASIA @BlackHatEvents


> Recovered by OCR — confidence 84/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Before Fuzzing
4 Protocol Examples
¢ Target
4.1 Annotated Initialization Sequence
The following is an annotated dump of an initialization sequence using virtual channels for data
e Seeds transfer, as specified in section 1.3.2.1.
4.1.1 Server Audio Formats and Version PDU
Fal NamedPipeClientChannel:: OnDataReceived(ulong, uchar *) The following is an annotated dump of a Server Audio Formats and Version PDU.
(#] CSndInputChannelCallback :: OnDataReceived(ulong,uchar *)
[7] CTsUsbDevice :: OnDataReceived(ulong,uchar *)
(¥] CRIMObjManager :: OnDataReceived(uchar *,ulong)
|] CRIMStreamProxy :: OnDataReceived(CMemory *)
(|¥] CRIMStreamStub :: OnDataReceived(CMemory *)
7] CRdrServerRequestHandler :: OnDataReceived(ulong,uchar *)
Regular Expr: .*::OnDataReceived
```

## Slide 24

### Environment Preparation

• **2 Virtual Machines**

• **1 Virtual Machines + RDPWrap**

# BHASIA @BlackHatEvents

## Slide 25

### Environment Preparation #1

• **2 Virtual Machines**

• **1 Virtual Machines + RDPWrap**

# BHASIA @BlackHatEvents

## Slide 26

### Environment Preparation #1

• **2 Virtual Machines** • **1 Virtual Machines + RDPWrap**

# BHASIA @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Environment Preparation #1
2 Virtual Machines
1 Virtual Machines + RDPWrap
© binarymaster INI: Add support for new builds (fix #586)
Code
Blame 4998 lines (4662 loc) 124 KB
; RDP Wrapper Library configuration
; Do not modify without special knowledge
[Main]
© stascorp / rdpwrap
© 495Open vy 1,973 Closed
© 10.0.22621. 1
#2536 opened 3 day o by loyejaotdiqr47123
#2534 opened 4 days ago by loyejaotdiqr47123
© Support Windows 10.0.19041.4239 @EEDaD
#2529 opened last week by CStolle4
© 10.0.22621.3374 not * supported
#2528 opened last week by billchenbes
© windows 10 19041.4235 sea
#2524 opened 2 weeks ago by qaz1q
```

## Slide 27

### Environment Preparation #1

- **2 Virtual Machines**

- **1 Virtual Machines + RDPWrap**

# BHASIA @BlackHatEvents

## Slide 28

### Start Fuzzing

# BHASIA @BlackHatEvents


> Recovered by OCR — confidence 84/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
WinAFL 1.16b based on AFL 2.43b (mstsc.exe)
0 days, 0
0 days, 0
none seen
none seen
0 (0.00%)
0 (0.00%)
bitflip 2\1
5820/6175 (94
12.8k
202.9/sec
30/6176, 9/0,
0/0, 0/0, 0/0
0/0, 0/0, 0/0
0/0, 0/0, 0/0
0/0, 0/0, 0/0
0/0, 0/0
0.00%/372, n/a
hrs, 1 min, 20 sec
hrs, @ min, 27 sec
yet
yet
0.95% / 1.27%
2.13 bits/tuple
1 (2.94%)
7 (20.59%)
@ (@ unique)
@ (@ unique)
```

## Slide 29

### Batch Deploy

~~•~~ **~~2 Virtual Machines~~**

• **1 Virtual Machines + RDPWrap**

• **Others?**

# BHASIA @BlackHatEvents

## Slide 30

### RDS (Remote Desktop Service)

# BHASIA @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
VET FOIE WIN-OF7C
Select one or more roles to install on the selected server.
Roles Description
Remote Desktop Services enable
users to access virtual desktops
I ind Storage Services (1 of 12 installed) session-based desktops, and
ice RemoteApp programs. Use the
Hyper-V Remote Desktop Services installation
Netw ork Controller to configure a Virtual machine-
Network Policy and Access Services (Installed) based or a Session-based deskt
Print and Document Services deployment
Remote
Remote Desktop Gatew
Remote Desktop Licensing (Installed)
n Host (Installed)
rtualiz
Remote Desktop
Remote Desktop
lume Activation Services
b Server (IIS)
Deployment Services
Web Access
Cancel
```

## Slide 31

### Start Fuzzing

# BHASIA @BlackHatEvents

## Slide 32

### Guideboard: An Old Unfixed OOBR

**Same bug with:** https://blog.thalium.re/posts/fuzzing-microsoft-rdp-client-using-virtual-channels/#out-of-bounds-read-in-rdpsnd

# BHASIA @BlackHatEvents

## Slide 33

### Enhancing Fuzzing

- **WinAFL**

   - Transplant the mutation strategy of honggfuzz

   - Coverage visualization & statistics

   - Fuzzer arch **#1** to **#2** ( **Loop** -> **Proxy** )

- **Reversing**

- **RTFM**

# BHASIA @BlackHatEvents

## Slide 34

### Dream Start: A New NPD (Won’t Fix)

# BHASIA @BlackHatEvents


> Recovered by OCR — confidence 82/100 on the text kept, 61/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
2
*(_DWOF
= 32
}
else
{
= Ug
}
CRIMObjManz
Break Go
Home View Breakpoints Time Travel Model Scripting Source Memory Command
{} Step Out {'} Step Out Bac © Restart =) | lel E) @ Fy
{*} Step Into {*} Step Into Back _ @ Stop Debugging — |=
Go Settings |Source| Assembly Local Feedback
(18c8.23f@): Access violation - code ceeeeees (first chance)
First chance exceptions are reported before any exception handling.
This exception may be expected and handled.
mstscax! CRIMObjManager: : ExchangeCapabilities+@xcs:
eeee7ffb cfc31485 efba6s5cle bts dword ptr [rax+5Ch],1Eh ds:@eeeeeee eeGeReSc=????????
# Child-sP RetAddr Call Site
4
T Entry
```

## Slide 35

### Check & Doubt

# BHASIA @BlackHatEvents

## Slide 36

### Eureka: Race Condition

https://i.blackhat.com/BH-US-23/Presentations/US-23-YukiChen-Diving-into-Windows-Remote-Access.pdf

# BHASIA @BlackHatEvents

## Slide 37

### New Fuzzer

• Developed a simple Fuzzer

# BHASIA @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
New Fuzzer
¢ Developed a simple Fuzzer
A Simple Fuzzer for Quick Proofing
e Developed a simple fuzzer:
1. Create a connection to server
2. Create some calls for this connection
3. Create some threads which randomly perform below actions:
2.1 Send call related messages to the server (create/destroy/setting)
2.2 Send control related messages to the server (create/destroy)
2.3 Close the connection
GREAT TRUTHS.
ARE ALL SIMPLE
i
&
```

## Slide 38

### New World

• Got a few crashes in days • Manual auditing

# BHASIA @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 88/100 on the text kept, 66/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
New World

• Got a few crashes in days
• Manual auditing

ModLoad: 00007ffb`fbb80000 00007ffb`fbba8000    C:\WINDOWS\SYSTEM32\edputil.dll
(1d70.ff0): Access violation - code c0000005 (first chance)
First chance exceptions are reported before any exception handling.
This exception may be expected and handled.
WebAuthn!I_ProcessRemoteRpcRequestOnClient+0x132:
00007ffb`ff7045e2 488902          mov     qword ptr [rdx],rax ds:00000000`00000000=????????????????
0:019> k
 # Child-SP          RetAddr           Call Site
00 000000ae`802ff8f0 00007ffb`ff7194e1 WebAuthn!I_ProcessRemoteRpcRequestOnClient+0x132
01 000000ae`802ff970 00007ffb`c05893a2 WebAuthn!WebAuthNDVCCallback::OnDataReceived+0xf1
02 000000ae`802ffa40 00007ffb`c055667c mstscax!CDynVCChannel::HandleAsyncCall+0xc2
03 000000ae`802ffaa0 00007ffb`c05882c3 mstscax!CDynVCThreadPoolThread::ThreadPoolEntry+0xd8
04 000000ae`802ffb20 00007ffb`c05f6fc1 mstscax!CTSThread::TSStaticThreadEntry+0x2a3
05 000000ae`802ffb80 00007ffc`0c951fe7 mstscax!PAL_System_Win32_ThreadProcWrapper+0x31

(7b30.6670): Unknown exception - code 000006ef (first chance)
(7b30.8018): Unknown exception - code 000006ef (first chance)
(7b30.35334): Access violation - code c0000005 (first chance)
First chance exceptions are reported before any exception handling.
This exception may be expected and handled.
msvcrt!memcpy+0x17:
00007ffb`2cc99597 4c8919          mov     qword ptr [rcx],r11 ds:00000229`0f2dffee=????????????????
0:060> k
 # Child-SP          RetAddr           Call Site
00 000000ad`318ff6a8 00007ffb`0f21f21d msvcrt!memcpy+0x17
01 000000ad`318ff6b0 00007ffb`0f231b99 WINSPOOL!PrivateWritePrinter+0x435

First chance exceptions are reported before any exception handling.
This exception may be expected and handled.
xpsprint!Ordinal2+0x3d2:
00007ffc`3a049752 48832000          and     qword ptr [rax],0 ds:000001e3`8811cd98=????????????????
0:075> k
 # Child-SP          RetAddr           Call Site
00 00000006`4317f620 00007ffc`3a04ac63 xpsprint!Ordinal2+0x3d2
01 00000006`4317f710 00007ffc`10e29a9e xpsprint!StartXpsPrintJob+0x193

[photo of a woman on a talk-show stage in a red dress, arms raised, holding a microphone]
```

## Slide 39

# Case Study

# BHASIA @BlackHatEvents

## Slide 40

### Case 01 - Normal Printer UAF

0:060> k # Child-SP          RetAddr Call Site 00 000000ad`318ff6a8 00007ffb`0f21f21d     msvcrt!memcpy+0x17 01 000000ad`318ff6b0 00007ffb`0f231b99     WINSPOOL!PrivateWritePrinter+0x435 02 000000ad`318ffbe0 00007ffa`4c1c8c40     WINSPOOL!WritePrinter+0x9 03 000000ad`318ffc20 00007ffa`4c1c1fea mstscax!W32DrAutoPrn::AsyncWriteIOFunc +0x3d0

……

WINSPOOL!Ordinal361+0x182: 00007ffc`5080a942 83bfb000000002  cmp dword ptr [rdi+0B0h],2 ds:0000024d`1e422fa0=???????? 0:029> k

# Child-SP          RetAddr Call Site 00 00000063`ea1ffa70 00007ffc`507fe72b     WINSPOOL!Ordinal361+0x182 01 00000063`ea1ffab0 00007ffc`5080d6e4     WINSPOOL!StartDocDlgW+0x67b 02 00000063`ea1ffdb0 00007ffc`10d89770     WINSPOOL!StartDocPrinterW+0xe4 03 00000063`ea1ffe00 00007ffc`10d82cea mstscax!W32DrAutoPrn::AsyncWriteIOFunc +0x200

# BHASIA @BlackHatEvents

## Slide 41

### Case 01 - Normal Printer UAF

**Thread 1 – Worker thread Thread 2 – Close Printer Thread** W32DrAutoPrn::AsyncWriteIOFunc W32DrAutoPrn::ClosePrinter { { // ... // ... if (bUseXpsMode) CALL W32DrAutoPrn::StartXPSJob; if (bUseXpsMode) CALL W32DrAutoPrn::CloseXPSJob; CALL OpenPrinterW; **// 1. Get the printer handle** CALL EndPagePrinter; // ... Race window ... CALL EndDocPrinter; CALL WritePrinter; **// 3. Use the printer handle** CALL ClosePrinter; **// 2. Free the printer handle** // ... // ... } }

# BHASIA @BlackHatEvents

## Slide 42

### Case 02 - XPS Printer UAF

- Are there any other points?

- • **CreateThread()** function

- Free and Use

# BHASIA @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Case 02 - XPS Printer UAF
¢ Are there any other points?
¢ CreateThread() function
¢ Free and Use
USA 2@0e5
Case Study - Call
Thread 1 — Client sends Call-Disconnect-
Notify request with a Callld
CtlpEngine
{
For each Call in Control. CallList:
if Call.id == Callld:
break
// No Lock, no reference counter
CallEventCallDisconnectNotify(Call)
}
Use After Free
Thread 2 - Client close the same connection
CtlpCleanup
{
For each Call in Control. CallList:
// Free the call, no lock
CallCleanup(Call)
Race Window
```

## Slide 43

### Case 02 - XPS Printer UAF

- Variant analysis

- Targeted test

# BHASIA @BlackHatEvents


> Recovered by OCR — confidence 80/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Case 02 - XPS Printer UAF
¢ Variant analysis
¢ Targeted test
if ( printerRef )
(*(*printerRef + 64164))(printerRef, 548164, this + 1804, @i164);// CTSCoreEventSource: :FireSyncNotification
paramPtr = (this + 648);
{
if ( W32DrAutoPrn: :StartXPSJob(this) )
{
errorCode = 1630;
goto LABEL_66;
}
goto LABEL_38;
}
printerRefPtr = (this + 1224);
if ( W32DrAutoPrn: :W32DrOpenPrinter( this + 44, this + 153) )
: printerHandlePtr = *printerRefPtr; :
tempVar2 = 0164; F | CXPSPrintJob2::CanPrintXPS (int *) . text
*documentInfo = this + 1260; F| CXPSPrint Job2: :CheckXPSPrint ingProgressThreadPro-* . text
if ( IsXPSDriver(printerHandlePtr) == 1) |] CxPSPrintJob2: :Close (ulong) . text
t docType = L"XPS_PASS"; Fi CXPSPrintJob2::CreateInstance(ushort const *,CXP*: .text
} a - ? F|CXPSPrintJob2::Initialize(ushort const *) . text
else # [CXPSPrint Job2: :Open(ushort const *, ulong, ulong, [°--] . text
Fa CXPSPrintJob2: : Terminate (void) . text
ra CXPSPrintJob2::Write(uchar *, ulong) . text
Fa CXPSPrint Job2: :XPSDataStreamIsOpen (void) . text
```

## Slide 44

### Case 02 - XPS Printer UAF

# BHASIA @BlackHatEvents


> Recovered by OCR — confidence 85/100 on the text kept, 57/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Case O02 - XPS Printer UAF
T zz
{} Step Over Back Back & Detach Help ~
Flow Contro Reverse Flow Contro End Preferences Help
First chance exceptions are reported before any exception handling.
This exception may be expected and handled.
+ {}* Step Over
* 7
7 89808806 4317F9a8
Locals
Name
# Child-SP RetAddr Call Site
mstscax!CXPSPrintJob2: :Open+@xi2e
mstscax! ThreadPool: :HandlePendingRequest+0x72
mstscax! ThreadPool: :PooledThread+@x11le
Value Name
Value
```

## Slide 45

}

### Case 02 - XPS Printer UAF

**Thread 1 – Send Creat PDU To Load xpsprint.dll**

**Thread 2 – Send Close PDU To Free xpsprint.dll**

W32DrAutoPrn::StartXPSJob()

{

CXPSPrintJob2::Initialize

{

**// Load xpsprint.dll**

library = LoadLibraryExW(L"xpsprint.dll",0,0x800u);

}

CXPSPrintJob2::Close()

{

if ( !CXPSPrintJob2::XPSDataStreamIsOpen(this) ) {

return 0x8007139;

}

CXPSPrintJob2::~CXPSPrintJob2

- {

CXPSPrintJob2::Open(pXPSJob)

{

if (CXPSPrintJob2::XPSDataStreamIsOpen(this) )

{

return 0x8007139;

}

}

CXPSPrintJob2::Terminate(pXPSJob)

{

**// Unload xpsprint.dll !**

FreeLibrary(xpsprint.dll) ;

}

}

// ... Race window ...

**// Use some pointer in xpsprint.dll and crash !**

TempFile = StartXpsPrintJob();

}

# BHASIA @BlackHatEvents

## Slide 46

### Patches

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-21307

# BHASIA @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Patches
Remote Desktop Client Remote Code Execution Vulnerability
CVE-2024-21307
Security Vulnerability
Released: Jan 9, 2024
Last updated: Feb 23, 2024
Assigning CNA: Microsoft
CVE-2024-21307 ©
Impact: Remote Code Execution Max Severity: Important
Weakness: CWE-416: Use After Free
Vector String Source: Microsoft
CVSS:3.17.5/6.5 ©
https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-21307
```

## Slide 47

### Patches

**Patches – CVE-2024-21307 #1 Patches – CVE-2024-21307 #2** W32DrAutoPrn::StartXPSJob W32DrAutoPrn::CloseXPSJob { { **+CALL EnterCriticalSection;** // ... // ... **+CALL EnterCriticalSection;** CALL Create_CXPSPrintJob(&_ptrXPSJob, ...); // ... CALL _ptrXPSJob->Open(_ptrXPSJob, ...); **+CALL LeaveCriticalSection;** // ... // ... **+CALL LeaveCriticalSection;** } }

# BHASIA @BlackHatEvents

## Slide 48

# Future

# BHASIA @BlackHatEvents

## Slide 49

### Future Work

RDP Server
More Protocols

More Channels
…

# BHASIA @BlackHatEvents

## Slide 50

### Black Hat Sound Bytes

- We have shared some skills on fuzzing Windows RDP components

- We have shared our latest research on Windows RDP Client vulnerability

- We have showed the significance of race condition in vulnerability discovery

# BHASIA @BlackHatEvents

## Slide 51

# Thanks!

# BHASIA @BlackHatEvents

## Slide 52

### References

1. <u>https://github.com/cyberark/RDPFuzz</u>

2. <u>https://github.com/Team-BT5/WinAFL-RDP</u>

3. <u>https://blog.thalium.re/posts/misc/rdpegfx/Hexacon2022-Fuzzing_RDPEGFX_with_wtf.pdf</u>

4. <u>https://i.blackhat.com/BH-US-23/Presentations/US-23-YukiChen-Diving-into-Windows-Remote-Access.pdf</u>

5. <u>https://i.blackhat.com/eu-19/Wednesday/eu-19-Park-Fuzzing-And-Exploiting-Virtual-Channels-In-Microsoft-RemoteDesktop-Protocol-For-Fun-And-Profit-4.pdf</u>

6. <u>https://www.sstic.org/media/SSTIC2022/SSTIC-actes/fuzzing_microsofts_rdp_client_using_virtual_channe/SSTIC2022Article-fuzzing_microsofts_rdp_client_using_virtual_channels-ricotta.pdf</u>

7. <u>https://conference.hitb.org/hitbsecconf2021sin/materials/D2T1%20-</u>

<u>%20Holding%20The%20Stick%20at%20Both%20Ends%20-%20Fuzzing%20RDP%20Client%20and%20Server%20%20Shaked%20Reiner%20&%20Or%20Ben-Porath.pdf</u>

# BHASIA @BlackHatEvents
