---
title: "Make KSMA Great Again The Art of Rooting Android Devices by GPU MMU Features"
speakers: ["Yong Wang"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/Yong Wang_Make KSMA Great Again The Art of Rooting Android Devices by GPU MMU Features.pdf"
pages: 83
sha256: "ef2eb026aae3db1f5b8a761b9a2f8aa5f7f92fcf57093218455de8a0fa7375f7"
text_chars: 32421
ocr_pages: 8
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:26:31Z"
---
# Make KSMA Great Again The Art of Rooting Android Devices by GPU MMU Features

**Speakers:** Yong Wang  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Yong Wang_Make KSMA Great Again The Art of Rooting Android Devices by GPU MMU Features.pdf` (83 pages)

## Slide 1

Make KSMA Great Again: The Art of Rooting Android devices by GPU MMU features

WANG, YONG (@ThomasKing2014) Alibaba Cloud Pandora Lab

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
| pisekhat a
LSA 2025 oS
AUGUST 9-10, 2023
BRIEFINGS —
‘Make KSMA Great Again: The Art 5 Rooting Android.
| - devices by GPU MMU. features : |
WANG, YONG G (@Thomasking2024) _
- Alibaba Cloud Pandora Lab ee
```

## Slide 2

## Whoami

- WANG, YONG @ThomasKing2014@infosec.exchange

   - @ThomasKing2014 on Twitter/Weibo

- Security Engineer of Alibaba Cloud

- Focus on Android/Chrome vulnerability

- Speaker at BlackHat{ASIA/EU/USA}/HITBAMS/Zer0Con/POC/CanSecWest

- Nominated at Pwnie Award 2019(Best Privilege Escalation)

Alibaba Cloud Pandora Lab

## Slide 3

## Agenda

- Introduction

- GPU version of the KSMA exploitation technique

- Case study

- Conclusion

Alibaba Cloud Pandora Lab

## Slide 4

## Linux kernel VMM 101

• Process isolation is a set of different hardware and software technologies designed to protect each process from other processes on the operating system. – Wikipedia

- `cat /proc/<pid>/maps`

Alibaba Cloud Pandora Lab

## Slide 5

## Linux kernel VMM 101

#### struct mm_struct

#### struct vm_area_struct

Alibaba Cloud Pandora Lab

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Linux kernel VMM 101
struct mm_struct —
7cdc448000-7cdc5a6000 -—-p 00000000 00:00 2
7cdc5a6000-7cdc5a7000 -—-p 00000000 00:00 2
7cdc5a7000-7cdc5af000 rw-p 00000000 00:00 0 [anon:thread signal stack]
7cdc5af000-7cdc5b0000 rw-p 00000000 00:00 0 [anon:arc4random data]
7cdc5b@000-7cdc5b2000 rw-p 00000000 00:00 0 [anon:ReadFileToBuffer]
7cdc5b2000-7cdc5b3000 rw-p 00000000 00:00 0 [anon:arc4random data]
7cdc5b3000-7cdc5b5000 r—p 00000000 00:00 0 [war]
7cdc5b5000-7cdc5b6000 r-xp 00000000 00:00 2 [vdso]
7cdc5b6000-7cdc5ee000 r——p 00000000 07:60 16 /apex/com.android. runtime/bin/linker64
7cdc5ee000-7cdc6d8000 r-xp 00038000 07:62 16 /apex/com.android. runtime/bin/linker64
7cdc6d8000-7cdc6eQ000 r——p 00122000 07:62 16 /apex/com.android. runtime/bin/linker64
7cdc6e0000-7cdc6e2000 rw-p 00129000 07:60 16 /apex/com.android. runtime/bin/linker64
7cdc6e2000-7cdc6eb000 rw-p 00000000 00:00 0 [anon:.bss]
7cdc6eb000-7cdc6ec000 r—p 00000000 00:00 2 [anon:.bss]
7cdc6ec000-7cdc6eeQ00 rw-p 20000000 00:00 0 [anon:.bss]
7fed13d000-7fed13e000 -——-p 00000000 00:00 2
[7fed13e000-7fed93d000 Tw-p 00000000 00:00 0 [stack] ]
struct vm_area_struct
pisek hat
USA 2&0es3
Alibaba Cloud Pandora Lab
```

## Slide 6

## Linux kernel VMM 101

struct mm_struct {

struct vm_area_struct *mmap; struct rb_root mm_rb; …

/* list of VMAs */

unsigned long mmap_base; /* base of mmap area */ … pgd_t * pgd;

…

/* store ref to file /proc/<pid>/exe symlink points to */ struct file __rcu *exe_file;

Alibaba Cloud Pandora Lab

## Slide 7

## Linux kernel VMM 101

### struct vm_area_struct {

unsigned long vm_start; unsigned long vm_end; struct rb_node vm_rb; unsigned long vm_flags; const struct vm_operations_struct *vm_ops; unsigned long vm_pgoff; struct file * vm_file;

…

Alibaba Cloud Pandora Lab

## Slide 8

## Linux kernel VMM 101

Offset within  Offset within  Offset within  Offset within
Process PGD PMD Page Frame PTE Page Frame Data Frame
Page
pte_offset() pte_t
Frame
pmd_offset() pmd_t
pgd_offset() pgd_t
mm_struct->pgd

Alibaba Cloud Pandora Lab

## Slide 9

## Linux kernel VMM 101

- For Android

   - 4KB granule

   - 39-bit (512GB)

   - Three levels

- TTBRx

   - TTBR0 - user address

      - Up to 0x0000_007F_FFFF_FFFF

   - TTBR1 - kernel address

      - Start from 0xFFFF_FF80_0000_0000

Alibaba Cloud Pandora Lab

## Slide 10

## Kernel Space Mirroring Attack

### • ARMv8-64 level 0, level 1, and level 2 descriptor formats

Alibaba Cloud Pandora Lab

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Kernel Space Mirroring Attack
¢ ARMv8-64 level 0, level 1, and level 2 descriptor formats
63 10
Invalid IGNORED 0
52:51 48 47 12-11 10
nn-1
Block Tae block attributes [reso | Output address[47:n] RESO Lower block attribute attributes
With the 4KB granule size, for the level 1 descriptor n is 30, and for the level 2 descriptor, nis 21.
With the 16KB granule size, for the level 2 descriptor, n is 25.
With the 64KB granule size, for the level 2 descriptor, n is 29.
NSTable
APTable Stage 1 only,
XNTable RESO at stage 2
p- PXNTable
—
Table LIT I Ticsoreo [reso | Next-level table address[47:m]* IGNORED
With the 4KB granule size m is 12, with the 16KB granule size m is 14, and with the 64KB granule size, m is 16.
A level 0 Table descriptor returns the address of the level 1 table.
A level 1 Table descriptor returns the address of the level 2 table.
A level 2 Table descriptor returns the address of the level 3 table.
$ When m 2 12, bits [m:12] are RESO.
biSek hat
USA 2&0es3
Alibaba Cloud Pandora Lab
```

## Slide 11

## Kernel Space Mirroring Attack

### • ARMv8-64 level 3 descriptor format

Alibaba Cloud Pandora Lab

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Kernel Space Mirroring Attack
e ARMv8-64 level 3 descriptor format
Invalid| IGNORED 0
63 210
Reserved RESO [o[ 1]
Page, 4KB granule| a attributes [reso | Output address[47:12] Lower’ attributes s00
Page, 16KB granulte| Tel attributes | reso | Output address[47:14] L + | Lower’ attributes TH]
52 51 48 47 1615 1211
Page, 64KB granule| er attributes | reso | Output address[47:16] [reso | Lower’ attributes 300
t+ Upper page attributes and Lower page attributes
t Field is RESO
black hat Alibaba Cloud Pandora Lab
USA 2&0es3
```

## Slide 12

## Kernel Space Mirroring Attack

No level 0 table for Android

Alibaba Cloud Pandora Lab

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Kernel Space Mirroring Attack
Level 3 table
Level 2 table
Level 1 table
c tC“‘“CO;™OC;*”dS
D Block }»'CB |
nn aa
Level 0 table
D_Table is a Table descriptor
D_Block is a Block descriptor
D_Page is a Page descriptor
a Indexed by IA[n:39], where IA width is (n+1) bits
b Indexed by IA[38:30]
c Indexed by IA[29:21]
d Indexed by IA[20:12]
No level 0 table for Android
A
black hat Alibaba Cloud Pandora Lab
USA 2&0es3
```

## Slide 13

## Kernel Space Mirroring Attack

- Directly read/write the kernel virtual address

Alibaba Cloud Pandora Lab

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Kernel Space Mirroring Attack
Attribute fields for VMSAv8-64 stage 1 Block and Page descriptors
Upper attributes Lower attributes
eos [wom [TT (Itt TT]
Reserved for software use ——! nc 4
PXN SH[1:0]
Contiguous AP[2:1]
NS
Attrindx[2:0]
t UXN for the EL1&0 translation regime, XN for the other regimes.
Data access permissions for stage 1 of the EL1&0 translation regime
AP[2:1] Access fromEL1 Access from ELO
Read/write
Read/writ Read/write * Directly read/write the kernel
Read-only vi rt Ua | d d | ress
Read-only Read-only
A
black hat
Alibaba Cloud Pandora Lab
USA 2&0es3
```

## Slide 14

## Kernel Space Mirroring Attack

Level 1 table
Start of 1GB region
FFFFFFFFC0000000 0
FFFFFFC230002000
…
FFFFFFC240000000 0
R/W from EL0 & EL1, break kernel isolation
AP[2:1] = ‘01’
FFFFFFC200000000 D_Block
FFFFFFC1C0000000 0 PA: 30002000
FFFFFFC180000000 0
Physical memory
Text and Data Freed Pages Freed Pages
FFFFFFC140000000 0 (3GB)
...
FFFFFFC080000000 D_Table
FFFFFFC040000000 D_Table
FFFFFFC000000000 D_Table
R/W from EL1 D_Table is Table descriptor
… FFFFFFC030002000 D_Block is Block descriptor
FFFFFF8000000000 0

Alibaba Cloud Pandora Lab

## Slide 15

## Kernel Space Mirroring Attack

- Where to add a special block descriptor

   - swapper_pg_dir is the pgd for the kernel

- Kernel mirroring base

   - Entry address

      - (swapper_pg_dir + kernel_slide) + (Kernel_Mirroring_Base / 1GB) * 8

- Kaddr to Mirroring Kaddr

   - Mirroring_kaddr = Kernel_Mirroring_Base + (kaddr - PAGE_OFFSET)

Alibaba Cloud Pandora Lab

## Slide 16

## Kernel Space Mirroring Attack

- CVE-2017-0583 / CVE-2017-7533

   - https://i.blackhat.com/briefings/asia/2018/asia-18-WANG-KSMA-Breaking-Androidkernel-isolation-and-Rooting-with-ARM-MMU-features.pdf

- CVE-2020-3680

   - https://github.com/2freeman/Slides/blob/main/PoC-2020Three%20Dark%20clouds%20over%20the%20Android%20kernel.pdf

- CVE-2020-0423

   - https://www.longterm.io/cve-2020-0423.html

   - https://i.blackhat.com/USA21/Wednesday-Handouts/us-21-Typhoon-MangkhutOne-Click-Remote-Universal-Root-Formed-With-Two-Vulnerabilities.pdf

- CVE-2021-0399

   - https://conference.hitb.org/hitbsecconf2021sin/materials/D1T1%20%20%20The%20Art%20of%20Exploiting%20UAF%20by%20Ret2bpf%20in%20Androi d%20Kernel%20-%20Xingyu%20Jin%20&%20Richard%20Neal.pdf

Alibaba Cloud Pandora Lab

## Slide 17

## KSMA defence

https://github.com/2freeman/Slides/blob/main/PoC-2020-Three%20Dark%20clouds%20over%20the%20Android%20kernel.pdf

Alibaba Cloud Pandora Lab

## Slide 18

## Agenda

- Introduction

- _GPU version of the KSMA exploitation technique_

- Case study

- Conclusion

Alibaba Cloud Pandora Lab

## Slide 19

## GPU Memory Management

https://community.arm.com/arm-community-blogs/b/graphics-gaming-and-vr-blog/posts/memorymanagement-on-embedded-graphics-processors

Alibaba Cloud Pandora Lab

## Slide 20

## GPU Memory Management

- Features

   - Unified Memory Sharing

      - Same virtual address on both the CPU and GPU

   - Independent address spaces

   - …

Alibaba Cloud Pandora Lab

## Slide 21

## GPU Memory Management

- Features

   - Unified Memory Sharing

      - Same virtual address on both the CPU and GPU

   - Independent address spaces

   - …

- Virtual Memory Management

   - How to manage the virtual addresses?

   - How to manage the physical memory?

   - How the GPU MMU works?

Alibaba Cloud Pandora Lab

## Slide 22

## Virtual Address Management

struct kbase_va_region { struct rb_node rblink; struct list_head link; u64 start_pfn; // virtual address size_t nr_pages; size_t initial_commit; unsigned long flags; // {KBASE_REG_CPU_WR, KBASE_REG_FREE, …} struct kbase_mem_phy_alloc *cpu_alloc; struct kbase_mem_phy_alloc *gpu_alloc; struct list_head jit_node; u16 jit_usage_id; u8 jit_bin_id; int va_refcnt;

Alibaba Cloud Pandora Lab

## Slide 23

## Virtual Address Management

struct kbase_mem_phy_alloc { struct kref kref;

atomic_t gpu_mappings; atomic_t kernel_mappings; size_t nents; struct tagged_addr *pages; struct list_head mappings; struct list_head evict_node; size_t evicted; struct kbase_va_region *reg;

enum kbase_memory_type type; struct kbase_vmap_struct *permanent_map; u8 properties; u8 group_id;

union {umm, alias, native, user_buf} imported;

Alibaba Cloud Pandora Lab

## Slide 24

## Virtual Address Management

- struct kbase_reg_zone reg_zone[KBASE_REG_ZONE_MAX]; KBASE_REG_ZONE_CUSTOM_VA KBASE_REG_ZONE_SAME_VA KBASE_REG_ZONE_EXEC_VA

…

- kbase_context

kbase_ctx_reg_zone_init(kctx, KBASE_REG_ZONE_SAME_VA, same_va_base, same_va_pages);

kbase_ctx_reg_zone_init(kctx, KBASE_REG_ZONE_EXEC_VA, exec_va_base, KBASE_REG_ZONE_EXEC_VA_SIZE);

…

Alibaba Cloud Pandora Lab

## Slide 25

## Virtual Address Management

- BASE_MEM_SAME_VA

   - Same virtual address on both the CPU and GPU

   - Force SAME_VA if a 64-bit process

   - Allocate virtual address when mapping the kbase_va_region

   - Map a specific address on the GPU

- Non SAME_VA

   - Allocate virtual address and map it on the GPU immediately

   - Allocate virtual address on the CPU when mapping the kbase_va_region

Alibaba Cloud Pandora Lab

## Slide 26

## Physical Page Management

struct kbase_mem_pool { struct kbase_device *kbdev; size_t cur_size; size_t max_size; u8                  order;

struct kbase_mem_pool { struct kbase_mem_pool_group { struct kbase_device *kbdev; struct kbase_mem_pool small[16]; size_t cur_size; struct kbase_mem_pool large[16]; size_t max_size; }; u8                  order; u8                  group_id; int kbase_context_mem_pool_group_init(struct kbase_context spinlock_t pool_lock; *kctx) struct list_head page_list; { struct shrinker     reclaim; return kbase_mem_pool_group_init( &kctx->mem_pools, struct kbase_mem_pool *next_pool; kctx->kbdev, &kctx->kbdev->mem_pool_defaults, bool dying; &kctx->kbdev->mem_pools);

bool dying; bool dont_reclaim;

}

};

Alibaba Cloud Pandora Lab

## Slide 27

## Physical Page Management

- Allocate

   - Step 1: allocate from the kctx->mem_pools. If insufficient, goto step 2

   - Step 2: allocate from the kbdev->mem_pools. If insufficient, goto step 3

   - Step 3: allocate from the kernel

- Free

   - Step 1: add the pages to kctx->mem_pools. If full, goto step 2

   - Step 2: add the pages to kbdev->mem_pools. If full, goto step 3

   - Step 3: free the remaining pages to the kernel

Alibaba Cloud Pandora Lab

## Slide 28

## Physical Page Management

- Allocate

   - Step 1: allocate from the kctx->mem_pools. If insufficient, goto step 2

   - Step 2: allocate from the kbdev->mem_pools. If insufficient, goto step 3

   - Step 3: allocate from the kernel

- Free

   - Step 1: add the pages to kctx->mem_pools. If full, goto step 2

   - Step 2: add the pages to kbdev->mem_pools. If full, goto step 3

   - Step 3: free the remaining pages to the kernel

- Shrinker

   - register_shrinker(&kctx->reclaim);

   - register_shrinker(&pool->reclaim);

Alibaba Cloud Pandora Lab

## Slide 29

## Memory Management Unit

- No GPU Architecture Reference Manual

   - Learn from the kernel driver

   - Compare with CPU MMU

   - Blind test

Alibaba Cloud Pandora Lab

## Slide 30

## Memory Management Unit

- No GPU Architecture Reference Manual

   - Learn from the kernel driver

   - Compare with CPU MMU

   - Blind test

- kctx.mmu

struct kbase_mmu_table {

u64 *mmu_teardown_pages[MIDGARD_MMU_BOTTOMLEVEL]; struct mutex mmu_lock; phys_addr_t pgd; u8 group_id; struct kbase_context *kctx;

};

Alibaba Cloud Pandora Lab

## Slide 31

## Memory Management Unit

Alibaba Cloud Pandora Lab

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Memory Management Unit
bisa hat
USA 2023
Alibaba Cloud Pandora Lab
```

## Slide 32

Memory Management Unit
• ATE descriptor formats
63 1 0
Invalid 1 0
63 47 12 11 2 1 0
Block Output address Attributes 0 1
63 58 55 47 12 11 2 1 0
Table UNUSED Next-level table address Ignored 1 1
• PTE descriptor formats
63 47 12 11 2 1 0
Page Output address Attributes 1 1

Alibaba Cloud Pandora Lab

## Slide 33

## Memory Management Unit

63 54 10 9 8 7 6 4 2
NX ACCESS SHARE ACCESS_XX ATTR

- ATTR(4:2)

   - KBASE_REG_MEMATTR_VALUE(flags) << 2;

- ACCESS_XX(7:6)

   - KBASE_REG_GPU_WR -> ENTRY_ACCESS_RW

   - KBASE_REG_GPU_RD -> ENTRY_ACCESS_RO

- SHARE(9:8)

   - KBASE_REG_SHARE_BOTH -> SHARE_BOTH_BITS

- KBASE_REG_SHARE_IN -> SHARE_INNER_BITS

- • ACCESS(10)

   - ENTRY_ACCESS_BIT

- NX(54)

   - KBASE_REG_GPU_NX  -> ENTRY_NX_BIT

#define ENTRY_ATTR_BITS (7ULL << 2) #define ENTRY_ACCESS_RW (1ULL << 6) #define ENTRY_ACCESS_RO (3ULL << 6) #define ENTRY_SHARE_BITS (3ULL << 8) #define ENTRY_ACCESS_BIT (1ULL << 10) #define ENTRY_NX_BIT (1ULL << 54) enum kbase_share_attr_bits {

SHARE_BOTH_BITS = (2ULL << 8), SHARE_INNER_BITS = (3ULL << 8)

~~};~~

Alibaba Cloud Pandora Lab

## Slide 34

## Memory Management Unit

D_Block
D_Page
D_Block
d
D_Block
D_Table
c
D_Table
b a indexed by VA[47:39]
D_Table
b indexed by VA[38:30]
a
c indexed by VA[29:21]
PGD
d indexed by VA[20:12]

Alibaba Cloud Pandora Lab

## Slide 35

## Memory Management Unit

D_Block
D_Page
D_Block
d
D_Block
D_Table
c
D_Table
b
D_Table
a
PGD
D_Block has never been used in the driver code

Alibaba Cloud Pandora Lab

## Slide 36

## Memory Management Unit

- MMU entries can be dumped

   - Leak the physical page frames(including zero page)

   - Fixed and guarded by non-default config

Alibaba Cloud Pandora Lab

## Slide 37

## Memory Management Unit

- Cache maintenance

   - Cache line is made of 64 bytes (8 page table entries)

   - MMU lock region is a self-aligned region whose size is a power of 2

- Example: va=0x4F000 num_pages=2

   - Address range between 0x4F000 and 0x50FFF

   - 0x4F000 falls into the [0x48000, 0x4FFFF]

   - 0x50000 falls into the [0x50000, 0x57FFF]

   - [0x40000, 0x5FFFF]

Alibaba Cloud Pandora Lab

## Slide 38

## Memory Management Unit

- Cache maintenance

   - Cache line is made of 64 bytes (8 page table entries)

   - MMU lock region is a self-aligned region whose size is a power of 2

   - Align to 2MB boundaries

Alibaba Cloud Pandora Lab

## Slide 39

## Block descriptor

- One of the key steps of KSMA is crafting a valid block entry

   - Figure out whether the GPU MMU supports block descriptor or not

   - Which level? (L2-2MB, L1-1GB, L0-512GB)

- kbase_mmu_dump_mmap

- “-” denotes Invalid descriptor

- “*” denotes Page descriptor

Alibaba Cloud Pandora Lab

## Slide 40

## Block descriptor

- Add a block descriptor to L2

   - ENTRY_NX_BIT | (PA_aligned & 0xfffffffff000LL) |ENTRY_ACCESS_BIT | ENTRY_ACCESS_RW | 0x01

Alibaba Cloud Pandora Lab

## Slide 41

## Block descriptor

- Add a block descriptor to L2

   - ENTRY_NX_BIT | (PA_aligned & 0xfffffffff000LL) |ENTRY_ACCESS_BIT | ENTRY_ACCESS_RW | 0x01

   - Leak the PGD of L2

   - Write this descriptor to the associated physical page

Alibaba Cloud Pandora Lab

## Slide 42

## Block descriptor

- No kbase_va_region and kbase_mem_phy_alloc is associated with this descriptor

   - determined by the GPU whether this descriptor is valid or not

Alibaba Cloud Pandora Lab

## Slide 43

## GPU READ/WRITE

- Require reverse-engineering the GPU instruction sets

   - https://gitlab.freedesktop.org/panfrost

   - https://github.blog/2022-07-27-corrupting-memory-without-memorycorruption/

Alibaba Cloud Pandora Lab

## Slide 44

## GPU READ/WRITE

- Require reverse-engineering the GPU instruction sets

   - https://gitlab.freedesktop.org/panfrost

   - https://github.blog/2022-07-27-corrupting-memory-without-memorycorruption/

- New features and enhancements

Alibaba Cloud Pandora Lab

## Slide 45

## GPU READ/WRITE

- OpenCL(Open Computing Language)

   - A framework for writing programs that execute across heterogeneous platforms consisting of central processing units (CPUs), graphics processing units (GPUs), digital signal processors (DSPs), field-programmable gate arrays (FPGAs) and other processors or hardware accelerators

   - Provides a standard interface for parallel computing using task- and databased parallelism

   - Specifies programming languages (based on C99, C++14 and C++17) for programming abovementioned devices

Alibaba Cloud Pandora Lab

## Slide 46

## GPU READ/WRITE

const char* gpu_code =

"__kernel void rw_mem(__global unsigned long *p0, __global unsigned long *p1, __global unsigned long *p2) {”  // p0 – dest, p1 – src, p2 – rw_flag "   size_t idx = get_global_id(0);"

"   if (p2[idx]) {” // write

"       __global unsigned long *addr = (__global unsigned long)(p0[idx]);" "       addr[0] = p1[idx];"

"   } else {” // read

"       __global unsigned long *addr = (__global unsigned long *)(p1[idx]);" "       p0[idx] = addr[0];"

"   }" "}";

Alibaba Cloud Pandora Lab

## Slide 47

## GPU READ/WRITE

- How to use the OpenCL

   - Find all the needed functions(clCreateBuffer/clSetKernelArg,etc.) from libOpenCL.so

   - Create the GPU buffer for P0-P2 (clCreateBuffer)

   - Set the parameters of kernel function - rw_mem (clSetKernelArg)

   - Kick off the GPU work (clEnqueueNDRangeKernel)

   - Read the result (clEnqueueReadBuffer)

- For a valid kbase_va_region, it works well

Alibaba Cloud Pandora Lab

## Slide 48

## GPU READ/WRITE

### • clEnqueueReadBuffer always fails

No kbase_va_region and kbase_mem_phy_alloc is associated with the block descriptor.

Alibaba Cloud Pandora Lab

## Slide 49

## GPU READ/WRITE

- MMU cache flush

   - Insert/teardown pages can flush the MMU cache

   - The block descriptor is invisible from CPU side

Alibaba Cloud Pandora Lab

## Slide 50

## GPU READ/WRITE

- MMU cache flush

Fake VA start

- Insert/teardown pages can flush the MMU cache

- The block descriptor is invisible from CPU side

(2^(n-1) - 1) * 2MB

Valid VA start

- Side-channel cache flush

   - Valid GPU VA start: (2^(n-1) + 1) * 2MB

(2^(n-1) + 1) * 2MB

- Fake GPU VA start: (2^(n-1) - 1) * 2MB

- MMU lock region: (2^n) * 2MB

~~<u>GPU virtual address</u>~~

Alibaba Cloud Pandora Lab

## Slide 51

## Side-channel cache flush example

0x5ec0000000

- Valid GPU VA

   - [0x5ec0c00000, 0x5ec2000000)

- Fake GPU VA

   - [0x5ec0000000, 0x5ec0c00000) 0x5ec0c00000

0x5ec2000000

6M

10M

~~GPU virtual address~~

Alibaba Cloud Pandora Lab

## Slide 52

## Side-channel cache flush example

- Valid GPU VA

0x5ec0000000

   - [0x5ec0c00000, 0x5ec2000000)

- Fake GPU VA

6M

- [0x5ec0000000, 0x5ec0c00000)

0x5ec0c00000

- Commit or shrink the valid VA • Lock region [0x5ec0000000, 0x5ec2000000)

10M

0x5ec2000000

~~GPU virtual address~~

Alibaba Cloud Pandora Lab

## Slide 53

## GPU READ/WRITE

- Is it possible to add the L1 or L0 block descriptor?

   - Absolutely yes

- Problems

   - Shaping the GPU VA layout may be more complex

   - Using too many physical pages can trigger the Out of Memory

Alibaba Cloud Pandora Lab

## Slide 54

## GPU version of KSMA

- Shape the GPU VA layout

   - Spray the GPU VAs without pages

- Full physical memory access • 1. Add 31 block descriptors • 2. Commit/shrink the valid VA • 3. Read/write the fake VA • 4. GOTO Step 1

Fake VA

Valid VA

62M
MMU lock
region
66M

Alibaba Cloud Pandora Lab

## Slide 55

## Agenda

- Introduction

- GPU version of the KSMA exploitation technique

- _Case study_

- Conclusion

Alibaba Cloud Pandora Lab

## Slide 56

## Vulnerability analysis

- New features and enhancements

   - New code

   - MTK dimensity 9000 /  Google tensor GS201(Pixel 7)

Alibaba Cloud Pandora Lab

## Slide 57

## Vulnerability analysis

• KBASE_IOCTL_CS_QUEUE_REGISTER

queue_addr = reg->buffer_gpu_addr; queue_size = reg->buffer_size >> PAGE_SHIFT; /* Check if queue is already registered */ if (find_queue(kctx, queue_addr) != NULL) { ret = -EINVAL; goto out;

}

region = kbase_region_tracker_find_region_enclosing_address(kctx, queue_addr);

region->flags |= KBASE_REG_NO_USER_FREE;

Alibaba Cloud Pandora Lab

## Slide 58

## Vulnerability analysis

- KBASE_IOCTL_CS_QUEUE_TERMINATE

queue = find_queue(kctx, term->buffer_gpu_addr); if (queue) {

unbind_queue(kctx, queue); if (!WARN_ON(!queue->queue_reg)) {

/* After this the Userspace would be able to free the

- memory for GPU queue. In case the Userspace missed

- terminating the queue, the cleanup will happen on

- context termination where tear down of region tracker

- would free up the GPU queue memory.

*/

queue->queue_reg->flags &= ~KBASE_REG_NO_USER_FREE;

Alibaba Cloud Pandora Lab

## Slide 59

## Vulnerability analysis

int kbase_mem_free_region(struct kbase_context *kctx, struct kbase_va_region *reg) { int err;

KBASE_DEBUG_ASSERT(kctx != NULL); KBASE_DEBUG_ASSERT(reg != NULL); dev_dbg(kctx->kbdev->dev, "%s %pK in kctx %pK\n", __func__, (void *)reg, (void *)kctx); lockdep_assert_held(&kctx->reg_lock); if (reg->flags & KBASE_REG_NO_USER_FREE) {

forbidden!\n");

dev_warn(kctx->kbdev->dev, "Attempt to free GPU memory whose freeing by user space is return -EINVAL;

}

Alibaba Cloud Pandora Lab

## Slide 60

## Vulnerability analysis

- Unconditionally clear the KBASE_REG_NO_USER_FREE flag

   - KBASE_IOCTL_CS_QUEUE_REGISTER

   - KBASE_IOCTL_CS_QUEUE_TERMINATE

Alibaba Cloud Pandora Lab

## Slide 61

## Vulnerability analysis

- Unconditionally clear the KBASE_REG_NO_USER_FREE flag

   - KBASE_IOCTL_CS_QUEUE_REGISTER

   - KBASE_IOCTL_CS_QUEUE_TERMINATE

- Impact

   - A region with KBASE_REG_NO_USER_FREE can be freed by user space

   - • A region with KBASE_REG_NO_USER_FREE can be aliased(KBASE_IOCTL_MEM_ALIAS)

Alibaba Cloud Pandora Lab

## Slide 62

## Vulnerability analysis

- JIT region can be aliased

BASE_MEM_PROT_CPU_RD | BASE_MEM_PROT_GPU_RD | BASE_MEM_PROT_GPU_WR | BASE_MEM_GROW_ON_GPF | BASE_MEM_COHERENT_LOCAL | BASEP_MEM_NO_USER_FREE;

GPU VA

Alias region JIT region
Physical pages

Alibaba Cloud Pandora Lab

## Slide 63

## Vulnerability analysis

- JIT region can be freed via BASE_KCPU_COMMAND_TYPE_JIT_FREE

   - The associated physical pages can be reclaimed

GPU VA Alias region JIT region
Physical pages

Alibaba Cloud Pandora Lab

## Slide 64

## Vulnerability analysis

void kbase_jit_free(struct kbase_context *kctx, struct kbase_va_region *reg) { old_pages = kbase_reg_current_backed_size(reg); if (reg->initial_commit < old_pages) { u64 new_size = MAX(reg->initial_commit, div_u64(old_pages * (100 - kctx->trim_level), 100)); u64 delta = old_pages - new_size; if (delta) { mutex_lock(&kctx->reg_lock); kbase_mem_shrink(kctx, reg, old_pages - delta); mutex_unlock(&kctx->reg_lock); }

- Tear down the entries of CPU MMU

- Insert the region into the evict_list

- Partially shrink the memory when initial_commit is less than old_pages

kbase_mem_shrink_cpu_mapping(kctx, reg, 0, reg->gpu_alloc->nents); list_add(&reg->gpu_alloc->evict_node, &kctx->evict_list); list_move(&reg->jit_node, &kctx->jit_pool_head);

Alibaba Cloud Pandora Lab

## Slide 65

## Vulnerability analysis

// register_shrinker(&kctx->reclaim);

unsigned long kbase_mem_evictable_reclaim_scan_objects(struct shrinker *s, struct shrink_control *sc)

- Tear down the entries of GPU MMU

// …

list_for_each_entry_safe(alloc, tmp, &kctx->evict_list, evict_node) { err = kbase_mem_shrink_gpu_mapping(kctx, alloc>reg, 0, alloc->nents);

err = kbase_mem_shrink_gpu_mapping(kctx, alloc-

- Free the physical pages

kbase_free_phy_pages_helper(alloc, alloc->evicted); // ...

Alibaba Cloud Pandora Lab

## Slide 66

## Vulnerability analysis

// register_shrinker(&kctx->reclaim);

unsigned long kbase_mem_evictable_reclaim_scan_objects(struct shrinker *s, struct shrink_control *sc)

- Tear down the entries of GPU MMU

// …

list_for_each_entry_safe(alloc, tmp, &kctx->evict_list, evict_node) { err = kbase_mem_shrink_gpu_mapping(kctx, alloc>reg, 0, alloc->nents);

err = kbase_mem_shrink_gpu_mapping(kctx, alloc-

kbase_free_phy_pages_helper(alloc, alloc->evicted); // ...

- Free the physical pages

- It requires finding a method to trigger the callback function

Alibaba Cloud Pandora Lab

## Slide 67

## Vulnerability analysis

- reg->initial_commit

   - reg->initial_commit = jit_alloc_info.commit_pages

- old_pages = kbase_reg_current_backed_size(reg);

   - reg->cpu_alloc->nents;

Alibaba Cloud Pandora Lab

## Slide 68

## Vulnerability analysis

- reg->initial_commit

   - reg->initial_commit = jit_alloc_info.commit_pages

- old_pages = kbase_reg_current_backed_size(reg);

   - reg->cpu_alloc->nents;

- BASE_KCPU_COMMAND_TYPE_JIT_ALLOC

   - jit_alloc_info.va_pages = 1;

   - jit_alloc_info.commit_pages = 0;

   - reg->initial_commit = 0;

   - old_pages = 0;

Alibaba Cloud Pandora Lab

## Slide 69

## Vulnerability analysis

• JIT region

BASE_MEM_PROT_CPU_RD | BASE_MEM_PROT_GPU_RD | BASE_MEM_PROT_GPU_WR | BASE_MEM_GROW_ON_GPF | BASE_MEM_COHERENT_LOCAL | BASEP_MEM_NO_USER_FREE;

Alibaba Cloud Pandora Lab

## Slide 70

## Vulnerability analysis

- JIT region

BASE_MEM_PROT_CPU_RD | BASE_MEM_PROT_GPU_RD | BASE_MEM_PROT_GPU_WR | BASE_MEM_GROW_ON_GPF | BASE_MEM_COHERENT_LOCAL | BASEP_MEM_NO_USER_FREE;

- Page fault

   - Read or write the JIT region via OpenCL kernel function

   - reg->initial_commit = 0;

   - old_pages = 1;

Alibaba Cloud Pandora Lab

## Slide 71

## Vulnerability analysis

void kbase_jit_free(struct kbase_context *kctx, struct kbase_va_region *reg) {

- trim_level is 0

   - new_size = old_pages

old_pages = kbase_reg_current_backed_size(reg); • delta is 0 if (reg->initial_commit < old_pages) { u64 new_size = MAX(reg->initial_commit, div_u64(old_pages * (100 - kctx->trim_level), 100)); • trim_level is 100 u64 delta = old_pages - new_size; • if (delta) { • delta is 1 mutex_lock(&kctx->reg_lock); kbase_mem_shrink(kctx, reg, old_pages - delta); mutex_unlock(&kctx->reg_lock);

- new_size = reg->initial_commit;

- • delta is 1

}

kbase_mem_shrink_cpu_mapping(kctx, reg, 0, reg->gpu_alloc->nents); list_add(&reg->gpu_alloc->evict_node, &kctx->evict_list); list_move(&reg->jit_node, &kctx->jit_pool_head);

Alibaba Cloud Pandora Lab

## Slide 72

## Vulnerability analysis

void kbase_jit_free(struct kbase_context *kctx, struct kbase_va_region *reg) {

old_pages = kbase_reg_current_backed_size(reg); if (reg->initial_commit < old_pages) {

- trim_level is 0

   - new_size = old_pages

   - delta is 0

}

u64 new_size = MAX(reg->initial_commit, div_u64(old_pages * (100 - kctx->trim_level), 100)); • trim_level is 100 u64 delta = old_pages - new_size; • if (delta) { • delta is 1 mutex_lock(&kctx->reg_lock); kbase_mem_shrink(kctx, reg, old_pages - delta); • kctx->trim_level = trim_level; mutex_unlock(&kctx->reg_lock);

   - new_size = reg->initial_commit;

- kctx->trim_level = trim_level;

   - KBASE_IOCTL_MEM_JIT_INIT

   - Always free the physical pages

kbase_mem_shrink_cpu_mapping(kctx, reg, 0, reg->gpu_alloc->nents); list_add(&reg->gpu_alloc->evict_node, &kctx->evict_list); list_move(&reg->jit_node, &kctx->jit_pool_head);

Alibaba Cloud Pandora Lab

## Slide 73

## Fix

• https://android.googlesource.com/kernel/google-modules/gpu/+/422aa1fad7e63f16000ffb9303e816b54ef3d8ca%5E%21/#F0

Alibaba Cloud Pandora Lab

## Slide 74

## Exploit analysis

- Allocate

   - Step 1: allocate from the kctx->mem_pools. If insufficient, goto step 2

   - Step 2: allocate from the kbdev->mem_pools. If insufficient, goto step 3

   - Step 3: allocate from the kernel

- Free

   - Step 1: add the pages to kctx->mem_pools. If full, goto step 2

   - Step 2: add the pages to kbdev->mem_pools. If full, goto step 3

   - Step 3: free the remaining pages to the kernel

- Shrinker

   - register_shrinker(&kctx->reclaim);

   - register_shrinker(&pool->reclaim);

Alibaba Cloud Pandora Lab

## Slide 75

## Exploit analysis

- kbase_mmu_insert_pages_no_flush

   - If invalid, allocate one page as the PGD

   - Allocate from kbdev->mem_pools, not from kctx->mem_pools

Alibaba Cloud Pandora Lab

## Slide 76

## Exploit analysis

- kbase_mmu_insert_pages_no_flush

   - If invalid, allocate one page as the PGD

   - Allocate from kbdev->mem_pools, not from kctx->mem_pools

   - It’s possible to reuse the freed pages as the PGD

Alibaba Cloud Pandora Lab

## Slide 77

## Exploit analysis

- Put it together

   - Initialize the kctx with trim_level = 100

   - Allocate the dummy region with (SZ_64M >> PAGE_SHIFT) pages

      - #define KBASE_MEM_POOL_MAX_SIZE_KCTX  (SZ_64M >> PAGE_SHIFT)

   - Allocate a JIT region(VA_SIZE=1, nents=0)

   - Write a value to JIT region and trigger the page fault (VA_SIZE=1, nents=1)

   - Clear the KBASE_REG_NO_USER_FREE flag of the JIT region

   - Create an alias region of the JIT region

   - Free the dummy region

      - kctx->mem_pools is full

   - Shape the VA layout and allocate a candidate region with no page

      - Spray the VA with no page

   - Free the JIT region

      - Pages will be add to kbdev->mem_pools

   - Commit the pages to the candidate region

      - Allocate some pages for PGDs

   - Read or write the specific PGD page via the alias region

      - BASE_MEM_PROT_GPU_RD | BASE_MEM_PROT_GPU_WR | BASE_MEM_PROT_CPU_RD

   - Apply the KSMA exploit technique and access the full memory

Alibaba Cloud Pandora Lab

## Slide 78

## Exploit analysis

- Devices without any protection for kernel code/data area

   - Patch the kernel code

- Find a target process and patch the cred pointer

   - GPU accelerate the search!

Alibaba Cloud Pandora Lab

## Slide 79

## demo

Alibaba Cloud Pandora Lab

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
~" Permissions, account activity, personal data
Location
9 Off
* Safety & emergency
Emergency SOS, medical info, alerts
a Passwords & accounts
Saved passwords, autofill, synced accounts
Digital Wellbeing & parental
& controls
Screen time, app timers, bedtime schedules
G Googie
Services & preferences
Languages, gestures, time, backup
tp About phone
Pixel 7
® Tips & support
Help articles, phone & chat
```

## Slide 80

## Agenda

- Introduction

- GPU version of the KSMA exploitation technique

- Case study

- _Conclusion_

Alibaba Cloud Pandora Lab

## Slide 81

## Black Hat sound bytes

- The GPU memory management has been fully discussed.

- The GPU version of the KSMA exploitation technique has been detailed. The bug as case study has been fully discussed.

- • With more and more both hardware and software mitigations, Android rooting needs better bug and more advanced exploitation technique.

Alibaba Cloud Pandora Lab

## Slide 82

## References

[1] https://i.blackhat.com/briefings/asia/2018/asia-18-WANG-KSMA-Breaking-Android-kernel-isolation-andRooting-with-ARM-MMU-features.pdf

[2] https://github.com/2freeman/Slides/blob/main/PoC-2020Three%20Dark%20clouds%20over%20the%20Android%20kernel.pdf

[3] https://www.longterm.io/cve-2020-0423.html

[4] https://i.blackhat.com/USA21/Wednesday-Handouts/us-21-Typhoon-Mangkhut-One-Click-RemoteUniversal-Root-Formed-With-Two-Vulnerabilities.pdf

[5] https://conference.hitb.org/hitbsecconf2021sin/materials/D1T1%20%20%20The%20Art%20of%20Exploiting%20UAF%20by%20Ret2bpf%20in%20Android%20Kernel%20%20Xingyu%20Jin%20&%20Richard%20Neal.pdf

[6] https://community.arm.com/arm-community-blogs/b/graphics-gaming-and-vr-blog/posts/memorymanagement-on-embedded-graphics-processors

[7] https://community.arm.com/arm-community-blogs/b/graphics-gaming-and-vr-blog/posts/new-suite-ofarm-mali-gpus

[8] https://en.wikipedia.org/wiki/OpenCL

[9] https://gitlab.freedesktop.org/panfrost

[10]https://github.blog/2022-07-27-corrupting-memory-without-memory-corruption

[11] https://www.blackhat.com/asia-23/briefings/schedule/index.html#two-bugs-with-one-poc-rooting-pixel-- <u>from-android--to-android--30148</u>

Alibaba Cloud Pandora Lab

## Slide 83

# Thank you!

WANG, YONG (@ThomasKing2014) ThomasKingNew@gmail.com
