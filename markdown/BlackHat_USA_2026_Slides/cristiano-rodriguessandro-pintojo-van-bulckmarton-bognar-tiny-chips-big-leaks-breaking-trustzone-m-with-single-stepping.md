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
text_chars: 60695
ocr_pages: 41
has_ocr: true
redacted_secrets: 6
ocr_confidence: 85.2
ocr_unreliable_blocks: 0
vision_verified_blocks: 7
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:34:20Z"
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

\```
[REDACTED:private-key-block]
\```

## Slide 7

\```
[REDACTED:private-key-block]
\```


> Recovered by OCR — confidence 78/100 on the text kept, 55/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
N RSA PRIVATE KEY-----
ee 10 RSA PRIVATE KEY-----
```

## Slide 8

\```
010111001101010101010100100111010101101011
\```

## Slide 9

\```
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
\```

## Slide 10

\```
[REDACTED:private-key-block]
\```

## Slide 11

\```
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
\```

## Slide 12

\```
[REDACTED:private-key-block]
\```

## Slide 13

[REDACTED:private-key-block]

## Slide 14

\```
[REDACTED:private-key-block]
\```

## Slide 15

## Slide 16

## Slide 17

## Slide 18

## Slide 19

## Slide 20

## Slide 21

## Slide 22

## Slide 23

## Slide 24

## Slide 25

First TrustZone-M single-stepping framework Instruction-level side-channel analysis Single-trace RSA key extraction **CVE-2025-54764**


> Recovered by OCR — confidence 83/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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


> Recovered by OCR — confidence 95/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
600
Revenue in billion U.S. dollars
Annual Production of loT devices
200 bn 2021 2022* 2023* 2024* 2025* 2026* 2027* 2028* 2029* 2030*
L trillion
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


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 88/100 on the text kept, 52/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
[Slide is a single wide table of 405 single-step trace entries, laid out in
nine columns of 45 rows each; each entry is an index, a program-counter
address and a two-digit cycle/interrupt count. Read column by column:]

1 0x0c024dd6 01
2 0x0c02b81a 03
3 0x0c02b81e 01
4 0x0c02b820 03
5 0x0c02b824 01
6 0x0c02b826 01
7 0x0c02b828 01
8 0x0c02b82a 01
9 0x0c02b82c 01
10 0x0c02be12 01
11 0x0c02be14 01
12 0x0c02be16 03
13 0x0c02be1a 01
14 0x0c02b830 01
15 0x0c02b834 01
16 0x0c02b846 01
17 0x0c02b848 01
18 0x0c02b84a 01
19 0x0c02b84c 01
20 0x0c02c406 03
21 0x0c02c408 01
22 0x0c02c40c 01
23 0x0c02c410 02
24 0x0c02c412 01
25 0x0c02c414 01
26 0x0c02c416 01
27 0x0c02c41a 01
28 0x0c02c41c 01
29 0x0c02c41e 02
30 0x0c02c422 02
31 0x0c02c426 01
32 0x0c02c428 01
33 0x0c02c42a 02
34 0x0c02c42c 01
35 0x0c02c3ce 01
36 0x0c02c3d2 01
37 0x0c02c36c 03
38 0x0c02c370 02
39 0x0c02c374 02
40 0x0c02c378 01
41 0x0c02c37a 01
42 0x0c02c37e 01
43 0x0c02c380 01
44 0x0c02c382 01
45 0x0c02c384 01
46 0x0c02c388 01
47 0x0c02c38a 01
48 0x0c02c38c 01
49 0x0c02c11e 03
50 0x0c02c120 02
51 0x0c02c122 01
52 0x0c02c12e 02
53 0x0c02c130 01
54 0x0c02c134 02
55 0x0c02c138 01
56 0x0c02c124 02
57 0x0c02c126 01
58 0x0c02c140 02
59 0x0c02c142 01
60 0x0c02c146 02
61 0x0c02c14a 01
62 0x0c02c150 01
63 0x0c02c12a 01
64 0x0c02c15e 04
65 0x0c02c390 01
66 0x0c02c394 01
67 0x0c02c396 01
68 0x0c02c398 01
69 0x0c02c39a 01
70 0x0c02c39c 01
71 0x0c02c2cc 03
72 0x0c02c2d0 01
73 0x0c02c2d2 01
74 0x0c02c2d4 01
75 0x0c02c2d6 02
76 0x0c02c2d8 01
77 0x0c02c334 02
78 0x0c02c338 01
79 0x0c02c33c 02
80 0x0c02c340 01
81 0x0c02c346 02
82 0x0c02c348 01
83 0x0c02c2dc 01
84 0x0c02c2de 01
85 0x0c02be38 01
86 0x0c02be3c 01
87 0x0c02be3e 03
88 0x0c02be40 01
89 0x0c02be42 01
90 0x0c02be4c 02
91 0x0c02be4e 01
92 0x0c02be56 01
93 0x0c02be58 01
94 0x0c02be5a 01
95 0x0c01f33c 01
96 0x0c01f33e 02
97 0x0c01f340 01
98 0x0c01f0ec 01
99 0x0c01f0ee 03
100 0x0c01f0f2 02
101 0x0c01f0f4 02
102 0x0c01f0f6 01
103 0x0c01f0f8 02
104 0x0c01f0fa 01
105 0x0c01f0fc 01
106 0x0c01f100 01
107 0x0c01f104 01
108 0x0c01f108 03
109 0x0c01f10c 01
110 0x0c01f110 01
111 0x0c01f114 01
112 0x0c01f134 01
113 0x0c01f11e 01
114 0x0c01f12a 01
115 0x0c01f122 02
116 0x0c01f124 01
117 0x0c01f138 02
118 0x0c01f13c 01
119 0x0c01f140 01
120 0x0c01f148 01
121 0x0c01f14a 01
122 0x0c01f14c 01
123 0x0c01f150 03
124 0x0c01f154 01
125 0x0c01f18e 01
126 0x0c01f192 01
127 0x0c01f196 01
128 0x0c01f198 03
129 0x0c01f19c 02
130 0x0c01f19e 01
131 0x0c01f1a2 02
132 0x0c01f1a4 02
133 0x0c01f1a6 02
134 0x0c01f1aa 01
135 0x0c01f1ae 02
136 0x0c01f1b2 01
137 0x0c01f1b4 02
138 0x0c01f1b6 03
139 0x0c01f1ba 01
140 0x0c01f1ce 02
141 0x0c01f1be 02
142 0x0c01f1c0 01
143 0x0c01f1c2 02
144 0x0c01f1c4 01
145 0x0c01f1c6 02
146 0x0c01f1c8 03
147 0x0c01f1cc 01
148 0x0c01f166 01
149 0x0c01f168 03
150 0x0c01f16c 02
151 0x0c01f16e 01
152 0x0c01f17a 01
153 0x0c01f17c 01
154 0x0c01f17e 01
155 0x0c01f180 01
156 0x0c01f182 01
157 0x0c02952c 01
158 0x0c02952e 03
159 0x0c029530 01
160 0x0c029532 01
161 0x0c029536 01
162 0x0c029538 01
163 0x0c02953c 01
164 0x0c029552 01
165 0x0c02953e 01
166 0x0c029540 01
167 0x0c029542 01
168 0x0c02955e 01
169 0x0c029560 02
170 0x0c029562 01
171 0x0c029542 01
172 0x0c02955e 01
173 0x0c029560 02
174 0x0c029562 01
175 0x0c029542 01
176 0x0c02955e 01
177 0x0c029560 02
178 0x0c029562 01
179 0x0c029542 01
180 0x0c02955e 01
181 0x0c029560 02
182 0x0c029562 01
183 0x0c029542 01
184 0x0c02955e 01
185 0x0c029560 02
186 0x0c029562 01
187 0x0c029542 01
188 0x0c02955e 01
189 0x0c029560 02
190 0x0c029562 01
191 0x0c029542 01
192 0x0c02955e 01
193 0x0c029560 02
194 0x0c029562 01
195 0x0c029542 01
196 0x0c02955e 01
197 0x0c029560 02
198 0x0c029562 01
199 0x0c029542 01
200 0x0c02955e 01
201 0x0c029560 02
202 0x0c029562 01
203 0x0c029542 01
204 0x0c02955e 01
205 0x0c029560 02
206 0x0c029562 01
207 0x0c029542 01
208 0x0c02955e 01
209 0x0c029560 02
210 0x0c029562 01
211 0x0c029542 01
212 0x0c02955e 01
213 0x0c029560 02
214 0x0c029562 01
215 0x0c029542 01
216 0x0c02955e 01
217 0x0c029560 02
218 0x0c029562 01
219 0x0c029542 01
220 0x0c02955e 01
221 0x0c029560 02
222 0x0c029562 01
223 0x0c029542 01
224 0x0c02955e 01
225 0x0c029560 02
226 0x0c029562 01
227 0x0c029542 01
228 0x0c02955e 01
229 0x0c029560 02
230 0x0c029562 01
231 0x0c029542 01
232 0x0c029546 01
233 0x0c029548 01
234 0x0c02954c 01
235 0x0c029550 04
236 0x0c01f186 01
237 0x0c01f12e 01
238 0x0c01f130 04
239 0x0c02be5e 01
240 0x0c02be60 01
241 0x0c02be64 02
242 0x0c02be66 01
243 0x0c02be7a 02
244 0x0c02be7c 02
245 0x0c02be52 01
246 0x0c02be4a 04
247 0x0c02c2e2 01
248 0x0c02c2e4 01
249 0x0c02c2e6 02
250 0x0c02c2e8 01
251 0x0c02c2ec 01
252 0x0c02c2f0 02
253 0x0c02c2f2 02
254 0x0c02c2f4 01
255 0x0c02c2f6 01
256 0x0c02c2f8 01
257 0x0c02c2fc 01
258 0x0c02c300 01
259 0x0c02968e 01
260 0x0c029690 03
261 0x0c029692 01
262 0x0c0296b0 01
263 0x0c0296b4 01
264 0x0c029694 01
265 0x0c029696 01
266 0x0c029698 01
267 0x0c0296c4 01
268 0x0c0296c6 02
269 0x0c0296c8 01
270 0x0c0296ca 02
271 0x0c0296cc 01
272 0x0c029696 01
273 0x0c029698 01
274 0x0c0296c4 01
275 0x0c0296c6 02
276 0x0c0296c8 01
277 0x0c0296ca 02
278 0x0c0296cc 01
279 0x0c029696 01
280 0x0c029698 01
281 0x0c0296c4 01
282 0x0c0296c6 02
283 0x0c0296c8 01
284 0x0c0296ca 02
285 0x0c0296cc 01
286 0x0c029696 01
287 0x0c029698 01
288 0x0c0296c4 01
289 0x0c0296c6 02
290 0x0c0296c8 01
291 0x0c0296ca 02
292 0x0c0296cc 01
293 0x0c029696 01
294 0x0c029698 01
295 0x0c0296c4 01
296 0x0c0296c6 02
297 0x0c0296c8 01
298 0x0c0296ca 02
299 0x0c0296cc 01
300 0x0c029696 01
301 0x0c029698 01
302 0x0c0296c4 01
303 0x0c0296c6 02
304 0x0c0296c8 01
305 0x0c0296ca 02
306 0x0c0296cc 01
307 0x0c029696 01
308 0x0c029698 01
309 0x0c0296c4 01
310 0x0c0296c6 02
311 0x0c0296c8 01
312 0x0c0296ca 02
313 0x0c0296cc 01
314 0x0c029696 01
315 0x0c029698 01
316 0x0c0296c4 01
317 0x0c0296c6 02
318 0x0c0296c8 01
319 0x0c0296ca 02
320 0x0c0296cc 01
321 0x0c029696 01
322 0x0c029698 01
323 0x0c0296c4 01
324 0x0c0296c6 02
325 0x0c0296c8 01
326 0x0c0296ca 02
327 0x0c0296cc 01
328 0x0c029696 01
329 0x0c029698 01
330 0x0c0296c4 01
331 0x0c0296c6 02
332 0x0c0296c8 01
333 0x0c0296ca 02
334 0x0c0296cc 01
335 0x0c029696 01
336 0x0c029698 01
337 0x0c0296c4 01
338 0x0c0296c6 02
339 0x0c0296c8 01
340 0x0c0296ca 02
341 0x0c0296cc 01
342 0x0c029696 01
343 0x0c029698 01
344 0x0c0296c4 01
345 0x0c0296c6 02
346 0x0c0296c8 01
347 0x0c0296ca 02
348 0x0c0296cc 01
349 0x0c029696 01
350 0x0c029698 01
351 0x0c0296c4 01
352 0x0c0296c6 02
353 0x0c0296c8 01
354 0x0c0296ca 02
355 0x0c0296cc 01
356 0x0c029696 01
357 0x0c029698 01
358 0x0c0296c4 01
359 0x0c0296c6 02
360 0x0c0296c8 01
361 0x0c0296ca 02
362 0x0c0296cc 01
363 0x0c029696 01
364 0x0c029698 01
365 0x0c0296c4 01
366 0x0c0296c6 02
367 0x0c0296c8 01
368 0x0c0296ca 02
369 0x0c0296cc 01
370 0x0c029696 01
371 0x0c029698 01
372 0x0c02969c 01
373 0x0c0296a0 01
374 0x0c0296a2 01
375 0x0c0296a4 01
376 0x0c0296a6 01
377 0x0c0296aa 01
378 0x0c0296ae 04
379 0x0c02c304 02
380 0x0c02c306 02
381 0x0c02c308 01
382 0x0c02c31c 02
383 0x0c02c320 01
384 0x0c02c322 02
385 0x0c02c324 02
386 0x0c02c326 01
387 0x0c02d102 03
388 0x0c02d104 01
389 0x0c02d106 01
390 0x0c02d108 01
391 0x0c02d10a 01
392 0x0c02d110 02
393 0x0c02d114 02
394 0x0c02d118 01
395 0x0c02d11c 01
396 0x0c02d120 01
397 0x0c02d124 01
398 0x0c02d128 01
399 0x0c02d12a 02
400 0x0c02d12e 01
401 0x0c02d132 01
402 0x0c02d134 01
403 0x0c02d138 01
404 0x0c02d10a 01
405 0x0c02d10e 04
```

