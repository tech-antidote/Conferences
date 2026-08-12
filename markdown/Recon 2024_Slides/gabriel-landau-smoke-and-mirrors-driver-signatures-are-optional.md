---
title: "Smoke and Mirrors Driver Signatures Are Optional"
speakers: ["Gabriel Landau"]
conference: "REcon"
conference_full: "REcon 2024"
edition: ""
year: 2024
source_pdf: "Recon 2024_Slides/Gabriel Landau_Smoke and Mirrors Driver Signatures Are Optional.pdf"
pages: 58
sha256: "1643dd276e13ff4a110c51d6895c7ed53aa68e7498f73e1097544ef190ca1318"
text_chars: 29130
ocr_pages: 9
has_ocr: true
redacted_secrets: 0
companion_files: ["Gabriel Landau_Smoke and Mirrors Driver Signatures Are Optional_code.txt"]
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:29:26Z"
---
# Smoke and Mirrors Driver Signatures Are Optional

**Speakers:** Gabriel Landau  
**Conference:** REcon 2024  
**Source:** `Recon 2024_Slides/Gabriel Landau_Smoke and Mirrors Driver Signatures Are Optional.pdf` (58 pages)


## Slide 1

REcon Montreal 2024

**Smoke and Mirrors: Driver Signatures are Optional** Gabriel Landau

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
REcon Montreal 2024
Smoke and Mirrors:
Driver Signatures are Optional
Gabriel Landau
& elastic security labs
```

## Slide 2

# **whoami**

Low-level Windows [reverse] engineer Help build Elastic Endpoint Security Detecting malware tradecraft Attack & defense of EDR Presented research at: BlueHat IL Shmoocon Black Hat USA Black Hat Asia

Pic

Blue, formerly red

## Slide 3

**Chapter 1 - Windows File Sharing** More than you’ve ever wanted to know about sharing violations.

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Chapter 1 - Windows File Sharing
More than you’ve ever wanted to know about sharing violations.
@ napster XG
The Wtrate Hap
```

## Slide 4

# **Opening Files - Access Rights**

**CreateFile** - Win32 API to open or create files.

- ntdll analog is **NtCreateFile** .

- Kernel driver analog is **ZwCreateFile** .

Specify desired access rights:

- **FILE_READ_DATA**

- **FILE_WRITE_DATA**

- **DELETE**

-

Pic

<u>https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-createfilew https://learn.microsoft.com/en-us/windows/win32/fileio/file-security-and-access-rights</u>

## Slide 5

# **Opening Files - Share Mode**

**FILE_SHARE_READ** / **FILE_SHARE_WRITE** / **FILE_SHARE_DELETE**

“I’m okay with others reading/writing/deleting this file while I’m using it.” As file is opened:

- **DesiredAccess** is tested against **ShareMode** of all existing file handles

- **ShareMode** is tested against **GrantedAccess** of all existing file handles

<u>https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-createfilew https://learn.microsoft.com/en-us/windows/win32/fileio/creating-and-opening-files</u>

## Slide 6

**Opening Files - Sharing Violation DesiredAccess** / **ShareMode** incompatibilities fail the **CreateFile** call.

- **ERROR_SHARING_VIOLATION** / **STATUS_SHARING_VIOLATION**

<u>https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-createfilew https://learn.microsoft.com/en-us/windows/win32/fileio/creating-and-opening-files</u>

## Slide 7

# **Opening Files - Exclusive Access**

Set **ShareMode** =0 for exclusive access to files until you close the handle.

<u>https://learn.microsoft.com/en-us/windows/win32/fileio/creating-and-opening-files</u>

## Slide 8

# **I/O Flow (Abbreviated)**

