---
title: "Houston, We Have a Problem Analyzing the Security of Low Earth Orbit Satellites"
speakers: ["Johannes Willbold"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/Johannes Willbold_Houston, We Have a Problem Analyzing the Security of Low Earth Orbit Satellites.pdf"
pages: 148
sha256: "4c2f858764f58d40d69e641a608e804d78a528009d23925a5a7b17446b7cc619"
text_chars: 35792
ocr_pages: 31
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:18:42Z"
---
# Houston, We Have a Problem Analyzing the Security of Low Earth Orbit Satellites

**Speakers:** Johannes Willbold  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Johannes Willbold_Houston, We Have a Problem Analyzing the Security of Low Earth Orbit Satellites.pdf` (148 pages)

## Slide 1

Houston, We Have a Problem Analyzing the Security of Low Earth Orbit Satellites

Johannes Willbold @jwillbold /jwillbold

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
RUHR RUB 8 SecHUMAN
¥ UNIVERSITAT
BOCHUM
SECURITY FOR HUMANS IN CYBERSPACE
Houston, We Have a Problem
Analyzing the Security of Low Earth Orbit Satellites
Johannes Willbold
W eWwittborc in /jwillbold : ;
```

## Slide 2

#### **<u>$whoami</u>**

Satellite & Space Systems Security Doctoral Student

Ruhr University Bochum, DE Visiting Researcher

Cyber-Defence Campus, CH Co-Founder of the SpaceSec Workshop

## Slide 3

#### **Space Odyssey**

**Distinguished Paper Award**

44th IEEE Symposium on Security and Privacy (S&P)

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Space Odysséy
Space Odyssey: An Experimental Software Security Analysis of Satellites
Johannes Willbo
Moritz Schloegel*t, Manuel
gele*, Maximilian Gerhardt,
Thorsten Holzt, Ali Abb
*Ruhr Univer;
Bochum, firstname.lastname @ rub.de
'CISPA Helmholtz Center for Information Security, lastname @ cispa.de
Abstract—Satellites are an essential aspect of our modern
society and have contributed significantly to the way we
live today, most notable through modern telecommunications,
global positioning, and Earth observation. In recent years, and
especially in the wake of the New Space Era, the number of
satellite deployments has seen explosive growth. Despite its
critical importance, little academic research has been con-
ducted on satellite security and, in particular, on the security of
onboard firmware. This lack likely stems from by now outdated
assumptions on achieving security by obscurity, effectively
preventing meaningful research on satellite firmware.
AAth |EEE Symposium on Security and Privacy (S&P)
in 2022 [2]. The vast majority of these satellites form mega-
constellations like Starlink, which plans to launch more than
AO, 000 satellites in the coming years [3].
Small satellites [4] are at the heart of this New Space Era
as thei and the widespread use of Commercial off-the-
shelf (COTS) components makes them affordable even for
small institutions. Furthermore, they cover a broad spectrum
of use cases ranging from commercial applications (like
Earth observation, machine-to-machine communication, and
Internet services) to research applications, such as technol-
ogy testing, weather and earthquake fore ng, and even
interplanetary missions [5|-[8].
Distinguished
Paper Award
```

## Slide 4

#### **Applications**

Global Positioning

Telecommunications

Earth Obervation

Research

Technology Testing

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Applications - ©
@
~~ |
=~ &
i (JG QAaey- mp”
Telecommunications Global Positioning Earth Obervation
a -
HR es
Research Technology Testing
```

## Slide 5

**Satellite Orbits**

## Slide 6

## **Satellite Orbits**

LEO
160 - 2k km

## Slide 7

## **Satellite Orbits**

MEO
2k - 35k km
LEO
160 - 2k km

## Slide 8

## **Satellite Orbits**

MEO
2k - 35k km
LEO
GEO
160 - 2k km
35786 km

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Satellite Orbits
==
-”=
-
MEO
LEO ~ ‘ vet
35786 km
```

## Slide 9

## **Satellite Orbits**

MEO
2k - 35k km
LEO
GEO
160 - 2k km
35786 km

## Slide 10

## **Context**

Space Segment

## Slide 11

## **Context**

ISL
Space Segment

## Slide 12

## **Context**

Space Segment

ISL

3U CubeSat

## Slide 13

## **Context**

ISL
Space Segment
34 cm
3U CubeSat
10 cm

## Slide 14

## **Context**

Space Segment

ISL

Ground Segment

## Slide 15

## **Context**

Space Segment

ISL

Ground Segment

## Slide 16

## **Context**

Space Segment

ISL

Ground Segment

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Context ,
Space Segment ——e
BANS
vo Ear
See: Ground Segment
e@
```

## Slide 17

## **Context**

Space Segment

ISL

Ground Segment

## Slide 18

## **Context**

Space Segment

ISL
Space
Protocol

Ground Segment

## Slide 19

## **Context**

Space Segment

ISL

Space Protocol

User Segment

Ground Segment

## Slide 20

#### **Our Journey ...**

Firmware Attacks

## Slide 21

#### **Our Journey ...**

Firmware Attacks

## Slide 22

#### **Our Journey ...**

System Analysis

Firmware Attacks

## Slide 23

#### **Our Journey ...**

System Analysis

Firmware Attacks

## Slide 24

#### **Our Journey ...**

System Analysis

Firmware Attacks

## Slide 25

#### **Our Journey ...**

System Analysis

Firmware Attacks

Live Demo

## Slide 26

#### **Our Journey ...**

System Analysis

Firmware Attacks

Live Demo

## Slide 27

#### **Our Journey ...**

System Analysis

Firmware Attacks Survey
Live Demo

## Slide 28

#### **Our Journey ...**

System Analysis

Firmware Attacks Survey
Live Demo

## Slide 29

#### **Our Journey ...**

System Analysis

Firmware Attacks Survey
Live Demo

## Slide 30

#### **Our Journey ...**

System Analysis

Bigger Picture

Firmware Attacks Survey
Live Demo

## Slide 31

**Firmware Attacks**

## Slide 32

## **ViaSat Incident**

Space Segment

Ground Segment

User Segment

## Slide 33

## **ViaSat Incident**

Space Segment

Ground Segment

User Segment

## Slide 34

## **ViaSat Incident**

Space Segment

Ground Segment

User Segment

## Slide 35

## **ViaSat Incident**

Space Segment

Ground Segment

User Segment

## Slide 36

## **ViaSat Incident**

Space Segment

Ground Segment

User Segment

## Slide 37

## **Firmware Attacks**

Space Segment

**?**

##### **?**

Ground Segment

Attackers

## Slide 38

## **Not so Novel**

## Slide 39

## **Not so Novel**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
~ Notso Novel
CONCERNING SECURITY THREATS AGAINST MISSIONS
348 REPLAY
Applicable to: Space Segment, Ground Segment, Space-Link Communication
Description: Transmissions to or from a spacecraft or be found system computers can
be intercepted, recorded, and played back ata later time
Possible Mission Impact: [f the recorded data were a command set from the ground to the
f and they are re-trapsi intended destination, they might be
not rejected, they
such as a mill a spacecraft rc
in the wrong direc ed away from the SUM phe reset
Miical onboard parameters)
349 SOFTWARE THREATS
Applicable to: Space Segment, Ground Segment
Description: Users, system operators, and programmers often make mistakes that can result
in security problems. Users or administrators can install unauthorized or unvetted sof
that might contain bugs, viruses, or spyware, which could result in system in
System operators might misconfigure a system resulting im securt
Programmers may introduce logic or implementation errors that could result i
ulneral nstabilty/reliability. Weaknesses may be di after
‘operatic smal threat agents might attempt to ©
Possible Mission Impact: Software threats could result i os
of spacecraft control, unauthorized spacecraft control
3.4.10 CRPSEHORIZED ACCESS
Applicable to: Spo een
Description: Access control policies based om strong authentication provide a means by which
‘only authorized entities are allowed to perform system actions, while all others are probil
Possible Mission Impact: An access control breach would allow an unauthorized entity to
take control of a ground system or a ground system network, shut down a ground system,
upload unauthorized commands to a spacecraft, execute unauthorized commands aboard a
: : mmauthorized data, contaminate archived data, or completely shut
down a mission k access controls are in place, unauthor:
jon of data might result in unauthorized 9
be obtained. Social engineering could be employed to obtain identities
or other technical details permitting unauthorized ac
```

## Slide 40

## **Not so Novel**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
~ Notso Novel .
348 REPLAY
Applicable to: Space Segment, Ground Segment, Space-L
Description: Transm: or from a spacecraft or bet —— ee e
be intercepted, recorded, an: back ata later time
MARCH 2020 A REPORT OF
Possible Mission Impact: [f the recorded data THE cis
pa and they are " AEROSPACE
eae Teene re Sait
aft operations, such PROJECT
Spacecraft is in an unintende
ng direction, solar arrays point
3.49 SOFTWARE THREATS
Applicable to: Sezment, Ground Segment
Description perators, and programmers often mak .
ators ca install unauthor,
yyware, which could res
we a system results
ibility. Weaknesses may b
at agents might attempt tc
Applicable to: Sp mn
Description: Access cor ietes based on strong authentication p
nly authorized e ed to perform system action
Possible Mission Impact ss control breach would
tak of a ground system network
2 spacecraft, execute unauthor
ized data, contaminate archived
cess controls ate in place, unsauthori
result in unauthorized 4
engineering could
```

## Slide 41

## **Not so Novel**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
~ Notso Novel
CONCERNING SECURITY THREATS AGAINST MISSIONS
348 REPLAY
Applicable to: Space Segment, Ground Segment, Space-Link Communication
Description: Transmissions to or from a spacecraft or be em computers can
intercepted, recorded, and played back ata later time
Possible Mission Impact: [f the recorded data were a command set from the ground to the
pacecraft and they are re-trap pilee stcncied destination, they might be
Counterspace weapons that are rever
ble and have limited
ally suited for sit
Pponent may want
executed, potential me not rejected, they
could resulpggtiigpeate spacecraft such as a mill a spacecraft rc
Mir the result that a space tumbling
in the wrong direc eset
Miical onboard parameters)
349 SOFTWARE THREATS
Applicable to: Space Segment, Ground Segment Ry 7 9 3d States from in
/ may believe that
Description: Users, system operators, and programmers often make mistakes that can result Alustration ‘below the threshold
sers or administrators can install unauthorized or unvetted softw yberatacks can be ., not trigger the vi
that might contain bugs, viruses, or spyware, which could result in system in thing ts trying to prevent) while creat
used to take contr
System operators might misconfigure a system resulting in security  weakne of 2 ficant operational challenges for th
Programmers may introduce logic or implementation errors that could result ve that make the prospect
ulneral astabilty/reliability, Weaknesses may be discovere
‘operatic siemal threat agents might attempt to exploit
Imited battle damage assess
Possible Mission Impact: Software threats could result i os aries in many situation
of spacecraft control, unauthorized spacecraft control Jt reliable battle damage at
3.4.10 CRSEFORIZED ACCESS ns with the confidence
Applicable to Spe en y costful. Further pons that
y duce collateral darnage in space, such
tan P run th
Description: Access control policies based om strong authentication provide a means by which
only authorized entities are allowed to perform system actions, while all others are probi Fisk of escalating a conflict and turning
Possible Mission Impact: An access control breach would allow an unauthorized enti
take control of a ground system or a ground system network, shut down a
upload unauthorized commands to a spacecraft, execute unauthorize
mauthorized data, contaminate archi
sion k access controls are in place, unauthor:
jon of data might result in unauthorized 9
be obtained. Social engineering could
or other techni
```

## Slide 42

## **Not so Novel**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Not so Novel
CCSDS REPORT CONCERNING SECURITY THREATS AGAINST SPACE MISSIONS,
348 REPLAY
Applicable to: Space Segment, Ground Segment, Space-Link Communication.
Description: Transmissions to or from a spacecraft or between ground system computers can
b
corded, and played back ata later time
Possible Mission Impact: If the recorded data were a comin the ground to the
ination, they might be
are not rejected, they
a spacecraft rc
real onboard parameters)
349 SOFTWARE THREATS:
Applicable to: Space Segment, Ground Segament
Description: Users, system operators, and programmers often make mistakes that can result
Users or administrators can install unauthorized or unvetted software
ntain bugs, viruses, or spyware, which could result in system instability
r misconfigure a system resulting in security weaknes
summers may introduce logic or implementation errors that could result in system
bilities, or instability reliability. Weaknesses may be discovered after @ mission is
which extemal threat agents might attempt to exploit to inject instructions
softwate, of configuration changes
Possible Mission Impact: Soflware threats could result in loss of data and safety
vss of spacecraft control, unauthorized spacecraft control, ot Loss of mission
3410
Applicable to: Spo
Description: Access control policies based on strong authentication provide a means by which
‘only authorized entities are allowed to perform system actions, while all others are p
Possible Mission Impact: An access control breach would allow an unauthorized entity 10
take control of a ground system or a ground system network, shut ¢
upload unauthorized commands to a spacecraft, execute unauthorized commands abo
in unauthorized data, contaminate archived data, or co
sak access controls are in place, unauthorized access migh
passwords might be obtained. Social en;
otifies, passwords, or other techni
cesps 3501-62
ustration
yeratacks ca
used to take contr
user terminals that con cs | Counterspace weapons that are revers
ace all potential intrusion points ble, dificult to atvibute, and have limited
berattacks. Cyberattacks can be used to | public awareness are ideally suited
monitor data traffic patterns (i.e, which | uations in which an opponent may want
rupted | mind ofits opponent, or achieve afait ac
data in the system. While cyberattacks ut triggering an escala
igh degree of understanding of | response. For examp
uct. Cyberattacks can be contract. | such attacks wil stay below the tres
to prvate groups or individuals, | for escalation (Le, not trigger the very
ans that a state or non-state ac. | thing itis trying to prevent) while creating
Fas posal cyber threat . that make the prospect of
intervention more costly and protracted
ystems can Fe | Cocversely, counterspace weapons that
ult in data loss, widespread disruptions, | haye limited battle damage assessment
and even permanent loss of a satelite. | 6, ehat rik collateral damage may be less
ntrol of a satellite through a cyberat- | without reliable battle damage as:
attack could shut down al c plan operations with the co
munications and permanently damage | its counterspace actions hi
ful. Furtherme
duce collateral da
large amounts of sp
the satellite by expending its propellan
upply or damaging its electronics and
Accurate and timely attribution
ick can be difficult, if not | risk of escalating a conflict and turning
ause attackers can use a | other nations against the attacker
dso heir iden
tity, such as using hijacked servers to
THREAT
CHARACTERISTICS
he types of space threats de
ribed above have distinctly different
characteristics make them mor
pace threats are dificult t
attribute or have fully reversible effects
such as n vers. High-powered
laser le, re “silent” and can
arry out an attack with little public
awareness that anything has ha
Other types
duce effec
Cybersecurity Protections for Spacecraft: A Threat Based
ssment and Research Department (CARD)
Cybersecurity Subdivision (CSS)
Prepared for
U.S. GOVERNMENT AGENCY
Contract No, FA8802-19-C-0001
Authorized by: Defense Systems Group
Distribution Statement A: Ost 200 datbaton unites
```

## Slide 43

**Outdated Assumptions**

## Slide 44

## **Myth of Inaccessibility**

$$$ → $ Affordable Ground Stations

## Slide 45

## **Myth of Inaccessibility**

$$$ → $

Affordable Ground Stations

Ground Station as a Service GSaaS

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Myth of Inactessibility
~
> Fs
\\
Affordable ° Ground Station as a Service
Ground Stations GSaaS
```

## Slide 46

## **Myth of Inaccessibility**

$$$  →  $
More Satellites
Ground Station as a Service
Affordable
GEO → LEO
Ground Stations GSaaS

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Myth of Inactessibility
~
> Fs
\\
Affordable ° Ground Station as a Service
Ground Stations GSaaS
eb £e
More Satellites
GEO — LEO
```

## Slide 47

**Security by Obscurity** _“_<sup>_No Insights <=> No Attacker_</sup>

## Slide 48

## **Security by Obscurity**

- _“_<sup>_~~No Insights <=> No Attacker~~_</sup>

## Slide 49

## **Security by Obscurity**

_“_<sup>_~~No Insights <=> No Attacker~~_</sup>

More Developers More People Involved

## Slide 50

## **Security by Obscurity**

_“_<sup>_~~No Insights <=> No Attacker~~_</sup>

More Developers More People Involved

###### Commercial off-the-Shelf (COTS) Components

## Slide 51

## **Security by Obscurity**

_“_<sup>_~~No Insights <=> No Attacker~~_</sup>

More Developers More People Involved

Commercial off-the-Shelf
(COTS)
Components

Higher Stakes Critical Infrastructure

## Slide 52

## **Attacker Goals**

###### Denial of Service

## Slide 53

## **Attacker Goals**

Denial of Service

Malicious Data
Interaction

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Attacker Goals
@
[S
QO
Denial of Service ; Malicious Data
Interaction
```

## Slide 54

## **Attacker Goals**

Denial of Service

Seizure of Control

Malicious Data
Interaction

## Slide 55

## **Attacker Goals**

Seizure of Control
Malicious Data
Denial of Service
Interaction

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Attacker Goals _
e-
— i
> .¥
Seizure of sontrol Malicious Data
Interaction
e
Denial of Service
```

## Slide 56

## **Attacker Goals**

Seizure of Control

## Slide 57

## **Attacker Goals**

Seizure of Control

## Slide 58

## **Components**

Bus
Payload

## Slide 59

## **Components**

Bus
Payload

## Slide 60

## **Components**

Bus
Payload

## Slide 61

## **Components**

Bus
?
Payload

## Slide 62

## **Components**

ADCS
EPS
CDHS
Payload
COM

## Slide 63

## **Components**

ADCS
EPS
CDHS
Payload
COM

## Slide 64

## **TC / TM Flow**

###### **ADCS**

###### **EPS**

Telecommand (TC)

Telemetry (TM)

COM CDHS
Decode Parse
Authenticate Execute
Repackage Respond

**Payload**

## Slide 65

## **TC / TM Flow**

###### **ADCS**

###### **EPS**

TC / TM Traffic

Payload Traffic

COM
Decode
Authenticate
Repackage

**PLCOM**

CDHS
Parse
Execute
Respond

**PDHS**

## Slide 66

## **Attack Path**

**COM**

**PLCOM**

**CDHS**

PDHS

**Bus**

## Slide 67

## **Attack Path**

PLCOM

**PDHS**

Hack CySat 2022 & 2023
CySat 202

## Slide 68

## **Attack Path**

**COM**

Bypass COM Protection Missing AC Insecure Protocol Outdated Crypto Timing Side Channels Leaked Keys Timed Backdoor ...

###### **CDHS**

**Bus**

## Slide 69

## **Attack Path**

**COM CDHS** Bypass COM Protection Deploy Attacker Payload [...] Firmware Update Signed Image Slow Upload Complex System

###### **Bus**

## Slide 70

## **Attack Path**

COM CDHS Bus
Bypass COM Protection Deploy Attacker Payload
[...] Firmware Update
Dangerous TC
Vulnerable TC

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Attack Path
COM CDHS Bus
¢ Bypass COM Protection e Deploy Attacker Payload
= [...] = Firmwaretpedate
= Dangerous TC
# Vulnerable TC
```

## Slide 71

## **Attack Path**

COM CDHS Bus
Bypass COM Protection Deploy Attacker Payload Hijack Bus Control Flow
[...] Firmware Update Full Bus Privileges
Dangerous TC
Vulnerable TC

## Slide 72

## **Attack Path**

COM CDHS Bus
Bypass COM Protection Deploy Attacker Payload Hijack Bus Control Flow
[...] Firmware Update Full Bus Privileges
Dangerous TC
Vulnerable TC

## Slide 73

#### **Objectives**

1 Bypass COM Protection
2 Dangerous / Vulnerable TC
3 Hijack Bus Control Flow
4 Full Bus Privileges

## Slide 74

**Satellite Case Studies**

## Slide 75

## **Approach**

System Design
Protocols

## Slide 76

**ESTCube-1**

## Slide 77

#### **ESTCube-1**

[1]

**ESTCube-1**

E-Sail (Electric Solar Wind Sail) Proplsion Peripherals

Developed by University of Tartau

ARM STM32 Payload Platform

## Slide 78

#### **Custom Protocol**

COM

Sender Subsystem ID Recipient Subsystem ID Flow Control Flags TX seq. TX seq. Inner Payload Fletcher-16 Checksum

## Slide 79

#### **Custom Protocol**

COM
ID Subsystem
0 EPS
1 COM
2 CDHS
Sender Subsystem ID
...
Recipient Subsystem ID
5 Ground Station
Flow Control Flags
TX seq. TX seq.
Inner Payload
Fletcher-16 Checksum

## Slide 80

#### **Custom Protocol**

COM
ID Subsystem
0 EPS
1 COM
2 CDHS
Sender Subsystem ID
...
Recipient Subsystem ID
5 Ground Station
Flow Control Flags
bit 0 bit 1 bit 2 bit 3 bit 4 bit 5 bit 6 bit 7
TX seq. TX seq.
Byte 0 Command Identifier (MSB)
Inner Payload Byte 1 Command Identifier (LSB)
Byte 2 Source Block ID
Fletcher-16 Checksum
Byte 3 Length
...
Args

## Slide 81

#### Security Analysis

###### **COM**

###### **CDHS**

Bypass COM Protection Missing TC Protection

- 1 **int sch_handle_command** ( **scheduler_packed_cmd_t** ∗pCmd) { 2 // ! simplified !

- 3 sch_unpack_command(&g_command, pCmd);

- 4 // ...

- 5 handler_func = &handler_table[g_command.handler_func_index] ; 6 // ...

**bit 0 bit 1 bit 2 bit 3 bit 4 bit 5 bit 6 bit 7** Byte 0 Command Identifer i <u>(MSB)</u> Byte 1 Command Identifer (LSB) i Byte 2 Source Block ID Byte 3 Length ... Args

- 7 retval = (∗handler_func) (&g_command) ;

- 8 }

## Slide 82

#### Security Analysis

**COM CDHS** Bypass COM Protection Missing TC Protection

- 1 **int sch_handle_command** ( **scheduler_packed_cmd_t** ∗pCmd) {

- 2 // ! simplified !

- 3 sch_unpack_command(&g_command, pCmd);

- 4 // ...

- 5 handler_func = &handler_table[g_command.handler_func_index] ; 6 // ...

**bit 0 bit 1 bit 2 bit 3 bit 4 bit 5 bit 6 bit 7** Byte 0 Command Identifer i <u>(MSB)</u> Byte 1 Command Identifer (LSB) i Byte 2 Source Block ID Byte 3 Length ... Args

- 7 retval = (∗handler_func) (&g_command) ; 8 }

## Slide 83

#### Security Analysis

**COM CDHS** Bypass COM Protection Missing TC Protection

   - 1 **int sch_handler_set_raw_memory** ( **scheduler_cmd_t** * pCmd) { 2 **raw_mem_access_cmd_t** * pAddr = pCmd−>pCmdArgs;

   - 3 **char** * pWriteData;

   - 4

   - 5 **if** (pAddr) {

   - 6 **if** (g_sch_exec_mode != 1 ) {

   - 7 /* exception and return */

   - 8 }

- 9 **char** * pWriteData = &pAddr−>start_of_data_buf;

- 10 **if** (pAddr−>filesystem_target) {

- 11 // [...]

- 12 } **else** {

- 13 memcpy(pAddr−>targetAddr, 14 &pAddr−>start_of_data_buf, 15 pAddr−>writeLength);

- 16 } 17 } 18 // ... 19 }

## Slide 84

#### Security Analysis

**COM CDHS** Bypass COM Protection Missing TC Protection

   - **1 int sch_handler_set_raw_memory ( scheduler_cmd_t * pCmd) { 2 raw_mem_access_cmd_t * pAddr = pCmd−>pCmdArgs; 3 char * pWriteData;**

   - **4**

   - **5 if (pAddr) {**

- **6 if (g_sch_exec_mode != 1 ) { 7 /* exception and return */ 8 } 9 char * pWriteData = &pAddr−>start_of_data_buf;**

- **10 if (pAddr−>filesystem_target) {**

- **11 // [...]**

**12 } else { 13 memcpy(pAddr−>targetAddr, 14 &pAddr−>start_of_data_buf, 15 pAddr−>writeLength); 16 } 17 } 18 // ... 19 }**

## Slide 85

#### Real-World Test

**COM** Bypass COM Protection Missing TC Protection

**CDHS** Deploy Attacker Payload Dangerous TC

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Real-World Test = 2)
. Te COM CDHS
e Bypass COM Protection e Deploy Attacker Payload
= Missing TC Protection = Dangerous TC
```

## Slide 86

#### Real-World Test

**COM**

###### **CDHS**

Bypass COM Protection Missing TC Protection

Deploy Attacker Payload Dangerous TC

Image Source: Maximilian Gerhardt, Reverse Engineering Satellite Firmware for Security Evaluation, 13. Dec. 2021

## Slide 87

# **OPS-Sat**

## Slide 88

#### **System Chart**

[2]

**Experimenter**

Operated by ESA Open for Research

S-/X-Band, SDR, Optical Rx., Camera, ... Peripherals

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
System Chart
COM EPS
CDHS
GPS ADCS
[2]
e
Experimenter
S-/X-Band, SDR, Optical Rx., Camera, ...
@) ted by ESA ;
ee Peripherals
Open for Research .-
```

## Slide 89

**System Chart**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
System Chart
COM EPS
CDHS
GPS ADCS
```

## Slide 90

#### **System Chart**

1

1 Cubesat Space Protocol (CSP)

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
System Chart .
@ CG) Cubesat Space Protocol (CSP)
COM ———»> EPS
CDHS
GPS ADCS
```

## Slide 91

#### **System Chart**

1

1
Cubesat Space Protocol (CSP)
2
2 AVR32 AT32UTC3, FreeRTOS

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
System Chart .
@ CG) Cubesat Space Protocol (CSP)
com > EPS
CDHS (2)
ADCS
Q) AVR32 AT32UTC3, FreeRTOS
```

