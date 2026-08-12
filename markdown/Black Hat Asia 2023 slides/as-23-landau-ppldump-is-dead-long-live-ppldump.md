---
title: "PPLdump Is Dead Long Live PPLdump"
speakers: ["Landau"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2023"
edition: "ASIA"
year: 2023
source_pdf: "Black Hat Asia 2023 slides/AS-23-Landau-PPLdump-Is-Dead-Long-Live-PPLdump.pdf"
pages: 49
sha256: "3fe64bb7d19b93bb826a2ecda2b1d2642bfbf43eb0f17782e38ba282933118b8"
text_chars: 26877
ocr_pages: 10
has_ocr: true
redacted_secrets: 0
ocr_confidence: 83.0
ocr_unreliable_blocks: 0
vision_verified_blocks: 4
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T03:47:50Z"
---
# PPLdump Is Dead Long Live PPLdump

**Speakers:** Landau  
**Conference:** Black Hat ASIA 2023  
**Source:** `Black Hat Asia 2023 slides/AS-23-Landau-PPLdump-Is-Dead-Long-Live-PPLdump.pdf` (49 pages)


## Slide 1

# PPLdump Is Dead. Long Live PPLdump!

Gabriel Landau Principal, Elastic

#BHASIA   @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
MAY 11-12
BRIEFINGS
PPLdump Is Dead.
Long Live PPLdump!
Gabriel Landau
&Y elastic security labs Principal, Elastic
#BHASIA @BlackHatEvents
```

## Slide 2

Gabriel Landau is a principal at Elastic Security. His public research includes Process Ghosting, AV sandboxing attacks, Kernel Mode Threats and Practical Defenses (Black Hat USA), Hide Your Valuables - Mitigating Physical Credential Dumping Attacks (Shmoocon), PPLGuard, and CI Spotter. His non-public work includes endpoint protections, exploit mitigation, product and DRM evaluation, and malware reversing. Though he mostly wears blue these days, his heart will always be red.

#BHASIA   @BlackHatEvents

## Slide 3

## Outline

- **●Introduction**

   - **What is a protected process?**

   - **Implementation**

- ●Attacks

   - Historical

   - Current

- ●New Research

   - Novel Attack

   - Chaining Exploits

   - ○ Mitigation

#BHASIA   @BlackHatEvents

## Slide 4

## Protected Process (PP)

- ●Introduced in Windows 8

- ●Process hardened against code injection and memory tampering

- ●Created to isolate DRM processing from piracy tools with admin rights

- ●Will only load specially-signed code (EXEs/DLLs) ○ No DLL side-loading

- ●Handles are hardened:

   - No PROCESS_VM_WRITE, THREAD_SET_CONTEXT, etc

- ●Also protects System, Registry, and and System Guard Runtime processes

#BHASIA   @BlackHatEvents

## Slide 5

## Protected Process Light (PPL)

- ●Introduced in Windows 8.1 as an extension of PP

- ●Similar signature requirements and process/thread HANDLE hardening

- ●Protect OS internals and AV from tampering

   - CSRSS - highly trusted by kernel

   - LSASS - credential dumping

   - SCM - service control manager

   - AntiMalware - prevent trivial termination of AV

- ●Later extended to prevent application tampering

   - Hyper-V Shielded VMs

- _●The rest of this talk is about PPL_

#BHASIA   @BlackHatEvents

## Slide 6

## PPL Implementation - EPROCESS

- Structure within kernel EPROCESS

- ●Assigned at process creation

- ●Protection type

   - None, Protected Process, or PPL

- ●Protection signer

   - See diagram

##### **PPL Signers (Simplified)**

WinTcb
(Most Secure)
Windows
LSA Anti-Malware CodeGen
Restricted Access
Restricted Access

Diagram adapted from James Forshaw then updated: <u>https://googleprojectzero.blogspot.com/2018/10/injecting-code-into-windows-protected.html</u> Thanks to @sixyvividtails for clarification: <u>https://twitter.com/sixtyvividtails/status/1644098456951087104</u>

#BHASIA   @BlackHatEvents

## Slide 7

## Code Integrity - Signatures

#BHASIA   @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 83/100 on the text kept, 76/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Code Integrity - Signatures

[Window 1] SgrmBroker.exe Properties
Certificate
General | Details | Certification Path
Show: <All>
Field                          Value
Enhanced Key Usage             Windows TCB Component (1.3.…
Subject Key Identifier         793165f0dbf15e5c04453d756..
Subject Alternative Name       Directory Address:SERIALNUM.
Authority Key Identifier       KeyID=a92902398e16c49778..
CRL Distribution Points        [1]CRL Distribution Point: Distr..
Authority Information Access   [1]Authority Info Access: Acc…
Basic Constraints              Subject Type=End Entity, Pat..
Thumbprint                     08647820d503fd505df763ab2..
[red box]
Windows TCB Component (1.3.6.1.4.1.311.10.3.23)
Protected Process Verification (1.3.6.1.4.1.311.10.3.24)
Windows System Component Verification (1.3.6.1.4.1.311.10.3.6)
Code Signing (1.3.6.1.5.5.7.3.3)

[Window 2] svchost.exe Properties
Certificate
General | Details | Certification Path
Show: <All>
Field                          Value
Enhanced Key Usage             Protected Process Light Verific.
Subject Key Identifier         01f0d3a457341838ebb31253..
Subject Alternative Name       Directory Address:SERIALNUM.
Authority Key Identifier       KeyID=a92902398e16c49778.
CRL Distribution Points        [1]CRL Distribution Point: Distr.
Authority Information Access   [1]Authority Info Access: Acc..
Basic Constraints              Subject Type=End Entity, Pat..
Thumbprint                     c60a14a6bd925780e9f0463ba..
[red box]
Protected Process Light Verification (1.3.6.1.4.1.311.10.3.22)
Windows System Component Verification (1.3.6.1.4.1.311.10.3.6)
Code Signing (1.3.6.1.5.5.7.3.3)

[Window 3] csrss.exe Properties
Certificate
General | Details | Certification Path
Show: <All>
Field                          Value
Enhanced Key Usage             Protected Process Light Verific..
Subject Key Identifier         7d3af1a3055c18fdf39399016..
Subject Alternative Name       Directory Address:SERIALNUM.
Authority Key Identifier       KeyID=a92902398e16c49778..
CRL Distribution Points        [1]CRL Distribution Point: Distr..
Authority Information Access   [1]Authority Info Access: Acc..
Basic Constraints              Subject Type=End Entity, Pat..
Thumbprint                     e94a68b056ce2fa8ab046a84f..
[red box]
Protected Process Light Verification (1.3.6.1.4.1.311.10.3.22)
Windows TCB Component (1.3.6.1.4.1.311.10.3.23)
Windows System Component Verification (1.3.6.1.4.1.311.10.3.6)
Code Signing (1.3.6.1.5.5.7.3.3)
```

## Slide 8

## PPL Implementation - EPROCESS

#BHASIA   @BlackHatEvents


> Recovered by OCR — confidence 79/100 on the text kept, 57/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
PPL Implementation - EPROCESS
7: kd> dx -g @$cursession.Processes.Select(p => new {Name =
o.Name, Type =
[@x8c] Registry @x2 @x7 8x8
[6x21f8] SecurityHealthService.exe @x1 @x5 @x8
```

## Slide 9

## Processes and Thread Protection

- Process and Thread Hardening

   - Read/write access rights blocked to less-privileged callers

      - No PROCESS_TERMINATE, PROCESS_VM_WRITE, PROCESS_VM_READ, etc.

      - Checked in kernel by RtlTestProtectedAccess

      - No exceptions for SeDebugPrivilege

   - New limited-access rights

      - PROCESS_QUERY_ **LIMITED** _INFORMATION, PROCESS_SET_ **LIMITED** _INFORMATION

      - ■ THREAD_QUERY_ **LIMITED** _INFORMATION, THREAD_SET_ **LIMITED** _INFORMATION

#BHASIA   @BlackHatEvents

## Slide 10

## Processes and Thread Protection

#BHASIA   @BlackHatEvents


> Recovered by OCR — confidence 79/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
PS C:\Windows\System32> Get-NtToken Select User, IntegrityLevel
User IntegrityLevel
NT AUTHORITY\SYSTEM
PS C:\Windows\System32> (Get-NtToken).Groups| Where {$_.Name
Attributes
SERVICE\TrustediInstaller EnabledByDefault, Enabled, Owner
S C:\Windows \Sy 3 (Get-NtToken) .Privileges where {$ .Name eC 4 . Select Name, Enabled
Name
SeDebugPrivilege
: \Windows\System32> Get-NtProcess services.exe All
: \Windows\System32> Get-NtProcess services.exe QueryLimitedInformation
NtTypeName Inherit ProtectFromClose
services.exe Process False False
```

## Slide 11

## Resource Protection

- Token Trust Level

   - New token attribute which indicates the trust level of the acting process or thread

#BHASIA   @BlackHatEvents

## Slide 12

## Resource Protection

- Trust Labels

   - New System Access Control List Entry (SACL ACE) type that allow trust level test for any securable object

   - ○ Examples:

      - Protecting KnownDlls against modification by malicious administrators

      - Protect PPL process tokens against sandboxing by malicious administrators*

* Recent addition.  See my work: https://www.elastic.co/security-labs/sandboxing-antimalware-products

#BHASIA   @BlackHatEvents

## Slide 13

## Outline

- ●Introduction

   - What is a protected process?

   - Implementation

- **●Attacks**

   - **Historical**

   - **Current**

- ●New Research

   - Novel Attack

   - Chaining Exploits

   - ○ Mitigation

#BHASIA   @BlackHatEvents

## Slide 14

## Attack: Cached Signing Level

- ●NtSetCachedSigningLevel race condition

- ●CI caches signing information for performance reasons

- ●Cache entries are automatically invalidated by NTFS if file is modified

- ●Race condition in CI allowed file to be modified before cache entry is finalized

- ●Fixed as CVE-2017-11830

Source: <u>Unknown Known DLLs and other Code Integrity Trust Violations</u>

#BHASIA   @BlackHatEvents

## Slide 15

### Attack: Counterfeit \KnownDlls via Silos

- ●Windows containers (aka silos) are similar to docker containers. ●Containers created ability to “chroot” a process into a new object manager namespace ●“chroot” ability creates a unique namespace for all named objects including drives, network shares, events, mutexes, named pipes, etc

- ●\KnownDlls section object cache is part of the Object Manager namespace

   - Protected by trust label so this cannot normally be modified by attackers

- ●Windows treats \KnownDlls as verified - no additional checks before loading into PPL ●Attacker can create a counterfeit KnownDlls directory then spawn a new “chrooted” PPL, which will use their KnownDlls, loading DLLs specified therein

- ●Fixed in 7/2022 by removing KnownDlls support from PPL

Source: <u>Unknown Known DLLs and other Code Integrity Trust Violations</u>

#BHASIA   @BlackHatEvents

## Slide 16

## Attack: Script Engine COM Hijack

- ●Some script interpreter DLLs will automatically load scripts specified in the registry ●Use DotNetToJScript to convert .NET payload to JS

- ●Find COM used by PPL, and hijack its registry run a script interpreter DLL instead ●Script interpreter loads attacker JS based on registry key, which loads .NET payload ●Fixed in 1803 by blocking script interpreters from loading into PPL

   - New function nt!CipMitigatePPLBypassThroughInterpreters blocks PPL from loading interpreter DLLs

Source: <u>Unknown Known DLLs and other Code Integrity Trust Violations</u>

#BHASIA   @BlackHatEvents

## Slide 17

### Attack: Bring Your Own Vulnerable EXE

- ●Windows Error Reporting process memory dumper (WerFaultSecure) encrypts dumps to protect PP and PPL confidentiality

- ●Bug in Windows 8.1 build can lead to creation of unencrypted dumps

- ●Microsoft fixed the WerFaultSecure bug ~2014

- ●Latest Win11 will still run old vulnerable builds as WinTcb-Full ○ Easy RunAsPPL LSASS defeat

Source: http://publications.alex-ionescu.com/NoSuchCon/NoSuchCon%202014%20-%20Unreal%20Mode%20-%20Breaking%20Protected%20Processes.pdf

#BHASIA   @BlackHatEvents

## Slide 18

## Attack: COM IRundown::DoCallback

- ●Use vulnerable Windows 8.1 WerFaultSecure to dump process and find secrets and addresses

- ●Use COM hijack to exploit undocumented COM feature: IRundown::DoCallback ●Use acquired secrets and addresses to call an arbitrary function within WerFault.exe ●Call existing code in process, achieving arbitrary write primitive

- ●Use arbitrary write primitive to overwrite LdrpKnownDllDirectoryHandle

- ●With counterfeit KnownDlls installed, attack proceeds like DefineDosDevice exploit

Source: https://googleprojectzero.blogspot.com/2018/11/injecting-code-into-windows-protected.html

#BHASIA   @BlackHatEvents

## Slide 19

## Attack: AntiMalware Blight

- ●ELAM - Early Launch AntiMalware Driver

   - Driver containing certificate hashes

   - Special signature from Microsoft

   - Any certificate listed in an ELAM driver can sign a file to run as AntiMalware-Light

- ●Overly-permissive ELAM

   - Some Antimalware vendors included hashes of certificates third-party certificates

   - Microsoft didn’t vet certificate lists before signing ELAM drivers

- ●There are many overly-permissive ELAM drivers ○ Microsoft CAs included

- ●Example: You can run msbuild.exe as AntiMalware-Light with arbitrary parameters

Source: <u>https://github.com/mattifestation/AntimalwareBlight</u>

#BHASIA   @BlackHatEvents

## Slide 20

## Attack: DefineDosDevice Bug

●The DefineDosDevice API defines, redefines, or deletes MS-DOS device names ●Implemented via RPC to WinTcb-PPL CSRSS

- Remember this is the highest level of PPL

●TOCTOU enables attackers to trick CSRSS into creating entries in \KnownDlls ●Attacker can inject entries into KnownDlls, which PPL will load without verification ●Publicly documented in 2018 by James Forshaw

●Turnkey implementation released in April 2021 by Clément Labro as <u>PPLdump</u> ●Fixed in 7/2022 by removing KnownDlls support from PPL

Source: <u>Unknown Known DLLs and other Code Integrity Trust Violations</u>

#BHASIA   @BlackHatEvents

## Slide 21

### Attack: COM Proxy Type Library Confusion

- ●.NET Runtime Optimization Service runs as CodeGen PPL and hosts COM service

- ●Modify COM proxy configuration for service to trigger type confusion

- ●Use type confusion to trigger arbitrary write, replacing KnownDlls handle with counterfeit directory that is pre-loaded with attacker’s DLL

- ●With counterfeit KnownDlls installed, attack proceeds like DefineDosDevice exploit ●Leverage CodeGen PPL access to create a signing cache entry making any DLL as trusted so it can be side-loaded into WinTcb PPL (highest level)

- ●Variant implemented as turnkey <u>PPLmedic</u> tool in March 2023 by Clément Labro ●Microsoft: KnownDlls handle mitigation coming in June 2023

Source: https://googleprojectzero.blogspot.com/2018/10/injecting-code-into-windows-protected.html

#BHASIA   @BlackHatEvents

## Slide 22

## Outline

- ●Introduction

   - What is a protected process?

   - Implementation

- ●Attacks

   - Historical

   - Current

- **●New Research**

   - **Novel Attack**

   - **Chaining Exploits**

   - **Mitigation**

#BHASIA   @BlackHatEvents

## Slide 23

## Planning the Attack

- ●Attacks so far focus on:

   - CachedSigningLevel

   - KnownDlls

   - COM

- ●Let’s try a different approach

   - Bait and Switch aka Time of Check, Time of Use (TOCTOU)

#BHASIA   @BlackHatEvents

## Slide 24

CI TOCTOU: Planning the Attack
WinTcb-Light Kernel &
Storage
Process Code Integrity
Request DLL Load Request File Contents
Signed File Contents
Validate Signature
✔
Map DLL into Process
Execute DLL
Page Fault Request Page from File
Page Payload into Process Payload
Execute Payload
#BHASIA   @BlackHatEvents

## Slide 25

## CI TOCTOU: Page Hashes

●Page hashes present in services.exe but not EventAggregation.dll

#BHASIA   @BlackHatEvents


> Recovered by OCR — confidence 85/100 on the text kept, 63/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Ci TOCTOU: Page Hashes
e Page hashes present in services.exe but not EventAggregation.dll
;) /v /ph services.exe
Page hashes:
C:\Windows
\System32>signtool verify /a
973911FSDEABEFCF45A87 E948DE1DF57DBE1C6C22D12559F2754862CECSBB516
/v /ph EventAggregation.dll
SignTool Warning: No page hashes are present.
grep -A1® “Page hash"
grep -A1i@ “Page hash"
```

## Slide 26

## CI TOCTOU: Hunting for Local Paging

●Start simple - run services.exe as WinTcb-PPL

○ No file reads, and no paging I/O

#BHASIA   @BlackHatEvents

## Slide 27

#BHASIA   @BlackHatEvents

## Slide 28

### CI TOCTOU: Hunting for Remote Paging

●What about SMB?  Replace EventAggregation.dll with a symlink to loopback SMB ●We can see a paging operation over SMB

#BHASIA   @BlackHatEvents

## Slide 29

#BHASIA   @BlackHatEvents


> Recovered by OCR — confidence 83/100 on the text kept, 38/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ASIA 20253
AND THE ONLY PRESCRIPTION
```

## Slide 30

## CI TOCTOU: Oplock Candidates

●Can we slow down process launch to allow time for paging?

- ●What about an opportunistic lock (oplock)?

○ Non-cooperative NTFS/SMB file locking mechanism

- ●Let’s look for a CreateFile operation that we can interrupt

#BHASIA   @BlackHatEvents

## Slide 31

## CI TOCTOU: Oplock Results

●Set an oplock on devobj.dll and launch services.exe

●IRP has no result - operation is still pending

#BHASIA   @BlackHatEvents

## Slide 32

## CI TOCTOU: Oplock Results

#BHASIA   @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 78/100 on the text kept, 43/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
CI TOCTOU: Oplock Results

3: kd> k
 *** Stack trace for last set context - .thread/.cxr resets it
 # Child-SP          RetAddr               Call Site
00 ffffb88e`ac5be210 fffff807`7e4cb6c5     nt!KiSwapContext+0x76
01 ffffb88e`ac5be350 fffff807`7e4ccae7     nt!KiSwapThread+0xb05
02 ffffb88e`ac5be4a0 fffff807`7e4cf106     nt!KiCommitThreadWait+0x137
03 ffffb88e`ac5be550 fffff807`7e95be2c     nt!KeWaitForSingleObject+0x256
04 ffffb88e`ac5be8f0 fffff807`7e95bae7     nt!FsRtlCancellableWaitForMultipleObjects+0xcc
05 ffffb88e`ac5be960 fffff807`822c16c8     nt!FsRtlCancellableWaitForSingleObject+0x27
06 ffffb88e`ac5be9a0 fffff807`82256222     Ntfs!NtfsWaitForOplockCompletionEvent+0x24   [red box]
07 ffffb88e`ac5be9e0 fffff807`7e4d00a5     Ntfs!NtfsFsdCreate+0x272
08 ffffb88e`ac5bec60 fffff807`813d9f5b     nt!IofCallDriver+0x55
09 ffffb88e`ac5beca0 fffff807`8140eff3     FLTMGR!FltpLegacyProcessingAfterPreCallbacksCompleted+0x15b
0a ffffb88e`ac5bed10 fffff807`7e4d00a5     FLTMGR!FltpCreate+0x323
0b ffffb88e`ac5bedc0 fffff807`7e8e2979     nt!IofCallDriver+0x55
0c ffffb88e`ac5bee00 fffff807`7e8de4f1     nt!IopParseDevice+0x8c9
0d ffffb88e`ac5befd0 fffff807`7e8dd4d2     nt!ObpLookupObjectName+0xae1
0e ffffb88e`ac5bf170 fffff807`7e8c1cf9     nt!ObOpenObjectByNameEx+0x1f2
0f ffffb88e`ac5bf2a0 fffff807`7e8bdfc8     nt!IopCreateFile+0x439
10 ffffb88e`ac5bf360 fffff807`7e63e1e8     nt!NtOpenFile+0x58
11 ffffb88e`ac5bf3f0 00007fff`dd26f2b4     nt!KiSystemServiceCopyEnd+0x28
12 00000083`4a77f0f8 00007fff`dd1e064c     ntdll!NtOpenFile+0x14
13 00000083`4a77f100 00007fff`dd1e0bb8     ntdll!LdrpMapDllNtFileName+0xe8
14 00000083`4a77f200 00007fff`dd1e0f80     ntdll!LdrpMapDllSearchPath+0x1d0
15 00000083`4a77f460 00007fff`dd1e0dbb     ntdll!LdrpProcessWork+0x148
16 00000083`4a77f4b0 00007fff`dd23236a     ntdll!LdrpWorkCallback+0xbb
17 00000083`4a77f4e0 00007fff`dd205976     ntdll!TppWorkpExecuteCallback+0x13a
18 00000083`4a77f530 00007fff`dcf626bd     ntdll!TppWorkerThread+0x8f6
19 00000083`4a77f810 00007fff`dd22a9f8     KERNEL32!BaseThreadInitThunk+0x1d
1a 00000083`4a77f840 00000000`00000000     ntdll!RtlUserThreadStart+0x28
```

## Slide 33

## CI TOCTOU: Forcing Paging

- ●Where do we go from here?

- ●We have a frozen WinTcb PPL process.  We want it to page-in code over the network.

- ●Can we page it out using EmptyWorkingSet?

   - Requires PROCESS_SET_QUOTA, which we can’t get

- ●What about paging out the whole OS?

   - Empty system working set and standby lists

      - NtSetSystemInformation(SystemMemoryListInformation)*

      - Requires SeProfileSingleProcessPrivilege, which Admins have

* <u>https://github.com/elastic/Silhouette/blob/main/2023-01%20Silhouette%20Shmoocon%20Presentation.pdf</u>

#BHASIA   @BlackHatEvents

## Slide 34

## CI TOCTOU: Paged Reads

#BHASIA   @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 72/100 on the text kept, 68/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
CI TOCTOU: Paged Reads

Process Monitor - Sysinternals: www.sysinternals.com
File  Edit  Event  Filter  Tools  Options  Help

Relative Time | Process Name | PID | Operation | Path | Result | Detail
00:00:17.0969135  services.exe  508  CloseFile          C:\Windows\System32\EventAggregation.dll                             SUCCESS
00:00:17.0971696  services.exe  508  CreateFile         C:\Windows\System32\EventAggregation.dll                             REPARSE            Desired Access: Read Data/List Directory, Execute/Trav...
00:00:17.1006151  services.exe  508  CreateFile         \\127.0.0.1\C$\Windows\System32\EventAggregation.dll.bak            SUCCESS            Desired Access: Read Data/List Directory, Execute/Trav...
00:00:17.1017799  services.exe  508  CreateFileMapping  \\127.0.0.1\C$\Windows\System32\EventAggregation.dll.bak            FILE LOCKED WI...   SyncType: SyncTypeCreateSection, PageProtection: PA...
00:00:17.1018504  services.exe  508  ReadFile           \\127.0.0.1\C$\Windows\System32\EventAggregation.dll.bak            SUCCESS            Offset: 0, Length: 90,112, I/O Flags: Non-cached, Paging...
00:00:17.1018615  services.exe  508  ReadFile           C:\Windows\System32\EventAggregation.dll.bak                         SUCCESS            Offset: 0, Length: 90,112, I/O Flags: Non-cached
00:00:17.1027614  services.exe  508  QueryEAFile        \\127.0.0.1\C$\Windows\System32\EventAggregation.dll.bak            ACCESS DENIED
00:00:17.1057495  services.exe  508  QueryEAFile        \\127.0.0.1\C$\Windows\System32\EventAggregation.dll.bak            ACCESS DENIED
00:00:17.1058253  services.exe  508  SetEAFile          \\127.0.0.1\C$\Windows\System32\EventAggregation.dll.bak            ACCESS DENIED
00:00:17.1064822  services.exe  508  CreateFileMapping  \\127.0.0.1\C$\Windows\System32\EventAggregation.dll.bak            SUCCESS            SyncType: SyncTypeOther
00:00:17.1066262  services.exe  508  Load Image         \\127.0.0.1\C$\Windows\System32\EventAggregation.dll.bak            SUCCESS            Image Base: 0x7ffdf0450000, Image Size: 0x16000
00:00:17.1066861  services.exe  508  CloseFile          \\127.0.0.1\C$\Windows\System32\EventAggregation.dll.bak            SUCCESS
──────────────────────────── [red separator line] ────────────────────────────
00:00:51.1699161  services.exe  508  ReadFile           \\127.0.0.1\C$\Windows\System32\EventAggregation.dll.bak            SUCCESS            Offset: 0, Length: 4,096, I/O Flags: Non-cached, Paging I...
00:00:51.1701225  services.exe  508  ReadFile           C:\Windows\System32\EventAggregation.dll.bak                         SUCCESS            Offset: 0, Length: 4,096, I/O Flags: Non-cached
00:00:51.1702783  services.exe  508  ReadFile           \\127.0.0.1\C$\Windows\System32\EventAggregation.dll.bak            SUCCESS            Offset: 53,248, Length: 16,384, I/O Flags: Non-cached, P...
00:00:51.1702900  services.exe  508  ReadFile           C:\Windows\System32\EventAggregation.dll.bak                         SUCCESS            Offset: 53,248, Length: 16,384, I/O Flags: Non-cached
00:00:51.1715041  services.exe  508  ReadFile           \\127.0.0.1\C$\Windows\System32\EventAggregation.dll.bak            SUCCESS            Offset: 73,728, Length: 4,096, I/O Flags: Non-cached, Pa...
00:00:51.1715132  services.exe  508  ReadFile           C:\Windows\System32\EventAggregation.dll.bak                         SUCCESS            Offset: 73,728, Length: 4,096, I/O Flags: Non-cached
00:00:51.1715971  services.exe  508  ReadFile           \\127.0.0.1\C$\Windows\System32\EventAggregation.dll.bak            SUCCESS            Offset: 4,096, Length: 4,096, I/O Flags: Non-cached, Pag...
00:00:51.1716052  services.exe  508  ReadFile           C:\Windows\System32\EventAggregation.dll.bak                         SUCCESS            Offset: 4,096, Length: 4,096, I/O Flags: Non-cached
00:00:51.1716701  services.exe  508  ReadFile           \\127.0.0.1\C$\Windows\System32\EventAggregation.dll.bak            SUCCESS            Offset: 4,096, Length: 32,768, I/O Flags: Non-cached, Pa...
00:00:51.1716803  services.exe  508  ReadFile           C:\Windows\System32\EventAggregation.dll.bak                         SUCCESS            Offset: 4,096, Length: 32,768, I/O Flags: Non-cached
00:00:51.1717834  services.exe  508  ReadFile           \\127.0.0.1\C$\Windows\System32\EventAggregation.dll.bak            SUCCESS            Offset: 40,960, Length: 4,096, I/O Flags: Non-cached, Pa...
00:00:51.1717897  services.exe  508  ReadFile           C:\Windows\System32\EventAggregation.dll.bak                         SUCCESS            Offset: 40,960, Length: 4,096, I/O Flags: Non-cached
00:00:51.1718510  services.exe  508  ReadFile           \\127.0.0.1\C$\Windows\System32\EventAggregation.dll.bak            SUCCESS            Offset: 36,864, Length: 12,288, I/O Flags: Non-cached, P...
00:00:51.1718630  services.exe  508  ReadFile           C:\Windows\System32\EventAggregation.dll.bak                         SUCCESS            Offset: 36,864, Length: 12,288, I/O Flags: Non-cached

Showing 26 of 43 events (60%)          Backed by virtual memory
```

## Slide 35

## CI TOCTOU: Delivering the Payload

- ●Now that we can reliably force page faults, let’s try to inject some code

   - a. Disable the local SMB server (LanManServer service) and reboot

   - b. Run local SMB server that serves two versions of EventAggregation.dll

      - First, serve original DLL for CI verification

      - Later, patch in special sauce over DllMain for subsequent requests

#BHASIA   @BlackHatEvents

## Slide 36

## CI TOCTOU: Code Execution

#BHASIA   @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 83/100 on the text kept, 78/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
CI TOCTOU: Code Execution

Break instruction exception - code 80000003 (first chance)
0033:00007fff`addb1550 cc                  int     3
5: kd> db @rip
00007fff`addb1550  cc 90 90 90 90 90 90 90-90 90 90 90 90 90 90 90  ................
00007fff`addb1560  ca fe c0 de ca fe c0 de-ca fe c0 de ca fe c0 de  ................
00007fff`addb1570  ca fe c0 de ca fe c0 de-ca fe c0 de ca fe c0 de  ................
00007fff`addb1580  ca fe c0 de ca fe c0 de-ca fe c0 de ca fe c0 de  ................
00007fff`addb1590  ca fe c0 de ca fe c0 de-ca fe c0 de ca fe c0 de  ................
00007fff`addb15a0  ca fe c0 de ca fe c0 de-ca fe c0 de ca fe c0 de  ................
00007fff`addb15b0  ca fe c0 de ca fe c0 de-ca fe c0 de ca fe c0 de  ................
00007fff`addb15c0  ca fe c0 de ca fe c0 de-ca fe c0 de ca fe c0 de  ................
5: kd> dx @$curprocess->Name
@$curprocess->Name : services.exe
    Length           : 0xc
5: kd> dx @$curprocess->KernelObject->Protection
@$curprocess->KernelObject->Protection                [Type: _PS_PROTECTION]
    [+0x000] Level            : 0x61 [Type: unsigned char]
    [+0x000 ( 2: 0)] Type             : 0x1 [Type: unsigned char]
    [+0x000 ( 3: 3)] Audit            : 0x0 [Type: unsigned char]
    [+0x000 ( 7: 4)] Signer           : 0x6 [Type: unsigned char]
```

## Slide 37

## CI TOCTOU: Removing the Reboot

- LanManServer configuration change is noisy.  Can we remove the reboot?

- a. SMB - port fixed.  LanManServer takes it early in boot.  No way to release it

- b. WebDAV - file is read once at mapping and cached locally

- ● Cloud Filter API

   - a. Available by default in Client SKUs of 1709+

   - b. Create small/empty placeholder files marked with reparse tags

   - c. When read requests come, minifilter drive detects reparse tags and calls UM callback to request data

   - d. UM callback provides the requested file contents

      - You decide what bytes to serve to the client in your rehydration callback

   - e. Simple-to-use usermode API

   - No COM

- f. No special signing requirements

- g. James Forshaws provided working <u>sample code.</u>

https://googleprojectzero.blogspot.com/2021/01/windows-exploitation-tricks-trapping.html

#BHASIA   @BlackHatEvents

## Slide 38

## CI TOCOTU: Putting it All Together

●Final attack flow:

- a. Use CloudFilter to create an empty placeholder file with a callback function we control

- b. Redirect EventAggregation.dll to our placeholder through loopback SMB via symbolic link

- c. Set oplock on devobj.dll to interrupt process initialization

- d. Run the target PPL

- e. The target PPL attempts to load EventAggregation.dll

- f. CloudFilter callback fires to rehydrate placeholder

   - Serve up original EventAggregation.dll for CI verification

   - Page everything out by emptying working set and standby lists

   - Release oplock

- g. The PPL resumes and leads to paging reads over SMB, which are forwarded to the placeholder h. CloudFilter callback fires to rehydrate placeholder

   - Serve up patched copy of EventAggregation.dll

- i. The PPL executes our PIC payload inside services.exe as WinTcb-Light, which dumps the process of your choosing

#### ●This is PPLFault

#BHASIA   @BlackHatEvents

## Slide 39

## PPLFault: DEMO

●DEMO

#BHASIA   @BlackHatEvents

## Slide 40

## Why Stop at LSASS? ANGRYORCHARD

- ●Released in July 2022 by Austin Hudson when Microsoft patched PPLdump

- ●Exploits PPLdump bug to achieve code execution in CSRSS (WinTcb PPL)

- ●Exploits bug in NtUserHardErrorControl to perform arbitrary kernel decrement a. Only exploitable within CSRSS

- ●Decrement KTHREAD.PreviousMode from UserMode (1) to KernelMode (0) a. KernelMode disables most memory and security access checks on the system

   - b. GodMode - syscalls treat you like a kernel worker thread c. Examples:

      - hSystemProcess = OpenProcess(4, PROCESS_ALL_ACCESS)

      - WriteProcessMemory(SomeKernelAddress)

      - NtOpenSection(\Device\PhysicalMemory, SECTION_ALL_ACCESS)

#BHASIA   @BlackHatEvents

## Slide 41

## Exploit Chain Demo - GodFault

●DEMO

#BHASIA   @BlackHatEvents

## Slide 42

## Mitigations - Windows

●Root of problem is a TOCTOU where signature validation is decoupled from paging ●If only Windows had some way to validate the hashes of pages…

#BHASIA   @BlackHatEvents

## Slide 43

## Mitigations - AV Vendors

- ●AntiMalware vendors can’t

   - a. Modify the memory manager to require page hashes for all images loaded into PPL

   - b. Re-sign Microsoft binaries with PPL certs to add page hashes

- ●AntiMalware vendors can still break the PPLFault exploit chain

#BHASIA   @BlackHatEvents

## Slide 44

## Mitigation - NoFault

- ●NoRemoteImages

   - a. Exploit mitigation to prevent loading of DLLs from network locations (SMB, WebDAV, etc)

   - b. Originally introduced with EMET.  Later integrated directly into Windows

- ●Set-ProcessMitigation PowerShell cmdlet

   - a. Persists key in registry

   - b. Useless against attacker who controls registry

- ●NoFault.sys

   - a. Enables NoRemoteImages policy early in process lifecycle via process creation callback

https://learn.microsoft.com/en-us/windows/win32/api/winnt/ns-winnt-process_mitigation_image_load_policy https://learn.microsoft.com/en-us/powershell/module/processmitigations/set-processmitigation

#BHASIA   @BlackHatEvents

## Slide 45

## NoFault - DEMO

●DEMO

#BHASIA   @BlackHatEvents

## Slide 46

## Disclosure Timeline

- ●Timeline

   - 2022-09-22 Reported PPLFault and GodFault to MSRC as VULN-074311

   - 2022-10-21 MSRC case closed without action

   - 2023-02-28 I publicly announced this BlackHat talk on Twitter

   - 2023-03-01 Windows Defender team reached out to me via Twitter

- ●Exploits still functional against:

   - Windows 11 22H2 22621.1702 (May 2023)

   - Windows 11 Insider Canary 25346.1001 (April 2023)

#BHASIA   @BlackHatEvents

## Slide 47

## Conclusions / Black Hat Sound Bytes

- ●Defending against administrators is hard

   - Lots of power and attack surface

- ●Little things add up

   - Non-Elevated => Admin (UAC bypass) is not a security boundary

   - Admin => PPL is not a security boundary

   - PPL => Kernel RW is not a security boundary

   - Transitively: Non-Elevated => Kernel RW is not a security boundary

- ●When MSRC doesn’t care, the Defender team still might

- ●Public tooling get bugs fixed

   - It required “active abuse” to force Microsoft’s hand on the DefineDosDevice vulnerability

#BHASIA   @BlackHatEvents

Source: https://twitter.com/tiraniddo/status/1551966781761146880

## Slide 48

## Conclusions: Patching

#BHASIA   @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
= =
Conclusions: Patchin
a
ppp
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air 3rd generation and later, iPad 5th ROOT->KERNEL LPE REPORTED
generation and later, iPad mini 5th generation and later
Impact: An app with foot privileges may be able to execute arbitrary code with kernel privileges
Description: A use after free issue was addressed with improved memory management.
CVE-2022-42829: an anonymous researcher
Ppp
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air 3rd generation and later, iPad 5th
generation and later, iPad mini 5th generation and later
Impact: An app with root privileges may be able to execute arbitrary code with kernel privileges
Description: The issue was addressed with improved memory handling.
CVE-2022-42830: an anonymous researcher
ppp
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air 3rd generation and later, iPad 5th
generation and later, iPad mini 5th generation and later
Impact: An app with root privileges may be able to execute arbitrary code with kernel privileges
Description: A race condition was addressed with improved locking.
CVE-2022-42831: an anonymous researcher PAT C HES | i
CVE-2022-42832: an anonymous researcher
```

## Slide 49

## Questions?

- ●Gabriel Landau at Elastic Security Labs ●Twitter: @GabrielLandau

●PoC code: https://github.com/gabriellandau/PPLFault

#BHASIA   @BlackHatEvents
