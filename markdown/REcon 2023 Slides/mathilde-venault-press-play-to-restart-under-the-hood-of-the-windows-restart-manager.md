---
title: "Press Play to Restart Under the Hood of the Windows Restart Manager"
speakers: ["Mathilde Venault"]
conference: "REcon"
conference_full: "REcon 2023"
edition: ""
year: 2023
source_pdf: "REcon 2023 Slides/Mathilde Venault_Press Play to Restart Under the Hood of the Windows Restart Manager.pdf"
pages: 55
sha256: "2948a101dd34a8b4b3433494d551282d24b2be06a89504ccbb1a8b32bb74aa13"
text_chars: 13152
ocr_pages: 18
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:25:13Z"
---
# Press Play to Restart Under the Hood of the Windows Restart Manager

**Speakers:** Mathilde Venault  
**Conference:** REcon 2023  
**Source:** `REcon 2023 Slides/Mathilde Venault_Press Play to Restart Under the Hood of the Windows Restart Manager.pdf` (55 pages)

## Slide 1

Press Play to Restart: Under the Hood of the Restart Manager Mathilde Venault - REcon 2023

©2023 CROWDSTRIKE, INC. ALL RIGHTS RESERVED.

## Slide 2

# About me

- Security Researcher at CrowdStrike

- Ex-volunteer firefighter

- Previously talked at Black Hat & c0c0n

- c0c0n CFP/CFW review committee member

## Slide 3

1 Introduction

2 Internals of the Restart Manager

- 3 Malicious Case 1: Ransomware Encryption

- 4 Malicious Case 2: Evasion & Anti-analysis

- 5 Processes Protection

- 6 Conclusion

## Slide 4

# Introduction

> Default way of opening a file:

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Introduction
> Default way of opening a file:
hFile = CreateFile(argv[1],
GENERIC_READ,
FILE _SHARE_READ,
NULL,
OPEN_EXISTING,
FILE FLAG OVERLAPPED,
NULL);
//
//
//
//
//
//
//
file to open
open for reading
share for reading
default security
existing file only
overlapped operation
no attr. template
X
```

## Slide 5

# Introduction

> What happens when a process opens a file without sharing access:

## Slide 6

# Introduction

> and if another process really needs to access the file….

## Slide 7

The Windows Restart Manager The playing field

## Slide 8

# The Origin

> Introduced in Windows Vista in the “RstrtMgr.dll” library

> Goal: avoid/reduce OS reboots during updates

> Allow applications to check that resources they need aren’t locked by other processes and request the termination of the blocking process, if needed

## Slide 9

# Architecture

- Applications communicate with the Restart Manager through sessions

- Each session contains one or more

- resources, that can be:

- Files

- Processes

- Services

## Slide 10

Global Operation

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
| \gROWDST! RIKE
Global Operation
Restart Manager —
|
To
\ ~ 1. Creates a
rs session
> ~ Application
crx)
</>
```

## Slide 11

Global Operation

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
| \gROWDST! RIKE
Global Operation
Restart Manager —
To
\ ~ 1. Creates a
| session
c 2. Registers
resource
re
> ~ Application
crx)
```

## Slide 12

Global Operation

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
| \gROWDST! RIKE
Global Operation
Restart Manager —
TO
\ ~ 1. Creates a
| session
> ~ Application
{/_ 2.Registersa _
\< resource </>
cu affected app: LockFile.exe 3. Gets the list of /
affected applications
```

## Slide 13

