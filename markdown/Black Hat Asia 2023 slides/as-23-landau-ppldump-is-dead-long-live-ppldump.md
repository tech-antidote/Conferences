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
text_chars: 30978
ocr_pages: 11
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:54:47Z"
---
# PPLdump Is Dead Long Live PPLdump

**Speakers:** Landau  
**Conference:** Black Hat ASIA 2023  
**Source:** `Black Hat Asia 2023 slides/AS-23-Landau-PPLdump-Is-Dead-Long-Live-PPLdump.pdf` (49 pages)


## Slide 1

# PPLdump Is Dead. Long Live PPLdump!

Gabriel Landau Principal, Elastic

#BHASIA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pifkhat”
ASIA 20a
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisek hat
ASIA 2023
a Certificate
General Details Certification Path
Show: | <All> v
Field Value
& Enhanced Key Usage Windows TCB Component (1.3.
793 165fO0dbf15e5c04453d756..
Directory Address:SERIALNUM.
KeyID=a92902398e 16c49778..
[1]CRL Distribution Point: Distr..
[1]Authority Info Access: Acc...
Subject Type=End Entity, Pat..
ORAS7AINASN AAA SN SAFTA Rah?
&] Subject Key Identifier
| &) Subject Alternative Name
&] Authority Key Identifier
(=: |CRL Distribution Points
§S)) Authority Information Access
(=| Basic Constraints
| (lth imbhnrint
Windows TCB Component (1.3.6. 1.4, 1.311. 10.3.23)
Protected Process Verification (1.3.6. 1.4. 1.311. 10.3.24)
Windows System Component Verification (1.3.6. 1.4, 1.311. 10.3.6)
Code Signing (1.3.6. 1.5.5.7.3.3)
Certificate
General Details Certification Path
Show: | <All> v
Field Value
(=| Enhanced Key Usage Protected Process Light Verific.
5 |Subject Key Identifier 01f0d3a457341838ebb31253..
(Z| Subject Alternative Name Directory Address:SERIALNUM,
&] Authority Key Identifier KeyID=a92902398e 16c49778.
[1]CRL Distribution Point: Distr.
[1] Authority Info Access: Acc..
Subject Type=End Entity, Pat..
cANa 14a6hdO757AaNeGM44 Gha
3) CRL Distribution Points
Authority Information Access
=||Basic Constraints
[Sl Thuimbnrint
fe
(SE
Protected Process Light Verification (1.3.6. 1.4, 1.311. 10.3.22)
Windows System Component Verification (1.3.6. 1.4, 1.311. 10.3.6)
Code Signing (1.3.6. 1.5.5.7.3.3)
a Certificate
General Details Certification Path
Show: | <All> v
Field Value
eal Enhanced Key Usage Protected Process Light Verific.
Gs] Subject Key Identifier 7d3af1a3055c18fdf39399016..
& Subject Alternative Name Directory Address:SERIALNUM.
eal Authority Key Identifier KeyID =a92902398e 16c49778..
|| CRL Distribution Points [1]CRL Distribution Point: Distr.
| Authority Information Access [1]Authority Info Access: Acc..
‘| Basic Constraints Subject Type=End Entity, Pat..
SS) thumbnrint _eO4a468hN SAce IfaRahNasarat _
Protected Process Light Verification (1.3.6. 1.4. 1.311. 10.3.22)
Windows TCB Component (1.3.6. 1.4. 1.311. 10.3.23)
Windows System Component Verification (1.3.6. 1.4. 1.311. 10.3.6)
Code Signing (1.3.6. 1.5.5.7.3.3)
```

## Slide 8

## PPL Implementation - EPROCESS

#BHASIA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2023
PPL Implementation - EPROCESS
o.KernelObject.
7: kd> dx -g @$cursession.Processes.Select(p => new {Name =
Pane ype Bt Signer ff SectionSignatureLevel
6x4
o.Name, Type =
System Ox2 Ox7 Oxc
[@x8c] Registry @x2 @x7 8x8
[8x97@ ] SermBroker.exe @x2 8x6 8x8
[6x1d38 ] smss.exe @x1 @x6 @x8
[8x22c] csrss.exe Oxi @x6 @x8
[6x278] wininit.exe @x1 @x6 ex8
[8x286 ] csrss.exe @x1 8x6 @x8
[O@x2cc ] services.exe 6x1 @x6 @xs
[@xbas ] svchost.exe @x1 @xS ex8
[6@x11bc] svchost.exe @x1 @x5 @x8
[6x21f8] SecurityHealthService.exe @x1 @x5 @x8
[@x21dc]} elastic-endpoint.exe @x1 @x3 8x8
[6x3ae] svchost.exe 6xe@ 8x8 8x8
[8@x3c8] fontdrvhost.exe @xe exe @x8
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blaekhat
ASIA 2023
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
€
black hat
ASIA 2023
C:\Windows \System32>signtool
Ci TOCTOU: Page Hashes
e Page hashes present in services.exe but not EventAggregation.dll
;) /v /ph services.exe
Page hashes:
OxGGGG0000
6x88800400
8x88001400
6x80882400
6x800634060
8x88004406
6x880085400
6x88886408
8x88007400
8x88008400
C:\Windows
\System32>signtool verify /a
973911FSDEABEFCF45A87 E948DE1DF57DBE1C6C22D12559F2754862CECSBB516
40648953BD60329AC1486A95 7A4EECSD3A14ABC4EGE359BBAD063697495C3AB9
DA4D752F6CSEAA717CD127E8C4D4491F1D87CD2D73E2B7F38BC8AG1336FE76E4
A8A85175F216A21BF276A6S5CCF26CD623E9SFC88DAG8FE8747606A16716A655F
A95303468AB638FD630C643265C819C14224865B954CAE98701D9428A2C6C1E9
161A769452176F6659EE9639432462D4E3454A31FSFEFSAAASE3E29D9E5249C1
B8ADD3652917342812D22A573E/75AFC85066321E360F15D7895658C2152847750
6755C750AD27D96B7F2D68D83216C4183B625E6CF/768DF98F1IC4F62F346D1D1C
A3A63DA8FB35B218BA9E3F116789D81D84CEB35B4F3FFE1DSA1O63ESASDAG7AA
3A2467@DDBEGS8CO46B1A4BC2B183CF41D35EF623COEGE2F3O58E1EDESBCD2C87
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blaekhat
ASIA 2023
WE NEED TO GO;
7
DEEPER ”
```

## Slide 28

### CI TOCTOU: Hunting for Remote Paging

●What about SMB?  Replace EventAggregation.dll with a symlink to loopback SMB ●We can see a paging operation over SMB

#BHASIA   @BlackHatEvents

## Slide 29

#BHASIA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bide hat
ASIA 20253
ie oy" g » ~~ f a ee
i el! nt _— =.
5 <2 £ A BESS \ . g : ‘
_ ac by ¥, Nie $7 - f
a :
1 GOT A FEWER
ar
AND THE ONLY PRESCRIPTION
-» IS MORE PAGING READS.
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2!
Ci TOCTOU: Oplock Results
ae
oo to ce SE a I pee ee wd mg ad ee a ScRSeeESs
Im IO [oo Ny Jon [un fe [uy Ir te 1d Ih ID [IA Io Im ho Ico Sk I LB I Iho te ID te
kd> k
*** Stack trace for last set context -
Child-sP
F¥FFb88e° acSbe2108
F¥FFb88e° acSbe35e
F¥FFb88e° acSbe4ae
F¥FFb88e° acSbe550
F¥FFb88e° acSbesfe
FfFFb88e° acSbe96e
FFFFb88e° acSbe9ae
F¥fFb88e° acSbe9ee
F¥FFb88e° acSbec6e
F¥¥Fb88e° acSbeca@
F¥FFb88e° acSbed1e
F¥FFb88e° acSbedce@
F¥FFb88e° acSbeeee
F¥FFb88e° acSbefde
F¥FFb88e° acSbf17e
F¥FFb88e° acSbf2ae
f¥Ffb88e° acSbf36e
F¥FFb88e° acSbf3fe
60000083" 4a77FOF3
00000083 ° 4a77F100
80000083" 4a77F200
80000083 ° 4a77F460
00000083" 4a77F4bO
00000083 ° 4a77F4e0
00000083" 4a77530
80800083 4a77F8108
80800083" 4a77F84E
RetAddr
F¥FFF807° 7e4cb6c5
F¥FFF807° 7edccae7
FF£4F807° 7e4c F106
F¥£FF£807° 7e9Sbe2c
F¥FFF807° 7e9Sbae7
F£FFF807° 822c16c8
F£¥FF807° 82256222
F£FFF807° 7e4deea5
FF¥F¥F807° 813d9F5b
F£FFF807° 8140ef F3
F¥¥¥F307° 7e4deeas
F#£FF807° 7e8e2979
F¥¥FF807° 7e8de4F1
F£FFF807° 7e8dd4d2
FFFFF807° 7e8cicf9
F££FF807° 7e8bdfc8
FFFFF807° 7e63e1e8
eeee7 FFF dd26f2b4
ee0e7 FFF ddiee@64c
eeee7 FFF ddle@bbs
eeee7 FFF ddieef3e
ee00e7 FFF ddle@dbb
e0007FFF dd23236a
eee0e7ffF dd265976
eee0e7ffF dcf626bd
eeee7 FFF dd22a9f8
eeeeeeee BeeGEeeRE
-thread/.cxr resets it
Call Site
nt !KiSwapContext+0x76
nt! KiSwapThread+@xbes
nt!KiCommitThreadwWait+0x137
nt!KeWaitForSingleObject+0x256
a oicuestikiani ee
TE cAINSCTE OUT EENGEr
nt! IofCallDriver+0x55
FLTMGR! FltpLegacyProcessingAfterPreCallbacksCompleted+0x15b
FLTMGR! FltpCreate+@x323
nt! IofCallDriver+8x55
nt! IopParseDevice+@x8c9
nt! ObpLookupObjectName+@xae1
nt! ObOpenObjectByNameEx+0x1F2
nt! IopCreateFile+0x439
nt! NtOpenFile+@x58
nt! KiSystemServiceCopyEnd+0x28
ntd11!NtOpenFile+0x14
ntd11!LdrpMapD11NtFileName+@xe8
ntd11!LdrpMapD11SearchPath+0x1de
ntd11!LdrpProcessWork+0x148
ntd11!LdrpWorkCallback+@xbb
ntd11! TppWorkpExecuteCallback+@x13a
ntd11! TppWorkerThread+@x8f6
KERNEL32!BaseThreadInitThunk+@xid
ntd11!RtlUserThreadStart+0x28
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2023
Cl TOCTOU: Paged Reads
BB Process Monitor - Sysinternals: www.sysinternals.com - Ei x
File Edit Event Filter Tools Options Help
Sallcs6 W|\VYAO| s&s! % © |e ie DoF
Relative Time Process Name PID Operation Path Result Detail
00:00:17.0969135 “Mi services.exe 508  CloseFile C:\Windows \System32\EventAggregation dil SUCCESS |
00:00:17.0971696 “MF services.exe 508 W CreateFile C:\Windows \System32\\EventAggregation dll REPARSE Desired Access: Read Data/List Directory, Execute/Trav... |
00:00:17.1006151 “i services.exe 508 j CreateFile \\127.0.0.1\C$\Windows\System32\EventAggregation.dilbak SUCCESS Desired Access: Read Data/List Directory, Execute/Trav... |
00:00:17.1017799 “MW services.exe 508 je CreateFileMapping \\127.0.0.1 Windows \System32\EventAggregation.dilbak FILE LOCKED WI... SyncType: SyncTypeCreateSection, PageProtection: PA.
00:00:17.1018504 -m@ services.exe 508 jy ReadFile \\127.0.0.1\C$\Windows\System32\EventAgaregation.dilbak SUCCESS Offset: 0, Length: 90,112, 1/0 Flags: Non-cached, Paging... j
00:00:17.1018615 “Br services.exe 508 Ws ReadFile C:\Windows \System32\Event Aggregation dil. bak SUCCESS Offset: 0, Length: 90,112, 1/O Flags: Non-cached
00:00:17.1027614 “iF services.exe 508 i QueryEAFile 127.0.0.1
00:00:17.1057495 “i services.exe 508 We QueryEAFile \\127.0.0.1
00:00:17.1058253 <M services.exe 508 fy SetEAFile \\127.0.0.1
00:00:17.1064822 “Wservices.exe 508  CreateFileMapping \127.
00:00:17.1066262
508 «Load Image
Windows \System32\EventAggregation.dilbak ACCESS DENIED
Windows \System32\EventAggregation.dilbak ACCESS DENIED
Windows \System32\EventAggregation.dilbak ACCESS DENIED
Windows \System32\EventAggregation.dilbak SUCCESS Sync Type: Sync TypeOther
Windows \ 5 penne ato Renda dilbak SUCCESS Image Base: Ox 7df0450000, Image Size: 0x 16000
@ services.exe SUCCESS
ge arshomennicss hae veneer dil bak : 0, Length: 4,096, 1/O Flags: Non-cached, Paging |...
00:00:51. 1701225 @ services.exe 508 i ReadFile C:\Windows \System32\Event Aggregation dil. bak SUCCESS Offset: 0, Length: 4,096, 1/O Flags: Non-cached
00:00:51.1702783 “@ services.exe 508 % ReadFile \\127.0.0.1\C$\Windows\System32\EventAggregation.dilbak SUCCESS Offset: 53,248, Length: 16,384, 1/O Flags: Non-cached, P..
00:00:51.1702900 “WF services.exe 508 Ws ReadFile C:\Windows \System32\\EventAggregation dil bak SUCCESS Offset: 53,248, Length: 16,384, 1/O Flags: Non-cached
00:00:51.1715041 “Mservices.exe 508 Sy ReadFile \\127.0.0.1\C$\Windows\System32\EventAggregation.dilbak SUCCESS Offset: 73,728, Length: 4,096, 1/O Flags: Non-cached, Pa...
00:00:51.1715132 “MW services.exe 508 jy ReadFile C:\Windows \System32\EventAggregation dil bak SUCCESS Offset: 73,728, Length: 4,096, 1/O Flags: Non-cached
00:00:51.1715971 “H services.exe 508 % ReadFile \\127.0.0.1\CS\Windows\System32\EventAggregation.dilbak SUCCESS Offset: 4.096, Length: 4,096, I/O Flags: Non-cached, Pag..
00:00:51.1716052 “i services.exe 508 i ReadFile C:\Windows \System32\EventAggregation dil. bak SUCCESS Offset: 4,096, Length: 4,096, I/O Flags: Non-cached
00:00:51.1716701 “Wservices.exe 508 Sy ReadFile \\127.0.0.1\C$\Windows\System32\EventAggregation.dilbak SUCCESS Offset: 4,096, Length: 32,768, 1/O Flags: Non-cached, Pa...
00:00:51.1716803 “MF services.exe 508 js ReadFile C:\Windows \System32\Event Aggregation dil. bak SUCCESS Offset: 4.096, Length: 32,768, 1/O Flags: Non-cached
00:00:51.1717834 ‘ services.exe 508 ws ReadFile \\127.0.0.1\CS\Windows\System32\EventAggregation.dilbak SUCCESS Offset: 40,960, Lenath: 4,096, 1/O Flags: Non-cached, Pa..
00:00:51.1717897 “Mf services.exe 508 We ReadFile C:\Windows\System32\\Event Aggregation dil bak SUCCESS Offset: 40,960, Length: 4,096, 1/O Flags: Non-cached
00:00:51.1718510 “Mservices.exe 508 fy ReadFile \\127.0.0.1\C$\Windows\System32\EventAggregation.dilbak SUCCESS Offset: 36,864, Length: 12,288, 1/O Flags: Non-cached, P...
00:00:51.1718630 “HF services.exe 508 fy ReadFile C:\Windows \System32\EventAggregation dil. bak SUCCESS Offset: 36,864, Length: 12,288, 1/O Flags: Non-cached
Showing 26 of 43 events (60%) Backed by virtual memory
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2023
Cli TOCTOU: Code Execution
Break instruction exception - code 8@000003 (first chance)
0033 :e0007fFF addbiS5@ cc int 3
5: kd> db @rip
eeee7fff addbi55@ cc 98 96 96 98 986 96 98-98 96 96 96 90 96
eeee7ftf addbi56@ ca fe c@ de ca fe c@ de-ca fe c@ de ca fe
eeee7fff addbiS576@ ca fe c@ de ca fe c@ de-ca fe c@ de ca fe
eeee7fff addbi58@ ca fe c@ de ca fe c@ de-ca fe c@ de ca fe
eeee7fff addbi599 ca fe c@ de ca fe c@ de-ca fe c@ de ca fe
eeee7fff addbiSa@ ca fe c@ de ca fe c@ de-ca fe c@ de ca fe
eeee7fff addbiSb@ ca fe c@ de ca fe c@ de-ca fe c@ de ca fe
eeee7fff addbi5c@ ca fe c@ de ca fe cO de-ca fe c@ de ca fe
5: kd> dx @$curprocess->Name
@$curprocess->Name : services.exe
Length : @xc
5: kd> dx @$curprocess->KernelObject->Protection
OM SB iiteieiece che euerereierere
EO GE oionewicwciessecemeee
CO d@  ssseesecoeca
€QO G0 2i2osc5cote
CO de fssesiecewcetace
CO ge jseisSoonetace
@$curprocess->KernelObject->Protection [Type: _PS PROTECTION]
[+0xe8@0] Level : @x61 [Type: unsigned char]
[+90x@80 ( 2: 8)] Type : @x1 [Type: unsigned char]
[+0xe@@ ( 3: 3)] Audit : @x@ [Type: unsigned char]
[+@x@00 ( 7: 4)] Signer : @x6 [Type: unsigned char]
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2023
= =
Conclusions: Patchin
a
ppp
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air 3rd generation and later, iPad 5th ROOT->KERNEL LPE REPORTED
_ a
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
