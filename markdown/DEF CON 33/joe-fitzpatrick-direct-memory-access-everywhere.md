---
title: "Direct Memory Access Everywhere"
speakers: ["Joe FitzPatrick"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33/Joe FitzPatrick - Direct Memory Access Everywhere.pdf"
pages: 96
sha256: "1c39d33fe460c6f92181f3dd5e60fe31d0f6f267728857557102d69729dba66e"
text_chars: 19272
ocr_pages: 33
has_ocr: true
redacted_secrets: 0
ocr_confidence: 90.0
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T07:04:04Z"
---
# Direct Memory Access Everywhere

**Speakers:** Joe FitzPatrick  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33/Joe FitzPatrick - Direct Memory Access Everywhere.pdf` (96 pages)


## Slide 1

2


> Recovered by OCR — confidence 80/100 on the text kept, 56/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
— Aa]
3& \
DIRECT MEMORY
ACCESS EVERYWHERE
securelyfitz & baelfire 9 AUG 2025
©2025 SecuringHardware.com 2
```

## Slide 2

##### **JOE FITZPATRICK**

10+ years of fun with hardware silicon debug security research pen testing of CPUs security training Applied Physical Attacks Training: X86 Systems Embedded Systems Hardware Pentesting Own white shoes full of LEDs

Joe FitzPatrick

@securelyfitz

joefitz@securinghardware.com

3

## Slide 3

##### **GRACE PARRISH**

Studying cybersecurity at OSU Working as SOC analyst Board level repair technician Taught industrial control systems 9 years PLCs HMIs Enjoys learning Jack of all trades Goal: offensive security career

Grace Parrish

@BaelfireNightshd

4

## Slide 4

This is PCIe.

5


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
This is PCle.
©2025 SecuringHardware.com 5
```

## Slide 5

Tribble, a PCI DMA attack device by Joe Grand

Firewire, external dma spanning 2 millenia

6


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Tribble, a PCl DMA attack
device by Joe Grand
Firewire, external dma
spanning 2 millenia
©2025 SecuringHardware.com 6
```

## Slide 6

A brief tale of epic procrastination:

2014: Slotscreamer 2016: Pcileech 2017: Pcileech FPGA 2019: Thunderclap 2020: Thunderspy more to come...

7

## Slide 7

## **4 QUESTION THREAT MODEL:**

1. 2. 3. 4.

8

## Slide 8

**4 QUESTION THREAT MODEL:** 1. **What are we working on?** 2.

3.

4.

8

## Slide 9

## **4 QUESTION THREAT MODEL:**

1. **What are we working on?** 2. **What can go wrong?** 3.

4.

8

## Slide 10

## **4 QUESTION THREAT MODEL:**

1. **What are we working on?** 2. **What can go wrong?** 3. **What are we going to do about it?** 4.

8

## Slide 11

## **4 QUESTION THREAT MODEL:**

1. **What are we working on?** 2. **What can go wrong?** 3. **What are we going to do about it?** 4. **Did we do a good job?**

8

## Slide 12

### **PCIE THREAT MODEL**

1. **What are we working on?**

2. **What can go wrong?**

3. **What are we going to do about it?**

4. **Did we do a good job?**

10

## Slide 13

### **PCIE THREAT MODEL**

1. **What are we working on?** _High Speed interconnects_ 2. **What can go wrong?**

3. **What are we going to do about it?**

4. **Did we do a good job?**

10

## Slide 14

### **PCIE THREAT MODEL**

1. **What are we working on?** _High Speed interconnects_ 2. **What can go wrong?** _Malicious Devices_

3. **What are we going to do about it?**

4. **Did we do a good job?**

10

## Slide 15

### **PCIE THREAT MODEL**

1. **What are we working on?** _High Speed interconnects_ 2. **What can go wrong?** _Malicious Devices_

3. **What are we going to do about it?** _Keep it inside the case_ 4. **Did we do a good job?**

10

## Slide 16

### **PCIE THREAT MODEL**

1. **What are we working on?** _High Speed interconnects_ 2. **What can go wrong?** _Malicious Devices_

3. **What are we going to do about it?** _Keep it inside the case_ 4. **Did we do a good job?** _Mostly?_

10

## Slide 17

## **ATTACKING PCIE**

1. Connect your hardware 2. Enumerate

3. Enable Bus Master

4. Read or Write memory

5. Present at DEF CON

11

## Slide 18

## **CONNECTING HARDWARE**

12


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CONNECTING HARDWARE
©2025 SecuringHardware.com 12
```

## Slide 19

## **ENUMERATING**

13


> Recovered by OCR — confidence 82/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ENUMERATING
CPU
Root complex Memory
PCle F PCle A
2 ! @ Switch bridge to
endpoint endpoint PCI/PCI-X
PCle Legacy
endpoint endpoint
©2025 SecuringHardware.com 13
```

## Slide 20

## **ENUMERATING**

14


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ENUMERATING
joefitz@linmax2:~§ lspci -tv
-(0000:00]-+-00.@ Advanced Micro Devices, Inc. [AMD] Strix/Strix Halo Root Complex
+-00.2 Advanced Micro Devices, Inc. [AMD] Strix/Strix Halo IOMMU
+-01.0 Advanced Micro Devices, Inc. [AMD] Strix/Strix Halo Dummy Host Bridge
+-01.1-[01-60]--
+-02.0 Advanced Micro Devices, Inc. [AMD] Strix/Strix Halo Dummy Host Bridge
+-02.1-[cl]----00.0 Shenzhen Longsys Electronics Co., Ltd. Lexar NM79@ NVME SSD (DRAN-lLess)
+-02.2-[c2]----00.0 Genesys Logic, Inc GL9755 SD Host Controller
+-02.3-[c3]----00.0 Intel Corporation Wi-Fi 6E(802.11ax) AX210/AX1675* 2x2 [Typhoon Peak]
+-03.0 Advanced Micro Devices, Inc. [AMD] Strix/Strix Halo Dummy Host Bridge
+-08.0 Advanced Micro Devices, Inc. [AMD] Strix/Strix Halo Dummy Host Bridge
©2025 SecuringHardware.com 14
```

## Slide 21

## **READ/WRITE MEMORY**

15


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
READ/WRITE MEMORY
Table 2-2: PCI Express TLP Packet Types
Abbreviated
TLP Packet Types ae
Memory Read Request
Memory Read Request - Locked access MRdLk
Memory Write Request MWr
10 Read IORd
10 Write 1OWr
Configuration Read (Type 0 and Type 1)
CfgRd1
Configuration Write (Type 0 and Type 1) CfgWr0,
Message Request without Data Msg
Message Request with Data MsgD
Completion without Data Cpl
Completion with Data CplID
Completion without Data - associated with Locked Memory Read _ | CpILk
Requests
Completion with Data - associated with Locked Memory Read CpIDLk
Requests
©2025 SecuringHardware.com 15
```

## Slide 22

## **PCILEECH**

16


> Recovered by OCR — confidence 85/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
PCILEECH
= © ufrisk / pcileech Q Type (7) to search B- ++ ©} 2 8B
<> Code © Issues 4 { Pullrequests ©) Actions [fF Projects 1) Wiki © Security |~ Insights
€@ ufrisk Version 4.19.3 3ca4e7b-last week ©) His
9
Preview Code Blame 305 lines (230 loc) - 19.8 KB B
PCILeech Summary:
PCILeech uses PCIe hardware devices to read and write target system memory. This is achieved by using DMA over PCle.
No drivers are needed on the target system.
PCILeech also works without hardware together with a wide range of software memory acqusition methods
supported by the LeechCore library - including capture of remote live memory using DumplIt or WinPmem.
PCILeech also supports local capture of memory and a number of memory dump file formats.
©2025 SecuringHardware.com 16
```

## Slide 23

## **EXAMPLE: DUMPING MEMORY**

17

## Slide 24

## **EXAMPLE: LOCKSCREEN BYPASS**

18

## Slide 25

0:00 / 1:28

19

## Slide 26

### **KEY TAKEAWAY:**

## **PCIE IS PERMISSIVE BY DESIGN**

20

## Slide 27

Joe's DMA Attack Taxonomy: Tethered Drive-By Embedded

**FYI: I made this up**

22

## Slide 28

# **TETHERED**

23


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
TETHERED
©2025 SecuringHardware.com 23
```

