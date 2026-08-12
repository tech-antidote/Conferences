---
title: "Crashing the Party Vulnerabilities in RPKI Validation"
speakers: ["Niklas Vogel", "Donika Mirdita", "Haya Schulmann", "Michael Waidner"]
conference: "Black Hat"
conference_full: "Black Hat USA 2024"
edition: "USA"
year: 2024
source_pdf: "Black Hat USA 2024 slides/Niklas Vogel & Donika Mirdita & Haya Schulmann & Michael Waidner_Crashing the Party Vulnerabilities in RPKI Validation.pdf"
pages: 89
sha256: "1bebad48f89f43ce23641b94ca4f5fe0f8595b9a93f5985bed4101fd0207116c"
text_chars: 18889
ocr_pages: 17
has_ocr: true
redacted_secrets: 0
ocr_confidence: 87.6
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:38:53Z"
---
# Crashing the Party Vulnerabilities in RPKI Validation

**Speakers:** Niklas Vogel, Donika Mirdita, Haya Schulmann, Michael Waidner  
**Conference:** Black Hat USA 2024  
**Source:** `Black Hat USA 2024 slides/Niklas Vogel & Donika Mirdita & Haya Schulmann & Michael Waidner_Crashing the Party Vulnerabilities in RPKI Validation.pdf` (89 pages)


## Slide 1

# Crashing the Party: Vulnerabilities in RPKI Validation **<u>Donika Mirdita</u>** , **<u>Niklas Vogel</u>** , Haya Schulmann, Michael Waidner

#BHUSA @BlackHatEvents

## Slide 2

### Outline

###### ❖ **Resource Public Key Infrastructure (RPKI)**

- ✓ A niche new protocol

- ✓ & why it matters

- ❖ **Systemic Analysis of RPKI Software**

- ✓ Introducing a bespoke fuzzing mechanism

- ✓ & how it works

- ❖ **Analysis Results**

- ✓ What they mean

- ✓ & consequences

- ❖ **Disclosure Process**

#BHUSA @BlackHatEvents

## Slide 3

### BGP as Achille's Heel

#BHUSA @BlackHatEvents

## Slide 4

### BGP as Achille's Heel

_Notes from the IETF Cafeteria, 1989_

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 78/100 on the text kept, 46/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BGP as Achille's Heel
lowg heed @ cisco.com
/
block fen th R hyfes
open ~ |
down ~ 2
H- tale - @
| O - nowe
List hop gakwe 4 by fos
cba bee
Notes from the
IETF Cafeteria, 1989
```

## Slide 5

### BGP as Achille's Heel

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
black hat |
USA 2024 ,
BGP as Achille's Heel
Cloudflare blames recent outage on BGP hijacking incident
ROUTING SECURITY INCIDENTS
By Bill Toulas July 5, 2024 02:41 PM 1
For 12 Hours, Was Part of Apple
Engineering’s Network Hijacked
by Russia’s Rostelecom?
By Aftab Siddiqui * 27 Jul 2022
aaa OUTAGE ANALYSES
CLOUDFLARE
Russian telco hijacks internet traffic for Twitter Outage Analysis: March
Google, AWS, Cloudflare, and others 28, 2022
| April 15, 2022 | 14 min read
Rostelecom involved in BGP hijacking incident this week
impacting more than 200 CDNs and cloud providers. &® & in o
Written by Catalin Cimpanu, Contributor
q April 5, 2020 at 2:53 p.m. PT
```

## Slide 6

