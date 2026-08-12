---
title: "Unveiling the Cracks in Virtualization, Mastering the Host System--VMware Workstation Escape"
speakers: ["Victor V"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2024"
edition: "ASIA"
year: 2024
source_pdf: "BlackHat ASIA 2024-Slides/Victor V-Unveiling the Cracks in Virtualization, Mastering the Host System--VMware Workstation Escape.pdf"
pages: 35
sha256: "8fb5d7b7cb0cf409353f43045613b1277b90e95707c1dacf6ec89a7a781484b1"
text_chars: 10128
ocr_pages: 16
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:52:40Z"
---
# Unveiling the Cracks in Virtualization, Mastering the Host System--VMware Workstation Escape

**Speakers:** Victor V  
**Conference:** Black Hat ASIA 2024  
**Source:** `BlackHat ASIA 2024-Slides/Victor V-Unveiling the Cracks in Virtualization, Mastering the Host System--VMware Workstation Escape.pdf` (35 pages)

## Slide 1

Unveiling the Cracks in Virtualization,

Mastering the Host System

VMware Workstation Escape

Speaker:

VictorV

**#BHASIA @BlackHatEvents**

## Slide 2

About Me : VictorV (@vv474172261)
VMware
Workstation
Escape
TianfuCup Zer0Con 2022
Top 3 of MSRC
2018/2021/2023 HITB 2020
2023 Q3/Q4
Leaderboard
Bugs in
Hyper-V Escape
SQLServer, RDP,
CVE-2019-0887
QEMU, DNS,
In 2021
DHCP, Samba,
ESXi…
#BHASIA @BlackHatEvents

## Slide 3

目录

###### CONTENTS

**Virtualization Basic Info**

**Historic Bugs In UHCI**

**Exploit for TianfuCup 2023 Summary**

**#BHASIA @BlackHatEvents**

## Slide 4

## **Virtualization Basic Info**

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisek hat
ASIA 2024
PART ONE
Virtualization Basic Info
Pes Fas Ee ek a SPARRRPIG EGA SS “i
®
e@ s
#BHASIA @BlackHatEvents
```

## Slide 5

### **Virtualization Basic Info VMware Worksation Architecture**

**#BHASIA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
§ Virtualization Basic Info
VMware Worksation Architecture
Printer
Backdoor VMCI
Storage(S
CD Rom
CST)
Display
#BHASIA @BlackHatEvents
```

## Slide 6

### **Virtualization Basic Info Virtual Process Address and Guest Physical Address**

Guest Virtual Address(GVA) Guest Physical Address(GPA) Host process Virtual Address(HVA)

In Guest, use GVA access its physical memory In Host vmx, use HVA of GPA access Guest memory

**#BHASIA @BlackHatEvents**

## Slide 7

### **Virtualization Basic Info Virtual Device and Guest Driver Interaction**

Guest System
IO Port IO Memory
Insb/Inb/outb/outsb Map to GVA, Directly read and write
IO Memory handler
IO port handler functions
functions
VMX process

**#BHASIA @BlackHatEvents**

## Slide 8

Virtualization Basic Info
VM Escape and RCE exploit
I/O
Read/Write
send data
Crack the
structure, and
leak data
Read/Write
receive info
send data Control RIP, run
ROP

**#BHASIA @BlackHatEvents**

## Slide 9

### **Virtualization Basic Info USB Controller**

USB 1.x
UHCI

CVE-2021-22041 CVE-2019-5519 CVE-2019-5518 CVE-2023-20870 …

USB 2.0
EHCI

CVE-2022-31705 …

USB 3.x USB 4.0
XHCI Future

CVE-2024-22252 CVE-2021-22040 CVE-2020-4004 CVE-2020-3968 CVE-2017-4904 …

**#BHASIA @BlackHatEvents**

## Slide 10

### **Virtualization Basic Info Virtual USB Controller Device Info**

**#BHASIA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
§ Virtualization Basic Info
Virtual USB Controller Device Info
{root@lLocalhost vv]# lspci -v -s 03:00.0
03:00.0 USB controller: VMware USB3 xHCI 1.0 Controller (prog-if 30 [XHCI])
Subsystem: VMware USB3 xHCI 1.0 Controller
Physical Slot: 160
-prefetchable) [size=128K]
abilities: anagement version 3
abilities: [6c] Express Endpoint, MSI 60
abilities: [a8] MSI: Enable- Count=1/1 Maskable+ 64bit+
abilities: [cO] MSI-X: Enable+ Count=31 Masked-
Kernel driver in use: xhci_hcd
[root@localhost vwv]# lspci -v -s 02:00.0
02:00.0 USB controller: VMware USB1.1 UHCI Controller (prog-if 00 [UHCI])
Subsystem: VMware Device 1976
Physical Slot: 32
L - Rdvanced Features
Kernel driver in use: uhci_hed
#BHASIA @BlackHatEvents
```

## Slide 11

### **Virtualization Basic Info UHCI Controller**

Ejected XHCI

**#BHASIA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
§ Virtualization Basic Info
UHCI Controller
bluetooth usb hub
a
i
€ Fundion 3} ™
/ ( Fundion *) (C Funclion
( Function) ( Fundion |)
#BHASIA @BlackHatEvents
```

