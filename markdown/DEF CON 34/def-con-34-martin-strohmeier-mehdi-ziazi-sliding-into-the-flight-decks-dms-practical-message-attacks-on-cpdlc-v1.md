---
title: "Sliding into the Flight Deck’s DMs Practical Message Attacks on CPDLC"
speakers: ["Martin Strohmeier", "Mehdi Ziazi"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: null
source_pdf: "DEF CON 34/DEF CON 34 - Martin Strohmeier, Mehdi Ziazi - Sliding into the Flight Deck’s DMs Practical Message Attacks on CPDLC - v1.pdf"
pages: 69
sha256: "ed586be9f959cdc136a458dca7d17d53b95832fbadc79723bbd1658f7ef32b1c"
text_chars: 28024
ocr_pages: 36
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:24:17Z"
---
# Sliding into the Flight Deck’s DMs Practical Message Attacks on CPDLC

**Speakers:** Martin Strohmeier, Mehdi Ziazi  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Martin Strohmeier, Mehdi Ziazi - Sliding into the Flight Deck’s DMs Practical Message Attacks on CPDLC - v1.pdf` (69 pages)


## Slide 1

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
>
~~
4 CONNECTION INTERCEPTED
* a
a Ta
: is
Sao Ss : 3 MESSAGE MANIPULATION
ATC 18:427
CLx123
CLIMB FL380
* Injection
* Modification
+ Deletion A |
REPORT LEVEL ws z =
Replay
ee
vw
r CLX123 18:43Z Flight
WILCO
a": Practical Message Attacks on CPDLC
> INTERCEPTING CPDLC...
| > DECODING MESSAGE...
EXPECT TURBULENCE |
: = ) > ALTERING CONTENT...
FL340-FL360 el | 2 Mehdi Ziazi j | 2 Martin Strohmeier } > SENDING FAKE CLEARANCE...
a EEN —— = al
> ATTACK SUCCESSFUL
(ey)
CPDOLC BOARNEL} i 2
| cPpie
CONNECTED v
LOGON COMPLETE
```

## Slide 2

### Who are we? - Martin

- Security Researcher & Senior Scientist @ Swiss Cyber-Defence Campus

- Background/PhD in wireless security

- Published in all major academic systems security & AI conferences

- Leading research efforts on transportation cyber security at armasuisse

- Co-founder & board member of the OpenSky Network

## Slide 3

#### Who are we? - Mehdi

- Cybersecurity Master’s Student

- Incoming Researcher in Space Systems Security

- NOT a Security Researcher nor Senior Scientist @ Swiss Cyber-Defence Campus

- NO Background/PhD in wireless security

- NO Leading research efforts on transportation cyber security at armasuisse

- NOT a Co-founder & board member of the OpenSky Network

- Just a student

## Slide 4

Aircraft Have DMs Now

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Aircraft Have DMs Now
1231z ATC UPLINK 274
AFTER CNK CLEARED TO
KBED ARPT AS* FILED
“FREE TEXT ~
RUUDYS, CLIMB ¥IA SID
“FREE TEXT
EXPECT FL19@ 10 NIN AFT
——-CONTINUED-—
| 4aTC INDEX
```

## Slide 5

Inspiration: DEF CON 20 / Blackhat 2012 Talks

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Inspiration: DEF CON 20 / Blackhat 2012 Talks
EF EGON
Q”
Re oh
EURECOM bisok| =A 22
USAeaiS
```

## Slide 6

That got everyone’s attention

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
That got everyone's attention
News
Hackers say coming air traffic control system lets . =
them hijac planes ” Researcher: New air traffic control
FAA says it can spot hacking attempts, but won't allow independent ‘stress tests’ syste m is hacka b I e
ymerding, CSO
06:12 AM ET ie | By Heather Kelly, CNN
July 26, 2012 — Updated 2249 GMT (0649 HKT) | Filed under: Web
Feo aaa comment ont inEenY eO nen)
cs An iItibillion-doll: haul of the 's ait ffi i) +4 4 +4 +
sien a doagadeneke ommecdaiaenocstceseone Ait Traffic Control of the Future Is (Still) Incredibly
friendly and safer by 2025.
Sleeping air traffic controllers get federal wakeup Hac ka bl e
But some white-hat hackers are questioning the safety part. The Next Genen
Transportation System (NextGen) will rely on Global Positioning Systems (GI uy «
of radar. And so far, several hackers have said they were able to demonstrate the
capability to hijack aircraft by spoofing their GPS components.
Defcon Researchers Build Tool To Track the Planes of the Rich and Famous
AM
Air Traffic Controllers Pick the Wrong Week
to Quit Using Radar
Hacker Shows Air Traffic Control Danger With 'Ghost
Planes' security 012.6 21840 | 17,096 view
ee le - _ Next-Gen Air Traffic Control
Read More: Air Force One, Air Traffic Control, Faa, Travel News, Air Travel, Airlines, Hacking, Black Hat, Travel
Se Vulnerable To Hackers Spoofing
Andrei Costin, a Cypriad hacker, gave an unnerving demonstration Planes Ou t O f Thin Air
outlining the weaknesses of air traffic control systems today at the
Black Hat hackin...
Ut IBLLGH <cormenes, 3 caes-out | + comment Now + Potlow Comments
Read Whole Story
```

## Slide 7

Aviation Industry’s Answer

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Aviation Industry’s Answer
THE SKY IS CALLING, NOT FALLING
Tim Taylor talks about the disturb Indeed, the FAA expounded on a larger concern-the number of functions that prudently should be
as if the ongoing roll-out of ADS-f contained in one box of avionics. Just as the value of real estate is based on the cliché, "location,
peril. He recommends: location, location, Bair safety is built on the trinity of “redundancy, redundancy, redundan If TCAS
1) Relax, the situation is OK, bordering on “normal.” - The FAA says it has procedures
in place to prevent that, and that system security is integral to ADS-B technical
specifications. At minimum the subject ¢ /ININ .
engineering circles - by people who are onl | ne BIZAV AIR TRANSPORT DEFENSE
who have had more than a decade to co
over this. AIR TRANSPORT
~ — S eon Hackers, FAA Disagree Over ADS-B Vulnerability
by Matt Thurber - August 21, 2012, 4:15 PM
4 “An FAA ADS-B security action plan idenuneo ang miugateu nsKs ang monnors we progress OF
clelbeeeeliéeds FAA Denies Vulnerabilities In New Air Traffic Control System
A spokeswoman for key ADS-B: Posted by Soulskill on Wednesday August 22, 2012 @05:23PM
from th t's-the-worst-that-could-hay it.
security certification and accredivauw:. sabe hele haialaes pcbaliloige Barina ood euvowsswar ninuieuun
security features built in, including features to protect against...spoofing attacks. [This] is provided through
hat a target is where it is reported to be.”
```

## Slide 8

A 15 year journey on practical aviation hacking

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Aircraft-to-Satellite
Aircraft-to-Aircraft
mol
(=
=)
°
1
2
°
>
£
©
He
S
=
<=
A 15 year journey on practical aviation hacking
% %, >
we w% we
© = SS MY ILS
\ o
», 2022/23 2024 2020 TD
cs sey foes | |=
oo SADS-B ACARS =.
2 a
=
=a > =" >
15
.
2024 o f
o
< > =
TCAS
ADS-B T T T T T
Mode A/C/S Ground Departure —_En-route Approach Ground
ADS-B FIS-B ACARS DME
Mode A/C/S TIS-B i NDB
MLAT Mode A/C/S [ CPDLC VOR un 5
2012-25 (Interrogations) 2026 Pe ILs
2017 2020
) SA 2
ATC ground stations
¥
(« ] »)
NS
( ») Pi
Grou ised navigation aids
```

## Slide 9

#### One Lesson Learned: *Full* Live Demos Required

**No crypto on paper = trivial, right?**

Lots of radio-frequency security research has been conducted in simulated hardware/software but no (public) real-world tests are available.

###### **The Industry Response**

You show them the hacks in theory or simulation and you basically get the same responses: _“This is not possible in practice”_ — for some magical unexplained reasons.

DO-282A Standards: Searching for "security" yields "No matches found"

## Slide 10

Consequence: The Original Avionics Security Lab

## Slide 11

#### Extension: The CPDLC Hacking Lab

Thanks to Q.C.M. quality control management AG!

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Extension: The CPDLC Hacking Lab
VHF
FMS UNS-1Ew ANTENNA
; n
= .
| A429
| ETHERNET
Unilink UL-801
CMU
Thanks to Q.C.M. quality control management AG!
```

