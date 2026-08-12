---
title: "Help! Linux in my Webcam!"
speakers: ["Mickey Shkatov Jesse Michael"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33/Mickey Shkatov Jesse Michael - Help! Linux in my Webcam!.pdf"
pages: 42
sha256: "05c38889e79c79735b4dab12b992d12b1e6a879a639c024146325492e29fec4d"
text_chars: 6956
ocr_pages: 11
has_ocr: true
redacted_secrets: 0
ocr_confidence: 87.3
ocr_unreliable_blocks: 1
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T07:07:34Z"
---
# Help! Linux in my Webcam!

**Speakers:** Mickey Shkatov Jesse Michael  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33/Mickey Shkatov Jesse Michael - Help! Linux in my Webcam!.pdf` (42 pages)


## Slide 1

## Slide 2

- Mickey and Jesse

- Who are we

## Slide 3

## A long time ago in a computer far,

• I had a web cam


> Recovered by OCR — confidence 89/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
A long time ago in a computer far,
far away...
¢ | had a web cam
```

## Slide 4

## A long time ago in a computer far,

-

- One day my webcam was flaky

- Firmware update?

- Download update package!

## Slide 5

# Background

• Install update package!


> Recovered by OCR — confidence 93/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
License Agreement
Please read the following important information before continuing.
nse Agreement. You must accept the terms of this
ntinuing with the installation.
joes not apply to non
> in conjunction third
I accept the agreement
@ 1 do not accept the agreement
```

## Slide 6

# Background

• Install update package!


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Lenovo Performance/510 Webcam
No device detected, please retry
```

## Slide 7

# Background

### • Install update package!


> Recovered by OCR — confidence 92/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
® Setup - CameraFwTool
Installing
Please wait while Setup installs CameraFwTool on your computer.
Extracting files...
C:\...\Mickey\AppData\Local\Temp\Lenovo\CameraFwTool\HD510\CameraFwTool.exe
DO YOU SEE IT?
```

## Slide 8

# Background

•


> Recovered by OCR — confidence 86/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
¢ Let’s open that folder
Name
Bl Resource
AitUVCExtApi.dll
B auto_update.txt
® CameraFwTool.exe
i CameraFwTool.exe.config
® lenovo_hd510_ota_v4.6.2.bin
log4net.dll
B make_imge.sh
© usb_updater.bin
Size
1KB
195 KB
1KB
1,477 KB
2 KB
4KB
2,084 KB
7,808 KB
275 KB
3 KB
344 KB
100 KB
64 KB
```

## Slide 9

# Background

• Can you see anything interesting?

## Slide 10

# Background

• Can you see anything interesting?


> Recovered by OCR — confidence 78/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
¢ Can you see anything interesting?
o CameraFwlool.exe.contig 2 KB
@ dummy.bin 4KB
BB HD510Sdk.dll 2,084 KB
```

## Slide 11

Background

## Slide 12

# Background • binwalk a little

### • Now we REALLY need to open this thing up!


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
° Ok, let’s binwalk a little
1835008 0x1C0000 gzip compressed data, operating system: Unix,
timestamp: 1970-01-01 00:00:00, total size:
2700525 bytes
4653056 0x4'70000 SquashFS file system, Little endian, version:
4.0, compression: xz, inode count: 26, block
size: 131072, image size: 2654642 bytes, created:
2022-05-21 07:25:29
7471104 0x720000 JFFS2 filesystem, little endian, nodes: 22, total
size: 327692 bytes
¢ Now we REALLY need to open this thing up!
```

## Slide 13

# Background

• BACK

• FRONT

## Slide 14

# Background

8MB
RX
SPI
GND
TX

## Slide 15

UART boot

## Slide 16

## Slide 17

# Background

**.**

**.**

**.** MZ decomp_size=0x0030b000 decomp_size=0x00000000 Booting Linux on physical CPU 0x0 Linux version 4.9.84 (nick@ubuntu) (gcc version 9.1.0 (GCC) ) #445 SMP PREEMPT Tue Mar 22 17:08:22 CST 2022 CPU: ARMv7 Processor [410fc075] revision 5 (ARMv7), cr=50c5387d CPU: div instructions available: patching division code CPU: PIPT / VIPT nonaliasing data cache, VIPT aliasing instruction cache early_atags_to_fdt() success OF: fdt:Machine model: INFINITY6E SSC012B-S01A **. .**

**.** disable sensor FW VERSION:CMK-HD510-OT1917-FW-4.6.2,buildate:Jun  7 2022,20:57:26 (none) login: aision login: can't chdir to home directory '/home/aision' login[496]: root login on 'ttyS0' / #

## Slide 18


> Recovered by OCR — confidence 80/100 on the text kept, 58/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
WHAT KIND DOF DEVICE ] THIS?
OO
DEFCON
```

## Slide 19

# FW Update from UART

• Firmware update flow from inside the device:

## Slide 20

# Update tool flow

CameraFwTool.exe - GUI 1 HD510Sdk.dll DLL Wrapper for the API 2 AitUVCExtApi.dll The API

3

auto_update.txt First Commands

4

- [[ota Second commands

5

FW.bin Firmware file to flash

6

## Slide 21

# Back to the update tool

CameraFwTool.exe - GUI
1
2 HD510Sdk.dll   DLL Wrapper for the API
AitUVCExtApi.dll   The API
3
4 auto_update.txt   First Commands
[[ota   Second commands
5
FW.bin   Firmware file to flash
6

## Slide 22

# Back to the update tool

CameraFwTool.exe - GUI
1
2 HD510Sdk.dll   DLL Wrapper for the API
AitUVCExtApi.dll   The API
3
4 auto_update.txt   First Commands
[[ota   Second commands
5
FW.bin   Firmware file to flash
6

## Slide 23

Back to the update tool


> Recovered by OCR — confidence 90/100 on the text kept, 62/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Back to the update tool
SF: 8060928 bytes @ 0x50000 Written: OK
[UFU runcmd] reset
resetting ...
```

