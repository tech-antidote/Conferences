---
title: "Portrait of the artist as a young vx-er This painting is an MBR bootkit"
speakers: ["Nika Korchok Wakulich"]
conference: "REcon"
conference_full: "REcon 2023"
edition: ""
year: 2023
source_pdf: "REcon 2023 Slides/Nika Korchok Wakulich_Portrait of the artist as a young vx-er This painting is an MBR bootkit .pdf"
pages: 46
sha256: "1694da4420b62d74cfd92b93b75aa7151ddaa8cd952a88a90b9fa3ecaa4ecda7"
text_chars: 26559
ocr_pages: 9
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:26:43Z"
---
# Portrait of the artist as a young vx-er This painting is an MBR bootkit

**Speakers:** Nika Korchok Wakulich  
**Conference:** REcon 2023  
**Source:** `REcon 2023 Slides/Nika Korchok Wakulich_Portrait of the artist as a young vx-er This painting is an MBR bootkit .pdf` (46 pages)

## Slide 1

# **`Portrait of the artist as a young vx-er This painting is an MBR bootkit Nika Korchok Wakulich`**

## Slide 2

**DISCLAIMER: The views expressed in this presentation are my own and do not reflect the opinions of my past, present or future employers Viewer Discretion is advised.**

## Slide 3

### **whoami**

**Twitter: @nikaroxanne Discord: @ic3qu33n Mastodon: ic3qu33n@infosec.exchange Website:** **<u>https://ic3qu33n.fyi/</u> GitHub: @nikaroxanne**

**Security Consultant at Leviathan Security Group Reverse engineer + artist I <3 malware, hardware hacking, firmware hacking, skateboarding, learning languages, creating art, writing lil assembly programs, etc.**

**greetz 2 the following for their assistance/support w this talk: Ben Mason (@suidroot), @Laughing_Mantis, Richard Johnson (@richinseattle), the Rootsyn Discord (@qkumba, @phLaul and @barbie), The team at Leviathan REcon**

## Slide 4

##### **Focus of this talk**

- A project focused on creative applications of vx/ malware reverse engineering

- How I reverse engineered 16-bit bootkits targeting systems with a legacy BIOS boot process— specifically focused on bootkits of the 1980s/1990s

- Provides overview of the legacy boot process and several prominent bootkits of that era

- Aims to answer questions including:

- ‘How would you write a bootkit that exists as a work of art and/or how would you use vx techniques to create new art?’

- Why would you do such a thing?

## Slide 5

### **Motivations**

- Test the claim that malware of the 1980s/ 1990s was simple/easy/unsophisticated/ “just about drawing pretty pictures”

   - Conclusively False

   - Different talk covers this in more detail “My Super Sweet 16-Bit Malware: MS- <u>DOS Edition — TSR Remix”</u>

- Study the techniques of vx legends of the 1980s/1990s to create malware art

- Use the unique properties of vx to extend the medium — create new work that lives up to Spanska’s declaration: “Coding a virus can be creative”

“The Young Martyr” by Paul Delaroche

## Slide 6

### **From “the young martyr” to ~*yung m4rtyr *~ Artistic motivations/inspirations:**

- **“The Work of Art in the Age of Mechanical Reproduction” — Walter Benjamin**

- **“Simulacra and Simulation” — Jean Baudrillard**

- **“Tlön, Uqbar, Orbis Tertius” — Jorge Luis Borges**

- **The work of Spanska**

- **The work of Vera Molnar and other groundbreaking artists in computer/digital art**

- **• Many more influences, see References slides and blog posts for more background on my art process**

16-bit painting of a scan of the painting “Young Martyr” by Paul Delaroche,

## Slide 7

##### **Definitions**

