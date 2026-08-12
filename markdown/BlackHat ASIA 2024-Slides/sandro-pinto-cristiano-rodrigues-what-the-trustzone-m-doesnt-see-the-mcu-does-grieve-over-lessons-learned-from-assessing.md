---
title: "M Doesn't See, the MCU Does Grieve Over Lessons Learned from Assessing a Microcontroller TEE"
speakers: ["Sandro Pinto", "Cristiano Rodrigues -What the TrustZone"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2024"
edition: "ASIA"
year: 2024
source_pdf: "BlackHat ASIA 2024-Slides/Sandro Pinto & Cristiano Rodrigues -What the TrustZone-M Doesn't See, the MCU Does Grieve Over Lessons Learned from Assessing a Microcontroller TEE.pdf"
pages: 342
sha256: "21b8a36edabb19fd1edb3c8332b29ac3ffb11cfd1612e2e79712ce53a4d97189"
text_chars: 111721
ocr_pages: 34
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:52:32Z"
---
# M Doesn't See, the MCU Does Grieve Over Lessons Learned from Assessing a Microcontroller TEE

**Speakers:** Sandro Pinto, Cristiano Rodrigues -What the TrustZone  
**Conference:** Black Hat ASIA 2024  
**Source:** `BlackHat ASIA 2024-Slides/Sandro Pinto & Cristiano Rodrigues -What the TrustZone-M Doesn't See, the MCU Does Grieve Over Lessons Learned from Assessing a Microcontroller TEE.pdf` (342 pages)


## Slide 1

What the TrustZone-M Doesn't See, the MCU Does Grieve Over

Lessons Learned from Assessing a Microcontroller TEE

###### **Cristiano Rodrigues | Sandro Pinto, PhD**

(Centro ALGORITMI / LASI, Universidade do Minho)

#BHASIA @BlackHatEvents

## Slide 2

#### What the TrustZone-M Doesn't See, the MCU Does Grieve Over Lessons Learned from Assessing a Microcontroller TEE

**Cristiano Rodrigues | Sandro Pinto, PhD**

(Centro ALGORITMI / LASI, Universidade do Minho)

# BHASIA @BlackHatEvents

## Slide 3

01

###### Introduction

Background and Motivation

A Bumpy but Revealing Journey 02 Weak Protections, TEE Assessment and our Responsible Disclosure Journey

##### **AGENDA**

What Can Go Wrong 03

Attack Examples and “Live” Demo

04 Lessons Learned

Advices for HW & SW providers and System Designers

Summary 05

Final Thoughts and BH Sound Bytes

## Slide 4

##### **Introduction**

**Background and Motivation**

## Slide 5

AI-ENABLED SMART EDGE DEVICES CITIES SMART FACTORIES SMART AGRICULTURE INTERNET OF THINGS

DRONES HARDWARE WALLETS

MEDICAL HOME
DEVICES APPLIANCES
AUTONOMOUS
WEARABLES
VEHICLES

## Slide 6

AI-ENABLED SMART
EDGE DEVICES CITIES
SMART
FACTORIES
SMART
AGRICULTURE

DRONES

INTERNET OF THINGS

HARDWARE WALLETS

MEDICAL HOME
DEVICES APPLIANCES
AUTONOMOUS
WEARABLES
VEHICLES

## Slide 7

AI-ENABLED SMART EDGE DEVICES CITIES SMART FACTORIES SMART

AGRICULTURE **THE AGE OF** INTERNET OF THINGS **CYBERWARFARE**

DRONES

HARDWARE WALLETS

MEDICAL HOME DEVICES APPLIANCES AUTONOMOUS WEARABLES VEHICLES

## Slide 8

AI-ENABLED SMART EDGE DEVICES CITIES SMART FACTORIES SMART AGRICULTURE

DRONES

###### INTERNET OF THINGS

MEDICAL HOME
DEVICES APPLIANCES
AUTONOMOUS
WEARABLES
VEHICLES

HARDWARE WALLETS

## Slide 9

###### INTERNET OF THINGS

MCU

## Slide 10

###### INTERNET OF THINGS

MCU

### TRUSTZONE

## Slide 11

###### Armv8-M TrustZone

Armv6/7-M Processor Modes

**ESRGv3**

**BLACKHAT24**

## Slide 12

###### Armv8-M TrustZone

Armv6/7-M Processor Modes

THREAD

**ESRGv3**

**BLACKHAT24**

## Slide 13

###### Armv8-M TrustZone

Armv6/7-M Processor Modes

THREAD
HANDLER

**ESRGv3**

**BLACKHAT24**

## Slide 14

###### Armv8-M TrustZone

Armv6/7-M Processor Modes

Armv6/7-M Privileges Levels

THREAD
HANDLER

**ESRGv3**

**BLACKHAT24**

## Slide 15

###### Armv8-M TrustZone

Armv6/7-M Processor Modes

Armv6/7-M Privileges Levels

THREAD
HANDLER

UnPrivileged

**ESRGv3**

**BLACKHAT24**

## Slide 16

###### Armv8-M TrustZone

Armv6/7-M Processor Modes

Armv6/7-M Privileges Levels

THREAD
HANDLER

UnPrivileged
Privileged

**ESRGv3**

**BLACKHAT24**

## Slide 17

###### Armv8-M TrustZone

Armv6/7-M Processor Modes

Armv6/7-M Privileges Levels

THREAD
HANDLER

UnPrivileged
Privileged

**ESRGv3**

**BLACKHAT24**

## Slide 18

###### Armv8-M TrustZone

Armv6/7-M Processor Modes

Armv6/7-M Privileges Levels

Armv6/7-M Base Architecture

THREAD UnPrivileged
HANDLER Privileged

**ESRGv3**

**BLACKHAT24**

## Slide 19

###### Armv8-M TrustZone

Armv6/7-M Processor Modes

Armv6/7-M Privileges Levels

Armv6/7-M Base Architecture

THREAD
HANDLER

UnPrivileged
Privileged

UnPriv. THREAD

**ESRGv3**

**BLACKHAT24**

## Slide 20

###### Armv8-M TrustZone

Armv6/7-M Processor Modes

Armv6/7-M Privileges Levels

Armv6/7-M Base Architecture

THREAD
HANDLER

UnPrivileged UnPriv. THREAD
Priv.  THREAD
Privileged

**ESRGv3**

**BLACKHAT24**

## Slide 21

###### Armv8-M TrustZone

Armv6/7-M Processor Modes

Armv6/7-M Privileges Levels

Armv6/7-M Base Architecture

THREAD
HANDLER

UnPrivileged UnPriv. THREAD
Priv.  THREAD
Privileged
Priv.  HANDLER

**ESRGv3**

**BLACKHAT24**

## Slide 22

###### Armv8-M TrustZone

Armv6/7-M Processor Modes

Armv6/7-M Privileges Levels

Armv6/7-M Base Architecture

THREAD
HANDLER

UnPrivileged UnPriv. THREAD
Priv.  THREAD
Privileged
Priv.  HANDLER

**ESRGv3**

**BLACKHAT24**

## Slide 23

###### Armv8-M TrustZone

Armv6/7-M Base Architecture

UnPriv. THREAD
Priv.  THREAD
Priv.  HANDLER

**ESRGv3**

**BLACKHAT24**

## Slide 24

###### Armv8-M TrustZone

Armv6/7-M Base Architecture

UnPriv. THREAD
Priv.  THREAD
Priv.  HANDLER

x2

**ESRGv3**

**BLACKHAT24**

## Slide 25

###### Armv8-M TrustZone

###### Armv6/7-M Base Architecture

UnPriv. THREAD
Priv.  THREAD
Priv.  HANDLER

x2

UnPriv. THREAD

Priv.  THREAD
Priv.  HANDLER

**ESRGv3**

**BLACKHAT24**

## Slide 26

###### Armv8-M TrustZone

###### Armv6/7-M Base Architecture

UnPriv. THREAD

Priv.  THREAD
Priv.  HANDLER

x2

UnPriv. THREAD

UnPriv. THREAD

Priv.  THREAD Priv.  THREAD
Priv.  HANDLER Priv.  HANDLER

**ESRGv3**

**BLACKHAT24**

## Slide 27

###### Armv8-M TrustZone

###### Armv6/7-M Base Architecture

###### Non-Secure State

UnPriv. THREAD

Priv.  THREAD
Priv.  HANDLER

x2

UnPriv. THREAD

UnPriv. THREAD

Priv.  THREAD Priv.  THREAD
Priv.  HANDLER Priv.  HANDLER

**ESRGv3**

**BLACKHAT24**

## Slide 28

###### Armv8-M TrustZone

###### Armv6/7-M Base Architecture

###### Non-Secure State

Secure State

UnPriv. THREAD

Priv.  THREAD
Priv.  HANDLER

x2

UnPriv. THREAD

Priv.  THREAD
Priv.  HANDLER

UnPriv. THREAD

Priv.  THREAD Priv.  HANDLER

**ESRGv3**

**BLACKHAT24**

## Slide 29

###### Armv8-M TrustZone

Armv8-M TrustZone Architecture

###### Armv6/7-M Base Architecture

UnPriv. THREAD
Priv.  THREAD
Priv.  HANDLER

x2

Non-Secure State Secure State
UnPriv. THREAD UnPriv. THREAD
Priv.  THREAD Priv.  THREAD
Priv.  HANDLER Priv.  HANDLER

**ESRGv3**

**BLACKHAT24**

## Slide 30

###### Armv8-M TrustZone

###### Non-Secure State

UnPriv. THREAD

Priv.  THREAD

Priv.  HANDLER

###### Secure State

UnPriv. THREAD

Priv.  THREAD

Priv.  HANDLER

**ESRGv3**

**BLACKHAT24**

## Slide 31

###### Armv8-M TrustZone

###### Non-Secure State

UnPriv. THREAD

Priv.  THREAD

Priv.  HANDLER

Secure State

UnPriv. THREAD

Priv.  THREAD

Priv.  HANDLER

Armv8-M CPU

**ESRGv3**

**BLACKHAT24**

## Slide 32

###### Armv8-M TrustZone

Non-Secure State

Secure State

Armv8-M CPU

Armv8-M Processor Core

UnPriv. THREAD

Priv.  THREAD

Priv.  HANDLER

UnPriv. THREAD

Priv.  THREAD

Priv.  HANDLER

**ESRGv3**

**BLACKHAT24**

## Slide 33

###### Armv8-M TrustZone

Non-Secure State

Secure State

Armv8-M CPU

Armv8-M Processor Core

UnPriv. THREAD Priv.  THREAD Priv.  HANDLER

UnPriv. THREAD

Priv.  THREAD Priv.  HANDLER

Memory Access

Memory

**ESRGv3**

**BLACKHAT24**

## Slide 34

###### Armv8-M TrustZone

###### Non-Secure State

Secure State

Armv8-M CPU

Armv8-M Processor Core

UnPriv. THREAD

Priv.  THREAD

Priv.  HANDLER

UnPriv. THREAD

Priv.  THREAD

Priv.  HANDLER

Access Permissions Checks

Memory Access

Memory

**ESRGv3**

**BLACKHAT24**

## Slide 35

###### Armv8-M TrustZone

###### Non-Secure State

UnPriv. THREAD Priv.  THREAD Priv.  HANDLER

Secure State

UnPriv. THREAD

Priv.  THREAD Priv.  HANDLER

Armv8-M CPU

Armv8-M Processor Core Memory Access Access Permissions Checks

SAU + IDAU

Memory

**ESRGv3**

**BLACKHAT24**

## Slide 36

###### Armv8-M TrustZone

###### Non-Secure State

UnPriv. THREAD
Priv.  THREAD
Priv.  HANDLER

###### Secure State

UnPriv. THREAD

Priv.  THREAD
Priv.  HANDLER

Armv8-M CPU

Armv8-M Processor Core Memory Access Access Permissions Checks SAU + IDAU

Memory

**ESRGv3**

**BLACKHAT24**

## Slide 37

###### Armv8-M TrustZone

###### Non-Secure State

UnPriv. THREAD Priv.  THREAD Priv.  HANDLER

###### Secure State

UnPriv. THREAD

Priv.  THREAD Priv.  HANDLER

Armv8-M CPU

Armv8-M Processor Core Memory Access Access Permissions Checks SAU + IDAU

Memory

**ESRGv3**

**BLACKHAT24**

## Slide 38

###### Armv8-M TrustZone

###### Non-Secure State

Secure State

Armv8-M CPU

UnPriv. THREAD UnPriv. THREAD Priv.  THREAD Priv.  THREAD Priv.  HANDLER Priv.  HANDLER

Armv8-M Processor Core Memory Access Access Permissions Checks SAU + IDAU MPU_NS MPU_S Memory

**ESRGv3**

**BLACKHAT24**

## Slide 39

###### Armv8-M TrustZone

###### Non-Secure State

Secure State

Armv8-M CPU

UnPriv. THREAD UnPriv. THREAD Priv.  THREAD Priv.  THREAD Priv.  HANDLER Priv.  HANDLER

Armv8-M Processor Core Memory Access Access Permissions Checks SAU + IDAU MPU_NS MPU_S Memory

**ESRGv3**

**BLACKHAT24**

## Slide 40

###### Armv8-M TrustZone

###### Non-Secure State

UnPriv. THREAD Priv.  THREAD Priv.  HANDLER

Secure State

UnPriv. THREAD Priv.  THREAD Priv.  HANDLER

Armv8-M CPU

Armv8-M Processor Core Memory Access Access Permissions Checks SAU + IDAU MPU_NS MPU_S Memory

**ESRGv3**

**BLACKHAT24**

## Slide 41

CPU Protection vs System Protection

## Slide 42

###### CPU Protection vs System Protection

**ESRGv3**

**BLACKHAT24**

## Slide 43

###### CPU Protection vs System Protection

Armv8-M CPU
Armv8-M Processor
Core
SAU MPU
Memory

**ESRGv3**

**BLACKHAT24**

## Slide 44

###### CPU Protection vs System Protection

Armv8-M CPU
Armv8-M Processor
Core
SAU MPU
Memory

Armv8-M
Memory Protection  Controllers

**ESRGv3**

**BLACKHAT24**

## Slide 45

###### CPU Protection vs System Protection

Armv8-M CPU
Armv8-M Processor
Core
SAU MPU
Memory

**ESRGv3**

**BLACKHAT24**

## Slide 46

###### CPU Protection vs System Protection

Armv8-M CPU
Armv8-M Processor
Other
Core
DMA
Peripherals
SAU MPU
Memory

**ESRGv3**

**BLACKHAT24**

## Slide 47

###### CPU Protection vs System Protection

Armv8-M CPU
Armv8-M Processor
Other
Core
DMA
Peripherals
M CU
SAU MPU
Memory

**ESRGv3**

**BLACKHAT24**

## Slide 48

###### CPU Protection vs System Protection

Armv8-M CPU
Armv8-M Processor
Other
Core
DMA
Peripherals
SAU MPU
ACCESS POLICIES
ADDR SAU MPU
0x100 … …
0x200 … …
Memory
0x300 … …
0x400 … …
0x500 … …

**BLACKHAT24**

## Slide 49

###### CPU Protection vs System Protection

Armv8-M CPU
Armv8-M Processor
Other
Core
DMA
Peripherals
Priv. Access
SAU
Permissions
ACCESS POLICIES
ADDR SAU MPU
0x100 S …
0x200 NS …
Memory
0x300 S …
0x400 S …
0x500 NS …

**BLACKHAT24**

## Slide 50

###### CPU Protection vs System Protection

Armv8-M CPU
Armv8-M Processor
Other
Core
DMA
Peripherals
SAU MPU
ACCESS POLICIES
ADDR SAU MPU
0x100 S Priv
0x200 NS Unpriv Memory
0x300 S Unpriv
0x400 S Priv
0x500 NS Priv

**BLACKHAT24**

## Slide 51

###### CPU Protection vs System Protection

Armv8-M CPU
Armv8-M Processor
Other
Core
DMA
Peripherals
SAU MPU
ACCESS POLICIES
ADDR SAU MPU
0x100 S Priv
0x200 NS Unpriv Memory
0x300 S Unpriv
0x400 S Priv
0x500 NS Priv

**BLACKHAT24**

## Slide 52

###### CPU Protection vs System Protection

Armv8-M CPU
Armv8-M Processor Core
Secure Unprivileged
Other
DMA
Peripherals
SAU MPU
ACCESS POLICIES
0x100
ADDR SAU MPU
0x100 S Priv
0x200 NS Unpriv Memory
0x300 S Unpriv
0x400 S Priv
0x500 NS Priv

**BLACKHAT24**

## Slide 53

###### CPU Protection vs System Protection

Armv8-M CPU
Armv8-M Processor Core
Secure Unprivileged
Other
DMA
Peripherals
SAU MPU
ACCESS POLICIES
0x100
ADDR SAU MPU
0x100 S Priv
0x200 NS Unpriv Memory
0x300 S Unpriv
0x400 S Priv
0x500 NS Priv

**BLACKHAT24**

## Slide 54

###### CPU Protection vs System Protection

Armv8-M CPU
Armv8-M Processor Core
Secure Unprivileged
Other
DMA
Peripherals
SAU MPU
0x100
ACCESS POLICIES
0x100
ADDR SAU MPU
0x100 S Priv
0x200 NS Unpriv Memory
0x300 S Unpriv
0x400 S Priv
0x500 NS Priv

**BLACKHAT24**

## Slide 55

###### CPU Protection vs System Protection

Armv8-M CPU
Armv8-M Processor Core
Secure Unprivileged
Other
DMA
Peripherals
SAU MPU
0x100
ACCESS POLICIES
0x100
ADDR SAU MPU
0x100 S Priv
0x200 NS Unpriv Memory
0x300 S Unpriv
0x400 S Priv
0x500 NS Priv

**BLACKHAT24**

## Slide 56

###### CPU Protection vs System Protection

Armv8-M CPU
Armv8-M Processor Core
Secure Unprivileged
Other
DMA
Peripherals
SAU MPU
MPC MPC
ACCESS POLICIES
0x100
ADDR SAU MPU
0x100 S Priv
0x200 NS Unpriv Memory
0x300 S Unpriv
0x400 S Priv
0x500 NS Priv

**BLACKHAT24**

## Slide 57

###### CPU Protection vs System Protection

Armv8-M CPU
Secure Unprivileged
Other
DMAVendor-Specific
Peripherals
Memory Protection  Controllers
SAU MPU
MPC MPC
ACCESS POLICIES
0x100
ADDR SAU MPU
0x100 S Priv
0x200 NS Unpriv Memory
0x300 S Unpriv
0x400 S Priv
0x500 NS Priv

**BLACKHAT24**

## Slide 58

###### CPU Protection vs System Protection

Armv8-M CPU
Armv8-M Processor Core
Secure Unprivileged
Other
DMA
Peripherals
SAU MPU
MPC MPC
ACCESS POLICIES
0x100
ADDR SAU MPU
0x100 S Priv
0x200 NS Unpriv Memory
0x300 S Unpriv
0x400 S Priv
0x500 NS Priv

**BLACKHAT24**

## Slide 59

###### CPU Protection vs System Protection

Armv8-M CPU
Armv8-M Processor Core
Secure Unprivileged
Other
DMA
Peripherals
SAU MPU
MPC MPC
ACCESS POLICIES
0x100
ADDR SAU MPU 0x100
0x100 S Priv
0x200 NS Unpriv Memory
0x300 S Unpriv
0x400 S Priv
0x500 NS Priv

**BLACKHAT24**

## Slide 60

###### CPU Protection vs System Protection

Armv8-M CPU
Armv8-M Processor Core
Secure Unprivileged
Other
DMA
Peripherals
SAU MPU
MPC MPC
ACCESS POLICIES
0x100
ADDR SAU MPU 0x100
0x100 S Priv
0x200 NS Unpriv Memory
0x300 S Unpriv
0x400 S Priv
0x500 NS Priv

**BLACKHAT24**

## Slide 61

###### CPU Protection vs System Protection

Armv8-M CPU
Armv8-M Processor
Other
Core
DMA
Peripherals
SAU MPU
MPC MPC
Memory

**ESRGv3**

**BLACKHAT24**

## Slide 62

###### CPU Protection vs System Protection

Armv8-M CPU
Armv8-M Processor
Other
Core
DMA
Peripherals
SAU MPU
MPC MPC
Memory

**ESRGv3**

**BLACKHAT24**

## Slide 63

###### CPU Protection vs System Protection

Armv8-M CPU
Armv8-M Processor
CPU-Only
Other
Core
DMA
Protections Peripherals
SAU MPU
MPC MPC
(Armv8-M)
Memory

**ESRGv3**

**BLACKHAT24**

## Slide 64

###### CPU Protection vs System Protection

Armv8-M CPU
Armv8-M Processor
System-Wide
CPU-Only
Other
Core
DMA
Peripherals
Protections Protection
SAU MPU
MPC MPC
(Armv8-M)
(Vendors)
Memory

BLACKHAT24

**ESRGv3**

## Slide 65

Platform Security Architecture (PSA)

## Slide 66

###### Platform Security Architecture (PSA)

NORMAL WORLD SECURE WORLD
NSPE SPE
SW SW
CPU

**ESRGv3**

**BLACKHAT24**

## Slide 67

###### Platform Security Architecture (PSA)

NORMAL WORLD SECURE WORLD
NSPE SPE
SW SW
CPU

**ESRGv3**

**BLACKHAT24**

## Slide 68

###### Platform Security Architecture (PSA)

NORMAL WORLD SECURE WORLD
NSPE SPE
SW SW
CPU

**ESRGv3**

**BLACKHAT24**

## Slide 69

###### Platform Security Architecture (PSA)

NORMAL WORLD SECURE WORLD
NSPE SPE
SW SW
CPU

SPE
SW

**ESRGv3**

**BLACKHAT24**

## Slide 70

###### Platform Security Architecture (PSA)

NORMAL WORLD SECURE WORLD
NSPE SPE
SW SW
CPU

UNPRIV.
PRIV.

**ESRGv3**

**BLACKHAT24**

## Slide 71

###### Platform Security Architecture (PSA)

NORMAL WORLD SECURE WORLD
NSPE SPE
SW SW
CPU

Unprivileged Secure Software UNPRIV.
PRIV.

**ESRGv3**

**BLACKHAT24**

## Slide 72

###### Platform Security Architecture (PSA)

NORMAL WORLD SECURE WORLD
NSPE SPE
SW SW
CPU

Unprivileged Secure Software UNPRIV.
PRIV.
Privileged Secure Services

**ESRGv3**

**BLACKHAT24**

## Slide 73

###### Platform Security Architecture (PSA)

NORMAL WORLD SECURE WORLD
THREAD
NSPE SPE
SW SW
CPU

Unprivileged Secure Software UNPRIV.
PRIV.
Privileged Secure Services

**ESRGv3**

**BLACKHAT24**

## Slide 74

###### Platform Security Architecture (PSA)

NORMAL WORLD SECURE WORLD
THREAD
NSPE SPE
SW SW
CPU

Unprivileged Secure Software UNPRIV.
Privileged Secure Services
PRIV.
Privileged Secure Software

**ESRGv3**

**BLACKHAT24**

## Slide 75

###### Platform Security Architecture (PSA)

NORMAL WORLD SECURE WORLD
THREAD Unprivileged Secure Software UNPRIV.
NSPE SPE
SW SW
THREAD Privileged Secure Services
PRIV.
Privileged Secure Software
CPU

**ESRGv3**

**BLACKHAT24**

## Slide 76

###### Platform Security Architecture (PSA)

NORMAL WORLD SECURE WORLD
THREAD Unprivileged Secure Software UNPRIV.
NSPE SPE
SW SW
THREAD Privileged Secure Services
PRIV.
HANDLER Privileged Secure Software
CPU

**ESRGv3**

**BLACKHAT24**

## Slide 77

###### Platform Security Architecture (PSA)

NORMAL WORLD SECURE WORLD
THREAD ARoT 1 ARoT 2 ARoT N UNPRIV.
NSPE SPE
SW SW
THREAD Privileged Secure Services
PRIV.
HANDLER Privileged Secure Software
CPU

**ESRGv3**

**BLACKHAT24**

## Slide 78

###### Platform Security Architecture (PSA)

NORMAL WORLD SECURE WORLD
THREAD ARoT 1 ARoT 2 ARoT N UNPRIV.
NSPE SPE
SW SW
THREAD PRoT 1 PRoT 2 PRoT N
PRIV.
HANDLER Privileged Secure Software
CPU

**ESRGv3**

**BLACKHAT24**

## Slide 79

###### Platform Security Architecture (PSA)

NORMAL WORLD SECURE WORLD
THREAD ARoT 1 ARoT 2 ARoT N UNPRIV.
NSPE SPE
SW SW
THREAD PRoT 1 PRoT 2 PRoT N
PRIV.
HANDLER IPC SPM IRQ
CPU

**ESRGv3**

**BLACKHAT24**

## Slide 80

###### Platform Security Architecture (PSA)

###### PSA Level 1

**ESRGv3**

**BLACKHAT24**

## Slide 81

###### Platform Security Architecture (PSA)

PSA Level 1

NORMAL WORLD SECURE WORLD
SW
CPU

**ESRGv3**

**BLACKHAT24**

## Slide 82

###### Platform Security Architecture (PSA)

###### PSA Level 1

NORMAL WORLD SECURE WORLD
NSPE SPE
SW SW
CPU

**ESRGv3**

**BLACKHAT24**

## Slide 83

###### Platform Security Architecture (PSA)

###### PSA Level 1

NORMAL WORLD SECURE WORLD
ARoTs
NSPE
SW PRoTs
Kernel
CPU

**ESRGv3**

**BLACKHAT24**

## Slide 84

###### Platform Security Architecture (PSA)

PSA Level 1

PSA Level 2

NORMAL WORLD SECURE WORLD
ARoTs
NSPE
SW PRoTs
Kernel
CPU

**ESRGv3**

**BLACKHAT24**

## Slide 85

###### Platform Security Architecture (PSA)

###### PSA Level 1

###### PSA Level 2

NORMAL WORLD SECURE WORLD
ARoTs
NSPE
SW PRoTs
Kernel
CPU

NORMAL WORLD SECURE WORLD
ARoTs
NSPE
SW PRoTs
Kernel
CPU

**ESRGv3**

**BLACKHAT24**

## Slide 86

###### Platform Security Architecture (PSA)

###### PSA Level 1

###### PSA Level 2

NORMAL WORLD SECURE WORLD
ARoTs
NSPE
SW PRoTs
Kernel
CPU

NORMAL WORLD SECURE WORLD
ARoTs
NSPE
SW
PRoTs
Kernel
CPU

**ESRGv3**

**BLACKHAT24**

## Slide 87

###### Platform Security Architecture (PSA)

###### PSA Level 1

PSA Level 2

PSA Level 3

NORMAL WORLD SECURE WORLD
ARoTs
NSPE
SW PRoTs
Kernel
CPU

NORMAL WORLD SECURE WORLD
ARoTs
NSPE
SW
PRoTs
Kernel
CPU

**ESRGv3**

**BLACKHAT24**

## Slide 88

###### Platform Security Architecture (PSA)

###### PSA Level 1

###### PSA Level 2

PSA Level 3

NORMAL WORLD SECURE WORLD
ARoTs
NSPE
SW PRoTs
Kernel
CPU

NORMAL WORLD SECURE WORLD
ARoTs
NSPE
SW
PRoTs
Kernel
CPU

NORMAL WORLD SECURE WORLD
ARoTs
NSPE
SW
PRoTs
Kernel
CPU

**ESRGv3**

**BLACKHAT24**

## Slide 89

###### Platform Security Architecture (PSA)

###### PSA Level 1

###### PSA Level 2

PSA Level 3

NORMAL WORLD SECURE WORLD
ARoTs
NSPE
SW PRoTs
Kernel
CPU

NORMAL WORLD SECURE WORLD
ARoTs
NSPE
SW
PRoTs
Kernel
CPU

NORMAL WORLD SECURE WORLD
ARoT ARoT
1 N
NSPE
SW
PRoTs
Kernel
CPU

**ESRGv3**

**BLACKHAT24**

## Slide 90

###### PARADOXAL OBSERVATIONS

**01 TRUSTZONE-M HAS A CPU-CENTRIC VIEW**

Armv8-M Only Defines Protection Controllers at The CPU-level (MPU, SAU, IDAU)

**02**

**SYSTEM-WIDE PROTECTIONS ARE PROPRIETARY**

Vendors Are Forced to Develop System Protection Controllers (PPCs, MPCs)

**~~03~~**

**03**

**MISSMATCH BETWEEN TZ-M AND PSA LEVELS**

PSA Level 2/3 Need CPU- and Systemlevel Memory Protection Controllers (the latter isn’t defined by Armv8-M)

**ESRGv3**

**BLACKHAT24**

## Slide 91

**_While System-Wide protections are a must, Armv8-M only defines CPU-level memory protections.  We hypothesize that this dichotomy (together with a lack of  understanding of the PSA isolation levels) may open security holes in modern TrustZone-M systems_**

###### Hypothesis

## Slide 92

##### **A Bumpy but Revealing Journey**

**Weak Protections, TEE Assessment and our Responsible Disclosure Journey**

## Slide 93

MICROCHIPSAML11

## Slide 94

MICROCHIP TRUSTONIC

## Slide 95

### MICROCHIP

### TRUSTONIC

SAML11

## Slide 96

### MICROCHIP

SAML11

### TRUSTONIC

Kinibi-M

## Slide 97

### MICROCHIP TRUSTONIC

SAML11 Kinibi-M

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
aking The World A Safer Place
Mircochip First To Use Turstonic Revolutionary
Kinibi-M Platform For Microcontrollers
YMG Ole nile kel T RUSTONIC
SAML11 Kinibi-M
```

## Slide 98

### MICROCHIP TRUSTONIC

SAML11 Kinibi-M

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
security com
Making The World A Safer Place
ElectronicDesign
Artificial Intelligence (Al) Cybe
TECHNOLOGIES > EMBEDDED
Microchip Debuts Cortex-M23
MCUs
June 25,2018 E&I)
Two of the first Cortex-M23 microcontrollers
have arrived—developed by Microchip—and
advanced security is among the features.
Mircochip First To Use Turstonic Revolutionary
Kinibi-M Platform For Microcontrollers
William G. Wong
YMG Ole nile kel T RUSTONIC
SAML11 Kinibi-M
```

## Slide 99

### MICROCHIP TRUSTONIC

SAML11 Kinibi-M

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ElectronicDesign. LOGIN JO
security@nformed con
Making The World A Safer Place
Artificial Intelligence (Al) Mobile Access Healthcare Security Cybe eA ee Eee REMESDDED
Microchip Debuts Cortex-M23
Mircochip First To Use Turstonic Revolutionary}mcus _
Kinibi-M Platform For Microcontrollers :
Two of the first Cortex-M23 microcontrollers
have arrived—developed by Microchip—and
advanced security is among the features.
William G. Wong
TRUSTONIC FIND OUT MORE
Not just droning on! The rise of Kinibi-M| @
31 OCTOBER 2017
```

## Slide 100

### MICROCHIP TRUSTONIC

SAML11 Kinibi-M

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
security@nformed om ElectronicDesign. LOGIN JO
Making The World A Safer Place
Artificial Intelligence (Al) Mobile Access Healthcare Security Cybe eA ee Eee REMESDDED
Microchip Debuts Cortex-M23
Mircochip First To Use Turstonic Revolutionary|mcus
June 25,2018 E&I
Kinibi-M Platform For Microcontrollers Two of the first Cortex-Mzg microcontrollers
have arrived—developed by Microchip—and
advanced security is among the features.
William G. Wong
TRUSTONIC fe saox =
Flying Vehicles V Smart Cities Vv Transportation V Robotics IIoT v Security Vv More ¥
Not just droning on! The rise of Kinibi-M Trustonic Embeds IoT Security Technology in Microchip
MCU
31 OCTOBER 2017 The IoT security technology will be embedded at the chip level using Trustonic’s Kinibi-M software.
```