## Slide 92

#### **System Chart**

1

1
Cubesat Space Protocol (CSP)

2

2 AVR32 AT32UTC3, FreeRTOS

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
System Chart .
@ CG) Cubesat Space Protocol (CSP)
COM ———» EPS
CDHS ( 2 ) ;
3 ADCS
Q) AVR32 AT32UTC3, FreeRTOS
```

## Slide 93

#### **System Chart**

1

3

1
Cubesat Space Protocol (CSP)

2
2 AVR32 AT32UTC3, FreeRTOS

3 CCSDS Protocl Stack

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
System Chart .
@ CG) Cubesat Space Protocol (CSP)
COM ———» EPS
ebris ADCS
Q) AVR32 AT32UTC3, FreeRTOS
G) CCSDS Protocl Stack
```

## Slide 94

#### **System Chart**

1
Cubesat Space Protocol (CSP)
1
2
2 AVR32 AT32UTC3, FreeRTOS
3
3 CCSDS Protocl Stack
4
4 ARM Cortex A9, Yocto Linux

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
System Chart .
@ CG) Cubesat Space Protocol (CSP)
COM ———»> EPS
CDHS(2)
Q) AVR32 AT32UTC3, FreeRTOS
G) CCSDS Protocl Stack
() ARM Cortex A9, Yocto Linux, “
```

## Slide 95

#### **UHF-Stack**

1

###### **Cubesat Space Protocol (CSP) v1**

TCP/IP Oriented Design

_Source: https://en.wikipedia.org/wiki/Cubesat_Space_Protocol_

/ libcsp

## Slide 96

#### **UHF-Stack**

1

###### Cubesat Space Protocol (CSP) v1

Security Features

Security Issues

HMAC-SHA1 Authentication XTEA Encryption Support

1. MAC comparison leaks timing data #44 memcmp to compare the digest

2. HMAC doesn't protect headers #45 Same problem for the CRC checks

3.  XTEA encrypt packet nonce too predictable #162 const uint32_t nonce = (uint32_t)rand();

_Authors_ : Issues fixed in libcsp v2

## Slide 97

#### **S-Band Stack**

3

###### CCSDS - Protocol Stack

IPSec
...

Message Abstraction

Space Packet Protocol

IP Protocol TM Space Link TC Space Link AOS Space Proximity-1 Protocol Protocol Data Link P. Data Link Lay.

Sync. and Channel Coding Sublayer

## Slide 98

#### **S-Band Stack**

3

###### CCSDS - Protocol Stack

IPSec
...

Message Abstraction

Space Packet Protocol

IP Protocol TM Space Link TC Space Link AOS Space Proximity-1 Protocol Protocol Data Link P. Data Link Lay.

Sync. and Channel Coding Sublayer

## Slide 99

#### **Unprotected TCs**

**COM**

- 1 **int csp_route_security_chek** (...) {

- 2 **if** (packet->id.flags & CSP_FXTEA) {

- 3 csp_log_error("Received XTEA encrypted packet, but CSP was compiled without XTEA support. Discarding packet");

- 4 }

- 5

   - 6 // ...

   - 7

   - 8 **if** (packet->id.flags & CSP_FHMAC) {

   - 9 csp_log_error("Received packet with HMAC, but CSP was compiled without HMAC support. Discarding packet");

- 10

   - }

- 11

- 12 // ...

- 13

- }

## Slide 100

#### **Unprotected TCs**

###### **COM CDHS**

Bypass COM Protection Missing TC Protection

   - 1 **int sch_handler_set_raw_memory** ( **scheduler_cmd_t** * pCmd) { 2 **raw_mem_access_cmd_t** * pAddr = pCmd−>pCmdArgs;

   - 3 **char** * pWriteData;

   - 4

   - 5 **if** (pAddr) {

   - 6 **if** (g_sch_exec_mode != 1 ) {

      - /* exception and return */

   - 7

   - 8 }

- 9 **char** * pWriteData = &pAddr−>start_of_data_buf;

- 10 **if** (pAddr−>filesystem_target) { 11 // [...]

- 12 } **else** {

- 13 memcpy(pAddr−>targetAddr, 14 &pAddr−>start_of_data_buf, 15 pAddr−>writeLength); 16 } 17 } 18 // ... 19 }

## Slide 101

#### **Unprotected TCs**

**COM CDHS** Bypass COM Protection Missing TC Protection

   - **1 int sch_handler_set_raw_memory ( scheduler_cmd_t * pCmd) { 2 raw_mem_access_cmd_t * pAddr = pCmd−>pCmdArgs;**

   - **3 char * pWriteData;**

   - **4**

   - **5 if (pAddr) {**

      - **if (g_sch_exec_mode != 1 ) { /* exception and return */**

   - **6**

   - **7**

   - **8 } 9 char * pWriteData = &pAddr−>start_of_data_buf; if (pAddr−>filesystem_target) {**

- **10**

   - **// [...]**

- **11**

- **12 } else { 13 memcpy(pAddr−>targetAddr, 14 &pAddr−>start_of_data_buf, 15 pAddr−>writeLength); 16 } 17 } 18 // ... 19 }**

## Slide 102

**Vulnerable TC**

## Slide 103

#### **Vulnerable TC**

ADCS Server
Cubesat Space Protocol Parameter DB
(CSP)
...
UHF CSP => SPP

## Slide 104

#### **Vulnerable TC**

ADCS Server
Cubesat Space Protocol Parameter DB
(CSP)
...
UHF CSP => SPP
PUBSUB_MonitorEvent
SUBMIT_SetPowerState
Space Packet Protocol
INVOKE_GetGPSData
(SPP)
S-Band ...
PROGRESS_GetSummary

## Slide 105

#### **Vulnerable TC**

ADCS Server
Cubesat Space Protocol Parameter DB
(CSP)
...
UHF CSP => SPP
PUBSUB_MonitorEvent
SUBMIT_SetPowerState
Space Packet Protocol
INVOKE_GetGPSData
(SPP)
S-Band ...
PROGRESS_GetSummary

## Slide 106

Vulnerable TC
ADCS Server
Cubesat Space Protocol Parameter DB
(CSP)
...
UHF CSP => SPP
PUBSUB_MonitorEvent
Message
SUBMIT_SetPowerState
Abstraction
Space Packet Protocol
INVOKE_GetGPSData Message
(SPP)
Abstraction Layer
...
(MAL)
S-Band
Space Packet
PROGRESS_GetSummary
Protocol

## Slide 107

Vulnerable TC
ADCS Server
Cubesat Space Protocol Parameter DB Custom Byte
(CSP) Parsing
...
UHF CSP => SPP
PUBSUB_MonitorEvent
Message
SUBMIT_SetPowerState
Abstraction
Space Packet Protocol
INVOKE_GetGPSData Message
(SPP)
Abstraction Layer
...
(MAL)
S-Band
Space Packet
PROGRESS_GetSummary
Protocol

## Slide 108

Vulnerable TC
ADCS Server
Cubesat Space Protocol Parameter DB Custom Byte
(CSP) Parsing
...
UHF CSP => SPP
PUBSUB_MonitorEvent
Message
SUBMIT_SetPowerState
Abstraction
Space Packet Protocol
INVOKE_GetGPSData Message
(SPP)
Abstraction Layer
...
(MAL)
S-Band
Space Packet
PROGRESS_GetSummary
Protocol

## Slide 109

#### **Vulnerable TC**

Cubesat Space Protocol (CSP)

ADCS Server

- 1 **void task_adcs_servr** () {

- 2 **char** log_file_name [32];

- 3

- 4 csp_listen(socket, 10);

- 5 csp_bind(socket, port);

- 6

- 7 **do** {

- 8 **do** {

- 9

   - conn = csp_accept(socket, 0xff);

- 10 } **while** (do_wait_for_conn);

- 11

- 12 packet = csp_read(conn, 10);

- 13 **if** (packet) {

- 14

- 15

- 16

- 17

   - packet_data = packet->data;

   - **switch** (*packet_data) {

   - // [...]

   - **case** SET_LOGFILE: {

- 18 packet_data = packet->data + 0xf;

- 19 log_file_name[0] = '\0';

- 20 strcat(log_file_name,packet_data);

- 21 // ... 22 } 23 } 24 } 25 }

## Slide 110

#### **Vulnerable TC**

Cubesat Space Protocol (CSP)

ADCS Server

   - **1 void task_adcs_servr () {**

   - **2 char log_file_name [32];**

   - **3**

   - **4 csp_listen(socket, 10);**

   - **5 csp_bind(socket, port);**

   - **6**

   - **7 do {**

   - **8 do {**

   - **9 conn = csp_accept(socket, 0xff);**

- **10 } while (do_wait_for_conn);**

- **11**

- **12 packet = csp_read(conn, 10);**

- **13**

- **14**

- **15**

- **16**

- **17**

   - **if (packet) {**

   - **packet_data = packet->data;**

   - **switch (*packet_data) {**

   - **// [...]**

   - **case SET_LOGFILE: {**

- **18 packet_data = packet->data + 0xf; 19 log_file_name[0] = '\0';**

   - **strcat(log_file_name,packet_data);**

**20 21 22 } 23 } 24 } 25 }**

- **// ...**

## Slide 111

#### **Vulnerable TC**

Cubesat Space Protocol (CSP)

ADCS Server

   - **1 void task_adcs_servr () {**

   - **2 char log_file_name [32];**

   - **3**

   - **4 csp_listen(socket, 10);**

   - **5 csp_bind(socket, port);**

   - **6**

   - **7 do {**

   - **8 do {**

   - **9 conn = csp_accept(socket, 0xff);**

- **10 } while (do_wait_for_conn);**

**11**

- **12**

   - **packet = csp_read(conn, 10);**

- **13 if (packet) {**

- **14 packet_data = packet->data;**

- **15 switch (*packet_data) {**

- **16**

   - **// [...]**

- **17 case SET_LOGFILE: {**

- **18 packet_data = packet->data + 0xf;**

- **19 log_file_name[0] = '\0';**

- **20 strcat(log_file_name,packet_data); 21 // ... 22 } 23 } 24 } 25 }**

## Slide 112

#### **Defenses - 404?**

**COM CDHS Bus** Bypass COM Protection Deploy Attacker Payload Missing TC Protection Vulnerable TC

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
‘Defenses - 404?
e
e
Te COM CDHS Bus ,
e Bypass COM Protection e Deploy Attacker Payload
= Missing TC Protection # Vulnerable TC
e
e
e
e e
e
@
```

