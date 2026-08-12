---
title: "Chaining Microsoft Binaries to get Privileged Primitives in the Windows kernel"
speakers: ["Angelo Frasca Caccia"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: null
source_pdf: "DEF CON 34/DEF CON 34 - Angelo Frasca Caccia - Chaining Microsoft Binaries to get Privileged Primitives in the Windows kernel - Binariesto Achiev.pdf"
pages: 45
sha256: "890f8a1a50b55f2d0f9905b8a2eb0c6493873e1df4f43e6e1a257752801c6d92"
text_chars: 17408
ocr_pages: 4
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:12:12Z"
---
# Chaining Microsoft Binaries to get Privileged Primitives in the Windows kernel

**Speakers:** Angelo Frasca Caccia  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Angelo Frasca Caccia - Chaining Microsoft Binaries to get Privileged Primitives in the Windows kernel - Binariesto Achiev.pdf` (45 pages)

## Slide 1

Chaining Microsoft Binaries to Achieve Privileged Primitives in the Windows Kernel

###### Angelo Frasca Caccia

Senior Security Researcher - SentinelOne (Exploit & Anti Tampering Team)

###### Alejandro Pinna Toral

Security Research Manager - SentinelOne (Offensive Security Team)

## Slide 2

### **<u>$~Whoami</u>**

- **Angelo Frasca Caccia** - Senior Security Researcher @SentinelOne;

- ●Windows Exploit Detection & Anti-tampering Security Research;

- ●Previously Red Teamer & Penetration Tester;

- ●Independent security researcher in the free time, author of the _ShellGhost_ Evasion Concept & _CreateRemoteThreadPlus_ .

<u>@lem0nSec</u>

<u>linkedin.com/in/angelo-frasca-caccia</u>

2

## Slide 3

## Presentation Agenda

###### ■ Abusing System Guard Runtime Monitor

   - SGRM Purpose & Core Components

   - SgrmAgent Internals & Abuse

- PPL Injection in 2026

   - PPL Processes: history & abuse

   - Old Code Injection through COM

   - Overcoming Patches

- Exploit Chain

   - Shellcode Execution in WerFaultSecure

   - Talking to SGRM through Shellcode

   - Demo: APC-based process tampering

   - Detection & Prevention for Defenders

   - Why this matters?

## Slide 4

### **<u>System Guard Runtime Monitor (SGRM)</u>**

###### **What is SGRM?**

SGRM acts as an extension of **Windows Defender** . Its purpose is to monitor OS integrity through custom **Lua rules** .

- **●Malicious Device Monitoring:** Protects against malicious drivers (e.g. Mimidrv.sys);

- **●Runtime Integrity Attestation:** Monitors process, thread, driver objects against DKOM tampering, as well as firmware/CPU via manufacturer-specific MSRs.

###### **Timeline**

- **●Introduced**

   - **October 2017**

   - Windows 10 1709 - Fall Creators Update

- ●Infrastructure Disabled

○January 2025

   - ●Full Removal

      - **May 2025**

- _<u>https://www.microsoft.com/en-us/security/blog/2018/04/19/introducing-windows-defender-system-guard-runtime-attestation/</u>_

- _-_ _<u>https://en.ittrip.xyz/windows/troubleshooting/event7023-may25-fix</u>_

4

## Slide 5

### **<u>SGRM Core Components</u>**



###### **SgrmBroker.exe**

**Userland Service**

Main userland service responsible for loading signed Lua assertions and brokering the assertion engine system access.



**SgrmAgent.sys Kernel Driver**

Driver for privileged operations (kernel objects inspection, MSR reading, file/process mapping).



**SgrmEnclave_secure.dll VTL-1 Enclave**

Assertion engine running in VTL-1 to perform secure processing.

  **SgrmEnclave.dll Fallback Engine**

**SgrmLpac.exe RPC Server**

"Fallback" assertion engine in case RPC server initiating HTTP POST Virtualization-Based Security (VBS) requests upon integrity violations. is not available.

_<u>https://infocon.org/mirrors/vx%20underground%20-%202025%20June/Papers/Windows/Internals%20and%20Analysis/2022-08-02%20-%20Inside%20Windows%20Defender%20System%20Guard%20Runtime%20Monitor.pdf</u>_

5

## Slide 6

### **<u>SgrmAgent Internals</u>**

6

## Slide 7

### **<u>SgrmAgent.sys - FastIoDispatch</u>**

**IOCTL 0x9C402480 → OctpHandleInitRequest**

Initialization handler to be called upon first usage.

##### **IOCTL 0x9C402484**

**→ OctpMailboxDispatcher**

- Main driver dispatcher for internal routines.

- A 'sub-IOCTL' switch-case statement is used in substitution of single IOCTL calls.

- First double word in the input buffer acts as the switch _condition_ .

###### **Provides 20 internal routines, including:**

- Physical memory reading

- Kernel virtual memory reading

- File and process memory mapping

7

## Slide 8

### **<u>SgrmAgent.sys - OctpMailBoxDispatcher</u>**

|**Routine**|**Operation (case label)**|
|---|---|
|OctpHandleMapVirtualAddress|0x01|
|**OctpHandleGetReferencedProcessObject**|**0x03**|
|OctpHandleGetNextReferencedProcessObject|0x05|
|**OctpHandleGetNextReferencedThreadObject**|**0x06**|
|OctpHandleGetReferencedDriverObject|0x08|
|OctpHandleGetReferencedDeviceObject|0x0A|
|OctpHandleGetStructureOffsetSize|0x0C|
|**OctpHandleFreezeThread**|**0x0D**|
|OctpHandleThawThread|0x0E|
|OctpHandleCopyMemory|0x0F|
|OctpHandleMapFile|0x10|
|OctpHandleGetMemoryRegionInfo|0x12|
|OctpHandleGetThreadContext|0x13|
|OctpHandleGetMsrValue|0x15|
|OctpPurgeAll|0x16|

8

## Slide 9

### **<u>SgrmAgent.sys - OctpMailBoxDispatcher</u>**

###### Can we abuse the driver to tamper with security solutions?

OctpHandleFreezeThread!!!

9

## Slide 10

### **<u>OctpHandleFreezeThread</u>**

10

## Slide 11

### **<u>OctpHandleFreezeThread</u>**

- ●Allocate APC **normal context** ;

- ●Write target **_KTHREAD** into the normal context;

- ●Initialize **_KAPC** ;

- ●Initialize **_KEVENT** to the **non-signalled** state in the normal context;

- ●Queue _KAPC.

11

## Slide 12

### **<u>OctpHandleFreezeThread - APC Normal Routine</u>**

- **KeWaitForSingleObject** called by the thread on the event object;

   - **Thread waits** up until the event is set to the signalled state;

- ●APC rundown routine called for cleanup (normal context is freed).

12

## Slide 13

### **<u>OctpHandleFreezeThread - Requirements</u>**

- **g_FrozenThread** : links all normal contexts of currently frozen threads

   - ○First check makes sure the target thread is not yet frozen

- **g_refProcessObjects** : links all referenced processes in the driver

   - ○Second check makes sure the process the target thread belongs to is referenced

- **g_refThreadObjects** : links all referenced threads in the driver

   - ○Third check makes sure the target thread is referenced.

13

## Slide 14

### **<u>OctpHandleGetReferencedProcessObject</u>**

14

## Slide 15

### **<u>OctpHandleGetReferencedProcessObject</u>**

- ●Resolve **_EPROCESS** by PID;

- ●Allocates 0x28 bytes from Paged Pool to store process information;

- ●Populates allocation with **process information** (PID, _EPROCESS, process sequence number);

- **Links** the structure to **g_refProcessObjects** .

15

## Slide 16

### **<u>OctpHandleGetNextReferencedThreadObject</u>**

16

## Slide 17

### **<u>OctpHandleGetNextReferencedThreadObject</u>**

- ●Loops through the process **ThreadListHead** with PsGetNextProcessThread;

- ●Breaks the loop with PsQuitNextProcessThread if a match is found;

- ●Populates a 0x28-byte allocation with **thread information** and **links** it to **g_refThreadObjects** .

17

## Slide 18

### **<u>SgrmAgent.sys for Process Tampering</u>**

- **●OctpHandleGetReferencedProcessObject** : links process into a global linked list;

- ●Loop through process threads:

   - **○OctpHandleGetNextReferencedThreadObject** : takes a process and a thread object, and returns the next thread in the process ‘ThreadListHead’ field. The thread is linked to a global linked list;

   - **○OctpHandleFreezeThread** : freezes the thread by queuing the thread-freezing APC into it.

18

## Slide 19

### **<u>How do we communicate with SgrmAgent.sys?</u>**

19

## Slide 20

### **<u>SgrmAgent.sys - Interaction Requirements</u>**

●SgrmBroker **service SID embedded** within the device SDDL string;

- ○D:P(A;;GRGWGX;;;S-1-5-80-3706850399-3459138796-2835936764-562029542-397710147)

20

## Slide 21

### **<u>SgrmAgent.sys - Interaction Requirements</u>**

- ●Caller process **Protection level 98** (WinTCB);

- **First IRP_MJ_CREATE** call will grant the handle, subsequent calls will return access denied.

21

## Slide 22

### **<u>SgrmAgent.sys - Interaction Requirements</u>**

- ●SgrmBroker.exe meets all three pre-conditions:

   - ○Runs as WinTCB;

   - ○Has the expected service SID;

   - ○Opens a handle to the device “\Device\MSSGRMAGENTSYS” at service run.

22

## Slide 23

### **<u>SgrmAgent.sys Abuse</u>**

- ●Clone SgrmBroker’s handle to “ **\Device\MSSGRMAGENTSYS”** with **DuplicateHandle** ;

- ●Leverage cloned handle to instruct SgrmAgent.sys to freeze a process of choice.

- **DuplicateHandle** requires a handle to the source process with the **PROCESS_DUP_HANDLE** access right.

###### **How do we get a handle to SgrmBroker?**

23

## Slide 24

### **<u>PPL Injection in 2026</u>**

24

## Slide 25

### **<u>What are PPL Processes</u>**

- ●Protected processes were introduced in Windows Vista to protect software from piracy;

      - ○Protected Process Light (PPL) was an extension introduced in Windows 8.1 which enabled to protect also other system processes.

      - ○Handle opening is limited.

   - _<u>https://projectzero.google/2018/10/injecting-code-into-windows-protected.html</u>_

25

## Slide 26

### **<u>History of PPL Exploitation</u>**

- ●Most PPL injection exploits used to tamper with **ntdll!LdrpKnownDllDirectoryHandle** .

- ●This stores a handle to the **\KnownDlls** directory object. Core libraries are mapped from this, rather than being loaded from disk which requires signature checking.

- ●Any arbitrary write in a PPL process could potentially be turned into a code injection by **overwriting the KnownDlls handle with a fake one** . A call to LoadLibrary mapped the fake library.

- In 2018, James Forshaw posted an injection technique targeting **WerFaultSecure.exe** (WinTCB-signed) based on **IRundown::DoCallback** .

   - <u>https://projectzero.google/2018/11/injecting-code-into-windows-protected.html</u>

_-_ _<u>https://projectzero.google/2018/10/injecting-code-into-windows-protected.html</u> -_ _<u>https://projectzero.google/2018/11/injecting-code-into-windows-protected.html</u>_

26

## Slide 27

### **<u>Code injection using IRundown COM interface</u>**

return ((__int64 (__fastcall *)(__int64)) **pCallbackData->pfnCallback)(pCallbackData->pParam);**

27

## Slide 28

### **<u>Code injection using IRundown COM interface</u>**

**01**

###### **COM Object Load**

**Vulnerable Faultrep.dll**

**Faultrep.dll** (WerFaultSecure library) creates the following COM object while dumping an **AppContainer** : **HKCR\CLSID\{07FC2B94-5285-417E-8AC3-C2CE5240B0FA}**

**02**

###### **IRundown Initialization**

**Forcing IRundown**

Setting the CLSID ThreadingModel to “free” forces WerFaultSecure to initialize the **IRundown** interface.

**03**

###### **Memory Extraction**

**Unencrypted Dump**

A vulnerable **WerFaultSecure** version from **Windows 8.1** was used to generate an unencrypted memory dump of WerFaultSecure.

The dump was searched to locate the connection parameters for the active **IRundown** interface.

_-_ _<u>https://projectzero.google/2018/10/injecting-code-into-windows-protected.html</u>_

_-_ _<u>https://projectzero.google/2018/11/injecting-code-into-windows-protected.html</u>_

28

## Slide 29

### **<u>Patches</u>**

 **ReadOnly Handle**

**ntdll!LdrpKnownDllDirectoryHandle** This handle now lives in the _.mrdata_ section, which is marked **ReadOnly** at runtime.

 **Bypassed Call Path Faultrep.dl** **l no longer calls CCrashReport::ExemptFromPlmHandling**

This call path was replaced with a function that **skips COM initialization** entirely.

29

## Slide 30

### **<u>Overcoming Patches - Sideloading faultrep.dll</u>**

30

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Overcoming Patches - Sideloading faultrep.dll
B® Process Monitor - Sysinternals: www.sysinternals.com
File Edit Event Filter Tools Options Help
SCA See VIO Al\FQAA BaAQBA
Ti... Proces... >... Operati... Path
9:... Hlwerfau...
9:... Niwerfau...
o0oononononononoo ©
Hiwerfau
a .
> SentinelOne
.. Hwerfau...
.. Hiwerfau...
.. Hwerfau...
.. Hwerfau...
.. Hiwerfau...
.. Hwerfau...
.. Hwerfau...
.. Hiwerfau...
.. Hwerfau...
.. Hwerfau...
DMAMAA®AAAAADA DED
.. Create...
.. a.Create...
...C:\Users\test\Desktop\faultrep
.. Create...
.. Create...
.. s/Create...
.. »Create...
.. Create...
.. Create...
.. Create...
.. »Create...
.. alCreate...
.. Create...
“Create
C:\Users\test\Desktop\ADVAPI32.dll
C:\Users\test\Desktop\msvert.dll
C:\Users\test\Desktop\SECHOST.dIl
C:\Users\test\Desktop\RPCRT4-.dll
C:\Users\test\Desktop\dbghelp.dll
C:\Users\test\Desktop\RPCRT4.dll
C:\Users\test\Desktop\dbgcore.DLL
C:\Users\test\Desktop\SHELL32.dll
C:\Users\test\Desktop\USER32.dll
C:\Users\test\Desktop\GDI32.dll
C:\Users\test\Desktop\msvcp_win.dll
C:\Users\test\Desktop\GDI32.dll
C’\Users\test\Deskton\win3?1 dll
Result
NAME NOT FOUND
NAME NOT FOUND
NAME NOT FOUND
NAME NOT FOUND
NAME NOT FOUND
NAME NOT FOUND
NAME NOT FOUND
NAME NOT FOUND
NAME NOT FOUND
NAME NOT FOUND
NAME NOT FOUND
NAME NOT FOUND
NAME NOT FOUND
NAMF NOT FOUND
Petail
Desired ...
Desired ...
Desired ...
Desired ...
Desired ...
Desired ...
Desired ...
Desired ...
Desired ...
Desired ...
Desired ...
Desired ...
Desired
30
```

## Slide 31

### **<u>Overcoming Patches - WerFault CMD Arguments</u>**

_-_ _<u>https://helgeklein.com/blog/anatomy-of-werfault-exe-application-crash-error-reporting/</u>_

31

## Slide 32

#### **Overcoming Patches - WerFaultSecure “-s” Argument**

- ●WerFaultSecure.exe main function.

- The argument is a handle to a section object that is used by faultrep.dll in a **MapViewOfFile** call.

32

## Slide 33

### **<u>Overcoming Patches - Shared Section</u>**

1. Exploit creates a **section object** , then maps it with MapViewOfFile.

2. WerFaultSecure receives the handle to the section object through the ‘-s’ parameter.

3. Section object (already mapped by the exploit) is mapped by WerFaultSecure as well.

4. Result is a **shared section** between WerFaultSecure and the exploit.

33

## Slide 34

### **<u>Overcoming Patches - Shared Section</u>**

●IRundown::DoCallback calls
NtContinue with a custom
_CONTEXT .
●We can make WerFaultSecure call
any function with parameters.

34

## Slide 35

### **<u>Exploit Chain</u>**

35

## Slide 36

### **<u>Shellcode Execution in WerFaultSecure</u>**

**01. DoCallback calls RtlCaptureContext** DoCallback calls RtlCaptureContext and saves the current thread _CONTEXT in the shared section. We can now use this _CONTEXT as baseline.

###### **02. Exploit writes the shellcode in the shared section**

The exploit writes the shellcode in the shared section, after the _CONTEXT saved by RtlCaptureContext.

###### **03. DoCallback calls NtContinue which calls WriteProcessMemory**

Set up the saved _CONTEXT to make a WriteProcessMemory call, and craft a fake stack on the shared section storing a pointer to wer.dll .text section as return address. WriteProcessMemory writes the shellcode to wer.dll.

**04. WriteProcessMemory Returns** WriteProcessMemory returns to the wer.dll .text section, where the shellcode now lives.

36

## Slide 37

### **<u>Shellcode Execution in WerFaultSecure</u>**

Exploit.exe WerFaultSecure.exe wer.dll .text section
Shellcode
Shared section Shared section
1. DoCallback  → RtlCaptureContext
_CONTEXT _CONTEXT
2. Modify _CONTEXT and fake stack
3. DoCallback  →  NtContinue →
Shellcode Shellcode
WriteProcessMemory
4. Returns to  wer.dll with  shellcode
Fake Stack Fake Stack
37

## Slide 38

### **<u>Talking to SGRM through Shellcode</u>**

###### **01. Driver Handle Discovery**

_NtQuerySystemInformation_ ( _SystemHandleInformation_ ) to enumerate handles. Clone SgrmBroker’s handles with _DuplicateHandle_ and use _NtQueryObject_ to identify **"\Device\MSSGRMAGENTSYS"** .

**02. Target Process Referencing** Submit a **OctpHandleGetReferencedProcessObject** request to SgrmAgent.sys to reference the MsMpEng.exe process.

###### **03. Thread Freezing Loop**

Iterate through **OctpHandleGetNextReferencedThreadObject** and **OctpHandleFreezeThread** to suspend all threads of the process.

###### **04. Execution Window**

Sleep for 15 minutes to establish a window for activity.

###### **05. Restoration**

Send **PurgeAll** request to the driver to restore Defender.

38

## Slide 39

### **<u>Talking to SGRM through Shellcode</u>**

Talking to SGRM through Shellcode
WerFaultSecure.exe - PPL  SgrmBroker.exe - PPL MsMpEng.exe
(Shellcode)
DuplicateHandle
Driver
handle
User
(clone)
Kernel
1. Reference process
2. Reference threads
SgrmAgent.sys 3. Freeze threads
39

## Slide 40

### **<u>Demo</u>**

40

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Demo
a .
> SentinelOne
40
```

## Slide 41

41

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
te
(ikaogetat
Adiministrator:
\Users\test\Desktop>, O Virus & threat protection
Protection for your device against threat lave
O Virus & threat protection > Current threats
ra & Account protection 0 current threa’
Wesedtpelld -
ff) Firewall & network protection thi
5 App & browser contro 64 annie
I) Device security
£1 Device security Quick scan
} Device perlornance & health
a Cha
Bree & family options -
) Protection history
Virus & threat protection settings
<2 Virus & threat protection updates
G) Ransomware protection
IneDrive for file r ry option ase of a ransomware attack
Set up OneDeve
a ;
> SentinelOne
```

## Slide 42

### **<u>Detection & Prevention for Defenders</u>**

######  **SgrmAgent.sys Version Build**

######  **Exploitation Detection**

###### **SgrmAgent.sys <= 10.0.20348.2849**

Versions prior to the one indicated above can be abused for process tampering. Newer versions return `STATUS_NOT_SUPPORTED`.

**SgrmBroker.exe Privileged Handles** SgrmBroker.exe handle opening is very limited in general.

###### **Indicator of Compromise (IOCs)**

###### **Indicator of Compromise (IOCs)**

   - Privileged handles may indicate active exploitation.

- Downgrade attacks targeting newer versions.

- BYOVD cases on modern OS builds.

42

## Slide 43

### **<u>Why this matters?</u>**



###### **SGRM is Deprecated**

SGRM is deprecated and absent from the latest Windows builds.



###### **Current POC on 22H2**

Abused SGRM on Windows 11 22H2.



###### **Component Porting**

Bring SgrmAgent.sys, WerFaultSecure.exe, and Faultrep.dll to **Windows 11 25H2** machines.



###### **Next Gen. BYOVD**

Next Generation of BYOVD attacks - **entirely based on first-party abusable components** .

43

## Slide 44

# Thank You

Sentinelone.com

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
S SentinelOne
Thank You
Sentinelone.com
```

## Slide 45

### **<u>Contact</u>**

- ●Angelo Frasca Caccia

   - ○Email: <u>angelo.frascacaccia@sentinelone.com</u> | <u>frascacaccia.96@gmail.com</u>

   - ○GitHub: <u>https://github.com/lem0nSec</u>

   - ○LinkedIn: <u>https://www.linkedin.com/in/angelo-frasca-caccia</u> ○X: <u>https://x.com/lem0nSec_</u>

45
