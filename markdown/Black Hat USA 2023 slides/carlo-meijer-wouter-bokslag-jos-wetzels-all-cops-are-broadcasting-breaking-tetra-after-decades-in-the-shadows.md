---
title: "All Cops Are Broadcasting Breaking TETRA After Decades in the Shadows"
speakers: ["Carlo Meijer", "Wouter Bokslag", "Jos Wetzels"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/Carlo Meijer & Wouter Bokslag & Jos Wetzels_All Cops Are Broadcasting Breaking TETRA After Decades in the Shadows.pdf"
pages: 59
sha256: "60096e69e317376b560b06e9dd9b3eab0ca1dd4aa478935fbe5d9044f1cd1829"
text_chars: 23553
ocr_pages: 1
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:14:31Z"
---
# All Cops Are Broadcasting Breaking TETRA After Decades in the Shadows

**Speakers:** Carlo Meijer, Wouter Bokslag, Jos Wetzels  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Carlo Meijer & Wouter Bokslag & Jos Wetzels_All Cops Are Broadcasting Breaking TETRA After Decades in the Shadows.pdf` (59 pages)


## Slide 1

All Cops Are Broadcasting

**August 2023**

###### ALL COPS ARE BROADCASTING Breaking TETRA after decades in the shadows

By Midnight Blue

1

sales@midnightblue.nl  //  midnightblue.nl  //  All Right Reserved

## Slide 2

All Cops Are Broadcasting

Jos Wetzels, MSc

Wouter Bokslag, MSc

Carlo Meijer, MSc

# Midnight Blue

Selected Research

midnightblue.nl

2

August 2023

## Slide 3

All Cops Are Broadcasting

# What is TETRA?

- Globally used radio technology ▪ Competes with P25, DMR, TETRAPOL

- Standardized in 1995 by ETSI

   - Known for GSM, 3G/4G/5G, GMR, etc.

- Used for voice & data communications incl. machine-to-machine

- Relies on secret, proprietary cryptography

midnightblue.nl

3

August 2023

## Slide 4

All Cops Are Broadcasting

### Use by police

Vast majority of global police forces use TETRA radio technology.

- C2000 (NL)

- ASTRID (BE)

- BOSNET (DE)

- AIRWAVE (UK)

- Nødnett (NO)

- Rakel (SE)

- SINE (DK)

- VIRVE (FI)

- SIRESP (PT)

   - ...

Based on OSINT

August 2023

midnightblue.nl

4

## Slide 5

All Cops Are Broadcasting

### Military & Intelligence

Many countries have one or more military or intelligence units using TETRA radio technology as primary, fallback, or interfacing comms.

Based on OSINT

August 2023

midnightblue.nl

5

## Slide 6

All Cops Are Broadcasting

### Critical Infrastructure

Many parties such as airports, harbors, and train stations use TETRA for voice communications. In addition TETRA is used for SCADA WAN, such as substation & pipeline control, or railway signalling.

Based on OSINT

6

August 2023

midnightblue.nl

## Slide 7

All Cops Are Broadcasting

# Open standard?

- Public standard, secret crypto

   - NDAs, only available for ‘bona fide’ parties

- Manufacturers must protect algorithms

   - Hardware, or, implementations

   - Software with extraction countermeasures

midnightblue.nl

August 2023

7

## Slide 8

All Cops Are Broadcasting

### Lots of ‘bona fide’ vendors

Significant amount of geographically dispersed players Top-tier adversaries likely have specs (e.g. via in-country manufacturers or theft)

Historical M&As

Teltronic, Simoco → Sepura, Nokia → Airbus, Rohde & Schwarz, PowerTrunk → Hytera, Selex ES → Leonardo, Chelton → Cobham, Artevea → dissolved.

midnightblue.nl

8

August 2023

## Slide 9

All Cops Are Broadcasting

###### • TAA1 suite

# TETRA security

   - Authentication, key management / distribution (OTAR)

   - Identity encryption

   - Remote disable

- TEA (TETRA Encryption Algorithm) suite

   - Voice and data encryption (Air Interface Encryption (AIE))

      - **TEA1: Readily exportable**

      - **TEA2: European public safety**

      - **TEA3: Extra-European public safety**

      - **TEA4: Readily exportable (hardly used)**

   - Not to be confused with Tiny Encryption Algorithm!

midnightblue.nl

9

August 2023

## Slide 10

All Cops Are Broadcasting

# Optional: end-to-end

- Only used by some countries, usually for special cases only

- Not inside TETRA standard

   - Some guidelines / integrations are provided

- Proprietary solution on top of AIE − Expensive

- Again, very opaque…

   - High-level specification but no detail

midnightblue.nl

10 August 2023

## Slide 11

# Project RE:TETRA

midnightblue.nl

sales@midnightblue.nl  //  midnightblue.nl  //  All Right Reserved

## Slide 12

All Cops Are Broadcasting

# Kerckhoffs’ principle

midnightblue.nl

12

August 2023

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
oe) All Cops Are Broadcasting
Kerckhoffs’ principle
“A cryptosystem should be secure even if everything about the system,
except the key, is public knowledge.”
-Auguste Kerckhoffs, 1883
midnightblue.nl 12 August 2023
```

## Slide 13

All Cops Are Broadcasting

## Violators don’t fare well

- A5/1, A5/2 (GSM), COMP128 (GSM)

- GMR-1, GMR-2 (SATPHONES)

- DSAA, DSC (DECT)

- MIFARE (RFID)

- HITAG (RFID)

   - DST (RFID)

   - Legic (RFID)

   - CSS (DVD)

- GEA-1, GEA-2 (GPRS)

- MEGAMOS (RFID)

   - CryptoAG / Hagelin

- Orange = backdoored

midnightblue.nl

13

August 2023

## Slide 14

All Cops Are Broadcasting

# ~~Kerckhoffs’ principle~~ ETSI’s principle

- Interview between Kim Zetter and Brian Murgatroyd, Chair of ETSI TC TETRA https://zetter.substack.com/p/interview-with-the-etsi-standards

midnightblue.nl

14

August 2023

## Slide 15

All Cops Are Broadcasting

## Project motivation

- Proprietary cryptography has repeatedly suffered from practically exploitable flaws which remain unaddressed until disclosed

- GOAL: open up TETRA for public review after 20+ years

   - Enables informed risk analysis

   - Resolve issues

   - Level playing field

- Funded by NLnet

   - NPO funding open IT projects

midnightblue.nl

15

August 2023

## Slide 16

All Cops Are Broadcasting

## Research program

Analysis

Cipher Extraction

###### Attack R&D

Procurement

   - Firmware analysis

- Analyze landscape

- Hack the radio (multiple 0-days)

      - Cipher reverse engineering

   - Identify cipher location

- Obtain right radio (Motorola MTM5400)

   - Cryptanalysis

- Extract ciphers from radio

   - Validate with PoC

- Develop tooling

midnightblue.nl

16

August 2023

## Slide 17

All Cops Are Broadcasting

##### Pwning MTM5400

1. Format string code exec on AP

2. Pivot to DSP via shared memory

3. Cache timing side-channel on TEE

4. Secret algos!

   - … and key extraction …

5. More details at DEF CON

   - … we only have 40 minutes here 

midnightblue.nl

17

August 2023

## Slide 18

# The secret TETRA primitives and their security

midnightblue.nl

sales@midnightblue.nl  //  midnightblue.nl  //  All Right Reserved

## Slide 19

All Cops Are Broadcasting

# TAA1 auth and OTAR

- Protocols in public standard, primitives not. We recovered:

- All TAxx based on HURDLE* cipher

   - 16-round Feistel cipher

   - 64-bit blocks, 128-bit key

- All TBx based on XOR / addition

- Some blocks identical / related − TA11 = TA41

   - TA12 = TA22

   - TA11(K, RS) = TA21(K, reversed(RS))

* https://impact.ref.ac.uk/casestudies/CaseStudy.aspx?Id=30193

midnightblue.nl

19

August 2023

## Slide 20

All Cops Are Broadcasting

###### CVE-2022-24400 DCK pinning attack

- Mutual authentication

   - Shared long-term secret K

   - Random seed RS

   - Challenge-response (RANDx/RESx)

   - Session key DCK

###### **`DCK = TB4(TA12(TA11(K, RS), RAND1), TA22(TA21(K, RS), RAND2)))`**

midnightblue.nl

20

August 2023

## Slide 21

All Cops Are Broadcasting

###### CVE-2022-24400 DCK pinning attack

- We can simplify the authentication procedure now that we know primitives

TA11(K, reverse(RS))
TA12
XOR

```
DCK = TB4(TA12(TA11(K, RS), RAND1), TA22(TA21(K, RS), RAND2)))
equals
```

```
DCK =     TA12(TA11(K, RS), RAND1) ^ TA12(TA11(K, reversed(RS)), RAND2)
```

midnightblue.nl

21

August 2023

## Slide 22

All Cops Are Broadcasting

###### CVE-2022-24400 DCK pinning attack

- Assume we impersonate infrastructure and:

   - reversed(RS) = RS    (“palindrome”)

− Predict MS challenge RAND2, use it as RAND1 as well

- Then, DCK simplifies to:

```
DCK = TA12(TA11(K, RS), RAND2) ^ TA12(TA11(K, RS), RAND2)
equals
```

**`DCK = XOR(X, X) = 0`**  **`ALL ZERO KEY`** • Authenticated channel with radio, intercept uplink, post-auth functionality, etc.

August 2023

midnightblue.nl

22

## Slide 23

All Cops Are Broadcasting

## Identity encryption

- Part of TAA1, called TA61

- Encrypts 24-bit TETRA addresses − encrAddr = TA61(addr)

- Pseudonymity, not anonymity

   - Encrypted identities change only when network key changes

- _Implementation disclosed in December.._

   - _Following serious concerns raised by stakeholders_

midnightblue.nl

23

August 2023

## Slide 24

All Cops Are Broadcasting

##### CVE-2022-24403 De-anonymization

- _Intermediate secret_ 𝑐 is derived from CCK using HURDLE

   - Full details in December

- TA61 is vulnerable to _meet-in-themiddle_ attack

   - Recovers value of 𝑐

   - Complexity: 2<sup>48</sup> with 3 identity pairs

   - 1 min on laptop

   - Then, instant deanonymization

- Also: attack on HURDLE could be catastrophic now… − **CCK recovery?**

midnightblue.nl

24

August 2023

## Slide 25

All Cops Are Broadcasting

##### De-anonymization Scenario

- Contextualize

   - Correlate identities with observed units

   - Identity ranges allocated to user groups

- Build live tracking map

   - Counter-intelligence (unmask covert surveillance units)

   - Early warning (of e.g. police intervention)

- Convenient

   - Raspberry Pi + RTL-SDR dongle can be spread for geographic coverage

   - Fully passive, so stealthy!

midnightblue.nl

25

August 2023

## Slide 26

All Cops Are Broadcasting

### TEA Keystream generators

- Used for air interface encryption

- All KSGs have similar structure

- TEA2 seems robust* − We are not cryptographers

- Public scrutiny needed!

Pictured: TEA2

midnightblue.nl

26

August 2023

## Slide 27

All Cops Are Broadcasting

##### CVE-2022-24402 TEA1 backdoor

- Target audience

   - Private security, “less friendly” police / mil

   - .. But also, power, water, oil & gas

- Advertised with 80-bit key

   - Readily exportable but no hard indication on actual security (56-bit? 40-bit? 32-bit?)

- Has “key initialization” function − Reduces 80-bit key into 32-bit register

- Trivial passive brute force (<1min)

- Intercept comms

- Inject data (SCADA WAN!)

midnightblue.nl

27

August 2023

## Slide 28

All Cops Are Broadcasting

Demo: CVE-2022-24402 TEA1 Attack

midnightblue.nl

28

August 2023

## Slide 29

All Cops Are Broadcasting

##### NVIDIA GTX 1080

State-of-the-art… consumer hardware… in 2016…

“ **BM** : The researchers found that they were able to decrypt messages from this, using a **very highpowered graphics card** in about a minute.”<sup>1</sup>

“ **BM** : I suppose all I can say is that **25 years ago the length of this algorithm was probably sufficient to withstand brute-force attacks** . **KZ** : You’re saying 25 years ago 32 bit would have been secure? **BM** : I think so. I can only assume.”<sup>1</sup>

“ **BM** : I would say it’s vulnerable if you happen to be an expert and have some **pretty reasonable equipment** .”<sup>1</sup>

1 Interview between Kim Zetter and Brian Murgatroyd, Chair of ETSI TC TETRA <u>https://zetter.substack.com/p/interview-with-the-etsi-standards</u>

midnightblue.nl

29

August 2023

## Slide 30

All Cops Are Broadcasting

• Let’s not assume

midnightblue.nl

30

August 2023

## Slide 31

All Cops Are Broadcasting

- Let’s not assume

- Let’s not use reasonable equipment

midnightblue.nl

31

August 2023

## Slide 32

All Cops Are Broadcasting

##### Toshiba Satellite 4010CDS

- Let’s not assume

- Let’s not use reasonable equipment

- Let’s go back to 1998!

   - 266 MHz Pentium II

   - 4.1 billion byte hard disk

   - 32MB SDRAM

midnightblue.nl

32

August 2023

## Slide 33

All Cops Are Broadcasting

# Demo: Party like the ‘90s

midnightblue.nl

33

August 2023

## Slide 34

All Cops Are Broadcasting

- Air interface signalling is encrypted

##### Air Interface Encryption

- MAC header is unencrypted*

- LLC header and further payload gets encrypted by TEAx keystream generator (KSG)

- TETRA messages have no cryptographic auth/integrity guarantee

   - CRC16 on lower MAC layer

   - Optional CRC32 on LLC layer

midnightblue.nl

34

August 2023

## Slide 35

All Cops Are Broadcasting

#### Air Interface Encryption

- TEAx keystream generators depend on key and on network time

   - Need to guarantee different keystream is used each time

- Network time broadcast in unencrypted, unauthenticated manner

   - SYNC and SYSINFO frames

- As mentioned; no further _cryptographic_ integrity checks

   - Any encrypted data is taken at face value

midnightblue.nl

35

August 2023

## Slide 36

All Cops Are Broadcasting

##### CVE-2022-24401 Keystream recovery attack

- Attacker can overpower infrastructure and alter MS perception of time

- MS will then use keystream that fits the attacker specified network time

- Works regardless of TEA used, regardless of ‘network authentication’

August 2023

midnightblue.nl

36

## Slide 37

All Cops Are Broadcasting

## Attack outline

###### Attack outline:

- Capture interesting encrypted message at time T

- Target MS (any, with same keys)

- Overpower legitimate signal

- Set MS time to time T

- _Somehow recover keystream for that time_

- …

- Profit

August 2023

midnightblue.nl

37

## Slide 38

All Cops Are Broadcasting

#### Recovering keystream

- Assume we have n bits of keystream for time t. Construct message such that:

   - It is of length n+1

   - It has an FCS

   - It needs an ACK from the MS

- Encrypt, guess last ks bit is zero

- Send to MS

- If MS ACKs: FCS was good

   - Found keystream bit n+1 = 0

   - If no ACK: keystream bit  n+1 = 1

- Repeat

August 2023

midnightblue.nl

38

## Slide 39

All Cops Are Broadcasting

##### Bootstrap

- We need _seed keystream_

- Send 16 messages

   - `00000` , `00010` , …, `11110`

   - Will be decrypted by MS

- Only one will get ACK from MS

   - BL-DATA w/o FCS

   - Other messages are longer or unACKed

- Recovered 4 bits of ks ☺

midnightblue.nl

39

August 2023

## Slide 40

All Cops Are Broadcasting

- Recover 4 bits for 10 slots

##### From 4 to 37 bits

- Craft aforementioned message with FCS (min 37 bits)

- Use MAC fragmentation to distribute over the 10 slots

- Grow keystream knowledge for any slot of interest by guessing next ks bit

August 2023

midnightblue.nl

40

## Slide 41

All Cops Are Broadcasting

### Intermezzo: ETSI

- “Theoretical attack”

- Okay, so, can we have a base station to prove practicality?

   - Haha lol no

   - More stakeholders responded like this

- What do we do now?

   - Implement TETRA infra stack for SDR?

   - Sounds like a lot of work…

midnightblue.nl

41

August 2023

## Slide 42

All Cops Are Broadcasting

# There’s your PoC

- Bought old Motorola MBTS

- Found some vulns in it

- Wrote module framework for it

- Turned it into attack platform 💪

midnightblue.nl

42

August 2023

## Slide 43

All Cops Are Broadcasting

# Demo: CVE-2022-24401 Keystream recovery attack

midnightblue.nl

43

August 2023

## Slide 44

All Cops Are Broadcasting

### ETSI’s response?

“The research uncovered some general areas for improvement in the TETRA protocol”<sup>1</sup>

1 ETSI and TCCA Statement to TETRA Security Algorithms Research Findings Publication on 24 July 2023 <u>https://www.etsi.org/newsroom/news/2260-etsi-and-tcca-statement-to-tetra-security-algorithms-research-findings-publication-on-24-july-2023</u>

midnightblue.nl

August 2023

44

## Slide 45

All Cops Are Broadcasting

**0f**

**00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f 00** 7D BF 7B 92 AE 7C F2 10 5A 0F 61 7A 98 76 07 64 **10** EE 89 F7 BA **C2** 02 0D E8 56 2E CA 58 C0 FA 2A 01 **20** 57 6E 3F 4B 9C DA A6 5B 41 26 50 24 3E F8 0A 86 **30** B6 5C 34 E9 06 88 1F 39 33 DF D9 78 D8 A8 51 B2 **40** 09 CD A1 DD 8E 62 69 4D 23 2B A9 E1 53 94 90 1E **50** B4 3B F9 4E 36 FE B5 D1 A2 8D 66 CE B7 C4 60 ED **60** 96 4F 31 79 35 EB 8F BB 54 14 CB DE 6B 2D 19 82 **70** 80 AC 17 05 FF A4 CF C6 6F 65 E6 74 C8 93 F4 7E **80** F3 43 9F 71 AB 9A 0B 87 55 70 0C AD CC A5 44 E7 **90** 46 45 03 30 1A EA 67 99 DB 4A 42 D7 AA E4 **C2** D5 **a0** F0 77 20 C3 3C 16 B9 E2 EF 6C 3D 1B 22 84 2F 81 **b0** 1D B1 3A E5 73 40 D0 18 C7 6A 9E 91 48 27 95 72 **c0** 68 0E 00 FC C5 5F F1 F5 38 11 7F E3 5E 13 AF 37 **d0** E0 8A 49 1C 21 47 D4 DC B0 EC 83 28 B8 F6 A7 C9 **e0** 63 59 BD 32 85 08 BE D3 FD 4C 2C FB A0 C1 9D B3 **f0** 52 8C 5D 29 6D 04 BC 25 15 8B 12 9B D6 75 A3 97

### TEA3 quirk 🤔

- Sbox not a permutation

- Duplicate entry

- • Used for air − Flip bit matches properties of other TEAs interface encryption

- Key register feedback structure slightly different, hides the issue

- • All KSGs have

   - similar structure

- Highly unusual, certainly not positive

- • Here: TEA2

   - Unlikely to be accidental

- Could find no flaws − Interoperability, feedback structure

- − Public scrutiny

- needed

- • Impact unclear

   - Could not find practical attack

   - **Public scrutiny needed!**

midnightblue.nl

## Slide 46

# Coordinated Vulnerability Disclosure

46

sales@midnightblue.nl  //  midnightblue.nl  //  All Right Reserved

## Slide 47

All Cops Are Broadcasting

• Started work on the RETETRA project 01-2021 • First contact NCSC-NL 12-2021 • First meeting Dutch police 01-2022 • First meeting ETSI 01-2022 • First meeting intelligence community 01-2022 • Detailed preliminary advisory distributed 02-2022 • Further advisory info & mitigations distributed to stakeholders ’22/’23 • Coordinated publication timeline midnightblue.nl

######

August 2023

47

## Slide 48

All Cops Are Broadcasting

# Mitigations

|**CVE**|**Description**|**Recommended Mitigation**|**Compensating Controls**|
|---|---|---|---|
|CVE-2022-24401
CVE-2022-24404|Keystream recovery
attack|•
Firmware updates
•
E2E
•
(data) TLS / IPsec|•
Renew keys frequently
•
Risk assessment, adjust
OPSEC|
|CVE-2022-24402|TEA1 backdoor|•
TEA2
•
E2E
•
(data) TLS / IPsec|•
Assume TEA1 == cleartex
•
Risk assessment, adjust
OPSEC|
|CVE-2022-24403|Deanonymization
attack|•
Migrate to TAA2|•
Risk assessment, adjust
OPSEC|
|CVE-2022-24400|DCK key pinning
attack|•
Firmware updates
•
E2E
•
Migrate to TAA2|•
Disable radios with
unacceptable FW update
rollout timelines|

- Assume TEA1 == cleartext

- • Risk assessment, adjust OPSEC

midnightblue.nl

48

August 2023

## Slide 49

# Aftermath

49

midnightblue.nl

sales@midnightblue.nl  //  midnightblue.nl  //  All Right Reserved

## Slide 50

All Cops Are Broadcasting

- What’s this “Europe” you speak of?

# Hold on…

- Poland, Bulgaria, Croatia, Montenegro, Moldova

- All (candidate) EU states

“ **BM:** And I would expect that anybody … who need a lot of protection would not just be using TEA1. Within Europe… I would suggest that anyone who needed high security would be using TEA2. …. The problems generally are that TEA2 is only licensed for use within Europe by public safety authorities.”<sup>1</sup>

- 1 Interview between Kim Zetter and Brian Murgatroyd, Chair of ETSI TC TETRA <u>https://zetter.substack.com/p/interview-with-the-etsi-standards</u>

- Allowed to use TEA2 according to ETSI’s own standards<sup>4</sup> − As far back as 2003 or 2008

- Yet…

   - **Tenders show TEA1 equipment was procured by all for police/military in last 5 years**<sup>**2,3**</sup> **…**

> 2 <u>https://www.volkskrant.nl/nieuws-achtergrond/overheid-weet-al-dertig-jaar-van-achterdeur-in-beveiliging-radiocommunicatie~bcefc760/</u>

- 3 <u>https://www.o2.pl/informacje/niepokojace-informacje-luka-w-systemie-tetra-niech-ktos-cos-zrobi-6923376203832288a</u>

4 https://www.etsi.org/deliver/etsi_tr/101000_101099/10105302/02.01.01_60/tr_10105302v020101p.pdf <u>https://www.etsi.org/deliver/etsi_tr/101000_101099/10105302/02.02.02_60/tr_10105302v020202p.pdf https://www.etsi.org/deliver/etsi_ts/101000_101099/10105302/02.03.01_60/ts_10105302v020301p.pdf</u>

midnightblue.nl

50

August 2023

## Slide 51

#### Maybe nobody targets TETRA networks?

“ **KZ:** But is that in the best interest of the public that are using these algorithms?

**BM:** Well it’s a moot point isn’t it, really. That’s a difficult thing to say “yes it’s to the benefit of the public or not.” There’s no evidence of any attacks on … TETRA that we know of.”<sup>1</sup>

“ETSI and TCCA are not at this time aware of any exploitations on operational networks.”<sup>2</sup>

**2 out of 5 attacks are passive so…** 🤔

- 1 Interview between Kim Zetter and Brian Murgatroyd, Chair of ETSI TC TETRA <u>https://zetter.substack.com/p/interview-with-the-etsi-standards</u>

- 2 ETSI and TCCA Statement to TETRA Security Algorithms Research Findings Publication on 24 July 2023 <u>https://www.etsi.org/newsroom/news/2260-etsi-and-tcca-statement-to-tetra-security-algorithms-research-findings-publication-on-24-july-2023</u>

midnightblue.nl

sales@midnightblue.nl  //  midnightblue.nl  //  All Right Reserved

## Slide 52

All Cops Are Broadcasting

## Right…

Snowden leaks show joint NSA & ASD project to collect Indonesian police TETRA comms during U.N. climate change conf in Bali 2007<sup>1</sup>

Not proof of TETRA:BURST – exploitation specifically but proof of _active TETRA targeting_

> 1 <u>https://theintercept.com/document/nsa-telegraph-sigdev-efforts-in-support-of-the-united-nations-framework-for-climate-change-conferencebali-indonesia/</u> midnightblue.nl

52

August 2023

## Slide 53

All Cops Are Broadcasting

## Right…

Snowden leaks reveal GCHQ TSI ‘ _effects operation_ ’ QUITO Falklands/Malvinas oil exploration rights tensions in 2009<sup>1</sup> Involved TETRA collects as part of military/leadership tasking

against AR around

Not proof of TETRA:BURST exploitation specifically – but proof of _active TETRA targeting_

> 1 <u>https://cryptome.org/2015/04/nsa-gchq-jtrig-intercept-15-0402.pdf</u> midnightblue.nl

53

August 2023

## Slide 54

All Cops Are Broadcasting

# What’s next?

- ETSI announced update to standard − TAA1 TAA2 − TEA{1,3} TEA{5,7} − Keystream recovery mitigation*

- Again: secret algorithms<sup>2</sup> !

“ **KZ:** If you’re saying that the only reason they’re secret is because the government has advised it, can ETSI decide on its own to make them public? **BM:** I’d have to say yes. **KZ:** So why don’t you? **BM: I don’t know** .“<sup>1</sup>

1 Interview between Kim Zetter and Brian Murgatroyd, Chair of ETSI TC TETRA <u>https://zetter.substack.com/p/interview-with-the-etsi-standards</u> 2 ETSI TS 101 053-5, ETSI TS 101 053-6, ETSI TS 101 053-7

midnightblue.nl

August 2023

54

## Slide 55

All Cops Are Broadcasting

# Should we trust TEA6/7? What do you think?

August 2023

midnightblue.nl

55

## Slide 56

All Cops Are Broadcasting

# Should we trust TEA6/7? Let’s ask ETSI!

“ **KZ: Should we trust ETSI algorithms going forward** ?

**BM:** I’ve no reason to believe you shouldn’t.

**KZ:** But the public has a reason not to — the fact that they’re secret.

**BM:** I can think of all sorts of algorithms that, over time, they become weak. And lots of them have been public ones as well. Sure, algorithm may not have a life of a quarter of a century that’s for sure…. [But] **we have no reason to produce dodgy algorithms, if you like.** ”<sup>1</sup>

“ **BM:** We were just given those algorithms. **And the algorithms were designed with some assistance from some government authorities, let me put it that way** .”<sup>1</sup>

“ **BM: At the end of the day, it’s down to the customer organization to ensure that things are secure enough for them. Now, I agree that’s difficult with a private algorithm.** The manufacturer knows the length of the key, but it’s not publicly available. **But the reason we have three different algorithms available must be clear to somebody that they’re not all as secure as each other.** “<sup>1</sup>

1 Interview between Kim Zetter and Brian Murgatroyd, Chair of ETSI TC TETRA <u>https://zetter.substack.com/p/interview-with-the-etsi-standards</u>

NOTE: BM’s comments refer to TEA1-4 but there is little reason to doubt their applicability to TEA5-7

midnightblue.nl

56

August 2023

## Slide 57

All Cops Are Broadcasting

### Conclusion

- First public, in-depth TETRA security analysis (after 20+ years)

- Secret crypto algorithms reverse-engineered

- Multiple vulnerabilities uncovered (incl. backdoor)

100+ many sectors countries

- Implications for voice, data, and SCADA

- Patches available for some issues, mitigations for others

midnightblue.nl

57

August 2023

## Slide 58

All Cops Are Broadcasting

###### 1. Take a closer look at the TEAs

# Call to Action

   - Especially the TEA3 S-Box!

2. Take a closer look at HURDLE

   - An attack on HURDLE could be catastrophic due to attack on TA61

3. Implement / extend open TETRA stacks

   - Great work by OsmocomTETRA / SQ5BPF

   - .. Still lots to do, talk to NLnet, OsmocomTETRA

###### **4. Stop doing secret crypto please**

- Looking at you, TEA{5,6,7} / TAA2…

- • Also looking at you, TETRA E2EE…

58

midnightblue.nl

August 2023

## Slide 59

All Cops Are Broadcasting

###### Social

## Questions?

###### Web

- midnightblue.nl

- tetraburst.com

###### Contact

- c.meijer@midnightblue.nl

- w.bokslag@midnightblue.nl

- j.wetzels@midnightblue.nl

midnightblue.nl

59

August 2023
