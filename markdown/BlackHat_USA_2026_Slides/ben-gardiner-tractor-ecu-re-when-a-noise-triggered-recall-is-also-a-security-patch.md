---
title: "Tractor ECU RE When a Noise Triggered Recall is Also a Security Patch"
speakers: ["Ben Gardiner"]
conference: "Black Hat"
conference_full: "Black Hat USA 2026"
edition: "USA"
year: 2026
source_pdf: "BlackHat_USA_2026_Slides/Ben Gardiner_Tractor ECU RE When a Noise Triggered Recall is Also a Security Patch.pdf"
pages: 43
sha256: "bca0b49e63ffbc5fbac80363d0919da12a4e5d89351d0354b00308f2a192acd6"
text_chars: 11855
ocr_pages: 6
has_ocr: true
redacted_secrets: 0
ocr_confidence: 87.9
ocr_unreliable_blocks: 0
vision_verified_pages_changed: 43
vision_verified_pages: 43
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:29:22Z"
---
# Tractor ECU RE When a Noise Triggered Recall is Also a Security Patch

**Speakers:** Ben Gardiner  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/Ben Gardiner_Tractor ECU RE When a Noise Triggered Recall is Also a Security Patch.pdf` (43 pages)


## Slide 1

Tractor ECU RE: When a "Noise-Triggered” Recall is Also a Security Patch

Safety-Impacting vulns patched in the recall of ~450,000 Trucks via SAE J2497 (PLC4TRUCKS)

**Ben Gardiner** NMFTA Inc.

## Slide 2

#### Almost a Decade Watching Truck Cybersecurity

**The National Motor Freight Traffic Assoc.** has been analysing truck cybersecurity and sharing its findings since ~2017.

## Slide 3

Body / Chassis · Cameras (Int & Ext) · SRS · Climate Control · Radio · OEM Telematics

'CABIN' J1939

J560 · J560 Conn. · ABS · Gateway · Instrument Cluster · 'PT' J1939

J2497 aka PLC4TRUCKS

Fleet Telematics · RP1226 Connector · OBD Connector · Engine / Aftertreat. · Engine Telematics

J1939

J1708 / J1587

ABS · Brake Telematics · Stability / Suspension · Adaptive CC · ADAS Lane Keep · Trans-mission · Tire Pres Mon Sys

Canvassing · Temperature Monitoring · Telematics via Modem

Trailer ABS · Lift Axle · Tire Monitoring

Wireless Proprietary

J2497 aka PLC4TRUCKS

Wireless (Prop) · J2497

## Slide 4

## SECTION: MOTIVATIONS

Why NMFTA chased a brake-controller recall.

## Slide 5

## Our J2497 Track Record

- Studying **J2497** (PLC4TRUCKS) protocol since 2019

- Three CVEs across J2497 and trailer equipment

- Three CISA ICS Advisories also (one for each)

- (several) Public domain technical mitigations against wireless attacks released

*PLC: Power-Line Carrier

Yet we were told, repeatedly, that tractors are <u>unaffected.</u>

## Slide 6

## A Tip About a Recall

- An engineer friend flagged a safety recall.

- It blamed a brake-controller crash on noise in-band with the **J2497** protocol.

- Could that crash be triggered **intentionally**?

*Recall of: the Bendix EC80 Anti-lock Braking System (ABS) / Electronic Stability Program (ESP) controller.

## Slide 7

## Current Threat Model

Fleets assume tractor safety systems are isolated from the trailer's unauthenticated PLC4TRUCKS (J2497)

The operators of the equipment believe they can ignore the J2497 attack path found in every class 8 towing application trucks since 2001.

## Slide 8

## Safety & Security (yet again)

**<u>IT</u>**

Stays **<u>secure</u>** if updated frequently

**<u>Cyber-Physical Systems</u>**

Stays **<u>safe</u>** if left untouched

## Slide 9

## SECTION HEAVY VEHICLES: J1939 & PLC4TRUCKS

Meet the vehicle architecture, the buses.

## Slide 10

## Trailers and Tractors

<u>12 Volts DC</u> **& J2497 Bus**

Ground

Trailer Fault LAMP

Trailer Telematics

Trailer Brake ECU

Trailer Brake ECU

Trailer Brake ECU

Tractor Brake ECU

e.g. a Bendix EC80 Brake Controller

J1939 Busses

## Slide 11

#### Truck Attack Surface: Diagnostics-time vs Mission-time Communications

| DIAGNOSTICS | MISSION-TIME |
|---|---|
| **This communication is rejected while in motion** | **Works (as intended) in motion** |
| Authentication & Authorization: Seed-Key exchange | OLD: network access only, NEW: message authentication codes on the bus |
| Cyber-physical impacts. Commands, reconfigurations and also firmware dump, update | Cyber-physical impacts. Many are a de-rate. |
| Connections: e.g. UDS, KWP2000, XCP | Signals encoded in: SPNs (J1939), **PIDs (J1587)** |

**Same data busses: J1939 and J2947/J1708/J1587**

## Slide 12

#### Two Buses: J2497 & J1939

<u>J2497</u> (powerline PHY for J1587)

- 9600 bps

- One segment

- Mission-time LAMP and 'ABS event active' messages standardized

- Diagnostics: none

<u>J1939</u> (aka CAN bus)

- 250 kbps / 500 kbps

- **Multiple segments**

- Mission-time standardized J1939 signals (and proprietary messages)

- Diagnostics both J1939-specific and UDS

## Slide 13

## Wirelessly Accessible

- Tractor brakes are wirelessly accessible via CVE-2022-26131.

- Range is equipment-dependent. Most susceptible is tankers.

- E.g. wireless write to tanker J2497 segment from ~15 ft (~3m) range, for ~300 USD of gear

## Slide 14

## Bridging the Trust Boundary

Body / Chassis · Cameras (Int & Ext) · SRS · Climate Control · Radio · OEM Telematics

'CABIN' J1939

J560 · J560 Conn. · ABS · Gateway · Instrument Cluster · 'PT' J1939

J2497 aka PLC4TRUCKS

Fleet Telematics · RP1226 Connector · OBD Connector · Engine / Aftertreat. · Engine Telematics

J1939

J1708 / J1587

ABS · Brake Telematics · Stability / Suspension · Adaptive CC · ADAS Lane Keep · Trans-mission · Tire Pres Mon Sys

## Slide 15

## Building on Prior Work

| This work | Other’s Prior work | Our Prior Work | This Works’ Firsts |
|---|---|---|---|
|  | Hass et. al. 2016 (Wired): commanding tractor systems via J1708 | NMFTA + AIS 2020, NMFTA 2022-2024 extends to Wireless J2497 | First evidence of safety impact on tractors via (wireless) J2497. |
| This work: Mission Time instead of Diagnostic Time | Chatterjee 2024 exploiting J1939 diagnostics on tractors |  | First reverse-engineering of a safety recall’s firmware update. |
| This work: More in Silent Patches | 2019 DEVCORE, PAN-OS GlobalProtect … 2020 Hauser, Cisco Security Manager … 2023 Bishop Fox, GoAnywhere MFT … 2025 Rapid7, Connect Secure |  | First evidence of silent security patching in the motor vehicles. |

## Slide 16

and the update to remediate it.

## SECTION: THE RECALL

## Slide 17

## The 2024 Bendix EC80 Recall(s)

**Apr 2020**

Affected Units Produced

"ESC and ATC EC-80 ECUs produced between about April 2020…"

**~2023 , Sep 2024**

**Field Reports, Competitor's TSB**

"high electrical noise and low Power Line Carrier (PLC) signal strength"

**Oct 2024**

(Initial) Recall, **ID9363** updater released

Recalls 24V-790 and 24V-818 for two OEMs

"**memory overwrite** effects"

**The tip** 🎯

Engineer flags it to NMFTA

**Dec 2024**

One more OEM

Recall 24V-915

**Feb 2025**

Approached Bendix

**Oct 2025**

Aftermarket parts added

Recalls 25E07-3000, -8000, 7000

**Nov 2025 – Jan 2026**

In-Motion Security Impact of Recall Confirmed by NMFTA

Reverse Engineering Completed early 2026

**July 17th**

Recall Status

24V780000, 25E07-3000, -7000, -8000: **99.04%** 24V818000: **81.45%** 24V915000: **70.32%**

*OEM Original Equipment Manufacturer (they make the trucks)

## Slide 18

## The Recall's Remediation

Bendix released ID9363 to remediate all ECUs affected by the recall.

We obtained the executable and used it to update our own ECUs (one for each OEM recall)

Firmware updater software (Windows exe) 'ID9363'

Unified Diagnostic Services (UDS) transfer over J1939 to one of the two S12X MCUs inside the Bendix EC-80 ABS / stability controller

## Slide 19

## Inside the ID9363 Update

Skipped region is very likely the bootloader hosting the ECU-side transfer

Entropy level suggests that cleartext firmware is transferred

## Slide 20

## SECTION: REVERSING & BINDIFFING THE S12X FIRMWARE

From chip to callgraphs.

## Slide 21

## Extracting Firmware via BDM Interface

*BDM (Background Debug Module)

## Slide 22

## Beating Banked Memory (etc.)

- Making duplicates of data in (banked) segments

- Function-pointer discovery

- PID handlers table parsing

- Basic concolic analysis

*PID: signal 'types'

**Before Memory Map Correction**

**After Memory Map Correction**

## Slide 23

## Automated QBinDiff Results

|  | 1ec80 | 2ec80 | 3ec80 |
|---|---|---|---|
| New | 0 | 0 | 0 |
| Deleted | 104 | 127 | 123 |
| Modified | 11 | 12 | 13 |
| Unchanged | 1109 | 1100 | 1031 |
| Low Confidence | 12 | 13 | 14 |

- Byte Differences
- <95% confidence Function Extents
- Function Extents (unmatched)
- Function Extents (matched, changed)
- Function Extents (matched, unchanged)
- PPAGE Regions (16KiB)

"Drive Block" 1 of 2

3ec80 · 2ec80 · after · 1ec80 · before

## Slide 24

What the ID9363 updater changed.

## SECTION: BINDIFF RESULTS & DELETED J2497 ATTACK SURFACE

## Slide 25

## J2497 Receive Path Changes

Interrupt Context

sub_C12B (SCI2 ISR/Handler)

via various

sub_EBBB47 (Main State Machine) Handles: RX, Idle, Timeout

via sub_EC8000 · Byte Received Pass Byte (B Reg) · Increment on Frame Complete

sub_F1AFA7 (SCI2 Data Read and Error Checking)

sub_EC803E (Append Rx Buf)

Read Data · Write Byte

Hardware Registers: SCI2_DRL (Data Register Low)

Local Memory - RAM: (1) FIFO Receive Buffer Addr: 0x3BF5 (J2497 Frame Data); (2) Frame Counter Addr: 0x3BF4 (Semaphor)

Local Memory

RAM: (1) FIFO Receive Buffer Addr: 0x3BF5 (J2497 Frame Data); (2) Frame Counter Addr: 0x3BF4 (Semaphor)

PFLASH: PID Handlers Table Addr: 0xD9DD (via Context 0xDC3D); Post-Processing Table Addr: 0xD87D (via Context 0xDC3D)

Read · Read (Polling)

Main Thread

sub_EEB989 (check LAMP ON OFF and ABS event)

Read Base Addr Calculate Offset · Indirect Read via PayloadPtr · Fall-through Call · Read Table Rows

sub_F096F9 (PID payload splitting and periodic post-processing)

Call (Pass PayloadPtr: SP+0x17, Len: SP+0x13)

sub_F2A3E1 (dispatch each PID payload)

## Slide 26

## J2497 Receive Path Changes

Interrupt House-keeping · Build Message Byte by Byte · Flag Message Received

Poll for Received Message · Handle LAMP or 'ABS Event Active'? · Handle other (J1587) PIDs · PID Handler Table

## Slide 27

## PID Handlers Removed

| **BYTES MATCH** | **J1587 STANDARD PID DESCRIPTION** | **DATA INPUT SIZE** |
|---|---|---|
| ***PID request handlers group*** |  |  |
| **0031 / 803188** | Request for 0x31 ABS Control Status | one byte data (broadcast req) / zero bytes data (unicast req) |
| *… (13 more request handlers)* |  |  |
| ***Streamed PID handlers group*** |  |  |
| **2A** | 42 Pressure Switch Status | 1 byte data |
| *… (6 more)* |  |  |
| **C2** | 194 Transmitter System Diagnostic Code and Occurrence Count Table | variable bytes data; byte count followed by sets of diagnostic data |
| **C3** | 195 Diagnostic Data Request / Clear | 3 bytes data |
| **C7** | 199 Traction Control Disable State | variable length data; byte count, state flags, ASCII access code of 0–15 characters selected by the manufacturer |
| **D1** | 209 ABS Control Status, Trailer | variable bytes data; up to 3 × 5 bytes for 5 trailers, byte count followed by status bytes |
| **ED** | 237 Vehicle Identification Number | variable bytes data; byte count followed by VIN ASCII |
| **F5** | 245 Total Vehicle Distance | 4 bytes data |
| **F7** | 247 Total Engine Hours | 4 bytes data |
| **FE88C5 / FE88C6** | 254 Proprietary DLE | (only 0xC5 and 0xC6) |
| **FF73** | 115 Trailer Pneumatic Supply Line Pressure | one byte data |
| **FF7B** | 123 Door Status | one byte data |

## Slide 28

What lived in the deleted code.

## SECTION: VULNERABILITIES & DEMOS

## Slide 29

## Vulns in the Deleted Code

| **COMPONENT** | **VULNERABILTIY** | **IMPACT** |
|---|---|---|
| PID 0xC2 | Buffer Overflow | DoS (Verified), RCE (Verified) |
| PID 0xED | Unbounded Copy | DoS (Verified), RCE (Theoretical) |
| PID 0xC7 | Hardcoded Credential | Auth Bypass (Verified) |
| SCI2 EDGE | OOB Write | DoS (Theoretical), RCE (Theoretical) |

## Slide 30

## Demos: DoS on the Track, RCE on the Bench

## Slide 31

**Control: no attack signal**

## Slide 32

This slide carries no title or text of its own.

## Slide 33

This slide carries no title or text of its own.

## Slide 34

This slide carries no title or text of its own.

## Slide 35

## RCE

sigrok FX2 LA (8ch)

CAN_RX · J2497-J1708

J1708 decode: J1708: RX Data — 89c234a7200e6019800a08c00c00da7a9a10a…a462

CAN 2.0 decode: CAN 2.0: Payload

CAN Payload

18f0090b · DATA=0xffffffffffffffff · 0c00c005 · 0xc00c00da7a9a10ad

## Slide 36

## Exploitation/Abuse Mechanisms

| VULNERABILITY | METHOD (Verified Only) |
|---|---|
| PID 0xC2 – Buffer Overflow | **DOS**: Single Message; **RCE**: Uninterrupted Message Sequence |
| PID 0xED – Unbounded Copy | **DOS**: Repeated Message |
| PID 0xC7 – Hardcoded Credential | Single Message |
| SCI2 EDGE – OOB Write ‘Race Condition’ | **DOS**: Custom J2497 Signals |

## Slide 37

What ID9363 really was.

## SECTION: CONCLUSIONS & TAKEAWAYS

## Slide 38

## ID9363 is Also a Security Patch

- Removes unauthenticated memory corruptions (both DoS and RCE)

- Removes a hardcoded-credential

- Reachable wirelessly from various distances (equipment-dependent)

- Reachable by compromised trailer telematics

## Slide 39

## On 'Random Noise'

EDGE: plausible as a noise triggered bug

## Slide 40

## Now Aligned With Best Practices

|  | Guidance | AFTER ID9363 |
|---|---|---|
| ATA TMC PP 2024-3 | Restrict tractor J2497 to lamp messages | ✓ |
| CISA ICSA-25-021-03 | Minimize reachable attack surface | ✓ |
| SAE J2497 (2026) | Receive ABS warning lamp **only** | ✓ |

## Slide 41

## The Recall Effort is Commendable

Best Practice Documents:

- ISO/IEC 29147 Information Technology– Security Techniques– Vulnerability Disclosure

- CISA “*Shifting the Balance of Cybersecurity Risk: Principles and Approaches for Security-by-Design and-Default*”

Security patches should be communicated to users so that they can make their own informed risk calculations.

## Slide 42

## Acknowledgements

- This work would not be possible without the support of the member fleets of the NMFTA Inc.

- AIS and AFRL for access to their Class 8 vehicle multiple times during this research.

- Hannah Silva and Jesse Norton for sharing S12X development materials and EC80 experience.

- Chris York for the trailhead.

- Jonatan Mars for critical support at a critical time.

- Many industry engineers for their support of this research– the rest of whom would prefer not to be named.

- We used various large language models (Gemini 2, 2.5 pro, 3-pro) for tasks such as: drafting Python code and Mermaid diagrams.

- We acknowledge the open-source tools used: Zynamics BinDiff, Quarkslab QBinDiff, Quokka, Python 3, python-can, py-hv-networks, RP1210 python, Osmocom FL2K

## Slide 43

# THANK YOU

**White paper:**

**<u>https://i.blackhat.com/BH-USA-26/Presentations/BHUS26-Gardiner-Tractor_ECU_RE-WP.pdf</u>**

**Ben Gardiner** NMFTA Inc.

