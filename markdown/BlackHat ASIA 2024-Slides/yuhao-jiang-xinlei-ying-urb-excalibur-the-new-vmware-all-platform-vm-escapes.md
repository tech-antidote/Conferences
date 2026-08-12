---
title: "URB Excalibur The New VMware All-Platform VM Escapes"
speakers: ["Yuhao Jiang", "Xinlei Ying"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2024"
edition: "ASIA"
year: 2024
source_pdf: "BlackHat ASIA 2024-Slides/Yuhao Jiang & Xinlei Ying-URB Excalibur The New VMware All-Platform VM Escapes.pdf"
pages: 41
sha256: "3db538a17761c558c48606784bd79f26aa434d58afd12c788ac0cd0249e58129"
text_chars: 10920
ocr_pages: 7
has_ocr: true
redacted_secrets: 0
ocr_confidence: 87.9
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:53:35Z"
---
# URB Excalibur The New VMware All-Platform VM Escapes

**Speakers:** Yuhao Jiang, Xinlei Ying  
**Conference:** Black Hat ASIA 2024  
**Source:** `BlackHat ASIA 2024-Slides/Yuhao Jiang & Xinlei Ying-URB Excalibur The New VMware All-Platform VM Escapes.pdf` (41 pages)


## Slide 1

**URB Excalibur: The New VMware All-Platform VM Escapes**

Yuhao Jiang (@danis_jiang) Xinlei Ying (@0x140ce)

#BHASIA @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
blackh
APRIL 18-19, 2024 _
BRIEFINGS
URB Excalibur: The New VMware
All-Platform VM Escapes
Yuhao Jiang (@danis_jiang)
Xinlei Ying (@0x140ce)
#BHASIA @BlackHatEvents
```

## Slide 2

## Who are we?

Security researchers at Ant Group Light-Year Security Lab Escaped from virtual machine many times Won the Pwnie Awards🦄 at 2023

Yuhao Jiang Xinlei Ying (@danis_jiang) (@0x140ce)

# BHASIA @BlackHatEvents

## Slide 3

## Talk Roadmap

**1. Introduction**

**2. A journey of finding vulnerabilities in VMware’s hypervisor**

**3. Exploit development of VMware VM escape**

# BHASIA @BlackHatEvents

## Slide 4

# Introduction

#BHASIA @BlackHatEvents

## Slide 5

## What is Virtual Machine escape and the danger of it

- Escape from the isolation sphere

- Take control over the whole hypervisor

- Network escape

**One of the most catastrophic threats to the Cloud**

# BHASIA @BlackHatEvents

## Slide 6

## VMware’s Architecture

# BHASIA @BlackHatEvents


> Recovered by OCR — confidence 84/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
VMware’s Architecture
Any
Mee Virtual Machine 3
>
2
Host OS 2
Disk \
‘ \
Driver xy
CPU [(iii) | a a
Host OS Context e VMM Context
Fig. 2. The VMware Hosted Architecture. VMware Workstation consists of the three shaded components.
```

## Slide 7

## VMware hypervisors’ attack surface

||**Hard Disk**|**LSI Logic**||
|---|---|---|---|
|||**NVME**||
||**Network**|**E1000/E1000e**||
||**Adapter**|**VMXNET3**||
||**USB**
|**UHCI**|**Tianfu Cup 2021 Workstation (CVE-2021-22041),**
**Tianfu Cup 2023 Workstation (CVE-2024-22253, CVE-**
**22255)**|
||**Controlle**
**r**|**EHCI**|**GeekPwn 2022 Fusion(CVE-2022-31705)**|
|**Virtual Device**||**XHCI**|**Tianfu Cup 2021 ESXi (CVE-2021-22040),**
**Tianfu Cup 2023 ESXi(CVE-2024-22252)**|
|||**HID(mouse)**||
||**USB**
**Device**|**Bluetooth**|**Pwn2Own 2023 Workstation (CVE-2023-20869, CVE-**
**2023-20870)**|
||**GPU**|**…**
**SVGA 2D**||
|||**SVGA 3D**||
||**Sound Card**|**ES1371**||
||**TPM**|**vTPM**||
|**GuestRPC**||**…**
**Backdoor**||
|**VMM**||||

# BHASIA @BlackHatEvents

## Slide 8

Vulnerability Discovery

A journey of finding vulnerabilities in VMware’s hypervisor

#BHASIA @BlackHatEvents

## Slide 9

## Start vulnerability discovery in VMware

First encounter with VMware, closed-source hypervisor

**1. Focusing on an interesting and potentially risky attack surface** ● Having studied QEMU EHCI vulnerabilities

   - Interested in VMware's EHCI implementation

**2. Reverse engineering**

   - Using string search as an entry point

   - Understanding EHCI specification and QEMU code while reverse engineering VMware

# BHASIA @BlackHatEvents

## Slide 10

## EHCI / USB 2.0 Controller

VMware’s virtual EHCI
controller
VMware’s virtual video device
(face time)

# BHASIA @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
EHCI / USB 2.0 Controller
Client Driver Software
Universal
System Bus Driver (USBD)
Software
Companion (UHCI or Enhanced Host
OHCI) Host Controller Controller Driver (EHCD)
Driver
Scope Of
EHCI
Companion (UHCI or
Enhanced Host
Hardware
USB controller
USB Device VMware’s virtual video device
Figure 1-1. Universal Serial Bus, Revision 2.0 System Block Diagram (face ti aa e)
```

## Slide 11

## EHCI / USB 2.0 Controller

# BHASIA @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
EHCI / USB 2.0 Controller
Start
or.
AND.
Advance
Queue
Active AND. !Halted
Active
Execute
Transaction
Active
Write Back
Follow QH
Horizontal
Pointer
Figure 4-14. Host Controller Queue Head Traversal State Machine
```

## Slide 12

## EHCI / USB 2.0 Controller

### **Endpoint/Pipe:**

- Control

- ● Bulk

- Interrupt

- Isochronous

**Token:**

- Setup

- In: Device -> Software

- Out: Software -> Device

# BHASIA @BlackHatEvents

## Slide 13

How the data flow
CVE-2020-14364
do_token_setup
QEMU
ehci_state_fetchqh ehci_state_fetchqtd usb_handle_packet do_token_in
do_token_out
Could there be
bugs here?
while (1) VUsb_NewUrb
YES!
setup
VMware
ehci_control_transfer in urb_submit
out

# BHASIA @BlackHatEvents

## Slide 14

## CVE-2022-31705

# BHASIA @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CVE-2022-31705
3. Heap out-of-bounds write vulnerability in EHCI controller (CVE-2022-31705)
Description
Mware ESX nd Fusior
e Critical severity range v
Known Attack Vectors
Resolution
VMware w 1d like t ank t gal
Notes
```

## Slide 15

## CVE-2022-31705

SETUP qTD
urb’s size =
0x98 + 8 + setup_len

# BHASIA @BlackHatEvents


> Recovered by OCR — confidence 85/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
VE 2022 3 1 705 1 Void __fastcall ehci_control_transfer(__int64 state, pipe *pipe, EHCIgh *qh)
5 = pipe->urb_link_first;
6 = &gh->next_qtd;
7 = 0164;
SETUP qTD
0x98 + 8 + setup_len 143 [6] + s;
= VUsb_NewUrb(
1 = ->purb_data_cursor;
->interrupt_pid =
160 =1;
161 ->num_packets = 1;
162 irb->datalen =
```

## Slide 16

## CVE-2022-31705

OUT qTD IN qTD
Where is the BUG?
Next qTD
# BHASIA @BlackHatEvents

# BHASIA @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CVE-2022-31705
OUT qTD
if ¢
Warning("EHCI: Unexpected status packet size
ABEL.
Next qTD
IN qTD
Where is the BUG?
```

## Slide 17

## CVE-2022-31705

OUT qTD IN qTD
Check if qTD-
>tbytes is valid
Where is the BUG?
Next qTD
# BHASIA @BlackHatEvents

# BHASIA @BlackHatEvents

## Slide 18

## CVE-2022-31705

OUT qTD
Check if qTD-
>tbytes is valid
Next qTD

IN qTD
NO CHECK!
Directly subtract
Where is the BUG?
tbytes from setup_len

# BHASIA @BlackHatEvents

## Slide 19

## CVE-2022-31705

- Missing tbytes check when handling IN qTD

- ● setup_len downward integer overflow

QH
Value of
setup_len

SETUP IN IN IN OUT
0x340 0x7FFF 0x7FFF 0x7FFF 0x340+0x100
0x340 -0x7CBF -0xFCBE …… 0x6004c339

- setup_len is much larger than the size of urb

- Use OUT qTD to obtain heap out-of-bounds write

# BHASIA @BlackHatEvents

## Slide 20

## What else did we find?   BUG 1: Out-of-bounds read vulnerability

● Pipe type confusion (Control ⇐⇒ ISOC) ● Handle urb incorrectly

Always be 1 in control pipe’s urb

# BHASIA @BlackHatEvents

## Slide 21

## What else did we find?

BUG 2: Information disclosure vulnerability

- In many virtual USB devices (USB Audio, USB Video, USB RNG…)

- ● No memset, writeback_len is set to the data size of urb.

# BHASIA @BlackHatEvents

## Slide 22

# Exploit Development

#BHASIA @BlackHatEvents

## Slide 23

## The problem

- **[Again]** Closed-source

- No public exploit code and rarely disclosed exploit flow

- Most of past exploit primitives have been patched

- Few code paths that can be controlled with in the guest OS.

# BHASIA @BlackHatEvents

## Slide 24

## Some patches for old primitives

- DnD/CP objects in **backdoor module** (2017)

   - a. VMware remove dynamic allocation and release of DnD/CP objects

- ResourceContainer in **SVGA backend module** (2018)

   - a. VMware first removed the function pointer table in the ResourceContainer in 15.5.7

b. VMware moves SVGA backend module into sandbox (mksSandbox) in 16

- GMR in **SVGA front-end module** (2021)

   - a. VMware adds a check at the head of GMR chunk (MKSMemMgrSafeMalloc)

-

# BHASIA @BlackHatEvents

## Slide 25

## URB: Powerful Excalibur

- USB Request Block

- Used by all virtual USB controllers

   - Dynamic allocate and free

   - ● Has:

      - A variable length data array

      - A member to control length to read

      - A data pointer

      - A pipe pointer

   -

# BHASIA @BlackHatEvents

## Slide 26

## Out-of-bounds write -> Out-of-bounds Read

1. Allocate URB1 and URB2, leaving space for EHCI Control URB

2. Allocate EHCI Control URB, then overwrites writeback_len of URB1

3. Read back URB1, we can read the buffer address and pipe address

# BHASIA @BlackHatEvents

## Slide 27

## Arbitrary Address Read

1. Allocate EHCI Control URB again

2. This time overwrite purb_data_cursor to any location

3. Read back URB1

Everywhere

# BHASIA @BlackHatEvents

## Slide 28

## Arbitrary Address Write

- Write from a pointer in frame to another pointer in frame

- ● frame is a member in pipe

- ● We can fake the pipe in urb using out-of-bonds write

# BHASIA @BlackHatEvents

## Slide 29

## Control the RIP

1. A dynamically allocated object that holds function pointers

2. We can trigger a call to the function pointer

pipe

# BHASIA @BlackHatEvents

## Slide 30

## Control the RIP: Path 1

- The pipe when calling cancel_pipe in ehci_check_and_writeback comes from the pointer of urb

- We can use out-of-bounds write to forge the urb->pipe to implement arbitrary address calls.

# BHASIA @BlackHatEvents

## Slide 31

## Control the RIP

**Path 2**

● Fake a new pipe directly in vusbDev by arbitrary address write

EHCI
port reset

destory_all_pipe

cancel_pipe

**Use Path 2 when we can’t reserve EHCI urb, although it needs more actions**

# BHASIA @BlackHatEvents

## Slide 32

## What’s more? We need heap grooming

Heap spraying and grooming primitive: **SVGA_3D_CMD_SET_SHADER** Allocate and free in large quantities, the heap size is sizeInBytes+8 **svga_3d_cmd_define_gb_shader(shid, SVGA3D_SHADERTYPE_MIN, sizeInBytes); svga_3d_cmd_bind_gb_shader(shid, mobid, 0); svga_3d_cmd_set_shader(cid, SVGA3D_SHADERTYPE_MIN, shid);**

**svga_3d_cmd_destroy_gb_shader(shid);**

<u>https://census-labs.com/media/straightouttavmware-wp.pdf</u>

# BHASIA @BlackHatEvents

## Slide 33

## Try on the VMware Fusion!

- 1 out-of-bounds read, 3 arbitrary address reads, and 2 arbitrary address writes

   1. Heap grooming

   2. Leak pipe address and heap address

   3. Leak the program base address (pipe->dev)

   4. Leak ehci state address (in .data)

   5. Leak vusbdev address (in ehci state)

   6. Write the upper 4 bytes of the fake pipe to vusbdev

   7. Write the lower 4 bytes of the fake pipe to vusbdev

   8. Trigger cancel pipe

   9. Escape

# BHASIA @BlackHatEvents

## Slide 34

## Big problem. Magazine

- MacOS’s libmalloc uses magazines to manage heap blocks

- ● Each CPU core will have a unique corresponding magazine

# BHASIA @BlackHatEvents

## Slide 35

## Big problem. Magazine. How we deal with it

- Repeat the basic heap layout, and try to have at lease one layout on each magazine

- Try a large number of times for every step (place objects, do oob read…)

- How to ensure that all magazines are occupied?

   - Add sleep between each allocation

   - Increase cpu’s occupancy and try to increase cpu core switching

- Remove sleep, speed up exploit

- ● Use a huge number of spray rounds (0x1000)

**<u>Success rate > 80%</u>**

# BHASIA @BlackHatEvents

## Slide 36

## Demo

# BHASIA @BlackHatEvents

## Slide 37

## On VMware Workstation

- In the default configuration, there will be no device on the EHCI

   - Plug in a usb device to connect to ehci

- To avoid the randomization of LFH:

   - Use chunks larger than 0x4000

   - Select a size that has not been used by LFH when we can’t allocate larger than 0x4000

1. Leak heap address

2. Leak process base address 3. Leak the address of createProcessW (KERNEL32.dll)

4. Call WinExec

# BHASIA @BlackHatEvents

## Slide 38

## Demo

# BHASIA @BlackHatEvents

## Slide 39

## On ESXi

- Same as Workstation, no default device on EHCI

- ● Similar to CentOS 7, use very old glibc-2.17 (2.28 after ESXi 8.0.2)

- ● Basically the same as on Fusion (No need to face magazines)

- ● Use GMR instead of Shader

# BHASIA @BlackHatEvents

## Slide 40

## Takeaways

- Where bugs have arisen with similar software, there may be new bugs

- When looking for exploit primitives, try to look for objects related to the vulnerability

- Virtual devices, especially USB-related devices, are now a popular attack surface

# BHASIA @BlackHatEvents

## Slide 41

## Questions?

# BHASIA @BlackHatEvents