## Slide 29

# **DRIVE-BY**

24


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
DRIVE-BY
©2025 SecuringHardware.com 24
```

## Slide 30

# **EMBEDDED**

25


> Recovered by OCR — confidence 94/100 on the text kept, 57/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
EMBEDDED
©2025 SecuringHardware.com 25
```

## Slide 31

#### Types of DMA Attacks

#### **Short Term**

#### **Long Term**

#### Quick access/ hot plug Internal access/ reboot

#### Drive By Tethered

#### Tethered

#### Embedded

26

## Slide 32

## **MULTITENANT THREAT MODEL**

1. **What are we working on?**

2. **What can go wrong?**

3. **What are we going to do about it?**

4. **Did we do a good job?**

28

## Slide 33

## **MULTITENANT THREAT MODEL**

1. **What are we working on?** _Make $ by sharing hardware_ 2. **What can go wrong?**

3. **What are we going to do about it?**

4. **Did we do a good job?**

28

## Slide 34

## **MULTITENANT THREAT MODEL**

1. **What are we working on?** _Make $ by sharing hardware_ 2. **What can go wrong?** _Hardware assisted tenant hopping_ 3. **What are we going to do about it?**

4. **Did we do a good job?**

28

## Slide 35

## **MULTITENANT THREAT MODEL**

