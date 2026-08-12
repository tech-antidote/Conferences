---
title: "Adventures of My Oven (Pinocchio) with ChipWhisperer"
speakers: ["Colin O'Flynn"]
conference: "REcon"
conference_full: "REcon 2023"
edition: ""
year: 2023
source_pdf: "REcon 2023 Slides/Colin O'Flynn_Adventures of My Oven (Pinocchio) with ChipWhisperer .pdf"
pages: 61
sha256: "bf22a1bca01a5d1bbec50ebfeed7cdddba05b93b57934c63322411372a2dd344"
text_chars: 22450
ocr_pages: 22
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:24:39Z"
---
# Adventures of My Oven (Pinocchio) with ChipWhisperer

**Speakers:** Colin O'Flynn  
**Conference:** REcon 2023  
**Source:** `REcon 2023 Slides/Colin O'Flynn_Adventures of My Oven (Pinocchio) with ChipWhisperer .pdf` (61 pages)

## Slide 1

Adventures of my Oven (Pinocchio) & ChipWhisperer

_Colin O’Flynn_

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.

1

## Slide 2

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn. 2

## Slide 3

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn. 3

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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
77 comments ©
Rodney Parsons's Thanksgiving dinner turned into disaster Fhisfall)gfter; his,dayghterclissevered acented by Colin O'Flynn
their range stove was on fire. ’
```

## Slide 4

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn. 6

## Slide 5

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn. 7

## Slide 6

# TMP91FW60

- TLCS 900/L1 CPU

- 8K RAM / 128 K flash

- Bootloader in ROM

- External xtal (no PLL)

- Obsolete…

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.

8

## Slide 7

# Bootloader

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.

9

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Bootloader
14.4.6 Data Transfer Formats
Table 14-7 to Table 14-12 show the operation command data and the data transfer format for each operation
mode.
Table 14-7 Operation Command Data
Operation Command Data Operation Mode
10H RAM Transfer
20H Flash Memory SUM
30H Product Information Read
40H Flash Memory Chip-Erase
60H Flash Memory Protect Set
RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.
```

## Slide 8

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.

10

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Table 14-8 Transfer Format of Single Boot Program [RAM Transfer]
Transfer Data
Nth Avta
DADA otarann atart nddreee 92+, 42084
June 952023. Pres|
Transfer Byte Transfer Data Baud Rate
Number from Controller to Device from Device to Controller
BOOT ROM 4st byte Baud rate setting Desired
y UART 86H baud rate*!
ACK response to baud rate setting
Normal (baud rate OK)
2nd byte - >UART. 86H
(If the desired baud rate cannot be set,
operation is terminated.)
3rd byte Operation command data (10H) -
ACK-response to operation command*2
Normal 10H
4th byte - Error x1H
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
19th byte RAM storage start addresé:31 to. 24,4.
enited by Colin O'Flynn.
10
```

## Slide 9

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.

11

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Table 14-12 Transfer Format of Single Boot Program [Flash Memory Protect Set]
Transfer Byte
Transfer Data
Transfer Data
Baud Rat
Number from Controller to Device aue nate from Device to Controller
Baud rate setting Desired
BOOT ROM 1st byt -
els | UART 86H | baud rate*!
ACK response to baud rate setting
Normal (baud rate OK)
2nd byte - >UART, 86H
(If the desired baud rate cannot be set,
operation is terminated.)
3rd byte Operation command data (60H) -
ACK-response to operation command*2
4th byte . Normal 60H
Error x1H
Communications x8H
5th byte Password data (12 bytes)
to -
16th byte (O2FEF4H to O2FEFFH)
17th byte CHECKSUM value for 5th to 16th bytes >
ACK response to checksum value*2
48th byte . Normal 60H
Error 61H
Communications 68H
ADU rAnnanann tn Deatant Cat nnmman a
RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.
14
```

## Slide 10

# Important Take-Aways (for next part)

1. Bootloader has no read-back command, only RAM program. Need to build/find 2<sup>nd</sup> stage bootloader.

2. Bootloader has TWO security protections that can be enabled:

   1. “Protection Flag” → Disables second-stage capability (leaves “erase” enabled). Disables RAM functionality, so no chance to read-back flash.

   2. 12-byte Password that can be set in Flash. Password locks RAM functionality but does not disable it.

