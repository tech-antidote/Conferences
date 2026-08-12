---
title: "Tiny Chips, Big Leaks Breaking TrustZone-M with Single-Stepping Attacks"
speakers: ["Cristiano Rodrigues", "Sandro Pinto", "Jo Van Bulck", "Marton Bognar"]
conference: "Black Hat"
conference_full: "Black Hat USA 2026"
edition: "USA"
year: 2026
source_pdf: "BlackHat_USA_2026_Slides/Cristiano Rodrigues&Sandro Pinto&Jo Van Bulck&Marton Bognar_Tiny Chips, Big Leaks Breaking TrustZone-M with Single-Stepping Attacks.pdf"
pages: 303
sha256: "1832b2f77bb34b5cb2ce0a3dbb002b04d0403b762650e6b9fc14d74593fc8c06"
text_chars: 78586
ocr_pages: 50
has_ocr: true
redacted_secrets: 6
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:09:29Z"
---
# Tiny Chips, Big Leaks Breaking TrustZone-M with Single-Stepping Attacks

**Speakers:** Cristiano Rodrigues, Sandro Pinto, Jo Van Bulck, Marton Bognar  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/Cristiano Rodrigues&Sandro Pinto&Jo Van Bulck&Marton Bognar_Tiny Chips, Big Leaks Breaking TrustZone-M with Single-Stepping Attacks.pdf` (303 pages)


## Slide 1

## Slide 2

# **Tiny Chips Big Leaks!**

Breaking TrustZone-M with Single-Stepping Attacks **Cristiano Rodrigues, Sandro Pinto,** Marton Bognar, and Jo Van Bulck Centro ALGORITMI, University of Minho, DistriNet, KU Leuven

2

## Slide 3

## **Tiny Chips Big Leaks!** Breaking TrustZone-M with Single-Stepping Attacks

**Cristiano Rodrigues, Sandro Pinto,** Marton Bognar, and Jo Van Bulck Centro ALGORITMI, University of Minho, DistriNet, KU Leuven

77

## Slide 4

## Slide 5

THE FOLLOWING **TECHNICAL PREVIEW** HAS BEEN APPROVED FOR **THE BLACK HAT COMMUNITY**

FOR EDUCATIONAL PURPOSES ONLY

NR

**NOT RATED** The Content of This Talk Has Not Been Evaluated

## Slide 6

```
[REDACTED:private-key-block]
```

## Slide 7

```
[REDACTED:private-key-block]
```

## Slide 8

```
010111001101010101010100100111010101101011
```

## Slide 9

```
010111001101010101010100100111010101101011
101000101011001010101111000101010101010110
101010101010100101010101010101010101111111
010101010101001010101010110001110011010010
101001010101010101101111111111101010010100
101000101010101010101010110101001001010101
010101010100101010100101111111001010101010
101010101111110000010010101101110010101100
010101010101011010001111010101010101010101
010101110101010010101010110101010101010101
010101010101010101010101010101010101010101
```

## Slide 10

```
[REDACTED:private-key-block]
```

## Slide 11

```
010111001101010101010100100111010101101011
101000101011001010101111000101010101010110
101010101010100101010101010101010101111111
010101010101001010101010110001110011010010
101001010101010101101111111111101010010100
101000101010101010101010110101001001010101
010101010100101010100101111111001010101010
101010101111110000010010101101110010101100
010101010101011010001111010101010101010101
010101110101010010101010110101010101010101
010101010101010101010101010101010101010101
```

## Slide 12

```
[REDACTED:private-key-block]
```

## Slide 13

[REDACTED:private-key-block]

## Slide 14

```
[REDACTED:private-key-block]
```

## Slide 15

## Slide 16

## Slide 17

## Slide 18

## Slide 19

## Slide 20

## Slide 21

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
arm
TrustZone’
AMD«¢l
SEV
```

## Slide 22

## Slide 23

## Slide 24

## Slide 25

First TrustZone-M single-stepping framework Instruction-level side-channel analysis Single-trace RSA key extraction **CVE-2025-54764**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ First TrustZone-M single-stepping framework
@ Instruction-level side-channel analysis
3) Single-trace RSA key extraction
CVE-2025-54764
```

## Slide 26

Tiny chips have become valuable targets

## Slide 27

###### Modern Connected World

Satellites

Industrial

Drones

Hardware Wallets

Cars

Medical

Appliances

Wearables

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Modern Connected World
«. eS 1» = 3
Se Baa et bes
Satellites Industrial Drones Hardware Wallets
Cars Medical Appliances Wearables
= 6 & 8
```

## Slide 28

**What powers almost all of them?**

## Slide 29

MCU

## Slide 30

MCU

## Slide 31

MCU

### **CORTEX-M**

## Slide 32

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
600
Revenue in billion U.S. dollars
Annual Production of loT devices
200 bn 2021 2022* 2023* 2024* 2025* 2026* 2027* 2028* 2029* 2030*
L trillion
150 bn .
cumulative
100 bn
50 bn
The route to a trillion devices
0 bn
2017 2020 2023 2026 2029 2032 2035 The outlook for loT investment to 2035
Source: SoftBank and ARM estimates
```

## Slide 33

###### **Armv6-M & Armv7-M**

MCU

###### **CORTEX-M**

Base Architecture

Unprivileged
THREAD

Priv.  THREAD Priv.  HANDLER

## Slide 34

###### **Armv8-M**

MCU

##### **TRUSTZONE-M**

Armv6/7-M Base Architecture

Unprivileged
THREAD
Priv.  THREAD
Priv.  HANDLER

x2

## Slide 35

###### **Armv8-M**

MCU

##### **TRUSTZONE-M**

Secure State

Non-Secure State

Unprivileged Unprivileged THREAD THREAD

Priv.  THREAD Priv.  HANDLER

Priv.  THREAD

Priv.  HANDLER

## Slide 36

**Hand Me Your Secret, MCU! Microarchitectural Timing Attacks on Microcontrollers are Practical**

## Slide 37

**Hand Me Your Secret, MCU! Microarchitectural Timing Attacks on Microcontrollers are Practical**

**What the TrustZone-M Doesn't See, the MCU Does Grieve Over: Lessons Learned from Assessing a Microcontroller TEE**

## Slide 38

**Hand Me Your Secret, MCU! Microarchitectural Timing Attacks on Microcontrollers are Practical**

**What the TrustZone-M Doesn't See, the MCU Does Grieve Over: Lessons Learned from Assessing a Microcontroller TEE**

**?????????????? ??????????????**

## Slide 39

THE LAST MISSING FRAMEWORK

## Slide 40

## Slide 41

## Slide 42

**End-2-End Timing Single-Stepping**

## Slide 43

###### **End-2-End Timing**

Inst 1 1 2 3 4 5 6 7 8
Inst 2 1 2 3 4 5 6 7 8
Inst 3 1 2 3 4 5 6 7 8
Inst 4 1 2 3 4 5 6 7 8
Inst 5 1 2 3 4 5 6 7 8
Inst 6 1 2 3 4 5 6 7 8
Inst 7 1 2 3 4 5 6 7 8
Inst 8 1 2 3 4 5 6 7 8

###### **Single-Stepping**

## Slide 44

###### **End-2-End Timing**

Inst 1 2 3 4 5 6 7 8
Inst 2 2 3 4 6 7 8
Inst 3 3 4 6 7 8
Inst 4 3 4 6 7
Inst 5 3 6 7
Inst 6 3 7
Inst 7 7
Inst 8

###### **Single-Stepping**

## Slide 45

###### **End-2-End Timing**

Temporal
Resolution
Inst 1 2 3 4 5 6 7 8
Inst 2 2 3 4 6 7 8
Inst 3 3 4 6 7 8
Inst 4 3 4 6 7
Inst 5 3 6 7
Inst 6 3 7
Inst 7 7
Inst 8

###### **Single-Stepping**

## Slide 46

###### **End-2-End Timing**

Temporal
Resolution
Inst 1 2 3 4 5 6 7 8
Inst 2 2 3 4 6 7 8
Inst 3 3 4 6 7 8
Inst 4 3 4 6 7
Inst 5 3 6 7
Inst 6 3 7
Inst 7 7
Inst 8

###### **Single-Stepping**

## Slide 47

End-2-End Timing
Temporal
Resolution
Inst 1 2 3 4 5 6 7 8
Inst 2 2 3 4 6 7 8
Inst 3 3 4 6 7 8
Inst 4 3 4 6 7
No Pattern!! No Leak!!
Inst 5 3 6 7
Inst 6 3 7
Inst 7 7
Inst 8

###### **Single-Stepping**

## Slide 48

###### **End-2-End Timing**

Temporal
Resolution
Inst 1 2 3 4 5 6 7 8
Inst 2 2 3 4 6 7 8
Inst 3 3 4 6 7 8
Inst 4 3 4 6 7
No Pattern!! No Leak!!
Inst 5 3 6 7
Inst 6 3 7
Inst 7 7
Inst 8

###### **Single-Stepping**

Inst 1 1 2 3 4 5 6 7 8
Inst 2 1 2 3 4 5 6 7 8
Inst 3 1 2 3 4 5 6 7 8
Inst 4 1 2 3 4 5 6 7 8
Inst 5 1 2 3 4 5 6 7 8
Inst 6 1 2 3 4 5 6 7 8
Inst 7 1 2 3 4 5 6 7 8
Inst 8 1 2 3 4 5 6 7 8

## Slide 49

###### **End-2-End Timing**

Temporal
Resolution
Inst 1 2 3 4 5 6 7 8
Inst 2 2 3 4 6 7 8
Inst 3 3 4 6 7 8
Inst 4 3 4 6 7
No Pattern!! No Leak!!
Inst 5 3 6 7
Inst 6 3 7
Inst 7 7
Inst 8

###### **Single-Stepping**

Inst 1 1 2 3 4 5 6 7 8
Inst 2 1 2 3 4 5 6 7 8
Inst 3 1 2 3 4 5 6 7 8
Inst 4 1 2 3 4 5 6 7 8
Inst 5 1 2 3 4 5 6 7 8
Inst 6 1 2 3 4 5 6 7 8
Inst 7 1 2 3 4 5 6 7 8
Inst 8 1 2 3 4 5 6 7 8

## Slide 50

###### **End-2-End Timing**

Temporal
Resolution
Inst 1 2 3 4 5 6 7 8
Inst 2 2 3 4 6 7 8
Inst 3 3 4 6 7 8
Inst 4 3 4 6 7
No Pattern!! No Leak!!
Inst 5 3 6 7
Inst 6 3 7
Inst 7 7
Inst 8

###### **Single-Stepping**

Inst 1 1 2 3 4 5 6 7 8
Inst 2 1 2 3 4 5 6 7 8
Inst 3 1 2 3 4 5 6 7 8
Inst 4 1 2 3 4 5 6 7 8
Inst 5 1 2 3 4 5 6 7 8
Inst 6 1 2 3 4 5 6 7 8
Inst 7 1 2 3 4 5 6 7 8
Inst 8 1 2 3 4 5 6 7 8

## Slide 51

###### **End-2-End Timing**

Temporal
Resolution
Inst 1 2 3 4 5 6 7 8
Inst 2 2 3 4 6 7 8
Inst 3 3 4 6 7 8
Inst 4 3 4 6 7
No Pattern!! No Leak!!
Inst 5 3 6 7
Inst 6 3 7
Inst 7 7
Inst 8

###### **Single-Stepping**

Inst 1 1 2 3 4 5 6 7 8
Inst 2 1 2 3 4 5 6 7 8
Inst 3 1 2 3 4 5 6 7 8
Inst 4 1 2 3 4 5 6 7 8
Inst 5 1 2 3 4 5 6 7 8
Inst 6 1 2 3 4 5 6 7 8
Inst 7 1 2 3 4 5 6 7 8
Inst 8 1 2 3 4 5 6 7 8

## Slide 52

###### **End-2-End Timing**

Temporal
Resolution
Inst 1 2 3 4 5 6 7 8
Inst 2 2 3 4 6 7 8
Inst 3 3 4 6 7 8
Inst 4 3 4 6 7
No Pattern!! No Leak!!
Inst 5 3 6 7
Inst 6 3 7
Inst 7 7
Inst 8

###### **Single-Stepping**

Inst 1 1 2 3 4 5 6 7 8
Inst 2 1 2 3 4 5 6 7 8
Inst 3 1 2 3 4 5 6 7 8
Inst 4 1 2 3 4 5 6 7 8
Inst 5 1 2 3 4 5 6 7 8
Inst 6 1 2 3 4 5 6 7 8
Inst 7 1 2 3 4 5 6 7 8
Inst 8 1 2 3 4 5 6 7 8

## Slide 53

###### **End-2-End Timing**

###### **Single-Stepping**

Temporal
Resolution
Inst 1 2 3 4 5 6 7 8 Inst 1 1 2 3 4 5 6 7 8
Inst 2 2 3 4 6 7 8 Inst 2 1 2 3 4 5 6 7 8
Inst 3 3 4 6 7 8 Inst 3 1 2 3 4 5 6 7 8
Inst 4 3 4 6 7 Inst 4 1 2 3 4 5 6 7 8
No Pattern!! No Leak!!
Inst 5 3 6 7 Inst 5 1 2 3 4 5 6 7 8
Inst 6 3 7 Inst 6 1 2 3 4 5 6 7 8
Inst 7 7 Inst 7 1 2 3 4 5 6 7 8
Inst 8 Inst 8 1 2 3 4 5 6 7 8

## Slide 54

###### **End-2-End Timing**

Temporal
Resolution
Inst 1 2 3 4 5 6 7 8
Inst 2 2 3 4 6 7 8
Inst 3 3 4 6 7 8
Inst 4 3 4 6 7
No Pattern!! No Leak!!
Inst 5 3 6 7
Inst 6 3 7
Inst 7 7
Inst 8

###### **Single-Stepping**

> **Inst 1 1 2 3 4 5 6 7 8**

> **Inst 2 1 2 3 4 5 6 7 8**

> **Inst 3 1 2 3 4 5 6 7 8**

> **Inst 4 1 2 3 4 5 6 7 8**

> **Inst 5 1 2 3 4 5 6 7 8 Inst 6 1 2 3 4 5 6 7 8**

> **Inst 7 1 2 3 4 5 6 7 8 Inst 8 1 2 3 4 5 6 7 8**

## Slide 55

###### **End-2-End Timing**

Temporal
Resolution
Inst 1 2 3 4 5 6 7 8
Inst 2 2 3 4 6 7 8
Inst 3 3 4 6 7 8
Inst 4 3 4 6 7
No Pattern!! No Leak!!
Inst 5 3 6 7
Inst 6 3 7
Inst 7 7
Inst 8

###### **Single-Stepping**

Inst 1 1 2 3 4 5 6 7 8
Inst 2 1 2 3 4 5 6 7 8
Inst 3 1 2 3 4 5 6 7 8
Inst 4 1 2 3 4 5 6 7 8
Inst 5 1 2 3 4 5 6 7 8
Inst 6 1 2 3 4 5 6 7 8
Inst 7 1 2 3 4 5 6 7 8
Inst 8 1 2 3 4 5 6 7 8

## Slide 56

###### **End-2-End Timing**

Temporal
Resolution
Inst 1 2 3 4 5 6 7 8
Inst 2 2 3 4 6 7 8
Inst 3 3 4 6 7 8
Inst 4 3 4 6 7
No Pattern!! No Leak!!
Inst 5 3 6 7
Inst 6 3 7
Inst 7 7
Inst 8

###### **Single-Stepping**

> **Inst 1 1 2 3 4 5 6 7 8**

> **Inst 2 1 2 3 4 5 6 7 8**

> **Inst 3 1 2 3 4 5 6 7 8**

> **Inst 4 1 2 3 4 5 6 7 8**

> **Inst 5 1 2 3 4 5 6 7 8 Inst 6 1 2 3 4 5 6 7 8**

> **Inst 7 1 2 3 4 5 6 7 8 Inst 8 1 2 3 4 5 6 7 8**

## Slide 57

###### **End-2-End Timing**

Temporal
Resolution
Inst 1 2 3 4 5 6 7 8
Inst 2 2 3 4 6 7 8
Inst 3 3 4 6 7 8
Inst 4 3 4 6 7
No Pattern!! No Leak!!
Inst 5 3 6 7
Inst 6 3 7
Inst 7 7
Inst 8

###### **Single-Stepping**

> **Inst 1 1 2 3 4 5 6 7 8**

> **Inst 2 1 2 3 4 5 6 7 8**

> **Inst 3 1 2 3 4 5 6 7 8**

> **Inst 4 1 2 3 4 5 6 7 8**

> **Inst 5 1 2 3 4 5 6 7 8 Inst 6 1 2 3 4 5 6 7 8**

> **Inst 7 1 2 3 4 5 6 7 8 Inst 8 1 2 3 4 5 6 7 8**

## Slide 58

###### **End-2-End Timing**

Temporal
Resolution
Inst 1 2 3 4 5 6 7 8
Inst 2 2 3 4 6 7 8
Inst 3 3 4 6 7 8
Inst 4 3 4 6 7
No Pattern!! No Leak!!
Inst 5 3 6 7
Inst 6 3 7
Inst 7 7
Inst 8

###### **Single-Stepping**

Inst 1 1 2 3 4 5 6 7 8
Inst 2 1 2 3 4 5 6 7 8
Inst 3 1 2 3 4 5 6 7 8
Inst 4 1 2 3 4 5 6 7 8
Inst 5 1 2 3 4 5 6 7 8
Inst 6 1 2 3 4 5 6 7 8
Inst 7 1 2 3 4 5 6 7 8
Inst 8 1 2 3 4 5 6 7 8

## Slide 59

###### **End-2-End Timing**

Temporal
Resolution
Inst 1 2 3 4 5 6 7 8
Inst 2 2 3 4 6 7 8
Inst 3 3 4 6 7 8
Inst 4 3 4 6 7
No Pattern!! No Leak!!
Inst 5 3 6 7
Inst 6 3 7
Inst 7 7
Inst 8

###### **Single-Stepping**

Inst 1 1 2 3 4 5 6 7 8
Inst 2 1 2 3 4 5 6 7 8
Inst 3 1 2 3 4 5 6 7 8
Inst 4 1 2 3 4 5 6 7 8
Pattern! Leak!
Inst 5 1 2 3 4 5 6 7 8
Inst 6 1 2 3 4 5 6 7 8
Inst 7 1 2 3 4 5 6 7 8
Inst 8 1 2 3 4 5 6 7 8

## Slide 60

###### Single-Step Frameworks

###### **CacheGrab**

**Load-Step**

**SEV-Step**

**TDXeploit TDXdown**

**SGX TrustZone-A TrustZone-A SEV TDX TDX**

## Slide 61

###### Single-Step Frameworks

**CacheGrab Load-Step SEV-Step TDXeploit TDXdown SGX TrustZone-A TrustZone-A SEV TDX TDX TRUSTZONE-M?**

## Slide 62

The Spark: we noticed something weird

## Slide 63

###### General Assumption

Jo Van Bulck et al, “Nemesis: Studying Microarchitectural Timing Leaks in Rudimentary CPU Interrupt Logic”.

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
General Assumption
instruction being interrupted. Alternatively, ARM Cortex MO pro-
cessors [5] abandon multi-cycle instructions to handle any pending
interrupt immediately. While such processors are immune to the
IRQ latency timing attacks described in this paper, they remain
Jo Van Bulck et al, “Nemesis: Studying Microarchitectural Timing Leaks in Rudimentary CPU Interrupt Logic”.
```

