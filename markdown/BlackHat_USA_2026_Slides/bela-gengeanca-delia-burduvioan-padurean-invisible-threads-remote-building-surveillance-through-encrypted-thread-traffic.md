---
title: "Invisible Threads Remote Building Surveillance Through Encrypted Thread Traffic Analysis"
speakers: ["Bela Genge", "Anca Delia Burduv", "Ioan Padurean"]
conference: "Black Hat"
conference_full: "Black Hat USA 2026"
edition: "USA"
year: 2026
source_pdf: "BlackHat_USA_2026_Slides/Bela Genge&Anca Delia Burduv&Ioan Padurean_Invisible Threads Remote Building Surveillance Through Encrypted Thread Traffic Analysis.pdf"
pages: 81
sha256: "97de04b7e66a82e9da13f04a724e4222bb8f920fcd9af24c3a65e653906b78f9"
text_chars: 24523
ocr_pages: 26
has_ocr: true
redacted_secrets: 0
ocr_confidence: 90.9
ocr_unreliable_blocks: 0
vision_verified_blocks: 1
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:29:51Z"
---
# Invisible Threads Remote Building Surveillance Through Encrypted Thread Traffic Analysis

**Speakers:** Bela Genge, Anca Delia Burduv, Ioan Padurean  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/Bela Genge&Anca Delia Burduv&Ioan Padurean_Invisible Threads Remote Building Surveillance Through Encrypted Thread Traffic Analysis.pdf` (81 pages)


## Slide 1

## Invisible Threads: Remote building surveillance through encrypted Thread traffic analysis

Speakers: Béla Genge, Anca Delia Burduv Contributor: Ioan Pădurean

## Slide 2

##### OUR PREVIOUS RESEARCH ON MATTER IOT

- Brand new standard, adopted by **600+ major industry players** (Google, Apple, Samsung, Amazon, etc.)

- We found several design flaws and vulnerabilities in the Matter IoT standard

- Enabled effective DoS, device identification

- • Exploit **required Wi-Fi access**

Initiator

Responder RandomI, SessionIdI, destId, EphPubKeyI [, ...] Sigma1 No replay protection

2

## Slide 3

##### OUR LATEST BLACK HAT TALK: INFO LEAKS

- We accidentally found that Matter's encrypted traffic **leaks information** about devices

- Attackers can **accurately profile devices** on the network, conduct spying and profiling activities, **user behavior identification** , which can lead to other malicious activities

- Exploit **required Wi-Fi access**

Encrypted packets

Communication patterns
Device +  user behavior
identification

3

## Slide 4

##### NATURAL CURIOSITY: THIS RESEARCH

**Application** layer

Communication / **transport** layer

**34, 73, 42** , **34, 59, 67** , **34, 73, 42** , **34, 59, 67**

**Application** layer patterns

**34, 73, 42** , **34, 59, 67** , **34, 73, 42** , **34, 59, 67**

Is there protection to **prevent** further **information leakage and exploitation** ?

**Transport** layer cryptographic protection

4

## Slide 5

INNOCENT BYSTANDERS


> Recovered by OCR — confidence 87/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
INNOCENT BYSTANDERS
=
[—]
_
_
=
=
2526
```

## Slide 6

##### POSSIBLE EXPLOITATION

Information
leakage?


> Recovered by OCR — confidence 96/100 on the text kept, 38/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
POSSIBLE EXPLOITATION
Information
leakage?
2026
```

## Slide 7

###### **Béla GENGE** Senior Security Researcher Bitdefender

Leading research on Matter IoT security since 2023. He combines industrial innovation with academic exploration, diving deep into reverse-engineering proprietary protocols and making sense of the chaos in computer and IoT network traffic.

**Anca Delia BURDUV** Junior Security Researcher Bitdefender

She has a Bachelor's degree in Computer Science. Before joining Bitdefender, she interned on Arm’s GNU Compiler Collection team, where she worked on Arm intrinsics.

**Ioan PĂDUREAN** Security Researcher Bitdefender

Research on Matter IoT since early 2024. He has a master's degree in Artificial Intelligence and is currently pursuing a PhD in IoT security.

7

## Slide 8

##### OUTLINE

#### Buildings, motivation

Demo Threads, information Demo Exploitability leaks Demo Infrastructure discovery

8

## Slide 9

##### BUILDINGS

Buildings serve several societal needs – occupancy, primarily as shelter from weather, **security** , living space, **privacy** , to store belongings, and to comfortably live and work.

9

## Slide 10

##### BUILDINGS – THE PROBLEM

10

## Slide 11

### The walls haven't changed. The threats have.

11

## Slide 12

##### WHAT MOTIVATED THIS RESEARCH?

###### Notice anything interesting?

12

## Slide 13

##### WHAT TRIGGERED THE RESEARCH

If we take a closer look

It just happens we had prior experience with such devices

13


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
WHAT TRIGGERED THE RESEARCH
If we take a closer look
It just happens we had prior
experience with such devices
2026 13
```

