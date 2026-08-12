---
title: "Shuffle Up and Deal Analyzing the Security of Automated Card Shufflers"
speakers: ["Joseph Tartaro", "Enrique Nissim", "Ethan Shackelford"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/Joseph Tartaro & Enrique Nissim & Ethan Shackelford_Shuffle Up and Deal Analyzing the Security of Automated Card Shufflers.pdf"
pages: 69
sha256: "d786287f5a9a8ef032e296f1829cef8d2f436e257c002e13b7755b3768fe628d"
text_chars: 26018
ocr_pages: 11
has_ocr: true
redacted_secrets: 0
ocr_confidence: 90.2
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:11:59Z"
---
# Shuffle Up and Deal Analyzing the Security of Automated Card Shufflers

**Speakers:** Joseph Tartaro, Enrique Nissim, Ethan Shackelford  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Joseph Tartaro & Enrique Nissim & Ethan Shackelford_Shuffle Up and Deal Analyzing the Security of Automated Card Shufflers.pdf` (69 pages)


## Slide 1

# Shuffle Up and Deal Auditing the Security of Automated Card Shufflers

- ♤ Joseph Tartaro

- ♡ Enrique Nissim ♧ Ethan Shackelford ♢

#BHUSA  @BlackHatEvents

## Slide 2

### Introduction

Joseph Tartaro

Enrique Nissim

Ethan Shackelford

###### Embedded Security Consultants at **IOActive**

- Low-level code review

- Reverse engineering (Operating Systems, Drivers, Firmware)

- • Specialized tooling development

#BHUSA @BlackHatEvents

## Slide 3

### What and Why?

- Hustler Live Cheating Scandal

   - Suspicious play occurs with accusations of cheating

   - • Independent investigators hired

#BHUSA @BlackHatEvents

## Slide 4

### What and Why?

• Investigators Focus Areas

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
What and Why?
¢ Investigators Focus Areas
Table 1: Examined Areas
Potential Attack Vectors Estimated Priority Estimated Complexity
Table Low Complex
RFID None Highly Complex
Card Shuffler Highly Complex
Production Booth and Operations
Network, PC Workstations,
And Systems
Communications | Medium | Complex
```

## Slide 5

### What and Why?

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 84/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Sho}
cate
ShuffleMaster Card Shuffler Deckmate One / Deckmate 1
v | Q Search for anything
All Categories
Shuffler
Shipping: FREE Standard Shipping | see<etaiis
Located in: Los Angeles, California, United State:
Shipping:
Delivery: Estimated between Tue, Oct 18 and Thu, Oct 20 to 90274 ©
Hover to zoom Returns: Seller does not accept returns | see details Delivery:
Payments:
PayPal CREDIT
“$288.04 for 24 months. Minimum purchase required. |
Have onetosell? Sell now See terms and apply now
Earn up to 5x points when you use your eBay Mastercard ®.
Learn more
Ships from United States
<8 Listed incategory: Collectibles > CasinoCollectibles > Collectible Casino Card Shuffiers
Condition: Used
o . ” ShuffleMaster Card Shuffler Deckmate Two / Deckmate 2
fully reconditioned, working like brand new. Shuffler
Quantity: [1 3 available / 3 sold
ie | Condition: Used
“fully reconditioned, working like brand new.”
Price: US $6,000.00 Buy ItNo\ | Quantity: [1 | Saveilable
$289 for 24 months with “
PayPal Credit* f
$409 for24 months with
( QO Add to Watchlist 4 PayPal Credit”
2 Add to Watchlist )
Ships from United States 7 watchers
6watchers
FREE Standard Shipping |
Estimated between Mon, Oct 17 and Thu, Oct 20 to 90274 @
Sellerdoes not accept returns |
PayPo! CREDIT
"$408.06 for 24 months. Minimum purchase required. |
See terms and apply now
Earn up to §x points when you use your eBay Mastercard ®.
rn more
```

## Slide 6

### What and Why?

- ShuffleMaster Deck Mate Series

- Most popular automated shufflers

- Used across the world in casinos, card rooms and home games

- Official shuffler of the World Series of Poker (WSOP)

#BHUSA @BlackHatEvents

## Slide 7

### What and Why?

###### Deck Mate 1

- Single Deck Shuffler

- Detects missing / additional cards

###### Deck Mate 2

- Single Deck Shuffler

- Detects missing / additional cards (w/ details)

- Shuffles significantly faster than DM1

- Supports remote management via network

- Supports external display module

- Player clock feature

#BHUSA @BlackHatEvents

## Slide 8

### Demo

#BHUSA @BlackHatEvents

## Slide 9

### Attack Scenarios

#BHUSA @BlackHatEvents

## Slide 10

### Maintenance Employees

• Extremely complex

- Contains

   - Rubber belts

   - Sensors

   - Motors

- Requires

   - Regular maintenance

   - Contractual service agreements

#BHUSA @BlackHatEvents

## Slide 11

### Gaming Operator Employees

- Casino Employees / Device Operators

- • Unrestricted access to shufflers

- Access to exposed external ports

- Manager/Operator

- • Dealer

- Chip Runner

- • Security

-

...

#BHUSA @BlackHatEvents

## Slide 12

### Attacker at Poker Table (DM2)

###### • Shuffler cutouts in table

- External interfaces exposed to players

- Ethernet, USB, Power

#BHUSA @BlackHatEvents

## Slide 13

### Attacker with Network Access (DM2)

- Various network services

- Unnecessary attack surface

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Attacker with Network Access (DM2)
¢ Various network services
¢ Unnecessary attack surface
scan initiated Tue Nov 8 18:16:17 2022 as: nmap -sV -p- --open -oA nmap-deckmate2 169.254.0.1
90rt for 169.254.0.1
9 closed tcp ports (conn-refused)
VERSION
open s Dropbear sshd 9.53.1 (protocol 2.0)
open telnet BusyBox telnetd
open C lighttpd
open netbios-ssr smbd 3.X - 4.X (workgroup: WORKGROUP)
open netbios-ssn a smbd 3.X - 4.X (workgroup: WORKGROUP)
open X11 (acc enied)
ice Info: Host: shuffler; inux, Unix; CPE: cpe:/o: linux: Linux_kernel
Service detection performed. Plea results at https://nmap ‘submit/
# Nmap done at Tue Nov. 8 18:16:35 2022 = (1 host up) scanned in 18.73 seconds
```

## Slide 14

#### Attacker with Cellular Network Access (DM2)

- Documents identified during research suggest the cellular modem can be used for pay-per-shuffle rental of shufflers

- No firewall or network or iptables rules prevent Ethernet/USB network services from also being exposed on the cellular interface

#BHUSA @BlackHatEvents

## Slide 15

### Casino Architecture and Standards

#BHUSA @BlackHatEvents

## Slide 16

### Modern Casino Floor

- The International Gaming Standards Association (iGSA) is the entity responsible for the standards implemented across the gaming industry.

- Different types of specifications

   - Communication

   - Regulatory

- G2S

- S2S

IGSA Unleash the Power of Your Floor, 3rd edition

#BHUSA @BlackHatEvents

## Slide 17

### Gaming to System (G2S)

- Standardizes communications between gaming devices and management systems

- Asynchronous XML based messages

- TCP (with optional SSL) and other IP protocols for transport

- P2P and Multicast

#BHUSA @BlackHatEvents

## Slide 18

### G2S Classes

G2S define classes of functionality a device can implement

- _communication​_

- _cabinet​_

- _optionConfig_

- _download​_

These classes relate to specific functions or features of the EGM, e.g. meters, cabinet, jackpots, vouchers, etc.

- _eventHandler_

- _meters​_

- _gamePlay_

- _deviceConfig_

   - _handpay_

   - _coinAcceptor_

   - _noteAcceptor_

   - _commConfig_

- _printer_

   - _player_

- _progressive_

   - _voucher_

- _idReader_

   - _wat_

- _bonus_

   - _gat_

- _hopper_

   - _central_

- _noteDispense_

#BHUSA @BlackHatEvents

## Slide 19

### Game Authentication Terminal

- This class provides a set of commands that regulators can use retrieve errors logs and authenticate EGMs and peripherals

   - Serial GAT

   - Network GAT

- Permits ensuring the software running on devices has not been modified

- GAT does not define or require a particular authentication algorithm

Establish communication with device

OS
Request list of components for
Software
authentication
Peripheral
SHA1-HMAC
Request authentication for
CRC-32
component
Offsets

#BHUSA @BlackHatEvents

## Slide 20

### Serial GAT and Network GAT

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Serial GAT and Network GAT
Slot Floor Operator/Casino Backend Remote, Offsite Access
(via Internet)
Regulator
laptop
Regulator or checking Regulator
Operator server office PC
directly performing
checking EGM S remote audit
H RS232 or USB
! RS232 or USB Ethernet
VPN with
Firewall
Ethernet Ethernet Ethernet
```

## Slide 21

### GAT Protocol

###### Application Layer

|**Command**|**Length**|**Message Data**|**CRC**|
|---|---|---|---|
|1 Byte|1 Byte|0 - 251 Bytes|2 Bytes|

###### Commands in GAT

|**Request**|**Description**|**Response**|**Description**|
|---|---|---|---|
|0x01 SQ|Status Query|0x81 SR|Status Response|
|0x02 LASQ|Last Authentication Status Query|0x82 LASR|Last Authentication Status Response|
|0x03 LARQ|Last Authentication Results Query|0x83 LARR|Last Authentication Results Response|
|0x04 IACQ|Initiate Authentication Calculation Query|0x84 IACR|Initiate Authentication Calculation Response|

#BHUSA @BlackHatEvents

## Slide 22

### GAT – IACQ Get File

Master EGM / Peripheral
IACR - Acknowledged – Calculation started
SR (Status Response): Calculating
SR: Calculation Finished
LARR: [Authentication Result]

#BHUSA @BlackHatEvents

## Slide 23

GAT Requires Transaction Logs to be G2S compliant

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 96/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
GAT Requires Transaction Logs
to be G2S compliant
Chapter 23
G2S™ Message Protocol v1.0.3 gat Class
23.2 Transaction Logs
Within the gat class, the EGM MUST store critical data related to GAT accesses and responses in persistent
memory. This data is designed to provide an audit trail of all actions related to GAT devices. Log entries
MUST be generated for GAT actions initiated by devices local to the EGM, such as through an RS232
connection, as well as GAT actions initiated by host systems. See Chapter 1 for more details on
transaction logs.
```

## Slide 24

### GAT Security

- The GAT authentication is inherently flawed: relies on the response the EGM or Peripheral hands it (which could be compromised)

- There is no mention of Public Key Infrastructure in the G2S and GAT specifications

- The algorithms defined for authentication are cryptographically weak or not suitable for cryptographic purposes: HMAC-SHA1, CRC16, CRC32

- The HMAC-SHA1 algorithm provide some randomness to the process, but nothing more

#BHUSA @BlackHatEvents

## Slide 25

### Shufflers and GAT

#BHUSA @BlackHatEvents

## Slide 26

###### DM1

- It does not implement any GAT concept

- Modified firmware cannot be easily detected

- It features "History Logs" but these are not G2S Transaction Logs

#BHUSA @BlackHatEvents

## Slide 27

###### **`Get Special Functions Result`**

###### DM2

- It features a HMAC-SHA1 Authentication

- Serial GAT only

- • No transaction records of GAT accesses

\```
Feature: Get File
 Parameter: AuthenticationResponse.xml
 Parameter: %%SHA1_HMAC%%
Feature: Component
 Parameter: DeckMate2_UI_2.0.254
 Parameter: %%SHA1_HMAC%%
Feature: Component
 Parameter: DeckMate2_CardRec_5.0.023
 Parameter: %%SHA1_HMAC%%
Feature: Component
 Parameter: DeckMate2_NXP_NXP 1.0.172
 Parameter: %%SHA1_HMAC%%
Feature: Component
 Parameter: DeckMate2_Games_1.0.095
 Parameter: %%SHA1_HMAC%%
\```

#BHUSA @BlackHatEvents

## Slide 28

#### IACQ Get File AuthenticationResponse.xml

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
IACQ Get File AuthenticationResponse.xml
<?xml version='1.0'?>
<Components GatExec='default'>
<Game>
<Name>Deck Mate 2</Name>
<Manufacturer>Bally Technologies</Manufacturer>
<Component>
<Checksum>32A66E4EAFB35AE6DC51268104111118377EE254</Checksum>
</Component>
<Component>
<Checksum>2EA4D5A836604B7676D7C7EB3EA8BEC84B410903</Checksum>
</Component>
<Component>
<Name>DeckMate2_Games_1.0.095</Name>
<Checksum>39FF668A8BEE8B19E72A7DED15F4B043A1D2DE2B</Checksum>
</Component>
<Component>
<Name>DeckMate2_NXP_NXP 1.@.172</Name>
</Component>
</Game>
</Components>
```

## Slide 29

###### Deck Mate 1

#BHUSA @BlackHatEvents

## Slide 30

#BHUSA @BlackHatEvents

## Slide 31

### Reverse Engineering DM1

- Goals: understand operation, RNG and shuffling algorithm

- The ROM code was extracted from the M27C512 EEPROM

- The MCU is AT89S53 (Intel 8051). Old 8-bit architecture. Fun to reverse

- Bare Metal. No symbols, no debug information

#BHUSA @BlackHatEvents

## Slide 32

### Setup Menu

- Set Game Type

   - Poker

   - Blackjack single deck

   - Blackjack double deck

- Set number of cards

- Set time

- Set date

- Configure delay after platform drop

- Read serial number

- Read total cycles

- Read reset cycles

- Reset history logs

- Re-Seed RNG

#BHUSA @BlackHatEvents

## Slide 33

### Timer Interrupt Setup

- Shuffler Xtal is 11.0592 MHz

- Configures 8051 Timer0 to Mode1 (16-bit mode)

- Sets TH0|TL0 to 0xFF1E, to interrupt every ~245us

- A TIMER_TICK variable is incremented on each interrupt

#BHUSA @BlackHatEvents

## Slide 34

### RNG

\```
voidreseed_rng() {
 UINT32 *seed = XRAM_014Dh;
 *seed = 0;
 for (inti= 0;i< 4;i++ ) {
 // Wait for green button input
 BYTEtimer_count= XRAM_151_TimerTick;
 *seed = *seed | (((UINT32)timer_count) << 8 * i);
 }
}
\```

GenerateRandomDeck()
GetRandom(min, max)
GetNextSeed()

###### **_`Seed = 0x19660d * seed + 0x3c6ef35f`_**

#BHUSA @BlackHatEvents

## Slide 35

### Shuffling Algorithm

1. Cards are physically loaded into the first compartment

2. Based on the configured game settings, the algorithm expects a specific number of cards. For Poker, this number is 52

3. A new deck configuration is randomly generated.

   - a. This is represented by an array of numbered positions.

   - b. This also indicates how many cards the set of grippers should grip at each step

4. Shuffling starts => the deck configuration is "executed". Cards are placed into the correct location one at a time starting from the bottom of the deck

5. Upon error-free completion, the shuffled deck becomes available

#BHUSA @BlackHatEvents

## Slide 36

### Cheating with DM1

Due to the limitations in the hardware architecture of the DM1, if a bad actor has internal access to the device, they can flash or replace the EEPROM chip and the MCU will simply execute the code.

AT89S53 MCU do not support secure boot

DM1 does not support GAT => there is no trivial way for an auditor to detect a modified EEPROM.

#BHUSA @BlackHatEvents

## Slide 37

### Bypassing Card Count Detection

The DM1 keeps track of the number of cards that were fed into the shuffling compartment.

This permits the detection of missing or extra cards.

By manipulating the firmware, an attacker can alter the code logic to avoid failing when too few or too many cards are processed.

This would allow an attacker at the poker table to keep an ace back (hidden up their sleeve) and the dealer would shuffle a deck of only 51 cards without being alerted

#BHUSA @BlackHatEvents

## Slide 38

### Partial Deck Order Knowledge

Following the way the shuffling algorithm works, a compromised device could place specific cards into known locations with the help of the dealer.

###### **_[0, 9, x2, x3, x4, x5, x6, x7, x8 …]_**

This could be concealed by for example, requiring the dealer pressing the green button N times before inserting the deck.

#BHUSA @BlackHatEvents

## Slide 39

### False Shuffles

The device could be configured to perform false shuffles periodically or after a rogue dealer presses a button sequence before the shuffle. The dealer can keep the deck in the state as after the previous hand and the cheater will be aware of the previous flop, turn, and river cards, as well as their hands, which would be on top of the deck.

**_[51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]_**

Given this knowledge, upon the deck is cut by the dealer, those known cards could be considered dead, giving the cheater a significant edge.

#BHUSA @BlackHatEvents

## Slide 40

###### Deck Mate 2

#BHUSA @BlackHatEvents

## Slide 41

###### Reverse Engineering DM2

- Goals: understand operation, RNG and shuffling algorithm

- Display Board firmware extracted via dumping unencrypted NAND

   - CPU is i.MX28 NXP ARM CPU

   - Linux 2.6.35.3

- Control Board firmware extracted from Display Board updater

   - MCU is NXP LPC1769 cortex-m3

   - QP/C Real Time Embedded Framework

- No symbols, no debug information

#BHUSA @BlackHatEvents

## Slide 42

###### DM2 System Architecture

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
DM2 System Architecture
Deck Mate 2
Display Module
Control Board
Interaction UART listener ha UART
Logic es
Control Board
Transmits shuffle and card information
Network Services to the Display module
USB
ETH | anpis
Controls physical shuffling
```

## Slide 43

##### Display Board

- Reach Technology touchscreen display development module

- Embedded Linux Environment

- Responsible for connecting user interface (buttons, screen) to Control board

- • Hosts various network services, used during operation and for maintenance

- Ethernet and USB RNDIS for networking

#BHUSA @BlackHatEvents

## Slide 44

##### Display Board Network Services

|**Port**|**Service**|**Description**|
|---|---|---|
|22|ssh|Secure Shell, used for remote display|
|23|telnet|Telnet, unused|
|80|http|Configuration Web Server|
|139|SMB|SMB server, no shares|
|445|SMB|SMB server, no shares|
|6000|X11|X11 Remote display server|

#BHUSA @BlackHatEvents

## Slide 45

##### Display Board: Initial Foothold

- USB and Ethernet both expose network services – primary initial attack surface

- SSH and Telnet – Linux login prompt (no creds yet)

- SMB – No shares available

- Configuration web server requires creds, only one low-priv set available at outset

#BHUSA @BlackHatEvents

## Slide 46

##### Display Board: Initial Foothold

- Need more information for network attack surface, get physical

- Reach Technology Display module can be booted from NAND or SD Card

- Built OS image with known creds, booted from SD

- Dump on-board NAND flash with Shuffler Firmware

#BHUSA @BlackHatEvents

## Slide 47

##### Display Board: OS Review

- No real privilege separation

- Significantly outdated Linux kernel

\```
$ time john --format=md5crypt remote-root.hash
Using default input encoding: UTF-8
Loaded 1 password hash (md5crypt, crypt(3) $1$ (and
variants) [MD5 128/128 AVX 4x3])
Will run 80 OpenMP threads
\```

\```
Proceeding with single, rules:Single
\```

- Weak, hardcoded, universal system passwords

- SSH and Telnet unrestricted beyond login prompt, login as root permitted

- No Secure Boot, filesystem integrity

\```
root:$1$<redacted>:0:0:99999:7:::
daemon:*:14250:0:99999:7:::
sshd:*:0:0:99999:7:::
ftp::0:0:99999:7:::
\```

\```
Press 'q' or Ctrl-C to abort, almost any other key
for status
\```

\```
Almost done: Processing the remaining buffered
candidate passwords, if any.
Proceeding with
\```

\```
wordlist:/usr/share/john/password.lst, rules:Wordlist
Proceeding with incremental:ASCII
\```

\```
<redacted> (root)
1g 0:00:08:59 DONE 3/3 (2023-08-04 10:58) 0.001851g/s
799083p/s 799083c/s 799083C/s 3KDYL..411s5
Use the "--show" option to display all of the cracked
passwords reliably
Session completed
\```

\```
john --format=md5crypt remote-root.hash 41246.77s
user 15.83s system 7630% cpu9:00.76 total
\```

#BHUSA @BlackHatEvents

## Slide 48

##### Display Board: Software Update Security

- Weak update authentication – faulty SHA1 logic and authentication key same as encryption key

- Hardcoded, universal encryption/authentication key

- Update format (self extracting bash script) easily exploitable for code execution as root

- IOActive extracted key and logic for encryption/authentication from on-board utility

- Developed a tool for creating arbitrary cryptographically valid firmware updates

#BHUSA @BlackHatEvents

## Slide 49

##### Display Board: Configuration Web Server

- Hardcoded, universal credentials for all accounts including web superuser

• Credentials embedded in plaintext in service binary

#BHUSA @BlackHatEvents

## Slide 50

###### Control Board System Review

- No Secure Boot Implemented

- Code Read Protection not enabled (ISP/JTAG possible)

#BHUSA @BlackHatEvents

## Slide 51

###### Control Board Architecture – QP/C and Events

- QP/C: Real Time Embedded Framework

   - "Active Object" model of Computing

   - Event-based

   - **Open source**

#BHUSA @BlackHatEvents

## Slide 52

###### Identifying Active Objects

###### **Pattern Matching**

- main identified

- Calls to QActive_start_ are passed ActiveObject references

- xrefs lead to __initial_ functions for each object

- __initial_ functions contain event subscriptions and _Root_events_ function pointer

- 16 Active Objects identified

#BHUSA @BlackHatEvents

## Slide 53

###### Random Number Generation

###### **Questions to Answer:**

- Hardware or Software?

- How is entropy sourced?

- What seed?

- What PRNG algorithm?

#BHUSA @BlackHatEvents

## Slide 54

###### Random Number Generation

###### **Entropy**

- RITimer -> Repetitive Interrupt Timer

- 32 bit counter, counts from 0 to 0xffffffff

- Configurable tick rate, division of system clock

- By default, equals clock rate

- NXP LPC1769 clock max @ 120MHz

A single poll of the RITIMER counter value not sufficient for entropy – timing may be constant if _SeedRNG_ called at fixed time after boot.

SeedRNG _seed_status_ maintaned across multiple calls, and timer queried twice. Delay between calls variable, dependent on whims of QP/C Scheduler

Delays on the order of tens of nanoseconds will affect the final seed value

#BHUSA @BlackHatEvents

## Slide 55

###### Random Number Generation **PRNG Algorithm**

- Magic constants _0x19660d_ and _0x3c6ef35f_

- Parameters found in _Numerical Recipes_ by D. Knuth and H. W. Lewis, in common use

- Used as _multiplier_ and _increment_ for Linear Congruential Generator

###### **Linear Congruential Generator Security**

- LCG output considered to be sufficiently random for non-cryptographic applications

- Acceptably unpredictable for this specific application, without knowledge of initial seed and iteration count

- Same PRNG as the Deck Mate 1

#BHUSA @BlackHatEvents

## Slide 56

###### Shuffling Algorithm

- Constructs an array _target_positions_ equal to size of inserted deck

- Each index in array represents a card in the unshuffled deck

- Populates this array with _target position_ values

- Each card in unshuffled deck at position _i_ is placed at position _target_positions[i]_ in the shuffled deck

- Similar to Deck Mate 1 randomization

#BHUSA @BlackHatEvents

## Slide 57

###### Physical Shuffling Mechanism

#BHUSA @BlackHatEvents

## Slide 58

###### Shuffler Mode

- Multiple modes supported

- • Normal Shuffle

- Sort: multiple modes for different suit orders

- Sort mode reads card data from camera for placement information.

- Normal Shuffle reads order information from virtual deck, card values in physical deck irrelevant (though still read and recorded).

#BHUSA @BlackHatEvents

## Slide 59

###### Cheating with DM2

#BHUSA @BlackHatEvents

## Slide 60

###### Cheating with DM2: Deck Order Manipulation

- Repurpose the DM2 Camera to identify each card and place it in a target location

- • This allows for "sort" mode, where cards are placed in a specific order

- Modifying Control Board firmware allows for cheater-specified sort order

- Dealer will usually cut deck, disrupting intended order

- Deck orders which allow for the cheater to win consistently are suspicious

- Requires cheater to be in a specific seat

#BHUSA @BlackHatEvents

## Slide 61

###### Cheating with DM2: Exfiltrating the Deck

- Use the Camera to read the current card being shuffled and exfiltrate it.

- Control Board firmware can be modified so that this information is reported to the Display board over UART

- Cheater-controlled device connected to the Display Board extracts this data

- Order of deck post-shuffle can be transmitted to the cheater

- Deck order is not modified and thus avoids suspicion

- Deck cut can be accounted for

- Does not attempt to force a win but rather increase odds for cheater, thus no specific seat or game configuration is necessary

#BHUSA @BlackHatEvents

## Slide 62

###### Cheating with DM2: Proof of Concept

###### Attack Scenario: Cheating player

###### Vulnerabilities Leveraged

- SSH exposed over USB/Ethernet/Cellular

- Hardcoded Display Board root credentials

- Incomplete GAT implementation

- Lack of firmware update security for Control Board

- Lack of secure boot for Control Board

- Lack of filesystem integrity protections for Display Board

- Inadequate physical security for Deck Mate 2 device and enclosure

- Inadequate physical access restrictions/monitoring in common deployment

###### Equipment

- Raspberry Pi Zero W

- Android Phone

#BHUSA @BlackHatEvents

## Slide 63

###### Cheating with DM2: Exfiltrating Deck Information via Bluetooth

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Cheating with DM2: Exfiltrating Deck Information via Bluetooth
Deck Mate 2
Display Module
Label
| Control Board
running firmware modified to report:
Network service
TCP port 8838 « Gard position post-shuffle
Android Application ¥ ¥ + Suit
USB
ETH | RNDIS
Results Display
Raspberry
Shuffler log parser Pi Zero
Poker Hand Configuration
Solver ul
Bluetooth Low Energy
BLE GATT
```

## Slide 64

###### Cheating with DM2: Exfiltrating Deck Information via Bluetooth

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
> Generic Access
Generic Attribute
houdini a
E E
> Generic Access
> Generic Attribute
> Device Information
read notify
Client Characteristic Configuration
Characteristic Extended Properties
Characteristic User Descriptor
Configure Game
Player Count
4
Player position
A
Deck Cut @
Dealer Distance
Hand
Card 1
2@
7@
Card3
Flop
4
12:30 @
vo
Winner Winner Chicken Dinner
$1 - One pair: [2H, 2C, AS, QD, JS]
$4 - One pair: [2H, 2C, KD, JS, 8S]
$3 - One pair: [2H, 2C, JS, 10D, 7H]
$2 - One pair: [2H, 2C, JS, 8D, 7H]
```

## Slide 65

### Conclusions

#BHUSA @BlackHatEvents

## Slide 66

###### Impact

- Automated shufflers and gaming standards sport surprisingly weak security given the high-stakes nature of their purpose

- Research focused on Poker, but similar shufflers are used in other table games such as Blackjack and Baccarat and incur losses to gaming operators

- Overall, cheating scenarios like this affect players trust in the integrity of the game, without trust there is no game

#BHUSA @BlackHatEvents

## Slide 67

###### Recommendations

###### Gaming Operators

- Implement physical restrictions on access to exposed ports

- Leverage relationship with manufacturer to directly address concerns

- Players

- Ultimately boils down to your trust in the operator/game

#BHUSA @BlackHatEvents

## Slide 68

###### Recommendations

#BHUSA @BlackHatEvents

https://twitter.com/DougPolkVids/status/1529976301536280576


> Recovered by OCR — confidence 96/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Recommendations
https://twitter.com/DougPolkVids/status/1529976301536280576
Doug Polk @
| have heard of MANY different occasions where this tactic was used to
cheat players. In home games, in clubs, and even at least once at a major
casino. There are countless times this has been used to swindle people out
of their money.
Doug Polk @
It is far more likely that players use the knowledge of deck order to cheat
than sort the deck into rigged hands. Cutting the deck does nothing, as
once you know 1 card location you know where it was cut and thus the
entire order.
Doug Polk @
The main ways that this information is relayed to in game players is via ear
piece or their mobile device. | dont know the exact specifics of that
transmission.
Wanted to clear up these common misconceptions I'm seeing regarding
using the shufflers to cheat.
Doug Polk @
Oh 1 last thing.
If you are ever worried ask for the dealer to riffle a few times at the end. With
a few riffles its basically impossible to use this technique to cheat.
```

## Slide 69

## Questions?

A detailed whitepaper will be available in the new few weeks Thank you

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
USA &
AUGUST 9-10, ©0253
BRIEFINGS
Questions?
A detailed whitepaper will be available in the new few weeks
Thank you
lOActive.
#BHUSA @BlackHatEvents
```
