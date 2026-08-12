---
title: "Breaking Amazon lockers by any means necessary"
speakers: ["Martin Vigo"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: null
source_pdf: "DEF CON 34/DEF CON 34 - Martin Vigo - Breaking Amazon lockers by any means necessary - into.pdf"
pages: 37
sha256: "bed9215cb97abe549ea2a82394a1976bf2c51c8fced98843c4f632f3db604031"
text_chars: 27976
ocr_pages: 19
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:25:12Z"
---
# Breaking Amazon lockers by any means necessary

**Speakers:** Martin Vigo  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Martin Vigo - Breaking Amazon lockers by any means necessary - into.pdf` (37 pages)

## Slide 1

# **Breaking into Amazon Lockers by any means necessary! Martin Vigo**

## Slide 2

Amstrad CPC 6128

#### Martín Vigo

- **Education**

   - Bachelor in Computer Science

   - Masters in Software Engineering

   - Multiple cybersecurity trainings & certifications

   - Court-Appointed IT Expert Witness in Spain

- **Professional career**

   - Software Engineer - **Apple**

   - Product Security - **Salesforce**

   - Red Teamer - **Meta**

   - Security research - **AppOmni**

- Founder of **Triskel Security** , a offensive cybersecurity consulting company

- **• Research**

   - Compromising online accounts by cracking voicemail systems - **DEF CON**

   - Even the LastPass will be gone, deal with it - **Blackhat**

   - Do-It-Yourself Spy Program: Abusing Apple's Call Relay Protocol - **Ekoparty**

   - Operation KAERB & my story of hunting down the thieves that stole my phone - **OSINTomaticos**

   - From email address to phone number, a new OSINT approach - **BSides Las Vegas**

   - The importance of protecting our privacy in Internet - **TEDx**

   - Phonerator, an advanced *valid* phone number generator for your OSINT needs - **Intelcon**

   - Ransombile, yet another reason to ditch SMS - **Recon Village @ DEF CON**

- **Mentorship**

   - Hacking competitions mentor & BSides Barcelona organizer

   - Specialized trainings and masterclasses for various Law Enforcement agencies

   - University lectures, seminars & students coaching

## Slide 3

Tierra de Hackers _Tu noticiero de ciberseguridad hecho podcast_

@tierradehackers | <u>tierradehackers.com</u>

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Tierra de Hackers
Tu noticiero de ciberseguridad hecho podcast
@tierradehackers | tierradehackers.com T | F RE
LE
ERS
```

## Slide 4

### **What started it all…**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
What started it all...
he Ubertooth Retirement
t* Blog Posts by Tag
About
‘Contact 22 December 2022 17:44 by Straithe and Elizabeth (ubertooth) (permalink)
tFree Stuff Program
H Jobs After 12 years and 17 production runs, Gréat Scott Gadgets is retiring our first product) Ubertooth One, from our hardware catalog.
i; Merch
§ Open Source Ethos
: Support our Work
}Upcoming Events
#Where to Buy
GSG’s founder Michael Ossmann designed Ubertooth One because he wanted a device that could detect and monitor Bluetooth. At the time, §
such instruments existed but cost at least five figures—prohibitively expensive for most security researchers. His goal was to design an open-}
source, affordable-to-make tool that anyone in the security community with basic soldering skills could assemble. At the project’s inception, |
his intent was not to sell hardware but to provide a solution to a problem that no one else had solved. However, demand from the community
prompted him to start GSG and launch a Kickstarter campaign that funded the first production.
```

## Slide 5

### **2 types of lockers**

## Slide 6

### **My target**

- No internet connectivity

- No integrated camera

- Usually installed outdoors

- • Completely BLE operated • The most common in Spain

## Slide 7

# Packet ≠ Package Locker ≠ Cabinet

## Slide 8

Attacking the BLE protocol

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
TARGET ACQUIRED A VULNERABILITY DETECTED
PROTOCOL BLE a CVE-2023
VERSION: 5.4 7. H
STATUS: VULNERABLE CT: HIGH
T: AVAILABLE
EXPLOIT PATH MEMORY DUMP
>|
f
CONNECTION HIJACK
)
. keafyd
aA
ws
SUCCESS
Attacking the BLE protocol
```

## Slide 9

### **1-slide BLE strictly need to know**

Before connecting After connecting
Advertising packet Prof i le
Services
Characteristics
Properties
Local name Manufacturer data
Properties
Characteristics
Properties
Properties

## Slide 10

Local name

Manufacturer data

Properties

Properties

Properties

Service

Characteristic

Characteristic

