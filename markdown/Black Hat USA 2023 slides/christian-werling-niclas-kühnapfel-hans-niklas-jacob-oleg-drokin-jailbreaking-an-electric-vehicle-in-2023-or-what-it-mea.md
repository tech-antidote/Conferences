---
title: "Niclas Kühnapfel    Hans Niklas Jacob    Oleg Drokin Jailbreaking an Electric Vehicle in 2023 or What It Means to Hotwire Tesla's x86-Based Seat Heater"
speakers: ["Christian Werling"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/Christian Werling _ Niclas Kühnapfel  _ Hans Niklas Jacob  _ Oleg Drokin_Jailbreaking an Electric Vehicle in 2023 or What It Means to Hotwire Tesla's x86-Based Seat Heater.pdf"
pages: 92
sha256: "90ec702582fd8fbbc029f42f773a83f87e7bf0585d83fac2736a43b3686c62e4"
text_chars: 33055
ocr_pages: 19
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:15:11Z"
---
# Niclas Kühnapfel    Hans Niklas Jacob    Oleg Drokin Jailbreaking an Electric Vehicle in 2023 or What It Means to Hotwire Tesla's x86-Based Seat Heater

**Speakers:** Christian Werling  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Christian Werling _ Niclas Kühnapfel  _ Hans Niklas Jacob  _ Oleg Drokin_Jailbreaking an Electric Vehicle in 2023 or What It Means to Hotwire Tesla's x86-Based Seat Heater.pdf` (92 pages)

## Slide 1

Jailbreaking an Electric Vehicle in 2023 WHAT IT MEANS TO HOTWIRE TESLA'S X86-BASED SEAT HEATER

Chris&an Werling Niclas Kühnapfel TU Berlin Hans Niklas Jacob Oleg Drokin Independent

## Slide 2

# Tesla’s Infotainment Now AMD-Powered

2

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Tesla’s Infotainment Now AMD-Powered
Tesla to Soon Start Delivering Model 3 &
Y with AMD Ryzen Chips to Europe,
Parts Catalog Hints
```

## Slide 3

# Our Previous AMD Research

3

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
faulTPM: Exposing AMD fTPMs’ Deepest Secrets
Hans Niklas Jacob*, Christian Werling*, Robert Buhren, Jean-Pierre Seifert!
e
Technische Universitit Berlin cT
ur Previous esearc aes
{ hnj, cwerling, roberi.buhren, jpseifert }@sect.tu-berlin.de
1) mediacec.de ES) OO
me Oat
One Glitch to Rule Them All: Fault Injection Attacks Against
Uncover, Understand, Own - Regai AMD’s Secure Encrypted Virtualization
trol Over Your AMD CPU
os Robert Buhren Hans Niklas Jacob
robert. buhren@sect.tu-berlin.de hnj@sect.tu-berlin.de
mnische Universitat Berlin - SECT Technische Universitit Berlin - SECT
bboot
e and
Mt the
Thilo Krachenfels
tkrachenfels@sect.tu-berl:
‘Technische Universitit Berlin - S Technische Universitat Ber!
Fraunhofer SIT
(0S).
fonent
Uncover, Understand, Own EM-Fault It Yourself: Building a Replicable EMFI
Setup for Desktop and Server Hardware
Introduce software-
Kiihnapfel*, Robert Buhren*, Hans Niklas Jac Thilo Krachenfe! pe ROR spi
Christian Werling*, Jean-Pierre Seifert* BE trstanciation of
* Technische Universitit Berlin, Chair of Security in Telecommunications, Germany
} Fraunhofer SIT, Germany encryption keys
frure, AMD CPUs
AMD Secure Pro:
Eonditions of fe so0t-of-trust for
One Glitch to Rule Them All: Fault pe vie
Injection Attacks against AMD’s : —
Secure Processor Biicting vos
Robert Buhren B (3-15) and
Hans Niklas cob Technische Universitat Berlin Insecure Until Proven Updated: fs and CPUs.
Analyzing AMD SEV’s Remote Attestation | Pagrethe
Pthe DUT by
Robert Buhren Christian Werling Jean-Pierre Seifert uly changing
robert buhren@sect.tu-berlin.de hhristian.werling@student hpide ipseifert@se Fe. both tech.
Technische Universitt Berlin Hasso Plattner Institute, Potsdam 1 che c to the power
Security in Te fasive attacks.
decapsulated
jon-shiclding
technologies to ng is one of FFI and EMFI
duccepeed Bs and change
to trust the o¢ high availability of
berlin
of this technology. However, outsourcing
prise data comes at a risk, The technical inf | aagetiseiaad
Tage glitching,
among multiple tenants. Executin the cloud is owned by the cloud provider and thus under his
visor has dir ° mntrol. This J server hardware
hat allow the co-location of multi
AMD Secure Encrypted Virtualization (SEV) claim: - s range fro onfiguration of software componen
of protection in such cloud seenari 'V encrypts the main n government access [8
1 machines with ic keys, the 0 ca ¢ threats, the research community, as well as in
slow secure cloud computing
```

## Slide 4

# Why Jailbreak a Car?

Many reasons:

- to ”look around” (curiosity)

- to replace its soHware

- **to ac&vate so*-locked features**

What you know
What you know
you don’t know
What you don’t know
you don’t know

4

## Slide 5

5

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
8:48 7 oat! > 84)
@ tesla.com
< Back to Vehicle Profile
Upgrades
Rear Heated Seats
ers riding experience
```

## Slide 6

# Outline

**1** Analyzing Boot and Firmware Security **2** Hotwiring the Infotainment system **3** ExtracOng Secrets from the Tesla

6

## Slide 7

Model 3 Car Computer

7

## Slide 8

Infotainment and Connec:vity ECU (ICE)

8

## Slide 9

Cooling chassis

9

## Slide 10

Autopilot v3

10

## Slide 11

Infotainment and Connec:vity ECU (ICE)

11

## Slide 12

ICE (Backside)

12

## Slide 13

Gateway
•
NXP MPC5748G µController
•
PowerPC-based
•
FreeRTOS-based OS
•
SD card reader for logs
•
Boots from internal flash
•
manages car confgura:oni
ICE (Backside)

13

## Slide 14

# Car configuraGon

- Stored and managed by the Gateway

- Lists (paid) hardware and soHware features

   - Car performance

   - Ba-ery capacity (for so3ware-locked ba-eries)

   - Level of Autopilot: (Enhanced) Autopilot, Full Self-Driving capability

   - Car region

   - Rear seat heaters

14

## Slide 15

Infotainment APU

- AMD Zen 1 CPU, Vega GPU

- • Linux 5.4

- • Firmware and recovery system on SPI flash

- • System and user par::on on NVMe ICE (Backside)

15

## Slide 16

# Previous Tesla Hacking

- Threat model: _Outsider_ who is remote or in physical proximity

- Goal: Access/control car

**REGULAR EXPLOITATION OF A TESLA MODEL 3 THROUGH CHROMIUM REGEXP**

- SoHware-based vulnerabiliOes: Can be fixed by Tesla over-the-air

16

## Slide 17

# PlaIorm Threats from the _Inside_

- Threat model: Insider who already has **digital and physical access to the car**

- Goal: Tweak car beyond normal flows • acHvate **so#-locked features** without paying

   - li3 repair and regulaHon restricHons

- Insider not limited to soHware-based aYacks

17

## Slide 18

# Verified Boot

**x86**

⏸

**Non-vola(le storage** SPI Flash NVMe

18

## Slide 19

Verified Boot
x86 ⏸ Coreboot
Non-vola(le storage
SPI Flash Coreboot
NVMe

19

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Verified Boot
x86 wv
Coreboot
eee ackin XH1)
PET deve 10p/2021. 44. 25. 2-8836-gb025¢688348a |
Thu Jan 13 14:46:27 UTC 2022 ai 2 2 8836- abt (log leve
PMxC@ STATUS: @x800 BIT11
coreboot-archive/develop/2021.44.25.2-8836-gb025c688348a
Thu Jan 13 14:46:27 UTC 2022 ponecaqe ceaer inal (log level
POST: x41
POST: @x42
POST: 0x43
POST: Qx34
POST: x36
POST: @x92
POST: x98
SF size 0x2000000 does not correspond to CONFIG_ROM_SIZE
0x1000000!!
POST: 0x44
coreboot—archive/develop/2021. 44.25.2-8836-gb025c688348a
‘Thu Jan 13 14:46:27 UTC 2022 raNstage startind (log level
Bile co
POST: x39
POST: x8@
POST: 0x70
POST: x71
Board name: Spinach
19
```

