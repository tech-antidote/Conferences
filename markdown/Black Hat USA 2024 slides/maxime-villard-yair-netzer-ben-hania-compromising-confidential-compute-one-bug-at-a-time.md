---
title: "Compromising Confidential Compute, One Bug at a Time"
speakers: ["Maxime Villard", "Yair Netzer", "Ben Hania"]
conference: "Black Hat"
conference_full: "Black Hat USA 2024"
edition: "USA"
year: 2024
source_pdf: "Black Hat USA 2024 slides/Maxime Villard & Yair Netzer & Ben Hania_Compromising Confidential Compute, One Bug at a Time.pdf"
pages: 93
sha256: "9d37220217361a01604109a9cbf3d6cbbc64f1a8f78e3c0bec1ddf99a8fc4b89"
text_chars: 22181
ocr_pages: 7
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:34:41Z"
---
# Compromising Confidential Compute, One Bug at a Time

**Speakers:** Maxime Villard, Yair Netzer, Ben Hania  
**Conference:** Black Hat USA 2024  
**Source:** `Black Hat USA 2024 slides/Maxime Villard & Yair Netzer & Ben Hania_Compromising Confidential Compute, One Bug at a Time.pdf` (93 pages)


## Slide 1

# Compromising Confidential Compute

##### **One bug at a time**

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blackhat | -
USA 2024
AUGUST 7-8, 2024
Compromising Confidential
Compute
One bug at a time
#BHUSA @BlackHatEvents
```

## Slide 2

### ▪ Max

▪ **<u>M</u>** icrosoft **<u>O</u>** ffensive **<u>R</u>** esearch & **<u>S</u>** ecurity **<u>E</u>** ngineering – MORSE Team

#BHUSA @BlackHatEvents

## Slide 3

▪ **Security review of Intel TDX**

▪ Partnership between Microsoft and Intel

▪ 4-month teamwork

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
| -
pisek hat
USA 2024
" Security review of Intel TDX
=" Partnership between Microsoft and Intel
# 4-month teamwork
= Microsoft intel
#BHUSA @BlackHatEvents
```

## Slide 4

### **1. The TDX Module: technical overview**

**2. Research approach and first findings**

**3. Vulnerability 1**

**4. Vulnerability 2**

#BHUSA @BlackHatEvents

## Slide 5

## A change in virtualization architecture

###### **Standard Architecture**

Cloud Provider
Hypervisor
Cloud Customers Guest1 Guest2

- The guests’ memory and registers are visible to the hypervisor

#BHUSA @BlackHatEvents

## Slide 6

## A change in virtualization architecture

###### **Standard Architecture**

Attacker
Cloud Provider
Hypervisor
Cloud Customers Guest1 Guest2

- The guests’ memory and registers are visible to the hypervisor

#BHUSA @BlackHatEvents

## Slide 7

## A change in virtualization architecture

###### **Standard Architecture**

**TDX Architecture**

Attacker
Cloud Provider
Hypervisor
Cloud Customers Guest1 Guest2

Hypervisor TDX
Guest1 Guest2

- The guests’ memory and registers are visible to the hypervisor

- TDX Module: firmware, _gatekeeper_

- Memory is encrypted, registers are hidden

#BHUSA @BlackHatEvents

## Slide 8

## A change in virtualization architecture

**Standard Architecture**

TDX Architecture

Attacker
Cloud Provider
Hypervisor
Cloud Customers Guest1 Guest2

Attacker
Hypervisor TDX
Guest1 Guest2

- The guests’ memory and registers are visible to the hypervisor

- TDX Module: firmware, _gatekeeper_

- Memory is encrypted, registers are hidden

#BHUSA @BlackHatEvents

## Slide 9

## The TDX Module

- Provides **confidentiality** and **integrity** guarantees to guests

- Available in future generation CPUs

- We’re very interested in Confidential Computing in Azure

- **Our goal** : verify the security of the TDX module

#BHUSA @BlackHatEvents

## Slide 10

### **1. The TDX Module: technical overview**

**2. Research approach and first findings**

**3. Vulnerability 1**

**4. Vulnerability 2**

#BHUSA @BlackHatEvents

## Slide 11

## Generalities

- Software that runs on the main CPU, **not** on a separate chip

- Open-Source, MIT license: https://github.com/intel/tdx-module

