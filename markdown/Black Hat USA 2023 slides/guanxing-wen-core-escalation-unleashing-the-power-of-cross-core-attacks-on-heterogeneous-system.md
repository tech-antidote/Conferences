---
title: "Core Escalation Unleashing the Power of Cross-Core Attacks on Heterogeneous System"
speakers: ["Guanxing Wen"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/Guanxing Wen_Core Escalation Unleashing the Power of Cross-Core Attacks on Heterogeneous System.pdf"
pages: 87
sha256: "1f9edee4ad650f6d1fa663c8b92927a4226de3a2e6c942fa89d171d50786e9ab"
text_chars: 23792
ocr_pages: 10
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:17:39Z"
---
# Core Escalation Unleashing the Power of Cross-Core Attacks on Heterogeneous System

**Speakers:** Guanxing Wen  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Guanxing Wen_Core Escalation Unleashing the Power of Cross-Core Attacks on Heterogeneous System.pdf` (87 pages)

## Slide 1

# **Core Escalation** Unleashing the Power of Cross-Core Attack on Heterogeneous System

###### Guanxing Wen

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pifek hat
USA 2023 a
AUGUST 9-10, 2025
BRIEFINGS
Core Escalation
Unleashing the Power of Cross-Core Attack on Heterogeneous System
Guanxing Wen
#BHUSA @BlackHatEvents
```

## Slide 2

## $ whoami

> ✤ Security Researcher @ Pangu Team in Shanghai

> ✤ Interested in bootloader, kernel, Trustzone

> ✤ Also a fan of pwning smart devices at hand

> ✤ Electric Vehicles, TV, speakers, POS …

> ✤ Twitter: @hhj4ck

## Slide 3

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
g b Huawei Bug Bounty Program Homepage
HUAWEI
Seasonal Ranking General ranking
Ranking list Nickname
@ Wen Guanxing
slipper
cererdlong
bugbounty.huawei.com
List of heroes Reward plan Announcement Log in
Time 2021 Type of business organization
Wa Huawei Bug Bounty Program Homepage
HUAWEI
Seasonal Ranking Annual ranking General ranking
Ranking list Nickname
@ Wen Guanxing
2. 360A lphaLab
3) 4ice
Contribution value
All business
bugbounty.huawei.com
List of heroes Reward plan
Time 2022
The team
pangu
360 Alpha Lab
ZETAO082895USCIS
Announcement Log in
Type of business organization All business
Contribution value
25112
23109
6752
```

## Slide 4

### EL3 Tour: Get The Ultimate Privilege of Android Phone

Guanxing Wen
2019

Exploit the **BL31** of Huawei **P20**

## Slide 5

EL3 Tour: Get The Ultimate Privilege of Android Phone

Guanxing Wen

2019

Exploit the **bootrom** of Huawei **Mate30**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
EL3 Tour: Get The Ultimate Privilege
Checkmate Mate30
Attack the bootrom of Huawei Smartphones
USA 2023
Core Escalation
Unleashing the Power of rost-CreAtackon Heterogeneous Sytem
```

## Slide 6

