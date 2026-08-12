---
title: "Two bugs with one PoC Rooting Pixel 6 from Android 12 to Android 13"
speakers: ["WANG"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2023"
edition: "ASIA"
year: 2023
source_pdf: "Black Hat Asia 2023 slides/AS-23-WANG-Two-bugs-with-one-PoC-Rooting-Pixel-6-from-Android-12-to-Android-13.pdf"
pages: 65
sha256: "f111708442932b599b3be5576aed5da426757545af4c3405aeb2de526d359ee6"
text_chars: 36174
ocr_pages: 22
has_ocr: true
redacted_secrets: 0
ocr_confidence: 87.4
ocr_unreliable_blocks: 0
vision_verified_blocks: 1
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T03:50:30Z"
---
# Two bugs with one PoC Rooting Pixel 6 from Android 12 to Android 13

**Speakers:** WANG  
**Conference:** Black Hat ASIA 2023  
**Source:** `Black Hat Asia 2023 slides/AS-23-WANG-Two-bugs-with-one-PoC-Rooting-Pixel-6-from-Android-12-to-Android-13.pdf` (65 pages)


## Slide 1

Two bugs with one PoC: Roo2ng Pixel 6 from Android 12 to Android 13

WANG, YONG (@ThomasKing2014)

## Slide 2

## Whoami

- WANG, YONG @ThomasKing2014@infosec.exchange

   - @ThomasKing2014 on Twitter/Weibo

- Security Engineer of Alibaba Group

- Focus on Android/Chrome vulnerability

- BlackHat{ASIA/EU/USA}/HITBAMS/Zer0Con/POC/CanSecWest

- Nominated at Pwnie Award 2019(Best Privilege Escalation)

## Slide 3

## Agenda

- Introduction

- Bug #1

- Bug #2

- Conclusion

## Slide 4

## Android kernel mitigations 101

- Android 12/13 – kernel 5.10(5.15)

   - PXN - Privileged eXecute Never

   - PAN - Privileged Access Never

   - UAO - User Access Override

   - PAC - Pointer Authentication Code

   - MTE - Memory Tagging Extension

   - KASLR - Kernel Address Space Layout Randomization

   - CONFIG_DEBUG_LIST

   - CONFIG_SLAB_FREELIST_RANDOM/HARDENED

   - # CONFIG_SLAB_MERGE_DEFAULT is not set

   - CONFIG_BPF_JIT_ALWAYS_ON

## Slide 5

## User Access Override

- Without UAO, corrupting addr_limit of thread_info is the only step to gain AARW

   - AAR: write(pipefd[1], kbuf, count);/read(pipefd[0], ubuf, count);

   - AAW: write(pipefd[1], ubuf, count);/read(pipefd[0], kbuf, count);

## Slide 6

## User Access Override

• Without UAO, corrup_ng addr_limit of thread_info is the only step to gain AARW

   - AAR: write(pipefd[1], kbuf, count);/read(pipefd[0], ubuf, count);

   - AAW: write(pipefd[1], ubuf, count);/read(pipefd[0], kbuf, count);

- UAO state

   - KERNEL_DS(-1), enabled

   - Other, disabled

## Slide 7

CONFIG_DEBUG_LIST

## Slide 8

## CONFIG_SLAB_FREELIST_RANDOM

Without randomiza.on
With randomization

0 1 2 3
2 0 1 3

## Slide 9

CONFIG_SLAB_FREELIST_HARDENED

## Slide 10

## # CONFIG_SLAB_MERGE_DEFAULT is not set

https://i.blackhat.com/USA-22/Thursday/US-22-WANG-Ret2page-The-Art-of-Exploiting-Use-After-Free-Vulnerabilities-in-the-Dedicated-Cache.pdf

## Slide 11

## CONFIG_BPF_JIT_ALWAYS_ON

https://googleprojectzero.blogspot.com/2020/12/an-ios-hacker-tries-android.html


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CONFIG BPF JIT ALWAYS ON
The ultimate ROP
Finally, it's time to consider our ROP payload. Because we can write at most 15 distinct 64-bit values into the
stack via our overflow (2 of which we've already used), we'll need to be careful about keeping the ROP
payload small.
When | mentioned this progress to Jann, he suggested that | check the function — bpf prog run(),
which he described as the ultimate ROP gadget. And indeed, if your kernel has it compiled in, it does appear
to be the ultimate ROP gadget!
___bpf_prog_run() is responsible for interpreting eBPF bytecode that has already been deemed safe by
the eBPF verifier. As such, it provides a number very powerful primitives, including:
1. arbitrary control flow in the eBPF program;
2. arbitrary memory load;
3. arbitrary memory store;
4. arbitrary kernel function calls with up to 5 arguments and a 64-bit return value.
```

## Slide 12

## Google Tensor

<u>https://en.wikipedia.org/wiki/Google_Tensor</u>


> Recovered by OCR — confidence 89/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Google Tensor
Connectivity
Model number
Codename
Manufacturer
Fabrication
ISA
Bit width
Security
Bus width
Bandwidth
NPU
Storage type
Modem
Wireless
Navigation
First-generation (2021)
2.8 GHz Cortex-X1 (2x)
2.25 GHz Cortex-A76 (2x)
1.8 GHz Cortex-A55 (4x)
TrustZone (Trusty OS)
848 MHz/26]
Exynos 5123/26]
Wi-Fi 6 and Wi-Fi 6E!>
Bluetooth 5.21941[85]
Second-generation (2022)
2.85 GHz Cortex-X1 (2x)
2.35 GHz Cortex-A78 (2x)
1.8 GHz Cortex-A55 (4x)
TrustZone (Trusty OS)!8°!
UFS 3.115!
Wi-Fi 6 1
Dual-band GNSs!
```

## Slide 13

## Android LPE aKack surfaces

- DAC

   - ptmx (root root 0o666) ptmx_device

   - tty (root root 0o666) owntty_device

   - system (system system 0o664) dmabuf_system_heap_device

   - ashmem (root root 0o666) ashmem_device

   - binder(root root 0o777) binder_device

   - kgsl-3d0 (system system 0o666) gpu_device / mali0 (system system 0o664) gpu_device

#### • SELinux policy

- ALLOW domain-->ptmx_device (chr_file) [map append write ioctl watch_reads getattr read watch lock open]

- • ALLOW domain-->owntty_device (chr_file) [map append write ioctl watch_reads getattr read watch lock open]

- ALLOW domain-->ashmem_device (chr_file) [map append write ioctl getattr read lock]

- ALLOW untrusted_app-->dmabuf_system_heap_device (chr_file) [map ioctl watch_reads getattr read watch lock open]

- ALLOW untrusted_app-->binder_device (chr_file) [map ioctl watch_reads getattr read watch lock open]

- ALLOW untrusted_app-->gpu_device (chr_file) [map ioctl watch_reads getattr read watch lock open]

## Slide 14

## Motivation

- Why gpu_device?

   - Not ubiquitous

   - Complicated

   - Bugs reported

## Slide 15

## Motivation

- Why gpu_device?

   - Not ubiquitous

   - Complicated

   - Bugs reported

   - Exploitable bugs in the wild


> Recovered by OCR — confidence 89/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Motivation
¢ Why gpu_device?
¢ Not ubiquitous
¢ Complicated
¢ Bugs reported
¢ Exploitable bugs in the wild
Android has updated the May security with notes that 4 vulns were
exploited in-the-wild.
Qualcomm GPU: CVE-2021-1905, CVE-2021-1906
ARM Mali GPU: CVE-2021-28663, CVE-2021-28664
```

## Slide 16

## Agenda

- Introduc_on

- _Bug #1_

- Bug #2

- Conclusion

## Slide 17

## CVE-2021-28664 analysis

https://developer.arm.com/Arm%20Security%20Center/Mali%20GPU%20Driver%20Vulnerabilities


> Recovered by OCR — confidence 93/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CVE-2021-28664 analysis
Title Mali GPU Kernel Driver elevates CPU RO pages to writable
CVE CVE-2021-28664
Date of issue 18th March 2021
e Midgard GPU Kernel Driver: All versions from r8p0 - r30p0
Affects ¢ Bifrost GPU Kernel Driver: All versions from rOpO - r29p0
¢ Valhall GPU Kernel Driver: All versions from r19p0 - r29p0
Impact Anon-privileged user can get a write access to read-only memory, and may be able to gain root privilege, corrupt memory and modify the memory of other processes.
Resolution This issue is fixed in Bifrost and Valhall GPU Kernel Driver r30p0 and in Midgard GPU Kernel Driver r31p0 release. Users are recommended to upgrade if they are impacted by this issue.
Credit n/a
```

## Slide 18

## CVE-2021-28664 analysis

### • kbase_mem_from_user_buffer diff(Bifrost r28 vs r29)

• Only GPU_WR permission check

- CPU_WR instead of GPU_WR

## Slide 19

## CVE-2021-28664 analysis

### • kbase_mem_from_user_buffer diff(Bifrost r29 vs r30)

• Check both CPU_WR and GPU_WR


> Recovered by OCR — confidence 87/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CVE-2021-28664 analysis
¢ kbase_mem_from_user_buffer diff(Bifrost r29 vs r30)
#if KERNEL_VERSION(4, 6, 0) > LINUX_VERSION_CODE #if KERNEL_VERSION(4, 6, 0) > LINUX_VERSION_CODE
faulted_pages = get_user_pages(current, current->mm, address, *va_pages, faulted_pages = get_user_pages(current, current->mm, address, *va_pages,
#if KERNEL_VERSION(4, 4, ) <= LINUX_VERSION_CODE && \ #if KERNEL_VERSION(4, ) LINUX_VERSION_CODE && \
KERNEL_VERSION(4, 5, ©) > LINUX_VERSION_CODE KERNEL_VERSION(4, 5, 0) > LINUX_VERSION_CODE
reg->flags & KBASE_R CPU ? FOLL_WRITE ‘
pages, NULL); t pages, NULL);
#else #else
gs & 3A G_CPU_WR, ®, pages, NULL); < » 0, pages, NULL);
#endif #endif
#elif KERNEL_VERSION(4, 9, 9) > LINUX_VERSION_CODE #elif KERNEL_VERSION(4, 9, 0) > LINUX_VERSION_CODE
faulted_pages = get_user_pages(address, *va_pages, faulted_pages = get_user_pages(address, *va_pages,
g->fl & KBASE_REG_CPU_LWR, 0, pages, NULL); é , ®, pages, NULL);
#else #else
faulted_pages get_user_pages(address, *va_pages, faulted_pages = get_user_pages(address, *va_pages,
reg 5E_RE J RITE
pages, NULL) ; F RITE pages, NULL);
#endif #endif
¢ Check both CPU_WR and GPU_WR
```

## Slide 20

## CVE-2021-28664 PoC

• KBASE_IOCTL_MEM_IMPORT imported_ubuf.ptr = (u64)ro_page; // Read-only memory imported_ubuf.length = ro_len; mem_import.in.flags = BASE_MEM_PROT_CPU_RD | BASE_MEM_PROT_CPU_WR | BASE_MEM_PROT_GPU_RD; mem_import.in.phandle = (__u64)&imported_ubuf; mem_import.in.type = BASE_MEM_IMPORT_TYPE_USER_BUFFER; mem_import.in.padding = 0; mem_import.in.header_page_number = 0; • mmap the buffer mmap(0, ro_len, PROT_READ | PROT_WRITE, MAP_SHARED, fd, mem_import.out.gpu_va);

## Slide 21

## CVE-2021-28664 PoC

• Always SIGBUS


> Recovered by OCR — confidence 87/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CVE-2021-28664 PoC
¢ Always SIGBUS
```