## Slide 12

#### Connecting to the Real World

ATC
Bretigny

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Connecting to the Real World
Niedergl&t a Lt
\
@ sovsise Lagern Radar arenas N\ ATC
ee Lidl Schweiz | \ Bretigny
XN ROTI
(a ] Oberglatt \
S Sa Sb \
—_—_—— —. ghafen
De hy — A urich
a te L51 |
> 9 =
Rumlang Pst] Kloten
Seilpark Zurich @)
.
—— YOU ARE CONNECTED To A
VofehPLeRge 4
Danikon
ATC MSG 1/2 MSG
44432 Lepy>tNew
Seebad Katzensee Opfikon
```

## Slide 13

## Slide 14

Most of Pilot - ATC Comms still runs on Voice via VHF!

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Most of Pilot - ATC Comms still runs on Voice via VHF!
At least 13 other unauthorised transmissions were reportedly
H acke rs Attack Ai r Traffic Co ntrol received by aircraft and Melbourne Air Traffic Services
Centre over a two-week period.
By DAVID MORGAN - : : :
x The hoax caller is thought to have found a way to tap into the air
traffic control frequency, allowing them to communicate directly
A different kind of hijacking is taking place in the skies. with the planes and control towers.
Britain’s Civil Aviation Authority has issued a safety alert about a new thri
passengers: hackers taking over air traffic control transmissions and givit
bogus orders.
The number of incidents in which radio hackers have broken into freque!
bv British air traffic controllers and given false instructions to pilots, or bri
Extreme frequency congestion ting rise. There were three such incide
leads to near miss this year, 20. a
7 News Melbourne @ vy
By NASA - November 23, 2021 - @7NewsMelbourne
This is an excerpt from a report made to the Aviation Safety Reporting System. BREAKING: Major security breach at @Melair with radio
The narrative is written by the pilot, rather than FAA or NTSB officials. To communications to incoming passenger flights hacked. #7News
maintain anonymity, many details, such as aircraft model or airport, are often 7:02 AM - Nov 7, 2016
scrubbed from the reports.
```