## Slide 101

MICROCHIP TRUSTONIC SAML11 Kinibi-M

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Secu rityOnformed com ElectronicDesign. LOGIN Jo
Making The World A Safer Place
Artificial Intelligence (Al) Mobile Access Healthcare Security Cybe eA ee Eee REMESDDED
Microchip Debuts Cortex-M23
Mircochip First To Use Turstonic Revolutionary|mcus
June 25,2018 E&I
Kinibi-M Platform For Microcontrollers Two of the first Cortex-Mz23 microcontrollers
have arrived—developed by Microchip—and
advanced security is among the features.
William G. Wong
TRUSTONIC C Si: HOOX |e
Flying Vehicles V Smart Cities Vv Transportation V Robotics IIoT v Security Vv More ¥
Not just droning on! The rise of Kinibi-M Trustonic Embeds IoT Security Technology in Microchip
MCU
31 OCTOBER 2017 The IoT security technology will be embedded at the chip level using Trustonic’s Kinibi-M software.
CLOUD DESIGN + OPTIMISATION ENERGY MANAGEMENT HOSTING + COLOCATION INFRASTRU:
Trustonic launches loT device security
solution
Blockchain-based Digital Holograms, trusted device provisioning and a modular,
secure OS combine to bring trust to constrained loT devices.
&86 years ago Posted in
```

## Slide 102

MICROCHIP TRUSTONIC SAML11 Kinibi-M

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
security@nformed com ElectronicDesign LOGIN JO
Making The World A Safer Place _— ———— — SS
Artificial Intelligence (Al) Mobile Access —_ Healthcare Security  Cybelf —- iG) ocies > EMBEDDED
Microchip Debuts Cortex-M23
Mircochip First To Use Turstonic Revolutionary mcus
June 25,2018 &
Kinibi-M Platform For Microcontrollers Two of the first Cortex-M23 microcontrollers
have arrived—developed by Microchip—and
advanced security is among the features.
William G. Wong
TRUSTONIC 4 *S HRLD inl FOX Mista
~~) TODAY
Flying Vehicles Vv Smart Cities Vv Transportation ¥ Robotics IIoT v Security Vv More ¥
Not just droning on! The rise of Kinibi- Mit Trustonic Embeds IoT Security Technology in Microchip
MCU
31 OCTOBER 2017 The IoT security technology will be embedded at the chip level using Trustonic’s Kinibi-M software.
> A n = NEWSLETTER MEDIA EVENTS SHOP RSS @ @encush M XK in
lektroniknet.de Markt&Technik | Elektronik] Elektronik Ekoni
CLOUD DESIGN + OPTIMISATION ENERGY MANAGEMENT HOSTING + COLOCATION INFRASTRU§ = Rubrics | ticker Pictures videos Market overviews White paper Web seminars glossary Q
Trustonic launches loT device security Microchip introduces SAM L10/L11 MCUs
solution
slockchain-based Digital Holograms, trusted device provisioning and a modular, AFM Cortex-M23 plus on-chip security for the loT
secure OS combine to bring trust to constrained loT devices.
&3 6 years ago Posted in June 25, 2018, 12:30 am | Frank Riemenschneider
```

## Slide 103

###### MICROCHIP SAML11

**ESRGv3**

**BLACKHAT24**

## Slide 104

###### MICROCHIP SAML11

**ESRGv3**

