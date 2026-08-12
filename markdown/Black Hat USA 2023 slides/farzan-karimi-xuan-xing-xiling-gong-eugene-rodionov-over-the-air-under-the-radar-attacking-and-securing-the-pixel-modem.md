---
title: "Over the Air, Under the Radar Attacking and Securing the Pixel Modem"
speakers: ["Farzan Karimi", "Xuan Xing", "Xiling Gong", "Eugene Rodionov"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/Farzan Karimi & Xuan Xing & Xiling Gong & Eugene Rodionov_Over the Air, Under the Radar Attacking and Securing the Pixel Modem.pdf"
pages: 41
sha256: "e3de27e5f4f5bdefcfcbc35d77830b5303bb9c399f2646c6cede76f890e44fe4"
text_chars: 18512
ocr_pages: 6
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:15:54Z"
---
# Over the Air, Under the Radar Attacking and Securing the Pixel Modem

**Speakers:** Farzan Karimi, Xuan Xing, Xiling Gong, Eugene Rodionov  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Farzan Karimi & Xuan Xing & Xiling Gong & Eugene Rodionov_Over the Air, Under the Radar Attacking and Securing the Pixel Modem.pdf` (41 pages)

## Slide 1

Over the Air, Under the Radar Attacking and Securing the Pixel Modem

Xuan Xing

Eugene Rodionov

Xiling Gong

Farzan Karimi

#BHUSA   @BlackHatEvents

## Slide 2

### **Agenda**

- Who We Are

- Pixel Modem Red Team Engagement Overview ○ Why Modem?

   - Goals & Methodology

- Proof of Concept Demonstrations

   - CVE-2022-20170

   - CVE-2022-20405

- How we secure the next generation of Pixel

All vulnerabilities mentioned in this presentation have been fixed

#BHUSA  @BlackHatEvents

## Slide 3

### **Mission**

We are the **eyes of Android Security** : Increase Pixel and Android security by attacking key components and features, identifying critical vulnerabilities before adversaries Offensive Security Reviews to verify (break) security assumptions Scale through tool development (e.g. continuous fuzzing) Develop proof of concepts to demonstrate real-world impact Assess the efficacy of security mitigations

#BHUSA  @BlackHatEvents

## Slide 4

# Why Modem?

#BHUSA  @BlackHatEvents

## Slide 5

###### **2019-2023**

#### **Modem has been an emerging area of risk**

#BHUSA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 20253
Modem has been an
emerging area of risk
Qualcomm chip vulnerability found in millions
of Google, Samsung, and LG phones
Over The Air Baseband Exploit:
Gaining Remote Code
Execution on 5G Smartphones
Marco Grassi (@marcograss)
Xingyu Chen (@@xkira233)
K) xeon
security
lab
Black Hat talk exposes how ea: inals can hack mobile
broadband modems
ek)
Samsung Smartphones Already Received Modem
Vulnerability Patch
The vulnerability in Qualcomm modems
OR or cmt ty 20 affects 30 percent of mobile phones
—
2
#BHUSA @BlackHatEvents
```

## Slide 6

### **So What?**

**What an attacker would get:**

- Over-the-air Remote Code Execution

- ● Running in Privileged Context

- **What that means:**

- DDoS Botnet

- SMS/RCA Sniffing and Spoofing

- ● MFA Compromise

- ● Pivot Opportunities to Kernel

#BHUSA  @BlackHatEvents

## Slide 7

### **So What?**

Why Modem?

**OTA            RCE**

MFA Compromise

#BHUSA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
blackhat So What?
USA 2&0e5
2FA compromise led to $34M Crypto.com hack
Anita Ramaswamy @anitaramaswamy / 10:13 AM PST + January 20, 2022
```

## Slide 8

### **Engagement Overview**

###### **Timeline:**

- Multi-month Android Red Team engagement from late 2021 to early 2022

Mission

- Gain remote code execution on baseband via the Pixel 6 modem stack

- ● Suggest systemic security improvements to harden the Pixel 6+ modem

- Bonus: Get everything patched before debrief

#BHUSA  @BlackHatEvents

## Slide 9

# Modem Overview

#BHUSA  @BlackHatEvents

## Slide 10

### **Modem Overview**

###### **Modem at a glance:**

#BHUSA  @BlackHatEvents

## Slide 11

### **Modem Overview**

###### **Modem at a glance:**

- A critical component with access to sensitive user data

- Remotely accessible with various radio technologies

- A high profile target which could benefit from security hardening mitigations

- A historical source of vulnerabilities from external researchers and modem owners

- Many legacy protocols with outdated security practice

Image Credit: Pixel 6 X-ray Imablog

#BHUSA  @BlackHatEvents

## Slide 12

## **Modem Overview**

AP
Radio Services
Kernel Driver
Interface
Modem Drivers AP/CP IPC Interface

CP Base Station
Modem
Firmware
Cellular Network

#BHUSA  @BlackHatEvents

## Slide 13

## **Modem Overview**

Communication Service
Telephony services IMS SMS, MMS, etc
Abstraction Layer
HLOS Interfaces
Protocol Level
2G WCDMA 4G-LTE 5G
ASN.1 and
other
low-level  Pre- Post- Pre- Post- Pre- Post- Pre- Post-
decoders AKA AKA AKA AKA AKA AKA AKA AKA
Physical Layer
DSP System Module System Tools

LEGEND
Layer
Component
Attack Surface Covered by
Android Red Team
Proof of Concept

#BHUSA  @BlackHatEvents

## Slide 14

# Our Methodology

#BHUSA  @BlackHatEvents

## Slide 15

### **Evaluation Approaches**

- **Fuzzing as the primary approach**

   - Host based fuzzing has been proven effective during first modem engagement

   - Full system emulation is complete

   - ○ On-device fuzzing was cut due to schedule constraint

- **Static analysis using CodeQL**

   - Exploring modem codebase

   - Variant analysis

- **Manual code review**

   - Only for areas identified by fuzzing or external researches

Fuzzing
review
Manual code  Static analysis

#BHUSA  @BlackHatEvents

## Slide 16

## **Fuzzing Overview**

###### **Progress:**

- 10 fuzzers created during the engagement and running on our internal at-scale device fuzzing platform.

- Fuzzers not only find great bugs, but also identify high risk areas for manual code review.

- ● Developing an easy to use framework for host based modem fuzzing.

###### **Fuzzing Challenges:**

- Low severity bugs blocking fuzzing from continuing

- ● Complex dependencies to other components

- ● Tasks dealing with internal messages no value for fuzzing

|**Fuzzer Name**|**Description**|
|---|---|
|AsnDecoder|Targets ASN.1 decoder which
reads and translates data
encoded in ASN.1 format by
feeding malformed inputs.
ASN.1 is widely used in various
protocols and data formats|
|CdParseMsg|Targets parser responsible for
processing and interpreting
messages received by the
modem from external sources|
|More fuzzers…|More protocols…|

#BHUSA  @BlackHatEvents

## Slide 17

## **CodeQL**

###### **CodeQL Overview:**

CodeQL is a static analysis tool with powerful data-flow and taint analysis engine to find code errors, check code quality, and identify vulnerabilities.

###### **Modem Exploration Queries:**

###### **General purpose bug finding queries:**

- Finding all task entry points

- ● Finding all Low-level Interrupt Service Routines (LISRs)

- ● Finding all High-level Interrupt Service Routines (HISRs)

- ● Graphing IPC between different tasks

- Identifying memcpy which write to a fixed-size buffer, but use a non-constant size argument

- ● Identifying for loops writing to buffers, where the loop could iterate more times than the size of the buffer

#BHUSA  @BlackHatEvents

## Slide 18

## **Modem Emulator**

###### **Technical Spec**

###### **Benefits & Usages**

- **Unicorn-base full-stack emulation**

   - Supports 5G Modem Chipset (Shannon 5123)

- **Emulates some hardware layers**

   - Hardware Registers

   - PCIE interface

      - Accurate emulation with full symbols vs <u>FirmWire</u> with guessed limited symbols

      - Fuzzing - <u>AFLPlusPlus</u> unicorn mode integration

         - Better code coverage

   - OTP

   - Flash Memory (RFS)

- **Software layer functionalities**

   - Process snapshot and restore - useful for high-speed fuzzing

   - Root Cause Analysis

      - Triaging & Investigation

      - Accurate and fast crash investigation

- ASAN-style instrumentation

#BHUSA  @BlackHatEvents

## Slide 19

## **Modem Emulator Root Cause Analysis**

#BHUSA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
a
a
=
>
ye
ra) | Modem Emulator ~
black hat =
USA 2023 Root Cause Analysis
Heap header corruption at 50596c01 (heap: 50596c00) size: 00000001 value: 000000ad @421e2860 BitUnpacking8+000000cb
None
Memory Dump @50596c00
* Debug Message: Output(®xAD) from Buffer(@xBE) with unpackingLen(8)/unpackedLen( 1206555239) @line @ (BitUnpacking173)
12: BitUnpacking8 return: 0x00000180
2: BitUnpacking8(ProAsnParam_t* asnParam = 505a75a0, unsigned int line = 000005d2, u8 *output = 50596c02, int outputLen = 00000008,
* Instructions @421e285a
421e285a: b #0x421e2874
421e285c: mov fp, r5 american fuzzy lop ++4.0la ault} (python3) [fast]
421e285e: b #0x421e28ae p timing overall results
421€2860: movw r6, #0x48ae ® days, 7 hrs, 46 min, 31 sec
421e2864: subs r7, r7, r3 ® days, @ hrs, @ min, 34 sec 639
421e2866: movt r6, #0x4032 @ days, @ hrs, 7 min, @ sec
421e286a: ldrb r6, [r6, r3] Seets araareee @ days, 4 hrs, 39 min, 2 sec voce 5)
sone, wn ee v6, e8 619.1 (96.9%) 0.83% / 11.21%
: ae 1 (0.16%) 4.97 bits/tuple
CEC LO3 VETS Uy 7 stage progress ini s in depth
421e2874: strb r6, [r2] splice 4 354 (55.40%)
CERCA (ek Op Cab eh ne! 188/441 (42.63%) 524 (82.00%)
421e287a: movs r7, #8 3.31M
421e287c: str r2, [sp, #0x18] 212.5/sec 54.3k (358 saved)
421e287e: movw r2, #0x9464 ) strategy yields m geometry
disabled (default, enable with 12
disabled (default, enable with 191
disabled (default, enable with 1
disabled (default, enable with 638
n/a Q
547/1.68M, 119/1.61M
unused, unused, unused, unused
2.03%/3823, disabled
```

## Slide 20

# Our Findings

#BHUSA  @BlackHatEvents

## Slide 21

_Re: ASN.1_ “Maybe all the bugs are gone…?”

How to Hack Shannon Baseband (from a Phone) OffensiveCon Presentation by Google Project Zero (May, 2023)

(~12 months after the Android Red Team Engagement)

#BHUSA  @BlackHatEvents

## Slide 22

### **Findings Summary**

##### **By the numbers:**

122 18% 50
Total Issues Critical/High Severity Fuzzer Bugs

Two bugs in particular stood out in this engagement, and when chained, led to a Modem RCE.

- **CVE-2022-20170** is a critical severity issue. This is an OOB write issue that occurs when decoding the OTA packets from 2G (GSM).

- **CVE-2022-20405** is a moderate severity issue that is the result of a mis-configuration in modem code makes most of the memory space with RWX.

All vulnerabilities mentioned in this presentation have been fixed

#BHUSA  @BlackHatEvents

## Slide 23

### **CVE-2022-20170 Details**

- Linear OOB write in the heap

**… if (param_2 == 0x70) { target_buffer = AsnInnerMemAlloc(param_1, 1); Allocate 1-byte buffer if (target_buffer == 0x0) goto LAB_XXXXXXX; *(unsigned char *)target_buffer = 0; iVar1 = AsnDecodeInformationElement(param_1, param_3, target_buffer, 0); … int AsnDecodeInformationElement(void *param_1, int param_3, void *target_buffer, int param_4) { … target_lenght = 0;** **ret_val = BitUnpacking8(param_1, 0x5ca, &target_lenght, 8, ret_val); Extract number of bytes to write into the buffer if ((ret_val != -1) && ((target_lenght < 0x81 || (ret_val = Decoding_String_Lpart(param_1, ret_val, &target_lenght), ret_val != -1)))) {** **ret_val = BitUnpacking(param_1, 0x5d2, target_buffer, target_lenght << 3, ret_val); Overflow the buffer return ret_val; }**

- Happens during ASN.1 parsing of Information Element during call setup stage in 2G stack

- ● The attacker fully controls up to 255 bytes written into 1-byte buffer in the heap

#BHUSA  @BlackHatEvents

## Slide 24

### **Heap Management Overview**

- Every heap allocation is prepended with a 0x20-byte header with the metadata ○ Allocation driver ID: partitioned memory driver, system dynamic memory driver, etc

- ○ Size of allocated chunk

   - Allocation-driver-specific metadata

5079f380: **04 00** 00 00 05 00 00 00 8F 2B 29 41 34 00 00 00 5079f390: C0 76 61 44 40 00 00 00 B0 4A 03 00 AA AA AA AA 5079f3a0: 00 01 3C 01 AA AA AA AA AA AA AA AA AA AA AA AA 5079f3b0: AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA

**Allocation heap header Allocated heap buffer**

###### **Partitioned Memory Driver:**

- manages arrays of fixed-size memory blocks

- ● tracks state of the memory blocks using a separate bitmap

- not very convenient for exploitation

- **System Dynamic Memory Driver:**

- ● uses a double-linked list to manage allocated/free chunks

- **heap header contains the double-linked list and free function pointer!!!**

#BHUSA  @BlackHatEvents

## Slide 25

### **Getting Arbitrary Write Primitive**

- Leverage the linear OOB write in the heap to obtain write-what-where primitive: ○ CVE-2022-20170 enables us to overwrite heap header of the next adjacent chunk with the fully controlled data

- The overwritten adjacent heap chunk is:

   - Conveniently allocated by ASN.1 parsing code **before** the buffer overflow happens

   - ○ Reliably freed **after** the overflow

- Use the “classic” heap unlink technique to overwrite free function pointer

5079f380: 04 00 00 00 05 00 00 00 8F 2B 29 41 34 00 00 00 5079f390: C0 76 61 44 40 00 00 00 B0 4A 03 00 AA AA AA AA 5079f3a0: 00 01 3C 01 AA AA AA AA AA AA AA AA AA AA AA AA 5079f3b0: AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA

**Vulnerable heap buffer**

###### **Overflow direction**

5079f3c0: **04 00** 00 00 0C 00 00 00 8F 2B 29 41 3D 00 00 00 5079f3d0: C0 76 61 44 40 00 00 00 B1 4A 03 00 AA AA AA AA 5079f3e0: 3C 01 3C 01 00 00 01 00 AA AA AA AA AA AA AA AA 5079f3f0: AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA

**Header of the adjacent heap chunk**

#BHUSA  @BlackHatEvents

## Slide 26

### **Getting RCE on Modem**

###### **CVE-2022-20170 + CVE-2022-20405 Overview**

- Out-of-bounds write occurs in the **ASN decoder within the 2G stack** (CVE-2022-20170). This allows us to write a limited number of controlled bytes in the heap and corrupt adjacent heap objects.

- Corrupted adjacent heap objects give us arbitrary pointer write primitive when those objects are freed.

- **Misconfiguration in MMU** (CVE-2022-20405) allows us to stage executable shellcode in the heap.

- Overwrite the function pointer pointing to the free function of the heap allocator to point to our shell code

- When a heap object is freed, it will execute our shellcode.

#BHUSA  @BlackHatEvents

## Slide 27

### **Shellcode Delivery**

Malicious base station Victim device
Send stage 0 shellcode
Store stage 0 shellcode
in a global “attack” buffer *
Trigger CVE-2022-20170
Hook free function with
stage 0 shellcode
Send stage 1 shellcode chunk 0
Assemble stage 1 shellcode
in executable memory
...
Send stage 1 shellcode chunk N
Rehook free function
with stage 1 shellcode

_* Global array of ~80 bytes at a known address used for storing stage 0 and chunks of stage 1 shellcode_

#BHUSA  @BlackHatEvents

## Slide 28

# Modem RCE Proof of Concept

#BHUSA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2023
CNDROID B
GD) TECM
Modem RCE Proof of Concept
#BHUSA @BlackHatEvents
```

## Slide 29

## **Attack Chain**

User connects their phone to a **1** cellular network (e.g. 4G/5G)

Attacker sets up a malicious **2** 2G base station

OTP:
1234

**5**

**3**

**2G**

**4**

Attacker can capture and forward SMS messages (+more)

User (victim) comes in proximity of malicious base station. Victim’s phone connects to the malicious base station.

OTP:
1234

Attacker sends exploit payload. Establishes foothold on victim’s modem

#BHUSA  @BlackHatEvents

## Slide 30

#BHUSA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
“Sees - eeae
Trem 2 2 SO
Attacker can now target ®
Victini's apps supporting
SMS MFA ¥
CiNOROID © *“#@e@60
2G5 TEqGnm . .
```

## Slide 31

## **Exploitation Details**

###### **Prerequisites:**

- 2G stack is enabled (default on Pixel 6)

- “Nearby range” to deploy the attack (<5 miles)

###### **Impact:**

- Total modem firmware compromise

- ● Possible Android OS compromise with radio driver/HAL side issues

###### **Issues utilized for this exploit:**

- An attacker controlled heap OOB write in GSM code (CVE-2022-20170)

- A mis-configuration of MMU allowing writable and executable memory (CVE-2022-20405)

- ● Lack of standard security mitigations making the exploiting easier

2G
<5 Mile Range

#BHUSA  @BlackHatEvents

## Slide 32

## **Proof of Concept Setup**

###### Required hardware:

- SDR

- Cables and USB hubs

- Faraday cage (not needed for real attack)

###### Required software:

- OpenBTS (free, open source)

**Total cost** : <$2,800

#BHUSA  @BlackHatEvents

## Slide 33

### **Exploitation Challenges**

- Not that easy to pack SDR, the attacker and victim devices into the Faraday cage to avoid interference

   - Subject to the value of the radio wavelength

- Reliability of the exploitation and time between iterations

   - Multiple complex systems involved into the exploitation: SDR + OpenBTS & modem

- Debugging shellcode on the production modem image

   - Collect ramdump when modem crash and then check the memory status

   - ○ Patched an AT command handler in modem to confirm success of the exploitation locally on the victim device

- 80 bytes of thumb2 instructions is very tight to implement stage 0 shellcode

   - Effective shellcode area is less than 80 bytes due to specifics on heap “unlink” primitive

#BHUSA  @BlackHatEvents

## Slide 34

# Remediation & What Comes Next

#BHUSA  @BlackHatEvents

## Slide 35

## **What You Can Do**

Google is committed to making the Pixel modem as secure as possible. Here’s what you can do:

- 2G security is obsolete. The 2G standards didn’t take in account rogue cell towers as an attack vector (lack of mutual auth)

- Weak encryption combined with no authentication between device and tower means impersonation is easy over 2G.

- 2G is optional on Pixel devices. Disable the “Allow 2G” toggle on your device. This feature is supported in all Android (12+) devices with Radio HAL >1.6

The best mitigation is to disable 2G on your device

- 2G disablement isn’t enforced as it’s required in certain locations

#BHUSA  @BlackHatEvents

## Slide 36

## **Bare Metal Mitigations**

###### **Android Security prioritizes** **<u>hardening bare metal f</u> i** **<u>rmware</u>**

- System hardening and exploit mitigations

- ● Exploring and enabling compiler-based sanitizers ( BoundSan, IntSan) and other exploit mitigations ( CFI, kCFI, Shadow Call Stack, Stack Canaries) in firmware.

- Enabling further memory safety features ( Auto-initialize Memory) in firmware.

- ● Exploring the application of Rust in bare metal firmware.

#BHUSA  @BlackHatEvents

## Slide 37

Cross-Functional Coverage
Upstream  Threat  Vendor
Build  Modeling Security
Support Workshops
Vulnerability
Vulnerability Rewards  Android Red
Rewards Program Team
Program Modem
Vendor
Continuous  Static
Security
Continuous  Analysis
Reviews Fuzzing
Fuzzing
#BHUSA  @BlackHatEvents

## Slide 38

# Conclusion

#BHUSA  @BlackHatEvents

## Slide 39

## **Concluding Thoughts**

###### **Red Team to Secure Pixel**

**2G security is outdated**

###### **Our Work is Never done**

~100 security issues were identified and **fixed in Pixel 6** **<u>before</u> its release** Exploit development helps articulate impact

Google has protections in place to limit the outdated security and lack of mutual authentication of 2G. **Turning off 2G protects you from most attacks.**

Many Google teams came together on these security investments prioritizing security and remediation

We’re never done! The team continues testing new features and releases

###### **Fuzzing is the Way**

###### **Modem mitigations**

We heavily invested in fuzzing, developing 8 fuzzers identifying >60% of bugs logged during the engagement. These fuzzers run continuously and find issues today.

We applied various mitigations to eradicate entire classes of vulnerabilities, with more hardening measures to come.

#BHUSA  @BlackHatEvents

## Slide 40

# Acknowledgements

- **Android Red Team**

- **Connectivity Security Team**

- **Pixel Engineering & Security Team**

- **● Android Security**

- **Project Zero**

- **External Partners**

#BHUSA  @BlackHatEvents

## Slide 41

# Thanks!

#BHUSA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2023
ANDROID ww
RED TEaAn Thanks!
#BHUSA @BlackHatEvents
```