## Slide 64

###### General Assumption

Jo Van Bulck et al, “Nemesis: Studying Microarchitectural Timing Leaks in Rudimentary CPU Interrupt Logic”.

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
General Assumption
instruction being interrupted. Alternatively, ARM Cortex MO pro-
cessors [5] abandon multi-cycle instructions to handle any pending
interrupt immediately. While such processors are immune to the
IRQ latency timing attacks described in this paper, they remain
Jo Van Bulck et al, “Nemesis: Studying Microarchitectural Timing Leaks in Rudimentary CPU Interrupt Logic”.
```

## Slide 65

###### General Assumption

Jo Van Bulck et al, “Nemesis: Studying Microarchitectural Timing Leaks in Rudimentary CPU Interrupt Logic”.

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
General Assumption
instruction being interrupted. Alternatively, ARM Cortex MO pro-
cessors [5] abandon multi-cycle instructions to handle any pending
interrupt immediately. W mile such processors are immune to the
IRQ latency timing attacks described in this paper, they remain
Jo Van Bulck et al, “Nemesis: Studying Microarchitectural Timing Leaks in Rudimentary CPU Interrupt Logic”.
```

## Slide 66

###### General Assumption

Jo Van Bulck et al, “Nemesis: Studying Microarchitectural Timing Leaks in Rudimentary CPU Interrupt Logic”.

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
General Assumption
instruction being interrupted. Alternatively, ARM Cortex MO pro-
cessors [5] abandon multi-cycle instructions to handle any pending
interrupt immediately. W mile such processors are immune to the
IRQ latency timing attacks described in this paper, they remain
Jo Van Bulck et al, “Nemesis: Studying Microarchitectural Timing Leaks in Rudimentary CPU Interrupt Logic”.
```

## Slide 67

###### General Assumption

Jo Van Bulck et al, “Nemesis: Studying Microarchitectural Timing Leaks in Rudimentary CPU Interrupt Logic”.

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
General Assumption
instruction being interrupted. Alternatively, ARM Cortex MO pro-
cessors [5] abandon multi-cycle instructions to handle any pending
interrupt immediately. While such processors are immune to the
IRQ latency timing attacks described in this paper, they remain
Jo Van Bulck et al, “Nemesis: Studying Microarchitectural Timing Leaks in Rudimentary CPU Interrupt Logic”.
```

## Slide 68

**Instruction MOV**

###### **Instruction UDIV**

53

## Slide 69

**Instruction MOV**

**Clk 1**

**1 Clock cycle**

###### **Instruction**

**UDIV**

**Clk 1 Clk 2 Clk 3**

**3 Clock cycles**

53

## Slide 70

Instruction
MOV

Timer
Clk 1 ISR
1 Clock cycle

Instruction
UDIV

Clk 1 Clk 2 Clk 3
3 Clock cycles

53

## Slide 71

Instruction
MOV
Timer
Clk 1 ISR
1 Clock cycle

Instruction
UDIV
Timer
Clk 1 ISR Clk 2 Clk 3
1 Clock cycle

53

## Slide 72

**Instruction MOV**

###### **Instruction UDIV**

53

## Slide 73

Instruction
MOV

Timer
Clk 1 ISR

Instruction
UDIV

53

## Slide 74

Instruction
MOV
Timer
Clk 1 ISR

**Instruction UDIV**

53

## Slide 75

Instruction
MOV
Timer
Clk 1 ISR

Instruction
UDIV

53

## Slide 76

Instruction
MOV
Timer
Clk 1 ISR
1 Clock

**Instruction UDIV**

53

## Slide 77

Instruction
MOV
Timer
Clk 1 ISR
1 Clock

Instruction
UDIV
Timer
Clk 1 Clk 2 Clk 3 ISR

53

## Slide 78

Instruction
MOV
Timer
Clk 1 ISR
1 Clock

Instruction
UDIV

Timer
Clk 1 Clk 2 Clk 3 ISR
3 Clocks

53

## Slide 79

###### **Instruction**

**MOV**

Timer
Clk 1 ISR
1 Clock

**Instruction UDIV**

Timer
Clk 1 Clk 2 Clk 3 ISR
3 Clocks

53

## Slide 80

###### **Instruction**

###### **Instruction**

MOV UDIV
Timer Timer
Different Interrupt Latencies
Clk 1 ISR Clk 1 Clk 2 Clk 3 ISR
1 Clock
3 Clocks

53

## Slide 81

Instruction Instruction
MOV UDIV
Timer Timer
Different Interrupt Latencies
Clk 1 ISR LEAK! Clk 1 Clk 2 Clk 3 ISR
1 Clock
3 Clocks
53

## Slide 82

###### If (S=1)

Instruction 1 else Instruction 2

Timer
Clk 1 ISR
1 Clock
Timer
Clk 1 Clk 2 Clk 3 ISR
3 Clocks

53

## Slide 83

The Bumpy Road to Achieve Single-Stepping

## Slide 84

###### Single-Stepping

**Instruction Instruction Instruction Instruction Instruction Instruction Instruction Instruction Instruction Instruction Debug Production**

**Production**

## Slide 85

###### Single-Stepping

**Instruction Instruction Instruction Instruction Instruction Debug**

**Instruction Instruction Instruction Instruction Instruction**

**Production**

## Slide 86

###### Single-Stepping

**Instruction Instruction Instruction Instruction Instruction Instruction Instruction Instruction Instruction Instruction Debug Production**

**Production**

## Slide 87

###### Single-Stepping

**Instruction Instruction Instruction Instruction Instruction Instruction Instruction Instruction Instruction Instruction Debug Production**

**Production**

## Slide 88

###### Single-Stepping

**Instruction Instruction Instruction Instruction Instruction Instruction Instruction Instruction Instruction Instruction Debug Production**

**Production**

## Slide 89

###### Single-Stepping

**Instruction Instruction Instruction Instruction Instruction**

**Debug**

**Instruction Instruction Instruction Instruction Instruction**

**Production**

## Slide 90

###### Single-Stepping

**Instruction Instruction Instruction Instruction Instruction Debug**

**Instruction Instruction Instruction Instruction Instruction**

**Production**

## Slide 91

###### Single-Stepping

**Instruction Instruction Instruction Instruction Instruction Debug**

**Instruction Instruction Instruction Instruction Instruction**

**Production**

## Slide 92

###### Single-Stepping

**Instruction Timer** **Instruction Instruction Instruction Instruction Debug**

**Instruction Instruction Instruction Instruction Instruction Production**

## Slide 93

###### Single-Stepping

**Instruction Instruction Instruction Timer** **Instruction Instruction Instruction Instruction Instruction Instruction Instruction Debug Production**

## Slide 94

Single-Stepping

**Instruction Instruction Instruction Instruction Instruction Timer** **Instruction Instruction Instruction Instruction Instruction Debug Production**

## Slide 95

###### Single-Stepping

**Instruction Instruction Instruction Instruction Instruction Instruction Instruction Timer** **Instruction Instruction Instruction Debug Production**

## Slide 96

###### Single-Stepping

**Instruction Instruction Instruction Instruction Instruction Instruction Instruction Instruction Instruction Timer** **Instruction Debug Production**

## Slide 97

**Timer Context Switch**

## Slide 98

Timer Context Switch
Ctx Switch
Inst Inst Inst Inst

## Slide 99

**Timer Context Switch**

## Slide 100

**Timer Context Switch**

## Slide 101

Zero-Step
Timer Context Switch
Ctx Switch
Too Early!
Inst Inst Inst Inst

## Slide 102

Multi-Step
Zero-Step
Timer Context Switch
Ctx Switch
Too Late!
Inst Inst Inst Inst

## Slide 103

Multi-Step
Zero-Step
Timer Context Switch
Ctx Switch
Single-Step!
Inst Inst Inst Inst

## Slide 104

###### **Multi-Step**

**Zero-Step Timer Context Switch Ctx Switch S ngle-Step!**

## Slide 105

**Timer Context Switch**

## Slide 106

**Timer Context Switch**

## Slide 107

Timer Context Switch
Inst Inst Inst Inst

**Ctx Switch**

## Slide 108

Timer Context Switch
Inst Inst Inst Inst

**Ctx Switch**

## Slide 109

Timer Context Switch
Inst Inst Inst Inst

**Ctx Switch**

## Slide 110

Timer Context Switch
Ctx Switch
Inst Inst Inst Inst

## Slide 111

Timer Context Switch
Inst Inst Inst Inst

**Ctx Switch**

## Slide 112

Timer Context Switch
Ctx Switch
Single-Step!
Inst Inst Inst Inst

## Slide 113

Timer Instruction
Instruction
Instruction
Instruction
Instruction
ISR Instruction
Cortex-M

## Slide 114

Instruction
Instruction
Timer
Instruction
Instruction
Instruction
ISR Instruction
Cortex-M

## Slide 115

Instruction
Instruction
Timer Instruction
Instruction
Instruction
ISR Instruction
Cortex-M

## Slide 116

Instruction
Instruction
Timer Instruction
Instruction
Instruction
ISR Instruction
Cortex-M

## Slide 117

##### **Single-Step Challenges On Cortex-M**

## Slide 118

###### **Normal Instructions**

###### **Interruptible Instructions**

39

## Slide 119

###### **Normal Instructions**

Timer
Instruction 1 ISR

###### **Interruptible Instructions**

39

## Slide 120

###### **Normal Instructions**

Timer
Instruction 1 ISR

###### **Interruptible Instructions**

39

## Slide 121

###### **Normal Instructions**

Timer
Instruction 1 ISR

###### **Interruptible Instructions**

Timer
Instruction 1 ISR

39

## Slide 122

###### **Normal Instructions**

Timer
Instruction 1 ISR

###### **Interruptible Instructions**

Timer
Instru ISR ction 1

39

## Slide 123

###### **Normal Instructions**

Timer
Instruction 1 ISR

###### **Interruptible Instructions**

Timer
Instru ISR ction 1

39

## Slide 124

###### **Normal Instructions**

Timer
Instruction 1 ISR

###### **Interruptible Instructions**

Timer
Instru ISR ction 1

39

## Slide 125

###### **Normal Instructions**

###### **Interruptible Instructions**

Timer
Instruction 1 ISR

Timer
Instru ISR ction 1

###### **Heterogenous Interrupt Behavior!!**

39

## Slide 126

##### **Cortex-M Instruction Classes**

## Slide 127

###### Cortex-M Instruction Classes

Restartable
Atomic Resumable

41

## Slide 128

###### Cortex-M Instruction Classes

Atomic

**Resumable**

**Restartable**

41

## Slide 129

###### Cortex-M Instruction Classes

Atomic

Resumable

Restartable

41

## Slide 130

###### Cortex-M Instruction Classes

Atomic

Resumable

Restartable

41

## Slide 131

###### Cortex-M Instruction Classes

Atomic
Timer
Restartable
Resumable
Clk 1 Clk 2 Clk 3 ISR
Interrupts can
arrive anywhere.

41

## Slide 132

###### Cortex-M Instruction Classes

Atomic
Timer
Restartable
Resumable
Clk 1 Clk 2 Clk 3 ISR
Interrupts can
arrive anywhere.

41

## Slide 133

###### Cortex-M Instruction Classes