Exported Functions

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
| XGROWDSTRIKE
Exported Functions
RmStartSession RwiRegisterResources RwGetList
RmShutdown ( RwiRestart )
Ee)
Initiates a new
Restart Manager
session
Registers resources such as
filenames, service short names,
or RM_UNIQUE_PROCESS
structures
Gets the list of all applications
affected by registered resources
and their current status
Initiates the shutdown
of affected applications
and services
Restarts applications and services
that have been shut down by the
RmShutdown function and that have
been registered for restart using
RegisterApplicatioiRestart
```

## Slide 14

# RmStartSession()

> Assigns a session ID > Creates the internal database of the session PID of the register’s process > Initializes a registry hive for the session:

FILETIME of the register’s process creation

Current state of the session Hash of the “Owner” + unique UUID used in the SessionKey

## Slide 15

# RmRegisterResources()

> Registers the resources in its internal database

> Updates the registry hive of the session:

Registered Resource

Hash of the registered resource

## Slide 16

# RmGetList()

> Goal: find the affected applications for each different type of resource

> Relies on decorators: internal components designed to collect information

- 2 categories of information collected:

- System information

- - Application information

## Slide 17

# RmGetList() - Decorators

System Information

- SysProcInfo

- SvcInfo

Application Information

> Signature

> Restart

- WindowInfo

## Slide 18

RmGetList() - Decorators

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
RmGetList() - Decorators
Restart Manager
```

## Slide 19

RmGetList() - Decorators

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
| \gROWDST RIKE
RmGetList() - Decorators
Restart Manager
```

## Slide 20

RmGetList() - Decorators

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
| \gROWDST RIKE
RmGetList() - Decorators
Restart Manager
affected app: LockFile.exe
```

## Slide 21

# RmGetList() - For Files

> For registered files, retrieves the PIDs of processes using:

## Slide 22

# RmGetList() - For Services

- For registered services:

- Retrieves information about the service itself

- - If the service is currently running, retrieves the list of active dependant services

## Slide 23

# RmGetList() - Dependent Services

> Services can depend on one or more other services

> The other service(s) must be running before the dependent service can run

> Value defined in the registry hive of the service:

## Slide 24

RmGetList() - For Services

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
RmGet?List() - For Services
Please enter the short name of the service you want to check.
| PID associated: 728
| Application Type: RmService
| Application status: RmStatusRunning
| Application is restartable: true
| Application Type: RmCritical
| Application status: RmStatusRunning
| Application is restartable: false
```

## Slide 25

# RmGetList() - For Processes

- For registered processes:

- Retrieves information about the process itself

- - If associated with a service, retrieves the list of active dependant services

## Slide 26

RmGetList() - For Processes

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
RmGe?tList() - For Processes
--- Process: ----
| PID associated:728 |
| Application Type: RmCritical
| Application status: RmStatusRunning
| Application is restartable: false
--- Process: ----
| PID associated:728 |
| Application Type: RmCritical
| Application status: RmStatusRunning
| Application is restartable: false
--- Service: ----
| PID associated:"728
| Application Type: RmService
| Application status: RmStatusRunning
| Application is restartable: true
--- Process: ----
| PID associated:728 1
| Application Type: RmCritical
| Application status: RmStatusRunning
| Application is restartable: false
--- Service: ----
| PID associated:"728 |
| Application Type: RmService
| Application status: RmStatusRunning
| Application is restartable: true
--- Process:
| PID associatéa: “lel
| Application Type: RmCritical
| Application status: RmStatusRunning
| Application is restartable: false
```

## Slide 27

# RmShutdown()

> Scenario 1: the affected application is a GUI application

- 1st call to SendMessageTimeoutW() with WM_QUERYENDSESSION

- 2nd call to SendMessageTimeoutW() with WM_ENDSESSION

- If not, 3rd call to SendMessageTimeoutW() with WM_CLOSE

## Slide 28

# RmShutdown()

> Scenario 2: the affected application is a console application

- Sends a CTRL_C_EVENT notification

- By default, processed by the control handler that calls ExitProcess()

## Slide 29

# RmShutdown()

> Scenario 3: the affected application is associated with a service

- Stops the service using ControlService()

- Terminates the associated process  using TerminateProcess()

## Slide 30

# RmShutdown()

> Scenario 4: the affected application is explorer.exe

- Same as for classic applications - 1st call to SendMessageTimeoutW() with WM_QUERYENDSESSION

- Same as for classic applications - 2nd call to SendMessageTimeoutW() with WM_ENDSESSION

> The main difference with classic applications: no 3rd call to SendMessageTimeoutW() with WM_CLOSE

## Slide 31

# RmShutdown()

