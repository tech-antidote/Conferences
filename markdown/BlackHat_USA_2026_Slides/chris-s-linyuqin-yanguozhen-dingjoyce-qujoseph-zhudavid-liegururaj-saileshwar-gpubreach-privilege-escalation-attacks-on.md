---
title: "GPUBreach Privilege Escalation Attacks on GPUs Using Rowhammer"
speakers: ["Chris S. Lin", "Yuqin Yan", "Guozhen Ding", "Joyce Qu", "Joseph Zhu", "David Lie", "Gururaj Saileshwar"]
conference: "Black Hat"
conference_full: "Black Hat USA 2026"
edition: "USA"
year: 2026
source_pdf: "BlackHat_USA_2026_Slides/Chris S. Lin&Yuqin Yan&Guozhen Ding&Joyce Qu&Joseph Zhu&David Lie&Gururaj Saileshwar_GPUBreach Privilege Escalation Attacks on GPUs Using Rowhammer.pdf"
pages: 98
sha256: "f7596a16c96080b296d82ce16d1631e8b60ef96674c9fd3baf35c0966f8ccc47"
text_chars: 26934
ocr_pages: 3
has_ocr: true
redacted_secrets: 0
ocr_confidence: 88.8
ocr_unreliable_blocks: 0
vision_verified_blocks: 2
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:30:16Z"
---
# GPUBreach Privilege Escalation Attacks on GPUs Using Rowhammer

**Speakers:** Chris S. Lin, Yuqin Yan, Guozhen Ding, Joyce Qu, Joseph Zhu, David Lie, Gururaj Saileshwar  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/Chris S. Lin&Yuqin Yan&Guozhen Ding&Joyce Qu&Joseph Zhu&David Lie&Gururaj Saileshwar_GPUBreach Privilege Escalation Attacks on GPUs Using Rowhammer.pdf` (98 pages)


## Slide 1

##### GPUBreach: Privilege Escalation Attacks on GPUs using Rowhammer

**Presenters:**

Chris S. Lin Yuqin Yan Guozhen Ding

**In collaboration with:**

Joyce Qu, Joseph Zhu, David Lie, and Gururaj Saileshwar

**#BHUSA @BlackHatEvents**

## Slide 2

**GPU Chip VRAM (GDDR6)**

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)


> Recovered by OCR — confidence 87/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
VRAM
(GDDR6)
black hat
2026 Chris S. Lin (Shaopeng.lin@cs.toronto.edu) Yugin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)
```

## Slide 3

### **Executive Summary of GPUBreach**

Page
Flip bits on GPU Memory to Corrupt Page Tables Table
GPU
Enables GPU Privilege Escalation Attacks VRAM
DMA
System-Wide Root Privileges on Host

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 4

**What’s Rowhammer (on GPUs)?**

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 5

### **The Rowhammer Vulnerability**

0 0 0 1 0 0 0 1 0 0
0 1 0 1 0 0 1 0 0 0
0 0 0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1
…

Memories are organized into **rows** of electrical cells (binary data)

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 6

### **The Rowhammer Vulnerability**

0 0 0 1 0 0 0 1 0 0
0 1 0 1 0 0 1 0 0 0
Repeated
0  1  0  0  0  1 0  0 0 0
Accesses
1 1 1 1 1 1 1 1 1 1
…
Rapid Accesses to Rows Can Flip Bits in its Neighbour!

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 7

### **CPU Rowhammer Exploits**

###### **Rowhammer Exploits are well-studied on CPUs**

Kernel Exploit: NaCI Exploit:
Page Table Tampering Corrupt Insturction
jmp
Page
Page
PageTables
Mark Seaborn Tables
Tables jmp rcx
(Blackhat 2015) Root!
And many more enabled by bit flips…

NaCI Exploit:
Corrupt Insturction
jmp rax
jmp rcx

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 8

### **State of Rowhammer**

DDR3-5
LPDDR3&4X
All Vulnerable!

Still Not Fixed! And Getting Worse!

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 9