## Slide 113

#### **Defenses - 404?**

**COM** Bypass COM Protection Missing TC Protection

**CDHS**

**CDHS Bus** Deploy Attacker Payload Hijack Bus Control Flow Vulnerable TC

## Slide 114

#### **Defenses - 404?**

**COM**

Bypass COM Protection Missing TC Protection No OS-Defenses ASLR NX Stack

**CDHS**

Deploy Attacker Payload Vulnerable TC

**Bus** Hijack Bus Control Flow

## Slide 115

#### **Defenses - 404?**

**COM**

Bypass COM Protection Missing TC Protection No OS-Defenses ASLR NX Stack

###### **CDHS**

Deploy Attacker Payload Vulnerable TC

**Bus** Hijack Bus Control Flow

No SW-Defenses

Stack Cookies

## Slide 116

#### **Defenses - 404?**

**COM**

Bypass COM Protection Missing TC Protection No OS-Defenses ASLR NX Stack

###### **CDHS**

Deploy Attacker Payload Vulnerable TC

**Bus** Hijack Bus Control Flow Full Bus Privileges

No SW-Defenses

Stack Cookies

## Slide 117

#### **Defenses - 404?**

**COM**

Bypass COM Protection Missing TC Protection No OS-Defenses ASLR NX Stack