- Programmed in C, compiled by Clang, ELF binary

- Uses the standard x64 ISA, and runs in ring0 64bit paged mode

#BHUSA @BlackHatEvents

## Slide 12

## Initialization time

- The TDX Module is loaded in a protected range of physical memory called the **_SEAM Range_**

###### **_SEAM Range_**

Physical
TDX Module …
Memory
Hypervisor

- The hypervisor cannot access the SEAM Range

#BHUSA @BlackHatEvents

## Slide 13

## Run time

- The TDX Module executes only when **explicitly invoked**

- Two new CPU instructions: **SEAMCALL** and **SEAMRET**

- The TDX Module is invoked via **SEAMCALL** , and returns via **SEAMRET**

SEAMCALL
Hypervisor TDX Module
SEAMRET

#BHUSA @BlackHatEvents

## Slide 14

## Privileges

▪ “TDX Mode”, has access to the SEAM Range

TDX Mode

Host Mode

**Hypervisor**

**_Time_**

#BHUSA @BlackHatEvents

## Slide 15

## Privileges

▪ “TDX Mode”, has access to the SEAM Range

TDX Mode

TDX Module

Host Mode

SEAMCALL
Hypervisor

**_Time_**

#BHUSA @BlackHatEvents

## Slide 16

## Privileges

▪ “TDX Mode”, has access to the SEAM Range

TDX Module
TDX Mode
SEAMRET
SEAMCALL
Host Mode
Hypervisor Hypervisor

Time

#BHUSA @BlackHatEvents

## Slide 17

## SEAMCALL commands

###### **SEAMCALL**

**Hypervisor RAX** = Command Code **RCX** = Param1 **RDX** = Param2 **R8** = Param3 **R9** = Param4

TDX Module

- The **SEAMCALL** interface implements commands, with parameters passed in registers

- ▪ Similar to **SYSCALL** / **SYSRET** to implement syscalls on traditional kernels

- Around ~80 commands

- Mostly guest management: “Create a guest”, …, “Run a guest”

#BHUSA @BlackHatEvents

## Slide 18

## Command: “run the guest”

###### **_Guest Mode_**

###### **_TDX Mode_**

###### **_Host mode_**

##### **Hypervisor**

**_Time_**

#BHUSA @BlackHatEvents

## Slide 19

## Command: “run the guest”

###### **_Guest Mode_**

**_TDX Mode_**

**_TDX Mode_** **TDX Module** **_SEAMCALL Host mode_** **Hypervisor**

**_Time_**

#BHUSA @BlackHatEvents

## Slide 20

## Command: “run the guest”

Guest Mode
Guest
VMLAUNCH
TDX Mode
TDX Module
SEAMCALL
Host mode
Hypervisor
Time

#BHUSA @BlackHatEvents

## Slide 21

## Command: “run the guest”

Guest Mode
Guest
VMEXIT
VMLAUNCH
TDX Mode
TDX Module TDX Module
SEAMCALL
Host mode
Hypervisor
Time

#BHUSA @BlackHatEvents

## Slide 22

## Command: “run the guest”

Guest Mode
Guest
VMEXIT
VMLAUNCH
TDX Mode
TDX Module TDX Module
SEAMRET
SEAMCALL
Host mode
Hypervisor Hypervisor
Time

#BHUSA @BlackHatEvents

## Slide 23

### **1. The TDX Module: technical overview**

**2. Research approach and first findings**

**3. Vulnerability 1**

**4. Vulnerability 2**

#BHUSA @BlackHatEvents

## Slide 24

## Where to look for vulns?

(Boundary 2)
(Boundary 1)

Guest
VMEXIT
VMLAUNCH
TDX Module TDX Module
SEAMRET
SEAMCALL
Hypervisor Hypervisor

#BHUSA @BlackHatEvents

## Slide 25

## Where to look for vulns?

Not in this talk
(Boundary 2)
(Boundary 1)

Guest
VMEXIT
VMLAUNCH
TDX Module TDX Module
SEAMRET
SEAMCALL
Hypervisor Hypervisor

▪ **Attack scenario** : the hypervisor is compromised, and tries to steal customer data

#BHUSA @BlackHatEvents

## Slide 26

## Execution environment?

- Need a physical machine with a new-generation Intel CPU that supports TDX