### **Rowhammer on GPUs**

**GPUHammer [SEC’25]** Found bit flips on RTX A6000 GPU, GDDR6 Memory

###### Chris S. Lin,    Joyce Qu Gururaj Saileshwar

<u>https://www.utoronto.ca/news/how-three-u-t-researchers-discoveredgpu-vulnerability-threatened-ai-models</u>

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 10

### **Rowhammer on GPUs**

**GPUHammer [SEC’25]** Found bit flips on RTX A6000 GPU, GDDR6 Memory

**Accuracy 0%**

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 11

### **Rowhammer on GPUs**

**But GPU Rowhammer Has A Huge Gap…**

Better
Exploits?
What about when:
No time-slicing while sharing?
20+ Product Lines at Risk!
No sharing at all?

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 12

# **Background**

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 13

### **Page Tables in GPU**

Virtual Address
GPU Memory
0xABCD Management Unit
( GMMU )
Physical Address
0x0001
GPU VRAM

**Page Table Purpose:** Stores data for address translation.

Page
Page
Page Tables
Tables
Tables

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 14

### **Page Tables in GPU**

Frame
16B PagePage
Page Tables
Tables
(2MB)
Tables
PT (4KB)
Frame
8B
8B (4KB)
8B
8B
Frame
(64KB)
PD0 (4KB) PT (256B)

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 15

### **Page Tables in GPU: PTEs**

We target the physical address bits.
AD RO P E VOL A V

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 16

Page Table Tampering No need to thank me
Step 1:  Step 2:  Step 3:
Neighbor PT & Aggressor Corrupt PTE  Place PT in New Dest.
Original
Virtual
Frame
Address
Page GPU
0x1234 PTE
Table VRAM
Page
Table

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 17

### **Page Table Tampering**

###### **From their own words (Blackhat ‘15):**

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 18

### **Page Table Tampering**

**From their own words (Blackhat ‘15):**

**Can’t Fill GPU VRAM with PTE like on Linux**

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 19

### **Where are Page Tables?**

GPU Page Table Placements **(2MB PT Region)**

**PT Region**

PT
PD0
200+ MBs
DATA

**Challenge:** Naively Filling PT Region Requires Allocating **256 GB** of Memory Initial PT Region is **Far Away (200+ MB)** from User Data

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 20

### **Challenges For Page Table Massaging**

**1 Memory Inefficiency of Page Table Allocations**

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 21

### **Q1. How to Get More PT Regions?**

cudaMalloc() cudaMallocManaged()
4KB
64KB
2MB
4KB PT
256B PT
16B PTE
256GB 16GB 1GB

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 22

### **Q1. How to Get More PT Regions?**

###### **Unified Virtual Memory (UVM)**

VRAM DRAM

###### cudaMallocManaged()

**CPU as Swap**

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 23

### **Q1. How to Get More PT Regions?**

DNE?
cudaMalloc() cudaMallocManaged()
4KB
64KB
2MB
4KB PT
256B PT
16B PTE
256GB 16GB 1GB

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 24

### **Getting 4KB Pages! (They thought it DNE…)** cudaMallocManaged(&ptr, **2 MB + 4 KB** )

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 25

### **Getting 4KB Pages!**

###### cudaMallocManaged(&ptr, **2 MB + 4 KB** <u>)</u>

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 26

### **Getting 4KB Pages!**

cudaMallocManaged(&ptr, **<u>2 MB + 4 KB</u>** )

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 27

**Getting 4KB Pages!** cudaMallocManaged(&ptr, **<u>2 MB + 4 KB</u>** )

**I am Lazy Loaded!**

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 28

### **Q2. How to Get Dense PT Regions?**

4KB PT can efficiently allocate PT Regions **, but...**

4KB PT is Sparse… à Hard to Hit PTEs PTEs (3%) PT

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 29

### **Q2. How to Get Dense PT Regions?**

1. Access
UVM Eviction!
64KB
64KB
2MB 64KB
97% 31X
PT (256B)

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 30