Exploit the **XXX** of Huawei **XXXX40**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisekhat MS
LUISA 2&2
AUGUST 9-10, 2023
BRIEFINGS
Core Escalation
Unleashing the Power of Cross-Core Attack on Heterogeneous System
Guanxing Wen
Checkmate Mate30
a tne
thebootom: Smanpones
```

## Slide 7

## Motivation

> ✤ Decrypt the firmwares of Mate40 (kirin9000)

> ✤ Xloader, Fastboot, TEEOS, BL31, LPM3, MODEM …

## Slide 8

## Motivation

> ✤ Decrypt the firmwares of Mate40 (kirin9000)

> ✤ Xloader, Fastboot, TEEOS, BL31, LPM3, MODEM …

> ✤ Bootrom exploit used to build the decryption oracle was dead

## Slide 9

## Motivation

> ✤ Decrypt the firmwares of Mate40 (kirin9000)

> ✤ Xloader, Fastboot, TEEOS, BL31, LPM3, MODEM …

> ✤ Bootrom exploit used to build the decryption oracle was dead

> ✤ The only solution I came up with is to follow the traditional approach

## Slide 10

## ARM Trustzone (ACPU)

EL0

EL1

EL2

EL3

Secure World

###### Normal World

APP APP TA TA
Linux Kernel TEEOS
Hypervisor

TA TA
TEEOS

Secure Monitor (BL31)

## Slide 11

## ARM Trustzone (ACPU)

EL0
EL1
EL2

EL3

Secure World

###### Normal World

APP APP TA TA
Linux Kernel TEEOS
Hypervisor

TA TA
TEEOS

Secure Monitor (BL31)

## Slide 12

## ARM Trustzone (ACPU)

EL0
EL1
EL2

EL3

Secure World
TA(ENC) TA(ENC)
TEEOS(ENC)

Normal World Secure World
APP APP TA(ENC) TA(ENC)
Linux Kernel TEEOS(ENC)
Hypervisor

Secure Monitor (BL31)

## Slide 13

## ARM Trustzone (ACPU)

EL0
EL1
EL2

EL3

Secure World

Normal World Secure World
APP APP TA(ENC) TA(ENC)
Linux Kernel TEEOS(ENC)
Hypervisor

TA(ENC) TA(ENC)
TEEOS(ENC)

Secure Monitor (BL31)

## Slide 14

## Find suitable TEE issues

> ✤ Logic bugs that work stably and can be exploited blindly

> ✤ No prior knowledge is required, such as gadgets or offsets

> ✤ Two primary attack surface

> ✤ BL31 & TEEOS

## Slide 15

## TEEOS

Hexacon 2022

- ‣<sup>**DRV_TIMER**</sup>

   - Manages secure timers

- ‣<sup>**GATEKEEPER**</sup>

   - Gatekeeper implementation

- ‣<sup>**KEYMASTER**</sup>

   - Keymaster implementation

- ‣<sup>**PERMISSION_SERVICE**</sup>

   - Permissions system for RPMB, SSA and TUI

- ‣<sup>**PLATDRV**</sup>

   - Platform drivers

   - Interrupts, crypto engine, secure element, fingerprint sensor, etc.

###### Tasks & Drivers **Examples of Tasks & Drivers**

###### SECURE WORLD

TA TA TA TA TA
libc libgm libtee libvendor
IPC
GTask
Perm
Platdrv RPMB SSA TUI
Serv
IPC
hmsysmgr hmfilemgr
Secure Kernel

- ‣<sup>**RPMB**</sup>

   - RPMB filesystem

   - Uses a normal world agent

- ‣<sup>**SSA**</sup>

   - Trusted Storage API

      - Uses a normal world agent

   -

- ‣<sup>**TALOADER & TARUNNER**</sup>

   - glue between GlobalPlatform and OS-level APIs

- ‣<sup>**TUI**</sup>

   - Trusted User Interface implementation

## Slide 16

SION ✤ Memory can switch between non-secure and secure dynamically ✤ Speeds up the decryption of DRM video streams

## Slide 17

## SION

> ✤ Memory can switch between non-secure and secure dynamically

> ✤ Speeds up the decryption of DRM video streams

> ✤ SECMEM (TA) exports SION APIs to the normal world

|CMD|Function Name|Description|
|---|---|---|
|1|**sion_alloc**|registers physical pages into platdrv and update their DMSS bits|
|2|**sion_free**|zero out related pages and update their DMSS bits|
|3|sion_map_iommu|map operations related to iommu|
|4|sion_unmap_iommu|unmap operations related to iommu|
|7|sion_config|set attribute bits of DMSS|
|8|sion_unconfig|unset attribute bits of DMSS|

## Slide 18

## SION ALLOC

`ion.heap_id_mask = 1 << ION_DRM_HEAP_ID` EL0 `ioctl(open(“/dev/ion”), ION_IOC_ALLOC, &ion)` EL1 `ion_secsg_heap_allocate -> secmem_tee_exec_cmd` SEL0 `sion_ioctl alloc buff_id <=> ion pages` secmem platdrv

SEL0

## Slide 19

EL1

## SION ALLOC

EL0

SEL0

```
ion.heap_id_mask = 1 << ION_DRM_HEAP_ID
ioctl(open(“/dev/ion”), ION_IOC_ALLOC, &ion)
```

```
ion_secsg_heap_allocate -> secmem_tee_exec_cmd
```

```
sion_ioctl
```

```
alloc buff_id <=> ion pages
```

platdrv

###### secmem

```
struct ion_buffer {
  u64 magic;
union {
struct rb_node node;
struct list_head list;
  };
struct ion_device *dev;
struct ion_heap *heap;
unsignedlongflags;
unsignedlong private_flags;
size_t size;
void *priv_virt;
structmutexlock;
int kmap_cnt;
void *vaddr;
struct sg_table *sg_table;
struct list_head attachments;
char task_comm[TASK_COMM_LEN];
  pid_t pid;
```

```
#if defined(CONFIG_ION_HISI_SECSG)
unsignedintid;
#endif
};
```

## Slide 20

## SION MAP

ion.fd vma
EL0 SEL0
TEEC_ION_INPUT
sion_map_user
ion.fd buff.id buff.id
EL1 ion pages SEL1

## Slide 21

## CVE-2022-46762

> ✤ Each module assumes other modules for input validation

> ✤ NW kernel should never be a firewall for SW

> ✤ EL0 can invoke sion_alloc directly with arbitrary physical address

> ✤ The same goes for sion_free

## Slide 22

## Bind ion fd, buff id and ion page

ion.fd buff.id

```
sion_alloc
```

buff.id

ion pages

## Slide 23

## Unbind buff id and ion page

sion_alloc
sion_free_freefree

sion_alloc
ion.fd buff.id
sion_free_freefree
buff.id

buff.id ion pages
buff.id ion pages

## Slide 24

## Rebind the buff id and target page

sion_alloc
ion.fd buff.id
sion_free
buff.id
sion_alloc
buff.id

buff.id ion pages
buff.id ion pages
buff.id
any pages

## Slide 25

## Make use of the malformed buff id

> ✤ CHINADRM_COMMON_TA

> ✤ A substitute of widevine

> ✤ Cleartext need no decryption

- ✤ Decryption = memmove

> ✤ Overwrite any SW pages?

## Slide 26

## A Small Setback

###### ✤ hmsysmgr blacklists mmap

> ✤ 0x13000000-0x13101000

> ✤ 0x13102000-0x13600000

> ✤ 0x13600000-0x19600000

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
A Small Setback
Ry hmsysmgr blacklists mmap if en length_) )
~end a end; ;
if i(unsigned __int8)get_sec_regions()
fe Ox] 3000000-0x1 37 01 000 | _Start < reg_info.phys_region_start + 0x5FF000 - reg_info.cc_workspace_mem
“end > reg_info.phys_region_start + Ox5FFO00 )
goto LABEL 177;
}
}
fe Ox1 31 02000-0x1 3600000 se if ( LODWORD(v230[0]) || (unsigned int)is_in_range_of_protect_space(start, length_)
{
goto LABEL_177;
}
_length = a2->length;
start_ = *(_QWORD *)&a2->start;
v98 = OLL;
else
v98 = v93;
v230[0] = OLL;
v230[1] = start_;
v230[2] = _length;
memset (&v230[3], 0, 0x14);
v99 = hm map range( int64)v53, v59, v98,
length, nents & OxFFF, (__int64)v230);
```

