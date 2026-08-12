---
title: "Windows Downdate Downgrade Attacks Using Windows Updates"
speakers: ["Alon Leviev"]
conference: "Black Hat"
conference_full: "Black Hat USA 2024"
edition: "USA"
year: 2024
source_pdf: "Black Hat USA 2024 slides/Alon Leviev_Windows Downdate Downgrade Attacks Using Windows Updates.pdf"
pages: 87
sha256: "6b7ff7abd4c5b57a2c5b3df354a3d756367cdcb0dc9cf336b39c896e4861e571"
text_chars: 18409
ocr_pages: 5
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:29:15Z"
---
# Windows Downdate Downgrade Attacks Using Windows Updates

**Speakers:** Alon Leviev  
**Conference:** Black Hat USA 2024  
**Source:** `Black Hat USA 2024 slides/Alon Leviev_Windows Downdate Downgrade Attacks Using Windows Updates.pdf` (87 pages)

## Slide 1

Windows Downdate: **Downgrade Attacks Using Windows Updates**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
3: SafeBreach
DOWNDATE
er
ia
/ 4
tie ole
i fig
) /
i
Via
Windows Downc
Downgrade Atta
Using Window
```

## Slide 2

###### Alon Leviev

Security Researcher @ SafeBreach 22-years-old

Self-taught

OS internals, reverse engineering and vulnerability research

Former BJJ world and european champion Creator of PoolParty process injection techniques

## Slide 3

###### Agenda

Research Background

Downgrade Attacks Using Windows Updates Virtualization-Based Security Vulnerabilities Windows Update Restoration Vulnerability Closing Remarks

## Slide 4

W I N D O W S D O W N D AT E

# Research Background

## Slide 5

###### What are Downgrade Attacks?

**Attacker**

**Vulnerable Software**

Downgrade **immune** software to **vulnerable** software

**Immune Software**

## Slide 6

Downgrade Attacks In-The-Wild – BlackLotus UEFI Bootkit

The BlackLotus UEFI bootkit employed a downgrade attack to bypass Secure Boot

The Secure Boot bypass worked on fully updated Windows 11 machines

Caused a massive panic in the cyber security industry

## Slide 7

###### Secure Boot In a Nutshell

UEFI
Firmware
UEFI Boot
Manager
Verify
Windows
Boot Manager
Verify
Windows
Each component in the
Boot Loader
Verify
boot chain must be
digitally signed
Windows Kernel
Verify

## Slide 8

###### BlackLotus Secure Boot Bypass

UEFI
Firmware
BlackLotus downgraded the  Windows
Boot Manager  to  signed  but  vulnerable
UEFI Boot  version of it
Manager
Verify
Windows
Boot Manager
Verify
Windows
Boot Loader
Verify
Windows Kernel
Verify

## Slide 9

###### Microsoft’s Mitigation Against Secure Boot Downgrades

Microsoft’s mitigation included adding signed but vulnerable boot managers to revocation lists

**UEFI** adding signed but vulnerable boot managers to **Firmware** revocation lists **Revoked boot managers are not allowed UEFI Boot Manager Verify Windows Boot Manager Verify Revocation List Windows … Boot Loader Verify … Windows Kernel Verify …**

## Slide 10

###### Research Motivation

Are there any components affected by downgrade attacks other then Secure Boot?

## Slide 11

###### Research Goals

Evaluate the state of downgrade attacks on Windows Find if any other critical components have been overlooked

## Slide 12

###### Downgrade Vision

###### Bring Your Own Vulnerable Windows!

## Slide 13

###### What makes a downgrade attack complete?

Fully Undetectable The downgrade is performed in a legitimate way

Invisible

Persistent

Irreversible

The downgraded components appear up to date Future updates do not overwrite the downgraded components

Scanning and repairing tools are unable to detect and repair corruptions

## Slide 14

###### Finding the suitable component

Which component is the least expected to perform downgrades?

## Slide 15

###### Finding the suitable component

###### Windows Updates!

## Slide 16

W I N D O W S D O W N D AT E

##### Downgrade Attacks Using Windows Updates

## Slide 17

###### Windows Updates Architecture

**Administrator Enforcement**

**Trusted Installer Enforcement**

**Communication Over COM**

Update Client Process

Update Server Process

**Update Files**

**Ntoskrnl.exe**

**Ntdll.dll**

**… …**

## Slide 18

Trusted Installer enforcement – Is It Useful?

Multiple working public PoC’s of Administrator to Trusted Installer elevation

It is considered malicious and EDRs detect such elevations Even if I bypass detection, self-implementing the downgrade may seem malicious

**Taking over the Windows Update process solves all of that**

## Slide 19

###### Update Flow

Update Client
Process

1. Client asks the server to perform an update given an update folder

Update
Folder

Update Server Process

## Slide 20

###### Update Flow

Update Client
Process

2. Server validates the integrity of the client supplied update folder

Update Server
Process

Update
Folder

## Slide 21

###### Update Flow

Update Client
Process

3. Server operates on the update folder to finalize the update files

Update Server
Process

Update Files
Update
Folder

## Slide 22

###### Update Flow

4. Server saves the update action list to **%WinDir%\WinSxS\Pending.xml**

Update Client Process

Update Server Process

Update Files
Update
Folder

## Slide 23

###### Update Flow

Update Client
Process

5. In the next reboot, **Pending.xml** is operated on, and the update actions are performed

Update Server Process

Update Files
Update
Folder

## Slide 24

###### What Is Client Controlled?

Update Client
Process

Trusted Installer Enforced

Update Server
Process
Update Files
Update
Folder
Client
Trusted Installer Enforced Controlled

## Slide 25

###### Update Folder Contents

**Update folder** contains update components

Update
Folder

Update Component

## Slide 26

###### Update Folder Contents – MUM

**MUM files** contain component metadata, component dependencies, installation order etc.

**Update Folder**

Update Component

## Slide 27

###### Update Folder Contents – Manifest

**Manifest files** contain installation specific data such as file paths, registry keys, and installers to execute

**Update Folder**

Update Component

## Slide 28

###### Update Folder Contents – Differential

**Differential files** are deltas from the base files **Base + Differential = Full Update File**

**Update Folder**

Update Component

## Slide 29

###### Update Folder Contents – Catalog

**Catalog files** are the digital signatures of **MUM** and **Manifest** files

**Update Folder**

Update Component

## Slide 30

###### Update Folder Contents – Recap

Only **Catalogs** are explicitly digitally signed **Manifests** and **MUMs** are not explicitly digitally signed, but are signed in **Catalogs**

**Differentials** are not digitally signed

**Differentials** control the actual final update file content

## Slide 31

###### Targeting Differential Files

Any chance that **differential** files were left behind in terms of verification?

## Slide 32

###### Targeting Differential Files – Impossible

Expected full update files hashes are hardcoded in the **manifests**

**Sha256** (Full Update File)

## Slide 33

###### Targeting The Action List

The action list is Trusted Installer enforced. Since operated on during reboots, the system must save its state somewhere.

## Slide 34

###### Targeting The Action List – Possible!

Action List path is saved in the registry and is **not Trusted Installer enforced!**

**HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\SideBySide\Configuration\PoqexecCmdline**

**PoqExec.exe Pending.xml [more args]**

## Slide 35

###### What Can We Do With The Action List?

```
<POQpostAction="reboot">
```

```
<CreateFilepath="C:\Windows\System32\Create.exe"fileAttributes="0x00000000"/>
<MoveFilesource="C:\UpdateDir\Source.exe“ destination="C:\Windows\System32\Destination.exe"/>
<HardlinkFilesource="C:\UpdateDir\Source.exe“destination="C:\Windows\System32\Destination.exe"/>
<SetFileInformationpath="C:\UpdateDir\Source.exe“securityDescriptor="binary base64:[BASE64-BLOB]"flags="0x00000040"/>
<DeleteFilepath="C:\Windows\System32\Delete.exe"/>
```

```
<CreateDirectorypath="C:\Windows\System32\Directory"fileAttribute="0x00000080“securityDescriptor="binary base64:[BASE64-BLOB]"/>
<CreateKeypath="\Registry\Machine\Key"/>
```

```
<SetKeyValuepath="\Registry\Machine\Key"name="Name" type="0x00000001“ encoding="base64" value="[BASE64-BLOB]"/>
<SetKeySecuritypath="\Registry\Machine\Key“securityDescriptor="binary base64:[BASE64-BLOB]"flags="0x00000001"/>
<DeleteKeyValuepath="\Registry\Machine\Key"name="Value"/>
<DeleteKeyflags="0x00000001"path="\Regsitry\Machine\Key"/>
</POQ>
```

## Slide 36

###### How To Downgrade Files?

The **HardlinkFile** action can be used to downgrade system files

```
<HardlinkFilesource="C:\UpdateDir\Source.exe“destination="C:\Windows\System32\Destination.exe"/>
```

## Slide 37

###### Initiating Update

**1. Set Trusted Installer service as Auto-Start**

**2. Add Pending.xml path in registry**

Trusted
Installer Service

###### **HKLM\.....\PoqexecCmdline**

**3. Add Pending.xml identifier in registry**

**HKLM\COMPONENTS\PendingXmlIdentifier**

## Slide 38

###### Downgrade Attack via Windows Update Achieved!

Ability to “update” the system with a downgrading Pending.xml

All integrity verification checks are bypassed No Trusted Installer elevation is required

Complete Windows Update takeover!

## Slide 39

###### Complete Downgrade Attack – Fully Undetectable

The downgrade is fully undetectable, it is performed in the most legitimate way

## Slide 40

###### Complete Downgrade Attack – Invisible

The system will appear up to date, as we “updated” the system

## Slide 41

###### Complete Downgrade Attack – Persistent

The action list parser PoqExec.exe is not digitally signed, and can be patched to install empty updates

…

PoqExec.exe

Not installing
updates

## Slide 42

###### Complete Downgrade Attack – Irreversible

The System Integrity Check and Repair utility SFC.exe is not digitally signed, and can be patched to never detect or repair corruptions

**SFC.exe**

**Not detecting or repairing corruptions**

## Slide 43

Demo #1

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
‘Windows 11 23h2 on VOSTRO-02
DING OWSSDO}
80°F 2:55 PM
Partly clou Bm Q Search aA Law CB = ~A & OS® gr 20n9 |
```