### **Q2. How to Get Dense PT Regions?**

1. Access
UVM Eviction!
64KB
64KB
2MB 64KB
64KB
97% 31X
2. Evict to CPU PT (256B)

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 31

### **Q2. How to Get Dense PT Regions?**

1. Access
UVM Eviction!
64KB
64KB
2MB 64KB
64KB
97% 31X
2. Evict to CPU PT (256B)

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 32

Q2. How to Get Dense PT Regions?
1. Access
UVM Eviction!
64KB
64KB
2MB 64KB
3. Converts
64KB
97% 31X
2. Evict to CPU PT (256B)

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 33

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 90/100 on the text kept, 85/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
[Terminal window]

# Before Eviction
243-->PD0@0x000c035000
    48-->2MB-Page@0x001cc00000

# After Eviction
243-->PD0@0x000c035000
    48-->PT@0x000c022100
        0-->64KB-Page@0x001cc00000
        1-->64KB-Page@0x001cc10000
        2-->64KB-Page@0x001cc20000
        3-->64KB-Page@0x001cc30000

[A large red arrow points at the line "48-->2MB-Page@0x001cc00000"]
```

## Slide 34

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 90/100 on the text kept, 85/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
[Terminal window]

# Before Eviction
243-->PD0@0x000c035000
    48-->2MB-Page@0x001cc00000

# After Eviction
243-->PD0@0x000c035000
    48-->PT@0x000c022100
        0-->64KB-Page@0x001cc00000
        1-->64KB-Page@0x001cc10000
        2-->64KB-Page@0x001cc20000
        3-->64KB-Page@0x001cc30000

[A large red arrow points at the line "48-->PT@0x000c022100"]
```

## Slide 35

### **Challenges For Page Table Massaging**

**1 Efficient & Dense PT Region Allocation Technique!**

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 36

### **Challenges For Page Table Massaging**

**1 Efficient & Dense PT Region Allocation Technique!**

**2 Lack of Control Over GPU PT Region Placement.**

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 37

### **How to Massage PTEs?**

PT Region
Target Memory

Observation:
PT Region and User Data
use the SAME memory pool

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 38

### **How to Massage PTEs?**

Full PT Region PT Region
Target Memory

**Observation:** PT Region and User Data use the SAME memory pool

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 39

### **How to Massage PTEs?**

Full PT Region PT Region
Target Memory Free Target
Free

**Observation:** PT Region and User Data use the SAME memory pool

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 40

### **How to Massage PTEs?**

**Full PT Region PT Region Target Memory** **Free Target Allocate Free**

**Observation:** PT Region and User Data use the SAME memory pool

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 41

### **How to Massage PTEs?**

Full PT Region PT Region
New PT Region Target MemoryFree Target
Allocate Free

Observation:
PT Region and User Data
use the SAME memory pool

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 42

### **How to Massage PTEs?**

**Full PT Region PT Region** **New PT Region Target MemoryFree TargetFree Target**

New PT Region Target MemoryFree TargetFree Target
Allocate Free

**Observation:** PT Region and User Data use the SAME memory pool

Question: **How do we know when PT Region is full?**

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 43

### **Challenges For Page Table Massaging**

**1 Efficient & Dense PT Region Allocation Technique!**

- **2 Exhaust VRAM to Force Placement!**

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 44

### **Challenges For Page Table Massaging**

- **1 Efficient & Dense PT Region Allocation Technique!**

- **2 Exhaust VRAM to Force Placement!**

- **3 PT Region Allocation is Invisible to Attacker.**

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 45

### **Identify PT Region Allocations**

Silent
Allocation

We leverage **timing side-channel** in **Unified Virtual Memory (UVM)**

Full PT Region
New PT Region Free Target
Allocate Evict

Allocations Above Memory Limit are **Evicted to CPU**

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 46

### **Eviction Timing Side-channel!**

Fill GPU memory full

###### **PT Region**

DATA

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 47

### **Eviction Timing Side-channel!**

Fill GPU memory full

Repeat Evict and allocate **(Low Latency)**

