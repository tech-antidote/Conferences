---
title: "Weaponization of Cellular Based IoT Technology – Leveraging Smart Devices to Gain a Foothold"
speakers: ["Deral Heiland", "Carlota Bindner"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Deral Heiland&Carlota Bindner_Weaponization of Cellular Based IoT Technology – Leveraging Smart Devices to Gain a Foothold.pdf"
pages: 55
sha256: "b2284625d7c14b5eac0036aa05a337889a3fa3e59f2114713cfdac1251cd26b8"
text_chars: 14662
ocr_pages: 18
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T22:52:39Z"
---
# Weaponization of Cellular Based IoT Technology – Leveraging Smart Devices to Gain a Foothold

**Speakers:** Deral Heiland, Carlota Bindner  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Deral Heiland&Carlota Bindner_Weaponization of Cellular Based IoT Technology – Leveraging Smart Devices to Gain a Foothold.pdf` (55 pages)


## Slide 1

### Weaponization Of Cellular Based IoT Technology Leveraging Smart Devices to Gain a Foothold

Deral Heiland  &  Carlota Bindner

#BHUSA @BlackHatEvents

## Slide 2

**Deral Heiland Principal Security Research (IoT), Rapid7 deral_heiland@rapid7.com @percent_x**

**Carlota Bindner Lead Product Security Researcher Thermo Fisher Scientific @carlotabindner**

#BHUSA @BlackHatEvents

## Slide 3

## Project Introduction

#BHUSA @BlackHatEvents

## Slide 4

###### Observations

- Growing use of cellular in IoT

- Lack of effective knowledge

- Lack of security testing methods

###### Goal

- Understand technology

- Build testing methodologies

- Answer needed security question

#BHUSA @BlackHatEvents

## Slide 5

###### NB-IoT

- Slow (26-127 kbits)

- Telemetry Data

- Half-duplex

- Latency  (1.6-10s)

###### LTE-M

- Faster (1-4 mbits)

- Voice, Images, Video

- Full-duplex

- Latency (10-15ms)

#BHUSA @BlackHatEvents

## Slide 6

###### Inter-Chip Communication

- Encryption (Unlikely)

- Easy to sniff

- Easy to inject & control

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
BRIEFINGS
FRIGGA
v56ur48
EOP Epeue
POUL BPP a?
inter-Chip Communication
¢ Encryption (Unlikely)
¢ Easy to sniff
¢ Easy to inject & control
ooeeea
```

## Slide 7

Cellular
Service

Internet of Things Hardware
Inter-Chip Communication
Main Cellular
CPU Module
Typically Encrypted
&
FCC Regulated
Not Typically Encrypted

#BHUSA @BlackHatEvents

## Slide 8

###### Trust

- Machine-to-Machine (overly trusted)

- Implicit Trust

- Automated Authentication & Validation

- Limited Containment & Segmentation

#BHUSA @BlackHatEvents

## Slide 9

Cellular
Service

###### Internet of Things Hardware

Main Inter-Chip Communication Cellular
CPU Module

Services
Cloud & Internet
Private Network

#BHUSA @BlackHatEvents

## Slide 10

Cellular Service

###### Internet of Things Hardware

Main Inter-Chip Communication Cellular
CPU Module

Services
Cloud & Internet
Private Network

#BHUSA @BlackHatEvents

## Slide 11

Cellular
Service

Internet of Things Hardware
Main Inter-Chip Communication Cellular
CPU Module
By controlling these, I have access to all trusted resources

Services
Cloud & Internet
Private Network

#BHUSA @BlackHatEvents

## Slide 12

## How To Interact With Cellular Modules

#BHUSA @BlackHatEvents

## Slide 13

###### USB

- Standard 2.0 HS

- Implement basic functions

###### UART

- Debug UART (External)

- Main UART (Inter-Chip)

#BHUSA @BlackHatEvents

## Slide 14

###### Talking to a Cellular Module

###### **AT Commands**

   - AT=Attention

   - Used to control modems

- **Allow communication and control**

   - Configuration and management

   - Diagnostics

   - Updates

#BHUSA @BlackHatEvents

## Slide 15

**Type Syntax Function** Test AT+<COMMAND>=? Returns parameters and value ranges. Read AT+<COMMAND>? Returns the current parameter values. Write/Set AT+<COMMAND>=<INPUT> Sets command parameters to user-defined values. Execute AT+<COMMAND> Executes the command.

#BHUSA @BlackHatEvents

## Slide 16

###### Types of AT Commands

###### **3GPP Standardized**

- Required

- Implement basic functions

###### **Manufacturer Specific**

- Specific to features

- • Enhance functionality

**Manufacturer Custom Syntax** Quectel AT+Q U-Blox AT+U Telit AT@, AT#, AT$, AT* Nordic AT% Murata AT% Huawei AT^

#BHUSA @BlackHatEvents

## Slide 17

## Hardware Hacking Physical Interaction with Hardware

#BHUSA @BlackHatEvents

## Slide 18

###### Mapping Access Obverse

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
pee
ae Be 3
Mapping Access
Obverse
Bs
Ca
e) am
]
,
iy
|
1ovf
SAG00-A100-1 Mode! :
Mae inChinas
(Cc: 78 $624
FCC IDPRQIPPLS
=
:
ce
```

## Slide 19

Mapping Access Reverse (flipped)

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
Mapping Access
Reverse (flipped)
b303-tbSO¥ sue
&.. @ @PS°D sws0s
OI Agee 53
Lb310 . bes = uz (Dad “
@ ibs © Ques. : ib3S¢ © oz Za
o"e @-w3ie™ © OO} ads 27 dth-0 bKI>
ane iigoe 1b3S0 ~ 1b3se “S@ 21-2
@>1b30s
©
b 3
1b302
ay
```

## Slide 20

Mapping Access Transparency (Obverse overlay)

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
= et ‘
Mapping Access Sy 6am sem (Ee se
soot a ht ae Sat
Lope at @ nS
Transparency (Obverse overlay) ine Tees
(V1)
£6339
```

## Slide 21

Mapping Access Data sheet LGA overlayed

#BHUSA @BlackHatEvents

## Slide 22

Mapping Access Data sheet LGA overlayed • UART

RXD0
TXD0

#BHUSA @BlackHatEvents

## Slide 23

RXD0
TXD0

USB_DN
USB_DP

###### Mapping Access

###### Data sheet LGA overlayed

- UART

- USB

#BHUSA @BlackHatEvents

## Slide 24

What if USB & UART Are Not Bot Accessible?

- Acupuncture needles

- Circuit run modifications

- Cut through sublayers

#BHUSA @BlackHatEvents

## Slide 25

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bifek hat : = ee fr
BRIEFINGS
```

## Slide 26

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
\ 4 >
2) ‘x = Af g
black hat | F > |
BRIEFINGS . 7 3 Y) | A ;
```

## Slide 27

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@)
O
Zz
im
Wu!
oO
aa
ed
6
&
3
Cg
fe}
```

