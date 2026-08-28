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
vision_verified_pages_changed: 72
vision_verified_pages: 98
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

Chris S. Lin

Yuqin Yan

Guozhen Ding

**In collaboration with:**

Joyce Qu, Joseph Zhu, David Lie, and Gururaj Saileshwar

**#BHUSA @BlackHatEvents**

## Slide 2

**GPU Chip**

**VRAM (GDDR6)**

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 3

### **Executive Summary of GPUBreach**

Flip bits on GPU Memory to Corrupt Page Tables

Page Table

Enables GPU Privilege Escalation Attacks

GPU VRAM

System-Wide Root Privileges on Host

DMA

CPU

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

Repeated Accesses

0 0 0 1 0 0 0 1 0 0
0 1 0 1 0 0 1 0 0 0
0 1 0 0 0 1 0 0 0 0
1 1 1 1 1 1 1 1 1 1
…

Rapid Accesses to Rows Can Flip Bits in its Neighbour!

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 7

### **CPU Rowhammer Exploits**

###### **Rowhammer Exploits are well-studied on CPUs**

Mark Seaborn
(Blackhat 2015)

Kernel Exploit:
Page Table Tampering

Page Tables

~$ whoami
root

Root!

NaCl Exploit:
Corrupt Insturction

jmp rax

jmp rcx

And many more enabled by bit flips…

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 8

### **State of Rowhammer**

DDR3-5

LPDDR3&4X

**All Vulnerable!**

Rowhammer Threshold (T_RH)

139K   22K   18K   10K   4.8K   ?   ?

DDR3 (2014)   DDR4 (2018)   LPDDR4 (2020)   LPDDR5, DDR5 (2023)   DDR6 …

Still Not Fixed! And Getting Worse!

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 9

### **Rowhammer on GPUs**

**GPUHammer [SEC’25]**

Found bit flips on RTX A6000 GPU, GDDR6 Memory

Chris S. Lin,    Joyce Qu
Gururaj Saileshwar

<u>https://www.utoronto.ca/news/how-three-u-t-researchers-discovered-gpu-vulnerability-threatened-ai-models</u>

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 10

### **Rowhammer on GPUs**

**GPUHammer [SEC’25]** Found bit flips on RTX A6000 GPU, GDDR6 Memory

**Accuracy 0%**

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 11

### **Rowhammer on GPUs**

**But GPU Rowhammer Has A Huge Gap…**

Better Exploits?

**What about when:**

*No time-slicing while sharing?*

*No sharing at all?*

20+ Product Lines at Risk!

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 12

# **Background**

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 13

### **Page Tables in GPU**

Virtual Address
0xABCD

GPU Memory Management Unit (**GMMU**)

Page Tables

Physical Address
0x0001

GPU VRAM

**Page Table Purpose:** Stores data for address translation.

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 14

### **Page Tables in GPU**

16B

Frame (2MB)

PT (4KB)

8B

Frame (4KB)

PD0 (4KB)

8B
8B

PT (256B)

8B

Frame (64KB)

Page Tables

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 15

### **Page Tables in GPU: PTEs**

We target the physical address bits.

63    55   53                                            7

Type | Physical Address [:12] | AD | RO | P | E | VOL | A | V

PTE Flags [7:0]

64-bit PTE Format

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 16

### **Page Table Tampering**

No need to thank me

**Step 1:**
Neighbor PT & Aggressor

**Page Table**

Virtual Address
0x1234

**Step 2:**
Corrupt PTE

PTE

Original Frame

**Step 3:**
Place PT in New Dest.

**Page Table**

**GPU VRAM**

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 17

### **Page Table Tampering**

**From their own words (Blackhat ‘15):**

Mark was more clever: He simply put the system under memory pressure - when backed into a corner, the OS behaves nicely.

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 18

### **Page Table Tampering**

**From their own words (Blackhat ‘15):**

