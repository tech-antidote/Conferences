---
title: "UEFI and the Task of the Translator Using Cross-Architecture UEFI Quines as a Framework for UEFI Exploit Development"
speakers: ["Nika Korchok Wakulich"]
conference: "OffensiveCon"
conference_full: "OffensiveCon 2024"
edition: ""
year: 2024
source_pdf: "OffensiveCon24 slides/Nika Korchok Wakulich_UEFI and the Task of the Translator Using Cross-Architecture UEFI Quines as a Framework for UEFI Exploit Development.pdf"
pages: 108
sha256: "d48793ae985c902301834a6411372f13e6dbf90f99daad8e9249d9f673f72a5a"
text_chars: 71522
ocr_pages: 16
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:22:40Z"
---
# UEFI and the Task of the Translator Using Cross-Architecture UEFI Quines as a Framework for UEFI Exploit Development

**Speakers:** Nika Korchok Wakulich  
**Conference:** OffensiveCon 2024  
**Source:** `OffensiveCon24 slides/Nika Korchok Wakulich_UEFI and the Task of the Translator Using Cross-Architecture UEFI Quines as a Framework for UEFI Exploit Development.pdf` (108 pages)


## Slide 1

```
UEFI and The Task of the
Translator
Using cross-architecture UEFI quines as a framework
for UEFI exploit development
```

```
Nika Korchok Wakulich (ic3qu33n)
OffensiveCon 2024
```

## Slide 2

**DISCLAIMER: The views expressed in this presentation are my own and do not reflect the opinions of my past, present or future employers Viewer Discretion is advised.**

## Slide 3

### **whoami**

**Twitter: @nikaroxanne Discord: @ic3qu33n Mastodon: ic3qu33n@infosec.exchange Website:** **<u>https://ic3qu33n.fyi/</u> GitHub: @ic3qu33n and @nikaroxanne bsky: @ic3qu33n**

**Security Consultant at Leviathan Security Group Reverse engineer + artist + hacker I <3 UEFI, hardware hacking, binary exploitation, skateboarding, learning languages, creating art, writing programs in assembly languages, etc.**

**greetz 2 the following for their assistance/support w this talk: 0day (@0day_simpson), James Chambers (@jamchamb_), Erik Cabetas, netspooky (@netspooky), dnz (@dnoiz1), zeta Xeno Kovah (@xenokovah) Ben Mason (@suidroot), Richard Johnson (@richinseattle), The team at Leviathan OffensiveCon**

## Slide 4

### **This talk is dedicated to Sophia d’Antoine**

## Slide 5

Format of this talk

## Slide 6

##### **Format of this Talk**

This is a talk about translation Part 1: UEFI Quines (self-replicating UEFI apps) in three architectures

x86-64, arm64, EBC Part 2: The evolution of an SMM exploit From simple Chipsec PoC to standalone malicious driver

## Slide 7

##### **Housekeeping** Notes on terminology [This is a talk about translation after all]

“EBC isn’t an “architecture,” it’s a platform agnostic intermediary language that leverages natural-indexing to automatically adjust its instruction width to either 32-bit or 64-bit dependent on the architecture of the host machine. It uses a VM! That sounds like ring -1 to me!”

I know. But referring to it as an architecture at this point in the talk is sufficient for our understanding of EBC in relation to the narrative. And it’s more succinct. We’ll get to EBC and the spec. Hang tight.

Wait… is the architecture arm64? Or aarch64? Or is it AArch64? Aarch64? ARM64? Arm64? Which is it? Team Edward or Team Jacob??

**Team arm64**

**<u>arm64</u>** is the term I will use in this presentation to refer to the assembly language of the Armv8 64-bit architecture, known as ARM64/AArch64

## Slide 8

###### **What is “The Task of the Translator”** **An essay by Walter Benjamin**

- Walter Benjamin was a philosopher, cultural critic, essayist

- Other famous works by Benjamin: “The Work of Art in the Age of Mechanical Reproduction” The Arcades Project

- His essay “The Task of the Translator” was a seminal work in translation theory

- For this presentation, I’ll be referring to Steven Rendall’s English translation of Benjamin’s essay: <u>https://german.yale.edu/sites/default/fles/i benjamin_translators_task.pdf</u>

Walter Benjamin (1892–1940) ~1930 © Charlotte Joel

## Slide 9

**What is “The Task of the Translator” in UEFI?** A framing device for understanding how to write cross-architecture exploits Combine the work of four separate projects using the framework of Walter Benjamin’s “Task of the Translator”

1. UEFI Exploit Research and Development at Leviathan —> SMM exploits

2. BGGP4 and UEFI binary golfing —> UEFI quines

3. OST2 ARM Assembly class —> 4. VX-Underground Black Mass article —> UEFI exploit dev on arm64 EBC

## Slide 10

###### **How do we apply “The Task of the Translator” to UEFI?**

Apply “the Task of the Translator” to two tasks:

1. Translating my winning BGGP4 UEFI quine from x86-64 asm to two other architectures: arm64 and EBC 2. Developing one exploit for an SMM callout vulnerability, then creating new generations of that exploit, altering the technique used, the language the exploit is written, the architecture it targets, etc.

One goal of optimization is to eliminate redundancy. Are we creating redundancy? No, this isn’t redundant work. I’m not creating *copies* of the original UEFI app (the UEFI app already creates copies of itself)

## Slide 11

“Translation is a mode. In order to grasp it as such, we have to go back to the original.” Walter Benjamin, “The Task of the Translator,” translated by Steven Rendall, page 152.

## Slide 12

**How do we apply “The Task of the Translator” to UEFI?** **Notable examples to set the precedent** Developing a “next generation” for a piece of art: • cr4sh - SmmBackdoorNg (Smm Backdoor Next Generation): <u>https://github.com/Cr4sh/SmmBackdoorNg</u> • See cr4sh’s earlier project SmmBackdoor: <u>https://github.com/Cr4sh/SmmBackdoor</u> • Star Trek [with the notable exception of Leonard Nimoy, Leonard Nimoy is eternal]

## Slide 13

##### **What is “The Task of the Translator” in UEFI? Research questions** • What are the essential techniques for UEFI reverse engineering and exploit development?

- How does one UEFI exploit differ when it is translated across multiple different architectures?

- • What can architecture-specific requirements for an exploit teach us about how to approach finding vulnerabilities and writing new gnarly exploits?

- • How many different ways can we write an exploit for an SMM callout vulnerability?

- What **_is_** the task of the translator?

## Slide 14

A brief introduction to UEFI

## Slide 15

##### **Introduction to UEFI** In the beginning there was legacy BIOS

And now we have UEFI and everything is fine! And there are no more vulnerabilities and Secure Boot wasn’t just a marketing strategy for a feature that was never intended as a security feature of UEFI in the first place!

Source: “BIOS Disassembly Ninjutsu Uncovered: Listing 5.27 AMI BIOS Boot Block Jump Table,” 1st edition, Darmawan Salihun (pinczakko), page 60,  https://github.com/pinczakko/BIOS-Disassembly- <u>Ninjutsu-Uncovered</u>

## Slide 16

##### **Introduction to UEFI** In the beginning there was legacy BIOS

And now we have UEFI and everything is fine! And there are no more vulnerabilities and Secure Boot wasn’t just a marketing strategy for a feature that was never intended as a security feature of UEFI in the first place!

Oh… wait, never mind.

## Slide 17

Source: “Trusted Platforms UEFI, PI and TCG-based firmware,” Vincent J. Zimmer (Intel Corporation), Shiva R. Dasari Sean P. Brogan (IBM), White Paper by Intel Corporation and IBM Corporation, September 2009 <u>https://www.intel.com/content/dam/doc/white-paper/uefi-pi-tcg-frmwarei</u> -white-paper.pdf

## Slide 18

###### **Introduction to UEFI Legacy BIOS Reverse Engineering**

- BIOS code was written in 16-bit assembly and it ran in real mode

- Legacy BIOSes were nonstandardized, IBV specific implementations

- Legacy BIOS was responsible for important functionality— initialization of platform hardware in preparation for loading an OS — but it was limited in scope and size

- Refer to “BIOS Disassembly <u>Ninjutsu Uncovered” by Darmawan</u> Salihun (pinczakko) for the holy scripture of Legacy BIOS RE + xdev

Source: “BIOS Disassembly Ninjutsu Uncovered: 5.2.3.2. Decompression Block Relocation,” 1st edition, Darmawan Salihun (pinczakko), page 62,  https://github.com/pinczakko/BIOS-Disassembly-Ninjutsu- <u>Uncovered/blob/master/BIOS_Disassembly_Ninjutsu_Uncovered.pdf</u>

## Slide 19

Source: “Trusted Platforms UEFI, PI and TCG-based firmware,” Vincent J. Zimmer (Intel Corporation), Shiva R. Dasari Sean P. Brogan (IBM), White Paper by Intel Corporation and IBM Corporation, September 2009 <u>https://www.intel.com/content/dam/doc/white-paper/uefi-pi-tcg-frmwarei</u> -white-paper.pdf

## Slide 20

###### **Introduction to UEFI RE advantages of UEFI over Legacy BIOS**

- Rich ecosystem of built-in functionality

- UEFI follows implementation standards with detailed and comprehensive spec [obvious caveats, it’s not perfect but wow look at those diagrams. AMI never gave me a diagram </3]

- source code primarily written in C following a standardized specification —> easier to debug / disassemble

- A selection of great plugins and tools for UEFI RE + xdev:

   - <u>UEFITool: https://github.com/LongSoft/UEFITool</u>

   - <u>efiXplorer: https://github.com/binarly-io/efXplorer i</u>

   - Ghidra plugins:

      - <u>efiSeek: https://github.com/DSecurity/efSeek i</u>

- <u>ghidra-frmwarei</u> -utils: https://github.com/al3xtjames/ <u>ghidra-frmwarei</u> -utils

- • UEFI has expansive breadth + depth —> greater attack surface Source: “UEFI Specification, Fig.7.2 Handle Database”

- <u>https://uefi.org/specs/UEFI/2.10/07_Services_Boot_Services.html#device-handle-to-protocol-handle</u>

<u>mapping</u>

## Slide 21

###### **Introduction to UEFI UEFI apps/drivers + UEFI shell**

- UEFI Shell: A UEFI application that provides a shell interfacing for interacting with various UEFI components (i.e. other UEFI apps and drivers, and the protocols therein)

- UEFI apps and drivers are PE/COFF executables (occasionally TE) and have a PE/COFF header

- The only difference between an UEFI app and a UEFI driver is that an app is unloaded from memory after it is run and a driver remains resident until it is unloaded

Source: “Harnessing the UEFI Shell: Moving the Platform Beyond DOS, 2nd edition,” Vincent Zimmer, Michael Rothman and Tim Lewis

## Slide 22

###### **Introduction to UEFI Protocols**

- Protocols are the keys to the empire

- UEFI is the empire

- A protocol is an interface that encapsulates data and function pointers

- Provide abstractions for hardware/firmware/OS communications

- A driver can produce one or more protocols

