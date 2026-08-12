---
title: "From Shanghai to the Shore The Silent Threat in Global Shipping"
speakers: ["Kenneth Miltenberger Nicholas Fredericksen"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33/Kenneth Miltenberger Nicholas Fredericksen - From Shanghai to the Shore The Silent Threat in Global Shipping.pdf"
pages: 31
sha256: "bc784369af635e96e91e9738b29f22b949fedad6f4f5e7106b12921f0501cb90"
text_chars: 7309
ocr_pages: 11
has_ocr: true
redacted_secrets: 0
ocr_confidence: 89.3
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T07:04:05Z"
---
# From Shanghai to the Shore The Silent Threat in Global Shipping

**Speakers:** Kenneth Miltenberger Nicholas Fredericksen  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33/Kenneth Miltenberger Nicholas Fredericksen - From Shanghai to the Shore The Silent Threat in Global Shipping.pdf` (31 pages)


## Slide 1

`

**From Shanghai to the Shore: The Silent Threat in Global Shipping**

**Kenny Miltenberger Lieutenant Commander, U.S. Coast Guard 2003 Cyber Protection Team**

**Nick Fredericksen Lieutenant Commander, U.S. Coast Guard 1790 Cyber Protection Team**

1

## Slide 2

#### Agenda

- # whoami’s

- US Coast Guard & Cyber 101

- Cranes Manufactured in China

   - Why they're important.

   - What they are.

   - What we've done to protect them.

2

## Slide 3

### # whoami’s

Kenny Nick

## Slide 4

###### The U.S. Coast Guard does cyber?

: Source: The Claw of Knowledge

4


> Recovered by OCR — confidence 95/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ASHTON
The U.S. Coast Guard does cyber?
HOW DO YOU DECIDE
WHO LIVES OR WHO DIES?
Source:
FROM THE DIRECTOR OF “THE FUGITIVE”
```

## Slide 5

###### U.S. Coast Guard Overview

5

## Slide 6

###### And we do cyber!

: Source: The Claw of Knowledge

## Slide 7

### Protecting National Critical Infrastructure

Highway and Motor Carrier

Aviation

Pipeline Systems

Mass Transit and Passenger Rail

Postal and Shipping

Freight Rail

**Marine Transportation System (MTS)**

## Slide 8

### U.S. Coast Guard Cyber Protection Teams

Reserve


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
U.S. Coast Guard Cyber Protection Teams
Reserve
CALIFORNIA REPUBLIC
```

## Slide 9

# Theory of the Case

**Ship-to-shore (STS) cranes manufactured in China present a risk to the Marine Transportation System (MTS).**

- The U.S. is dependent on cranes manufactured by a Chinese state-owned enterprise which could present a significant supply chain risk.

- Extensive analysis conducted by Coast Guard Cyber Protection Teams (CPTs) has revealed vulnerabilities that may enable a malicious cyber actor the ability to disrupt port operations.

## Slide 10

**Chinese Manufactured Cranes**


> Recovered by OCR — confidence 90/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
THE WALL STREET JOURNAL.
Espionage Probe Finds
Communications Device on Chinese
Cargo Cranes
Daily Mail
Chinese 'spy cranes' in US shipping
ports ARE equipped with secret Congressional probe finds communications
modems that could be used for gear in Chinese cranes, raising spying
espionage or sabotage, probe finds concems
THE WALL STREET JOURNAL.
‘Blazemedia Chinese Cargo Cranes at U.S. Ports Pose
Communication devices found on Espionage Risk, Probe Finds Washington * Examiner
Chinese-built cranes located at US Be sonsi dion House investigation finds Chinese-made
ports spark espionage concerns cranes at US ports have communications
gear installed
FOX\ Chinese Manufactured Suspicious tech found in Chinese-made
Chinese crane firm denies posing security risk cargo cranes, fueling spying worries:
at US ports amid investigation C r an es Congre:
BUSINESS INSIDER
China could be spying on US ports
using secret tech built into cranes
The Maritime Executive
Chinese-Built Port Cranes May Be House Committees
Able to Call Home On Their Own Probie deca leithode IDAILY CALLER}
Spying at US Ports ‘Clearly Overlooked This’: Probe Finds Strange
2 Communication Devices On Chinese Cranes In
US Ports
```

## Slide 11

#### Why cranes?

- 70% of non-bulk cargo is moved by containers.

- Over 70% of the world’s ship to shore cranes are made by Shanghai Zhenhua Heavy Industries (ZPMC), a Chinese State-Owned Enterprise (SOE).

- ZPMC accounts for over 80% of STS cranes in the U.S.

- Congressional interest:

   - <u>March 2024</u>

   - <u>September 2024</u>

## Slide 12

#### ZPMC Cranes in the US

12


> Recovered by OCR — confidence 92/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ZPMC Cranes
Port of
Port of
Portland
Port of
Oakland
Port of Long Beach/
Port of Los Angeles »
Port of
Anchorage
Port of
Kodiak
Port of
Tacoma
aera Port of Boston
Balen of Port of Newark /
Beau Elizabeth
Port of Norfolk
Port of Port of
Charleston Wilmington
Port of
Mobile Port of
Port of [— Jacksonville
Houston
Port of Ft.
Port of Port of Lauderdale
Freeport Gulfport
Port of New Port of
Orleans Port of Miami
Tampa
Port of San
Port of Juan
Ponce
```

