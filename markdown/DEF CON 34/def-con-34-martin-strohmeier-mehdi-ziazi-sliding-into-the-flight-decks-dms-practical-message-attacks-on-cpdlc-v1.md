---
title: "Sliding into the Flight Deck’s DMs Practical Message Attacks on CPDLC"
speakers: ["Martin Strohmeier", "Mehdi Ziazi"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: 2026
source_pdf: "DEF CON 34/DEF CON 34 - Martin Strohmeier, Mehdi Ziazi - Sliding into the Flight Deck’s DMs Practical Message Attacks on CPDLC - v1.pdf"
pages: 69
sha256: "ed586be9f959cdc136a458dca7d17d53b95832fbadc79723bbd1658f7ef32b1c"
text_chars: 25825
ocr_pages: 35
has_ocr: true
redacted_secrets: 0
ocr_confidence: 89.5
ocr_unreliable_blocks: 0
vision_verified_pages_changed: 66
vision_verified_pages: 69
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:37:59Z"
---
# Sliding into the Flight Deck’s DMs Practical Message Attacks on CPDLC

**Speakers:** Martin Strohmeier, Mehdi Ziazi  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Martin Strohmeier, Mehdi Ziazi - Sliding into the Flight Deck’s DMs Practical Message Attacks on CPDLC - v1.pdf` (69 pages)


## Slide 1

# Sliding into the Flight Deck's DMs: Practical Message Attacks on CPDLC

Mehdi Ziazi — Martin Strohmeier

Artwork slide. An airliner climbs over a stylised world map and a hooded figure at a bank of monitors; a satellite at the top right is linked to the aircraft by a red beam. Overlaid callouts, clockwise from the top left:

- **⚠ CONNECTION INTERCEPTED**
- **SATCOM LINK UNSECURE**
- **MESSAGE MANIPULATION** — Injection / Modification / Deletion / Replay, beside a red warning triangle
- A terminal pane with a red pixel-skull:

```text
> ATTACKER@SYSTEM:~$
> INTERCEPTING CPDLC...
> DECODING MESSAGE...
> ALTERING CONTENT...
> SENDING FAKE CLEARANCE...
> ATTACK SUCCESSFUL
```

- A cockpit display reading `CPDLC CONNECTED ✓` and `LOGON COMPLETE ✓`
- **ACCESS GRANTED**, under a padlock icon
- **CPDLC CHANNEL VULNERABLE**

Down the left edge, a chat-bubble thread of CPDLC messages, each with a double tick:

| From | Time | Message |
| --- | --- | --- |
| ATC | 18:42Z | CLX123 / CLIMB FL380 / REPORT LEVEL |
| CLX123 | 18:43Z | WILCO |
| ATC | 18:44Z | EXPECT TURBULENCE FL340-FL360 |
| CLX123 | 18:45Z | ROGER |

Logos: CYD Cyber Defence Campus, ETH zürich.

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

### Aircraft Have DMs Now

A cockpit MCDU showing a CPDLC uplink, beside a photo of two pilots on the flight deck, one holding an EFB tablet with an "ATC Direct - GVA" message thread open.

```text
   1231z ATC UPLINK  2/4

AFTER CMK CLEARED TO

KBED ARPT AS FILED
/FREE TEXT
RUUDY5, CLIMB VIA SID
/FREE TEXT
EXPECT FL190 10 MIN AFT

--CONTINUED--

<ATC INDEX             LOG>
```

## Slide 5

### Inspiration: DEF CON 20 / Blackhat 2012 Talks

Three overlapping screenshots:

- A video still captioned **DEF CON 20 - RenderMan - Hacker + Airplanes = No Good Can Come Of This**, playing at `0:00 / 50:55`, chapter marker "Intro". Behind it, a PlanePlotter window showing aircraft tracks over a road map; its title bar and toolbar are too low-resolution to transcribe.
- A title slide reading **Ghost is in the Air(Traffic)** over an aircraft icon, with `Andrei Costin <andrei.costin@eurecom.fr>` and `Aurelien Francillon <aurelien.francillon@eurecom.fr>`, and the black hat USA 2012 and EURECOM Sophia Antipolis logos.
- A photo of a speaker at the black hat BRIEFINGS USA 2012 podium.

## Slide 6

### That got everyone's attention

A collage of 2012-2013 press clippings:

**CSO — News.** "Hackers say coming air traffic control system lets them hijack planes / FAA says it can spot hacking attempts, but won't allow independent 'stress tests'". By Taylor Armerding, CSO, January 11, 2013 08:12 AM ET. Share widgets read `Share 23`, `+1`, `Like 143`, `More`.

> CSO - An ongoing multibillion-dollar overhaul of the nation's air traffic control system is designed to make commercial aviation more efficient, more environ… friendly and safer by 2025.
>
> Sleeping air traffic controllers get federal wakeup
>
> But some white-hat hackers are questioning the safety part. The Next Genera… Transportation System (NextGen) will rely on Global Positioning Systems (GPS) instead of radar. And so far, several hackers have said they were able to demonstrate the capability to hijack aircraft by spoofing their GPS components.

**CNN.** "Researcher: New air traffic control system is hackable". By Heather Kelly, CNN. July 26, 2012 -- Updated 2249 GMT (0649 HKT) | Filed under: Web

**"Air Traffic Control of the Future Is (Still) Incredibly Hackable"**

**"Defcon Researchers Build Tool To Track the Planes of the Rich and Famous"**

**"Air Traffic Controllers Pick the Wrong Week to Quit Using Radar"**

**"Hacker Shows Air Traffic Control Danger With 'Ghost Planes'"** — Posted 09.26.2012 | Travel. Read More: Air Force One, Air Traffic Control, Faa, Travel News, Air Travel, Airlines, Hacking, Black Hat, Travel News

> Andrei Costin, a Cypriad hacker, gave an unnerving demonstration outlining the weaknesses of air traffic control systems today at the Black Hat hackin…
>
> Read Whole Story

**Forbes-style clipping.** SECURITY | 7/25/2012 @ 1:54PM | 17,036 views — "Next-Gen Air Traffic Control Vulnerable To Hackers Spoofing Planes Out Of Thin Air". 4 comments, 3 called-out. + Comment Now  + Follow Comments

## Slide 7

### Aviation Industry's Answer

Overlapping clippings; several are partly hidden where they overlap, and three passages are boxed in red.

**"THE SKY IS CALLING, NOT FALLING"**

> Tim Taylor talks about the disturb… as if the ongoing roll-out of ADS-B… peril.  He recommends:
>
> 1) <u>Relax</u>, the situation is OK, bordering on "normal." – The FAA says it has procedures in place to prevent that, and that system security is integral to ADS-B technical specifications. At minimum the subject g… engineering circles – by people who are… who have had more than a decade to co… over this.
>
> - tons of redundancy
>
> [The FAA said that the ADS-B system is secure] and… displays. "An FAA ADS-B security action plan identified and mitigated risks and monitors the progress of corrective action," an FAA spoke… told AIN.
>
> A spokeswoman for key ADS-B… security certification and accreditation. The accreditation recognizes that the system has substantial information security features built in, including features to protect against…spoofing attacks. [This] is provided through [multiple means of independent validation] that a target is where it is reported to be."

Second clipping, top right:

> Indeed, the FAA expounded on a larger concern–the number of functions that prudently should be contained in one box of avionics. Just as the value of real estate is based on the cliché, "location, location, location," [air safety is built on the trinity of "redundancy, redundancy, redundancy."] If TCAS

**AINonline** (nav: BIZAV / AIR TRANSPORT / DEFENSE; section AIR TRANSPORT) — "Hackers, FAA Disagree Over ADS-B Vulnerability", by Matt Thurber - August 21, 2012, 4:15 PM

**Slashdot** — "FAA Denies Vulnerabilities In New Air Traffic Control System". Posted by Soulskill on Wednesday August 22, 2012 @05:23PM, from the what's-the-worst-that-could-happen dept.

## Slide 8

### A 15 year journey on practical aviation hacking

A diagram of aviation data links in three stacked bands, with the year each was attacked in green, and a companion bar chart.

**Aircraft-to-Satellite** — three satellite/aircraft pairs:

- **2022/23 GPS** — a dashed arrow from the satellite down to the aircraft
- **2024 ADS-C, SADS-B** — a double-headed arrow between aircraft and satellite
- **2020 CPDLC, ACARS** — a double-headed arrow between aircraft and satellite

**Aircraft-to-Aircraft** — two aircraft joined by a double-headed arrow: **2024 TCAS, ADS-B, Mode A/C/S**

**Aircraft-to-Ground** — four link groups:

| Link group | Year | Arrow drawn |
| --- | --- | --- |
| ADS-B, Mode A/C/S, MLAT | 2012-25 | aircraft → ground dish (one direction) |
| FIS-B, TIS-B, Mode A/C/S (Interrogations) | — | aircraft → ground dish (one direction) |
| ACARS, Voice, **CPDLC**, PSR | 2017 | double-headed, aircraft ↔ ground dish |
| DME, NDB, VOR | 2026 | double-headed, aircraft ↔ ground navigation aid |
| ILS | 2020 | dashed arrow from the tower up to an aircraft |

`CPDLC` is boxed in red and a large red arrow points at it. The ground row is captioned **ATC ground stations** on the left and **Ground-based navigation aids** on the right; "Voice" and "PSR" are partly covered by the red box and arrow.

Right-hand panel, **Use during flight phases** — horizontal bars against an axis whose ticks read Ground, Departure, En-route, Approach, Ground:

| Technology | Spans |
| --- | --- |
| GPS | Ground → Ground (all phases) |
| VOR/DME/NDB | Departure → Approach |
| ILS | Approach → Ground |
| VHF | all phases |
| PSR | all phases |
| Mode A/C | Departure → Approach |
| Mode S | all phases |
| ADS-B | all phases |
| MLAT | all phases |
| CPDLC/ACARS | all phases |
| TCAS | Departure → Approach |
| FIS-B / TIS-B | all phases |

## Slide 9

#### One Lesson Learned: *Full* Live Demos Required

**No crypto on paper = trivial, right?**

Lots of radio-frequency security research has been conducted in simulated hardware/software but no (public) real-world tests are available.

A screenshot of the RTCA standard "Minimum Operational Performance Standards for Universal Access Transceiver (UAT) Automatic Dependent Surveillance - Broadcast (ADS-B)" — sidebar `RTCA UAT MOPS DO-282A ADS-B` — with `security` typed into the Adobe Reader find box and the dialog reading "Reader has finished searching the document. No matches were found."

Caption: DO-282A Standards: Searching for "security" yields "No matches found"

###### **The Industry Response**

You show them the hacks in theory or simulation and you basically get the same responses: _"This is not possible in practice"_ — for some magical unexplained reasons.

A "Move along, nothing to see here." meme image.

## Slide 10

Consequence: The Original Avionics Security Lab

## Slide 11

#### Extension: The CPDLC Hacking Lab

Left: a photo of a shielded test enclosure with an RF feed running to a ground-plane whip antenna on the floor.

Right: a block diagram of the test rig.

- **FMS UNS-1Ew** ↔ **Unilink UL-801 CMU** over **A429** (arrowheads at both ends)
- **SSDTU** ↔ **Unilink UL-801 CMU** over **ETHERNET** (arrowheads at both ends)
- **VHF ANTENNA** ↔ **Unilink UL-801 CMU** (green double-headed arrow)

Thanks to Q.C.M. quality control management AG!

## Slide 12

#### Connecting to the Real World

A Google map of the area north-west of Zurich (labels visible: Niederglatt, Dielsdorf, Lidl Schweiz, Oberglatt, Flughafen Zürich, Rüti, Buchs, Dänikon, Dällikon, Rümlang, Kloten, Seilpark Zürich, Seebad Katzensee, Opfikon, Mövenpick H… Zürich Regens…) with three annotations overlaid:

- A dropped pin labelled **Skyguide Lägern Radar**, with a photo of the radome tower beside it.
- **ATC Bretigny** in red, at the head of a dashed line that runs down to the **Flughafen Zürich** marker.
- A dashed double-headed arrow between the Lägern radar photo and Flughafen Zürich, and a solid double-headed arrow between the radar photo and a cartoon aircraft sitting over the MCDU photo.

The MCDU shows an uplink from the Brétigny test system:

```text
        ATC MSG 1/2   MSG
1443Z LFPY>^NEW
YOU ARE CONNECTED TO A
TEST SYSTEM,PLEASE
CONFIRM NO CPDLC
INSTRUCTION WILL BE
EXECUTED
(SENT 1443Z)
<-STANDBY
                     1443Z
<-UNILINK MENU     RETURN->
```

## Slide 13

A "make a meme" image of a bald eagle in front of a US flag:

> WHAT. THE. HELL.
>
> IS A ~~KILOMETER~~

with `KILOMETER` struck through in yellow and **CPDLC** written over it in yellow. Watermark: makeameme.org

## Slide 14

### Most of Pilot - ATC Comms still runs on Voice via VHF!

A collage of press clippings, several partly hidden where they overlap.

**"Hackers Attack Air Traffic Control"** — By DAVID MORGAN · Aug. 29

> A different kind of hijacking is taking place in the skies.
>
> Britain's Civil Aviation Authority has issued a safety alert about a new thre… passengers: hackers taking over air traffic control transmissions and givi… bogus orders.
>
> The number of incidents in which radio hackers have broken into frequen… by British air traffic controllers and given false instructions to pilots, or bro… …ning rise. There were three such incide… this year, 20.

**"Extreme frequency congestion leads to near miss"** — By NASA · November 23, 2021 ·

> This is an excerpt from a report made to the <u>Aviation Safety Reporting System</u>. The narrative is written by the pilot, rather than FAA or NTSB officials. To maintain anonymity, many details, such as aircraft model or airport, are often scrubbed from the reports.

Right-hand clipping:

> At least 13 other unauthorised transmissions were reportedly received by aircraft and Melbourne Air Traffic Services Centre over a two-week period.
>
> The hoax caller is thought to have found a way to tap into the air traffic control frequency, allowing them to communicate directly with the planes and control towers.

A tweet, with an embedded 7NEWS FIRST video still:

> 7 News Melbourne ✓ @7NewsMelbourne
>
> BREAKING: Major security breach at @Melair with radio communications to incoming passenger flights hacked. #7News
>
> 7:02 AM - Nov 7, 2016

## Slide 15

#### There must be a better solution - What is CPDLC?

- Controller Pilot Data Link Communications allows air traffic controllers and pilots to communicate via text messages.

- A subset of CPDLC messages is clearances, emergency messages and free text.

- CPDLC is an alternative to traditional VHF voice and has gained widespread adoption due to its operational efficiency, reduced voice channel congestion, decreased human error, and is **highly trusted by pilots** .

A photo of the Universal MCDU shows the current ATC unit:

```text
        ATC MSG 1/1   MSG
1044Z LFPY>^NEW
CURRENT ATC UNIT
LFPYTEST,BRETIGNY,CENTER
(SENT 1044Z)

     ADVISORY          1044Z
<-LFPYTEST CNECT   RETURN->
```

## Slide 16

#### CPDLC Deployment Types

- **FANS-1/A+ over ACARS** (HF, VHF, Satcom; used in long-haul/transoceanic operations)

- **ATN B1 over VDL Mode 2** (higher data rates, integrated with radar/transponder; mandatory above FL285 in Europe since 2013).

A line diagram of CPDLC air-ground paths, drawn over a horizontal baseline labelled **Ground Network (ACARS / ATN)**:

- A satellite at the top, joined to a ground earth-station tower on the left by a line with arrowheads at both ends. The label **SATCOM (FANS 1/A)** has leader arrows to the satellite and to an aircraft.
- A blue ellipse encircling an aircraft, the label **CPDLC/ADS-C (FANS 1/A)**, and a ground radio mast; the label has an arrow up to the aircraft and an arrow down to the mast.
- A second blue ellipse encircling a second aircraft, the label **CPDLC (ATN B1)**, and a second ground radio mast, with the same pair of arrows.
- **ATSU** — a control tower, building and antennas at the right, drawn outside that ellipse, connected to the ground-network baseline.

## Slide 17

#### Which CPDLC?

Protected Mode CPDLC (PM-CPDLC) is an enhanced version of ATN-B1 CPDLC designed to “improve the reliability and security of air-ground data communication”

A line diagram of CPDLC air-ground paths, drawn over a horizontal baseline labelled **Ground Network (ACARS / ATN)**:

- A satellite at the top, joined to a ground earth-station tower on the left by a line with arrowheads at both ends. The label **SATCOM (FANS 1/A)** has leader arrows to the satellite and to an aircraft.
- A blue ellipse encircling an aircraft, the label **CPDLC/ADS-C (FANS 1/A)**, and a ground radio mast; the label has an arrow up to the aircraft and an arrow down to the mast.
- A thick red ellipse encircling a second aircraft, the label **CPDLC (ATN B1)**, and a second ground radio mast, with the same pair of arrows.
- **ATSU** — a control tower, building and antennas at the right, drawn outside the red ellipse, connected to the ground-network baseline.

## Slide 18

#### Unsecured, Yet Uncompromised

- ➢ **No cryptographic authentication**

- ➢ **20+ years without a breach**

- ➢ **No recorded compromises**

- ➢ **No prior practical attacks in the literature**

A line diagram of CPDLC air-ground paths, drawn over a horizontal baseline labelled **Ground Network (ACARS / ATN)**:

- A satellite at the top, joined to a ground earth-station tower on the left by a line with arrowheads at both ends. The label **SATCOM (FANS 1/A)** has leader arrows to the satellite and to an aircraft.
- A blue ellipse encircling an aircraft, the label **CPDLC/ADS-C (FANS 1/A)**, and a ground radio mast; the label has an arrow up to the aircraft and an arrow down to the mast.
- A thick red ellipse encircling a second aircraft, the label **CPDLC (ATN B1)**, and a second ground radio mast, with the same pair of arrows.
- **ATSU** — a control tower, building and antennas at the right, drawn outside the red ellipse, connected to the ground-network baseline.

## Slide 19

### Many Airspaces Mandate CPDLC

Two screenshots side by side.

**Left — Update – 29 Sep 2025**

Eurocontrol has confirmed that from 4 Nov 2025, the IFPS (Integrated Initial Flight Plan Processing System) will [**automatically reject any flight plans filed above FL285 unless CPDLC is filed correctly.**]

IFPS is the central system that processes and validates all flight plans in European airspace. If your plan is filed incorrectly, it will be rejected, and **you won't be able to depart until the error is fixed.**

To avoid rejection:

- **If equipped:**
  - Field 10a: J1
  - Field 18: CODE/XXX (Mode S hex code)
- **If exempt from the mandate or CPDLC is unserviceable:**
  - Field 10a: Z
  - Field 18: DAT/CPDLCX

**Important:** Do not file both J1 and DAT/CPDLCX together, and do not leave both out. Either scenario will result in automatic rejection by the IFPS system.

**Also important:** You don't need to file either J1 nor CPDLCX if your requested level is below FL285.

**Also also important:** Eurocontrol has also advised separately that if CPDLC is unserviceable, you may continue to operate above FL285 for up to 10 days under MEL relief, provided the flight plan is filed correctly using DAT/CPDLCX. After this period, you must either fix the issue or operate below FL285.

**Also also also important:** On 4 Nov 2025, IFPS will be unavailable between 2100-0000 UTC for a system upgrade. The outage is expected to last about one hour, but up to two hours if a rollback is needed. During this time, no flight plans can be filed or validated, so submit plans in advance.

**Right — a Eurocontrol leaflet, "Recommended Practices for CPDLC in Europe - 2026 -"**

[CPDLC Logon is mandatory in most of European airspace.]

CPDLC usage helps to prevent Loss of Communication incidents and significantly improves ATC capacity. **Your participation and commitment is key!**

<u>Preparation for Log-On</u>

- FMC/CDU Flight INIT:
  - Check DEP/ARR airport, load route if available
  - Valid/correct FLT NBR (callsign)
- Ensure <u>ATN</u> logon for Europe → <u>not</u> FANS1/A
- Prepare first ATC Logon address
  - Chart provider, AIP or SID

Beside it, a photo of an MCDU with `DATALINK ATN READY` circled in red:

```text
   ATC LOGON/STATUS 1/2
 LOGON TO           LOGON
EDYY            REJECTED
 FLT ID           ACT CTR
EM0001
   TAIL NO       NEXT CTR
PP-XJE
 MAX U/L DELAY     ORIGIN
---                  KPHX
                     DEST
                     KLAX
                 DATALINK
<ATC INDEX      ATN READY
RE-LOGON TO ATC CENTER
```

<u>When to Log-On</u>

- As soon as possible, considering your company's SOPs
- According to ICAO: see picture

_Good practices_:

- Don't know the logon address? Log-On failed? _Ask ATC by voice_!
- Check CPDLC connection after passing 10.000 ft
- Report _UNABLE CPDLC_ unless the issue is due to known GNSS interference

The accompanying pictures show an aircraft **Entering** a dashed **CPDLC Airspace** box **10 Mins Prior**, and, below, an aircraft on a runway logging on **Prior to Departure¹** — footnote: ¹ May not be available at all airports.

## Slide 20

### PM-CPDLC ATN-B1 protocol stack: Key Elements

A layer table with dotted callouts on the right. The middle column carries the Layer 5 entries and the right column the Layer 6 entries (the other cell holds an em dash); from Layer 4 down the entry spans both columns.

| Layer | Element | Callout |
| --- | --- | --- |
| Layer 6 (Application) | CPDLC Message | |
| Layer 6 (Presentation) | Protected PDU | PM-CPDLC checksum |
| Layer 6 (Presentation) | ICAO Fully Encoded Data | |
| Layer 5 (Session) | ATN Context Management | Logon/Setup/Maintenance |
| Layer 5 (Session) | ACSE X.227 | Application Setup |
| Layer 5 (Session) | SPDU X.225 | Session Type Setup |
| Layer 4 (Transport) | COTP X.224 | Connection Type Setup; ATN checksum |
| Layer 3 (Network) | CLNP X.233 | IDRP |
| Layer 2 (Datalink) | X.25 Packet | ES-IS |
| Layer 2 (Datalink) | AVLC Frame | CRC 16; XID |
| Layer 1 (PHY) | VDL Mode 2 | Reed Solomon FEC; PN scrambling |
| Layer 1 (PHY) | D8PSK @ 31.5 Kbps | |

## Slide 21

#### Link Establishment

A message-sequence sketch: a control-tower illustration on the left, an aircraft on the right.

- A **Broadcast** cloud, with a dotted arrow pointing right, towards the aircraft.
- **Link Establishment Request** — solid arrow, aircraft → tower.
- **Link Establishment Response** — solid arrow, tower → aircraft.

## Slide 22

#### X.25 Handshake

Same tower/aircraft sketch.

- A **Broadcast** cloud, with a dotted arrow pointing right, towards the aircraft.
- **Link Established** — blue arrow with heads at both ends.
- **Call <u>Request</u> [ES-IS IS HELLO]** — solid arrow, aircraft → tower.
- **Call <u>Accepted</u> [ES-IS IS HELLO]** — solid arrow, tower → aircraft.

Note:  * **ES-IS** is analogous to **ARP**

## Slide 23

#### The Network Layer

Same tower/aircraft sketch.

- A **Broadcast** cloud, with a dotted arrow pointing right, towards the aircraft.
- **Link Established** — blue arrow with heads at both ends.
- **ES-IS** — blue arrow with heads at both ends.
- **IDRP Init.** — a dashed grey line with square end caps and no arrowheads.

Note:  * BGP is an instance of IDRP *  IDRP is managed by a FSM

## Slide 24

#### The Transport Layer

Same tower/aircraft sketch.

- A **Broadcast** cloud, with a dotted arrow pointing right, towards the aircraft.
- **Link Established** — blue arrow with heads at both ends.
- **ES-IS** — blue arrow with heads at both ends.
- **IDRP [ESTABLISHED]** — blue arrow with heads at both ends.
- **Transport Session** — a dashed grey line with square end caps and no arrowheads.

## Slide 25

#### Connection Overview

Same tower/aircraft sketch. A **Broadcast** cloud with a dotted arrow pointing right, then seven horizontal blue arrows, each with heads at both ends, in this order:

1. Link Established
2. ES-IS
3. IDRP [ESTABLISHED]
4. Transport Session
5. Session [ATN Context Management *]
6. Transport Session BIS
7. Session [PM CPDLC Application *]

Note: *CPDLC is a Ground Initiated Application in this case.

## Slide 26

### Full Reverse Engineering Setup

Left: a photograph of the bench — a ThinkPad running a terminal, a shielded enclosure containing the MCDU, and a grey RF case.

Right: a block diagram in three boxes.

**Real World Environment** (blue box)

- **ATC** — a radio mast, joined to an ATC facility below it by a blue arrow with heads at both ends labelled **Global CPDLC Network**.
- **Wireless Channel** — a dashed arrow with heads at both ends running between the ATC mast and the **VHF Antenna** of the lab rig.

**Lab aircraft side** (orange box)

- **VHF Antenna** feeding a splitter, then the **Unilink UL 801 CMS**.
- **FMS UNS-1EW**, joined to the Unilink by a dashed line labelled **Arinc 429**.
- A blue line runs between the antenna and the Unilink with arrowheads at both ends; blue and red lines branch off towards the attacker box, the blue one ending in an arrowhead at the Faraday cage, the red one splitting into an arrowhead at the Faraday cage and an arrowhead pointing back down at the Unilink.

**Attacker Setup** (pink box)

- **Faraday Cage (RF Isolation)** — a shielded box drawn with three amplifier symbols on bulkhead feedthroughs.
- **RTL-SDR**, fed from the cage, cabled to a laptop — labelled **dumpVDL2 Capture**.
- **USRP B210**, fed from the cage, cabled to the same laptop — labelled **RGS/DoS Frames Transmission**.

Legend: a red line is **Attacker Msg Flow**; a blue line is **Real-world Msg Flow**.

## Slide 27

#### Multi-Year Reverse Engineering Ordeal

- Huge complexity

- Very scattered documentation

- Missing documents

- Unfindable checksums

- Obscure integrity checks

- Undocumented elements

A staged photo of a desk buried in standards, a man tearing his hair out under a banner reading **REVERSE ENGINEERING DRIVES YOU CRAZY!**. Text visible in the picture:

- Two ICAO volumes: `Doc 9880 — Technical Specifications for ATN using ISO/OSI Standards and Protocols, Second edition, 2016, Part I – Air-Ground Applications` and `Doc 9880 — … Second edition, 2016, Part III – Upper Layer Communications Service (ULCS) and Internet Communications Service (ICS)`; both footed `INTERNATIONAL CIVIL AVIATION ORGANIZATION`. Written on the paper stacks and repeated on sticky notes: `DOC 9880-1 268 PAGES` and `DOC 9880-3 326 PAGES`.
- `RTCA — MASPS - Minimum Aviation System Performance Standards`, on a stack marked `RTCA DO-224D ~1000 PAGES`, sticky note `DO-224D ~1000 PAGES`.
- `ITU — Free ITU docs: ITU X.233 (CLNP) / ITU X.224 (COTP) / ITU X.25 (X.25)`, on a stack marked `ITU X. SERIES ?? PAGES (WHO KNOWS)`, sticky note `INSANE COMPLEXITY... NO END. SEND HELP.`
- Pinned note: `IF YOU UNDERSTAND EVERYTHING... YOU'RE PROBABLY USING THE WRONG STANDARD`
- The man's T-shirt: `sleep(0); reverse(); repeat(); cry(); goto insane;`
- An SDR receiver tuned to `1.420.000.000` with a spectrum trace.
- Sticky note: `☑ STANDARDS ☑ DOCUMENTS ☑ PROTOCOLS ☑ SUPPLEMENTS ☑ AMENDMENTS ☑ CORRIGENDA ...FOREVER`
- Sticky note with a smiley: `ME BEFORE THIS`; sticky note with a screaming figure: `ME AFTER THIS`
- A notebook headed `WHERE DO I EVEN START?!` holding a hand-drawn box diagram — X.25, CLNP, COTP, X.25, ASI, OSI, AMHS, CPDLC, AIDC, APDc, PENG and a box reading `...???`, with one scrawled label above CLNP that is not legible — captioned `EVERYTHING CONNECTS TO EVERYTHING (WHY?!)`.
- A mug: `I REVERSE THINGS AND I KNOW THINGS`
- A sheet headed `SUMMARY:` — `☑ WRONG STANDARDS ☑ FALSE CHECKSUMS ☑ BAD DOCUMENTATION ☑ MIND = DESTROYED`, with a skull and crossbones.

## Slide 28

### One example: PM-CPDLC checksum

A data-flow diagram. Four input boxes — **payload** (set vertically), **Flight number**, **Facility Designation** and **Aircraft ICAO** — each feed an arrow into the **Content Protected Message** box; that box feeds an arrow into the **ATN-32 Checksum** box, whose **Output** arrow curves across to the algorithm panel:

```text
Addition is performed in one's complement arithmetic

Init: C0 = C1 = C2 = C3 = 0

For each byte x:
   C0 = C0 + x
   C1 = C1 + C0
   C2 = C2 + C1
   C3 = C3 + C2

Final checksum:
   X0 = -(C0 + C1 + C2 + C3)
   X1 = C1 + 2*C2 + 3*C3
   X2 = -(C2 + 3*C3)
   X3 = C3

Return:
      (X0,X1,X2,X3)
```

## Slide 29

### Let's explore the stack

The same layer table as before.

| Layer | Element | Callout |
| --- | --- | --- |
| Layer 6 (Application) | CPDLC Message | |
| Layer 6 (Presentation) | Protected PDU | PM-CPDLC checksum |
| Layer 6 (Presentation) | ICAO Fully Encoded Data | |
| Layer 5 (Session) | ATN Context Management | Logon/Setup/Maintenance |
| Layer 5 (Session) | ACSE X.227 | Application Setup |
| Layer 5 (Session) | SPDU X.225 | Session Type Setup |
| Layer 4 (Transport) | COTP X.224 | Connection Type Setup; ATN checksum |
| Layer 3 (Network) | CLNP X.233 | IDRP |
| Layer 2 (Datalink) | X.25 Packet | ES-IS |
| Layer 2 (Datalink) | AVLC Frame | CRC 16; XID |
| Layer 1 (PHY) | VDL Mode 2 | Reed Solomon FEC; PN scrambling |
| Layer 1 (PHY) | D8PSK @ 31.5 Kbps | |

## Slide 30

### Let's explore the stack

The same layer table, with the **Layer 2 (Datalink) / AVLC Frame** row boxed in red and annotated in red to its right: **We start here**.

| Layer | Element | Callout |
| --- | --- | --- |
| Layer 6 (Application) | CPDLC Message | |
| Layer 6 (Presentation) | Protected PDU | PM-CPDLC checksum |
| Layer 6 (Presentation) | ICAO Fully Encoded Data | |
| Layer 5 (Session) | ATN Context Management | Logon/Setup/Maintenance |
| Layer 5 (Session) | ACSE X.227 | Application Setup |
| Layer 5 (Session) | SPDU X.225 | Session Type Setup |
| Layer 4 (Transport) | COTP X.224 | Connection Type Setup; ATN checksum |
| Layer 3 (Network) | CLNP X.233 | IDRP |
| Layer 2 (Datalink) | X.25 Packet | ES-IS |
| Layer 2 (Datalink) | AVLC Frame | CRC 16; XID |
| Layer 1 (PHY) | VDL Mode 2 | Reed Solomon FEC; PN scrambling |
| Layer 1 (PHY) | D8PSK @ 31.5 Kbps | |

## Slide 31

### AVLC Layer

```text
[2025-04-24 14:02:06 CEST] [136.975] [-19.5/-49.5 dBFS] [30.0 dB] [1.0 ppm]
 52 b4 fe fe 94 ac 48 19  20 ff ff 01 32 2e 2e 43  |R.....H.  ...2..C|
 50 44 4c 43 31 5f 7f 41  03 56 41 7f bc 25        |PDLC1_.A .VA..%  |
2D4918 (Ground station, On ground) -> 4B7FFF (Aircraft): Command
AVLC type: I sseq: 0 rseq: 1 poll: 0
 ACARS:
  Reassembly: skipped
  Reg: ..CPDLC
  Mode: 2 Label: _d Blk id: A More: 0 Ack: 1
```

The pane is captioned **dumpvdl2** in cyan at the bottom right.

## Slide 32

### AVLC  Frame: Closer Look

```text
[2025-04-24 14:02:06 CEST] [136.975] [-19.5/-49.5 dBFS] [30.0 dB] [1.0 ppm]
 52 b4 fe fe 94 ac 48 19  20 ff ff 01 32 2e 2e 43  |R.....H.  ...2..C|
 50 44 4c 43 31 5f 7f 41  03 56 41 7f bc 25        |PDLC1_.A .VA..%  |
2D4918 (Ground station, On ground) -> 4B7FFF (Aircraft): Command
AVLC type: I sseq: 0 rseq: 1 poll: 0
 ACARS:
  Reassembly: skipped
  Reg: ..CPDLC
  Mode: 2 Label: _d Blk id: A More: 0 Ack: 1
```

**Sender Address** — a blue arrow points at `2D4918 (Ground station, On ground)`, which is boxed in blue.

## Slide 33

### AVLC  Frame: Closer Look

```text
[2025-04-24 14:02:06 CEST] [136.975] [-19.5/-49.5 dBFS] [30.0 dB] [1.0 ppm]
 52 b4 fe fe 94 ac 48 19  20 ff ff 01 32 2e 2e 43  |R.....H.  ...2..C|
 50 44 4c 43 31 5f 7f 41  03 56 41 7f bc 25        |PDLC1_.A .VA..%  |
2D4918 (Ground station, On ground) -> 4B7FFF (Aircraft): Command
AVLC type: I sseq: 0 rseq: 1 poll: 0
 ACARS:
  Reassembly: skipped
  Reg: ..CPDLC
  Mode: 2 Label: _d Blk id: A More: 0 Ack: 1
```

- **Sender Address** — blue arrow to `2D4918 (Ground station, On ground)`, boxed in blue.
- **Receiver Address** — green arrow to `4B7FFF (Aircraft)`, boxed in green.

## Slide 34

### AVLC  Frame: Closer Look

```text
[2025-04-24 14:02:06 CEST] [136.975] [-19.5/-49.5 dBFS] [30.0 dB] [1.0 ppm]
 52 b4 fe fe 94 ac 48 19  20 ff ff 01 32 2e 2e 43  |R.....H.  ...2..C|
 50 44 4c 43 31 5f 7f 41  03 56 41 7f bc 25        |PDLC1_.A .VA..%  |
2D4918 (Ground station, On ground) -> 4B7FFF (Aircraft): Command
AVLC type: I sseq: 0 rseq: 1 poll: 0
 ACARS:
  Reassembly: skipped
  Reg: ..CPDLC
  Mode: 2 Label: _d Blk id: A More: 0 Ack: 1
```

- **Sender Address** — blue arrow to `2D4918 (Ground station, On ground)`, boxed in blue.
- **Receiver Address** — green arrow to `4B7FFF (Aircraft)`, boxed in green.
- **Type && Sequence numbers** — yellow arrow to the boxed line `AVLC type: I sseq: 0 rseq: 1 poll: 0`; the control byte `20` in the hex dump is boxed in yellow as well.

## Slide 35

#### The backbone: Information frame

```text
[2025-04-24 14:02:06 CEST] [136.975] [-19.5/-49.5 dBFS] [30.0 dB] [1.0 ppm]
 52 b4 fe fe 94 ac 48 19  20 ff ff 01 32 2e 2e 43  |R.....H.  ...2..C|
 50 44 4c 43 31 5f 7f 41  03 56 41 7f bc 25        |PDLC1_.A .VA..%  |
2D4918 (Ground station, On ground) -> 4B7FFF (Aircraft): Command
AVLC type: I sseq: 0 rseq: 1 poll: 0
 ACARS:
  Reassembly: skipped
  Reg: ..CPDLC
  Mode: 2 Label: _d Blk id: A More: 0 Ack: 1
```

- **Sender Address** — blue arrow to `2D4918 (Ground station, On ground)`, boxed in blue.
- **Receiver Address** — green arrow to `4B7FFF (Aircraft)`, boxed in green.
- **Type && Sequence numbers** — yellow arrow to `AVLC type: I sseq: 0 rseq: 1 poll: 0`; the control byte `20` is boxed in yellow.
- **Payload** — purple arrow to the boxed `ACARS:` block (`Reassembly: skipped`, `Reg: ..CPDLC`, `Mode: 2 Label: _d Blk id: A More: 0 Ack: 1`).

## Slide 36

#### Error handling frame : AVLC FRMR

```text
[2024-08-30 20:17:17 CEST] [136.975] [-22.3/-46.3 dBFS] [23.9 dB] [3.3 ppm]
 52 b4 fe fe 94 ac 48 e9  97 c8 8a 08 08 81        |R.....H. ......   |
2D4917 (Ground station, On ground) -> 4B7FFF (Aircraft): Command
AVLC type: U (FRMR) P/F: 1
 Data (3 bytes):
  c8 8a 08
```

- **Sender Address** — blue arrow to `2D4917 (Ground station, On ground)`, boxed in blue.
- **Receiver Address** — green arrow to `4B7FFF (Aircraft): Command`, boxed in green.
- **Type && Params** — yellow arrow to `AVLC type: U (FRMR) P/F: 1`, boxed in yellow.

## Slide 37

#### AVLC FRMR: Closer Look

```text
[2024-08-30 20:17:17 CEST] [136.975] [-22.3/-46.3 dBFS] [23.9 dB] [3.3 ppm]
 52 b4 fe fe 94 ac 48 e9  97 c8 8a 08 08 81        |R.....H. ......   |
2D4917 (Ground station, On ground) -> 4B7FFF (Aircraft): Command
AVLC type: U (FRMR) P/F: 1
 Data (3 bytes):
  c8 8a 08
```

- **Sender Address** — blue arrow to `2D4917 (Ground station, On ground)`, boxed in blue.
- **Receiver Address** — green arrow to `4B7FFF (Aircraft): Command`, boxed in green.
- **Type && Params** — yellow arrow to `AVLC type: U (FRMR) P/F: 1`, boxed in yellow.
- **Faulty Frame LCF** — purple arrow to the first data byte `c8`, boxed in purple.

Any frame can be flagged and the aircraft trusts it immediately, what could go wrong?...

## Slide 38

### 1st DoS vector: **Malicious AVLC FRMR Injection**

Left, a photo of the Universal MCDU after the attack:

```text
        COMM STATUS      MSG
VHF 136.975MHZ
AOA:NOCOMM/NO SERVICE
ATN:NOCOMM/NO CIRCUIT


                COMM CNTRL->
ADVISORY               1427Z
<-ATC DISCNECT       RETURN->
```

(Keypad legends visible below the screen: NAV, VNAV, DTO, LIST, PREV / FPL, PERF, TUNE, MENU, NEXT / B C D E F G / I J K L M N, and a numeric pad 1-9, BACK, 0, MSG.)

Right, a sequence diagram over three lifelines — **ATC**, **Aircraft**, **Attacker** — top to bottom:

1. **Normal Protocol Execution** — arrowheads at both ends, ATC ↔ Aircraft.
2. **Target Frame** (blue) — Aircraft → ATC.
3. A framed block tabbed **Attack**, spanning Aircraft to Attacker: **AVLC FRMR [Target Frame]** (red) — Attacker → Aircraft.
4. **Updates internal state** — a self-message looping back into the Aircraft lifeline.
5. **AVLC UA** — Aircraft → ATC.
6. **AVLC FRMR** — ATC → Aircraft.
7. **Link Reset** — dashed, arrowheads at both ends, ATC ↔ Aircraft.

## Slide 39

### But it doesn't get easier than this… right?

A two-panel meme. Left: a man in sunglasses captioned **ABSOLUTE FOSHU**. Right: a "gigachad" figure whose sunglasses are labelled **RTCA** and **FAA**, holding a mug labelled **ICAO**.

## Slide 40

#### Deeper dive into link management

The LME state machine, five states drawn as circles:

- **Link Unavailable (S0)**
- **Link Establishment Pending (S1)**
- **Link Connected (S2)**
- **Link Handoff Pending (S3)**
- **Double-Links Connected (S4)**

Transitions:

| From | To | Label |
| --- | --- | --- |
| (entry) | S0 | VME Creates New LME |
| S0 | S1 | Receipt of Link Establishment Event : A1 |
| S1 | S1 | T3 Expiration : A1 |
| S1 | S0 | Receipt of XID_RSP_LCF : A3 |
| S1 | S0 | N2 Exceeded : A9 |
| S1 | S2 | Receipt of XID_RSP_LE : A2 |
| S2 | S0 | Receipt of Disc. Notification from DLE : A3 |
| S2 | S3 | Receipt of VME Handoff Command : A4 |
| S3 | S2 | Link Handoff Refusal : A10 |
| S3 | S4 | Receipt of XID_RSP_HO (F=1) : A6 |
| S2 | S4 | Receipt of XID_CMD_HO (P=1) : A5,A6 |
| S4 | S2 | TGS Timeout : A8 |

It might look intimidating but we don't need to understand all of it!

## Slide 41

### What we actually care about

A cut-down version of the LME state machine, three states:

- **Link Unavailable (S0)** (label in dark red)
- **Link Establishment Pending (S1)**
- **Link Connected (S2)** (label in green)

| From | To | Label |
| --- | --- | --- |
| S0 | S1 | Receipt of Link Establishment Event : A1 |
| S1 | S1 | T3 Expiration : A1 |
| S1 | S0 | Receipt of XID_RSP_LCF : A3 |
| S1 | S0 | N2 Exceeded : A9 |
| S1 | S2 | Receipt of XID_RSP_LE : A2 |
| S2 | S0 | Receipt of Disc. Notification from DLE : A3 (drawn in red) |

## Slide 42

#### Keep it simple and stupid

A cut-down version of the LME state machine, three states:

- **Link Unavailable (S0)** (label in dark red)
- **Link Establishment Pending (S1)**
- **Link Connected (S2)** (label in green)

| From | To | Label |
| --- | --- | --- |
| S0 | S1 | Receipt of Link Establishment Event : A1 |
| S1 | S1 | T3 Expiration : A1 |
| S1 | S0 | Receipt of XID_RSP_LCF : A3 |
| S1 | S0 | N2 Exceeded : A9 |
| S1 | S2 | Receipt of XID_RSP_LE : A2 |
| S2 | S0 | Receipt of Disc. Notification from DLE : A3 (drawn in red) |

Below it, the frame layout:

| DST addr | SRC addr | LCF=0x43 | FCS |
| --- | --- | --- | --- |
| (4 B) | (4 B) | (1 B) | (2 B) |

**Stateless** frame!

## Slide 43

A four-panel Anakin/Padmé Star Wars meme, captioned in yellow:

1. DoS on CPDLC is trivial
2. But an attacker can only target one aircraft at a time … right?
3. Broadcast Address
4. (no caption)

## Slide 44

### Bonus Points: Broadcast DoS

```text
[2025-08-25 20:28:22.381 CEST] [136.975] [-9.9/-49.4 dBFS] [39.5 dB] [2.8 ppm]
 f2 fe fe fe 94 ac 48 19  43 4d 4f                 |......H. CMO     |
2D4918 (Ground station, On ground) -> FFFFFF (Aircraft): Command
AVLC type: U (DISC) P/F: 0
```

`FFFFFF (Aircraft): Command` is boxed in orange, and an orange arrow runs from it down to the frame layout:

| DST addr | SRC addr | LCF=0x43 | FCS |
| --- | --- | --- | --- |
| (4 B) | (4 B) | (1 B) | (2 B) |

captioned in red **AVLC U DISC (Stateless)**. A dark red arrow runs from that frame box leftwards to a thumbnail of the full five-state LME state machine (S0 Link Unavailable, S1 Link Establishment Pending, S2 Link Connected, S3 Link Handoff Pending, S4 Double-Links Connected). In this rendering the labels read `Receipt of XID_RSP_LCR:A3` and `TG5 Timeout:A8`, and the action codes are set in bold: T3 Expiration:**A1**, Receipt of XID_RSP_LE:**A2**, Link Handoff Refusal:**A10**, Receipt of VME Handoff Command:**A4**, N2 Exceeded:**A9**, Receipt of Link Establishment Event:**A1**, Receipt of Disc. Notification from DLE:**A3**, Receipt of XID_CMD_HO (P=1):**A5,A6**, Receipt of XID_RSP_HO (F=1):**A6**, VME Creates New LME.

- We leverage **Data Link State Machines** as an Attack Vector
- Escalation from a single targeted DoS to **disruption of all aircraft in range** using Broadcast address

## Slide 45

### DoS outcome

Three photos of the Universal MCDU.

```text
        COMM STATUS      MSG
VHF 136.975MHZ
AOA:NOCOMM/NO SERVICE
ATN:NOCOMM/NO CIRCUIT


                COMM CNTRL->
ADVISORY               1427Z
<-ATC DISCNECT       RETURN->
```

```text
             LOG ON
  CURR ATC:        NEXT ATC:
    ....               ....
CALLSIGN
EEC9999                 ORIG
ATSU:ATN                LSZH
<-LFPYTEST              DEST
NO SERVICE              LSZH
<-LOG ON                 ETD
                       ----Z
                       1833Z
<-UNILINK MENU       RETURN->
```

```text
             LOG ON      MSG
+-------------------------+
|RECOMMEND CONTACTING     |
|ATC VIA VOICE            |
|                     OK->|
+-------------------------+
ATSU:ATN                DEST
<-LFPYTEST              LSZH
LOG ON TIMEOUT           ETD
<-LOG ON               ----Z
                       1831Z
<-UNILINK MENU       RETURN->
```

In the third photo the pop-up covers the CALLSIGN field; only the `C` and `E` of `CALLSIGN`/`EEC9999` show at the left edge.

## Slide 46

### So much more remains to discuss

The same layer table, with a red box drawn around the top nine rows — Layer 6 (Application) down to Layer 2 (Datalink) / X.25 Packet.

| Layer | Element | Callout |
| --- | --- | --- |
| Layer 6 (Application) | CPDLC Message | |
| Layer 6 (Presentation) | Protected PDU | PM-CPDLC checksum |
| Layer 6 (Presentation) | ICAO Fully Encoded Data | |
| Layer 5 (Session) | ATN Context Management | Logon/Setup/Maintenance |
| Layer 5 (Session) | ACSE X.227 | Application Setup |
| Layer 5 (Session) | SPDU X.225 | Session Type Setup |
| Layer 4 (Transport) | COTP X.224 | Connection Type Setup; ATN checksum |
| Layer 3 (Network) | CLNP X.233 | IDRP |
| Layer 2 (Datalink) | X.25 Packet | ES-IS |
| Layer 2 (Datalink) | AVLC Frame | CRC 16; XID |
| Layer 1 (PHY) | VDL Mode 2 | Reed Solomon FEC; PN scrambling |
| Layer 1 (PHY) | D8PSK @ 31.5 Kbps | |

## Slide 47

#### Attack surface is VERY large

Our work focuses on DoS attacks at the protocol level, excluding jamming

**We found four attack types:**

- ➢ AVLC FRMR injection

- ➢ Broadcast AVLC U DISC

- ➢ Control flow injection

- ➢ Malformed payload injection

Right, a generalised sequence diagram over the lifelines **ATC**, **Aircraft**, **Attacker**:

1. **Normal Protocol Execution** — arrowheads at both ends, ATC ↔ Aircraft.
2. A framed block tabbed **Attack**, spanning Aircraft to Attacker: **Malicious frame** (red) — Attacker → Aircraft.
3. **Updates internal state** — a self-message looping back into the Aircraft lifeline.
4. A framed block tabbed **X Virtual Circuit Mismatch**, spanning ATC to Aircraft, holding a note: "Aircraft and ATC are no longer synchronized due to the malicious frame."
5. **Link Failure state** — dashed, arrowheads at both ends, ATC ↔ Aircraft.

## Slide 48

### Attacking the DMs: An IMSI Catcher for Aircraft

| CHALLENGE | IMPLEMENTATION |
| --- | --- |
| Mimic a legitimate ground–aircraft connection | Emulates connection as a finite-state machine |
| Multiple layers, each with rules and timing (icon labelled L3 / L2 / L1) | Progresses step by step through all layers |
| Numerous parameters and timeouts | Negotiates values and maintains session state |
| Obscure Integrity checks at several points | Reverse engineer and generates required checks |
| Stable long-lived connection | Maintain session state over time, handling all necessary steps and checks to keep the link active (icon marked 24h) |

Right: a photo of the bench — the MCDU in an open rack showing a green CPDLC page, a ThinkPad running a terminal, and the grey shielded RF enclosure with its fan, cabled together.

## Slide 49

#### Rogue Ground Station

A schematic over a ground line. On the left, a radio mast with a red devil-face icon: **Attacker** / **(Rogue Ground Station)** (in red). On the right, an airport with tower, dishes and antennas: **ATSU** / **(Ground Station)**. An aircraft flies above the ATSU, joined to it by a vertical arrow with heads at both ends labelled **CPDLC connection**.

## Slide 50

#### Rogue Ground Station

The same schematic — **Attacker (Rogue Ground Station)** on the left, **ATSU (Ground Station)** on the right, the aircraft above it joined by the double-headed **CPDLC connection** arrow — with one addition: a dark red arrow labelled **Rogue Disconnect** running from the attacker's mast up to the aircraft (single arrowhead, at the aircraft).

## Slide 51

#### Rogue Ground Station

The same schematic — a radio mast with a red devil-face icon labelled **Attacker** / **(Rogue Ground Station)** (in red) on the left, an airport labelled **ATSU** / **(Ground Station)** on the right, and an aircraft above the right-hand side of the scene.

- **Rogue Disconnect** — dark red arrow from the attacker's mast up to the aircraft (arrowhead at the aircraft).
- **CPDLC connection** — the double-headed arrow between the aircraft and the ATSU is still drawn, but a large red **X** is placed over it and the label `CPDLC connection` is struck through in red.

## Slide 52

#### Rogue Ground Station

The same schematic — a radio mast with a red devil-face icon labelled **Attacker** / **(Rogue Ground Station)** (in red) on the left, an airport labelled **ATSU** / **(Ground Station)** on the right, and an aircraft above the right-hand side of the scene.

A single curved dark red arrow rises from the attacker's mast, arrowhead at the top, labelled **Broadcast RGS Information Frame**. No link is drawn to the ATSU.

## Slide 53

#### Rogue Ground Station

The same schematic — a radio mast with a red devil-face icon labelled **Attacker** / **(Rogue Ground Station)** (in red) on the left, an airport labelled **ATSU** / **(Ground Station)** on the right, and an aircraft above the right-hand side of the scene.

- **Broadcast RGS Information Frame** — a curved red dotted arrow from the attacker's mast up to the aircraft (arrowhead at the aircraft).
- **Initiate Link Establishment** — a straight black arrow from the aircraft down to the attacker's mast (arrowhead at the mast).

## Slide 54

#### Rogue Ground Station

The same schematic — a radio mast with a red devil-face icon labelled **Attacker** / **(Rogue Ground Station)** (in red) on the left, an airport labelled **ATSU** / **(Ground Station)** on the right, and an aircraft above the right-hand side of the scene.

A dark red arrow with heads at both ends runs between the attacker's mast and the aircraft, labelled **CPDLC connection**.

## Slide 55

#### Rogue Ground Station

The same schematic — a radio mast with a red devil-face icon labelled **Attacker** / **(Rogue Ground Station)** (in red) on the left, an airport labelled **ATSU** / **(Ground Station)** on the right, and an aircraft above the right-hand side of the scene.

- **Rogue CPDLC Session** — a black dashed arrow with heads at both ends, between the attacker's mast and the aircraft.
- **Attacker CPDLC Messages** (in red) — a solid dark red arrow from the attacker's mast up to the aircraft (arrowhead at the aircraft).

## Slide 56

### Demo Time!    Demo Time!

Between the two titles, a video still of the Universal MCDU:

```text
             LOG ON      MSG
  CURR ATC:        NEXT ATC:
    ....
CALLSIGN               ....
EEC9999                 ORIG
ATSU:ATN                LSZH
<-LFPYTEST              DEST
NO SERVICE              LSZH
<-LOG ON                 ETD
     ADVISORY          ----Z
<-VHF NOCOMM           1406Z
                     RETURN->
```

(The still is a low-resolution video frame; the full keypad — DATA/FUEL, NAV, VNAV, DTO, LIST, PREV, FPL, PERF, TUNE, MENU, NEXT, A-Z, the numeric pad, BACK, ON/OFF DIM, ± and ENTER — is visible below the screen.)

## Slide 57

### Impact of Rogue Ground Station

**System-level risk:**

A **rogue ground station** can establish a legitimate ATN/CPDLC session and obtain the same operational privileges as an authentic ATC. Because messages are protocol-compliant and appear authenticated, flight crews may treat malicious clearances as genuine.

**Key takeaway:**

The threat is **abusing the existing trust** in CPDLC communication. A rogue ground station can blend malicious instructions with legitimate traffic, making detection difficult until operational consequences emerge.

The following scenarios were **reviewed with commercial pilots and controllers** and identified as realistic, high-impact examples:

**Trajectory Manipulation**

**False lateral clearance** (UM79 PROCEED DIRECT)
→ Diverts aircraft into conflicting traffic flows, holding stacks, or restricted airspace.

**Separation Loss**

**False altitude clearance** (UM21 CLIMB TO / UM20 DESCEND TO)
→ Places aircraft at an occupied flight level, potentially triggering TCAS resolution advisories.

**Terminal Area Disruption**

**Modified approach clearance** (UM80 CLEARED VIA)
→ Forces unexpected procedure changes during high-workload phases of flight.

**Trust Exploitation**

**Fabricated emergency or operational messages** (UM169)
→ Creates confusion, unnecessary diversions, and erosion of confidence in CPDLC.

## Slide 58

### Thousands of Affected Aircraft in Europe Alone

Three stat cards.

**Adoption Rate**

**83%** — **Filed CPDLC Capability (J1)**. Of European flight movements in early 2024.

**Actual Usage**

**42%** — **Active CPDLC Usage**. Equipped does not mean logged on or actively used.

**Daily Flight Traffic**

**~29,300 flights/day**. Out of 10.7 million total flights in Europe in 2024.

**Daily CPDLC Volume**

**24,000** Equipped flight legs / day

**12,000** Actually active legs / day

**Aircraft Population**

**22,948** — **Individual Civil Aircraft**. Operating at least once in the EUROCONTROL Network Manager area in 2022.

Sources: EUROCONTROL Datalink Operations (2024-02) | European Aviation Overview (2025-01)

## Slide 59

### Is the US CPDLC safe/secure? No, just easier…

A screenshot of a paper:

**On the Implications of Spoofing and Jamming Aviation Datalink Applications**

Harshad Sathaye — Khoury College of Computer Sciences, Northeastern University, Boston, USA
Guevara Noubir — Khoury College of Computer Sciences, Northeastern University, Boston, USA
Aanjhan Ranganathan — Khoury College of Computer Sciences, Northeastern University, Boston, USA

and a passage from its body, most of it highlighted in blue:

> to note that ATN B1 does not support ADS-C application [26]. This work focuses on FANS 1/A applications and targets specific CPDLC, and ADS-C messages exchanged using the ACARS network. ATN B1 and FANS 1/A support different message sets. However, these attacks can be used against ATN B1 applications with some changes.

## Slide 60

### How did we end up here…?

Three illustrated cards.

**Aviation Design Philosophy** — a blueprint-style flight-deck schematic captioned in the image `A350 FLIGHT DECK SCHEMATIC - SAFE CERTIFIED TECHNOLOGY / 1:100 SCALE`.

Rigid safety-first principles prioritize extreme reliability and long-proven hardware, choosing stability over the rapid adoption of modern commercial technology.

**Long Upgrade Cycles** — an AI-rendered image of interlocking gears along a winding road.

Extremely complex certification processes and high integration costs mean deployment cycles often span decades, keeping active aircraft tied to legacy systems.

**The Savior that never comes: Datalink over IP** — an AI-rendered image of an airliner over a networked globe with satellite and node labels.

While IP-based networks promise a modern security standard, rollouts face constant technical and logistical delays, remaining a distant future solution.

## Slide 61

#### What Can Be Done About This?

Realistically right now? Probably nothing.

Maybe make pilots aware?

Safety engineering DOES help for now.
(We still plan to fly back after DEF CON…)

Right, a four-panel "waiting Pablo" meme — a man sitting alone on a swing, a skeleton left sitting on a bench, the same man waiting at a kitchen table, and him standing by an empty swimming pool — captioned:

**Aviation community waiting for security patches**

## Slide 62

#### What Can Be Done About This (longer term)?

**Improving Standards**

- **SDS to DTLS:** Adopting DTLS for authentication and replay protection.

- **Timeline:** Trials expected in the 2030s; rollout faces cost and delay challenges.

**Academic Research**

- **Limited Proposals:** Current landscape includes HIP, ECC, and AKAASH.

- **Focus:** Advancing formal verification efforts.

**Physical Layer Intrusion Detection**

- **Strategies:** Spectrum monitoring, RF fingerprinting.

Right: a black slide headed **Elliptic Curve Cryptography (ECC)** showing an orange cubic curve on x/y axes with points A, B and C and a chord through them, plus the annotation `P = [k]G` with arrows labelled **Public key** (under `P`) and **Private key** (under `k`). Below it, a blocky pixel-art portrait on a green background.

## Slide 63

#### Disclosure

Disclosed to everyone we could find:

- Aviation ISAC

- European Aviation Safety Agency (EASA)

- EUROCONTROL

- US CISA/FAA

- Airbus

- Boeing

- Pilatus

- Swiss Aviation Authorities & ANSP

- British Airline Pilots' Association

- Lufthansa Group

- Universal

- Collins

Right: an AI-generated photo of a woman in a phone-bank room, handset to her ear and a terminal-green phone in her hand, surrounded by monitors of green text. Legible props: posters reading `GET OUT & THE VOTE`, `COMMUNITY DRIVE INFO`, `CALLING TREE` and `RECRUIT THE VOTE`; handwritten sheets headed `war dialing lists`; and a desk phone labelled `phreak` / `hack`.

## Slide 64

#### Disclosure Stories (1/3)

> [...] I'm really impressed with your findings (they were to expect as **the industry talks about these issues for ages now and nothing really happens**). [...]

— European Airline

> [...] Having been **harping on about CPDLC vulnerability for years**, I'm so pleased that we now have proof that it can indeed be 'spoofed'. In the past I **have even had a categoric 'not possible' from a senior comms engineer, citing that handshake protocols would prevent any successful rogue connection!** [...]

— European Pilots Association

## Slide 65

#### Disclosure Stories (2/3)

> [...] On Monday, the **Product Security community of interest (COI), which has subject matter experts across manufacturers, ANSPs, airlines, and airports, met and had a healthy discussion on the content** [...] The COI is including this topic in their next monthly meeting agenda, and I will again ask the group for any questions and feedback to provide to you. [...]

— Aviation ISAC

## Slide 66

#### Disclosure Stories (3/3): FAA

Disclosed via CISA/VINCE on 2025-08-27

Confirmed contact to FAA on 2025-09-17

Across the middle of the slide, a screenshot of the disclosure thread with white boxes pasted over the names. Left, the responder's card: two blank white rectangles, and under them a bold line clipped by the lower box edge reading `CISA Industrial`, then **Federal Aviation Administration_FAA** and, in grey, `General Engineer`. Right, the reply, dated `2026-06-24 (3 weeks, 1 day ago)`: a large `Hi` followed by a white box over the name, a sliver of the screenshot showing along its lower edge as `for your up` before the box cuts it off, and then:

> We do have some folks reviewing the details now, thanks. Will let you know as soon as we have some feedback to share.

Upon acceptance of DEF CON talk they finally started reading the paper.

## Slide 67

#### Key Takeaways

Three cards, each numbered in large red digits.

**01**

**CPDLC is critically insecure - like all other aviation protocols**

We have demonstrated that we can fully pwn the CPDLC system, exposing fundamental gaps in global aviation communications.

**02**

**Complexity != Security**

More ancient protocol complexity does not equal security.

**03**

**15 Years of Inaction**

Nobody seems to be doing anything about this critical issue despite 15 years of DEF CON talks.

## Slide 68

#### To appear in Usenix Sec’26 next week!

You can find it here: <u>https://www.usenix.org/conference/usenixsecurity26/presentation/ziazi</u>

We do not release the code thought ;)

