---
title: "Breaking Amazon lockers by any means necessary"
speakers: ["Martin Vigo"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: 2026
source_pdf: "DEF CON 34/DEF CON 34 - Martin Vigo - Breaking Amazon lockers by any means necessary - into.pdf"
pages: 37
sha256: "bed9215cb97abe549ea2a82394a1976bf2c51c8fced98843c4f632f3db604031"
text_chars: 23326
ocr_pages: 17
has_ocr: true
redacted_secrets: 0
ocr_confidence: 85.4
ocr_unreliable_blocks: 8
vision_verified_pages_changed: 29
vision_verified_pages: 37
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:39:09Z"
---
# Breaking Amazon lockers by any means necessary

**Speakers:** Martin Vigo  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Martin Vigo - Breaking Amazon lockers by any means necessary - into.pdf` (37 pages)


## Slide 1

# **Breaking into Amazon Lockers**

**by any means necessary!**

**Martin Vigo**

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

   - Founder of **Triskel Security**, a offensive cybersecurity consulting company

- **Research**

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

### **Tierra de Hackers**

_Tu noticiero de ciberseguridad hecho podcast_

@tierradehackers | <u>tierradehackers.com</u>

## Slide 4

### **What started it all…**

**GREAT SCOTT GADGETS**

**Ubertooth Retirement**

Home
• Blog Posts by Tag
About
Contact
Free Stuff Program
Jobs
Merch
Open Source Ethos
Support our Work
Upcoming Events
Where to Buy

22 December 2022 17:44 by Straithe and Elizabeth (ubertooth) (permalink)

After 12 years and 17 production runs, Great Scott Gadgets is retiring our first product, Ubertooth One, from our hardware catalog.

GSG's founder Michael Ossmann designed Ubertooth One because he wanted a device that could detect and monitor Bluetooth. At the time, such instruments existed but cost at least five figures—prohibitively expensive for most security researchers. His goal was to design an open-source, affordable-to-make tool that anyone in the security community with basic soldering skills could assemble. At the project's inception, his intent was not to sell hardware but to provide a solution to a problem that no one else had solved. However, demand from the community prompted him to start GSG and launch a Kickstarter campaign that funded the first production.

## Slide 5

### **2 types of lockers**

## Slide 6

### **My target**

- No internet connectivity

- No integrated camera

- Usually installed outdoors

- Completely BLE operated

- The most common in Spain

## Slide 7

# Packet ≠ Package

# Locker ≠ Cabinet

## Slide 8

Attacking the BLE protocol

## Slide 9

### **1-slide BLE strictly need to know**

**Before connecting**

- Advertising packet

   - Local name

   - Manufacturer data

**After connecting**

- Profile

   - Services

      - Characteristics

         - Properties

         - Properties

      - Characteristics

         - Properties

         - Properties

## Slide 10

Local name

Manufacturer data

Service

Properties

Characteristic

Properties

Characteristic

Properties

Characteristic

```text
11:39                                             4G  45

Scanner

Filtering Active (4 / 187)

N/A                                     Connect
Tx Power: 12 dBm

nRF5x                                   Connect
Manufacturer Data: Amazon.com Services LLC <0171> 0011 0100 0101 83A2 25BD E700
Tx Power: 0 dBm
-62 dBm  74.36 ms

N/A                                     Connect
Tx Power: 11 dBm
-73 dBm  279.59 ms

N/A
-69 dBm  2004.02 ms

N/A
-74 dBm  2003.67 ms

Scanner    RSSI Graph    Peripheral    Settings
```

```text
Close    Adv...  Client  Ser...  Log  DFU              Connect

Attribute Table

PRIMARY SERVICE
Generic Attribute
UUID: 1801

PRIMARY SERVICE
Unknown Service
UUID: 5E400001-B5A3-F393-E0A9-E50E24DCCA9E

PRIMARY SERVICE
Unknown Characteristic
UUID: 5E400002-B5A3-F393-E0A9-E50E24DCCA9E
Properties: Write
Value: N/A
Value Sent: N/A

Unknown Characteristic
UUID: 5E400003-B5A3-F393-E0A9-E50E24DCCA9E
Properties: Indicate
Value: N/A
Value Sent: N/A

Client Characteristic Configuration
UUID: 2902
Value: Disabled
Value Sent: N/A

Unknown Characteristic
UUID: 5E400004-B5A3-F393-E0A9-E50E24DCCA9E
Properties: Read
Value: N/A
Value Sent: N/A

N/A
```

## Slide 11

##### **BLE packet collection on Android**

1. Activate developer options

2. Enable “USB debugging”

3. Enable “Bluetooth HCI Snoop log”

4. Collect traffic

5. Pull the logs

6. Import into Wireshark

## Slide 12

**Each locker advertises a different/unique ID**

```text
No.   Time           Source       Destination   Protocol   Length   Value
244   31479083.57…   controller   host          HCI_EVT    43

Frame 244: Packet, 43 bytes on wire (344 bits), 43 bytes captured (344 bits)
Bluetooth
Bluetooth HCI H4
Bluetooth HCI Event - LE Meta
    Event Code: LE Meta (0x3e)
    Parameter Total Length: 40
    Sub Event: LE Advertising Report (0x02)
    Num Reports: 1
    Event Type: Connectable Undirected Advertising (0x00)
    Peer Address Type: Random Device Address (0x01)
    BD_ADDR: c6:10:f5:5c:6a:15 (c6:10:f5:5c:6a:15)
    Data Length: 28
    Advertising Data
        Flags
        Tx Power Level
        Peripheral Connection Interval Range: 40 - 80 msec
            Connection Interval Min: 32 (40 msec)
            Connection Interval Max: 64 (80 msec)
        Manufacturer Specific
            Length: 15
            Type: Manufacturer Specific (0xff)
            Company ID: Amazon.com Services LLC (0x0171)
            Data: 00110100010183a225bde700
            [Expert Info (Note/Undecoded): Undecoded]
    RSSI: -60 dBm
```

## Slide 13

### **We got data!**

```text
Apply a display filter … <⌘/>

No.  Time        Source        Destination     Protocol  Length  Value
 28  0.727420    remote ()     localhost ()    ATT
 29  0.727847    localhost ()  remote ()       ATT       14
 30  0.742502    remote ()     localhost ()    ATT       14
 31  0.799352    localhost ()  remote ()       ATT       12
 32  0.810054    remote ()     localhost ()    ATT       12      0502
 33  0.842704    localhost ()  remote ()       ATT       14
 34  0.945335    remote ()     localhost ()    ATT       10
 35  0.990489    remote ()     localhost ()    L2CAP     21
 36  0.990805    localhost ()  remote ()       L2CAP     15
 37  1.005948    localhost ()  remote ()       ATT       50      10220000a461610161620161631a6502ff32616451a46161016162016172f5616544d4178530
 38  1.215272    remote ()     localhost ()    ATT       10
 39  1.261524    remote ()     localhost ()    HCI_ACL   107
 40  1.305572    remote ()     localhost ()    ATT       39      117d0000a461610161620161631a6502ff2f6164586ba361610261620161675860b436d644a4c864808a249a6bb89b6fa08ed59fe7a99cef276c64377eeac91dabaa
 41  1.305885    localhost ()  remote ()       ATT       10
 42  6.636825    localhost ()  remote ()       HCI_ACL   128
 43  6.642854    localhost ()  remote ()       HCI_ACL   128
 44  6.643126    localhost ()  remote ()       HCI_ACL   128
 45  6.643402    localhost ()  remote ()       ATT       48      10910100a461610161620161631a6502ff38616459017ea861610361620161681864616958a43076301006072a8648ce3d020106052b8104002203620004572bbfa9
 46  6.719828    remote ()     localhost ()    ATT       10
 47  6.930603    remote ()     localhost ()    ATT       43      121b0000a461610161620161631a6502ff3561644aa3616104616201616e00
 48  6.930903    localhost ()  remote ()       ATT       10
 49  13.211028   localhost ()  remote ()       ATT       121     10690000a461610261620161631a6502ff3f61645857a2616f58204d0091c3f24955a0e7b42c4f4127e9ec99e50d0535e09b3c0ab41f690a8ebdf96170582ea54bb1
 50  13.259836   remote ()     localhost ()    ATT       10
 51  13.260754   remote ()     localhost ()    ATT       47      131f0000a461610161620161631a6502ff3b61644ea3616105616201616544288685b4
 52  13.261042   localhost ()  remote ()       ATT       10
 53  13.392253   localhost ()  remote ()       ATT       77      103d0000a461610161620161631a6502ff3f6164582ba361610661620161665820ef3dcfcc08db08a90174c091e7a11b9f6ada0da70bbc40302127a1af368dcfa4
 54  13.469894   remote ()     localhost ()    ATT       10
 55  15.511367   remote ()     localhost ()    ATT       117     10650000a461610261620161631a6502ff3d61645853a3616f5820cd076560a53cf977951373df2cedb30cf4cc6f6e5088b5d0fb94c440f84923e26170406171582
 56  15.511659   localhost ()  remote ()       ATT       10
 57  43.588564   remote ()     localhost ()    HCI_ACL   128
 58  43.588971   remote ()     localhost ()    ATT       43      11960000a461610261620161631a6502ff5961645884a3616f58208f1a807d7de65c024579dd9443f99e7d15102136bd419792d478ba886467a4b4617040617158
 59  43.589372   localhost ()  remote ()       ATT       10
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
```

```
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

- …

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
```

```
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

```text
packet1.txt
  1    0502
  2    0502
  3    0502
  4    0502
  5    0502
  6    0502
  7    0502
  8    0502
  9    0502
 10    0502
```

## Slide 18

**10 packages picked up Comparing by packet - Packet 2 | phone -> locker**

```text
packet2.txt
  1    10 22 0000 a461610161620161631a 6502ff32 6164 51    a4 6161 01 6162 01 6172 f5 6165 44 d4178530
  2    10 22 0000 a461610161620161631a 6504e609 6164 51    a4 6161 01 6162 01 6172 f5 6165 44 6dec6ef6
  3    10 22 0000 a461610161620161631a 650618d9 6164 51    a4 6161 01 6162 01 6172 f5 6165 44 5b445eff
  4    10 22 0000 a461610161620161631a 6515c85c 6164 51    a4 6161 01 6162 01 6172 f5 6165 44 e2f352ed
  5    10 22 0000 a461610161620161631a 6525a1d0 6164 51    a4 6161 01 6162 01 6172 f5 6165 44 a6ceca2a
  6    10 22 0000 a461610161620161631a 6525a6bf 6164 51    a4 6161 01 6162 01 6172 f5 6165 44 37cb4755
  7    10 22 0000 a461610161620161631a 6537e0a6 6164 51    a4 6161 01 6162 01 6172 f5 6165 44 6586eae3
  8    10 22 0000 a461610161620161631a 65453bc1 6164 51    a4 6161 01 6162 01 6172 f5 6165 44 f318bb32
  9    10 22 0000 a461610161620161631a 65454014 6164 51    a4 6161 01 6162 01 6172 f5 6165 44 4b6c6502
 10    10 22 0000 a461610161620161631a 65454068 6164 51    a4 6161 01 6162 01 6172 f5 6165 44 4ba9a942
```

## Slide 19

### **10 packages picked up Comparing by packet - Packet 3 | locker -> phone**

TRUNCATED

```text
packet3.txt
  1    11 7d 0000 a461610161620161631a 6502ff2f 6164 58 6b    a3 6161 02 6162 01 6167    58 60 b436d644a4c864808a
  2    11 7d 0000 a461610161620161631a 6504e603 6164 58 6b    a3 6161 02 6162 01 6167    58 60 97d581e369f02fbff2
  3    11 7d 0000 a461610161620161631a 650618d5 6164 58 6b    a3 6161 02 6162 01 6167    58 60 4875a0dcf9726b5ce0
  4    11 7d 0000 a461610161620161631a 6515c85a 6164 58 6b    a3 6161 02 6162 01 6167    58 60 e2741bcfa7106f6f7b
  5    11 7d 0000 a461610161620161631a 6525a1cb 6164 58 6b    a3 6161 02 6162 01 6167    58 60 e749119e3c62ee1b52
  6    11 7d 0000 a461610161620161631a 6525a6bb 6164 58 6b    a3 6161 02 6162 01 6167    58 60 66038f33cb140449da
  7    11 7d 0000 a461610161620161631a 6537e0a7 6164 58 6b    a3 6161 02 6162 01 6167    58 60 0b660b9e49c2180e87
  8    11 7d 0000 a461610161620161631a 65453bbe 6164 58 6b    a3 6161 02 6162 01 6167    58 60 8541e34f7b5f42bd82
  9    11 7d 0000 a461610161620161631a 65454013 6164 58 6b    a3 6161 02 6162 01 6167    58 60 e199f3e1e11b1ebe63
 10    11 7d 0000 a461610161620161631a 65454067 6164 58 6b    a3 6161 02 6162 01 6167    58 60 bde290645e5f175ed9
```

## Slide 20

### **10 packages picked up Comparing by packet - Packet 4 (only interesting parts) | phone -> locker**

packet4.txt

```text
 1  10 91 0100 a461610161620161631a 6502ff38 6164 59 017e a8 6161 03 6162 01 6168 1864 6169 58 a4 3076301 00 6072a8648ce3d020106052b8104 00 220362 0004
 2  10 8f 0100 a461610161620161631a 6504e60d 6164 59 017c a8 6161 03 6162 01 6168 1864 6169 58 a4 3076301 00 6072a8648ce3d020106052b8104 00 220362 0004
 3  10 90 0100 a461610161620161631a 650618dd 6164 59 017d a8 6161 03 6162 01 6168 1864 6169 58 a4 3076301 00 6072a8648ce3d020106052b8104 00 220362 0004
 4  10 8f 0100 a461610161620161631a 6515c861 6164 59 017c a8 6161 03 6162 01 6168 1864 6169 58 a4 3076301 00 6072a8648ce3d020106052b8104 00 220362 0004
 5  10 8f 0100 a461610161620161631a 6525a1d4 6164 59 017c a8 6161 03 6162 01 6168 1864 6169 58 a4 3076301 00 6072a8648ce3d020106052b8104 00 220362 0004
 6  10 90 0100 a461610161620161631a 6525a6c2 6164 59 017d a8 6161 03 6162 01 6168 1864 6169 58 a4 3076301 00 6072a8648ce3d020106052b8104 00 220362 0004
 7  10 91 0100 a461610161620161631a 6537e0aa 6164 59 017e a8 6161 03 6162 01 6168 1864 6169 58 a4 3076301 00 6072a8648ce3d020106052b8104 00 220362 0004
 8  10 91 0100 a461610161620161631a 65453bc5 6164 59 017e a8 6161 03 6162 01 6168 1864 6169 58 a4 3076301 00 6072a8648ce3d020106052b8104 00 220362 0004
 9  10 91 0100 a461610161620161631a 65454018 6164 59 017e a8 6161 03 6162 01 6168 1864 6169 58 a4 3076301 00 6072a8648ce3d020106052b8104 00 220362 0004
10  10 91 0100 a461610161620161631a 6545406d 6164 59 017e a8 6161 03 6162 01 6168 1864 6169 58 a4 3076301 00 6072a8648ce3d020106052b8104 00 220362 0004
```

T R U N C A T E D

```text
231eb1
4c
94c6
52
44
452f
a6cee6
dfc747
656d16
656d16
```

###### Packet length

T R U N C A T E D

```text
3239373434383866 2d 39363762 2d 34663634 2d 39383039 2d 383461303934633839653565
3565373139333964 2d 32636439 2d 34373639 2d 39663830 2d 613965376362393265363462
3436323530313561 2d 66646466 2d 34353163 2d 62636632 2d 373630643463646166366439
3165623634343364 2d 61353534 2d 34353837 2d 61373564 2d 646661393762373633313438
3239316332616235 2d 39613465 2d 34646537 2d 62393363 2d 643533666531383136616130
6462336133333763 2d 34356236 2d 34376231 2d 62363635 2d 303635336539646433393365
3338663662313332 2d 38316265 2d 34396138 2d 61393266 2d 373562363564633835343033
3839343364646435 2d 32313739 2d 34366330 2d 39363266 2d 396135353666356230643461
6464396366393232 2d 66346564 2d 34356539 2d 38353665 2d 623633626332633938613733
6464396366393232 2d 66346564 2d 34356539 2d 38353665 2d 623633626332633938613733
```

T R U N C A T E D

UUIDs!

## Slide 21

**10 packages picked up Comparing by packet - Packet 5 | locker -> phone**

packet5.txt

```text
 1  12 1b 0000 a461610161620161631a 6502ff35 6164 4a  a3 6161 04 6162 01 616e 00
 2  12 1b 0000 a461610161620161631a 6504e607 6164 4a  a3 6161 04 6162 01 616e 00
 3  12 1b 0000 a461610161620161631a 650618d9 6164 4a  a3 6161 04 6162 01 616e 00
 4  12 1b 0000 a461610161620161631a 6515c85f 6164 4a  a3 6161 04 6162 01 616e 00
 5  12 1b 0000 a461610161620161631a 6525a1cf 6164 4a  a3 6161 04 6162 01 616e 00
 6  12 1b 0000 a461610161620161631a 6525a6bf 6164 4a  a3 6161 04 6162 01 616e 00
 7  12 1b 0000 a461610161620161631a 6537e0ab 6164 4a  a3 6161 04 6162 01 616e 00
 8  12 1b 0000 a461610161620161631a 65453bc3 6164 4a  a3 6161 04 6162 01 616e 00
 9  12 1b 0000 a461610161620161631a 65454017 6164 4a  a3 6161 04 6162 01 616e 00
10  12 1b 0000 a461610161620161631a 6545406b 6164 4a  a3 6161 04 6162 01 616e 00
```

## Slide 22

**10 packages picked up Comparing by packet - Packet 6 | phone -> locker**

The “open cabinet” payload

packet6.txt

```text
 1  10 69 0000 a461610261620161631a 6502ff3f 6164 58 57 a2 616f 58 20 4d0091c3f24955a0e7b42c4f4127e9ec99e50d0535e09b3c0ab41f690a8ebdf9 6170 58 2e a54bb1c56391fdfcff183aaf04588a6411fded197601a6c88375a7bfabd3ee2e0e6ecc816fc14d79c52c6070d736
 2  10 69 0000 a461610261620161631a 6504e629 6164 58 57 a2 616f 58 20 e60d613da38eca3e9d7795942e8e6ae78fef6c5b739188359f219a369b3f091f 6170 58 2e 422ad4db4946c7881dcfcd4f2fcfc93e614fbfaa25db2125ab62ddc910a9f9f608c771950c10c9e6a4e73cf0b88b
 3  10 69 0000 a461610261620161631a 650618f7 6164 58 57 a2 616f 58 20 c4de8954ee36bbea0b39e9a83ccef0948532eb6d132d22bbc55d9f8f337f15ec 6170 58 2e b6741234266d00d9fe4b0acb1185153c1476786c66c64f28269560fdbfe302568cf71c7170451c6c3a8ad551660f
 4  10 68 0000 a461610261620161631a 6515c883 6164 58 56 a2 616f 58 20 64971f6ca9ae5caa3a2e6523b20e4b2a17546a6ac2b0f820c5c451030df6f022 6170 58 2d 637667bd4df407c4079f08370f2ccb171d3c703ebbc70729872d185ddfd22ea43ff356a411615d97833f987a50
 5  10 69 0000 a461610261620161631a 6525a202 6164 58 57 a2 616f 58 20 b08278d7b201175a396f93a3563be7ffd6991699b3f242790e4bada5a57c38c2 6170 58 2e 852b553d47a53124050922b537fb8cf104cb0170acadeba3dff7f20fbaf39c9058ab8aa58d954f190a8fa1b3c805
 6  10 68 0000 a461610261620161631a 6525a6ee 6164 58 56 a2 616f 58 20 8e5c2ce01cf358184ac03f4c587f6977d5873d3a4c259ffa631e03b9c2041ceb 6170 58 2d 6c4d8fd3eb00811e67651199e99340236ad28db8186165297df7ce29d30d66da3554cc3578d30afd0b94b293e3
 7  10 69 0000 a461610261620161631a 6537e0b0 6164 58 57 a2 616f 58 20 a977a2ed726936609fa8c56bdd9faf26e596bede5e4aef9eaddf1b4b44e20a4c 6170 58 2e 454c06b5f53c8dc29ee20e8e1b0814ce9129509ae2a74ef7641c5a467683f112f807baa21a7f79d0d9f198e4526b
 8  10 69 0000 a461610261620161631a 65453bcb 6164 58 57 a2 616f 58 20 83a59cc55015e8eb06beed89ba36f01c530de2e4b522b5c3ef3352352a791c57 6170 58 2e 4096360666b81d3bbd76fec9c519a8c10b3081a9aad8bc27d01b88698b7ba66051738b94ad3d856e66dc6f6970f9
 9  10 69 0000 a461610261620161631a 65454026 6164 58 57 a2 616f 58 20 fd5bdcb9610fc51174393e4650687f8746b54222b29a810039f69768808a375f 6170 58 2e 8480fefc2431d82e3d5801b504834e6d6ebd369679bf2be03424be20b39812a9bc705c236c7beedc12066ebd17e3
10  10 69 0000 a461610261620161631a 65454078 6164 58 57 a2 616f 58 20 1f85d6cd970f96b4ed63128813563120175fef539fadce848badb664a33d9a40 6170 58 2e 70588f2cc700d2c63ec38c7ad8121b9fe76f17b65b44f0d455c7780509764ae0201ca796ec462c4ed912443f8229
```

Param iD + 58 + param length

## Slide 23

### **2 package pickups compared 6 first packets**

```text
 1  0502
 2  10 22 00 00 a46161 01 61620161631a 6631 0128 6164 51        a4 6161 01 61620161 72f5616544 5f3c00cc
 3  11 7d 00 00 a46161 01 61620161631a 6631 0125 6164 58 6b     a3 6161 02 61620161 675860 2b179888d5e302202
 4  10 91 01 00 a46161 01 61620161631a 6631 012d 6164 59 017e   a8 6161 03 61620161 681864616958a43076301006
 5  12 1b 00 00 a46161 01 61620161631a 6631 012a 6164 4a        a3 6161 04 61620161 6e00
 6  10 69 00 00 a46161 02 61620161631a 6631 0134 6164 58 57     a2 616f                     58 20 71059bd0f2ea56183a
 7
 8
 9
10
11  0502
12  10 22 00 00 a46161 01 61620161631a 6631 021d 6164 51        a4 6161 01 61620161 72f5616544 accc5c7e
13  11 7d 00 00 a46161 01 61620161631a 6631 021a 6164 58 6b     a3 6161 02 61620161 675860 49b9dc691ca7841e0
14  10 8f 01 00 a46161 01 61620161631a 6631 0221 6164 59 017c   a8 6161 03 61620161 681864616958a43076301006
15  12 1b 00 00 a46161 01 61620161631a 6631 021e 6164 4a        a3 6161 04 61620161 6e00
16  10 69 00 00 a46161 02 61620161631a 6631 0224 6164 58 57     a2 616f                     5820 0edc0ed6e6cad07b8dd
```

T R U N C A T E D

| PacketID | Length | Separator | Static field | Epoch time | Payload |
| --- | --- | --- | --- | --- | --- |

## Slide 24

Many assumptions, no evidence

## Slide 25

### **Lockerpirate An Amazon Locker & Mobile App emulator PoC**

github.com/martinvigo/lockerpirate

## Slide 26

Can’t figure out how to forge the “open cabinet” payload…

packet6.txt

```text
 1  10 69 0000 a461610261620161631a 6502ff3f 6164 58 57 a2 616f 58 20 4d0091c3f24955a0e7b42c4f4127e9ec99e50d0535e09b3c0ab41f690a8ebdf9 6170 58 2e a54bb1c56391fdfcff183aaf04588a6411fded197601a6c88375a7bfabd3ee2e0e6ecc816fc14d79c52c6070d736
 2  10 69 0000 a461610261620161631a 6504e629 6164 58 57 a2 616f 58 20 e60d613da38eca3e9d7795942e8e6ae78fef6c5b739188359f219a369b3f091f 6170 58 2e 422ad4db4946c7881dcfcd4f2fcfc93e614fbfaa25db2125ab62ddc910a9f9f608c771950c10c9e6a4e73cf0b88b
 3  10 69 0000 a461610261620161631a 650618f7 6164 58 57 a2 616f 58 20 c4de8954ee36bbea0b39e9a83ccef0948532eb6d132d22bbc55d9f8f337f15ec 6170 58 2e b6741234266d00d9fe4b0acb1185153c1476786c66c64f28269560fdbfe302568cf71c7170451c6c3a8ad551660f
 4  10 68 0000 a461610261620161631a 6515c883 6164 58 56 a2 616f 58 20 64971f6ca9ae5caa3a2e6523b20e4b2a17546a6ac2b0f820c5c451030df6f022 6170 58 2d 637667bd4df407c4079f08370f2ccb171d3c703ebbc70729872d185ddfd22ea43ff356a411615d97833f987a50
 5  10 69 0000 a461610261620161631a 6525a202 6164 58 57 a2 616f 58 20 b08278d7b201175a396f93a3563be7ffd6991699b3f242790e4bada5a57c38c2 6170 58 2e 852b553d47a53124050922b537fb8cf104cb0170acadeba3dff7f20fbaf39c9058ab8aa58d954f190a8fa1b3c805
 6  10 68 0000 a461610261620161631a 6525a6ee 6164 58 56 a2 616f 58 20 8e5c2ce01cf358184ac03f4c587f6977d5873d3a4c259ffa631e03b9c2041ceb 6170 58 2d 6c4d8fd3eb00811e67651199e99340236ad28db8186165297df7ce29d30d66da3554cc3578d30afd0b94b293e3
 7  10 69 0000 a461610261620161631a 6537e0b0 6164 58 57 a2 616f 58 20 a977a2ed726936609fa8c56bdd9faf26e596bede5e4aef9eaddf1b4b44e20a4c 6170 58 2e 454c06b5f53c8dc29ee20e8e1b0814ce9129509ae2a74ef7641c5a467683f112f807baa21a7f79d0d9f198e4526b
 8  10 69 0000 a461610261620161631a 65453bcb 6164 58 57 a2 616f 58 20 83a59cc55015e8eb06beed89ba36f01c530de2e4b522b5c3ef3352352a791c57 6170 58 2e 4096360666b81d3bbd76fec9c519a8c10b3081a9aad8bc27d01b88698b7ba66051738b94ad3d856e66dc6f6970f9
 9  10 69 0000 a461610261620161631a 65454026 6164 58 57 a2 616f 58 20 fd5bdcb9610fc51174393e4650687f8746b54222b29a810039f69768808a375f 6170 58 2e 8480fefc2431d82e3d5801b504834e6d6ebd369679bf2be03424be20b39812a9bc705c236c7beedc12066ebd17e3
10  10 69 0000 a461610261620161631a 65454078 6164 58 57 a2 616f 58 20 1f85d6cd970f96b4ed63128813563120175fef539fadce848badb664a33d9a40 6170 58 2e 70588f2cc700d2c63ec38c7ad8121b9fe76f17b65b44f0d455c7780509764ae0201ca796ec462c4ed912443f8229
```

## Slide 27

## Slide 28

Attacking the Amazon Mobile App

## Slide 29

###### NOTE: Content missing due to responsible disclosure delays with Amazon. To be uploaded in the next couple days

## Slide 30

Attacking the Hardware

## Slide 31

###### NOTE: Content missing due to responsible disclosure delays with Amazon. To be uploaded in the next couple days

## Slide 32

Attacking the Locker’s Physical Security

## Slide 33

###### NOTE: Content missing due to responsible disclosure delays with Amazon. To be uploaded in the next couple days

## Slide 34

Closing remarks

## Slide 35

### **20 bucks in tooling… and you can purchase everything directly from Amazon!**

amazon | Deliver to Spain | All | triangle head screwdriver

All | Today's Deals | Gift Cards | Sell | Registry | Prime Video | Customer Service

Tools & Home Improvement | Best Sellers | Deals & Savings | Gift Ideas | Power & Hand Tools | Lighting & Ceiling Fans | Kitchen & Bath Fixtures | Smart Home | Shop by Room | Launchpad | Amazon Business

Tools & Home Improvement › Power & Hand Tools › Power Tool Parts & Accessories › Screwdriver Accessories › Screwdriver Bit Sets

**5 Piece Magnetic Triangle Screwdriver Bit, S2 Steel Triangular Screwdriver Bit Set 1/4 Inch Hex Triangle Drill, 50 mm Length**

Brand: Uacen

4.5 ★★★★☆ (218)

Amazon's Choice

**50+ bought** in past month

EUR 4.26

No Import Charges & EUR 6.97 Shipping to Spain Details

| Brand | Uacen |
| --- | --- |
| Item Length | 1.97 Inches |
| Material | Alloy Steel |
| Finish Type | Steel |
| Number of Pieces | 5 |

**About this item**

amazon.es prime | Deliver to Priscilla Barcelona 08013 | All | ganzuas | EN

All | Amazon Haul | Sell on Amazon | Grocery | Customer Service | Amazon Basics | Keep Shopping For | Buy Again | Our Deals | Prime | Best Sellers | Kindle Books | New Releases

DIY & Tools › Power, Garden & Hand Tools › Hand Tools › Tool Sets

**6 in 1 Comb Lock Pick Set, Locksmith, Portable Stainless Steel Kit, Decompression Tools, Pick Set Kgj383 (Silver, 9 x 2 cm)**

Brand: Generic

Search this page

€2.47

Prices include VAT.

Save 10% on any 2 or more Shop qualifying items ›

Save 15% on any 3 or more Shop qualifying items ›

Save 20% on any 5 or more Shop qualifying items ›

Size Name: **9x2 cm**

Colour Name: **Silver**

- Compact & Portable Design - Lock Pick Set. Slim and lightweight, this tool fits easily in your pocket or bag, perfect for hobbyists, toy lovers and everyday carry. Set Toys Set Locksmith, Picks, Compact And Portable Lock Clock Pick Hook Set, Decompression Tool

amazon | Deliver to Spain | All | Search Amazon

All | Today's Deals | Prime Video | Registry | Gift Cards | Customer Service | Sell

Office Products | Amazon Business

Tools & Home Improvement › Hardware › Padlocks & Hasps › Combination Padlocks

**FixtureDisplays Combination Cam Lock Master Key Cabinet Combo Lock Drawer Lock Donation Box Lock Pass Code Pin Work with 22 GA Sheet Metal, Can Modify to Work with 3/4" Wood Door 18619-1PK-NPF**

Visit the FixtureDisplays Store

5.0 ★★★★★ (1)

| Brand | FixtureDisplays |
| --- | --- |
| Special Feature | Master Key for Dual Access |
| Lock Type | Combination Lock |
| Item dimensions L x W x H | 3.03 x 1.85 x 1.06 inches |
| Material | Wood,Zinc,Plastic,Metal |

Click to see full view

**About this item**

- FixtureDisplays Combination Cam Lock w/ Master Key Cabinet Lock Drawer Lock Donation Box Lock 18619-1PK. Work with sheet metal face up to 22 GA (0.8mm). Or with purchase of additional mounting plate and longer screws, you can use this for thicker boards such as 3/4" Wood. See diagram for more mounting details.

- Use in Personal and/or Public modes. This combination cam lock is ideal for tool boxes, cabinets, drawers, mail box, cash box, DIY safe, school lockers or any other places where keys are not too much to manage. Help you solve the problem where people keep losing keys.

- Overall product size is 1.06" Width X 3.03" Height X 1.85" Deep. Lock tongue size is 1.25" Length X 0.07" Height. Gross weight is 0.16 bls. Cover and knob are made of black engineering plastic, core of lock is made of Zinc alloy. Install horizontally and vertically.

- The Defaul code is 0-0-0-0. Dual access lock comes with a master key. Refer to either the pictured instruction sheet of video for more details how the lock works. Itallation cut-out openning size is:

## Slide 36

**Smallest locker has 23 cabinets…**

amazon | Deliver to Spain | All | Search Amazon

All | Today's Deals | Prime Video | Registry | Gift Cards | Customer Service | Sell

## Help & Customer Service

‹ All Help Topics

### Collection Points

Order to an Amazon Pickup Location

Ship to a Pickup Location

Collect a Package at an Amazon Locker

Pick Up a Package at an Amazon Hub Apartment Locker

Return a Package at an Amazon Pickup Location

Pickup Locations

Amazon Locker

Amazon Hub Apartment Locker

**Pickup Location Eligibility**

Accessibility for Amazon Hub Locker

Collect Your Package at an Amazon Counter

### Quick solutions

**Find more solutions**

Shipping and Delivery › Shipping Options › Collection Points ›

## Pickup Location Eligibility

Items shipped or returned to a Pickup Location need to meet certain guidelines.

### Amazon Locker

If the following applies, your order is eligible for Amazon Locker delivery:

- The shipping weight is less than 10 lbs.
- The product dimensions are smaller than 16 x 12 x 14 inches.
- All items are sold or fulfilled by Amazon.com.
- The total value is less than $5,000.
- The shipment contains no hazardous materials.
- The order does not contain Subscribe & Save items.
- The order does not contain items shipping from other countries.
- The order does not contain items for Release-Date Delivery
- The Locker will not be used as a delivery address for a wishlist

## Slide 37

## Stay paranoid!

**martin@martinvigo.com**

**@martin_vigo**

**martinvigo.com**

**linkedin.com/in/martinvigo**

**github.com/martinvigo**

**youtube.com/martinvigo**

TRISKEL SECURITY

BOOST YOUR CYBER RESILIENCE

TIERRA DE HACKERS