Characteristic

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
11:39 4 all 4G GE}: Close Aav... Client Ser.. Log DFU Connect
a © Attribute Table
S | PRIMARY SERVICE
canner Generic Attribute
a ; UUID: 1801
Filtering Active (4 / 187) lj PRIMARY SERVICE
Unknown Service ;
eo N/A Connect UUID: 5£400001-B5A3-F303-E0A9- hekeaMiMceae
Tx Power: 12 dBm E50E24DCCA9E
L In m PRIMARY SERVICE
Ocal name [ie Unknown Characteristic
UUID: 5E400002-B5A3-F393-E0A9-
Manufacturer data
E50E24DCCAQ9E
Characteristic
Properties
UUID: 5E400003-B5A3-F393-E0A9-
E50E24DCCA9E
tere N/A Characteristic
Client Characteristic Configuration
UUID: 2902
Value: Disabled
Value Sent: N/A
Manufacturer Data: Amazon.com Services
LLC <0171> 0011 0100 0101 83A2 25BD E700
al -62 dBm € 74.36 ms
eo N/A Connect
Tx Power: 11 dBm
aa! -73 dBm € 279.59 ms
e~
atl -69 dBm €> 2004.02 ms
N/A Unknown Characteristic
UUID: 5E400004-B5A3-F393-E0A9-
Properties
ail -74 dBm €> 2003.67 ms ES50E24DCCAQE
Value: N/A —
Value Sent: N/A Characteristic
N/A
Properties
a Ww CD) 03:
Scanner RSSI Graph Peripheral Settings
```

## Slide 11

##### **BLE packet collection on Android**

- 1.Activate developer options

- 2.Enable “USB debugging”

3.Enable “Bluetooth HCI Snoop log”

- 4.Collect traffic

- 5.Pull the logs

6.Import into Wireshark

## Slide 12

**Each locker advertises a different/unique ID**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Each locker advertises a different/unique ID
Time Source Destination Protocol Lengtf Value
244 31479083.57.. controller host HCI_EVT 43
Frame 244: Packet, 43 bytes on wire (344 bits), 43 bytes captured (344 bits)
Bluetooth
Bluetooth HCI H4
Bluetooth HCI Event - LE Meta
Event Code: LE Meta (@x3e)
Parameter Total Length: 40
Sub Event: LE Advertising Report (@x@2)
Num Reports: 1
Event Type: Connectable Undirected Advertising (@x@Q)
Peer Address Type: Random Device Address (@x@1)
BD_ADDR: c6:10:f5:5c:6a:15 (c6:10:f5:5c:6a:15)
Data Length: 28
Advertising Data
Flags
Tx Power Level
Peripheral Connection Interval Range: 40 - 8@ msec
Connection Interval Min: 32 (40 msec)
Connection Interval Max: 64 (8@ msec)
Manufacturer Specific
Length: 15
Tyne: Manufacturer Snecific (Oxff)
Company ID: Amazon.com Services LLC (0x@171)
Data: 00110100010183a225bde700
TExpert into (NOte/Undecoded): Undecodéed!
RSSI: -6@ dBm
```

## Slide 13

