---
title: "Enabling Security Research on Qualcomm Wifi Chips"
speakers: ["Daniel Wegemer"]
conference: "REcon"
conference_full: "REcon 2023"
edition: ""
year: 2023
source_pdf: "REcon 2023 Slides/Daniel Wegemer_Enabling Security Research on Qualcomm Wifi Chips .pdf"
pages: 43
sha256: "61482f06d55be44b04531bd6c6f12e7932406b2362ddaa34ef30c013175c8a10"
text_chars: 13357
ocr_pages: 1
has_ocr: true
redacted_secrets: 0
ocr_confidence: 92.3
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:01:02Z"
---
# Enabling Security Research on Qualcomm Wifi Chips

**Speakers:** Daniel Wegemer  
**Conference:** REcon 2023  
**Source:** `REcon 2023 Slides/Daniel Wegemer_Enabling Security Research on Qualcomm Wifi Chips .pdf` (43 pages)


## Slide 1

Enabling Security Research on Qualcomm Wifi Chips

RECON Montreal 2023 – Daniel Wegemer

(Qualcomm logo according to Bing AI)

Disclaimer: Opinions are my own and not the views of my employer

## Slide 2

## Motivation

- Wifi chips contain powerful processors

- These processors allow **general purpose computing**

   - Proprietary binaries prohibit running your own code

- Modifying the existing firmware can: • Enable additional functionality

- • Enable security research (dynamic analysis)

https://commons.wikimedia.org/wiki/File:WiFi_Module__ESP8266_%2816730689880%29.jpg

## Slide 3

## Motivation

##### Vendors of Wifi chips:

- **Qualcomm**

- Broadcom

- Intel

- Mediatek

- Texas Instruments

- NXP (former Marvell)

https://aireye.tech/2022/03/29/trends-in-wi-fi-vulnerabilities-this-time-its-qualcomm/

Qualcomm Wifi chips had many high or critical rated vulnerabilities in the past. **How many other vulnerabilities are there?**

## Slide 4

## Motivation

•
Two types of Wifi chips: FullMAC and  SoftMAC FullMAC
SoftMAC
User
wpa_supplicant wpa_supplicant
Space
•
FullMAC implements MAC layer on-
chip, often used for IoT and portable  driver
device driver Host
MAC Layer
Kernel
→ Much bigger firmware
→ Making changes to the driver does
not change the behavior of (FullMAC)  firmware Wifi Chip
firmware
Wifi chips MAC Layer
→ We need to change the Wifi chip
firmware directly PHY Layer PHY Layer

## Slide 5

## Previous Work

- Broadcom Wifi Chips: **Nexmon** Framework

• Allows Wifi firmware patching on many Broadcom chips • Deep modifications on Wifi subsystem possible • See: https://nexmon.org

- **Intel** chips at Blackhat 2022: “Ghost in the Wireless, iwlwifi Edition”

• Qualcomm **Hexagon** based chips at DEFCON 27 and Blackhat 2019: “Exploiting Qualcomm WLAN and Modem Over the Air”

→ This is the first work on **<u>Xtensa based</u>** Qualcomm Wifi firmware

## Slide 6

**Background**

## Slide 7

## Wifi/IoT Chipset Overview

- SoC bundles multiple processors into a single package

- Wifi enabled devices often contain an **application processor** and a **processor** responsible for **Wifi**

- • Timing critical Wifi functionality is sometimes handled by an additional processor

Wifi-SoC
Interconnect
Wifi
Application
Core
Core
Optional:
Real-Time
Core

## Slide 8

## Three types of driver and firmware

- **ath10k** by Qualcomm

- **ath10k-ct** by Candelatech

- **qcacld** by Qualcomm → Used for factory processes

https://www.candelatech.com/

**ath10k-ct** driver can also run QCA firmware

## Slide 9

IPQ4019 (“Habanero” by 8devices)

https://lian-mueller.com/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/h/a/habanero-dvk-top.jpg

## Slide 10

## IPQ4019

- Used mainly in Wifi home routers (e.g. AVM FritzBox)

- • Application Core: ARM Cortex A7 → Runs OpenWRT 19.07 on Kernel 4.14

- • Wifi Subsystem: Cadence/Tensilica Xtensa

   - 2.4 and 5 GHz

   - Uses PCIe to communicate

