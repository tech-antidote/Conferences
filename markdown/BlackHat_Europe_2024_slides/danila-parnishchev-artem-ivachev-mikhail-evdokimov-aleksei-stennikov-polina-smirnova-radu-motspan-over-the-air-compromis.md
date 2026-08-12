---
title: "Over the Air Compromise of Modern Volkswagen Group Vehicles"
speakers: ["Danila Parnishchev", "Artem Ivachev", "Mikhail Evdokimov", "Aleksei Stennikov", "Polina Smirnova", "Radu Motspan"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2024"
edition: "Europe"
year: 2024
source_pdf: "BlackHat_Europe_2024_slides/Danila Parnishchev & Artem Ivachev & Mikhail Evdokimov & Aleksei Stennikov & Polina Smirnova & Radu Motspan_Over the Air Compromise of Modern Volkswagen Group Vehicles.pdf"
pages: 77
sha256: "a77ade94a3de45e79505afdad7d62ba139ca9e7036e930adac002b8881fb5db7"
text_chars: 28437
ocr_pages: 6
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:53:12Z"
---
# Over the Air Compromise of Modern Volkswagen Group Vehicles

**Speakers:** Danila Parnishchev, Artem Ivachev, Mikhail Evdokimov, Aleksei Stennikov, Polina Smirnova, Radu Motspan  
**Conference:** Black Hat Europe 2024  
**Source:** `BlackHat_Europe_2024_slides/Danila Parnishchev & Artem Ivachev & Mikhail Evdokimov & Aleksei Stennikov & Polina Smirnova & Radu Motspan_Over the Air Compromise of Modern Volkswagen Group Vehicles.pdf` (77 pages)


## Slide 1

## Over the Air Compromise of Modern Volkswagen Group Vehicles

Speaker(s):

Artem Ivachev Danila Parnishchev

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
~BaRO o .
\ DECEMBER 11-12, 2024 Cf
IEFINGS x =
*
:
x: |
Compromise of Modem Volkswagen Group Vehicles
Speaker(s):
Artem lvachev
Danila Parnishchev
#BHEU @BlackHatEvents
```

## Slide 2

### Intro – PCA and speakers

• PCA Budapest, Hungary

- Security team: vulnerability research for automotive, fintech, other industries …

- Threat intelligence research team

- Product security monitoring

Danila Parnishchev Artem Ivachev Head of security research Senior security researcher

and Mikhail Evdokimov, Aleksei Stennikov, Polina Smirnova, Radu Motspan, Abdellah Benotsmane

Information Classification: General

#BHEU @BlackHatEvents

2

## Slide 3

### Skoda Superb and Volkswagen MIB3 Infotainment

- Skoda Superb 3 (B8) was produced from 2015 to 2023. Now it’s 4<sup>th</sup> gen (B9)

- • MIB3 infotainment appeared in 2021, now being used in many VW Group cars

- MIB3 features:

   - Wi-Fi in client and hotspot modes

   - Bluetooth (hands-free calls)

   - USB

   - Apple CarPlay, Android Auto, CarLife, MirrorLink

   - In-car microphone for Bluetooth calls and voice control

   - Maps with GPS navigation

#### Skoda Superb 3

MIB3 infotainment unit (HMI screen)

Information Classification: General

#BHEU @BlackHatEvents

3

## Slide 4

### Results of our research

- 21 vulnerability was found and reported to VW in 2022

• 9 of them published in 2023 • <u>https://pcautomotive.com/vulnerabilities-in-skoda-and-volkswagen-vehicles</u>

|**N**|**Vulnerability**|**CVSS**|**N**
**Vulnerability**|**CVSS**|
|---|---|---|---|---|
|1
2|2 debuginterfaces(IVI)|-|6
IVI DoS via CarPlay|5.3|
|3|Hardcoded debug interface
credentials(IVI)|3.5|7
Engine DoS via UDS service
(under conditions)|4.7|
|4
5|<sup>Weak UDS service</sup>
authentication(IVI)|3.3 4.0|8 9 <sup>Broken access control on</sup>
backend|5.3|
|IVI|– In-Vehicle Infotainment||||

#### UDS – Unified Diagnostic Services

Information Classification: General

#BHEU @BlackHatEvents

4

## Slide 5

### Results of our research II

- … and the rest 12 vulnerabilities in MIB3 led to the following impact:

Code execution on IVI via Bluetooth

**#** Privilege escalation to root

Persistent code execution

Access to CAN bus

Remote IVI control via Internet

Information Classification: General

#BHEU @BlackHatEvents

5

## Slide 6

### Results of our research III

Persistent root code execution with internet access gave us remote control over the car:

Remote controls
#

Track vehicle speed and location in real time

Eavesdrop in-car microphone Control vehicle sound

Control infotainment screen Exfiltrate phone contact database

Information Classification: General

#BHEU @BlackHatEvents

6

## Slide 7

### A note about different MIB3 infotainments

- VW Group brands do not build MIB3 infotainment themselves – they order from Tier-1 suppliers

- There are multiple MIB3 models:

   - MIB3 manufactured by Preh Car Connect Gmbh

   - MIB3 manufactured by LG

   - MIB3 manufactured by Aptiv

   - Others may exist

- Our talk is only about MIB3 by Preh Car Connect Gmbh

Information Classification: General

#BHEU @BlackHatEvents

7

## Slide 8

### List of affected MIB3 unit OEM part numbers

`3G5035816[A|B|C|D|E|F|G|H|G|K|L|M|N] 3V0035816[A|B|C|D|E|F|G|H|G|K|L|M|N]` `3G5035820[A|B|C|D|E|F|G|H|G|K|L|M|N] 3V0035820[A|B|C|D|E|F|G|H|G|K|L|M|N]` `3G5035832[A|C|D|E|F|G] 3V0035824[A|B|C|D|E]` `3G5035846 3V0035832[A|B|C|D|E|F|G|H|G|K|L|M|N]` `3G5035864[B|C|D|E|F] 3V0035874[A|B|C|D|E]` `3G5035876 3V0035876[A|B|C|D|E|F|G|H|G|K|L|M|N]` `3G5035880 3V9035832[A|B|C|D]` `3G5035882[B|C|D||F] 3V9035876[A|B|C|D]` `3G9035824[A|B|C|D] 3G9035832[A|B|C|D]` The list was found on the infotainment inside `3G9035874[A|B|C|D] /etc/swup/tnr/tnrref.csv` `3G9035876[A|B|C|D]`

Information Classification: General

#BHEU @BlackHatEvents

8

## Slide 9

### Affected cars – only modifications with Preh MIB3

Skoda Karoq

Skoda Kodiaq

Skoda Superb

VW Arteon

VW Passat B8 & CC

VW Polo & Golf

VW Tiguan

VW T-Roc

VW T-Cross

> 1 400 000 cars sold in 2022

Information Classification: General

#BHEU @BlackHatEvents

9

## Slide 10

# How we did it? Our story

Information Classification: General

#BHEU @BlackHatEvents

10

## Slide 11

### Vehicle ECU enumeration

To get part numbers of electronic control units (ECUs) in the car, we used diagnostic tools:

ODIS Engineering software

VAS 6154 OBD adapter

Information Classification: General

#BHEU @BlackHatEvents

11

## Slide 12

### Infotainment system info

Information Classification: General

#BHEU @BlackHatEvents

12

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pis hat
EUROPE 2024
Infotainment system info
Hardware: H22
Software: 0304
Navigation database:
22.12
Media Codec:
f9e141 py fy hii ativan BZA RERRERAK
12
Information Classification: General
```

## Slide 13

### Search ECUs by part numbers

- Official dealers and repairing shops

- Aftermarket components

- Auto junkyards

Information Classification: General

#BHEU @BlackHatEvents

13

## Slide 14

### Connecting test ECUs together

For that, we used wiring diagrams purchased at VW/Skoda erWin portal

Information Classification: General

#BHEU @BlackHatEvents

14

## Slide 15

### Skoda CAN networks, entry points, controls

#### Gateway ECU – GW MQB High J533

CAN4 Running CAN2 Convenience
CAN1 Powertrain CAN3 Infotainment Diagnostic CAN
gear sensors
Instrument cluster
Engine ECU MIB3
ABS ECU
J285
J623 infotainment
J104 E
OBD
Telematic unit
E
Transmission
Power steering  J949
ECU J743
ECU J500
KESSY J518
Airbag ECU
Parking aid
J234 Climate Body Cellular
ECU J446
Door electronic
Key fob
J386

E – Automotive Ethernet Base-T1

Information Classification: General

#BHEU @BlackHatEvents

15

## Slide 16

Screen connector (LVDS)
Preh MIB3 infotainment unit
USB hub ECU connector
Speakers
GND +12V
-
+
CAN3 H
Mic
CAN3 L
+
-
OEM part number
- -
+ +
UART
11 – their RX ETH ETH
Information Classification: General 16 12 – their TX J285 J949#BHEU @BlackHatEvents

Information Classification: General

## Slide 17

### Preh MIB3 infotainment unit internals – side A

Renesas R-Car M3 Automotive SoC

Murata WLAN + BT

32MB SPI with lowlevel firmware

64 GB eMMC with Linux FS#BHEU @BlackHatEvents

Information Classification: General

17

## Slide 18

### Preh MIB3 infotainment unit internals – side B

NXP Power Controller Chip Mentioned in MIB3 firmware as PWC ARM Cortex-M0 (32-bit)

Information Classification: General

#BHEU @BlackHatEvents

18

## Slide 19

### Firmware extraction – dump eMMC and SPI

- Desolder eMMC with infrared rework station

- Desolder SPI with hot air gun

- Use chip programmer to extract data

Chip programmers RT809H (left), DediProg NuProg E2 (right)

BGA-169 socket

Information Classification: General

#BHEU @BlackHatEvents

19

## Slide 20

### MIB3 infotainment architecture & connections

MIB3 infotainment

R-CAR M3 SoC
TrustZone Yocto Linux 4.14.75
4 Cortex A-53, 2 Cortex A-57 cores
Boot loader
Shared RAM
CARCOM FreeRTOS
Cortex R7 core

Information Classification: General

#BHEU @BlackHatEvents

20

## Slide 21

### MIB3 infotainment architecture & connections

MIB3 infotainment
R-CAR M3 SoC
eMMC
TrustZone Yocto Linux 4.14.75
Root FS
4 Cortex A-53, 2 Cortex A-57 cores
Boot loader
SPI
Shared RAM
Boot images
CARCOM FreeRTOS
Cortex R7 core

Information Classification: General

#BHEU @BlackHatEvents

21

## Slide 22

### MIB3 infotainment architecture & connections

MIB3 infotainment
R-CAR M3 SoC
eMMC
TrustZone Yocto Linux 4.14.75
Root FS
Eth Base-T1
4 Cortex A-53, 2 Cortex A-57 cores Instrument
Boot loader
cluster
SPI
Eth Base-T1
Shared RAM
Telematic
Boot images
unit
CAN3
Gateway
CARCOM FreeRTOS
ECU
Cortex R7 core

Information Classification: General

#BHEU @BlackHatEvents

22

## Slide 23

### MIB3 infotainment architecture & connections

Bluetooth
MIB3 infotainment
R-CAR M3 SoC
Wi-Fi
Baseband
USB in the car
eMMC
TrustZone Yocto Linux 4.14.75
UART via ECU connector
Root FS
Eth Base-T1
4 Cortex A-53, 2 Cortex A-57 cores Instrument
Boot loader
cluster
SPI
Eth Base-T1
Shared RAM
Telematic
Boot images
unit
CAN3
Gateway
CARCOM FreeRTOS
ECU
Cortex R7 core

Information Classification: General

#BHEU @BlackHatEvents

23

## Slide 24

### UART – locked with RSA-based challenge-response

```
pwc: 16:02:11,204 inituart0 (cpu)...
pwc: 16:02:11,204 inituart1 (carcom)...
<...SNIP...>
```

```
[    0.021224] NOTICE:  BL2:
v1.5(release):mqb_sop2-15.20.110
```

```
[    0.025218] NOTICE:  BL2: Secure boot
```

```
[    0.092902] NOTICE:  R7: loaded
[    0.098896] NOTICE:  BL31: loaded
```

```
<...SNIP...>
```

```
Welcome to Linux!
```

```
skoda-infotainment-5572 login: root
1-time code:
```

```
C0670D36FB788E5B673007DEA7A4DFB13CF9E28CBC2129C
AE94DA92DB871C28A15529C6CDBF9E1384096E7E6328088
DD1F95AB7FBDB0EEFD37F1CB061DDB01BD
```

```
root
```

`invalid input lenght (4)` UART capture `Login incorrect`

Authentication is implemented in _/lib/security/pam_pcc.so pam_sm_authenticate()_ function

Information Classification: General

#BHEU @BlackHatEvents

24

## Slide 25

### No luck with UART. Bluetooth analysis

Bluetooth
MIB3 infotainment
R-CAR M3 SoC
Baseband
Yocto Linux 4.14.75
UART via ECU connector
Boot loader

Information Classification: General

#BHEU @BlackHatEvents

25

## Slide 26

### Bluetooth service

- System service with name “phone”

- Is used for:

   - Making calls

   - Playing music

   - Phone book and messages sync

- CarPlay

-

- …

Information Classification: General

#BHEU @BlackHatEvents

26

## Slide 27

### Phone book synchronization

- Implemented according to Phone Book Access Profile (PBAP)

- Phone Book Access Profile:

   - Provides opportunity to exchange phone book and call history between IVI and phone

   - Is tailored for Hands-Free Profile (HFP)*

   - • Works over OBEX protocol

   - Requires pairing between phone and IVI

- This is done so that the IVI user can use contacts from the phone book (for example, for calls).

Information Classification: General

#BHEU @BlackHatEvents

27

## Slide 28

### Phone Book Access Profile

- There are two entities:

   - Phone Book Client Equipment (PCE) – This is the device that retrieves phone book objects from the Server Equipment

   - • Phone Book Server Equipment (PSE) – This is the device that contains the source phone book objects

Information Classification: General

#BHEU @BlackHatEvents

28

## Slide 29

### Phone book format

- This format described in RFC6350

- Phone book is a sequence of vCards

- Each vCard is a set of properties between BEGIN:VCARD and END:VCARD

   - Required properties are VERSION, TEL, N (ver. 2.1 and 3.0), FN (ver. 3.0 and 4.0)

   - Property PHOTO can be used to set a picture for contact

```
BEGIN:VCARD
VERSION:2.1
FN:ChristopherNolan
N:Nolan;Christopher;;;
TEL;CELL:1234567890
PHOTO;ENCODING=B;TYPE=JPEG:<image content in base64>
END:VCARD
```

Information Classification: General

#BHEU @BlackHatEvents

29

## Slide 30

### Contact’s PHOTO handling

Original photo is scaled to size 100x100 to fit well on the contacts menu.

The scaling procedure has 2 steps:

1. Conversion of the original photo to scaled bitmap;

2. Creation of JPEG picture from this bitmap.

In case of JPEG image, libjpeg with version 9c is used.

original

in contacts

menu

Information Classification: General

#BHEU @BlackHatEvents

30

## Slide 31

### Reading bitmap data during JPEG handing

1. Allocation of scanline_buffer* (with size 0x4000 bytes).

2. Reading the bitmap data to this buffer (by using jpeg_read_scanlines function).

Is scan line buffer long enough to store a very long scan line?

- Scan line is a row of pixels in the image

Information Classification: General

#BHEU @BlackHatEvents

31

## Slide 32

### Scan line maximum size

- Maximum JPEG image width is around 65535 (0xffff) pixels

- • Pixel size depends on the color space that is used (RGB, CMYK, …)

- • Maximal size of the pixel 4 bytes for the libjpeg library in this MIB3*

- • Therefore, maximum length of a scan line is 4 * 0xffff = 0x3fffc bytes

* It equals 4 for the set of all known color spaces in this library build. For unknown color space (JCS_UNKNOWN), it can be more. For us, it is enough to have 4 bytes per pixel.

Information Classification: General

#BHEU @BlackHatEvents

32

## Slide 33

### Scaling feature usage

- In our case, libjpeg internal scaling feature is used with the scaling multiplier 1/8*

- This fact changes maximum scan line size to 0x3fffc / 8 ≈ 0x7fff bytes

- This is still more than 0x4000, and we have the heap overflow!

- The multiplier 1/8 is the minimum possible for libjpeg.

Information Classification: General

#BHEU @BlackHatEvents

33

## Slide 34

### How to control output Bitmap data

- Version 9c of libjpeg doesn’t have any implementation of lossless algorithm :(

- • The naive approach of lossy algorithm usage wasn’t successful:

Information Classification: General

#BHEU @BlackHatEvents

34

## Slide 35

### How to control output Bitmap data

• But the following approach worked well for us:

Works only for one scan line image case

Information Classification: General

#BHEU @BlackHatEvents

35

## Slide 36

### How to trigger the vulnerability

- Raspberry Pi 4 (as fake phone).

- Tool nOBEX from NCCGroup* (to emulate PBAP and HFP Bluetooth profiles)

- For nOBEX, we need to make the file with responses for HFP profile.**

- https://github.com/nccgroup/nOBEX

- A big thanks to NCCGroup for this tool!

- ** It can be generated from Bluetooth traffic between IVI and phone.

Information Classification: General

#BHEU @BlackHatEvents

36

## Slide 37

Triggering of the vulnerability in Bluetooth service This is the MIB3 UART debug log during vulnerability triggering process:

Information Classification: General

#BHEU @BlackHatEvents

37

## Slide 38

### What do we have now?

- ✓ We have the buffer overflow on heap

- ✓ We can control the length and content of scan line data

- No ASLR for main executable

CFI or any Pointer Guard (like in glibc) mechanisms aren’t used for libjpeg

What do we want to overwrite to achieve RCE?

Information Classification: General

#BHEU @BlackHatEvents

38

## Slide 39

Exploitation strategy Objects from libjpeg are looking interesting:

- They are allocated inside large memory pools on the heap;

- They have a lot of function pointers.

Very simple exploitation strategy was used:

1. Place a libjpeg obj pool after the scan line buffer by manipulating the heap.

2. Overwrite any function pointer inside some object from this pool with a gadget address.

3. Trigger the usage of this gadget and apply JOP+ROP techniques to get RCE.

Information Classification: General

#BHEU @BlackHatEvents

39

## Slide 40

### LPE

- Phone service has:

   - There are several possible targets:

- dedicated UID

   - Linux kernel

- CAP_SYS_NICE

   - Privileged services

- No sandboxing (!)

- SUID executables

-

- …

Information Classification: General

#BHEU @BlackHatEvents

40

## Slide 41

### Custom IPC mechanism in MIB3 RCAR M3 SoC

Information Classification: General

#BHEU @BlackHatEvents

41

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
EUROPE 2024
Custom IPC mechanism in MIB3 RCAR M3 SoC
Carcom chip services
shared memory
Audio DSP chip services
Linux
phone | networking
Information Classification: General 1
41
```

## Slide 42

### Lack of access control in MIB3 custom IPC

Information Classification: General

#BHEU @BlackHatEvents

42

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
EUROPE 2024
Lack of access control in MIB3 custom IPC
Carcom chip services Audio DSP chip services
shared memory
Linux
mib3.root No access control checks
Information Classification: General
42
```

## Slide 43

### Shell injection in Networking service

- MIB3 has RPC mechanism that is based on MIB3 custom IPC.

- We can make RPC of initCarPlayInterface function in the Networking service and pass a string with shell command to it as the argument.

- • Profit!

Information Classification: General

#BHEU @BlackHatEvents

43

## Slide 44

### Getting root privileges

- Networking service has:

   - Dedicated UID;

   - A lot of capabilities. One of them is CAP_SYS_MODULE.

- Module signature verification is disabled in MIB3 Linux kernel.

Then we can achieve code execution with kernel privileges (and root privs too) :)

Information Classification: General

#BHEU @BlackHatEvents

44

## Slide 45

### Demo: getting root privileges

Watch on YouTube: https://youtu.be/cqBSh8xg-rM

Information Classification: General

#BHEU @BlackHatEvents

45

## Slide 46

### From RCE on Yocto Linux to CAN bus

MIB3 infotainment
R-CAR M3 SoC
Baseband
Yocto Linux 4.14.75
UART via ECU connector
4 Cortex A-53, 2 Cortex A-57 cores
Shared RAM
We are
here now

Information Classification: General

#BHEU @BlackHatEvents

46

## Slide 47

### From RCE on Yocto Linux to CAN bus

MIB3 infotainment
R-CAR M3 SoC
Baseband
Yocto Linux 4.14.75
UART via ECU connector
4 Cortex A-53, 2 Cortex A-57 cores
Shared RAM
Our next
target CARCOM FreeRTOS
Cortex R7 core

Information Classification: General

#BHEU @BlackHatEvents

47

## Slide 48

### Achieving code exec inside Carcom chip

Information Classification: General

#BHEU @BlackHatEvents

48

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
EUROPE 2024
Achieving code exec inside Carcom chip
R-CAR M3 SoC
| Linux OS CPU set Shared RAM
Linux OS CPU
1 | uses memory for OS
Carcom code and (rwx access)
data <— >
| Carcom CPU
communication with Linux OS
rw access
Linux OS CPU + communication with Carcom OS ereleal IG ( )
memory
' : (rw access)
Information Classification: General 48
```

## Slide 49

### Achieving code exec inside Carcom chip

Information Classification: General

#BHEU @BlackHatEvents

49

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
EUROPE 2024
Achieving code exec inside Carcom chip
R-CAR M3 SoC
Linux OS CPU set
Linux OS CPU |
Shared RAM
Linux CPUs have rw access too! our injected code
uses memory for OS
Carcom code and (rwx access)
data <— >
Carcom CPU
communication with Linux OS
Shared IPC (rw access)
memory
Linux OS CPU
communication with Carcom OS
(rw access)
Information Classification: General 49
```

## Slide 50

### Access to CAN bus

#### Carcom logs

Patch this call to read from CAN

#### candump output

```
char can_msg[8] = "\x11\x22\x33\x44\xaa\xaa\xaa\xaa";
while (1) {
```

```
// can_writeis the function from Carcomfirmware
can_write(0x666, can_msg, 8);
```

Information Classification: General

#BHEU @BlackHatEvents

50

## Slide 51

### Can’t bypass gateway…

MIB3 infotainment
R-CAR M3 SoC
Baseband
Yocto Linux 4.14.75
UART via ECU connector
4 Cortex A-53, 2 Cortex A-57 cores
Shared RAM
CAN3
Gateway
CARCOM FreeRTOS
ECU
Cortex R7 core

#BHEU @BlackHatEvents

Information Classification: General

51

## Slide 52

### … But obtained persistence on IVI

MIB3 infotainment
R-CAR M3 SoC
Baseband
eMMC
Yocto Linux 4.14.75
UART via ECU connector
Root FS
4 Cortex A-53, 2 Cortex A-57 cores
SPI
Shared RAM
Boot images
Our next target –
CAN3
Gateway
persistent storage CARCOM FreeRTOS
ECU
Cortex R7 core

Information Classification: General

#BHEU @BlackHatEvents

52

## Slide 53

### Available persistent storage & storage protections

- eMMC 64 GB

   - Linux root FS is read-only & protected by dm-verity

   - /var is RW, but no binary executables. Can be used to store payload

- SPI 32 MB contains boot images

   - Image integrity is protected by secure boot

Information Classification: General

#BHEU @BlackHatEvents

53

## Slide 54

### ARM Trusted Firmware

- Preh MIB3 secure boot is based on Renesas ARM Trusted Firmware  for R-Car SoCs

   - <u>https://github.com/renesas-rcar/arm-trusted-firmware</u>

- Renesas ARM Trusted Firmware originates from ARM repository

   - The open-source reference implementation of secure world software for ARM.

   - <u>https://github.com/ARM-software/arm-trusted-firmware</u>

- Preh MIB3 has a proprietary feature – image compression

- This feature appeared vulnerable

Information Classification: General

#BHEU @BlackHatEvents

54

## Slide 55

### ARM Trusted Firmware boot on Preh MIB3 1

- R-CAR M3 ROM BL1

- 1.1 BL1 copies BL2 into RAM 1.2 BL1 verifies BL2 by certificate 1.3 BL1 passes control to BL2

Uncompressed image
Image(s) certificate(s) for secure boot
Compressed image

SPI 32 MB R-CAR M3 RAM
BL2 cert
BL2
BL3_X certs
BL31 – EL3 FW
BL32 – TEE OS
BL332 – CARCOM
BL334 – dev tree
BL333 – yocto krnl
BL335 – initrd BL2

RAM addresses

E6 08 00 00

Information Classification: General

#BHEU @BlackHatEvents

55

## Slide 56

### ARM Trusted Firmware boot on Preh MIB3 2

SPI 32 MB R-CAR M3 RAM
R-CAR M3 ROM
BL2 cert
BL1
BL2
BL3_X certs
2.1 BL2 uncompresses CARCOM to RAM
2.2 BL2 verifies CARCOM by certificate
BL31 – EL3 FW
2.3 BL2 starts CARCOM on R7 core
BL32 – TEE OS
BL332 – CARCOM
BL334 – dev tree
Uncompressed image
BL333 – yocto krnl CARCOM
Image(s) certificate(s) for secure boot
BL335 – initrd
BL2
Compressed image

- 2.1 BL2 uncompresses CARCOM to RAM 2.2 BL2 verifies CARCOM by certificate 2.3 BL2 starts CARCOM on R7 core

RAM addresses

51 80 00 00 E6 08 00 00

Information Classification: General

#BHEU @BlackHatEvents

56

## Slide 57

### ARM Trusted Firmware boot on Preh MIB3 3

SPI 32 MB R-CAR M3 RAM RAM addresses
R-CAR M3 ROM
BL2 cert
BL1
BL2 EL3 FW 44 00 00 00
TEE OS 44 10 00 00
BL3_X certs
3.1 BL2 loads EL3 FW
3.1
3.2 BL2 loads TEE OS
BL31 – EL3 FW
3.2
BL32 – TEE OS
BL332 – CARCOM
BL334 – dev tree
Uncompressed image
BL333 – yocto krnl CARCOM
51 80 00 00
Image(s) certificate(s) for secure boot
BL335 – initrd
BL2 E6 08 00 00
Compressed image

R-CAR M3 ROM BL1 3.1 BL2 loads EL3 FW 3.2 BL2 loads TEE OS

Information Classification: General

#BHEU @BlackHatEvents

57

## Slide 58

### ARM Trusted Firmware boot on Preh MIB3 4

R-CAR M3 ROM
BL1

4.1 BL2 loads kernel 4.2 BL2 loads device tree 4.3 BL2 loads initrd

Uncompressed image Image(s) certificate(s) for secure boot Compressed image

SPI 32 MB
BL2 cert
BL2

##### R-CAR M3 RAM

EL3 FW

BL3_X certs
BL31 – EL3 FW
BL32 – TEE OS
BL332 – CARCOM
BL334 – dev tree
BL333 – yocto krnl
BL335 – initrd

TEE OS

4.2
device tree
4.1
yocto krnl
4.3
initrd
CARCOM
BL2

RAM addresses

44 00 00 00

44 10 00 00

48 00 00 00

48 08 00 00

4C 00 00 00

51 80 00 00

E6 08 00 00

Information Classification: General

#BHEU @BlackHatEvents

58

## Slide 59

### Compressed image and certificate format

#### Compressed image (example for BL31)

Magic Compressed size

Decompressed size

LZ4-compressed data

Certificate

Size: 0x800 bytes Only first 0x368 bytes are meaningful

**Offset Size Description** 0x1D4 8 Image load address 0x364 4 Image size in DWORDs

**Example value (BL31)** 44 00 00 00 (hex) 00 00 30 24 (hex)

Information Classification: General

#BHEU @BlackHatEvents

59

## Slide 60

### Vulnerability in BL2

- Signature verification happens after decompression

- For decompression, file size from PCCP header is used

- For signature verification, size from certificate is used

- It’s possible to append arbitrary content to each compressed image, and signature verification will still succeed

- Vulnerability is in proprietary code (not in Renesas ARM Trusted Firmware repository)

Information Classification: General

#BHEU @BlackHatEvents

60

## Slide 61

### Vulnerability in BL2 (2)

R-CAR M3 ROM
BL1

4.1 BL2 loads kernel

- 4.2 BL2 loads device tree

4.3 BL2 loads initrd

Uncompressed image Image(s) certificate(s) for secure boot Compressed image

SPI 32 MB
BL2 cert
BL2
BL3_X certs
BL31 – EL3 FW
BL32 – TEE OS
BL332 – CARCOM
BL334 – dev tree
BL333 – yocto krnl
BL335 – initrd

Arbitrary initrd tail Can overwrite CARCOM

R-CAR M3 RAM

EL3 FW

TEE OS

device tree

yocto krnl

initrd

CARCOM BL2

RAM addresses

44 00 00 00

44 10 00 00

48 00 00 00

48 08 00 00

4C 00 00 00

51 80 00 00

E6 08 00 00

Information Classification: General

#BHEU @BlackHatEvents

61

## Slide 62

### Vulnerability in BL2 (3)

When we were trying to modify Carcom with this vulnerability, we noticed the following error:

This error shows that our additional part of initrd is also used by Linux kernel.

Information Classification: General

#BHEU @BlackHatEvents

62

## Slide 63

### How is initrd used in MIB3?

- Linux kernel unpacks initrd image from RAM to temporary rootfs (with type ramfs).

- Linux runs “init” script from temporary rootfs to mount the real rootfs with integrity check enabled (dm-verity).

Information Classification: General

#BHEU @BlackHatEvents

63

## Slide 64

### Initrd structure: CPIO format

- CPIO file is just sequence of file records

- Each file record contains:

   - File metadata (path, size, etc.)

   - File data

- The last file record should have name “TRAILER!!!” (common CPIO unpacker should finish, if it reached this file)

Information Classification: General

#BHEU @BlackHatEvents

64

## Slide 65

### What can we do with it?

- In initrd case, the trailer file is not the end of the CPIO archive.

- Therefore, we can try to add our file records in the end of initrd.

Information Classification: General

#BHEU @BlackHatEvents

65

## Slide 66

### What can we do with it?

- In initrd case, the trailer file is not the end of the CPIO archive.

- Therefore, we can try to add our file records in the end of initrd.

- File record can have the same path.

- We can overwrite init script and bypass persistence!

Information Classification: General

#BHEU @BlackHatEvents

66

## Slide 67

### Demo with persistence

For example, this bug can be used to permanently disable PAM authentication for login command on UART interface:

Our Hello World after reboot :)