**BLACKHAT24**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
MICROCHIP SAML11
Overview
The SAML11 Xplained Pro evaluation kit is ideal for evaluating and prototyping with the ultra low
power SAML11 ARM® Cortex®-M23 based microcontrollers integrating robust security which
includes ARM® TrustZone®, secure boot, crypto acceleration, secure key storage and chip-level
tamper detection. In addition to security the SAM L11 MCU features general purpose embedded
control capabilities with enhanced peripheral touch controller and advanced analog.
ESRGv3 BLACKHAT24
```

## Slide 105

###### MICROCHIP SAML11

**ESRGv3**

**BLACKHAT24**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
MICROCHIP SAML11
Overview
The SAML11 Xplained Pro evaluation kit is ideal for evaluating and prototyping with the ultra low
power SAML11 ARM® Cortex®-M23 based microcontrollers integrating robust security which
includes ARM® TrustZone®, secure boot, crypto acceleration, secure key storage and chip-level
tamper detection. In addition to security the SAM L11 MCU features general purpose embedded
control capabilities with enhanced peripheral touch controller and advanced analog.
ESRGv3 BLACKHAT24
```

## Slide 106

###### MICROCHIP SAML11

**ESRGv3**

**BLACKHAT24**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
MICROCHIP SAML11
Overview
The SAML11 Xplained Pro evaluation kit is ideal for evaluating and prototyping with the ultra low
power SAML11 ARM® Cortex®-M23 based microcontrollers integrating robust security which
includes ARM® TrustZone®, secure boot, crypto acceleration, secure key storage and chip-level
tamper detection. In addition to security the SAM L11 MCU features general purpose embedded
control capabilities with enhanced peripheral touch controller and advanced analog.
ESRGv3 BLACKHAT24
```

## Slide 107

###### MICROCHIP SAML11

**ESRGv3**

**BLACKHAT24**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
MICROCHIP SAML11
Overview
The SAML11 Xplained Pro evaluation kit is ideal for evaluating and prototyping with the ultra low
power SAML11 ARM® Cortex®-M23 based microcontrollers integrating robust security which
includes ARM® TrustZone®, secure boot, crypto acceleration, secure key storage and chip-level
tamper detection. In addition to security the SAM L11 MCU features general purpose embedded
control capabilities with enhanced peripheral touch controller and advanced analog.
ESRGv3 BLACKHAT24
```

## Slide 108

###### MICROCHIP SAML11

**ESRGv3**

**BLACKHAT24**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
MICROCHIP SAML11
Overview
The SAML11 Xplained Pro evaluation kit is ideal for evaluating and prototyping with the ultra low
power SAML11 ARM® Cortex®-M23 based microcontrollers integrating robust security which
includes ARM® TrustZone®, secure boot, crypto acceleration, secure key storage and chip-level
tamper detection. In addition to security the SAM L11 MCU features general purpose embedded
control capabilities with enhanced peripheral touch controller and advanced analog.
ESRGv3 BLACKHAT24
```

## Slide 109

###### MICROCHIP SAML11

**ESRGv3**

**BLACKHAT24**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
MICROCHIP SAML11
Overview
The SAML11 Xplained Pro evaluation kit is ideal for evaluating and prototyping with the ultra low
power SAML11 ARM® Cortex®-M23 based microcontrollers integrating robust security which
includes ARM® TrustZone®, secure boot, crypto acceleration, secure key storage and chip-level
tamper detection. In addition to security the SAM L11 MCU features general purpose embedded
control capabilities with enhanced peripheral touch controller and advanced analog.
ESRGv3 BLACKHAT24
```

## Slide 110

###### MICROCHIP SAML11

**ESRGv3**

**BLACKHAT24**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
MICROCHIP SAML11
Overview
The SAML11 Xplained Pro evaluation kit is ideal for evaluating and prototyping with the ultra low
power SAML11 ARM® Cortex®-M23 based microcontrollers integrating robust security which
includes ARM® TrustZone®, secure boot, crypto acceleration, secure key storage and chip-level
tamper detection. In addition to security the SAM L11 MCU features general purpose embedded
control capabilities with enhanced peripheral touch controller and advanced analog.
ESRGv3 BLACKHAT24
```

## Slide 111

###### MICROCHIP SAML11

**ESRGv3**

**BLACKHAT24**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
MICROCHIP SAML11
Overview
The SAML11 Xplained Pro evaluation kit is ideal for evaluating and prototyping with the ultra low
power SAML11 ARM® Cortex®-M23 based microcontrollers integrating robust security which
includes ARM® TrustZone®, secure boot, crypto acceleration, secure key storage and chip-level
tamper detection. In addition to security the SAM L11 MCU features general purpose embedded
control capabilities with enhanced peripheral touch controller and advanced analog.
ESRGv3 BLACKHAT24
```

## Slide 112

Pag. 17 - Microchip. SAM L10/L11 Family Data Sheet. Tech. rep. Microchip, June 2020.

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
I sav 11 Added
64/32/16 KB Flash
Crypto Accelerators with Cache
(AES128, SHA256, GCM)
| MPU 2KB Data Flash
16/8/8 KB RAM (SAM L11)
PROCESSOR .
SWCLK SERIAL cae 32 Mele 128-bit_ Unique ID 16/8/4 KB RAM (SAM L10)
WDI
S Oo WIRE NVM EVENT
TrustZone for ARMv8-M
Se CONTROLLER SRAM CONTROLLER
DEVICE
SERVICE ao i ‘it y _ 48 4s
UNIT
» M M M
<
CRC-32 ob
High-Speed Bus Matrix
8 KB ROM
Secure
8
S Ss
ZN VAN ZN
tt XZ KZ XA
AHB-APB AHB-APB AHB-APB
BRIDGE B BRIDGE A BRIDGE C
(APBB) (APBA) (APBC)
Pag. 17 - Microchip. SAM L10/L11 Family Data Sheet. Tech. rep. Microchip, June 2020.
```

## Slide 113

MPU

Pag. 17 - Microchip. SAM L10/L11 Family Data Sheet. Tech. rep. Microchip, June 2020.

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
| SAM L11 Added
64/32/16 KB Flash
Crypto A M with Cache
(AES128, §
2KB Data Flash
Cortex-M23 16/8/8 KB RAM (SAM L11)
PROCESSOR
SWCLK F F
SWDIO WIRE
NVM EVENT
TrustZone for ARMv8-M
Se CONTROLLER SRAM CONTROLLER
DEVICE
a ai r= =|
CRC-32
=
High-Speed Bus Matrix
8 KB ROM
Secure
8
S S
ZN ZN ZN
ls \Z \Z XZ
AHB-APB AHB-APB AHB-APB
BRIDGE B BRIDGE A BRIDGE C
(APBB) (APBA) (APBC)
Pag. 17 - Microchip. SAM L10/L11 Family Data Sheet. Tech. rep. Microchip, June 2020.
```

## Slide 114

MPU
SAU

Pag. 17 - Microchip. SAM L10/L11 Family Data Sheet. Tech. rep. Microchip, June 2020.

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Crypto A
(AES128, §
DEVICE
SERVICE
UNIT
CRC-32
Cortex-M23
PROCESSOR
Fmax 32 MHz
TrustZone for ARMv8-M
64/32/16 KB Flash
with Cache
| SAM L11 Added
2KB Data Flash
Scrambling
128-bit Unique ID
16/8/8 KB RAM (SAM L11)
16/8/4 KB RAM (SAM L10)
NVM EVENT
CONTROLLER
SRAM CONTROLLER
4\ Z2\
8 KB ROM
Secure
Boot
»s
=
High-Speed Bus Matrix
cS)
>
VAN
Z~
VAN
Rv,
XZ
NZ
AHB-APB
BRIDGE B
(APBB)
AHB-APB
BRIDGE A
(APBA)
AHB-APB
BRIDGE C
(APBC)
Pag. 17 - Microchip. SAM L10/L11 Family Data Sheet. Tech. rep. Microchip, June 2020.
```

## Slide 115

MPU
SAU
IDAU

Pag. 17 - Microchip. SAM L10/L11 Family Data Sheet. Tech. rep. Microchip, June 2020.

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
(AES128, §
Cortex-M23
PROCESSOR
Fmax 32 MHz
64/32/16 KB Flash
with Cache
| SAM L11 Added
2KB Data Flash
Scrambling
128-bit Unique ID
16/8/8 KB RAM (SAM L11)
16/8/4 KB RAM (SAM L10)
NVM EVENT
CONTROLLER
SRAM CONTROLLER
4\ Z2\
8 KB ROM
Secure
Boot
»
1 &
High-Speed Bus Matrix
cS)
>
VAN Z~
VAN
Rez <7
NZ
AHB-APB AHB-APB
BRIDGE B BRIDGE A
(APBB) (APBA)
AHB-APB
BRIDGE C
(APBC)
Pag. 17 - Microchip. SAM L10/L11 Family Data Sheet. Tech. rep. Microchip, June 2020.
```

## Slide 116

MPU
SAU
IDAU
MPC ???

Pag. 17 - Microchip. SAM L10/L11 Family Data Sheet. Tech. rep. Microchip, June 2020.

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Crypto A
(AES128, §
VVII\wW
8 KB ROM
Secure
Boot
Cortex-M23
PROCESSOR
Fmax 32 MHz
TrustZone for ARMv8-M
64/32/16 KB Flash
with Cache
| SAM L11 Added
2KB Data Flash
128-bit Unique ID
16/8/8 KB RAM (SAM L11)
16/8/4 KB RAM (SAM L10)
NVM EVENT
CONTROLLER
SRAM CONTROLLER
4\ Z2\
gL
Hig MPC 22? atrix
cS)
VAN
NZ
AHB-APB
BRIDGE B
(APBB)
AHB-APB
BRIDGE A
(APBA)
AHB-APB
BRIDGE C
(APBC)
Pag. 17 - Microchip. SAM L10/L11 Family Data Sheet. Tech. rep. Microchip, June 2020.
```

## Slide 117

MPU
SAU
IDAU
MPC ???

Pag. 17 - Microchip. SAM L10/L11 Family Data Sheet. Tech. rep. Microchip, June 2020.

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
8 KB ROM
Secure
Boot
Cortex-M23
PROCESSOR
Fmax 32 MHz
TrustZone for ARMv8-M
64/32/16 KB Flash
with Cache
| SAM L11 Added
2KB Data Flash
128-bit Unique ID
16/8/8 KB RAM (SAM L11)
16/8/4 KB RAM (SAM L10)
NVM EVENT
CONTROLLER
SRAM CONTROLLER
4\ Z2\
gL
AHB-APB
BRIDGE B
(APBB)
AHB-APB
BRIDGE A
(APBA)
AHB-APB
BRIDGE C
(APBC)
Pag. 17 - Microchip. SAM L10/L11 Family Data Sheet. Tech. rep. Microchip, June 2020.
```

## Slide 118

Pag. 53 - Microchip. SAM L10/L11 Family Data Sheet. Tech. rep. Microchip, June 2020.

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
SAM L11 Specific Security Features
This chapter provides an overview of the security features which are specific to the SAM L11.
Features
SAM L11-specific security features can be divided into two main categories.
The first category relates to the ARM TrustZone for Cortex-M technology features:
* Flexible hardware isolation of memories and peripherals:
Up to six regions for the Flash
Up to two regions for the Data Flash
Up to two regions for the SRAM
Individual security attribution (secure or non-secure) for each peripheral using the Peripheral Access
Controller (PAC)
Mix-Secure peripherals which support both secure and non-secure security attributions
* Three debug access levels allowing:
The highest debug level with no restrictions in term of memory and peripheral accesses
A restricted debug level with non-secure memory regions access only
The lowest debug level where no access is authorized except with a debugger using a Boot ROM-specific
mode
* Different chip erase support according to security settings
* Security configuration is fully stored in Flash and safely auto-loaded at startup during Boot ROM execution using
CRC checks
Pag. 53 - Microchip. SAM L10/L11 Family Data Sheet. Tech. rep. Microchip, June 2020.
```

## Slide 119

Pag. 53 - Microchip. SAM L10/L11 Family Data Sheet. Tech. rep. Microchip, June 2020.

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
SAM L11 Specific Security Features
This chapter provides an overview of the security features which are specific to the SAM L11.
Features
SAM L11-specific security features can be divided into two main categories.
The first category relates to the ARM TrustZone for Cortex-M technology features:
* Flexible hardware isolation of memories and peripherals:
Up to six regions for the Flash
Up to two regions for the Data Flash
Up to two regions for the SRAM
Individual security attribution (secure or non-secure) for each peripheral using the Peripheral Access
Controller (PAC)
Mix-Secure peripherals which support both secure and non-secure security attributions
Three debug access levels allowing:
The highest debug level with no restrictions in term of memory and peripheral accesses
A restricted debug level with non-secure memory regions access only
The lowest debug level where no access is authorized except with a debugger using a Boot ROM-specific
mode
Different chip erase support according to security settings
Security configuration is fully stored in Flash and safely auto-loaded at startup during Boot ROM execution using
CRC checks
Pag. 53 - Microchip. SAM L10/L11 Family Data Sheet. Tech. rep. Microchip, June 2020.
```

## Slide 120

Pag. 53 - Microchip. SAM L10/L11 Family Data Sheet. Tech. rep. Microchip, June 2020.

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
SAM L11 Specific Security Features
This chapter provides an overview of the security features which are specific to the SAM L11.
Features
SAM L11-specific security features can be divided into two main categories.
The first category relates to the ARM TrustZone for Cortex-M technology features:
* Flexible hardware isolation of memories and peripherals:
Up to six regions for the Flash
Up to two regions for the Data Flash
Up to two regions for the SRAM
Individual security attribution (secure or non-secure) for each peripheral using the Peripheral Access
Controller (PAC)
Mix-Secure peripherals which support both secure and non-secure security attributions
Three debug access levels allowing:
The highest debug level with no restrictions in term of memory and peripheral accesses
A restricted debug level with non-secure memory regions access only
— The lowest debug level where no access is authorized except with a debugger using a Boot ROM-specific
mode
Different chip erase support according to security settings
Security configuration is fully stored in Flash and safely auto-loaded at startup during Boot ROM execution using
CRC checks
Pag. 53 - Microchip. SAM L10/L11 Family Data Sheet. Tech. rep. Microchip, June 2020.
```

## Slide 121

Pag. 53 - Microchip. SAM L10/L11 Family Data Sheet. Tech. rep. Microchip, June 2020.

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
SAM L11 Specific Security Features
This chapter provides an overview of the security features which are specific to the SAM L11.
Features
SAM L11-specific security features can be divided into two main categories.
The first category relates to the ARM TrustZone for Cortex-M technology features:
* Flexible hardware isolation of memories and peripherals:
Up to six regions for the Flash
Up to two regions for the Data Flash
Up to two regions for the SRAM
Individual security attribution (secure or non-secure) for each peripheral using the Peripheral Access
Controller (PAC)
Mix-Secure peripherals which support both secure and non-secure security attributions
* Three debug access levels allowing:
— The highest debug level with no restrictions in term of memory and peripheral accesses
— A restricted debug level with non-secure memory regions access only
— The lowest debug level where no access is authorized except with a debugger using a Boot ROM-specific
mode
* Different chip erase support according to security settings
* Security configuration is fully stored in Flash and safely auto-loaded at startup during Boot ROM execution using
CRC checks
Pag. 53 - Microchip. SAM L10/L11 Family Data Sheet. Tech. rep. Microchip, June 2020.
```

## Slide 122

Pag. 53 - Microchip. SAM L10/L11 Family Data Sheet. Tech. rep. Microchip, June 2020.

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
SAM L11 Specific Security Features
This chapter provides an overview of the security features which are specific to the SAM L11.
Features
SAM L11-specific security features can be divided into two main categories.
The first category relates to the ARM TrustZone for Cortex-M technology features:
* Flexible hardware isolation of memories and peripherals:
Up to six regions for the Flash
Up to two regions for the Data Flash
Up to two regions for the SRAM
Individual security attribution (S@6UFeGPnoresecure) for each peripheral using the Peripheral Access
Controller (PAC)
Mix-Secure peripherals which support both secure and non-secure security attributions
* Three debug access levels allowing:
— The highest debug level with no restrictions in term of memory and peripheral accesses
— A restricted debug level with non-secure memory regions access only
— The lowest debug level where no access is authorized except with a debugger using a Boot ROM-specific
mode
* Different chip erase support according to security settings
* Security configuration is fully stored in Flash and safely auto-loaded at startup during Boot ROM execution using
CRC checks
Pag. 53 - Microchip. SAM L10/L11 Family Data Sheet. Tech. rep. Microchip, June 2020.
```

## Slide 123

What about **Privilege** and **NonPrivileged** ??

Pag. 53 - Microchip. SAM L10/L11 Family Data Sheet. Tech. rep. Microchip, June 2020.

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
SAM L11 Specific Security Features
This chapter provides an overview of the security features which are specific to the SAM L11.
What about
Features
SAM L11-specific security features
The first category relates to the ARM TrustZone for Cortex-M technology features:
* Flexible hardware isolation of memories and peripherals:
Up to six regions for the Flash
Up to two regions for the Data Flash
Up to two regions for the SRAM
Individual security attribution (S66UF6 GMnGhesecure) for each peripheral using the Peripheral Access
Controller (PAC)
Mix-Secure peripherals which support both secure and non-secure security attributions
Three debug access levels allowing:
— The highest debug level with no restrictions in term of memory and peripheral accesses
— Arestricted debug level with non-secure memory regions access only
— The lowest debug level where no access is authorized except with a debugger using a Boot ROM-specific
mode
Different chip erase support according to security settings
Security configuration is fully stored in Flash and safely auto-loaded at startup during Boot ROM execution using
CRC checks
Pag. 53 - Microchip. SAM L10/L11 Family Data Sheet. Tech. rep. Microchip, June 2020.
```

## Slide 124

What about **Privilege** and **NonPrivileged** ??

What about **Memory Protection** at the **System-Level** ??

Pag. 53 - Microchip. SAM L10/L11 Family Data Sheet. Tech. rep. Microchip, June 2020.

## Slide 125

What about **Privilege** and **NonPrivileged** ??

What about **Memory Protection** at the **System-Level** ??

Pag. 53 - Microchip. SAM L10/L11 Family Data Sheet. Tech. rep. Microchip, June 2020.

## Slide 126

###### SAML11 WEAK PROTECTIONS