Atomic
Timer
Restartable
Resumable
Clk 1 Clk 2 Clk 3 ISR
Interrupts can
arrive anywhere.

41

## Slide 134

###### Cortex-M Instruction Classes

Atomic
Timer
Restartable
Resumable
Clk 1 Clk 2 Clk 3 ISR
Interrupts can
arrive anywhere.

41

## Slide 135

###### Cortex-M Instruction Classes

Atomic Resumable
Timer Timer
Restartable
Clk 1 Clk 2 Clk 3 ISR Clk 1 Clk 2 Clk 3
Interrupts can  Interrupts require
arrive anywhere. extra clock cycle.

41

## Slide 136

###### Cortex-M Instruction Classes

Restartable

Atomic Resumable

Timer Timer
Restartable
Clk 1 Clk 2 Clk 3 ISR Clk 1 ISR Clk 2 Clk 3
Interrupts can  Interrupts require
arrive anywhere. extra clock cycle.

41

## Slide 137

###### Cortex-M Instruction Classes

Restartable

Atomic

**Resumable**

Timer Timer
Restartable
Clk 1 Clk 2 Clk 3 ISR Clk 1 ISR X Clk 2 Clk 3
Interrupts can  Interrupts require
arrive anywhere. extra clock cycle.

41

## Slide 138

###### Cortex-M Instruction Classes

Atomic Resumable
Timer Timer
Restartable
Clk 1 Clk 2 Clk 3 ISR Clk 1 ISR X Clk 2 Clk 3
Interrupts can  Interrupts require
arrive anywhere. extra clock cycle.

41

## Slide 139

###### Cortex-M Instruction Classes

Restartable

Atomic

**Resumable**

Timer Timer
Restartable
Clk 1 Clk 2 Clk 3 ISR Clk 1 ISR X Clk 2 Clk 3
Interrupts can  Interrupts require
arrive anywhere. extra clock cycle.

41

## Slide 140

###### Cortex-M Instruction Classes

Restartable

Atomic

Resumable

Timer Timer
Restartable
Clk 1 Clk 2 Clk 3 ISR Clk 1 ISR X Clk 2 Clk 3
Interrupts can  Interrupts require
arrive anywhere. extra clock cycle.

41

## Slide 141

###### Cortex-M Instruction Classes

Atomic Resumable Restartable
Timer Timer Timer
Clk 1 Clk 2 Clk 3 ISR Clk 1 ISR X Clk 2 Clk 3 Clk 1 Clk 2 Clk 3
Interrupts can  Interrupts require  Interrupt must arrive in
arrive anywhere. extra clock cycle. the last clock cycle.

41

## Slide 142

###### Cortex-M Instruction Classes

**Atomic**

**Resumable**

###### **Restartable**

**Timer Timer Clk 1 Clk 2 Clk 3 ISR Clk 1 ISR X Clk 2 Clk 3 Interrupts can Interrupts require arrive anywhere. extra clock cycle.**

Timer
Clk 1 ISR

**Interrupt must arrive in the last clock cycle.**

41

## Slide 143

###### Cortex-M Instruction Classes

**Atomic**

**Resumable**

###### **Restartable**

Timer
Clk 1 Clk 2 Clk 3 ISR
Interrupts can
arrive anywhere.

Timer
Clk 1 ISR X Clk 2 Clk 3
Interrupts require
extra clock cycle.

Timer
Clk 1 Clk 2 ISR

**Interrupt must arrive in the last clock cycle.**

41

## Slide 144

###### Cortex-M Instruction Classes

**Atomic**

**Resumable**

**Restartable**

Timer Timer
Clk 1 Clk 2 Clk 3 ISR Clk 1 ISR X Clk 2 Clk 3
Interrupts can  Interrupts require
arrive anywhere. extra clock cycle.

Timer
Clk 1 Clk 2 Clk 3 ISR
Interrupt must arrive in
the last clock cycle.

41

## Slide 145

###### Cortex-M Instruction Classes

Atomic Resumable Restartable
Timer Timer
Timer
Clk 1 Clk 2 Clk 3 ISR Clk 1 ISR X Clk 2 Clk 3 Clk 1 Clk 2 Clk 3 ISR
Interrupts can  Interrupts require  Interrupt must arrive in
arrive anywhere. extra clock cycle. the last clock cycle.

41

## Slide 146

##### **Dynamic Single-Step Algorithm**

## Slide 147

**Timer Context Switch Instruction Instruction**

**Timer**

## Slide 148

Timer Context Switch Instruction Instruction

**Timer**

## Slide 149

Timer Context Switch Instruction Instruction

Timer

## Slide 150

Timer
Atomic
Instruction
Instruction
Instruction
Instruction
ISR Instruction
Cortex-M

## Slide 151

Instruction
Atomic
Timer
Instruction
Instruction
Instruction
ISR Instruction
Cortex-M

## Slide 152

Instruction
Instruction
Timer Restartable
Instruction
Instruction
ISR Instruction
Cortex-M

## Slide 153

Instruction
Instruction
Timer Restartable
Instruction
Instruction
ISR Instruction
Cortex-M

## Slide 154

Timer Context Switch Instruction
Instruction
Instruction
Timer Restartable
Instruction
Instruction
ISR Instruction
Cortex-M

## Slide 155

Timer Context Switch Instruction
Instruction
Instruction
Timer Restartable
Instruction
Instruction
ISR Instruction
Cortex-M

## Slide 156

Instruction
Instruction
Timer Restartable
Instruction
Instruction
ISR Instruction
Cortex-M

## Slide 157

Instruction
Instruction
Timer Restartable
Instruction
Instruction
ISR Instruction
Cortex-M

## Slide 158

Timer Context Switch Instruction
Instruction
Instruction
Timer Restartable
Instruction
Instruction
ISR Instruction
Cortex-M

## Slide 159

Timer Context Switch Instruction
Instruction
Instruction
Timer Restartable
Instruction
Instruction
ISR Instruction
Cortex-M

## Slide 160

Instruction
Instruction
Timer Restartable
Instruction
Instruction
ISR Instruction
Cortex-M

## Slide 161

Instruction
Instruction
Instruction
Timer Atomic
Instruction
ISR Instruction
Cortex-M

## Slide 162

Instruction
Instruction
Instruction
Timer Instruction
Atomic
ISR Instruction
Cortex-M

## Slide 163

Instruction
Instruction
Instruction
Timer Instruction
Instruction
ISR Atomic
Cortex-M

## Slide 164

**But…..**

## Slide 165

**How can we detect that we are making progress?**

## Slide 166

##### **Progress Detection on Cortex-M**

## Slide 167

**Detect Zero-Steps on APUs**

**Detect Zero-Steps on Cortex-M**

## Slide 168

###### **Detect Zero-Steps on APUs**

###### **Zero-Step**

**Instruction 1**

**Detect Progression on Cortex-M**

###### **Single-Step**

**Instruction 1**

## Slide 169

###### **Detect Zero-Steps on APUs**

###### **Zero-Step**

Instruction 1

**Detect Progression on Cortex-M**

###### **Single-Step**

**Instruction 1**

## Slide 170

###### **Detect Zero-Steps on APUs**

###### **Zero-Step**

Instruction 1

###### **Detect Progression on Cortex-M**

**Single-Step**

Instruction 1 Instruction 2

## Slide 171

###### **Detect Zero-Steps on APUs**

###### **Zero-Step**

Instruction 1
Page-Table Access Bits

**Detect Progression on Cortex-M**

**Single-Step**

Instruction 1 Instruction 2

## Slide 172

###### **Detect Zero-Steps on APUs**

###### **Zero-Step**

Instruction 1
Page-Table Access Bits

**Detect Progression on Cortex-M**

**Single-Step**

Instruction 1 Instruction 2
Page-Table Access Bits

## Slide 173

###### **Detect Zero-Steps on APUs**

###### **Zero-Step**

Instruction 1
Page-Table Access Bits

###### **Detect Progression on Cortex-M**

###### **Single-Step**

Instruction 1 Instruction 2
Page-Table Access Bits

## Slide 174

###### **Detect Zero-Steps on APUs**

###### **Zero-Step**

###### **Single-Step**

Instruction 1
Page-Table Access Bits

Instruction 1 Instruction 2
Page-Table Access Bits

###### **Detect Progression on Cortex-M**

## Slide 175

###### **Detect Zero-Steps on APUs**

Zero-Step

###### **Single-Step**

Instruction 1
Page-Table Access Bits

###### **No Virtual Memory on Cortex-M!!**

Instruction 1 Instruction 2
Page-Table Access Bits

###### **Detect Progression on Cortex-M**

## Slide 176

###### **Detect Zero-Steps on APUs**

Instruction 1
Page-Table Access Bits

###### **Zero-Step**

###### **Detect Zero-Steps on Cortex-M**

Instruction 1

###### **Zero-Step**

###### **Latency Oracle**

###### **No Virtual Memory on Cortex-M!!**

###### **Single-Step**

Instruction 1 Instruction 2
Page-Table Access Bits

Single-Step

**Instruction 1Instr on 1 Instruction 2Instr on 2 1 2 1 4 3 1**

**Latency Oracle**

## Slide 177

###### **Detect Zero-Steps on APUs**

Instruction 1
Page-Table Access Bits

###### **Zero-Step**

###### **Detect Zero-Steps on Cortex-M**

Instruction 1
1

###### **Zero-Step**

###### **Latency Oracle**

###### **No Virtual Memory on Cortex-M!!**

###### **Single-Step**

Instruction 1 Instruction 2
Page-Table Access Bits

Single-Step

Instruction 1Instr on 1 Instruction 2Instr on 2
1 2 1 4 3 1

**Latency Oracle**

## Slide 178

###### **Detect Zero-Steps on APUs**

Instruction 1
Page-Table Access Bits

###### **Zero-Step**

###### **Detect Zero-Steps on Cortex-M**

Instruction 1
1 1

###### **Zero-Step**

###### **Latency Oracle**

###### **No Virtual Memory on Cortex-M!!**

###### **Single-Step**

Instruction 1 Instruction 2
Page-Table Access Bits

Single-Step

Instruction 1Instr on 1 Instruction 2Instr on 2
1 2 1 4 3 1

**Latency Oracle**

## Slide 179

###### **Detect Zero-Steps on APUs**

Instruction 1
Page-Table Access Bits

###### **Zero-Step**

###### **Detect Zero-Steps on Cortex-M**

Instruction 1
1 1 1

###### **Zero-Step**

###### **Latency Oracle**

###### **No Virtual Memory on Cortex-M!!**

###### **Single-Step**

Instruction 1 Instruction 2
Page-Table Access Bits

Single-Step

**Instruction 1Instr on 1 Instruction 2Instr on 2 1 2 1 4 3 1**

**Latency Oracle**

## Slide 180

###### **Detect Zero-Steps on APUs**

Instruction 1
Page-Table Access Bits

###### **Zero-Step**

###### **Detect Zero-Steps on Cortex-M**

Instruction 1
1 1 1 1

###### **Zero-Step**

###### **Latency Oracle**

###### **No Virtual Memory on Cortex-M!!**

###### **Single-Step**

Instruction 1 Instruction 2
Page-Table Access Bits

Single-Step

**Instruction 1Instr on 1 Instruction 2Instr on 2 1 2 1 4 3 1**

**Latency Oracle**

## Slide 181

###### **Detect Zero-Steps on APUs**

Instruction 1
Page-Table Access Bits

###### **Zero-Step**

###### **Detect Zero-Steps on Cortex-M**

Instruction 1
1 1 1 1 1

###### **Zero-Step**

###### **Latency Oracle**

###### **No Virtual Memory on Cortex-M!!**

###### **Single-Step**

Instruction 1 Instruction 2
Page-Table Access Bits

Single-Step

**Instruction 1Instr on 1 Instruction 2Instr on 2 1 2 1 4 3 1**

**Latency Oracle**

## Slide 182

###### **Detect Zero-Steps on APUs**

Instruction 1
Page-Table Access Bits

###### **Zero-Step**

###### **Detect Zero-Steps on Cortex-M**

Instruction 1
1 1 1 1 1 1

###### **Zero-Step**

###### **Latency Oracle**

###### **No Virtual Memory on Cortex-M!!**

###### **Single-Step**

Instruction 1 Instruction 2
Page-Table Access Bits

Single-Step

Instruction 1Instr on 1 Instruction 2Instr on 2
1 2 1 4 3 1

**Latency Oracle**

## Slide 183

###### **Detect Zero-Steps on APUs**

Instruction 1
Page-Table Access Bits

###### **Zero-Step**

###### **Detect Zero-Steps on Cortex-M**

Instruction 1
1 1 1 1 1 1

###### **Zero-Step**

###### **Latency Oracle**

###### **No Virtual Memory on Cortex-M!!**

###### **Single-Step**

Instruction 1 Instruction 2
Page-Table Access Bits

###### **Single-Step**

Instruction 1Instr on 1 Instruction 2Instr on 2
1 2 1 4 3 1

**Latency Oracle**

## Slide 184

###### **Detect Zero-Steps on APUs**

Instruction 1
Page-Table Access Bits

###### **Zero-Step**

###### **Detect Zero-Steps on Cortex-M**

Instruction 1
1 1 1 1 1 1

###### **Zero-Step**

###### **Latency Oracle**

###### **No Virtual Memory on Cortex-M!!**

###### **Single-Step**

Instruction 1 Instruction 2
Page-Table Access Bits

###### **Single-Step**

Instruction 1Instr on 1 Instruction 2Instr on 2

1 2 1 4 3 1

**Latency Oracle**

## Slide 185

###### **Detect Zero-Steps on APUs**

Instruction 1
Page-Table Access Bits

###### **Zero-Step**

###### **Detect Zero-Steps on Cortex-M**

Instruction 1
1 1 1 1 1 1

###### **Zero-Step**

###### **Latency Oracle**

###### **No Virtual Memory on Cortex-M!!**

###### **Single-Step**

Instruction 1 Instruction 2
Page-Table Access Bits

Single-Step

Instruction 1Instr on 1 Instruction 2Instr on 2
1 2 1 4 3 1

**Latency Oracle**

## Slide 186

###### **Detect Zero-Steps on APUs**

Instruction 1
Page-Table Access Bits

###### **Zero-Step**

###### **Detect Zero-Steps on Cortex-M**

Instruction 1
1 1 1 1 1 1

###### **Zero-Step**

###### **Latency Oracle**

###### **No Virtual Memory on Cortex-M!!**

###### **Single-Step**

Instruction 1 Instruction 2
Page-Table Access Bits

###### **Single-Step**

Instruction 1Instr on 1 Instruction 2Instr on 2
1 2 1 4 3 1

**Latency Oracle**

## Slide 187

###### **Detect Zero-Steps on APUs**

Instruction 1
Page-Table Access Bits

###### **Zero-Step**

###### **Detect Zero-Steps on Cortex-M**

Instruction 1
1 1 1 1 1 1

###### **Zero-Step**

###### **Latency Oracle**

###### **No Virtual Memory on Cortex-M!!**

###### **Single-Step**

Instruction 1 Instruction 2
Page-Table Access Bits

###### **Single-Step**

Instruction 1Instr on 1 Instruction 2Instr on 2
1 2 1 4 3 1

**Latency Oracle**

## Slide 188

###### **Detect Zero-Steps on APUs**

Instruction 1
Page-Table Access Bits

###### **Zero-Step**