## Slide 211

**Raw Trace**


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 88/100 on the text kept, 51/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
[Same 405-entry single-step trace table as the previous slide, with three "confused" reaction-meme images pasted over it. Visible table text, read column by column:]

Column 1 (entries 1-45):
1 0x0c024dd6 01
2 0x0c02b81a 03
3-22 [addresses hidden behind meme image; only the leading "0x0" of each is visible]
23 0x0c02c410 02
24 0x0c02c412 01
25 0x0c02c414 01
26 0x0c02c416 01
27 0x0c02c41a 01
28 0x0c02c41c 01
29 0x0c02c41e 02
30 0x0c02c422 02
31 0x0c02c426 01
32 0x0c02c428 01
33 0x0c02c42a 02
34 0x0c02c42c 01
35 0x0c02c3ce 01
36 0x0c02c3d2 01
37 0x0c02c36c 03
38 0x0c02c370 02
39 0x0c02c374 02
40 0x0c02c378 01
41 0x0c02c37a 01
42 0x0c02c37e 01
43 0x0c02c380 01
44 0x0c02c382 01
45 0x0c02c384 01

Column 2 (entries 46-90):
46 0x0c02c388 01
47 0x0c02c38a 01
48-67 [hidden behind meme image]
68 0x0c02c398 01
69 0x0c02c39a 01
70 0x0c02c39c 01
71 0x0c02c2cc 03
72 0x0c02c2d0 01
73 0x0c02c2d2 01
74 0x0c02c2d4 01
75 0x0c02c2d6 02
76 0x0c02c2d8 01
77 0x0c02c334 02
78 0x0c02c338 01
79 0x0c02c33c 02
80 0x0c02c340 01
81 0x0c02c346 02
82 0x0c02c348 01
83 0x0c02c2dc 01
84 0x0c02c2de 01
85 0x0c02be38 01
86 0x0c02be3c 01
87 0x0c02be3e 03
88 0x0c02be40 01
89 0x0c02be42 01
90 0x0c02be4c 02