## Slide 27

```
START
```

```
USAGE
```

```
END
```

|`10000000`|`105FFFFF`|`sensorhub-shmemext`|
|---|---|---|
|`10600000`|`1063FFFF`|`sensorhub-shmem`|
|`10640000`|`106BFFFF`|`sensorhub-share-mem`|
|`106C0000`|`108BFFFF`|`iommu_pgtable`|
|`108C0000`|`109BEFFF`|`fka-mem`|
|`109BF000`|`109BFFFF`|`mntndump`|
|`109C0000`|`10ABFFFF`|`ivp`|
|`114C0000`|`11CBFFFF`|`hhee`|
|`11CC0000`|`11D3FFFF`|`lpmx-core`|
|`11D40000`|`11DFFFFF`|`lpmcu`|
|`11E00000`|`127FFFFF`|`sensorhub-s`|
|`12800000`|`12FFFFFF`|`npu-tiny`|
|`13000000`|`135FFFFF`|`bl31`|
|`13600000`|`165FFFFF`|`secos`|
|`16600000`|`16AFFFFF`|`voiceid`|

## Slide 28

|`2CE00000`|`2D9FFFFF`|`sec_camera`|
|---|---|---|
|`2DA00000`|`2E97FFFF`|`hifi-base`|
|`2E980000`|`2F37FFFF`|`npu-sec`|
|`2F380000`|`2F8FFFFF`|`hifi-data`|
|`2F900000`|`3015FFFF`|`bbox-mem`|
|`30160000`|`3025FFFF`|`dp-dhcp`|
|`30260000`|`3035FFFF`|`pstore-mem`|
|`30360000`|`3075FFFF`|`npu_ai_ts_fw`|
|`30760000`|`3105FFFF`|`npu_ai_server`|
|`36500000`|`3A3FFFFF`|`logo-buffer`|
|`3A400000`|`3FFFFFFF`|`fastboot-cma-mem`|
|`40000000`|`4FFFFFFF`|`hisi_cma`|
|`50000000`|`5ABFFFFF`|`hisi_iris_static_cma`|
|`60000000`|`63FFFFFF`|`tiny_cma`|
|`90000000`|`9FFFFFFF`|`hisi_smemheap_cma`|
|`A0000000`|`B127FFFF`|`modem-s`|

## Slide 29

