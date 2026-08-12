---
title: "E-Trojans Ransomware, Tracking, DoS, and Data Leaks on Xiaomi Electric Scooters"
speakers: ["Marco Casagrande", "Daniele Antonioli"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Marco Casagrande&Daniele Antonioli_E-Trojans Ransomware, Tracking, DoS, and Data Leaks on Xiaomi Electric Scooters.pdf"
pages: 38
sha256: "c5c6586209b00eaf5c1fbd666a1622b5c8cb828105d8304e61bfe06060787754"
text_chars: 14982
ocr_pages: 9
has_ocr: true
redacted_secrets: 0
ocr_confidence: 91.0
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:16:24Z"
---
# E-Trojans Ransomware, Tracking, DoS, and Data Leaks on Xiaomi Electric Scooters

**Speakers:** Marco Casagrande, Daniele Antonioli  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Marco Casagrande&Daniele Antonioli_E-Trojans Ransomware, Tracking, DoS, and Data Leaks on Xiaomi Electric Scooters.pdf` (38 pages)


## Slide 1

**E-Trojans: Ransomware, Tracking, DoS, and Data Leaks on Battery-powered Embedded Systems**

M. Casagrande (KTH), D. Antonioli (EURECOM).

#BHUSA   @BlackHatEvents

## Slide 2

# Marco Casagrande

- ●Postdoc at <u>KTH</u> (Sweden), Prof. Papadimitratos ○ <u>Networked Systems Security (NSS) group</u>

- PhD at EURECOM (France), Dec 2024, Prof. Antonioli

- ●Research in Security and Privacy:

   - Proprietary protocols (fitness trackers, e-scooters, …)

   - ○ Standard protocols (BLE, Wi-Fi, NFC, FIDO2, …)

   - Mobile (Android, …)

2

#BHUSA   @BlackHatEvents

## Slide 3

# Daniele Antonioli

●Professor at <u>EURECOM (</u> France) ○ <u>Software and System Security (S3) group</u>

- ●Research **security and privacy**

   - Bluetooth (BLUFFS, BLURtooth, BIAS, KNOB, …)

   - ○ E-Scooters (E-Spoofer, E-Trojans, …)

   - FIDO2 (CTRAPS, …)

   - Web tracking (FP-tracer, …)

   -

- …

●More at <u>https://francozappa.github.io</u>

3

#BHUSA   @BlackHatEvents

## Slide 4

# Acknowledgments

- ●Co-authors from University of Padova (UniPD) ○ Riccardo Cestaro

- Prof. Eleonora Losiouk

- ○ Prof. Mauro Conti

4

#BHUSA   @BlackHatEvents

## Slide 5

E-Trojans Talk Outline

●Introduction ●Vulnerabilities and Attacks ●Overvoltage Battery Destruction ●Undervoltage Battery Ransomware ●RE, Toolkit, and Evaluation ●Countermeasure and Disclosure

5

#BHUSA   @BlackHatEvents

## Slide 6

# **Introduction**

#BHUSA   @BlackHatEvents

## Slide 7

# E-Scooter Ecosystem

Prop proto  Standard TLS
over BLE
E-Scooter E-Scooter  E-Scooter
mobile app backend

7

#BHUSA   @BlackHatEvents

## Slide 8

Xiaomi E-Scooter Ecosystem Xiaomi is a _e-scooter market leader_ (personal and rental) e-scooters, including **M365** and **Mi 3** . **Mi Home** mobile app to manage the e-scooter (password lock, firmware update, …). E-scooter can be remotely attacked to compromise security, privacy, and safety.

8

#BHUSA   @BlackHatEvents

## Slide 9

Don’t Give me a Brake, Zimperium 2019 [ <u>ref]</u>

Attacker remotely locks a Xiaomi M365 e-scooter via a custom wireless message.

9

#BHUSA   @BlackHatEvents

## Slide 10

# Our Xiaomi **E-Spoofer** Attacks 2023 [ref]

10

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
E-Spoofer: Attacking and Defending Xiaomi Electric Scooter
Ecosystem
Marco Casagrande
marco.casagrande@eurecom.fr
EURECOM
Sophia Antipolis, France
Mauro Conti
mauro.conti@unipd.it
University of Padova
Padova, Italy
ABSTRACT
Xiaomi is the market leader in the electric scooter (e-scooter) seg-
ment, with millions of active users. It provides several e-scooter
models and Mi Home, a mobile application for Android and iOS
to manage and control an e-scooter. Mi Home and the e-scooter
interact via Bluetooth Low Energy (BLE). No prior research eval-
uated the security of this communication channel, as it employs
security protocols proprietary to Xiaomi. Exploiting these protocols
results in severe security, privacy, and safety issues, e.g., an attacker
could steal an e-scooter or prevent the owner from controlling it. In
this work, we fill this research gap by performing the first security
evaluation on all proprietary wireless protocols deployed to Xiaomi
e-scooters from 2016 to 2021. We identify and reverse-engineer
four of them, each having ad-hoc Pairing and Session phases. We
Riccardo Cestaro
riccardo.cestaro.1@studenti.unipd.it
University of Padova
Padova, Italy
Eleonora Losiouk
eleonora.losiouk@unipd.it
University of Padova
Padova, Italy
Daniele Antonioli
daniele.antonioli@eurecom.fr
EURECOM
Sophia Antipolis, France
CCS CONCEPTS
+ Security and privacy — Mobile and wireless security; Hard-
ware reverse engineering.
KEYWORDS
Security, Xiaomi, Electric Scooter, Reverse Engineering
ACM Reference Format:
Marco Casagrande, Riccardo Cestaro, Eleonora Losiouk, Mauro Conti, and
Daniele Antonioli. 2023. E-Spoofer: Attacking and Defending Xiaomi Elec-
tric Scooter Ecosystem. In Proceedings of the 16th ACM Conference on Secu-
rity and Privacy in Wireless and Mobile Networks (WiSec '23), May 29-June
1, 2023, Guildford, United Kingdom. ACM, New York, NY, USA, 11 pages,
https://doi.org/10.1145/3558482.3590176
Xiaomi Protocols
Over BLE
+>
Xiaomi E-scooter
Xiaomi Protocols
Over BLE
User Phone
E-scooter
Web Requests
Pee Wi-Fi
Xiaomi Backend
p 4 Remote Attacker
Xiaomi Protocols
Over BLE
Victim
Phone
10
```

## Slide 11

# Our Xiaomi **E-Trojans** Attacks 2023 [ref]

11

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Our Xiaomi E-Trojans Attacks 2023 [
E-Trojans: Ransomware, Tracking, DoS, and Data Leaks
on Battery-powered Embedded Systems
Marco Casagrande
EURECOM
marco.casagrande @ eurecom.fr
Mauro Conti
University of Padova
mauro.conti@ unipd. it
Abstract
Battery-powered embedded systems (BESs), such as laptops,
smartphones, e-scooters, and drones, have become ubiquitous.
Their internals (hardware and firmware) include a battery
management system (BMS), a radio interface, and a motor
controller. Despite their associated risk, there is little research
on BES internal attack surfaces. For example, what can be
accomplished by a (remote) attacker with access to a BMS
needs to be clarified. This lack of understanding is primarily
due to the challenges of analyzing internal attack surfaces, as
these components are vendor-specific, proprietary, and undoc-
umented.
Ta fill thie aan we nrecent the firct cecurity and nrivacy
Riccardo Cestaro
University of Padova
Eleonora Losiouk
University of Padova
Daniele Antonioli
EURECOM
daniele.antonioli@ eurecom.fr
omy by 50% in three hours, and our user tracking generates
a persistent fingerprint to track the user over BLE while also
leaking sensitive data about the e-scooter. We propose four
practical countermeasures to fix our attacks and improve the
Xiaomi e-scooter ecosystem security and privacy.
1 Introduction
Battery-powered embedded systems (BESs) are an integral
part of our society. They include electric cars, e-scooters,
e-bikes, drones, smartphones, and laptops. Electric vehicles
alone have a market size of USD 422.8 billion [68]. Mean-
while e.cenatere have a market of TISD 27 hill
BMS Board
BCTRL DRV Board
BMON BTS Board
Batt Charger
[ay
BLE
Remote
```

## Slide 12

# Xiaomi E-Scooter Internals Block Diagram

**DRV** : Electric motor system

**BMS** : Battery management system **BTS** : Bluetooth radio system for remote control

12

#BHUSA   @BlackHatEvents

## Slide 13

# Xiaomi E-Scooter Internals Pictures

M365 ES3
Batt Batt
BTS

13

#BHUSA   @BlackHatEvents

## Slide 14

Target Most Pop E-Scooters Gen in 2023 (+1M sold) **M365:** 1st gen, 2016. **Mi 3 (ES3):** 2nd gen, 2021.

**Mi 3 (ES3):** 2nd gen, 2021.

Others: Pro (2018), Pro2/1S/Essential (2020).

14

#BHUSA   @BlackHatEvents

## Slide 15

E-Trojans target E-Scooters and Chips

- **●M365**

   - BTS (Nordic nRF51822)

   - ○ BCTRL (STMicro STM8L151K6)

   - ○ BMON (Texas Instr. BQ76930)

- **●Mi 3 (ES3)**

   - BTS (Nordic nRF51822)

   - ○ BCTRL (STMicro STM8L151K6)

   - BMON (Texas Instr. BQ76930)

15

#BHUSA   @BlackHatEvents

## Slide 16

**E-Trojans Vulnerabilities and Attacks**

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
E-Trojans Vulnerabilities and Attacks
```

## Slide 17

# Proximity and Remote Attacker Models

Victim
smartphone
Malicious app
(modding app)

17

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Proximity and Remote Attacker Models
BMON
BMS Board
BCTRL DRV Board
V3 V4
BTS Board
4
da
Batt Charger
smartphone
C2} Malicious app
Remote (modding app)
BLE
Attacker 17
```

## Slide 18

# Four E-Trojans Vulnerabilities

**V1** : Unencrypted BCTRL firmware **V2** : Unsigned BCTRL firmware **V3** : UART lacks integrity, encryption, and authentication **V4** : UART lacks DoS protection

18

#BHUSA   @BlackHatEvents

## Slide 19

E-Trojans Attack Technique (E-Spoofer auth bypass)

Attacker BCTRL Radio (BTS) as Mi Home BLE: E-Spoofer Mi Home auth bypass BLE: BCTRL firmware update UART: Malicious BCTRL update UART: BCTRL update OK BLE: BCTRL update OK

19

#BHUSA   @BlackHatEvents

## Slide 20

Five E-Trojans Attacks on Xiaomi Internals

1. **UBR** : Undervoltage Battery Ransomware

2. **OBD** : Overvoltage Battery Destruction

3. **UTI** : User Tracking via Internals

4. **DES** : Denial of E-Scooter Services

5. **PLR** : Password Leak and Recover

20

#BHUSA   @BlackHatEvents

## Slide 21

# **Overvoltage Battery Destruction (OBD)**

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 83/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
blackhat ee
BRIEFINGS SV
AUGUST 6-7, 2025 la
Overvoltage Battery Destruction (OBD)
```

## Slide 22

# E-Scooter Battery Overvoltage

**Critical: VBC > 4.7V** E-scooter plugged to the charger. **Dangerous: VBC > 4.2V** BCTRL stops charging when all VBC are at 4.2V (100% charge). **100% charge Battery overvoltage** (voltage **OK: VBC in [3.6V, 4.2V]** overflow) when a VBC > 4.2V.

**OV**

**Battery Cell**

22

#BHUSA   @BlackHatEvents

## Slide 23

# E-Scooter Battery Overvoltage Threshold

**Critical: VBC > 4.7V** BMON has a 1 Byte OV register. When set to 0xFF, BMON sends an **Dangerous: VBC > 4.2V** OV alarm if VBC > 4.7V (critical OV). **100% charge** BCTRL initializes the BMON OV register and reacts to OV alarms. **OK: VBC in [3.6V, 4.2V]** Eg: stop charging, load balancing.

**OV**

**Battery Cell**

23

#BHUSA   @BlackHatEvents

## Slide 24

# Overvoltage Battery Destruction ( **OBD** )

**OBD** flashes BCTRL firmware: 1) Sets BMON OV threshold to 4.7V. 2) Ignores BMON OV alarm → cell can overvolt (>4.2V). 3) Ignores load balancing issues → faster overvoltage. 4) Reports no overvoltage to BTS → stealthy to Mi Home and user. Overvoltage → battery damage, overheating, swelling, fire, explosion.