Armv8-M CPU
Armv8-M Processor
Other
Core
DMA
Peripherals
TZ Access  Priv. Access
Permissions Permissions
TZ & Priv. Access  TZ & Priv. Access
Permissions Permissions
Memory

**ESRGv3**

**BLACKHAT24**

## Slide 127

###### SAML11 WEAK PROTECTIONS

Armv8-M CPU
PAC Distinguishes Only Security States
Armv8-M Processor
Other
Core
DMA
Peripherals
TZ Access  Priv. Access
Permissions Permissions
TZ & Priv. Access  TZ & Priv. Access
Permissions Permissions
Memory

**ESRGv3**

**BLACKHAT24**

## Slide 128

###### SAML11 WEAK PROTECTIONS

Armv8-M CPU
PAC Distinguishes Only Security States
NS NS
Armv8-M Processor
Other
Core
DMA
Peripherals
TZ Access  Priv. Access
Permissions Permissions
TZ & Priv. Access  TZ & Priv. Access
Permissions Permissions
Memory

**ESRGv3**

**BLACKHAT24**

## Slide 129

###### SAML11 WEAK PROTECTIONS

Armv8-M CPU
PAC Distinguishes Only Security States
S S
Armv8-M Processor
Other
Core
DMA
Peripherals
TZ Access  Priv. Access
Permissions Permissions
TZ & Priv. Access  TZ & Priv. Access
Permissions Permissions
Memory

**ESRGv3**

**BLACKHAT24**

## Slide 130

###### SAML11 WEAK PROTECTIONS

Armv8-M CPU
SAML11 doesn’t have MPC
S S
Armv8-M Processor
Other
Core
DMA
Peripherals
TZ Access  Priv. Access
Permissions Permissions
TZ & Priv. Access  TZ & Priv. Access
Permissions Permissions
Memory

**ESRGv3**

**BLACKHAT24**

## Slide 131

###### SAML11 WEAK PROTECTIONS

Armv8-M CPU
S. Unpriv. Try To Access S Priv Mem
S S
Armv8-M Processor Core
Secure Unprivileged
Other
DMA
Peripherals
TZ Access  Priv. Access
Permissions Permissions
Memory

**ESRGv3**

**BLACKHAT24**

## Slide 132

###### SAML11 WEAK PROTECTIONS

Armv8-M CPU
S. Unpriv. Try To Access S Priv Mem
S S
Armv8-M Processor Core
Secure Unprivileged
Other
DMA
Peripherals
TZ Access  Priv. Access
Permissions Permissions
Memory

**ESRGv3**

**BLACKHAT24**

## Slide 133

###### SAML11 WEAK PROTECTIONS

Armv8-M CPU
S. Unpriv. Try To Access S Priv Mem
S S
Armv8-M Processor Core
Secure Unprivileged
Other
DMA
Peripherals
TZ Access  Priv. Access
Permissions Permissions
Memory

**ESRGv3**

**BLACKHAT24**

## Slide 134

PSA Certification SAML11 SAML11

## Slide 135

#### PSA Certification

SAML11

## Slide 136

#### PSA Certification

SAML11

## Slide 137

#### PSA Certification

SAML11

## Slide 138

#### PSA Certification

SAML11

PSA Level 1

NORMAL WORLD SECURE WORLD
ARoTs
NSPE
SW PRoTs
Kernel
CPU

## Slide 139

#### PSA Certification

SAML11

PSA Level 1

NORMAL WORLD SECURE WORLD
ARoTs
NSPE
SW PRoTs
Kernel
CPU

## Slide 140

#### PSA Certification

SAML11

PSA Level 1

NORMAL WORLD SECURE WORLD
ARoTs
NSPE
SW PRoTs
Kernel
CPU

## Slide 141

#### PSA Certification

SAML11 + Kinibi-M

PSA Level 1

**NORMAL WORLD SECURE WORLD ARoTs NSPE SW** **PRoTs Kernel**

**CPU**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
SILICON SILICON |
SAML11-KPH SAM L11-KPH with Kinibi-M
v1.0
S S
MICROCHIP MICROCHIP
PSA Certification
psacertified™ psacertified™
level two | ready
PSA Level 1
NORMAL WORLD SECURE WORLD
NSPE
SW | PRoTs |
```

## Slide 142

#### PSA Certification

SAML11 + Kinibi-M

PSA Level 1

**NORMAL WORLD SECURE WORLD ARoTs NSPE SW** **PRoTs Kernel**

**CPU**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
SILICON SILICON |
SAML11-KPH SAM L11-KPH with Kinibi-M
v1.0
S S
MICROCHIP MICROCHIP
PSA Certification
psacertified™ psacertified™
level two | ready
PSA Level 1
NORMAL WORLD SECURE WORLD
NSPE
SW | PRoTs |
```

## Slide 143

#### PSA Certification

SAML11 + Kinibi-M

PSA Level 1

**NORMAL WORLD SECURE WORLD ARoTs NSPE SW** **PRoTs Kernel** **CPU**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
SILICON SILICON |
SAML11-KPH SAM L11-KPH with Kinibi-M
v1.0
S S
MICROCHIP MICROCHIP
PSA Certification
psacertified™
psacertified™
PSA Level 1
NORMAL WORLD SECURE WORLD
NSPE
SW | PRoTs |
```

## Slide 144

#### PSA Certification

SAML11 + Kinibi-M

PSA Level 1

**NORMAL WORLD SECURE WORLD ARoTs NSPE SW** **PRoTs**

**Kernel**

**CPU**

PSA Level 2

**NORMAL WORLD SECURE WORLD ARoTs NSPE SW** **PRoTs Kernel**

**CPU**

## Slide 145

#### PSA Certification

SAML11 + Kinibi-M

PSA Level 1

**NORMAL WORLD SECURE WORLD ARoTs NSPE SW** **PRoTs**

**Kernel**

**CPU**

PSA Level 2

**NORMAL WORLD SECURE WORLD ARoTs NSPE SW** **PRoTs Kernel**

**CPU**

## Slide 146

#### PSA Certification

SAML11 + Kinibi-M

PSA Level 1

**NORMAL WORLD SECURE WORLD ARoTs NSPE SW** **PRoTs**

**Kernel**

**CPU**

PSA Level 2

**NORMAL WORLD SECURE WORLD ARoTs NSPE SW** **PRoTs Kernel CPU**

## Slide 147

###### SAML11 WEAK PROTECTIONS

Armv8-M CPU
S S
Armv8-M Processor Core
Secure Unprivileged
Other
DMA
Peripherals
TZ Access  Priv. Access
Permissions Permissions
Memory

**ESRGv3**

**BLACKHAT24**

## Slide 148

###### SAML11 WEAK PROTECTIONS

Armv8-M CPU
PSA Level 2?
S S
Armv8-M Processor Core
Secure Unprivileged
Other
DMA
Peripherals
TZ Access  Priv. Access
Permissions Permissions
Memory

**ESRGv3**

**BLACKHAT24**

## Slide 149

###### SAML11 WEAK PROTECTIONS

Armv8-M CPU
PSA Level 2?
S S
Armv8-M Processor Core Secure Unprivileged
Other
Diffic ult W ithout MPC DMA
Peripherals
TZ Access  Priv. Access
Permissions Permissions
TZ & Priv. Access  TZ & Priv. Access
Permissions Permissions
Memory

**ESRGv3**

**BLACKHAT24**

## Slide 150

**_We report to Microchip that the lack of a MPC may create security issues, special in PSA level 2/3, Microchip didn’t take any actions!_**

Responsible Disclosure: Microchip

## Slide 151

## Trustonic SAML11 Kinibi-M

## Slide 152

###### TRUSTONIC KINIBI-M

**BLACKHAT24**

Image: Pag. 3 - Kinibi-M Developer’s Guide

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
TRUSTONIC KINIBI-M
fotolia al eel al le gd ed |
Non-secure} -Secure-World
Callable Eager
Memory ;
Non-secure
World
Crypto Attestation
module module
Storage
module
Application
|
|
Kinibi-M module API
Kinibi-M API Secure gateway Kinibi-M OS
| ARM TrustZone® enabled MCU
Figure 1: Kinibi-M Architecture Overview.
Image: Pag. 3 - Kinibi-M Developer’s Guide BLACKHAT 24
```

## Slide 153

###### TRUSTONIC KINIBI-M

###### PSA Level 2

NORMAL WORLD SECURE WORLD
CPU

**BLACKHAT24**

Image: Pag. 3 - Kinibi-M Developer’s Guide

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
TRUSTONIC KINIBI-M
' isiniaiaLaalelsiala, Woisioio PSA Level 2
Non-secure | Non-secure | Secure-World s
World ! Callable Ree
1 iv v : a.
Memory NORMAL WORLD SECURE WORLD
1 i §6Crypto | Attestation Storage
‘N i module module module
; a ae
Kinibi-M module API
Kinibi-M API Secure gateway Kinibi-M OS
CPU
ARM TrustZone® enabled MCU |
Figure 1: Kinibi-M Architecture Overview.
Image: Pag. 3 - Kinibi-M Developer’s Guide BLACKHAT 24
```

## Slide 154

###### TRUSTONIC KINIBI-M

PSA Level 2

NORMAL WORLD SECURE WORLD
NSPE
SW
CPU

**BLACKHAT24**

Image: Pag. 3 - Kinibi-M Developer’s Guide

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
TRUSTONIC KINIBI-M
Non-secure } Non-secure Secure-World PSA Level 2
Callabl
World Memory NORMAL WORLD SECURE WORLD
NSPE
SW.
Kinibi-lV: 4 PI
ARM TrustZone® enabled MCU |
Figure 1: Kinibi-M Architecture Overview.
Image: Pag. 3 - Kinibi-M Developer’s Guide BLACKHAT 24
```

## Slide 155

###### TRUSTONIC KINIBI-M

###### PSA Level 2

NORMAL WORLD SECURE WORLD
NSPE
SW
Kernel
CPU

**BLACKHAT24**

Image: Pag. 3 - Kinibi-M Developer’s Guide

## Slide 156

###### TRUSTONIC KINIBI-M

###### PSA Level 2

NORMAL WORLD SECURE WORLD
NSPE
SW
PRoTs
Kernel
CPU

Image: Pag. 3 - Kinibi-M Developer’s Guide

**BLACKHAT24**

## Slide 157

###### TRUSTONIC KINIBI-M

PSA Level 2

NORMAL WORLD SECURE WORLD
ARoTs
NSPE
Could be Both
SW
PRoTs
Kernel
CPU

**BLACKHAT24**

Image: Pag. 3 - Kinibi-M Developer’s Guide

## Slide 158

###### TRUSTONIC KINIBI-M

###### PSA Level 2

NORMAL WORLD SECURE WORLD
ARoTs
NSPE
SW
PRoTs
Kernel
CPU

Kinibi-M Refers to PRoT and ARoT as a Secure Module

**BLACKHAT24**

Image: Pag. 3 - Kinibi-M Developer’s Guide

## Slide 159

###### TRUSTONIC KINIBI-M

PSA Level 2
NORMAL WORLD SECURE WORLD
ARoTs
NSPE
SW
PRoTs
Kernel
Text: Pag. 4 - Kinibi-M Developer’s Guide
CPU
Kinibi-M Refers to PRoT and ARoT as a Secure Module
Image: Pag. 3 - Kinibi-M Developer’s Guide  BLACKHAT24

**BLACKHAT24**

## Slide 160

###### TRUSTONIC KINIBI-M

PSA Level 2
NORMAL WORLD SECURE WORLD
ARoTs
NSPE
SW
PRoTs
Kernel
Text: Pag. 4 - Kinibi-M Developer’s Guide
CPU
Kinibi-M Refers to PRoT and ARoT as a Secure Module
Image: Pag. 3 - Kinibi-M Developer’s Guide  BLACKHAT24

**BLACKHAT24**

## Slide 161

###### TRUSTONIC KINIBI-M

###### PSA Level 2

NORMAL WORLD SECURE WORLD
ARoTs
NSPE
SW
PRoTs
Kernel
CPU

Kinibi-M Refers to PRoT and ARoT as a Secure Module

**BLACKHAT24**

Image: Pag. 3 - Kinibi-M Developer’s Guide

## Slide 162

###### TRUSTONIC KINIBI-M

###### PSA Level 2

NORMAL WORLD SECURE WORLD
ARoTs PRoTs
NSPE
SW
Kernel
CPU

Kinibi-M Refers to PRoT and ARoT as a Secure Module

**BLACKHAT24**

Image: Pag. 3 - Kinibi-M Developer’s Guide

## Slide 163

###### TRUSTONIC KINIBI-M

PSA Level 2

NORMAL WORLD SECURE WORLD
ARoTs PRoTs
PSA Level 2 ??? NSPE
SW
Kernel

**CPU**

Kinibi-M Refers to PRoT and ARoT as a Secure Module

**BLACKHAT24**

Image: Pag. 3 - Kinibi-M Developer’s Guide

## Slide 164

KINIBI-M
PSA Level 2
NORMAL WORLD SECURE WORLD

###### TRUSTONIC KINIBI-M

**ARoTs PRoTs** PSA Level 2 ??? **NSPE SW Kernel**

**Text: Pag. 5 - Kinibi-M Developer’s Guide**

**CPU**

Kinibi-M Refers to PRoT and ARoT as a Secure Module Image: Pag. 3 - Kinibi-M Developer’s Guide

**BLACKHAT24**

## Slide 165

###### TRUSTONIC KINIBI-M

PSA Level 2 **NORMAL WORLD SECURE WORLD ARoTs PRoTs** PSA Level 2 ??? **NSPE SW Kernel**

**Text: Pag. 5 - Kinibi-M Developer’s Guide**

**CPU**

Kinibi-M Refers to PRoT and ARoT as a Secure Module Image: Pag. 3 - Kinibi-M Developer’s Guide

**BLACKHAT24**

## Slide 166

###### TRUSTONIC KINIBI-M

PSA Level 2 **NORMAL WORLD SECURE WORLD ARoTs PRoTs** PSA Level 2 ??? **NSPE SW Kernel**

**Text: Pag. 5 - Kinibi-M Developer’s Guide**

**CPU**

Kinibi-M Refers to PRoT and ARoT as a Secure Module Image: Pag. 3 - Kinibi-M Developer’s Guide

**BLACKHAT24**

## Slide 167

###### TRUSTONIC KINIBI-M

**Text: Pag. 5 - Kinibi-M Developer’s Guide**

PSA Level 2 **NORMAL WORLD SECURE WORLD ARoTs PRoTs** PSA Level 2 ??? **NSPE SW Kernel CPU**

Kinibi-M Refers to PRoT and ARoT as a Secure Module Image: Pag. 3 - Kinibi-M Developer’s Guide

**BLACKHAT24**

## Slide 168

###### TRUSTONIC KINIBI-M

PSA Level 2 **NORMAL WORLD SECURE WORLD ARoTs PRoTs** PSA Level 2 ??? **NSPE SW Kernel**

**Text: Pag. 5 - Kinibi-M Developer’s Guide**

**CPU** PSA Level 3 ??? Kinibi-M Refers to PRoT and ARoT as a Secure Module Image: Pag. 3 - Kinibi-M Developer’s Guide

**BLACKHAT24**

## Slide 169

###### TRUSTONIC KINIBI-M

NORMAL WORLD SECURE WORLD
ARoTs PRoTs
NSPE
SW
Kernel
CPU

**BLACKHAT24**

Text: Pag. 4 - Kinibi-M Developer’s Guide

## Slide 170

###### TRUSTONIC KINIBI-M

NORMAL WORLD SECURE WORLD
ARoT ARoT PRoT PRoT
1 N 1 N
NSPE
SW
Kernel
CPU

**BLACKHAT24**

Text: Pag. 4 - Kinibi-M Developer’s Guide

## Slide 171

###### TRUSTONIC KINIBI-M

NORMAL WORLD SECURE WORLD
ARoT ARoT PRoT PRoT
1 N 1 N
NSPE
SW
Kernel
CPU

Microkernel-like Architecture

**BLACKHAT24**

Text: Pag. 4 - Kinibi-M Developer’s Guide

## Slide 172

###### TRUSTONIC KINIBI-M

**NORMAL WORLD SECURE WORLD ARoT ARoT PRoT PRoT 1 N 1 N** PSA Level  ???? **NSPE SW Kernel**

**CPU**

Microkernel-like Architecture

**BLACKHAT24**

Text: Pag. 4 - Kinibi-M Developer’s Guide

## Slide 173

###### TRUSTONIC KINIBI-M

NORMAL WORLD SECURE WORLD
ARoTs PRoTs
NSPE
SW
Kernel
CPU

**BLACKHAT24**

Text: Pag. 4 - Kinibi-M Developer’s Guide

## Slide 174

###### TRUSTONIC KINIBI-M

MPU
NORMAL WORLD SECURE WORLD
ARoTs PRoTs
NSPE
SW
Kernel
CPU

**BLACKHAT24**

Text: Pag. 4 - Kinibi-M Developer’s Guide

## Slide 175

###### TRUSTONIC KINIBI-M

MPU
NORMAL WORLD SECURE WORLD
ARoTs PRoTs
Just MPU ???? NSPE
SW
Kernel
CPU

**BLACKHAT24**

Text: Pag. 4 - Kinibi-M Developer’s Guide

## Slide 176

###### TRUSTONIC KINIBI-M

NORMAL WORLD SECURE WORLD
ARoT ARoT PRoT PRoT
1 N 1 N
NSPE
SW
Kernel
CPU

###### Kinibi-M Architecture

**ESRGv3**

**BLACKHAT24**

## Slide 177

###### TRUSTONIC KINIBI-M

NORMAL WORLD SECURE WORLD
ARoT ARoT PRoT PRoT
1 N 1 N
NSPE
SW
Kernel
CPU

###### Kinibi-M Architecture

###### Seems Probably More then PSA Level 3

**ESRGv3**

**BLACKHAT24**

## Slide 178

###### TRUSTONIC KINIBI-M

