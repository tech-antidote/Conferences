---
title: "Infecting the Boot to Own the Kernel Bootkits and Rootkits Development Presentation"
speakers: ["Alejandro Vazquez Vazquez Maria San Jose"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33/Alejandro Vazquez Vazquez Maria San Jose - Infecting the Boot to Own the Kernel Bootkits and Rootkits Development Presentation.pdf"
pages: 37
sha256: "dd08518291fb4ad182afff43cae08622d7923ae25921f9c566a5c91144836590"
text_chars: 16732
ocr_pages: 0
has_ocr: false
redacted_secrets: 0
ocr_confidence: null
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2"
converted_at: "2026-08-12T06:51:16Z"
---
# Infecting the Boot to Own the Kernel Bootkits and Rootkits Development Presentation

**Speakers:** Alejandro Vazquez Vazquez Maria San Jose  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33/Alejandro Vazquez Vazquez Maria San Jose - Infecting the Boot to Own the Kernel Bootkits and Rootkits Development Presentation.pdf` (37 pages)


## Slide 1

# INFECTING THE BOOT TO OWN THE KERNEL: BOOTKITS AND ROOTKITS DEVELOPMENT

Demistifying UEFI Bootkits and Kernel-Mode Rootkits Development

<u>[in/vazquez-vazquez-alejandro] [in/mariasanjose]</u> DEF CON 33, Las Vegas 2025

## Slide 2

# WHOAREWE

**GEEK** ( **G** entleman **E** xploring u **E** FI and OS **K** ernel)

**GEEK** ( **G** irl **E** xploring **E** xploits and **K** ernel threats)

Octopus lovers

## Slide 3

### Sensitive Content

This presentation contains age-restricted materials including malware and explicit hooking techniques. By entering, you affirm that you are at least 18 years of age and you consent to viewing “hacker” stuff. **No Let me In I prefer to stay with the This is real malware**

**No I prefer to stay with the humans in the Villages**

## Slide 4

## BOOTKITS & ROOTKITS DEMYSTIFIED

- Bootkit: Malicious program designed to load as early as possible in the boot process, in order to control all stages of the operating system start up, modifying system code and drivers before security components are loaded. ~ Kaspersky

- Rootkit: Sophisticated piece of malware that can add new code to the operating system or delete and edit operating system kernel code.

   - ~ Crowdstrike

## Slide 5

## BOOTKITS & ROOTKITS DEMYSTIFIED

- Bootkit: Malicious program designed to load as early as possible in the boot process, in order to control all stages of the operating system start up, modifying system code and drivers before security components are loaded. ~ Kaspersky

**UEFI Application C/C++ - boot.efi**

- Rootkit: Sophisticated piece of malware that can add new code to the operating system or delete and edit operating system code.

   - ~ Crowdstrike

**Kernel-Mode Driver C/C++ - driver.sys**

## Slide 6

## BOOTKITS & ROOTKITS DEMYSTIFIED

- Bootkit: Malicious program designed to load as early as possible in the boot process, in order to control all stages of the operating system start up, modifying system code and drivers before security components are loaded. ~ Kaspersky

**UEFI Application C/C++ - boot.efi** • Rootkit: Sophisticated piece of malware that can add new code to the operating system or delete and edit operating system code. ~ Crowdstrike **Kernel-Mode Driver C/C++ - driver.sys**

## Slide 7

## SECURITY MECHANISMS TO BYPASS

- * [ _Anti-Bootkit Installation_ ] Prevent installation of malicious UEFI applications - Prevent installation of malicious Kernel-mode drivers * [ _Anti-Rootkit Installation_ ]

## Slide 8

## SECURITY MECHANISMS TO BYPASS

- * [ _Anti-Bootkit Installation_ ] Prevent installation of malicious UEFI applications • SecureBoot Only software trusted by the Original Manufacturer Firmware checks the signature of UEFI firmware drivers, EFI applications and SO

_CVE-2025-33043_ (SMRAM write) _CVE-2024-8105_ (PKfail) _CVE-2024-7344_ (Custom PE loader) _CVE-2023-40238_ (LogoFAIL Image parsing) _CVE-2022-21894_ (Baton Drop)

## Slide 9

## SECURITY MECHANISMS TO BYPASS

- Prevent installation of malicious Kernel-mode drivers * [ _Anti-Rootkit Installation_ ] • Driver Signature Enforcement (DSE) Windows won't run drivers not certified by Microsoft

Bring Your Own Vulnerable Driver (BYOVD) _RTCore64.sys Viragt64.sys dbutil_2_3. sys loldrivers_

## Slide 10

# CHECKPOINT

- ➢ Bootkit = Malicious UEFI Application

- ➢ Rootkit = Malicious Kernel Mode Driver

➢ Protection Mechanisms SecureBoot DSE PatchGuard Vulnerable driver blocklist

…..

## Slide 11

Power ON
Read Instructions
POST
Windows NT OS Kernel
%SystemRoot%\system32\
ntoskrnl.exe
UEFI Firmware
Windows OS Loader
%SystemRoot%\system32\
winload.efi
Boot Information
Windows Boot Manager
\EFI\Microsoft\Boot\
UNDERSTANDING
EFI System Partition bootmgfw.efi
THE BOOT PROCESS
Boot order
Boot0001 = /EFI/Microsoft/boot/bootmgfw.efi
Boot0002 = /EFI/Ubuntu/shimx64.efi
Boot000x = /EFI/Vendor/bootx64.efi

## Slide 12

Power ON
Read Instructions
POST
Windows NT OS Kernel
%SystemRoot%\system32\
ntoskrnl.exe
UEFI Firmware
Windows OS Loader
%SystemRoot%\system32\
winload.efi
Boot Information
Windows Boot Manager
\EFI\Microsoft\Boot\ Bootkit
MANIPULATING
EFI System Partition bootmgfw.efi UEFI Application
bootmgfw.efi THE BOOT PROCESS
Boot order
Boot0001 = /EFI/Microsoft/boot/bootmgfw.efi
Boot0002 = /EFI/Ubuntu/shimx64.efi
Boot000x = /EFI/Vendor/bootx64.efi

## Slide 13

`// Find function pattern Status = FindPattern(TargetFunctionSignature, 0xCC, sizeof(TargetFunctionSignature), (UINT8*)ImageBase...` **Power ON** `// Find function start OriginalFunctionPointer = (VOID*)FindStartAddress(ImageBase, NtHeaders, Found);` **Read Instructions** `// Hook bootmgfw.efi!Function, winload.efi!Function` **POST** `VOID* HookAddress = (VOID*)&MyHookHandlerFunction;` **Windows NT OS Kernel** %SystemRoot%\system32\ `// Backup original function bytes` **ntoskrnl.exe** `CopyMem(BackupOriginalBytes, OriginalFunctionPointer, sizeof(HookTemplate)); // Place hook trampoline at the start of the original function CopyMem` **UEFI Firmware** `(OriginalFunctionPointer, HookTemplate, sizeof(HookTemplate));` **Windows OS Loader** `// Write hook handler address into trampoline template` %SystemRoot%\system32\ `CopyMem((UINT8*) OriginalFunctionPointer + HookTemplateAddressOffset, (UINTN*)&HookAddress, sizeof(UINTN));` **winload.efi Boot Information Windows Boot Manager** \EFI\Microsoft\Boot\ **Bootkit EFI System Partition bootmgfw.efi UEFI Application bootmgfw.efi** THE BOOT PROCESS Boot order Boot0001 = /EFI/Microsoft/boot/bootmgfw.efi Boot0002 = /EFI/Ubuntu/shimx64.efi Boot000x = /EFI/Vendor/bootx64.efi

MANIPULATING THE BOOT PROCESS

## Slide 14

**Power ON ntoskrnl.exe** ➔ **user Read Instructions** • CmGetSystemDriverList(); • SeCodeIntegrityQueryInformation(); **POST Windows NT OS Kernel** %SystemRoot%\system32\ **winload.efi** ➔ **ntoskrnl.exentoskrnl.exe** • OslArchTransferToKernel(); • OslFwpKernelSetupPhase1(); **UEFI Firmware** • BlImgAllocateImageBuffer(); **Windows OS Loader** %SystemRoot%\system32\ **bootmgfw.efi** ➔ **winload.efiwinload.efi Boot Information** • ImgArchStartBootApplication(); • Archpx64TransferTo64BitApplicationAsm(); **boot** ➔ **bootmgfw.efiWindows Boot Manager** \EFI\Microsoft\Boot\ **Bootkit** MANIPULATING **EFI System Partition bootmgfw.efi UEFI Application** • ExitBootServices(); **bootmgfw.efi** THE BOOT PROCESS • gBS->LoadImage(); Boot order Boot0001 = /EFI/Microsoft/boot/bootmgfw.efi Boot0002 = /EFI/Ubuntu/shimx64.efi Boot000x = /EFI/Vendor/bootx64.efi

## Slide 15

Power ON
Read Instructions
POST
Windows NT OS Kernel
%SystemRoot%\system32\
ntoskrnl.exe
UEFI Firmware
Windows OS Loader
%SystemRoot%\system32\
winload.efi
Boot Information
Windows Boot Manager
\EFI\Microsoft\Boot\ Bootkit
MANIPULATING
EFI System Partition bootmgfw.efi UEFI Application
bootmgfw.efi THE BOOT PROCESS
Boot order
Boot0001 = /EFI/Microsoft/boot/bootmgfw.efi
Boot0002 = /EFI/Ubuntu/shimx64.efi
Boot000x = /EFI/Vendor/bootx64.efi

## Slide 16

Power ON
Read Instructions
POST
Windows NT OS Kernel
%SystemRoot%\system32\
ntoskrnl.exe
UEFI Firmware
Windows OS Loader
%SystemRoot%\system32\
winload.efi
Boot Information
Windows Boot Manager
Rootkit
\EFI\Microsoft\Boot\ Bootkit
Kernel-Mode Driver
EFI System Partition bootmgfw.efi UEFI Application
kmdf.sys
bootmgfw.efi
Boot order
Boot0001 = /EFI/Microsoft/boot/bootmgfw.efi
Boot0002 = /EFI/Ubuntu/shimx64.efi
Boot000x = /EFI/Vendor/bootx64.efi

## Slide 17

## Slide 18

Windows NT OS Kernel
%SystemRoot%\system32\
ntoskrnl.exe
Windows OS Loader
%SystemRoot%\system32\
winload.efi
Windows Boot Manager
Rootkit
\EFI\Microsoft\Boot\ Bootkit
Kernel-Mode Driver
bootmgfw.efi UEFI Application
kmdf.sys
bootmgfw.efi

## Slide 19

Windows NT OS Kernel
%SystemRoot%\system32\
ntoskrnl.exe
Windows OS Loader
%SystemRoot%\system32\
winload.efi
Windows Boot Manager
Rootkit
\EFI\Microsoft\Boot\ Bootkit
Kernel-Mode Driver
bootmgfw.efi UEFI Application
kmdf.sys
bootmgfw.efi

## Slide 20

Windows NT OS Kernel
%SystemRoot%\system32\
ntoskrnl.exe
Windows OS Loader
%SystemRoot%\system32\
winload.efi
Windows Boot Manager
Rootkit
\EFI\Microsoft\Boot\ Bootkit
Kernel-Mode Driver
bootmgfw.efi UEFI Application
kmdf.sys
bootmgfw.efi

## Slide 21

Windows NT OS Kernel
%SystemRoot%\system32\
ntoskrnl.exe
Windows OS Loader
%SystemRoot%\system32\
winload.efi
Windows Boot Manager
Rootkit
\EFI\Microsoft\Boot\ Bootkit
Kernel-Mode Driver
bootmgfw.efi UEFI Application
kmdf.sys
bootmgfw.efi
DXE Runtime Driver
runtime.efi

## Slide 22

CmGetSystemDriverList();
SeCodeIntegrityQueryInformation();
OslArchTransferToKernel();
OslFwpKernelSetupPhase1();
BlImgAllocateImageBuffer();
Windows NT OS Kernel
%SystemRoot%\system32\
ntoskrnl.exe
ImgArchStartBootApplication();
Archpx64TransferTo64BitApplicationAsm(); Windows OS Loader
%SystemRoot%\system32\
winload.efi
Windows Boot Manager
Rootkit
\EFI\Microsoft\Boot\ Bootkit
Kernel-Mode Driver
bootmgfw.efi UEFI Application
kmdf.sys
bootmgfw.efi
DXE Runtime Driver
runtime.efi
ExitBootServices();
gBS->LoadImage();

## Slide 23

## Slide 24

CmGetSystemDriverList(); SeCodeIntegrityQueryInformation();

OslArchTransferToKernel();
OslFwpKernelSetupPhase1();
BlImgAllocateImageBuffer();
Windows NT OS Kernel
%SystemRoot%\system32\
ntoskrnl.exe
ImgArchStartBootApplication();
Archpx64TransferTo64BitApplicationAsm(); Windows OS Loader
%SystemRoot%\system32\
winload.efi
Windows Boot Manager
Rootkit
\EFI\Microsoft\Boot\ Bootkit
Kernel-Mode Driver
bootmgfw.efi UEFI Application
kmdf.sys
bootmgfw.efi
DXE Runtime Driver
runtime.efi
ExitBootServices();
gBS->LoadImage();

## Slide 25

CmGetSystemDriverList(); SeCodeIntegrityQueryInformation();

OslArchTransferToKernel();
OslFwpKernelSetupPhase1();
BlImgAllocateImageBuffer();
Windows NT OS Kernel
%SystemRoot%\system32\
ntoskrnl.exe
ImgArchStartBootApplication();
Archpx64TransferTo64BitApplicationAsm(); Windows OS Loader
%SystemRoot%\system32\
winload.efi
Windows Boot Manager
Rootkit
\EFI\Microsoft\Boot\ Bootkit
Kernel-Mode Driver
bootmgfw.efi UEFI Application
kmdf.sys
bootmgfw.efi
Filter Driver
DXE Runtime Driver
wfp_wsk_minifilter.sys
runtime.efi
Console App
Ioctl_irp.exe
ExitBootServices();
gBS->LoadImage();

## Slide 26

1. User Mode - Kernel Mode Communication ntddk.h

Toolkit Communication

2. Direct Kernel Object Manipulation ntddk.h

Hide Processes DKOM

3. Keyboard and Mouse Filter ntddk.h

Keylogger Keyboard Filter

4. Windows Filtering Platform fwpmk.h, fwpsk.h, fwpmu.h

Network Control WFP

5. WinSock Kernel wsk.h

Network Requests WSK

6. File System Minifilter Driver fltKernel.h

Hide Folders Minifilter

## Slide 27

## Slide 28

# **I**

User Mode

# COMMUNICATION

Kernel Mode

#### kernel_mode_driver.sys

\```
// -----------------------
#define IOCTL_COMM_0 CTL_CODE(FILE_DEVICE_UNKNOWN, 0x800, METHOD_BUFFERED, FILE_ANY_ACCESS)
\```

\```
// -----------------------
\```

#### console_application.exe

\```
// -----------------------
#define IOCTL_COMM_0 CTL_CODE(FILE_DEVICE_UNKNOWN, 0x800, METHOD_BUFFERED, FILE_ANY_ACCESS)
// -----------------------
hDevice = CreateFile(L"\\\\.\\MyKernelDriver", GENERIC_READ | GENERIC_WRITE, ...
// -----------------------
BOOL success = DeviceIoControl(
hDevice,
*IOCTL_COMM_0,
*inBuffer, sizeof(inBuffer),
*outBuffer, sizeof(outBuffer),
&bytesReturned, NULL
);
\```

#### Handle IRP

#### IRP

\```
typedefstruct_IRP {}
\```

\```
IRP_MJ_DEVICE_CONTROL
\```

Simbolic Link Device Object `"\\DosDevices\\MyKernelDriver" "\\Device\\MyKernelDriver"`

#### Device Object

\```
status = IoCreateDevice(...);
status = IoCreateSymbolicLink(...);
\```

\```
// -----------------------
pDriverObject->MajorFunction[...] = ...;
pDriverObject->MajorFunction[IRP_MJ_DEVICE_CONTROL] = DriverHandleIOCTLs;
\```

\```
// -----------------------
NTSTATUS
DriverHandleIOCTLs(
_In_  PDEVICE_OBJECT  pDeviceObject,
_In_  PIRP pIrp
)
{
PIO_STACK_LOCATION stack = IoGetCurrentIrpStackLocation(pIrp);
ULONG controlCode = stack->Parameters.DeviceIoControl.IoControlCode;
\```

\```
switch(controlCode)
{
caseIOCTL_COMM_0:
...
break;
\```

\```
caseIOCTL_COMM_1:
...
break;
\```

\```
pIrp->IoStatus.Status = STATUS_SUCCESS;
IoCompleteRequest(pIrp, IO_NO_INCREMENT);
returnSTATUS_SUCCESS;
}
\```

## Slide 29

# **II**

# HIDE PROCCESSES

“Windows maintains a doubly linked list of active processes in (LIST_ENTRY) EPROCESS->ActiveProcessLinks. Unlink a process from the chain, and it disappears from user-mode enumeration.”

struct  EPROCESS struct  EPROCESS struct  EPROCESS struct  EPROCESS struct  EPROCESS
{ { { { {
… … … … …
LIST_ENTRY 0x1d8 LIST_ENTRY 0x1d8 LIST_ENTRY 0x1d8 LIST_ENTRY 0x1d8 LIST_ENTRY 0x1d8
{ { { { {
FLINK FLINK FLINK FLINK FLINK
BLINK BLINK BLINK BLINK BLINK
} } } } }
… … … … …
} } } } }

## Slide 30

# **III**

# KEYLOGGER

“Keystroke interception in kernel mode: The Windows keyboard driver stack routes all keystrokes through a device object called \Device\KeyboardClass0. By attaching a driver to this device and registering a CompletionRoutine (a callback executed after an IRP has been processed by lower drivers, allowing access to data before it reaches the next stage), we can capture raw keystroke data before it propagates to user-mode applications like text editors or browsers.”

Keyboard Port Driver Keyboard Class Driver (i8042prt.sys) (kbdclass.sys) Keyboard Filter Drivers \Device\KeyboardClass0 (Optional 1..N) Keylogger Driver \Device\My Keylogger Attached to intercept IRP_MJ_READ requests and set a CompletionRoutine to capture keystroke data.

User Mode

Physical Keyboard

## Slide 31

# **IV**

# NETWORK CONTROL

“Windows Filtering Platform (WFP) allows real-time inspection and control of network connections. By attaching filters (static rules applied at specific layers of the network stack to identify traffic based on attributes like IPs or ports) and callouts (custom drivers that execute dynamic logic on flagged traffic), it’s possible to classify traffic based on metadata such as the remote IP address and the associated process. Traffic that matches specific rules can be blocked, logged, or modified, enabling comprehensive network security policies.”

Conditions
Filter A
Layer 1
Callout F Fields Conditions
Filter B
Network  Filter  Layer 2 Conditions
Callout G
Stack Engine Fields Filter C
Conditions
Callout H Filter D
Layer 3
Fields
Conditions
Filter E

## Slide 32

# **V**

# NETWORK REQUESTS

“WinSock Kernel (WSK) allows kernel-mode programs to perform complex network operations, such as establishing connections, binding sockets, and transferring data. With support for asynchronous communication using IRPs, WSK enables efficient and controlled interaction with network protocols, ensuring low-latency communication and making it a robust solution for implementing kernel-level networking features.”

I/O Manager
WSK
Registration
Library WinSock Kernel
AFD.SYS
(WSK)
Network
Module
TCP/IPV4 TCP/IPV6
\Device\TCP \Device\TCP6 3 Party
Registrar
\Device\UDP \Device\UDP6 \Device\Proto
(NMR) \Device\RAW \Device\RAW6

## Slide 33

# **VI**

# HIDE FOLDERS

“MiniFilters attach to the file system stack to filter I/O operations. Using a PreOperation callback (triggered before the file system processes a request), access to files or directories can be explicitly denied by returning STATUS_ACCESS_DENIED or FLT_PREOP_COMPLETE. In the PostOperation callback (triggered after the request finishes), the DirectoryBuffer - which temporarily holds the directory listing - can be modified to remove specific entries, effectively making files and folders invisible to user-mode applications like File Explorer.”

I/O Manager Filter Manager Minifilter A
Forwards request to file  Intercept requests and calls  FSFilter Activity Monitor
system registered minifilters in altitude  Altitude 360000
order
Minifilter B
FSFilter Anti-Virus
Altitude 320000
Storage Driver Stack
File System Driver
for target volume Processes and forwards  Minifilter C
Prepares request for  FSFilter Encryption
modifies request
hardware Altitude 140000

## Slide 34

CmGetSystemDriverList(); SeCodeIntegrityQueryInformation();

OslArchTransferToKernel();
OslFwpKernelSetupPhase1();
BlImgAllocateImageBuffer();
Windows NT OS Kernel
%SystemRoot%\system32\
ntoskrnl.exe
ImgArchStartBootApplication();
Archpx64TransferTo64BitApplicationAsm(); Windows OS Loader
%SystemRoot%\system32\
winload.efi
Windows Boot Manager
Rootkit
\EFI\Microsoft\Boot\ Bootkit
Kernel-Mode Driver
bootmgfw.efi UEFI Application
kmdf.sys
bootmgfw.efi
Filter Driver
DXE Runtime Driver
wfp_wsk_minifilter.sys
runtime.efi
Console App
Ioctl_irp.exe
ExitBootServices();
gBS->LoadImage();

## Slide 35

## Slide 36

FROM UEFI TO KERNEL

## Slide 37

- ❤️ In loving memory of Shira 01-01-2013 / 04-07-2025

# THANK YOU 🐾

#### UEFI Bootkit

   - **<u>github.com/TheMalwareGuardian/Abyss</u>**

- Kernel-Mode Rootkit

   - **<u>github.com/TheMalwareGuardian/Benthic</u>**

- Every resource you need to develop Bootkits/Rootkits

   - **<u>github.com/TheMalwareGuardian/Awesome-Bootkits-Rootkits-Development</u>**

- Automate Bootkits/Rootkits Development Environment

   - **<u>github.com/TheMalwareGuardian/Bootkits-Rootkits-Development-Environment</u>**

- Contact:

   - **<u>https://www.linkedin.com/in/vazquez-vazquez-alejandro</u>**

   - **<u>https://www.linkedin.com/in/mariasanjose</u>**