24

#BHUSA   @BlackHatEvents

## Slide 25

# **Undervoltage Battery Ransomware (UBR)**

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 83/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
blackhat ee
BRIEFINGS SV
AUGUST 6-7, 2025 la
Undervoltage Battery Ransomware (UBR)
```

## Slide 26

# E-Scooter Battery Undervoltage **Battery Cell**

**UV**

**OK: VBC in [3.6V, 4.2V]**

**0% charge Dangerous: VBC < 3.6V**

**Critical: VBC < 1.58V**

BCTRL activates sleep mode to prevent discharge when all VBC are at 3.6V (0% charge). **Battery undervoltage** (voltage underflow) when a VBC < 3.6V. E-scooter could be charging.

26

#BHUSA   @BlackHatEvents

## Slide 27

# E-Scooter Battery Undervoltage Threshold **Battery Cell**

**UV**

**OK: VBC in [3.6V, 4.2V]**

**0% charge Dangerous: VBC < 3.6V**

**Critical: VBC < 1.58V**

BMON has a 1 Byte UV register. When set to 0x00, BMON sends an UV alarm if VBC <1.58V (critical UV). BCTRL initializes the BMON UV register and reacts UV alarms. Eg: sleep mode, load balancing.

27

#BHUSA   @BlackHatEvents

## Slide 28

# Undervoltage Battery Ransomware ( **UBR** )

**UBR** flashes BCTRL firmware: 1) Sets BMON UV threshold to 1.58V. 2) Ignores BMON UV alarm → cell can undervolt (<3.6V). 3) Ignores load balancing issues, no charging, no sleep mode. 4) Reports no undervoltage to BTS. 5) Asks for a ransom over BLE.

Undervoltage → battery damage, gas, short circuit, polarity inversion.

28

#BHUSA   @BlackHatEvents

## Slide 29

# **RE, Toolkit, and Evaluation**

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
RE, Toolkit, and Evaluation
```