IPQ4019
Wifi Wifi Ethernet
Debug
Core 1 Core 2 Subsystem
Interconnect
Arm Cortex A7 PCIe
(OpenWRT)

## Slide 11

**Firmware**

## Slide 12

## Firmware: Overview

- Xtensa, little endian

- ROM + RAM

- RAM part of a file in the OpenWRT filesystem → Contains multiple “segments” (aka “SGMT”) → lz77 compressed

- ROM can be patched

- Codeswap: mechanism to put code of Wifi subsystem in the hosts memory

https://www.cadence.com

- No security enabled by default

   - No secure boot

   - No stack canneries

   - No address randomization

## Slide 13

## Firmware: Debugging

Debugfs: /sys/kernel/debug/ieee80211/phy0/ath10k/... → .../ **mem_value** can be used for memory access r+w (only works after core+pci kernel modules are loaded) →.../ **debug_mask** , can be used to increase verbosity. Also possible via module parameter “debug=mask=0xYYY” in ath10k_core.ko

https://patchwork.kernel.org/project/ath10k/patch/1416656922-6645-1-git-send-email-yanbol@qti.qualcomm.com/

## Slide 14

Firmware: Interfaces Interfaces between driver and Wifi subsystem

- **BMI** (Bootloader Messaging Interface)

→ Communicaton between host and Wifi subsystem during bootup

→ Implemented in ROM

- **WMI** (Wireless Module Interface)

   - →Communicaton between host and Wifi subsystem after bootup →Example commands: wifi scanning, channel configuration etc...

## Slide 15

## Firmware: Loading

##### **Two loading methods** possible:

- BMI (Bootloader Messaging Interface)

- Copy Engine: ath10k_hw_diag_fast_download() in ath10k, different in ath10k-ct

- In case of **compressed** firmware:

- BMI method needs to be used

- Decompression done in ROM of Wifi Core

BMI
Firmware Driver Wifi Core

## Slide 16

## Firmware: File Format

IE_HEADERS 1
Magic: “SGMT”
Segment Header 1
Flags: 0x1 (compressed) Driver logs:
Address: 0x409200 (literals base) Metadata 1
Length: 0x170
OTP:
Gets overwritten by 2 nd part
FW PART1 bmi_lz_stream_start()
1. bmi_lz_data(lenght 0x1244)
FW:
METADATA2
bmi_lz_stream_start()
bmi_lz_data(lenght 0x59c96)
...
FW PART2
<do it again…>
IE_HEADERS 2
Magic: “SGMT” Segment Header 2 OTP:
Flags: 0x1 (compressed)
bmi_lz_stream_start()
Address: 0x409200 (literals base) METADATA3
bmi_lz_data(lenght 0x1244)
Length: 0x4018
FW:
bmi_lz_stream_start()
FW PART1
bmi_lz_data(lenght 0x59c96)
2.
METADATA4
FW PART2
Ath10k-ct firmware version:
10.4b-ct-4019-fW-012-17ba98334

## Slide 17

Firmware: Memory Layout Memory contents are repeating:

Ath10k-ct firmware version:  10.4b-ct-4019-fW-012-17ba98334

## Slide 18

**Xtensa Architecture**

## Slide 19

## Xtensa in QCA Wifi chips

- **Literal Pools** are used for “L32R” instructions

   - Loads are **independent** of PC

   - Instead the offset is calculated from a fixed “LITBASE”

- **Call8** is used to move a register window by 8

|**Register**|**Usage**|
|---|---|
|a0|Return address|
|a1|Stack Pointer|
|a2 - a7|Incomingarguments|

- e.g. a10 of caller will be a2 of callee

See also: https://github.com/chipsi007/noduino-sdk/blob/master/bootloader/xtos/reset-vector.S#L302-#L309

## Slide 20

## Xtensa Literal Pools

LITBASE 0xc3834 Memory: my_patch() { Literal Pool: … Target Code: wlan_main() … wlan_main() … … wlan_main() → 0xc3834 }

Memory:

- “wlan_main()” will use a “L32R” instruction to get the target address: LITBASE

   - + offset within Literal Pool (part of L32R)

= Target Address

This calculation is done in every “ **l32r** ” instruction!

## Slide 21

## Xtensa Literal Pools

