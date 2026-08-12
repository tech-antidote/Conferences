---
title: "Your Mitigations are My Opportunities"
speakers: ["Yarden Shafir"]
conference: "OffensiveCon"
conference_full: "OffensiveCon 2023"
edition: ""
year: 2023
source_pdf: "Offensivecon 2023 slides/Yarden Shafir_Your Mitigations are My Opportunities.pdf"
pages: 31
sha256: "d8d140d3dded6c044dfe02953ed89b382e70a5cf890ccbe4923d55204ca7a1c8"
text_chars: 13852
ocr_pages: 6
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:23:58Z"
---
# Your Mitigations are My Opportunities

**Speakers:** Yarden Shafir  
**Conference:** OffensiveCon 2023  
**Source:** `Offensivecon 2023 slides/Yarden Shafir_Your Mitigations are My Opportunities.pdf` (31 pages)

## Slide 1

Your Mitigations are My Opportunities

Yarden Shafir

## Slide 2

# About Me

- Sr. Security Engineer at Trail of Bits

- Previously Sr. Software Engineer at CrowdStrike and SentinelOne

- Instructor of Windows Internals classes

- Circus artist

- Former pastry chef

- Author of articles and tools at windows-internals.com

   - CET internals, extension host hooking, I/O ring exploitation, kernel exploit mitigations, heap backed pool internals

- @yarden_shafir

## Slide 3

# State of Windows Exploitation

- New features and mitigations kill entire bug classes or exploitation techniques

   - CET, CastGuard, KASAN…

- But…

   - Some require new hardware

   - Or require recompilation of software

   - Many are disabled by default

- Code Integrity Policies limit unsigned software

- ◦ Win32k rewrite in rust could remove the biggest source of kernel vulnerabilities

## Slide 4

# Introducing CET

- CET creates a shadow stack that stores return addresses

   - Attacker can’t modify the shadow stack without an additional vulnerability

- On every “ret” instruction, the return address is compared with the top address in the shadow stack

   - Mismatch will generate INT21: Control Protection Fault

   - ▫ Windows implements CET support for both user-mode and kernel-mode targets

## Slide 5

Stack Shadow Stack
Data Return Address 1
Data call Return Address 2
Return Address 1 Return Address 3
Data
Data
Data
Return Address 2
Data
Return Address 3 ret
Jump to return
address

## Slide 6

Stack Shadow Stack
Data Return Address 1
Data call Return Address 2
Return Address 1 Return Address 3
Data
Data
Data INT 21
Return Address 2
Data
Return Fake Address  3 ret
Exploit

## Slide 7

# CET – the Windows Implementation

- Kernel doesn’t immediately crash the process on Control Protection fault

   - Processes where CET is disabled / in audit mode are exempt

   - Return to modules compiled without CET is allowed

- Returning to any address in the shadow stack is allowed

- ◦ Additional logic to handle APCs, SetThreadContext, exceptions

- The kernel has CET too (KCET) implemented by VTL1 ▫ Also allows returning to any address in the shadow stack

## Slide 8

# **The Bypass**

- Returning to any address in the shadow stack is allowed

   - We can create a type confusion by returning to a valid address with a different register state

   - More stack frames == More type confusion choices

## Slide 9

# Normal Case

FuncB
FuncA
FuncC(); FuncC
s = FuncB();  s = new MyClass();
return 7;
s->Table[1](); s.Table[1] = Foo;
return s;
Foo
…

## Slide 10

# The Bypass

FuncC
_retaddr = FuncA + 8;
FuncB
b = new BadClass();
FuncA
FuncC(); b[0] = “AAAAAAAA”;
s = FuncB();  s = new MyClass(); b[1] = MaliciousFunc;
s->Table[1](); s.Table[1] = Foo;  b[2] = “BBBBBBBB”;
return s; return b;
MaliciousFunc
…

## Slide 11

Demo

## Slide 12

# Getting to the Kernel

- BYOVD! (Bring Your Own Vulnerable Driver)

- ◦ HVCI block list blocks some vulnerable drivers

   - But many drivers are still allowed to load

   - Loldrivers.io has over 600 vulnerable drivers – over 170 aren’t blocked by HVCI block list

   - Some blocked drivers have new unblocked builds too that are sometimes still vulnerable

■ New version of dbutil_2_3.sys is identical – but now requires admin rights to trigger vulns

## Slide 13

# The Problem With EDRs

- Most EDRs use drivers to monitor the system and block/ kill processes detected as malicious