### The RPKI Protocol

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 96/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
The RPKI Protocol
[REC Home] [TEXT|PDF|HTML] [Tracker] [IPR] [Errata] [Info page]
INFORMATIONAL
Errata Exist
Internet Engineering Task Force (IETF) M. Lepinski
Request for Comments: 6480 S. Kent
Category: Informational BBN Technologies
ISSN: 2070-1721 February 2012
An Infrastructure to Support Secure Internet Routing
Abstract
This document describes an architecture for an infrastructure to
support improved security of Internet routing. The foundation of
this architecture is a Resource Public Key Infrastructure (RPKI) that
represents the allocation hierarchy of IP address space and
Autonomous System (AS) numbers; and a distributed repository system
for storing and disseminating the data objects that comprise the
RPKI, as well as other signed objects necessary for improved routing
security. As an initial application of this architecture, the
document describes how a legitimate holder of IP address space can
explicitly and verifiably authorize one or more ASes to originate
routes to that address space. Such verifiable authorizations could
be used, for example, to more securely construct BGP route filters.
Status of This Memo
This document is not an Internet Standards Track specification; it is
published for informational purposes.
This document is a product of the Internet Engineering Task Force
(IETF). It represents the consensus of the IETF community. It has
received public review and has been approved for publication by the
Internet Engineering Steering Group (IESG). Not all documents
approved by the IESG are a candidate for any level of Internet
Standard; see Section 2 of RFC 5741.
Information about the current status of this document, any errata,
and how to provide feedback on it may be obtained at
```

## Slide 7

### The RPKI Protocol

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Q
black hat
The RPKI Protocol
. . . . Comcast now blocks BGP hijacking attacks and route leaks —
How AWS is helping to secure internet routing =
with RPKI
by Fredrik Korsback | on 13 JAN 2021 | in Announcements, Best Practices, Networking & Content Delivery,
7 7 Comcast, one of America's largest broadband providers, has now deployed RPKI on its
network to defend against BGP route hijacks and leaks.
20 May 2021
Some of the larger service provider networks have implemented RPKI Origin Validation in the last year. This can be seen
in the preceding chart (figure 5) by looking at the reduction of BGP prefixes with an Invalid RPKI state accepted by their
networks. Telia Carrier deployed in February, and many other large operators followed suit afterwards. The number of
@ BleepingComputer
All Dutch govt networks to use RPKI to prevent BGP P a
The Dutch government will adopt the RPKI (Resource Public Key Infrastructure)
Verisign’s Path to RPKI
standard on all its systems before the end of 2024 to upgrade.
By Mike Hollyman + 7 Jun 2023
9 Apr 2023
case study RPKI
|_| Capacity Media
Telia Carrier set to install RPKI to global backbone
Telia Carrier has announced that it will be implementing resource public key
infrastructure (RPKI) technology to its global network.
17 Sept 2019
```

## Slide 8

### The RPKI Protocol

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Q
black hat
The RPKI Protocol
How AWS Harry Coker: Federal Agencies Advance attacks and route leaks
by Fredrik Korsba
ers, has now deployed RPKI on its
Resource Public Key Infrastructure ra
Adoption
usy20 2029 mines ECC pushes ISPs to fix security flaws in
by Jane Edwards
W_Bieringcompue Internet routing ix
All Dutch govt net ,
hijacking Chair: Addressing BGP flaws will "help make our Internet routing more secure." Iti ng
The Dutch government wi N - 6/6/2024, 11:40 PM
standard on all its system
9 Apr 2023 . .
rent crooks, spies hijacking victims’
Harry Coker
National Cyber Director
Office of the National Cyber Director
|_| Capacity Media
ue 31 Mar 2020 12:00 UTC
Telia Carrier se
Telia Carrier has ann
infrastructure (RPKI)
17 Sept 2019
```

## Slide 9

### BGP Security with RPKI

#BHUSA @BlackHatEvents

## Slide 10

### BGP Security with RPKI

**RPKI Repositories**

#BHUSA @BlackHatEvents

## Slide 11

### BGP Security with RPKI

ROA
Prefix - ASN
---

**RPKI Repositories**

#BHUSA @BlackHatEvents

## Slide 12

### BGP Security with RPKI

ROA
Prefix - ASN
---
R elying
P arty

RPKI Repositories

#BHUSA @BlackHatEvents

## Slide 13

### BGP Security with RPKI

ROA
Prefix - ASN
---
RPKI-to-Router
R elying
P arty

RPKI Repositories

#BHUSA @BlackHatEvents

## Slide 14

### BGP Security with RPKI

ROA
Prefix - ASN
---
RPKI-to-Router
R elying
P arty

RPKI Repositories

#BHUSA @BlackHatEvents

## Slide 15

### BGP Security with RPKI

ROA
Prefix - ASN
---
RPKI-to-Router
R elying
P arty

RPKI Repositories

#BHUSA @BlackHatEvents

## Slide 16

### BGP Security with RPKI

ROA
Prefix - ASN
---
RPKI-to-Router
R elying
P arty

AS212795

RPKI Repositories

#BHUSA @BlackHatEvents

## Slide 17

### BGP Security with RPKI

ROA
Prefix - ASN
---
RPKI-to-Router
R elying
P arty

AS212795

RPKI Repositories

#BHUSA @BlackHatEvents

## Slide 18

### BGP Security with RPKI

ROA
Prefix - ASN
---
RPKI-to-Router
R elying
P arty

AS666

RPKI Repositories

#BHUSA @BlackHatEvents

## Slide 19

### BGP Security with RPKI

ROA
Prefix - ASN
---
RPKI-to-Router
R elying
P arty

AS666

RPKI Repositories

#BHUSA @BlackHatEvents

## Slide 20

### Why is DoS-ing RPs a big deal?

RPKI-to-Router

#BHUSA @BlackHatEvents

## Slide 21

### Why is DoS-ing RPs a big deal?

RPKI-to-Router

#BHUSA @BlackHatEvents

## Slide 22

### Why is DoS-ing RPs a big deal?

AS666

#BHUSA @BlackHatEvents

## Slide 23

### So we decided to tinker with the protocol...

#BHUSA @BlackHatEvents

## Slide 24

### So we decided to tinker with the protocol...

###### ➢ **Relaying Party Impl. 1: crash when objects malformed**

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
iC (MESTHE CYBER > Relaying Party Impl. 1: crash when objects malformed
1975 "Fatal: failed to write file {}: {}", path.display(), err
1976 i
197 Failed
1
978 })
```

