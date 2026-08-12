---
title: "How to Secure Unique Ecosystem Shipping 1 Billion+ Cores"
speakers: ["Adam Zabrocki", "Marko Mitic"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Adam Zabrocki&Marko Mitic_How to Secure Unique Ecosystem Shipping 1 Billion+ Cores.pdf"
pages: 90
sha256: "fb64b15eb8554b18b166665951774b09f7cf11a1482cd2e5d3e85d6a38b3772b"
text_chars: 45204
ocr_pages: 2
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T22:48:32Z"
---
# How to Secure Unique Ecosystem Shipping 1 Billion+ Cores

**Speakers:** Adam Zabrocki, Marko Mitic  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Adam Zabrocki&Marko Mitic_How to Secure Unique Ecosystem Shipping 1 Billion+ Cores.pdf` (90 pages)


## Slide 1

How to Secure Unique Ecosystem Shipping 1 Billion+ Cores?

Adam ‘pi3’ Zabrocki, Marko Mitic

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
- bladk hat |
on BRIEFINGS
AUGUST 6-7, 2025
MANDALAY BAY / LAS VEGAS
How to Secure Unique Ecosystem
Shipping 1 Billion+ Cores?
Adam ‘pi3’ Zabrocki, Marko Mitic
```

## Slide 2

### /usr/bin/whoarewe

Private contact: <u>http://pi3.com.pl pi3@pi3.com.pl</u> Twitter: <u>@Adam_pi3</u>

Private contact: <u>markomitic.net linkedin.com/markomitic</u> Twitter: <u>@markomitic</u>

##### Adam ‘pi3’ Zabrocki:

##### Marko Mitic

- NVIDIA (currently – Director of Offensive Security)

   - Leading Offensive Security Research efforts

   - RISC-V (Vice-Chair of J-ext, author: PM, HW CFI, MTE, more)

   - Security architect for GPU and next-gen NVIDIA products

   - Software Security Architect & System Software Manager at NVIDIA

      - Leads NVIDIA’s Core RISC-V team

   -

   - GPU Product Security & Risk Officer, PSIRT lead

- Phrack author

- Bughunter (Hyper-V, KVM, RISC-V ISA, Intel uCode, Linux kernel, FreeBSD, OpenSSH, Apache, gcc SSP/ProPolice, more) – CVEs

- Creator and a developer of Linux Kernel Runtime Guard (LKRG)

- Speaker at BlackHat, DEF CON, BSides, Confidence, Open-Source Tech more

- The Pwnie Awards nominee (x2)

#BHUSA @BlackHatEvents

## Slide 3

### Why this talk?

#BHUSA @BlackHatEvents

## Slide 4

### Why this talk?

#BHUSA @BlackHatEvents

## Slide 5

### Why this talk?

#BHUSA @BlackHatEvents

## Slide 6

### Why this talk?

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisekchat >
BRIEFINGS
( Yi,
MLL
NVIDIA’ Tegra’ XT
i
#BHUSA @BlackHatEvents
```

## Slide 7

Why this talk? **“There is nothing hidden under the sun”**

#BHUSA @BlackHatEvents

## Slide 8

### Why this talk?

- Each NVIDIA chipset may include ~10-50 microcontrollers (MCUs)

   - Function Level Controllers (e.g., Codecs, Memory Controllers, Chip2Chip Interfaces, more)

   - Chip/System Level Control (e.g., Resource Management, PMU, Security, more)

   - Data Processing including packet routing in networking

#BHUSA @BlackHatEvents

## Slide 9

### Why this talk?

- Each NVIDIA chipset may include ~10-50 microcontrollers (MCUs)

   - Function Level Controllers (e.g., Codecs, Memory Controllers, Chip2Chip Interfaces, more)

   - Chip/System Level Control (e.g., Resource Management, PMU, Security, more)

   - Data Processing including packet routing in networking

- Legacy Falcon (internal proprietary RISC ISA) were difficult to scale

   - Sufficient at that time… requirements and expectation changed

   - Security layer needed to be updated to fulfill modern and future(!) expectations

#BHUSA @BlackHatEvents

## Slide 10

### Why this talk?

- Each NVIDIA chipset may include ~10-50 microcontrollers (MCUs)

   - Function Level Controllers (e.g., Codecs, Memory Controllers, Chip2Chip Interfaces, more)

   - Chip/System Level Control (e.g., Resource Management, PMU, Security, more)

   - Data Processing including packet routing in networking

- Legacy Falcon (internal proprietary RISC ISA) were difficult to scale

   - Sufficient at that time… requirements and expectation changed

   - Security layer needed to be updated to fulfill modern and future(!) expectations

- NVIDIA chip must meet the demand

   - Not only AI workloads is booming – NVIDIA processors are crucial

   - Opportunity to redesign the ecosystem

      - In secure manner that will be scalable in the future!

#BHUSA @BlackHatEvents

## Slide 11

### Why RISC-V

#BHUSA @BlackHatEvents

## Slide 12

### Why RISC-V

Retire proprietary Falcon architecture

#BHUSA @BlackHatEvents

## Slide 13

### Why RISC-V

Retire proprietary Falcon architecture

Performance

#BHUSA @BlackHatEvents

## Slide 14

### Why RISC-V

Retire proprietary Falcon architecture

Performance

Enable fast & flexible HW/SW co-design, custom extensions

#BHUSA @BlackHatEvents

## Slide 15

### Why RISC-V

Retire proprietary Falcon architecture

Performance

Enable fast & flexible HW/SW co-design, custom extensions

Layered security isolation primitives

#BHUSA @BlackHatEvents

## Slide 16

### Why RISC-V

Retire proprietary Falcon architecture

Performance

Enable fast & flexible HW/SW co-design, custom extensions **<u>Layered security isolation primitives</u>**

#BHUSA @BlackHatEvents

## Slide 17

### Why RISC-V

Retire proprietary Falcon architecture

Performance

Enable fast & flexible HW/SW co-design, custom extensions **<u>Layered security isolation primitives</u>**

Common configurable foundation for all MCUs across all products

#BHUSA @BlackHatEvents

## Slide 18

### Why RISC-V

Retire proprietary Falcon architecture

Performance

Enable fast & flexible HW/SW co-design, custom extensions **<u>Layered security isolation primitives</u>**

Common configurable foundation for all MCUs across all products

Scale up and out and build only for what is needed

#BHUSA @BlackHatEvents

## Slide 19

### RISC-V Cores & Apps in NVIDIA

Feynman

Rubin Blackwell

~10-50 RISC-V cores per GPU ~1 Billion RISC-V cores shipping in 2024 NVIDIA chips

Turing

2018

Hopper Ada Ampere 2020 2022

2024

HW/SW Design

Security Hardening

Performance & Scaling

IP Adoption

#BHUSA @BlackHatEvents

## Slide 20

### From Silicon to Software: Foundational elements for Secure Execution

#BHUSA @BlackHatEvents

## Slide 21

### From Silicon to Software: Foundational elements for Secure Execution

- Memory Protection and Isolation

   - HW Root of Trust

- Hardware Security Mitigations

   - Secure Storage

- BootROM

   - Crypto Accelerator

- TEE

   - Tamper Detection

- (TEE) Operating Systems

   - Crypto Libraries

- Formal Verification

   - Key Management

- OSR

   - Secure Software Development Lifecycle

- …

- …

#BHUSA @BlackHatEvents

## Slide 22

### From Silicon to Software: Foundational elements for Secure Execution

- Memory Protection and Isolation

   - HW Root of Trust

- Hardware Security Mitigations

   - Secure Storage

- BootROM

   - Crypto Accelerator

- TEE

   - Tamper Detection

- (TEE) Operating Systems

   - Crypto Libraries

- Formal Verification

   - Key Management

- OSR

   - Secure Software Development Lifecycle

- …

- …

#BHUSA @BlackHatEvents

## Slide 23

### RISC-V Intro – Privilege Modes

IO-PMP
RISCV Core
SW
Control Bus
U mode Task Task
S mode OS
Devices
NV MPU
IO-PMP
M mode
M-mode SW
PMP
Data Bus
PMA
I/O
Memory

RISC-V Modes
Level Name Abbr.
0 User/Application U
1 Supervisor S
2 Hypervisor HS
3 Machine M

Supported Combinations of Modes
1 M
2 M. U
3 M, S, U
4 M, HS, (V)S, (V)U

- **Each mode has Control and Status Registers (CSRs)**

#BHUSA @BlackHatEvents

## Slide 24

### RISC-V Intro – Memory Protection

- **PMP – Physical Memory Protection**

IO-PMP
RISCV Core
SW
Control Bus
U mode Task Task
S mode OS
Devices
NV MPU
IO-PMP
M mode
M-mode SW
PMP
Data Bus
PMA
I/O
Memory

- **IO-PMP – PMP for I/O and devices**

- • **Ability to lock a region until reset**

Locked Region
User Mode Context
(RWX)
Shared data
eXecute only
S-mode context

#BHUSA @BlackHatEvents

## Slide 25

### NVRISC-V

Local Control Plane

External Interrupt
Interrupt Controller
NV-RISCV
Trace Buffer
NV MPU
In-Circuit Debug
PMP
PMA
Boot and Control
Registers
L1 Cache
Local Data Plane

NV-RISCV32 NV-RISCV64 NV-RVV
RV32I-MU RV64I-MSU RV32I-MU
Multiplication Multiplication Multiplication
Compression Compression Compression
Float Float Float
Bit manipulation Vector
Atomics
In Order Out of Order NV-RISCV32 +
Single Issue Dual Issue vector extension
1.8 CM/MHz 5 CM/MHz (1024-bit)
1.8 GHz 2 GHz
SMP
Examples of NVIDIA custom security extensions
Secure Debug with ICD
ROM memory protection extension
DCLS
ePMP (draft 0.7)
TBI/PM (Draft 0.7)
Secure I/0 (Exception on bus error)
Halt extension (via CSR)
NV Priv. level extension (via CSR)

#BHUSA @BlackHatEvents

## Slide 26

### Peregrine

NVRISCV + Peripheral devices Single and multi-core MCUs RISC-V extensions may be present or not Configurable peripherals (crypto, channels) Cache and TCM sizes parameterized

Optional DCLS (Dual Core Lock Step)

Interrupt
TRNG Key Store Timer
Controller
Local Control Plane Control
Plane
NVRISCV Core RSA/
AES  Hashing
DMA PKA
Engine Engine
Engine
ICACHE DCACHE
Local Data Plane Memory
System
ROM ITCM DTCM
Peregrine

#BHUSA @BlackHatEvents

## Slide 27

### One Core Strategy – Peregrine Ecosystem

- Unified embedded HW and SW across all NVIDIA products

Partitions
Confidential Compute vGPU DRM
Measurement &
Secure Boot Power management
Attestation
NVRISCV SDK
Partition OS Baremetal Applications
Separation Kernel
Boot Plugin
or
BootROM
Peregrine IP
RISC-V Core(s)

SPARK

Offsec

#BHUSA @BlackHatEvents

## Slide 28

### One Core Strategy – Peregrine Ecosystem

- Unified embedded HW and SW across all NVIDIA products

- Configurable architecture, easily adapted to different products, features and deployments

- Uniform attack mitigations; In-depth offensive security efforts investments

Partitions
Confidential Compute vGPU DRM
Measurement &
Secure Boot Power management
Attestation
NVRISCV SDK
Partition OS Baremetal Applications
Separation Kernel
Boot Plugin
or
BootROM
Peregrine IP
RISC-V Core(s)

SPARK

Offsec

#BHUSA @BlackHatEvents

## Slide 29

### One Core Strategy – Peregrine Ecosystem

- Unified embedded HW and SW across all NVIDIA products

- Configurable architecture, easily adapted to different products, features and deployments

- Uniform attack mitigations; In-depth offensive security efforts investments

- Partition architecture is the foundation for running mixed-criticality applications on NVRISCV

- Peregrine/NVIRSCV architecture foundation for GPU SW Security

Partitions
Confidential Compute vGPU DRM
Measurement &
Secure Boot Power management
Attestation
NVRISCV SDK
Partition OS Baremetal Applications
Separation Kernel
Boot Plugin
or
BootROM
Peregrine IP
RISC-V Core(s)

#BHUSA @BlackHatEvents

## Slide 30

### One Core Strategy – Peregrine Ecosystem

- Architectural flexibility: Great for innovation, but there are still challenges

Partitions
Confidential Compute vGPU DRM
Measurement &
Secure Boot Power management
Attestation
NVRISCV SDK
Partition OS Baremetal Applications
Separation Kernel
Boot Plugin
or
BootROM
Peregrine IP
RISC-V Core(s)
SPARK
Offsec

#BHUSA @BlackHatEvents

## Slide 31

### - RISC V challenges

- Open-source and flexibility

   - Despite undeniable advantages, there are drawbacks:

      - Fragmentation

         - Remediations: Profiles, RISC-V Foundation

      - Not as mature SW ecosystem

         - Remediations: RISC-V Dev Partners, Extension TG/SIG

- Profiles

   - Addresses fragmentation but they may NOT be mutually compatible

      - E.g., RVB23 != RVA23

      - RVA profiles are trying to be backward compatible but there are caveats

- “Custom” extensions might be costly (contribute to RISC-V!)

   - Your custom (private) extension may become incompatible with the officially ratified one

      - New extension may solve your problem in a better (or not) way

   - Custom HW means custom SW support

#BHUSA @BlackHatEvents

## Slide 32

### - NVRISC V

Peregrine chiplet (packet)

NVRISC-V

How to secure this new execution environment? Learn from the past (e.g., No ASLR). Peregrine must consider inner-”outside” peregrines

#BHUSA @BlackHatEvents

## Slide 33

### - NVRISC V

- How to effectively find software vulnerabilities (the BIGGEST attack surface)?

   - NVIDIA Offensive Security Research (OSR)

      - Manual Vulnerability Research is a *must have* but not a sufficient neither a scalable solution

      - Automatic vulnerability detection (fuzzing) is a crucial piece – how to increase the effectiveness?

         - Address Sanitizers and instrumentation (code-coverage) can help but…

#BHUSA @BlackHatEvents

## Slide 34

### - NVRISC V

- How to effectively find software vulnerabilities (the BIGGEST attack surface)?

   - NVIDIA Offensive Security Research (OSR)

      - Manual Vulnerability Research is a *must have* but not a sufficient neither a scalable solution

      - Automatic vulnerability detection (fuzzing) is a crucial piece – how to increase the effectiveness?

         - Address Sanitizers and instrumentation (code-coverage) can help but… <u>RISC-V did not support that (not at that time) :(</u>

#BHUSA @BlackHatEvents

## Slide 35

### - NVRISC V

- How to effectively find software vulnerabilities (the BIGGEST attack surface)?

   - NVIDIA Offensive Security Research (OSR)

      - Manual Vulnerability Research is a *must have* but not a sufficient neither a scalable solution

      - Automatic vulnerability detection (fuzzing) is a crucial piece – how to increase the effectiveness?

         - Address Sanitizers and instrumentation (code-coverage) can help but… <u>RISC-V did not support that (not at that time) :(</u>

- RISC-V Pointer Masking (PM) extension

   - NVIDIA aimed to add HWASAN  (and later MTE) to its RISC-V ecosystem

      - Including M-mode (unusual), S-mode and U-mode support

      - Bare mode support (unusual)

      - With and without OS layer support

#BHUSA @BlackHatEvents

## Slide 36

### - NVRISC V

- How to effectively find software vulnerabilities (the BIGGEST attack surface)?

   - NVIDIA Offensive Security Research (OSR)

      - Manual Vulnerability Research is a *must have* but not a sufficient neither a scalable solution

      - Automatic vulnerability detection (fuzzing) is a crucial piece – how to increase the effectiveness?

         - Address Sanitizers and instrumentation (code-coverage) can help but… <u>RISC-V did not support that (not at that time) :(</u>

- RISC-V Pointer Masking (PM) extension

   - NVIDIA aimed to add HWASAN  (and later MTE) to its RISC-V ecosystem

      - Including M-mode (unusual), S-mode and U-mode support

      - Bare mode support (unusual)

      - With and without OS layer support

   - We developed a custom extension and brought it to the RISC-V International (TEE group)

#BHUSA @BlackHatEvents

## Slide 37

### - NVRISC V

- How to effectively find software vulnerabilities (the BIGGEST attack surface)?

   - NVIDIA Offensive Security Research (OSR)

      - Manual Vulnerability Research is a *must have* but not a sufficient neither a scalable solution

      - Automatic vulnerability detection (fuzzing) is a crucial piece – how to increase the effectiveness?

         - Address Sanitizers and instrumentation (code-coverage) can help but… <u>RISC-V did not support that (not at that time) :(</u>

- RISC-V Pointer Masking (PM) extension

   - NVIDIA aimed to add HWASAN  (and later MTE) to its RISC-V ecosystem

      - Including M-mode (unusual), S-mode and U-mode support

      - Bare mode support (unusual)

      - With and without OS layer support

   - We developed a custom extension and brought it to the RISC-V International (TEE group)

   - Independently, Google was working on own “Pointer Masking”

#BHUSA @BlackHatEvents

## Slide 38

### - NVRISC V

- How to effectively find software vulnerabilities (the BIGGEST attack surface)?

   - NVIDIA Offensive Security Research (OSR)

      - Manual Vulnerability Research is a *must have* but not a sufficient neither a scalable solution

      - Automatic vulnerability detection (fuzzing) is a crucial piece – how to increase the effectiveness?

         - Address Sanitizers and instrumentation (code-coverage) can help but… <u>RISC-V did not support that (not at that time) :(</u>

- RISC-V Pointer Masking (PM) extension

   - NVIDIA aimed to add HWASAN  (and later MTE) to its RISC-V ecosystem

      - Including M-mode (unusual), S-mode and U-mode support

      - Bare mode support (unusual)

      - With and without OS layer support

   - We developed a custom extension and brought it to the RISC-V International (TEE group)

   - Independently, Google was working on own “Pointer Masking”

   - We decided to unite our use-cases and promote a single standard for all.

#BHUSA @BlackHatEvents

## Slide 39

### - NVRISC V

- RISC-V Pointer Masking extension

   - Serves as a framework

   - PM supported multiple use-cases:

      - HWASAN (later a base for HW MTE)

      - Pointer Authentication (PAC)

in-process memory sandbox

- HW Memory Sandboxing (PM introduced 2 CSRs: actual_address = (requested_address & ~mpmmask) | mpmbase

#BHUSA @BlackHatEvents

## Slide 40

### - NVRISC V

- RISC-V Pointer Masking extension

   - Serves as a framework

   - PM supported multiple use-cases:

      - HWASAN (later a base for HW MTE)

      - ~~Pointer Authentication (PAC)~~

in-process memory sandbox

   - ~~HW Memory Sandboxing (PM introduced 2 CSRs: actual_address = (requested_address & ~mpmmask) | mpmbase~~

- Ratified version – HWASAN only + ISA integration

   - Current equation for VA:

      - transformed_effective_address = {{PMLEN{effective_address[XLEN-PMLEN-1]}}, effective_address[XLEN-PMLEN-1:0]}

   - Current equation for PA:

transformed_effective_address = {{PMLEN{0}}, effective_address[XLEN-PMLEN-1:0]}

- No new CSRs, PMLEN in *envcfg (2 bits, **<u>supports top 7 or 16 bits of masking</u>** )

#BHUSA @BlackHatEvents

## Slide 41

### - NVRISC V

- RISC-V Pointer Masking extension

   - Serves as a framework

   - PM supported multiple use-cases:

      - HWASAN (later a base for HW MTE)

      - ~~Pointer Authentication (PAC)~~

in-process memory sandbox

   - ~~HW Memory Sandboxing (PM introduced 2 CSRs: actual_address = (requested_address & ~mpmmask) | mpmbase~~

- Ratified version – HWASAN only + ISA integration

   - Current equation for VA:

transformed_effective_address = {{PMLEN{effective_address[XLEN-PMLEN-1]}}, effective_address[XLEN-PMLEN-1:0]}

   - Current equation for PA:

         - transformed_effective_address = {{PMLEN{0}}, effective_address[XLEN-PMLEN-1:0]}

   - No new CSRs, PMLEN in *envcfg (2 bits, **<u>supports top 7 or 16 bits of masking</u>** )

- RISC-V included PM as part of the profiles!

   - RVA23:

      - Supm, Ssnpm – mandatory for RVA23S64

      - Sspm – optional for RVA23S64

- RVB23:

   - Supm – optional for RVB23U64

   - Ssnpm and Sspm – optional for RVB23S64

#BHUSA @BlackHatEvents

## Slide 42

### - NVRISC V

- RISC-V Pointer Masking extension

   - 4+ years of work

   - Pointer Masking – umbrella for 5 extensions

      - Split per priv-level:

         - Ssnpm – A supervisor-level extension for the next lower privilege

         - Smnpm – A machine-level extension for the next lower privilege

         - Smmpm – A machine-level extension for M-mode

      - Additionally, 2 extensions describing an execution environment – no bearing on HW implementations.

         - Sspm – PM support available in supervisor mode

         - Supm – PM support available in user mode

   - SW ecosystem got support for it

      - LLVM/GCC compilers, binutils, Linux kernel, Qemu, SPIKE, SAIL and more

   - We added HWASAN support for NVIDIA SW ecosystems

      - Fuzzing GSP firmware (under Partition OS)

      - Preparing to fuzz bare-metal microcode

   - Fuzzing RM

   - Preparing to fuzz firmware under RTOS

- More in progress

#BHUSA @BlackHatEvents

## Slide 43

### - NVRISC V

- RISC-V Pointer Masking extension

   - 4+ years of work

   - Pointer Masking – umbrella for 5 extensions

      - Split per priv-level:

         - Ssnpm – A supervisor-level extension for the next lower privilege

         - Smnpm – A machine-level extension for the next lower privilege

         - Smmpm – A machine-level extension for M-mode

      - Additionally, 2 extensions describing an execution environment – no bearing on HW implementations.

         - Sspm – PM support available in supervisor mode

         - Supm – PM support available in user mode

   - SW ecosystem got support for it

      - LLVM/GCC compilers, binutils, Linux kernel, Qemu, SPIKE, SAIL and more

   - We added HWASAN support for NVIDIA SW ecosystems

      - Fuzzing GSP firmware (under Partition OS)

      - Preparing to fuzz bare-metal microcode

   - Fuzzing RM

   - Preparing to fuzz firmware under RTOS

- More in progress

#BHUSA @BlackHatEvents

## Slide 44

### - NVRISC V

##### • RISC-V Control Flow Integrity (CFI) extension

- CFI tries to protect against code reuse attacks (e.g., ret2libc, ROP, COP/JOP, etc)

###### Fake stack

… 0x12345678: … pop %rcx <--- %rcx = 0xdeadbeef 0x12345678 ret 0xdeadbeef … 0x87654320: 0x87654320 pop %rax <--- %rax = 0xabadbabe ret 0xabadbabe … 0xaabbccd0: 0xaabbccd0 mov (%rax),%rcx … ret          ^----- *0xabadbabe = 0xdeadbeef 0x12345678 … pop %r8              <--- %rax = 0x12345678 … jmp *%r8 … Original stack … Function 1 Legit value Function 2 Legit value … Function N Legit value …

#BHUSA @BlackHatEvents

## Slide 45

### - NVRISC V

- RISC-V Control Flow Integrity (CFI) extension

   - CFI tries to protect against code reuse attacks (e.g., ret2libc, ROP, COP/JOP, etc)

   - CFI is actually 2 sub-extensions

      - <u>Zicfiss</u> – Control Flow Integrity Shadow Stack

         - Enforces backward-edge control flow integrity

         - Creates a new region “shadow stack” which keeps a copy of RA only

         - New reg (SSP) and instructions for “shadow stack” management

         - Preserves the original stack ABI

         - Before return, the RA is verified against the “shadow stack” copy

###### Fake stack

… 0x12345678: … pop %rcx <--- %rcx = 0xdeadbeef 0x12345678 ret 0xdeadbeef … 0x87654320: 0x87654320 pop %rax <--- %rax = 0xabadbabe ret 0xabadbabe … 0xaabbccd0: 0xaabbccd0 mov (%rax),%rcx … ret          ^----- *0xabadbabe = 0xdeadbeef 0x12345678 … pop %r8              <--- %rax = 0x12345678 … jmp *%r8 …

- Function can only return to its original caller

- If verification failed, SW-check exception is raised – “Shadow Stack Fault (code=3)”

###### Original stack

###### Shadow stack

Shadow stack
…
…
Function 1
Function 1
Legit value
Function 2
Function 2
…
Legit value
Function N
…
…
Function N
Legit value
…

#BHUSA @BlackHatEvents

## Slide 46

### - NVRISC V

- RISC-V Control Flow Integrity (CFI) extension

   - CFI tries to protect against code reuse attacks (e.g., ret2libc, ROP, COP/JOP, etc)

###### Fake stack

- CFI is actually 2 sub-extensions

…
0x12345678
0xdeadbeef
0x87654320
0xabadbabe
0xaabbccd0
==? …
0x12345678
…

- <u>Zicfiss</u> – Control Flow Integrity Shadow Stack

   - Enforces backward-edge control flow integrity

   - Creates a new region “shadow stack” which keeps a copy of RA only

   - New reg (SSP) and instructions for “shadow stack” management

   - Preserves the original stack ABI

   - Before return, the RA is verified against the “shadow stack” copy

… 0x12345678: pop %rcx <--- %rcx = 0xdeadbeef ret … 0x87654320: pop %rax <--- %rax = 0xabadbabe ret … 0xaabbccd0: mov (%rax),%rcx ret          ^----- *0xabadbabe = 0xdeadbeef … pop %r8              <--- %rax = 0x12345678 jmp *%r8 …

- Function can only return to its original caller

- If verification failed, SW-check exception is raised – “Shadow Stack Fault (code=3)”

###### Original stack

###### Shadow stack

Shadow stack
…
…
Function 1
Function 1
Legit value
Function 2
Function 2
…
Legit value
Function N
…
…
Function N
Legit value
…

#BHUSA @BlackHatEvents

## Slide 47

### - NVRISC V

- RISC-V Control Flow Integrity (CFI) extension

   - CFI tries to protect against code reuse attacks (e.g., ret2libc, ROP, COP/JOP, etc)

   - CFI is actually 2 sub-extensions

      - <u>Zicfilp</u> – Control Flow Integrity Landing Pads

         - Enforces forward-edge control flow integrity

         - Indirect branch *must* be a landing pad instruction (LPAD)

            - 20-bit encoded label instruction

         - Each hart maintains an expected landing pad (ELP) state

         - If ELP == LP_EXPECTED a SW exception is raised if

            - PC of next instruction is not 4-bytes aligned or is not an LPAD

            - A label does not match the expected landing pad label in bits 31:12 of the x7 register

            - If verification failed, SW-check exception is raised – “Landing Pad Fault (code=2)”

#BHUSA @BlackHatEvents

## Slide 48

### - NVRISC V

- RISC-V Control Flow Integrity (CFI) extension

   - CFI tries to protect against code reuse attacks (e.g., ret2libc, ROP, COP/JOP, etc)

   - CFI is actually 2 sub-extensions

      - <u>Zicfilp</u> – Control Flow Integrity Landing Pads

         - Enforces forward-edge control flow integrity

         - Indirect branch *must* be a landing pad instruction (LPAD)

            - 20-bit encoded label instruction

         - Each hart maintains an expected landing pad (ELP) state

         - If ELP == LP_EXPECTED a SW exception is raised if

            - PC of next instruction is not 4-bytes aligned or is not an LPAD

            - A label does not match the expected landing pad label in bits 31:12 of the x7 register

            - If verification failed, SW-check exception is raised – “Landing Pad Fault (code=2)”

…
Function_B:
…
lpad 0xABCDE
Function_A: lui
… jalr
lw x5, 4(sp)  # Load pointer to Function_B …
lui x7, 0xABCDE # Set Label ecall
jalr ra, x5 # indirect branch to Function_B …
… Function_C:
lpad 0xAB123
…

#BHUSA @BlackHatEvents

## Slide 49

### - NVRISC V

- RISC-V Control Flow Integrity (CFI) extension

   - CFI tries to protect against code reuse attacks (e.g., ret2libc, ROP, COP/JOP, etc)

   - CFI is actually 2 sub-extensions

      - <u>Zicfilp</u> – Control Flow Integrity Landing Pads

   - CFI as part of the RISC-V profiles

- Enforces forward-edge control flow integrity

- Indirect branch *must* be a landing pad instruction (LPAD)

      - SW ecosystem got support for it

         - LLVM/GCC, binutils, Linux kernel, Qemu, more

   - 20-bit encoded label instruction

- Each hart maintains an expected landing pad (ELP) state

- If ELP == LP_EXPECTED a SW exception is raised if

   - PC of next instruction is not 4-bytes aligned or is not an LPAD

   - We are adding SW support for CFI

      - We are committed to bringing CFI support for HW and SW in “Rubin” chips (GR20x)

      - We are considering adding “Zicfiss” to M-mode

- A label does not match the expected landing pad label in bits 31:12 of the x7 register

- If verification failed, SW-check exception is raised – “Landing Pad Fault (code=2)”

…
Function_B:
…
lpad 0xABCDE
Function_A: lui
… jalr
lw x5, 4(sp)  # Load pointer to Function_B …
lui x7, 0xABCDE # Set Label ecall
jalr ra, x5 # indirect branch to Function_B …
… Function_C:
lpad 0xAB123
…

#BHUSA @BlackHatEvents

## Slide 50

### - NVRISC V

- RISC-V Control Flow Integrity (CFI) extension

   - CFI tries to protect against code reuse attacks (e.g., ret2libc, ROP, COP/JOP, etc)

   - CFI is actually 2 sub-extensions

      - <u>Zicfilp</u> – Control Flow Integrity Landing Pads •

CFI as part of the RISC-V profiles

- Enforces forward-edge control flow integrity

- Indirect branch *must* be a landing pad instruction (LPAD)

SW ecosystem got support for it

- •

LLVM/GCC, binutils, Linux kernel, Qemu, more

- 20-bit encoded label instruction

We are adding SW support for CFI • We are committed to bringing CFI support for HW and SW in “Rubin” chips (GR20x) • We are considering adding “Zicfiss” to M-mode

- •

- Each hart maintains an expected landing pad (ELP) state •

- • If ELP == LP_EXPECTED a SW exception is raised if •

- • PC of next instruction is not 4-bytes aligned or is not an LPAD

   - A label does not match the expected landing pad label in bits 31:12 of the x7 register

   - If verification failed, SW-check exception is raised – “Landing Pad Fault (code=2)”

…
Function_B:
…
lpad 0xABCDE
Function_A: lui
… jalr
lw x5, 4(sp)  # Load pointer to Function_B …
lui x7, 0xABCDE # Set Label ecall
jalr ra, x5 # indirect branch to Function_B …
… Function_C:
lpad 0xAB123
…

#BHUSA @BlackHatEvents

## Slide 51

### - NVRISC V

- (NV)RISC-V extensions – what’s next?

   - RISC-V Memory Tagging extension (MTE)

   - RISC-V CFI M-mode Shadow Stack sub-extension

   - RISC-V Hardware Fault Isolation (HFI)

#BHUSA @BlackHatEvents

## Slide 52

### - NVRISC V

- (NV)RISC-V extensions – what’s next?

   - RISC-V Memory Tagging extension (MTE)

      - Hardware-assisted Memory Tagging – addresses performance issues with HWASAN

      - We are actively contributing to RISC-V MTE. Beta spec released in June 2025.

      - NVRISC-V ecosystem (HW and SW) support when ratified

- RISC-V CFI M-mode Shadow Stack sub-extension

- RISC-V Hardware Fault Isolation (HFI)

#BHUSA @BlackHatEvents

## Slide 53

### - NVRISC V

- (NV)RISC-V extensions – what’s next?

   - RISC-V Memory Tagging extension (MTE)

   - RISC-V CFI M-mode Shadow Stack sub-extension

      - CFI Shadow Stack (Zicfiss) is not defined for M-mode

         - NVIDIA and RISC-V are working on Zicfiss for M-mode to enhance protection of the critical M-mode SW.

      - Landing Pads (Zicfilp) is defined for all modes (include M-mode) already

   - RISC-V Hardware Fault Isolation (HFI)

#BHUSA @BlackHatEvents

## Slide 54

### - NVRISC V

- (NV)RISC-V extensions – what’s next?

   - RISC-V Memory Tagging extension (MTE)

   - RISC-V CFI M-mode Shadow Stack sub-extension

   - RISC-V Hardware Fault Isolation (HFI)

      - Addresses in-process Memory Sandbox

         - No TG yet

      - We are evaluating benefits of bringing HFI sandbox to our SW ecosystem (Partition OS, Separation Kernel)

      - HFI introduce a user-mode concept of memory regions. Any access “outside” of the predefined region generates a trap.

hfi_enter
Base, length, attributes
Base, length, attributes
hfi_set_region
0       base1 base2 ...                    …   baseN 2^64 .
.
.
hfi_exit
Base, length, attributes

#BHUSA @BlackHatEvents

## Slide 55

### - NVRISC V

- (NV)RISC-V extensions – what’s next?

   - RISC-V Memory Tagging extension (MTE)

   - RISC-V CFI M-mode Shadow Stack sub-extension

   - RISC-V Hardware Fault Isolation (HFI)

- Additional areas of interest:

   - Post Quantum Cryptography (PQC)

   - Side-channel protection / hardening

   - CHERI

   - Enhanced Hardware Fault Injection protection

#BHUSA @BlackHatEvents

## Slide 56

## **Building the Secure Software Foundation on RISC-V**

## Slide 57

#### Peregrine / NVRISCV Multi-Partition Software Architecture

• Multiple Independent Levels of Security/Safety (MILS)
Partition Partition
architecture
Baremetal app Task Task
U-mode
Partition OS
Supervisor RT Supervisor RT
S-mode
M-mode
Partition
Separation Kernel
Policies
BootROM Manifest
Hardware

#BHUSA @BlackHatEvents

## Slide 58

#### Peregrine / NVRISCV Multi-Partition Software Architecture

- Multiple Independent Levels of Security/Safety (MILS) architecture

Partition Partition
architecture
• Fine-grained access control to HW defined by
Baremetal app Task Task manifest and partition policies
U-mode
Partition OS
Supervisor RT Supervisor RT
S-mode
M-mode
Partition  uC SW Privilege
Separation Kernel
Policies
Partition
Privilege
Partition
BootROM Manifest
Privilege Task  Task
Privilege Privilege
Hardware

- Fine-grained access control to HW defined by manifest and partition policies

#BHUSA @BlackHatEvents

## Slide 59

#### Peregrine / NVRISCV Multi-Partition Software Architecture

- Multiple Independent Levels of Security/Safety (MILS) architecture

Partition Partition
architecture
• Fine-grained access control to HW defined by
Baremetal app Task Task manifest and partition policies
•
Partition is defined by partition configurations – partition policies
U-mode
•
Manifest and policies are signed static configuration sets
Partition OS
Supervisor RT Supervisor RT
S-mode
M-mode
Partition  uC SW Privilege
Separation Kernel
Policies
Partition
Privilege
Partition
BootROM Manifest
Privilege Task  Task
Privilege Privilege
Hardware

- Fine-grained access control to HW defined by manifest and partition policies

- • Partition is defined by partition configurations – partition policies

- Manifest and policies are signed static configuration sets

#BHUSA @BlackHatEvents

## Slide 60

#### Foundation for running mixed-criticality applications

- All information flow in/out partitions is access controlled

S/U Mode
Active Partition
Partition 0 Partition N
Peregrine
Peripherals
Baremetal Task Task Task Task Hardware  Engine MMIO
app Access
… Controls
External MMIO
Partition OS Partition OS
Memory
SBI SBI SBI SBI
Policy 0 Policy 1 … Policy N
Separation Kernel
Manifest BootROM

#BHUSA @BlackHatEvents

## Slide 61

#### Foundation for running mixed-criticality applications

- All information flow in/out partitions is access controlled

- Separation Kernel (not a Hypervisor):

- • Controls what HW is exposed to partition

- Does not abstract HW

- Small and formally verified to be free of runtime errors

S/U Mode
Active Partition
Partition 0 Partition N
Peregrine
Peripherals
Baremetal Task Task Task Task Hardware  Engine MMIO
app Access
… Controls
External MMIO
Partition OS Partition OS
Memory
SBI SBI SBI SBI
Policy 0 Policy 1 … Policy N
Separation Kernel
Manifest BootROM

#BHUSA @BlackHatEvents

## Slide 62

#### NVIDIA’s custom RISC-V extensions to enforce External secure boot

• Immutable BootROM

Dual Core Lock Step (DCLS)
Device Map Lockdown
NVRISCV
Partition
Control Bus
U mode Task Task
Crypto Engine
S mode Partition OS
Devices
Secret Control
Supervisor RT
NV MPU
IO-PMP
M mode Separation
BootROM
Kernel
PMP
Data Bus
PMA Debug control
I/O
Memory BootROM TCM

DRAM

#BHUSA @BlackHatEvents

## Slide 63

#### NVIDIA’s custom RISC-V extensions to enforce External secure boot

- Immutable BootROM

- mromprot (NV extension), XOM

Dual Core Lock Step (DCLS)
Device Map Lockdown
NVRISCV
Partition
Control Bus
U mode Task Task
Crypto Engine
S mode Partition OS
Devices
Secret Control
Supervisor RT
NV MPU
IO-PMP
M mode Separation
BootROM
Kernel
PMP
Data Bus
PMA Debug control
I/O
Memory BootROM TCM

DRAM

#BHUSA @BlackHatEvents

## Slide 64

#### NVIDIA’s custom RISC-V extensions to enforce External secure boot

- Immutable BootROM

- mromprot (NV extension), XOM

- No return address spill on stack

Dual Core Lock Step (DCLS)
Device Map Lockdown
NVRISCV
Partition
Control Bus
U mode Task Task
Crypto Engine
S mode Partition OS
Devices
Secret Control
Supervisor RT
NV MPU
IO-PMP
M mode Separation
BootROM
Kernel
PMP
Data Bus
PMA Debug control
I/O
Memory BootROM TCM

DRAM

#BHUSA @BlackHatEvents

## Slide 65

#### NVIDIA’s custom RISC-V extensions to enforce External secure boot

- Immutable BootROM

- mromprot (NV extension), XOM

- No return address spill on stack

- External MMIO Lockdown

Dual Core Lock Step (DCLS)
Device Map Lockdown
NVRISCV
Partition
Control Bus
U mode Task Task
Crypto Engine
S mode Partition OS
Devices
Secret Control
Supervisor RT
NV MPU
IO-PMP
M mode Separation
BootROM
Kernel
PMP
Data Bus
PMA Debug control
I/O
Memory BootROM TCM

DRAM

#BHUSA @BlackHatEvents

## Slide 66

#### NVIDIA’s custom RISC-V extensions to enforce External secure boot

- Immutable BootROM

- mromprot (NV extension), XOM

- No return address spill on stack

- External MMIO Lockdown

- DEF CON 29: “ _Glitching RISC-V chips: MTVEC corruption for hardening ISA”_

Dual Core Lock Step (DCLS)
Device Map Lockdown
NVRISCV
Partition
Control Bus
U mode Task Task
Crypto Engine
S mode Partition OS
Devices
Secret Control
Supervisor RT
NV MPU
IO-PMP
M mode Separation
BootROM
Kernel
PMP
Data Bus
PMA Debug control
I/O
Memory BootROM TCM

DRAM

#BHUSA @BlackHatEvents

## Slide 67

#### NVIDIA’s custom RISC-V extensions to enforce External secure boot

- Immutable BootROM

- mromprot (NV extension), XOM

- No return address spill on stack

- External MMIO Lockdown

- DEF CON 29: “ _Glitching RISC-V chips: MTVEC corruption for hardening ISA”_

PC PC ROB
• DCLS
Main Core Main Core
Compare Error Compare Error
Glitch!
n-cycle-delay n-cycle-delay
PC PC ROB
Shadow Core Shadow Core

Dual Core Lock Step (DCLS)
Device Map Lockdown
NVRISCV
Partition
Control Bus
U mode Task Task
Crypto Engine
S mode Partition OS
Devices
Secret Control
Supervisor RT
NV MPU
IO-PMP
M mode Separation
BootROM
Kernel
PMP
Data Bus
PMA Debug control
I/O
Memory BootROM TCM
DRAM

#BHUSA @BlackHatEvents

## Slide 68

#### Language-based security: formally verified components

#BHUSA @BlackHatEvents

## Slide 69

#### Language-based security: formally verified components

• Tests can only prove bugs exist, not that they don’t

#BHUSA @BlackHatEvents

## Slide 70

#### Language-based security: formally verified components

- Tests can only prove bugs exist, not that they don’t

- SPARK uses contracts and formal verification to prove whole classes of bugs cannot happen

#BHUSA @BlackHatEvents

## Slide 71

#### Language-based security: formally verified components

- Tests can only prove bugs exist, not that they don’t

- SPARK uses contracts and formal verification to prove whole classes of bugs cannot happen

- `Procedure Do_Operation(X : in out Integer; Y : in out Integer; V : in Integer)` **`Precondition`** `:`

   - `V > 0`

   - `X >= V`

```
Postcondition:
```

- `X = X'Old - V`

- `Y = Y'Old + V`

#BHUSA @BlackHatEvents

## Slide 72

#### Language-based security: formally verified components

- Tests can only prove bugs exist, not that they don’t

- SPARK uses contracts and formal verification to prove whole classes of bugs cannot happen

```
ProcedureDo_Operation(X : in out Integer; Y : in out Integer; V : inInteger)
Precondition:
```

```
V > 0
X >= V
```

```
Postcondition:
```

```
X = X'Old-V
Y = Y'Old+ V
```

```
begin
X := X -V;
Y := Y + V;
endDo_Operation;
```

#BHUSA @BlackHatEvents

## Slide 73

#### Language-based security: formally verified components

- Tests can only prove bugs exist, not that they don’t

- SPARK uses contracts and formal verification to prove whole classes of bugs cannot happen

```
ProcedureDo_Operation(X : in out Integer; Y : in out Integer; V : inInteger)
Precondition:
```

```
V > 0
X >= V
```

```
Postcondition:
```

```
X = X'Old-V
Y = Y'Old+ V
```

```
begin
X := X -V;
Y := Y + V;
endDo_Operation;
```

Ada/SPARK Code with Contracts (Preconditions, Postconditions, etc.) Static Analysis Converts code/contracts to logical statements Verification Conditions (VCs) (Logical mathematical claims) SMT Solver (Z3, Alt-Ergo, CVC5) (Automatic mathematical proofs) Manual intervention Proof successful (Improve assertions, code refactor, etc.)

#BHUSA @BlackHatEvents

## Slide 74

#### Language-based security: formally verified components

- Tests can only prove bugs exist, not that they don’t

###### Start with requirements

- SPARK uses contracts and formal verification to prove whole classes of bugs cannot happen

```
ProcedureDo_Operation(X : in out Integer; Y : in out Integer; V : inInteger)
Precondition:
```

```
V > 0
X >= V
```

```
Postcondition:
X = X'Old-V
Y = Y'Old+ V
```

```
begin
X := X -V;
Y := Y + V;
endDo_Operation;
```

Write/Refine Specification (.ads) - Add contracts (pre, post, invariants)

- Write/Refine Implementation (.adb)

- - Implement to meet the specified contracts

Run GNATprove - Prove properties using static analysis

###### Analyze Results

GNATprove reports issues All proofs succeed → Analyze & refine → Component is verified spec/code

#BHUSA @BlackHatEvents

## Slide 75

#### Language-based security: formally verified components

- Tests can only prove bugs exist, not that they don’t

###### Start with requirements

- SPARK uses contracts and formal verification to prove whole classes of bugs cannot happen

```
ProcedureDo_Operation(X : in out Integer; Y : in out Integer; V : inInteger)
Precondition:
```

- `V > 0 X >= V`

**Proven Procedure**

###### **Tested Procedure**

```
Postcondition:
```

```
X = X'Old-V
Y = Y'Old+ V
```

**Tested Procedure** _Preconditions_ `begin X := X - V;` _are proven_ `Y := Y + V;` _Postconditions_ `end Do_Operation;` _are tested_

###### **Proven Procedure**

_Preconditions_ _are tested Postconditions are proven_

Write/Refine Specification (.ads) - Add contracts (pre, post, invariants)

Write/Refine Implementation (.adb) - Implement to meet the specified contracts

- Run GNATprove

- - Prove properties using static analysis

###### Analyze Results

GNATprove reports issues → Analyze & refine spec/code

All proofs succeed → Component is verified

#BHUSA @BlackHatEvents

## Slide 76

#### Language-based security: formally verified components

- Why not do all this with C, Ada, Rust..?

_*What is Safety-Critical Software, and How Can Ada and SPARK Help?_

#BHUSA @BlackHatEvents

## Slide 77

#### Language-based security: formally verified components

Machine states

_*What is Safety-Critical Software, and How Can Ada and SPARK Help?_

#BHUSA @BlackHatEvents

## Slide 78

#### Language-based security: formally verified components

Machine states

Language states

_*What is Safety-Critical Software, and How Can Ada and SPARK Help?_

#BHUSA @BlackHatEvents

## Slide 79

#### Language-based security: formally verified components

Machine states
Language states
Correct States

_*What is Safety-Critical Software, and How Can Ada and SPARK Help?_

#BHUSA @BlackHatEvents

## Slide 80

#### Language-based security: formally verified components

Machine states
Language states
C
Correct States
Ada

_*What is Safety-Critical Software, and How Can Ada and SPARK Help?_

#BHUSA @BlackHatEvents

## Slide 81

#### Language-based security: formally verified components

Machine states

Language states
C
Correct States
SPARK
Ada

_*What is Safety-Critical Software, and How Can Ada and SPARK Help?_

#BHUSA @BlackHatEvents

## Slide 82

#### Language-based security: formally verified components

Machine states

Language states
C
Correct States
SPARK
Ada

_*What is Safety-Critical Software, and How Can Ada and SPARK Help?_

#BHUSA @BlackHatEvents

## Slide 83

#### Language-based security: formally verified components

```
Procedure Do_Operation(X : in out Integer; Y :
in out Integer; V : in Integer)
Precondition:
```

Procedure Do_Operation(X : in out Integer; Y :
Machine states in out Integer; V : in Integer)
Precondition:
V > 0
X >= V
Language states
Postcondition:
X = X'Old - V
Y = Y'Old + V
C
Tested Procedure Proven Procedure
Correct States
SPARK
Ada
Proven Procedure Tested Procedure
Preconditions Preconditions
are tested are proven
Postconditions    Postconditions
are tested
are proven

_*What is Safety-Critical Software, and How Can Ada and SPARK Help?_

#BHUSA @BlackHatEvents

## Slide 84

#### Foundation for running mixed-criticality applications

- Partitions are isolated execution environments where applications run

- Core SW formally verified to be free of runtime errors (AoRTE)

Partitions
Confidential Compute vGPU DRM
Measurement &
Secure Boot Power management
Attestation
NVRISCV SDK
Partition OS Baremetal Applications
Separation Kernel
Boot Plugin
or
BootROM
Peregrine IP
RISC-V Core(s)

SPARK

#BHUSA @BlackHatEvents

## Slide 85

#### Foundation for running mixed-criticality applications

- Partitions are isolated execution environments where applications run

- Core SW formally verified to be free of runtime errors (AoRTE)

- Hardware never speculates past privilege mode switch

- Hardware never speculates past CSR read

- Speculative D cache refill is disabled

- Branch predictor partitioned between privilege modes

Partitions
Confidential Compute vGPU DRM
Measurement &
Secure Boot Power management
Attestation
NVRISCV SDK
Partition OS Baremetal Applications
Separation Kernel
Boot Plugin
or
BootROM
Peregrine IP
RISC-V Core(s)

#BHUSA @BlackHatEvents

## Slide 86

#### Practical takeaways from designing and deploying a billion-core secure system

- Think Holistically

- HW/SW Co-Design is a must

- Standardize When You Can, Innovate When You Must

- Memory Safety is a Hardware Problem Too

- No Silver Bullets – Layered Defense is Essential

Partitions
Confidential
vGPU DRM
Compute
Measurement &
Secure Boot Attestation Power management
NVRISCV SDK
Partition OS Baremetal Applications
Core/Boot SW
Peregrine IP
SPARK

Offsec

#BHUSA @BlackHatEvents

## Slide 87

### Lessons learned

- Hardware extensions are not enough

   - The BIGGEST attack surface is software

      - HW and SW must cooperate to create a secure ecosystem (HW CFI, MTE, HFI, more)

#BHUSA @BlackHatEvents

## Slide 88

### Lessons learned

- Hardware extensions are not enough

   - The BIGGEST attack surface is software

      - HW and SW must cooperate to create a secure ecosystem (HW CFI, MTE, HFI, more)

   - Formally verified languages (like Ada/SPARK) and memory safe languages (like Rust) are great!

      - Significant security ROI but costs are substantial

         - It is likely to have “hybrid” software for a while

      - Non-memory safety vulnerabilities still exist and affect both type of languages

         - DefCon 30: Adam Zabrocki, Alex Tereshkin - Exploitation in the era of Formal Verification <u>https://www.youtube.com/watch?v=TcIaZ9LW1WE</u>

#BHUSA @BlackHatEvents

## Slide 89

### Lessons learned

- Hardware extensions are not enough

   - The BIGGEST attack surface is software

      - HW and SW must cooperate to create a secure ecosystem (HW CFI, MTE, HFI, more)

   - Formally verified languages (like Ada/SPARK) and memory safe languages (like Rust) are great!

      - Significant security ROI but costs are substantial

         - It is likely to have “hybrid” software for a while

      - Non-memory safety vulnerabilities still exist and affect both type of languages

         - DefCon 30: Adam Zabrocki, Alex Tereshkin - Exploitation in the era of Formal Verification <u>https://www.youtube.com/watch?v=TcIaZ9LW1WE</u>

   - Creating innovative ecosystems demands a forward-thinking mindset:

      - Flexibility should support adaptation to ecosystem evolution forecasting in both HW and SW

         - Something which is not a problem today, can be a critical vulnerability tomorrow (e.g., side channels)

         - Being part of various initiatives/organizations is important

            - It helps identify industry trends and make informed predictions, even if the signals aren't always obvious.

      - Scalability, flexibility, performance, reliability and security should be considered collectively, not separately.

      - Hybrid attacks (not just pure SW or pure HW) are likely to be rising (Rowhammer, speculative execution, etc.)

#BHUSA @BlackHatEvents

## Slide 90

# Q&A

Private contact: <u>http://pi3.com.pl pi3@pi3.com.pl</u> Twitter: <u>@Adam_pi3</u> Adam ‘pi3’ Zabrocki

Private contact: <u>markomitic.net linkedin.com/markomitic</u> Twitter: <u>@markomitic</u> Marko Mitic

#BHUSA @BlackHatEvents
