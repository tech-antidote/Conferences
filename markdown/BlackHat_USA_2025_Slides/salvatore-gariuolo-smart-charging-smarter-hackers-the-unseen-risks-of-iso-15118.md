---
title: "Smart Charging, Smarter Hackers The Unseen Risks of ISO 15118"
speakers: ["Salvatore Gariuolo"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Salvatore Gariuolo_Smart Charging, Smarter Hackers The Unseen Risks of ISO 15118.pdf"
pages: 20
sha256: "7d4af5c6bbc8001e3339bf1977ff5c2342f68a7ce4312ca094f8bcd157eb796e"
text_chars: 4661
ocr_pages: 1
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:00:32Z"
---
# Smart Charging, Smarter Hackers The Unseen Risks of ISO 15118

**Speakers:** Salvatore Gariuolo  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Salvatore Gariuolo_Smart Charging, Smarter Hackers The Unseen Risks of ISO 15118.pdf` (20 pages)


## Slide 1

# Smart Charging, Smarter Hackers: The Unseen Risks of ISO 15118

Salvatore Gariuolo

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisekhat
BRIEFINGS
AUGUST 6-7, 2025
MANDALAY BAY / LAS VEGAS
Smart Charging, Smarter Hackers:
The Unseen Risks of ISO 15118
Salvatore Gariuolo
```

## Slide 2

### About me

**Dr. Salvatore Gariuolo** Senior Threat Researcher

#BHUSA @BlackHatEvents

## Slide 3

### Agenda

1. The ISO 15118 Standard.

A strategic response to the EV surge

2. Old Risks, New Risks?. How ISO 15118 changes the threat landscape

3. The Hidden Risks of Compliance

Conclusion and key takeaways

#BHUSA @BlackHatEvents

## Slide 4

1. The ISO 15118 Standard

A Strategic Response to the EV Surge

#BHUSA @BlackHatEvents

## Slide 5

EV Surge: What is the problem?

**As of today** , approx. **By 2040,** we expect **27 Million** EVs **600 Million** EVs 3% of the global fleet 30% of the global fleet

**Grid Strain.**

#BHUSA @BlackHatEvents

## Slide 6

## Power Grids: A Fragile Balance

April 2025, **A lesson from Spain:**

- § **Excess electricity can disrupt grid’s frequency**

- § Renewables supply 50% - but they're intermittent

- § Consumption can adjust quickly - generation can’t

#### **The entire grid was disconnected to prevent a full collapse .**

#BHUSA @BlackHatEvents

## Slide 7

## Grid Stress: What is the solution?

**Upgrade Grid** Infrastructure Global investment needs could exceed **$4.5 billion** per year

•
•

**Smart charging and** **V2G communication**

- Dynamic charging based on grid conditions and user preferences

- EVs can absorb excess electricity and feed it back when needed

#BHUSA @BlackHatEvents

## Slide 8

ISO 15118 : Three Key Benefits Across two versions: **ISO 15118-2** and **ISO 15118- 20.**

#### **Grid-efficient**

#### **User-friendly**

**Secure**

- Smart Charging

- Plug & Charge

   - Public Key Infrastructure

- **Vehicle- to-** **Grid.**

- Multiple Profiles

- Transport Layer Security

#BHUSA @BlackHatEvents

## Slide 9

2. Old Risks, New Risks? How ISO 15118 changes the threat landscape

#BHUSA @BlackHatEvents

## Slide 10

A. Mitigated Risks Securing the Communication between EVs and Charging Stations

Digital
Private Key
Certificate How does Plug&Charge work?
- Authentication and Authorization through  PKI
- Data transmission encrypted via  TLS
No more RFID cloning or card skimming
No more eavesdropping on session ID and data

#BHUSA @BlackHatEvents

## Slide 11

A. Mitigated Risks Securing the Communication between EVs and Charging Stations Threat **Pre - ISO 15118 ISO 15118-2 ISO 15118-20 Unauthorized Charging Session Hijacking** Low Medium High #BHUSA @BlackHatEvents

## Slide 12

## B. Shifted Risks

Moving Data Security to a Centralized Back-End

e-Mobility
Service Provider
Charging Point
Operator
Charging Point
Operator

How is user data handled?

- **Single entity** managing payments and data

- **More consistency** , lower risk exposure

**Charging stations are no longer exploitable eMSP breaches can expose large pool of data**

#BHUSA @BlackHatEvents

## Slide 13

## B. Shifted Risks

Moving Data Security to a Centralized Back-End

Threat **Pre - ISO 15118 ISO 15118-2 ISO 15118-20 User Data Theft ***

- _The risk moves from the_ **_charging station_** _to the_ **_eMPS_**

Low Medium High

#BHUSA @BlackHatEvents

## Slide 14

## C. Residual Risks

Charging Stations Remain the Weak Link

- Why is this happening? - **Poor implementation** of charging stations - **No ISO 15118 guidelines** on physical security

**Stations remain vulnerable to compromise** No mechanism to verify charging station integrity

#BHUSA @BlackHatEvents

## Slide 15

C. Residual Risks
Charging Stations Remain the Weak Link
Threat Pre - ISO 15118 ISO 15118-2 ISO 15118-20
Denial-of-Service
Unsafe Power Delivery
Unauthorized Charging  *
* A threat that ISO 15118 was designed to mitigate
#BHUSA @BlackHatEvents

## Slide 16

## D. New Risks

How Innovation Opens the Door to New Threats

Where do these risks come from?

- New features like **Smart charging** and **V2G**

- **Vulnerable charging stations** as entry points **Grid signal manipulation to simulate congestion Synchronized charging / discharging cycles**

#BHUSA @BlackHatEvents

## Slide 17

D. New Risks How Innovation Opens the Door to New Threats Threat **Pre - ISO 15118 ISO 15118-2 ISO 15118-20 Charging Manipulation - Battery Degradation** * **Grid Attack *** _* These threats require V2G communication_ #BHUSA @BlackHatEvents

## Slide 18

3. The Hidden Risks Of Compliance Conclusion and key takeaways

#BHUSA @BlackHatEvents

## Slide 19

A Standard can create
a false sense of security

True security requires a shift in mindset

#BHUSA @BlackHatEvents

## Slide 20

## Black Hat Sound Bites

**While reducing risks, standards can create blind spots**

**When one piece is left out, the whole ecosystem is at risk** .

**True security requires action beyond compliance**

#BHUSA @BlackHatEvents
