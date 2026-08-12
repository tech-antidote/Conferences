---
title: "Talkers Without Borders Worldwide Free Speech without an Internet Connection"
speakers: ["T. Gwyddon Owen", "amp"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: null
source_pdf: "DEF CON 34/DEF CON 34 - T. Gwyddon Owen, amp - Talkers Without Borders Worldwide Free Speech without an Internet Connection - v1.pdf"
pages: 24
sha256: "11b110411b1904d638fa6f241e47108269508a4686473933044cefc036797d87"
text_chars: 13188
ocr_pages: 14
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:28:24Z"
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
a
i”
Each time slot
represents
26.6
milliseconds.
7 RSs =. >
i, J, X Xx PERI Et
|. The AIS of Ship A The same
: senses the next open procedure is
5 time slot. At the same repeated by all
Ue time, it reserves other AIS-
: another time slot for L equipped ships.
: the next message. ia oe
ae 9 N7,
a C) tropiesqui OE
A 75 ©0000 tae
```

## Slide 6

tropicsquirrel/EvilAIS-dc34

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
4
<P
———
~~ AIS RECEIVER COMPARISON & HOME SETUP
orere — Clean comparison of gear, antenna needs, and GPS precision — ---- -—
CLASS A AIS TRANSPONDER
Model: Furuno FA- oy
34°37. 1850°N
135°24:5100°E
0.0kn
11.7NH
Tone — Coiwanee — NeRT
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
> =A
LS | 135°24.5100'E
=
34°37.1850’ N Position shown to :
135°24,5100’ E
Class A card shows a typical external AIS VHF antenna size; home setup card shows the compact antenna currently in use.
4 decimal places in minutes.
TO
tropicsquirrel/EvilIAIS-de34
```

## Slide 7

tropicsquirrel/EvilAIS-dc34

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
-——— as ee ae’
al aid ic
—_—e a ° \
ta AIS Transceivers —> Messages TheySend =~
| Simplified transmit-side view x SS
i
LQ ) Lee (e Position / status } (e Static / voyage } ( @ Binary / safety / ASM } (@ Control / infrastructure | 4
' Transceiver Messages transmitted Notes : :
| f Class A | 1/2/3 Position | (5 Static + voyage | Mee Ales Full shipborne set
oy
ae F 27 Long-range Receives 6 / 8 but does
ty Class B | 18 Position J ( 19/24 Static ] not transmit them
& AN SAR Aircraft 9 SAR aircraft position Airborne SAR reporting
“W
v
AIS AtoN ( 21 AtoN report } ( 6/8 ASM/ broadcast data } Aid-to-navigation station BES
AIS SART / 1 Position burst q
ART ali
MOB / EPIRB 14 SART alert text Kav state) Emergency locating beacon
Base Station / ; : 16 /17/ 20/22/23 NAIS is a network of
NAIS | 4 Base station report} (6/ 8 Binary / ase } 21 AtoN report baseictttions
Simplified transmit map — receive-only, interrogation, and acknowledgement messages omitt: clarity.
+ Jy eee - tropics
Sees
Gee,
\
```

## Slide 8

tropicsquirrel/EvilAIS-dc34

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
|. SHIP + SHORE AIS COMMUNICATIONS 2. COMMERCIAL AGGREGATION PLATFORM 3. STEGANOGRAPHY IN PLAIN SIGHT
Relayed by ships, shore stations, FILTERING Encode inside messages
and occasional AIS satellite EVERY system processes
No internet required Not stripped out by
Commercial aggregators aggregator filters
Binary msgs6/ 8 / 25/26 f drop ALL binary-type
| messages
a i Pinata oneness : leo buenas POSITION / TIME / STATUS
SHIP ++°2 B Position / time / status ----- > time, and maneuvering status
4 amt by 9 55° 37.123 N
7 cleaning filters
( )) Binary msgs 6/8 / 25/26 | © 12:45:30 ure
—— tree: > |] = vi
eat +» Hl Position / time/ status ----- i | a socal Oy
SHORE STATION = atehigdl P=) lees Proteccadrand Boooocop-s-}" HIDDEN
Binary msgs 6/8 / 25 / 26 | Eee == tare ; a
<0 BESSOOOD------ > What paying Ji
customers care about
‘a
Ly +++©o Bi Position / time / status -----> a
AIS SATELLITE Hidden bits travel everywhere
(OCCASIONAL RELAY) because the messages stay
@ BBB Binary / ASM messages (6/8 / 25/26) — DROPPED BOeaae Position/ time / status messages > RETAINED & RETRANSMITTED
Irrelevant to position, time, and maneuvering status What customers pay for and every system needs
©) tropicsquirrel/EvilAIS-dc34
```

## Slide 9

