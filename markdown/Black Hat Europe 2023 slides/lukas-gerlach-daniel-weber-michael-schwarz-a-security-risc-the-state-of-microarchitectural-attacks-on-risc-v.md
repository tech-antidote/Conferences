---
title: "A Security RISC The State of Microarchitectural Attacks on RISC-V"
speakers: ["Lukas Gerlach", "Daniel Weber", "Michael Schwarz"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2023"
edition: "Europe"
year: 2023
source_pdf: "Black Hat Europe 2023 slides/Lukas Gerlach, Daniel Weber, Michael Schwarz_A Security RISC The State of Microarchitectural Attacks on RISC-V.pdf"
pages: 209
sha256: "745f4a12675f4ae90f533f97f86126779e87d204543a04b87259db2b9ab0ee39"
text_chars: 44005
ocr_pages: 7
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:14:52Z"
---
# A Security RISC The State of Microarchitectural Attacks on RISC-V

**Speakers:** Lukas Gerlach, Daniel Weber, Michael Schwarz  
**Conference:** Black Hat Europe 2023  
**Source:** `Black Hat Europe 2023 slides/Lukas Gerlach, Daniel Weber, Michael Schwarz_A Security RISC The State of Microarchitectural Attacks on RISC-V.pdf` (209 pages)


## Slide 1

**A Security RISC?** The State of Microarchitectural Attacks on RISC-V **Lukas Gerlach** , **Daniel Weber** , Michael Schwarz | BlackHat EU 2023

1

## Slide 2

#### **Agenda**

2 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 3

#### **Agenda**

###### **CPU Security**

###### **Basics**

2 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 4

#### **Agenda**

###### **CPU Security Basics**

###### **Learn about existing Attacks**

2 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 5

#### **Agenda**

###### **CPU Security Basics**

**Learn about existing Attacks**

**Investigate RISC-V Security**

2 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 6

#### **Who are we?**

##### **RootSec**

###### **Research Group @ CISPA**

Helmholtz Center for Information Security

3 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 7

#### **Who are we?**

RootSec

Research Group
@
CISPA
Helmholtz Center for
Information Security

Lukas Gerlach
PhD Student

3 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 8

#### **Who are we?**

RootSec

Research Group
@
Lukas Gerlach
CISPA
PhD Student
Helmholtz Center for
Information Security

Daniel Weber
PhD Student

3 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 9

#### **Who are we?**

RootSec

**Research Group @ Lukas Gerlach CISPA** PhD Student Helmholtz Center for Information Security

Daniel Weber Michael Schwarz
PhD Student Faculty

3 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 10

#### **Why do we Care about CPU Security?**

4 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 11

## **Live Demo**

5 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 12

6 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
eee demo@!ab24: ~/ademos Aa!
demo@Lab24:~/demos$ ./leak
Calibrating Threshold
Cache hit timing: 5, Cache miss timing: 150
Threshold is: 101
```

## Slide 13

#### **Why do We Care about CPU Security?**

7 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 14

#### **Why do We Care about CPU Security?**

###### • **CPU vulnerabilities can leak or spy on…**

7 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 15

#### **Why do We Care about CPU Security?**

###### • **CPU vulnerabilities can leak or spy on…**

− … cryptographic keys.

7 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 16

#### **Why do We Care about CPU Security?**

###### • **CPU vulnerabilities can leak or spy on…**

- … cryptographic keys.

- … browser cookies.

7 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 17

#### **Why do We Care about CPU Security?**

###### • **CPU vulnerabilities can leak or spy on…**

- … cryptographic keys.

- … browser cookies.

- … (almost) arbitrary memory.

7 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 18

#### **Why do We Care about CPU Security?**

###### • **CPU vulnerabilities can leak or spy on…**

   - … cryptographic keys.

   - … browser cookies.

   - … (almost) arbitrary memory.

- **CPU vulnerabilities can attack…**

7 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 19

#### **Why do We Care about CPU Security?**

###### • **CPU vulnerabilities can leak or spy on…**

   - … cryptographic keys.

   - … browser cookies.

   - … (almost) arbitrary memory.

- **CPU vulnerabilities can attack…**

   - … the kernel.

7 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 20

#### **Why do We Care about CPU Security?**

###### • **CPU vulnerabilities can leak or spy on…**

   - … cryptographic keys.

   - … browser cookies.

   - … (almost) arbitrary memory.

- **CPU vulnerabilities can attack…**

   - … the kernel.

- … the browser (from within JavaScript).

7 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 21

#### **Why do We Care about CPU Security?**

###### • **CPU vulnerabilities can leak or spy on…**

   - … cryptographic keys.

   - … browser cookies.

   - … (almost) arbitrary memory.

- **CPU vulnerabilities can attack…**

   - … the kernel.

- … the browser (from within JavaScript).

- … virtual machines.

7 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 22

#### **Why do We Care about CPU security?**

8 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 23

#### **Why do We Care about CPU security?**

8 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 24

#### **Why do We Care about CPU security?**

8 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 25

#### **Why do We Care about CPU security?**

8 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 26

#### **Why do We Care about CPU security?**

8 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 27

#### **Why do We Care about CPU security?**

8 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 28

#### **Why do We Care about CPU security?**

8 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 29

#### **Why do We Care about CPU security?**

8 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
€ Why do We Care about CPU security?
PLUNDER
VO_T
8 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz
```

## Slide 30

#### **Why do We Care about CPU security?**

8 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
€ Why do We Care about CPU security?
ya
akage
Qe Al
PLUNDER
VO_T
8 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz
```

## Slide 31

#### **Why do We Care about CPU security?**

8 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
€ Why do We Care about CPU security?
Qe Al
PLUNDER
VO_T
iLeakage
8 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz
```

## Slide 32

#### **Why do We Care about CPU security?**

8 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
€ Why do We Care about CPU security?
Qe Al
PLUNDER
VO_T
iLe
8 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz
```

## Slide 33

#### **Different Vulnerabilities, Different Attacks**

9 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 34

#### **Different Vulnerabilities, Different Attacks**

###### • **Leaking Secrets:**

9 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 35

#### **Different Vulnerabilities, Different Attacks**

###### • **Leaking Secrets:**

− Spectre

9 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 36

#### **Different Vulnerabilities, Different Attacks**

###### • **Leaking Secrets:**

- Spectre

- Meltdown

9 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 37

#### **Different Vulnerabilities, Different Attacks**

###### • **Leaking Secrets:**

− Spectre

- Meltdown

− MDS

- …

9 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 38

#### **Different Vulnerabilities, Different Attacks**

###### • **Leaking Secrets:**

   - Spectre

   - Meltdown

   - MDS

   - …

- **Tampering with Data:**

9 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 39

#### **Different Vulnerabilities, Different Attacks**

###### • **Leaking Secrets:**

   - Spectre

   - Meltdown

   - MDS

   - …

- **Tampering with Data:** − PlunderVolt

9 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 40

#### **Different Vulnerabilities, Different Attacks**

###### • **Leaking Secrets:**

   - Spectre

   - Meltdown

   - MDS

   - …

- **Tampering with Data:** − PlunderVolt

   - CacheWarp

- …

9 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 41

#### **Only Intel and AMD CPUs?**

10 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 42

#### **Only Intel and AMD CPUs? What about the Others?**

10 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 43

#### **Other Architectures? ARM?**

11 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 44

#### **Other Architectures? ARM?**

###### • **Demonstrated attacks** include:

11 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 45

#### **Other Architectures? ARM?**

###### • **Demonstrated attacks** include:

###### − **Cache** attacks

11 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 46

#### **Other Architectures? ARM?**

###### • **Demonstrated attacks** include:

- **Cache** attacks

- **Spectre**

11 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 47

#### **Other Architectures? ARM?**

###### • **Demonstrated attacks** include:

- **Cache** attacks

- **Spectre**

- Some **Meltdown** Variants

11 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 48

#### **Other Architectures? ARM?**

###### • **Demonstrated attacks** include:

- **Cache** attacks

- **Spectre**

- Some **Meltdown** Variants

− …

11 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 49

#### **Other Architectures? ARM?**

###### • **Demonstrated attacks** include:

- **Cache** attacks

- **Spectre**

- Some **Meltdown** Variants

− …

##### **ARM is also vulnerable**

11 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 50

#### **There is another!**

12 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 51

#### **RISC-V: The New Star on the Horizon**

13 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 52

#### **RISC-V: The New Star on the Horizon**

###### • New **Instruction Set Architecture** (ISA)

13 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 53

#### **RISC-V: The New Star on the Horizon**

- New **Instruction Set Architecture** (ISA)

###### • **Open-Source** Standard

13 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 54

#### **RISC-V: The New Star on the Horizon**

- New **Instruction Set Architecture** (ISA)

- **Open-Source** Standard

   - White-box bug hunting

13 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 55

#### **RISC-V: The New Star on the Horizon**

- New **Instruction Set Architecture** (ISA)

- **Open-Source** Standard

   - White-box bug hunting

   - Testing of hardware mitigations

13 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 56

#### **RISC-V: The New Star on the Horizon**

- New **Instruction Set Architecture** (ISA)

- **Open-Source** Standard

   - White-box bug hunting

   - Testing of hardware mitigations

- Lots of **academic research**

13 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 57

#### **Is RISC-V just another Academia Thingy?**

14 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 58

#### **You Can Buy RISC-V Cores!**

15 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 59

#### **You Can Buy RISC-V Cores!**

### **Now available in Hardware**

15 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 60

#### **You Can Buy RISC-V Cores!**

##### **Allwinner D1 (C906)**

### **Now available in Hardware**

15 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 61

#### **You Can Buy RISC-V Cores!**

##### **Allwinner D1 (C906)**

##### **SiFive U74**

### **Now available in Hardware**

15 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 62

#### **RISC-V is Coming**

16 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 63

#### **RISC-V is Coming**

##### **_62.4 billion_** _RISC-V cores predicted to be running_ **_by 2025_**

16 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 64

#### **RISC-V is Coming**

##### **_62.4 billion_** _RISC-V cores predicted to be running_ **_by 2025_** _RISE Project by major vendors (_ **_Google_** _,_ **_Qualcomm_** _,_ **_Samsung_** _, …)_

16 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 65

#### **But Security?**

17 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 66

#### **But Security?**

# **Security?**

17 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 67

#### **But Security?**

**Security?** _What is the_ **_status quo_** _on_ **_hardware RISC-V processors_** _?_

17 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 68

#### **Let’s Investigate RISC-V…**

18 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 69

#### **Let’s Investigate RISC-V…**

###### • **Did we learn from the past** ?

18 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 70

#### **Let’s Investigate RISC-V…**

###### • **Did we learn from the past** ?

− **Are these CPUs hardened** against known attacks?

18 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 71

#### **Let’s Investigate RISC-V…**

###### • **Did we learn from the past** ?

- **Are these CPUs hardened** against known attacks?

- **Do academic mitigations make it** into production CPUs?

18 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 72

#### **Let’s Investigate RISC-V…**

- **Did we learn from the past** ?

   - **Are these CPUs hardened** against known attacks?

   - **Do academic mitigations make it** into production CPUs?

- Does **open-source imply better or worse** security?

18 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 73

#### **Let’s Investigate RISC-V…**

- **Did we learn from the past** ?

   - **Are these CPUs hardened** against known attacks?

   - **Do academic mitigations make it** into production CPUs?

##### • Does **open-source imply better or worse** security? **Let’s analyze the C906 and U74!**

18 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 74

#### **How Does a CPU Work?**

L1 I-Cache
BPU
Decoder / Register Read
Execution  Data
units Caches

19 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 75

#### **How Does a CPU Work?**

1. Fetch instruction from memory

L1 I-Cache
BPU
Decoder / Register Read
Execution  Data
units Caches

19 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 76

#### **How Does a CPU Work?**

1. Fetch instruction from memory

2. Decode instruction and decide what to do

L1 I-Cache
BPU
Decoder / Register Read
Execution  Data
units Caches

19 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 77

#### **How Does a CPU Work?**

1. Fetch instruction from memory

2. Decode instruction and decide what to do

3. Execute the instruction

L1 I-Cache
BPU

Decoder / Register Read
Execution  Data
units Caches

19 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 78

#### **How Does a CPU Work?**

1. Fetch instruction from memory

2. Decode instruction and decide what to do

3. Execute the instruction

4. Write back the results to memory

L1 I-Cache
BPU

Decoder / Register Read
Execution  Data
units Caches

19 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 79

#### **What Type of Attacks are There?**

L1 I-Cache
BPU
Decoder / Register Read
Execution  Data
units Caches

20 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 80

#### **What Type of Attacks are There?**

###### • Attack **timing differences** in caches and predictors

L1 I-Cache
BPU
Decoder / Register Read
Execution  Data
units Caches

20 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 81

#### **What Type of Attacks are There?**

- Attack **timing differences** in caches and predictors

− Flush+Reload, Prime+Probe

Prime+Probe
L1 I-Cache
BPU
Decoder / Register Read
Execution  Data
units Caches
Prime+Probe

20 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 82

#### **What Type of Attacks are There?**

- Attack **timing differences** in caches and predictors

− Flush+Reload, Prime+Probe

Flush+Reload
L1 I-Cache
BPU
Decoder / Register Read
Execution  Data
units Caches
Flush+Reload

20 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 83

#### **What Type of Attacks are There?**

- Attack **timing differences** in caches and predictors

− Flush+Reload, Prime+Probe

- Exploiting **implementation bugs**

L1 I-Cache
BPU
Decoder / Register Read
Execution  Data
units Caches

20 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 84

#### **What Type of Attacks are There?**

- Attack **timing differences** in caches and predictors

   - Flush+Reload, Prime+Probe

- Exploiting **implementation bugs**

- Abusing **physical properties**

   - Rowhammer

   - Power Analysis

L1 I-Cache
BPU
Decoder / Register Read
Execution  Data
units Caches
Power Analysis

20 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 85

#### **Let’s start with our first attack!**

21 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 86

#### **CPU Design: Flush+Reload**

Flush+Reload
L1 I-Cache
BPU
Decoder / Register Read
Execution
Data Caches
units

22 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 87

#### **CPU Optimization: The Cache**

```
access(array[0]);
access(array[0]);
```

###### **CPU Cache**

**DRAM**

23 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 88

#### **CPU Optimization: The Cache**

Cache Miss

```
access(array[0]);
access(array[0]);
```

###### **CPU Cache**

**DRAM**

23 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 89

#### **CPU Optimization: The Cache**

Cache Miss

```
access(array[0]);
access(array[0]);
```

CPU Cache

Request

**DRAM**

23 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 90

#### **CPU Optimization: The Cache**

Cache Miss

```
access(array[0]);
access(array[0]);
```

CPU Cache

Request
Response

**DRAM**

23 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 91

#### **CPU Optimization: The Cache**

Request
Response
0x1337
CPU Cache

Cache Miss

```
access(array[0]);
access(array[0]);
```

**DRAM**

23 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 92

#### **CPU Optimization: The Cache**

Cache Miss Request
Cache Hit Response
0x1337
CPU Cache

```
access(array[0]);
access(array[0]);
```

**DRAM**

23 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 93

#### **CPU Optimization: The Cache**

###### DRAM access required  **Slow**

Cache Miss Request
Cache Hit Response
0x1337
CPU Cache

```
access(array[0]);
access(array[0]);
```

**DRAM**

23 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 94

#### **CPU Optimization: The Cache**

###### DRAM access required  **Slow**

Cache Miss Request
access(array[0]);
Cache Hit Response
access(array[0]); 0x1337
DRAM access skipped   Fast CPU Cache

**DRAM**

23 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 95

#### **Measuring Cache Timings**

24 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
€ Measuring Cache Timings
10*
rf m Cache hit
Bos ™ Cache miss
e)
O
©
qe 25
O
D
O 1.
E
>
Z
I ] ] ] | | t
O 100 200 300 400 500 600 ‘700 800 900 1,000 1,100 1,200
Measured access time (CPU cycles)
24 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz
```

## Slide 96

#### **Flush+Reload: Shared Memory**

Shared Memory
Shared
Attacker Victim

25 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 97

#### **Flush+Reload: Shared Memory**

Shared Memory
access(…)
Shared
Attacker Victim

25 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 98

#### **Flush+Reload: Shared Memory**

Shared Memory
access(…)
Shared
Attacker Victim

25 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 99

#### **Flush+Reload: Shared Memory**

Shared Memory
access(…)
Shared
Shared
Attacker Victim

25 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 100

#### **Flush+Reload: Shared Memory**

Shared Memory
access(…)
Shared
Shared
Attacker Victim

25 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 101

#### **Flush+Reload**

Shared Memory
Shared
Attacker Victim

26 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 102

#### **Flush+Reload**

Shared Memory
flush
Shared
Attacker Victim

26 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 103

#### **Flush+Reload**

Shared Memory
flush
Attacker

Victim

26 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 104

#### **Flush+Reload**

Shared Memory
flush
Attacker

access(…)
Victim

26 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 105

#### **Flush+Reload**

Shared Memory
flush
access(…)
Shared
Attacker Victim

26 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 106

#### **Flush+Reload**

Shared Memory
flush
Shared
access(…)
Attacker

access(…)
Victim

26 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 107

#### **Flush+Reload is Mitigated on RISC-V**

27 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 108

#### **Flush+Reload is Mitigated on RISC-V**

###### • Flush+Reload is typically used to **spy on control flow**

27 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 109

#### **Flush+Reload is Mitigated on RISC-V**

• Flush+Reload is typically used to **spy on control flow** − **Requires shared caches** for data and instructions

27 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 110

#### **Flush+Reload is Mitigated on RISC-V**

• Flush+Reload is typically used to **spy on control flow** − **Requires shared caches** for data and instructions

###### • The RISC-V cores have **split data and instruction caches**

27 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 111

#### **Flush+Reload is Mitigated on RISC-V**

- Flush+Reload is typically used to **spy on control flow** − **Requires shared caches** for data and instructions

- The RISC-V cores have **split data and instruction caches**

- Cache design **mitigates** Flush+Reload

27 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 112

#### **Flush+Reload is Mitigated on RISC-V**

• Flush+Reload is typically used to **spy on control flow** − **Requires shared caches** for data and instructions

- The RISC-V cores have **split data and instruction caches**

- Cache design **mitigates** Flush+Reload

###### **New Attack Variant: Flush+Fault**

27 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 113

#### **Flush+Fault**

###### Attacker

```
if(secret){
A();
} else {
B();
}
```

Victim

28 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 114

#### **Flush+Fault**

###### Attacker

###### I. Flush I-Cache with `fence.i`

if(secret){
A();
} else {
B();
}

Victim

28 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 115

#### **Flush+Fault**

###### Attacker

- I. Flush I-Cache with `fence.i`

II. Time jump to address containing victim cache line

```
if(secret){
A();
} else {
B();
}
```

**Victim**

28 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 116

#### **Flush+Fault**

###### Attacker

- I. Flush I-Cache with `fence.i`

- II. Time jump to address containing victim cache line

- III. Handle Fault

Fault handler

if(secret){
A();
} else {
B();
}

**Victim**

28 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 117

#### **Flush+Fault**

###### Attacker

- I. Flush I-Cache with `fence.i`

II. Time jump to address containing victim cache line

III. Handle Fault

Fault handler

if(secret){
A();
} else {
B();
}

**Victim**

IV. Timing of fault handling leaks secret

28 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 118

#### **Lesson Learned: Cache Attacks are Still Possible**

29 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 119

#### **Lesson Learned: Cache Attacks are Still Possible**

###### • The cache design **mitigates well-known attacks**

29 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 120

#### **Lesson Learned: Cache Attacks are Still Possible**

###### • The cache design **mitigates well-known attacks**

− e.g., Flush+Reload

29 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 121

#### **Lesson Learned: Cache Attacks are Still Possible**

###### • The cache design **mitigates well-known attacks**

   - e.g., Flush+Reload

- **Adaptions are still possible**

29 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 122

#### **Lesson Learned: Cache Attacks are Still Possible**

- The cache design **mitigates well-known attacks**

− e.g., Flush+Reload

- **Adaptions are still possible**

   - Flush+Fault

29 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 123

#### **Lesson Learned: Cache Attacks are Still Possible**

- The cache design **mitigates well-known attacks**

− e.g., Flush+Reload

- **Adaptions are still possible**

   - Flush+Fault

   - Data-cache Attacks

29 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 124

#### **Nice! But What About the Other Attacks?**

30 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 125

#### **CPU Design: Performance Counters**

L1 I-Cache
BPU
Decoder / Register Read
Execution units Data Caches
CycleDrift

31 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 126

#### **What are Performance Counters?**

CPUs are complex and hard to benchmark

32 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 127

#### **What are Performance Counters?**

CPUs are complex and hard to benchmark Performance Counters ease **benchmarking**

32 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 128

#### **What are Performance Counters?**

CPUs are complex and hard to benchmark Performance Counters ease **benchmarking**

• Performance Counters **count/report events** such as...

32 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 129

#### **What are Performance Counters?**

- CPUs are complex and hard to benchmark Performance Counters ease **benchmarking**

- • Performance Counters **count/report events** such as... − ... cache misses

32 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 130

#### **What are Performance Counters?**

CPUs are complex and hard to benchmark Performance Counters ease **benchmarking** • Performance Counters **count/report events** such as...

- ... cache misses

- ... instructions executed

32 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 131

#### **What are Performance Counters?**

CPUs are complex and hard to benchmark Performance Counters ease **benchmarking** • Performance Counters **count/report events** such as...

- ... cache misses

- ... instructions executed

- ... CPU Frequency

32 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 132

#### **Why are Performance Counters Dangerous?**

if(secret)
Performance
divide();
Counters
Attacker Shared Hardware Victim

33 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 133

#### **Why are Performance Counters Dangerous?**

if(secret)
Performance
Monitors
divide();
Counters
Attacker Shared Hardware Victim

33 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 134

#### **Why are Performance Counters Dangerous?**

if(secret)
Performance
Reads Monitors
divide();
Counters
Attacker Shared Hardware Victim

33 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 135

#### **Why are Performance Counters Dangerous?**

Inspects  if(secret)
Performance
Reads Monitors
"Branch Taken"
divide();
Counters
event
Attacker Shared Hardware Victim

33 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 136

#### **Why are Performance Counters Dangerous?**

Inspects  if(secret)
Performance
Reads Monitors
"Branch Taken"
divide();
Counters
event
Attacker Shared Hardware Victim
Fix:  Make the interface  privileged  ( root only )!

33 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 137

#### **What Happens on RISC-V?**

34 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 138

#### **What Happens on RISC-V?**

###### • Some Performance Counter are still **unprivileged** !

34 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 139

#### **What Happens on RISC-V?**

- Some Performance Counter are still **unprivileged** !

   - Dictated by the RISC-V ISA standard

34 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 140

#### **What Happens on RISC-V?**

- Some Performance Counter are still **unprivileged** !

   - Dictated by the RISC-V ISA standard

- Only few **unprivileged** events

34 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 141

#### **What Happens on RISC-V?**

- Some Performance Counter are still **unprivileged** !

   - Dictated by the RISC-V ISA standard

- Only few **unprivileged** events

   - No "Branch Taken" event!

34 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 142

#### **What Happens on RISC-V?**

- Some Performance Counter are still **unprivileged** !

   - Dictated by the RISC-V ISA standard

- Only few **unprivileged** events

   - No "Branch Taken" event!

- Existing Events:

34 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 143

#### **What Happens on RISC-V?**

- Some Performance Counter are still **unprivileged** !

   - Dictated by the RISC-V ISA standard

- Only few **unprivileged** events

   - No "Branch Taken" event!

- Existing Events:

   - Number of **CPU cycles elapsed**

34 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 144

#### **What Happens on RISC-V?**

- Some Performance Counter are still **unprivileged** !

   - Dictated by the RISC-V ISA standard

- Only few **unprivileged** events

   - No "Branch Taken" event!

- Existing Events:

   - Number of **CPU cycles elapsed**

   - Number of **Instructions executed**

A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

34

## Slide 145

#### **KASLR: Kernel Address Space Layout Randomization**

35 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 146

#### **KASLR: Kernel Address Space Layout Randomization**

• Kernel **exploits require** knowledge about **addresses**

35 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 147

#### **KASLR: Kernel Address Space Layout Randomization**

- Kernel **exploits require** knowledge about **addresses**

- **KASLR randomizes** the kernel **addresses** on boot

35 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 148

#### **KASLR: Kernel Address Space Layout Randomization**

- Kernel **exploits require** knowledge about **addresses**

- **KASLR randomizes** the kernel **addresses** on boot

**Can we break that maybe?**

35 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 149

## **Live Demo: CycleDrift**

36 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 150

37 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 151

#### **Lesson Learned: Perf Attacks are Still Possible**

38 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 152

#### **Lesson Learned: Perf Attacks are Still Possible**

• RISC-V cores have **unprivileged** performance counters

38 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 153

#### **Lesson Learned: Perf Attacks are Still Possible**

- RISC-V cores have **unprivileged** performance counters

- Performance counter **attacks are again possible** !

38 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 154

#### **Lesson Learned: Perf Attacks are Still Possible**

- RISC-V cores have **unprivileged** performance counters

- Performance counter **attacks are again possible** !

- More performance counters **will yield stronger attacks...**

38 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 155

#### **CPU Design: Spectre**

L1 I-Cache
BPU
Decoder / Register Read
Execution units Data Caches
Spectre

39 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 156

#### **CPU Optimization: Branch-Prediction-Unit (BPU)**

```
if(secret){
A();
}else{
B();
}
```

40 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 157

#### **CPU Optimization: Branch-Prediction-Unit (BPU)**

###### • **Branches** impact execution speed

```
if(secret){
A();
}else{
B();
}
```

40 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 158

#### **CPU Optimization: Branch-Prediction-Unit (BPU)**

- **Branches** impact execution speed

   - The CPU has to **wait for Branches**

###### **`if(secret){ A(); }else{ B(); }`**

40 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 159

#### **CPU Optimization: Branch-Prediction-Unit (BPU)**

- **Branches** impact execution speed

   - The CPU has to **wait for Branches**

   - Stalling slows down execution

###### **`if(secret){ A(); }else{ B(); }`**

40 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 160

#### **CPU Optimization: Branch-Prediction-Unit (BPU)**

- **Branches** impact execution speed

   - The CPU has to **wait for Branches**

   - Stalling slows down execution

•

• **Optimize by Prediction**

###### **`if(secret){ A(); }else{ B(); }`**

40 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 161

#### **CPU Optimization: Branch-Prediction-Unit (BPU)**

- **Branches** impact execution speed

   - The CPU has to **wait for Branches**

   - Stalling slows down execution

•

• **Optimize by Prediction**

- Look at history of last branches

```
if(secret){
A();
}else{
B();
}
```

40 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 162

#### **CPU Optimization: Branch-Prediction-Unit (BPU)**

- **Branches** impact execution speed

   - The CPU has to **wait for Branches**

− Stalling slows down execution

•

• **Optimize by Prediction**

- Look at history of last branches

```
if(secret){
A();
}else{
B();
}
```

- **Predict** which **branch direction** is taken next

40 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 163

#### **CPU Optimization: Branch-Prediction-Unit (BPU)**

- **Branches** impact execution speed

   - The CPU has to **wait for Branches**

   - Stalling slows down execution

•

• **Optimize by Prediction**

- Look at history of last branches

```
if(secret){
A();
}else{
B();
}
```

- **Predict** which **branch direction** is taken next

40 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 164

#### **CPU Optimization: Branch-Prediction-Unit (BPU)**

- **Branches** impact execution speed

   - The CPU has to **wait for Branches**

   - Stalling slows down execution

•

• **Optimize by Prediction**

- Look at history of last branches

```
if(secret){
A();
}else{
B();
}
```

- **Predict** which **branch direction** is taken next

40 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 165

#### **CPU Optimization: Speculative Execution**

41 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 166

#### **CPU Optimization: Speculative Execution**

###### • Why stop at predicting the branch?

41 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 167

#### **CPU Optimization: Speculative Execution**

- Why stop at predicting the branch?

- • Instead **execute** the **prediction**

41 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 168

#### **CPU Optimization: Speculative Execution**

- Why stop at predicting the branch?

- • Instead **execute** the **prediction**

- Two cases:

41 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 169

#### **CPU Optimization: Speculative Execution**

- Why stop at predicting the branch?

- Instead **execute** the **prediction**

- Two cases:

   - Correct prediction, we win

41 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 170

#### **CPU Optimization: Speculative Execution**

- Why stop at predicting the branch?

- Instead **execute** the **prediction**

- Two cases:

   - Correct prediction, we win

   - False prediction, **rollback** effects of branch

41 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 171

#### **Spectre?**

42 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 172

#### **Spectre?**

###### • Spectre **requires speculative execution**

42 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 173

#### **Spectre?**

- Spectre **requires speculative execution**

- **Our RISC-V CPUs:** No support for speculative execution **(yet...)**

42 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 174

#### **But there is speculative prefetching!**

43 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 175

#### **Cache+Time**

```
if(secret){
A();
}else{
B();
}
```

###### **Victim**

44 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 176

#### **Cache+Time**

• New **side channel** on the **instruction cache**

###### **`if(secret){ A(); }else{ B(); }`**

###### **Victim**

44 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 177

#### **Cache+Time**

- New **side channel** on the **instruction cache**

   - No shared memory

###### **`if(secret){ A(); }else{ B(); }`**

###### **Victim**

44 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 178

#### **Cache+Time**

- New **side channel** on the **instruction cache**

   - No shared memory

   - Cache-line granularity

```
if(secret){
A();
}else{
B();
}
```

###### **Victim**

44 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 179

#### **Cache+Time**

- New **side channel** on the **instruction cache**

   - No shared memory

   - Cache-line granularity

**`if(secret){ A(); }else{ B();`** } **`}`**