|`2CE00000`|`2D9FFFFF`|`sec_camera`|
|---|---|---|
|`2DA00000`|`2E97FFFF`|`hifi-base`|
|`2E980000`|`2F37FFFF`|`npu-sec`|
|`2F380000`|`2F8FFFFF`|`hifi-data`|
|`2F900000`|`3015FFFF`|`bbox-mem`|
|`30160000`|`3025FFFF`|`dp-dhcp`|
|`30260000`|`3035FFFF`|`pstore-mem`|
|`30360000`|`3075FFFF`|`npu_ai_ts_fw`|
|`30760000`|`3105FFFF`|`npu_ai_server`|
|`36500000`|`3A3FFFFF`|`logo-buffer`|
|`3A400000`|`3FFFFFFF`|`fastboot-cma-mem`|
|`40000000`|`4FFFFFFF`|`hisi_cma`|
|`50000000`|`5ABFFFFF`|`hisi_iris_static_cma`|
|`60000000`|`63FFFFFF`|`tiny_cma`|
|`90000000`|`9FFFFFFF`|`hisi_smemheap_cma`|
|`A0000000`|`B127FFFF`|`modem-s`|

## Slide 30

A bigger picture

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
eer ar
; .
ne) QEP picture
```

## Slide 31

## ARM Trustzone (ACPU)

EL0

EL1

EL2

EL3

Secure World

###### Normal World

APP APP TA TA
Linux Kernel TEEOS
Hypervisor

TA TA
TEEOS

Secure Monitor (BL31)

## Slide 32

## ARM Trustzone (ACPU)

Normal World (NW)

Secure World (SW)

AXI BUS

## Slide 33

## ARM Trustzone (ACPU)

Normal World (NW)

Secure World (SW)

AXI BUS

## Slide 34

## ARM Trustzone (ACPU)

SCR.NS = 1

Normal World (NW) Secure World (SW)
SCR.NS = 0

AXI BUS

## Slide 35

## ARM Trustzone (ACPU)

Normal World (NW) Secure World (SW)
AXI BUS
TZASC TZPC AXI-to-APB
DRAM DRAM
DRAM DRAM
DRAM Peripherals

Secure World (SW) SCR.NS = 0

SCR.NS = 1

## Slide 36

## ARM Trustzone (ACPU)

ACPU
AXI BUS
TZASC TZPC AXI-to-APB
DRAM DRAM
DRAM DRAM
DRAM Peripherals

## Slide 37

## ARM Trustzone (SOC)

ACPU MODEM GPU ISP LPMCU IOMCU UFS
AXI BUS
TZASC TZPC AXI-to-APB
DRAM DRAM
DRAM DRAM
DRAM Peripherals

## Slide 38

## ARM Trustzone (SOC)

ACPU MODEM GPU ISP LPMCU IOMCU UFS
AXI BUS
TZASC TZPC AXI-to-APB
DRAM DRAM
DRAM DRAM
DRAM Peripherals

## Slide 39

```
START
```

```
USAGE
```

```
END
```

|`10000000`|`105FFFFF`|`sensorhub-shmemext`|
|---|---|---|
|`10600000`|`1063FFFF`|`sensorhub-shmem`|
|`10640000`|`106BFFFF`|`sensorhub-share-mem`|
|`106C0000`|`108BFFFF`|`iommu_pgtable`|
|`108C0000`|`109BEFFF`|`fka-mem`|
|`109BF000`|`109BFFFF`|`mntndump`|
|`109C0000`|`10ABFFFF`|`ivp`|
|`114C0000`|`11CBFFFF`|`hhee`|
|`11CC0000`|`11D3FFFF`|`lpmx-core`|
|`11D40000`|`11DFFFFF`|`lpmcu`|
|`11E00000`|`127FFFFF`|`sensorhub-s`|
|`12800000`|`12FFFFFF`|`npu-tiny`|
|`13000000`|`135FFFFF`|`bl31`|
|`13600000`|`165FFFFF`|`secos`|
|`16600000`|`16AFFFFF`|`voiceid`|

## Slide 40

## Pivot to IOMCU

> ✤ load_and_run sensorhub.img (ARM Cortex M7, not encrypted)

## Slide 41

## Pivot to IOMCU

> ✤ load_and_run sensorhub.img (ARM Cortex M7, not encrypted)

> ✤ Tamper its memory with a thorough overwrite

## Slide 42

## Pivot to IOMCU

> ✤ load_and_run sensorhub.img (ARM Cortex M7, not encrypted)

> ✤ Tamper its memory with a thorough overwrite

> ✤ Crash dump (RDR) revealed that 0x1248d000 gets executed

> ✤ IOMCU reboots itself, without interfering entire system

## Slide 43

## Pivot to IOMCU

> ✤ load_and_run sensorhub.img (ARM Cortex M7, not encrypted)

> ✤ Tamper its memory with a thorough overwrite

> ✤ Crash dump (RDR) revealed that 0x1248d000 gets executed

> ✤ IOMCU reboots itself, without interfering entire system

> ✤ A secure master can raise AWPROT=0, ARPROT=0

## Slide 44

## Pivot to LPMCU

> ✤ SRAM of LPMCU is accessible from IOMCU

> ✤ #define SOC_IOMCU_LP_RAM_BASE_ADDR (0x5FF50000)

## Slide 45

## Pivot to LPMCU

> ✤ SRAM of LPMCU is accessible from IOMCU

> ✤ #define SOC_IOMCU_LP_RAM_BASE_ADDR (0x5FF50000)

> ✤ Dump the SRAM of LPMCU into crash dump (RDR) of IOMCU

## Slide 46

## Pivot to LPMCU

> ✤ SRAM of LPMCU is accessible from IOMCU

> ✤ #define SOC_IOMCU_LP_RAM_BASE_ADDR (0x5FF50000)

> ✤ Dump the SRAM of LPMCU into crash dump (RDR) of IOMCU

> ✤ Patch LPMCU RDR related code to get code execution

> ✤ RDR is triggered during a crash of IOMCU

## Slide 47

Mountain Top: LPMCU ✤ A secure master (ARM Cortex M3), definitely ✤ LPM3.img runs in this core after bootrom and xloader ✤ Recent mitigations only accumulated more privilege for the LPMCU ✤ DMSS control is shifted from ACPU to LPMCU ✤ dma_transfer() is powerful enough to hack into other cores

> ✤ Even DDR belongs to ACPU

## Slide 48

## Acquire ACPU EL3 privilege

```
stpx29, x30, [sp, -0x10]!
tstx0, 1
beqexec
ldrw3, [x1]
strw3, [x2]
bend
exec:
blrx3
strx0, [x6]
end:
tlbialle3
dsbish
isb
ldpx29, x30, [sp], 0x10
ret
```

##### Patch BL31 (adding a RWX smc handler)

## Slide 49

## Establish a Decryption Oracle

Patch TEEOS (platdrv)

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Establish a Decryption Oracle
int _ fastcall hisi_secboot_verify_modem_imgs(int al, int a2, int a3, int a4)
// [COLLAPSED LOCAL DECLARATIONS. PRESS KEYPAD CTRL-"+" TO EXPAND]
v8 (int *)modem_image _ info();
{
v1l0 = -1;
log(0, "%s td:hisi_modem_ disreset get modem_image info failed.\n ", "[error]", 671);
return v10;
}
if ( (unsigned int)(al - 7) >3 )
i!
return hisi_secboot_verify_modem_comm_imgs(5, a3, a4);
v1l2 = &v8[10 * al];
goto LABEL 15;
v10 = hisi_secboot_verify(__SPAIR64__(a2, al), *((_QWORD *)v12 + 2), “modem
fw", a4);
```