## Slide 28

## Weaponization The Mechanics of UART

#BHUSA @BlackHatEvents

## Slide 29

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
Primary
CPU
*)
USB D+
USB D-
a
ie
UART
FTDI
Debug UART
RX TX
Cellular
, Module
TX
```

## Slide 30

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
>
biSekhat SS ee p
BRIEFINGS 4
t Traces
"O/ G yo,
```

## Slide 31

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
>
bisek hat
BRIEFINGS
#
3
3
```

## Slide 32

##### HTTP and Sockets

- Vendor-specific AT commands for HTTP and sockets

- Allows communications to cloud and internet-facing resources

- HTTPS support varies across modules and may be limited or inconsistent

#BHUSA @BlackHatEvents

## Slide 33

# DEMO

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
[MODEM] HTTPS GET: https://research-cellbucket1.s3.us—east-—1.amazonaws.com/flag2.txt h
[MODEM] >> AT+QHTTPURL=65, 30
[MODEM] << AT+QHTTPURL=65, 30
[MODEM] << CONNECT
[MODEM] >> AT+QHTTPGET=60
[MODEM] <<
[MODEM] << OK
[MODEM] << AT+QHTTPGET=6@
[MODEM] << OK
[MODEM] <<
[MODEM] << +QHTTPGET: 0,404
[MODEM] >> AT+QHTTPREAD=30
[MODEM] << AT+QHTTPREAD=30
[MODEM] << CONNECT
[MODEM] << <?xml version="1.0" encoding="UTF-8"?>
[MODEM] << <Error><Code>NoSuchKey</Code><Message>Thd bed e fe) s ie ge><Key>flag2.txt</Key><RequestId>9X2ADHEAXME@49ZH</
RequestId><HostId>yl@pI89BBMb60bDZTY1c3E4WdPgC@qxiWe Oo 4) e Mnuk=</HostId></Error>
[MODEM] << OK
[MODEM] Response Body (truncated):
AT+QHTTPREAD=30
CONNECT
<?xml version="1.0" encoding="UTF-8"?>
<Error><Code>NoSuchKey</Code><Message>The specified key does not exist.</Message><Key>flag2.txt</Key><RequestId>9X2ADHEAXME049ZH</RequestId><
HostId>yl@pI89BBMb60bDZTY1c3E4WdPgC@qxiWBzVj1JuK902dXXré6én@MHorUIXzyLeNmhpWa5B7Mnuk=</HostId></Error>
OK
[MODEM] HTTPS GET: https://research-cellbucket1.s3.us—east-—1.amazonaws.com/Flagi.txt
[MODEM] >> AT+QHTTPURL=65, 30
[MODEM] <<
[MODEM] << +QHTTPREAD: @
[MODEM] << AT+QHTTPURL=65, 30
[MODEM] << CONNECT
[MODEM] >> AT+QHTTPGET=60
[MODEM] <<
faeammersay ver AV
```

