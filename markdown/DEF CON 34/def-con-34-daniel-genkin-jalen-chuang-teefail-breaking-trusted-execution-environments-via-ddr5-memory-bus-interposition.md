---
title: "TEE.fail Breaking Trusted Execution Environments via DDR5 Memory Bus Interposition"
speakers: ["Daniel Genkin", "Jalen Chuang"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: 2026
source_pdf: "DEF CON 34/DEF CON 34 - Daniel Genkin, Jalen Chuang - TEE.fail Breaking Trusted Execution Environments via DDR5 Memory Bus Interposition - TEEFail v1.pdf"
pages: 22
sha256: "32adc2f7b42bb4c9842b232af692969eab89d905b6dd8f1bac393ee1552a1327"
text_chars: 6702
ocr_pages: 9
has_ocr: true
redacted_secrets: 0
ocr_confidence: 87.6
ocr_unreliable_blocks: 1
vision_verified_pages_changed: 21
vision_verified_pages: 22
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:25:20Z"
---
# TEE.fail Breaking Trusted Execution Environments via DDR5 Memory Bus Interposition

**Speakers:** Daniel Genkin, Jalen Chuang  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Daniel Genkin, Jalen Chuang - TEE.fail Breaking Trusted Execution Environments via DDR5 Memory Bus Interposition - TEEFail v1.pdf` (22 pages)


## Slide 1

# TEE.fail: Breaking Trusted Execution Environments via Memory Bus Interposition

**Jalen Chuang**

**Daniel Genkin**

Georgia Institute of Technology

Purdue University

## Slide 2

Bio

**Jalen Chuang**

**Daniel Genkin**

2

## Slide 3

## Trusted Execution Environments

- Hardware features that enforce data access control and code isolation

- Confidentiality and Integrity of data “guaranteed” by hardware

   - Even if everything but the CPU is malicious!

- Near native performance

- Has attestation mechanisms for setting up secure channels with remote clients

- **Trust is entirely based on the attestation key**

- Many versions of this in use today

- Today’s focus: Server TEEs

   - Intel SGX / TDX, latest AMD SEV-SNP

   - Present on many Intel CPUs (since 2016)

Privilege-stack diagram on the right. Each layer is a bar; an angry red face marks a layer the model treats as malicious, a smiling yellow face marks a trusted one. Top to bottom:

- User Space (angry face), with a green **Enclave** box (smiling face) inside the same bar
- OS Kernel (angry face), Windows logo
- VMM (angry face), an unlabelled virtualization product icon and the Xen logo
- SMM (angry face), a BIOS setup screenshot
- Bottom row of three separate bars: RAM (angry face), HW (angry face), and a green CPU bar (smiling face) with a key drawn over it

An **Attestation** arrow starts at the User Space / Enclave bar and points right, out of the stack, to the **Remote Client** — drawn as a detective holding a magnifying glass and a TOP SECRET folder.

Product logos below the stack: arm TRUSTZONE, arm CCA, AWS Nitro Enclave, AMD SEV-SNP, intel SGX, and intel XEON (3rd Gen Intel® Xeon® Scalable Processors).

3

## Slide 4

## Server SGX and TDX

- SGX has moved from client parts to servers

- TDX was launched (~2023)

   - Just run your VM

   - … but encrypted and totally secure!!!!!

- Much larger encrypted memory

   - From 128MB to 1TB

- Completely different security guarantees

   - Different memory encryption engine

   - CPU still prevents software from reading ciphertext

- TDX security is just as bad, and relies on SGX

Logos along the top right: intel SGX, intel TDX, intel XEON (3rd Gen Intel® Xeon® Scalable Processors), and a consumer Intel Core CPU badge struck through with a large red X — the X hides most of the wording, leaving only `CO`, `9` and `th Gen` legible.

| Protect Memory from | Attack Vector | Client SGX | Scalable SGX |
| --- | --- | --- | --- |
| Loss of Confidentiality | SW | Yes | Yes |
| Loss of Integrity | SW | Yes | Yes |
| Anti-Replay | SW | Yes | Yes |
| Loss of Confidentiality | HW | Yes | Yes* |
| Loss of Integrity | HW | Yes | No |
| Anti-Replay | HW | Yes | No |

Table 3: Memory Protections Comparison

A green arrow points in from the right edge of the table, its tip on the rule between the SW `Anti-Replay` row and the HW `Loss of Confidentiality` row — the row whose Scalable SGX cell is the asterisked `Yes*`.

*The final thing to note is that Scalable SGX for data center use TME which relies on AES-XTS mode for confidentiality. The cryptographic scheme used can only mitigate a class of HW attacks where the adversary can only see the cipher text once and not while the system is changing the data.

4

## Slide 5

## Inside Your Computer…

Photograph of a server motherboard, silkscreened `SUPER`, `X12SPL-`, `REV:1.02`. Two orange dashed rectangles are drawn on it: one around the CPU socket holding an Intel Xeon package, and one around the bank of blue DIMM slots below the socket. The blue DIMM bank above the socket is not boxed.

To the right the same package is shown enlarged — intel XEON, 3rd Gen Intel® Xeon® Scalable Processors — with a double-headed arrow between it and a DDR DIMM. Below the arrow a cartoon child peers through a magnifying glass at a handful of 1s and 0s. A money bag heaped with gold coins sits at the foot of the DIMM.

5

## Slide 6

## How do the pros do it?

Screenshot of a Keysight configure-and-quote page.

**U4970A DDR5 Protocol Debug and Analysis Solution** — Prices will be shown in your Quote.

Header bar: KEYSIGHT logo, a green tick, `Cancel`, `Add to Transaction`.

**Selected Configurations** (26 items) — Total: USD 277,565.00

The line-item list prints no column headings; the columns are quantity, model number, description and price.

|  |  |  |  |
| --- | --- | --- | --- |
| 1 | B4661A-2FP | LPDDR/2/3/4 Listing Decoder, fixed perpetual license | USD 11,234.00 |
| 1 | B4661A-3FP | DDR/2/3/4 and LPDDR/2/3/4 … Validation, fixed perpetual license | USD 5,692.00 |
| 1 | B4661A-4FP | DDR3/4, LPDDR2/3/4, and ONFi Analysis, fixed perpetual license | USD 7,891.00 |
| 1 | B4661A-5FP | DDR5 Analysis and Compliance Validation, fixed perpetual license | USD 15,338.00 |
| 1 | U4970A-DSC | U4970A DDR5 Bundle (M9502A Chassis U4164A Logic Analyzer) Bundle Adjustment | -USD 27,868.00 |

Total: USD 277,565.00

In the `B4661A-3FP` row a hover tooltip reading `B4661A-3FP` is drawn over the description and covers the words between `LPDDR/2/3/4` and `Validation, fixed perpetual license`; those words are genuinely hidden. The list is a scrolling pane — only 5 of the 26 configured items are on screen, so the five visible prices do not sum to the stated total.

Right pane: **Model Details**, a money-mouth emoji, captioned **DDR5 Bundle (M9502A Chassis U4164A Logic Analyzer)**.

6

## Slide 7

## Inside Your Computer…

The Intel Xeon package — intel XEON, 3rd Gen Intel® Xeon® Scalable Processors — and a DDR DIMM, joined by a single double-headed arrow standing for the memory bus. A money bag heaped with gold coins sits at the foot of the DIMM.

7

## Slide 8

## Inside Your Computer…

The same CPU-to-DIMM picture as the previous slide, but the bus is now cut in two by a photograph of a DIMM-socket interposer — a slot riser with a fan of ribbon-cable conductors soldered out of its pin rows. One double-headed arrow runs CPU ↔ interposer, a second interposer ↔ DIMM.

A speech bubble points at the CPU package:

**And don’t do that again!** — beside an angry red face emoji.

Bottom left, a photograph of the POST screen:

```text
Press F2 or DEL to run Setup.
Press F11 for Boot Menu.

Detected ATA/ATAPI Devices...
SATA Port0: HL-DT-ST DVDRAM GH24NSD1
SATA Port1: ST1000DM003-1SB10C
Press F1 to Continue

The following Channel memory did not pass CPU memory test.
Please remove the memory then plug again.
Channel B
```

The photograph's left edge clips the leading `P` of the first two lines; every other character is fully legible.

Beside it, a close-up of the board's status-LED block. Four LEDs are labelled, top to bottom, `BOOT`, `VGA`, `DRAM`, `CPU`; the `DRAM` and `CPU` LEDs are lit, `BOOT` and `VGA` are dark. Nearby silkscreen reads `ADDR`, `ADDR`, `LEDF4`, `LEDF3`, `LEDU7`, `LEDU10`, `LEDD8`, `LEDD7`, `PQ58`, `PQ62`.

8

## Slide 9

It boots!

Photograph of a **Tektronix CSA7404 Communications Signal Analyzer** — front-panel legend `4 GHz`, `20 GS/s`, `DPO`. The display holds a stopped single-sequence capture: status line `Tek  Stopped  Single Seq`, `1 Acqs`, timestamp `01 Dec 24 00:12:30`; menu tabs Vert, Horiz, Trig, Disp, Cursors, Meas, Masks, Math, Setups, Refs, Help, Menu.

Two traces are shown, each with a callout arrow:

- a green box labelled **CMD pin** points at the upper, irregular trace
- an orange box labelled **Clock** points at the lower, regularly periodic trace

Cursor readouts down the right edge: `Curs1 Pos` `2.27V`, `Curs2 Pos` `-530.0` (the unit and the V1/V2/ΔV readouts beneath it are covered by the green **CMD pin** callout). The measurement pane along the bottom of the screen — Ampl/Max/Min/Freq entries and the timebase line — is photographed too small to transcribe reliably and is not reproduced here.

**More Cable**

**(~276 more pins)**

To the right, a photograph of the rig: logic-analyzer probe pods clamped onto the interposer sitting in a DIMM slot, ribbon leads and coloured probe-tip caps running up out of frame.

9

## Slide 10

## MORE CABLE

Left photograph — a DDR4 DIMM riser with ribbon-cable conductors soldered to its contact fingers, silkscreened `DDR4 288Pin Adapter REV:A01`, the pin-number scale running 285, 280, 275 … 145 along the edge connector.

DDR4 interposer

Centre photograph — the DDR5 build: a green riser card with a bundle of ribbon leads running to four Agilent probe pods, each labelled `Agilent  N4834-61601  DOUBLE PROBE, FOOTPRINTS 1 & 4` and hand-labelled **POD 1**, **POD 2**, **POD 3**, **POD 4**.

DDR5 interposer

< $1000 each with secondhand parts

Top right, the probe-loading schematic. A vertical line runs from **Interposer DIMM Slot** at the top down to **Interposer Edge Connector (to Motherboard)** at the bottom, with arrowheads on the line pointing downwards. A tap leaves the middle of that line into a parallel pair — a 12 kΩ resistor on the upper branch, a 0.3 pF capacitor on the lower branch — and continues through a 3nH inductor to an arrow labelled **To Logic Analyzer**.

Bottom right, a macro photograph of the interposer's edge connector: hand-soldered wires on every gold finger, the silkscreened pin numbers 265, 260, 255, 250, 245 legible on both rows of contacts.

10

## Slide 11

## Even more cable

Photograph of the bench. On the left an open PC tower — power supply labelled `Thermaltake`, `SMART SERIES POWER SUPPLY`, and `SMART 700W` across the case front — with grey ribbon cables leaving the interposer in the DIMM slots, arcing out of the case and down to the right.

Behind it a Lenovo `ThinkCentre` small-form-factor PC. In front, an **Agilent 16902A LOGIC ANALYSIS SYSTEM**, its screen running *Agilent Logic and Protocol Analyzer (LPA)* with a Waveform window open (menu bar File, Edit, View, Setup, Tools, Markers, Run/Stop, Waveform, Window, Help).

The waveform pane lists these buses down the left, top to bottom: `COMMAND`, `CHIPID 0-2`, `CHIPID 3`, `BANK GROUP`, `BANK ADDR`, `ROW 0-3`, `ROW 4-17`, `COLUMN`, `READ DATA 0-7`, `READ DATA 8-15`, `READ DATA 16-23`, `READ DATA 24-31`, `READ CHECK BITS`, `READ DATA`, with at least one further row scrolled off the bottom. The `COMMAND` row steps through `Power Down…`, `Read`, `Activate`, `Power Down Exit (NOP)`. The hex bus values beside them are photographed too small to transcribe reliably and are not reproduced here.

11

## Slide 12

## Even more cable

Photograph of the portable rig, with a TSA baggage-inspection notice laid over the left of the frame and a cut-out of a blue-gloved TSA officer standing at the right.

The rig: a bare motherboard stood on end with a heatsink, a small LCD panel below it, and a coiled bundle of grey ribbon cable running from its DIMM interposer into a hard flight case. The case lid holds a screen showing the LPA listing window; the base holds a system board, a fan and a DIMM carrying a hand-written sticker reading `Win11+new LPA`.

The notice, in full:

> **Transportation Security Administration**
>
> **NOTICE OF BAGGAGE INSPECTION**
>
> To protect you and your fellow passengers, the Transportation Security Administration (TSA) is required by law\* to inspect all checked baggage. As part of this process, some bags are opened and physically inspected. Your bag was among those selected for physical inspection.
>
> During the inspection, your bag and its contents may have been searched for prohibited items. At the completion of the inspection, the contents were returned to your bag.
>
> If the TSA security officer was unable to open your bag for inspection because it was locked, the officer may have been forced to break the locks on your bag. TSA sincerely regrets having to do this, however TSA is not liable for damage to your locks resulting from this necessary security precaution.
>
> For packing tips and suggestions on how to secure your baggage during your next trip, please visit:
>
> **tsa.gov**
>
> We appreciate your understanding and cooperation. If you have questions, comments, or concerns, please feel free to contact the TSA Contact Center:
>
> **Toll-free telephone:** 1.866.289.9673
> **Direct telephone:** 571.227.2900 (U.S.)
> **Email:** TSA-ContactCenter@dhs.gov
>
> \*Section 110(b) of the Aviation and Transportation Security Act of 2001, 49 U.S.C. 44901(c)-(e)
>
> TSA-OSO Form 1000 (Rev. 1-13-2010)
>
> **Smart Security Saves Time**

12

## Slide 13

## Portable setup

Two photographs taken in a machine room, in front of an open server rack.

Left: a wheeled scissor-lift trolley carrying a rack server with its lid off, ribbon cables running from its DIMM area down to a hard-shell suitcase standing on the floor, more ribbon cable coiled around the case handle.

Right: the same trolley from closer in. The opened case sits on the trolley beside the server and holds a system board, an RGB-lit fan and cabling; a laptop propped in the case lid shows a dense blue-and-white logic-analyzer listing. Ribbon cables run from the server's DIMM slots into the case.

13

## Slide 14

## Demo 1 – setup and interposer

Live demo, backup: demo1.mp4

14

## Slide 15

## The Final Note

*The final thing to note is that Scalable SGX for data center use TME which relies on AES-XTS mode for confidentiality. The cryptographic scheme used can only mitigate a class of HW attacks where the adversary can only see the cipher text once and not while the system is changing the data.

_(tl;dr: we know our encryption sucks)_

Below the note, three side-by-side images: the Tux penguin as a clean original, the same penguin still plainly recognisable through a coloured-noise encryption, and a third panel of uniform random noise.

**Weak Deterministic Encryption**

Same input becomes same output

Right-hand diagram — the AES-XTS construction, drawn under a CPU-chip graphic, with a DIMM graphic below it:

- **address** — arrow into a box **block cipher encryption**
- a line leaves that box on the right, turns down, and feeds both XOR nodes on the data path
- **Plaintext** — a register of cells — arrow down into the first ⊕
- first ⊕ — arrow down into a second box **block cipher encryption**
- **Key₁** — arrow into that second box from the left
- second box — arrow down into the second ⊕
- second ⊕ — arrow down into **Ciphertext**, a register of cells

15

## Slide 16

## The Final Note

*The final thing to note is that Scalable SGX for data center use TME which relies on AES-XTS mode for confidentiality. The cryptographic scheme used can only mitigate a class of HW attacks where the adversary can only see the cipher text once and not while the system is changing the data.

_(tl;dr: we know our encryption sucks)_

Same slide as the previous one, but the Tux panels are replaced by a logic-analyzer listing screenshot, and a large green arrow points left from the words:

**Let’s see this on real hardware!**

The listing:

```text
Sample Number          Data           ECC   Plaintext Data
           -1   FFFF FFFF FFFF FFFF   FFFF
            0   FFFF FFFF FFFF FFFF   FFFF
           31   7168 BE2C 20D2 83FD   65EA   0000 0000 0000 0000
           32   7080 148D 7C6E 417E   C3F0   0000 0000 0000 0000
           33   E102 0819 9350 64E3   6B44   0000 0000 0000 0000
           34   2737 9AEC 2E22 EB30   335F   0000 0000 0000 0000
           35   24A9 2776 25F3 5622   102A   0000 0000 0000 0000
           36   B69E E26B 3645 F4AA   A1F0   0000 0000 0000 0000
           37   1123 A1D5 63DC 3B12   3178   0000 0000 0000 0000
           38   9BB8 6E8B 5445 5CE3   6CAE   0000 0000 0000 0000
          382   FFFF FFFF FFFF FFFF   FFFF
          517   FFFF FFFF FFFF FFFF   FFFF
          518   FFFF FFFF FFFF FFFF   FFFF
          549   42DA E2AE 180E 6848   E79C   ffff ffff ffff ffff
          550   29A6 CE17 7F2F D528   8BE9   ffff ffff ffff ffff
          551   90CA BE10 8288 9305   2972   ffff ffff ffff ffff
          552   D0E0 E819 32FE E77E   A7AA   ffff ffff ffff ffff
          553   2AA5 C0EB 3217 DD87   792A   ffff ffff ffff ffff
          554   12D2 11C0 9CB3 99C0   BB01   ffff ffff ffff ffff
          555   B38D F824 B343 CF9F   E20A   ffff ffff ffff ffff
          556   96C1 2045 7741 5A34   AB0D   ffff ffff ffff ffff
          906   FFFF FFFF FFFF FFFF   FFFF
         1041   FFFF FFFF FFFF FFFF   FFFF
         1042   FFFF FFFF FFFF FFFF   FFFF
         1073   7168 BE2C 20D2 83FD   65EA   0000 0000 0000 0000
         1074   7080 148D 7C6E 417E   C3F0   0000 0000 0000 0000
         1075   E102 0819 9350 64E3   6B44   0000 0000 0000 0000
         1076   2737 9AEC 2E22 EB30   335F   0000 0000 0000 0000
         1077   24A9 2776 25F3 5622   102A   0000 0000 0000 0000
         1078   B69E E26B 3645 F4AA   A1F0   0000 0000 0000 0000
         1079   1123 A1D5 63DC 3B12   3178   0000 0000 0000 0000
         1080   9BB8 6E8B 5445 5CE3   6CAE   0000 0000 0000 0000
         1424   FFFF FFFF FFFF FFFF   FFFF
```

Three yellow rectangles are drawn over the Data column, boxing samples 31–38, 549–556 and 1073–1080. Samples 31–38 and 1073–1080 are byte-for-byte identical in both Data and ECC — the point of the slide. The rows with no plaintext (-1, 0, 382, 517, 518, 906, 1041, 1042, 1424) are highlighted in teal; on the rows where a yellow box edge crosses the Data column (0, 382, 518, 906, 1042, 1424) the glyphs are only half visible, but what shows is `FFFF FFFF FFFF FFFF` as on the fully visible rows. The listing continues past sample 1424, below the bottom edge of the slide. Gutter markers sit beside samples -1 and 0.

Right-hand diagram — the AES-XTS construction, drawn under a CPU-chip graphic, with a DIMM graphic below it:

- **address** — arrow into a box **block cipher encryption**
- a line leaves that box on the right, turns down, and feeds both XOR nodes on the data path
- **Plaintext** — a register of cells — arrow down into the first ⊕
- first ⊕ — arrow down into a second box **block cipher encryption**
- **Key₁** — arrow into that second box from the left
- second box — arrow down into the second ⊕
- second ⊕ — arrow down into **Ciphertext**, a register of cells

16

## Slide 17

## Demo 2 – deterministic encryption

Live demo

Screenshot of the analyzer software. Title bar: `Agilent Logic and Protocol Analyzer (LPA) - [..\Desktop\ddr5-        demo2.ala] - [Listing-1]` (the file path is printed with that wide gap in it). Menu bar: File, Edit, View, Setup, Tools, Markers, Run/Stop, Listing, Window, Help. Above the grid: `Click here to insert new measurements`. Tabs along the bottom: Overview, Waveform-1, Listing-1. Status bar: `For Help, press F1` … `Status...` … `Local`.

```text
Sample Number       Time      Command  ChipID 0-2  ChipID 3  BGroup  Bank  Row 0-3  Row 4-17  Column         Data           ECC   Plaintext Data
           -1    -625 ps      Read          0          0        5      3      F      05FD      1FD    FFFF FFFF FFFF FFFF   FFFF
            0       0 s       Activate      3          0        2      3      C      1AF0      0F0    FFFF FFFF FFFF FFFF   FFFF
           31   19.450 ns     NOP           7          1        7      3      F      3FFF      1FF    7168 BE2C 20D2 83FD   65EA   0000 0000 0000 0000
           32   20.075 ns     NOP           7          1        7      3      F      3FFF      1FF    7080 148D 7C6E 417E   C3F0   0000 0000 0000 0000
           33   20.700 ns     NOP           7          1        7      3      F      3FFF      1FF    E102 0819 9350 64E3   6B44   0000 0000 0000 0000
           34   21.325 ns     NOP           7          1        7      3      F      3FFF      1FF    2737 9AEC 2E22 EB30   335F   0000 0000 0000 0000
           35   21.950 ns     NOP           7          1        7      3      F      3FFF      1FF    24A9 2776 25F3 5622   102A   0000 0000 0000 0000
           36   22.575 ns     NOP           7          1        7      3      F      3FFF      1FF    B69E E26B 3645 F4AA   A1F0   0000 0000 0000 0000
           37   23.225 ns     NOP           7          1        7      3      F      3FFF      1FF    1123 A1D5 63DC 3B12   3178   0000 0000 0000 0000
           38   23.850 ns     NOP           7          1        7      3      F      3FFF      1FF    9BB8 6E8B 5445 5CE3   6CAE   0000 0000 0000 0000
          382  239.750 ns     Activate      3          0        2      3      C      1AF0      0F0    FFFF FFFF FFFF FFFF   FFFF
          517  324.425 ns     Read          0          0        5      3      F      05FD      1FD    FFFF FFFF FFFF FFFF   FFFF
          518  325.050 ns     Activate      3          0        2      3      C      1AF0      0F0    FFFF FFFF FFFF FFFF   FFFF
          549  344.500 ns     NOP           7          1        7      3      F      3FFF      1FF    42DA E2AE 180E 6848   E79C   ffff ffff ffff ffff
          550  345.125 ns     NOP           7          1        7      3      F      3FFF      1FF    29A6 CE17 7F2F D528   8BE9   ffff ffff ffff ffff
          551  345.750 ns     NOP           7          1        7      3      F      3FFF      1FF    90CA BE10 8288 9305   2972   ffff ffff ffff ffff
          552  346.375 ns     NOP           7          1        7      3      F      3FFF      1FF    D0E0 E819 32FE E77E   A7AA   ffff ffff ffff ffff
          553  347.000 ns     NOP           7          1        7      3      F      3FFF      1FF    2AA5 C0EB 3217 DD87   792A   ffff ffff ffff ffff
          554  347.625 ns     NOP           7          1        7      3      F      3FFF      1FF    12D2 11C0 9CB3 99C0   BB01   ffff ffff ffff ffff
          555  348.250 ns     NOP           7          1        7      3      F      3FFF      1FF    B38D F824 B343 CF9F   E20A   ffff ffff ffff ffff
          556  348.875 ns     NOP           7          1        7      3      F      3FFF      1FF    96C1 2045 7741 5A34   AB0D   ffff ffff ffff ffff
          906  568.500 ns     Activate      3          0        2      3      C      1AF0      0F0    FFFF FFFF FFFF FFFF   FFFF
         1041  653.100 ns     Read          0          0        5      3      F      05FD      1FD    FFFF FFFF FFFF FFFF   FFFF
         1042  653.725 ns     Activate      3          0        2      3      C      1AF0      0F0    FFFF FFFF FFFF FFFF   FFFF
         1073  673.225 ns     NOP           7          1        7      3      F      3FFF      1FF    7168 BE2C 20D2 83FD   65EA   0000 0000 0000 0000
         1074  673.850 ns     NOP           7          1        7      3      F      3FFF      1FF    7080 148D 7C6E 417E   C3F0   0000 0000 0000 0000
         1075  674.475 ns     NOP           7          1        7      3      F      3FFF      1FF    E102 0819 9350 64E3   6B44   0000 0000 0000 0000
         1076  675.100 ns     NOP           7          1        7      3      F      3FFF      1FF    2737 9AEC 2E22 EB30   335F   0000 0000 0000 0000
         1077  675.725 ns     NOP           7          1        7      3      F      3FFF      1FF    24A9 2776 25F3 5622   102A   0000 0000 0000 0000
         1078  676.350 ns     NOP           7          1        7      3      F      3FFF      1FF    B69E E26B 3645 F4AA   A1F0   0000 0000 0000 0000
         1079  676.975 ns     NOP           7          1        7      3      F      3FFF      1FF    1123 A1D5 63DC 3B12   3178   0000 0000 0000 0000
         1080  677.600 ns     NOP           7          1        7      3      F      3FFF      1FF    9BB8 6E8B 5445 5CE3   6CAE   0000 0000 0000 0000
         1424  893.450 ns     Activate      3          0        2      3      C      1AF0      0F0    FFFF FFFF FFFF FFFF   FFFF
         1559  978.125 ns     Read          0          0        5      3      F      05FD      1FD    FFFF FFFF FFFF FFFF   FFFF
         1560  978.750 ns     Activate      3          0        2      3      C      1AF0      0F0    FFFF FFFF FFFF FFFF   FFFF
         1591  998.200 ns     NOP           7          1        7      3      F      3FFF      1FF    42DA E2AE 180E 6848   E79C
         1592  998.825 ns     NOP           7          1        7      3      F      3FFF      1FF    29A6 CE17 7F2F D528   8BE9
         1593  999.450 ns     NOP           7          1        7      3      F      3FFF      1FF    90CA BE10 8288 9305   2972
         1594  1.000100 us    NOP           7          1        7      3      F      3FFF      1FF    D0E0 E819 32FE E77E   A7AA
         1595  1.000725 us    NOP           7          1        7      3      F      3FFF      1FF    2AA5 C0EB 3217 DD87   792A
         1596  1.001350 us    NOP           7          1        7      3      F      3FFF      1FF    12D2 11C0 9CB3 99C0   BB01
         1597  1.001975 us    NOP           7          1        7      3      F      3FFF      1FF    B38D F824 B343 CF9F   E20A
         1598  1.002600 us    NOP           7          1        7      3      F      3FFF      1FF    96C1 2045 7741 5A34   AB0D
```

Three yellow rectangles are drawn over the Data column, boxing samples 31–38, 549–556 and 1073–1080; the samples with no plaintext decode are highlighted in teal. Where a yellow box edge crosses a teal row's Data cell (0, 382, 518, 906, 1042, 1424) the glyphs are only half visible, and what shows is `FFFF FFFF FFFF FFFF` as on the fully visible rows. The last group, 1591–1598, has an empty Plaintext Data column.

17

## Slide 18

## Boring Math Slide

Top left, set in four stacked lines beside a key-over-`intel inside`-chip graphic and a sealed scroll labelled **Quote**: **ECSDA Private Attestation Key**

A large black arrow runs left to right from that group to a cartoon detective, labelled **Remote Client**.

Green box, the ECDSA signing steps (a shushing-face emoji sits beside step 2):

```text
1. z = Hash(quote)
2. k = random()
3. (x,y) = [k]G
4. r = x mod n
5. s = k⁻¹(z+rd_priv)
6. Output (r,s)
```

A yellow callout, its tail pointing back at the green box, holds:

**Recovering the nonce k reveals the key**

k is processed in 5-bit chunks

K=**k₁ k₂ k₃ ... kₙ**

Below that, a DIMM graphic and a CPU-package graphic. The CPU is captioned `[k`…`]G` — several builds of the caption are printed on top of one another, so the subscript on `k` is not readable. To their right an ellipsis `. . .`, and five gold arrows fan inwards and down from across the callout to converge on **[k]G**.

Right-hand column, top to bottom:

- Pink box: **Observe encrypted values and mount a dictionary attack**
- A dictionary-book icon, a gold double-headed horizontal arrow, and a green arrow pointing down
- **Deduce kᵢ**
- A yellow key with a green luggage tag reading **Attestation Private key**
- In orange, **in about 1.5 min**. A second run of black monospace text is printed underneath it and is clipped by the bottom of its panel; between the overlap and the clipping it cannot be transcribed.
- A photograph of a benchtop logic analyzer displaying a waveform window

18

## Slide 19

## Demo 3 – key extraction

Live demo, backup: demo3.mp4

19

## Slide 20

## Who cares?

- We extract SGX/TDX attestation keys

   - First time for TDX

- Attacker can pretend to be running a TEE in a genuine Intel CPU

- Signal uses SGX for password recovery (on Azure)

- Blockchains love “decentralized” TEEs

   - Support fancy confidential transactions and smart contracts

   - Fully decrypted if even a single node is compromised ☺

- NVIDIA Confidential Compute relies on CPU TEE

   - Without linking attestation reports to the specific CPU (printed with a literal leading hyphen, below the rubber-duck graphics)

- AMD SEV-SNP with latest mitigations similarly affected

Graphics down the right of the slide.

Top right: a yellow key with a green tag reading **Attestation Private key**; badges for intel TDX, intel SGX and intel XEON (3rd Gen Intel® Xeon® Scalable Processors) beside a CPU-die photograph.

Below them, an image captioned **M4** over **intel SGX** with a key drawn on it, a hand-drawn **Subpoena — YOU ARE COMMANDED** document, and the dstack, Secret network and Ethereum logos.

Beside those, a three-block chain diagram. Three purple cubes each carrying an `intel inside` logo, captioned **BLOCK 1**, **BLOCK 2**, **BLOCK 3**, with a chain-link icon drawn between 1 and 2 and between 2 and 3. Under each block:

| | BLOCK 1 | BLOCK 2 | BLOCK 3 |
| --- | --- | --- | --- |
| Hash: | 6U9P2 | 8Y5C9 | 9L4Z1 |
| Previous hash: | 00000 | 6U9P2 | 8Y5C9 |

A red curved arrow runs from BLOCK 1's `Hash` to BLOCK 2's `Previous hash`, and another from BLOCK 2's `Hash` to BLOCK 3's `Previous hash`.

Bottom left: a photograph of a yellow rubber duck, an arrow to a 3D-printed blue duck. Above the arrow, **Use AI** with the OpenAI mark; below it, **STL file for 3d printer**.

Beside that: a pink scroll with an `intel inside` seal and a green tick, the **M4 / intel SGX** image with a key, then an arrow labelled **~3$ / hour** pointing into a blue cloud that holds a GPU card, two sealed scrolls with green ticks (one `intel inside`, one NVIDIA), and an intel TDX badge.

Bottom right, the NVIDIA confidential-computing diagram, two panels side by side.

Left panel, labelled **GPU 1** at the bottom. In its upper band: a box **Traditional VM** containing a green **NVIDIA Driver** box, with **Host OS** and **Hypervisor** drawn as separate boxes outside the VM. In its lower band: a white box **GPU CC Off**. A single double-headed vertical arrow joins the NVIDIA Driver and GPU CC Off.

Right panel, labelled **GPU 2** at the bottom. A rectangle labelled **TEE** spans both bands and encloses a dark-green **Confidential VM** box (which itself contains a green **NVIDIA Driver** box) in the upper band and a green **GPU CC On** box in the lower band. Between them the label **Encrypted Transfers**, with two separate single-headed arrows: one above the label pointing up into the NVIDIA Driver, one below it pointing down into GPU CC On. The **GPU 2** caption sits outside the TEE rectangle.

20

## Slide 21

## Mitigations

- Out of Scope.

   - Intel: “Such attacks are outside the scope of the boundary of protection offered [by SGX / TDX]”

   - Similar response from AMD

   - Users get to deal with it ☺

- Talked to Intel…

- Weak security for performance reasons

   - Gave up integrity, replay protection and randomized encryption

   - At the benefit 30%-50% improvement in memory bandwith

- CPUs can’t be updated to fix this

   - ETA for hardware countermeasures 2029+

- Software fixes have severe performance implications, good luck…

21

## Slide 22

## Thanks!

A QR code with a small blue teapot glyph (X-ed-out eyes) set in its centre.

This: https://tee.fail

Us: https://architecture.fail

DEFCON 34

On the right, a photograph of a page of *Frog and Toad*, with black boxes and red handwriting pasted over the printed text:

> Frog put the cookies in ⟦SGX / TDX⟧ “There,” he
> said. “Now we will not eat any more cookies.”
> “But we can ⟦still use side channels⟧ x,” said Toad.
> “That is true,” said Frog.

The first overlay is a black box printing `SGX` in white, struck through with a large red X, with `TDX` written above it in red. The second is a black box printing `use side channels` over two lines, with `still` written in red across its top-left corner. Both cover the book's original wording; of the words they hide, only the trailing `x,` on the third line still shows.