- Execute **SEAMCALL** to talk to the TDX Module

- But we can’t attach a debugger, can’t inspect register states, can’t inspect memory…

- **Life is going to be hard if we go down that road**

#BHUSA @BlackHatEvents

## Slide 27

## Introducing Cornelius

- Started as an intellectual exercise to learn more about TDX

- Turned into a full emulator able to run the TDX Module in a VM

- Does not require TDX hardware

- Full introspection capabilities: can inspect register states and memory

- Bonus features: support for **ASAN** , **UBSAN** , **SANCOV**

- **Life is easy now**

#BHUSA @BlackHatEvents

## Slide 28

## Cornelius demo

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisa hat
USA 2024
ornelius demo
PS C:\br\Cornelius\Binaries> .\Test.exe .\pseamldr_1.5.01.02.so.consts .\pseamldr_1.5.01.02.so .\libtdx__1.5.@1-pc.so
PS C:\br\Cornelius\Binaries>
```

## Slide 29

## Cornelius demo

- Zooming in

- Sancov: we executed most commands on CPU0, so CPU0 has the highest coverage

#BHUSA @BlackHatEvents

## Slide 30

## Initial assessment: no easy vulns

- Started looking for standard vulnerabilities, didn’t find any…

- Good programming guidelines: extensive testing, static analysis

- Good mitigations: **CET** , **IBT** , **ASLR** , **W^X** , etc

- Overall good quality, limited opportunities for traditional memory corruptions

- **Will have to think harder**

#BHUSA @BlackHatEvents

## Slide 31

## Looking at context-switching

▪ During **SEAMCALL** and **SEAMRET** , the CPU performs a context-switch

- **SEAMCALL:**

RAM

TDX Module value

**Hypervisor value**

#BHUSA @BlackHatEvents

## Slide 32

## Looking at context-switching

▪ During **SEAMCALL** and **SEAMRET** , the CPU performs a context-switch

▪ **SEAMCALL:**

RAM

Hypervisor value

TDX Module value

#BHUSA @BlackHatEvents

## Slide 33

## Looking at context-switching

▪ During **SEAMCALL** and **SEAMRET** , the CPU performs a context-switch

▪ **SEAMCALL:**

RAM

Hypervisor value

TDX Module value

#BHUSA @BlackHatEvents

## Slide 34

## Looking at context-switching

▪ During **SEAMCALL** and **SEAMRET** , the CPU performs a context-switch

▪ **SEAMCALL:**

RAM

TDX Module value

**Hypervisor value**

#BHUSA @BlackHatEvents

## Slide 35

## Looking at context-switching

▪ During **SEAMCALL** and **SEAMRET** , the CPU performs a context-switch

▪ **SEAMCALL:**

RAM

TDX Module value

**Hypervisor value**

#BHUSA @BlackHatEvents

## Slide 36

## Looking at context-switching

▪ During **SEAMCALL** and **SEAMRET** , the CPU performs a context-switch

- **SEAMCALL:**

RAM

TDX Module value

**Hypervisor value**

#BHUSA @BlackHatEvents

## Slide 37

## Looking at context-switching

▪ During **SEAMCALL** and **SEAMRET** , the CPU performs a context-switch

▪ **SEAMCALL:**

###### **SEAMCALL**

**Hypervisor**

**TDX Module**

TDX Module value

**Hypervisor value**

#BHUSA @BlackHatEvents

## Slide 38

## Looking at context-switching

- During **SEAMCALL** and **SEAMRET** , the CPU performs a context-switch

- **But** ! Not all registers are context-switched by the CPU

- The TDX Module has to context-switch some registers itself manually…

- **… Does it do so correctly?**

#BHUSA @BlackHatEvents

## Slide 39

## Context-switching: a quick test

- The **XMM** registers are switched **neither** by the CPU **nor** by the TDX Module

- The TDX Module doesn’t use **XMM** registers so it doesn’t bother, which is fine

SEAMCALL
Hypervisor TDX Module
XMM0 XMM0
XMM1 XMM1

Hypervisor value TDX Module value

#BHUSA @BlackHatEvents

## Slide 40

## Context-switching: a quick test

▪ **We can disable XMM registers in Cornelius, right?**

▪ _… Right?_

#BHUSA @BlackHatEvents

## Slide 41

## Context-switching: a quick test

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisa hat
USA 2024
Context-switching: a quick test
E3 Windows PowerShell
PS C:\br\Cornelius\Binaries> .\Test.exe .\pseamldr__1.5.01.02.so.consts .\pseamldr__1.5.01.02.so .\libtdx__1.5.@1-pc.so
PS C:\br\Cornelius\Binaries>
```

