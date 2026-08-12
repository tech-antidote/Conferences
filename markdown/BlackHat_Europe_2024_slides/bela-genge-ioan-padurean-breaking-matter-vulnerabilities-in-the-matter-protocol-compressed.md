---
title: "Breaking Matter Vulnerabilities in the Matter Protocol"
speakers: ["Bela Genge", "Ioan Padurean"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2024"
edition: "Europe"
year: 2024
source_pdf: "BlackHat_Europe_2024_slides/Bela Genge & Ioan Padurean_Breaking Matter Vulnerabilities in the Matter Protocol_Compressed.pdf"
pages: 92
sha256: "56f1791b0c0e675a64f7b233d86ecdb59a88e8bfdb3d45fcb682decb28a3f51a"
text_chars: 40286
ocr_pages: 21
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:01:31Z"
---
# Breaking Matter Vulnerabilities in the Matter Protocol

**Speakers:** Bela Genge, Ioan Padurean  
**Conference:** Black Hat Europe 2024  
**Source:** `BlackHat_Europe_2024_slides/Bela Genge & Ioan Padurean_Breaking Matter Vulnerabilities in the Matter Protocol_Compressed.pdf` (92 pages)


## Slide 1

# Breaking Matter: Vulnerabilities in the Matter Protocol

Speaker: Béla Genge Contributor: Ioan Pădurean

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
= acral Vii =* 74
— EWROPE 20 “~
DECEMBER 11-12, 2024 | _ yore
Breaking Matter: Vulnerabilities ir in
the Matter Protocol
Speaker: Bela Genge
Contributor: loan Padurean
#BHEU @BlackHatEvents
```

## Slide 2

### Béla GENGE

Senior Security Researcher @ Research on Matter for ~two years University teaching / research background for ~20 years <u>bgenge@bitdefender.com</u>

## Slide 3

# AGENDA

- Intro & motivation

- Background on Matter protocol

- • Security findings • Way forward

## Slide 4

## Modern world is about automation

###### **Smart Factory**

###### **Smart Home/Building**

**4**<sup>**th**</sup> **industrial revolution INDUSTRY** **~~4.0~~ 5.0 Digital Transformation**

**<accepting applications for cool buzzwords>**

## Slide 5

## Modern home is connected

#### **Inverter**

#### **Solar panels**

EV Charging

**Smart battery**

**Heat pump**

**Not isolated but connected to the power grid!**

## Slide 6

## Traditional IoT ecosystem

**IPv4/v6 to Z-Wave / ZigBee / ... Border Router** A A C D

B

B

Information Classification: General

#BHEU @BlackHatEvents

## Slide 7

## IoT ecosystem: Attacker's perspective

CVE b CVE c
CVE d
CVE a

Information Classification: General

#BHEU @BlackHatEvents

## Slide 8

## (Attacker’s) Life is about to get easier

**Interoperability through industry-unifying standard**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 9

## Matter: the beginning

- December 2019: Work Group on Connected Home over IP

- CSA: **Connectivity Standards Alliance**

- Provides a secure and interoperable solution

Secure

Source: <u>https://bytebeam.io/blog/what-is-the-matter-protocol/</u>

IPv6 Open

Interoperable Multi-admin

Established protocols

Information Classification: General

#BHEU @BlackHatEvents

## Slide 10

## Shift in communication

<u>Understanding Matter (1.0) and its Significance (bytebeam.io)</u>

Information Classification: General

#BHEU @BlackHatEvents

## Slide 11

## Thread anyone?

- IPv6-based protocol for low-power, mesh networks

- • It uses 6LoWPAN on top of IEEE 802.15.4 wireless protocol

Thread
Border Router

HTTP, CoAP, MQTT, ...
DTLS
UDP
Distance Vector Routing
6LowPAN (IPv6)
IEEE 802.15.4

Information Classification: General

#BHEU @BlackHatEvents

## Slide 12

## Matter: today

- Global collaboration ( **600+** ):

   - 32 promoters

   - 284 participants

   - 288 adopters

- Device certification programs aligned with several directives

**Matter is becoming the (single?) established standard for IoT**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 13

## Matter: versions

Dec. 2019   Oct. 2022 May 2023   Oct. 2023 May 2024     Nov. 2024

Amazon, Apple, **v1.0: v1.1: v1.2: v1.3: v1.4:** - - - - - Google, Samsung Lighting: power Bug fixes Refrigerators Water **Home Router** - - SmartThings and plugs, electric Enhanced SDK Portable air conditioning management **Access Point** - - - the Zigbee Alliance lights, switches API Dishwashers **Energy Solar Power** - - - Door locks Laundry washers **management Batteries** - - - - Thermostats Robotic vacuum **Electric Vehicle Heat Pumps** - - Heating cleaners **Charging Water Heaters** - - - - Ventilation Monoxide alarms Microwave ovens Enhancements - - - Air conditioning Air quality sensors Ovens - - - Blinds & shades Air purifiers Cooktops - - - Motion sensors Fans Extractor hoods - - TV Laundry dryers - - Video games Media players

Information Classification: General

#BHEU @BlackHatEvents

## Slide 14

## Matter: latest news

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Matter: latest news ae ah
blackhat
EUROPE 2024
BLOGS
Matter: Enabling Universal Grid-Friendly Integration press reveases
Energy Smart Appliances and more
Matter 1.4 Enables More Capable Smart Homes
10/1/2024 11/7/2024
; ; Enhanced Network Infrastructure with Home Routers and Access Points
Matter: Enabling Universal 5 & be (HRAP)
Grid-Friendly Integration for Energy ~
Smart Appliances and more Tl \ wy New Energy Device Types and Capabilities
“Tr ote” | | oe
ait Tater re man ™ . ie
CSa m"| az matter = —
LO _----)
=r >
Information Classification: General
```

## Slide 15

## Matter: attacker's perspective

Find (vulnerability) Once, Run Everywhere!

Information Classification: General

#BHEU @BlackHatEvents

## Slide 16

## Matter: my perspective

(2024)

(2024)

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Matter: my perspective < blackhat
WIP: Security Vulnerabilities and Attack Scenarios
in Smart Home with Matter (2024)
“Research
MATTER?...
by Larry Pesce-| © 10 TF — | (@ Mar 27, 2023:2:47:16.PM
~
WHERE IS VERYBOD\) 7 Risks in AiDot-Controlled Matter Devices
(2024)
' Seamlessly Insecure: Uncovering Outsider Access
mDNS in action with the home
automation Matter protocol
Real life example of mDNS being used to find and add devices toa
home automation network.
@ ~=—~Paul Otto - Follow
BS otminread
Information Classification: General
```

## Slide 17

## First questions

**130 million batteries will be both manufactured and disposed of every single day by 2025.** <u>https://cordis.europa.eu/article/id/430457-up-to-78-million-batteries-will-be-discarded-daily-by-2025-researchers-warn</u>

<u>https://www.enables-project.eu/outputs/position-paper/</u>

- How resilient are battery-powered devices?

- While privacy is protected by the fabric, how can one still discover devices?

- What about running disruptive DoS attacks?

**Smart Factories**

**Smart Homes**

**Smart Cities**

**Smart Healthcare**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 18

## **What can possibly go wrong?**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 19

No router

##### **No detection**

**No alarm**

**No charging**

#BHEU @BlackHatEvents

Information Classification: General

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biscichat
EUROPE 2024
901101001011010110108
011101011" *10101100
6110111000" 101010100. *110110101
01010101010 1010101018 ol rout
01011001011 100101101011  oso10138 No er er
100101101110 O1 10. 10001111011
Connectivity Standards Alliance : Security Vulnerabilities, CVEs _ detection
nemorio1o1 20101100 01011 1012001011
90101010 .pitororoioy4
Published in: =~ 2024 January February March April May June July August September October
CVSS Scores Greater Than:0 123 45 67 8 9 In CISA KEV Catalog
Sort Results By: Publish Date !§ Update Date!’ CVE Number!$ CVENumberts’ CVSS Scorels EPSS Score lé
i Copy l
CVE-2024-3454 Max CVSS 3.5 o a
An implementation issue in the Connectivity Standards Alliance Matter 1.2 protocol as used in the connectedhomeip SDK EPSS Score 0.04% \ | Z
allows a third party to disclose information about devices part of the same fabric (footprinting), even though the protocol Published 2024-07-24 7 7
is designed to prevent access to such information. Updated 2024-09-10
Source: Bitdefender
CVE-2024-3297 Max CVSS 6.5 No charging
An issue in the Certificate Authenticated Session Establishment (CASE) protocol for establishing secure sessions between EPSS Score 0.04%
two devices, as implemented in the Matter protocol versions before Matter 1.1 allows an attacker to replay manipulated Published 2024-07-24
CASE Sigma messages to make the device unresponsive until the device is power-cycled. Updated 2024-09-10 ( ) e
Information Classification: General source: Bitdefende
```

## Slide 20

## Today

- Learn about the **game changer Matter** standard

- The **First** reported **vulnerabilities** in Matter **SDK** (Software Development Kit):

(DeeDoS) [di: dos]
#BHEU @BlackHatEvents

- CVE-2024-3297 – **Delayed Denial of Service** (DeeDoS) [di: dos]

- CVE-2024-3454 – **Device feature scanning**

<u>https://www.cvedetails.com/vendor/35076/</u>

Information Classification: General

## Slide 21

## (few) Fundamental concepts

Information Classification: General

#BHEU @BlackHatEvents

## Slide 22

## Basic terminology

- Matter uses Multicast DNS (mDNS) to discover devices

##### Root CA

Sensor
IPK
CASE
sessions
NOC
Smart Plug

- Devices are added (commissioned) into a **fabric**

- **Fabric:** collection of devices sharing a trusted root certificate

- Operational **root of trust** : the root certificate authority responsible for:

   - Allocating fabrics

   - Issuing node operational certificates (NOC)

- **CASE:** Certificate Authenticated Session Establishment

##### **Matter fabric**

- **IPK** : Integrity Protection Key

Information Classification: General

#BHEU @BlackHatEvents

## Slide 23

## Multi-fabric support

##### Root CA 1

Root CA 1
Root CA 2
IPK1 IPK2
CASE
CASE

Information Classification: General

#BHEU @BlackHatEvents

## Slide 24

## SDK vs. device (product)

###### Commissioning

Data Model

Fabrics CASE PASE Interaction Model SDK: development tools for Matter devices

Information Classification: General

#BHEU @BlackHatEvents

## Slide 25

## Commissioning: certified device

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ = ™ss315 x
Powered Off
MANUFACTURER
Meross
CTm© Chengdu Meross Technology... View
tok ‘
FREE
Accessory Ready to Connect
ye Me “MSS315" is now in pairing mode. ss
—_ ” Copy and paste the setup code to
pee 3 connect.
g Se 29
“ @ Setup Code: 1531-955-5610
_ - Ae
Mc fini
Wi-r ewwork piuerenuer iesirry
Firmware 9.3.26
T n Pairing Mode
Remove Accessory
Information Classification: General
| _| | it a || (2) “ -
Commissioning: certified device Ts.
No SIM >
@ Mss315 x
Powered Off
Connected Services
Manage the services that can access
and control this accessory.
II still apy
Dear in thei
ar in the Apple Home
Status
Connected Services
CTURER
Meross
mM Chengdu Meross Technology...
FREE
```

## Slide 26

## Non-certified device

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
on-certified d
Add Accessory
Scan code or hold iPhone near the
accessory.
@Q = Scana Setup Code
B= Look for a QR code on the
tion it in the
era frame abov
») Hold iPhone Near Accessory
You can also hold iPhone
if it appears
this
symbol on the
Information Classification: General
Uncertified Accessory
This accessory has not been certified
to work with your home and may not
work reliably or securely with this
iPhone.
Add Anyway Cancel
=, Setting Up...
Testing
Locked
Speakers & TVs
HomePod
Not Playing
MSS315
4
Automation
biscichat
EUROPE 2024
```

## Slide 27

## CASE protocol

- Certificate Authenticated Session Establishment ( **CASE** ):

   - Built on the SIGn-and-MAc ( **SIGMA** ) family of protocols (Krawczyk, 2003)

- Mutual authentication

- Negotiate new session keys

Original SIGMA-I protocol Krawczyk, 2003

Information Classification: General

#BHEU @BlackHatEvents

## Slide 28

## CASE protocol: Sigma2, Sigma3 spec

Error 404: Not found (not defined)

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
—_
CASE protocol: Sigma2, Sigma3 spec = °3skhst
Msg2 = byte TBEData2_A[] = {}
{ byte TBEData2_Nonce[13] = /* "NCASE_Sigma2N" */
responderRandom (1) = Random, {Ox4e, 0x43, 0x41, 0x53, 0x45, Ox5f, 0x53, 0x69,
responderSessionId (2) = ResponderSessionId, 0x67, Ox6d, 0x61, 0x32, Ox4e}
responderEphPubKey (3) = ResponderEphKeyPair.pubLicKey,
encrypted2 (4) = TBEData2Encrypted, TBEData2Encrypted = Crypto_AEAD_GenerateEncrypt(
responderSessionParams (5) = session-parameter-struct (optional) K = S2K
} P = TBEData
A = TBEData2_A,
N = TBEData2_Nonce
8. The initiator SHALL send a message with Secure Channel Protocol ID and Sigma3 Protocol Ope byte TBEData3_A[] = {}
from Table 18, “Secure Channel Protocol Opcodes” whose payload is the TLV-encoded Sigr byte TBEData3_Nonce[13] = /* "NCASE_Sigma3N" */
Msg3 = { encrypted3 (1) = TBEData3Encrypted } with an anonymous tag for the outerm {Ox4e, 0x43, 0x41, 0x53, Ox, Ox5Sf, 0x53, 0x69,
struct. 0x67, Ox6d, 0x61, 0x33, Ox4e}
TBEData3Encrypted = Crypto_AEAD_GenerateEnckypt(
a Error 404: Not found
a .
X= TBEDatas_A, (not defined)
N = TBEData3_Nonce
Information Classification: General
```

## Slide 29

## CASE protocol: unfolded

##### Initiator

Responder

RandomI, SessionIdI, destId, EphPubKeyI [, ...] RandomR, SessionIdR, EphPubKeyR, {CertsR, ...}S2K [, ...] {CertsI, Sign{EphPubKeyI, EphPubKeyR}}S3K

Sigma1 Sigma2 Sigma3

Information Classification: General

#BHEU @BlackHatEvents

## Slide 30

## CASE Sigma1

Responder
RandomI, SessionIdI, destId, EphPubKeyI [, ...]
Sigma1

Initiator

HMACIPK(RandomI, FabricRootPK, FabricId, DestNodeId) IPK: Integrity Protection Key

#BHEU @BlackHatEvents

Information Classification: General

## Slide 31

## CASE Sigma1 validation

Fabr A Fabr B Fabr C ROOT ROOT ROOT PK PK PK NOC NOC NOC A B C

For-each (FabricId, NodeId, RootPK) in FabricList: destId' = HMACIPK(RandomI, RootPK, FabricId, NodeId);; If (destId' == destId) ValidateSigma1(); break; EndIf EndFor-each

FabricList

Information Classification: General

#BHEU @BlackHatEvents

## Slide 32

## CASE Sigma1 replay protection

Counter verified for freshness Not cryptographically protected!

Sigma1

Information Classification: General

#BHEU @BlackHatEvents

## Slide 33

## Testbed setup

Information Classification: General

#BHEU @BlackHatEvents

## Slide 34

## Controllers and devices

- Controllers (administrative domains) with Google and Apple's technologies

- For a controlled experiment we also added our own controller and Lock-App Matter Wi-Fi device

- Used the Matter reference implementation

- Other variants available:

   - RUST

   - JavaScript

Information Classification: General

#BHEU @BlackHatEvents

## Slide 35

## Testbed and components

Border Routers

Matter/Wi-Fi Devices

Matter/Thread Devices

#BHEU @BlackHatEvents

Information Classification: General

## Slide 36

## Testbed fabrics and connectivity

#BHEU @BlackHatEvents

Information Classification: General

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Testbed fabrics and connectivity biacichat
—_—— — _— —_-—-
Nanoleaf
| : 1) GAC) ames 1
Nanoleat | l
| | Light Bulb lI > =
© I
|
! Eve Door =~ | Hones Pod { ~~ Google Nest ~ \ [I '@) Eve Energy I
| & Window
|
Eve Door |
& Window ! |
|
| Eve Mation |
. ,
. ;
a — nee |
Meross ee ina
Smart Plug C)
| , Pore =
| | Eve Motion
j o) Meross |
* a Smart Plu
We ’ \\ a!
: —_—— oo
—- — ~ = ~ Legend
~Y a CHIP controller | g
CHIP lock app | (chip-tool) le's fabri Cs
(Cluster l, l Apple's fabric:
enumeration | (— —_ = l and
attack) |, J | Google's fabric > |
J === a
| CHIP's fabric oy
Information Classification: General
```

## Slide 37

## Novel attack class

## Delayed DoS: CVE-2024-3297

Information Classification: General

#BHEU @BlackHatEvents

## Slide 38

## Start of research

##### Impersonation

##### MITM

- **Motivating facts** for investigating the CASE protocol:

Address Poisoning

- Protocol runs on IPv6/UDP

DoS

- `messageCounter` is not cryptographically protected

- • Handling of `Sigma1` messages is complex

Integrity Battery depletion Remote control

Information Classification: General

#BHEU @BlackHatEvents

## Slide 39

## Incentive to test for a DoS attack

structure
destinationId
Initiator Responder
Generate: 8 steps
Sigma1
Gen. Rand resumption ID
Validate: 7 steps Load NOC
Generate: 14 steps Gen. Ephemeral Keys
Sigma2
Gen. Shared Secret
Validate: 13 steps
Sign (Certs, PubKeys)
Generate: 9 steps
Sigma3
Gen. Random
Validate: 15 steps Gen. S2K
Encrypt (Certs, Sign)

Information Classification: General

#BHEU @BlackHatEvents

## Slide 40

## What we expected

Information Classification: General

#BHEU @BlackHatEvents

## Slide 41

## What we got

## Delayed Denial of Service: DeeDoS [di: dos ]

Information Classification: General

#BHEU @BlackHatEvents

## Slide 42

## Attack impact: first day

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Pay ~
Attack impact: first day — blackhat
No SIM > 14:54
< Home Office if! = +
NOTHINGJERRY | : ;
:
VirtuallockApp Matter Accessory
al ro
4 7 ‘ ’ oy Locked No Response
5 2 1 :
» “
a
@ HomePod
Not Playing
_ THIS MEMEIS ABOUT NOTHING!
Automation
Information Classification: General
```

## Slide 43

## Attack impact: next days

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Attack impact: next days blackhat
No SIM > 14:55 =
< Home Office ih + ©
a a
WHY IS NOTHING WORKING mn
Locked No Response
HomePod
Not Playi
ag MSS315
No Response
I'MWRITINGC
Information Classification: General
```

## Slide 44

## We called this: DeeDoS

- Devices have limited session slots: • Session handling is complex, it involves timeouts/retransmissions • DeeDoS **depletes session slots**

- Why Delayed?

   - It does not affect existing CASE

- Controllers **are unable to create new CASE**

   - Devices display "No Response"

Information Classification: General

#BHEU @BlackHatEvents

## Slide 45

## Step1: get a CASE Sigma1 message

Remember! CASE Sigma1 is not encrypted

Message type: Sigma1

RandomI, SessionIdI, destId, EphPubKeyI [, ...]

Information Classification: General

#BHEU @BlackHatEvents

## Slide 46

## **But CASE Sigma1 is not broadcasted...**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 47

## Step1a: mDNS-SD poisoning

Q: 52DDBB89B9DAE14A-00000000000000DE._matter._tcp.local

**CASE Sigma1**

A: fe80::bb14:b38e:9a7:b874

Border Router

A: fd25:491c:aeda:1:514f:d62f:2b9:29c6

Information Classification: General

#BHEU @BlackHatEvents

## Slide 48

## Step2: replay

Existing CASE not affected

messageCounter++ / CASE Sigma1 payload Replay 2 packets / second

Border Router

Run for ~10 minutes

Information Classification: General

#BHEU @BlackHatEvents

## Slide 49

## Impact 1

While the attack is running new CASE cannot be established Border X Router

messageCounter++ / CASE Sigma1 payload 2 packets / second

Affects: **all Matter devices & versions**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 50

## Impact 2

After the attack is stopped new CASE cannot be established Border X Router

Affects: **all Matter devices with SDK version < 1.1**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 51

## Vulnerability report

- Vulnerability first reported to device manufacturers: Meross, Nanoleaf • Response: **issue is in the SDK**

- Vulnerability reported to the Connectivity Standards Alliance (CSA)

Information Classification: General

#BHEU @BlackHatEvents

## Slide 52

## Response from CSA & solutions

- Vulnerability is indeed in the SDK

   - Affects: **all Matter devices running SDK version < 1.1**

- Solution(s):

   - Update to (at least) Matter 1.1

   - Patch the code (PR #32990)

- While the attack is running, **new CASE cannot be established**

- Affects: **all Matter devices (all versions)**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 53

## Upgrade to superior Matter version

Information Classification: General

#BHEU @BlackHatEvents

## Slide 54

## Upgrade to superior Matter ver...

- Upgrade to Matter 1.1+ leads to improved CASE

- Matter 1.1 compliance: **additional resource requirements**

**Matter Version Access Control Limits Group limits Group key limits** Min. 3 entries / supported 1.0 NO minimum req. 1 group key / fabric fabric Min. 4 entries / supported Min. 3 group keys / 1.1 Min. 4 groups / fabric fabric fabric

Information Classification: General

#BHEU @BlackHatEvents

## Slide 55

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
piseicha :
EUROPE 2024
a
TH Download more RAM!
Instant, Fast, FREE
>)
° \
Information Classification: General
```

## Slide 56

## Protect the messageCounter (1)

HMACIPK(RandomI, FabricRootPK, FabricId, DestNodeId) HMACIPK(messageCounter, RandomI, FabricRootPK, FabricId, DestNodeId)

Information Classification: General

#BHEU @BlackHatEvents

## Slide 57

## Protect the messageCounter (2)

`messageCounter:` **+4 bytes**

HMACIPK(messageCounter, RandomI, FabricRootPK, FabricId, DestNodeId)

1 Sigma1 packet (2-3 days)

1200 Sigma1 packets (2400 days ~ 6.5 years)

Information Classification: General

#BHEU @BlackHatEvents

## Slide 58

## Protect the messageCounter (3)

- Matter does not have version negotiation!

- This would break backward-compatibility

Information Classification: General

#BHEU @BlackHatEvents

## Slide 59

## So what is the solution?

- Unable to upgrade?

- Unable to change the specification & integrate counter protection?

- • **Monitor & detect!**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 60

## Monitor & detect

- Matter packet headers are not encrypted

- We can **count CASE Sigma1** packets

- Simple packet statistics can **detect the DeeDoS attack**

Foreach (TimeWnd) If (count(Sigma1, TimeWnd) >= Th) Raise_DeeDoS(); Endif Endforeach

Sigma1
Sigma1

Information Classification: General

#BHEU @BlackHatEvents

## Slide 61

## Count CASE Sigma1 packets

DeeDoS attack & detection

CASE Sigma1 on normal reconnection

Information Classification: General

#BHEU @BlackHatEvents

## Slide 62

## What about battery depletion?

- Feasible, it takes **~ 6 – 12 days** (depending on device)

- Tested with several devices by replaying **15 Sigma1 packets / second**

- Attack has an immense **impact on usability** , important that it is stopped early!

Information Classification: General

#BHEU @BlackHatEvents

## Slide 63

## Feature enumeration: CVE-2024-3454

Information Classification: General

#BHEU @BlackHatEvents

## Slide 64

## Starting point

- The Matter fabric is a closed and protected ecosystem

- Within a fabric, devices do not have access to each other's **clusters** and **attributes**

Attribute?
Access
denied!

   r        u  er
        e    r  u e
       a e    r  u e
        r     and
 n        r     and
 e   reden  a      and
   r        ar    en

   r
  de
 nd   n            de  nd   n        r
 a     n  r a   n   u  er  den       u  er
   e     n r     u  er    r        u  er
 enera           n n
 e   r           n n

Source: <u>https://developer.nordicsemi.com/nRF_Connect_SD K/doc/latest/nrf/protocols/matter/overview/data_model.html</u>

Information Classification: General

#BHEU @BlackHatEvents

## Slide 65

## Steps to follow

1. Create a Virtual device

2. Add to target fabric

3. Interrogate other devices

Sensor
CASE
sessions
Smart Plug

Information Classification: General

#BHEU @BlackHatEvents

## Slide 66

## Step #1: create a virtual device

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Step #1: create a virtual device
connectedhomeip
README.md
xam
Information Classification: General
ples / lock-app
Lock Application for Linux
linux /
» Se
blackhat
EUROPE 2024
A
Indalone/chip-lock-app
::Init: Using KVS config file: /tmp/chip_kvs
::Init: Using KVS config file: /tmp/chip_kvs
::Init: Attempt to re-initialize with KVS config file:
::Init: Using KVS config file: /tmp/chip_factory.int
::Init: Using KVS config file: /tmp/chip_config.int
nuxStorage::Init: Using KVS config file: /tmp/chip_counters. ini
ig settings to file (/tmp/chip_counters.ini-HiMisk)
to file (/tmp/chip_counters.ini)
: chip-counters/reboot-count = 5 (x5)
/tmp/chip_kvs
Application that showcases abilities of the Door Lock Cluster. (etsiSaiNtihd-lee-(o-Fa-Tilep
[ 1729250960.
y and will disappear.
(1729250960.
4
663978]
663990][198718:
ase update your scripts to
[1729250960.
(1729250960.
[1729250960.
[1729250960.
[1729250960.
(1729250960.
[1729250960.
[1729250960.
(1729250960.
[1729250960.
[1729250960.
[1729250960.
[1729250960.
[1729250960.
(1729250960.
[1729250960.
663993][198718:
663996 ][198718:
665414][198718:
665420][198718:
665424][198718:
665427][198718:
665430][198718:
665433][198718:
665435][198718:
665437 ][198718:
665441][198718:
665443][198718:
665445 ][198718:
665450][198718:
665453][198718:
665456 1[198718:
198718]
198718]
198718]
198718]
198718]
198718]
198718]
198718]
198718]
198718]
198718]
198718]
198718]
198718]
198718]
198718]
Tivo tO.ToOTTo eon
(198718:198718] CHIP:DL:
[1729250960 .663982][198718:198718] CHIP:DL:
[1729250960.663987][198718:198718] CHIP:SPT:
Please update your scripts to explicitly configure onboarding credentials.
198718] CHIP:SPT:
explicitly configure discriminator.
CHIP:
CHIP:
CHIP:
CHIP:
CHIP:
CHIP:
CHIP:
CHIP:
CHIP:
CHIP:
CHIP:
CHIP:
CHIP:
CHIP:
CHIP:
CHIP:
he primary Ethernet interface:eno1
Failed to get WiFi interface
Failed to reset WiFi statistic counts
*x*x*x WARNING: Using temporary passcode 20202021 due to no neither --passcode or --spake2p
KKK
*x*x* WARNING: Using temporary test discriminator 3840 due to --discriminator
eK
SPT: PASE PBKDF iterations set to 1000
SPT: LinuxCommissionableDataProvider didn't get a PASE salt, generating one.
DL: Device Configuration:
DL: Serial Number: TEST_SN
DL: Vendor Id: 65521 (OxFFF1)
DL: Product Id: 32769 (0x8001)
DL: Product Name: TEST_PRODUCT
DL: Hardware Version: 0
DL: Setup Pin Code (@ for UNKNOWN/ERROR): 20202021
DL: Setup Discriminator (OxFFFF for UNKNOWN/ERROR):
DL: Manufacturing Date: (not set)
DL: Device Type: 65535 (OxFFFF)
-: ==== Onboarding payload for Standard Commissioning Flow ====
SVR: SetupQRCode: [MT:-243042CO0KA0648G00 ]
SVR: Copy/paste the below URL in a browser to see the QR Code:
SVR: https://project-chip.github. 1o/connectedhomeip/qrcode. html ?data=MT%3A-24J042COOKA0648G00
not given on
3840 (OxF00)
```

## Slide 67

## Step #2: add to target fabric

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Step #2: add to target fabric " biBeichat
bgenge@bgenge-d: $ ./out/debug/standalone/chip-lock-app
[1729250960 .662813][198718:198718] CHIP:DL: ChipLinuxStorage::Init: Using KVS config file: /tmp/chip_kvs
[1729250960.663152][198718:198718] CHIP:DL: ChipLinuxStorage::Init: Using KVS config file: /tmp/chip_kvs
[1729250960.663158][198718:198718] CHIP:DL: ChipLinuxStorage::Init: Attempt to re-initialize with KVS config file: /tmp/chip_kvs
[1729250960 .663275][198718:198718] CHIP:DL: ChipLinuxStorage::Init: Using KVS config file: /tmp/chip_factory.ini
[1729250960.663314][198718:198718] CHIP:DL: ChipLinuxStorage::Init: Using KVS config file: /tmp/chip_config.ini
[1729250960.663328][198718:198718] CHIP:DL: ChipLinuxStorage::Init: Using KVS config file: /tmp/chip_counters Please scan with your CHIPTool app.
[1729250960.663443][198718:198718] CHIP:DL: writing settings to file (/tmp/chip_counters. ini-HiMisk)
[1729250960.663547][198718:198718] CHIP:DL: renamed tmp file to file (/tmp/chip_counters.ini)
[1729250960.663554][198718:198718] CHIP:DL: NVS set: chip-counters/reboot-count = 5 (0x5)
[1729250960 .663707][198718:198718] CHIP:DL: Got Ethernet interface: enol
[1729250960 .663829][198718:198718] CHIP:DL: Found the primary Ethernet interface:eno1
[1729250960.663978][198718:198718] CHIP:DL: Failed to get WiFi interface
[1729250960 .663982][198718:198718] CHIP:DL: Failed to reset WiFi statistic counts
[1729250960 .663987][198718:198718] CHIP:SPT: *** WARNING: Using temporary passcode 20202021 due to no neither
y and will disappear. Please update your scripts to explicitly configure onboarding credentials. ***
[1729250960 .663990][198718:198718] CHIP:SPT: *** WARNING: Using temporary test discriminator 3840 due to --di
ase update your scripts to explicitly configure discriminator. ***
[1729250960 .663993][198718:198718] CHIP:SPT: PASE PBKDF iterations set to 1000
[1729250960 .663996][198718:198718] CHIP:SPT: LinuxCommissionableDataProvider didn't get a PASE salt, generati
[1729250960.665414][198718:198718] CHIP:DL: Device Configuration:
[1729250960.665420][198718:198718] CHIP:DL: Serial Number: TEST_SN Payload: MT:-24J042CO0KA0648G00
[1729250960.665424][198718:198718] CHIP:DL: Vendor Id: 65521 (OxFFF1) This QR code is unique for your device. You may print a copy of this for subsequent use.
[1729250960.665427][198718:198718] CHIP:DL: Product Id: 32769 (0x8001)
[1729250960.665430][198718:198718] CHIP:DL: Product Name: TEST_PRODUCT
[1729250960.665433][198718:198718] CHIP:DL: Hardware Version: 0
[1729250960.665435][198718:198718] CHIP:DL: Setup Pin Code (0 for UNKNOWN/ERROR): 20202021
[1729250960 .665437][198718:198718] CHIP:DL: Setup Discriminator (@OxFFFF for UNKNOWN/ERROR): 3840 (0xF00)
[1729250960 .665441][198718:198718] CHIP:DL: Manufacturing Date: (not set)
UY0U.
[1729250960.665445 ][198718:198718] -3
[1729250960 .665450][198718: 198718] SVR: SetupQRCode: [MT:-243042COOKA0648G00 ]
(1729250960. 665453][198718: 198718] SVR: Copy/paste the below URL in a browser to see the QR Code:
(1729250960. :198718] SVR: https://project-chip.github. to/connectedhomeip/qrcode. html ?data=MT%3A-24J042CO0KA0648G00
Information Classification: General
```

## Slide 68

## Step #2: add to target fabric

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Step #2: add to target fabric” piseichat
Add Accessory
Scan code or hold iPhone near the
accessory.
Uncertified Accessory
This accessory has not been certified
to work with your home and may not
work reliably or securely with this
iPhone.
Add Anyway Cancel
Scan a Setup Code Speakers & TVs
oo
ia}
on the
J OF r HomePod
d position it in the y Not Playing
‘a frame above
Look for a QR
») Hold iPhone Near Accessory
You can also hold iPhor
symbol if it appears on t
accessory >, Setting Up... MSS315
4
near this
Automation
Information Classification: General
```

## Slide 69

## Step #3: interrogate other devices

## **Should be straightforward, right?**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 70

## Step #3: interrogate other devices

- **No documentation** on API to open CASE

- **No documentation** on API to interrogate clusters / attributes

Information Classification: General

#BHEU @BlackHatEvents

## Slide 71

## Change the lock application (1)

1. Add necessary include files

2. Add global variables

Information Classification: General

#BHEU @BlackHatEvents

## Slide 72

## Change the lock application (2)

##### 3. Add callback functions

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Change the lock application (2) © wibichat
oid HandleDeviceConnected(void *context,
Messaging: :ExchangeManager &exchangeMgr,
const SessionHandle &sessionHandle)
}
void HandleDeviceConnectionFailure(void *context,
const ScopedNodeld &peerId,
3. Add callback functions CHIP_ERROR-err)
Callback: :Callback<OnDeviceConnected>
gOnConnectedCallback(HandleDeviceConnected, nullptr) ;
Callback: :Callback<OnDeviceConnectionFailure>
gOnConnectionFailureCallback(HandleDeviceConnectionFailure, nullptr);
Information Classification: General
```

## Slide 73

## Change the lock application (3)

##### 4. Change FromJSON()

##### 5. Change HandleCommand()

Information Classification: General

#BHEU @BlackHatEvents

## Slide 74

## Change the lock application (4)

##### 6. Add scan code

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Change the lock application (4) blackchat
6. Add scan code
Information Classification: General
g> -
auto: onSuccess =: [](const ConcreteDataAttributePath &attributePath, const auto &dataResponse) - {
ChipLogProgress(NotSpecified, "Read attribute: successful!") ;
auto onFailure = [](const ConcreteDataAttributePath *attributePath, CHIP_ERROR error) - {
ChipLogError(NotSpecified, "Read attribute: failed: -%"»CHIP_ERROR_FORMAT, error.Format()) ;
Controller:
gXMgr,
Controller:
gXMgr,
Controller:
gXMgr,
Controller:
gXMgr,
Controller:
gXMgr,
:ReadAttribute<Clusters: :OnOff: :Attributes: :OnOff: : TypeInfo>(
sessionHandle, @x@1, onSuccess, onFailure) ;
:ReadAttribute<Clusters: :LevelControl: :Attributes: :CurrentLevel: : TypeInfo> (
sessionHandle, @x@1, onSuccess, onFailure) ;
:ReadAttribute<Clusters: :ColorControl: :Attributes: :CurrentHue: :TypeInfo> (
sessionHandle, x01, onSuccess, onFailure) ;
:ReadAttribute<Clusters: :OccupancySensing: :Attributes: :Occupancy: : TypeInfo>(
sessionHandle, @x@1, onSuccess, onFailure) ;
:ReadAttribute<Clusters: :BooleanState: :Attributes: :StateValue: : TypeInfo>(
sessionHandle, @x01, onSuccess, onFailure) ;
```

## Slide 75

## Run the lock application

1. Run lock app

```
./chip-lock-app &
```

##### 2. Issue Scan command

```
pid=$(pidof./chip-lock-app)
NODE_ID="00000000DA41E4CF"
```

```
CMD="{\"Cmd\": \"RunScan\", \"Params\": { \"EndpointId\": 1,\"Node\":
\"$NODE_ID\" } }"
```

```
echo $CMD > /tmp/chip_lock_app_fifo-"$pid"
```

Information Classification: General

#BHEU @BlackHatEvents

## Slide 76

## Did you expect to get access?

- Unfortunately, we only <u>get ERROR after ERROR!</u>

- Matter's built-in Access Control List denies, by default, all access to clusters and attributes

```
CHIP:-: Read attribute failed: IM Error 0x000005C3: General error: 0xc3
(UNSUPPORTED_CLUSTER)
```

```
CHIP:-: Read attribute failed: IM Error 0x000005C3: General error: 0xc3
(UNSUPPORTED_CLUSTER)
```

```
CHIP:-: Read attribute failed: IM Error 0x0000057E: General error: 0x7e
(UNSUPPORTED_ACCESS)
```

```
CHIP:-: Read attribute failed: IM Error 0x000005C3: General error: 0xc3
(UNSUPPORTED_CLUSTER)
```

```
...
```

Information Classification: General

#BHEU @BlackHatEvents

## Slide 77

## All is not loosed!

- Observe the two errors:

   - `UNSUPPORTED_CLUSTER`

   - `UNSUPPORTED_ACCESS`

Source: Matter 1.2 specification

Information Classification: General

#BHEU @BlackHatEvents

## Slide 78

## What can we infer?

- Cluster: `OnOff`

   - Attribute: `OnOff`

- Cluster: `BooleanState`

   - Attribute: `StateValue`

- Cluster: `OnOff`

   - Attribute: `OnOff`

- Cluster: LevelControl

   - Attribute: CurrentLevel

- Cluster: ColorControl

   - Attribute: CurrentHue

- Cluster: `OnOff`

   - Attribute: `OnOff`

Information Classification: General

#BHEU @BlackHatEvents

## Slide 79

## Vulnerability report & response

- Detailed report submitted to CSA

   - Response: vulnerability is applicable to **all Matter versions and devices on the market**

- Resulted in a change in the Matter specification!

<u>https://github.com/project-chip/connectedhomeip/issues/33735</u>

Information Classification: General

#BHEU @BlackHatEvents

## Slide 80

## Alternative solution: packet analysis

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Alternative solution: packet analysis
Matter
Matter
Matter
Matter
Matter
Matter
Matter
Matter
Matter
Matter
Matter
Matter
Matter
Matter
Information Classification: General
239 5540
88 5540
972 5540
435 5540
88 5540
96 5540
113 5540
113 5540
114 5540
114 5540
113 5540
113 5540
113 5540
113 5540
9940 jLen=177
9540 JLen=26
9540 }LEn=510
9540 JLeEn=373
9540
9540
9540
9540
9540
9540
9540
9540
5540
9540
—
pigtichat
a
>Message Flags: 0x01, B@stination ID Type: 64-bit Node ID
Session ID: 0x0000
> Security Flags: 0x00, Session Type: Unicast Session
Message Counter: Ox0efcf2do0
Destination Node ID: 0x16083547e39ae6eb
» Protocol Payload a
> Exchange Flags: 0x02, Ack
Protocol Opcode: 0x10
Exchange ID: @x091e a
Protocol ID: 0x0000
AcknowLedged message counter: 0x074b3203
Application payload (0 bytes)
~ Matter
edgement
EUROPE 2024
```

## Slide 81

## Matter packet fingerprint

<matter_msg_len>-<msg_flags>-<security_flags>-<enc_payload_len>; <exch_flags>-<proto_opcode>-<proto_id>-<app_payload_len>;

Information Classification: General

#BHEU @BlackHatEvents

## Slide 82

## Fingerprint similar to JA3/JA4

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Fingerprint similar to JA3/JA4 pigekhat
v Transport Layer Security
. TLSv1.2 Record Layer: Handshake Protocol: Client Hello
Content Type: Handshake (22)
Version: TLS 1.0 (0x0301)
Length: 707
v Handshake Protocol: Client Hello
Handshake Type: Client Hello (1)
Length: 703
> Version: TLS 1.2 (0x0303)
> Random: 0b279f74d6e4f62f53fde2c93f71837576dce0b4c55f 29a1462b7548a9360929
Session ID Length: 32
Session ID: c8e57809ac4f3e1e46dc92660653c3d63bd65520ec01350f 3db9c39d5aef4b34
Cipher Suites Length: 32
Cipher Suites (16 suites)
Compression Methods Length: 1
Compression Methods (1 method)
Extensions Length: 598
> Extension: Reserved (GREASE) (len=0)
Extension: key_share (lLen=43) x25519
Extension: ec_point_formats (len=2)
Extension: application_settings (len=5)
Extension: renegotiation_info (len=1)
Extension: signed_certificate_timestamp (len=0)
Extension: server_name (len=21) name=webmail.umfst.ro
Extension: extended_master_secret (len=0)
Extension: psk_key_exchange_modes (len=2)
> Extension: session_ticket (len=208)
Extension: supported_groups (len=10)
Extension: compress_certificate (len=3)
Extension: status_request (len=5)
Extension: supported_versions (len=7) TLS 1.3, TLS 1.2
Extension: application_layer_protocol_negotiation (len=14)
Extension: encrypted_client_hello (len=186)
Extension: signature_algorithms (len=18)
Extension: Reserved (GREASE) (len=1)
[JA4: t13d1516h2_8daaf6152771_02713d6af 862]
[JA4_r: t13d1516h2_002f, 0035, 009c, 009d, 1301, 1302, 1303, C013, C014, CO2b, cO2c, cO2F, C030, cca8, Cca9_0005, 000a, 000b, 000d, 0012, 0017, 001b, 0023, 002b, 002d, 0033, 4469, Fedd, FFO1_:
[JA3: 351edb9670cb8a3fd330e2811cb787e4]
```

## Slide 83

## Fingerprint example

###### Enc payload length

###### Security flags

Message flags

Packet length

Exchange flags Protocol opcode Protocol id App payload length

**177-4-0-;5-48-0-155;**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 84

## Matter packet analysis

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biscichat
EUROPE 2024
Information Classification: General
I Minute 5 Minutes 10 Minutes
saci — Normal cial — Normall acd — Normall
Normal 2 Normal 2 Normal 2
3 a - |
s 7007 | Normal 3 M007) _ Normal 3 1009) Normal 3
S — FScan —— FScan —— FScan
= 300- 300- 300-
0S
c
$ 200- 200 - 200 -
a I
®
5 100 | 100- ih. 100
0- A vivee \ 0-| A AA AN O- In s
(e) 20 40 60 fe) 20 40 60 (e) 20 40 60
IMinute 5 Minutes 10 Minutes
500+ | Normal | | 500% (Normal | 5007 Normal ! A
Normal 2 Normal 2 Normal 2
4007 __ Normal 3 4007 __ Normal 3 4007 __ Normal 3
5 — FScan —— FScan —— FScan
‘= 300- 300- 300-
=
2 2007 200 - | 200 -
“4 | \
100+ | | 100- | 100-
K\ !
\
o- Non _ o-| & aA J ly O- .
0 20 40 60 0 20 40 60 0 20 40 60
```

## Slide 85

## Packet cumulative distributions

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Packet cumulative distributions
Information Classification: General
biscichat
EUROPE 2024
I Minute 5 Minutes 10 Minutes
Loy Normal | [i Sf Loy Normal | S—_ / Loy Normal 1 ZZ TF
3 Normal 2 4 Normal 2 7 Normal 2 /
eS OB | aa Normal 3 OB hem Normal 3 OB | ae Normal 3
S — — FS
2 age can can
()
L
S o4-
(a)
S o2-
re 0.2
0.0- ~/)
O 20 40 60 20 40 60
I Minute 5 Minutes lO Minutes
10- , 10-| <= 10- a ee
— Normal] VY — Normall A — Normall
Normal 2 SL Normal 2 /” Normal 2 |
O87 __ Normal 3 O87 __ Normal 3 O87 __ Normal 3
s — FScan — FScan
: O6-
°
=
© O44
LJ
0.2 -
0.0-
0 20 40 60
```

## Slide 86

## Way forward

Information Classification: General

#BHEU @BlackHatEvents

## Slide 87

## Call for action

- Call for both **offensive** and **defensive** security research

- Matter is heavily anchored into legislative initiatives worldwide

- Security researchers may shape the evolution of the Matter IoT standard

Source: https://csa-iot.org/newsroom/the-connectivity-standards-alliance-and- <u>the-cyber-security-agency-of-singapore-sign-mutual-recognition-arrangementon-cybersecurity-labels-for-consumer-iot/</u>

Source: https://www.theverge.com/2024/3/18/24104906/csa- <u>iot-device-security-specification-product-security-verificationmark</u>

Information Classification: General

#BHEU @BlackHatEvents

## Slide 88

## Call for action – NIS-2 & CRA

- Network and Information Security (NIS) Directive 2 (NIS 2 (EU) 2022/2555) outlines a wide variety of security requirements

- The EU Cyber Resilience Act (2024) provides harmonized rules for all connected devices

- **Monitoring can help** with early detection of compromise

- Implement mandatory **vulnerability management processes**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 89

## Remember the OPC UA path?

- Similarly to Matter, OPC UA promised **unification** and **robust security features**

- Vulnerabilities still arise due to massive protocol complexities, implementation errors, misconfigurations, evolving cyber threats

- Let's not go down the same path again!

<u>A Broken Chain: Discovering OPC UA Attack Surface and Exploiting the Supply Chain - Black Hat USA 2021 Resting on Feet of Clay: Securely Bootstrapping OPC UA Deployments - Black Hat Europe 2021 Exploiting OPC-UA in Every Possible Way: Practical Attacks Against Modern OPC-UA Architectures - Black Hat USA 2023</u>

Information Classification: General

#BHEU @BlackHatEvents

## Slide 90

## Lessons learned

- The **description of security protocols** must be improved to facilitate analysis

- **Offensive security** investigations are needed (e.g., hackathons, bounty-hunting) to ensure a robust, bullet-proof standard

- **(encrypted) Matter traffic** must be **monitored** in order to detect (new) attacks

Information Classification: General

#BHEU @BlackHatEvents

## Slide 91

## Black Hat Sound Bytes

**Matter is a nuclear blast protocol** from ALL perspectives!

After almost 30 years from Gavin Lowe's pioneering work on security protocol analysis*, **packet replay attacks are still the #1 hit** !

There is still time! The standard is being shaped, **be the one that improves it (all stakeholders)** by challenging the protocol's security!

- Lowe, G. (1996). Breaking and fixing the Needham-Schroeder Public-Key Protocol using FDR. In: TACAS, LNCS, vol 1055. Springer, Berlin, Heidelberg 1996. <u>https://link.springer.com/chapter/10.1007/3-540-61042-1_43</u>

Information Classification: General

#BHEU @BlackHatEvents

## Slide 92

Thank you! Béla Genge <u>bgenge@bitdefender.com</u>

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
—- uw! |
_ EWROP ‘Ss
tt |
ae li , | mee Los
\ | y = eee, oN. =
—E L- = la
Béla Genge
bgenge@bitdefender.com
#BHEU @BlackHatEvents
```