NORMAL WORLD SECURE WORLD
ARoT ARoT PRoT PRoT
1 N 1 N
NSPE
SW
Kernel
CPU

###### Kinibi-M Architecture

###### Seems Probably More then PSA Level 3

**ESRGv3**

**BLACKHAT24**

## Slide 179

###### TRUSTONIC KINIBI-M

NORMAL WORLD SECURE WORLD
ARoT ARoT PRoT PRoT
1 N 1 N
NSPE
SW
Kernel
CPU

###### Kinibi-M Architecture Seems Probably More then PSA Level 3

###### Microchip SAML11

**ESRGv3**

**BLACKHAT24**

## Slide 180

###### TRUSTONIC KINIBI-M

NORMAL WORLD SECURE WORLD
ARoT ARoT PRoT PRoT
1 N 1 N
NSPE
SW
Kernel
CPU

Kinibi-M Architecture Seems Probably More then PSA Level 3

Microchip SAML11

Only PSA Level 1 & No MPC

**ESRGv3**

**BLACKHAT24**

## Slide 181

Kinibi-M TEE

###### **NORMAL WORLD**

**SECURE WORLD**

**ARoT ARoT PRoT PRoT 1 N 1 N NSPE SW**

**Kernel**

**CPU**

Kinibi-M Architecture Seems Probably More then PSA Level 3

Microchip SAML11

Only PSA Level 1 & No MPC

**ESRGv3**

**BLACKHAT24**

## Slide 182

###### TRUSTONIC KINIBI-M

NORMAL WORLD SECURE WORLD
ARoT ARoT PRoT PRoT
1 N 1 N
NSPE
SW
Kernel
CPU

Kinibi-M Architecture Seems Probably More then PSA Level 3

Microchip SAML11

Only PSA Level 1 & No MPC

**ESRGv3**

**BLACKHAT24**

## Slide 183

###### TRUSTONIC KINIBI-M

SAU+IDAU

NORMAL WORLD SECURE WORLD
ARoT ARoT PRoT PRoT
1 N 1 N
NSPE
SW
Kernel
CPU

###### Kinibi-M Architecture

Microchip SAML11

Seems Probably More then PSA Level 3

Only PSA Level 1 & No MPC

**ESRGv3**

**BLACKHAT24**

## Slide 184

###### TRUSTONIC KINIBI-M

NORMAL WORLD SECURE WORLD
ARoT ARoT PRoT PRoT
1 N 1 N
NSPE
SW
Kernel
CPU

###### SAU+IDAU

MPU

Kinibi-M Architecture Seems Probably More then PSA Level 3

Microchip SAML11

Only PSA Level 1 & No MPC

**ESRGv3**

**BLACKHAT24**

## Slide 185

###### TRUSTONIC KINIBI-M

NORMAL WORLD SECURE WORLD
ARoT ARoT PRoT PRoT
1 N 1 N
NSPE
SW
Kernel
CPU

SAU+IDAU MPC MPU

Kinibi-M Architecture Seems Probably More then PSA Level 3

Microchip SAML11

Only PSA Level 1 & No MPC

**ESRGv3**

**BLACKHAT24**

## Slide 186

**_With this gap of protection, a Secure Unprivileged application that has been granted a DMA can bypass all Kinibi-M security mechanism and achieve arbitrary read, write or execute capabilities_**

###### Observation

## Slide 187

Responsible Disclosure Trustonic SAML11 A Journey

## Slide 188

1

###### **We Contact Trustonic Reporting our Findings**

Jan 10<sup>th</sup> Jan 12<sup>th</sup>

Jan 30<sup>th</sup> Jan 31<sup>st</sup> Feb 9<sup>th</sup>

Feb 14<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

## Slide 189

###### **1 Trustonic Security Team Acknowledged the Reception of Our Report**

Feb 14 th Feb 16 th Mar 10 th

Jan 31 st

Feb 9 th

Jan 10<sup>th</sup>

Jan 12<sup>th</sup> Jan 30<sup>th</sup>

## Slide 190

1

###### **Trustonic Security Team Provided 1**<sup>**st**</sup> **Feedback**

Jan 30<sup>th</sup> Jan 31<sup>st</sup> Feb 9<sup>th</sup>

Feb 14<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

Jan 10<sup>th</sup> Jan 12<sup>th</sup>

## Slide 191

1

###### **We Respond to 1**<sup>**st**</sup> **Feedback**

Jan 30 th

Jan 12 th

Jan 31<sup>st</sup> Feb 9<sup>th</sup>

Feb 14<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

Jan 10<sup>th</sup>

## Slide 192

1

###### **Trustonic Security Team Provided 2**<sup>**nd**</sup> **Feedback**

Jan 30 th

Jan 12 th

Jan 31<sup>st</sup>

Feb 14<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

Jan 10<sup>th</sup>

Feb 9<sup>th</sup>

## Slide 193

1

###### **We Respond to 2**<sup>**nd**</sup> **Feedback**

Jan 30 th

Jan 12 th

Jan 31<sup>st</sup>

Feb 9<sup>th</sup>

Feb 14<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

Jan 10<sup>th</sup>

## Slide 194

1

###### **Trustonic Security Team Provided 3rd and last Feedback**

Jan 30 th

Jan 12 th

Jan 31 st

Feb 9 th

Feb 14<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

Jan 10<sup>th</sup>

## Slide 195

1

###### **We Sent a Last Response Wrapping up the Responsible Disclosure**

Jan 30 th

Jan 12 th

Jan 31<sup>st</sup>

Feb 9 th

Feb 14<sup>th</sup>

Mar 10<sup>th</sup>

Jan 10<sup>th</sup>

Feb 16<sup>th</sup>

## Slide 196

Jan 10<sup>th</sup> Jan 12<sup>th</sup> Jan 30<sup>th</sup> Jan 31<sup>st</sup> Feb 9<sup>th</sup> Feb 14<sup>th</sup> Feb 16<sup>th</sup> Mar 10<sup>th</sup>

## Slide 197

**Topic:** Evaluatoin SDK vs Comercial SDK

Jan 30<sup>th</sup>

Jan 31<sup>st</sup> Feb 9<sup>th</sup>

Feb 14<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

## Slide 198

**Topic:** Evaluatoin SDK vs Comercial SDK **Topic:** Attestation Secure Modules

Jan 31<sup>st</sup> Feb 9<sup>th</sup> Feb 14<sup>th</sup>

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

Jan 30<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

## Slide 199

**Topic:** Evaluatoin SDK vs Comercial SDK **Topic:** Attestation Secure Modules **Topic:** DMA Permissions

Jan 31<sup>st</sup>

Feb 14<sup>th</sup>

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

Jan 30<sup>th</sup>

Feb 9<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

## Slide 200

**Topic:** Evaluatoin SDK vs Comercial SDK **Topic:** Attestation Secure Modules **Topic:** DMA Permissions

Jan 31<sup>st</sup>

Feb 9<sup>th</sup>

Feb 14<sup>th</sup>

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

Jan 30<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

## Slide 201

###### **1 2 3**

###### **Topic:** Evaluatoin SDK vs Comercial SDK

**1**

   - **“** We note that you are **using the Kinibi-M evaluation SDK** , **not** the full ( **commercial** ) **production SDK** .

- (…) Kinibi-M evaluation (…) is deliberately more flexible than a commercial (…) production SDK”

Jan 30<sup>th</sup>

Jan 31<sup>st</sup> Feb 9<sup>th</sup> Feb 14<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

## Slide 202

###### **1 2 3**

###### **Topic:** Evaluatoin SDK vs Comercial SDK

**1**

   - **“** We note that you are **using the Kinibi-M evaluation SDK** , **not** the full ( **commercial** ) **production SDK** .

- (…) Kinibi-M evaluation (…) is deliberately more flexible than a commercial (…) production SDK”

**DISCLAIMER**

We were only granted access to the **evaluation SDK** , thus all assessments and **conclusions presented on this talk** are derived form documentation and artifacts **from the Evaluation SDK** .

Jan 30<sup>th</sup>

Jan 31<sup>st</sup>

Feb 9<sup>th</sup>

Feb 14<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

## Slide 203

###### **1 2 3**

###### **Topic:** Evaluatoin SDK vs Comercial SDK

**1**

- **“** We note that you are **using the Kinibi-M evaluation SDK** , **not** the full ( **commercial** ) **production SDK** .

- (…) Kinibi-M evaluation (…) is deliberately more flexible than a commercial (…) production SDK”

###### **DISCLAIMER**

We were only granted access to the **evaluation SDK** , thus all assessments and **conclusions presented on this talk** are derived form documentation and artifacts **from the Evaluation SDK** .

We **still think commercial version may suffer from the same problem** (the underlying architecture problem is the same, weak hardware protections on SAML11)

**1**

Jan 30<sup>th</sup>

Jan 31<sup>st</sup>

Feb 9<sup>th</sup>

Feb 14<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

## Slide 204

**Topic:** Evaluatoin SDK vs Comercial SDK **Topic:** Attestation Secure Modules **Topic:** DMA Permissions

Jan 10<sup>th</sup> Jan 12<sup>th</sup>

Jan 30<sup>th</sup> Jan 31<sup>st</sup> Feb 9<sup>th</sup> Feb 14<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

## Slide 205

**Topic:** Evaluatoin SDK vs Comercial SDK **Topic:** Attestation Secure Modules **Topic:** DMA Permissions

Jan 10<sup>th</sup> Jan 12<sup>th</sup>

Jan 30<sup>th</sup> Jan 31<sup>st</sup> Feb 9<sup>th</sup> Feb 14<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

## Slide 206

**1 2**

**3 Topic:** Attestation Secure Modules

**You cannot install malicious modules** because, “all **modules** must be **signed** , and are **validated** at **1** install time against a protected list of signing keys” (attestation).

Jan 30<sup>th</sup>

Jan 31<sup>st</sup> Feb 9<sup>th</sup> Feb 14<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

## Slide 207

**1 2**

**3 Topic:** Attestation Secure Modules

**You cannot install malicious modules** because, “all **modules** must be **signed** , and are **validated** at **1** install time against a protected list of signing keys” (attestation).

**DISCLAIMER**

The **Evaluation SDK doesn’t support attestation** of secure modules so we could freely instantiate secure modules, but in the **Commercial SDK only OEMs can instantiate modules** and they are all **signed** and **validated** .

Jan 30<sup>th</sup>

Jan 31<sup>st</sup>

Feb 9<sup>th</sup>

Feb 14<sup>th</sup>

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

## Slide 208

**1 2**

> **3 Topic:** Attestation Secure Modules

**You cannot install malicious modules** because, “all **modules** must be **signed** , and are **validated** at **1** install time against a protected list of signing keys” (attestation).

###### **DISCLAIMER**

The **Evaluation SDK doesn’t support attestation** of secure modules so we could freely instantiate secure modules, but in the **Commercial SDK only OEMs can instantiate modules** and they are all **signed** and **validated** .

**Attesting** OEMs’ **Secure Modules** offers **no guarantees** that the Secure Module has **no defects** .

**1**

Feb 14<sup>th</sup>

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

Jan 30<sup>th</sup>

Feb 9<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

Jan 31<sup>st</sup>

## Slide 209

###### **1 2**

**3 Topic:** Attestation Secure Modules

**You cannot install malicious modules** because, “all **modules** must be **signed** , and are **validated** at **1** install time against a protected list of signing keys” (attestation).

The **Evaluation SDK doesn’t support attestation** of secure modules so we could **DISCLAIMER** freely instantiate secure modules, but in the **Commercial SDK only OEMs can instantiate modules** and they are all **signed** and **validated** .

**Attesting** OEMs’ **Secure Modules** offers **no guarantees** that the Secure Module has **no defects** .

**1**

**Unless** OEMs code is **formally verified** (which, as far as we know, is not the industry standard) **we should** (by probability) **expect bugs** and vulnerabilities.

**1**

Jan 30<sup>th</sup> Jan 31<sup>st</sup> Feb 9<sup>th</sup>

Feb 14<sup>th</sup>

Jan 10<sup>th</sup> Jan 12<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

## Slide 210

###### TAKEAWAY

We argue that there is a **naive trust in OEM developers** . **Even if** there is **no 1 malicious intent** , unintended **bugs may be introduced in the code** which may lead to a vulnerability, e.g., privileged escalation.

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

Jan 30<sup>th</sup>

Feb 9<sup>th</sup>

Feb 14<sup>th</sup>

Feb 16<sup>th</sup>

Mar 10<sup>th</sup>

Jan 31<sup>st</sup>

## Slide 211

**Topic:** Evaluatoin SDK vs Comercial SDK **Topic:** Attestation Secure Modules **Topic:** DMA Permissions

Jan 10<sup>th</sup> Jan 12<sup>th</sup>

Jan 30<sup>th</sup> Jan 31<sup>st</sup> Feb 9<sup>th</sup> Feb 14<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

## Slide 212

**Topic:** Evaluatoin SDK vs Comercial SDK **Topic:** Attestation Secure Modules **Topic:** DMA Permissions

Jan 30<sup>th</sup> Jan 31<sup>st</sup> Feb 9<sup>th</sup> Feb 14<sup>th</sup>

Jan 10<sup>th</sup> Jan 12<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

## Slide 213

**1**

**2**

> **3 Topic:** DMA Permissions

It’s true that a **Secure Module with access to a DMA** " **can effectively access any part of the system** ", **1** it is " **a common limitation** of low-cost hardware, **however** it is **far from an open door** "

Jan 31<sup>st</sup>

Feb 9<sup>th</sup>

Feb 14<sup>th</sup>

Jan 10<sup>th</sup> Jan 12<sup>th</sup>

Jan 30<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

## Slide 214

**1**

**2**

> **3 Topic:** DMA Permissions

It’s true that a **Secure Module with access to a DMA** " **can effectively access any part of the system** ", **1** it is " **a common limitation** of low-cost hardware, **however** it is **far from an open door** "

- “ **Access** to the **DMA** controller **needs to be granted** , and the best practice guidance in the **production**

- **1 SDK** (which we acknowledge you do not have) **explains how to lock down** access to **devices** from less trusted developers”

Jan 31<sup>st</sup>

Feb 9<sup>th</sup>

Feb 14<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

Jan 10<sup>th</sup> Jan 12<sup>th</sup>

Jan 30<sup>th</sup>

## Slide 215

**1**

###### **2**

> **3 Topic:** DMA Permissions

It’s true that a **Secure Module with access to a DMA** " **can effectively access any part of the system** ", **1** it is " **a common limitation** of low-cost hardware, **however** it is **far from an open door** "

“ **Access** to the **DMA** controller **needs to be granted** , and the best practice guidance in the **production 1 SDK** (which we acknowledge you do not have) **explains how to lock down** access to **devices** from less trusted developers”

**Contradictory ideas** , on one side, Trustonic admits that a **Secure Module with DMA** access **has full access to the system** , and, on the other side, Trustonic claims that it **is not an open door** .

**1**

Feb 14<sup>th</sup>

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

Jan 30<sup>th</sup>

Feb 9<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

Jan 31<sup>st</sup>

## Slide 216

**1**

**2**

> **3 Topic:** DMA Permissions

It’s true that a **Secure Module with access to a DMA** " **can effectively access any part of the system** ", **1** it is " **a common limitation** of low-cost hardware, **however** it is **far from an open door** "

“ **Access** to the **DMA** controller **needs to be granted** , and the best practice guidance in the **production 1 SDK** (which we acknowledge you do not have) **explains how to lock down** access to **devices** from less trusted developers”

**Contradictory ideas** , on one side, Trustonic admits that a **Secure Module with DMA** access **has full access to the system** , and, on the other side, Trustonic claims that it **is not an open door** .

**DMA** access **should not** need to **be granted but MEDIATED** (because lack of hardware mechanisms). **Kinibi-B should mediate** access from **ALL Secure Modules** via DMA interposer.

**1**

**1**

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

Jan 30<sup>th</sup>

Feb 9<sup>th</sup>

Feb 14<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

Jan 31<sup>st</sup>

## Slide 217

**1**

**2**

> **3 Topic:** DMA Permissions

It’s true that a **Secure Module with access to a DMA** " **can effectively access any part of the system** ", **1** it is " **a common limitation** of low-cost hardware, **however** it is **far from an open door** "

“ **Access** to the **DMA** controller **needs to be granted** , and the best practice guidance in the **production 1 SDK** (which we acknowledge you do not have) **explains how to lock down** access to **devices** from less trusted developers”

**Contradictory ideas** , on one side, Trustonic admits that a **Secure Module with DMA** access **has full access to the system** , and, on the other side, Trustonic claims that it **is not an open door** .

**DMA** access **should not** need to **be granted but MEDIATED** (because lack of hardware mechanisms). **Kinibi-B should mediate** access from **ALL Secure Modules** via DMA interposer.

**We proposed** to share the **DMA interposer mechanism** to fix the DMA issue.

**1**

**1**

**1**

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

Jan 30<sup>th</sup> Jan 31<sup>st</sup>

Feb 9<sup>th</sup>

Feb 14<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

## Slide 218

###### TAKEAWAY

1

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

Jan 30<sup>th</sup>

Feb 9<sup>th</sup>

Feb 14<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

Jan 31<sup>st</sup>

## Slide 219

###### TAKEAWAY

We argue that there is a **lack of understanding of the limitations** of the **1 underlying hardware** (where Kinibi-M runs) and the necessary **Software mechanisms needed** to **enforce claimed protections** .

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

Jan 30<sup>th</sup>

Feb 9<sup>th</sup>

Feb 14<sup>th</sup>

Feb 16<sup>th</sup>

Mar 10<sup>th</sup>

Jan 31<sup>st</sup>

## Slide 220

Jan 10<sup>th</sup> Jan 12<sup>th</sup> Jan 30<sup>th</sup> Jan 31<sup>st</sup> Feb 9<sup>th</sup> Feb 14<sup>th</sup> Feb 16<sup>th</sup> Mar 10<sup>th</sup>

## Slide 221

**Topic:** No Native DMA Support