**PT Region**

**PT Region**

DATA

DATA

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 48

### **Eviction Timing Side-channel!**

Fill GPU memory full **PT Region**

DATA

Repeat Evict and allocate **(Low Latency)**

PT Region
Evicted / Freed
DATA

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 49

### **Eviction Timing Side-channel!**

Fill GPU memory full

Repeat Evict and allocate **(Low Latency)**

**PT Region**

DATA

**PT Region** Evicted / FreedAllocate DATA

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 50

### **Eviction Timing Side-channel!**

Fill GPU memory full **PT Region**

DATA

Repeat Evict and allocate **(Low Latency)**

PT Region
Evicted / Freed
DATA

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 51

### **Eviction Timing Side-channel!**

Fill GPU memory full

Repeat Evict and allocate **(Low Latency)**

**PT Region**

DATA

**PT Region** Evicted / FreedAllocate DATA

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 52

### **Eviction Timing Side-channel!**

Repeat Evict and allocate New PT region needed Fill GPU memory full **(Low Latency) (High Latency!)** **PT Region PT Region Full Region** Evicted / FreedAllocate Evicted / Freed DATA DATA DATA

New PT region needed **(High Latency!)**

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 53

### **Eviction Timing Side-channel!**

Fill GPU memory full **PT Region**

DATA

Repeat Evict and allocate New PT region needed **(Low Latency) (High Latency!)** **PT Region Full Region** Evicted / FreedAllocate Evicted / FreedAllocate DATA DATA

New PT region needed **(High Latency!)**

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 54

### **Eviction Timing Side-channel!**

Repeat Evict and allocate New PT region needed Fill GPU memory full **(Low Latency) (High Latency!)** **PT Region PT Region Full Region** Evicted / FreedAllocate Evicted / FreedAllocate DATA DATA DATA **PT Region**

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 55

### **Eviction Timing Side-channel!**

Fill GPU memory full **PT Region**

DATA

Repeat Evict and allocate New PT region needed
(Low Latency) (High Latency!)
PT Region Full Region
Evicted / FreedAllocate Evicted / FreedAllocate
DATA DATA
PT Region
Eviction!

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 56

Eviction Timing Side-channel!
508 508 508 508

PT Region
Allocation
We can  deterministically  predict PT Region Allocations.

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 57

### **Challenges For Page Table Massaging**

- **1 Efficient & Dense PT Region Allocation Technique!**

- **2 Exhaust VRAM to Force Placement!**

- **3 Timing Side-channel to Detect Allocation!**

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 58

Page Table Tampering
Step 1:  Step 2:  Step 3:
Neighbor PT & Aggressor Corrupt PTE  Place PT in New Dest.
Original
Virtual
Frame
Address
Page GPU
0x1234 PTE
Table VRAM
Page
Table

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 59

GPUBreach can **Practically & Reliably Tamper GPU Page Tables** and enable downstream privilege escalation.

Works on open-source driver versions from 2023-26. Tested on RTX A6000 GPU.

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 60

### **Exploits!**

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 61

### **Exploit 1: Arbitrary Read on GPU**

**Arbitrary Read:** What can we steal?

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 62

### **Exploit 1: Arbitrary Read on GPU**

Attacker
Arbitrary Read:
What can we steal?

Victim

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 63

### **Exploit 1: Arbitrary Read on GPU**

ML Model

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 64

### **Exploit 1: Arbitrary Read on GPU**

ML Model

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 65

### **Exploit 1: Arbitrary Read on GPU**

ML Model Crypto Keys
(Short-lived)

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 66

### **Exploit 1: Arbitrary Read on GPU**

ML Model Crypto Keys

<u>https://developer.nvidia.com/cupqc</u>

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 67

### **Exploit 1: Arbitrary Read on GPU**

ML Model Crypto Keys
Where are the keys?
Monitor GPU State Changed
GPU State Start Dumping
Key Exchange Key Exchange
Starts Finishes
~6 ms

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 68

