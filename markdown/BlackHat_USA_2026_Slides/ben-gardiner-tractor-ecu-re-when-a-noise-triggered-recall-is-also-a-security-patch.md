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
text_chars: 12337
ocr_pages: 7
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:06:20Z"
---
# Tractor ECU RE When a Noise Triggered Recall is Also a Security Patch

**Speakers:** Ben Gardiner  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/Ben Gardiner_Tractor ECU RE When a Noise Triggered Recall is Also a Security Patch.pdf` (43 pages)

## Slide 1

Tractor ECU RE: When a "Noise-Triggered” Recall is Also a Security Patch

Safety-Impacting vulns patched in the recall of ~450,000 Trucks via SAE J2497 (PLC4TRUCKS)

**Ben Gardiner** NMFTA Inc.

1

## Slide 2

#### Almost a Decade Watching Truck Cybersecurity

**The National Motor Freight Traffic Assoc.** has been analysing truck cybersecurity and sharing its findings since ~2017.

2

## Slide 3

3

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Cameras
(Int & Ext)
Telematics
‘CABIN’ J1939
Fleet ~ RP1226 OBD Engine /
Telematics Connector Connector Aftertreat.
J1939
Brake ~
Telematics
Temperature
Canvassing
Telematics
via Modem
Trailer
ABS
Lift Axle
black hat
2026 3
```

## Slide 4

## SECTION: MOTIVATIONS

Why NMFTA chased a brake-controller recall.

4

## Slide 5

## Our J2497 Track Record

- Studying **J2497** (PLC4TRUCKS) protocol since 2019

- Three CVEs across J2497 and trailer equipment

- Three CISA ICS Advisories also (one for each)

- (several) Public domain technical mitigations against wireless attacks released

- *PLC: Power-Line Carrier

Yet we were told, repeatedly, that tractors are unaffected.

5

## Slide 6

## A Tip About a Recall

- An engineer friend flagged a safety recall.

- It blamed a brake-controller crash on noise in-band with the **J2497** protocol.

- Could that crash be triggered **intentionally** ?

*Recall of: the Bendix EC80 Anti-lock Braking System (ABS) / Electronic Stability Program (ESP) controller.

6

## Slide 7

## Current Threat Model

Fleets assume tractor safety systems are isolated from the trailer's unauthenticated PLC4TRUCKS (J2497)

The operators of the equipment believe they can ignore the J2497 attack path found in every class 8 towing application trucks since 2001.

7

## Slide 8

## Safety & Security

**<u>IT</u>** (yet again) Stays **<u>secure</u>** if updated frequently **<u>Cyber-Physical Systems</u>** Stays **<u>safe</u>** if left untouched

8

## Slide 9

## SECTION HEAVY VEHICLES: J1939 & PLC4TRUCKS

###### Meet the vehicle architecture, the buses.

9

## Slide 10

Trailers and Tractors
12 Volts DC Trailer Fault
Ground
 & J2497 Bus LAMP
Trailer
Telematics
Trailer
Brake
ECU Trailer
Trailer
Brake
Brake
ECU
ECU
Tractor
Brake
ECU
J1939
e.g. a Bendix  Busses
EC80 Brake
Controller

## Slide 11

#### Truck Attack Surface: Diagnostics-time vs Mission-time Communications

**DIAGNOSTICS**

##### **MISSION-TIME**

**This communication is rejected while in motion**

Authentication & Authorization: Seed-Key exchange

Cyber-physical impacts. Commands, reconfigurations and also firmware dump, update

**Works (as intended) in motion** OLD: network access only, NEW: message authentication codes on the bus Cyber-physical impacts. Many are a de-rate.

Connections: e.g. UDS, KWP2000, XCP

Signals encoded in: SPNs (J1939), **PIDs (J1587)**

**Same data busses: J1939 and J2947/J1708/J1587**

## Slide 12

#### Two Buses: J2497 & J1939

###### <u>J2497 (powerline PHY for J1587)</u>

- 9600 bps

- One segment

- Mission-time LAMP and ‘ABS event active’ messages standardized