Source: “UEFI Specification: Fig. 2.4 Construction of a Protocol” <u>https://uefi.org/specs/UEFI/2.10/02_Overview.html#construction-of-a-protocol</u>

## Slide 23

###### **Introduction to UEFI Protocols Example: LoadedImageProtocol**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Introduction to UEFI
Protocols Example: LoadedimageProtocol
|
il, all Ell I
ial
EFI_MEMORY_TYPE imageDataType
|
```

## Slide 24

“True translation is transparent, it does not obscure the original, does not stand in its light, but rather allows pure language, as if strengthened by its own medium, to shine even more fully on the original.” Walter Benjamin, “The Task of the Translator,” translated by Steven Rendall, page 162.

## Slide 25

UEFI generation 1: x86-64

## Slide 26

###### UEFI generation 1: x86-64

###### **The Specs**

My winning entry in the UEFI app category of Binary Golf Grand Prix 4 • BGGP: “The goal of the Binary Golf Grand Prix is to challenge programmers to make the smallest possible binary that fits within certain constraints.” [Source “Binary Golf Grand Prix”, netspooky, https://n0.lol/bggp/]

Source: “Binary Golf Grand Prix 4,” Binary Golf Association,  https://binary.golf/

## Slide 27

#### UEFI generation 1: x86-64 **Methodology**

1. Write a valid working solution (a self-replicating UEFI app) in C

2. Use the C solution as a base text and translate the quine from C to assembly —> Reverse engineer the C solution

3. Golf the assembly solution and shrink the size of the binary as much as possible 4. Reverse engineer, rewrite and refactor the assembly

Size of C quine: ~17,000 bytes

Final size of x86_64 asm UEFI quine: 1480 bytes

[Side note: shoutout to my friend @netspooky who I worked with on this project for teaching me PE binary mangling. Check out his fantastic write-up on his recent solution that set the new record to 420 bytes: https://github.com/netspooky/golfclub/tree/master/uef/bggp4]i

## Slide 28

##### **UEFI generation 1: x86-64 RE and development tools**

- nasm

- Hex editor (xxd, hexdump)

- Ghidra, specifically using these two plugins for UEFI:

   - efiSeek: https://github.com/DSecurity/efiSeek

   - ghidra-firmware-utils: https://github.com/al3xtjames/ghidra-firmware-utils

- Radare2 for a faster option, better for disassembling and other reversing tasks near the end of the project that involved nitty gritty changes to the assembly

- QEMU and gdb for debugging/testing

• I didn’t use IDA Pro for this project, it’s a better tool for other projects

## Slide 29

UEFI generation 1: x86-64 **UEFI x64 - Handof f** **state upon program invocation**

rcx - EFI_HANDLE rdx - EFI_SYSTEM_TABLE*

rsp - <return address> Source: UEFI Specification - 2.3.4.1. Handoff State

Program entry point - setting up stack frame, saving gST, ImageHandle Use gST to save gBS and ConOut

## Slide 30

**Base text: Self-replicating UEFI app Written in C**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
UEFI Interactive Shell v2.2
EDK II
UEFI v2.70 CEDK II, @x@0010000)
Mapping table
FS@: Alias(s):HDQa1: ;BLK1:
PciRoot(@x@)/Pci (0x1, 0x1)/Ata(Ox®)/HD(1,MBR, @xBE1AFDFA, @x3F , @xFBFC1)
BLK@: Alias(s):
PciRoot(Qx®@)/PciC@x1, @x1)/AtaC@xd)
BLK2: Alias(s):
PciRoot(0x@)/PciC@x1, @x1)/AtaC@xd)
[Press ESC in 3 seconds to skip startup.nsh or any other key to continue.
[Shell> fs:
FS@:\>
Base text:
Self-replicating UEFI app
Written in C
```

## Slide 31

#### UEFI generation 1: x86-64 **x64 self-replicating UEFI app - program logic breakdown**

gBS->HandleProtocol() gBS->HandleProtocol() Retrieve LoadedImageProtocol Retrieve SimpleFilesystemProtocol

SimpleFilesystemProtocol->OpenVolume() FileProtocol->OpenFile() Retrieve Root Volume Open Host File

FileProtocol->OpenFile() Open Target File

FileProtocol->CloseFile() Close Target File, Host File + Root Volume

gBS->FreePool() Free buffer FileProtocol->WriteFile() FileProtocol->ReadFile() gBS->AllocatePool() Write buffer to target file Read host file into buffer Allocate buffer to hold file contents

## Slide 32

#### UEFI generation 1: x86-64 **x64 self-replicating UEFI app - program logic breakdown**

gBS->HandleProtocol() Retrieve LoadedImageProtocol

gBS->HandleProtocol() Retrieve SimpleFileSystemProtocol

## Slide 33

#### UEFI generation 1: x86-64 **x64 self-replicating UEFI app - program logic breakdown**

SimpleFileSystemProtocol->OpenVolume() Retrieve Root Volume

## Slide 34

UEFI generation 1: x86-64 **x64 self-replicating UEFI app - program logic breakdown** FileProtocol.OpenFile() FileProtocol.OpenFile() Open Host File Open Target File

###### FileProtocol.OpenFile() Open Target File

## Slide 35

UEFI generation 1: x86-64 **x64 self-replicating UEFI app - program logic breakdown** FileProtocol.ReadFile() gBS->Allocate ~~Pool()~~ Read host file into buffer Allocate buffer to hold file contents

FileProtocol.ReadFile() Read host file into buffer

## Slide 36

UEFI generation 1: x86-64 **x64 self-replicating UEFI app - program logic breakdown** FileProtocol->WriteFile() Write buffer to target file

## Slide 37

#### UEFI generation 1: x86-64 **x64 self-replicating UEFI app - program logic breakdown**

FileProtocol->CloseFile()
gBS->FreePool()
Close Target File,
Free buffer
Close Host File +
Close Root Volume

## Slide 38

#### UEFI generation 1: x86-64 **x64 self-replicating UEFI app - program logic breakdown**

gBS->HandleProtocol() gBS->HandleProtocol() Retrieve LoadedImageProtocol Retrieve SimpleFilesystemProtocol

SimpleFilesystemProtocol->OpenVolume() FileProtocol->OpenFile() Retrieve Root Volume Open Host File

FileProtocol->OpenFile() Open Target File

FileProtocol->CloseFile() Close Target File, Host File + Root Volume

gBS->FreePool() Free buffer FileProtocol->WriteFile() FileProtocol->ReadFile() gBS->AllocatePool() Write buffer to target file Read host file into buffer Allocate buffer to hold file contents

## Slide 39

#### UEFI generation 1: x86-64

**Golfing the solution**

1. Remove unnecessary libraries and dependencies: Use the UEFI ecosystem