Column 3 (entries 91-135):
91 0x0c02be4e 01
92 0x0c02be56 01
[entries 93-112: addresses hidden behind meme image; only the trailing counts are visible: 01 01 01 02 01 01 03 02 02 01 02 01 01 01 01 03 01 01 01 01]
113 0x0c01f11e 01
[entries 114-134: addresses visible but trailing counts clipped by the meme image]
114 0x0c01f12a
115 0x0c01f122
116 0x0c01f124
117 0x0c01f138
118 0x0c01f13c
119 0x0c01f140
120 0x0c01f148
121 0x0c01f14a
122 0x0c01f14c
123 0x0c01f150
124 0x0c01f154
125 0x0c01f18e
126 0x0c01f192
127 0x0c01f196
128 0x0c01f198
129 0x0c01f19c
130 0x0c01f19e
131 0x0c01f1a2
132 0x0c01f1a4
133 0x0c01f1a6
134 0x0c01f1aa
135 0x0c01f1ae 02

Column 4 (entries 136-180):
136 0x0c01f1b2 01
137 0x0c01f1b4 02
138 0x0c01f1b6 03
139 0x0c01f1ba 01
140 0x0c01f1ce 02
141 0x0c01f1be 02
142 0x0c01f1c0 01
143 0x0c01f1c2 02
144 0x0c01f1c4 01
145 0x0c01f1c6 02
146 0x0c01f1c8 03
147 0x0c01f1cc 01
148 0x0c01f166 01
149 0x0c01f168 03
150 0x0c01f16c 02
151 0x0c01f16e 01
152 0x0c01f17a 01
153 0x0c01f17c 01
154 0x0c01f17e 01
155 0x0c01f180 01
156 0x0c01f182 01
157 0x0c02952c 01
158 0x0c02952e 03
159-178 [hidden behind meme image]
179 0x0c029542 01
180 0x0c02955e 01

