---
title: "Dark Corners How a Failed Patch Left VMware ESXi VM Escapes Open for Two Years"
speakers: ["Yuhao Jiang", "Xinlei Ying", "Ziming Zhang"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Yuhao Jiang&Xinlei Ying&Ziming Zhang_Dark Corners How a Failed Patch Left VMware ESXi VM Escapes Open for Two Years.pdf"
pages: 55
sha256: "dd7efa7b53a0fc96d8b663e972f2241bb71db11aad413f39f58081d7158a6b14"
text_chars: 17431
ocr_pages: 6
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:04:15Z"
---
# Dark Corners How a Failed Patch Left VMware ESXi VM Escapes Open for Two Years

**Speakers:** Yuhao Jiang, Xinlei Ying, Ziming Zhang  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Yuhao Jiang&Xinlei Ying&Ziming Zhang_Dark Corners How a Failed Patch Left VMware ESXi VM Escapes Open for Two Years.pdf` (55 pages)

## Slide 1

## Dark Corners: How a Failed Patch Left VMware ESXi VM Escapes Open for Two Years Yuhao Jiang, 0x140ce, Ezrak1e

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
AUGUST 6-7, 2025
MANDALAY BAY / LAS VEGAS
Dark Comers: How a Failed Patch
Left VMware ESXi VM Escapes
Open for Two Years
Yuhao Jiang, 0x140ce, Ezrak1e
#BHUSA @BlackHatEvents
```

## Slide 2

### Who are we?

- Security researchers at Ant Group Light-Year Security Lab

- Escaped from virtual machine many times

- Won the Pwnie Awards in 2023

#BHUSA @BlackHatEvents

## Slide 3

### Talk Roadmap

- Introduction

- Escape VM First

- Escape ESXi Sandbox

- Demo

#BHUSA @BlackHatEvents

## Slide 4

#### Introduction

#BHUSA @BlackHatEvents

## Slide 5

### The Wake-Up Call

- VMware announced a 0day which has occurred in the wild.

- We exploited VMware ESXi on Tianfu Cup 2023.

- Let’s share some interesting things behind that story.

#BHUSA @BlackHatEvents

## Slide 6

### ESXi Architecture Overview

- Pretty same as VMware Workstation

- But the host OS is replaced as VMkernel

- Has sandbox

#BHUSA @BlackHatEvents

## Slide 7

#### Escape VM First

#BHUSA @BlackHatEvents

## Slide 8

### Attack Surface

|||**LSI Logic**||
|---|---|---|---|
||**Hard Disk**|**PVSCSI**|**Pwn2Own 2025 Workstation(CVE-2025-41238)**|
|||**NVME**||
||**Network**|**E1000/E1000e**||
||**Adapter**|**VMXNET3**|**Pwn2Own 2025 ESXi(CVE-2025-41236)**|
||**USB**|**UHCI (USB 1)**|**Tianfu Cup 2021 Workstation (CVE-2021-22041),**
**Tianfu Cup 2023 Workstation (CVE-2024-22253, CVE-22255)**|
||
**Controller**|**EHCI(USB 2)**|**GeekPwn 2022 Fusion(CVE-2022-31705)**|
|||**XHCI (USB 3)**|**Tianfu Cup 2021 ESXi (CVE-2021-22040),**
**Tianfu Cup 2023 ESXi(CVE-2024-22252)**|
|**Virtual Device**||**HID(mouse)**||
||**USB Device**|**Bluetooth**
**…**|**Pwn2Own 2023 Workstation (CVE-2023-20869, CVE-2023-20870),**
**Pwn2Own 2024 Workstation(CVE-2024-22267, CVE-2024-22269)**|
||**GPU**|**SVGA 2D**||
|||**SVGA 3D**||
||**Sound Card**|**ES1371**||
||**TPM**|**vTPM**||
||**VMCI**|**VMCI**|**Occurred in the wild (CVE-2025-22224),**
**Pwn2Own 2025 ESXi(CVE-2025-41237)**|
|||**…**
**Backdoor**||
|**GuestRPC**||**HGFS**|**Pwn2Own 2024 Workstation (CVE-2024-22270),**
**Occurred in the wild(CVE-2025-22226)**|
|**VMM**||||

~~#BHUSA~~ @BlackHatEvents

## Slide 9

The “Ancient” Vulnerability CVE-2021-22040 (Found by Wei of Kunlun Lab on Tianfu Cup 2021).

### Diff the Patch

We diffed v16.2.1 with v16.2.0. Good, only 7 functions need to be analysis.

#BHUSA @BlackHatEvents

## Slide 10

### xHCI / USB3.x Controller

Stream Context 0
Control EP 0 Stream Context 1
slot 1 EP 1 OUT Stream Context 2
slot 2 EP 1 IN
…
EP 2 OUT
…
Stream Context 65534
EP 2 IN
Slot
Stream Context Array
…
Stream Context 0
EP 15 IN Stream Context 1
urb 1
Endpoint Stream Context 2
Control Pipe 0
TR
urb 2 Pipe 1 OUT …
Ring
Pipe 1 IN
Stream Context 65534
urb n
Pipe 2 OUT
Stream Context Array
Pipe 2 IN
…
Pipe 15 IN

Spec/VMware objects

VMware-specific objects

Pipe

#BHUSA @BlackHatEvents

## Slide 11

### The “Ancient” Vulnerability

The key changes were located at xHCI Command Ring handler functions. The changes were reordering the execution sequence of slot context rewriting and invoking _xhci_clear_stream_ctx_ .

Before patch

After patch

In the older version, we can modify slot context before executing _xhci_clear_stream_ctx_ . What can we do with it?

#BHUSA @BlackHatEvents

## Slide 12

The “Ancient” Vulnerability Let’s see into the _xhci_clear_stream_ctx_

If _xhci_fetch_pipe_ fails, _cancel_pipe_ won't be executed at all!

#BHUSA @BlackHatEvents

## Slide 13

### The “Ancient” Vulnerability What can we do in xhci_fetch_pipe function?

There's a check on the slot content, and if it fails, it directly returns 0. Then there won't be pipe on the endpoint!

delete StreamCtx cancel pipe free urbs free StreamCtx

#BHUSA @BlackHatEvents

## Slide 14

### The use after free

Now we can leave the pipe not freed after stream context has been freed. What can we do next?

Free urb 1

hcpriv
0x205c
urb 1
urb_link_num
urb_size
- urb1_size
hcpriv
XHCIStreamContext

urb 2

**…**

#BHUSA @BlackHatEvents

## Slide 15

Resurrecting the “Ancient” Some new code in xhci_fetch_pipe! There was A new way for fetching pipe in xhci_fetch_pipe function.

1. For Slot State: Disabled/Enabled/Default → Find vusbDev in Root Hub

2. For other Slot States → Index via Dev State field in xHCI State's vsubDev table

#BHUSA @BlackHatEvents

## Slide 16

### Resurrecting the “Ancient”

**Step 1:** Data transfer → finds pipe via second path Root Hub Port Number incorrect

**Step 2:** Configure Endpoint → changes Slot State Forces first path → no pipe found

**Step 3:** Disable Slot → triggers vulnerability xhci_clean_pipe skipped **URBs left dangling in pipe**

#BHUSA @BlackHatEvents

## Slide 17

#### Wait wait wait

#BHUSA @BlackHatEvents

## Slide 18

### It Never Really “Died”

Actually, we don't need new code to make the _xhci_fetch_pipe_ function fail. We found that the patch never succeeded.

_The xhci_clear_stream_ctx_ function only delete stream context of a specific endpoint (ep). But the content of the entire slot has already been modified by us!

Modify slot content → Clear non-essential endpoints → Issue disable slot command → UAF

#BHUSA @BlackHatEvents

## Slide 19

#### Exploit Time!

#BHUSA @BlackHatEvents

## Slide 20

The Exploitation Challenge Constrained UAF:

• Only affects at offset +0x205c

• Operation: Subtract a value

The Problems:

1. If we want to change a 64-bit pointer alignment. We can only modify high 4 bytes Meaningless for exploitation.

2. Massive offset distance. +0x205c = 8284 bytes. Need do better in heap fengshui.

#BHUSA @BlackHatEvents

## Slide 21

### Finding Our Saving Grace **HashMap**

- Each element: value + key

- Controllable heap allocation size:

When storage exceeds capacity → reallocates to 2x size

stream_ctx hashmap:

- value: address, 8-byte

- key: id, 4-byte

Place 64-bit pointer at offset +0xc, perfect!

#BHUSA @BlackHatEvents

## Slide 22

### The Arsenal of Primitives

###### **1. URB**

   - Controllable size, dynamic allocate and free

   - Has a data array and its length member, and some pointers.

- Modify the length member → out-of-bounds read.

- New finding: Use vmware-USBArbitrator in Linux version to get USB-related symbols.

**2. mob, Surface, and GMR**

Useful for heap spraying and heap grooming.

**…**

Yuhao Jiang & Xinlei Ying 2024

Abdul-Aziz Hariri 2018

#BHUSA @BlackHatEvents

## Slide 23

### The Exploitation Flow

1. Construct a UAF

2. Allocate a URB at the location of the original stream context

3. Trigger the use, causing urb->actualLen to integer underflow

StreamCtx
0x2870

4. Out-of-bounds read, obtain heap address that we placed afterwards

0x2050 actualLen 0x40a0
gmr
urb
StreamCtx
0x2870

#BHUSA @BlackHatEvents

## Slide 24

### The Exploitation Flow

1. Construct another UAF

2. Use hashmap to occupy

3. Trigger the use, causing the streamctx pointer to point to the URB located ahead

0x2050 actualLen 0x40a0
gmr
urb
StreamCtx StreamCtx

0x2870

4. We can prepare a fake streamctx in the URB in advance

5. Pass streamctx check and free fake streamctx

6. Achieve heap overlapping

0x2050 actualLen 0x40a0 StreamCtx pointer
fake StreamCtx
gmr hashmap
urb
StreamCtx StreamCtx

0x2870

#BHUSA @BlackHatEvents

## Slide 25

### Control Flow Hijacking

1. Before URB is freed, _vusbCompleteUrbAddBatch_ function checks whether it's an xHCI URB. If so, it calls xhci_stream_ctx_sub_one_urb through the function pointer in vusbDev.

2. Using our existing heap overlap capability, we can take over URB objects, modify their contents to craft fake vusbDev objects, and achieve arbitrary address calls.

3. But this is still not enough - we need the ability to execute shellcode.

#BHUSA @BlackHatEvents

## Slide 26

### Execute Shellcode

1. We can obtain ROP capability via stack migration.

2. Replace rsp with the value at rdx address.

3. Subsequently, use ROP to allocate executable memory, copy shellcode, and execute it.

At the point of arbitrary address calls, the r12 register contains

the same value as rdi - the URB address.

#BHUSA @BlackHatEvents

## Slide 27

### The Dark Secret Revealed

- CVE-2021-22040 was not correctly patched.

- Until we reported the vulnerability at the end of 2023.

- Nobody pointed out that CVE-2021-22040 and CVE-2024-22252 are same.

### Reasons

- VMware’s bounty program is significantly lower than the vulnerability's true value.

- Closed source.

- Less technical sharing in the community.

#BHUSA @BlackHatEvents

## Slide 28

### How About This Time?

**CVE-2025-22224**

- Directly fetch values from guest memory to perform packet size validation

- **Step 1:** Use legitimate length → pass validation

**Step 2:** Immediately modify to oversized value

**Step 3:** Enter VMCIDatagramDispatch with malicious size

Before patch

#BHUSA @BlackHatEvents

After patch

## Slide 29

#### Escape ESXi Sandbox

#BHUSA @BlackHatEvents

## Slide 30

### ESXI Sandbox Overview

###### ⚫ ESXi uses security domains to limit process access to files, networks, etc.

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
[root@localhost:~] secpolicytools -l
2111
2113
authdBinObj 2114
certObj 2115
cim0bj 2105
erxclidbj 2110
default 1
dhclientObj 2127
esxcfgInitObj 2128
esxcfgadvcfg0bj 2129
esxtopObj 2126
etcd0bj 2108
infravisorSpherelet0Obj 2109
localclidbj 2131
opensslObj 2130
osfsd0bj 2121
pluginObj 2106
pmemGCObj 2119
secpolicyObj 2104
sfcbVmwPLuginObj 2107
shellobj 2118
sshdObj 2125
sslKeyObj 2112
supershellObj 2123
supportUtil0bj 2124
swapobjd0bj 2122
tardiskMountObj 2116
tpm2emu0bj 2117
unlabeled co}
vdsVsipIoctl 2134
vmkloadmod0bj 2133
vsanObserverObj 2120
vsishObj 2132
watchdogObj 2135
ESXI Sandbox Overview
e ESXi uses security domains to limit process access to files, networks, etc.
Valid domains
superDom
regularVMDom
1lprDom
actionScriptDom
clomdDom
cmmdsTimeMachineDom
cmmdsdDom
dcuiDom
dhclientDom
driverVMDom
entropydDom
entropydEsxcfgInitDom
epdDom
esxioCommdDom
genericDom
genericDomLocalAuth
jumpstartDom
keypersistDom
kmxaDom
lacpDom
loadsecpolicyDom
nfsgssdDom
nvmf -authdDom
osfsdDom
vaainasdDom
vmkdevmgrDom
vmkeventdDom
vmsyslogdDom
vobdDom
vsanObserverDom
vsanmgmtdDom
vsantracedDom
[root@localhost:~] ps -Z
WID cID WorldName
66184 66184 esxgdpd
66185 66185 sandboxd
66196 66184 esxgdpd-worker
66197 66184 esxgdpd-fair
66198 66184 esxgdpd-backend
66201 66185 worker
66202 66185 worker
SecurityDomain
43
82
43
43
43
82
82
```

## Slide 31

### Sandbox for Syscall

⚫ Looking at the rules, we can see restrictions on Syscalls

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
€Q
black hat
BRIEFINGS
Sandbox for Syscall
@ Looking at the rules, we can see restrictions on Syscalls
genericSys grant
vmxSys grant
ioctlSys grant
getpgidSys grant
getsidSys grant
vobSys grant
vsiReadSys grant
rpcSys grant
killSys grant
sysctlSys grant
syncSys grant
forkSys grant
forkExecSys grant
cloneSys grant
openSys grant
mprotectSys grant
iofilterSys grant
crossfdSys grant
pmemGenSys grant
keyCacheGenSys grant
vmfsGenSys grant
```

