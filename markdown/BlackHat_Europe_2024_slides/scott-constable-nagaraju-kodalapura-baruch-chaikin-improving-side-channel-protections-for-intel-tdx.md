---
title: "Improving Side-Channel Protections for Intel TDX"
speakers: ["Scott Constable", "Nagaraju Kodalapura", "Baruch Chaikin"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2024"
edition: "Europe"
year: 2024
source_pdf: "BlackHat_Europe_2024_slides/Scott Constable & Nagaraju Kodalapura & Baruch Chaikin_Improving Side-Channel Protections for Intel TDX.pdf"
pages: 40
sha256: "38abbbfe3c6d0f145b0e744ef2c61e27b4ed4d43d674a4adf438aaedc980a25d"
text_chars: 18588
ocr_pages: 2
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:51:44Z"
---
# Improving Side-Channel Protections for Intel TDX

**Speakers:** Scott Constable, Nagaraju Kodalapura, Baruch Chaikin  
**Conference:** Black Hat Europe 2024  
**Source:** `BlackHat_Europe_2024_slides/Scott Constable & Nagaraju Kodalapura & Baruch Chaikin_Improving Side-Channel Protections for Intel TDX.pdf` (40 pages)

## Slide 1

# Improving Side-Channel Protections for Intel® TDX

*Scott Constable Defensive Security Researcher, Intel Labs, Intel Corporation *Nagaraju (Raju) Kodalapura Principal Engineer, Offensive Security Research, Intel Corporation Baruch Chaikin Principal Engineer, CPU Architecture, Intel Corporation

*Speakers

#BHEU @BlackHatEvents

## Slide 2

## Acknowledgements

- Intel Labs

- Intel Product Security and Assurance (IPAS) research

- Intel CPU Security Effectiveness Team

- Intel CPU Architecture Team

- The TDXdown researchers at TU Lübeck: Luca Wilke, Florian Sieck, Thomas Eisenbarth

Scott Constable

Nagaraju (Raju) Kodalapura

Baruch Chaikin

Information Classification: General

#BHEU @BlackHatEvents

2

## Slide 3

## Agenda

- Intro to Confidential Computing, Intel TDX (Trust Domain Extensions), side-channel Attacks, and malicious single-stepping

- Pre-TDX PoC (Proof of Concept) TDX-step exploit and mitigation

- Techniques to bypass the TDX-Step mitigation, and intro to the new ICSSD (Instruction Counting Single-Step Defense) feature

- Comparison with the SGX-Step mitigation

Information Classification: General

#BHEU @BlackHatEvents

3

## Slide 4

## What is Confidential Computing (CC)?

Protects  data at rest (in storage, a database, etc.).

- Data encryption

- Access control

Protects **data in transit** (over a network, PCI bus, etc.)

- HTTPS

- TLS

#### **The Focus of CC**

##### Protects **data in use** (within a CPU, XPU, etc.)

- Hardware-based, attested Trusted Execution Environments (TEEs) such as Intel TDX and Intel SGX

Information Classification: General

#BHEU @BlackHatEvents

4

## Slide 5

## What is Intel® TDX?

Host VMM managed access control, enhanced with MK-TME

Intel TDX module managed access control, leveraging MK-TME and Secure EPT

control, enhanced with MK-TME leveraging MK-TME and Secure EPT
Legacy VM Legacy VM Trust Domain Trust Domain
Unmodified  Unmodified
Applications Applications
Applications Applications
Unmodified  Unmodified
Drivers Drivers
Drivers Drivers
TDX- TDX-
OS OS Enlightened Enlightened
OS OS
Intel TDX Intel TDX
Guest-Side Interface Guest-Side Interface
Intel TDX Intel TDX Module
TDX-Aware Host VMM Host-Side
Interface Running in SEAM Root Mode
Platform (Cores, Caches, Devices etc.)

**Intel TDX is a CC technology that provides confidentiality and integrity for data in use by tenant VMs, called Trust Domains (TDs)**

- **Objective:** Remove the Virtual Machine Monitor (VMM) and other system SW from the TDs’ TCB

- **TDX Module:** Intel-signed security services module responsible for enforcing security policies for TDs

- **SEAM:** A new Secure Arbitration Mode (SEAM) hosts the TDX module

Information Classification: General

#BHEU @BlackHatEvents

5

## Slide 6

## TDX Threat Model

**Protects against SW adversary Protects against SW/HW adversary**

**Some side-channel attacks are out of scope for the TDX threat model**

Source: White Paper | Intel® Trust Domain Extensions 6

Information Classification: General

#BHEU @BlackHatEvents

## Slide 7

## What is a Side Channel?

#### Victim Context

#### Attacker Context

Do a cat thing! Do something else! Do a different cat thing!

HW buffer

Do a teapot thing! My teapot thing was _slow_ , so the victim must have done a cat thing! Do a teapot thing! My teapot thing was _fast_ , so the victim must _not_ have done a cat thing! Do a teapot thing! My teapot thing was _slow_ , so the victim must have done a cat thing!

Information Classification: General

#BHEU @BlackHatEvents

7

## Slide 8

## Adversary’s Challenge: Shutter Speed

What if the adversary just triggers a single operation at a time, and then performs a side-channel measurement?

TD instruction stream (typically 1.8 GHz or more):

```
TD runs
```

Information Classification: General

#BHEU @BlackHatEvents

8

## Slide 9

## Adversary’s Challenge: Shutter Speed **Slow Shutter**

Slow Shutter

TD instruction stream
1 Operation
(typically 1.8 GHz or more):

Information Classification: General

#BHEU @BlackHatEvents

9

## Slide 10

## Adversary’s Challenge: Shutter Speed

Let’s try something more precise: can the adversary trigger a at a single **_<u>instruction</u>_** time?

TD instruction stream (typically 1.8 GHz or more):

TD runs

Information Classification: General

#BHEU @BlackHatEvents

10

## Slide 11

## Adversary’s Challenge: Shutter Speed

##### **Fast Shutter**

1 Instruction

This technique was pioneered in a framework called:

Information Classification: General

#BHEU @BlackHatEvents

11

## Slide 12

## Searching for an Ideal HW Primitive

Information Classification: General

#BHEU @BlackHatEvents

12

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
EUROPE 2024
Searching for an Ideal HW Primitive
Intel® 64 and IA-32 Architectures
Software Developer's Manual
CHAPTER 12
ADVANCED PROGRAMMABLE INTERRUPT CONTROLLER (APIC)
12.5.4 APIC Timer
The local APIC unit contains a 32-bit programmable timer that is available to software to time events or operations.
This timer is set up by programming four registers: the divide configuration register (see Figure 12-10), the initial-
count and current-count registers (see Figure 12-11), and the LVT timer register (see Figure 12-8).
TSC-deadline mode allows software to use the local APIC timer to signal an interrupt at an absolute time. In TSC-
deadline mode, writes to the initial-count register are ignored; and current-count register always reads O. Instead,
timer behavior is controlled using the IA32_TSC_DEADLINE MSR.
Information Classification: General 1 2
```

## Slide 13

## A Small Target for an (Inaccurate) APIC

**rate**

**APIC timer:**

Time

**Actual distribution of Why is there so much hit variation? APIC timer interrupts:**

**~220 cycles**

**Interrupt and exit Page A-bit Exec Walk assist Flush TLBs Flushes Page Translations Arm APIC timer Enter SGX enclave INSTR**

**Example: Singlestepping an SGX enclave**

Time

Information Classification: General

#BHEU @BlackHatEvents

13

## Slide 14

A Small Target for an (Inaccurate) APIC

**Key Idea 1: Don’t try to hit a small target! Instead, make the target** **_slower_ and therefore bigger**

**Example: Singlestepping an SGX enclave**

**Flush TLBs Flushes Page Translations Arm APIC timer Enter SGX enclave**

**Page A-bit Exec Walk assist INSTR**

**Interrupt and exit**

Time

Information Classification: General

#BHEU @BlackHatEvents

14

## Slide 15

## Agenda

- Intro to Confidential Computing, Intel TDX (Trust Domain Extensions), side-channel Attacks, and malicious single-stepping

- Pre-TDX PoC (Proof of Concept) TDX-step exploit and mitigation

- Techniques to bypass the TDX-Step mitigation, and intro to the new ICSSD (Instruction Counting Single-Step Defense) feature

- Comparison with the SGX-Step mitigation

Information Classification: General

#BHEU @BlackHatEvents

15

## Slide 16

## TDX-Step Attack Scenario

- **PoC (Proof of Concept) Exploit** was developed in a virtualization setup (no TDX support)

- **Interrupt based attack:** VMM mounts attack on VM/TD application using APIC

VM
If secret do
Inst1
else
Inst2 Interrupt
Clean
LAPIC Malicious
Arm Timer
VM Exit VMRESUME
VMMVMM

Information Classification: General

#BHEU @BlackHatEvents

16

## Slide 17

## Pre-TDX Test Setup

VM
INSTR
INSTR
vmx- non-root
INSTR
mode
…
j IRQ
INSTR
VM Exit VM Resume APIC
vmx- root mode
Good VMM Bad VMM
KVM
Trusted Malicious Clean

vmx- non-root
mode

- KVM (Host VMM ) as the host used as the both Good (Mitigation) and Bad (Attack) Actor

- Ubuntu VM (Virtual Machine) as the Guest, running “strlen” workload/app as a victim app

- Good VMM portion of the KVM code was eventually implemented in Intel TDX Module, which is responsible for mitigating the TDX-Step attack

Information Classification: General

#BHEU @BlackHatEvents

17

## Slide 18

## TDX-Step Attack Realized

VM (Victim)
INSTR
INSTR
vmx- non-root
INSTR
mode … IRQj IRQ
INSTR
VM Exit VM Resume APIC
vmx- root
mode
KVM Bad VMM
Malicious Clean

- Bad VMM configures the APIC timer to cause periodic interrupts to Victim VM on an instruction boundary

- Once interrupted, victim VM will exit to the host through VM Exit

- Now Bad VMM has the ability conduct side channel analysis on the VM instruction execution

- Also, bad VMM will cause VM Resume to make the victim VM to execute all the instructions

Information Classification: General

#BHEU @BlackHatEvents

18

## Slide 19

## Proof of Concept attack: Interrupt-based attack on strlen

- Victim VM executing the strlen 7 consisted of 34 instructions

- Out of 100 experiments, the PoC attack was able to cause single-step attack successfully for 8 times

- This was sufficient to prove that TDX-Step attack indeed is real

Information Classification: General

#BHEU @BlackHatEvents

19

## Slide 20

## Mitigation - Proposal 1

VE Handler
VM
INSTR (random set of
instructions)
INSTR
vmx- non-root
INSTR
mode
… IRQ
INSTR
VM Exit Inject  #VE VM Resume
APIC
vmx- root
mode
KVM Good VMM Bad VMM

- **Mitigation:** “Good VMM” portion of KVM implements the stepdetector which will inject #VE (Virtualization Exception) to VM

- VM will eventually exit to the Host

Malicious Mitigation Clean

Information Classification: General

#BHEU @BlackHatEvents

20

## Slide 21

## Proposal 1: Mitigation PoC Result

- Test results show that it wasn’t possible to cause VM Exits exactly on every instruction boundary (34 instructions)

- Even if so, the real instruction count of 34 was never met

- **Limitations**

   - 1) NOT scalable

   - 2) Increased attack surface

- **Next step:** Define a mitigation to overcome the above limitations

Information Classification: General

#BHEU @BlackHatEvents

21

## Slide 22

## Mitigation - Proposal 2

VM
INSTR
INSTR
VM Exit
INSTR
…
IRQ
vmx non-root
INSTR
mode
VMResume (extra random N instruction) APIC
Good VMM
vmx root
mode
Bad VMM
KVM
Malicious Mitigation Clean

- Mitigation is fully self-contained within the “Good VMM”, employing the step-filter

- Resumes the victim VM to execute extra “N” random instructions before it transfer the control back to the Bad VMM

- **Result:** With the mitigation enabled, instruction count never matched the expected count value of 34, thereby defeating the attack

Information Classification: General

#BHEU @BlackHatEvents

22

## Slide 23

### TDX-Step (v1.0) Mitigation using TDX Module

• TDX Module @ **https://github.com/intel/tdx-module**

- The TDX module employs a VM exit Step-filter algorithm

- Pre-conditions to enable step filter:

   1. Interrupt duration should be less 4K cycles since the last entry – **TSC (Time Stamp Counter)** ) **or**

   2. The RIP of the VCPU has not made progress

- TDX Module resumes the VCPU in “stepping mode” for random number (2-32) of instructions

- VCPU stepping is done using the VMX Monitor Trap Flag (MTF) mechanism.

Information Classification: General

#BHEU @BlackHatEvents

23

## Slide 24

## Agenda

- Intro to Confidential Computing, Intel TDX (Trust Domain Extensions), side-channel Attacks, and malicious single-stepping

- Pre-TDX PoC (Proof of Concept) TDX-step exploit and mitigation

- Techniques to bypass the TDX-Step mitigation, and intro to the new ICSSD (Instruction Counting Single-Step Defense) feature

- Comparison with the SGX-Step mitigation

Information Classification: General

#BHEU @BlackHatEvents

24

## Slide 25

## (We showed this slide earlier)

**rate**

APIC timer:

Time

**Actual distribution of Why is there so much hit variation? APIC timer interrupts:**

**~220 cycles**

Interrupt
and exit
Example: Single- Page  A-bit
Exec
stepping an SGX  Walk assist
Flush TLBs
Flushes Page Translations
Arm APIC timer Enter SGX enclave INSTR

**Example: Singlestepping an SGX enclave**

Time

Information Classification: General

#BHEU @BlackHatEvents

25

## Slide 26

## Attempting to Single-step a TD

**Recall that each TD’s page tables are protected within its own private memory**

Page  A-bit
Example: Single- Exec
Walk assist
stepping a TD? Flush TLBs
Arm APIC timer Enter TD INSTR Exit TD
Record  Record
TSC1 TSC2
Flushes Page Translations
Recall that the TD forces RAND[2,32]
If (TSC2-TSC1 < 4K):
instructions to execute if less than 4K
Apply mitigation
cycles elapse between entry and exit

**Example: Singlestepping a TD?**

Information Classification: General

#BHEU @BlackHatEvents

26

## Slide 27

## Demo 1

- Let’s attempt to single-step a TD

- (Note that RAX=10 at the start)

62 instructions

÷

~16 instructions forced by the TDX module

=

~4 instructions per attack attempt

Listing Source: L. Wilke, F. Sieck, and T. Eisenbarth, ‘TDXdown: SingleStepping and Instruction Counting Attacks against Intel TDX’, in _Proceedings of the 2024 ACM SIGSAC Conference on Computer and Communications Security, CCS 2024, Salt Lake City, UT, USA, October 14--18, 2024_ , 2024.

Information Classification: General

#BHEU @BlackHatEvents

27

## Slide 28

## Single-stepping a TD (TDXdown)

**Example: Singlestepping a TD using frequency scaling Slow victim core frequency**

**Arm APIC timer**

**Enter TD**

**Page Exec Walk INSTR**

**Exit TD**

**TSC1**

**Example:** Slowing the victim core from 1.8 GHz to 800 MHz will increase the latency of all victim operations by 2.25x, as measured by the TSC

**TSC2 TSC2-TSC1 < 4K?**

Information Classification: General

#BHEU @BlackHatEvents

28

## Slide 29

## Demo 2

- Let’s attempt to single-step a TD using frequency scaling (TDXdown technique)

62 instructions

Listing Source: L. Wilke, F. Sieck, and T. Eisenbarth, ‘TDXdown: SingleStepping and Instruction Counting Attacks against Intel TDX’, in _Proceedings of the 2024 ACM SIGSAC Conference on Computer and Communications Security, CCS 2024, Salt Lake City, UT, USA, October 14--18, 2024_ , 2024.

Information Classification: General

#BHEU @BlackHatEvents

29

## Slide 30

#### **Key Idea 2: Frequency scaling can be used to fool mitigation heuristics that rely on the TSC**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 31

## Single-stepping a TD (Method 2)

Can we make this
a lot slower?
Page
Exec
Walk
Flush TLBs
Arm APIC timer Enter TD INSTR Exit TD
Slowing these operations is the focus of TDXdown
Key Idea 1: Don’t try to hit a small target!
Instead, make the target  slower  and therefore
bigger

Information Classification: General

#BHEU @BlackHatEvents

31

## Slide 32

## A Page Walk isn’t always a Cake Walk

VM address translation

Non-VM address translation

Image Source: https://rayanfam.com/topics/hypervisor-from-scratch-part-4/

Information Classification: General

#BHEU @BlackHatEvents

32

## Slide 33

## Demo 3

- Let’s attempt to single-step a TD by flushing the EPTs

62 instructions

Listing Source: L. Wilke, F. Sieck, and T. Eisenbarth, ‘TDXdown: SingleStepping and Instruction Counting Attacks against Intel TDX’, in _Proceedings of the 2024 ACM SIGSAC Conference on Computer and Communications Security, CCS 2024, Salt Lake City, UT, USA, October 14--18, 2024_ , 2024.

Information Classification: General

#BHEU @BlackHatEvents

33

## Slide 34

## Instruction-Count Single-Step Defense

Information Classification: General

#BHEU @BlackHatEvents

34

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pis hat
EUROPE 2024
Instruction-Count Single-Step Defense
Intel® Trust Domain Extensions (Intel® TDX) Module
Base Architecture Specification
17.Side Channel Attack Mitigation Mechanisms
Suspected Attack Detection Using Instruction Counting
This attack detection method is applicable if the TDX module implements Instruction-Count Single-Step Defense (ICSSD),
as indicated by TDX_FEATURESO.ICSSD, readable by the host VMM using TDH.SYS.RD*. It is used only if the TD is not
Perfmon-enabled, i.e., ATTRIBUTES.PERFMON is 0. An interruption is considered far enough from the last TD entry if
either of the following conditions is true:
e More than one instruction has been retired since the last TD entry, or
e More than one round of a REP-prefixed instruction has been executed since the last TD entry.
Information Classification: General 34
```

## Slide 35

## Demo 4

- Let’s attempt to single-step a TD when ICSSD is enabled

62 instructions ÷

~16 instructions forced by the TDX module

=

~4 instructions per attack attempt

Listing Source: L. Wilke, F. Sieck, and T. Eisenbarth, ‘TDXdown: SingleStepping and Instruction Counting Attacks against Intel TDX’, in _Proceedings of the 2024 ACM SIGSAC Conference on Computer and Communications Security, CCS 2024, Salt Lake City, UT, USA, October 14--18, 2024_ , 2024.

Information Classification: General

#BHEU @BlackHatEvents

35

## Slide 36

## Agenda

- Intro to Confidential Computing, Intel TDX (Trust Domain Extensions), side-channel Attacks, and malicious single-stepping

- Pre-TDX PoC (Proof of Concept) TDX-step exploit and mitigation

- Techniques to bypass the TDX-Step mitigation, and intro to the new ICSSD (Instruction Counting Single-Step Defense) feature

- Comparison with the SGX-Step mitigation

Information Classification: General

#BHEU @BlackHatEvents

36

## Slide 37

## AEX-Notify: the SGX-Step mitigation

**Example: An SGX enclave hardened with Flushes Page TranslationsFlush TLBs AEX-Notify Arm APIC timer Enter SGX enclave**

Page
A-bit assists
Walks
AEX-Notify handler
SW feature that “warms up”
code and data memory
INS1 INS2 INS3

**Example: Singlestepping an SGX enclave, without Flushes Page TranslationsFlush TLBs AEX-Notify Arm APIC timer Enter SGX enclave**

**Page A-bit Exec Walk assist INSTR**

Information Classification: General

#BHEU @BlackHatEvents

37

## Slide 38

Why implement two different single-step mitigations for SGX and TDX?

- TDX is a virtualization-based technology, and therefore has different capabilities

- AEX-Notify uses a SW component that is available in the Intel SGX SDK—a similar SW solution for TDX would require para-virtualization in the guest OS

- Popular OS kernels such as Linux cannot handle arbitrary externally generated events

Trust Boundary: Elements with potential to access confidential data

VM Isolation  Cloud Stack  BIOS and  Host OS and  VM Guest  Confidential
Guest OS Applications
with Intel® TDX and Admins Firmware Hypervisor Admin Data
App Isolation  Cloud Stack  BIOS and  Host OS and  VM Guest  Confidential
Guest OS Apps
with Intel® SGX and Admins Firmware Hypervisor Admin Data
Enclave

Information Classification: General

#BHEU @BlackHatEvents

38

## Slide 39

- Conclusion (and Q&A before lunch) • Confidential Computing’s strong adversary model continues to drive exciting research. This presentation showed some capabilities that a privileged adversary may use:

   - Arming the APIC timer to hit an adversary-desired instruction with an interrupt

   - Scaling the clock frequency of the victim’s CPU core

   - Flushing all of the CPU’s caches

- Defense-in-depth mechanisms such as ICSSD and AEX-Notify can help to mitigate potential side-channel attacks against Trusted Execution Environments

- Modern processors use a variety of address translation caching techniques to dramatically accelerate memory accesses in virtualized environments

Information Classification: General

#BHEU @BlackHatEvents

39

## Slide 40

#BHEU @BlackHatEvents