Column 5 (entries 181-225):
181 0x0c029560 02
182 0x0c029562 01
183 0x0c029542 01
184 0x0c02955e 01
185 0x0c029560 02
186 0x0c029562 01
187 0x0c029542 01
188 0x0c02955e 01
189 0x0c029560 02
190 0x0c029562 01
191 0x0c029542 01
192 0x0c02955e 01
193 0x0c029560 02
194 0x0c029562 01
195 0x0c029542 01
196 0x0c02955e 01
197 0x0c029560 02
198 0x0c029562 01
199 0x0c029542 01
200 0x0c02955e 01
201 0x0c029560 02
202 0x0c029562 01
203 0x0c029542 01
204-224 [hidden behind meme image]
225 0x0c029560 02

Column 6 (entries 226-270):
226 0x0c029562 01
227 0x0c029542 01
228 0x0c02955e 01
229 0x0c029560 02
[entries 230-250: index numbers visible, addresses hidden behind meme image]
[entries 251-269: addresses visible, index numbers hidden behind meme image]
   0x0c02c2ec 01
   0x0c02c2f0 02
   0x0c02c2f2 02
   0x0c02c2f4 01
   0x0c02c2f6 01
   0x0c02c2f8 01
   0x0c02c2fc 01
   0x0c02c300 01
   0x0c02968e 01
   0x0c029690 03
   0x0c029692 01
   0x0c0296b0 01
   0x0c0296b4 01
   0x0c029694 01
   0x0c029696 01
   0x0c029698 01
   0x0c0296c4 01
   0x0c0296c6 02
   0x0c0296c8 01
270 0x0c0296ca 02

Column 7 (entries 271-315):
271 0x0c0296cc 01
272 0x0c029696 01
273 0x0c029698 01
274 0x0c0296c4 01
275-295 [hidden behind meme image]
296 0x0c0296c6 02
297 0x0c0296c8 01
298 0x0c0296ca 02
299 0x0c0296cc 01
300 0x0c029696 01
301 0x0c029698 01
302 0x0c0296c4 01
303 0x0c0296c6 02
304 0x0c0296c8 01
305 0x0c0296ca 02
306 0x0c0296cc 01
307 0x0c029696 01
308 0x0c029698 01
309 0x0c0296c4 01
310 0x0c0296c6 02
311 0x0c0296c8 01
312 0x0c0296ca 02
313 0x0c0296cc 01
314 0x0c029696 01
315 0x0c029698 01

Column 8 (entries 316-360):
316 0x0c0296c4 01
317 0x0c0296c6 02
318 0x0c0296c8 01
319 0x0c0296ca 02
320-340 [hidden behind meme image]
341 0x0c0296cc 01
342 0x0c029696 01
343 0x0c029698 01
344 0x0c0296c4 01
345 0x0c0296c6 02
346 0x0c0296c8 01
347 0x0c0296ca 02
348 0x0c0296cc 01
349 0x0c029696 01
350 0x0c029698 01
351 0x0c0296c4 01
352 0x0c0296c6 02
353 0x0c0296c8 01
354 0x0c0296ca 02
355 0x0c0296cc 01
356 0x0c029696 01
357 0x0c029698 01
358 0x0c0296c4 01
359 0x0c0296c6 02
360 0x0c0296c8 01

