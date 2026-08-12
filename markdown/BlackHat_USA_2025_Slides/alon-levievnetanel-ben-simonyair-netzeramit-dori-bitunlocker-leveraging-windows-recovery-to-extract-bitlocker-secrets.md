---
title: "BitUnlocker Leveraging Windows Recovery to Extract BitLocker Secrets"
speakers: ["Alon Leviev", "Netanel Ben Simon", "Yair Netzer", "Amit Dori"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Alon Leviev&Netanel Ben Simon&Yair Netzer&Amit Dori_BitUnlocker Leveraging Windows Recovery to Extract BitLocker Secrets.pdf"
pages: 98
sha256: "8ad011ab5e74902e34c122d8e9e319bbc5cfd947da50c86215f4ec68ff7f0173"
text_chars: 19273
ocr_pages: 12
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T22:49:49Z"
---
# BitUnlocker Leveraging Windows Recovery to Extract BitLocker Secrets

**Speakers:** Alon Leviev, Netanel Ben Simon, Yair Netzer, Amit Dori  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Alon Leviev&Netanel Ben Simon&Yair Netzer&Amit Dori_BitUnlocker Leveraging Windows Recovery to Extract BitLocker Secrets.pdf` (98 pages)

## Slide 1

**BitUnlocker​** Leveraging Windows Recovery to Extract BitLocker Secrets

## Slide 2

Who are we?

S

ecurity

T

esting &

O

ffensive

esearch at

R

M

icrosoft (STORM)

**Alon Leviev (@alon_leviev) Netanel Ben Simon (@NetanelBenSimon) Security Researcher @ Microsoft Senior Security Researcher @ Microsoft**

## Slide 3

# **Agenda**

###### **Research Background**

**WinRE Overview**

**Vulnerabilities and Exploitation**

**Closing Remarks**

## Slide 4

**Research Background**

## Slide 5

## **Data at Rest Protection**

**Defend your sensitive data against theft scenarios**

## Slide 6

## **Data at Rest Protection – Why Should You Care?**

According to research, **a laptop is stolen every 53 seconds** – but how prepared are you for what comes next? _The Guardian_

Did you know that **laptop computer have a 1-in-10 chance of being stolen** , which means there is a 10% chance for you to be the victim of laptop theft. _Prey Project_

**The average value of a lost laptop is $49,246** . This value is based on seven cost components: replacement cost, detection, forensics, data breach, lost IP costs, lost productivity, and legal, consulting and regulatory expenses. _Intel_

## Slide 7

**BitLocker – Windows’s Data Protection Cornerstone BitLocker is a Full Volume Encryption (FVE) technology**

BitLocker encrypted volume

EFI Volume OS Volume Recovery Volume Hard Disk

## Slide 8

## **BitLocker Threat Model**

**Full physical access**

**No login credentials**

## Slide 9

### **The Hidden Attack Surface - The Windows Recovery Environment (WinRE)**

**Physical attackers without logon credentials can directly boot into WinRE**

Shift +

## Slide 10

### **Targeting the Windows Recovery Environment (WinRE) We performed a security review of WinRE focused on –**

Finding new
vulnerabilities

Exploiting them

Fixing them

Hardening WinRE

## Slide 11

**WinRE Overview**

## Slide 12

## **WinRE Overview**

- WinRE is the recovery platform of Windows

- • WinRE is designed to recover from critical system issues

1 st  Crash

2 nd  Crash

WinRE

## Slide 13

## **WinRE Architecture – Recovery OS**

- WinRE is a lean Windows OS with recovery customizations (aka. Recovery OS)

Windows OS
Recovery OS

## Slide 14

## **WinRE Architecture – Recovery OS Customizations**

• The customizations include Startup Repair, System Reset, System Restore etc.

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
WinRE Architecture — Recovery OS Customizations
¢ The customizations include Startup Repair, System Reset, System Restore etc.
Choose an option
Continue
Bait and con
a tinue to Windows 1 (!)
```

## Slide 15

## **WinRE Architecture – WinRE.wim**

• The recovery OS is compressed into a single WIM file – WinRE.wim

###### Full Recovery OS

WinRE.wim

**Compress into WIM**

## Slide 16

## **WinRE Architecture – RAM disk boot**

- WinRE.wim is booted from RAM disk

- Changes to RAM disk are never committed back to WinRE.wim

RAM

##### **Volatile** RAM disk

###### WinRE.wim

Decompress WinRE.wim into RAM

## Slide 17

## **WinRE Changes As Part Of BitLocker’s Introduction**

What potential
To support
impact these
BitLocker
changes had?
recovery –
design
BitLocker WinRE
changes were
implemented
in WinRE

## Slide 18

**WinRE Design Change #1 – WinRE.wim Relocation WinRE.wim was relocated from the BitLocker protected OS volume to the unprotected recovery volume**

WinRE.wim
EFI Volume OS Volume Recovery Volume
Hard Disk

## Slide 19

**WinRE Design Change #2 – Trusted WIM Boot Trusted WIM boot was developed to establish trust between the Recovery OS and the Main OS**

WinRE.wim
Compare against
Hash WinRE.wim known trusted hash
Boot
Manager

Auto-Unlock
OS Volume
Lock  OS Volume

## Slide 20

## **WinRE Design Change #2 – Trusted WIM Boot**

- **In Auto-Unlock state – WinRE can fully access the OS volume**

- **In Locked state – WinRE cannot access the OS volume**

Locked State

_Auto-Unlocked State_

WinRE

No access

WinRE

Full access

OS Volume

OS Volume

## Slide 21

**WinRE Design Change #3 – Volume Re-Lock Main OS volume re-lock functionality was developed to safeguard BitLocker from by-design harmful recovery operations (e.g., Command Prompt)**

WinRE UI

User launches risky recovery tool

**Re-lock** OS Volume

## Slide 22

**WinRE Design Change #3 – Volume Re-Lock**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
WinRE Design Change #3 — Volume Re-Lock
Administrator: X:\windows\system32\cmd.exe
You must unlock this drive from Control Panel.
BitLocker ve Encryp : Configuration Tool version 10.0.22621
Copyright (C) 2013 Microsoft Corpor ghts reserved.
Disk volumes that can be protected with
tLocker ve Encryp
me C: [Label Unknown]
[Data Volume]
Si Unknown GB
Bit H 2.8
Conver IS: Unknown
Percen Encrypted: Unknown%
Method: XTS-AES 128
Status: Unknown
Locked
Unknown
Disabled
```

## Slide 23

## **WinRE Design Changes Summary**

**As long as WinRE.wim hash is trusted, and no harmful recovery operations are triggered – the main OS volume is unlocked!**

## Slide 24

**Any Attack Surfaces Exposed? Attacking parsers of external files residing in non-protected volumes**

Parsing Parsing
WinRE
EFI Volume OS Volume Recovery Volume
Hard Disk

## Slide 25

## **Our Focus Today**

ReAgent.xml
BCD
Boot.sdi
EFI Volume OS Volume Recovery Volume
Hard Disk

## Slide 26

## **Vulnerabilities and Exploitations**

## Slide 27

Attacking Boot.sdi Parsing
ReAgent.xml
BCD
Boot.sdi
EFI Volume OS Volume Recovery Volume
Hard Disk

## Slide 28

## **Boot.sdi purpose**

- Boot.sdi is an optional component in the RAM disk boot procedure

- It contains metadata used for the RAM disk creation

- If specified, it is **prepended to the RAM disk image**

RAM disk buffer
0x00
Prepend Boot.sdi
Boot.sdi
to RAM disk
image
Disk.img
0xFF

## Slide 29

## **Boot.sdi Usage In WIM boot**

In the context of WIM boot, Boot.sdi contains –

- Relative offset to WinRE.wim

**RAM disk buffer** 0x00

- Empty NTFS volume

WIM offset
NTFS volume
Boot.sdi

Trusted
WinRE.wim
0xFF

## Slide 30

## **Why is this Setup Required?** For compatibility

**RAM disk buffer** 0x00

WIM offset
NTFS volume
Boot.sdi

WIM offset
NTFS volume
Trusted
WinRE.wim
0xFF

## Slide 31

## **RAM Disk Load – Pseudo Code Analysis**

1) Allocate the SDI + WIM buffer

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
RAM Disk Load // Allocate memory for both SDI and WIM
RamDiskImageButfer = AllocateMemory(SdiSize + WimSize);
— Pseudo Code
Analysis // Load SDI to buffer and DO NOT calculate SDI hash
LoadFileToBuffer (SdiPath,
RamDiskImageBuffer ,
SdiSize,
1) Allocate the SDI + NULL) ;
WIM buffer
// Load WIM to buffer right after SDI and calculate WIM hash
LoadFileToBuffer (WimPath,
Add2Ptr(RamDiskImageBuffer, SdiSize),
WimSize,
WimHash) ;
// The WIM booted from is the one pointed by the SDI!
WimAddress = RamDiskImageBuffer + SdiStrust->WimOffset;
```

## Slide 32

## **RAM Disk Load – Pseudo Code Analysis**

2) Load the SDI into the allocated buffer

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
RAM Disk Load // Allocate memory for both SDI and WIM
RamDiskImageButfer = AllocateMemory(SdiSize + WimSize);
— Pseudo Code
Analysis // Load SDI to buffer and DO NOT calculate SDI hash
LoadFileToBuffer (SdiPath,
RamDiskImageBuffer ,
SdiSize,
2) Load the SDI into the NULL) ;
allocated buffer
// Load WIM to buffer right after SDI and calculate WIM hash
LoadFileToBuffer (WimPath,
Add2Ptr(RamDiskImageBuffer, SdiSize),
WimSize,
WimHash) ;
// The WIM booted from is the one pointed by the SDI!
WimAddress = RamDiskImageBuffer + SdiStrust->WimOffset;
```

## Slide 33

## **RAM Disk Load – Pseudo Code Analysis**

3) Load the WIM into the allocated buffer, following the SDI. **The load API also calculates the WIM hash used for WIM trust validation!**

## Slide 34

## **RAM Disk Load – Pseudo Code Analysis**

4) The WIM that is booted is the one pointed by the SDI. **There is no correlation between the used WIM and the hashed WIM!**

## Slide 35

## **Vulnerability #1 – Bypassing WIM Validation Through WIM offset** Trusted WinRE.wim is used for WIM validation

0x00

**RAM disk buffer**

WIM offset
NTFS volume
Boot.sdi
Trusted

WIM offset
NTFS volume
Trusted
WinRE.wim
0xFF

## Slide 36

## **Vulnerability #1 – Bypassing WIM Validation Through WIM offset**

Trusted WinRE.wim is used for WIM validation Untrusted WinRE.wim is the actual WIM booted

is the actual WIM booted RAM disk buffer
0x00
WIM offset
NTFS volume
Boot.sdi
Untrusted WinRE.wim

Trusted
WinRE.wim
0xFF

## Slide 37

**Vulnerability #1 DEMO**

## Slide 38

## Slide 39

## **Attacking ReAgent.xml Parsing**

ReAgent.xml
BCD
Boot.sdi
EFI Volume OS Volume Recovery Volume
Hard Disk

## Slide 40

**ReAgent.xml Purpose ReAgent.xml represents the state and configuration of WinRE runtime**

Parse ReAgent.xml
WinRE
ReAgent.xml

## Slide 41

## **ReAgent.xml Scheduled Operations ReAgent.xml controls which recovery operation will be executed in WinRE**

Execute scheduled
e.g.
Parse ReAgent.xml
recovery operation
WinRE Startup Repair
ReAgent.xml

## Slide 42

Focused Scheduled Operations

Microsoft Confidential | Internal Use Only

**Offline Scanning WinRE Apps**

## Slide 43

## **Offline Scanning Scheduled Operation**

- Offline scanning allows launching Anti-Virus scan from WinRE against the main OS

- This is valuable against malwares that do not persist in WinRE runtime

Scan for malware!
WinRE Main OS

## Slide 44

## **Offline Scanning Scheduled Operation Limitations**

1) Offline scanning apps are always executed from the Main OS

- 2) Offline scanning apps must be signed by Microsoft or WHQL

- 3) Signatures must be embedded

Embedded
Signature
AVScan.exe
OS Volume

Execute AVScan.exe
WinRE
From OS volume!

## Slide 45

**How Many Apps Fit With The Limitations?**

**~ 30 apps that fit with the limitations**

**Not all apps are compatible running in WinRE**

## Slide 46

## **Any Apps That Can Be Abused?**

- Among the allowed apps is tttracer.exe, a Time Travel Debugging utility

- Tttracer.exe allows tracing an arbitrary executable

>> tttracer.exe cmd.exe

Tttracer.exe

cmd.exe

## Slide 47

## **Vulnerability #2 – Exploitation Flow**

**1 Schedule offline scanning in ReAgent.xml**

Parse ReAgent.xml
Offline
WinRE
Scanning
ReAgent.xml

## Slide 48

## **Vulnerability #2 – Exploitation Flow**

2 WinRE performs offline scanning operation
Perform scheduled
Parse ReAgent.xml
recovery operation
Offline
WinRE Offline Scanning
Scanning
ReAgent.xml

## Slide 49

## **Vulnerability #2 – Exploitation Flow**

**3 The offline scanning app tttracer.exe is executed**

Perform scheduled Parse ReAgent.xml recovery operation Offline WinRE Scanning **ReAgent.xml**

Offline Scanning

Tttracer.exe

## Slide 50

## **Vulnerability #2 – Exploitation Flow**

4 Tttracer.exe executes cmd.exe
Perform scheduled
Parse ReAgent.xml
recovery operation
Offline
WinRE Offline Scanning
Scanning
ReAgent.xml
cmd.exe Tttracer.exe

## Slide 51

## **Vulnerability #2 – Exploitation Flow**

**5 The executed cmd.exe now has full access to the BitLocker encrypted data!**

Perform scheduled
Parse ReAgent.xml
recovery operation
Offline
WinRE Offline Scanning
Scanning
ReAgent.xml
Extract BitLocker
encrypted data!

**Extract BitLocker encrypted data!**

Tttracer.exe

cmd.exe

## Slide 52

**Vulnerability #2 DEMO**

## Slide 53

## Slide 54

Today

s Focused Scheduled Operations

’

s presentation we will focus on analyzing two operations

In today

Microsoft Confidential | Internal Use Only

**~~Offline Scanning~~ WinRE Apps**

## Slide 55

## **WinRE Apps Scheduled Operation**

- WinRE apps allows the execution of apps in WinRE runtime

- If the app is trusted, it is executed in auto-unlock state

- If the app is not trusted, it is executed after volumes re-locked

Trusted.exe

Is app trusted?
WinRE

**Execute** app in **auto-unlock Re-lock** volumes and **execute** app

## Slide 56

## **WinRE Apps Trust Validation**

- Trusted WinRE apps are registered by name and hash in WinRE’s registry

- WinRE’s registry lives in WinRE.wim and is **not accessible to an attacker!**

Trusted.exe 83e83…e1919

## Slide 57

## **WinRE Apps Trust Validation**

- If the hash of the app **matches a registry entry** , the app is **trusted**

- If the hash of the app **does not match a registry entry** , the app is **untrusted**

Is app  name  and  hash Trusted
Hash app existing in registry?
WinRE
Untrusted
Trusted.exe

## Slide 58

## **Is the Trust Validation Secure?**

**WinRE apps trust validation is SOLID!**

**But already registered apps also expose an attack surface!**

## Slide 59

## **The SetupPlatform.exe Trusted App**

- During Windows Upgrade, the **SetupPlatform.exe** app is registered as trusted

- After the upgrade completes, the trusted app entry is **not removed** !

SetupPlatform.exe is trusted on upgraded machines!

SetupPlatform.exe

## Slide 60

## **Peeking Inside SetupPlatform.exe**

Shift F10  Configuration
Exit
Registration check
SetupPlatform.exe
OS
Volume

cmd.exe

## Slide 61

## **Time Window – Impossible to Trigger**

~ 1ms
Shift F10  Configuration
Exit
Registration check
SetupPlatform.exe
OS
Volume
cmd.exe

## Slide 62

## **Creating Infinite Time Window**

SetupPlatform.exe

Shift F10  INI  Message
Registration check Box
Recovery
Volume

cmd.exe

## Slide 63

## **Vulnerability #3 – Exploitation Flow**

**1 Schedule SetupPlatform WinRE app in ReAgent.xml**

Parse ReAgent.xml WinRE app WinRE **ReAgent.xml**

## Slide 64

## **Vulnerability #3 – Exploitation Flow**

2 WinRE validates the app to be executed
Perform scheduled
Parse ReAgent.xml recovery operation
WinRE app WinRE WinRE app execution
ReAgent.xml

## Slide 65

## **Vulnerability #3 – Exploitation Flow**

**3 The WinRE app SetupPlatform.exe is executed** Perform scheduled Parse ReAgent.xml recovery operation WinRE app WinRE **ReAgent.xml**

WinRE app execution

SetupPlatform.exe

## Slide 66

## **Vulnerability #3 – Exploitation Flow**

**4 SetupPlatform.exe registers Shift+F10 hotkey as cmd.exe launcher** Perform scheduled Parse ReAgent.xml recovery operation WinRE app WinRE WinRE app execution **ReAgent.xml**

Shift+F10

Register cmd.exe launcher

SetupPlatform.exe

## Slide 67

## **Vulnerability #3 – Exploitation Flow**

5 SetupPlatform.exe locates and parses SetupPlatform.ini
Perform scheduled
Parse ReAgent.xml recovery operation
WinRE app WinRE WinRE app execution
ReAgent.xml
Look for INI Register cmd.exe launcher
SetupPlatfornm.ini Shift+F10
SetupPlatform.exe

## Slide 68

**Vulnerability #3 – Exploitation Flow SetupPlatform.exe launches message box and blocks execution until message 6 box is closed**

Perform scheduled Parse ReAgent.xml recovery operation WinRE app WinRE WinRE app execution **ReAgent.xml**

Look for INI SetupPlatfornm.ini Message Box

Shift+F10

Register cmd.exe launcher

SetupPlatform.exe

## Slide 69

## **Vulnerability #3 – Exploitation Flow**

7 Shift+F10 is pressed to launch cmd.exe
Perform scheduled
Parse ReAgent.xml recovery operation
WinRE app WinRE WinRE app execution
ReAgent.xml
Look for INI Register cmd.exe launcher
SetupPlatfornm.ini Shift+F10
SetupPlatform.exe
Press Shift+F10
Message Box

cmd.exe

## Slide 70

## **Vulnerability #3 – Exploitation Flow**

8 The executed cmd.exe now has full access to the BitLocker encrypted data!
Perform scheduled
Parse ReAgent.xml recovery operation
WinRE app WinRE WinRE app execution
ReAgent.xml
Look for INI Register cmd.exe launcher
SetupPlatfornm.ini Shift+F10
SetupPlatform.exe
Press Shift+F10
Extract BitLocker
Message Box
encrypted data!
cmd.exe

## Slide 71

**Vulnerability #3 DEMO**

## Slide 72

## Slide 73

## **Attacking BCD Parsing**

ReAgent.xml
BCD
Boot.sdi
EFI Volume OS Volume Recovery Volume
Hard Disk

## Slide 74

## **BCD Purpose**

- BCD – Boot  Configuration Data

- BCD represents Windows Boot configuration

- BCD controls boot entries, boot parameters, recovery settings and more

Boot Entries
Boot Parameters
Recovery Settings
…
BCD

## Slide 75

## **WinRE BCD Usage – Locate Target OS Volume**

Disk Volumes
EFI
Where the OS to
recover reside?
OS device:
WinRE OS
OS
BCD
Recovery

## Slide 76

## **WinRE Blindly Trusts Target OS Volume**

Disk Volumes

EFI
OS
Recovery

WinRE

## Slide 77

## **Desired Primitive – Target OS Location Impersonation**

_Current State_

_Desired State_

Disk Volumes

Disk Volumes

EFI
OS device:
OS
OS
BCD
Recovery

EFI
OS device:
Recovery OS
BCD
Recovery

## Slide 78

## **Directly Controlling Target OS Location – Not Valuable**

Boot phase OS phase

Lookup the OS to unlock in BCD Boot Manager Recovery OS Lookup the OS to recover in BCD

Disk Volumes
EFI
OS device:
OS
Recovery
BCD
Recovery

## Slide 79

## **WinRE BCD Store Search Logic**

**WinRE iterates over disk volumes and searches each one for the BCD store**

Does BCD store exist?
EFI Volume OS Volume Recovery Volume
Hard Disk

## Slide 80

## **Volume Iteration Functions – Find[First/Next]Volume**

FindFirstVolume and FindNextVolume Remarks Section from MSDN

“You should not assume any correlation between the order of the volumes that are returned by these functions and the order of the volumes that are on the computer […]”

## Slide 81

**Typical Volume Order**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Typical Volume Order
DISKPART> list vol
Volume Windows Partition Healthy
Volume SYSTEM Partition Healthy
Volume WinRE DRV Partition 2000 MB Health Hidden
```