## Slide 22

## CVE-2021-28664 PoC

- Always SIGBUS

🤔

- No physical pages


> Recovered by OCR — confidence 80/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
static vm_fault_t kbase_cpu_vm_fault(struct vm_fault x*vmf)
{
V F 2 2 1 2 4 p struct vm_area_struct *xvma = vmf->vma;
~ ~ O struct kbase_cpu_mapping map = vma—>vm_private_data;
pgoff_t map_start_pgoff;
pgoff_t fault_pgoff;
size_t i;
pgoff_t addr;
¢ Always SIGBUS size_t nents;
vm_fault_t ret = VM_FAULT_SIGBUS;
e N O p hysica | pages & Struct memory group_manager_device +mgm_dev;
KBASE_DEBUG_ASSERT(map) ;
KBASE_DEBUG_ASSERT(map->count > Q);
KBASE_DEBUG_ASSERT(map->kctx) ;
KBASE_DEBUG_ASSERT(map->alloc) ;
map_start_pgoff = vma—>vm_pgoff -— map->region->start_pfn;
kbase_gpu_vm_lock(map->kctx) ;
switch (query) { if (unlikely(map->region->cpu_alloc->type == KBASE_MEM_TYPE_ALIAS)) {
case KBASE_MEM_QUERY_COMMIT_SIZE: struct kbase_aliased *aliased = c
if (reg—>cpu alloc->type != ASE MEM TYPE ALIAS) { get_aliased_alloc(vma, map->region, &map_start_pgoff, 1);
*out = kbase_reg_current_backed_size(reg); ae (Wlelesaa)
} else { goto exit;
size_t i; :
struct kbase_aliased x*aliased; nents = aliased->length; ;
xout = 0: pages = aliased->alloc->pages + aliased->offset;
aliased = reg->cpu_alloc->imported.alias.aliased; nents = map->alloc->nents;
for (i = 0; i < reg->cpu_alloc—>imported.alias.nents; i++) pages = map->alloc->pages;
xout += aliased[i]. length;
ee fault_pgoff = map_start_pgoff + (vmf->pgoff - vma->vm_pgoff);
if (fault_pgoff >= nents)
goto exit;
```

## Slide 23

CVE-2021-28664 PoC


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
user_buf->pages = vmalloc(*va_pages * sizeof(struct page x));
else
user_buf->pages = kmalloc_array(xva_pages,
if (pages) { sizeof(struct page x), GFP_KERNEL);
struct device
ev = kctx->kbdev->dev;
unsigned long locat.size = user_buf->size;
unsigned long offset =-user_buf->address & ~PAGE_MASK;
struct tagged_addr «pa = kb get_gpu_phy_pages(reg);
if (!user_buf->pages)
goto no_page_array;
/* If the region is coherent with the CPU then the memory is imported
and mapped onto the GPU immediately.
Otherwise get_user_pages is called as a sanity check, but with
don import */ *
*
* NULL as the pages argument which will fault the pages, but not
*
*
ED_ON_IMPORT;
/* Top bit signifies that this was pi
user_buf—>current_mapping_usage_count |=
dma_addr_t dma_addr;
pin them. The memory will then be pinned only around the jobs that
specify the region as an external resource.
unsigned long min;| ™ */
if (reg->flags & KBASE_REG_SHARE_BOTH) {
min = MIN(PAGE_SIZE - offset, local_size); | ~* pages = user_buf->pages;
dma_addr = dma_map_page(dev, pages[il, *flags |= KBASE_MEM_IMPORT_HAVE_PAGES;
offset, min, }
DMA_BIDIRECTIONAL) ;
if (dma_mapping_error(dev, dma_addr) )
goto unwind_dma_map; if (!kbase_device_is_cpu_coherent(kctx->kbdev)) {
user_buf->dma_addrs[i] = dma_addr;
pali] = as_tagged(page_to_phys(pages [i] ));
local_size -= min;
offset = 0; } else if (flags & (BASE_MEM_COHERENT_SYSTEM |
| reg->gpu_alloc->nents = faulted_pages; |
```

## Slide 24

## CVE-2021-28664 PoC

😢

- Cannot set KBASE_REG_SHARE_BOTH on my MTK phone


> Recovered by OCR — confidence 82/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
user_buf->pages = vmalloc(*va_pages * sizeof(struct page x));
if (pages) { else
struct device «dev = kctx->kbdev-—>dev; user_buf->pages = kmalloc_array(*va_pages,
unsigned long local_size = user_buf->size; sizeof(struct page *), GFP_KERNEL) ;
unsigned long offset = user_buf->address & ~PAGE_MASK;
struct tagged_addr *pa = kbase_get_gpu_phy_pages(reg); if (!user_buf->pages)
goto no_page_array;
/* Top bit signifies that this was pinned on import */
user_buf->current_mapping_usage_count |= PINNED_ON_IMPORT; /* If the region is coherent with the CPU then the memory is imported
2 a; Se a Pee : * and mapped onto the GPU immediately.
a aes Ser. * Otherwise get_user_pages is called as a sanity check, but with
ie ae pesca — { * NULL as the pages argument which will fault the pages, but not
ie ier tigi min,| * pin them. The memory will then be pinned only around the jobs that
g 9g : * specify the region as an external resource.
ma_addr = dma_map_page(dev, pages[il, pages = user_buf—>pages;
offset, min, xflags |= KBASE_MEM_IMPORT_HAVE_PAGES;
DMA_BIDIRECTIONAL) ; }
if (dma_mapping_error(dev, dma_addr) )
user_buf->dma_addrs[i] = dma_addr; Uf: (flags & BASE_MEM_COHERENT_SYSTEM_REQUIRED &&
pali] = as_tagged(page_to_phys(pages[il)); '(flags & BASE_MEM_UNCACHED_GPU) )
offset = 0; } else if (flags & (BASE_MEM_COHERENT_SYSTEM |
reg->flags |= KBASE_REG_SHARE_BOTH;
reg->gpu_alloc->nents = faulted_pages;
¢ Cannot set KBASE_REG_SHARE_BOTH on my MTK phone ®
```

## Slide 25

CVE-2021-28664 PoC


> Recovered by OCR — confidence 81/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CVE-2021-28664 PoC
if (katom->core_req & BASE_JD_REQ_EXTERNAL_RESOURCES) { for (res_no = @; res_no < katom->nr_extres; res_no++) {
1 */ struct base_external_resource xres = &input_extres[res_no];
{it (kbase_jd_pre_external_resources(katom, user_atom) != @) { } struct kbase_va_region reg;
/* setup failed (no access, bad resource, unknown resource types, etc.) */ ~
katom->event_code = BASE_JD_EVENT_JOB_INVALID; Setter kbase_mem_phy_alloc alloc;
return jd_done_nolock(katom, NULL); #ifdef CONFIG_MALT_DMA_FENCE
} bool exclusive;
y exclusive = (res->ext_resource & BASE_EXT_RES_ACCESS_EXCLUSIVE)
? true : false;
#endif
reg = kbase_region_tracker_find_region_enclosing_address(
struct kbase_mem_phy_alloc #{base_map_external_resource( katom—>kctx,
struct kbase_context *kctx, struct kbase_va_region xreg, res—>ext_resource & ~BASE_EXT_RES_ACCESS_EXCLUSIVE) ;
SHAH: LGUs 2 Wetelee Li /* did we find a matching region object? +*/
if (kbase_is_region_invalid_or_free(reg)) {
/* roll back */
goto failed_loop;
lockdep_assert_held(&kctx->reg_lock) ;
}
if (!(katom—>core_req & BASE_JD_REQ_SOFT_JOB) &&
(reg->flags & KBASE_REG_PROTECTED)) {
/* decide what needs to happen for this resource */
switch (reg->gpu_alloc->type) {
case KBASE_MEM_TYPE_IMPORTED_USER_BUF: {
if ((reg->gpu_alloc—>imported.user_buf.mm != locked_mm) &
(!reg->gpu_alloc->nents) )
goto exit; katom—>atom_flags |= KBASE_KATOM_FLAG_PROTECTED;
reg->gpu_alloc->imported. user_buf. current_mapping_usage_count++;
if (1 == reg->gpu_alloc—>imported.user_buf.current_mapping_usage_count) {
if (err) { current—>mm) ;
reg—>gpu_alloc->imported.user_buf.current_mapping_usage_count—-; if (!alloc) {
Fi goto exit; err_ret_val = -EINVAL;
} goto failed_loop;
+ }
break;
```

## Slide 26

CVE-2021-28664 PoC


> Recovered by OCR — confidence 86/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
{
CVE-2021-28664 PoC
static int kbase_jd_user_buf_map(struct kbase_context xkctx,
struct kbase_va_region xreg)
long pinned_pages;
struct kbase_mem_phy_alloc xalloc;
struct page *kpages;
struct tagged_addr xpa;
long i;
unsigned long address;
struct device xdev;
unsigned long offset;
unsigned long local_size;
unsigned long gwt_mask = ~Q;
int err = kbase_jd_user_buf_pin_pages(kctx,
if (err)
return err;
alloc = reg->gpu_alloc;
pa = kbase_get_gpu_phy_pages(reg);
address = alloc-—>imported.user_buf.address;
pinned_pages = alloc-—>nents;
pages = alloc—>imported.user_buf.pages;
dev = kctx->kbdev->dev;
offset = address & ~PAGE_MASK;
local_size = alloc—>imported.user_buf.size;
reg);
int kbase_jd_user_buf_pin_pages(struct kbase_context *kctx,
struct kbase_va_region reg)
al
"struct kbase_mem_phy_alloc *alloc = reg->gpu_alloc;
struct page **pages = alloc->imported.user_buf. pages;
unsigned long address = alloc->imported.user_buf.address;
struct mm_struct *mm = alloc—>imported.user_buf.mm;
long pinned_pages;
long i;
if (WARN_ON(alloc->type != KBASE_MEM_TYPE_IMPORTED_USER_BUF) )
return —EINVAL;
if (alloc->nents) {
if (WARN_ON(alloc->nents != alloc->imported.user_buf.nr_pages) )
return —EINVAL;
else
return Q;
be
if (WARN_ON(reg->gpu_alloc->imported.user_buf.mm != current->mm) )
return —EINVAL;
#if LINUX_VERSION_CODE < KERNEL_VERSION(4, 6, 0)
pinned_pages = get_user_pages(NULL, mm,
address,
alloc->imported.user_buf.nr_pages,
#if KERNEL_VERSION(4, 4, 168) <= LINUX_VERSION_CODE && \
KERNEL_VERSION(4, 5, @) > LINUX_VERSION_CODE
reg->flags & KBASE_REG_GPU_WR ? FOLL_WRITE : @,
pages, NULL);
#else
reg->flags & KBASE_REG_GPU_WR,
#endif
#elif LINUX_VERSION_CODE < KERNEL_VERSION(4, 9, @)
pinned_pages = get_user_pages_remote(NULL, mm,
address,
alloc—>imported.user_buf.nr_pages,
reg->flags & KBASE_REG_GPU_WR,
@, pages, NULL);
#elif LINUX_VERSION_CODE < KERNEL_VERSION(4, 10, @)
pinned_pages = get_user_pages_remote(NULL, mm,
address,
alloc->imported.user_buf.nr_pages,
reg->flags & KBASE_REG_GPU_WR ? FOLL_WRITE : Q,
```

## Slide 27

## CVE-2021-28664 PoC

- 1. Mmap the Read-Only anonymous memory (CPU_VA1)

- 2. Import the CPU memory with BASE_MEM_PROT_CPU_WR

- 3. Mmap the GPU memory (CPU_VA2)

- 4. Submit a JOB with BASE_JD_REQ_EXTERNAL_RESOURCES (CPU_VA2, same VA)

- 5. Write the CPU_VA1 via CPU_VA2

## Slide 28

## Insufficient fix

• It sounds like double fetch

Import again


> Recovered by OCR — confidence 85/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
int
{
Insufficient fix
kbase_jd_user_buf_pin_pages(struct kbase_context *kctx,
struct kbase_va_region *reg)
struct kbase_mem_phy_alloc alloc = reg->gpu_alloc;
struct page **pages = alloc->imported.user_buf. pages;
unsigned long address = alloc->imported.user_buf. address;
struct mm_struct +mm = alloc->imported.user_buf.mm;
long pinned_pages;
long i;
if (WARN_ON(alloc->type != KBASE_MEM_TYPE_IMPORTED_USER_BUF) )
return —EINVAL;
#if KERNEL_VERSION(4, 6, 0) > LINUX_VERSION_CODE
faulted_page
#if KERNEL_VERSION( ) <= LINUX_VERSION_CODE && \
KERNEL_VERSION(4, 5, 0) > LINUX_VERSION_CODE
pages, NULL);
#else
©, pages, NULL);
#elif KERNEL_V! , 9, 8) > LINUX_VERSION_CODE
faulted; et_user_pages(address, *va_pages,
E ®, pages, NULL);
#else
faulted_page
ser_pages(current, current->mm, address, *va_pages,
#if KERNEL
fault
#elif KERNE!
faulted
#else
®, pages
LINUX_VERSION_CODE
NULL)
pages,
NULL)
address
pages, NULL); t pages, NULL);
if (alloc->nents) {
if (WARN_ON(alloc->nents != alloc->imported.user_buf.nr_pages) )
return —EINVAL;
else
return Q;
}
if (WARN_ON(reg->gpu_alloc->imported.user_buf.mm != current->mm) )
return —EINVAL;
e It sounds like double fetch
#if LINUX_VERSION_CODE < KERNEL_VERSION(4, 6, 0)
pinned_pages = get_user_pages(NULL, mm,
address,
#if KERNEL_VERSION(4, 4, 168) <= LINUX_VERSION_CODE && \
KERNEL_VERSION(4, 5, @) > LINUX_VERSION_CODE
reg->flags & KBASE_REG_GPU_WR ? FOLL_WRITE : 0,
pages, NULL);
#else
reg->flags & KBASE_REG_GPU_WR,
#endif
#elif LINUX_VERSION_CODE < KERNEL_VERSION(4, 9, 0)
pinned_pages = get_user_pages_remote(NULL, mm,
address,
reg->flags & KBASE_REG_GPU_WR,
@, pages, NULL);
#elif LINUX_VERSION_CODE < KERNEL_VERSION(4, 10, 0)
pinned_pages = get_user_pages_remote(NULL, mm,
address,
alloc—>imported.user_buf.nr_pages,
reg->flags & KBASE_REG_GPU_WR ? FOLL_WRITE : 0,
Import again
```

## Slide 29

## Insufficient fix

• It sounds like double fetch

   - KBASE_IOCTL_MEM_IMPORT: just touch the user memory

- KBASE_IOCTL_JOB_SUBMIT: import the physical pages

- Import again

## Slide 30

## PoC

- 1. Mmap the Read/Write anonymous memory (CPU_VA1)

- 2. Import the CPU memory with BASE_MEM_PROT_CPU_WR

- 3. Mmap the GPU memory (CPU_VA2)

- 4. Munmap the CPU_VA1

- 5. Fixedly mmap the Read-Only memory (CPU_VA1)

- 6. Submit a JOB with BASE_JD_REQ_EXTERNAL_RESOURCES (CPU_VA2, same VA)

- 7. Write the CPU_VA1 via CPU_VA2

## Slide 31

## Fix

<u>https://googleprojectzero.github.io/0days-in-the-wild//0day-RCAs/2021/CVE-2021-39793.html</u>


> Recovered by OCR — confidence 93/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CVE-2022-22706 | CVE-2021-39793:
Mali GPU driver makes read-only imported
pages host-writable
Jann Horn
The Basics
Disclosure or Patch Date: March 7, 2022
Product: Arm Mali GPU driver for Linux/Android
Advisory:
¢ from Arm (upstream):
¢ from Google Pixel: http xel
Affected Versions: see Arm advisory (note that the affected version range for the Bifrost version of
the related CVE-2021-28664 seems to be off-by-one)
First Patched Version:
¢ for Arm: see Arm advisory
¢ for Pixel: patch level 2022-03-05
Issue/Bug Report: N/A
blackhat
```

## Slide 32

## Exploit – Modifying the disk cache

• Old way

https://www.blackhat.com/docs/eu-16/materials/eu-16-Taft-GPU-Security-Exposed.pdf


> Recovered by OCR — confidence 93/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Exploit — Modifying the disk cache
° Old way
Modifying the Disk Cache
¢ mmap() can be used to map files into memory.
¢ Contents of file are cached in memory for other processes to
use.
¢ By mmap()-ing a suid binary, instructions in privileged
binaries can be over-written through the GPU.
e Changes aren't stored to disk.
```

## Slide 33

## Exploit – Modifying the disk cache

• New way

hSps://source.android.com/docs/core/architecture/kernel/loadable-kernel-modules


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Exploit — Modifying the disk cache
° New way
Loadable Kernel Modules °-
As part of the module kernel requirements introduced in Android 8.0, all system-on-chip (SoC) kernels must support
loadable kernel modules.
Module signing
Module-signing isnot supported for GKI vendor modules. On devices required to support verified boot, Android requires
kernel modules to be in the partitions that have dm-verity enabled. This removes the need for signing individual modules
for their authenticity. Android 13 introduced the concept of GKI modules. GK! modules use the kernel's build time signing
infrastructure to differentiate between GKI and other modules at run time. Unsigned modules are allowed to load as long
as they only use symbols appearing on the allowlist or provided by other unsigned modules. To facilitate GKI modules
signing during GKI build using kernel's build time key pair, GKI kernel config has enabled CONFIG_MODULE_SIG_ALL=y .
To avoid signing non-GKI modules during device kernel builds, you must add # CONFIG_MODULE_SIG_ALL is not set
Kernel configuration options ©
To support loadable kernel modules, android-base.cfg [4 in all common kernels includes the following ker
options (or their kernel-version equivalent):
CONFIG_MODULES=y
CONFIG_MODULE_UNLOAD=y
CONFIG_MODVERSION
as part of your kernel config fragments.
All device kernels must enable these options. Kernel modules should also support unloading and reloading whenever
possible.
https://source.android.com/docs/core/architecture/kernel/loadable-kernel-modules
```

## Slide 34

## Exploit – Modifying the disk cache

- It’s similar to Dirty pipe exploit for Android

- Exploit steps:

   - 1. Modify a shared library and hijack a privileged process

   - 2. Patch the modprobe and a shared library as the kernel module, transit the SELinux context, and execute the patched modprobe

   - 3. Insert the kernel module and gain the kernel arbitrary code execution ability

## Slide 35

## Exploit – Memory corruption

- Not GKI (<kernel 5.10)

- Module signing enabled


> Recovered by OCR — confidence 83/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Exploit - Memory corruption
CONFIG_RT_MUTEXES=y
* Not GKI (<kernel 5.10) CONFIG_BASE_SMALL=0
CONFIG_MODULE_SIG_FORMAT=y
CONFIG_MODULES=y
# CONFIG _MODULE_FORCE_LOAD is not set
* Module signing enabled # CONFIG_MODULE_FORCE_UNLOAD is not set
CONFIG_MODVERSIONS=y
CONFIG_ASM_MODVERSIONS=y
# CONFIG_MODULE_SRCVERSION_ALL is not set
CONFIG_MODULE_SCMVERSION=y
CONFIG_MODULE_SIG=y
CONFIG_MODULE_SIG_FORCE=y
CONFIG_MODULE_SIG_ALL=y
# CONFIG _MODULE_SIG_SHA224 is not set
# CONFIG _MODULE_SIG_SHA256 is not set
# CONFIG_MODULE_SIG_SHA384 is not set
CONFIG_MODULE_SIG_SHA512=y
CONFIG_MODULE_SIG_HASH="sha512"
# CONFIG _MODULE_COMPRESS is not set
# CONFIG_MODULE_ALLOW_MISSING_NAMESPACE_IMPORTS is not set
# CONFIG_UNUSED_SYMBOLS is not set
CONFIG_TRIM_UNUSED_KSYMS=y
```

## Slide 36

## Exploit – Memory corrupXon

- Read only memory

- vm_insert_page

   - User buffer can be imported


> Recovered by OCR — confidence 83/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Exploit - Memory corruption
¢ Read only memory
*vm_insert_page
¢ User buffer can be imported
page->page_ptr = alloc_page(GFP_KERNEL B
__GFP_HIGHMEM |
__GFP_ZERO) ;
if (!page->page_ptr) {
pr_err("%d: binder_alloc_buf failed for Py
alloc->pid, page_addr) ;
goto err_alloc_page_failed;
page->alloc = alloc;
user_page_addr = (uintptr_t)page_addr;
static int binder_mmap(struct file *filp, struct vm_area_struct *vma)
struct binder_proc *proc = filp->private_data;
if (proc->tsk != current->group_leader)
return -EINVAL;|
if (vma->vm_flags & FORBIDDEN_MMAP_FLAGS) { // VM_WRITE
pr_err("%s: %d %lx-%lx %s failed %d\n", __func__,
proc->pid, vma—>vm_start, vma->vm_end, “bad vm_flags", —EPERM);
return —EPERM;
vma->vm_flags |= VM_DONTCOPY | VM_MIXEDMAP;
vma->vm_flags &= ~VM_MAYWRITE;
vma->vm_ops = &binder_vm_ops;
vma->vm_private_data = proc;
return binder_alloc_mmap_handler(&proc-—>alloc, vma);
ret = vm_insert_page(vma, user_page_addr, page[Q].page_ptr);
```

## Slide 37

## Exploit – Memory corrupXon

• Craft the flat_binder_object by modifying the binder’s user buffer


> Recovered by OCR — confidence 83/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Exploit - Memory corruption
° Craft the flat_binder_object by modifying the binder’s user buffer
hdr = &object.hdr;
switch (hdr->type) {
struct flat_binder_object { case Joba Ns bs
struct binder_object_header hdr; case BINDER_TYPE_WEAK_BINDER: {
u32 flags; struct flat_binder_object xfp;
struct binder_node xnode;
/* 8 bytes of data. x*/
eer fp = to_flat_binder_object(hdr);
: : 3 ; de = binder_get_node(proc, fp->binder);
We —u32 handle; /* remote object */ pr_err("transaction release %d bad node %01611x\n",
: debug_id, (u64)fp->binder) ;
/* extra data associated with local object x*/ }
binder_uintptr_t cookie; binder_debug(BINDER_DEBUG_TRANSACTION,
node->debug_id, (u64)node->ptr);
binder_dec_node(node, hdr->type == BINDER_TYPE_BINDER,
Q);
binder_put_node(node) ;
} break;
blackhat
```

## Slide 38

## Exploit – Memory corruption

- Exploit the UAF bug like CVE-2020-0041

• https://labs.bluefrostsecurity.de/blog/2020/04/08/cve-2020-0041-part-2escalating-to-root/

## Slide 39

## Exploit – Memory corruption

- Exploit the UAF bug like CVE-2020-0041

   - hjps://labs.bluefrostsecurity.de/blog/2020/04/08/cve-2020-0041-part-2escalakng-to-root/

## Slide 40

## Agenda

- Introduc_on

- Bug #1

- _Bug #2_

- Conclusion

## Slide 41

## Bug #1 PoC more details

- 1. Mmap the Read/Write anonymous memory (CPU_VA1)

- 2. Import the CPU memory with BASE_MEM_PROT_CPU_WR

- 3. Mmap the GPU memory (CPU_VA2)

- 4. Munmap the CPU_VA1

- 5. Fixedly mmap the Read-Only memory (CPU_VA1)

- 6. Submit a JOB with BASE_JD_REQ_EXTERNAL_RESOURCES (CPU_VA2, same VA)

- 7. Write the CPU_VA1 via CPU_VA2

   - Wait a moment for kbase_jd_user_buf_pin_pages to be called

## Slide 42

## Bug #1 PoC more details

- 1. Mmap the Read/Write anonymous memory (CPU_VA1)

- 2. Import the CPU memory with BASE_MEM_PROT_CPU_WR • 3. Mmap the GPU memory (CPU_VA2)

- 4. Munmap the CPU_VA1

- 5. Fixedly mmap the Read-Only memory (CPU_VA1)

- 6. Submit a JOB with BASE_JD_REQ_EXTERNAL_RESOURCES (CPU_VA2, same VA)

- 7. Write the CPU_VA1 via CPU_VA2

   - Sleep(5) == Always SIGBUS

## Slide 43

Bug #1 PoC more details

🤔

- No physical pages, why?


> Recovered by OCR — confidence 85/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Bug #1 PoC more details
¢ No physical pages, why?@
switch (query) {
if (reg->cpu_alloc->type != KBASE_MEM_TYPE_ALIAS) {
*out = kbase_reg_current_backed_size(reg);
} else {
size_t i;
struct kbase_aliased x*aliased;
aliased = reg->cpu_alloc-—>imported.alias.aliased;
xout += aliased[i]. length;
}
break;
static vm_fault_t kbase_cpu_vm_fault(struct vm_fault x*vmf)
{
struct vm_area_struct *vma = vmf—>vma;
struct kbase_cpu_mapping +map = vma—>vm_private_data;
pgoff_t map_start_pgoff;
pgoff_t fault_pgoff;
size_t i;
pgoff_t addr;
size_t nents;
vm_fault_t ret = VM_FAULT_SIGBUS;
Struct memory_group_manager_device *mgm_dev;
KBASE_DEBUG_ASSERT(map) ;
KBASE_DEBUG_ASSERT(map->count > Q);
KBASE_DEBUG_ASSERT(map->kctx) ;
KBASE_DEBUG_ASSERT(map->alloc) ;
map_start_pgoff = vma—>vm_pgoff -— map->region->start_pfn;
kbase_gpu_vm_lock(map->kctx) ;
if (unlikely(map->region->cpu_alloc->type == KBASE_MEM_TYPE_ALIAS)) {
struct kbase_aliased x*aliased =
get_aliased_alloc(vma, map->region, &map_start_pgoff, 1);
if (!aliased)
goto exit;
nents = aliased->length;
pages = aliased->alloc->pages + aliased->offset;
}else {
nents = map->alloc-—>nents;
pages = map—>alloc-—>pages;
fault_pgoff = map_start_pgoff + (vmf->pgoff - vma->vm_pgoff);
if (fault_pgoff >= nents)
goto exit;
```

## Slide 44

## Bug #1 PoC more details

- Physical pages will be released when the JOB is finished

- Trigger the VM_FAULT before the pages are released

## Slide 45

## Bug #1 PoC more details

- 1. Mmap the Read/Write anonymous memory (CPU_VA1)

- 2. Import the CPU memory with BASE_MEM_PROT_CPU_WR

- 3. Mmap the GPU memory (CPU_VA2)

- 4. Munmap the CPU_VA1

- 5. Fixedly mmap the Read-Only memory (CPU_VA1)

- 6. Submit a JOB with BASE_JD_REQ_EXTERNAL_RESOURCES (CPU_VA2, same VA)

- 7. Write the CPU_VA1 via CPU_VA2

   - Query the GPU VA whether the pages are imported or not

## Slide 46

Bug #1 PoC more details

## Slide 47

## Bug #1 PoC more details

😊

- The CPU mapping has not been handled

- The imported pages can be freed and reclaimed


> Recovered by OCR — confidence 84/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
int kbase_mem_shrink(struct kbase_context xconst kctx,
B U g it 1 Po C an O re d eta Is ; struct kbase_va_region *const reg, u64 const new_pages)
u64 delta, old_pages;
int err;
static void kbase_jd_user_buf_unmap(struct kbase_context x*kctx, lockdep_assert_held(&kctx—>reg_lock) ;
truct kl h loc *all l writeabl
F struct kbase_mem_phy_alloc xalloc, bool writeable) if (WARN_ON(!ketx))
long i; return -EINVAL;
struct page *xpages;
unsigned long size = alloc->imported.user_buf.size; if (WARN_ON( !reg))|
KBASE_DEBUG_ASSERT(alloc->type == KBASE_MEM_TYPE_IMPORTED_USER_BUF) ;
unsigned long local_size;
dma_addr_t dma_addr = alloc->imported.user_buf.dma_addrs [i] ;
old_pages = kbase_reg_current_backed_size(reg);
if (WARN_ON(old_pages < new_pages) )
return —EINVAL;
delta = old_pages - new_pages;
local_size = MIN(size, PAGE_SIZE - (dma_addr & ~PAGE_MASK)); 5
dma_unmap_page(kctx->kbdev->dev, dma_addr, local_size, /* Update the GPU mapping */
DMA_BIDIRECTIONAL) ; err = kbase_mem_shrink_gpu_mapping(kctx, reg,
if (writeable) new_pages, old_pages) ;
put_page(pages [il] ); kbase_mem_shrink_cpu_mapping(kctx, reg,
pages[i] = NULL; new_pages, old_pages);
kbase_free_phy_pages_helper(reg->cpu_alloc, delta);
size -= local_size; if (reg->cpu_alloc != reg->gpu_alloc)
} kbase_free_phy_pages_helper(reg->gpu_alloc, delta);
#if IMALI_USE CSF ip
#endif return err;
Ip }
¢ The CPU mapping has not been handled ®
¢ The imported pages can be freed and reclaimed
```

## Slide 48

## Two bugs One PoC

- 1. Mmap the Read/Write anonymous memory (CPU_VA1)

- 2. Import the CPU memory with BASE_MEM_PROT_CPU_WR

- 3. Mmap the GPU memory (CPU_VA2)

- 4. Munmap the CPU_VA1

- 5. Fixedly mmap the Read-Only memory (CPU_VA1)

- 6. Submit a JOB with BASE_JD_REQ_EXTERNAL_RESOURCES (CPU_VA2, same VA)

- 7. Read/Write the CPU_VA2 and trigger the VM_FAULT on the CPU side

- 8. Munmap and release the CPU_VA1

- 9. Read/Write the freed pages via CPU_VA2

## Slide 49

## Bug #2 PoC

- 1. Mmap the Read/Write anonymous memory (CPU_VA1)

- 2. Import the CPU memory with BASE_MEM_PROT_CPU_WR

- 3. Submit a JOB with BASE_JD_REQ_EXTERNAL_RESOURCES (CPU_VA2, same VA)

- 4. Read the CPU_VA2 and trigger the VM_FAULT on the CPU side

- 5. Munmap and release the CPU_VA1

- 6. Read/Write the freed pages via CPU_VA2

## Slide 50

Fix


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 94/100 on the text kept, 91/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Code Integrity - Signatures

[Window 1] SgrmBroker.exe Properties
Certificate
General | Details | Certification Path
Show: <All>
Field                          Value
Enhanced Key Usage             Windows TCB Component (1.3.…
Subject Key Identifier         793165f0dbf15e5c04453d756..
Subject Alternative Name       Directory Address:SERIALNUM.
Authority Key Identifier       KeyID=a92902398e16c49778..
CRL Distribution Points        [1]CRL Distribution Point: Distr..
Authority Information Access   [1]Authority Info Access: Acc…
Basic Constraints              Subject Type=End Entity, Pat..
Thumbprint                     08647820d503fd505df763ab2..
[red box]
Windows TCB Component (1.3.6.1.4.1.311.10.3.23)
Protected Process Verification (1.3.6.1.4.1.311.10.3.24)
Windows System Component Verification (1.3.6.1.4.1.311.10.3.6)
Code Signing (1.3.6.1.5.5.7.3.3)

[Window 2] svchost.exe Properties
Certificate
General | Details | Certification Path
Show: <All>
Field                          Value
Enhanced Key Usage             Protected Process Light Verific.
Subject Key Identifier         01f0d3a457341838ebb31253..
Subject Alternative Name       Directory Address:SERIALNUM.
Authority Key Identifier       KeyID=a92902398e16c49778.
CRL Distribution Points        [1]CRL Distribution Point: Distr.
Authority Information Access   [1]Authority Info Access: Acc..
Basic Constraints              Subject Type=End Entity, Pat..
Thumbprint                     c60a14a6bd925780e9f0463ba..
[red box]
Protected Process Light Verification (1.3.6.1.4.1.311.10.3.22)
Windows System Component Verification (1.3.6.1.4.1.311.10.3.6)
Code Signing (1.3.6.1.5.5.7.3.3)

[Window 3] csrss.exe Properties
Certificate
General | Details | Certification Path
Show: <All>
Field                          Value
Enhanced Key Usage             Protected Process Light Verific..
Subject Key Identifier         7d3af1a3055c18fdf39399016..
Subject Alternative Name       Directory Address:SERIALNUM.
Authority Key Identifier       KeyID=a92902398e16c49778..
CRL Distribution Points        [1]CRL Distribution Point: Distr..
Authority Information Access   [1]Authority Info Access: Acc..
Basic Constraints              Subject Type=End Entity, Pat..
Thumbprint                     e94a68b056ce2fa8ab046a84f..
[red box]
Protected Process Light Verification (1.3.6.1.4.1.311.10.3.22)
Windows TCB Component (1.3.6.1.4.1.311.10.3.23)
Windows System Component Verification (1.3.6.1.4.1.311.10.3.6)
Code Signing (1.3.6.1.5.5.7.3.3)
```

## Slide 51

## Exploit

- Physical pages Use-Aoer-Free

   - In theory, all the pages within the free state can be imported and reused

0x1337000
0x8001000
0x1338000
0x8300000
0x18003000
0x8337000
0x8338000
0x20005000
User virtual address Physical pages

## Slide 52

## Exploit

- Physical pages Use-After-Free

   - In theory, all the pages within the free state can be imported and reused

- Hijack a kernel object

## Slide 53

## Exploit

- Physical pages Use-Aoer-Free

   - In theory, all the pages within the free state can be imported and reused

- Hijack a kernel object

   - MIGRATE_UNMOVABLE VS MIGRATE_MOVABLE

hHp://i.blackhat.com/USA-22/Thursday/US-22-WANG-Ret2page-The-Art-of-ExploiIng-Use-AJer-Free-VulnerabiliIes-in-the-Dedicated-Cache.pdf

## Slide 54

## Exploit

- task_struct as the target object

   - Leak kernel pointer to bypass KASLR

   - • Leak cred pointer to gain ROOT privilege later

## Slide 55

## Exploit

- task_struct as the target object

   - Leak kernel pointer to bypass KASLR

   - Leak cred pointer to gain ROOT privilege later

   - Can be easily found

## Slide 56

## Exploit

- cat /proc/slabinfo |grep task_struct

   - task_struct 3536   3804   4736    6    8 : tunables 634    634      0

      - 0    0    0 : slabdata

- Some objects can occupy two pages

   - The physical pages corresponding to user addresses are unlikely to be conkguous

0 1 2 3 4 5

## Slide 57

## Exploit

- Search the task_struct objects

##### User address

##### task_struct

- PID/TID

- Comm

- …

PID/TGID

- The target object only occupies one page

- Leak kernel pointers • Cred - *(u64*)(A + OFF_CRED – OFF_PID)

Share the same physical page(start address aligned)

## Slide 58

## Exploit

- The vic_m thread can be iden_fied

• The addr_limit of thread_info is completely under the control


> Recovered by OCR — confidence 92/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Exploit
¢ The victim thread can be identified
¢ The addr_limit of thread_info is completely under the control
```

## Slide 59

## Exploit

- The vic_m thread can be iden_fied

- The addr_limit of thread_info is completely under the control

- • AARW – (Write primi_ve step)

   - Main process write the data to pipe

      - Any value

      - USER_DS

   - Main process write KERNEL_DS to the addr_limit of vickm thread

   - Vickm thread wake up and use the kernel pointer as read buffer

      - Target kernel address

      - addr_limit kernel address

   - Vickm read the data from pipe

## Slide 60

## Exploit

### • Exploit steps

- 1. Mmap a large chunk of anonymous memory(RW permission)

- 2. Import the CPU memory with BASE_MEM_PROT_CPU_WR

- 3. Submit a JOB with BASE_JD_REQ_EXTERNAL_RESOURCES

- 4. Read the mapped GPU VA and trigger the VM_FAULT on the CPU side

- 5. Munmap and release the anonymous memory

- 6. Spawn a large number of threads

- 7. Search the mapped GPU VA and find the target thread

- 8. Leak the kernel pointers and bypass KASLR

- 9. Patch the cred and SELinux state

- 10. Spawn a ROOT shell

## Slide 61

Demo

## Slide 62

## Agenda

- Introduc_on

- Bug #1

- Bug #2

- _Conclusion_

## Slide 63

## Black Hat Sound Bytes

- Analyzing the old bug is always an efficient way to find a new one.

- Memory corrup_on is good, logic bug is beter.

- Even with more and more both hardware and sooware mi_ga_ons, Android roo_ng is s_ll possible.

## Slide 64

## References

[1] <u>https://googleprojectzero.blogspot.com/2022/11/a-very-powerful-clipboardsa</u> ~~<u>msung-in-the-wild-exploit-chain.html</u>~~

[2] <u>https://i.blackhat.com/USA-22/Thursday/US-22-WANG-Ret2page-The-Art-ofEx</u> ~~<u>ploiting-Use-After-Free-Vulnerabilities-in-the-Dedicated-Cache.pdf</u>~~ [3] <u>https://googleprojectzero.blogspot.com/2020/12/an-ios-hacker-triesan</u> ~~<u>droid.html</u>~~

[4] <u>https://www.blackhat.com/docs/eu-16/materials/eu-16-Taft-GPU-SecurityEx</u> ~~<u>posed.pdf</u>~~

[5] <u>https://googleprojectzero.github.io/0days-in-the-wild//0day-RCAs/2021/CVE20</u> ~~<u>21-39793.html</u>~~

[6] <u>https://source.android.com/docs/core/architecture/kernel/loadable-kernelmo</u> ~~<u>dules</u>~~

[7] <u>https://labs.bluefrostsecurity.de/blog/2020/04/08/cve-2020-0041-part-2esc</u> ~~<u>alating-to-root/</u>~~

## Slide 65

# Thank you!

WANG, YONG (@ThomasKing2014) ThomasKingNew@gmail.com
