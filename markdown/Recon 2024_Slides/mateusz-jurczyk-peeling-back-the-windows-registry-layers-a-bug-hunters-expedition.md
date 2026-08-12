---
title: "Peeling Back the Windows Registry Layers A Bug Hunter's Expedition"
speakers: ["Mateusz Jurczyk"]
conference: "REcon"
conference_full: "REcon 2024"
edition: ""
year: 2024
source_pdf: "Recon 2024_Slides/Mateusz Jurczyk_Peeling Back the Windows Registry Layers A Bug Hunter's Expedition.pdf"
pages: 96
sha256: "2e1c28912fa61d70c4e874f69874c3c59d7f86c5acd63787730569a116708935"
text_chars: 41881
ocr_pages: 14
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:30:13Z"
---
# Peeling Back the Windows Registry Layers A Bug Hunter's Expedition

**Speakers:** Mateusz Jurczyk  
**Conference:** REcon 2024  
**Source:** `Recon 2024_Slides/Mateusz Jurczyk_Peeling Back the Windows Registry Layers A Bug Hunter's Expedition.pdf` (96 pages)

## Slide 1

Peeling Back the Windows Registry Layers: A Bug Hunter's Expedition

Mateusz Jurczyk REcon, June 2024

## Slide 2

# The registry fundamentals

- A hierarchical database for storing system/application settings in Windows

- Essential concepts: **hives** , **keys** and **values**

- Built-in tools for management: **Regedit.exe** (GUI), **Reg.exe** (CLI)

- Documented Registry API for software developers

- Most of the implementation is in the kernel

## Slide 3

# A bit of history

- First introduced in **Windows 3.1** (1992) to replace INI files

- Current code and design directly rooted in **Windows NT 3.1** (1993) and **Windows NT 4.0** (1996)

- Started out small, then extended and improved over the next 30 years

   - Performance improvements: _faster subkey lookups, optimized key renaming_

   - Backwards compatibility: _registry virtualization_

   - New features: _big values, registry callbacks, transactions, application hives, differencing hives_