Jan 30<sup>th</sup> Jan 31<sup>st</sup> Feb 9<sup>th</sup> Feb 14<sup>th</sup> Feb 16<sup>th</sup> Mar 10<sup>th</sup>

Jan 10<sup>th</sup> Jan 12<sup>th</sup>

## Slide 222

**Topic:** No Native DMA Support **Topic:** No System MMU & DMA permissions

Jan 12<sup>th</sup>

Jan 30<sup>th</sup>

Jan 31<sup>st</sup>

Feb 14<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

Jan 10<sup>th</sup>

Feb 9<sup>th</sup>

## Slide 223

**Topic:** No Native DMA Support **Topic:** No System MMU & DMA permissions **Topic:** Native FLASH Access Mediation but not Native DMA mediation.

Jan 30<sup>th</sup>

Jan 31<sup>st</sup>

Feb 14<sup>th</sup> Feb 16<sup>th</sup> Mar 10<sup>th</sup>

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

Feb 9<sup>th</sup>

## Slide 224

**Topic:** No Native DMA Support **Topic:** No System MMU & DMA permissions **Topic:** Native FLASH Access Mediation but not Native DMA mediation.

Jan 30<sup>th</sup>

Jan 31<sup>st</sup> Feb 9<sup>th</sup> Feb 14<sup>th</sup> Feb 16<sup>th</sup> Mar 10<sup>th</sup>

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

## Slide 225

**1 2**

**3**

###### **Topic:** No Native DMA Support

“ **Kinibi-M** for SAML11 **does not ship with a Secure World DMA module** , and it is **left up to 1 customers** to source one or do without.”

Feb 9<sup>th</sup>

Feb 14<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

Jan 30<sup>th</sup>

Jan 31<sup>st</sup>

## Slide 226

**1 2**

**3**

###### **Topic:** No Native DMA Support

“ **Kinibi-M** for SAML11 **does not ship with a Secure World DMA module** , and it is **left up to 1 customers** to source one or do without.”

- **1** “In our architecture it **would be up to the OEM** provided **DMA module to provide that mediation** ”

Jan 30<sup>th</sup>

Feb 9<sup>th</sup>

Feb 14<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

Jan 31<sup>st</sup>

## Slide 227

**1 2**

**1**

###### **1**

###### **Topic:** No Native DMA Support

**3**

“ **Kinibi-M** for SAML11 **does not ship with a Secure World DMA module** , and it is **left up to customers** to source one or do without.”

“In our architecture it **would be up to the OEM** provided **DMA module to provide that mediation** ”

OEMs have to source one DMA module if they want to use a DMA. **We don’t think is a good approach** , because this **forces OEMs to trust each other** (which they don’t).

**1**

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

Jan 30<sup>th</sup>

Feb 9<sup>th</sup>

Feb 14<sup>th</sup>

Jan 31<sup>st</sup>

## Slide 228

###### **1 2**

**3**

###### **Topic:** No Native DMA Support

“ **Kinibi-M** for SAML11 **does not ship with a Secure World DMA module** , and it is **left up to 1 customers** to source one or do without.”

**1** “In our architecture it **would be up to the OEM** provided **DMA module to provide that mediation** ”

OEMs have to source one DMA module if they want to use a DMA. **We don’t think is a good approach** , because this **forces OEMs to trust each other** (which they don’t).

**1**

It also **increases** the **probability** of a **bug** / **vulnerability** .

**1**

Jan 10<sup>th</sup>

Feb 9 th

Feb 14<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

Jan 12<sup>th</sup>

Jan 30<sup>th</sup>

Jan 31<sup>st</sup>

## Slide 229

###### TAKEAWAY

1

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

Jan 30<sup>th</sup>

Feb 9<sup>th</sup>

Feb 14<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

Jan 31<sup>st</sup>

## Slide 230

###### TAKEAWAY

We argue that there is a **lack of understanding of multi-OEM threat model** . In a **1** multistakeholder scenario (i.e., multiple OEMs) **OEMs don’t trust each other** .

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

Jan 30<sup>th</sup>

Feb 9<sup>th</sup>

Feb 14<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

Jan 31<sup>st</sup>

## Slide 231

**Topic:** No Native DMA Support **Topic:** No System MMU & DMA permissions **Topic:** Native FLASH Access Mediation but not Native DMA mediation.

Jan 31<sup>st</sup> Feb 9<sup>th</sup> Feb 14<sup>th</sup> Feb 16<sup>th</sup> Mar 10<sup>th</sup>

Jan 10<sup>th</sup> Jan 12<sup>th</sup>

Jan 30<sup>th</sup>

## Slide 232

**Topic:** No Native DMA Support **Topic:** No System MMU & DMA permissions **Topic:** Native FLASH Access Mediation but not Native DMA mediation.

Jan 31<sup>st</sup> Feb 9<sup>th</sup> Feb 14<sup>th</sup> Feb 16<sup>th</sup> Mar 10<sup>th</sup>

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

Jan 30<sup>th</sup>

## Slide 233

**1 2 3**

###### **Topic:** No System MMU & DMA permissions

- “ **You have at most revealed** that this **device has no system MMU** (covered in the data sheet), and that

- **1 DMA permissions should not be granted** to untrusted application modules”

Jan 31<sup>st</sup>

Feb 9<sup>th</sup>

Feb 14<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

Jan 30<sup>th</sup>

## Slide 234

**1 2 3 Topic:** No System MMU & DMA permissions

**1**

- “ **You have at most revealed** that this **device has no system MMU** (covered in the data sheet), and that

- **DMA permissions should not be granted** to untrusted application modules”

**System MMU** is an access control IP used in **platforms with virtual memory** , In **Cortex-M (MCU** ) platforms, there are no SMMU, but **MPC** (Memory Protection Controller) and **PPC** (Peripheral Protection Controller)

**1**

Jan 30<sup>th</sup>

Jan 31<sup>st</sup>

Feb 9<sup>th</sup>

Feb 14<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

## Slide 235

**1 2**

**3**

###### **Topic:** No System MMU & DMA permissions

“ **You have at most revealed** that this **device has no system MMU** (covered in the data sheet), and that **1 DMA permissions should not be granted** to untrusted application modules”

**System MMU** is an access control IP used in **platforms with virtual memory** , In **Cortex-M (MCU** ) platforms, there are no SMMU, but **MPC** (Memory Protection Controller) and **PPC** (Peripheral Protection Controller)

**1**

The **PPC/MPC** in **SAML11 cannot enforce** access control in terms of **privilege levels** . **If you** directly **assign a DMA** device **to an OEM** you are basically **granting them full control of the system**

**1**

Jan 10<sup>th</sup>

Feb 14<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

Jan 12<sup>th</sup>

Jan 30<sup>th</sup>

Feb 9<sup>th</sup>

Jan 31<sup>st</sup>

## Slide 236

**1 2 3**

###### **Topic:** No System MMU & DMA permissions

“ **You have at most revealed** that this **device has no system MMU** (covered in the data sheet), and that **1 DMA permissions should not be granted** to untrusted application modules”

**System MMU** is an access control IP used in **platforms with virtual memory** , In **Cortex-M (MCU** ) platforms, there are no SMMU, but **MPC** (Memory Protection Controller) and **PPC** (Peripheral Protection Controller)

**1**

The **PPC/MPC** in **SAML11 cannot enforce** access control in terms of **privilege levels** . **If you** directly **assign a DMA** device **to an OEM** you are basically **granting them full control of the system**

**1**

**Kinibi-M should provide native DMA support** once it is a critical piece of infrastructure for Microcontrollers, due to the power and resource-constrained nature of this devices.

**1**

Jan 10<sup>th</sup>

Feb 9<sup>th</sup> Feb 14<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

Jan 12<sup>th</sup>

Jan 30<sup>th</sup>

Jan 31<sup>st</sup>

## Slide 237

###### TAKEAWAY

1

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

Jan 30<sup>th</sup>

Feb 9<sup>th</sup>

Feb 14<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

Jan 31<sup>st</sup>

## Slide 238

###### TAKEAWAY

We argue there is a **lack of understanding** about **the memory protection 1 controllers** of **Microcontrollers** (system wide protection mechanisms).

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

Jan 30<sup>th</sup>

Feb 9<sup>th</sup>

Feb 14<sup>th</sup>

Feb 16<sup>th</sup>

Mar 10<sup>th</sup>

Jan 31<sup>st</sup>

## Slide 239

**Topic:** No Native DMA Support **Topic:** No System MMU & DMA permissions **Topic:** Native FLASH Access Mediation but not Native DMA mediation.

Jan 31<sup>st</sup> Feb 9<sup>th</sup> Feb 14<sup>th</sup> Feb 16<sup>th</sup> Mar 10<sup>th</sup>

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

Jan 30<sup>th</sup>

## Slide 240

**Topic:** No Native DMA Support **Topic:** No System MMU & DMA permissions **Topic:** Native FLASH Access Mediation but not Native DMA mediation.

Feb 9<sup>th</sup> Feb 14<sup>th</sup> Feb 16<sup>th</sup> Mar 10<sup>th</sup>

Jan 10<sup>th</sup> Jan 12<sup>th</sup> Jan 30<sup>th</sup>

Jan 31<sup>st</sup>

## Slide 241

###### **1 2 3 Topic:** Native FLASH Access Mediation but not Native DMA mediation.

**1**

“Kinibi-M fully supports secure identification of module-to-module caller identity precisely to support this sort of use case. For example this is the pattern we use to **mediated access to flash storage provided by our secure storage module.”**

Feb 14<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

Jan 30<sup>th</sup>

Feb 9<sup>th</sup>

Jan 31<sup>st</sup>

## Slide 242

###### **1 2 3 Topic:** Native FLASH Access Mediation but not Native DMA mediation.

“Kinibi-M fully supports secure identification of module-to-module caller identity precisely to support **1** this sort of use case. For example this is the pattern we use to **mediated access to flash storage provided by our secure storage module.”**

**Kinibi-M provides mediation** for **flash** storage, but **why doesn't** it offer similar **mediation for DMA** ? DMA is also a critical service, arguably even more.

**1**

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

Jan 30<sup>th</sup>

Feb 9<sup>th</sup>

Feb 14<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

Jan 31<sup>st</sup>

## Slide 243

###### TAKEAWAY

1

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

Jan 30<sup>th</sup>

Feb 9<sup>th</sup>

Feb 14<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

Jan 31<sup>st</sup>

## Slide 244

###### TAKEAWAY

- We argue that there is a **lack of understanding** regarding the **criticality of a core service**

- **1 such as the DMA** . If mismanaged, it can grant full access to all system memory.

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

Jan 30<sup>th</sup>

Feb 9<sup>th</sup>

Feb 14<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

Jan 31<sup>st</sup>

## Slide 245

Jan 10<sup>th</sup> Jan 12<sup>th</sup> Jan 30<sup>th</sup> Jan 31<sup>st</sup> Feb 9<sup>th</sup> Feb 14<sup>th</sup> Feb 16<sup>th</sup> Mar 10<sup>th</sup>

## Slide 246

###### **Topic:** Clarification of Kinibi-M isolation levels

Jan 30<sup>th</sup>

Jan 31<sup>st</sup> Feb 9<sup>th</sup> Feb 14<sup>th</sup> Feb 16<sup>th</sup> Mar 10<sup>th</sup>

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

## Slide 247

**Topic:** Clarification of Kinibi-M isolation levels **Topic:** Clarification of who should provide DMA mediator

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

Jan 30<sup>th</sup>

Feb 9<sup>th</sup> Feb 14<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

Jan 31<sup>st</sup>

## Slide 248

**Topic:** Clarification of Kinibi-M isolation levels **Topic:** Clarification of who should provide DMA mediator **Topic:** Requests to Trustonic

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

Jan 30<sup>th</sup>

Feb 9<sup>th</sup> Feb 14<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

Jan 31<sup>st</sup>

## Slide 249

**Topic:** Clarification of Kinibi-M isolation levels **Topic:** Clarification of who should provide DMA mediator **Topic:** Requests to Trustonic

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

Jan 30<sup>th</sup>

Feb 9<sup>th</sup> Feb 14<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

Jan 31<sup>st</sup>

## Slide 250

###### **1 2 3**

###### **Topic:** Clarification of Kinibi-M isolation levels

**1**

- “ **Kinibi-M pre-dates Arm PSA** and was not built on the PSA architecture. (…) **In some areas we do**

- **more that PSA (any level) in others we do less** . That is why we do not claim PSA Level 3 and have not certified against it.”

Mar 10<sup>th</sup>

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

Jan 30<sup>th</sup>

Feb 9<sup>th</sup>

Feb 14<sup>th</sup>

Feb 16<sup>th</sup>

Jan 31<sup>st</sup>

## Slide 251

###### TAKEAWAY

1

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

Jan 30<sup>th</sup>

Feb 9<sup>th</sup>

Feb 14<sup>th</sup>

Feb 16<sup>th</sup>

Mar 10<sup>th</sup>

Jan 31<sup>st</sup>

## Slide 252

###### TAKEAWAY

- We argue there is **lack of awareness and mapping** regarding the **PSA isolation**

- **1 levels** on Kinibi-M.

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

Jan 30<sup>th</sup>

Feb 9<sup>th</sup>

Feb 14<sup>th</sup>

Feb 16<sup>th</sup>

Mar 10<sup>th</sup>

Jan 31<sup>st</sup>

## Slide 253

**Topic:** Clarification of Kinibi-M isolation levels **Topic:** Clarification of who should provide DMA mediator **Topic:** Requests to Trustonic

Feb 14<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

Jan 30<sup>th</sup>

Feb 9<sup>th</sup>

Jan 31<sup>st</sup>

## Slide 254

**Topic:** Clarification of Kinibi-M isolation levels **Topic:** Clarification of who should provide DMA mediator **Topic:** Requests to Trustonic

Jan 31<sup>st</sup> Feb 9<sup>th</sup> Feb 14<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

Jan 30<sup>th</sup>

## Slide 255

###### **1 2 3 Topic:** Clarification of who should provide DMA mediator

“This **device has only** (at most) **64kb of flash** and a **16kb of ram** . There are very few use cases for **1** secure world DMA. In practice **most customers simply disable the use of DMA in the secure world** , preventing any potential abuse.”

DMAs are key components (but bus masters!!) in MCU-based platforms, and not providing DMA

module (or let that for OEMs) is limiting the capabilities of the system from one side and leaving an

open threat vector on the other side.

Feb 14<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

Jan 30<sup>th</sup>

Feb 9<sup>th</sup>

Jan 31<sup>st</sup>

## Slide 256

###### **1 2 3 Topic:** Clarification of who should provide DMA mediator

“This **device has only** (at most) **64kb of flash** and a **16kb of ram** . There are very few use cases for **1** secure world DMA. In practice **most customers simply disable the use of DMA in the secure world** , preventing any potential abuse.”

“If needed, **DMA access should be** provided and **mediated by a “system” module** . That is what we **1** have said all along. **However** , that module needs to be **provided by an OEM** . **It is not provided by Trustonic** .”

DMAs are key components (but bus masters!!) in MCU-based platforms, and not providing DMA

module (or let that for OEMs) is limiting the capabilities of the system from one side and leaving an

open threat vector on the other side.

Jan 10<sup>th</sup>

Feb 14<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

Jan 12<sup>th</sup>

Jan 30<sup>th</sup>

Feb 9<sup>th</sup>

Jan 31<sup>st</sup>

## Slide 257

###### **1 2 3 Topic:** Clarification of who should provide DMA mediator

“This **device has only** (at most) **64kb of flash** and a **16kb of ram** . There are very few use cases for **1** secure world DMA. In practice **most customers simply disable the use of DMA in the secure world** , preventing any potential abuse.”

“If needed, **DMA access should be** provided and **mediated by a “system” module** . That is what we **1** have said all along. **However** , that module needs to be **provided by an OEM** . **It is not provided by Trustonic** .”

We strongly believe that **not providing DMA mediation** is **not** a **good security practice** .

**1**

Feb 14<sup>th</sup>

Feb 16<sup>th</sup>

Mar 10<sup>th</sup>

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

Jan 30<sup>th</sup>

Feb 9<sup>th</sup>

Jan 31<sup>st</sup>

## Slide 258

###### **1 2 3 Topic:** Clarification of who should provide DMA mediator

“This **device has only** (at most) **64kb of flash** and a **16kb of ram** . There are very few use cases for **1** secure world DMA. In practice **most customers simply disable the use of DMA in the secure world** , preventing any potential abuse.”

“If needed, **DMA access should be** provided and **mediated by a “system” module** . That is what we **1** have said all along. **However** , that module needs to be **provided by an OEM** . **It is not provided by Trustonic** .”

We strongly believe that **not providing DMA mediation** is **not** a **good security practice** .

**1**

**DMAs** are **key components** in **MCUs** (but bus masters!!). **Not providing** DMA module **is limiting** the **system’s capabilities** from one side and **leaving an open threat vector** on the other side.

**1**

Jan 10<sup>th</sup>

Feb 14<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

Jan 12<sup>th</sup>

Jan 30<sup>th</sup>

Feb 9<sup>th</sup>

Jan 31<sup>st</sup>

## Slide 259

**Topic:** Clarification of Kinibi-M isolation levels **Topic:** Clarification of who should provide DMA mediator **Topic:** Requests to Trustonic

Jan 31<sup>st</sup> Feb 9<sup>th</sup> Feb 14<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

Jan 30<sup>th</sup>

## Slide 260

**Topic:** Clarification of Kinibi-M isolation levels **Topic:** Clarification of who should provide DMA mediator **Topic:** Requests to Trustonic

Feb 14<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

Jan 31<sup>st</sup>

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

Jan 30<sup>th</sup>

Feb 9<sup>th</sup>

## Slide 261

**1 2 3**

###### Requests to Trustonic

To **issue** a **Security Advisory** .

Feb 14<sup>th</sup>

**1**

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

Jan 30<sup>th</sup>

Feb 9<sup>th</sup>

Jan 31<sup>st</sup>