## Slide 42

## A first bug

- Disabling **XMM** registers in Cornelius causes the TDX Module to crash

- Because the TDX Module **<u>does in fact use XMM registers</u>**

- But forgot to context-switch them

#BHUSA @BlackHatEvents

## Slide 43

## A first bug

Hypervisor TDX Module
SEAMCALL
XMM0 XMM0
XMM1 XMM1

#BHUSA @BlackHatEvents

## Slide 44

## A first bug

Hypervisor TDX Module
SEAMCALL
XMM0 XMM0
XMM1 XMM1
XMM0 New value
XMM1

#BHUSA @BlackHatEvents

## Slide 45

## A first bug

Hypervisor TDX Module
SEAMCALL
XMM0 XMM0
XMM1 XMM1
XMM0 New value
XMM1
SEAMRET
XMM0 XMM0
XMM1 XMM1

#BHUSA @BlackHatEvents

## Slide 46

## Two impacts

1. Hypervisor registers get corrupted

2. Guest secrets can be leaked

#BHUSA @BlackHatEvents

## Slide 47

## Two impacts

1. Hypervisor registers get corrupted

2. ~~Guest secrets can be leaked~~ _Not the case_

- Intel fixed it as a functional bug

#BHUSA @BlackHatEvents

## Slide 48

## Two impacts

1. Hypervisor registers get corrupted

2. ~~Guest secrets can be leaked~~ _Not the case_

- Intel fixed it as a functional bug

- **Found in 20 seconds**

#BHUSA @BlackHatEvents

## Slide 49

### **1. The TDX Module: technical overview**

**2. Research approach and first findings**

**3. Vulnerability 1**

**4. Vulnerability 2**

#BHUSA @BlackHatEvents

## Slide 50

## ProcessorTrace: background

- ProcessorTrace (PT): tracing feature

- The CPU _records_ the execution and creates a log in memory

- The TDX Module supports PT in guests

#BHUSA @BlackHatEvents

## Slide 51

## ProcessorTrace: registers

- PT is controlled by several registers

- Two registers are important:

1. **IA32_RTIT_CTL** : has a **TraceEn** bit that enables tracing

2. **IA32_RTIT_OUTPUT_BASE** : contains the physical address where the log is written

#BHUSA @BlackHatEvents

## Slide 52

## ProcessorTrace context switches

▪ **SEAMCALL** : the CPU forces **CTL.TraceEn** to zero

SEAMCALL

**Hypervisor**

**TDX Module**

**CTL.TraceEn OUTPUT_BASE**

**CTL.TraceEn OUTPUT_BASE**

**TDX Module value**

**Guest value**

**Hypervisor value**

#BHUSA @BlackHatEvents

## Slide 53

## ProcessorTrace context switches

- **SEAMCALL** : the CPU forces **CTL.TraceEn** to zero

- **VMLAUNCH** : the TDX module does a c-switch in software to install the guest values

**Hypervisor**

SEAMCALL

**TDX Module**

VMLAUNCH

**Guest**

**CTL.TraceEn OUTPUT_BASE**

**CTL.TraceEn OUTPUT_BASE**

**CTL.TraceEn OUTPUT_BASE**

TDX Module value

Guest value

**Hypervisor value**

#BHUSA @BlackHatEvents

## Slide 54

## ProcessorTrace context switches

- Focus on the 2<sup>nd</sup> context switch

- Made in software

CTL.TraceEn=0
OUTPUT_BASE

**CTL.TraceEn RAM OUTPUT_BASE**

**TDX Module value**

**Guest value**

**Hypervisor value**

#BHUSA @BlackHatEvents

## Slide 55

## ProcessorTrace context switches

- Focus on the 2<sup>nd</sup> context switch

- Made in software

CTL.TraceEn=0 CTL.TraceEn
RAM
OUTPUT_BASE OUTPUT_BASE

Hypervisor value

TDX Module value