Column 9 (entries 361-405):
361 0x0c0296ca 02
362 0x0c0296cc 01
363 0x0c029696 01
364 0x0c029698 01
[entries 365-385: addresses hidden behind meme image; only the trailing counts are visible: 01 02 01 02 01 01 01 01 01 01 01 01 01 04 02 02 01 02 01 02 02]
386 0x0c02c326 01
387 0x0c02d102 03
388 0x0c02d104 01
389 0x0c02d106 01
390 0x0c02d108 01
391 0x0c02d10a 01
392 0x0c02d110 02
393 0x0c02d114 02
394 0x0c02d118 01
395 0x0c02d11c 01
396 0x0c02d120 01
397 0x0c02d124 01
398 0x0c02d128 01
399 0x0c02d12a 02
400 0x0c02d12e 01
401 0x0c02d132 01
402 0x0c02d134 01
403 0x0c02d138 01
404 0x0c02d10a 01
405 0x0c02d10e 04

Text inside the overlaid images:
  SEL MAR 28
  ["math lady" meme panels showing chalkboard formulas: V = (1/3)πr²h ; A = πr² ; C = 2πr ; V = πr²h ; a sin/cos/tan table for 30° 45° 60° ; ∫ sin x dx = -cos x + C ; ∫ dx/cos² x = tg x + C ; ∫ tg x dx = -ln|cos x| + C ; ∫ dx/(a² + x²) = (1/a) arctg ... ; tan(θ) plot with θ/rad axis ; ax² + bx + c = 0 ; a(x² + (b/a)x + (c/a)) = 0]
```

## Slide 212

## Slide 213


> Recovered by OCR — confidence 84/100 on the text kept, 58/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
18
19
20
21
22
23
@x@c@2c406
@x@c@2c408
@x@c@2c40c
20
```

## Slide 214

###### **Program Counter of the Instruction**

**Raw Trace**

## Slide 215

###### **Program Counter of the Instruction**

##### **Raw Trace**

###### **Interrupt Latency**

## Slide 216

**Mstp-Visualizer**

## Slide 217

M-Step Visualizer (GTKwave)


> Recovered by OCR — confidence 80/100 on the text kept, 45/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Time
clk=0
Instructior
inst_raw=c|
inst_full =c|
M-Step Visualizer (GI Kwave)
```

## Slide 218

###### M-Step Visualizer (GTKwave)

v


> Recovered by OCR — confidence 77/100 on the text kept, 42/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
4676 ns 4690 ns
Time
clk =6
cycle[31:0] =2
func =t
```

## Slide 219

###### M-Step Visualizer (GTKwave)

**Program Counter of the Instruction**

v


> Recovered by OCR — confidence 93/100 on the text kept, 46/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
M-Step Visualizer (GI Kwave)
Time
clk=0
Instruction
Program Counter of the Instruction
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


> Recovered by OCR — confidence 69/100 on the text kept, 65/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
M-Step Visualizer (GI Kwave)
inst_full =. ré, r2, r3 icmp r2, #3 subs r7, r6, r2_ {str ré
```

## Slide 222

M-Step Visualizer (GTKwave)


> Recovered by OCR — confidence 82/100 on the text kept, 60/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
M-Step Visualizer (GI Kwave)
Time
clk=0 |
Instruction
ime
cycle[31:0] =2
instr_addr[31:0] =0)
```

## Slide 223

M-Step Visualizer (GTKwave)


> Recovered by OCR — confidence 82/100 on the text kept, 56/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
M-Step Visualizer (GI Kwave)
Time
Instruction
Time
clk =6
cycle[31:0] =2
tructio
```

## Slide 224

M-Step Visualizer (GTKwave)


> Recovered by OCR — confidence 90/100 on the text kept, 41/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
M-Step Visualizer (GI Kwave)
Time
ime
clk=0
Instructio
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


> Recovered by OCR — confidence 86/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
[ No Source Available ]
[ No Assembly Available ]
lextended-r Thread 1 In: Reset_Handler L893 PC: Oxc018e70
(gdb) ||
[M-Step-DeO:bash*Z 1:fish- 2:fish ",/1-gdb-py.sh -s exp " 12:47 18-jun-25
```

## Slide 235