### **We got data!**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
We got data!
= 2
Time
usrerteu
Ss
«727847
«742502
«799352
+ 810054
+ 842704
+ 945335
«990489
+ 990805
+ 005948
«215272
«261524
+ 305572
+ 305885
- 636825
- 642854
- 643126
+ 643402
. 719828
+ 930603
+ 930903
+211028
+ 259836
+ 260754
+ 261042
+392253
+ 469894
.511367
+511659
+ 588564
43.588971
43.589372
Uy)
U1)
1)
1)
1)
U1)
1)
1
1
1
1
1
6
6
6
6
6
6
6
Source
promvec Vs
localhost
remote ()
localhost
remote ()
localhost
remote ()
remote ()
localhost
localhost
remote ()
remote ()
remote ()
localhost
localhost
localhost
localhost
localhost
remote ()
remote ()
localhost
localhost
remote ()
remote ()
localhost
localhost
remote ()
remote ()
localhost
remote ()
remote ()
localhost
Destination
wuLauiVvoe Vs
remote ()
localhost ()
remote ()
localhost ()
remote ()
localhost ()
localhost ()
remote ()
remote ()
localhost ()
localhost ()
localhost ()
remote ()
remote ()
remote ()
remote ()
remote ()
localhost ()
localhost ()
remote ()
remote ()
localhost ()
localhost ()
remote ()
remote ()
localhost ()
localhost ()
remote ()
localhost ()
localhost ()
remote ()
east Titian rs Itt OE Baas ot SET IOI OR DIT Sot OI sa a ante 2 ‘aaa Sacto Ria eS ai ciate ana
Protocol Lengt)§Value
1
nit
ATT
ATT
ATT
ATT
ATT
ATT
ATT
ATT
HCI_ACL
ATT
ATT
HCI_ACL
HCI_ACL
HCI_ACL
ATT
ATT
ATT
ATT
ATT
ATT
ATT
ATT
ATT
ATT
ATT
ATT
ATT.
ATT
```

## Slide 14

**The Amazon Locker Protocol locker -> phone | phone -> locker**

```
0502
```

```
10220000a461610161620161631a6502ff32616451a46161016162016172f5616544d4178530
```

```
117d0000a461610161620161631a6502ff2f6164586ba361610261620161675860b436d644a4c864808a249a6bb89b6fa08ed59fe7a99cef276c64377eeac91dabaa3d5
95927135050461549c38f05fb2023a136c76fce300f36be8f7247c970de6f5e4183cfc89552ad852822f92f06384cfa6997e627f0de595dee85c5f4aaa9
```

```
10910100a461610161620161631a6502ff38616459017ea861610361620161681864616958a43076301006072a8648ce3d020106052b8104002203620004572bbfa9d2d
0c691efa36e36008f1ac669d88d4118f15d8f5a1d1d7da366c800ef40912c106614a5f65ee32dd8cc5c6f794a936b9602581b7c75048578579eb2d09e0c08c4b2d7661c
902ce2a738fa3d81ed214101c80b4bdb63c3a63e2dcecf33c2f9ede15a31076a056df6b96dafd1d049acb2c0f8f4bf285a94fa718610b877341f31260d6cfc62cc07966
16a582c627491fb3bc2a4693306030caa44e255945d253e3661b6ec92d2455b65dd5864cd51f85be9126d2423028e26616b4465045093616c582432393734343838662d
393637622d346636342d393830392d383461303934633839653565616d586830660231008be708303b2196dbe32a4b0b21ea1a5bcca8b4d7526180575083e8b79bf68d6
44e7a3f027e86530b252febacd3ef3d1b023100ab34b9751fb727b0363233cc528a89d1863983f74bedec582b970c1067cc41598a6942dcbebe6f32fa37d6a755231eb1
```

```
121b0000a461610161620161631a6502ff3561644aa3616104616201616e00
```

```
10690000a461610261620161631a6502ff3f61645857a2616f58204d0091c3f24955a0e7b42c4f4127e9ec99e50d0535e09b3c0ab41f690a8ebdf96170582ea54bb1c56
391fdfcff183aaf04588a6411fded197601a6c88375a7bfabd3ee2e0e6ecc816fc14d79c52c6070d736
```

```
131f0000a461610161620161631a6502ff3b61644ea3616105616201616544288685b4
```

```
103d0000a461610161620161631a6502ff3f6164582ba361610661620161665820ef3dcfcc08db08a90174c091e7a11b9f6ada0da70bbc40302127a1af368dcfa4
10650000a461610261620161631a6502ff3d61645853a3616f5820cd076560a53cf977951373df2cedb30cf4cc6f6e5088b5d0fb94c440f84923e261704061715827baa
ad55fe6e536b88ca30b6fd7d69c836fb88c7debb2cf2c9ba7eda92bc9600609fbc93c879375
```

```
11960000a461610261620161631a6502ff5961645884a3616f58208f1a807d7de65c024579dd9443f99e7d15102136bd419792d478ba886467a4b46170406171585801a
ca7a72404216eeb560cfaa5d8107e12d7554dc1997a144d56aee59d539598b098cc452bd1128061d2081f7aed4b7b01a69f6aabc3935aa72996c18d68c42aec751be158
a394dd476ce40df00361e7f382590d2a8764d4
```

## Slide 15

### **The strategy Collect as many samples as possible in different scenarios**

- Picking up packages on different days

- Picking up packages on different lockers

- Picking up two packages on the same locker

- Picking up packages with different users

- Picking up packages with different phones

• …

## Slide 16

**Cabinet opens when packet #6 is sent! locker -> phone | phone -> locker**

```
0502
```

```
10220000a461610161620161631a6502ff32616451a46161016162016172f5616544d4178530
```

```
117d0000a461610161620161631a6502ff2f6164586ba361610261620161675860b436d644a4c864808a249a6bb89b6fa08ed59fe7a99cef276c64377eeac91dabaa3d5
95927135050461549c38f05fb2023a136c76fce300f36be8f7247c970de6f5e4183cfc89552ad852822f92f06384cfa6997e627f0de595dee85c5f4aaa9
10910100a461610161620161631a6502ff38616459017ea861610361620161681864616958a43076301006072a8648ce3d020106052b8104002203620004572bbfa9d2d
0c691efa36e36008f1ac669d88d4118f15d8f5a1d1d7da366c800ef40912c106614a5f65ee32dd8cc5c6f794a936b9602581b7c75048578579eb2d09e0c08c4b2d7661c
902ce2a738fa3d81ed214101c80b4bdb63c3a63e2dcecf33c2f9ede15a31076a056df6b96dafd1d049acb2c0f8f4bf285a94fa718610b877341f31260d6cfc62cc07966
16a582c627491fb3bc2a4693306030caa44e255945d253e3661b6ec92d2455b65dd5864cd51f85be9126d2423028e26616b4465045093616c582432393734343838662d
393637622d346636342d393830392d383461303934633839653565616d586830660231008be708303b2196dbe32a4b0b21ea1a5bcca8b4d7526180575083e8b79bf68d6
44e7a3f027e86530b252febacd3ef3d1b023100ab34b9751fb727b0363233cc528a89d1863983f74bedec582b970c1067cc41598a6942dcbebe6f32fa37d6a755231eb1
```

```
121b0000a461610161620161631a6502ff3561644aa3616104616201616e00
```

```
10690000a461610261620161631a6502ff3f61645857a2616f58204d0091c3f24955a0e7b42c4f4127e9ec99e50d0535e09b3c0ab41f690a8ebdf96170582ea54bb1c56
391fdfcff183aaf04588a6411fded197601a6c88375a7bfabd3ee2e0e6ecc816fc14d79c52c6070d736
```

```
131f0000a461610161620161631a6502ff3b61644ea3616105616201616544288685b4
```

```
103d0000a461610161620161631a6502ff3f6164582ba361610661620161665820ef3dcfcc08db08a90174c091e7a11b9f6ada0da70bbc40302127a1af368dcfa4
10650000a461610261620161631a6502ff3d61645853a3616f5820cd076560a53cf977951373df2cedb30cf4cc6f6e5088b5d0fb94c440f84923e261704061715827baa
ad55fe6e536b88ca30b6fd7d69c836fb88c7debb2cf2c9ba7eda92bc9600609fbc93c879375
```

```
11960000a461610261620161631a6502ff5961645884a3616f58208f1a807d7de65c024579dd9443f99e7d15102136bd419792d478ba886467a4b46170406171585801a
ca7a72404216eeb560cfaa5d8107e12d7554dc1997a144d56aee59d539598b098cc452bd1128061d2081f7aed4b7b01a69f6aabc3935aa72996c18d68c42aec751be158
a394dd476ce40df00361e7f382590d2a8764d4
```

## Slide 17

**10 packages picked up Comparing by packet - Packet 1 | locker -> phone**

## Slide 18

**10 packages picked up Comparing by packet - Packet 2 | phone -> locker**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
10 packages picked up
Comparing by packet - Packet 2 | phone -> locker
= packet2.txt SAARa/enee pewnancemnmtsg
1 10 22 0000 2461610161620161631a) 6502ff3246164 51 a4 6161 01 6162 01 6172 f5 6165 44/d4178530)
2 10 22 0000 a461610161620161631a! 650460916164 51 a4 6161 01 6162 01 6172 f5 6165 44) 6dec6ef6
3 10 22 0000 a461610161620161631a}650618d9 16164 51 a4 6161 @1 6162 01 6172 f5 6165 44°5b445eff |
4 10 22 0000 a461610161620161631a) 6515c85c 46164 51 a4 6161 01 6162 01 6172 f5 6165 44 e2f352ed"
5 10 22 0000 a461610161620161631a! 6525a1d036164 51 a4 6161 01 6162 01 6172 f5 6165 44 a6ceca2a’>
6 10 22 0000 a461610161620161631a) 6525a6bf #6164 51 a4 6161 01 6162 @1 6172 f5 6165 44) 37cb4755)
7 10 22 0000 a461610161620161631a/.6537e0a6 (6164 51 a4 6161 @1 6162 01 6172 f5 6165 44) ;
8 10 22 0000 a461610161620161631a),65453bc1 +6164 51 a4 6161 @1 6162 01 6172 f5 6165 44). f318bb32_
9 10 22 0000 a461610161620161631a).6545401476164 51 a4 6161 01 6162 01 6172 f5 6165 447 4b6c6502:
RP
S
10 22 0000 a461610161620161631a/ 654540686164 51 a4 6161 01 6162 @1 6172 f5 6165 44! 4ba9a942!
```