UART shell root access is available now

Information Classification: General

#BHEU @BlackHatEvents

67

## Slide 68

### Phone contact database

Contact database is stored on Preh MIB3 as SQLITE db under: `/var/lib/tsd.bt.phone.mib3/database`

Profile pictures are stored under: `/var/lib/tsd.bt.phone.mib3/photo/`

Contact data is not encrypted on the infotainment unit

Information Classification: General

#BHEU @BlackHatEvents

68

## Slide 69

### Attack summary 1. One-time access via BT

MIB3 infotainment
R-CAR M3 SoC
Baseband
Attack via Bluetooth
Pairing required
eMMC
Yocto Linux 4.14.75
Root FS
4 Cortex A-53, 2 Cortex A-57 cores
SPI
Shared RAM
Boot images
unit
CAN3
Gateway
CARCOM FreeRTOS
ECU
Cortex R7 core

Information Classification: General

#BHEU @BlackHatEvents

69

## Slide 70

### Attack summary 2. Infection with malware

MIB3 infotainment
R-CAR M3 SoC
Baseband
eMMC
Yocto Linux 4.14.75
Root FS
4 Cortex A-53, 2 Cortex A-57 cores
SPI
Shared RAM
Boot images
unit
CAN3
Gateway
CARCOM FreeRTOS
ECU
Cortex R7 core

