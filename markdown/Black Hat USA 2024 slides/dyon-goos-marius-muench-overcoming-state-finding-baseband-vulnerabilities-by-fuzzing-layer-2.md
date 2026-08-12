---
title: "Overcoming State Finding Baseband Vulnerabilities by Fuzzing Layer-2"
speakers: ["Dyon Goos", "Marius Muench"]
conference: "Black Hat"
conference_full: "Black Hat USA 2024"
edition: "USA"
year: 2024
source_pdf: "Black Hat USA 2024 slides/Dyon Goos & Marius Muench_Overcoming State Finding Baseband Vulnerabilities by Fuzzing Layer-2.pdf"
pages: 40
sha256: "0a67d8ee2facf72413ecb3cc9ab996fa5bebdcb59e414707d53fddc881395544"
text_chars: 21337
ocr_pages: 7
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:30:00Z"
---
# Overcoming State Finding Baseband Vulnerabilities by Fuzzing Layer-2

**Speakers:** Dyon Goos, Marius Muench  
**Conference:** Black Hat USA 2024  
**Source:** `Black Hat USA 2024 slides/Dyon Goos & Marius Muench_Overcoming State Finding Baseband Vulnerabilities by Fuzzing Layer-2.pdf` (40 pages)


## Slide 1

# Overcoming State: Finding Baseband Vulnerabilities by Fuzzing Layer-2

Speakers: Dyon Goos & Marius Muench

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
on
blackhat +
USA 2024
AUGUST 7-8, 2024
BRIEFINGS
Overcoming State: Finding Baseband
Vulnerabilities by Fuzzing Layer-2
Speakers: Dyon Goos & Marius Muench
```

## Slide 2

## About Us

### Dyon:

### Marius:

- Independent security researcher

- MSc (Vrije Universiteit Amsterdam)

- Spent the last 2 years in baseband stacks :)

- Assistant Professor (University of Birmingham), UK

- Baseband research since 2018

- Co-creator of FirmWire

- Captures flags with Tasteless

#BHUSA  @BlackHatEvents

## Slide 3

## This talk

Layer-3
Layer-2
Layer-1

Layer-3
Layer-2
Layer-1

#BHUSA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
black hat
USA 2024
This talk
—,
1oo1GIo
BIolola |
IGOo01IGI
= A
S )
Q P= re) x
ol\ie — CINE
d Layer-3 » Layer-3
} Layer-2
} Layer-2
(« a Ww Layer-1 © w Layer-1
```

## Slide 4

## Basebands

#BHUSA  @BlackHatEvents

## Slide 5

￼ AP CP

## Basebands

- Modern phones are a collection of processors

11:25                    GSM

   - Including: Application Processor (AP) & Cellular Processor (CP)

- CP also referred to as “Baseband”

   - Implements most layers of cellular communication stack

- Lucrative attack surface

   - Myriad of parsers, legacy code, obscure features

#BHUSA  @BlackHatEvents

## Slide 6

## The code running on basebands Custom Real-Time Operating Systems (RTOS), providing:

- Core OS functionality:

   - Scheduler, timers, interrupts

   - Messaging

- Cellular stack implementation:

   - Stack is split into “tasks”

   - Tasks communicate via message queues

#BHUSA  @BlackHatEvents

## Slide 7

Baseband Security Research Plenty of attention in recent years, e.g.:

