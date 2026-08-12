---
title: "All Your Secrets Belong to Us Leveraging Firmware Bugs to Break TEEs"
speakers: ["Tom Dohrmann"]
conference: "Black Hat"
conference_full: "Black Hat USA 2024"
edition: "USA"
year: 2024
source_pdf: "Black Hat USA 2024 slides/Tom Dohrmann_All Your Secrets Belong to Us Leveraging Firmware Bugs to Break TEEs.pdf"
pages: 58
sha256: "1bc4dae0b30dcfe2930f03c1c44df33b455c37f02c2fd878fd65ed3afba3cdee"
text_chars: 29934
ocr_pages: 4
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:39:31Z"
---
# All Your Secrets Belong to Us Leveraging Firmware Bugs to Break TEEs

**Speakers:** Tom Dohrmann  
**Conference:** Black Hat USA 2024  
**Source:** `Black Hat USA 2024 slides/Tom Dohrmann_All Your Secrets Belong to Us Leveraging Firmware Bugs to Break TEEs.pdf` (58 pages)

## Slide 1

All Your Secrets Belong to Us: Leveraging Firmware Bugs to Break TEEs

Tom Dohrmann

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blackhat } # +
USA 2024
AUGUST 7-8, 2024
BRIEFINGS
All Your Secrets Belong to Us:
Leveraging Firmware Bugs to Break TEEs
Tom Dohrmann
#BHUSA @BlackHatEvents
```

## Slide 2

# whoami

- Tom Dohrmann

- Low-level enthusiast

- Coding

- Hacking

#BHUSA @BlackHatEvents

## Slide 3

# Outline

- Short Intro to TEEs and AMD SEV-SNP

- Prerequisites

   - Platform Security Processor & Firmware

   - Reverse Map Table

- Bug #1

   - Simple Exploit

   - Improved Exploit

- Bug #2

   - Exploit

- Wrap-up and take-aways

#BHUSA @BlackHatEvents

## Slide 4

# What‘s a TEE Anyway?

- TEE = Trusted Execution Environment

- A secure area of a main processor

- Workloads are protected from conventionally privileged parts of an OS e.g. the kernel

- • For a lot of applications leakage of secrets is a bad as arbitrary code execution.

- Many implementations:

- AMD SEV(-ES/-SNP)

- Intel SGX, Intel TDX → “Compromising Confidential Compute, One Bug at a Time”

- Arm TrustZone, Arm CCA

- IBM SE

- RISC-V CoVE

- NVIDIA H100

#BHUSA @BlackHatEvents

## Slide 5

# Very Short Intro to AMD SEV-SNP

- AMD SEV-SNP implements a Trusted Execution Environment (TEE).

- It aims to shield protected virtual machines from untrusted and even malicious hypervisors.

- All data and code is encrypted and integrity protected.

- Upon creation of a VM, the initial memory contents are measured and can be verified through attestation reports.

#BHUSA @BlackHatEvents

## Slide 6

# Platform Security Processor (PSP)

- The Platform Security Processor is a highly privileged components of AMD SoCs.

- In the context of SEV, the PSP implements the root of trust and is required to create, attest, migrate, delete SEV-SNP virtual machines.

- The SEV firmware is also used with the SEV-SNP’s predecessors, SEV and SEV-ES.

- The firmware can be live-updated.

- Parts of the firmware were published in August 2023.

#BHUSA @BlackHatEvents

## Slide 7

# Reverse Map Table (RMP)

- The RMP is used to protect the integrity of memory.

- It contains an entry for every guest-assignable page of memory to track its state.

- Before every write access, the CPU checks the RMP to decide whether the access is allowed. These checks are done for all privilege levels including hypervisor and SMM accesses.

- The firmware is more privileged and can write to any memory → It needs to do these checks manually.

- The RMP is managed by the CPU through special instructions and by the SEV firmware.

- A lot of trust is put into the RMP permission and state checks being enforced correctly (foreshadowing!).

#BHUSA @BlackHatEvents

## Slide 8

# Reverse Map Table (RMP)

#### • Each page can be owned by the hypervisor, a virtual machine, or the SEV firmware.

Hypervisor 0x000000-0x1FFFFF
Guest ASID=1 0x200000-0x3FFFFF
Firmware 0x400000-0x5FFFFF
Guest ASID=1 0x600000-0x7FFFFF
Hypervisor 0x800000-0x9FFFFF
Hypervisor 0xA00000-0xBFFFFF
Guest ASID=2 0xC00000-0xDFFFFF
Firmware 0xE00000-0xFFFFFF
… …

#BHUSA @BlackHatEvents

## Slide 9

### CVE-2024-21980

#BHUSA @BlackHatEvents

## Slide 10

# Command Dispatch

#### 1. The hypervisor writes the request to memory.

0x0000 0x1000 0x2000 1 0x3000 Hypervisor 0x4000 0x5000 0x6000 Firmware 0x7000

#BHUSA @BlackHatEvents

## Slide 11

# Command Dispatch

0x0000
0x1000
0x2000
1 2
0x3000
Hypervisor
0x4000
8
3 7
0x5000
4
0x6000
Firmware
0x7000
6
5

1. The hypervisor writes the request to memory. 2. The hypervisor donates the page to the firmware. 3. The hypervisor tells the firmware about the request.

4. The firmware reads the request.

5. The firmware processes the request.

6. The firmware writes the response back.

7. The firmware tells the hypervisor it’s done.

8. The hypervisor reads the response.

#BHUSA @BlackHatEvents

## Slide 12

# Command Dispatch

0x0000
0x1000
0x2000
1 2 9
0x3000
Hypervisor
0x4000
8
3 7
0x5000
4
0x6000
Firmware
0x7000
6
5

1. The hypervisor writes the request to memory. 2. The hypervisor donates the page to the firmware.

3. The hypervisor tells the firmware about the request.

4. The firmware reads the request.

5. The firmware processes the request.

6. The firmware writes the response back.

7. The firmware tells the hypervisor it’s done.

8. The hypervisor reads the response.

9. The hypervisor asks the firmware to reclaim the page.

TL;DR: Command requests and responses are written to regular memory.

- → During step 6, the firmware needs to check whether it’s allowed to write to memory.

#BHUSA @BlackHatEvents

## Slide 13

# Command Dispatch (w/o Response)

1. The hypervisor writes the request to memory. 0x0000
2. The hypervisor donates the page to the firmware. 0x1000
3. The hypervisor tells the firmware about the request. 0x2000
1 2 9
4. The firmware reads the request. 0x3000
Hypervisor
5. The firmware processes the request. 0x4000
8
3 7
6. The firmware writes the response back. 0x5000
4
7. The firmware tells the hypervisor it’s done. 0x6000
Firmware
8. The hypervisor reads the response. 0x7000
6
5

- 5

- ~~9. The hypervisor reclaims the page.~~ → The firmware only has to check the RMP if it writes back a response.

#BHUSA @BlackHatEvents

## Slide 14

## Bug #1 One Of These It Not Like The Others…

|Command|Buffer Type|RMP Write Checks|
|---|---|---|
|INIT|Input Only|No|
|SHUTDOWN|Ignore|No|
|PLATFORM_RESET|Ignore|No|
|PLATFORM_STATUS|Output Only|Yes|
|…|…|…|
|ATTESTATION|Input & Output & Error|No|
|SEND_START|Input & Output & Error|Yes|
|SEND_UPDATE_DATA|Input & Output & Error|Yes|
|SEND_UPDATE_VMSA|Input & Output & Error|Yes|

#BHUSA @BlackHatEvents

## Slide 15

# Command Dispatch

~~1. The hypervisor writes the request to memory.~~

0x0000 0x1000 0x2000 ~~1~~ 0x3000 Hypervisor 0x4000 0x5000 0x6000 Firmware 0x7000

#BHUSA @BlackHatEvents

## Slide 16

# Command Dispatch

1. The hypervisor writes the request to memory. 0x0000
2. The hypervisor donates the page to the firmware. 0x1000
3. The hypervisor tells the firmware about the request. 0x2000
1 2
4. The firmware reads the request. 0x3000
Hypervisor
5. The firmware processes the request. 0x4000
8
3 7
6. The firmware writes the response back. 0x5000
4
7. The firmware tells the hypervisor it’s done. 0x6000
Firmware
8. The hypervisor reads the response. 0x7000
6
5

#BHUSA @BlackHatEvents

## Slide 17

# Command Dispatch

1. The hypervisor writes the request to memory. 0x0000
2. The hypervisor donates the page to the firmware. 0x1000
3. The hypervisor tells the firmware about the request. 0x2000
1 2 9
4. The firmware reads the request. 0x3000
Hypervisor
5. The firmware processes the request. 0x4000
8
3 7
6. The firmware writes the response back. 0x5000
4
7. The firmware tells the hypervisor it’s done. 0x6000
Firmware
8. The hypervisor reads the response. 0x7000
6
5

- 5

- ~~9. The hypervisor asks the firmware to reclaim the page.~~ → The firmware just corrupted the memory of a protected guest.

#BHUSA @BlackHatEvents

## Slide 18

# Primitive Exploit

Hypervisor

ATTESTATION

Guest Memory

result=0x000000d0

SEV Firmware

The value is fixed, but we can choose the location (with some limitations).

#BHUSA @BlackHatEvents

## Slide 19

# Choosing a Target

- It’s not always easy to know what each guest memory region contains.

Kernel Code?
0x000000-0x1FFFFF
0x200000-0x3FFFFF
User Data?
0x400000-0x5FFFFF
0x600000-0x7FFFFF
Kernel Data?
0x800000-0x9FFFFF
0xA00000-0xBFFFFF
Secrets?
0xC00000-0xDFFFFF
0xE00000-0xFFFFFF
User Code?

#BHUSA @BlackHatEvents

## Slide 20

# Choosing a Target

• The attacker has very little control over the plaintext values for the corrupted ciphertext.

Ciphertext Plaintext
6D 4A 0D CE F9 82 C2 53 ... 55 48 89 E5 48 83 EC 10 ...
Ciphertext Plaintext
D0 00 00 00 C3 2F 1E 81 ... CC 54 C3 D4 B5 D2 29 06 ...

#BHUSA @BlackHatEvents

## Slide 21

Attacking the guest directly is possible, but … … It’s far from trivial and … … Exploits will likely have to be tailored to specific workloads.

#BHUSA @BlackHatEvents

## Slide 22

# Attacking the Firmware

Hypervisor

ATTESTATION

SEV Firmware

Guest Memory

result=0x000000d0

#BHUSA @BlackHatEvents

## Slide 23

# Guest Context Pages

- Guest context pages contain metadata about a guest.

- Marked as owned by the SEV firmware in the RMP using a special _CONTEXT_ state.

- Guest context pages are encrypted.

#BHUSA @BlackHatEvents

## Slide 24

# Guest Context Pages

|||||||U|MC K|eySe|ed|||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|51|7E|7B|D1|B1|66|DA
Offlin|FE
e Enc|05
ryptio|D3
n Key|E8|A3|F7|AE|E5|CA|
|16|04|B4|B1|51|3C|05|21|76|EA|A4|9F|28|20|CD|54|
|||||||L|…
aunch|Dige|st|||||||
|81|B6|EC|B6|BD|D9|93|20|C0|D1|C6|57|54|3D|C1|23|
||||||||…|||||||||
|||Offlin|e En|cryptio|n IV||||Han|dle|||Pol|icy||
|00|00|00|00|00|00|00|00|00|00|00|00||SM|T||
||St|ate|||AS|ID|||CC|Xs|||Guest|Flags||
||RUN|NING||D6|01|00|00|FF|00|00|00||SEV|-ES||

…

<u>#BHUSA @BlackHatEvents</u>

## Slide 25

# Guest Context Pages

|||||||U|MC K|eySe|ed|||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|51|7E|7B|D1|B1|66|DA
Offlin|FE
e Enc|05
ryptio|D3
n Key|E8|A3|F7|AE|E5|CA|
|16|04|B4|B1|51|3C|05|21|76|EA|A4|9F|28|20|CD|54|
|||||||L|…
aunch|Dige
|st|||||||
|81|B6|EC
Offlin|B6
e En|BD
cryptio|D9
n IV|93|20
…|C0
|D1
Han|C6
dle|57|54|3D
Pol|C1
icy|23|
|00|00|00|00|00|00|00|00|00|00|00|00||SM|T||
||St|ate|||AS|ID|||CC|Xs|||Guest|Flags||
||RUN|NING||D6|01|00|00|FF|00|00|00||SEV|-ES||

…

<u>#BHUSA @BlackHatEvents</u>

## Slide 26

# Guest Context Pages

UMC Key Seed 51 7E 7B D1 B1 66 DA FE 05 D3 E8 A3 F7 AE E5 CA Offline Encryption Key 16 04 B4 B1 51 3C 05 21 76 EA A4 9F 28 20 CD 54

- When the guest is created, the firmware uses a secure RNG to generate the UMC key seed.

- Before the guest is first used, the firmware programs the UMC key seed into all the Unified Memory Controllers (UMC) on the platform.

- The UMCs use this key seed to derive the guest’s encryption key.

#BHUSA @BlackHatEvents

## Slide 27

# Guest Context Pages

|||||||U|MC K|eySe|ed|||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|51|7E|7B|D1|B1|66|DA
Offlin|FE
e Enc|05
ryptio|D3
n Key|E8|A3|F7|AE|E5|CA|
|16|04|B4|B1|51|3C|05|21|76|EA|A4|9F|28|20|CD|54|
|||||||L|…
aunch|Dige
|st|||||||
|81|B6|EC
Offlin|B6
e En|BD
cryptio|D9
n IV|93|20
…|C0
|D1
Han|C6
dle|57|54|3D
Pol|C1
icy|23|
|00|00|00|00|00|00|00|00|00|00|00|00||SM|T||
||St|ate|||AS|ID|||CC|Xs|||Guest|Flags||
||RUN|NING||D6|01|00|00|FF|00|00|00||SEV|-ES||

…

<u>#BHUSA @BlackHatEvents</u>

## Slide 28

# Guest Context Pages

|||||||U|MC Ke|ySe|ed|||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D0
|00
|00
|00
|B1
|66
|DA
Offlin
|FE
e Encr
|05
 yptio
|D3
n Key
|E8
|A3
|F7
|AE
|E5
|CA
|
|16|04|B4|B1|51|3C|05|21|76|EA|A4|9F|28|20|CD|54|
|||||||L|…
aunch|Dige
|st
|||||||
|81|B6|EC|B6|BD|D9|93|20|C0|D1|C6|57|54|3D|C1|23|
|||Offlin|e En|cryptio|n IV||…||Han|dle|||Pol|icy||
|00|00|00|00|00|00|00|00|00|00|00|00||SM|T||
||St|ate|||AS|ID|||CC|Xs|||Guest|Flags||
||RUN|NING||D6|01|00|00|FF|00|00|00||SEV|-ES||

…

<u>#BHUSA @BlackHatEvents</u>

## Slide 29

# Guest Context Pages

|||||||U|MC Ke|ySe|ed|||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D0
|D0
|00
|00
|00
|66
|DA
Offlin
|FE
e Encr
|05
 yptio
|D3
n Key
|E8
|A3
|F7
|AE
|E5
|CA
|
|16|04|B4|B1|51|3C|05|21|76|EA|A4|9F|28|20|CD|54|
|||||||L|…
aunch|Dige
|st
|||||||
|81|B6|EC|B6|BD|D9|93|20|C0|D1|C6|57|54|3D|C1|23|
|||Offlin|e En|cryptio|n IV||…||Han|dle|||Pol|icy||
|00|00|00|00|00|00|00|00|00|00|00|00||SM|T||
||St|ate|||AS|ID|||CC|Xs|||Guest|Flags||
||RUN|NING||D6|01|00|00|FF|00|00|00||SEV|-ES||

…

<u>#BHUSA @BlackHatEvents</u>

## Slide 30

# Guest Context Pages

|||||||U|MC Ke|ySe|ed|||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D0
|D0
|D0
|00
|00
|00
|DA
Offlin
|FE
e Encr
|05
 yptio
|D3
n Key
|E8
|A3
|F7
|AE
|E5
|CA
|
|16|04|B4|B1|51|3C|05|21|76|EA|A4|9F|28|20|CD|54|
|||||||L|…
aunch|Dige
|st
|||||||
|81|B6|EC|B6|BD|D9|93|20|C0|D1|C6|57|54|3D|C1|23|
|||Offlin|e En|cryptio|n IV||…||Han|dle|||Pol|icy||
|00|00|00|00|00|00|00|00|00|00|00|00||SM|T||
||St|ate|||AS|ID|||CC|Xs|||Guest|Flags||
||RUN|NING||D6|01|00|00|FF|00|00|00||SEV|-ES||

…

<u>#BHUSA @BlackHatEvents</u>

## Slide 31

# Guest Context Pages

|||||||U|MC Ke|ySe|ed|||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D0
|D0
|D0
|D0
|00
|00
|00
Offlin
|FE
e Encr
|05
 yptio
|D3
n Key
|E8
|A3
|F7
|AE
|E5
|CA
|
|16|04|B4|B1|51|3C|05|21|76|EA|A4|9F|28|20|CD|54|
|||||||L|…
aunch|Dige
|st
|||||||
|81|B6|EC|B6|BD|D9|93|20|C0|D1|C6|57|54|3D|C1|23|
|||Offlin|e En|cryptio|n IV||…||Han|dle|||Pol|icy||
|00|00|00|00|00|00|00|00|00|00|00|00||SM|T||
||St|ate|||AS|ID|||CC|Xs|||Guest|Flags||
||RUN|NING||D6|01|00|00|FF|00|00|00||SEV|-ES||

…

<u>#BHUSA @BlackHatEvents</u>

## Slide 32

# Guest Context Pages

|||||||U|MC K|eySe|ed|||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D0
|D0
|D0
|D0
|D0
|D0
|D0
Offlin
|D0
e Enc
|D0
ryptio
|D0
n Key
|D0
|D0
|D0
|D0
|D0
|D0
|
|00|00|00|B1|51|3C|05|21|76|EA|A4|9F|28|20|CD|54|
|||||||L|…
aunch|Dige
|st|||||||
|81|B6|EC|B6|BD|D9|93|20|C0|D1|C6|57|54|3D|C1|23|
|||Offlin|e En|cryptio|n IV||…||Han|dle|||Pol|icy||
|00|00|00|00|00|00|00|00|00|00|00|00||S|MT||
||St|ate|||AS|ID|||CC|Xs|||Guest|Flags||
||RUN|NING||D6|01|00|00|FF|00|00|00||SEV|-ES||

…

<u>#BHUSA @BlackHatEvents</u>

## Slide 33

Guest Context Pages Identical Key Seeds = Identical Encryption Keys

UMC Key Seed UMC Key Seed
D0 D0 D0 D0 D0 D0 D0 D0 D0 D0 D0 D0 D0 D0 D0 D0 D0 D0 D0 D0 D0 D0 D0 D0 D0 D0 D0 D0 D0 D0 D0 D0
Offline Encryption Key Offline Encryption Key
00 00 00 B1 51 3C 05 21 76 EA A4 9F 28 20 CD 54 00 00 00 B1 51 3C 05 21 76 EA A4 9F 28 20 CD 54
… …
Launch Digest Launch Digest
81 B6 EC B6 BD D9 93 20 C0 D1 C6 57 54 3D C1 23 81 B6 EC B6 BD D9 93 20 C0 D1 C6 57 54 3D C1 23
… …
Offline Encryption IV Handle Policy Offline Encryption IV Handle Policy
00 00 00 00 00 00 00 00 00 00 00 00 SMT 00 00 00 00 00 00 00 00 00 00 00 00 SMT | DEBUG
State ASID CCXs Guest Flags State ASID CCXs Guest Flags
RUNNING D6 01 00 00 FF 00 00 00 SEV-ES RUNNING D6 01 00 00 FF 00 00 00 SEV-ES
… …

Victim guest

Attacker guest with debugging enabled

#BHUSA @BlackHatEvents

## Slide 34

# Guest Context Pages

- Guest context pages contain metadata about a guest.

- Marked as owned by the SEV firmware in the RMP using a special _CONTEXT_ state.

- **Guest context pages are encrypted.**

Ciphertext
UMC Key Seed
D0 D0 D0 D0 D0 D0 D0 D0 ...

Plaintext

UMC Key Seed 3A CB 3E 3D F6 8F 1F BC ...

#BHUSA @BlackHatEvents

## Slide 35

# Location-Dependent Encryption

- All guest context pages are encrypted using the same key, but use a physical-addressdependent IV.

IV=f(0x2000)

Ciphertext at 0x2000 IV=f(0x2000) Plaintext at 0x2000 UMC Key Seed UMC Key Seed D0 D0 D0 D0 D0 D0 D0 D0 ... 0F 50 3A A0 2A 0A 01 15 ... Ciphertext at 0x5000 IV=f(0x5000) Plaintext at 0x5000 UMC Key Seed UMC Key Seed D0 D0 D0 D0 D0 D0 D0 D0 ... 3A CB 3E 3D F6 8F 1F BC ...

- → We have to use the same physical address for the guest and attacker context pages.

- → We have to shut the victim guest down before starting the attack guest.

#BHUSA @BlackHatEvents

## Slide 36

# Improved Exploit

1. Launch victim guest.

2. Corrupt _UMC key seed_ with fixed values.

3. Run victim guest and records its encrypted memory.

4. Decommission victim guest.

5. Launch attacker guest at the same location with debug options enabled.

6. Corrupt _UMC key seed_ with the same fixed values.

7. Use debug commands with the attacker guest to decrypt the memory of the victim guest.

#BHUSA @BlackHatEvents

## Slide 37

# Demo

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
root@server:~/firmware-vuln-poc# cargo run -- --pfn 0x171a24
F
inished dev [unoptimized + debuginfo] target(s) in 0.03s
Creating VM with identical UMC key seed
Raw
000:
p
020:
040:
060:
080:
Oad:
OcO0:
Oe0:
100:
120:
140:
160:
age:
0300000000000000110 Fa00000000000000000000000000000000000a98d95 f F
29d761f0c5bdc1b4b4a69 fd2f37c829cab6d30d439252f7daefd72fcd45262053
3c10be491d825e35ea4166261486e417187c679efcc2d2be8553f32c2c62bbFf3
27ac6d99214a2cel1fc37d35a94475ff377e67caacc43add86e908a9369207343
14c197f fbcfade378bd1b33819051d5d3628b5eb7 1la0b84daefed27671e8e202
DONDNDDDNDNDDD0D0D0D0D0000000000000000000000000000000000000000000
DONDDDNDDDDDDDDD0D0D000000000000000000000000000000000000000000000
DDDDDDNDDDDNDDDDDDDDD0DDDDDDD0DDDD0D0DD0D000000000000000000000000
000000000080008800000000eef FOOOO TOT TT tft ttt ttf ttf ff3fO0O0000000000
DNDNDDDNDDDDD0D0000000000000000000000000000000000000000000000000
DNDNDNDDDDDDDDD0D0D000000000000000000000000000000000000000000000
C8DNDNDDDDNDDDDDDDDDDDDDDDDDDD0DD0DDDD0D000D0000000000000000000000
```