## Slide 25

### So we decided to tinker with the protocol...

###### ➢ **Relaying Party Impl. 1: crash when objects malformed**

- ➢ **Relying Party Impl. 2: crash when index out-of-bounds**

#BHUSA @BlackHatEvents

## Slide 26

### So we decided to tinker with the protocol...

- ➢ **Relaying Party Impl. 1: crash when objects malformed**

**=> 84.9% of global Relying Party deployments affected by low-cost lowburden RPKI Downgrade Attacks** ➢ **Relying Party Impl. 2: crash when index out-of-bounds**

#BHUSA @BlackHatEvents

## Slide 27

### Towards a systematic approach

- ➢ RP is interesting target, but how do we test it?

- ➢ Fuzzing is a promising solution for systematic testing

- ➢ Simple idea:

   - Run many random inputs against RP

   - Find vulnerabilities

   - **Profit** ( _optional_ )

#BHUSA @BlackHatEvents

## Slide 28

### Towards a systematic approach

- ➢ RP is interesting target, but how do we test it?

- ➢ Fuzzing is a promising solution for systematic testing

- ➢ Simple idea:

   - Run many random inputs against RP - Find vulnerabilities - **Profit** ( _optional_ )

**If it's so easy, why has nobody done it.... ????**

#BHUSA @BlackHatEvents

## Slide 29

### Our simple Plan

- ➢ Use existing Fuzzer, generate inputs, find crashes

- ➢ Keep trying until we find a vulnerability

#BHUSA @BlackHatEvents

## Slide 30

### Our simple Plan

- ➢ Use existing Fuzzer, generate inputs, find crashes

➢ Keep trying until we find a vulnerability

#BHUSA @BlackHatEvents

## Slide 31

### Our simple Plan

- ➢ Use existing Fuzzer, generate inputs, find crashes

- ➢ Keep trying until we find a vulnerability

#BHUSA @BlackHatEvents

## Slide 32

### Our simple Plan

- ➢ Use existing Fuzzer, generate inputs, find crashes

➢ Keep trying until we find a vulnerability

#BHUSA @BlackHatEvents

## Slide 33

### Our simple Plan

- ➢ Use existing Fuzzer, generate inputs, find crashes

➢ Keep trying until we find a vulnerability

#BHUSA @BlackHatEvents

## Slide 34

### Our simple Plan

- ➢ Use existing Fuzzer, generate inputs, find crashes

