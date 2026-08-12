---
title: "Riding for Free - Breaking Public Transport RFID at Scale"
speakers: ["Aidan Nakache"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: null
source_pdf: "DEF CON 34/DEF CON 34 - Aidan Nakache - Riding for Free - Breaking Public Transport RFID at Scale - v1.pdf"
pages: 54
sha256: "b7b1102d94843dbc016b3168a10365bcfe93b977aeaaef7150eec39504618a3e"
text_chars: 18073
ocr_pages: 0
has_ocr: false
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2"
converted_at: "2026-08-12T00:11:16Z"
---
# Riding for Free - Breaking Public Transport RFID at Scale

**Speakers:** Aidan Nakache  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Aidan Nakache - Riding for Free - Breaking Public Transport RFID at Scale - v1.pdf` (54 pages)

## Slide 1

**D E F C O N 3 4   ·   L A S V E G A S   ·   A U G U S T 2 0 2 6**

RIDING FOR FREE Breaking Public Transport RFID at Scale

**Aidan Nakache   luu176** `github.com/luu176   ·   linkedin.com/in/nakache-aidan`

## Slide 2

###### **I N T R O**

###### **`$ whoami`**

###### Aidan Nakache **`luu176`**

Creator of **Metroflip** , open source transit card reader for Flipper Zero **Returning speaker** : DEF CON 33, self-laundry RFID card vulns I mess with hardware in my free time

Just graduated high school CTO at an analog film shop in Spain

Two more jobs under NDA: cybersecurity and full-stack dev

**INTRO**

```
02
```

R I D I N G F O R F R E E

## Slide 3

###### **T H E T A P**

###### You've done this a thousand times

Metro, bus, tram. You tap, you're in.

You never think about the card.

**INTRO**

```
03
```

R I D I N G F O R F R E E

## Slide 4

###### **W H A T Y O U ' R E A C T U A L L Y C A R R Y I N G**

###### It's a tiny computer

Holds money, travel history, sometimes an ID that ties back to you This talk looks at the application layer: the data inside and its cryptographic weaknesses

**Hundreds of millions** of people tap one every day

**INTRO**

```
04
```

R I D I N G F O R F R E E

## Slide 5

###### **T H E U N I V E R S A L T R U T H**

###### 50+ cities. Zero published specs.

Every agency rolls its own data format None of it is documented Security through obscurity is the whole model

**OBSCURIT Y**

```
05
```

R I D I N G F O R F R E E

## Slide 6

###### **S E C U R I T Y T H R O U G H O B S C U R I T Y**

###### “If nobody knows the format, nobody can break it.”

That is the whole bet. It does not hold.

**OBSCURIT Y**

```
06
```

R I D I N G F O R F R E E

## Slide 7

###### **D E F C O N H A S S E E N T R A N S I T B E F O R E**

###### Every past talk broke one city

DEF CON 16: the Boston subway hack DEF CON 31: the Boston money glitch This talk is about **the patterns everywhere**

**OBSCURIT Y**

```
07
```

R I D I N G F O R F R E E

## Slide 8

###### **T H E T O O L**

###### One open tool reads them all

Metroflip: open source, on the Flipper Zero **100,000+** downloads

17+ card formats

Built by contributors worldwide

Metroflip reading and parsing Navigo card contents

**METROFLIP**

```
08
```

R I D I N G F O R F R E E

## Slide 9

###### **O N E T A P , M A N Y T E C H N O L O G I E S U N D E R N E A T H**

|**PROTOCOL**|**SECURITY**|**WHERE YOU'VE TAPPED IT**|
|---|---|---|
|**MIFARE Classic**|**CRYPTO1 (broken)**|RENFE (Spain), Troika (Russia), CharlieCard (US)|
|**MIFARE DESFire**|**AES-128**|Clipper (US), myki (AU), Opal (AU), nol (UAE)|
|**MIFARE Ultralight (C/AES)**|**none / 3DES / AES**|TRT (China), single-use tickets|
|**FeliCa**|**3DES / AES**|Suica (Japan), Octopus (Hong Kong)|
|**Calypso**|**SAM 3DES / AES**|Navigo (France), Opus (Canada), Rav-Kav (Israel)|
|**CIPURSE**|**AES-128, SAM**|T-Mobilitat (Spain)|
|**ST25TB**|**none**|Intertic (France), 25 cities|

**METROFLIP**

```
09
```

R I D I N G F O R F R E E

## Slide 10

###### **O N E O P E N T O O L , T H E W H O L E N E T W O R K**

**Hong Kong Tokyo** Octopus Suica

**San Francisco Boston** Clipper CharlieCard

**Moscow Paris London** Troika Navigo ITSO **Sydney Melbourne Montreal** Opal myki Opus

**Dubai** nol

**Israel** Rav-Kav

**Santiago** Bip!

**Tbilisi** Metromoney

**Tianjin** TRT

**Spain** RENFE

**Barcelona** T-Mobilitat

**METROFLIP**

```
10
```

R I D I N G F O R F R E E

## Slide 11

###### **H O N G K O N G**

###### Buying groceries with your bus card?

Octopus, a pioneer since 1997

- A fare card that became a debit card

Dining, supermarkets, vending, convenience stores

- ~190,000 acceptance points across Hong Kong FeliCa kept up: 3DES and AES now

The longer it runs, the harder it is to change

**METROFLIP**

```
11
```

R I D I N G F O R F R E E

## Slide 12

###### **T H E P A T T E R N**

###### The broken stuff never leaves

**CRYPTO1** : broken since 2008, still deployed

Secure chips get deployed insecurely Static keys, unlocked pages, no integrity Security through obscurity buys time, never security

**METROFLIP**

```
12
```

R I D I N G F O R F R E E

## Slide 13

###### **A N D I T ' S N O T J U S T M E**

###### Even single-ride tickets fall

MIFARE Ultralight is behind limited-use tickets The **BreakMeIfYouCan** team broke the 3DES and AES versions Keyspace collapses from **2^112 to 2^28** Static keys and clones crack in seconds

Research: Nye, Teuwen, Messmer, Mauch, Clark, Li, Weiss, Voeltner. breakmeifyoucan.com, eprint 2026/100

**METROFLIP**

```
13
```

R I D I N G F O R F R E E

## Slide 14

###### **T H E M E T H O D**

###### So how does reverse engineering work?

Start from a value you already know Change one variable, nothing else **Diff** it and find the pattern

Repeat per variable to isolate them all

**METHOD**

```
14
```

R I D I N G F O R F R E E

## Slide 15

###### **T H E R E A D P H A S E**

###### A locked card is not a wall

Recover keys with darkside, nested, hardnested No key needed to start

One known key leaks the rest

Minutes on a Proxmark or Flipper

**METHOD**

```
15
```

R I D I N G F O R F R E E

## Slide 16

###### **D E C O D E B Y C O N T R A S T**

###### Make the card change, watch what moves

Bought a 10-trip card? Look for 0x0A Travelled on a date? Find the field that matches Tapped at a station? Find its code Predict, tap, re-read. If right, you named a field.

**METHOD**

```
16
```

R I D I N G F O R F R E E

## Slide 17

###### **E V E R Y C A R D I S I T S O W N A L I E N**

###### No two systems agree on anything

Little-endian here, big-endian two bytes over

Dates nibble-swapped, or from a random year

Balances stored in tenths of a cent

Station codes need a table they won't share

**METHOD**

```
17
```

R I D I N G F O R F R E E

## Slide 18

###### **R E A D I N G I S E A S Y , C H A N G I N G I S H A R D**

###### Every block is guarded by a checksum

Get it wrong and the gate says no. So the checksum is **the whole game** .

**METHOD**

```
18
```

R I D I N G F O R F R E E

## Slide 19

###### **C A S E S T U D Y 0 1**

# RENFE

Spain's national rail. The only thing left guarding the card was a secret.

INTRO OBSCURITY METROFLIP METHOD RENFE CHARLIECARD BARCELONA ETHICS FIX CLOSE
R I D I N G F O R F R E E 19

## Slide 20

###### **T H E T A R G E T**

###### MIFARE Classic, and one secret

CRYPTO1 broke in 2008, memory is wide open The only barrier left is a proprietary checksum The backend hands over **all 32 keys** for any UID No login, no challenge

**RENFE**

```
20
```

R I D I N G F O R F R E E

## Slide 21

###### **O N E M E M O R Y B L O C K**

###### 15 bytes of data, 1 byte of judge

00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 CRC
1 5 DATA BY T E S CHECKSUM

Get that last byte wrong and every validator rejects the block. That byte was the whole security model.

RENFE

```
21
```

R I D I N G F O R F R E E

## Slide 22

###### **W H Y N O T J U S T R E P L A Y A N O L D D U M P ?**

**REPLAY THE OLD STATE RECOVER THE CHECKSUM** Write back a pre-trip dump Modify any field directly Expired dates stay expired Push the expiry to 2035 Rewrite it after every ride One write, valid forever

###### Replays age out. Cracking the checksum does not.

**RENFE**

```
22
```

R I D I N G F O R F R E E

## Slide 23

###### **P H A S E 1 : R U L E O U T T H E O B V I O U S**

**CRC-8**

**LFSR**

**Fletcher**

**Pearson**

**GF(256)**

**weighted sums**

## 2,000,000+

0 **MATCHES**

- 8-bit checksum configs, brute-forced

So the internal state has to be wider than a single byte.

**RENFE**

```
23
```

R I D I N G F O R F R E E

## Slide 24

###### **P H A S E 2 : N A R R O W I T D O W N**

###### Which CRC-16 is it?

Phase 1 ruled out everything 8-bit. So I test each CRC-16 against my real samples, one data-andchecksum pair at a time.

65,796 just 1 CRC-16/X-25
configs fit 6 samples fits all 22 samples poly 0x8408, init 0xFFFF

Every extra sample is one more constraint each config must satisfy, until a single CRC-16 fits all twenty-two.

RENFE

```
24
```

R I D I N G F O R F R E E

## Slide 25

###### **P H A S E 3 : T H E T W I S T**

###### Most samples matched. Six didn't.

I ran CRC-16/X-25 against all 22 samples.

16 of 22 6 of 22
matched outright refused every config
trip history  ·  config  ·  the rest blocks 8  ·  12  ·  13  ·  14

The six were exactly the blocks that hold the balance and the expiry dates. Only the forgeable fields are diversified.

**RENFE** R I D I N G F O R F R E E

```
25
```

## Slide 26

###### **P H A S E 3 : T H E R E L A T I O N S H I P**

###### The six were hiding the UID

|**CARD UID**
**CHECKS**|**UM XOR 0XB1**
**XOR OF THE 4 UID BYTES**|
|---|---|
|**`2E EF 05 12`**
**`0xD6`**|**`0xD6`**|
|**`37 E0 DB 71`**
**`0x7D`**|**`0x7D`**|
|**`B7 00 DC 71`**
**`0x1A`**|**`0x1A`**|
|**`57 BB 0A 6D`**
**`0x8B`**|**`0x8B`**|
|`checksum = CRC16_X25_fold(data)`|`XOR  (UID[0]^UID[1]^UID[2]^UID[3])`|

The UID is broadcast in the clear. The diversification adds zero security.

**RENFE** R I D I N G F O R F R E E

```
26
```

## Slide 27

###### **T H E W H O L E A L G O R I T H M**

15 data bytes CRC-16/X-25 fold to 8 bits XOR the UID 1-byte checksum

```
crc  = crc16_x25(data[:15])          # poly 0x8408, init 0xFFFF
out  = (crc >> 8) ^ (crc & 0xFF)      # high byte XOR low byte
out ^= uid[0]^uid[1]^uid[2]^uid[3]    # per-card; UID is public
```

A proprietary integrity check turns out to be a standard CRC, XORed with a value the card broadcasts in the clear.

- 3 days   ·   about 22 card samples   ·   AI helped

**RENFE**

```
27
```

R I D I N G F O R F R E E

## Slide 28

###### **O N E R E A L E D I T**

###### One byte moves, the checksum follows

||**block**|**13   ·**|**the t**|**itle d**|**ate**||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||`00`|`01`|`02`|`03`|`04`|`05`|`06`|`07`|`08`|`09`|`10`|`11`|`12`|`13`|`14`|`15`|
|**BEFORE**|**`5A`**|**`25`**|`00`|`00`|`60`|`21`|`0F`|`A3`|`56`|`4C`|`0A`|`C1`|`07`|`00`|`00`|**`3D`**|
|**AFTER**|**`DA`**|**`35`**|`00`|`00`|`60`|`21`|`0F`|`A3`|`56`|`4C`|`0A`|`C1`|`07`|`00`|`00`|**`76`**|
||**pass da**|**te   9**|**May**
**→**|**13 Jul**
|**2026**||||||||**che**|**cksum**|**, reco**|**mpute**|

**checksum, recomputed**

Roll the pass forward and bytes 0 and 1 change, so byte 15 no longer matches. I recompute it: fold the CRC-16/X-25 of bytes 0 to 14, then XOR the UID.

same fix on every block I edited **`8   12   13   14   16`**

**RENFE**

```
28
```

R I D I N G F O R F R E E

## Slide 29

###### **W H A T T H A T C O S T S T O P U L L O F F**

€200
HARDWARE

30 sec minimal
PER CARD SKILL NEEDED

Unlimited free travel, and the gate cannot tell.

**RENFE**

```
29
```

R I D I N G F O R F R E E

## Slide 30

###### **D I S C L O S U R E**

###### Disclosed, then shelved

Disclosed to Renfe

Then deadly derailments made travel temporarily free Fare security dropped down the priority list A fix is expected in **a few years**

**RENFE**

```
30
```

R I D I N G F O R F R E E

## Slide 31

###### **T H E M O N E Y G L I T C H C A R D**

###### Boston's CharlieCard

DEF CON 31's Money Glitch was all about this card Same idea as RENFE: a checksum on every block That team cracked it by comparing two different cards It worked, and it took two cards and a lot of math

**CHARLIECARD**

```
31
```

R I D I N G F O R F R E E

## Slide 32

###### **A S I M P L E R P A T H**

###### One card is enough

Their checksum and data modifiers relate two different cards That relationship comes down to the two cards' UIDs The algorithm I found needs **only one card** Feed its UID into the CRC and recompute the block

**CHARLIECARD**

```
32
```

R I D I N G F O R F R E E

## Slide 33

###### **T H E A L G O R I T H M**

###### CharlieCard's checksum, in full

00 01 02 03 04 05 06 07 08 09 10 11 12 13 CRC CRC
14 DATA BYTES 2-BYTE CRC
CRC-16    poly 0x1005    reflected    init 0x3141
input  = the 14 data bytes  +  the 4-byte UID
output = the 2-byte trailer

CHARLIECARD

```
33
```

R I D I N G F O R F R E E

## Slide 34

**P R O O F**

###### Give it a UID, get the trailer

```
$ checksum.py
UID  (4 bytes) : 04 48 5A 35
Data (14 bytes): 00 00 ... 00 05 00 00 00 00
Checksum       : 82 4B
```

Verified against all six known samples. RENFE folds a CRC and XORs the UID; CharlieCard appends it. Every card is its own algorithm.

**CHARLIECARD**

```
34
```

R I D I N G F O R F R E E

## Slide 35

**C A S E S T U D Y 0 2**

### T-Mobilitat

Barcelona went modern. The card you cannot crack.

|**BARCELONA**
INTRO
OBSCURITY
METROFLIP
METHOD
RENFE
CHARLIECARD
ETHICS
FIX
CLOSE
R I D I N G F O R F R E E
`35`|
|---|

## Slide 36

###### **T H E T A R G E T**

###### The card is not the weak point

AES-128, MIFARE DESFire and CIPURSE Keys diversified per card

Secure hardware inside every validator No public breaks in DESFire EV2 or EV3

**BARCELONA**

```
36
```

R I D I N G F O R F R E E

## Slide 37

**S O D O N ' T A T T A C K T H E C A R D**

###### Attack the thing that talks to it

The card is AES-128 and locked You reload trips from your phone That reload path is the **soft way in**

**BARCELONA**

```
37
```

R I D I N G F O R F R E E

## Slide 38

###### **R E A D I N G A P R I V A T E A P I**

T-Mobilitat app mitmproxy ATM backend
APK patched, pinning off every command in the clear none the wiser

Patch the app to drop cert pinning, sit in the middle, and the whole protocol is readable.

**BARCELONA**

```
38
```

R I D I N G F O R F R E E

## Slide 39

###### **Y O U R E L O A D I T F R O M Y O U R P H O N E**

server phone card
trusted untrusted relay trusted

The server trusted whatever the phone reported. It never checked.

**no signature, no read-back**

**BARCELONA**

```
39
```

R I D I N G F O R F R E E

## Slide 40

###### **T H E E X P L O I T : F L I P O N E S T A T U S B Y T E**

normal
card: 91 00 server: trips added
attack
card: 91 00 I swap: 91 AE server: refund

0x91 00 = SUCCESS         0x91 AE = AUTHENTICATION_ERROR

Card keeps the trips. Money comes back. Repeat.

**BARCELONA**

```
40
```

R I D I N G F O R F R E E

## Slide 41

###### **W H Y I T W O R K E D : T H R E E M I S S I N G C H E C K S**

× **No cryptographic binding**

The card's reply is not signed. DESFire supports it; they skipped it.

×

###### **No server read-back**

The server never re-reads the card to confirm what happened.

× **The phone is trusted blindly** Pinning is bypassed, so the report is attacker-controlled.

Solid card crypto, undone by trusting the messenger.

**BARCELONA**

```
41
```

R I D I N G F O R F R E E

## Slide 42

###### **T H E A F T E R M A T H**

Their fix? They killed automatic refunds. For everyone.

After disclosure, I noticed more security and controls going in across the network: inspectors, checks, tighter enforcement.

The response was control, not the architecture fix I recommended.

**BARCELONA**

```
42
```

R I D I N G F O R F R E E

## Slide 43

###### **W H Y D O E S N ' T T H I S G E T P A T C H E D ?**

###### Why can't transit authorities just patch it?

Software patches within hours, whereas transit:

Sometimes just a settings change on the cards Sometimes new card stock entirely

New firmware across thousands of gates

Migrating millions of cards, **spend millions**

**ETHICS**

```
43
```

R I D I N G F O R F R E E

## Slide 44

###### **W H Y P U T T H I S O N A S T A G E ?**

###### The quiet exploiters aren't waiting for a talk

**Organized crime** already sells counterfeit fares Report first, every time Demonstrate the flaw, don't ship a weapon Publish so defenders catch up

**ETHICS**

```
44
```

R I D I N G F O R F R E E

## Slide 45

###### **W H Y D O E S N ' T T H E B A C K E N D C A T C H I T ?**

###### It can. The signals are there.

- A trip counter that only ever climbs

- An expired card still opening gates

The same card in two cities, minutes apart

- A balance that never adds up

**FIX**

```
45
```

R I D I N G F O R F R E E

## Slide 46

###### **B U T O N L Y A T S C A L E**

###### One careful rider is invisible

- A fresh ticket ID every time

Balances that always look plausible Switch stations, switch patterns Every ticket still cryptographically valid

**FIX**

```
46
```

R I D I N G F O R F R E E

## Slide 47

###### **T H E W R O N G F I X**

###### The answer isn't more surveillance

More inspectors punish honest riders And still miss the careful attacker The fix is the architecture, **not more watching**

**FIX**

```
47
```

R I D I N G F O R F R E E

## Slide 48

###### **T H E R E A L F I X : C A R D - B A S E D V S A C C O U N T - B A S E D**

CBT

###### **Card-Based Ticketing**

value lives on the card (today)

###### **P R O S**

- **+** fast: one tap, no backend needed

- **+** can be secure, in theory

C O N S

- all security rides on the card

- one crypto or app-layer slip breaks it

###### ABT

###### **Account-Based Ticketing**

card holds a secure token (the future)

###### **P R O S**

- **+** card holds a token, nothing to forge

- **+** gate opens offline, fare settles later

C O N S

- needs backend accounts and settlement

- risk moves to the cloud: APIs, fraud

**FIX**

```
48
```

R I D I N G F O R F R E E

## Slide 49

**W H E R E I T ' S H E A D E D**

###### The fight moves to the cloud

No balance on the card, no physical hack It becomes an API and account-fraud problem But migrating costs a fortune So real change is years away, not months

**FIX**

```
49
```

R I D I N G F O R F R E E

## Slide 50

The world's transit runs on assumptions nobody tested. So I checked.

Metroflip is open because this belongs in the open. `github.com/luu176`

**CLOSE** `50`

R I D I N G F O R F R E E

## Slide 51

###### **W I T H T H A N K S**

###### None of this was solo

My mom My dad My girlfriend Scarlett Gabriel Grigor Equip Torron Willy Randy

Prometheus

The BreakMeIfYouCan team All of The Pirates' Plunder group

**CLOSE** `51`

R I D I N G F O R F R E E

## Slide 52

### Demo  -  Renfe

```
52
```

R I D I N G F O R F R E E

## Slide 53

**Y O U R T U R N**

#### CTF

A NIMBUS TRANSIT fare card lands in your reader.

1 KB of MIFARE Classic.

Some of its blocks end in a single checksum byte the validators trust. Nobody published the format.

So you'll reverse it.

Play it live **`ridingforfree.live`**

scan to play

**CLOSE** `53`

R I D I N G F O R F R E E

## Slide 54

###### **T H A N K Y O U**

##### Aidan Nakache

```
luu176   ·   github.com/luu176   ·   Metroflip
```

prior work & credit Dismantling MIFARE Classic (2008)  ·  Boston Money Glitch (DC31)  ·  Unsaflok (DC32) BreakMeIfYouCan, Ultralight 3DES/AES (eprint 2026/100) Metrodroid  ·  Proxmark3  ·  ChameleonUltra

**connect on LinkedIn**

**CLOSE** `54`

R I D I N G F O R F R E E