What happens when a program opens a file?

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
I/O Flow (Abbreviated)
What happens when a program opens a file?
LN Zo”
NtCreateFile ObOpenObjectByName IofCallDriver NtfsFsdCreate
System Service Object Manager I/O Manager Filesystem
® Windows Object Explorer 64-bit (Administrator)
File View Object Find Extras Plugins Help
Name Type Additional Information
8
© Objectiypes @ BTH#MS_BTHPAN#7&20f38eb4&082#{cac88424-... SymbolicLink
> Sessions "|| @ BTHEMS_ RFCOMM#78&20F38eb480802{9e16888d... SymbolicLink
(2 ArcName
> NLS
(3 Windows
7} GLOBAL?
@ CimfsControl SymbolicLink \Device\cimfs\control
\GLOBAL??\ DISPLAY#Default_Monitor#4&427137e&0&UIDOF{ e6f07b5f-ee97-4a90-b076-33f57bf4eaa7}
```

## Slide 9

# **I/O Flow (Abbreviated)**

What happens when a program opens a file?

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
I/O Flow (Abbreviated)
What happens when a program opens a file?
Child-SP
FFF¥8580° 26e66c98
F¥F¥8580° 26e66ca0
FFF¥8580° 28e66ce0
F¥¥¥8580° 26e66d50
F¥F¥8580° 20e66e00
FFF¥8580° 20e66e40
FFF¥8580° 20e66e908
F¥F¥8580° 20067000
F¥¥¥8580° 20e671d0
F¥F¥8580° 20067300
F¥F¥8580° 2006730
F¥F¥8580° 20e67450
RetAddr
F¥¥F¥800° 3742d935
FF¥FF800° 330b710F
F¥¥F¥800° 330e9f54
Ff¥¥F800° 3742d935
F¥¥¥¥800° 37444704
FF¥¥F800° 3783ec6b
FF¥FF800° 37833527
Ff¥¥£800° 3783baca
F¥¥F¥800° 3782ae8b
F¥¥F¥800° 37828fb9
F¥¥F¥800° 376119c8
eeee7 fff Sb68da84
Call Site ;
Ntfs!NtfsFsdCreate riHesystel
nt! IofCallDriver+0x55
FLTMGR! FltpLegacyProcessingAfterPreCallbacksCompleted+0x28f
FLTMGR! FltpCreate+0x324
nt! IofCallDriver+0x55 /O Manager
nt! IoCal1DriverwithTracing+0x34
nt! IopParseDevice+@x11bb
nt! ObpLookupObjectName+0x1117 IDje
nt! ObOpenObjectByNameEx+0xifa
nt! IopCreateFile+@x132b
nt! NtCreateFile+0x79 System Servic
nt! KiSystemServiceCopyEnd+0x28 KERN
lo Fit IR IRIE IS IS BIS IS IRIS ISIS IBIS
Dib id [LIN Hoe Im [6 [60 IN [oh [un Le [We Ih | 1
egee0090  da3fe5538
eeeeGe9e da3fe560
ee8eeese da3febde
08000090 da3fe730
eee8e0090° da3fe960
eeee7 fff 58d741e9
ee0e7 fff 58d73c56
eeee7 fff 58d75343
eee0e7 fff 58d732ae
eeee7 fff 4b2afc16
ntdll!NtCreateFile+0x14 LiSEE
KERNELBASE ! CreateFileInternal+0x579
KERNELBASE ! CreateFileW+0x66
KERNELBASE ! BasepLoadL ibraryAsDataFileInternal+0x293
KERNELBASE ! LoadLibraryExw+0xe@
```

## Slide 10

# **Sharing Enforcement - I/O Manager**

Filesystems call **IoCheckLinkShareAccess** to see whether **DesiredAccess** / **ShareMode** is compatible with existing handles.

**NTSTATUS NtfsCheckShareAccess(FileObject, DesiredAccess, ShareAccess) {**

**ntStatus = IoCheckLinkShareAccess( FileObject, DesiredAccess, ShareAccess); if (!NT_SUCCESS(ntStatus)) { return ntStatus; } ... }**

<u>https://github.com/Microsoft/Windows-driver-samples/blob/622212c3fff587f23f6490a9da939fb85968f651/filesys/fastfat/create.c#L6822-L6884</u>

## Slide 11

# **Sharing Enforcement - File Mapping**

File mappings (section objects) allow files to be readable/writable after handles are closed.

**ZwOpenFile File Handle ZwCreateSection Section Handle ZwMapViewOfSection Memory Mapped View**

**NTSTATUS NtfsOpenAttributeCheck(...) {**

**if (!FlagOn(ShareMode, FILE_SHARE_WRITE) && MmDoesFileHaveUserWritableReferences(FileObject->SectionObjectPointer)) { return STATUS_SHARING_VIOLATION; } ... }**

<u>https://github.com/Microsoft/Windows-driver-samples/blob/622212c3fff587f23f6490a9da939fb85968f651/filesys/fastfat/create.c#L6858-L6870</u>

## Slide 12

**Sharing Enforcement - Executables** Files mapped as executable images (EXEs/DLLs/etc) **must be immutable** while in use. In other words, **ZwMapViewOfSection(SEC_IMAGE)** implies no-write-sharing.

**NTSTATUS NtfsOpenAttributeCheck(...) { // Block writes to active image section objects if (FlagOn(DesiredAccess, FILE_WRITE_DATA) && FileObject->SectionObjectPointer.ImageSectionObject && !MmFlushImageSection(FileObject->SectionObjectPointer), MmFlushForWrite) { return STATUS_SHARING_VIOLATION } } ... }**

<u>https://github.com/Microsoft/Windows-driver-samples/blob/622212c3fff587f23f6490a9da939fb85968f651/filesys/fastfat/create.c#L3572-L3593</u>

## Slide 13

**Chapter 2 - Code Integrity** How do you trust the code that’s running on your system?

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Chapter 2 - Code Integrity
How do you trust the code that’s running on your system?
Open File - Security Warning
Do you want to run this file?
Name: .. GabrielLandau\Download
Publisher: Microsoft Corporation
Type: Application
From: C:\Users\GabrielLandau\Downloads\VisualStudioSetup...
Always ask before opening this file
iar While files from the Internet can be useful, this file type can potentially
‘ ) harm your computer. Only run software from publishers you trust.
```

## Slide 14

# **Authenticode**

Microsoft specification to digitally sign Portable Executable (PE) files.

Pic

Pic

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Authenticode
Microsoft specification to digitally
® ntoskrnl.exe Properties
curity
General
Details
Previous Versions
Digital Signatures
File Hashes
Signature list
Name of signer: Digest algorithm
Microsoft Windows sha256
Timestamp
Friday, April 5, 2024 1.
Sign Portable Executable
(PE) files.
Digital Signature Details
General Advanced
, Digital Signature Information
This digital signature is OK.
Signer information
Name: [Microsoft Windows SSS
E-mail: Not available
Signing time: Friday, April 5, 2024 03 AM
Countersignatures
Name of signer: E-mail address: Timestamp
Microsoft Time-S... Not available Friday, April 5, 2024...
```

## Slide 15

# **Authenticode Signing**

**Authentihash** algorithm computes hash over most (but not all) of the PE file.

Authentihash is signed using PKCS #7 and appended to PE as Security Directory (aka  Certificate Table).

Pic

<u>https://download.microsoft.com/download/9/c/5/9c5b2167-8017-4bae-9fde-d599bac8184a/authenticode_pe.docx</u>

## Slide 16

**Authenticode Implementations** User and kernel implementations to validate signatures.

The user implementation is out of scope for this talk.

The kernel implementation is the **Code Integrity** (CI) subsystem.

CI.dll protected from tampering by Secure Boot and Trusted Boot systems.

## Slide 17

# **Code Integrity**

Kernel Mode Code Integrity (KMCI)

- Enforces Driver Signing Enforcement and Vulnerable Driver Blocklist.

User Mode Code Integrity (UMCI)

- CI validates the signatures of EXEs and DLLs before allowing them to load.

- ● Enforces Protected Processes and Protected Process Light signature requirements.

- Enforces Microsoft Signer process mitigation ( **SetProcessMitigationPolicy** ).

- Enforces **/INTEGRITYCHECK** for FIPS 140-2 modules.

- Exposed to consumers as **Smart App Control** .

- Exposed to businesses as **App Control for Business** (formerly WDAC).

KMCI and UMCI implement different policies for different scenarios.

<u>https://learn.microsoft.com/en-us/windows/security/application-security/application-control/windows-defender-application-control/design/select-types-of-rules-to-cr eate</u>

<u>https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-setprocessmitigationpolicy https://x.com/GabrielLandau/status/1668353640833114131</u>

<u>https://learn.microsoft.com/en-us/windows/apps/develop/smart-app-control/overview https://learn.microsoft.com/en-us/windows/security/application-security/application-control/windows-defender-application-control/wdac https://learn.microsoft.com/en-us/windows/security/application-security/application-control/windows-defender-application-control/design/microsoft-recommended-drive</u> <u>r-block-rules</u>

## Slide 18

# **Chapter 3 - Incorrect Assumptions**

Let’s discuss a class of vulnerabilities resulting from incorrect assumptions.

## Slide 19

# **Incorrect Assumptions**

Microsoft docs imply that files successfully opened without write sharing can’t be modified under you.

_What if the filesystem doesn’t know that the file’s been modified?_

## Slide 20

# **Executable Image Section Paging**

Executable image sections originate from PE files.

MM can page these out if memory is needed:

- Never modified?  Discard it.  We already have a copy in the original PE.

- ● Modified?  Save it to the pagefile.

   - Example: ntdll was detoured.  MM copy-on-write created private copy.

Upon page fault:

- Never modified*?  Read the page from the original PE file.

- Modified? Grab the private copy from the pagefile.

* Exception: The memory manager may treat PE-relocated pages as unmodified, dynamically reapplying relocations during page faults.

## Slide 21

# **Page Hashes**

Optional list of hashes of each 4KB page of PE.  Allows MM to validate hashes of individual pages during page faults.

Static page hashes

- Stored within signature when file is signed.

- **signtool.exe /ph**

Dynamic page hashes

- Computed on the fly by CI when **SEC_IMAGE** is created and validated.

- Enables page hash enforcement even if signature does not include them.

Page hashes are not free - they use CPU and slow down page faults.

<u>https://learn.microsoft.com/en-us/windows/win32/seccrypto/signtool</u>

## Slide 22

# **Attacking Code Integrity**

Scenario:

1. Orphanage administrator enables macros in email attachment containing ransomware.

2. Ransomware employs UAC bypass to instantly elevate to Admin.

3. Ransomware fails to terminate AV running as Protected Process Light (PPL).

4. Ransomware author wants PPL rights so it can kill AV and ransom orphanage.

- Can it launch itself directly as PPL?

   - UMCI prevents improperly-signed EXEs and DLLs from loading into PPL.

- **CreateFile(FILE_WRITE_DATA)** to inject code into already-in-use DLL?

   - NTFS checks prevent **CreateFile(FILE_WRITE_DATA)** to in-use image sections. ○ Aforementioned **MmFlushImageSection** check.

- **FILE_WRITE_DATA** check is in NTFS.  What if we move the filesystem to another machine? ● SMB server could be a Samba server, or even a python script.

- Attacker can modify a DLL server-side, bypassing sharing restrictions.

- DLLs are incorrectly assumed to be immutable.

- **False File Immutability**

## Slide 23

# **Can Attacker Exploit Paging?**

Even if an attacker successfully exploits **false file immutability** to inject code into a PE, won’t page hashes catch this attack?

|||Authenticode|Page|Hashes|
|---|---|---|---|---|
|Kernel Drivers|||||
|Protected Processes|||||
|Protected Process Light|(PPL)||||

## Slide 24

# **Admin->PPL Exploit: PPLFault**

Disclosed by me at Black Hat Asia 2023.

<u>https://github.com/gabriellandau/PPLFault https://www.youtube.com/watch?v=5xteW8Tm410 https://i.blackhat.com/Asia-23/AS-23-Landau-PPLdump-Is-Dead-Long-Live-PPLdump.pdf</u>

## Slide 25

# **Mitigating PPLFault**

In February 2024, Microsoft added a check to mitigate PPLFault.

MM sets a flag requiring dynamic page hashes for images that originate from remote devices such as network redirectors like SMB.

<u>https://www.elastic.co/security-labs/inside-microsofts-plan-to-kill-pplfault</u>

## Slide 26

# **PPLFault - Takeaways**

What did we learn?

PPLFault successfully exploited bad assumptions in CI about DLL immutability, achieving unsigned WinTcb-Light PPL code execution.  For reasons out-of-scope, it was easy to chain this to full physical memory read/write, **compromising the entire OS in a few seconds** .

- The mitigation was narrow in scope - targeting images loaded from remote devices.

## Slide 27

# **Chapter 4 - New Research**

Can we exploit false file immutability in other ways?

Let’s look beyond executable image sections.

_What about attacks against data files?_

## Slide 28

# **Authenticode - Security Catalogs**

Security catalogs - detached Authenticode signatures.

- Signed array of Authentihashes in .cat files in **C:\Windows\System32\CatRoot**

- Every PE with Authentihash in list is considered to be signed by that signer.

**Hash Hash Hash Hash Hash Hash Hash Hash Hash Hash**

**Hash Hash Hash Signature**

## Slide 29

# **Authenticode - Security Catalogs**

Large list of catalogs.  CI loads them into kernel pool for fast lookup.

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Authenticode - Security Catalogs
Large list of catalogs. CI loads them into kernel pool for fast lookup.
| es Fy > | {F750E6C3-38EE-11D1-85E5-00C04FC295EE} _ Oo x
mo) LS}
iF} Home Share View a &
1H i's iv) LE
¢ & | Y. Cut  ¢ E co | "lis New item + BB Open -+ Select all |
Copy path = Bi Easy access ~ Be eait HE Select none
Pinto Quick Copy Paste Move Copy Delete Rename New Properties =
eres Gi Paste shortcut = tg <0 = Fontes = Be History i invert selection
Clipboard Organize New Open Select
€ > » & [EB « System32 » CatRoot » {F750E6C3-38EE-11D1-85E5-00CO4FC295EE} vo -
Name Date modified Type
2 Microsoft-Windows-Client-Desktop-Required-WOW64-Package001 1 ~31bf3856ad364e35~amd64~~ 10,0.19041.4046.cat 2/2/2024 7:47 AM Security Catalog
2 Microsoft-Windows-Client-Desktop-Required-WOW64-Package001 1 ~31bf3856ad364e35~amd64~~ 10.0.19041.4170.cat 3/7/2024 3:01 PM Security Catalog
4 Microsoft-Windows-Hello-Face-Package~31bf3856ad364e35~amd64~~ 10.0.19041.3636.cat 11/9/2023 6:45 AM Security Catalog
2 Microsoft-Windows-NetFx4-US-OC-Package~31bf3856ad364e35~amd64~~ 10.0.19041.3636.cat 11/9/2023 6:45 AM Security Catalog
& Microsoft-Windows-Client-Desktop-Required-WOW64-Package0010~3 1bf3856ad364e35 ~amd64~~10,0.19041.4170.cat 3/7/2024 3:00 PM Security Catalog
& Microsoft-Windows-Client-Desktop-Required-WOW64-Package0010~3 1bf3856ad364e35~amd64~ ~ 10.0.19041.4046.cat 2/2/2024 7:48 AM Security Catalog
1,956 items
```

## Slide 30

# **Code Integrity - Catalog Parsing**

Map File Into Memory Validate Signature Parse Catalog
nt!ZwOpenFile( CI!MinCrypK_ CI!I_MapFileHashes
  GENERIC_READ,  VerifySignedDataKModeEx
FILE_SHARE_READ )
nt!ZwCreateSection(
SEC_COMMIT )
nt!ZwMapViewOfSection

## Slide 31

# **Catalog Parsing - Key Insights**

## **ZwOpenFile(GENERIC_READ, FILE_SHARE_READ)**

- Denies write sharing to prevent catalog modifications during processing.

- Bad assumption - **false file immutability** .

## **ZwCreateSection(SEC_COMMIT)**

- Creates a data section.

- Not an image section - no page hashes.

Can we perform a PPLFault-style attack on security catalogs?

## Slide 32

# **Exploiting Security Catalogs**

Attacker Kernel &  Storage
(UserMode) Code Integrity (SMB)
Install Catalog
Request Unsigned Driver Load
Map Catalog
Request Catalog
Signed Catalog
Validate Signature  ✔
Purge W orking Set
Request Page
Parse
Unsigned Driver Authentihash
Load Unsigned Driver

## Slide 33

# **Exploit - Toggling the Catalog**

PPLFault used an oplock to
deterministically pause the  Hash Hash Hash Hash Hash Hash Hash Hash Signature
victim process then switch to
the payload DLL contents.
Hash Hash Hash Hash Hash Hash Hash Hash Signature
No good opportunities here
for oplocks.
Rapidly toggle the catalog  Hash Hash Hash Hash Hash Hash Hash Hash Signature
between benign and malicious
- probabilistic approach.
Hash Hash Hash Hash Hash Hash Hash Hash Signature
Choose hash near end of
catalog because parsing is
[probably] linear.
Hash Hash Hash Hash Hash Hash Hash Hash Signature
Hash Hash Hash Hash Hash Hash Hash Hash Signature

## Slide 34

# **Exploit - Race Condition**

Attacker needs CI to trigger a page fault between validation and parsing, but the page is already resident from recent validation.  Without a page fault, CI will use the same pages for validation and parsing.

To evict page from kernel memory, attacker must empty working set between **MinCrypK_VerifySignedDataKModeEx** and **I_MapFileHashes** .

Very short race window. Employ multiple approaches to slow CI and improve chances of winning race:

- Choose large security catalog (4MB).

- Dedicated thread emptying working set.

- Dedicated thread repeatedly loading unsigned driver.

- High-priority dummy threads spinning CPU cores to starve system worker threads.

## Slide 35

# **Fail - Signature Check Failed**

If the payload Authentihash is read during the signature check, the catalog will be rejected.

Validate Signature **Hash Hash Hash Hash Hash Hash Hash Hash Signature**

## Slide 36

# **Fail - Benign Catalog Parsed**

An even number of swaps (including zero) between signature validation and parsing means CI will parse the benign hash and reject our driver.

Validate Signature ✔ Hash Hash Hash Hash Hash Hash Hash Hash Signature
Context Switch  Hash Hash Hash Hash Hash Hash Hash Hash Signature
Parse Catalog  Hash Hash Hash Hash Hash Hash Hash Hash Signature

## Slide 37

# **Win - Payload Catalog Parsed**

CI must validate a benign catalog then parse a malicious one.

Validate Signature **Hash Hash Hash Hash Hash Hash Hash Hash Signature** Validate Signature ✔ **Hash Hash Hash Hash Hash Hash Hash Hash Signature** Parse Catalog **Hash Hash Hash Hash Hash Hash Hash Hash Signature**

## Slide 38

# **Exploit Demo!**

Windows 11 23H2 22631.3447 (April 2024)

## Slide 39

# **Chapter 4 - Avoiding Pitfalls**

To avoid this type of bug, we first need to understand it better.

## Slide 40

# **Double Read / Fetch**

Imagine a shared memory mapping for an IPC mechanism.  Double Read is a TOCTOU where victim reads a value from attacker-controlled shared memory twice.

Attacker changes memory between the reads, resulting in a unexpected victim behavior.

Example:

- Attacker initially specifies a small length field.

   - **pPacket->length = 16;**

- Victim code allocates a small buffer to hold data.

   - **pBuffer = malloc(pPacket->length);**

**struct IPC_PACKET {**

**SIZE_T length; UCHAR data[]; };**

- Attacker changes to large length value.

   - **pPacket->length = 32;**

- Victim code uses new length, copying too much data and overflowing buffer. **○ memcpy(pBuffer, pPacket->data, pPacket->length);**

Windows kernel (and drivers) often operate directly on user mode memory.

- Significant consideration for **METHOD_DIRECT** IOCTL handlers.

Recent example: <u>https://exploits.forsale/24h2-nt-exploit/</u>

## Slide 41

# **Call To Action**

Treat attacker-writable files as subject to double-read vulnerabilities.

Denying write sharing does not necessarily prevent modification.

## Slide 42

# **Affected Operations**

What types of operations are affected by **False File Immutability** ?

|Operation|API|Mit|igations|
|---|---|---|---|
|Image Sections|**CreateProcess**|1.|Enable Page Hashes.|
||**LoadLibrary**|||
|Data Sections|**MapViewOfFile**|1.|Avoid double reads.|
|||2.|Copy the file to a heap buffer before processing.|
|||3.|Prevent paging via**MmProbeAndLockPages/VirtualLock**.|
|Regular I/O|**ReadFile**|1.|Avoid double reads.|
|||2.|Copy the file to a heap buffer before processing.|

## Slide 43

# **What Else Could Be Vulnerable?**

Note: **ZwReadFile** may be used for more than just files.  Only uses on files (or those which could be coerced into operating on files) could be vulnerable.

## Slide 44

# **What Else Could Be Vulnerable?**

Note: **ZwReadFile** may be used for more than just files.  Only uses on files (or those which could be coerced into operating on files) could be vulnerable.

## Slide 45

# **Don’t Forget About User Mode**

_Any user-mode application_ that calls **ReadFile** , **MapViewOfFile** , or **LoadLibrary** on an attacker-controllable file, denying write sharing for immutability, may be vulnerable. Hypothetical examples:

- **MapViewOfFile**

- Auto-elevate installers that apply downloaded patches if correctly signed

- ● **ReadFile**

   - Memory corruption in file parsers by changing double-read values

      - AV engines

      - Search indexers

- **LoadLibrary**

   - RPC server relying on **SetProcessMitigationPolicy(ProcessSignaturePolicy)** to prevent DLL injection via impersonation system drive remapping attacks.

<u>https://bugs.chromium.org/p/project-zero/issues/detail?id=2451</u>

## Slide 46

# **Chapter 5 - Mitigating the Exploit**

MSRC won’t service Admin -> Kernel vulnerabilities by default.

- “service” means “fix via security update.”

As a third-party AV dev, I can’t fix CI.dll.  How can I protect my customers?

What can Microsoft do to fix it?

<u>https://www.microsoft.com/en-us/msrc/windows-security-servicing-criteria</u>

## Slide 47

# **Third-Party Mitigation**

To mitigate **ItsNotASecurityBoundary** , I wrote **FineButWeCanStillEasilyStopIt.sys**

Filesystem Minifilter. In Pre **IRP_MJ_ACQUIRE_FOR_SECTION_SYNCHRONIZATION** callback invoked during **ZwCreateSection** , if:

- **SyncType == SyncTypeCreateSection &&**

- **PageProtection == PAGE_READONLY &&**

- **FlagOn(TargetFileObject->DeviceObject->Characteristics, FILE_REMOTE_DEVICE) &&**

- **Data->RequestorMode == KernelMode &&**

- **FltGetRequestorProcess(Data) == PsInitialSystemProcess &&**

- **IsCalledByCodeIntegrity() && // Check caller via RtlWalkFrameChain**

- **Contains catalog magic bytes and Certificate Trust List PKCS #7 OID.**

then deny the operation.

Messy, right?  It’s likely imperfect too.  Compare that to a three-line fix in CI.

## Slide 48

# **DSE Exploit Mitigation #1**

Map File Into Memory Validate Signature Parse Catalog nt!ZwOpenFile( CI!MinCrypK_ CI!I_MapFileHashes GENERIC_READ, VerifySignedDataKModeEx FILE_SHARE_READ) nt!ZwCreateSection( SEC_COMMIT) nt!ZwMapViewOfSection **nt!ExAllocatePool2** Copy the file to a heap buffer before processing. **nt!RtlCopyMemory**

## Slide 49

# **DSE Exploit Mitigation #2**

Map/ **Lock** File Into Memory Validate Signature Parse Catalog nt!ZwOpenFile( CI!MinCrypK_ CI!I_MapFileHashes GENERIC_READ, VerifySignedDataKModeEx FILE_SHARE_READ) nt!ZwCreateSection( SEC_COMMIT) nt!ZwMapViewOfSection **nt!IoAllocateMdl** Lock pages into RAM to block working set eviction. **nt!MmProbeAndLockPages**

## Slide 50

# **Mitigating the Exploit - HVCI**

If HVCI is enabled, CI.dll doesn’t do catalog parsing.

- CI sends the catalog contents to the Secure Kernel (SK)

- SK runs in a separate virtual machine.

- SK puts catalog contents in its own secure allocation.

- Signature validation and parsing are done from this secure allocation.

- Attack is mitigated because file changes have no effect on the secure allocation.

<u>https://learn.microsoft.com/en-us/windows/win32/procthread/isolated-user-mode--ium--processes</u>

## Slide 51

# **Disclosure Timeline**

- 2024-02-14 Reported **ItsNotASecurityBoundary** and **FineButWeCanStillEasilyStopIt** to MSRC as VULN-119340, suggesting **ExAllocatePool** and **MmProbeAndLockPages** as fixes, and offering to coordinate disclosure.

- 2024-02-22 I asked MSRC for an update

- 2024-02-29 Windows Defender team reached out to coordinate disclosure.

- 2024-04-23 Microsoft releases KB5036980 preview with **MmProbeAndLockPages** fix.

- 2024-05-14 Fix reaches GA for desktop releases.

- 2024-05-20 I gave this talk at BlueHat IL

<u>https://support.microsoft.com/en-us/topic/april-23-2024-kb5036980-os-builds-22621-3527-and-22631-3527-preview-5a0d6c49-e42e-4eb4-8541-33a7139281ed</u>

## Slide 52

# **Inside The Mitigation**

**I_MapAndSizeDataFile** is the legacy vulnerable code.

<u>https://www.youtube.com/watch?v=ha-uagjJQ9k</u>

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Inside The Mitigation
I_MapAndSizeDataFile is the legacy vulnerable code.
-~_ > 4 v10 = ZwiapViewOfSection(
SectionHandle,
; ' (HANDLE) OxFFFFFFFFFFFF FFFFLL,
BaseAddress,
y hel ,
I
! L
v1l2 = FileHandle;
goto LABEL _ 16;
4
I
OLD anb BUSTED
bs > 17 = 5 —*> eo
0004CC04\ I MapAndSizeDataFile:83 (1C004DC04)
```

## Slide 53

# **Inside The Mitigation**

**CipMapAndSizeDataFileWithMDL** contains the fix.

<u>https://www.youtube.com/watch?v=ha-uagjJQ9k</u>

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Inside The Mitigation
CipMapAndSizeDataFileWithMDL contains the fix.
v13 = ZwCreateSection(&SectionHandle, SECTION_MAP_READ,
if ( v13 >= @ )
{
v13 = ZwiapViewOfSection(
SectionHandle,
(HANDLE )@xFFFFFFFFFFFFFFFFi64,
vi2,
0164,
ois4,
0i64,
&ViewSize,
ViewShare,
a,
2u)5
if ( v13 >= @ )
if ( ale )
{
if ( ViewSize > @xFFFFEFFF )
{
v13 = -1073741760;
goto LABEL_16;
Mdl = IoAllocateMdl(*v12, ViewSize, @, @, @i64);
v1i5 = Mdl;
if ( IMdl )
{ New t
vi3 = -1073741676;
goto LABEL_16;
4
ae
MmProbeAndLockPages(Mdl, @, IoReadAccess);
*al@ = v15;
goto LABEL_15;
}
t
0004E138 CipMapAndSizeDataFileWithMDL:-57 (1C004F138)
```

## Slide 54

# **Disclosure Timeline**

- 2024-02-14 Reported **ItsNotASecurityBoundary** and **FineButWeCanStillEasilyStopIt** to MSRC as VULN-119340, suggesting **ExAllocatePool** and **MmProbeAndLockPages** as fixes, and offering to coordinate disclosure.

- 2024-02-22 I asked MSRC for an update

- 2024-02-29 Windows Defender team reached out to coordinate disclosure.

- 2024-04-23 Microsoft releases KB5036980 preview with **MmProbeAndLockPages** fix.

- 2024-05-14 Fix reaches GA for desktop releases.

- 2024-05-20 I gave this talk at BlueHat IL

- **2024-06-14 MSRC responded:**

   - **“We have completed our investigation and determined that the case doesn't meet our bar for servicing at this time. As a result, we have opened a next-version candidate bug for the issue, and it will be evaluated for upcoming releases. Thanks, again, for sharing this report with us.”**

<u>https://support.microsoft.com/en-us/topic/april-23-2024-kb5036980-os-builds-22621-3527-and-22631-3527-preview-5a0d6c49-e42e-4eb4-8541-33a7139281ed</u>

## Slide 55

# **It’s All About Incentives**

Admin -> PPL / Kernel bugs:

- 4 months for MSRC response.

- Multiple occurrences, not just one.

- This is a different bug

- My cable company is more responsive.

- _Is MSRC sufficiently staffed?_

Researchers must wait months for expected WONTFIX responses before publishing.

- Disrespectful of our time.

<u>https://x.com/GabrielLandau/status/1801255800607797321</u>

## Slide 56

# **It’s All About Incentives**

Many such bugs eventually get fixed, which acknowledges that these bugs DO matter. ● No credit.

- No bounty.

- No CVE.

- Why bother reporting?

- Can there be a middle ground between WONTFIX and Security Boundary?

- Is MSRC creating perverse incentives?

“Did I report these issues to Microsoft? Microsoft has made it clear that they will not fix issues only affecting PP and PPL in a security bulletin. Without a security bulletin the researcher receives no acknowledgement for the find, such as a CVE. The issue will not be fixed in current versions of Windows although it might be fixed in the next major version. Previously confirming Microsoft’s policy on fixing a particular security issue was based on precedent, however they’ve recently published a list of Windows technologies that will or will not be fixed in the Windows Security Service Criteria which, as shown below for Protected Process Light, Microsoft will not fix or pay a bounty for issues relating to the feature. **Therefore, from now on I will not be engaging Microsoft if I discover issues which I believe to only affect PP or PPL.** ”

James Forshaw

<u>https://googleprojectzero.blogspot.com/2018/10/injecting-code-into-windows-protected.html</u>

## Slide 57

# **Summary**

Bug class: False File Immutability

PPLFault: Admin -> PPL [-> Kernel via GodFault/AngryOrchard]

- Exploits bad immutability assumptions about image sections in CI/MM.

- ● Reported September 2022

- Patched February 2024 (~510 days)

ItsNotASecurityBoundary: Admin -> Kernel

- Exploits bad immutability assumptions about data sections in CI.

- ● Reported February 2024

- Patched May 2024 (~90 days)

Call to action

- Treat attacker-writable files as subject to double-read vulnerabilities.

- ● Denying write sharing is insufficient to prevent modification.

More exploits: TBA

<u>https://x.com/GabrielLandau/status/1757818200127946922 https://twitter.com/GabrielLandau/status/1801255800607797321</u>

## Slide 58

# **Conclusion**

Gabriel Landau at Elastic Security.  Any opinions expressed are my own.

Thanks to the Windows Defender team for collaborating on disclosure and fixes!

Exploit PoC to be released on Twitter later today.

Twitter/  : @GabrielLandau

## Companion resources

### `Gabriel Landau_Smoke and Mirrors Driver Signatures Are Optional_code.txt`

```text
https://x.com/GabrielLandau/status/1807471934780969214
```