1. **What are we working on?** _Make $ by sharing hardware_ 2. **What can go wrong?** _Hardware assisted tenant hopping_ 3. **What are we going to do about it?** _IOMMU!_ 4. **Did we do a good job?**

28

## Slide 36

## **MULTITENANT THREAT MODEL**

1. **What are we working on?** _Make $ by sharing hardware_ 2. **What can go wrong?** _Hardware assisted tenant hopping_ 3. **What are we going to do about it?** _IOMMU!_ 4. **Did we do a good job?** _Mostly?_

28

## Slide 37

29


> Recovered by OCR — confidence 90/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Virtual Machine (n)
Virtual Machine (0)
Ap ADpy App
Driver for Driver for Device Devicg B
Virtual Devices Virtual Devices Driver : Driver
Virtual Machine (n)
Virtual Machine (0)
App App App
Guest OS
Guest OS
Virtual Machine Monitor (VMM) or Hosting GS
Virtual Devices Emulation
A
Device A
Driver
A
8
Devic
Driver
+
1
!
Monitor (VMM) or Hosting OF
'
-Remapping Hardware
Device B Device A
Device A
Example Software-based Direct Assignment of I/O Devices
0 Virtualization
```

## Slide 38

## **KEY TAKEAWAY: DMA MITIGATIONS EXIST**

30

## Slide 39

## **THUNDERBOLT THREAT MODEL**

1. **What are we working on?**

2. **What can go wrong?**

3. **What are we going to do about it?**

4. **Did we do a good job?**

31

## Slide 40

## **THUNDERBOLT THREAT MODEL**

1. **What are we working on?** _High speed peripherals_ 2. **What can go wrong?**

3. **What are we going to do about it?**

4. **Did we do a good job?**

31

## Slide 41

## **THUNDERBOLT THREAT MODEL**

1. **What are we working on?** _High speed peripherals_ 2. **What can go wrong?** _Malicious devices_

3. **What are we going to do about it?**

4. **Did we do a good job?**

31

## Slide 42

## **THUNDERBOLT THREAT MODEL**

1. **What are we working on?** _High speed peripherals_ 2. **What can go wrong?** _Malicious devices_

3. **What are we going to do about it?** _Authenticate and Isolate devices_ 4. **Did we do a good job?**

31

## Slide 43

## **THUNDERBOLT THREAT MODEL**

1. **What are we working on?** _High speed peripherals_ 2. **What can go wrong?** _Malicious devices_

3. **What are we going to do about it?** _Authenticate and Isolate devices_ 4. **Did we do a good job?** _In time... yes!_

31

## Slide 44

About those mitigations: Thunderbolt released OSX 10.8.2 Windows 10 1802 Linux 5.0

32

## Slide 45

About those mitigations: Thunderbolt released _(2011)_ OSX 10.8.2 Windows 10 1802 Linux 5.0

32

## Slide 46

About those mitigations: Thunderbolt released _(2011)_ OSX 10.8.2 _(2012, +1 year)_ Windows 10 1802 Linux 5.0

32

## Slide 47

About those mitigations: Thunderbolt released _(2011)_ OSX 10.8.2 _(2012, +1 year)_ Windows 10 1802 _(2018, + 7 years)_ Linux 5.0

32

## Slide 48

About those mitigations: Thunderbolt released _(2011)_ OSX 10.8.2 _(2012, +1 year)_ Windows 10 1802 _(2018, + 7 years)_ Linux 5.0 _(2019, + 8 years)_

32

## Slide 49

### **KEY TAKEAWAY:**

### **THUNDERBOLT GOT FIXED, EVENTUALLY**

33

## Slide 50

### **HOW ARE WE GONNA DO DRIVE-BY DMA ATTACKS WHEN THUNDERBOLT IS AT LEAST SOMEWHAT SECURED?**

35


> Recovered by OCR — confidence 85/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
HOW ARE WE GONNA DO DRIVE-BY DMA
ATTACKS WHEN THUNDERBOLT IS AT
LEAST SOMEWHAT SECURED?
=
= Life, un. zjinds a way ua
```