## Slide 19

### **10 packages picked up Comparing by packet - Packet 3 | locker -> phone**

T
R
U
N
C
A
T
E
D

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
10 packages picked up
Comparing by packet - Packet 3 | locker -> phone
= packet3.txt scene
1 11 7d 0000 a461610161620161631a)6502ff2f. a3 6161 02 6162 @1 6167
2 11 7d 0000 a461610161620161631a,, a3 6161 @2 6162 01 6167
3 11 7d 0000 a461610161620161631a¥ a3 6161 02 6162 01 6167
4 11 7d 0000 a461610161620161631a> a3 6161 02 6162 01 6167
5 11 7d 0000 a461610161620161631a! a3 6161 02 6162 01 6167
6 11 7d 0000 a461610161620161631a; a3 6161 02 6162 01 6167
7 11 7d 0000 a461610161620161631az a3 6161 02 6162 01 6167
8 11 7d 0000 a461610161620161631a" a3 6161 @2 6162 01 6167
9 11 7d 0000 a461610161620161631a¥ a3 6161 @2 6162 01 6167
fy
S
a3 6161 @2 6162 @1 6167
11 7d 0000 a461610161620161631a}65454067 )
```

## Slide 20

### **10 packages picked up Comparing by packet - Packet 4 (only interesting parts) | phone -> locker**

###### Packet length

T R U N C A T E D

T T R R U U N N C C A A T T E E D D

UUIDs!

## Slide 21

**10 packages picked up Comparing by packet - Packet 5 | locker -> phone**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
10 packages picked up
Comparing by packet - Packet 5 | locker -> phone
= packet5.txt a
1 12 1b 0000 a461610161620161631a '6502ff35 6164 4a a3 6161
2 12 1b 0000 a461610161620161631a | 16164 4a a3 6161
3 12 1b 0000 a461610161620161631a | 16164 4a a3 6161
4 12 1b 0000 a461610161620161631a} 16164 4a a3 6161
5 12 1b 0000 a461610161620161631a } 16164 4a a3 6161
6 12 1b 0000 a461610161620161631a} 46164 4a a3 6161
7 12 1b 0000 a461610161620161631a (6537e0ab! 6164 4a a3 6161
8 12 1b 0000 a461610161620161631a }65453bc3} 6164 4a a3 6161
9 12 1b 0000 a461610161620161631a | 16164 4a a3 6161
10 12 1b 0000 a461610161620161631a 6545406b) 6164 4a a3 6161
04
04
04
04
04
04
04
04
04
04
6162
6162
6162
6162
6162
6162
6162
6162
6162
6162
Q1
Q1
Q1
Q1
01
Q1
Q1
01
Q1
Q1
616e
616e
616e
616e
616e
616e
616e
616e
616e
616e
00
00
00
00
00
00
00
00
00
00
```