###### **CDHS**

**Bus** Hijack Bus Control Flow Full Bus Privileges

Deploy Attacker Payload Hijack Bus Control Flow Vulnerable TC Full Bus Privileges Privilege-free RTOS

No SW-Defenses

Stack Cookies

## Slide 118

**Demo Setup**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Demo Setup
Hook
20— --Oro-
-O00r: O-O-Or-0Or
-OOreeee a
CCOK-O0ee- OC -H- OKO DOeree
-e-O00rr Or coOrrro yOro
-Or-Or-000-0000C Oreo
YR ORK KOKKKKH- OO: -oCOr
.OOrH--9000r-00K -Oo-00Fr
Or-H—COP CORK Cer Kk Serre
2-O900K-O0- Or 00000r-O
we--00R--O0r-000-0-0¢
O-0O0F X- OOK O-O-0OK-H-y YOO-OO- OL
y-O00r O-c000O-rrer-O-Orrraoo
*-Orro mer Or OK HK OC00OKKO00COOeF KK
DO-Or -O-00—-0-6—
OSere HO 000K OK O- OOF KR KKK KO
20-00 =—Oee —-O--Oree- Or ore
200-0 e--OOr -—CO--00OrK-- 00
-OOrr Oro” COreK9000r0
+.-o00- 200" -OK- KH OOK KO,
ro 2H OreKH-O- OF D-O0O-
2OOO-Ororr -Ore:
Ieee K Ore -Ore
oocoooe
CO-or-
xr OC
```

## Slide 119

## **Emulation Overview**

TC Handlers
OBSW
AVR32
QEMU
UHF
Sensors
Simulation Agent

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Emulation Overview .
Cc
TC Handlers =z n
m™ 3
=
OBSW oS
5 et,
AVR32 S 5
os
ra)
mm)
( on
QEMU
```

