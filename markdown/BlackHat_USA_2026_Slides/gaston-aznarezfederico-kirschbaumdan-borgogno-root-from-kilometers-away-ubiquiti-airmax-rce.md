---
title: "Root From Kilometers Away Ubiquiti AirMax RCE"
speakers: ["Gaston Aznarez", "Federico Kirschbaum", "Dan Borgogno"]
conference: "Black Hat"
conference_full: "Black Hat USA 2026"
edition: "USA"
year: 2026
source_pdf: "BlackHat_USA_2026_Slides/Gaston Aznarez&Federico Kirschbaum&Dan Borgogno_Root From Kilometers Away Ubiquiti AirMax RCE.pdf"
pages: 120
sha256: "994094fda60a15a894412b2c837971dda32d740b06ebd164393060a0cc51b609"
text_chars: 37097
ocr_pages: 53
has_ocr: true
redacted_secrets: 0
ocr_confidence: 86.4
ocr_unreliable_blocks: 0
vision_verified_pages_changed: 93
vision_verified_pages: 120
vision_verified_blocks: 2
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:35:54Z"
---
# Root From Kilometers Away Ubiquiti AirMax RCE

**Speakers:** Gaston Aznarez, Federico Kirschbaum, Dan Borgogno  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/Gaston Aznarez&Federico Kirschbaum&Dan Borgogno_Root From Kilometers Away Ubiquiti AirMax RCE.pdf` (120 pages)


## Slide 1

# BRIEFINGS

black hat

black hat USA 2026

## Slide 2

# ROOT FROM KILOMETERS AWAY

Ubiquiti AirMax RCE

Faraday

2

## Slide 3

#### WHO ARE WE?

**Gaston Aznarez** Principal Security Researcher Faraday Security

**Federico Kirschbaum** Co-Founder Faraday Security Head Of Security Lab XBOW

3

## Slide 4

# HOW DID THIS STARTED?

4

## Slide 5

### HOW DID THIS STARTED?

○ Obsession? You think?

```text
Thread
Direct message
fedek
Nov 10th, 2025 at 1:01 PM
```

5

## Slide 6

### HOW DID THIS STARTED?

○ Obsession? You think?

```text
LU1AQS
Está era la del jueves    20:23
Jajajajaja    20:23
20:23
Si te sirve de consuelo    20:55

Thread
Direct message
fedek
Nov 10th, 2025 at 1:01 PM
```

6

## Slide 7

### HOW DID THIS STARTED?

○ Obsession? You think?

```text
LU1AQS
December 11, 2025
13:30

LU1AQS
Está era la del jueves    20:23
Jajajajaja    20:23
20:23
Si te sirve de consuelo    20:55

Thread
Direct message
fedek
Nov 10th, 2025 at 1:01 PM
```

7

## Slide 8

### HOW DID THIS STARTED?

○ Obsession? You think?

```text
LU1AQS
December 11, 2025
13:30

LU1AQS
Está era la del jueves    20:23
Jajajajaja    20:23
20:23
Si te sirve de consuelo    20:55

LU1AQS
De una, nos vemos    10:08
September 1, 2025
13:04

Thread
Direct message
fedek
Nov 10th, 2025 at 1:01 PM
```

8

## Slide 9

### HOW DID THIS STARTED?

○ Obsession? You think?

```text
LU1AQS
Aparecen por todos lados    16:35
Once you see them    16:36
Message

LU1AQS
December 11, 2025
13:30

LU1AQS
Está era la del jueves    20:23
Jajajajaja    20:23
20:23
Si te sirve de consuelo    20:55

LU1AQS
De una, nos vemos    10:08
September 1, 2025
13:04

Thread
Direct message
fedek
Nov 10th, 2025 at 1:01 PM
```

9

## Slide 10

### HOW DID THIS STARTED?

○ Obsession? You think?

```text
LU1AQS
Aparecen por todos lados    16:35
Once you see them    16:36
Message

LU1AQS
December 11, 2025
13:30

LU1AQS
Está era la del jueves    20:23
Jajajajaja    20:23
20:23
Si te sirve de consuelo    20:55

LU1AQS
De una, nos vemos    10:08
September 1, 2025
13:04

Thread
Direct message
fedek
Nov 10th, 2025 at 1:01 PM

LU1AQS
September 8, 2025
14:56
September 9, 2025
14:48
14:48
14:48
+16
Message
```

10

## Slide 11

### HOW DID THIS STARTED?

○ Obsession? You think?

```text
LU1AQS
Aparecen por todos lados    16:35
Once you see them    16:36
Message

LU1AQS
December 11, 2025
13:30

LU1AQS
Está era la del jueves    20:23
Jajajajaja    20:23
20:23
Si te sirve de consuelo    20:55

LU1AQS
De una, nos vemos    10:08
September 1, 2025
13:04

LU1AQS
September 8, 2025
14:56
September 9, 2025
14:48
14:48
14:48
+16
Message
```

11

## Slide 12

### HOW DID THIS STARTED?

○ Obsession? You think?

```text
I SEE THEM
THEY ARE EVERYWHERE
imgflip.com

LU1AQS
Aparecen por todos lados    16:35
Once you see them    16:36
Message

LU1AQS
De una, nos vemos    10:08
September 1, 2025

LU1AQS
September 8, 2025
14:56
September 9, 2025
14:48
+16
Message
```

12

## Slide 13

### HOW DID THIS STARTED?

○ Obsession? You think?

```text
I SEE THEM
THEY ARE EVERYWHERE
imgflip.com

LU1AQS
De una, nos vemos    10:08
September 1, 2025

LU1AQS
September 8, 2025
14:48
Message
```

13

## Slide 14

### THEY ACTUALLY ARE

**About Ubiquiti Networks**

Ubiquiti Networks, Inc. (Nasdaq: UBNT) eliminates barriers to connectivity for under-networked enterprises, communities and consumers with its leading-edge platforms that connect hundreds of millions of people throughout the world.  **With over 60 million devices sold worldwide,** through a network of over 100 distributors, to customers in **more than 180 countries and territories,** Ubiquiti has maintained an industry-leading financial profile by leveraging a unique business model to develop products that combine innovative technology with disruptive price-to-performance characteristics.  Our growth is supported by the Ubiquiti Community, a global grass-roots community of 4 million entrepreneurial operators and systems integrators who engage in thousands of forums.  For more information, join our community at http://www.ubnt.com.

Ubiquiti, Ubiquiti Networks, the U logo, UBNT, airMAX, UniFi, airFiber, mFi, EdgeMAX and AmpliFi are registered trademarks or trademarks of Ubiquiti Networks, Inc. in the United States and other countries.

2017

14

## Slide 15

### THEY ACTUALLY ARE

**Success in Initial Target Market Demonstrated Power of Our Business Model**

- Targeted and transformed wireless broadband in underserved markets
- Superior product at disruptive price
- Shipped **37+ million airMAX®** units to ~60 countries (life-to-date)

**Built $2B airMAX® business**

airMAX ac

Copyright © Ubiquiti Networks, Inc. 2017    8

15

## Slide 16

### THEY ACTUALLY ARE

**User prompt:** How many Airmax devices were sold until now ?

Worked for 25s ›

Ubiquiti **does not publicly disclose a cumulative sales figure specifically for airMAX.**

The strongest verified number is **more than 101 million Ubiquiti devices shipped globally as of May 2020**, covering all product families—not only airMAX. `[U] Ubiquiti Investor …`

Ubiquiti's current investor page still says "nearly 85 million devices," but that text appears to be stale boilerplate originally used in 2018–2019. `[U] Ubiquiti Investor … +1`

So the defensible answer is:

> **AirMAX has sold tens of millions of devices worldwide, but Ubiquiti has never published an exact airMAX-only total. The company as a whole has shipped well over 100 million devices.**

I would avoid claiming a specific airMAX number such as 50 or 70 million without labeling it as an estimate.

_(Action icons: copy, thumbs-up, thumbs-down, share, regenerate, more; and a "Sources" chip.)_

## Slide 17

### WHAT THE ANTENNAS ARE USED FOR?

**Technology**
- Based on IEEE 802.11
- Unlicensed spectrum: primarily 2.4 GHz and 5 GHz, 60Ghz

**Network Topologies**
- Point-to-Point (PtP)
- Point-to-Multipoint (PtMP)

**Common Uses**
- Wireless Internet service providers (WISPs)
- Public and municipal CCTV
- Critical-infrastructure connectivity
- Industrial and utility networks
- Rural broadband and remote-site access

_(Right: photo of a rooftop antenna / communications tower.)_

## Slide 18

# TIME TO DIG DEEPER

18

## Slide 19

WE DID WHAT EVERYONE WOULD DO… WE FOUND SOME ANTENNAS

19

## Slide 20

### WE DID WHAT EVERYONE WOULD DO… WE FOUND SOME ANTENNAS

_(Left: photo of a pile of Ubiquiti dish antennas stacked in a room.)_

Marketplace listing:

**Antenas para internet**
$45
Electrónica › Sistemas de audio y video para el hogar
Publicado hace 14 semanas en Villa General San Martín, SJ

Enviar mensaje · Guardar · Compartir

**Detalles**
Estado — Usado - Como nuevo
Con poeta incluido

Villa General San Martín, SJ · La ubicación es aproximada

**Búsquedas relacionadas**
antenas · antena · antena para tv · antenas led · antena digital tv · antena para auto · antenas para carro

## Slide 21

##### WE DID WHAT EVERYONE WOULD DO… WE FOUND SOME ANTENNAS

###### Litebeam 5ac gen2

NanoBeam M5

21

## Slide 22

##### WE DID WHAT EVERYONE WOULD DO… WE FOUND SOME ANTENNAS

Litebeam 5ac gen2

NanoBeam M5

22

## Slide 23

##### WE DID WHAT EVERYONE WOULD DO… WE FOUND SOME ANTENNAS

23

## Slide 24

### WE COULDN'T CONNECT TO THE WI-FI

_(Screenshot of a phone's Wi-Fi "Networks" list; all SSIDs are blacked out except one, and every entry is locked/secured.)_

**Networks**

- [redacted] — Saved
- **faraday_poc** — Saved / Connection failure
- [redacted] — Saved
- [redacted]
- [redacted]
- [redacted]

## Slide 25

### WE COULDN'T CONNECT TO THE WI-FI

_(Left: the same phone Wi-Fi "Networks" list; all SSIDs blacked out except one, all locked.)_

**Networks**

- [redacted] — Saved
- **faraday_poc** — Saved / Connection failure
- [redacted] — Saved
- [redacted]
- [redacted]
- [redacted]

_(Right: the "confused white monkey" reaction meme.)_

## Slide 26

# NOW WHAT?

26

## Slide 27

### GETTING A SHELL INTO THE ANTENNA

```text
❯ ssh -o HostKeyAlgorithms=+ssh-rsa ubnt@192.168.2.8
ubnt@192.168.2.8's password:

BusyBox v1.24.2 (2025-08-22 19:57:45 EEST) built-in shell (ash)
Enter 'help' for a list of built-in commands.

XW.v6.3.22# id
uid=0(ubnt) gid=0(admin)
XW.v6.3.22#
```

That was easy

## Slide 28

### GETTING A SHELL INTO THE ANTENNA

**Hacking the hardware with hard stuff?**

- Glitching
- Find/Enable JTAG
- Hidden serial interfaces?

Just connect to the UART and configure the bootloader

```text
U-Boot 1.1.4-g2f965ccd (Jan 31 2023 - 15:08:14)

DRAM:  64 MB
Flash:  8 MB (0xc2, 0x20, 0x17)
Net:   AR8032 Detected
eth0, eth1
Board: Ubiquiti Networks AR9342 board (e815-86040.1122.0030)
Radio: 0777:e815
Reset: Normal
Hit any key to stop autoboot:  0
ar7240>
Unknown command ' - try 'help'
ar7240> setenv bootargs console=ttyS0,115200n8 root=31:03 rootfstype=squashfs init=/init
ar7240> boot
## Booting image at 9f050000 ...
   Image Name:   MIPS Ubiquiti Linux-2.6.32.71
   Created:      2025-08-22  17:05:49 UTC
   Image Type:   MIPS Linux Kernel Image (lzma compressed)
   Data Size:    979880 Bytes = 956.9 kB
```

_(Right: photo of the antenna's PCB with the UART header circled and labelled **UART** in red.)_

## Slide 29

### GETTING A SHELL INTO THE ANTENNA

_(Left: ASCII-art Ubiquiti "U" logo printed by the login banner.)_

```text
BusyBox v1.24.2 (2025-08-22 19:57:45 EEST) built-in shell (ash)
Enter 'help' for a list of built-in commands.