## Slide 51

36


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
©2025 SecuringHardware.com 36
```

## Slide 52

37

## Slide 53

## **OCULINK THREAT MODEL**

1. **What are we working on?**

2. **What can go wrong?**

3. **What are we going to do about it?**

4. **Did we do a good job?**

38

## Slide 54

## **OCULINK THREAT MODEL**

1. **What are we working on?** _High speed peripherals_ 2. **What can go wrong?**

3. **What are we going to do about it?**

4. **Did we do a good job?**

38

## Slide 55

## **OCULINK THREAT MODEL**

1. **What are we working on?** _High speed peripherals_ 2. **What can go wrong?** _Malicious devices_

3. **What are we going to do about it?**

4. **Did we do a good job?**

38

## Slide 56

## **OCULINK THREAT MODEL**

1. **What are we working on?** _High speed peripherals_ 2. **What can go wrong?** _Malicious devices_

3. **What are we going to do about it?** _Only use it in secured locations?_ 4. **Did we do a good job?**

38

## Slide 57

## **OCULINK THREAT MODEL**

1. **What are we working on?** _High speed peripherals_ 2. **What can go wrong?** _Malicious devices_

3. **What are we going to do about it?** _Only use it in secured locations?_ 4. **Did we do a good job?** _Not really._

38

## Slide 58

#### Example: Metamask

39


> Recovered by OCR — confidence 90/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
+ Met
Example: Metamask
+
| Add MetaMask
Crypto Wa
aMask
1
Required permissions:
More... v * Access your data for all websites
¢ Input data to the clipboard
¢ Display notifications to you
Firefox Browser
ADD-ONS Extensions Themes
Optional settings:
Allow extension to run in private windows
A This add-on is not actively monitored for security by Mozilla. Make sure you trust it before installin|
Cancel
&@ MetaMask - Crypto Wallet
by danfinlay
The most secure wallet for crypto, NFTs, and DeFi, trusted by millions of users
We 4.1 (44791 382,986 Users
©2025 SecuringHardware.com
Add
jin
39
```

## Slide 59

0:00 / 1:20


> Recovered by OCR — confidence 93/100 on the text kept, 54/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
©2025 SecuringHardware.com
```

## Slide 60

40

## Slide 61

https://github.com/pierce403/PASIV

41


> Recovered by OCR — confidence 92/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
https://github.com/pierce403/PASIV
Preview Code Blame 102 lines (74 loc) - 4
x
PASIV: Peripheral Attack Simulation and Introspection
Vehicle
PASIV is a comprehensive test harness for emulating, executing, and
analyzing Direct Memory Access (DMA) attacks within a controlled
QEMU/KVM environment. This framework aims to provide researchers
and security professionals with a powerful, scriptable, and repeatable
platform for studying DMA vulnerabilities and defenses.
Project Goals
* Automate the setup of vulnerable and hardened virtual machine
targets.
¢ Integrate with leading memory forensics tools like PCILeech,
memflow, and MemProcFS.
¢ Provide a modular framework for developing and executing custom
DMA attack payloads.
¢ Enable the study and verification of IOMMU-based defenses.
* Serve as a research platform for advanced DMA attack and defense techniques.
©2025 SecuringHardware.com 41
```

## Slide 62

### **DMA GAMING CHEATS**

Now, the attacker is the owner.

This changes the threat model!

This is currently an arms race!

43

## Slide 63

44