• Virus: Fred Cohen (credited as being the “creator” of the term “computer virus” as a way to describe a selfreproducing program, which he used in his 1984 paper “Computer Viruses, Theory and Experiments.” Cohen’s definition was thus: We define a computer 'virus' as a program that can 'infect' other programs by modifying them to include a possibly evolved copy of itself. With the infection property, a virus can spread throughout a computer system or network using the authorizations of every user using it to infect their programs. Every program that gets infected may also act as a virus and thus the infection grows. — Fred Cohen, “Computer Viruses, Theory and Experiments,” 1984

- **Virus** = a self-replicating program that uses a host program to produce those new copies of itself

- vx = “Virus eXchange,” a collection of malware samples; the term “vx” in the 1980s/1990s was also used by communities that grew around vx sites; “vx-er” refers to someone who writes viruses, typically reserved for truly 1337 vx writers

## Slide 8

##### **Definitions**

- **Polymorphic virus = a virus that uses a** **_variable_ encryption/decryption routine and a variable key to create an encrypted copy of itself in memory, which is appended to/inserted into a host file [1]** • **The encrypted image of the virus payload (and the encryption routine of the virus itself) changes with each iteration, so as to avoid/minimize the presence of known byte patterns used in AV signatures**

- **Bootkit = A bootkit is a type of malware that infects a critical component of the OS boot process to install itself and maintain persistence.**

- **Boot sector infector = the earliest form of bootkit; a BSI is a bootkit that targets storage media that did not have an MBR (Master Boot Record), and only had a boot sector (hence the name! Surprise!)** • **BSIs targeted various forms of floppy diskettes, which did not use an MBR**

   - **[1] Page 318-322** "The Giant Black Book of Computer Viruses. Chapter 27: Polymorphic Viruses” Mark Ludwig, 2nd ed., American Eagle Books, 1998.

## Slide 9

# Notable Interrupts for 16-Bit Malware

## Slide 10

###### **Notable Interrupts for MS-DOS Malware**

- <sup>System Interrupts (ROM BIOS):</sup>

   - <sup>Int 10h: Video services</sup>

ROM Bios Interrupts are 05h, and 10h-1Fh

   - **_Int 13h: Disk services_**

   - <sup>Int 16h: Keyboard services</sup>

- <sup>MS-DOS Interrupts:</sup>

   - **_<u>Int 21h - MS-DOS System Functions</u>_**

   - <sup>Int 25h - Absolute Disk Read</sup>

MS-DOS Reserved Interrupts: 20h-3Fh

- <sup>Int 26h - Absolute Disk Write</sup>

## Slide 11

###### **Notable Interrupts for Legacy BIOS Bootkits**

- <sup>System Interrupts (ROM BIOS):</sup>

   - <sup>Int 10h: Video services</sup>

ROM Bios Interrupts are 05h, and 10h-1Fh

   - **_Int 13h: Disk services_**

   - <sup>Int 16h: Keyboard services</sup>

- <sup>MS-DOS Interrupts:</sup>

   - **_<u>Int 21h - MS-DOS System Functions</u>_**

   - <sup>Int 25h - Absolute Disk Read</sup>

   - •<sup>Int 26h - Absolute Disk Write</sup>

In the pre-boot environment, we do not have the OSspecific interrupts available. Our target interrupts are now the ROM BIOS interrupts.

## Slide 12

###### **Interrupt Vector Table Invoking system calls on MS-DOS**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Interrupt Vector Table
System call,
jumps to INT21h IVT entry
IVT[21] | IVT[22] | IVT[23] | IVT [24] eee pecan Aberin
Jump to address of
INT 21h ISR
(retrieved from IVT),
execute ISR
Typical code flow of executing an Interrupt Service Routine
on MS-DOS by invoking a system call
```

## Slide 13

###### **Terminate and Stay Resident Programs [TSRs]**

- <sup>**TSR =  a feature of MS-DOS that allows a user to bypass the limitations of a single-task OS by installing a persistent**</sup> **program in RAM, which would be invoked by subsequent interrupts**

- In order to install a TSR, one had to modify several components of the Interrupt Vector Table, which was the precursor to the Interrupt Descriptor Table, and that defined the addresses of all of the 256 interrupts in 8086 real-mode.

- The basic formula went as follows:

1. Find the address of a desired interrupt in the IVT

2. Retrieve both address components of the target interrupt (“address components” = the original segment and the original offset, because DOS used a segmented addressing scheme)

3. The original interrupt’s address components (segment and offset) are saved to a specific address (i.e. two variables in the data segment or to some other location in memory, defined by the virus writer)

4. A new interrupt handler is installed in the IVT

5. That new interrupt handler’s interrupt routine concludes by jumping back to the original address and passing control back, creating the illusion that the original interrupt has proceeded as per usual

More detailed walk-throughs of TSR techniques are available on my website: <u>https://ic3qu33n.fyi/projects/16bitm4lw4r3-MSDOS/TerminateStayResidentPrograms-part1 https://ic3qu33n.fyi/projects/16bitm4lw4r3-MSDOS/TerminateStayResidentPrograms-part2</u>

## Slide 14

###### **Interrupt Vector Table**

Hooking
system calls
on MS-DOS

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
System call,
jumps to INT21h IVT entry
para hook
TSR INT 21th
hook routine:
checks INT 21h params
for call to
subfunction 4B (EXEC)
VA
\gesion met, jump to new ISR
YY N
Condition not met,
jump to saved address [MSjs)iSj5)
of original INT 21h ISR
&
Jump back to saved address
of original INT 21h ISR
Return to calling function
after execution of ISR chain
Modifying control flow of Interrupt Service Routines by hooking the IVT with a TSR
Interrupt
A (=Yoq Co) am Fz] 0) (=
Hooking
system calls
on MS-DOS
```

## Slide 15

# A Whirlwind Tour of the Legacy BIOS Boot Process

## Slide 16

Legacy BIOS Boot Process

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
BIOS Initialization
CPU begins executing at FO00:FFFO
BIOS initialization (includes setting up the IVT)
ig Legacy BIOS Boot Process
BIOS attempts to retrieve first sector (Track 0, Head 0, Sector 1)
from disk in floppy disk drive A:
Floppy Disk boot process
If disk found in floppy disk drive A:,
read boot sector from (T 0, HO, S 1) | | If no disk found in floppy disk drive A:
into memory at 0x0000:0x7C00
Hard Disk boot
If BIOS check for last two bytes of boot sector == Ox55AA | | If BIOS check for last two bytes of boot sector != Ox55AA || If hard disk present
BIOS attempts to retrieve first sector
(Track 0, Head 0, Sector 1) from disk in hard disk drive C:
If corrupt/invalid MBR
Active partition found in MBR partition table |} No active partition found in MBR partition table
Move/save MBR to fixed location in memory
BIOS attempts to read OS boot sector
from first sector of active partition
(using values of the start and end sectors from MBR partition table entry)
into memory at 0x0000:0x7C00
If successful read of OS boot sector into 0x0000:0x7C00 | | If unsuccessful read of OS boot sector into 0x0000:0x7C00
Final Step in Successful Boot iam
BIOS assumes valid boot sector found;
BIOS transfers control to boot sector
Error Handling in Boot Process
BIOS Boot sector error handling
loaded in memory at 0x00 7C00
```

## Slide 17

### **The Master Boot Record**

- A hard drive has a larger storage capacity than a floppy disk, so it is able to hold multiple different operating systems (up to four) in different partitions

- Partition = as a region of the disk, denoted by a start and an end sector

   - Sectors are defined by a triplet (C, H, S) corresponding to the Cylinder (or Track), Head (or Side) and Sector location of that sector on disk

- The main goal of the MBR code is primarily to read the partition table and load the correct OS partition

## Slide 18

#### **So… you want to be a vx-er? Or “ingredients of a 16-bit legacy BIOS bootkit”**

- A bootkit needs the following:

- A malicious implant targeting some part of the pre-OS boot environment (i.e. MBR infectors — both MBR code infectors and partition table infectors, as well as VBR (Volume Boot Record) and IPL (Initial Program Loader) infectors)

- Technique for going memory resident — on DOS, this was done using a TSR (Terminate and Stay Resident program) that targeted a system interrupt by installing a malicious interrupt handler in the IVT (Interrupt Vector Table)

- Going resident required the virus to allocate adequate space for itself in memory; one of the most common techniques for doing this was manipulating the BIOS Parameter Block (BPB)

- Stealth techniques

   - Saving a copy of the original MBR somewhere on disk (i.e. a sector in a “hidden area” or an unused region of sectors, hiding it in clusters in the FAT and marking those clusters as bad to avoid deletion by OS)

   - Spoofing calls to interrupts that have been hooked by the bootkit to simulate normal system behavior

   - Especially for int 13h, this can include returning the saved copy of the MBR during read requests

   - Polymorphism to avoid AV detection

## Slide 19

**Additional features of legacy BIOS bootkits** • Legacy BIOS bootkits (and legacy BIOS boot code, i.e. MBR code) operate in 16-bit real mode • Legacy BIOS bootkits of the 1980s/1990s had to target different storage media formats (i.e. 360kB floppies, hard drives, etc.) -> had to develop routines for handling as many as possible

## Slide 20

Iconic bootkits

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Sa emcee enna
ie ees mer eres
Iconic bootkits
```