## Slide 12

### **Virtualization Basic Info UHCI Controller**

0

**#BHASIA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
§ Virtualization Basic Info
UHCI Controller
31 2
| Frame List Pointer Indicates ‘Nil’ Next a
31 1
Link Pointer (Horiz) Link Pointer (Horiz) Link Pointer (Horiz) A 0 ; _|a
a
Link Pointer (Vert)
Link Pointer (Vert) [a Link Pointer (Vert) Link Pointer (Vert
/ Indicates "Nil Next Point
Indicates 'NULL' Queue Head Link Pointer
TD Link Pointer a
Link Pointer (Horiz)
Link Pointer (Vert)
Link Pointer
TD
Link Pointer
Link Pointer (Horzi=Queue Head Link Pointer TD
field in QH DWord 0
Link Pointer Vert)=Queve Element Link Pointer
field in QH DWord 1 Link Pointer
TD
#BHASIA @BlackHatEvents
```

## Slide 13

### **Virtualization Basic Info UHCI Controller**

u32 * TD = dmaAlloc(0x10, &TD_GPA); buffer = dmaAlloc(0x10, &buffer_GPA); frame_list[0] = TD_GPA | 1; TD[0] = 1;// end TD[1] = 1 << 23;// active TD[2] = (2 << 8) | (0 << 15) | (7 << 21) | 0x2d; //dev_id: 2, ep_id: 0, length: 8(7+1), type: setup(0x2d) TD[3] = buffer_GPA; buffer[0] =XXX;

**#BHASIA @BlackHatEvents**

## Slide 14

## **Historic Bugs In UHCI**

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisek hat
ASIA 2024
PART TWO
Historic Bugs In UHCI
009 O04 HM £ Me cPee ec. « <a
®
e@ ®
#BHASIA @BlackHatEvents
```

## Slide 15

### **CVE-2019-5519 TOCTOU**

**#BHASIA @BlackHatEvents**

Found by Amat Cama and Richard Zhu

## Slide 16

### **CVE-2021-22041 TOCTOU**

If frame_start = 0x3ff, i=0x400, frame_index = (0x400+0x3ff)&0x3ff = 0x3ff; ret = 1 frame[(0+0x3ff)&0x3ff] == frame[(0x400+0x3ff)&0x3ff] transfer_tag will match

**#BHASIA @BlackHatEvents**

Found by me, used in TianfuCup 2021

## Slide 17

### **CVE-2021-22041 TOCTOU**

1. Access frame[0x3ff]

2. Change frame[0x3ff] in SVGA thread 3. Access frame[(0x400+0x3ff)&0x3ff] again Get a new GPA

**#BHASIA @BlackHatEvents**

Found by me, used in TianfuCup 2021

## Slide 18

### **CVE-2023-20870 Uninitialize Leak**

##### struct urb{

- +0h reference;

- +4h buffer size;

- +8h count size;

+Ch size can read to vm; default 0

+18h endpoint;

- +78h buffer start;

- +80h cur_buff;

char buffer[xxx]; size is determined by input size }

**#BHASIA @BlackHatEvents**

Found by Thach Nguyen Hoang of STAR Labs, Wei and me also found it.

## Slide 19

### **CVE-2023-20870 Uninitialize Leak**

Fix:

Set urb->Ch = 8 in Bluetooth handler

**#BHASIA @BlackHatEvents**

Found by Thach Nguyen Hoang of STAR Labs, Wei and me also found it.

## Slide 20

### **CVE-2024-22255 Uninitialize Leak**

##### struct urb{

- +0h reference;

- +4h buffer size;

- +8h count size;

- +Ch size can read to vm; default 0

+18h endpoint;

- +78h buffer start; +80h cur_buff; char buffer[xxx]

}

U8(buffer, 0) = 0x21; U8(buffer, 1) = 9;// CASE U16(buffer, 6) = buffer size  - 8;

**#BHASIA @BlackHatEvents**

Found by Wei and me

## Slide 21

### **CVE-2024-22253 UAF**

**#BHASIA @BlackHatEvents**