> Recovered by OCR — confidence 90/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
DMA cheat for Faceit CS2
Only cheat
$30
¥ CS2 cheat for 1 month ©
* you should have DMA Card with
Firmware to use this cheat
Buy now
Basic package
@ DMACARD, rw
$720
¥ CS2 cheat for 1 month ©
¥ DMA PCle Card 75T ©
¥ Firmware for Faceit
* with this package you will be able to
use only radar hack on second PC
Out of stock
©2025 SecuringHardware.com
Full package
@ FULL PACKAGE
$930
¥ CS2 cheat for 1 month @
¥ DMA PCle Card 75T ©
¥ Firmware for Faceit
¥ Makcu for Aimbot ©
v DP Fuser for ESP on monitor ©
Out of stock
44
```

## Slide 64

45


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Pcileech-DMA-NVMe-VMD / README.md (0
@ Ptolemaios9 Update README.md 97e9651-Sdaysago ©) History
Preview Code Blame 21 Lines (45 loc) - 1.57 KB 8) (rw iS)4) Al-) =
Pcileech-DMA-NVMe-VMD
Many firmware scammers sell Beaters free and open source VMD firmware at high prices.
How to get help
discord : https://discord.gg/beater
@ Beaters DC channel offers free firmware (Many scammers firmware distributors are angry because Beater has made VMD firmware
available for free, Try to discredit Beater by claiming that the free firmware is unsafe so that users can buy their paid Poor quality
firmware.),BeaterFreeVMD play the games you want to play!VGK has implemented VMD detection not long ago, and EAC BE still runs
well. Beater Never tried to sell VMD firmware solutions for profit.
Requirements!
¢ Intel CPU (11th Generation or newer) in the main PC where the DMA card is installed.
¢ Intel VMD (Virtual RAID on CPU) must be enabled in BIOS.
¢ Specific Intel drivers must be installed on Windows.
¢ AWindows reinstall may be required for proper driver initialization and device recognition.
AVMD firmware solution has been discovered by game developers, but it is stillsafe, It has been
free and open source from the beginning, Sacirinarerdverecom 45
```

## Slide 65

46


> Recovered by OCR — confidence 89/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Hardware based memory aqusition methods:
Please find a summary of the supported hardware based memory acquisition methods listed below. All
hardware based memory acquisition methods are supported on both Windows and Linux. The FPGA based
methods however sports a slight performance penalty on Linux and will max out at approx: 90MB/s compared
to 150MB/s on Windows.
64-bit
PCIe TLP Project
Device Type Interface Speed memory © roje
access Sponsor
access
Screamer PCle FPGA USB-C 190MB/s ‘Yes Yes
ZDMA FPGA Thunderbolt3. 1000MB/s_ Yes Yes y
LeetDMA FPGA USB-C 190MB/s Yes Yes y
AC701/FT601 FPGA USB3 190MB/s Yes Yes
USB3380-EVB USB3380 | USB3 150MB/s No No
DMA patched HP ic TcP 1MB/s Yes No
iLO
©2025 SecuringHardware.com 46
```

## Slide 66

### **KEY TAKEAWAY: CHANGING FORM FACTOR =**

### **CHANGING THREAT MODEL**

47

## Slide 67

CF Express

#### SD Express

49


> Recovered by OCR — confidence 95/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
SD Express - Highest Speed SD Memory Card Standard
EXPRESS
CF Express SD Express
©2025 SecuringHardware.com 49
```

## Slide 68

## **CFE/SDE THREAT MODEL**

1. **What are we working on?**

2. **What can go wrong?**

3. **What are we going to do about it?**

4. **Did we do a good job?**

50

## Slide 69

## **CFE/SDE THREAT MODEL**

1. **What are we working on?** _High speed small storage_ 2. **What can go wrong?**

3. **What are we going to do about it?**

4. **Did we do a good job?**

50

## Slide 70

## **CFE/SDE THREAT MODEL**

1. **What are we working on?** _High speed small storage_ 2. **What can go wrong?** _Malicious devices? Counterfeit devices?_ 3. **What are we going to do about it?**

4. **Did we do a good job?**

50

## Slide 71

## **CFE/SDE THREAT MODEL**

1. **What are we working on?** _High speed small storage_ 2. **What can go wrong?** _Malicious devices? Counterfeit devices?_ 3. **What are we going to do about it?** _???_

4. **Did we do a good job?**

50

## Slide 72

## **CFE/SDE THREAT MODEL**

1. **What are we working on?** _High speed small storage_ 2. **What can go wrong?** _Malicious devices? Counterfeit devices?_ 3. **What are we going to do about it?** _???_ 4. **Did we do a good job?** _???_

50

## Slide 73

51


> Recovered by OCR — confidence 86/100 on the text kept, 66/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
TB SSD
©2025 SecuringHardware.com 51
```

## Slide 74

## **EXAMPLE: CFEXPRESS ATTACK**

52

## Slide 75

## **EXAMPLE: CFEXPRESS ATTACK**

53

## Slide 76

## **EXAMPLE: CFEXPRESS ATTACK**

54


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
EXAMPLE: CFEXPRESS ATTACK
©2025 SecuringHardware.com
```

## Slide 77

## **SWITCH 2 SDEXPRESS PROGRESS**

55

## Slide 78