## Slide 30

Reverse Engineering E-Scooters

- ●Months of static and dynamic RE ○ Static: firmware decompiling, disassembling, …

- ○ Dynamic: firmware debugging, internal traffic analysis, …

- ●RE of BCTRL firmware with Ghidra ○ Downloaded STM8 plugin, LE ( <u>ref)</u>

- ○ Set memory map: FLASH, RAM, … ( <u>ref)</u>

- ●BCTRL firmware runtime debugging ○ ST-Link, SWIM, COSMIC debugger

30

#BHUSA   @BlackHatEvents

## Slide 31

E-Trojans Toolkit has 3 Modules ( <u>repo)</u>

●Binary patcher

   - Adds malicious features to BCTRL firmware via binary patching

   - ○ Eg: ignore BMON alarms, disable charging, disable balancing, …

- ●Malicious BCTRL firmware

   - UBR, OBR, UTI, …

   - Flashable with a script

- ●UBR ransom app and backend

   - To be installed to pay the ransom

   - Backend with Django and MongoDB

31

#BHUSA   @BlackHatEvents

## Slide 32

# E-Trojans Attack Evaluation (2024)

Attack M365 ES3
UBR ✓ ✓ *
OBD ✓ ✓
UTI ✓ ✓
DES ✓ ✓
PLR ✓ ✓

