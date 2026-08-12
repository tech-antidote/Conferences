---
title: "Hand Me Your Secret MCU"
speakers: ["Pinto"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2023"
edition: "ASIA"
year: 2023
source_pdf: "Black Hat Asia 2023 slides/AS-23-Pinto-Hand-Me-Your-Secret-MCU.pdf"
pages: 207
sha256: "f8f0c389af23a06b827892ea4588201a3ab76f6e7b5a87ccd828815a4c65f78c"
text_chars: 32611
ocr_pages: 79
has_ocr: true
redacted_secrets: 0
ocr_confidence: 86.0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T01:39:21Z"
---
# Hand Me Your Secret MCU

**Speakers:** Pinto  
**Conference:** Black Hat ASIA 2023  
**Source:** `Black Hat Asia 2023 slides/AS-23-Pinto-Hand-Me-Your-Secret-MCU.pdf` (207 pages)


## Slide 1

**Hand Me Your SECRET, MCU!** Microarchitectural Timing Attacks on Microcontrollers are Practical

**Cristiano Rodrigues | Sandro Pinto, PhD**

(Centro ALGORITMI / LASI, Universidade do Minho)

#BHASIA @BlackHatEvents

## Slide 2

### **Hand Me Your SECRET, MCU!** Microarchitectural Timing Attacks on Microcontrollers are Practical

**Cristiano Rodrigues | Sandro Pinto, PhD**

(Centro ALGORITMI / LASI, Universidade do Minho)

## Slide 3

#### Microarchitectural **SIDE-CHANNEL Attacks**

## Slide 4

CPU CPU CPU CPU
CPU CPU CPU CPU
Interconnect
CPU CPU CPU CPU
CPU CPU CPU CPU

Microarchitectural **SIDE-CHANNELS** Servers, PCs, Mobile

## Slide 5

Core Core Core Core
Core Core Core Core
Interconnect
Core Core Core Core
Core Core Core Core
CPU CPU CPU CPU
L1 L1 L1 L1 L1 L1 L1 L1
L2 L2 L2 L2
L3
M

##### Microarchitectural **SIDE-CHANNELS** Servers, PCs, Mobile

## Slide 6

Core Core Core Core
Core Core Core Core
Interconnect
Core Core Core Core
Core Core Core Core
CPU CPU CPU CPU
L1 L1 L1 L1 L1 L1 L1 L1
L2 L2 L2 L2
L3
M

##### Microarchitectural **SIDE-CHANNELS** Servers, PCs, Mobile

## Slide 7

Core Core Core Core
Pipeline
Core Core Core Core
Interrupt Cont.
Interconnect PredictorsCore
Prefetchers
Core Core Core Core
L1-I L1-D
Core Core Core Core
CPU CPU CPU CPU
L1 L1 L1 L1 L1 L1 L1 L1
L2 L2 L2 L2
L3
M

Microarchitectural **SIDE-CHANNELS** Servers, PCs, Mobile

## Slide 8

##### **Microcontrollers**

CPU
DMA
BUS interconnect
M P

## Slide 9

**_Which unique microarchitectural elements on MCUs may create new channels, and how can they be used to mount effective attacks?_**

Research Question

CPU
DMA
BUS interconnect
M P

## Slide 10

CPU
DMA
BUS interconnect
M P

**Novel Channel** BUS Interconnect

## Slide 11

CPU
DMA
BUS interconnect
M P

**BUS Interconnect** Arbitration logic

## Slide 12

CPU
DMA
BUS interconnect
M P

**Hardware Gadgets** Novel Concept

## Slide 13

CPU
DMA
BUS interconnect
M P

**Hardware Gadgets** Smart Gadget Network

## Slide 14

**BUSted** Attack

## Slide 15

NON-SECURE WORLD TZ SECURE WORLD
* * *
TA Victim
SPY
TF-M
Cortex-M

NS S

###### **TrustZone for Cortex-M**

# **BUSted** Attack

> Text below was recovered by OCR (confidence 88/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
NON-SECURE WORLD
TrustZone for Cortex-M
TZ
SECURE WORLD
Victim
BUSted
arm
CORTEX®-M23
TrustZone for Armv8-M
Nested vectored Wake-up
interrupt controller interrupt controller
Memory protection unit
Data
AHBS5 watchpoint JTAG
ETM trace cel petit
unit
ear GD erial wire
arm
CORTEX®-M33
Nested vectored
interrupt controller
Memory protection unit
2x AHB5S ITM trace
Coprocessor
Common Criteria
EAL6+ Certified
TruztZone for Armv8-M
Wake-up
interrupt controller
DSP. FPU
Data
watchpoint JTAG
Breakpoint
unit
Serial wire
MTB
```

## Slide 16

01 Introduction

Motivation and Side-Channels “101”

###### 02 Hidden Threat

Novel Side-Channel Source: MCU Bus Interconnect

###### **AGENDA**

03 “Toy” Example Basic Attack Example

04 BUSted Attack

Microarchitectural Side-Channel Attacks on MCUs

05 “Live” Demo

Demo of BUSted Attack

06

Summary

Responsible Disclosure and BH Sound Bytes

## Slide 17

###### **Introduction**

**Motivation and Side-Channels “101”**

## Slide 18

Time
ACTION
Sound Heat
Electromagnetic Emanations

## Slide 19

“Stay Cool! Understanding Thermal Attacks on Mobile-based User Authentication” by Abdelrahman and Khamis

## Slide 20

**“RSA Key Extraction via Low-Bandwidth Acoustic Cryptanalysis” by Daniel Genkin**

## Slide 21

**“Lamphone: Passive Sound Recovery from a Desk Lamp's Light Bulb Vibrations” by Ben Nassi**

## Slide 22

## Slide 23

TIMING DIFFERENCES

## Slide 24

Simple Pipeline
Pipeline
Interrupt Cont. Superscalar
Predictors Core Out-of-Order
Prefetchers
L1-I L1-D
Cluster 1 Cluster 2
Core Core Core Core Core Core Core Core
L2 L2 L2 L2 L2 L2 L2 L2
L3 L3
Interconnect
Memory

## Slide 25

###### Microarchitectural Attacks

CPU
Memory

## Slide 26

###### Microarchitectural Attacks

App 1 App 2
CPU
Core Core
L1-D L1-I L1-D L1-I
Memory L2 L2
L3
Memory

## Slide 27

> Text below was recovered by OCR (confidence 90/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
bypass Google Chrome’s protections against
Spectre-style exploits
attack impacts Intel's
P, and server CPUs
```

## Slide 28

###### APUs

Servers

Mobile

PCs

Computing spectrum

###### MCUs

Drones
Wearables

Hardware Wallets

Appliances

## Slide 29

###### APUs

###### MCUs

Drones
Servers Mobile Wearables
PCs Appliances Hardware Wallets
Computing
spectrum

> Text below was recovered by OCR (confidence 89/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Microcontroller unit (MCU) shipments forecast worldwide from 2021 to
2027 (in millions) |; a |
Drones Wearables
Appliances Hardware Wallets
€
2
G
2027*
Spectrum
```

## Slide 30

###### APUs

###### **Sh** **ipm ents 2022 – 29 billions**

###### MCUs

Drones
Servers Mobile Wearables
PCs Appliances Hardware Wallets
Computing
spectrum

## Slide 31

> Text below was recovered by OCR (confidence 95/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Source
Int.
BUS
BP
Cache
MCUs (Low-End)
Int.
BUS
OoO
BP
Cache No 1:1 correlation between attacks and dots (Ilustrative Graph)
1996 1998 2000 2002 2004 2006 2008 2010 2012 2014 2016 2018 2020 2022 Today
```

## Slide 32

> Text below was recovered by OCR (confidence 95/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Source
Int.
BUS
BP
Cache
MCUs (Low-End)
Nemesis
Int. O
BUS
OoO
BP
Cache No 1:1 correlation between attacks and dots (Ilustrative Graph)
1996 1998 2000 2002 2004 2006 2008 2010 2012 2014 2016 2018 2020 2022 Today
```

## Slide 33

Intel Skylake Microarchitecture Arm Cortex-M33 Microarchitecture

## Slide 34

[1]

###### Arm Cortex-M33 Microarchitecture

[1] - Meltdown: Reading Kernel Memory from User Space

## Slide 35

Arm Cortex-M33 Microarchitecture 2
[2]
[1]

[1] - Meltdown: Reading Kernel Memory from User Space

[2] - Arm Cortex-M33 Processor Datasheet

> Text below was recovered by OCR (confidence 79/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
ITLB
LI Instruction Cache [ me J
Branch Instruction Fetch & PreDecode
‘| Predictor
oO Instruction Queue
& HOP Cache y 1* Stage - Fetch at
ri and Pre-decode
Allocation Queue
2s Reorder buffer
A Scheduler Pre-decode
3 5} SF] 4 optimization Read/write ports
Execution Units
3 s L1 Data Cache
B L2 Cache a
]
=
[1] - Meltdown: Reading Kernel Memory from User Space
[2] - Arm Cortex-M33 Processor Datasheet
```

## Slide 36

L1-I
[1]

•  L1-I

[1] - Meltdown: Reading Kernel Memory from User Space [2] - Arm Cortex-M33 Processor Datasheet

> Text below was recovered by OCR (confidence 80/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
ITLB
LI Instruction Cache je fy
Branch Instruction Fetch & PreDecode
oO Instruction Queue
2 HOP Cache Micgy Beeite 1* Stage - Fetch
Allocation Queue
CDB Reorder buffer
is Scheduler Pre-decode
3 é =| |3 2 g Instruction fetch rate
9 5 S| |3) |a optimization Read/write ports
Z
5 Bs LI Data Cache nn
2 a L2 Cache i
[1]
[1] - Meltdown: Reading Kernel Memory from User Space
[2] - Arm Cortex-M33 Processor Datasheet
```

## Slide 37

L1-I
 L1-D
[1]

•  L1-I
•  L1-D

[1] - Meltdown: Reading Kernel Memory from User Space [2] - Arm Cortex-M33 Processor Datasheet

> Text below was recovered by OCR (confidence 78/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
ITLB
LI Instruction Cache je fy
Branch Instruction Fetch & PreDecode
oO Instruction Queue
E HOP Cache Micgy Beeite 1* Stage - Fetch
Allocation Queue
ce Reorder buffer
o
s Scheduler Pre-decode
=| é = S| |e g Instruction fetch rate
9 5 S| |3) |a optimization Read/write ports
a
a DTLB STLB 4
5 Bs LI Data Cache pr
2 a L2 Cache al
[1]
[1] - Meltdown: Reading Kernel Memory from User Space
[2] - Arm Cortex-M33 Processor Datasheet
```

## Slide 38

L1-I
 L1-D
 L2
[1]

•  L1-I
•  L1-D
•  L2

[1] - Meltdown: Reading Kernel Memory from User Space

[2] - Arm Cortex-M33 Processor Datasheet

> Text below was recovered by OCR (confidence 82/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
ITLB
LI Instruction Cache je fy
—
Branch Instruction Fetch & PreDecode
oO Instruction Queue
=
iS OP Cache 4-Way Decode
MUX
Allocation Queue
oP nor nor — | wor
ce Reorder buffer
HOP HOP HOP HOP HOP HOP HOP HOP
& Scheduler
= Memory
Subsystem
LI Data Cache
STLB ai
L2 Cache 5
[1] - Meltdown: Reading Kernel Memory from User Space
[2] - Arm Cortex-M33 Processor Datasheet
1* Stage - Fetch
and Pre-decode
Fetch and
Pre-decode
Instruction fetch rate
optimization
Read/write ports
```

## Slide 39

L1-I
 L1-D
 L2
 TLBs
[1]

•  L1-I
•  L1-D
•  L2
•  TLBs

[1] - Meltdown: Reading Kernel Memory from User Space

[2] - Arm Cortex-M33 Processor Datasheet

## Slide 40

L1-I
 L1-D
 L2
 TLBs
 BP
[1]

•  L1-I
•  L1-D
•  L2
•  TLBs
•  BP

[1] - Meltdown: Reading Kernel Memory from User Space

[2] - Arm Cortex-M33 Processor Datasheet

## Slide 41

L1-I
 L1-D
 L2
 TLBs
 BP
 OoO
[1]

•  L1-I
•  L1-D
•  L2
•  TLBs
•  BP
•  OoO

[1] - Meltdown: Reading Kernel Memory from User Space

[2] - Arm Cortex-M33 Processor Datasheet

## Slide 42

L1-I
 L1-D
 L2
 TLBs
 BP
 OoO
[1]

•  L1-I
•  L1-D
•  L2
•  TLBs
•  BP
•  OoO

[1] - Meltdown: Reading Kernel Memory from User Space

[2] - Arm Cortex-M33 Processor Datasheet

## Slide 43

L1-I
 L1-D
 L2
 TLBs
 BP
 OoO
[1]

•  L1-I
•  L1-D
•  L2
•  TLBs
•  BP
•  OoO

[1] - Meltdown: Reading Kernel Memory from User Space

[2]

•  Fetch

[2] - Arm Cortex-M33 Processor Datasheet

## Slide 44

L1-I
 L1-D
 L2
 TLBs
 BP
 OoO
[1]

•  L1-I
•  L1-D
•  L2
•  TLBs
•  BP
•  OoO

[1] - Meltdown: Reading Kernel Memory from User Space

[2]

•  Fetch
•  Decode

[2] - Arm Cortex-M33 Processor Datasheet

## Slide 45

L1-I
 L1-D
 L2
 TLBs
 BP
 OoO
[1]

•  L1-I
•  L1-D
•  L2
•  TLBs
•  BP
•  OoO

[1] - Meltdown: Reading Kernel Memory from User Space

[2]

•  Fetch
•  Decode
•  Execute

[2] - Arm Cortex-M33 Processor Datasheet

## Slide 46

##### **Microcontrollers**

CPU
DMA
BUS interconnect
M P

## Slide 47

###### **Hidden Threat**

**Novel Side-Channel Source: MCU Bus Interconnect**

## Slide 48

###### MCU Bus Interconnect as a Threat

CPU
DMA
Bus Interconnect
SRAM Flash Peripherals

## Slide 49

###### MCU Bus Interconnect as a Threat

CPU
DMA
Bus Interconnect
SRAM Flash Peripherals

## Slide 50

###### MCU Bus Interconnect as a Threat

CPU
DMA
Bus Interconnect
SRAM Flash Peripherals

## Slide 51

###### MCU Bus Interconnect as a Threat

CPU
DMA
B us Interconnect
SRAM Flash Peripherals

## Slide 52

###### MCU Bus Interconnect as a Threat

CPU
DMA
Bus Interconnect
SRAM Flash Peripherals

## Slide 53

###### MCU Bus Interconnect as a Threat

CPU
DMA
Bus Interconnect
SRAM Flash Peripherals

## Slide 54

###### MCU Bus Interconnect as a Threat

CPU
DMA
Bus Interconnect
SRAM Flash Peripherals

## Slide 55

###### MCU Bus Interconnect as a Threat

CPU
DMA
Bus Interconnect
SRAM Flash Peripherals

## Slide 56

###### MCU Bus Interconnect as a Threat

CPU
DMA
Bus Interconnect
SRAM Flash Peripherals

## Slide 57

**STM32L073 (M0+)**

**STM32L412 (M4)**

###### **STM32L552 (M33)**

**STM32L767 (M7)**

## Slide 58

**STM32L412 (M4)**

###### **STM32L552 (M33)**

**STM32L767 (M7)**

## Slide 59

**STM32L412 (M4) STM32L767 (M7)**

> Text below was recovered by OCR (confidence 93/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
- 1.0
80727
76687 ~ 0.8
71868 os
65910
0.4
59954
0.2
53996
50755 + 0.0
0 20 40 60 80 100 120 140 160 180 200 220 240
STM32L412 (M4)
57363
57163
56963
56763
56563
56363
- 1.0
- 0.8
0.4
0.2
0.0
0 20 40 60 80 100 120 140 160 180 200 220 240
STM32L767 (M7)
```

## Slide 60

**STM32L767 (M7)**

> Text below was recovered by OCR (confidence 92/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
0 20 40 60 80 100 120 140 160 180 200 220 240 ‘ 0 20 40 60 80 100 120 140 160 180 200 220 240
STM32L767 (M7)
0 20 40 60 80 100 120 140 160 180 200 220 240
```

## Slide 61

> Text below was recovered by OCR (confidence 93/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
80727
76687
71868
65910
59954
53996
50755
58385
55345
52305
49265
46225
43185
40201
20 40 60 80 100 120 140 160 180 200 220 240
20 40 60 80 100 120 140 160 180 200 220 240
- 1.0
57363
57163 ~ 0.8
56963 06
56763
0.4
56563
0.2
56363
56163 + 0.0
0 20 40 60 80 100 120 140 160 180 200 220 240
188269
164109 - 0.8
139949 0.6
115789
0.4
91629
0.2
66304
42432 0.0
0 20 40 60 80 100 120 140 160 180 200 220 240
```

## Slide 62

###### MCU Channels

STM32L552 (M33)

###### STM32L073 (M0+)

STM32L767 (M7)

###### STM32L412 (M4)

###### APU Channels

Skylake TLB Channel

1
Arm Cortex-A9 L1-I Channel

2

[1,2] – “Your Processor Leaks Information – and There’s Nothing You Can Do About It”, Ge et al.

## Slide 63

**“Toy” Attack**

**Basic Attack Example**

## Slide 64

Attack Overview – The Basics

> Text below was recovered by OCR (confidence 91/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Attack Overview — The Basics
CPU
DMA X
-
-
```

## Slide 65

Attack Overview – The Basics

> Text below was recovered by OCR (confidence 91/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Attack Overview — The Basics
CPU
DMA X
-
-
```

## Slide 66

Attack Overview – The Basics

> Text below was recovered by OCR (confidence 91/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Attack Overview — The Basics
CPU
DMA X
-
-
```

## Slide 67

Attack Overview – The Basics

> Text below was recovered by OCR (confidence 87/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Attack Overview — The Basics
CPU
Spy ; Victim
‘Memory
M
DMA 8 y SPY
```

## Slide 68

Attack Overview – The Basics

> Text below was recovered by OCR (confidence 85/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Attack Overview — The Basics
CPU
Spy ; Victim
‘Memory
M
DMA 8 y SPY
-
-
```

## Slide 69

Attack Overview – The Basics

> Text below was recovered by OCR (confidence 81/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Attack Overview — The Basics
CPU
‘Memory CPU
M ,
DMA 8 SPY i
```

## Slide 70

Attack Overview – The Basics

> Text below was recovered by OCR (confidence 90/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Attack Overview — The Basics
CPU
DMA x SPY ;
-
-
```

## Slide 71

Attack Overview – The Basics

> Text below was recovered by OCR (confidence 89/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Attack Overview — The Basics
CPU
DMA X SPY ;
-
-
```

## Slide 72

Attack Overview – The Basics

> Text below was recovered by OCR (confidence 93/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Attack Overview — The Basics
CPU
-
-
```

## Slide 73

Attack Overview – The Basics

> Text below was recovered by OCR (confidence 93/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Attack Overview — The Basics
CPU
-
-
```

## Slide 74

Attack Overview – The Basics

> Text below was recovered by OCR (confidence 86/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Attack Overview — The Basics
CPU
DMA —> SPY
-
-
```

## Slide 75

Attack Overview – The Basics

> Text below was recovered by OCR (confidence 85/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Attack Overview — The Basics
CPU
Spy ——+}> Victim
-
-
DMA —> SPY
```

## Slide 76

Attack Overview – The Basics

> Text below was recovered by OCR (confidence 90/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Attack Overview — The Basics
CPU
Spy ——+}> Victim
-
-
```

## Slide 77

Attack Overview – The Basics

> Text below was recovered by OCR (confidence 92/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Attack Overview — The Basics
CPU
Spy —> Victim
-
-
```

## Slide 78

Attack Overview – Toy Example

## Slide 79

Attack Overview – Toy Example

## Slide 80

Attack Overview – Toy Example

> Text below was recovered by OCR (confidence 81/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Attack Overview — Toy Example
var=1
Firmware . ; else
~ 1 var=0;
Mem I
M
```

## Slide 81

Attack Overview – Toy Example

If-else statement compiled for Arm Cortex-M33 (-O0)

> Text below was recovered by OCR (confidence 70/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Attack Overview — Toy Example
!
Spy | Vietim | | if(s==1) Lo 1 IF movs 3, #1 ;
SS ne | var=1; | ; str 3, [r7, #0]
X .
DMA ———> spy If-else statement compiled for Arm Cortex-M33 (-O0)
```

## Slide 82

Attack Overview – Toy Example

If-else statement compiled for Arm Cortex-M33 (-O0)

> Text below was recovered by OCR (confidence 73/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Attack Overview — Toy Example
Spy Victim | \ if ( ==1) Loe 1 IF movs r3, #1 1 clk
Ld nn var=1; | ; str 3, [r7, #2] Lelk !
Firmware yA ; else q ; b.n END 2 clk !
DMA ———> spy If-else statement compiled for Arm Cortex-M33 (-O0)
```

## Slide 83

Attack Overview – Toy Example

If-else statement compiled for Arm Cortex-M33 (-O0)

> Text below was recovered by OCR (confidence 74/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Attack Overview — Toy Example
--77 ! 1 of ! beq.n ELSE 3 clk (else), 1 clk (if) 1
Spy Victim I L? 1 IF movs r3, #1 \
SS ne | var=1; | ; str 3, [r7, #0]
DMA ———> sey, If-else statement compiled for Arm Cortex-M33 (-O0)
```

## Slide 84

Attack Overview – Toy Example

If-else statement compiled for Arm Cortex-M33 (-O0)

> Text below was recovered by OCR (confidence 69/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Attack Overview — Toy Example
I
; --77 ' l -7 ! beq.n ELSE 3 clk (else), 1 clk (if) 1
Spy H Victim I L- 1 IF: movs r3, #1 Iclk ;
Firmware ~s, 1 else b.n END 2elk |
a er str 3, [r7, #0] Lclk |
```

## Slide 85

Attack Overview – Toy Example

> Text below was recovered by OCR (confidence 93/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Attack Overview — Toy Example
IF:
ELSE:
END:
cmp
beq.n
movs
str
b.n
movs
str
nop
r3, #0
ELSE
r3, #1
r3, [r7, #0]
END
r3, #0
r3, [r7, #0]
1 clk
3 clk (else), 1 clk (if)
1 clk
1 clk
2 clk
1 clk
1 clk
1 clk
Clock
If
Trace
Else
Trace
t
t+2
t+3
t+4
t+5
t+6
```

## Slide 86

Attack Overview – Toy Example

> Text below was recovered by OCR (confidence 93/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Attack Overview — Toy Example
IF:
ELSE:
END:
cmp
beq.n
movs
str
b.n
movs
str
nop
r3, #0
ELSE
r3, #1
r3, [r7, #0]
END
r3, #0
r3, [r7, #0]
1 clk
3 clk (else), 1 clk (if)
1 clk
1 clk
2 clk
1 clk
1 clk
1 clk
Clock
If
Trace
Else
Trace
t
cmp
t+2
t+3
t+4
t+5
t+6
```

## Slide 87

Attack Overview – Toy Example

> Text below was recovered by OCR (confidence 93/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Attack Overview — Toy Example
IF:
ELSE:
END:
cmp
beq.n
movs
str
b.n
movs
str
nop
r3, #0
ELSE
r3, #1
r3, [r7, #0]
END
r3, #0
r3, [r7, #0]
1 clk
3 clk (else), 1 clk (if)
1 clk
1 clk
2 clk
1 clk
1 clk
1 clk
Clock
If
Trace
Else
Trace
t
cmp
beq
t+2
t+3
t+4
t+5
t+6
```

## Slide 88

Attack Overview – Toy Example

> Text below was recovered by OCR (confidence 93/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Attack Overview — Toy Example
IF:
ELSE:
END:
cmp
beq.n
movs
str
b.n
movs
str
nop
r3, #0
ELSE
r3, #1
r3, [r7, #0]
END
r3, #0
r3, [r7, #0]
1 clk
3 clk (else), 1 clk (if)
1 clk
1 clk
2 clk
1 clk
1 clk
1 clk
Clock
If
Trace
Else
Trace
t
cmp
beq
t+2
movs
t+3
t+4
t+5
t+6
```

## Slide 89

Attack Overview – Toy Example

> Text below was recovered by OCR (confidence 92/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Attack Overview — Toy Example
Spy Victim
Firmware
Memory
IF:
ELSE:
END:
cmp
beq.n
movs
str
b.n
movs
str
nop
r3, #0
ELSE
r3, #1
r3, [r7, #0]
END
r3, #0
r3, [r7, #0]
1 clk
3 clk (else), 1 clk (if)
1 clk
1 clk
2 clk
1 clk
1 clk
1 clk
Clock
If
Trace
Else
Trace
t
emp | beq | movs
t+2
t+3
str
t+4
t+5
t+6
```

## Slide 90

Attack Overview – Toy Example

> Text below was recovered by OCR (confidence 92/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Attack Overview — Toy Example
IF:
ELSE:
END:
cmp
beq.n
movs
str
b.n
movs
str
nop
r3, #0
ELSE
r3, #1
r3, [r7, #0]
END
r3, #0
r3, [r7, #0]
1 clk
3 clk (else), 1 clk (if)
1 clk
1 clk
2 clk
1 clk
1 clk
1 clk
Clock: t ttl
If emp | beg
Else
Trace
t+2
movs
t+3
str
t+4
b
t+5
t+6
```

## Slide 91

Attack Overview – Toy Example

> Text below was recovered by OCR (confidence 78/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Attack Overview — Toy Example
CPU
y | ie beq.n ELSE 3 clk (else), 1 clk (if) ; , ,
str r3, [r7, #0] 1 clk race
Memory b.n END elk
My ELSE: movs r3, #0 1 clk Else
```

## Slide 92

Attack Overview – Toy Example

> Text below was recovered by OCR (confidence 92/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Attack Overview — Toy Example
IF:
ELSE:
END:
cmp
beq.n
movs
str
b.n
movs
str
nop
r3, #0
ELSE
r3, #1
r3, [r7, #0]
END
r3, #0
r3, [r7, #0]
1 clk
3 clk (else), 1 clk (if)
1 clk
1 clk
2 clk
1 clk
1 clk
1 clk
Clock: t ttl
If emp | beg
Else
Trace
t+2
movs
t+3
str
```

## Slide 93

Attack Overview – Toy Example

> Text below was recovered by OCR (confidence 85/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Attack Overview — Toy Example
CPU
PY : scene beq.n ELSE 3 clk (else), 1 clk (if)
Firmware IF: movs r3, #1 1 clk
str r3, [r7, #0] 1 clk
Memory b.n END elk
str r3, [r7, c
X
```

## Slide 94

Attack Overview – Toy Example

> Text below was recovered by OCR (confidence 81/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Attack Overview — Toy Example
CPU
PY : scene beq.n ELSE 3 clk (else), 1 clk (if)
Firmware IF: movs r3, #1 1 clk
str r3, [r7, #0] 1 clk
Memory b.n END elk
M ELSE: movs — — - ok Else ‘cmp
str r3, [r7, # C
```

## Slide 95

Attack Overview – Toy Example

> Text below was recovered by OCR (confidence 81/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Attack Overview — Toy Example
CPU
PY : scene beq.n ELSE 3 clk (else), 1 clk (if)
Firmware IF: movs r3, #1 1 clk
str r3, [r7, #0] 1 clk
Memory b.n END elk
M ELSE: movs — — - ok Else ‘cmp
str r3, [r7, # C
```

## Slide 96

Attack Overview – Toy Example

> Text below was recovered by OCR (confidence 92/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
CPU
Spy ‘| Victim
Memory
xcs
ISPY|
IF:
ELSE:
END:
cmp
beq.n
movs
str
b.n
movs
str
nop
r3, #0
ELSE
r3, #1
r3, [r7, #0]
END
r3, #0
r3, [r7, #0]
1 clk
3 clk (else), 1 clk (if)
1 clk
1 clk
2 clk
1 clk
1 clk
1 clk
Clock
If
Trace
Else
Trace
cmp
cmp
beq
beq
Attack Overview — Toy Example
```

## Slide 97

Attack Overview – Toy Example

> Text below was recovered by OCR (confidence 83/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Attack Overview — Toy Example
CPU
PY : scene beq.n ELSE 3 clk (else), 1 clk (if)
Fi IF: movs r3, #1 1 clk
str r3, [r7, #0] 1 clk race
emer b.n END 2 clk
M ELSE: movs r3, #0 ok Else ‘cmp: beq | beq
— str r3, [r7, #0] c
```

## Slide 98

Attack Overview – Toy Example

> Text below was recovered by OCR (confidence 81/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Attack Overview — Toy Example
CPU
Py ‘ a beq.n ELSE 3 clk (else), 1 clk (if)
Fi IF: movs r3, #1 1 clk
irmware TT — = --- ».¢
str r3, [r7, #0] 1 clk race
o b.n END 2 clk
```

## Slide 99

Attack Overview – Toy Example

> Text below was recovered by OCR (confidence 92/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
CPU
Spy ‘| Victim
Memory
xcs
ISPY|
IF:
ELSE:
END:
cmp
beq.n
movs
str
b.n
movs
str
nop
r3, #0
ELSE
r3, #1
r3, [r7, #0]
END
r3, #0
r3, [r7, #0]
1 clk
3 clk (else), 1 clk (if)
1 clk
1 clk
2 clk
1 clk
1 clk
1 clk
Clock
If
Trace
Else
Trace
cmp
cmp
beq
beq
t+2
movs
Attack Overview — Toy Example
t+3
```

## Slide 100

Attack Overview – Toy Example

> Text below was recovered by OCR (confidence 84/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Attack Overview — Toy Example
CPU
a tetim beq.n ELSE 3 clk (else), 1 clk (if)
Fi IF: movs r3, #1 1 clk
str r3, [r7, #0] 1 clk
emer b.n END 2 clk
nv str r3, [r7, #0 ©
```

## Slide 101

Attack Overview – Toy Example

> Text below was recovered by OCR (confidence 92/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
CPU
Spy ‘| Victim
Memory
xcs
ISPY|
IF:
ELSE:
END:
cmp
beq.n
movs
str
b.n
movs
str
nop
r3, #0
ELSE
r3, #1
r3, [r7, #0]
END
r3, #0
r3, [r7, #0]
1 clk
3 clk (else), 1 clk (if)
1 clk
1 clk
2 clk
1 clk
1 clk
1 clk
Clock
If
Trace
Else
Trace
cmp
cmp
beq
beq
t+2
movs
beq
Attack Overview — Toy Example
t+3
str
beq
t+4
t+5
str
```

## Slide 102

Attack Overview – Toy Example

> Text below was recovered by OCR (confidence 91/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
CPU
Spy ‘| Victim
Memory
xcs
ISPY
IF:
ELSE:
END:
cmp
beq.n
movs
str
b.n
movs
str
nop
r3, #0
ELSE
r3, #1
r3, [r7, #0]
END
r3, #0
r3, [r7, #0]
1 clk
3 clk (else), 1 clk (if)
1 clk
1 clk
2 clk
1 clk
1 clk
1 clk
Clock
If
Trace
Else
Trace
cmp
cmp
beq | movs
Ae beq
Attack Overview — Toy Example
t+3
str
xX
beq
t+4
t+5
str
```

## Slide 103

Attack Overview – Toy Example

> Text below was recovered by OCR (confidence 90/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Spy ‘| -‘Victim
ISPY
IF:
ELSE:
END:
cmp
beq.n
movs
str
b.n
movs
str
nop
r3, #0
ELSE
r3, #1
r3, [r7, #0]
END
r3, #0
r3, [r7, #0]
1 clk
3 clk (else), 1 clk (if)
1 clk
1 clk
2 clk
1 clk
1 clk
1 clk
Clock
If
Trace
Else
Trace
ttl t+2
béq | movs
Ae beq
Attack Overview — Toy Example
<0
t+3
str
beq
t+4
t+5
str
```

## Slide 104

Attack Overview – Toy Example

> Text below was recovered by OCR (confidence 83/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Attack Overview — Toy Example
<0
ISPY
IF:
ELSE:
END:
cmp r3, #0 1 clk
beq.n ELSE 3 clk (else), 1 clk (if)
movs r3, #1 1 clk
str n2 [nZ HAT 1 elk
ber q 2 clk
if(s==1)
mo\ 1 clk
sti var=1 ’ 1 clk
Clock
If
Trace
Else
Trace
ttl t+2
béq | movs
Ae beq
t+3
str
beq
t+4
t+5
str
```

## Slide 105

Attack Overview – Toy Example

SECRET = 1

> Text below was recovered by OCR (confidence 72/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Attack Overview — Toy Example
<0
Vieti cmp r3, #0 1 clk Clock: t ttl] | t+2 | tt3 § tt+4 > t45
```

## Slide 106

###### **BUSted**

**Microarchitectural Side-Channel Attacks on MCUs**

## Slide 107

* * *<sup>-</sup>

## Slide 108

-
* * * USER

## Slide 109

-
* * * USER

## Slide 110

USER
* * * -

## Slide 111

* * *<sup>-</sup>

## Slide 112

* * * - Hacker

## Slide 113

* * * - Hacker

## Slide 114

Hacker
* * * -

## Slide 115

* * *<sup>-</sup>

## Slide 116

* * *<sup>-</sup>

## Slide 117

* * * -
Cortex-M

## Slide 118

NON-SECURE WORLD TZ SECURE WORLD
* * * -
Cortex-M

## Slide 119

NON-SECURE WORLD TZ SECURE WORLD
TA Victim
TF-M
* * * -
Cortex-M

## Slide 120

NON-SECURE WORLD TZ SECURE WORLD
TA Victim
SPY
TF-M
* * * -
Cortex-M

## Slide 121

NON-SECURE WORLD TZ SECURE WORLD
TA Victim
SPY
TF-M
* * * -
Cortex-M

## Slide 122

NON-SECURE WORLD TZ SECURE WORLD
TA Victim
SPY
DMA TF-M
* * * -
Cortex-M
PPC
AHB
PPC
MPC MPC PPC
Peripheral 1
Peripheral 1
Peripheral 2
Peripheral 2
Peripheral N FLASH SRAM
Peripheral N

## Slide 123

NON-SECURE WORLD TZ SECURE WORLD
TA Victim
SPY
DMA TF-M
* * * -
Cortex-M
PPC
AHB
PPC
MPC MPC PPC
Peripheral 1
Peripheral 1
Peripheral 2
Peripheral 2
Peripheral N FLASH SRAM
Peripheral N

## Slide 124

NON-SECURE WORLD TZ SECURE WORLD
TA Victim
SPY
DMA TF-M
* * * -
Cortex-M
PPC
AHB
PPC
MPC MPC PPC
Peripheral 1 SPY SPY
Peripheral 1
CODE DATA
Peripheral 2 Victim Victim Peripheral 2
CODE DATA
Peripheral N FLASH SRAM
Peripheral N

## Slide 125

## Slide 126

###### Challenges

Spy Victim
CPU
M
U
DMA X

Spy Victim
CPU
M
U
DMA X

Spy Victim
CPU
M
U
DMA X

## Slide 127

###### Challenges

Spy

Spy Victim
CPU
M
U
DMA X

Spy Victim
CPU
M
U
DMA X

Spy Victim
CPU
M
U
DMA X

## Slide 128

###### Challenges

Victim

Spy

Spy Victim Spy Victim
CPU CPU
M M
U U
DMA X DMA X

Spy Victim
CPU
M
U
DMA X

## Slide 129

###### Challenges

Victim

Spy

Spy Victim Spy Victim
CPU CPU
M M
U U
DMA X DMA X

Spy

Spy Victim
CPU
M
U
DMA X

## Slide 130

###### Challenges

Spy

Spy Victim
CPU
M
U
DMA X

Spy

Victim

Spy Victim
CPU
M
U
DMA X

Spy Victim
CPU
M
U
DMA X

No Difference

## Slide 131

###### Challenges

Spy Victim
Spy Victim Spy Victim
CPU CPU
M M
U U
DMA X DMA X

###### No Difference

Spy
Spy Victim
CPU
M
U
DMA X

## Slide 132

###### Challenges

Spy Victim
C1 -  The bus is a stateless component;
Spy Victim Spy Victim
CPU CPU
M M
U U
DMA X DMA X
No Difference

Spy

Spy Victim
CPU
M
U
DMA X

## Slide 133

###### Challenges

Spy Victim
CPU
M
U
DMA X

Spy Victim
CPU
M
U
DMA X

Spy Victim
CPU
M
U
DMA X

## Slide 134

###### Challenges

Spy Victim Spy Victim
CPU 1 CPU 2 CPU 1 CPU 2
M M
U U
DMA X DMA X

Spy Victim
CPU 1 CPU 2
M
U
DMA X

Dual-Core, Spy Always Executing

## Slide 135

###### Challenges

Spy Victim
CPU 1 CPU 2
M
U
DMA X

Spy Victim
CPU 1 CPU 2
M
U
DMA X

Spy Victim
CPU 1 CPU 2
M
U
DMA X

###### Always Spying

## Slide 136

###### Challenges

Spy Victim Spy Victim
CPU 1 CPU 2 CPU 1 CPU 2
M M
U U
DMA X DMA X

Spy Victim
CPU 1 CPU 2
M
U
DMA X

## Slide 137

###### Challenges

Spy Victim Spy Victim
CPU 1 CPU 2 CPU 1 CPU 2
M M
U U
DMA X DMA X

Spy Victim
CPU 1 CPU 2
M
U
DMA X

## Slide 138

###### Challenges

Spy Victim Spy Victim
CPU 1 CPU 2 CPU 1 CPU 2
M M
U U
DMA X DMA X

Spy Victim
CPU 1 CPU 2
M
U
DMA X

## Slide 139

###### Challenges

Spy Victim
CPU 1 CPU 2
M
U
DMA X

Spy Victim
CPU 1 CPU 2
M
U
DMA X

Spy Victim
CPU 1 CPU 2
M
U
DMA X

## Slide 140

###### Challenges

Spy Victim
CPU 1 CPU 2
M
U
DMA X

Spy Victim
CPU 1 CPU 2
M
U
DMA X

Spy Victim
CPU 1 CPU 2
M
U
DMA X

## Slide 141

###### Challenges

Spy Victim
CPU 1 CPU 2
M
U
DMA X

Spy Victim
CPU 1 CPU 2
M
U
DMA X

###### Different States

Spy Victim
CPU 1 CPU 2
M
U
DMA X

## Slide 142

###### Challenges

Spy Victim Spy Victim
CPU 1 CPU 2 CPU 1 CPU 2
M M
U U
DMA X DMA X

Spy Victim
CPU 1 CPU 2
M
U
DMA X

Single-Core MCU!!!

## Slide 143

###### Challenges

C1 -  The bus is a stateless component;
Spy Victim Spy Victim Spy Victim
CPU 1 CPU 2 CPU 1 CPU 2 CPU 1 CPU 2
M M M
U U U
DMA X DMA X DMA X
Single-Core MCU!!!

###### **C1 -** The bus is a stateless component;

## Slide 144

###### Challenges

###### **C1 -** The bus is a stateless component; **C2 -** No concurrent execution between Spy and Victim (single-core); **Spy Victim Spy Victim Spy Victim**

CPU 1 CPU 2 CPU 1 CPU 2 CPU 1 CPU 2
M M M
U U U
DMA X DMA X DMA X

Single-Core MCU!!!

## Slide 145

###### Challenges

###### **C1 -** The bus is a stateless component; **C2 -** No concurrent execution between Spy and Victim (single-core); **Spy Victim Spy Victim Spy Victim C3 -** Victim execution cannot be interrupted; **CPU 1 CPU 2 CPU 1 CPU 2 CPU 1 CPU 2**

CPU 1 CPU 2 CPU 1 CPU 2 CPU 1 CPU 2
M M M
U U U
DMA X DMA X DMA X
Single-Core MCU!!!

## Slide 146

###### Challenges

**C1 -** The bus is a stateless component; **C2 -** No concurrent execution between Spy and Victim (single-core); **Spy Victim Spy Victim Spy Victim C3 -** Victim execution cannot be interrupted; **CPU 1 CPU 2 CPU 1 CPU 2 CPU 1 CPU 2 C** **4 -** Spy only has one ch anc e to steal the secret.

**CPU 1 CPU 2 CPU 1 CPU 2 CPU 1 CPU 2 -** Spy only has one ch anc e to steal the secret. **M M M U U U DMA** **~~X~~ DMA** **~~X~~ DMA** **~~X~~**

Single-Core MCU!!!

## Slide 147

## Slide 148

###### Solution

Spy Victim Spy Victim
CPU 1 CPU 2 CPU 1 CPU 2
M M
U U
DMA X DMA X

Spy Victim
CPU 1 CPU 2
M
U
DMA X

###### Single-Core MCU!!!

## Slide 149

###### Solution

Victim Victim Victim
CPU CPU CPU
M M M
U U U
DMA X DMA X DMA X

Single-Core MCU!!!

## Slide 150

###### Solution

Victim
?
CPU
M
U
DMA X

Victim
?
CPU
M
U
DMA X

Victim
?
CPU
M
U
DMA X

###### Single-Core MCU!!!

## Slide 151

###### Solution

P P
Victim Victim
CPU CPU
M M
U U
DMA X DMA X

P
Victim
CPU
M
U
DMA X

MCUs Have a lot of Peripherals!!

## Slide 152

###### Solution

P P
Victim Victim
CPU CPU
M M
U U
DMA X DMA X

P
Victim
CPU
M
U
DMA X

###### Group Some Peripherals!!

## Slide 153

###### Solution

P P P
Victim Victim Victim
CPU CPU CPU
M M M
U U U
DMA X DMA X DMA X

###### Interconnect the Peripherals!!

## Slide 154

###### Solution

P P P
Victim Victim Victim
CPU CPU CPU
M M M
U U U
DMA X DMA X DMA X

Voilà!!! Hardware Gadgets!

## Slide 155

###### Solution

Spy
P
Victim
CPU
M
U
DMA X

Spy Spy
P P
Victim Victim
CPU CPU
M M
U U
DMA X DMA X

Always Spying

## Slide 156

###### Solution

Spy
P
Victim
CPU
M
U
DMA X

Spy

Victim
Spy
P
Victim
CPU
M
U
DMA X

Spy
P
Victim
CPU
M
U
DMA X

Always Spying

## Slide 157

###### Solution

Spy
P
Victim
CPU
M
U
DMA X

Spy

Victim

P
Victim
CPU
M
U
DMA X
Always  Spying

Spy
P
Victim
CPU
M
U
DMA X

## Slide 158

###### Solution

Spy
P
Victim
CPU
M
U
DMA X

Spy

Victim
Spy
P
Victim
CPU
M
U
DMA X

Different  States

Spy
P
Victim
CPU
M
U
DMA X

## Slide 159

###### Challenges

Victim Spy Spy Spy **C1 -** The bus is a stateless component; **C2** P **~~-~~** No concurrent execut P ~~ion~~ between Spy and Vi P ~~ct~~ im (single-core); **Victim Victim Victim C** **~~3 -~~** Victim execution can ~~not~~ be interrupted; **CPU CPU CPU C4 -** Spy only has one chance to steal the secret.

**CPU CPU CPU** Spy only has one chance to steal the secret. **M M M U U U DMA** **~~X~~ DMA** **~~X~~ DMA** **~~X~~**

## Slide 160

###### Challenges

Victim Spy Spy Spy **C1 -** The bus is a stateless component; **C2** P **~~-~~** No concurrent execut P ~~ion~~ between Spy and Vi P ~~ct~~ im (single-core); **Victim Victim Victim C** **~~3 -~~** Victim execution can ~~not~~ be interrupted; **CPU CPU CPU C4 -** Spy only has one chance to steal the secret. **M M M U U U DMA** **~~X~~ DMA** **~~X~~ DMA** **~~X~~**

## Slide 161

###### Hardware Gadgets

###### Spy

P
Victim
CPU
M
U
DMA X

## Slide 162

###### Hardware Gadgets

Spy
P
Victim
CPU
M
U
DMA X

## Slide 163

Hardware Gadgets

## Slide 164

Hardware Gadgets

> Text below was recovered by OCR (confidence 95/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Hardware Gadgets
DMA CPU
Bus Matrix
TIMER SRAM 1 SRAM 2
Write Timer
```

## Slide 165

###### Hardware Gadgets

Contention
Threshold

> Text below was recovered by OCR (confidence 93/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Hardware Gadgets
Bus Matrix
TIMER SRAM 1 SRAM 2
Read SRAM 2 |
Timer
Contention
Threshold
```

## Slide 166

###### Hardware Gadgets

Contention
Threshold

> Text below was recovered by OCR (confidence 87/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Hardware Gadgets
Contention
Threshold
J SRAM 2
Write Timer
Trigger =) DMA
```

## Slide 167

###### Hardware Gadgets

Normal Operation

Contention
Threshold

## Slide 168

###### Hardware Gadgets

Normal Operation

## Slide 169

###### Hardware Gadgets

Normal Operation

> Text below was recovered by OCR (confidence 87/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Hardware Gadgets
Normal Operation
Read SRAM 2
Trigger =) DMA
Write Timer
```

## Slide 170

###### Hardware Gadgets

Normal Operation

Transfer
Latency

> Text below was recovered by OCR (confidence 90/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Hardware Gadgets
Normal Operation
SRAM 2
Trigger =) DMA
Transfer
Latency
Write Timer
```

## Slide 171

Hardware Gadgets

> Text below was recovered by OCR (confidence 86/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Hardware Gadgets
J SRAM 2
Write Timer
Trigger =) DMA
```

## Slide 172

Hardware Gadgets

## Slide 173

###### Hardware Gadgets

###### CONTENTION!!

> Text below was recovered by OCR (confidence 84/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Hardware Gadgets
CONTENTION!!
Trigger =) DMA
Write Timer
```

## Slide 174

###### Hardware Gadgets

###### CONTENTION!!

> Text below was recovered by OCR (confidence 82/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Hardware Gadgets
CONTENTION!!
Read SRAM 2
Trigger =>) DMA
Write Timer
```

## Slide 175

###### Hardware Gadgets

###### CONTENTION!!

Transfer
Latency

> Text below was recovered by OCR (confidence 84/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Hardware Gadgets
CONTENTION!!
Read SRAM 2
Trigger =>) DMA
Write Timer Tra n sfe r
Latency
```

## Slide 176

###### Hardware Gadgets

###### CONTENTION!!

Transfer
Latency

> Text below was recovered by OCR (confidence 88/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Hardware Gadgets
CONTENTION!!
Read SRAM 2
Write Timer Tra n sfe r
Latency
```

## Slide 177

###### Hardware Gadgets

###### CONTENTION!!

Interrupt
(Detection)

## Slide 178

###### BUSted Attack

NON-SECURE WORLD TZ SECURE WORLD
TA Victim
SPY
TF-M
Cortex-M

## Slide 179

###### BUSted Attack

NON-SECURE WORLD TZ SECURE WORLD
TA Victim
SPY
TF-M
Cortex-M

Code based in Sancus and Texas Reference Implementation of a Keypad [1,2]

> [1] <u>https://github.com/sancus-tee/vulcan/blob/master/demo/ecu-tcs/sm_tcs_kypd.c</u>

> [2] Implementing An Ultra-Low-Power Keypad Interface With MSP430™MCUs

## Slide 180

###### BUSted Attack

NON-SECURE WORLD TZ SECURE WORLD
TA Victim
SPY
TF-M
Cortex-M

Code based in Sancus and Texas Reference Implementation of a Keypad [1,2]

> [1] <u>https://github.com/sancus-tee/vulcan/blob/master/demo/ecu-tcs/sm_tcs_kypd.c</u>

> [2] Implementing An Ultra-Low-Power Keypad Interface With MSP430™MCUs

## Slide 181

BUSted Profiling

> Text below was recovered by OCR (confidence 82/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
3USted Profiling
while clock != END do 1:2:3:4:5:6:7:8:9 :10:11:12:13:14:15
16:17
Start_Trace(clock++); If bi pin[x++] =i
veitim();
End_Trace();
While = Read_Key= For
Else ™ dummy|[x++] =i
he Trigger Cont. 0 Record Cont.
Gadget ? Gadget
v
SRAM
VIC
SPY
```

## Slide 182

BUSted Profiling

> Text below was recovered by OCR (confidence 88/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
3USted Profiling
while clock != END do
1
Start_Trace(clock++);
veitim();
End_Trace();
he Trigger Cont. oe
Gadget
If (Key Pressed) ie
Else (Key !Pressed)
Record Cont.
Gadget
SRAM
VIC
SPY
```

## Slide 183

BUSted Profiling

> Text below was recovered by OCR (confidence 82/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
53USted Profiling
while clock != END do 1:2
Start_Trace(clock++);
veitim(); While
End_Trace();
ke SRAM
Trigger Cont. fc) Record Cont. vic
Gadget > Gadget
bd SPY
If (Key Pressed) eB
Else (Key !Pressed)
```

## Slide 184

BUSted Profiling

> Text below was recovered by OCR (confidence 88/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
3USted Profiling
while clock != END do
Start_Trace(clock++);
veitim();
he Trigger Cont. oe Record Cont.
Gadget
If (Key Pressed) Be
Else (Key !Pressed)
Gadget
SRAM
VIC
SPY
```

## Slide 185

BUSted Profiling

> Text below was recovered by OCR (confidence 88/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
3USted Profiling
while clock != END do
Start_Trace(clock++);
veitim();
]
Trigger Cont. ° Record Cont.
Gadget Gadget
If (Key Pressed) Be 4
v
Else (Key !Pressed)
SRAM
VIC
SPY
```

## Slide 186

BUSted Profiling

> Text below was recovered by OCR (confidence 79/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
3USted Profiling
while clock != END do 1:2:3:;4:5:6:7:8
Start_Trace(clock++);
veitim(); While = Read_Key = For
end 4
7) I SRAM
Trigger Cont. ° Record Cont. VIC
Gadget Gadget
vV SPY
If (Key Pressed) Be 4|5 i 7|8
Else (Key !Pressed)
```

## Slide 187

BUSted Profiling

> Text below was recovered by OCR (confidence 81/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
3USted Profiling
while clock != END do 162:3:4:5:6 7:8
Start_Trace(clock++);
veitim(); While = Read_Key = For
end 4
7) I SRAM
Trigger Cont. ° Record Cont. VIC
Gadget Gadget
vV SPY
Else (Key !Pressed)
```

## Slide 188

BUSted Profiling

> Text below was recovered by OCR (confidence 84/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
3USted Profiling
while clock != END do 1:2:3:4:5:6:7:8
Start_Trace(clock++);
veitim(); While = Read_Key = For
end |
Trigger Cont. ° Record Cont. VIC
Gadget Gadget
Vv SPY
Else (Key !Pressed)
```

## Slide 189

BUSted Profiling

> Text below was recovered by OCR (confidence 85/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
3USted Profiling
while clock != END do 1:2:3:4:5:6:7:8
Start_Trace(clock++);
veitim(); While = Read_Key = For
end
Trigger Cont. ° Record Cont. VIC
Gadget Gadget
Vv SPY
Else (Key !Pressed)
```

## Slide 190

BUSted Profiling

> Text below was recovered by OCR (confidence 82/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
3USted Profiling
while clock != END do 1:2:3:4:5:6:7:8:9 :10:11:12:13:14:15:16:17
Start_Trace(clock++); If Hf pin[x++] =i
veitim(); While = Read_Key = For
Ise = dummy[x++] =i
SRAM
Trigger Cont. f Record Cont. VIC
Gadget Gadget
v SPY
```

## Slide 191

###### BUSted Profiling

Monitor Clock Cycle 14

> Text below was recovered by OCR (confidence 81/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
3USted Profiling
Start_Trace(clock++); If Hf pin[x++] =i
While = Read_Key = For
Ise = dummy[x++] =i
a ] SRAM
Trigger Cont. <] Record Cont.
—> VIC
Gadget Gadget
SPY
v
Monitor Clock Cycle 14
```

## Slide 192

BUSted Exploitation

> Text below was recovered by OCR (confidence 80/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
3USted Exploitation
begin
Start_Exploit(clock);
End_Exploit();
SRAM
Trigger Cont. 3 Detect Cont.
—P Gadget 4 Gadget
Counter © Auto-Sync Read Secret
Gadget Gadget Gadget
a 7) | Syne a 5} = Read
VIC
SPY
```

## Slide 193

BUSted Exploitation

> Text below was recovered by OCR (confidence 85/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
3USted Exploitation
begin
Start_Exploit(clock);
End_Exploit();
Firmware
Trigger Cont. © Detect Cont.
Counter © Auto-Sync Read Secret
Gadget Gadget Gadget
A | Syne . 2 Read
SRAM
VIC
SPY
```

## Slide 194

BUSted Exploitation

> Text below was recovered by OCR (confidence 85/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
3USted Exploitation
begin
Start_Exploit(clock);
End_Exploit();
Firmware
Trigger Cont. © Detect Cont.
Counter © Auto-Sync Read Secret
Gadget Gadget Gadget
A | Syne . 2 Read
SRAM
VIC
SPY
```

## Slide 195

BUSted Exploitation

> Text below was recovered by OCR (confidence 85/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
3USted Exploitation
begin
Start_Exploit(clock);
End_Exploit();
Firmware
Trigger Cont. © Detect Cont.
Counter © Auto-Sync Read Secret
Gadget Gadget Gadget
A | Syne . 2 Read
SRAM
VIC
SPY
```

## Slide 196

BUSted Exploitation

> Text below was recovered by OCR (confidence 79/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
3USted Exploitation
If 4 pin|x++]:
While = Read Key = For {' °
Else = dummy[x+-
begin
Start_Exploit(clock);
End_Exploit();
end
Trigger Cont. 3] Detect Cont.
P| Gadget > Gadget vIC
Counter © Auto-Sync Read Secret SPY
Gadget Gadget Gadget
A | Syne . 2 Read
```

## Slide 197

###### BUSted Exploitation

SECRET = 7

> Text below was recovered by OCR (confidence 82/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
3USted Exploitation
begin
end
Start_Exploit(clock);
End_Exploit();
If 4 pin|x++]:
While = Read Key = For {' °
Else = dummy[x+-
Counter
Gadget
.
unter
SRAM
SPY
SECRET = 7
```

## Slide 198

###### **“Live” Demo**

**Demo of BUSted Attack**

## Slide 199

###### Under the hood

NON-SECURE WORLD TZ SECURE WORLD
TA Victim
SPY
TF-M
Cortex-M

###### “Live” Demo

## Slide 200

###### **Summary**

**Responsible Disclosure, and Black Hat Sound Bytes**

## Slide 201

We have introduced the concept of **hardware gadgets** and presented **BUSted,** the **1**<sup>**st**</sup> **microarchitectural side-channel attack** exploiting **TrustZone-M** devices.

## Slide 202

Responsible Disclosure

## Slide 203

Responsible Disclosure

## Slide 204

###### Responsible Disclosure

TF-M
Application

## Slide 205

###### BH Sound Bytes

1. We **debunked** the common belief **that MCUs are not vulnerable** to **microarchitectural side-channel attacks** .

2. We presented **a new class** of software-based **microarchitectural side-channel attacks** affecting **MCUs**

3. We provided a **reference attack** that **bypasses** the TEE ( **TrustZone-M** ) of modern Armv8-M MCUs (Cortex-M33), **breaking all memory isolations!!**

## Slide 206

## THANK YOU!

Cristiano Rodrigues  | Sandro Pinto, PhD (Centro ALGORITMI / LASI, Universidade do Minho)

###### **id9492@alunos.uminho.pt**

**LinkedIn** - https://www.linkedin.com/in/cristiano-rodrigues-msc-engineer/ **ResearchGate** - https://www.researchgate.net/profile/Cristiano-Rodrigues-10 **Github** - https://github.com/ESCristiano

###### **sandro.pinto@dei.uminho.pt**

**LinkedIn** - https://www.linkedin.com/in/sandro-pinto-phd-40535455/ **ResearchGate** - https://www.researchgate.net/profile/Sandro_Pinto2 **Github** - https://github.com/sandro2pinto/

## Slide 207

**Q&A**