3. Bootloader has a function that only needs password (even if protection is set).

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.

12

## Slide 11

# Programmer / Disassembler / Simulator?

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.

13

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Programmer / Disassembler / Simulator?
Toshiba BMSKTOPAS9IFY42(A) kit for flash
microcontroller TOPAS 900/L1
® Last item available
Condition: New - Open box
“New item in Good Condition”
Quantity: f | Last One /1sold
Price: US $280.00
Buy another
Se Fe
Add to cart
% Haveonetosell? Sellnow
Best Offer:
RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.
```

## Slide 12

# Windows XP?

Mirrored
Here

<u>https://github.com/ colinoflynn/ToshibaTLCS-900-LResources</u>

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.

14

## Slide 13

# Can you Read Back Bootloader?

Segger “ToshLoad” can readback bootloader (ROM) section!

Watch for how ROM remaps when in bootloader (single boot) mode.

(I made a Python version of this program so you _don’t_ need Windows XP)

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.

15

## Slide 14

```
FUNCTION START: Receive & Verify Password
00fff2a2 CALR    0x0FFF5EF <-- RX
```

```
...
00fff2ce JR      NZ,0x0FFF2D5
00fff2d0 DJNZB   C,0x0FFF2C9
```

```
00fff2d3 JR      0x0FFF2D7
```

```
00fff2d5 LDB     L,0x1 <-- L is flag, if set to 1 comparison failed
00fff2d7 LDW     BC,0x0C <-- 12 bytes to compare
```

```
00fff2da LDL     XIX,(0x0FFF00C) <-- Points to 0004FEF4 (PW)
```

```
00fff2df LDB     RH1,0x0
```

```
00fff2e2 LDB     W,(XIX+) <--Load byte into W, inc XIX ptr (loop)
00fff2e5 CALR    0x0FFF635 <--- RX assumed
```

```
00fff2e8 CPB     W,A <--Compare W & A
```

```
00fff2ea JR      Z,0x0FFF2EE <-- Compare OK, skip fail set
00fff2ec LDB     L,0x1 <--Set 'fail' flag
```

```
00fff2ee DJNZW   BC,0x0FFF2E2 <--Jump to next byte (12 times)
00fff2f1 CALR    0x0FFF67B <-- checksum
00fff2f4 RET
```

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.

16

## Slide 15

```
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
```

```
00fff30c JR      NZ,0x0FFF29C <-- Error
00fff30e CALR    0x0FFF5EF <- TX
00fff311 LDB     RH1,0x0
```

```
00fff314 CALR    0x0FFF635 <--
00fff317 LDB     QIXH,A
```

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.

17

## Slide 16

# Important Take-Aways (for next stage)

1. Password check has slight code-flow dependency.

2. Fuse byte check has obvious fault injection location.

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.

18

## Slide 17

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.

19

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Select difficulty:
Easy
Medium
——e.— um - orsrs
Hard
RECON Montreal - June 9, 2023. Presented by Colin O'Flynn. 19
```

## Slide 18

# ChipWhisperer-Husky Intro

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.

20

## Slide 19

# Power Analysis?

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.

21

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Power Analysis?
A\
Rshunt VCC
Micro-
Controller
RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.
29.4912 MHz
(7.3728 x 4)
21
```

## Slide 20

# Easy-Mode Level 1: Password Power Analysis

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.

22

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Easy-Mode Level 1: Password Power Analysis
Power Measurement for 4 Password Guesses
0.24
» 014
Cc
(oD)
=
©
=}
2 0.04
(0)
=
o
3
3-01 |
— 0x70 (p) |
_63- 0x71 (q) ul
0x72 (r) |
— 0x73 (s)
ock Cycle 16
RECON Montrse Sine 9, 20 56, M2), by Colin O'Flynn. 22
```

## Slide 21

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.