### **Exploit 1: Arbitrary Read on GPU**

###### **Approach 1:** Shared Library

**Approach 2:** Victim Page Profiling **Obs.** Memories are Zeroed on Free

###### **Attacker Key**

Victim Key

**0x1234 0x1234** Physical Location Equivalent

0xFFFFFFFF 0xFFFFFFFF 0xFFFFFFFF 0xFFFFFFFF

Before

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 69

### **Exploit 1: Arbitrary Read on GPU**

###### **Approach 1:** Shared Library

Attacker Key Victim Key

**0x1234 0x1234** Physical Location Equivalent

Approach 2:  Victim Page Profiling
Obs.  Memories are Zeroed on Free
0xFFFFFFFF 0xFFFFFFFF
0xFFFFFFFF 0x0
0xFFFFFFFF 0xFFFFFFFF
0xFFFFFFFF 0x0
Before After

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 70

### **Exploit 1: Arbitrary Read on GPU**

Attacker **Arbitrary Read:** What can we steal?

Victim

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 71

### **Exploit 1: Arbitrary Read on GPU**

Attacker Leak **ML model weights** and **secret keys** from GPU memory

Victim

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 72

### **Exploit 2: Arbitrary Write on GPU**

Attacker

Victim

Leak **ML model weights** and **secret keys** from GPU memory

**Arbitrary Write:** What can we tamper?

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 73

### **Exploit 2: Arbitrary Write on GPU**

0% Model
Accuracy
Universal
Degradation

**But everything seems fine…**

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 74

### **Exploit 2: Arbitrary Write on GPU**

**Offline Phase:** Filter Critical Instructions

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 75

### **Exploit 2: Arbitrary Write on GPU**

**Offline Phase:** Filter Critical Instructions

Identify Kernels

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 76

### **Exploit 2: Arbitrary Write on GPU**

**Offline Phase:** Filter Critical Instructions

Branch in SASS

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 77

### **Exploit 2: Arbitrary Write on GPU**

**Offline Phase:** Filter Critical Instructions

**Goal:** Find Branch that

(1) Degrade models universally (2) ~0% Runtime Impact

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 78

### **Exploit 2: Arbitrary Write on GPU**

**Offline Phase:** Filter Critical Instructions

**Goal:** Find Branch that (1) Degrade models universally (2) ~0% Runtime Impact

Filter by this criteria at different granularity **Pages** SASS Template **Kernels Instructions**

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 79

### **Exploit 2: Arbitrary Write on GPU**

**Offline Phase:** Filter Critical Instructions SASS Template

**Online Phase:** Apply Template to Victim Code

0% Model
Accuracy
Code
Segment
No
(1) CPU-side Change
(2) Runtime Change

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 80

### **Exploit 2: Arbitrary Write on GPU**

Attacker

Victim

Leak **ML model weights** and **secret keys** from GPU memory

**Arbitrary Write:** What can we tamper?

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 81

### **Exploit 2: Arbitrary Write on GPU**

Attacker

Victim

Leak **ML model weights** and **secret keys** from GPU memory

**Stealthily tamper cuBLAS code** & universally degrade ML accuracy

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 82

## **Let’s do even better!**

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 83

### **Exploit 3: CPU-side Privilege Escalation**

CPU DRAM

CPU DRAM
Malicious DMA to Host DRAM
Privilege Escalation to the Host!
A = 11
CPU Memory
AD RO P E VOL A V
Aperture:
Select between GPU and CPU Memory

A = 00 **GPU VRAM**

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 84

### **Exploit 3: CPU-side Privilege Escalation**

**CPU DRAM Malicious DMA to Host DRAM**

**IOMMU DisabledEnabled**

**Entire Host MemoryIOMMU Protected Host MemoryTamperable**

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 85

### **Exploit 3: CPU-side Privilege Escalation**

CPU DRAM
Malicious DMA to Host DRAM
Driver
GPU Status Queue
Unprotected
Message
Region
Root Shell
Buffer Overflow
Staging Buffer Pointers
IOMMU
Protected Message

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 86