Guest value

#BHUSA @BlackHatEvents

## Slide 56

## ProcessorTrace context switches

- Focus on the 2<sup>nd</sup> context switch

- Made in software

CTL.TraceEn=0CTL.TraceEn CTL.TraceEn
RAM
OUTPUT_BASE OUTPUT_BASE

Hypervisor value

TDX Module value Guest value

#BHUSA @BlackHatEvents

## Slide 57

## ProcessorTrace context switches

- Focus on the 2<sup>nd</sup> context switch

- Made in software

###### _Guest Mode_

_TDX Mode_

TDX Module

###### **_Time_**

#BHUSA @BlackHatEvents

## Slide 58

## ProcessorTrace context switches

- Focus on the 2<sup>nd</sup> context switch

- Made in software

###### _Guest Mode_

Context
Switch
TDX Mode TDX Module

###### **_Time_**

#BHUSA @BlackHatEvents

## Slide 59

## ProcessorTrace context switches

- Focus on the 2<sup>nd</sup> context switch

- Made in software

Guest Mode Guest
Context
Switch
VMLAUNCH
TDX Mode TDX Module

###### **_Time_**

#BHUSA @BlackHatEvents

## Slide 60

## ProcessorTrace context switches

- Focus on the 2<sup>nd</sup> context switch

- Made in software

- The TDX Module is still executing afterwards

- **Problem? No…**

CTL.TraceEn=0CTL.TraceEn
OUTPUT_BASE

RAM

**In-memory value is zero**

**CTL.TraceEn OUTPUT_BASE**

**Hypervisor value**

**TDX Module value**

**Guest value**

#BHUSA @BlackHatEvents

## Slide 61

## Problem

- Except that… On debuggable guests, the in-memory state is accessible to the hypervisor!

In-memory
value is zero
CTL.TraceEn
RAM
OUTPUT_BASE
Guest value

CTL.TraceEn=0TL.TraceEn
OUTPUOUTPUT_BASEBASE

Hypervisor value

TDX Module value

#BHUSA @BlackHatEvents

## Slide 62

## Problem

- Except that… On debuggable guests, the in-memory state is accessible to the hypervisor!

In-memory
value is zero

- The hypervisor can set **TraceEn** =1 in the in-memory state

- **<u>The hypervisor can therefore enable PT in the TDX Module</u>**

CTL.TraceEn
RAM
OUTPUT_BASE

CTL.TraceEn=0TL.TraceEn
OUTPUOUTPUT_BASEBASE

Hypervisor value

TDX Module value

Guest value

#BHUSA @BlackHatEvents

## Slide 63

## Vulnerability

- There is a window where PT is enabled in the TDX Module

Guest Mode

TDX Mode TDX Module

**_Time_**

#BHUSA @BlackHatEvents

## Slide 64

## Vulnerability

- There is a window where PT is enabled in the TDX Module

Guest Mode

Context  PT enabled!
Switch
TDX Mode TDX Module

**_Time_**

#BHUSA @BlackHatEvents

## Slide 65

## Vulnerability

- There is a window where PT is enabled in the TDX Module

Guest Mode Guest
VMEXIT
Context  PT enabled!
Switch
VMLAUNCH
TDX Mode TDX Module TDX Module

###### **_Time_**

#BHUSA @BlackHatEvents

## Slide 66

## Assembling the pieces

- The hypervisor can control **OUTPUT_BASE** …

- **… Meaning: the hypervisor can decide where the log gets written to in memory**

- Via additional PT registers, the hypervisor can ~mostly control the contents of the log…

- **… Meaning: the hypervisor can decide what data gets written in memory**

- While the TDX Module executes, the CPU is in TDX Mode…

- **… Meaning: the SEAM Range is accessible**

#BHUSA @BlackHatEvents

## Slide 67

## The primitive

- The hypervisor can set **OUTPUT_BASE** to point to the SEAM Range, and have TDX memory be overwritten by the PT log, the contents of which are controlled by the hypervisor

- The hypervisor effectively gets a **write-what-where** primitive in TDX memory

- **<u>Achieve complete privilege escalation</u>**

#BHUSA @BlackHatEvents

## Slide 68

## The primitive

- The hypervisor can set **OUTPUT_BASE** to point to the SEAM Range, and have TDX memory be overwritten by the PT log, the contents of which are controlled by the hypervisor