## Slide 32

### Sandbox for Syscall

- ⚫ In order to know which specific syscalls can be used,it is time to analyze the vmkernel

- ⚫ The vmkernel binary with symbols can be extracted from k.b00 in the system

#BHUSA @BlackHatEvents

## Slide 33

### Sandbox for Syscall

⚫ syscall number < 0x400                      Linux64_SyscallTable

- ⚫ 0x400 < syscall number < 0x4000      UW64VMKSyscall_HandlerTable

⚫ syscall number > 0x4000                 UW64VMKPrivateSyscall_HandlerTable

#BHUSA @BlackHatEvents

## Slide 34

### Sandbox for Syscall

⚫ Sandbox restrictions on syscall are mainly implemented in VmkAccessSyscallCheck

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
BRIEFINGS
Sandbox for Syscall
e Sandbox restrictions on syscall are mainly implemented in
VmkAccessSyscallCheck
EnforcementLevel = DomainObject->EnforcementLevel;
if ( !EnforcementLe el
| | _bittest64(&DomainObject->SyscallMask, (unsigned int)a2)
| Somaincbject-»PrivilegeLevel == 3
&& !_interlockedbittestandset64((volatile signed __int32 *)&DomainObject->SyscallMask, (unsigned int)a2) )
{
return @LL;
}
return @xBAD@117LL;
Log(
(unsigned int)"VmkAccess: %d: %s: %s:: dom:%s(%d), sysClass:%s(%d)\n",
81,
__readgsqword(@x1@u) + 3024,
(unsigned int)"access warning",
(_DWORD)DomainObject + 233,
DomainObject->dworde,
sysClassIdentifiers[(unsigned int)a2],
a2);
return @LL;
```

## Slide 35

### Sandbox for Syscall

Example :genericSys | vmxSys 1<<0 | 1<<1 = 3 Domain AccessMask=3

GetPrivateSyscallVersion belongs to genericSys access check succeed

#BHUSA @BlackHatEvents

## Slide 36

### Domain Transition

⚫ There are two ways to change domains

⚫ By adding SecurityDom to the parameters in the exec system call, the sandbox domain can be switched.

If you want to test your own programs in a sandbox domain, there is an easy way example ./test ++securitydom=51

#BHUSA @BlackHatEvents

## Slide 37

Domain Transition Only privileged domains and arbitraryTransitionDomains can use this method to transition domains.

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
BRIEFINGS
Domain Transition
Only privileged domains and arbitrary!ransitionDomains can use
this method to transition domains.
{ F nkAccessDomain eate+2D
esult = @LL; align 40h
if ( !al->IsarbitraryTransitionDomains ) aJumpstartdom db 'jumpstartDom',@
{ align 40h
result = al->EnforcementLevel; _ aSettingsddom db ‘settingsdDom',®
if ( (_DWORD)result == 1 || al->PrivilegeLevel ) align 40h
aSuperdom_@ db ‘superDom',@
return @xBAD@117LL; align 4eh
else if ( (_DWORD)result aGenericdom db ‘genericDom' ,@
{ - align 40h
Log( aGenericdomloca db ‘genericDomLocalAuth',@
(unsigned int)"VmkAccess: %d: Allow %s(%u) -> %s(%u) transition as %s(%u) is not enforcing\n", align 4@h
1335, aHostddom db 'hostdDom' ,@
align 40h
```