###### **Victim**

44 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 180

#### **Cache+Time**

- New **side channel** on the **instruction cache**

   - No shared memory

   - Cache-line granularity

```
if(secret){
A();
}else{
B();
}
```

###### **Victim**

44 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 181

#### **Cache+Time**

- New **side channel** on the **instruction cache**

   - No shared memory

   - Cache-line granularity

```
if(secret){
A();
}else{
B();
}
```

Victim

44 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 182

#### **Cache+Time**

- New **side channel** on the **instruction cache**

   - No shared memory

   - Cache-line granularity

```
if(secret){
A();
}else{
B();
}
```

Victim

44 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 183

#### **Cache+Time**

- New **side channel** on the **instruction cache**

   - No shared memory

   - Cache-line granularity

##### **Speculative prefetching is exploitable**

```
if(secret){
A();
}else{
B();
}
```

**Victim**

44 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 184

## **Surpise Demo: Spectre is fixed? Right?**

45 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 185

46 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
eee beagle@lab46: ~/specre-riscv X31
peagLe@Lab46: ~/specre-riscv$ A |
```

## Slide 186

#### **Lesson Learned: BPU Attacks Possible. Spectre also.**

47 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 187

#### **Lesson Learned: BPU Attacks Possible. Spectre also.**

###### • The limited speculation on C906 and U74 **mitigates well-known attacks**

47 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 188

#### **Lesson Learned: BPU Attacks Possible. Spectre also.**

- The limited speculation on C906 and U74 **mitigates well-known attacks**

   - e.g., Spectre

47 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 189

#### **Lesson Learned: BPU Attacks Possible. Spectre also.**

- The limited speculation on C906 and U74 **mitigates well-known attacks**

   - e.g., Spectre

- Even **limited speculation** allows for **powerful attacks**

47 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 190

#### **Lesson Learned: BPU Attacks Possible. Spectre also.**

- The limited speculation on C906 and U74 **mitigates well-known attacks**

− e.g., Spectre

- Even **limited speculation** allows for **powerful attacks More optimized cores (C910) are more vulnerable**

47 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 191

#### **Conclusion**

48 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 192

#### **Lessons learned: Summary**

49 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 193

#### **Lessons learned: Summary**

• **Open-source architectures are great!**

49 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 194

#### **Lessons learned: Summary**

• **Open-source architectures are great!**

- Allow for **white-box bug hunting**

49 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 195

#### **Lessons learned: Summary**

• **Open-source architectures are great!**

- Allow for **white-box bug hunting**

- Eases proposing **and testing of defenses**

49 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 196

#### **Lessons learned: Summary**

• **Open-source architectures are great!**

   - Allow for **white-box bug hunting**

   - Eases proposing **and testing of defenses**

- RISC-V hardware comes with **similar vulnerabilities** as **other architectures**

49 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 197

#### **Lessons learned: Summary**

- **Open-source architectures are great!**

      - Allow for **white-box bug hunting**

      - Eases proposing **and testing of defenses**

- RISC-V hardware comes with **similar vulnerabilities** as **other architectures**

   - Cache attacks

49 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 198

#### **Lessons learned: Summary**

- **Open-source architectures are great!**

      - Allow for **white-box bug hunting**

      - Eases proposing **and testing of defenses**

- RISC-V hardware comes with **similar vulnerabilities** as **other architectures**

   - Cache attacks

   - Prediction-based attacks

49 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 199

#### **Lessons learned: Summary**

- **Open-source architectures are great!**

      - Allow for **white-box bug hunting**

      - Eases proposing **and testing of defenses**

- RISC-V hardware comes with **similar vulnerabilities** as **other architectures**

   - Cache attacks

   - Prediction-based attacks

   - Transient-execution attacks

49 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 200

#### **Lessons learned: Summary**

- **Open-source architectures are great!**

      - Allow for **white-box bug hunting**

      - Eases proposing **and testing of defenses**

- RISC-V hardware comes with **similar vulnerabilities** as **other architectures**

   - Cache attacks

   - Prediction-based attacks

   - Transient-execution attacks

49 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 201

#### **Lessons learned: Summary**

- **Open-source architectures are great!**

      - Allow for **white-box bug hunting**

      - Eases proposing **and testing of defenses**

- RISC-V hardware comes with **similar vulnerabilities** as **other architectures**

   - Cache attacks

   - Prediction-based attacks

   - Transient-execution attacks

- **“Surprising” design decision:**

49 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 202

#### **Lessons learned: Summary**

- **Open-source architectures are great!**

      - Allow for **white-box bug hunting**

      - Eases proposing **and testing of defenses**

- RISC-V hardware comes with **similar vulnerabilities** as **other architectures**

   - Cache attacks

   - Prediction-based attacks

   - Transient-execution attacks

- **“Surprising” design decision:**

- Unprivileged performance counters

49 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 203

#### **Want to Play Around with the Code?**

**https://github.com/cispa/Security-RISC**

50 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 204

#### **Takeaways**

@____salmon____

@weber_daniel

51 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 205

#### **Takeaways**

###### RISC-V has **a lot of potential…**

@____salmon____

@weber_daniel

51 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 206

#### **Takeaways**

RISC-V has **a lot of potential… Redesigned open-source** architectures do **not automagically solve security**

@____salmon____

@weber_daniel

51 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 207

#### **Takeaways**

RISC-V has **a lot of potential… Redesigned open-source** architectures do **not automagically solve security More (optimized) RISC-V cores** on the way

@____salmon____

@weber_daniel

51 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 208

#### **Takeaways**

RISC-V has **a lot of potential… Redesigned open-source** architectures do **not automagically solve security More (optimized) RISC-V cores** on the way **Security Research** on RISC-V hardware **is essential!**

@____salmon____

@weber_daniel

51 A Security RISC? - Lukas Gerlach, Daniel Weber, Michael Schwarz

## Slide 209

**A Security RISC?** The State of Microarchitectural Attacks on RISC-V **Lukas Gerlach** , **Daniel Weber** , Michael Schwarz | BlackHat EU 2023

52