## Slide 50

DEMO: Firmware Decryption

## Slide 51

## Core Escalation

LPMCU
IOMCU
ACPU EL0 ACPU EL3

## Slide 52

What else lies under this attack model?

## Slide 53

## ARM Trustzone (SOC)

ACPU MODEM GPU ISP LPMCU IOMCU UFS
AXI BUS
TZASC TZPC AXI-to-APB
DRAM DRAM
DRAM DRAM
DRAM Peripherals

## Slide 54

## ARM Trustzone (SOC)

ACPU MODEM GPU ISP LPMCU IOMCU UFS
AXI BUS
TZASC TZPC AXI-to-APB
Peripherals
DRAM PeripheralsPeripherals

## Slide 55

## ARM Trustzone (SOC)

Peripherals Peripherals Peripherals Peripherals Peripherals
AXI BUS

TZASC TZPC
DRAM
UFS
IOMCU
LPMCU
ISP
GPU
MODEM
ACPU

AXI-to-APB

## Slide 56

## Cross-Core Communication

ACPU MODEM GPU ISP LPMCU IOMCU UFS

## Slide 57

Cross-Core Attack Surface ✤ ACPU <=> LPMCU, MODEM <=> HIFI, ISP <=> GPU …

> ✤ DMA

> ✤ Mailbox

> ✤ Shared memory

> ✤ Hardware specific issues

## Slide 58

