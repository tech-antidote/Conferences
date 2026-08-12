---
title: "The ByzRP Solution A Global Operational Shield for RPKI Validators"
speakers: ["Donika Mirdita", "Jens Frieß", "Haya Schulmann", "Michael Waidner"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2025"
edition: "ASIA"
year: 2025
source_pdf: "Black Hat Asia 2025 Slides/Donika Mirdita & Jens Frieß & Haya Schulmann & Michael Waidner_The ByzRP Solution A Global Operational Shield for RPKI Validators.pdf"
pages: 68
sha256: "bf1762745d0a94f432ab2a4e98050c45116e41a8fb609d2131dba3dfabf823d5"
text_chars: 10349
ocr_pages: 21
has_ocr: true
redacted_secrets: 0
ocr_confidence: 86.9
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T03:53:30Z"
---
# The ByzRP Solution A Global Operational Shield for RPKI Validators

**Speakers:** Donika Mirdita, Jens Frieß, Haya Schulmann, Michael Waidner  
**Conference:** Black Hat ASIA 2025  
**Source:** `Black Hat Asia 2025 Slides/Donika Mirdita & Jens Frieß & Haya Schulmann & Michael Waidner_The ByzRP Solution A Global Operational Shield for RPKI Validators.pdf` (68 pages)


## Slide 1

**The ByzRP Solution A Global Operational Shield for RPKI Validators** <u>Jens Friess</u> |  Donika Mirdita |  Haya Schulmann  |  Michael Waidner

#BHAS @BlackHatEvents

## Slide 2

#BHAS @BlackHatEvents

BGP The Achilles' Heel of the Internet

## Slide 3

**Border Gateway Protocol (BGP)** is the defacto interdomain routing protocol. It prioritizes: ❖ **Scalability**

❖ Efficiency
❖ Speed

Notes from the IETF Cafeteria, 1989

#BHAS @BlackHatEvents

## Slide 4

**Border Gateway Protocol (BGP)** is the defacto interdomain routing protocol. It prioritizes: ❖ **Scalability**

❖ Efficiency
❖ Speed
❖ Security

Notes from the IETF Cafeteria, 1989

#BHAS @BlackHatEvents

## Slide 5

Long History of BGP Routing Hijacks...

#BHAS @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
&
OUTAGE ANALYSES
Twitter Outage Analysis: March
28, 2022
| April 15, 2022 | 14 min read
ROUTING SECURITY INCIDENTS
For 12 Hours, Was Part of Apple
Engineering’s Network Hijacked
by Russia’s Rostelecom?
By Aftab Siddiqui * 27 Jul 2022
Long History of BGP Routing Hijacks...
Russian telco hijacks internet traffic for
Google, AWS, Cloudflare, and others
Rostelecom involved in BGP hijacking incident this week
impacting more than 200 CDNs and cloud providers.
Written by Catalin Cimpanu, Contributor
April 5, 2020 at 2:53 p.m. PT
Cloudflare blames recent outage on BGP hijacking incident
By Bill Toulas
CLOUDFLARE
to
```

## Slide 6

BGP Route Announcement

#BHAS @BlackHatEvents

## Slide 7

## **Forwarding Neighboring Announcement**

#BHAS @BlackHatEvents

## Slide 8

BGP Prefix Hijack

#BHAS @BlackHatEvents

## Slide 9

BGP Prefix Hijack

#BHAS @BlackHatEvents

## Slide 10

# RPKI Resource Public Key Infrastructure

#BHAS @BlackHatEvents

## Slide 11

**RPKI: Cryptographic Objects in** **_Publication Points_**

#BHAS @BlackHatEvents

## Slide 12

**RPKI: Objects Collected by** **_Relying Party_**

#BHAS @BlackHatEvents

## Slide 13

**RPKI: Validated Objects Sent to Router**

#BHAS @BlackHatEvents

## Slide 14

**RPKI:** **_Validated ROA Payloads (VRPs)_**

#BHAS @BlackHatEvents


> Recovered by OCR — confidence 82/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
blackhat ee. RPKI: Validated ROA Paylogds (VRPs)
Publication Point Repository Tree
```

## Slide 15

**RPKI: VRPs to Verify BGP Announcements**

#BHAS @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
blackhat Ay
1.2.3.0/24:
1.2.3.0/24: AS2, AS1
Publication Point Repository Tree
```

## Slide 16

**RPKI - the most promising BGP security add-on**

#BHAS @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Comcast now blocks BGP hijacking attacks and route leaks fey
with RPKI|
Comcast, one of America’s largest broadband providers, has now deployed RPKI on its
network to defend against BGP route hijacks and leaks.
17 Sept 2019
20 May 2021
Capacity Media
Telia Carrier set to install RPKI to global backbone
Telia Carrier has announced that it will be implementing resource public key
infrastructure (RPKI) technology to its global network.
How AWS is helping to secure internet routing
by Fredrik Korsback | on 13 JAN 2021 | in Announcements, Best Practices, Networking & Content Delivery,
Verisign’s Path to RPKI
By Mike Hollyman + 7 Jun 2023
FCC pushes ISPs to fix security flaws in —
Internet routing
Chair: Addressing BGP flaws will "help make our Internet routing more secure."
All Dutch govt networks to use RPK] to prevent BGP
hijacking
JON BRODKIN - 6/6/2024, 11:40 PM
The Dutch government will adopt the RPKI (Resource Public Key Infrastructure)
standard on all its systems before the end of 2024 to upgrade...
9 Apr 2023
```

## Slide 17

**RPKI - the most promising BGP security add-on**

#BHAS @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
blackhat - RPKithe most promising BGP security add-on
a Capacity
Telia Cal
riecer'er FCC takes some action against notorious BGP
‘72291 How's your RPKI-based security plan coming along? Feds want to know
How A @ Jessica Lyons Fri 7 Jun 2024 | 22:29 UTC "
by Fredrik Korsback | on 13 JAN 2021 | in Announcements, Best Practices, Networking & Content Delivery,
By Mike Hollyman + 7 Jun 2023
FCC pushes ISPs to fix security flaws in —
Internet routing
Chair: Addressing BGP flaws will "help make our Internet routing more secure."
All Dutch govt networks to use RPK] to prevent BGP
hijacking
JON BRODKIN - 6/6/2024, 11:40 PM
The Dutch government will adopt the RPKI (Resource Public Key Infrastructure)
standard on all its systems before the end of 2024 to upgrade...
9 Apr 2023
```

## Slide 18

**RPKI - the most promising BGP security add-on**

#BHAS @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
a Capacity
Telia Cal
riecer'er FCC takes some action against notorious BGP
‘72291 How's your RPKI-based security plan coming along? Feds want to know
How A @ Jessica Lyons Fri 7 Jun 2024 | 22:29 UTC
by Fredrik Korsback | on 13 JAN 2021 | in Announcements, Best Practices, Networking & Content Delivery,
FCC] @ Internet Society
Inter US Government Networks Get a Security Boost: White
House Roadmap Tackles Routing Vulnerabilities
Chair: Addi
ue“ The White House's Roadmap to Enhancing Routing Security is an important step
toward strengthening routing security in the United States.
06.09.2024
```