## Slide 4

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Ei My Computer
(9) HKEY_CLASSES_ROOT
HKEY_CURRENT_USER
f#-) Windows NT
-() UNICODE Program Groups
(2) HKEY_LOCAL_MACHINE
wy HKEY_USERS
mC) HKEY_CURRENT_CONFIG
~{() HKEY_DYN_DATA
[ab] (Default)
CompletionChar
DefaultColor
EnableE xtensions
(value not set)
000000000 (0)
000000000 (0)
000000001 (1)
Editor
```

## Slide 5

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
fic Registry Editor
File Edit View Favorites Help
Computer\HKEY_CURRENT_USER\Control Panel\Cursors
v @ computer
> HKEY_CLASSES_ROOT
bd HKEY_CURRENT_USER
> AppEvents
> Console
Y Control Panel
> Accessibility
> Appearance
> Bluetooth
Colors
Cursors
> Desktop
> Input Method
> International
Keyboard
Mouse
NotifylconSettings
Personalization
PowerCfg
Quick Actions
Sound
> TimeDate
UnsupportedHardwareNotificationCache
Environment
> EUDC
> Keyboard Layout
> Network
> Printers
> Software
Name
a8|(Default)|
ab|AppStarting
ablArrow
88|ContactVisualiza...
ab)Crosshair
§\CursorBaseSize
ab Hand
at)Help
2>|IBeam
ab)No
ab |NWPen
88|Scheme Source
ab)sizeAll
ab)sizeNESW
ab)sizeNS
ab|sizeNWSE
ab)sizeWE
ab)UpArrow
ab |Wait
estureVisualizat...
Type
REG_SZ
REG_SZ
REG_SZ
REG_DWORD
REG_SZ
REG_DWORD
REG_DWORD
REG_SZ
REG_SZ
REG_SZ
REG_SZ
REG_SZ
REG_DWORD
REG_SZ
REG_SZ
REG_SZ
REG_SZ
REG_SZ
REG_SZ
REG_SZ
Data
Windows Default
C:\Windows\cursors\aero_working.ani
C:\Windows\cursors\aero_arrow.cur
0x00000001 (1)
0x00000020 (32)
0x0000001f (31)
C:\Windows\cursors\aero_link.cur
C:\Windows\cursors\aero_helpsel.cur
C:AWindows\cursors\aero_unavail.cur
C:AWindows\cursors\aero_pen.cur
0x00000002 (2)
C:\Windows\cursors\aero_move.cur
C:\Windows\cursors\aero_nesw.cur
C:\Windows\cursors\aero_ns.cur
C:\Windows\cursors\aero_nwse.cur
C:\Windows\cursors\aero_ew.cur
C:AWindows\cursors\aero_up.cur
C:AWindows\cursors\aero_busy.ani
```

## Slide 6

Lines of decompiled kernel code

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Lines of decompiled kernel code
Lines of code
100000
90000
80000
70000
60000
50000
40000
30000
20000
10000
Windows version
```

## Slide 7

# Registry as an attack surface: the good

Ability to load custom hives as an unprivileged user

Access to sensitive data: system configuration, user credentials

Error prone parts of the design: self-healing, size-bound, heavily optimized A mixture of complex C code from different eras: from 30 years ago to now A variety of potential bug classes and attack vectors

## Slide 8

# Registry as an attack surface: the bad*

Very hard to fuzz effectively

Source code not available, and documentation is poor for specific areas

Public symbols incomplete, lack some type definitions

Lots of reverse engineering required: significant time and energy investment Not all bugs are good, as usual

## Slide 9

# How the research started

- Started in May 2022 as a test of my new coverage-based fuzzer for the Windows kernel

- Found one bug: **CVE-2022-35768**

   - _Windows Kernel multiple memory problems when handling incorrectly formatted security descriptors in registry hives_

- The initial success prompted me to have a deeper look into the kernel

- It quickly turned into a challenge to reverse and review _all_ of the code...

## Slide 10

The research process
Test, reproduce, report bugs
Reverse engineer 04
Test any discovered bugs, create reliable
Choose a self-contained part of the registry  reproducers, write up detailed reports and
implementation and try to get it as close to  submit them to Microsoft.
readable C-like code as possible.
01 03
Understand the logic
Compare with prior
Try to understand the purpose,  knowledge
assumptions, guarantees and underlying
intentions of the code. 02 Consider if the behavior of the feature is
consistent with what we already know
about the registry.

## Slide 11

# Research progression: major features

Hive loading
Basic operations
Registry virtualization
Transactions
Differencing hives
Registry callbacks

## Slide 12

# How it went

- The audit lasted for ~20 months between May 2022 – December 2023

- ● Results:

   - **39 issues** reported in the Project Zero bug tracker (under a 90 day deadline)

   - **20 issues** reported outside the tracker (no deadline, low/unclear severity)

   - **= 50 CVEs** assigned by Microsoft across 15 monthly bulletins

## Slide 13

# Bug classes

Kernel-specific
Windows Registry
bugs
File parsing
Logic bugs
bugs
Object lifetime
bugs

## Slide 14

<u>https://bugs.chromium.org/p/project-zero/issues/list?q=finder%3Amjurczyk%20opened%3E2022-05-01%20opened%3C2024-01-01&can=1</u>

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ID + Status ~ Restrict ~ Reported ~ Vendor ~ Product ~ Finder ~ Summary + Labels ~
2295 Fined - 2022May-11 Microsoft Kemel rmjurezyk Windows Kernel use-afterfree due to refcount overfiow in registry hive security descriptors CCProjectZeroMembers
2297 Fixed 2022May-17 Microsoft Kemel mjurezyk Windows Kernel invalid read/write due to unchecked Blink cell index in root security descriptor CCProjectZeroMembers
2299 Fined = 2022May:20 Microsoft Kernel rmjurczyk Windows Kerne! multiple memory problems when handling ly formatted security descriptors in registry hives OO
2318 Fixed ~ 2022Jun-22 Microsoft Kernel rmjurczyk Windows Kernel integer overflows in registry subkey lists leading to memory corruption CCProjectZeroMembers
2330 Fined ~ 2022JuK8 Microsoft Kernel rmiurezyk Windows Kemel registry use-fterfree due to bad handling of failed reallocations under memory pressure CCProjectZeroMembers
2332 Fined - 2022Jul11 Microsoft Kernel rmjurczyk Windows Kernel memory corruption due to type confusion of subkey index leaves in registry hives CcProjectZeroMembers
2341 Fed - 2022-Aug3 Microsoft —_Kemel rjurczyk Windows Kerne! multiple memory corruption issues when operating on very long registry paths CCProjectZeroMembers
2344 Fired es 2022-AugS Microsoft Kernel rmjurczyk Windows Kernel out of-bounds reads and other issues when operating on long registry key and value names CCProjectZeroMembers
2359 Fixed = 2022Sep:22 Microsoft —_Kemel rmjurczyk Windows Kemet due to bad handling ofp keys in NtNotifyci ocr
2366 Fixed _ 2022-0ct6 Microsoft Kernel rmjurczyk Windows Kernel memory dueto handling of keys in registry cc
2369 Fixed — 2022-0ct'13. Microsoft Kernel rmiurczyk Windows Kernel use-afterfree due to dangling registry link node under paged pool memory pressure CCProjectZeroMemibers
2375 Fined - 2022-0ct25 Microsoft —_Kemel rmjurczyk Windows Kernel multiple issues in the key replication feature of registry virtualization CoProjectZeroMembers
2378 Fined - 2022-0ct31 Microsoft —_Kemel mjurezyk Windows Kernel registry SID table poisoning leading to bad locking and other issues CcProjectZeroMemibers
2379 Fed = 2022Nov2 Microsoft Kernel mjurczyk Windows Kernel allows deletion of keys in vrtualizable hives with KEY_READ and KEY_SET_VALUE access rights CCProjectZeroMembers
2389 Fixed - 2022Nov30 Microsoft Kernel rmjurczyk Windows Kernel registry with leading to hive state and memory corruption C1
2392 Fined a” 2022.0ec7 Microsoft Kernel rmjurczyk Windows Kernel multiple issues with subkeys of transactionally renamed registry keys COProjectZeroMembers
2394 Fined - 2022-0e0-14 Microsoft —_Kemel rjurczyk Windows Kernel multiple issues in the prepare/commit phase ofa transactional registry key rename CoProjectZeroMembers
2408 Fixed - 2023-Jan-13 Microsoft —_Kemel mjurczyk Windows Kernel insufficient validation of new registry key names in transacted NtRenameKey CCProjectZeroMembers
2610 Fixed a 2023Jan-19 Microsoft Kernel rmjurcayk Windows Kermel CmpCleanupLightWeightPrepare registry security descriptor refcount leak leading to UAF CCProjectZeroMembers
2618 Fixed = 2023Jan31 Microsoft Kernel rmjurczyk Windows Kernel disclosure of kernel pointers and uninitialized memory through registry KTM transaction log files CCProjectZeroMembers
2419 Fixed - 2023Feb-2 — Microsoft Kernel rmjurczyk Windows Kernel out-of bounds reads when operating on invalid registry paths in CmpDoReD« /ompDoReOpenTransKey cc
2433 Fined - 2023Mar7 Microsoft Kernel mjurcayk Windows Kernel KTM registry transactions may have non-atomic outcomes CCProjectZeroMembers
2445 Fined - 2023-Apr-19 Microsoft —_Kemel rmjurczyk Windows Kernel arbitrary read by accessing pr keys through ng hives CCProject
2446 Fed - 2023-Apr-20 Microsoft Kernel ‘mjurczyk Windows Kernel may reference unbacked layered keys through registry virtualization CCProjectZeroMembers
2487 Fined = 2023-Apr27 Microsoft Kernel rmjurcayk Windows Kernel may reference rolled back keys through 1g hives CoProject
2449 Fined - 2023May2 Microsoft Kernel mjurczyk Windows Kemel renaming layered keys doesnt reference count security descriptors, leading to UAF CProjectZeroMembers
2452 Fined - 2023May-10 Microsoft Kernel rmjurczyk Windows Kernel CmDeleteLayeredKey may delete predefined tombstone keys, leading to security descriptor UAF COProjectZeroMembers
2454 Fed - 2023May-15 Microsoft —_Kemel mjurezyk Windows Kernel outof-bounds reads due to an integer overflow in registry LOG file parsing CcProjectZeroMembers
2456 Fined - 2023May-22 Microsoft _Kemel mjurczyk Windows Kernel partial success of registry hive log recovery may lead to inconsistent state and memory corruption CcProjectZeroMemibers
2457 Fixed - 2023May-31 Microsoft Kem! rmjurcayk Windows Kernel doesnt reset security cache during sel healing leading to refcount overflow and UAF CCProjectZeroMembers
2462 Fined - 2023Jun-26 Microsoft Kernel rmiurezyk Windows Kernel passes user-mode pointers to registry callbacks, leading to race conditions and memory commuption CCProjectZeroMembers
2463 Fined - 2023Jun-27 Microsoft Kernel rjurczyk Windows Kernel paged pool memory disclosure in VipPostEnumerateKey CCProjectZeroMemibers
2464 Fixed - 2023-Jun-27 Microsoft —_Kemel rmjurczyk Windows Kernel out-f-bounds reads and paged pool memory disclosure in VipU Proj
2466 Fixed - 2023-Jul7 Microsoft —_Kemel mjurczyk Windows Kernel containerized registry escape through integer overflows in and other CoProject
2479 Fixed - 2023-Aug-10 Microsoft Kernel rmjurczyk Windows Kemmel time of-check/time-of-use issue in verifying layered key security may lead to information disclosure from privileged registry keys CCProjectZeroMembers
2480 Fixed = 2023-Aug22 Microsoft Kernel rmjurcayk Windows Kernel bad locking in registry virtualization leads to race conditions CCProjectZeroMember
2492 Fined ~ 2023.0ct Microsoft Kernel rmjurczyk Windows registry predefined keys may lead to confused deputy problems and local privilege escalation CCProjectZeroMembers
https://bugs.chromium.org/p/project-zero/issues/list?q=finder%3Amjurczyk%200pened%3E2022-05-01%200pened%3C2024-01-01&can=1
```

## Slide 15

<u>https://github.com/googleprojectzero/p0tools/tree/master/WinRegLowSeverityBugs</u>

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Microsoft Windows Registry Low/Unclear Severity Bugs
This repository contains the descriptions and proof-of-concept exploits of 20 issues with low or unclear security impact found in the Windows
Registry. They were reported to Microsoft between November 2023 and January 2024. Six of them were fixed by the vendor in the March 2024
Patch Tuesday, while the other fourteen were closed as WontFix/vNext. The bugs were identified during my registry research in 2022-2024,
alongside the 39 vulnerabilities filed in the Project Zero bug tracker with the 90-day deadline.
For more information about the research, please see the blog post series starting with The Windows Registry Adventure #1: Introduction and
research results, as well as the Exploring the Windows Registry as a powerful LPE attack surface presentation from BlueHat Redmond 2023. At
the time of this writing, further talks about the registry are planned this year at OffensiveCon, CONFidence and REcon.
The issues are summarized in the table below:
ID Title Status CVE
Windows Kernel out-of-bounds read of key node security in oe CVE-2024-
i 7 _ Fixed in March 2024
CmpValidateHiveSecurityDescriptors when loading corrupted hives 26174
CVE-2024-
Windows Kernel out-of-bounds read when validating symbolic links in CmpCheckValueList Fixed in March 2024 me
Windows Kernel pool-based buffer overflow when parsing deeply nested key paths in
<< = WontFix/vNext
(CmpComputeComponentHashes
Windows Kernel allows the creation of stable subkeys under volatile keys via registry we CVE-2024-
aS Fixed in March 2024
transactions 26173
Windows Kernel lightweight transaction reference leak in CmpTransReferenceTransaction WontFix/vNext
Windows Kernel pool-based out-of-bounds read in CmpRmReDoPhase when restoring
. WontFix/vNext
registry transaction logs
Windows Kernel NULL pointer dereference in CmpLightWeightPrepareSetSecDescUoW WontFix/vNext
Windows Kernel infinite loop in CmpDoReOpentransKey when recovering a corrupted vNext (fixed in Insider
transaction log Preview)
Windows Kernel NULL pointer dereference in NtDeleteValueKey WontFix
Windows Kernel user-triggerable crash in CmpKeySecurityIncrementReferenceCount via
WontFix/vNext
unreferenced security descriptors
Windows Kernel memory leak in VrpPostOpenOrCreate when propagating error
https://github.com/googleprojectzero/p0tools/tree/master/WinRegLowSeverityBugs
```

## Slide 16

# Lessons learned

- Software continues to have bugs

- Different bugs lie at different points on the code understanding scale

- Security research is akin to peeling back the layers of an onion

## Slide 17

# A taxon(ion)omy of bugs

Level of context required
(easiest to hardest to find?)

## Slide 18

# A taxonomy of bugs

 Logic bugs
 Cross-feature bugs
 Object-lifetime bugs
4. Concurrency-related bugs
5. Cross-function bugs
6. Local bugs of omission
7. Information disclosure
8. Obvious, local bugs
9. Greppable
10. Fuzzable

## Slide 19

# A taxonomy of bugs

 Logic bugs
 Cross-feature bugs
 Object-lifetime bugs
4. Concurrency-related bugs
5. Cross-function bugs
6. Local bugs of omission
7. Information disclosure
8. Obvious, local bugs
9. Greppable
10. Fuzzable

## Slide 20

# Fuzzable bugs

- Virtually zero knowledge of the target required, only its behavior and examples of inputs:

   - How to build it (optional)

   - How to run it and pass input data

   - How it fails/crashes

## Slide 21

# Registry fuzzing – easy in theory

- Hives are a binary format

- Input samples readily available in Windows

- Initial harness easy to write

   - RegLoadAppKey + RegCloseKey

- Simple bug detection

   - Catching BSoDs / unexpected reboots

## Slide 22

# Registry fuzzing – hard in practice

- Hives are a binary format

- ● Input samples readily available in Windows

- Initial harness easy to write

   - RegLoadAppKey + RegCloseKey

- Simple bug detection

   - Catching BSoDs / unexpected reboots

## Slide 23

# Registry fuzzing – hard in practice

   - Structurally very simple

- ~~Hives are a binary format~~

- Input samples readily available in Windows

      - Most interesting bugs occur on a higher level

      - Bitflipping can only trigger the lowest hanging fruit

- Initial harness easy to write

   - RegLoadAppKey + RegCloseKey

- Simple bug detection

   - Catching BSoDs / unexpected reboots

## Slide 24

# Registry fuzzing – hard in practice

- ~~Hives are a binary format~~

- ~~Input samples readily available in Windows~~

      - Default hives don't contain any interesting/non-standard constructs

- Initial harness easy to write

   - RegLoadAppKey + RegCloseKey

- Simple bug detection

   - Catching BSoDs / unexpected reboots

## Slide 25

# Registry fuzzing – hard in practice

- ~~Hives are a binary format~~

- ~~● Input samples readily available in Windows~~

- ~~Initial harness easy to write~~

- ~~RegLoadAppKey + RegCloseKey~~

- ● Simple bug detection

   - This only covers a very small part of the registry

   - Dozens of other operations required to properly test the code

- Catching BSoDs / unexpected reboots

## Slide 26

# Registry fuzzing – hard in practice

- ~~Hives are a binary format~~

- ~~● Input samples readily available in Windows~~

- ~~Initial harness easy to write~~

- ~~RegLoadAppKey + RegCloseKey~~ Most registry bugs don't trigger hard crashes

- ~~● Simple bug detection~~

      - Hive memory corruption

   - ~~Catching BSoDs / unexpected reboots~~ ● Logic bugs

## Slide 27

# Registry fuzzing – hard in practice

- This might explain why only 1 bug was fuzzed out

   - Miscalculation of a security descriptor buffer size

   - Trivial leak of OOB kernel pool data into the hive file

   - Likely wouldn't have been found manually

- ... and why the other 49 survived for so long

## Slide 28

CVE-2022-35768
RtlLengthSecurityDescriptor( Header Owner Group Sacl Dacl ) =
buffer size = sum of components

## Slide 29

CVE-2022-35768
RtlLengthSecurityDescriptor( Header Owner Group Sacl Dacl ) =  too large
RtlLengthSecurityDescriptor( Header Owner Group Sacl Dacl ) =  too small

## Slide 30

# A taxonomy of bugs

 Logic bugs
 Cross-feature bugs
 Object-lifetime bugs
4. Concurrency-related bugs
5. Cross-function bugs
6. Local bugs of omission
7. Information disclosure
8. Obvious, local bugs
9. Greppable
10. Fuzzable

## Slide 31

# Patterns for grepping

- General:

   - Buffer operations: calls to **memcpy** etc.

   - Dynamic allocations: calls to **malloc** etc.

   - Integer arithmetic: especially next to allocations, on 16-bit types etc.

- Kernel-specific:

   - Pointer probing: **ProbeForRead** / **ProbeForWrite** calls, references to **MmUserProbeAddress**

- Registry-specific:

   - Calls to the hive allocator: **HvAllocateCell** , **HvReallocateCell** , **HvFreeCell**

   - Operating on key handles: references to **CmKeyObjectType**

## Slide 32

# Example: long strings

- Under certain circumstances*, registry paths may be over 64 KiB long

- ● Windows stores strings, including registry paths, in UNICODE_STRING

   - 16-bit Length and MaximumLength fields

- Manually calculating the unicode buffer size may indicate insecure code

- Relatively easy to grep for 16-bit arithmetic in x86 assembly:

(add|sub)\s+[a-z][xi],

## Slide 33

# Examples

CmpVEExecuteVirtualStoreParseLogic (CVE-2022-38038)

CmRealKCBToVirtualPath (CVE-2022-37990)

CmpDoWritethroughReparse (CVE-2022-38039)

VrpBuildKeyPath (CVE-2023-36576)

## Slide 34

# A taxonomy of bugs

 Logic bugs
 Cross-feature bugs
 Object-lifetime bugs
4. Concurrency-related bugs
5. Cross-function bugs
6. Local bugs of omission
7. Information disclosure
8. Obvious, local bugs
9. Greppable
10. Fuzzable

## Slide 35

# Obvious, local bugs

- Disclaimer: often "obvious" only after hours of reversing

- Typical root causes:

   - Evident out-of-bounds array accesses

   - Incorrect allocation size

   - Incorrect return value

   - Incorrect reference counting

- Most frequent bug class in the research: **13 of 50**

## Slide 36

# Example (CVE-2022-34707)

BOOLEAN CmpCheckAndFixSecurityCellsRefcount(CMHIVE *CmHive) { ... for (int i = 0; i < CmHive->SecurityCount; i++) { CM_KEY_SECURITY_CACHE_ENTRY *CacheEntry = &CmHive->SecurityCache[i];

CM_KEY_SECURITY *SecurityNode           = CmHive->Hive.GetCellRoutine(CmHive, CacheEntry->Cell);

if (SecurityNode->ReferenceCount < CacheEntry->CachedSecurity->RealRefCount) { SecurityNode->ReferenceCount = CacheEntry->CachedSecurity->RealRefCount; } }

... }

## Slide 37

# Example (CVE-2022-34707)

What about inadequately large refcounts?

BOOLEAN CmpCheckAndFixSecurityCellsRefcount(CMHIVE *CmHive) { ... for (int i = 0; i < CmHive->SecurityCount; i++) { CM_KEY_SECURITY_CACHE_ENTRY *CacheEntry = &CmHive->SecurityCache[i]; CM_KEY_SECURITY *SecurityNode           = CmHive->Hive.GetCellRoutine(CmHive, CacheEntry->Cell); if (SecurityNode->ReferenceCount < CacheEntry->CachedSecurity->RealRefCount) { SecurityNode->ReferenceCount = CacheEntry->CachedSecurity->RealRefCount; } } ... }

## Slide 38

# CVE-2022-34707

- The bug lead to a refcount integer overflow, and a security descriptor use-after-free in the hive mapping

   - A registry-specific memory corruption primitive that hasn't been explored before

- With some work, it can be converted to a KASLR leak and arbitrary read/write

- For details, see my latest OffensiveCon talk on exploitation

## Slide 39

Demo

## Slide 40

# A taxonomy of bugs

 Logic bugs
 Cross-feature bugs
 Object-lifetime bugs
4. Concurrency-related bugs
5. Cross-function bugs
6. Local bugs of omission
7. Information disclosure
8. Obvious, local bugs
9. Greppable
10. Fuzzable

## Slide 41

# Kernel information disclosure

- Disclosing uninitialized kernel stack/pool memory: partially filled arrays, padding structure bytes etc.

- _Could be_ fuzzable or greppable, but it's harder, hence its own category

   - Never triggers a system crash, requires a dedicated detector (e.g. Bochspwn Reloaded)

   - Doesn't stand out when reading the code

- Enables a local attacker to leak kernel addresses or other system secrets

## Slide 42

# Examples

- **Issue 2418** (CVE-2023-28271)

   - The kernel directly saved a kernel structure with pointers and padding bytes to a file

   - Required the use of transactions and observing that the log files are user-readable

- **Issue 2463** (CVE-2023-38140)

   - In principle, a standard kernel memory disclosure bug

   - Existed in a very specific code path, required layered keys and invoking a system call directly

## Slide 43

Demo

## Slide 44

Logic bugs
 Cross-feature bugs
 Object-lifetime bugs
4. Concurrency-related bugs
5. Cross-function bugs
6. Local bugs of omission
7. Information disclosure
8. Obvious, local bugs
9. Greppable
10. Fuzzable

# A taxonomy of bugs

## Slide 45

# Local bugs of omission

- Bugs that are local in scope, but caused by something that is _not_ in the code

- Require a different mindset to identify

   - Consider whether a function does everything it should be doing in every code path

- Good candidates:

   - Missing bounds/correctness checks of some structure fields

   - Missing handling of specific object types in generic functions

   - Missing return value checks

   - Missing state unwinding in error code paths

## Slide 46

# Example (CVE-2023-28248)

VOID CmpCleanupLightWeightUoWData(CM_KCB_UOW *UoW) { switch (UoW->ActionType) { // // Other action types... //

Missing security descriptor dereference

case UoWSetSecurityDescriptor: CM_UOW_SET_SD_DATA *SecurityData = UoW->SecurityData; +     CmpDereferenceSecurityNode(SecurityData->Hive, SecurityData->SecurityCell); ExFreePoolWithTag(SecurityData, 'wUMC'); break; }

}

## Slide 47

# Example (CVE-2023-28248)

- A functionality-neutral issue

- Virtually impossible to find without careful analysis of the logic of the function

- ● Outcome:

   - The missing call leads to a leak of a single reference

   - The security descriptor refcount is a uint32, and can be incremented multiple times

   - There is no overflow protection, and once the value overflows, we get a UAF

- The proof-of-concept takes ~20 hours to complete

## Slide 48

Demo

## Slide 49

Logic bugs
 Cross-feature bugs
 Object-lifetime bugs
4. Concurrency-related bugs
5. Cross-function bugs
6. Local bugs of omission
7. Information disclosure
8. Obvious, local bugs
9. Greppable
10. Fuzzable

# A taxonomy of bugs

## Slide 50

# Cross-function bugs

- Bugs that are rooted in (mis)interactions between two or more functions

- Examples observed in the registry:

   - Assumption that certain internal functions never fail

   - Assumption that a failed call implies no internal state change

   - Confusion about what success/failure even means

   - Using the wrong function for the wrong task

## Slide 51

# Example (CVE-2023-23423)

NTSTATUS CmpCommitRenameKeyUoW(CM_KCB_UOW *UoW) { // ...

if (!CmpAddSubKeyEx(Hive, ParentKey, NewNameKey) || !CmpRemoveSubKey(Hive, ParentKey, OldNameKey)) { -   CmpFreeKeyByCell(Hive, NewNameKey); +   HvFreeCell(Hive, NewNameKey); return STATUS_INSUFFICIENT_RESOURCES; }

Deep vs. shallow free

// ... }

## Slide 52

# Successful rename case

"OldName" key
Class SecurityDescriptor Value list
Value Value Value

## Slide 53

Successful rename case
"OldName" key "NewName" key
Class SecurityDescriptor Value list
Value Value Value

# Successful rename case

## Slide 54

Successful rename case
"OldName" key "NewName" key
Class SecurityDescriptor Value list
Value Value Value

# Successful rename case

## Slide 55

# Failed rename case (correct)

"OldName" key
Class SecurityDescriptor Value list
Value Value Value

## Slide 56

# Failed rename case (correct)

"OldName" key "NewName" key
Class SecurityDescriptor Value list
Value Value Value

## Slide 57

# Failed rename case (correct)

"OldName" key "NewName" key
Class SecurityDescriptor Value list
Value Value Value

## Slide 58

# Failed rename case (buggy)

"OldName" key
Class SecurityDescriptor Value list
Value Value Value

## Slide 59

# Failed rename case (buggy)

"OldName" key "NewName" key
Class SecurityDescriptor Value list
Value Value Value

## Slide 60

# Failed rename case (buggy)

"OldName" key "NewName" key
Class SecurityDescriptor Value list
Value Value Value

## Slide 61

Logic bugs
 Cross-feature bugs
 Object-lifetime bugs
4. Concurrency-related bugs
5. Cross-function bugs
6. Local bugs of omission
7. Information disclosure
8. Obvious, local bugs
9. Greppable
10. Fuzzable

# A taxonomy of bugs

## Slide 62

# Race conditions

- Bugs that require an understanding of how global state can be manipulated in different code paths at the same time

- General problem types:

   - Missing synchronization of access to a resource

   - Bad synchronization: _shared_ vs. _exclusive_ access

   - Bad synchronization: locking the wrong thing **(two registry reports)**

   - Interactions with user-mode memory: double fetches etc. **(one registry report)**

## Slide 63

Example (CVE-2023-38141)

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Example (CVE-2023-38141)
Issue 2462: Windows Kernel passes user-mode pointers to registry callbacks, leading to race conditions and memory corruption :
Reported by mjurczyk@google.com on Mon, Jun 26, 2023, 3:13 PMGMT+2 =e
The Windows operating system exposes a documented kernel API named Registry Callbacks. It allows drivers and the kernel itself to
register callback functions using CmRegisterCallbackEx, which then get invoked every time a registry operation takes place in the
system. The callbacks are provided with full information about the type and context of the operations through the REG_NOTIFY_CLASS enum
and one of the many corresponding REG_*_INFORMATION structures. Based on this data, the callbacks can decide whether to act on it - for
example log the operation, block it, adjust the output data, or intercept it and bypass the Configuration Manager completely. One
obvious use case for this interface is antivirus-like software, but it is also utilized by the core Windows kernel as well, e.g. to
implement the namespace redirection feature of the VRegDriver (part of containerized registry support for app/server silos), or for ETW
logging of registry activity.
There is a fundamental weakness in the way the callback support is currently implemented: many of the operation-specific structures
contain pointers to input/output data, and in some cases, these fields point directly to user-mode buffers passed to the registry
syscalls as arguments by client applications. This fact is documented in the specification of the registry callback function [1].
According to MSDN, input buffer pointers are safe to use because they are captured by the kernel before being passed to the callbacks on
modern versions of Windows (8 and newer), while output buffer pointers are always potentially unsafe and must be accessed within
try/except blocks and/or captured in kernel-mode memory before passing them to other kernel functions.
However, there are two issues here:
```

## Slide 64

# Registry callbacks?

_Kernel-mode_

_User-mode_

Client program

Registry Pre callbacks Post callbacks operation exit syscall exit syscall enter syscall Client program

## Slide 65

Operating on input/output pointers

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Operating on input/output pointers
Buffer type Windows Buffer pointer Safe for callback Safe to pass to system routines (such as
version passed to callback routine todirectly ZwOpenKey)?
routine access?
User-mode Windows 8 Points to captured Yes Yes
input and later data.
User-mode Windows 7 Points to captured No. Must read No. Must allocate kernel memory, copy data
input and earlier data or original under try/except. from the original buffer under try/except, and
user-mode buffer. pass the copied data to the system routine.
User-mode All Points to original No. Must write No. Must allocate kernel memory, pass kernel
output user-mode buffer. under try/except. memory to the system routine, and copy the
results back to the original buffer under
try/except.
Kernel-mode_ All Points to original Yes Yes
input and kernel-mode buffer.
output
```

## Slide 66

# Operating on input/output pointers

Problem #1: untrue for some operations:
●
SetInformationKey
●
QueryMultipleValueKey

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Operating on input/output pointers
Problem #1: untrue for some operations:
Buffer type Windows Buffer pointer Safe for cal .
version passed to callback _ routine tod 0 SetInformationKey
routine e QueryMultipleValueKey
User-mode Windows 8 Points to captured Yes
input and later data.
User-mode Windows 7 Points to captured No. Must read No. Must allocate kernel memory, copy data
input and earlier data or original under try/except. from the original buffer under try/except, and
user-mode buffer. pass the copied data to the system routine.
User-mode All Points to original No. Must write No. Must allocate kernel memory, pass kernel
output user-mode buffer. under try/except. memory to the system routine, and copy the
results back to the original buffer under
try/except.
Kernel-mode_ All Points to original Yes Yes
input and kernel-mode buffer.
output
```

## Slide 67

# Operating on input/output pointers

Problem #1: untrue for some operations
●
SetInformationKey
●
QueryMultipleValueKey
Problem #2: documented, but surprising
even for Windows kernel developers

## Slide 68

Logic bugs
 Cross-feature bugs
 Object-lifetime bugs
4. Concurrency-related bugs
5. Cross-function bugs
6. Local bugs of omission
7. Information disclosure
8. Obvious, local bugs
9. Greppable
10. Fuzzable

# A taxonomy of bugs

## Slide 69

# Object lifetime bugs

- Bugs that require understanding of how objects are created, managed and destroyed in time

   - Temporal violations, typically use-after-free

- In registry, a key's lifetime may be hard to reason about

   - Referenced by a handle in the period between RegOpenKey and RegCloseKey

   - Within that time, many things can happen:

      - The key can be renamed / deleted

      - Its parent key can be renamed

      - The underlying hive can be unloaded

## Slide 70

# Key lifetime challenges

- Challenge 1: renaming keys (NtRenameKey)

   - Very complex, combines the delete + create operation in one

- Challenge 2: uncommitted transactions

- Operations aren't atomic; an intermediate state gets exposed that had previously been hidden

- ● Put the things together: renaming + transactions = Schrödinger's key

   - A single key is simultaneously known by two different names, and its subkeys by two paths

   - The Windows NT-era registry was not designed for this

## Slide 71

# Examples

_All reports fixed collectively in March 2023 by disabling transacted renames_

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Examples
Issue 2392: Windows Kernel multiple issues with subkeys of transactionally renamed registry keys
Reported by mjurczyk@google.com on Wed, Dec 7, 2022, 11:24 AM GMT+1
Issue 2394: Windows Kernel multiple issues in the prepare/commit phase of a transactional registry key rename
Reported by mjurczyk@google.com on Wed, Dec 14, 2022, 5:23 PM GMT+1 (iets
Issue 2408: Windows Kernel insufficient validation of new registry key names in transacted NtRenameKey
Reported by mjurczyk@google.com on Fri, Jan 13, 2023, 2:12 PM GMT+1
All reports fixed collectively in March 2023 by disabling transacted renames
```

## Slide 72

# CVE-2023-23420

1. Open a handle to Parent\OldName\Subkey to create its corresponding KCB

KCB tree

"Parent"
"OldName"
"Subkey"

## Slide 73

# CVE-2023-23420

1. Open a handle to Parent\OldName\Subkey to create its corresponding KCB

2. Transactionally rename "OldName"

KCB tree
"Parent"
"NewName"
"OldName"
(transacted)
"Subkey"

## Slide 74

# CVE-2023-23420

1. Open a handle to Parent\OldName\Subkey to create its corresponding KCB

2. Transactionally rename "OldName"

3. Open a handle to Parent\NewName\Subkey

KCB tree
"Parent"
"NewName"
"OldName"
(transacted)
"Subkey" "Subkey"

## Slide 75

# CVE-2023-23420

1. Open a handle to Parent\OldName\Subkey to create its corresponding KCB

2. Transactionally rename "OldName"

3. Open a handle to Parent\NewName\Subkey

4. Commit the transaction, leading to duplicate KCBs of the subkey

## _KCB tree_

"Parent"

"NewName"
"Subkey" "Subkey"

## Slide 76

# CVE-2023-23420

1. Open a handle to Parent\OldName\Subkey to create its corresponding KCB

2. Transactionally rename "OldName"

3. Open a handle to Parent\NewName\Subkey

4. Commit the transaction, leading to duplicate KCBs of the subkey

5. Delete the subkey and discard one of the KCBs; the other KCB now refers to freed objects

## _KCB tree_

"Parent"

"NewName"

"Subkey"

## Slide 77

Demo

## Slide 78

Logic bugs
 Cross-feature bugs
 Object-lifetime bugs
4. Concurrency-related bugs
5. Cross-function bugs
6. Local bugs of omission
7. Information disclosure
8. Obvious, local bugs
9. Greppable
10. Fuzzable

# A taxonomy of bugs

## Slide 79

# Cross-feature bugs

- The Windows NT 3.1 registry design was elegant, but simple

- Many mechanisms introduced later are "hacks" addressing specific problems:

   - Predefined keys

   - Symbolic links

   - Registry virtualization

   - KTM and lightweight transactions

   - Differencing hives and layered keys

- So how do they all work together?

## Slide 80

Predefined
Registry
Keys
Virtualization
Layered
Keys Transactions
Symbolic
Links

## Slide 81

# Cross-feature bugs

- A bit of a hyperbole – they are not actively hostile

- However, they are often unaware of each others' corner cases and may trip over them:

   - Reimplementing a standard operation without porting all of the checks from the canonical one

   - Accessing weird keys / key placeholders indirectly, where directly wouldn't have been possible

   - Forgetting to opt out of specific options, which are opt-in by default and not immediately obvious

## Slide 82

Examples

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Examples
Issue 2389: Windows Kernel registry virtualization incompatible with transactions, leading to inconsistent hive state and memory
corruption
Reported by mjurczyk@google.com on Wed, Nov 30, 2022, 3:50 PM GMT+1
Issue 2445: Windows Kernel arbitrary read by accessing predefined keys through differencing hives
Reported by mjurczyk@google.com on Wed, Apr 19, 2023, 3:20 PM GMT+2
Issue 2446: Windows Kernel may reference unbacked layered keys through registry virtualization
Reported by mjurczyk@google.com on Thu, Apr 20, 2023, 3:44 PM GMT+2
Issue 2447: Windows Kernel may reference rolled-back transacted keys through differencing hives
Reported by mjurczyk@google.com on Thu, Apr 27, 2023, 1:01 PM GMT+2
```

## Slide 83

Logic bugs
 Cross-feature bugs
 Object-lifetime bugs
4. Concurrency-related bugs
5. Cross-function bugs
6. Local bugs of omission
7. Information disclosure
8. Obvious, local bugs
9. Greppable
10. Fuzzable

# A taxonomy of bugs

## Slide 84

# Logic bugs

- The crown jewel of software vulnerabilities

   - Can be very deep and hard to find with automation

   - Often 100% reliable

   - Typically don't involve memory corruption and are easier to exploit

- Particularly relevant to the registry

   - Implements a substantial amount of high-level logic

   - Responsible for enforcing its own security access checks

   - Manages sensitive system configuration that is attractive both to leak and corrupt

   - Shared by both restricted and highly-privileged processes in the system

## Slide 85

# Case study: symbolic links

- Symbolic links with source/destination across different privilege levels are dangerous, as they can lead to confused deputy problems

- This has been previously the case in Windows XP and earlier versions

- Addressed in Windows Server 2003 and later with _hive trust classes_

## Slide 86

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
fic Registry Editor = oO x
File Edit View Favorites Help
Computer
v B computer Name Type Data
> 7 HKEY_CLASSES_ROOT
> 7 HKEY_CURRENT_USER
v © HKEY_LOCAL_MACHINE
™ BcD00000000
“7 DRIVERS
“> HARDWARE
> SAM
© SECURITY
“7 SOFTWARE
“SYSTEM
> ©) DEFAULT
> Ms-1-5-18
S-1-5-19
S-1-5-20
S-1-5-21-309235459-240059954-4066018515-1001
S-1-5-21-309235459-240059954-4066018515-1001_Classes
> 7) S-1-5-21-309235459-240059954-4066018515-1002
> 7) S-1-5-21-309235459-240059954-4066018515-1002_Classes
> HKEY_CURRENT_CONFIG
VEZ
vey
```

## Slide 87

# Predefined keys

- A special type of key introduced for compatibility reasons in Windows NT 3.5

   - Redirects a key to a controlled HKEY_* top-level key on the Registry API level

- Used to redirect two Perflib-related keys to their HKEY_PERFORMANCE_* counterparts

- ● Conceptually equivalent to symbolic links, but not subject to trust classes

- More restricted than regular symlinks:

   - Source: a hive that grants write access to its backing file

   - Destination: one of ~10 possible top-level keys

## Slide 88

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
fic Registry Editor
File Edit View Favorites Help
Computer
v B computer Name Type Data
> "1 HKEY_CLASSES_ROOT hal
> > HKEY_CURRENT_USER al
y=) HKEY_LOCAL_MACHINE nal
BCD00000000
HARDWARE
SAM
SECURITY
SOFTWARE
SYSTEM
v "7 HKEY_USERS le
-DEFAULT
S-1-5-18
S-1-5-19
2155220:
> * $-1-5-21-309235459-240059954-4066018515-1001
> | S-1-5-21-309235459-240059954-4066018515-1001_Classes
v7) HKEY_CURRENT_CONFIG al
Software
System
```

