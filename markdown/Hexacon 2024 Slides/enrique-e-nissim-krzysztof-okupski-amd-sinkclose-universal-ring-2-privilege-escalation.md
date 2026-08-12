---
title: "AMD Sinkclose Universal Ring -2 Privilege Escalation"
speakers: ["Enrique E Nissim", "Krzysztof Okupski"]
conference: "Hexacon"
conference_full: "Hexacon 2024"
edition: ""
year: 2024
source_pdf: "Hexacon 2024 Slides/Enrique E Nissim & Krzysztof Okupski_AMD Sinkclose Universal Ring -2 Privilege Escalation.pdf"
pages: 123
sha256: "906fd7f59d9f0283db911e4bb20e5bf20bc844301e0024075103191f66a26d9e"
text_chars: 48499
ocr_pages: 25
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:19:43Z"
---
# AMD Sinkclose Universal Ring -2 Privilege Escalation

**Speakers:** Enrique E Nissim, Krzysztof Okupski  
**Conference:** Hexacon 2024  
**Source:** `Hexacon 2024 Slides/Enrique E Nissim & Krzysztof Okupski_AMD Sinkclose Universal Ring -2 Privilege Escalation.pdf` (123 pages)

## Slide 1

AMD Sinkclose Universal SMM Privilege Escalation

Enrique Nissim `@kiqueNissim` Krzysztof Okupski `@exminium`

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
AMD Sinkclose
Universal SMM Privilege Escalation
Enrique Nissim @kiqueNissim
Krzysztof Okupski @exminium
lOActive.
```

## Slide 2

#### Outline

- Technical background

   - Privilege levels and SMM security

   - Remapping attacks

- Exploitation

   - Exploit development

   - Demo

- Attack paths

- Conclusions

©2024 IOActive, Inc. All Rights Reserved.

2

## Slide 3

©2023 IOActive, Inc. All Rights Reserved. 3

## Slide 4

## SMM Introduction

©2024 IOActive, Inc. All Rights Reserved.

4

## Slide 5

#### Introducing System Management Mode

- One of the most powerful execution modes in x86 `o` Full access to system and I/O device memory `o` Access to the SPI flash (potential for persistence)

- Invisible to the rest of the system `o` Hidden from the OS and Hypervisor `o` EDRs cannot help here

©2024 IOActive, Inc. All Rights Reserved.

5

## Slide 6

#### Privilege levels

Apps
OS
Hypervisor / VMM
SMM

©2024 IOActive, Inc. All Rights Reserved.

6

## Slide 7

Ring 3 Apps
Ring 0 Firmware OS Loader OS
Ring -2 SMM
Boot-time Run-time

©2024 IOActive, Inc. All Rights Reserved.

7

## Slide 8

#### System Management Interrupts

- SMM is entered using a special external interrupt called the systemmanagement interrupt (SMI)

SMM

SW SMI

- After an SMI is received by the processor, the processor saves the processor state in a separate address space, called System Management RAM (SMRAM)

OS

DRAM

©2024 IOActive, Inc. All Rights Reserved.

8

## Slide 9

#### Previous research

- Blogs

   - <u>Exploring the security configuration of AMD platforms</u> (2022)

   - <u>Adventures in the Platform Security Coordinated Disclosure Circus (2023)</u>

   - <u>Back to the Future with Platform Security (2023)</u>

   - <u>Exploring AMD Platform Secure Boot  (2023)</u>

- Couple of CVEs _CVE-2023-20576 CVE-2023-20577 CVE-2023-20587 CVE-2023-20596 CVE-2023-28468 CVE-2023-2290_

_CVE-2023-20579 CVE-2023-31100 CVE-2023-5078_

- Tooling: https://github.com/IOActive/Platbox

©2024 IOActive, Inc. All Rights Reserved.

9

## Slide 10

## SMM Security

©2024 IOActive, Inc. All Rights Reserved.

10

## Slide 11

CPU
SMM

Memory SMRAM Controller

DRAM

©2024 IOActive, Inc. All Rights Reserved.

11

## Slide 12

CPU
Normal mode

Memory
Controller

- Execution disallowed

- Reads FFs

- Writes are discarded

SMRAM

DRAM

©2024 IOActive, Inc. All Rights Reserved.

12

## Slide 13

#### TSEG Region

- How does the memory controller protects SMRAM? `o` At boot-time BIOS configures two registers to setup the TSEG Region

###### MSRC001_0112 SMM TSeg Base Address (SMMAddr)

|**Rsvd**|**TSEG Base**|**Reserved**|
|---|---|---|
|63           39
0||17|

###### MSRC001_0113 SMM TSeg Mask (SMMMask)

Tm Am Tm Am
Rsvd TSEG Mask Rsvd Type Rsvd Type Rsvd Type Type TClose AClose TValid AValid
Dram Dram IoWc IoWc
63           39                            17                                                                                                      4                 3               2              1

0

©2024 IOActive, Inc. All Rights Reserved.

13

## Slide 14

SMI Handlers
SMM Save State (CPUn)
...
SMM Save State (CPU0) SMM Base  + FE00h
SMM Entrypoint (CPUn)
TSeg Base (SMMAddr) TSEG ...
Region
TSeg Mask (SMMMask)
SMM Entrypoint (CPU0) SMM Base + 8000h
SMM Base (CPUn)
...
SMM Base (CPU0) SMM Base (SMM_BASE)
SMM Core
Physical
Address Space
SMRAM
©2024 IOActive, Inc. All Rights Reserved. 14

## Slide 15

#### Summary of SMRAM Registers

- MSRC001_0111 (SMM_BASE used for SMM base address)

- MSRC001_0112 (SMM TSeg Base Address (SMMAddr))

- MSRC001_0113 (SMM TSeg Mask (SMMMask))

- MSRC001_0015[SmmLock] (HWCR used for locking the config)

_These need to be configured for each core_

©2024 IOActive, Inc. All Rights Reserved.

15

## Slide 16

#### Differences between AMD and Intel MSRs

- On Intel systems there are specific MSRs that are only accessible while the processor is executing at SMM `o` _Example: IA32_SMBASE (SMM base register)_ `o` _Obtaining this value could be considered a leak_

- On AMD all the MSRs that are related to the security of SMM are accessible from ring 0

`o` _Note that when SmmLock bit is set, accesibility does not imply the configuration can be changed even from SMM_

©2024 IOActive, Inc. All Rights Reserved.

16

## Slide 17

## Spotting the bug

©2024 IOActive, Inc. All Rights Reserved.

17

## Slide 18

©2024 IOActive, Inc. All Rights Reserved.

18

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
>
Bits |Description
63:40 |Reserved.
39:17 |TSegMask[39:17]: TSeg address range mask. IF MSRC001_0015[SmmLock] THEN Read-only
ELSE Read-write ENDIF. See MSRC001_ 0112.
16:15 |Reserved.
14:12 |TMTypeDram: TSeg address range memory type. IF MSRC001_0015[SmmLock] THEN Read-
only. ELSE Read-write. ENDIF. Specifies the memory type for SMM accesses to the TSeg range that
are directed to DRAM. See: Table 219 [Valid Values for Memory Type Definition].
11 |Reserved.
10:8 |AMTypeDram: ASeg Range Memory Type. IF MSRC001_0015[SmmLock] THEN Read-only.
ELSE Read-write. ENDIF. Specifies the memory type for SMM accesses to the ASeg range that are
directed to DRAM. See: Table 219 [Valid Values for Memory Type Definition].
7:6 |Reserved.
5 |TMTypeloWc: non-SMM TSeg address range memory type. IF MSRC001_0015[SmmLock]
THEN Read-only. ELSE Read-write. ENDIF. Specifies the attribute of TSeg accesses that are
directed to MMIO space. 0=UC (uncacheable). 1=WC (write combining).
AMTypeloWe: non-SMM ASeg address range memory type. IF MSRC001_0015[SmmLock]
THEN Read-only. ELSE Read-write. ENDIF. Specifies the attribute of ASeg accesses that are
directed to MMIO space. 0=UC (uncacheable). 1=WC (write combining).
TClose: send TSeg address range data accesses to MMIO. Read-write. 1=When in SMM, direct
data accesses in the TSeg address range to MMIO space. See AClose.
AClose: send ASeg address range data accesses to MMIO. Read-write. 1=When in SMM, direct
data accesses in the ASeg address range to MMIO space.
[A, T]Close allows the SMI handler to access the MMIO space located in the same address region as
the [A, T]Seg. When the SMI handler is finished accessing the MMIO space, it must clear the bit.
Failure to do so before resuming from SMM causes the CPU to erroneously read the save state from
MMIO space.
TValid: enable TSeg SMM address range. IF MSRC001_0015[SmmLock] THEN Read-only.
ELSE Read-write. ENDIF. 1=The TSeg address range SMM enabled.
AValid: enable ASeg SMM address range. IF MSRC001_0015[SmmLock] THEN Read-only.
ELSE Read-write. ENDIF. 1=The ASeg address range SMM enabled.
©2024 |OActive, Inc. All Rights Reserved.
» lOActive.
```

