---
title: "Unveiling the Mysteries of Qualcomm's QDSP6 JTAG A Journey into Advanced Theoretical Reverse Engineering"
speakers: ["Alisa Esage"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2025"
edition: "ASIA"
year: 2025
source_pdf: "Black Hat Asia 2025 Slides/Alisa Esage_Unveiling the Mysteries of Qualcomm's QDSP6 JTAG A Journey into Advanced Theoretical Reverse Engineering.pdf"
pages: 32
sha256: "c0e7f526c902a488642585ad6df5d5acf0c1d07c32d89f4ec8226f4670670522"
text_chars: 23397
ocr_pages: 16
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:03:17Z"
---
# Unveiling the Mysteries of Qualcomm's QDSP6 JTAG A Journey into Advanced Theoretical Reverse Engineering

**Speakers:** Alisa Esage  
**Conference:** Black Hat ASIA 2025  
**Source:** `Black Hat Asia 2025 Slides/Alisa Esage_Unveiling the Mysteries of Qualcomm's QDSP6 JTAG A Journey into Advanced Theoretical Reverse Engineering.pdf` (32 pages)


## Slide 1

Unveiling the Mysteries of Hexagon QDSP6 JTAG

A Journey into Advanced Theoretical Reverse Engineering

Alisa Esage Zero Day Engineering Research & Training Black Hat Asia 2025, Singapore

## Slide 2

## About me

### **Alisa Esage Shevchenko**

- Independent Hacker

- Founder of Zero Day Engineering

- Researcher of God Mode<sup>*</sup> since 1999

* gaming term

## Slide 3

## About this talk

### **What is Hexagon?**

- Qualcomm Snapdragon & MDM chips

   - ~30% of smartphone market

### **What is the problem with Hexagon?**

      - You can’t debug it

   - Now entering **laptop market**

   - One or more specialized cores on the Snapdragon SoC are Hexagon cores

- Hexagon architecture

   - Proprietary by Qualcomm, secure

   - ○ Mostly fw code behind Secure Boot

   - ○ VLIW optimized for parallel execution, solid benchmarks

   - Started as DSP for specialized media workloads

   - Runs modem on Android MSM, aka baseband. Variety of attack vectors

   - Now, **NPU**

## Slide 4

Intro

## Slide 5

Recap: Hexagon architecture

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Recap: Hexagon
architecture
Hexagon: programmer's view
Memory
(unified address space)
Load/
vg P4832 bit Store
— Instructions
XTVPE instructions
‘ALUS2 Instructions
J Instructions
CR Instructions
Sequencer
Packets of
1-4 instructions
$2: X Unit
XTYPE instructions
‘ALUS2 Instructions
J Instructions
JR Instructions
eS
Control Registers
Hardware Loop Regs
Modifier Registers
Status Register
Program Counter
Prodicate Registers
User General Poin
Global Pointer
Circular Start Registers,
$1: Load/Store
Unit
LD Instructions
ST Instructions
‘ALUS2 Instructions
$0: Load/Store
Unit
LD Instructions
ST Instructions
‘ALU32 Instructions
MEMOP Instructions
NV Instructions
SYSTEM Instructions
‘igure 1-1__Hexagon V62 processor architecture
1.3.6 Instruction packets
Sequences of instructions can be explicitly grouped into p: for parallel execution.
For example:
{
R8 = memh (R3++#2)
R12 = memw(R1++#4)
R7 = add(R9,#2)
a 1.3.7 Dot-new instructions
eneral
In many cases, a predicate or general register can be both generated and used in the same
instruction packet. This feature is expressed in assembly language by appending the suffix
“new” to the specified register. For example:
2, #4)
R3 =
RS =
PO = cmp.eq(
new) memw (R4)
#5
R2 =
memw (R5)
developer.qualcomm.com/download/hexagon/hexagon-v62-programmers-reference-manual.pdf
[HEXAGONISA] https:
```

## Slide 6

## Hexagon and Snapdragon

<u>https://d eveloper. qualcom m.com/d ownload/ sd820e/q ualcomm</u> -snapdra <u>gon-820e</u> -processo <u>r-apq809 6sge-devi ce-specifi cation.pd f</u>

## Slide 7

Hexagon™ now

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Hexagon™ now
Introducing Snapdragon’ X Elite, the most powerful, intelligent,
and efficient processor in its class for Windows.
With a powerful Al engine, including the world’s fastest NPU for laptops, Snapdragon” X Elite enables
Al-enhanced apps that unlock focus, flow and innovation. Because laptops powered by Snapdragon
technology work equally well plugged-in or on battery, your employees can work from wherever they need to.
Up to Up to
Snapdragon* X Elite: SKU Comparison Table
2x 5.4x i
FASTER NPU MORE EFFICIENT NPU secon | parm | cm
than M3! than Core Ultra 72 ss :
```

## Slide 8

## How do they debug Hexagon code?

###### **Hardware debugger**

- Lauterbach TRACE32 (JTAG/Coresight)

   - 3rd party product, endorsed by Qualcomm

   - **Requires Qualcomm “partner enrollment” level support to use it (impossible)**

   - Not applicable to off-the-shelf devices

   - Expensive

###### **Software debugger**

- Doesn’t exist

   - Code that runs on Hexagon arch is heavily proprietary and undocumented, you are not supposed to know about it, let alone debug it

- Engineer your own gdb server on software vulnerability primitives

   - **DIY** reports in the past

   - Limited, unreliable & unsustainable

- Hexagon emulator/simulator are available

   - You can write high-level app code in Hexagon SDK and “debug” it on simulator, no problem with that

   - Mostly useless for deep security research

## Slide 9

Trace32 User’s Manual is pessimistic…

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Trace32 User’s Manual is pessimistic...
1. Hexagon Conceptual Basics
Especially when starting to get familiar with the Hexagon architecture these points are of exceptional
importance:
.
Hexagon iis a’secure platform: by default) debugging is prohibited. Whether the user can debug a
specific application or not is configured by the application which is executed.
If you write your own application, please consult the Hexagon documentation on how to enable
debugging. If you are using a third-party application please contact the vendor of this application
for a debug-enabled version.
Beside from “debugging not allowed” there are two debugging levels:
- Untrusted debugging requires a debug monitor running under the control of the application
and RTOS.
Trusted debugging allows full control over the Hexagon core. See also Hexagon Security for
more information on the Hexagon debug modes.
Because the debugger does not have any access to the core by default, Hexagon needs to be
configured via some external “instance”. Normally an Arm core is responsible for configuration
and loading at least an initial application for enabling debugging. Please see the chipset’s
documentation on how to do this.
Hexagon Securi'
Hexagon has three debug modes:
1. No debugging allowed.
+ Untrusted debug.
The debugger communicates with a debug monitor integrated in the kernel. This allows debugging of
only a few resources, e.g. some dedicated user applications or tasks.
Trusted debug.
The debugger has full access and control over Hexagon.
TRACE32 only supports trusted debug.
The application running on the target selects the debug mode in its startup code. After this is done, a hard-
coded software breakpoint will halt the DSP.
11989-2024 Lav
```

## Slide 10

Wait, what is ISDB?

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Wait, what is ISDB?
ISDB
Television system :
©1989-2024 Lauterbach
SYStem.RESetOut ithout reset of debug port
Format: SYStem.RESetOut
This command resets the DSP via the debug registers in ISDB. Only the DSP will reset, not the debug port
or the target system. This function only works when the CPU is in SYStem.Mode Up.
Integrated Services Digital Broadcasting is a Japanese
broadcasting standard for digital television and digital
radio. ISDB supersedes both the NTSC-J analog
television system and the previously used MUSE Hi-
vision analog HDTV system in Japan. Wikipedia >
```

## Slide 11

## Start researching, mystery builds up…

Google knows little aside from a few patents…

Mentions in open source code added and removed…

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Start researching, mystery builds up...
C adreno_aSxx.c 5 X
drivers > gopu > msm > C adreno_a5xx.c > @ a5xx_start(adreno_device *)
if ((adreno_compare_pfp_version(adreno_dev, 0x5FF077) >= 0))
kgsl_regrmw(device, A5XX_PC_D! CNTL, @, (1 << 8));
kgsl_regwrite(device, A5XX_CP_CHICKEN_
BG, 0x02000000) ;
if (test_bit (ADRENO_DEVICE_ISDB_ENABLED, &adreno_dev->priv)) {
if (!kgsl_active_count_get(device)) {
kgsl_regwrite(device, A AHB_CNTL1, @x@6FFFFFF);
h k ISDB
kgsl_regwrite(device, A5XX_RBBM_CLOCK_CNTL_SP®, @x@);
kgsl_regwrite(device, A5XX_RBBM K_CNTL_SP1, @x@);
kgsl_regwrite(device, RBBI K_CNTL_SP2, @x®);
kgsl_regwrite(device, A5XX_RBBM.
kgsl_regwrite(device, A5XX_RBBM.
kgsl_regwrite(device, A5XX_RBBM
kgsl_regwrite(device,
kgsl_regwrite(device,
kgsl_regwrite(device,
kgsl_regwrite(device, A5X
} else
KGSL_CORE_ERR(
“active count failed while turning on TSDB."
A5XX_RBBM_CLOCK_CNTL, @x@);
( RBBM_ISDB_CNT, @x0);
} else {f
+DEF_MACRO(f£IN_DEBUG_MODE, (TNUM),
+ "in_debug_mode",
+ "“in_debug_mode",
(thread->debug_mode || (£READ_GLOBAL_REG_FIELD GREEpT "T_DEBUGMODE) & 1<<TNUM)),
+ )
+)
+DEF_MACRO(fIN_DEBUG_MODE_NO (TNUM),
& "in_debug_mode",
+ "in_debug_mode",
+ (thread->debug_mode) ,
ns 0)
+)
+ . ;
i Mentions in open source
+DEF_M . .
Male Google knows little aside code added and removed...
: from a few patents... Jource.com/kernel/msm/+/android-msm-dory-3.10-kitkat-wear/drivers/esoc/esoc-mdm~4x.c
qualeomm sdb" debugeing mdm->dbg_addr = addr + MOM_D8G_OFFSET;
val = readl_relaxed (mdm->dbg_addr) ;
if (val == MDMJDBG_MODE)
mdm->dbg_mode
mdm->cti = coresight_cti_get(MDM_CTI_NAME
4f (TS_ERR(mdm
dev_err (mdm
Google Patents
Non-intrusive, thread-selective, debugging method and system
{SDB 62, may be used to debug the DSP 40 operating system software, [SDB 62 supports debugging
true
hardware threads individually. Users may suspend thraad cti)
Google Patents
Method and system for trusted/untrusted digital signal processor
SDB 82 provides sofware debug features through JTAG interface 84 by sharing systom or supervisor-
goto cti_get.
ret = coresight_cti_map_trigout(mdm->cti, MDM_CTI_TRIG,
nly registers, tht are vided into superior coil MDM_CTI_
4f (ret)
ee yee dev_err (mdn->dev, "un:
QRB5165 features goto cti_map_err
Piayfteady $12000/S.3000, Widevne level 1 and level 3, ISDB-T fuse bits avaiable for
(OEM use. Access contol, Programmable secury domain nda->trigent
facies gmiomencon psec 20. dev_dbg(mdm->dev, "Not
QRBS165 mdm->dbg_mode = false;
1SD-T fuse bits avallabl
EM use, Access control. Programmable .. JTAG,
16 USB debug (EUD)
design fr software debug (OFS), em
```

## Slide 12

## Reverse Engineering Hexagon Debugging

###### **Sources - open**

### **Results**

- Patent documentation

- Qualcomm Programmer’s Reference Manuals

- Open source code

- Datasheets

- Qualcomm ISDB system internals revealed for the first time

###### **Methods - theoretical**

- OSINT

- Thinking

- Grepping QURT binaries for strings

- Open baseband firmware in IDA and close it

###### **Funding - private**

- This research project was partially sponsored by a company that chose to remain anonymous

   - Outlined basic prerequisites to enable and operate both trusted and untrusted debugging of Hexagon

   - ● This talk will focus on the core aspects of the matter due to limited time and disclosure, a lot had to be left out

   - Still a lot to uncover

- Findings approved for disclosure

- Thank you

## Slide 13

Fast forward to findings >>>

## Slide 14

Hexagon Debugging Internals

## Slide 15

ISDB (In Silicone Debugger)

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ISDB (In Silicone Debugger)
JTAG VF
ISDB
cil4
cilé
ISDB
MCD V/F
jtag_tck--->}
JTAG
ISDB JTAGSyne
jtag_tck---»
core_clock
Poste
core_clk ==>
cis
ISDB_gprDataOut
ETM_breakTrigger
ISDB
CUL
CONTROLLER
QDSP6 Core
core_clock--->
CONTROLLER
128
‘|
' cunitISDBlogic
core_clock
+
ISDB_reset ISDB_ interrupt
1324 Pe 134
cM
JTAG
INTERFACE
FARD
BREA\
SOPTWARE
BREAKPOINT
ix)
140
EIM YES
BREAKPOINT.
Ro
ITAG a
BREAKPOIN
No
EXTERNAL
BREAKPOINT,
1
DE
OPERATIO
148:
RESUME
NORMAL THREAD,
OPERATION
¥
ES
RESET E
CORE DSP
136
```

## Slide 16

Breakpoint processing circuitry

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Breakpoint processing circuitry
debugModeStatus_ ANY[0]
174
brkptinfo_D[2:0]
190
ucg_resumeTnum_ANY[0]
OR reset
```

## Slide 17

## Recap: JTAG IEEE 1149.1

**The standard**

- Basic technology for testing microelectronic circuits

- Simple interface - serial pins

   - TDI (Test Data In), TDO (Test Data Out)

   - Test mode selection, clock, reset

- **Very powerful**

- **No access control**

- **No resource control**

- Most device vendors either don’t care or rely on “security by obscurity” to hide JTAG port

<u>https://www.researchgate .net/publication/2206489 26_Security_extension_fo r_IEEE_Std_11491</u>

## Slide 18

## Extended JTAG pinouts

<u>https://www.allaboutcircu its.com/technical-articles/ jtag-connectors-and-interf aces/</u>

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Extended JTAG pinouts
a STOCHE intertace
ARM STAG 20 in STME2 STAGSWD with VCP)
APMLSTAG 14 TLITAG 2k CoreSight 20 Intertace ARM CoraSight 10 letertace
www.allaboutcircu
technical-articles,
-connectors-and-interf
```

## Slide 19

## JTAG and software debugging

- Powerful primitives

   - Access to memory

   - Access to registers

   - Halt signal

- Software debugger engineering

   - Build standard debugging ops on JTAG hardware primitives

   - wrap in GUI/CLI/gdb

   - FTDI (USB-TTL) for wiring

- Example: tracing/single step

   - Halt signal + program counter register modification

- Example: breakpoint

- Hardware bp: program the register

- Software bp: inject the opcode

<u>https://pinout.xyz/pinout/jtag</u>

- **OpenOCD**

<u>https://sysprogs.com/VisualKernel/tutorials/raspberry/ jtagsetup/</u>

## Slide 20

ISDB Registers

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ISDB Registers
; q ISDB_ aCe
CRIPTION ; SS UNTRUSTED| guPERVISOR
MODE*
sonst | _Woostaros | oo | e | «® | R
[BRKPTINFO | BREAKPOINTINFO_| og | _R | NONE_| NONE
:AKPOINT 0 ADDRESS NONE
BREAKPOINT 0 CONFIG Oxs NONE
MAILBOX IN (CORE-->IS
PR
Zz
a
¢
```

## Slide 21

Trusted and Untrusted debugging mode

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Trusted and Untrusted debugging mode
(54) Title: METHOD AND SYSTEM FOR TRUSTED/UNTRUSTED DIGITAL SIGNAL PROCESSOR DEBUGGING OPER
ATIONS
[0012 ] According to one aspect of the disclosed subject matter, a method and
system for controlling between trusted and untrusted debugging operational modes aniiiine
includes the processes, circuitry, and instructions for operating a core processor process —
within a core processor associated with the digital signal processor. The method and
system further operate a debugging process within a debugging mechanism of the
digital signal processor, which debugging mechanism associates with the core
processor. The core processor process determines the origin of debugging control as
trusted debugging control or untrusted debugging control. In the event that debugging
trol is trusted debugging control, the core processor process provides to the trusted
debugging control a first set of features and privileges. Alternatively, in the event that
```

## Slide 22

Supervisor Mode

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Supervisor Mode
Qualcomm Hexagon V73 Programmer's Reference Manual Instruction Set
Trap
The trap instruction causes a precise exception
Executing a trap instruction sets the EX bit in SSR to 1, which disables interrupts and enables
Supervisor mode. The program then jumps to the vector location (either TRAPO or TRAP1). The
instruction specifies a n 8-bit immediate field. This field is copied into the system status register
cause field.
Upon returning from the service routine with a RTE, execution resumes at the packet after the
TRAP instruction.
These instructions are generally intended for user code to request services from the operating
system. Two TRAP instructions are provided so the OS can optimize for fast service routines and
slower service routines.
Syntax Behavior
0 (#uB)
Assembler mapped to: "trap1(RO,#u8)"
apl_virtinsn(#u)) {
ISPSWAP;
```

## Slide 23

## SYSCFG register

- Hexagon architecture register, exposed to assembler

   - But, undocumented

   - Patent shows “one way of forming the register” →

- **Supervisor-only (privileged)**

   - QURT kernel OR application in privileged mode of execution; eg. modem firmware in early boot

- Use to set ISDB_TRUSTED bit

   - 0x28 == 0b0..1000

- ISDB status bit will be tested by host debugger and eligible others

- Patent documentation:

   - “Communication through a SYSCFG register as a 40-bit packet identifies the ISDB register to read/write and a 32-bit data payload”

   - RESERVED part?

## Slide 24

## How to program SYSCFG register?

V69 (2022)

V73 (2024) no longer mentions SYSCFG register layout & ISDB bits

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
How to program SYSCFG register?
Qualcomm Hexagon V60 Programmers Reference Manual bediociin Sa Qualcomm Hexagon V73 Programmer's Reference Manual Instruction Set
System control register transfer V69 (2022)
Move data between supervisor control registers and general registers.
Instruction synchronization
Registers can be moved as 32-bit singles or as 64-bit aligned pairs. The figure shows the system
control registers and their register field encodings. The isync instruction ensures that all previous instructions have committed before continuing to
the next instruction.
This instruction should execute after the following events (when subsequent instructions must
observe the results of the event):
After modifying the TLB with a TLBW instruction 5
rors ving V73 (2024) no longer mentions
After modifying the SSR register SYSCFG register layout &
After modifying the SYSCFG register ISDB bits
After any instruction cache maintenance operation
After modifying the TID register
Syntax Behavior
isyne instruction_sync;
Behavior Class: SYSTEM (slot 2)
Notes
sda-Res
Class: SYSTEM (slot 3) = This is a solo instruction. It must not be grouped with other instructions in a packet.
```

## Slide 25

Breakpoints

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Breakpoints
Qualcomm Hexagon V73 Programmer's Reference Manual Instruction Set
Breakpoint
The brkpt instruction causes the program to enter Debug mode'if enabled by ISDB,
Execution control is handed to ISDB and the program does not proceed until directed by the
debugger.
If ISDB is disabled, this instruction is treated as a NOP.
Syntax Behavior
brkpt r Debug mode;
Class: SYSTEM (slot 3)
Notes
= = This is a solo instruction. It must not be grouped with other instructions in a packet.
Encoding
31/30 29 28 27 26 25 24 23 22 21 20 19 18 17 16151413 1211109 8 7 6 5 43210
ICLASS ‘sm Parse
o4
1
0/1|1/0 0 0/0|1|-|-|-|-|-|pip|-|-|-|-)-|-|0|0 [0 |---| ~| = | bekpt
Field name —_Description
Supervisor mode only
Instruction class
Packet/loop parse bits
```

## Slide 26

## Magic Cookie

Newer msm kernels no longer leak it

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Magic Cookie
https://android.googlesource.com/kernel/msm/+/android-7.1.0_r0.2/drivers/esoc/esoc-mdm.h
Newer msm kernels no longer leak it
https://android.googlesource.com/kernel/msm/+/android-msm-dory-3.10-kitkat-wear/drivers/esoc/esoc-mdm-4x.c
#define MDM_PBLRDY_CNT 20 mdm->dbg_addr = addr + MDM_DBG_OFFSET;
#define INVALID_GPTO (-1) val = readl_relaxed(mdm->dbg_addr) ;
itdefine MDM_GPIO(mdm, i) (mdm->gpios[i]) TF (Wal nd otoe oot. true;
iade;f-ine|, MDM9X25_LABEL "BRHSEAS" ndm->cti = coresight_cti_get(MOM_CTI_NAME) ;
#define MDM9x25_HSIC "HSIC" 4f (1S_ERR(mdm->cti))
#define MDM9x35_LABEL "MDM9x35" dev_err(mdm->dev, “unable to get cti handle\n");
#define MDM9x35_PCIE "PCIe" goto cti_get_err;
#define MDM9x35_DUAL_LINK "HSTC+PCIe" ;
#define MDM9x35_HSIC “HSIC"
#define MDM9x45_LABEL "MDM9x45" Sf (ret) {
#define MDM9x45_PCIE "PCIe" dev_err(mdm->dev, “unable to map trig to channel\n");
#define MDM9x55_LABEL "MDM9x55" goto cti_map_err}
#define MDM9x55_PCIE "PCIe" }
#define MDM2AP_STATUS_TIMEOUT_MS 120000L
#define MDM_MODEM_TIMEOUT 3000 dev_dbg(mdm->dev, "Not in debug mode. debug mode = %u\n", val);
#define DEF_RAMDUMP_TIMEOUT 120000 mdm->dbg_mode = false;
#define DEF_RAMDUMP_DELAY 2000
#define RD_BUF_SIZE 100
define SFR_MAX_RETRIES 10
#define SFR_RETRY_INTERVAL 1000
#define MDM_DBG_OFFSET 0x934
#define MDM_DBG_MODE 0x53444247
#define MDM_CTI_NAME “coresight-cti-rpm-cpuo"
#define MDM_CTI_TRIG c)
#define MDM_CTI_CH r)
ret = coresight_cti_map_trigout(mdm->cti, MDM_CTI_TRIG,
MDM_CTI_CH) ;
mdm->trig_ent = 0;
} else {
```

## Slide 27

## Qualcomm IMEM

- Shared memory

- Exposed in MSM →

- Undocumented

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blob: 630fa1a07f118327627afb3da8b846fc92053130 [file] [log] [blame]
e Shared memory Qualcomm TNEM
e Exposed in MSM >
e Undocumented
IMEM is fast on-chip memory used for various debug features and dma transactions.
Required properties
-compatible: "qcom,msm-imem"
-reg: start address and size of imem memory
If any children nodes exist the following properties are required:
-#address-cells: should be 1
-#size-cells: should be 1
-ranges: A triplet that includes the child address, parent address, &
length. The child address is assumed to be 0.
Child nodes:
Peripheral Image Loader (pil):
Required properties:
-compatible: "qcom,msm-imem-pil"
-reg: start address and size of PIL region in imem
Bootloader Stats:
```

## Slide 28

## Enable Hexagon debugging with Magic Cookie

- QURT kernel operates ISDB, mostly via privileged mode

- It uses a simple flag-based mechanism to trigger ISDB operations for applications/users

- ● 0x53444247 (‘SDBG’ in hex)

- **Put the magic cookie in IMEM via JTAG**

   - You need to know **specific offset** in IMEM for each application/control

   - ○ Modem, PIL, mba, Android msm, QURT kernel will check the cookie

   - ○ Triggers software setup consistent with debug mode of thread, and/or **enter debug mode** via ISDB

Big secret

## Slide 29

qurtkernel.o

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
-Start :@00004F8 _AFB: DA
: memw_phys (r@, r1) }
e rT ) e @) f asl (r2, #loc_10)
q :
loc_500:
immext (#9)
memw (r25 + ##start) = r2.new }
: r10 = isdben }
-Start :0000050C pO = tstbit (r10, #(start+2))
-Start :00000510 if !pO.new jump:t _setup_isdb_cont }
immext (#9)
10 = memw (r25 + ##start)
if (cmp.eq (r10.new, #start)) jump:t _setup_isdb_cont }
immext (#9x53444240)
rll = ##0x53444247
memw (r10 + #start) }
cmp.eq (r10, r11)
ppoooed7C nmmext (#8) if !p@.new jump:t _setup_isdb_cont @ not equal
9000480 E ‘immext (#0)
0800480 Toevaees DATA XR r10 = add (r25, ##start) }
790000480 = 10 = memw (r25 + ##start) é memw (r16 + #start) = #(start+1)
000484 immext (#0) : memw (r16 + #loc_4) = #(start+1) }
900488 memw (r25 + ##start) } -Start:00000544 memw (r16 + #loc_8) =
00048C re } -Start :00000548
000490 chicken = @ S63 : 10000548 _setup_isdb_cont: @ CODE XREF: setup_isdb_cont+41j
#(start+l) }
9900494 : 9000548 @ setup_isdb_cont+30;j
900494 _configure_basic_syscfg: é 9000548 rl = #(start+1)
0900494 { r@ = sybefg } Ef }980054C immext (#0)
0000498 { 13:2 = combine (#start, #start) é 19800556 r17 = memw (r25 + ##start)
:0000049C r® = or (r@, #byte_42) } E 0000554 if (cmp.eq (ri7.new, #start)) jump:t _skip_isdb_debug }
sysctg = r@ } E 0000558 isdben = rl } @ enable
31:30 = 3:2 } : 98055C isyne }
isync } nanaren
immext (#0)
rO = memw (r25 + ##start)
immext (#0)
200000488 rl = memw (r25 + ##start) }
0004BC cmp.eq (r®, #start) ; if (pO.new) jump:nt _setup_isdb
004C0 cmp.eq (r1, #start) ; if (!pl.new) jump:nt _setup_isdb }
_Stop_at_bootup: @ CODE XREF: start_next:_stop_at_bootup.j
_stop_at_bootup }
19000048
90048
0048 _setup_isdb: @ CODE XREF: start_next+BCrj
19000048 @ start_next+COrj
r@ = #(loc_C+1)
call _setup_isdb }
immext (#0)
110 = memw (r25 + ##start)
if (cmp.eq (r1@.new, #start)) jump:nt _setup_isdb_start }
setup_isdb
```

## Slide 30

## Conclusions

#### **Technology summary**

- ISDB is the low-level debugging circuitry of Hexagon architecture which sits in-between JTAG and the core

   - Don’t confuse with ISDB-T, a digital TV broadcasting standard

- Debugging works by reading/writing ISDB registers, via either JTAG or software

- Multiple ways of doing things

- ● This research is the first step

   - System internals of ISDB

   - Key requirements to enable and control debugging over JTAG and via software

   - **○ Untested - may need extra config!**

##### **Security**

- Basically, ISDB is the **core gatekeeper of debugging** on Hexagon cores

   - Blocks JTAG if is ISDB_TRUSTED register is not set

   - Exposes software-based debugging controls via proprietary kernel code

- Trusted and Untrusted mode of execution

- Trusted: Qualcomm’s kernel dev

- ○ Untrusted: you

- ● Specialized enablement and configuration protocols

- **Qurt Kernel will check other debugging controls before enabling ISDB**

   - Build-time configuration variables

   - CoT & Attestation Certificates, Fuses, IMEM

## Slide 31

## References

1. A.Esage, “Advanced Hexagon Diag”, Chaos Communications Congress (2020) 2. A.Esage, “Deep Dive: Qualcomm MSM Linux Kernel & ARM Mali GPU 0-day Exploit Attacks of October 2023”, Zero Day Engineering Research Blog (2023)

3. APQ8016E Technical Reference Manual

4. Qualcomm® Snapdragon™ 410 Processor APQ8016 Hardware Register Description

5. Qualcomm® Snapdragon™ 410E (APQ 8016E) Processor Device Specification 6. WIPO patent no.2008/061067 A2

7. WIPO patent no.2008/061089 A2

8. US patent no.7,657,791 B2 of Feb. 2, 2010

9. Qualcomm Hexagon V66 Programmer’s Reference Manual (2017)

10. Qualcomm Hexagon V69 Programmer’s Reference Manual (2022) 11. Qualcomm Hexagon V73 Programmer’s Reference Manual (2024)

## Slide 32

# Q&A

Twitter/Youtube: @alisaesage

Email: contact@zerodayengineering.com