## Slide 44

Admin to Kernel – Security Boundary?

Not a security boundary

Administrator

Kernel

## Slide 45

Admin to Kernel – Not a Boundary, But Still a Threat

Lots of users are still running as Administrator

## Slide 46

###### Microsoft’s Solution – Deprivileging the Kernel

Microsoft decided to deprivilege the kernel to make kernel access less valuable

## Slide 47

W I N D O W S D O W N D AT E

### VirtualizationBased Security

## Slide 48

###### What Is VBS?

Secure and isolated virtual environment powered by the Hyper-V hypervisor

## Slide 49

###### Why VBS was created?

Kernel is assumed compromised Need a secure place for security features and key storage

## Slide 50

###### VBS Security Features

Credential Guard

Hypervisor-Protected Code Integrity (aka. HVCI) System Guard Secure Launch

Shielded VMs

And more!

## Slide 51

###### Windows Architecture – Before VBS

**User Mode (Ring 3)**

**Kernel Mode (Ring 0)**

**Hypervisor (Ring -1)**

Process A

Kernel

Process B

Hypervisor

## Slide 52

###### Windows Architecture – After VBS

**User Mode (Ring 3) Kernel Mode (Ring 0)**

**Hypervisor (Ring -1)**

**Normal Mode (VTL0)** Process A Process B