Mark was more clever: He simply put the system under memory pressure - when backed into a corner, the OS behaves nicely.

**Can’t Fill GPU VRAM with PTE like on Linux**

Possible somehow. I spent a few afternoons fumbling around in the Linux physical page allocator. Not very fun code.

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 19

### **Where are Page Tables?**

GPU Page Table Placements **(2MB PT Region)**

**PT Region**

PT
PD0
200+ MBs
DATA

**Challenge:** Naively Filling PT Region Requires Allocating **256 GB** of Memory

Initial PT Region is **Far Away (200+ MB)** from User Data

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 20

### **Challenges For Page Table Massaging**

**1 Memory Inefficiency of Page Table Allocations**

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 21

### **Q1. How to Get More PT Regions?**

cudaMalloc()

2MB

16B PTE

256GB

cudaMallocManaged()

64KB

256B PT

16GB

4KB

4KB PT

1GB

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 22

### **Q1. How to Get More PT Regions?**

**Unified Virtual Memory (UVM)**

cudaMallocManaged()

VRAM → DRAM

CPU

**CPU as Swap**

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 23

### **Q1. How to Get More PT Regions?**

cudaMalloc()

2MB

16B PTE

256GB

cudaMallocManaged()

64KB

256B PT

16GB

DNE?

4KB

4KB PT

1GB

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 24

### **Getting 4KB Pages! (They thought it DNE…)**

cudaMallocManaged(&ptr, **2 MB + 4 KB**)

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 25

### **Getting 4KB Pages!**

cudaMallocManaged(&ptr, **2 MB + <u>4 KB</u>**)

Page Type (y-axis): 2MB, 64KB, 4KB

Allocation Size (x-axis): 0, 0.5MB, 1MB, 1.5MB, 2MB

Legend: 2MB, 64KB, 4KB

```text
241-->PT@0x000c036000
    0-->4KB-Page@0x001cc00000
243-->PT@0x000c037000
    0-->4KB-Page@0x001cc01000
245-->PT@0x000c038000
    0-->4KB-Page@0x001cc02000
```

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 26

### **Getting 4KB Pages!**

?

cudaMallocManaged(&ptr, **<u>2 MB</u> + 4 KB**)

Page Type (y-axis): 2MB, 64KB, 4KB

Allocation Size (x-axis): 0, 0.5MB, 1MB, 1.5MB, 2MB

Legend: 2MB, 64KB, 4KB

```text
241-->PT@0x000c036000
    0-->4KB-Page@0x001cc00000
243-->PT@0x000c037000
    0-->4KB-Page@0x001cc01000
245-->PT@0x000c038000
    0-->4KB-Page@0x001cc02000
```

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 27

### **Getting 4KB Pages!**

I am Lazy Loaded!

cudaMallocManaged(&ptr, **<u>2 MB</u> + 4 KB**)

Page Type (y-axis): 2MB, 64KB, 4KB

Allocation Size (x-axis): 0, 0.5MB, 1MB, 1.5MB, 2MB

Legend: 2MB, 64KB, 4KB

```text
241-->PT@0x000c036000
    0-->4KB-Page@0x001cc00000
243-->PT@0x000c037000
    0-->4KB-Page@0x001cc01000
245-->PT@0x000c038000
    0-->4KB-Page@0x001cc02000
```

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 28

### **Q2. How to Get Dense PT Regions?**

4KB PT can efficiently allocate PT Regions**, but...**

Page Type (y-axis): 2MB, 64KB, 4KB

Allocation Size (x-axis): 0, 0.5MB, 1MB, 1.5MB, 2MB

Legend: 2MB, 64KB, 4KB

4KB PT is Sparse… → Hard to Hit PTEs

PTEs (3%)

PT

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 29

### **Q2. How to Get Dense PT Regions?**

**1. Access**

CPU

**UVM Eviction!**

2MB

64KB

97%

PT (256B)

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 30

### **Q2. How to Get Dense PT Regions?**

