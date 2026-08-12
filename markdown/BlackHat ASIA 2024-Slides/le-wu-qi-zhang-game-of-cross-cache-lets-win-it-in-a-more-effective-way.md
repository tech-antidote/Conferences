---
title: "Game of Cross Cache Let's Win It in a More Effective Way"
speakers: ["Le Wu", "Qi Zhang"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2024"
edition: "ASIA"
year: 2024
source_pdf: "BlackHat ASIA 2024-Slides/Le Wu & Qi Zhang-Game of Cross Cache Let's Win It in a More Effective Way.pdf"
pages: 93
sha256: "3d6f4e948d13a7c9ea659d69a624716081b23ed883037e27566cc01912d05da4"
text_chars: 41711
ocr_pages: 2
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:49:21Z"
---
# Game of Cross Cache Let's Win It in a More Effective Way

**Speakers:** Le Wu, Qi Zhang  
**Conference:** Black Hat ASIA 2024  
**Source:** `BlackHat ASIA 2024-Slides/Le Wu & Qi Zhang-Game of Cross Cache Let's Win It in a More Effective Way.pdf` (93 pages)

## Slide 1

Game of Cross Cache: Let's win it in a more effective way!

Le Wu From Baidu Security

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Sang ~~. T
blackhat« D> <> Se
oo” —ieiens 2024 l : - &. evi
Game of Cross Cache:
Let's win itin a more effective way!
Le Wu From Baidu Security
#BHASIA @BlackHatEvents
```

## Slide 2

## About me

- Le Wu, @NVamous on Twitter

- Focus on Android/Linux vulnerability

- Dirty Pagetable —— A novel technique to rule the Linux Kernel [1]

- Blackhat USA, Europe, Asia

[1]:https://yanglingxi1993.github.io/dirty_pagetable/dirty_pagetable.html

# BHASIA @BlackHatEvents

## Slide 3

## Agenda

- Introduction to Cross-cache attack

- Challenges in Cross-cache attack

- Advancing Towards a More Effective Cross-cache Attack

- Exploit File UAF with Dirty Pagetable

- Summary

# BHASIA @BlackHatEvents

## Slide 4

### Introduction to Cross-cache attack A Simplified Cross-cache Attack For UAF

**UAF** Trigger UAF to release the victim **object A** ;

Reclaim the victim slab of victim **object A** to Page allocator; kmem_cache B reuse the pages of victim slab, and **object A** is reallocated as **object B** ; Operations to victim **object A** ; corrupt the **object B** Make use of corrupted **object B** to get ROOT;

(Object A or object B could be pages or other kinds of memory regions)

## Slide 5

### Introduction to Cross-cache attack

Cross-cache attack is getting popular:

- Original vulnerable object is not exploitable, especially the one allocated from a dedicated kmem_cache

- Transform the unknown vulnerability to well-known one to simplify the exploitation

- Build data-only exploitation techniques to defeat growing mitigations like KASLR, PAN, CFI...

|**Method**|**Cross-cache From**|**Cross-cache To**|
|---|---|---|
|ret2dir|*|direct mapping|
|ret2page|*|kernel allocated page|
|Drity Cred|*|struct cred|
|**Dirty Pagetable**
...|*
...|**user page table**
...|

## Slide 6

### Introduction to Cross-cache attack

Can we make it less unstable, or in other words, more efficient?

Well, it's known as an **unstable** technique...

## Slide 7

#### Common workflow of Cross-cache attack

##### Step0. Common knowledge for SLUB allocator

**objs_per_slab** : number of objects in a single slab **order** : order of pages in a single slab

## Slide 8

#### Common workflow of Cross-cache attack

Step 0. Common knowledge for SLUB allocator

## Slide 9

#### Common workflow of Cross-cache attack

Step0. Common knowledge for SLUB allocator

The deterministic method for putting slab into the percpu partial list:

- Create a full slab

## Slide 10

#### Common workflow of Cross-cache attack

Step0. Common knowledge for SLUB allocator

The deterministic method for putting slab into the percpu partial list:

- Pin on cpu#0 and release an object from the full slab

## Slide 11

#### Common workflow of Cross-cache attack

Step0. Common knowledge for SLUB allocator

Flushing for the percpu partial list:

**cpu_partial:** the maximum number of slabs can be put in the percpu partial list

## Slide 12

#### Common workflow of Cross-cache attack

##### Step0. Common knowledge for SLUB allocator

Flushing for the percpu partial list:

- Slabs containing some in-use objects are placed on SLUB's per-NUMA-node partial list

- **Slabs that are completely empty are freed back to the page allocator**

## Slide 13

#### Common workflow of Cross-cache attack [2]

Step1. Pin our task to a single CPU, for example, cpu#0

Step2. Defragmentation: to drain partially-free slabs of all their free objects Step3. Allocate around **objs_per_slab** * (1+ **cpu_partial** ) objects

[2]:https://googleprojectzero.blogspot.com/2021/10/how-simple-linux-kernel-memory.html

## Slide 14

#### Common workflow of Cross-cache attack

Step4. Allocate objs_per_slab-1 objects as pre-alloc objects

Step5. Allocate the victim object

Step6. Trigger the vulnerability(UAF) to release the victim object

## Slide 15

#### Common workflow of Cross-cache attack

Step7. Allocate objs_per_slab+1 objects as post-alloc objects

## Slide 16

#### Common workflow of Cross-cache attack

Step8. Release all the pre-alloc and post-alloc objects

## Slide 17

#### Common workflow of Cross-cache attack

Step9. Free one object per slab from the allocations in Step3

After releasing "cpu_partial – 1" objects:

## Slide 18

#### Common workflow of Cross-cache attack

Step9. Free one object per slab from the allocations from Step3

After releasing one more object, the flushing for cpu partial list gets triggered:

## Slide 19

#### Common workflow of Cross-cache attack

Step10. Heap spray with object B to occupy the victim slab, victim **object A** gets reallocated as **object B**

Step11. Construct primitives for privilege escalation

## Slide 20

### Challenges in Cross-cache attack

Challenge 1
Challenge 2

- **Challenge 1** : How to discard the victim slab under a constrained allocation primitive

- **Challenge 2** : How to make high-order slab reuse the low-order slab deterministically

# BHASIA @BlackHatEvents

## Slide 21

Challenges in Cross-cache attack **Challenge 1** : How to discard the victim slab under a constrained allocation primitive

Step 3. Allocate around **objs_per_slab** * (1+ **cpu_partial** ) objects

This step requires us:

- Allocate a large number of objects

- Keep this large number of objects unreleased for a while

## Slide 22

### Challenges in Cross-cache attack

• Allocate a large number of objects

   - ❑ Dedicated kmem-cache is becoming a mitigation for cross-cache attack. We can hardly find suitable allocation primitives. The known mitigations like: CONFIG_RANDOM_KMALLOC_CACHES, AUTOSLAB

   - ❑ Limited system resources

   - ❑ Constraints of kernel components

- Keep the large number of objects unreleased for a while

   - ❑ Temporary kernel object: gets allocated and then released.

## Slide 23

### Challenges in Cross-cache attack

**Challenge 2** : How to make high-order slab reuse the low-order slab deterministically ⚫ order-N pages --> order-M pages, N > M

Can be done by allocating tons of object B, order-N pages will definitely be reused as order-M pages. This may require:

• too many object B, this can be really hard under a limited system resources

## Slide 24

### Challenges in Cross-cache attack

**Challenge 2** : How to make high-order slab reuse the low-order slab deterministically ⚫ order-N pages --> order-M pages, N < M

Allocating tons of object B won't help. We need to let order-N pages get compacted into order-M pages, so object B can reuse these order-N pages. So how? ---- Shaping the heap!

## Slide 25

### Advancing Towards a More Effective Cross-Cache Attack

# BHASIA @BlackHatEvents

## Slide 26

#### Advancing Towards a More Effective Cross-Cache Attack CVE-2023-21400

A NPU issue affected qualcomm 4.14 kernel, can be accessed from unstrusted app, found by Ye Zhang **Task A(On cpu1) Task B(On cpu2)**

**mutex_lock(&host_ctx->lock);**

**network = get_network_by_hdl(host_ctx, …,unload->network_hdl); unload_cmd1 = npu_alloc_network_cmd(host_ctx, 0); npu_queue_network_cmd(network, unload_cmd1); mutex_unlock(&host_ctx->lock);**

**mutex_lock(&host_ctx->lock);**

20s

**network = get_network_by_hdl(host_ctx, …,unload->network_hdl); unload_cmd2 = npu_alloc_network_cmd(host_ctx, 0); npu_queue_network_cmd(network, unload_cmd2); mutex_unlock(&host_ctx->lock); wait_for_completion_timeout(&unload_cmd2->cmd_done,NW_CMD_TIMEOUT); mutex_lock(&host_ctx->lock); npu_dequeue_network_cmd(network, unload_cmd2); npu_free_network_cmd(host_ctx, unload_cmd2); free_network(host_ctx, client, network->id); mutex_unlock(&host_ctx->lock); unload_cmd1 gets released here!**

**wait_for_completion_timeout(&unload_cmd1->cmd_done,NW_CMD_TIMEOUT); mutex_lock(&host_ctx->lock);**

**npu_dequeue_network_cmd(network, unload_cmd1); npu_free_network_cmd(host_ctx, unload_cmd1); UAF or Double free happens! free_network(host_ctx, client, network->id); mutex_unlock(&host_ctx->lock);**

## Slide 27

#### Advancing Towards a More Effective Cross-Cache Attack CVE-2023-21400)[3]

With the bug, we can:

static void npu_dequeue_network_cmd(struct npu_network *network, struct npu_network_cmd *cmd)

{ list_del(&cmd->list); list_del() primitive }

wait_for_completion_timeout(& **unload_cmd1** ->cmd_done,NW_CMD_TIMEOUT); mutex_lock(&host_ctx->lock);

npu_dequeue_network_cmd(network, **unload_cmd1** ); npu_free_network_cmd(host_ctx, **unload_cmd1** ); free_network(host_ctx, client, network->id); mutex_unlock(&host_ctx->lock);

static void npu_free_network_cmd(struct npu_host_ctx *ctx, struct npu_network_cmd *cmd) { **Arbitrary kmem_cache_free() primitive** if (cmd->stats_buf) kmem_cache_free(ctx->stats_buf_cache, cmd->stats_buf);

kmem_cache_free(ctx->network_cmd_cache, cmd); } Double free primitive

[3]:https://i.blackhat.com/EU-23/Presentations/EU-23-Zhang-Attacking-NPUs-of-Multiple-Platforms.pdf

## Slide 28

#### Advancing Towards a More Effective Cross-Cache Attack

##### CVE-2023-21400

Victim object:

struct npu_network_cmd { struct list_head list;

... struct completion cmd_done; /* stats buf info */ uint32_t stats_buf_size; void __user *stats_buf_u; void *stats_buf; int ret_status;

Allocated from a dedicated kmem_cache "IPA_TX_PKT_WRAPPER"

};

## Slide 29

#### Advancing Towards a More Effective Cross-Cache Attack

CVE-2023-21400

Allocated from a dedicated kmem_cache "IPA_TX_PKT_WRAPPER"

## Slide 30

#### Advancing Towards a More Effective Cross-Cache Attack CVE-2023-21400

Allocated from a dedicated kmem_cache "IPA_TX_PKT_WRAPPER"

Clean and inactive
kmem_cache

## Slide 31

Advancing Towards a More Effective Cross-Cache Attack CVE-2023-21400

Exploitation plan:

Trigger the issue Victim  Cross-cache attack
npu_network_cmd  Victim file array
object
Make use of arbitrary
Dirty Pagetable
kfree() primitive
A file UAF Get ROOT!
Data-only exploitation, woohoo!
But the cross cache is known for the unstable...

## Slide 32

#### Advancing Towards a More Effective Cross-Cache Attack

Step1. Trigger the issue

Step2. Cross-cache attack: cross from kmem_cache "IPA_TX_PKT_WRAPPER" to file_array(kmalloc-8k)

kmem_cache "IPA_TX_PKT_WRAPPER": order-0 slab

file_array: allocated from kmem_cache "kmalloc-2k" ~ "kmalloc-8k" , all are order-3 slab

static struct fdtable * alloc_fdtable(unsigned int nr) { struct fdtable *fdt; void *data; ... nr /= (1024 / sizeof(struct file *)); nr = roundup_pow_of_two(nr + 1); nr *= (1024 / sizeof(struct file *)); ... data = kvmalloc_array(nr, sizeof(struct file *), GFP_KERNEL_ACCOUNT); ... fdt->fd = data; ... return fdt;

We choose kmalloc-8k to allocate file array from.

... }

## Slide 33

#### Advancing Towards a More Effective Cross-Cache Attack

Step2. Cross-cache attack: cross from kmem_cache "IPA_TX_PKT_WRAPPER" to file_array(kmalloc-8k)

Challenge 1
Challenge 2

- Challenge 1: How to discard the victim order-0 slab under a constrained allocation primitive

- Challenge 2: How to make order-3 slab reuse the order-0 slab deterministically

## Slide 34

Advancing Towards a More Effective Cross-Cache Attack Challenge 1: How to discard the victim order-0 slab under a constrained allocation primitive

❑ npu_network_cmd object is a temporary likely kernel object: gets allocated and then released

`o` MSM_NPU_LOAD_NETWORK_V2 `o` MSM_NPU_UNLOAD_NETWORK `o` MSM_NPU_EXEC_NETWORK_V2 (use this later)

struct npu_network_cmd *cmd = NULL; mutex_lock(&host_ctx->lock); **cmd = kmem_cache_zalloc(ctx->network_cmd_cache, GFP_KERNEL);** mutex_unlock(&host_ctx->lock); wait_for_npu_firmware(); mutex_lock(&host_ctx->lock); **kmem_cache_free(ctx->network_cmd_cache, cmd);** mutex_unlock(&host_ctx->lock);

A really constrained allocation primitive:

We can't Allocate a large number of npu_network_cmd objects and keep this large number of objects unreleased for a while.

## Slide 35

#### Advancing Towards a More Effective Cross-Cache Attack

Challenge 1: How to discard the victim order-0 slab under a constrained allocation primitive

Well, we found another kernel object sharing the same kmem_cache IPA_TX_PKT_WRAPPER because of SLAB Merging: From msm_cvp driver:

struct msm_cvp_frame { struct list_head list; struct msm_cvp_list bufs; u64 ktid; };

System privilege required to access the driver 

So we can't even discard the victim order-0 slab with the old method

## Slide 36

#### Advancing Towards a More Effective Cross-Cache Attack

Solving Challenge1: Discard the empty slab in a Race way

The slab move primitive: move the cpu slab from one cpu to another cpu’s percpu partial list

## Slide 37

#### Advancing Towards a More Effective Cross-Cache Attack

Solving Challenge1: Discard the empty slab in a Race way

The slab move primitive: move the cpu slab from one cpu to another cpu’s percpu partial list

**Example** :move cpu slab of cpu#1 into the percpu parital list of cpu#0

**Step1** . Pin the task on cpu#1 **Step2** . Make cpu slab of cpu#1 full by allocating OBJS_PER_SLAB objects

## Slide 38

#### Advancing Towards a More Effective Cross-Cache Attack

Solving Challenge1: Discard the empty slab in a Race way The slab move primitive: move the cpu slab from one cpu to another cpu’s percpu partial list

**Example** :move cpu slab of cpu#1 into the percpu parital list of cpu#0

**Step1** . Pin the task on cpu#1 **Step2** . Let cpu slab of cpu#1 become full by allocating OBJS_PER_SLAB objects **Step3** . Pin the task on cpu#0

**Step4** . Release all the objects allocated in step2. The “slab move” happens（The move would happen when the first object of the full slab get released）

With the help of slab move primitive, we can put one more slab into the cpu partial list of target cpu by allocating OBJS_PER_SLAB objects at most!

## Slide 39

Advancing Towards a More Effective Cross-Cache Attack Solving Challenge1: Discard the empty slab in a Race way

###### Repeat the slab move primitive

we can put controllable number of slabs into the percpu partial list of target cpu

## Slide 40

#### Advancing Towards a More Effective Cross-Cache Attack

Solving Challenge1: Discard the empty slab in a Race way

By this new way of putting slabs into the percpu partial list, we can remove the Step3 in common workflow of cross-cache attack, and replace the step9 with "repeating slab move primitive"

Step 3. Allocate around  objs_per_slab  * (1+ cpu_partial ) objects

## Slide 41

Advancing Towards a More Effective Cross-Cache Attack Solving Challenge1: Discard the empty slab in a Race way

Repeating slab move pritimive helps us accomplish discarding of victim slab under a very constrained allocation of objects:

Ideally, we can finish the attack with **only OBJS_PER_SLAB objects** !

However, it's still not good enough for the issue:

We only have the ability to allocate **one** npu_network_cmd object and hold it for a very short time

## Slide 42

#### Advancing Towards a More Effective Cross-Cache Attack

Solving Challenge1: Discard the empty slab in a Race way

Race style slab move primitive:

Task 1

Task N (N > OBJS_PER_SLAB)

Pinned on cpu#1

...

Pinned on cpu#1

struct npu_network_cmd *cmd; mutex_lock(&host_ctx->lock); cmd = **kmem_cache_zalloc** (...); mutex_unlock(&host_ctx->lock);

struct npu_network_cmd *cmd;
mutex_lock(&host_ctx->lock);
cmd =  kmem_cache_zalloc (...);
mutex_unlock(&host_ctx->lock);

mutex_lock(&host_ctx->lock);
kmem_cache_free (..., cmd);
mutex_unlock(&host_ctx->lock);

mutex_lock(&host_ctx->lock);
kmem_cache_free (..., cmd);
mutex_unlock(&host_ctx->lock);

## Slide 43

#### Advancing Towards a More Effective Cross-Cache Attack

Solving Challenge1: Discard the empty slab in a Race way

Race style slab move primitive:

###### Task 1

###### Task N

###### (N > OBJS_PER_SLAB)

OBJS_PER_SLAB tasks can race like this:

Pinned on cpu#1

Pinned on cpu#1

...

struct npu_network_cmd *cmd; struct npu_network_cmd *cmd;
mutex_lock(&host_ctx->lock); mutex_lock(&host_ctx->lock);
cmd =  kmem_cache_zalloc (...); cmd =  kmem_cache_zalloc (...);
mutex_unlock(&host_ctx->lock); mutex_unlock(&host_ctx->lock);
mutex_lock(&host_ctx->lock); mutex_lock(&host_ctx->lock);
kmem_cache_free (..., cmd); kmem_cache_free (..., cmd);
mutex_unlock(&host_ctx->lock); mutex_unlock(&host_ctx->lock);

Pinned on cpu#1 struct npu_network_cmd *cmd;Pinned on cpu#1 mutex_lock(&host_ctx->lock);struct npu_network_cmd *cmd; cmd = kmem_cache_zalloc(...);mutex_lock(&host_ctx->lock); Pinned on cpu#1 mutex_unlock(&host_ctx->cmd = **kmem_cache** _zal **loc** k);(...); struct npu_network_cmd *cmd; mutex_unlock(&host_ctx->lock); mutex_lock(&host_ctx->lock); cmd = **kmem_cache_zalloc** (...); ... mutex_unlock(&host_ctx->lock);

Pinned on cpu#1 mutex_lock(&host_ctx->lock);Pinned on cpu#1 kmem_cache_free(..., mutex_lock(&host_ **c** tx->lock);md); mutex_unlock(&host_ctx->lock); **kmem_cache_free** (..., cmd); Pinned on cpu#1 mutex_unlock(&host_ctx->lock);mutex_lock(&host_ctx->lock); **kmem_cache_free** (..., cmd); ... mutex_unlock(&host_ctx->lock);

**OBJS_PER_SLAB allocations**

## Slide 44

#### Advancing Towards a More Effective Cross-Cache Attack

Solving Challenge1: Discard the empty slab in a Race way

Race style slab move primitive:

Pinned on cpu#1
struct npu_network_cmd *cmd;Pinned on cpu#1
mutex_lock(&host_ctx->lock);struct npu_network_cmd *cmd;
cmd = kmem_cache_zalloc(...);mutex_lock(&host_ctx->lock); OBJS_PER_SLAB
Pinned on cpu#1
mutex_unlock(&host_ctx->cmd =  kmem_cache _zal loc k);(...); allocations lead to A full
struct npu_network_cmd *cmd;
mutex_unlock(&host_ctx->lock);
mutex_lock(&host_ctx->lock); slab created on cpu#1
cmd =  kmem_cache_zalloc (...);
... mutex_unlock(&host_ctx->lock);
Switch any task to cpu#0
Pinned on cpu#1
mutex_lock(&host_ctx->lock);Pinned on cpu#1
kmem_cache_free(..., mutex_lock(&host_ c tx->lock);md);
mutex_unlock(&host_ctx->lock); kmem_cache_free (..., cmd); Pinned on cpu#0 The full slab gets moved
mutex_unlock(&host_ctx->lock);mutex_lock(&host_ctx->lock); from cpu#1 to the percpu
kmem_cache_free(..., cmd);
... mutex_unlock(&host_ctx->lock); partial list of cpu#0

## Slide 45

#### Advancing Towards a More Effective Cross-Cache Attack

Solving Challenge1: Discard the empty slab in a Race way

Model for race style slab move primitive:

Task 1

Task N (N > OBJS_PER_SLAB)

Task for Switching cpu

Pinned on cpu#1

...

Pinned on cpu#1

Pinned on cpu#2

struct npu_network_cmd *cmd; mutex_lock(&host_ctx->lock); cmd = **kmem_cache_zalloc** (...); mutex_unlock(&host_ctx->lock);

struct npu_network_cmd *cmd; mutex_lock(&host_ctx->lock); cmd = **kmem_cache_zalloc** (...); mutex_unlock(&host_ctx->lock);

For (i = 0; i < SWITCH_CPU_NUM; i++) { ( SWITCH_CPU_NUM < OBJS_PER_SLAB) pin Task i to cpu#0 ; }

mutex_lock(&host_ctx->lock); **kmem_cache_free** (..., cmd); mutex_unlock(&host_ctx->lock);

mutex_lock(&host_ctx->lock); **kmem_cache_free** (..., cmd); mutex_unlock(&host_ctx->lock);

Pin task to cpu#1

Pin task to cpu#1

(         Usually race condition blocks us from exploitation, but this time it helps us)

## Slide 46

#### Advancing Towards a More Effective Cross-Cache Attack

Solving Challenge1: Discard the empty slab in a Race way

Race style slab move primitive

###### By adjusting:

- The number of race tasks

- SWITCH_CPU_NUM

- Race time

- Maybe some time window expanding technique ?

###### Move a relatively stable

number of slabs into the percpu parital list of cpu#0

###### Will there be some side effects for the original percpu slabs of cpu#0 ?

Not really. In the worst case, we might allocate SWITCH_CPU_NUM objects on cpu#0, which won't create a full slab on cpu#0, so:

- If any of these objects gets released on cpu#0, no slab move would happen because we are the same cpu

- If any of these objects gets released on cpu#1, no slab move would happen because the slab is not full

With the race style slab move primitive, we can easily all add enough slabs into the percpu partial list, and then succeed in reclaiming the empty slab with a really constrained allocation.

## Slide 47

Advancing Towards a More Effective Cross-Cache Attack The new optimized workflow of cross-cache attack for the issue

Step1. Defragmentation with race style slab move primitive, a **new** slab will be created:

## Slide 48

Advancing Towards a More Effective Cross-Cache Attack The new optimized workflow of cross-cache attack for the issue

Step2. Allocate the victim object

Step3. Trigger the vulnerability(UAF) to release the victim object

## Slide 49

Advancing Towards a More Effective Cross-Cache Attack The new optimized workflow of cross-cache attack for the issue

Step4. Move the victim slab to the percpu partial list of cpu#1. Don't trigger the flushing of percpu partial list

## Slide 50

Advancing Towards a More Effective Cross-Cache Attack The new optimized workflow of cross-cache attack for the issue

Step 5: move the victim slab from the percpu partial list of cpu#1 to cpu#0. Trigger flushing of percpu partial list of cpu#0

Step 6: Heap spray with file array to occupy the victim slab

## Slide 51

#### Advancing Towards a More Effective Cross-Cache Attack

Step2. Cross-cache attack: cross from kmem_cache "IPA_TX_PKT_WRAPPER" to file_array(kmalloc-8k)

Challenge 1
Challenge 2

- Challenge 1: How to discard the victim order-0 slab under a constrained allocation primitive

SOLVED!

- Challenge 2: How to make order-3 slab reuse the order-0 slab deterministically

## Slide 52

Advancing Towards a More Effective Cross-Cache Attack **Challenge 2** : How to make order-3 slab reuse the order-0 slab deterministically

Challenge 1
Challenge 2

## Slide 53

Advancing Towards a More Effective Cross-Cache Attack Pre-knowledge for page allocator (based on kernel 4.14)

A simplified view of page allocator for Android devices:(single pgdata & single zone)

Kernel space alloc_pages()

User space mmap()

## Slide 54

Advancing Towards a More Effective Cross-Cache Attack Pre-knowledge for page allocator (based on kernel 4.14)

Exported by procfs

/proc/pagetypeinfo (unreadable by untrusted app)

## Slide 55

Advancing Towards a More Effective Cross-Cache Attack Pre-knowledge for page allocator (based on kernel 4.14)

Exported by procfs

/proc/zoneinfo (unreadable by untrusted app)

High watermark for zone

Current number of order-0 pages Maxium number of order-0 pages

Specific number of order-0 pages for pcplist shrink or bulk

## Slide 56

Advancing Towards a More Effective Cross-Cache Attack Pre-knowledge for page allocator (based on kernel 4.14)

Charactoristic of pcplist

- Order-0 allocation and releasing will use pcplist first, stack-liked way

- • Flushing for the pcplist: flush from tail

## Slide 57

#### Advancing Towards a More Effective Cross-Cache Attack

Pre-knowledge for page allocator (based on kernel 4.14)

continue_merging:

Deterministic page merging:

while (order < max_order - 1) {

Page allocator tends to merge low-order pages to high-order pages when low-order pages gets reclaimed into free_area.

buddy_pfn = __find_buddy_pfn(pfn, order); buddy = page + (buddy_pfn - pfn);

if (!pfn_valid_within(buddy_pfn))

…

goto done_merging;

- if (!page_is_buddy(page, buddy, order)) goto done_merging;

/*

static inline void __free_one_page(struct page *page, unsigned long pfn, struct zone *zone, unsigned int order, int migratetype)

* Our buddy is free or it is CONFIG_DEBUG_PAGEALLOC guard page, * merge with it and move up one order. */

if (page_is_guard(buddy)) { clear_page_guard(zone, buddy, order, migratetype); } else {

list_del(&buddy->lru);

zone->free_area[order].nr_free--; rmv_page_order(buddy);

}

combined_pfn = buddy_pfn & pfn; page = page + (combined_pfn - pfn); pfn = combined_pfn; order++;

}

## Slide 58

#### Advancing Towards a More Effective Cross-Cache Attack

Solving Challenge2: Deterministic heap shaping

Step1: Pin task on cpu#0

Step2: Allocate a specific number of order-0 pages, the specific number is: maxium number of order-0 pages could be in pcplist. Releasing these pages will definitely trigger the flushing or pcplist later.

Choosing the proper kernel component:

- ➢ ION

###### Requirements for page allocation:

- Able to allocate a large number of order-0 pages

- Allocated from UNMOVALE free_area

- ➢ Pipe

- ➢ Socket

- ➢ GPUs(kgsl)

...

- ➢ ION: releasing pages asynchronously

###### Requirements for page releasing:

- Synchronized releasing(No cpu switching)

- ➢ **_Pipe_**

- ➢ Socket

- ➢ GPUs(kgsl):releasing pages asynchronously

...

## Slide 59

Advancing Towards a More Effective Cross-Cache Attack Solving Challenge2: Deterministic heap shaping

Step3: allocate a few hundreds of **_physically continuous_** order-0 pages from UNMOVALE free_area

pfn ...

pfn+8

pfn+16

Memory area
pfn+24
...

In-use order-0 page free order-0 page

## Slide 60

#### Advancing Towards a More Effective Cross-Cache Attack

Solving Challenge2: Deterministic heap shaping

Step3: allocate a few hundreds of **_physically continuous_** order-0 pages from UNMOVALE free_area

...

Memory area ...

###### Choosing the proper kernel component:

###### Requirements for page allocation:

- Able to allocate a large number of order-0 pages

- Allocated from UNMOVALE free_area

- Relatively Clean: No other allocation than allocating order-0 pages

- ➢ ION

- ➢ Pipe

- ➢ Socket

- ➢ GPUs(kgsl)

- ...

###### Requirements for page releasing:

- Synchronized releasing

- Able to release pages partially

- ➢ ION: releasing pages asynchronously

- ➢ **_Pipe_**

- ➢ Socket

- ➢ GPUs(kgsl):releasing pages asynchronously

...

## Slide 61

Advancing Towards a More Effective Cross-Cache Attack Solving Challenge2: Deterministic heap shaping

Step3: allocate a few hundreds of **_physically continuous_** order-0 pages from UNMOVALE free_area

Page allocation and releasing with pipe:

Allocating order-0 page when writing pipe:

###### Releasing order-0 page when reading pipe:

pipe_write(struct kiocb *iocb, struct iov_iter *from)

{

static void anon_pipe_buf_release(struct pipe_inode_info *pipe, struct pipe_buffer *buf)

{

if (bufs < pipe->buffers) {

int newbuf = (pipe->curbuf + bufs) & (pipe->buffers-1); struct pipe_buffer *buf = pipe->bufs + newbuf; struct page *page = pipe->tmp_page; int copied;

if (!page) {

**page = alloc_page** (GFP_HIGHUSER | __GFP_ACCOUNT); if (unlikely(!page)) {

ret = ret ? : -ENOMEM; break;

} }

pipe->tmp_page = page;

struct page *page = buf->page;

###### /*

- If nobody else uses this page, and we don't already have a * temporary page, let's keep track of it as a one-deep * allocation cache. (Otherwise just release our reference to it)

*/

if (page_count(page) == 1 && !pipe->tmp_page)

pipe->tmp_page = page;

else

**put_page(page);**

}

(The very first page won't be released, so we need to pre-allocated it before the heap shaping)

## Slide 62

Advancing Towards a More Effective Cross-Cache Attack Solving Challenge2: Deterministic heap shaping

Step3: allocate a few hundreds of **_physically continuous_** order-0 pages from UNMOVALE free_area Memory area ... ... Owned by pipe_n Owned by pipe_n+1 Owned by pipe_n+2 Step4: Create order-o page holes by releasing one order-0 page every 8 order-0 pages Memory area ... ... Owned by pipe_n+1 Owned by pipe_n+2 Owned by pipe_n

order-0 page hole

## Slide 63

Advancing Towards a More Effective Cross-Cache Attack Solving Challenge2: Deterministic heap shaping

Pcplist of cpu#0 would be like:

... pcplist

...

order-0 page hole

## Slide 64

Advancing Towards a More Effective Cross-Cache Attack Solving Challenge2: Deterministic heap shaping

Step5. Trigger the step1 in “new optimized workflow of cross cache attack for the issue”

The optimized workflow of cross cache attack for the issue:

Step1. Defragmentation with race style slab move primitive, a **new** slab will be created:

Empty slab comes from order-0 page holes

## Slide 65

Advancing Towards a More Effective Cross-Cache Attack Solving Challenge2: Deterministic heap shaping

Step5. Trigger the step1 in “new optimized workflow of cross cache attack for the issue”

Memory area
... ...
Owned by pipe_n+1 Owned by pipe_n+2
Owned by pipe_n

order-0 page hole New slab(victim slab)

## Slide 66

#### Advancing Towards a More Effective Cross-Cache Attack

Solving Challenge2: Deterministic heap shaping

Step6. Occupy all the other order-0 page holes, except the one has been used as new slab

###### Choosing the proper kernel component:

Requirements for page allocation:

- Able to allocate a large number of order-0 pages

- Allocated from UNMOVALE free_area

➢ **ION**

- ➢ Pipe

- ➢ Socket

- ➢ GPUs(kgsl)

...

Memory area

...

Owned by pipe_n+2

Owned by pipe_n+1

Owned by pipe_n

order-0 page hole ION occupied page New slab

## Slide 67

Advancing Towards a More Effective Cross-Cache Attack Solving Challenge2: Deterministic heap shaping

Step7. Finish the step2 ~ step5 of “new optimized workflow of cross cache attack for the issue” After the step5 of "optimized workflow of cross cache attack for the issue", the victim slab will be reclaimed to page allocator:

reclaimed to page allocator:
Memory area
...
Owned by pipe_n+1 Owned by pipe_n+2
Owned by pipe_n

order-0 page hole ION occupied page released victim slab Pcplist of cpu#0 would be like: ... pcplist

## Slide 68

Advancing Towards a More Effective Cross-Cache Attack Solving Challenge2: Deterministic heap shaping

Step8. Release all the pages owned by the pipe

...

Memory area ...

There must be one and only one order-3 pages here, and released victim slab must be in it!

order-0 page hole released victim slab

ION occupied page free order-0 page

Pcplist of cpu#0 would be like:

... ...
pcplist

## Slide 69

Advancing Towards a More Effective Cross-Cache Attack Solving Challenge2: Deterministic heap shaping

Step9. Release all the pages created in step2 to forse the flushing of pcplist

Victim slab and other order-0 pages are reclaimed into free_area, page merging will happen because of "Deterministic page merging"

...
Order-3 pages

Memory area ...

Step10. Heap spray lots of file array to occupy the order-3 pages where victim slab lies

## Slide 70

Advancing Towards a More Effective Cross-Cache Attack Solving Challenge2: Deterministic heap shaping

In actual practice, the success rate of the entire utilization largely depends on step 3:

How?

Step3: allocate a few hundreds of **_physically continuous_** order-0 pages from UNMOVALE free_area

## Slide 71

#### Advancing Towards a More Effective Cross-Cache Attack

Detect status of page allocator in a side-channel way

If we keeps on allocate order-0 pages with "__GFP_KSWAPD_RECLAIM" flag enabled from UNMOVALBE free_area:

State 1:allocated from pcplist first State 2:pcplist become empty, Unmovable free_area will be used: Start from low-order

(1)
(2)

## Slide 72

Advancing Towards a More Effective Cross-Cache Attack Detect status of page allocator in a side-channel way

If we keeps on allocate order-0 pages with "__GFP_KSWAPD_RECLAIM" flag enabled from UNMOVALBE free_area:

State3: If Unmovable free_area becom empty, other migration type free_areas will be used for allocation acording to fallback list

Wake up kswapd for reclaiming pages if free pages of zone is under High watermark.

(3)

static int fallbacks[MIGRATE_TYPES][4] = { [MIGRATE_UNMOVABLE] = { MIGRATE_RECLAIMABLE, MIGRATE_MOVABLE, MIGRATE_TYPES },

…... };

## Slide 73

Advancing Towards a More Effective Cross-Cache Attack Detect status of page allocator in a side-channel way

If we keeps on allocate order-0 pages with "__GFP_KSWAPD_RECLAIM" flag enabled from UNMOVALBE free_area:

State 4: If other migration type free_areas becom empty, then enter the slow path for allocating order-0 page:

- Wake up kswpad for reclaiming pages

- Direct reclaim

...

## Slide 74

Advancing Towards a More Effective Cross-Cache Attack Detect status of page allocator in a side-channel way

If we keeps on allocate order-0 pages with "__GFP_KSWAPD_RECLAIM" flag enabled from UNMOVALBE free_area:

   - LRU_INACTIVE_ANON

- Reclaming pages:

- Wake up kswpad for reclaiming pages

- • direct reclaim

- LRU_INACTIVE_FILE

- LRU_ACTIVE_ANON

- LRU_ACTIVE_FILE

- shrinker_list

## Slide 75

Advancing Towards a More Effective Cross-Cache Attack Detect status of page allocator in a side-channel way

Exported by /proc/meminfo, accessable from untrusted app:

- LRU_ACTIVE_ANON

- LRU_INACTIVE_ANON

- LRU_ACTIVE_FILE

- LRU_INACTIVE_FILE

- shrinker_list

## Slide 76

#### Advancing Towards a More Effective Cross-Cache Attack Detect status of page allocator in a side-channel way

Get reduced frequently Page allocator might be in State 3 or State 4

Unmovable free_area is almost empty!

## Slide 77

#### Advancing Towards a More Effective Cross-Cache Attack

Detect status of page allocator in a side-channel way

Tested on the device with kernel 4.14:

/proc/pagetypeinfo:

## Slide 78

#### Advancing Towards a More Effective Cross-Cache Attack

Strategy for allocating a few hundreds of **_physically continuous_** order-0 pages from UNMOVALE free_area:

Step1: reserve a dozen of order-8/9 pages with ION

#if defined(CONFIG_IOMMU_IO_PGTABLE_ARMV7S) static const unsigned int orders[] = {8, 4, 0}; #else static const unsigned int orders[] = {9, 4, 0}; #endif

Step2: Create and detect the empty state of Unmovable free_area:

2.1: Consume a large memory from both Unmoable free_area and Movable free_area. This will put memory of zone under pressure(for example, under High watermark )

Allocate_large_memory _with_ION(); // Consume a large memory from both Unmoable free_area Allocate_large_memory_with_mmap(); // Consume a large memory from both Moable free_area

2.2: Run the circle to detect the empty state of Unmovable free_area

While (1) { Allocate_a_few_order0_pages(); Detect_page_allocator_state_by_watching_meminfo(); If (page_allocator_enter_state_3_or_4) {

break; }

}

## Slide 79

#### Advancing Towards a More Effective Cross-Cache Attack

Strategy for allocating a few hundreds of **_physically continuous_** order-0 pages from UNMOVALE free_area:

Step3: release the order-8 pages with ION

Step4: allocate some order-0 pages to reduce the noise

Step5: allocate a few hundreds of **_physically continuous_** order-0 pages from UNMOVALE free_area

## Slide 80

Advancing Towards a More Effective Cross-Cache Attack Strategy for allocating a few hundreds of **_physically continuous_** order-0 pages from UNMOVALE free_area:

Step5: allocate a few hundreds of order-0 pages from UNMOVALE free_area

The order-0 page comes from the spliting of high-order pages:

Allocated page

Order:

Order:

Original state of Unmovable free_area

Allocate one order-0 page

So these order-0 pages will be **_physically continuous_**

## Slide 81

#### Advancing Towards a More Effective Cross-Cache Attack

- Challenge 2: How to make order-3 slab reuse the order-0 slab deterministically

Challenge 1
Challenge 2

- Challenge 1: How to discard the victim order-0 slab under a constrained allocation primitive

SOLVED!

- Challenge 2: How to make order-3 slab reuse the order-0 slab deterministically SOLVED!

## Slide 82

### Exploit File UAF with Dirty Pagetable

2
1

1: Use the old method to discard the victim filp slab

2: Occupy the released victim filp slab with user page table by heap spraying many user page tables

## Slide 83

### Exploit File UAF with Dirty Pagetable

Step1. Use the mentioned method to make Unmovable free_area become almost empty

Step2. Discard the victim filp slab

The occupation is more likely to succeed because the free_area is relatively clean.

Step3. Heap spray many user page tables to occupy the released victim filp slab.

## Slide 84

### Exploit File UAF with Dirty Pagetable

Adapt Dirty Pagetable to Samsung Device

Mitigations on Samsung Device:

- Physical KASLR

- • RO kernel text

Not working :( Construct physical AARW with Dirty Pagetable: <u>https://yanglingxi1993.github.io/dirty_pagetable/dirty_pagetable.html</u>

## Slide 85

### Exploit File UAF with Dirty Pagetable

Adapt Dirty Pagetable to Samsung Device

Corrupt kernel object to construct AARW

## Slide 86

### Exploit File UAF with Dirty Pagetable

Adapt Dirty Pagetable to Samsung Device

Corrupt pipe_buffer to construct AARW

- ⚫ Make the page of pipe buffer follow the page owned by ION: Using the similar technique for allocating physically continuous order-0 pages.

## Slide 87

Exploit File UAF with Dirty Pagetable Adapt Dirty Pagetable to Samsung Device

Corrupt kernel object to construct virtual AARW

- ⚫ Make the page of pipe buffer follow the page owned by ION: Using the similar technique for allocating physically continuous order-0 pages.

- ⚫ victim_pte += 0x1000

for(int i = 0; i < 0x1000; i++) { dup(victim_fd); }

- ⚫ Using pipe primitive to construct AARW!

## Slide 88

### Bypass SELinux in Samsung device

##### Attack global data used in "security_compute_av()":

void security_compute_av(u32 ssid,

u32 tsid, u16 orig_tclass, struct av_decision *avd, ...)

{

u16 tclass;

static void map_decision(u16 tclass, struct av_decision *avd, int allow_unknown) {

if (tclass < current_mapping_size) { unsigned i, n = current_mapping[tclass].num_perms; u32 result;

struct context *scontext = NULL, *tcontext = NULL;

read_lock(&policy_rwlock); avd_init(avd); xperms->len = 0; if (!ss_initialized) goto allow;

for (i = 0, result = 0; i < n; i++) { if (avd->allowed & current_mapping[tclass].perms[i]) result |= 1<<i;

if (allow_unknown && !current_mapping[tclass].perms[i]) result |= 1<<i;

}

avd->allowed = result;

tclass = unmap_class(orig_tclass);

context_struct_compute_av(scontext, tcontext, tclass, avd, xperms); map_decision(orig_tclass, avd, policydb.allow_unknown);

}

... }

out:

read_unlock(&policy_rwlock); return;

allow:

avd->allowed = 0xffffffff; goto out;

}

## Slide 89

### Win The Game

- System privilege required

- • Less than 10% success rate

- Attack from Untrusted App

- • ~65%(13/20) success rate

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Win The Game
e System privilege required
e Less than 10% success rate
10:49 08 %4100%8
ao1
‘data/user/0/jackpal.androidterm/app_HOME $
: /data/user/0/jackpal.androidterm/app_HOME $ id
luid=10284(u0_a284) gid=10284(u0_a284) groups=10284(u0_a284),
[3003 (inet ) ,9997( everybody), 20284 (uC |_cache) ,50284(al1_a2]
84) context=u:r:untrusted_app_25:50:c512,c76
/data/user/0/jackpal.androidterm/app_HOME $
/data/user /0/jackpal.androidterm/app_HOME $ getenforce
etenforce: Couldn't get enforcing status: Permission den
/data/user/0/jackpal.androidterm/app_HOME $
p ro.build. fingerprint <
24 .014/69810ZCU4HWDT : user /rel
/data jackpal.androidterm/app_HOME $
/data/user /0/jackpal.androidterm/app_HOME $ ./poc
(LLLLLLLLLLLLLLL LLL cd
qi #
Game of Cross Cache #
#
TO CLLULULLLLLLCLLLLL Lab ceeu bacco occcad
10, epoll_fd:11
fd:9124
map_buf_ioct1.npu_phys_addr: ff fff000
req.network_hdl: 10001
prepare_alloc_new_slab is done
prepare_gen_mov_slab is done
unload thread: 10
active_candidate:2681644
active_candidate: 2681856
em gets quite maybe
finsihed running out kmalloc-8k
[+] try running out the cached pages in ion-pool to reduce nf
loise
[+] old kreclaim: 133356
[+] new kreclaim: 133396
[+] finished creating high-order pag
[+] Try to construct and detect kernel shrink action... (may|
take a while)
value for evaluating the reclaiming
value for evaluating the reclaiming
value for evaluating the reclaiming
value for evaluating the reclaiming
value for evaluating the reclaiming:
value for evaluating the reclaiming
value for evaluating the
¢ Attack from Untrusted App
value for evaluating the reclaiming
value for evaluating the reclaiming
value for evaluating the reclaiming
value for evaluating the reclaiming
value for evaluating the reclaiming
value for evaluating the reclaiming
value for evaluating the reclaiming
value for evaluating the reclaiming
value for evaluating the reclaiming
value for evaluating the reclaiming
value for evaluating the reclaiming
value for evaluating the reclaiming
Unmovable free_area should be almost empty now
5 dma-buf fd
Detected the kernel shrink!
finish the victim slab discard
the victim filp slab should have been discarded, wal
the file release
[+] finished the pagetable heaping
[+] start the Dirty Pagetable
[+] eased the memory wait for a whil
[+] to perform dup()*0x1000, we might get into a dead loop
[+] found the evil vaddr
[+] evil_vaddr:Oxbfaf9000, dup vaddr :Oxbfb29
, mark: Oxdead}
[+] munmap() the evil_vaddr
[+] remap the evil_vaddr with dma_buf fd
[+] init the pipe buffer
[+] to the leak pipe buffer
[+] try to flush pte cache
[+] leaked data
[+] addr: oxbfafs content: fff fffbf0994bdcO
[+] addr content :8300000000
[+] addr: Oxbfaf9010, content: ffffff8009b42900
[+] we might have catch one pipe buffer at Oxbfaf9000
[+] Yes! We catch the pipe buffer
pipe page: Oxf fffffbfo994bdc0, pipe ops:0xffffff8009b4290}
kas1r: 120000
pipe page: ffffffbfos94bdc0, vaddr: ffffffc2652f7000, len:|
31
vil_pipe_fds[0]:172, evil_pipe_fds(1]:173
finish writing the reject_allow_unknown_vaddr
selinux_map_mapping: Oxf fffffc267e48000, selinu
[+] finish overwriting the selinux_map_mapping
[+] reverse shell should be ready now !!!
nect to root shell with cmd: /system/bin/toybox netca}
1 -p 1234 -L
10:50 BO®
cat /proc/iomem
100100000-002ef FFF
lo0408000-004
100784000-0
00800
lo0980000-'
100984000
Joosgsod
loo9940
1009c0000-009c 1fff
looasso
)a8c000-00a8f fff
100ac0000-00ac 1 fff
10188101c-0188101f
101881024-01881027
101881028-0188102b
10188103c-0188103f
101882014-01882017
101d84000-01d86fff
101d87000-01d87dff
101d90000-01d97f ff
103d00000-03d3f fff
103d90000-03d98f ff
100-O3daf ftF
103dc2200-03de2207
103dc2208-03dc220f
06002000-06002fFF
106004000-06004f ff
06004000-06004f FF
106005000-06005f fF
06005000-06005f ff
106010000-06010f Ff
06010000-o6010f ff
10601 1000-06011 FFF
06011000-06011f fF
106012000-06012F ff
06012000-06012f ff
106013000-06013f FF
06013000-06013f fF
106014000-06014f FF
06014000-06014f fF
* ~65%(13/20) success rate
qcom, ipcc@408000
afprom@780000
12¢@880000
i2c@884000
qcom, qupv3.
12¢@980000
984000
2988000
i2¢@994000
qcom, qupv
i2¢@a88000
100
7m, qupv3_1_geni_se@ac0000
tatus
geni_se@8c0000
se@9c0000
sp2:
mb.
mb, spare2
ufs
phy_mem
ufs_ice
kgs1-3d0
cc_base
base
status-reg
status-reg
base
base
stm-base
funnel-base
funnel-base
cti-base
cti-base
cti-base
cti-base
ti-base
cti-base
ti-base
O
```

## Slide 90

### Mitigations for Cross-cache Attack

SLAB_VIRTUAL: <u>https://github.com/thejh/linux/commit/bc52f973a53d0b525892088dfbd251bc934e3ac3</u>

Kill the Game!

## Slide 91

### Summary

- ➢ Advancing Towards a More Effective Cross-Cache Attack

   - Solve the challenge 1: Discard the victim order-0 slab under a really limitation allocation primitive

   - Solve the challenge 2: How to make order-3 slab reuse the order-0 slab deterministically

- ➢ Dirty Pagetable on Samsung Device

# BHASIA @BlackHatEvents

## Slide 92

### Acknowledgements Ye Zhang, Teacher Jin

# BHASIA @BlackHatEvents

## Slide 93

# Q&A

# BHASIA @BlackHatEvents