DMA

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
DMA
Over The Air: Exploiting Broadcom’s Wi-Fi Stack (Part 2)
Posted by Gal Beniamini, Project Zero
In this blog post we'll continue our journey into gaining remote kernel code execution, by means of Wi-Fi
communication alone. Having previously developed a remote code execution exploit giving us control over
Broadcom’s Wi-Fi SoC, we are now left with the task of exploiting this vantage point in order to further
elevate our privileges into the kernel.
Device
Crypto
Camera Engines
Application Processor
Kernel
GPU Wi-Fi Sot |“ - -
User-Space
Baseband
Processor
```

## Slide 59

## DMA

###### DMA Attacks: Trial And Error

###### Modem EDMA: FAIL

IOMCU DMA: SUCCESS (on 980)

###### How To Tame Your Unicorn

Daniel Komaromy       Lorant Szabo

TASZK Security Labs

#BHUSA  @BlackHatEvents

- **CVE-2021-22432**

- Why do these fail/succeed though?

#BHUSA   @BlackHatEvents

## Slide 60

## Mailbox

> ✤ Key component of the cross-core communication architecture

> ✤ Hardware-based module with registers and exported small buffers

###### Mailboxes

SOURCE
0x40 DSET
…
DCLR
DSTATUS
ACPU 0x40 NO. 17 MODE LPMCU
IMASK
ICLR
0xFE101000 0x40 SEND 0xBE101000
…
DATA[0x20]

## Slide 61

## CVE-2020-36600

ACPU

LPMCU

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
CVE-2020-36600
C —fastcall mailbox_17_handler(int al) void __fastcall rdr_init(unsigned int addr, int size)
// [COLLAPSED LOCAL DECLARATIONS. PRESS KEYPAD CTRL-"+" TO EXPAND] { // [COLLAPSED LOCAL DECLARATIONS. PRESS KEYPAD CTRL-"
if MEMORY
( (OxBE101460] == 0x80202 ) if ( addr > Ox2FOFFFFF && addr + size <= 0x2F960000 )
rdr_init (MEMORY[0xBE101464], MEMORY[0xBE10146C]); {
goto LABEL 26; g_addr = addr;
} g_size = size;
void __cdecl rdr_data_save(int addr, int outsize, char *msg, int msg qmemcpy(msg, "LPM3_ RDR", 8&);
*(_DWORD *)&msg[8] = 0x80;
// [COLLAPSED LOCAL DECLARATIONS. PRESS KEYPAD CTRL-"+" TO EXPAND] *("DWORD *)&msg[24] = 0x3C00;
*(_DWORD *)&msg[60] = 0;
teas op _-—-*(DWORD *)&msg[64] = 0x400;
{ van ape ret 1b) Bee nee 2019 00:52:46");// st
at ¢ eis atin int)outsize ) if ( snprintf((unsigned int)&msg[96], Oxl8u, (unsig
; dma_transfer((int)(msg + 0xFFF30000), addr, _msgsize, 0); Los_Print (2, “rdrbuf err\n");
else
} rdr data save(g addr, 0x80, (int)msg, 0x78);
```

## Slide 62

## Shared Memory

###### ✤ Common usage

> ✤ State synchronization, data transfer and logging

> ✤ Pointer, offset, length on shared memory are not reliable

## Slide 63

## CVE-2022-46322

DRAM
Page Table
ACPU RDR_VA RDR_PA RDR_PA
…

###### EL0 access RDR by mmap(/dev/isplog)

Page Table
0xC1800000 RDR_PA ISP
…
EL3 updates the page table of ISP

## Slide 64

## CVE-2022-46322

DRAM
Page Table Page Table
ACPU RDR_VA RDR_PA RDR_PA 0xC1800000 RDR_PA ISP
… …
EL0 access RDR by mmap(/dev/isplog) EL3 updates the page table of ISP

## Slide 65

## Hardware specific issues

###### ✤ Internal sram exposed

> ✤ Registers exposed: SCTRL, TZPC …

> ✤ Lack of bootchain verification

> ✤ Secure master runs its image in unprotected memory

## Slide 66

Abstract thinking was nice, but it's code o'clock!

## Slide 67

## CVE-2022-48353

> ✤ ISP is actually a secure master

> ✤ Think of face recognition

## Slide 68

## CVE-2022-48353

> ✤ ISP is actually a secure master

> ✤ Think of face recognition

> ✤ ISP does not verify its firmware

> ✤ shellcode injection in a single line of command

```
    mount --bind isp_fw_mod.elf /odm/etc/firmware/isp_fw.elf
```

## Slide 69

Mitigations of Cross-Core Attack ✤ DMSS & CFGBUS: think of TZASC & TZPC ✤ DMSS maintains a DDR permission table for each master ✤ Each cell declares if a subrange of DDR is allowed to be accessed with Normal/Secure AWPROT/ARPROT

> ✤ CFGBUS manages MMIO access

> ✤ Each table declares if a group of masters are allowed to access a range of MMIO

## Slide 70

## ISP

> ✤ Cannot RW DDR without ACPU EL3 setting up its IOMMU

> ✤ Cannot RW 0xFFE00000 - 0xFFFFFFFF (blocked by CFGBUS)

> ✤ #define SOC_ACPU_DMSS_BASE_ADDR (0xFFE80000)

> ✤ #define SOC_ACPU_LP_RAM_BASE_ADDR (0xFFF50000)

## Slide 71

## ISP

> ✤ Cannot RW DDR without ACPU EL3 setting up its IOMMU

> ✤ Cannot RW 0xFFE00000 - 0xFFFFFFFF (blocked by CFGBUS)

