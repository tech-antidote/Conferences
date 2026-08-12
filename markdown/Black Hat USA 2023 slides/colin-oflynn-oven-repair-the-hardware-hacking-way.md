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
text_chars: 27248
ocr_pages: 28
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:15:24Z"
---
# Oven Repair (The Hardware Hacking Way)

**Speakers:** Colin O'Flynn  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Colin O'Flynn_Oven Repair (The Hardware Hacking Way).pdf` (74 pages)


## Slide 1

# Oven Repair The Hardware Hacking Way

Speaker: Colin O’Flynn

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
plack hat
ISA 2PO0es3
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Nova Scotia
This Halifax-area man's oven caught fire while
making turkey dinner
f) vom S&S (in
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
PID Controller?
704 — Temperature (i=0.01)
Temperature (i=1.1)
60-4 — Setpoint
50 7
r(t) y e(t) Plant; PX 404
+ Process
~ 30
207
1074
o- T T T T T T
a) 20 40 60 80 100
Time
Black Hat USA - August 10, 2023. Colin O'Flynn. 6
```

## Slide 7

Black Hat USA - August 10, 2023. Colin O'Flynn. 7

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
VEN MAINS
® 2012
OF a
3 6g DESL 12439
P
z iin
DE41-00408C n |
Fe : i
es 5 ce 3
‘ii [3
<
=
_
a
(2)
4
Oo
(S)
ee)
N
ro}
N
fo)
4
```

## Slide 8

Black Hat USA - August 10, 2023. Colin O'Flynn. 8

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
aLieese)
puedes
<
Cc
>
uw
fo)
£
ze)
o)
00)
A
ro)
A
S
a
w
n
=)
oo
_)
a
<x
70)
=)
Z
ise)
=
x<
oO
&
iva]
```

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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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
Black Hat USA - August 10, 2023. Colin O'Flynn.
10
```

## Slide 11

Black Hat USA - August 10, 2023. Colin O'Flynn.

11

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Table 14-8 Transfer Format of Single Boot Program [RAM Transfer]
Transfer Byte
Transfer Data
Transfer Data
Nth hvta
DANA cetarancs otart ndedirnce 92 +- 1084
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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
to “
16th byte (O2FEF4H to O2FEFFH)
17th byte CHECKSUM value for 5th to 16th bytes >
ACK response to checksum value*2
48th byte . Normal 60H
Error 61H
Communications 68H
ADU rAnnannn tn Deatant Cat nnmman a
Black Hat USA - August 10, 2023. Colin O'Flynn.
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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
< Sie Fe
Add to cart
§% Have onetosell? Sell now
Best Offer:
Black Hat USA - August 10, 2023. Colin O'Flynn.
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

```
FUNCTION START: Receive & Verify Password
00fff2a2 CALR    0x0FFF5EF <-- RX
```

```
...
00fff2ce JR      NZ,0x0FFF2D5
00fff2d0 DJNZB   C,0x0FFF2C9
00fff2d3 JR      0x0FFF2D7
```

```
00fff2d5 LDB     L,0x1 <-- L is flag, if set to 1 comparison failed
00fff2d7 LDW     BC,0x0C <-- 12 bytes to compare
```

```
00fff2da LDL     XIX,(0x0FFF00C) <-- Points to 0004FEF4 (PW)
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
00fff2ee DJNZW   BC,0x0FFF2E2 <--Jump to next byte (12 times)
00fff2f1 CALR    0x0FFF67B <-- checksum
00fff2f4 RET
```

Black Hat USA - August 10, 2023. Colin O'Flynn.

17

## Slide 18

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
00fff30c JR      NZ,0x0FFF29C <-- Error
00fff30e CALR    0x0FFF5EF <- TX
00fff311 LDB     RH1,0x0
00fff314 CALR    0x0FFF635 <--
00fff317 LDB     QIXH,A
```

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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Select difficulty:
Easy
ye Pore | 7
Medium
Hard
Black Hat USA - August 10, 2023. Colin O'Flynn.
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Power Analysis?
~_= rr — ——
-
Rshunt VCC
Micro-
l ia
Controller
29.4912 MHz
(
(
(
( |
GND "7.3728 MHz
' (7.3728 x 4)
— - — => — - =-
—_ oe
Black Hat USA - August 10, 2023. Colin O'Flynn. 22
```

## Slide 23

## Easy-Mode Level 1: Password Power Analysis

Black Hat USA - August 10, 2023. Colin O'Flynn.

23

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Easy-Mode Level 1: Password Power Analysis
Power Measurement for 4 Password Guesses
0.24
p O17
Cc
o
€
v
a
4“ 0.0 5
o
=
o
=
3-01 |
—— 0x70 (p)
-0.24 0x71 (q)
0x72 (r)
— 0x73 (s)
0 20 40 60 80 100 120 140
Clock Cycle (@ 16 MHz) .
Black Hat USA - August TO, 2023. Colin O'Flynn. 23
```

## Slide 24

24

Black Hat USA - August 10, 2023. Colin O'Flynn.

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Difference from Mean
Difference Between Guessed Power Trace & Mean
Xx x  Guessed Byte
13.4- --- Mean
; --- Axstd+mean
13.2 5
13.0 5
12.8 5
12.6 |e
Sx
xX oa x os x x x Xx
12.4 4 ve > 4 rah Oe
x x me ee
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Clock Fault Injection
kK .of fset >
oT
Lf .-- Lu j---+eJ- -bLIt -
kK .ext_offset— sf —| |—.-width
Trigger event
```

## Slide 28

## Easy-Mode Level 2: Fault Injection Tuning

Flash memory SUM = MANY opportunities to glitch result (entire SUM operation)

Black Hat USA - August 10, 2023. Colin O'Flynn.

28

## Slide 29

## Fault Injection Setup / Demo

Black Hat USA - August 10, 2023. Colin O'Flynn.

29

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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
print(”"#@", en
else:
gc.add("normal")
print("Done glitching")
Black Hat USA - August 10, 2023. Colin O'Flynn.
29
```

## Slide 30

## Fault Injection Results (SUM Corruption)

Black Hat USA - August 10, 2023. Colin O'Flynn.

30

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Fault Injection Results (SUM Corruption)
TMP91 Clock Glitch Settings
1300 4
> 1200 4
£
©
1100 4
2
wn
=)
F 1000 +
S
Y
@ 900;
: weeiinaeet
5 8004 E HF
B= j TH
° seas o2oam +
700 4 ee ;
#4
+
600 1 T T T T T T T
50 100 150 200 250 300 350
Glitch Width (CW-Husky Setting)
Black Hat USA - August 10, 2023. Colin O'Flynn.
30
```

## Slide 31

## Easy-Mode Level 3: Fault Injection Attack

Black Hat USA - August 10, 2023. Colin O'Flynn.

31

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Easy-Mode Level 3: Fault Injection Attack
SLUpE-BLLLUIWAUL = 2v0u wiey #1000
for glitch_settings in gc.glitch_values():
scope.glitch.ext_offset = glitch_settings[o]
for i in range(sample_size):
reset_target()
target. ser.flush()
response, responsehex
if responsehex[0] !
raise IoError("sync Error")
"\x86", 1, 1)
scope.arm()
400 glitch Loop
target.ser.write(b"\x10")
ret = scope.capture()
if ret:
print('Timeout - no trigger’)
gc.add ("reset")
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
print (response)
print(hex(response[0]))
print (scope.glitch.ext_offset)
print("#@", end=
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
bl.cmd_ram_transfer(rc.B_F16_RAM1000_ROM10000_TLCS9@L1["data"], rc.B_F16_RAM1000_ROM10000_TLCS9@0L1[“start_address"], skipcm
rl = tl.RamCodeProtocol (target. ser)
#Print the password (should match the known one)
time.sleep(0.1)
data = rl.cmd_read(@x@2FEF4, 12)
":"join(hex(ord(char)) for char in data)
"oxde: Oxad : Oxbe: Oxef :Oxca:Oxfe: Oxfa:Oxce:0x11:0x22:0x33:0x44"
#Read the full flash itself
91FW27UG in Single Boot Mode - flash is from @x10000 to 0x30000 (starts @ @x10000, Length = @x20000)
flash = rl.cmd_read(0x10000, 0x20000)
len(flash)
131072
known_pw =
@xDE, OXAD, OxBE, OxEF, OxCA, OXFE, OXxFA, OxCE, Ox11, 0x22, 0x33, 0x44]
bl = tl.LowLevelBootloader(target.ser, reset_target, password=known_pw, reset_and_connect=False)
b1.cmd_ram_transfer(rc.B_F16_RAM1000_ROM10000_TLCS90QL1["data"], rc.B_F16_RAM1000_ROM10000_TLCS900L1["start_address"], skipcm
rl = tl.RamCodeProtocol (target .ser)
Black Hat USA - August 10, 2023. Colin O'Flynn.
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Select difficulty:
Easy
Medium
Hard
Black Hat USA - August 10, 2023. Colin O'Flynn.
33
```

## Slide 34

Black Hat USA - August 10, 2023. Colin O'Flynn. 34

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Seles,
20-Pin
Target B.
ik Hat USA - August 10, 2023.
13
© CW312 Sty)
Suppor ,
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Medium-Mode Level 2: Fault Injection
x87
11710
& [133]
@x85
11715
& [17]
x11
11750
r [16]
0x10
11755
In [59]: bl #known_pw = [@xDE, @xAD, OxBE, OxEF, @xCA, @xFE, @xFA, @xCE, @x11, x22, 0x33, Ox44]
known_pw = [ord(c) for c in “samsungovene"
bl = tl.LowLevelBootloader(target.ser, reset_target, password=known_pw, reset_and_connect=False)
bl.cmd_ram_transfer(rc.B_F16_RAM100@_ROM10000_TLCS9@@L1["data"], rc.B_F16_RAM1000_ROM10000_TLCS9@@L1["start_address"], skipcm
rl = tl.RamCodeProtocol(target.ser)
Black Hat USA - August 10, 2023. Colin O'Flynn
```

## Slide 37

Black Hat USA - August 10, 2023. Colin O'Flynn.

37

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
In [11]: Dl resp = rcp.cmd_read(0x10000, 9x100)
In [12]: DP resp
out[a2}: *¥ iv iv EODED SED EEDEED BIDET BEDE EDD EL
YYYYYYYYYYYYYYYYYYY: YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY YY YY
yyyyyyyyy
In [7]: PW bl = tl
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
EH AutoSave @ of) BE] O-~ GS» F_ REOvenxisx v PP Search Colin O'Flynn {co} ® S} = ia} El
File Home Insert Draw PageLayout Formulas Data Review View Help Acrobat Table Design Query | © Comments |
tw 4 |Calibri 11 >| RN ==|=|%- 25 Wrap Text |General -| EY wy ea maxX = 2 ov P ta
Paste Ht) . BI UY. Oi TAS a $ ~%9 <8 8 Conditional Formatas Cell Insert Delete Format % Sort & Find& Analyze
¥ = Formattingy Tabley Stylesy ¥ a ™ re v Filtery Selecty Data
Clipboard & Font & Alignment & Number § Styles Cells Editing Analysis ¥'
F9931 vi te v
[y > ¥ = . +
cost columne =) Gollmnns [=] vies [+ | Column5 [+|Columt~|Columi~| G H J LE M N fe} P Q R
9927 Oxfe9683. £202 110031 LDAL XBC,0x1102
9928 Oxfe9688  c307e4e021 LDB  A,(XBC+WA)
9929 Oxfe968d £10802 41 LDB (0x208),A Kick off TX routine?
9930 Oxfe9691 c2 1e 110061 INCB Ox1,(0x111E)
9931|Oxfe9696 Oe RET i
9932 Oxfe9697 £10902 cb BITB 0x3,(0x209) Serial RX Start QBITB Ox3,(0x209)
9933 Oxfe969b  660b JR Z,OxOFE96A8 JR Z,HERE
9934 Oxfe969d 00 NOP NOP
9935 Oxfe969e c1 080221 LDB A,(0x208) LDB A,(0x208)
9936 Oxfe96a2_- f2000 1100 41 LDB (0x1100),A LDB (0x1120),0x0
9937 Oxfe96a7_——«Oe RET HERE BITB  0x2,(0x209)
9938 Oxfe96a8_ «109 02. ca BITB 0x2,(0x209) JR Z,HERE2
9939 Oxfe96ac 66 Ob JR Z,0xOFE96B9 NOP
9940 Oxfe96ae 00 NOP LDB  A,(0x208)
9941 Oxfe96af —c1 08.02 21 LDB  A,(0x208) LDB  (0x1120),0x0
9942 Oxfe96b3 {200 1100 41 LDB (0x1100),A HERE2 BITB__0x4,(0x209)
9943 Oxfe96b8 Oe RET JR Z,HERE3
9944 Oxfe96b9_  f1 09 02 cc BITB 0x4,(0x209) NOP
9945 Oxfe96bd 66 Ob JR Z,0xOFE96CA LDB  A,(0x208)
9946 Oxfe96bf 00 NOP LDB  (0x1120),0x0
9947 Oxfe96cO = c1 08 02 21 LDB A,(0x208) HERE3 LDB A,(0x1120)
9948 Oxfe96c4_ «200 1100 41 LDB (0x1100),A LOB GA
9949 Oxfe96c9_ «Oe RET EXTZW BC
9950 Oxfe96ca c2 20110021 LDB A,(0x1120) What is 1120?? LDAL XDE,0x1110
9951 Oxfe96cf  c98b LDB CA LDB A,(0x208)
9952 Oxfe96d1 d912 EXTZW BC BC has (0x1120) data LDB (XDE+BC),A
9953 Oxfe96d3_ f2 10 1100 32 LDAL XDE,0x1110 CPB (0x1120),0x0C
9954 Oxfe96d8  c1080221 LDB A,(0x208) RX Byte RET ULE
9955 Oxfe96dc =: f3: 07 e8 e441 LDB (XDE+BC),A Load byte here? LDB (0x1120),0x0
9956 Oxfe96e1 c2 20 11 00 3f 00 CPB (0x1120),0x0 CALR OxOFE956F
9957 Oxfe96e7 + 6e10 JR -NZ,OxOFE96F9 Fail | guess? 0x1110 RET
< > DE92-02439F FW Disassembly —_ Sheet 1 oe Black Hat USA - August 10, 2023. Colin 0) TS 44?
Ready  $& Accessibility: investigate Cg Display Settings 1333] —&) -——#—- + _ 100%
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
OK, Just
In [11]: Dl resp = rcp.cmd_read
In [12]: DP resp
Out[12]: ‘y
YY"
In [7]; PW bl=t
#bL. cmd
#bL. cmd
bl.cmd
Read:
Write:
Black Hat USA - August 10, 2023. Colin O'Flynn.
ly YVYYYYYYVYYYYYYY
YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
47
```

## Slide 48

## $$$  Samsung Parts Department

48

Black Hat USA - August 10, 2023. Colin O'Flynn.

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
$$ > Samsung Parts Department
Prt cong inguie 79090 5x00
Black Hat USA - August 10, 2023. Colin O'Flynn.
```

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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
..Add the Serial Monitor
1H Autosave @ off cotinoryn QP ZG -
v RE Oven REVD.xisx ¥ £ Search
File Home Insert Draw PageLayout Formulas Data Review View Help Acrobat Table Design Query
ul x Calibri in Jk aw |= S&~- 2B Wrap Text {General . ii=ai| BY in Se mex fey z= 49 Pp
paste “A BIU. He ae As $ ~ % 9) BG 99 Conditional Format as Cell Insert Delete Format ~ Sort & Find & — Analyze
. =| _ 2 00 0 Formatting’ Table~ Styles ~ ¥ v ¥ © ~ Filter~ Select Data
Clipboard = & Font & Alignment & ‘Number 8 Styles Cells Editing Analysis
(© SECURITY WARNING External Data Connections have been disabled Enable Content
H124388 vi Se RX Interrupt
wn2_|~|Column3 ~|Column4 {-|Column5 ‘~|Column6 _|~|Column7 [~| Column] ~ |Column ~ | J
124376 f4 ff SWI Ox7
124377 f5 ff SWI 0x7
124378 f6 ff SWI 0x7
124379 f7 ff SWI 0x7
124380 f8 ff SWI 0x7
124381 f9 ff SWI 0x7
124382 fa ff SWI 0x7
124383 fb ff SWI 0x7
124384 fc ff SWI 0x7
124385 fd ff SWI 0x7
124386 fe ff SWI Ox7
124387 ff ff SWI 0x7 a
124388 }00 ff SWI 0x7 3e PUSHL XIZ RX Interrupt
124389 101 ff SWI 0x7 3d PUSHL XIY
124390 102 ff SWI 0x7 3c PUSHL XIX
124391 103 ff SWI 0x7 3b PUSHL XHL
124392 104 ff SWI 0x7 3a PUSHL XDE
124393 105 ff SWI 0x7 39 PUSHL XBC
124394 106 ff SWI 0x7 38 PUSHL XWA
124395 107 ff SWI 0x7 1D 50 EO FF CALL OxOFFEOSO
124396 108 ff SWI 0x7 58 POPL XWA
124397 109 ff SWI 0x7 59 POPL XBC
124398 10a ff SWI 0x7 5a POPL XDE
124399 |0b ff SWI 0x7 5b POPL XHL
DE92-02439D FW Disassembly —Sheet1 + —————
C@ Display Settings B O © - it
Black Hat USA - August 10, 2023. Colin O'Flynn.
Ready $x Accessibility: Investigate
Oo x
© Comments
Slight risk of
overwriting something
else important....
52
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Examples of Global Variables
Ox1248 = Top Temp in F
Ox120a = Heater “ON” Flag |
0.45
0.275
0.05
T T
0 200
Black Hat USA - August 10, 2023. Colin O'Flynn.
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Patched Display Logic
2 om
Bake Roast
Start/set
sserole Chicken
Casserole Naggets ~ 4 B Hold 3 sec
Steam Self
Detrost Seam Sell
Warming Custom Cooking Timer
Drawer Cook Time On/o Delay Start
Black Hat USA - August 10, 2023. Colin O'Flynn.
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Set 375F, Cold Start, Load (Shepherds Pie)
T T T T
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