## Slide 120

## **Emulation Overview**

Telecommand
TC Handlers
TCP
Telemtry
OBSW
AVR32
QEMU
UHF
Sensors
Simulation Agent

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Emulation Overview .
Telecommand
Cc
TC Handlers = n
"TI =| TCP
OBSW wn = Telemtry
5 =
AVR32 S 5
“  &
fe)
|
a
QEMU
```

## Slide 121

## **Emulation Overview**

Telecommand
TC Handlers
TCP
Telemtry
OBSW
Sensor Values
AVR32
TCP
Flight Manuvers
QEMU
UHF
Sensors
Simulation Agent

## Slide 122

## **AVR32-QEMU**

404 - AVR32 Not Found

AVR32
QEMU

## Slide 123

## **AVR32-QEMU**

404 - AVR32 Not Found

AVR32

QEMU

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
- AVR32-QEMU is
404 - AVR32 Not Found QEMU
RUHR-UNIVERSITAT BOCHUM
Hacking the Stars: A Fuzzing Based Sei
Assessment of CubeSat Firmware
Florian Géhler
```

## Slide 124

## **AVR32-QEMU**

404 - AVR32 Not Found

AVR32

**QEMU**

Florian Göhler AVR32 in QEMU from Scratch Incl. I2C, SPI, PDCA, etc. Blog: _How to add a new architecture to QEMU - Part 1-4_

