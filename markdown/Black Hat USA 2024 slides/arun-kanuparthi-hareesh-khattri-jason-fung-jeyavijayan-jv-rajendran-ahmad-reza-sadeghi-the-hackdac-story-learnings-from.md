---
title: "The Hack@DAC Story Learnings from Organizing the World's Largest Hardware Hacking Competition"
speakers: ["Arun Kanuparthi", "Hareesh Khattri", "Jason Fung", "Jeyavijayan JV Rajendran", "Ahmad-Reza Sadeghi"]
conference: "Black Hat"
conference_full: "Black Hat USA 2024"
edition: "USA"
year: 2024
source_pdf: "Black Hat USA 2024 slides/Arun Kanuparthi & Hareesh Khattri & Jason Fung & Jeyavijayan JV Rajendran & Ahmad-Reza Sadeghi_The Hack@DAC Story Learnings from Organizing the World's Largest Hardware Hacking Competition.pdf"
pages: 50
sha256: "49b60f600683efedbaaaf709676bb8b6bb6c0d8a6866d976b9b0494763741088"
text_chars: 24522
ocr_pages: 9
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:47:44Z"
---
# The Hack@DAC Story Learnings from Organizing the World's Largest Hardware Hacking Competition

**Speakers:** Arun Kanuparthi, Hareesh Khattri, Jason Fung, Jeyavijayan JV Rajendran, Ahmad-Reza Sadeghi  
**Conference:** Black Hat USA 2024  
**Source:** `Black Hat USA 2024 slides/Arun Kanuparthi & Hareesh Khattri & Jason Fung & Jeyavijayan JV Rajendran & Ahmad-Reza Sadeghi_The Hack@DAC Story Learnings from Organizing the World's Largest Hardware Hacking Competition.pdf` (50 pages)

## Slide 1

The Hack@DAC* Story: Learnings from Organizing the World’s Largest Hardware Hacking Competition **<u>Arun Kanuparthi</u>** , Hareesh Khattri, Jason Fung (Intel Corporation, USA) JV Rajendran (Texas A&M University, USA), Ahmad-Reza Sadeghi (TU Darmstadt, Germany)

*Design Automation Conference

#BHUSA @BlackHatEvents

## Slide 2

# The Team

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

#BHUSA @BlackHatEvents

*Special Interest Group (SIG)

## Slide 3

# Full Team

#### **<u>Texas A&M University</u>**

- Rahul Kande*

- Chen Chen*

- Patrick Haney

- Garrett Persyn

- Bhagyaraja Adapa

#### **<u>TU Darmstadt</u>**

- Mohammadreza Rostami*

- Ghada Dessouky

- David Gens

- Pouya Mahmoody

- Shaza Zeitouni

#### **<u>Synopsys</u>**

- Shylaja Sen*

- Yann Antonioli*

- Jagminder Chugh

- Meriav Nitzan

* Part of most recent team

#BHUSA @BlackHatEvents

## Slide 4

# Overview

# Introduction

Value of Organizing HW CTFs How Hack@DAC is Unique

Organizing Hack@DAC Key Takeaways & Summary

#BHUSA @BlackHatEvents

## Slide 5

# Overview

# Introduction

Value of Organizing HW CTFs

How Hack@DAC is Unique

Organizing Hack@DAC Key Takeaways & Summary

#BHUSA @BlackHatEvents

## Slide 6

# Computing Stack - Refresher

**Application Algorithm Programming Language Operating System Firmware MicroarchitectureMicroarchitecture Register Transfer Hardware Level Level(RTL) Gate Level Transistor**

#BHUSA @BlackHatEvents <u>Image3 Source Image4 Source</u>

## Slide 7

# Computing Stack - Refresher

**Application Algorithm**

**Application Algorithm Programming Language Operating System Firmware MicroarchitectureMicroarchitecture Register Transfer Level Level(RTL) Gate Level Transistor**

Microarchitecture

Gate Level

assign ADD_result = reg_A + reg_B; assign SUB_result = reg_A – reg_B; assign AND_result = reg_A & reg_B;

… if (IR_opcode_field == 0) case (IR_function_field)

6’b100000: ALU_result <= ADD_result; 6’b100010: ALU_result <= SUB_result; 6’b100100: ALU_result <= AND_result;

Register Transfer Level (RTL)

Transistor

#BHUSA @BlackHatEvents <u>Image3 Source Image4 Source</u>

## Slide 8

Race to the Bottom of the Stack **<u>Challenge #1</u>** : Limited Awareness of HW Security Weaknesses **Application Algorithm Programming Language Operating System Firmware MicroarchitectureMicroarchitecture** Bugs in hardware could be exploitable by software! **Register Transfer Level Level(RTL) Gate Level**

