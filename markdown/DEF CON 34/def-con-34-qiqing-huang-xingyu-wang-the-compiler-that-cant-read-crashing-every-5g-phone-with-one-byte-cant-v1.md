---
title: "The Compiler That Can't Read Crashing Every 5G Phone With One Byte"
speakers: ["Qiqing Huang", "Xingyu Wang"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: null
source_pdf: "DEF CON 34/DEF CON 34 - Qiqing Huang, Xingyu Wang - The Compiler That Can't Read Crashing Every 5G Phone With One Byte - Cant v1.pdf"
pages: 34
sha256: "4e4f6d85e2acc46b9efe3f8aa97cc5b648bd8d0249e5e5fe5729e16c2aea1872"
text_chars: 11704
ocr_pages: 1
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:26:14Z"
---
# The Compiler That Can't Read Crashing Every 5G Phone With One Byte

**Speakers:** Qiqing Huang, Xingyu Wang  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Qiqing Huang, Xingyu Wang - The Compiler That Can't Read Crashing Every 5G Phone With One Byte - Cant v1.pdf` (34 pages)

## Slide 1

### **The Compiler That Can't Read**

Crashing Every 5G Phone With One Byte **Qiqing Huang · Xingyu Wang University at Buffalo Aug 8, 2026**

## Slide 2

###### **Your Phone Has a Second Computer**

Cellular messages reach it before Android or iOS can intervene.

**APPS OS APPLICATION PROCESSOR BASEBAND PROCESSOR MODEM FIRMWARE RRC DECODER …**

**CELLULAR TOWER**

The Compiler That Can't Read  ·  DEF CON 34

## Slide 3

###### **Your Phone Chases the Loudest Tower**

Picks the loudest — no ID check
RECEIVE → PARSE → APPLY → SAFE??
UE
Your phone!

Tower
−95 dBm
ROGUE
−55 dBm · loudest

Tower
−85 dBm

_Your phone connects to whoever's loudest — automatically. It trusts signal strength, not identity._

The Compiler That Can't Read  ·  DEF CON 34

## Slide 4

###### **THE SCHEMA PARSES, THE SPEC DEFINES**

**RRCSetup** _one downlink message_

csi-MeasConfig srs-Config
nzp-CSI-RS-ResourceId startPosition
reportConfigId nrofSymbols
csi-IM-ResourceId srs-ResourceId
pdsch-Config pucch-Config
pdsch-AggregationFactor dl-DataToUL-ACK
rateMatchPattern schedulingRequestId
mcs-Table format1

Before authentication, the baseband receives instructions that shape how the phone communicates.

The Compiler That Can't Read  ·  DEF CON 34

## Slide 5

###### **THE SCHEMA PARSES, THE SPEC DEFINES**

**What if the message parses —but one value is forbidden by the spec?**

The Compiler That Can't Read  ·  DEF CON 34

## Slide 6

**01**

###### **Who We Are**

- We’re Ph.D. researchers at the **University at Buffalo** . We work on 5G and baseband security, especially the gap between what telecom standards require and what real implementations actually enforce.

- Our findings have been coordinated through **GSMA CVDs** and communicated to the **3GPP** standards community.

- Our vulnerability research has led to public CVEs and fixes across **commercial modem** platforms and **open-source** 5G implementations.

The Compiler That Can't Read  ·  DEF CON 34

## Slide 7

###### **Three Players in a 5G Network**

Uu  N2 / N1
 —   —
UE gNB 5G Core
RRC NGAP
Your phone! Base station · NG-RAN AMF / SMF / UPF

_Your phone connects to the base station before the core authenticates the network._

The Compiler That Can't Read  ·  DEF CON 34

## Slide 8

###### **Meet the Baseband**

NAS to the 5G core (AMF)
RRC parsed here
RRC ASN.1 / UPER decoded HERE
— pre-auth, after PDCP decrypts
PDCP ciphering · integrity
Same decoder,
RLC segmentation · ARQ every pre-auth message
SIB1 · RRCSetup · …
MAC scheduling · HARQ
PHY over the air (Uu)

The Compiler That Can't Read  ·  DEF CON 34

## Slide 9

###### **Obey First, Check ID Later**

UE gNB
SIB1    ·    broadcast    ·    no security
RRCSetupRequest    ·    SRB0 / CCCH
RRCSetup    ·    SRB0 / CCCH    ·    no security yet
RRCSetupComplete    ·    SRB1 / DCCH
Authentication  +  SecurityModeCommand
SecurityModeComplete    →    ciphering ON
Cell selection ── SIB1 ── RRCSetup ── Auth ── Security Mode ──…
└────── PRE-AUTH WINDOW ──────┘
                  Attacker message

The Compiler That Can't Read  ·  DEF CON 34

## Slide 10

###### **What Does the Attacker Actually Need?**

###### **Need**

###### **Does Not Need**

- **A selectable rogue cell**

- **SDR + gNB software**

- **A crafted pre-auth RRC message**

- **Within effective radio range**

- **A malicious app**

- **A link or attachment**

- **User interaction**

- **Successful core authentication**

The Compiler That Can't Read  ·  DEF CON 34

## Slide 11

###### **How to Test**

Strongest cell
Rogue gNB
OAI · USRP B210 Your phone
Crafted Message CRASH Reboot Reconnect

_Rogue gNB (OAI on USRP B210) + phone in an RF-shielded box — real over-the-air, in lab._

The Compiler That Can't Read  ·  DEF CON 34

## Slide 12

###### **The ASN.1 Compiler Wrote It**

ASN.1 compiler
TS 38.331
spec → C code
ASN.1 schema

Decoder
Baseband RRC
uper_decode()
acts on the struct

_The generated decoder checks the structure — bits form a valid struct — but not the value range, nor the conditional / cross-field rules that live only in the prose._

The Compiler That Can't Read  ·  DEF CON 34

## Slide 13

Same Inherited Blind Spot
Apple C1 Qualcomm Samsung MediaTek OAI
SAME INHERITED BLIND SPOT
five vendors link a flavor of the same ASN.1-compiler-generated decoder
GSMA agreed   → CVD-2026-0123 →   LS to 3GPP RAN2

###### **Same Inherited Blind Spot**

The Compiler That Can't Read  ·  DEF CON 34

## Slide 14

**The decoder enforces only what made it into the schema.** _Every vendor links a flavor of the same generated code._

**So: what did the schema leave out?**

The Compiler That Can't Read  ·  DEF CON 34

## Slide 15

###### **The Gap**

_An ASN.1 compiler generated the decoder — it skips two kinds of check:_

##### **Can't read English**

##### **Can't count**

**the rule's in the manual,** _not the code_

**the range is narrower** _than the bits allow_

**Valid-looking messages crash your phone — before authentication, no SIM credentials needed**

The Compiler That Can't Read  ·  DEF CON 34

## Slide 16

###### **The Compiler Can't Read Presence**

**THE 3GPP SPEC  ·  prose “Index of first PRB after frequency hopping of PUCCH”**

**→ meaningless without frequency hopping** **_TS 38.331 · secondHopPRB field description_**

**THE ASN.1 SCHEMA intraSlotFrequencyHopping ENUMERATED{enabled} OPTIONAL secondHopPRB PRB-Id OPTIONAL**

**But they are two independent OPTIONALs —** _the schema never links them_

**The rule's in the spec, not the code. so the generated decoder never checks it.** ▸ **CVD-2026-0123**

The Compiler That Can't Read  ·  DEF CON 34

## Slide 17

###### **The Rule Is Just a Comment**

**ServingCellConfigCommon ::= SEQUENCE { ... tdd-UL-DL-ConfigurationCommon TDD-UL-DL-ConfigCommon OPTIONAL,   -- Cond TDD downlinkConfigCommon DownlinkConfigCommon OPTIONAL,   -- Cond HOAndServCellAdd ... }**

**if (presence_bitmap & (1 << N)) { // the guard TS 38.331 requires: if (!is_tdd_cell(cell_config)) // never generated return CONSTRAINT_VIOLATION; // never generated rv = decode_TDD_UL_DL_ConfigCommon( &msg->tdd_UL_DL_ConfigurationCommon, ...); // decoded; passed to upper layer as-is }**

**_The presence rule lives only in that '-- Cond' comment — and ASN.1 compilers discard comments. The 'Cond TDD' guard the spec requires is never generated._**

The Compiler That Can't Read  ·  DEF CON 34

## Slide 18

###### **The Compiler Can't Read Presence**

**_TS 38.211 §6.4.1.4.1 Sounding reference signal (SRS) resource_**

The Compiler That Can't Read  ·  DEF CON 34

## Slide 19

###### **One Rule. Two Fields. No Check.**

**IN THE SCHEMA  (ASN.1) IN THE MANUAL  (prose)** SRS-Resource ::= SEQUENCE { resourceMapping SEQUENCE { **startPosition ≥ startPosition  INTEGER (0..5), nrofSymbols    ENUM {n1, n2, n4} nrofSymbols − 1** } _so the SRS never crosses the slot boundary_ } **TS 38.211 §6.4.1.4.1 — never in the schema** _two independent fields — the schema never links them_

**nrofSymbols: n1 → n4   (change one field)    → modem crash**

The Compiler That Can't Read  ·  DEF CON 34

## Slide 20

###### **Three Invisible Rules**

**1**

**Presence**

**_WHEN a field may even appear_**

**2**

**Cross-f i** **eld** **_fields that secretly depend on each other_**

## **3**

**Extension Groups** **_newer optional chunks — named, out of scope_**

The Compiler That Can't Read  ·  DEF CON 34

## Slide 21

###### **How We Found Them**

TS 38.331
  field descriptions
Cond SUL 286 423+ 1,162
presence dependencies extension markers
  present only if
  SUL is configured
  extensionGroup {
    ... optional ... Each → one valid message that breaks exactly one rule
Too many to read by hand — so we built a system.

The Compiler That Can't Read  ·  DEF CON 34

## Slide 22

###### **A Tool That Reads What the Compiler Can't**

- ① **preprocess spec** _3GPP PDF → text_

② **collect fields** _every IE + field_

③   pair the fields
which fields relate

- ⑥ **send pre-auth** _→ the modem crashes_

⑤   build a test
valid message, broken rule

④   infer the rule
cross-field — not in the schema

###### **Presence, ranges, cross-field — it reads every rule the schema drops, on any field.**

The Compiler That Can't Read  ·  DEF CON 34

## Slide 23

###### **One Malformed IE. One Segfault.**

**gdb — nr-uesoftmodem**

**Thread 20 "UEthread_0" received signal SIGSEGV, Segmentation fault. setup_puschpowercontrol (...) at .../NR_MAC_UE/config_ue.c:963 963   RELEASE_IE_FROMLIST(source->pathlossReferenceRSToReleaseList, ...)**

**RELEASE_IE_FROMLIST has no NULL check — the add path does.** **_Same class, in code you can read: the release path was never taught to check OpenAirInterface 5G UE (open source) — CVE-2025-63356 (fixed)._**

The Compiler That Can't Read  ·  DEF CON 34

## Slide 24

###### **More.**

The Compiler That Can't Read  ·  DEF CON 34

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
More.
Qualcomn
Google
Baseband
Snapdragon X80
Dimensity 9300 / 1200
C1 Modem
Shannon g53000
Acknowledged
Triaged high severity
Reproduced by Apple
Acknowledged
```

## Slide 25

###### **It Can't Count Either**

the schema declares a hard ceiling
nzp-CSI-RS-ResourceId   INTEGER (0 .. 191)
we sent 192
0 legal range 191 192

**8 bits hold 0..255 — the spec defines only 0..191** _the decoder accepts the spec-undefined 192..255 as legal → straight into the array_

The Compiler That Can't Read  ·  DEF CON 34

## Slide 26

###### **Straight Through, Into The Array**

**wire byte decoded number array index out of bounds CRASH** **_array[192] ·  valid indices  0 … 191_ 192 The array was only ever sized for the legal range** **_Just a number too big—or Something Deeper?_** ▸ **CVD-2025-0110**

The Compiler That Can't Read  ·  DEF CON 34

## Slide 27

###### **One Byte: 0xbf**

reportConfigId  INTEGER (0 .. 47)
But UPER can pack it as a 6-bit field
= 0xBF
1 0 1 1 1 1 1 1 (wire
byte)
neighbour reportConfigId = 63   (spec max 47)

- **6 bits hold 0..63 — but the spec allows only 0..47.** **_the decoder never checks → 48–63 slip straight through_**

**The Compiler That Can't Read  ·  DEF CON 34**

## Slide 28

#### **Watch It Die By Itself Watch It Die By Itself**

RUN 1
normal setup message
Phone is happy   ✓

RUN 2
one byte changed
gone   ✗

RUN 3
left it running
crash · reboot · crash  ↻

**_a hands-off, permanent denial of service — nobody is touching anything_**

The Compiler That Can't Read  ·  DEF CON 34

## Slide 29

###### **Not Two Bugs, One Hole**

**can't read English** _presence · cross-field · extension_ **can't count ONE HOLE** _range rule in prose, not the schema_ **_Every vendor inherits it_**

The Compiler That Can't Read  ·  DEF CON 34

## Slide 30

###### **Real-World Impact**

**PUBLIC  CVE**

**CVE-2025-20644 · CVE-2025-20703 · CVE-2025-20666 CVE-2026-20503 · CVE-2026-20504 CVE-2025-47384 CVE-2025-63356**

GSMA mobile security research acknowledgements **(CVD)**

**UNDER DISCLOSURE** _named only_

**Apple C1**

**Google Pixel Samsung Shannon**

**CVD-2025-0110 · CVD-2026-0123**

The Compiler That Can't Read  ·  DEF CON 34

## Slide 31

###### **The Bug Finder Is the Fix**

**spec.word schema.asn asn1c decoder baseband**

**long-term: Validation shim 3GPP puts the constraints back re-enforce the dropped rules between decoder & baseband in the schema**

The Compiler That Can't Read  ·  DEF CON 34

## Slide 32

###### **This Is a Class, Not a Quirk.**

**5G** _shown today_ **·    LTE    ·    automotive    ·    aviation**

**…the field shall only be present when… — public spec text**

**The attack surface is public — the only question is who reads it first.**

The Compiler That Can't Read  ·  DEF CON 34

## Slide 33

###### **More To Come**

_The full method + CVEs behind today →_ our **USENIX Security '26 talk** https://www.usenix.org/conference/usenixsecurity26/presentation/huang-qiqing

**Base-Station Security Testing**

--- _the network side of the air interface_

**eSIM Security Testing** --- _the SIM, reimagined in software_

And a Google-confirmed **Critical-severity finding** .

The Compiler That Can't Read  ·  DEF CON 34

## Slide 34

# **~~<u>Questions? Questions?</u>~~**

**Qiqing Huang linkedin.com/in/qiqing-huang Xingyu Wang linkedin.com/in/xingyu-wxy**

The Compiler That Can't Read  ·  DEF CON 34