###### **Detect Zero-Steps on Cortex-M**

Instruction 1
1 1 1 1 1 1

###### **Zero-Step**

###### **Latency Oracle**

###### **No Virtual Memory on Cortex-M!!**

###### **Single-Step**

Instruction 1 Instruction 2
Page-Table Access Bits

Single-Step

Instruction 1Instr on 1 Instruction 2Instr on 2
1 2 1 4 3 1

**Latency Oracle**

## Slide 189

###### **Detect Zero-Steps on APUs**

Instruction 1
Page-Table Access Bits

###### **Zero-Step**

###### **Detect Zero-Steps on Cortex-M**

Instruction 1
1 1 1 1 1 1

###### **Zero-Step**

###### **Latency Oracle**

###### **No Virtual Memory on Cortex-M!!**

###### **Single-Step**

Instruction 1 Instruction 2
Page-Table Access Bits

Single-Step

Instruction 1Instr on 1 Instruction 2Instr on 2
1 2 1 4 3 1

**Latency Oracle**

## Slide 190

###### **Detect Zero-Steps on APUs**

Instruction 1
Page-Table Access Bits

###### **Zero-Step**

###### **Detect Zero-Steps on Cortex-M**

Instruction 1
1 1 1 1 1 1
Latency Oracle

###### **Zero-Step**

###### **No Virtual Memory on Cortex-M!!**

###### **Single-Step**

Instruction 1 Instruction 2
Page-Table Access Bits

Single-Step

Instruction 1Instr on 1 Instruction 2Instr on 2

1 2 1 4 3 1
Latency Oracle

## Slide 191

###### **Detect Zero-Steps on APUs**

Zero-Step Instruction 1
Page-Table Access Bits
No Virtual Memory on Cortex-M!!

###### **Zero-Step**

Instruction 1 Instruction 2
Page-Table Access Bits

###### **Single-Step**

###### **Detect Zero-Steps on Cortex-M**

Zero-Step Instruction 1
1 1 1 1 1 1
Latency Oracle
Detect Zero-Steps via Latency Oracle!
Single-Step Instruction 1Instr on 1 Instruction 2Instr on 2
1 2 1 4 3 1
Latency Oracle

**Latency Oracle Detect Zero-Steps via Latency Oracle!**

Single-Step

## Slide 192

##### **Voilà! Single-Step on Cortex-M**

## Slide 193

Timer PUSH
MOV
LDR
B
4 4
MUL 3 3
2
UDIV
1
1
POP
Code Interrupt Latency Trace

## Slide 194

Timer PUSH
MOV
LDR
B
4 4
MUL 3 3
2
UDIV
1
1
POP
Code Interrupt Latency Trace

## Slide 195

PUSH
Timer MOV
LDR
B
4 4
MUL 3 3
2
UDIV
1
1
POP
Code Interrupt Latency Trace

**Interrupt Latency Trace**

## Slide 196

PUSH
MOV
Timer LDR
B
4 4
MUL 3 3
2
UDIV
1
1
POP
Code Interrupt Latency Trace

**Interrupt Latency Trace**

## Slide 197

PUSH
MOV
LDR
Timer B
4 4
MUL 3 3
2
UDIV
1
1
POP
Code Interrupt Latency Trace

**Interrupt Latency Trace**

## Slide 198

PUSH
MOV
LDR
B
4 4
Timer MUL 3 3
2
UDIV
1
1
POP
Code Interrupt Latency Trace

**Interrupt Latency Trace**

## Slide 199

PUSH
MOV
LDR
B
4 4
MUL 3 3
2
Timer UDIV
1
1
POP
Code Interrupt Latency Trace

**Interrupt Latency Trace**

## Slide 200

PUSH
MOV
LDR
B
4 4
MUL 3 3
2
UDIV
1
1
Timer POP
Code Interrupt Latency Trace

**Interrupt Latency Trace**

## Slide 201

**M-Step Framework**

## Slide 202

**M-Step Framework**

## Slide 203

39

## Slide 204

Profile

Pwn

39

## Slide 205

Profile

###### **Develop the Exploit**

Pwn

**Recover Secrets**

39

## Slide 206

**1**<sup>**st**</sup> **M-Step Use Case- Printf**

Printf TA
SPY
TF-M
Cortex-M
Memory

## Slide 207

1 st  M-Step
Use Case- Printf

Printf TA
SPY 1
TF-M
Cortex-M
Memory

## Slide 208

**1**<sup>**st**</sup> **M-Step Use Case- Printf**

M-Step
2
Printf TA
SPY 1
TF-M
Cortex-M
Memory

## Slide 209

**Raw Trace**

## Slide 210

**Raw Trace**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
O©ANDUAWNHR
@x@c@24dd6
@x0c@2b81a
@x0c@2b81e
@x@c@2b820
@x@c@2b824
@x0@c@2b826
@x0c@2b828
@x0c@2b82a
@x@c@2b82c
@x@c@2be12
@x@c@2be14
@x0c@2be16
@x@c@2bela
@x0cO2b830
@x0@c@2b834
@x0@c@2b846
@x@c@2b848
@x0c@2b84a
@x0c@2b84c
@x@c@2c406
@x@c@2c408
@x@c@2c40c
@x0c@2c410
@x@c@2c412
@x@c@2c414
@x@c@2c416
@x@c@2c41a
@x@c@2c41c
@x@c@2c41e
@x@c@2c422
@x@c@2c426
@x@c@2c428
@x@c@2c42a
@x@c@2c42c
@x@c@2c3ce
@x0c@2c3d2
@x@c@2c36c
@x@c@2c370
@x@c@2c374
@x@c@2c378
@x@c@2c37a
@x@c@2c37e
@x@c@2c380
@x@c@2c382
@x@c@2c384
e1
@3
e1
e@3
e1
e1
e1
e1
Q1
e1
e1
@3
e1
e1
e1
e1
e1
e1
e1
@3
e1
e1
@2
e1
e1
e1
e1
e1
e@2
@2
e1
e1
Q2
e1
e1
e1
@3
e2
e@2
e1
e1
e1
e1
e1
e1
46
47
48
49
50
51
52
53
54
55
56
57
58
59
68
61
62
63
64
65
66
67
68
69
78
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
Qx0@c02c388
@x@c02c38a
@x@c02c38c
@x@c@2c1le
@x@c02c120
@x@c@2c122
@x@c@2c12e
@x@c02c130
@x@c02c134
@x0@c02c138
@x@c@2c124
Qx@c02c126
@x@c02c140
@x@c@2c142
Qx@c02c146
@x@c@2c14a
Qx@c02c150
@x@c@2c12a
@x@c@2c15e
@x@c02c390
@x@c02c394
@x@c@2c396
@x@c02c398
@x@c02c39a
@x@c02c39c
@x@c@2c2cc
@x0c@2c2do
@x@c@2c2d2
@x@c@2c2d4
@x0c@2c2d6
@x@c@2c2d8
@x@c02c334
0x@c02c338
@x@c02c33c
@x0@c02c340
Qx0@c02c346
@x@c02c348
@x@c@2c2dc
@x@c@2c2de
@x0c@2be38
@x@c@2be3c
@x@c@2be3e
@x@c@2be40
@x@c@2be42
@x@cO2be4c
e1
e1
e1
3
e2
e1
@2
e1
@2
e1
@2
e1
e2
e1
@2
e1
e1
e1
04
e1
e1
e1
e1
e1
e1
Q3
e1
e1
e1
e2
e1
e2
e1
e2
e1
@2
e1
e1
e1
e1
e1
3
e1
e1
e2
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
@x@c@2be4e
@x@c@2be56
@x@c@2be58
@x@c@2be5a
@x0c01F33c
@x@c01F33e
Qx0c01F340
@x0ce1feec
@x0c01feee
Ox@ce1fef2
Oxece1fef4
Ox@ce1feféE
Qxe0ce1fefs
xece1fefa
Ox0ce1feFc
Qx0ce1F100
@x0c01F104
@x0c01F108
@x0c01F10Cc
@x0c01F110
@x@ce1f114
Qx0c01f134
@x@c@1fi1le
@x0ce1f12a
@x0c01F122
@x0ce1f124
Qx0c01F138
@x0c01F13c
@x0c01F140
Qx0c01F148
@x0ce1f14a
@x0ce1F14c
@x@c01F150
@x0ce01f154
@x@c01f18e
@x@c01F192
@x0c01F196
@x0c01F198
@x0c01F19c
@x@c01f19e
@x@c01f1a2
@x@ce1f1a4
@x@ce01f1a6
@x@c01filaa
@x@c01flae
Q1
e1
e1
e1
e1
e2
e1
e1
3
e2
e@2
e1
e2
e1
e1
e1
e1
e3
e1
e1
Q1
e1
e1
e1
e2
e1
2
e1
e1
e1
e1
e1
3
e1
e1
e1
e1
3
e2
e1
2
e@2
e2
e1
@2
136
137
138
139
140
141
142
143
144
145
146
147
148
149
158
151
152
153
154
155
156
157
158
159
168
161
162
163
164
165
166
167
168
169
178
171
172
173
174
175
176
177
178
179
180
@x@c01Ff1b2
@x0c01Ff1b4
@xO@c01F1b6
@x@c@1fiba
@xOc@1fice
@x0c0@1f1be
@x0c@1F1cO
@x@c@1f1c2
@x@c@1f1c4
@x0c@1f1c6
@x0cO@1F1c8
@xOc@1ficc
@x0@c01F166
@x0c01F168
@x0c@1f16c
@x0c0@1f16e
@x@c@1f17a
@x0c@1F17¢
@x0c@1f17e
@x0c01F180
@x@c@1F182
@x@cO2952c
@x@c02952e
@x0c029530
@x@c029532
@x@c029536
@x0c029538
@x@c02953c
Qx@cQ29552
@x@c02953e
@x@c029540
@x@c029542
@x@c02955e
Qx@c029560
Qx@c029562
@x@c029542
@x@c@2955e
@x@c029560
@x@c029562
@x@c029542
@x@c02955e
@x@c029560
@x@c029562
@x@c029542
@x@c@2955e
Q1
@2
@3
e1
@2
@2
e1
@2
e1
@2
@3
@1
Q1
@3
@2
Q1
e1
Q1
e1
Q1
e1
Q1
@3
e1
Q1
e1
e1
Q1
e1
Q1
e1
@1
Q1
@2
Q1
e1
Q1
e2
Q1
e1
@1
@2
e1
e1
e@1
181
182
183
184
185
186
187
188
189
198
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
@x@c@29560
Qx0c@29562
@x0@c@29542
@x@c@2955e
@x0c@29560
@x@c@29562
Qx0c@29542
@x@c@2955e
@x0c@29560
@x0c@29562
@x@c@29542
@x@c@2955e
@x@c@29560
Qx0c@29562
@x0@c@29542
@x@c@2955e
@x0c@29560
@x@c@29562
Qx0c@29542
@x@c@2955e
@x0c@29560
@x0@c@29562
@x@c@29542
@x@c@2955e
@x@c@29560
Qx0c@29562
@x0@c@29542
@x@c@2955e
@x0c@29560
@x@c@29562
Qx0c@29542
@x@c@2955e
@x@c@29560
@x0@c@29562
@x@c@29542
@x@c@2955e
@x0@c@29560
@x0c@29562
@x0@c@29542
@x@c@2955e
@x0c@29560
@x@c@29562
Qx0c@29542
@x@c@2955e
@x0@c@29560
e@2
e1
e1
e1
2
e1
e1
e1
e2
e1
e1
e1
e@2
e1
e1
e1
2
e1
e1
Q1
e2
e1
e1
e1
e2
e1
Q1
e1
e2
e1
e1
e1
e2
e1
e1
e1
e@2
e1
e1
e1
e2
Q1
e1
e1
@2
226
227
228
229
230
231
232
233
234
235
236
237
238
239
248
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
@x@c@29562
@x@c@29542
@x@c@2955e
Qx@c0@29560
@x@c@29562
@x@c@29542
@x@c@29546
@x0c@29548
@x@c@2954c
@x@c@29550
@x0@c01Ff186
@x0c@1f12e
0x0c01F130
@x@c@2be5e
@x@c@2be60
@x@c@2be64
@xO@c@2be66
@x@c@2be7a
@x@c@2be7c
@x@c@2be52
@x@c@2be4a
@x@c@2c2e2
@x@cO@2c2e4
@x@c@2c2e6
Qx@c@2c2e8
@x@c@2c2ec
@x0cO2c2FO
@x0cO2c2F2
@xOcO2c2F4
@x0cO2c2F6
@x0cO2c2F8
@x@cO@2c2Fc
Qx@c02c300
@x@c@2968e
Qx@c0@29690
@x@c@29692
@x0@c0@296be
@x@c0@296b4
@x0c@29694
Qx0@c@29696
@x@c@29698
@x@c0296c4
@x@c@296c6
@x@c@296c8
@x@cO@296ca
e1
e1
e1
@2
e1
e1
e1
e1
e1
04
e1
e1
04
e1
e1
@2
e1
e2
e2
e1
04
e1
e1
e2
e1
e1
e2
@2
e1
e1
e1
e1
e1
e1
e3
e1
e1
e1
e1
e1
e1
e1
@2
e1
@2
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
298
291
292
293
294
295
296
297
298
299
300
301
302
303
304
305
306
307
308
309
310
311
312
313
314
315
@x@c@296cc
@x@c029696
@x0c@29698
@x@c0296c4
@x@c0296c6
@x@c0296c8
Qx@cO296ca
@x@cO296cc
@x@c029696
@x0c@29698
@x@c0296c4
Qx@c0296c6
@x@c0296c8
@x@c@296ca
@x@c0296cc
@x0c@29696
Qx@c029698
@x@c@296c4
@x@c0296c6
Qx@c0296c8
@x@c0296ca
@x@c@296cc
@x0c@29696
@x0c@29698
@x@c0296c4
@x@c0296c6
@x@c0296c8
@x@cO296ca
@x@cO296cc
@x@c029696
@x0c@29698
@x@c0296c4
Qx@c0296c6
@x@c0296c8
@x@c@296ca
@x@cO296cc
@x0c@29696
Qx@c029698
@x@c0296c4
@x@c0296c6
Qx@c0296c8
@x@c0296ca
@x@c@296cc
@x0c@29696
@x@c029698
e1
e1
e1
Q1
e2
e1
e2
e1
e1
e1
e1
e2
e1
e2
e1
e1
Q1
e1
e2
Q1
e2
e1
e1
e1
Q1
e2
e1
e2
e1
Q1
e1
e1
e2
e1
e2
e1
e1
Q1
e1
e2
Q1
e2
e1
e1
e1
316
317
318
319
320
321
322
323
324
325
326
327
328
329
330
331
332
333
334
335
336
337
338
339
340
341
342
343
344
345
346
347
348
349
350
351
352
353
354
355
356
357
358
359
360
@x@c0296c4
@x@c0296c6
@x@c0296c8
Q@x@c@296ca
@x@c@296cc
@x@c029696
Qx@c029698
@x@c0296c4
@x@c0296c6
@x@c0296c8
@x@c@296ca
@x@c@296cc
Q@x@c029696
Qx@c029698
@x@c0296c4
@x@c0296c6
Qx@c0296c8
@x@cO296ca
@x@cO296cc
@x@c029696
@x@c029698
Qx@c0296c4
@x@c@296c6
@x@c0296c8
Qx@c0296ca
@x@cO296cc
@x@c029696
Qx@c029698
@x@c0296c4
@x@c0296c6
@x@c0296c8
@x@c@296ca
@x@cO296cc
@x@c@29696
@x@c029698
@x@c0296c4
@x@c0296c6
Qx@c0296c8
@x@cO296ca
@x@cO296cc
@x@c029696
@x@c029698
Qx@c0296c4
@x@c@296c6
@x@c0296c8
e1
@2
e1
@2
e1
e1
e1
e1
@2
e1
e2
e1
e1
e1
e1
e2
e1
@2
e1
e1
e1
e1
e2
e1
e2
e1
e1
e1
e1
@2
e1
e2
e1
e1
e1
e1
e2
e1
@2
e1
e1
e1
e1
@2
e1
361
362
363
364
365
366
367
368
369
370
371
372
373
374
375
376
377
378
379
380
381
382
383
384
385
386
387
388
389
390
391
392
393
394
395
396
397
398
399
400
401
402
403
404
405
@x@c0296ca
@x@cO296cc
@x0c029696
Qx@c029698
@x@c0296c4
@x@c0296c6
@x@c0296c8
@x@c0296ca
@x@cO296cc
Qx@c029696
@x@c029698
@x@cO2969c
@x@c0296a0
@x@c0296a2
@x@c0296a4
@x@c0296a6
@x@c0296aa
@x@cO296ae
@x@c02c304
@x@c02c306
Qx@c02c308
@x@cO2c31c
@x@c02c320
@x@c02c322
@x@c02c324
Qx@c02c326
@x@c@2d102
@x@c02d104
@x@c02d106
@x@c02d1e8
@x0c@2d10a
@x@c02d110
@x@c02d114
@x@c02d118
@x@c@2d11¢
@x@c@2d120
@x@c0@2d124
@x@c02d128
@x@c@2d12a
@x@c@2d12e
@x@c@2d132
@x0@c02d134
@x@c02d138
@x0c@2d10a
@x@c@2d10e
e2
e1
e1
e1
e1
@2
e1
@2
e1
e1
e1
e1
e1
e1
e1
e1
e1
04
e2
@2
e1
Q2
e1
Q2
e2
e1
3
e1
e1
e1
e1
@2
e2
e1
e1
e1
e1
e1
@2
e1
e1
e1
e1
e1
e4
```

## Slide 211

**Raw Trace**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
O©ANDUAWNHR
@x@c@24dd6
OxArArhata
ext
@xt
@xt
@xt
ext
oxé
ext
@xt
@x'
@x
@x
ex
xt
ext
@x
@x
ex
@x'
xt
@x0c@2c410
@x@c@2c412
@x@c@2c414
@x@c@2c416
@x@c@2c41a
@x@c@2c41c
@x@c@2c41e
@x@c@2c422
@x@c@2c426
@x@c@2c428
@x@c@2c42a
@x@c@2c42c
@x@c@2c3ce
@x0c@2c3d2
@x@c@2c36c
@x@c@2c370
@x@c@2c374
@x@c@2c378
@x@c@2c37a
@x@c@2c37e
@x@c@2c380
@x@c@2c382
@x@c@2c384
e1
ar
@2
e1
e1
e1
e1
e1
@2
@2
e1
e1
@2
e1
e1
e1
@3
@2
@2
e1
e1
e1
Q1
e1
e1
46
Ay
68
69
78
71
72
73
74
75
76
77
78
79
88
81
82
83
84
85
86
87
88
89
98
Qxc@2c388
AVArAIe AA
@x@c@2c398
Qx@c@2c39a
@x0c@2c39c
Ox@c@2c2cc
@x@c@2c2de
@x@c@2c2d2
@x@c@2c2d4
@x@c@2c2d6
@x@c02c2d8
Qx@c@2c334
@x0c@2c338
@x@c@2c33c
@x0c0@2c340
@x@c@2c346
Qx@c@2c348
@x@cO@2c2dc
@x@c@2c2de
@x@c@2be38
@x@c@2be3c
@x@c@2be3e
@x@c@2be40
O@x@cO2be42
@x@c@2be4c
e1
a1
e1
e1
e1
Q3
e1
e1
e1
e2
e1
e2
e1
e2
e1
@2
e1
e1
e1
e1
e1
3
e1
e1
e2
91
a?
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
@x@c@2be4e
AvAcrAMhaACA
@x@c@1fi1le
@x@ce1f12a
@x0c01F122
@x0ce1f124
Qx0c01F138
@x0c01F13c
@x0c01F140
Qx0c01F148
@x@c01f14a
@x0ce1F14c
@x@c01F150
@x0ce01f154
@x@c01f18e
@x@c01F192
@x0c01F196
@x0@c01F198
@x0c01F19c
@x@c01f19e
@x@c01f1a2
@x@ce1f1a4
@x@c01f1a6
@x@c01filaa
@x@c01flae
Q1
e1
e1
e1
e1
e2
136
137
138
139
140
141
142
143
144
145
146
147
148
149
158
151
152
153
154
155
156
157
180
@x@c01Ff1b2
@x0c01Ff1b4
@xO@c01F1b6
@x@c@1fiba
@xOc@1fice
@x0c0@1f1be
@x0c@1F1cO
@x0c@1f1c2
@x@c@1f1c4
@x0c@1f1c6
@x0cO@1F1c8
@xOc@1ficc
@x0@c01F166
@x0c01F168
@x0c@1f16c
@x0c0@1f16e
@x@c@1f17a
@x0c@1F17¢
@x@c@1f17e
@x0c01F180
@x@c@1F182
@x@cO2952c
@x@c02952e
@x@c@2955e
Q1
@2
@3
e1
@2
@2
e1
@2
e1
@2
@3
@1
Q1
@3
@2
Q1
e1
Q1
e1
Q1
e1
Q1
OL
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
225
@x@c@29560
Qx0c@29562
@x0@c@29542
@x@c@2955e
@x0c@29560
@x@c@29562
Qx0c@29542
@x@c@2955e
@x0c@29560
@x0c@29562
@x@c@29542
@x@c@2955e
@x0@c0@29560
Qx0c@29562
@x0@c@29542
@x@c@2955e
@x0c@29560
@x@c@29562
Qx0c@29542
@x@c@2955e
@x0c@29560
@x0@c@29562
@x@c@29542
@x0@c@29560
e@2
e1
e1
e1
2
e1
e1
e1
e2
e1
e1
e1
e@2
e1
e1
e1
2
e1
e1
Q1
e2
e1
@2
270
@x@c@29562 01
@x0c@29542 01
@x@c@2955e 01
@x@c@29560 02
i}
@
q
q
g
q
M,
@x@cO2c2FfO 02
Ox@c@2c2Ff2 O2
Ox@cO2c2F4 01
Ox@c@2c2f6 01
@x@cO2c2F8 O1
@x@c@2c2Ffc 01
@x0c@2c300 O1
@x@c02968e 01
@x@c@29698 @3
@x@c029692 01
@x@c@296be@ 01
@x@c@296b4 O1
@x@c029694 01
@x0c@29696 @1
@x@c029698 01
@x@c@296c4 O1
@x@c@296c6 82
@x@c@296c8 01
@x@c@296ca O2
296
297
298
299
300
301
302
303
304
305
306
307
308
309
310
311
312
313
314
315
@x@cO296cc
@x@c@29696
Qx@c029698
@x@c0296c4
@x@c0296c6
@x@c0296c8
@x@cO296ca
@x@cO296cc
@x@c029696
@x0c@29698
@x@c0296c4
Qx@c0296c6
@x@c0296c8
@x@c@296ca
@x@c@296cc
@x0c@29696
Qx@c029698
@x@c0296c4
@x@c0296c6
Qx@c0296c8
@x@c0296ca
@x@c@296cc
@x0c@29696
@x@c029698
e1
e1
e1
Q1
316
317
318
319
341
342
343
344
345
346
347
348
349
350
351
352
353
354
355
356
357
358
359
360
@x@cO296cc
@x@c0296c4
@x@c@296c6
@x@c0296c8
Q@x@c@296ca
@x@c029696
Qx@c029698
@x@c0296c4
@x@c0296c6
@x@c0296c8
@x@c@296ca
@x@cO296cc
@x@c@29696
@x@c029698
@x@c@296c4
@x@c0296c6
Qx@c0296c8
@x@cO296ca
@x@cO296cc
@x@c029696
@x@c029698
Qx@c0296c4
@x@c@296c6
@x@c0296c8
e1
@2
e1
@2
e1
e1
e1
e1
@2
e1
e2
e1
e1
e1
e1
e2
e1
@2
e1
e1
e1
e1
@2
e1
361
362
363
364
386
387
388
389
398
391
392
393
394
395
396
397
398
399
400
401
402
403
404
405
@x@c0296ca
@x@cO296cc
@x0c029696
Q@x@c029698
Qx@c02c326
@x@c@2d102
@x@c02d104
@x@c02d106
@x@c02d1e8
@x0c@2d10a
@x@c02d110
@x@c02d114
@x@c02d118
@x@c@2d11¢
@x@c@2d120
@x@c0@2d124
@x@c02d128
@x@c@2d12a
@x@c@2d12e
@x@c@2d132
@x0@c02d134
@x@c02d138
@x0c@2d10a
@x@c@2d10e
```

