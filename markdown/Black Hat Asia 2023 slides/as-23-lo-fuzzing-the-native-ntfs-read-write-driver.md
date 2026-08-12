---
title: "Fuzzing the Native NTFS Read Write Driver"
speakers: ["Lo"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2023"
edition: "ASIA"
year: 2023
source_pdf: "Black Hat Asia 2023 slides/AS-23-Lo-Fuzzing-the-Native-NTFS-Read-Write-Driver.pdf"
pages: 33
sha256: "b942d6a681cb6f02f40fbc6d0e72f5ec71824bcfe8b793c57354e1a964765766"
text_chars: 15099
ocr_pages: 6
has_ocr: true
redacted_secrets: 0
ocr_confidence: 87.6
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T01:51:14Z"
---
# Fuzzing the Native NTFS Read Write Driver

**Speakers:** Lo  
**Conference:** Black Hat ASIA 2023  
**Source:** `Black Hat Asia 2023 slides/AS-23-Lo-Fuzzing-the-Native-NTFS-Read-Write-Driver.pdf` (33 pages)


## Slide 1

# Fuzzing the Native NTFS Read-Write Driver in the Linux Kernel

Edward Lo, Chiachih Wu

#BHASIA @BlackHatEvents

> Text below was recovered by OCR (confidence 93/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
ASIA &
MAY 11-12
BRIEFINGS
Fuzzing the Native NTFS Read-Write
Driver in the Linux Kernel
Edward Lo, Chiachih Wu
#BHASIA @BlackHatEvents
```

## Slide 2

## Agenda

- About us

- Motivation

- Linux file system 101

- Challenges to file system fuzzing

- Papora – the efficient file system fuzzer for NTFS

- Evaluation

- Takeaways

#BHASIA @BlackHatEvents

## Slide 3

## About Us

- Edward Lo

   - Security researcher at Amber Group

   - Survey and apply feasible fuzzing technology to blockchain clients

   - Internal auditing on blockchain projects

- Chiachih Wu (@chiachih_wu)

   - Head of web3 security team at Amber Group

   - Blockchain security auditing/researching

   - Blockchain data analytics

#BHASIA @BlackHatEvents

## Slide 4

## Motivation

- NTFS3 was firstly upstreamed to Linux kernel in late 2021

- A new file system is complicated enough to have some bugs

- Existing fuzzers cannot efficiently fuzz a new file system

#BHASIA @BlackHatEvents

## Slide 5

## NTFS

- New Technology File System (NTFS)

   - A proprietary journaling file system developed by Microsoft

   - Default file system of the Windows NT family starting NT 3.1

- There are ways to work with NTFS from Linux

   - NTFS: an old implementation that supports read and limited write on NTFS drive

   - NTFS-3G: a full-featured, R/W FUSE (Filesystem in Userspace) package

   - NTFS3: a fully functional R/W NTFS driver, upstreamed in Linux kernel v5.15

#BHASIA @BlackHatEvents

## Slide 6

## File System

file operations

mount image

file system

#BHASIA @BlackHatEvents

## Slide 7

## Attack Vectors

crafted parameter

malformed image

file system

#BHASIA @BlackHatEvents

## Slide 8

Choosing a Weapon
AFL Syzkaller
?
Hongg
Trinity
Fuzz
file system
Real
? VM
machine
#BHASIA

#BHASIA  @BlackHatEvents

## Slide 9

## Janus

- A coverage-driven fuzzer that efficiently and effectively test images and file operations in a joint manner (published in IEEE S&P '19)

- However, we can’t use it for our target file system (NTFS)

   - Need a specific image parser for NTFS (more about it later)

   - The library (Linux kernel library) used by executor was obsolete (v5.3) and inactive at the surveying time

   - KASAN patch integration and modification for the evolving new kernel

#BHASIA @BlackHatEvents

## Slide 10

## Challenges to Image Fuzzing

- Images are large

   - Only metadata matters

   - Mutation on user data is basically a waste of time

- Each file system has its own metadata structure design

   - Need to develop a specific parser for the file system

- Checksums

   - Corrupted after mutation, which could lead to mount fails

#BHASIA @BlackHatEvents

## Slide 11

## Challenges to Image Fuzzing - NTFS

### • NTFS image format

#### Partition Boot Sector

PBS

#### Master File Table

MFT

User data

|Offset|Field|Remark|
|---|---|---|
|0x00|jump code|Jump to boot code|
|0x03|OEM ID|“NTFS    “|
|0x0B|Bytes per sector||
|0x0D|Sectors per cluster||
|…|…|…|
|0x01FE|End of sector mark|value = 0xAA55|

|Entry|File name|Purpose|
|---|---|---|
|0|$MFT|Metadata for all files|
|1|$MFTMirr|Duplicate of the first
4 entries of $MFT|
|2|$LogFile|Transaction log|
|3|$Volume|Volume information|
|…|…|…|
|26|$Extend\$Reparse|Reparse point data|

#BHASIA @BlackHatEvents

## Slide 12

## Challenges to Image Fuzzing - PBS

OEM ID must equal “NTFS    “ (4 spaces) Sector size >= 512 and must be a power of 2

Cluster size must be a power of 2

More sanity checks…

#BHASIA @BlackHatEvents

## Slide 13

## Challenges to Image Fuzzing - MFT

- The unit of disk space that NTFS uses is a cluster, which is a collections of sectors

Sector Sector … Sector
Cluster

- NTFS applies a concept – fixup, to protect the integrity of some important metadata

   - FILE Records in the $MFT

   - INDX Records in directories and other indexes

   - RCRD Records in the $LogFile…and other critical metadata

#BHASIA @BlackHatEvents

## Slide 14

## Fixup – Write

|Offset|Data|Description|
|---|---|---|
|0x00|…|Metadata header|
|0x30|0x12|0x34 | 0x00 | 0x00 | 0x00 | 0x00 ||0x00 | 0x00
0x30-0x31: update sequence number
0x32- : update sequence array|
|0x1F8|0x11 | 0x12 | 0x13 | 0x14 | 0x15 | 0x16 ||0x17|0x18
End of sector 1|
|0x3F8|0x21 | 0x22 | 0x23 | 0x24 | 0x25 | 0x26 ||0x27|0x28
End of sector 2|
|0x5F8
…|0x31 | 0x32 | 0x33 | 0x34 | 0x35 | 0x36 |
…|0x37|0x38
End of sector 3
…|

### Before write

1. Update Sequence Number + 1 2. Copy last 2 bytes of each sector into the update sequence array

3. Write the new USN to the end of each sector

4. Write back to disk

|Offset|Da|ta|Description|
|---|---|---|---|
|0x00||…|Metadata header|
|0x30
0x12|0x35 | 0x17||0x18||0x27|0x28||0x37|0x38
0x30-0x31: update sequence number
0x32- : update sequence array|
|0x1F8
0x11 | 0x12 | 0x13|| 0x14 ||0x15 | 0x16 ||0x12|0x35
End of sector 1|
|0x3F8
0x21 | 0x22 | 0x23|| 0x24 ||0x25 | 0x26 ||0x12|0x35
End of sector 2|
|0x5F8
0x31 | 0x32 | 0x33|| 0x34 ||0x35 | 0x36 ||0x12|0x35
End of sector 3|

#BHASIA @BlackHatEvents

## Slide 15

## (Cont'd)

#BHASIA @BlackHatEvents

> Text below was recovered by OCR (confidence 90/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
ASIA 20253
(Cont'd)
ul6 ff = lel6 to cpu(rhdr->fix off);
ul6 fn lel6 to cpu(rhdr->fix_num);
fn * SECTOR SIZE > bytes) {
return false;
}
/* Get fixup pointer. */
fixup = Add2Ptr(rhdr, ff);
if (*fixup >= FFF)
*fixup = 1;
else
*fixup += 1;
sample = *fixup;
ptr = Add2Ptr(rhdr, SECTOR SIZE - sizeof(short));
while (fn--) {
*++fixup = *ptr;
*ptr = sample;
ptr += SECTOR SIZE / sizeof(short);
}
return
```

## Slide 16

## Fixup – Read

|Offset|Data|Description|
|---|---|---|
|0x00|…|Metadata header|
|0x30|0x12|0x35 |0x17|0x18|0x27|0x28||0x37|0x38
0x30-0x31: update sequence number
0x32- : update sequence array|
|0x1F8|0x11 | 0x12 | 0x13 | 0x14 | 0x15 | 0x16 ||0x12|0x35
End of sector 1|
|0x3F8|0x21 | 0x22 | 0x23 | 0x24 | 0x25 | 0x26 ||0x12|0x35
End of sector 2|
|0x5F8
…|0x31 | 0x32 | 0x33 | 0x34 | 0x35 | 0x36 |
…|0x12|0x35
End of sector 3
…|

||Offset|Data|Description|
|---|---|---|---|
|After read|0x00|…|Metadata header|
|1.
Compare the USN against last 2 bytes of|0x30|0x12|0x35| 0x17|0x18|0x27|0x28||0x37|0x38
0x30-0x31: update sequence number|
|each sector, make sure they are the same|||0x32- : update sequence array|
|2.
Check fail could mean a bad sector, disk
corrution or sstem error|0x1F8|0x11 | 0x12 | 0x13 | 0x14 | 0x15 | 0x16 ||0x17|0x18
End of sector 1|
|p  y
3.
Copy the corresponding fixup back to the|0x3F8|0x21 | 0x22 | 0x23 | 0x24 | 0x25 | 0x26 ||0x27|0x28
End of sector 2|
|last 2 bytes of each sector|0x5F8|0x31 | 0x32 | 0x33 | 0x34 | 0x35 | 0x36 ||0x37|0x38
End of sector 3|

#BHASIA @BlackHatEvents

## Slide 17

## (Cont'd)

#BHASIA @BlackHatEvents

> Text below was recovered by OCR (confidence 90/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Q
black hat
ASIA 20253
(Cont'd)
lel6 to cpu(rhdr->fix_off);
simple ? ((bytes >> SECTOR SHIFT) + 1)
lel6 to cpu(rhdr->fix_num) ;
Check errors. */
((i@ & 1) |] + fn * sizeof(short) > SECTOR SIZE || !fn-- ||
fn * SECTOR SIZE > bytes) {
return -EINVAL; /* Native chkntfs returns ok! */
}
/* Get fixup pointer. */
fixup = Add2Ptr(rhdr, fi);
sample = *fixup;
ptr = Add2Ptr(rhdr, SECTOR SIZE - sizeof(short));
ret ;
while (fn--) {
/* Test current word. */
if (*ptr != sample) {
/* Fixup does not match! Is it serious error? */
ret = -E NTFS FIXUP;
}
/* Replace fixup. */
*ptr = *++fixup;
ptr += SECTOR SIZE / sizeof(short);
}
return ret;
```

## Slide 18

## Papora Image Parser

metadata
metadata
image  image
extract meatadata
userdata
mutation mutator
parser
seed image
metadata
metadata
LibOS
mount image
userdata
executor
seed image

#BHASIA @BlackHatEvents

## Slide 19

## Challenges to Syscall Fuzzing

- What to generate

   - system calls for file operations

- How to mutate

   - The fuzzer should know how to mutate each arguments of the system calls

   - A valid **_fd_** , combination of flags, pre-allocated buffers …

- Context awareness

   - The context should be maintained across each system calls

int fd = open(“papora.seed”, …); read(fd, buf, 256); close(fd);

#BHASIA @BlackHatEvents

## Slide 20

## Papora Syscall Fuzzer

mutate
seed  LibOS
syscall
deserialize
fuzzer executor
program
variables
generate
syscalls
file objects
serialized
program
(testcase)

#BHASIA @BlackHatEvents

## Slide 21

## Challenges to Executor

Speed Fast Slow Scalability Buy more devices ($) Spawn more VM Management Hard Easy <u>(reboot / debug / etc)</u> Risk High (bricked) Low (out-of-mem?)

#BHASIA @BlackHatEvents

## Slide 22

## (Cont’d)

LibOS
executor

##### Pros

##### Cons

- •

- Fast execution Since LKL is an arch of Linux, there are

- • Easy management (reboot / debug / etc) some limitations of current implementation,

- • Easy to scale e.g., !MMU / !SMP / etc

- •

- Easy to reproduce (non-aging kernel) Kernel upgrading effort

#BHASIA @BlackHatEvents

## Slide 23

## Papora Workflow

seed image image parser
seed program image mutator
Initial corpus
syscall fuzzer
Fuzzing engine
upgraded
kernel
LibOS new coverage
new corpus
executor
KASAN
integration
crash case

#BHASIA @BlackHatEvents

## Slide 24

## Evaluation

|• Run Syzkaller for 1 month with the customized syz-lang|descript|ion||
|---|---|---|---|
|• Constrain the system calls to file operations only|Commit|Bug Type|Root Cause|
|• No interesting outcome|0b66046|NPD|Sanity check miss|
||e19c627|OOB Read|Arithmetic overflow|
||6db6208|OOB Read|Sanity check miss|
|• Run Papora for 3 months intermittently|2681631|NPD|Sanity check miss|
|• Upgrade LKL whenever new kernel is available (v5.15➔v6.0)|c1ca8ef|NPD|Implementation flaw|
|• Identified 12 issues|4f1dc7d|Heap Corruption|Sanity check miss|
||bfcdbae|OOB Read|Sanity check miss|
||******|OOB Read|Sanity check miss|
||******|Heap Corruption|Type confusion|
|******: not upstreamed|******|OOB Read|Sanity check miss|
|
Type 1: Triggered by image mount|4d42ecd|OOB Read|Sanity check miss|
|Type 2: Triggered by image mount + file operations|54e4570|OOB Write|Sanity check miss|

#BHASIA @BlackHatEvents

## Slide 25

## Case Study – Type 1

##### MFT record

PBS

Attribute array Record Attr #1 Attr #1 Attr #2 Attr #2 Attr Header Header Value Header Value … end

|Offset|Field|Remark|
|---|---|---|
|0x00|jump code|Jump to boot code|
|0x03|OEM ID|“NTFS    “|
|0x0B|Bytes per sector||
|0x0D|Sectors per cluster||
|…|…|…|
|0x40|MFT entry size||

A positive value denotes the number of clusters of a MFT entry. ➔ 0x1 ➔ 1 cluster (bytes per sector x sectors per cluster)

A negative value denotes the number of bytes of a MFT entry, in which case the size is 2 to the power of the absolute value ➔ 0xF6 ➔ -10 → 2<sup>10</sup> = 1024

#BHASIA @BlackHatEvents

## Slide 26

## (Cont’d)

BUG: kernel NULL pointer dereference, address: 0000000000000158

Call Trace:

<TASK>

? ntfs_alloc_inode+0x1a/0x60 attr_load_runs_vcn+0x2b/0xa0 mi_read+0xbb/0x250 ntfs_iget5+0x114/0xd90 ntfs_fill_super+0x588/0x11b0 ? put_ntfs+0x130/0x130 ? snprintf+0x49/0x70

? put_ntfs+0x130/0x130 get_tree_bdev+0x16a/0x260 vfs_get_tree+0x20/0xb0 path_mount+0x2dc/0x9b0 do_mount+0x74/0x90 __x64_sys_mount+0x89/0xd0 do_syscall_64+0x3b/0x90 entry_SYSCALL_64_after_hwframe+0x63/0xcd

#BHASIA @BlackHatEvents

## Slide 27

## (Cont’d)

The record_size is derived by the formula. However, the corresponding record_bits is calculated with the assumption that it’s larger than 256

Say if we have a boot->record_size = 0xF8 = -8 ➔sbi->record_size = 2<sup>8</sup> = 256 ➔sbi->record_bits = 9 So we have a mismatch here, which will lead to a NPD issue

#BHASIA @BlackHatEvents

## Slide 28

## Patch

#BHASIA @BlackHatEvents

> Text below was recovered by OCR (confidence 80/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
ASIA 20253
Patch
diff --git a/fs/ntfs3/super.c b/fs/ntfs3/super.c
index d72a27abfl1c83..af9b7947dfé4e 100644
--- a/fs/ntfs3/super.c
+++ b/fs/ntfs3/super.c
@@ -814,7 +814,7 @@ static int ntfs_init_from_boot(struct super_block *sb, u3?2 sector_size,
: (u32)boot->record_size
<< sbi->cluster_bits;
- if (record_size > MAXIMUM _BYTES_PER_MFT)
+ if (record_size > MAXIMUM_BYTES_PER_MFT || record size < SECTOR_SIZE)
goto out;
sbi->record_bits = blksize bits(record size);
```

## Slide 29

Case Study – Type 2 (CVE-2022-48423)

##### MFT record

MFT

Attribute array Record Attr #1 Attr #1 Attr #2 Attr #2 Attr Header Header Value Header Value … end

|Entry|File name|Purpose|
|---|---|---|
|0|$MFT|Metadata for all files|
|1|$MFTMirr|Duplicate of the first
4 enties of $MFT|
|2|$LogFile|Transation log|
|3|$Volume|Volume information|
|…|…|…|
|26|$Extend\$Reparse|Reparse point data|

#BHASIA @BlackHatEvents

## Slide 30

## (Cont’d)

Allocated by task 255: BUG: KASAN: slab-out-of-bounds in ni_create_attr_list+0x1e1/0x850 kasan_save_stack+0x26/0x50 Write of size 426 at addr ffff88800632f2b2 by task exp/255 ... __kasan_kmalloc+0x88/0xb0 Call Trace: __kmalloc+0x192/0x320 <TASK> ni_create_attr_list+0x11e/0x850 ni_ins_attr_ext+0x52c/0x5c0 dump_stack_lvl+0x49/0x63 ... ni_insert_attr+0x1ba/0x420 ni_insert_resident+0xc0/0x1c0 kasan_report+0xa7/0x130 … ntfs_set_ea+0x6bf/0xb30 ntfs_setxattr+0x114/0x5c0 memcpy+0x3c/0x70 __vfs_setxattr+0xda/0x120 ni_create_attr_list+0x1e1/0x850 ... __vfs_setxattr_noperm+0x93/0x300 __vfs_setxattr_locked+0x141/0x160 ni_ins_attr_ext+0x52c/0x5c0 ... vfs_setxattr+0x128/0x300 do_setxattr+0xb8/0x170 ni_insert_resident+0xc0/0x1c0 ... setxattr+0x126/0x140 path_setxattr+0x164/0x180 ntfs_setxattr+0x114/0x5c0 ... __x64_sys_setxattr+0x6d/0x80 do_syscall_64+0x3b/0x90 vfs_setxattr+0x128/0x300 entry_SYSCALL_64_after_hwframe+0x63/0xcd do_setxattr+0xb8/0x170 setxattr+0x126/0x140 ... The buggy address belongs to the object at ffff88800632f000 which belongs to the cache kmalloc-1k of size 1024 __x64_sys_setxattr+0x6d/0x80 ...

The buggy address belongs to the object at ffff88800632f000 which belongs to the cache kmalloc-1k of size 1024

#BHASIA @BlackHatEvents

## Slide 31

## (Cont’d)

#BHASIA @BlackHatEvents

> Text below was recovered by OCR (confidence 84/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Q
black hat
ASIA 20253
{
(Cont’d)
ntfs_inode *ni)
le = kmalloc(al_aligned(rs);
goto out;
}
for (; (jattr = mi_enum_attr(&ni->mi, attr))};—-le—=
le->type = attr->type;
le->size = cpu _ to lel6(sz);
le->name_len = attr->name_len;
le->name_off = offsetof(struct ATTR LIST ENTRY, name) ;
le->vcn = 0;
if (le != ni->attr_list.le)
le->ref = ni->attr_list.le->ref;
le->id = attr->id;
if (attr->name_len)
memcpy(le->name, attr_name(attr),
sizeof(short) * attr->name_len);
sz)) {
static inline size t al_aligned(size t size)
{
}
return (size + ) & ~(size t)1
struct ATTRIB *mi_enum attr(struct mft_inode *mi, struct ATTRIB *attr)
{
asize = le32_to cpu(attr->size) ;
/* Check size of attribute. */
if (!attr->non_res) {
if (asize < SIZEOF RESIDENT)
return N .
t16 = lel6 to cpu(attr->res.data off);
if (t16 > asize)
return NULL;
if (t16 + t32 > asize)
return N Q
return attr;
/* Check some nonresident fields. */
if (attr->name len &
lel6_to_ cpu(attr->name_ off) + sizeof(short) * attr->name_len >
le16 to cpu(attr->nres.run off)) {
return N f°
}
```

## Slide 32

## Patch

#BHASIA @BlackHatEvents

> Text below was recovered by OCR (confidence 89/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
ASIA 20253
Patch
diff --git a/fs/ntfs3/record.c b/fs/ntfs3/record.c
index 66eb11e0965ef..a952cd7aa7a4b 100644
--- a/fs/ntfs3/record.c
+++ b/fs/ntfs3/record.c
@@ -265,6 +265,11 @@ struct ATTRIB *mi_enum_attr(struct mft_inode *mi, struct ATTRIB *attr)
if (t16 + t32 > asize)
return NULL;
if (attr->name_len &&
le16_to_cpu(attr->name_off) + sizeof(short) * attr->name_len > t16) {
return NULL;
1
J
return attr;
```

## Slide 33

## Black Hat Sound Bytes

- Complicated and hard-to-fuzz software are good targets for security researchers

- File system maintainers should pay more attention on metadata integrity

- Users should be cautious on mounting an disk image

#BHASIA @BlackHatEvents