- Diagnostics: none

<u>J1939 (aka CAN bus)</u>

- 250 kbps / 500 kbps

- **Multiple segments**

- Mission-time standardized J1939 signals (and proprietary messages)

- Diagnostics both J1939-specific and UDS

12

## Slide 13

#### Wirelessly Accessible

- Tractor brakes are wirelessly accessible via CVE-2022-26131.

- Range is equipment-dependent. Most susceptible is tankers.

- E.g. wireless write to tanker J2497 segment from ~15 ft (~3m) range, for ~300 USD of gear

13

## Slide 14

## Bridging the Trust Boundary

Gateway

Copyrig ht ©

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Bridging the Trust Boundary
w------------ —=~
\ ~~
Body / Cameras ! Climate Radio OEM
Chassis we iint & Ext) ) Control Telematics
‘CABIN’ J1939
i
Cluster
1
‘PT’ J1939 13
Fleet ~ RP1226 Engine / Engine=
Telematics Connector ete Aftertreat. felematics |
J1939
Stability / Adaptive ADAS Lane Trans- Tire Pres
Suspension CC Keep mission Mon SYS
black hat
2026 Copyrig
ht ©
Brake ~
Ladle
```

## Slide 15

## Building on Prior Work

###### **This work**

This work: Mission Time instead of Diagnostic Time

This work: More in Silent Patches

**Other’s Prior work Our Prior Work** Hass et. al. 2016 (Wired): NMFTA + AIS 2020, commanding tractor systems via NMFTA 2022-2024 extends J1708 to Wireless J2497

**This Works’ Firsts**

Chatterjee 2024 exploiting J1939 diagnostics on tractors

- First evidence of safety impact on tractors via (wireless) J2497.

• First reverseengineering of a safety recall's firmware update.

2019 DEVCORE, PAN-OS GlobalProtect … 2020 Hauser, Cisco Security Manager … 2023 Bishop Fox, GoAnywhere MFT … 2025 Rapid7, Connect Secure

- First evidence of silent security patching in the motor vehicles.

15

## Slide 16

and the update to remediate it.

## SECTION: THE RECALL

16

## Slide 17

## The 2024 Bendix EC80 Recall(s)

**Apr 2020 ~2023 , Oct 2024 Dec 2024 Feb 2025 Oct 2025 Nov 2025 – July 17th Sep 2024 Jan 2026** Affected **Field** (Initial) **The tip** One more Approached Aftermarket In-Motion Recall Status Units **Reports,** Recall, OEM Bendix parts added Security Produced **CompID9363** Impact of **etitor’s** Recall updater **TSB** Confirmed released by NMFTA

“ESC and “high Recalls Engineer Recall 24VATC EC-80 electrical 24V-790 flags it to 915 ECUs noise and and 24VNMFTA produced low Power 818 for two between Line Carrier OEMs about April (PLC) signal 2020…” strength” " **memory overwrite** effects"

Recalls 25E073000, - 8000, 7000

Reverse 24V780000, Engineering 25E07-3000, - Completed 7000, -8000: early 2026 **99.04%** 24V818000: **81.45%** 24V915000: **70.32%**

*OEM Original Equipment Manufacturer (they make the trucks)

17

## Slide 18

## The Recall’s Remediation

Firmware updater software (Windows exe) ‘ID9363’

Bendix released ID9363 to remediate all ECUs affected by the recall.

We obtained the executable and used it to update our own ECUs (one for each OEM recall)

Unified Diagnostic Services (UDS) transfer over J1939 to one of the two S12X MCUs inside the Bendix EC-80 ABS / stability controller

18

## Slide 19

## Inside the ID9363 Update

Skipped region is very likely the bootloader hosting the ECU-side transfer

Entropy level suggests that cleartext firmware is transferred

19

## Slide 20

## SECTION: REVERSING & BINDIFFING THE S12X FIRMWARE

From chip to callgraphs.

20

## Slide 21

## Extracting Firmware via BDM Interface

*BDM (Background Debug Module)

21

## Slide 22

## Beating Banked Memory (etc.)

**Before Memory Map Correction**

- Making duplicates of data in (banked) segments

- Function-pointer discovery **After Memory Map Correction**

- • PID handlers table parsing

- Basic concolic analysis

*PID: signal ‘types’

22

## Slide 23

## Automated QBinDiff Results

3ec80
2ec80
after
1ec80
before

23

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Automated QOBinDiff Results
aii AQAA
ITEC 1 M0
eT
I
```