tropicsquirrel/EvilAIS-dc34

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
( AIS MANIPULATION IN THE WILD \ ‘
: | : OSS
(1) NEWS HEADLINES / EVIDENCE INTHE WILD ~- — = ——=— ——=— = = os i -
——_————SoEeee sy) & es eee a >. |
. | \
Old Ships, ‘ te _ Fake Iraq callers Dangerous tech | 3
Modern Menace: | £8 Xt sanctionedin found aboard :
How to Tackle the ge (Mest U.S. targeting ‘dark-fleet’ tankers :
0 World’s Shadow Fleets ae be ie = aha captured by the U.S. :
( /
See cron *12,000 seeminson sorte ,
linked to AIS manipulation caught spoofing worldwide ;
AIS manipulation at scale is well documented in the wild—even if this specific steganographic technique is not yet evidenced. ‘
(2.) PRIOR RESEARCH / GROUNDWORK ALREADY LAID -
0) | AISTOOLS DEMOLAB AT DC29 | GCK demonstrated easy AIS spoofing of vessels and navigation aids,
including AlSTools Demolab at DC29 and the Trend Micro AIS Blacktoolkit
ee & TREND MICRO AIS BLACKTOOLKIT for reséarch.and development.
THE NORTH SEA with GPS jamming, and AIS spoofing could create phantom vessels.
Me (3) | DC33: NAVIGATING | DC33 ‘Navigating the Invisible” showed tools can detect real-world Wi
si THE INVISIBLE AIS manipulation such as GPS jittering, a way to fool tracking systems with noise.
= ————S== Cc:
....C) tropicsquirre/EvilAl
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Za 1. Get the News, Tell a cel
()
NO ACCOUNT
NO PHONE
NO TRACE
2. Dead Drop
AIS POSITION REPORT | ~_
48°12.345' N ste
004°23.678' E
HIDDEN DROP LOCATION
NO TRANSMISSION
2,7 wa
)) = fs
)) @).
J= Cae ie iss
TRUSTED INPUT ATTN area
3. Implant to Cascading Effects
‘
by
anh TRADING / MARKETS
= (
4. Implant to Kinetic Effect ‘
VULNERABLE
SCADA / WORKSTATION ZERO-AUTH
NMEA BUS
= 35;
SLEEPER IMPLANT
IN TRUSTED SYSTEM
pe PORT OPERATIONS i
Tie al ay y)
1AIVOM.1.1..A,1SNF, eon Se]
I=1D9 1AIVDM,1.1,,A.1 |
ROUTING / NAV OPTIMIZER
TRIGGER SIGNAL
rb}! (als)
AS | NAVAL/ OPS sySTEMS
i rs
& tropicsquj el/EVIIAIS-des4
ecoo0o
```

## Slide 12

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ee
EVILAIS
COVERT GLOBAL DATA NETWORK
```

## Slide 13

tropicsquirrel/EvilAIS-dc34

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
by,
e@e00o
——° 1. ENCODING TECHNIQUES >—
We built 9 different encoding techniques
to embed data in standard network messages.
y->| [120-1] SPARE BITS
IN FIELDS
TIMING CHANNELS
(INTER-REPORT DELAYS)
NETWORK |}. sp ‘eo
TRANSCEIVER |,
>| eee 7S MORE TECHNIQUES
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
fi ff
|| | \ +
WW
— 2. HIGH THROUGHPUT, REAL IMPACT -— \
We can exfiltrate meaningful data over the network. Sao
ENCRYPTION KEY
IN 30 SECONDS =:
JPG IMAGE i
IN UNDER AN HOUR ; j
NEWS ARTICLE | J °
IN HOURS oie ia
es
@ Not 5G speeds—but you often don’t need that much data. “3
‘ we ; :
“FS |t’s not being watched, and there is a ton of traffic to hide in. |
B Monitoring and filters are often blind to these techniques. |
No reliance on binary fields. Works in plain sight.
Seo
© Ae ©) tropi
Ew — quirreVEvilAIS-dc34
```

## Slide 14

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
| BABYS FIRST »
| 5 DIFFERENTIALS §
| ‘STEGANOGRAPHY, §
—
```

## Slide 15

SS DEFCON is at 36.13 4278 °N 115.157 130° W

**`21680567` −69094278** **`Low = 183 Low = 122`**

SS DEFCON is at 36.134 345° N 115.15 7302° W

Δ ≅ 7m N, 15m W