- ➢ Keep trying until we find a vulnerability

#BHUSA @BlackHatEvents

## Slide 35

### Our simple Plan

- ➢ Use existing Fuzzer, generate inputs, find crashes

➢ Keep trying until we find a vulnerability

#BHUSA @BlackHatEvents

## Slide 36

### Our simple Plan

- ➢ Use existing Fuzzer, generate inputs, find crashes

➢ Keep trying until we find a vulnerability

#BHUSA @BlackHatEvents

## Slide 37

### Our simple Plan

- ➢ Use existing Fuzzer, generate inputs, find crashes

- ➢ Keep trying until we find a vulnerability

#BHUSA @BlackHatEvents

## Slide 38

### Our simple Plan

- ➢ Use existing Fuzzer, generate inputs, find crashes

➢ Keep trying until we find a vulnerability

#BHUSA @BlackHatEvents

## Slide 39

### Our simple Plan

- ➢ Use existing Fuzzer, generate inputs, find crashes

➢ Keep trying until we find a vulnerability

#BHUSA @BlackHatEvents

## Slide 40

### Our simple Plan

- ➢ Use existing Fuzzer, generate inputs, find crashes

- ➢ Keep trying until we find a vulnerability

#BHUSA @BlackHatEvents

## Slide 41

### Our simple Plan

- ➢ Use existing Fuzzer, generate inputs, find crashes

➢ Keep trying until we find a vulnerability

#BHUSA @BlackHatEvents

## Slide 42

### Our simple Plan

➢ Use existing Fuzzer, generate inputs, find crashes

➢ Keep trying until we find a vulnerability

#BHUSA @BlackHatEvents

## Slide 43

### The complex Reality

- ➢ RPs require very complex inputs

- ➢ We still tried to use existing Fuzzers...

#BHUSA @BlackHatEvents

## Slide 44

### The complex Reality

- ➢ RPs require very complex inputs

- ➢ We still tried to use existing Fuzzers...

#BHUSA @BlackHatEvents

## Slide 45

### The complex Reality

- ➢ RPs require very complex inputs

- ➢ We still tried to use existing Fuzzers...

#BHUSA @BlackHatEvents

## Slide 46

### The complex Reality

- ➢ RPs require very complex inputs

- ➢ We still tried to use existing Fuzzers...

#BHUSA @BlackHatEvents

## Slide 47

### The complex Reality

- ➢ RPs require very complex inputs

- ➢ We still tried to use existing Fuzzers...

#BHUSA @BlackHatEvents

## Slide 48

### The complex Reality

- ➢ RPs require very complex inputs

- ➢ We still tried to use existing Fuzzers...

#BHUSA @BlackHatEvents

## Slide 49

### The complex Reality

- ➢ RPs require very complex inputs

- ➢ We still tried to use existing Fuzzers...

#BHUSA @BlackHatEvents

## Slide 50

### Why is this so difficult

- ➢ RPKI objects are complex (ASN.1 / X.509 formats)

➢ Fuzzers struggle with complex objects

#BHUSA @BlackHatEvents

## Slide 51

### Why is this so difficult

➢ RPKI objects are complex (ASN.1 / X.509 formats)

➢ Fuzzers struggle with complex objects

#BHUSA @BlackHatEvents

## Slide 52

### It gets worse...

###### ➢ RPKI uses...

#BHUSA @BlackHatEvents

## Slide 53

### It gets worse...

###### ➢ RPKI uses...

## **CRYPTOGRAPHY**

#BHUSA @BlackHatEvents

## Slide 54

### It gets worse...

- ➢ RPKI uses cryptography

➢ Fuzzers struggle with cryptography

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
> RPKI uses cryptography
> Fuzzers struggle with cryptography
CA Certificate
SignerName
Validity
SubjectName
SubjectKey
IssuerRsync
Digest
CertSignature
DigestSignature
7—| CA Certificate
SignerName
Validity
SubjectName
SubjectKey
IssuerRsync
Digest
CertSignature
DigestSignature
It gets worse...
Manifest
HashList
SignerName
Validity
SubjectName
SubjectKey
Digest
CertSignature
DigestSignature
```

## Slide 55

### It gets worse...

- ➢ RPKI uses cryptography

➢ Fuzzers struggle with cryptography

#BHUSA @BlackHatEvents

## Slide 56

### Only one solution...

#BHUSA @BlackHatEvents

## Slide 57

### Only one solution...

#BHUSA @BlackHatEvents

## Slide 58

### Building yet another Fuzzer

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 78/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Building yet another Fuzzer
RPs
CURE
Object Setting fields A Exposing
J : and signing BORGES Objects to RPs
Generation
```