## Slide 21

Brain

## Slide 22

###### **BRAIN**

- The first PC virus, written + released in 1986

- Most accurately described as a Boot Sector Infector (BSI) because it only targeted floppy disks — a storage medium that only held one OS, thus one boot sector

   - Specifically Brain targeted 360kB floppies

- Stealth

   - Saved the original boot sector in a hidden area of the disk

   - Memory residence achieved using INT 13h TSR and stealth achieved by spoofing INT13h calls (i.e. reads/writes returned the saved boot sector)

- See Mikko Hipponen’s documentary “Brain: Searching for the first PC virus in Pakistan”

## Slide 23

Stoned

## Slide 24

###### **STONED**

- Famous bootkit — inspired a range of related bootkits in this virus family, of varying levels of sophistication [Michelangelo, what an absolute flop]

- Able to infect boot sectors of multiple different formats of storage media (routines for both floppy diskettes, and for hard drives)

- Stealth

   - Saved the original MBR on a hidden area of the disk

   - Spoofed valid INT 13h reads/writes with a TSR

- Logic bomb - only displayed the famous “Your PC is now Stoned!” message 1/8 times (using PC timer)

- Other than infecting every drive it came into contact with, Stoned was non-destructive and was — relatively speaking — not too malicious

## Slide 25