## Slide 125

# **Live Demo**

- 1 $> ./access-satellite.

- 2 [*] Uploading TC ...

- 3 [*] Deploying payload ...

- 4 [*] Payload written to flash ...

- 5 [*] Rebooting ... 6 [*] $$$

## Slide 126

**Flying Laptop**

## Slide 127

#### **Flying Laptop**

[3]

**Technology Tester**

De-orbit mechanism, AIS, Camera, etc... Peripherals

SPARC LEON 3 - OBC from Airbus S&D Co-Developed by Airbus Space & Defense Bus Platform

## Slide 128

#### **CCSDS**

IPSec

Custom
...

Space Packet
IP
Protocol
TM Space Link TC Space Link AOS Space Proximity-1
Protocol Protocol Data Link P.
Data Link Lay.

Sync. and Channel Coding Sublayer

## Slide 129

#### **CCSDS - SDLP**

Space Link Frame Data Protocol Header

Space Link
Protocol Trailer

## Slide 130

#### **CCSDS - SDLS**

Space Link Security Frame Data Security Space Link Protocol Trailer Protocol Header Header Trailer

## Slide 131

# **Bigger Picture**

## Slide 132

### _“_ **But it's different for [...] satellites.**

## Slide 133

_“_ **But it's different for [...] satellites, .... right?**

