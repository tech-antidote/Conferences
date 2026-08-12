---
title: "LogoFAIL Security Implications of Image Parsing During System Boot"
speakers: ["Fabio Pagani", "Alex Matrosov", "Alex Ermolov", "Yegor Vasilenko", "Sam Thomas", "Anton Ivanov"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2023"
edition: "Europe"
year: 2023
source_pdf: "Black Hat Europe 2023 slides/Fabio Pagani, Alex Matrosov, Alex Ermolov , Yegor Vasilenko , Sam Thomas , Anton Ivanov _ LogoFAIL Security Implications of Image Parsing During System Boot.pdf"
pages: 53
sha256: "c2ee5f64eb7f9c6180a2eb1e4bcd8eb4fcc871aac7dda69dd341263307f16c26"
text_chars: 16904
ocr_pages: 11
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:12:01Z"
---
# LogoFAIL Security Implications of Image Parsing During System Boot

**Speakers:** Fabio Pagani, Alex Matrosov, Alex Ermolov, Yegor Vasilenko, Sam Thomas, Anton Ivanov  
**Conference:** Black Hat Europe 2023  
**Source:** `Black Hat Europe 2023 slides/Fabio Pagani, Alex Matrosov, Alex Ermolov , Yegor Vasilenko , Sam Thomas , Anton Ivanov _ LogoFAIL Security Implications of Image Parsing During System Boot.pdf` (53 pages)

## Slide 1

**Logo** **_FAIL_** Security implications of image parsing during system boot

Fabio Pagani Alex Matrosov Yegor Vasilenko

Alex Ermolov Sam Thomas Anton Ivanov

## Slide 2

## **$ whoami**

### **Research Scientist @ Binarly**

RR

##### **Fabio Pagani**

- @pagabuc

- Vulnerability and Threat Research

- ◆ Program  analysis

   - Fuzzing, Dynamic analysis

### **Academic background**

- PostDoc @ UCSB SecLab

- ◆ Looked at binary code from different angles (binary similarity, fuzzing, forensics)

**© BINARLY.IO**

## Slide 3

## **Binarly REsearch Team**

**Alex Matrosov** @matrosov

###### **Fabio Pagani**

@pagabuc

**Sam Thomas** @xorpse

**Alex Ermolov** @flothrone

**Yegor Vasilenko** @yeggorv

**Anton Ivanov** @ant_av7

### Logo _FAIL_ [edition]

## Slide 4

## **Scan**

**The Far-Reaching Inside the LogoFAIL Consequences of Vulnerabilities LogoFAIL** (Blog) (Video)

**© BINARLY.IO**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
© BINARLY.IO
Ble ici ole
The Far-Reaching
Consequences of
LogoFAIL (Blog)
Inside the LogoFAIL
Vulnerabilities
(Wife [=te))
Binarly
```

## Slide 5

## **Data-Only Attacks Against UEFI Firmware** 🔥

- **Insecure handling of content from R/W areas (NVRAM)**

- **Allow bypassing Secure Boot and hardware-based Verified Boot:**

   - Intel Boot Guard

   - AMD Hardware-Validated Boot

   - ARM TrustZone-based verification

- **Lead to compromise of other protections in Pre-EFI like Intel PPAM**

Breaking Firmware Trust From Pre-EFI: Exploiting Early Boot Phases

<u>https://i.blackhat.com/USA-22/Wednesday/US-22-Matrosov</u> -Breaking-Firmware-Trust-From-Pre-EFI.pdf

**© BINARLY.IO**

## Slide 6

## **Exploring new Attack Surfaces** 🔬

**While looking at vulnerabilities discovered by our platform, we observed that image parsers in firmware are actually quite common.**

**But why do we even need image parsers during boot?!**

**© BINARLY.IO**

## Slide 7

## **History Repeats Itself**

Attacking Intel BIOS at BlackHat USA 2009 by Rafal Wojtczuk and Alexander Tereshkin https://www.blackhat.com/presentations/bh-usa-09/WOJTCZUK/BHUSA09-Wojtczuk-AtkIntelBios-SLIDES.pdf

**© BINARLY.IO**

## Slide 8

## **History Repeats Itself (~15 years later)**

- **Different image parsers available in UEFI firmware**

   - **BMP, GIF, PNG,  JPEG, PCX, and TGA**

- **User can pass image data to them**

   - **Various logo customization features are available**

- **Image parsing is done during boot**

   - **DXE phase**

   - **C-written code (3rd party)**

   - **No mitigations for exploitation of software vulnerabilities**

**What could go wrong?!**

**© BINARLY.IO**

## Slide 9

## **Meet Logo** **_FAIL_**

- **New set of security vulnerabilities affecting image parsing libraries used during the device boot process**

- **LogoFAIL is cross-silicon and impacts x86 and ARM-based devices**

- **LogoFAIL is UEFI and IBV-specific**

- **Impacts the entire ecosystem across this reference code and device vendors**

**© BINARLY.IO**

## Slide 10

## **Meet Logo** **_FAIL_**

- **New set of security vulnerabilities affecting image parsing libraries used during the device boot process**

- **LogoFAIL is cross-silicon and impacts x86 and ARM-based devices**

- **LogoFAIL is UEFI and IBV-specific**

- **Impacts the entire ecosystem across this reference code and device vendors**

**150+ days of embargo lifts TODAY**

**© BINARLY.IO**

## Slide 11

💣

## **Implications of LogoFAIL**

|**Attack Vector**|**Vulnerability ID**|**Exploited**
**in-the-wild**|**Impact**|**CVSS Score**|**CWE**|
|---|---|---|---|---|---|
||**VU#811862**
**CVE-2023−40238**
**CVE-2023−5058**
**CVE-2023−39539**
**CVE-2023−39538**
**and more …**|**Unknown**|**HW-based Verified**
**Boot and Secure**
**Boot Bypass**
**x86 and ARM**|**8.2 High**
**6.7Medium**|**CWE-122:**
**Heap-based Buffer**
**Overflow**
**CWE-125:**
**Out-of-bounds Read**|
|Baton Drop|CVE-2022−21894
CVE-2023−24932||Secure Boot Bypass
x86|6.7
Medium|CWE-358: Improperly
Implemented Security
Check for Standard|
|3rd-party
Bootloaders|VU#309662|Unknown|Secure Boot Bypass
x86|6.7
Medium|CWE-358: Improperly
Implemented Security
Check for Standard|
|BootHole|VU#174059|Unknown|Secure Boot Bypass
x86|8.2 High|CWE-120: Buffer Copy
without Checking Size
of Input|

**© BINARLY.IO**

## Slide 12

# **Attack Surface**

Image
Parser
Attack Surface

**© BINARLY.IO**

## Slide 13

## **Different Shades of  UEFI Image Parsers** 🔬

**© BINARLY.IO**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Different Shades of UEFI Image Parsers
BmpDecoderDxe-A9F634A5 -29F1-4456 -A9D5-6E24B88BDB65
TgaDecoderDxe - ADCCA887 - 5330-414A-81A1-5B578146A397
PngDecoderDxe -C1D5258B-F61A-4C02-9293-AQO5BEB3EAA1
JpegDecoderDxe -2707E46D-DBD7 -41C2-9C04-C9FDB8BAD86C
PcxDecoderDxe -A8F634A5 -28F1-4456-A9D5-7E24B99BDB65
GifDecoderDxe- 1353DE63 -B74A- 4BEF - 80FD-2C5CFA83040B
SystemImageDecoderDxe- 5F65D21A- 8867 -45D3 -A41A-526F9FE2C598
AMITSE-B1DAOADF - 4F77 -4070-A88E-BFFE1C60529A
MdeModulePkg/Library/BaseBmpSupportLib/BmpSupportLib.c
© BINARLY.IO
6insyde
phoenix
technologies
Binarly
```

## Slide 14

## **Identifying the Attack Surface**

- All the channels used by firmware to read a logo image

- **●** A lot of reversing with efiXplorer

- ● Start from image parsers, then looks “backwards”

<u>https://github.com/binarly-io/efiXplorer</u>

**© BINARLY.IO**

## Slide 15

## **Attack Surface**

###### **Several OEM-specific customizations:**

1. Logo is read from a fixed location (e.g., “\EFI\OEM\Logo.jpg”)

2. Logo is stored into an unsigned volume of a firmware update

3. An NVRAM variable contains the path of the logo

4. An NVRAM variable contains the logo itself

<u>https://binarly.io/advisories/BRLY-2023-006 https://binarly.io/advisories/BRLY-2023-018</u>

**© BINARLY.IO**

## Slide 16

# **Fuzzing**

**© BINARLY.IO**

## Slide 17

## **Fuzzing UEFI Image Parsers**

- UEFI DXE modules are normal PE files

- The UEFI runtime environment needed to re-hosted

- Fuzzer based on newly-developed emulation capabilities which we integrated with LibAFL

**© BINARLY.IO**

## Slide 18

## **Fuzzing Harness**

**A bridge between the fuzzer and the fuzzed module:**

- Module initialization (protocols are installed)

- Prepare call to parsing function

- Forwards fuzzer-generated data to the target module

**We are ready to fuzz!**

**© BINARLY.IO**

## Slide 19

## **Root Causes**

- We found hundreds of crashes

- Extended Binarly's internal program analysis framework to support us in this task

**© BINARLY.IO**

## Slide 20

## **Root Causes (** **_Excerpt_ ) We found 29 unique root causes, 15 of which are likely exploitable**

|**BRLY ID**|**CERT/CC ID**|**Affected**
**IBV**|**Image**
**Library**|**Impact**|**CVSS**
**Score**|**CWE**|
|---|---|---|---|---|---|---|
|BRLY-LOGOFAIL-2023-001|VU#811862|Insyde|BMP|DXE Memory
Content
Disclosure|Medium|CWE-200: Exposure of Sensitive
Information|
|BRLY-LOGOFAIL-2023-007|VU#811862|Insyde|GIF|DXE Memory
Corruption|High|CWE-122: Heap-based Buffer Overflow|
|BRLY-LOGOFAIL-2023-016|VU#811862|AMI|PNG|DXE Memory
Corruption|High|CWE-122: Heap-based Buffer Overflow
CWE-190: Integer Overflow|
|BRLY-LOGOFAIL-2023-022|VU#811862|AMI|JPEG|DXE Memory
Corruption|High|CWE-787: Out-of-bounds Write|
|BRLY-LOGOFAIL-2023-025|VU#811862|Phoenix|BMP|DXE Memory
Corruption|High|CWE-122: Heap-based Buffer Overflow|
|BRLY-LOGOFAIL-2023-029|VU#811862|Phoenix|GIF|DXE Memory
Corruption|High|CWE-125: Out-of-bounds Read|

**© BINARLY.IO**

## Slide 21

## **BRLY-LOGOFAIL-2023−006: Memory Corruption**

- PixelHeight and PixelWidth are attacker controlled

- When PixelHeight and i are 0: BltBuffer[PixelWidth * -1]

- Arbitrary write anywhere below BltBuffer

BMP parser developed by Insyde

**© BINARLY.IO**

## Slide 22

## **BRLY-LOGOFAIL-2023−022: Memory Corruption**

- Assumption that JPEG can contain only 4 Huffman Tables

- NumberOfHTs variable is unchecked

- Overflow on global data with pointers to our image

JPEG parser developed by AMI

**© BINARLY.IO**

## Slide 23

## **Takeaways from Fuzzing**

**None of these libraries where ever fuzzed by IBVs/OEMs:**

- We found crashes in every parser

- First crashes where found after seconds of fuzzing

- Some parsers even crash with images downloaded from the Internet :-)

