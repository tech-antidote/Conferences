---
title: "Jailbreaking an Electric Vehicle in 2023 or What It Means to Hotwire Tesla's x86-Based Seat Heater"
speakers: ["Christian Werling", "Niclas Kühnapfel", "Hans Niklas Jacob", "Oleg Drokin"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/Christian Werling _ Niclas Kühnapfel  _ Hans Niklas Jacob  _ Oleg Drokin_Jailbreaking an Electric Vehicle in 2023 or What It Means to Hotwire Tesla's x86-Based Seat Heater.pdf"
pages: 92
sha256: "90ec702582fd8fbbc029f42f773a83f87e7bf0585d83fac2736a43b3686c62e4"
text_chars: 30525
ocr_pages: 14
has_ocr: true
redacted_secrets: 0
ocr_confidence: 83.7
ocr_unreliable_blocks: 0
vision_verified_blocks: 3
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:07:33Z"
---
# Jailbreaking an Electric Vehicle in 2023 or What It Means to Hotwire Tesla's x86-Based Seat Heater

**Speakers:** Christian Werling, Niclas Kühnapfel, Hans Niklas Jacob, Oleg Drokin  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Christian Werling _ Niclas Kühnapfel  _ Hans Niklas Jacob  _ Oleg Drokin_Jailbreaking an Electric Vehicle in 2023 or What It Means to Hotwire Tesla's x86-Based Seat Heater.pdf` (92 pages)


## Slide 1

Jailbreaking an Electric Vehicle in 2023 WHAT IT MEANS TO HOTWIRE TESLA'S X86-BASED SEAT HEATER

Chris&an Werling Niclas Kühnapfel TU Berlin Hans Niklas Jacob Oleg Drokin Independent

## Slide 2

# Tesla’s Infotainment Now AMD-Powered

2


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Tesla’s Infotainment Now AMD-Powered
Tesla to Soon Start Delivering Model 3 &
Y with AMD Ryzen Chips to Europe,
Parts Catalog Hints
```

## Slide 3

# Our Previous AMD Research

3


> Recovered by OCR — confidence 82/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
faulTPM: Exposing AMD fTPMs’ Deepest Secrets
Hans Niklas Jacob*, Christian Werling*, Robert Buhren, Jean-Pierre Seifert!
e
Technische Universitit Berlin cT
ur Previous esearc aes
{ hnj, cwerling, roberi.buhren, jpseifert }@sect.tu-berlin.de
One Glitch to Rule Them All: Fault Injection Attacks Against
Uncover, Understand, Own - Regai AMD’s Secure Encrypted Virtualization
trol Over Your AMD CPU
os Robert Buhren Hans Niklas Jacob
robert. buhren@sect.tu-berlin.de hnj@sect.tu-berlin.de
mnische Universitat Berlin - SECT Technische Universitit Berlin - SECT
Mt the
Thilo Krachenfels
‘Technische Universitit Berlin - S Technische Universitat Ber!
Fraunhofer SIT
fonent
Uncover, Understand, Own EM-Fault It Yourself: Building a Replicable EMFI
Setup for Desktop and Server Hardware
Introduce software-
Kiihnapfel*, Robert Buhren*, Hans Niklas Jac Thilo Krachenfe! pe ROR spi
* Technische Universitit Berlin, Chair of Security in Telecommunications, Germany
} Fraunhofer SIT, Germany encryption keys
frure, AMD CPUs
AMD Secure Pro:
One Glitch to Rule Them All: Fault pe vie
Injection Attacks against AMD’s : —
Secure Processor Biicting vos
Hans Niklas cob Technische Universitat Berlin Insecure Until Proven Updated: fs and CPUs.
Analyzing AMD SEV’s Remote Attestation | Pagrethe
Pthe DUT by
Robert Buhren Christian Werling Jean-Pierre Seifert uly changing
robert buhren@sect.tu-berlin.de hhristian.werling@student hpide ipseifert@se Fe. both tech.
Technische Universitt Berlin Hasso Plattner Institute, Potsdam 1 che c to the power
Security in Te fasive attacks.
decapsulated
jon-shiclding
technologies to ng is one of FFI and EMFI
duccepeed Bs and change
to trust the o¢ high availability of
berlin
of this technology. However, outsourcing
prise data comes at a risk, The technical inf | aagetiseiaad
among multiple tenants. Executin the cloud is owned by the cloud provider and thus under his
visor has dir ° mntrol. This J server hardware
hat allow the co-location of multi
AMD Secure Encrypted Virtualization (SEV) claim: - s range fro onfiguration of software componen
of protection in such cloud seenari 'V encrypts the main n government access [8
1 machines with ic keys, the 0 ca ¢ threats, the research community, as well as in
slow secure cloud computing
```

## Slide 4

# Why Jailbreak a Car?

Many reasons:

- to ”look around” (curiosity)

- to replace its soHware

- **to ac&vate so*-locked features**

What you know
What you know
you don’t know
What you don’t know
you don’t know

4

## Slide 5

5


> Recovered by OCR — confidence 92/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
@ tesla.com
< Back to Vehicle Profile
Upgrades
Rear Heated Seats
ers riding experience
```

## Slide 6

# Outline

**1** Analyzing Boot and Firmware Security **2** Hotwiring the Infotainment system **3** ExtracOng Secrets from the Tesla

6

## Slide 7

Model 3 Car Computer

7

## Slide 8

Infotainment and Connec:vity ECU (ICE)

8

## Slide 9

Cooling chassis

9

## Slide 10

Autopilot v3

10

## Slide 11

Infotainment and Connec:vity ECU (ICE)

11

## Slide 12

ICE (Backside)

12

## Slide 13

Gateway
•
NXP MPC5748G µController
•
PowerPC-based
•
FreeRTOS-based OS
•
SD card reader for logs
•
Boots from internal flash
•
manages car confgura:oni
ICE (Backside)

13

## Slide 14

# Car configuraGon

- Stored and managed by the Gateway

- Lists (paid) hardware and soHware features

   - Car performance

   - Ba-ery capacity (for so3ware-locked ba-eries)

   - Level of Autopilot: (Enhanced) Autopilot, Full Self-Driving capability

   - Car region

   - Rear seat heaters

14

## Slide 15

Infotainment APU

- AMD Zen 1 CPU, Vega GPU

- • Linux 5.4

- • Firmware and recovery system on SPI flash

- • System and user par::on on NVMe ICE (Backside)

15

## Slide 16

# Previous Tesla Hacking

- Threat model: _Outsider_ who is remote or in physical proximity

- Goal: Access/control car

**REGULAR EXPLOITATION OF A TESLA MODEL 3 THROUGH CHROMIUM REGEXP**

- SoHware-based vulnerabiliOes: Can be fixed by Tesla over-the-air

16

## Slide 17

# PlaIorm Threats from the _Inside_

- Threat model: Insider who already has **digital and physical access to the car**

- Goal: Tweak car beyond normal flows • acHvate **so#-locked features** without paying

   - li3 repair and regulaHon restricHons

- Insider not limited to soHware-based aYacks

17

## Slide 18

# Verified Boot

**x86**

⏸

**Non-vola(le storage** SPI Flash NVMe

18

## Slide 19

Verified Boot
x86 ⏸ Coreboot
Non-vola(le storage
SPI Flash Coreboot
NVMe

19


> Recovered by OCR — confidence 76/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Verified Boot
Coreboot
Thu Jan 13 14:46:27 UTC 2022 ai 2 2 8836- abt (log leve
PMxC@ STATUS: @x800 BIT11
coreboot-archive/develop/2021.44.25.2-8836-gb025c688348a
Thu Jan 13 14:46:27 UTC 2022 ponecaqe ceaer inal (log level
POST: x41
POST: @x42
POST: 0x43
POST: x36
POST: @x92
POST: x98
SF size 0x2000000 does not correspond to CONFIG_ROM_SIZE
POST: 0x44
‘Thu Jan 13 14:46:27 UTC 2022 raNstage startind (log level
POST: x8@
POST: 0x70
POST: x71
Board name: Spinach
19
```

## Slide 20

# Verified Boot

verifies
Tesla
x86 ⏸ Coreboot
OS Loader
Non-vola(le storage
Tesla
SPI Flash Coreboot
OS Loader
NVMe

20

## Slide 21

# Verified Boot

🔗 verifies
Tesla
x86 ⏸ Coreboot Linux Kernel
OS Loader
Non-vola(le storage
Tesla
SPI Flash Coreboot
OS Loader
Linux
NVMe
kernel

21

## Slide 22

Verified Boot
verifies🔗 🔗 verifies
Tesla
x86 ⏸ Coreboot Linux Kernel Root FS
OS Loader
Non-vola(le storage
Tesla
SPI Flash Coreboot
OS Loader
Linux
NVMe … RootFS A RootFS B … nvme0n2
kernel

22

## Slide 23

# Verified Boot

🔗

🔗

🔗

Tesla
x86 ⏸ Coreboot Linux Kernel Root FS
OS Loader
Non-vola(le storage
Tesla
SPI Flash Coreboot
OS Loader
Linux
NVMe … RootFS A RootFS B … nvme0n2
kernel

23

## Slide 24

How to get a **root shell** Many opOons:

- Spawn serial shell on boot

- • Add  SSH key to `authorized_keys` file

- Add known SSH password

They all require **changes** to the Root file system

# SSH
password
RootFS A

24

## Slide 25

loaded
rejected
Verified Boot
⛔
🔗 🔗 verifies
Tesla
x86 ⏸ Coreboot Linux Kernel Root FS
OS Loader
Non-vola(le storage
Tesla
SPI Flash Coreboot
OS Loader
#
Linux
NVMe … RootFS A RootFS B … nvme0n2
kernel

25

## Slide 26

# dm-verity

- Integrity checking of block devices • When a block is read into memory, it’s hashed in parallel

- Merkle tree used to efficiently store and verify hashes of individual block

   - Trusted root file system represented by root hash

#
# #
01 10 11 00

- Intermediate hashes stored alongside data

19.06.23

26

## Slide 27

# dm-verity **_# Patch_**

19.06.23

27


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 80/100 on the text kept, 80/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
CVE-2024-5838

What happend if we confuse these two
structures?

=> Fake a callable object.

[terminal panel, top right]
DebugPrint: 0x2b200049aa1: [JSArray]
 - map: 0x02b20018d095 <Map[16](PACKED_DOUBLE_ELEMENTS)> [FastProperties]
 - prototype: 0x02b20018ca09 <JSArray[0]>
 - elements: 0x02b200049941 <FixedDoubleArray[43]> [PACKED_DOUBLE_ELEMENTS]
 - length: 43
 - properties: 0x02b200000725 <FixedArray[0]>
 - All own properties (excluding elements): {
    0x2b200000d99: [String] in ReadOnlySpace: #length: 0x02b20028818d <AccessorInfo name= 0x02b200000d99 <String[6
 }
 - elements: 0x02b200049941 <FixedDoubleArray[43]> { // <--- [10]
       0-42: 1.1
 }
...

DebugPrint: 0x266200049a81: [WasmTrustedInstanceData]
 ...
 - dispatch_table_for_imports: 0x266200049a41 <WasmDispatchTable[1]> // <--- [9]
 ...

[terminal panel, bottom right]
Thread 1 "d8" received signal SIGSEGV, Segmentation fault.
0x0000555556896f17 in v8::internal::HeapObject::HeapObjectPrint(std::__Cr::basic_ostream<char, std::__Cr::char_traits<char> >&) ()
LEGEND: STACK | HEAP | CODE | DATA | RWX | RODATA
--------------------------------------------------------------------------------
*RAX  0x2b200000000 <-- 0x40940
 RBX  0x555557f77540 --> 0x555557d93098 (vtable for v8::internal::StdoutStream+24) --> 0x5555567d4200 (v8::internal::StdoutStream::~StdoutStream(
*RCX  0x9999999a
 RDX  0xc
 RDI  0x7fffffffcc58 --> 0x2b200049a41 <-- 0x9a3ff19999999999
 RSI  0x555557f77540 --> 0x555557d93098 (vtable for v8::internal::StdoutStream+24) --> 0x5555567d4200 (v8::internal::StdoutStream::~StdoutStream(
 R8   0x555557f77598 --> 0x555557d930c0 (vtable for v8::internal::StdoutStream+64) --> 0x5555567d4600 (virtual thunk to v8::internal::StdoutStrea
 R9   0x20
 R10  0x7ffff41fddd8 <-- 0x2
*R11  0xafc527c8e4c063c3
 R12  0x555557dea728 (vtable for std::__Cr::basic_ios<char, std::__Cr::char_traits<char> >+16) --> 0x555557b9e530 (std::__Cr::basic_ios<wchar_t,
 R13  0x555557e2f388 (v8::internal::MainCage::base_) --> 0x2b200000000 <-- 0x40940
*R14  0x2b200049a41 <-- 0x9a3ff19999999999
*R15  0x2b200049a40 <-- 0x3ff199999999999a
 RBP  0x7fffffffcc40 --> 0x7fffffffcc70 --> 0x7fffffffcca0 --> 0x7fffffffcce0 --> 0x7ffff41fddf8 <-- ...
 RSP  0x7fffffffcc10 --> 0x555557f77540 --> 0x555557d93098 (vtable for v8::internal::StdoutStream+24) --> 0x5555567d4200 (v8::internal::StdoutSt
 RIP  0x555556896f17 (v8::internal::HeapObject::HeapObjectPrint(std::__Cr::basic_ostream<char, std::__Cr::char_traits<char> >&)+39) <-- movzx eax,
```

## Slide 28

loaded
rejected
Verified Boot
# Patch
🔗 🔗
Tesla
x86 ⏸ Coreboot Linux Kernel Root FS
OS Loader
Non-vola(le storage
Tesla
SPI Flash Coreboot
OS Loader
# #
Linux
NVMe SSD … RootFS A RootFS B … nvme0n2
kernel

28

## Slide 29

loaded
rejected
Verified Boot
⛔
🔗 verifies
Tesla
x86 ⏸ Coreboot Linux Kernel Root FS
OS Loader
Non-vola(le storage
Tesla
SPI Flash Coreboot
OS Loader
# #
Linux
NVMe SSD … RootFS A RootFS B … nvme0n2
kernel

29

## Slide 30

# Tesla OS Loader **_# Patch_**

30


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 85/100 on the text kept, 70/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
CVE-2024-8638

[left panel]
# CMD: /tmp/d8-linux-debug-v8-component-95842/d8 --allow-natives-syntax --jit-fuzzing poc.js
# OUTPUT ==============================================================

#
# Fatal error in ../../src/objects/shared-function-info-inl.h, line 911
# Debug check failed: HasWasmExportedFunctionData().
#
#
#
#FailureMessage Object: 0x7ffd2b60ead0
==== C stack trace ===============================

   /tmp/d8-linux-debug-v8-component-
95842/libv8_libbase.so(v8::base::debug::StackTrace::StackTrace()+0x13) [0x7f831d74b153]
   /tmp/d8-linux-debug-v8-component-95842/libv8_libplatform.so(+0x199ed) [0x7f831d6f39ed]
   /tmp/d8-linux-debug-v8-component-95842/libv8_libbase.so(V8_Fatal(char const*, int, char const*,
...)+0x194) [0x7f831d72c854]
   /tmp/d8-linux-debug-v8-component-95842/libv8_libbase.so(+0x2c265) [0x7f831d72c265]
   /tmp/d8-linux-debug-v8-component-
95842/libv8.so(v8::internal::SharedFunctionInfo::wasm_exported_function_data(v8::internal::PtrComprCage
Base) const+0xa3) [0x7f831a87b143]
   /tmp/d8-linux-debug-v8-component-95842/libv8.so(+0x3ffb012) [0x7f831bdfb012]
   /tmp/d8-linux-debug-v8-component-95842/libv8.so(+0x3fda1fb) [0x7f831bdda1fb]
   /tmp/d8-linux-debug-v8-component-95842/libv8.so(v8::internal::Runtime_WasmCompileWrapper(int,
unsigned long*, v8::internal::Isolate*)+0x90) [0x7f831bdd9a30]
   /tmp/d8-linux-debug-v8-component-95842/libv8.so(+0x1f65dd7) [0x7f8319d65dd7]

[right panel]
d8.test.enableJSPI();
d8.test.installConditionalFeatures();
d8.file.execute('test/mjsunit/wasm/wasm-module-builder.js');
const sig = makeSig([kWasmI32], []);
const builder = new WasmModuleBuilder();
const _type = builder.addType(sig);
const _import = builder.addImport('m', 'foo', _type);
const _table = builder.addTable(kWasmAnyFunc, 10).index;
builder.addExportOfKind(sig, builder, _import, _table);
builder.addFunction('main', _type).addBody([
  kExprLocalGet, 0,
  kExprI32Const, 0,
  kExprTableGet, _table,
  kGCPrefix,
  kExprRefCast, _type,
  kExprCallRef, _type
]).exportFunc();
const func = new WebAssembly.Function(
  { parameters: ['i32'], results: [] },
  () => 12);
const instance = builder.instantiate({ 'm': { 'foo': func } });
instance.exports.main(15);
```

## Slide 31

# Tesla OS Loader **_# Patch_**

31


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 75/100 on the text kept, 72/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Motivation

What's being sent?          Is the encryption sound?          Why custom encryption?

[Wireshark packet list]
No.      | Time  | Source        | Destination    | Protocol | Length | Info
  33 170...  Android.local  43.130.30.2...  HTTP       652  POST /mmtls/7d44b6a2 HTTP/1.1
  76 170...  Android.local  49.51.67.253    HTTP       658  POST /mmtls/2a9b1264 HTTP/1.1
  92 170...  Android.local  49.51.67.253    HTTP       392  POST /mmtls/2a9b1264 HTTP/1.1
 111 170...  Android.local  49.51.67.253    HTTP       713  POST /mmtls/582198f5 HTTP/1.1
 116 170...  Android.local  49.51.67.253    HTTP       863  POST /mmtls/582198f5 HTTP/1.1
 121 170...  Android.local  49.51.67.253    HTTP       670  POST /mmtls/582198f5 HTTP/1.1
 126 170...  Android.local  49.51.67.253    HTTP       670  POST /mmtls/582198f5 HTTP/1.1
 134 170...  Android.local  49.51.67.253    HTTP       730  POST /mmtls/582198f5 HTTP/1.1

[packet detail pane - lines clipped at pane edge]
> Frame 92: 392 bytes on wir
> Ethernet II, Src: Android.
> Internet Protocol Version
> Transmission Control Proto
> [5 Reassembled TCP Segment
> Hypertext Transfer Protoco
> Data (5704 bytes)

[hex pane]
00e0   43 6c 69 65 6e 74 0d 0a   0d 0a 19 f1 04 00 a1 00
00f0   00 00 9d 01 04 f1 01 00   a8 4f 67 76 fb b4 66 8f
0100   2a 36 bb 55 74 94 c4 0c   cd c8 bb f4 44 41 b0 24
0110   d8 8e c4 86 29 cc 35 e2   1b 65 6e 78 3c 00 00 00
0120   6f 01 00 00 00 6a 00 0f   01 00 00 00 63 01 00 09
0130   3a 80 00 00 00 00 00 3d   00 0c ce 4f 44 55 2e a9
0140   34 fc aa d4 e9 af 00 48   00 f2 e6 a8 76 9f b1 1a
0150   95 cc b8 9b aa 47 4a 75   e1 41 fc ef 7a f6 fc ba
0160   89 30 ca 4e ff fe dc 68   23 bb fe 14 69 09 64 54
0170   0b 40 a4 49 9b d5 6f 7b   69 7f 3e e6 9e 2b 18 fe
0180   75 68 6c b5 15 70 80 a6   06 59 9e 00 f8 bc 1f 3e
```

## Slide 32

loaded
rejected
Verified Boot
🔗 # Patch
Tesla
x86 ⏸ Coreboot Linux Kernel Root FS
OS Loader
Non-vola(le storage
#
Tesla
SPI Flash Coreboot
OS Loader
# #
Linux
NVMe SSD … RootFS A RootFS B … nvme0n2
kernel

32

## Slide 33

loaded
rejected
Verified Boot
⛔
verifies
Tesla
x86 ⏸ Coreboot Linux Kernel Root FS
OS Loader
Non-vola(le storage
#
Tesla
SPI Flash Coreboot
OS Loader
# #
Linux
NVMe SSD … RootFS A RootFS B … nvme0n2
kernel

33

## Slide 34

loaded
rejected
Verified Boot
# Patch
Tesla
x86 ⏸ Coreboot Linux Kernel Root FS
OS Loader
Non-vola(le storage
# #
Tesla
SPI Flash Coreboot
OS Loader
# #
Linux
NVMe SSD … RootFS A RootFS B … nvme0n2
kernel

34

## Slide 35

loaded
rejected
Verified Boot
⛔
⁉ verifies
Tesla
x86 ⏸ Coreboot Linux Kernel Root FS
OS Loader
Non-vola(le storage
# #
Tesla
SPI Flash Coreboot
OS Loader
# #
Linux
NVMe SSD … RootFS A RootFS B … nvme0n2
kernel

35

## Slide 36

# AMD Secure Processor

- ARMv7 µController

- Integrated into CPU SoC

- Highly privileged

- Variety of responsibiliOes

SP
APU

- Hardware root of trust

- Firmware TPM (fTPM) for key management and more

- (On EPYC Servers) Secure Encrypted VirtualizaHon

36

## Slide 37

loaded
rejected
AMD PlaIorm Secure Boot
Tesla
x86 ⏸ Coreboot Linux Kernel Root FS
OS Loader
⛔
verifies
ROM
Off-Chip
AMD SP ▶
Boot Loader Boot Loader
Non-vola(le storage
# #
AMD Root  Tesla
Off-Chip Boot
SPI Flash Coreboot
Key Loader OS Loader
# #
Linux
NVMe SSD … RootFS A RootFS B … nvme0n2
kernel

37

## Slide 38

loaded
rejected
AMD PlaIorm Secure Boot
Tesla
x86 ⏸ Coreboot Linux Kernel Root FS
OS Loader
# Patch
verifies
ROM
Off-Chip
AMD SP ▶
Boot Loader Boot Loader
Non-vola(le storage
# # #
AMD Root  Tesla
Off-Chip Boot
SPI Flash Coreboot
Key Loader OS Loader
# #
Linux
NVMe SSD … RootFS A RootFS B … nvme0n2
kernel

38

## Slide 39

# AMD PlaIorm Secure Boot

loaded
rejected

Tesla
x86 ⏸ Coreboot Linux Kernel Root FS
OS Loader
⛔
ROMROM verifies Off-ChipOff-Chip
AMD SP ▶
BoB o ot Loadert Loader Boot LoaderBoot Loader
Non-vola(le storage
# # #
AMD Root  Tesla
Of-Chip Boot  f
SPI Flash Coreboot
Key Loader OS Loader
# #
Linux
NVMe SSD … RootFS A RootFS B … nvme0n2
kernel

39

## Slide 40

# Previous AMD SP VulnerabiliGes

- 2019: Off-Chip Boot Loader Buffer overflow

⛔
ROM verifes i
Off-Chip
AMD SP
Boot Loader Boot Loader
Non-vola(le storage
#
AMD Root
Off-Chip Boot
SPI Flash
Key Loader

   - ✅

   - • Arbitrary Code ExecuHon

   - **Fixed via firmware updates**

- 2020: ROM Boot Loader Buffer overflow

   - ✅

   - • Arbitrary Code ExecuHon

   - Not fixable (ROM)

   - Fixed in new generaHons (>= Zen 2)

   - **Fixes backported to Tesla’s Zen 1 APU**

40

## Slide 41

# Tesla’s Security EvoluGon

2014

- Open X servers

- Hardcoded passwords

- DiagnosOc Ethernet: root

2023

   - Firmware and OS signing

   - Chain of trust during boot

   - **Root of trust in AMD SoC**

- No code signing

41

## Slide 42

# Outline

**1** Analyzing Boot and Firmware Security **2** Hotwiring the Infotainment system **3** ExtracOng Secrets from the Tesla

42

## Slide 43

loaded
rejected
Regular Early Boot VerificaGon
ROM Boot Loader
Of-Chip f
AMD SP Load Compare to hash Load & Verify
Boot Loader
ARK Hash
Non-vola(le storage
Of Off-Chip Boot  -Chip Boot  f
SPI Flash AMD Root Key
Loader Loader

# Regular Early Boot VerificaGon

43

## Slide 44

# Failed Early Boot VerificaGon

loaded
rejected

ROM Boot Loader
AMD SP Load Compare to hash ⛔
ARK Hash
Non-vola(le storage
Patched
Off-Chip Boot Off-Chip Boot
SPI Flash AMD Root Key
LoaderLoader

44

## Slide 45

# Fault InjecGon AQacks

**Induce fault by altering the IC’s environment:**

- Laser, electromagneHc-radiaHon, clock, supply voltage

## **Voltage Glitching:**

- Lowering voltage shortly

_width_

_fall *me_

_rise *me_

45

## Slide 46

# Key Challenges

- **Most faults are “useless”**

- **Trigger:** Figure out when targeted check happens

- **Parameters:** Voltage drop steepness, width, minimum

- **Reset/Success:** IdenOfy failed aYacks and retry as fast as possible

Glitch

if input() ==
“teslaSecret123”
System Lock,
Con&nue  Ignore
Reset,
normally comparison
Error
print(„Incorrect!“)

\```
print(„Correct!“)
\```

46

## Slide 47

loaded
rejected
Failed Early Boot VerificaGon
ROM Boot Loader
AMD SP Load Compare to hash ⛔
ARK Hash
Non-vola(le storage
#
Off-Chip Boot Off-Chip Boot
SPI Flash AMD Root Key
LoaderLoader

# Failed Early Boot VerificaGon

47

## Slide 48

loaded
rejected
Glitched Early Boot VerificaGon
ROM Boot Loader
Off-Chip
AMD SP Load Compare to hash ✅ Load & Verify
Boot Loader
ARK Hash
Non-vola(le storage
# #
Off-Chip Boot Off-Chip Boot
SPI Flash AMD Root Key
LoaderLoader
Glitch

48

## Slide 49

# Finding the ARK VerificaGon Time Window

Load ARK Verify ARK Load & Verify Off-Chip BL?
Original ARK
SPI bus
ARK bytes
Modified ARK
⛔
SPI bus

49

## Slide 50

AMD SoC
VR
VSoC
SVI2 AMD SP
VCORE
SMU
x86 cores

# Dynamic Voltage Control

- SMU monitors SoC and uses the SVI2 bus to communicate with the external voltage regulator (VR)

- • SVI2 allows to control two voltage domains per VR

50

## Slide 51

AMD SoC
ATX reset
Teensy
µController VR
VSoC
SVI2 AMD SP
FLASH
VCORE
SMU
SPI
Glitch Setup
• Teensy
• Inject SVI2 packets
• Resets target via ATX reset line
x86 cores
• Monitors the SPI bus (CS) to trigger

   - Resets target via ATX reset line

   - • Monitors the SPI bus (CS) to trigger voltage glitch

- External PC controls glitch parameters

51

## Slide 52

# Voltage Glitch Wiring

SVI2 bus (SVD + SVC)

SPI chip-select

52

## Slide 53

Glitch Setup in Reality
SVI2 bus
Teensy
µController
SPI bus
ATX reset
SPI programmer
Serial output

53

## Slide 54

# Voltage Glitch Steps

**SVI2 SVC SVI2 SVD**

VSoC

**SPI CS** failed

**SPI CS**

success

- SVI2 SVC: bus clock

   - VSoC: target’s voltage

- SVI2 SVD: bus data

- SPI CS: chip-select signal

54

## Slide 55

# Voltage Glitch Steps

SVI2 SVC
SVI2 SVD
VSoC
SPI CS
failed
SPI CS
success

- SoC sets iniHal voltage

- SVD rising edge triggers a-ack logic

- VSoC rises

55

## Slide 56

# Voltage Glitch Steps

SVI2 SVC
SVI2 SVD
VSoC
SPI CS
failed
SPI CS
success

- VR sends telemetry packets

- VSoC stable

56

## Slide 57

# Voltage Glitch Steps

SVI2 SVC
SVI2 SVD
VSoC
SPI CS
failed
SPI CS
success

- Teensy injects SVI2 packets

   - VSoC is adjusted

- Disable telemetry to avoid collisions

57

## Slide 58

# Voltage Glitch Steps

SVI2 SVC
SVI2 SVD
VSoC
SPI CS
failed
SPI CS
success

- Teensy starts counHng CS edges to trigger glitch on Hme

- CS becomes acHve à AMD SP loads data

58

## Slide 59

# Voltage Glitch Steps

SVI2 SVC
SVI2 SVD
VSoC
SPI CS
failed
SPI CS
success

- Teensy injects two SVI2 packets to create voltage disturbance

- Voltage drop on VSoC (glitch)

59

## Slide 60

# Voltage Glitch Steps

SVI2 SVC
SVI2 SVD
VSoC
SPI CS
failed
SPI CS
success

- Teensy monitors CS to detect success

   - CS inacHve (high) à failed a-empt

- Teensy resets target on fail

- CS acHve (low) à successful a-empt

60

## Slide 61

loaded
rejected
AMD PlaIorm Secure Boot
Tesla
x86 ⏸ Coreboot Linux Kernel Root FS
OS Loader
⛔
ROMROM verifies Off-ChipOff-Chip
AMD SP ▶
BoB o ot Loadert Loader Boot LoaderBoot Loader
Non-vola(le storage
# # #
AMD Root  Tesla
Of-Chip Boot  f
SPI Flash Coreboot
Key Loader OS Loader
# #
Linux
NVMe SSD … RootFS A RootFS B … nvme0n2
kernel

61

## Slide 62

loaded
rejected
AMD PlaIorm Secure Boot
Tesla
x86 ⏸ Coreboot Linux Kernel Root FS
OS Loader
ROMROM
Off-Chip
AMD SP ▶
BoB o ot Loadert Loader Boot Loader
Non-vola(le storage
# # # #
AMD Root  Tesla
Off-Chip Boot
SPI Flash Coreboot
Key Loader OS Loader
# #
Linux
NVMe … RootFS A RootFS B … nvme0n2
kernel
Glitch

62

## Slide 63

Trying to AcGvate the Rear Seat Heaters

63

## Slide 64

# Finding their ConfiguraGon ID

64


> Recovered by OCR — confidence 86/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Finding their Configuration ID
2 "accessId": 13,
3 "codeKey": "rearSeatHeaters",
5 "enums": [
6 {
7 "codeKey": "NONE",
8 "description": "None",
9 "value": 0
10 }
11 {
12 "codeKey": "KONGSBERG_LOW_POWER",
25, "description": "Kongsberg Low-power heaters",
14 "value": 1
15 }
16 J
17 },
18 "description": "Type of rear seat heaters installed",
19 "nroducts": [
20 "Model3",
21 "Modely"
22 J
23 }
```

## Slide 65

Serial console
A^ack script
SSH console

65


> Recovered by OCR — confidence 72/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
deploy@psp-deploy:~/tesla—-hacking$ picocom /dev/ttyUSBHUB1® —b 115200 | tee -a $(|deploy@psp-deploy:~/tesla/fi-attack$ python3 start-tesla.py -r ../../tesla-hacking/
Serial console
Attack script
deploy@psp-deploy:~$ ssh -t root@192.168.90.10@ ‘bash’
SSH console
```

## Slide 66

Trying to AcGvate the Rear Seat Heaters

66

## Slide 67

# What About Persistence?

- Sorry, voltage glitch is not persistent

   - Need to glitch on every Infotainment boot

   - But the car configuraHon survives regular infotainment (re)boot

   - And Infotainment supposedly doesn’t reboot very o3en

- Glitching could be made even smoother by a mod chip/PCB 🙃

- • ImplementaHon detail …

   - _We leave this as an exercise to the interested audience_

67

## Slide 68

# Secure ConfiguraGon Items

- Demo possible since the rear seat heaters were an “insecure configuraOon item” in our Gateway firmware version

   - ”Secure configuraHon items” can only be changed with a valid signature

- “ **Rear seat heaters were upgraded to be a signed configura4on star4ng in the 2022.44 release** ”, Tesla told us

- So being root on the Infotainment is not sufficient

   - So3ware or hardware vulnerability in Gateway necessary

68

## Slide 69

69


> Recovered by OCR — confidence 95/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ZERO DAY
INITIATIVE
PRIVACY WHO WE ARE HOW IT WORKS BLOG ADVISORIES LOGIN | SIGN UP
July 18th, 2023
(Pwn20wn) Tesla Model 3 Gateway Firmware Signature Validation Bypass Vulnerability
ZDI-23-972
ZDI-CAN-20734
CVSS SCORE
AFFECTED VENDORS
AFFECTED PRODUCTS
VULNERABILITY DETAILS
ADDITIONAL DETAILS
CVE-2023-32156
Tesla
Model 3
This vulnerability allows network-adjacent attackers to execute arbitrary code on affected Tesla Model 3 vehicles. An attacker
must first obtain the ability to execute privileged code on the Tesla infotainment system in order to exploit this vulnerability.
The specific flaw exists within the handling of firmware updates. The issue results from improper error-handling during the
update process,
Fixed in 2023.12 firmware release.
69
```

## Slide 70

# Outline

**1** Analyzing Boot and Firmware Security **2** Hotwiring the Infotainment system **3** ExtracOng Secrets from the Tesla

70

## Slide 71

# What secrets are there on the Tesla?

CAR CREDENTIALS

USER DATA

- Authen'cates car against Tesla servers (Tesla’s car VPN)

   - Firmware updates

   - Car configura:on

   - Phones connected via Bluetooth

      - Contacts, calendar, call logs ...

   - Loca'ons visited

- Bound to Vehicle Iden'fica'on Number (VIN)

   - WiFi passwords

   - Spo'fy and Gmail session cookies

- Used to remotely (de-)authorize services

71

## Slide 72

# How are these secrets secured?

- Everything used to be cleartext

   - Car CredenHals on SD card, on storage

   - User data on cleartext storage parHHon

- Now there is TPM-based security

   - Car Creds sealed in TPM

   - User data parHHon encrypted, key sealed in TPM

72

19.06.23

## Slide 73

# What we extracted

- We wrote a paper on aYacking AMD’s fTPM

   - ExtracHng the TPM’s internal state

   - **_Unsealing arbitrary TPM objects_**

- We extracted the car credenOals à giving us access to Tesla’s server endpoints meant for cars

- We extracted the encrypted user parOOon’s disk encrypOon keys à we have access to user data

73

## Slide 74

# Where in the boot is the fTPM?

x86 ⏸ ▶ Opera:ng System
Key pls? 🔑
ROM Secure OS
Off-Chip
AMD SP ▶
Boot Loader Boot Loader µKernel fTPM App …
Non-vola(le storage
🔓
AMD Root  AMD SP
Off-Chip
SPI Flash x86 Firmware
Key Boot Loader Firmware
NVMe x86 OperaRng System 🔐 User Data

74

## Slide 75

# Where in the boot is the fTPM?

x86 ⏸ ▶ Opera:ng System
unseal 🔑
ROM Secure OS
Off-Chip
AMD SP
Boot Loader Boot Loader µKernel fTPM App …
Non-vola(le storage
🔓
AMD Root  AMD SP
Off-Chip
SPI Flash x86 Firmware NV Data
Key Boot Loader Firmware
Sealed
NVMe x86 OperaRng System 🔐 User Data
Disk Key

75

## Slide 76

# TPM Objects

- Public Part

   - Metadata

      - Which algorithm (AES, RSA, ECC, ...)

      - When and how can the object be used (policy)

   - Public key (if asymmetric algo.)

- Private Part

   - (Private) key

   - Auth value (for user input policy)

   - Seed value

   - Encrypted, integrity-protected

TPM Object

## **Public Part**

algorithm: RSA usage: sign=with pin en/decrypt=never copy=never

public key: c28e f334 c9...

## **Private Part**

private key: 3175 4088 06... auth value: hash(PIN 1, 2, 3, 4) seed value: adf9 8dd3 0e...

76

## Slide 77

Parent Object (loaded)
Public Part
🔓
Private Part
Seed value
TPM Object
KDF Public Part
🔒
🔑 Storage/Integrity Keys Private Part

# TPM Object Sealing

- Objects are sealed using a parent object

- TPM Spec. gives sealing algorithms

77

## Slide 78

# TPM Object Hierarchies

- TPM objects form a forest (mulOple trees)

- Roots: Primary objects • Derived from one of three primary seeds

- Need to walk hierarchy to unseal/load object

stored on TPM
*is there* persistently
Primary Seed
derives derives
derive
Primary
Primary derived
Object
Object
seals seals
load
TPM Object TPM Object
seals
seals
seals
TPM Object seals loaded
seals
TPM Object TPM Object TPM Object
TPM Object TPM Object TPM Object

unseal

78

## Slide 79

# The Non-VolaGle fTPM Data

- On SPI flash chip

   - Primary seeds, persistent counters, etc.

- Encrypted and integrity-protected

- We reverse-engineered the key derivaOon

- **Chip-unique secret** locked in CCP storage

   - Can only be used as AES key

- But we can extract intermediate value

ARK

79

## Slide 80

# Where in the boot is the fTPM?

leak
x86 ⏸ ▶
ROM Secure OS
Off-Chip
AMD SP Payload
🔑 Boot Loader Boot Loader µKernel fTPM App etc.
Non-vola(le storage
# #
AMD Root  AMD SP
Off-Chip
SPI Flash x86 Firmware NV Data 🔐
Key Boot Loader Firmware
NVMe x86 OperaRng System
Glitch

80

## Slide 81

How do we unseal a TPM Object?

Primary Seed
✅
derives derives❓
Primary
Primary
Object✅ Object
❓
(cache)
seals
seals✅
TPM Object TPM Object
✅
seals
seals
seals✅
TPM Object seals
seals
TPM Object TPM Object TPM Object
TPM Object TPM Object TPM Object
✅

- TPM objects are stored externally

- Sealing is defined in TPM spec.

- Primary objects: • Some are cached in NV data (see faulTPM)

   - Seeds should be in NV data

   - DerivaHon only loosely specified!

81

## Slide 82

# Primary Object DerivaGon

- Most fields come from the input “template”

   - Metadata, AuthorizaHon,  …

- Other fields are derived from a **determinis4c random bit generator (DRBG)**

   - Seeded with template and seed

   - **Algorithm not specified by spec.** à **reverse engineering**

Template

Primary Object
Public Part
algorithm: ECC
usage: …
public key: c28e f334 c9...

Public Part
algorithm: ECC
usage: …
public key: c28e f334 c9...
Private Part
private key: 3175 4088 06...
DRBG
auth value: …
seed value: adf9 8dd3 0e...
Primary Seed

82

## Slide 83

fTPM Unsealing AQack Recap
Primary Seed
✅
derives derives✅
Primary
Primary
NV Data
Object✅ Object
✅
NV Data🔐 (cache)
seals
seals✅
TPM Object TPM Object
✅
seals
seals
leak
seals✅
TPM Object seals
Payload seals
TPM Object TPM Object TPM Object
TPM Object TPM Object TPM Object
✅

83

## Slide 84

# Finding the Car CredenGals

TPM Object

84


> Recovered by OCR — confidence 82/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Finding the Car Credentials
x hnj@piepmatz: ~/Projects/psp/tesia/ftpm-offline Qe
(venv) hnj@piepmatz:~/Projects/psp/tesla/ftpm-offline$ cat ../car_creds/car.key
----4BEGIN TSS2 PRIVATE KEY;----
=
H
——- END TSS2 PRIVATE KEY-----
(venv) hnj@piepmatz:~/Projects/psp/tesla/ftpm-offlines Jj
84
```

## Slide 85

# Unsealing the Car CredenGals

NV Data🔐

leak
TPM Object
Payload

85


> Recovered by OCR — confidence 84/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Unsealing the Car Credentials
(venv) hnj@piepmatz:~/Projects/psp/tesla/ftpm-offline$ python3 unseal-tesla-car-creds.py from-image
../boot_nvme.bin $(xxd -p -c32 ../ftpm-seed.bin) ../car_creds/car.key >../car_creds/car.key.clear
=---5 BEGIN PRIVATE KEY-----
(venv) hnj@piepmatz :~/Projects/psp/tesla/ftpm-offlineS [J
85
```

## Slide 86

Finally: ExtracGng the Car CredenGals

Using the Car CredenGals

86


> Recovered by OCR — confidence 85/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
x hnj@piepmatz: ~/Projects/psp/tesla/ftpm-offline QqQn «a
(venv) hnj@piepmatz:~/Projects/psp/tesla/ftpm-offline$ echo -e "GET /mothership/vehicles// HTTP/1.0\r\n"
| openssl s_client -connect api-prd.vn.tesla.services:443 -cert ../car_creds/car.crt -verify_quiet -quiet -ign_eof -nocomm
ands -key ../car_creds/car.key.clear
depth=@ CN = api-prd.vn.tesla.services, OU = Tesla Motors, O = Tesla, L = Palo Alto, ST = California, C = US
verify error :num=2@:unable to get local issuer certificate
depth=@ CN = api-prd.vn.tesla.services, OU = Tesla Motors, O = Tesla, L = Palo Alto, ST = California, C = US
verify error:num=21:unable to verify the first certificate
HTTP/1.1 200 OK
Date: Wed, 26 Jul 2023 = GMT
Content-Type: application/json; charset=utf-8
Connection: close
Cache-Control: no-cache
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block e .
X-Content-Type-Options: nosniff U Sl ng t al e Ca r Cred e nt a Is
X-Download-Options: noopen
X-Permitted-Cross-Domain-Policies: none
Referrer-Policy: strict-origin-when-cross-origin
Cache-Control: max-age=8, private, must-revalidate
X-Runtine: i
Strict-Transport-Security: max-age=31536000; includeSubDomains
Content-Security-Policy: default-sre ‘none’
y":"US", "backseat_token" :null, "backseat_token_updated_at" :null, "radio_config" :null, “service_possession" :false, "hermes_capa
connection_region" :"aws:us-west-2", "birthplace" :"fremont-factory”, "do_not_disturb_until":null, “device_type":"vehicle", “is_
(venv) hnj@piepmatz:~/Projects/psp/tesla/ftpm-offlines |
86
```

## Slide 87

# ExtracGng the Disk EncrypGon Keys

|TPM Object|
|---|

87


> Recovered by OCR — confidence 85/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Extracting the Disk Encryption Keys
[root@fatbox3 ~]# cryptsetup -v LuksOpen --header /tmp/m3/var.luks /tmp/m3/var m
a|3-var --key-file /tmp/m3/var.key
No usable token is available.
iKey slot @ unlocked.
Command successful.
[rootefatbox3 ~]# cryptsetup -v LuksOpen --header /tmp/m3/home.luks /tmp/m3/home
bash-3.2# strings /dev/tle/home.luks | grep -m 1 sealed | jq
"af": 4 : No usable token is available.
Command successful.
[root@fatbox3 ~]# blkid /dev/mapper/m3-home
/dev/mapper/m3-home: LABEL="Home" UUID=""
OCK_SIZE="4096" TYPE="ext4"
[root@fatbox3 ~]# mount /dev/mapper/m3-home /mnt/home
[root@fatbox3 ~]# mount /dev/mapper/m3-var /mnt/var
[root@fatbox3 ~]# cat /mnt/var/vin
cat: /mnt/var/vin: No such file or directory
[root@fatbox3 ~]# cat /mnt/var/etc/vin
[root@fatbox3 ~]# sqlite3 /mnt/home/tesla/.Tesla/data/PhonebookV2.db "select «* f
rom vcards limit 15"
(venv) hnj@piepmatz:~/Projects/psp/tesla/ftpm-of fl
from-image ../boot_nvme.bin $(xxd -p -c32 ../ftpm-sed
(venv) hnj@piepmatz:~/Projects/psp/tesla/ftpm-offli
"BL
"type": "pbkdf2",
“hash": "sha256",
“iterations”: 1000,
}
"tokens": {
“keyslots”: [
ZwfvQdWSLFYR7YkTmer \nefMdy jRaXp96HF
87
```

## Slide 88

# Outline

**1** Analyzing Boot and Firmware Security **2** Hotwiring the Infotainment system **3** ExtracOng Secrets from the Tesla

88

## Slide 89

# Summary

1. We reverse-engineered Tesla’s boot security

   - Tesla sets a good example of how it should be done

2. We sOll rooted the system through voltage glitching

   - This allows to acHvate some so3-locked features without paying

   - Not so3ware-patchable by anyone

3. We extracted hardware-bound secrets from the TPM using the same aYack

   - This can ease independent repairs

89

## Slide 90

# Key Takeaways

1. SoH-locking hardware features increases hacking incenOves

2. Using baYle-tested open-source soHware like Coreboot and Linux provides a good level of soHware security

3. But: Consider _hardware_ aYacks in your threat model, too

90

## Slide 91

# Responsible Disclosure(s)

- 2021: Informed AMD about voltage glitching suscepObility

- 2022: Shared faulTPM aYack with AMD (based on glitching)

- 2023: Informed Tesla about “AMD jailbreak”

   - Tesla was ‘relieved’ that a single glitch did not yield persistence

   - Did not comment the car_creds extracHon

91

## Slide 92

Jailbreaking an Electric Vehicle in 2023 WHAT IT MEANS TO HOTWIRE TESLA'S X86-BASED SEAT HEATER

Chris&an Werling Niclas Kühnapfel Hans Niklas Jacob Oleg Drokin

cwerling@sect.tu-berlin.de kuehnapfel@tu-berlin.de hnj@sect.tu-berlin.de

drokin@linuxhacker.ru

All code available at: **github.com/PSPReverse**