> Recovered by OCR — confidence 87/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
[ No Source Available ]
lextended-r Thread 1 In: Reset_Handler
[ No Assembly Available ]
(gdb) b *0x0c028868
Breakpoint 1 at 0xc028868: file /home/cris/Documents/0_Projects/jo-collab/m-step/mstp-victims/s/src/victims.c, line 6.
(gab) []
[M-Step-DeO:bash*Z 1:fish- 2:fish
",/1-gdb-py.sh -s exp " 12:48 18-jun-25|
```

## Slide 236


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 80/100 on the text kept, 77/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
┌─/home/cris/Documents/0_Projects/jo-collab/m-step/mstp-victims/s/src/victims.c
        1 #include "victims.h"
        2
        3 #define STRING "M-Step-S\r\n"
        4
        5 void victim_printf_inst(){
B+>     6   printf(STRING);
        7 }
        8
        9 void victim_strlen_inst(){
       10   strlen(STRING);
       11 }
       12

B+>0xc028868 <victim_printf_inst>         ldr     r0, [pc, #4]    @ (0xc028870 <victim_printf_inst+8>)
   0xc02886a <victim_printf_inst+2>       b.w     0xc028e8c <printf>
   0xc02886e <victim_printf_inst+6>       nop
   0xc028870 <victim_printf_inst+8>       asrs    r1, r6, #29
   0xc028872 <victim_printf_inst+10>      lsrs    r3, r0, #16
   0xc028874 <victim_strlen_inst>         ldr     r0, [pc, #4]    @ (0xc02887c <victim_strlen_inst+8>)
   0xc028876 <victim_strlen_inst+2>       b.w     0xc02fbce <strlen>
   0xc02887a <victim_strlen_inst+6>       nop
   0xc02887c <victim_strlen_inst+8>       asrs    r1, r6, #29
   0xc02887e <victim_strlen_inst+10>      lsrs    r3, r0, #16
   0xc028880 <QCBOREncode_EncodeHead>     stmdb   sp!, {r0, r1, r2, r4, r5, r6, r7, r8, r9, lr}
   0xc028884 <QCBOREncode_EncodeHead+4>   add     r4, sp, #8
   0xc028886 <QCBOREncode_EncodeHead+6>   stmdb   r4, {r1, r2}

extended-r Thread 1 In: victim_printf_inst                                              L6      PC: 0xc028868
(gdb) b *0x0c028868
Breakpoint 1 at 0xc028868: file /home/cris/Documents/0_Projects/jo-collab/m-step/mstp-victims/s/src/victims.c, line 6.
(gdb) c
Continuing.

Breakpoint 1, victim_printf_inst () at /home/cris/Documents/0_Projects/jo-collab/m-step/mstp-victims/s/src/victims.c:6
[Trace Info] PC=0x0C028868 | 7 clk
(gdb) █

[M-Step-De0:bash*Z 1:fish- 2:fish                                          "./1-gdb-py.sh -s exp " 12:49 18-jun-25
```

## Slide 237


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 81/100 on the text kept, 76/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
┌─/home/cris/Documents/0_Projects/jo-collab/m-step/mstp-victims/s/src/victims.c
        1 #include "victims.h"
        2
        3 #define STRING "M-Step-S\r\n"
        4
        5 void victim_printf_inst(){
B+>     6   printf(STRING);
        7 }
        8
        9 void victim_strlen_inst(){
       10   strlen(STRING);
       11 }
       12

B+ 0xc028868 <victim_printf_inst>         ldr     r0, [pc, #4]    @ (0xc028870 <victim_printf_inst+8>)
  >0xc02886a <victim_printf_inst+2>       b.w     0xc028e8c <printf>
   0xc02886e <victim_printf_inst+6>       nop
   0xc028870 <victim_printf_inst+8>       asrs    r1, r6, #29
   0xc028872 <victim_printf_inst+10>      lsrs    r3, r0, #16
   0xc028874 <victim_strlen_inst>         ldr     r0, [pc, #4]    @ (0xc02887c <victim_strlen_inst+8>)
   0xc028876 <victim_strlen_inst+2>       b.w     0xc02fbce <strlen>
   0xc02887a <victim_strlen_inst+6>       nop
   0xc02887c <victim_strlen_inst+8>       asrs    r1, r6, #29
   0xc02887e <victim_strlen_inst+10>      lsrs    r3, r0, #16
   0xc028880 <QCBOREncode_EncodeHead>     stmdb   sp!, {r0, r1, r2, r4, r5, r6, r7, r8, r9, lr}
   0xc028884 <QCBOREncode_EncodeHead+4>   add     r4, sp, #8
   0xc028886 <QCBOREncode_EncodeHead+6>   stmdb   r4, {r1, r2}

extended-r Thread 1 In: victim_printf_inst                                              L6      PC: 0xc02886a
(gdb) b *0x0c028868
Breakpoint 1 at 0xc028868: file /home/cris/Documents/0_Projects/jo-collab/m-step/mstp-victims/s/src/victims.c, line 6.
(gdb) c
Continuing.

Breakpoint 1, victim_printf_inst () at /home/cris/Documents/0_Projects/jo-collab/m-step/mstp-victims/s/src/victims.c:6
[Trace Info] PC=0x0C028868 | 7 clk
(gdb) ni
[Trace Info] PC=0x0C02886A | 1 clk
(gdb) █

[M-Step-De0:bash*Z 1:fish- 2:fish                                          "./1-gdb-py.sh -s exp " 12:50 18-jun-25
```

## Slide 238


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 80/100 on the text kept, 76/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
┌─/home/cris/Documents/0_Projects/jo-collab/m-step/mstp-victims/s/src/victims.c
        1 #include "victims.h"
        2
        3 #define STRING "M-Step-S\r\n"
        4
        5 void victim_printf_inst(){
B+>     6   printf(STRING);
        7 }
        8
        9 void victim_strlen_inst(){
       10   strlen(STRING);
       11 }
       12

B+ 0xc028868 <victim_printf_inst>         ldr     r0, [pc, #4]    @ (0xc028870 <victim_printf_inst+8>)
  >0xc02886a <victim_printf_inst+2>       b.w     0xc028e8c <printf>
   0xc02886e <victim_printf_inst+6>       nop
   0xc028870 <victim_printf_inst+8>       asrs    r1, r6, #29
   0xc028872 <victim_printf_inst+10>      lsrs    r3, r0, #16
   0xc028874 <victim_strlen_inst>         ldr     r0, [pc, #4]    @ (0xc02887c <victim_strlen_inst+8>)
   0xc028876 <victim_strlen_inst+2>       b.w     0xc02fbce <strlen>
   0xc02887a <victim_strlen_inst+6>       nop
   0xc02887c <victim_strlen_inst+8>       asrs    r1, r6, #29
   0xc02887e <victim_strlen_inst+10>      lsrs    r3, r0, #16
   0xc028880 <QCBOREncode_EncodeHead>     stmdb   sp!, {r0, r1, r2, r4, r5, r6, r7, r8, r9, lr}
   0xc028884 <QCBOREncode_EncodeHead+4>   add     r4, sp, #8
   0xc028886 <QCBOREncode_EncodeHead+6>   stmdb   r4, {r1, r2}

extended-r Thread 1 In: victim_printf_inst                                              L6      PC: 0xc02886a
(gdb) b *0x0c028868
Breakpoint 1 at 0xc028868: file /home/cris/Documents/0_Projects/jo-collab/m-step/mstp-victims/s/src/victims.c, line 6.
(gdb) c
Continuing.

Breakpoint 1, victim_printf_inst () at /home/cris/Documents/0_Projects/jo-collab/m-step/mstp-victims/s/src/victims.c:6
[red highlight box around the following four lines:]
[Trace Info] PC=0x0C028868 | 7 clk
(gdb) ni
[Trace Info] PC=0x0C02886A | 1 clk
(gdb) █

[M-Step-De0:bash*Z 1:fish- 2:fish                                          "./1-gdb-py.sh -s exp " 12:50 18-jun-25
```

## Slide 239


> Recovered by OCR — confidence 84/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
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


> Recovered by OCR — confidence 84/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
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


> Recovered by OCR — confidence 84/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
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


> Recovered by OCR — confidence 85/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
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
Info] PC=0x0CO2886A | 1 clk
Info] PC=0xOCO28E8C | 3 clk
Info] PC=0xOCO28E8E | 3 clk
Info] PC=0x0CO28E90 | 1 clk
Info] PC=0xOCO28E92 | 2 clk
L166 PC: Oxc028e92
",/1-gdb-py.sh -s exp " 12:51 18-jun-25
```

## Slide 243


> Recovered by OCR — confidence 85/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
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
gdb) ni
Info] PC=0x0CO2886A | 1 clk
Info] PC=0x0CO28E8C clk
Info] PC=0x0CO28E8E clk
Info] PC=0x0C028E90 clk
Info] PC=0x0C028E92 clk
Info] PC=0x0CO28E96 clk
L170 PC: Oxc028e96
",/1-gdb-py.sh -s exp " 12:51 18-jun-25
```

