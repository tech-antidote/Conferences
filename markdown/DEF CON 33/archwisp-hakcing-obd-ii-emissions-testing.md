---
title: "HaKCing OBD-II Emissions Testing"
speakers: ["Archwisp"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33/Archwisp - HaKCing OBD-II Emissions Testing.pdf"
pages: 57
sha256: "f8598eba470bcc6f0d3905fd2263518ad2e3df54f0fcd9240d8bb858be350595"
text_chars: 4574
ocr_pages: 11
has_ocr: true
redacted_secrets: 0
ocr_confidence: 85.0
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:54:21Z"
---
# HaKCing OBD-II Emissions Testing

**Speakers:** Archwisp  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33/Archwisp - HaKCing OBD-II Emissions Testing.pdf` (57 pages)


## Slide 1

## Slide 2

# HaKCing OBD-II Emissions Testing DEF CON 33

Archwisp - August 2025

## Slide 3

## Slide 4

#### **The thing about rotary motors is that they kill catalytic converters.**

## Slide 5

“Kansas City, MO, and the surrounding areas **do not require emissions testing** . “

## Slide 6

**Rip it out!**

## Slide 7

### **The next 8 years**

## Slide 8

**Me**

## Slide 9

"Vehicle **emissions testing is required** in major metropolitan areas…”

## Slide 10

## Slide 11

“Statute authorizes the Director of **** to **exempt certain vehicles** , including collectible vehicles, **from vehicle emissions requirements** .”

## Slide 12

## Slide 13

“… **primarily for use in car club activities** , exhibitions, parades … **and be used only infrequently** …”

## Slide 14

## Slide 15

“… and **requires the owner to have another vehicle** for personal use.”

## Slide 16

## Slide 17

Welp. Glad I kept those parts.

## Slide 18

## Slide 19


> Recovered by OCR — confidence 84/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CATALYST | ; EVAP SYSTEM +- ¢
HEATED CAT /NOT SUPPORTED AIR SYSTEM
EGR | NOT SUPPORTED | HEATED 02 AIR CONDITIONER ‘NOT SUPPORTED
IN PREPARING TO INSPECT THIS VEHICLE, THE FOLLOWING ITEM(S) PREVENTED THE INSPECTION FROM cee
COMPLETED:
- THE VEHICLE’'S COMPUTER SYSTEM IS "NOT READY" TO BE TESTED AS REPORTED.
```

## Slide 20


> Recovered by OCR — confidence 87/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Mode 3 (HO2S heater, HO2S, and TWC Repair Verification Drive Mode)
1. Perform the Mode | first.
2. Verify that all accessory loads (A/C, headlights, blower fan, rear window defroster) are off.
3. Drive the vehicle as shown in the graph. The driving condition before driving at constant spee
specified.
MORE THAN 89 {55}
(MT: STH, AT: D ae 72—88 {45—55}
r _ (MT: STH, AT: D RANGE)
© VEHICLE SPEED (km/h (mph)})
MORETHANS5 = 1 3
START ENGINE
```

## Slide 21

## Slide 22

**!@#$**

## Slide 23

**DEF CON 26**

## Slide 24

## Slide 25

https://www.csselectronics.com/pages/obd2-explained-simple-intro


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
The OBD2 diagnostic message [SAE J1979, ISO 15031-5]
To better understand OBD2 on CAN, let us consider a raw 'Single Frame' OBD2 CAN message. In simplified terms, an OBD2 message is
comprised of an identifier, data length (PCI field) and data. The data is split in Mode, parameter ID (PID) and data bytes.
OBD2 on CAN (Single Frame)
Mode PID (Unused)
(e.g. 41) (e.g. OD) (eg 32) lee, AA) lee AA) fee, AA) (e.g. AA)
CAN data (8 bytes)
https://www.csselectronics.com/pages/obd2-explained-simple-intro
```

## Slide 26

https://www.csselectronics.com/pages/obd2-explained-simple-intro


> Recovered by OCR — confidence 83/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Legislated OBD CAN identifiers (11-bit)
AN
@x7DF Functionally addressed request sent by tester
@x7E8 to @x7E7 Physical request from tester _to FCUl #4) to #8
@x7E8 to @x7EF Physical response fro@ ECU #1 to #8 to tester:
Legislated OBD CAN identifiers (29-bit)
N Li
8@x18DB33F1 Functionally addressed request sent by tester
@x18DAxxF1 Physical request from tester to ECU #
8@x18DAF1 Physical response from ECU # to tester
https://www.csselectronics.com/pages/obd2-explained-simple-intro
```

## Slide 27

## Slide 28

## Slide 29


> Recovered by OCR — confidence 73/100 on the text kept, 53/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
2000
2909000
290000
0
0
0
0
2 00000
2 090000
```

## Slide 30

## Slide 31

## Slide 32


> Recovered by OCR — confidence 82/100 on the text kept, 49/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
398 ms
+0.1 ms +0.2 ms +0.3 ms
Identifier: Ox7DF Data: 0x02 ff Data: 0x01 0x99 CRC value: 0x187B [BN
po CANH H
® CAN
ov
```

## Slide 33

## Slide 34

## Slide 35

##### **PID Length**

##### **Service**

## Slide 36

https://en.wikipedia.org/wiki/OBD-II_PIDs


> Recovered by OCR — confidence 91/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Service 01 - Show current data [cit]
Data
$ ¢ bytes ¢ Description ¢ ¢ Maxvalue ¢ Units ¢ Formula’?!
(hex) | (Dec) value
returned
4
4
PIDs supported Bit encoded [A7..D0] == [PID
[$01 - $20] $01..PID $20] See below
Monitor status
since DTCs
cleared.
(Includes
malfunction
indicator lamp
Q1 1 4 (MIL), status Bit encoded. See below
and number of
DTCs,
components
tests, DTC
readiness
checks)
https://en.wikipedia.org/wiki/OBD-II_PIDs
```

## Slide 37

https://www.csselectronics.com/pages/obd2-pid-table-on-boarddiagnostics-j1979


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
HEX v 11-bit IDs v
Bit Bit . .
PID Name Scale Offset Min | Max Unit
start Length
00 v PIDs supported [01 - 20] 31 32 1 0 Encoded
Byte 0 Byte 1 Byte 2 Byte 3 Byte 4 Byte 5 Byte 6 Byte 7
Response (example) 06 41 00 12 34 56 78 AA
Physical value (DEC) = 0 + 1 * 305419896 = 305419896 Encoded
Physical value (BIN) =
PID Name Supported?
01 Monitor status since DTCs cleared
02 Freeze DTC
03 Fuel system status
https://www.csselectronics.com/pages/obd2-pid-table-on-board-
```

## Slide 38


> Recovered by OCR — confidence 71/100 on the text kept, 62/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
2ms
+0.1 ms
+0.2 ms
Identifier: Ox7E8 Data: 0x41 §§ Data: 0x00 §§ Data: OxBE Data: Ox1F —§Data: OxE8@§ Data: 0x1B —Data: OxAAMData: OxAA
Identifier: Ox7E8 Data: 0x41 Data: 0x00 Data: OxBE Data: Ox1F Data: OxE8#™@ Data: 0x1B §§Data: OxAABData: OxAA
Xesee
```

## Slide 39


> Recovered by OCR — confidence 91/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
D2 RX
D3 TX
AO CANH
Al CANL
+0.3 ms
+0.4 ms
4.0V
3.5V
3.0V
2.5V
2.5V
2.0V
1.5V
1.0V
```

## Slide 40

## Slide 41

Remember the owl?

## Slide 42

## • Hardware • Microcontroller drivers • Protocols • High-level logic

## Slide 43

This is the point where my friends were making a lot of noise about AI coding agents.

## Slide 44

## Slide 45

**Things AI is good at** • Hardware ❌ • Microcontroller drivers ✅ • Protocols ❌ ❌ • High-level logic

## Slide 46

## Slide 47

## Slide 48

## Slide 49

## Slide 50

**ALL MONITORS READY**


> Recovered by OCR — confidence 87/100 on the text kept, 49/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ALL MONITORS READY
@actron.
OBD I! PocketScan™
```

## Slide 51

# AI, please turn this into a proxy.

## Slide 52

## Slide 53

## Slide 54

## Slide 55

## Slide 56

**DEMO TIME**

## Slide 57

### **https://github.com/ archwisp/OBD2Proxy**