## Slide 34

##### PPP over UART

Provides network access via serial:

- Establishes IP network interface

- Compatible with standard TCP/IP stacks

- Modem handles cellular network layer

- After initial setup, no AT commands

#BHUSA @BlackHatEvents

## Slide 35

# DEMO

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
Wed Jul 23 18:55:44 2025 : revd [LCP ConfReq id=@x® <asyncmap @x@> <auth chap MD5> <magic @x7a2cc1@a> <pcomp> <accomp>]
Wed Jul 23 18:55:44 2025 : lcp_reqci: returning CONFREJ.
Wed Jul 23 18:55:44 2025 : sent [LCP ConfRej id=@x® <pcomp> <accomp>] hr
Wed Jul 23 18:55:44 2025 : revd [LCP ConfAck id=@x1 <asyncmap @x@> <magic 9x623e01f5>]
Wed Jul 23 18:55:44 2025 : revd [LCP ConfReq id=@x1 <asyncmap @x@> <auth chap MD5> <magic @x7a2cc1@a>]
Wed Jul 23 18:55:44 2025 : lcp_reqci: returning CONFACK.
Wed Jul 23 18:55:44 2025 : sent [LCP ConfAck id=@x1 <asyncmap @x@> <auth chap MD5> <magic @x7a2cc1@a>]
Wed Jul 23 18:55:44 2025 : rcevd [LCP DiscReq id=@x2 magic=@x7a2cc1@a]
Wed Jul 23 18:55:44 2025 : revd [CHAP Challenge id=@x1 <c7b6édbeb97d117e73ad88d31d945aec7>, name = "UMTS_CHAP_SRVR"]
Wed Jul 23 18:55:44 2025 : sent [CHAP Response id=@x1 <c731bca8afb@cb7e771043ce163c4adQ@>, name = “admin"]
Wed Jul 23 18:55:44 2025 : revd [CHAP Success id=@x1 ""]
Wed Jul 23 18:55:44 2025 : CHAP authentication succeeded
Wed Jul 23 18:55:44 2025 : sent [IPCP ConfReq id=@x1 <addr @.@.0.@> <ms—dns1 0.0.0.0> <ms—dns3 @.0.0.0>]
Wed Jul 23 18:55:44 2025 : sent [ACSCP ConfReq id=0x te 77 > ai 16777216>]
Wed Jul 23 18:55:44 2025 : revd [LCP ProtRej id=@x3 6 (s) 2 06 08 08 B8 C1)
Wed Jul 23 18:55:44 2025 : revd [IPCP ConfReq id=0x@
Wed Jul 23 18:55:44 2025 : ipcp: returning Configure
Wed Jul 23 18:55:44 2025 : sent [LIPCP ConfNak id=@x@ 0.
Wed Jul 23 18:55:44 2025 : revd [IPCP ConfNak id=@x1 dr 100. x ~ > <ms—-dnsi I-1f.1.1> <ms-dns3 8.8.8.8>]
Wed Jul 23 18:55:44 2025 : sent [LIPCP ConfReq id=@x2 <addr 100.64.139.49> <ms-—dns1 1.1.1.1> <ms-dns3 8.8.8.8>]
Wed Jul 23 18:55:44 2025 : revd [IPCP ConfReq id=@x1]
Wed Jul 23 18:55:44 2025 : ipcp: returning Configure-ACK
Wed Jul 23 18:55:44 2025 : sent [IPCP ConfAck id=@x1]
Wed Jul 23 18:55:44 2025 : revd [LIPCP ConfAck id=@x2 <addr 100.64.139.49> <ms-—dns1 1.1.1.1> <ms-—dns3 8.8.8.8>]
Wed Jul 23 18:55:44 2025 : ipcp: up
Wed Jul 23 18:55:44 2025 : Could not determine remote IP address: defaulting to 10.64.64.64
Wed Jul 23 18:55:44 2025 : local IP address 100.64.139.49
Wed Jul 23 18:55:44 2025 : remote IP address 10.64.64.64
Wed Jul 23 18:55:44 2025 : primary DNS address 1.1.1.1
Wed Jul 23 18:55:44 2025 : secondary DNS address 8.8.8.8
Wed Jul 23 18:55:44 2025 : Received protocol dictionaries
Wed Jul 23 18:55:44 2025 : Received acsp/dhcp dictionaries
Wed Jul 23 18:55:44 2025 : Committed PPP store
Wed Jul 23 18:55:44 2025 : Received acsp/dhcp dictionaries
Wed Jul 23 18:55:44 2025 : Committed PPP store
Default route is now through ppp@:
default link#19 UCSg pppe
```

## Slide 36

###### UART Pros and Cons

- Low level of effort

- PPP over UART

- Slower speeds and limited data throughput

- APN may not support PPP

#BHUSA @BlackHatEvents

## Slide 37

## Weaponization The Mechanics of USB

#BHUSA @BlackHatEvents

## Slide 38

###### USB Interfacing

- Can I gain access to and control the USB?

- What technical issues will I need to deal with?

- Where do I even start?

#BHUSA @BlackHatEvents

## Slide 39

###### USB Interfacing

Termination & impedance matching resistors Trace length limitation Trace spacing

- Prevent crosstalk

- Signal reflections

- Impedance mismatch

#BHUSA @BlackHatEvents

## Slide 40

###### USB Interfacing

###### Texas Instrument

- TS3USB221E High-Speed USB 2.0 (480Mbps) 1:2 Multiplexer

Pre-assembled Board (China)

- Solved electronic requirement

- Now, how do I splice this in?

#BHUSA @BlackHatEvents

## Slide 41

###### USB Multiplexer

#BHUSA @BlackHatEvents

## Slide 42

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
\ ~ ya: < ; ~~ ' tf yA
black hat ; ag pf eee. G . VA a
BRIEFINGS
```

## Slide 43

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
BRIEFINGS
7 y WA P 4 * (3/7 > S >
+) ~~ ieee, yA ~~ WT A mis
black hat a | J gLfE
LZZ—NOWo
+
”
Ww
c
|
‘i
z
=
```

## Slide 44

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisekhat AS te. | fe
BRIEFINGS
```

## Slide 45

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
gQ SS y _ 4 ’ iki mm % a a
X ~ _ yan oy) } y y ¢
blackhat ae 4 ’ a
BRIEFINGS 4 Cire Yf W/Z
```

## Slide 46

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
>
gQ 4 > -
blackhat / ra ’
BRIEFINGS I 4
Gy
ve ¥6: AVENS
BOXKVN Wer 4 2
‘S
```

## Slide 47

# DEMO

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
#BHUSA @BlackHatEvents
```

## Slide 48

###### USB Pros & Cons

**USB ECM (Ethernet Control Model)**

- Supported drivers on most host OS’s

- All standard tools at your disposal

###### **Complex Hardware Hacking**

- Limited bandwidth (NB-IoT)

- • Latency issues (NB-IoT)

#BHUSA @BlackHatEvents

## Slide 49

## Security Mitigation Strategies

#BHUSA @BlackHatEvents

## Slide 50

###### Mitigations

Tamper Protection

   - Case triggers

- Epoxy potting

- Disable USB/UART

   - Physically

   - Software

   - AT commands

Using a SIM Card PIN or Password Communication Encrypted

#BHUSA @BlackHatEvents

## Slide 51

###### Mitigations (cont.)

APN monitoring

- Cellular bandwidth usage

- Behavior

Internal network security monitoring Segmentation

Re-evaluate current security

   - Models & Methodologies

- Threat modeling

- Product Security testing

#BHUSA @BlackHatEvents

## Slide 52

###### One Last Comment

Two communication channels (USB/UART) also allows a cellular-enabled IoT device to be modified so it can phone home and be used for any number of nefarious activities

- C2

- Surveillance

- Remote function triggers

- No impact on devices’ normal functionality

   - Vendor may not know

- Vendor never sees the traffic

- End user not aware

#BHUSA @BlackHatEvents

## Slide 53

###### "Black Hat Sound Bytes"

- Cellular module AT language allow easy construction of tool to weaponizing cellular modules in IoT devices.

- Cellular enabled IoT devices' trusted access allows for compromise and attacks against cloud & internet services and private network environments.

- Mitigation of these threats are not easy. How do you protect a device against its normal functions from being used against you – General good security practices such as, limit access to only what is needed, segmentation, and monitoring.

#BHUSA @BlackHatEvents

## Slide 54

## Conclusion & Questions

**Deral Heiland Principal Security Research (IoT), Rapid7 deral_heiland@rapid7.com @percent_x**

**Carlota Bindner Lead Product Security Researcher Thermo Fisher Scientific @carlotabindner**

- https://github.com/dheiland-r7/CellPOC

- https://github.com/dheiland-r7/CellMod

#BHUSA @BlackHatEvents

## Slide 55

#### References

- (1) Craig Peacock, (2010) , USB in a Nutshell, https://www.beyondlogic.org/usbnutshell/usb2.shtml

- (2) Ken Munro, (2017). Hacking IoT vendors & smart cars via private APNs : https://www.pentestpartners.com/security-blog/hacking-iot-vendors-smart-cars-via-private-apns/

- (3) Deral Heiland, Matthew Kienow, and Pearce Barry (2021),  Leveraging Inter-chip Communication Analysis for Examining End-to-End Security within IoT Technology,

   - https://www.rapid7.com/globalassets/_pdfs/whitepaperguide/rapid7-leveraging-inter-chip-communication-analysis.pdf

- (4) Kaspersky ICS CERT researchers (2021), Kaspersky identifies significant security risks in widely-used Cinterion modems: https://usa.kaspersky.com/about/press-releases/kaspersky-identifiessignificant-security-risks-in-widely-used-cinterion-modems

- (5) Reza Vahidnia and F. John Dian (2021), Cellular Internet of Things for Practitioners, https://pressbooks.bccampus.ca/cellulariot/

- (6) Renesas (2022), Data Over UART with PPP,  https://www.mouser.com/pdfDocs/REN_r19an0071eu0150-lte-modules-data-over-uart-ppp_APN_20221012.pdf?srsltid=AfmBOor_Ti0_2v7S6bi_ZisDiqg0pGebXr3glSYftYWGLWqbEaZwix6

- (7) Deral Heiland and Carlota Bindner (2024), ANALYSIS OF CELLULAR BASED INTERNET OF THINGS (IOT) TECHNOLOGY, https://www.rapid7.com/globalassets/_pdfs/research/rapid7-2024cellular-iot.pdf

- (8) Jennifer C. Lin, Richard Y. Lin, and Salim S.I (2024), Cellular IoT Vulnerabilities: Another Door to Cellular Networks, https://www.trendmicro.com/vinfo/us/security/news/internet-of-things/cellular-iotvulnerabilities-another-door-to-cellular-networks

- (9)Texas Instruments (2024),TS3USB221E USB Multiplexer Datasheet , https://www.ti.com/lit/ds/symlink/ts3usb221e.pdf

- (10) Jesal Shah (2025), How USB Works: Communication Protocol (Part 2), https://www.circuitbread.com/tutorials/how-usb-works-communication-protocol-part-2

#BHUSA @BlackHatEvents