#BHUSA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat
USA 2024
Baseband Security Research
Plenty of attention in recent years, e.g.:
bisekhat 4 oo EGHOUL
a How to Hack Shannon Baseband
(from a Phone)
Basebanheimer
Now | Am Become Death, The Destroyer of Chains Over the Air, Under the Radar
i . Attacking and Securing the Pixel Modem 5Ghoul : Unleashing Chaos on 5G Edge Devices
TASZK hardwear.io . 5
Al § q fal ‘ Matheus E. Garbelini'; Zewen Shang’; Shijie Luo’; Sudipta Chattopadhyay’; Sumei Sun Ernest Kurniawan?
Xuan Xing Eugene Ri Farzan Karimi
White Paper | Atackoveriew @ | Targets 4, | impact JW | desciptins @ | sctooingeroc = |
Singapore University of Technology and Design;
2/2R, A*STAR
Cracking the 5G Fortress: Peering Into 5G's
Vulnerability Abyss
q Kai Tu | Research Assistant, The Pennsylvania State University
@) al S MS t Yilu Dong | Research Assistant, The Pennsylvania State University
bdullah Al Ishtiaq | Research Assistant, The Pennsylvania State
Root Them All Univers
There will be Bugs: Exploitin:
Basebands in Radio Layer wo
Daniel Komaromy Analyzing Cellular Base’
Baseband exploitation in public originally focused on message decoding bugs in layer 3 (NAS and RRC) and
more recently in layer 4 (traffic over IP). in this presentation we uncover a new area of exploration for remote
Md Mukit Rashid | Research Assistant, The Pennsylvania State
University
baseband exploitation in layer 2. In the past, this part of cellular specifications has been overlooked due to its
function and packet size limitations. However, a deeper dive uncovers possibilities that show up in both old
and new standards. Importantly, this is a layer that is below the ciphering applied to cellular communications | Graduate Researcher, The Pennsylvania State
providing an attack surface reachable not only with fake base stations but with direct MITM-ing of legitimate
cell tower communications too. The presentation will describe the chain of vulnerabilities we have found and CCCamp ‘23 iR heagaistark THe'P: site .
1 esearch Assistant, The Pennsylvania State University
explain how to exploit them for remote code execution in the baseband of flagship Samsung smartphones 2023-08-17 nisr & domenukk
in | Assistant Professor, The Pennsylvania State
The new class of bugs meant new challenges both in developing and delivering an exploit. | will describe how
we have modified radio software to inject a more complex sequence of malicious layer two traffic without the University
```

## Slide 8

What about Layer-2? When we started, most research/findings focus on cellular L3 (or higher)

Let’s have a look at layer-2 ourselves!

- ⇒ Let’s start with the lowest hanging fruits:

   - GSM Layer-2

   - Fuzzing

#BHUSA  @BlackHatEvents

## Slide 9

CCLayer-2 SMS

SS

## GSM Protocol Stack

  CC
  CM   SMS
  SS
Layer-3    MM
  RR
    LAPDm
Layer-2
  Phy
Layer-1

**RR** : Radio Resource **MM** : Mobility Management **CM** : Connection Management **CC** : Call Control **SMS** : Short Messaging Service **SS** : Supplementary Services

**LAPDm** : Link Access Protocol on the Dm Channel (LAPDm) **Phy** : Physical

#BHUSA  @BlackHatEvents

## Slide 10

## GSM Layer 2

- Link Access Protocol on the Dm Channel (LAPDm).

- Frame Concatenation

- PD: _information[0] & 0xF._

struct LAPDM_frame{ uint8_t addr; uint8_t ctrl; uint8_t len; uint8_t information[N]; } PACKED;

CC Task SS Task SMS Task
PD = 0xB
MM Task
PD = 0x3 PD = 0x9
PD != 0x6
RR Task
L3 RR Frame
LAPDm #1 LAPDm #N

#BHUSA  @BlackHatEvents

## Slide 11

## Our approach to fuzzing

#BHUSA  @BlackHatEvents

## Slide 12

## Our Fuzzing Campaigns: FirmWire

- Full-system baseband emulator

   - Baseband emulation from boot

   - Fuzzing support via AFL++

   - Support for MTK & Exynos firmware

- Advantages:

   - Analyzable logs

   - Coverage tracking

   - Task-interaction

#BHUSA  @BlackHatEvents

## Slide 13

## Fuzzing in FirmWire

- Requires injection of “Fuzzing Task”

#include <shannon.h> #include <afl.h>

- Written in C, AFL wrapper present

- Appears like an ordinary task for emulated CP

- Sends messages to other tasks

const char TASK_NAME[] = "AFL_DEMO\0"; static uint32_t qid;

int fuzz_single_setup() { qid = queuename2id("TARGET_TASK_QUEUE"); struct qitem_target * init =

pal_MemAlloc(4, sizeof(struct qitem_target), __FILE__, __LINE__); // setup init payload [...] pal_MsgSendTo(qid, init, 2); return 1; }

#BHUSA  @BlackHatEvents

## Slide 14

## The Plan: Fuzzing Layer-2

### Existing Fuzzers (non-OTA)

### Our Approach (GSM)

fuzz
ASN.1_d fuzz
ASN.1_ CC
ecode CC
decode CC
fuzz
LAPDm RR MM SS
LAPDm
CC
SMS
fuzz
MM SS
MM
SMS
#BHUSA  @BlackHatEvents

#BHUSA  @BlackHatEvents

## Slide 15

## The Target: Galaxy S10e Firmware

- Latest phone model supported by FirmWire

- Released date: 2019

- Firmware date: March 2023

   - Original FirmWire bugs are patched

#BHUSA  @BlackHatEvents

## Slide 16

## Challenges

#BHUSA  @BlackHatEvents

## Slide 17

## The Challenges

Need to create fuzzing tasks

How to deal with complex baseband state No support for recent phones

#BHUSA  @BlackHatEvents

## Slide 18

## Challenge 1: Creating fuzzing tasks Sending initialization messages

**/Initialize RR task CC Task SS Task SMS Task struct qitem_rr * init = //Initialize MM task pal_MemAlloc(4, sizeof(struct qitem_rr) + struct//Initialize CC task qitem_mm * init_mm = sizeof(struct qitem_grr_init_req),__FILE__, __LINE__); structpal_MemAlloc qitem_cc * nit_cc =(4, sizeof(struct qitem_mm) + //Initialize SS task MM Task init->header.op = 0; sizeofpal_MemAlloc((struct qitem_mm_init_req), __FILE__, __LINE__);4, sizeof(struct qitem_cc), struct qitem_ss * init_ss = pal_MemAlloc(4, sizeof(struct init->header.op2** //Initialize SMS task **= 0x3c; init_mm__FILE__->header.op , __LINE__= 0; ); qitem_ss) + sizeof(struct qitem_ss_init_req), init->header.size** struct qitem_sms * init_sms = **= sizeof(struct qitem_grr_init_req); init_mminit_cc->header.op = ->header.op2 = 0x200; ; __FILE__, __LINE__); RR Task init->header.msgGroup** pal_MemAlloc( **= 0x327f** 4, sizeof **;** (struct qitem_sms), **init_mminit_cc->header.size = ->header.size = sizeof1; (struct qitem_mm_init_req); memset(init->payload** __FILE__ **,** , **0, init** __LINE__ **->header.size);** ); **init_mminit_cc->header.msgGroup = ->header.msgGroup = 0x29a30x2a01; ; init_ss->header.op = 0; pal_MsgSendTo(queuename2id("GRR"), init, 2); memsetpal_MsgSendTo(queuename2id((init_mm->payload, 0, init_mm"CC"), init_cc, ->header.size);2); L3 RR Frame init_ss->header.op2 = 0x27;** init_sms->header.op = 0; **pal_MsgSendTo(queuename2id("MM"), init_mm, 2); init_ss->header.size = sizeof(struct qitem_** grr_init_req);ss_init_req); init_sms->header.op2 = 0x8a; **init_ss->header.msgGroup = 0x2200;** init_sms->header.size = sizeof(struct qitem_sms_init_req); **LAPDm #1 LAPDm #N** init_sms->header.msgGroup = 0x2d07; pal_MsgSendTo(queuename2id("SMS"), init_sms, 2);

#BHUSA  @BlackHatEvents

## Slide 19

### - All tasks are initialized, we should now be able to start fuzzing ….

Let’s go fuzzing

#BHUSA  @BlackHatEvents

## Slide 20

####

### …. but we initialized all tasks?

[GLAPD] 0x4195a44b 0b101: [../../../HEDGE/GSM/GL2/GLAPD/Code/Src/dl_uti.c] - Add concat buf : 4463223c [GLAPD] 0x41a35bf5 0b101: [.[GRR] 0x40f0f8d7 0b10: [../ **.** /../ **.** /../HEDGE/GSM/GL2/GLAPD/Code./HEDGE/GSM/GL3/GRR/Code/Src **/** Sr **r** c/dl_os.c] - Lib Mem buf_dedi.c] - Receive Data rom Network (BTS) **f** er 446225a0 [GLAPD] 0x41a35bf5 0b101: [.[GRR] 0x40f0f907 0b10: [../ **.** /../ **.** /../HEDGE/GSM/GL2/GLAPD/Code./HEDGE/GSM/GL3/GRR/Code/Src **/** Sr **r** c/dl_os.c] - Lib Mem buff_dedi.c] - (CIQ)## - In S **e** r 44632f20mRecBtsData, TID : 0x0, [GLAPD] 0x41a35bf5 PD : 3, MSG_Type :[MM] 0x40f439af 0b10: [../../../HEDGE/NASL3/MM/Code/Src/mm_Main.c] - STACK ID - 0 **0** b101: [../../../HEDGE/GSM/GL2/GLAPD/Code/Src/dl_os.c] - Lib Mem buffer 446310a0x5 ,CHANNEL : 1, Message : 1147347516 [GLAPD] 0x4195a531 0b101: [.[GRR[MM 0x40f43561 0b10: [../../../HEDGE/NASL3/MM/Code/Src/mm_Main.c] - MM Message Count -> 5 **]** 0x40f0f9a1 0b10: [../ **.** /../ **.** /../HEDGE/GSM/GL2/GLAPD/Code./HEDGE/GSM/GL3/GRR/Code/Src **/** Sr **r** c/dl_uti.c] - Add la_dedi.c] - Route mes **s** t byage o **t** e of concat buf : 44632297MM/ CC **[GLAPD] pal_MsgSendTo+0x3ff (0x4100460f) pal_MsgSendTo(GRR (60)) - PALMsg<0x3203, GLAPD (32) -> GRR (3c), 84 bytes>** [GRR[MM 0x40f5546d 0b10: [../../../HEDGE/NASL3/MM/Code/Src/mm_CellInd **]** 0x4069c6ef 0b10: [../../../HEDGE/GSM/GL3/GRR/Code/Src/rr_ **i** cation.c] -  Resetting Sent Reg Statusnit.c] - MSG: GRR_MM_DATA_IND **[GRR] pal_MsgSendTo+0x3ff (0x4100460f) pal_MsgSendTo(MM (32)) - PALMsg<0x2922, GRR (3c) -> MM (20), 84 bytes>** [MM] 0x41359a0f 0b1: [../../../HEDGE/NASL3/MM/Code/Src/mm_Utilities.c] - TRAP MESSAGE !!! - Invalid Request for this State in mm_DecodeRrDataIndMsg !!!

CC
fuzz LAPDm RR MM SS
SMS

#BHUSA  @BlackHatEvents

## Slide 21

## Challenge 2 : Initialize the state

(1) Identifying crucial state beyond task initialization

**returns *(uint8_t*) 0x42e22f58**

[1.67198][MM] 0x41359a0f 0b1: [../../../HEDGE/NASL3/MM/Code/Src/mm_Utilities.c] - TRAP MESSAGE !!! - Invalid Request for this State in mm_DecodeRrDataIndMsg !!!

#BHUSA  @BlackHatEvents

## Slide 22

## Challenge 2: Initialize the state

(2a) Fix up the state variables

- We need to fake a valid connection state

- Simple state constants, as well as ..

#ifdef SAMSUNG_S10e .... uint32_t rr_state_addr = 0x4182cdcc; uint32_t rr_cur_dlci_addr = 0x4182cfe0; uint32_t glapd_state_addr = 0x42c5cacc; uint32_t mm_state_addr = 0x42e22f58; .... #endif

.... // make sure the baseband is in RR state 8 *(uint16_t*)rr_state_addr = 0x8; //make sure the lapdm state is 2 *(uint8_t*)glapd_state_addr=0x2; *(uint8_t*)(glapd_state_addr+0x2) = 0x1; //make sure the mm state is 9 *(uint8_t*)mm_state_addr = 0x9; //set the DLCI *(uint8_t*)rr_cur_dlci_addr = 0x4; ....

#BHUSA  @BlackHatEvents

## Slide 23

## Challenge 2: Initialize the state

(2b) .. more advanced state Wait, unknown?

Only restore crucial state

#ifdef SAMSUNG_S10e .... uint32_t rr_serv_cell_addr = 0x4182cdd8 ; .... #endif struct rr_servingCell{ uint16_t arfcn; uint16_t rxLvl; uint8_t[0x17] unk; uint8_t[0x3] mnc_mmc; uint16_t lac; uint8_t[0xd0] unk2; } PACKED;

.... struct rr_servingCell *rr_servCell; rr_servCell = alloc(0xec); memset(rr_servCell, 0x0, 0xec); rr_servCell->arfcn = 0x35d; rr_servCell->mnc_mmc = 0x1869f; rr_servCell->lac = 0x3e8; *rr_serv_cell_addr = rr_servCell; ....

#BHUSA  @BlackHatEvents

## Slide 24

- [GLAPD] 0x4195a44b 0b101: [../../../HEDGE/GSM/GL2/GLAPD/Code/Src/dl_uti.c] - Add concat buf : 4463223c [GLAPD] 0x41a35bf5 0b101: [.[GRR] 0x40f0f8d7 0b10: [../ **.** /../ **.** /../HEDGE/GSM/GL2/GLAPD/Code./HEDGE/GSM/GL3/GRR/Code/Src **/** Sr **r** c/dl_os.c] - Lib Mem buf_dedi.c] - Receive Data rom Network (BTS) **f** er 446225a0 [GLAPD] 0x41a35bf5 0b101: [.[GRR] 0x40f0f907 0b10: [../ **.** /../ **.** /../HEDGE/GSM/GL2/GLAPD/Code./HEDGE/GSM/GL3/GRR/Code/Src **/** Sr **r** c/dl_os.c] - Lib Mem buff_dedi.c] - (CIQ)## - In S **e** r 44632f20mRecBtsData, TID : 0x0, [MM] 0x40f439af 0b10: [../../../HEDGE/NASL3/MM/Code/Src/mm_Main.c] - STACK ID - 0

- [GLAPD] 0x41a35bf5 PD : 3, MSG_Type : **0** b101: [../../../HEDGE/GSM/GL2/GLAPD/Code/Src/dl_os.c] - Lib Mem buffer 446310a0x5 ,CHANNEL : 1, Message : 1147347516 [MM] 0x40f43561 0b10: [../../../HEDGE/NASL3/MM/Code/Src/mm_Main.c] - MM Message Count -> 5

- [GLAPD] 0x4195a531 0b101: [.[GRR] 0x40f0f9a1 0b10: [../ **.** /../ **.** /../HEDGE/GSM/GL2/GLAPD/Code./HEDGE/GSM/GL3/GRR/Code/Src **/** Sr **r** c/dl_uti.c] - Add la_dedi.c] - Route mes **s** t byage o **t** e of concat buf : 44632297MM/ CC [MM] 0x40f5546d 0b10: [../../../HEDGE/NASL3/MM/Code/Src/mm_CellIndication.c] -  Resetting Sent Reg Status

- **[GLAPD] pal_MsgSendTo+0x3ff (0x4100460f) pal_MsgSendTo(GRR (60)) - PALMsg<0x3203, GLAPD (32) -> GRR (3c), 84 bytes>** [GRR] 0x4069c6ef 0b10: [../../../HEDGE/GSM/GL3/GRR/Code/Src/rr_init.c] - MSG: GRR_MM_DATA_IND [MM] 0x40f4706d 0b101: [../../../HEDGE/NASL3/MM/Code/Src/mm_Main.c] - Protocol Discriminator -> **[CC] 0x40fe8cfd 0b101: [../../../HEDGE/NASL3/CC/Code/Src/cc_Main.c] - ------------------------- CC TASK**

- **[GRR] pal_MsgSendTo+0x3ff (0x4100460f) pal_MsgSendTo(MM (32)) - PALMsg<0x2922, GRR (3c) -> MM (20), 84 bytes>----------------------------** CC_AND_CALL_RELATED_SS_PD **[MM] 0x4135b371 pal_MsgSendTo(CC (23)) - PALMsg<0x2a3c, MM (20) -> CC (17), 84 bytes>** [CC] 0x40fe87e3 0b10: [../../../HEDGE/NASL3/CC/Code/Src/cc_Main.c] - cc_UpdStackId :CcCurrentStackId: 0

   - [CC] 0x40ac21b1 0b101: [../../../HEDGE/NASL3/CC/Code/Src/cc_MsgDescription.c] - cc_MapSubTypeToMessageNum SubType = 0x5

CC
fuzz LAPDm RR MM SS
SMS

#BHUSA  @BlackHatEvents

## Slide 25

- All tasks (and State) are initialized, we should now be able to start fuzzing ….

Let’s go fuzzing pt 2

#BHUSA  @BlackHatEvents

## Slide 26

#BHUSA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
gQ : hd
black hat ,
USA 2024 ,
american fuzzy lop ++4.22a (./firmwire.py) [explore]
@ days, 1 hrs, 27 min, 54 sec
© days, © hrs, O min, © sec
© days, © hrs, 2 min, 18 sec
none seen yet
1465.0 (74.7%) map density : 1.63% / 27.95%
0 (0.00%) ( it coverage : 1.66 bits/tuple
havoc favored items : 981 (50.00%)
2275/7680 (29.62%) 1€ yn : 1284 (65.44%)
222k total :
© (0 saved)
20/7640, 7/7623, 11/7589
1/955, 3/938, 6/904
48/66.5k, 2/128k, 0/122k
5/8480, 26/35.3k, 25/50.3k
0/0, 0/0, 0/0, 0/0
1009/122k, 644/69.7k
unused, unused, unused, unused
: 0.37%/4588, 97.17%
expLore tat in progress
```