### **Exploit 3: CPU-side Privilege Escalation**

**GPU Status Queue Staging Buffer** Message Message

**Unprotected DMA Region**

**IOMMU Protected**

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 87

### **Exploit 3: CPU-side Privilege Escalation**

GPU Status Queue Staging Buffer [16]
Message Message
1 st Entry 16 th
elemCount =  16 … Entry
Unsanitized
Unprotected DMA Region IOMMU Protected

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 88

### **Exploit 3: CPU-side Privilege Escalation**

GPU Status Queue Staging Buffer [16]
Message Message
1 st Entry 16 th
elemCount =  17 … Entry
Unsanitized
Unprotected DMA Region IOMMU Protected

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 89

### **Exploit 3: CPU-side Privilege Escalation**

GPU Status Queue Staging Buffer [16]
Message Message
1 st Entry 16 th
elemCount =  17 … Entry
Unsanitized 17 th Entry
Unprotected DMA Region IOMMU Protected

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 90

### **Exploit 3: CPU-side Privilege Escalation**

GPU Status Queue
Message
1 st Entry 16 th
…
Staging Buffer [16]
elemCount =  17 Entry
Message
Unsanitized 17 th Entry
Unprotected DMA Region IOMMU Protected

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 91

### **Exploit 3: CPU-side Privilege Escalation**

GPU Status Queue
Message
1 st Entry 16 th
elemCount =  17 … Entry
Staging Buffer  [16] pMetadata
Unsanitized 17 th Entry
Unprotected DMA Region IOMMU Protected

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 92

### **Exploit 3: CPU-side Privilege Escalation**

GPU Status Queue
Message
Writes to
pReadOutgoing rxReadPtr
1 st Entry 16 th
elemCount =  17 … Entry
Staging Buffer  [16] pMetadata
Unsanitized 17 th Entry
Unprotected DMA Region IOMMU Protected

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 93

### **Exploit 3: CPU-side Privilege Escalation**

GPU Status Queue
_backendWrite32
Message &EUID 0(Root)
pReadOutgoing rxReadPtr
1 st Entry 16 th
elemCount =  17 … Entry
Staging Buffer  [16] pMetadata
Unsanitized 17 th Entry
Unprotected DMA Region IOMMU Protected

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 94

### **Takeaways**

###### **GPU Rowhammer is a real threat!**

- § We went from random corruption to targeted attacks that take over GPUs.

**CPU-side Driver is not safe from a malicious GPU.**

- § GPUBreach extended the exploit to the host, gaining powerful primitives

- § Driver’s lack of sanitization on input from the GPU is the main culprit.

**Rethinking GPU Security Assumptions**

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 95

### **Takeaways**

PT Region
DATA
VRAM
ECC
GDDR

**Sanitize GPU-Side Inputs in Driver**

**Isolate GPU Page Tables from Data**

**Error Correction Codes in GPU DRAM**

**Principled RH Defense in GPU DRAM**

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 96

### **Responsible Disclosure**

Responsibly disclosed to NVIDIA & Cloud Vendors

###### **GPUBreach has been reported to respective parties.**

§ **Vendor:** NVIDIA. **CSPs:** Google, Microsoft, etc

- § NVIDIA acknowledged the risks, while the CSPs are discussing mitigation approaches with their respective engineering teams.

Awarded **Google Bug Bounty**

Awarded IEEE S&P **Distinguished Paper**

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 97

### **Thanks!**

#### **Collaborators:** Joyce Qu, Joseph Zhu, David Lie, and Gururaj Saileshwar

**Presentation Coach:** Philip Young

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 98

### **Thanks!**

www.gpubreach.ca

#### **Contacts:**

Chris: email: <u>shaopenglin@cs.toronto.edu</u> personal site: https://shaopenglin.github.io Yuqin: email: <u>me@yqyan.com</u>

Guozhen: email: <u>gzh.ding@mail.utoronto.ca</u> personal site : <u>https://www.guozhen.dev/</u>

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)