Bugs in hardware could be exploitable by software!

**Transistor**

_USENIX Security 2019_

#BHUSA @BlackHatEvents

## Slide 9

# Tools for Security – SW vs HW

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

#BHUSA @BlackHatEvents

## Slide 10

# System on a Chip (SoC) Security

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

- Typical Security Objectives for Assets

   - Data Confidentiality

   - Data Integrity

   - Availability

- Example Security Features

   - Execution core & debug privilege checks

   - Access control

   - Memory encryption & integrity

   - Secure data erase

   - Power and thermal critical trip alerts

#BHUSA @BlackHatEvents

## Slide 11

# HW Vulnerability Example – Key Clear

|**Asset (Objective)**|Secret Keys in AES block (Confidentiality)|
|---|---|
|**Threat**|HW debug adversary extracts keys|
|**Mitigation**|Return all 0s for all reads when chip is in debug mode|

When in debug mode, return 0 when keys are read

debug_mode is not checked for key_big2

Attacker can extract key_big2 during debug

<u>https://github.com/PrincetonUniversity/openpiton</u>

#BHUSA @BlackHatEvents

## Slide 12

# HW Vulnerability Example – Key Leak

|Asset (Objective)|Secret Keys in AES block (Confidentiality)|
|---|---|
|Threat|Keys should not be readable by untrusted software code|
|Mitigation|A read lock signal (when enabled) returns ‘0’ when keys are read by software|

Logic to read the key. If lock is set, reads return ‘0’ When valid read is detected (en is high), key0 is passed to read data without checking for lock

Key0 leaks to attacker observable interface

Expected Path through AES engine Unexpected/hidden path leaks key

<u>https://github.com/PrincetonUniversity/openpiton</u>

#BHUSA @BlackHatEvents

## Slide 13

Tools for Security – SW vs HW **<u>Challenge #2</u>** : Need for Security-Aware Design Automation Tools

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

#BHUSA @BlackHatEvents

## Slide 14

# Cost of Fixing Bugs

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

#BHUSA @BlackHatEvents

## Slide 15

# Motivation for Hack@DAC

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

Hack@DAC

- Hackathons, trainings

- Open-source hardware as target?

- What about hardware CTF?

#BHUSA @BlackHatEvents

## Slide 16

# Overview

# Introduction

Value of Organizing HW CTFs How Hack@DAC is Unique

Organizing Hack@DAC Key Takeaways & Summary

#BHUSA @BlackHatEvents

## Slide 17

# Fostering Awareness for HW Security

- Continuous race between attackers and defenders

- Defenders need to up their game!

- Hardware CTFs foster greater awareness about

   - Common hardware security weaknesses

   - Constraints of chip design teams

#BHUSA @BlackHatEvents

Image <u>source</u>

## Slide 18

# What’s in it for Academia & Industry?

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

#BHUSA @BlackHatEvents

## Slide 19

# Overview

# Introduction

Value of Organizing HW CTFs

How Hack@DAC is Unique

Organizing Hack@DAC Key Takeaways & Summary

#BHUSA @BlackHatEvents

## Slide 20

# Popular HW CTFs

#### **Application Algorithm**

- Popular HW CTFs are “closed-box”

#### **Programming Language Operating System Firmware MicroarchitectureMicroarchitecture Register Transfer Level Level(RTL) Gate Level**

**Transistor**

- Adopt a hacker-centric approach

   - Involve physical interaction with target chip

      - Probing input/output ports

      - Desoldering and reverse engineering attacks

      - Physical side channel attacks, etc.

   - No insights into the RTL code of the chip

- Very important research!

- Does not address “shift-left” challenge

#BHUSA @BlackHatEvents

## Slide 21

# Closed-box vs Open-box CTFs

- Hack@DAC is “Open-box”

   - Participants given a buggy SoC RTL

   - Finer grained scope

- Participants attempt to break security features

   - RTL Simulation/ Emulation

   - Formal Verification

   - RTL Static Analysis

   - Manual reviews

- **<u>Designer-centric approach</u>**

#BHUSA @BlackHatEvents

## Slide 22

# Overview

# Introduction

Value of Organizing HW CTFs

How Hack@DAC is Unique

Organizing Hack@DAC Key Takeaways & Summary

#BHUSA @BlackHatEvents

## Slide 23

# Hack@DAC – The Process

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

#BHUSA @BlackHatEvents

## Slide 24

# Selection of Target

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

#BHUSA @BlackHatEvents