## Slide 27

[7.17742][REG_SAP] 0x41122839 0b100: [../../../PSS/StackService/CNS/Common/Code/Src/ns_Main.c] - Stack Id: 0

[7.17782][REG_SAP] 0x41122853 0b100: [../../../PSS/StackService/CNS/Common/Code/Src/ns_Main.c] - Creating Inst: NS_INFORMATION_IND

[7.17820][REG_SAP] 0x4112233b 0b101: [../../../PSS/StackService/CNS/Common/Code/Src/ns_OsInterface.c] - Allocating memory size(107) from e/Src/ns_OsInterface.c (#163)

[7.17863][REG_SAP] 0x411224a3 0b101: [../../../PSS/StackService/CNS/Common/Code/Src/ns_OsInterface.c] - Memory allocated for message 0x760D, length 107

[7.18030][REG_SAP] 0x4112233b 0b101: [../../../PSS/StackService/CNS/Common/Code/Src/ns_OsInterface.c] - Allocating memory size(40) from e/Src/ns_ServiceHandlerEmm.c (#2503)

[7.18108][REG_SAP] 0x4079a4a5 0b101: [../../../PSS/StackService/CNS/Common/Code/Src/ns_MsgInstance.c] - ns_GetMsgInstance [MsgName : NS_INFORMATION_IND]

[7.18149][REG_SAP] 0x407d9e3d 0b101: [../../../PSS/StackService/CNS/Common/Code/Src/ns_MsgHandler.c] - Message out: BaseType 0, MsgCat 2, rtsInd 0

- [7.18197][REG_SAP] 0x4112233b 0b101: [../../../PSS/StackService/CNS/Common/Code/Src/ns_OsInterface.c] - Allocating memory size(107) from e/Src/ns_MsgHandler.c (#336)

[7.18285][REG_SAP] 0x407d9a1f 0b11: [../../../PSS/StackService/CNS/Common/Code/Src/ns_MsgHandler.c] - REG_SAP ==> NS_INFORMATION_IND (Mbx 159)

- [7.18330][REG_SAP] pal_MsgSendTo+0x3ff (0x4100460f) pal_MsgSendTo(MTI (159)) - PALMsg<0x760d, REG_SAP (a5) -> MTI (9f), 99 bytes>

- [7.18368][REG_SAP] 0x407d9a1f 0b11: [../../../PSS/StackService/CNS/Common/Code/Src/ns_MsgHandler.c] - REG_SAP ==> NS_INFORMATION_IND (Mbx 5)

- [7.18412][REG_SAP] pal_MsgSendTo+0x3ff (0x4100460f) pal_MsgSendTo(ATI (5)) - PALMsg<0x760d, REG_SAP (a5) -> ATI (5), 99 bytes>

**[ERROR] firmwire.vendor.shannon.hooks: FATAL ERROR (REG_SAP): from 0x40effd05 [pal_PlatformMisc.c:146 - Fatal error: PAL_MEM_GUARD_CORRUPTION pal_MemInterface.c Line 895]**

#BHUSA  @BlackHatEvents

## Slide 28

- Challenge 3: No support for recent phones - Our fuzzing targeted a firmware from early 2023

- Confirm vulnerabilities OTA against newer devices

- Collect a bunch of crashing payloads

- Patch open source tooling to allow for automated testing.

For every
crash file
do ..

#BHUSA  @BlackHatEvents

## Slide 29

## OTA Setup

- Hardware

SDR (BladeRF 2.0 micro xA4) USB hub + cables Raspberry Pi 4 Faraday Cage

- Software

Open source GSM Base Station software : Yate v6.2.1 / YateBTS v6.1.1

- Tested Phone:

   - Google Pixel 6 and 8

   - Samsung Galaxy S10e, S22, A14

#BHUSA  @BlackHatEvents

## Slide 30

02-24 07:11:12.305 1098 1161 D RFSD    : [ModemStateMonitor::OnModemCrashOrReset] Modem  is STATE_CRASH_EXIT or STATE_CRASH_RESET 02-24 07:11:14.286 1088 1219 D DMD     : ModemStateMonitor : Modem  CRASH!!![2] 02-24 07:11:14.286 1088 1219 D DMD     : ModemStateMonitor : Check the state again after 2 seconds later.

02-24 07:11:14.305 1098 1161 D RFSD    : [ModemStateMonitor::OnModemCrashOrReset] Modem  is STATE_CRASH_EXIT or STATE_CRASH_RESET

02-24 07:11:16.286 1088 1219 D DMD     : ModemStateMonitor : Modem  CRASH!!![2] 02-24 07:11:16.287 1088 1219 D DMD     : ModemStateMonitor : Check the state again after 2 seconds later.

02-24 07:11:16.306 1098 1161 D RFSD    : [ModemStateMonitor::OnModemCrashOrReset] Modem  is STATE_CRASH_EXIT or STATE_CRASH_RESET

02-24 07:11:18.287 1088 1219 D DMD     : ModemStateMonitor : Modem  CRASH!!![2] 02-24 07:11:18.287 1088 1219 D DMD     : ModemStateMonitor : Check the state again after 2 seconds later.

#BHUSA  @BlackHatEvents

## Slide 31

## Found Vulnerabilities

#BHUSA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
Found Vulnerabilities
all Ke
J =
py a
```

## Slide 32

## Showcase

||**ID**|**Tested Phones**|**Affected**
**Protocol**|**What?**|**Severity**|**Reported in**|
|---|---|---|---|---|---|---|
||CVE-2023-50807|Pixel 6, S22|MM|Heap-based buffer overflow|8.1|Oct-23|
||CVE-2023-50805|Pixel 6, 8, S22|RR|Heap-based buffer overflow|8.1|Oct-23|
|Previously
Unknown|CVE-2024-28068|S22, A14|SS/GPRS|Null-Pointer Deref|5.3|Jan-24|
|Duplicates
|N/A - internal find|Pixel 6, S22, A14|CC/SS|Heap-based buffer overflow|N/A|Jan-24|
|(unpatched at time of
testing)|N/A - internal find|A14|SMS|Stack-based buffer overflow|N/A|Jan-24|
|Under Disclosure|CVE-XXXX-YYYYY
CVE-XXXX-YYYYY
CVE-XXXX-YYYYY|-|-|-|-|-|

#BHUSA  @BlackHatEvents

## Slide 33

## Example bug : CVE-2023-50807 (MM)

### - MM Information message

- Holds information about the network

05 32 45 8c 03 03 03 … 48 41 41 00 01 04 00 …

|**IE**|**Presence**|**Value**|
|---|---|---|
|MM PD|M|0x05|
|MsgType|M|0x32|
|Full Network Name|O|0x43|
|Short Network Name|O|0x45|
|Local Time Zone|O|0x46|
|Universal time|O|0x47|
|LSA Identity|O|0x48|
|Network Daylight Saving
Time|O|0x49|

#BHUSA  @BlackHatEvents

## Slide 34

## Example Bug: CVE-2023-50807 (MM)

05 32 45 8c 03 03 03 … 48 41 41 00 01 04 00 …

- LSA Identity IE

- - LSA Identity IE length

void mm_getIe(uint8_t *src, int p2){ **uVar1** = mm_getIeLength(p2); if((p2 == 0x3c) && (3 < uVar1)) uVar1 = 3; memcpy( **src** , IE_buf, uVar1); } void ns_ServiceHandlerEmm(..){ uint8_t* buf = mem_Alloc(0x6f); memcpy(buf+0x58, **src** , **IE_len** ); }

- LSA Identity IE length should be fixed to 3 bytes - Value from the first check is not propagated

#BHUSA  @BlackHatEvents

## Slide 35

## Demo : Triggering the vulnerability

#BHUSA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
Network & internet
imernet
Netenuthe raewde
Calis & SMS
“ABD } (Termpness'ty cnwvadtaie!
Private DNS:
Aatorsate
Hotspot § tethering
oF
Dato Saver
on
VPN
Private ONS.
Aeon:
```

## Slide 36

## Defenses

- Recent shift in vendor’s approaches: - More hardening for basebands (good)!

- Recently introduced defenses:

- Heap Sanitization (Pixel 8)

- More consistent use of XN

- Allow 2G

#BHUSA  @BlackHatEvents

## Slide 37

## Wrapping Up

#BHUSA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
Wrapping Up
all Ke
J =
py a
```

## Slide 38

## Limitations/Future Work

- State needs to be reversed for every image

   - Potential for automation

- What if we cannot replicate a vulnerability OTA? - FirmWire support for firmware targeting recent firmware

- What about 3G/4G/5G?

   - More reversing, more harnessing, more state, more everything

#BHUSA  @BlackHatEvents

## Slide 39

## Key Takeaways

- State is key to overcome fuzzing roadblocks when fuzzing across communication stacks

- Fuzzing older firmware images can lead to discovering vulnerabilities in the newest devices

- Despite years of research, critical vulnerabilities still hide in 2G implementations.

#BHUSA  @BlackHatEvents

## Slide 40

## Questions

#BHUSA  @BlackHatEvents