## Slide 22

**10 packages picked up Comparing by packet - Packet 6 | phone -> locker**

The “open cabinet” payload

Param iD + 58 + param length

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
10 packages picked up
Comparing by packet - Packet 6 | phone -> locker
= packet6.txt
O©ODNINMMNERWNPR
10
10
10
10
10
10
10
10
10
10
10
a
69} 0000
6940000
69} 0000
6840000
6940000
68/0000
6940000
6940000
6940000
6940000
o9oooooo oD ®»
161)
161)
161
161)
161}
161)
161}
161)
161}
SOS SSS SS
162:
162!
162)
162)
162)
162:
162}
162!
162)
162!
SOS SSS St
163}
163}
163}
163}
163}
163}
163}
163}
163}
163}
o9ooooOoDoO oD wD oD
6502f f3f
6504e629
6506187
6515c883
6525a202
6525a6ee
6537e0b0
65453bcb
65454026
65454078
The “open cabinet” payload
4d0091¢3f24955a0e7b42c4f4127e9ec99e50d0535e09b3c0ab41f690a8ebdf9
€60d613da38eca3e9d7795942e8e6ae78fef6c5b739188359F219a369b3 f091F
c4de8954ee36bbeadb39e9a83ccef0948532eb6d132d22bbc55d9f8F337 f15ec
64971f6ca9ae5caa3a2e6523b20e4b2a17546a6ac2b0F820c5c451030df6FO22
b08278d7b201175a396 f93a3563be7 f fd6991699b3f242790e4bada5a57c38c2
8e5c2ce01cf358184ac03f4c587f6977d5873d3a4c259f fa631e03b9c2041ceb
a977a2ed726936609 fa8c56bdd9 fa f26e596bede5e4aef9eaddf1b4b44e20a4c
83a59cc55015e8eb06beed89ba36 f01c530de2e4b522b5c3ef3352352a791c57
fd5bdcb9610f c51174393e4650687 f8746b54222b29a810039F69768808a375f
1f85d6cd970f96b4ed63128813563120175 fef539 fadce848badb664a33d9a40
617
617
617
617
617
617
617
617
617
617
58
58
58
58
58
58
58
58
58
58
—,
aram iD + 58 + param length
a54bb1c56391fdfcff183aaf04588a6411 fded197601a6c88375a7bfabd3ee2e0e6ecc816fc14d79c52c6070d736
422ad4db4946c7881dcfcd4f2fcfc93e614fbfaa25db2125ab62ddc910a9 F9 F608c771950c10c9e6a4e73cfOb88b
b6741234266d00d9fe4b0acb1185153c1476786c66c64 28269560 fdbfe302568cf71c7170451c6c3a8ad551660F
637667bd4df407c4079f08370f2ccb171d3c703ebbc70729872d185dd fd22ea43f f356a411615d97833F987a50
852b553d47a53124050922b537 fb8cf104cb0170acadeba3df f7 f20fbaf39c9058ab8aa58d954F190a8 falb3c805
6c4d8fd3eb00811e67651199e99340236ad28db8186165297df7ce29d30d66da3554cc3578d30afdeb94b293e3
'454c06b5 f53c8dc29ee20e8e1b0814ce9129509ae2a7 4eF7641c5a467683F112 F807 baa21a7 F79d0d9F198e4526b
4096360666b81d3bbd76fec9c519a8c10b3081a9aad8bc27d01b88698b7ba66051738b94ad3d856e66dc6F6970F9
8480fefc2431d82e3d5801b504834e6d6ebd369679bf2be03424be20b39812a9bc705c236c7beedc12066ebd17e3
70588f2cc700d2c63ec38c7ad8121b9 fe76f17b65b44 F0d455c7780509764ae0201ca796ec462c4ed912443f8229
```

## Slide 23

### **2 package pickups compared 6 first packets**

T R U N C A T E D

Static PacketID Length Separator Epoch time Payload field

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2 package pickups compared
6 first packets
1 Q502
2 10|'22|10@ 01146161 01 61620161631a/16631 0128/6164 51 a4 6161 01 61620161 72f5616544 5f3c0@cc T
3 111:7d:}}@@ @0/1a46161 01 61620161631a/}6631 0125)'6164 58 6b a3 6161 02 61620161 675860 2b179888d5e302202
4 110191101 00l|a46161 Q@1 61620161631a/|6631 012d)'6164 59 017e a8 6161 03 61620161 681864616958a43076301006 R
5 1211bi/@@ @0||a46161 @1 61620161631a//6631 012a|'6164 4a a3 6161 04 61620161 6e00
6 he 691100 00//a46161 @2 61620161631a};6631 01346164 58 57 a2 616f 58 20 71059bd0f2ea56183a U
7 H
S
Re
114;7d
108 Ff
1b
he|ie9
100 QO
ae)
@1 00
00 20
@0@ 00
j
{a46161 01 61620161631a//6631 @21d/,6164 51
a46161 01 61620161631a)/6631 @21a),6164 58 6b
a46161 01 61620161631a}}6631 0221) 6164 59 017c a8 6161 03 61620161 681864616958a43076301006 =
a46161 @1 61620161631a/;6631 @21e}6164 4a
a46161 @2 61620161631a);/6631 @224),6164 58 57
N
a4 6161 01 61620161 72f5616544 accc5c7e T
a3 6161 @2 61620161 675860 49b9dc691ca7841e@
a3 6161 04 61620161 6e00
a2 616f 5820 ®edc@ed6e6cad07b8dd
PacketID| Length |Separator
Epoch time| Payload
```

