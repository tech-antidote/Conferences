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

TALKERS WITHOUT BORDERS Worldwide Free Speec h Wit hout an Int ernet Connec t ion Researching covert channels over AIS. Communicate without a conventional server or ISP.

tropicsquirrel/EvilAIS-dc34

## Slide 2

### TALKERS WITHOUT BORDERS

your individual agency ≠ your internet connection

tropicsquirrel/EvilAIS-dc34

## Slide 3

whoami data amp

what this talk is about old system: AIS new tool: EvilAIS

tropicsquirrel/EvilAIS-dc34

## Slide 4

satellite AIS (S-AIS)
ship-to-shore
ship-to-ship
shore networ k
tropicsquirrel/EvilAIS-dc34

## Slide 5

tropicsquirrel/EvilAIS-dc34


> Recovered by OCR — confidence 84/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Each time slot
represents
26.6
milliseconds.
|. The AIS of Ship A The same
: senses the next open procedure is
5 time slot. At the same repeated by all
Ue time, it reserves other AIS-
: another time slot for L equipped ships.
: the next message. ia oe
A 75 ©0000 tae
```

## Slide 6

tropicsquirrel/EvilAIS-dc34


> Recovered by OCR — confidence 89/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
4
orere — Clean comparison of gear, antenna needs, and GPS precision — ---- -—
CLASS A AIS TRANSPONDER
Model: Furuno FA- oy
34°37. 1850°N
0.0kn
Antenna needed:
External VHF AIS antenna
Typical antenna size:
~4 ft /1.2 m whip
Typical Class A antenna
Mounted outside / high
for best range
HOME SETUP: dAISY USB AIS RECEIVER RX only }
compact
antenna
Model: dAlISy AIS receiver
Price: $96.88
Use: Compact USB receive-only setup
Antenna needed: Small foldable / telescopic whip
Antenna size: compact desktop / portable
GPS PRECISION SHOWN ON THE FURUNO DISPLAY
34°37.1850’ N Position shown to :
135°24,5100’ E
Class A card shows a typical external AIS VHF antenna size; home setup card shows the compact antenna currently in use.
4 decimal places in minutes.
```

## Slide 7

tropicsquirrel/EvilAIS-dc34


> Recovered by OCR — confidence 78/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ta AIS Transceivers —> Messages TheySend =~
| Simplified transmit-side view x SS
LQ ) Lee (e Position / status } (e Static / voyage } ( @ Binary / safety / ASM } (@ Control / infrastructure | 4
' Transceiver Messages transmitted Notes : :
| f Class A | 1/2/3 Position | (5 Static + voyage | Mee Ales Full shipborne set
oy
ae F 27 Long-range Receives 6 / 8 but does
ty Class B | 18 Position J ( 19/24 Static ] not transmit them
& AN SAR Aircraft 9 SAR aircraft position Airborne SAR reporting
AIS AtoN ( 21 AtoN report } ( 6/8 ASM/ broadcast data } Aid-to-navigation station BES
AIS SART / 1 Position burst q
ART ali
MOB / EPIRB 14 SART alert text Kav state) Emergency locating beacon
Base Station / ; : 16 /17/ 20/22/23 NAIS is a network of
NAIS | 4 Base station report} (6/ 8 Binary / ase } 21 AtoN report baseictttions
Simplified transmit map — receive-only, interrogation, and acknowledgement messages omitt: clarity.
\
```

## Slide 8

tropicsquirrel/EvilAIS-dc34


> Recovered by OCR — confidence 85/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
|. SHIP + SHORE AIS COMMUNICATIONS 2. COMMERCIAL AGGREGATION PLATFORM 3. STEGANOGRAPHY IN PLAIN SIGHT
Relayed by ships, shore stations, FILTERING Encode inside messages
and occasional AIS satellite EVERY system processes
No internet required Not stripped out by
Commercial aggregators aggregator filters
Binary msgs6/ 8 / 25/26 f drop ALL binary-type
| messages
SHIP ++°2 B Position / time / status ----- > time, and maneuvering status
4 amt by 9 55° 37.123 N
7 cleaning filters
( )) Binary msgs 6/8 / 25/26 | © 12:45:30 ure
customers care about
AIS SATELLITE Hidden bits travel everywhere
(OCCASIONAL RELAY) because the messages stay
@ BBB Binary / ASM messages (6/8 / 25/26) — DROPPED BOeaae Position/ time / status messages > RETAINED & RETRANSMITTED
Irrelevant to position, time, and maneuvering status What customers pay for and every system needs
©) tropicsquirrel/EvilAIS-dc34
```

## Slide 9

tropicsquirrel/EvilAIS-dc34