> ✤ #define SOC_ACPU_DMSS_BASE_ADDR (0xFFE80000)

> ✤ #define SOC_ACPU_LP_RAM_BASE_ADDR (0xFFF50000)

> ✤ Can RW 0xFE252000 - 0xFE252400 (CFGBUS Registers)

## Slide 72

## CFGBUS

|`REGs`|`2.0.0.222`|`2.0.0.243`|
|---|---|---|
|`0xFE2520BC`|`0x4DA000`|`0x01A000`|
|`0xFE2520C0`|`0xFFFE00`|`0x03FE00`|
|`0xFE2520C4`|`00000000`|`00000000`|
|`0xFE2520C8`|`0`|`0`|
|`0xFE2520CC`|`0x14`|`0x15`|
|`0xFE2520D0`|`0`|`0`|
|`0xFE2520D4`|`0`|`0`|
|`0xFE2520D8`|`0x3`|`0x2`|
|`0xFE2520DC`|`0x3`|`0x3`|
|`0xFE2520E0`|`0xF`|`0xF`|
|`0xFE2520E4`|`0`|`0`|
|`0xFE2520E8`|`0x10000`|`0x10000`|
|`0xFE2520EC`|`0x00000`|`0x00000`|
|0xFFE00000|+ 2 **0x15=|0x100000000|

```
 master bits
 log₂(size)
 rw permission
```

## Slide 73

## CFGBUS

REGs 2.0.0.243
0xFE252044 0x002000
0xFE252048 0x03FE00
0xFE25204C  00002000
0xFE252050  0
0xFE252054  0x0a
0xFE252058  0
0xFE25205C  0
0xFE252060  0x2
0xFE252064  0x3
0xFE252068  0xF
0xFE25206C  0
0xFE252070  0x10000
0xFE252074 0x00000

```
 offset
```

0xFE250000 + 0x2000 = 0xFE252000 0xFE252000 + 2 **0xa = 0xFE252400

## Slide 74

## Configure CFGBUS

```
REGs2.0.0.243
0xFE252044 0x002000
0xFE252048 0x03FE00
0xFE25204C 00002000
0xFE252050 0
0xFE252054 0x0a
0xFE252058 0
0xFE25205C 0
0xFE252060 0x2
0xFE252064 0x3
0xFE252068 0xF
0xFE25206C 0
0xFE252070 0x10000
0xFE2520740x00000
```

```
[0xfe25200c] <= 0x00
[0xfe252008] <= 0x00
[0xfe25240c] <= 0x00
[0xfe25248c] <= 0x00
[0xfe252018] <= 0x00
[0xfe252020] <= 0x0F
```

```
. . .
```

```
[0xfe252014] <= 0xBA
[0xfe252008] <= 0x0F
[0xfe25200c] <= 0x01
[0xfe252008] <= 0x1F
[0xfe252018] <= 0x08
```

## Slide 75

## Configure CFGBUS

|`REGs`|`2.0.0.243`|
|---|---|
|`0xFE252044`|`0x002000`|
|`0xFE252048`|`0x03FE00`|
|`0xFE25204C`|`00002000`|
|`0xFE252050`|
`0`|
|`0xFE252054`|
`0x0a`|
|`0xFE252058`|
`0`|
|`0xFE25205C`|
`0`|
|`0xFE252060`|
`0x2`|
|`0xFE252064`|
`0x3`|
|`0xFE252068`|
`0xF`|
|`0xFE25206C`|
`0`|
|`0xFE252070`|
`0x10000`|
|`0xFE252074`|`0x00000`|

```
[0xfe25200c] <= 0x00
[0xfe252008] <= 0x00
[0xfe25240c] <= 0x00
[0xfe25248c] <= 0x00
[0xfe252018] <= 0x00
[0xfe252020] <= 0x0F
```

```
. . .
```

```
[0xfe252014] <= 0xBA
[0xfe252008] <= 0x0F
[0xfe25200c] <= 0x01
[0xfe252008] <= 0x1F
[0xfe252018] <= 0x08
```

```
Disable
```

## Slide 76

## Configure CFGBUS

|`REGs`|`2.0.0.243`|
|---|---|
|`0xFE252044`|`0x002000`|
|`0xFE252048`|`0x03FE00`|
|`0xFE25204C`|`00002000`|
|`0xFE252050`|
`0`|
|`0xFE252054`|
`0x0a`|
|`0xFE252058`|
`0`|
|`0xFE25205C`|
`0`|
|`0xFE252060`|
`0x2`|
|`0xFE252064`|
`0x3`|
|`0xFE252068`|
`0xF`|
|`0xFE25206C`|
`0`|
|`0xFE252070`|
`0x10000`|
|`0xFE252074`|`0x00000`|