###### **STONED**

- Stoned stores the part of its code that performs replication (mainly via the infection and signature test routines which check for an existing installation of the virus on a diskette), in the INT 0x13 handler

- So the int 0x13 handler really is a viral interrupt handler — it ensures successful replication of the virus onto all disks inserted into the machine

- Stoned’s viral ISR only executes when the following two conditions are met:

1. An INT 13h call is made for either a Disk Read or Disk Write operation

2. The drive motor is off

- “The Giant Black Book of Computer Viruses” by Mark Ludwig also includes excellent analysis of key features of Stoned

## Slide 26

###### **STONED**

- Stoned begins simply: it hooks — and installs an interrupt handler for — INT 13h.

- Stoned stores its code in a region of memory by altering the value of a variable in the BIOS Parameter Block (BPB) that holds the number of available 1Kb chunks of memory.

- It does this by reading the value stored there and moving it into a register; decreasing that register value by 2 (new_available_memory = original_available_memory - 2k) and writing this value back to the BPB

- It has now carved out a nice 2Kb free region of memory that it can use.

## Slide 27

16-bit bootkit RE methodology

## Slide 28

###### **16-bit Malware RE Methodology**

- Preliminary research

- Static Analysis:

   - radare2 (I wrote an r2 plugin for automatically identifying interrupts + adding annotations to the disassembly)

   - Cutter (for when I’m too tired to use r2)

   - IDA Free 5.0 (rip 16-bit support </3)

   - Reading the source files (majority of the source files are written in x86 assembly, with syntax specific to a range of assemblers (MASM, TASM, FASM, A86, etc…)

      - Assembling the source using one of the many assemblers

      - … or making modifications to the source for use with a different assembler (NASM); mixed results

- Dynamic Analysis:

   - QEMU + FreeDOS

   - Bochs

   - DosBox (more useful for testing sample programs and performing basic analysis, not as flexible as QEMU+FreeDOS which is better for more involved dynamic analysis)

- *For samples where a compiled binary was not available for dynamic analysis, an auxiliary source of information is danooct1 YouTube channel: <u>https://www.youtube.com/@danooct1</u> Specifically their “MS-DOS malware” playlist: <u>https://youtube.com/playlist?list=PLi_KYBWS_E71ObQ8QpGj5zIDXHREbdWaM</u>

## Slide 29

###### **RE Methodology for 1990s-era bootkits, cont.**

• All of the previous 16-bit vx RE methodology as well as:

- Using my r2 plugin automating analysis/identification of interrupts + adding annotations to the disassembly • The process for developing this r2 plugin was an RE side quest, where the goal was to recreate the IDA 5.0 functionality in an up-to-date tool I like using for RE

rip IDA 5.0 </3

radare2 plugin for auto analysis of 16-bit disassembly of COM files, using Ralf Brown Interrupt List

## Slide 30

###### **RE Methodology for 1990s-era bootkits, cont.**

- All of the previous 16-bit vx RE methodology as well as:

- Using more recent bootkits as a frame of reference

###### • Specifically, the Stoned bootkit… from BlackHat 2012, presentation by Peter Kleissner

[left: radare2 disassembly of Stoned bootkit MBR, featured in “Stoned Bootkit” Black Hat 2012 presentation; right: source code of the Stoned bootkit]

## Slide 31

**RE Methodology for 1990s-era bootkits, cont.** • Rewriting my own viruses/bootkits was a more productive use of time than spending hours correcting syntax or digging through documentation for everyone’s favorite assembler for 1990s vx… TASM

Michaelangelo?? Never heard of her.

## Slide 32

Michelangelo

## Slide 33

###### **MICHAELANGELO**

- “Michaelangelo” was a spooky ripoff of Stoned

   - Almost identical functionality, with the exception of the logic bomb: Michelangelo (the virus) trashed a user’s hard drive on March 6th (the birthday of Michelangelo di Lodovico Buonarroti Simoni. The artist…  Alright, you know who I’m talking about. He did the paintings on the ceiling of the Sistine Chapel. And David. The sculpture of David.)

- Michelangelo was/is an absolute legend in the art world

   - He deserves a better bootkit

- Did the Michelangelo bootkit do anything to improve upon Stoned?

   - improved code structure/style in Michelangelo:

      - removes a lot of redundant code in Stoned

      - simplifies certain functions with better assembly coding patterns

      - smaller total size

Image credit - still from “Michaelangelo: 25 Years Later” by danooctl1 <u>https://youtu.be/kl_Hbj0BpRU</u> Image also used in this article: “Watch Journalists in the 90s Freak Out Over the Destructive ‘Michelangelo’ Virus That Wasn’t” <u>https://www.vice.com/en/article/kbybkz/watch-the-collective-media-freakout-over-thedestructive-michelangelo-virus-that-wasnt</u>

## Slide 34

###### **“Reverse Engineering” Michaelangelo**

• vx-underground GitHub — MS-DOS Malware collection - Michaelangelo (original source file?) <u>https://github.com/vxunderground/MalwareSourceCode/tree/main/MSDOS</u>

- vx-underground GitHub — MS-DOS Malware collection - Michaelangelo (Dark Angel’s disassembly of the Michaelangelo bootkit, 40Hex number 8, volume 2, issue 4) <u>https://github.com/vxunderground/MalwareSourceCode/tree/main/MSDOS</u>

- Again, the zine archives on VX-UG, primarily 40hex and 29a zine archives

   - Both for vx work in those zines and for the articles/tutorials therein

- “Reverse Engineering” —> reading the assembly files; using that knowledge to rewrite my own

   - Due to the amount of preliminary research on other viruses, this part of the process was relatively quick

## Slide 35

###### **Michelangelo REanimator wake the dead!!**

- Use the best techniques of Stoned and Michelangelo to write a better bootkit

- Use techniques of Spanska for sprites, animation, vx writing as art

- Use techniques of other vx writers (i.e. Dark Angel) for *flair*

- Flair == polymorphism

## Slide 36

**Challenges of bootkit art “Artists must suffer for the art. That’s why it’s called** **_painting_ .”**

- 512 bytes is a pretty small amount of small for a virus under normal conditions

- 512 bytes is brutal when you are trying to load an image of a sprite at 128x80 resolution even after downsampling it and adding the byte buffer to the data section of your virus and realizing you probably can only fit a sprite that’s < 64 bytes and at that point, the pixelated output of your original image is so drastically different so as to be unrecognizable and wow I am really suffering for the art, someone give me a solo show at the Whitney

   - 128*80 == 10240 bytes

   - Why this resolution? Because 320x200 bytes would occupy the entire VGA buffer. But it also results in an image file that is 64000 bytes.

      - 64000 bytes is almost too large for a normal COM program on DOS [file size limit of .COM program: 65536 bytes - length PSP (256 bytes) - word of stack (2 bytes) = 65278 bytes (~63kB)

   - Try scaling down to 1/10 at 32*20?

   - 32*20 == 640 bytes, but the resulting image just looks like trash… and it’s still larger than 512 bytes

- 128*80 was the sprite size that provided a happy medium — the generated sprite was still recognizable and detailed enough, and the resulting image size was small enough to fit into the region of sectors between the MBR and VBR

## Slide 37

**michelangelo REanimator Bootkit features and functionality **Work in Progress**

- Int 13h handler (TSR) — adapted from one of my other demo TSRs

- Polymorphic -> used for graphics routines and for simple bootkit encryption/decryption routine

- Replaces original MBR code with vx MBR, saves original MBR on free sectors on “disk”

   - (I have only tested this on my emulator setup, so this is infecting a virtual disk image in QEMU; I have yet to test this on hardware of that era.)

- Graphical payload

- Stores the graphical payload in sectors on disk that are free (using same technique as bootkits of the 1980s/1990s — FDISK formats a drive so first sector of active partition is at (C 0, H 1, S 1) • # free sectors between MBR and root directory of active partition = # of sectors on a cylinder (roughly 62, 63 - 1 (MBR), depends on disk formatting)

## Slide 38

**Sprite generation using Python script, part 1: downsampling**

## Slide 39

###### **Sprite generation using Python script, part 2: bitmap -> bytes**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Sprite generation using Python script,
part 2: bitmap -> bytes
MichelAngeBitmap:
```

## Slide 40

**Sprite generation using Python script, part 3: displaying the sprite with VGA magic**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Sprite generation using Python script, part 3:
displaying the sprite with VGA magic
he 1
```

## Slide 41

**michelangelo reanimator generation 0**

## Slide 42

## **michelangelo reanimator generation 1-1337**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
xOxXO See
* ic3qu3 33n
xoxo # i
1esqussnag
es FAT.g ot
Soy at
eS
rere be teres
\r
t
oP ige
u_kn u know u luv me.
xoxo re3qus snip ;
ics HEED EE: j
- michelangelo reanimator &
. generation 1- -1337 site? Bye ee SE eae
-
```

## Slide 43

Connections to modern bootkits

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
s to modern bootkits
lO
Connect
```

## Slide 44

###### **Practical applications of 16-bit legacy BIOS bootkits**

- MS-DOS is dead (rip) but systems using Legacy BIOS are not…

   - RE techniques for legacy BIOS bootkits (specifically DOS bootkits) are equally applicable to 16-bit bootkits of different OSes

   - Also applicable for legacy BIOS RE/exploit writing (i.e. legacy BIOS implants)

   - Relevant resources:

      - <u>BIOS Disassembly Ninjutsu Uncovered - by pinczakko</u>

      - Phrack articles:

         - “A Real SMM Rootkit: Reversing and Hooking BIOS SMI Handlers” Filip Wecherowski

         - “Persistent BIOS Infection: The early bird catches the worm” by .aLS and Alfredo

         - “System Management Mode Hack: Using SMM for ‘Other Purposes’” By BSDaemon, coideloko, D0nAnd0n

- VGA-targeting malware — “VGA Bootkit” by Nicholas E. Economou and Eduardo Juarez, presented at Ekoparty 2012

- Legacy BIOS —> UEFI

   - UEFI replaced legacy BIOS and offers significant security improvements, but it isn’t perfect

   - Knowing where to look in legacy BIOS bootkits can provide insights when trying to understand the code patterns used in modern UEFItargeting malware

[1]“Rootkits and Bootkits: Reversing Modern Malware and Next Generation Threats,” Alex Matrosov, Eugene Rodionov, and Sergey Bratus

## Slide 45

###### **VX Sources**

• vx-underground GitHub — MS-DOS Malware collection: <u>https://github.com/vxunderground/MalwareSourceCode/tree/main/MSDOS</u>

• “Internet Archive — Malware Museum,” Mikko Hypponen, <u>https://archive.org/details/malwaremuseum</u> NOTE: These are defanged binaries, they are useful for preliminary research but lack the malicious functionality that it interesting from an RE/malware analysis perspective

• The zine archives on VX-UG, primarily 40hex and 29a zine archives

• A myriad of knowledgeable experts who wish to remain anonymous

## Slide 46

### **References**

“Advanced MS-DOS Programming,” Ray Duncan, Microsoft Press, 1986

“Microsoft MS-DOS Programmer’s Reference,” Microsoft Corporation, 2nd ed.: version 6.0., Microsoft Press, 1993 "The Giant Black Book of Computer Viruses," Mark Ludwig, 2nd ed., American Eagle Books, 1998.

"Rootkits and Bootkits: Reversing Modern Malware and Next Generation Threats,”Alex Matrosov, Eugene Rodionov, and Sergey Bratus, No Starch Press, 2019

“Computer Viruses and Data Protection: Unclassified,” Ralf Burger, Abacus Software, 1991

“A Look Back at Memory Models in 16-bit MS-DOS,” Raymond Chen, The Old New Thing, Microsoft Blogs, July 28, 2020, <u>https://devblogs.microsoft.com/oldnewthing/20200728-00/?p=104012</u>

“On Memory Allocations Larger Than 64KB on 16-Bit Windows,” Raymond Chen, The Old New Thing,  Microsoft Blogs, <u>https://devblogs.microsoft.com/oldnewthing/20171113-00/?p=97386</u>

“Retired Malware Samples, Everything Old is New Again,” Lenny Zeltser, August 1, 2018. <u>https://zeltser.com/retired-malware-samples-retrospective/</u>