## Slide 19

©2024 IOActive, Inc. All Rights Reserved.

19

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
>
Bits
Description
63:40
Reserved.
39:17
TSegMask[39:17|: TSeg address range mask. IF MSRCO01_0015{SmmLock| THEN Read-only
ELSE Read-write ENDIF. See MSRCO001_0112.
16:15
Reserved.
14:12
TMTypeDram: TSeg address range memory type. IF MSRC001_0015{[SmmLock| THEN Read-
only. ELSE Read-write. ENDIF. Specifies the memory type for SMM accesses to the TSeg range that
are directed to DRAM. See: Table 219 [Valid Values for Memory Type Definition].
Reserved.
10:8
AMTypeDram: ASeg Range Memory Type. If MSRC001_0015[SmmLock] THEN Read-only.
ELSE Read-write. ENDIF. Specifies the memory type for SMM accesses to the ASeg range that are
directed to DRAM. See: Table 219 [Valid Values for Memory Type Definition].
7:6
Reserved.
TMTypeloWe: non-SMM TSeg address range memory type. IF MSRCO001_0015[/SmmLock]
THEN Read-only. ELSE Read-write. ENDIF. Specifies the attribute of TSeg accesses that are
directed to MMIO space. 0=UC (uncacheable). 1=WC (write combining).
AMTypeloWe: non-SMM ASeg address range memory type. IF MSRCO0!_0015[SmmLock]
THEN Read-only. ELSE Read-write. ENDIF. Specifies the attribute of ASeg accesses that are
directed to MMIO space. 0=UC (uncacheable). 1=WC (write combining).
TClose: send TSeg address range data accesses to MMIO. Read-write. 1=When in SMM, direct
data accesses in the TSeg address range to MMIO space. See AClose.
AClose: send ASeg address range data accesses to MMIO. Read-write. 1=When in SMM, direct
data accesses in the ASeg address range to MMIO space.
[A, T]Close allows the SMI handler to access the MMIO space located in the same address region as
the [A, T]Seg. When the SMI handler is finished accessing the MMIO space, it must clear the bit.
Failure to do so before resuming from SMM causes the CPU to erroneously read the save state from
MMIO space.
TValid: enable TSeg SMM address range. IF MSRCO01_0015{SmmlLock) THEN Read-only.
ELSE Read-write. ENDIF. 1=The TSeg address range SMM enabled.
AValid: enable ASeg SMM address range. IF MSRCO0! 0015{SmmLock] THEN Read-only.
ELSE Read-write. ENDIF. 1=The ASeg address range SMM enabled.
©2024 |OActive, Inc. All Rights Reserved.
» lOActive.
```

## Slide 20

©2024 IOActive, Inc. All Rights Reserved.

20

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
>
Bits
Description
63:40
Reserved.
39:17
TSegMask[39:17|: TSeg address range mask. IF MSRCO01_0015{SmmLock| THEN Read-only
ELSE Read-write ENDIF. See MSRCO001_0112.
16:15
Reserved.
14:12
TMTypeDram: TSeg address range memory type. IF MSRC001_0015{[SmmLock| THEN Read-
only. ELSE Read-write. ENDIF. Specifies the memory type for SMM accesses to the TSeg range that
are directed to DRAM. See: Table 219 [Valid Values for Memory Type Definition].
Reserved.
10:8
AMTypeDram: ASeg Range Memory Type. If MSRC001_0015[SmmLock] THEN Read-only.
ELSE Read-write. ENDIF. Specifies the memory type for SMM accesses to the ASeg range that are
directed to DRAM. See: Table 219 [Valid Values for Memory Type Definition].
7:6
Reserved.
TMTypeloWe: non-SMM TSeg address range memory type. IF MSRCO001_0015[/SmmLock]
THEN Read-only. ELSE Read-write. ENDIF. Specifies the attribute of TSeg accesses that are
directed to MMIO space. 0=UC (uncacheable). 1=WC (write combining).
AMTypeloWe: non-SMM ASeg address range memory type. IF MSRCO0!_0015[SmmLock]
THEN Read-only. ELSE Read-write. ENDIF. Specifies the attribute of ASeg accesses that are
directed to MMIO space. 0=UC (uncacheable). 1=WC (write combining).
TClose: send TSeg address range data accesses to MMIO. Read-write. 1=When in SMM, direct
data accesses in the TSeg address range to MMIO space. See AClose.
AClose: send ASeg address range data accesses to MMIO. Read-write. 1=When in SMM, direct
data accesses in the ASeg address range to MMIO space.
[A, T]Close allows the SMI handler to access the MMIO space located in the same address region as
the [A, T]Seg. When the SMI handler is finished accessing the MMIO space, it must clear the bit.
Failure to do so before resuming from SMM causes the CPU to erroneously read the save state from
MMIO space.
TValid: enable TSeg SMM address range. IF MSRCO01_0015{SmmlLock) THEN Read-only.
ELSE Read-write. ENDIF. 1=The TSeg address range SMM enabled.
AValid: enable ASeg SMM address range. IF MSRCO0! 0015{SmmLock] THEN Read-only.
ELSE Read-write. ENDIF. 1=The ASeg address range SMM enabled.
©2024 |OActive, Inc. All Rights Reserved.
» lOActive.
```

## Slide 21

#### More explicit in earlier docs

Source:

<u>https://www.amd.com/content/dam/amd/en/documents/archived-techdocs/revision-guides/41322_10h_Rev_Gd.pdf</u>

©2024 IOActive, Inc. All Rights Reserved.

21

## Slide 22

MSR C001_0113 SMM TSeg Mask (SMMMask)

©2024 IOActive, Inc. All Rights Reserved.

22

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
MSR C001 0113 SMM TSeg Mask
(SMMMask)
This register specifies how accesses to the ASeg and TSeg address ranges are controlled as follows:
¢ If [A,T]Valid=1, then:
¢ If in SMM, then:
¢ If [A, T]Close=0, then the accesses are directed to DRAM with memory type as specified in [A,
T]MTypeDram.
¢ If [A, T]Close=1, then instruction accesses are directed to DRAM with memory type as specified in
[A, T]MTypeDram and data accesses are directed at MMIO space and with attributes based on [A,
T]MTypeloWce.
¢ Ifnot in SMM, then the accesses are directed at MMIO space with attributes based on
[A,T]MTypeloWc.
.
Na ©2024 |OActive, Inc. All Rights Reserved. 22 lOActive.
```

## Slide 23

#### X86 goes to Harvard

FFFF_FFFF 4GB
h SPI Flash Device X
FF00_0000
h APIC Device Y
FEE0_0000h
SPI Controller Device Z
Core 0 FEC1_0000h
Normal mode MMIO Space
PCIe ECAM
E000_0000h
MMIO
Data fetch B000_0000
h
TSEG SMRAM
Instruction fetch
AE00_0000
h
Memory
0000_0000
h
Physical Address  DRAM
Space
©2024 IOActive, Inc. All Rights Reserved. 23

©2024 IOActive, Inc. All Rights Reserved.

## Slide 24

#### X86 goes to Harvard

FFFF_FFFF 4GB
h SPI Flash Device X
FF00_0000
h APIC Device Y
FEE0_0000h
SPI Controller Device Z
Core 0 FEC1_0000h
SMM MMIO Space
PCIe ECAM
E000_0000h
MMIO
B000_0000
h
TSEG SMRAM
AE00_0000
h
Memory
TClose OFF
0000_0000
h
Physical Address  DRAM
Space
©2024 IOActive, Inc. All Rights Reserved. 24

©2024 IOActive, Inc. All Rights Reserved.

## Slide 25

#### X86 goes to Harvard

FFFF_FFFF 4GB
h SPI Flash Device X
FF00_0000
h APIC Device Y
FEE0_0000h
SPI Controller Device Z
Core 0 FEC1_0000h
SMM MMIO Space
PCIe ECAM
E000_0000h
MMIO
B000_0000
h
TSEG SMRAM
Instruction fetch
AE00_0000
h
Memory
TClose OFF
0000_0000
h
Physical Address  DRAM
Space
©2024 IOActive, Inc. All Rights Reserved. 25

©2024 IOActive, Inc. All Rights Reserved.

## Slide 26

#### X86 goes to Harvard

FFFF_FFFF 4GB
h SPI Flash Device X
FF00_0000
h APIC Device Y
FEE0_0000h
SPI Controller Device Z
Core 0 FEC1_0000h
SMM MMIO Space
PCIe ECAM
E000_0000h
MMIO
Data fetch B000_0000
h
TSEG SMRAM
Instruction fetch
AE00_0000
h
Memory
TClose OFF
0000_0000
h
Physical Address  DRAM
Space
©2024 IOActive, Inc. All Rights Reserved. 26

©2024 IOActive, Inc. All Rights Reserved.

## Slide 27

#### X86 goes to Harvard

FFFF_FFFF 4GB
h SPI Flash Device X
FF00_0000
h APIC Device Y
FEE0_0000h
SPI Controller Device Z
Core 0 FEC1_0000h
SMM MMIO Space
PCIe ECAM
E000_0000h
MMIO
B000_0000
h
TSEG SMRAM
AE00_0000
h
Memory
TClose ON
0000_0000
h
Physical Address  DRAM
Space
©2024 IOActive, Inc. All Rights Reserved. 27

©2024 IOActive, Inc. All Rights Reserved.

## Slide 28

#### X86 goes to Harvard

FFFF_FFFF 4GB
h SPI Flash Device X
FF00_0000
h APIC Device Y
FEE0_0000h
SPI Controller Device Z
Core 0 FEC1_0000h
SMM MMIO Space
PCIe ECAM
E000_0000h
MMIO
B000_0000
h
TSEG SMRAM
Instruction fetch
AE00_0000
h
Memory
TClose ON
0000_0000
h
Physical Address  DRAM
Space
©2024 IOActive, Inc. All Rights Reserved. 28

©2024 IOActive, Inc. All Rights Reserved.

## Slide 29

#### X86 goes to Harvard

FFFF_FFFF 4GB
h SPI Flash Device X
FF00_0000
h APIC Device Y
FEE0_0000h
SPI Controller Device Z
Core 0 FEC1_0000h
SMM MMIO Space
PCIe ECAM
E000_0000h
MMIO
Data fetch B000_0000
h
TSEG SMRAM
Instruction fetch
AE00_0000
h
Memory
TClose ON
0000_0000
h
Physical Address  DRAM
Space
©2024 IOActive, Inc. All Rights Reserved. 29

©2024 IOActive, Inc. All Rights Reserved.

## Slide 30

#### X86 goes to Harvard

FFFF_FFFF 4GB
h SPI Flash Device X
FF00_0000
Attacker
h APIC Device Y
FEE0_0000h Controlled
SPI Controller Device Z
Core 0 FEC1_0000h
SMM MMIO Space
PCIe ECAM
E000_0000h
MMIO
Data fetch B000_0000
h
TSEG SMRAM
Instruction fetch
AE00_0000
h
Memory
TClose ON
0000_0000
h
Physical Address  DRAM
Space
©2024 IOActive, Inc. All Rights Reserved. 30

©2024 IOActive, Inc. All Rights Reserved.

## Slide 31

#### Triggering the condition

©2024 IOActive, Inc. All Rights Reserved.

31

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Triggering the condition
void test() {
open_platbox_device();
UINT64 tseg_mask = 0;
do_read_msr(AMD_MSR_SMM_TSEG_MASK, &tseg_mask) ;
tseg_mask = tseg_mask | (@b11 << 2);
do_write_msr(AMD_MSR_SMM_TSEG_MASK, tseg_mask) ;
SW_SMI_CALL smi_call = { 0 };
trigger_smi(&smi_call) ;
close_platbox_device();
.
Na ©2024 |OActive, Inc. All Rights Reserved 31 lOActive.
```

## Slide 32

#### Why does this feature exist?

- This allows to re-use the physical address space

- We have yet to see a vendor using this feature

©2024 IOActive, Inc. All Rights Reserved.

32

## Slide 33

#### When did this feature appear?

- First mentioned for AMD 0Fh processor families (2006)

- BIOS and Kernel Developer's Guide for AMD NPT Family 0Fh Processors <u>https://www.amd.com/content/dam/amd/en/documents/a rchived-tech-docs/programmer-references/32559.pdf</u>

- It's been around for 18 years...

©2024 IOActive, Inc. All Rights Reserved.

33

## Slide 34

#### Differences with the "Memory Sinkhole"

- Cristopher Domas presented the Memory Sinkhole attack in 2015 `o` Affected Intel Sandy Bridge and previous generations `o` Remaps the APIC over the TSEG area

   - Causes data fetches to go to MMIO instead of SMRAM

- Key differences:

   - The memory sinkhole only affects the 4K portion where the APIC gets mapped

   - Sinkclose changes the behavior of the entire TSEG region `o` Any device could be overlapped... right?

©2024 IOActive, Inc. All Rights Reserved.

34

## Slide 35

## Brainstorming attack ideas

©2024 IOActive, Inc. All Rights Reserved.

35

## Slide 36

#### Attack idea

- Use a PCIe device with a BAR having register values such that when overlapped with the SMM entry point, we could take control of the execution

- There are multiple integrated devices in modern systems

- We can try re-mapping the PCI Base Address Register (BAR) from one of them to make it overlap with SMRAM

- The registers for the device should become visible for the OS at the TSEG location

©2024 IOActive, Inc. All Rights Reserved.

36

## Slide 37

#### PCI BARs failed

©2024 IOActive, Inc. All Rights Reserved.

37

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
PCI BARs failed
/dev/KernetixDriver® opened successfully: 3
+ SMM region info:
TSEG Base : bf000000
TSEG Size : OOFFFFFF
SMM Base : bfea8000
SMM-Entry : bfeb0000
Ethernet controller BAR2 at:} d0714000
-> remapping BAR2 to overlap TSEG
+ successfully overlaped the ethernet bar over SMM at: bfeb0000
-> view of memory at smm entry point:
at BAR2 (d0714000) :
Restoring BAR and dumping again:
lOActive.
```

## Slide 38

#### PCI BARs failed

Visible device registers

©2024 IOActive, Inc. All Rights Reserved.

38

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
PCI BARs failed
/dev/KernetixDriver® opened successfully: 3
+ SMM region info:
TSEG Base : bf000000
TSEG Size : OOFFFFFF
SMM Base : bfea8000
SMM-Entry : bfeb0000
Ethernet controller BAR2 at:} d0714000
-> remapping BAR2 to overlap TSEG
+ successfully overlaped the ethernet bar over SMM at: bfeb0000
-> view of memory at smm entry point:
-+gR|..
Visible device registers
at BAR2 (d0714000) :
Restoring BAR and dumping again:
Ws . 10 Active.
```

## Slide 39

#### PCI BARs failed

Visible device registers

Remap failed; registers are not available

©2024 IOActive, Inc. All Rights Reserved.

39

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
PCI BARs failed
/dev/KernetixDriver® opened successfully: 3
+ SMM region info:
TSEG Base : bf000000
TSEG Size : OOFFFFFF
SMM Base : bfea8000
SMM-Entry : bfeb0000
Ethernet controller BAR2 at:} d0714000
-> remapping BAR2 to overlap TSEG
+ successfully overlaped the ethernet bar over SMM at: bfeb0000
-> view of memory at smm entry point:
-+gR|..
Visible device registers
-> Memory at BAR2 (d07140QQ):
Restoring BAR and dumping again:
es » 10Active.
```

## Slide 40

#### PCI BARs failed

Visible device registers

Remap failed; registers are not available

The BAR was indeed moved from its original place

©2024 IOActive, Inc. All Rights Reserved.

40

## Slide 41

#### PCI BARs failed

Visible device registers

Remap failed; registers are not available

The BAR was indeed moved from its original place

After restoration

©2024 IOActive, Inc. All Rights Reserved.

41

## Slide 42

#### TOM - Top of Memory

- This register dictates where the MMIO region below 4G starts

- On Intel this register has a lock bit and cannot be modified when set

- There is no such lock in AMD :)

©2024 IOActive, Inc. All Rights Reserved.

42

## Slide 43

#### Moving TOM down

4GB FFFFFFFFh
MMIO
TOM B0000000h
TSEG
TSEG_BASE AE000000h

©2024 IOActive, Inc. All Rights Reserved.

43

## Slide 44

#### Moving TOM down

4GB FFFFFFFFh 4GB FFFFFFFFh
MMIO MMIO
TOM B0000000h
TSEG TSEG
TSEG_BASE AE000000h TSEG_BASE AE000000h
TOM

©2024 IOActive, Inc. All Rights Reserved.

44

## Slide 45

#### Moving TOM down

4GB FFFFFFFFh 4GB FFFFFFFFh
MMIO MMIO
TOM B0000000h
TSEG TSEG
TSEG_BASE AE000000h TSEG_BASE AE000000h
TOM

_This worked in theory but not in practice..._

©2024 IOActive, Inc. All Rights Reserved.

45

## Slide 46

#### Memory routing priorities

©2024 IOActive, Inc. All Rights Reserved.

46

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Memory routing priorities
2.4.6.1.2 Determining The Access Destination for Core Accesses
The access destination, DRAM or MMIO, is based on the highest priority of the following ranges that the
access falls in: 1==Lowest priority.
1. RdDram/WrDram as determined by MSRC001_001A [Top Of Memory (TOP_MEM)] and
MSRC001_001D [Top Of Memory 2 (TOM2)].
The IORRs. (see MSRCO001_00[18,16] and MSRCO01_00[19,17]).
The fixed MTRRs. (see MSR0000_02[6F:68,59:58,50] [Fixed-Size MTRRs])
TSeg & ASeg SMM mechanism. (see MSRC001_0112 and MSRCO01_0113)
MMIO config space, APIC space.
* MMIO APIC space and MMIO config space must not overlap.
¢ RdDram=IO, WrDram=IO.
¢ See 2.4.9.1.2 [APIC Register Space] and 2.7 [Configuration Space].
6. NB address space routing. See 2.8.2.1.1 [DRAM and MMIO Memory Space].
i oe
.
Na ©2024 lOActive, Inc. All Rights Reserved 46 lOActive.
```

## Slide 47

#### Memory routing priorities

©2024 IOActive, Inc. All Rights Reserved.

47

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Memory routing priorities
2.4.6.1.2 Determining The Access Destination for Core Accesses
The access destination, DRAM or MMIO, is based on the highest priority of the following ranges that the
access falls in: 1==Lowest priority.
1. RdDram/WrDram as determined by MSRC001_001A [Top Of Memory (TOP_MEM)] and
MSRC001_001D [Top Of Memory 2 (TOM2)].
The IORRs. (see MSRCO001_00[18,16] and MSRCO01_00[19,17]).
The fixed MTRRs. (see MSR0000_02[6F:68,59:58,50] [Fixed-Size MTRRs])
TSeg & ASeg SMM mechanism. (see MSRC001_0112 and MSRCO01_0113)
MMIO config space, APIC space.
* MMIO APIC space and MMIO config space must not overlap.
¢ RdDram=IO, WrDram=IO.
¢ See 2.4.9.1.2 [APIC Register Space] and 2.7 [Configuration Space].
6. NB address space routing. See 2.8.2.1.1 [DRAM and MMIO Memory Space].
i oe
.
Na ©2024 lOActive, Inc. All Rights Reserved 47 lOActive.
```

## Slide 48

#### Memory routing priorities

©2024 IOActive, Inc. All Rights Reserved.

48

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Memory routing priorities
2.4.6.1.2 Determining The Access Destination for Core Accesses
The access destination, DRAM or MMIO, is based on the highest priority of the following ranges that the
access a in: i. Lanes priority.
MSRCOOL _001D [Top Of Mer
= a (see MSRCO01—
TSeg & ASeg SMM mechanism. (see MSRCOO!_011 12 and MSRCOO1 0113)
MMIO config space, APIC space.
* MMIO APIC space and MMIO config space must not overlap.
¢ RdDram=IO, WrDram=IO.
¢ See 2.4.9.1.2 [APIC Register Space] and 2.7 [Configuration Space].
6. NB address space routing. See 2.8.2.1.1 [DRAM and MMIO Memory Space].
.
Na ©2024 lOActive, Inc. All Rights Reserved 48 lOActive.
```

## Slide 49

#### Memory routing priorities

©2024 IOActive, Inc. All Rights Reserved.

49

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Memory routing priorities
2.4.6.1.2 Determining The Access Destination for Core Accesses
The access destination, DRAM or MMIO, is based on the highest priority of the following ranges that the
access a in: i. Lanes priority.
MSRCOOL _001D [Top Of Mer
= a (see MSRCO01—
2
3:
4. TSeg & ASeg SMM mechanism. (see MSRCO001_011 12 and MSRCOO1_01 13)
5. | MMIO config space, APIC space.
* MMIO APIC space and MMIO config space must not overlap.
¢ RdDram=IO, WrDram=IO.
* See 2.4.9.1.2 [APIC Register Space] and 2.7 [Configuration Space].
6. NB address space routing. See 2.8.2.1.1 [DRAM and MMIO Memory Space].
.
Na ©2024 lOActive, Inc. All Rights Reserved 49 lOActive.
```

## Slide 50

#### Memory routing priorities

?

©2024 IOActive, Inc. All Rights Reserved.

50

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Memory routing priorities
2.4.6.1.2 Determining The Access Destination for Core Accesses
The access destination, DRAM or MMIO, is based on the highest priority of the following ranges that the
access a in: i. Lanes priority.
MSRCOOL _001D [Top Of Mer
= a (see MSRCOO
2
3:
4. TSeg & ASeg SMM mechanism. (see MSRCO001_011 12 and MSRCO001_01 13)
5
MMIO config space, APIC space.
* MMIO APIC space and MMIO config space must not overlap.
¢ RdDram=IO, WrDram=IO.
* See 2.4.9.1.2 [APIC Register Space] and 2.7 [Configuration Space].
6. | NB address space routing. See 2.8.2.1.1 [DRAM and MMIO Memory Space]} ?
.
Na ©2024 lOActive, Inc. All Rights Reserved 50 lOActive.
```

## Slide 51

#### Analysis of the SMM entry point

Real mode (16 bit) Protected mode (32 bit) Long mode (64 bit)

SMM Mode

SMI handlers

©2023 IOActive, Inc. All Rights Reserved.

51

## Slide 52

#### Global Descriptor Table (GDT)

```
jmp 0x8:0x1000
```

Descriptor N
Data Descriptor
Base: 0x00000000
Code Descriptor
Base: 0x00000000
Descriptor 0
Limit Base
(NULL)
GDTR GDT

©2024 IOActive, Inc. All Rights Reserved.

52

## Slide 53

#### Global Descriptor Table (GDT)

jmp 0x8:0x1000
Descriptor N
Data Descriptor
Base: 0x00000000
Code Descriptor
Base: 0x00000000
Descriptor 0
Limit Base
(NULL)
GDTR GDT

©2024 IOActive, Inc. All Rights Reserved.

53

## Slide 54

#### Global Descriptor Table (GDT)

jmp 0x8:0x1000
Descriptor N
Data Descriptor
Base: 0x00000000
Code Descriptor Linear address
Base: 0x00000000
0x1000
Descriptor 0
Limit Base
(NULL)
GDTR GDT

©2024 IOActive, Inc. All Rights Reserved.

54

## Slide 55

#### Analysis of the EDKII SMM entry point

©2024 IOActive, Inc. All Rights Reserved.

55

## Slide 56

#### Analysis of the EDKII SMM entry point

SMM entry point + 0x4D

©2024 IOActive, Inc. All Rights Reserved.

56

## Slide 57

#### Analysis of the EDKII SMM entry point

SMM entry point + 0x4D

©2024 IOActive, Inc. All Rights Reserved.

57

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
>
Analysis of the EDKII SMM entry point
Ts 48
2e: 00
4c: 20
4d: [ GDTR HERE ]
ae
80
fa
ae
1)
of
08
©2024 |OActive, Inc. All Rights Reserved.
mov
mov
dec
mov
mov
mov
lgdtd
mov
mov
mov
lea
mov
mov
and
or
mov
jmp
bx ,@x804d ; @x8000 + @x40 ———>_— SMM entry point + 0x4D
ax,cs:@xfdd8 ; DSC_OFFSET + @xD8
ax
WORD PTR cs: [bx],ax
eax,cs:@xfdd®@ ; DSC_OFFSET + xD
DWORD PTR cs: [bx+0x2],eax
GS? [bx] §
ax, @x8
WORD PTR cs: [bx-®x2] ,ax
edi, 0xaef43000
eax, [edi+0x8053]
DWORD PTR cs: [bx-@x6] ,eax
ebx, cra
ebx, 0x9ffafff3
ebx , 0x23
crd,ebx
x8 : Oxaef4b@53
. lOActive.
```

## Slide 58

#### Analysis of the EDKII SMM entry point

SMM entry point + 0x4D Loads GDTR

©2024 IOActive, Inc. All Rights Reserved.

58

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
>
Analysis of the EDKII SMM entry point
Ts 48
2e: 00
4c: 20
4d: [ GDTR HERE ]
ae
80
fa
ae
1)
of
08
©2024 |OActive, Inc. All Rights Reserved.
mov
mov
dec
mov
mov
mov
lgdtd
mov
mov
mov
lea
mov
mov
and
or
mov
jmp
bx ,@x804d
ax,cs:@xfdd8 ; DSC_OFFSET + @xD8
ax
WORD PTR cs: [bx],ax
eax,cs:@xfdd®@ ; DSC_OFFSET + xD
DWORD PTR cs: [bx+0x2],eax
GS? [bx] §
; @x8000 + @x40 ———>_— SMM entry point + 0x4D
ax, @x8
WORD PTR cs: [bx-®x2] ,ax
edi, 0xaef43000
eax, [edi+0x8053]
DWORD PTR cs: [bx-@x6] ,eax
ebx, cra
ebx, 0x9ffafff3
ebx , 0x23
crd,ebx
x8 : Oxaef4b@53
> Loads GDTR
. lOActive.
```

## Slide 59

#### Analysis of the EDKII SMM entry point

SMM entry point + 0x4D Loads GDTR

Jumps to 32-bit (protected) code

©2024 IOActive, Inc. All Rights Reserved.

59

## Slide 60

#### Analysis of the EDKII SMM entry point

SMM entry point + 0x4D Loads GDTR Jumps to 32-bit (protected) code

_We need to control the BAR of the overlapped device at offset 0x4D_

©2024 IOActive, Inc. All Rights Reserved.

60

## Slide 61

#### Problems with the APIC

- The system becomes unstable when the APIC is moved

- The APIC registers are not useful for taking control at the SMM entry point

©2024 IOActive, Inc. All Rights Reserved.

61

## Slide 62

#### APIC Registers

**Reserved region Writes are discarded**

©2024 IOActive, Inc. All Rights Reserved.

62

## Slide 63

## Introducing the SPI controller

©2024 IOActive, Inc. All Rights Reserved.

63

## Slide 64

#### SPI controller

- Used to read / write / erase the SPI flash

- Key features:

   - The BAR can be relocated over the SMM entry point

   - `o` Portions of the BAR are attacker-controlled

   - Takes precedence over SMRAM when TClose is enabled

©2024 IOActive, Inc. All Rights Reserved.

64

## Slide 65

SMI Handlers
SMM Save State (CPUn)
...
SMM Save State (CPU0)
SMM Entrypoint (CPUn)
...
Data fetch
SMM Entrypoint (CPU0) SPI BAR
Instruction fetch
SMM Base (CPUn)
Core 0
SMM ...
MMIO
SMM Base (CPU0)
SMM Core
SMRAM

©2024 IOActive, Inc. All Rights Reserved.

65

## Slide 66

©2024 IOActive, Inc. All Rights Reserved.

66

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Zz Memory
[Address = 00000000FEC11000 _|
P
i}
dword
32bi
word
16bi
(7 Refresh
Info Text
Hardware
.
Na ©2024 lOActive, Inc. All Rights Reserved 66 lOActive.
```

## Slide 67

#### SPI BAR

- GDTR is loaded from offset 0x4D

- Controllable fields:

   - 0x4C-50: FCH::LPCPCICFG::memoryrange

   - `o` 0x50-54: FCH::LPCPCICFG::rom_protect_0

©2024 IOActive, Inc. All Rights Reserved.

67

## Slide 68

## Debugging setup

©2024 IOActive, Inc. All Rights Reserved.

68

## Slide 69

#### Debugging Setup

- BAR buffer

   - PCI Squirrel with PCILeech firmware

   - `o` Used for persistent memory across boot cycles

- SMM backdoor

   - Used for modifying code in SMM on-demand

©2024 IOActive, Inc. All Rights Reserved.

69

## Slide 70

PCIe Squirrel
Power supply
M2 to PCI 4x
adapter

©2024 IOActive, Inc. All Rights Reserved.

70

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
PCle Squirrel
Power supply
adapter
Bas"
.
Ng ©2024 lOActive, Inc. All Rights Reserved 70 lOActive.
```

## Slide 71

## Exploitation

©2024 IOActive, Inc. All Rights Reserved.

71

## Slide 72

### **Attempt #1**

©2024 IOActive, Inc. All Rights Reserved.

72

## Slide 73

TSEG
Data fetch 1. Remap
SMM Entrypoint
Instruction fetch
Core 0
SMM
SPI BAR
DRAM MMIO

73

©2024 IOActive, Inc. All Rights Reserved.

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
mov bx ,@x804d ; @x8000 + @x4D
mov ax,cs:@xfdd8 ; DSC_OFFSET + @xD8
dec ax
mov WORD PTR cs: [bx],ax
mov eax,cs:@xfdd®@ ; DSC_OFFSET + ®xDd
mov DWORD PTR cs: [bx+0x2],eax
lgdtd cs: [bx];
mov ax ,@x8
mov WORD PTR cs: [bx-@x2] ,ax
mov edi, @xaef43000
lea eax, [edi+0x8053]
TSEG
mov DWORD PTR cs: [bx-@x6] ,eax
LULL mov ebx, cra
_ = and ebx , Ox9f faffF3
= _ Data fetch 1. Remap or ebx , 0x23
7 > SMM Entrypoint mov cx, ebx
a = Instruction fetch jmp 0x8 : Oxaef4b053
TTTTTT
Core 0
SMM
SPI BAR
DRAM MMIO .
lOActive.
~
o
Na ©2024 |OActive, Inc. All Rights Reserved.
```

## Slide 74

TSEG
Data fetch 1. Remap
SMM Entrypoint
Instruction fetch
Core 0
SMM
SPI BAR 2. Tweak
DRAM MMIO
©2024 IOActive, Inc. All Rights Reserved. 74

©2024 IOActive, Inc. All Rights Reserved.

## Slide 75

TSEG
Data fetch 1. Remap
SMM Entrypoint
Instruction fetch
Core 0
SMM
Payload SPI BAR 2. Tweak
3. Map +
tweak
Fake GDT
DRAM MMIO
©2024 IOActive, Inc. All Rights Reserved. 75

©2024 IOActive, Inc. All Rights Reserved.

## Slide 76

TSEG
Data fetch 1. Remap
SMM Entrypoint
Instruction fetch
Core 0
SMM
Payload SPI BAR 2. Tweak
3. Map +
tweak
Fake GDT
DRAM MMIO
©2024 IOActive, Inc. All Rights Reserved. 76

©2024 IOActive, Inc. All Rights Reserved.

## Slide 77

TSEG
Data fetch 1. Remap
SMM Entrypoint
Instruction fetch
Core 0
SMM
Payload SPI BAR 2. Tweak
3. Map +
Size: 0x100
tweak
Address: 0x00000000 Fake GDT
GDTR
DRAM MMIO
©2024 IOActive, Inc. All Rights Reserved. 77

©2024 IOActive, Inc. All Rights Reserved.

## Slide 78

TSEG
Data fetch 1. Remap
SMM Entrypoint
Instruction fetch
Core 0
SMM
Payload SPI BAR 2. Tweak
3. Map +
Size: 0x100
tweak
Address: 0x00000000 Fake GDT
GDTR
DRAM MMIO
©2024 IOActive, Inc. All Rights Reserved. 78

©2024 IOActive, Inc. All Rights Reserved.

## Slide 79

TSEG
Data fetch 1. Remap
SMM Entrypoint
Instruction fetch
Core 0
SMM
Payload SPI BAR 2. Tweak
3. Map +
Size: 0x100
tweak
Address: 0x00000000 Fake GDT
GDTR
DRAM MMIO
©2024 IOActive, Inc. All Rights Reserved. 79

©2024 IOActive, Inc. All Rights Reserved.

## Slide 80

#### GDT far jmp wrap-around

jmp 0x8:0xaef4b053
Descriptor N
Descriptor 2
Descriptor 1 Linear address
Base: 0x00000000 0xaef4b053
Limit Base Descriptor 0
GDTR GDT

©2024 IOActive, Inc. All Rights Reserved.

80

## Slide 81

#### GDT far jmp wrap-around

jmp 0x8:0xaef4b053
Descriptor N
Descriptor 2
Descriptor 1 Linear address
Base: 0x510b4fad 0x00000000
Limit Base Descriptor 0
GDTR GDT

©2024 IOActive, Inc. All Rights Reserved.

81

## Slide 82

It worked, but the system crashed… why?

©2024 IOActive, Inc. All Rights Reserved.

82

## Slide 83

#### The SMM save state

- The SMM save state is automatically saved upon entering SMM and restored when leaving it `o` With TClose enabled these writes are dropped `o` The SMM save state from the last SMI is still there

- Solution: Trigger SMI twice

   - Once without TClose to prime SMM save state

   - `o` Once with TClose to trigger bug

- Does not require overwriting SMM save state values

©2024 IOActive, Inc. All Rights Reserved.

83

## Slide 84

### **Attempt #2**

©2024 IOActive, Inc. All Rights Reserved.

84

## Slide 85

The system crashed again... why?

©2024 IOActive, Inc. All Rights Reserved.

85

## Slide 86

#### Enabling TClose

©2024 IOActive, Inc. All Rights Reserved.

86

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Enabling TClose
a
HB Access Specific
RE] Refresh
Usep |
MTAR User
Register Name Address CPUI cPU2 CPU3 cPU4 CPUS CPUG
MTRR_DEF_TYPE Ox2FF ooo0000000000C00 ooos000000000C00 ooo0000000000C00 ‘ooo0000000000C00 ooo00000000000C00 ‘cooo00R000000C00
SMM_BASE OxC0010111 QOOOCOOOCEF38000  OO000000CEF34000  ON000000CEF3C000  O0000000CEF3E000
QOO00000CEF4O000 + GO000000CEF 42000
OOOOFFFFFFOO6603 © OOOOFFFFFFOO6603
SMM_MASK 0xC0010113 OOOOFFFFFFOO6603  OOOOFFFFFFOO6603  OO0OFFFFFFOO6603  OOOOFFFFFFOO6603
Bl Edit CPU1 MSR 0xC0010113
x
00 00 FF FF OD Toall CPUs
31 30 29 28 27 26 25 24/23 221212019 18 17 16 15 14 13 1211 10 9 8176 5 4392 710 5
111713111 %1#100000000080170031C000 0001708828741 ei
FF 00 66 OF Cancel
©2024 |OActive, Inc. All Rights Reserved.
» lOActive.
```

## Slide 87

#### Bingo...

©2024 IOActive, Inc. All Rights Reserved.

87

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Bingo...
A RW- Read & Write Utility v1.7 - [CPU MSR Registers] = Oo x
Hl Access Specific Window Help -8x
EEE? es pen pepe pew _ JE?
MTRR User
MTRR_DEF_TYPE — Ox2FF odood0o00000c09 — oo0000000000C00 —o0B000000000C00 — OOND0000000C0N — doDDODDON0000C00 —_od0DD00000000C00
SMM_BASE oxconi0111 ONOONHOOCEESE0N0 _ONOONOONCEESANNN — OOOOONDOCEFSCO00 © OOONDONOCEFSEDN0 — dODDONDOCEF4O000 — od0DD0DNCEF4z000
SMM_MASK oxcoo1o113 | (NGGGGFFFFFFOGSG0R |) OO00FFFFFFOGEeOF | QOOOFFFFFFOO6E03 © QOOOFFFFFFODSE03 © OD0OFFFFFFO08603 © OOD0FFFFFFOO6603
.
©2024 lOActive, Inc. All Rights Reserved. 87 lOActive.
```

## Slide 88

#### Symmetric Multi-Threading

- Physical cores are split into two logical cores (threads)

- Some resources are shared between logical cores `o` SMM base MSR is separate but `o` TSEG mask MSR is not

- Is it an issue if only one core goes into SMM at a time?

©2023 IOActive, Inc. All Rights Reserved.

88

## Slide 89

#### SMIs explained

Normal mode Normal mode Normal mode Normal mode `xor eax, eax xor eax, eax xor eax, eax xor eax, eax xor eax, eax xor eax, eax xor eax, eax xor eax, eax`

©2024 IOActive, Inc. All Rights Reserved.

89

## Slide 90

#### SMIs explained

Normal mode Normal mode Normal mode Normal mode `xor eax, eax xor eax, eax xor eax, eax xor eax, eax xor eax, eax xor eax, eax xor eax, eax xor eax, eax smi`

©2024 IOActive, Inc. All Rights Reserved.

90

## Slide 91

#### SMIs explained

Normal mode Normal mode Normal mode Normal mode `xor eax, eax xor eax, eax xor eax, eax xor eax, eax xor eax, eax xor eax, eax xor eax, eax xor eax, eax smi`

©2024 IOActive, Inc. All Rights Reserved.

91

## Slide 92

#### SMIs explained

SMM mode `xor eax, eax xor eax, eax smi`

SMM mode `xor eax, eax xor eax, eax`

SMM mode `xor eax, eax xor eax, eax`

SMM mode `xor eax, eax xor eax, eax`

```
mov bs, 0x804dmov bs, 0x804dmov bs, 0x804dmov bs, 0x804d
mov ax, cs:0xfdd8mov ax, cs:0xfdd8mov ax, cs:0xfdd8mov ax, cs:0xfdd8
............
```

©2024 IOActive, Inc. All Rights Reserved.

92

## Slide 93

#### SMIs explained

- We assumed that SMIs are local, but they are global

- Initially we thought that:

   - we could control exactly which core enters into SMM first

   - each core would later reach the rendezvous routine and

   - send Inter-Processor-Interrupts (IPI) to bring the rest of the cores into SMM before continuing

- We were wrong: The I/O Hub sends the SMI to all cores at once

©2024 IOActive, Inc. All Rights Reserved.

93

## Slide 94

#### Problem summarized

- SMIs make all cores go to SMM at the same time

- TClose is enabled on two logical cores at a time `o` They will read 0xFFs since no device is mapped there `o` Writes to SMM save state will be dropped

- This will make core 1 triple-fault and crash the system

©2024 IOActive, Inc. All Rights Reserved.

94

## Slide 95

#### Tackling the problem

- We had:

   - Control of data fetches on core 0

   - `o` No control of data fetches on core 1

- We tried many things to solve the problem: `o` Finding another device to overlap with the SMM entry point `o` Disabling Simultaneous Multi-Threading (SMT) `o` Sending an INIT IPI / executing SKINIT to ignore SMIs `o` Sending an SMI IPI to trigger an SMI on individual cores

©2024 IOActive, Inc. All Rights Reserved.

95

## Slide 96

#### Running out of options

- Taking a step back: `o` Our `lgdt` is the issue

   - What happens if the GDTR is loaded all with `FFs` ?

- Let's look into that...

©2023 IOActive, Inc. All Rights Reserved.

96

## Slide 97

#### GDTR wrap-around

jmp 0x8:0xaef4b053
Descriptor N
0xAED030C0
Descriptor 2
Descriptor 1 Linear address
Base: 0x00000000
0xaef4b053
Base
Limit Descriptor 0
0xAED030B8
GDTR GDT

97

©2024 IOActive, Inc. All Rights Reserved.

## Slide 98

#### GDTR wrap-around

jmp 0x8:0xaef4b053
Descriptor N
0x00000007
Descriptor 2
Descriptor 1 Linear address
Limit Base
Descriptor 0
0xFFFF 0xFFFFFFFF
GDTR GDT

98

©2024 IOActive, Inc. All Rights Reserved.

## Slide 99

#### Wrap-arounds in x86

- The are two instances of wrap-arounds:

   - The addition between GDT descriptor base and `far jmp` offset can overflow

   - The addition between the GDTR base and `far jmp` segment selector can overflow

- We can use the same fake GDT for core 0 and 1

- Added bonus: No need for the SPI BAR remapping

©2024 IOActive, Inc. All Rights Reserved.

99

## Slide 100

#### SMM save state (again)

- For core 0 we use the same technique as before

- For core 1 we:

   - Need to bring core 1 into a known / controlled state

   - `o` We use kernel synchronization APIs to achieve that

      - Deferred Procedure Calls (DPC) on Windows

      - Symmetric Multi-Processing (SMP) on Linux

©2024 IOActive, Inc. All Rights Reserved.

10 0

## Slide 101

#### **Attempt #3**

©2024 IOActive, Inc. All Rights Reserved.

10 1

## Slide 102

TSEG
0xFF
SMM Entrypoint 1
Core 1 0xFF
SMM Entrypoint 0
SMM
Core 0
SMM

DRAM

©2024 IOActive, Inc. All Rights Reserved.

10 2

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
mov bx ,@x804d ; @x8000 + @x4D
mov ax,cs:@xfdd8 ; DSC_OFFSET + @xD8
dec ax
mov WORD PTR cs: [bx],ax
mov eax,cs:@xfdd®@ ; DSC_OFFSET + ®xDd
mov DWORD PTR cs: [bx+0x2],eax
lgdtd cs: [bx];
mov ax ,@x8
mov WORD PTR cs: [bx-@x2] ,ax
mov edi, @xaef43000
lea eax, [edi+0x8053]
7 Lijit _ TSEG
= = mov DWORD PTR cs: [bx-@x6] ,eax
a = mov ebx,cr®
“TITTTT >| SMM Entrypoint 1 OFF = es
Littit ‘
_ . > mov cr@,ebx
ies = = > SMM Entrypoint 0 OXF jmp —- @x8: @xaef4b053
Core 0
SMM
DRAM
.
Na ©2024 lOActive, Inc. All Rights Reserved 10 lOActive.
```

## Slide 103

TSEG
0xFF
SMM Entrypoint 1
Core 1 0xFF
SMM Entrypoint 0
SMM
Core 0
Payload 1
SMM
Payload 0
1. Map + tweak
Fake GDT
(1st byte truncated)
DRAM

©2024 IOActive, Inc. All Rights Reserved.

10 3

## Slide 104

TSEG
0xFF
SMM Entrypoint 1
Core 1 0xFF
SMM Entrypoint 0
SMM
Core 0
Payload 1
SMM
Payload 0
1. Map + tweak
Fake GDT
(1st byte truncated)
DRAM

©2024 IOActive, Inc. All Rights Reserved.

10 4

## Slide 105

GDTR
Size: 0xFFFF
Address: 0xFFFFFFFF
TSEG
0xFF
SMM Entrypoint 1
Core 1 0xFF
SMM Entrypoint 0
SMM
Core 0
Payload 1
SMM
Payload 0
1. Map + tweak
Fake GDT
(1st byte truncated)
DRAM
©2024 IOActive, Inc. All Rights Reserved. 10
5

## Slide 106

GDTR
Size: 0xFFFF
Address: 0xFFFFFFFF
TSEG
0xFF
SMM Entrypoint 1
Core 1 0xFF
SMM Entrypoint 0
SMM
Core 0
Payload 1
SMM
Payload 0
1. Map + tweak
Fake GDT
(1st byte truncated)
DRAM
©2024 IOActive, Inc. All Rights Reserved. 10
6

## Slide 107

GDTR
Size: 0xFFFF
Address: 0xFFFFFFFF
TSEG
0xFF
SMM Entrypoint 1
Core 1 0xFF
SMM Entrypoint 0
SMM
Core 0
Payload 1
SMM
Payload 0
1. Map + tweak
Fake GDT
(1st byte truncated)
DRAM
©2024 IOActive, Inc. All Rights Reserved. 10
7

## Slide 108

#### And it worked!

©2024 IOActive, Inc. All Rights Reserved.

10 8

## Slide 109

#### Extra steps

- We can execute code in SMM but in protected mode

- Our payload performs the following steps: `o` Reload the GDT to avoid IP misalignments

   - Setup long mode (including page tables)

   - Install an SMI handlers to avoid re-exploiting the issue

©2023 IOActive, Inc. All Rights Reserved.

10 9

## Slide 110

# DEMO

©2024 IOActive, Inc. All Rights Reserved.

11 0

## Slide 111

#### Next attack paths

- Next steps depend on the platform configuration

- The firmware is responsable for: `o` Restricting access to the SPI flash (e.g. via ROM Armor) `o` Verifying the firmware chain-of-trust (via Platform Secure Boot)

- If everything is enabled, we can at least break secure boot

- If not, there is potential for firmware implants

©2024 IOActive, Inc. All Rights Reserved.

11 1

## Slide 112

Ring 3 Apps
FW FW
Ring 0 OS Loader OS
(SEC+PEI) (DXE)
Load and
verify FW
Read / write SPI FW
Ring -2
(SMM)
AMD
Security
Processor
FW CFG HDD
Read / write SPI
©2024 IOActive, Inc. All Rights Reserved. 11
2

## Slide 113

Ring 3 Apps
FW FW
Ring 0 OS Loader OS
(SEC+PEI) (DXE)
Load
without
verification Read / write SPI FW
Ring -2
(SMM)
AMD
Security
Processor
FW CFG HDD
Read / write SPI
©2024 IOActive, Inc. All Rights Reserved. 11
3

## Slide 114

Ring 3 Apps
FW FW
Ring 0 OS Loader OS
(SEC+PEI) (DXE)
Load and
verify FW
FW
Ring -2
(SMM)
AMD
Security  Read / write SPI
Processor
FW CFG HDD
©2024 IOActive, Inc. All Rights Reserved. 11
4

## Slide 115

Ring 3 Apps
FW FW
Ring 0 OS Loader OS
(SEC+PEI) (DXE)
Load
without
verification FW
Ring -2
(SMM)
AMD
Security  Read / write SPI
Processor
FW CFG HDD
©2024 IOActive, Inc. All Rights Reserved. 11
5

## Slide 116

#### Platform security (overview from 2023)

|**Vendor**|**Model**|**PSB State**|**ROM Armor State**|
|---|---|---|---|
|Acer|Swift 3 SF314-42|Not configured|Not configured|
|Acer|TravelMate P414-41|Not configured|Configured|
|ASUS|Strix G513QR|Not configured|Not configured|
|Lenovo|Thinkpad P16s|Configured*|Not configured|
|Lenovo|IdeaPad 1|Not configured|Not configured|
|Lenovo|Thinkpad T495s|Not configured|Not configured|
|Huawei|Matebook D16|Not configured|Not configured|
|HP|15s|Not configured|Not configured|
|Microsoft|Surface 4|Configured|Unknown|
|MSI|Bravo 15|Not configured|Not configured|

©2024 IOActive, Inc. All Rights Reserved.

11 6

## Slide 117

#### Platform security continued

• We took a look ROM Armor and Platform Secure Boot before

• See our "Back to the Future with Platform Security" from Hexacon 2023 presentation

##### <u>https</u>

<u>://www.youtube.com/watch?v=xSp38lFQeRE&ab_channel</u> =Hexacon

©2023 IOActive, Inc. All Rights Reserved.

11 7

## Slide 118

## Outro

©2024 IOActive, Inc. All Rights Reserved.

11 8

## Slide 119

#### Affected systems

- Pretty much all of them `o` Ryzen series `o` Ryzen Threadripper series

   - EPYC series

- Total number of affected chips: 100s of millions

• AMD advisory AMD-SB-7014 published at <u>https://www.amd.com/en/resources/product-security/bulletin/amd</u> -sb-7014.html ©2023 ~~IOActive, Inc. All Rights Reserved.~~ 11

11 9

## Slide 120

#### Mitigations

- AMD:

   - A microcode update is available

   - Con: Might not cover all affected systems due to product EOL

- OEMs:

   - Modify SMM entry point code to detect if TClose bit is enabled and abort execution

   - `o` Can be done at the reference code level

   - Con: Specific to one OEM or even specific systems

- Users:

   - A hypervisor could be used to trap accesses on the TSEG mask MSR

©2023 IOActive, Inc. All Rights Reserved.

12 0

## Slide 121

#### Timeline

Vulnerability Mitigations will be Hexacon reported to AMD developed (Today) PSIRT (11<sup>th</sup> Dec 2023) (30<sup>th</sup> Oct 2023) Assigned AMD publishes CVE-2023-31315 advisory SB-7014 (30<sup>th</sup> Nov 2023) (9<sup>th</sup> Aug 2024)

AMD publishes advisory SB-7014 (9<sup>th</sup> Aug 2024)

©2023 IOActive, Inc. All Rights Reserved.

12 1

## Slide 122

#### Conclusions

- The vulnerability has been around for nearly two decades

- The complexity of modern architectures plays in favor of attackers

- The flexibility of segmentation played a crucial role for exploitation

- Exploitation requires in-depth understanding of the architecture

_Exploit code will be released mid November_

_Stay tuned!_

©2024 IOActive, Inc. All Rights Reserved.

12 2

## Slide 123

## Questions?

©2024 IOActive, Inc. All Rights Reserved.

12 3