Information Classification: General

#BHEU @BlackHatEvents

70

## Slide 71

### Attack summary 3. Remote control via DNS

MIB3 infotainment
R-CAR M3 SoC
Baseband
eMMC
Yocto Linux 4.14.75
Root FS
4 Cortex A-53, 2 Cortex A-57 cores
SPI
Eth Base-T1 DNS
Shared RAM
Telematic
Boot images
unit
eSIM
CAN3 Internet
Gateway
CARCOM FreeRTOS
ECU
Cortex R7 core

Information Classification: General

#BHEU @BlackHatEvents

71

## Slide 72

### Attack impact demonstration

https://youtu.be/lo2WTsRthZ4

Watch on YouTube: https://youtu.be/T4v8H0qJSOg

Information Classification: General

#BHEU @BlackHatEvents

72

## Slide 73

### List of identified vulnerabilities

- CVE-2023-28902 DoS via integer underflow in picserver

- CVE-2023-28903 DoS via integer overflow in picserver

-

   - CVE-2023-28904 Secure boot bypass in BL2

- CVE-2023-28905 Heap buffer overflow in picserver

-

   - CVE-2023-28906 Command injection in networking service

- CVE-2023-28907 Lack of access restrictions in CARCOM memory

- CVE-2023-28908 Integer overflow in non-fragmented data (phone service)

