---
title: "Decoding EM-FI Attacks Lessons Learned from Glitching the GigaDevice GD32F407"
speakers: ["Jonathan Andersson", "Thanos Kaliyanakis"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2024"
edition: "Europe"
year: 2024
source_pdf: "BlackHat_Europe_2024_slides/Jonathan Andersson & Thanos Kaliyanakis_Decoding EM-FI Attacks Lessons Learned from Glitching the GigaDevice GD32F407.pdf"
pages: 50
sha256: "0774f4e3ee8f77eef80b69b52c152be6085c21a13c8e0a46d3bdb1f755bdbba8"
text_chars: 15571
ocr_pages: 4
has_ocr: true
redacted_secrets: 0
ocr_confidence: 81.1
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:58:06Z"
---
# Decoding EM-FI Attacks Lessons Learned from Glitching the GigaDevice GD32F407

**Speakers:** Jonathan Andersson, Thanos Kaliyanakis  
**Conference:** Black Hat Europe 2024  
**Source:** `BlackHat_Europe_2024_slides/Jonathan Andersson & Thanos Kaliyanakis_Decoding EM-FI Attacks Lessons Learned from Glitching the GigaDevice GD32F407.pdf` (50 pages)


## Slide 1

# Decoding EM-FI Attacks: Lessons Learned from Glitching the GigaDevice GD32F407 Jonathan Andersson & Thanos Kaliyanakis

#BHEU @BlackHatEvents

## Slide 2

Jonathan Andersson Sr. Manager Advanced Security Research Group Trend Micro ZDI

Thanos Kaliyanakis Vulnerability Researcher Advanced Security Research Group Trend Micro ZDI

#BHEU @BlackHatEvents

## Slide 3

## Agenda

- Introduction & Background

- The Rig

- Getting Started

- The Attack

- Calibration

- Perfecting the Glitch

- Attack Results

- Mitigations

- Conclusions

Information Classification: General

#BHEU @BlackHatEvents

## Slide 4

# Introduction & Background

#BHEU @BlackHatEvents

## Slide 5

## Introduction

- Why the GD32F407?

- Why fault injection?

- Why EM-FI?

Autel MaxiCharger

Information Classification: General

#BHEU @BlackHatEvents

## Slide 6

## GigaDevice vs STMicro - 32F407

© John McMaster

GD32F407

ST32F407

Information Classification: General

#BHEU @BlackHatEvents

## Slide 7

## Read Out Protection Levels

- None / RDP 0

   - No restrictions

- Low / RDP 1

   - Flash accessible only in flash boot mode

   - Flash disabled when SWD attached

   - Can be reverted to None / RDP 0 but flash gets erased

- High / RDP 2

   - SWD cannot attach

   - Only flash mode boot allowed

Lock by Puspa Kusuma CC BY 3.0 / blue with shadow

- No reversion back to lower security levels possible

Information Classification: General

#BHEU @BlackHatEvents

## Slide 8

# The Rig

#BHEU @BlackHatEvents

## Slide 9

## The Rig (~$600 USD)

- ChipSHOUTER PicoEMP with firmware additions

- Managed USB hub with individual power control

- XYZ table (G-Code)

- Programmable power supply

- SWD debugger (OpenOCD / GDB)

- USB to serial (console)

- 3D printed parts (PicoEMP & PCB mounts)

- Custom python code driving the rig

Information Classification: General

#BHEU @BlackHatEvents

## Slide 10

## The Rig

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
bistkhat The Rig
Information Classification: Genera
Python PC
USB to Serial (console)
—
Managed USB Hub
Power Supply
XYZ Table
GD32F407 Target
SWD Debugger
```

## Slide 11

## The Rig – Purchase Links

PicoEMP $100

XYZ Table $137

Power Supply $140

Managed USB Hub $176

USB to serial $14

SWD Debugger $10

Information Classification: General

#BHEU @BlackHatEvents

## Slide 12

## Custom 3D Printed Parts

- PicoEMP & PCB mount 3D models on www.zerodayinitiative.com/blog soon…

- Limit switch mounts (Thingiverse)

Information Classification: General

#BHEU @BlackHatEvents

## Slide 13

## ChipSHOUTER PicoEMP – DIY

- https://github.com/newaetech/chipshouter-picoemp

- PCB + ~$90 in parts

- Required DigiKey and Mouser BOMs:

DigiKey Cart

Mouser Cart

Information Classification: General

#BHEU @BlackHatEvents

## Slide 14

## PicoEMP Firmware Additions

- Added an all-in-one (4 into 1) command to maximize glitch rate

- Added deterministic pulse counting trigger in PIO

   - Used for basic serial triggering functionality

- Posted to original git soon…

chipset by pictranoosa CC BY 3.0 / blue with shadow

Information Classification: General

#BHEU @BlackHatEvents

## Slide 15

# Getting Started

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 72/100 on the text kept, 53/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Getting Started _—_
#BHEU @BlackHatEvents
```

## Slide 16

## First, Educate Yourself

#### Target CPU & supporting hardware

- Datasheets

- Programming resource guides

- Security application notes

- Prior research

Document by Dicky Prayudawanto CC BY 3.0 / multiple blue with shadow

- Understand how HW security mitigations are supposed to work in detail…

Information Classification: General

#BHEU @BlackHatEvents

## Slide 17

### Enumerate Vendor Mitigations & Security Measures

- Don’t believe the datasheet, verify for yourself!

- Confirm the device’s behavior in various scenarios…

   - What can and can’t be done with JTAG/SWD in various modes?

   - What memories can be accessed and how?

   - Are register changes allowed?

   - Is stepping allowed?

- Examine the edge cases…

   - Reset / boot sequencing / debug attachment

   - Memory persistence?

   - Halt/run states

Detective by Visual Glow CC BY 3.0 / blue with shadow

Information Classification: General

#BHEU @BlackHatEvents

## Slide 18

## What Dimensions to Control & Automate?

- Trigger

- Controlled parameters :

   - Target (V)oltage (VCC)

   - (D)elay

   - Spatial dimensions (X, Y, Z)

   - (P)ulse power

   - System state / device mode

control by SHAHAREA CC BY 3.0 / blue with shadow

Information Classification: General

#BHEU @BlackHatEvents

## Slide 19

## What Data to Collect?

- Primary

   - Controlled dimensions

   - Target’s current draw

   - Clock out / memory signals / other I/O

- Secondary

   - Program counter / CPU fault status

   - Console output

- Glitch loop / code timing!

- Use a scope to validate everything from the beginning

data collection by Fahri CC BY 3.0 / blue with shadow

- Monitor ongoing operations with the scope!

Information Classification: General

#BHEU @BlackHatEvents

## Slide 20

## Coding & Ops

- Code

   - Isolate config parameters into a single file

   - Code for resumability

   - Use exception handling

- Log everything!

   - Keep a textual diary

   - Log what you did and plan to do

Recycle by Vicons Design CC BY 3.0 / blue with shadow

- Document and analyze observations every run...

- Document data thoroughly – today’s trash is tomorrow’s treasure!

Information Classification: General

#BHEU @BlackHatEvents

## Slide 21

# The Attack

#BHEU @BlackHatEvents

## Slide 22

## The Attack – Bootloader Mode

- Extracted bootloader from unlocked GD32F407 via SWD

- Reversed in Ghidra

- Noted bootloader compatible with ST

- Located same Read Memory command

- The attack

   - Boot into bootloader

   - Issue Read Memory command (0x11)

   - Glitch

processing power by Juicy Fish CC BY 3.0 / blue with shadow

- Wait for NACK (0x7F) or ACK (0x79)

Information Classification: General

#BHEU @BlackHatEvents

## Slide 23

## The Attack – Read Memory Command

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 75/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
biStkhat The Attack— Read Memory Command
void Read Memory _cmd FUN 1£ff£f£0774 (void)
{ =
— if (command = Oxll) {
se isa goto Bootloader Main Loop LAB l1fff4éfa;
if (({opt and length « Oxff00) == Oxaadd) {
Serial TX byte FUN _1fff3c04 (0x79);
address = get_address FUN 1fff3at0();
Information Classification: General
```

## Slide 24

## The Attack – An Example Glitch

Trigger

RDP Check

Programmable (D)elay

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
piStkhat The Attack—An Example Glitch
NACK 0x7F
Trigger
=
«
Information Classification: General P rog ram mM abl e ( D) el ay
```

## Slide 25

# Calibration: Establishing Glitch Influence

#BHEU @BlackHatEvents

## Slide 26

## Scan For a Sensitive Spot…

- First, verify glitch production with a scope!

- Use _strong glitches_ : Z = min & P = max & Target VCC = min (lift brownout protection pin)

   - Z is correlated to (P)ulse power and VCC

- Step size: our probe tip resolution is ~1-2 mm<sup>2</sup> , use ~0.2mm steps

- • Post-glitch look at current / brownouts / resets / PC / CPU faults / CLK OUT / memory bus

- • Spiral scan…

dimensions by Dániel Z. Aczél CC BY 3.0 / blue with shadow

Information Classification: General

#BHEU @BlackHatEvents

## Slide 27

## Why Spirals?

- _With QFP, all unique sensitivity behaviors can be observed in concentric rings ~25 to 50% the distance between die edge and pins_

- _Distinct sensitivity regions form radial lobes aligned with lead frame_ – “flower petals”

TQFP Leadframe © NobbiP. CC BY-SA 2.5 / Cropped

Information Classification: General

#BHEU @BlackHatEvents

## Slide 28

## Calibrate Pulse Power & VCC

- Seek to one sensitive spot & collect data…

- Calibrate

   - Dial it back: _strong glitches_ will preclude _useful_ influence!

   - Independently reduce P & Increase VCC: _Note their ranges of influence_

   - Minimum VCC? - Consider % of zero current states vs continuation

      - 1.62V: 0.62% Brownout, 0.62% Unreadable PC

verify by WEBTECHOPS LLP CC BY 3.0 / blue with shadow

      - 1.61V: 33.33% , 38.27%

      - 1.51V: 53.70%, 98.15% (minimum operating voltage)

   - Sweet spot == ‘balanced’ mix of low current vs continuation

- Each sensitive area may have different optimum P & VCC

Information Classification: General

#BHEU @BlackHatEvents

## Slide 29

## Program Counter Logging

- Sweet spots == modified code paths

- Characterizes level of glitch influence

   - Unreadable? (brownout or lockup – extreme influence)

   - In fault ISR? (significant influence)

   - Is PC still in expected code loop? (no or low influence)

- Also illuminates possible attacks…

   - In user writable RAM / buffer controllable by user?

   - Random place (existing useful code – get lucky?)

List by VERA CC BY 3.0 / blue with shadow

Information Classification: General

#BHEU @BlackHatEvents

## Slide 30

# Perfecting the Glitch

#BHEU @BlackHatEvents

## Slide 31

## Perfecting the Glitch – Trigger

- A stable trigger is key to reproducibility, repeatability, and progression

   - Trigger -> Delay -> Glitch: Hard timing is required on nS scale!

   - Manual triggering is useless

   - Reducing trigger jitter can reduce (D)elay window

- Sooner is better than later

   - Leverage boot code processes (register config, memory copies)

   - Multitasking / multiprocessing are your enemies!

Present by Hayashi Fumihiro CC BY 3.0 / blue with shadow

Information Classification: General

#BHEU @BlackHatEvents

## Slide 32

## Perfecting the Glitch – Delay

- ARM fault status registers contain PC of fault (see Memfault’s blog)

- _ARM faults associate (D)elay with exact location of a strong glitch’s influence in code!_

   - Seek to one sensitive spot

   - Use _strong glitches_ and log fault PCs…

   - Establish a range of (D)elay around your glitch target PC

- Without reading ARM fault status registers…

   - (D)elay range is much larger, increasing brute force time

Stopwatch by Andre Buand CC BY 3.0 / blue with shadow

Information Classification: General

#BHEU @BlackHatEvents

## Slide 33

## Perfecting the Glitch – Optimization

- Glitch rate optimization is key! (It’s brute force, of course!)

- Reduce iterated parameter count and range

   - Collapse overlapping effects / correlated dimensions

      - Z & VCC can generally remain fixed and P can vary

- Classify glitch results faster (zero current vs protocol response)

- Minimize EMP charging time

   - PicoEMP: 5kHz @ 1.5% duty cycle (0.38s) or 8.7kHz @ 3.5% (0.24s)

- Parallelize operations (move while charging EMP)

- Optimize code and measure timing in logs

optimize by Kamin Ginkaew CC BY 3.0 / blue with shadow

Information Classification: General

#BHEU @BlackHatEvents

## Slide 34

## Perfecting the Glitch – Analysis

- Visual analysis is a must!

- Is an observation unambiguous?

   - Frame in the context of SoC subsystems...

      - Reset: Triggered brownout vs jumped to ISR and triggered watchdog?

- Utilize an unlocked development board

   - Unlocked behavior vs locked

   - Extract and analyze available ROM (bootloader) code

   - Prior versions of firmware unlocked or published?

analyze by Mia Elysia CC BY 3.0 / blue with shadow

Information Classification: General

#BHEU @BlackHatEvents

## Slide 35

## Perfecting the Glitch – Got Lost?

- Try a new known sensitive region

- Rescan and recalibrate when…

   - Lack of any glitch influence

   - Changing EM injector or probe tips

   - Changing or realigning targets

   - Observed anomalies

- Getting unstuck…

   - Precisely controlling variables key!

   - Is there a control or a measurement problem?

lost by Bailey CC BY 3.0 / blue with shadow

- Measure more _or_ more accurately…

Information Classification: General

#BHEU @BlackHatEvents

## Slide 36

# Attack Results

#BHEU @BlackHatEvents

## Slide 37

## The Attack – Data Analysis

Pin1 = Upper right

Main die

Flash die

Scanned area

Dot color = Current draw ACK = Successful glitch

Flash Timeout = BL no response 0x1fff01a0 = NMI

0x1fff01a2 = Hard Fault

ISRs = Other IRQs DeadBeef = Unreadable

#BHEU @BlackHatEvents

Information Classification: General

## Slide 38

## The Attack – Results?

- ~10M glitches later, we successfully bypassed the security check…

- Bus Fault upon flash read (after Memory Read Length parameter is input)

- We confirmed the flash is disabled in bootloader mode, even without SWD attached

success by Edy Subiyanto CC BY 3.0 / blue with shadow

Information Classification: General

#BHEU @BlackHatEvents

## Slide 39

## A Pivot to… The Second Attack – SRAM

- We Observed

   - SRAM contents persistent after HW reset

   - Logged some PC jumps to SRAM

- The Second Attack

   - NOP Slide + dump routine injected to SRAM via SWD

   - Reset and glitch early during reboot

chip by muhamad afiffudin CC BY 3.0 / blue with shadow

- Good data collection and a reliable, consistent rig made a pivot easy

Information Classification: General

#BHEU @BlackHatEvents

## Slide 40

## The Second Attack – Save it All!

Floppy by Vectorstall CC BY 3.0 / blue with shadow

Information Classification: General

#BHEU @BlackHatEvents

## Slide 41

## The Second Attack – Wait for it…

Information Classification: General

#BHEU @BlackHatEvents

## Slide 42

The Second Attack – Success!

[2024-06-14 06:47:50,468] g: v2.00_x3.80_y-1.40_z0.00_d7.833 B0.000+ Z0.022 P288 Vb2.01 Ib0.050 F0.648 Vc2.01 Ic0.050 J0.669- PC080052c2 LPC00000000 LLR08004285 SOK -R2.200 G4.151 C4.325 [2024-06-14 06:47:51,636] NOP Slide detected, extracting flash...

Log Key:

v = Voltage

x, y, z = Position (mm) (origin is center of chip, pin 1 upper right)

d = Delay from trigger (ms) (RST release)

P = Pulse power (ns) (time EMP switch is closed)

V[x] = Voltage at stage x

I[x] = Current at stage x

circuit hack by Hai Studio CC BY 3.0 / blue with shadow

Information Classification: General

#BHEU @BlackHatEvents

## Slide 43

## A Bonus – RDP1 Bypass

- Bypass found!

   - Boot in Flash Mode

   - Connect to device with RDP1 protections via SWD

   - Inject firmware extraction code into SRAM

   - Set PC to start of extraction code

   - Disconnect SWD

   - Execution continues and flash is extracted!

- Important to exercise mitigation edge cases!

bonus by Yosua Bungaran CC BY 3.0 / blue with shadow

- Vary sequence, timing, modes, parameters, etc

Information Classification: General

#BHEU @BlackHatEvents

## Slide 44

# Mitigations

#BHEU @BlackHatEvents

## Slide 45

## Bypass Mitigations?

- GD _may_ patch in follow-on IC tape-outs, but EM-FI mitigations are not so easy!

- Segger (J-Link) pseudo-mitigated this bypass, but don’t be fooled!

   - J-Link v7.94m (03/06/2024) introduced a _feature_ that blocks all SWD access to RDP1 locked GD devices without a forced erase!

   - • Prior J-Link applications allow bootloader code access, SRAM R/W, stepping, and execution!

   - • Appears to be implemented in the host sw, not the J-Link fw...

   - Obfuscation != Security (not cool, Segger!)

- Lesson: try old fw versions and alternate debug tools…

Information Classification: General

#BHEU @BlackHatEvents

smile by Evgeni Moryakov CC BY 3.0 / blue with shadow

## Slide 46

# Conclusions

#BHEU @BlackHatEvents

## Slide 47

Conclusions

- Fault injection is a brute force exercise, but…

- There are optimizations and methods that will save you _significant_ time

   - P, Z, VCC correlation

   - PicoEMP charge rate optimization

   - ARM fault status PC & D association

- Prepare yourself and don’t be discouraged!

hack by Sunardi CC BY 3.0 / blue with shadow

Information Classification: General

#BHEU @BlackHatEvents

## Slide 48

Sound Bytes

- The GigaDevice GD32F407 in RDP1 is vulnerable to a simple bypass

- • The GigaDevice GD32F407 in RDP1 is vulnerable to EM-FI

- EM-FI: Calibrate, Scan, Tune, Analyze, Document, Optimize, Repeat…

Sound Wave by Yayat Dayat CC BY 3.0 / blue with shadow

Information Classification: General

#BHEU @BlackHatEvents

## Slide 49

# Q&A

#BHEU @BlackHatEvents

## Slide 50

## Contact Us

- <u>Jonathan_Andersson@trendmicro.com</u>

- <u>Thanos_Kaliyanakis@trendmicro.com</u>

Information Classification: General

#BHEU @BlackHatEvents