```
[0xfe25200c] <= 0x00
[0xfe252008] <= 0x00
[0xfe25240c] <= 0x00
[0xfe25248c] <= 0x00
[0xfe252018] <= 0x00
[0xfe252020] <= 0x0F
```

```
. . .
Config
[0xfe252014] <= 0xBA
[0xfe252008] <= 0x0F
[0xfe25200c] <= 0x01
[0xfe252008] <= 0x1F
[0xfe252018] <= 0x08
```

## Slide 77

## Configure CFGBUS

```
REGs2.0.0.243
0xFE252044 0x002000
0xFE252048 0x03FE00
0xFE25204C 00002000
0xFE252050 0
0xFE252054 0x0a
0xFE252058 0
0xFE25205C 0
0xFE252060 0x2
0xFE252064 0x3
0xFE252068 0xF
0xFE25206C 0
0xFE252070 0x10000
0xFE2520740x00000
```

```
[0xfe25200c] <= 0x00
[0xfe252008] <= 0x00
[0xfe25240c] <= 0x00
[0xfe25248c] <= 0x00
[0xfe252018] <= 0x00
[0xfe252020] <= 0x0F
```

```
. . .
```

```
[0xfe252014] <= 0xBA
[0xfe252008] <= 0x0F
[0xfe25200c] <= 0x01
[0xfe252008] <= 0x1F
[0xfe252018] <= 0x08
```

```
Enable
```

## Slide 78

## Disable CFGBUS

```
REGs2.0.0.243
0xFE252044 0x002000
0xFE252048 0x03FE00
0xFE25204C 00002000
0xFE252050 0
0xFE252054 0x0a
0xFE252058 0
0xFE25205C 0
0xFE252060 0x2
0xFE252064 0x3
0xFE252068 0xF
0xFE25206C 0
0xFE252070 0x10000
0xFE2520740x00000
```

```
[0xfe25200c] <= 0x00
[0xfe252008] <= 0x00
[0xfe25240c] <= 0x00
[0xfe25248c] <= 0x00
[0xfe252018] <= 0x00
[0xfe252020] <= 0x0F
```

```
. . .
```

```
[0xfe252014] <= 0xBA
[0xfe252008] <= 0x0F
[0xfe25200c] <= 0x01
[0xfe252008] <= 0x1F
[0xfe252018] <= 0x08
```

## Slide 79

## ACPU EL0 -> ISP -> LPMCU -> ACPU EL3

###### ✤ Disable CFGBUS

> ✤ Pivot to LPMCU by RW its SRAM

> ✤ Enable BL31 patching by updating DMSS Table of LPMCU

> ✤ Use dma_transfer() to patch BL31 with a RWX SMC handler

## Slide 80

## ACPU EL0 -> ISP -> LPMCU -> ACPU EL3

###### ✤ Disable CFGBUS

> ✤ Pivot to LPMCU by RW its SRAM

> ✤ Enable BL31 patching by updating DMSS Table of LPMCU

> ✤ Use dma_transfer() to patch BL31 with a RWX SMC handler

> ✤ DEMO: Screen Passcode Bypass

## Slide 81

DEMO: Screen Passcode Bypass

## Slide 82

## Key Takeaways

> ✤ Interactions between different cores should be explored

> ✤ Cross-Core attacks can be a powerful technique to exploit

> ✤ Vendors should exercise caution when adding new cores to the SW

## Slide 83

## Key Takeaways

> ✤ Interactions between different cores should be explored

> ✤ May discover new paths for privilege escalation

> ✤ Cross-Core attacks can be a powerful technique to exploit

> ✤ Vendors should exercise caution when adding new cores to the SW

## Slide 84

## Key Takeaways

> ✤ Interactions between different cores should be explored

> ✤ Cross-Core attacks can be a powerful technique to exploit

> ✤ Do I mention ASLR, CFI, PXN, PAN, PAC, MTE ?

> ✤ Vendors should exercise caution when adding new cores to the SW

## Slide 85

## Key Takeaways

> ✤ Interactions between different cores should be explored

> ✤ Cross-Core attacks can be a powerful technique to exploit

> ✤ Vendors should exercise caution when adding new cores to the SW

> ✤ With each additional core, the complexity of writing bug-free software increases exponentially

## Slide 86

# **Credit**

#### Tielei Wang John Dickson

#BHUSA   @BlackHatEvents

## Slide 87

# **Questions?**

@hhj4ck

Meet + Greet: Aug 9, 17:00 – 17:30 Booth 3241 - Meetup Lounge, Business Hall

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pifzkhat
LUISA 2O2z3 ae
Questions?
X W @hhj4ck
Meet + Greet: Aug 9, 17:00 — 17:30
Booth 3241 - Meetup Lounge, Business Hall
#BHUSA @BlackHatEvents
```