## Slide 15

#### There must be a better solution - What is CPDLC?

- Controller Pilot Data Link Communications allows air traffic controllers and pilots to communicate via text messages.

- A subset of CPDLC messages is clearances, emergency messages and free text.

- CPDLC is an alternative to traditional VHF voice and has gained widespread adoption due to its operational efficiency, reduced voice channel congestion, decreased human error, and is **highly trusted by pilots** .

## Slide 16

#### CPDLC Deployment Types

- **FANS-1/A+ over ACARS** (HF, VHF, Satcom; used in long-haul/transoceanic operations)

- **ATN B1 over VDL Mode 2** (higher data rates, integrated with radar/transponder; mandatory above FL285 in Europe since 2013).

## Slide 17

#### Which CPDLC?

Protected Mode CPDLC (PM-CPDLC) is an enhanced version of ATN-B1 CPDLC designed to “improve the reliability and security of air-ground data communication”

## Slide 18

#### Unsecured, Yet Uncompromised

- ➢ **No cryptographic authentication**

- ➢ **20+ years without a breach**

- ➢ **No recorded compromises**

- ➢ **No prior practical attacks in the literature**

## Slide 19

Many Airspaces Mandate CPDLC

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Many Airspaces Mandate CPDLC
Update - 29 Sep 2025
Eurocontrol has confirmed that from 4 Nov 2025, the IFPS (Integrated Initial Flight Plan Processing System) will
[Eutomatically reject any fight plans fled above FL265 unless CPDLC Is filed correctly. ]
IFPS is the central system that processes and validates all fight plans in European airspace. If your plan is filed
incorrectly, it will be rejected, and you won't be able to depart until the error is fixed.
To avoid rejection:
+ If equipped:
~ Field 10a: 31
~ Field 18: CODE/XXX (Mode S hex code)
+ If exempt from the mandate or CPDLC is unserviceable:
~ Field 10a: Z
- Field 18: DAT/CPDLCX
Important: Do not file both J1 and DAT/CPDLCX together, and do not leave both out. Either scenario will result in
automatic rejection by the IFPS system.
Also important: You don't need to file either J1 nor CPDLCX if your requested level is below FL285.
Also also important: Eurocontrol has also advised separately that if CPDLC is unserviceable, you may continue to operate
above FL285 for up to 10 days under MEL relief, provided the flight plan is filed correctly using DAT/CPDLCX. After this
period, you must either fix the issue or operate below FL285.
Also also also important: On 4 Nov 2025, IFPS will be unavailable between 2100-0000 UTC for a system upgrade. The
outage is expected to last about one hour, but up to two hours if a rollback is needed. During this time, no flight plans can
be filed or validated, so submit plans in advance.
€
Recommended Practices for CPDLC in Europe
- 2026 -
| CPDLC Logon is mandatory in most of European airspace. }
CPDLC usage helps to prevent Loss of Communication incidents and significantly improves ATC capacity.
Your participation and commitment is key!
Preparation for Log-On
ATC LOGON/STATUS 172
= FMC/CDU Flight INIT: ett
= Check DEP/ARR airport, load route if available
= Valid/correct FLT NBR (callsign) Bitar ocuayonrgzy,
= Ensure ATN logon for Europe —> not FANS1/A
= Prepare first ATC Logon address
= Chart provider, AIP or SID
When to Log-On Treacy 1
10Mins + 3
> Prior > croc #
= As soon as possible, considering your company’s SOPs SF “crnering! SP
= According to ICAO: see picture i
Good practices:
= Don’t know the logon address? Log-On failed? Ask ATC by voice!
= Check CPDLC connection after passing 10.000 ft
= Report UNABLE CPDLC unless the issue is due to known GNSS
interference
```

## Slide 20

PM-CPDLC ATN-B1 protocol stack: Key Elements

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
PM-CPDLC ATN-B1 protocol stack: Key Elements
Layer 6 (Application) _ CPDLC Message
Layer 6 (Presentation) = Protected PDU @---- PM-CPDLC checksum
Layer 6 (Presentation) — ICAO Fully Encoded Data
Layer 5 (Session) ATN Context Management @ _ Logon /Setup/Maintenance
Layer 5 (Session) ACSE X.227 e-. : _—_ . i Application Setup
Layer 5 (Session) SPDU X.225 e = : Session Type Setup
@- Connection Type Setup
Layer 4 (Transport) COTP X.224
° ATN checksum
Layer 3 (Network) CLNP X.233 e IDRP
Layer 2 (Datalink) X.25 Packet ° ES-IS.
e CRC 16
Layer 2 (Datalink) AVLC Frame
e-., XID
e Reed Solomon FEC
Layer 1 (PHY) VDL Mode 2 .
e-. PN scrambling
Layer 1 (PHY) D8PSK @ 31.5 Kbps
```