> Recovered by OCR — confidence 85/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
( AIS MANIPULATION IN THE WILD \ ‘
Old Ships, ‘ te _ Fake Iraq callers Dangerous tech | 3
Modern Menace: | £8 Xt sanctionedin found aboard :
How to Tackle the ge (Mest U.S. targeting ‘dark-fleet’ tankers :
linked to AIS manipulation caught spoofing worldwide ;
AIS manipulation at scale is well documented in the wild—even if this specific steganographic technique is not yet evidenced. ‘
(2.) PRIOR RESEARCH / GROUNDWORK ALREADY LAID -
0) | AISTOOLS DEMOLAB AT DC29 | GCK demonstrated easy AIS spoofing of vessels and navigation aids,
including AlSTools Demolab at DC29 and the Trend Micro AIS Blacktoolkit
ee & TREND MICRO AIS BLACKTOOLKIT for reséarch.and development.
THE NORTH SEA with GPS jamming, and AIS spoofing could create phantom vessels.
Me (3) | DC33: NAVIGATING | DC33 ‘Navigating the Invisible” showed tools can detect real-world Wi
si THE INVISIBLE AIS manipulation such as GPS jittering, a way to fool tracking systems with noise.
® (2) | DC33: PIRATES OF | DC33 ‘Pirates of the North Sea” showed RF testing could disable navigation a :
```

## Slide 10

satellite-to-internet
person-to-shore
person-to-person
shore-to-internet
tropicsquirrel/EvilAIS-dc34

## Slide 11

tropicsquirrel/EvilAIS-dc34


> Recovered by OCR — confidence 86/100 on the text kept, 65/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Za 1. Get the News, Tell a cel
NO ACCOUNT
NO PHONE
NO TRACE
2. Dead Drop
AIS POSITION REPORT | ~_
48°12.345' N ste
004°23.678' E
HIDDEN DROP LOCATION
NO TRANSMISSION
3. Implant to Cascading Effects
by
anh TRADING / MARKETS
= (
4. Implant to Kinetic Effect ‘
VULNERABLE
SCADA / WORKSTATION ZERO-AUTH
NMEA BUS
SLEEPER IMPLANT
IN TRUSTED SYSTEM
ROUTING / NAV OPTIMIZER
TRIGGER SIGNAL
```

## Slide 12


> Recovered by OCR — confidence 95/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
EVILAIS
COVERT GLOBAL DATA NETWORK
```

## Slide 13

tropicsquirrel/EvilAIS-dc34


> Recovered by OCR — confidence 89/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
——° 1. ENCODING TECHNIQUES >—
We built 9 different encoding techniques
to embed data in standard network messages.
IN FIELDS
TIMING CHANNELS
(INTER-REPORT DELAYS)
(SEE PAPER)
NOT LIMITED TO BINARY FIELDS
These techniques do not rely on binary fields.
Binary fields can be used, but they are not required.
NOISY NETWORKS ARE EXPLOITABLE.
We built tools to hide in the noise—and move data in plain sight.
© POSITION LSBS
BINARY PAYLOADS
1010
WE USE DIFFERENTIAL STEGANOGRAPHY TO HIDE IN PLAIN SIGHT.
“DIFFERENTIAL STEGANOGRAPHY” YOU SAY? F¥~a
WW
— 2. HIGH THROUGHPUT, REAL IMPACT -— \
We can exfiltrate meaningful data over the network. Sao
ENCRYPTION KEY
IN 30 SECONDS =:
JPG IMAGE i
IN UNDER AN HOUR ; j
NEWS ARTICLE | J °
IN HOURS oie ia
@ Not 5G speeds—but you often don’t need that much data. “3
“FS |t’s not being watched, and there is a ton of traffic to hide in. |
B Monitoring and filters are often blind to these techniques. |
No reliance on binary fields. Works in plain sight.
© Ae ©) tropi
```

## Slide 14

## Slide 15

SS DEFCON is at 36.13 4278 °N 115.157 130° W

**`21680567` −69094278** **`Low = 183 Low = 122`**

SS DEFCON is at 36.134 345° N 115.15 7302° W

Δ ≅ 7m N, 15m W

\```
21680607
Low = 223
\```

**223^183=104 = h,**

**−69094381 Low = 19**

**19^122=105 = i** **`->` ‘hi’**

## Slide 16

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

**Network Hub AIS-over-TCP Local-Only**

**Receiver Real+Our AIS Feed Decode**

**Sender Real AIS Feed Twiddling**


> Recovered by OCR — confidence 78/100 on the text kept, 58/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Network Hub
AlS-over-TCP
Local-Only
FE command Prompt
>python -m evilais.clonedeno receiver —Feed opencpn-listen —psk-mode constellation —-observe-seconds 30.0 —observe-host 127.0.0.1
serve-port 17771
Receiver
Real+Our AIS Feed
Decode
0b
FE command Prompt
1 —kystverket:
Real AIS Feed
Twiddling
```

## Slide 19


> Recovered by OCR — confidence 80/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
>python ~m evilais.clone_deno configure
EviLAIS clone_demo - runbook generator
Answer a few questions; copy the commands into two terminals.
AIS source feed?
Tel* kystverket Live Norwegian Coast Guard TCP feed (recording deno)
2] file specific NMEA capture file you provide
choice [8-2, default 0):
string fixed PSK string (reproducible across runs)
fie constellation derive pikipras observed Kystverket vessels (talk-flavor)
choice [0-1, default 1):
observation window seconds [default:
{@] journalist single 69-985 clip - Good 1: free press
[2] trigger Single 60-985 clip - Evil: kinetic effect
{3} att all three sequentially mith Ss gaps (long video)
[4] custom type your own —plaintext,
choice [O-a, default 3]:
Use real OpenCPN as the bridge?
t real OpenCPN handles relay - receiver Listens on 17770
no chart visual; sender uses —no-opencpn
choice [8-1, default 0}:
validator-period-s (lower = faster demo, more pairs/sec) (default:
see the same byte stream and converge on the same key.)
Terminal © - fake-opencpn (Kystverket relay, Leave running):
Terminal A - receiver:
python ~m evilais.clone.deno receiver —feed opencpn-Listen —psk-mode constellation —observe-seconds 30.
~observe-port 17771
Terminal 8 - sender:
In OpenCPN: ensure both connections exist
on the MMNSIs (366000777 / 7
>python -m evilais.clone_demo receiver —feed opencpn-Listen —psk-mode constellation --observe-seconds 30.0 —-observe-host 127.
serve-port 1771
Vessels observes: S72 unique MMSTS
Observation tuples unique (after dedup)
Constellation key acquisition (Receiver)
port 1771
Listening to 127.0.0.1:17771 for 36.8 seconds
Vessels observed: S71 unique MMSIs
Observation tuples’ S72 unique (after dedup)
```

## Slide 20


> Recovered by OCR — confidence 78/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
{ Totat: 6,404 | 11/3: 2,916 TB: 343 Spare!=9: 39 | Pairs: 94 Confirmed: 15
38/2883 (1.3%) expected <@.1% ABOVE BASELINE
0/338 (0.6%) expected #7% WITHIN NORMAL
79/2883 (2.7%) expected <2% ABOVE BASELINE
[IWFO] 36600777 near—dup (n=1)
4
@
Total: 28 Demo: 1 Ambient: 27
Forwarded: 6,162 | 11/3: 2,775 TS: 13 Spare!=@: 39 | Pairs: 96
Scenario: journalist shard 16/16
> PUBLISH IF SILENT UBH bit. ly/4@DaApu
```

## Slide 21


> Recovered by OCR — confidence 78/100 on the text kept, 63/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
[[Totat: 6,705 | Ta/3: 3,964 TB: 366 Spare!=9: 47 | Pairs: 94 Confirmed: 15
47/3054 (1.5%) expected <®.1% ABOVE BASELINE
3/365 (0.8%) expected =7% WITHIN NORMAL
79/3054 (2.6%) expected <2% ABOVE BASELINE
a [NED] 366001234 spare!=0+typ
a
a
Total: 38 Demo: 2 Ambient: 28
AFF29U76 7373DSED 91
9369930 u62
Scenario: dead-drop binary broadcast (Type 8 DAC=1/FI=29)
```

## Slide 22

# **SO NOW WHAT**

**?**

tropicsquirrel/EvilAIS-dc34

## Slide 23

your individual agency ≠ your internet connection

tropicsquirrel/EvilAIS-dc34


> Recovered by OCR — confidence 88/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
your individual agency # your internet connection
C) tropicsquirrel/EvilAIS-de34
```

## Slide 24

#### **References**

DC10 Stealth Data Transport (Khan) AIS Spoofing: A Tutorial for Researchers Dr. Gary Kessler DC27 Hack the Sea (Julian Blanco) DC33 Pirates of the North Sea (Bjørkhaug) DC33 Navigating the invisible (Mehmet Onder Key & Furkan Aydogan) Amro, A., & Gkioulos, V. (2022, September). From Click To Sink: Utilizing AIS for Command and Control in Maritime Cyber Attacks. 27th European Symposium on Research in Computer Security (ESORICS) 2022, Copenhagen, Denmark, pp. 535-553. Lecture Notes in Computer Science (LNCS), 13556. DOI: 10.1007/978-3-031-17143-7_26

tropicsquirrel/EvilAIS-dc34
