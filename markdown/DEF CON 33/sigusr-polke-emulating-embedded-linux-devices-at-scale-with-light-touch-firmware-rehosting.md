---
title: "Emulating Embedded Linux Devices at Scale with Light-Touch Firmware Rehosting"
speakers: ["Sigusr Polke"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33/Sigusr Polke - Emulating Embedded Linux Devices at Scale with Light-Touch Firmware Rehosting.pdf"
pages: 55
sha256: "3d5c80584ae51362a27c462a22ef29244eb4770baa5ac2bee3d4c25451202073"
text_chars: 31865
ocr_pages: 10
has_ocr: true
redacted_secrets: 0
ocr_confidence: 87.0
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T07:15:07Z"
---
# Emulating Embedded Linux Devices at Scale with Light-Touch Firmware Rehosting

**Speakers:** Sigusr Polke  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33/Sigusr Polke - Emulating Embedded Linux Devices at Scale with Light-Touch Firmware Rehosting.pdf` (55 pages)


## Slide 1

**Emulating Embedded Linux Devices at Scale with Light-Touch Firmware Rehosting**


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Emulating Embedded Linux Devices at Scale
with Light-Touch Firmware Rehosting
```

## Slide 2

# **Embedded Linux Emulation Today**

**Find stock ARM/MIPS QEMU machine chroot to unpacked root filesystem Boot common Linux distro**

**Run binaries (with LD_PRELOAD hacks)**

**Unpack firmware image**

## Slide 3

# **Emulation Friction**

_Missing hardware_

_Non-standard interfaces_

_Holistic system design doesnʼt “travelˮ_


> Recovered by OCR — confidence 86/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Emulation Friction
»< Missing hardware
>< Non-standard interfaces
>< Holistic system design doesn’t “travel”
```

## Slide 4

# **What Do We Want?**

**Full system emulation** we can use in:

**→ Vulnerability research → Honeypots**

## Slide 5

# **Rehosting Approach**

Looks as close as a “realˮ device as possible, from userspace.

_Don’t touch userspace!_

**Rehosting Environment**

Modified QEMU machine

Modified kernel

& boots into…
loads…

_→ Userspace can only use what the kernel exposes. → Custom QEMU machine + modified kernel = terrain which looks as close as a “realˮ device as possible._

**Real firmware user image**

## Slide 6

# **Where Do We Start?**

_What are embedded Linux systems made of?_

Built on SoCs (“System-on-Chipˮ). Vendors Netgear, ASUS, TPLink, etc) are not chip companies! **Vendors donʼt build SoCs!**

The same SoCs are used across multiple devices by different vendors.

© Raimond Spekking / CC BY-SA 4.0 (via Wikimedia Commons)

## Slide 7

# **SoC and Load**

_The supply chain looks something like:_

SoC Manufacturer
Vendor
SoC
Device
SDK

## Slide 8

# **So What?**

→ Shift perspective

→ Away from device, towards the SoC/SDK → Take firmware from any device based on that SoC family and run it

## Slide 9

# **Info to Lean On**

QEMU machines

Datasheets

Linux kernel

Firmware images

Source code for many drivers, binaries, libraries

Documentation

RE tools

**Unlimited time, energy, money**

GPL code

Compiled kernels

OSS distros OpenWRT, etc)

## Slide 10

# **The Plan**

_This is enough to try_ **_something_** _._

Compile kernel
& QEMU

Add “hardwareˮ (to QEMU and/or the kernel)

See what breaks

Run kernel on QEMU machine Load firmware filesystem & init

## Slide 11

# **ASUS RT-AC87U**

Older ASUS router. Based around the BCM4709.


> Recovered by OCR — confidence 88/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ASUS RT-AC87U
Older ASUS router.
Based around the BCM4709.
) CrowdStrike, Inc. All Rights Reserve:
```

## Slide 12

ASUS RT-AC56R ASUS RT-AC56S ASUS RT-AC56U ASUS RT-AC66U B1 rev A1 ASUS RT-AC67U ASUS RT-AC68U V3 **BCM4709 Data** ASUS RT-AC68U rev A1 ASUS RT-N18U ASUS RT-N66U C1 ASUS TM-AC1900 AirTies Air 4920 AirTies Air 4921 AirTies Air 4930 Arcadyan WA9117A-AC23 → Broadcom Belkin F9K1113 v2 Belkin F9K1118 v2 Buffalo WZR-1166DHP → Cortex A9 Buffalo WZR-1750DHP Buffalo WZR-600DHP2 Buffalo WZR-900DHP → BCM4707/4708/4709 family. D-Link DIR-860L rev A1 D-Link DIR-868L rev A1 D-Link DIR-880L rev A1 → Five integrated 10/100/1000 PHY ports Huawei E5186s-22a Huawei WS880 Kasda KA1200 → No actual physical device Kasda KA1750 Linksys EA6200 Linksys EA6300 v0.1 Linksys EA6300 v1 Linksys EA6350 Linksys EA6350 v2 Linksys EA6400 Linksys EA6500 v2 Linksys EA6700 Linksys EA6900 v1.0 Linksys EA6900 v1.1

Motorola MR1900 Netgear AC1450 Netgear EX6200 Netgear EX7000 Netgear Nighthawk RS400 Netgear R6200v2 Netgear R6250 Netgear R6300 v2 Netgear R6400 v1 Netgear R6400 v2 U12H332T20 Netgear R6400 v2 U12H332T30 Netgear R6700 v3 Netgear R6900P Netgear R7000P Netgear XR300 SmartRG SR400ac TP-LINK Archer C5 v2.x TP-LINK Archer C8 v1.x TP-LINK Archer C8 v2.x TP-LINK Archer C8 v4.x TRENDnet TEW-811DRU TRENDnet TEW-812DRU v2 TRENDnet TEW-818DRU V1.0R Tenda AC15 Tenda AC18 Tenda F452 Xunlei rs1309

## Slide 13

# **RT-AC87U Firmware**

→ 3.0.0.4.382.52545

→ GPL tarball available

   - **$ file RT-AC87U_3.0.0.4_382_52545-ga0245cc.trx_extract/part0** RT-AC87U_3.0.0.4_382_52545-ga0245cc.trx_extract/part0: LZMA compressed

   - data, non-streamed, size 4034880

- → TRX format

- → Unpack with unblob

→ part0: LZMA-compressed kernel

**$ file RT-AC87U_3.0.0.4_382_52545-ga0245cc.trx_extract/part1** RT-AC87U_3.0.0.4_382_52545-ga0245cc.trx_extract/part1: Squashfs filesystem, little endian, version 4.0, xz compressed, 39299338 bytes, 2624 inodes, blocksize: 131072 bytes, created: Fri Apr 30 20:18:52 2021

→ part1: SquashFS filesystem

## Slide 14

# **Interrogate the Firmware**

- → 2.6.36.4brcmarm.

→ Linux 2.6.36.4

- → brcm = Broadcom?

- **$ strings part0_extract/0-1685649.lzma_extract/lzma.uncompressed | grep Linux**

- Linux version 2.6.36.4brcmarm (root@asus) (gcc version 4.5.3 (Buildroot 2012.02) ) #1 SMP PREEMPT Sat May 1 03:57:40 CST 2021

→ gcc 4.5.3 Buildroot 2012.02

- **$ strings part0_extract/0-1685649.lzma_extract/lzma.uncompressed | grep root=**

root=/dev/mtdblock2 console=ttyS0,115200 init=/sbin/preinit earlyprintk debug

## Slide 15

# **Interrogate the Firmware**

_Understand the boot process..._

→ root=/dev/mtdblock2.

→ MTD = flash.

**$ strings part0_extract/0-1685649.lzma_extract/lzma.uncompressed | grep root=** root=/dev/mtdblock2 console=ttyS0,115200 init=/sbin/preinit earlyprintk debug

→ Init process is /sbin/preinit.

→ /sbin/preinit is a link to /sbin/rc.

**$ ls -al part1_extract/0-39301120.squashfs_v4_le_extract/sbin/preinit** lrwxrwxrwx 1 tests tests 2 Jul  5 20:39

part1_extract/0-39301120.squashfs_v4_le_extract/sbin/preinit -> rc

→ /sbin/rc = big binary

**$ file part1_extract/0-39301120.squashfs_v4_le_extract/sbin/rc** part1_extract/0-39301120.squashfs_v4_le_extract/sbin/rc: ELF 32-bit LSB executable, ARM, EABI5 version 1 (SYSV), dynamically linked, interpreter /lib/ld-uClibc.so.0, stripped

## Slide 16

# **Layout**

### → Important system directories missing

→ /tmp/ must be populated at some point during the boot?

**$ ls -al part1_extract/0-39301120.squashfs_v4_le_extract/** total 80 drwxrwxr-x 18 tests tests  4096 Jul  5 20:39 . drwxr-xr-x  3 tests tests  4096 Jul  5 20:39 .. drwxrwxr-x  2 tests tests  4096 Apr 30  2021 asus_jffs drwxrwxr-x  2 tests tests  4096 Jul  5 20:39 bin drwxrwxr-x  2 tests tests  4096 Apr 30  2021 cifs1 drwxrwxr-x  2 tests tests  4096 Apr 30  2021 cifs2 drwxrwxr-x  2 tests tests  4096 Apr 30  2021 dev lrwxrwxrwx  1 tests tests     7 Jul  5 20:39 etc -> tmp/etc lrwxrwxrwx  1 tests tests     8 Jul  5 20:39 home -> tmp/home drwxrwxr-x  2 tests tests  4096 Apr 30  2021 jffs drwxrwxr-x 11 tests tests  4096 Jul  5 20:39 lib lrwxrwxrwx  1 tests tests     9 Jul  5 20:39 media -> tmp/media drwxrwxr-x  2 tests tests  4096 Apr 30  2021 mmc lrwxrwxrwx  1 tests tests     7 Jul  5 20:39 mnt -> tmp/mnt lrwxrwxrwx  1 tests tests     7 Jul  5 20:39 opt -> tmp/opt drwxrwxr-x  2 tests tests  4096 Apr 30  2021 proc drwxrwxr-x 23 tests tests  4096 Jul  5 20:39 rom lrwxrwxrwx  1 tests tests    13 Jul  5 20:39 root -> tmp/home/root drwxrwxr-x  2 tests tests  4096 Jul  5 20:39 sbin drwxrwxr-x  2 tests tests  4096 Apr 30  2021 sys drwxrwxr-x  2 tests tests  4096 Apr 30  2021 sysroot drwxrwxr-x  2 tests tests  4096 Apr 30  2021 tmp drwxrwxr-x  9 tests tests  4096 Jul  5 20:39 usr lrwxrwxrwx  1 tests tests     7 Jul  5 20:39 var -> tmp/var drwxrwxr-x 14 tests tests 12288 Jul  5 20:39 www

## Slide 17

# **Naive Planning**

_The first cycle._

→ Find/build Cortex A9 QEMU machine with flash memory.

→ Build a 2.6.36.4 kernel using gcc 4.5.3 → Use a defconfig written for the QEMU machine

Add
“hardwareˮ (to
QEMU and/or
the kernel)

Compile kernel & QEMU Run kernel on QEMU machine

→ Pass raw SquashFS filesystem binary (part1) as flash

→ ???

See what  Load firmware
breaks filesystem &
init

## Slide 18

# **Initial Setup**

- → vexpress-a9 board

→ Cortex A9 core

- → Flash memory (pflash).

→ vexpress_defconfig for the 2.6.36.4 Linux kernel

→ Build GCC 4.5.3 from Buildroot 2012.2 first…

## Slide 19

# **First Test**

→ Get the kernel running

→ CONFIG_* audit/checks/changes

→ How to pass a “flashˮ chip?

→ Lay out file as “flashˮ

→ mtdparts boot arg tells the kernel the layout

→ Pass flash as pflash to QEMU

## Slide 20

Flash Layout
64MB
\x00 \x00 SquashFS filesystem (part1)
mtdblock0 mtdblock1 mtdblock2
QEMU
-drive if=pflash,format=raw,file=flash0.img
flash.img
Kernel boot args
mtdparts=armflash:512k(something1),512k(something2),63m(rootfs)

## Slide 21

# **Expecting Failure**

qemu-system-arm -M vexpress-a9 -m 1024 \ -kernel linux-2.6.36.4/arch/arm/boot/zImage \ -drive if=pflash,format=raw,file=flash0.img \ -append "root=/dev/mtdblock2 console=ttyS0 mtdparts=armflash:512k(smth1),512k(smth1),63m(rootfs) mtd_probe=cmdline init=/sbin/preinit"

## _But what kind?_

### → Filesystem doesnʼt unpack! → **Why?**

**... input: AT Raw Set 2 keyboard as /devices/mb:kmi0/serio0/input/input0 input: ImExPS/2 Generic Explorer Mouse as /devices/mb:kmi1/serio1/input/input1** **SQUASHFS error: Filesystem uses "unknown" compression. This is not supported List of all partitions: 1f00             512 mtdblock0 (driver?) 1f01             512 mtdblock1 (driver?) 1f02           63488 mtdblock2 (driver?)** **No filesystem could mount root, tried:  ext3 ext2 cramfs squashfs vfat Kernel panic - not syncing: VFS: Unable to mount root fs on unknown-block(31,2) [<8003c594>] (unwind_backtrace+0x0/0x17c) from [<80402e78>] (panic+0x64/0x190) [<80402e78>] (panic+0x64/0x190) from [<80009194>] (mount_block_root+0x1d0/0x210) [<80009194>] (mount_block_root+0x1d0/0x210) from [<800093f4>] (prepare_namespace+0x12c/0x190) [<800093f4>] (prepare_namespace+0x12c/0x190) from [<80008dbc>] (kernel_init+0x1f4/0x248) [<80008dbc>] (kernel_init+0x1f4/0x248) from [<8003724c>] (kernel_thread_exit+0x0/0x8)**

## Slide 22

**Broadcom Speedbump 1**


> Recovered by OCR — confidence 94/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
News
SquashFS version 4 is
What does it mean for this project (squashfs-lzma.org)? There is no
longer any need to use external patches, so this project is discontinued. You can happily
mount your newly created squashfs images directly with recent kernel! :) This website will
remain with slight updates for reference.
```

## Slide 23

**Broadcom Kernel Changes**

## Slide 24

# **Firmware Unpacks!**

**... IPv6 over IPv4 tunneling driver sit0: Disabled Privacy Extensions ip6tnl0: Disabled Privacy Extensions NET: Registered protocol family 17 Bridge firewalling registered Ebtables v2.0 registered L2TP core driver, V2.0 802.1Q VLAN Support v1.8 Ben Greear <greearb@candelatech.com> All bugs added by David S. Miller <davem@redhat.com> lib80211: common routines for IEEE802.11 drivers VFP support v0.3: implementor 41 architecture 3 part 30 variant 9 rev 0 rtc-pl031 mb:rtc: setting system clock to 2025-07-10 10:18:07 UTC (1752142687) input: AT Raw Set 2 keyboard as /devices/mb:kmi0/serio0/input/input0 input: ImExPS/2 Generic Explorer Mouse as /devices/mb:kmi1/serio1/input/input1** **VFS: Mounted root (squashfs filesystem) readonly on device 31:2. devtmpfs: mounted Freeing init memory: 180K ...**

## Slide 25

# **init=/bin/sh**

VFP support v0.3: implementor 41 architecture 3 part 30 variant 9 rev 0 rtc-pl031 mb:rtc: setting system clock to 2025-07-10 14:27:55 UTC (1752157675) input: AT Raw Set 2 keyboard as /devices/mb:kmi0/serio0/input/input0 input: ImExPS/2 Generic Explorer Mouse as /devices/mb:kmi1/serio1/input/input1 VFS: Mounted root (squashfs filesystem) readonly on device 31:2. devtmpfs: mounted Freeing init memory: 180K / **# ls -al** drwxr-xr-x   18 0        0              325 Apr 30  2021 . drwxr-xr-x   18 0        0              325 Apr 30  2021 .. drwxr-xr-x    2 0        0                3 Apr 30  2021 asus_jffs drwxr-xr-x    2 0        0              667 Apr 30  2021 bin drwxr-xr-x    2 0        0                3 Apr 30  2021 cifs1 drwxr-xr-x    2 0        0                3 Apr 30  2021 cifs2 drwxr-xr-x    4 0        0             2760 Jan  1  1970 dev lrwxrwxrwx    1 0        0                7 Apr 30  2021 etc -> tmp/etc lrwxrwxrwx    1 0        0                8 Apr 30  2021 home -> tmp/home drwxr-xr-x    2 0        0                3 Apr 30  2021 jffs drwxr-xr-x    3 0        0              260 Apr 30  2021 lib lrwxrwxrwx    1 0        0                9 Apr 30  2021 media -> tmp/media drwxr-xr-x    2 0        0                3 Apr 30  2021 mmc lrwxrwxrwx    1 0        0                7 Apr 30  2021 mnt -> tmp/mnt ...

## Slide 26

# **/sbin/preinit**

→ /sbin/rc in preinit mode

→ Mounts sys, dev, tmp, proc, etc.

- → Copies /etc/ from /rom/etc/*

- → Reads NVRAM a lot

→ Brings up network interfaces → & more!

## Slide 27

# **init=/sbin/preinit**

**... input: ImExPS/2 Generic Explorer Mouse as /devices/mb:kmi1/serio1/input/input0 input: AT Raw Set 2 keyboard as /devices/mb:kmi0/serio0/input/input1 VFS: Mounted root (squashfs filesystem) readonly on device 31:2. devtmpfs: mounted Freeing init memory: 180K** **/dev/nvram: No such file or directory /dev/nvram: No such file or directory ## mknod /dev/null: File exists ## mknod /dev/console: File exists** **/dev/nvram: No such file or directory /dev/nvram: No such file or directory /dev/nvram: No such file or directory 1: set_action 0** **/dev/nvram: No such file or directory**

**Hit ENTER for console... firmware version: 3.0.0.4.382_52545-ga0245cc** **/dev/nvram: No such file or directory /dev/nvram: No such file or directory /dev/nvram: No such file or directory ...**

## Slide 28

# **NVRAM 101**

→ Filesystem is r/o, NVRAM is r/w

→ key=value store

→ nvram_get(), nvram_set(), nvram_commit(), etc in libnvram.so


> Recovered by OCR — confidence 86/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
NVRAM 101
> Filesystem is r/o, NVRAM is r/w
> key=value store
> nvram_get(), nvram_set(),
nvram_commit(), etc in libnvram.so
Ate_temp_5G_max=0
Ate_temp_5G_over_sec=
Ate_temp_cpu_limit=115
Ate_temp_cpu_max=0
Ate_temp_cpu_over_sec=
Ate_temp_phy_limit=115
Ate_temp_phy_max=0
Ate_temp_phy_over_sec=
CoBrand=4
DCode=20230328
HwId=A
ICFILTER_MAC=
ICFILTER_MACFILTER_DAYTIME=
MULTIFILTER_MACFILTER_DAYTIME_V2_CONVERTED=1
NVRAMRev=$Rev: 791930 $
OPTUS_MULTIFILTER_ALL=0
OPTUS_MULTIFILTER_ENABLE=
TM_EULA_time=Sat, @5 May 2018 08:33:45 +0100
aae_area=
aae_awsiot_desc_updated=0
aae_portal=
abl_eid=0
acs_version=2
acscli2_acs_restart=1
ahs_bhc_log=/jffs/bhc_chg. log
she Ahr lan 1-—/3affc/hhr chan lan 1
```

## Slide 29

# **libnvram.so**

→ Contains nvram_init(), nvram_get(), nvram_set(), etc.

**nvram_init()** Opens /dev/nvram and stores the fd at a global memory location.

**nvram_get()** read(fd, key, outbuf).

**nvram_set()** write(fd, keyvalpair, ret).

**nvram_commit()** ioctl(fd, 0x48534C46u, 0).

int nvram_init() { int fd; // r0 if ( nvramfd >= 0 ) return 0; fd = open("/dev/nvram", 2); nvramfd = fd; if ( fd >= 0 ) { dword_8C90 = (int)mmap(0, 0x10000u, 1, 1, fd, 0); if ( dword_8C90 != -1 ) { fcntl(nvramfd, 2, 1); return 0; } close(nvramfd); nvramfd = -1; } perror("/dev/nvram"); return *_errno_location(); }

## Slide 30

# **Fake NVRAM in the Kernel**

... static struct miscdevice nvram_miscdev = { .minor = MISC_DYNAMIC_MINOR, .name = "nvram", .fops = &nvram_fops, }; ...

... #define MAX_MSG_LEN 512 #define MAX_FILTER_LIST_ENTRIES 16 #define MAX_FILTER_ENTRY_LEN    32 #define NVRAM_MAX_DEVICE_SIZE (512 * 1024) #define NVRAM_BUFSIZE 0x10000 #define NVRAM_DEVICE "/dev/mtdblock1" ...

### Device at /dev/nvram

Backed by a part of the “flashˮ

... static struct file_operations nvram_fops = { .owner = THIS_MODULE, .read = nvram_read , .write = nvram_write , .mmap    .unlocked_ioctl = nvram_mmap= ,nvram_ioctl , Handles all read(), write(), }; mmap(), ioctl(). ...

## Slide 31

# **Fake NVRAM in the Kernel**

static ssize _ t nvram _ read(struct file *file, char __user *buf, size _ t count)

{ char key[128]; char *ptr, *eq;

nvram_load_from_device();

static ssize_t nvram_write(struct file *file, const char __user *buf, size_t count) {

char *input = NULL; char *key = NULL, *value = NULL; char *eq = NULL;

static long nvram_ioctl(struct file *file, unsigned int cmd, unsigned long arg) {

pid_t pid = current->pid; const char *proc_name = current->comm;

if (cmd == 0x48534C46) pr_warn("NVRAM commit called with 0x%x\n", cmd); return nvram_commit_to_device(); pr_err("NVRAM ioctl called with unknown argument 0x%x\n", cmd); return -EINVAL; }

if (count == 0 || count >= PAGE_SIZE) return -EINVAL;

input = kmalloc(count + 1, GFP_KERNEL); if (!input)

return -ENOMEM;

if (copy_from_user(input, buf, count)) { kfree(input); return -EFAULT; } input[count] = '\0'; pr_warn(proc_name, "[nvram] %s (%d) trying to write key %s\n", proc_name, pid, input); nvram_load_from_device(); eq = strchr(input, '='); if (eq) { *eq = '\0'; key = input; value = eq + 1; } else {

static void nvram _ load _ from _ device(void) { struct file *filp; mm_segment_t oldfs; loff_t pos; ssize_t bytes; char *buf;

if (g_nvram_loaded) return;

buf = kmalloc(NVRAM_BUFSIZE, GFP_KERNEL); if (!buf) return;

pid_t pid = current->pid; const char *proc _ name = current->comm;

key[count] = '\0'; ptr = g_nvram_buf; while (*ptr) {

eq = strchr(ptr, '='); if (!eq) break;

if (strncmp(ptr, key, eq - ptr) == 0 && strlen(key) == (size_t)(eq - ptr)) { char *value = eq + 1; unsigned long offset = value - g_nvram_buf; pr_warn(proc_name, "[nvram] %s (%d) read key %s, value: %s\n", proc _ name, pid, buf, value); return copy_to_user(buf, &offset, sizeof(offset)) ? -EFAULT : sizeof(offset); } ptr += strlen(ptr) + 1; } pr_warn(proc_name, "[nvram] %s (%d) tried to read key %s, but couldn't find it\n", proc_name, pid, buf); return 0; }

## Slide 32

# **Working Fake System-Wide NVRAM**

**admin@RT-AX87U:/tmp/home/root# nvram show**

/dev/nvram device

Persistent

Transferrable

Hackable

... 68feaaa3=1 6e3f7d37=1 767cd197=Sat, 05 May 2018 10:39:08 +0100 ASUS_EULA_time=Sat, 05 May 2018 08:16:43 +0100 AllLED_brightness=255 Ate_runin_skip_stress=0 Ate_temp_2G_limit=115 Ate_temp_2G_max=0 Ate_temp_2G_over_sec= Ate_temp_5G_limit=115 Ate_temp_5G_max=0 Ate_temp_5G_over_sec= Ate_temp_cpu_limit=115 Ate_temp_cpu_max=0 Ate_temp_cpu_over_sec= Ate_temp_phy_limit=115 Ate_temp_phy_max=0 Ate_temp_phy_over_sec= CoBrand=4 ...

## Slide 33

# **What Goes in NVRAM?**

- → No device = no NVRAM dump

- → /sbin/preinit populates “defaultsˮ


> Recovered by OCR — confidence 83/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
What Goes in NVRAM?
restore_defaults = 1;
v5® = fputs("\n## R
restore_defaults_g = restore_defaults;
if ( restore_defaults )
nvram_unset("s _config_state");
nvram_unset (“wp nfig_method") ;
nvram_unset ("w
nvram_unset("wps_re 5
Nvram_unset("wps_proc_mac");
nvram_unset("s
nvram_unset (
nvram_unset ( '
nvram_unset ("wp
v51 = nvram_unset("wps_enr_|
productid = get_productid(v51) ;
v53 = nvram_set("wps_device_name", productid) ;
v54 get_productid(v53) ;
v55 = nvram_set("wps_modelnum", v54);
oring defaults ##\n",
lan_hwaddr = (const char *)get_lan_hwaddr(v55) ;
(FILE *)stderr) ;
nvram_set("sv dy", "O");
nvram_set("j
nvram_unset( (int) "qtn_rest
nvram_set_int("vpnc_sta
nvram_set_int("vpnc_s
nvram_set("apps_ipkg_old", "@");
nvram_set("apps_install_folder
nvram_set("aae_enab
v27 = nvram_get_int("aae_enable");
nvram_set_int("aae_enable", v27 | 2);
v28 = nvram_get_int("aae_enable");
nvram_set_int("aae ab. » v28 | 4);
return nvram_unset((int)"r
»_ flag");
http: //nw-d.
> No device = no NVRAM dump
> /sbin/preinit populates “defaults”
```

## Slide 34

# **Uncharted Waters**

→ /sbin/preinit get further

→ Needs more network interfaces!

... ifconfig: SIOCSIFADDR: No such device generate_wl_para(0x0b6c): unit 0 subunit -1 **eth1: WLC_GET_VAR(cap): No such device eth1: cmd=39 (errno 19): No such device** generate_wl_para(0x0f0a): bw: 0 ...

## Slide 35

# **Patching QEMU**

### Modify vexpress-a9 to add another interface

Modify kernel machine definition to support it


> Recovered by OCR — confidence 84/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Modify vexpress-a9 to add
Patching QEMU > “Sl another interface
static void vexpress_common_init(MachineState *machine) Modify kernel machine
if (nd_table[@].used) { definition to support it
* Ox 2®@@ Second LAN9118 E 1 addition) *
orresponds to
/ TIRQ_V2M_LAN9118 2 in motherboard.h in the mach-vexpress board
if (nd_table[1] .used) {
1an9118_init(&nd_table[1], map[VE_ETHERNET2], pic[32]);
static hwaddr motherboard_legacy_map[] = {
ee #define { (32 + 12) )
ie C53 ax4c JO2000 0x50000000 = #define { { 32 + 13) }
[VE_ETHERNET1] = 0x4e000000, #define || (32 + 15)
[VE_LETHERNET2] = 0x4e800000, #define IRQ_V2M_LAN9118 2 (32 + 32) // ADDED
#define IRQ_V2M PCIE (32 + 17)
```

## Slide 36

# **Patching QEMU**

- → Compile QEMU & kernel

- → Run with new machine

- → Run with more NICs

- **$ qemu-system-arm** **-M bcm4709 -m 1024 \**

- **-kernel zImage \**

- **-drive if=pflash,format=raw,file=flash0.img \**

- **-append "root=/dev/mtdblock2 console=ttyAMA0 mtdparts=armflash:512k(bootloader),512k(nvram),62m(rootfs) mtd_probe=cmdline init=/sbin/preinit" \**

- **-nographic \**

- **-netdev user,id=net0 -net nic,netdev=net0 \**

- **-netdev user,id=net1 -net nic,netdev=net1**

## Slide 37

# **New Errors!**

**...** **cp: can't stat '/jffs/syslog.log': No such file or directory cp: can't stat '/jffs/syslog.log-1': No such file or directory ... wanduck(0)(fo change): state 0, state_old 0, changed 0, wan_state 0. wanduck(0)(all   end): state 0, state_old 0, changed 0, wan_state 0. [register_feature] blockfile registered** **mv: can't rename '/jffs/asd.log': No such file or directory [register_feature] chknvram registered** **mv: can't rename '/jffs/asd.log': No such file or directory [register_feature] misc registered ... Registering HINFO record with values 'ARMV7L'/'LINUX'.** **json_object_from_file: error opening file /jffs/nmp_cl_json.js: No such file or directory /jffs/cert.tgz -C / etc/cert.pem etc/key.pem decomp: gzip -dc /var/lib/misc/rstats-history.gz > /var/tmp/rstats-uncomp != 0 load_history: load failed** **ls: /jffs/usericon/*.log: No such file or directory [rc 710] hour_monitor** **tar: can't open '/jffs/cert.tgz': No such file or directory ...**

## Slide 38

# **preinit Again**

→ preinit creates JFFS2 partitions

→ Based on /proc/mtd map file


> Recovered by OCR — confidence 86/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
preinit Again
if ( !nvram_get_compare_1("jff
return notice_set();
result = wait_action_idle(1®);
if ( result )
result = mtd_getinfo("brcmnand
if ( result )
model = get_model(result) ;
dword_FF5E8 = 0;
cprintf("start jffs2: %d, %d\n"
compare_1 = nvram_get_compare_1("jffs2_format");
if ( compare_1 )
nvram_set("jffs2_format", "");
v3 = model > @x38;
, &blockNum, &partSize) ;
, blockNum, partSize);
int __fastcall mtd_getinfo(const char *al,
> preinit creates JFFS2 partitions
> Based on /proc/mtd map file
FILE *v6; // x7
t result; // x®@
char v9[256]; // [sp+@h] [bp-220h] BYREF
char v10[288]; // [sp+1@@h] [bp-120h] BYREF
v6 = fopen("/p ie
while ( fgets(v1@, 256, v6) )
if ( sscanf(v10, “mtd%d: %x", a2, a3) == 2 && strstr(vl1@,
goto LABEL_9;
_DWORD *a2, _DWORD *a3)
```

## Slide 39

# **What Can We Do?**

flash.bin
64MB
\x00 NVRAM SquashFS filesystem (part1) jffs2 jffs2
mtdblock0 mtdblock1 mtdblock2 mtdblock3 mtdblock4
mtdparts=armflash:512k(bootloader),512k(nvram),58m(rootfs),2m(brcmnand),2m(asus)
admin@RT-AX87U:/tmp/home/root# cat /proc/mtd
dev:    size   erasesize  name
→ CONFIG_JFFS* mtd0: 00080000 00040000 "bootloader"
mtd1: 00080000 00040000 "nvram"
mtd2: 03a00000 00040000 "rootfs"
→ Add more parts to flash mtd3: 00200000 00040000 "brcmnand"
mtd4: 00200000 00040000 "asus"

## Slide 40

# **JFFS Works!**

### → Log files

### → Certificates

**admin@RT-AX87U:/tmp/home/root# ls -al /jffs/ drwxr-xr-x    4 admin    root             0 May  5 06:05 . drwxr-xr-x   18 admin    root           325 Apr 30  2021 .. -rw-rw-rw-    1 admin    root         48554 May  5 06:07 HTTPD_DEBUG.log drwxr--r--    2 admin    root             0 May  5 06:05 asd -rw-rw-rw-    1 admin    root          1821 May  5 06:05 asd.log -rw-rw-rw-    1 admin    root          2078 May  5 06:05 cert.tgz -rw-r--r--    1 admin    root            80 May  5 06:06 nmp_cl_json.js -rw-rw-rw-    1 admin    root         19296 May  5 06:04 syslog.log**

## Slide 41

# **More Errors**

→ /dev/gpio doesnʼt exist

→ Doesnʼt completely block, but nice-to-have

→ Create quick dummy GPIO

**...** **Failed to open /dev/gpio Failed to open /dev/gpio wanduck: delay 3 seconds before the first detect... wanduck: delay 4 seconds before the first detect... wanduck: delay 5 seconds before the first detect... wanduck(0)(first detect start): state 1, state_old 0, changed 0, wan_state 0. ...**

## Slide 42

# **GPIO Hell**

- → Button state is polled

- → Read/write state in <u>libshared.so</u>

- → 0xC0084701 - 0xC0084705 ops


> Recovered by OCR — confidence 85/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
GPIO Hell
> Button state is polled
> Read/write state in Libshared.so
> 0xC88847801 - 8xC8084785 ops
gpiofd = open_dev_gpio();
v3 = gpiofd >= 0;
v3-= 0;
gpiofd_1 = gpiofd;
int _fastcall gpio_write(int pin, int a2)
int gpiofd; // 1@
int gpiofd_1; // r5
int pinbitmap; // 14
int value; // 13
gpiofd = j_gpio_open(®);
gpiofd_1 = gpiofd;
pinbitmap = 1 << pin;
gpio_ioctl(gpiofd, ®xC@0847@1, pinbitmap, pinbitmap) ;
gpio_ioctl(gpiofd_1, ®xC0084705, pinbitmap, pinbitmap) ;
value = pinbitmap;
value = @;
gpio_ioctl(gpiofd_1, ®xC0084703, pinbitmap, value) ;
return close(gpiofd_1) ;
return gpiofd;
gpio_ioctl(gpiofd_1, 0xC@084701, (unsigned int *)((1 << i) & a1), (1 << i) & al);
gpio_ioctl(gpiofd_1, ®xC@084705, (unsigned int *)((1 << i) & al), @);
close(gpiofd_1);
return open_dev_gpio() ;
```

## Slide 43

# **GPIO Hell**

- → Figure out “activeˮ state

- → Reference DTS files

→ Return “highˮ if ACTIVE_LOW on e.g. reset button. Otherwise: boot loop!

## Slide 44

# **NIC Hell**

- → QEMU uses smsc911x

- → Firmware expects BCM57XXX

- → get_phy_status() in libshared.so


> Recovered by OCR — confidence 83/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
NIC Hell
int __fastcall robo_ioctl(int sockfd, int a2, int a3, int a4, int *a5)
int v7; // 16
int result; // 1@
unsigned int *v9[8]; // [sp+®h] [bp-5@h] BYREF
int v1@[12]; // [sp+20h] [bp-3@h) BYREF
memset(v9, @, sizeof(v9));
strcpy((char *)v9, "eth");
v10[@] = v7;
int v4; // x5 v9[4] = (unsigned int *)v10;
int v6; // [sp+Ch] [bp-1Ch] BYREF v10[1] = 0;
]
v10@[2] = *a5;
t = ioctl(sockfd, dword_3EB58[a2], v9);
resu
v2 = j_get_switch();
if ( v2) *aS = v10[2];
{ return result;
fd = socket(2, 2, @);
if ( fd >= 0 ) > QEMU uses smsc911x
{ > Firmware expects BCM57XXX
j_cprintf("et ioctl SIOCG
v2 = V6 & OxIF & al; : + get_phy_status() in libshared.so
close(v4) ;
```

## Slide 45

# **Commit Fraud**

→ Handle these operations in the smsc911x driver.

→ Tell userspace that the interface is “upˮ

static int smsc911x_do_ioctl(struct net_device *dev, struct ifreq *ifr, int cmd) {

... switch (cmd) { ... case SIOCGETCROBORD: if (copy_from_user(&args, ifr->ifr_data, sizeof(args))) return -EFAULT; // Correct structure for BCM5301X? page_reg = args[0]; page = (args[0] >> 16) & 0xffff; reg = args[0] & 0xffff; if ((page == 0x1) && (reg == 0x0)) { int override = 0xffffffff; args[2] = override; } else { ... }

if (copy_to_user(ifr->ifr_data, &args, sizeof(args))) return -EFAULT; return ret;

... default: // This is the original handler ... }

## Slide 46

**admin@RT-AX87U:/tmp/home/root# brctl show bridge name     bridge id               STP enabled     interfaces br0             8000.525400123457       yes             eth1**

# **LAN Plan**

- → The AC87U creates a bridge, adds eth1 to that

- **$ sudo ip tuntap add dev tap0 mode tap $ sudo ip addr add 192.168.1.22/24 dev tap0 $ sudo ip link set tap0 up**

→ Add a TAP device on the host

- → Pass a tap network device to QEMU as the eth1 interface.

- ../../qemu/build/qemu-system-arm -M bcm4709 -m 1024 \

- -kernel ../../linux-2.6.36.4/arch/arm/boot/zImage \

- -drive if=pflash,format=raw,file=flash0.img \

- -append "root=/dev/mtdblock2 console=ttyS0

mtdparts=armflash:512k(bootloader),512k(nvram),58m(rootfs),2m(brcmnand),2m(asus) mtd_probe=cmdline init=/sbin/preinit" \

-nographic \

- -netdev user,id=net0 -net nic,netdev=net0 \

- -netdev tap,id=lan0,ifname=tap0,script=no,downscript=no -net nic,netdev=lan0

## Slide 47

# **It (mostly) works!**

# **DEMO**

## Slide 48

# **It (mostly) works!**

_As much as we need it to, for now._

**httpd**

SSH/telnetd

General configuration

Most other services

WLAN Flash-heavy mechanisms

Use kernel-level logging to see which processes are trying to do what.

## Slide 49

More Devices!
More devices based on BCM4709 work, some with more tweaks than others…
 Other ASUS devices
 Netgear Small tweaks
 Linksys
 Tenda
 Belkin
 TRENDnet
⚠ TPLink
 Phicomm Bigger tweaks
⚠ Xiaomi
 DLink

## Slide 50

# **Conclusions**

→ Still early days/PoC, but it works

- → Relatively light-touch

- → Hybrid QEMU/kernel approach works!

→ Concepts are transportable

→ Porting to other SoCs looking promising

**Questions? Abuse?** @n-o.bsky.social

## Slide 51

# **Appendix: Other Tweaks**

→ Change the pl011 default name from ttyAMA* to ttyS*.

→ Flash layouts are more important in some than others

→ Proprietary mechanisms exist (e.g. Tenda CFM, TPLink bcm_flash_chrdev)

## Slide 52

# **Appendix: Tenda CFM**

→ First 8 bytes of the partition are a header

→ First 4 bytes of the header is the CRC32 of the non-header section → Thatʼs it!

... # Tenda libCfm.so -> get _ cfm _ new _ flag _ from _ mtd( ) crc = zlib.crc32(b"\x00"*(part.size-8)) outfile.write(crc.to _ bytes(4, byteorder="little")) ...

## Slide 53

# **Appendix: Dynamic RE From Kernel**

→ Want to know where ioctls are being issued! → In dummy drivers, use current to get registers → ARM32 link register has return address → Combination mm & task_pt_regs() to get the libname.so+0x<offset>

static int get _ caller _ info(struct caller _ info *info) { struct pt_regs *regs; struct mm_struct *mm; struct vm_area_struct *vma; unsigned long caller_addr; int ret = -1;

if (!info || !current || !(mm = current->mm)) { return -EINVAL; }

regs = task_pt_regs(current); // Use link register (LR) to get the return addre ss caller_addr = regs->ARM_lr;

down_read(&mm->mmap _ sem);

// Find VMA containing the return addres s vma = find_vma(mm, caller_addr); if (vma && vma->vm_start <= caller_addr) { if (vma->vm_file) { char buf[256];

char *path = d _ path(&vma->vm_file->f_path, buf, sizeof(buf)); if (!IS _ ERR(path)) {

**... GetUnitFromIfname(1844) ifname=eth0 wan_up network.c 2919 wan_ifname=eth0 index=0 wan_up 2939 wan_proto**

**[acos_nat_cli hack] udhcpc (10939, libnat.so+0xc474) called ioctl. cmd: 0x800464b2, arg: 0x2. [acos_nat_cli hack] udhcpc (10939, libnat.so+0xc474) called unknown ioctl. cmd: 0x800464b2, arg: 0x2. [Bonjour] Can not open "/proc/printer_status"** **[acos_nat_cli hack] httpd (10955, libnat.so+0x9fe4) called ioctl. cmd: 0x8004643d, arg: 0x7e842d14. [acos_nat_cli hack] httpd (10955, libnat.so+0x9fe4) called ioctl. cmd: 0x8004643d, arg: 0x7e842d14. [Bonjour] Can not open "/proc/printer_status" call add_ns wan_ifname=eth0 route: ioctl 0x890c failed: No such process GetUnitFromIfname(1844) ifname=eth0 ...**

char *filename = strrchr(path, '/'); if (filename) { filename++; // Skip the '/' } else { filename = path; } strncpy(info->lib_name, filename, sizeof(info->lib_name) - 1); info->lib_name[sizeof(info->lib_name) - 1] = '\0'; info->offset = caller_addr - vma->vm_start; ret = 0; } } } up_read(&mm->mmap _ sem); return ret; }

## Slide 54

# **Appendix: Netgear acos_nat_cli**

static int device _ ioctl(struct file *file, unsigned int cmd, unsigned long arg) → Char device { int ret; const pid_t pid = current->pid; → Lots of ioctls to it const char *proc _ name = current->comm; struct caller _ info info; → Dummy driver which catches switch (cmd & 0xFFFFFFFF) { known ioctls and returns 1 case 0x400464aa: // httpd calls IOCTL_AG_REGION_SET in agApi_natSetReadyshareName (libnat.so) ret = 1; break; [...] → Can “do somethingˮ if needed default: if (get_caller_info(&info) != 0) { pr_warn("Couldn't get caller info!"); /bin/mknod -m 755 /dev/acos_nat_cli c 100 0 }; ^  ^  ^ pr_warn("[acos_nat_cli hack] %s (%d, %s+0x%lx) called unknown ioctl. cmd: 0x%x, arg: 0x%lx.\n", |  |  | proc _ name, pid, info.lib _ name, info.offset, cmd, arg); char dev | minor number | ret = 0; major number break; } return ret; }

## Slide 55

# **Appendix: Useful Additions**

→ Global do_execve() logging

- → loglevel=8 to boot args

- → Helps to unpick errors

/ # /etc/system/wait[do_execve] pid=885 comm=sh cmdline="/etc/system/wait"

[do_execve] pid=886 comm=wait cmdline="mkdir -p /tmp/etc/.root" [do_execve] pid=887 comm=wait cmdline="chmod 711 /tmp/etc/.root" [do_execve] pid=888 comm=wait cmdline="mkdir -p /tmp/udev/rules.d" [do_execve] pid=889 comm=wait cmdline="mount -t cgroup -o memory memory /cgroup"

[do_execve] pid=890 comm=wait cmdline="awk -F: /brcmnand/ { print $1 } /proc/mtd"

[do_execve] pid=893 comm=wait cmdline="sed s/mtd/mtdblock/"

[do_execve] pid=894 comm=wait cmdline="mkdir -p /var/config"

[do_execve] pid=896 comm=wait cmdline="mtd_debug info /dev/mtd3"

[do_execve] pid=897 comm=wait cmdline="grep mtd.type"

[do_execve] pid=899 comm=wait cmdline="cut -d  -f2"

[do_execve] pid=898 comm=wait cmdline="cut -d= -f2"