## Slide 38

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
Secrets page:
imi en: false
FMS: 00a00f11
gosvw: 000000000000000000000000a98d95 fF F
vmpck@: 29d761f0c5bdc1b4b4a69 fd2 f37c829ca6d30d439252f7daefd72fcd45262053
vmpckl: 3c10be491d825e35ea4166261486e417187c679ef cc2d2be8553F32c2c62bbf3
vmpck2: 27ac6d99214a2celfc37d35a944/5fF377e6/caacc43add86e908a9369207343
vmpck3: 14c197ffbcfade378bd1b33819051d5d3628b5eb7 1la0b84daefed27671e8e202
VMSA tweak bitmap: 000000000080008800000000eef FOOOO TOF fF fff ttttttttfff3foo
000000000000000000000000000000
tsc factor: 200
```

## Slide 39

### CVE-2024-21978

#BHUSA @BlackHatEvents

## Slide 40

# Bug #2

- The firmware stores some certificates in non-volatile storage.

- The _INIT_EX_ command can be used to ask the firmware to use regular memory instead of on-chip SPI flash for non-volatile storage.

- The hypervisor has to donate memory to the firmware by converting some memory into the _FIRMWARE_ state.

- The firmware only checks that the memory is in the _FIRMWARE_ state when _INIT_EX_ is executed. All following accesses skip the access checks.

- The hypervisor can use the _PAGE_RECLAIM_ command to ask the firmware to convert unused _FIRMWARE_ memory back into hypervisor state.

- → _PAGE_RECLAIM_ doesn’t whether the address is being used for non-volatile storage.

#BHUSA @BlackHatEvents

## Slide 41

# Rough Plan of Attack

1. Convert some memory into the _FIRMWARE_ state.

2. Use that memory with _INIT_EX_ as non-volatile storage.

3. Reclaim the memory using _PAGE_RECLAIM_ .

4. Assign the memory to a guest.

5. Trigger a command that causes the firmware to non-volatile storage.

#BHUSA @BlackHatEvents

## Slide 42

# Can We Better Than Exploit #1?

- Last time we were limited by the fixed value of the memory corruption.

- The _PDH_GEN_ command regenerates some certificates and writes ~3 pages of random data to the memory backing used for non-volatile storage.

#BHUSA @BlackHatEvents

## Slide 43

# Guest Context Pages

|||||||U|MC K|eySe|ed|||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|51|7E|7B|D1|B1|66|DA
Offlin|FE
e Enc|05
ryptio|D3
n Key|E8|A3|F7|AE|E5|CA|
|16|04|B4|B1|51|3C|05|21|76|EA|A4|9F|28|20|CD|54|
|||||||L|…
aunch|Dige|st|||||||
|81|B6|EC|B6|BD|D9|93|20|C0|D1|C6|57|54|3D|C1|23|
||||||||…|||||||||
|||Offlin|e En|cryptio|n IV||||Han|dle|||Pol|icy||
|00|00|00|00|00|00|00|00|00|00|00|00||SM|T||
||St|ate|||AS|ID|||CC|Xs|||Guest|Flags||
||RUN|NING||D6|01|00|00|FF|00|00|00||SEV|-ES||

…

<u>#BHUSA @BlackHatEvents</u>

## Slide 44

# Guest Context Pages

|||||||U|MC K|eySee|d|||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|51|7E|7B|D1|B1|66|DA|FE|05|D3|E8|A3|F7|AE|E5|CA|
|||||||Offlin|e Enc|ryptio|n Key|||||||
|16|04|B4|B1|51|3C|05|21
|76
…|EA|A4|9F|28|20|CD|54|

• Corrupting the _UMC key seed_ isn’t very useful because we have no control of the value.

#BHUSA @BlackHatEvents

## Slide 45

# Guest Context Pages

|||||||U|MC K|eySe|ed|||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|51|7E|7B|D1|B1|66|DA
Offlin|FE
e Enc|05
ryptio|D3
n Key|E8|A3|F7|AE|E5|CA|
|16|04|B4|B1|51|3C|05|21|76|EA|A4|9F|28|20|CD|54|
|||||||L|…
aunch|Dige|st|||||||
|81|B6|EC|B6|BD|D9|93|20|C0|D1|C6|57|54|3D|C1|23|
||||||||…|||||||||
|||Offlin|e En|cryptio|n IV||||Han|dle|||Pol|icy||
|00|00|00|00|00|00|00|00|00|00|00|00||SM|T||
||St|ate|||AS|ID|||CC|Xs|||Guest|Flags||
||RUN|NING||D6|01|00|00|FF|00|00|00||SEV|-ES||

…

<u>#BHUSA @BlackHatEvents</u>

## Slide 46

# Guest Context Pages

- After the UMC key seed has been programmed into the UMC, the encryption unit in the memory controller uses the address space identifier ( _ASID_ ) to look up the encryption key for a guest.

|||Offlin|e En|cryptio|n IV||||Han|dle||Policy|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|00|00|00|00|00|00|00|00|00|00|00|00|SMT|
||St|ate|||AS|ID|||CC|Xs||Guest Flags|
||RUN|NING||D6|01|00|00|FF|00|00|00|SEV-ES|

…

<u>#BHUSA @BlackHatEvents</u>

## Slide 47

# Guest Context Pages

- After the UMC key seed has been programmed into the UMC, the encryption unit in the memory controller uses the address space identifier ( _ASID_ ) to look up the encryption key for a guest.

- If we corrupt the _ASID_ we can trick the firmware into using another guest’s encryption keys.

|||Offlin|e En|crypti|on IV||||Han|dle||Policy|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|F7|CC|FD|61|9E|D9|3D|FF|4B|97|D8|AF|VMSA_REG_PROT|
||St|ate|||AS|ID|||CC|Xs||Guest Flags|
||LAU|NCH||45|22|BB|A9|17|63|4B|23|SEV-ES|

…

<u>#BHUSA @BlackHatEvents</u>

## Slide 48

# Guest Context Pages

- After the UMC key seed has been programmed into the UMC, the encryption unit in the memory controller uses the address space identifier ( _ASID_ ) to look up the encryption key for a guest.

- If we corrupt the _ASID_ we can trick the firmware into using another guest’s encryption keys.

- If we also corrupt the _Policy_ we can issue debug commands for that other guest.

|||Offli|ne En|cryptio|n IV||||Han|dle||Policy|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|00|59|EF|80|2C|78|1D|CE|4D|99|67|51|DEBUG|
||Sta|te|||AS|ID|||CC|Xs||Guest Flags|
||IN|IT||E8|5F|73|60|24|87|5B|EA|(empty)|

…

<u>#BHUSA @BlackHatEvents</u>

## Slide 49

# Guest Context Pages

- After the UMC key seed has been programmed into the UMC, the encryption unit in the memory controller uses the address space identifier ( _ASID_ ) to look up the encryption key for a guest.

- If we corrupt the _ASID_ we can trick the firmware into using another guest’s encryption keys.

- If we also corrupt the _Policy_ we can issue debug commands for that other guest.

- There are only relatively few valid _ASID_ s (<509 or <1006 depending on the CPU).

|• We can|query both|the_A_|_SID_an|d the|_policy_|using|the_G_|_UES_|_T_STAT_|_US_command.|
|---|---|---|---|---|---|---|---|---|---|---|
||Offline En|crypti|on IV||||Han|dle||Policy|
|00
59|EF
80|2C|78|1D|CE|4D|99|67|51|DEBUG|
|Sta|te||AS|ID|||CC|Xs||Guest Flags|
|IN|IT|E8|5F|73|60|24|87|5B|EA|(empty)|

…

<u>#BHUSA @BlackHatEvents</u>

## Slide 50

# Guest Context Pages

- After the UMC key seed has been programmed into the UMC, the encryption unit in the memory controller uses the address space identifier ( _ASID_ ) to look up the encryption key for a guest.

- If we corrupt the _ASID_ we can trick the firmware into using another guest’s encryption keys.

- If we also corrupt the _Policy_ we can issue debug commands for that other guest.

- There are only relatively few valid _ASID_ s (<509 or <1006 depending on the CPU).

|• W|e can|query both|the_AS_|_ID_an|d the|_policy_|using|the_G_|_UES_|_T_STA_|_TUS_command.|
|---|---|---|---|---|---|---|---|---|---|---|---|
|||Offline En|cryptio|n IV||||Han|dle||Policy|
|A9|AD|C0
7D|C3|40|CB|45|7E|BC|36|4E|SMT|DEBUG|
||St|ate||AS|ID|||CC|Xs||Guest Flags|
||IN|IT|F7|3E|19|2E|90|B3|52|C4|SEV-ES|

…

<u>#BHUSA @BlackHatEvents</u>

## Slide 51

# Guest Context Pages

- After the UMC key seed has been programmed into the UMC, the encryption unit in the memory controller uses the address space identifier ( _ASID_ ) to look up the encryption key for a guest.

- If we corrupt the _ASID_ we can trick the firmware into using another guest’s encryption keys.

- If we also corrupt the _Policy_ we can issue debug commands for that other guest.

- There are only relatively few valid _ASID_ s (<509 or <1006 depending on the CPU).

|• We can|query both|the_A_|_SID_an|d the|_policy_|using|the_G_|_UES_|_T_STAT_|_US_command.|
|---|---|---|---|---|---|---|---|---|---|---|
||Offline En|crypti|on IV||||Han|dle||Policy|
|A1
12|2B
90|00|7E|AC|F9|9E|FA|CA|73|SMT|
|St|ate||AS|ID|||CC|Xs||Guest Flags|
|RUN|NING|FB|46|05|00|23|73|7A|01|SEV-ES|

…

<u>#BHUSA @BlackHatEvents</u>

## Slide 52

# Guest Context Pages

- After the UMC key seed has been programmed into the UMC, the encryption unit in the memory controller uses the address space identifier ( _ASID_ ) to look up the encryption key for a guest.

- If we corrupt the _ASID_ we can trick the firmware into using another guest’s encryption keys.

- If we also corrupt the _Policy_ we can issue debug commands for that other guest.

- There are only relatively few valid _ASID_ s (<509 or <1006 depending on the CPU).

|• W|e can|Offli
query|ne Encryptio
both the_AS_|n IV
_ID_an|d the|_policy_|usin|Han
g the_G_|dle
_UES_|_T_STA_|Policy
_TUS_command.|
|---|---|---|---|---|---|---|---|---|---|---|---|
|DE|FD|97|D5
8F|B9|1C|F3|D1|7E|91|6E|SMT|DEBUG|
||St|ate||AS|ID|||CC|Xs||Guest Flags|
||IN|IT|89|1E|00|00|88|3F|71|91|(empty)|

…

<u>#BHUSA @BlackHatEvents</u>

## Slide 53

# Guest Context Pages

- After the UMC key seed has been programmed into the UMC, the encryption unit in the memory controller uses the address space identifier ( _ASID_ ) to look up the encryption key for a guest.

- If we corrupt the _ASID_ we can trick the firmware into using another guest’s encryption keys.

- If we also corrupt the _Policy_ we can issue debug commands for that other guest.

- There are only relatively few valid _ASID_ s (<509 or <1006 depending on the CPU).

|• W|e can|query both|the_A_|_SID_an|d the|_policy_|using|the_G_|_UES_|_T_STAT_|_US_command.|
|---|---|---|---|---|---|---|---|---|---|---|---|
|||Offline En|crypti|on IV||||Han|dle||Policy|
|E8|D5|E6
AA|43|CA|81|7E|5D|85|15|06|DEBUG|
||St|ate||AS|ID|||CC|Xs||Guest Flags|
||LAU|NCH|A4|01|00|00|61|3F|08|CF|SEV-ES|

…

<u>#BHUSA @BlackHatEvents</u>

## Slide 54

# Guest Context Pages

- We repeatedly corrupt guest context pages until hit an _ASID_ < 509/1006 and _Policy_ allows debugging.

- The chances of getting everything right are about 1 in 20,000,000.

- We can corrupt 300 guest context pages per second.

- We expect to get a hit about once a day.

- This can be in advance before launching the victim guest.

|||Offli|ne En|cryptio|n IV||||Han|dle||Policy|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|E8|D5|E6|AA|43|CA|81|7E|5D|85|15|06|DEBUG|
||St|ate|||AS|ID|||CC|Xs||Guest Flags|
||LAU|NCH||A4|01|00|00|61|3F|08|CF|SEV-ES|

…

<u>#BHUSA @BlackHatEvents</u>

## Slide 55

Exploit

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
freax13@server :~/code/cve-2024-21978-poc$ bash exploit.sh
Corrupt guest context page so that ASID is in range 1..510
Smallest ASID: Ox0000001f iterations: 14052175 zeros: 10539628 unique asids: 31500727 elapsed time: 1d 19h 20m 31s
Creating VM with same ASID
[03, 00, 00, 00, 00, 00, 00, 00, 11, Of, a0, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00,
00, 00, 00, f0, 51, a5, 03, 3f, 69, 6b, 93, e8, d8, 61, Od, 2e, 5a, 45, fl, ea, 6d, bf, 49, fe, e4, a9, 2d, 8d, af, 7
6, 5e, 2e, 56, e0, fa, a9, b3, a7, e0, bc, 09, d9, 4f, 28, 5c, Of, 84, d2, 7e, 34, eb, ea, 3f, 29, 88, 30, 01, 28, 65
, 8b, 73, 3c, 84, 00, ae, 4a, 74, a2, 7a, dl, c7, 4f, 63, 7f, 72, 7b, 3b, 2f, 08, b3, la, 8c, 99, 1b, ad, b5, 1d, 42,
Ob, 4d, 98, d4, 7d, cl, Ob, d6, 2f, b4, 6c, 6b, 51, a2, 92, 17, 3b, O01, e8, 82, 11, le, cb, cb, a2, 8f, c9, bO, 52,
1d, 1d, b7, d2, 25, 8d, 32, a9, 7a, 6f, 86, e4, 40, 44, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, O
0, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00
, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00,
00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 80, 00,
88, 00, 00, 00, 00, ee, ff, 00, 00, fO, ff, ff, ff, ff, ff, ff, ff, ff, 3f, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 0
0, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00
, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00,
00, 00, 00, 00, 00, 00, 00, 00, 00, 00,00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, O
0, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00,00, 00, 00, 00, 00, 00, 00, 00, 00, 00,
00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00,0
0, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00
, 00, 00, 00, 00, 00, 00, 00, 00, 00,00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00,
00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00,00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00
, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00,00,
00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 0
0, 00, 00, 00, 00, 00, 00, 00, 00,00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00,
```

## Slide 56

# Reusability of Exploits

- The exploits assume very little about the memory corruption:

- Fixed and random writes to RMP-protected memory are exploitable.

- Completely workload-independent

- A third bug I discovered, CVE-2023-31355, can be exploited using strategy #1 with very few changes.

#BHUSA @BlackHatEvents

## Slide 57

# Take-Aways

1. The hypervisor is very powerful: Even very simple bugs can have a large security impact.

2. The firmware used by SEV (and other TEEs) deserves more attention from the researcher community.

3. Demand as much transparency as possible in all parts of the stack.

#BHUSA @BlackHatEvents

## Slide 58

# Thanks & Q/A

- Proof of Concepts are available on GitHub

   - <u>github.com/freax13/cve-2024-21980-poc</u>

   - <u>github.com/freax13/cve-2024-21978-poc</u>

   - <u>github.com/freax13/cve-2023-31355-poc</u>

      - Follow me on Twitter: @13erbse

#BHUSA @BlackHatEvents