- The hypervisor effectively gets a **write-what-where** primitive in TDX memory

- **<u>Achieve complete privilege escalation</u>**

- What about ASLR in the TDX Module? …

- … ASLR is on the **virtual** memory, not the **physical** memory

#BHUSA @BlackHatEvents

## Slide 69

## Attack scenario

###### 1. Create a debuggable guest

Attacker
Hypervisor TDX
Target Dbg Guest

#BHUSA @BlackHatEvents

## Slide 70

## Attack scenario

1. Create a debuggable guest

2. Escalate privileges into the TDX Module

Attacker

Hypervisor TDX
Target Dbg Guest

#BHUSA @BlackHatEvents

## Slide 71

## Attack scenario

1. Create a debuggable guest

2. Escalate privileges into the TDX Module

3. Steal data from the target

Attacker

Hypervisor TDX
Target Dbg Guest

#BHUSA @BlackHatEvents

## Slide 72

## Attack scenario

1. Create a debuggable guest

2. Escalate privileges into the TDX Module

3. Steal data from the target

- **Defeat the confidentiality guarantees**

- **CVE-2024-39283**

- Affected all versions of the TDX Module

Attacker

Hypervisor

TDX

TDX
Target Dbg Guest

- Fixed by Intel in version 1.5.01

#BHUSA @BlackHatEvents

## Slide 73

**1. The TDX Module: technical overview**

**2. Research approach and first findings**

**3. Vulnerability 1**

**4. Vulnerability 2**

#BHUSA @BlackHatEvents

## Slide 74

## What is SEAMCALL, actually?

- Looking at the very instruction pseudo-code, from the Intel specification

(Source: <u>Intel® Trust Domain CPU Architectural Extensions)</u>

#BHUSA @BlackHatEvents

## Slide 75

## SEAMCALL unconditionality

- **SEAMCALL** is unconditionally recognized

- No toggle to enable or disable it

- **Weird, normally there should be a toggle for new CPU features**

#BHUSA @BlackHatEvents

## Slide 76

## VMEXIT(SEAMCALL) unconditionality

- **SEAMCALL** has a _VMEXIT Reason_ associated to it

- The VMEXIT(SEAMCALL) unconditionally triggers if the guest executes **SEAMCALL**

- **Weird again, normally there should be a toggle**

Hypervisor

**_VMEXIT(SEAMCALL)_ Guest**

#BHUSA @BlackHatEvents

## Slide 77

## Unconditionality

- TDX is a new feature, so current hypervisors do not know about it

- **What happens if a guest executes SEAMCALL but the hypervisor doesn’t recognize**

- **VMEXIT(SEAMCALL)?**

Hypervisor
VMEXIT(SEAMCALL)
Guest

#BHUSA @BlackHatEvents

## Slide 78

## Unconditionality: a problem?

- TDX is a new feature, so current hypervisors do not know about it

- **What happens if a guest executes SEAMCALL but the hypervisor doesn’t recognize**

- **VMEXIT(SEAMCALL)?**

- The hypervisor **kills the guest** , because it doesn’t know how to emulate the operation

Hypervisor
VMEXIT(SEAMCALL)
Guest

#BHUSA @BlackHatEvents

## Slide 79

## Nested scenarios

- The guest is itself a hypervisor that runs a guest

- If the nested guest executes **SEAMCALL** , it’s the outer hypervisor that handles it

Hypervisor
VMEXIT(SEAMCALL)
Hypervisor
Guest

#BHUSA @BlackHatEvents

## Slide 80

## Nested scenarios

- The guest is itself a hypervisor that runs a guest

- If the nested guest executes **SEAMCALL** , it’s the outer hypervisor that handles it

- The outer hypervisor kills the whole guest: its hypervisor and its nested guests

Hypervisor
VMEXIT(SEAMCALL)
Hypervisor
Guest

#BHUSA @BlackHatEvents

## Slide 81

## Nested scenarios in Azure

▪ Containers run in nested VMs

Hypervisor
Nested hypervisor Nested hypervisor
Guest 1 Guest 2 Guest 3 Guest 7 Guest 8 Guest 9
Guest 4 Guest 5 Guest 6

#BHUSA @BlackHatEvents

## Slide 82