XW.v6.3.22# uname -a
Linux NanoBeam M5 16 2.6.32.71 #1 Fri Aug 22 20:05:15 EEST 2025 mips GNU/Linux
XW.v6.3.22# id
uid=0(ubnt) gid=0(admin) groups=0(admin)
XW.v6.3.22#
```

_(Red boxes highlight `2.6.32.71`, `mips`, and the `uid=0(ubnt) gid=0(admin) groups=0(admin)` line.)_

```text
commit 2896b357f6d1619f8ed767fe816ced87dbf5abe4
Author: Willy Tarreau <w@1wt.eu>
Date:   Sat Mar 12 14:25:38 2016 +0100

    Linux 2.6.32.71
```

_(The date `Mar 12 14:25:38 2016` is underlined in red.)_

**USERSPACE mitigations**

| Mitigation | Present? |
| --- | --- |
| NX / non-exec stack (W^X) | no |
| Stack canaries (SSP) | no |
| PIE | no |
| ASLR of the main image | no |
| RELRO (applications) | no |
| RELRO (libc / loader) | part/full |

**KERNEL / PLATFORM mitigations**

| Mitigation | Present? |
| --- | --- |
| Userspace ASLR (va_space) | weak |
| NX pages (kernel W^X) | no |
| KASLR | no |
| RODATA / module RO-NX | no |
| Module signing | no |
| Kernel stack protector | no* |

That was easy, **too easy**

## Slide 30

### WHERE DOES THAT INFO COME FROM?

_(Top: scan-results table from the device UI, with a "Scan" button at the right.)_

| MAC Address | SSID | Device Name | Radio Mode | Encryption | Signal / Noise, dBm | Frequency, GHz / Channel |
| --- | --- | --- | --- | --- | --- | --- |
| [redacted] |  |  | 802.11ac | WPA2 | -89 / -96 | 5.18 / 36 |
| 1C:6A:1B:BE:FA:3A |  |  | airMAX AC | WPA2 | -52 / -99 | 5.18 / 36 |
| 44:D9:E7:52:4D:31 | faraday_poc | NanoBeam M5 16 | 802.11n airMAX | NONE | -54 / -96 | 5.18 / 36 |

```text
XW.v6.3.22# iwlist ath0 scan
ath0      Scan completed :
          Cell 01 - Address: 78:8A:20:A2:42:97
                    ESSID:"ubnt"
                    Mode:Master
                    Frequency:5.185 GHz (Channel 37)
                    Quality=57/94  Signal level=-39 dBm  Noise level=-103 dBm
                    Encryption key:off
                    Bit Rates:54 Mb/s
                    Extra:ubnt=0e4e616e6f4265616d204d352031360000
                    Extra:ieee_mode=802.11n
          Cell 02 - Address: 1C:6A:1B:C4:67:FD
                    ESSID:""
                    Mode:Master
                    Frequency:5.18 GHz (Channel 36)
                    Quality=56/94  Signal level=-40 dBm  Noise level=-103 dBm
                    Encryption key:off
                    Bit Rates:54 Mb/s
                    Extra:ubnt=05
                    Extra:ieee_mode=802.11ac
```

_(A red arrow labelled **NanoBeam M5 16** points to the underlined `Extra:ubnt=0e4e616e6f4265616d204d352031360000`; `Extra:ubnt=05` is also underlined.)_

## Slide 31

#### SO, WHERE IS IT IMPLEMENTED?

###### **Difference in the hardware?**

- No, it's a normal Atheros Chipset

###### **Difference in the software?**

- We can install **_OpenWRT_** and it will work as a regular Wi-Fi card (No-Airmax)

- It has custom versions of the drivers

- Probably even custom firmware

THE DIFFERENCE IS **IN THE SOFTWARE**

*Terminal screenshot (right side of slide, text runs off the slide's right edge):*

```text
XW.v6.3.22# dmesg | grep Atheros
[   12.462000] ath_rate_atheros: Copyright (c) 2001-2005 Atheros C[cut off]
[   12.908000] ath_dev: Copyright (c) 2001-2007 Atheros Communicat[cut off]
[   12.951000] Copyright (c) 2005-2006 Atheros Communications, Inc[cut off]
[   13.467000] ath_ahb: 9.2.0_U11.14 (Atheros/multi-bss)
[   13.636000] wifi0: Atheros 9340: mem=0xb8100000, irq=2
```

```text
 ________                    ________       __
|        |.-----.-----.-----.|  |  |.----.|  |_
|   -    ||  _  |  -__|     ||  |  ||   _||   _|
|________||   __|_____|__|__||________||__|  |____|
         |__| WIRELESS FREEDOM
------------------------------------------------------
OpenWrt 24.10.4, r28959-29397011cc
------------------------------------------------------

root@OpenWrt:~#
```

31

## Slide 32

#### WHAT **AIRMAX** IS?

32

## Slide 33

# WHAT REALLY IS **AIRMAX**

33

## Slide 34

#### TDMA PROTOCOLS

**Time Division Multiple Access** . Everyone shares one frequency. So the base station gives each client its own time slot. They take turns, in a repeating cycle.

###### **AirMAX is a protocol and implements TDMA on top of 802.11**

*Diagram: an "airMAX" logo above a stylized beam flowing from client buildings on the left into a directional antenna on a pole at right. The beam is labeled "Timeline", then narrows into "Time Slots" (Time Slot 1, Time Slot 2, Time Slot 3, Time Slot 4), which further narrows into "Packet Prioritization" (VOIP, Data, VOIP, VOIP).*

34

## Slide 35

#### WHAT **AIRMAX** IS?

Now we know is a protocol and not a **sneaker**

35

## Slide 36

###### THIS IS NOT NEW

More TDMA capable devices

- 2001 - $300   - Motorola / Canopy

- 2003 - $1250 - Proxim Tsunami MP.11

- 2003 - $600   - Alvarion BreezeACCESS VL

- 2004 - $1500 - InfiNet Wireless InfiLINK

- 2010 - $90     - Mikrotik SXT

- 2010 - $90     - Ubiquiti AirMAX M

- 2011 - $2000 - RADWIN 5000

- 2013 - $100   - LigoWave LigoDLB

- 2013 - $200   - Cambium PMP 450

- 2015 - $130   - Ubiquiti AirMAX AC

- 2016 - $900   - Mimosa A5c

36

## Slide 37

#### WI-FI TDMA HISTORY (WITH CHEAP HARDWARE)

**… — Before Atheros**
- Every Wi-Fi chipset locks radio control
- vendors keep the HAL closed

**2006 — Atheros and the Open source drivers**
- MadWiFi (2003)
- ath5k (2007)
- ath9k (2008)

**2009 — FreeBSD TDMA Implementation**
- Proves deterministic time-slots are possible on commodity Wi-Fi silicon

**2010 — All the Vendors**
- Atheros ships one SDK
- Each adds only a thin proprietary TDMA layer
- Linux 2.6 becomes the kernel everyone freezes on

**Today — We are in the same point**
- Millions of radios still on kernel 2.6.32 (EOL Feb 2016)
- The protocols are undocumented and unresearched

37

## Slide 38

# HIDING A PROTOCOL INSIDE WIFI

38

## Slide 39

###### 802.11 BASICS - JUST FRAMES Over The Air

| MANAGEMENT | CONTROL | DATA |
|---|---|---|
| Beacon | RTS | Data |
| Probe Request | CTS | Null |
| Probe Response | ACK | QoS Data |
| Association Request | Block Ack Request | QoS Null |
| Association Response | Block Ack | Data + CF-Ack |
| Reassociation Request | PS-Poll | Data + CF-Poll |
| Reassociation Response | CF-End | Data + CF-Ack + CF-Poll |
| Authentication | CF-End + CF-Ack | CF-Ack |
| Deauthentication | Control Wrapper | CF-Poll |
| Disassociation | NDP Announcement | CF-Ack + CF-Poll |
| ATIM | Beamforming Poll | QoS Data + CF-Ack |
| Action | | QoS Data + CF-Poll |
| Action No-Ack | | QoS Data + CF-Ack + Poll |
| | | QoS CF-Poll |
| | | QoS CF-Ack + CF-Poll |

39

## Slide 40

###### 802.11 BASICS - JUST FRAMES Over The Air

| MANAGEMENT | CONTROL | DATA |
|---|---|---|
| **Beacon** | RTS | Data |
| **Probe Request** | CTS | Null |
| **Probe Response** | ACK | QoS Data |
| **Association Request** | Block Ack Request | QoS Null |
| **Association Response** | Block Ack | Data + CF-Ack |
| Reassociation Request | PS-Poll | Data + CF-Poll |
| Reassociation Response | CF-End | Data + CF-Ack + CF-Poll |
| **Authentication** | CF-End + CF-Ack | CF-Ack |
| Deauthentication | Control Wrapper | CF-Poll |
| Disassociation | NDP Announcement | CF-Ack + CF-Poll |
| ATIM | Beamforming Poll | QoS Data + CF-Ack |
| **Action** | | QoS Data + CF-Poll |
| Action No-Ack | | QoS Data + CF-Ack + Poll |
| | | QoS CF-Poll |
| | | QoS CF-Ack + CF-Poll |

*(Red boxes on this slide highlight Beacon, Probe Request, Probe Response, Association Request, Association Response, Authentication, and Action.)*

40

## Slide 41

###### 802.11 BASICS - A CONNECTION

*Hand-drawn sequence diagram between STA and AP:*

- AP → STA: Beacon
- STA → AP: Probe Request
- AP → STA: Probe Response
- STA → AP: Authentication (os)
- AP → STA: Authentication(Success)
- STA → AP: Association Request
- AP → STA: Association Response
- STA ⇄ AP: 4-Way Handshake
- STA ⇄ AP: Encrypted Data

41

## Slide 42

###### PACKET CAPTURE TIME

###### **~USD $20**

```text
[Wireshark window - ubnt_ac_multiple_reconnections.pcapng]