**© BINARLY.IO**

## Slide 24

## **Thanks to the Internet Archive!**

- One of the parsers is for PCX images

- Finding good corpus for the fuzzer turned out to be more difficult than expected

- ● Until..

https://archive.org/details/Universe_Of_PCX_1700_PCX_Files

**© BINARLY.IO**

## Slide 25

## **Proof of concept**

**© BINARLY.IO**

## Slide 26

## **Let’s PWN a Real Device**

**● Lenovo ThinkCentre M70s Gen 2**

**● 11**<sup>**th**</sup> **Gen Intel Core (Tiger Lake)**

- **BIOS released on June 2023**

**© BINARLY.IO**

## Slide 27

## **Selecting a Target**

Simple format  + exploitable crash: PNG parser from AMI

**© BINARLY.IO**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Selecting a Target
PNG Image
Compressed
. —__ E OutputBuffer
PNG Magic \x89PNG\r\n\x1a\n IDAT chunks
IHDR Chunk IHDR\x00\x00\x000\x00\x00
\x00\x08\x06\x00\x00...
nd
IDAT Chunk IDATh\xde\xed\x9a{\xd4_Uy
\xe7\xcf\xdeg\x9f\xcb...
IDATx\xda\xec\xc1\x01\x01
\x00\x00\x00\x80\x90...
IDAT Chunk
Simple format + exploitable crash: PNG parser from AMI
© BINARLY.1O Binarly
```

## Slide 28

## **Selecting a Target**

Simple format  + exploitable crash: PNG parser from AMI

**© BINARLY.IO**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Selecting a Target
PNG Image
Compressed
PNG Magic \x89PNG\r\n\x1a\n IDAT chunks Tey REN
IHDR Chunk THDR\x00\x00\x000\x00\x00
\x00\x08\x06\x00\x00...
h\xde\xed\x9a{\xd4_Uy\x
e7\xcf\xdeg\x9F\xcb\xef
IDAT Chunk IDATh\xde\xed\x9a{\xd4_Uy \xfe\xde\x92\xbce\xb9x\x
\xe7\xcf\xdeg\x9f\xcb...
da\xec\xc1\x01\x01\x00\
x00\x00\x80\x90\xfe\xaf
\xee\x08\x02\x00\x00
IDATx\xda\xe
IDAT Chunk \x00\x00\x00\>
Simple format + exploitable crash: PNG parser from AMI
© BINARLY.1O Binarly
```

## Slide 29

## **Selecting a Target**

Simple format  + exploitable crash: PNG parser from AMI

**© BINARLY.IO**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Selecting a Target
PNG Image
Compressed
PNG Magic \x89PNG\r\n\x1a\n IDAT chunks Tey REN
IHDR Chunk THDR\x00\x00\x006\x00\x00
\x00\x08\x06\x00\x00... INEM RENCE DAR:
e7\xcf\xdeg\x9f\xcb\xef
ae
IDAT Chunk IDATh\xde\xed\x9a{\xd4_Uy \xfe\xde\x92\xbco\xb9x\x
\xe7\xcf\xdeg\x9f\xcb...
da\xec\xc1\x01\x01\x00\
x00\x00\x80\x90\xfe\xaf
\xee\x08\x02\x00\x00...
IDATx\xda\xec\xc1\x01\x01
\x00\x00\x00\x80\x90...
IDAT Chunk
Simple format + exploitable crash: PNG parser from AMI
© BINARLY.1O Binarly
```

## Slide 30

## **Integer Overflow to Heap Overflow**

**Integer overflow on 32 bit value used as allocation size:**

● 2 * 0x20       = 0x40 ● 2 * 0x60       = 0xc0 ● 2 * 0x80000040 = 0x80

**© BINARLY.IO**

## Slide 31

## **Integer Overflow to Heap Overflow**

**Integer overflow on 32 bit value used as allocation size:**

● 2 * 0x20       = 0x40 ● 2 * 0x60       = 0xc0 ● 2 * 0x80000040 = 0x80

**© BINARLY.IO**

## Slide 32

## **Wait a Minute..**

- How does heap exploitation even work for UEFI?

- ● No debugging capabilities:

   - Intel DCI doesn’t work on new CPU models

   - ○ Intel Boot Guard prevents replacing modules

- Not even output on crash :(

**© BINARLY.IO**

## Slide 33

## **UEFI Heap Internals**

### ● Pool-based heap

**© BINARLY.IO**

## Slide 34

## **UEFI Heap Internals**

● Pool-based heap

#### **VOID *p = AllocatePool(0x40)**

**© BINARLY.IO**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
UEFI Heap Internals
e Pool-based heap VOID xp = AllLocatePool(0x40)
mPoolHead
(E£iBoot
Services POOL_HEAD
Data) ~
[ Size 0x80 he POOL_FREE a POOL_FREE KY POOL_FREE }
[ su (o 100 tf POOL_FREE Wy POOL_FREE Wy POOL_FREE ] DATA
[ sux o 100 ff POOL_FREE ian POOL_FREE lanl POOL_FREE }
[size onan tf POOL_FREE ] ( POOL_FREE iat POOL_FREE ]
fe ox7as] ( POOL_FREE im POOL_FREE Hf POOL_FREE }
© BINARLY.1O Binarly
```

## Slide 35

## **UEFI Heap Internals**

### ● Pool-based heap

**FreePool(p)**

**© BINARLY.IO**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
UEFI Heap Internals
e Pool-based heap
(E£iBoot
Services POOL_HEAD
Data) —
[ Size 0x80 he POOL_FREE a POOL_FREE jf POOL_FREE }
[ su o 100 tf POOL_FREE Wy POOL_FREE Wy POOL_FREE ] DATA
[ sux ® 100 ff POOL_FREE ian POOL_FREE lanl POOL_FREE ]
( WH } f } f }  POOL_TAIL | TAIL
Size 0x280 POOL_FREE POOL_FREE POOL_FREE ~
fe ox7as] [ POOL_FREE Hf POOL_FREE Hf Poo._FRE | F ree Poo 1 ( p )
© BINARLY.1O Binarly
```

## Slide 36

## **What Are We Even Corrupting?**

**We don’t know!!**

**© BINARLY.IO**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
What Are We Even Corrupting?
OutputBuffer Allocated Chunk
POOL_HEAD |BRLYBRLYBRLYBRLYBRLYBRLY| POOL_TAIL | POOL_HEAD}| OBJ DATA | POOL_TAIL
>
OutputBuffer Free Chunk
POOL_HEAD | BRLYBRLYBRLYBRLYBRLYBRLY | POOL_TAIL POOL_FREE ]
We don’t know!!
© BINARLY.1O Binarly
```

## Slide 37

## **Long Live UEFI Memory**

- Memory used by UEFI is not cleared

- If the OS doesn’t overwrite it, we can dump it after boot

- **●** OutputBuffer is not freed, so it’s somewhere in memory!

**© BINARLY.IO**

## Slide 38

## **Long Live UEFI Memory**

- Memory used by UEFI is not cleared

- If the OS doesn’t overwrite it, we can dump it after boot

- **●** OutputBuffer is not freed, so it’s somewhere in memory!

**This is NOT the object we can corrupt!**

**© BINARLY.IO**

## Slide 39

## **Preserving Heap Chunks**

- New technique to preserve chunks

- ● Corrupting the signature ensures a chunk is not reused

**© BINARLY.IO**

## Slide 40

## **Preserving Heap Chunks**

**This IS the object we can corrupt!!**

**© BINARLY.IO**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Preserving Heap Chunks
© BINARLY.IO
82c83f10:
82c83f20:
82c83f30:
82c83f40:
82c83f50:
82c83f60:
82c83f70:
82c83f80:
82c83f90:
82c83fa0:
82c83fb0:
82c83fc0:
4252 4c59 4252
4252 4c59 4252
4252 4c59 4252
4252 4c59 4252
4252 4c59 4252
4252 4c59 4252
4c59
4c59
4c59
4c59
4c59
4c59
4252 4c59 4252 4c59
4252 4c59 4252 4c59
4252 4c59 4252 4c59
4252 4c59 4252 4c59
4252 4c59 4252 4c59
4f4f 4f4f 4f4f 4f4f
This IS the object we can
corrupt!!
<>
oe
4
BRLYBRLYBRLYBRLY
BRLYBRLYBRLYBRLY
BRLYBRLYBRLYBRLY
BRLYBRLYBRLYBRLY
BRLYBRLYBRLYBRLY
BRLYBR 0000
OOO00COOXhdg....
Binarly
```

## Slide 41

## **Little Recap**

What we achieved so far:

- We have arbitrary overflow on the heap

- ● We can prevent the next chunk from being freed

- ● We can inspect the object stored in the next chunk

What’s left?

- Finding a good target for corruption

- ● Get code execution out of it

**© BINARLY.IO**

## Slide 42

## **Enter the UEFI Heap Feng Shui**

- Heap exploitation often requires strong allocation and deallocation primitives

- ● We can influence the heap by adding PNG chunks or changing their sizes

**© BINARLY.IO**

## Slide 43

## **Enter the UEFI Heap Feng Shui**

● Heap exploitation often requires strong allocation and deallocation primitives ● We can influence the heap by adding PNG chunks or changing their sizes

**© BINARLY.IO**

## Slide 44

## **PROTOCOL_ENTRY, tell me more..**

- Protocols are a core concept in UEFI

**●** PROTOCOL_ENTRY has multiple pointers to objects with function pointers

**© BINARLY.IO**

## Slide 45

## **UEFI Event System**

● Events are generated when protocols are installed

**© BINARLY.IO**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
UEFI Event System
e Events are generated when protocols are installed
Moto or PROTOCOL_ENTRY PROTOCOL_ENTRY |x—>....
Database
PROTOCOL_NOTIFY
IEVENT
Callback
Handler
Function
©BINARLY.IO Binarly
```

## Slide 46

## **Arbitrary Code Exec in UEFI**

- Memory region where NVRAM variables is often executable and always mapped at the same fixed address

- We can just store a shellcode there

- ● Our shellcode can: ○ Disable Secure Boot (zero a global variable)

- ○ Start a second-stage payload from disk: ■ Unload current NTFS driver (no write support)

- ■ Load new NTFS driver (with write support)

- ■ Creates a  file on the Windows filesystem

**© BINARLY.IO**

## Slide 47

## **Putting it All Together**

- Preparation:

   1. Malicious PNG on the ESP (or in NVRAM)

   **2.** PROTOCOL_NOTIFY, IEVENT and Shellcode in NVRAM

   **3.** Second-stage payload on disk: \Users\user\LogoFAIL\SecondStageWin.efi

- Reboot the system

- UEFI firmware will parse our PNG

- Heap overflow corrupts a PROTOCOL_ENTRY with pointers to PROTOCOL_NOTIFY and IEVENT

- ● When the protocol will be installed, we achieve arbitrary code execution

- Shellcode + Second stage payload execution

**© BINARLY.IO**

## Slide 48

# **Demo**

https://www.youtube.com/watch?v=EufeOPe6eqk

**© BINARLY.IO**

## Slide 49

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
) © eee eee +
Wdbert Shere thet!
Capprtyht PLD Geren) Carperetter bf) rights rewerend
DPT Ph Leteet Peer eT) f6e ee Peet ere Get bepeererertl: Often ee Oo
LA ee ee Deed ie)
te
ee ee ee Seley -dtebag verifice
Peli thet Geet Cam bet tretir’
7) © Weer theater i eaere* free «(Leelee
SOCCER) NTT TEETH MOTE E SET TT TT TT TT Te Reem ER TRE ET TTT TTT TT eee eee
er “he heer ee ee Le eee
OPE) 1 chewed eet be betel bee eel ered ce eheterl bee ee coer treater
semi tev ented tet
SOOT F Fe eee meme EE EE ET ETE TE NESSES eee eeOS ESTEE NEUE Cee eeR eens
Tr) Ged bebe Uhetlomdte weteg Gyvteef asic § tebe
```

## Slide 50

## **Logo** **_FAIL_**

- Majority of UEFI firmware contains vulnerable images parsers

- ● Hundreds of devices from Lenovo, Intel and Acer allow logo customizations thus are exploitable

- ● Doesn’t require any physical access to the device

- Targets UEFI specific code that affects both x86 and ARM devices

- ● Modern “below-the-OS” defenses, such as Secure Boot are completely ineffective against it

**© BINARLY.IO**

## Slide 51

**Thanks to CERT/CC for coordinating this massive industry-wide disclosure!**

**© BINARLY.IO**

## Slide 52

## **Phoenix Technology** 󰣻

*https://webcache.googleusercontent.com/search?q=cache:cWlnW4oat9sJ:https://www.phoenix.com/security-notifications/cve-2023-5058/

**© BINARLY.IO**

## Slide 53

**That’s all folks, thank you for your attention...**

**... and don’t forget to update your firmware!**

**© BINARLY.IO**
