---
title: "Booting into Breaches Hunting Windows SecureBoot's Remote Attack Surfaces"
speakers: ["Jietao Yang"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Jietao Yang_Booting into Breaches Hunting Windows SecureBoot's Remote Attack Surfaces.pdf"
pages: 86
sha256: "60585adc230a5781c19fd683888203a02faa5c8ced3d4f501d47e7fefe058324"
text_chars: 65231
ocr_pages: 41
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T22:57:24Z"
---
# Booting into Breaches Hunting Windows SecureBoot's Remote Attack Surfaces

**Speakers:** Jietao Yang  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Jietao Yang_Booting into Breaches Hunting Windows SecureBoot's Remote Attack Surfaces.pdf` (86 pages)


## Slide 1

Booting into Breaches Hunting Windows SecureBoot's Remote Attack Surfaces

Azure Yang @ CyberKunlun

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat
BRIEFINGS
AUGUST 6-7, 2025
MANDALAY BAY / LAS VEGAS
Booting into Breaches
Hunting Windows SecureBoot's Remote Attack Surfaces
Azure Yang @ CyberKunlun
```

## Slide 2

## About me

- Azure Yang @4zure9

**Security Researcher @ Cyber Kunlun | MSRC MVR(2022–2025)**

- Started journey into Windows security from late 2021

- Discovered **79 public CVEs** in Windows security, specializing in bootloaders, remote vulnerabilities. Ranked **#5 on MSRC’s 2024/2025 annual Windows Leaderboard** and **#2 in 2023Q4** for SecureBoot research.

- Retired CTF player, **DEF CON CTF Black Badge** owner.

- Blending offensive expertise into defensive evolution.

#BHUSA @BlackHatEvents

## Slide 3

## Agenda

- **Background**

- Attack surface in bootloader

   - Network protocol

   - BCD Registry

   - Security Policy

   - Filesystem

   - Logic flaw

- How to fuzz

- Attack surface beyond bootloader

- Future Work & Take Aways

#BHUSA @BlackHatEvents

## Slide 4

## Why Explore SecureBoot?

- Exploring unknown area is attractive for researcher

- The foundation of computer security starts with SecureBoot process

- SecureBoot vulnerabilities in Windows is rare in past decade.

#BHUSA @BlackHatEvents

## Slide 5

##### – SecureBoot The bigger picture

- Mobile – Hardware lockout implementation

- PC – UEFI

- Using digital signatures and certificates to establishing a chain of trust from hardware to OS

#BHUSA @BlackHatEvents

## Slide 6

## Mobile Secureboot

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
#) | SN _.. hw, | >a _
bieckhat Mobile Secuireboot f°
This phone is not running Samsung's official
software. You may have problems with features The boot loader is unlocked and software
or security,-and you woit't be able to install Integrity cannot be guaranteed. finy data
stored on the device may be available to
attackers. Do not store any sensitive data
on the device.
software updates.
Visit this link on another device:
g .co/ABH
SAMSUNG
Galaxy S10 5G
‘8 Secured by Knox
PRESS POWER KEY TO PAUSE BOOT
```

## Slide 7

### – SecureBoot Where is enforced

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
QQ j Sy jb é k , | 2 > _
blackhat SecureBootA Where is/enfofced
Windows Feature Secure Boot
Required?
Windows 11 Installation/Upgrade Yes (capable) Must be Secure Boot capable, recommended
to enable
BitLocker Device Encryption Strongly Protects boot chain integrity
recommended
Credential Guard Yes Depends on Secure Boot for trusted boot
Device Guard Yes Uses Secure Boot for code integrity
Early Launch Anti- Yes Ensures trusted anti-malware drivers load first
Malware (ELAM)
Measured Boot Relies on Secure Boot for integrity checks
Recall (Copilot+ PCs) Requires Secure Boot, BitLocker, and
Windows Hello
```

## Slide 8

###### What makes the SecureBoot

###### breaches

- Despite fixed in code and the updates has already been shipped, all my 32 Secure Boot Vulnerabilities findings still exploitable by default

- PCA2011 gets expired in 2026

- PCA2023

- UEFI var DBX 32K limit

- Compatibility issue

#BHUSA @BlackHatEvents

## Slide 9

## Previous research

###### **Golden Key’s unlock attack**

|`Fixed in CVE`|`Title`|`In wild`|Score
`CVSS`|
|---|---|---|---|
|`2016-Jul CVE-2016-3287`|`Secure Boot Security Feature Bypass Vulnerability`|`FALSE`|6.2 `CVSS:3.0/AV:P`|
|`2016-Aug CVE-2016-3320`|`Secure Boot Security Feature Bypass Vulnerability`|`FALSE`|6.6 `CVSS:3.0/AV:P`|
|`2016-Nov CVE-2016-7247`|`Secure Boot Component Security Feature Bypass Vulnerability`|`FALSE`|6.2 `CVSS:3.0/AV:P`|
|`2019-Sep CVE-2019-1294`|`Windows Secure Boot Security Feature Bypass Vulnerability`|`FALSE`|5.3 `CVSS:3.0/AV:P`|
|`2019-Oct CVE-2019-1368`|`Windows Secure Boot Security Feature Bypass Vulnerability`|`FALSE`|4.9 `CVSS:3.0/AV:P`|
|`2020-Feb CVE-2020-0689`|`Microsoft Secure Boot Security Feature Bypass Vulnerability`|`FALSE`|8.2 `CVSS:3.0/AV:L`|
|`2022-Jan CVE-2022-21894`|`Secure Boot Security Feature Bypass Vulnerability`|`FALSE`|4.4 `CVSS:3.1/AV:L`|
|`2023-May CVE-2023-24932`|`Secure Boot Security Feature Bypass Vulnerability`|`TRUE`|6.7 `CVSS:3.1/AV:L`|

Used by BlackLotus bootkit malware

- About Attack vector

   - (P)hysical

   - (L)ocal

   - (R)emote

   - (A)djacent

#BHUSA @BlackHatEvents

## Slide 10

## My findings

|There’s only|56 Secure Boot SFB from 2016-2025|
|---|---|
|`1 2024-Apr CVE-2024-20688`
`Secure Boot Security Feature Bypass Vulnerability`|7.1 `CVSS:3.1/AV:A/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H/E:U/RL:O/RC:C`|
|`2 2024-Apr CVE-2024-28896`
`Secure Boot Security Feature Bypass Vulnerability`|7.5 `CVSS:3.1/AV:A/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H/E:U/RL:O/RC:C`
|
|`3 2024-Apr CVE-2024-28898`
`Secure Boot Security Feature Bypass Vulnerability`|6.3 `CVSS:3.1/AV:A/AC:H/PR:H/UI:R/S:U/C:H/I:H/A:H/E:U/RL:O/RC:C`|
|`4 2024-Apr CVE-2024-20689`
`Secure Boot Security Feature Bypass Vulnerability`|7.1 `CVSS:3.1/AV:A/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H/E:U/RL:O/RC:C`|
|`5 2024-Apr CVE-2024-26171`
`Secure Boot Security Feature Bypass Vulnerability`|6.7 `CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H/E:U/RL:O/RC:C`|
|`6 2024-Apr CVE-2024-26175`
`Secure Boot Security Feature Bypass Vulnerability`|7.8 `CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H/E:U/RL:O/RC:C`|
|`7 2024-Apr CVE-2024-26180`
`Secure Boot Security Feature Bypass Vulnerability`|8 `CVSS:3.1/AV:A/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H/E:U/RL:O/RC:C`|
|`8 2024-Apr CVE-2024-26189`
`Secure Boot Security Feature Bypass Vulnerability`|8 `CVSS:3.1/AV:A/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H/E:U/RL:O/RC:C`|
|`9 2024-Apr CVE-2024-26240`
`Secure Boot Security Feature Bypass Vulnerability`|8 `CVSS:3.1/AV:A/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H/E:U/RL:O/RC:C`|
|`10 2024-Apr CVE-2024-28925`
`Secure Boot Security Feature Bypass Vulnerability`|8 `CVSS:3.1/AV:A/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H/E:U/RL:O/RC:C`|
|`11 2024-Apr CVE-2024-28897`
`Secure Boot Security Feature Bypass Vulnerability`|6.8 `CVSS:3.1/AV:A/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H/E:U/RL:O/RC:C`|
|`12 2024-Apr CVE-2024-29061`
`Secure Boot Security Feature Bypass Vulnerability`|7.8 `CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H/E:U/RL:O/RC:C`|
|`13 2024-Apr CVE-2024-29062`
`Secure Boot Security Feature Bypass Vulnerability`|7.1 `CVSS:3.1/AV:A/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H/E:U/RL:O/RC:C`|
|`14 2024-Apr CVE-2024-28923`
`Secure Boot Security Feature Bypass Vulnerability`|6.4 `CVSS:3.1/AV:L/AC:H/PR:H/UI:N/S:U/C:H/I:H/A:H/E:U/RL:O/RC:C`|
|`15 2024-Jul CVE-2024-28899`
`Secure Boot Security Feature Bypass Vulnerability`|8.8 `CVSS:3.1/AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H/E:U/RL:O/RC:C`|
|`16 2024-Jul CVE-2024-37969`
`Secure Boot Security Feature Bypass Vulnerability`|8 `CVSS:3.1/AV:A/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H/E:U/RL:O/RC:C`|
|`17 2024-Jul CVE-2024-37970`
`Secure Boot Security Feature Bypass Vulnerability`|8 `CVSS:3.1/AV:A/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H/E:U/RL:O/RC:C`|
|`18 2024-Jul CVE-2024-37974`
`Secure Boot Security Feature Bypass Vulnerability`|8 `CVSS:3.1/AV:A/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H/E:U/RL:O/RC:C`|
|`19 2024-Jul CVE-2024-37981`
`Secure Boot Security Feature Bypass Vulnerability`|8 `CVSS:3.1/AV:A/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H/E:U/RL:O/RC:C`|
|`20 2024-Jul CVE-2024-37986`
`Secure Boot Security Feature Bypass Vulnerability`|8 `CVSS:3.1/AV:A/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H/E:U/RL:O/RC:C`|
|`21 2024-Jul CVE-2024-37987`
`Secure Boot Security Feature Bypass Vulnerability`|8 `CVSS:3.1/AV:A/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H/E:U/RL:O/RC:C`|
|`22 2024-Jul CVE-2024-26184`
`Secure Boot Security Feature Bypass Vulnerability`|6.8 `CVSS:3.1/AV:A/AC:H/PR:L/UI:R/S:U/C:H/I:H/A:H/E:U/RL:O/RC:C`|
|`23 2024-Jul CVE-2024-37971`
`Secure Boot Security Feature Bypass Vulnerability`|8 `CVSS:3.1/AV:A/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H/E:U/RL:O/RC:C`|
|`24 2024-Jul CVE-2024-37972`
`Secure Boot Security Feature Bypass Vulnerability`|8 `CVSS:3.1/AV:A/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H/E:U/RL:O/RC:C`|
|`25 2024-Jul CVE-2024-37973`
`Secure Boot Security Feature Bypass Vulnerability`|8.8 `CVSS:3.1/AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H/E:U/RL:O/RC:C`|
|`26 2024-Jul CVE-2024-37975`
`Secure Boot Security Feature Bypass Vulnerability`|8 `CVSS:3.1/AV:A/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H/E:U/RL:O/RC:C`|
|`27 2024-Jul CVE-2024-37977`
`Secure Boot Security Feature Bypass Vulnerability`|8 `CVSS:3.1/AV:A/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H/E:U/RL:O/RC:C`|
|`28 2024-Jul CVE-2024-37978`
`Secure Boot Security Feature Bypass Vulnerability`|8 `CVSS:3.1/AV:A/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H/E:U/RL:O/RC:C`|
|`29 2024-Jul CVE-2024-37988`
`Secure Boot Security Feature Bypass Vulnerability`|8 `CVSS:3.1/AV:A/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H/E:U/RL:O/RC:C`|
|`30 2024-Jul CVE-2024-37989`
`Secure Boot Security Feature Bypass Vulnerability`|~~#BHUSA BlkHtEt~~
8 `CVSS:3.1/AV:A/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H/E:U/RL:O/RC:C`|
|`31 2024-Jul CVE-2024-38010`
`Secure Boot Security Feature Bypass Vulnerability`|~~@acavens~~
8 `CVSS:3.1/AV:A/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H/E:U/RL:O/RC:C`|
|`32 2024-Jul CVE-2024-38011`
`Secure Boot Security Feature Bypass Vulnerability`|8 `CVSS:3.1/AV:A/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H/E:U/RL:O/RC:C`|

## Slide 11

##### Reflections on Research Impact

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
be
2)
BRIEFINGS
if
Mi
blackhat Reflections ow Research Amp:
€ CG 23 zerodayinitiative.com/blog/2024/7/9/the-july-2024-security-update-review ae G iG o> tee
ZERO DAY
INITIATIVE
There are also two dozen fixes for security feature bypass (SFB) bugs, although | think we
need to rename a component. Between 23 fixes in April and 20 more this month, | don't
think we can really call it Secure Boot anymore. Even worse, all but two of these could be
exploited by an Adjacent attacker with LAN access to the target. Oof. I'm calling this feature
“Protected Boot” rather than “Secure Boot”. The SFB bug in BitLocker requires physical
access, but BitLocker is specifically designed to prevent this sort of attack, so...er...not good.
11
```

## Slide 12

## How AV:A possible?

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
blackhat How AV:A_péssible? /
OS Deployer PXE server
—EE Ports used - 69 and 4011
Client Computer Router
DHCP Server
12
```

## Slide 13

###### Define Secure boot SFB in Windows

- Before secure boot, Microsoft doesn’t acknowledge vulnerabilities in bootloader.

- With Secure Boot, bootloader issue can get a CVE

- Secure Boot is a security feature of Windows

- Vulnerabilities in Secure Boot are security feature bypass

   - It can be remote

   - It can be without user interaction

   - It can be preauth

   - It can be Remote Code Execution/Information Leak

   - It can’t be Denial of Service

#BHUSA @BlackHatEvents

## Slide 14

## Impact

- Most of PC with UEFI Secure boot enabled

   - Linux

   - Windows

- B(ring) Y(our) O(wn) B(ootloader)

   - Can be from adjacent network

- Can be preauth

- Exploitable by default in many scenario

- Exploitable until PCA2011 expire or added to DBX

#BHUSA @BlackHatEvents

## Slide 15

## Summary of my research **ID Attack Surface method CVE**

|**Attack Surface**
**1Networkprotocol**
|**Compomnet**
**PXE Bootloader**
|**method**
**Audit**
|**CVE**
**CVE-2024-20688**
|**Type**
**Stack OOB W**
|
|---|---|---|---|---|
|**2Networkprotocol**|**PXE Bootloader**|**Audit**|**CVE-2024-20689**|**Stack OOB W**|
|**3Networkprotocol**|**PXE Bootloader**|**Audit**|**-**|**DoS**|
|**4Networkprotocol**|**PXE Bootloader**|**Audit**|**CVE-2024-28925**|**Recursive Calling**|
|**5Networkprotocol**|**PXE Bootloader**|**Audit**|**CVE-2024-26180**|**Recursive Calling**|
|**6BCD Element Processing**|**Bootloader**|**fuzzing**|**CVE-2024-26175**|**Heap OOB W**|
|**7BCD Element Processing**|**Bootloader**|**fuzzing**|**CVE-2024-37971**|**Recursive Calling**|
|**8BCD Element Processing**|**Bootloader**|**fuzzing**|**CVE-2024-37970**|**Heap OOB W**|
|**9BCD Registry structer**|**Bootloader**|**fuzzing**|**CVE-2024-37972**|**Heap OOB W**|
|**10BCD Element Processing**|**Bootloader**|**fuzzing**|**CVE-2024-28896**|**Stack OOB W**|
|**11BCD Element Processing**|**Bootloader**|**Audit & fuzzing**|**CVE-2024-28897**|**Arbitrary Memory W**|
|**12BCD Element Processing**|**Bootloader**|**fuzzing**|**CVE-2024-28923**|**Heap OOB W**|
|**13BCD Element Processing**|**Bootloader**|**Audit & fuzzing**|**CVE-2024-37973**|**Recursive Calling**|
|**14BCD Element Processing**|**Bootloader**|**Audit & fuzzing**|**CVE-2024-29061**|**Stack OOB W**|
|**15BCD Element Processing**|**Bootloader**|**Audit**|**CVE-2024-37969**|**Info leak**|
|**16BCD Element Processing**|**Bootloader**|**Audit**|**CVE-2024-37974**|**Heap OOB W**|
|**17BCD Element Processing**|**Bootloader**|**Audit**|**?**|**Recursive Calling**|
|**18BCD Element Processing**|**Bootloader**|**Audit**|**CVE-2024-26171**|**Heap OOB W**|
|**19BCD Element Processing**|**Bootloader**|**Audit**|**CVE-2024-37970**|**Heap OOB W**|
|**20Networkprotocol**|**Bootloader**|**Audit**|**CVE-2024-37975**|**Integer Overflow**|
|**21BCD Element Processing**|**Bootloader**|**Audit**|**?**|**Arbitrary Memory W**|
|**22BCD Element Processing**|**Bootloader**|**Audit**|**CVE-2024-37978**|**Heap OOB W**|
|**23BCD Element Processing**|**Bootloader**|**Audit**|**CVE-2024-26240**|**Calling Stack**|
|**24BCD Element Processing**|**Bootloader**|**Audit**|**CVE-2024-37981**|**Heap OOB W**|
|**25BCD Element Processing**|**Bootloader**|**Audit**|**CVE-2024-26189**|**Recursive Calling**|
|**26Security Policy**|**Bootloader**|**Audit**|**-**|**Logical**|
|**27BCD Element Processing**|**Bootloader**|**Audit**|**CVE-2024-28897**|**Heap OOB W**|
|**28BCD Element Processing**|**Bootloader**|**Audit**|**CVE-2024-26175**|**Heap OOB W**|
|**29BCD Element Processing**|**Bootloader**|**Audit**|**CVE-2024-26175**|**Heap OOB W**|
|**30BCD Element Processing**|**Bootloader**|**Audit**|**CVE-2024-26175**|**Heap OOB W**|
|**31BCD Element Processing**|**Bootloader**|**Audit**|**CVE-2024-28898**|**Recursive Calling**|
|**32BCD Element Processing**|**Bootloader**|**Audit**|**CVE-2024-37986**|**Heap OOB W**|
|**33Architecture issue**|**Bootloader**|**Audit**|**-**|**Logical**|
|**34WIM filesystem**|**Bootloader**|**fuzzing**|**CVE-2024-37987**|**Invalid Pointer Deref**|
|**35WIM filesystem**|**Bootloader**|**Audit**|**CVE-2024-37988**|**Heap OOB W**|
|**36WIM filesystem**|**Bootloader**|**Audit**|**CVE-2024-37989**|**Arbitrary Memory W**|
|**37WIM filesystem**|**Bootloader**|**Audit**|**CVE-2024-38010**|**Heap OOB W**|
|**38WIM filesystem**|**Bootloader**|**fuzzing**|**-**|**DoS**|
|**39WIM filesystem**|**Bootloader**|**fuzzing**|**-**|**DoS**|
|**40NTFS filesystem**|**Bootloader**|**fuzzing**|**-**|**DoS**|
|**41NTFS filesystem**|**Bootloader**|**fuzzing**|**?**|**Recursive Calling**|
|**42WIM filesystem**|**Bootloader**|**Audit**|**?**|**Arbitrary Memory W**|
|**43NTFS filesystem**|**Bootloader**|**fuzzing**|**-**|**DoS**|
|**44NTFS filesystem**|**Bootloader**|**fuzzing**|**-**|**DoS**|
|**45NTFS filesystem**|**Bootloader**|**fuzzing**|**CVE-2024-38011**|**Heap OOB W**|
|**46NTFS filesystem**|**Bootloader**|**fuzzing**|**CVE-2024-28899**|**Recursive Calling**|
|**47NTFS filesystem**|**Bootloader**|**fuzzing**|**-**|**DoS**|
|**48FAT filesystem**|**Bootloader**|**fuzzing**|**-**|**DoS**|
|
**49FAT filesystem**|**Bootloader**|**fuzzing**|**-**|**DoS**|
|**50Architecture issue**|**Bootloader**|**Audit**|**CVE-2024-29062**|**Logical**|
|**51Driver Config**|**Kernel**|**fuzzing**|**-**|**Heap OOB W**|
|**52Sdb Parsing**|**Kernel**|
**fuzzing**|
**-**|
**DoS**|
|**53Driver Config**|**Kernel**|~~#BHUSA~~
**Audit**|~~@BlackHatE~~
**-**|~~ents~~
**Heap OOB W**|
|**54Driver Config**|**Kernel**|**Audit**|**-**|**DoS**|
|**55Driver Config**|**Kernel**|**Audit**|**-**|**Recursive Calling**|

**ID**

- 55 unique reports

- Duplicate cases are already removed

- All reported cases can be carried by **unauthenticated attacker from network** ~~.~~

- By finding method

   - Audit: 35

   - Fuzzing: 20

- By attack surface

   - BCD Registry: 25

   - Filesystem: 16

   - Network protocol: 6

   - Windows Kernel: 5

## Slide 16

###### My way to reduce duplication report

- On the developer view

   - Find a bug

   - Write a fuzzer to make it discoverable through fuzzing

   - Conduct hot patching on vulnerability

   - Find out if there are still any related crashes caused by the same rootcause.

   - Repeat

#BHUSA @BlackHatEvents

## Slide 17

###### About the heap memory management

- No pageheap

- OOB write can happened silently without crash the bootloader

- The MmHapReportHeapCorruption itself has self recursive calling issue

- Allocate 0x20 at least, OOB write to block offset less than 0x20 is not a real vulnerability can be exploit, block is 0x20 aligned.

#BHUSA @BlackHatEvents

## Slide 18

## Agenda

- Background

- **Attack surface in bootloader**

   - Network protocol

   - BCD Registry

   - Security Policy

   - Filesystem

   - Logic flaw

- How to fuzz

- Attack surface beyond bootloader

- Future Work & Take Aways

#BHUSA @BlackHatEvents

## Slide 19

## Network protocol

- IPv4 DHCP PXE

- IPv6 DHCPv6 PXE

- HTTP

• WDS Multicast

WDS Multicast TFTP

UDP Device

HTTP 1

TFTP Redirect

Uri Device

BCD Registry parsing

bootmgfw.efi

Firmware UefiPxeBcDxe

IPv4/v6

wdsmgfw.efi 4 Bugs

#BHUSA @BlackHatEvents

## Slide 20

## IPv4 PXE

#BHUSA @BlackHatEvents

Preboot Execution Environment (PXE) Specification – Version 2.1

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat |
BRIEFINGS
DHCP Discover to port 67
“ 4 DHCP Discover to Port 67
Contains “PXEClient” extension
oN DHCP Contains "PXEClient” extension tags. DHCP
| DHCP Offer to port 68 ———_| Service Service
Conta eee | "ocr Offer to port 68 contains: ——_|
jent IP addr :
[Other DHCP option tags] +
Client IP addr +
PXE Opt 60 "PXEClient"
DHCP Request to port 67 —_|
DHCP
DHCP Ack to port68. =} Service
DHCP
DHCP Request to Installation Server port 67—_ Service
DHCP Server
Contains [Other DHCP option tags]
DHCP Discover to port 67
Contains “PXEClient” extension
DHCP Offer to port 68 ~————__|
Client IP addr set to 0.0.0.0
—__
DHCP Ack reply to Port 68
Lo ems to Port 4011 ———“
Proxy
DHCP
.——— DHCP Request to port 4011
Contains “PXEClient” extension | Contains "PXEClient” extension tags Service
oo _ |
DHCP Ack reply to port client's port Extended DHCP Offer to client port contains:
Contains “PXECItent” extension tags + ——————] PXE client extension ta s
BStrap.0 file | ___ 9 Proxy DHCP
| ————____ strap.o download request to TFTP Server
port 69 or MTFTP port assigned in __-_-_—+ }—__ Boot Service Discovery
DHCP Ack w/ BStrap.0 file.
_ Contains "PXEClient" extension tags
BStrap.0 download to client's port + [Other DHCP option tags]
: Proxy DHCP ——_~__| B.
——————___—— oot
PH Server . Service
Boot Service Discover to port 67 or 4011 Client Boot Service Ack reply to Client's Port
Contains: “PXEClient” extension tags + . 5 1.
[Other DHCP option tags] Contains: PXE Client extension tags
——+—_] Boot Execute + NBP file name
Boot Service Ack reply to port 68 or client's port Service
--—. Contains: “PXEClient” extension tags + ——, Downloaded
NBP file name Boot Image NBP Download
> Request to TFTP port 68———_|
2.00 00
NBP Download request to TFTP port 69 or PXE
Popp te RS
MITFTP
MTFTP port assigned in Boot en Service Client --——___ _
--—__ . NBP Download to
PXE Client NBP Download to client's port Boot Server PXE Client Client's port Boot Server
Figure 2-4 PXE Client Response to DHCP Server Supplying Boot Service Discovery Code Figure 2-3 PXE Client Response to DHCP Server Containing a Proxy DHCP Service
Preboot Execution Environment (PXE) Specification — Version 2.1 20
```

## Slide 21

## IPv6 PXE

Unified Extensible Firmware Interface Specification – Version 2.3

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
IPv6 PXE_/
OOOQOE
DHCP6 Solicit to 547
| yoni “PXEClient’ ext tags -_]
DHCP6 Advertise to 546
Contains [Other DHCP6 option tags
+ client address
—Eh
DHCP6 Request to 547—___ |
DHCP6 Reply to 546 | 4
DHCPE6 Solicit to 547
DHCP6
Service
DHCP6
Service
Contains “PXEClient’ ext tags
|
DHCP6 Advertise to 546
Contains “PXEClient’ ext tags
DHCP6 Request to 4011
Contains “PXEClient’ ext tags
DHCP6 Reply to client port
Contains “PXEClient’ ext tags —iH
+ BootFileURL(Boot Server address)
Boot Service Request to 4011
Proxy
DHCP6
Service
Contains “PXEClient’ ext tags
+ [Other DHCP6 option tagg
-——__ DHCP6 Reply to client port
Contains “PXEClient’ ext tags
+ BootFileURL(Boot Server address __ FF
and NBP file name)
+ BootFilePara (NBP file size)
TFTP ReadFile to 69 to request NBP file
——— et
NBP file download to client pore—— Ey]
Figure 59. IPv6-based PXE boot (DHCP6 and ProxyDHCP6 reside on the different server)
Unified Extensible Firmware Interface Specification — Version 2.3
Boot
Service
DHCPE6 Solicit to 547
Ea Contains “PXEClient” ext tags——__ |
DHCP6 Advertise to 546 2 |
Contains[Other DHCP6 options tags}
+ “PXEClient’ + client address
DHCP6 Request to 547
I; nai [Other DHCP6 option tagg-———___}
DHCP6 Reply to 546 ZH
|
DHCP6 Request to 4011
He Contains “PXEClient’ ext tags~_]
DHCP6 Reply to client port
Contains “PXEClient” ext tags —H
+ BootFile URL{Boot Server address)
|__—_——
DHCP6
Service
A=)
FE)
DHCP6
Service
Boot Service Request to 4011
7 Contains “PXEClient” ext tags
+ [Other DHCP6 option tagg —_
Boot Service Reply to client port
Contains “PXEClient” ext tags
| + BootFileURL(Boot Server address
and NBP file name) —H
+ BootFilePara (NBP file size)
TFTP ReadFile to 69 to request NBP file
a nH
NBP file download to client po
Boot
Service
©
91
Zr
Figure 58. netboot6 (DHCP6 and ProxyDHCP6 reside on the same server)
```

## Slide 22

## Research environment

- Hyper-V Gen2 VM is recommended

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
* be y a y | 4
blackhat Research_envirohnment
° Hyper-V Gen2 VM Is recommended
~~ Microsoft
Hyper-V
22
```

## Slide 23

###### - Hyper V Gen 2 VM Default Boot Settings

**Support IPv6 boot in firmware, Use powershell to enable IPv6 PXE booting.**

**Set-VMFirmware boottest -PreferredNetworkBootProtocol IPv6**

#BHUSA @BlackHatEvents

## Slide 24

## - Why choose Hyper V

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat
ve
78
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
98
91
92
93
94
95
96
97
98
ack hat Why
Paneer eat \very — &o
v5 = v4->__vftable->TriageDump64: : Initialize __MEMORY_DUMP_PARAMETERS__ PTR(
v4,
(GuestCrashDumpWriter *)((char *)this + 56));
if ( v5 >= @ )
{
LODWORD(v18) = 3;
v19 = 0164;
v9 = (const WCHAR *)((char *)this + 8);
v1@ = (const unsigned __int16 *)((char *)this + 8);
if ( *((_QWORD *)this + 4) >= 8uié4 )
v1@ = *(const unsigned __int16 **)v9;
Vm1::VmFile::VmFile((Vml::VmFile *)&v19, v1, v8, *((_DWORD *)this + 11));
LODWORD(v18) = 4;
v5 = va-> _vFtable prriageDunpéd: :Write_Vml: :VMFile(v4, &v19);// Generate Dump, | ?Write@TriageDump64@@UEAAJAEAVVmF ile@Vm1@@@Z
Vm1: :VmFile: :Reset = =
if ( v5 >=@ )
{
v4->__vftable->TriageDump64: :GetBugcheckCode_uint(v4, (unsigned int *)&v18);
v2@ = (struct _EVENT_DESCRIPTOR)MSVM_GUEST_CRASH_DUMP_SUCCESS;
Vm1::VmFile: :Reset(&v19, v13);
v5 = 8;
}
else
{
LODWORD(v18) = v5;
if ( *((_QWORD *)this + 4) >= 8ui64 )
v9 = *(const WCHAR **)v9;
DeleteFileW(v9);
Vm1: :VmFile: :Reset(&v19, v12);
24
000A6275 ?7InitiateDump@GuestCrashDumpWriter@@QEAAJI@Z:40 (1400A6275)
```

## Slide 25

## - Why choose Hyper V

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat
BRIEFINGS
*
*
*
2)
Why choose“Hyper-V
FO GR RRR RK
Bugcheck Analysis
le
BUGCHECK_CODE:
*
* BUGCHECK_P1: ffffffffceeeeees
RR RRR RRR RRR RRR RR RRR RR RRR RR RR ER ERE KR RR RRR RRR RRR RRR RR RR RR ER ERE RE RE RR EKER ERE
KMODE_EXCEPTION_NOT_HANDLED (1e)
This is a very common BugCheck.
the driver/function that caused the problem.
Usually the exception address pinpoints
Always note this address
BUGCHECK_P2: 3e915383
BUGCHECK_P3: 6
as well as the link date of the driver/image that contains this address.
Arguments:
Argi: fffffffFc9eee8es ,
Arg2: 006000063e915383,
Arg3: eeeeeeeeeeeeeeen,
Arg4: 9e9e9eeee46eece8,
bootmgfw!WimpSearchForDirent+@x63:
@e008880 36915383 Ofb74364
kd> kf
# Memory
ee
@1 40
@2 100
@3 ae
@4 ae
@5 ae
@6 168
e7 78
e8 78
e9 1be
Ga 1008
Child-sP
08000000 646eebbe
00000000 O46eebfO
@0e00000 e46eec FO
@e0e0880 e46eed90
00000000 846ecece30
00000000 646eeed0
@0000008 846efO30
ee0e0880 e46efead
00000000 646ef110
00000008 846ef2c0
00000008 846eF3cO
BUGCHECK_P4: 46eeceé
The exception code that was not handled
The address that the exception occurred at
Parameter @ of the exception
Parameter 1 of the exception
FILE_IN_CAB: Memory.dmp
EXCEPTION_PARAMETER1: e99@e99ee00e080
movzx  eax,word ptr [rbx+64h] ds:0030:41414141° 414141a5=? ???
RetAddr Call Site EXCEPTION_PARAMETER2: 9@000000046ce
00008000 3e91461c bootmgfw!WimpSearchForDirent+0x63
00008000 3e90F36a bootmgfw! WimOpen+@x74 READ ADDRESS: eeeeeeeee46eeces
00000000 3e90F32c bootmgfw! FileIoOpen+0x24e a
00000800 3e90F32c bootmgfw! FileIoOpen+0x210
ee098800 3e99ee14 bootmgfw! FileIoOpen+0x210
@e008000 3e90da21 bootmgfw! BlpFileOpen+e0xe8
@e000000 3ea6e84F bootmgfw! B1FileOpen+0x71
00000800 3e9e903e bootmgfw! SbeEnumerateFilesInDirectory+0x5f
00008000 3e8a2214 bootmgfw! BlImgLoadBootApplication+0x21e
ee000000 3e8a30de bootmgfw! BmTransferExecution+0x84 25
00000008 3e8a1c46
bootmgfw! BmpLaunchBootEntry+@x25c
```

## Slide 26

## VMware ESXi

## Firmware

Support IPv6 boot in firmware and can be configured in UEFI console.

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blackhat VMware ESXrFikmwadre // ,
Boot Manager
Boot normal ly Device Path:
Pc iRoot (0x0) /Pci (x16, 0x . .
EFI Netuork Winona! §SUoport IPv6 boot in firmware and can be
zr 5698947C 0x0) /TPub (0000: . .
EFI Virtual disk (0.0) Tim! §$COnfigured in UEFI console.
EFI UMware Virtual SATA CDROM Drive (0.0) 70000 :0000 ,Ox0 , Static ,00 ;
PRE HTITPu6 00-0000 0000 :0000:0000:0 |, DpeDxe are OxE ee
PRE HTTP v4 000:0000:0000 0x40, 0000: | > mnpoxe File DXE driver
0000 : 0000 : 0000 : 0000 : 9000 i appe i OnE er
Enter setup :0000 : 0000) > Udp4Dxe File DXE driver
Reset the susten ae 7 aoe
Shut down the susten > UefiPxeBcDxe File DXE driver
> Ip6Dxe File DXE driver
> Udp6Dxe File DXE driver
>» Dhcp6Dxe File DXE driver
» Mtftp6Dxe File DXE driver
> TcpDxe File DXE driver
>» DnsDxe File DXE driver
>» HttpDxe File DXE driver
>» HttpBootDxe File DXE driver
+ HttpUtilitiesDxe i driver
Tl=Move Highlight <Enter>=Select Entry
```

## Slide 27

## Case study

- CVE-2024-20688-PXE Bootloader BmpParseDhcpv6Packet ServerIdentifier stack out of bound write

- CVE-2024-20689-PXE Bootloader BmpParseDhcpv6Packet ClientIdentifier stack out of bound write

#BHUSA @BlackHatEvents

## Slide 28

## Case study

#BHUSA @BlackHatEvents

Register controlled by remote attacker.

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bldekhat
BRIEFINGS
y
Case s tudy/
/}
yf
Une. 7
!!!! X64 Exception Type - OD(#GP - General Protection)
ExceptionData - 90900000000000000
RIP
RAX
RBX
RSI
R8
Ril
R14
DS
GS
CRO
CR4
DRO
DRS
GDTR
IDTR
4141414141414141,
geq00e0eco0ee24o,
9eo0000000000013,
4242424242424242,
geq00e00e0000000,
GOGG0OG03FE36CAO,
9eo00o00e0000000,
0e00000000000030,
0000000000000030,
0000000080010033,
60600000000000668,
6000000000000000,
geo00o00e0000000,
OGGG0GG03F5DC000 06000000000000047,
OOOOOGOO3EE5E918 OOOOOOOD000000FFF,
FXSAVE_STATE - 800000003FE37170
cs
RCX
RSP
RDI
R9
Ri2
R15
i)
55
CR2
CR8
DR1
DRG
6000000000000038,
9eq00e0eco0ed24o,
OG0000003FE37510,
4242424242424242
geq0eeo0e0000000,
6000000000000000,
90900000000000000
9e00000000000030,
0600000000000030
4141414141414141,
60000060000000000
6000000000000000,
OOOOOOOOFFFFOFFO,
LDTR -
TR -
CPU Apic ID - 90000000 !!!!
RFLAGS - 9060000000000202
RDX - 0000000010133828
RBP - 000000003FE375D0
R10 - 9000000010161170
R13 - 9600000000000000
FS - §000000000000030
CR3 - 900000003F801000
DR2 - 9800000000000000
DRY - 0000000000000400
00e0000000000000
H000000000000000
Register controlled by remote attacker.
```

## Slide 29

## BCD Registry

- Registry Hive file

- Can be edit by regedit and API

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
blackhat BCD Registry .. “
° Registry Hive file
° Can be edit by regedit and API
w PXREBCD Edit Binary Value x
Description Value name:
vi i Objects | Element
i {4636856e-540f-4170-a130-al4776f4c6544 teed ERE
{68d9e51c-a129-4ee1-9725-2ab00a95 fda} aooeenee [a5 D4 2D cD FE 7D 8A 43 G-fb}.c a
{9dea862c-Scedd-4e70-accl-f32b344d4795} Seen eR KE
{ed2dd485-7dfe-438a-bb26-e8e3cOc8809d} eeeeee18 8688 Oe HG ee ee
: eoeeee2@ = 3 —“‘(‘CTCTCCtCwCstC.
i {esf4eicl -c/b4-4416-9bea-dfofosd 744c at PEBRRB28 ae ae ae ae ae ae ae SB ave ee we
i Description eoe0ee3@ «8860 ww
i eoeeee38 86 la (‘NCTC ln
w Elements eoeeee4a = SiS tC‘ CCC.
; eoseee4s «= iii LH.
11000001 eoeeeesa = a (i ww ll
| 2000004 AAR ARAS A Aaa AA Aaa AA Aaa AA Aaa AA v
21000001 Cancel
22000002
26000010
26000022
29
```

## Slide 30

## - - - Case study CVE 2024 37972

• Bootloader CmpRemoveCellFromIndex Heap out of bound write

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
FA
wily yw >=.
‘CVE-2024-37972
* Bootloader CmpRemoveCellFromindex Heap out of bound write
bisek hat
BRIEFINGS
Case study
3; // rie
t; // ax
3 // r8
3 // rdx
3 // rex
3 // dx
v2 = CellIndex;
result = CellPaged->word@ -
f ( (result & @xFDFF) !=@ )
.
L
v4 = CellPaged->Cellcount - 1;
CellPaged->Cellcount = v4;
if ( !v4 )
; result;
[v5 = 4 * (v4 - ( ] t64)CellIndex); > v5
v6 = &CellPaged|CelliIndex + 2];
v7 = &CellPaged[v2 + 1];
{
v8 = CellPaged->CellCount - 1;
CellPaged->CellCount = v8;
if ( !v8 )
t result;
v5 = * (v8 - v2
v6 = &CellPaged[2
v7 = &CellPaged[
)
* (unsigned int)(v2 + 1) + 1
* v2 + 1];
t16)memmove(v7, v6, v5);
```

## Slide 31

## Say hello to bcdedit

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pis hat
BRIEFINGS Say h he
BCDEDIT - Boot Configuration Data Store Editor
The Bcdedit.exe command-line tool modifies the boot configuration data store.
The boot configuration data store contains boot configuration parameters and
controls how the operating system is booted. These parameters were previously
in the Boot.ini file (in BIOS-based operating systems) or in the nonvolatile
RAM entries (in Extensible Firmware Interface-based operating systems). You can
use Bcdedit.exe to add, delete, edit, and append entries in the boot
configuration data store.
For detailed command and option information, type bcdedit.exe /? <command>. For
example, to display detailed information about the /createstore command, type:
bcdedit.exe /? /createstore
For an alphabetical list of topics in this help file, run "bcdedit /? TOPICS".
Commands that operate on a store
/store Used to specify a BCD store other than the current system default
/createstore Creates a new and empty boot configuration data store.
/export Exports the contents of the system store to a file. This file
can be used later to restore the state of the system store.
/import Restores the state of the system store using a backup file
created with the /export command.
/sysstore Sets the system store device (only affects EFI systems, does
not persist across reboots, and is only used in cases where
the system store device is ambiguous).
Commands that operate on entries in a store
/copy
Makes copies of eee in aT store.
/create Creates new entries in the store.
/delete Deletes entries from the store.
/mirror Creates mirror of entries in the store.
Run bededit /? ID for information about identifiers used by these commands.
/deletevalue
/set
Deletes entry options from the store.
Sets entry option values in the store.
Run bcededit /? TYPES for a list of datatypes used by these commands.
Run bcdedit /? FORMATS for a list of valid data formats.
Commands that control output
Lists entries in the store.
Command-Line option that displays entry identifiers in full,
rather than using names for well-known identifiers.
Use /v by itself as a command to display entry identifiers
in full for the ACTIVE type.
Running "bcdedit" by itself is equivalent to running "bcdedit /enum ACTIVE".
* Commands that control the boot manager
/bootsequence Sets the one-time boot sequence for the boot manager.
/default Sets the default entry that the boot manager will use.
/displayorder Sets the order in which the boot manager displays the
multiboot menu.
/timeout Sets the boot manager time-out value.
/toolsdisplayorder Sets the order in which the boot manager displays
the tools menu.
Commands that control Emergency Management Services for a boot application
/bootems Enables or disables Emergency Management Services
for a boot application.
/ems Enables or disables Emergency Management Services for an
operating system entry.
/emssettinas Sets the oqlobal Emergency Management Services parameters.
```

## Slide 32

## BCD element meaning

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blackhat BCD element mean
G www.geoffchappell.com
Geoff Chappell, Software Analyst
Not indeed look to be complete, given its stated caveats, for Windows 8.
lotes
Dos
Expression Web
Front Page
Independent Hardware Vendors
Independent Software Vendors
Global Elements
The following apply to all object types.
Office Library Elements
& Security
Web Before Windows 10, all the elements that can be in all types of object are Library
Windows elements.
& Startup
Windows Vista and High . ; ;
mdows View and Hgner Constant Symbolic Names Friendly Name Format or Value Versions
Boot Configuration Data
© BCD Objects
fa] BCD Elements) BedLibraryDevice_ApplicationDevice ,
The Advanced Boot Options Menu «11000001 BCDE_LIBRARY_TYPE_APPLICATION_DEVICE Cia device 6.0 and higher
& The Edit Boot Options Menu
The Boot Status Data Log BedLibraryString_ApplicationPath
15 Older Windows Versions 012000002 Be Te eT ATION. PATH path string 6.0 and higher
31 Kernel - a a
@ Licensing
| Internet Information Services (IIS) BedLibraryString_Description
B inten 0x12000004 BODE LIBRARY TYPE, DESCRIPTION description string 6.0 and higher
@ Internet Explorer
aj Help BedLibraryString_PreferredLocale
1 Debugging 0x12000005 sR CDE_LIBRARY_TYPE_PREFERRED_LOCALE locale string 6.0 and higher
3) Retro-Computing
Archive
BcdLibraryObjectList_InheritedObjects a
0x14000008 BeDE LIGRADY TYEE, INHERIT inherit GUID list 6.0 and higher
BedLibraryinteger_TruncatePhysicalMemory . ;
0x18000007 BOE LIBRARY TYPE, TRUNCATE. PHYSIGAL_MEMORY truncatememory integer 6.0 and higher
BedLibraryObjectList_RecoverySequence ;
0x14000008 Bee LIBRARY TYPE RECOVERY. SEQUENCE recoverysequence GUID list 6.0 and higher
BcdLibraryBoolean_AutoRecoveryEnabled ,
0x16000009 BeDE LIBRARY. TYPE AUTO. RECOVERY_ENABLED recoveryenabled boolean 6.0 and higher
BcdLibraryIntegerList_BadMemoryList - 7 a
Ox17000008 Bee LIBRARY. TYPE BAD MEMORY LIST badmemorylist integer list 6.0 and higher
oxteo00008 —- BedLibraryBoolean_AllowBadMemoryAccess badmemoryaccess boolean 32.. higher
BCDE_LIBRARY_TYPE_ALLOW_BAD_MEMORY_ACCESS
```

## Slide 33

###### Understand BOOT_ENVIRONMENT_DEVICE

- REG_BINARY

- Valid when unpacking from REG_BINARY format.

- Size gets checked

- Content in it is not checked

#BHUSA @BlackHatEvents

## Slide 34

## BCD Element processing

- BL_DEVICE_TYPE

   - DiskDevice = 0x0

   - LegacyPartitionDevice = 0x2

   - SerialDevice = 0x3

   - UdpDevice = 0x4

   - BootDevice = 0x5

   - PartitionDevice = 0x6

   - VmbusDevice = 0x7

   - LocateDevice = 0x8

   - UriDevice = 0x9

   - CompositeDevice = 0xA

   - CimfsDevice = 0xB

#BHUSA @BlackHatEvents

## Slide 35

### A tale of an unsafe function

##### **BiSanitizeRamdiskDevicesInDe vice**

|CVE|Attack Surface
Finding method|Report title
|
|---|---|---|
|CVE-2024-28896|BCD Element Processing fuzzing|Bootloader BiSanitizeRamdiskDevicesInDevice RamDiskDevice stack OOB Write preauth RCE|
|CVE-2024-28897|BCD Element Processing Audit|Bootloader BiSanitizeRamdiskDevicesInDevice LocateDevice invalid ParentOffset arbitrary memory write preauth RCE|
|CVE-2024-29061|BCD Element Processing Audit|Bootloader BiSanitizeRamdiskDevicesInDevice FileDevice stack OOB Write preauth RCE|
|CVE-2024-26175|BCD Element Processing Audit|Bootloader BiSanitizeRamdiskDevicesInDevice CimfsDevice Heap OOB write preauth RCE|
|CVE-2024-26175|BCD Element Processing Audit|Bootloader BiSanitizeRamdiskDevicesInDevice RamDiskDevice Heap OOB write preauth RCE|
|CVE-2024-26175|BCD Element Processing Audit|Bootloader BiSanitizeRamdiskDevicesInDevice CompositeDevice Heap OOB write preauth RCE|

#BHUSA @BlackHatEvents

## Slide 36

A design level change to fix(?) them all

Define design level change:

Before: BiSanitizeRamdiskDevicesInDevice After: BlDeviceSanitizeRamdiskDevicesInDevice

#BHUSA @BlackHatEvents

## Slide 37

###### A design level change to fix(?) them all

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blackhat A design level change\to fix(?) thén-all
" CimfsDevice Heap OOB write
Release Date: 09/04/2024
on: OS Builds 22621.3447 and 22631.3447
kd> ImUynbootmgtw
Bro’ full module list
start end nodule name
ooo00000° 10000000 oo000000° 10160000 bootngfw C (pdb symbols) C:\Program Files\Windows Kits\10\Debuggers™:
Loaded symbol image file: bootmgfw.efi
Mapped memory image file: C:\Program Files\Windows Kits\10\Debuggers\x64\sym\bootmgtw. ef i\C5D5959B1e0000\bootng
Image path: bootmgfw.efi
Image name: bootmgfw.efi
Browse all global symbols functions dat
Image was built with /“Brepro flag.
av
Timestamp 00000000 (This is a reproducible build file hash. not 4 timestamp)
CheckSum ooooo000 —— sntantaieintaiatinanar ‘
ImageSize 001E0000 =
File version 10.0.22621.3447 Product Version: 10. 0. 32621 3447
Product version 10.0.22621.3447
File flags 0 (Mask 3F) FileVersion : 10. 0.22621 .3447 ||
File 0S 40004 NT Win32
File type 1.04 DO BO
File date oo000000. 00000000
Translations: 0409.04b0
Information from resource tables:
CompanyName: Microsoft Corporation
Product Name Microsoft® Windows® Operating _Sy¥Sstem
InternalName: bootngr. exe
Oe 5 ti na De ame eet mcr ere
Product Version: 10.0.22621.3447
FileVersion: 10.0.22621.3447) (WinBuild.160101.0800)
PITepescriperen. Leer tansger
LegalCopyright : © Microsoft Corporation. All rights reserved
kd> r= gee: I
=0000000000000000 rbx-00000000008:
7ae-00000000008%af20 res-00000000000 | |LOOtMgE w! MnHapReportHeapCorrupt ion+0x37 :
rip=00000000100c24ab rsp=00000000046e
r8=0000000000000000 r3=O00000000000C go000000" 100c24ab cc int
r11=00000000046e23d8 r12=00000000000GuUUU rils=uUUDUUUUUUUUUUUU
r14=0000000000838610 r1S=0000000000000068
iopl=0 nv up ei pl nz na pe nc
cs=0028 ss=0009 do=0030 ec=0N30 fa=0030  gs=0030 ef1=00000202
bootngfw! MnHapReportHeapCorruption+0x3?7:
00000000°100c24ab cco int 3 37
ROS" RT
# Memory Child—-SP RetAddr Call Site
oo 00000000° 046e23e0 00000000°0083af20 bootmgfw! MmHapReportHeapCorruption+0x37
```

## Slide 38

## When bcdedit cry

- CVE-2024-28898

   - Recursive calling when enumerate the GUID element

   - contained by the first 16 bytes GUID in the device element

#BHUSA @BlackHatEvents

## Slide 39

### About Recursive calling

- Stack memory layout

RSP

Gap?
RSP

Hyper-V firmware

#BHUSA @BlackHatEvents

edk2/ESXi firmware

## Slide 40

### About Recursive calling

• Stack memory layout Gap? RSP edk2/ESXi firmware Hyper-V firmware

RSP

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q 1 R sere //; bp \ 5 A
blackhat About ecuySive'ealli ig
BRIEFINGS
Vi
s Oxfecf8b1: mov DWORD PTR [r13+0x0] ,r12d
sBUXTECTODS. Cate "UXTECT IU ”
Oxfecf8ba: mov eax ,r12d
Oxfecf8bd: add rsp, 0x20
Oxfecf8cl: pop ri2
T direction overflow)
0000 | —— > (0x00000000)
0004 | ——> (0x00000000)
0008 | SSE HSE (0x00000000)
0012] —=> (0x00000000 )
0016| --> Oxfe223818
0020 | ——> (0x00000000)
0024 | ==> --—> ==> (O0x00000000)
== 9028 | --> (0x90000000)
2310-2 Legend: ; , rodata, value
23-10-27 Stopped reason:
e23-10-2 in 27? Q
info reg r13
Ire s: Oxfe223818 Oxfe223818
x/10gx Oxfe223818 PROT 64-bit fluff=0000
Cannot access memory at address Oxfe223818' dor cu tit farfooee
```

## Slide 41

## When bcdedit cry

- CVE-2024-28898

   - Recursive calling when enumerate the GUID element

   - contained by the first 16 bytes GUID in the device element

#BHUSA @BlackHatEvents

## Slide 42

## When bcdedit cry

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
HKEY hiveKey;
| a ee
blackhat When bcedeg@i
LONG result + RegLoadKey(HKEY_USERS, "BCD123", hiveFilePath.c_str());
if (result != ERROR SUCCESS) {
std::cout << "Failed to load the registry hive. Error code: " << result << std::ene
getchar();
return 1;
GUID guid = stringToGuid("{@0000000-9000-9000-9000-a0aa0eG0@000}");
int cc = atoi(argv[2]);
for (int i=@;i<cc;++i)
{
printf("i: %d\n", i);
BODCreateElement(HKEY_USERS, guid, i);
puts("set dome");
?
f/f Unload the registry hive
result 4 RegUnLoadKkey(HKEY_USERS, "BCD123");
if (result != ERROR SUCCESS) {
std::cout << "Failed to unload the registry hive. Error code: " << result
return 1;
4< Std: ce
std::cout << "Registry hive loaded, key value set, and hive unloaded successfully." <<
X ~~:
void BCDCreateElement(HKEY hRootKey, GUID NodeGUID, int i)
{
HKEY hElementRoot;
HKEY hElementElements;
HKEY hElementElementsSubE lement;
HKEY hElementDescription;
/ Format BCD123\\Objects\\{%s}\\
memset(datal, 9, @x100);
NodeGUID.Datal = i;
sprintf((char*)&data1, "BCD123\\Objects\\%s", guidToString(&NodeGUID) );
puts((char *)datal);
RegCreateKeyA(hRootKey, (LPCSTR)datal, &hElementRoot);
lements\\11000001
sprintf((char*)&data1, "BCD123\\Objects\\%s\\Elements", guidToString(&NodeGUID) );
RegCreateKeyA(hRootKey, (LPCSTR)datal, &hElementElements);
sprintf ((char*)&datal, “BCD123\\Objects\\%s\\Description", guidToString(&NodeGUID) );
RegCreateKeyA(hRootKey, (LPCSTR)datal, &hElementDescription);
sprintf((char*)&data1, “BCD123\\Objects\\%s\\Elements\\%x", guidToString(&NodeGUID) ,0x11000001);
/ Create the sub element REG_BINARY
RegCreateKeyA(hRootKey, (LPCSTR)datal, &hElementElementsSubElement) ;
datal1[@x110] = @x5;
data1[0x114] = 1;
data1[@x118] = @xCc;
pa DUORD = idat alto looL sais).
RegSetValueEx(hElementElementsSubElement, "Element", @, REG_BINARY, &data1[@x100], @x1C);
RegCloseKey(hElementElementsSubElement) ;
RegCloseKey(hElementDescription) ;
RegCloseKey(hElementElements) ; 42
RegCloseKey(hElementRoot) ;
```

## Slide 43

## HTTP Protocol

- Can be set by BCD element

- Not vulnerable when use firmware HTTP function

- Vulnerability exists when using firmware TCP and a hand-made HTTP parser in the bootloader.

#BHUSA @BlackHatEvents

## Slide 44

## - - - Case study CVE 2024 37975

• Bootloader HttppGetResponseTcp Integer overflow preauth RCE

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
VA yf
blacichat Case study CVE-2024-3 975
* Bootloader HttopGetResponselcp Integer overflow preauth RCE
oe v1l9 = httpTcp4_recvdata.DataLength - 3;
° tT ( httplcp4 recvdata.
oa 10+ ARE 40;
a LODWORD(v19) = RtlCompareMemory ( ( =
o f v19 7 -
tC vi9 1 v19 = httpTcp4 recvdata. pa - 3;
1
e *(( T )Heap + v18) =
oO DataLength = httpTcp4_ recvdata. i
eo vi6 = ( )Heap + v18 + 4;
o vi5 = ( t ] )Heap;
oO v17 = httpTcp4 recvdata.DataLength - v18 - 4;
na
a DataLength = httpTcp4 recvdata.DataLength;
* ++v18;
8 vi9 = DataLength - 3;
or) ile ( v18 < ( : / t)vi9 );
° if ( !vi5 )
£
L
00194A82 HttppGetResponseT cp:68 (10195682)
```

## Slide 45

## Security Policy

- Golden Key’s unlock attack

   - CVE-2016-3287 / CVE-2016-3320

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
blackhat Security Policy ©
BRIEFINGS
* Golden Key’s unlock attack
* CVE-2016-3287 / CVE-2016-3320
Must be an admin and have physical access to exploit the bug
— Private Key was not leaked
Mi icrosoft U E Fl Secu rity U pd ates — This isSHle has no impact on Encryption or Bitlocker
And what it is
— For RT we had a debug policy to unlock individual devices for development
— The mechanism for debug policies was changed to simplify debug policies
UEFI US Fall Plugfest _ September 20 - 22] 2016 — Adesign issue allowed the new policies to unlock old devices/OS versions
Presented by Microsoft -
— KR and later is secure, only down level operating systems are vulnerable
Scott Anderson, Suhas Manangi, Nate Nunez, Jeremiah Cox, Michael Anderson
— {Must be an admin and have physical access to exploit the bug
45
UEFI Plugfest - September 2016 www.uefi.org 1 UEFI Plugfest — September 2016 www.uefi.org 4
```

## Slide 46

## Security Policy

- Case 83787

   - Logic, by design, can be attack carried by unauthenticated attacker in network

   - • Ability to put everyone uses PXE boot at risk

   - It only works in theory; this is one of only two cases among my submissions where I cannot bypass secure boot when I submitted.

#BHUSA @BlackHatEvents

## Slide 47

#### The real security feature bypass

• CVE-2024-29062
BmFwVerifySelfIntegrity SFB
• Exist because bootloader fetch
bootmgfw.efi for verification
from the bootdevice.
#BHUSA @BlackHatEvents
CVE-2021-40045 – By taszk

## Slide 48

#BHUSA @BlackHatEvents BlackHat USA 2024 - Locked Down but Not Out / Fighting the Hidden War in Your Bootloader - Bill Demirkapi@MSRC

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Windows Boot Code: Extensibility
¢ Another major threat for boot code is extensibility.
- For example, did you know some variants of boot manager support
10+ unique filesystems?
PFILESYSTEM_TABLE FsTable[] = {
+ Why do we expose this by default? NetRegisterFunctionTable,
CompositeFsRegisterFunctionTable,
VmbfsRegisterFunctionTable,
CimFSRegisterFunctionTable,
NtfsRegisterFunctionTable,
EfiFsRegisterFunctionTable,
FatRegisterFunctionTable,
RefsRegisterFunctionTable,
FppRegisterFunctionTable,
WimRegisterFunctionTable,
UdfsRegisterFunctionTable,
EtfsRegisterFunctionTable,
NULL
BlackHat USA 2024 - Locked Down but Not Out / Fighting the Hidden War in Your Bootloader - Bill Demirkapi@MSRC
```

## Slide 49

### Bad Fixup

|CVE|method|Titile|
|---|---|---|
|CVE-2024|-37987 fuzzing|FixupDirEntry wStream invalid 64bit pointer|
|CVE-2024|-37988 audit|WimpFixupRoot invalid WIM SecurityBlock size check heap OOB write|
|CVE-2024|-37989 audit|WimpFixupRoot lack of Directory attribute check arbitrary memory write|
|CVE-2024|-38010 audit|FixupDirEntry Directory File NextEntry invalid check heap OOB write|
||-fuzzing|WimpRead invalid chunk error deadloop preauth DoS|
||-fuzzing|WimpReadResource div zero preauth DoS|
||?audit|WimpFixupRoot lack of flags check arbitrary memory write|

#BHUSA @BlackHatEvents

## Slide 50

### Fuzzing infra

- AFLplusplus

   - NYX mode

- AFL++ - Free mutator

- NYX – Fast snapshot

- Intel PT – Code Coverage

#BHUSA @BlackHatEvents

## Slide 51

–
Harness

## My approach

- Patch bootmgfw.efi

- Patch image integrity check

##### **Trampoline seg**

- Add sections

   - Harness shellcode written by C++

###### **Metadata segment**

- Metadata contains control data

- Bitmap is coverage

- Payload used to receive mutate input

###### **Bitmap segment**

- Modify target function call to trampoline

**Payload segment**

#BHUSA @BlackHatEvents

## Slide 52

## Tips to fuzz filesystem

- Filesystem itself is a code coverage amplifier

   - fuzzing use code basic block bitmap to collect coverage

   - To reach same logic in code, all roads can lead you to Rome

- Fuzzing approach

- Reversing

- Understanding

- Fuzzing

- Conduct hot patching on vulnerability

- Repeat

- Result: 16 reports in 5 days, 5 by audit, 11 by fuzzing

#BHUSA @BlackHatEvents

## Slide 53

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat
BRIEFINGS
american fuzzy lop ++4.09a {0} (./nyx_mode/efi/ntfs) [fast] ~ Nyx
[— process timing
overall result:
Ss
run time : 23 days, 3 hrs, 30 min, 31 sec cycles done : 477
last new find : @ days, 10 hrs, 47 min, 19 sec corpus count : 956
last saved crash : 13 days, 3 hrs, 20 min, 50 sec saved crashes : 4
last saved hang : 3 days, 10 hrs, 6 min, @ sec saved hangs : 20
/ cycle progress ——————————— map coverag:
now processing : 682.419 (71.3%) map density : 2.2U% / 3.38%
runs timed out : @ (0.00%) count coverage : 3.17 bits/tuple
+ stage progress ———_——_________- findings in depth
now trying : splice 9 favored items : 171 (17.89%)
stage execs : 40/86 (46.51%) new edges on : 235 (24.58%)
total execs : 234M total crashes : 15 (4 saved)
exec speed : 153.6/sec total tmouts : 523 (@ saved)
+ fuzzing strategy yields item geometry
bit flips : disabled (default, enable with -D) levels : 14
byte flips : disabled (default, enable with -D) pending : ©
arithmetics : disabled (default, enable with -D) pend fav : 0
known ints : disabled (default, enable with -D) own finds : 416
dictionary : n/a imported : 538
havoc/splice : 239/81.6M, 181/152M stability : 100.00%
py/custom/rq : unused, unused, unused, unused
trim/eff : disabled, disabled [cpuoee: 16%]
L. strategy: exploit ————— state: in progress J
american fuzzy lop ++4.09a {9} (./nyx_mode/efi/ntfs) [fast] — Nyx
[- process timing
run time : 23 days, 3 hrs, 28 min, 46 sec
last new find : @ days, 18 hrs, 49 min, 15 sec
last saved crash : 13 days, 12 hrs, 36 min, 26 sec
last saved hang : © days, 20 hrs, 19 min, 7 sec
overall results
cycles done : 402
corpus count : 1291
saved crashes : 3
saved hangs : 55
cycle progress map coverag
| now processing : 1160.131 (89.9%) map density : 1.91% / 3.38%
runs timed out : @ (0.00%) count coverage : 3.80 bits/tuple
stage progress ————————|_ findings in depth
now trying : splice 8 favored items : 158 (12.24%)
stage execs : 16/172 (9.30%) new edges on : 234 (18.13%)
total execs : 148M total crashes : 4 (3 saved)
exec speed : 210.6/sec total tmouts : 572 (@ saved)
fuzzing strategy yields item geometry
| bit flips : disabled (default, enable with -D) levels : 34
| byte flips : disabled (default, enable with -D) pending : ©
| arithmetics : disabled (default, enable with -D) pend fav : ®
| known ints : disabled (default, enable with -D) own finds : 1289
| dictionary : n/a imported : ®
havoc/splice : 806/52.4M, 486/96.5M stability : 100.00%
py/custom/rq : unused, unused, unused, unused
L trim/eff : disabled, disabled [cpu0o1: 8%]
strategy: exploit —————— state: in progress —|
american fuzzy lop +#4.09a {0} (./nyx_mode/efi/ntfs) [fast] - Nyx
[— process timing
overall result:
s
run time : 23 days, 3 hrs, 28 min, 6 sec cycles done : 358
last new find : © days, 12 hrs, 29 min, 9 sec corpus count : 1139
last saved crash : 20 days, 19 hrs, 16 min, 26 sec |saved crashes : 2
last saved hang : 1 days, 16 hrs, 5 min, 37 sec saved hangs : 82
L cycle progress ———————_ map coverag
now processing : 1072.75 (94.1%) map density : 2.25% / 3.38%
runs timed out : © (0.00%) count coverage : 3.43 bits/tuple
+ stage progress | findings in depth
now trying : splice 12 favored items : 159 (13.96%)
stage execs : 6/14 (42.86%) new edges on : 232 (20.37%)
total execs : 125M total crashes : 13 (2 saved)
exec speed : 2.53/sec (zzzz...) total tmouts : 1738 (@ saved)
+ fuzzing strategy yields item geometry
bit flips : disabled (default, enable with -D) levels : 24
byte flips : disabled (default, enable with -D) pending : 0
arithmetics : disabled (default, enable with -D) pend fav : ©
known ints : disabled (default, enable with -D) | own finds : 1137
dictionary : n/a imported : @
havoc/splice : 723/44.2M, 416/81.4M stability : 100.00%
py/custom/rq : unused, unused, unused, d
trim/eff : disabled, disabled [cpuoe3: 9%]
\ strategy: exploit —-————— state: in progress —
american fuzzy lop ++4.09a {0} (./nyx_mode/efi/ntfs) [fast] - Nyx
[— process timing
overall results
run time : 23 days, 3 hrs, 28 min, 8 sec cycles done : 420
last new find : @ days, 9 hrs, 31 min, 4 sec corpus count : 1100
last saved crash : 12 days, 4 hrs, 5 min, 7 sec saved crashes : 4
last saved hang : 2 days, 21 hrs, 9 min, 20 sec saved hangs : 18
-- cycle progress map coverag
| now processing : 407.331 (37.0%) map density : 2.30% / 3.37%
runs timed out : © (0.00%) count coverage : 3.39 bits/tuple
| stage progress | findings in depth
now trying : splice 11 favored items : 167 (15.18%)
stage execs : 81/129 (62.79%) new edges on : 230 (20.91%)
total execs : 130M total crashes : 10 (4 saved)
exec speed : 155.2/sec total tmouts : 286 (@ saved)
| fuzzing strategy yields item geometry
| bit flips : disabled (default, enable with -D) levels : 27
| byte flips : disabled (default, enable with -D) pending : ©
| arithmetics : disabled (default, enable with -D) pend fav : ©
| known ints : disabled (default, enable with -D) own finds : 1098
| dictionary : n/a imported : @
havoc/splice : 684/45.7M, 418/84.4M stability : 100.00%
py/custom/rq : unused, unused, unused, unused
trim/eff : disabled, disabled [cpu0o2: 9%]
\ strategy: exploit —-—————- state: in progress —
53
```

## Slide 54

# Harvest

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
bisexhat Harvest»
5000
4500
4000
3500
3000 _/
2500
1600
1400
1200
1000
800
600
400
200
rr edges
5000 10000 15000 20000 20 — FA
relative time in seconds 0
5000 10000 15000
corpus count relative time in seconds
current item
pending items
pending favs
cycles done
A
10000 15000
\/ ea4 1 || ee jd
5000 10000 15000 20000 relative time in seconds
relative time in seconds
20000
unig crashes
uniq hangs
levels
execs/sec -
54
```

## Slide 55

## Go speed racer

Making VM snapshot tree really helps you accelerate the analysis

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
bieckhat Go speed_racer \
GO) u22dsk_edk2dev - ROZESESE
» Q@-+ @— @— @- @- @- 9 @- O-- @
: works server ipv+ debug ‘2824 bootmofw PRE 6 ‘BRE 7 patched debug 21 me
— 0 O—- @@- OOOO
wMext vNext restarted bootmofw ‘8219 python wim debug poison
wdsstage bootmafw load heapoob
Q
newloop
@
debug
vhdrarndisk
Q—@
DRE 27 release
RRB 26
Sari
Making VM snapshot tree really helps you accelerate the analysis 95
```

## Slide 56

###### Exploiting the vulnerability without infoleak

- Why do I need an infoleak to exploit the vulnerabilities?

   - Because there’s ASLR on bootmgfw.efi

#BHUSA @BlackHatEvents

## Slide 57

###### Exploiting the vulnerability without infoleak

• What if I can bypass ASLR as if it does not exist from the start?

#BHUSA @BlackHatEvents

## Slide 58

Unauthenticated Attacker Security boot chains remains intact and complete from network

Firmware bootloader verification

Microsoft signed Bootloader

UEFI PXE Microsoft signed Bootloader Protocol BCD Element Processing Filesystem vulnerabilities vulnerabilities vulnerabilities Memory corruption

Remote code execution

Security feature bypass

#BHUSA @BlackHatEvents

## Slide 59

## Agenda

- Background

- Attack surface in bootloader

   - Network protocol

   - BCD Registry

   - Security Policy

   - Filesystem

   - Logic flaw

- **Attack surface beyond bootloader**

- Future Work & Take Aways

#BHUSA @BlackHatEvents

## Slide 60

## One more thing

###### Bootloader

• I have just taken my first step into secure boot research.

• The PXE architecture problem exposes countless Windows kernel and userland service code to unauthenticated remote attackers, Windows Kernel potentially ushering in a new era of unauthenticated RCE attacks on Windows.

Windows Services

#BHUSA @BlackHatEvents

## Slide 61

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Unauthenticated Attacker im
from network od
Windows Kernel
Remote code execution
tiserand
Application
61
```

## Slide 62

Up-to date
OS Binary

Default
Configuration

Up-to date
OS Binary

Attacker compromised
Configuration

#BHUSA @BlackHatEvents

## Slide 63

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Unauthenticated Attacker im
from network od
Windows Kernel
Remote code execution
tiserand
Application
63
```

## Slide 64

## Your PC is under risk

#BHUSA @BlackHatEvents

## Slide 65

# How to make this attack

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
File Action View Help
@9/|4n| S| &
fa Windows Deployment Services WIN-POM7B6RSUD3
v Ga Servers
=, WIN-POM7B6RSUD3
mw Active Directory Prestaged Devices H
Windows Deployment Services is not configured
&4 Windows Deployment Services Configuration Wizard
Before You Begin
You can use this wizard to configure Windows Deployment Services. Once the server is
configured, you will need to add at least one boot image and one install image to the server
before you will be able to install an operating system.
Before you begin. ensure that the following requirements are met:
The server is a member of an Active Directory Domain Services (AD DS) domain, or
a domain controller for an AD DS domain. If the server supports Standalone mode, it
can be configured without having a dependency on Active Directory.
There is an active DHCP server on the network. This is because Windows
Deployment Services uses Pre-Boot Execution Environment (PE), which relies on
DHCP for IP addressing.
There is an active DNS server on your network.
This server has an NTFS file system partition on which to store images.
To continue, click Next.
Bac { Next >
Cancel
fa Add Image Wizard »
Image File cH |
Enter the location of the Windows image file that contains the images to add.
File location:
| Browse...
Note: The default boot and install images (Boot.wim and Install .wim) are located on the
installation D'VD in the \Sources folder.
More information about images and image types
Next 65) Cancel |
```

## Slide 66

## Introduce a handful tool

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
blackhat Introduce_anandful ¢
BRIEFINGS
1.1002.1 UEFI Firmware - oOo
File Recovery Options Help
indows 11 ZEMMhR x64 Windows 11 Pro x64 Windows Server 2022 Datacenter x64 Windows PE 10.0.26244.5000 ARM64
c:\Temp\mounts\win11_22h2 C:\Temp\mounts\win2022 C:\Temp\mounts\Boot
Local Disk Mounted Image Mounted Image Mounted Image
Ready Ready Ready Ready
About Dism++ x
Dism++x64 10.1.1002.1 UEFI
Firmware
CbsHost: 10.1.1002.1
NCleaner: 10.1.1001.10
WimGAPI: 10.0.22621.3672
OK
Open session
66
```

## Slide 67

## Introduce a handful tool

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
blackhat Introduce_qfandful tool
Mount Image-Max
Name Value
Image Name ___ Microsoft Windows Setup (arm64)
Image Descri... Microsoft Windows Setup (arm64)
Edition 2
Architecture ARM64
Created 2024/6/22 16:05:24
Expanded Sp... 1.51 GB
OS Version 10.0.26244.5000
Target Image: 2: Microsoft Windows Setup (arm64)(Bootable)
C:\Temp\images\boot.wim
:\Temp\mounts\Boot!
Browse
Browse
67
```

## Slide 68

## Replace the setup.exe

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blackhat Replace the‘setup.exe /,
+
IHRBAM «86> «=A (C:) +> Temp
@ W ‘N HRY 06 = OBB
(EA RB
B& Program Files 2024/6/22 15:54
B® Program Files (x86) 2024/6/22 15:54
Bl sources 2024/6/22 16:00
BB Windows 2024/6/22 16:04
al FAP JOVAICINIALC-CA
Boot Images 1 Boot Image(s)
n& setup
Image Name Architecture Status Expanded Size fersi Priority
EJ Microsoft Windows S.. xb4 Online 2295 MB 9/11... .0. 500000 ...
68
```

## Slide 69

## Just wait for fish to bite

#BHUSA @BlackHatEvents

## Slide 70

If you don’t want to wait

- You might exploit a remote DoS to force the victim to reboot

Physical Attack SecureBoot

Remote Attack SecureBoot

Local Attack SecureBoot

Remote DoS Based Attack SecureBoot

#BHUSA @BlackHatEvents

## Slide 71

#BHUSA @BlackHatEvents BlackHat USA 2024 - Locked Down but Not Out / Fighting the Hidden War in Your Bootloader - Bill Demirkapi@MSRC

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Where Does Microsoft Draw the Line?
Can an attacker achieve the same outcome by design?
Defensible? Defensible?
Admin User —— eavronmen Meet —— enanint
ya Considered defensible a a Usually defensible
: Defensible? i Defensible?
Attacker Environment Npoot| PT (User-mode
as? Usually defensible ) Not defensible!
BlackHat USA 2024 - Locked Down but Not Out / Fighting the Hidden War in Your Bootloader - Bill Demirkapi@MSRC
```

## Slide 72

###### Data shared between bootloader and kernel

###### • \WINDOWS\inf\errata.inf

NT Kernel

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blackhay Data shared betwéen.boetloadet and, fernel
\WINDOWS\inf\errata.inf
if ( OslGetErrataFileNameFromRegistry(a4, &DestinationString) )
£
L
a2->Butfer[v7] = 95
a2->Length = Length;
if ( BlAppendUnicodeToString(a2, L"inf
1
if ( OslIsTcbLaunchEnabled() )
vl3 = BlLdrPreloadFile(a3, a2->Buffer);
") && BlAppendUnicodeToString(a2, DestinationString.Buffer) )
vil3 = BlimgLoadImageWithProgress2(
&a1->BasicData.Extension->EmInfFileImage,
&al->BasicData.Extension->EmInfFileSize,
aoe NT Kernel
Local Types
ned int Size;
_PROFILE PARAMETER BLOCK Profile;
20000014
oid *EmInfFileImage;
i int EmInfFileSize;
```

## Slide 73

## What’s the file looks like

- Attacker controlled

- Standard INF file

- Parsing in Kernel

- No common API

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
VA yf
blackhat What’s the,fi le looks Jike/ _
= erratainf X
= errata.inf
Be Attacker controlled
Standard INF file
s evaraciwe Parsing in Kernel
>
3;Abstract: No common API
& INF file for the Errata Manager Database
;Copyright (c) Microsoft Corporation. All rights reserved.
;Module Name:
ae |
;Specify the rules that the clients can register for notifications
3;Also need to specify the necessary string parameters if required
3N.B. The rule names must have been defined in the [RuleNameGuidDef] Section
o Declared in [RuleDef] Section and implemented in [Rule] Section
pessssssssscss sess
[TargetRuleDef ]
ACPISLPWorkAround = {FACP.ACER_OEMID.FACP.M25D_TableId}, \ 3; ACERM25D02/25/¢e0
{FACP.COMPAQ_OEMID.FACP.LAREDO_TableId}, \ ; COMPAQLAREDO@7/05/99
{FACP.DELL_OEMID.FACP.WS21@ TABLEID}, \ ;DellPrecisionWS21e
{FACP.DELL_OEMID.FACP.WS41@ TABLEID}, \ ;Del1lPrecisionWS410e
{FACP.DELL_OEMID.FACP.WS61@_ TABLEID}, \ ;DellPrecisionWS61e
{FACP.DELL OEMID.FACP.PE130@ TABLEID}, \ :DellPowerEdge130e0
```

## Slide 74

Standing on the shoulders of giants

Start fuzzing harness code from opensource code base

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
BRIEFINGS
G hook.cpp M G kdvm.cpp 4 X
VirtualKD-Redux > Lib > kdvmguestlib > G+ kdvm.cpp > ¢ ChannelHelper<DefaultRPCChannel>
static NTSTATUS KdDebuggerInitialize@(PVOID lpLoaderParameterBlock )
r
au
#ifdef VKD_EXPERIMENTAL_PACKET_POLL_DIVIDER_SUPPORT
#endif
//PVOID hMod = Kerne loduleB ("ntoskrnl.exe") ;
PVOID hMod = GetModuleBaseAddress(&lofCallDriver) ;
setup((size_t)hMod) ;
return STATUS_INVALID_ PARAMETER;
Start fuzzing harness code from opensource code base
=
75
```

## Slide 75

How to setup fuzzing infra

• Step.2 Store the fuzzing file

• pass in errata.inf to C:\Temp

- Install the fuzzing kdcom by clicking VirtualKD-redux Install

• Reboot the machine and press F8, to complete the snapshot capture

#BHUSA @BlackHatEvents

## Slide 76

## Analyzing the crash

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
id_000000,sig_00,src_000419,time_306686,execs_34066,op_havoc,rep_2
fl: kd> .trap Oxfffff8
NOTE: The trap frame
Some register values
rax=0000000000000000
rdx=fffF9c0e1F960600
rip=ffffF80235986c69
r8=fFfFfF9c0e1F99a150
ri1=ffff9c0e1Ff9Ia9 Fad
7r14=0000000000000000
iopl=0 nv up
nt! EmpParseRules+0x27
FFFFF802°>35986c69 483
1: kd> kf
xxx Stack trace for
# Memory Child-SP
00 FffFF886
01 70 fffFfF886
02 40 fffff886
03 240 Fffff886
04 1a0 fffff886
05 40 fffff886
06 50 ffffFf886
864ca06F50
does not contain all
registers.
may be zeroed or incorrect.
rbx=0000000000000000
rsi=0000000000000000
rsp=fffff8864ca070e0
r9=0000000000000002
r12=0000000000000000
r15=0000000000000000
Pox=FFTTFFFFFTTTTTTS
rdi=0000000000000000
rbp=0000000000000101
r10=0000000000000543
r13=0000000000000000
4
Analyzing the-crash
ei pl nz na pe nc
5:
919 cmp qword ptr [rcex],rbx ds: ffffffff FFFFFFF8=? 222222222722 2?2??
last set context - .thread/.cxr resets it
RetAddr Call Site
“4ca070e0 FfFfFF802 35985F77 nt! EmpParseRules+0x275
“4ca07150 ffFfFF802 359cec43 nt! EmpParseInfDatabase+0x97
*4ca07190 fffFfF802°3597ce6b nt! EmInitSystem+0x12b
~4ca073d0 ffffFf802 354992a3 nt!Phase1InitializationDiscard+0xe63
~4ca07570 ffffF802° 35263a2a nt!PhaselInitialization+0x23
“4ca075b0 FfFfFF802 3546e2d4 nt!PspSystemThreadStartup+0x5a
~4ca07600 00000000 00000000 nt!KiStartSystemThread+0x34
_
PP
```

## Slide 77

## Do RE job, find RCE

Windows Kernel EmpParseCallbacks Heap Out-ofBounds Write

The first Windows kernel memory corruption I’ve discovered in my career.

#BHUSA @BlackHatEvents

## Slide 78

## What’s Actually Going On?

**Kernel-mode**

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
wdcnet What’s Actwally Going Ow? -
Defensible? Defensible?
Network
Boot
Network
——>_ _User-mode Boot —i—» Kernel-mode
oo
CS) Not defensible! CS) Not defensible!
We have determined that the behavior described in your report is by design.
This case has been determined to be a moderate severity
defense in depth issue and will not require a security update.
l™ Status changed from Review/Repro to Complete
```

## Slide 79

## Agenda

- Background

- Attack surface in bootloader

   - Network protocol

   - BCD Registry

   - Security Policy

   - Filesystem

   - Logic flaw

- Attack surface beyond bootloader

- **Future Work & Take Aways**

#BHUSA @BlackHatEvents

## Slide 80

## Future Work

- Continue research on bootmgfw.efi on other attack surface

- Winload.efi

   - Hardware specific firmware (etc. HSP on AMD platform)

- Resume.efi

- Hyper-V bootloader

- Research on Windows kernel and userland service code that is invisible to remote attacker from normal boot

#BHUSA @BlackHatEvents

## Slide 81

## One more interesting thing

- Looking at Microsoft’s patch, there’s multiple branch, PCA2011 and PCA2023. Code before 26100 and code after 26100.

- You really should take the update guide manually. It’s not only for DBX update, also to switching your bootloader to PCA2023 branch.

#BHUSA @BlackHatEvents

## Slide 82

## Booting into breaches

- PCA2011 Time breaches

- Patch branch breaches

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
BRIEFINGS
¢ PCA2011 Time breaches
¢ Patch branch breaches
Patch
branch
PCA20T1 breaches
Time bre 4
```

## Slide 83

## Take Aways

- B(ring) Y(our) O(wn) B(ootloader) to archive AV:A in secureboot attack

- Small function with sanitize in its name could be very vulnerable

- Recursive calling could be exploitable to RCE in UEFI environment

- Check twice after your patch release, especially when you have found vulnerabilities in same component at a very large volume, don’t be lazy.

- Take closer look at the code if fuzzer can generate DoS.

- Out of scope vulnerabilities could also be interesting in real world.

- Take further action immediately to fix these SecureBoot vulnerabilities.

#BHUSA @BlackHatEvents

## Slide 84

###### **Recheck for multiple WDS server**

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Unauthenticated Attacker im
from network oo
Recheck for multiple VWWDS server
H UEFI PXE Bootloader OS Loader
i
```

## Slide 85

## A tool to detect secureboot status

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ARH I TLSVEbLSmLet
1sK7u53zWLdoVoL
FCbv5ukP/jTvNdrY
yFS£uCkIJwNdZNF JC
GzpWsB8k3KdU
SHNXlylyUtEn1tG8tuZYPMia
376CBiEGFMglyheaswddg1Pt3M2@UstdDct
RACSesLChIRpP9AVLArmn 1 yf
bskxvzLPCwgs+2LMZ
jLGdLvUpmkCD/1Z
SECUREBOOT STATUS CHECK English wh 2bGKDpEGXGAT
eXnTLzm5D9V
Lh H4sZ+TP&
i5GcUeRLr7ht u FF5Syd+X3259 1/dH
gJoP@m179M0k9Ve NaOL@a+d/4Vmom5VuY t3GEYqhk
Ou/8X8AVL TyWOdwAAA=
ANALYZE
Thi pject t of the Black Hat USA research "Booting into B ne S B R Sw iy ee Pale i
Attack S t helps you check if your system is affected b erabilitie ered b
zure Yang and patched in 2024. The tool collects Gnonymous data for presentatio e final Black Hat ta Analysis Results
:o detect secureboot
em status
Z V Windows PCA 2023 Certificate detected
ate database is up to date.
Windows Instructions
® Help us improve by taking a quick survey about your system
Copied!
Boot UEFI dat dbx inary £
```

## Slide 86

Thanks! X: @4zure9

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
Thanks!
xX: @4zureY
uty CYBER
l | 1. KUNLUN
87
```
