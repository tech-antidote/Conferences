---
title: "Handoff All Your Privacy (Again)"
speakers: ["Christine Fossaceca"]
conference: "REcon"
conference_full: "REcon 2023"
edition: ""
year: 2023
source_pdf: "REcon 2023 Slides/Christine Fossaceca_Handoff All Your Privacy (Again) .pdf"
pages: 184
sha256: "288523c20e41b4a5f9c0883aa9a62e2e128e01cdf06a295279acdbc4007ce0c1"
text_chars: 79465
ocr_pages: 78
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:25:42Z"
---
# Handoff All Your Privacy (Again)

**Speakers:** Christine Fossaceca  
**Conference:** REcon 2023  
**Source:** `REcon 2023 Slides/Christine Fossaceca_Handoff All Your Privacy (Again) .pdf` (184 pages)

## Slide 1

```
Handoff All Your
Privacy(Again)
```

```
By Christine Fossaceca
```

## Slide 2

### `PLEASE TURN OFF YOUR BLUETOOTH`

## Slide 3

## `$whoami`

my dog Honey(pot)

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Swhoami
4ihome/christine $ c
, PODCAST
: a@x71n3 my dog Honey(pot)
```

## Slide 4

```
STREAM SEASON 2 NOW!
```

```
@herhaxpodcast
```

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
STREAM SEASON 2 NOW!
w
hur fox
@herhaxpodcast 6 PODCAST
```

## Slide 5

#### `Agenda`

• `What is the Continuity Protocol?` • `How to Capture Continuity Data` • `Packet Breakdown` • ✨ `Live DEMO!` ✨ • `FindMy Protocol + Airtag Packets` • `Airtag Encryption`

## Slide 6

Continuity Protocol Explained _It’s not a bug, it’s a feature!_

- ”Continuity” allows for information sharing and “seamless” experience” across Apple products and peripherals

   - Examples: Resume browsing from iPhone to MacBook, Universal Clipboard, Instant Hotspot, WiFi Password

- Powered via a combination of Wi-Fi and Bluetooth LE

   - furiousMAC

- Proprietary! But we have reverse engineered this protocol and disclosed to Apple where Continuity exposes sensitive information or is poorly implemented **. Shmoocon 2020. Objective By the Sea 2022. Jailbreak Security Summit 2022.**

- Past @furiousmac Papers: **<u>Handoff All Your Privacy – A Review of Apple’s Bluetooth Low Energy Continuity Protocol; Who Tracks the Trackers? Circumventing Apple’s Anti-Tracking Alerts in the Find My Network;</u>**

- Other research: <u>Discontinued Privacy: Personal Data Leaks in Apple Bluetooth-Low-Energy Continuity Protocols; TU Darmstadt (multiple works) such as Open Haystack</u> and AirGuard

## Slide 7

##### So you might be wondering…

- What types of information are being sent in the clear?

● And how are you capturing this?

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
So you might be wondering...
e What types of information are being sent in the clear?
continuity
Activities [=] Terminal Mon 23:08 @
—s
wonder@ubuntu: ~/bluetooth
Trash
File Edit View Search Terminal Help VMware Fusion
Radio options:
-a[0-7] get/set power amp
-c[2400-2483] get/set che ES
-C[0-78] get/set channel Remember my choice and do not ask again
-q[1-225 (RSSI threshold
-t intitiate continuous {
-z set squelch level
Desktop
Ubertooth One.
v Choose where you would like to connect OpenMoko
Connect to Mac Connect to Linux
Range test:
-e start repeater mode
-m display range test result
-n initiate range test
Miscellaneous:
-f activate flash programming (DFU) mode
i activate In-System Programming (ISP) mode
-b get hardware board id number
p get microcontroller Part ID
-s get microcontroller serial number
-x xmas Lights
wonder@ubuntu:~/blLuetooth$
e And how are you capturing this?
```

## Slide 8

##### How to Capture Continuity Data

- Bluetooth Hardware Dongle

   - Ubertooth or NRF Dongle

- Wireshark (compiled from source)

- ● furiousMAC custom dissector!

   - <u>https://github.com/furiousMAC/continuity</u>

- Check out our repository with build instructions!

## Slide 9

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

Apple BLE Frame Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained — !t’snota bug, it’s a feature!
Access Address - 0x8E89BED6
Packet Header
Advertising Address - xx:xx:xx:xx:xx:Xxx
Length / Type - 0x01 / Flags (Optional) Length
Type - OxFF Company ID - 0x004C Apple Type
Apple Length | Variable Length Apple Data Apple Type
Apple Length Variable Length Apple Data
Apple BLE Frame Format
```

## Slide 10

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

###### Apple BLE Frame Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained _ !t’snota bug, it’s a feature!
Advertising Address - xx:xx:xx:xxX!XX:XX
Length / Type - 0x01 / Flags (Optional) Length
Type - OxFF Company ID - 0x004C Apple Type
Apple Length | Variable Length Apple Data | Apple Type 00 00 18 00 fb G8 OO BO 36 75 Oc BO OO 62 9 OO 6u---b
Apple Length Variable Length Apple Data 75 da 7d 14 62 01 06 Oa ff 4c 00 10 05 06 ic e7 u-} L
Apple BLE Frame Format
```

## Slide 11

##### Continuity Protocol Explained

_It’s not a bug, it’s a feature!_

###### Apple BLE Frame Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained _ !t’snota bug, it’s a feature!
Advertising Address - xx:xx:xx:xxX!XX:XX
Length / Type - 0x01 / Flags (Optional) Length
Type - OxFF Company ID - 0x004C Apple Type
Apple Length | Variable Length Apple Data | Apple Type 00 00 18 00 fb G8 OO BO 36 75 Oc BO OO 62 9 OO 6u---b
Apple Length Variable Length Apple Data 75 da 7d 14 62 01 06 Oa ff 4c 00 10 05 06 ic e7 u-} L
Apple BLE Frame Format
```

## Slide 12

##### Continuity Protocol Explained

_It’s not a bug, it’s a feature!_

###### Apple BLE Frame Format

The access address is at a 24 byte offset

## Slide 13

##### Continuity Protocol Explained

_It’s not a bug, it’s a feature!_

###### Apple BLE Frame Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained — !t’snota bug, it’s a feature!
Access Address - 0x8E89BED6 nee Mi : 6u---b
Advertising Address - xx:xx:xx:xxX!XX:XX
Length / Type - 0x01 / Flags (Optional) Length
Type - OxFF Company ID - 0x004C Apple Type
Apple Length | Variable Length Apple Data Apple Type : : ‘ ue ‘ 6u---b
, |d6_be 89 se}oo 14 be 7b {
Apple Length Variable Length Apple Data 75 da 7d 14 02 01 06 Oa [us be ss se]oo 06 ic e7 u-} L
Apple BLE Frame Format
```

## Slide 14

##### Continuity Protocol Explained

_It’s not a bug, it’s a feature!_

###### Apple BLE Frame Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained — !t’snota bug, it’s a feature!
Access Address - 0x8E89BED6 ae A 6u---b
Advertising Address - xx:xx:xx:xxX!XX:XX
Length / Type - 0x01 / Flags (Optional) Length
Type - OxFF Company ID - 0x004C Apple Type
Apple Length | Variable Length Apple Data Apple Type ae ‘ 6u---b
Apple Length Variable Length Apple Data 00 14 be 7b {
Apple BLE Frame Format
```

## Slide 15

##### Continuity Protocol Explained

_It’s not a bug, it’s a feature!_

###### Apple BLE Frame Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained _ !t’snota bug, it’s a feature!
Access Address - 0x8E89BED6 ae u : 6u---b
Advertising Address - xx:xx:xx:xxX!XX:XX
Length / Type - 0x01 / Flags (Optional) Length
Type - OxFF Company ID - 0x004C Apple Type
Apple Length | Variable Length Apple Data Apple Type ae ‘ 6u---b
Apple Length Variable Length Apple Data 00 14 be 7b {
Apple BLE Frame Format
```

## Slide 16

##### Continuity Protocol Explained

_It’s not a bug, it’s a feature!_

###### Apple BLE Frame Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained _ !t’snota bug, it’s a feature!
Access Address - 0x8E89BED6 ae u : 6u---b
Advertising Address - xx:xx:xx:xxX!XX:XX
Length / Type - 0x01 / Flags (Optional) Length
Type - OxFF Company ID - 0x004C Apple Type
Apple Length | Variable Length Apple Data Apple Type ‘ ‘ : ‘ ‘ 6u---b
, 00 14]}bc 7b {
mpale Leneih Variable Length pple sts 75 da 7d 14 02 01 6 Oa ff 4c 00 10 ea a4)pe ey u-} L
Apple BLE Frame Format
[eaa]en of w @--0
```

## Slide 17

##### Continuity Protocol Explained

_It’s not a bug, it’s a feature!_

###### Apple BLE Frame Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained _ !t’snota bug, it’s a feature!
Access Address - 0x8E89BED6 ae A : 6u---b
Advertising Address - xx:xx:xx:xxX!XX:XX
Length / Type - 0x01 / Flags (Optional) Length
Type - OxFF Company ID - 0x004C Apple Type
Apple Length | Variable Length Apple Data Apple Type é ‘ : ‘ Oe ‘ 6u---b
Apple Length Variable Length Apple Data 75 da 7d 14 02 01 06 Oa ff 4c 00 10 05 06 ic e7 u-} L
Apple BLE Frame Format
```

## Slide 18

##### Con3nuity Protocol Explained

_It’s not a bug, it’s a feature!_

###### Apple BLE Frame Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained _ !t’snota bug, it’s a feature!
Access Address - 0x8E89BED6 ae u : : 6u---b
Packet_ Header } } 17 df "h B B
Advertising Address - xx:xx:xx:xxX!XX:XX |
Length / Type - 0x01 / Flags (Optional) Length
Type - OxFF Company ID - 0x004C Apple Type
Apple Length | Variable Length Apple Data Apple Type ‘ ‘ : ‘ Oe ‘ 6u---b
Apple Length Variable Length Apple Data 75 da 7d 14 02 01 06 Oa ff 4c 00 10 05 06 ic e7 u-} L
Apple BLE Frame Format
```

## Slide 19

##### Con3nuity Protocol Explained

_It’s not a bug, it’s a feature!_

###### Apple BLE Frame Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained _ !t’snota bug, it’s a feature!
Access Address - 0x8E89BED6 nee Mi : ‘ 6u---b
Packet_ Header ( } } i7 df "h B B
Advertising Address - xx:xx:xx:xxX!XX:XX |
Length / Type - 0x01 / Flags (Optional) Length
Type - OxFF Company ID - 0x004C Apple Type
Apple Length | Variable Length Apple Data Apple Type ‘ ‘ : ‘ Oe ‘ 6u---b
Apple Length Variable Length Apple Data [7s da 7d 14]o2 01 06 Oa ff 4c 00 10 05 O6 TEST U} L
de R
Apple BLE Frame Format
Jo 6
```

## Slide 20

##### Con3nuity Protocol Explained

_It’s not a bug, it’s a feature!_

###### Apple BLE Frame Format

c2:b6:98:c8:df:17

14:7d:da:75:7b:bc

60:7e:9d:e4:6f:8b

## Slide 21

##### Continuity Protocol Explained

_It’s not a bug, it’s a feature!_

###### Apple BLE Frame Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained — !t’snota bug, it’s a feature!
Access Address - 0x8E89BED6 oF es ‘i oe ‘ : 6u---b
Packet Header aed — "h B B
Advertising Address - xx:xx:xx:xxX!XX:XX
Length / Type - 0x01 / Flags (Optional) Length
Type - OxFF Company ID - 0x004C Apple Type
Apple Length | Variable Length Apple Data Apple Type ‘ f : \ oe ( \ 6u b
; {
Apple Length Variable Length Apple Data 92 01 06 0a ff 4c 00 10 05 06 1c e7 U} L
Apple BLE Frame Format
Ww @--o
```