## Slide 20

# Verified Boot

verifies
Tesla
x86 ⏸ Coreboot
OS Loader
Non-vola(le storage
Tesla
SPI Flash Coreboot
OS Loader
NVMe

20

## Slide 21

# Verified Boot

🔗 verifies
Tesla
x86 ⏸ Coreboot Linux Kernel
OS Loader
Non-vola(le storage
Tesla
SPI Flash Coreboot
OS Loader
Linux
NVMe
kernel

21

## Slide 22

Verified Boot
verifies🔗 🔗 verifies
Tesla
x86 ⏸ Coreboot Linux Kernel Root FS
OS Loader
Non-vola(le storage
Tesla
SPI Flash Coreboot
OS Loader
Linux
NVMe … RootFS A RootFS B … nvme0n2
kernel

22

## Slide 23

# Verified Boot

🔗

🔗

🔗

Tesla
x86 ⏸ Coreboot Linux Kernel Root FS
OS Loader
Non-vola(le storage
Tesla
SPI Flash Coreboot
OS Loader
Linux
NVMe … RootFS A RootFS B … nvme0n2
kernel

23

## Slide 24

How to get a **root shell** Many opOons:

- Spawn serial shell on boot

- • Add  SSH key to `authorized_keys` file

- Add known SSH password

They all require **changes** to the Root file system

# SSH
password
RootFS A

24

## Slide 25

loaded
rejected
Verified Boot
⛔
🔗 🔗 verifies
Tesla
x86 ⏸ Coreboot Linux Kernel Root FS
OS Loader
Non-vola(le storage
Tesla
SPI Flash Coreboot
OS Loader
#
Linux
NVMe … RootFS A RootFS B … nvme0n2
kernel

25

## Slide 26

# dm-verity

- Integrity checking of block devices • When a block is read into memory, it’s hashed in parallel

- Merkle tree used to efficiently store and verify hashes of individual block

   - Trusted root file system represented by root hash

#
# #
01 10 11 00

- Intermediate hashes stored alongside data

19.06.23

26

## Slide 27

# dm-verity **_# Patch_**

19.06.23

27

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
—— i
+ +--39@ lines: 00000000: 7f45 4c46 0201 0100 00200 0000 0200 0000 «ELF --- £46 @201 0100 0000 20020 2000 2000 .ELF
@0001860: Sdc3 5548 89e5 5348 8did dal3 200@ 4883 ].UH..SH.... .H. 8did dal3 200@ 4883 ].UH..SH.... .H.
@0001870: ec08 4883 eb@8 488b 0348 83f8 ff74 O4ff ..H...H..H...t.. 0348 83f8 ff74 O4ff ..H...H..H...t.
@0001880: d@eb ef58 Sb5d c350 e86a fF6ff FF58 c325 ...X[].P.j...X.% e86a f6off ff58 c325 ...X[].P.j...X.%
@0001890: 752@ 2575 2025 752@ 256c 752@ 256c 7520 u %u %U %lu %lu 256c 752@ 256c 7520 u %uU %U %lu %luU
@00018a@: 2531 3673 2025 3132 3873 2025 3132 3873 %16s %128s %128s 3873 2025 3132 3873 %16s %128s %128s
@00018b0: 2025 7500 556e 6b6e 6f77 6e2@ 6572 726f  %u.Unknown erro 6f77 6e20 6572 726f  %u.Unknown erro
@00018c@: 720@ 3200 342e 3100 7265 7374 6172 745f 1r.2.4.1.restart_ fee? 6e6f 7265 5f63 r.2.4.1.ignore_c
000018d0: 6f6e 5f63 6f72 7275 7074 696f 6e20 0075 on_corruption .u e2@ 2020 2020 0075 orruption U
Q00018e0: 7365 5f66 6563 5f66 726f 6d5f 6465 7669 se_fec_from_devi 726f 6d5f 6465 7669 se_fec_from_devi
@00018f@: 6365 2025 7320 6665 635f 726f 6f74 7320 ce %s fec_roots 635f 726f 6f74 7320 ce %s fec_roots
@0001900: 2575 2066 6563 5f62 6c6f 636b 7320 256c %u fec_blocks %l 6c6f 636b 7320 256c %u fec_blocks %l
@0001910: 752@ 6665 635f 7374 6172 7420 2531 246c wu fec_start %1$1 6172 7420 256¢ 7520 u fec_start %lu
00001920: 7520 6c69 6e65 6172 2025 3324 7320 3020 u linear %3$s 0 per 6974 7920 2575 .0 %lu verity %u
00001930: 2325 3131 2473 2000 7520 2575 2025 6c75 #%11$s .u %u %lu 520 2575 2025 6c75 %s %s %u %u %lu
@0001940: 2025 6c75 2025 7320 2573 2025 7300 2025 %lu %s %s %S. % 2573 2025 7300 2025 %lu %s %s %s. %
00001950: 7a75 2025 7300 2f75 7372 2f73 6269 6e2f zu %s./usr/sbin/ 7372 273 6269 6e2f zu %s./usr/sbin/
Q0001960: 646d 7365 7475 700@ 6372 6561 7465 @@2d dmsetup.create. - 6372 6561 7465 002d dmsetup.create. -
Q0001970: 720@ 2d2d 7461 626c 650@ 7265 6d6f 7665 r.--table.remove 6500 7265 6d6f 7665 r.--table.remove
@0001980: Q@2d 2d66 6f72 6365 O@2d 2d72 6574 7279 .--force.--retry @02d 2d72 6574 7279 .--force.--retry
@0001990: Q@2d 2d64 6566 6572 7265 640@ 4553 5550. .--deferred.ESUP 7265 640@ 4553 5550 .--deferred.ESUP
+ +--453 lines: @00019a@: 4552 4241 4400 496e 7661 6c69 6420 7375 ERBAD. Invalid su--- B41 4400 496e 7661 6c69 6420 7375 ERBAD.Invalid su---
19.06.23 27
```

## Slide 28

loaded
rejected
Verified Boot
# Patch
🔗 🔗
Tesla
x86 ⏸ Coreboot Linux Kernel Root FS
OS Loader
Non-vola(le storage
Tesla
SPI Flash Coreboot
OS Loader
# #
Linux
NVMe SSD … RootFS A RootFS B … nvme0n2
kernel

28

## Slide 29

loaded
rejected
Verified Boot
⛔
🔗 verifies
Tesla
x86 ⏸ Coreboot Linux Kernel Root FS
OS Loader
Non-vola(le storage
Tesla
SPI Flash Coreboot
OS Loader
# #
Linux
NVMe SSD … RootFS A RootFS B … nvme0n2
kernel

29

## Slide 30

# Tesla OS Loader **_# Patch_**

30

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Tesla OS Loader ' # Patch |
ee |
00101b11
00101b14
@0101b19
@0101ble
0101b23
00101b26
@0101b29
00101b2c
00101b2f
00101b32
0101b34
00101b37
00101b38
00101b39
0101b3e
@0101b41
00101b44
@0101b48
00101b4a
0101b4d
0101b52
@0101b57
0101b5a
0101b5d
LAB_00101b11
SUB
PUSH
PUSH
CALL
ADD
MOV
SUB
MOV
MOV
ADD
SUB
PUSH
PUSH
CALL
ADD
MOV
CMP
IZ
SUB
PUSH
CALL
ADD
SUB
PUSH
s_Verifying_nvme_image..._@011516
s_[tes la-os-loader]_%s_@0114c51
puts
0x1
,dword ptr
,dword ptr
,»dword ptr
,dword ptr
Oxé
2
FUN_00100b96
0x1
dword ptr [
dword ptr [
LAB_00101b88
A)
s_[tesla-os-loader]_Invalid_boot_
puts
0x10
@x
,
dword ptr [
}
= FUN_@0100b96(
)
puts(
*param_3 =
puts(
return
}
puts (
uVar2 = FUN_@0100c@a(local_24);
FUN_01000f4(uVar2, 0x20);
puts (&DAT_00114beb);
+
,
}
:
else {
puts(s_[tesla-os-Loader]_Invalid_boot_c_00114d78);
uVar2 = FUN_@010@cOa(local_24);
FUN_001000f4(UVar2,0x20);
puts (&DAT_@0114beb);
}
}
}
*xparam_3 = 0;
+
}
else {
}
return 0;
puts(s_[tesla-os—loader]_%s_@0114c51,5_ERROR:_Could_not_find_or_initial_00114f74);
```

## Slide 31

# Tesla OS Loader **_# Patch_**

31

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Tesla OS Loader ' # Patch |
Saas
Listing: tesla-
LAB_00101b11
@0101b11 83 SUB 0x8 ~ = FUN_00100b96(
@0101b14 68 PUSH s_Verifying_nvme_image..._@011516 ==01-t
11 puts(
@0101b19 68 PUSH s_[tesla-os-loader]_%s_0@114c51 *param_3 =
11 puts (
@0101ble e8 CALL puts return
00 }
@0101b23 83 ADD 10x16 puts(
@0101b26 8b MoV ,dword ptr a C uVar2 = FUN_@0100c@a(local_24);
@0101b29 2b SUB ,dword ptr a1_18 FUN_001000f4(uVar2, 0x20);
@01@1b2c 8b Mov ,dword ptr Local_10 puts (&DAT_00114beb);
@0101b2f 8b 5 MOV ,dword ptr local_18 +
@0101b32 01 ADD ' ,
00101b34 83 SUB 0x8 }
00101b37 50 PUSH :
00101b38 52 PUSH else {
@0101b39 e8 CALL FUN_@01@0b96 puts(s_[tesla-os-Loader]_Invalid_boot_c_00114d78);
ff uVar2 = FUN_0010@c@a(local_24);
@0101b3e 83 ADD 0x1 FUN_001000f4(UVar2,0x20);
@0101b41 89 MoV dword ptr [ C 4 puts (&DAT_00114beb) ;
00101b44 83 cMP dword ptr [ 124] ,0x@ }
@0101b48 eb IMP} LAB_00101b88 }
00101b4a 83 SUB ,OXxc }
00101b4d 68 PUSH s_[tesla-os-loader]_Invalid_boot_ *param_3 = 0;
11 +
@0101b52 e8 CALL puts }
00 else {
@0101b57 83 ADD A) puts(s_[tesla-os—loader]_%s_@0114c51,5_ERROR:_Could_not_find_or_initial_00114f74);
00101b5a 83 SUB Ox }
@0101b5d ff PUSH dword ptr [ 1.24 return 0;
```

## Slide 32

loaded
rejected
Verified Boot
🔗 # Patch
Tesla
x86 ⏸ Coreboot Linux Kernel Root FS
OS Loader
Non-vola(le storage
#
Tesla
SPI Flash Coreboot
OS Loader
# #
Linux
NVMe SSD … RootFS A RootFS B … nvme0n2
kernel

32

## Slide 33

loaded
rejected
Verified Boot
⛔
verifies
Tesla
x86 ⏸ Coreboot Linux Kernel Root FS
OS Loader
Non-vola(le storage
#
Tesla
SPI Flash Coreboot
OS Loader
# #
Linux
NVMe SSD … RootFS A RootFS B … nvme0n2
kernel

33

## Slide 34

loaded
rejected
Verified Boot
# Patch
Tesla
x86 ⏸ Coreboot Linux Kernel Root FS
OS Loader
Non-vola(le storage
# #
Tesla
SPI Flash Coreboot
OS Loader
# #
Linux
NVMe SSD … RootFS A RootFS B … nvme0n2
kernel

34

## Slide 35

loaded
rejected
Verified Boot
⛔
⁉ verifies
Tesla
x86 ⏸ Coreboot Linux Kernel Root FS
OS Loader
Non-vola(le storage
# #
Tesla
SPI Flash Coreboot
OS Loader
# #
Linux
NVMe SSD … RootFS A RootFS B … nvme0n2
kernel

35

## Slide 36

# AMD Secure Processor

- ARMv7 µController

- Integrated into CPU SoC

- Highly privileged

- Variety of responsibiliOes

SP
APU

- Hardware root of trust

- Firmware TPM (fTPM) for key management and more

- (On EPYC Servers) Secure Encrypted VirtualizaHon

36

## Slide 37

loaded
rejected
AMD PlaIorm Secure Boot
Tesla
x86 ⏸ Coreboot Linux Kernel Root FS
OS Loader
⛔
verifies
ROM
Off-Chip
AMD SP ▶
Boot Loader Boot Loader
Non-vola(le storage
# #
AMD Root  Tesla
Off-Chip Boot
SPI Flash Coreboot
Key Loader OS Loader
# #
Linux
NVMe SSD … RootFS A RootFS B … nvme0n2
kernel

37

## Slide 38

loaded
rejected
AMD PlaIorm Secure Boot
Tesla
x86 ⏸ Coreboot Linux Kernel Root FS
OS Loader
# Patch
verifies
ROM
Off-Chip
AMD SP ▶
Boot Loader Boot Loader
Non-vola(le storage
# # #
AMD Root  Tesla
Off-Chip Boot
SPI Flash Coreboot
Key Loader OS Loader
# #
Linux
NVMe SSD … RootFS A RootFS B … nvme0n2
kernel

38

## Slide 39

# AMD PlaIorm Secure Boot

loaded
rejected

Tesla
x86 ⏸ Coreboot Linux Kernel Root FS
OS Loader
⛔
ROMROM verifies Off-ChipOff-Chip
AMD SP ▶
BoB o ot Loadert Loader Boot LoaderBoot Loader
Non-vola(le storage
# # #
AMD Root  Tesla
Of-Chip Boot  f
SPI Flash Coreboot
Key Loader OS Loader
# #
Linux
NVMe SSD … RootFS A RootFS B … nvme0n2
kernel

39

## Slide 40

# Previous AMD SP VulnerabiliGes

- 2019: Off-Chip Boot Loader Buffer overflow

⛔
ROM verifes i
Off-Chip
AMD SP
Boot Loader Boot Loader
Non-vola(le storage
#
AMD Root
Off-Chip Boot
SPI Flash
Key Loader

   - ✅

   - • Arbitrary Code ExecuHon

   - **Fixed via firmware updates**

- 2020: ROM Boot Loader Buffer overflow

   - ✅

   - • Arbitrary Code ExecuHon

   - Not fixable (ROM)

   - Fixed in new generaHons (>= Zen 2)

   - **Fixes backported to Tesla’s Zen 1 APU**

40

## Slide 41

# Tesla’s Security EvoluGon

2014

- Open X servers

- Hardcoded passwords

- DiagnosOc Ethernet: root

2023

   - Firmware and OS signing

   - Chain of trust during boot

   - **Root of trust in AMD SoC**

- No code signing

41

## Slide 42

# Outline

**1** Analyzing Boot and Firmware Security **2** Hotwiring the Infotainment system **3** ExtracOng Secrets from the Tesla

42

## Slide 43

loaded
rejected
Regular Early Boot VerificaGon
ROM Boot Loader
Of-Chip f
AMD SP Load Compare to hash Load & Verify
Boot Loader
ARK Hash
Non-vola(le storage
Of Off-Chip Boot  -Chip Boot  f
SPI Flash AMD Root Key
Loader Loader

# Regular Early Boot VerificaGon

43

## Slide 44

# Failed Early Boot VerificaGon

loaded
rejected

ROM Boot Loader
AMD SP Load Compare to hash ⛔
ARK Hash
Non-vola(le storage
Patched
Off-Chip Boot Off-Chip Boot
SPI Flash AMD Root Key
LoaderLoader

44

## Slide 45

# Fault InjecGon AQacks

**Induce fault by altering the IC’s environment:**

- Laser, electromagneHc-radiaHon, clock, supply voltage

## **Voltage Glitching:**

- Lowering voltage shortly

_width_

_fall *me_

_rise *me_

45

## Slide 46

# Key Challenges

- **Most faults are “useless”**

- **Trigger:** Figure out when targeted check happens

- **Parameters:** Voltage drop steepness, width, minimum

- **Reset/Success:** IdenOfy failed aYacks and retry as fast as possible

Glitch

if input() ==
“teslaSecret123”
System Lock,
Con&nue  Ignore
Reset,
normally comparison
Error
print(„Incorrect!“)

```
print(„Correct!“)
```

46

## Slide 47

loaded
rejected
Failed Early Boot VerificaGon
ROM Boot Loader
AMD SP Load Compare to hash ⛔
ARK Hash
Non-vola(le storage
#
Off-Chip Boot Off-Chip Boot
SPI Flash AMD Root Key
LoaderLoader

# Failed Early Boot VerificaGon

47

## Slide 48

loaded
rejected
Glitched Early Boot VerificaGon
ROM Boot Loader
Off-Chip
AMD SP Load Compare to hash ✅ Load & Verify
Boot Loader
ARK Hash
Non-vola(le storage
# #
Off-Chip Boot Off-Chip Boot
SPI Flash AMD Root Key
LoaderLoader
Glitch

48

## Slide 49

# Finding the ARK VerificaGon Time Window

Load ARK Verify ARK Load & Verify Off-Chip BL?
Original ARK
SPI bus
ARK bytes
Modified ARK
⛔
SPI bus

49

## Slide 50

AMD SoC
VR
VSoC
SVI2 AMD SP
VCORE
SMU
x86 cores

# Dynamic Voltage Control

- SMU monitors SoC and uses the SVI2 bus to communicate with the external voltage regulator (VR)

- • SVI2 allows to control two voltage domains per VR

50

## Slide 51

AMD SoC
ATX reset
Teensy
µController VR
VSoC
SVI2 AMD SP
FLASH
VCORE
SMU
SPI
Glitch Setup
• Teensy
• Inject SVI2 packets
• Resets target via ATX reset line
x86 cores
• Monitors the SPI bus (CS) to trigger

   - Resets target via ATX reset line

   - • Monitors the SPI bus (CS) to trigger voltage glitch

- External PC controls glitch parameters

51

## Slide 52

# Voltage Glitch Wiring

SVI2 bus (SVD + SVC)

SPI chip-select

52

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Voltage Glitch Wiring
SVI2 bus (SVD + SVC)
Dot
a> esa
Lv.
—
SPI chip-select
use gon04
52
```

## Slide 53

Glitch Setup in Reality
SVI2 bus
Teensy
µController
SPI bus
ATX reset
SPI programmer
Serial output

53

## Slide 54

# Voltage Glitch Steps

**SVI2 SVC SVI2 SVD**

VSoC

**SPI CS** failed

**SPI CS**

success

- SVI2 SVC: bus clock

   - VSoC: target’s voltage

- SVI2 SVD: bus data

- SPI CS: chip-select signal

54

## Slide 55

# Voltage Glitch Steps

SVI2 SVC
SVI2 SVD
VSoC
SPI CS
failed
SPI CS
success

- SoC sets iniHal voltage

- SVD rising edge triggers a-ack logic

- VSoC rises

55

## Slide 56

# Voltage Glitch Steps

SVI2 SVC
SVI2 SVD
VSoC
SPI CS
failed
SPI CS
success

- VR sends telemetry packets

- VSoC stable

56

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Voltage Glitch Steps
svizsve VM fh
svizsv> | | a
BV MAA AAA
VSOC isv
SPICS “™
failed Low
sPICcs “™
SUCCESS Low
e VR sends telemetry packets
e VSOoC stable
56
```

## Slide 57

# Voltage Glitch Steps

SVI2 SVC
SVI2 SVD
VSoC
SPI CS
failed
SPI CS
success

- Teensy injects SVI2 packets

   - VSoC is adjusted

- Disable telemetry to avoid collisions

57

## Slide 58

# Voltage Glitch Steps

SVI2 SVC
SVI2 SVD
VSoC
SPI CS
failed
SPI CS
success

- Teensy starts counHng CS edges to trigger glitch on Hme

- CS becomes acHve à AMD SP loads data

58

## Slide 59

# Voltage Glitch Steps

SVI2 SVC
SVI2 SVD
VSoC
SPI CS
failed
SPI CS
success

- Teensy injects two SVI2 packets to create voltage disturbance

- Voltage drop on VSoC (glitch)

59

## Slide 60

# Voltage Glitch Steps

SVI2 SVC
SVI2 SVD
VSoC
SPI CS
failed
SPI CS
success

- Teensy monitors CS to detect success

   - CS inacHve (high) à failed a-empt

- Teensy resets target on fail

- CS acHve (low) à successful a-empt

60

## Slide 61

loaded
rejected
AMD PlaIorm Secure Boot
Tesla
x86 ⏸ Coreboot Linux Kernel Root FS
OS Loader
⛔
ROMROM verifies Off-ChipOff-Chip
AMD SP ▶
BoB o ot Loadert Loader Boot LoaderBoot Loader
Non-vola(le storage
# # #
AMD Root  Tesla
Of-Chip Boot  f
SPI Flash Coreboot
Key Loader OS Loader
# #
Linux
NVMe SSD … RootFS A RootFS B … nvme0n2
kernel

61

## Slide 62

loaded
rejected
AMD PlaIorm Secure Boot
Tesla
x86 ⏸ Coreboot Linux Kernel Root FS
OS Loader
ROMROM
Off-Chip
AMD SP ▶
BoB o ot Loadert Loader Boot Loader
Non-vola(le storage
# # # #
AMD Root  Tesla
Off-Chip Boot
SPI Flash Coreboot
Key Loader OS Loader
# #
Linux
NVMe … RootFS A RootFS B … nvme0n2
kernel
Glitch

62

## Slide 63

Trying to AcGvate the Rear Seat Heaters

63

## Slide 64

# Finding their ConfiguraGon ID

64

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Finding their Configuration ID
eee
1 {
2 "accessId": 13,
3 "codeKey": "rearSeatHeaters",
4 "content': i
5 "enums": [
6 {
7 "codeKey": "NONE",
8 "description": "None",
9 "value": 0
10 }
11 {
12 "codeKey": "KONGSBERG_LOW_POWER",
25, "description": "Kongsberg Low-power heaters",
14 "value": 1
15 }
16 J
17 },
18 "description": "Type of rear seat heaters installed",
19 "nroducts": [
20 "Model3",
21 "Modely"
22 J
23 }
```

## Slide 65

Serial console
A^ack script
SSH console

65

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
deploy@psp-deploy:~/tesla—-hacking$ picocom /dev/ttyUSBHUB1® —b 115200 | tee -a $(|deploy@psp-deploy:~/tesla/fi-attack$ python3 start-tesla.py -r ../../tesla-hacking/
date +"%Y_%m_%d").log roms/boot_nvme. bin
Serial console
Attack script
deploy@psp-deploy:~$ ssh -t root@192.168.90.10@ ‘bash’
SSH console
```

## Slide 66

Trying to AcGvate the Rear Seat Heaters

66

## Slide 67

# What About Persistence?

- Sorry, voltage glitch is not persistent

   - Need to glitch on every Infotainment boot

   - But the car configuraHon survives regular infotainment (re)boot

   - And Infotainment supposedly doesn’t reboot very o3en

- Glitching could be made even smoother by a mod chip/PCB 🙃

- • ImplementaHon detail …

   - _We leave this as an exercise to the interested audience_

67

## Slide 68

# Secure ConfiguraGon Items

- Demo possible since the rear seat heaters were an “insecure configuraOon item” in our Gateway firmware version

   - ”Secure configuraHon items” can only be changed with a valid signature

- “ **Rear seat heaters were upgraded to be a signed configura4on star4ng in the 2022.44 release** ”, Tesla told us

- So being root on the Infotainment is not sufficient

   - So3ware or hardware vulnerability in Gateway necessary

68

## Slide 69

69

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ZERO DAY
INITIATIVE
PRIVACY WHO WE ARE HOW IT WORKS BLOG ADVISORIES LOGIN | SIGN UP
July 18th, 2023
(Pwn20wn) Tesla Model 3 Gateway Firmware Signature Validation Bypass Vulnerability
ZDI-23-972
ZDI-CAN-20734
CVE ID
CVSS SCORE
AFFECTED VENDORS
AFFECTED PRODUCTS
VULNERABILITY DETAILS
ADDITIONAL DETAILS
CVE-2023-32156
9.0, (AV:A/AC:L/PR:L/UI:N/S:C/C:H/1:H/A:H)
Tesla
Model 3
This vulnerability allows network-adjacent attackers to execute arbitrary code on affected Tesla Model 3 vehicles. An attacker
must first obtain the ability to execute privileged code on the Tesla infotainment system in order to exploit this vulnerability.
The specific flaw exists within the handling of firmware updates. The issue results from improper error-handling during the
update process,
Fixed in 2023.12 firmware release.
69
```

## Slide 70

# Outline

**1** Analyzing Boot and Firmware Security **2** Hotwiring the Infotainment system **3** ExtracOng Secrets from the Tesla

70

## Slide 71

# What secrets are there on the Tesla?

CAR CREDENTIALS

USER DATA

- Authen'cates car against Tesla servers (Tesla’s car VPN)

   - Firmware updates

   - Car configura:on

   - Phones connected via Bluetooth

      - Contacts, calendar, call logs ...

   - Loca'ons visited

- Bound to Vehicle Iden'fica'on Number (VIN)

   - WiFi passwords

   - Spo'fy and Gmail session cookies

- Used to remotely (de-)authorize services

71

## Slide 72

# How are these secrets secured?

- Everything used to be cleartext

   - Car CredenHals on SD card, on storage

   - User data on cleartext storage parHHon

- Now there is TPM-based security

   - Car Creds sealed in TPM

   - User data parHHon encrypted, key sealed in TPM

72

19.06.23

## Slide 73

# What we extracted

- We wrote a paper on aYacking AMD’s fTPM

   - ExtracHng the TPM’s internal state

   - **_Unsealing arbitrary TPM objects_**

- We extracted the car credenOals à giving us access to Tesla’s server endpoints meant for cars

- We extracted the encrypted user parOOon’s disk encrypOon keys à we have access to user data

73

## Slide 74

# Where in the boot is the fTPM?

x86 ⏸ ▶ Opera:ng System
Key pls? 🔑
ROM Secure OS
Off-Chip
AMD SP ▶
Boot Loader Boot Loader µKernel fTPM App …
Non-vola(le storage
🔓
AMD Root  AMD SP
Off-Chip
SPI Flash x86 Firmware
Key Boot Loader Firmware
NVMe x86 OperaRng System 🔐 User Data

74

## Slide 75

# Where in the boot is the fTPM?

x86 ⏸ ▶ Opera:ng System
unseal 🔑
ROM Secure OS
Off-Chip
AMD SP
Boot Loader Boot Loader µKernel fTPM App …
Non-vola(le storage
🔓
AMD Root  AMD SP
Off-Chip
SPI Flash x86 Firmware NV Data
Key Boot Loader Firmware
Sealed
NVMe x86 OperaRng System 🔐 User Data
Disk Key

75

## Slide 76

# TPM Objects

- Public Part

   - Metadata

      - Which algorithm (AES, RSA, ECC, ...)

      - When and how can the object be used (policy)

   - Public key (if asymmetric algo.)

- Private Part

   - (Private) key

   - Auth value (for user input policy)

   - Seed value

   - Encrypted, integrity-protected

TPM Object

## **Public Part**

algorithm: RSA usage: sign=with pin en/decrypt=never copy=never

public key: c28e f334 c9...

## **Private Part**

private key: 3175 4088 06... auth value: hash(PIN 1, 2, 3, 4) seed value: adf9 8dd3 0e...

76

## Slide 77

Parent Object (loaded)
Public Part
🔓
Private Part
Seed value
TPM Object
KDF Public Part
🔒
🔑 Storage/Integrity Keys Private Part

# TPM Object Sealing

- Objects are sealed using a parent object

- TPM Spec. gives sealing algorithms

77

## Slide 78

# TPM Object Hierarchies

- TPM objects form a forest (mulOple trees)

- Roots: Primary objects • Derived from one of three primary seeds

- Need to walk hierarchy to unseal/load object

stored on TPM
*is there* persistently
Primary Seed
derives derives
derive
Primary
Primary derived
Object
Object
seals seals
load
TPM Object TPM Object
seals
seals
seals
TPM Object seals loaded
seals
TPM Object TPM Object TPM Object
TPM Object TPM Object TPM Object

unseal

78

## Slide 79

# The Non-VolaGle fTPM Data

- On SPI flash chip

   - Primary seeds, persistent counters, etc.

- Encrypted and integrity-protected

- We reverse-engineered the key derivaOon

- **Chip-unique secret** locked in CCP storage

   - Can only be used as AES key

- But we can extract intermediate value

ARK

79

## Slide 80

# Where in the boot is the fTPM?

leak
x86 ⏸ ▶
ROM Secure OS
Off-Chip
AMD SP Payload
🔑 Boot Loader Boot Loader µKernel fTPM App etc.
Non-vola(le storage
# #
AMD Root  AMD SP
Off-Chip
SPI Flash x86 Firmware NV Data 🔐
Key Boot Loader Firmware
NVMe x86 OperaRng System
Glitch

80

## Slide 81

How do we unseal a TPM Object?

Primary Seed
✅
derives derives❓
Primary
Primary
Object✅ Object
❓
(cache)
seals
seals✅
TPM Object TPM Object
✅
seals
seals
seals✅
TPM Object seals
seals
TPM Object TPM Object TPM Object
TPM Object TPM Object TPM Object
✅

- TPM objects are stored externally

- Sealing is defined in TPM spec.

- Primary objects: • Some are cached in NV data (see faulTPM)

   - Seeds should be in NV data

   - DerivaHon only loosely specified!

81

## Slide 82

# Primary Object DerivaGon

- Most fields come from the input “template”

   - Metadata, AuthorizaHon,  …

- Other fields are derived from a **determinis4c random bit generator (DRBG)**

   - Seeded with template and seed

   - **Algorithm not specified by spec.** à **reverse engineering**

Template

Primary Object
Public Part
algorithm: ECC
usage: …
public key: c28e f334 c9...

Public Part
algorithm: ECC
usage: …
public key: c28e f334 c9...
Private Part
private key: 3175 4088 06...
DRBG
auth value: …
seed value: adf9 8dd3 0e...
Primary Seed

82

## Slide 83

fTPM Unsealing AQack Recap
Primary Seed
✅
derives derives✅
Primary
Primary
NV Data
Object✅ Object
✅
NV Data🔐 (cache)
seals
seals✅
TPM Object TPM Object
✅
seals
seals
leak
seals✅
TPM Object seals
Payload seals
TPM Object TPM Object TPM Object
TPM Object TPM Object TPM Object
✅

83

## Slide 84

# Finding the Car CredenGals

TPM Object

84

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Finding the Car Credentials
x hnj@piepmatz: ~/Projects/psp/tesia/ftpm-offline Qe
+ x ftpm-offiine. 2
(venv) hnj@piepmatz:~/Projects/psp/tesla/ftpm-offline$ cat ../car_creds/car.key
----4BEGIN TSS2 PRIVATE KEY;----
=
H
——- END TSS2 PRIVATE KEY-----
(venv) hnj@piepmatz:~/Projects/psp/tesla/ftpm-offlines Jj
84
```

## Slide 85

# Unsealing the Car CredenGals

NV Data🔐

leak
TPM Object
Payload

85

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Unsealing the Car Credentials
x ‘hnj@piepmatz: ~/Projects/psp/tesia/ttpm-offline aes
+ x ‘fApm-offiine. 2
(venv) hnj@piepmatz:~/Projects/psp/tesla/ftpm-offline$ python3 unseal-tesla-car-creds.py from-image
../boot_nvme.bin $(xxd -p -c32 ../ftpm-seed.bin) ../car_creds/car.key >../car_creds/car.key.clear
j@piepmatz :~/Projects/php/tesla/ftpm-offline$ cat k/car_creds/car.key.clear
=---5 BEGIN PRIVATE KEY-----
YY
(venv) hnj@piepmatz :~/Projects/psp/tesla/ftpm-offlineS [J
85
```

## Slide 86

Finally: ExtracGng the Car CredenGals

Using the Car CredenGals

86

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
x hnj@piepmatz: ~/Projects/psp/tesla/ftpm-offline QqQn «a
+ * ftpm-offline co)
(venv) hnj@piepmatz:~/Projects/psp/tesla/ftpm-offline$ echo -e "GET /mothership/vehicles// HTTP/1.0\r\n"
| openssl s_client -connect api-prd.vn.tesla.services:443 -cert ../car_creds/car.crt -verify_quiet -quiet -ign_eof -nocomm
ands -key ../car_creds/car.key.clear
depth=@ CN = api-prd.vn.tesla.services, OU = Tesla Motors, O = Tesla, L = Palo Alto, ST = California, C = US
verify error :num=2@:unable to get local issuer certificate
depth=@ CN = api-prd.vn.tesla.services, OU = Tesla Motors, O = Tesla, L = Palo Alto, ST = California, C = US
verify error:num=21:unable to verify the first certificate
HTTP/1.1 200 OK
Date: Wed, 26 Jul 2023 = GMT
Content-Type: application/json; charset=utf-8
Connection: close
Cache-Control: no-cache
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block e .
X-Content-Type-Options: nosniff U Sl ng t al e Ca r Cred e nt a Is
X-Download-Options: noopen
X-Permitted-Cross-Domain-Policies: none
Referrer-Policy: strict-origin-when-cross-origin
X-TX1D:
Cache-Control: max-age=8, private, must-revalidate
X-Request-I¢d: DIT
X-Runtine: i
Strict-Transport-Security: max-age=31536000; includeSubDomains
Content-Security-Policy: default-sre ‘none’
{"id" : | Vin": ee" icknane" :" ee", last_seen" : EEE, “Created_at" :
,"current_version” :"develop/20623 .2¢. NN", "current_version_time" :null, "active" : true, "cell_number” :nul1, "countr
y":"US", "backseat_token" :null, "backseat_token_updated_at" :null, "radio_config" :null, “service_possession" :false, "hermes_capa
ble" :true, "factory_gated” :true, "delivered" :true, "model" :"3","use_country" :null, "service_state" :null, "connection_id" :nu1l, "
connection_region" :"aws:us-west-2", "birthplace" :"fremont-factory”, "do_not_disturb_until":null, “device_type":"vehicle", “is_
customer" :true, "state":"asleep", "odin_grablogs" : false, “type":"Vehicle"}
(venv) hnj@piepmatz:~/Projects/psp/tesla/ftpm-offlines |
86
```

## Slide 87

# ExtracGng the Disk EncrypGon Keys

|TPM Object|
|---|

87

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Extracting the Disk Encryption Keys
[root@fatbox3 ~]# cryptsetup -v LuksOpen --header /tmp/m3/var.luks /tmp/m3/var m
a|3-var --key-file /tmp/m3/var.key
No usable token is available.
iKey slot @ unlocked.
Command successful.
[rootefatbox3 ~]# cryptsetup -v LuksOpen --header /tmp/m3/home.luks /tmp/m3/home
x deploy @psp~deploy:—
+ x fipm-offing
bash-3.2# strings /dev/tle/home.luks | grep -m 1 sealed | jq
‘ “keyslots": {
narre(
sido ee m3-home --key-file /tmp/m3/home.key
"af": 4 : No usable token is available.
zi UAtcsamatidsaral Key slot ® unlocked.
Command successful.
[root@fatbox3 ~]# blkid /dev/mapper/m3-home
/dev/mapper/m3-home: LABEL="Home" UUID=""
OCK_SIZE="4096" TYPE="ext4"
[root@fatbox3 ~]# mount /dev/mapper/m3-home /mnt/home
[root@fatbox3 ~]# mount /dev/mapper/m3-var /mnt/var
[root@fatbox3 ~]# cat /mnt/var/vin
cat: /mnt/var/vin: No such file or directory
[root@fatbox3 ~]# cat /mnt/var/etc/vin
—
[root@fatbox3 ~]# sqlite3 /mnt/home/tesla/.Tesla/data/PhonebookV2.db "select «* f
rom vcards limit 15"
+ ftom-offiine
(venv) hnj@piepmatz:~/Projects/psp/tesla/ftpm-of fl
from-image ../boot_nvme.bin $(xxd -p -c32 ../ftpm-sed
7f66a65523e6ebde89bf667d8b779d4aa21d759F 597 F42eec4ed
74e895a061 £1651 f6a9d5cd187f8815996481adc
(venv) hnj@piepmatz:~/Projects/psp/tesla/ftpm-offli
"BL
be,
kd: {
"type": "pbkdf2",
“hash": "sha256",
“iterations”: 1000,
} "salt": “eE9dseA9GNZtgpbKyBOSDdUM20DymUZQvbdogDVNSNo="
}
},
"tokens": {
"gr: {
"type": "verypt",,
“keyslots”: [
20974|4| |ALice | MM m92 | 1111 {| | | a | | 5; 10
JAAUAAGACWAA\
WAC#+ACCj2Gb3QEb /AASTORLAV1Gi \nRu9j|
ZwfvQdWSLFYR7YkTmer \nefMdy jRaXp96HF
87
```

## Slide 88

# Outline

**1** Analyzing Boot and Firmware Security **2** Hotwiring the Infotainment system **3** ExtracOng Secrets from the Tesla

88

## Slide 89

# Summary

1. We reverse-engineered Tesla’s boot security

   - Tesla sets a good example of how it should be done

2. We sOll rooted the system through voltage glitching

   - This allows to acHvate some so3-locked features without paying

   - Not so3ware-patchable by anyone

3. We extracted hardware-bound secrets from the TPM using the same aYack

   - This can ease independent repairs

89

## Slide 90

# Key Takeaways

1. SoH-locking hardware features increases hacking incenOves

2. Using baYle-tested open-source soHware like Coreboot and Linux provides a good level of soHware security

3. But: Consider _hardware_ aYacks in your threat model, too

90

## Slide 91

# Responsible Disclosure(s)

- 2021: Informed AMD about voltage glitching suscepObility

- 2022: Shared faulTPM aYack with AMD (based on glitching)

- 2023: Informed Tesla about “AMD jailbreak”

   - Tesla was ‘relieved’ that a single glitch did not yield persistence

   - Did not comment the car_creds extracHon

91

## Slide 92

Jailbreaking an Electric Vehicle in 2023 WHAT IT MEANS TO HOTWIRE TESLA'S X86-BASED SEAT HEATER

Chris&an Werling Niclas Kühnapfel Hans Niklas Jacob Oleg Drokin

cwerling@sect.tu-berlin.de kuehnapfel@tu-berlin.de hnj@sect.tu-berlin.de

drokin@linuxhacker.ru

All code available at: **github.com/PSPReverse**
