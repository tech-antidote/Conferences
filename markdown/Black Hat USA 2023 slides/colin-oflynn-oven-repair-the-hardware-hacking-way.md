---
title: "Oven Repair (The Hardware Hacking Way)"
speakers: ["Colin O'Flynn"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/Colin O'Flynn_Oven Repair (The Hardware Hacking Way).pdf"
pages: 74
sha256: "a27638ca1592b71cf1b69ec50732370999958854113ab5253e99800bfef1e16d"
text_chars: 23369
ocr_pages: 24
has_ocr: true
redacted_secrets: 0
ocr_confidence: 87.3
ocr_unreliable_blocks: 0
vision_verified_blocks: 2
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:07:58Z"
---
# Oven Repair (The Hardware Hacking Way)

**Speakers:** Colin O'Flynn  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Colin O'Flynn_Oven Repair (The Hardware Hacking Way).pdf` (74 pages)


## Slide 1

# Oven Repair The Hardware Hacking Way

Speaker: Colin O’Flynn

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
AUGUST 9-10, 2023
BRIEFINGS
Oven Repai
The Hardware Hacking
Speaker: Colin O’Flynn
#BHUSA @BlackHatEvents
```

## Slide 2

Black Hat USA - August 10, 2023. Colin O'Flynn. 2

## Slide 3

### About Me

- Co-author of _Hardware Hacking Handbook_

- • Started _ChipWhisperer_ project & related company (NewAE Technology), now part of lowRISC CIC

• Adjunct professor at Dalhousie University

- Lives in Halifax, NS, Canada

#BHUSA @BlackHatEvents

## Slide 4

4

Black Hat USA - August 10, 2023. Colin O'Flynn.


> Recovered by OCR — confidence 91/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Nova Scotia
This Halifax-area man's oven caught fire while
making turkey dinner
Technician determined the stove's relay switch malfunctioned on 5-year-old range
Company embroiled in lawsuit
Samsung is the subject of a class action lawsuit filed in December 2020 in New Jersey pertaining
to 87 Samsung stoves, including Parsons's model.
The lawsuit alleges that a defect in the oven temperature sensor causes failures in the
range's control boards.
"When the control boards fail, the [range's] oven and burner temperatures deviate from the
user-selected temperature settings," the document said.
77 comments —
Rodney Parsons's Thanksgiving dinner turned into disaster this Faiatter bis dagahtar discqvertco23 Colin O'Flynn
their range stove was on fire. ’
```

## Slide 5

## Wasted $$, Wasted Resources

https://www.applianceblog.com/mainforums/threads/samsung-fer300sx-will-not-maintain-temperature.68145/

Black Hat USA - August 10, 2023. Colin O'Flynn.

5

## Slide 6

## PID Controller?

Black Hat USA - August 10, 2023. Colin O'Flynn.

6


> Recovered by OCR — confidence 89/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
PID Controller?
704 — Temperature (i=0.01)
Temperature (i=1.1)
60-4 — Setpoint
50 7
+ Process
~ 30
207
1074
Time
Black Hat USA - August 10, 2023. Colin O'Flynn. 6
```

## Slide 7

Black Hat USA - August 10, 2023. Colin O'Flynn. 7

## Slide 8

Black Hat USA - August 10, 2023. Colin O'Flynn. 8

## Slide 9

## TMP91FW60

- TLCS 900/L1 CPU

- 8K RAM / 128 K flash

- Bootloader in ROM

- External xtal (no PLL)

- Obsolete…

Black Hat USA - August 10, 2023. Colin O'Flynn.

9

## Slide 10

## Bootloader

Black Hat USA - August 10, 2023. Colin O'Flynn.

10


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Bootloader
14.4.6 Data Transfer Formats
Table 14-7 to Table 14-12 show the operation command data and the data transfer format for each operation
mode.
Table 14-7 Operation Command Data
Operation Command Data
Operation Mode
10H RAM Transfer
20H Flash Memory SUM
30H Product Information Read
40H Flash Memory Chip-Erase
60H Flash Memory Protect Set
10
```

## Slide 11

Black Hat USA - August 10, 2023. Colin O'Flynn.

11


> Recovered by OCR — confidence 88/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Table 14-8 Transfer Format of Single Boot Program [RAM Transfer]
Transfer Byte
Transfer Data
Transfer Data
Baud Rat .
Number from Controller to Device ane nane from Device to Controller
BOOT ROM 4st byte Baud rate setting Desired
y UART 86H baud rate*!
ACK response to baud rate setting
Normal (baud rate OK)
2nd byte - >UART 86H
(If the desired baud rate cannot be set,
operation is terminated.)
3rd byte Operation command data (10H) -
ACK-response to operation command*2
Normal 10H
4th byte - Error x14
Protection applied*? x6H
Communications error x8H
5th byte PASSWORD data (12 bytes)
to -
16th byte (O2FEF4H to O2FEFFH)
17th byte CHECKSUM value for 5th to 16th bytes -
AGK response to CHECKSUM value#2
18th byte . Normal 10H
Error 11H
Communications error 18H
#4
19th byte RAM storage start addres8.3319-24/73+ SA - AuBust40, 2093.) Cblin O'Flynn.
14
```

## Slide 12

Black Hat USA - August 10, 2023. Colin O'Flynn.

12


> Recovered by OCR — confidence 88/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Table 14-12 Transfer Format of Single Boot Program [Flash Memory Protect Set]
Transfer Byte
Transfer Data
Transfer Data
Baud Rat
Number from Controller to Device aua ate from Device to Controller
Baud rate setting Desired
BOOT ROM 1st byt -
stewie UART 86H baud rate"!
ACK response to baud rate setting
Normal (baud rate OK)
2nd byte - >UART, 86H
(If the desired baud rate cannot be set,
operation is terminated.)
3rd byte Operation command data (60H) -
ACK-response to operation command*#2
4th byte . Normal 60H
Error x1H
Communications x8H
5th byte Password data (12 bytes)
16th byte (O2FEF4H to O2FEFFH)
17th byte CHECKSUM value for 5th to 16th bytes >
ACK response to checksum value*2
48th byte . Normal 60H
Error 61H
Communications 68H
ADU rAnnannn tn Deatant Cat nnmman a
12
```

## Slide 13

## Important Take-Aways (for next part)

1. Bootloader has no read-back command, only RAM program. Need to build/find 2<sup>nd</sup> stage bootloader.

2. Bootloader has TWO security protections that can be enabled: 1. “Protection Flag”  Disables second-stage capability (leaves “erase” enabled). Disables RAM functionality, so no chance to read-back flash.

2. 12-byte Password that can be set in Flash. Password locks RAM functionality but does not disable it.

3. Bootloader has a function that only needs password (even if protection is set).

Black Hat USA - August 10, 2023. Colin O'Flynn.

13

## Slide 14

## Programmer / Disassembler / Simulator?

14

Black Hat USA - August 10, 2023. Colin O'Flynn.


> Recovered by OCR — confidence 90/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Programmer / Disassembler / Simulator?
Toshiba BMSKTOPAS9IFY42(A) kit for flash
microcontroller TOPAS 900/L1
® Last item available
Condition: New - Open box
“New item in Good Condition”
Quantity: t | Last One /1sold
Price: US $280.00
Buy another
Add to cart
Best Offer:
```

## Slide 15

## Windows XP?

Mirrored
Here

<u>https://github.com/ colinoflynn/ToshibaTLCS-900-LResources</u>

Black Hat USA - August 10, 2023. Colin O'Flynn.

15

## Slide 16

## Can you Read Back Bootloader?

Segger “ToshLoad” can readback bootloader (ROM) section!

Watch for how ROM remaps when in bootloader (single boot) mode.

(I made a Python version of this program so you _don’t_ need Windows XP)

Black Hat USA - August 10, 2023. Colin O'Flynn.

16

## Slide 17

\```
FUNCTION START: Receive & Verify Password
00fff2a2 CALR    0x0FFF5EF <-- RX
\```

\```
...
00fff2ce JR      NZ,0x0FFF2D5
00fff2d0 DJNZB   C,0x0FFF2C9
00fff2d3 JR      0x0FFF2D7
\```

\```
00fff2d5 LDB     L,0x1 <-- L is flag, if set to 1 comparison failed
00fff2d7 LDW     BC,0x0C <-- 12 bytes to compare
\```

\```
00fff2da LDL     XIX,(0x0FFF00C) <-- Points to 0004FEF4 (PW)
00fff2df LDB     RH1,0x0
\```

\```
00fff2e2 LDB     W,(XIX+) <--Load byte into W, inc XIX ptr (loop)
00fff2e5 CALR    0x0FFF635 <--- RX assumed
\```

\```
00fff2e8 CPB     W,A <--Compare W & A
\```

\```
00fff2ea JR      Z,0x0FFF2EE <-- Compare OK, skip fail set
00fff2ec LDB     L,0x1 <--Set 'fail' flag
00fff2ee DJNZW   BC,0x0FFF2E2 <--Jump to next byte (12 times)
00fff2f1 CALR    0x0FFF67B <-- checksum
00fff2f4 RET
\```

Black Hat USA - August 10, 2023. Colin O'Flynn.

17

## Slide 18

\```
FUNCTION START: RAM WRITE FUNCTION
00fff2f5 CALR    0x0FFF75F  <-- Load protection status
00fff2f8 CPB     A,0x0FF <-- Compare protection status
00fff2fb JR      NZ,0x0FFF290 <-- Send error if protection enabled
00fff2fd CALR    0x0FFF2A2 <-- PW Check
00fff300 CPB     RE1,0x0
00fff303 JR      NZ,0x0FFF28A
00fff305 CPB     RL1,0x0
00fff308 JR      NZ,0x0FFF29C <-- Error
00fff30a CPB     L,0x0
00fff30c JR      NZ,0x0FFF29C <-- Error
00fff30e CALR    0x0FFF5EF <- TX
00fff311 LDB     RH1,0x0
00fff314 CALR    0x0FFF635 <--
00fff317 LDB     QIXH,A
\```

Black Hat USA - August 10, 2023. Colin O'Flynn.

18

## Slide 19

## Important Take-Aways (for next stage)

1. Password check has slight code-flow dependency.

2. Fuse byte check has obvious fault injection location.

Black Hat USA - August 10, 2023. Colin O'Flynn.

19

## Slide 20

Black Hat USA - August 10, 2023. Colin O'Flynn.

20


> Recovered by OCR — confidence 94/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Select difficulty:
Easy
Hard
20
```

## Slide 21

## ChipWhisperer-Husky Intro

Black Hat USA - August 10, 2023. Colin O'Flynn.

21

## Slide 22

## Power Analysis?

Black Hat USA - August 10, 2023. Colin O'Flynn.

22


> Recovered by OCR — confidence 85/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Power Analysis?
Rshunt VCC
Micro-
Controller
29.4912 MHz
(
(
(
( |
GND "7.3728 MHz
' (7.3728 x 4)
—_ oe
Black Hat USA - August 10, 2023. Colin O'Flynn. 22
```

## Slide 23

## Easy-Mode Level 1: Password Power Analysis

Black Hat USA - August 10, 2023. Colin O'Flynn.

23


> Recovered by OCR — confidence 87/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Easy-Mode Level 1: Password Power Analysis
Power Measurement for 4 Password Guesses
0.24
p O17
o
o
=
=
3-01 |
—— 0x70 (p)
-0.24 0x71 (q)
0x72 (r)
Clock Cycle (@ 16 MHz) .
Black Hat USA - August TO, 2023. Colin O'Flynn. 23
```

## Slide 24

24

Black Hat USA - August 10, 2023. Colin O'Flynn.


> Recovered by OCR — confidence 83/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Difference from Mean
Difference Between Guessed Power Trace & Mean
Xx x Guessed Byte
13.4- --- Mean
13.2 5
13.0 5
12.8 5
12.2 4
0 50 100 150 200 250
Byte. Value (Range 0x00 to, OxFR)
24
```

## Slide 25

## Fault Injection?

1C9 CF FF6E A293

Fetch

CALRCPB A,0xFFJR NZ,0xFFF2900x F2A2
Decode

Execute

Black Hat USA - August 10, 2023. Colin O'Flynn.

25

## Slide 26

## Fault Injection?

Black Hat USA - August 10, 2023. Colin O'Flynn.

26

## Slide 27

## Clock Fault Injection

Black Hat USA - August 10, 2023. Colin O'Flynn.

27

## Slide 28

## Easy-Mode Level 2: Fault Injection Tuning

Flash memory SUM = MANY opportunities to glitch result (entire SUM operation)

Black Hat USA - August 10, 2023. Colin O'Flynn.

28

## Slide 29

## Fault Injection Setup / Demo

Black Hat USA - August 10, 2023. Colin O'Flynn.

29


> Recovered by OCR — confidence 89/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Fault Injection Setup / Demo
In [52]: Pl reset_target()
Out[52]:
response, responsehex
tx_rx(b"\x86", 1, 1)
if responsehex[@] != exs6:
raise I0Error("Sync Error")
response, responsehex
responsehex
[32, 250, 165, 97]
tx_rx(b"\x20", 4)
broken = False
for glitch_setting in gc.glitch_values():
reset_target()
scope.glitch.offset = glitch_setting[1]
scope.glitch.width = glitch_setting[0]
reset_target()
target.ser.flush()
response, responsehex = tx_rx(b"\x86", 1, 1)
if responsehex[0] != 0x86
raise I0Error("Sync Error”)
scope.arm()
#00 glitch Loop
target.ser.write(b"\x20")
ret = scope.capture()
loff = scope.glitch.offset
lwid = scope.glitch.width
if ret:
print('Timeout - no trigger’)
#Device is slow to boot?
reset_target()
else:
response = target.ser.read(4)
response = [ord(i) for i in response]
if len(response)
gc.add("reset")
else:
if response != [32, 250, 165, 97]:
broken = True
gc.add("success")
print (response)
print(”"#@", en
else:
gc.add("normal")
29
```

## Slide 30

## Fault Injection Results (SUM Corruption)

Black Hat USA - August 10, 2023. Colin O'Flynn.

30


> Recovered by OCR — confidence 90/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Fault Injection Results (SUM Corruption)
TMP91 Clock Glitch Settings
1300 4
> 1200 4
£
1100 4
F 1000 +
5 8004 E HF
+
50 100 150 200 250 300 350
Glitch Width (CW-Husky Setting)
30
```

## Slide 31

## Easy-Mode Level 3: Fault Injection Attack

Black Hat USA - August 10, 2023. Colin O'Flynn.

31


> Recovered by OCR — confidence 85/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Easy-Mode Level 3: Fault Injection Attack
for glitch_settings in gc.glitch_values():
scope.glitch.ext_offset = glitch_settings[o]
for i in range(sample_size):
reset_target()
response, responsehex
if responsehex[0] !
raise IoError("sync Error")
scope.arm()
400 glitch Loop
target.ser.write(b"\x10")
ret = scope.capture()
if ret:
print('Timeout - no trigger’)
#Device
s slow to boot
reset_target()
else:
response
response
= target.ser.read(1)
= [ord(i) for i in response]
if len(response)
gc.add(“reset")
else:
if response[o]
#broken = Tru
gc.add("success")
print(hex(response[0]))
if response[0] =
broken=True
break
#break
else:
gc.add("normal")
if broken:
break
[16]
0x10
8015
In [59]:
In [60]:
In [12]:
In [13]:
known_pw = [@XDE, OxAD, @xBE, OxEF, OxCA, OxFE, OxFA, @xCE, Ox11, 0x22, 0x33, 0x44]
bl = t1.LowLevelBootloader(target.ser, reset_target, password=known_pw, reset_and_connect=False)
rl = tl.RamCodeProtocol (target. ser)
#Print the password (should match the known one)
data = rl.cmd_read(@x@2FEF4, 12)
":"join(hex(ord(char)) for char in data)
#Read the full flash itself
91FW27UG in Single Boot Mode - flash is from @x10000 to 0x30000 (starts @ @x10000, Length = @x20000)
flash = rl.cmd_read(0x10000, 0x20000)
131072
known_pw =
bl = tl.LowLevelBootloader(target.ser, reset_target, password=known_pw, reset_and_connect=False)
rl = tl.RamCodeProtocol (target .ser)
31
```

## Slide 32

## Skills & Resources

- Python class for communicating & programming TMP91 (including 2<sup>nd</sup> stage bootloader communications).

- Timing on power analysis.

- Rough timing / details on fault injection.

Black Hat USA - August 10, 2023. Colin O'Flynn.

32

## Slide 33

Black Hat USA - August 10, 2023. Colin O'Flynn.

33


> Recovered by OCR — confidence 94/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Select difficulty:
Easy
Hard
33
```

## Slide 34

Black Hat USA - August 10, 2023. Colin O'Flynn. 34


> Recovered by OCR — confidence 83/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
20-Pin
Target B.
ik Hat USA - August 10, 2023.
13
© CW312 Sty)
Colin O'Flynn.
34
```

## Slide 35

## Medium-Mode Level 1: Power Analysis

Sending known part of password, then do the attack on next unknown byte

s..a..m..s..u..n..g..o..v..e..n..0

Black Hat USA - August 10, 2023. Colin O'Flynn.

35

## Slide 36

## Medium-Mode Level 2: Fault Injection

Black Hat USA - August 10, 2023. Colin O'Flynn.

36


> Recovered by OCR — confidence 84/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Medium-Mode Level 2: Fault Injection
11710
@x85
11715
11750
r [16]
0x10
11755
In [59]: bl #known_pw = [@xDE, @xAD, OxBE, OxEF, @xCA, @xFE, @xFA, @xCE, @x11, x22, 0x33, Ox44]
known_pw = [ord(c) for c in “samsungovene"
bl = tl.LowLevelBootloader(target.ser, reset_target, password=known_pw, reset_and_connect=False)
rl = tl.RamCodeProtocol(target.ser)
Black Hat USA - August 10, 2023. Colin O'Flynn
```

## Slide 37

Black Hat USA - August 10, 2023. Colin O'Flynn.

37


> Recovered by OCR — confidence 85/100 on the text kept, 60/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
In [11]: Dl resp = rcp.cmd_read(0x10000, 9x100)
In [12]: DP resp
yyyyyyyyy
#bL.cmd
#bL.cmd
bl.cmd_
Read: n
Write:
Black Hat USA - August 10, 2023. Colin O'Flynn. 37
```

## Slide 38

## $$  Samsung Parts Department

Black Hat USA - August 10, 2023. Colin O'Flynn.

38

## Slide 39

## Did they have problems with returns?

Only the password is needed on the
replacement boards!!

Black Hat USA - August 10, 2023. Colin O'Flynn.

39

## Slide 40

40

Black Hat USA - August 10, 2023. Colin O'Flynn.

## Slide 41

## EMFI POC

- R-Pi Pico implements serial protocol.

   - PicoEMP triggers an electromagnetic fault injection (EMFI).

-

- Tested on checksum request from bootloader  successfully corrupted checksums.

- Code available in repo (linked later).

41

Black Hat USA - August 10, 2023. Colin O'Flynn.

## Slide 42

## Sidenote: PicoEMP is Open Source!

CC-BA-SA 3.0 License!

Remix (but share per CC-BY-SA 3.0)

42

Black Hat USA - August 10, 2023. Colin O'Flynn.

## Slide 43

## Reverse Engineering Tools

43

Black Hat USA - August 10, 2023. Colin O'Flynn.

## Slide 44

Black Hat USA - August 10, 2023. Colin O'Flynn. 44


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 72/100 on the text kept, 64/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
grep -nrbai "API Username and Password" OSX/Test_ready_lldb/OSX-KVM/ -A 10
mac_hdd_ng.img:5920941:1337630732:#API Username and Password
mac_hdd_ng.img-5920942-1337630759-username="service_api_[obscured]
mac_hdd_ng.img-5920943-1337630790-password="[obscured]
mac_hdd_ng.img-5920944-1337630828-url="https://[obscured]
mac_hdd_ng.img-5920945-1337630862-loggedInUser=$( scutil <<< "show State:/Users/ConsoleUser" | awk '/Name :/ && ! /loginwindow/ { print $3 }' )
mac_hdd_ng.img-5920946-1337630972-echo $loggedInUser
mac_hdd_ng.img-5920947-1337630991-
mac_hdd_ng.img-5920948-1337630992-#Variable declarations
mac_hdd_ng.img-5920949-1337631015-bearerToken=""
mac_hdd_ng.img-5920950-1337631030-tokenExpirationEpoch="0"
mac_hdd_ng.img-5920951-1337631055-aduser="[obscured]
```

## Slide 45

## Serial Monitor Built-In!?

- Not documented anywhere I could find (service docs).

- Could be useful for repair technicians!

   - Seems to only show status of various flags however, doesn’t seem to take any input.

- We could patch it to make a simple memory-dump monitor.

45

Black Hat USA - August 10, 2023. Colin O'Flynn.

## Slide 46

DE92-02439D vs. DE92-02439F

46

Black Hat USA - August 10, 2023. Colin O'Flynn.

## Slide 47

## OK, Just Read-Out the Oven PCB

47

Black Hat USA - August 10, 2023. Colin O'Flynn.


> Recovered by OCR — confidence 85/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
OK, Just
In [11]: Dl resp = rcp.cmd_read
In [12]: DP resp
Out[12]: ‘y
In [7]; PW bl=t
bl.cmd
Read:
Write:
47
```

## Slide 48

## $$$  Samsung Parts Department

48

Black Hat USA - August 10, 2023. Colin O'Flynn.

## Slide 49

## Sidenote on Glitch Reliability

- Hitting too _early_ seems more likely to trigger erase.

- my code tends to sweep early->late.

- Can increase reliability on specific targets (oven control board), I didn’t do that as thought it was just bad luck the 1<sup>st</sup> time…

49

Black Hat USA - August 10, 2023. Colin O'Flynn.

## Slide 50

Black Hat USA - August 10, 2023. Colin O'Flynn. 50

## Slide 51

## Have there been Firmware Fixes?

**MY OVEN (REVISION D FIRMWARE)**

$ python print_status.py b'TMP91FW60   ' PW Comparison Address: 0x2fef4 RAM Start Address: 0x1000 RAM End Address: 0x2dff Read: protected Write: protected 29171

Checksums Differ!

**NEW BOARD (REVISION D)** $ python print_status.py b'TMP91FW60   ' PW Comparison Address: 0x2fef4 RAM Start Address: 0x1000 RAM End Address: 0x2dff Read: not protected

Write: not protected 29238

Black Hat USA - August 10, 2023. Colin O'Flynn.

51

## Slide 52

## ..Add the Serial Monitor

_Slight_ risk of overwriting something else important….

Black Hat USA - August 10, 2023. Colin O'Flynn.

52


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 82/100 on the text kept, 71/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
QuickSniff - 1st Tool

Hooking Quick Share to sniff
sent and received Offline
Frames on Windows

initiator_to_responder:
v1:
  payloadTransfer:
    packetType: DATA
    payloadChunk:
      body:
        v1:
          introduction:
            fileMetadata:
            - id: '585290039179534374'
              mimeType: image/png
              name: TFMyMDI0MDYxMzEzMzM1Ni5wbmc=
              payloadId: '-8969229381597391197'
              size: '622679'
              type: IMAGE
          type: INTRODUCTION
        version: V1
      flags: 0
      index: 0
      offset: '0'
    payloadHeader:
      id: '-5778571142958742193'
      isSensitive: false
      totalSize: '85'
      type: BYTES
  type: PAYLOAD_TRANSFER
version: V1
```

## Slide 53

## “Production” Serial Interface

Black Hat USA - August 10, 2023. Colin O'Flynn.

53

## Slide 54

## R.E. Data Storage Locations

Can find data blocks from R.E. work. Then find changing data as you do different things (start/stop oven, change temp, etc).

54

Black Hat USA - August 10, 2023. Colin O'Flynn.

## Slide 55

## Examples of Global Variables

0x1248 = Top Temp in F 0x120a = Heater “ON” Flag

Black Hat USA - August 10, 2023. Colin O'Flynn.

55


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Examples of Global Variables
Ox1248 = Top Temp in F
Ox120a = Heater “ON” Flag |
0.45
0.275
0.05
T T
0 200
T
400
T
600
T
800
T
1000
55
```

## Slide 56

## Set 375F, Cold Start, No Load

Oven starts reading real
Short pulses to maintain temp (spikes
temp (which is higher)
down are when heater is on)
Element turns off.
When heating element
turns ON, measured
temp drops.

Black Hat USA - August 10, 2023. Colin O'Flynn.

56

## Slide 57

## Set 375F, Cold Start, Load (Shepherds Pie)

##### Open oven to put shepherds pie in.

Black Hat USA - August 10, 2023. Colin O'Flynn.

57

## Slide 58

Observed Display Logic During Pre-Heat if temp < 150F:

display(150F) elif temp < old_temp: display(old_temp) else:

display(temp) old_temp = temp

Black Hat USA - August 10, 2023. Colin O'Flynn.

58

## Slide 59

## Observed Display Logic During Cooking

display(set_temp)

Black Hat USA - August 10, 2023. Colin O'Flynn.

59

## Slide 60

## Patched Display Logic

Black Hat USA - August 10, 2023. Colin O'Flynn.

60


> Recovered by OCR — confidence 83/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Patched Display Logic
Bake Roast
Start/set
Casserole Naggets ~ 4 B Hold 3 sec
Warming Custom Cooking Timer
Drawer Cook Time On/o Delay Start
```

## Slide 61

## Best Guess for Display Logic Design?

- Confusing for customers if temperature drops suddenly when heater is on.

   - Easier to lie to customers & show the max temp.

- Don’t want customers to worry about “peaking”

   - Switch to “maintain” mode once temp > set_temp, after that only show set_temp. Customer feels like they see preheat working, now they “see” oven working. Happy Customer!

Black Hat USA - August 10, 2023. Colin O'Flynn.

61

## Slide 62

## Burning Cookies

Known work-around for these ovens is to stop & restart them.

- This shows you the “true” temperature again.

- This puts them back into “pre-heat” mode where they have enough power.

• If you are lucky it now can stabilize around the right temperature. PROBLEM: The “peak” tends to still happen -> can burn items in the oven! This was also observed in practice…

Black Hat USA - August 10, 2023. Colin O'Flynn.

62

## Slide 63

New Cooking/Display Logic (old-school thermostat)

if temp < setpoint:

heater(on) display(temp+11)

else:

heater(off) display(temp)

_Code also stops it from going into the “maintain” temperature mode, leaves it in “preheat” mode._

Black Hat USA - August 10, 2023. Colin O'Flynn.

63

## Slide 64

## Set 375F, Cold Start, Load (Shepherds Pie)

64

Black Hat USA - August 10, 2023. Colin O'Flynn.


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Set 375F, Cold Start, Load (Shepherds Pie)
it) 500 1000 1500 2000
Time (sec)
Black Hat USA - August 10, 2023. Colin O'Flynn. 64
```

## Slide 65

## Soufflé Test

Black Hat USA - August 10, 2023. Colin O'Flynn.

65

## Slide 66

Black Hat USA - August 10, 2023. Colin O'Flynn. 66

## Slide 67

<u>https://www.myrecipes.com/recipe/individual-chocolate-souffl-cakes</u>

Black Hat USA - August 10, 2023. Colin O'Flynn.

67

## Slide 68

## Known Bugs

With my patches: after the oven is plugged in for some length of time, seems it stops heating correctly. Need to power cycle at circuit breakers and will work again for a while.

Black Hat USA - August 10, 2023. Colin O'Flynn.

68

## Slide 69

## Future Work

#### DE92-03960J Controller Board:

- “Newer” ovens based on R5F100LEAFB#V0 (RL78/G13)

- No protection (can read-out with debugger)

- Supported Ghidra plugin!

Black Hat USA - August 10, 2023. Colin O'Flynn.

69

## Slide 70

## Playing with Your Own Oven

- Confirm it’s correct version using TMP91 (not newer board)

- Need serial interface cable, if running in-place need 5V compatible + isolated due to mains input (suggest _μArt_ , https://uart- <u>adapter.com/)</u>

- Script in repo can check status of oven (if write protection enabled).

   - If no write protection, need only known password.

   - If write protection enabled, need firmware image first OR glitch.

- Feel free to try some fixes (at your own risk)

Black Hat USA - August 10, 2023. Colin O'Flynn.

70

## Slide 71

## Playing with Your Own Oven

Make Display Show  Add Serial Interface  Patching Heating
Actual Temperature (Uses random RAM) Algorithm
Least
Most
Dangerous
Dangerous

Black Hat USA - August 10, 2023. Colin O'Flynn.

71

## Slide 72

## Important Design Reminder

The range elements are knob controlled (mechanical action needed).

The heating elements IN the oven are <u>100% firmware controlled .</u>

Black Hat USA - August 10, 2023. Colin O'Flynn.

72

## Slide 73

## What I learned?

- Might not be your fault having trouble with receipies & cooking time.

- Many ovens _actively lie to you_ to hide their issues.

- <u>Lots</u> of wasted electronic waste generated from this problem (at minimum parts, at worst full ovens).

- Just reflashing boards should be a repair item (but isn’t).

Black Hat USA - August 10, 2023. Colin O'Flynn.

73

## Slide 74

Questions? Details? <u>https://github.com/colinoflynn/samsung-ovens-deconstructed https://github.com/colinoflynn/Toshiba-TLCS-900-L-Resources</u>

General overview at blog post on: <u>https://www.oflynn.com</u> @colinoflynn.bsky.social colinoflynn@bluenoser.me

Book
Signing!
TODAY @
11AM!

74

Black Hat USA - August 10, 2023. Colin O'Flynn.