## Slide 134

**Developer Survey**

## Slide 135

## **TC Protocols**

Custom Standard Weight
~ 1.3 kg
~ 5.4 kg
~ 120 kg

Weight ≈ Money

## Slide 136

## **TC Protocols**

Custom / Standard

||**1-50 kg**|**50-100 kg**|**> 100 kg**|
|---|---|---|---|
|Standard|1|1|4|
|Custom|6|1|0|
|Abstains|3|0|1|
|∑|10|2|5|

###### Weight ≈ Money

## Slide 137

## **TC Protocols**

Custom / Standard

||**1-50 kg**|**50-100 kg**|**> 100 kg**|
|---|---|---|---|
|Standard|1|1|4|
|Custom|6|1|0|
|Abstains|3|0|1|
|∑|10|2|5|

Weight ≈ Money

## Slide 138

## **TC Protocols**

Custom / Standard

||**1-50 kg**|**50-100 kg**|**> 100 kg**|
|---|---|---|---|
|Standard|1|1|4|
|Custom|6|1|0|
|Abstains|3|0|1|
|∑|10|2|5|

###### Weight ≈ Money

## Slide 139

## **TC Protocols**

Custom / Standard

||**1-50 kg**|**50-100 kg**|**> 100 kg**|
|---|---|---|---|
|Standard|1|1|4|
|Custom|6|1|0|
|Abstains|3|0|1|
|∑|10|2|5|