Found by me, used at TianfuCup 2023

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
— CVE-2024-22253 UAF
uhci_ nan
idle_TDs(){
as = uhci_main->ep@_link.next;
whi
le(next != &uhci_main->ep@_link){
ep = next-18;
next = ep->link_uhci_main.next;
if(uhci_handle_in_urb(ep))
break
uhci_handle_type@ td({ep)
if(uhc i_handle_in_urb{ep))
(
d
oants(dev){
cep d
unlink ep->link_uhci_main;
dev->eps[i] = @;
free(ep);
}
}
dev->ep[@] = new_ep();
Found by me, used at TianfuCup 2023
VMware Workstation Windows 10 Guest System
bluetooth
usb hub
mouse
#BHASIA @BlackHatEvents
```

## Slide 22

PART THREE

## **Exploit for TianfuCup 2023**

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisek hat
ASIA 2024
PART THREE
Exploit for TianfuCup 2023 |
#BHASIA @BlackHatEvents
```

## Slide 23

### **Old Exploit primitives-Straight outta VMware**

**#BHASIA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
= Old Exploit primitives-Straight outta VMware
backend heap
backend heap
backend heap
backend heap
HVA of GPA
bug heap
backend
backend heap
backend heap
backend heap
160h LFH sesment
#BHASIA @BlackHatEvents
```

## Slide 24

### **Old Exploit primitives-Straight outta VMware**

Move to mksSandbox.exe

**#BHASIA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
= Old Exploit primitives-Straight outta VMware
backend heap back backend heap
| backend heap backend heap backend heap
D mkpaandbox.¢
bug heap backend backend heap
HAVA of GPA backend heap
160h LFH sesment
#BHASIA @BlackHatEvents
```

## Slide 25

### **Old Exploit primitives-Breakout Script of the Westworld**

Move to mksSandbox.exe

**#BHASIA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
— Old Exploit primitives-Breakout Script of the Westworld
surtace
HVA of GPA 01000 heap bug heap
80h LFH segment
#BHASIA @BlackHatEvents
```

## Slide 26

### **Old Exploit primitives-Breakout Script of the Westworld**

Move to mksSandbox.exe
Move into vector
can’t be heap

**#BHASIA @BlackHatEvents**

## Slide 27

### **Exploit primitives-UHCI Endpoint**

**#BHASIA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
— Exploit primitives-UHCI Endpoint
urb_link = (a2 + 64);
urb = *urb_link - 4@;
#BHASIA @BlackHatEvents
```

## Slide 28

### **Exploit primitives-Leak address by Urb bug**

struct urb{

- +70h vmx related process address

- +78h buffer start;

- +80h cur_buff;

char buffer[xxx]; size is determined by input size

- }

Get a urb heap address Get VMX related address

**#BHASIA @BlackHatEvents**

## Slide 29

### **Exploit primitives-R/W Everywhere by Endpoint primitive and urb**

**#BHASIA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
— Exploit primitives-R/W Everywhere by Endpoint primitive and urb
UHCI SVGA
thread
reset virtual
allocate and
mouse ep
Old ep release heap,
fake ep
~~
fak
fake ep fake ep new ope ms
(freeing)
fake ep fake ep fake ep
fake ep
(Ireeins) (freeing) (freeing)
sizeot(ep) LFH segment(Ox41 ff0)
#BHASIA @BlackHatEvents
```

## Slide 30

### **Exploit primitives-R/W Everywhere by Endpoint primitive and urb**

**#BHASIA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
— Exploit primitives-R/W Everywhere by Endpoint primitive and urb
. fake mouse urb = Vmx:
shader fake urb ; ———
dma_map buffer mob_table
i
change urb+80h
fake mouse urb VME:
dma_map buffer mob_ table
i
change it to svga global buffer
fake mob anywhere
;
HVA of GPA
BHASIA @BlackHatEvents
```

## Slide 31

### **Exploit Demo**

**#BHASIA @BlackHatEvents**

## Slide 32

PART FOUR
Summary

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat
ASIA 2024
PART FOUR
Summary
Wnt a Ned et
#BHASIA @BlackHatEvents
```

## Slide 33

### **Black Hat Sound Bytes**

Bug

#### Bug Research Tips

- TOCTOU, data of HVA  can complete

- UAF, Notice reset operation, similar bug: cve-2020-4004

Exp

#### Exploit Tips

- Urb to leak data

- Endpoint to write arbitrary anywhere

Defense

#### Defense Escape Attack

- Remove unnecessary virtual devices: Usb, Sound, CDrom

- Disable SVGA 3D

- Keep your software newest

**#BHASIA @BlackHatEvents**

## Slide 34

### **参考**

<u>https://census-labs.com/media/straightouttavmware-wp.pdf Zero Day Initiative — Taking Control of VMware Through the Universal Host Control Interface: Part 2 https://github.com/474172261/slides/blob/main/Breakout%20Script%20of%20the%20Westworldnew%5B1088%5D.pdf Universal Host Controller Interface (UHCI) Design Guide</u>

**#BHASIA @BlackHatEvents**

## Slide 35

# **Q&A**

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q&A
HANKS
. @
ae e@
bd ®
oe 8 meat: : He
#BHASIA @BlackHatEvents
```