Bottom left, the conference logo: **35TH USENIX Security Symposium**, `AUGUST 12–14, 2026`, `BALTIMORE, MD, USA`.

Right, a screenshot of the paper's first page, badged `ARTIFACT EVALUATED` / `USENIX` / `AVAILABLE`:

**Sliding into the Flight Deck’s DMs: Practical Message Attacks on CPDLC**

Mehdi Ziazi — Department of Computer Science, ETH Zurich, Switzerland
Khalid Aleem — Independent, London, United Kingdom
Harshad Sathaye — Department of Computer Science, ETH Zurich, Switzerland
Martin Strohmeier — Cyber-Defence Campus, armasuisse S + T, Switzerland

**Abstract**

> The Controller–Pilot Data Link Communications (CPDLC) system has become integral to modern air traffic management, particularly in high-density or oceanic airspace where voice communication is limited or unavailable. Designed to increase operational efficiency, CPDLC is an alternative to traditional VHF voice communication with standardized digital messages for altitude changes, heading adjustments, free-text messages, and frequency handovers. However, CPDLC does not implement encryption and relies primarily on protocol complexity and obscurity as a barrier to misuse.
>
> In this work, we present a full-stack security analysis of CPDLC and showcase several vulnerabilities that allow hijacking ATC-Pilot link with rogue ground station attacks and large-scale denial of service attacks that are capable of disabling CPDLC services for all aircraft in radio range. As a proof-of-concept, we also introduce `cpdlc-gs`, a *first* SDR based full-stack CPDLC ground-station implementation capable of injecting uplink messages to issue fake CPDLC flight instructions and effective denial of service attacks. Furthermore, to evaluate `cpdlc-gs`, together with air navigation service providers and avionics manufacturers, we develop a novel, fully-functional test environment with real, certifiable hardware from Universal Avionics. Through such a setup we conceptualize and validate several attacks and demonstrate that even isolated rogue stations can pose a substantial threat, especially when pilots are under high workload or in degraded communication scenarios. Overall, we argue that the heavy reliance and global adoption of CPDLC make it a high value target, and that the lagging aviation datalink security standardization process needs to be urgently addressed.