23

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Difference from Mean
Difference Between Guessed Power Trace & Mean
x *  Guessed Byte
13.44 --- Mean
, --- 4xstd+mean
13.2 5
13.0 -
12.8 -
12.6 |e
12.44 Riyal os * moe we
REAR eat
12.2 7
0 50 100 150 200 250
recByte Value, (Range 0x00,£0,0XFFdriynn.
23
```

## Slide 22

# Fault Injection?

1C9 CF FF6E 93A2

Fetch

CALRJR NZ,0xFFF290CPB A,0xFF0x F2A2
Decode

Execute

24

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.

## Slide 23

# Fault Injection?

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.

25

## Slide 24

# Clock Fault Injection

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.

26

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Clock Fault Injection
a
kK .of fset >
kK
.ext_offset— >f
Trigger event
RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.
_. -J- --tee J -
-|
\—.-width
26
```

## Slide 25

# Easy-Mode Level 2: Fault Injection Tuning

Flash memory SUM = MANY opportunities to glitch result (entire SUM operation)

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.

27

## Slide 26

# Fault Injection Setup / Demo

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.

28

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Fault Injection Setup / Demo
broken = False
for glitch_setting in gc.glitch_values():
reset_target()
scope.glitch.offset = glitch_setting[1]
scope.glitch.width = glitch_setting[0]
reset_target()
target.ser.flush()
response, responsehex = tx_rx(b"\x86", 1, 1)
if responsehex[0] != x86:
In [52]: Dl reset_target() raise I0Error("sync Error”)
response, responsehex = tx_rx(b"\x86", 1, 1) gare)
if responsehex[@] != exs6: ;
= " " #Do glitch Loop
raise I0Error("Sync Error") target. ser.write(b"\x20")
response, responsehex = tx_rx(b"\x20", 4) at co orETMT
responsehex
loff = scope.glitch.offset
out[52]: [32, 250, 165, 97] lwid = scope.glitch.width
if ret:
print('Timeout - no trigger’)
gc.add("reset")
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
print (loff)
print (lwid)
print("#@", en
else:
gc.add("normal")
Q:
print("Done glitching")
RECON Montreal - June 9, 2023. Presented by Colin O'Flynn
```

## Slide 27

# Fault Injection Results (SUM Corruption)

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.

29

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Fault Injection Results (SUM Corruption)
TMP91 Clock Glitch Settings
1300 5
hb
N
oO
Oo
n
1100 5
1000 +
900 5
800 5
Glitch Offset (CW-Husky Setting)
700 4
600 +
puis
t
ppp
t
4 T
Trt et
50 100 150 200 250 300 350
Glitch Width (CW-Husky Setting)
RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.
29
```

## Slide 28

# Easy-Mode Level 3: Fault Injection Attack

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.

30

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Easy-Mode Level 3: Fault Injection Attack
SCupe.giitcrnwiuun = 200
for glitch settings in gc.glitch_values():
scope.glitch.ext_offset = glitch_settings[0]
for i in range(sample_size):
reset_target()
target.ser.flush()
response, responsehex = tx_rx(b"\x86", 1, 1)
if responsehex[0] != 0
raise Ioerror
pcopetarm() In [59]: DL known_pw = [@xDE, @xAD, OxBE, OxEF, @xCA, OxFE, OxFA, OxCE, @x11, 0x22, x33, 0x44]
#D0 glitch Loop bl = t1.LowLevelBootloader(target.ser, reset_target, password=known_pw, reset_and_connect=False)
target ..ser.write(b"\x10") bl.cmd_ram_transfer(rc.B_F16_RAM1000_ROM10000_TLCS9@0L1["data"], rc.B_F16_RAM1000_ROM1@0@0_TLCS9@@L1["start_address"], skipcm
rl = t1.RamCodeProtocol(target.ser)
ret = scope.capture()
if ret:
print( "Timeout - no trigger’) In [60]: Dl #Print the password (should match the known one)
poadd @reset a) time.sleep(0.1)
data = rl.cmd_read(@x@2FEF4, 12)
#Device is slow to boot?
reset. target() . ":".join(hex(ord(char)) for char in data)
else “oxde: Oxad : @xbe: Oxef :Oxca:Oxfe:Oxfa:0xce:0x11:0x22:0x33:0x44"
response = target.ser.read(1)
response = [ord(i) for i in response]
In [12]: Dl #Read the U flash itself
91FW27UG in Single Boot Mode - flash is from @x10000 to 0x30000 (starts @ @x10000, Length = @x20000)
flash = rl.cmd_read(0x10000, 0x20000)
if len(response)
gc.add(“reset
else:
In [13]: DP len(flash)
if response[0]
#broken = T
gc.add ("success")
print(response)
print (hex(response[0]))
print(scope.glitch.ext_offset)
Out[13]: 131072
In [ ]: DM known_pw = [OxDE, OxAD, OxBE, OxEF, OxCA, OxFE, OxFA, OxCE, Ox11, 0x22, 0x33, 0x44]
print("#", end=
bl = tl.LowLevelBootloader(target.ser, reset_target, password=known_pw, reset_and_connect=False)
if response[0] == 0x10: b1.cmd_ram_transfer(rc.B_F16_RAM1000_ROM10000_TLCS90QL1["data"], rc.B_F16_RAM1000_ROM10000_TLCS900L1["start_address"], skipcm
broken=True rl = tl.RamcodeProtocol(target.ser)
break
else:
gc.add("normal")
if broken:
break
[16]
0x10
8015
RECON Montreal - June 9, 2023. Presented by Colin O'Flynn. 30
```

## Slide 29

# Skills & Resources

- Python class for communicating & programming TMP91 (including 2<sup>nd</sup> stage bootloader communications).

- Timing on power analysis.

- Rough timing / details on fault injection.

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.

31

## Slide 30

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.

32

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Select difficulty:
Easy
Medium
——e.— um - orsrs
Hard
RECON Montreal - June 9, 2023. Presented by Colin O'Flynn. 32
```

## Slide 31

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn. 33

## Slide 32

# Medium-Mode Level 1: Power Analysis

Sending known part of password, then do the attack on next unknown byte

s..a..m..s..u..n..g..o..v..e..n..0

34

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.

## Slide 33

# Medium-Mode Level 2: Fault Injection

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.

35

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Medium-Mode Level 2: Fault Injection
@x87
11710
#& [133]
@x85
11715
# [17]
ex11
11750
s [16]
@x10
11755
In [59]: bl #known_pw = [@xDE, @xAD, @xBE, @xEF, @xCA, @xFE, @xFA, @xCE, @x11, @x22, 0x33, Ox44]
known_pw = [ord(c) for c in "samsungovene" ]|
bl = tl.LowLevelBootloader(target.ser, reset_target, password=known_pw, reset_and_connect=False)
bl.cmd_ram_transfer(rc.B_F16_RAM1000_ROM10000_TLCS9@0L1["data"], rc.B_F16_RAM1000_ROM10000_TLCS9@@L1["“start_address"], skipcm
rl = tl.RamCodeProtocol(target.ser)
RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.
```

## Slide 34

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn. 36

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
In [11]: Dl resp = rcp.cmd_read(0x10000, 9x100)
In [12]: Dl resp
Out[12]: ‘y yy
YIVIIIIISIVIISIVY
yyyyyyyyy
yy YYYVVYYYYYYVVYYYYYIVVIYYYV IVY
YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
#bL.cmd
#bL.cmd
bl.cmd_
Read: n
Write:
RECON Montreal - June 9, 2023. Presented by Colin O'Flynn. 36
```

## Slide 35

# $$ → Samsung Parts Department

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.

37

## Slide 36

# Did they have problems with returns?

Only the password is needed on the
replacement boards!!

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.

38

## Slide 37

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.

39

## Slide 38

# EMFI POC

- R-Pi Pico implements serial protocol.

   - PicoEMP triggers an electromagnetic fault injection (EMFI).

-

   - Tested on checksum request from bootloader → successfully corrupted checksums.

-

- Code available in repo (linked later).

40

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.

## Slide 39

# Reverse Engineering Tools

41

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.

## Slide 40

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn. 42

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
File
Home
x
CO a
Paste
-
Clipboard
F9931
&
v
Column2) ~ | Column3
9926 Oxte9681 ~~ d8 12
9927 Oxfe9683
9928 Oxfe9688
9929 Oxfe968d
9930 Oxfe9691
9931 Oxfe9696
9932 Oxfe9697
9933 Oxfe969b
9934 Oxfe969d
9935 Oxfe969e
9936 Oxfe96a2
9937 Oxfe96a7
9938 Oxfe96a8
9939 Oxfe96ac
9940 Oxfe96ae
9941 Oxfe96af
9942 Oxfe96b3
9943 Oxfe96b8
9944 Oxfe96b9
9945 Oxfe96bd
9946 Oxfe96bf
9947 Oxfe96cO
9948 Oxfe96c4
9949 Oxfe96c9
9950 Oxfe96ca
9951 Oxfe96cf
9952 Oxfe96d1
9953 Oxfe96d3
9954 Oxfe96d8
9955 Oxfe96dc
9956 Oxfe96e1
9957 Oxfe96e7
< >
Ready
Insert Draw Page Layout Formulas
|Calibri jn |e xe =
BIU-y ary Ae
Font 8
i Se
[+ | Column4
EXTZW WA
f2 02 110031 LDAL XBC,0x1102
c3 07 e4e0 21 LDB A,(XBC+WA)
£10802 41 LDB (0x208),A
c2 1e 110061 INCB Ox1,(0x111E)
Oe RET
109 02 cb BITB 0x3,(0x209)
66 Ob JR Z,OxOFE96A8
00 NOP
1080221 LDB A,(0x208)
f200 110041 LDB (0x1100),A
Oe RET
f10902ca BITB 0x2,(0x209)
66 Ob JR Z,0xOFE96B9
00 NOP
10802 21 LDB  A,(0x208)
f200 110041 LDB (0x1100),A
Oe RET
f109 02 cc BITB 0x4,(0x209)
66 Ob JR Z,OxOFE96CA
00 NOP
c108 0221 LDB A,(0x208)
£200 1100 41 LDB (0x1100),A
Oe RET
c2 20110021 LDB A,(0x1120)
d9 12 EXTZW BC
f2 10 1100 32 LDAL XDE,0x1110
1080221 LDB  A,(0x208)
307 e8 e4 41 LDB (XDE+BC),A
6e 10 JR NZ,OxOFE96F9
DE92-02439F FW Disassembly
Sheet1
& Accessibility: Investigate
RE Oven.xisx ¥
£P Search
Data Review View Help Acrobat
= wr 2b, Wrap Text
Alignment
Ly | Column5
Kick off TX routine?
Serial RX Start
What is 1120??
BC has (0x1120) data
RX Byte
Load byte here?
Fail | guess?
RECON Montreal - June 9, 2023. Presented by Colin Ut
|General
[+ | Columt ~ | Columi ~ |
L]
Table Design
Number
G
Query
|
09
0
$-~%9 BS
Conditional Format as
Formatting v
&
0x1110
By
Table ~
Styles
4
Cell
Styles v
Colin O'Flynn ‘o) e@ Ff - ia) [|
| Acomments |
Insert Delete Format ~ Sort & Find & Analyze
. <i © ~ Filtery Select
Data
Cells Editing Analysis
QBITB  0x3,(0x209)
JR ZHERE
NoP
LDB A,(0x208)
LDB (0x1120),0x0
BITB Ox2,(0x209)
JR Z,HERE2
NoP
LDB A,(0x208)
LDB (0x1120),0x0
BITB 0x4,(0x209)
JR Z,HERE3
NoP
LDB
LDB
HERE
HERE2
A,(0x208)
(0x1120),0x0
LDB A,(0x1120)
LOB CA
EXTZW BC
LDAL XDE,0x1110
LDB A,(0x208)
LDB  (XDE+BC),A
CPB (0x1120),0x0C
RET ULE
LDB (0x1120),0x0
CALR OxOFE9S6F
RET ’
42°”
—& -——#—- + _ 100%
HERE3
C@ Display Settings 1332]
```

## Slide 41

# Serial Monitor Built-In!?

- Not documented anywhere I could find (service docs).

- Could be useful for repair technicians!

   - Seems to only show status of various flags however, doesn’t seem to take any input.

- We could patch it to make a simple memory-dump monitor.

43

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.

## Slide 42

DE92-02439D vs. DE92-02439F

44

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.

## Slide 43

# OK, Just Read-Out the Oven PCB

45

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
OK, Just
In [11]: Dl resp = rcp.cmd_reaq
In [12]: Dl resp
orlal: IIIIIII y SPI
rorf YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
YYYYYYYYY
In [7]; PW bl=t
#bL. cmd
#bL. cma
bl.cmd
Read:
Write:
RECON Montreal - June 9, 2023. Presented by Colin O'Flynn. 45
```

## Slide 44

# $$$ → Samsung Parts Department

46

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Samsung Parts Department
~
(uivn N3A0 XSI
eee ee, ORNL ee
RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.
```

## Slide 45

# Sidenote on Glitch Reliability

- Hitting too _early_ seems more likely to trigger erase.

- my code tends to sweep early->late.

- Can increase reliability on specific targets (oven control board), I didn’t do that as thought it was just bad luck the 1<sup>st</sup> time…

47

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.

## Slide 46

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn. 48

## Slide 47

# Have there been Firmware Fixes?

**MY OVEN (REVISION D FIRMWARE)** $ python print_status.py b'TMP91FW60   ' PW Comparison Address: 0x2fef4 RAM Start Address: 0x1000 RAM End Address: 0x2dff Read: protected Write: protected 29171

Checksums Differ!

**NEW BOARD (REVISION D)** $ python print_status.py b'TMP91FW60   ' PW Comparison Address: 0x2fef4 RAM Start Address: 0x1000 RAM End Address: 0x2dff Read: not protected

Write: not protected 29238

49

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.

## Slide 48

# ..Add the Serial Monitor

_Slight_ risk of overwriting something else important….

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.

50

## Slide 49

# Examples of Global Variables

0x1248 = Top Temp in F 0x120a = Heater “ON” Flag

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.

53

## Slide 50

# Set 375F, Cold Start, Load (Shepherds Pie)

Open oven to put shepherds pie in.

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.

55

## Slide 51

# Patched Display Logic

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.

58

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Patched Display Logic
) =
Start/set
Casserole Chicken
Nuggets
8 Hold 3 sec
Defrost Steam Sel
[ Clean Clean
Warming Custom
Cookin T
Drawer Cook 9 imer
Time On/O# Delay Start
RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.
```

## Slide 52

New Cooking/Display Logic (old-school thermostat)

if temp < setpoint:

heater(on) display(temp+11) else:

heater(off) display(temp)

_Code also stops it from going into the “maintain” temperature mode, leaves it in “preheat” mode._

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.

61

## Slide 53

# Set 375F, Cold Start, Load (Shepherds Pie)

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.

62

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Set 375F, Cold Start, Load (Shepherds Pie)
i¢) 500 1000 1500 2000
Time (sec)
RECON Montreal - June 9, 2023. Presented by Colin O'Flynn. 62
```

## Slide 54

# Soufflé Test

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.

63

## Slide 55

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn. 64

## Slide 56

<u>https://www.myrecipes.com/recipe/individual-chocolate-souffl-cakes</u>

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.

65

## Slide 57

# Known Bugs

With my patches: after the oven is plugged in for some length of time, seems it stops heating correctly. Need to power cycle at circuit breakers and will work again for a while.

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.

66

## Slide 58

# Playing with Your Own Oven

Make Display Show  Add Serial Interface  Patching Heating
Actual Temperature (Uses random RAM) Algorithm
Least
Most
Dangerous
Dangerous

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.

69

## Slide 59

# Important Design Reminder

The range elements are knob controlled (mechanical action needed).

The heating elements IN the oven are <u>100% firmware controlled</u> .

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.

70

## Slide 60

# What I learned?

- Might not be your fault having trouble with receipies & cooking time.

- Many ovens _actively lie to you_ to hide their issues.

- <u>Lots of wasted electronic waste generated from this problem (at</u> minimum parts, at worst full ovens).

- Just reflashing boards should be a repair item (but isn’t).

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.

71

## Slide 61

# Questions? Details?

<u>https://github.com/colinoflynn/samsung-ovens-deconstructed https://github.com/colinoflynn/Toshiba-TLCS-900-L-Resources</u>

General overview at blog post on: <u>https://www.oflynn.com</u>

colinoflynn@bluenoser.me Hellsite: @colinoflynn

RECON Montreal - June 9, 2023. Presented by Colin O'Flynn.

72