***** : Best undervoltage is 2.75V because of DRV.

Pro, Pro2, 1S, and Essential also vulnerable because they are affected by **V1--V4** .

32

#BHUSA   @BlackHatEvents

## Slide 33

# **Countermeasures and Disclosure**

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Countermeasures and Disclosure
```

## Slide 34

# E-Trojans Four Countermeasures

- ●We propose **4 countermeasures** (CN fixes VN) ○ **C1** : Encrypt the BCTRL firmware with Xiaomi <u>TEA</u> ○ **C2** : Sign and verify the BCTRL firmware with ECDSA

- ○ **C3** : Protect the UART bus with SCP03

- **C4** : Protect the UART bus with rate limiting

- ●Lightweight and legacy-compliant

   - Compatible with Xiaomi TEA and ECDSA used by Xiaomi

34

#BHUSA   @BlackHatEvents

## Slide 35

# Xiaomi Disclosure (via HackerOne)

●E-Spoofer disclosure

   - Nov 2021, informative (vulns not repro)

- ●E-Trojans 1st disclosure ○ Nov 2023, informative (attacks not repro)

● E-Trojans 2nd disclosure

- June 2025, acknowledged our attacks

- ○ Medium CVE to be assigned, highest bounty for its category

35

#BHUSA   @BlackHatEvents

## Slide 36

Xiaomi Statement about E-Trojans BHUS Talk

● The M365 and ES3 (Mi3) models have reached the end of their lifecycle. For more details, please refer to our <u>Trust Center.</u>

● These vulnerabilities have been mitigated in all subsequent Xiaomi electric scooter models, which now incorporate enhanced security measures.

36

#BHUSA   @BlackHatEvents

## Slide 37

# E-Trojans Sound Bytes

●E-scooter internals can be (remotely) attacked

- Overvolt the battery via rogue BCTRL firmware ( **OBD** )

- ○ Undervolt the battery via rogue BCTRL firmware ( **UBR** )

●Safety, security, and privacy implications

   - Damage battery, fire, explosion, …

   - Track a user via e-scooter, …

- ●Security-through-obscurity is bad

- ●E-Trojans on other battery-powered devices?!

37

#BHUSA   @BlackHatEvents

## Slide 38

Grazie! Q&A

38

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Grazie! Q&A
VETENSKAP
OCH KONST
Trojans: Ransomware, Tracking, DoS, and Data Leaks
on Battery-powered Embedded Systems BMS Board 4 44
Marco Casagrande Riccardo Cestaro Eleonora Losiouk vl
EURECOM University of Padova University of Padova v2 oe Batt Charger
marco.casagrande @ eurecom.fr riccardo.cestaro@ outlook. it eleonora.losiouk@ unipd.it DRV B ~ d
Mauro Conti Daniele Antonioli
University of Padova EURECOM
Abstract omy by 50% in three hours, and our user tracking ge 12C UART BLE At]
Battery-powered embedded systems (BESs), such as laptops, _® Persistent fingerprint to track the user over BLE while also Remote
smartphones, e-scooters, and drones, have become ubiquitous. leaking sensitive data about the e-scooter. We propose four Attack
Their internals (hardware and firmware) include a battery _ Practical countermeasures to fix our attacks and improve the acker
management system (BMS), a radio inter nda motor Xiaomi e-scooter ecosystem security and privacy
controller. Despite their associated risk, there is little research
on BES internal attack surfaces. For example, what can be 1 Introduction BLE
accomplished by a (remote) attacker with access to a BMS
needs to be clarified. This lack of understanding is primar Battery-powered embedded systems (BESs) are an integral BMON BTS Board
due to the challenges of analyzing internal attack surfaces, part of our society. They include electric cars, e-scooters, Proximity
these components are vendor-specific, proprietary, and undoc e-bike: smartphones, and laptops. Electric vehicles
umented. alone have a market size of USD 422.8 billion [68]. Me Attacker
Tr fll thie oan wa
38
```