**1 Introduction**

> Modern air traffic control (ATC) increasingly relies on digital communications to manage growing volumes of aircraft with greater efficiency and safety. Among these systems, *Controller-Pilot Data Link Communications* (CPDLC) has become a critical component as it improves over traditional analog voice instructions with structured digital messages exchanged between aircraft and ground stations. CPDLC has gained widespread adoption due to its operational efficiency, reduced voice channel congestion, decreased human error, and environmental benefits such as lower CO₂ emissions [44].
>
> CPDLC was standardized primarily with functionality in mind, and its development did not incorporate a robust threat model involving malicious actors. As a result, the protocol lacks essential security features, including encryption, authentication, and cryptographic message integrity. The security literature has already postulated several classes of radio-based attacks against CPDLC, particularly spoofing and injection [8, 38, 42]. However, most of this prior work focuses solely on the application layer of the CPDLC stack and all fail to demonstrate that they work in practice.
>
> We argue that analyzing the application layer in isolation is insufficient to understand or execute real-world RF attacks. In practice, successful exploitation requires detailed knowledge of the full communication stack, from physical and data link layers to session and application logic. This necessitates dealing with a complex black-box network stack, reverse engineering undocumented checksums and proprietary implementations, and obtaining access to compliant avionics systems and operational procedures.
>
> We develop a low-cost, software-defined radio (SDR) suite `cpdlc-gs` capable of implementing arbitrary attacks on the full protocol stack. Illustrated in Figure 1, we demonstrate how to conduct broadcast denial of service attacks and create rogue ground stations capable of issuing malicious commands to the pilot, which are safety-critical but cannot be detected or prevented by the system.
>
> To further bridge theory and practice, we build a real-world test environment with certified avionics hardware and access to ground stations used by regulators for testing aircraft compliance. This unique aviation security testbed, developed in collaboration with avionics manufacturers, enables safe and reproducible experimentation under controlled conditions.
>
> The implications of such attacks are severe. For denial

(The screenshot is cut off there, mid-sentence, at its lower edge.)

## Slide 69

#### Thank you for your attention!

Left, a photo of the Universal MCDU, bezel marked `UNIVERSAL`:

```text
        ATC MSG 1/1   MSG
1418Z LFPY>^NEW
THANK YOU FOR YOUR
INTEREST.
(SENT 1418Z)

     ADVISORY          1419Z
<-LFPYTEST CNECT   RETURN->
```

(The full keypad is visible below the screen: DATA, NAV, VNAV, DTO, LIST, PREV / FUEL, FPL, PERF, TUNE, MENU, NEXT / A-Z / the numeric pad 1-9, BACK, 0, MSG, ON/OFF DIM, ± and ENTER.)