## Slide 24

What the ID9363 updater changed.

## SECTION: BINDIFF RESULTS & DELETED J2497 ATTACK SURFACE

24

## Slide 25

## J2497 Receive Path Changes

25

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Ja249'7 Receive Path Changes
Interrupt Context PFLASH
sub_C12B
(SCI2 ISR/Handler) FIFO Receive Buffer
Frame Counter
Addr: 0x3BF4
t-Processing Table
S ID Handlers Table
iddr: OxD9DD
Addr: 0x3BF5
| (J2497 Frame Data) |. (Semaphor) | hid Context 0xDC3D)
via various U :
sub_EBBB47 : —_
_ Read Read (Polling)
(Main State Machine) r :
Handles: RX, Idle, Timeout a Fi Main Thread
eal jase r : 7
i H Read Table R
Via sub EC8@00 Byte Received Calculate Offset (check LAMP ON OFF ea a le Rows
{ Pass Byte (B Reg) i and ABS event) :
sub_F1AFA7 TSS Fall-through Call Read Table Rows
7 sub_EC8@3E Increment on PayloadPtr ss,
(SCI2 Data Read and E s /
. (Append Rx Buf) Frame Complete aN
Error Checking) :
sub_F@96F9
(PID payload splitting
Oo
: i aos and periodic post-
Read Data Write Byte | | processing)
Hardware Registers Call
(Pass PayloadPtr: SP+0x17,
Len: SP+0x13)
Ze sub_F2A3E1
| | | (dispatch each PID payload) t
FIFO Receive Buffer Frame Counter
Addr: 0x3BF5 Addr: 0x3BF4
(J2497 Frame Data) (Semaphor)
SCI2_DRL
(Data Register Low)
```

## Slide 26

### J2497 Receive Path Changes

Poll for Build Interrupt Flag Received Message HouseMessage Message Byte by keeping Received Byte Handle LAMP or ‘ABS Event Active’? PID Handler Handle other Table (J1587) PIDs

26

## Slide 27

## PID Handlers Removed

|**BYTES MATCH**|**J1587 STANDARD PID DESCRIPTION **|**DATA INPUT SIZE**|
|---|---|---|
||**_PID request handlers_**|**_group_**
|
|**0031 / 803188**|Request for 0x31 ABS Control Status|one byte data (broadcast req) / zero bytes data
(unicast req)|
||_…(13 more request ha_|_ndlers)_|
||**_Streamed PID handlers_**|**_group_**|
|**2A**|42 Pressure Switch Status|1 byte data|
||_…(6 more)_||
|**C2**|194 Transmitter System Diagnostic Code and
Occurrence Count Table|variablebytes data; byte count followed by sets of
diagnostic data|
|**C3**|195 Diagnostic Data Request / Clear|3 bytes data|
|**C7**|199 Traction Control Disable State|variablelength data; byte count, state flags, ASCII
access code of 0–15 characters selected by the
manufacturer|
|**D1**|209 ABS Control Status, Trailer|variablebytes data; up to 3 × 5 bytes for 5 trailers,
byte count followed bystatus bytes|
|**ED**|237 Vehicle Identification Number|variablebytes data;byte count followed byVIN ASCII|
|**F5**|245 Total Vehicle Distance|4 bytes data|
|**F7**|247 Total Engine Hours|4 bytes data|
|**FE88C5 / FE88C6**|254 ProprietaryDLE|(only0xC5 and 0xC6)|
|**FF73**|115 Trailer Pneumatic SupplyLine Pressure|one byte data|
|**FF7B**|123 Door Status|one byte data|

## Slide 28

What lived in the deleted code.

## SECTION: VULNERABILITIES & DEMOS

28

## Slide 29

## Vulns in the Deleted Code

###### **COMPONENT VULNERABILTIY IMPACT**

PID 0xC2 Buffer Overflow

DoS (Verified), RCE (Verified)

PID 0xED Unbounded Copy Hardcoded PID 0xC7 Credential SCI2 EDGE OOB Write

DoS (Verified), RCE (Theoretical)

Auth Bypass (Verified)

DoS (Theoretical), RCE (Theoretical)

29

## Slide 30

## Demos: DoS on the Track, RCE on the Bench

30

## Slide 31

31

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Control: no attack signal
```

## Slide 32

32

## Slide 33

33

## Slide 34

34

## Slide 35

## RCE

35

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
RCE
@- 8-8-8868 sigrok FX2 LA (8ch) ~ X
1+16150 me +1616N me +16290
, #16150 ms) aylog i |
CAN_RX
ppUskeene lg INOS: GYEee MEE 89¢234a7200e6019800a08c00c00da7a9a10: 3462 89c234a720
CAN 2.0 decode » CAN 2.0: Payload
5277400 ps © +16277500 us = +16277600 us © +16277700 us. ~©= +16277800us ~=s: + 162 +16278001
```

## Slide 36

## Exploitation/Abuse Mechanisms

**VULNERABILITY METHOD (Verified Only) DOS** : Single Message; PID 0xC2 – Buffer Overflow **RCE** : Uninterrupted Message Sequence PID 0xED – Unbounded **DOS** : Repeated Message Copy PID 0xC7 – Hardcoded Single Message Credential SCI2 EDGE – OOB Write **DOS** : Custom J2497 Signals ‘Race Condition’

36

## Slide 37

What ID9363 really was.

## SECTION: CONCLUSIONS & TAKEAWAYS

37

## Slide 38

## ID9363 is Also a Security Patch

• Removes unauthenticated memory corruptions (both DoS and RCE)

• Removes a hardcoded-credential

• Reachable wirelessly from various distances (equipment-dependent)

• Reachable by compromised trailer telematics

38

## Slide 39

## On 'Random Noise'

EDGE: plausible as a noise triggered bug

39

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
On ‘Random Noise"
EDGE: plausible as a noise triggered bug
black hat
USA
2026 39
```

## Slide 40

## Now Aligned With Best Practices

**Guidance AFTER ID9363** ATA TMC PP Restrict tractor 2024-3 J2497 to lamp messages CISA ICSA-25Minimize 021-03 reachable attack surface SAE J2497 Receive ABS (2026) warning lamp **only**

40

## Slide 41

## The Recall Effort is Commendable

Best Practice Documents:

- ISO/IEC 29147 Information Technology– Security Techniques– Vulnerability Disclosure

- • CISA “ _Shifting the Balance of Cybersecurity Risk: Principles and Approaches for Securityby-Design and-Default_ ”

Security patches should be communicated to users so that they can make their own informed risk calculations.

41

## Slide 42

## Acknowledgements

- This work would not be possible without the support of the member fleets of the NMFTA Inc.

- • AIS and AFRL for access to their Class 8 vehicle multiple times during this research. • Hannah Silva and Jesse Norton for sharing S12X development materials and EC80 experience.

- Chris York for the trailhead.

- Jonatan Mars for critical support at a critical time.

- Many industry engineers for their support of this research– the rest of whom would prefer not to be named.

- We used various large language models (Gemini 2, 2.5 pro, 3-pro) for tasks such as: drafting Python code and Mermaid diagrams.

- We acknowledge the open-source tools used: Zynamics BinDiff, Quarkslab QBinDiff, Quokka, Python 3, python-can, py-hv-networks, RP1210 python, Osmocom FL2K

## Slide 43

# THANK YOU

**White paper:**

**<u>https://i.blackhat.com/BH-USA-26/Presentations/BHUS26Gardiner-Tractor_ECU_RE-WP.pdf</u>**

**Ben Gardiner** NMFTA Inc.
