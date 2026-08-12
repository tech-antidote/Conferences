---
title: "The HackDAC Story Learnings from Organizing the World's Largest Hardware Hacking Competition"
speakers: ["Arun Kanuparthi", "Hareesh Khattri", "Jason Fung", "Jeyavijayan JV Rajendran", "Ahmad-Reza Sadeghi"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2024"
edition: "ASIA"
year: 2024
source_pdf: "BlackHat ASIA 2024-Slides/Arun Kanuparthi & Hareesh Khattri & Jason Fung & Jeyavijayan JV Rajendran & Ahmad-Reza Sadeghi-The HackDAC Story Learnings from Organizing the World's Largest Hardware Hacking Competition.pdf"
pages: 47
sha256: "8b9f634fc4b1c46ad7c63175bf90df4f49dd5a47ac1347ad3bd52cbfd99a49ce"
text_chars: 23189
ocr_pages: 8
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:48:49Z"
---
# The HackDAC Story Learnings from Organizing the World's Largest Hardware Hacking Competition

**Speakers:** Arun Kanuparthi, Hareesh Khattri, Jason Fung, Jeyavijayan JV Rajendran, Ahmad-Reza Sadeghi  
**Conference:** Black Hat ASIA 2024  
**Source:** `BlackHat ASIA 2024-Slides/Arun Kanuparthi & Hareesh Khattri & Jason Fung & Jeyavijayan JV Rajendran & Ahmad-Reza Sadeghi-The HackDAC Story Learnings from Organizing the World's Largest Hardware Hacking Competition.pdf` (47 pages)


## Slide 1

# The Hack@DAC* Story: Learnings from Organizing the World’s Largest Hardware Hacking Competition **<u>Arun Kanuparthi</u>** <u>Intel Corporation, USA</u>

Collaborators: Hareesh Khattri, Jason Fung (Intel Corporation, USA) JV Rajendran (Texas A&M University, USA), Ahmad Reza Sadeghi (TU Darmstadt, Germany)

*Design Automation Conference (DAC)

#BHASIA @BlackHatEvents

## Slide 2

## The Team

**Arun Kanuparthi** Hareesh Khattri Principal Engineer, Principal Engineer, Offensive Security Researcher Offensive Security Researcher Intel Corporation, USA Intel Corporation, USA

Jason Fung Sr. Director

Offensive Security Research Intel Corporation, USA

Ahmad-Reza Sadeghi Professor TU Darmstadt, Germany

Jeyavijayan (JV) Rajendran Associate Professor Texas A&M University, USA

###### Offensive Security Research at Intel

- 50+ years of combined experience

- CPUs, Servers, Clients, Networking, Cellular, Storage, Security technologies, …

- • 500+ vulnerabilities identified

- Vulnerability root causing and categorization

- MITRE HW CWE SIG* members

###### Security Research

- 35+ years of combined experience

- Circuits, system security, network security, cryptography, microarchitecture, etc.

- 44000+ citations!

# BHASIA @BlackHatEvents

*Special Interest Group (SIG)

## Slide 3

## Full Team

###### **<u>Texas A&M University</u>**

- Rahul Kande

- Chen Chen

- Patrick Haney

- Garrett Persyn

- Bhagyaraja Adapa

###### **<u>TU Darmstadt</u>**

- Ghada Dessouky

- David Gens

- Pouya Mahmoody

- Mohammadreza Rostami

- Shaza Zeitouni

###### **<u>Synopsys</u>**

   - Shylaja Sen

   - Yann Antonioli

   - Jagminder Chugh

   - • Meriav Nitzan

- Venkatakrishnan Sutharsan

# BHASIA @BlackHatEvents

## Slide 4

## Overview

## Introduction

Value of Organizing HW CTFs

How Hack@DAC is Unique

Organizing Hack@DAC Key Takeaways & Summary

# BHASIA @BlackHatEvents

## Slide 5

## Overview

## Introduction

Value of Organizing HW CTFs

How Hack@DAC is Unique

Organizing Hack@DAC Key Takeaways & Summary

# BHASIA @BlackHatEvents

## Slide 6

## Computing Stack - Refresher

**Application Algorithm Programming Language Operating System Firmware MicroarchitectureMicroarchitecture Register Transfer Hardware Level Level(RTL) Gate Level**

**Transistor**

# BHASIA @BlackHatEvents <u>Image3 Source Image4 Source</u>

## Slide 7

## Computing Stack - Refresher

**Application Algorithm Programming Language Operating System Firmware MicroarchitectureMicroarchitecture Register Transfer Level Level(RTL) Gate Level Transistor**

Microarchitecture

Gate Level

assign ADD_result = reg_A + reg_B; assign SUB_result = reg_A – reg_B; assign AND_result = reg_A & reg_B; … if (IR_opcode_field == 0) case (IR_function_field) 6’b100000: ALU_result <= ADD_result; 6’b100010: ALU_result <= SUB_result; 6’b100100: ALU_result <= AND_result;

Register Transfer Level (RTL)

Transistor

# BHASIA @BlackHatEvents <u>Image3 Source Image4 Source</u>

## Slide 8

Race to the Bottom of the Stack **<u>Challenge #1</u>** : Limited Awareness of HW Security Weaknesses **Application Algorithm Programming Language Operating System Firmware MicroarchitectureMicroarchitecture** Bugs in hardware could be exploitable by software! **Register Transfer Level Level(RTL) Gate Level**

Bugs in hardware could be exploitable by software!

**Transistor**

_USENIX Security 2019_

# BHASIA @BlackHatEvents

## Slide 9

## Tools for Security – SW vs HW

Application
Algorithm
Programming
Language
Operating System
Firmware
MicroarchitectureMicroarchitecture
Register Transfer
Level Level(RTL)
Gate Level
Transistor
Software
Hardware

Lots of tools for SW/FW security!

- Code scanners

- Protocol checkers

- Configuration checkers

- Decompilers & RE tools

# BHASIA @BlackHatEvents

## Slide 10

## Tools for Security – SW vs HW **<u>Challenge #2</u>** : Need for Security-Aware Design Automation Tools

Application
Algorithm
Programming
Language
Operating System
Firmware
MicroarchitectureMicroarchitecture
Register Transfer
Level Level(RTL)
Gate Level
Transistor
Software
Hardware

HW security tools (at RTL level) are limited

# BHASIA @BlackHatEvents

## Slide 11

## Cost of Fixing Bugs

**<u>Challenge #3</u>** : Need to Detect/Fix Bugs at RTL Design Phase

Pre-Silicon Post-Silicon
1000X
100X
10X
X
RTL  Physical
Fab Customer
Design  Design
Fix bugs here! “Shift Left”
Cost to fix

- SW bugs fixed with patches

- HW bugs are complicated to fix

-
Time consuming
-
Expensive
-
Cause brand damage

# BHASIA @BlackHatEvents

## Slide 12

## Motivation for Hack@DAC

Awareness of  CONCEPTS
Hardware
Common
Weaknesses

Security- TOOLS
Aware Design
Automation

BEST PRACTICES
“Shift-Left” to
Detect & Fix
Bugs in RTL

**Hack@DAC**

- Hackathons, trainings

- Open-source hardware as target?

- What about hardware CTF?

# BHASIA @BlackHatEvents

## Slide 13

## Overview

## Introduction

Value of Organizing HW CTFs

How Hack@DAC is Unique

Organizing Hack@DAC Key Takeaways & Summary

# BHASIA @BlackHatEvents

## Slide 14

## Community Building

- CTFs bring passionate people together!

- Team make up comprises varied skill set

   - Design, Verification, Security expertise

   - Cross pollination of ideas

- Fun way to learn and share

# BHASIA @BlackHatEvents

Image: Design Automation Conference

## Slide 15

## Fostering Awareness for HW Security

- Continuous race between attackers and defenders

- Defenders need to up their game!

- Hardware CTFs foster greater awareness about

   - Common hardware security weaknesses

   - Constraints of chip design teams

# BHASIA @BlackHatEvents

Image <u>source</u>

## Slide 16

## What’s in it for Academia & Industry?

- A buggy SoC* framework for **<u>furthering innovation</u>**

   - Realistic security features, threat model, and security objectives

   - Vulnerabilities inspired by CVEs and real-world bugs

   - Open source and commercial tool support

- Benchmark for **<u>developing and testing HW security tools</u>**

   - Closest to commercial chip designs

- Participants **<u>gain hardware security assurance experience</u>**

   - Develop hacker mindset

   - Launchpad for researchers from adjacent areas (e.g., Firmware)

*SoC = System on a chip

# BHASIA @BlackHatEvents

## Slide 17

## System on a Chip (SoC)

- Data Confidentiality

   - Protect secrets from unauthorized access

- Data Integrity

   - Protect data modification by untrusted agents

- Availability

   - Protect against permanent damage to system

- Security features examples

   - Execution core & debug privilege checks

   - Access control

   - Memory encryption & integrity

   - Secure data erase

   - Power and thermal critical trip alerts

Core privilege
checks
Memory
Encryption
Thermal
Alert
Access control
Data Erase
JTAG
FW Secure boot Debug
Authentication
FW Filter
Volt, Freq,
Temp limits

# BHASIA @BlackHatEvents

## Slide 18

## Overview

## Introduction

Value of Organizing HW CTFs

How Hack@DAC is Unique

Organizing Hack@DAC Key Takeaways & Summary

# BHASIA @BlackHatEvents

## Slide 19

## Popular HW CTFs

###### **Application Algorithm**

- Popular HW CTFs are “closed-box”

###### **Programming Language Operating System Firmware MicroarchitectureMicroarchitecture Register Transfer Level Level(RTL) Gate Level**

**Transistor**

- Adopt a hacker-centric approach

   - Involve physical interaction with target chip

      - Probing input/output ports

      - Desoldering and reverse engineering attacks

      - Physical side channel attacks, etc.

   - No insights into the RTL code of the chip

- Very important research!

- Does not address “shift-left” challenge

# BHASIA @BlackHatEvents

## Slide 20

## Closed-box vs Open-box CTFs

- Hack@DAC is “Open-box”

   - Participants given a buggy SoC RTL

   - Finer grained scope

- Participants attempt to break security features

   - RTL Simulation/ Emulation

   - Formal Verification

   - RTL Static Analysis

   - Manual reviews

- **<u>Designer-centric approach</u>**

# BHASIA @BlackHatEvents

## Slide 21

## Overview

## Introduction

Value of Organizing HW CTFs

How Hack@DAC is Unique

Organizing Hack@DAC Key Takeaways & Summary

# BHASIA @BlackHatEvents

## Slide 22

## Hack@DAC – The Process

Participants Design Team Judges
1
5 Registration
Security features
Open-source design
Threat model
2
Bug list
3
Updated spec 7
6 Bug submission
Bug evaluation
Buggy design (RTL)
4
Tool support
Cloud Team
8 Scoreboard
9 10
FPGA support for
Commercial tools
emulation Winners announced
11 Opportunities on cloud

# BHASIA @BlackHatEvents

## Slide 23

## Selection of Target

- Survey various open-source hardware designs and pick full SoC

- Priority given to designs with support for hardware simulation (open-source tool support), stability

- Reduced Instruction Set Computing (RISCV) RISC-V architecture based SoCs

   - **<u>Pulpino</u>** -> **<u>Pulpissimo</u>** -> **<u>OpenPiton</u>** -> **<u>Open Titan</u>**

Boot
UART SPI
ROM
AXI 4
I$ D$
JTAG PLIC
CLINT
RISC-V Core

# BHASIA @BlackHatEvents

## Slide 24

## Adding Security Features to HW

HMAC SHA-256 - Counter-mode AES  - Contains keys, passwords,
Register locks and other sensitive config
information
SHA-256
HMAC AES SHA Fuse
DMA
Password
Proxy Kernel
- Fabric access control
- Enables virtual memory addresses and
memory isolation
- Password-based protection -ROM privilege switch  - FW running at machine mode performs
- Verification of HMAC of password from M to U self-test of crypto engines
- loads data from fuses into peripherals
1 https://github.com/pulp-platform/ariane
2 https://content.riscv.org/wp-content/uploads/2017/05/riscv-privileged-v1.10.pdf

# BHASIA @BlackHatEvents

## Slide 25

## Threat Modeling & Security Objectives

- Threat Model

- Security Objectives

   - Unprivileged code in core should not be able to compromise privilege level

   - Internal registers of crypto blocks should not be accessible from JTAG

# BHASIA @BlackHatEvents

## Slide 26

## Inserting Vulnerabilities

HMAC
- Counter-mode AES  - Contains keys, passwords,
Register locks SHA-256
and other sensitive config
SHA-256 information
HMAC AES SHA Fuse
DMA
Password
- Fabric access  Proxy Kernel - Enables virtual memory addresses
control and memory isolation
- FW running at machine mode
- Password-based protection -ROM privilege
performs self-test of crypto engines
- Verification of HMAC of  switch from M to U
Inserted Security Vulnerability  - loads data from fuses into
password
peripherals
Non-Inserted Security Vulnerability

###### Vulnerabilities inspired by:

- CVEs

- Security advisories

- Our experience

# BHASIA @BlackHatEvents

## Slide 27

## Advertisement

- Website updated with Call for Participation

- Advertised on social media

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blackhat Advertisement
¢ Website updated with Call for Participation
¢« Advertised on social media
HAGK
The
SILICON
i TEXAS“ intel SYNOPSYS’ [one
```

## Slide 28

## Competition: Phase 1

- Phase 1 is offline

- Participants have over 2 months to:

   - Analyze entry points

   - Identify assets based

   - Develop security test cases

   - Develop custom tools to detect bugs

   - Submit bugs for evaluation by judges

# BHASIA @BlackHatEvents

## Slide 29

## Submission and Scoring

##### Specific security feature that participants managed to bypass

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
blackhat Submission and Scoring
B <> D E F
Team name > Security feature > Finding > Location or code >
bypassed reference
Register Lock Control _In access control register wrapper file, reglk_ctrl _ piton/design/chip/tile/arian
signal unset signal is responsible for reading/writing the signal e/src/acct/acct_wrapper.s
for locked peripherals. All bits set to ‘1 of v, Line 96, 98 and 100
reglk_ctrl signal indicates the peripheral is locked
otherwise bits set to '0' indicate normal operation
Therefore, by default reglk_ctrl should always be
set high to prevent unauthorized access. We
found that only lower half of the reglk_ctrl is set
from 8-bit input reglk_ctrl_i and higher bits are set
to 0. Thus, all bits from 8-15 are set to 0 and
should not be accessed for any read/write
operation. In acc_wrapper.sy, at line 96, 98 and
Specific security feature that participants managed to bypass
```

## Slide 30

## Submission and Scoring

How was the vulnerability identified? - Simulation

- Formal Verification?

- Custom tool?

- Manual code review?

# BHASIA @BlackHatEvents

## Slide 31

## Submission and Scoring

##### What is the security impact of bypassing security feature?

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
blackhat Submission and Scoring
B «> D E F G H |
Team name > Security feature > Finding > Location or code > Detectionmethod = Security impact >
bypassed reference
other wrappers, all the
secure data can be read
out.
Register Lock Control _In access control register wrapper file, reglk_ctrl__ piton/design/chip’tile/arian Manual analysis + User This bug will lead to
signal unset signal is responsible for reading/writing the signal e/src/acct/acct_wrapper.s level assertion accessing peripheral
for locked peripherals. All bits set to ‘1 of v, Line 96, 98 and 100 generation + Formal device even when its
reglk_ctrl signal indicates the peripheral is locked property verification register is in locked
otherwise bits set to '0' indicate normal operation using Synopsys state (which ideally
Therefore, by default reglk_ctrl should always be VCStatic should have restricted
set high to prevent unauthorized access. We its access)
found that only lower half of the reglk_ctrl is set
from 8-bit input reglk_ctrl_i and higher bits are set
to 0. Thus, all bits from 8-15 are set to 0 and
should not be accessed for any read/write
operation. In acc_wrapper.sy, at line 96, 98 and
What is the security impact of bypassing security feature?
```

## Slide 32

## Submission and Scoring

##### Mitigation suggestions

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
blackhat Submission and Scoring
5 «> D E F G H ll 1 J
Team name > Security feature > Finding > Location or code > Detectionmethod = Security impact > Adversary profile = Proposed >
bypassed reference mitigation
other wrappers, all the
secure data can be read
out.
Register Lock Control _In access control register wrapper file, reglk_ctrl__ piton/design/chip’tile/arian Manual analysis + User This bug will lead to Unprivileged software at One line verilog change
signal unset signal is responsible for reading/writing the signal e/src/acct/acct_wrapper.s level assertion accessing peripheral user-level mode in acct_wrapper.sv:
for locked peripherals. All bits set to ‘1 of v, Line 96, 98 and 100 generation + Formal device even when its reglk_ctri[13] ->
reglk_ctrl signal indicates the peripheral is locked property verification register is in locked reglk_ctri[3]
otherwise bits set to '0' indicate normal operation using Synopsys state (which ideally
Therefore, by default reglk_ctrl should always be VCStatic should have restricted
set high to prevent unauthorized access. We its access)
found that only lower half of the reglk_ctrl is set
from 8-bit input reglk_ctrl_i and higher bits are set
to 0. Thus, all bits from 8-15 are set to 0 and
should not be accessed for any read/write
operation. In acc_wrapper.sy, at line 96, 98 and
Mitigation suggestions
```

## Slide 33

## Submission and Scoring

##### CVSS scoring details to determine severity of issue

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
blackhat Submission and Scoring
B <> D E F G H ll 1 J K L <
Team name > Security feature > Finding > Location or code > Detectionmethod = Security impact > Adversary profile = Proposed > CVSSv3.1 score > CVSSv3.1 Details =
bypassed reference mitigation and severity
other wrappers, all the
secure data can be read
out.
Register Lock Control _In access control register wrapper file, reglk_ctrl__ piton/design/chip’tile/arian Manual analysis + User This bug will lead to Unprivileged software at One line verilog change Medium (6.1) CVSS:3.1/AV:LIAC:L/P
signal unset signal is responsible for reading/writing the signal e/src/acct/acct_wrapper.s level assertion accessing peripheral user-level mode in acct_wrapper.sv: R:L/UE:N/S:U/C:LILHIA:
for locked peripherals. All bits set to ‘1 of v, Line 96, 98 and 100 generation + Formal device even when its reglk_ctri[13] -> N/RC:C
reglk_ctrl signal indicates the peripheral is locked property verification register is in locked reglk_ctri[3] Attack vector: Local. A
otherwise bits set to '0' indicate normal operation using Synopsys state (which ideally person having
Therefore, by default reglk_ctrl should always be VCStatic should have restricted read/write/execute
set high to prevent unauthorized access. We its access) access on the SoC can
found that only lower half of the reglk_ctrl is set mount the attack
from 8-bit input reglk_ctrl_i and higher bits are set Attack complexity: Low.
to 0. Thus, all bits from 8-15 are set to 0 and An exploit code
should not be accessed for any read/write developed can sureshot
operation. In acc_wrapper.sy, at line 96, 98 and obtain access control of
CVSS scoring details to determine severity of issue
```

## Slide 34

## Submission and Scoring

Scoring based on:

- Validity of issue

Special award for “cool” finds!

- Novelty of methodology used

- Correctness of security impact, mitigation, CVSS

- Conference theme based bonus

   - New tool bonus at DAC

Manual vs Automated scoring

- Exploit bonus at USENIX Security

# BHASIA @BlackHatEvents

## Slide 35

## Competition: Phase 2 (Finals)

- Top 10 teams invited to participate in finals

- Phase 2 live at the conference

- Partnership with Synopsys

   - All necessary tools hosted on Synopsys cloud

   - Buggy design ported to cloud

   - Tool trainings provided to all finalists

- Travel grants to US-based finalists to attend in person

- 33 hours of competition

# BHASIA @BlackHatEvents

## Slide 36

## Competition: Phase 2 (Finals)

# BHASIA @BlackHatEvents

Image: “Hacking SoC IP Under Pressure”, SemiEngineering 2018 source

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
ASIA 2024
Hack@DAC'19 Beta Scoreboard : Live
Team name Points
Hackin' Aggies* 465
NOPS 330
Always@Posedge 290
NotATrojan 276
Alpha4 163
.thackamole:. 144
SEC 115
Team 11 104
52
Tribe 28
CCNY 15
15
Image: “Hacking SoC IP Under Pressure”, SemiEngineering 2018
```

## Slide 37

## Competition: Phase 2 (Finals) Winners Honored Publications

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
piSek hat Competition: Phase 2 (Finals)
ASIA 2024
DesignStlest
‘ALEXANDER TORRES 20271
€ Special Issue on Hack@DAC
* SoC Security Evaluation: Reflections on Methodology and Tooling
* Hardware Penetration Testing Knocks Your SoCs Off
* Hunting Security Bugs in SoC Designs: Lessons Learned
* Texas A&M Hackin’ Aggies’ Security Verification Strategies for the 2019 Hack@DAC Competition
Tutoria’
* Merged Logic and Memory Fabrics for Accelerating Machine Learning Workloads
General Interest
* Real-Time Hardware Implementation of ARM CoreSight Trace Decoder
CEMA a tttc
IEEE
```

## Slide 38

## So Far..

- Extended to USENIX Security (Hack@SEC) and CHES (Hack@CHES)

- 300+ teams participated from all over the world; 1000+ participants

   - Strong participation from Asian teams!

- Industry participation too!

- Past winners now working in hardware security roles at top companies

# BHASIA @BlackHatEvents

## Slide 39

## Overview

## Introduction

Value of Organizing HW CTFs

How Hack@DAC is Unique

Organizing Hack@DAC Key Takeaways & Summary

# BHASIA @BlackHatEvents

## Slide 40

## Recap of 3 Top Challenges

Awareness of
Hardware
Common
Weaknesses

Security-Aware
Design
Automation

“Shift-Left” to
Detect & Fix
Bugs in RTL

# BHASIA @BlackHatEvents

## Slide 41

## Awareness of HW Weaknesses MITRE Hardware CWE

**<u>https://cwe.mitre.org</u>**

- 75+/110 CWE entries contributed by Intel

- • Hack@DAC vulnerability and mitigation examples now added to several CWE entries

# BHASIA @BlackHatEvents

## Slide 42

### Security-Aware Tooling & Bug Detection

- Framework can be used to build new tools/ flows/ methodologies to detect bugs

   - <u>Security Test Case Generation and Bug Patching using LLMs</u>

      - (Security) Assertions by Large Language Models _(IEEE TIFS 2024)_

`o` Examining Zero Shot Vulnerability Repair with Large Language Models (IEEE Security and Privacy 2023) `o` Fixing Hardware Security Bugs with Large Language Models _(arXiv)_

   - <u>Formal Verification</u>

      - Sylvia: Countering the Path Explosion Problem in the Symbolic Execution of Hardware Designs _(FMCAD 2023)_

   - <u>Static Analysis</u>

      - Don’t CWEAT It: Toward CWE Analysis Techniques in Early Stages of Hardware Design _(IEEE/ACM ICCAD 2022)_

   - <u>Concolic Testing</u>

      - RTL-ConTest: Concolic Testing on RTL for Detecting Security Vulnerabilities _(IEEE TCAD 2022)_

   - <u>Hardware Information Flow Tracking</u>

      - Cell-IFT: Leveraging Cells for Scalable & Precise Dynamic Information Flow Tracking in RTL _(USENIX Security 2022)_

- **<u>All these work on RTL!</u>**

# BHASIA @BlackHatEvents

## Slide 43

## Key Takeaways for Academia

- Hack@DAC SoC framework

   - Realistic threat model and security objectives

   - Closest available to commercial chip designs

   - Uncover new classes of security vulnerabilities

- Get invaluable hardware security assurance skills!

- Mimic security teams at a chip design company

- Develop a hacker mindset

Hack@DAC 2018 finals at San Francisco, CA

# BHASIA @BlackHatEvents

Image: “Hacking SoC IP Under Pressure”, SemiEngineering 2018 source

## Slide 44

## Takeaways for Industry

- Improve in-house security assurance best practices

   - Exposure to new kinds of weaknesses

   - Planning for survivability features

   - Easier for functional verification teams to pick up security assurance

- New tools for identifying weakness classes

   - Publish guides on detection of classes of hardware security weaknesses

- Add security capabilities to today’s functional tools

   - Address gaps of today’s security verification tools to detect classes of vulnerabilities

# BHASIA @BlackHatEvents

## Slide 45

## Media Coverage

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
blackhat Media Coverage
ASIA 2024
YNYEVOoOrPsS>
FE Times Q)) osu CYBER DEFENSE
Capture-the-Flag Competitions Need to Include Learning Hardware Security Via Capture-The- Why Do We Need a Standardized Framework to
Hardware Flag Competitions Enumerate Hardware Security Weaknesses?
te C a S D 'S, ctl | VE rath SEMICONDUCTOR En
..4 unique'perspective on technology ~ H ICG k@ DAC:
Winning Strategies!
means
Intel Hardware CTF Competitions Drive Hacking SoC IP Under Pressure
Innovation for Next-Gen Secure Computing cyber
security hosted by
Platforms inside Camille Morhardt
```

## Slide 46

## Black Hat Sound Bytes

- Increased HW Security Awareness

   - _<u>MITRE HW CWE</u>_

- _Corpus of weaknesses and code examples_

- • Open-sourced buggy SoC design

   - _Realistic security features_

   - _CVE-inspired vulnerabilities_

   - _Complexity matching commercial chips_

#### **Register for Hack@DAC 2024**

- Innovations in HW security tooling

   - _Tools that detect and patch bugs at RTL_

**<u>Website</u>** : https://hackthesilicon.com/ **<u>Email</u>** : hackatevent@gmail.com

- Participants developed hacker mindset

# BHASIA @BlackHatEvents

## Slide 47

## System on a Chip (SoC)

- Data Confidentiality

   - Protect secrets from unauthorized access

- Data Integrity

   - Protect data modification by untrusted agents

- Availability

   - Protect against permanent damage to system

- Security features examples

   - Execution core & debug privilege checks

   - Access control

   - Memory encryption & integrity

   - Secure data erase

   - Power and thermal critical trip alerts

Core privilege
checks
Memory
Encryption
Thermal
Alert
Access control
Data Erase
JTAG
FW Secure boot Debug
Authentication
FW Filter
Volt, Freq,
Temp limits

# BHASIA @BlackHatEvents