• **LITBASE** is set at the beginning of FW execution: • For IPQ4019 Literal pool start is at 0x408001 • Code: _l32r a2, lib4_start + 0x40001 wsr a2, LITBASE_

• Existing Wifi firmware code does expect the LITBASE to be set as shown above

## Slide 22

## Xtensa Litbase in Disassemblers

**IDA** 7.7 adds support of Xtensa, but ignores LITBASE

**Ghidra** supports Xtensa using this plugin (https://github.com/yath/ghidra- <u>xtensa) but ignores LITBASE</u>

**Radare2** ignores LITBASE

**Binary Ninja** using this plugin (https://github.com/zackorndorff/binja-xtensa) ignores LITBASE too

## Slide 23

## Xtensa: Disassembler Plugin for Binary Ninja

• Based on https://github.com/zackorndorff/binja-xtensa • Patch: diff --git a/binja_xtensa/instruction.py b/binja_xtensa/instruction.pyindex 7243f07..e7f1700 100644 --- a/binja_xtensa/instruction.py +++ b/binja_xtensa/instruction.py @@ -34,6 +34,8 @@ Link to the Xtensa docs/manual I was referencing: """

from enum import Enum

+LITBASE = 0x408000 + 0x40001 + # https://stackoverflow.com/a/32031543 def sign_extend(value, bits): @@ -233,7 +235,8 @@ class Instruction: def offset_l32r(self, addr): enc = sign_extend(self.imm16 | 0xFFFF0000, 32) << 2 - return (enc + addr + 3) & 0xFFFFFFFC +        return ( **LITBASE** & 0xFFFFF000) + enc

## Slide 24

## Xtensa: Disassembler Plugin for Ghidra

• Based on: https://github.com/Ebiroll/ghidra-xtensa

diff --git a/data/languages/xtensa.sinc b/data/languages/xtensa.sinc • Patch: index 80ac9bf..e8ef5c8 100644 --- a/data/languages/xtensa.sinc +++ b/data/languages/xtensa.sinc @@ -236,7 +236,7 @@ srel_6.23_sb2: rel is s8_6.23 [ ] { export *:4 rel; } srel_8.23_oex_sb2: rel is u16_8.23 [ - rel = ((inst_start + 3) & ~3) + ((u16_8.23 | 0xffff0000) << 2); +    rel = ( **0x448001** & 0xFFFFF000) + ((u16_8.23 | 0xffff0000) << 2); ] { export *:4 rel; }

## Slide 25

# **Firmware patching using Nexmon**

## Slide 26

## Nexmon: Introduction

- Extract ROM, “Flashpatches”, RAM, UCODE for Broadcom Wifi chips

- Write patches in C, call existing firmware functions

- • Compile and link firmware code

- • Create firmware file

Matthias Schulz. Teaching Your Wireless Card New Tricks: Smartphone Performance and Security Enhancements through Wi-Fi Firmware Modifications. Dr.-Ing. thesis, Technische Universität Darmstadt, Germany, February 2018

## Slide 27

## Nexmon: Introduction

patch.c gcc patch.o
1. nexmon.pre
wrapper.c gcc wrapper.o
2. nexmon.pre awk nexmon.ld
*.ld
3. ld patch.elf
*.o
definitions.mk
4. awk nexmon.mk
patch.elf
patch.elf
5. objcopy section.bin dd firmware.bin
nexmon.mk

## Slide 28

## Nexmon: Adaption

Necessary **changes** Qualcomm firmware:

1. Decompress segments from firmware-5.bin

2. Support multiple binaries (one for each segment)

3. Support “LITBASE”

Overview (steps in Makefile):

- Compiles + Links patches

- Copy patches into binary 0x980000 of 2<sup>nd</sup> (decompressed) segment

- Compress segment parts, create 2nd segment

- Adds padding bytes to 2nd segment

- Creates complete binary: firmware-5.bin

## Slide 29

Nexmon: 2. Handle multiple binaries

- GCC Plugin is used to create “nexmon.pre” file

- • This file is also used as input to dd & linker

- Extended to include a file name:

“attribute” in source code

|||Compile|
|---|---|---|
|nexmon.pre|||
|0x00409228
PATCH|obj/patch.o|my_patch
segment2_00409200_mod.bin|
|0x000c3834
DUMMY|obj/wrapper.o|wlan_main
segment2_00980000_mod.bin|

## Slide 30

## Patching Firmware – 1<sup>st</sup> attempt

- Patch goal: write 0x1234 to an address, jump back to original code

- • Use xtensa-esp32-elf-gcc to compile + link LE binary

- • Load into IPQ4019 chip

- • Use DebugFS to read memory after patch has run to check if 0x1234 was written successfully

- → Does not work! Why?

## Slide 31

## Patching Firmware – 1<sup>st</sup> attempt

- L32R uses offset in LITBASE to calculate target address

- LITBASE is set at the very beginning of the FW execution in ROM

   - → Existing code in FW relies on this

- There is no parameter to tell our compiler/linker where an already existing LITERAL POOL is!

## Slide 32

## Patching Firmware – 1<sup>st</sup> attempt

Hack: Avoid L32R instructions

- Use immediate values only

- No references!

- Needs handcrafted Assembly

## Slide 33

## Nexmon: 3. Handle LITBASE

Two possible solutions:

1. Tell Linker where **existing Literal Base** is and how full it is

2. Use our **own LITBASE value**

- → We are going with option **#2!**

Necessary steps:

- Set LITBASE to 0x0 at function **entry** . → This can be done extending Nexmons GCC plugin

- Set LITBASE to original value at function **exit** .

   - → This needs to be done in Binutils assembler because it expands/relaxes calls to a load+call

## Slide 34

## Nexmon: 3. Handle LITBASE

Patching Binutils Assembler “as”

- Needs to be done because of “ **Instruction Relaxation** ” in the assembler

- Relaxation adds a l32r before each call instruction

- The LITBASE used in this l32r needs to point to 0x0.

- Only **after this** we can set the LITBASE back to its original value

→ We can not patch this in GCC, its needs to be patched in the assembler!

## Slide 35

Nexmon: 3. Handle LITBASE

The assembler uses “string patterns” to “relax” instructions:


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Nexmon: 3. Handle LITBASE
The assembler uses “string patterns” to “relax” instructions:
static []
```

## Slide 36

## Nexmon: 3. Handle LITBASE

#### Patching Binutils Assembler “as”

static bool xg_build_to_stack (IStack *istack, TInsn *insn, BuildInstr *bi) { … for (; bi != NULL; bi = bi->next) { +        /* QCAMON: IF CURRENT OPCODE is **callx8** && PREV OPCODE is **l32r** */ +       if(bi->opcode == 0x3a && prev_bi->opcode == 0x86) { +            TInsn *new_ins = (TInsn *) malloc(sizeof(TInsn)); +            tinsn_init (new_ins); **+            build_wsr_litbase_insn(new_ins);** +            new_ins->debug_line = insn->debug_line; +            new_ins->loc_directive_seen = insn->loc_directive_seen; +            istack_push(istack, new_ins); +        } + TInsn *next_insn = istack_push_space (istack); … return true; }

## Slide 37

## Patching Firmware – 2<sup>nd</sup> attempt

- Patch goal: write 0x1234 to an address, jump back to original code

- C-Code can now be used!

- We can use GCC plugin + patched “as” to compile our code

- → Much simpler code

## Slide 38

## Patching Firmware – 2<sup>nd</sup> attempt

Assembly compiled with our GCC plugin and the patched binutils assembler

## Slide 39

## Open Problems

- Binutils patch needs implementation based on using Stack (avoid using a register)

- Support for disassemblers is lacking

- Missing text console in firmware for easier debugging → We can implement this ourselves now!

## Slide 40

### **(lame) Demo Time!**

## Slide 41

## Summary & Future Work

- Modified Nexmon framework can be found here: https://qcamon.org, including:

   - Demo patch

   - patches for Ghidra and Binary Ninja

   - GCC to complie LE Xtensa

   - Patched Binutils

- First POC patch code shows **feasibility of firmware modifications**

- • **Further improvements** will help to make firmware modifications easier and enable security research

- Use “Production Software” ( **QDART** ) by Qualcomm to explore hidden FW functionality

- Explore “ **Codeswap** ” feature of FW

## Slide 42

## Thanks

- Martin Korth (aka ProblemKaputt) for his awesome GBA reverse engineering

- • rqou (aka ArcaneNibble) for “ath10k_unzl.py” script

## Slide 43

# **Q&A**

Visit <u>https://qcamon.org</u> !

Mail: daniel@wegemer.com