## Slide 212

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
18
19
20
21
22
23
@x0c@2b84a 01
Q@x@c@2b84c O1
@x@c@2c406 3
@x@c@2c408 01
@xO@c@2c40c @1
@x0c@2c410 @2
@xO@c@2b84a
@xO@c@2b84c
@x6c@2c466
@x6c62c468
@x6c62c46c
@xOce@2c410
```

## Slide 213

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
18
19
20
21
22
23
@x0c@2b84a
@x0c@2b84c
@x@c@2c406
@x@c@2c408
@x@c@2c40c
@x0@c@2c410
e1
e1
@3
e1
e1
@2
20
Ox@cO2c486 83
```

## Slide 214

###### **Program Counter of the Instruction**

**Raw Trace**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
18
19
20
21
22
23
@x0c@2b84a 01
Q@x@c@2b84c O1
@x@c@2c406 3
@x@c@2c408 01
@xO@c@2c40c @1
@x0c@2c410 @2
@x6c@2c466
Program Counter of the Instruction
```

## Slide 215

###### **Program Counter of the Instruction**

##### **Raw Trace**

###### **Interrupt Latency**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
18
19
20
21
22
23
@x0c@2b84a 01
Q@x@c@2b84c O1
@x@c@2c406 3
@x@c@2c408 01
@xO@c@2c40c @1
@x0c@2c410 @2
@x6c@2c466
Program Counter of the Instruction
Interrupt Latency
```

## Slide 216

**Mstp-Visualizer**

## Slide 217

M-Step Visualizer (GTKwave)

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Time
clk=0
cycle[31:0] =1
Instructior
instr_addr[31:0] =0!
inst_raw=c|
inst_full =c|
M-Step Visualizer (GI Kwave)
—— 1
(ices id i |
TEV E Mt fm_arch threads]
i) (oe000087 ) if
A ER tfm_arch thread fn_catt
he a cca
```

## Slide 218

###### M-Step Visualizer (GTKwave)

v

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
4676 ns 4690 ns
Time
clk =6
cycle[31:0] =2
structio
instr_addr[31:0] =@) [Ogee yD erp Clee leer nes
inst_raw=Li EXC Co Cl is ce?
CMRMMESIEM adds 6, 2, r3 \cmp r2, #3 \subs r?, r6, r2 \str r4, [r7, #0]
func =t
inst_len[31: O] ERE \ooaonon2
```

## Slide 219

###### M-Step Visualizer (GTKwave)

**Program Counter of the Instruction**

v

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
M-Step Visualizer (GI Kwave)
Time
clk=0
cycle[31:0] =1' j
Instruction
Wa Pe eee 10, ve TT es ee 2 ee
Program Counter of the Instruction
inst _raw=Li Ete
st_fu ro a or os
nc =t) a ec cc
a a
(a
```

## Slide 220

###### M-Step Visualizer (GTKwave)

**Program Counter of the Instruction**

v

**Interrupt Latency**

## Slide 221

###### M-Step Visualizer (GTKwave)

v
Debug Symbols

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
M-Step Visualizer (GI Kwave)
inst_full =. ré, r2, r3 icmp r2, #3 subs r7, r6, r2_ {str ré
func =t [Sm I I I }
```

## Slide 222

M-Step Visualizer (GTKwave)

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
M-Step Visualizer (GI Kwave)
Time
clk=0 |
cycle[31:0] =1!
Instruction
Za78 ns Tee ns 7E90 ns
ime
clk =6
cycle[31:0] =2
Instructto
instr_addr[31:0] =0)
oot 1) ae
```

## Slide 223

M-Step Visualizer (GTKwave)

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
M-Step Visualizer (GI Kwave)
Time
clk=0
cycle[31:0] =1!
Instruction
Time
clk =6
cycle[31:0] =2
tructio
instr_addr[31:0]=8:
inst_raw=l
inst_full =Li EXRER GC ee cece str r4, [r/, #0]
func =t [Sms } } memset
```

## Slide 224

M-Step Visualizer (GTKwave)

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
M-Step Visualizer (GI Kwave)
Time
cycle[31:0] =1!
Instruction es es : | _
— TT) 7670 1s
ime
clk=0
cycle[31:0]=2 Bg a >:
Instructio
instr_addr[31:0]=0: Eee ‘OCO2ED96 ‘OCO2SDB2 acezEDB4
inst_raw=1 EEE as TS
inst_full =L) ERRERRS I ee ee subs r7, ro, rz:
func =t TERR memset == memset:
```

## Slide 225

Target Board

**Host PC**

## Slide 226

Step

**Target Board**

**Host PC**

## Slide 227

Step
Target Board
Trace

Host PC

## Slide 228

Step
Target Board
Trace
Host PC
4 MHZ

## Slide 229

Step
Target Board
Trace
Host PC
4 MHZ

## Slide 230

**Mstp-Debug & Mstp-Emulator**

## Slide 231

Trace

**Target Board**

**Host PC**

## Slide 232

Trace
Target Board

###### **Host PC**

## Slide 233

**Host PC**

## Slide 234

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
/home/cris/Documents/0_Projects/jo-collab/copilot/build/nucleo_1552ze_q_mstp_s/lib/ext/cmsis-src/CMSIS/Core/Include/m-profile/cmsis_gcc_m.h
[ No Source Available ]
[ No Assembly Available ]
lextended-r Thread 1 In: Reset_Handler L893 PC: Oxc018e70
(gdb) ||
[M-Step-DeO:bash*Z 1:fish- 2:fish ",/1-gdb-py.sh -s exp " 12:47 18-jun-25
```