## Slide 262

###### Requests to Trustonic

**1 2 3**

To **issue** a **Security Advisory** .

**Clarify** the **documentation** clearly communicating the limitations of **Evaluation** SDK **vs Commercial** SDK.

Feb 14<sup>th</sup>

Feb 16<sup>th</sup>

**1**

**1**

Mar 10<sup>th</sup>

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

Jan 30<sup>th</sup>

Feb 9<sup>th</sup>

Jan 31<sup>st</sup>

## Slide 263

###### Requests to Trustonic

**1 2 3**

To **issue** a **Security Advisory** .

**Clarify** the **documentation** clearly communicating the limitations of **Evaluation** SDK **vs Commercial** SDK.

Provide us **access** to the **Commercial SDK** for internal assessment.

Feb 14<sup>th</sup>

**1**

**1**

**1**

Mar 10<sup>th</sup>

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

Jan 30<sup>th</sup>

Feb 9<sup>th</sup>

Feb 16<sup>th</sup>

Jan 31<sup>st</sup>

## Slide 264

###### Requests to Trustonic

**3**

**1 2**

To **issue** a **Security Advisory** .

**Clarify** the **documentation** clearly communicating the limitations of **Evaluation** SDK **vs Commercial** SDK.

Provide us **access** to the **Commercial SDK** for internal assessment.

**1**

**1**

**1**

###### **NO RESPONSE TO OUR REQUESTS!**

Jan 31<sup>st</sup>

Feb 14<sup>th</sup>

Feb 16<sup>th</sup>

Mar 10<sup>th</sup>

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

Jan 30<sup>th</sup>

Feb 9<sup>th</sup>

## Slide 265

###### SUMMING UP

**1**

**2**

**3**

**4**

**5**

Jan 30<sup>th</sup>

**Jan 31**<sup>**st**</sup>

Feb 9<sup>th</sup>

Feb 14 th

Feb 16<sup>th</sup>

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

Mar 10<sup>th</sup>

## Slide 266

###### SUMMING UP

We **could only validate** our claims on **Evaluation SDK** (the only SDK we were granted **1** permissions);

**2**

**3**

**4**

**5**

Feb 14<sup>th</sup>

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

Jan 30<sup>th</sup>

Feb 9<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

**Jan 31**<sup>**st**</sup>

## Slide 267

###### SUMMING UP

We **could only validate** our claims on **Evaluation SDK** (the only SDK we were granted **1** permissions);

**2 Secure Modules** (from OEMs) are **signed and validated** on the **Commercial** Version;

**3**

**4**

**5**

Jan 30<sup>th</sup>

Feb 14<sup>th</sup>

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

Feb 9<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

**Jan 31**<sup>**st**</sup>

## Slide 268

###### SUMMING UP

- We **could only validate** our claims on **Evaluation SDK** (the only SDK we were granted

- **1** permissions);

**2 Secure Modules** (from OEMs) are **signed and validated** on the **Commercial** Version;

**3** We think **attestation is orthogonal** to the problem we discussed in this presentation;

**4**

**5**

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

Jan 30<sup>th</sup>

Feb 9<sup>th</sup>

Feb 14<sup>th</sup>

Feb 16<sup>th</sup>

Mar 10<sup>th</sup>

**Jan 31**<sup>**st**</sup>

## Slide 269

###### SUMMING UP

###### We **could only validate** our claims on **Evaluation SDK** (the only SDK we were granted **1** permissions);

###### **2**

**3**

**Secure Modules** (from OEMs) are **signed and validated** on the **Commercial** Version; We think **attestation is orthogonal** to the problem we discussed in this presentation;

**4**

- Official **Kinibi-m claims** only **PSA Level 2** ready, **but** its **secure architecture claims higher protections levels** (not backed by any hardware or software mechanism);

**5**

Jan 30<sup>th</sup>

Mar 10 th

Feb 9 th

Feb 14 th

Feb 16 th

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

**Jan 31**<sup>**st**</sup>

## Slide 270

###### SUMMING UP

###### We **could only validate** our claims on **Evaluation SDK** (the only SDK we were granted **1** permissions);

- **2 Secure Modules** (from OEMs) are **signed and validated** on the **Commercial** Version;

**3** We think **attestation is orthogonal** to the problem we discussed in this presentation;

- Official **Kinibi-m claims** only **PSA Level 2** ready, **but** its **secure architecture claims**

- **4 higher protections levels** (not backed by any hardware or software mechanism);

- There is **no DMA mediator** , the responsibility is **left to the OEMs** , and by default Kinibi-M

- **5** has no control of such an import core service, able to disrupt all system;

Feb 14<sup>th</sup>

Feb 16<sup>th</sup> Mar 10<sup>th</sup>

Jan 10<sup>th</sup>

Jan 12<sup>th</sup>

Jan 30<sup>th</sup>

Feb 9<sup>th</sup>

**Jan 31**<sup>**st**</sup>

## Slide 271

DMA Mediation SAML11

## Slide 272

###### DMA MEDIATION

NORMAL WORLD SECURE WORLD
ARoT 1 ARoT 2 PRoT 1
NSPE
SW
DMA
TEE Kernel
CPU PERIPH
MPU / SAU
MEMORY
UNPRIV
PRIV

**ESRGv3**

**BLACKHAT24**

## Slide 273

###### DMA MEDIATION

DMA Mediator
NORMAL WORLD SECURE WORLD
ARoT 1 ARoT 2 PRoT 1
NSPE
SW
DMA
TEE Kernel
CPU PERIPH
MPU / SAU
MEMORY
UNPRIV
PRIV

**ESRGv3**

**BLACKHAT24**

## Slide 274

###### DMA MEDIATION

WHITELIST MEMORY RANGE
ID BASE ADDR SIZE
NORMAL WORLD SECURE WORLD Unused Unused Unused
Unused Unused Unused
PRoT 1 Unused Unused Unused
ARoT 1 ARoT 2
DMA Mediator Unused Unused Unused
NSPE
SW Unused Unused Unused
DMA
TEE Kernel
CPU PERIPH
MPU / SAU
MEMORY
UNPRIV
PRIV

**ESRGv3**

**BLACKHAT24**

## Slide 275

###### DMA MEDIATION

NORMAL WORLD SECURE WORLD
PRoT 1
ARoT 1 ARoT 2
DMA Mediator
NSPE
SW
DMA
TEE Kernel
CPU PERIPH
MPU / SAU
MEMORY
UNPRIV
PRIV

###### **MEMORY RANGE**

###### **WHITELIST**

ID BASE ADDR SIZE
ARoT 1 Unused Unused
Unused Unused Unused
Unused Unused Unused
Unused Unused Unused
Unused Unused Unused

**ESRGv3**

**BLACKHAT24**

## Slide 276

###### DMA MEDIATION

NORMAL WORLD SECURE WORLD
PRoT 1
ARoT 1 ARoT 2
DMA Mediator
NSPE
SW
DMA
TEE Kernel
CPU PERIPH
MPU / SAU
MEMORY
UNPRIV
PRIV

###### **MEMORY RANGE**

###### **WHITELIST**

ID BASE ADDR SIZE
ARoT 1 0x20000000 0x1000
Unused Unused Unused
Unused Unused Unused
Unused Unused Unused
Unused Unused Unused

**ESRGv3**

**BLACKHAT24**

## Slide 277

###### DMA MEDIATION

NORMAL WORLD SECURE WORLD
PRoT 1
ARoT 1 ARoT 2
DMA Mediator
NSPE
SW
DMA
1 TEE Kernel
CPU PERIPH
MPU / SAU
MEMORY
UNPRIV
PRIV

###### **MEMORY RANGE**

###### **WHITELIST**

ID BASE ADDR SIZE
ARoT 1 0x20000000 0x1000
Unused Unused Unused
Unused Unused Unused
Unused Unused Unused
Unused Unused Unused

1 NS calls ARoT 1

**ESRGv3**

**BLACKHAT24**

## Slide 278

###### DMA MEDIATION

NORMAL WORLD SECURE WORLD
PRoT 1
ARoT 1 ARoT 2
DMA Mediator
NSPE
SW 2
DMA
1 TEE Kernel M2M
Binding
CPU PERIPH
MPU / SAU
MEMORY
UNPRIV
PRIV

###### **MEMORY RANGE**

###### **WHITELIST**

ID BASE ADDR SIZE
ARoT 1 0x20000000 0x1000
Unused Unused Unused
Unused Unused Unused
Unused Unused Unused
Unused Unused Unused

- 1 NS calls ARoT 1 2 ARoT 1 requests access to DMA mediator

**ESRGv3**

**BLACKHAT24**

## Slide 279

###### DMA MEDIATION

NORMAL WORLD SECURE WORLD
PRoT 1
ARoT 1 ARoT 2
DMA Mediator
NSPE
SW 2 3
DMA
1 TEE Kernel M2M
Binding
CPU PERIPH
MPU / SAU
MEMORY
UNPRIV
PRIV

###### **MEMORY RANGE**

###### **WHITELIST**

ID BASE ADDR SIZE
ARoT 1 0x20000000 0x1000
Unused Unused Unused
Unused Unused Unused
Unused Unused Unused
Unused Unused Unused

- 1 NS calls ARoT 1 2 ARoT 1 requests access to DMA mediator

3 TEE Kernel Invokes DMA Mediator

**ESRGv3**

**BLACKHAT24**

## Slide 280

###### DMA MEDIATION

###### **MEMORY RANGE**

WHITELIST MEMORY RANGE
ID BASE ADDR SIZE
NORMAL WORLD SECURE WORLD ARoT 1 0x20000000 0x1000
Unused Unused Unused
4
PRoT 1 Unused Unused Unused
ARoT 1 ARoT 2
NSPE DMA Mediator Unused Unused Unused
SW 2 3 Unused Unused Unused
DMA
1 TEE Kernel M2M
Binding
CPU PERIPH
MPU / SAU
MEMORY
UNPRIV
PRIV

1 NS calls ARoT 1 4 DMA Mediator Checks Access Permissions and Memory Range 2 ARoT 1 requests access to DMA mediator

3 TEE Kernel Invokes DMA Mediator

**ESRGv3**

**BLACKHAT24**

## Slide 281

###### DMA MEDIATION

###### **MEMORY RANGE**

WHITELIST MEMORY RANGE
ID BASE ADDR SIZE
NORMAL WORLD SECURE WORLD ARoT 1 0x20000000 0x1000
Unused Unused Unused
4
PRoT 1 Unused Unused Unused
ARoT 1 ARoT 2
NSPE DMA Mediator Unused Unused Unused
SW 2 3 Unused Unused Unused
DMA 5
1 TEE Kernel M2M
Binding
CPU PERIPH
MPU / SAU
MEMORY
UNPRIV
PRIV

4 DMA Mediator Checks Access Permissions and Memory Range

1 NS calls ARoT 1 4 DMA Mediator Checks Access Permissions and Memory Range 2 ARoT 1 requests access to DMA mediator 5<sup>DMA Memory Access Granted to ARoT 1</sup>

3 TEE Kernel Invokes DMA Mediator

**ESRGv3**

**BLACKHAT24**

## Slide 282

###### DMA MEDIATION

WHITELIST MEMORY RANGE
ID BASE ADDR SIZE
NORMAL WORLD SECURE WORLD ARoT 1 0x20000000 0x1000
Unused Unused Unused
4
PRoT 1 Unused Unused Unused
ARoT 1 ARoT 2
NSPE DMA Mediator Unused Unused Unused
SW 2 A 3 Unused Unused Unused
DMA 5
1 TEE Kernel M2M
Binding
CPU PERIPH
MPU / SAU
MEMORY
UNPRIV
PRIV

1 NS calls ARoT 1 2 ARoT 1 requests access to DMA mediator

4 DMA Mediator Checks Access Permissions and Memory Range

5<sup>DMA Memory Access Granted to ARoT 1</sup>

3 TEE Kernel Invokes DMA Mediator **ESRGv3**

A ARoT 2 requests access to DMA mediator

**BLACKHAT24**

## Slide 283

###### DMA MEDIATION

###### **MEMORY RANGE**

WHITELIST MEMORY RANGE
ID BASE ADDR SIZE
NORMAL WORLD SECURE WORLD ARoT 1 0x20000000 0x1000
Unused Unused Unused
4
PRoT 1 Unused Unused Unused
ARoT 1 ARoT 2
NSPE DMA Mediator Unused Unused Unused
SW 2 A 3 Unused Unused Unused
DMA 5
1 TEE Kernel M2M
Binding
CPU PERIPH
MPU / SAU
MEMORY
UNPRIV
PRIV

1 NS calls ARoT 1 4 DMA Mediator Checks Access Permissions and Memory Range 2 ARoT 1 requests access to DMA mediator 5<sup>DMA Memory Access Granted to ARoT 1</sup>

ARoT 2 is not on the DMA Mediator Whitelist, requested is rejected

3 TEE Kernel Invokes DMA Mediator A ARoT 2 requests access to DMA mediator **ESRGv3**

**BLACKHAT24**

## Slide 284

##### **What Can Go Wrong**

**Attack Examples and “Live” Demo**

## Slide 285

WHEN WE WANT “PSA 3+” ISOLATION

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
NORMAL WORLD SECURE WORLD
WHEN WE WANT =| ial | a |
ae
Kinibi-M Architecture
Seems Probably More then PSA Level 3
```

## Slide 286

###### NO MPC

###### BUT THE MCU HAS NO MPC

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Armv8-M CPU
BUT THE MCU eae "
Peripherals
TZ Access Priv. Access
Permissions Permissions
```

## Slide 287

AND FIRMWARE HAS NO DMA MEDIATION

## Slide 288

AND FIRMWARE HAS
NO DMA MEDIATION

## Slide 289

###### POTENTIAL EXPLOITS

**Arbitrary Code Execution in Secure Privilege Mode 01 Demonstrates** the capability to directly tamper with Kinibi-M and achieve Attack 1 **arbitrary code execution** in **secure privileged mode** , rendering all Kinibi-M memory protections ineffective. **Steal Proprietary Code from a Secure Module 02 Demonstrates** the capability to **read arbitrary CODE memory** from other Attack 2 secure modules and entirely bypass Kinibi-M’s system memory protections.

**~~03~~**

**Steal Cryptographic Keys from Kinibi-M Secure Storage 03 Demonstrates** the capability to **read** and **write arbitrary DATA memory** from other secure modules and entirely bypass Kinibi-M’s system memory protections.

Attack 3

**ESRGv3**

**BLACKHAT24**

## Slide 290

###### POTENTIAL EXPLOITS

###### **Arbitrary Code Execution in Secure Privilege Mode**

**01 Demonstrates** the capability to directly tamper with Kinibi-M and achieve **arbitrary code execution** in **secure privileged mode** , rendering all Kinibi-M memory protections ineffective.

###### Attack 1

###### **Steal Proprietary Code from a Secure Module**

**02 Demonstrates** the capability to **read arbitrary CODE memory** from other secure modules and entirely bypass Kinibi-M’s system memory protections.

Attack 2

**~~03~~**

###### **Steal Cryptographic Keys from Kinibi-M Secure Storage**

**03 Demonstrates** the capability to **read** and **write arbitrary DATA memory** from other secure modules and entirely bypass Kinibi-M’s system memory protections.

Attack 3

**ESRGv3**

**BLACKHAT24**

## Slide 291

###### POTENTIAL EXPLOITS

###### **Arbitrary Code Execution in Secure Privilege Mode**

**01 Demonstrates** the capability to directly tamper with Kinibi-M and achieve **arbitrary code execution** in **secure privileged mode** , rendering all Kinibi-M memory protections ineffective.

###### Attack 1

###### **Steal Proprietary Code from a Secure Module**

**02**

**Demonstrates** the capability to **read arbitrary CODE memory** from other secure modules and entirely bypass Kinibi-M’s system memory protections.

Attack 2

**~~03~~**

**Steal Cryptographic Keys from Kinibi-M Secure Storage**

**03 Demonstrates** the capability to **read** and **write arbitrary DATA memory** from other secure modules and entirely bypass Kinibi-M’s system memory protections.

Attack 3

**ESRGv3**

**BLACKHAT24**

## Slide 292

###### POTENTIAL EXPLOITS

###### **Arbitrary Code Execution in Secure Privilege Mode**

###### **01**

**Demonstrates** the capability to directly tamper with Kinibi-M and achieve **arbitrary code execution** in **secure privileged mode** , rendering all Kinibi-M memory protections ineffective.

###### Attack 1

###### **Steal Proprietary Code from a Secure Module**

###### **02**

**Demonstrates** the capability to **read arbitrary CODE memory** from other secure modules and entirely bypass Kinibi-M’s system memory protections.

Attack 2

**~~03~~**

###### **Steal Cryptographic Keys from Kinibi-M Secure Storage**

**03**

**Demonstrates** the capability to **read** and **write arbitrary DATA memory** from other secure modules and entirely bypass Kinibi-M’s system memory protections.

###### Attack 3

**ESRGv3**

**BLACKHAT24**

## Slide 293

###### POTENTIAL EXPLOITS

**Arbitrary Code Execution in Secure Privilege Mode 01 Demonstrates** the capability to directly tamper with Kinibi-M and achieve Attack 1 **arbitrary code execution** in **secure privileged mode** , rendering all Kinibi-M memory protections ineffective.

###### **Steal Proprietary Code from a Secure Module**

**02 Demonstrates** the capability to **read arbitrary CODE memory** from other secure modules and entirely bypass Kinibi-M’s system memory protections.

Attack 2

**~~03~~**

###### **Steal Cryptographic Keys from Kinibi-M Secure Storage**

**03 Demonstrates** the capability to **read** and **write arbitrary DATA memory** from other secure modules and entirely bypass Kinibi-M’s system memory protections.

Attack 3

**ESRGv3**

**BLACKHAT24**

## Slide 294

What are the consequences Steal Cryptographic Keys from Kinibi-M Secure Storage

## Slide 295

###### ATTACK 3 STEALING KEYS