> What may happen when WM_CLOSE message is sent to explorer.exe:

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
| \GROWDSTRIKE
RmShutdown()
>What may happen when message is sent to
Shut Down Windows
gm Windows 10
What do you want the computer to do?
Shut down
Closes all apps and turns off the PC.
OK Cancel
```

## Slide 32

# Legitimate Use Case Example

- Typical use case: installers & updaters

- Benefits:

- Ensures to be able to complete the update

- Avoids a reboot

- Let’s find out who/how thanks to ninite :)

## Slide 33

Legitimate Use Case Example

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
| \GROWDSTRIKE
Legitimate Use Case Example
4 || All Modules exer
=.) [f] Restart Manager GQ C:\Users\User\Desktop\Ninite Evernote GIMP PeaZip ShareX Skype Installer.exe - PID: 16
5.) Gy Rstrtmgr.all a4 C:\Users\User\AppData\Local\Temp\5466cb2d-e35c-11ed-94a 3f09d\Ninite.exe - PID: 4
[El Rmadafitter 4B C:\Users\User\AppData\Local\T emp\S58COC~1\target.exe - PID: 6320 - (Terminated)
[I RmcancelCurrentTask #-9@J C:\Users\User\AppData\Local\Temp\S58COC~3\target.exe - PID: 3328 - (Terminated)
EE] RmEndsession =|] C:\Users\User\AppData\Local\ Temp \is-S6640.tmp\target.tmp - PID: 3076 - (Terminated)
El RmGetFiltertist :
[=] RmGetList
EE] RmoinSession ow
EE] RmRegisterResources Q, Return Value Duration
[=] RmRemoveFilter R 5 a ERROR.
a pnpesar 2 egisterResource 0 ERROR_SUCCESS 0,0006251
=] RmShutdown
ERROR_SUCCESS 502
=] RmStartSession -
ERRO S 0.0015493
ISS 088
<
Pre-Call Value
9 nFiles 14
& ¢ rgsFileNames Ox044ab1
# [0] C:\Program Files\Microsoft VS Code\Code.exe™
LPcwsTR 411] «04137730 “C:\Program Files\Microsoft VS Code\d3dcompiler_47.
LPcwsTR ¢ 12] D C:\Program Files\Microsoft VS Code\ffmpeg. dil
#14] 0 C:\Program Files\Microsoft VS Code\libGLESv2.dll
LPCWSTR 4 [5] x041377a0 “C:\Program Files\Microsoft VS Code\vk_swiftshader.dll”
a
a
a
LPCWSTR @ ¢ (3) 0x0. ‘C:\Program Files\Microsoft VS Code\libEGL.dlI”
a
a
a
LPCWSTR 4 [6] m 38 “C:\Program Files\Microsoft VS Code\vulkan-1.dll
```

## Slide 34

# Legitimate Use Case Example

VS Code
installer
Hooked
functions Function calls
performed by
the installer
Arguments of RmRegisterResources()
List of files registered
as resources

## Slide 35

# Malicious Use Cases

How can the Restart Manager be hijacked?

## Slide 36

Supporting Ransomware Encryption Cheat code Δ ✚ XO

## Slide 37

A real world example: Conti Ransomware

> Source code leaked in March 2022

> Goal: check if a potential file to encrypt is blocked by another process and attempts to terminate it if necessary

> Method: iterating over files to register each potential target as a resource in a Restart Manager session

## Slide 38