## Slide 235

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
/home/cris/Documents/0_Projects/jo-collab/copilot/build/nucleo_1552ze_q_mstp_s/lib/ext/cmsis-src/CMSIS/Core/Include/m-profile/cmsis_gcc_m.h
[ No Source Available ]
lextended-r Thread 1 In: Reset_Handler
[ No Assembly Available ]
(gdb) b *0x0c028868
Breakpoint 1 at 0xc028868: file /home/cris/Documents/0_Projects/jo-collab/m-step/mstp-victims/s/src/victims.c, line 6.
(gab) []
[M-Step-DeO:bash*Z 1:fish- 2:fish
L893 PC: Oxc018e70
",/1-gdb-py.sh -s exp " 12:48 18-jun-25|
```

## Slide 236

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
/home/cris/Documents/0_Projects/jo-collab/m-step/mstp-victims/s/src/victims.c
1 #include "victims.h"
2
3 #define STRING "M-Step-S\r\n"
4
5 void victim_printf_inst(){
EMMA print (STRING) |
7}
8
9 void victim_strlen_inst(){
10 =strlen(STRING);
11 }
12
cEesOxXcO28868 <victim_printf_inst> ro, [pc, #4] @ (OxcO28870 <victim_printf_inst+8>)
0xc02886a <victim_printf_inst+2> b.w OxcO28e8c <printf>
O0xcO2886e <victim_printf_inst+6> nop
0xc028870 <victim_printf_inst+8> asrs ri, r6, #29
0xc028872 <victim_printf_inst+10> lsrs r3, rO, #16
0xc028874 <victim_strlen_inst> ldr r@, [pce, #4] @ (0xcO2887c <victim_strlen_inst+8>)
0xc028876 <victim_strlen_inst+2> b.w OxcO2fbce <strlen>
0xc02887a <victim_strlen_inst+6> nop
0xc02887c <victim_strlen_inst+8> asrs r1, r6, #29
O0xc02887e <victim_strlen_inst+10> lsrs r3, rO, #16
0xc028880 <QCBOREncode_EncodeHead> stmdb sp!, {r0, r1, r2, r4, r5, r6, 77, r8, 79, Ur}
0xcO28884 <QCBOREncode_EncodeHead+4> add r4, sp, #8
0xcO28886 <QCBOREncode_EncodeHead+6> stmdb 4, {ri, r2}
lextended-r Thread 1 In: victim_printf_inst
(gdb) b *0x0c028868
Breakpoint 1 at 0xc028868: file /home/cris/Documents/0_Projects/jo-collab/m-step/mstp-victims/s/src/victims.c, line 6.
(gdb) c
Continuing.
Breakpoint 1, victim_printf_inst () at /home/cris/Documents/0_Projects/jo-collab/m-step/mstp-victims/s/src/victims.c:6
[Trace Info] PC=0x0C028868 | 7 clk
(gdb) []
L6é PC: 0xc028868
[M-Step-DeO:bash*Z 1:fish- 2:fish
",/1-gdb-py.sh -s exp " 12:49 18-jun-25|
```

## Slide 237

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
/home/cris/Documents/0_Projects/jo-collab/m-step/mstp-victims/s/src/victims.c
1 #include "victims.h"
#define STRING "M-Step-S\r\n"
void victim_printf_inst(){
2
“
4
5
REMY prints (STRING) |
7}
8
9
void victim_strlen_inst(){
10 =strlen(STRING);
11 }
12
B+ 0xc028868 <victim_printf_inst> ldr rd, [pc, #4] @ (OxcO28870 <victim_printf_inst+8>)
moxc02886a_<Victim_printf_inst+2> | b.w _0xc028e8e_<printf>|
O0xcO2886e <victim_printf_inst+6> nop
0xc028870 <victim_printf_inst+8> asrs ri, r6, #29
0xc028872 <victim_printf_inst+10> lsrs r3, rO, #16
0xc028874 <victim_strlen_inst> ldr r@, [pce, #4] @ (0xcO2887c <victim_strlen_inst+8>)
0xc028876 <victim_strlen_inst+2> b.w OxcO2fbce <strlen>
0xc02887a <victim_strlen_inst+6> nop
0xc02887c <victim_strlen_inst+8> asrs r1, r6, #29
O0xc02887e <victim_strlen_inst+10> lsrs r3, rO, #16
0xc028880 <QCBOREncode_EncodeHead> stmdb sp!, {r0, r1, r2, r4, r5, r6, 77, r8, 79, Ur}
0xcO28884 <QCBOREncode_EncodeHead+4> add r4, sp, #8
0xcO28886 <QCBOREncode_EncodeHead+6> stmdb 4, {ri, r2}
lextended-r Thread 1 In: victim_printf_inst
(gdb) b *0x0c028868
Breakpoint 1 at 0xc028868: file /home/cris/Documents/0_Projects/jo-collab/m-step/mstp-victims/s/src/victims.c, line 6.
(gdb) c
Continuing.
Breakpoint 1, victim_printf_inst () at /home/cris/Documents/0_Projects/jo-collab/m-step/mstp-victims/s/src/victims.c:6
[Trace Info] PC=0x0C028868 | 7 clk
(gdb) ni
[Trace Info] PC=0x0C02886A | 1 clk
(gdb) []
L6 PC: Oxc02886a
[M-Step-DeO:bash*Z 1:fish- 2:fish
",/1-gdb-py.sh -s exp " 12:50 18-jun-25|
```

## Slide 238

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
/home/cris/Documents/0_Projects/jo-collab/m-step/mstp-victims/s/src/victims.c
1 #include "victims.h"
2
3 #define STRING "M-Step-S\r\n"
4
5 void victim_printf_inst(){
B+> 6 printf (STRING) ;
8
9 void victim_strlen_inst(){
10 =strlen(STRING);
11 }
12
B+ 0xc028868 <victim_printf_inst> ldr rd, [pc, #4] @ (OxcO28870 <victim_printf_inst+8>)
B0xc02886a <victim_printf_inst+2> OxcO28e8c <printf>
O0xcO2886e <victim_printf_inst+6> nop
0xc028870 <victim_printf_inst+8> asrs ri, r6, #29
0xc028872 <victim_printf_inst+10> lsrs r3, rO, #16
0xc028874 <victim_strlen_inst> ldr rd, [pc, #4] @ (OxcO2887c <victim_strlen_inst+8>)
0xc028876 <victim_strlen_inst+2> b.w OxcO2fbce <strlen>
0xc02887a <victim_strlen_inst+6> nop
0xc02887c <victim_strlen_inst+8> asrs ri, r6, #29
O0xc02887e <victim_strlen_inst+10> lsrs r3, rO, #16
0xc028880 <QCBOREncode_EncodeHead> stmdb sp!, {r0, r1, r2, r4, r5, r6, 77, r8, 79, Ur}
0xcO28884 <QCBOREncode_EncodeHead+4> add r4, sp, #8
0xcO28886 <QCBOREncode_EncodeHead+6> stmdb 4, {ri, r2}
lextended-r Thread 1 In: victim_printf_inst L6é PC: Oxc02886a
(gdb) b *0x0c028868
Breakpoint 1 at 0xc028868: file /home/cris/Documents/0_Projects/jo-collab/m-step/mstp-victims/s/src/victims.c, line 6.
(gdb) c
Continuing.
Brealnoin Loti m opin ip at /home/cris/Documents/0_Projects/jo-collab/m-step/mstp-victims/s/src/victims.c:6
[Trace Info] PC=0x0C028868 | 7 clk
(gdb) ni
[Trace Info] PC=0x0C02886A | 1 clk
(gdb) []
[M-Step-DeO:bash*xZ 1:fish- 2:fish ",/1-gdb-py.sh -s exp " 12:50 18-jun-25
```

## Slide 239

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
/home/cris/Documents/0_Projects/jo-collab/tf-m/trusted-firmware-m/secure_fw/partitions/lib/runtime/tfm_sp_log_raw.c:
165 int printf(const char *fmt, ...)
166 {
167 int count = 0;
168 va_list ap;
169
> 170 va_start(ap, fmt);
171 count = vprintf(fmt, ap);
172 va_end(ap);
173
174 return count;
175 }
psOxcO28e8c <printf> {rO, ri, r2, r3}
OxcO28e8e <printf+2> push {rO, ri, r2, Ur}
OxcO28e90 <printf+4> add ri, sp, #16
OxcO28e92 <printf+6> ldr.w rd, [ri], #4
OxcO28e96 <printf+10> str ri, [sp, #4]
OxcO28e98 <printf+12> bl Oxc01e848 <vprintf>
OxcO28e9c <printf+16> add sp, #12
OxcO28e9e <printf+18> ldr.w Ur, [sp], #4
OxcO28ea2 <printf+22> add sp, #16
OxcO28ea4 <printf+24> bx lr
OxcO28ea6 <tfm_output_unpriv_string> svc 2
OxcO28ea8 <tfm_output_unpriv_string+2> bx lr
OxcO28eaa <tfm_hal_output_sp_log> b.w OxcO28ea6 <tfm_output_unpriv_string>
lextended-r Thread 1 In: printf
(gdb) b *0x0c028868
Breakpoint 1 at 0xc028868: file /home/cris/Documents/0_Projects/jo-collab/m-step/mstp-victims/s/src/victims.c, line 6.
(gdb) c
Continuing.
at /home/cris/Documents/0_Projects/jo-collab/m-step/mstp-victims/s/src/victims.c:6
[Trace Info] PC=0x0C028868 | 7 clk
(gdb) ni
[Trace Info] PC=0x0CO2886A | 1 clk
printf (fmt=0x0) at /home/cris/Documnts/0_Projects/jo-collab/tf-m/trusted-firmware-m/secure_fw/partitions/Lib/runtime/tfm_sp_log_raw.c:170
[Trace Info] PC=0x0CO28E8C | 3 clk
(gdb) []
L170 PC: OxcO28e8c
[M-Step-DeO:bash*Z 1:fish- 2:fish
",/1-gdb-py.sh -s exp " 12:50 18-jun-25}
```

## Slide 240

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
/home/cris/Documents/0_Projects/jo-collab/tf-m/trusted-firmware-m/secure_fw/partitions/lib/runtime/tfm_sp_log_raw.c:
165 int printf(const char *fmt, ...)
166 {
167 int count = 0;
168 va_list ap;
169
> 170 va_start(ap, fmt);
171 count = vprintf(fmt, ap);
172 va_end(ap);
173
174 return count;
175 }
OxcO28e8c <printf> push {rO, ri, r2, r3}
BoxcO28e8e <printf+2> push fro, rd, 2, ir}
OxcO28e90 <printf+4> add ri, sp, #16
OxcO28e92 <printf+6> ldr.w rd, [ri], #4
OxcO28e96 <printf+10> str ri, [sp, #4]
OxcO28e98 <printf+12> bl Oxc01e848 <vprintf>
OxcO28e9c <printf+16> add sp, #12
OxcO28e9e <printf+18> ldr.w Ur, [sp], #4
OxcO28ea2 <printf+22> add sp, #16
OxcO28ea4 <printf+24> bx lr
OxcO28ea6 <tfm_output_unpriv_string> svc 2
OxcO28ea8 <tfm_output_unpriv_string+2> bx lr
OxcO28eaa <tfm_hal_output_sp_log> b.w OxcO28ea6 <tfm_output_unpriv_string>
lextended-r Thread 1 In: printf
(gdb) b *0x0c028868
Breakpoint 1 at 0xc028868: file /home/cris/Documents/0_Projects/jo-collab/m-step/mstp-victims/s/src/victims.c, line 6.
(gdb) c
Continuing.
at /home/cris/Documents/0_Projects/jo-collab/m-step/mstp-victims/s/src/victims.c:6
[Trace Info] PC=0x0C028868 | 7 clk
(gdb) ni
[Trace Info] PC=0x0CO2886A | 1 clk
printf (fmt=0x0) at /home/cris/Documnts/0_Projects/jo-collab/tf-m/trusted-firmware-m/secure_fw/partitions/Lib/runtime/tfm_sp_log_raw.c:170
[Trace Info] PC=0x0CO28E8C | 3 clk
[Trace Info] PC=0x0CO28E8E | 3 clk
L170 PC: OxcO28e8e
[M-Step-DeO:bash*Z 1:fish- 2:fish
",/1-gdb-py.sh -s exp " 12:50 18-jun-25}
```

## Slide 241

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
/home/cris/Documents/0_Projects/jo-collab/tf-m/trusted-firmware-m/secure_fw/partitions/lib/runtime/tfm_sp_log_raw.c:
165 int printf(const char *fmt, ...)
> 166
167 int count = 0;
168 va_list ap;
169
170 va_start(ap, fmt);
171 count = vprintf(fmt, ap);
172 va_end(ap);
173
174 return count;
175 }
OxcO28e8c <printf> push {rO, ri, r2, r3}
OxcO28e8e <printf+2> push {r0, ri, r2, Ur}
Boxcd28e90 <printf+4> add rd sp, #16
OxcO28e92 <printf+6> ldr.w rd, [ri], #4
OxcO28e96 <printf+10> str ri, [sp, #4]
OxcO28e98 <printf+12> bl Oxc01e848 <vprintf>
OxcO28e9c <printf+16> add sp, #12
OxcO28e9e <printf+18> ldr.w Ur, [sp], #4
OxcO28ea2 <printf+22> add sp, #16
OxcO28ea4 <printf+24> bx lr
OxcO28ea6 <tfm_output_unpriv_string> svc 2
OxcO28ea8 <tfm_output_unpriv_string+2> bx lr
OxcO28eaa <tfm_hal_output_sp_log> b.w OxcO28ea6 <tfm_output_unpriv_string>
lextended-r Thread 1 In: printf
(gdb) b *0x0c028868
Breakpoint 1 at 0xc028868: file /home/cris/Documents/0_Projects/jo-collab/m-step/mstp-victims/s/src/victims.c, line 6.
(gdb) c
Continuing.
[Trace Info] PC=0x0C028868 | 7 clk
(gdb) ni
[Trace Info] PC=0x0CO2886A | 1 clk
[Trace Info] PC=0x0CO28E8C | 3 clk
[Trace Info] PC=0x@CO28E8E | 3 clk
[Trace Info] PC=0x0CO28E90 | 1 clk
(gdb) []
at /home/cris/Documents/0_Projects/jo-collab/m-step/mstp-victims/s/src/victims.c:6
printf (fmt=0x0) at /home/cris/Documnts/0_Projects/jo-collab/tf-m/trusted-firmware-m/secure_fw/partitions/Lib/runtime/tfm_sp_log_raw.c:170
L166 PC: Oxc028e90
[M-Step-DeO:bash*Z 1:fish- 2:fish
",/1-gdb-py.sh -s exp " 12:51 18-jun-25
```

## Slide 242

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
/home/cris/Documents/0_Projects/jo-collab/tf-m/trusted-firmware-m/secure_fw/partitions/lib/runtime/tfm_sp_log_raw.c:
165 int printf(const char *fmt,
> 166
167 int count = 0;
168 va_list ap;
169
170 va_start(ap, fmt);
171 count = vprintf(fmt, ap);
172 va_end(ap);
173
174 return count;
175 }
OxcO28e8c <printf> push {rO, ri, r2, r3}
OxcO28e8e <printf+2> push {rO, ri, r2, Ur}
OxcO28e90 <printf+4> add ri, sp, #16
Boxc028e92 <printf+6> drew, [rd], a
OxcO28e96 <printf+10> str ri, [sp, #4]
OxcO28e98 <printf+12> bl Oxc01e848 <vprintf>
OxcO28e9c <printf+16> add sp, #12
OxcO28e9e <printf+18> ldr.w Ur, [sp], #4
OxcO28ea2 <printf+22> add sp, #16
OxcO28ea4 <printf+24> bx lr
OxcO28ea6 <tfm_output_unpriv_string> svc 2
OxcO28ea8 <tfm_output_unpriv_string+2> bx lr
OxcO28eaa <tfm_hal_output_sp_log> b.w OxcO28ea6 <tfm_output_unpriv_string>
lextended-r Thread 1 In: printf
(gdb) b *0x0c028868
Breakpoint 1 at 0xc028868: file /home/cris/Documents/0_Projects/jo-collab/m-step/mstp-victims/s/src/victims.c, line 6.
(gdb) c
Continuing.
(gdb) ni
Bros im pdb ip at /home/cris/Documents/0_Projects/jo-collab/m-step/mstp-victims/s/src/victims.c:6
[Trace Info] PC=0x0C028868 | 7 clk
Info] PC=0x0CO2886A | 1 clk
Info] PC=0xOCO28E8C | 3 clk
Info] PC=0xOCO28E8E | 3 clk
Info] PC=0x0CO28E90 | 1 clk
Info] PC=0xOCO28E92 | 2 clk
(fmt=0x0) at /home/cris/Documfnts/0_Projects/jo-collab/tf-m/trusted-firmware-m/secure_fw/partitions/lib/runtime/tfm_sp_log_raw.c:170
L166 PC: Oxc028e92
",/1-gdb-py.sh -s exp " 12:51 18-jun-25
```

## Slide 243

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
/home/cris/Documents/0_Projects/jo-collab/tf-m/trusted-firmware-m/secure_fw/partitions/lib/runtime/tfm_sp_log_raw.c:
165 int printf(const char *fmt,
166 {
167 int count = 0;
168 va_list ap;
169
> 170 va_start(ap, fmt);
171 count = vprintf(fmt, ap);
172 va_end(ap);
173
174 return count;
175 }
OxcO28e8c <printf> push {rO, ri, r2, r3}
OxcO28e8e <printf+2> push {rO, ri, r2, Ur}
OxcO28e90 <printf+4> add ri, sp, #16
OxcO28e92 <printf+6> ldr.w rd, [ri], #4
B0xc028e96 <printf+10> str rd, [sp #4]
OxcO28e98 <printf+12> bl Oxc01e848 <vprintf>
OxcO28e9c <printf+16> add sp, #12
OxcO28e9e <printf+18> ldr.w Ur, [sp], #4
OxcO28ea2 <printf+22> add sp, #16
OxcO28ea4 <printf+24> bx lr
OxcO28ea6 <tfm_output_unpriv_string> svc 2
OxcO28ea8 <tfm_output_unpriv_string+2> bx lr
OxcO28eaa <tfm_hal_output_sp_log> b.w OxcO28ea6 <tfm_output_unpriv_string>
lextended-r Thread 1 In: printf
Breakpoint 1 at 0xc028868: file /home/cris/Documents/0_Projects/jo-collab/m-step/mstp-victims/s/src/victims.c, line 6.
(gdb) c
Continuing.
t /home/cris/Documents/0_Projects/jo-collab/m-step/mstp-victims/s/src/victims.c:6
[Trace Info] PC=0x0C028868 | 7 clk
gdb) ni
Info] PC=0x0CO2886A | 1 clk
(fmt=0x0) at /home/cris/Docum§nts/0_Projects/jo-collab/tf-m/trusted-firmware-m/secure_fw/partitions/lib/runtime/tfm_sp_log_raw.c:170
Info] PC=0x0CO28E8C clk
Info] PC=0x0CO28E8E clk
Info] PC=0x0C028E90 clk
Info] PC=0x0C028E92 clk
Info] PC=0x0CO28E96 clk
L170 PC: Oxc028e96
",/1-gdb-py.sh -s exp " 12:51 18-jun-25
```

## Slide 244

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
/home/cris/Documents/0_Projects/jo-collab/tf-m/trusted-firmware-m/secure_fw/partitions/lib/runtime/tfm_sp_log_raw.c:
165 int printf(const char *fmt, ...)
166 {
167 int count = 0;
168 va_list ap;
169
170 va_start(ap, fmt);
> 171 count = vprintf(fmt, ap);
172 va_end(ap);
173
174 return count;
175 }
OxcO28e8c <printf> push {rO, ri, r2, r3}
OxcO28e8e <printf+2> push {rO, ri, r2, Ur}
OxcO28e90 <printf+4> add ri, sp, #16
OxcO28e92 <printf+6> ldr.w rd, [ri], #4
OxcO28e96 <printf+10> str ri, [sp, #4]
Boxc028e96 <printfe12> bl Oxc012848 <vprint >
OxcO28e9c <printf+16> add sp, #12
OxcO28e9e <printf+18> ldr.w Ur, [sp], #4
OxcO28ea2 <printf+22> add sp, #16
OxcO28ea4 <printf+24> bx lr
OxcO28ea6 <tfm_output_unpriv_string> svc 2
OxcO28ea8 <tfm_output_unpriv_string+2> bx lr
OxcO28eaa <tfm_hal_output_sp_log> b.w OxcO28ea6 <tfm_output_unpriv_string>
lextended-r Thread 1 In: printf
(gdb) c
Continuing.
[Trace Info] PC=0x0C028868 | 7 clk
(gdb) ni
Info] PC=0x0CO2886A | 1 clk
(fmt=0x0) at /home/cris/Docum§nts/0_Projects/jo-collab/tf-m/trusted-firmware-m/secure_fw/partitions/lib/runtime/tfm_sp_log_raw.c:170
Info] PC=0x0CO28E8C clk
Info] PC=0x0CO28E8E clk
Info] PC=0x0C028E90 clk
Info] PC=0x0CO28E92 clk
t /home/cris/Documents/0_Projects/jo-collab/m-step/mstp-victims/s/src/victims.c:6
Info] PC=0x0CO28E96 clk
PC=0x0CO28E98 clk
L171 PC: Oxc028e98
",/1-gdb-py.sh -s exp " 12:52 18-jun-25]
```

## Slide 245

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
/home/cris/Documents/0_Projects/jo-collab/tf-m/trusted-firmware-m/secure_fw/partitions/lib/runtime/tfm_sp_log_raw.c:
165 int printf(const char *fmt, ...)
166 {
167 int count = 0;
168 va_list ap;
169
170 va_start(ap, fmt);
171 count = vprintf(fmt, ap);
172 va_end(ap);
173
> 174 return count;
175 }
OxcO28e8c <printf> push {rO, ri, r2, r3}
OxcO28e8e <printf+2> push {rO, ri, r2, Ur}
OxcO28e90 <printf+4> add ri, sp, #16
OxcO28e92 <printf+6> ldr.w rd, [ri], #4
OxcO28e96 <printf+10> str ri, [sp, #4]
Oxc028e98 <printf+12> bl Oxc01e848 <vprintf>
Boxco28eve <printfrio> add sp, #1
OxcO28e9e <printf+18> ldr.w Ur, [sp], #4
OxcO28ea2 <printf+22> add sp, #16
OxcO28ea4 <printf+24> bx lr
OxcO28ea6 <tfm_output_unpriv_string> svc 2
OxcO28ea8 <tfm_output_unpriv_string+2> bx lr
OxcO28eaa <tfm_hal_output_sp_log> b.w OxcO28ea6 <tfm_output_unpriv_string>
lextended-r Thread 1 In: printf
Continuing.
Pnoalinoin Jt Di ip t /home/cris/Documents/0_Projects/jo-collab/m-step/mstp-victims/s/src/victims.c:6
[Trace Info] PC=0x0C028868 | 7 clk
(gdb) ni
Info] PC=0x0CO2886A | 1 clk
(#mt=0x0) at /home/cris/Docum§nts/0_Projects/jo-collab/tf-m/trusted-firmware-m/secure_fw/partitions/lib/runtime/tfm_sp_log_raw.c:170
Info] PC=0x0CO28E8C clk
Info] PC=0x0CO28E8E clk
Info] PC=0x0C028E90 clk
Info] PC=0x0C028E92 clk
Info] PC=0x0C028E96 clk
Info] PC=0x0CO28E98 clk
PC=0xOCO28E9C clk
L174 PC: OxcO28e9c
",/1-gdb-py.sh -s exp " 12:52 18-jun-25
```

## Slide 246

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
/home/cris/Documents/0_Projects/jo-collab/tf-m/trusted-firmware-m/secure_fw/partitions/lib/runtime/tfm_sp_log_raw.c:
165 int printf(const char *fmt, ...)
166 {
167 int count = 0;
168 va_list ap;
169
170 va_start(ap, fmt);
171 count = vprintf(fmt, ap);
172 va_end(ap);
173
> 174 return count;
175 }
OxcO28e8c <printf> push {rO, ri, r2, r3}
OxcO28e8e <printf+2> push {rO, ri, r2, Ur}
OxcO28e90 <printf+4> add ri, sp, #16
OxcO28e92 <printf+6> ldr.w rd, [ri], #4
OxcO28e96 <printf+10> str ri, [sp, #4]
OxcO28e98 <printf+12> bl Oxc01e848 <vprintf>
OxcO28e9c <printf+16> add sp, #12
eOxcO28e9e <printf+18> ldr.w  .r, [sp], #4
OxcO28ea2 <printf+22> add sp, #16
OxcO28ea4 <printf+24> bx lr
OxcO28ea6 <tfm_output_unpriv_string> svc 2
OxcO28ea8 <tfm_output_unpriv_string+2> bx lr
OxcO28eaa <tfm_hal_output_sp_log> b.w OxcO28ea6 <tfm_output_unpriv_string>
lextended-r Thread 1 In: printf
Rnealnoin Loti moni n ip at /home/cris/Documents/0_Projects/jo-collab/m-step/mstp-victims/s/src/victims.c:6
[Trace Info] PC=0x0C028868 | 7 clk
(gdb) ni
Info] PC=O0x0CO2886A | 1 clk
(fmt=0x0) at /home/cris/Docum§nts/0_Projects/jo-collab/tf-m/trusted-firmware-m/secure_fw/partitions/lib/runtime/tfm_sp_log_raw.c:170
Info] PC=0x0CO28E8C clk
Info] PC=0x0CO28E8E clk
Info] PC=0x0C028E90 clk
Info] PC=0x0C028E92 clk
Info] PC=0x0C028E96 clk
Info] PC=0x0CO28E98 clk
Info] PC=0x0CO28E9C clk
PC=0xOCO28E9E clk
L174 PC: OxcO28e9e
",/1-gdb-py.sh -s exp " 12:52 18-jun-25
```

