---
title: "The Bugs in Your Bootloaders Embedded Device Secure Boot Fails and How to Fix Them"
speakers: ["Henrik Ferdinand Nölscher"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2024"
edition: "Europe"
year: 2024
source_pdf: "BlackHat_Europe_2024_slides/Henrik Ferdinand Nölscher_The Bugs in Your Bootloaders Embedded Device Secure Boot Fails and How to Fix Them.pdf"
pages: 54
sha256: "e52a6584c069e90b9f9a9cfd967179facfb4543d5cb3ceaf21447021a2724d32"
text_chars: 14787
ocr_pages: 3
has_ocr: true
redacted_secrets: 0
ocr_confidence: 84.7
ocr_unreliable_blocks: 0
vision_verified_blocks: 2
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:57:26Z"
---
# The Bugs in Your Bootloaders Embedded Device Secure Boot Fails and How to Fix Them

**Speakers:** Henrik Ferdinand Nölscher  
**Conference:** Black Hat Europe 2024  
**Source:** `BlackHat_Europe_2024_slides/Henrik Ferdinand Nölscher_The Bugs in Your Bootloaders Embedded Device Secure Boot Fails and How to Fix Them.pdf` (54 pages)


## Slide 1

The Bugs in Your Bootloaders: Embedded Device Secure Boot Fails and How to Fix Them

Henrik Ferdinand Nölscher @s1ckcc Product Security Engineering (PSE), Google Cloud Blackhat Europe 2024

1

## Slide 2

Hi! I’m Ferdi. I’m part of Google Cloud - Product Security Engineering We study how low-level attacks can compromise our hardware and firmware

2

## Slide 3

We study how low-level attacks can compromise our hardware and firmware **Our approach:** Perform hardware and firmware penetration tests. Find exploitable vulnerabilities. Report vulnerabilities, influence vendors and standards, protect our infrastructure. Start with the lowest layers: Hardware, Firmware, Bootloaders

3

## Slide 4

We study how low-level attacks can compromise our hardware and firmware **Our approach:** Perform hardware and firmware penetration tests. Find exploitable vulnerabilities. Report vulnerabilities, influence vendors and standards, protect our infrastructure. Start with the lowest layers: Hardware, Firmware, Bootloaders

4

## Slide 5

## **Our approach:** Find exploitable vulnerabilities.

Before Regular Reuse or Deployment Operations Decommission **Supply Chain Insider Threat OS-to-Firmware Escape Device Reuse** Attackers have When deployed, attackers Attackers gain privilege Attackers try to time-limited access to gain time-limited physical on the device remotely compromise past or device before it arrives at access on the device and and infect the firmware future users its destination perform attacks

5

## Slide 6

## **Our approach:** Find exploitable vulnerabilities.

Before Regular Deployment Operations **Supply Chain Insider Threat OS-to-Firmware Escape** Attackers have When deployed, attackers Attackers gain privilege time-limited access to gain time-limited physical on the device remotely device before it arrives at access on the device and and infect the firmware its destination perform attacks

Reuse or Decommission

**Device Reuse** Attackers try to compromise past or future users

6

## Slide 7

## **Our approach:** Find exploitable vulnerabilities.

Before Regular Reuse or Deployment Operations Decommission **Supply Chain Insider Threat OS-to-Firmware Escape Device Reuse** Attackers have When deployed, attackers Attackers gain privilege Attackers try to time-limited access to gain time-limited physical on the device remotely compromise past or device before it arrives at access on the device and and infect the firmware future users its destination perform attacks

7

## Slide 8

We study how low-level attacks can compromise our hardware and firmware **Our approach:** Perform hardware and firmware penetration tests. Find exploitable vulnerabilities. Report vulnerabilities, influence vendors and standards, protect our infrastructure. Start with the lowest layers: Hardware, Firmware, Bootloaders

8

## Slide 9

We study how low-level attacks can compromise our hardware and firmware **Our approach:** Perform hardware and firmware penetration tests. Find exploitable vulnerabilities. Report vulnerabilities, influence vendors and standards, protect our infrastructure. Start with the lowest layers: Hardware, Firmware, Bootloaders

9

## Slide 10

We study how low-level attacks can compromise our hardware and firmware. All 15+ reviewed device types that use open source bootloaders were affected by bootloader vulnerabilities.

10

## Slide 11

Real-World Bootloader Vulnerabilities: Cisco

11

## Slide 12

# The Device

Affected devices: Cisco Nexus N9K Series

12

## Slide 13

13

## Slide 14

14

## Slide 15

15


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 87/100 on the text kept, 75/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
[Background: faded, duplicated screenshot of a symbol/module tree (columns "File" / "SMM module") — mostly illegible under the overlay; visible fragments include TpmClearOnRollbackSmm, AcpiModeEnable, Grub, PxePkg, Shell, SmallLogo]

[Ghidra decompiler panel]
********************************************
*                                    FUNCTION *
********************************************
undefined __fastcall _start(undefined8 param_1, int para...
    undefined      AL:1        <RETURN>
    undefined8     XMM0_Qa:8   param_1
    int            XMM1_Da:4   param_2
    int            XMM2_Da:4   param_3
    undefined4     XMM3_Da:4   param_4
entry
                                                  XREF[2]:   Ent...

[Ghidra string cross-reference panel]
00066177 00                                            ??        00h
                              s__Grub_Source_Code_Version_%s_00066178   XREF[1]:
00066178 0a 09 09              ds        "\n\t\tGrub Source Code Version %s\n"
   47 72 75
   62 20 53 ...

[Disassembly, continued below]
0000a237 52                PUSH   RDX
0000a238 e8 b3 6f          CALL   _relocate
   05 00
0000a23d 5f                POP    RDI
0000a23e 5e                POP    RSI
0000a23f e8 a6 fe          CALL   efi_main
   ff ff
0000a244 48 83 c4 08       ADD    RSP,0x8
.exit
0000a248 c3                RET
```

## Slide 16

# cisco-grub workflow

Identify
Identify OS  Verify  Prepare
Bootable  Execute!
Image Signature OS image
Device

16

## Slide 17

# cisco-grub workflow

Identify
Identify OS  Verify  Prepare
Bootable  Execute!
Image Signature OS image
Device

#### Requires file system interaction

17

## Slide 18

cisco-grub workflow
Identify
Identify OS  Verify  Prepare
Bootable  Execute!
Image Signature OS image
Device
for each storage device:
for each file system $fs:
if $fs->mount():$fs->mount()::
try_boot($fs)

# cisco-grub workflow

for each storage device: for each file system $fs: if $fs->mount():$fs->mount():: try_boot($fs)

18

## Slide 19

cisco-grub workflow
Identify
Identify OS  Verify  Prepare
Bootable  Execute!
Image Signature OS image
Device
for each storage device: Idea: find bugs in file
for each file system $fs:
system backends!
if $fs->mount():
try_boot($fs)
19

## Slide 20

cisco-grub workflow
Identify
Identify OS  Verify  Prepare
Bootable  Execute!
Image Signature OS image
Device
function xfs_dir():
char linkbuf[superblock->bsize];
for each storage device:
di_size = read(...);
for each file system $fs:
if di_size < (superblock->bsize-1):
if $fs->mount():
memcpy(linkbuf,...,di_size);
try_boot($fs)
Classic buffer overflow!
20

## Slide 21

# Exploiting cisco-grub

**USB DRIVE ATTACK**

1. Craft a malicious XFS partition

2. Write it to a USB drive

3. Plug into device 4. Reboot

### **OS-TO-FIRMWARE ATTACK**

1. Remotely: obtain admin privileges

2. Get a shell (this is a feature) 3. Write ma licious XFS partition to disk

4. Reboot

21

## Slide 22

# Exploiting cisco-grub

### **USB DRIVE ATTACK**

### **OS-TO-FIRMWARE ATTACK**

1. Craft a malicious XFS partition

2. Write it to a USB drive

3. Plug into device 4. Reboot

1. Remotely: obtain admin privileges

2. Get a shell (this is a feature) 3. Write ma licious XFS partition to disk

4. Reboot

5. Wait for cisco-grub to open a well-known file

6. Exploit buffer overflow, bypass signature checks

22

## Slide 23

23

Exploit in action


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 80/100 on the text kept, 64/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
grub > root (hd1,0)
  Filesystem type is xfs, partition type 0x83

grub > cat /asdf/asdfsdf
-> pwnd by OTS-HS <-
!!!! X64 Exception Type - 06(#UD - Invalid Opcode)  CPU Apic ID - 00000000 !!!!
RIP  - 000000007FBFBB12, CS  - 0000000000000038, RFLAGS - 0000000000010202
RAX  - 000000000000BD00, RCX - 00000000BF0351E0, RDX - 0000000000000015
RBX  - 7FFFFFFFFFFFFFFF, RSP - 000000007FBFBB38, RBP - 000000007FBFBBA0
RSI  - 00000000BE78E150, RDI - 00000000BE78B043
R8   - 0000000000000000, R9  - 000000007FBFB87F, R10 - 0000000000000244
R11  - 0000000000000010, R12 - 00000000BEA37F3C, R13 - 0000000000000000
R14  - 0000000000000000, R15 - 00000000BDBBF018
DS   - 0000000000000030, ES  - 0000000000000030, FS  - 0000000000000030
GS   - 0000000000000030, SS  - 0000000000000030
CR0  - 0000000080010033, CR2 - 0000000000000000, CR3 - 00000000BF801000
CR4  - 0000000000000668, CR8 - 0000000000000000
DR0  - 0000000000000000, DR1 - 0000000000000000, DR2 - 0000000000000000
DR3  - 0000000000000000, DR6 - 00000000FFFF0FF0, DR7 - 0000000000000400
GDTR - 00000000BF5DC000 0000000000000047, LDTR - 0000000000000000
IDTR - 00000000BF059018 0000000000000FFF,   TR - 0000000000000000
FXSAVE_STATE - 000000007FBFB790
!!!! Find image based on IP(0x7FBFBB12) (No PDB)  (ImageBase=0000000000E26B54, EntryPoint=0000000000E2BBDF) !!!!

Exploit in action
```

## Slide 24

# Exploiting cisco-grub

Code execution in bootloader allows signature verification bypass. If exploited correctly: undetectable, unrecoverable compromise

XFS vulnerability was fixed in NX-OS 10.4.2 CVE 2023-4949 Vulnerable XFS code was reused in Xen tools and Coreboot Filo! CVE-2023-34325

24

## Slide 25

Real World Bootloader Vulnerabilities: Dell RootBlock

25

## Slide 26

# What is Dell iDRAC?

Server
Dell’s BMC is named iDRAC.
Network Its current version (iDRAC9)
is used in millions of
devices, such as PowerEdge
servers.
Host
BMC
Manages
26

## Slide 27

# What is Dell iDRAC?

Server
Dell’s BMC is named iDRAC.
Network Its current version (iDRAC9)
is used in millions of
devices, such as PowerEdge
servers.
Host
BMC
iDRAC uses an open source
first-stage bootloader
called BootBlock, which was
Manages
found vulnerable
27

## Slide 28

}

# iDRAC First Stage Bootloader: BootBlock

function CheckImageCopyAndJump { header_t image_header; memcpy(&image_header, spi_flash+..., sizeof(image_header); Attacker controls destination address if(image_header->size > MAX_IMAGE_SZ || …) bail();

memcpy( **image_header->dst** , spi_flash, image_header->size); if(! check_signature(image_header->dst, &image_header)) bail(); // signature check fail

execute_uboot_image(); Signature is checked AFTER copying the u-boot image

28

## Slide 29

DRAM
0xFFFFFFFF
memcpy
CheckImageCopyAndJump:
BootBlock
BootBlock
u-boot Slot 1
u-boot Slot 1
Payload
Payload
0xFF5E0000
SRAM
BMC SoC 29
SPI Flash
1. Read header

## Slide 30

DRAM
0xFFFFFFFF
memcpy
CheckImageCopyAndJump:
…
memcpy() BootBlock
… BootBlock
u-boot Slot 1
Payload u-boot Slot 1
Payload
Payload
0xFF5E0000
SRAM
BMC SoC 30
SPI Flash
2. Overwrite
BootBlock
1. Read header

## Slide 31

DRAM
0xFFFFFFFF
memcpy
CheckImageCopyAndJump:
…
memcpy() BootBlock
… BootBlock
u-boot Slot 1
Payload u-boot Slot 1
Payload
Payload
0xFF5E0000
SRAM
BMC SoC 31
SPI Flash
2. Overwrite
BootBlock
3. Return from
memcpy
1. Read header

## Slide 32

# Exploiting RootBlock

32

## Slide 33

# Exploiting RootBlock

33


> Recovered by OCR — confidence 87/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Exploiting RootBlock
U-Boot 2021.04 (Feb 23 2024 - 12:30:26 +0000) -> pwnd by OTS-HS
CPU: NPCM750 Al @ Model:
DRAM: 464 MiB
RNG: NPCM RNG module bind OK
OTP: NPCM OTP module bind OK
$: NPCM AES module bind OK
Nuvoton npom750 Development Board (Device Tree)
SHA: NPCM SHA module bind OK ()
MMC: sdhcioefos42000: 0
Loading Environment from SPIFlash... SF: Detected w25q32jv with page size 2
56 Bytes, erase size 4 Kis, total 4 MiB
*** Warning - bad CRC, using default environment
In: serial@1000
Out: serial#@1000
Err: serial#1000
Net: No ethernet found.
Security is enabled 9
Hit any key to stop autoboot:
80006970: 046 10 81 e3 1¢ 1000 sss hing
No MDIO bus found ra}
NULL device name! c
No such device: <NULI>
```

## Slide 34

# Exploiting RootBlock

Vulnerability is exploited by writing a malicious u-boot image to iDRAC’s SPI flash. If exploited, RootBlock can lead to persistent, undetectable compromise.

Dell fixed BootBlock in iDRAC9 Version 7.00.00.172 (14G) and 7.10.50.00_A00 (15G/16G) For more information, see our <u>advisory</u> on CVE-2024-38433 and Dell <u>DSA-2024-223</u>

34

## Slide 35

How to fix it: A Recipe

35

## Slide 36

**Modern Hardware Security**

**~~2~~**

> **~~3~~ Hardened Bootloaders**

> **~~1~~ Better Threat Models**

36

## Slide 37

**Modern Hardware Security**

**~~2~~**

> **~~3~~ Hardened Bootloaders**

> **~~1~~ Better Threat Models**

37

## Slide 38

Ingredient #1: Better Threat Models

**Do not assume** that physical security is guaranteed. Consider Insider & Supply Chain risk

**Do not assume** that users/workloads can be trusted. **Consider** your early-boot attack surface!

38

## Slide 39

# Ingredient #1: Bootloader Attack Surface

Network
Storage Hardware Support
IP Stack
Device Drivers
File Systems
Protocols (PXE,
Memory Mgmt
Partitions FTP etc.)
PCIe / NVMe Custom
Image Formats Handlers
USB
Configuration
Remote
Local

39

## Slide 40

# Ingredient #1: Bootloader Attack Surface

Storage Hardware SupportExample: Network
CVE-2023-40547
IP Stack
Device Drivers
File Systems
Protocols (PXE,
Memory Mgmt
Partitions FTP etc.)
PCIe / NVMe Custom
Image Formats Handlers
Configuration
Remote
Local
Credit: Bill Demirkapi

40

## Slide 41

# Ingredient #1: Bootloader Attack Surface

Network
Storage Hardware Support
Example: IP Stack
Device Drivers
CVE-2022-36763File Systems
Protocols (PXE,
Memory Mgmt
Partitions FTP etc.)
PCIe / NVMe
???
Image Formats
Configuration
Remote
Local

41

Credit: Marc Beatove

## Slide 42

Ingredient #1: Bootloader Attack Surface
Network
Storage Hardware Support
This talk:
IP Stack
Device Drivers
File Systems Grub-legacy XFS
CVE 2023-4949
Protocols (PXE,
Memory Mgmt
Partitions FTP etc.)
PCIe / NVMe Custom
Image Formats Handlers
This talk:
Configuration Dell RootBlock
CVE 2024-38433
Remote
Local
42

## Slide 43

#### **Modern Hardware Security**

**~~2~~**

> **~~3~~ Hardened Bootloaders**

> **~~1~~ Better Threat Models**

43

## Slide 44

Ingredient #2: Modern Hardware Security There will always be bugs. A single vulnerability must not lead to full compromise. We need downgrade protection:

Forward Path:
Version 1 Version 1.1 Version 2.0
Blocked Backward Path:
Version 1 Version 1.1 Version 2.0

44

## Slide 45

Ingredient #2: Modern Hardware Security There will always be bugs. A single vulnerability must not lead to full compromise. We need remote attestation:

Device
Stage 1
verify
Stage 2
verify
Stage 3

45

## Slide 46

Ingredient #2: Modern Hardware Security There will always be bugs. A single vulnerability must not lead to full compromise. We need remote attestation:

Device
Stage 1
verify
Stage 2
verify
Stage 3
Trust me bro, I’m totally
running your firmware!

It boots, therefore it must
be running the firmware I
trust!

46

## Slide 47

Ingredient #2: Modern Hardware Security There will always be bugs. A single vulnerability must not lead to full compromise. We need remote attestation:

Device
Root of Trust
Stage 1 Proof
Evidence: aa898f1…
measure
Stage 2
Identity
measure
Stage 3 Freshness

47

## Slide 48

**Modern Hardware Security**

**~~2~~**

> **~~3~~ Hardened Bootloaders**

> **~~1~~ Better Threat Models**

48

## Slide 49

# Ingredient #3: Hardened Bootloaders

There will always be bugs. A single vulnerability must not lead to full compromise. We need exploit mitigations:

Classic Exploit Mitigations

Mitigations such as Stack Canaries and Control Flow Integrity could improve defense in depth

Read-Only Sections

RootBlock could have been prevented if SRAM was made read-only before loading untrusted images

49

## Slide 50

# Ingredient #3: OSS Bootloader Security State

|**Bootloader Project**|**Memory Safe?**|**Exploit Mitigations?**|**Fuzzed?**|**Security Critical?**|
|---|---|---|---|---|
|BootBlock|No|No|No|Yes|
|grub-legacy|No|No|No|Sometimes|
|u-boot|No|No|No|Yes|
|grub2|No|No|Kind of|Yes|
|shim|No|No|Kind of|Yes|
|linuxboot|Partially|No|No|Yes|
|EDK2|No|Optional|Kind of|Yes|
|Arm Trusted
Firmware (ATF)|No|Yes|No|Yes|
|Caliptra Firmware|Yes|Yes|Yes|Yes|

50

## Slide 51

# Ingredient #3: OSS Bootloader Security State

##### **Danger territory**

|**Bootloader Project**|**Memory Safe?**|**Exploit Mitigations?**|**Fuzzed?**|**Security Critical?**|
|---|---|---|---|---|
|BootBlock|No|No|No|Yes|
|grub-legacy|No|No|No|Sometimes|
|u-boot|No|No|No|Yes|
|grub2|No|No|Kind of|Yes|
|shim|No|No|Kind of|Yes|
|linuxboot|Partially|No|No|Yes|
|EDK2|No|Optional|Kind of|Yes|
|Arm Trusted
Firmware (ATF)|No|Yes|No|Yes|
|Caliptra Firmware|Yes|Yes|Yes|Yes|

51

## Slide 52

# Ingredient #3: Discovering more vulnerabilities

Code Scanning Code scanning can catch basic vulnerabilities

LLMs were able to find the presented vulnerabilities. However LLMs they did not uncover more vulnerabilities, yet

Fuzzing

Integrate fuzzers upstream. Extend fuzzers so that they cover our attack surface. Find and report bugs.

52

## Slide 53

# oss-fuzz for Bootloaders

Receive up to 15 000 USD reward for integrating critical open source projects Are popular bootloaders critical? Yes! u-boot integration has already been started Are you a bootloader developer? Please reach out!

53

## Slide 54

##### **Hardened Bootloaders**

# **Thanks!**

**Modern Hardware Security** Hardware should offer more protection against a single compromised **~~2~~** component. In many cases, secure boot is not enough.

**Advisories** <u>grub-legacy XFS cisco-grub script execution Dell RootBlock</u>

Google Cloud - Product Security Engineering

**~~3~~**

**~~1~~**

Hardening bootloaders can increase security for a wide range of devices. Approaches like code review, exploit mitigations and fuzzing work well.

##### **Better Threat Models**

A threat model that considers threats to hardware and firmware is required to improve security in the long term. This can be applied across different bootloaders, vendors or devices.

**Contact** Henrik Ferdinand Nölscher <u>@s1ckcc</u> bootloader-bugs@google.com

54