## Slide 24

# Fw update process

• We write a C# tool to flash firmware

• We share everything on GitHub/MEGA

• Links to follow

## Slide 25

Surprise Chain


> Recovered by OCR — confidence 81/100 on the text kept, 42/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Surprise Chain
GG. ~NEXIGO
```

## Slide 26

# Surprise Chain

• SigmaStar websites have documentation

   - <u>https://www.comake.online/3g/index.php?p=products_list &lanmu=2&c_id=11</u>

- Pros:

   - Detail step by step build and toolchain setup

   - Explain the entirety of all the features in the SoC

   - Explain in detail firmware structure

   -

   - Shows hyperlinks to all requires files/sdk/downloads

- Cons:

   - Require authentication to access

## Slide 27

# Surprise Chain

- Trying to get more info about anything

- You have to do everything yourself

- Google

- GitHub

- Forums

- LinkedIn


> Recovered by OCR — confidence 83/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Surprise Chain
¢ Trying to get more info about anything
=
wie
=
WHY IS THIS SO HARD?
¢ You have to do everything yourself
* Google
¢ GitHub
¢ Forums
¢ LinkedIn
Fine, I'll do it myself
```

## Slide 28

# Surprise Chain

- Explore the forums and websites

   - Find references to files and toolchains

      - Google for those files

      - Search for them on GitHub

      - Repeat previous steps with slightly modified names

      -

- Profit

- Bonus points Russian Forums

## Slide 29

# Surprise Chain

- https://github.com/DongshanPI

   - **<u>https://github.com/DongshanPI/SigmaStar-USBDownloadTool</u>**

   - **<u>https://github.com/DongshanPI/Buildroot_SigmastarOriginalSDK</u>**

   - • **<u>https://github.com/DongshanPI/Sigmastar-Linux</u>**

   - **<u>https://github.com/DongshanPI/Sigmastar-Boot</u>**

- http://code.moobox.cn:8002/

- http://www.anjvision.com:8021/

- https://github.com/OpenIPC

## Slide 30

# Surprise Chain

- No help from SoC vendors • TBD There might be something by time this is presented on stage.

- So we ask Lenovo for the GPL code

   - Thanks RFP!

- Get Linux + u-boot sources

   - Build

   - Build fails, missing code

   - Request updated GPL

## Slide 31

# Surprise Chain

• We have the U-Boot and the Kernel , but we • We have a collection of files from GitHub, what can we do?

## Slide 32

# Digging deep

### • Firmware image breakdown (SPI-NOR)

|0x0|IPL|
|---|---|
|0x1000|IPL Customer|
|0x2000|MXPT|
|0x30000|UBOOT|
|0x4F000|UBOOT_Env|
|0x50000|Kernel|
|0x210000|RootFS|
|0x4C0000|Miservice (SquashFS)|
|0x770000|Customer (JFFS2)|

## Slide 33

# Exploitation and Fun

- We know the camera runs linux

- We know we can flash it

- We know how we can flash it

- We know what to put in the flash and where

•

_CAMMY_

## Slide 34

DEMO 1

## Slide 35

DEMO 2

## Slide 36

YOLO /  DEMO 3

## Slide 37

# Exploitation and Fun

- •Go forth and have fun! • Camera on Amazon ($45-$60) <u>https://a.co/d/5P1ACtw</u>

- Cheaper on eBay if you are willing to wait for shipping

- • SPI flash tool ($7 and up) <u>https://hackerwarehouse.com/product/tigard</u>

## Slide 38

# Going beyond Lenovo

- Same SoC in use with other cameras • OBSBot Confirmed newer kernel (5.1) Still waiting on GPL *Insert 0day root here*

- • Opal Tadpole Confirmed linux Still waiting on GPL

## Slide 39

# Going beyond Lenovo

- New age of more linux everywhere

- SoCs now using root of trust and secure boot • Is the age of IoT low hanging fruit coming to an end?

## Slide 40

# Summary

• and Performance FHD were produced in early 2021 and do not support firmware validation. These web cameras have also reached End of development support (EODS), which means

## Slide 41

# Summary

• Lenovo has released a firmware update tool to update U-BOOT to support firmware update signature verification

## Slide 42

Questions