## Slide 59

### Building yet another Fuzzer

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 78/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Building yet another Fuzzer
RPs
CURE
Object Setting fields A Exposing
J : and signing BORGES Objects to RPs
Generation
```

## Slide 60

Object Generation in CURE

### Object Generation

###### **1. Random Byte Mutation**

**i. feed the randomizer a set of valid objects ii. splice files & generate random mutations iii. targets programming, parsing & schematic errors**

#BHUSA @BlackHatEvents

## Slide 61

Object Generation in CURE

### Object Generation

###### **1. Random Byte Mutation**

###### **2. Structure Aware Mutation**

ASN.1

ASN.1

- **i. feed the randomizer a set of valid objects ii. splice files & generate random mutations iii. targets programming, parsing & schematic errors**

- **i. schema-abiding, correctly encoded objects ii. manipulate content of fields iii. targets processing and validation logic**

#BHUSA @BlackHatEvents

## Slide 62

Object Generation in CURE

### Object Generation

###### **1. Random Byte Mutation**

###### **2. Structure Aware Mutation**

ASN.1

ASN.1

- **i. feed the randomizer a set of valid objects ii. splice files & generate random mutations iii. targets programming, parsing & schematic errors**

- **i. schema-abiding, correctly encoded objects ii. manipulate content of fields iii. targets processing and validation logic**

###### **Found Bugs: 7**

###### **Found Bugs: 11**

#BHUSA @BlackHatEvents

## Slide 63

### Repositorify Module

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 79/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Repositorify Module
RPs
CURE
Object Setting fields ws Exposing
J : and signing BORGES Objects to RPs
Generation
```

## Slide 64

### Repositorify Module

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 82/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Repositorify Module
RPs
CURE
Exposing
Objects to RPs
O bj ect Set ng felds Repositorify
: and signing
Generation
```

## Slide 65

### Repositorify Module

- ➢ Create valid RPKI repository

- ➢ Replace fields in objects E.g. compute signatures

- ➢ Insert Test-Objects into repository

#BHUSA @BlackHatEvents

## Slide 66

### Repositorify Module

- Create valid RPKI repository

- Replace fields in objects E.g. compute signatures

- Insert Test-Objects into repository

##### **Let's find vulnerabilities!!**

#BHUSA @BlackHatEvents

## Slide 67

### Relying Party Distributions

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Q
black hat
Relying Party Distributions
Other
RIPE NCC
Fort
Relying Party
rpki-client
Routinator
% of relying party distributions
```

## Slide 68

### Summary of Results

We found
issues on
3 out of 4
maintained RPs