```
21680607
Low = 223
```

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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Ppython -m evilais.clone_deno configure
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
wig ats chee sens enter <foet yetvectat —pstrende coastal ttden m9 127.0.0.1
1 —kystverket:
>python -=
port 17771 --kystverket-host 127.0.0 port 17771 scenario all —-vatidator-period-s ©
Sender
Real AIS Feed
Twiddling
```

## Slide 19

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
a.
>python ~m evilais.clone_deno configure
EviLAIS clone_demo - runbook generator
Answer a few questions; copy the commands into two terminals.
AIS source feed?
Tel* kystverket Live Norwegian Coast Guard TCP feed (recording deno)
G2] fixture static 600-Line capture replayed Locally pan deom}
2] file specific NMEA capture file you provide
choice [8-2, default 0):
irene
string fixed PSK string (reproducible across runs)
fie constellation derive pikipras observed Kystverket vessels (talk-flavor)
choice [0-1, default 1):
observation window seconds [default:
{@] journalist single 69-985 clip - Good 1: free press
dead-drep single G0-S0s Clip - EviU/erininal coords
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
python -m evilais.clone_demo fake-opencpn —sender-host 153.ull.253.27 —sender-port 5631 —Listen-port 17771
Terminal A - receiver:
python ~m evilais.clone.deno receiver —feed opencpn-Listen —psk-mode constellation —observe-seconds 30.
~observe-port 17771
Terminal 8 - sender:
Bite A Saint 6i nn Mey ect —GAd Seite — eae. coment
ve-port 17771 <2 port 17772 nt
In OpenCPN: ensure both connections exist
= ToP-input~client to 127.0.0.1:12345 (consumes from sender)
Ce ee 1777 (pushes to receiver)
~ Fer visusl pap, MST Properties > Wandle as SANT/PLOCATS) (8
on the MMNSIs (366000777 / 7
>python -m evilais.clone_demo receiver —feed opencpn-Listen —psk-mode constellation --observe-seconds 30.0 —-observe-host 127.
serve-port 1771
Cistaning to 127.0,0.1:3770 for 30.8 seconds
(MN) 222 =
Vessels observes: S72 unique MMSTS
Observation tuples unique (after dedup)
Constellation key acquisition (Receiver)
Fingerprint. 8fc3eBeb...
De
Race a secrce greg 7p Bleed eat een pe ront i pa
port 1771
“por
Sovetaliation bey acqeteitzan Gander)
Listening to 127.0.0.1:17771 for 36.8 seconds
(MN) ©:
Vessels observed: S71 unique MMSIs
Observation tuples’ S72 unique (after dedup)
Fingerprint: 8fc3eBeb...
```

## Slide 20

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ne  ..,,..., x Be =a
{ Totat: 6,404 | 11/3: 2,916 TB: 343 Spare!=9: 39 | Pairs: 94 Confirmed: 15
38/2883 (1.3%) expected <@.1% ABOVE BASELINE
0/338 (0.6%) expected #7% WITHIN NORMAL
79/2883 (2.7%) expected <2% ABOVE BASELINE
[IWFO] 36600777 near—dup (n=1)
&
4
6
>
g
@
®
ad
(=)
Total: 28 Demo: 1 Ambient: 27
Forwarded: 6,162 | 11/3: 2,775 TS: 13 Spare!=@: 39 | Pairs: 96
Scenario: journalist shard 16/16
> PUBLISH IF SILENT UBH bit. ly/4@DaApu
```

## Slide 21

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
OBS#Ose NOLS
EE eva Receiver x be
[[Totat: 6,705 | Ta/3: 3,964 TB: 366 Spare!=9: 47 | Pairs: 94 Confirmed: 15
47/3054 (1.5%) expected <®.1% ABOVE BASELINE
3/365 (0.8%) expected =7% WITHIN NORMAL
79/3054 (2.6%) expected <2% ABOVE BASELINE
a [NED] 366001234 spare!=0+typ
[Type8] dead-drop masi=366001234 Lat=56.5000 Lon=3.0000 [INFO] 366006777 near—dup (n:
a
a
Total: 38 Demo: 2 Ambient: 28
AFF29U76 7373DSED 91
9369930 u62
‘hug 08 22.00 [[Fermarded: 6,404 | 11/3: 2,981 TB: 14 Spare
[Type8] binary mnsi=366001234 !AIVOM,2,2,0,A,@j8a=D8d>CVs3'mD; SjSrAaHQ
[Type8] binary mnsi=366901234 !AIVDM,2,1,0,A, SSM2tDPOGAOMjcVBBVqDOILeU
[Type8] binary mnsi=366001234 !AIVDM,2,2,0,A,j8a=D8d>CVs3"mD; SjSrAaHQ
Scenario: dead-drop binary broadcast (Type 8 DAC=1/FI=29)
HeuCUeRe BeBEEGee 4oeEoe0e 9000000 001901:
```

## Slide 22

# **SO NOW WHAT**

**?**

tropicsquirrel/EvilAIS-dc34

## Slide 23

your individual agency ≠ your internet connection

tropicsquirrel/EvilAIS-dc34

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
your individual agency # your internet connection
C) tropicsquirrel/EvilAIS-de34
```

## Slide 24

#### **References**

DC10 Stealth Data Transport (Khan) AIS Spoofing: A Tutorial for Researchers Dr. Gary Kessler DC27 Hack the Sea (Julian Blanco) DC33 Pirates of the North Sea (Bjørkhaug) DC33 Navigating the invisible (Mehmet Onder Key & Furkan Aydogan) Amro, A., & Gkioulos, V. (2022, September). From Click To Sink: Utilizing AIS for Command and Control in Maritime Cyber Attacks. 27th European Symposium on Research in Computer Security (ESORICS) 2022, Copenhagen, Denmark, pp. 535-553. Lecture Notes in Computer Science (LNCS), 13556. DOI: 10.1007/978-3-031-17143-7_26

tropicsquirrel/EvilAIS-dc34