## Slide 21

#### Link Establishment

Broadcast

Link Establishment  Request
Link Establishment  Response

## Slide 22

#### X.25 Handshake

Broadcast

Link Established
Accepted  [ES-IS IS HELLO]
Call
Request  [ES-IS IS HELLO]
Call

Note:  * **ES-IS** is analogous to **ARP**

## Slide 23

#### The Network Layer

Broadcast

Link Established
ES-IS
IDRP Init.

Note:  * BGP is an instance of IDRP *  IDRP is managed by a FSM

## Slide 24

#### The Transport Layer

Broadcast
Link Established
IDRP  [ESTABLISHED]
Transport Session
ES-IS

## Slide 25

#### Connection Overview

Broadcast
Note: *CPDLC is a Ground Initiated Application in this case.
Link Established
IDRP  [ESTABLISHED]
Session [ATN Context Management *]
Session [PM CPDLC Application *]
Transport Session
Transport Session BIS
ES-IS

Note: *CPDLC is a Ground Initiated Application in this case.

## Slide 26

Full Reverse Engineering Setup

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Real World
Environment
ATC ie =
ad ire)
4
é
a
4
XXX
/
ras
—>~_—__
Global
CPDLC
Network
boa ee
ess Channel
Unilink
UL 801 CMS
Full Reverse Engineering Setup
VHF Antenna
Faraday Cage
(RF Isolation)
—p>
———> |
FMS
UNS-1EW
> ails
USRP B210
Attacker Setup
RTL-SDR dumpVDL2
Capture
=
RGS/DoS Frames
Transmission
Attacker Msg Flow
Real-world Msg Flow
```

## Slide 27

#### Multi-Year Reverse Engineering Ordeal

- Huge complexity

- Very scattered documentation

- Missing documents

- Unfindable checksums

- Obscure integrity checks

- Undocumented elements

## Slide 28

#### One example: PM-CPDLC checksum

p
a Addition is performed in one’s
complement arithmetic
y
l
Init: C0 = C1 = C2 = C3 = 0
o
a For each byte x:
C0 = C0 + x
d
C1 = C1 + C0
Content
ATN-32  C2 = C2 + C1
Protected Output C3 = C3 + C2
Checksum
Flight  Message
number Final checksum:
X0 = -(C0 + C1 + C2 + C3)
X1 = C1 + 2*C2 + 3*C3
Facility  X2 = -(C2 + 3*C3)
Designation X3 = C3
Return:
Aircraft
ICAO  (X0,X1,X2,X3)

## Slide 29

Let’s explore the stack

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Let’s explore the stack
Layer 6 (Application)
Layer 6 (Presentation)
Layer 6 (Presentation)
Layer 5 (Session)
Layer 5 (Session)
Layer 5 (Session)
Layer 4 (Transport)
Layer 3 (Network)
Layer 2 (Datalink)
Layer 2 (Datalink)
Layer 1 (PHY)
Layer 1 (PHY)
CPDLC Message
Protected PDU @--|------
ICAO Fully Encoded Data
ATN Context Management @
ACSE X.227
SPDU X.225
COTP X.224
CLNP X.233
X.25 Packet
AVLC Frame
VDL Mode 2
eoe@¢ @
D8PSK @ 31.5 Kbps
~ PM-CPDLC checksum
Logon/Setup/Maintenance
Application Setup
- Session Type Setup
Connection Type Setup
» ATN checksum
IDRP
ES-IS
CRC 16
- XID
Reed Solomon FEC
PN scrambling
```