18 total
vulnerabilities
&
5 CVEs

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Summary of Results
We found
issues on
maintained RPs
Other
RIPE NCC
Fort
Relying Party
OctoRPKI 18 total
rpki-client vulnerabilities
&
Routinator
5 CVEs
% of relying party distributions
```

## Slide 69

#### Vulnerability Type: Path Traversal

###### ➢ **Vulnerable Software:** **_<u>Routinator</u>_**

➢ **Critical: 9.3 (CVE-2023-39916)**

#BHUSA @BlackHatEvents

## Slide 70

#### Vulnerability Type: Path Traversal

###### ➢ **Vulnerable Software:** **_<u>Routinator</u>_**

- ➢ **Critical: 9.3 (CVE-2023-39916)**

- ➢ **Exploit:**

   **1. place malicious file anywhere on disk**

   **2. poison the RPKI data by adding a malicious root certificate pointer**

#BHUSA @BlackHatEvents

## Slide 71

#### Vulnerability Type: DoS

###### ➢ **Adversary can create objects of any format**

#BHUSA @BlackHatEvents

## Slide 72

#### Vulnerability Type: DoS

###### ➢ **Adversary can create objects of any format**

- ➢ **Vulnerable Software:**

   - **_<u>Routinator:</u>_ Parsing of ASN.1 Data**

   - `o` **_<u>OctoRPKI:</u>_ Processing of Object Fields**

   - **_<u>Fort:</u>_ Processing of RTR Requests**

- ➢ **Exploit:**

###### **Adversary forces RPs in perpetual fail-and-restart mode**

#BHUSA @BlackHatEvents

## Slide 73

### Internet Evaluations (Then)

#BHUSA @BlackHatEvents

## Slide 74

### Internet Evaluations (Then)

#BHUSA @BlackHatEvents

## Slide 75

### Internet Evaluations (Now)

Secure RPs

#BHUSA @BlackHatEvents

## Slide 76

### Results: Global Inconsistencies

#BHUSA @BlackHatEvents

## Slide 77

### Results: Global Inconsistencies

how the RFC how Routinator How OctoRPKI How Fort explained it understood it Understood it Understood it

#BHUSA @BlackHatEvents

## Slide 78

### Results: Global Inconsistencies

➢ **Post-processing ROA Payload:**

**_Routinator:_** 441,770 | **_Fort:_** 435,002 **_OctoRPKI:_** 434,074 | **_rpki-client:_** 441,777

#BHUSA @BlackHatEvents

## Slide 79

### Results: Global Inconsistencies

➢ **Post-processing ROA Payload:**

**_Routinator:_** 441,770 | **_Fort:_** 435,002 **_OctoRPKI:_** 434,074 | **_rpki-client:_** 441,777

➢ **Processing inconsistencies in the real-world:** _6405 unprotected Amazon prefixes in_ **_one implementation_** _due to the presence of OrganisationName header in certificates_

#BHUSA @BlackHatEvents

## Slide 80

### Disclosures

➢ Of course, we responsibly disclosed all vulnerabilities

➢ We sent out E-Mail to the vendors and waited for replies

**_Sent: Jul 19th '23 - 20:25 Sent: Jul 20th '23 - 11:01 Sent: Jul 20th '23 - 11:56_**

**The experience differed significantly between vendors...**

#BHUSA @BlackHatEvents

## Slide 81

### Disclosure – Vendor 1

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Disclosure — Vendor 1
Disclosure E-mail
Email Ack. Patches
2h 5d
```

## Slide 82

### Disclosure – Vendor 1

That was nice!

#BHUSA @BlackHatEvents

## Slide 83

### Disclosure – Vendor 2

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Bug does
not exist??
Email Ack. 2.Email Patches
4d 68d 77d
```

## Slide 84

### Disclosure – Vendor 2

**Learning: Updates might close the vector to a vulnerability w/o fixing the bug**

#BHUSA @BlackHatEvents

## Slide 85

### Disclosure – Vendor 3

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Disclosure — Vendor 3
Disclosure E-mail
Disclosure E-mail
We will publish
tomorrow
*silently
archives repo*
Email 2. Email 3. Email 4. Email Archived
33d 65d 98d 278d
```

## Slide 86

### Disclosure – Vendor 3

#BHUSA @BlackHatEvents

## Slide 87

### Disclosure – Vendor 3

## **Learning: If you don't get a reply, keep trying... Deprecation is better than nothing**

#BHUSA @BlackHatEvents

## Slide 88

### Lessons Learned

➢ **Takeaway 1:** RPKI is a core internet security protocol! The software maturity is (partially) not production ready.

➢ **Takeaway 2:** 41.2% of RPs on the internet are still vulnerable! Operators <u>must</u> be more reactive and patch their software.

➢ **Takeaway 3:** Fuzzing crypto is hard! We need more tools to efficiently fuzz cryptographic protocols.

#BHUSA @BlackHatEvents

## Slide 89

**Thank you!** donika.mirdita@athene-center.de niklas.vogel@athene-center.de

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Thank you!
donika.mirdita@athene-center.de
niklas.vogel@athene-center.de
e National Research Center
e for Applied Cybersecurity
```