- Many EDR user-mode processes are hard to kill because they run as a Protected Process Light (PPL)

   - Run with a special level protecting them from other processes ■ Yes, even admin processes

      - Well, sort of

   - Only other protected processes can read/write/suspend/ terminate

   - Requires an ELAM driver

## Slide 14

# How Can We Neutralize EDRs?

- HVCI has undocumented features that can be configured through the registry

- HKLM\System\CurrentControlSet\Control\CI

- ◦ HvciAuditMode (regular/full) allows receiving ETW messages for HVCI events without any blocking

- UMCIAuditMode is the same for user mode CI events

- ◦ HVCIDisallowedImages allows registering an array of driver names to be blocked by HVCI (requires reboot)

   - Only blocks by driver file name on disk

   - Great for blocking EDR drivers (except WdFilter.sys )

## Slide 15

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Operational Number of events:
Date and Time Source Event ID Task Category
2/11/2023 3:52:51 PM Codelntegrity 3004 (1)
2/11/2023 3:52:51 PM Codelntegrity 3089 (1)
) Information 2/11/2023 3:52:51 PM Codelntegrity 3089 (1)
2/11/2023 3:52:51 PM Codelntegrity 3004 (1)
1) Warning 2/11/2023 3:50:27 PM Codelntegrity 3073 (1)
(DI Infrnematinn 914119072 2-CN.9E DNA Cadalntancit: 2naa
eee!
Event 3073, Codelntegrity
General Details
Code Integrity determined that the module \Device\HarddiskVolume3\Windows\System 32\drivers\CrowdStrike\C SAgent.sys is
not compatible with strict mode hypervisor enforcement due to it having an executable section that is also writable.
Log Name: Microsoft-Windows-Codelntegrity/Operational
Source: Codelntegrity Logged: 2/11/2023 3:50:27 PM
Event ID: 3073 Task Category: (1)
Level: Warning Keywords:
User: SYSTEM Computer:
OpCode: (8060928)
More Information: Event Log Online Help
```

## Slide 16

# How Can We Disable a PPL?

- Common method is to terminate, suspend or close the handles of a PPL through a driver

   - KProcessHacker.sys, ProcExp.sys

- Defender ATP installs a “KseSec” shim to hook APIs in drivers known to be used for PPL suspension/termination

   - Hooks ZwTerminateProcess, PsSuspendProcess, NtClose, etc

   - Also hooks drivers/functions that allow mapping physical memory

   - Will block requests or log them to Microsoft-Windows-Sec ■ Depends on configuration received from user mode agent

## Slide 17

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
File Tools
Info Help
Name Value KDRIVER: * “
NAME: *
ha “OD: -s WILDCARD_NAME: *
> KDRIVER: usbser_lowerfitix64.sys ciccnma control
v NDOR.:
> KORIVER: usbser_lowerfitx64.sys EXE_ID: 27fc8c0f-8726-484b-b60f-<2663546e9 tb
> KDRIVER: usbser_lowerfitx64j.sys MATCHING _FILE: *
N Sa
> KDRIVER: wsr_rd.sys vie
ORIGINAL _FILENAME: LenovoDiagnosticsDriver.sys
> KDRIVER: * KSHIM_REF: SecKse
» | KORIVER: © FDC JD: #1405007-1c35-4e80-0626-47390 143eBbe
> KDRIVER: * FLAGS: 0
> KDRIVER: * MODULE: mssecfit
> KDRIVER: *
>» KDRIVER: *
> KDRIVER: *
KDRIVER: *
> KDEVICE: BTHENUM:BTHENUM\{0000 1124-0000-
: Camera:30. 18305.6. 12414;0 IDSSFFES
3110.540.0.0;0 1D64E716SC9C
3110.540.0.0;0 1D64E716SC9C
3110.540.0.0;0 1064E716SC9C
: Camera:
: Camera:
: Camera:
arde\OneDrive\drvmain_ksesec.sdb | File version ollapse nodes
```

## Slide 18

# MsSecFlt.sys and MsSecCore.sys

- MsSecFlt.sys – Microsoft Security Events Component file system filter driver

   - Responsible for logging events to the Microsoft-Windows-Sec ETW channel

   - Provides security-related events to security tools

      - Process must be an AM PPL or above to subscribe

- MsSecCore.sys – Microsoft Security Core Boot Driver

   - Recently added driver that works as an extension of MsSecFlt.sys

## Slide 19

Shimmed
Driver
SecBindHost(..)
ZwTerminateProcess
Function Table
SecRegisterKernelShimProvider(
MsSecFlt.sys
MsSecCore.sys
SecKseShimInformation) Register shims
ntoskrnl
SecKseZwTerminateProcess SecKseZwTerminateProcess
Send shim configuration over
filter port
\MicrosoftSecFilterControlPort
MsSense.exe

## Slide 20

MsSecCore.sys

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
O
MsSecCore.sys
NTSTATUS __fastcall SecKseZwTerminateProcess(HANDLE ProcessHandle, NTSTATUS ExitStatus)
{
char allowCall; // si
NTSTATUS status; // ebx
__int64 (__fastcall *KernelShimProviderApiHookAddress) (HANDLE, _QWORD); // rax
__int64 kernelShimProvider; // [rsp+4@h] [rbp+18h] MAPDST BYREF
kernelShimProvider = @i64;
allowCall = 1;
status = SecReferenceRegisteredShimProviderAndAcquireRundownProtection(&kernelShimProvider) ;
if ( status >= @ && SecIsHookSupportedByKernelShimProvider(kernelShimProvider, @) )
{
allowCall = 9;
KernelShimProviderApiHookAddress = SecGetKernelShimProviderApiHookAddress(kernelShimProvider, @);
status = KernelShimProviderApiHookAddress(ProcessHandle, ExitStatus) ;
}
SecDereferenceRegisteredShimProviderAndReleaseRundownProtection(kernelShimProvider) ;
if ( allowCall )
{
}
return status;
return (pZwTerminateProcessForwardingAddress) (ProcessHandle, ExitStatus) ;
```

## Slide 21

MsSecFlt.sys

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
NTSTATUS __fastcall SecKseZwTerminateProcess(void *ProcessHandle, NTSTATUS ExitStatus)
{
// [COLLAPSED LOCAL DECLARATIONS. PRESS KEYPAD CTRL-"+" TO EXPAND]
status = 9;
process = 0164;
allowCall = 1;
_InterlockedAdd64(&qword_1C09014530, 1ui64);
if ( BYTE4(SecKsePolicyConfig) )
®)
MsSecFit.sys
SecKseAuditKernelApi(moduleCtx, L"ZWTERMINATEPROCESS", moduleCtx->ConfigBitmask & 1);
{
if ( (BYTE8(xmmword_1C@0148E8) & 1) != @ )// Policy enabled?
{
callerAddress = SecKseCaptureCallerAddress() ;
moduleCtx = SecKseLookupModuleContextByAddress(callerAddress) ;
if ( moduleCtx )
{
auditConfig = &moduleCtx->AuditBitmask;
{
status = ObReferenceObjectByHandle(ProcessHandle, 1u, PsProcessType, @, &process, 0i64);
{
if ( PsIsProtectedProcess(process) )
{
{
status = STATUS_ACCESS DENIED;
allowCall = 9;
}
}
t
}
}
}
}
if ( process )
ObfDereferenceObject (process) ;
if ( allowCall )
return ZwlerminateProcess(ProcessHandle, ExitStatus) ;
return status;
```

## Slide 22

# Time for Plan B

- MsMpEng.exe is a PPL – hard to suspend/terminate

   - WdFilter.sys can terminate the process but only MsMpEng.exe can send it commands

- WdFilter.sys has a “Panic Mode”

   - Enabled when MsMpEng.exe times out on multiple file scans

   - ▫ Opens a “back door” that allows any process to sent certain commands to the driver

   - Sending a FSCTL with code 0x902EB will enter MpFsCtlDispatcher: a private IOCTL interface

      - Allows setting internal flags, resetting cache and terminating MsMpEng.exe

## Slide 23

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
NTSTATUS __fastcall MpPreFsControl(
PFLT_CALLBACK_DATA CallbackData,
PCFLT_RELATED_OBJECTS F1tObjects,
PFLT_CONTEXT *CompletionContext)
// [COLLAPSED LOCAL DECLARATIONS. PRESS KEYPAD CTRL-"+" TO EXPAND]
Context = @i64;
*v31 = 0164;
v33 = 0164;
if ( !FltObjects->FileObject )
{
if ( DeviceObject != &DeviceObject && (HIDWORD(DeviceObject->Timer) & 1) !=@ )
WPP_SF_(DeviceObject->AttachedDevice, 10164, &unk_1C@012F1@) ;
return 1;
}
*CompletionContext = 0164;
Iopb = CallbackData->Iopb;
MinorFunction = Iopb->MinorFunction;
if ( MinorFunction && MinorFunction != IRP_MN_KERNEL_CALL )// user request / kernel request are both valid
return 1;
FsControlCode = Iopb->Parameters.FileSystemControl.Common.FsControlCode;
if ( FsControlCode <= @x9@2EB )
{
if ( FsControlCode == @x9@2EB )
{
if ( PsGetCurrentProcessId() != MpData->EngineProcessId
&& (MpData->InternalFlags & @x800@0000) == @
&& !MpData->PanicMode )
{
return 13
}
CallbackData->IoStatus.Status = MpFsCtlDispatcher(CallbackData, FltObjects) ;
}
else
c
```

## Slide 24

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
BOOLEAN __fastcall MpFsCtlDispatcher(PFLT_CALLBACK_DATA CallbackData, PCFLT_RELATED_OBJECTS FltObjects)
{
unsigned int *InputBuffer; // rcx
int result; // eax MAPDST
unsigned int input; // [rsp+30h] [rbp-18h]
ProbeForRead(CallbackData->Iopb->Parameters.FileSystemControl.Neither.InputBuffer, 4ui64, 4u);
InputBuffer = CallbackData->Iopb->Parameters.FileSystemControl.Neither. InputBuffer ;
input = *InputBuffer;
switch ( *InputBuffer )
{
case 2u:
return MpFsCtlQueryNormalizedName(CallbackData, F1tObjects) ;
case 6u:
return MpFsCtlResetFileInCache(InputBuffer, F1ltObjects) ;
case 7u:
return MpFsCtlSetFileStateFlags(CallbackData, FltObjects);
}
if ( (MpData->InternalFlags & @x80000000) == @ && !MpData->PanicMode )
return STATUS_SEVERITY_WARNING;
if ( input !=9 )
if
Fo oc
return STATUS _SEVERITY_WARNING;
t
result = MpTerminateEngineProcess() ;
if ( WPP_GLOBAL_Control != &WPP_GLOBAL_Control && (*(WPP_GLOBAL_Control + 11) & 2) !=@ )
WPP_SF_qd(
*(WPP_GLOBAL_Control + 3),
19164,
&WPP_415afb42e9ed3bea82bd2F46ee3c28b4_Traceguids,
MpData->EngineProcess,
result);
return result;
```

## Slide 25

# Windows Defender Backdoor FSCTL

- Timeout is determined by MpData->LocalTimeout ▫ Default is 4 minutes for local files and 6 for network files

      - After 4 timeouts WdFilter.sys will go into panic mode ■ Also set in MpData together with the number of times it entered panic mode

         - FSCTL 0x902EB with code 9 will terminate MsMpEng.exe

   - `f = win32file.CreateFile("c:\\temp\\test.txt", win32file.GENERIC_READ, win32file.FILE_SHARE_READ, None, win32file.OPEN_EXISTING, 0)`

   - `win32file.DeviceIoControl(f, 0x902eb, b'\x09\x00\x00\x00', None, None)`

## Slide 26

Demo

## Slide 27

# Hiding in the Kernel

- Drivers are visible to anyone who is looking

   - And user<->kernel communication mechanisms are too

   - Many kernel structures are protected or monitored so they can’t be hooked or tampered with anymore

- But we can live off the land in the kernel

   - MsSecCore.sys shim functions call the registered functions in MsSecFlt.sys – this interface isn’t protected

- Build private comms mechanism by hooking callback routines and invoking hooked APIs from the UM process to send messages to the driver

## Slide 28

ntoskrnl
Rootkit.sys
Call shim
PsSuspendProcess
function
Call
evaluation
Shimmed
routine MsSecCore.sys
Driver
Request
process
suspension
User Mode
Process

## Slide 29

# Summary

- Bypass CET by returning to a different address from the shadow stack

   - Works against KCET too

- Reach the kernel through a vulnerable driver

   - Even if HVCI block list is enabled

- Neutralize EDRs with HVCI features or built-in backdoors

   - Or vulnerable drivers

- Live off the land in the kernel by hooking and abusing existing internal mechanisms

## Slide 30

# References

- Protected Processes:

   - <u>http://publications.alexionescu.com/NoSuchCon/NoSuchCon%202014%20%20Unreal%20Mode%20-%20Breaking%20Protected%20Processes.pdf</u>

   - ▫ <u>https://googleprojectzero.blogspot.com/2018/10/injecting-code-intowindows-protected.html</u>

   - <u>https://drive.google.com/file/d/1Pj7hSvsj0qvegdIUvABa9KUEKOrLzu2p/vi ew</u> + <u>https://github.com/gabriellandau/PPLFault</u>

- Kernel Shim Engine:

   - <u>https://www.youtube.com/watch?v=qCa9icMqBNM</u>

## Slide 31

Questions?