## Slide 24

Many assumptions, no evidence

## Slide 25

### **Lockerpirate An Amazon Locker & Mobile App emulator PoC**

github.com/martinvigo/lockerpirate

## Slide 26

Can’t figure out how to forge the “open cabinet” payload…

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
= packet6.txt
10 69
10 69
10 69
10 68
10 69
10 68
10 69
10 69
10 69
C©OMNMUABWNPR
Can’t figure out how to forge the
“open cabinet” payload...
6170 58 2e a54bb1c56391 fdfcf f183aaf04588a6411 fded197601a6c88375a7bfabd3ee2e0e6ecc816fc14d79¢52c6070d736 |
16170 58 2e§422ad4db4946c7881dcfcd4f2fcfc93e614fbfaa25db2125ab62ddc910a9F9 F608c771950c10c9e6a4e73cfOb88b
6170 58 2e$b6741234266d00d9fe4b0acb1185153c1476786c66c64F28269560fdbfe302568cf71c7170451c6c3a8ad551660F §
6170 58 2d§637667bd4df407c4079f08370f2ccb171d3c703ebbc70729872d185dd fd22ea43f f356a411615d97833F987a50
16170 58 2e)852b553d47a53124050922b537 fb8cf104cb0170acadeba3df f7 f20fbaf39c9058ab8aa58d954F190a8 falb3c805
6170 58 2d76c4d8fd3eb00811e67651199e99340236ad28db8186165297d F7 ce29d30d66da3554cc3578d30afd0b94b293e3
6170 58 2e)454c06b5f53c8dc29ee20e8e1b0814ce9129509ae2a74ef 7641c5a467683F112f807baa21a7 f79ded9f198e4526b
6170 58 2e§4096360666b81d3bbd76fec9c519a8c10b3081a9aad8bc27d01b88698b7ba66051738b94ad3d856e66dc6F6970F9 §
6170 58 2e)8480fefc2431d82e3d5801b504834e6d6ebd369679bf 2be03424be20b39812a9bc705c236c7beedc12066ebd17e3
6170 58 2e)70588f2cc700d2c63ec38c7ad8121b9 fe76f17b65b44 f0d455c7780509764ae0201ca796ec462c4ed912443f8229 |
4d0091¢3f24955a0e7b42c4f4127e9ec99e50d0535e09b3c0ab41f690a8ebdf9
€60d613da38eca3e9d7795942e8e6ae78fef6c5b739188359F219a369b3 fe91f
c4de8954ee36bbeadb39e9a83ccef0948532eb6d132d22bbc55d9 F8F337 fidec.
164971f6ca9ae5caa3a2e6523b20e4b2a17546a6ac2b0F820c5c451030df6F022
1b08278d7b201175a39693a3563be7 f fd6991699b3f242790e4bada5a57c38C2)
8e5c2ce01cf358184ac03f4c587 f6977d5873d3a4c259f fa631e03b9c2041ceb}
a977a2ed726936609fa8c56bdd9 faf26e596bede5e4aef9eaddf1b4b44e20a4c
83a59cc55015e8eb06beed89ba36f01c530de2e4b522b5c3ef3352352a791c57
fd5bdcb9610f c51174393e4650687 f8746b54222b29a810039f69768808a375F
1f85d6cd970f96b4ed63128813563120175 fef539 fadce848badb664a33d9a40 }
0000 a461610261620161631a 6502ff3f 6164 58 57 a2 616f 58 20
0000 a461610261620161631a 6504e629 6164 58 57 a2 616f 58 20
0000 a461610261620161631a 650618f7 6164 58 57 a2 616f 58 20
0000 a461610261620161631a 6515c883 6164 58 56 a2 616f 58 20
0000 a461610261620161631a 6525a202 6164 58 57 a2 616f 58 20
0000 a461610261620161631a 6525a6ee 6164 58 56 a2 616f 58 20
0000 a461610261620161631a 6537e0b@ 6164 58 57 a2 616f 58 20
0000 a461610261620161631a 65453bcb 6164 58 57 a2 616f 58 20
0000 a461610261620161631a 65454026 6164 58 57 a2 616f 58 20
0000 a461610261620161631a 65454078 6164 58 57 a2 616f 58 20
```

## Slide 27

## Slide 28

Attacking the Amazon Mobile App

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
£ ARTIFACTS
oolean isUserAuthenticated() (
LOCAL STORAG
f (token != nul ;
( : fen '= null && !token. isEmpty()) ( r es. xml
omen preferences. xml
droid. shopping_prefere
} android.s
} ine
d ketplaze=ATVPDKIKXODER
\ ‘
sQuite
- = amazon_dd
® API ENDPOINTS. i user.-sqlite
cart.sqlite
maz m/aut storage/
— om/a h / (awed amazon.com
amazon. com/user localStorage. json Ye
amazon.com/orders/v8/order:
amazon.com
(~ HEXDUMP
| Pp AUTH TOKENS
t
“access_token": "Atza]...9YotnF”,
“token_type”: “bearer”,
“expires_in": 3600, |
“scope”: “profile orders payments” y
}
=> NETWORK TRAFFIC (MITM)
c
etal i guth/o2/token HTTP/1.1
CERTIFICATE PINNING CHECKS spi.amazon.com
Amazm/26.10.0.100 (Linux; Android 13
ooleon checkServerTrust yp: ication k-www-form-urlen:
ha2s6, ; c =
cart] lib/arm64-v8a/ = , oke a|...9YotnF&expires_in=3600
throw new SSLPeerUnverifiedExc - > ad -
} assets/ ‘ont Type: a at
y pplication/jso
return true; vA META-INF/
Attacking the Amazon Mobile App
```