## Nested scenarios: vulnerability

▪ If a malicious guest executes **SEAMCALL** , all of nested system gets killed

Hypervisor
VMEXIT(SEAMCALL)
Nested hypervisor Nested hypervisor
Guest 1 Guest 2 Guest 3 Guest 7 Guest 8 Guest 9
Guest 4 Guest 5 Guest 6

#BHUSA @BlackHatEvents

## Slide 83

## Nested scenarios: vulnerability

- If a malicious guest executes **SEAMCALL** , all of nested system gets killed

- **Ability to DoS other customers by just executing SEAMCALL**

Hypervisor
VMEXIT(SEAMCALL)
Nested hypervisor Nested hypervisor
Guest 1 Guest 2 Guest 3 Guest 7 Guest 8 Guest 9
Guest 4 Guest 5 Guest 6

#BHUSA @BlackHatEvents

## Slide 84

## An additional bug

- What’s more: there’s a priority inversion between VMEXIT(SEAMCALL) and the CPL check

- **The malicious customer doesn’t even have to be in kernelmode: they can directly execute SEAMCALL from usermode!**

#BHUSA @BlackHatEvents

## Slide 85

## Affected systems

- Remember: we’re talking about the case where the hypervisor doesn’t know about TDX

- Future setups where an **old** hypervisor runs on **new** hardware

- Not an unexpected setup in the cloud, legitimate for various reasons

#BHUSA @BlackHatEvents

## Slide 86

## Affected systems

- Remember: we’re talking about the case where the hypervisor doesn’t know about TDX

- Future setups where an **old** hypervisor runs on **new** hardware

- Not an unexpected setup in the cloud, legitimate for various reasons

- **CVE-2024-22374**

- Intel fixed half of the vulnerability via a microcode update

- We patched all Hyper-V versions to recognize VMEXIT(SEAMCALL)

#BHUSA @BlackHatEvents

## Slide 87

#### **Takeaways**

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blackhat —_
USA 2024
Takeaways
#BHUSA @BlackHatEvents
```

## Slide 88

## Whitepaper

- Whitepaper covering our research: <u>link</u>

- Partnership between Microsoft and Intel

- **21 findings** , with **6 confirmed vulnerabilities**

- BlueHat IL 2024: <u>Compromising Confidential Compute and then fixing it</u> (YouTube)

- Intel Blog Post: <u>Intel and Microsoft joint security review of Intel TDX 1.5</u>

#BHUSA @BlackHatEvents

## Slide 89

## Cornelius

- Cornelius is now open-source

- <u>https://github.com/microsoft/Cornelius</u>

- Great tool

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
€
black hat
USA 2024
Cornelius
= Cornelius is now open-source
: vM
P-SEAMLDR
0 SeamcallentryPoint:
= Greattool 12 y
YourAgent.exe ... Instructions ...
(the Host VMM) SEAMRET-To-HostVmm
printf("Invoking TDH.VP.ENTER... ")3 ( \ TDX module
SeamcallTdx_TdhvpEnter(Vm, @, Tdvm, @); SeamcallEntryPoint:
printf("Done!\n"); <«€ .+. Instructions ...
printf("Triggering VMEXIT... "); c li dil ie VMLAUNCH-To-TdGuest
ornetius.
Tdvmexit(vm, 0); TdGuestvmexitEntryPoint:
printf("Done!\n");  <——————> ... Instructions ...
€ SEAMRET-To-HostVmm
XY
Call into firmware
<< Entry into TD guest
Exit from TD guest
< Return from firmware
```

## Slide 90

## TDX: a fun target to look at

- TDX Module source code: https://github.com/intel/tdx-module

- Written with security in mind, finding bugs is hard

- Good mitigations

- **Perfect intellectual exercise**

#BHUSA @BlackHatEvents

## Slide 91

## Bug bounty

- Intel has a bug bounty program that covers the TDX Module

- Random idea: you can write a fuzzer based on Cornelius, find bugs, report them

#BHUSA @BlackHatEvents

## Slide 92

#### **Thank you**

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blackhat —_
USA 2024
Thank you
= Microsoft intel
#BHUSA @BlackHatEvents
```

## Slide 93

### **PS: we’re recruiting!** **<u>aka.ms/morsejobs</u>**

#BHUSA @BlackHatEvents