Weight ≈ Money

###### => Inaccessible Standard

## Slide 140

## **TC Protection**

Question: _Are_ **_any measures deployed_** _to prevent 3rd parties from controlling your satellite?_

8
6
9
4
Unknown*:
5
2 Prefer not to say /
3
Don't know
Yes No Unknown*

## Slide 141

## TC **Obscurity**

Question: **_What measures_** _are deployed to prevent 3rd parties from controlling your satellite? (Multiple Answers)_

4 5 2 4 *: Special knowledge 3 3 about .... 2 Access Control Special permit needed Encryption * ... Frequences, Modulation, etc. * ... Protocols

## Slide 142

_“_ **But it's different for *my* satellite**

## Slide 143

# **Impact**

1. Hack a Satellite

???

## Slide 144

## **Scenarios**

###### Orbital Access

###### 1 Attacking Inter-Sat Links

###### 2 Orbital Traffic Interception

###### 3 Kessler Syndrome

## Slide 145

**Lesson Learnt**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Lesson Learnt ~ :
@dd3399
```

## Slide 146

## **Lessons Learnt**

Firmware Attacks on Satellites are a thing

ViaSat Incident != Satellite Firmware Attack

Common Sat Protocols lack Security Security by Obscurity

## Slide 147

## **Lessons Learnt**

Missing TC Protection Missing State-of-the-Art Defenses Attacker Access to Orbit as Staging Ground Unknown Consequences

## Slide 148

# **<u>Thanks!</u>**

Firmware Attacks on Satellite Satellite Exploitation Objectives Three Satellite Case Studies Satellite Developer Survey Impact beyond Vulnerable Satellites Johannes Willbold - johannes.willbold@rub.de

@jwillbold

/jwillbold

- [1] ESTCube-1 Image: https://www.eoportal.org/satellite-missions/estcube-1

- [2] OPS-Sat Image: https://www.esa.int/ESA_Multimedia/Videos/2019/12/OPS-SAT_ESA_s_flying_lab_open_to_all

[3] Flying Laptop Image: https://www.irs.uni-stuttgart.de/en/research/satellitetechnology-and-instruments/smallsatelliteprogram/flying-laptop/