## Slide 25

# Adding Security Features to HW

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

#BHUSA @BlackHatEvents

## Slide 26

# Threat Modeling & Security Objectives

- Threat Model

- Security Objectives

   - Unprivileged code in core should not be able to compromise privilege level

   - Internal registers of crypto blocks should not be accessible from JTAG

#BHUSA @BlackHatEvents

## Slide 27

# Inserting Vulnerabilities

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

##### Vulnerabilities inspired by:

- CVEs

- Security advisories

- Our experience

#BHUSA @BlackHatEvents

## Slide 28

# Advertisement

- Website updated with Call for Participation

- Advertised on social media

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pSxnat Advertisement
USA 2024
¢ Website updated with Call for Participation
¢ Advertised on social media
HAGK
The
SILICON
ey 745" intel Synopsys aE
```

## Slide 29

# Competition: Phase 1

- Phase 1 is offline

- Participants have over 2 months to:

   - Analyze entry points

   - Identify assets

   - Develop security test cases

   - Develop custom tools to detect bugs

   - Submit bugs for evaluation by judges

- Extended duration allows for equal access to participants from various backgrounds.

#BHUSA @BlackHatEvents

## Slide 30

# Submission and Scoring

### Specific security feature that participants managed to bypass

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
blackhat Submission and Scoring
USA 2024
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

## Slide 31

# Submission and Scoring

How was the vulnerability identified? - Simulation

- Formal Verification?

- Custom tool?

- Manual code review?

#BHUSA @BlackHatEvents

## Slide 32

# Submission and Scoring

### What is the security impact of bypassing security feature?

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
blackhat Submission and Scoring
USA 2024
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

## Slide 33

# Submission and Scoring

### Mitigation suggestions

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
blackhat Submission and Scoring
USA 2024
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

## Slide 34

# Submission and Scoring

### CVSS scoring details to determine severity of issue

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
blackhat Submission and Scoring
USA 2024
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

## Slide 35

# Submission and Scoring

Scoring based on:

- Validity of issue

Special award for “cool” finds!

- Novelty of methodology used

- Correctness of security impact, mitigation, CVSS

- Conference theme based bonus

   - New tool bonus at DAC

Manual vs Automated scoring

- Exploit bonus at USENIX Security

#BHUSA @BlackHatEvents

## Slide 36

# Competition: Phase 2 (Finals)

- Top 10 teams invited to participate in finals

- Phase 2 live at the conference

- Partnership with Synopsys

   - All necessary tools hosted on Synopsys cloud

   - Buggy design ported to cloud

   - Tool trainings provided to all finalists

- Travel grants to US-based finalists to attend in person

- Duration of 48 hours

#BHUSA @BlackHatEvents

## Slide 37

# Competition: Phase 2 (Finals)

Image: “Hacking SoC IP Under Pressure”, SemiEngineering 2018 source

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biackhat Competition: Phase 2 (
Live Scoreboard
Hack@DAC'19 Beta Scoreboard : Live
Team name Points
Hackin' Aggies* 465 465
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

## Slide 38

# Competition: Phase 2 (Finals) Winners Honored Publications

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pistkhat Competition: Phase 2 (Finals) »
USA 2024
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

## Slide 39

# So Far..

- Extended to USENIX Security (Hack@SEC) and CHES (Hack@CHES)

- 300+ teams participated from all over the world; 1000+ participants

- Industry participation too!

- Past winners now working in hardware security roles at top companies

#BHUSA @BlackHatEvents

## Slide 40

# Overview

# Introduction

Value of Organizing HW CTFs

How Hack@DAC is Unique

Organizing Hack@DAC Key Takeaways & Summary

#BHUSA @BlackHatEvents

## Slide 41

# Recap of 3 Top Challenges

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

#BHUSA @BlackHatEvents

## Slide 42

# Awareness of HW Weaknesses

MITRE Hardware CWE **<u>https://cwe.mitre.org</u>**

- 75+/110 CWE entries contributed by Intel

- Hack@DAC vulnerability and mitigation examples now added to several CWE entries

- ”

- • “Hardware Security Failure Scenarios

#BHUSA @BlackHatEvents

## Slide 43

## Security-Aware Tooling & Bug Detection

- <u>Security Test Case Generation and Bug Patching using GenAI/ LLMs</u>

   - (Security) Assertions by Large Language Models _(IEEE TIFS 2024)_

   - Examining Zero Shot Vulnerability Repair with Large Language Models _(IEEE Security and Privacy 2023)_

   - Fixing Hardware Security Bugs with Large Language Models _(arXiv)_

   - On Prompting Hardware Security Bug Code Fixes by Prompting Large Language Models _(IEEE TIFS 2024)_

   - DIVAS: An LLM-based End to End Framework for SoC Security Analysis and Policy-based Protection _(arXiv)_

- <u>Formal Verification</u>

   - Sylvia: Countering the Path Explosion Problem in the Symbolic Execution of Hardware Designs _(FMCAD 2023)_

   - `o` All Artificial, Less Intelligence: GenAI Through the Lens of Formal Verification _(arXiv)_

- <u>Static Analysis</u>

   - Don’t CWEAT It: Toward CWE Analysis Techniques in Early Stages of Hardware Design _(IEEE/ACM ICCAD 2022)_

- <u>Concolic Testing</u>

   - RTL-ConTest: Concolic Testing on RTL for Detecting Security Vulnerabilities _(IEEE TCAD 2022)_

- <u>Hardware Information Flow Tracking</u>

`o` Cell-IFT: Leveraging Cells for Scalable & Precise Dynamic Information Flow Tracking in RTL _(USENIX Security 2022)_

#BHUSA @BlackHatEvents

## Slide 44

# Key Takeaways for Academia

- Hack@DAC SoC framework

   - Realistic threat model and security objectives

   - Closest available to commercial chip designs

   - Uncover new classes of security vulnerabilities

- Get invaluable hardware security assurance skills!

   - Mimic security teams at a chip design company

   - Develop a hacker mindset

- Competition format

   - provides equal access to participants from diverse backgrounds

Hack@DAC 2018 finals at San Francisco, CA

   - Strong technical female participation

- Facilitates participation from various geos/ time zones

#BHUSA @BlackHatEvents

Image: “Hacking SoC IP Under Pressure”, SemiEngineering 2018 source

## Slide 45

# Takeaways for Industry

- Improve in-house security assurance best practices

   - Exposure to new kinds of weaknesses

   - Planning for survivability features

   - Easier for functional verification teams to pick up security assurance

- New tools for identifying weakness classes

   - Publish guides on detection of classes of hardware security weaknesses

- Add security capabilities to today’s functional tools

   - Address gaps of today’s security verification tools to detect classes of vulnerabilities

#BHUSA @BlackHatEvents

## Slide 46

# Media Coverage

Intel Harnesses Hackathons to Tackle Hardware Vulnerabilities

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pi&xnat Media Coverage
USA 2024
FE Times Q)) osu CYBER DEFENSE
YNEVOoOPrPsS
Capture-the-Flag Competitions Need to Include Learning Hardware Security Via Capture-The- Why Do We Need a Standardized Framework to
Hardware Flag Competitions Enumerate Hardware Security Weaknesses?
techspective 2BBES SewiconoucTor ENOINEERING DARKREADING
..a unique'perspective on technology SB Be Cm inmne ron ne re ey =
Intel Hardware CTF Competitions Drive Hacking SoC IP Under Pressure Intel Harnesses Hackathons to Tackle
Innovation for Next-Gen Secure Computing Hardware Vulnerabilities
Platforms
```