#### SDExpress Progress

56


> Recovered by OCR — confidence 82/100 on the text kept, 43/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
SDExpress Progress
= \ho
RS -
= J
©2025 SecuringHardware.com
56
```

## Slide 79

#### SDExpress Progress

57


> Recovered by OCR — confidence 86/100 on the text kept, 55/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
SDExpress Progress
5303 1V3
©2025 SecuringHardware.com
57
```

## Slide 80

#### Who wants to see a switch 2 jailbreak?

58


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Who wants to see a switch 2 jailbreak?
©2025 SecuringHardware.com 58
```

## Slide 81

### **KEY TAKEAWAY: PCIE IS PERVASIVE!**

59

## Slide 82

**A CONTINUING TALE OF EPIC PROCRASTINATION:**

2021: Erebus Schematic 2022: Erebus PCBs 2023: Erebus Test Jig 2024: Erebus Assembled 2025: Profit?

61

## Slide 83

62


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
©2025 SecuringHardware.com 62
```

## Slide 84

63


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
©2025 SecuringHardware.com 63
```

## Slide 85

64


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Other Notes:
The completed solution contains Xilinx proprietary IP cores licensed under the
Xilinx CORE LICENSE AGREEMENT. This project as-is published on Github
contains no Xilinx proprietary IP. Published source code are licensed under the
MIT License. The end user that have downloaded the no-charge Vivado
WebPACK from Xilinx will have the proper licenses and will be able to re-
generate Xilinx proprietary IP cores by running the build detailed above.
©2025 SecuringHardware.com
64
```

## Slide 86

65


> Recovered by OCR — confidence 90/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Projects Launched
EPIC Erebus iCEBreaker-bitsy FPGA iCEBreaker FPGA
A tiny PCle DMA tool that's fully An open source iCE40 FPGA dev board in a An open source iCE40 FPGA development
customizable with an open toolchain and Teensy form factor board designed for teachers and students
gateware
Coming Soon Coming Soon 992% Funded! Stock
Sign up Sign up $148,949
Tigard Glasgow Interface
An open source FT2232H-based, multi- Explorer
protocol, multi-voltage tool for hardware
A highly capable and extremely flexible open
hacking
source multitool for digital electronics
$145,610 $430,222 2,212
```

## Slide 87

## **WHY EREBUS?**

#### Platform Security

67

## Slide 88

68

## Slide 89

### **KEY TAKEAWAYS:**

PCIe is permissive by design DMA Mitigations exist Thunderbolt got fixed, eventually Form factor changes your threat model PCIe is Pervasive! Progress has been made -

but there's still way more to do!

69

## Slide 90

## **4 QUESTION THREAT MODEL:**

1. **What are we working on?** 2. **What can go wrong?**

3. **What are we going to do about it?** 4. **Did we do a good job?**

70

## Slide 91

71


> Recovered by OCR — confidence 88/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
a blackhat event B/S =n a
ATTEND ~ BRIEFINGS ~ ARSENAL ~ SUMMITS ~ FEATURES ~ BUSINESS HALL SPONSORS ~
All times are in Eastern Time (GMT/UTC -4h) fy / a
Security is Easier Before PCB Assembly: Easy Threat Modeling for Hardware
SPEAKERS Eric Evenchick | Co-Founder and Managing Partner, Tetre! Security
tack | President, Shostack + Associates
FitzPat | Trainer and Researcher, SecuringHardware.com
Format: 45-Minute Briefings
Tracks: Security Essentials & Lessons Learned, Cyber-physical & Embedded Security
©2025 SecuringHardware.com 71
```

## Slide 92

72


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
©2025 SecuringHardware.com 72
```

## Slide 93

#### **THANKS**

Prior Art/Inspriation: Support/tooling Kingpin Esden Metlstorm Aki-Nyan Snare Dragonmux Carmaa Whitequark Ufrisk Gaya Tech Mossman Dean Pierce And many more...

73

## Slide 94

#### **DIRECT MEMORY ACCESS EVERYWHERE**

Presentation: github.com/securelyfitz/ DirectMemoryAccessEverywhere Erebus Design: github.com/epic-erebus CrowdSupply: crowdsupply.com/securinghw/erebus

74

## Slide 95

75


> Recovered by OCR — confidence 78/100 on the text kept, 54/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
— Aa]
3& \
DIRECT MEMORY
ACCESS EVERYWHERE
securelyfitz & baelfire 9 AUG 2025
©2025 SecuringHardware.com WAs)
```

## Slide 96