## Slide 22

##### Continuity Protocol Explained

_It’s not a bug, it’s a feature!_

###### Apple BLE Frame Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained _ !t’snota bug, it’s a feature!
Access Address - 0x8E89BED6 oF es ‘i oe ‘ : 6u---b
Packet Header aed — "h B B
Advertising Address - xx:xx:xx:XxX!XX:XX
Length / Type - 0x01 / Flags (Optional) Length
a |
| Type -OxFF | Company ID - 0x004C Apple Type
Apple Length | Variable Length Apple Data Apple Type ‘ f : \ oe ( \ 6u b
; {
Apple Length Variable Length Apple Data 92 01 06 0a ff 4c 00 10 05 06 1c e7 U} L
Apple BLE Frame Format
Ww @--o
```

## Slide 23

##### Continuity Protocol Explained

_It’s not a bug, it’s a feature!_

###### Apple BLE Frame Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained _ !t’snota bug, it’s a feature!
Access Address - 0x8E89BED6 oF es ‘i oe ‘ : 6u---b
Packet Header aed — "h B B
Advertising Address - xx:xx:xx:XxX!XX:XX
Length / Type - 0x01 / Flags (Optional) Length
a |
| Type -OxFF | Company ID - 0x004C Apple Type
Apple Length | Variable Length Apple Data Apple Type ‘ f : \ oe ( \ 6u b
; {
Apple Length Variable Length Apple Data 92 01 06 6a ff 4c 00 10 05 06 1c e7 U} L
Apple BLE Frame Format
Ww @--o
```

## Slide 24

##### Continuity Protocol Explained

_It’s not a bug, it’s a feature!_

###### Apple BLE Frame Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained _ !t’snota bug, it’s a feature!
Access Address - 0x8E89BED6 oF es ‘i oe ‘ : 6u---b
Packet Header aed — "h B B
Advertising Address - xx:xx:xx:XxX!XX:XX
Length / Type - 0x01 / Flags (Optional) Length
a |
| Type -OxFF | Company ID - 0x004C Apple Type
Apple Length | Variable Length Apple Data Apple Type ‘ f : \ oe ( \ 6u b
; {
Apple Length Variable Length Apple Data 92 01 06 6a ff 4c 00 10 05 06 1c e7 U} L
Apple BLE Frame Format
Ww @--o
```

## Slide 25

##### Con3nuity Protocol Explained

_It’s not a bug, it’s a feature!_

###### Apple BLE Frame Format

Length only                 7 Bytes

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained _ !t’snota bug, it’s a feature!
Access Address - 0x8E89BED6 oF es ‘i oe ‘ : 6u---b
Packet Header aed — "h B B
Advertising Address - xx:xx:xx:XxX!XX:XX
Length / Type - 0x01 / Flags (Optional) Length Length only 7 Bytes
a |
| Type -OxFF | Company ID - 0x004C Apple Type
Apple Length | Variable Length Apple Data Apple Type ‘ ‘ 5 é ua : ‘ 6u---b
Apple Length Variable Length Apple Data Beraives ca [rac ais os Of ice?” w.} A {
Apple BLE Frame Format
Ww @--o
```

## Slide 26

##### Continuity Protocol Explained

_It’s not a bug, it’s a feature!_

###### Apple BLE Frame Format

Length only                 7 Bytes

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained — !t’snota bug, it’s a feature!
Access Address - 0x8E89BED6 Sa 6u---b
Packet Header ; _- ae "h B B
Advertising Address - xx:xx:xx:XxX!XX:XX
Length / Type - 0x01 / Flags (Optional) Length Length only 7 Bytes
| Type -OxFF | Company ID - 0x004C Apple Type
| Apple Length | Variable Length Apple Data | Apple Type | ; al ; ‘ 6u b
| Apple Length | Variable Length Apple Data | ) 02 01 06 Ga ff 4c 00 10 05 06 ic e7 u-} L {
Apple BLE Frame Format
6u b
Ww @--o
```

## Slide 27

##### Con3nuity Protocol Explained

_It’s not a bug, it’s a feature!_

###### Apple BLE Frame Format

Length only                 7 Bytes

**BLE flags related to discoverability and transmission power (not Apple Specific)**

## Slide 28

##### Continuity Protocol Explained

_It’s not a bug, it’s a feature!_

###### Apple BLE Frame Format

Length only                 7 Bytes

Length 0x2, 2 bytes of flag info

## Slide 29

##### Continuity Protocol Explained

_It’s not a bug, it’s a feature!_

Apple BLE Frame Format

Length only                 7 Bytes

Length 0x2, 2 bytes of flag info

## Slide 30

##### Continuity Protocol Explained

_It’s not a bug, it’s a feature!_

###### Apple BLE Frame Format

Length only                 7 Bytes

Length 0x2, 2 bytes of flag info Length 0xa, 10 bytes succeeding

## Slide 31

##### Continuity Protocol Explained

_It’s not a bug, it’s a feature!_

Apple BLE Frame Format

Length only                 7 Bytes

Length 0x2, 2 bytes of flag info Length 0xa, 10 bytes succeeding

## Slide 32

##### Continuity Protocol Explained

_It’s not a bug, it’s a feature!_

###### Apple BLE Frame Format

Length only                 7 Bytes

Length 0x2, 2 bytes of flag info Length 0xa, 10 bytes succeeding

## Slide 33

##### Con3nuity Protocol Explained

_It’s not a bug, it’s a feature!_

###### Apple BLE Frame Format

Length only                 7 Bytes

Length 0x2, 2 bytes of flag info Length 0xa, 10 bytes succeeding

Length 0x2, 2 bytes of flag info

## Slide 34

##### Continuity Protocol Explained

_It’s not a bug, it’s a feature!_

###### Apple BLE Frame Format

Length only                 7 Bytes

Length 0x2, 2 bytes of flag info Length 0xa, 10 bytes succeeding

Length 0x2, 2 bytes of flag info

## Slide 35

##### Continuity Protocol Explained

_It’s not a bug, it’s a feature!_

###### Apple BLE Frame Format

Length only                 7 Bytes

Length 0x2, 2 bytes of flag info Length 0xa, 10 bytes succeeding

Length 0x2, 2 bytes of flag info Length 0x13, 19 bytes succeeding

## Slide 36

##### Con3nuity Protocol Explained

_It’s not a bug, it’s a feature!_

###### Apple BLE Frame Format

Length only                 7 Bytes

Length 0x2, 2 bytes of flag info Length 0xa, 10 bytes succeeding

Length 0x2, 2 bytes of flag info Length 0x13, 19 bytes succeeding

## Slide 37

##### Con3nuity Protocol Explained

_It’s not a bug, it’s a feature!_

###### Apple BLE Frame Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained _ !t’snota bug, it’s a feature!
Access Address - 0x8E89BED6 oF es : oe ‘ : 6u---b
Packet Header aed — "h B B
Advertising Address - xx:xx:xx:xxX!XX:XX
Length / Type - 0x01 / Flags (Optional) Length
Type - OxFF Company ID - 0x004C Apple Type
Apple Length | Variable Length Apple Data Apple Type oe ( \ 6u b
Apple Length Variable Length Apple Data mesesice? wt A {
Apple BLE Frame Format
Ww @--o
```

## Slide 38

##### Continuity Protocol Explained

_It’s not a bug, it’s a feature!_

###### Apple BLE Frame Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained — !t’snota bug, it’s a feature!
Access Address - 0x8E89BED6 Sa 6u---b
Packet Header aed — "h B B
Advertising Address - xx:xx:xx:xxX!XX:XX
Length / Type - 0x01 / Flags (Optional) Length
Type - OxFF Company ID - 0x004C Apple Type
Apple Length | Variable Length Apple Data Apple Type ‘ ‘ 5 é ua : ‘ 6u---b
Apple Length Variable Length Apple Data ; “Tiles 06 ice? u} A {
Apple BLE Frame Format
Ww @--o
```

## Slide 39

##### Continuity Protocol Explained

_It’s not a bug, it’s a feature!_

|0xb|
|---|

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained — !t’snota bug, it’s a feature!
Message Dec Hex
Type Value | Value ie ? 6u---b
; aeels Mee “h
AirDrop 5 0x05 12]02 00 00 90 88 04 °
Proximity 7 0x07
Pairing
Hey Siri 8 0x08 ie 6u-b {
Switch
Handoff 12 Oxc
Instant 14 Oxfe “a 6u---b
@
Action
Nearby Info 16 0x10
FindMy 18 0x12
```

## Slide 40

##### Continuity Protocol Explained

_It’s not a bug, it’s a feature!_

|Apple Message Types|
|---|
|0xb|

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained _ !t’snota bug, it’s a feature!
Message Dec Hex Apple Me
KS
Type Value Value Sage Types i oe bu. -b
; aeels Mee “h
AirDrop 5 0x05 12]02 00 00 90 88 04 t °
Proximity 7 0x07 ?
Pairing
Hey Siri 8 0x08 OS 6u: <b :
Switch
Handoff 12 Oxc
Instant 14 Oxfe “a 6u---b
@
Action
Nearby Info 16 0x10
FindMy 18 0x12
```

## Slide 41

##### Con3nuity Protocol Explained

_It’s not a bug, it’s a feature!_

Type 18: Find My
0xb
Apple Message Types

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained _ !t’snota bug, it’s a feature!
Message Dec Hex Apple Me
KS
Type Value Value Sage Types i oe bu. -b
AirDrop 5 0x05 12]02 00 00 90 88 04 ” t °
Proximity 7 0x07 ? oo
Pairing Type 18: Find My
Hey Siri 8 0x08 OS 6u: <b :
Switch
Handoff 12 Oxc
Instant 14 Oxfe “a 6u---b
@
Action
Nearby Info 16 0x10
FindMy 18 0x12
```