## Slide 30

#### Let’s explore the stack

We start here

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Let’s explore the stack
Layer 6 (Application)
Layer 6 (Presentation)
Layer 6 (Presentation)
Layer 5 (Session)
Layer 5 (Session)
Layer 5 (Session)
_ CPDLC Message
_ Protected PDU @-}---- PM-CPDLC checksum
— ICAO Fully Encoded Data
Logon/Setup/Maintenance
ATN Context Management @--------- +
ACSE X.227 @eesssssssesetsenesnetntes Ee snteneenenee - Application Setup
SPDU X.225 - Session Type Setup
Connection Type Setup
Layer 4 (Transport) COTP X.224
» ATN checksum
Layer 3 (Network) CLNP X.233 e IDRP
Layer 2 (Datalink) X.25 Packet e- ES-IS
e- CRC 16
Layer 2 (Datalink) AVLC Frame . po We start here
e- Reed Solomon FEC
La 1 (PHY
yet ( ) Web Mise @-). -- PN scrambling
Layer 1 (PHY)
D8PSK @ 31.5 Kbps
```

## Slide 31

#### AVLC Layer

dumpvdl2

## Slide 32

### AVLC  Frame: Closer Look

**Sender Address**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
AVLC Frame: Closer Look
Sender
Address
2 Label: _d Blk id: A More: © Ack: 1
```

## Slide 33

### AVLC  Frame: Closer Look