Filter: ((wlan.sa == 1c:6a:1b:c4:67:fd || wlan.sa == 1c:6a:1b:be:fa:3a) && (wlan.da == 1c:6a:1b:c4:67:fd || wlan.da == 1c:6a:1b:be:fa:3a || wlan.da == ff:ff:ff:ff:ff:ff )) && !(wlan.fc.type_s

No.   Time        Source              Destination         Info
5881  85.716759   Ubiquiti_be:fa:3a   Ubiquiti_c4:67:fd   Probe Request, SN=259, FN=0, Flags=........C, SSID=W
5882  85.717099   Ubiquiti_be:fa:3a   Broadcast           Probe Request, SN=260, FN=0, Flags=........C, SSID=W
5883  85.717444   Ubiquiti_c4:67:fd   Ubiquiti_be:fa:3a   Probe Response, SN=2746, FN=0, Flags=........C, BI=1
5885  85.718496   Ubiquiti_c4:67:fd   Ubiquiti_be:fa:3a   Probe Response, SN=2747, FN=0, Flags=........C, BI=1
5886  85.739038   Ubiquiti_c4:67:fd   Broadcast           Beacon frame, SN=2748, FN=0, Flags=........C, BI=100
5889  85.748085   Ubiquiti_be:fa:3a   Ubiquiti_c4:67:fd   Probe Request, SN=261, FN=0, Flags=........C, SSID=W
5890  85.748094   Ubiquiti_be:fa:3a   Broadcast           Probe Request, SN=262, FN=0, Flags=........C, SSID=W
5892  85.749297   Ubiquiti_c4:67:fd   Ubiquiti_be:fa:3a   Probe Response, SN=2750, FN=0, Flags=........C, BI=1
5893  85.841836   Ubiquiti_c4:67:fd   Broadcast           Beacon frame, SN=2751, FN=0, Flags=........C, BI=100
5896  85.886664   Ubiquiti_be:fa:3a   Ubiquiti_c4:67:fd   Probe Request, SN=256, FN=0, Flags=........C, SSID='
5897  85.886686   Ubiquiti_c4:67:fd   Ubiquiti_be:fa:3a   Probe Response, SN=2752, FN=0, Flags=........C, BI=1
5898  85.887629   Ubiquiti_be:fa:3a   Ubiquiti_c4:67:fd   Authentication, SN=257, FN=0, Flags=........C
5899  85.887636   Ubiquiti_c4:67:fd   Ubiquiti_be:fa:3a   Authentication, SN=2753, FN=0, Flags=........C
5900  85.889551   Ubiquiti_be:fa:3a   Ubiquiti_c4:67:fd   Association Request, SN=258, FN=0, Flags=........C
5901  85.891087   Ubiquiti_c4:67:fd   Ubiquiti_be:fa:3a   Association Response, SN=256, FN=0, Flags=........C
5902  85.902799   Ubiquiti_be:fa:3a   Ubiquiti_c4:67:fd   Key (Message 2 of 4)
5903  85.904167   Ubiquiti_c4:67:fd   Ubiquiti_be:fa:3a   Key (Message 3 of 4)
5904  85.906988   Ubiquiti_be:fa:3a   Ubiquiti_c4:67:fd   Key (Message 4 of 4)
5913  86.048352   Ubiquiti_c4:67:fd   Broadcast           Beacon frame, SN=2755, FN=0, Flags=........C, BI=100
5933  86.148396   Ubiquiti_c4:67:fd   Broadcast           Beacon frame, SN=2756, FN=0, Flags=........C, BI=100

> Frame 3197: Packet, 179 bytes on wire (1432 bits), 179 bytes captured (1432 bits) on interface -,
> Radiotap Header v0, Length 36
> 802.11 radio information
v IEEE 802.11 QoS Data, Flags: ......FTC
    Type/Subtype: QoS Data (0x0028)
    v Frame Control Field: 0x8803
       .... ..00 = Version: 0
       .... 10.. = Type: Data frame (2)
       1000 .... = Subtype: 8
     > Flags: 0x03
    .000 0000 0011 1100 = Duration: 60 microseconds
  > Receiver address: Ubiquiti_c4:67:fd (1c:6a:1b:c4:67:fd)
  > Transmitter address: Ubiquiti_be:fa:3a (1c:6a:1b:be:fa:3a)

0000  00
0010  04
0020  00 00 de 00 88 03 3c 00   1c 6a 1b c4 67
0030  1b be fa 3a 1c 6a 1b c4   67 fd 10 00 1c
0040  fa 3a 07 00 aa aa 03 00   00 00 88 8e 01
0050  02 03 0a 00 00 00 00 00   00 00 00 00 02
0060  00 00 00 00 00 00 00 00   00 00 00 00 00
0070  00 00 00 00 00 00 00 00   00 00 00 00 00
0080  00 00 00 00 00 00 00 00   00 00 00 00 00
0090  00 00 00 00 00 00 00 00   00 00 00 00 00
00a0  04 4f 5e 42 15 a5 95 d6   d1 7a 3f 76 b0
00b0  61 93 9a

Frame subtype (wlan.fc.subtype), 4 bits        Packets: 15097 · Displayed: 2057 (13.6%)        Profile: Default

[Overlaid product listing screenshot, right side]
Ver más productos marca TP-Link
Nuevo | +10 mil vendidos
MÁS VENDIDO   2º en Placas de Red
Receptor Wifi Tp Link T2u Ac600 Plus Adaptador Red Usb Wifi Dual Band Internet
4.8 (4093)
$ 35.647      ~USD $20
Mismo precio en 6 cuotas de $ 5.941,17 sin tarjeta
Precio sin impuestos nacionales: $ 32.260
Ver los medios de pago

Lo que tenés que saber de este producto
- Operación en doble ban[illegible] GHz que permite mayor e[illegible]on para actividades[illegible]
- Tasa d[illegible]33 Mbps en 5 GH[illegible]asta 14 MB/s en
```

42

## Slide 43

###### IT WORKS LIKE A NORMAL IEEE 802.11 WIFI

| Source | Destination | Info |
|---|---|---|
| Ubiquiti_c4:67:fd | Broadcast | Beacon frame, SN=2748, |
| Ubiquiti_c4:67:fd | Broadcast | Beacon frame, SN=2751, |
| Ubiquiti_be:fa:3a | Ubiquiti_c4:67:fd | Probe Request, SN=256, |
| Ubiquiti_c4:67:fd | Ubiquiti_be:fa:3a | Probe Response, SN=275 |
| Ubiquiti_be:fa:3a | Ubiquiti_c4:67:fd | Authentication, SN=257 |
| Ubiquiti_c4:67:fd | Ubiquiti_be:fa:3a | Authentication, SN=275 |
| Ubiquiti_be:fa:3a | Ubiquiti_c4:67:fd | Association Request, S |
| Ubiquiti_c4:67:fd | Ubiquiti_be:fa:3a | Association Response, |
| Ubiquiti_be:fa:3a | Ubiquiti_c4:67:fd | Key (Message 2 of 4) |
| Ubiquiti_c4:67:fd | Ubiquiti_be:fa:3a | Key (Message 3 of 4) |
| Ubiquiti_be:fa:3a | Ubiquiti_c4:67:fd | Key (Message 4 of 4) |

## Slide 44

###### IT WORKS LIKE A NORMAL IEEE 802.11 WIFI

*A curly brace on the left labeled "Broadcast & Probing" spans the first four table rows (both Beacon frames, the Probe Request, and the Probe Response).*

| Source | Destination | Info |
|---|---|---|
| Ubiquiti_c4:67:fd | Broadcast | Beacon frame, SN=2748, |
| Ubiquiti_c4:67:fd | Broadcast | Beacon frame, SN=2751, |
| Ubiquiti_be:fa:3a | Ubiquiti_c4:67:fd | Probe Request, SN=256, |
| Ubiquiti_c4:67:fd | Ubiquiti_be:fa:3a | Probe Response, SN=275 |
| Ubiquiti_be:fa:3a | Ubiquiti_c4:67:fd | Authentication, SN=257 |
| Ubiquiti_c4:67:fd | Ubiquiti_be:fa:3a | Authentication, SN=275 |
| Ubiquiti_be:fa:3a | Ubiquiti_c4:67:fd | Association Request, S |
| Ubiquiti_c4:67:fd | Ubiquiti_be:fa:3a | Association Response, |
| Ubiquiti_be:fa:3a | Ubiquiti_c4:67:fd | Key (Message 2 of 4) |
| Ubiquiti_c4:67:fd | Ubiquiti_be:fa:3a | Key (Message 3 of 4) |
| Ubiquiti_be:fa:3a | Ubiquiti_c4:67:fd | Key (Message 4 of 4) |

44

## Slide 45

###### IT WORKS LIKE A NORMAL IEEE 802.11 WIFI

*Two curly braces on the left: "Broadcast & Probing" spans the first four table rows; "Open System Auth. and Assoc" spans the next four rows (both Authentication frames, the Association Request, and the Association Response).*

| Source | Destination | Info |
|---|---|---|
| Ubiquiti_c4:67:fd | Broadcast | Beacon frame, SN=2748, |
| Ubiquiti_c4:67:fd | Broadcast | Beacon frame, SN=2751, |
| Ubiquiti_be:fa:3a | Ubiquiti_c4:67:fd | Probe Request, SN=256, |
| Ubiquiti_c4:67:fd | Ubiquiti_be:fa:3a | Probe Response, SN=275 |
| Ubiquiti_be:fa:3a | Ubiquiti_c4:67:fd | Authentication, SN=257 |
| Ubiquiti_c4:67:fd | Ubiquiti_be:fa:3a | Authentication, SN=275 |
| Ubiquiti_be:fa:3a | Ubiquiti_c4:67:fd | Association Request, S |
| Ubiquiti_c4:67:fd | Ubiquiti_be:fa:3a | Association Response, |
| Ubiquiti_be:fa:3a | Ubiquiti_c4:67:fd | Key (Message 2 of 4) |
| Ubiquiti_c4:67:fd | Ubiquiti_be:fa:3a | Key (Message 3 of 4) |
| Ubiquiti_be:fa:3a | Ubiquiti_c4:67:fd | Key (Message 4 of 4) |

45

## Slide 46

###### IT WORKS LIKE A NORMAL IEEE 802.11 WIFI

| Source | Destination | Info |
|--------|-------------|------|
| Ubiquiti_c4:67:fd | Broadcast | Beacon frame, SN=2748, |
| Ubiquiti_c4:67:fd | Broadcast | Beacon frame, SN=2751, |
| Ubiquiti_be:fa:3a | Ubiquiti_c4:67:fd | Probe Request, SN=256, |
| Ubiquiti_c4:67:fd | Ubiquiti_be:fa:3a | Probe Response, SN=275 |
| Ubiquiti_be:fa:3a | Ubiquiti_c4:67:fd | Authentication, SN=257 |
| Ubiquiti_c4:67:fd | Ubiquiti_be:fa:3a | Authentication, SN=275 |
| Ubiquiti_be:fa:3a | Ubiquiti_c4:67:fd | Association Request, S |
| Ubiquiti_c4:67:fd | Ubiquiti_be:fa:3a | Association Response, |
| Ubiquiti_be:fa:3a | Ubiquiti_c4:67:fd | Key (Message 2 of 4) |
| Ubiquiti_c4:67:fd | Ubiquiti_be:fa:3a | Key (Message 3 of 4) |
| Ubiquiti_be:fa:3a | Ubiquiti_c4:67:fd | Key (Message 4 of 4) |

Left-side group brackets: **Broadcast & Probing** (rows 1-4), **Open System Auth. and Assoc** (rows 5-8), **4-Way Handshake** (rows 9-11). (The Info column is cut off at the table's right edge.)

## Slide 47

###### IT WORKS LIKE A NORMAL IEEE 802.11 WIFI

| Source | Destination | Info |
|--------|-------------|------|
| Ubiquiti_c4:67:fd | Broadcast | Beacon frame, SN=2748, |
| Ubiquiti_c4:67:fd | Broadcast | Beacon frame, SN=2751, |
| Ubiquiti_be:fa:3a | Ubiquiti_c4:67:fd | Probe Request, SN=256, |
| Ubiquiti_c4:67:fd | Ubiquiti_be:fa:3a | Probe Response, SN=275 |
| Ubiquiti_be:fa:3a | Ubiquiti_c4:67:fd | Authentication, SN=257 |
| Ubiquiti_c4:67:fd | Ubiquiti_be:fa:3a | Authentication, SN=275 |
| Ubiquiti_be:fa:3a | Ubiquiti_c4:67:fd | Association Request, S |
| Ubiquiti_c4:67:fd | Ubiquiti_be:fa:3a | Association Response, |
| Ubiquiti_be:fa:3a | Ubiquiti_c4:67:fd | Key (Message 2 of 4) |
| Ubiquiti_c4:67:fd | Ubiquiti_be:fa:3a | Key (Message 3 of 4) |
| Ubiquiti_be:fa:3a | Ubiquiti_c4:67:fd | Key (Message 4 of 4) |

Left-side group brackets: **Broadcast & Probing** (rows 1-4), **Open System Auth. and Assoc** (rows 5-8), **4-Way Handshake** (rows 9-11). (The Info column is cut off at the table's right edge.)

A right-side bracket spans the whole table, labelled **What we expect from WIFI**.

## Slide 48

###### 802.11 BASICS - A MANAGEMENT FRAME

Hand-drawn diagram.

Left - a box labelled **Management Frame** containing, top to bottom:

- Header
- Body
  - Fixed Params
  - Tagged Params
- Trailer

An arrow runs from **Tagged Params** to the right-hand side:

**Information Elements** (underlined)

TLV

| Tag | Length | Value |

- 0 --> SSID
- 1 --> Supported Rates
- 3 --> Channel
- ...
- 221 --> Vendor Specific

## Slide 49

###### 802.11 BASICS - A MANAGEMENT FRAME

Hand-drawn diagram.

Left - a box labelled **Management Frame** containing, top to bottom:

- Header
- Body
  - Fixed Params
  - Tagged Params
- Trailer

An arrow runs from **Tagged Params** to the right-hand side:

**Information Elements** (underlined)

TLV

| Tag | Length | Value |

- 0 --> SSID
- 1 --> Supported Rates
- 3 --> Channel
- ...
- 221 --> Vendor Specific

The **221 --> Vendor Specific** entry is highlighted with a red box.

## Slide 50

###### 802.11 BASICS - THE ANATOMY OF A VENDOR IE

The workhorse of the proprietary protocols

- Other devices ignore the unknown OUI
- No new spectrum
- No new frames, just riding on top of management

Hand-drawn byte-field diagram:

| IE Tag | Len | OUI | OUI Type | Vendor Data |
|--------|-----|-----|----------|-------------|
| 0xDD | 1 Byte | 3 Bytes | 1 Byte | len - Bytes |

## Slide 51

###### 802.11 BASICS - A FRAME BODY

Left panel:

```text
v IEEE 802.11 Wireless Management
  > Fixed parameters (12 bytes)
  v Tagged parameters (230 bytes)
    > Tag: Supported Rates 6(B), 9, 12(B), 18, 24(B
    > Tag: DS Parameter set: Current Channel: 36
    > Tag: Traffic Indication Map (TIM): DTIM 0 of
    > Tag: Power Constraint: 3
    > Tag: RSN Information
    > Tag: HT Capabilities
    > Tag: HT Operation
    > Tag: Extended Capabilities (8 octets)
    > Tag: VHT Capabilities
    > Tag: VHT Operation
    > Tag: Tx Power Envelope
    > Tag: Vendor Specific: Microsoft Corp.: WMM/WM
    > Tag: Vendor Specific: Atheros Communications,
    > Tag: Vendor Specific: Ubiquiti Inc
```

Top-right panel:

```text
v IEEE 802.11 Wireless Management
  v Fixed parameters (12 bytes)
    Timestamp: 377848832080
    Beacon Interval: 0.102400 [Seconds]
    > Capabilities Information: 0x1831
  v Tagged parameters (334 bytes)
    v Tag: SSID parameter set: Wildcard SSID
      Tag Number: SSID parameter set (0)
      Tag length: 0
      SSID: <MISSING>
    > Tag: Supported Rates 6(B), 9, 12(B), 18, 24
    v Tag: DS Parameter set: Current Channel: 36
      Tag Number: DS Parameter set (3)
      Tag length: 1
      Current Channel: 36
```

Bottom-right panel:

```text
v Tag: Vendor Specific: MediaTek Inc
    Tag Number: Vendor Specific (221)
    Tag length: 7
    OUI: 00:0c:43 (MediaTek Inc)
    Vendor Specific OUI Type: 0
    Vendor Specific Data: 000000
v Tag: Vendor Specific: MediaTek Inc
    Tag Number: Vendor Specific (221)
    Tag length: 33
    OUI: 00:0c:e7 (MediaTek Inc)
    Vendor Specific OUI Type: 0
    Vendor Specific Data: 000000bf0c
v Tag: Vendor Specific: Wi-Fi Allianc
    Tag Number: Vendor Specific (221)
    Tag length: 7
    OUI: 50:6f:9a (Wi-Fi Alliance)
    Vendor Specific OUI Type: 22
    > MBO/OCE attribute: 010100 (MBO AF
```

The SSID parameter block (top-right) and the second MediaTek block (bottom-right) are each outlined in red; "Tagged parameters (230 bytes)" (left) and the first MediaTek tag (bottom-right) are highlighted. Several lines are cut off at each panel's right edge.

## Slide 52

###### MORE ABOUT INFORMATION ELEMENTS

*Black-and-white photo of a dense tangle of overhead cables, overlaid with the title* **802.11 Protocol Chaos** *and credited* Andrés Blanco / @6e726d.

If you are interested  in Vendor IE check @6e726d deck

## Slide 53

###### TDMA IMPLEMENTATION OVER IEEE 802.11

Vendor Specific Information Element with AirMAX enabled

- OUI: 00:0C:42 -> Device name

*(Top right: a Batman "I'LL SEE" reaction meme.)*

Wireshark capture. Selected packet in the list:

```text
397 Beacon frame, SN=1515, FN=0, Flags=........C, BI=100, SSID="Comodoro"
```

Packet detail tree:

```text
> Tag: Vendor Specific: Microsoft Corp.: WMM/WME: Parameter Element
> Tag: Vendor Specific: Epigram, Inc.: HT Capabilities (802.11n D1.10)
> Tag: Vendor Specific: Epigram, Inc.: HT Additional Capabilities (802.11n
> Tag: Vendor Specific: Atheros Communications, Inc.: Advanced Capability
> Tag: Vendor Specific: Atheros Communications, Inc.: Unknown
> Tag: Vendor Specific: Ubiquiti Inc
v Tag: Vendor Specific: Routerboard.com
    Tag Number: Vendor Specific (221)
    Tag length: 38
    OUI: 00:0c:42 (Routerboard.com)
    Vendor Specific OUI Type: 0
    Unknown: 0000
    v Sub IE (T/L: 1/30)
        Subtype: 1
        Sublength: 30
        Subdata: 000000001f660902ff0f4c6176616c6c65202d2050790000000000000000
        Subtype 1 Prefix: 000000001f660902ff0f
        Subtype 1 Data: Lavalle – Py
```

Hex view (offsets and bytes; the ASCII decode column at right is largely cropped at the slide edge):

```text
0050  64 6f 72 6f 01 08 8c 12   98 24 b0 48 60 6c 03 01
0060  a5 05 04 00 01 00 00 07   06 42 5a 20 95 11 1e 20
0070  01 03 30 14 01 00 00 0f   ac 04 01 00 00 0f ac 04
0080  01 00 00 0f ac 02 00 00   2d 1a ad 01 03 ff ff 00
0090  00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
00a0  00 00 00 00 3d 16 a5 08   00 00 00 00 00 00 00 00
00b0  00 00 00 00 00 00 00 00   00 00 00 00 dd 18 00 50
00c0  f2 02 01 01 85 00 03 a4   00 00 27 a4 00 00 42 43
00d0  5e 00 62 32 2f 00 dd 1e   00 90 4c 33 ad 01 03 ff
00e0  ff 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
00f0  00 00 00 00 00 00 dd 1a   00 90 4c 34 a5 08 00 00
0100  00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
0110  00 00 dd 09 00 03 7f 01   01 00 00 ff 7f dd 0a 00
0120  03 7f 04 01 00 02 00 0a   00 dd 0e 00 15 6d 00 00
0130  00 01 02 b5 e6 02 02 02   00 dd 26 00 0c 42 00 00
0140  00 01 1e 00 00 00 00 1f   66 09 02 ff 0f 4c 61 76
0150  61 6c 6c 65 20 2d 20 50   79 00 00 00 00 00 00 00
0160  00 dd 26 00 15 6d ff ff   ff 4b 05 cc 83 d8 2e be
0170  20 5e 8d a4 cf e2 d3 dc   7f dc 97 0c 69 81 eb 61
0180  a0 da 44 93 99 71 56 1b   bc 3a 4b 6e 66
```

The bytes at 0x14d–0x158 (`4c 61 76 61 6c 6c 65 20 2d 20 50 79` = "Lavalle - Py") are selected/highlighted, and the corresponding ASCII "Lavalle – Py" is boxed in red in the decode column.

## Slide 54

###### RECAP - EXTRA INFORMATION

```text
XW.v6.3.22# iwlist ath0 scan
ath0      Scan completed :
          Cell 01 - Address: 78:8A:20:A2:42:97
                    ESSID:"ubnt"
                    Mode:Master
                    Frequency:5.185 GHz (Channel 37)
                    Quality=57/94  Signal level=-39 dBm  Noise level=-103 dBm
                    Encryption key:off
                    Bit Rates:54 Mb/s
                    Extra:ubnt=0e4e616e6f4265616d204d352031360000
                    Extra:ieee_mode=802.11n
          Cell 02 - Address: 1C:6A:1B:C4:67:FD
                    ESSID:""
                    Mode:Master
                    Frequency:5.18 GHz (Channel 36)
                    Quality=56/94  Signal level=-40 dBm  Noise level=-103 dBm
                    Encryption key:off
                    Bit Rates:54 Mb/s
                    Extra:ubnt=05
                    Extra:ieee_mode=802.11ac
```

A red annotation **NanoBeam M5 16** with an arrow points to the underlined tail of `Extra:ubnt=0e4e616e6f4265616d204d352031360000` (which decodes to "NanoBeam M5 16").

## Slide 55

###### AIRMAX IE

Hand-drawn diagram of three Vendor IE frame layouts (each ending in a torn/continued edge):

| Group | Tag | Len | OUI | OUI-type | Data |
|-------|-----|-----|----------|----------|------|
| M | 0xDD | Len | 00:0C:42 | … | Device Name |
| M | 0xDD | Len | 00:15:6D | FF:FF:FF | Payload |
| AC | 0xDD | Len | 00:27:22 | FF:FF:FF | Payload |

Field labels below the diagram: the 00:xx:xx column is **OUI**, the FF:FF:FF column is **OUI-type**.

## Slide 56

###### INFORMATION ELEMENTS DATA

```text
> Tag: Tx Power Envelope
> Tag: Vendor Specific: Microsoft Corp.: WMM/WME: Parameter Element
> Tag: Vendor Specific: Atheros Communications, Inc.: Advanced Capability
v Tag: Vendor Specific: Ubiquiti Inc
    Tag Number: Vendor Specific (221)
    Tag length: 58
    OUI: 00:27:22 (Ubiquiti Inc)
    Vendor Specific OUI Type: 255
    Vendor Specific Data: ffff020100306cb4acbf04471336476fe1494da40c5a1f2bd59d79
```

"Tag: Vendor Specific: Ubiquiti Inc" is highlighted; the Vendor Specific Data value is cut off at the panel's right edge.

## Slide 57

###### INFORMATION ELEMENTS DATA

```text
> Tag: Tx Power Envelope
> Tag: Vendor Specific: Microsoft Corp.: WMM/WME: Parameter Element
> Tag: Vendor Specific: Atheros Communications, Inc.: Advanced Capability
v Tag: Vendor Specific: Ubiquiti Inc
    Tag Number: Vendor Specific (221)
    Tag length: 58
    OUI: 00:27:22 (Ubiquiti Inc)
    Vendor Specific OUI Type: 255
    Vendor Specific Data: ffff020100306cb4acbf04471336476fe1494da40c5a1f2bd59d79
```

The Vendor Specific Data value is boxed in red, with an arrow pointing down to the hex view:

```text
00f0  ff 7f dd 3a 00 27 22 ff   ff ff 02 01 00 30 6c b4   ···:·'"· ·····0l·
0100  ac bf 04 47 13 36 47 6f   e1 49 4d a4 0c 5a 1f 2b   ···G·6Go ·IM··Z·+
0110  d5 9d 79 93 6d 5b b4 6f   b9 a2 a2 9c 66 51 58 05   ··y·m[·o ····fQX·
0120  ec 42 01 46 d3 49 4f c0   66 a4 5a 20 46 59 12 5f   ·B·F·IO· f·Z FY·_
0130  23 04                                               #·
```

## Slide 58

###### INFORMATION ELEMENTS DATA

```text
> Tag: Tx Power Envelope
> Tag: Vendor Specific: Microsoft Corp.: WMM/WME: Parameter Element
> Tag: Vendor Specific: Atheros Communications, Inc.: Advanced Capability
v Tag: Vendor Specific: Ubiquiti Inc
    Tag Number: Vendor Specific (221)
    Tag length: 58
    OUI: 00:27:22 (Ubiquiti Inc)
    Vendor Specific OUI Type: 255
    Vendor Specific Data: ffff020100306cb4acbf04471336476fe1494da40c5a1f2bd59d79
```

The Vendor Specific Data value is boxed in red, with an arrow pointing down to the hex view:

```text
00f0  ff 7f dd 3a 00 27 22 ff   ff ff 02 01 00 30 6c b4   ···:·'"· ·····0l·
0100  ac bf 04 47 13 36 47 6f   e1 49 4d a4 0c 5a 1f 2b   ···G·6Go ·IM··Z·+
0110  d5 9d 79 93 6d 5b b4 6f   b9 a2 a2 9c 66 51 58 05   ··y·m[·o ····fQX·
0120  ec 42 01 46 d3 49 4f c0   66 a4 5a 20 46 59 12 5f   ·B·F·IO· f·Z FY·_
0130  23 04                                               #·
```

Encrypted?

## Slide 59

# REVERSING TIME

59

## Slide 60

###### WE STARTED REVERSE ENGINEERING

A dense directed call graph (Ghidra/graphviz style) of the reverse-engineered driver modules.

Module nodes: **asf**, **ubnthal**, **adf**, **urd**, **ar724x-eth**, **ath_hal**, **ath_spectral**, **ath_dev**, **ath_rate_atheros**, **ath_dfs_prescan**, **ath_dfs**, **umac**, **ath_pktlog**, **ubnt_poll_host**, **rssi-leds**.

Edge labels (imported/exported symbol clusters) along the arrows:

- afree_private / amalloc_private
- asf_print_category_private
- afree_private / amalloc_private
- gpio_line_config / gpio_line_set
- afree_private / amalloc_private
- afree_private / amalloc_private / asf_print_ctrl_register_private / asf_print_ctrl_unregister_private / asf_print_mask_set / ... (+1 more)
- ath_dfs_prescan_register / ath_dfs_prescan_unregister
- board_identify / ubnthal_get_radio_cap
- ath_process_spectraldata / is_spectral_phyerr / spectral_attach / spectral_check_hw_capability / spectral_control / ... (+7 more)
- ath_hook_host_register / ath_kickout_node_notify / ieee80211_find_node / ieee80211_free_node / ieee80211_indicate_node_assoc / ... (+5 more)
- ath_dfs_module_locked / ath_dfs_register / ath_dfs_unregister
- g_pktlog_funcs
- spectral_attach / spectral_check_hw_capability / spectral_control / spectral_detach / spectral_process_phyerr / ... (+1 more)
- ACBEMinfree / ACBKMinfree / ACVIMinfree / ACVOMinfree / CABMinfree / ... (+20 more)
- afree_private / amalloc_private / asf_amem_create / asf_amem_destroy / asf_amem_setup / ... (+5 more)
- afree_private / amalloc_private
- gpio_int_disable / gpio_int_enable / gpio_int_init / gpio_int_uninit
- board_identify / gpio_line_config / gpio_line_get / gpio_line_set / ubnthal_get_eeprom_data / ... (+11 more)
- ath_get_tx_chainmask / ath_rate_attach / ath_rate_create_vap / ath_rate_detach / ath_rate_findrate / ... (+16 more)
- _ath_hal_attach / ath_hal_computetxtime / ath_hal_detach / ath_hal_display_tpctables / ath_hal_enabledANI / ... (+14 more)
- ubnt_eth_phy / ubnthal_get_eth_port_count
- ubnthal_get_radio_cap
- ath_hal_get_device_info
- ath_hal_probe
- adf_os_mem_zero_outline
- adf_os_mem_alloc_outline / adf_os_mem_free_outline / adf_os_spin_lock_bh_outline / adf_os_spin_unlock_bh_outline
- ath_get_softc
- g_pktlog_funcs
- ieee80211_leds_register / ieee80211_leds_unregister
- urd_alpha2_to_countrycode / urd_find_countrycode / urd_intersect_domains / urt_count_group_countries
- ath_hal_log_ani_callback_register
- board_identify / gpio_led_set / led_blink_in_progress
- urd_alpha2_to_countrycode / urd_find_countrycode / urd_intersect_domains / urt_count_group_countries

## Slide 61

### IMPORTANT KERNEL MODULES

*Diagram: a directed call graph of kernel modules, drawn as boxes ("asf", "ath_hal", "ath_dev", "umac", "ubnt_poll") connected by curved arrows, each arrow labeled with the function names crossing that boundary. Three groups of nodes are circled in red with callouts below them.*

**Nodes:** asf, ath_hal, ath_dev, umac, ubnt_poll

**Callouts (red circles with red arrows pointing down to the labels):**
- ath_hal + ath_dev → "Atheros drivers"
- umac → "MAC drivers / Modified version of Ath9k"
- ubnt_poll → "AirMAX core driver"

**Edges (arrow direction → label / function names):**
- asf → ath_hal: afree_private, amalloc_private
- asf → ath_dev: afree_private, amalloc_private
- asf → umac: afree_private, amalloc_private, asf_amem_setup, asf_amem_destroy, asf_amem_create, ... (+1 more)
- asf → ubnt_poll: afree_private, amalloc_private
- ath_hal → ath_dev: ath_hal_getChanNoise, ath_hal_computetxtime, ath_hal_get_device_info, ath_hal_set_config_param, ath_hal_mhz2ieee, ... (+15 more)
- ath_hal → umac: ath_hal_probe, ath_hal_subVendorID
- ath_hal → ubnt_poll: ath_hal_set_config_param, ath_hal_reg_write, ath_hal_reg_read
- ath_dev → umac: ath_iw_attach, CABMinfree, ACBKMinfree, wbuf_alloc, ath_cancel_timer, ... (+17 more)
- ath_dev → umac: hook_ops, bus_dma_sync_single, ath_register_hook
- ath_dev → ubnt_poll (no label)
- umac → ubnt_poll: ieee80211_set_beacon_rx_vendor_ie_hook, ieee80211_set_assoc_req_tx_vendor_ie_hook, ieee80211_set_scan_hook, ieee80211_chan2mode, ieee80211_beacon_alloc, ... (+20 more)

61

## Slide 62

### HOW ARE THE IEs BUILD

*Hand-drawn flow diagram of two kernel modules:*

**umac.KO** box: incoming arrow labeled `mgmt` → `recv_mgmt(...)` box; `Send_{msg}(...)` box → outgoing arrow labeled `mgmt`.

**Ubnt_poll.KO** box: `recv_mgmt(...)` → `On_[Msg]_rx_Hook()` → `Parse_ie()`; and `Insert_ie()` → `On_[Msg]_rx_Hook()` → `Send_{msg}(...)` (arrows flow back left into umac.KO's `Send_{msg}(...)`).

Two disassembly listing panels below the diagram:

**Left panel (tx):**
```
▾ ubnt_poll_host_on_beacon_tx
   |← 00018a70  jal   ubnt_poll_host_proto_insert_ie
▾ ubnt_poll_host_on_deauth_tx
   |← 00019060  jal   ubnt_poll_host_proto_insert_ie
▾ ubnt_poll_host_on_probe_req_tx
   |← 000190dc  jal   ubnt_poll_host_proto_insert_ie
▾ ubnt_poll_host_on_assoc_req_tx
   |← 0001947c  jal   ubnt_poll_host_proto_insert_ie
▾ ubnt_poll_host_on_assoc_resp_tx
   |← 00019fcc  jal   ubnt_poll_host_proto_insert_ie
```

**Right panel (rx):**
```
▾ ubnt_poll_host_on_beacon_rx
   |← 00018b8c  jal   ubnt_poll_host_proto_parse_ie
▾ ubnt_poll_host_on_deauth_rx
   |← 00018df4  jal   ubnt_poll_host_proto_parse_ie
▾ ubnt_poll_host_on_probe_req_rx
   |← 00019198  jal   ubnt_poll_host_proto_parse_ie
▾ ubnt_poll_host_on_assoc_req_rx
   |← 00019760  jal   ubnt_poll_host_proto_parse_ie
▾ ubnt_poll_host_on_assoc_resp_rx
   |← 0001a0f0  jal   ubnt_poll_host_proto_parse_ie
```

62

## Slide 63

### ENCRYPTION? I DON'T THINK SO

```c
uint8_t* key

key = dst_mac != 0 ? dst_mac : &bcast_mac

void out
hmac_sha1(message: src_mac, msglen: 6, key, keylen: 6, &out)
aes_encrypt_key128(&out, &var_170)
int32_t $s0 = $s0_1 + 0xf

if ($s0_1 s>= 0)
    $s0 = $s0_1

char* out_ie_enc = &out_ie_ptr->enc
int32_t $s2_1 = 0
uint16_t* $s1_1 = &plain_ie.hdr.version

while (true)
    char* $a0_18 = $s1_1

    if ($s2_1 s>= $s0 s>> 4)
        break

    $s1_1 = &$s1_1[8]
    aes_encrypt($a0_18, out_ie_enc, &var_170)
    out_ie_enc = &out_ie_enc[0x10]
    $s2_1 += 1
```

*Hand-drawn diagram (right side):* a box labeled "802.11 MSG" contains three sub-boxes — "SRC Mac", "DST Mac", and "Encrypted Data". Arrows: SRC Mac → SHA 1; DST Mac → SHA 1; SHA 1 → Key; Key → AES-128-ECB; Encrypted Data → AES-128-ECB (long arrow bypassing SHA1/Key); AES-128-ECB → Clear Data.

Validated with **mtscan** by **Konrad Kosmatka**:

- github.com/kkonradpl/mtscan/

63

## Slide 64

### ENCRYPTION? I DON'T THINK SO

**Gaston Aznarez** 11:58

```text
MAC Address: 44:d9:e7:6a:3a:43
AES Key (derived): ff1db564cf91b27557ff9343ed1d4d16 (16)

Decrypting
Encrypted data: ca 44 6d 0e 37 58 6f 21 62 e0 c5 18 27 b5 cf 37 b1 89 af 52 ca 0a c3 3c c2 13 4f 1b 6e 52 2d 76 (32)
[*] Cipher created
Decrypted data: 0f 01 44 d9 e7 6a 3a 43 01 00 00 00 00 00 00 00 0a 82 82 00 00 44 d9 e7 6a 3a 43 00 00 00 00 00

                          |_________   ______|
                              ||
                              \/
                             MAC
```

Parece que funciona je

Epico

Validated with **mtscan** by **Konrad Kosmatka**:

- github.com/kkonradpl/mtscan/

64

## Slide 65

### ENCRYPTION? I DON'T THINK SO

**fedek** 9:42 PM

```text
════ Frame 44 ════
BSSID: fc:ec:da:0c:9e:04
Key MAC: embedded_addr3
Signal: -66 dBm
Seq#: 578
Mode: 0x01
Mode Flags: {'ptp': True, 'ptmp': False, 'mixed1': False, 'mixed2': False, 'mixed3': False}
Radio Name: 'COV-LOREA-AP'
SSID: 'COV-LOREA'
Cipher[0:8]: 75c93c59b41f63b8

Ciphertext (48 bytes):
 0000  75 c9 3c 59 b4 1f 63 b8 ce c7 39 9a ea 72 8d 70   u.<Y..c...9..r.p
 0010  f1 f8 23 e3 9b 79 75 73 9b 7c ab c2 6b 89 1a d8   ..#..yus.|..k...
 0020  df 80 8e 06 b3 9b 3f ed cd ed 8d 2b 14 76 89 81   ......?....+.v..

Plaintext (48 bytes):
 0000  00 08 fc ec da 0c 9e 04 fc ec da 0c 9e 04 00 00   ................
 0010  00 01 00 00 00 00 01 0c 43 4f 56 2d 4c 4f 52 45   ........COV-LORE
 0020  41 2d 41 50 02 09 43 4f 56 2d 4c 4f 52 45 41 00   A-AP..COV-LOREA.
```

*(The last two lines of the plaintext ASCII column, "COV-LORE" / "A-AP..COV-LOREA.", are highlighted with a red box.)*

65

## Slide 66

### IT'S DECRYPTED BUT... WHAT IS THE STRUCTURE?

```text
Plaintext (48 bytes):
 0000  00 08 fc ec da 0c 9e 04 fc ec da 0c 9e 04 00 00   ................
 0010  00 01 00 00 00 00 01 0c 43 4f 56 2d 4c 4f 52 45   ........COV-LORE
 0020  41 2d 41 50 02 09 43 4f 56 2d 4c 4f 52 45 41 00   A-AP..COV-LOREA.
```

66

## Slide 67

### AIRMAX M FRAMES

*Hand-drawn diagram of the AirMAX M frame structure.*

Row 1 — "Plaintext" bracket over `00:15:6D` then `FF:FF:FF`; "AES-128-ECB" bracket over `version | type | mac | ...`

```
type ─┬─→ 1  Beacon
      ├─→ 2  Association Req
      └─→ 3  Association Res
```

Row 2 — "Plaintext" bracket over `00:0C:42` then `...` then `Device Name` then `...`

↓

`01 | len | Data`

67

## Slide 68

### AIRMAX AC FRAMES

*Hand-drawn diagram of the AirMAX AC frame structure.*

"Plaintext" bracket over `00:27:22 | FF:FF:FF | Header`, next to "AES-128-ECB" bracket over `Encrypted Payload`.

`Header` ↓ expands to: `flags | type | len`

`Encrypted Payload` ↓ expands to: `version | SRS mac | ...`, bracketed below as "Encrypted Header"

68

## Slide 69

### AIRMAX AC FRAMES

*Hand-drawn diagrams of frame layouts by type.*

**Type: 1 Beacon**

| mac | Cap.Flags | mode | Radioname TLV[1] | SSID TLV[2] |
|---|---|---|---|---|

**Type: 2 Assoc Req**

| Chainmask | Cap.Flags | ... | Radioname TLV[1] | SSID TLV[2] | ... | rssi | FW Name TLV[3] | tx Power |
|---|---|---|---|---|---|---|---|---|

**Type: 3 Assoc Res**

| ... | Rssi | Firmware Name TLV[3] | TX Power |
|---|---|---|---|

**Type: 4 Probe Req**

| Empty |
|---|

**Type: 12 Deauth**

| nonce | Token |
|---|---|

69

## Slide 70

###### 802.11 & AIRMAX - RECAP

###### 802.11

- Frames

- How a connection looks like

- Management Frames anatomy

- Information Elements

###### AirMAX

- Kernel modules

- ~~Encryption~~ Obfuscation

- AirMAX M & AC

- Frames

70

## Slide 71

### **RECON TIME**

*Photo of the "Detective Pikachu" character wearing a deerstalker hat and holding a magnifying glass up to one eye, with a crystal ball on a stand in the foreground.*

71

## Slide 72

### **RECON TIME**

### **GOTTA CATCH 'EM ALL**

*Same photo of "Detective Pikachu" with a magnifying glass, now with a second caption added in the lower right.*

72

## Slide 73

### FINDING AIRMAX NETWORKS (in-the-wild)

*Left: a satellite/wardriving map of a Buenos Aires neighborhood (Costanera Sur / Monserrat area), covered with dozens of overlapping Wi-Fi network name (SSID) labels and pins that are largely illegible due to overlap [illegible]. A few clearly legible place labels are visible: "MUNTREF Museo de la inmigración", "Teatro Colón", "Luna Park", "Grupo Paolini", "Costanera Sur", "MONSERRAT", "Estatua de Mafalda", "TeleCentro Wifi", "Personal Wifi Zone".*

*Right: a photograph of a person sitting in the passenger seat of a car, working on a laptop showing a terminal window, with a Wi-Fi antenna/adapter mounted on the dashboard and cables running to it. They are wearing a t-shirt with a patch reading "EXCESO DE IA".*

73

## Slide 74

### FINDING AIRMAX NETWORKS (in-the-wild)

*Screenshot of a Leaflet/OpenStreetMap web map of Buenos Aires, with a string of green pins tracing a route down through Recoleta, San Nicolás, Puerto Madero, and San Telmo toward La Boca. Neighborhood labels visible on the map include: Colegiales, Palermo, Chacarita (Cementerio de la Chacarita), Villa Crespo, Recoleta, Almagro, Balvanera, San Nicolás, Buenos Aires, Puerto Madero, Comuna 5, Caballito, San Cristóbal, Constitución, San Telmo, Flores, Boedo, Parque Chacabuco, Parque Patricios, La Boca, Autopista 25 de Mayo, AV1-Sur.*

Legend: 🟢 Access Point  🔵 Station  🟣 Unknown Role

Bottom-right attribution: "Leaflet | © OpenStreetMap contributors"

74

## Slide 75

### FINDING AIRMAX NETWORKS (in-the-wild)

*Screenshot of a map (Retiro/Plaza San Martín area of Buenos Aires) with several green access-point pins, one of which has an open info popup:*

**PTMP-CerritoYcordoba** `AP` ✕

- **BSSID:** 78:8a:20:6c:bd:a9
- **Radio:** AP PTMP-CerritoYcordoba
- **Signal:** -86.4 dBm
- **Location:** Cerrito, Buenos Aires, AR
- **Coords:** -34.598949, -58.381916

75

## Slide 76

###### FINDING AIRMAX NETWORKS (in-the-wild)

*Screenshot of the "AirMAX Survey" Network Analysis Tool (file `remoe_wireshark.pcapng`).*

Summary cards: **16** Networks · **785** AirMAX Frames · **773** Decrypted · **298156** Total Packets · **754** Access Points

**Discovered Networks (16)**

| SSID | BSSID | Radio Name | Device | Firmware | Type | Mode | Role | CH | Freq | Signal | Noise | SNR | AMQ | AMC |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gerencia_5GHz | 48:a9:8a:fa:a3:7d | - | - | - | MIKROTIK | - | AP | - | 3686 MHz | -80.7 | - | - | - | - |
| Aspen | ff:ff:ff:ff:ff:ff | BeamM5 TUC 54 | - | - | MIKROTIK | - | STA | - | 2406 MHz | -77.3 | - | - | - | - |
| (Hidden) | 00:15:6d:53:82:64 | 00156D538264 | - | - | MIKROTIK | - | AP | - | 2406 MHz | -79.2 | - | - | - | - |
| ubnt | 24:5a:4c:cc:f5:09 | CerritoDatos | - | - | AC_EMBEDDED | PTP | AP | - | 2406 MHz | -84.0 | - | - | - | - |
| PTMP-CerritoYcordoba | 78:8a:20:6c:bd:a9 | AP PTMP-CerritoYcordoba | - | - | AC_EMBEDDED | MIXED1 | AP | - | - | -63.0 | - | - | - | - |
| (Hidden) | ff:ff:ff:ff:ff:ff | - | - | - | AC_EMBEDDED | - | STA | - | - | -72.1 | - | - | - | - |
| Norte. | 74:83:c2:62:4d:2b | Norte | - | - | AC_EMBEDDED | - | AP | - | - | -77.7 | - | - | - | - |
| (Hidden) | 74:83:c2:62:f1:ae | - | - | - | AC_EMBEDDED | - | STA | - | - | -78.2 | - | - | - | - |
| CLMB | 74:ac:b9:8e:7a:ef | Oficina | - | - | AC_EMBEDDED | - | AP | - | - | -82.3 | - | - | - | - |
| AP CERRITO Y TUCUMAN | f0:9f:c2:ec:37:20 | AP CERRITO Y TUCUMAN | - | - | AC_EMBEDDED | MIXED1 | AP | - | - | -82.5 | - | - | - | - |
| ARMENON | d8:44:89:27:f0:7c | CPE510 | - | - | MIKROTIK | - | AP | - | - | -82.7 | - | - | - | - |
| Estrategias_2G | 18:fd:74:5b:f2:27 | - | - | - | MIKROTIK | - | AP | - | - | -82.7 | - | - | - | - |
| Comodoro | 04:18:d6:ec:22:06 | Lavalle - Py | - | - | M_ENCRYPTED | PTMP | AP | - | - | -85.1 | - | - | 7% | 6% |
| Espinosa#1 | 18:e8:29:78:1b:41 | NET-RADIO-AP-ROC17AC-Espinosa#1 | - | - | AC_EMBEDDED | - | AP | - | - | -85.1 | - | - | - | - |

76

## Slide 77

###### LET’S DO SOME TOOLS FOR THE COMMUNITY

###### Tools

- WireMAX - Wireshark dissector
- PyrMAX - Python package
- Web Platform

*Bottom-left: screenshot of the "AirMAX Survey" web platform (`remoe_wireshark.pcapng`, with Upload PCAP / Load Demo buttons) showing six stat cards — 16 Networks, 785 AirMAX Frames, 773 Decrypted, 298156 Total Packets, 754 Access Points, 31 Stations — above the Discovered Networks table.*

*Right: a Wireshark window (`ubnt_ac_multiple_reconnections.pcapng`) with the WireMAX dissector decoding an AirMAX AC frame:*

```text
No.    Time        Source             Destination        Protocol
1236   17.780235   Ubiquiti_c4:67:fd  Ubiquiti_be:fa:3a  802.11
1237   17.781692   Ubiquiti_be:fa:3a  Ubiquiti_c4:67:fd  802.11

v AirMAX AC (Vendor Specific IE)
    OUI: 002722
    OUI Type: ffffff
  > Flags: 0x02
    Message Type: Assoc Req (2)
    Encrypted Length: 96
    Ciphertext: 10bde1f8661daf7a9ef185d0d19f7fc5de0306334ad67904308160a2e02ead…
  v [Decrypted payload (AES-128-ECB)]
      [AES Key (HMAC-SHA1(dst,src)[:16]): 3f8e721868280c93417170f2a71a568f  (d…
      Version: 9
      Source MAC: Ubiquiti_be:fa:3a (1c:6a:1b:be:fa:3a)
      TX Chainmask: 3
      RX Chainmask: 3
    v Capability Flags: 0x00000041
        .... .... .... .... .... .... .... 0... = chanbw mode: False
        .... .... .... .... .... .... ...0 .... = high density: False
        .... .... .... .... .... .... .1.. .... = auth-deauth capable: True
        .... .... .... .... .... .... 0... .... = 11ax-compat: False
      field_14 [open]: 0x00000000
      Radioname: LiteBeam 5AC
      SSID: FaradayLB
    v TLV: Radioname (1), len 12
        Tag: Radioname (1)
        Length: 12
        Data: 4c6974654265616d20354143
  > TLV: SSID (2), len 9
      field_9c [open]: 0x7729d097
      RSSI (per-chain): 2c2d
      Firmware Name: WA.ar934x.v8.7.22.48486.260227.1
```

*Status bar: Ubiquiti AirMAX (airmax), 106 bytes · Packets: 15097 · Profile: Default*

77

## Slide 78

# HACKER DREAMS WITH OVER-THE-AIR EXPLOITS

78

## Slide 79

# HACKER DREAMS WITH OVER-THE-AIR EXPLOITS

*Full-width screenshot from the video game Watch Dogs: a hooded, masked character holding a phone on a city street (a "Congress Pkwy" sign and a "GREEN APARTMENTS / PRIVATE COUR… STARTING AT $695,900" billboard behind, police cars crashing at right). A loading-screen caption at lower-left reads "Fact #12 — Solving crimes before they hap[pen]".*

79

## Slide 80

# HACKER DREAMS WITH OVER-THE-AIR EXPLOITS

80

## Slide 81

###### WHAT IF I TOLD YOU…

###### Custom protocols sound great until someone reverses them

```c
arg3[0x18] = ie->__offset(0x1e).b
uint32_t $v0_20 = zx.d(ie->__offset(0x1f).b)
uint32_t $s0_4 = $v0_20
arg3[0x19] = $v0_20.b
// Where this size comes from???
memcpy(&key_1, ie + 0x20, $v0_20)
```

81

## Slide 82

###### WHAT IF I TOLD YOU…

###### Custom protocols sound great until someone reverses them

```c
arg3[0x18] = ie->__offset(0x1e).b
uint32_t $v0_20 = zx.d(ie->__offset(0x1f).b)
uint32_t $s0_4 = $v0_20
arg3[0x19] = $v0_20.b
// Where this size comes from???
memcpy(
```

*(the remainder of the `memcpy(...)` line is hidden behind a Slack message popup overlaying the code)*

*Slack popup:*

- **fedek** 11:21 AM — Necesito más memcpy’s
- IMG_7466 ▾ — *[image: a long-haired man resting both hands on his head — reaction meme]*
- 1 reply · Today at 5:27 PM

82

## Slide 83

###### WHAT IF I TOLD YOU…

###### Custom protocols sound great until someone reverses them

```c
arg3[0x18] = ie->__offset(0x1e).b
uint32_t $v0_20 = zx.d(ie->__offset(0x1f).b)
uint32_t $s0_4 = $v0_20
arg3[0x19] = $v0_20.b
// Where this size comes from???
memcpy(
```

*(the remainder of the `memcpy(...)` line is hidden behind a Slack popup)*

*Left Slack popup:*

- **fedek** 11:21 AM — Necesito más memcpy’s
- IMG_7466 ▾ — *[image: a long-haired man resting both hands on his head — reaction meme]*
- 1 reply · Today at 5:27 PM

*Right Slack conversation:*

**Gaston Aznarez** 10:58 AM

```text
Fri Aug 22 21:27:49 UTC 2025
Fri Aug 22 21:27:50 UTC 2025
Fri Aug 22 21:27:51 UTC 2025
Fri Aug 22 21:27:52 UTC 2025
Fri Aug 22 21:27:53 UTC 2025
Fri Aug 22 21:27:54 UTC 2025
Fri Aug 22 21:27:55 UTC 2025
Fri Aug 22 21:27:56 UTC 2025
Fri Aug 22 21:27:57 UTC 2025
Fri Aug 22 21:27:58 UTC 2025
Fri Aug 22 21:27:59 UTC 2025
Fri Aug 22 21:28:00 UTC 2025
Read from remote host 192.168.137.102: Connection reset by peer
Connection to 192.168.137.102 closed.
client_loop: send disconnect: Broken pipe
```

*(the final four lines — from `Fri Aug 22 21:28:00` through `Broken pipe` — are outlined in a red box)*

**fedek** 10:58 AM — 🙄

**Gaston Aznarez** 10:58 AM — sospechoso (844 kB) ▾ — *[image: Futurama's Fry squinting next to Ned Flanders and a dog looking out a window — meme]*

*[↓ Latest messages button]*

83

## Slide 84

DEMO 1

84

## Slide 85

###### THE VULNERABILITIES

**CVEs:**

- CVE-2026-21639
- CVE-2026-21638

**Criticality:**

- Over-The-Air (line of sight)
- Unauthenticated
- RCE
- Kernel Privileges

**CVSS limitations:**

- 8.8 (High) for this adjacent bug (would 9.8 (critical) for LAN bugs)

*Right — two NVD-style "CVE Detail" cards:*

**CVE-2026-21639 Detail — Description**

> A malicious actor in Wi-Fi range of the affected product could leverage a vulnerability in the airMAX Wireless Protocol to achieve a remote code execution (RCE) within the affected product. Affected Products: airMAX AC (Version 8.7.20 and earlier) airMAX M (Version 6.3.22 and earlier) airFiber AF60-XG (Version 1.2.2 and earlier) airFiber AF60 (Version 2.6.7 and earlier) Mitigation: Update your airMAX AC to Version 8.7.21 or later. Update your airMAX M to Version 6.3.24 or later. Update your airFiber AF60-XG to Version 1.2.3 or later. Update your airFiber AF60 to Version 2.6.8 or later.

**CVE-2026-21638 Detail — Description**

> A malicious actor in Wi-Fi range of the affected product could leverage a vulnerability in the airMAX Wireless Protocol to achieve a remote code execution (RCE) within the affected product. Affected Products: UBB-XG (Version 1.2.2 and earlier) UDB-Pro/UDB-Pro-Sector (Version 1.4.1 and earlier) UBB (Version 3.1.5 and earlier) Mitigation: Update your UBB-XG to Version 1.2.3 or later. Update your UDB-Pro/UDB-Pro-Sector to Version 1.4.2 or later. Update your UBB to Version 3.1.7 or later.

Metrics (CVSS Version 4.0 · **CVSS Version 3.x** · CVSS Version 2.0) — *NVD enrichment efforts reference publicly available information to associate vector strings. CVSS information contributed by other sources is also displayed.*

CVSS 3.x Severity and Vector Strings:

- NIST: NVD — Base Score: N/A — NVD assessment not yet provided.
- CNA: HackerOne — Base Score: 8.8 HIGH — Vector: CVSS:3.1/AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H

85

## Slide 86

#### Affected Products

**2.4, 5, 60 GHz**

- airMAX M
- airMAX AC
- airFiber AF60-XG
- airFiber AF60 (60GHz)
- UBB-XG
- UDB-Pro/UDB-Pro-Sector
- UBB

*Right: photo of a rooftop lattice tower carrying many Ubiquiti/airMAX dishes and sector antennas plus a surveillance camera.*

86

## Slide 87

#### Affected Products

**2.4, 5, 60 GHz**

- airMAX M
- airMAX AC
- airFiber AF60-XG
- airFiber AF60 (60GHz)
- UBB-XG
- UDB-Pro/UDB-Pro-Sector
- UBB

*Right: the same rooftop-tower photo, now with red spiky-star markers overlaid on roughly a dozen of the antennas and dishes to flag the affected devices.*

87

## Slide 88

###### THE IMPACT

###### Critical infrastructure:

- Critical infrastructure (OT)

- Government Infrastructure

- Public Safety CCTV

- Civilian and Military use

- And many more!

88

## Slide 89

# BUG BOUNTY

89

## Slide 90

###### BUG BOUNTY TIMELINE

*Top-right: the "hackerone" logo. A left-to-right time-arrow runs along the bottom; a brace over the Dec 1 – Dec 11 span is labelled "Just **10** days for the first patch".*

**Nov 13** — The bug was found

**Dec 1** — The vulnerability was reported

**Dec 8** — CVEs assigned
- CVE-2026-21638
- CVE-2026-21639

**Dec 11** — First patch wave
- AirMAX M

**Dec 17** — Second patch wave
- AF60-HD/XG
- AF60/AF60-LR

**Dec 22** — Third patch wave
- UniFi Device/Building Bridge XG

**Feb 28** — Last patch wave
- AirMAX AC

**Jan 6** — Advisories published

90

## Slide 91

###### BUG BOUNTY PAYMENT

- Top $8000 in LAN Networks

- Top $4000 in Adjacent

They pay more for a LAN Vuln than a Vulnerability that can be exploited from kilometers

**100 km** *(red label with an arrow pointing down into the screenshot below)*

*Screenshot (top right): a CVSS score calculator panel.*
**Attack Vector (AV)**: `Network (N)`  `Adjacent (A)` *(selected, highlighted green)*  `Local (L)`  `Physical (P)`
A tooltip covers part of the panel: "The vulnerable component is bound to the network stack, but the attack is limited at the protocol level to a logically adjacent topology. This can mean an attack must be launched from the same shared physical (e.g., Bluetooth or IEEE 802.11) or logical (e.g., local IP subnet) network, or from within a secure or otherwise limited administrative domain (e.g., MPLS, secure VPN to an administrative network zone)."
**Attack Complexity (AC** *(rest of row hidden behind the tooltip)*: `Low (L)`  `High (H)`
**Privileges Required (P** *(rest of label hidden behind the tooltip)*: `None (N)`  `Low (L)`  `High (H)` *(partly hidden)*

*Screenshot (bottom left): a Ubiquiti AirMax link-planner tool showing a point-to-point link between two towers.*
- Capacity: **149 Mbps**
- RF Noise: Noise Free
- Link distance: **100.16 km** *(boxed in red)*
- Product (both ends): LiteBeam ...
- Height: 239.38 m (left tower) / 241.34 m (right tower)
- Expected Signal: **-75 dBm**, 8X
- "LIDAR data is not available in this area."
- © 2026 Ubiquiti Inc.

*Box (bottom right):* **Payment Limits:**
Limits will be applied based on Attack Vector rules:
- Limit 1 (Physical) = 1,000
- Limit 2 (Local)= 2,500
- Limit 3 (Adjacent)= 4,000 *(boxed in red)*
- Limit 4 (LAN Side) = 8,000 *(boxed in red)*
- Limit 5 (WAN Side) = 25,000
- Limit 6 (Ubiquiti Cloud) = 30,000

91

## Slide 92

###### BUG BOUNTY PAYMENT

- Top $8000 in LAN Networks

- Top $4000 in Adjacent

They pay more for a LAN Vuln than a Vulnerability that can be exploited from kilometers

*Chart (right): a line graph, y-axis marked 0, 840, 1.7k, 2.5k, 3.4k, 4.2k and x-axis marked 1 through 10, plotting an exponential curve of bounty value against CVSS score, with labeled points 148 (x=7), 444 (x=8), 1,333 (x=9), and* **f(10) = 4000** *(x=10).*

**Decrease Bounty Drivers:**
Privileges Required
High (Admin access, other than view/read-only access) = Base Score / 6
High (View/Read-only admin access) = Base Score / 4
Low (User without admin permissions) = Base Score / 2

User Interaction:
Required = Base Score / 4

**Rewarding Formula**

Base Formula: (3^(x,x-1))*(AV/(3^9))

Where "x,x" is the CVSS score and maximum bounty is AV limit USD

92

## Slide 93

###### BUG BOUNTY PAYMENT

- Top $8000 in LAN Networks

- Top $4000 in Adjacent

They pay more for a LAN Vuln than a Vulnerability that can be exploited from kilometers

*Chart (right): the same exponential bounty-vs-CVSS-score graph as the previous build (y-axis 0/840/1.7k/2.5k/3.4k/4.2k, x-axis 1-10, points 148/444/1,333 and* **f(10) = 4000** *), now with a meme photo pasted over the middle of it: a close-up of a bearded man's face against a blurred, warmly-lit background, overlaid with white handwritten-style mathematical fragments (Σ, cos, a square-root expression, "3x2", "(A + η)²+ κ²", "and", a fraction resembling 4K(1+K)/PSF, and other equation scraps).*

**Decrease Bounty Drivers:**
Privileges Required
High (Admin access, other than view/read-only access) = Base Score / 6
High (View/Read-only admin access) = Base Score / 4
Low (User without admin permissions) = Base Score / 2

User Interaction:
Required = Base Score / 4

**Rewarding Formula**

Base Formula: (3^(x,x-1))*(AV/(3^9))

Where "x,x" is the CVSS score and maximum bounty is AV limit USD

93

## Slide 94

###### BUG BOUNTY PAYMENT

#### 5 GHz Wi-Fi DX record – Denmark logged in Poland @ 745 km

**ENGLISH**  **TROPO**  **WI-FI DX**  / 2020-08-15 / Przez Konrad / Jeden komentarz

A remarkable tropospheric ducting occurred on **August 11 and 12, 2020** between **Poland**, **Sweden** and **Denmark**. The propagation forecasts, which use color hue to scale their intensity, featured red shades over the Baltic Sea. Such a propagation strength is very rare, if ever seen on a forecast for this area. I was looking forward for something extraordinary, especially on the microwave bands. My stationary Wi-Fi DXing setup has been damaged three months ago. I could not miss such an opening, so a DX-pedition was the only option. In the evening of August 11 I made an opportunistic decision to visit the **Dylewska Góra** in north-eastern Poland. A few hours later, I was standing there with an antenna inside a lookout tower.

*Photo: a nighttime shot from beneath a wooden shelter roof, looking out over a dusky blue sky and distant city lights, with a white parabolic dish antenna (its feed lit blue) in the foreground.*

94

## Slide 95

###### BUG BOUNTY PAYMENT

The long-range tropospheric ducting propagation faded away at **7 UTC** and I left the Dylewska Góra after **7 hours** of continuous Wi-Fi DXing. I logged **4 networks** via **transbaltic paths**.

*Map: a road-map view of the southern Baltic Sea with four purple Wi-Fi-antenna icons plotted over Denmark/Sweden — near Vendsyssel/Aalborg, near Odense (labeled "Denmark"), near Malmö, and one between Malmö and the coast — each linked by a red line converging on a radio-tower icon on the Polish coast near Olsztyn. Background place labels visible on the map: Gothenburg, Jönköping, Gotland, Aarhus, Copenhagen, Sjælland, Klaipėda, Kaliningrad/Калининград, Riga, Jūrmala, Šiauliai, Lithuania, Kaunas, Grodno/Гродно, Białystok, Kiel, Rostock, Lübeck, Hamburg, Bremen, Szczecin, Gdynia, Gdańsk, Bydgoszcz, Olsztyn, Poland.*

The table below contains the farthest identified networks (≥ **350 km**) received on August 12, 2020.

https://radiodx.pl/2020/08/5ghz-wifi-dx-record-denmark-logged-in-poland-745-km/

95

## Slide 96

###### HOW "ADJACENT" WORKS IN PRACTICE

*Photo: two men standing indoors in front of a wall-mounted black flag printed with white icons (a running figure, a heart, a cloud). The one on the left, in an olive quilted jacket, holds a small circuit board wired with red/black clip leads to a black battery pack; the one on the right, in a dark puffer jacket, holds a round beige speaker-like device. Their devices are joined by a long yellow cable coiled on the floor between them.*

96

## Slide 97

###### HOW "ADJACENT" WORKS IN PRACTICE

*Photo: a close-up render of Solid Snake (from the Metal Gear Solid video game series) wearing a headband, looking toward the camera against a foggy grey background.*

97

## Slide 98

###### POC FROM KILOMETERS AWAY

- Like master snake told us: When in danger, use a cardboard box

*Screenshot: a video-game scene (Metal Gear Solid V) of a plain cardboard box sitting alone in a dusty, rocky desert landscape, with small HUD item-select icons in the bottom-left and bottom-right corners.*

98

## Slide 99

###### POC FROM KILOMETERS AWAY

*Photo: two men on a sunny city-street corner (Buenos Aires), trees and traffic behind them. The one with long hair holds a mate gourd, drinking through a metal straw while looking down at a small open cardboard box; the other looks down into the box.*

99

## Slide 100

###### THE PROOF OF CONCEPT

*Photo: looking down into an open cardboard box of jumbled electronics — a white parabolic antenna feed, a black battery with a red alligator clip, a blue step-down converter board with a red seven-segment display reading roughly "921", and a small screen propped up showing dense terminal/boot-log text [illegible, photographed at an angle], plus coiled white and yellow cables including an Ethernet cable.*

100

## Slide 101

###### POC FROM KILOMETERS AWAY

*Photo: a selfie of three men on a tree-lined city street (Buenos Aires), parked cars, a taxi, and a passing cyclist behind them. The man on the right holds an open cardboard box; a mate gourd and thermos are tucked in the crook of the middle man's arm.*

101

## Slide 102

###### POC FROM KILOMETERS AWAY

*Top right: clip-art icon of a yellow RS-232-style serial connector with a Bluetooth logo overlaid on it.*

*Screenshot: an Android "Terminal" (Bluetooth serial console) app, showing a boot log, with quick-command buttons M1-M6 and a text input field below.*

```text
ell (ash)
16:05:04.153
16:05:04.385
16:05:04.440
16:05:04.440
16:05:04.478   _______              ________    _
16:05:04.478  |      |.-----.-----.-----.| | | |.----.| |_
16:05:04.478  |   -  || _  | -__|     || | | ||  _|| _|
16:05:04.478  |______||  __|_____|__|__||________||__| |____|
16:05:04.478         |__| W I R E L E S S   F R E E D O M
16:05:04.503  --------------------------------------------------
16:05:04.503   OpenWrt 24.10.4, r28959-29397011cc
16:05:04.503  --------------------------------------------------
16:05:04.653  root@OpenWrt:~#
16:05:04.653  root@OpenWrt:~#
16:05:04.711  root@OpenWrt:~# [   72.890166] ath10k_pci 0000:00:0
0.0: set-coverage-class, phyclk: 88  value: 0
16:05:06.338
16:05:06.391
16:05:06.391  root@OpenWrt:~#
16:05:06.391  root@OpenWrt:~# 16:05:06.489
16:05:06.542
16:05:06.542  root@OpenWrt:~#
16:05:06.542  root@OpenWrt:~#
```

*Photo: a green Ubiquiti AirMax radio PCB (silkscreened "ubiquiti") on a wood table, connected to a white antenna horn/feed on the left and a yellow Ethernet cable on the right; chips on the board are labeled including a Winbond flash chip and one marked "FPE LY24102SN". A small add-on daughterboard wired into the board is highlighted with a red circle near the top right, and a red rectangle highlights a separate component near the middle of the board.*

102

## Slide 103

###### POC FROM KILOMETERS AWAY

- We setup a vulnerable antenna in a cardboard box

- We setup an antenna in the building sending the exploit

- We started walking

*Photo collage:*
- A white Ubiquiti dish antenna mounted on a rusty pole against a city skyline, overlooking a wide avenue.
- A cropped close-up of a building façade with a red rectangle highlighting a small dark object mounted high on the wall near a balcony.
- Street-level photos of a Buenos Aires avenue (trees, parked cars including a taxi, a mural of a woman's face on a building) and a wide intersection with a green bike lane.
- Two people (a man and a woman) on a balcony/terrace opening a cardboard box and looking inside at wired electronics.
- A tilted photo of a phone screen showing green/blue terminal log text, lit by lens glare, with part of it boxed in red; legible fragments include timestamps (19.895000, 19.930000, 19.963000, 19.970000, 19.975000, 19.984000, 19.992000, 20.916000, 21.020000, 28.486000) and the lines `init br0`, `'FARADAY PoC e[xec]`, `bro: port 2(ath0)`, and `Please press Enter to activate t[his console]` [partially illegible — angled photo with lens glare].
- A street map of Buenos Aires (Recoleta/Tribunales area) with a straight measured line and a "Measure distance" callout reading: "Click on the map to add to your path" / "Total distance: 1.50 km (4,913.53 ft)". Visible labels: Palladio Hotel Buenos Aires - MGallery, Paraguay, ENS1, Callao, Av. Córdoba, Plaza Lavalle, Libertad, AySA Museo del Agua, Del Carmen, Montevideo, Paraná, Uruguay, Viamonte, Junín, Ayacucho, Av. Callao, Teatro Colón, Sanatorio de la Providencia, Tucumán, Tribunales - Teatro Colón, Todo Whisky® (4.9★, 324 — "Los Mejores Whisky Japoneses"), ISEC, Riobamba, Lavalle, Teatro Picadero, Pizzería Güerrín.
- A street photo of a man with long hair and a beard pointing/gesturing, with two other people crossing behind him at a crosswalk.

103

## Slide 104

###### POC FROM KILOMETERS AWAY (At least a bit More)

- We setup a vulnerable antenna in a cardboard box

- We setup an antenna in the building sending the exploit

- We started walking

*The same photo collage as the previous slide (antenna on a rusty pole against the skyline, Buenos Aires street scenes, two people opening a cardboard box, the tilted terminal-log photo, and the measured-route map), now with an extreme close-up meme photo pasted over the center: a grainy, reddish-lit close-up of a man's face looking at the camera, captioned in bold white text* **"More !"**

104

## Slide 105

###### POC FROM KILOMETERS AWAY v2

*Photo collage:*
- A white Ubiquiti dish antenna mounted on a tripod on a waterfront boardwalk, sailboats and a marina behind it, its yellow cable coiled into a bag at the base.
- A woman with long hair looking out over a river toward a sunset skyline (Puerto Madero, Buenos Aires), holding a round white antenna feed wired into an open cardboard box.
- A close-up of a hand holding open a cardboard-box lid, revealing a small screen displaying dense terminal text [illegible] next to a blue step-down converter board with a red seven-segment display reading roughly "921".
- A map of the Puerto Madero docks with a straight measured line and callouts "ISLA PUERTO MADERO — Verano en BA Island", "Alvear Icon Hotel — Top rated", "La Trastienda", "BAR SUR Tango Show — Tango Show Buenos Aires - show de TANGO", "Museo Moderno", distance ticks 0.50 km/1.00 km/1.50 km/1.72 km, and a "Measure distance" callout reading "Click on the map to add to your path" / "Total distance: 1.72 km (1.07 mi)". Street labels visible: Plaza de Mayo, P.º del Bajo, Azopardo, Calabria, Juana Manso, Pierina Dealessi, Av. Elvira Rawson de Dellepiane, Av. Juan de Garay, Brasil, Parque Lezama.

105

## Slide 106

# FINGERPRINTING & VERSIONS

106

## Slide 107

###### FINDING AIRMAX ANTENNAS

```text
v AirMAX AC (Vendor Specific IE)
    OUI: 002722
    OUI Type: ffffff
  > Flags: 0x02
    Message Type: Beacon (1)
    Encrypted Length: 80
    Ciphertext: c286a8909dd964b5aa5d54996fea596f5dd5f7685b70781eaa10be3b6a5
  v [Decrypted payload (AES-128-ECB)]
      [AES Key (HMAC-SHA1(dst,src)[:16]): 6483ef489f21bca28d029e86c55d9f69
      Version: 8
      Source MAC: Ubiquiti_6c:bd:a9 (78:8a:20:6c:bd:a9)
      Radio MAC (mac_0c): Ubiquiti_6c:bd:a9 (78:8a:20:6c:bd:a9)
    > Capability Flags: 0x00000002
      Mixed Mode: 0
      Radioname: AP PTMP-CerritoYcordoba
      SSID: PTMP-CerritoYcordoba
```

*The "Version: 8" line is boxed in red.*

```text
> uv run python -m pyrmax discover ../../packets/ubnt_airmax_devices.pcapng

  78:8a:20:1c:98:1b  (AC)
    radioname      'AP PTMP-CerritoYsarmiento'
    ssid           'PTMP-CerritoYsarmiento'
    ac_msg_types   BEACON
    ac_version     8
    cap_flags      0x00000002
    mixed_mode     0
    frames         84
    first seen     1765842.012760
    last seen      1765842.718826
    peers          (broadcast only)
```

107

## Slide 108

###### FINGERPRINTING FIRMWARE VERSION

We start the Open-System Auth. and Assoc because the FW version in sent on the IE (AirMAX AC >= v9)

*Hand-drawn sequence diagram between "AP" and "STA": Probe Req-IE (STA→AP), Probe Resp-IE (AP→STA), Auth Req (STA→AP), Auth Res (AP→STA), Assoc Req-IE-FW (STA→AP), Assoc Res-IE-FW (AP→STA). The "FW" on both Assoc lines is circled, and the two circles are joined by a curved line labelled "Firmware version".*

| No. | Time | Source | Destination | Info |
|---|---|---|---|---|
| 1 | 0.0000… | Ubiquiti_c4… | Broadcast | Beacon frame, SN=2748, FN=… |
| 2 | 0.1027… | Ubiquiti_c4… | Broadcast | Beacon frame, SN=2751, FN=… |
| 3 | 0.1476… | Ubiquiti_be… | Ubiquiti_c4… | Probe Request, SN=256, FN=… |
| 4 | 0.1476… | Ubiquiti_c4… | Ubiquiti_be… | Probe Response, SN=2752, F… |
| 7 | 0.1505… | Ubiquiti_be… | Ubiquiti_c4… | Association Request, SN=25… |
| 8 | 0.1520… | Ubiquiti_c4… | Ubiquiti_be… | Association Response, SN=2… |

```text
> Frame 8: Packet, 265 bytes on wire (2120 bits), 265 bytes capture…
> Radiotap Header v0, Length 36
> 802.11 radio information
> IEEE 802.11 Association Response, Flags: ........C
> IEEE 802.11 Wireless Management
v AirMAX AC (Vendor Specific IE)
    OUI: 002722
    OUI Type: ffffff
  > Flags: 0x02
    Message Type: Assoc Resp (3)
    Encrypted Length: 64
    Ciphertext: f9a4c74cd7bd7b94cefb0ddd8af89c9493721794002e42b22950…
  v [Decrypted payload (AES-128-ECB)]
      [AES Key (HMAC-SHA1(dst,src)[:16]): ce1f241d63112e4eee7244f36a…
      Version: 9
      Source MAC: Ubiquiti_c4:67:fd (1c:6a:1b:c4:67:fd)
      ic_6b8 (chainmask pair): 0303
      sta_field_68 [open]: 0x338ef79d
      RSSI (per-chain): 2931
      Firmware Name: WA.ar934x.v8.7.22.48486.260227.1
      TX Power (half-dBm): 252
```

108

## Slide 109

HOW WE COULD MAKE THIS BETTER? (WEAPONIZING)

109

## Slide 110

HOW WE COULD MAKE THIS BETTER? (WEAPONIZING)

*Photo of a man's face lit in red, from a film still, captioned "More !" at the bottom.*

110

## Slide 111

###### Sending the exploit

Litebeam 5ac gen2

111

## Slide 112

###### SENDING THE EXPLOIT

###### Let’s make it simple…

- Create a new user in the configuration file

- Apply the configuration

- Turn ON provisioning mode

```text
WA# echo 'users.9.status=enabled' >> /tmp/system.cfg
WA# echo 'users.9.name=faradio2' >> /tmp/system.cfg
WA# echo 'users.9.password=$6$faradio2x$9Y.RJXWyJf07FO984unnsDNuFa3ZOzSCZd
HV/58EAxe3S3DUAt4NHRIvktvMytrqVot05qd1IgvjtYMuQaEI./' >> /tmp/system.cfg
WA# ubntconf
Uservice ... Done.
Fixup ... Done.
Plugin: provmode ... Done.
Plugin: hosts ... Done.
Plugin: infctld ... Done.
Plugin: radio ... Done.
Getty ... Done.
Startup_list ...Done.
Free_cfg ... Done.
Ready to go.
WA# provmode start
WA#
```

*Side panel (Wi-Fi scan detail card):*

```text
LBE-5AC-Gen2:1C6A1BBEFA3A (1e:6a:1b:be:fa:3a)
-34dBm CH 1 2412MHz ~0.5m
2402 - 2422 20 MHz
4 [lock icon] [NONE]
2.4 GHz
CH -1 -> 3 20 MHz
802.11n
[ESS]
[OPEN]
```

112

## Slide 113

###### POST EXPLOITATION - PERSISTENCE

- Connect to the provisioning WiFi with the new password

- Obtain old network password

- Connect an AirMAX device to the network

```text
> sshpass -p "admin12345" ssh faradio2@192.168.172.1

 ---  ---
|\   \|\   \        Welcome to airOS
 \ \   \\\   \
  \ \   \\\   \      PRODUCT: LiteBeam 5AC
   \ \   \\\   \     MAC: 1C6A1BBEFA3A
    \ \_______\
     \|________|     VERSION: WA.v8.7.19
```

```text
XW.v6.3.22# cat /etc/aaa1.cfg
interface=ath0
driver=wextap
wpa=2
eapol_version=2
wpa_key_mgmt=WPA-PSK
wpa_pairwise=CCMP
wpa_group_rekey=3600
wpa_passphrase=noteladigo
logger_syslog=-1
logger_syslog_level=2
disable_pmksa_caching=1
rsn_preauth=0
```

*The "wpa_passphrase=noteladigo" line is boxed in red.*

113

## Slide 114

ALL TOGETHER - DEMO 2

114

## Slide 115

# WE ARE IN, NOW WHAT?

115

## Slide 116

###### FINDING ANOTHER DEVICES

```text
XW.v6.3.22# ubntbox discover
```

| Hardware Address | IP address | Name |
|---|---|---|
| 78:8A:20:A2:42:97 | 192.168.37.103 | NanoBeam M5 16 'NanoBeam M5 16' |
| F0:9F:C2:C8:F0:AD | 192.168.37.104 | UAP-AC-Pro-Gen2 'Piaget AP' |
| 44:D9:E7:6A:3A:43 | 192.168.37.102 | NanoBeam M5 16 'NanoBeam M5 16' |
| 1C:6A:1B:C4:67:FD | 192.168.37.100 | LiteBeam 5AC 'FaradayLB2' |

Total: 4 devices.

*Side panel (NVD-style CVE detail card):*

**CVE-2026-21633 Detail**

**Description**

A malicious actor with access to the adjacent network could obtain unauthorized access to a UniFi Protect Camera by exploiting a discovery protocol vulnerability in the Unifi Protect Application (Version 6.1.79 and earlier). Affected Products: UniFi Protect Application (Version 6.1.79 and earlier). Mitigation: Update your UniFi Protect Application to Version 6.2.72 or later.

**Metrics** — CVSS Version 4.0 | CVSS Version 3.x (selected) | CVSS Version 2.0

*NVD enrichment efforts reference publicly available information to associate vector strings. CVSS information contributed by other sources is also displayed.*

CVSS 3.x Severity and Vector Strings:

| Source | Base Score | Detail |
|---|---|---|
| NIST: NVD | N/A | NVD assessment not yet provided. |
| CNA: HackerOne | 8.8 HIGH | Vector: CVSS:3.1/AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H |

116

## Slide 117

# CONCLUSIONS & TAKEAWAYS

117

## Slide 118

###### WHAT WE FOUND

###### Curiosity → kernel RCE. That's the whole path

- Curiosity. We just bought the devices.

- Linux 2.6.32, compiled in 2009, still shipping today

- Found where the proprietary protocol lives: 802.11 IEs that look encrypted

- Reverse engineered the protocol, AirOS, the kernel modules

- Two bugs. Present since inception.

- Exploited them over the air, from kilometers. No network. No credentials.

118

## Slide 119

###### TEN YEARS, NOBODY LOOKED

###### Or nobody said it.

- On rooftops around the world. Towns, ISPs, even at a front line.

- Vulnerable since inception. Public bounty program the whole time.

- Rated Adjacent → exploited from kilometers away

- CVSS has no vocabulary for line of sight

119

## Slide 120

# THANKS FOR YOUR TIME

##### QUESTIONS?

**WireMAX**

**PyRMAX**

*[A QR code below each label.]*

Gaston Aznarez:     𝕏 @GastonAznarez   [ln] gastonaznarez
Fede Kirschbaum:   𝕏 @fede_k                 [ln] fedek

**Faraday** *(company logo, bottom right)*

120