Kernel

Hypervisor

**Secure Mode (VTL1)** Secure Secure Process A Process B

Secure Kernel

## Slide 53

###### VBS Remote Disablement Protection via UEFI Locks

Boot service UEFI variable is used as configuration source instead of Windows Registry

Ignored Used
Registry Key
Winload.efi
VbsPolicy

NV|BS UEFI Variable
VbsPolicy

## Slide 54

###### VBS Remote Disablement Protection via UEFI Locks

Disabling UEFI lock protected feature requires loading a dedicated EFI application that **requires physical approval** to clear the UEFI lock

Ask user to **physically** SecConfig.efi **approve** disablement

Clear lock

**NV|BS UEFI Variable** VbsPolicy

## Slide 55

###### VBS Remote Disablement Protection via UEFI Locks

What will happen if we **invalidate** VBS files? How will VBS react?

**SecureKernel.exe**

**Hvix64.exe**

## Slide 56

VBS Remote Disablement Protection via UEFI Locks

Windows boots normally, abandoning VBS **Even when enforced with UEFI locks!**

**Validate SecureKernel.exe**

**Winload.efi**

**SecureKernel.exe**

Boot normally

**Validation fails**

## Slide 57

###### Demo #2 – Chaining It All Together

**What are we going to see?**

Credential extraction against the most restrictive settings

**Settings**

PPL enabled for LSASS with UEFI lock

Credential Guard enabled with UEFI lock

Windows Defender up and running

**How will it happen?** PPL bypass by reverting the PPLFault patch Credential Guard disablement bypassing UEFI lock

Turning Windows Defender unfunctional

## Slide 58

Demo #2 – What If only Credential Guard Is Bypassed?