2. PE Binary Mangling [netspooky’s guide to PE Binary Mangling: <u>https://n0.lol/a/pemangle.html ]</u>

3. Use the protocols you want, not the wrappers with extra fluff: e.g. OpenProtocol() is a wrapper for HandleProtocol()

First call to gBS function HandleProtocol in my winning BGGP4 entry

## Slide 40

###### **Final winning entry for BGGP4: Self-replicating UEFI app Written in x64 assembly** **<u>https://youtu.be/MglEnqr-1yY</u>**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
UEFI Interactive Shell v2.2
EDK II
UEFI v2.70 CEDK II, @x@0010000)
Mapping table
FS@: Alias(s):HDQa1: ;BLK1:
PciRoot(@x®)/Pci(Ox1, 0x1)/Ata(Ox®)/HD(1,MBR, @xBE1AFDFA, @x3F , @xFBFC1)
BLK@: Alias(s):
PciRoot(@x®@)/PciC@x1,@x1)/AtaC@xd)
BLK2: Alias(s):
PciRoot(0x®@)/PciC@x1, @x1)/AtaC@xd)
[Press ESC in 4 seconds to skip startup.nsh or any other key to continue.
[Shell> fs@:
[FS@:\> 1s
Directory of: FS@:\
@5/02/2024 06:41 1,540 self-rep-golf.efi N
@5/02/2024 06:41 17,856 UEFISelfRep.efi
2 File(s) 19,396 bytes
@ DirCs)
FS@:\>
Final winning entry for BGGP4:
Self-replicating UEFI app
Written in x64 assembly
https://youtu.be/MglEnqr-1yY
```

## Slide 41

#### UEFI generation 1: x86-64 **What did you learn at school today?**

- Leverage the UEFI ecosystem by walking from Protocol interface to Protocol interface —> better understanding of UEFI internals and base knowledge for building better exploits

   - Building ROP chains for SMM exploits to bypass Smm_CodeCheck_En

- New knowledge of PE Binary Mangling

- Knowledge of how to write UEFI shellcode

   - even if you write an exploit in C, knowing how to write UEFI shellcode for a payload is essential

## Slide 42

“The translator's task consists in this: to find the intention toward the language into which the work is to be translated, on the basis of which an echo of the original can be awakened in it.” Walter Benjamin, “The Task of the Translator,” translated by Steven Rendall, page 159.

## Slide 43

UEFI generation 2: arm64

## Slide 44

#### UEFI generation 2: arm64

###### **The specs**

- This is not an entry for BGGP4… what are the goals of this UEFI quine?

   - Confirm that a UEFI quine is *possible* on Aarch64/ARM64 architecture

   - Translate original x64 solution to valid working solution in arm64 assembly

   - Golfing -> Optimize for small size to maximize benefit of shellcode

- What are the goals for this UEFI arm64 project?

   - Advance mastery of arm64 assembly for teaching OST2 ARM Assembly class

   - Practice writing UEFI shellcode in arm64 assembly

   - Better understand the nuances of UEFI RE and exploit dev on arm64

## Slide 45

###### UEFI generation 2: arm64

**Methodology** 1. Recompile my valid working solution (a self-replicating UEFI app) in C with an arm64 (edk2 calls it aarch64) toolchain under the edk2 build system -> working solution to use as a base template 2. Use the C solution as a base text and translate the quine from C to assembly —> Reverse engineer the C solution

3. Reverse engineer, rewrite and refactor the assembly The task of the translator is to be a cross-compiler?

Bonus Step 0: Start with a “Hello world” UEFI app written in arm64 assembly

## Slide 46

UEFI generation 2: arm64 **arm64 assembly building blocks: handof state f**

X0 - EFI_HANDLE

X1 - EFI_SYSTEM_TABLE

X30 - Return Address Source: UEFI Specification - 2.3.6.2. Handoff State <u>https://uef.org/specs/UEFI/2.10/02_Overview.html#handofi</u> f-state-4

## Slide 47

###### **Base text: Self-replicating UEFI app Written in C, cross-compiled for arm64** **<u>https://youtu.be/af8IanzkYyQ</u>**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
UEFI Interactive Shell v2.1
EDK II
UEFI v2.60 (EDK II, 0x@0010000)
Mapping table
FS@: Alias(s):HD@b:;BLK1:
PciRoot (@x@) /Pci(@x1,@x@) /HD(1,MBR, @xBE1AFDFA, 0x3F, @xFBFC1)
BLK3: Alias(s):
VenHw( F9B94AE2-8BA6-409B-9D56-B9B417F53CB3)
BLK2: Alias(s):
VenHw(8047DB4B-7E9C—4C@C—8EBC—DFBBAACACESF )
BLK@: Alias(s):
PciRoot (@x@) /Pci(Ox1, 0x0) >
[Press ESC in 5 seconds to skip startup.nsh or any other key to continue.
Shell>
Base text: Self-replicating UEFI app
Written in C, cross-compiled for arm64
https://youtu.be/af8lanzkYyQ
```

## Slide 48

“In reality, with regard to syntax, word-for-word translation completely rejects the reproduction of meaning and threatens to lead directly to incomprehensibility.” Walter Benjamin, “The Task of the Translator,” translated by Steven Rendall, page 161.

## Slide 49

**arm64 UEFI quine RE and xdev**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
undefineds
(0001348 fd 7b b6 a9
0000134c fd
00001350 e0
00001354 el
00001358 e0
0000135c 00
00001360 e0
00001364 20
00001368
0000136c
00001370
00001374
00001378
0000137c
00001380
00001384
00001388
0000138c
00001390
00001394
00001398
0000139c
000013a0
000013a4
000013a8
00001 3ac
000013b0
000013b4
000013b8
000013bc
000013c0
000013c4
000013c8
000013cc
000013d0
000013d4
03
of
Ob
Ob
30
4b
34
63
63
00
00
00
40
40
00
86
ab
00
8d
00
82
00
87
b4
cd
e7
00
40
40
01
01
80
80
40
ol
00
40
3f
00
40
00
00
01
00
91
f9
f9
f9
f9
f9
52
72
bo
12
79
52
79
d2
f2
f2
f2
f9
f9
f9
91
91
52
d2
f9
aa
aa
f9
d6
f9
f9
fl
54
91
aa
Stack[-Oxa0]:
UefiSelfRepMain
stp
mov
str
str
ldr
ldr
str
mov
movk
str
mov
strh
mov
strh
mov
movk
movk
movk
str
ldr
ldr
add
add
mov
mov
ldr
mov
mov
ldr
blr
str
ldr
cmp
b.ne
add
mov
8 local_aO
x29,x30,[sp, #local_a0]!
x29, sp
ImageHandle, [sp, #local_88]
gST, [sp, #local_90]
ImageHandle, [sp, #local_90]
ImageHandle, [ImageHandle, #0x60]
ImageHandle, [sp, #qBS]
ImageHandle, #0x3lal
ImageHandle,#0xSblb, LSL #16
ImageHandle, [sp, #efiLoadedImageProtocolGuid.D...
ImageHandle, #Oxf ff f9562
ImageHandle, [sp, #efiLoadedImageProtocolGuid.D...
ImageHandle, #0x1ld2
ImageHandle, [sp, #efiLoadedImageProtocolGuid.D...
ImageHandle, #0x3f8e
ImageHandle,#0xa000, LSL #16
ImageHandle,#0x69c9, LSL #32
ImageHandle,#0x3b72, LSL #48
ImageHandle, [sp, #et1LoadedImageProtocolGuid.D...
ImageHandle, [sp, #gBS]
efiOpenProtocol, [ImageHandle, #0x118]
gST, sp,#0x70
ImageHandle, sp, #0x60
w5,#0x1
x4,#0x0
x3, [sp, #local_88]
x2, 9ST
gST, ImageHandle
ImageHandle, [sp, #local_88]
efi0penProtocol
ImageHandle, [sp, #local_8]
ImageHandle, [sp, #local_8]
ImageHandle, #0x0
LAB_00001698
ImageHandle, sp, #0x70
gST, ImageHandle
RE and xdev
BESSBIR ALSVVSsaraaARaNssBSIFALBV ASSaeruau
4 d.Ro & @ = yx
uVarll = 0;
efiImageHandle = ImageHandle;
local_8 = (*efiOpenProtocol) (ImageHandle, &efiLoadedImageProtocolGuid, efiLoadedImageProtocol,
ImageHandle, (EFI_HANDLE) 0x0, 1);
if (local_8 == 0) {
FUN_0000lelc((undefined *)
L"EFI BootServices OpenProtocol call with loadedimageprotocol was successful: %p
, &local_30, efiLoadedImageProtocol, efilmageHandle, uVarll,uVarl12,
(ulonglong)efiOpenProtocol,in_x7);
local_18 = *(EFI_HANDLE *)((longlong)local_30 + 0x18);
local_20 = *(UINTN *)((longlong)local_30 + 0x48);
local_58._0.4 = 0x964e5b22;
local_58._4 2 = 0x6459;
local_58._6 2. = Oxlld2;
local_58[8] = Ox8e;
local_58[9] = '9';
uStack_4e = '\0';
uStack_4d = Oxa0;
uStack_4c._0.1_ = Oxc9;
uStack_4c._11. = 'i';
uStack_4c._ 21 = 'r';
uStack_4c. 31 =';';
efiOpenProtocol = gBS->OpenProtocol;
efiLoadedImageProtocol = &local_48;
uVarl2 = 1;
uVarll = 0;
local_8 = (*efi0penProtocol) (local_18, (EFI_GUID *)local_58,efiLoadedImageProtocol, ImageHandle,
(EFI_HANDLE) 0x0, 1);
if (local_8 == 0) {
FUN_00001le1c((undefined *)
L"EFI BootServices OpenProtocol call with simplefilesystemprotocol was successf
: %p \n"
, &local_30, efiLoadImageProtocol, ImageHandle, uVarl1,uVarl2,
(ulonglong)efiOpenPPotocol, in_x7);
}
peVar6 = *(code **)((longlong)local_48 + 8);
puVarl = &local_60;
local_8 = (*pcVar6) (local_48);
if (local 8 == 0) {
```

## Slide 50

**arm64 UEFI quine RE and xdev**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
mov
movk
str
mov
strh
mov
strh
mov
movk
movk
movk
str
ldr
ldr
add
add
mov
mov
ldr
MageHandle, [sp, #local_o
ImageHandle, [sp, #local_8]
ImageHandle, #0x0
LAB_00001698
ImageHandle, sp, #0x70
gST, ImageHandle
ImageHandle, 0x4000
ImageHandle=>u_EFI_BootServices_OpenProtocol_c...
Print
ImageHandle, [sp, #loadedImageProtocol]
ImageHandle, [ImageHandle, #0x18]
ImageHandle, [sp, #local_18]
ImageHandle, [sp, #loadedImageProtocol]
ImageHandle, [ImageHandle, #0x48]
ImageHandle, [sp, #local_20]
ImageHandle, #0xSb22
ImageHandle,#0x964e, LSL #16
ImageHandle, [sp, #local_58]
ImageHandle, #0x6459
ImageHandle=>DAT_00006459, [sp, #local_54]
ImageHandle, #0x1ld2
ImageHandle, [sp, #local_52]
ImageHandle, #0x398e
ImageHandle,#0xa000, LSL #16
ImageHandle,#0x69c9, LSL #32
ImageHandle,#0x3b72, LSL #48
ImageHandle, [sp, #local_5S0]
ImageHandle, [sp, #gBS]
efiOpenProtocol, [ImageHandle, #0x118]
gST, sp, #0x58
ImageHandle, sp, #0x48
w5, #0x1
x4, #0x0
efilmaqeHandle, [sp
armo4 LU
RE and xdev
#local 88
quine
= u"EFI Bo 0
longlong Print (undefined * pa
if (local_8 == 0) {
Print ((undefined *)
L"EFI BootServices OpenProtocol call with loadedimageproto
&loadedImageProtocol, efiLoadedImageProtocol, efilmageHandle
(ulonglong)efiOpenProtocol,in_x7);
local_18 = loadedImageProtocol->DeviceHandle;
local _ _20 = loadedImageProtocol->ImageSize;
local_58.04 = oreeesi2e:
local | 58.42 = Ox F
local_ _58. “6.2. = 0x1ld2;
local_58[8] = Ox8e;
local_S8[9] = '9';
uStack_4e = '\0';
uStack_4d = Oxa0;
uStack_4c. 01 =
uStack_4c, 11. =
uStack_4c._21 = 'r';
uStack_4c, 31 = ;
efiOpenProtocol = gBS->OpenProtocol;
ppvVar7 = &local_48;
uVarl3 = 1;
uVarl2 = 0;
local_8 = (*efiOpenProtocol) (local_18, (EFI_GUID *)local_58, ppvVa
HF
if (local_8 == 0) {
Print ((undefined *)
L"EFI BootServices OpenProtocol call with simplefilesyst
, &LoadedImageProtocol, ppvVar7, ImageHandle, uVarl2, uVarl13,
a
}
pcVar8 = *(code **)((Longlong)local_48 + 8);
puVarl = &local_60;
```

## Slide 51

###### **arm64 UEFI quine RE and xdev**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
r mageHandle,[sp, #9
ldr efiOpenProtocol, [ImageHandle, #0x118]
add gST, sp, #0x70
add ImageHandle, sp,#0x60
mov w5, #0x1
mov x4,#0x0
ldr x3, [sp, #local_88]
mov x2, 9ST
mov gST, ImageHandle
ldr ImageHandle, [sp, #local_88]
blr efi0penProtocol
str ImageHandle, [sp, #local_8]
ldr ImageHandle, [sp, #local_8]
cmp ImageHandle, #0x0
b.ne LAB_00001698
add ImageHand1le, sp, #0x70
mov gST, ImageHandle
adrp ImageHandle, 0x4000
add ImageHandle=>u_EFI_BootServices_OpenProtocol_c...
bl Print
ldr ImageHandle, [sp, #loadedImageProtocol]
ldr ImageHandle, [ImageHandle, #0x18]
str ImageHandle, [sp, #local_18
ldr ImageHandle, [sp, #loadedImageProtocol]
ldr ImageHandle, [ImageHandle, #0x48]
str ImageHandle, [sp, #local_20
mov ImageHandle, #0xSb22
movk ImageHandle,#0x964e, LSL #16
str ImageHandle, [sp, #local_58
mov ImageHand1le, #0x6459
strh ImageHandle=>DAT_00006459, [sp, #local_54]
mov ImageHandle, #0x11ld2
strh ImageHandle, [sp, #local_52
mov ImageHand le, #0x398e
arm64 UEFI quine
RE and xdev
SINFSSBISRLIVASSSLVSALON4ASESSSEGEGHE
EFI_STATUS local_8;
gBS = gST->BootServices;
efiLoadedImageProtocolGuid.Datal = OxSblb3lal;
efiLoadedImageProtocolGuid.Data2 = 0x9562;
efiLoadedImageProtocolGuid.Data3 = Ox1ld2;
efiLoadedImageProtocolGuid.Data4[0] = Ox8e;
efiLoadedImageProtocolGuid.Data4[1] = '?';
efiLoadedImageProtocolGuid.Data4[2] = '\0';
efiLoadedImageProtocolGuid.Data4[3] = Oxa0;
efiLoadedImageProtocolGuid.Data4[4] = Oxc9;
efiLoadedImageProtocolGuid.Data4[5] = ‘'i';
efiLoadedImageProtocolGuid.Data4[6] = 'r';
efiLoadedImageProtocolGuid.Data4[7] = ';';
efiOpenProtocol = gBS->OpenProtocol;
efiLoadedImageProtocol = &l@adedimagerrotocul ;
uVarl3 = 1;
uVarl2 = 0;
efiImageHandle = ImageHandle;
local_8 = (*efiOpenProtocol) (ImageHandle, &efiLoad\dImageProtocol
ImageHandle, (EFI_HANDLE) 0x0, 1);
if (local_8 == 0) {
Print((undefined *)
L"EFI BootServices OpenProtocol call with loadedimagepro
&loadedImageProtocol, efiLoadedImageProtocol, efilmageHand
(ulonglong)efiOpenProtocol,in_x7);
local_18 = loadedImageProtocol->DeviceHandle;
local_20 = loadedImageProtocol->ImageSize;
local_58._0 4 = 0x964e5b22;
local_58._4 2 = 0x6459;
local _ _58. “62. = 0x1lld2;
local_S8[8] = Ox8e;
local_58[9] = '9';
uCtrele An tN,
en
```

## Slide 52

###### **arm64 UEFI quine RE and xdev**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
MOV MageHand le, #Oxsla
movk ImageHandle,#0xSblb, LSL #16 gBS = gST->BootServices;
str ImageHandle, [sp, #efiLoadedImageProtocolGuid.D... efiLoadedImageProtocolGuid.Datal = OxSblb3lal;
mov ImageHand le, #Oxf ff f9562 efiLoadedImageProtocolGuid.Data2 = 0x9562;
strh ImageHandle, [sp, #efiLoadedImageProtocolGuid.D... efiLoadedImageProtocolGuid.Data3 = Ox11d2;
mov ImageHandle, #0x11d2 efiLoadedImageProtocolGuid.Data4[0] = Ox8ef]
strh ImageHandle, [sp, #efiLoadedImageProtocolGuid.D... efiLoadedImageProtocolGuid.Data4[1] = '?';
mov ImageHand le, #0x3f8e efiLoadedImageProtocolGuid.Data4[2] = '\0';
movk ImageHandle,#0xa000, LSL #16 efiLoadedImageProtocolGuid.Data4[3] = Oxa0;
movk ImageHandle,#0x69c9, LSL #32 efiLoadedImageProtocolGuid.Data4[4] = Oxc9;
movk ImageHandle,#0x3b72, LSL #48 efiLoadedImageProtocolGuid.Data4[5] = 'i';
str ImageHandle, [sp, #efiLoadedImageProtocolGuid.D... efiLoadedImageProtocolGuid.Data4[6] = 'r';
ldr ImageHandle, [sp, #gBS] efiLoadedImageProtocolGuid.Data4[7] = ';';
ldr efiOpenProtocol, [ImageHandle, #0x118] efiOpenProtocol = gBS->OpenProtocol;
add gST, sp,#0x70 efiLoadedImageProtocol = &local_30;
add ImageHandle, sp, #0x60 uVarl2 = 1;
mov w5, #0x1 uVarll = 0;
mov x4,#0x0 efilmageHandle = ImageHandle;
ldr x3, [sp, #local_88] local_8 = (*efiOpenProtocol) (ImageHandle, &efiLoadedImageProtocolGuid, efiLoadedImageProtoc
mov x2, 9ST ImageHandle, (EFI_HANDLE) 0x0, 1);
mov gST, ImageHandle if (local_8 == 0) {
ldr ImageHandle, [sp, #local_88] Print ((undefined *)
bir efi0penProtocol L"EFI BootServices OpenProtocol call with loadedimageprotocol was successful: %p
str ImageHandle,[sp, #local_8] &local_30, efiLoadedImageProtocol, efilmageHandle, uVarll,uVarl2, (ulonglong)efi0pent
ldr ImageHandle, [sp, #local_8] in_x7);
cmp ImageHandle, #0x0 local_18 = *(EFI_HANDLE *)((longlong)local_30 + 0x18);
b.ne LAB_00001698 local_20 = *(UINTN *) ((longlong) local_30 + 0x48);
add ImageHandle, sp, #0x70 local_58._0.4 = Ox964e5b22;
mov gST, ImageHandle local_58._4 2 = 0x6459;
adrp ImageHandle, 0x4000 local_58._6 2. = Ox1ld2;
add ImageHandle=>u_EFI_BootServices_OpenProtocol_c... = u"EFI BootServices OpenPro local 58[8] = Ox8e;
bl Print longlong Print (undefined * pa local 58[9] = '9';
ldr ImageHandle, [sp, #local_30] uStack_4e = '\0';
1dr ImageHandle, [ImaqeHandle, #0x18 Ad Ont
armo4 U quine
RE and xdev
```

## Slide 53

**arm64 UEFI RE**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2SxRae
FPESSSSEBYSBLRESRBSSSBHUSSSS8S8sEsas
Oo
© Ore o
FOorF+rOoOOoOocoO
00001410 e2
00001414 20
00001418 01
0000141c e0
#38
80 d2
40 f9
00 aa
00 bo
00 91
40 f9
3f dé
00 f9
40 f9
00 fl
00 54
Ql 91
00 aa
00 fo
33 91
00 94
40 f9
40 f9
00 f9
40 f9
40 f9
00 f9
40 f9
01 91
00 f9
Ql 91
00 aa
00 fo
36 91
00 94
40 f9
40 f9
ER
40 f9
00 aa
00 bo
00 91
40 f9
3f dé
:
>
8
°o
8
00001424 e0 47 00 f9
478 ef)
x4,#0x0
x3, [sp, #local_78]
x2, param_1
param_1,0x6000
param_2=>EfiLoadedImageProtocolGuid, param_1,#0x8
param_l,[sp, #local_78]
x6
param_l,[sp, #local_8]
param_l,[sp, #local_8]
param_1,#0x0
LAB_00001658
param_1,sp,#0x60
param_2,param_1
param_1,0x4000
param_l=>u_EFI_BootServices_OpenProtocol_ca_00... = u"
FUN_00001ddc long]
param_l,[sp, #Stack[-0x30] ]
param_1,[param_1, #0x18]
param_l,[sp, #local_20]
param_l,[sp, #Stack[-0x30)] ]
param_l,[param_l, #0x48]
param_l,[sp, #local_28]
param_l,[sp, #Stack[-0x30)] ]
param_1,param_1,#0x40
param_l,[sp, #local_48]
param_l,sp,#0x48
param_2,param_1l
param_1,0x4000
param_l=>u_Base_Address_of_Image:_%p_00004d98....
FUN_00001dde
param_l,[sp, #local_10]
x6, [param_l1, #0x118]
param_1,sp,#0x58
wS, #0x1
x4, #0x0
x3, [sp, #local_78]
ppvVar6, param_1
param_1,0x6000
param_2=>EfiSimpleFileSystemProtocolGuid, param...
param_l,[sp, #local_20]
x6
param_l,[sp, #local_8]
Dara D ler
EFI_LOADED IMAGE PROTOCOL *pEStack_30;
UINTN local_28;
EFI_HANDLE local_20;
UINT64 local_18;
EFI_BOOT_SERVICES *local_10;
EFI_STATUS local_8;
local_10 = param_2->BootServices;
local_50 = (EFI_FILE_PROTOCOL *)0x0;
local_58 = 0;
local_18 = 0;
pEVarl7 = local_10->OpenProtocol;
ppvVax6 = &pEStack_30;
uVarI¥ = 1;
uVarl3 = 0;
pvVar9 = param_l;
local_8 = (*pEVarl17) (param_1,&EfiLoadedImageProtocolGuid, ppvVar6, param_1, (EF
if (local_8 == 0) {
FUN_00001ddc ((undefined *)
L"EFI BootServices OpenProtocol call with loadedimageprotoco
, &pEStack_30, ppvVar6, pvVar9, uVarl3, uVarl15, (ulonglong)pEVarl17,
local_20 = BEStaekiJS6->DeviceHandle;
local_28 = pEStack_30->ImageSize;
local_48 = &pEStack_30->ImageBase;
FUN_00001ddc ((undefined *)L"Base Address of Image: %p \n",&local_48, ppvVa
, (ulonglong)pEVarl7,in_x7);
pEVarl7 = local_10->OpenProtocol;
Interface = &local_38;
uVarl5 = 1;
uVarl3 = 0;
local_8 = (*pEVar17) (local_20, &EfiSimpleFileSystemProtocolGuid, Interface,
mela
if (local_8 == 0) {
FUN_00001ddc ((undefined *)
L"EFI BootServices OpenProtocol call with simplefilesystemp
: %p \n"
, &pEStack_30, Interface, param_1,uVarl3,uVar15, (ulonglong)pE
}
pEVar6 = local_38->OpenVolume;
ppEVarl = &local_40;
local_8 = (*pEVar6) (local_38, ppEVarl);
if (local 8 == 0
```

## Slide 54

##### **UEFI generation 2: arm64 RE and development tools**

- Write the assembly program and build it with the edk2 build system

   - This was easiest option because I wrote this on an arm64 machine (an M1 MacBook Pro) but the bindings for arm64 with the native Xcode Tools command line tools are for *Darwin* arm64 and for generating Mach-O arm64 binaries

   - UEFI apps and drivers are predominately PE files (and occasionally TE) that don’t use the Darwin bindings

   - The edk2 build system finally came through and was up to this task of generating arm64 UEFI apps

- For an assembler with solid UEFI support, there is the ARM-specific flavor of FASM:  FASMARM: https://arm.flatassembler.net/

   - [Note FASMARM only supports 32-bit and 64-bit ARM architectures up until v8; valid solution for ARM32 builds but not arm64 builds)

- Hex editor (xxd, hexdump)

- Ghidra with efiSeek and ghidra-firmware-utils

- radare2 for disassembly

- QEMU and gdb for debugging/testing

## Slide 55

**Final arm64 quine: Self-replicating UEFI app Written in arm64 assembly** **<u>https://youtu.be/C-jaMoCwdJE</u>**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
UEFI Interactive Shell v2.1
EDK II
UEFI v2.60 (EDK II, 0x@0010000)
Mapping table
FS@: Alias(s):HDOb:;BLK1:
PciRoot (0x0) /Pci(@x1, @x@) /HD(1,MBR, @xBE1AFDFA, 0x3F , @xFBFC1)
BLK3: Alias(s):
VenHw( F9B94AE2-8BA6—409B-9D56-B9B417F53CB3)
BLK2: Alias(s):
VenHw(8047DB4B-7E9C—4C@C-8EBC-DFBBAACACESF )
BLK@: Alias(s):
PciRoot (0x0) /Pci(@x1, 0x0)
Press ESC in 3 seconds to skip startup.nsh or any other key to continue.
Shell> fs:
FS@:\>
Final arm64 quine:
Self-replicating UEFI app
Written in arm64 assembly
https://youtu.be/C-jaMoCwd
```

## Slide 56

## **arm64 UEFI debugging qemu & gdb**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
/Users/nika/uefi_testing/edk2/MdePkg/Library/BaseLib/DivU64x32Remainder .c
1 /** @fil
Math worker functions.
Copyright (Cc) 2006 - 2008, Intel Corporation. All rights reserved.<BR>
SPDX-License-Identifier:
**/
BSD-2-Clause-Patent
#include "BaseLibInternals.h"
[**
Divides a 64-bit unsigned integer by a 32-bit unsigned integer and generates
arm64 UEFI debugginc
a 64-bit unsigned result and an optional 32-bit unsigned remainder.
qemu & gdb
<DivU64x32Remainder>
<DivU64x32Remainder+4>
<DivU64x32Remainder+8>
<DivU64x32Remainder+12>
<DivU64x32Remainder+16>
<DivU64x32Remainder+2Q0>
<DivU64x32Remainder+24>
<DivU64x32Remainder+28>
<DivU64x32Remainder+32>
<DivU64x32Remainder+36>
<DivU64x32Remainder+4Q>
<DivU64x32Remainder+44>
<DivU64x32Remainder+48>
<DivU64x32Remainder+52>
stp
mov
str
str
str
bl
and
cmp
b.eq
ldr
cmp
b.ne
adrp
add
x29, x30, [sp, }!
x29, sp
xO, [sp, J
wi, [sp, J
x2, [sp, J
<DebugAssertEnabled>
w0, wQ,
w,
<DivU64x32Remainder+72>
w0, Csp, J
wd,
<DivU64x32Remainder+72>
x@, <CpuBreakpoint+912>
x2, xO,
lexec No process In:
(No debugging symbols found in UEFI_bb_disk/UefiQuineAarch64. efi)
Cgdb) info files
Symbols from "/Users/nika/uefi-task-of-the-transLator/Aarch64_UEFI_exploits/UEFI_bb_disk/UefiQuineAarch64.efi".
Local exec file:
*/Users/nika/uefi-task-of-the-transLator/Aarch64_UEFI_exploits/UEFI_bb_disk/UefiQuineAarch64.efi', file type pei-aarch64-little.
Entry point: @x1000
Qx0000000000001000 - Ox0000000000005000 is .text
@x0000000000005000 - Ox0000000000006000 is
@x0000000000006000 - 0x0000000000007000 is
(gdb) add-symbol-file ~/uefi_testing/edk2/Build/BareBonesPkg/DEBUG_GCC/Aarch64/UefiQuineAarch64.debug @x7875e000 -s .data 0x78762000
add symbol table from file "/Users/nika/uefi_testing/edk2/Build/BareBonesPkg/DEBUG_GCC/Aarch64/UefiQuineAarch64.debug" at
.text_addr = 0x7875e000
.data_addr = 0x78762000
gy orn) y
Reading symbols from /Users/nika/uefi_testing/edk2/Build/BareBonesPkg/DEBUG_GCC/Aarch64/UefiQuineAarch64.debug...
(gdb)
.data
-reloc
L??
PC:
2?
```

## Slide 57

UEFI generation 2: arm64 **What did you learn at school today?** • Leverage the UEFI ecosystem by walking from Protocol interface to Protocol interface —> better understanding of UEFI internals and base knowledge for building better exploits

   - Building ROP chains for arm64 exploits

- Learning how to set up debugging for arm64 UEFI apps/drivers

- Knowledge of how to write UEFI shellcode for arm64

   - Expanded repertoire of knowledge and skills for UEFI exploit dev

   - Additional working payloads for arm64 UEFI exploits

## Slide 58

UEFI generation 3: EBC

## Slide 59

##### **EBC - EFI Byte Code**

###### **Why EBC?**

- EBC was a natural fit as the final architecture to choose for this project because of the inherent variability/malleability of natural indexing and the EBC spec itself

- • EBC aims to become something of a tower of Babel: a platform-agnostic architecture specification for PCI option ROM implementation; it uses naturalindexing to adjust the width of its instructions (32-bit or 64-bit) depending on the architecture of the host

- • EBC is an intermediate language (like LLVM byte code, Java byte code, [insert your favorite byte code here]) and it is run in the EFI Byte Code Virtual Machine (EBCVM)

- • If a compiler is a translator, then EBC could be considered the holy scripture [per Benjamin’s metaphor])…

## Slide 60

“For to some degree all great writings, but above all holy scripture, contain their virtual translation between the lines. The interlinear version of the holy scriptures is the prototype or ideal of all translation.” Walter Benjamin, “The Task of the Translator,” translated by Steven Rendall, page 165.

## Slide 61

#### UEFI generation 3: EBC **UEFI EBC architecture details**

- EBCVM uses 8 general purposes registers:

   - R0-R7

- EBCVM has 2 dedicated registers:

   - IP (instruction pointer)

   - F (Flags register)

- Natural indexing: uses a natural unit to calculate offsets of data relative to a base address, where a natural unit is defined as:

- Natural unit == sizeof (void *)

Source: “UEFI Spec, Chapter 22: EFI Byte Code Virtual Machine,” <u>https://uefi.org/specs/UEFI/2.10/22_EFI_Byte_Code_Virtual_Machine.html#natural-indexing</u>

## Slide 62

##### **EBC - EFI Byte Code If EBC is so great then why haven’t I heard of it?**

- Only one compiler specifically designed to target valid EBC binaries: the proprietary Intel C compiler for EBC

- This proprietary Intel C compiler for EBC was available for the low price of $995 [to my knowledge, it is no longer available; now the page on the Intel Products site redirects to an IoT toolkit for $2399]

- Open-source options are available … sort of

   - fasm-ebc is the closest open-source version to the Intel C compiler for EBC but it can’t handle edge cases for encoding instructions with natural-indexing [see this issue in the *archived* fasm-ebc GitHub repo: ]

- Very few in-the-wild reference EBC images

- EBC is technically “no longer part of the spec”

   - Chapter 22 doesn’t exist. Chapter 22 never existed.

## Slide 63

##### **EBC - EFI Byte Code If EBC is a dead ISA with little to no reference implementations why are you talking about it now?**

- What if there were legacy/deprecated features lingering in a codebase for years…

- What if IBVs/OEMs were slow to patch platform firmware and remove legacy/deprecated features…

- EBC interpreter is still part of the main branch in Tianocore’s edk2

- IBVs/OEMs fork edk2, along with the EBC interpreter…

   - … then a lot of machines might have the EBC interpreter, and can run EBC binaries

- Just because this feature is hardly (if ever) used, doesn’t mean it can’t be leveraged

- To be continued… [ongoing project, updates to be presented at REcon 2024 and in VX-Underground Black Mass, vol. 2]

## Slide 64

##### **UEFI generation 3: EBC RE and development tools**

- Open-source version of the EBC compiler: fasm-ebc <u>https://github.com/pbatard/fasmg-ebc</u>

- Hex editor (xxd, hexdump)

- ebcvm: https://github.com/yabits/ebcvm

• Ghidra with efSeek i and ghidra-firmware-utils and an EBC plugin: • <u>https://github.com/meromwolff/Ghidra-EFI-Byte-Code-Processor/</u>

## Slide 65

UEFI Exploit Dev

## Slide 66

Source: Vincent Zimmer, “EFI Byte Code,” Saturday, August 1, 2015, https://vzimmer.blogspot.com/2015/08/efi-byte-code.html

## Slide 67

##### **UEFI Exploit dev**

###### **Well, how did I get here?**

- My research on this began after I kept running into the same problem at work: I was *finding* UEFI vulnerabilities, but I didn’t know how to write exploits for UEFI

- This talk is an overview of my experience learning UEFI exploit dev; it’s ongoing, I welcome feedback. [If you work in or do research in this space, please come talk to me afterwards. I’m here to learn just like all of you.]

- How did I learn to write UEFI exploits?

   - 1. Reverse engineering and replicating the techniques of other PoCs [Translating PoC’s, if you will]

   - 2. Learning about UEFI by writing UEFI apps and drivers [How do you learn a language? How do you learn to write UEFI exploits? Exploit dev is like learning a language: it requires practice and accepting that you’ll fail many times before you communicate what you want to say (e.g. pwn a target)]

## Slide 68

**SMM Callout Exploit dev Reverse Engineering earlier malware/PoCs**

• How does one start writing an exploit for a new system/an unfamiliar target?

- Understand the target:

   - Build foundational knowledge (RTFM - the UEFI spec, Beyond BIOS, Rootkits and Bootkits)

   - • Find previous notable work in UEFI exploit development/malware, and read, re-read the base text

   - “Translate a base text” : Try to translate the same exploit technique on a different vulnerable target

• e.g. Use cr4sh’s SMM callout PoC for a vulnerability in SystemSmmAhciAspiLegacyRt [“Exploiting SMM callout vulnerabilities in Lenovo firmware”, http://blog.cr4.sh/2016/02/ <u>exploiting-smm-callout-vulnerabilities.html ], as a template for writing an SMM callout</u> exploit for a vulnerability in an IdeBusDxe driver

## Slide 69

**UEFI Exploit dev Reverse Engineering earlier malware/PoCs** • There is no ROP Emporium for UEFI specifically, and there are very few examples of UEFI-specific CTF challenges [Notable exception: SMM Cowsay from UIUCTF 2022, which we’ll return to] that you can use for practice • But there are good resources for learning all of the skills you’ll need to write UEFI exploits

• No exploit dev roadmap? Honey, that’s what I call a make-your-own-adventure CTF

## Slide 70

##### **UEFI Exploit dev Make-your-own-adventure CTF**

• (OST2) Architecture 4021: Introductory UEFI <u>https://ost2.fyi/Arch4021</u>

• (OST2)  Architecture 4001: x86-64 Intel Firmware Attack & Defense <u>https://ost2.fyi/Arch4001</u>

• (OST2) Hardware 1101: Intel SPI Analysis <u>https://ost2.fyi/HW1101</u>

• UEFI-Lessons by Kostr: https://github.com/Kostr/UEFI-Lessons/

- Tools

   - Chipsec: https://chipsec.github.io/

• UEFITool: https://github.com/LongSoft/UEFITool

## Slide 71

**UEFI Exploit dev: SMM Callouts Started from ring -2 now we’re calling out to an attackercontrolled region of memory**

## Slide 72

**SMM Callout ?????**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
EFI_LSTATUS _ fastcall ChildSwSmiHandler(
2 EFI_HANDLE DispatchHandle,
const void *Context,
char *CommBuffer, rs | '@) U
?
UINTN *CommBuf ferSize)
i ay
EFI_STATUS v5; // rbx ' ?? :
EFI_STATUS v6; // rax
UINTN v7; // rbx
EFI_STATUS result; // rax
INTN v9; // rsi
EFI_STATUS v1@; // ri2
EFI_HANDLE Buffer; // [rsp+3@h] [rbp-4@h] BYREF
UINTN BufferSize; // [rsp+38h] [rbp-38h] BYREF
UINTN NoHandles; // [rsp+4@h] [rbp-3@h] BYREF
EFI_LOADED_IMAGE PROTOCOL *EfilLoadedImageProtocol; // [rsp+48h] [rbp-28h] BYREF
EFI_ACPI_SUPPORT_PROTOCOL *EfiAcpiSupportProtocol; // [rsp+5@h] [rbp-20h] BYREF
void *Table; // [rsp+S8h] [rbp-18h] BYREF
UINTN Handle[2]; // [rsp+6@h] [rbp-10h] BYREF
EFI_ACPI_TABLE_VERSION Version; // [rsp+A@h] [rbp+30h] BYREF
if ( !CommBuffer || !CommBufferSize )
return 0164;
if ( *(_DWORD *)CommBuffer == 1 )
{
Buffer = 0164;
if ( gBS->LocateHandleBuffer(ByProtocol, &EFI_ATA_PASS THRU_PROTOCOL_GUID, @i164, &NoHandles, (EFI_HANDLE **)&Buffer)
{
v5 = @x8eeee2220000000E 164;
?
O000013Al ChildSwSmiHandler:27 (13Al)
```

## Slide 73

##### **UEFI Exploit dev: SMM Callouts Started from ring -2 now we’re calling out to an attacker-controlled region of memory**

- So… you found an SMM callout vulnerability in a combined SMM/DXE driver. Now what?

- Well… How does an exploit for an SMM callout work?

   - What process is it disrupting or manipulating or interfering with?

   - What is the starting state of the UEFI firmware’s environment before and after a successful SMM callout exploit?

- What are the critical data structures to know?

   - SMRAM

   - EFI Boot Services Table & EFI Runtime Services Table

   - EFI System Table

   - SMMC

## Slide 74

##### **SMM (System Management Mode)**

###### **Overview**

- The most privileged x86 processor mode — ring -2 [we’re going to ignore ME, but yes that’s ring -3, good job]

- The processor enters SMM only when a System Management Interrupt (SMI) is invoked

- SMIs have the highest priority of all interrupts — higher priority than NMIs (nonmaskable interrupts) and MIs (maskable interrupts)

- SMM is meant to act as a privileged and *separate* (read isolated) processor mode for handling critical system functionality that needs to proceed uninterrupted (i.e. power management, etc.)

- SMM code and data reside in SMRAM

## Slide 75

###### **SMM (System Management Mode)**

###### **SMRAM**

- SMM code and data (meaning SMI handler code and data) is stored in SMRAM

- SMRAM = a protected region of a processor’s address space, dedicated to storing SMM code and data

- SMRAM is locked (or it should be) during Platform Initialization (PI), so that SMM code and data in SMRAM are not accessible by code outside of SMRAM

How do we invoke an SMI if SMI Handler code is in SMRAM and SMRAM is a theoretically protected region of memory? How can we invoke an SMI handler with necessary arguments  if we’re outside of SMRAM?

   - SMRAM code should not be reachable by code running in kernel space or userspace

- Entering SMM is triggered by an SMI, which includes *saving execution context of code running outside of SMRAM*

###### Image credit:

- After execution of SMI handler code, RSM instruction triggers the restoration of the initial saved state

"Through the SMM Class and a Vulnerability Found There." Bruno Pujos, January 14, 2020, Synactiv <u>https://www.synacktiv.com/en/publications/through-the-smm-class-and-avulnerability-found-there.html</u>

## Slide 76

###### **SMM (System Management Mode)**

###### **The Communication Buf f** **er**

- SMM_Core_Private_Data structure:

   - Used as a shared buffer for data during communication between SMRAM/non-SMRAM

   - Easily identifiable by “smmc” signature in memory

- EFI_SMM_Communicate Protocol requires that the Smm Communicate Buffer has the following structure:

   - GUID of SmiHandler you want to communicate with

- The size of the data you’re sending to the SMI handler

- The data

Source: “A Tour Beyond BIOS Secure SMM Communication in the EFI Developer Kit II” Jiewen Yao, Vincent J. Zimmer, Star Zeng, Intel,  April 26, 2016

## Slide 77

##### **SMM Callouts**

###### **How**

- When code running in SMM (so SMI handler code) reaches out to a data structure/code located _outside_ of SMRAM, an SMM callout vuln can arise

- SMRAM == **safe** (relatively)

- EFI_BOOT_SERVICES and EFI_RUNTIME_SERVIES == data structures that are located outside of SMRAM

- Code in either of these data structures can be attacker controlled!

Source: “A New Class of Vulnerabilities in SMI Handlers,” Figure 1 – Schematic overview of an SMM callout, source: CanSecWest 2015

## Slide 78

##### **SMM Callouts why should I care?**

- A successful SMM exploit could allow an attacker arbitrary code execution within the most privileged execution level (ring -2) of the OS

• Ring -2 code execution would effectively bypass security protections at all other execution levels and allow an attacker to install a persistent malicious firmware backdoor or implant.

Source: “A New Class of Vulnerabilities in SMI Handlers,” Figure 1 – Schematic overview of an SMM callout, source: CanSecWest 2015

## Slide 79

SwSmi Handler executing code in SMRAM

# **SMM Callout**

###### **IdeBusDxe**

**[instance of the IdeBusDxe vulnerability reported by Binarly** **<u>BRLY-2021-020 CVE-2021-45970]</u>**

Necessary conditions for callout: CommBuffer != NULL CommBufferSize != NULL first DWORD of CommBuffer == 1 SwSmi Handler calling out to function in *attacker-controlled* EFI_BOOT_SERVICES table

## Slide 80

# **SMM Callout**

###### **qemu & gdb**

Hell yeah

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
EFI_STATUS _ fastcall ChildSwSmiHandler(
EFI_HANDLE DispatchHandle,
const void “Context,
char *CommBuffer,
UINTN *CommBuf ferSize)
6 i rr
EFI_STATUS v5; // rbx
EFI_STATUS v6; // rax
UINTN v7; // rbx
EFI_STATUS result; // rax
INTN v9; // rsi
EFI_STATUS v1@; // ri2
EFI_HANDLE Buffer; // [rsp+3@h] [rbp-4@h] BYREF
UINTN BufferSize; // [rsp+38h] [rbp-38h] BYREF
UINTN NoHandles; // [rsp+4@h] [rbp-3@h] BYREF
EFI_LOADED_IMAGE_ PROTOCOL *EfiloadedImageProtocol; // [rsp+48h] [rbp-28h] BYREF
EFI_ACPI_SUPPORT_PROTOCOL *EfiAcpiSupportProtocol; // [rsp+5@h] [rbp-20h] BYREF
void *Table; // [rsp+S8h] [rbp-18h] BYREF
UINTN Handle[2]; // [rsp+6@h] [rbp-1@h] BYREF
EFI_ACPI_TABLE_VERSION Version; // [rsp+A@h] [rbp+3@h] BYREF
if ( !CommBuffer || !CommBufferSize )
return 0164;
if ( *(_DWORD *)CommBuffer == 1 )
if
Buffer = 0164;
if ( gBS->LocateHandleBuffer(ByProtocol, &EFI_ATA_PASS THRU PROTOCOL GUID, @i64, &NoHandles, (EFI_HANDLE **)&Buffer)
{
v5 = @x8eeeeeeReR00000EUI64;
+
000013Al ChildSwSmiHandler-27 (13Al) |
```

## Slide 81

**SMM callout exploit dev Methodology overview, v.1 Adapted from base text: “Exploiting SMM callout vulnerabilities in Lenovo firmware” by cr4sh** Since SMI Handler is making a call *out* of SMRAM to a function in this data structure -- EFI_BOOT_SERVICES -- and EFI_BOOT_SERVICES can be attacker-controlled, an attacker would need to do the following to exploit this SMM callout and achieve arbitrary code execution in ring -2.

1. Identify the location of the EFI_BOOT_SERVICES data structure in memory

2. Determine the SW SMI which triggers the execution of the callout in vulnerable driver

3. Allocate space for shellcode in memory + save address of shellcode for use in step 4 4. Set the address of the LocateHandleBuffer function within the EFI_BOOT_SERVICES table to point to the address of shellcode (overwrite function pointer of LocateHandleBuffer to redirect code flow)

5. Trigger the SW SMI using the identified SW SMI number identified in step 2.

6. Attacker shellcode is executed in ring -2

## Slide 82

**SMM Callout exploit v. 1**

## Slide 83

##### **SMM Callout v.1**

###### **Chipsec**

- Back to the drawing board

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
SMM Callout v.1
Chipsec
¢ Back to the drawing board
<> ¢
=O
<> Code
ARM
&s github.com/chipsec/chipsec/issues/461
chipsec / chipsec Q Type (J) to search
© Issues 52 3] Pullrequests 6 ) Discussions ©) Actions [Fj Projects 3 © wiki © Sec
support? #461
-©open ismaws opened this issue on Oct 20, 2018 - 4 comments
ismaws commented on Oct 20, 2018 200
This is not an issue, more of a future-release / other tools question:
Does chipsec have any plans to support non-intel architectures?
Are there any other tools specific to check secure cfg or AMD/ARM architectures? also, are there other tools that
complement chipsec in its current scope?
©
ErikBjorge commented on Oct 20, 2018 Member) **°
We do have plans for adding the ability to test other architectures to CHIPSEC. Part of this will require restructuring the
driver and configuration file layout and updating the detection process. We also need a simple method for tagging
modules so they run only under the appropriate configurations. | am sure we will find other issues as we start to add
these features.
If you would like we can discuss potential changes in this issue for now. At some point we may need to track
plan/progress on the wiki or some other location.
©
```

## Slide 84

**UEFI Exploit dev: SMM Callouts Started from ring -2 now we’re calling out to an attacker-controlled region of memory ~*There are no binary exploitation mitigations present in the vulnerable SMM/ DXE driver but Chipsec won’t run on the host machine so now we’re reversing the swsmi function in Chipsec and replicating its functionality in C *~**

## Slide 85

##### **SMM callout exploit dev**

###### **Methodology overview, v.2**

Since SMI Handler is making a call *out* of SMRAM to a function in this data structure -- EFI_BOOT_SERVICES -- and EFI_BOOT_SERVICES can be attacker-controlled, an attacker would need to do the following to exploit this SMM callout and achieve arbitrary code execution in ring -2.

1. Identify the location of the EFI_BOOT_SERVICES data structure in memory

2. Determine the SW SMI which triggers the execution of the callout in vulnerable driver

3. Allocate space for shellcode in memory + save address of shellcode for use in step 4

4. Set the address of the LocateHandleBuffer function within the EFI_BOOT_SERVICES table to point to the address of shellcode (overwrite function pointer of LocateHandleBuffer to redirect code flow)

5. Trigger the SW SMI using the identified SW SMI number identified in step 2.

- A. Set up communication buffer

- B. SmmCommunicate()

C. Write to I/O ports 0xb2 and 0xb3

6. Attacker shellcode is executed in ring -2

## Slide 86

###### **SMM Callout v. 2 Chipsec? Never heard of her.**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
[FS8=\> Load SmmCal lLoutDriver.efi
Locate Handle Buffer address: @90000007EED@110 SMM Callout v.2
Locate Handle Buffer offset: 800000007EED0108
EFI SYSTEM TABLE pointer address: 7E5EC018 Chipsec? Never heard of her.
EFI BOOT SERVICES TABLE pointer address is: 7EEF6F68
EFI_LOADED_IMAGE_PROTOCOL pointer address is: 7EED@116
Found Runtime Data address range in memory map: 880880807E4ED800 - BBGB80807E5EDE00 of size BaBBBRR800100000
Found Runtime Code address range in memory map: 888808007E5ED808 - BBBBBGB07E6ED808 of size BBBBBRBRR0100000
potential smmc found at: 7E6CB148
potential smmc found at: 7E6CB148
Testing smmc_loc value, found at: 7E6CB148
Yulnerable gBS function pointer LocateHandleBuffer is at: 7EEF7@98
Testing ... confirming gBS function pointer LocateHandleBuffer is at: 7EEF7@98
Yulnerable gBS LocateHandleBuffer function handler is at: 7EED7@AF
Size of shellcode sggg8gg800000091
shellcode address: 7EED@143
alt shellcode address: 880088807EED@BE8
SMM Base2 protocol is located at 7E6CBGE8
SMM communication protocol is located at 7E6CB4a8
```

## Slide 87

###### **UEFI Exploit dev: SMM Callouts** **where’s my exploit uWu**

- I found this vulnerability on a time-boxed pentesting engagement at work

- I wrote my first two versions of the PoC and was ready to try it

- On the last day of testing, the other consultants on my team found a vulnerability and successfully exploited it!

- … which ended up bricking the device.

- • So while the client was happy and we delivered high-impact findings, I wrote a PoC that I haven’t tested yet on real hardware. More importantly, I don’t have a demo video

## Slide 88

###### **SMM Callout v. 2 Chipsec? Never heard of her.**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
[FS@=\%> Load SmmCal LoutDriver.efi S C
Locate Handle Buffer address: 880008807EED0118 MM allout V. 2
Locate Handle Buffer offset: S80808007EEDR108
EFI SYSTEM TABLE pointer address: 7E5EC@18 Chipsec? Never heard of her.
EFI BOOT SERVICES TABLE pointer address is: 7EEF6F60
EFI_LOADED_IMAGE_PROTOCOL pointer address is: 7EED@118
Found Runtime Data address range in memory map: @8@0880007E4EDR00 - BBBBB8B07E5EDR00 of size BaRRBRRBRRR100000
Found Runtime Code address range in memory map: B60800007E5ED80G - BBBBB8B87E6EDRG8 of size BaBRBBRRR0100000
potential smmc found at: 7E6CB14a
potential smmc found at: 7E6CB148
Testing smmc_loc value, found at: 7E6CB14a
Vulnerable gBS function pointer LocateHandleBuffer is at: 7EEF7898
Testing ... confirming gBS function pointer LocateHandleBuffer is at: 7EEF7@98
Vulnerable gBS LocateHandleBuffer function handler is at: 7EED?@AF
Size of shellcode sagg880000000091
shellcode address: 7EED@143
alt shellcode address: 880088080 7EED@BE8
SMM Base2 protocol is located at 7E6CBG@Ea
SMM communication protocol is Located at 7E6CB480
A4llocatePool for Smm Comm Buffer successful, located at: 7E5B5018
Testing sim_comm_buffer_offset address: 7E6CB176
Testing smm_comm_buffer_sz_offset address: 7E6CB188
comm buffer data is located at address: 7EED@aCC
SmmComm Communicate call returned status: 6x@G8088GF DataSize is: 1C
Testing ... confirming gBS function pointer LocateHandleBuffer now points to shellcode at: 7EED@143
Testing ... confirming gBS function pointer LocateHandleBuffer now points to shellcode at: 7EED@143
Testing ... confirming gBS function pointer LocateHandleBuffer again points to original address of LocateHandleBuffer(} function at: 7EED7@AF
Image 'FS8:\SmmCalloutDriver.efi' error in StartImage: Access Denied
```

## Slide 89

###### **UEFI Exploit dev: SMM Callouts**

###### **where’s my exploit uWu**

- This vulnerability is also present in Fujitsu Lifebook e449/e459, version

   - Possibly viable option for hardware testing?

   - Only available option for acquiring the device promptly was on Craigslist…

- However, the exploit I wrote initially was for a relatively simple case

- There were none of the typical mitigations that make SMM callout vulnerabilities more difficult to exploit (though not dramatically so), e.g. SMM_CODE_CHK_EN

## Slide 90

###### **UEFI Exploit dev: SMM Callouts** **where’s my exploit uWu**

- This vulnerability is also present in Fujitsu Lifebook e449/e459, version

   - Possibly viable option for hardware testing?

   - Only available option for acquiring the device promptly was on Craigslist…

- However, the exploit I wrote initially was for a relatively simple case

- There were none of the typical mitigations that make SMM callout vulnerabilities more difficult to exploit (though not dramatically so), e.g. SMM_CODE_CHK_EN

## Slide 91

**UEFI Exploit dev Make-your-own-adventure CTF continued**

- While testing and demo-ing the PoC on real hardware was not realistically feasible, there is that one CTF challenge I mentioned…

- SMM Cowsay parts 1, 2 and 3 from UIUCTF 2022: [archived 2022 CTF]: https://2022.uiuc.tf/challenges

- [Shoutout to the author of this challenge, Yifei Zhu (@zhuyifei1999 on GitHub)]: This CTF challenge has 3 levels of difficulty

- SMM Cowsay I: has 0 SMM exploit mitigations applied

- SMM Cowsay II: 1 mitigation

- SMM Cowsay III: 2 mitigations (ASLR and SMM_CODE_CHK_EN)

## Slide 92

##### **UEFI Exploit dev: SMM Callouts Mitigations: SMM_CODE_CHK_EN**

- SMM_CODE_CHK_EN: SMM Callout mitigation that aims to prevent SMM Callouts • If SMM_CODE_CHK_EN is enabled, then SMM code must be located within ranges defined by SMRR (System-Management Range Register); if SMM code is executed outside of this range, unrecoverable exception is triggered

- Recall: Entering SMM is triggered by an SMI, which includes *saving execution context of code running outside of SMRAM*

- After execution of SMI handler code, RSM instruction triggers the restoration of the initial saved state

- What if we just… polluted the SMI save state with a ROP chain and bypassed SMM_CODE_CHK_EN?

## Slide 93

##### **UEFI Exploit dev: SMM Callouts Mitigations: SMM_CODE_CHK_EN**

- **Requires building a ROP chain and calculating SMBASE**

- Run ropper on your target UEFI driver, find some gadgets, build your exploit

- A few resources on bypassing SMM_CODE_CHK_EN with ROP:

   - Binarly: “The Dark Side of UEFI: A technical Deep-Dive into Cross-Silicon Exploitation” <u>https://www.binarly.io/blog/the-dark-side-of-uefi-a-technical-deep-dive-into-cross-siliconexploitation</u>

   - Syntactiv: “Code Checkmate in SMM” by Bruno Pujos: https://www.synacktiv.com/en/publications/ <u>code-checkmate-in-smm</u>

   - cr4sh: “Exploiting AMI Aptio firmware on example of Intel NUC” <u>http://blog.cr4.sh/2016/10/exploiting-ami-aptio-firmware.html</u>

   - Many more examples

## Slide 94

##### **UEFI Exploit Dev**

###### **tips + tricks**

- It's helpful to think about UEFI as a separate ecosystem between the OS and onboard (i.e. SPI flash chip-resident) firmware. It operates like an intermediary OS in and of itself. Thus, in order to write effective UEFI-targeting exploits, we have to understand how to manipulate data structures within UEFI.

- The offsets of data structures in UEFI are consistent, so if we know which data structure + protocol we want to target, we can write a test program to find those offsets, then define them with macros in our final exploit • e.g. BootServices-> HandleProtocol is at offset 0x98 in the EFI_BOOT_SERVICES table

- We will have easy access to data structures right away:

- e.g. on x64, EFI_SYSTEM_TABLE * is in RDX and EFI_IMAGE_HANDLE is in RCX upon program invocation

- • We can also target other data structures/protocols (i.e. EFI_FILE_PROTOCOL for file operations, EFI_SIMPLE_FILESYSTEM_PROTOCOL for filesystem operations, etc.) to hook/inject our payload

- Binary exploit mitigations (i.e. ASLR, stack canaries, etc.) are not used consistently in UEFI firmware implementations (sometimes not even at all), so once you understand the UEFI ecosystem (even vaguely) then writing exploits is pretty straightforward

## Slide 95

##### **Challenges/hurdles for UEFI Exploit Dev Honey, you bricked the machine.**

- The edk2 build system and I have a blood feud

- QEMU and the Sisyphean task of UEFI firmware testing/debugging in emulators

- Chipsec does not work on M-series Mac machines, so the de-facto platform firmware testing framework both doesn’t work on architectures and can’t be used for testing/developing exploits for other architectures

- Debugging on real hardware has its own challenges:

   - It can be cost-prohibitive — you will brick machines, you will break things. That’s how these things go.

   - Documentation may not be available for the architecture you want to target (i.e. arm64 or EBC)

## Slide 96

**UEFI Exploit Dev is amazing and here’s why I love UEFI it’s my favorite**

- Exploit mitigations that are common on modern OSes (i.e. ASLR, DEP, stack canaries, etc.) aren’t always implemented or implemented fully on UEFI BIOS firmwares

- • If binary exploit mitigations are applied, bypass techniques aren’t unfamiliar (i.e. ROP/ JOP chains for bypassing SMM Code_Check_En)

- UEFI is a complex ecosystem -> error-prone and incomplete coverage of applied protections

- UEFI is so expansive and unexplored that it offers an environment for creativity in research and exploit development

• Firmware + hardware + low-level exploit dev + cross-architecture exploits == <3

## Slide 97

“Just as fragments of a vessel, in order to be fitted together, must correspond to each other in the tiniest details but need not resemble each other, so translation, instead of making itself resemble the meaning of the original, must lovingly, and in detail, fashion in its own language a counterpart to the original's mode of intention, in order to make both of them recognizable as fragments of a vessel, as fragments of a greater language.” Walter Benjamin, “The Task of the Translator,” translated by Steven Rendall, page 161.

## Slide 98

**Q & A**

## Slide 99

##### **UEFI Exploitation/Research Resources**

“Low Level PC/Server Attack & Defense Timeline,” By @XenoKovah of @DarkMentorLLC <u>https://darkmentor.com/timeline.html</u>

“Debugging System with DCI and Windbg,” Satoshi Tanda, 29 March 2021, <u>https://standa-note.blogspot.com/2021/03/debugging-system-with-dci-and-windbg.html</u>

"How Many Million BIOSes would You Like to Infect?" Xeno Kovah & Corey Kallenberg, LegbaCore, http:// <u>legbacore.com/Research_files/HowManyMillionBIOSWouldYouLikeToInfect_Full2.pdf</u> “Leaked Intel Boot Guard keys: What happened? How does it affect the software supply chain?” Binarly Team, Binarly, 9 November 2022, <u>https://www.binarly.io/blog/leaked-intel-boot-guard-keys-what-happened-how-does-it-affect-the-software-supplychain</u>

“Breaking through another Side: Bypassing Firmware Security Boundaries,” Alex Matrosov, Binarly, 14 July 2021, <u>https://www.binarly.io/blog/breaking-through-another-sidebypassing-frmwarei</u> -security-boundaries

## Slide 100

##### **UEFI Exploitation/Research Resources**

“Now You See It... TOCTOU Attacks Against BootGuard,” Peter Bosch & Trammell Hudson, HackInTheBox Conference 2019, <u>https://conference.hitb.org/hitbsecconf2019ams/materials/D1T1%20%20Toctou%20Attacks%20Against%20Secure%20Boot%20-%20Trammell%20Hudson%20&%20Peter%20Bosch.pdf</u>

“Who Watches BIOS Watchers?” Alex Matrosov, Binarly, 12 July 2021, <u>https://www.binarly.io/blog/who-watches-bios-watchers</u> “Firmware is the new Black — Analyzing Past 3 years of BIOS/UEFI Security Vulnerabilities” Bruce Monroe & Rodrigo Rubira Branco & Vincent Zimmer, BlackHat USA 2017, <u>https://github.com/rrbranco/BlackHat2017/blob/master/BlackHat2017-BlackBIOS-v0.13-Published.pdf</u>

“The Keys to the Kingdom and the Intel Boot Process,” Eclypsium Blog, 28 June 2023, Eclypsium, <u>https://eclypsium.com/blog/the-keys-to-the-kingdom-and-the-intel-boot-process/</u>

“BootGuard,” Trammell Hudson, 8 November 2020, <u>https://trmm.net/Bootguard/</u>

## Slide 101

**UEFI Exploitation/Research Resources** “Safeguarding rootkits: Intel BIOS Guard,” Alexander Ermolov, Zero Nights, <u>https://github.com/fothrone/bootguard/blob/master/Intel%20BootGuard%20fl</u> inal.pdf

“Securing the Boot Process: The hardware root of trust,” Jessie Frazelle, 2019 <u>https://dl.acm.org/doi/fullHtml/10.1145/3380774.3382016</u>

“CPUMicrocodes: Intel, AMD, VIA & Freescale CPU Microcode Repositories,” platomav, GitHub <u>https://github.com/platomav/CPUMicrocodes</u> “Breaking Firmware Trust from Pre-EFI: Exploiting Early Boot Phases,” Binarly, BlackHat USA 2022, <u>https://www.youtube.com/watch?v=Z81s7UIiwmI</u>

## Slide 102

##### **ARM UEFI Exploitation/Research Resources**

“Attacking the ARM’s TrustZone,” Joffrey Gibson, QuarksLab, 31 July 2018, <u>https://blog.quarkslab.com/attacking-the-arms-trustzone.html</u> “Introduction to Trusted Execution Environment: ARM's TrustZone,” Joffrey Gibson, QuarksLab, 19 June 2018, <u>https://blog.quarkslab.com/introduction-to-trusted-execution-environment-arms-trustzone.html</u> “The Dark Side of UEFI: A technical Deep-Dive into Cross-Silicon Exploitation Binarly efiXplorer Team, Binarly, 8 February 2024, <u>https://www.binarly.io/blog/the-dark-side-of-uefi-a-technical-deep-dive-into-cross-silicon-exploitation</u>

“Multiple Vulnerabilities in Qualcomm and Lenovo ARM-based Devices,” Binarly Team, Binarly, 9 January 2023, <u>https://www.binarly.io/blog/multiple-vulnerabilities-in-qualcomm-and-lenovo-arm-based-devices</u>

## Slide 103

##### **UEFI Exploitation/Research Resources**

"Moving From Common Sense Knowledge about UEFI To Actually Dumping UEFI Firmware," Assaf Carlsbad, Sentinel One, <u>https://www.sentinelone.com/labs/moving-from-common-sense-knowledge-about-uefi-to-actually-dumping-uefi-frmware/ i</u>

"Moving From Manual Reverse Engineering of UEFI Modules To Dynamic Emulation of UEFI Firmware," Assaf Carlsbad, Sentinel One, <u>https://www.sentinelone.com/labs/moving-from-manual-reverse-engineering-of-uefi-modules-to-dynamic-emulation-ofuefi-frmware/ i</u>

"Moving From Dynamic Emulation of UEFI Modules To Coverage-Guided Fuzzing of UEFI Firmware" Assaf Carlsbad, Sentinel One, <u>https://www.sentinelone.com/labs/moving-from-dynamic-emulation-of-uefi-modules-to-coverage-guided-fuzzing-of-uefifirmware/</u>

"Adventures From UEFI Land: the Hunt For the S3 Boot Script," Assaf Carlsbad, Sentinel One, <u>https://www.sentinelone.com/labs/adventures-from-uefi-land-the-hunt-for-the-s3-boot-script/</u>

## Slide 104

##### **SMM Callout resources “Exploiting SMM callout vulnerabilities in Lenovo frmwarei ” by cr4sh**

**“Building reliable SMM backdoor for UEFI based platforms” by cr4sh,** **<u>http://blog.cr4.sh/2015/07/building-reliable-smm-backdoor-for-uefi.html</u>** "Code Check(mate) in SMM." Bruno Pujos, January 14, 2020, Synactiv, <u>https://www.synacktiv.com/en/publications/code-checkmate-in-smm.html</u> "Through the SMM Class and a Vulnerability Found There." Bruno Pujos, January 14, 2020, Synactiv, <u>https://www.synacktiv.com/en/publications/through-the-smm-class-and-a-vulnerability-foundthere.html</u>

"Another Brick in the Wall: Uncovering SMM Vulnerabilities in HP Firmware," Assaf Carlsbad, Sentinel One,

<u>https://www.sentinelone.com/labs/another-brick-in-the-wall-uncovering-smm-vulnerabilities-in-hpfirmware/</u>

## Slide 105

##### **SMM Callout resources**

“SmmExploit,” tandasat, GitHub, <u>https://github.com/tandasat/SmmExploit</u>

“SmmExploit - FindSystemManagementServiceTable” tandasat, GitHub, <u>https://github.com/tandasat/SmmExploit/blob/main/Demo/Demo/FindSystemManagementServiceTable.cpp</u>

“PiSmmCore: SMM Core global variable for SMM System Table (SMST) Only accessed as a physical structure in SMRAM,” tianocore, edk2, GitHub, <u>https://github.com/tianocore/edk2/blob/stable/202011/MdeModulePkg/Core/PiSmmCore/PiSmmCore.c#L19</u>

“MdeModulePkg: PiSmmIpl,” tianocore, edk2, GitHub, <u>https://github.com/tianocore/edk2/blob/stable/202011/MdeModulePkg/Core/PiSmmCore/PiSmmIpl.c</u> “Platform Runtime Mechanism,” version 1.0, UEFI, November 2020, <u>https://uefi.org/sites/default/fles/resources/Platform%20Runtime%20Mechanism%20i</u> -%20with%20legal%20notice.pdf

“Platform Runtime Mechanism,” tianocore, edk2-staging repository, GitHub, <u>https://github.com/tianocore/edk2-staging/tree/PlatformRuntimeMechanism</u>

## Slide 106

##### **SMM Callout resources**

**"Advanced x86: BIOS and System Management Mode Internals, Day 7, System Management Mode (SMM)," Xeno Kovah & Corey Kallenberg, LegbaCore,** **<u>https://opensecuritytraining.info/IntroBIOS_files/Day1_07_Advanced%20x86%20-%20BIOS%20and%20SMM%20Internals%20%20SMM.pdf</u>**

"Advanced x86: BIOS and System Management Mode Internals , Day 8, SMRAM (System Management RAM)," Xeno Kovah & Corey Kallenberg, LegbaCore, <u>https://opensecuritytraining.info/IntroBIOS_files/Day1_08_Advanced%20x86%20-%20BIOS%20and%20SMM%20Internals%20%20SMRAM.pdf</u>

"Advanced x86: BIOS and System Management Mode Internals , Day 8, SMRAM (System Management RAM)," Xeno Kovah & Corey Kallenberg, LegbaCore, <u>https://opensecuritytraining.info/IntroBIOS_files/Day1_09_Advanced%20x86%20-%20BIOS%20and%20SMM%20Internals%20%20SMM%20and%20Caching.pdf</u>

"Advanced x86: BIOS and System Management Mode Internals, Day 10, More Fun with SMM," Xeno Kovah & Corey Kallenberg, LegbaCore, <u>https://opensecuritytraining.info/IntroBIOS_files/Day1_10_Advanced%20x86%20-%20BIOS%20and%20SMM%20Internals%20%20Other%20Fun%20with%20SMM.pdf</u>

"Advanced x86: BIOS and System Management Mode Internals, Day 11, SMM Conclusion," Xeno Kovah & Corey Kallenberg, LegbaCore, <u>https://opensecuritytraining.info/IntroBIOS_files/Day1_11_Advanced%20x86%20-%20BIOS%20and%20SMM%20Internals%20%20SMM%20Conclusion.pdf</u>

## Slide 107

##### **ARM64 UEFI Resources**

“Arm SystemReady and the UEFI Firmware Ecosystem,” Dong Wei (Arm) Samer El-Haj-Mahmoud (Arm), UEFI 2021 Virtual Plugfest, January 26, 2021 “Arm SystemReady Compliance Program,” ARM, <u>https://www.arm.com/architecture/system-architectures/systemready-certifcationi</u> -program “ARM Developer docs: UEFI,” ARM Developer, <u>https://developer.arm.com/Architectures/Unifed%20Extensible%20Firmware%20Interface i</u> “ARM Management Mode Interface Specification System Software on ARM,” ARM Developer, <u>https://developer.arm.com/documentation/den0060/a/?lang=en</u> “Base Boot Security Requirements 1.3,” ARM Developer, <u>https://developer.arm.com/documentation/den0107/latest</u> “Porting a PCI driver to ARM AArch64 platforms”, Olivier Martin (ARM), UEFI Spring Plugfest – May 18-22, 2015, <u>https://uef.org/sites/default/fi</u> iles/resources/UEFI_Plugfest_May_2015_ARM.pdf “Tailoring TrustZone as SMM Equivalent,” Tony C.S. Lo Senior Manager American Megatrends Inc., UEFI Plugfest March 2018, <u>https://uef.org/sites/default/fi</u> iles/resources/UEFI_Plugfest_March_2016_AMI.pdf

## Slide 108

##### **EBC Resources**

Writing and Debugging Writing and Debugging EBC Drivers EBC Drivers February 27 February 27th 2007, <u>https://uef.org/sites/default/fi</u> iles/resources/EBC_Driver_Presentation.pdf

“EFI Byte Code,” Vincent Zimmer, 1 August 2015, <u>https://vzimmer.blogspot.com/2015/08/efi-byte-code.html</u>

“Fasmg-ebc,” pbatard, GitHub, <u>https://github.com/pbatard/fasmg-ebc/</u>

“Ebcvm,” yabits, Github, <u>https://github.com/yabits/ebcvm/</u>

“Ghidra-EFI-Byte-Code-Processor,” meromwolff, GitHub, <u>https://github.com/meromwolff/Ghidra-EFI-Byte-Code-Processor/</u>

“EBC Compiler,” Ravi Narayanaswamy and Jiang Ning Liu, Intel, 2007, <u>https://uef.org/sites/default/fi</u> iles/resources/EBC_Compiler_Presentation.pdf