## Slide 14

##### WHAT IS THE TECHNOLOGY BEHIND IT?

14


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
WHAT IS THE TECHNOLOGY BEHIND IT?
A\qara
Agqara U200 smart lock EU black with keypad
Easy installation over existing lock without drilling or modification and wide
compatibility
Silent unlock mod
with major smart home systems, such as Apple Home and
Google Home
Description Features Videos (1)
Upgrade your home to a keyless lifestyle with the Aqara Smart Lock U200 Kit , wiich easily installs over your existing EURO cylinder lock, without the need fo)rilling.
This smart lock supports various access methods such as fingerprint, NFC , passcode and more, and integrates with Apple Home keys . Compatible with Matter, it is
managed through the Aqara Home app and is built to last, with a six-month bajtery life and an IPX5 water resistance rating, making it ideal for both indoor and outdoor use
¢ Apple Home Keys and Multiple Unlock Methods: The U200 offers a variety/of convenient unlock methods, including Apple Home Keys (requires Apple 2-in-] Matter
controller and Border Router), fingerprint, passcode, NFC, and more. You cgn control the lock using the app via either built-in Bluetooth or Thread for remote access
Additionally, it supports temporary passwords, such as one-time and recytring passwords, for easy sharing with others. The device also allows the use of mechanical keys
for emergencies
Advanced Software Control: U200 enhances home access with Silent nlock Mode, automatic alerts and hands-free unlocking, ensuring security and peace of mind with
features such as Activity Log, auto-lock and PIN Code Anti-spy Protectign. It offers flexibility with Passage Mode, temporary passwords including offline passwords (One-
Time Passwords) and periodic passwords available in the Aqara Hom¢ app, along with Do Not Disturb Mode.
Native Support for Matter over Thread: The U200's Matter over Thread support ensures seamless integration with leading smart home systems, such as Apple Home and
Google Home, improving user convenience by extending battery life and efficient remote management.
Rechargeable Battery and Multiple Power Options: The U200’s advanced engineering includes IPX5 waterproofing, an operating range of -15°C to 66°C, and multiple
power sources: rechargeable Li-lon for the lock (up to 6 months), AAA batteries for the keypad, and wired power capability, This ensures durable and reliable performance
```

## Slide 15

##### QUESTIONS OF INTEREST

If devices such as the smart door lock are not located on the street, is traffic still accessible from the street?

If so, what can "the (innocent) bystander" infer when analyzing such data leaks?

15

## Slide 16

# THREAD(S)

16

## Slide 17

##### THREAD, THREAD & MATTER

- Thread:

   - Energy-efficient communication-layer for low-power devices

   - Self-healing mesh network

- IPv6-based protocol for low-power, mesh networks

- • Matter: the application-layer protocol

HTTP, CoAP, MQTT, ...
DTLS
UDP
Distance Vector Routing
6LowPAN (IPv6)
Thread
Border Router
IEEE 802.15.4

17

## Slide 18

##### EXAMPLE THREAD DEVICES

**Border Routers** : Connect a Thread mesh network to external IP networks enabling communication between Thread devices and the outside world.

**Router Eligible End Devices** (REEDs): Can be promoted to routers if the network needs more routing capacity. (usually mains-powered)

**Minimal End Devices** (MEDs):

- Connect to a parent router but do not maintain full routing information, cannot become routers.

**Sleepy End Devices** (SEDs):

- Battery-powered devices that spend most of their time asleep to conserve energy.

- Rely on a parent router for message buffering cannot become routers.

18

## Slide 19

###### WHAT IS THE BIG DEAL ABOUT THREAD?

Thread **progressed a lot** from its first release, it is not only viewed as a standard for smart homes

Source: <u>https://www.knx.org/knx-en/newsroom/news/press/20240916-thread-becomes-partner-ofthe-knx-iot-startup-incubator-program/</u>

It is moving towards **commercial smart buildings**

**Energy and industrial applications** are on the horizon

19

## Slide 20

##### SELF-HEALING ARCHITECTURE

• Scalability of up to 10K Thread devices • Self-healing automates reconfiguration

Non-Router End device Router eligible node Router node Border router

20

## Slide 21

##### CHANNELS AND SIGNAL RANGE

• Thread uses the IEEE 802.15.4 2.4 GHz band from approximately 2405 MHz to 2480 MHz

- Possible channels:

   - 11: 2405 MHz

- 25: 2475 MHz

- Signal can range from 15m indoor to **30-50m+ outdoor**

21

## Slide 22

##### THREAD SECURITY

- **One network-wide** symmetric **key** :

- Media Access Layer (MAC) authentication and encryption

- Different levels of security as defined in IEEE 802.15.4

- **Does not change** very often

|**LEVEL**|**SECURITY LEVEL**|**DESCRIPTION**|**MIC* SIZE**|
|---|---|---|---|
|0x00|None|No security (unencrypted)|-|
|0x01|MIC-32|Data authenticity only|32 bits|
|0x02|MIC-64|Data authenticity only|64 bits|
|0x03|MIC-128|Data authenticity only|128 bits|
|0x04|ENC|Confidentiality only|-|
|0x05|ENC-MIC-32|Confidentiality + Authenticity|32 bits|
|0x06|ENC-MIC-64|Confidentiality + Authenticity|64 bits|
|0x07|ENC-MIC-128|Confidentiality + Authenticity|128 bits|

###### Application security

###### Thread security

_*MIC: Message Integrity Code_

22

## Slide 23

##### THREAD FRAME ENCRYPTION

- Uses the **AES-CCM** scheme to encrypt frames at the IEEE 802.15.4 (MAC/network) layer

- AES-CCM scheme (more specifically AES-CCM*), as defined by NIST 800-38C

slide 30: we had devices a subset of devices slide 31:
define the frame slide 41: more text

23

## Slide 24

##### ESSENTIALLY

The same action (e.g., command) will generate the **same request ... response** packet sizes

24


> Recovered by OCR — confidence 93/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ESSENTIALLY
Nonce
Key Command
€4327981b3a52... Turn ON
AES-CCM
The same action (e.g., command) will generate the
same request ... response packet sizes
Encrypted payload
AES-CCM
CTR | | CBC-MAC |
Key
Nonce
2026 24
```