## Slide 19

# ByzRP Operational Shield for RPKI

#BHAS @BlackHatEvents

## Slide 20

Malicious Publication Points Crashing & Stalling Attacks

#BHAS @BlackHatEvents

## Slide 21

## **Objects Stored in Publication Points, Validated by Relying Party**

#BHAS @BlackHatEvents

## Slide 22

Stalling Attacks

rpki-byzrp-2

#BHAS @BlackHatEvents

## Slide 23

Stalling Attacks

rpki-byzrp-2

**https://www.blackhat.com/us22/briefings/schedule/#stallorisrpki-downgrade-attack-27348**

#BHAS @BlackHatEvents

## Slide 24

DoS Attacks

#BHAS @BlackHatEvents

## Slide 25

DoS Attacks

**https://www.blackhat.com/us24/briefings/schedule/index.html#c rashing-the-party-vulnerabilities-inrpki-validation-40443**

#BHAS @BlackHatEvents

## Slide 26

**ByzRP: Watchdog**

#BHAS @BlackHatEvents

## Slide 27

**ByzRP: Watchdog**

#BHAS @BlackHatEvents

## Slide 28

**ByzRP: Watchdog**

#BHAS @BlackHatEvents

## Slide 29

**ByzRP: No Operational Downtime**

**repo starts crashing RPs**

