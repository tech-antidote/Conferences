---
title: "Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V"
speakers: ["Fabian Thomas", "Ruiyi Zhang", "Lorenz Hetterich", "Michael Schwarz"]
conference: "Black Hat"
conference_full: "Black Hat USA 2024"
edition: "USA"
year: 2024
source_pdf: "Black Hat USA 2024 slides/Fabian Thomas & Ruiyi Zhang & Lorenz Hetterich & Michael Schwarz_Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V_Compressed.pdf"
pages: 157
sha256: "0cfa12a78bcd776561c2684ec923ac201d4c9232f064414f1c229e026397cde8"
text_chars: 30591
ocr_pages: 1
has_ocr: true
redacted_secrets: 0
ocr_confidence: 87.6
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:31:16Z"
---
# Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V

**Speakers:** Fabian Thomas, Ruiyi Zhang, Lorenz Hetterich, Michael Schwarz  
**Conference:** Black Hat USA 2024  
**Source:** `Black Hat USA 2024 slides/Fabian Thomas & Ruiyi Zhang & Lorenz Hetterich & Michael Schwarz_Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V_Compressed.pdf` (157 pages)


## Slide 1

Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V

Fabian Thomas, Lorenz Hetterich

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
=>
blackhat — =
USA 2024
AUGUST 7-8, 2024
Arbitrary Data Manipulation and
Leakage with CPU Zero-Day Bugs
on RISC-V
Fabian Thomas, Lorenz Hetterich
#BHUSA @BlackHatEvents
```

## Slide 2

# **The Advertisement Panel**

**#BHUSA @BlackHatEvents**

**2 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 3

**The Challenge: Operating System**

Application

Hardware

**#BHUSA @BlackHatEvents**

**3 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 4

The Challenge: Operating System

Application

Hardware

**#BHUSA @BlackHatEvents**

**3 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 5

The Challenge: Operating System

system call
Application OS Hardware

**#BHUSA @BlackHatEvents**

**3 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 6

# **The Challenge: Operating System**

system call
Application OS Hardware
userspace kernelspace

**#BHUSA @BlackHatEvents**

**3 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 7

# **The Challenge: Sandboxing**

root
system call
Application
OS Hardware
userspace kernelspace

**#BHUSA @BlackHatEvents**

**4 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 8

# **The Challenge: Sandboxing**

root
blocked!
system call
nobody
OS Hardware
Application
userspace kernelspace

**#BHUSA @BlackHatEvents**

**4 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 9

# **The Challenge: Container**

root
Application
nobody
Application OS
Application
userspace kernelspace

**#BHUSA @BlackHatEvents**

**5 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 10

# **The Challenge: Full Isolation**

nobody

**#BHUSA @BlackHatEvents**

**6 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 11

# **The Challenge: Full Isolation**

nobody

**#BHUSA @BlackHatEvents**

**6 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 12

# **The Challenge: Full Isolation**

nobody

**#BHUSA @BlackHatEvents**

**6 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 13

# **You can’t break out** . . .

**#BHUSA @BlackHatEvents**

**7 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 14

**~~You can’t break out~~** <u>. . .</u> **~~:~~ GhostWrite**

**#BHUSA @BlackHatEvents**

**8 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 15

**Who are we?**

**Fabian Thomas** PhD student @CISPA (Germany) **E-Mail** fabian.thomas@cispa.de **Web** fabianthomas.de **Twitter** @fth0mas

**#BHUSA @BlackHatEvents**

**9 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 16

**Who are we?**

**Lorenz Hetterich** PhD student @CISPA (Germany)

**E-Mail** lorenz.hetterich@cispa.de **Twitter** @hetterichlorenz

**#BHUSA @BlackHatEvents**

**10 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 17

# **Who are we?**

## **Research Group Schwarz**

- Research focus:

   - Hardware vulnerabilities

   - . . . from software

- Recent discoveries:

**#BHUSA @BlackHatEvents**

**11 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 18

# **~~Full Isolation:~~ GhostWrite**

nobody

**#BHUSA @BlackHatEvents**

**12 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 19

# **~~Full Isolation:~~ GhostWrite**

nobody

#BHUSA @BlackHatEvents

**12 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 20

# **~~Full Isolation:~~ GhostWrite**

# Software World

**#BHUSA @BlackHatEvents**

**13 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 21

# **~~Full Isolation:~~ GhostWrite**

# Software World

# Hardware World

**#BHUSA @BlackHatEvents**

**13 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 22

# **Memory Isolation**

A A
B
A
A
B
B A

**#BHUSA @BlackHatEvents**

**14 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 23

# **Memory Isolation**

A A
B
A
A
B
B A

**#BHUSA @BlackHatEvents**

**14 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 24

# **Memory Isolation**

A A
B
A
A
B
B A

**#BHUSA @BlackHatEvents**

**14 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 25

# **~~Memory Isolation:~~ GhostWrite**

A A
B
A
A
B
B A

**#BHUSA @BlackHatEvents**

**14 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 26

Memory Isolation: GhostWrite

A A
B
A
A
B
B A

**#BHUSA @BlackHatEvents**

**14 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 27

# **~~Memory Isolation:~~ GhostWrite**

A A
B
A
A
B
B A

**#BHUSA @BlackHatEvents**

**14 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 28

# **The Exploit**

mv t0, phys_addr vmv.v.x v0, value vsetvli zero, zero, e8, m1 vse128.v v0, 0(t0)

**#BHUSA @BlackHatEvents**

**15 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 29

# **The Exploit**

mv t0, phys_addr vmv.v.x v0, value vsetvli zero, zero, e8, m1 vse128.v v0, 0(t0)

**#BHUSA @BlackHatEvents**

**15 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 30

# **GhostWrite: Investigation**

## vse128.v v0, 0(t0)

t0 v0 v1 v2 v3 v4 v5
Spec 0x1000 R I S C - V

**#BHUSA @BlackHatEvents**

**16 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 31

# **GhostWrite: Investigation**

## vse128.v v0, 0(t0)

t0 v0 v1 v2 v3 v4 v5
Spec 0x1000 R I S C - V
0x1000

**#BHUSA @BlackHatEvents**

**16 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 32

# **GhostWrite: Investigation**

## vse128.v v0, 0(t0)

t0 v0 v1 v2 v3 v4 v5
Spec 0x1000 R I S C - V
0x1000
R

**#BHUSA @BlackHatEvents**

**16 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 33

# **GhostWrite: Investigation**

## vse128.v v0, 0(t0)

t0 v0 v1 v2 v3 v4 v5
Spec 0x1000 R I S C - V
0x1000
R I

**#BHUSA @BlackHatEvents**

**16 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 34

# **GhostWrite: Investigation**

## vse128.v v0, 0(t0)

t0 v0 v1 v2 v3 v4 v5
Spec 0x1000 R I S C - V
0x1000
R I S

**#BHUSA @BlackHatEvents**

**16 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 35

# **GhostWrite: Investigation**

## vse128.v v0, 0(t0)

t0 v0 v1 v2 v3 v4 v5
Spec 0x1000 R I S C - V
0x1000
R I S C

**#BHUSA @BlackHatEvents**

**16 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 36

# **GhostWrite: Investigation**

## vse128.v v0, 0(t0)

t0 v0 v1 v2 v3 v4 v5
Spec 0x1000 R I S C - V
0x1000
R I S C -

**#BHUSA @BlackHatEvents**

**16 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 37

# **GhostWrite: Investigation**

## vse128.v v0, 0(t0)

t0 v0 v1 v2 v3 v4 v5
Spec 0x1000 R I S C - V
0x1000
R I S C - V

**#BHUSA @BlackHatEvents**

**16 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 38

# **GhostWrite: Investigation**

## vse128.v v0, 0(t0)

t0 v0 v1 v2 v3 v4 v5
Spec 0x1000 R I S C - V
0x1000
R I S C - V

**#BHUSA @BlackHatEvents**

**16 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 39

# **GhostWrite: Vector Instructions**

vse128.v v0, 0(t0)
t0 v0 v1 v2
Spec 0x1000 RISC-V is a supe r cool CPU archi tecture!
0x1000

#BHUSA @BlackHatEvents

**17 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 40

# **GhostWrite: Vector Instructions**

vse128.v v0, 0(t0)

t0 v0 v1 v2
Spec 0x1000 RISC-V is a supe r cool CPU archi tecture!
0x1000
RISC-V is a supe

#BHUSA @BlackHatEvents

**17 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 41

# **GhostWrite: Vector Instructions**

vse128.v v0, 0(t0)
t0 v0 v1 v2
Spec 0x1000 RISC-V is a supe r cool CPU archi tecture!
0x1000
RISC-V is a supe r cool CPU archi

#BHUSA @BlackHatEvents

**17 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 42

# **GhostWrite: Vector Instructions**

vse128.v v0, 0(t0)
t0 v0 v1 v2
Spec 0x1000 RISC-V is a supe r cool CPU archi tecture!
0x1000
RISC-V is a supe r cool CPU archi tecture!

#BHUSA @BlackHatEvents

**17 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 43

# **GhostWrite: Investigation**

t0 v0 v1 v2 v3 v4 v5
C910 0x1000 R I S C - V
0x1000

**#BHUSA @BlackHatEvents**

**18 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 44

# **GhostWrite: Investigation**

t0 v0 v1 v2 v3 v4 v5
C910 0x1000 R I S C - V
0x1000
B H U S 2 4

**#BHUSA @BlackHatEvents**

**18 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 45

# **GhostWrite: Investigation**

## vse128.v v0, 0(t0)

t0 v0 v1 v2 v3 v4 v5
C910 0x1000 R I S C - V
0x1000
B H U S 2 4

**#BHUSA @BlackHatEvents**

**18 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 46

# **GhostWrite: Virtual Memory**

A A
B
A
A
A

**#BHUSA @BlackHatEvents**

**19 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 47

# **GhostWrite: Virtual Memory**

physical
A A
B
A
A
A

**#BHUSA @BlackHatEvents**

**19 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 48

# **GhostWrite: Virtual Memory**

virtual physical
A A
page 1 B
A
A
A

**#BHUSA @BlackHatEvents**

**19 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 49

# **GhostWrite: Virtual Memory**

virtual physical
A A
page 1 B
A
A
A

**#BHUSA @BlackHatEvents**

**19 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 50

# **GhostWrite: Virtual Memory**

virtual physical
A A
page 1 B
A
A
A

**#BHUSA @BlackHatEvents**

**19 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 51

# **GhostWrite: Virtual Memory**

virtual physical
A A
page 1 B
A
A
A

**#BHUSA @BlackHatEvents**

**19 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 52

# **GhostWrite: Investigation**

t0 v0 v1 v2 v3 v4 v5
C910 0x1000 R I S C - V
0x1000
physical B H U S 2 4

**#BHUSA @BlackHatEvents**

**20 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 53

# **GhostWrite: Investigation**

## vse128.v v0, 0(t0)

t0 v0 v1 v2 v3 v4 v5
C910 0x1000 R I S C - V
0x1000
physical V H U S 2 4

**#BHUSA @BlackHatEvents**

**20 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 54

# **GhostWrite: Investigation**

## vse128.v v0, 0(t0)

t0 v0 v1 v2 v3 v4 v5
C910 0x1000 R I S C - V
0x1000
physical R H U S 2 4

**#BHUSA @BlackHatEvents**

**20 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 55

# **GhostWrite: Investigation**

## vse128.v v0, 0(t0)

t0 v0 v1 v2 v3 v4 v5
C910 0x1000 R I S C - V
0x1000
physical I H U S 2 4

**#BHUSA @BlackHatEvents**

**20 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 56

# **GhostWrite: Investigation**

vse128.v v0, 0(t0)

t0 v0 v1 v2 v3 v4 v5
C910 0x1000 R I S C - V
0x1000
physical S H U S 2 4

**#BHUSA @BlackHatEvents**

**20 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 57

# **GhostWrite: Investigation**

vse128.v v0, 0(t0)

t0 v0 v1 v2 v3 v4 v5
C910 0x1000 R I S C - V
0x1000
physical C H U S 2 4

**#BHUSA @BlackHatEvents**

**20 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 58

# **GhostWrite: Investigation**

## vse128.v v0, 0(t0)

t0 v0 v1 v2 v3 v4 v5
C910 0x1000 R I S C - V
0x1000
physical - H U S 2 4

**#BHUSA @BlackHatEvents**

**20 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 59

# **GhostWrite: Investigation**

## vse128.v v0, 0(t0)

t0 v0 v1 v2 v3 v4 v5
C910 0x1000 R I S C - V
0x1000
physical V H U S 2 4

**#BHUSA @BlackHatEvents**

**20 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 60

# **Is every system vulnerable?**

**#BHUSA @BlackHatEvents**

**21 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 61

**Is every system vulnerable?**

x86

**#BHUSA @BlackHatEvents**

**22 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 62

**Is every system vulnerable?**

x86

**#BHUSA @BlackHatEvents**

**22 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 63

# **T-Head XuanTie C910**

- one of the fastest RISC-V CPUs

**#BHUSA @BlackHatEvents**

**23 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 64

# **T-Head XuanTie C910**

- one of the fastest RISC-V CPUs

- 4 cores, 2GHz, vector extension

**#BHUSA @BlackHatEvents**

**23 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 65

# **T-Head XuanTie C910**

- one of the fastest RISC-V CPUs

- 4 cores, 2GHz, vector extension

- available in the cloud

**#BHUSA @BlackHatEvents**

**23 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 66

# **T-Head XuanTie C910**

- one of the fastest RISC-V CPUs

- 4 cores, 2GHz, vector extension

- available in the cloud

- available in laptops

**#BHUSA @BlackHatEvents**

**23 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 67

Instruction Set Architecture (ISA)

Specifies behavior

**#BHUSA @BlackHatEvents**

**24 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 68

# **Instruction Set Architecture (ISA)**

Specifies behavior Defines legal programs

**#BHUSA @BlackHatEvents**

**24 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 69

# **Instruction Set Architecture (ISA)**

Specifies behavior Defines legal programs

Licensing fees

**#BHUSA @BlackHatEvents**

**24 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 70

**Instruction Set Architecture (ISA)**

Specifies behavior Defines legal programs

Licensing fees

Limited customization

**#BHUSA @BlackHatEvents**

**24 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 71

# **RISC-V**

## open, community-driven

**#BHUSA @BlackHatEvents**

**25 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 72

# **RISC-V**

open, community-driven

no licensing fees

**#BHUSA @BlackHatEvents**

**25 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 73

# **RISC-V**

open, community-driven

no licensing fees

well designed

**#BHUSA @BlackHatEvents**

**25 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 74

**RISC-V**

open, community-driven

well designed

no licensing fees

extensible

**#BHUSA @BlackHatEvents**

**25 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 75

# **Software Fuzzing**

**#BHUSA @BlackHatEvents**

**26 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 76

Software Fuzzing

01011010011110100101

**#BHUSA @BlackHatEvents**

**26 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 77

Software Fuzzing

01001010010101010101

**#BHUSA @BlackHatEvents**

**26 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 78

Software Fuzzing

10101010010101101111

**#BHUSA @BlackHatEvents**

**26 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 79

Software Fuzzing

00000001101010100101

**#BHUSA @BlackHatEvents**

**26 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 80

# **Hardware Fuzzing**

**#BHUSA @BlackHatEvents**

**27 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 81

Hardware Fuzzing

01011010011110100101

**#BHUSA @BlackHatEvents**

**27 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 82

Hardware Fuzzing

01001010010101010101

**#BHUSA @BlackHatEvents**

**27 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 83

Hardware Fuzzing

10101010010101101111

**#BHUSA @BlackHatEvents**

**27 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 84

# **Hardware Fuzzing**

00000001101010100101

**#BHUSA @BlackHatEvents**

**27 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 85

# **Differential Fuzzing**

**#BHUSA @BlackHatEvents**

**28 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 86

# **Differential Fuzzing**

01011010011110100101

**#BHUSA @BlackHatEvents**

**28 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 87

# **Differential Fuzzing**

01011010011110100101

a=3
b=7

a=3
b=7

**#BHUSA @BlackHatEvents**

**28 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 88

# **Differential Fuzzing**

01001010010101010101

a=21
b=2

a=21
b=2

**#BHUSA @BlackHatEvents**

**28 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 89

# **Differential Fuzzing**

10101010010101101111

a=34
b=9

a=34
b=9

**#BHUSA @BlackHatEvents**

**28 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 90

# **Differential Fuzzing**

00000001101010100101

a=42
b=5

a=142
b=5

**#BHUSA @BlackHatEvents**

**28 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 91

# **Differential Fuzzing**

fadd f3, f4, f4
li x1, 42
x1: 0

**#BHUSA @BlackHatEvents**

**28 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 92

# **Let’s start fuzzing!**

**#BHUSA @BlackHatEvents**

**29 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 93

# **C908 and C906**

**#BHUSA @BlackHatEvents**

**30 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 94

**Demo: Freezing the C906**

**#BHUSA @BlackHatEvents**

**31 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 95

# **How to fix Hardware Bugs?**

disable vector
extension

**#BHUSA @BlackHatEvents**

**32 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 96

# **How to fix Hardware Bugs?**

disable vector
extension

**#BHUSA @BlackHatEvents**

**32 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 97

# **How to fix Hardware Bugs?**

disable vector
extension

**#BHUSA @BlackHatEvents**

**32 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 98

# **How to fix Hardware Bugs?**

disable vector
extension

**#BHUSA @BlackHatEvents**

**32 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 99

# **How to fix Hardware Bugs?**

disable vector
v1
extension
microcode

**#BHUSA @BlackHatEvents**

**32 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 100

# **How to fix Hardware Bugs?**

disable vector
v1
extension
microcode

**#BHUSA @BlackHatEvents**

**32 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 101

# **How to fix Hardware Bugs?**

disable vector
v2
extension
microcode

**#BHUSA @BlackHatEvents**

**32 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 102

# **How to fix Hardware Bugs?**

**#BHUSA @BlackHatEvents**

**33 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 103

**How to fix Hardware Bugs?**

disable vector extension

**#BHUSA @BlackHatEvents**

**33 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 104

**How to fix Hardware Bugs?**

OS

**#BHUSA @BlackHatEvents**

**33 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 105

# **How to fix Hardware Bugs?**

## disable vector

## extension

OS

**#BHUSA @BlackHatEvents**

**33 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 106

**How to fix Hardware Bugs?**

OS: disable extension

**#BHUSA @BlackHatEvents**

**34 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 107

**How to fix Hardware Bugs?**

OS: disable extension up to 33% overhead lose ∼ 50% instructions

**#BHUSA @BlackHatEvents**

**34 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 108

**How to fix Hardware Bugs?**

OS: disable extension up to 33% overhead lose ∼ 50% instructions

**#BHUSA @BlackHatEvents**

**35 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 109

**How to fix Hardware Bugs?**

OS: disable extension OS: disable extension up to 33% overhead lose ∼ 50% instructions

**#BHUSA @BlackHatEvents**

**35 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 110

**How to fix Hardware Bugs?**

OS: disable extension OS: disable extension up to 33% overhead up to 77% overhead lose ∼ 50% instructions lose ∼ 50% instructions

**#BHUSA @BlackHatEvents**

**35 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 111

**How to fix Hardware Bugs?**

OS: disable extension OS: disable extension up to 33% overhead up to 77% overhead lose ∼ 50% instructions lose ∼ 50% instructions

**#BHUSA @BlackHatEvents**

**35 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 112

**How to fix Hardware Bugs?**

OS: disable extension OS: disable extension no mitigation up to 33% overhead up to 77% overhead lose ∼ 50% instructions lose ∼ 50% instructions

**#BHUSA @BlackHatEvents**

**35 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 113

# **How to the fix C906?**

C906

**#BHUSA @BlackHatEvents**

**36 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 114

# **Reading Arbitrary Memory**

virtual physical
A A
page 1 B
A
A
A

**#BHUSA @BlackHatEvents**

**37 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 115

# **Reading Arbitrary Memory**

virtual physical
A A
page ✓1 2 B
A
A
A

**#BHUSA @BlackHatEvents**

**37 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 116

# **Reading Arbitrary Memory**

virtual physical
A A
page ✓1 2 B
A
A
A

**#BHUSA @BlackHatEvents**

**37 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 117

**Demo: Reading Arbitrary Memory**

**#BHUSA @BlackHatEvents**

**38 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 118

Getting root

if kernel_get_user() is not root then require_authentication() start_root_shell()

kernel_get_user: process = get_current_process() user = user_for_process(process) return user OS

**#BHUSA @BlackHatEvents**

**39 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 119

Getting root
if kernel_get_user() is not root then
require_authentication()
start_root_shell()
syscall
kernel_get_user:
process = get_current_process()
user = user_for_process(process)
return user
OS

**#BHUSA @BlackHatEvents**

**39 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 120

Getting root
if kernel_get_user() is not root then
require_authentication()
start_root_shell()
syscall
kernel_get_user:
process = get_current_process()
user = user_for_process(process)
return root
OS

**#BHUSA @BlackHatEvents**

**39 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 121

# **Getting root: Patching the Kernel**

virtual
A A
page 1
A
A
A
OS

**#BHUSA @BlackHatEvents**

**40 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 122

**Demo: Getting root**

**#BHUSA @BlackHatEvents**

**41 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 123

# **Is GhostWrite the only bug?**

**#BHUSA @BlackHatEvents**

**42 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 124

# **Is GhostWrite the only bug?**

**#BHUSA @BlackHatEvents**

**42 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 125

# **GhostWrite: The Big Picture**

Hardware Software
read
write

**#BHUSA @BlackHatEvents**

**43 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 126

# **GhostWrite: The Big Picture**

Hardware Software
read
write

**#BHUSA @BlackHatEvents**

**43 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 127

# **GhostWrite: The Big Picture**

Hardware Software
read
BH13,17
write

**#BHUSA @BlackHatEvents**

**43 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 128

# **GhostWrite: The Big Picture**

Hardware Software
read
BH13,17
write

**#BHUSA @BlackHatEvents**

**43 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 129

# **GhostWrite: The Big Picture**

Hardware Software
read
BH13,17
write
BH15,19

**#BHUSA @BlackHatEvents**

**43 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 130

# **GhostWrite: The Big Picture**

Hardware Software
read
BH13,17
write
BH15,19

**#BHUSA @BlackHatEvents**

**43 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 131

# **GhostWrite: The Big Picture**

Hardware Software
read
BH16,17
BH13,17
write
BH15,19

**#BHUSA @BlackHatEvents**

**43 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 132

# **GhostWrite: The Big Picture**

Hardware Software
read
BH16,17
BH13,17
write
BH15,19

**#BHUSA @BlackHatEvents**

**43 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 133

# **GhostWrite: The Big Picture**

Hardware Software
read
BH16,17
BH13,17
write
BH15
BH15,19

**#BHUSA @BlackHatEvents**

**43 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 134

# **GhostWrite: The Big Picture**

Hardware Software
read
BH16,17
BH13,17
write
BH15
BH15,19

**#BHUSA @BlackHatEvents**

**43 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 135

# **GhostWrite: The Big Picture**

Hardware Software
read restricted
BH16,17
BH13,17
write
BH15
BH15,19

**#BHUSA @BlackHatEvents**

**43 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 136

# **GhostWrite: The Big Picture**

Hardware Software
read restricted
BH16,17
BH13,17
write
BH15
BH15,19

**#BHUSA @BlackHatEvents**

**43 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 137

# **GhostWrite: The Big Picture**

Hardware Software
read restricted
BH16,17
BH13,17 BH18
write
BH15
BH15,19

**#BHUSA @BlackHatEvents**

**43 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 138

# **GhostWrite: The Big Picture**

Hardware Software
read restricted
BH16,17
BH13,17 BH18
write
BH15
BH15,19

**#BHUSA @BlackHatEvents**

**43 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 139

# **GhostWrite: The Big Picture**

Hardware Software
read restricted
BH16,17
BH13,17 BH18 BH23
write
BH15
BH15,19

**#BHUSA @BlackHatEvents**

**43 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 140

# **GhostWrite: The Big Picture**

Hardware Software
read restricted
BH16,17
BH13,17 BH18 BH23
write restricted
BH15
BH15,19

**#BHUSA @BlackHatEvents**

**43 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 141

# **GhostWrite: The Big Picture**

Hardware Software
read restricted
BH16,17
BH13,17 BH18 BH23
write restricted
BH15
BH15,19

**#BHUSA @BlackHatEvents**

**43 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 142

# **GhostWrite: Comparison**

Rowhammer CacheWarp GhostWrite
Restrictions bit flips
Speed
Practicality

**#BHUSA @BlackHatEvents**

**44 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 143

# **GhostWrite: Comparison**

Rowhammer CacheWarp GhostWrite
Restrictions bit flips old state
Speed
Practicality

**#BHUSA @BlackHatEvents**

**44 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 144

# **GhostWrite: Comparison**

Rowhammer CacheWarp GhostWrite
Restrictions bit flips old state –
Speed
Practicality

**#BHUSA @BlackHatEvents**

**44 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 145

# **What can we learn?**

## RISC-V is great

**#BHUSA @BlackHatEvents**

**45 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 146

# **What can we learn?**

RISC-V is great

Only C910

**#BHUSA @BlackHatEvents**

**45 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 147

# **What can we learn?**

RISC-V is great

Only C910

## Quality control important

**#BHUSA @BlackHatEvents**

**45 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 148

# **What can we learn?**

RISC-V is great

Only C910

Quality control important Configurable hardware

**#BHUSA @BlackHatEvents**

**45 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 149

# **GhostWrite: Overview**

ghostwriteattack.com

Microarchitecture Vulnerabilities: Past, Present, and Future

**#BHUSA @BlackHatEvents**

**46 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 150

# **The End: GhostWrite**

- GhostWrite destroys all isolations on C910 RISC-V CPU

@fth0mas @hetterichlorenz

ghostwriteattack.com

**#BHUSA @BlackHatEvents**

**47 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 151

# **The End: GhostWrite**

- GhostWrite destroys all isolations on C910 RISC-V CPU

- Mitigation: disable vector extension, up to 33% overhead

@fth0mas @hetterichlorenz

ghostwriteattack.com

**#BHUSA @BlackHatEvents**

**47 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 152

# **The End: GhostWrite**

- GhostWrite destroys all isolations on C910 RISC-V CPU

- Mitigation: disable vector extension, up to 33% overhead

- Hardware bugs are everywhere

@fth0mas @hetterichlorenz

ghostwriteattack.com

**#BHUSA @BlackHatEvents**

**47 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 153

# **GhostWrite: The Framework**

generate input
vsetvli x0, x0, ...
vse128.v t0, 0(t0)
li x1, 42
x1: 0

**#BHUSA @BlackHatEvents**

**48 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 154

# **GhostWrite: The Framework**

generate input C906
vsetvli x0, x0, ...
vse128.v t0, 0(t0)
li x1, 42 distribute
x1: 0
C910

**#BHUSA @BlackHatEvents**

**48 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 155

# **GhostWrite: The Framework**

generate input C906
vsetvli x0, x0, ...
SIGSEGV
vse128.v t0, 0(t0)
x1: 0
li x1, 42 distribute collect
OK
x1: 42
x1: 0
C910

**#BHUSA @BlackHatEvents**

**48 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 156

# **GhostWrite: The Framework**

generate input C906
vsetvli x0, x0, ...
SIGSEGV
vse128.v t0, 0(t0)
x1: 0
li x1, 42 distribute collect
OK
x1: 42
x1: 0
if diff,
C910 log reproducer

**#BHUSA @BlackHatEvents**

**48 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**

## Slide 157

GhostWrite: The Framework

generate input C906
instr seq:
vsetvli x0, x0, ...
SIGSEGV vsetvli x0, x0, ...
vse128.v t0, 0(t0)
x1: 0 vse128.v t0, 0(t0)
li x1, 42 distribute collect
OK li x1, 42
x1: 42 regs:
x1: 0
if diff, x1: 0
C910 log reproducer

**#BHUSA @BlackHatEvents**

**48 Arbitrary Data Manipulation and Leakage with CPU Zero-Day Bugs on RISC-V**
