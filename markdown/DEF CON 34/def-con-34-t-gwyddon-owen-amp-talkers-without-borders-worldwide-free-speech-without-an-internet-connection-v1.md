---
title: "Talkers Without Borders Worldwide Free Speech without an Internet Connection"
speakers: ["T. Gwyddon Owen", "amp"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: 2026
source_pdf: "DEF CON 34/DEF CON 34 - T. Gwyddon Owen, amp - Talkers Without Borders Worldwide Free Speech without an Internet Connection - v1.pdf"
pages: 24
sha256: "11b110411b1904d638fa6f241e47108269508a4686473933044cefc036797d87"
text_chars: 10499
ocr_pages: 13
has_ocr: true
redacted_secrets: 0
ocr_confidence: 84.0
ocr_unreliable_blocks: 0
vision_verified_pages_changed: 21
vision_verified_pages: 24
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:44:30Z"
---
# Talkers Without Borders Worldwide Free Speech without an Internet Connection

**Speakers:** T. Gwyddon Owen, amp  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - T. Gwyddon Owen, amp - Talkers Without Borders Worldwide Free Speech without an Internet Connection - v1.pdf` (24 pages)


## Slide 1

### TALKERS WITHOUT BORDERS

Worldwide Free Speech Without an Internet Connection

Researching covert channels over AIS. Communicate without a conventional server or ISP.

tropicsquirrel/EvilAIS-dc34

## Slide 2

### TALKERS WITHOUT BORDERS

your individual agency ≠ your internet connection

tropicsquirrel/EvilAIS-dc34

## Slide 3

whoami

- data
- amp

what this talk is about

- old system: AIS
- new tool: EvilAIS

tropicsquirrel/EvilAIS-dc34

## Slide 4

Illustration of the AIS ecosystem, with four large labels:

- satellite AIS (S-AIS) — a satellite at the top, linked by lightning-bolt paths to ships below
- ship-to-shore
- ship-to-ship
- shore network — a cloud on the left, wired to the shore installations

Smaller callout labels inside the illustration:

- AIS Base Station (three of them)
- VTS Control Center
- VTS Radar Site (two of them)

tropicsquirrel/EvilAIS-dc34

## Slide 5

Diagram of AIS SOTDMA slot reservation. A long horizontal row of time slots runs across the top; three of the slots are hatched and coloured (pink, yellow, cyan) and each has an arrow curving forward to a later slot marked with an X. Below, three ships in the matching colours: Ship A (pink), Ship B (yellow), Ship C (cyan).

Callouts:

- Each time slot represents 26.6 milliseconds.
- The AIS of Ship A senses the next open time slot. At the same time, it reserves another time slot for the next message.
- The same procedure is repeated by all other AIS-equipped ships.

Ship labels: Ship A, Ship B, Ship C.

tropicsquirrel/EvilAIS-dc34

## Slide 6

# AIS RECEIVER COMPARISON & HOME SETUP

Clean comparison of gear, antenna needs, and GPS precision

### CLASS A AIS TRANSPONDER — TX + RX

| Field | Value |
|---|---|
| Model | Furuno FA-170 |
| Price | $4,195.00 |
| Use | Full Class A transponder |
| Antenna needed | External VHF AIS antenna |
| Typical antenna size | ~4 ft / 1.2 m whip |

Typical Class A antenna

Mounted outside / high
for best range

Photograph of the Furuno FA-170 display. Its screen reads: TYPE A CLASS A; MMSI 351308000; NAME DUMMY_NAME_NO.2; POSN 34°37.1850'N / 135°24.5100'E; HDG 89°; SOG 0.0kn; COG 264°; RNG 11.7NM; BRG 127°; softkeys CURSOR, FUNC, RANGE, NEXT. The MMSI printed in the screen's top bar is too low-resolution to read reliably.

### HOME SETUP: dAISY USB AIS RECEIVER — RX only

Photograph of the author's receiver on a windowsill, with two callouts: compact antenna, dAISy.

| Field | Value |
|---|---|
| Model | dAISy AIS receiver |
| Price | $96.88 |
| Use | Compact USB receive-only setup |
| Antenna needed | Small foldable / telescopic whip |
| Antenna size | compact desktop / portable |

### GPS PRECISION SHOWN ON THE FURUNO DISPLAY

```text
POSN   34°37.1850'N
      135°24.5100'E
```

34°37.1850' N
135°24.5100' E

Position shown to 4 decimal places in minutes.

Class A card shows a typical external AIS VHF antenna size; home setup card shows the compact antenna currently in use.

tropicsquirrel/EvilAIS-dc34

## Slide 7

# AIS Transceivers → Messages They Send

Simplified transmit-side view

Colour legend: Position / status · Static / voyage · Binary / safety / ASM · Control / infrastructure

| Transceiver | Messages transmitted | Notes |
|---|---|---|
| Class A | 1 / 2 / 3 Position · 5 Static + voyage · 6 / 8 / 25 / 26 Binary / ASM · 27 Long-range | Full shipborne set |
| Class B | 18 Position · 19 / 24 Static · 27 Long-range (SO only) | Receives 6 / 8 but does not transmit them |
| SAR Aircraft | 9 SAR aircraft position | Airborne SAR reporting |
| AIS AtoN | 21 AtoN report · 6 / 8 ASM / broadcast data | Aid-to-navigation station |
| AIS SART / MOB / EPIRB | 14 SART alert text · 1 Position burst (nav status 14) | Emergency locating beacon |
| Base Station / NAIS | 4 Base station report · 6 / 8 Binary / ASM · 16 / 17 / 20 / 22 / 23 Control / DGNSS · 21 AtoN report | NAIS is a network of base stations |

Simplified transmit map — receive-only, interrogation, and acknowledgement messages omitted for clarity.

tropicsquirrel/EvilAIS-dc34

## Slide 8

Three-panel infographic.

### 1. SHIP + SHORE AIS COMMUNICATIONS

Relayed by ships, shore stations, and occasional AIS satellite

No internet required

Three emitters — SHIP, SHORE STATION, AIS SATELLITE (OCCASIONAL RELAY) — each sending two streams rightwards toward the platform:

- Binary msgs 6 / 8 / 25 / 26 (pink)
- Position / time / status (cyan)

### 2. COMMERCIAL AGGREGATION PLATFORM FILTERING

A monitor labelled COMMERCIAL AGGREGATION / MONITORING PLATFORM. Two arrows leave it:

- Up, to a trash icon: Commercial aggregators drop ALL binary-type messages. Irrelevant to position, time, and maneuvering status. Ignored by cleaning filters.
- Right: Processed and retransmitted. What paying customers care about.

### 3. STEGANOGRAPHY IN PLAIN SIGHT

Encode inside messages EVERY system processes

Not stripped out by aggregator filters

A POSITION / TIME / STATUS card:

- 55° 37.123 N
- 12:45:30 UTC
- 12.4 kn   145°

A row of small squares below the card; the last two are boxed in red and joined by a dashed line to an eye icon marked HIDDEN DATA.

Hidden bits travel everywhere because the messages stay

### Legend

- Binary / ASM messages (6 / 8 / 25 / 26) → DROPPED — Irrelevant to position, time, and maneuvering status
- Position / time / status messages → RETAINED & RETRANSMITTED — What customers pay for and every system needs

tropicsquirrel/EvilAIS-dc34

## Slide 9

# AIS MANIPULATION IN THE WILD

### 1 — NEWS HEADLINES / EVIDENCE IN THE WILD

Three news cards, each with a photo:

- Old Ships, Modern Menace: How to Tackle the World's Shadow Fleets
- Fake Iraq callers sanctioned in latest U.S. targeting of Iran's 'shadow fleet'
- Dangerous tech found aboard 'dark-fleet' tankers captured by the U.S.

Three statistics:

- **$200B** /year in sanctions-restricted oil linked to AIS manipulation
- **>12,000** vessels/year caught spoofing
- **0** AIS manipulation prosecutions worldwide

AIS manipulation at scale is well documented in the wild—even if this specific steganographic technique is not yet evidenced.

### 2 — PRIOR RESEARCH / GROUNDWORK ALREADY LAID

| # | Work | Summary |
|---|---|---|
| 1 | AISTOOLS DEMOLAB AT DC29 & TREND MICRO AIS BLACKTOOLKIT | GCK demonstrated easy AIS spoofing of vessels and navigation aids, including AISTools Demolab at DC29 and the Trend Micro AIS Blacktoolkit for research and development. |
| 2 | DC33: PIRATES OF THE NORTH SEA | DC33 'Pirates of the North Sea" showed RF testing could disable navigation with GPS jamming, and AIS spoofing could create phantom vessels. |
| 3 | DC33: NAVIGATING THE INVISIBLE | DC33 'Navigating the Invisible" showed tools can detect real-world AIS manipulation such as GPS jittering, a way to fool tracking systems with noise. |

tropicsquirrel/EvilAIS-dc34

## Slide 10

The same AIS-ecosystem illustration as before, now populated with people — a hooded figure at a laptop, a reporter with a microphone, three children, a group of soldiers, and a cluster of houses — and relabelled:

- satellite-to-internet
- person-to-shore
- person-to-person
- shore-to-internet

Smaller callout labels inside the illustration:

- AIS Base Station (three of them)
- VTS Control Center
- VTS Radar Site (two of them)

tropicsquirrel/EvilAIS-dc34

## Slide 11

Four-panel scenario diagram.

### 1. Get the News, Tell a Friend

A container ship with an AIS unit exchanges chat-bubble messages (via a hooded figure marked NO ACCOUNT / NO PHONE / NO TRACE) with a female news reporter (NEWS) and a male reporter (LIVE).

### 2. Dead Drop

Left to right: a hidden crate on a shore — HIDDEN DROP LOCATION / NO TRANSMISSION — at 48°12.345' N, 004°23.678' E; a map pin at the same coordinates; a ship broadcasting an AIS POSITION REPORT reading 48°12.345' N / 004°23.678' E.

### 3. Implant to Cascading Effects

TRUSTED INPUT (ship + AIS) feeds a SLEEPER IMPLANT IN TRUSTED SYSTEM (skull chip), which branches to four targets:

- TRADING / MARKETS
- PORT OPERATIONS
- ROUTING / NAV OPTIMIZER
- NAVAL / OPS SYSTEMS

### 4. Implant to Kinetic Effect

TRIGGER SIGNAL (AIS) → VULNERABLE SCADA / WORKSTATION (Windows) → ZERO-AUTH NMEA BUS carrying:

```text
!AIVDM,1.1,,A,15Mw;
!AIVDM,1.1,,A,15Nf;
!AIVDM,1.1,,A,15Ng;
...
```

which branches to BALLAST CONTROL, STEERING CONTROL, and PROPULSION CONTROL, ending at a warning triangle beside a ship near a bridge.

tropicsquirrel/EvilAIS-dc34

## Slide 12

EVILAIS logo — a warship with glowing red eyes over a globe, radiating red signal waves.

# EVILAIS

COVERT GLOBAL DATA NETWORK

## Slide 13

# NOISY NETWORKS ARE EXPLOITABLE.

We built tools to hide in the noise—and move data in plain sight.

### 1. ENCODING TECHNIQUES

We built 9 different encoding techniques to embed data in standard network messages.

A hooded figure at a NETWORK TRANSCEIVER, with five technique labels:

- 1 · 0 · 1 SPARE BITS
- POSITION LSBS
- BINARY PAYLOADS IN FIELDS
- TIMING CHANNELS (INTER-REPORT DELAYS)
- + 5 MORE TECHNIQUES (SEE PAPER)

NOT LIMITED TO BINARY FIELDS

These techniques do not rely on binary fields. Binary fields can be used, but they are not required.

WE USE DIFFERENTIAL STEGANOGRAPHY TO HIDE IN PLAIN SIGHT.

"DIFFERENTIAL STEGANOGRAPHY" YOU SAY?

### 2. HIGH THROUGHPUT, REAL IMPACT

We can exfiltrate meaningful data over the network.

A stopwatch reading 30 SECONDS, with three targets:

- ENCRYPTION KEY IN 30 SECONDS
- JPG IMAGE IN UNDER AN HOUR
- NEWS ARTICLE IN HOURS

- Not 5G speeds—but you often don't need that much data.
- It's not being watched, and there is a ton of traffic to hide in.
- Monitoring and filters are often blind to these techniques.
- No reliance on binary fields. Works in plain sight.

tropicsquirrel/EvilAIS-dc34

## Slide 14

Photograph of a children's board book standing on a wooden table. The cover reads:

# BABY'S FIRST DIFFERENTIAL STEGANOGRAPHY

A Playful Guide to Hiding Data in Pictures

The cover art shows a baby, an owl holding a card of binary digits, and a fox holding a dotted card. The spine repeats the title.

## Slide 15

Two speech-bubble position reports for **SS DEFCON**, before and after, with the differing digits boxed in red:

- SS DEFCON is at 36.134**278**°N 115.157**130**°W
- SS DEFCON is at 36.134**345**°N 115.157**302**°W

Δ ≅ 7m N, 15m W

Each coordinate maps to a scaled integer whose low byte carries the payload:

```text
36.134278°N  ->  21680567    115.157130°W  ->  -69094278
             Low = 183                      Low = 122

36.134345°N  ->  21680607    115.157302°W  ->  -69094381
             Low = 223                      Low = 19

223^183=104 = h, 19^122=105 = i -> 'hi'
```

## Slide 16

# Encoding Methods

|**Mode**|**Name**|**Capacity**|**Stealth**|
|---|---|---|---|
|0|Spare Bits|3 bits (T1)/10 bits (T18)|High|
|1|Text Padding|~90 bits|Medium|
|2|Binary Loud|~950 bits|None|
|3|Binary Covert|~950 bits|Very High|
|4|Position LSB|6 bits|Very High|
|5|Checksum Piggy|8 bits|None|
|6|Name Rotation|8-13 bits|Medium|
|7|Timing Channel|2 bits/msg pair|Medium|
|8|Multi Vector (0/4/7)|~11 bits/cycle|Very High|
|9|Noisy (all modes)|varies|None|

## Slide 17

## **DEMO**

tropicsquirrel/EvilAIS-dc34

## Slide 18

Three command-prompt windows, red-labelled.

**Network Hub — AIS-over-TCP — Local-Only** (left):

```text
>python -m evilais.clone_demo configure
```

**Receiver — Real+Our AIS Feed — Decode** (top right):

```text
>python -m evilais.clone_demo receiver --feed opencpn-listen --psk-mode constellation --observe-seconds 30.0 --observe-host 127.0.0.1 --observe-port 17771
```

**Sender — Real AIS Feed — Twiddling** (bottom right):

```text
>python -m evilais.clone_demo sender --feed kystverket --psk-mode constellation --observe-seconds 30.0 --observe-host 127.0.0.1 --observe-port 17771 --kystverket-host 127.0.0.1 --kystverket-port 17771 --scenario all --validator-period-s 0.4
```

## Slide 19

Three terminals: the FakeOpenCPN / runbook generator (left), the Receiver (top right), and the Sender (bottom right).

**FakeOpenCPN — runbook generator (left):**

```text
>python -m evilais.clone_demo configure
============================================================
  EvilAIS clone_demo - runbook generator
  Answer a few questions; copy the commands into two terminals.
============================================================

AIS source feed?
  [0]* kystverket      live Norwegian Coast Guard TCP feed (recording demo)
  [1]  fixture         static 600-line capture replayed locally (rehearsal)
  [2]  file            specific NMEA capture file you provide
choice [0-2, default 0]:

PSK source?
  [0]  string          fixed PSK string (reproducible across runs)
  [1]* constellation   derive from observed Kystverket vessels (talk-flavor)
choice [0-1, default 1]:

observation window seconds [default: '30']:

Which scenario(s) to send?
  [0]  journalist       single 60-90s clip - Good 1: free press
  [1]  dead-drop        single 60-90s clip - Evil/criminal coords
  [2]  trigger          single 60-90s clip - Evil: kinetic effect
  [3]* all              all three sequentially with 5s gaps (long video)
  [4]  custom           type your own --plaintext
choice [0-4, default 3]:

Use real OpenCPN as the bridge?
  [0]* yes              real OpenCPN handles relay - receiver listens on 17770
  [1]  no               no chart visual; sender uses --no-opencpn
choice [0-1, default 0]:

validator-period-s (lower = faster demo, more pairs/sec) [default: '0.4']:

============================================================
  Run these in THREE terminals - fake-opencpn FIRST, then receiver,
  then sender. (fake-opencpn fans out Kystverket so both observers
  see the same byte stream and converge on the same key.)
============================================================

  Terminal 0 - fake-opencpn (Kystverket relay, leave running):
    python -m evilais.clone_demo fake-opencpn --sender-host 153.44.253.27 --sender-port 5631 --listen-port 17771

  Terminal A - receiver:
    python -m evilais.clone_demo receiver --feed opencpn-listen --psk-mode constellation --observe-seconds 30.0 --observe-host 127.0.0.1 --observe-port 17771

  Terminal B - sender:
    python -m evilais.clone_demo sender --feed kystverket --psk-mode constellation --observe-seconds 30.0 --observe-host 127.0.0.1 --observe-port 17771 --kystverket-host 127.0.0.1 --kystverket-port 17771 --scenario all --validator-period-s 0.4

  In OpenCPN: ensure both connections exist
    - TCP-input-client to 127.0.0.1:12345 (consumes from sender)
    - TCP-output-client to 127.0.0.1:17770 (pushes to receiver)
    - For visual pop, MMSI Properties -> Handle as SART/PLB(AIS) MOB
       on the scenario MMSIs (366000777 / 366001234 / 366005000).

>python -m evilais.clone_demo fake-opencpn --sender-host 153.44.253.27 --sender-port 5631 --listen-port 17771
FakeOpenCPN: listening on 127.0.0.1:17771, connecting to 153.44.253.27:5631...
FakeOpenCPN: connected to sender at 153.44.253.27:5631
FakeOpenCPN: receiver connected from ('127.0.0.1', 32568)
FakeOpenCPN: receiver connected from ('127.0.0.1', 32569)
FakeOpenCPN: receiver disconnected from ('127.0.0.1', 32568)
FakeOpenCPN: receiver disconnected from ('127.0.0.1', 32569)
```

**Receiver (top right):**

```text
>python -m evilais.clone_demo receiver --feed opencpn-listen --psk-mode constellation --observe-seconds 30.0 --observe-host 127.0.0.1 --observe-port 17771
--- Constellation key acquisition (Receiver) ---
  Listening to 127.0.0.1:17771 for 30.0 seconds...

  [==========] 30.0 / 30.0 s

  Vessels observed:    571 unique MMSIs
  Observation tuples:  571 unique (after dedup)

  Fingerprint:  8fc3e8eb...
```

**Sender (bottom right):**

```text
>python -m evilais.clone_demo sender --feed kystverket --psk-mode constellation --observe-seconds 30.0 --observe-host 127.0.0.1 --observe-port 17771 --kystverket-host 127.0.0.1 --kystverket-port 17771 --scenario all --validator-period-s 0.4
--- Constellation key acquisition (Sender) ---
  Listening to 127.0.0.1:17771 for 30.0 seconds...

  [==========] 30.0 / 30.0 s

  Vessels observed:    571 unique MMSIs
  Observation tuples:  571 unique (after dedup)

  Fingerprint:  8fc3e8eb...
```

## Slide 20

Demo capture: OpenCPN 5.14.0-0 (left) showing a chart of the Norwegian coast densely populated with AIS targets, alongside the EvilAIS Receiver (top right) and EvilAIS Sender (bottom right) terminals.

**Receiver:**

```text
Total: 6,404  |  T1/3: 2,916  T8: 343  Spare!=0: 39  |  Pairs: 94  Confirmed: 15
```

A live AIS stream of scrolling !AIVDM sentences, then:

```text
--- analyst alerts ---
baseline: Kystverket 14h, n~3.5M, 2026-04-12
  spare!=0   38/2883 (1.3%) expected <0.1% ABOVE BASELINE
             demo:0  ambient:38 (real-fleet)
  type8-hi   0/338 (0.0%) expected ~7% WITHIN NORMAL
  near-dup   79/2883 (2.7%) expected <2% ABOVE BASELINE
             demo:79  ambient:0 (real-fleet)

[INFO] 366000777 near-dup (n=1)
[INFO] 245593000 spare!=0 (n=1)
[INFO] 257874000 spare!=0 (n=1)
[INFO] 259210000 spare!=0 (n=1)
[INFO] 258465000 spare!=0 (n=1)
[INFO] 259372000 spare!=0 (n=1)
[INFO] 249497000 spare!=0 (n=1)
[INFO] 259393000 spare!=0 (n=1)
Total: 28  Demo: 1  Ambient: 27

--- recovered plaintext ---
> PUBLISH IF SILENT 48H bit.ly/48DaApU
  recovered. RS parity tail: 4/4 (resilience - lossless under shard loss)
```

**Sender:**

```text
Forwarded: 6,160  |  T1/3: 2,775  T8: 13  Spare!=0: 39  |  Pairs: 96
```

A live AIS stream (sender) of scrolling !AIVDM sentences, then:

```text
--- encoding progress ---
Scenario: journalist   shard 16/16
> PUBLISH IF SILENT 48H bit.ly/48DaApU
```

## Slide 21

Demo capture: OpenCPN 5.14.0-0 (left) with an AIS target info window open on the dead-drop vessel, alongside the EvilAIS Receiver (top right) and EvilAIS Sender (bottom right) terminals.

**OpenCPN AIS Target window:**

```text
DEAD-DROP EVL
MMSI               Class         IMO
366001234          A             07654321
Flag
United States of America
Tanker, Underway using Engine
100m x 20m x 4.0m
Position                         Report Age
56° 30.3300' N                   6s
003° 00.3300' E
Destination                      ETA (UTC)
DEFCON34                         Aug 08 22:00
Speed        Course              Heading
12.0 kts     045°                045°
Range        Bearing             Turn Rate
---          ---                 ---
[ Create Waypoint ]  [ Record Track ]  [ OK ]
```

**Receiver:**

```text
Total: 6,705  |  T1/3: 3,064  T8: 366  Spare!=0: 47  |  Pairs: 94  Confirmed: 15
```

A live AIS stream of scrolling !AIVDM sentences (including a flagged `[Type8] dead-drop mmsi=366001234 lat=56.5000 lon=3.0000`), then:

```text
--- analyst alerts ---
baseline: Kystverket 14h, n~3.5M, 2026-04-12
  spare!=0   47/3054 (1.5%) expected <0.1% ABOVE BASELINE
             demo:6  ambient:41 (real-fleet)
  type8-hi   3/366 (0.8%) expected ~7% WITHIN NORMAL
             demo:3  ambient:0 (real-fleet)
  near-dup   79/3054 (2.6%) expected <2% ABOVE BASELINE
             demo:79  ambient:0 (real-fleet)

[MED]  366001234 spare!=0+type8-hi (n=2)
[INFO] 366000777 near-dup (n=1)
[INFO] 259210000 spare!=0 (n=1)
[INFO] 258465000 spare!=0 (n=1)
[INFO] 259372000 spare!=0 (n=1)
[INFO] 249497000 spare!=0 (n=1)
[INFO] 259393000 spare!=0 (n=1)
[INFO] 220223000 spare!=0 (n=1)
Total: 30  Demo: 2  Ambient: 28

--- recovered plaintext ---
Dead-drop received  mmsi=366001234
  lat:  56.5000°N    lon:  3.0000°E
  depth: 25 m        cargo:  alpha (1)
  eta:  2026-05-03 01:21 UTC
  raw:  17DDCAB9 884BEE54 7D972D95 E1DEFCCD AFF29476 7373D5ED 9154FC07 D9369930 46235F36 BAF8
```

**Sender:**

```text
Forwarded: 6,404  |  T1/3: 2,901  T8: 14  Spare!=0: 40  |  Pairs: 108
```

A live AIS stream (sender) of scrolling !AIVDM sentences (including flagged `[Type8] binary mmsi=366001234` lines), then:

```text
--- encoding progress ---
Scenario: dead-drop   binary broadcast (Type 8 DAC=1/FI=29)
> raw: DEADD400 404C4000 00000000 40080000 00000000 00190169 F6A330
```

## Slide 22

# **SO NOW WHAT**

**?**

tropicsquirrel/EvilAIS-dc34

## Slide 23

your individual agency ≠ your internet connection

tropicsquirrel/EvilAIS-dc34

## Slide 24

#### **References**

- DC10 Stealth Data Transport (Khan)
- AIS Spoofing: A Tutorial for Researchers Dr. Gary Kessler
- DC27 Hack the Sea (Julian Blanco)
- DC33 Pirates of the North Sea (Bjørkhaug)
- DC33 Navigating the invisible (Mehmet Onder Key & Furkan Aydogan)

Amro, A., & Gkioulos, V. (2022, September). From Click To Sink: Utilizing AIS for Command and Control in Maritime Cyber Attacks. 27th European Symposium on Research in Computer Security (ESORICS) 2022, Copenhagen, Denmark, pp. 535-553. Lecture Notes in Computer Science (LNCS), 13556. DOI: 10.1007/978-3-031-17143-7_26

tropicsquirrel/EvilAIS-dc34