#BHAS @BlackHatEvents

## Slide 30

Instability Network & Operational Errors

#BHAS @BlackHatEvents

## Slide 31

#BHAS @BlackHatEvents

## Slide 32

A Crowded Ecosystem

#BHAS @BlackHatEvents

## Slide 33

## **Inconsistent Object Sets Due to Instabilities**

#BHAS @BlackHatEvents

## Slide 34

**ByzRP: Robust Global Consensus**

#BHAS @BlackHatEvents

## Slide 35

**ByzRP: Robust Global Consensus**

#BHAS @BlackHatEvents

## Slide 36

**ByzRP: Jitter & Failure Resistant Output**

repository jitter

transient failures

#BHAS @BlackHatEvents


> Recovered by OCR — confidence 84/100 on the text kept, 60/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ant Output
500000 +
N SZ
repository jitter
local MEM consensus
537000 -
536000 -
=
transient failures ——”
consensus
RP
T
```

## Slide 37

**ByzRP: Fast Consensus Aggregation**

#BHAS @BlackHatEvents


> Recovered by OCR — confidence 77/100 on the text kept, 56/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
blackhat
400000 +
Mae local
200000 - union
3 nodes
400000 +
Ma local
S? ,.© 1.9079 {49 149 1.49 1.49
13 nodes
```

## Slide 38

**ByzRP: RP-as-a-Service**

#BHAS @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
should everyone run a ByZRP network?
```

## Slide 39

**ByzRP: RP-as-a-Service**

#BHAS @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
should everyone run a ByzZRP network?
not really...
```

## Slide 40

**ByzRP: RP-as-a-Service**

#BHAS @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ASIA 2025 7 7
should everyone run a ByzRP network?
not really...
better: a handful of operators run ByzRP
nodes in a global RP-as-a-Service network
```

## Slide 41

ByzRP: RP-as-a-Service

#BHAS @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
should everyone run a ByZRP network?
not really...
better: a handful of operators run ByzRP
nodes in a global RP-as-a-Service network
1. not everyone needs to run their own RP
2. reduced traffic to PPs
3. allows more frequent updates
```

## Slide 42

**ByzRP: Traffic Reduction Through RP-as-a-Service**

#BHAS @BlackHatEvents

## Slide 43

**ByzRP: Traffic Reduction Through RP-as-a-Service**

#BHAS @BlackHatEvents


> Recovered by OCR — confidence 80/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Standard RPKI
64x
GE 3156x 3156x
| 562MB, |_| 6.2MB -
```

## Slide 44

**ByzRP: Traffic Reduction Through RP-as-a-Service**

#BHAS @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Standard RPKI ByzRP
64x
S | 562MB 6.2MB, <>
5 RP
O
64x
2 | 1.2GB 13MB, <>
5 RP
LL
```

## Slide 45

## **ByzRP: Traffic Reduction Through RP-as-a-Service**

#BHAS @BlackHatEvents


> Recovered by OCR — confidence 81/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Standard RPKI
64x
S | 562MB 6.2MB, <>
5 RP
64x
© EE 128000x 428000x
2 | 1.2GB 13MB <P>
iD RP
```

## Slide 46

**ByzRP: Outsourcing Security**

#BHAS @BlackHatEvents

## Slide 47

**ByzRP: Outsourcing Security**

#BHAS @BlackHatEvents


> Recovered by OCR — confidence 83/100 on the text kept, 56/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ASIA 2025 _ =a oy ne Security
but RPs are security-critical!
how can we trust RPaaS?
```