## Slide 29

###### NOTE: Content missing due to responsible disclosure delays with Amazon. To be uploaded in the next couple days

## Slide 30

Attacking the Hardware

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
BLUETOOTH ATTACK SURFACE
*&
EXPLOIT PATH
7
#
SEN AR ! alk,
Attacking the Hardware
```

## Slide 31

###### NOTE: Content missing due to responsible disclosure delays with Amazon. To be uploaded in the next couple days

## Slide 32

Attacking the Locker’s Physical Security

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Attacking tt the Locker’ S Physical Security
```

## Slide 33

###### NOTE: Content missing due to responsible disclosure delays with Amazon. To be uploaded in the next couple days

## Slide 34

Closing remarks

## Slide 35

### **20 bucks in tooling… and you can purchase everything directly from Amazon!**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
20 bucks in tooling...
and you can purchase everything directly from Amazon!
amazon ej
Il Today's Deals Gift Cards Sell Registry Prime Video Customer Service
Tools & Home Improvement Best Sellers savings Lighting & Ceiling Fans Kitchen & Bath Fixtures SmartHome Shop byRoom Launchpad Amazon B
& Home Improvement : ‘ , drive
amazon @spain
5 Piece Magnetic Triangle Screwdriver Bit, S2 Steel
Triangular Screwdriver Bit Set 1/4 Inch Hex Triangle
Drill, 50 mm Length
Brand: Uacer
4s
All Today's Deals Prime Video Registry Gift Cards Customer Service Sell.
Office Products | Amazon Business
ombination Padlocks
FixtureDisplays Combination Cam Lock Master Key Cabinet
Combo Lock Drawer Lock Donation Box Lock Pass Code Pin
Work with 22 GA Sheet Metal, Can Modify to Work with 3/4"
Wood Door 18619-1PK-NPF
Visit the FixtureDisple e
‘50+ bought in past month
EUR 26
No Import Charé
Brand
Item Length 1.97 Inches
Material Alloy Steel
50 vo)
ish Type Steel
Number of Pieces 5 Brand FixtureDisplays
Special Feature Master Key for Dual Access
About this item Lock Type Combination Lock
Item dimensions Lx Wx 3.03 x 1.85 x 1.06 inches
H
Deliver to Priscilla Hq
ANAS © Barctne coors me Materia Wood.zinasticMetal
= All AmazonHaul Sellon Amazon Grocery ~ Customer Service Amazon Basics Keep Shopping For Buy Again OurDeals Prime ~ Best Sellers Kindle Books New Releases} About this item
* FixtureDisplays Combination Cam Lock w/ Master Key Cabinet Lock Drawer Lock Donation Box Lock
18619-1PK. Work with sheet metal face up to 22 GA (0.8mm). Or with purchase of additional
mounting plate and longer screws, you can use this for thicker boards such as 3/4" Wood. See diagram
Click to for more mounting details.
6 in 1 Comb Lock Pick Set, Locksmith, Portable
Stainless Steel Kit, Decompression Tools, Pick Set
Kgj383 (Silver, 9 x 2 cm)
Brand: Generic
* Use in Personal and/or Public modes. This combination cam lock is ideal for tool boxes, cabinets,
drawers, mail box, cash box, DIY safe, school lockers or any other places where keys are not too much
to manage. Help you solve the problem where people keep losing keys.
* Overall product size is 1.06" Width X 3.03" Height X 1.85" Deep. Lock tongue size is 1.25" Length X
0.07" Height. Gross weight is 0.16 bls. Cover and knob are made of black engineering plastic, core of
lock is made of Zinc alloy. Install horizontally and vertically.
* The Defaul code is 0-0-0-0. Dual access lock comes with a master key. Refer to either the pictured
instruction sheet of video for more details how the lock works. Itallation cut-out openning size is:
Search this page
47
Prices include VAT. ©
Save 10%) on any 2 or more Shop qualifying item
Save 15% on any 3 or more qualifying items
re ‘ Save 20% on any 5 or more Shop qualifying items
Z Size Name: 9x2 em
Colour Name: Silver
+ Compact & Portable Design - Lock Pick Set. Slim and lightweight, this tool fits easily in
your pocket or bag, perfect for hobbyists, toy lovers and everyday carry. Set Toys Set
Lackcmith Picks Camnact And Partahle Lack Clack Pick Hank Set Decomnraccian Taal
```

## Slide 36

**Smallest locker has 23 cabinets…**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Smallest locker has 23 cabinets...
amazon Osean” All y Search Amazon
Spain
=All Today'sDeals Prime Video Registry GiftCards CustomerService Sell
Help & Customer Service
« All Help Topics
Find more solutions
Q
Collection Points
Order to an Amazon Pickup
Location
Ship to a Pickup Location . . . . . .
Shipping and Delivery » Shipping Options » Collection Points >»
Collect a Package at an
Amazon Locker
Pick Up a Package at an Pickup Location Eligibility
Amazon Hub Apartment
Locker Items shipped or returned to a Pickup Location need to meet certain guidelines.
Return a Package at an
Amazon Pickup Location
Pickup Locations Amazon ocker
Amazon Locker If the following applies, your order is eligible for Amazon Locker delivery:
Amazon Hub Apartment
¢ The shipping weight is less than 10 lbs.
Locker
e The product dimensions are smaller than 16 x 12 x 14 inches.
e Allitems are sold or fulfilled by Amazon.com.
Accessibility for Amazon The total value is less than $5,000.
Hub Locker The shipment contains no hazardous materials.
Collect Your Package at an The order does not contain Subscribe & Save items.
Amazon Counter The order does not contain items shipping from other countries.
The order does not contain items for Release-Date Delivery
¢ The Locker will not be used as a delivery address for a wishlist
Pickup Location Eligibility
Quick solutions
```

## Slide 37

## Stay paranoid!

**martin@martinvigo.com**

**@martin_vigo martinvigo.com**

**linkedin.com/in/martinvigo github.com/martinvigo youtube.com/martinvigo**