**LSASS can not be dumped**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Demo #2
What If only Credential Guard Is Bypassed?
<Cluded>PPLFault.exe -v 766 lsass.dmp
Ba Kup ves not
F n over DLL entrypoint
Benign: C:\Wi \ tAg -egation.dll.bak
yload: PLFaultTemp\ \PPLFault
eholde : C:\PPLFaultTemp\Even
32\devabj.d11
finish.
DOWNDATE
the memor
ating 961
Did not find
```

## Slide 59

###### Demo #2 – What If only PPL Is Bypassed?

###### **Credentials are encrypted**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Demo #2 —
What If only PPL Is Bypassed?
uthentication Id : @ ; 466417 (@9ee0000:00071dT1)
: Interactive from 1
fcastle
DEKU
DEKU-DC
7/5/2024 12:13:63 PM
§-1-5-21-1272771627 -2707523857 -1367165163-1103
[66600003] Primary
* Username : fcastle
* Domain : DEKU
* LSA Isolated Data: NtlmHash
KdfContext: db@f131340c395ea798ee6896T146184b1cO8abdd3b7F56a874e4383560905a4
Tag : 197edS5S5ab8cal42dde67c9f8ccc38e93
AuthData : sleeeeeeeRgeeRgeRRSsRBREReEoREReRE 1 ERGR00340000004e746c6d48617368
Encrypted : 9c6@1dc3c53f49df535bee643ddf5fcf6ee5icb703e6ddtf8e32bal9F452d2852634daecee854eF3196c32ccc661958daffa296816
TS2OSOTZSOSTTTES 7 DeSbebSsbasUcasy
DOWNDATE
wdigest : KO a a
kerberos : Ly Ld
Ap Ay
* Username : fcastle
= Domain : DEKU.LOCAL
* Password : (null) |
ssp
credman
cloudap
```

## Slide 60

Demo #2

## Slide 61

###### VBS Security Boundaries

**Attacker** **<u>starting</u> point Normal Mode (VTL0)** Process A Process B

**User Mode (Ring 3)**

Kernel

**Kernel Mode (Ring 0)**

**Hypervisor (Ring -1)**

Hypervisor

**Security Boundaries:** VTL0 → VTL1 RING3/0 → RING -1

**Secure Mode (VTL1)** Secure Secure Process A Process B

Secure Kernel

## Slide 62

###### VBS Downgrades Goals

Understand if downgrade mitigation exists in the virtualization stack components

Aim to downgrade to vulnerable code Major downgrade without vulnerable code is still a vulnerability

## Slide 63

VBS Target – Isolated User Mode

**Attacker** **<u>starting</u> point Normal Mode (VTL0) User Mode** Process A Process B **(Ring 3)**

**Secure Mode (VTL1)** Secure Secure Process A Process B

Kernel

Secure Kernel

**Kernel Mode (Ring 0)**

Hypervisor

**Hypervisor (Ring -1)**

## Slide 64

Targeting Credential Guard Isolated User Mode Process

Implemented in Ring3-VTL1 as an Isolated User Mode process **LsaIso.exe**

LsaIso.exe contains secrets instead of the original Lsass.exe

Lsass.exe proxy authentication through LsaIso.exe

## Slide 65

Bringing CVE-2022-34709 Back To Life – Credential Guard Elevation of Privilege

Vulnerable module is **KerbClientShared.dll (10.0.22000.856)** Downgrading KernClientShared.dll to its vulnerable version worked! Crossed security boundary is Ring3-VTL0 to Ring3-VTL1

KerbClientShared.dll

Windows Update

KerbClientShared.dll

## Slide 66

###### VBS Target – Secure Kernel

**Attacker** **<u>starting</u> point Normal Mode (VTL0) User Mode** Process A Process B **(Ring 3)**

**Secure Mode (VTL1)** Secure Secure Process A Process B

Secure Kernel

Kernel

**Kernel Mode (Ring 0)**

**Hypervisor (Ring -1)**

Hypervisor

## Slide 67

###### Secure Kernel

**SecureKernel.exe** serves as the kernel for Secure Mode (VTL1) Implements security features such as HVCI, HyperGuard and more.

## Slide 68

Bringing CVE-2021-27090 Back To Life – Secure Kernel Elevation of Privilege

Vulnerable module is **SecureKernel.exe (10.0.19041.207)** Downgrading **SecureKernel.exe** with some of its dependencies such as **SKCI.dll** and **CI.dll** worked!

Crossed security boundary is **Ring3-VTL0** to **Ring0-VTL1**

SecureKernel.exe