- CVE-2023-28909 Integer overflow leading to MTU bypass (phone service)

-

   - CVE-2023-28910 Disabled abortion flag (phone service)

- CVE-2023-28911 Arbitrary channel disconnection leading to DoS (phone servcie)

- CVE-2023-28912 Clear-text phonebook information

- CVE-2023-29113 Lack of access control in custom IPC mechanism

Information Classification: General

#BHEU @BlackHatEvents

73

## Slide 74

### Vulnerability chaining

#### Bluetooth vector. Prerequisite: pairing required

CVE-2023CVE-2023CVE-2023-28905 Code execution 28906 29113 CVE-2023CVE-2023as 'phone' user CVE-2023Access 28909 28910 28912 phone CVE-2023DoS of Preh contact 28911 MIB3 ECU database

CVE-2023Send/recv 28907 CAN3 Privesc to 'root' CVE-2023Persistence 28904

#### USB vector (local). Prerequisite: access inside the vehicle

CVE-202328902 DoS of Preh CVE-2023MIB3 ECU 28903

Information Classification: General

#BHEU @BlackHatEvents

74

## Slide 75

### Disclosure timeline

- 07.03.2023 – vulnerabilities reported to vulnerability@volkswagen.de

- 11.04.2023 – VW requested clarifications

- 26.04.2023 – PCA sent clarifications to VW

- 22.06.2023 – First meeting of PCA and VW. VW confirms findings. Remediation is in progress

- End of 2023 – beginning of 2024 – VW informs PCA that vulnerabilities are remediated

- 08.2024 – PCA applies to BH EU and informs VW

- 12.12.2024 – public disclosure of the findings at BH EU 2024

Information Classification: General

#BHEU @BlackHatEvents

75

## Slide 76

### Thanks to contributors

- Mikhail Evdokimov

- Aleksei Stennikov

- Polina Smirnova

- Radu Motspan

- Abdellah Benotsmane

- Balazs Szabo

- Anna Breeva

- All PCAutomotive crew

Separate thanks to VW CSIRT for processing our findings

Information Classification: General

#BHEU @BlackHatEvents

76

## Slide 77

## Thank you! Q/A time

Contact us: info@pcautomotive.com

#BHEU @BlackHatEvents