## Slide 38

### Domain Transition

- ⚫ Another way to transition to a sandbox domain is when the binary has the vmware.security xattr attribute.

- ⚫ The label of the domain obtained through vmware.security is used to find the domain object

#BHUSA @BlackHatEvents

## Slide 39

### Domain Transition

⚫ Is it possible to directly escape the sandbox by setting the xattr of a binary file?

- ⚫ First, the sandbox restricts the use of the Setxattr syscall （need vmkacSys）

- ⚫ Second, the sandbox defines what kind of domain each domain can transition to.

#BHUSA @BlackHatEvents

## Slide 40

### ESXI Sandbox Overview

⚫ Now we can fully understand the sandbox rules returned by secpolicytools

##### Socket

##### File

##### Syscall

##### Transition

#BHUSA @BlackHatEvents

## Slide 41

### Target Selection

- ⚫ Changed Block Tracking (CBT) is a VMkernel feature that keeps track of the storage blocks of virtual machines as they change over time. The VMkernel keeps track of block changes on virtual machines, which enhances the backup process for applications that have been developed to take advantage of VMware’s vStorage APIs.

#BHUSA @BlackHatEvents

## Slide 42

### Bug Discovery

###### ⚫ The CBT driver is a File Device Service driver, which is registered into the kernel through FDS_RegisterDriver