Windows Update

SecureKernel.exe

## Slide 69

VBS Target – Hyper-V’s Hypervisor

**Attacker** **<u>starting</u> point Normal Mode (VTL0) User Mode** Process A Process B **(Ring 3)**

Kernel

**Kernel Mode (Ring 0)**

**Hypervisor (Ring -1)**

Hypervisor

**Secure Mode (VTL1)** Secure Secure Process A Process B

Secure Kernel

## Slide 70

###### Hyper-V Hypervisor

The Hyper-V hypervisor is **Hvix64.exe** (Intel) or **Hvax64.exe** (AMD) The hypervisor is a standalone micro-kernel – valuable target for downgrade

## Slide 71

Downgrading the Hyper-V Hypervisor to a two-year-old hypervisor

Many Hyper-V Elevation of Privileges have been found in the last two years Microsoft does not share the vulnerable component in the Hyper-V stack I decided to go **two years backward (10.0.22000.282)** to prove the vulnerability Downgrading the hypervisor with its loader **HvLoader.dll** worked!

Crossed security boundary is **Ring3-VTL0** to **Ring -1**

Hvix64.exe

Windows Update

Hvix64.exe

## Slide 72

Demo #3

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
(QO ENG - sul
SF in 4 hours
7/6/2024
```

## Slide 73

###### Downgrade Attacks Implications

Attacker
starting
point Normal Mode Secure Mode
(VTL0) (VTL1)
Secure  Secure
User Mode
Process A Process B
(Ring 3) Process A Process B
Kernel Mode
Kernel Secure Kernel
(Ring 0)
Hypervisor
(Ring -1) Hypervisor

## Slide 74

W I N D O W S D O W N D AT E

#### Windows Update Restoration Vulnerability

## Slide 75

It All Started With Windows.old Windows Quality Updates saves the old operating system in **C:\Windows.old** for restoration purposes

**old Windows OS**

**C:\Windows.old**

## Slide 76

Can Windows.old contents be tampered with?

Access lists are copied from the old OS

**It is impossible to temper with files that could not be previously tampered with**

**old Windows OS**

**C:\Windows.old**

**Unprivileged Attacker**

**Can not access old files**

## Slide 77

###### Can Windows.old be tampered with?

Unprivileged users have **full access** to C:\Windows.old itself!

**old Windows OS**

Unprivileged Attacker

**C:\Windows.old**

**Full access**

## Slide 78

###### Exploitation Strategy

Attacker can rename C:\Windows.old and re-create an attacker-controlled Windows.old

As a result, the attacker-controlled OS is used in case of update restoration!

Unprivileged Attacker

1. Rename
Windows.old

2. Create attacker
controlled
Windows.old

old Windows OS
Attacker Windows OS

C:\Old-Windows.old

**C:\Windows.old**

## Slide 79

W I N D O W S D O W N D AT E

## Closing Remarks

## Slide 80

###### Responsible Disclosure and CVE

We responsibly disclosed all the research findings to Microsoft in February 2024

Microsoft issued **CVE-2024-21302**

## Slide 81

###### Microsoft’s Official Response

We appreciate the work of SafeBreach in identifying and responsibly reporting this vulnerability through a coordinated vulnerability disclosure. We are actively developing mitigations to protect against these risks while following an extensive process involving a thorough investigation, update development across all affected versions, and compatibility testing, to ensure maximized customer protection with minimized operational disruption.

## Slide 82

Next Steps Are there additional Windows features vulnerable to downgrade attacks? Linux Virtualization-Based Security (LVBS) was introduced, does the same design issues exist in the Linux implementation?

Are other operating systems such as Linux or MacOS vulnerable to downgrade attacks?

## Slide 83

###### Takeaways

Awareness and mitigations against OS downgrade attacks

## Slide 84

###### Takeaways

Design must be regarded as a relevant attack surface

## Slide 85

###### Takeaways

Thoroughly examine and expand in-the-wild attacks

## Slide 86

###### Credits

James Forshaw **@tiraniddo**

Saar Amar **@AmarSaar**

Gabriel Landau **@GabrielLandau**

Valentina Palmiotti Ruben Boonen **@chompie1337 @FuzzySec** Benjamin Delphi **@gentilkiwi**

**CVE-2022-34709**

**CVE-2021-27090**

###### **PPLFault**

**CVE-2023-21768 Exploit**

**Mimikatz**

## Slide 87

###### Thank You!

**@_0xDeku linkedin.com/in/alonleviev alon.leviev@safebreach.com**