## Slide 13

#### Supply Chain Risks

- Chinese State-Owned Enterprise (SOEs)

- Previous Supply Chain Attacks

   - Solarwinds (2020)

   - Cisco Equipment (2014-2022)

- Huawei & Salt Typhoon

- Potential impact to cranes

## Slide 14

Ok, so what are we doing about it?

## Slide 15

##### USCG Cyber Protection Team Chinese Crane Missions

- Hundreds of days sensored on cranes across multiple ports

- More time spent analyzing crane data than any other federal agency.

15

## Slide 16

#### Parts of an STS Crane

## Slide 17

#### Modern Crane Features

- Features:

   - Assisted Control Systems

   - Optical Character Recognition

   - Remote Control

   - Autonomous Cranes

- Protocols:

   - PROFINET

   - Link Layer Discovery Protocol (LLDP)

## Slide 18

#### Logical Structure of a Crane


> Recovered by OCR — confidence 87/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Cameras (10) Landside Server(s)
IP
PROFINET
Logical
Structure of
eer x
Managed Switch Managed Switch
Layer 2 PROFINET Layer 2 PROFINET
Monitoring and Control Electrical Drive Subnet
Subnet (~30) (~20)
```

## Slide 19

#### PROFINET

Wireshark view of a PROFINET frame from a ZPMC Crane


> Recovered by OCR — confidence 78/100 on the text kept, 66/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
PROFINET
> Frame 12: 68 bytes on wire (48@ bits), 6@ bytes captured (488 bits) 66 24°59 Ge Je dajee 24°59 a5 29 52/88 92)ce 88
Address: ABBAutom_@e:57:bc (@@:24:59:@e:57:bc)
1B. nae Lo bit: Globally unique address (factory default)
Address: ABBAutom_@5:29:52 (@@:24:59:05:29:52)
~“ PROFINET cyclic Real-Time, RTC1(legacy), ID:@xc@@@, Len: 48, Cycle: 2048 (Walid,Primary,Ok,Run)
FrameID: @xc@@@ (@xC@@@-@xF7FF: Real-Time(class=1 unicast): Cyclic}
“ DataStatus: 8x35 (Frame: Valid and Primary, Prowider: Ok and Run)
@... .... = Ignore (l:Ignore/@:Evaluate): @x@
-O.. .... = Reserved_2 (should be zero}: @x®@
-1. .... = StationProblemIndicator (1:0k/@:Problem): @x1
-l.... = ProviderState (1:Run/@:Stop): @xL
@... = Reserved_1 (should be zero): @x®
-l.. = DataValid (1:Valid/@:Invalid): @x1
-@. = Redundancy: Redundancy has no meaning for OutputCRs / One primary AR of a given AR-set is present
PROFINET IO Cyclic Service Data Unit: 4@ bytes
Wireshark view of a PROFINET frame from a ZPMC Crane
```

## Slide 20

## Most Common Findings

20

## Slide 21

Improper network segmentation


> Recovered by OCR — confidence 94/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Improper
network
segmentation
Remote
User/Third
Party
Contractor
Server (Data
Historian)
Controller (PLC)
Level Indicator
Flow Meter
Valve
Valve le)
Flow Meter
```

## Slide 22

### Legacy Protocols

- Telnet

- SMBv1

- LLMNR

Source: <u>Countering Password Stealing Attacks - Replace telnet with SSH.</u>

22


> Recovered by OCR — confidence 91/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Legacy
P roto CO | S Telnet server
Telnet client (telnetd)
° SMBv1
telnet protocol
“username”
Source: Countering Password Stealing Attacks - Replace telnet with SSH.
22
```

## Slide 23

#### End-of-Life OS

23


> Recovered by OCR — confidence 84/100 on the text kept, 61/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
End-of-Life OS
Microsoft
Copyright © 1985-2003 7 "4
```

## Slide 24

#### Shared Accounts

Creds to Shared Account

## Slide 25

#### Cellular Modems

This was us!


> Recovered by OCR — confidence 86/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Daily Mail THE WALL STREET JOURNAL.
Chinese 'spy cranes' in US shippin
ports ARE equipped with secret Espionage Probe Finds ,
moderns flat couldibe een tae Communications Device on Chine
espionage or sabotage, probe finc s Cargo Cranes
Washington * Examiner
House investigation finds Chinese-made
cranes at US ports have communications
gear installed
Input: === 12/24VDC, 0.8A.
‘Clearly Overlooked This’: Probe Finds Strange Ce | | U | ar M| @) d ems
Communication Devices On Chinese Cranes In
US Ports
This was us!
```

## Slide 26

Where we found cellular modems.


> Recovered by OCR — confidence 91/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Server room
with STS
cranes’ firewall
and networking
equipment
Where we
found
cellular
modems.
| Spreaders |
```

## Slide 27

#### Attack Paths

Initial Access

Lateral
Movement

Privilege
Escalation &  Effects
Persistence

## Slide 28

### Potential Cyber Effects

Physical Disruption
Ransomware/Denial-of-
Service
Data Exfiltration and
Manipulation/Espionage
Complexity

Impact

## Slide 29

###### Malicious Cyber Activity

Source: AI Generated

## Slide 30

# Best Practices

- Scrutinize contract language.

- Restrict remote access.

- Standard enterprise cybersecurity best practices!

## Slide 31

Thank you!