- 1.open("/dev/cbt/control")+ioctl -> CBT_Ioctl

- 2.UW64VMKSyscallUnpackFDSMakeDev->CBT_MakeDev

- ⚫ For example, create the /dev/cbt/pwn1

- ⚫ open("/dev/cbt/pwn1")+ioctl -> CBT_Ioctl

#BHUSA @BlackHatEvents

## Slide 43

### Bug Discovery

- ⚫ CBT_MakeDev creates a CbtDev object.

- ⚫ CbtDev stores the file handle entered by the user.

- ⚫ Use FSS_GetFileAttributesByFH to get the file size by file handle

- ⚫ Create a bitmap object based on the file size value

#BHUSA @BlackHatEvents

## Slide 44

### Bug Discovery

- ⚫ The vulnerability occurs in CBTUpdateBitmap, which causes an out-ofbounds write based on the offset and size entered by the user.

#BHUSA @BlackHatEvents

## Slide 45

### Check Bypass

- ⚫ FSS_IoctlByFH -> Fil3_FileBlockUnmap

- ⚫ Check  the offset and size cannot be larger than the file size.

- ⚫ check can be bypassed by writing more content to the file

#BHUSA @BlackHatEvents

## Slide 46

### Analysis

- ⚫ Now we can trigger an out-of-bounds write on a heap object

