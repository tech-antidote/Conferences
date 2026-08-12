---
title: "Hacking the EOD Bot How I Learned to Stop Worrying and Love the Boomba"
speakers: ["Patrick Kiley", "Emily Astranova"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: 2026
source_pdf: "DEF CON 34/DEF CON 34 - Patrick Kiley, Emily Astranova - Hacking the EOD Bot How I Learned to Stop Worrying and Love the Boomba - Gigstorm V1.pdf"
pages: 56
sha256: "5029d9f1cb35c19073b4cb63aa815fcf708ca4e8517a804ddb5ee5f8f1dac0fc"
text_chars: 16019
ocr_pages: 9
has_ocr: true
redacted_secrets: 0
ocr_confidence: 87.3
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:40:17Z"
---
# Hacking the EOD Bot How I Learned to Stop Worrying and Love the Boomba

**Speakers:** Patrick Kiley, Emily Astranova  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Patrick Kiley, Emily Astranova - Hacking the EOD Bot How I Learned to Stop Worrying and Love the Boomba - Gigstorm V1.pdf` (56 pages)


## Slide 1

**Hacking the EOD Bot** How I Learned to Stop Worrying and Love the Boomba

August 2026


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
M Mandiant
Hacking the EOD Bot
How | Learned to Stop
Worrying and Love the
Boomba
August 2026
Google Cloud Secu
rity
```

## Slide 2

## **Agenda**

## **01 Introduction and Background 02 Hardware Teardown**

**03 Software Reversing**

- **04 Radio, Mesh & Networking**

**05 Owning The Boomba 06 Future Work, Thanks & Questions**

Mandiant

Google Cloud 2

## Slide 3

# **01 Introduction**

Mandiant

Google Cloud

3

## Slide 4

## **~ $ whoami**

- Embedded security specialist

- Industry veteran

- Researched avionics security

- Bricked his Tesla while hacking the BMS ○ Had to tow across state lines to fix

- Bought the first Boomba in December

### **Patrick Kiley**

Mandiant

Google Cloud 4

## Slide 5

## **~ $ whoami**

- Have been at Mandiant for 3 years

- Worked at a SOC for 2 years before Mandiant

- Physical security enjoyer

- ● FIRST Robotics mentor

### **Emily Astranova**

Mandiant

Google Cloud 5

## Slide 6

## **Packbot History**

1998 2007 2019 2022
DARPA and iRobot Research  PackBot 510 Released FLIR acquires Endeavor PackBot 525 Released
started
2001 2016 2021
PackBot used at WTC Endeavor Robotics  Teledyne Acquires FLIR
Created

Mandiant

Google Cloud

6

## Slide 7

# **Hardware Teardown**

Yes it runs Linux!

Mandiant

Google Cloud 7

## Slide 8

## **Five Layers of Intel**

1. Power, Main Motors, Ethernet Switch, FPGA

2. Moar FPGA, Conextant video, USB Hubs, DS Transceivers (RS485/RS422)

3. PCI, PCMCIA

4. SBC Carrier, CF Card (512MB)

5. Kontron SBC, 600Mhz Celeron M

Mandiant

Google Cloud 8

## Slide 9

## **45 Pin Accessory x5**

**Pins include:**

24V power, Ground

USB, Ethernet, RS422, Differential FPGA signals, analog video

A few unidentified signal pins

A accessory ports have the same pinout, but go to different transceivers.

Mandiant

Google Cloud 9

## Slide 10

## **Accessories**

- Radios

- Sensors

- Cameras and Manipulators

- Disablement devices

Mandiant

Google Cloud 10

## Slide 11

## **PackBot EOD “Strong Arm”**

- Higher torque version of original 3-joint arm

   - Can break itself

- Shoulder joint, Joint 2,

- Joint 3 with claw, cameras and accessory port

- Main Camera

   - Pan/tilt

   - Blast shield

   - Firing Mechanism

- 3+ cameras, turret, upper and lower manipulator

- 6 pin accessory, video, usb, power

Mandiant

Google Cloud

11

## Slide 12

## **ARM Base**

- Audio TX/RX

- USB Hub

- Xilinx FPGA

- DS-FPGA-DS-FPGA…

- PIC Microcontroller

- Shoulder motor

Mandiant

Google Cloud 12

## Slide 13

## **Tube Circuits**

- USB Hubs

- FPGAs

- Connections to cameras, manipulators

Mandiant

Google Cloud 13

## Slide 14

## **“High Res” Camera Head**

- Multiple FTDI USB/Serial

- Firing Circuit

- Vis/IR Lights

- Sony FCB Zoom camera 26x optical zoom

- Accessory Connector

Mandiant

Google Cloud 14

## Slide 15

## **Rear maintenance Port**

- RS-232

- Ethernet

   - RE hint, look for 1-4 ohms resistance between +,-

Mandiant

Google Cloud 15


> Recovered by OCR — confidence 82/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Rear maintenance Port
40 TX4+
38 CMGND
36 RX4-
e Ethernet
o RE hint, look for
1-4 ohms
resistance
between +,-
4
5
TD4- 2 O——
RD4-
TD4+ 1
15
```

## Slide 16

## **Power**

- Original PackBot used NiCad/Nimh

- Current one uses 4 BB-2590 Li-Ion

   - Same form factor as single use BA-5590

Mandiant

Google Cloud 16

## Slide 17

## **OCU Evolution and accessories**

- From Heavy with hockey puck controllers

- Amrel Laptop - Ubuntu

- x86 Rugged Android

- Logitech controller

- USB Firing system

Mandiant

Google Cloud 17

## Slide 18

# **Software Reversing**

Packbot 5.1.3, 6.9 / Aware 2.0

Mandiant

Google Cloud 18

## Slide 19

## **Architecture and OS**

- Robot Operating System: iRobot CommonOS (Linux kernel 2.6)

- OCU Operating System:

   - OCU 5.x: Ubuntu 9.04 (Jaunty Jackalope)

   - OCU 6.2: Ubuntu 10.04 (Lucid Lynx)

- Language Runtime: Aware 2.0 runs on Python 2.5, wrapped heavily around compiled C++ shared object bindings

- Management / Remote Access: SSH Server on TCP/22. Started via legacy init scripts

- All Packbots have same root password

- All processes run as root

- OCU uses irobot username

Mandiant

Google Cloud 19

## Slide 20

## **Ad-Hoc Addressing**

- OCUs and Robots have assigned serial numbers

- IP address derived from serial number

- For example 13913/256

   - 54 remainder 90

   - X.X.54.90

- Eliminates conflict and need for DHCP

- 172.16 - Ethernet

- 172.17 - Wireless

- 172.18 - Fiber

Mandiant

Google Cloud 20

## Slide 21

## **Session Management**

- Robot Metadata (/robot/info.html): XML payloads track dynamic subsystem access states (AVAILABLE vs. BUSY).

- Session Acquisition (selectSession.html):

   - Spawns backend Nysta UDP C++ daemons and initializes physical robot joints.

   - CGI Name Resolution: Requires a directly resolvable clientid hostname or IP (e.g., 172.16.0.232) via mDNS/DNS to prevent indefinite CGI lookup hangs

- Responds with session information, including numeric authid value

Mandiant

Google Cloud 21

## Slide 22

## **Session Management**

- Spin-Up Latency: Physical joint/daemon initialization takes 5–10 seconds (requires client HTTP timeouts ≥ 15s).

- Session release and Lockouts (releaseSession.html):

   - Employs unique numeric tokens (authid) to “defend” against session hijacking.

   - ○ Unclean client disconnects leave sessions locked as BUSY indefinitely.

Mandiant

Google Cloud 22

## Slide 23

## **Startup Process – 6.9**

- /opt/irobot/bin/aware2Start

   - Starts Aware Publish/Subscribe server XML/RPC server

- Starts Aware node manager

- ● /opt/irobot/bin/aware-cfgdb ← Listens on high random port

   - Uses libshttpd.so

- /opt/irobot/bin/packbot-payload-system

- /opt/irobot/bin/packbot-jaus-node-manager

- /opt/irobot/bin/robot-discovery

- /opt/irobot/bin/aware-web-server

Mandiant

Google Cloud 23

## Slide 24

## **Web Server**

- Port 80

Mandiant

Google Cloud 24


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Web Server 2
Cf A\ Notsecure 172.16.46.176
e Port 80
PackBot Chassis Login
Username: | |
Password: |
| Submit |
:~$ nmap -Pn -sV -T4 172.16.46.176
) at 2026-06- 30 16:10 PDT
Starting Nmap 7.94SVN ( htt
Nmap scan report for 172.16.
Host is up (0.0018s Latency).
Not shown: 951 closed tcp ports (conn-refused),
PORT STATE SERVICE VERSION
22/tcp open ssh Dropbear sshd 0.51 (protocol 2.0)
80/tcp open http BaseHTTPServer 0.3 (Python 2.5.2)
111/tcp open rpcbind 2 (RPC #100000)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
nmap.or
46 filtered tcp ports (no-response)
Mandiant Google Cloud
24
```

## Slide 25

## **Video Feed Decoding**

- Active UDP Feeds

   - Primary drive camera broadcasts on UDP/9002

   - High-Res secondary camera on UDP/9012

- Packetization Protocol (RFC 3550):

   - 1442-byte MTU consisting of 12-byte RTP headers and 1402 bytes of raw video payload.

   - Stream activation is triggered dynamically upon successful HTTP session registration.

- MPEG-1 Stream Reassembly:

   - Payloads grouped by RTP Timestamp and sorted by Sequence Number.

   - Stripping the 12-byte RTP header yields a MPEG-1 Video stream.

Mandiant

Google Cloud 25

## Slide 26

## **Video Feed Decoding**

- Active UDP Feeds

   - Primary drive camera broadcasts on UDP/9002

   - High-Res secondary camera on UDP/9012

- Packetization Protocol (RFC 3550):

   - 1442-byte MTU consisting of 12-byte RTP headers and 1402 bytes of raw video payload.

   - ○ Stream activation is triggered dynamically upon successful HTTP session registration.

- MPEG-1 Stream Reassembly:

   - Payloads grouped by RTP Timestamp and sorted by Sequence Number.

   - Stripping the 12-byte RTP header yields a MPEG-1 Video stream.

Mandiant

Google Cloud 26

## Slide 27

## **Video Feed Decoding**

- Getting the footage into VLC media player meant using a demux loopback proxy

- ● Standard FFmpeg/OpenCV demuxers fail on uncontainerized RTP UDP flows without .sdp manifests.

- Python Demux Proxy: A background thread catches UDP packets, reassembles raw MPEG-1 frames, and streams them over local TCP

- In 6.9, Video is Multicast to 239.2.x.x and format changes to MPEG-4/H.264

Mandiant

Google Cloud 27

## Slide 28

## **Video Feed Demo**

Mandiant

Google Cloud 28


> Recovered by OCR — confidence 88/100 on the text kept, 56/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Video Feed Demo
py 11976 8080 Wi-Fi
Battery: ?
407 PM
Mandiant Google Cloud 28
```

## Slide 29

## **Video Feed Demo**

Mandiant

Google Cloud 29

## Slide 30

## **Nysta 5.X**

- Protocol Overview: Aware 2.0 communications run across UDP/50001 and UDP/50002 using the proprietary Nysta 5.x binary framing layout

- Preamble & Invariant Offsets:

   - Magic string “tysn”

   - Session protocol flags (02 01 00 00)

   - 0x0a: Session Lease Connection Handle

   - ○ 0x0b - 0x0c: LEB128 Varint sequence framing

- Context Identifiers (CIDs): Command payloads are packed into distinct structural contexts (e.g., 0x2b for Master Brake, 0x2d for OCU Mode, 0x31 for Pose)

Mandiant

Google Cloud 30

## Slide 31

## **Joint Architecture for Unmanned Systems (JAUS)**

- Fully implemented as control protocol for 6.x

- Uses port UDP 3794

- Single packet can contain multiple messages

- https://docs.openjaus.com/2023.0/jaus/jaus_system/

Mandiant

Google Cloud 31

## Slide 32

## **Joint Architecture for Unmanned Systems (JAUS)**

- Uses port UDP 3794

- U-Point Android APK uses JAUS

   - Decompiled and analyzed/modded

- https://docs.openjaus.com/2023.0/jaus/jaus_sys tem/

Mandiant

Google Cloud 32

## Slide 33

# **Radio System, Mesh & Secure Networking**

Mandiant

Google Cloud

33

## Slide 34

## **Original Packbot**

- Long Range 802.11b

- Embedded into robot

- Sector Antennas

- AD-HOC 802.11 network “TMR”

Mandiant

Google Cloud 34

## Slide 35

## **Fiber Option**

- Fiber Spool

- ● 220 Meter spool of one strand single mode fiber

- 100Mb/Sec

- Spools out from robot

- Splits TX/RX into different wavelengths

Mandiant

Google Cloud 35

## Slide 36

## **Packbot 510**

- Upgraded to 802.11g

- Fiber Unchanged - If it ain’t broke

- ● Added option of 4.9 Ghz mesh radio as external module

- Uses OpenVPN as overlay

- ● Captured packets using surplus Cisco gear

Mandiant

Google Cloud 36

## Slide 37

## **Packbot 510**

- Hacked into radio by eavesdropping UART comms

- ● PIC microcontroller logs into radio module as root and executes shell script when encoder changes channel

- Mesh network that gets automatically created/healed

   - Uses Babel/OpenVPN

- Uses 4.9 GHZ Public-Safety Band

- Acquired surplus Cisco gear to sniff

Mandiant

Google Cloud 37

## Slide 38

## **Packbot 510**

- Used through at least 2015

- OpenVPN – Not encrypted

- 4.9 Ghz radio – Not encrypted

Mandiant

Google Cloud 38


> Recovered by OCR — confidence 78/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Packbot 510
Used through at least 2015
OpenVPN -— Not encrypted
4.9 Ghz radio - Not encrypted
dev tape
cipher none
Fast-10
ping 1
ping-restart 10
no-replay
proto udp
management localhost 7505
Source Port Destination Dest Port Protocol Lengt! Info
5555 Ubiquiti_44:7f:44 5e00 802.11 76 Acknowledgement, Flags=
172.16.0.5 IPv4 1514 Fragmented IP protocol (proto=UDP
1194 10.0.0.54 1194 OpenvPNn 88 MessageType: Unknown Messagetype
5555 Ubiqui 5000 802.11 76 Acknowledgement, Flags= oC
Ubiquiti_a4:7... 5555 Broadcast 5000 802.11 178 Beacon frame, SN=405, FN=®, Flags:
10.0.0.4 1194 10.0.0.54 1194 OpenVPN 1431 MessageType: Unknown Messagetype
172.16. 5555 Ubiquiti_. 5200 802.11 76 Acknowledgement, Flags= c
172.16. 172.16.0.5 IPv4 1514 Fragmented IP protocol (proto=UDP
10.0.0. 1194 10.0.0.54 1194 OpenvPNn 88 MessageType: Unknown Messagetype [55 —
172.16.0. 5555 Ubiquiti_44:7F:44 5@00 802.11 76 Acknowledgement, Flags= c
172.16. 172.16.0.5 IPv4 1514 Fragnented IP protocol (proto-uoP| 24 ++ Y6B.
10.0.0.4 1194 10.0.0.54 1194 OpenVPN 88 MessageType: Unknown Messagetype | 00 ackbot1
172.16.0.48 5555 Ubiquiti_aa: 5000 802.11 76 Acknowledgement, Flags= c | ee
172.16.0.48 172.16.0.5 IPv4 1514 Fragmented IP protocol (proto=U0P} 9g
10.0.0. 1194 1€.0.0.54 1194 OpenVPN 88 MessageType: Unknown Messagetype
172.16.0.48 5555 Ubiquiti_44:7f:44 5@00 802.11 76 Acknowledgement, Flags= ac
10.0.0. 1194 10.0.0.54 1194 OpenVPN 816 MessageType: Unknown Messagetype | 40
10.0.0. 1194 10.0.0.54 1194 OpenvPNn 598 MessageType: Unknown Messagetype | QQ
10.0.0.54 1194 10.0.0.4 1194 OpenvPNn 226 MessageType: Unknown Messagetype[!
172.16.0.48 5555 Ubiquiti_44:5a:2* 5000 802.11 76 Acknowledgement, Flags= wc | 1
10.0.0.4 1194 10.0.0.54 1194 OpenVPN 227 MessageType: Unknown Messagetype[N 0@
172.16.0.48 5555 Ubiquiti_44: 5000 802.11 76 Acknowledgement, Flag c | 10
10.0.0.54 1194 10.0 1194 OpenVPN 228 MessageType: Unknown Messagetype[N 29
172.16.0.48 5555 5000 802.11 76 Acknowledgement, Flags= C | og |. Y6B. ....e0d-
10.0.0.4 1194 10.0.0.54 1194 OpenVPN 583 MessageType: Unknown Messagetype[|
172.16.0.40 5555 Ubiquiti_44:7f:44 5e00 802.11 76 Acknowledgement, Flags= wc | 02 ackbot1 3913...
Google Cloud 38
```

## Slide 39

## **Newer Packbot 510s**

- Latest versions use Wave Relay

- Mesh radio system

- Made by Persistent Systems

- Walled garden using MPU5 radios

- 2.2-2.5 Ghz, C-Band, L-Band

Mandiant

Google Cloud 39

## Slide 40

## **Custom radios**

- Used Ethernet and Power from accessory port

- 3D Printed mounts/cases

- OpenWRT WiFi7

- MikroTik Outdoor ← Favorite

- Ubiquiti Rocket Prism 5Ghz

- Custom Persistent Systems embedded module ← Expensive but easy to use

- OM5P-AC (FIRST Robotics)

- GL.iNet GL-AXT1800 + Starlink

Mandiant

Google Cloud 40

## Slide 41

# **Owning the Boomba**

Mandiant

Google Cloud 41

## Slide 42

## **Original Brick**

Mandiant

Google Cloud

42

## Slide 43

## **Boomba to Roomba**

Mandiant

Google Cloud 43

## Slide 44

## **VM Ports**

- Version 5.1

- Version 6.2

   - Mostly Works on 6.9 robot

Mandiant

Google Cloud 44


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
VM Ports
Version 5.1
Version 6.2
o Mostly Works on 6.9 robot
4:04 PM | hhj-rzja-tyv
Emily Astranova
Brake Engaged
To release brake,
press the Back button
(do not press any other
buttons).
Patrick Kiley
44
```

## Slide 45

## **Tablet Based**

- Ported app to other tablets

- Android 6.01 - 12

- Harder, better, faster, stronger tablets

Mandiant

Google Cloud 45

## Slide 46

## **VM Ports**

- Steam Deck!

   - Used CachyOS since SteamOS is immutable(ish)

   - ○ Still in VMware Workstation, libvirt/KVM had graphical issues

   - Steam Input for mapping controller to keyboard inputs, USB forwarding headaches

Mandiant

Google Cloud

46

## Slide 47

## **VM Ports**

- Steam Deck!

   - Used CachyOS since SteamOS is immutable(ish)

   - ○ Still in VMware Workstation, libvirt/KVM had graphical issues

   - Steam Input for mapping controller to keyboard inputs, USB forwarding headaches

Mandiant

Google Cloud

47

## Slide 48

## **Bot Hijack**

Mandiant

Google Cloud 48


> Recovered by OCR — confidence 83/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Bot Hijack
PB Windows Powershell X
BE Windows Powershell
Ps C Emily> curl “t
Brake Engaged
To release brake, 9+
press the 9 button KA
(do not press any other
buttons). Onset
PackBot-11976
Press @ for
for Hot Keys
48
```

## Slide 49

## **Bot Hijack**

Mandiant

Google Cloud 49


> Recovered by OCR — confidence 87/100 on the text kept, 61/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Bot Hijack
x BE Windows Powershell
Select Robot...
Maintenance...
Shut Down
(2) Select
Mandiant Google Cloud 49
```

## Slide 50

# **Lessons & Future Efforts**

Ask us for STICKERS!

Mandiant

Google Cloud 50

## Slide 51

## **Lessons, Key Takeaways**

- Defense in Depth

   - Do not rely on a single external technology to protect everything

   - Implement authentication, and encryption for control traffic

      - PKI would be seamless

   - Implement Secure Boot, DM-Verity, LUKS

- Tech debt is a real issue

   - 20 year old CPU, Linux and language architecture

- Security through obscurity can delay, but not prevent analysis

   - Don’t rely on lack of public access as a control measure

Mandiant

Google Cloud 51

## Slide 52

## **ATAK Integration**

- Protocols already supported

- JAUS

- Multicast Video

Mandiant

Google Cloud

52


> Recovered by OCR — confidence 91/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ATAK Integration
e Protocols already supported
e JAUS
e Multicast Video
Red X
10S GE 11047 06841
779 ft MSL DTEDO
30°M 3.16 km
Red X
10S GE 11047 06841
16u R ETA:
Mandiant Google Cloud 52
```

## Slide 53

## **Video Upgrades**

- Conexant encoder heavily limits resolution

- Best solution is streaming camera  mounted and using out-of-band video

Mandiant

Google Cloud

53

## Slide 54

## **Car Hacking Village**

- PackBot Challenge

   - Control a robot and manipulate a device

   - Penalty for mistakes

   - Best times invited back to finals on Sunday

- Win a PackBot 510!

Mandiant

Google Cloud 54

## Slide 55

## **Credits and Thanks**

- Alex Tselevich

- Sam Schumacher

- Michael Maturi

- Angelo Alviar

- Teledyne Team

- Jacob/Aaron and the Mandiant FLARE team

- Mark Karayan and Google PR

Mandiant

Google Cloud

55

## Slide 56

# **Thank you**

© 2026 Google LLC. All rights reserved. Mandiant and Google are trademarks of Google LLC. All other trademarks are owned by their respective owners.