## Slide 25

##### WHAT ABOUT THE APPLICATION-LAYER?

Mandatory security Symmetric session keys Fabric-specific certificates Key exchange algorithms Ephemeral asymmetric keys

Source: <u>https://www.qorvo.com/design-hub/blog/matter-gets-everybody-talking</u>

**Mandatory security**

Interoperability

25

## Slide 26

##### MATTER PACKET ENCRYPTION

- Matter uses the **AES-CCM** scheme to encrypt packets at the IEEE 802.15.4 (MAC/network) layer

- AES-CCM scheme, as defined by NIST 800-38C

26

## Slide 27

27

## Slide 28

##### WHAT DOES THIS MEAN?

28


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
WHAT DOES THIS MEAN?
2026 28
```

## Slide 29

### SO EVERYTHING IS (DOUBLE) ENCRYPTED?

29

## Slide 30

# INFRASTRUCTURE DISCOVERY

30

## Slide 31

##### SNIFFING THREAD TRAFFIC

Get a Nordic nRF52840 DK development board

Download and install Nordic SDK Compile & flash: **Thread sniffer** Add Wireshark plug-in

Thread sniffer

31

## Slide 32

##### WHERE WE STARTED

32

## Slide 33

##### WORK OBJECT: THE FRAME

Applications
UDP
IP Routing
6LoWPAN
IEEE 802.15.4 MAC
Security / Commissioning

Frames are the individual messages devices exchange over the network Each frame is made up of protocol headers plus a payload

IEEE 802.15.4 PHY

33

## Slide 34

##### (NON-ENCRYPTED) FIELDS OF INTEREST

34


> Recovered by OCR — confidence 87/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
(NON-ENCRYPTED) FIELDS OF INTEREST
Epoch Arrival Time: 1768479792.734628000
Encapsulation type: IEEE 15.4 Wireless PAN S not pr ant (127 tenets ss =i
Frame Length: 103 bytes (824 bits)
0x9869, Frame Type: Data, Security Enak
Sequence Number: 96
ter encoding
Source: Oxac00
(Warning/Undecoded)
Data
Data: O6bi1é
[Length
2026 34
```