- ⚫ Which object can we overwrite?

- ⚫ It seems that we cannot find any exploitable objects from vmkernel

- ⚫ The cbt driver has only 15 functions and 24kb in size, which may not be as big as the problem in ctf

#BHUSA @BlackHatEvents

## Slide 47

### Analysis

- ⚫ Fortunately, we still have bitmap_object that can be used for exploitation

- ⚫ By modifying the BitmapSize field with an out-of-bounds write, we can get an out-ofbounds read to leak the kernel address.

#BHUSA @BlackHatEvents

## Slide 48

### GET AAW

By modifying bitmapptr, we can obtain arbitrary address write primitive

But out-of-bounds write primitive cannot modify a pointer address to another pointer address.

Example:

0x41(01000001) -> 0xff  (11111111)

0x41(01000001) -> 0x42(01000010)

#BHUSA @BlackHatEvents

## Slide 49

### Vmkernel Heap Exploitation

OOB write

... ...
OOB Bitmap OOB Bitmap
Victim  freed
Bitmap Bitmap
free
AAW victim freed  Placehold
Bitmap Bitmap

...
OOB Bitmap
Zero
Content

bitmap_ptr = 0 ！ Now we got AAR/W primitive

#BHUSA @BlackHatEvents

## Slide 50

### Expolit Overview

Step1:OverWrite Victim->BitmapSize to get  OOB READ primitive and leak kernel address

Step2:OverWrite Victim->ChunkSize and then release the chunk to control the BitmapPtr pointer to obtain AAW primitive

Step3:Use AAW primitive to modify SyscallMask_table and  call VmkAccessEnableDomain to close the sandbox

#BHUSA @BlackHatEvents

## Slide 51

# Summary

#BHUSA @BlackHatEvents

## Slide 52

### Summary

- How the ESXi sandbox works

- Found a bug in the CBT driver (CVE-2024-22254)

- Used OOB write + heap tricks to Escaped the sandbox and got full control

- • Small drivers can be dangerous

#BHUSA @BlackHatEvents

## Slide 53

#### Demo Video

#BHUSA @BlackHatEvents

## Slide 54

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat
BRIEFINGS
btw
AF —,
24968 UE)
BSmuen
8 tit
© me
*)
1246
PFS soos @
= 20:17
```

## Slide 55

#### Thank you

#### Questions?

#BHUSA @BlackHatEvents
