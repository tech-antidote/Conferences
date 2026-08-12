---
title: "Racing for Privilege Leaking Privileged Memory From Any Intel System Using a Microarchitectural Race Condition"
speakers: ["Sandro Rüegge", "Johannes Wikner"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Sandro Rüegge&Johannes Wikner_Racing for Privilege Leaking Privileged Memory From Any Intel System Using a Microarchitectural Race Condition.pdf"
pages: 69
sha256: "83f573ea3f08a811c32f570c42bfca496afe2a13741c7d0bdeca640c0ba9a55b"
text_chars: 7684
ocr_pages: 2
has_ocr: true
redacted_secrets: 0
ocr_confidence: 78.2
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: ["Sandro Rüegge&Johannes Wikner_Racing for Privilege Leaking Privileged Memory From Any Intel System Using a Microarchitectural Race Condition_TOOLS.txt"]
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:21:34Z"
---
# Racing for Privilege Leaking Privileged Memory From Any Intel System Using a Microarchitectural Race Condition

**Speakers:** Sandro Rüegge, Johannes Wikner  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Sandro Rüegge&Johannes Wikner_Racing for Privilege Leaking Privileged Memory From Any Intel System Using a Microarchitectural Race Condition.pdf` (69 pages)


## Slide 1

# Racing for Privilege

Leaking memory on any Intel processor with a microarchitectural race condition

Sandro Rüegge & Johannes Wikner

#BHUSA   @BlackHatEvents

## Slide 2

Sandro PhD student Wanted to defend, ended up attacking.

Johannes PhD Graduate Speculative execution vulnerabilities Retbleed, Phantom (e.g., Branch Type Confusion), Inception (SRSO)

Kaveh Professor

2

## Slide 3

## back in 2017…

3

## Slide 4

## A new paradigm exploitation …

4

## Slide 5

?

5

## Slide 6

?

**SPECTRE**

6

## Slide 7

Hilbert Hagedoorn Oct. 2024 AMD Ryzen 9000 Die Shots gets Annotated In Detail guru3d.com/story/amd-ryzen-9 000-die-shots-gets-annotated-i n-detail/

7

## Slide 8

8

## Slide 9

9

## Slide 10

10

## Slide 11

###### **BRANCH TARGET PREDICTIONS**

###### **CACHES**

###### **CPU CORE**

11

## Slide 12

Program 1
jmp   reg
BRANCH TARGET PREDICTIONS CACHES

12

## Slide 13

Program 1
mov   reg, [mem]

**BRANCH TARGET PREDICTIONS**

**CACHES**

13

## Slide 14

Program 1
jmp   ...
BRANCH TARGET PREDICTIONS CACHES

14

## Slide 15

**Program 2 jmp… mov… mov… jmp… etc**

BRANCH TARGET PREDICTIONS

CACHES

15

## Slide 16

**OS/kernel (ring 0) jmp… mov… mov… jmp… etc**

BRANCH TARGET PREDICTIONS

CACHES

16

## Slide 17

**VMM (“ring -1”) jmp… mov… mov… jmp… etc**

BRANCH TARGET PREDICTIONS

CACHES

17

## Slide 18

Program 1
mov   reg, [mem]

BRANCH TARGET PREDICTIONS

CACHES

18

## Slide 19

**Program 1 mov** reg, [mem]

L1$ is tagged by the full<sup>1</sup> physical memory address!

BRANCH TARGET PREDICTIONS

CACHES

19

## Slide 20

👷

#### So what? It’s a design choice.

Program 1
jmp   reg

Prediction is tagged by a **portion** of **virtual** memory address<sup>2</sup>

BRANCH TARGET PREDICTIONS

CACHES

20

## Slide 21

Program 1
jmp   reg
mov  …;   jmp   …
BRANCH TARGET PREDICTIONS CACHES

21

## Slide 22

Inject
prediction

Program 1
jmp   reg
BRANCH TARGET PREDICTIONS CACHES

22

## Slide 23

Inject
prediction

Prime side
channel

Program 1
mov   …;  mov   …;  mov   …;  mov   …;
BRANCH TARGET PREDICTIONS CACHES

23

## Slide 24

Inject
prediction

Prime side
channel

Program 1
syscall

BRANCH TARGET PREDICTIONS

CACHES

24

## Slide 25

Inject
prediction

OS/kernel
Prime side
channel
OS/kernel (ring 0)
jmp   reg

BRANCH TARGET PREDICTIONS

CACHES

25

## Slide 26

OS/kernel
Inject  Prime side  Trigger
prediction channel misprediction
OS/kernel (ring 0)
jmp   reg
BRANCH TARGET PREDICTIONS CACHES

26

## Slide 27

OS/kernel
Inject  Prime side  Trigger  Transmit bit
prediction channel misprediction (side channel)
OS/kernel (ring 0)
jmp   reg
“disclosure gadget”
“secret-dependent”
memory access
BRANCH TARGET PREDICTIONS CACHES

27

## Slide 28

Inject
prediction

OS/kernel
Prime side  Trigger  Transmit bit
channel misprediction (side channel)
OS/kernel (ring 0)
jmp   reg
“disclosure gadget”
“secret-dependent”
memory access

Prime side
channel

**BRANCH TARGET PREDICTIONS CACHES**

28

## Slide 29

OS/kernel
Inject  Prime side  Trigger  Transmit bit
prediction channel misprediction (side channel)
OS/kernel (ring 0)
jmp   reg
“disclosure gadget”
R1: &secret
movzx Rsec ,  byte  ptr [ R1]
R2: memory
mov Rsink, qword ptr [R2 + Rsec * 8]

BRANCH TARGET PREDICTIONS CACHES

29

## Slide 30

OS/kernel
Prime side  Trigger  Transmit bit  Deduce bit
channel misprediction (side channel) (side channel)
Program 1
cache hit/miss?

Inject
prediction

Prime side
channel

BRANCH TARGET PREDICTIONS CACHES

30

## Slide 31

OS/kernel
Prime side  Trigger  Transmit bit  Deduce bit
channel misprediction (side channel) (side channel)
Program 1
cache hit/miss?

Inject
prediction

BRANCH TARGET PREDICTIONS CACHES

31

## Slide 32

OS/kernel
Inject  Prime side  Trigger  Transmit bit  Deduce bit
prediction channel misprediction (side channel) (side channel)
Program 1
cache hit/miss?
BRANCH TARGET PREDICTIONS CACHES
32

32

## Slide 33

Indirect Branch
Restricted  Speculation
(IBRS)

33

## Slide 34

COMPLETE AND
UTTER GARBAGE.
The interface is
mis-designed by
morons
oh for fsck
sake!
34

## Slide 35

enhanced Indirect
Branch  Restricted
Speculation  (eIBRS)

35


> Recovered by OCR — confidence 66/100 on the text kept, 60/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
, enhanced Indirect
= 8 Branch Restricted
E® Speculation (eIBRS)
```

## Slide 36

Love the vibe in
the room rn
I think we
made some
Great meeting  real progress
everyone Great job team

36

## Slide 37

##### eIBRS

eIBRS

● **asm** (“wrmsr” :: “c”(SPEC_CTRL), “a”(1), “d”(0));

37

## Slide 38

##### eIBRS

eIBRS

- **asm** (“wrmsr” :: “c”(SPEC_CTRL), “a”(1), “d”(0));

- set and forget

###### Prediction Mode

###### **BRANCH TARGET PREDICTIONS**

isHV isKern Target …

38

## Slide 39

eIBRS
OS/kernel (ring 0)
jmp   reg
Prediction Mode
mismatch!
BRANCH TARGET PREDICTIONS
39

## Slide 40

##### Assessing eIBRS

kernel module via ioctl
Inject Prime Trigger Transmit Deduce

40

## Slide 41

##### Assessing eIBRS

“signal”
Inject Prime Trigger Transmit Deduce

41

## Slide 42

##### Assessing eIBRS

eIBRS

- Is eIBRS secretly turned on by firmware?

- ● **Inconclusive:** Does it really fail because of eIBRS?

Inject Prime

kernel module via ioctl
Trigger Transmit Deduce

42

## Slide 43

##### Assessing eIBRS

eIBRS

- Is eIBRS secretly turned on by firmware?

- ● **Inconclusive:** Does it really fail because of eIBRS?

kernel module via ioctl
Inject Prime Trigger Transmit Deduce

43

## Slide 44

##### Assessing eIBRS

eIBRS

- Is eIBRS secretly turned on by firmware?

- ● **Inconclusive:** Does it really fail because of eIBRS?

~~Inject Prime~~

kernel module via ioctl
Trigger Transmit Deduce

44

## Slide 45

##### Alder Lake, Golden Cove

eIBRS

kernel module via ioctl
Inject Prime Trigger Transmit Deduce

45

## Slide 46

##### Alder Lake, Golden Cove

eIBRS

kernel module via ioctl
Inject Prime Trigger Transmit Deduce

46

## Slide 47

## What is going on?

47

## Slide 48

Krnl Kernel
Inject getpid Prime syscall Trigger Transmit Deduce
Strong signalWeak signal
Kernel
Inject syscall Prime Trigger Transmit Deduce
Strong signal

48

## Slide 49

Krnl Kernel
Inject getpid Prime syscall Trigger Transmit Deduce

Success rate

Delay (# NOPs)

49


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Prime
syscall
Kernel
Trigger
Transmit Deduce }>
100% +
Success rate 50% -
0% +
0 64
128 192
256
320 384 448 512
Delay (# NOPs)
49
```

## Slide 50

## What could cause this?

50

## Slide 51

Inject
Program 1
jmp   reg
BRANCH TARGET PREDICTIONS CACHES

51

## Slide 52

Inject
Program 1
jmp   reg
BRANCH TARGET PREDICTIONS CACHES

52

## Slide 53

Krnl **Inject getpid OS/kernel (ring 0)Program 1 jmpsyscall** reg **…**

BRANCH TARGET PREDICTIONS

**CACHES**

53

## Slide 54

## Is it this easy?

54

## Slide 55

Krnl Kernel
Inject syscall Prime Trigger Transmit Deduce

55

## Slide 56

Just turn it off.
Signal found! No signal
IP based History based
<
BHI_DIS_S
56

## Slide 57

## Let’s build an attack!

57

## Slide 58

/etc/shadow
Program 1  OS/Kernel

● Local code execution
● Know kernel image

58

## Slide 59

secret
call [rax] disclosure gadget
Shared Mem
Memory

59

## Slide 60

✅ secret
call [rax] disclosure gadget
Shared Mem
Memory

Analyze Kernel

**key->type ->read ->read(key, buffer buffer, buflen buflen);** call [rcx] **secret = *(uint8_t *) buffer buffer ;** movzx edx, byte  ptr [r12] ***(uint64_t *) (** buflen **buflen + 8 * secret** secret **);** mov   rbx, qword ptr [r13 + rdx*8]

60

## Slide 61

✅ secret
call [rax] disclosure gadget
Shared Mem
Memory
Analyze
Kernel
Kernel
Inject syscall Prime Trigger Transmit Deduce

61

## Slide 62

✅ secret ✅
call [rax] disclosure gadget
Shared Mem
Memory
Analyze  Break Locate Locate  Leak
Kernel KASLR Shared Mem /etc/shadow /etc/shadow
Kernel Kernel Kernel Kernel
Inject syscall Prime Trigger Transmit Deduce Inject syscall Prime Trigger Transmit Deduce Inject syscall Prime Trigger Transmit Deduce Inject syscall Prime Trigger Transmit Deduce
root:$6$
62

## Slide 63

## DEMO TIME!

63

## Slide 64

### What security boundaries are affected?

64

## Slide 65

VM VM
Program 1  OS/Kernel Program 1  OS/Kernel
IBPB
VMM VMM

65

## Slide 66

IBPB Race eIBRS Race

**Emerald Rapids Rocket Sapphire Lake Rapids Raptor Coffee Cascade Alder Lunar Lake Lake Lake Lake Lake Refresh Coffee Kaby Comet Raptor Arrow Lake Lake Lake Lake Lake Refresh** 2017 2018 2019 2021 2022 2023 2024

Coffee
Lake
Sandy Kaby
Bridge Lake
2012 2017

66

## Slide 67

## How do we fix it?

67

## Slide 68

Microcode

###### **What does it do?**

68

## Slide 69

##### Conclusion

- Race condition, undermining the long trusted eIBRS mitigation

- ● Spectre: a cat n’ mouse game between offense/defense.

- ● We must assess “black box” mitigations. ○ Type confusions

- ○ Race conditions

   - Use of uninitialized µarch buffers

comsec.ethz.ch/bprc

69

## Companion resources

### `Sandro Rüegge&Johannes Wikner_Racing for Privilege Leaking Privileged Memory From Any Intel System Using a Microarchitectural Race Condition_TOOLS.txt`

```text
https://github.com/comsec-group/bprc
```
