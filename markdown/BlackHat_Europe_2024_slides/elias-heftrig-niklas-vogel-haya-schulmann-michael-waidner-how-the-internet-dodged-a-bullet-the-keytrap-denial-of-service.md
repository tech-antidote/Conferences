---
title: "How the Internet Dodged a Bullet The KeyTrap Denial-of-Service Attacks against DNSSEC"
speakers: ["Elias Heftrig", "Niklas Vogel", "Haya Schulmann", "Michael Waidner"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2024"
edition: "Europe"
year: 2024
source_pdf: "BlackHat_Europe_2024_slides/Elias Heftrig & Niklas Vogel & Haya Schulmann & Michael Waidner_How the Internet Dodged a Bullet The KeyTrap Denial-of-Service Attacks against DNSSEC.pdf"
pages: 73
sha256: "55a92d82a228e9634b6e8c11ad65e549724b894022f45a2570ae4be4697c6e96"
text_chars: 21334
ocr_pages: 14
has_ocr: true
redacted_secrets: 0
ocr_confidence: 91.7
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:57:11Z"
---
# How the Internet Dodged a Bullet The KeyTrap Denial-of-Service Attacks against DNSSEC

**Speakers:** Elias Heftrig, Niklas Vogel, Haya Schulmann, Michael Waidner  
**Conference:** Black Hat Europe 2024  
**Source:** `BlackHat_Europe_2024_slides/Elias Heftrig & Niklas Vogel & Haya Schulmann & Michael Waidner_How the Internet Dodged a Bullet The KeyTrap Denial-of-Service Attacks against DNSSEC.pdf` (73 pages)


## Slide 1

How the Internet Dodged a Bullet: The KeyTrap Denial-of-Service Attacks against DNSSEC Speaker(s): **<u>Elias Heftrig, Niklas Vogel</u>** Contributors:

**Haya Schulmann, Michael Waidner**

#BHEU @BlackHatEvents

## Slide 2

# **Refresher: DNS and DNSSEC**

#BHEU @BlackHatEvents

## Slide 3

## Why is it always DNS?

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
black hat
Why its it always DNS?
DDoS attack that disrupted internet was
largest of its kind in history, experts say
Dyn, the victim of last week’s denial of service attack, said it
was orchestrated using a weapon called the Mirai botnet as
the ‘primary source of malicious attack’
DNS poisoning slams web traffic from millions
in China into the wrong hole
ISP blames unspecified attack for morning outage
Understanding how Facebook
disappeared from the Internet
Home News Securi ity Akamai DNS global outage takes down major websites, online services
Akamai DNS global outage takes down major websites, online services
By Sergiu Gatlan July 22, 2021 12:39 PM
2
Salesforce cloud services go down
worldwide
Caused by DNS issue.
```

## Slide 4

## Why is it always DNS?

HTTPS VPN Signal
FTP
NTP ...
SMTP
VoIP
DNS

Information Classification: General

#BHEU @BlackHatEvents

## Slide 5

## DNS Resolution

3
.
2
www.bank.ing. IN A? 4
1
www.bank.ing. IN A 1.2.3.4 8 bank.ing. IN NS ns.bank.ing.
5
ing.
6
7
bank.ing.

Information Classification: General

#BHEU @BlackHatEvents

## Slide 6

## DNS Poisoning

.

www.bank.ing. IN A?
www.bank.ing. IN A 6.6.6.6 ing.
www.bank.ing. IN A 6.6.6.6
bank.ing.
#BHEU
➢ Attack on DNS Record Authenticity

Information Classification: General

#BHEU @BlackHatEvents

## Slide 7

## DNSSEC to the Rescue!

.

www.bank.ing. IN A?
www.bank.ing. IN A 1.2.3.4 ing.
www.bank.ing. IN A 6.6.6.6
bank.ing.
X

➢ Attack prevented

Information Classification: General

#BHEU @BlackHatEvents

## Slide 8

## DNSSEC Adoption on the Internet

###### Adoption in domains is dragging

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
pifekhat DNSSEC Adoption on the Internet
TLDs Top 1M
Msigned Munsigned Msigned mMunsigned
Adoption in domains is dragging
```

## Slide 9

## DNSSEC Adoption on the Internet

Better adoption in Resolvers

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Open Resolvers Web Clients
B not validating @ not validating
Better adoption in Resolvers
```

## Slide 10

## How DNSSEC Validation Works

~$ dig www.ietf.org -t A +dnssec

**_What is the IP Address of www.ietf.org?_**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 11

## How DNSSEC Validation Works

**_What is the IP Address of_** ~$ dig www.ietf.org -t A +dnssec **_www.ietf.org?_** ;; ANSWER SECTION: www.ietf.org.           300     IN      A       104.16.45.99 www.ietf.org.           300     IN      A       104.16.44.99 www.ietf.org.           300     IN      RRSIG A 13 3 300 20241211 20241209 ↳ 34505 ietf.org. eSTHK9ql[…]uvSgBA==

Information Classification: General

#BHEU @BlackHatEvents

## Slide 12

## How DNSSEC Validation Works

**_What is the IP Address of_** ~$ dig www.ietf.org -t A +dnssec **_www.ietf.org?_** **<u>How to validate??</u>** ;; ANSWER SECTION: www.ietf.org.           300     IN      A       104.16.45.99 www.ietf.org.           300     IN      A       104.16.44.99 www.ietf.org.           300     IN      RRSIG A 13 3 300 20241211 20241209 ↳ 34505 ietf.org. eSTHK9ql[…]uvSgBA==

Information Classification: General

#BHEU @BlackHatEvents

## Slide 13

## Obtaining Public Keys

~$ dig ietf.org -t DNSKEY +dnssec

###### **_What are the keys for ietf.org?_**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 14

## Obtaining Public Keys

~$ dig ietf.org -t DNSKEY +dnssec

**_What are the keys for ietf.org?_**

###### ;; ANSWER SECTION:

ietf.org.               3600    IN      DNSKEY  257 3 13 mdsswUyr[…]53eKGQ== ietf.org.               3600    IN      DNSKEY  256 3 13 oJMRESz5[…]a2XhSA== ietf.org.               3600    IN      RRSIG   DNSKEY 13 2 3600 20250130 20241130 ↳ 2371 ietf.org. gdCgidVw[…]heIodA==

Information Classification: General

#BHEU @BlackHatEvents

## Slide 15

## Associating Signatures with Keys

**<u>DNSKEY 1 DNSKEY 2</u>**

> **_What are the keys for_** **<u>RRSIG 1</u>** **_ietf.org?_** **<u>RRSIG 1</u>**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 16

## Associating Signatures with Keys

;; ANSWER SECTION:

ietf.org.               3600    IN      DNSKEY  257 3 13 mdsswUyr[…]53eKGQ== ietf.org.               3600    IN      DNSKEY  256 3 13 oJMRESz5[…]a2XhSA== ;; ANSWER SECTION: www.ietf.org.           300     IN      RRSIG A 13 3 300 20241211 20241209 ↳ 34505 ietf.org. eSTHK9ql[…]uvSgBA==

Information Classification: General

#BHEU @BlackHatEvents

## Slide 17

## Associating Signatures with Keys

;; ANSWER SECTION: ietf.org. 3600    IN DNSKEY 257 3 13 mdsswUyr[…]53eKGQ== ietf.org. 3600    IN DNSKEY 256 3 13 oJMRESz5[…]a2XhSA== ;; ANSWER SECTION: www.ietf.org. 300 IN RRSIG A 13 3 300 20241211 20241209 ↳ 34505 ietf.org. eSTHK9ql[…]uvSgBA==

Information Classification: General

#BHEU @BlackHatEvents

## Slide 18

## Associating Signatures with Keys

**DNSKEY 1:** ietf.org | Algo 13 | [KqXX...]

**DNSKEY 2:** ietf.org | Algo 13 | [KkxL...]

**Signature:** ietf.org | Algo 13 | Key Tag 34505

;; ANSWER SECTION: ietf.org. 3600    IN DNSKEY 257 3 13 mdsswUyr[…]53eKGQ== ietf.org. 3600    IN DNSKEY 256 3 13 oJMRESz5[…]a2XhSA== ;; ANSWER SECTION: www.ietf.org. 300 IN RRSIG A 13 3 300 20241211 20241209 ↳ 34505 ietf.org. eSTHK9ql[…]uvSgBA==

Information Classification: General

#BHEU @BlackHatEvents

## Slide 19

## Associating Signatures with Keys

**DNSKEY 1:** ietf.org | Algo 13 | f(KqXX...) = 2371

**DNSKEY 2:** ietf.org | Algo 13 | f(KkxL...) = 34505

**Signature:** ietf.org | Algo 13 | Key Tag 34505

;; ANSWER SECTION: ietf.org. 3600    IN DNSKEY 257 3 13 mdsswUyr[…]53eKGQ== ietf.org. 3600    IN DNSKEY 256 3 13 oJMRESz5[…]a2XhSA== ;; ANSWER SECTION: www.ietf.org. 300 IN RRSIG A 13 3 300 20241211 20241209 ↳ 34505 ietf.org. eSTHK9ql[…]uvSgBA==

Information Classification: General

#BHEU @BlackHatEvents

## Slide 20

## Associating Signatures with Keys

**DNSKEY 1:** ietf.org | Algo 13 | f(KqXX...) = 2371

**DNSKEY 2:** ietf.org | Algo 13 | f(KkxL...) = **34505**

**Signature:** ietf.org | Algo 13 | Key Tag **34505**

;; ANSWER SECTION: ietf.org. 3600    IN DNSKEY 257 3 13 mdsswUyr[…]53eKGQ== ietf.org. 3600    IN DNSKEY 256 3 13 oJMRESz5[…]a2XhSA== ;; ANSWER SECTION: www.ietf.org. 300 IN RRSIG A 13 3 300 20241211 20241209 ↳ 34505 ietf.org. eSTHK9ql[…]uvSgBA==

Information Classification: General

#BHEU @BlackHatEvents

## Slide 21

## Frequencies of Keys in Domains

Association of Keys and Signatures is efficient under normal conditions.

Information Classification: General

#BHEU @BlackHatEvents

## Slide 22

# **KeyTrap Attacks**

#BHEU @BlackHatEvents

## Slide 23

## Associating Signatures with Keys

**DNSKEY 1:** ietf.org | Algo 13 | f(KqXX...) = 2371

**DNSKEY 2:** ietf.org | Algo 13 | f(KkxL...) = 34505

**Signature:** ietf.org | Algo 13 | Key Tag **34505**

;; ANSWER SECTION: ietf.org. 3600    IN DNSKEY 257 3 13 mdsswUyr[…]53eKGQ== ietf.org. 3600    IN DNSKEY 256 3 13 oJMRESz5[…]a2XhSA== ;; ANSWER SECTION: www.ietf.org. 300 IN RRSIG A 13 3 300 20241211 20241209 ↳ 34505 ietf.org. eSTHK9ql[…]uvSgBA==

Information Classification: General

#BHEU @BlackHatEvents

## Slide 24

## Colliding Key Tags

**DNSKEY 1:** ietf.org | Algo 13 | f(KqXX...) = **2371**

**DNSKEY 2:** ietf.org | Algo 13 | f(KkxL...) = 34505

**Signature:** ietf.org | Algo 13 | Key Tag **34505**

;; ANSWER SECTION: ietf.org. 3600    IN DNSKEY 257 3 13 mdsswUyr[…]53eKGQ== ietf.org. 3600    IN DNSKEY 256 3 13 oJMRESz5[…]a2XhSA== ;; ANSWER SECTION: www.ietf.org. 300 IN RRSIG A 13 3 300 20241211 20241209 ↳ 34505 ietf.org. eSTHK9ql[…]uvSgBA==

Information Classification: General

#BHEU @BlackHatEvents

## Slide 25

## Colliding Key Tags

**DNSKEY 1:** ietf.org | Algo 13 | f(KqXX...) = **34505**

**DNSKEY 2:** ietf.org | Algo 13 | f(KkxL...) = **34505**

**Signature:** ietf.org | Algo 13 | Key Tag **34505**

**Wait this can happen!?**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 26

### A Closer Look at Signature Validation

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
blackhat A Closer Look at Signature Validation.
However, it is essential to note that the key tag is not a
unique identifier. It is theoretically possible for two
distinct DNSKEY RRs to have the same owner name, the
same algorithm, and the same key tag. The key tag is
used to limit the possible candidate keys, but it does not
uniquely identify a DNSKEY record. Implementations
MUST NOT assume that the key tag uniquely identifies a
DNSKEY RR.
RFC4034, Appendix B "Key Tag Calculation"
```

## Slide 27

### A Closer Look at Signature Validation

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
blackhat A Closer Look at Signature Validation
It is possible for more than one DNSKEY RR to match
the conditions above. In this case, the validator cannot
predetermine which DNSKEY RR to use to authenticate
the signature, and it MUST try each matching DNSKEY
RR until either the signature is validated or the validator
has run out of matching public keys to try.
RFC4035, Section 5.3.1. "Checking the RRSIG RR
Validity"
```

## Slide 28

### A Closer Look at Signature Validation

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
blackhat A Closer Look at Signature Validation
A
PLE KEYS?
```

## Slide 29

### A Closer Look at Signature Validation

- Linear time algorithm

- Resource-intensive public key crypto operations

- Resolver MUST try all keys?

**That sounds like a bad idea...**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 30

### A Closer Look at Signature Validation

- Linear time algorithm - Resouce intensive public key **<u>Wait, wasn't there more like this?</u>** crypto operations

- Resolver MUST try all keys? **That sounds like a bad idea...**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 31

## We can make it even worse

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
blackhat Wecan make it even worse
This document specifies that a resolver SHOULD accept
any valid RRSIG as sufficient, and only determine that
an RRset is Bogus if all RRSIGs fail validation.
If a resolver adopts a more restrictive policy, there’s a
danger that properly signed data might unnecessarily fail
validation due to cache timing issues. Furthermore,
certain zone management techniques, like the Double
Signature Zone Signing Key Rollover method described
in Section 4.2.1.2 of [RFC6781], will not work reliably.
Such a resolver is also vulnerable to malicious insertion
of gibberish signatures.
RFC6840 Section 5.4. "Caution about Local Policy and
Multiple RRSIGs"
```

## Slide 32

## It’s quadratic!

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
blackhat It’s quadratic!
This document specifies that a resolver SHOULD accept
any valid RRSIG as sufficient, and only determine that
an RRset is Bogus if all RRSIGs fail validation.
If a resolver adopts a more restrictive policy, there’s a
danger that properly signed data might unnecessarily fail
validation due to cache timing issues. Furthermore,
certain zone management techniques, like the Double
Signature Zone Signing Key Rollover method described &
in Section 4.2.1.2 of [RFC6781], will not work reliably. e
Such a resolver is also vulnerable to malicious insertion |
of gibberish signatures.
RFC6840 Section 5.4. "Caution about Local Policy and
Multiple RRSIGs"
```

## Slide 33

## Open Source is doing this…

Signature Loop

<u>https://github.com/NLnetLabs/unbound/ blob/master/validator/val_sigcrypt.c</u> (line 704)

<u>https://github.com/NLnetLabs/unbound/ blob/master/validator/val_sigcrypt.c</u> (line 641)

Key Loop

##### **<u>Nested Loops!</u>**

- Limited buffers?

- Other Mitigations in place?

- → there is only one way to find out

Information Classification: General

#BHEU @BlackHatEvents

## Slide 34

## How much can “all” be?

Not many restrictions in the DNS protocol

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 54/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
pisekhat How much can “all” be?
User Datagram Header Format
Not many restrictions in the DNS protocol
ID
| QDCOUNT
ANCOUNT
NSCOUNT |
```

## Slide 35

## Quick‘n’Dirty Maths

[1] https://blog.cloudflare.com/go-crypto-bridging-the-performance-gap/

Information Classification: General

#BHEU @BlackHatEvents

## Slide 36

## Let’s construct an attack…

How to obtain lots of DNSKEYs with the same tag?

- ➔ Generate many and keep only those conforming to a specific one

Information Classification: General

#BHEU @BlackHatEvents

## Slide 37

## Zone File Contents: DNSKEYs

\```
keytrap.org 60 IN DNSKEY 257 3 13 YpsCtFxj[...]0/G81g== ;{id=26539 (ksk)}
keytrap.org 60 IN DNSKEY 256 3 13 wwZzOFux[...]7s+jGg== ;{id=1337 (zsk)}
keytrap.org 60 IN DNSKEY 256 3 13 AHl8SDyd[...]vgk3gQ== ;{id=1337 (zsk)}
keytrap.org 60 IN DNSKEY 256 3 13 8GP1H4eS[...]3X6dCA== ;{id=1337 (zsk)}
...
keytrap.org 60 IN DNSKEY 256 3 13 brtDSnWm[...]nzlK0w== ;{id=1337 (zsk)}
keytrap.org 60 IN DNSKEY 256 3 13 WfKVRBtM[...]eC3Alw== ;{id=1337 (zsk)}
keytrap.org 60 IN DNSKEY 256 3 13 6+Gbtx4h[...]RacDLw== ;{id=1337 (zsk)}
keytrap.org 60 IN DNSKEY 256 3 13 6KNR3F+Q[...]RcK2kQ== ;{id=1337 (zsk)}
keytrap.org 60 IN DNSKEY 256 3 13 ijhRFa4f[...]L5cBtQ== ;{id=1337 (zsk)}
keytrap.org 60 IN RRSIG DNSKEY 13 4 60 20250117 20240119 26539 keytrap.org gTq+83Bx[...]hcLjQ==
\```

Information Classification: General

#BHEU @BlackHatEvents

## Slide 38

## Zone File Contents: RRSIGs

\```
a0001.keytrap.org 0 IN A 10.2.3.4
a0001.keytrap.org 0 IN RRSIG A 13 5 0 20250117 20240119 1337 keytrap.org GVHrz5G0+[...]0VObdw==
a0001.keytrap.org 0 IN RRSIG A 13 5 0 20250117 20240119 1337 keytrap.org GVHrz5G0+[...]0VObdw==
a0001.keytrap.org 0 IN RRSIG A 13 5 0 20250117 20240119 1337 keytrap.org GVHrz5G0+[...]0VObdw==
…
a0001.keytrap.org 0 IN RRSIG A 13 5 0 20250117 20240119 1337 keytrap.org GVHrz5G0+[...]0VObdw==
a0001.keytrap.org 0 IN RRSIG A 13 5 0 20250117 20240119 1337 keytrap.org GVHrz5G0+[...]0VObdw==
a0001.keytrap.org 0 IN RRSIG A 13 5 0 20250117 20240119 1337 keytrap.org GVHrz5G0+[...]0VObdw==
a0001.keytrap.org 0 IN RRSIG A 13 5 0 20250117 20240119 1337 keytrap.org GVHrz5G0+[...]0VObdw==
a0001.keytrap.org 0 IN RRSIG A 13 5 0 20250117 20240119 1337 keytrap.org GVHrz5G0+[...]0VObdw==
\```

Information Classification: General

#BHEU @BlackHatEvents

## Slide 39

## Attracting a Victim Resolver

###### Attack Vectors

- Querying directly

Information Classification: General

#BHEU @BlackHatEvents

## Slide 40

## Attracting a Victim Resolver

Inbound Mail Server
Victim

Victim

###### Attack Vectors

- Querying directly

- SMTP Bounce

- HTML E-mail

Information Classification: General

#BHEU @BlackHatEvents

## Slide 41

## Scaling up the victim count

###### How to attract many resolvers at the same time?

   - Internet Measurement Networks

- Online Ads

Information Classification: General

#BHEU @BlackHatEvents

## Slide 42

## Attack Procedure

…

attack.er.

…

➢ Flooding the victim resolver with malicious queries

Information Classification: General

#BHEU @BlackHatEvents

## Slide 43

## Demo Time

(Demo)

Information Classification: General

#BHEU @BlackHatEvents

## Slide 44

## KeyTrap Attacks

**SigJam** Jamming the validator with signatures only

**LockCram** Collisions-only attack, using a single RRSIG per response

**KeySigTrap** Combined attack **HashTrap** KeySigTrap with DS records

Information Classification: General

#BHEU @BlackHatEvents

## Slide 45

# **Impact and Evaluations**

#BHEU @BlackHatEvents

## Slide 46

## Which algorithm to use?

Max validations Min validations

##### **<u>Up to ~1M signature validations per DNS Request</u>**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 47

## Evaluations

#### **Test Setup with Unbound.**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 48

## Evaluations

#### **Test Setup with Unbound.**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 49

## Evaluations

#### **Test Setup with Unbound.**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 50

## Evaluations

#### **Test 1: SigJam (Many Signatures / 1 Key)**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 51

## Evaluations

#### **Test 1: SigJam (Many Signatures / 1 Key)**

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Test 1: SigJam (Many Signatures / 1 Key)
340 Signatures /1 Key
DNS Resolver <= l=) ——>
DNS Server
```

## Slide 52

## Evaluations

###### **340 Signature Validations per Request** **<u>10 req/s</u>**

Measured on Intel(R) Xeon(R) Gold 6242 CPU @ 2.80GHz with Unbound

Information Classification: General

#BHEU @BlackHatEvents

## Slide 53

## Evaluations

**340 Signature Validations per Request** **<u>10 req/s</u> Full DOS? We didn't even run the largest attack yet....**

Measured on Intel(R) Xeon(R) Gold 6242 CPU @ 2.80GHz

Information Classification: General

#BHEU @BlackHatEvents

## Slide 54

## Evaluations

#### **Test 2: KeySigTrap (Many Signatures / Many Keys)**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 55

## Evaluations

#### **Test 2: KeySigTrap (Many Signatures / Many Keys)**

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Test 2: KeySigTrap (Many Signatures / Many Keys)
DNS Resolver
340 Signatures / 582 Keys DNS Server
```

## Slide 56

## Evaluations

###### **340 Signatures x 582 Keys = 221160 Validations** **<u>Single Request</u>**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 57

## Evaluations

###### **340 Signatures x 582 Keys = 221160 Validations** **<u>Single Request</u>**

Measured on Intel(R) Xeon(R) Gold 6242 CPU @ 2.80GHz

Information Classification: General

#BHEU @BlackHatEvents

## Slide 58

## Evaluations

**340 Signatures x 582 Keys = 221160 Validations** **<u>Single Request</u>**

18 min DOS

Measured on Intel(R) Xeon(R) Gold 6242 CPU @ 2.80GHz

Information Classification: General

#BHEU @BlackHatEvents

## Slide 59

## Evaluations

|**Resolver**|**Stall Duration**
**(Single Request)**|
|---|---|
|Unbound|1014s|
|Bind9|58632s|
|Knot|51s|
|Akamai|186s|
|PowerDNS|170s|
|Windows Server|132s|
|Stubby|184s|
|Cloudflare 1.1.1.1|Vulnerable|
|Amazon Route 53|Vulnerable|
|Google DNS|Vulnerable|

###### **<u>All tested DNSSEC implementing resolvers vulnerable!</u>**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 60

## Evaluations

|**Resolver**|**Stall Duration**
**(Single Request)**|
|---|---|
|Unbound|1014s|
|Bind9|58632s|
|Knot|51s|
|Akamai|186s|
|PowerDNS|170s|
|Windows Server|132s|
|Stubby|184s|
|Cloudflare 1.1.1.1|Vulnerable|
|Amazon Route 53|Vulnerable|
|Google DNS|Vulnerable|

###### **<u>All tested DNSSEC implementing resolvers vulnerable!</u>**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 61

## Evaluations

|**Resolver**|**Stall Duration**
**(Single Request)**|
|---|---|
|Unbound|1014s|
|Bind9|58632s|
|Knot|51s|
|Akamai|186s|
|PowerDNS|170s|
|Windows Server|132s|
|Stubby|184s|
|Cloudflare 1.1.1.1|Vulnerable|
|Amazon Route 53|Vulnerable|
|Google DNS|Vulnerable|

###### **<u>All tested DNSSEC implementing resolvers vulnerable!</u>**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 62

## Evaluations

Resolver Stall Duration
(Single Request)
Unbound 1014s
Bind9 58632s
Knot 51s
Akamai 186s
PowerDNS 170s
Windows Server 132s
Stubby 184s
Cloudflare 1.1.1.1 Vulnerable
Amazon Route 53 Vulnerable
Google DNS Vulnerable

###### **<u>All tested DNSSEC implementing resolvers vulnerable!</u>**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 63

## Evaluations

###### **Does Multi-Threading help?**

###### **<u>No, but attacker needs to send a few more requests....</u>**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 64

## Evaluations

###### **Viable attack: Comprehensive persistent DoS**

###### **KeyTrap allows to disable DNSSEC resolver with max. a few packets / min**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 65

## Evaluations

###### **Viable attack: Comprehensive persistent DoS**

###### **KeyTrap allows to disable DNSSEC resolver with max. a few packets / min**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 66

# **Impact**

#BHEU @BlackHatEvents

## Slide 67

## Global Impact

Measurements by APNIC Labs

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
pistxhat Global Impact
Code Region DNSSEC Validates Partial Validates Total Validates
XA World 33.67% 8.02% 41.69%
XF Oceania 44.95% 3.80% 48.75%
XE Europe 42.92% 12.77% 55.69%
XB Africa 37.67% 12.11% 49.78% Measurements by APNIC Labs
XC Americas 34.82% 6.61% 41.43%
xD Asia 30.07% 6.57% 36.64%
XG Unclassified 28.84% 16.29% 45.13%
```

## Slide 68

# **Disclosure: Patch-Break-Fix Process**

#BHEU @BlackHatEvents

## Slide 69

## Disclosure

2/11 7/11 9/11 8/12 2/01
13/11 3/01

###### **<u>Fixing KeyTrap included > 30 people and took 3 months</u>**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 70

## Patches

###### **(Patched) Resolver under continuous attack**

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 60/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
(Patched) Resolver under continuous attack
Attack Simulation
—— CPU Load 1.
O 0 20 40 60 80 100 120 140 160
Time [s]
Information Classification: General 1
```

## Slide 71

## Patches

###### **(Patched) Resolver under Hash attack**

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Patches
(Patched) Resolver under Hash attack
CPU Load / Lost Packets [%]
100
~N
ul
N
ul
Attack Simulation
— CPU Load pon
y |
|
0 25 50 75 100 125 150 175
Time [s]
```

## Slide 72

# **Lessons Learned**

#BHEU @BlackHatEvents

## Slide 73

## BlackHat Soundbites

- The KeyTrap Attacks allow for comprehensive DoS on a plethora of DNSSEC-validating resolvers

- Vulnerability stems from "eager validation" in RFCs Desire to ensure availability compromised availability

- Specification needs to consider impact on resource consumption by implementations

- Read our paper here -

- https://doi.org/10.1145/3658644.3670389

Information Classification: General

#BHEU @BlackHatEvents