## Slide 89

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Issue 2492: Windows registry predefined keys may lead to confused deputy problems and local privilege escalation e
(og Code iH
Reported by mjurczyk@google.com on Fri, Oct 6, 2023, 11:44 AMGMT+2 (ia
In Windows Registry, predefined-handle keys are a special type of keys similar to symbolic links, but instead of transparently
redirecting to an arbitrary registry path, they redirect to an arbitrary predefined registry key (HKLM, HKCU, HKCR etc., see [1] for a
full list). The concept of symbolic links makes the system potentially prone to security bugs, in situations where a privileged process
(e.g. winlogon or a system service) operates on user-controlled keys. By abusing symbolic links, such processes could be tricked into
reading from or writing to a different key that they originally intended to, allowing a local attacker to elevate their privileges in
the system. For this reason, there is a mechanism in the Windows registry called "trust classes", which prevents traversing symbolic
links originating from untrusted hives (such as user hives) pointing to trusted hives (such as global system hives). Internally, the
verification of this security boundary is implemented in the CmpOKToFollowLink kernel function.
The problem discussed in this report is the fact that predefined keys don't have a similar safety mechanism, which means that a local
user may redirect any key within their HKEY_CURRENT_USER hive to any of the possible predefined keys, including some system-wide ones.
This behavior may potentially allow crossing a security boundary, but successful exploitation depends on finding a privileged process
that opens a key inside HKCU and does something “interesting” with it. We have found one such candidate in the form of the System Event
Notification Service (SENS), which is implemented by the sens.dll library that also extensively calls into es.dll (probably standing for
Event System). This service gets notified about all user logon/logoff events in the system, and when that happens, a series of function
calls leads to es!CreateEventSystemKey. This routine opens the HKCU\Software\Microsoft\EventSystem key in the hive of the user that is
just logging in, and sets its security descriptor to a very permissive DACL which grants the user full access (KEY_ALL_ACCESS) to the
key and all of its subkeys (the specific DACL string is formatted in es!InitializeStringSecurityDescriptorForEventSystemKey) .
```

## Slide 90

# Plan of attack

1. HKCU\Software\Microsoft\EventSystem → HKEY_CURRENT_CONFIG

2. _System Event Notification Service_ (svchost.exe) unknowingly sets a permissive descriptor on HKCC, granting us write access

3. HKCC\Link → HKCR\TypeLib\{GUID}\2.0

4. Trigger the bug a second time to gain control over the COM object

5. Corrupt a COM object used by a System process, elevate privileges

## Slide 91

# Attacker's view

1. Plant  2. Log out and
ntuser.man back in

5. Corrupt HKCR 6. Log out

4. Log out and
back in

3. Create
symlink

⌨
7. Press special  8. Elevated cmd
shortcut

## Slide 92

Demo

## Slide 93

Predefined key timeline

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Predefined key timeline
27 July 1993 27 May 2024
Windows NT 3.1 release Today
Windows NT 3.5 — 4.0
September 1994 - June 2002
NT 3.1
Windows 2000
February 2000 - July 2010
Windows XP
October 2001 - April 2014 11 July 2023
Windows Vista Patch Tuesday
January 2007 - April 2017
Windows 7
October 2009 - January 2020
Windows 8.x
October 2012 - January 2023
Windows 10
July 2015 - July 2023
Windows
11
Vulnerable Not affected
```

## Slide 94

# Predefined key summary

- A completely undocumented feature lived in the format for almost 30 years

- Demonstrates the strengths of logic bugs

   - Unfuzzable

   - Breaks high-level security guarantees

- Requires comprehensive knowledge of the target for exploitation

   - Identifying the fundamental problem with the feature

   - Finding the right set of primitives

      - Binary control over HKCU via ntuser.man

      - A system service that performs "abusable" operations on HKCU

## Slide 95

Conclusion

## Slide 96

# Takeaways

- The registry is a fascinating research target

- If you're a researcher: persistent analysis pays off

   - Fuzzing is often only scratching the surface

   - For some targets, the really good bugs come from a deep understanding of software

- If you're a vendor: some features shouldn't live forever

   - Legacy code is a security hazard and should be periodically reevaluated

   - Attack surface reduction and well-placed mitigations have an outsized impact on security
