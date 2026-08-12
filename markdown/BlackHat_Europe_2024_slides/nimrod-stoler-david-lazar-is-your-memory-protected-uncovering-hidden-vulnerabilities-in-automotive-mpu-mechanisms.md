---
title: "Is Your Memory Protected Uncovering Hidden Vulnerabilities in Automotive MPU Mechanisms"
speakers: ["Nimrod Stoler", "David Lazar"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2024"
edition: "Europe"
year: 2024
source_pdf: "BlackHat_Europe_2024_slides/Nimrod Stoler & David Lazar_Is Your Memory Protected Uncovering Hidden Vulnerabilities in Automotive MPU Mechanisms.pdf"
pages: 68
sha256: "8f6547415e762e4daf21fd8a38be83ad7ce294e10d46d383501fb78dabb22e4c"
text_chars: 27438
ocr_pages: 13
has_ocr: true
redacted_secrets: 0
ocr_confidence: 89.5
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: ["Nimrod Stoler & David Lazar_Is Your Memory Protected Uncovering Hidden Vulnerabilities in Automotive MPU Mechanisms_blog.txt"]
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:59:31Z"
---
# Is Your Memory Protected Uncovering Hidden Vulnerabilities in Automotive MPU Mechanisms

**Speakers:** Nimrod Stoler, David Lazar  
**Conference:** Black Hat Europe 2024  
**Source:** `BlackHat_Europe_2024_slides/Nimrod Stoler & David Lazar_Is Your Memory Protected Uncovering Hidden Vulnerabilities in Automotive MPU Mechanisms.pdf` (68 pages)


## Slide 1

Is Your Memory Protected? Uncovering Hidden Vulnerabilities in Automotive MPUs Nimrod Stoler & David Lazar

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 85/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
EUROPE 2024 © ve
DECEMBER 11-12, 2024 --
BRIEFINGS
| ==
Is Your Memory Protected?
Uncovering Hidden Vulnerabilities in Automotive MPUs
Nimrod Stoler & David Lazar
PLAXIDIT YX
GO EVERYWHERE
#BHEU
@BlackHatEvents
```

## Slide 2

###### **PlaxidityX**

###### Who we are

**Cybersecurity Solutions for the Automotive Industry:**

- Comprehensive cybersecurity products and services

- Automotive intrusion detection systems

- Anti-vehicle theft solutions

###### **Nimrod Stoler**

Security Researcher @ PlaxidityX

- Vulnerability management

- DevSecOps

###### **Embedded Research Team**

**Specializations** :

- Automotive vulnerability research & Penetration testing

- Embedded systems & Hardware research

###### **David Lazar**

Embedded Research Team Lead @ PlaxidityX

- Reverse engineering

- Fuzzing

###### **Highlights** :

- Over 250,000 hours of combined experience in automotive cybersecurity

- In-depth knowledge of the vehicle cybersecurity lifecycle

- Expertise in automotive architectures, protocols, and standards

- Proficient in UNR 155 & 156, ISO 21434, and related incident and vulnerability management and treatment

#BHEU @BlackHatEvents 2

Information Classification: General

## Slide 3

ECU ECU
ECU
ECU
ECU
ECU
ECU

ECU – Electronic Control Unit

3

Information Classification: General

#BHEU @BlackHatEvents

## Slide 4

ECU ECU
ECU
ECU
ECU
ECU
ECU

ECU – Electronic Control Unit

4

Information Classification: General

#BHEU @BlackHatEvents

## Slide 5

ECU ECU
X Execute code from stack
ECU
ECU X Send messages to ECUs
ECU
X Read sensitive data
ECU
ECU

ECU – Electronic Control Unit

#BHEU @BlackHatEvents 5

Information Classification: General

## Slide 6

# **MPU**

##### **M** emory **P** rotection **U** nit

#BHEU @BlackHatEvents 6

Information Classification: General

## Slide 7

###### Agenda

- MPU Introduction & Functionality

- Analysis of the vulnerabilities & Demo

- Disclosure Processes with vendors

- Mitigations and Concluding remarks

7

Information Classification: General

#BHEU @BlackHatEvents

## Slide 8

###### What’s an MPU?

- **M** emory **P** rotection **U** nit

- Programmable hardware unit that acts as a gatekeeper of memory

- **Divides** memory into **regions**

- For each region, MPUs set:

   - Memory **access permissions** and

   - Memory **attributes**

- MPUs oversee access control to shared memory resources. Goal is to **reduce attack surface**

8

Information Classification: General

#BHEU @BlackHatEvents

## Slide 9

Core 2
Other Bus
CPU
Managers (DMA,
Cores
Ethernet, etc..)
MPU Communication Bus
RAM Flash
Other Bus
Subordinates
Core 0 Data Core 0 Code
(Peripherals)
Core 1 Data Core 1 Code
Core 2 Data Core 2 Code

#BHEU @BlackHatEvents 9

Information Classification: General

## Slide 10

Core 2
Other Bus
CPU
Managers (DMA,
Cores
Ethernet, etc..)
MPU Communication Bus
RAM Flash
Other Bus
Subordinates
NO ACCESS Core 0 Data Core 0 Code
(Peripherals)
Core 1 Data Core 1 Code
NO ACCESS
READ/WRITE Core 2 Data Core 2 Code READ/WRITE/EXECUTE

MPU Regions
Region 1: No Access
Region 2: Read/Write
Region 3: Read/Write/Execute

#BHEU @BlackHatEvents 10

Information Classification: General

## Slide 11

Core 2
Other Bus
CPU
Managers (DMA,
Cores
Ethernet, etc..)
Read Core 1 Data
MPU Communication Bus
RAM Flash
Other Bus
Subordinates
NO ACCESS Core 0 Data Core 0 Code
(Peripherals)
Core 1 Data Core 1 Code
NO ACCESS
READ/WRITE Core 2 Data Core 2 Code READ/WRITE/EXECUTE

**<u>MPU Regions</u> Region 1: No Access Region 2: Read/Write Region 3: Read/Write/Execute**

#BHEU @BlackHatEvents 11

Information Classification: General

## Slide 12

Core 2
MPU Regions
Other Bus
CPU Region 1: No Access
Managers (DMA,
Cores Region 2: Read/Write
Ethernet, etc..)
Region 3: Read/Write/Execute
Read Core 2 Data
MPU Communication Bus
RAM Flash
Other Bus
Subordinates
NO ACCESS Core 0 Data Core 0 Code
(Peripherals)
Core 1 Data Core 1 Code
NO ACCESS
READ/WRITE Core 2 Data Core 2 Code READ/WRITE/EXECUTE

#BHEU @BlackHatEvents 12

Information Classification: General

## Slide 13

###### Types of MPUs

#BHEU @BlackHatEvents 13


> Recovered by OCR — confidence 93/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Types of MPUs
#BHEU @BlackHatEvents 13
```

## Slide 14

###### Core Memory Protection Unit

- Also called CMPU or CPU MPU

- **Integrated** into each of the cores

- Controls memory transactions **originating** from each of the cores

- Important attribute is the **“execute” flag** , critical to mitigate buffer overflows

Core 2
CPU
Other Bus
Cores
Managers (DMA,
Ethernet, etc..)
CMPU

Communication Bus

Other Bus
RAM Flash Subordinates
(Peripherals)

#BHEU @BlackHatEvents 14

Information Classification: General

## Slide 15

Core 2
CPU
Other Bus
Cores
Managers (DMA,
Ethernet, etc..)
CMPU
Communication Bus SMPU
Other Bus
RAM Flash Subordinates
(Peripherals)

###### System Memory Protection Unit

- Positioned between memory transaction sources and common memories

- It is **source aware**

- Offers **system wide protection**

- Manages a list of allowed sources, or bus-masters with their attributes

#BHEU @BlackHatEvents 15

Information Classification: General

## Slide 16

###### How to configure PowerPC MPUs?

<u>Source: Google’s Gemini</u>

#BHEU @BlackHatEvents 16

Information Classification: General

## Slide 17

###### **452 PAGES**

Source: https://en.wikipedia.org/wiki/PowerPC_600#/media/File:Motorola_PowerPC_604e_233MHz_2.jpg

#BHEU @BlackHatEvents 17

Information Classification: General

## Slide 18

###### **390 PAGES**

#BHEU @BlackHatEvents 18

Information Classification: General


> Recovered by OCR — confidence 79/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
390 PAGES
Table of contents UM0434
Table of contents
e200z3 PowerPC core
1.2 Related documentation
1.3 Audience ..............
Introduction
The primary objective of this user's manual is to describe the functionality of the e200z3
embedded microprocessor core for software and hardware developers. This book is
Book E is a PowerPC™ architecture definition for embedded processors that ensures binary 2.2 Acronyms and abbreviations .............. 0.0 cece cece eee eeu 23
compatibility with the user-instruction set architecture (UISA) portion of the PowerPC
architecture as it was jointly developed by Apple, IBM, and Motorola (referred to as the AIM
This document distinguishes among the three levels of the architectural and implementation 3.1 Overview of the €20023 .... 2... esse eee eee cece ee ee eee ees 24
@ The Book E architecture—Book E defines a set of user-level instructions and registers 3.2 Programming model ..... 2.200.200 ccc cece cece ec eeeeeuueeeuees 26
that are drawn from the user instruction set architecture (UISA) portion of the AIM
registers and instructions as they were defined in the AIM version of the PowerPC 3.3 Instruction set... 0... ccc cece cee ee cee eee ueueeeneueeueunes 27
architecture for the virtual environment architecture (VEA) and the operating
Because the operating system resources (such as the MMU and interrupts) defined by 3.5 Interrupts and exception handling ...............eeeeeeeeeeeeeee 29
Book E differ greatly from those defined by the AIM architecture, Book E introduces 3.5.1 Interrupt handling . 0.0... ccc cece cece eee eeeueeeeees 29
many new registers and instructions.
@ Freescale Book E implementation standards (EIS)—In many cases, the Book E 3.5.2 Interrupt Class€S 2.6... eee eect eee eeeeeeeeee 30
implementation. To ensure consistency among its Book E implementations, Freescale 3.5.4 Hnborruppt reGhebers wwe cece cece nese snasancasencanasscncsan 31
has defined implementation standards that provide an additional layer of architecture .
Information Classification: General 18
```

## Slide 19

147 PAGES

#BHEU @BlackHatEvents 19

Information Classification: General


> Recovered by OCR — confidence 90/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
147 PAGES
SPC58EHx, SPC58NHx
SPC58 H Line - 32 bit Power Architecture automotive MCU
Triple z4 cores 200 MHz, 10 MBytes Flash, HSM, ASIL-D
eTOFP 144 (20 x 20 x 1.0 mm) eLOFP 176 (24 x 24 x 1.4 mm)
FPBGA302 (17 x 17 x 1.8 mm) FPBGA386 (19 x 19x 1.8 mm)
Features
e AEC-Q100 qualified
e High performance e20024 triple core:
32-bit Power Architecture technology CPU
Core frequency as high as 200 MHz
Variable Length Encoding (VLE)
Floating Point, End-to-End Error Correction
* 10496 KB (10240 KB code Flash + 256 KB
data Flash) on-chip Flash memory:
— Supports read during program and erase
operations, and multiple blocks allowing
EEPROM emulation
Datasheet - production data
Comprehensive new generation ASIL-D safety
concept:
— ASIL-D of ISO 26262
— One CPU channel in lockstep
— Logic BIST
— FCCU for collection and reaction to failure
notifications
— Memory BIST
— Cyclic redundancy check (CRC) unit
— Memory Error Management Unit (MEMU)
for collection and reporting of error events
in memories
Crossbar switch architecture for concurrent
access to peripherals, Flash, or RAM from
multiple bus masters with end-to-end ECC
Body cross triggering unit (BCTU)
— Triggers ADC conversions from any eMIOS
channel
— Triggers ADC conversions from up to 2
dedicated PIT_RTis
Enhanced modular |O subsystem (eMIOS):
— up to 96 timed IO channels with 16-bit
Contents
2.1 Device feature summary ...........00 202.00 7
2.3 Features
3 Package pinouts and signal descriptions .....................25 17
4.3. Operating conditions
43.1 Power domains and power up/down sequencing ................. 24
44 Electrostatic discharge (ESD) ........... 0.0000. 25
19
```

## Slide 20

###### **1,439 PAGES**

#BHEU @BlackHatEvents 20

Information Classification: General


> Recovered by OCR — confidence 79/100 on the text kept, 58/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
1,439 PAGES
Contents RM0070
f Contents
14 Register description conventions . . aoe . 65
1.6 How to use the SPC564Bxx and SPC56ECxx documents ........... 66
Introducti on 1.6.1 The SPC564Bxx and SPC56ECxx document set .................66
The SPC564Bxx and SPC56ECxx is a family of Power Architecture® based microcontrollers tan deine econ ve 69
* Central t iy controller 1.7.3 Software design . . . . cesses 70
«* Smart junction boxes
* Front modules 2.1 The SPC564Bxx and SPC56ECxx microcontroller family ............ 72
* High end gateway 2.2 SPC564Bxx and SPCS56ECxx device comparison ................ 72
The SPC564Bxx and SPC56ECxx family expands the range of the SPC560B/C 342 edoedhnemaussson ap
microcontroller family. It provides the scalability needed to implement platform approaches 24.3 Memory Built-In Self Test (MBIST) ............ beceeeeeeeeees 77
and delivers the performance required by increasingly sophisticated software architectures. 2.4.4 Enhanced Direct Memory Access Controller (eDMA) .... 7
Information Classification: General 20
```

## Slide 21

### 2428 pages

1 bit

21

Information Classification: General

#BHEU @BlackHatEvents

## Slide 22

###### Analysis of HW vulnerabilities CVE-2023-48010 CVE-2024-33882

#BHEU @BlackHatEvents 22

## Slide 23

###### ■ **STMicroelectronic PowerPC Automotive & Industrial MCU**

<u>Source: https://www.st.com/resource/en/brochure/brspc58c.pdf</u>

#BHEU @BlackHatEvents 23

Information Classification: General

## Slide 24

###### ■ **STMicroelectronic PowerPC Automotive**

**& Industrial MCU**

###### ■ **Used in different automotive applications**

<u>Source: https://www.st.com/resource/en/brochure/brspc58c.pdf</u>

#BHEU @BlackHatEvents 24

Information Classification: General

## Slide 25

- **STMicroelectronic PowerPC Automotive**

   - **& Industrial MCU**

- **Used in different automotive applications**

- **Affected STM Parts:**

   - All SPC58 devices

   - SR5E1

   - SPC574K (K2)

   - SPC572L (Lavaredo)

- SPC574Sx (Sphaero)

Source: https://www.st.com/resource/en/brochure/brspc58c.pdf

#BHEU @BlackHatEvents 25

Information Classification: General

## Slide 26

###### STMicroelectronics SPC58xx Power PC

<u>SourceSour: SPC584C Datce: SPC58xx D</u> **a** tasheet, DSsheet, DS1 **1** 62 Rev 8, p. 923 **0** 4 Rev 5, p. 10

#BHEU @BlackHatEvents 26

Information Classification: General

## Slide 27

###### STMicroelectronics SPC58xx Power PC

<u>Source: SPC584C Datasheet, DS11620 Rev 8, p. 9</u>

27

27

Information Classification: General

#BHEU @BlackHatEvents

## Slide 28

###### STMicroelectronics SPC58xx Power PC

**<u>Source: SP</u>** C58xx DatasheC584C Datash **e** t, DS12304 Rev 5,et, DS11620 Rev 8, p. 9p. 10

#BHEU @BlackHatEvents 28

Information Classification: General

## Slide 29

###### STMicroelectronics SPC58xx Power PC

**Per Each SMPU Region:**

- Start address

- End address

- List of allowed **Sources**

- and their attributes

<u>Source: SPC584C Datasheet, DS11620 Rev 8, p. 9</u>

29

Information Classification: General

#BHEU @BlackHatEvents

## Slide 30

###### SMPU Bus-Masters

Source: RM0452-spc58-line Rev.4 p. 136

<u>Source: RM0452-spc58-line Rev.4 p. 136</u>

#BHEU @BlackHatEvents 30

Information Classification: General

## Slide 31

###### Configuration Steps

1. Define the region descriptors:

   - Set start address & end address for each region

   - List allowed bus masters and their access attributes

2. Lock the RGDs using RO field

3. Enable the SMPU by setting the GVLD bit

4. SMPU is now enabled and locked

Core 2
CPU
Other Bus
Cores
Managers (DMA,
Ethernet, etc..)
CMPU

Communication Bus SMPU

Other Bus
Subordinates
(Peripherals)

Flash

RAM

Core 0 Data
Core 0 Data
Core 1 Data
Core 1 Data

0x40000000

0x4000FFFF

0x40010000

**Core 2 Data** Core 2 Data

0x4001FFFF

31

Information Classification: General

#BHEU @BlackHatEvents

## Slide 32

Core 2
CPU
Other Bus
Cores
Managers (DMA,
Ethernet, etc..)
CMPU

###### Configuration Steps

1. Define the region descriptors:

- Set start address & end address for each region

- List allowed bus masters and their access attributes

Communication Bus SMPU

2. Lock the RGDs using RO field

3. Enable the SMPU by setting the GVLD bit

4. SMPU is now enabled and locked

Other Bus
Subordinates
(Peripherals)

###### **SMPU Region 1**

Flash

RAM

[0x40000000-0x4000FFFF] Bus masters: CPU Core 2 – No access

Core 0 Data
Core 0 Data
Core 1 Data
Core 1 Data

**NO ACCESS 0x40000000**

**NO ACCESS 0x4000FFFF**

**<u>SMPU Region 2</u>** [0x40010000-0x4001FFFF] READ/WRITE 0x40010000 Bus masters: CPU Core 2 – R/W READ/WRITE 0x4001FFFF

**Core 2 Data**

Core 2 Data

#BHEU @BlackHatEvents 32

Information Classification: General

## Slide 33

Core 2
CPU
Other Bus
Cores
Managers (DMA,
Ethernet, etc..)
CMPU

###### Configuration Steps

1. Define the region descriptors:

- Set start address & end address for each region

- List allowed bus masters and their access attributes

Communication Bus SMPU

2. Lock the RGDs using RO field

3. Enable the SMPU by setting the GVLD bit

4. SMPU is now enabled and locked

Other Bus
Subordinates
(Peripherals)

###### **<u>SMPU Region 1</u>**

Flash

RAM

[0x40000000-0x4000FFFF] Bus masters: CPU Core 2 – No access

**Core 0 Data** Core 0 Data **Core 1 Data** Core 1 Data

NO ACCESS 0x40000000

NO ACCESS 0x4000FFFF

###### **SMPU Region 2**

[0x40010000-0x4001FFFF] Bus masters: CPU Core 2 – R/W

**READ/WRITE 0x40010000 READ/WRITE 0x4001FFFF**

**Core 2 Data** Core 2 Data

#BHEU @BlackHatEvents 33

Information Classification: General

## Slide 34

###### The Control/Error Status Register 0

<u>Source: RM0452-spc58-line Rev.4 p. 557</u>

#BHEU @BlackHatEvents 34

Information Classification: General

## Slide 35

Source: RM0452-spc58-line Rev.4

<u>Source: RM0452-spc58-line Rev.4 p. 563</u>

#BHEU @BlackHatEvents 35

Information Classification: General

## Slide 36

<u>Source: RM0452-spc58-line Rev.4 p. 563</u> Source: RM0452-spc58-line Rev.4

#BHEU @BlackHatEvents 36

Information Classification: General

## Slide 37

<u>Source: RM0452-spc58-line Rev.4 p. 563</u>

#BHEU @BlackHatEvents 37

Information Classification: General


> Recovered by OCR — confidence 90/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Table 284. RGDn_WORDS field descriptions
Region Descriptor Format
This bit selects the configuration format (FMITO or FMT 1) for this region descriptor.
a7 Note: A specific module instance of the SMPU may support only the FMTO format.
EMT Ifso. the FMT field is read-only with a fixed value of 0 and only
, RGD_WORD2_FMTO applies.
Q Use format 0 (RGD_WORD2 FMTQ)
the valid bit ‘of the RGD and the global valid bit have no effect.
Note: Setting RO in an RGD locks all four words of the RGD until a system !
eset
the valid bit of the RGD and the global valid bit have no effect.
O The region descriptor can be read or written.
1 Attempted writes to any location in the region descriptor are ignored with an
error-free data transfer termination.
Source: RM0452-spc58-line Rev.4 p. 563
37
```

## Slide 38

<u>Source: RM0452-spc58-line Rev.4 p. 563</u>

#BHEU @BlackHatEvents 38

Information Classification: General


> Recovered by OCR — confidence 91/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Table 284. RGDn_WORDS field descriptions
Region Descriptor Format
This bit selects the configuration format (FMITO or FMT 1) for this region descriptor.
a7 Note: A specific module instance of the SMPU may support only the FMTO format.
EMT Ifso. the FMT field is read-only with a fixed value of 0 and only
, RGD_WORD2_FMTO applies.
Q Use format 0 (RGD_WORD2 FMTQ)
Note: Setting RO in an RGD locks all four words of the RGD until a system reset;
the valid bit of the RGD and the global valid bit have no effect.
RO the valid bit of the RGD and the global valid bit have no effect.
O The region descriptor can be read or written.
1 Attempted writes to any location in the region descriptor are ignored with an
error-free data transfer termination.
Source: RM0452-spc58-line Rev.4 p. 563
Information Classification: General 38
```

## Slide 39

###### Configuration Steps

**Core 2 CPU Cores CMPU**

**Other Bus Managers (DMA, Ethernet, etc..)**

1. Define the region descriptors:

   - Set start address & end address for each region

■ List allowed bus masters and their access attributes

2. Lock the RGDs using RO field

3. Enable the SMPU by setting the GVLD bit

4. SMPU is now enabled and locked

NO ACCESS 0x40000000 NO ACCESS 0x4000FFFF

**RAM**

**Core 0 Data** Core 0 Data **Core 1 Data** Core 1 Data

**<u>Config bits</u> RO             0 GVLD        0**

> **Communication Bus SMPU**

Flash

**Other Bus Subordinates (Peripherals)**

**READ/WRITE 0x4001FFFF**

**Core 2 Data**

Core 2 Data

#BHEU @BlackHatEvents 39

Information Classification: General

## Slide 40

###### Configuration Steps

**Core 2 CPU Other Bus Cores Managers (DMA, Ethernet, etc..) CMPU**

1. Define the region descriptors:

   - Set start address & end address for each region

■ List allowed bus masters and their access attributes

**2. Lock the RGDs using RO field**

3. Enable the SMPU by setting the GVLD bit

4. SMPU is now enabled and locked

NO ACCESS 0x40000000 NO ACCESS 0x4000FFFF

**<u>Config bits</u>** **RO 1 GVLD        0 Communication Bus SMPU**

Flash

**RAM**

**Other Bus Subordinates (Peripherals)**

Core 0 Data
Core 0 Data
Core 1 Data
Core 1 Data

**READ/WRITE 0x4001FFFF**

**Core 2 Data** Core 2 Data

#BHEU @BlackHatEvents 40

Information Classification: General

## Slide 41

###### Configuration Steps

**Core 2 CPU Other Bus Cores Managers (DMA, Ethernet, etc..) CMPU**

1. Define the region descriptors:

   - Set start address & end address for each region

■ List allowed bus masters and their access attributes

2. Lock the RGDs using RO field

**3. Enable the SMPU by setting the GVLD bit**

4. SMPU is now enabled and locked

NO ACCESS 0x40000000 NO ACCESS 0x4000FFFF

**<u>Config bits</u> RO             1** **GVLD 1 Communication Bus SMPU**

Flash

**RAM**

**Other Bus Subordinates (Peripherals)**

Core 0 Data
Core 0 Data
Core 1 Data
Core 1 Data

**READ/WRITE 0x4001FFFF**

**Core 2 Data** Core 2 Data

#BHEU @BlackHatEvents 41

Information Classification: General

## Slide 42

###### Configuration Steps

1. Define the region descriptors:

   - Set start address & end address for each region

■ List allowed bus masters and their access attributes

2. Lock the RGDs using RO field

3. Enable the SMPU by setting the GVLD bit

**4. SMPU is now enabled and locked**

NO ACCESS 0x40000000 NO ACCESS 0x4000FFFF

Core 2
CPU
Cores
CMPU

**Other Bus Managers (DMA, Ethernet, etc..)**

**<u>Config bits</u> RO             1 GVLD        1 Communication Bus SMPU**

Flash

**RAM**

**Other Bus Subordinates (Peripherals)**

Core 0 Data
Core 0 Data
Core 1 Data
Core 1 Data

**READ/WRITE 0x4001FFFF**

**Core 2 Data**

Core 2 Data

#BHEU @BlackHatEvents 42

Information Classification: General

## Slide 43

Core 2
CPU
Cores
CMPU

Other Bus
Managers (DMA,
Ethernet, etc..)
Config bits
RO             1
GVLD        1
SMPU
Other Bus
Subordinates
(Peripherals)

###### SMPU is now enabled and locked

Communication Bus
RAM
NO ACCESS 0x40000000 Core 0 Data Core 0 Data Flash
NO ACCESS 0x4000FFFF Core 1 Data Core 1 Data
Core 2 Data
Core 2 Data
READ/WRITE 0x4001FFFF

#BHEU @BlackHatEvents 43

Information Classification: General

## Slide 44

###### SMPU is now enabled and locked

#### Or is it?

**Core 2 CPU Cores CMPU**

**Other Bus Managers (DMA, Ethernet, etc..)**

**<u>Config bits</u> RO             1 GVLD        1 SMPU**

**Communication Bus**

RAM
NO ACCESS 0x40000000 Core 0 Data Core 0 Data
NO ACCESS 0x4000FFFF Core 1 Data Core 1 Data
Core 2 Data
Core 2 Data
READ/WRITE 0x4001FFFF

Flash

**Other Bus Subordinates (Peripherals)**

#BHEU @BlackHatEvents 44

Information Classification: General

## Slide 45

#### SMPU is now enabled and locked Or is it?

45

Information Classification: General

#BHEU @BlackHatEvents

## Slide 46

## **CVE-2023-48010**

After the SMPU is **configured** , **enabled** and regions are **locked** , a privileged attacker can flip the GVLD bit, **disabling** the SMPU Providing **read and write** access to protected areas

#BHEU @BlackHatEvents 46

Information Classification: General

## Slide 47

###### Seeking for similar targets

- NXP MPC5xx PowerPC family

- For our test we chose the MPC5748

- Automotive and Industrial Control MCU

- Does NXP MPC5748 share the SMPU issue?

v

Source: https://www.nxp.com/docs/en/fact-sheet/MPC5748GFS.pdf

#BHEU @BlackHatEvents 47

Information Classification: General

## Slide 48

###### NXP MPC5748 PowerPC

Cores 0 + 1
Core 2

<u>Source: MPC5748G Microcontroller Data Sheet, Rev. 6, 11/2018, p. 4</u> Source: MPC5748G Microcontroller Data Sheet, Rev. 6, 11/2018, p. 4

#BHEU @BlackHatEvents 48

Information Classification: General

## Slide 49

###### NXP SMPU Global Valid Flag

#BHEU @BlackHatEvents 49

Information Classification: General


> Recovered by OCR — confidence 86/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
biSekhat NXP SMPU Global Valid Flag
Memory map/register definition
SMPUx_CES0 field descriptions (continued)
Same cycle as the write, the flag remains set. A find-first-one instruction (or equivalent) can detect the
presence of a captured error,
0 No error has occurred for bus master n
1 An error has occurred for bus master n.
16-27 This field is reserved
Reserved This. read-only field is reserved and always has the value 0.
28-30 Hardware revision level
HAL
Specifies the SMPU's hardware and definition revision level. It can be read by software to determine the
functional definition of {he module.
a1 Global Valid (global enable/disable for the SMPU)
0 SMPU 65 disabled. All accesses from all bus masters are allowed.
1 SMPU is enabled.
Source: MPC5/48G Reference Manual, Rev. 7.1 p. 493-494
Information Classification: General 49
```

## Slide 50

###### NXP SMPU Lock Bit and note

#BHEU @BlackHatEvents 50

Information Classification: General

<u>SourceSourc: MPC5748G Reference Manual, Rev. 7.1, p. 505e: MPC5748G Reference Manual, Rev. 7.1, p. 505</u>

## Slide 51

###### NXP SMPU Lock Bit and note

#BHEU @BlackHatEvents 51

Information Classification: General

<u>SourceSourc: MPC5748G Reference Manual, Rev. 7.1, p. 505e: MPC5748G Reference Manual, Rev. 7.1, p. 505</u>

## Slide 52

## **CVE-2024-33882**

After the SMPU is **configured** , **enabled** and regions are **locked** , a privileged attacker can flip the GVLD bit, **disabling** the SMPU

Providing read, write and **execute** access to protected areas

#BHEU @BlackHatEvents 52

Information Classification: General

## Slide 53

###### The Demo

#BHEU @BlackHatEvents 53

## Slide 54

###### The Demo Setup

ECU ECU
BCM
ECU
ECU
ECU

■ A demo BCM is connected to the Airbag deployment mechanism and in charge of activating it

**ECU** – Electronic Control Unit **BCM** – Body Control Module

#BHEU @BlackHatEvents 54

Information Classification: General

## Slide 55

###### The Demo Setup

ECU ECU
BCM
ECU
ECU
ECU

- Attacker is exploiting a stack buffer overflow on the BCM

- The Airbag mechanism is protected by the BCM SMPU

- Stack is non-executable, so only ROP is available

**ECU** – Electronic Control Unit **BCM** – Body Control Module

55

Information Classification: General

#BHEU @BlackHatEvents

## Slide 56

###### The Demo Setup

ECU ECU
BCM
ECU
ECU
ECU

- Attacker’s goal is to reach the airbag mechanism’s memory and explode the airbags

**ECU** – Electronic Control Unit **BCM** – Body Control Module

#BHEU @BlackHatEvents 56

Information Classification: General

## Slide 57

Other Bus
CPU
Managers (DMA,
Cores
Ethernet, etc..)
Config bits SMPU Region 5
LCK/RO    1 [0xFFFC1300-0xFFFC13FF]
GVLD        1 Bus master 3 - R/W
Communication Bus SMPU
Airbag Deployment
Mechanism
RAM Flash
0xFFFC1300
0xFFFC13FF

###### Demo Attack Path

57

Information Classification: General

#BHEU @BlackHatEvents

## Slide 58

###### The Demo BCM

(1) Power LED
To rest of vehicle
NXP
MPC5748
(2) Airbag Deployment LED

#BHEU @BlackHatEvents 58

Information Classification: General

## Slide 59

###### Demo Video 1

#BHEU @BlackHatEvents 59

Information Classification: General


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
DEMO 1: SMPU is ON
Attacker has stack buffer overflow over the target BCM
Goal is to trigger Airbag Deployment
```

## Slide 60

###### Demo Video 2

#BHEU @BlackHatEvents 60

Information Classification: General


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
DEMO 2: Exploit SMPU vulnerability
(1) Attacker disables SMPU by flipping GVLD
(2) Attacker attempts to trigger the Airbags
```

## Slide 61

###### The Responsible Disclosures

#BHEU @BlackHatEvents 61


> Recovered by OCR — confidence 94/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
The Responsible Disclosures
#BHEU @BlackHatEvents 61
```

## Slide 62

###### Responsible Disclosure with ST

- We contacted ST PSIRT with all information

- ST acknowledged the issue

- **Would release an errata**

- But claimed the SMPU is not a security mechanism

<u>Source: https://www.st.com/content/dam/st-crew/st-logo-blue.svg</u>

#BHEU @BlackHatEvents 62

Information Classification: General

## Slide 63

STMicroelectronics Response: “ The behavior deviation of SMPU you detected may affect non-secure device domains. However, this domain should not be used for storing security information.

Secret/security-critical data shall be stored within the HSM sub-system memory, if stored outside, **they need to be encrypted** .

**The SMPU is not a security protection mechanism:** rather, for example, it helps to avoid interference.

[Emphasis added]

63

Information Classification: General

#BHEU @BlackHatEvents

## Slide 64

###### Responsible Disclosure with NXP

- We contacted NXP PSIRT with all information

- NXP acknowledged the issue

- **Would release a Documentation Errata**

- Also claimed the SMPU is not a security feature

<u>Source: https://www.nxp.com/docs/en/fact-sheet/MPC5748GFS.pdf</u>

64

Information Classification: General

#BHEU @BlackHatEvents

## Slide 65

###### NXP Response:

“

**The product’s Reference Manual is clear about the SMPU not being a security feature.** The SMPU is **not mentioned in the chapter ‘Security Overview’** , nor in the section ‘Security Modules’, **but rather in the section on ‘System Modules’** . The SMPU is also not listed under ‘Security’ in the ‘Feature List’ table and the chapter that describes the SMPU does not mention ‘security’.

[Emphasis added]

65

Information Classification: General

#BHEU @BlackHatEvents

## Slide 66

###### Mitigations and conclusion

#BHEU @BlackHatEvents 66


> Recovered by OCR — confidence 94/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Mitigations and conclusion
#BHEU @BlackHatEvents 66
```

## Slide 67

###### Mitigations and Concluding Remarks

- Memory Protection Units are a crucial part of every microcontroller’s defense

- MPUs are indispensable in the context of Automotive apps

- Fixing hardware issue is hard!

###### **Mitigations:**

- Test important claims made in datasheet

- Use exploit mitigations, such as stack smashing defenses

- In the case of the ST chip, block as much as possible using the CMPUs

#BHEU @BlackHatEvents 67

Information Classification: General

## Slide 68

###### Thank you!

#BHEU @BlackHatEvents 68

Information Classification: General


> Recovered by OCR — confidence 91/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Thank you!
PLAXIDIT Y
GO EVERYWHERE
```

## Companion resources

### `Nimrod Stoler & David Lazar_Is Your Memory Protected Uncovering Hidden Vulnerabilities in Automotive MPU Mechanisms_blog.txt`

```text
https://plaxidityx.com/blog/blog-post/is-your-memory-protecteduncovering-hidden-vulnerabilities-in-automotive-mpu-mechanisms/
```