## Slide 247

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
/home/cris/Documents/0_Projects/jo-collab/tf-m/trusted-firmware-m/secure_fw/partitions/lib/runtime/tfm_sp_log_raw.c:
165 int printf(const char *fmt, ...)
166 {
167 int count = 0;
168 va_list ap;
169
170 va_start(ap, fmt);
171 count = vprintf(fmt, ap);
172 va_end(ap);
173
> 174 return count;
175 }
OxcO28e8c <printf> push {rO, ri, r2, r3}
OxcO28e8e <printf+2> push {rO, ri, r2, Ur}
OxcO28e90 <printf+4> add ri, sp, #16
OxcO28e92 <printf+6> ldr.w rd, [ri], #4
OxcO28e96 <printf+10> str ri, [sp, #4]
OxcO28e98 <printf+12> bl Oxc01e848 <vprintf>
OxcO28e9c <printf+16> add sp, #12
OxcO28e9e <printf+18> ldr.w .r, [sp], #4
eOxcO028ea2 <printf+22> add sp, #16
OxcO28ea4 <printf+24> bx lr
OxcO28ea6 <tfm_output_unpriv_string> svc 2
OxcO28ea8 <tfm_output_unpriv_string+2> bx lr
OxcO28eaa <tfm_hal_output_sp_log> b.w OxcO28ea6 <tfm_output_unpriv_string>
t /home/cris/Documents/0_Projects/jo-collab/m-step/mstp-victims/s/src/victims.c:6
[Trace Info] PC=0x0C028868 | 7 clk
(gdb) ni
Info] PC=O0x0CO2886A | 1 clk
(#mt=0x0) at /home/cris/Docum§nts/0_Projects/jo-collab/tf-m/trusted-firmware-m/secure_fw/partitions/lib/runtime/tfm_sp_log_raw.c:170
Info] PC=0x0CO28E8C clk
Info] PC=0x0CO28E8E clk
Info] PC=0x0C028E90 clk
Info] PC=0x0CO28E92 clk
Info] PC=0x0C028E96 clk
Info] PC=0x0C028E98 clk
clk
clk
clk
w
Info] PC=0x0CO28E9C
Info] PC=0x0CO28E9E
PC=0xOCO28EA2
PNPRPNNRPW
",/1-gdb-py.sh -s exp " 12:52 18-jun-25
```

## Slide 248

###### M-Step Side-Channel Analysis

**Mstp-Nemesis**

**Mstp-BUSted**

Mstp-Cache

## Slide 249

###### **Mstp-Nemesis**

###### **Mstp-Cache**

###### **Mstp-Nemesis**

###### **Mstp-BUSted**

44

## Slide 250

###### **Data-Dependent Divisions**

**Cache Activity**

###### **Mstp-Cache**

###### **Differentiating Instructions**

###### **Mstp-Nemesis**

###### **Memory Access Activity**

###### **Mstp-BUSted**

44

## Slide 251

###### **Data-Dependent Divisions**

###### **Cache Activity**

###### **Mstp-Cache**

###### **Differentiating Instructions**

###### **Memory Access Activity**

###### **Mstp-BUSted**

44

## Slide 252

###### **Data-Dependent Divisions**

###### **Cache Activity**

###### **Differentiating Instructions**

###### **Memory Access Activity**

###### **Mstp-BUSted**

44

## Slide 253

###### **Data-Dependent Divisions**

###### **Cache Activity**

###### **Differentiating Instructions**

###### **Memory Access Activity**

44

## Slide 254

**M-Step Plugins**

## Slide 255

###### M-Step Plugins

**Side-Channel**

**Architectural**

**Framework**

## Slide 256

###### M-Step Plugins

**Side-Channel Mstp-Nemesis**

**Architectural**

**Framework**

**Mstp-Busted**

**Mstp-Cache**

## Slide 257

###### M-Step Plugins

**Side-Channel Mstp-Nemesis**

**Architectural**

**Framework**

**Mstp-Busted**

**Mstp-Zoom**

**Mstp-Cache**

## Slide 258

###### M-Step Plugins

**Side-Channel Mstp-Nemesis Mstp-Busted Mstp-Cache**

**Architectural Mstp-Zoom**

**Framework** **Mstp-Production Mstp-Debug Mstp-Metrics Mstp-Emulator Mstp-Visualizer Mstp-opDecoder Mstp-Test**

## Slide 259

###### M-Step Plugins

**Side-Channel Mstp-Nemesis**

**Mstp-Busted**

**Mstp-Cache**

**Architectural**

**Mstp-Zoom**

**Framework** **Mstp-Production Mstp-Debug Mstp-Metrics Mstp-Emulator Mstp-Visualizer Mstp-opDecoder Mstp-Test**

## Slide 260

BREAKING REAL SOFTWARE

## Slide 261

###### **Real World Use Case**

NON-SECURE WORLD TZ SECURE WORLD
Victi
TA Victim
m
SPY
TF-M
Cortex-M

49

## Slide 262

M-Step

###### **Real World Use Case**

NON-SECURE WORLD TZ SECURE WORLD
Victi
TA Victim
m
SPY
TF-M
Cortex-M

49

## Slide 263

###### **Real World Use Case**

M-Step
NON-SECURE WORLD TZ SECURE WORLD
Victi
TA Victim
m
SPY
TF-M
Cortex-M

49

## Slide 264

###### Real World Use Case

M-Step
NON-SECURE WORLD TZ SECURE WORLD
Victi
TA Victim
m
SPY
TF-M
Cortex-M

50

## Slide 265

###### Real World Use Case

M-Step
NON-SECURE WORLD TZ SECURE WORLD
Victi
TA Victim
m
SPY
TF-M
Cortex-M

50

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
[World Use Case
10
11
12
13
14
15
16
17
18
19
20
21
22
procedure Mbedtls_BEEA(x, A, B)
TU —A,TV <—B;
U1<—1,U2<—0,V1<—0,V2<—1;
while TU # 0 do
while TU even do
TU — TU/2;
if U1 or U2 odd then
| U1-—U1+TB;U2-—U2-TA
U1 —U1/2; U2 — U2/2;
while TV even do
TV —TV/2;
if V1 or V2 odd then
| V1 V1+TB, V2<—V2-TA;
V1 —V1/2; V2 — V2/2;
if TU > TV then
TU — TU -TV;
U1 <—U1-V1; U2 —U2-V2;
TU —TU/2;
TV —TV-TU;
V1—V1-U1;V2<—V2-U2:
TV —TV/2;
50
```