## Slide 42

##### Con3nuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

Type 18: Find My  ✨samteplov.com✨
0xb
Apple Message Types

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained _ !t’snota bug, it’s a feature!
Message Dec Hex Apple Me
S
Type Value Value Sage Types i oe bu. -b
AirDrop 5 0x05 12]02 00 00 90 88 04 t °
Proximity 7 0x07 ? .
: samteplov.com
Pairing Type 18: Find My p
Hey Siri 8 0x08 oe 6u---b :
Switch
Handoff 12 Oxc
Instant 14 Oxfe “a 6u---b
@
Action
Nearby Info 16 0x10
FindMy 18 0x12
```

## Slide 43

##### Con3nuity Protocol Explained

_It’s not a bug, it’s a feature!_

Type 18: Find My
0xb
Type 16: Nearby
Apple Message Types

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained _ !t’snota bug, it’s a feature!
Message Dec Hex APPle Me
S
Type Value Value Sage Types 4 ; bu. -b
AirDrop 5 0x05 12]02 00 00 90 88 04 ” t °
Proximity 7 0x07 ? oo
Pairing Type 18: Find My
Hey Siri 8 0x08 oe 6u---b :
Switch
Type 16: Nearby
Handoff 12 Oxc
Instant 14 Oxfe “a 6u---b
@
Action
Nearby Info 16 0x10
FindMy 18 0x12
```

## Slide 44

##### Continuity Protocol Explained

_It’s not a bug, it’s a feature!_

Type 18: Find My
0xb
Type 16: Nearby
Type 12: Handoff
Apple Message Types

## Slide 45

_It’s not a bug, it’s a feature!_

##### Con3nuity Protocol Explained

0xb

Type 16: Nearby

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained _ !t’snota bug, it’s a feature!
Message Dec Hex Apple Me
S
Type Value | Value Sage Typ es
AirDrop 5 0x05
Proximity 7 0x07 ?
Pairing
Hey Siri 8 0x08 oe 6u: <b :
Switch
Type 16: Nearby
Handoff 12 Oxc
Instant 14 Oxfe
Hotpot
Nearby 15 Oxff
Action
Nearby Info 16 0x10
FindMy 18 0x12
```

## Slide 46

##### Con3nuity Protocol Explained

_It’s not a bug, it’s a feature!_

Type 16: Nearby

###### Apple BLE Frame Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained _ !t’snota bug, it’s a feature!
Access Address - 0x8E89BED6 ‘ 4 : i {
Packet Header 52 b4 a7 aa de R
Advertising Address - xx:xx:xx:xxX!XX:XX
Length / Type - 0x01 / Flags (Optional) Length
Type 16: Nearby
Type - OxFF Company ID - 0x004C Apple Type
Apple Length | Variable Length Apple Data Apple Type
Apple Length Variable Length Apple Data
Apple BLE Frame Format
```

## Slide 47

##### Continuity Protocol Explained

_It’s not a bug, it’s a feature!_

Type 16: Nearby

###### Apple BLE Frame Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained — !t’snota bug, it’s a feature!
Access Address - 0x8E89BED6 ‘ 4 : i {
Packet Header 52 b4 a7 aa de R
Advertising Address - xx:xx:xx:xxX!XX:XX
Length / Type - 0x01 / Flags (Optional) Length
Type 16: Nearby
Type - OxFF Company ID - 0x004C Apple Type
Apple Length | Variable Length Apple Data Apple Type
Apple Length Variable Length Apple Data
Apple BLE Frame Format
```

## Slide 48

##### Con3nuity Protocol Explained

_It’s not a bug, it’s a feature!_

Length = 5

###### Apple BLE Frame Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained _ !t’snota bug, it’s a feature!
Access Address - 0x8E89BED6 ‘ 4 : a si {
10}O5)06 ic e7 u-} L
Packet Header 52 b4 a7 aa de R
Advertising Address - xx:xx:xx:xxX!XX:XX
- Length =5
Length / Type - 0x01 / Flags (Optional) Length
Type - OxFF Company ID - 0x004C Apple Type
Apple Length | Variable Length Apple Data Apple Type
Apple Length Variable Length Apple Data
Apple BLE Frame Format
```

## Slide 49

##### Continuity Protocol Explained

_It’s not a bug, it’s a feature!_

CRC

###### Apple BLE Frame Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained — !t’snota bug, it’s a feature!
Access Address - 0x8E89BED6 ‘ 4 : ‘ a é {
10}O5)06 ic e7 u-} L
Packet Header 52 b4 a7 aa de R
Advertising Address - xx:xx:xx:xxX!XX:XX
Length / Type - 0x01 / Flags (Optional) Length
Type - OxFF Company ID - 0x004C Apple Type
Apple Length | Variable Length Apple Data Apple Type
Apple Length Variable Length Apple Data
Apple BLE Frame Format
```

## Slide 50

##### Con3nuity Protocol Explained

_It’s not a bug, it’s a feature!_

###### Apple BLE Frame Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained _ !t’snota bug, it’s a feature!
Access Address - 0x8E89BED6 ‘ 4 : ‘ a é {
10}O5)06 ic e7 u-} L
Packet Header 52 b4 a7 aa de R
Advertising Address - xx:xx:xx:xxX!XX:XX
Length / Type - 0x01 / Flags (Optional) Length
Type - OxFF Company ID - 0x004C Apple Type
Apple Length | Variable Length Apple Data Apple Type
Apple Length Variable Length Apple Data
Apple BLE Frame Format
```

## Slide 51

##### Con3nuity Protocol Explained

_It’s not a bug, it’s a feature!_