Step 1: Register the target file

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
|e
Step 1: Register the target file
EIBOOL KillFileOwner(__in LPCWSTR PathName)
if
' // Check if RstrtMgr.dll is loaded based on a global variable flag
Es) if (!api: :IsRestartManagerLoaded())/ { ... } |
BOOL Result = FALSE;
DWORD dwSession = 0x0;
DWORD ret = 0;
WCHAR szSessionKey[CCH_RM_SESSION_KEY + 1];
Rt1lSecureZeroMemory(szSessionkey, sizeof(szSessionKey) ) ;
// Initiates the Restart Manager session
a! , if (pRmstartSession(&dwSession, @x@, szSessionKey) == ERROR SUCCESS)
a
' ' // Register into the session the target file
oh ' if (pRmRegisterResources(dwSession, 1, &PathName, @, NULL, @, NULL) == ERROR SUCCESS)
' ' Cc =e aaa aaa aaa aaa aaa aaa aaa ~
DWORD dwReason = 0x0;
UINT nProcInfoNeeded = @;
UINT nProciInfo = 0;
PRM_PROCESS_INFO ProcessInfo = NULL;
RtlSecureZeroMemory(&ProcessInfo, sizeof(ProcessInfo) ) ;
YX
```

## Slide 39

Step 2: Retrieve the list of affected apps

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
[4]
Step 2: Retrieve the list of affected apps
(
, ret = (DWORD)pRmGetList(dwSession, &nProcInfoNeeded, &nProcInfo, ProcessInfo, &dwReason); |
AF (ret != ERRORSUCCESS []~!nProcinfoNeeded)[{ Ty | -
// Allocates the required structures to get information for each process & service
ProcessInfo = (PRM PROCESS INFO)memory: :Alloc(sizeof(RM_PROCESS INFO) * nProcInfoNeeded) ;
nProcinfo = nProcInfoNeeded;
// Retrieves the list of processes & services currently using the target file
YX
```

## Slide 40

Step 3: Terminating the affected apps

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Step 3: Terminating the affected apps
DWORD ProcessId = (DWORD)pGetProcessId(pGetCurrentProcess());
// For each process or service using the target file
for (INT i = @; i < nProcInfo; i++) {
// Ends the session if one of the process using the file is the current process
if (ProcessInfo[i].Process.dwProcessId == ProcessId) {
memory : : Free(ProcessInfo) ;
pRmEndSession(dwSession) ;
return FALSE;
}
process _killer::PPID Pid = NULL;
TAILQ_FOREACH(Pid, g WhitelistPids, Entries) {
// Ends the session if one of the process using the file is one the whitelist
if (ProcessInfo[i].Process.dwProcessId == Pid->dwProcessId) {
memory : :Free(ProcessInfo) ;
pRmEndSession(dwSession) ;
return FALSE;
// Shutdown processes & services using the target file I
Result = pRmShutdown(dwSession, RmForceShutdown, NULL) == ERROR_SUCCESS; I
X
```

## Slide 41

Anti-analysis and Evasion Purposes

Cheat code  OΔXΔ

## Slide 42

Identifying Running Processes

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
\gROWDST! RIKE
Identifying Running Processes
Running processes \
```

## Slide 43

Identifying Running Processes

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
\gROWDST! RIKE
Identifying Running Processes
Restart Manager _
Running processes \
```

## Slide 44

Identifying Running Processes

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
\gROWDST! RIKE
Identifying Running Processes
Running processes \
Restart Manager ———,
ProcessB.exe |
)
ProcessB.exe
affected app: Process A |
```

## Slide 45

What can be done with this?

## Slide 46

# Process Discovery

> MITRE: Process Discovery

> Gather information about running processes and services (reconnaissance purposes)

## Slide 47

# Sandbox/Debugger Evasion

> MITRE: Debugger Evasion, Virtualization/Sandbox Evasion

- Detect and avoid debuggers, sandboxes and virtualized environments

## Slide 48

# Anti-analysis

> MITRE: Impair Defenses: Disable or Modify Tools

- Detect & disable monitoring tools

## Slide 49

Time for a demo!

## Slide 50

# Protect Processes

Game over?

## Slide 51

# What Makes Applications Immune

- For applications associated with service: Protected Process & Protected Process Light

   - Associated with binaries complying with specific signature requirements

   - Defined by an attribute in the EPROCESS structure

   - Limits accesses granted to protected processes

## Slide 52

# What Makes Applications Immune

- For other applications: User Interface Privilege Isolation (UIPI)

   - Boundary between applications based on their integrity level

   - Prevents apps with a lower privilege from sending messages to more privileged apps

## Slide 53

Conclusion

## Slide 54

# Conclusion

- More information on the internals of this little known component of Windows

- New techniques for performing process discovery, evasion and impair defense

- Release of the tool on GitHub: https://github.com/MathildeVenault

## Slide 55

Thank you for your attention! Any questions?