## Slide 35

##### REMEMBER OUR PRIOR RESEARCH

In our initial attempt we simply used our approaches developed in the previous research

35


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 89/100 on the text kept, 79/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
REMEMBER OUR PRIOR RESEARCH

[Thumbnail of the previous talk's title slide]
black hat
BRIEFINGS
DECEMBER 10-11, 2025
EXCEL LONDON / UNITED KINGDOM

Ghosts in the Stream: Exposing Lives and Devices Behind Encrypted Doors

Speakers: Kristopher Schlett, Béla Genge
Contributors: Ioan Pădurean, Savio Sciancalepore

#BHEU  @BlackHatEvents

In our initial attempt we simply used our approaches developed in the previous research

[Three packet-capture excerpts, each paired with a photo of a smart device]

Matter          137 35879 → 5540 Len=75
Matter          130 5540 → 35879 Len=68
Matter           96 35879 → 5540 Len=34

Matter          137 35879 → 5540 Len=75
Matter          130 5540 → 35879 Len=68
Matter           96 35879 → 5540 Len=34

Matter          137 35879 → 5540 Len=75
Matter          130 5540 → 35879 Len=68
Matter           96 35879 → 5540 Len=34

Information Classification: General

black hat USA 2026
35
```

## Slide 36

##### WE CAN JUST USE OUR PREVIOUS RESEARCH

One – to – one mapping

36


> Recovered by OCR — confidence 84/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
WE CAN JUST USE OUR PREVIOUS RESEARCH
Matter 5540 — 59065 Len=34
Matter 5540 = 59065 Len=73
Matter 59065 — 5540 Len=42
Matter 5540 — 59065 Len=34
Matter 59065 — 5540 Len=59
Matter 5540 — 59065 Len=67
Matter 59065 — 5540 Len=34
Matter 5540 — 59065 Len=73
Matter 59065 — 5540 Len=42
Matter 5540 — 59065 Len=34
Matter 59065 — 5540 Len=59 .
Matter 5540 — 59065 Len=67 mapping
Matter 59065 — 5540 Len=34
Matter 5540 — 59065 Len=229
Matter 59065 — 5540 Len=42
Matter 5540 — 59065 Len=34
Matter 5540 — 59065 Len=200
Matter 59065 — 5540 Len=42
Matter 5540 — 59065 Len=34
Matter 5540 — 59065 Len=73
Matter 59065 — 5540 Len=42
Matter 5540 — 59065 Len=34
Matter 5540 — 59065 Len=73
Matter 59065 — 5540 Len=42
150 Data, Src: Oxbéoo, : Oxasoo
31 Ack
60 Data, Src: Oxbsoe, : Oxasboo
131 Data, Src: Oxaésoo, : @xbsoo
31 Ack
31 Ack
150 Data, Src: Oxbsoo, : Oxasoo
60 Data, Src: Oxbsoe, : Oxasboo
48 Data Request
31 Ack
127 Data, Src: Oxbéoo, : Oxbse4
115 Data, Src: Oxbso4, : Oxbseo
31 Ack
116 Data, Src: Oxbéoo, : Oxasod
31 Ack
131 Data, : Oxacoo, : Oxagod
31 Ack
31 Ack
31 Ack
131 Data, > Oxasoo, : Oxa4o00
31 Ack
31 Ack
One — to — one
```

## Slide 37

37

## Slide 38

##### RESULT: VERY BAD – 37%

38

## Slide 39

##### WHY WAS THIS THE CASE?

- When forwarded through the mesh network, the same frame shows up several times

- The sniffer picks up the same frame several times

- Solution: identify **unique frames** (forwarding detection)

96Bytes
96Bytes
96Bytes
96Bytes

39

## Slide 40

##### HEURISTICS FOR FORWARDING DETECTION

if recv(frame) and send(frame) and delta(recv, send) < Threshold then **mark_forwarded** (frame) end_if

Value of Threshold determined empirically (~0.8s)

Eliminate "noise", keep only relevant frames

40

## Slide 41

##### LETS TRY AGAIN

##### RESULT: BETTER – 44%, STILL NOT GOOD

41

## Slide 42

##### WHY WAS THIS THE CASE?

Payload of 49 bytes

Payload of 42 bytes

42

## Slide 43

##### FRAME TRANSMISSION: DIFFERENT SIZES

###### The same **Matter** command can be packaged in **Thread** frames of different sizes

Command

43

## Slide 44

##### WHAT EXACTLY IS HAPPENING?

Nothing at the application layer seems different between commands packaged in larger or smaller frames

Command

44

## Slide 45

##### WHY IS THIS HAPPENING?

- Hop limit (decreases after each "hop"):

- 1, 64, 255: compressed

- • other values: **inline** takes up space

Some nodes add Fragmentation Header (fragment of 1)

Traffic class, flow label, etc.: inline / compressed

45

## Slide 46

##### FRAME SIZE DISTRIBUTION

The same payload
transmitted in frames of
different length

46


> Recovered by OCR — confidence 88/100 on the text kept, 63/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
FRAME SIZE DISTRIBUTION
S
The same payload
transmitted in frames of
different length
@ecurrences, log seale
Pvé payload leageh
2026 46
```

## Slide 47

##### REALITY IS COMPLEX

47


> Recovered by OCR — confidence 96/100 on the text kept, 56/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
REALITY IS COMPLEX
2026 47
```

## Slide 48

##### FRAMES CHANGE: HOP LIMIT

0x5c01
Hop limit
0x5c00
0xac00

Hop limit  changes

48


> Recovered by OCR — confidence 90/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
FRAMES CHANGE: HOP LIMIT
IEEE 802.15.4 Data, Src: Ox5c01, Dst: Ox5c00
v- IPHC Header Ox5c01
= Pattern: IP header compression (0x03)
Traffic class and flow label: Version, traffic class, and flow label compressed (0x3) Hop limit
Next header: Compressed "es,
Hop limit: 64 (0x2)
Context identifier extension: True
Ox5c00
Source address compression: Stateful
Source address mode: 64-bits inline (0x0001)
Multicast address compression: False
Destination address compression: Stateless
Destination address mode: Inline (0x0000)
Source context identifier: 0x1
Destination context identifier: 0x0
> IEEE 802.15.4 Data, Src: Ox5c00, Dst: Oxac00
vv 6LOWPAN, Src: ::a2c5:f62:1ac0:80f0, Dest: fda0:13ed:8be5: :be9
O11. .... = Pattern: IP header compression (0x03)
Traffic class and flow label: Version, traffic class, and flow label compressed (0x3)
. . Next header: Compressed
Hop limit changes Hop Limi Inline (0x0)
Context identifier extension: True
Source address compression: Stateful
Source address mode: 64-bits inline (0x0001)
Multicast address compression: False
Destination address compression: Stateless
Destination address mode: Inline (0x0000)
0001 .... = Source context identifier: 0x1
0000 = Destination context identifier: 0x0
Hop limit: 63
```

## Slide 49

##### FRAMES CHANGE: MESH HEADER

Mesh header
0xa000
0x3400
0xa001

###### **Mesh header** is removed

49


> Recovered by OCR — confidence 91/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
FRAMES CHANGE: MESH HEADER
> IEEE 802.15.4 Data,
v- Mesh Header
Flag
10..
Originator:
Destination:
> Fragmentation Header
1111 =
v- IPHC Header
011.
1...
.00
Mesh header is removed
= Pattern: Mesh (0x02)
Vv: True
D: True
Hops left: 15
Deep Hops left (Flags.Hops left == 15): 18
= Pattern:
0x3400, Dst: Oxa000
fdaQ:13ed:8be5::be9, Dest: ::e9c7:64aa:icf2:b5f5
Mesh header
IP header compression (0x03)
Traffic class and flow label: ECN and flow label inline (0x1) Oxa001
Next header: Compressed
Hop Limit: Inline (0x0)
Context identifier extension: True
IEEE 802.15.4 Data, Src: Oxa000, Dst: Oxa001
Vv 6LOWPAN, Src: fda0:13ed:8be5::be9, Dest: ::e9c7:64aa:1icf2:b5f5
Q11. .... = Pattern: IP header compression (0x03)
Source address compression: Stateless
Source address mode: Inline (0x0000)
Multicast address compression: False
Destination address compression: Stateful
. . = Traffic class and flow label: ECN and flow label inline (0x1)
Destination address mode: 64-bits inline (0x0001)
Next header: Compressed
Hop limit: Inline (0x0)
Context identifier extension: True
Source address compression: Stateless
Source address mode: Inline (0x0000)
Multicast address compression: False
Destination address compression: Stateful
Destination address mode: 64-bits inline (0x0001)
49
```

## Slide 50

##### FRAMES CHANGE: FRAGMENTATION HEADER

0x5c01
Fragmentation header
0x5c00
0xac00

###### **Fragmentation header** is removed

50


> Recovered by OCR — confidence 90/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
FRAMES CHANGE: FRAGMENTATION HEADER
> IEEE 802.15.4 Data, Src: OxacO0, Dst: Ox5c00
\- Fragmentation Header Ox5c01
1100 0... = Pattern: First fragment (0x18)
Datagram size: 90 Fragmentation header |
Datagram tag: 0x1ai4 ""enen,
= Pattern: IP header compression (0x03) |
Traffic class and flow label: ECN and flow label inline (0x1)
Next header: Compressed
Hop limit: Inline (0x0)
Context identifier extension: True
Source address compression: Stateless
Source address mode: Inline (0x0000)
Multicast address compression: False
Destination address compression: Stateful > IEEE 802.15.4 Data, Src: Ox5c00, Dst: Ox5c01
..01 Destination address mode: 64-bits inline (Ox'y. 6LOWPAN, Src: fda0:13ed:8be5::be9, Dest: ::a2c5:f62:1ac0:80f0O
Source context identifier: 0x0 \- IPHC Header
0001 = Destination context identifier: 0x1 @11. .... = Pattern: IP header compression (0x03)
00O.. .... = ECN: O
-00 .... = Paddi 0x00
0100 1110 1000 1101 0001 = Flow label: 0x04e8d1
Traffic class and flow label: ECN and flow label inline (0x1)
Next header: Compressed
Hop Limit: Inline (0x0)
Context identifier extension: True
Hop Limit: 63
Source address compression: Stateless
Source address mode: Inline (0x0000)
Fragmentation header is removed Multicast address compression: False
Destination address compression: Stateful
Destination address mode: 64-bits inline (0x0001)
Source context identifier: 0x0
= Destination context identifier: 0x1
ECN: 0
Padding: 0x00
0100 1110 1000 1101 0001 = Flow label: 0x04e8d1
USA
2026 50
Hop limit: 62
```

## Slide 51

125B
0x5c01
0x5c00
0xac00

51

## Slide 52

##### FRAMES CHANGE: SUDDEN FRAGMENTATION

Actual fragmentation
125B
0x5c01
32B
122B 0x5c00
0xac00

**Fragmentation** down the forwarding path

52

## Slide 53

##### FRAGMENTATION DOES NOT ADD UP

Actual fragmentation
125B
0x5c01
32B
122B 0x5c00
0xac00

122 + 32 = 125 ?

53

## Slide 54

54


> Recovered by OCR — confidence 87/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
|! HAVE MANY
PROBLEMS
2026 54
```

## Slide 55

##### COMPLEX PROBLEM REQUIRES (COMPLEX) SOLUTION

Machine learning to the rescue: **Random forests**

55


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
COMPLEX PROBLEM REQUIRES (COMPLEX)
SOLUTION
Machine learning to the rescue:
Random forests
2026 55
```

## Slide 56

##### DEVICE CLASSIFICATION – MODEL TRAINING

- Much better, accuracy increases **above 95%**

56


> Recovered by OCR — confidence 87/100 on the text kept, 63/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
DEVICE CLASSIFICATION — MODEL TRAINING
¢ Much better, accuracy increases above 95%
S
g
8
38
& 8
S
USA
2026 56
```

## Slide 57

##### DEVICE CLASSIFICATION – HOW LONG TO WAIT

- The more time we sniff, the more frames we acquire

- It's more a question of having **the "right" frames**

57

## Slide 58

##### YAP: YET ANOTHER PROBLEM

###### We are seeing more devices than we know we have in the lab

58


> Recovered by OCR — confidence 88/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
YAP: YET ANOTHER PROBLEM
We are seeing more devices than we know we have in the lab
ime cinco capture start (hours)
```

## Slide 59

59

## Slide 60

##### DEVICE COUNT IS CONSTANT

When a new device  shows up , another one  disappears

60

## Slide 61

##### ROUTING LOCATOR 16: RLOC16

- 16-bit address assigned to every Thread device that identifies its location in the current Thread topology

- • It is sent **non-encrypted**

- Router vs **Child**

- Router ID: upper 6 bits

- **Child ID** : lower 10 bits

- _RLOC16 = (Router ID_ ≪ _10) + Child ID_

**15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0**

0x5c00
0x5c01
0x5c02

Router ID Child ID

61

## Slide 62

##### RLOC16 MAY CHANGE

- Depending on the device, network state, RLOC16 may change

- Some devices do not change their RLOC16 for weeks, others change it more frequently

- Solution: **fingerprinting**

62

## Slide 63

##### DEVICE FINGERPRINTING

- Trained model

- The number of frames used as input does not have a major impact

- However, we seem to peak out in terms of accuracy at **~11 frames**

63

## Slide 64

# PRACTICAL EXPLOITATION

64

## Slide 65

##### END-APPROACH

Frame Frame Thread Frame Device Device forwarding variance frame sniffing defragment classification fingerprinting detection elimination

65

## Slide 66

##### TARGET BUILDING: OFFICES

###### Thread network in a partner building from Târgu Mureș, Romania!

We **asked and got permission** to analyze one of the office's Thread setup!

Thread network

66

## Slide 67

##### BUILDING SURVEILLANCE SCENARIOS

- Inside the building, sniff other's offices

- Signal strength can be very good

- - More frames, more details

- Outside the building, sniff whatever is leaking out - Signal strength can vary, often significantly

- - More time needed to capture (relevant) frames

67

## Slide 68

##### INTEGRATED APPLICATION

###### Real-time Thread frame capture & analysis

Integrates ML model for device identification

###### Off-line Thread frame analysis

Automated Thread channel scan & detection

68

## Slide 69

##### THREAD CHANNEL DISCOVERY

69


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
THREAD CHANNEL DISCOVERY
(venv) [bgenge@bgenge-l BHUSA]$ sudo python dynamic_network_topology.py
Starting capture on /dev/ttyACMO - auto-scanning channels for Thread traffic...
[capture] No channel specified - scanning for Thread traffic...
[scan]
[scan] 802.15.4 channel scan
[scan] Range : Ch 11-26 (16 channels)
[scan] Dwell : 2.0 s/channel
[scan] Est. : ~32 s total
[scan]
[scan] Ch 11 [ 1/16] 38 frame(s) < best so far
[scan] Ch 12 [ 2/16] 1 frame(s)
[scan] Ch 13 [ 3/16] © frame(s) - (no traffic)
[scan] Ch 14 [ 4/16] © frame(s) - (no traffic)
[scan] Ch 15 [ 5/16] 1 frame(s) fj
[scan] Ch 16 [ 6/16] © frame(s) - (no traffic)
[scan] Ch 17 [ 7/16] © frame(s) (no traffic)
[scan] Ch 18 [ 8/16] © frame(s) (no traffic)
[scan] Ch 19 [ 9/16] © frame(s) (no traffic)
[scan] Ch 20 [10/16] © frame(s) (no traffic)
[scan] Ch 21 [11/16] © frame(s) (no traffic)
[scan] Ch 22 [12/16] © frame(s) (no traffic)
[scan] Ch 23 [13/16] © frame(s) (no traffic)
[scan] Ch 24 [14/16] © frame(s) - (no traffic)
[scan] Ch 25 [15/16] 2 frame(s)
[scan] Ch 26 [16/16] © frame(s) - (no traffic)
2026 69
```

## Slide 70

##### INSIDE THE BUILDING, OUTSIDE OF OFFICE

70


> Recovered by OCR — confidence 92/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
INSIDE THE BUILDING, OUTSIDE OF OFFICE
1.7 - -74dBm
Active Nodes
-89dBm
60 - Frames / second
frames/s
2026 70
```

## Slide 71

##### INSIDE THE BUILDING, FLOOR -2

71


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
INSIDE THE BUILDING, FLOOR -2
0.8 - -88dBm
BORDER ROUTER
Active Nodes
Frames / second
frames/s
2026 71
```

## Slide 72

##### OUTSIDE THE BUILDING

72


> Recovered by OCR — confidence 87/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
OUTSIDE THE BUILDING
Mean RSSI a = Aa,
Active Nodes
nodes
30 - Frames / second
frames/s
(LIGHTAPP]
2026 72
```

## Slide 73

##### AT A NEARBY FAST FOOD ~30m DISTANCE

Target building

73


> Recovered by OCR — confidence 94/100 on the text kept, 59/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
AT A NEARBY FAST FOOD “30m DISTANCE
Active Nodes
Frames / second
2026 73
```

## Slide 74

##### OTHER SIDE OF THE BUILDING

74


> Recovered by OCR — confidence 89/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
OTHER SIDE OF THE BUILDING
Active Nodes 1.5 - -85dBm
BORDER ROUTER
nodes
Frames / second
frames/s
2026 74
```

## Slide 75

###### REMOTE MONITORING IS POSSIBLE LOCATION, LOCATION, LOCATION

Thread network
The place to be

75


> Recovered by OCR — confidence 90/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
REMOTE MONITORING IS POSSIBLE
LOCATION. LOCATION. LOCATION
Thread network
= ‘VLA
2526 75
The place to be
```

## Slide 76

# DEMO THE INNOCENT BYSTANDERS

76


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
DEMO
THE INNOCENT BYSTANDERS
2026 76
```

## Slide 77

# KEY TAKEAWAYS & ACTIONABLE ITEMS

77

## Slide 78

##### TAKEAWAYS

An increasing number of devices rely on wireless comms, making them inherently **susceptible to remote attacks**

**Insufficient protection** allows traffic capture, analysis, and information leakage. This can have serious privacy implications, leading to building and people profiling

**Protocols are** typically **not tested for "information leakage"** and therefore their design is not tailored to minimize information leakage

78

## Slide 79

##### ACTIONABLE ITEMS

**Protocol designers:**

**Add security (cryptographic) protection** before moving towards critical applications (e.g., building automation / industry-gradeapplications)

**Continue to research** the **security of Thread** , Matter/Thread; these are still new protocols and **likely have undiscovered attack surfaces** . They are also very popular (with steadily growing adoption), hence, vulnerabilities in these protocols may have significant or critical consequences

**Building designers:** Carefully **consider the positioning of critical devices** , since communications can expose them to remote surveillance

79

## Slide 80

##### ACTIONABLE ITEMS

**Everyone:**

Take this research further! Application-layer metadata is now freely available to the security community! <u>https://github.com/bitdefender/matter-iot-dataset</u>

Create your own IoT virtual playground with realistic devices! We have published a Matter IoT framework! <u>https://github.com/bitdefender/matter-ctf</u>

80

## Slide 81

# Thank you! Questions?

<u>bgenge@bitdefender.com, aburduv@bitdefender.com</u>

81