## Slide 244


> Recovered by OCR — confidence 84/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
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
",/1-gdb-py.sh -s exp " 12:52 18-jun-25]
```

## Slide 245


> Recovered by OCR — confidence 83/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
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
OxcO28e9e <printf+18> ldr.w Ur, [sp], #4
OxcO28ea2 <printf+22> add sp, #16
OxcO28ea4 <printf+24> bx lr
OxcO28ea6 <tfm_output_unpriv_string> svc 2
OxcO28ea8 <tfm_output_unpriv_string+2> bx lr
OxcO28eaa <tfm_hal_output_sp_log> b.w OxcO28ea6 <tfm_output_unpriv_string>
lextended-r Thread 1 In: printf
Continuing.
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


> Recovered by OCR — confidence 83/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
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
eOxcO28e9e <printf+18> ldr.w .r, [sp], #4
OxcO28ea2 <printf+22> add sp, #16
OxcO28ea4 <printf+24> bx lr
OxcO28ea6 <tfm_output_unpriv_string> svc 2
OxcO28ea8 <tfm_output_unpriv_string+2> bx lr
OxcO28eaa <tfm_hal_output_sp_log> b.w OxcO28ea6 <tfm_output_unpriv_string>
lextended-r Thread 1 In: printf
(gdb) ni
Info] PC=O0x0CO2886A | 1 clk
Info] PC=0x0CO28E8C clk
Info] PC=0x0CO28E8E clk
Info] PC=0x0C028E90 clk
Info] PC=0x0C028E92 clk
Info] PC=0x0C028E96 clk
Info] PC=0x0CO28E98 clk
Info] PC=0x0CO28E9C clk
L174 PC: OxcO28e9e
",/1-gdb-py.sh -s exp " 12:52 18-jun-25
```

## Slide 247


> Recovered by OCR — confidence 83/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
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