## Slide 47

# Black Hat Sound Bytes

Hack@DAC has resulted in:

**<u>Contact</u>**

- Increased HW Security Awareness

**<u>Website</u>** : https://hackthesilicon.com/ **<u>Email</u>** : hackatevent@gmail.com

   - _<u>MITRE HW CWE (https://cwe.mitre.org)</u>_

- _Corpus of weaknesses and code examples_

- • Availability of Open-sourced buggy SoCs

   - _Realistic security features_

   - _CVE-inspired vulnerabilities_

   - _Complexity matching commercial chips_

- Innovations in HW security tooling

   - _Tools that detect and patch bugs at RTL_

- Participants developed hacker mindset

#BHUSA @BlackHatEvents

## Slide 48

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Awe
Q
| I
black hat —
USA 2
O24
```

## Slide 49

# HW Vulnerability Example - Locks

Lock signal for sensitive registers Security sensitive register core_lock_reg is not locked

Attacker can overwrite security sensitive register

#BHUSA @BlackHatEvents

<u>https://github.com/PrincetonUniversity/openpiton</u>

## Slide 50

# HW Vulnerability Example - Debug

State machine implementing password authentication logic for secure debug access When opcode is DTM_PASS (for entering password), state change changes to WRITE Attacker wants to enter password – but gets write access to chip internals through debug interface

When in debug mode, return 0 when keys are read debug_mode is not checked for key_big2 Attacker can extract key_big2 during debug

#BHUSA @BlackHatEvents

<u>https://github.com/PrincetonUniversity/openpiton</u>