###### Apple BLE Frame Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained _ !t’snota bug, it’s a feature!
Access Address - 0x8E89BED6 ‘ 4 i {
Packet Header 52 b4 fl R
Advertising Address - xx:xx:xx:xxX!XX:XX
Length / Type - 0x01 / Flags (Optional) Length
Type - OxFF Company ID - 0x004C Apple Type
Apple Length | Variable Length Apple Data Apple Type
Apple Length Variable Length Apple Data
Apple BLE Frame Format
```

## Slide 52

##### Continuity Protocol Explained

_It’s not a bug, it’s a feature!_

###### Apple BLE Frame Format

06 1c
0000 0100 0001 1100

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained — !t’snota bug, it’s a feature!
Access Address - 0x8E89BED6 ‘ 4 f {
Packet Header 52 b4 R
Advertising Address - xx:xx:xx:xxX!XX:XX
Length / Type - 0x01 / Flags (Optional) Length
Type - OxFF Company ID - 0x004C Apple Type
Apple Length | Variable Length Apple Data Apple Type
Apple Length Variable Length Apple Data
Apple BLE Frame Format
06 1c
0000 0100 0001 1100
```

## Slide 53

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

Action  Meaning
Code
1 Activity Unknown
2 Activity Reporting Disabled
3 Idle
4 Locked Phone
5 Audio is playing with screen off
Apple BLE Frame Format 7 Transition Idle from Locked Screen
9 Screen is  on and video is playing
06 1c
10 Phone locked; push notifications to watch
0000  0100 0001 1100
11 Active user
Reserved
13 User is driving in a vehicle
Airdrop
Reserved AcOon Codes 14 Phone in phone call or face time
On/Off
Primary iCloud

## Slide 54

##### Continuity Protocol Explained

_It’s not a bug, it’s a feature!_

Auth Tag is 0xe752b4

###### Apple BLE Frame Format

06 1c
0000 0100 0001 1100
Airpods Connected
Auto Unlock
4 Byte Auth Tag
Auto Unlock Watch WiFi On/Off
Reserved
Watch Locked
AuthTag
Present

## Slide 55

##### Continuity Protocol Explained

_It’s not a bug, it’s a feature!_

Type 12: Handoff

###### Apple BLE Frame Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained — !t’snota bug, it’s a feature!
Access Address - 0x8E89BED6 ‘ w 4 @--0
Packet Header ' ~~ Ge 00 e3 Oe ~ L
Advertising Address - xx:xx:xx:xxX!XX:XX
Length / Type - 0x01 / Flags (Optional) Length
Type 12: Handoff
Type - OxFF Company ID - 0x004C Apple Type
Apple Length | Variable Length Apple Data Apple Type
Apple Length Variable Length Apple Data
Apple BLE Frame Format
```

## Slide 56

##### Continuity Protocol Explained

_It’s not a bug, it’s a feature!_

Length = 14

###### Apple BLE Frame Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained — !t’snota bug, it’s a feature!
Access Address - 0x8E89BED6 ‘ w @--0
Packet Header ' “a Ge} 00 e3 Oe ~ L
Advertising Address - xx:xx:xx:xxX!XX:XX
Length / Type - 0x01 / Flags (Optional) Length
Length = 14
Type - OxFF Company ID - 0x004C Apple Type
Apple Length | Variable Length Apple Data Apple Type
Apple Length Variable Length Apple Data
Apple BLE Frame Format
```

## Slide 57

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

CRC

###### Apple BLE Frame Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained — !t’snota bug, it’s a feature!
Access Address - 0x8E89BED6 : w 4 @--0
Packet Header ' , 00 e3 Oe ~ L
Advertising Address - xx:xx:xx:xxX!XX:XX
Length / Type - 0x01 / Flags (Optional) Length
Type - OxFF Company ID - 0x004C Apple Type
Apple Length | Variable Length Apple Data Apple Type
Apple Length Variable Length Apple Data
Apple BLE Frame Format
```

## Slide 58

##### Continuity Protocol Explained

_It’s not a bug, it’s a feature!_

###### Apple BLE Frame Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained — !t’snota bug, it’s a feature!
Access Address - 0x8E89BED6 ‘ w @--0
Packet Header ' , 00 e3 Ge ~ L
Advertising Address - xx:xx:xx:xxX!XX:XX
Length / Type - 0x01 / Flags (Optional) Length
Type - OxFF Company ID - 0x004C Apple Type
Apple Length | Variable Length Apple Data Apple Type
Apple Length Variable Length Apple Data
Apple BLE Frame Format
```

## Slide 59

##### Continuity Protocol Explained

_It’s not a bug, it’s a feature!_

Cut/Copy performed

###### Apple BLE Frame Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained — !t’snota bug, it’s a feature!
Access Address - 0x8E89BED6 ‘ w 4 @--0
Packet Header , nea ko €3 Ge ~ L
Advertising Address - xx:xx:xx:xxX!XX:XX
Length / Type - 0x01 / Flags (Optional) Length
Type - OxFF Company ID - 0x004C Apple Type Cut/Copy performed
Apple Length | Variable Length Apple Data Apple Type
Apple Length Variable Length Apple Data
Apple BLE Frame Format
```

## Slide 60

##### Con3nuity Protocol Explained

_It’s not a bug, it’s a feature!_

IV Seq Num

###### Apple BLE Frame Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained _ !t’snota bug, it’s a feature!
Access Address - 0x8E89BED6 ‘ w 4 @--0
Packet Header : otha ~ L
Advertising Address - xx:xx:xx:xxX!XX:XX
Length / Type - 0x01 / Flags (Optional) Length
Type - OxFF Company ID - 0x004C Apple Type IV Seq Num
Apple Length | Variable Length Apple Data Apple Type
Apple Length Variable Length Apple Data
Apple BLE Frame Format
```

## Slide 61

##### Continuity Protocol Explained

_It’s not a bug, it’s a feature!_

Auth Tag

###### Apple BLE Frame Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained — !t’snota bug, it’s a feature!
Access Address - 0x8E89BED6 ‘ w 4 @--0
Packet Header , » ~ L
Advertising Address - xx:xx:xx:xxX!XX:XX
Length / Type - 0x01 / Flags (Optional) Length Auth Tag
Type - OxFF Company ID - 0x004C Apple Type
Apple Length | Variable Length Apple Data Apple Type
Apple Length Variable Length Apple Data
Apple BLE Frame Format
```

## Slide 62

##### Con3nuity Protocol Explained

_It’s not a bug, it’s a feature!_

Encrypted Payload

###### Apple BLE Frame Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained _ !t’snota bug, it’s a feature!
Access Address - 0x8E89BED6 ‘ w 4 @--0
Packet Header ol vt ~ L
Advertising Address - xx:xx:xx:xxX!XX:XX
Length / Type - 0x01 / Flags (Optional) Length Encrypted Payload
Type - OxFF Company ID - 0x004C Apple Type
Apple Length | Variable Length Apple Data Apple Type
Apple Length Variable Length Apple Data
Apple BLE Frame Format
```

## Slide 63

##### Continuity Protocol Explained

_It’s not a bug, it’s a feature!_

Cons
Pros

###### Apple BLE Frame Format

Uses encryption Ivs sequential

## Slide 64

_It’s not a bug, it’s a feature!_

##### Con3nuity Protocol Explained

0xb Type 7: Proximity Pairing

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained _ !t’snota bug, it’s a feature!
Message
Type
AirDrop
Proximity
Pairing
Hey Siri
Magic
Switch
Handoff
Instant
Hotpot
Nearby
Action
Nearby Info
FindMy
Dec
Value
5
7
8
11
12
14
15
16
18
Hex
Value
0x05
0x07
0x08
Oxb
Oxc
Oxfe
Oxff
0x10
0x12
Type 7: Proximity
Pairing
```

## Slide 65

##### Con3nuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

Type 7: Proximity Pairing

###### Apple BLE Frame Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained _ !t’snota bug, it’s a feature!
Advertising Address - xx:xx:xx:xxX!XX:XX
Length / Type - 0x01 / Flags (Optional) Length
Type 7: Proximity
Pairing
Type - OxFF Company ID - 0x004C Apple Type
Apple Length | Variable Length Apple Data Apple Type
Apple Length Variable Length Apple Data
Apple BLE Frame Format
```

## Slide 66

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

Length =25

###### Apple BLE Frame Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained — !t’snota bug, it’s a feature!
pias (Belinea UaSeR enews 99 8f 01 00 64 cc 89 33 65 18 72 38 C9 3e te 39 3 e-r3->-9
Advertising Address - xx:xx:xx:xxX!XX:XX
Length =25
Length / Type - 0x01 / Flags (Optional) Length
Type - OxFF Company ID - 0x004C Apple Type
Apple Length | Variable Length Apple Data Apple Type
Apple Length Variable Length Apple Data
Apple BLE Frame Format
```

## Slide 67

##### Con3nuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

Airpods Prefix

###### Apple BLE Frame Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained _ !t’snota bug, it’s a feature!
_ 19fo1jof 20 23° v-[&-0-- L #
Access Address - 0x8E89BED6 99 8f @1 00 4 cc 89 33 65 18 72 sofa] or te 39 3 e-r3->-9
Advertising Address - xx:xx:xx:xx:!XX!XX
Length / Type - 0x01 / Flags (Optional) Length
Airpods Prefix
Type - OxFF Company ID - 0x004C Apple Type
Apple Length | Variable Length Apple Data Apple Type
Apple Length Variable Length Apple Data
Apple BLE Frame Format
```

## Slide 68

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

###### Apple BLE Frame Format

Device Model

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained — !t’snota bug, it’s a feature!
— 19 o1fef 20]23  v-[&-o-- L #
Access Address - 0x8E89BED6 99 8f 01 00 04 cc 89 33 65 18 72 33 eafor 2e]23 3 e-r3->-9
Advertising Address - xx:xx:xx:xx:!XX!XX
Length / Type - 0x01 / Flags (Optional) Length
Device Model
Type - OxFF Company ID - 0x004C Apple Type
Apple Length | Variable Length Apple Data Apple Type
Apple Length Variable Length Apple Data static const value_string airpods_device_vals[] = {
{ 0x0220, "AirPods 1" },
@x0f20, “AirPods 2" },
@x0e20, “AirPods Pro" },
@x0320, “Powerbeats3" },
0x0520, “BeatsXx" },
@x@620, “Beats Solo 3" },
@, NULL}
Apple BLE Frame Format
AAA AS
```

## Slide 69

##### Con3nuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

###### Apple BLE Frame Format

Device Model

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained _ !t’snota bug, it’s a feature!
— 19 o1fef 20]23  v-[&-o-- L #
Access Address - 0x8E89BED6 99 8f 01 00 04 cc 89 33 65 18 72 33 eafor 2e]23 3 e-r3->-9
Advertising Address - xx:xx:xx:xx:!XX!XX
Length / Type - 0x01 / Flags (Optional) Length
Device Model
Type - OxFF Company ID - 0x004C Apple Type
Apple Length | Variable Length Apple Data Apple Type
Apple Length Variable Length Apple Data static const value_string airpods_device_vals[] = {
{ 0x0220, "AirPods 1" },
@x0f20, “AirPods 2" },
@x0e20, “AirPods Pro" },
@x0320, “Powerbeats3" },
0x0520, “BeatsXx" },
@x@620, “Beats Solo 3" },
@, NULL}
Apple BLE Frame Format
AAA AS
```

## Slide 70

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

Status Codes Functional 👻 🤓 or spooky?

###### Apple BLE Frame Format

## Slide 71

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

🔋 Battery Levels

9 9 8 f
Left Airpod Right Airpod Is charging?  Case
(3bits)

###### Apple BLE Frame Format

## Slide 72

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

###### **Lid Open Count**

###### Apple BLE Frame Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained — !t’snota bug, it’s a feature!
TS Ree ~QSFROREDG 99 arferfee B4'cr ee" as 65 1872 a3 co Se le 39 wk. 8 @.ra.>-9
Advertising Address - xx:xx:xx:xx:!XX!XX
Length / Type - 0x01 / Flags (Optional) Length Lid Open Count
Type - OxFF Company ID - 0x004C Apple Type
Apple Length | Variable Length Apple Data Apple Type
Apple Length Variable Length Apple Data
Apple BLE Frame Format
```

## Slide 73

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

###### Apple BLE Frame Format

###### **Device Color**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained — !t’snota bug, it’s a feature!
peas Adee ONS FRIEERG 99 at 01 bop: ean oo 18 72 33 co 30 ie 30 ere 361328
Advertising Address - xx:xx:xx:xx:!XX!XX
Length / Type - 0x01 / Flags (Optional) Length Device Color
Type - OxFF Company ID - 0x004C Apple Type
Apple Length | Variable Length Apple Data Apple Type { 0x00, “White” },
Apple Length Variable Langtli ApplaData { @x01, "Black" },
{ @x@2, "Red" },
{ @x@3, "Blue" },
Apple BLE Frame Format { 0x04, "Pink" },
{ 0x@5, "Gray" },
{ @x06, "Silver" },
{ Qx@7, "Gold" },
{ @x08, "Rose Gold" },
{ @x09, "Space Gray" },
{ @x@A, "Dark Blue" },
{ @x@B, “Light Blue" },
{ @x@C, "Yellow" },
```

## Slide 74

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

###### **Airpods Suffix**

###### Apple BLE Frame Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained — !t’snota bug, it’s a feature!
sree MAb ~/ORSPROREDS 99 af 01 e0[ea] ec Benss 65 18 72 33 C8 3e ie 30 ee 361328
Packet Header 28 f5 al 79°EMb1 83 52 (--y---R
Advertising Address - xx:xx:xx:xx:!XX!XX
Length / Type - 0x01 / Flags (Optional) Length Airpods Suffix
Type - OxFF Company ID - 0x004C Apple Type
Apple Length | Variable Length Apple Data Apple Type
Apple Length Variable Length Apple Data
Apple BLE Frame Format
```

## Slide 75

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

###### **Encrypted Data**

###### Apple BLE Frame Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained — !t’snota bug, it’s a feature!
Access Add: Ox8E89BED6 dono ef os ov [eo 1 #
Packet Header 28 f5 al 79 ef|bi1 83 52 (--y---R
Advertising Address - xx:xx:xx:xx:!XX!XX
Length / Type - 0x01 / Flags (Optional) Length Encrypted Data
Type - OxFF Company ID - 0x004C Apple Type
Apple Length | Variable Length Apple Data Apple Type
Apple Length Variable Length Apple Data
Apple BLE Frame Format
```

## Slide 76

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

**CRC**

###### Apple BLE Frame Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained — !t’snota bug, it’s a feature!
sree MAb ~/ORSPROREDS 99 Sf 61 OD Ste TnEnay 65 18 72 33 C8 3e ie 30 ee 361328
Advertising Address - xx:xx:xx:xx:!XX!XX
Length / Type - 0x01 / Flags (Optional) Length
Type - OxFF Company ID - 0x004C Apple Type
Apple Length | Variable Length Apple Data Apple Type
Apple Length Variable Length Apple Data
Apple BLE Frame Format
```

## Slide 77

### `PLEASE TURN OFF YOUR BLUETOOTH`

## Slide 78

### `PLEASE TURN OFF YOUR BLUETOOTH`

seriously

please!!

## Slide 79

### `PLEASE TURN OFF YOUR BLUETOOTH`

seriously
please!!

## Slide 80

**`Demo`** 🔥

## Slide 81

🔥 **`Demo Backup`**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Demo Backup @
20220930-012514-ble.pcapng
File Edit View Go Capture Analyze Statistics Telephony Wireless Tools Help
imi C
Time Source Destinatic Length AirPods Status
64993 493... 6c:be :3f:b7:4 Tht: 56 Case: Both AirPods
64999 493... 6c:be 13Eibe a a 56 Case: Both AirPods
65005 493... 6c:be :b7: bt no 56 : Both AirPods
65023 493... 6c:be Shbrs4 1 56 Both AirPods
65025 493... 6c:be :3f:b7: fhitts— 56 : Both AirPods
65028 493... 6c:be : ttt 56 Case: Both AirPods
65036 493... 6c:be :b7: FoF EL 56 : Both AirPods
65038 493... 6c:be:04:3f:b7:4 Tift: 56 : Both AirPods
~ Advertising Data
~ Manufacturer Specific
Length: 30
Type: Manufacturer Specific (0xff)
~ Company ID: Apple, Inc. (0@x004c)
~ Type: AirPods (Proximity Pairing) (7)
Length: 25
AirPods Prefix: 01
AirPods Device Model: AirPods 2 (0x0f20)
AirPods Status: Both AirPods in ear (0x0b)
v AirPods Battery Levels & Charging Status
```

## Slide 82

Continuity Protocol Explained _It’s not a bug, it’s a feature!_

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained — !t’snota bug, it’s a feature!
'‘ AirTag stalking: Whatisit,andhow ~»,.
can | avoid it? "tt,
```

## Slide 83

##### Con3nuity Protocol Explained

_It’s not a bug, it’s a feature!_

0xb

Type 18: Find My

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained _ !t’snota bug, it’s a feature!
Message Dec Hex
Type Value Value 6u---b
Proximity 7 0x07 _
Pairing Type 18: Find My
Hey Siri 8 0x08
Magic 11 Oxb
Switch
Handoff 12 Oxc
Instant 14 Oxfe
Hotpot
Nearby 15 Oxff
Action
Nearby Info | 16 0x10
FindMy 18 0x12
```

## Slide 84

##### Continuity Protocol Explained

_It’s not a bug, it’s a feature!_

###### Type 18: Find My

###### Apple BLE Frame Format

## Slide 85

##### Con3nuity Protocol Explained

_It’s not a bug, it’s a feature!_

Type 18: Find My

###### Apple BLE Frame Format

###### Type 18: Find My

## Slide 86

##### Continuity Protocol Explained

_It’s not a bug, it’s a feature!_

Apple BLE Frame Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained
31
Access Address - 0x8E89BED6
Packet Header
Advertising Address - xx:xx:xx:xxX!XX:XX
Length / Type - 0x01 / Flags (Optional) Length
Type - OxFF Company ID - 0x004C Apple Type
Apple Length | Variable Length Apple Data Apple Type
Apple Length Variable Length Apple Data
Apple BLE Frame Format
It’s not a bug, it’s a feature!
6u b
6u b
Z ~%U>
```

## Slide 87

##### Con3nuity Protocol Explained

_It’s not a bug, it’s a feature!_

Apple BLE Frame Format

PAUSE: WHY ARE THESE DIFFERENT?!

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained _ !t’snota bug, it’s a feature!
Access Address - 0x8E89BED6 i i i i 6u b
Packet Header " zs *- U>
Advertising Address - xx:xx:xx:xxX!XX:XX
Length / Type - 0x01 / Flags (Optional) Length
Type - OxFF Company ID - 0x004C Apple Type
Apple Length ] Variable Length Apple Data Apple Type
Apple Length Variable Length Apple Data
6u---b
PAUSE: WHY ARE THESE DIFFERENT?!
```

## Slide 88

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

Nearby

Apple BLE Frame Format

PAUSE: WHY ARE THESE DIFFERENT?!

## Slide 89

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

Nearby
Apple BLE Frame Format
Separated

PAUSE: WHY ARE THESE DIFFERENT?!

## Slide 90

The State Machine of the AirTag

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ The State Machine of the AirTag
UnPaired
Disconnection
Connected
Connection
Separated
```

## Slide 91

The State Machine of the AirTag

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ The State Machine of the AirTag
Disconnection
Connected
Conneciion
Separated
```

## Slide 92

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

Nearby
Apple BLE Frame Format
Separated

PAUSE: WHY ARE THESE DIFFERENT?!

## Slide 93

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

Length = 2
Nearby
Apple BLE Frame Format
Separated

PAUSE: WHY ARE THESE DIFFERENT?!

## Slide 94

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

Length = 2 2 bytes
Nearby
Apple BLE Frame Format
Separated
PAUSE: WHY ARE THESE DIFFERENT?!

## Slide 95

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

Length = 2 2 bytes
Nearby
Apple BLE Frame Format
Separated
PAUSE: WHY ARE THESE DIFFERENT?!

## Slide 96

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

Length = 2 2 bytes
Nearby
Apple BLE Frame Format
Separated
Length = 25

PAUSE: WHY ARE THESE DIFFERENT?!

## Slide 97

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

Length = 2 2 bytes
Nearby
Apple BLE Frame Format
Separated
Length = 25  25 bytes

PAUSE: WHY ARE THESE DIFFERENT?!

## Slide 98

##### Con3nuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

Length = 2 2 bytes
Nearby
Apple BLE Frame Format
Separated
Length = 25  25 bytes

PAUSE: WHY ARE THESE DIFFERENT?!

## Slide 99

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

`
CRC
Length = 2 2 bytes
Nearby
Apple BLE Frame Format
`
CRC
Separated
Length = 25  25 bytes

PAUSE: WHY ARE THESE DIFFERENT?!

## Slide 100

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

`
CRC
Length = 2 2 bytes
Nearby

###### Apple BLE Frame Format

## Slide 101

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

`
CRC
Length = 2 2 bytes
Nearby

###### Apple BLE Frame Format

## Slide 102

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

` `
CRC
Length = 2 2 bytes
Nearby

###### Apple BLE Frame Format

## Slide 103

##### Continuity Protocol Explained

_It’s not a bug, it’s a feature!_

` `
CRC
Length = 2 2 bytes
Nearby
“Bacery Status”

###### Apple BLE Frame Format

## Slide 104

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

` `
CRC
Length = 2 2 bytes
Nearby
“Battery Status”
Apple BLE Frame Format

## Slide 105

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

` `
CRC
Length = 2 2 bytes
Nearby
“Battery Status”
Apple BLE Frame Format
7 6 5 4 3 2 1 0

## Slide 106

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

` `
CRC
Length = 2 2 bytes
Nearby
“Battery Status”
Apple BLE Frame Format
7 6 5 4 3 2 1 0
0 0 0 1 0 1  0 0

## Slide 107

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

` `
CRC
Length = 2 2 bytes
Nearby
“Battery Status”
Apple BLE Frame Format
7 6 5 4 3 2 1 0
0 0 0 1 0 1  0 0
Battery Battery Reserved Tracking Reserved Maintained Reserved Reserved

## Slide 108

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

` `
CRC
Length = 2 2 bytes
Nearby
“Battery Status”
Apple BLE Frame Format
7 6 5 4 3 2 1 0
0 0 0 1 0 1  0 0
Battery Battery Reserved Tracking Reserved Maintained Reserved Reserved
OLD tracking bit!

## Slide 109

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

` `
CRC
Length = 2 2 bytes
Nearby

“Battery Status”

Apple BLE Frame Format

**7 6 5 4 3 2 1 0** 0 0 0 1 0 1 0 0 Battery Battery Reserved Tracking Reserved Maintained Reserved Reserved

DISSECTOR CODE

OLD tracking bit!

## Slide 110

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

` `
CRC
Length = 2 2 bytes
Nearby
Old Left nibble Bit 5 tracking Bit 4 tracking New Left nibble
0 0000 0000 0
e 1110 1101 d
a 1010 1001 9
6 0110 0101 5
2 0010 0001 1

## Slide 111

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

` ` CRC **Length = 2** 2 bytes Nearby “Battery Status” Apple BLE Frame Format -> 0x00 -> 0xd4 **7 6 5 4 3 2 1 0** -> 0x94 0 0 0 1 0 1 0 0 -> 0x54 Battery Battery Reserved Tracking Reserved Maintained Reserved Reserved -> 0x14

Apple BLE Frame Format

###### DISSECTOR CODE

OLD tracking bit!

## Slide 112

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

` ` `
CRC
Length = 2 2 bytes
Nearby

###### Apple BLE Frame Format

## Slide 113

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

` ` `
CRC
Length = 2 2 bytes
Nearby
Public Key Bits

###### Apple BLE Frame Format

## Slide 114

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

` ` `
CRC
Length = 2 2 bytes
Nearby
Public Key Bits
Apple BLE Frame Format

## Slide 115

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

` ` `
CRC
Length = 2 2 bytes
Nearby
Public Key Bits
Apple BLE Frame Format
7 6 5 4 3 2 1 0

## Slide 116

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

` ` `
CRC
Length = 2 2 bytes
Nearby
Public Key Bits
Apple BLE Frame Format
7 6 5 4 3 2 1 0
0 0  0  0  0  0  1 0

## Slide 117

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

` ` `
CRC
Length = 2 2 bytes
Nearby
Public Key Bits
Apple BLE Frame Format
7 6 5 4 3 2 1 0
0 0  0  0  0  0  1 0
Reserved Reserved Reserved Reserved Reserved Reserved Pub Key Pub Key

## Slide 118

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

`
CRC
Separated
Length = 25  25 bytes

###### Apple BLE Frame Format

## Slide 119

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

`
CRC
Separated
Length  = 25

###### Apple BLE Frame Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained — !t’snota bug, it’s a feature!
Access Address - 0x8E89BED6 | i 6u : b
: %U>
Length / Type - 0x01 / Flags (Optional) Length
Type - OxFF Company ID - 0x004C Apple Type NN S ted
eparate
[ Apple Length | Variable Length Apple Data Apple Type Length =25 p
Apple Length Variable Length Apple Data
Apple BLE Frame Format
```

## Slide 120

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

`
`
CRC
Separated
Length  = 25

###### Apple BLE Frame Format

## Slide 121

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

`
`
CRC
Separated
Length  = 25
“Battery Status”

###### Apple BLE Frame Format

## Slide 122

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

`
`
CRC
Separated
Length  = 25
“Battery Status”

###### Apple BLE Frame Format

## Slide 123

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

`
`
CRC
Separated
Length  = 25
“Battery Status”
Apple BLE Frame Format
7 6 5 4 3 2 1 0
0 0 0 1 0 0  0 0
Battery Battery Reserved Tracking Reserved Maintained Reserved Reserved
Disconnected

## Slide 124

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

`
`
CRC
Separated
Length  = 25

###### Apple BLE Frame Format

## Slide 125

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

`
`
CRC
Separated
Length  = 25

###### Apple BLE Frame Format

## Slide 126

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

`
`
CRC
Separated
Length  = 25
Bytes 6-27 of the public key

###### Apple BLE Frame Format

## Slide 127

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

`
`
CRC
Separated

###### Apple BLE Frame Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained — !t’snota bug, it’s a feature!
Access Address - 0x8E89BED6 6u : b
%U>
Packet Header T L b
Length / Type - 0x01 / Flags (Optional) Length
Type - OxFF Company ID - 0x004C Apple Type NN
; Separated
Apple Length | Variable Length Apple Data Apple Type
Apple Length Variable Length Apple Data
Apple BLE Frame Format
```

## Slide 128

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

`
` `
CRC
Separated

###### Apple BLE Frame Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained — !t’snota bug, it’s a feature!
Access Address - 0x8E89BED6 6u : b
%U>
Packet Header T L b
Length / Type - 0x01 / Flags (Optional) Length
Type - OxFF Company ID - 0x004C Apple Type NN
; Separated
Apple Length | Variable Length Apple Data Apple Type
Apple Length Variable Length Apple Data
Apple BLE Frame Format
```

## Slide 129

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

`
` `
CRC
Separated
“Public Key Bits"
Apple BLE Frame Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained — !t’snota bug, it’s a feature!
Access Address - 0x8E89BED6 6u : b
%U>
Packet Header T L b
Length / Type - 0x01 / Flags (Optional) Length
Type - OxFF Company ID - 0x004C Apple Type NN
; Separated
Apple Length | Variable Length Apple Data Apple Type
Apple Length Variable Length Apple Data
Apple BLE Frame Format
```

## Slide 130

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

`
` `
CRC
Separated
“Public Key Bits"
Apple BLE Frame Format
7 6 5 4 3 2 1 0
0 0 0 0 0 0 1 0
Reserved Reserved Reserved Reserved Reserved Reserved Pub Key Pub Key

## Slide 131

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

`
` `
CRC
Separated

###### Apple BLE Frame Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained — !t’snota bug, it’s a feature!
Access Address - 0x8E89BED6 6u : b
%U>
Packet Header T L b
Length / Type - 0x01 / Flags (Optional) Length
Type - OxFF Company ID - 0x004C Apple Type NN
; Separated
Apple Length | Variable Length Apple Data Apple Type
Apple Length Variable Length Apple Data
Apple BLE Frame Format
```

## Slide 132

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

`
` ` `
CRC
Separated

###### Apple BLE Frame Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained — !t’snota bug, it’s a feature!
Access Address - 0x8E89BED6 6u : b
%U>
Packet Header T L b
Length / Type - 0x01 / Flags (Optional) Length
Type - OxFF Company ID - 0x004C Apple Type NN
; Separated
Apple Length | Variable Length Apple Data Apple Type
Apple Length Variable Length Apple Data
Apple BLE Frame Format
```

## Slide 133

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

`
` ` `
CRC
Hint
Separated

###### Apple BLE Frame Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained
7
8
15 16
23 24
31
Access Address - 0x8E89BED6
Packet Header
Advertising Address - xx:xx:xx:xxX!XX:XX
Length / Type - 0x01 / Flags (Optional) Length
Type - OxFF Company ID - 0x004C Apple Type
[ Apple Length | Variable Length Apple Data Apple Type
Apple Length
Variable Length Apple Data
Apple BLE Frame Format
It’s not a bug, it’s a feature!
12 filo] fo 62
NL Separated
```

## Slide 134

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

`
` ` `
CRC
Hint
Separated
(also related to public
key)

###### Apple BLE Frame Format

## Slide 135

##### Continuity Protocol Explained

_It’s not a bug, it’s a feature!_

# ?

## Slide 136

##### Continuity Protocol Explained

_It’s not a bug, it’s a feature!_

In 5 Minutes

## Slide 137

##### Continuity Protocol Explained

_It’s not a bug, it’s a feature!_

No GPS!

## Slide 138

##### Continuity Protocol Explained

_It’s not a bug, it’s a feature!_

No GPS!

..so how does it work?

## Slide 139

##### Continuity Protocol Explained

_It’s not a bug, it’s a feature!_

**<u>Encryption 101</u>** PUBLIC KEY = encrypt PRIVATE KEY = decrypt

## Slide 140

Continuity Protocol Explained _It’s not a bug, it’s a feature!_

## Slide 141

##### Continuity Protocol Explained

_It’s not a bug, it’s a feature!_

airtag

## Slide 142

_It’s not a bug, it’s a feature!_

##### Continuity Protocol Explained

###### No GPS but… BLUETOOTH!

airtag

## Slide 143

_It’s not a bug, it’s a feature!_

##### Continuity Protocol Explained

No GPS but… BLUETOOTH!

airtag

## Slide 144

_It’s not a bug, it’s a feature!_

##### Continuity Protocol Explained

No GPS but… BLUETOOTH!

airtag

## Slide 145

_It’s not a bug, it’s a feature!_

##### Continuity Protocol Explained

No GPS but… BLUETOOTH!

0x12345678910ABCDEFABCDEF

airtag

## Slide 146

##### Continuity Protocol Explained

_It’s not a bug, it’s a feature!_

No GPS but… BLUETOOTH!

0x12345678910ABCDEFABCDEF

Notional key PubKey

airtag

## Slide 147

##### Continuity Protocol Explained

_It’s not a bug, it’s a feature!_

No GPS but… BLUETOOTH!

0x12345678910ABCDEFABCDEF

Notional key PubKey P224 ELLIPTIC CURVE PUBLIC KEY 224 bits in PubKey = 28 byte key

airtag

## Slide 148

##### Continuity Protocol Explained

_It’s not a bug, it’s a feature!_

No GPS but… BLUETOOTH!

airtag

## Slide 149

_It’s not a bug, it’s a feature!_

##### Continuity Protocol Explained

No GPS but… BLUETOOTH!

airtag

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained — !t’snota bug, it’s a feature!
No GPS but... BLUETOOTH! 6)
6 ° PubKey
```

## Slide 150

##### Continuity Protocol Explained

_It’s not a bug, it’s a feature!_

Apple Server

No GPS but… BLUETOOTH!

airtag

## Slide 151

##### Continuity Protocol Explained

_It’s not a bug, it’s a feature!_

Apple Server

No GPS but… BLUETOOTH!

airtag

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained — !t’snota bug, it’s a feature!
Apple Server
»
No GPS but... BLUETOOTH! 0
0G ° PubKey
airtag
```

## Slide 152

##### Continuity Protocol Explained

_It’s not a bug, it’s a feature!_

Apple Server

No GPS but… BLUETOOTH!

airtag

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ Continuity Protocol Explained — !t’snota bug, it’s a feature!
Apple Server
No GPS but... BLUETOOTH! 0
0G ° PubKey
airtag
```

## Slide 153

##### Continuity Protocol Explained

_It’s not a bug, it’s a feature!_

Apple Server

No GPS but… BLUETOOTH!

airtag

Can download and unlock with Private Key

## Slide 154

##### Continuity Protocol Explained

_It’s not a bug, it’s a feature!_

If at 3:00pm on Saturday, the AirTag was nearby to a user who claimed they were at the Hilton
Hotel, then the AirTag must have also been at  or near the Hilton Hotel at the same time.
NOTE!!
This is not
live
tracking

## Slide 155

##### What the heck is P224- ECIES?!

● Let’s take a deep dive into encryption (photo cred @replover4eva)

## Slide 156

##### P-224 Encryption in General

- Recall the Diffie Hellman key exchange, and the ability to generate a shared secret

- P-224 Elliptic Curve Diffie Hellman (ECDH) is similar, with more parameters

The “domain parameters” are already agreed upon ( _p, a, b, G, n, h_ ) and the curve is represented by the formula:

- **`y`**<sup>**`2`**</sup> **`= x`**<sup>**`3`**</sup> **`-3x+18958286285566608000408668544493926415504680968679321075787234672564`** and ( _p, a, b, G, n, h_ ) are defined as follows:

- **`p = 26959946667150639794667015087019630673557916260026308143510066298881 a = -3`**

- **`b = 18958286285566608000408668544493926415504680968679321075787234672564 G= (19277929113566293071110308034699488026831934219452440156649784352033, 19926808758034470970197974370888749184205991990603949537637343198772) n = 26959946667150639794667015087019625940457807714424391721682722368061 h=1`**

(FIPS 186-4 Digital Standard)

## Slide 157

##### P-224 ECIES

- “Elliptic Curve Integrated Encryption Scheme”

- Supposed to be Even More Secure™ and protect against chosen-plaintext and chosen-ciphertext attacks

- ECIES integrates additional features such as message authentication codes (MAC) and key derivation functions (KDF) into the protocol, as well as a symmetric encryption scheme for faster encryption times

- • This is introduced in a 2009 paper (Daniel R. L. Brown. Standards for Efficient Cryptography 1 (SEC 1). 2009. https://www.secg.org/sec1-v2.pdf)

- In the AirTag implementation, the KDF used is ANSI-X9.63-KDF and the MAC scheme used is SHA-256. The symmetric key scheme ENC is AES-128-GCM.

- It is important to note that given an elliptic curve and an x-coordinate on that curve, the y-coordinate can be trivially calculated, so usually only the x-coordinate is shared in practical implementations

## Slide 158

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

The AirTag and owner device must collaboratively generate a 28 byte Master public key P, (comprised of key pair public p0 and private d0) as well a 32 byte key Secret Key Separated (SKS) _(if you want to know more, there’s bonus slides at the end, but basically, they use math to each generate P without either actually sending P over the channel, much like most shared secret generation)_

The master key P and SKS are used to generate a derivative key PWi, defined by key pairs public pi and private di

Every 15 minutes, a new key pair public pi and private di are generated, and the new pi value is what is beaconed

## Slide 159

##### All the math

```
1) ephemeral key is generated (extraction)
SKSi = KDF(SKSi-1, “update”, 32)
```

```
2)expansion of key pair
```

**`(ui , vi) = KDF(SKSi , “diversify”, 72` )**

```
3) Reduce into P-224 valid scalars
```

**`ui = ui(mod q-1) + 1` (** where q is the order of the base point G of the P-224 elliptic curve.) **`vi = vi(mod q-1) + 1`**

```
4)Generate pi  and di
di = (d0*ui) + vi
```

```
pi = (di *G )
```

```
Where * is the dot product,  G is the point generator and the original public key
is (d0,p0)
```

## Slide 160

##### Continuity Protocol Explained

_It’s not a bug, it’s a feature!_

•
The Finder device also creates its own ephemeral key
pairs on the P-224 Curve
•
When it receives the public key pi, it uses ECDH to
compute another shared secret –> SharedKeyFinder
SKF
•
It uses the KDF to compute an ephemeral key
SKF’ = KDF(SKF, “update”, 32)
•
The first 16 bytes of SKF’ become a 16 byte
encryption key e’ for AES-GCM. The last 16 bytes of
SKF’ become the initialization vector (IV). This is an
implementation of ECIES  (from TU
Darmstadt paper)

## Slide 161

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

- The Apple Servers store the locations reports as key value pairs ( SHA256(pi), 88 byte location report)

- • You can request a location report as long as you know the hash

•
•
•

- The owner device collaboratively generated (p0,d0), so calculating pi and SHA256(pi) is trivial.

- Also, because the owner device can recalculate all of the private keys from the airtag as well, it will calculate the corresponding private key di for public key pi, then using the ephemeral public key , the owner can calculate the shared secret SKF. Using the known KDF function, the owner can then calculate SKF’, which becomes e’ and IV, and was used to AES- 128 encrypt the original payload, and since AES is symmetric, this will decrypt that location report as well.

## Slide 162

##### Bluetooth Limitations

- Small Packet Size vs Strong Encryption Need

   - MTU recommendation is 512 bytes (that’s including header info and payload)

   - In practice this is much smaller! And for Bluetooth low energy EVEN smaller (max recommended payload only 27 bytes)

   - BUT we want to use strong encryption, and a P-224 key of 224 bits is equivalent to an RSA key of 2048 bits

   - So Apple does something a little creative here….

## Slide 163

##### Continuity Protocol Explained

###### _It’s not a bug, it’s a feature!_

`
CRC
Separated
Length = 25  25 bytes

###### Apple BLE Frame Format

## Slide 164

##### Creative Key Storage

_It’s not a bug, it’s a feature!_

Separated

###### Apple BLE Frame Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
é Creative Key Storage
90
98
54
c6
3T
0 7
90
85
Q7
7a
Q2
18
d7
14
23
3e
00
Ob
d9
18
d5
15 16
Tb
17
ie
60
39
90
Oa
ff
35
6a
00
16
Ac
3e
23 24
31
Access Address - 0x8E89BED6
Packet Header
Advertising Address - xx:xx:xx:xx:xXx:xx
Length / Type - 0x01 / Flags (Optional)
Length
Type - OxFF
Company ID - 0x004C
Apple Type
Apple Length
Variable Length Apple Data
Apple Type
Apple Length
Variable Length Apple Data
Apple BLE Frame Format
It’s not a bug, it’s a feature!
separated
```

## Slide 165

##### Creative Key Storage

_It’s not a bug, it’s a feature!_

Separated

###### Apple BLE Frame Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
é Creative Key Storage
90
98
54
c6
3T
0 7
90
85
Q7
7a
Q2
18
d7
14
23
3e
00
Ob
d9
18
d5
15 16
Tb
17
ie
60
39
90
Oa
ff
35
6a
00
16
Ac
3e
23 24
31
Access Address - 0x8E89BED6
Packet Header
Advertising Address - xx:xx:xx:xx:xXx:xx
Length / Type - 0x01 / Flags (Optional)
Length
Type - OxFF
Company ID - 0x004C
Apple Type
Apple Length
Variable Length Apple Data
Apple Type
Apple Length
Variable Length Apple Data
Apple BLE Frame Format
It’s not a bug, it’s a feature!
separated
```

## Slide 166

##### Creative Key Storage

_It’s not a bug, it’s a feature!_

Separated

###### Apple BLE Frame Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
é Creative Key Storage
90
98
54
c6
3T
0 7
90
85
Q7
7a
Q2
18
d7
14
23
3e
00
Ob
d9
18
d5
15 16
Tb
17
ie
60
39
90
Oa
ff
35
6a
00
16
Ac
3e
23 24
31
Access Address - 0x8E89BED6
Packet Header
Advertising Address - xx:xx:xx:xx:xXx:xx
Length / Type - 0x01 / Flags (Optional)
Length
Type - OxFF
Company ID - 0x004C
Apple Type
Apple Length
Variable Length Apple Data
Apple Type
Apple Length
Variable Length Apple Data
Apple BLE Frame Format
It’s not a bug, it’s a feature!
separated
```

## Slide 167

##### Creative Key Storage

28 byte key

_It’s not a bug, it’s a feature!_

Separated

Bytes 0-5

###### Apple BLE Frame Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
é Creative Key Storage
28 byte key
90
98
54
c6
3T
0 7
90
85
Q7
7a
Q2
18
d7
14
23
3e
00
Ob
d9
18
d5
15 16
Tb
17
ie
60
39
90
Oa
ff
35
6a
00
16
Ac
3e
23 24
31
Access Address - 0x8E89BED6
Bytes 0-5
Packet Header
Advertising Address - xx:xx:xx:xx:xx:xx
Length / Type - 0x01 / Flags (Optional)
Length
Type - OxFF
Company ID - 0x004C
Apple Type
Apple Length
Variable Length Apple Data
Apple Type
Apple Length
Variable Length Apple Data
Apple BLE Frame Format
It’s not a bug, it’s a feature!
separated
```

## Slide 168

##### Creative Key Storage

28 byte key

_It’s not a bug, it’s a feature!_

Separated

Bytes 0-5

Apple BLE Frame Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
é Creative Key Storage
28 byte key
90
1 98
2 54
c6
3T
0 7
90
85
Q7
7a
Q2
18
d7
14
23
3e
00
Ob
d9
18
d5
15 16
Tb
17
ie
60
39
00
Oa
Ff
35
6a
00
16
Ac
3e
23 24
31
Access Address - 0x8E89BED6
Bytes 0-5
Packet Header
Advertising Address - xx:xx:xx:xx:xx:xx
Length / Type - 0x01 / Flags (Optional)
Length
Type - OxFF
Company ID - 0x004C
Apple Type
Apple Length
Variable Length Apple Data
Apple Type
Apple Length
Variable Length Apple Data
Apple BLE Frame Format
It’s not a bug, it’s a feature!
separated
```

## Slide 169

##### Creative Key Storage

28 byte key

_It’s not a bug, it’s a feature!_

Separated

Bytes 0-5

Apple BLE Frame Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
é Creative Key Storage
28 byte key
90
1 98
2 54
c6
3T
0 7
90
85
Q7
7a
Q2
18
d7
14
23
3e
00
Ob
d9
18
d5
15 16
Tb
17
ie
60
39
00
Oa
Ff
35
6a
00
16
Ac
3e
23 24
31
Access Address - 0x8E89BED6
Bytes 0-5
Packet Header
Advertising Address - xx:xx:xx:xx:xx:xx
Length / Type - 0x01 / Flags (Optional)
Length
Type - OxFF
Company ID - 0x004C
Apple Type
Apple Length
Variable Length Apple Data
Apple Type
Apple Length
Variable Length Apple Data
Apple BLE Frame Format
It’s not a bug, it’s a feature!
separated
```

## Slide 170

##### Creative Key Storage

28 byte key

_It’s not a bug, it’s a feature!_

Separated

Bytes 0-5

Apple BLE Frame Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
é Creative Key Storage
90
1 98
2 54
c6
3T
28 byte key
15 16
Tb
17
ie
60
39
08 oO
Oa 16
fF Ac
35 3e
6a
23 24
31
Access Address - 0x8E89BED6
Bytes 0-5
Packet Header
Advertising Address - xx:xx:xx:xx:xx:xx
Length / Type - 0x01 / Flags (Optional)
Length
Type - OxFF
Company ID - 0x004C
Apple Type
Apple Length
Variable Length Apple Data
Apple Type
Apple Length
Variable Length Apple Data
Apple BLE Frame Format
It’s not a bug, it’s a feature!
separated
```

## Slide 171

##### Creative Key Storage

28 byte key

_It’s not a bug, it’s a feature!_

Separated

Bytes 0-5 Bytes 6-27

Apple BLE Frame Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
é Creative Key Storage
90
1 98
2 54
c6
3T
28 byte key
90
85
Q7
7a
Q2
18
d7
14
23
3e
00
@b
dg
18
d5
15 16
Tb
17
le
60
39
08 oO
Oa 16
fF Ac
35 3e
6a
23 24
31
Access Address - 0x8E89BED6
Packet Header
Advertising Address - xx:xx:xx:xx:xx:xx
Length / Type - 0x01 / Flags (Optional)
Type - OxFF
Company ID - 0x004C
Apple Length
Variable Length Apple Data
Bytes 0-5
Bytes 6-27
Length
Apple Type
Apple Type
Apple Length
Variable Length Apple Data
Apple BLE Frame Format
It’s not a bug, it’s a feature!
separated
```

## Slide 172

##### Creative Key Storage

28 byte key

_It’s not a bug, it’s a feature!_

`

` Hint

Separated

Bytes 0-5 Bytes 6-27

Apple BLE Frame Format

## Slide 173

##### Creative Key Storage

28 byte key

_It’s not a bug, it’s a feature!_

` Bytes 0-5 Bytes 6-27

` ` ` Hint

Separated

Apple BLE Frame Format

## Slide 174

##### Creative Key Storage

_It’s not a bug, it’s a feature!_

28 byte key ` ` ` ` Hint Separated Bytes 0-5 Bytes 6-27 **d 9** 1101 1001

###### Apple BLE Frame Format

## Slide 175

##### Creative Key Storage

_It’s not a bug, it’s a feature!_

28 byte key ` ` ` ` Hint Public Key Bits Separated Bytes 0-5 Bytes 6-27 **d 9** 110` 1 1001

###### Apple BLE Frame Format

## Slide 176

##### Creative Key Storage

28 byte key

_It’s not a bug, it’s a feature!_

`
`
` `
Hint
Public Key
Bits Separated
Bytes 0-5
Bytes 6-27
d 9
110` 1 1001
à0010à10à1001à9
Final PubKey:

Apple BLE Frame Format

## Slide 177

##### Creative Key Storage

28 byte key

_It’s not a bug, it’s a feature!_

` ` ` ` Hint Public Key Bits Separated Bytes 0-5 Bytes 6-27 **d 9** 110` 1 1001

Apple BLE Frame Format

à0010à10à1001à9 Final PubKey: 991407543e55f962a3958e

991407543e55f962a3958e c67a231860353ee746f8cb2771cfbd933f

## Slide 178

##### References

[1] Hardwick, Tim. “Apple Announces AirTag Tracking Devices Starting at $29 Each. _MacRumors,_ 20 Apr. 2021, https://www.macrumors.com/2021/04/20/apple-unveils-airtags-tracking-devices/.

[2] “AirTag.” _Apple,_ Apr. 2021, https://www.apple.com/airtag/.

- [3] “Create Innovative Accessories.” _Apple._ 2021,https://mfi.apple.com/.

[4] Goldheart, Sam. “AirTag Teardown: Yeah, This Tracks” _IFixit,_ 1 May 2021, https://www.ifixit.com/News/50145/airtagteardown-part-one-yeah-this-tracks.

- [5] “NRF52832.” Nordic Semiconductor, https://www.nordicsemi.com/products/nrf52832.

- [6] NIST. “Digital Signature Standard (DSS).” _Federal Information Processing Standards Publication_ , 2013, https://doi.org/10.6028/nist.fips.186-4.

[7] Guillaume Celosia, Mathieu Cunche. Saving Private Addresses: An Analysis of Privacy Issues in the Bluetooth-Low-Energy Advertising Mechanism. MobiQuitous 2019 - 16th EAI International Conference on Mobile and Ubiquitous Systems: Computing, Networking and Services, Dec 2019, Houston, United States. pp.1-10, ff10.1145/3360774.3360777ff. ffhal-02394629f [8] Afaneh, Mohammad. “Bluetooth Addresses & Privacy in Bluetooth Low Energy.” _Novel Bits_ , 6 Apr. 2020, https://novelbits.io/Bluetooth-address-privacy-ble/.

- [9] _Great Scott Gadgets_ , https://greatscottgadgets.com/ubertoothone/.

- [10] Bluetooth SIG. Bluetooth Core Specification Version 5.2. Tech. rep. 2019.

[11] Heinrich, Alexander, et al. “Who Can _Find My_ Devices? Security and Privacy of Apple’s Crowd-Sourced Bluetooth Location Tracking System.” _Proceedings on Privacy Enhancing Technologies_ , vol. 2021, no. 3, 2021, pp. 227–245., https://doi.org/10.2478/popets-2021-0045.

## Slide 179

##### More References

[12] “Find My Network Accessory Specification.” _Apple._ Version Release R1. 2020. url: https://developer.apple.com/ find-my/.

[13] Kassem Fawaz, Kyu-Han Kim, and Kang G Shin. 2016. Protecting Privacy of BLE Device Users. In 25th USENIX Security Symposium ( _USENIX Security 16_ ). 1205–1221.

[14] Celosia, Guillaume, and Mathieu Cunche. “Discontinued Privacy: Personal Data Leaks in Apple BluetoothLow-Energy Continuity Protocols.” _Proceedings on Privacy Enhancing Technologies_ , vol. 2020, no. 1, 2020, pp. 26–46., https://doi.org/10.2478/popets-2020-0003.

[15] “Throughput with Bluetooth Low Energy Technology.” Version 4.0 Bluetooth API Documentation. _Silicon Labs_ , June 2022, https://docs.silabs.com/Bluetooth/4.0/general/system-and- performance/throughput-withBluetooth-low-energy-technology.

[16] Derhgawen, Ashish. “Maximizing BLE Throughput Part 4: Everything You Need to Know.” _Punch Through_ , 16 Nov. 2020, https://punchthrough.com/ble-throughput-part-4/.

[17] “Size Considerations for Public and Private Keys.” Documentation, _IBM_ , 27 May 2021, https://www.ibm.com/docs/en/zos/2.4.0?topic=certificates-size-considerations-public-private-keys. [18] Jeremy Martin, Douglas Alpuche, Kristina Bodeman, Lamont Brown, Ellis Fenske, Lucas Foppe, Travis Mayberry, Erik Rye, Brandon Sipes, and Sam Teplov. “Handoff All Your Privacy: A Review of Apple’s Bluetooth Low Energy Implementation.” In: (2019). doi: 10.2478/popets-2019- 0057.

## Slide 180

##### More References

[18] Douglas Alpuche, Kristina Bodeman, Lamont Brown, Ellis Fenske, Lucas Foppe, Travis Mayberry, Erik Rye, Brandon Sipes, and Sam Teplov. “Handoff All Your Privacy: A Review of Apple’s Bluetooth Low Energy Implementation.” In: (2019). doi: 10.2478/popets-2019- 0057.

[19] Travis Mayberry, Ellis Fenske, Dane Brown, Jeremy Martin, Christine Fossaceca, Erik C. Rye, Sam Teplov, and Lucas Foppe. 2021. Who Tracks the Trackers? Circumventing Apple’s Anti- Tracking Alerts in the Find My Network. In Proceedings of the 20th Workshop on Privacy in the Electronic Society (WPES ’21), November 15, 2021, Virtual Event, Republic of Korea. _ACM_ , New York, NY, USA, 6 pages. https://doi.org/10.1145/3463676.3485616

[20] Daniel R. L. Brown. Standards for Efficient Cryptography 1 (SEC 1). 2009. https://www.secg.org/sec1-v2.pdf [21] “Apple Platform Security.” _Apple._ 2020. url: https : / / support.apple.com/guide/security/ (Alternate Link).https://github.com/0xmachos/Apple-Platform-Security-Guides/blob/master/2020- spring-apple-platformsecurity-guide.pdf

[22] _Wireshark · Go Deep._ , https://www.wireshark.org/.

[25] Diffie and M. E. Hellman, “New Directions in Cryptography,” IEEE Transactions on Information Theory, Vol. 22, No. 6, 1976, pp. 644-654. https://ee.stanford.edu/~hellman/publications/24.pdf

[26] “Elliptic-Curve Diffie–Hellman.” _Wikipedia_ , Wikimedia Foundation, 9 Nov. 2022,

https://en.wikipedia.org/wiki/Elliptic-curve_Diffie%E2%80%93Hellman.

[27] “P-224.” _Standard Curve Database_ , 2020, https://neuromancer.sk/std/nist/P-224.

## Slide 181

##### More References

[28] “Chapter 3 - An Introduction To Cryptography”.Editor(s): Dale Liu, Max Caceres, Tim Robichaux, Dario V. Forte, Eric S. Seagren, Devin L. Ganger, Brad Smith, Wipul Jayawickrama, Christopher Stokes, Jan Kanclirz, Next Generation SSH2 Implementation,Syngress,2009,

Pages 41-64,https://doi.org/10.1016/B978-1-59749-283-6.00003-9. (https://www.sciencedirect.com/topics/computerscience/plaintext-attack)

[29] Ryan K.L. Ko, Kim-Kwang Raymond Choo,Chapter 1 -The Cloud Security Ecosystem.Syngress, 2015,Pages 1-14,https://doi.org/10.1016/B978-0-12-801595-7.00001-X. (https://www.sciencedirect.com/topics/computerscience/el-gamal)

[30] NIST. “Digital Identity Guidelines”. _Special Publication_ , 2017, https://doi.org/10.6028/NIST.SP.800-63b [31] Abdel Hakeem SA, Kim H. Centralized Threshold Key Generation Protocol Based on Shamir Secret Sharing and HMAC Authentication. Sensors (Basel). 2022 Jan 3;22(1):331. doi:

10.3390/s22010331

[32] Alexander Heinrich, Niklas Bittner, and Matthias Hollick. 2022. AirGuard - Protecting Android Users from Stalking Attacks by Apple Find My Devices.

[33] NIST. “Recommendation for Key-Derivation Methods in Key-Establishment Schemes”. _Special Publication_ , 2018, https://doi.org/10.6028/NIST.SP.800-56Cr1

[34] Ireland, David. “AES-GCM Authenticated Encryption.” _CryptoSys PKI Pro Manual_ , DI Management Services Pty Limited, 10 Sept. 2022, https://www.cryptosys.net/pki/manpki/pki_aesgcmauthencryption.html.

[35] Daniel J. Bernstein and Tanja Lange. SafeCurves: choosing safe curves for elliptic-curve cryptography. 1 Jan 2017. https://safecurves.cr.yp.to.

[36] Giry, Damien. “Cryptographic Key Length Recommendation.” _BlueKrypt_ , 24 May 2020, https://www.keylength.com/en/4/.

## Slide 182

```
Questions?
```

<u>christine@herhaxpodcast.com</u> @x71n3 on Twitter

## Slide 183

##### AirTag + Owner Device Key Exchange

- Assume an a priori securely established Bluetooth communications channel ( During the Bluetooth pairing procedure, the two devices use an a priori Apple server key (written into the firmware of both devices) [12]to encrypt these initial transmissions )

- Collaborative Key Generation Steps (From the Original FindMy Specification)

   - “AirTag Accessory Alice” must generate a P-224 scalar _s_ and a random 32 byte value _r_ , then concatenates _s_ with _r_ , and calculates a value _c1_ by calculating the SHA-256 of _s_ concatenated with _r_ .

   - “Owner Device Bob” also generates a P-224 scalar, _s’_ , and a random 32 byte value _r’_ . However, Bob then uses generational point _G_ to generate _S’_ , where _S’ = G * s’_ , where * indicates the dot product. Note, this is quite similar to the calculation for Bob’s public key in the section above. Bob’s iDevice can then send _c2_ which is a set containing {S’, r’}.

   - Now, S’ is also point on the curve P-224, because it was created from G, the generational point. AirTag Accessory Alice verifies this. The AirTag will be the first to compute the Master public key P. Using S’ from the Owner device, the formula is P = S’ +s * G. Remember, P is never sent over the channel, so instead, the AirTag sends c3 = {s, r}

## Slide 184

##### AirTag + Owner Device Key Exchange (cont)

- Collaborative Key Generation Steps (cont)

   - Next, the owner device does a bit of verification, first, verifying that s is a valid P-224 scalar, and then computing the SHA-256 hash of s concatenated with r. The AirTag sent this value initially with c1, so the owner device compares its own calculation to c1, and aborts if they are not equal. Now, the owner device can independently compute the Master key P with the formula P = S’ +s * G and the private key d with the formula d = s +s’(mod q), where q is the order of the base point G of the P-224 elliptic curve.

   - At this point, the AirTag and the owner device (Alice and Bob) each have generated P without sending it over the channel. Using P, each can independently compute SKN and SKS as the 64 byte output of the KDF function ANSI-X9.63-KDF(x(P), r concatenated with r’). The SKN is the first 32 bytes of this value and SKS the last 32 bytes.