> Recovered by OCR — confidence 80/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
[World Use Case
1 procedure Mbedtls_BEEA(Xx, A, B)
= 2 TU —A,TV <—B;
— 5 while TU even do L |
8 | U1<—U1+TB,U2<U2-TA
10 while TV even do
17 U1 — U1-V1;U2 —U2-V2;
19 else
20 TV —TV-TU;
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


> Recovered by OCR — confidence 86/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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
while TU # 0 do
while TU even do
TU —TU/2;
| U1-—U1+T7TB,U2<—U2-TA
while TV even do
TV —TV/2;
if TU > TV then
TU —TU -TV;
U1 — U1-V1;U2 —U2-V2;
TU —TU/2;
else
TV —TV-TU;
TV —TV/2;
BRARY
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


> Recovered by OCR — confidence 86/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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
while TU # 0 do
while TU even do
TU —TU/2;
| U1-—U1+T7TB,U2<—U2-TA
while TV even do
TV —TV/2;
if TU > TV then
TU —TU -TV;
U1 — U1-V1;U2 —U2-V2;
TU —TU/2;
else
TV —TV-TU;
TV —TV/2;
BRARY
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


> Recovered by OCR — confidence 89/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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
U1<—1,U2<—0,V1<—0,V2<—1;
while TU # 0 do
while TU even do
while TV even do
TV —TV/2;
if TU > TV then
TU —TU -TV;
U1 — U1-V1; U2 — U2-V2;
TU —TU/2;
else
TV —TV-TU;
TV —TV/2;
50
```

## Slide 272

###### BEEA Template Matrices

51


> Recovered by OCR — confidence 85/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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
while TU # 0 do
while TU even do
while TV even do
TV —TV/2;
if TU > TV then
TU —TU -TV;
U1 — U1-V1;U2< U2-V2;
TU —TU/2;
else
TV —TV-TU;
TV —TV/2;
u_noif o ee
v_if eee | |
v_noif o ee a
) 2 4 6 8 138 140 142 144 146 148 150
Sample Index (samples 10-137 hidden)
SUB_U_1 ||
SUB_U_2 ||
SUB_U_5
SUB_V_2 |
SUB_V_3 ||
Sample Index
51
```

## Slide 273

###### BEEA Template Matrices

51

## Slide 274

###### BEEA Template Matrices

51


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 91/100 on the text kept, 86/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
BEEA Template Matrices

 1  procedure Mbedtls_BEEA(X, A, B)
 2      TU ← A, TV ← B;
 3      U1 ← 1, U2 ← 0, V1 ← 0, V2 ← 1;
 4      while TU ≠ 0 do
 5          while TU even do
 6              TU ← TU/2;
 7              if U1 or U2 odd then
 8                  U1 ← U1 + TB; U2 ← U2 − TA ;
 9              U1 ← U1/2; U2 ← U2/2 ;
10          while TV even do
11              TV ← TV/2;
12              if V1 or V2 odd then
13                  V1 ← V1 + TB; V2 ← V2 − TA ;
14              V1 ← V1/2; V2 ← V2/2 ;
15          if TU ≥ TV then
16              TU ← TU − TV;
17              U1 ← U1 − V1; U2 ← U2 − V2 ;
18              TU ← TU/2 ;
19          else
20              TV ← TV − TU;
21              V1 ← V1 − U1; V2 ← V2 − U2 ;
22              TV ← TV/2 ;

[lines 10-14 are shown in full black; lines 13 and 14 are highlighted in blue. All other lines are greyed out.]

[Top heat-map, rows top to bottom — u_if and u_noif greyed out, v_if and v_noif emphasised:]
u_if
u_noif
v_if
v_noif
x-axis ticks: 0  2  4  6  8      138  140  142  144  146  148  150
Sample Index (samples 10-137 hidden)

[Bottom heat-map, greyed out, rows top to bottom:]
SUB_U_1
SUB_U_2
SUB_U_3
SUB_U_4
SUB_U_5
SUB_V_1
SUB_V_2
SUB_V_3
x-axis ticks: 0  5  10  15  20
Sample Index

51
```

## Slide 275

###### BEEA Template Matrices

51

## Slide 276

###### BEEA Template Matrices

51


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 92/100 on the text kept, 88/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
BEEA Template Matrices

 1  procedure Mbedtls_BEEA(X, A, B)
 2      TU ← A, TV ← B;
 3      U1 ← 1, U2 ← 0, V1 ← 0, V2 ← 1;
 4      while TU ≠ 0 do
 5          while TU even do
 6              TU ← TU/2;
 7              if U1 or U2 odd then
 8                  U1 ← U1 + TB; U2 ← U2 − TA ;
 9              U1 ← U1/2; U2 ← U2/2 ;
10          while TV even do
11              TV ← TV/2;
12              if V1 or V2 odd then
13                  V1 ← V1 + TB; V2 ← V2 − TA ;
14              V1 ← V1/2; V2 ← V2/2 ;
15          if TU ≥ TV then
16              TU ← TU − TV;
17              U1 ← U1 − V1; U2 ← U2 − V2 ;
18              TU ← TU/2 ;
19          else
20              TV ← TV − TU;
21              V1 ← V1 − U1; V2 ← V2 − U2 ;
22              TV ← TV/2 ;

[lines 19-22 are shown in full black; line 21 is highlighted in blue and line 22 in orange. All other lines are greyed out.]

[Top heat-map, greyed out, rows top to bottom:]
u_if
u_noif
v_if
v_noif
x-axis ticks: 0  2  4  6  8      138  140  142  144  146  148  150
Sample Index (samples 10-137 hidden)

[Bottom heat-map, rows top to bottom — SUB_U_1 through SUB_U_5 greyed out, SUB_V_1, SUB_V_2 and SUB_V_3 emphasised:]
SUB_U_1
SUB_U_2
SUB_U_3
SUB_U_4
SUB_U_5
SUB_V_1
SUB_V_2
SUB_V_3
x-axis ticks: 0  5  10  15  20
Sample Index

51
```

## Slide 277

###### BEEA Template Matrices

51


> Recovered by OCR — confidence 85/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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
while TU # 0 do
while TU even do
while TV even do
TV —TV/2;
if TU > TV then
TU —TU -TV;
U1 — U1-V1;U2< U2-V2;
TU —TU/2;
else
TV —TV-TU;
TV —TV/2;
u_noif o ee
v_if eee | |
v_noif o ee a
) 2 4 6 8 138 140 142 144 146 148 150
Sample Index (samples 10-137 hidden)
SUB_U_1 ||
SUB_U_2 ||
SUB_U_5
SUB_V_2 |
SUB_V_3 ||
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


> Recovered by OCR — confidence 75/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
wli/vhs on 9 exp/cli [x!?] via [ impure (tfm-dev-shell-env)
```

## Slide 295

What Changes Now?

## Slide 296

What Changes Now?

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