**Sender Receiver Address Address**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
AVLC Frame: Closer Look
Sender Receiver
Address Address
5) fe
> (4B7FFF (Aircraf
2 Label: _d Blk id: A
```

## Slide 34

### AVLC  Frame: Closer Look

**Sender Receiver Address Address**

**Type && Sequence numbers**

## Slide 35

#### The backbone: Information frame

Sender  Receiver
Address Address
Type && Sequence numbers
Payload

## Slide 36

#### Error handling frame : AVLC FRMR

Sender
Receiver
Address
Address
Type && Params

## Slide 37

#### AVLC FRMR: Closer Look

Sender
Receiver
Address
Address
Type && Params
Faulty Frame LCF

Any frame can be flagged and the aircraft trusts it immediately, what could go wrong?...

## Slide 38

1st DoS vector: **Malicious AVLC FRMR Injection**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
1st DoS vector: Malicious AVLC FRMR Injection
COMM STATUS MSG
VHF 136.975MHZ
AOA:NOCOMM/NO SERVICE
ATN:NOCOMM/NO CIRCUIT
COMM CNTRL®
ADVISORY 14272
¢ATC DISCNECT RETURN
NAV VNAV DTO LIST PREV
FPL PERF TUNE MENU NEXT
ATC
_ Normal Protocol Executio
n
we
>
Target Frame
Attacker
7
\
f
\
'
; Attack
| \__AVLC FRMR [Target Frame]
f <
i Updates internal state i
<—
i_ AVLC UA
| AVLC FRMR x
r > f
ig tink Reset >
i \ i
ATC Attacker
```

## Slide 39

But it doesn’t get easier than this… right?

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
But it doesn’t get easier than this... right?
| __
ABSOLUTE = } ICAO
```

## Slide 40

#### Deeper dive into link management

It might look intimidating but we don’t need to understand all of it!

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Deeper dive into link management
T3 Expiration : Al
Receipt of Link
Establishment
Receipt of
Event : Al VME Handoff Link
Command : Ad Handoff
VME Creates ink Receipt of vise ro Pending Receipt of
New LME Unavailable XID_RSP_LCF : A3 rl Sat (S3)
(SO)
2 Ex XID_RSP_HO (F=1) : A6
9 Link Handoff HO (F=1)
N2 Exceeded : A
Refusal : A10
Receipt of Disc.
Notification from DLE : A3
Receipt of
XID_CMD_HO (P=1) : A5,A6
Double-
Links.
Connected
(S4)
TGS Timeout : A8&
It might look intimidating but we don’t need to understand all of it!
```

## Slide 41

What we actually care about

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
What we actually care about
T3 Expiration : Al
Receipt of Link
Establishment
Event : Al Link
Establishment
Receipt of Pending Receipt of
(SI) XID_RSP_LE : A2
XID_RSP_LCF: A3
N2 Exceeded : A9
Receipt of Disc.
Notification from DLE : A3
```

## Slide 42

#### Keep it simple and stupid

**Stateless** frame!

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Keep it simple and stupid
T3 Expiration : Al
Receipt of Link
Establishment
Event : Al
Link
Establishment
Pending
(S1)
Receipt of
Receipt of
XID_RSP_LE : A2
XID_RSP_LCF: A3
N2 Exceeded : A9
Receipt of Disc.
Notification from DLE : A3
DST addr SRC addr | LCF=0x43} FCS
(4 B) (4 B) (1 B) (2 B)
Stateless frame!
```

## Slide 43

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
rp But.an attacker'can only target one
; Dos on CPDLC is ie a2 airraft at atime .. ight?
:
ote te
[
```

## Slide 44

#### Bonus Points: Broadcast DoS

AVLC U DISC (Stateless)

- We leverage **Data Link State Machines** as an Attack Vector

● Escalation from a single targeted DoS to **disruption of all aircraft in range** using Broadcast address

## Slide 45

DoS outcome

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
COMM STATUS MSG
VHF 136.975MHZ
AOA:NOCOMM/NO SERVICE
ATN:NOCOMM/NO CIRCUIT
COMM CNTRL>
ADVISORY 14272
“ATC DISCNECT RETURN?
NAV VNAV oT0 LIST PREV
FPL PERF TUNE MENU NEXT
DoS outcome
LOG ON
CURR ATC: NEXT atc:
CALLSIGN
EECS999 hear
ATSU:ATN bs
*LFPYTEST LSZH
NO SERVICE ETD
“LOS ON wee
UNILINK MENU RETURNS
VNAV DTO LIST
FPL PERF TUNE MENU
ON/OFF
ENT
UNIVERSAL
LOG ON MSG
RECOMMEND CONTACTING
ATC VIA VOICE ame
ATSU:ATN DEST
. SLEPYTEST LSZH
LOG ON TIMEOUT ETD
LOG ON ore-2
18312
UNILINK MENU RETURN>
VWAV DTO LIST PREV
PERF TUNE MENU NEXT
c E F
G
N
T
Zz
D
K
Qa
Ww
```

## Slide 46

#### So much more remains to discuss

|…|
|---|

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
So much more remains to discuss
Layer 6 (Application)
Layer 6 (Presentation)
Layer 6 (Presentation)
Layer 5 (Session)
Layer 5 (Session)
Layer 5 (Session)
_ CPDLC Message
_ Protected PDU @-}---- PM-CPDLC checksum
— ICAO Fully Encoded Data
Logon/Setup/Maintenance
ATN Context Management @---------- re ene
ACSE X.227 rea te ae temrenee ete --emveee Application Setup
SPDU X.225 - Session Type Setup
Connection Type Setup
Layer 4 (Transport) COTP X.224
» ATN checksum
Layer 3 (Network) CLNP X.233 e IDRP
Layer 2 (Datalink) X.25 Packet e- ES-IS
e- CRC 16
Layer 2 (Datalink) AVLC Frame
o-.- - XID
e- Reed Solomon FEC
La 1 (PHY
yet ( ) Web Mise @-). -- PN scrambling
Layer 1 (PHY)
D8PSK @ 31.5 Kbps
```

## Slide 47

#### Attack surface is VERY large

Our work focuses on DoS attacks at the protocol level, excluding jamming

**We found four attack types:**

- ➢ AVLC FRMR injection

- ➢ Broadcast AVLC U DISC

- ➢ Control flow injection

- ➢ Malformed payload injection

## Slide 48

Attacking the DMs: An IMSI Catcher for Aircraft

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Attacking the DMs: An IMSI Catcher for Aircraft
CHALLENGE IMPLEMENTATION
[es
‘8 Multiple layers, each
& with rules and timing
Qa
AO
@ te
Mimic a legitimate
erumeealatatt connection
Numerous parameters
and uirrequts
Obscure Integrity checks
at several alipoints
Stable long-lived connection
£3
Se:
Enuuletee connection as
a finite-state machine
Progresses step by step
through all layers
Negotiates values and
maintains session state
Reverse engineer and generates
required checks
Maintain session state over time, f
| handling all necessary steps and
checks to keep the link active
24h
```

## Slide 49

#### Rogue Ground Station

CPDLC connection

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Rogue Ground Station
a
CPDLC connection
(yp)
BA
Attacker ATSU
(Rogue Ground Station) (Ground Station)
```

## Slide 50

#### Rogue Ground Station

Rogue Disconnect CPDLC connection

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Rogue Ground Station
a
CPDLC connection
(y)
BA
Attacker ATSU
(Rogue Ground Station) (Ground Station)
```

## Slide 51

#### Rogue Ground Station

CPDLC connection
X
Rogue Disconnect

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Rogue Ground Station
(y)
BA
Attacker ATSU
(Rogue Ground Station) (Ground Station)
```

## Slide 52

#### Rogue Ground Station

Broadcast RGS Information Frame

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Rogue Ground Station
Broadcast RGS
Information Frame
(y)
BA
Attacker ATSU
(Rogue Ground Station) (Ground Station)
```

## Slide 53

#### Rogue Ground Station

Initiate Link Establishment
Broadcast RGS
Information Frame

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Rogue Ground Station
Initiate Link Establishment
Broadcast RGS
Information Frame
Attacker ATSU
(Rogue Ground Station) (Ground Station)
```

## Slide 54

#### Rogue Ground Station

CPDLC connection

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Rogue Ground Station
(y)
BA
Attacker ATSU
(Rogue Ground Station) (Ground Station)
```

## Slide 55

#### Rogue Ground Station

Rogue CPDLC Session
Attacker CPDLC Messages

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Rogue Ground Station
(y)
BA
Attacker ATSU
(Rogue Ground Station) (Ground Station)
```

## Slide 56

Demo Time! Demo Time!

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Demo Time! = Sms ’ Demo Time!
=i ce
wos
fa |
\
```

## Slide 57

Impact of Rogue Ground Station

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Impact of Rogue Ground Station
System-level risk:
A rogue ground station can establish a legitimate
ATN/CPDLC session and obtain the same
operational privileges as an authentic ATC. Because
messages are protocol-compliant and appear
authenticated, flight crews may treat malicious
clearances as genuine.
Key takeaway:
The threat is abusing the existing trust in CPDLC
communication. A rogue ground station can blend
malicious instructions with legitimate traffic, making
detection difficult until operational consequences
emerge.
The following scenarios were reviewed with commercial pilots and
controllers and identified as realistic, high-impact examples:
»}> Trajectory Manipulation
False lateral clearance (UM79 PROCEED DIRECT)
» Diverts aircraft into conflicting traffic flows, holding stacks, or restricted
airspace.
{Separation Loss
False altitude clearance (UM21 CLIMB TO / UM20 DESCEND TO)
» Places aircraft at an occupied flight level, potentially triggering TCAS
resolution advisories.
ss Terminal Area Disruption
Modified approach clearance (UM80 CLEARED VIA)
~ Forces unexpected procedure changes during high-workload phases of
flight.
A Trust Exploitation
Fabricated emergency or operational messages (UM169)
+ Creates confusion, unnecessary diversions, and erosion of confidence in
CPDLC.
```

## Slide 58

#### Thousands of Affected Aircraft in Europe Alone

**Adoption Rate 83%**

**Filed CPDLC Capability (J1)** Of European flight movements in early 2024. **Actual Usage 42% Active CPDLC Usage** Equipped does not mean logged on or actively used.

###### **Aircraft Population**

**22,948**

**Daily Flight Traffic 22,948 ~29,300 flights/day Individual Civil Aircraft** Out of 10.7 million total flights in Europe in 2024. Operating at least once in the EUROCONTROL Network Manager **Daily CPDLC Volume** area in 2022.

**24,000** Equipped flight legs / day **12,000**

Actually active legs / day

Sources: EUROCONTROL Datalink Operations (2024-02) | European Aviation Overview (2025-01)

## Slide 59

Is the US CPDLC safe/secure? No, just easier…

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Is the US CPDLC safe/secure? No, just easier...
On the Implications of Spoofing and Jamming Aviation Datalink
Applications
Harshad Sathaye Guevara Noubir Aanjhan Ranganathan
Khoury College of Computer Sciences Khoury College of Computer Sciences Khoury College of Computer Sciences
Northeastern University, Boston, USA Northeastern University, Boston, USA Northeastern University, Boston, USA
to note that ATN B1 does not support ADS-C application [26]. This
work focuses on FANS 1/A applications and targets specific CPDLC,
and ADS-C messages exchanged using the ACARS network. ATN
B1 and FANS 1/A support different message sets. However, these
attacks can be used against ATN B1 applications with some changes.
```

## Slide 60

### How did we end up here…?

**Aviation Design Philosophy** Rigid safety-first principles prioritize extreme reliability and long-proven hardware, choosing stability over the rapid adoption of modern commercial technology.

**Long Upgrade Cycles** Extremely complex certification processes and high integration costs mean deployment cycles often span decades, keeping active aircraft tied to legacy systems.

**The Savior that never comes: Datalink over IP** While IP-based networks promise a modern security standard, rollouts face constant technical and logistical delays, remaining a distant future solution.

## Slide 61

#### What Can Be Done About This?

Realistically right now? Probably nothing. Maybe make pilots aware? Safety engineering DOES help for now. (We still plan to fly back after DEF CON…)

**Aviation community waiting for security patches**

## Slide 62

#### What Can Be Done About This (longer term)?

##### **Improving Standards**

- **SDS to DTLS:** Adopting DTLS for authentication and replay protection.

- **Timeline:** Trials expected in the 2030s; rollout faces cost and delay challenges.

##### **Academic Research**

- **Limited Proposals:** Current landscape includes HIP, ECC, and AKAASH.

- **Focus:** Advancing formal verification efforts.

**Physical Layer Intrusion Detection**

- **Strategies:** Spectrum monitoring, RF fingerprinting.

## Slide 63

#### Disclosure

Disclosed to everyone we could find:

- Aviation ISAC

- European Aviation Safety Agency (EASA)

- ● EUROCONTROL

- US CISA/FAA

- Airbus

- Boeing

- Pilatus

- Swiss Aviation Authorities & ANSP

- British Airline Pilots' Association

- Lufthansa Group

- Universal

- Collins

## Slide 64

#### Disclosure Stories (1/3)

“ [...] I'm really impressed with your findings (they were to expect as **the industry talks about these issues for ages now and nothing really happens** ). [...]

— European Airline

“ [...] Having been **harping on about CPDLC**

**vulnerability for years** , I'm so pleased that we now have proof that it can indeed be 'spoofed'. In the past I **have even had a categoric 'not possible' from a senior comms engineer, citing that handshake protocols would prevent any successful rogue connection!** [...]

- European Pilots Association

## Slide 65

#### Disclosure Stories (2/3)

# “

[...] On Monday, the **Product Security community of interest (COI), which has subject matter experts across manufacturers, ANSPs, airlines, and airports, met and had a healthy discussion on the content** [...] The COI is including this topic in their next monthly meeting agenda, and I will again ask the group for any questions and feedback to provide to you. [...]

— Aviation ISAC

## Slide 66

Disclosure Stories (3/3): FAA

Disclosed via CISA/VINCE on 2025-08-27 Confirmed contact to FAA on 2025-09-17

Then… nothing for 8 months.

Upon acceptance of DEF CON talk they finally started reading the paper.

## Slide 67

## Key Takeaways

**01**

**CPDLC is critically insecure - like all other aviation protocols**

**02**

**Complexity != Security**

More ancient protocol complexity does not equal security.

**03**

**15 Years of Inaction**

Nobody seems to be doing anything about this critical issue despite 15 years of DEF CON talks.

We have demonstrated that we can fully pwn the CPDLC system, exposing fundamental gaps in global aviation communications.

## Slide 68

#### To appear in Usenix Sec’26 next week!

You can find it here: <u>https://www.usenix.org/conference/usenixsecurity26/presentation/ziazi</u>

We do not release the code thought ;)

## Slide 69

Thank you for your attention!

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ATC MSG 1/1 MSG
14182 LFPY>TNEW
THANK YOU FOR YOUR
INTEREST.
(SENT 14182)
Thank you for
eLFPYTEST CNECT RETURNS your attention!
UNE MENU NEXT
```