NORMAL WORLD TZ SECURE WORLD
ARoT 1 ARoT 2 Secure
Back-End Crypto. Storage
Malicious App
Front-End
DMA
Kinibi-M
PERIPH CPU
MPU / SAU
DATA FLASH
Malicious Victim
ESRGv3

**BLACKHAT24**

## Slide 296

###### ATTACK 3 STEALING KEYS

NORMAL WORLD TZ SECURE WORLD
ARoT 1 ARoT 2 Secure
Back-End Crypto. Storage
Malicious App
Front-End
DMA
Kinibi-M
PERIPH CPU
MPU / SAU
DATA FLASH
Malicious Victim
ESRGv3

**BLACKHAT24**

## Slide 297

###### ATTACK 3 STEALING KEYS

NORMAL WORLD TZ SECURE WORLD
ARoT 1 ARoT 2 Secure
Back-End Crypto. Storage
Malicious App
Front-End
DMA
Kinibi-M
PERIPH CPU
MPU / SAU
DATA FLASH
Malicious Victim
ESRGv3

**BLACKHAT24**

## Slide 298

###### ATTACK 3 STEALING KEYS

NORMAL WORLD TZ SECURE WORLD
ARoT 1 ARoT 2TA 2 Secure
Back-End Crypto. Storage
Malicious App
0xdeadbeef
Front-End
DMA
Kinibi-M
PERIPH CPU
MPU / SAU
DATA FLASH
Malicious Victim
ESRGv3

**BLACKHAT24**

## Slide 299

###### ATTACK 3 STEALING KEYS

NORMAL WORLD TZ SECURE WORLD
1
ARoT 1 ARoT 2 Secure
Back-End Crypto. Storage
Malicious App
0xdeadbeef
Front-End
DMA
Kinibi-M
PERIPH CPU
MPU / SAU
DATA FLASH
Malicious Victim

**ESRGv3**

**BLACKHAT24**

## Slide 300

###### ATTACK 3 STEALING KEYS

NORMAL WORLD TZ SECURE WORLD
1
ARoT 1 ARoT 2 Secure
Back-End Crypto. Storage
Malicious App
0xdeadbeef
Front-End
2
DMA
Kinibi-M
PERIPH CPU
MPU / SAU
DATA FLASH
Malicious Victim

**ESRGv3**

**BLACKHAT24**

## Slide 301

###### ATTACK 3 STEALING KEYS

NORMAL WORLD TZ SECURE WORLD
3 1
ARoT 1 ARoT 2 Secure
Back-End Crypto. Storage
Malicious App
Front-End
2
DMA
Kinibi-M
PERIPH CPU
MPU / SAU
DATA FLASH 0xdeadbeef
Malicious Victim

**ESRGv3**

**BLACKHAT24**

## Slide 302

###### ATTACK 3 STEALING KEYS

NORMAL WORLD TZ SECURE WORLD
3 1
ARoT 1 ARoT 2 Secure
Back-End Crypto. Storage
Malicious App
Front-End
2
DMA
Kinibi-M
Text: Pag. 20 - Kinibi-M API Documentation
PERIPH CPU
MPU / SAU
DATA FLASH 0xdeadbeef
Malicious Victim
ESRGv3 BLACKHAT24

**BLACKHAT24**

## Slide 303

###### ATTACK 3 STEALING KEYS

NORMAL WORLD TZ SECURE WORLD
3 1
ARoT 1 ARoT 2 Secure
Back-End Crypto. Storage
Malicious App
Front-End
2
DMA
Kinibi-M
Text: Pag. 20 - Kinibi-M API Documentation
PERIPH CPU
MPU / SAU
DATA FLASH 0xdeadbeef
Malicious Victim
ESRGv3 BLACKHAT24

**BLACKHAT24**

## Slide 304

###### ATTACK 3 STEALING KEYS

NORMAL WORLD TZ SECURE WORLD
3 1
ARoT 1 ARoT 2 Secure
Back-End Crypto. Storage
Malicious App
Front-End
2
DMA
Kinibi-M
Text: Pag. 20 - Kinibi-M API Documentation
PERIPH CPU
MPU / SAU
DATA FLASH 0xdeadbeef
Malicious Victim
ESRGv3 BLACKHAT24

**BLACKHAT24**

## Slide 305

###### ATTACK 3 STEALING KEYS

NORMAL WORLD TZ SECURE WORLD
3 1
ARoT 1 ARoT 2 Secure
4
Back-End Crypto. Storage
Malicious App
Front-End
2
DMA
Kinibi-M
PERIPH CPU
MPU / SAU
DATA FLASH 0xdeadbeef
Malicious Victim

**ESRGv3**

**BLACKHAT24**

## Slide 306

###### ATTACK 3 STEALING KEYS

NORMAL WORLD TZ SECURE WORLD
3 1
ARoT 1 ARoT 2 Secure
4
Back-End Crypto. Storage
Malicious App
Front-End
2
DMA
Kinibi-M
5
PERIPH CPU
MPU / SAU
DATA FLASH 0xdeadbeef
Malicious Victim

**ESRGv3**

**BLACKHAT24**

## Slide 307

###### ATTACK 3 STEALING KEYS

NORMAL WORLD TZ SECURE WORLD
3 1
ARoT 1 ARoT 2 Secure
4
Back-End Crypto. Storage
Malicious App
0xdeadbeef Front-End
2
DMA
Kinibi-M
5
PERIPH CPU
MPU / SAU
DATA FLASH
Victim

Malicious

**ESRGv3**

**BLACKHAT24**

## Slide 308

###### ATTACK 3 STEALING KEYS

NORMAL WORLD TZ SECURE WORLD
3 1
ARoT 1 ARoT 2 Secure
4
Back-End Crypto. Storage
Malicious App
6
0xdeadbeef
Front-End
2
DMA
Kinibi-M
5
PERIPH CPU
MPU / SAU
DATA FLASH

Malicious Victim

**ESRGv3**

**BLACKHAT24**

## Slide 309

###### Live Demo

Video

**ESRGv3**

**BLACKHAT24**

## Slide 310

##### **Lessons Learned**

**Advices for HW & SW providers and System Designers**

## Slide 311

###### LESSONS

**ESRGv3**

**BLACKHAT24**

## Slide 312

<<<<<<<<<<
#1
For Hardware
Providers

###### LESSONS

**ESRGv3**

**BLACKHAT24**

## Slide 313

<<<<<<<<<<
#1
For Hardware
Providers

###### LESSONS

For Firmware
Providers
#2

**ESRGv3**

**BLACKHAT24**

## Slide 314

<<<<<<<<<<
#1
For Hardware
Providers

<<<<<<<<<<
#3
For System’s
Users

###### LESSONS

For Firmware
Providers
#2

**ESRGv3**

**BLACKHAT24**

## Slide 315

LESSONS
<<<<<<<<<<
#1
For Hardware
Providers
Hardware providers should
implement protections  at
For Firmware
the  system-level  that
takes in account both  Providers
privilege levels  and
security states .
#2
ESRGv3

<<<<<<<<<<
#3
For System’s
Users

**BLACKHAT24**

## Slide 316

###### LESSONS

<<<<<<<<<< **#1 For Hardware Providers RECOMENDED** Hardware providers should **implement protections** at **For Firmware** the **system-level** that takes in account both **Providers privilege levels** and **security states** . **#2**

<<<<<<<<<<
#3
For System’s
Users

**ESRGv3**

**BLACKHAT24**

## Slide 317

###### LESSONS

<<<<<<<<<< **#3 For System’s Users NOT RECOMENDED**

<<<<<<<<<< **#1 For Hardware Providers RECOMENDED** Hardware providers should **implement protections** at **For Firmware** the **system-level** that takes in account both **Providers privilege levels** and **security states** . **#2**

**ESRGv3**

**BLACKHAT24**

## Slide 318

LESSONS
NXP LPC5500
<<<<<<<<<< <<<<<<<<<<
#1  #3
For Hardware
For System’s
Providers
Users
MPC
NOT RECOMENDED
Hardware providers should
implement protections  at
For Firmware
PPC the system-lev el  that
takes in account both  Providers
privilege levels  and
security states .
#2
ESRGv3 BLACKHAT24

## Slide 319

LESSONS
NXP LPC5500
MICROCHIP SAML11
<<<<<<<<<< <<<<<<<<<<
#1  #3
For Hardware
For System’s
Providers
Users
MPC
MPC ???
Hardware providers should
implement protections  at
For Firmware
PPC the system-lev el  that
takes in account both  Providers
privilege levels  and
security states .
#2
ESRGv3 BLACKHAT24

## Slide 320

LESSONS
<<<<<<<<<<
#1
For Hardware
Providers
Hardware providers should
implement protections  at
For Firmware
the  system-level  that
takes in account both  Providers
privilege levels  and
security states .
#2
ESRGv3

<<<<<<<<<<
#3
For System’s
Users

**BLACKHAT24**

## Slide 321

LESSONS
<<<<<<<<<< <<<<<<<<<<
#1  <<<<<<<<<< #3
Firmware providers should
implement mechanisms
For Hardware
For System’s
that  enforce isolation
Providers defined in the PSA  Users
standard.
Hardware providers should
implement protections  at
For Firmware
the  system-level  that
takes in account both  Providers
privilege levels  and
security states .
#2
ESRGv3 BLACKHAT24

## Slide 322

LESSONS
<<<<<<<<<< <<<<<<<<<<
#1  <<<<<<<<<< #3
Firmware providers should
implement mechanisms
For Hardware
For System’s
that  enforce isolation
Providers defined in the PSA  Users
standard.
RECOMENDED NOT RECOMENDED
Hardware providers should
implement protections  at
For Firmware
the  system-level  that
takes in account both  Providers
privilege levels  and
security states .
#2
ESRGv3 BLACKHAT24

## Slide 323

###### LESSONS

**MULTIZONE #1**

**MULTIZONE** <<<<<<<<<< <<<<<<<<<< **#1** <<<<<<<<<< **#3** Firmware providers should implement mechanisms **For Hardware For System’s** that **enforce isolation Providers defined in the PSA Users “To enforce system separation standard. policies, MultiZone built-in support NOT RECOMENDED for protected DMA transfers traps all DMA requests and emulates the** Hardware providers should **implement protections** at **PMP logic in software” For Firmware** the **system-level** that **Pag. 19 - MultiZone. MultiZone® Security Reference** takes in account both **Providers Manual, RISC-V.  Tech. rep. MultiZone, Nov 2021. privilege levels** and **security states** .

**#2**

**ESRGv3**

**BLACKHAT24**

## Slide 324

###### LESSONS

**MULTIZONE #1**

<<<<<<<<<< **MULTIZONE KINIBI-M** <<<<<<<<<< **#1** <<<<<<<<<< **#3** Firmware providers should implement mechanisms **For Hardware For System’s** that **enforce isolation Providers defined in the PSA Users “To enforce system separation standard. policies, MultiZone built-in support for protected DMA transfers traps all DMA requests and emulates the** Hardware providers should **implement protections** at **PMP logic in software” For Firmware** the **system-level** that **Pag. 19 - MultiZone. MultiZone® Security Reference** takes in account both **Providers Manual, RISC-V.  Tech. rep. MultiZone, Nov 2021. privilege levels** and **security states** .

**#2**

**ESRGv3**

**BLACKHAT24**

## Slide 325

LESSONS
<<<<<<<<<< <<<<<<<<<<
#1  <<<<<<<<<< #3
Firmware providers should
implement mechanisms
For Hardware
For System’s
that  enforce isolation
Providers defined in the PSA  Users
standard.
Hardware providers should
implement protections  at
For Firmware
the  system-level  that
takes in account both  Providers
privilege levels  and
security states .
#2
ESRGv3 BLACKHAT24

## Slide 326

###### LESSONS

<<<<<<<<<< <<<<<<<<<< **#3** Firmware providers should implement mechanisms **For System’s** that **enforce isolation defined in the PSA Users standard.**

<<<<<<<<<< **#1** <<<<<<<<<< Firmware providers should implement mechanisms **For Hardware** that **enforce isolation Providers defined in the PSA standard.** Hardware providers should **implement protections** at **For Firmware** the **system-level** that takes in account both **Providers privilege levels** and **security states** . **#2**

**Users** (OEMs and software developers) **should be cautious in choosing the system** where they **want to deploy their software** .

**ESRGv3**

**BLACKHAT24**

## Slide 327

###### LESSONS

<<<<<<<<<< <<<<<<<<<< **#1** <<<<<<<<<< **#3** Firmware providers should implement mechanisms **For Hardware For System’s** that **enforce isolation Providers defined in the PSA Users standard.** WHY NOT AN EXTRA PSA LEVEL? Hardware providers should **Users** (OEMs and software **implement protections** at developers) **should be For Firmware** the **system-level** that **cautious in choosing the** takes in account both **Providers system** where they **want privilege levels** and **to deploy their software security states** . **#2**

**Users** (OEMs and software developers) **should be cautious in choosing the system** where they **want to deploy their software** .

**ESRGv3**

**BLACKHAT24**

## Slide 328

###### LESSONS

<<<<<<<<<< <<<<<<<<<< **#1** <<<<<<<<<< **#3** Firmware providers should **NORMAL WORLD SECURE WORLD** implement mechanisms **For Hardware For System’s** that **ARoTenforce isolation ARoT PRoT PRoT Providers defined in the PSA 1 N 1 N Users standard. NSPE SW Kernel** Hardware providers should **Users** (OEMs and software **implement protections** at developers) **should be For Firmware** the **system-level** that **cautious in choosing the CPU** takes in account both **Providers system** where they **want privilege levels** and **to deploy their software** . **security states** . **#2**

**ESRGv3**

**BLACKHAT24**

## Slide 329

##### **Summary**

**Final Thoughts and BH Sound Bytes**

## Slide 330

###### Responsible Disclosure

**ESRGv3**

**BLACKHAT24**

## Slide 331

###### Responsible Disclosure

###### **MICROCHIP**

**ESRGv3**

**BLACKHAT24**

## Slide 332

###### Responsible Disclosure

###### **MICROCHIP**

###### **TRUSTONIC**

Problem of the SW

**ESRGv3**

**BLACKHAT24**

## Slide 333

###### Responsible Disclosure

###### **MICROCHIP**

###### **TRUSTONIC**

**Problem of the SW It would be a Good Security Practice to Provide a MPC US**

**ESRGv3**

**BLACKHAT24**

## Slide 334

###### Responsible Disclosure

###### **MICROCHIP**

###### **TRUSTONIC**

**Problem of the SW It would be a Good Security Practice to Provide a MPC US**

**OEMs DMA Module is Responsibility of Developers**

**ESRGv3**

**BLACKHAT24**

## Slide 335

###### Responsible Disclosure

###### **MICROCHIP**

###### **TRUSTONIC**

**Problem of the SW It would be a Good Security Practice to Provide a MPC US**

**OEMs DMA Module is Responsibility of Developers**

**It would be a Good Security Practice to Provide DMA MEDIATION US**

**ESRGv3**

**BLACKHAT24**

## Slide 336

###### Responsible Disclosure

###### **MICROCHIP**

**Problem of the SW It would be a Good Security Practice to Provide a MPC**

**US**

**ATTESTATTION We signed all OEMs Secure Modules**

**TRUSTONIC**

**OEMs**

**DMA Module is Responsibility of Developers**

**It would be a Good Security Practice to Provide DMA MEDIATION US**

**ESRGv3**

**BLACKHAT24**

## Slide 337

Responsible Disclosure **ATTESTATION is ORTHOGONAL to the ATTESTATTION problem MICROCHIP We signed all OEMs TRUSTONIC Secure Modules Problem of the SW US OEMs DMA Module is Responsibility It would be a Good of Developers Security Practice to Provide a MPC It would be a Good Security Practice to Provide DMA MEDIATION US US ESRGv3 BLACKHAT2424**

**BLACKHAT2424**

## Slide 338

Responsible Disclosure **ATTESTATION is ORTHOGONAL to the ATTESTATTION problem MICROCHIP We signed all OEMs TRUSTONIC Secure Modules Problem of the SW US OEMs DMA Module is Responsibility It would be a Good of Developers Security Practice to Provide a MPC It would be a Good Security Practice to Provide DMA MEDIATION US EVALUATION SDK You Just Proved in an US Unsecure SDK Version ESRGv3 BLACKHAT2424**

**BLACKHAT2424**

## Slide 339

Responsible Disclosure **ATTESTATION is ORTHOGONAL to the ATTESTATTION problem MICROCHIP We signed all OEMs TRUSTONIC Secure Modules Problem of the SW US OEMs DMA Module is Responsibility It would be a Good of Developers Security Practice to Provide a MPC You Didn’t Provide us It would be a Good Security COMERCIAL SDK Practice to Provide DMA MEDIATION US EVALUATION SDK You Just Proved in an US Unsecure SDK Version ESRGv3 BLACKHAT2424**

**BLACKHAT2424**

## Slide 340

1. We shared our **journey** on fully **assessing** an **MCU-based TEE** ( **Kinibi-M** ) **targeting** a reference TrustZone-M hardware platform ( **SAML11** )

###### **Black Hat SOUND BYTES**

2. We presented how it is possible to **bypass CPUlevel isolation primitives** , and explain the design of a TEE **core mechanism (DMA Mediator)** to offer such protection;

3. We perform a **live demo** of one potential **exploit that retrieves a cryptographic key** from other Secure Partitions **bypassing all** hardware and software **TEE isolation boundaries.**

## Slide 341

# THANK YOU!

Cristiano Rodrigues  | Sandro Pinto, PhD (Centro ALGORITMI / LASI, Universidade do Minho)

**id9492@alunos.uminho.pt**

**@_CRodrigues__**

**sandro.pinto@dei.uminho.pt**

**@sandro2pinto**

## Slide 342

# Q&A

Cristiano Rodrigues  | Sandro Pinto, PhD (Centro ALGORITMI / LASI, Universidade do Minho)

**Cristiano Rodrigues**

**Sandro Pinto**