## Slide 266

###### Real World Use Case

M-Step
NON-SECURE WORLD TZ SECURE WORLD
Victi
TA Victim
m
SPY
TF-M
Cortex-M

50

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
[World Use Case
1 procedure Mbedtls_BEEA(Xx, A, B)
= 2 TU —A,TV <—B;
3s | Ule1,U2—0,V1i-0,v2-1,
rT 4 | while TU #0 do YPeN
— 5 while TU even do L |
6 TU —TU/2;
‘ 7 if U1 or U2 odd then
8 | U1<—U1+TB,U2<U2-TA
9 U1 — U1/2; U2 — U2/2;
10 while TV even do
11 TV —TV/2;
12 if V1 or V2 odd then
13 | V1 V1+TB, V2<—V2-TA;
14 V1 — V1/2; V2 —V2/2;
15 if TU > TV then
16 TU — TU -TV;
17 U1 — U1-V1;U2 —U2-V2;
18 TU —TU/2;
19 else
20 TV —TV-TU;
21 V1<—V1-U1;V2<—V2-U2;
22 TV —TV/2;
Sst
BRARY
50
```

## Slide 267

###### Real World Use Case

M-Step
NON-SECURE WORLD TZ SECURE WORLD
Victi
TA Victim
m
SPY
TF-M
Cortex-M

50

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
[World Use Case
1
2
3
4
} 5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
procedure Mbedtls_BEEA(X, A, B)
TU —A,TV — B;
while TU even do
TU — TU/2;
if U1 or U2 odd then
| U1-—U1+T7TB,U2<—U2-TA
U1 — U1/2; U2 — U2/2;
while TV even do
TV —TV/2;
if V1 or V2 odd then
| V1 V1+TB, V2<—V2-TA;
V1 — V1/2; V2 —V2/2;
if TU > TV then
TU —TU -TV;
U1 — U1-V1;U2 —U2-V2;
TU —TU/2;
else
TV —TV-TU;
V1 —V1-U1;V2<—V2-U2;
TV —TV/2;
U1<—1,U2—0,V1—0,V2—1; ) enSsl
while TU + 0 do
L |
BRARY
“
woli
50
```

## Slide 268

###### Real World Use Case

M-Step
NON-SECURE WORLD TZ SECURE WORLD
Victi
TA Victim
m
SPY
TF-M
Cortex-M

Libgcrypt

50

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
[World Use Case
10
11
12
13
14
15
16
17
18
19
20
21
22
procedure Mbedtls_BEEA(X, A, B)
TU —A,TV <—B;
U1<—1,U2<—0,V1<—0,V2<—1;
while TU # 0 do
while TU even do
TU —TU/2;
if U1 or U2 odd then
| U1-—U1+T7TB,U2<—U2-TA
U1 — U1/2; U2 — U2/2;
while TV even do
TV —TV/2;
if V1 or V2 odd then
| V1 V1+TB, V2<—V2-TA;
V1 — V1/2; V2 —V2/2;
if TU > TV then
TU —TU -TV;
U1 — U1-V1;U2 —U2-V2;
TU —TU/2;
else
TV —TV-TU;
V1—V1-U1;V2<—V2-U2:
TV —TV/2;
Openssl
BRARY
Libgcrypt
50
```

## Slide 269

###### Real World Use Case

|**M-Step**|||
|---|---|---|
|**NON-SECURE WORLD**
|**SECURE** **WORLD**
**Z**||
||**TA**
**Victi**
||
||**Victim**||
||**m**||
|**SPY**|||
||**TF-M**||
|**Cort**|**ex-M**|**Libgcrypt**|

50

## Slide 270

###### Real World Use Case

M-Step
NON-SECURE WORLD TZ SECURE WORLD
Victi
TA Victim
m
SPY
TF-M
Cortex-M

Libgcrypt

50

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
[World Use Case
10
11
12
13
14
15
16
17
18
19
20
21
22
procedure Mbedtls_BEEA(X, A, B)
TU —A,TV <—B;
U1<—1,U2<—0,V1<—0,V2<—1;
while TU # 0 do
while TU even do
TU —TU/2;
if U1 or U2 odd then
| U1-—U1+T7TB,U2<—U2-TA
U1 — U1/2; U2 — U2/2;
while TV even do
TV —TV/2;
if V1 or V2 odd then
| V1 V1+TB, V2<—V2-TA;
V1 — V1/2; V2 —V2/2;
if TU > TV then
TU —TU -TV;
U1 — U1-V1;U2 —U2-V2;
TU —TU/2;
else
TV —TV-TU;
V1—V1-U1;V2<—V2-U2:
TV —TV/2;
Openssl
BRARY
Libgcrypt
50
```

## Slide 271

###### Real World Use Case

M-Step
NON-SECURE WORLD TZ SECURE WORLD
Victi
TA Victim
m
SPY
TF-M
Cortex-M
Libgcrypt

Libgcrypt

50

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Real World Use Case
10
11
12
13
14
15
16
17
18
19
20
21
22
procedure Mbedtls_BEEA(X, A, B)
TU -—A,TV<—B;
U1<—1,U2<—0,V1<—0,V2<—1;
while TU # 0 do
while TU even do
TU — TU/2;
if U1 or U2 odd then
| U1<-—U1+TB,U2<-U2-TA
U1 — U1/2; U2 — U2/2;
while TV even do
TV —TV/2;
if V1 or V2 odd then
| V1 V1+TB,V2<—V2-TA;
V1 <— V1/2; V2 — V2/2;
if TU > TV then
TU —TU -TV;
U1 — U1-V1; U2 — U2-V2;
TU —TU/2;
else
TV —TV-TU;
V1—V1-U1;V2<—V2-U2;
TV —TV/2;
50
```

## Slide 272

###### BEEA Template Matrices

51

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
BEEA Template Matrices
10
11
12
13
14
15
16
17
18
19
20
21
22
procedure Mbedtls_BEEA(x, A, B)
TU —A,TV <— B;
U1<—1,U2<—0,V1<—0,V2<—1;
while TU # 0 do
while TU even do
TU — TU/2;
if U1 or U2 odd then
| U1 -—U1+T7TB;U2— U2-TA;
U1 — U1/2; U2 — U2/2;
while TV even do
TV —TV/2;
if V1 or V2 odd then
| Vic V1+TB,V2<—V2-TA;
V1<— V1/2; V2 <— V2/2;
if TU > TV then
TU —TU -TV;
U1 — U1-V1;U2< U2-V2;
TU —TU/2;
else
TV —TV-TU;
V1<—V1-U1;V2—V2-U2;
TV —TV/2;
u_if ee e | |
u_noif o ee
v_if eee | |
v_noif o ee a
) 2 4 6 8 138 140 142 144 146 148 150
Sample Index (samples 10-137 hidden)
SUB_U_1 ||
SUB_U_2 ||
SUB_U_3 |
SUB_U_4 | |
SUB_U_5
SUB_V_1 |
SUB_V_2 |
SUB_V_3 ||
0 5 10 15 20
Sample Index
51
```

## Slide 273

###### BEEA Template Matrices

51

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
BEEA Template Matrices
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
procedure Mbedtls_BEEA(x, A, B)
while TU even do
TU — TU/2;
if U1 or U2 odd then
| U1 -—U1+T7TB;U2— U2-TA;
U1 — U1/2; U2 — U2/2;
u_if ee e
u_noif o ee
51
```

## Slide 274

###### BEEA Template Matrices

51

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
BEEA Template Matrices
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
procedure Mbedtls_BEEA(x, A, B)
while /’V even do
TV —TV/2;
if V1 or V2 odd then
| Vic V1+TB,V2<—V2-TA;
V1 — V1/2; V2 — V2/2:
v_if
v_noif
138 140 142
Sample Index (samples 10-137 hidden)
144
146
148
51
150
```

## Slide 275

###### BEEA Template Matrices

51

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
BEEA Template Matrices
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
procedure Mbedtls_BEEA(x, A, B)
if TU > TV then
TU —TU -TV;
U1 — U1-V1;U2< U2-V2;
TU —TU/2;
SUB_U_1 ||
SUB.U.2 a
SUB_U_3
SUB_U_4 | |
SUB_U_5
51
```

## Slide 276

###### BEEA Template Matrices

51

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
BEEA Template Matrices
10
11
12
13
14
15
16
17
18
19
20
21
22
procedure Mbedtls_BEEA(x, A, B)
else
TV —TV-TU;
V1<—V1-U1;V2<— V2-U2;
TV —TV/2;
SUB_V_1
SUB_V_2
SUB_V_3
10
Sample Index
15
20
51
```

## Slide 277

###### BEEA Template Matrices

51

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
BEEA Template Matrices
10
11
12
13
14
15
16
17
18
19
20
21
22
procedure Mbedtls_BEEA(x, A, B)
TU —A,TV <— B;
U1<—1,U2<—0,V1<—0,V2<—1;
while TU # 0 do
while TU even do
TU — TU/2;
if U1 or U2 odd then
| U1 -—U1+T7TB;U2— U2-TA;
U1 — U1/2; U2 — U2/2;
while TV even do
TV —TV/2;
if V1 or V2 odd then
| Vic V1+TB,V2<—V2-TA;
V1<— V1/2; V2 <— V2/2;
if TU > TV then
TU —TU -TV;
U1 — U1-V1;U2< U2-V2;
TU —TU/2;
else
TV —TV-TU;
V1<—V1-U1;V2—V2-U2;
TV —TV/2;
u_if ee e | |
u_noif o ee
v_if eee | |
v_noif o ee a
) 2 4 6 8 138 140 142 144 146 148 150
Sample Index (samples 10-137 hidden)
SUB_U_1 ||
SUB_U_2 ||
SUB_U_3 |
SUB_U_4 | |
SUB_U_5
SUB_V_1 |
SUB_V_2 |
SUB_V_3 ||
0 5 10 15 20
Sample Index
51
```

## Slide 278

#### **End-to-end Attacks on Mbed TLS**

## Slide 279

###### **RSA Key Generation**

###### **RSA Decryption**

53

## Slide 280

###### **RSA Key Generation**

RSA TA
SPY
TF-M
Cortex-M
Memory

###### **RSA Decryption**

53

## Slide 281

###### **RSA Key Generation**

RSA TA
SPY 1
TF-M
Cortex-M
Memory

###### **RSA Decryption**

53

## Slide 282

###### **RSA Key Generation**

RSA TA
SPY 1
TF-M
Cortex-M
Memory

RSA Decryption

1 Request Public Key

53

## Slide 283

###### **RSA Key Generation**

RSA TA
SPY 1
2
TF-M
Cortex-M
Memory Key

###### **RSA Decryption**

1 Request Public Key

53

## Slide 284

###### **RSA Key Generation**

M-Step
3
RSA TA
SPY 1
2
TF-M
Cortex-M
Memory Key

RSA Decryption

1 Request Public Key

53

## Slide 285

###### **RSA Key Generation**

M-Step
3
RSA TA
SPY 1
2
TF-M
Cortex-M
Memory Key
1 Request Public Key

###### **RSA Decryption**

RSA TA
SPY
TF-M
Cortex-M
Memory Key

53

## Slide 286

###### **RSA Key Generation**

M-Step
3
RSA TA
SPY 1
2
TF-M
Cortex-M
Memory Key
1 Request Public Key

###### **RSA Decryption**

RSA TA
SPY 1
TF-M
Cortex-M
Memory Key

53

## Slide 287

###### **RSA Key Generation**

M-Step
3
RSA TA
SPY 1
2
TF-M
Cortex-M
Memory Key
1 Request Public Key

###### **RSA Decryption**

RSA TA
SPY 1
TF-M
Cortex-M
2
Memory Key

53

## Slide 288

###### **RSA Key Generation**

M-Step
3
RSA TA
SPY 1
2
TF-M
Cortex-M
Memory Key
1 Request Public Key

###### **RSA Decryption**

RSA TA
SPY 1
TF-M
Cortex-M
2
Memory Key

1 Request RSA Decryption

53

## Slide 289

###### **RSA Key Generation**

M-Step
3
RSA TA
SPY 1
2
TF-M
Cortex-M
Memory Key
1 Request Public Key

###### **RSA Decryption**

M-Step
3
RSA TA
SPY 1
TF-M
Cortex-M
2
Memory Key

1 Request RSA Decryption

53

## Slide 290

###### **Full Private Key Extraction**

M-Step
NON-SECURE WORLD TZ SECURE WORLD
Victi
TA Victim
m
SPY
TF-M
Cortex-M
Key

## Slide 291

###### **Full Private Key Extraction**

M-Step
NON-SECURE WORLD TZ SECURE WORLD
Victi
TA Victim
m
SPY
TF-M
Cortex-M
Key

## Slide 292

###### **Full Private Key Extraction**

M-Step
NON-SECURE WORLD TZ SECURE WORLD
Victi
TA Victim
m
SPY
TF-M
Cortex-M
Key

**100% Success Rate!**

## Slide 293

**Demo**

## Slide 294

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
wli/vhs on 9 exp/cli [x!?] via [ impure (tfm-dev-shell-env)
>» ./mstp.sfJ
```

## Slide 295

What Changes Now?

## Slide 296

What Changes Now?

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Ti \
Qs
y CUS
WE'RESCREWED
A SOUL oh
| [7] _ wer Ks
```

## Slide 297

###### **Constant time code**

###### **also matters on MCUs!**

###### **SW Developers**

## Slide 298

**HW Vendors**

**There is a need for secure-by-design solutions to prevent leakage!**

## Slide 299

**Single-stepping Attacks Should be Consider on The TZ-M Threat Model!**

**TEE / FW Providers**

## Slide 300

**Tiny chips…**

## Slide 301

**Tiny chips… no longer mean tiny leaks!**

## Slide 302

## **Thank You!**

**Cristiano Rodrigues, Sandro Pinto,** Marton Bognar, and Jo Van Bulck Centro ALGORITMI, University of Minho, DistriNet, KU Leuven

77

## Slide 303

## **Q&A**

**Cristiano Rodrigues, Sandro Pinto,** Marton Bognar, and Jo Van Bulck Centro ALGORITMI, University of Minho, DistriNet, KU Leuven

**mstep.eu**

**Github**

77