## Slide 82

## **WinRE BCD Store Search Logic**

Typical Order Returned Order
OS Volume
OS Volume
VS
EFI Volume Recovery Volume
EFI Volume
Recovery Volume

## Slide 83

## **Gaining The Desired Primitive**

Does BCD store exist?
OS Device:  OS device:
OS Recovery
BCD Attacker BCD
EFI Volume OS Volume Recovery Volume
Hard Disk

## Slide 84

## **The Gained Primitive**

###### EFI Volume

Lookup OS to unlock Boot Manager

Disk Volumes

Unlock
OS device:
OS
BCD

OS

Boot phase OS phase

…

Recovery Volume

Recovery OS

Recover
OS device:
Recovery
Recovery
BCD

Lookup OS to recover

## Slide 85

## **WinRE Blindly Trusts The Recovery Volume**

###### Disk Volumes

EFI
OS
Recovery

WinRE

## Slide 86

## **Exploitation Requirements**

Find a WinRE flow that:

**Can be executed from WinRE UI or ReAgent.xml**

**Does not trigger the relock functionality**

**Queries configuration from the target OS to perform sensitive operations**

## Slide 87

## **Potential Candidate – Push Button Reset (PBR) Push Button Reset (PBR) - Windows’s System Reset tool**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Potential Candidate — Push Button Reset (PBR)
Push Button Reset (PBR) - Windows’'s System Reset tool
’
Resetting this PC 2%
```

## Slide 88

**Online PBR Exploitation Applicability Online PBR mode was found applicable for exploitation**

**Can be executed from WinRE UI or ReAgent.xml**

**Does not trigger the relock functionality**

**Queries configuration from the target OS to perform sensitive operations**

## Slide 89

## **The Sensitive Configuration - PBR ResetSession.xml PBR can decrypt BitLocker volumes if stated in ResetSession.xml**

PBR ResetSession.xml
<Operation OperationType=“DecryptVolumes“ TargetVolume=“C:“ />

## Slide 90

## **Exploitation Setup**

#### **The exploit requires creating few files on the Recovery volume:**

Operation: OS device:  Decrypt:
Online PBR Recovery OS
ReAgent.xml BCD ResetSession.xml

##### Recovery Volume

## Slide 91

## **Exploitation Flow**

Retrieve  Check PBR  Decrypt OS
PBR
Target OS Configuration volume
OS device:  Decrypt:
Recovery OS
BCD ResetSession.xml

##### Recovery Volume

OS Volume

## Slide 92

## **Vulnerability #4 DEMO**

## Slide 93

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
—
Washington G) Daity Wonder
ta oe °F Po Pm Sri Lanka’s Cloud-Kissed
— weed — Nuwara Eliya: A Drone
2 as watch jiya: ss
See full forecast Watch more videos like this
Es
iS
Singapore quiz
se sl Singapore is located on
= which continent?
GC wade
Take the quiz
4h
ai
S| Si eee peg =
```

## Slide 94

**Closing Remarks**

## Slide 95

Vulnerability Fixes

- The CVEs for the vulnerabilities presented today are –

   - CVE-2025-48800

   - CVE-2025-48003

   - CVE-2025-48804

   - CVE-2025-48818

Fixes were shipped in July

’

s Patch Tuesday

## Slide 96

BitLocker Countermeasures

- Enable TPM+PIN for pre-boot authentication

- Enable the REVISE mitigation for anti-rollback protection

## Slide 97

We’re Never Done!
Find Vulnerabilities
Mitigate  Exploit them
common
patterns
Identify  Fix them
common
patterns

## Slide 98

Thank You!

S

ecurity

T

esting &

O

ffensive

esearch at

R

M

icrosoft (STORM)

**Alon Leviev (@alon_leviev) Netanel Ben Simon (@NetanelBenSimon) Security Researcher @ Microsoft Senior Security Researcher @ Microsoft**