1. Access

CPU

**UVM Eviction!**

2MB

64KB

**2. Evict to CPU**

64KB

97%

PT (256B)

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 31

### **Q2. How to Get Dense PT Regions?**

1. Access

CPU

**UVM Eviction!**

2MB

64KB

**2. Evict to CPU**

64KB

97%

PT (256B)

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 32

### **Q2. How to Get Dense PT Regions?**

1. Access

CPU

**UVM Eviction!**

2MB

**3. Converts**

64KB

2. Evict to CPU

64KB

97%

PT (256B)

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 33

```text
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
```

## Slide 34

```text
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

**Observation:**
PT Region and User Data use the <u>SAME</u> memory pool

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 38

### **How to Massage PTEs?**

Full PT Region

Target Memory

**Observation:**
PT Region and User Data use the <u>SAME</u> memory pool

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 39

### **How to Massage PTEs?**

Full PT Region

Free Target

Free

**Observation:**
PT Region and User Data use the <u>SAME</u> memory pool

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 40

### **How to Massage PTEs?**

Full PT Region

Free Target

Allocate

**Observation:**
PT Region and User Data use the <u>SAME</u> memory pool

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 41

### **How to Massage PTEs?**

Full PT Region

New PT Region

Allocate

**Observation:**
PT Region and User Data use the <u>SAME</u> memory pool

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 42

### **How to Massage PTEs?**

Full PT Region

New PT Region

Allocate

**Observation:**
PT Region and User Data use the <u>SAME</u> memory pool

Question:
**How do we know when PT Region is full?**

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 43

### **Challenges For Page Table Massaging**

**1 Efficient & Dense PT Region Allocation Technique!**

**2 Exhaust VRAM to Force Placement!**

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 44

### **Challenges For Page Table Massaging**

- **1 Efficient & Dense PT Region Allocation Technique!**

- **2 Exhaust VRAM to Force Placement!**

- **3 PT Region Allocation is Invisible to Attacker.**

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 45

### **Identify PT Region Allocations**

Silent Allocation

Full PT Region

New PT Region

Allocate

We leverage **timing side-channel** in **Unified Virtual Memory (UVM)**

Latency (ms) [y-axis]: 0.1, 0.3, 0.5

Number of 2MB Allocations [x-axis]: 6000, 12000, 18000, 24000

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

**PT Region**

Allocate

DATA

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

**PT Region**

Allocate

DATA

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 52

### **Eviction Timing Side-channel!**

Fill GPU memory full

Repeat Evict and allocate **(Low Latency)**

New PT region needed **(High Latency!)**

**PT Region**

DATA

**PT Region**

Allocate

DATA

**Full Region**

Evicted / Freed

DATA

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 53

### **Eviction Timing Side-channel!**

Fill GPU memory full

Repeat Evict and allocate **(Low Latency)**

New PT region needed **(High Latency!)**

**PT Region**

DATA

**PT Region**

Allocate

DATA

**Full Region**

Allocate

DATA

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 54

### **Eviction Timing Side-channel!**

Fill GPU memory full

Repeat Evict and allocate **(Low Latency)**

New PT region needed **(High Latency!)**

**PT Region**

DATA

**PT Region**

Allocate

DATA

**Full Region**

Allocate

DATA

**PT Region**

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 55

### **Eviction Timing Side-channel!**

Fill GPU memory full

Repeat Evict and allocate **(Low Latency)**

New PT region needed **(High Latency!)**

**PT Region**

DATA

**PT Region**

Allocate

DATA

**Full Region**

Allocate

DATA

**PT Region**

**Eviction!**

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 56

### **Eviction Timing Side-channel!**

508  508  508  508

420  928  1436  1944  2452

Latency (ms)

PT Region Allocation

4KB Page Frames Allocated

We can **deterministically** predict PT Region Allocations.

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 57

### **Challenges For Page Table Massaging**

- **1 Efficient & Dense PT Region Allocation Technique!**

- **2 Exhaust VRAM to Force Placement!**

- **3 Timing Side-channel to Detect Allocation!**

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 58

### **Page Table Tampering**

**Step 1:**
Neighbor PT & Aggressor

**Step 2:**
Corrupt PTE

**Step 3:**
Place PT in New Dest.

**Page Table**

Virtual Address

0x1234

PTE

Original Frame

**Page Table**

**GPU VRAM**

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

|  | Variant |
| --- | --- |
| Llama2 (7B) | Meta*<br>Nous<br>Meta, Chat |
| Llama3 (8B) | Meta*<br>Nous<br>Meta, Instruct |
| Mistral (7B) | v1.0*<br>Instruct v1.0<br>OpenHermes 2.5 |
| Gemma (7B) | Google*<br>Google, Instruct |

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 64

### **Exploit 1: Arbitrary Read on GPU**

ML Model

|  | Variant | Llama2 | Llama3 | Mistral | Gemma |
| --- | --- | --- | --- | --- | --- |
| Llama2 (7B) | Meta* | 0.99 | -0.20 | -0.05 | 0.29 |
|  | Nous | 0.99 | -0.20 | -0.05 | 0.29 |
|  | Meta, Chat | 0.99 | -0.20 | -0.05 | 0.29 |
| Llama3 (8B) | Meta* | 0.06 | 1.00 | 0.07 | -0.02 |
|  | Nous | 0.06 | 1.00 | 0.07 | -0.02 |
|  | Meta, Instruct | 0.06 | 1.00 | 0.07 | -0.02 |
| Mistral (7B) | v1.0* | 0.94 | -0.18 | 1.00 | 0.23 |
|  | Instruct v1.0 | 0.94 | -0.18 | 1.00 | 0.25 |
|  | OpenHermes 2.5 | 0.94 | -0.18 | 1.00 | 0.23 |
| Gemma (7B) | Google* | -0.04 | -0.20 | -0.08 | 1.00 |
|  | Google, Instruct | -0.03 | -0.16 | -0.04 | 0.97 |

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 65

### **Exploit 1: Arbitrary Read on GPU**

ML Model Crypto Keys
(Short-lived)

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 66

### **Exploit 1: Arbitrary Read on GPU**

ML Model Crypto Keys

**NVIDIA cuPQC**

https://developer.nvidia.com/cupqc

**NVIDIA cuPQC** is an SDK of GPU-optimized cryptographic math libraries for building both classical and next-generation high-performance cryptographic applications.

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 67

### **Exploit 1: Arbitrary Read on GPU**

ML Model Crypto Keys

Where are the keys?

Monitor GPU State

GPU State Changed Start Dumping

Key Exchange Starts

Key Exchange Finishes

~6 ms

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 68

### **Exploit 1: Arbitrary Read on GPU**

**Approach 1:** Shared Library

open-quantum-safe/**liboqs**

**Attacker Key**

**Victim Key**

**0x1234** <-> **0x1234**

Physical Location Equivalent

**Approach 2:** Victim Page Profiling

**Obs.** Memories are Zeroed on Free

0xFFFFFFFF

0xFFFFFFFF

0xFFFFFFFF

0xFFFFFFFF

Before

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 69

### **Exploit 1: Arbitrary Read on GPU**

**Approach 1:** Shared Library

open-quantum-safe/**liboqs**

**Attacker Key**

**Victim Key**

**0x1234** <-> **0x1234**

Physical Location Equivalent

**Approach 2:** Victim Page Profiling

**Obs.** Memories are Zeroed on Free

| Before | After |
| --- | --- |
| 0xFFFFFFFF | 0xFFFFFFFF |
| 0xFFFFFFFF | 0x0 |
| 0xFFFFFFFF | 0xFFFFFFFF |
| 0xFFFFFFFF | 0x0 |

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

cuBLAS

**0% Model Accuracy**

**Universal Degradation**

**But everything seems fine…**

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 74

### **Exploit 2: Arbitrary Write on GPU**

**Offline Phase:** Filter Critical Instructions

```
/* 0x0000011000000947, 0x003fde0003800000 */
@P0 BRA 0x1d0 ;
/* 0x0000000000007947, 0x003fde0003800000 */
BRA 0xd0 ;
...
/* 0x0000000000007918, 0x000fc00000000000 */
NOP;
```

PyTorch

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 75

### **Exploit 2: Arbitrary Write on GPU**

**Offline Phase:** Filter Critical Instructions

Identify Kernels

```
/* 0x0000011000000947, 0x003fde0003800000 */
@P0 BRA 0x1d0 ;
/* 0x0000000000007947, 0x003fde0003800000 */
BRA 0xd0 ;
...
/* 0x0000000000007918, 0x000fc00000000000 */
NOP;
```

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 76

### **Exploit 2: Arbitrary Write on GPU**

**Offline Phase:** Filter Critical Instructions

Branch in SASS

```
/* 0x0000011000000947, 0x003fde0003800000 */
@P0 BRA 0x1d0 ;
/* 0x0000000000007947, 0x003fde0003800000 */
BRA 0xd0 ;
...
/* 0x0000000000007918, 0x000fc00000000000 */
NOP;
```

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 77

### **Exploit 2: Arbitrary Write on GPU**

**Offline Phase:** Filter Critical Instructions

**Goal:** Find Branch that

(1) Degrade models universally

(2) ~0% Runtime Impact

```
/* 0x0000011000000947, 0x003fde0003800000 */
@P0 BRA 0x1d0 ;
/* 0x0000000000007947, 0x003fde0003800000 */
BRA 0xd0 ;
...
/* 0x0000000000007918, 0x000fc00000000000 */
NOP;
```

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 78

### **Exploit 2: Arbitrary Write on GPU**

**Offline Phase:** Filter Critical Instructions

**Goal:** Find Branch that

(1) Degrade models universally

(2) ~0% Runtime Impact

```
/* 0x0000011000000947, 0x003fde0003800000 */
@P0 BRA 0x1d0 ;
/* 0x0000000000007947, 0x003fde0003800000 */
BRA 0xd0 ;
...
/* 0x0000000000007918, 0x000fc00000000000 */
NOP;
```

Filter by this criteria at different granularity

**Pages**

**Kernels**

**Instructions**

SASS Template

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 79

### **Exploit 2: Arbitrary Write on GPU**

**Offline Phase:** Filter Critical Instructions

SASS Template

**Online Phase:** Apply Template to Victim Code

PyTorch

**Code Segment**

cuBLAS

**0% Model Accuracy**

**No**
**(1) CPU-side Change**
**(2) Runtime Change**

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

**Malicious DMA to Host DRAM**

**Privilege Escalation to the Host!**

CPU

**CPU DRAM**

A = 00

**GPU VRAM**

**CPU Memory**

A = 11

63  55  53

Type

Physical Address [:12]

7

**PTE Flags [7:0]**

AD | RO | P | E | VOL | A | V

**Aperture:**
Select between GPU and CPU Memory

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 84

### **Exploit 3: CPU-side Privilege Escalation**

**Malicious DMA to Host DRAM**

CPU

**CPU DRAM**

IOMMU **Enabled**

**IOMMU Protected Host Memory**

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 85

### **Exploit 3: CPU-side Privilege Escalation**

**Malicious DMA to Host DRAM**

CPU

**CPU DRAM**

**Driver**

**Unprotected Region**

**GPU Status Queue**

Message

**Buffer Overflow**

**IOMMU Protected**

**Staging Buffer**

**Pointers**

Message

**Root Shell**

~$ whoami
root

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 86

### **Exploit 3: CPU-side Privilege Escalation**

**GPU Status Queue Staging Buffer** Message Message

**Unprotected DMA Region**

**IOMMU Protected**

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 87

### **Exploit 3: CPU-side Privilege Escalation**

**GPU Status Queue**

Message

1st Entry elemCount = **16**

...

16th Entry

**Unsanitized**

**Unprotected DMA Region**

**Staging Buffer [16]**

Message

**IOMMU Protected**

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 88

### **Exploit 3: CPU-side Privilege Escalation**

**GPU Status Queue**

Message

1st Entry elemCount = **17**

...

16th Entry

**Unsanitized**

**Unprotected DMA Region**

**Staging Buffer [16]**

Message

**IOMMU Protected**

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 89

### **Exploit 3: CPU-side Privilege Escalation**

**GPU Status Queue**

Message

1st Entry elemCount = **17**

...

16th Entry

**Unsanitized**

**17th Entry**

**Unprotected DMA Region**

**Staging Buffer [16]**

Message

**IOMMU Protected**

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 90

### **Exploit 3: CPU-side Privilege Escalation**

**GPU Status Queue**

Message

1st Entry elemCount = **17**

...

16th Entry

**Unsanitized**

**17th Entry**

**Unprotected DMA Region**

**Staging Buffer [16]**

Message

**IOMMU Protected**

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 91

### **Exploit 3: CPU-side Privilege Escalation**

**GPU Status Queue**

Message

1st Entry elemCount = **17**

...

16th Entry

**Unsanitized**

**17th Entry**

**Unprotected DMA Region**

Staging Buffer **[16]**

**pMetadata**

**IOMMU Protected**

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 92

### **Exploit 3: CPU-side Privilege Escalation**

**GPU Status Queue**

Message

1st Entry elemCount = **17**

...

16th Entry

**Unsanitized**

**17th Entry**

**Unprotected DMA Region**

Writes to

`pReadOutgoing`

`rxReadPtr`

Staging Buffer **[16]**

**pMetadata**

**IOMMU Protected**

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 93

### **Exploit 3: CPU-side Privilege Escalation**

**GPU Status Queue**

Message

1st Entry elemCount = **17**

...

16th Entry

**Unsanitized**

**17th Entry**

**Unprotected DMA Region**

`_backendWrite32`

`&EUID`

`0(Root)`

`pReadOutgoing`

`rxReadPtr`

Staging Buffer **[16]**

**pMetadata**

**IOMMU Protected**

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 94

### **Takeaways**

**GPU Rowhammer is a real threat!**

- We went from random corruption to targeted attacks that take over GPUs.

**CPU-side Driver is not safe from a malicious GPU.**

- GPUBreach extended the exploit to the host, gaining powerful primitives

- Driver’s lack of sanitization on input from the GPU is the main culprit.

**Rethinking GPU Security Assumptions**

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 95

### **Takeaways**

CPU

**Sanitize GPU-Side Inputs in Driver**

PT Region

DATA

**Isolate GPU Page Tables from Data**

VRAM

ECC

**Error Correction Codes in GPU DRAM**

GDDR

**Principled RH Defense in GPU DRAM**

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

## Slide 96

### **Responsible Disclosure**

Responsibly disclosed to NVIDIA & Cloud Vendors

**GPUBreach has been reported to respective parties.**

- **Vendor:** NVIDIA. **CSPs:** Google, Microsoft, etc

- NVIDIA acknowledged the risks, while the CSPs are discussing mitigation approaches with their respective engineering teams.

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

Chris:

email: shaopenglin@cs.toronto.edu

personal site: https://shaopenglin.github.io

Yuqin:

email: me@yqyan.com

Guozhen:

email: gzh.ding@mail.utoronto.ca

personal site : https://www.guozhen.dev/

Chris S. Lin (shaopeng.lin@cs.toronto.edu) Yuqin Yan (me@yqyan.com) Guozhen Ding (gzh.ding@mail.utoronto.ca)