## Slide 48

ByzRP: Outsourcing Security

#BHAS @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 65/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ASIA 2025 me 4 Xen ne Security
but RPs are security-critical!
how can we trust RPaaS?
1. distribute nodes across distinct entities
2. trust in the majority
```

## Slide 49

Consensus With Byzantine Fault Tolerance

#BHAS @BlackHatEvents

## Slide 50

ByzRP: Consensus

### **_N_ =3** nodes

#BHAS @BlackHatEvents

## Slide 51

**ByzRP: Consensus**

Fully-connected **permissioned** network through **mutual TLS**

#BHAS @BlackHatEvents

## Slide 52

**ByzRP: Consensus**

Each node **asynchronously polls** its peers for their current object set

#BHAS @BlackHatEvents

## Slide 53

**ByzRP: Consensus**

Each node can **independently** produce the **same, deterministic** output by intersecting object sets

#BHAS @BlackHatEvents

## Slide 54

**ByzRP: Consensus**

Secure against **_f_ byzantine faults** based on voting threshold

#BHAS @BlackHatEvents

## Slide 55

**ByzRP: Consensus**

#BHAS @BlackHatEvents

## Slide 56

**ByzRP: Consensus**

**1-out-of-3 = union**

resist **censorship / errors**

#BHAS @BlackHatEvents

## Slide 57

**ByzRP: Consensus**

**2-out-of-3 = majority**

#BHAS @BlackHatEvents

## Slide 58

**ByzRP: Consensus**

**3-out-of-3 = unanimity = intersection**

resist **poisoning**

#BHAS @BlackHatEvents

## Slide 59

**ByzRP: Consensus Poisoning**

**3-out-of-3 = unanimity = intersection**

resist **poisoning**

#BHAS @BlackHatEvents

## Slide 60

**ByzRP: Consensus Poisoning**

**3-out-of-3 = unanimity = intersection**

resist **poisoning**

#BHAS @BlackHatEvents

## Slide 61

**ByzRP: Consensus Poisoning**

**3-out-of-3 = unanimity = intersection**

resist **poisoning**

#BHAS @BlackHatEvents

## Slide 62

**ByzRP: Consensus**

**3-out-of-5 = majority**

faster **inclusion**

faster **removal**

#BHAS @BlackHatEvents

## Slide 63

**ByzRP: Consensus for Watchdog Skiplist Entries**

#BHAS @BlackHatEvents

## Slide 64

Summary

#BHAS @BlackHatEvents


> Recovered by OCR — confidence 84/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
e stalling protection
e crashing protection
e adaptive skiplisting
```

## Slide 65

Summary

- **distribution of trust**

#BHAS @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
¢ stalling protection
e crashing protection
¢« adaptive skiplisting
parallel processing
asynchronous consensus
byzantine fault tolerance
distribution of trust
```

## Slide 66

Summary

- **distribution of trust**

#BHAS @BlackHatEvents


> Recovered by OCR — confidence 84/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
iA
e stalling protection ¢ parallel processing e reduced network traffic
e crashing protection e asynchronous consensus e higher update frequency
¢« adaptive skiplisting e byzantine fault tolerance e easier RPKI adoption
distribution of trust
```

## Slide 67

Summary

- **distribution of trust**

#BHAS @BlackHatEvents


> Recovered by OCR — confidence 85/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
¢ stalling protection ¢ parallel processing e reduced network traffic
e crashing protection e asynchronous consensus e higher update frequency
¢« adaptive skiplisting e byzantine fault tolerance e easier RPKI adoption
distribution of trust
```

## Slide 68

**jens.friess@athene-center.de**

**donika.mirdita@athene-center.de**

**github.com/Cyberbruecke/byzrp doi/pdf/10.1145/3658644.3690368**

#BHAS @BlackHatEvents
