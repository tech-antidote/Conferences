---
title: "The Key to Remote Vehicle Control Autonomous Driving Domain Controller"
speakers: ["Shupeng Gao", "Yingtao Zeng", "Jie Gao", "Yimi Hu"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2024"
edition: "ASIA"
year: 2024
source_pdf: "BlackHat ASIA 2024-Slides/Shupeng Gao & Yingtao Zeng & Jie Gao & Yimi Hu-The Key to Remote Vehicle Control Autonomous Driving Domain Controller.pdf"
pages: 95
sha256: "b0733adbb76857ff32566418cdd296c88387dcf3903eb729d9e9cc0741d87fcf"
text_chars: 33151
ocr_pages: 24
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:51:47Z"
---
# The Key to Remote Vehicle Control Autonomous Driving Domain Controller

**Speakers:** Shupeng Gao, Yingtao Zeng, Jie Gao, Yimi Hu  
**Conference:** Black Hat ASIA 2024  
**Source:** `BlackHat ASIA 2024-Slides/Shupeng Gao & Yingtao Zeng & Jie Gao & Yimi Hu-The Key to Remote Vehicle Control Autonomous Driving Domain Controller.pdf` (95 pages)

## Slide 1

# The Key to Remote Vehicle Control : Autonomous Driving Domain Controller

Shupeng Gao, Yingtao Zeng, Yimi Hu, Jie Gao From Baidu Security Lab

#BHASIA @BlackHatEvents

## Slide 2

### Traditional Cars

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2024
Traditional Cars
fuel tank
shock
absorber
brake
= exhaust
transmission Ce catalytic pipe
converter
© Encyclopaedia Britannica, Inc
```

## Slide 3

### Current Cars

# BHASIA @BlackHatEvents

## Slide 4

### Future Cars

# BHASIA @BlackHatEvents

## Slide 5

### The Evolution of BMW 3 Series Electronic Systems

# BHASIA @BlackHatEvents

## Slide 6

### 关于自动驾驶域控制器

# BHASIA @BlackHatEvents

## Slide 7

### Our Previous Research On the IVI

# BHASIA @BlackHatEvents

## Slide 8

### Our Previous Research On the T-Box

# BHASIA @BlackHatEvents

## Slide 9

### Our Previous Research On the 4G Module

# BHASIA @BlackHatEvents

## Slide 10

# BHASIA @BlackHatEvents

## Slide 11

### Regarding Autonomous Driving Domain Controllers

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2024
Regarding Autonomous Driving Domain Controllers
Camera
ADAS Domain Controller
ol
 ,
CAN-FD
Eth Gateway
*
GNSS/1PPS
```

## Slide 12

Why

# BHASIA @BlackHatEvents

## Slide 13

### Why Research ADAS ?

- Smart vehicles may be the most complex and advanced IoT devices accessible to the general public.

- Compared to the past, smart cars incorporate a myriad of new technologies including new architectures, communication interfaces, processors, and operating systems.

- Currently, there is a lack of attention to the security of ADAS, which is relatively poor.

- Improper design may pose risks of remote vehicle control.

- Compared to IVI and T-Box devices, this represents a new research area.

- Involves AI, which is very interesting and cutting-edge.

- A new research direction for security researchers and automotive manufacturer security teams.

Final goal: Enhancing the security of ADAS devices.

# BHASIA @BlackHatEvents

## Slide 14

#### Why Research ADAS -- High Complexity

NIO Center Computing Cluster

System: 4x Linux 1x Android ( QNX VM)

SoC:

4x Nvidia Orin-X 1x Qualcomm SA8155

MCU: 2x TC399 1x TC397

4x EMMC 5x UFS

More than 1000+ TOPS @int8 (RTX4090 660 TOPS @int8)

# BHASIA @BlackHatEvents

## Slide 15

### Why Research ADAS -- High Complexity

# BHASIA @BlackHatEvents

https://cars-technical.com/product/xpeng-service-repair-manual-circuit-diagram/

## Slide 16

#### Why Research ADAS – New Architecture - Ethernet Connectivity

# BHASIA @BlackHatEvents

https://cars-technical.com/product/geely-hip-hif-service-repair-manuals/

## Slide 17

#### Why Research ADAS – New Architecture - Ethernet Connectivity

# BHASIA @BlackHatEvents

https://cars-technical.com/product/im-l7-ls7-workshop-service-repair-manual-wiring-diagram/

## Slide 18

### Why Research ADAS -- Controllable Vehicles

###### ADAS is connected to

Powertrain CAN and Chassis CAN.

It Naturally Controls Vehicles

https://cars-technical.com/product/im-l7-ls7-workshop-service-repair-manual-wiring-diagram/

# BHASIA @BlackHatEvents

## Slide 19

What

# BHASIA @BlackHatEvents

## Slide 20

### More Than 30+ ADAS Devices

# BHASIA @BlackHatEvents

## Slide 21

### The Development Process of ADAS Controllers -- FPGA

## ACC / LKA 0.5 TOPS

# BHASIA @BlackHatEvents

## Slide 22

### Arm CPU with AI Inference Capabilities (Front Camera)

#### Mobileye Q4M/H 1.1~2 TOPS

#### Horizon Journey 2 4 TOPS

# BHASIA @BlackHatEvents

## Slide 23

### Low-Speed Autonomous Driving Domain Controller

#### TI TDA4VM 8 TOPS

#### Mobieye 4H 2 TOPS

# BHASIA @BlackHatEvents

## Slide 24

### Horizon J3

#### 1xJ3 5 TOPS

3xJ3

3xJ3

# BHASIA @BlackHatEvents

## Slide 25

### 1x J3 And 1xTDA4 VM

# BHASIA @BlackHatEvents

## Slide 26

### 2x TDA4 VM

# BHASIA @BlackHatEvents

## Slide 27

### TI TDA4 VH

32 TOPS

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat '
ASIA 2024
TI TDA4 VH
y WLLLLLLLI ae) y KEE AG
LEA SELLS Le SSEELS
32 TOPS
```

## Slide 28

### Horizon J5

# BHASIA @BlackHatEvents

## Slide 29

### Nvidia Xavier

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
ASIA 2024
Nvidia Xavier
piri ij yyh\\
PERREEEET HEE pPPPe ry |
```

## Slide 30

### Nvidia Orin-X

254 TOPS

# BHASIA @BlackHatEvents

## Slide 31

### Nvidia Orin-X

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
ASIA 2024
Nvidia Orin-X
+" woe
oe
A
ae ae
7
i>
. %
ot 3
Wii WwW
```

## Slide 32

### 2x Orin-X

#### 508 TOPS

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blackhat to Poo at
ASIA 2024 el Jatig SoS Bolt Boa
i
: = ped By # va, yo": wrt
2x Orin-X [Pee eee
508 TOPS [ia
aaa
```

## Slide 33

### 4x Orin-X

#### 1016 TOPS

# BHASIA @BlackHatEvents

## Slide 34

### Nvidia Orin-N

#### 84 TOPS

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
* Ni
blackhat
ASIA 2024
Nvidia Orin-N
4%
A
Mar OMS
Polelelaled
-.
*2Nd1 HO4 Bod NIVH
pbadsdbadetededaeede 4
pebheberrrrerehnrees
```

## Slide 35

### Orin-X VS Orin-N Same Interface

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blackhat .
ASIA 2024
Orin-X VS Orin-N Same Interface
Ie
```

## Slide 36

### 2x Mobileye 5H

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2024
2x Mobileye 5H
MODEL: V3YB
DAV3YBPTEGO
REV:G
```

## Slide 37

### 2x Qualcomm SA8650

100 TOPS

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
ASIA 2024
2x SET SA8650
nies Vivniieie
100 TOPS
re 0 erste +
wae
```

## Slide 38

#### ADAS Internal Structure:

- ADAS Internal Structure:

- SoC: Includes ARM CPU and AI NPU, runs an operating system, performs AI inference

- • Memory: DDR

- Storage: UFS, EMMC, NorFlash

- Network: Onboard Ethernet chip

- MCU: Autonomous driving decisions, CAN transmission and reception, fault monitoring and degradation, power management, ultrasonic radar algorithms, AEB decisions, etc.

- Serializer/Deserializer: Camera data input, outputs video signal (e.g., parking 360 view) to IVI

- • Power management chip, CAN transceiver chip. • Various interfaces: Power, Ethernet, CAN, etc.

- Other: GNSS GPS chip, IMU chip

# BHASIA @BlackHatEvents

## Slide 39

FSD View

#### IVI

Parking View

front LVDS Display
fisheye
FSD Parking
front
main MIPI Camera
Perception Tasks ZMQ/DDS/SOMEIP
HMI
Interface Localization
front
Deserializer Obstacle Monitor Time Sync
narrow
LVDS Prediction
Control HW Driver
AEB Log
left Lane Nvidia Drive OS
Planning
Traffic Light
IMU
HDMap
right
Soc Orin-X
GNSS
rear SPI Interface
Arbitration CAN/FlexRay Steer-by-wire
Fault diagnosis Power management
Lidar Marvell Switch
Ultrasonic radar
MCU TC397
ADAS CAN Transceiver
Chassis/Powertrain CAN
Ultrasonic radar
GW # BHASIA @BlackHatEvents

## Slide 40

Linux / QNX
Cameras
Soc Orin-X Perception
Control
Android on QNX 4/5G module
Display Internet
CAN MCU TC397
ADAS CAN IVI CAN T-Box
Chassis/Powertrain CAN Info CA N Telemati c s CAN
CAN CAN CA N CA N
Eth Switch
VCU CAN CAN GW
Diag CAN Body CAN
ECUs
CAN CAN
Auto AC Door
DoIP
OBD Body electronics
# BHASIA @BlackHatEvents

## Slide 41

**Perception Prediction BEV Planning OCC Fusion AEB Control Lane Localization Traffic Light MAP/HMI Obstacle** ROS2 Nvidia DriveOS Other Auto Framework Linux QNX Orin Horizon TI ….. MCU EMMC/UFS SW CAN ….. GNSS IMU Ser/Des PMIC

# BHASIA @BlackHatEvents

## Slide 42

How

# BHASIA @BlackHatEvents

## Slide 43

### How to Research ADAS - Analyze as an IoT Device

Familiarize with the structure, find entry points, complete the attack. Remote code execution (RCE) may not be achievable, but risks such as information leakage are also significant.

Operating System:

Access the file system, for example, through firmware extraction or firmware download. Obtain shell access, for example, through a debugging port.

Interface Analysis: Assess interfaces: UART, Ethernet ports, JTAG, DAP, etc.

Signal Analysis: Analyze CAN signals, CAN FD, vehicle Ethernet.

# BHASIA @BlackHatEvents

## Slide 44

### How to Research - Acquiring the Device

# BHASIA @BlackHatEvents

## Slide 45

### How to Research - Acquiring the Device

# BHASIA @BlackHatEvents

## Slide 46

#### How to Research - Powering On and Ignition

# BHASIA @BlackHatEvents

https://cars-technical.com/product/im-l7-ls7-workshop-service-repair-manual-wiring-diagram/

## Slide 47

### Read EMMC/UFS Storage

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
ASIA 2024
Read EMMC/UFS Storage
.
.
.
.
.
©
.
€
Se eee 2b eeeee0
eeeeee
```

## Slide 48

### Read EMMC Storage

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2024
Read EMMC Storage
SO-F BGA (11.54 13
O00 ~« ©8008
@~ @---@08008
© Own @OOSO
BJOGSSOSOSOOSSEOSSD
BSEVSOHSSSOSSSSEDSS
i
jeunggan’
```

## Slide 49

### Use UFS Programmer to dump / write

EMMC internally integrates a Flash Controller. Allows direct editing and deletion. For example, modifying the /etc/shadow file.

UFS currently lacks effective file management methods. Similar as dd.

Current use of UFS programmers:

- Complete dump, write (up to 300MB/s).

- Supports specified offset.

# BHASIA @BlackHatEvents

## Slide 50

### Use UFS Programmer to dump / write – Slowly Speed

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2024
Use UFS Programmer to dump / write
=) VD1:UFS_ MICRON _MT128GAVAT2U31AA 06 01 2024 20 47 48 Phys P
= FHKE (PRES IAF) (4)
= Cl
+] . data
#-([]| 4 ete
+-{_] home
4-] opt
4] . root
4] run
#-[]| , tmp
#-(]| } usr
4]! } var
[4 vss
S&S Medusa Pro Software version 2.1.5
Brand
Log
Manufacturer name: MICRON 73
Product name: ' T
Serial Number:
O&M ID: CR
Page size
Block size
Slock count
Size 2 119.2
AttrRefClkFreeq = 0
MaxDataInSize = 52768
MaxDataOutSize = 32768
Physical partition number: 0
Block count : 4 xix
Size 2
Partition table was not found.
Partition table was not found.
Partition table was not found.
Opening 3: /UFS_MICRON
MTLZ8GAVAT2U31AA_06_01_2024_ 25
Reading. Please wait...
a
Cocrorius;——~» Read Uniock Codes
ee S10 / S10+ / Sli0e
.47_46_Phys_Part_0.bin file...
~ Progress —— ——
] Read Android build info wha
onnecting
Vnite data venfication
Main [Factory repair|{ UFS Service
User Data Area
WREF 0.00V Speed] 4 7auBss] Progress 7.137 GE/1192G8 ETA 06:50:03 Goxstatus: Connected Firmware version. 1.00 SIN. 200005231
```

## Slide 51

### Use UFS Programmer to dump / write – New Tools

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2024
Use UFS Programmer to dump / write — New Tools
142.8MB/S
Brand:
Version:
Boot:
WDC
2.1
Boot A
SN: 2050
FW: 10303
Batrine
SDINDDH6-128G
2023-06
14
```

## Slide 52

### Partition Table Details

###### Has GPT

No GPT/MBR

Has a GPT partition table, allowing direct reading of partitions and files:

•EXT4: Horizon, TI

Nvidia devices lack a standard partition table:

•EXT4 (Orin)

•QNX (Xavier)

•QNX: Mobileye, TI, Qualcomm

QNX6: Mount read-only, can’t write

# BHASIA @BlackHatEvents

## Slide 53

### Has Partition Table

###### TDA4 EMMC Dump QNX，with GPT

###### J3 EMMC Dump EXT4，with GPT

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2024
Has Partition Table
ERs BO Fike DE Oink nage M29. 1G8(296248) eT
2 AR 2SS SMMRM GS BmEMTS 1079552
VO2GR_TOM4 VH_dd.tee(2968) Sen Te Nae (22 BDsFile EES:Disk image Sib7.3GB(7456MB) IETS HAR255 SMEs Smee: 15269888
~ HR o " ezee aces
— ACT) @ eH doops eet at exe sane snare ~~ HK (9) cae
~ #2)
ann ae wey eee
TDA4 EMMC Dump QNX, with GPT J3 EMMC Dump EXT4, with GPT
```

## Slide 54

### No Partition Table

If there is no partition table, need  rebuild

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2024
No Partition Table
RAW 16.068 11,968 12,668 111,068
} MT256GAV/ 2 28 @2_ 20:2 3 10 > Part { 3 MO:File HE:Disk image GM:158.7G0(162464MB) FEMOM20711 M255 MRS SMI 332727808
itior sec = HDOcharddiskSSD(256GB) Stem MO gare
© VOO:D)I 14 qnx2(1568) ; RHE x
HD1:SamsungPortableSSOTS(932GB) eM Se
_ VOt:feifan MT256GAVATAU31AA 28 $ Sf a oaaal aoe
a FRAG » 4577 FERRARI 12.668 19 OXT4 9 11 00:00:00
ap cont 11 00:00:00
: ap_data 11.00:00:04
o app 11 .00;00:0¢
. boot B
” containers 3
ce data 'B
etc 13 22:37:49
fota 11 00:0¢
hdm 1100: 1
home rr] Bil} PieR 1322
log Ji 00:0
lost+found yee dtwx--~--- 2022-04-26 04:38:16 2022-11-03 22
media ree rwexr-xr-x 2020-08-01 00:37:17 2022-11-03 22:37:49
mnt yee ewexrexrex 2022-04-26 02:38:46 2022-11-03
If there is no partition table,
need rebuild
```

## Slide 55

### Nvidia QNX / Android IVI QNX

- The tool only supports searching for EXT3 EXT4, FAT, and other file systems.

- QNX requires manual partitioning.

binwalk -R ‘\xeb\x10\x90\x00\x00’

start_offset=0x3EF500000 end_offset=0x543280000 count=$(( (end_offset - start_offset) / 0x100000 )) dd if=part3.dd of=new_part3.bin bs=1024 skip=$((0x80000/1024))

# BHASIA @BlackHatEvents

## Slide 56

### Nvidia QNX / Android IVI QNX

###### Then use tools, such as qnxmount

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
ASIA 2024
Nvidia QNX / Android IVI QNX
qnxmount
Then use tools, such as
qnxmount
* gnxmount
* @nxmount
@_prepare.sh b 5 Launch, ota_h ‘ p J lf_¢ i_cleanup.sh slm_ota_hd
Launch_fact« 5 Signature_verify.sh 5 lm_raw_sensor .xm
it_e28_ota_hdmap.sh lLaunch_raw_dat . t S| un 5 summon Launch .xm
check_board_fuse.sh init_factorymode.sh Launch . xml
init_vxminer_folder sion. t
early_start.sh Launch_e28_ota_ap. sh wait_for_cp_init.sh
* gnxmount x
* @nxmount x
```

## Slide 57

### What Can We Obtain From a Storage Dump?

Sensitive files:

- /etc/shadow for cracking passwords

- Encryption keys (disk encryption, file encryption, OTA)

- MQTT private keys, passwords

- OTA upgrade packages

- Model files

- MCU firmware

-

   - ….

- Used frameworks and technologies

Startup processes, where vulnerabilities can be discovered in listening port processes through reverse engineering.

# BHASIA @BlackHatEvents

## Slide 58

### How To Getshell

Half of the devices have SSH enabled:

- Default credentials: nvidia/nvidia

- Brute force with Hashcat

- Write a new /etc/shadow

Password verification mechanism:

- Password cracking algorithm

Dump flash, modify the startup process

Serial port login

Analysis and exploitation of vulnerabilities in listening processes

# BHASIA @BlackHatEvents

## Slide 59

### How To Getshell – Modify UFS

Modifying EMMC storage is quite common.

Now we:

1. Dump all UFS as a .img

2. Modify .img:

- 0xd65f03c0 is ret instruction

- Bypass ChangePasswd() function

- Modify shadow file

3. Write the .img file back to UFS

# BHASIA @BlackHatEvents

## Slide 60

### How To Getshell – UART Interface

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2024
How To Getshell — UART Interface
} Jas-t ode l#
3das/adas-—rt/model
da jas-—rt/model#
la 3das-rt/model# —a |
1.0K Nov 2008
ro 1.0K No 2000
i) 3 It 2008 model-che
rot 3M Ne 2008 model. hbmr
f - roo ro 5K ft 2000 model_info. ’
—fwx----—- 00 ro @.5K ft 2008 rsit sor
oh, See rrapps
hwte Lor
e| p|
} planning
2
o
4
'
a
”
```

## Slide 61

### Obtaining Network Access

- All onboard devices use vehicle Ethernet

- Use two-core cables

- Supports 100M/1000M

# BHASIA @BlackHatEvents

## Slide 62

#### Obtaining Network Access -- How to Use Vehicle Ethernet Adapters

- Vehicle Ethernet is divided into four combinations: 100M/1000M and master/slave.

- Additionally, 100M is differentiated by cable sequence.

- Recommended to use adapters with auto-negotiation capabilities.

# BHASIA @BlackHatEvents

## Slide 63

#### How to Obtain The IP

Capturing packets in promiscuous mode to determine the SOC IP address:

- VLANs are commonly present.

- Most devices do not use ARP and require MAC address binding.

- Sometimes, setting the local IP and MAC address is necessary based on the UDP's destination IP and MAC.

- Some devices use IPv6 addresses.

# BHASIA @BlackHatEvents

## Slide 64

#### Interface Risk

Board often has many interfaces, especially UART and JTAG.

Some car manufacturers not only have numerous debugging interfaces but also clearly label them.

These interfaces are often needed for debugging and firmware flashing. Hence, protection is necessary.

# BHASIA @BlackHatEvents

## Slide 65

#### Special Interfaces ： Flash 、 HDMI 、 DP 、 DAP 、 Ethernet 、 Recovery

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
ASIA 2024
Special Interfaces: Flash, HDMI, DP. aint Ethernet, Recovery —
O #iis_JTAG 5072 JiAG
flurix DAP cueol
furix OCOS
;3a559 Pets aaay
errr) Maas oo fl
```

## Slide 66

### Research on Other Related Peripherals -- CAN

Capture the Wakeup CAN signal

CAN BUS

MCU

CAN transceiver

Each controller has multiple CAN channels. One supports wake-up functionality, such as TJA1043.

CAN interface pins can be determined based on the CAN transceiver pinout. Some ADAS systems require CAN signals for wake-up, either any CAN signal or specific ID and data bits.

# BHASIA @BlackHatEvents

## Slide 67

### Research on Other Related Peripherals -- Lidar

- Automotive-grade LiDAR

- Uses Ethernet

- Automaker added 20 bytes of SOME/IP commands

- Reverse engineered automaker's driver to enable LiDAR hacking and use.

# BHASIA @BlackHatEvents

## Slide 68

Research on Other Related Peripherals -- Serializer/Deserializer

In the automotive field, image transmission does not use HDMI or DisplayPort, Use LVDS for data transmission and power supply.

Data transmission is carried out by calculating minor voltage changes. Technology: FPD-Link and GMSL

In the field of security: We can perform camera simulation injections and save on display screens (which are generally expensive).

Instrument display screen (currently has some color issues)

Camera Inject Device

# BHASIA @BlackHatEvents

## Slide 69

Risks

# BHASIA @BlackHatEvents

## Slide 70

### Firmware / Deploy Image / Development Document

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisekhat ‘
ASIA 2024
drwxr-xr-x. 3 root root
drwxr-xr-x. 3 root root
-rw-r—r—. 1 root root
1
re-T—T—. root root
drwxr-xr-x. 3 root root
-/persist/diff/base/local
total 24K
root root
root root
root root ug 5:13 pdeploy. json
root root 4.1K Aug 15:13 lList_of_files.json
root root
/base/Local
ec
o>
x x
root r t 4
root root
root root
root root 186K At : )_mce_flash_ol0_cr_prod_zerosign.bin
root root 1. g 5:13 mp_t234-TA977SA-Al_prod_zerosign.
root root 7K Aug lf 3 _5¢7_t234_prod_zerosign.bin
root root IK Aug 5:13 _rf_t234_prod_zerosign.bin
root root K At f 713 4 f_t2 zn. bin
root root 69 us 8 213 A_15_ 7ra234-bpmp-3898-0010-0000_zer
rw-r—-r-—-. root root 435 tl : camera-rtcpu-t2 rce-hv-sing m_zerosign.i
r
r
r
'w
w
w
w-
r-
r
r
r
root@tegra-ubuntu:/ota/update# 11
total 5.56
drwxr-xr-x. 3 root root 4.0K Jul 20
.dtb drwxr-xr-x. 6 root root 4.0K Jul 20
~rw-r--r--. 1 root root 5.5G Jul 20
rw-r—r-—-. root root 5K 3 : 7_ist_ucode_prod_zerosign.bin drwxr-xr-x. 4 root root 4.0K Jul 24
-rw-r—r-—. root root t :13 ; t_bpmp prod_zerosign.bin -rw-r--r-—-. 1 root root 4.1M Jul 2
-fw-r—r—. root root f } a 33 t ict zerosien.bin ~rwxrwxrwx. 1 root root 364 Jul 20 7:45 run.sh*
app d
appdata 9 BS) 8 md
applog BE diagcornengr a
bakdata E oO ™ diagmg@r ea md
#.... ° dilog cameraAcce
Readme. txt
« clude e m= mage
mapdata in execmar 8806113 3_ 202204 r flash_switch, sh
fault 8806113. V 20220404_(f r sdk_custom
```

## Slide 71

### Frameworks

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2024
Frameworks
20230217.160956 H vysfos)_mm
— oF
calib_camera_app
calib_camera_app_AS
ching
PH@@ r
FreeRunnine sformer data_buried_point
calib_mpd_diag
diag_proc_mpd
PHO@ —
dlerProxy ~
fusion_gtr
5 ta ; fusion_lane
ntegratedPositioning ial ner { | SS__PH@O f 2
onProces _PHOO dMiddLewareQh_PH¢ usion_pd
dTimeMonitor_PHO@ fusion_pse
fusion_psf
fusion_renv
fusion_se_gm =
motion control _app BehoviorP Lanni ngDDSApp motion_control_opp : ° ‘ Front tor config
motion_pLlancving app blackbox_app alibration Mot LonP LanningDDSApp ppt oader 6030_model.onnx
app_ihb ‘ Lot_detection ice aeing
pk_map_app €2 prepore_colibration_files servic zip_split.sh 6030_model.trt M
app_localization can_service l calib run_t
» bin
active _sofety_app ap 1sor_ fusion_app data_rec_synchromizer Og_manager sel f_calibration amera
behavior _planmming_app ourix utility d forwarder map manager on_app_ota i
ogmparam_ros.yaml
ogmparam.yaml
app “™ adas “7 adas-rt oa
TD app_param @ app_version deinit.sh A lib
™ backhaul deinit.sh hobot-adas-workflow.sh Ba ft t script
md nit.sh nit.sh @ (t_version "J fusion_se_re
By mnt Dy g_kerne! @@ log-udp-sender @ hobot-.
fusion_se_sef
userdata lost+for
log-udp-sender.json B inte
. fusion_se_tl
partstatus ntp * libe
trigger_module @ wate # libfacto fusion_tp
hdm adapter
```

## Slide 72

### TI / Nvidia / Horizon / Mobieye Model Files

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat “
ASIA 2024
TI / Nvidia / Horizon / Mobieye Model Files
oot@tegra-ubuntu:/app/package/202
otal 199M
2 root root 4.0K Nov
root root 4.0K Nov
root root 12M Nov
root root 8.1M Nov
root root 3.3M Nov
root root 11M Nov
root root 4.5M Nov
root root 5.0M Nov
root root 50M Nov
root root 6.2M Nov
root root 2.9M Nov
root root 37M Nov
root root 20M Nov
root root 11M Nov
root root 32M Nov
LM_v20220707_b1_best.plan
PLD_0611_fp16.plan
Speed_v20220710_sigmoid_dyn_fp16.plan
TSR_v20220707_b2_best.plan
avld_0701.plan
avod_infer_20220310_0516_crossid.plan
bevnet_merged_fp16_20220812.plan
dyreidcls.plan
fvModule_FVLane_best_GPU_20220829. plan
fvModule_FVOD_best_GPU sagem s]
fyModule_staticODdet “fp16. GPUs res
2 fyModule_trlclssify_fp16_DLAQ_ jammin
svModule_SVOD_best_GPU 8cls_ 736288. 1010.plan
@eooocoocoooooooeoooso S&S
KeyAlgorithms=+ssh-rsa -o PubkeyAcceptedKeyTypes=+ssh-rsc (base) + SV_project 11 configs/bev
total 20M
—rwx rwx r—x
—~TWXrwxr-x
zhxch zhxch 408 18
zhxch zhxch 354 18
zhxch zhxch 616 18
zhxch zhxch 576 18
zhxch zhxch 49 1B
zhxch zhxch 6.0M 15
zhxch zhxch 6.0M 1H
zhxch zhxch 4.1M 18
zhxch zhxch 4.1M 1H
cfg_fs_crop.json
cfg_fs.json
cfq_pld_crop.json
cfg_pld.json
d@m_version. txt
fs_crop.ann
fs.=mnn
pld_crop.ann
pld.mann
/models/pyramid_352_640_ fmt meee. hbr —PWX WX EX
—rwXx rwx r—x
—TWXTwxr—-x
‘res/hbrr ‘ action. hb —rwx wx r=x
res/hbmr .@/model_opt_3.hbm Bite elles
—TwxXrwxr-x
—TWXrwx rx
PRR RRR RRR
etection.hbm
```

## Slide 73

### Model Configuration, Raw Model

Convenient model invocation, training, and fine-tuning

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
ASIA 2024
Model Configuration,
“type”: "M
“value”:
{
\
Convenient
Raw Model
models
nhew_parking_0328_2_ 896.engine
328_2_896.0nnx
new_parking_O
orin_output_fisheye_0411_dynamic.engine
orin_output_fisheye_0411_dynamic.onnx
out 329_0_640.engine
0_640.0nnx
calpara txt
camera
camera_configure_cient.yrr
camera_configure_server ymi
Lut.bin
= release_classType_orin json
GE PROJECT_VERSION
model invocation, training, and fine-tuning
2024/3/10 EF 4:32
19KB JSON
```

## Slide 74

### Deployment of AI Models on Vehicles

**AI Compute Center Training**

**Technical Roadmap**

**Labeled Data**

Model output consumes significant computational and data resources, with extensive post-optimization iterations. Needs to be protected

**Inference Model**

**OTA**

Quantization and Optimization

**Continuous Road Testing Case Optimization**

**Model For Board Deployed**

As a security researcher, you can now move beyond using YOLO for model adversarial research(GAN) and paper writing, as you have access to real models.

# BHASIA @BlackHatEvents

## Slide 75

### Security Analysis of Model Files

The model file contains the model structure and parameter information

- Model structure is very important as it forms the basis of good results.

- .onnx .pt are original models, FP32, convenient for training and tuning.

- .hbm .trt .engine .bin are quantized models, INT8, suitable for inference on devices with low computing power.

**.onnx .trt/.plan**

Conclusion:

- Do not deploy/store .onnx models in vehicles, it's dangerous.

- Quantized models like .trt can be directly used for inference.

- Model structure analysis is also possible.

# BHASIA @BlackHatEvents

## Slide 76

### Analysis and Reconstruction of Model Files

###### Bevnet.onnx

+0 First 4 bytes are file magic, ptrt, ftrt

- +8 Serialized version number, 0xd5, 0xcd, 0xe8

- +0x10 Model data size

+0x18 Serialized data, TRT defines multiple tags, decoded with hardcoding

Reverse engineering on libnvinfer.so.8 using Frida hooks

# BHASIA @BlackHatEvents

## Slide 77

### Analysis and Reconstruction of Model Files

Compile the LeNet model using TensorRT and parse it with our script. Compared to the original model, the structure is similar,

Parse the acquired model.

Multiple tasks and output shapes.

some layers merged and optimized.

# BHASIA @BlackHatEvents

## Slide 78

### Analysis and Reconstruction of Model Files

##### model.hbm:

Reverse engineer hxxx-disas and hxxx-sim processes.

The first line :magic number; 'X2A' indicates that the following model instructions are for X2A. Other instructions, such as X2, B25, etc.

- X2A BERNOULLI2

- X2 BERNOULLI

- B25 BAYES

The offset table starts at 0xB8, with one entry for each model, each entry occupying 8 bytes.

# BHASIA @BlackHatEvents

## Slide 79

### Analysis and Reconstruction of Model Files

Use Frida for reverse engineering. detection_segment_0 contains instruction information.

Starting at 0x472E0, each instruction is 8 bytes, such as some convolution operations, which are accelerated in the BPU.

# BHASIA @BlackHatEvents

## Slide 80

#### Demo ： A Toy Car Utilizing An Automotive-grade AI Recognition Model

# BHASIA @BlackHatEvents

A $50 miniature car, with a NPU .

We extracted a set of models from the ADAS controller

And deployed them on the miniature car.

Now it's worth $500

## Slide 81

### About TC3XX MCU

TriCore TC3xx or RH850 Almost all controllers contain the TC397 and TC399. In ADAS, Gateway, T-Box, IVI, VCU, other controllers

Why?

- Supports ASIL-D safety requirements. So it can send CAN signals.

- Lockstep cores, ECC protection for instructions and data.

- Ethernet, FlexRay, CAN-FD, LIN, SPI.

- In ADAS：

Arbitration CAN/FlexRay Steer-by-wire Fault diagnosis Power management Ultrasonic radar MCU TC397 CAN Transceiver

# BHASIA @BlackHatEvents

## Slide 82

### TC397 Firmware Analysis

- Many systems contain MCU firmware files, even with .elf symbol files.

- Ghidra can perform reverse analysis!

- MCU firmware is readable! Only a few automakers set read protection,

- typically protecting only a few blocks.

- Every ADAS circuit board has DAP read pins.

- We specifically designed a core board reader that can remove the MCU,

- solder, and perform firmware reading, debugging, and signal analysis.

# BHASIA @BlackHatEvents

## Slide 83

### Reverse Engineering of TC397 Firmware

- Ghidra can analyze TriCore hex firmware.

- Analyzing MCU firmware primarily to understand CAN

   - control logic better. Because SoC cannot directly send CAN.

- Identify key functions in the MCU to confirm corresponding vehicle control interfaces in the SoC.

Since all controllers have the TC397 MCU, this is a very good research direction:

- Analyze the security of basic modules in AUTOSAR (especially the network modules).

- Examine TriCore's security mechanisms (such as encryption, protection), and whether they can be bypassed.

UDP receive function

# BHASIA @BlackHatEvents

## Slide 84

### How to Control

# BHASIA @BlackHatEvents

## Slide 85

### Ultimate Goal : Achieving Vehicle Control

Achieving vehicle control is the ultimate goal in researching ADAS controllers.

We need to:

- Understand the hardware architecture, workflow, and security risks of ADAS controllers.

- Understand the principles of vehicle control and control signals.

- Learn how to achieve complete remote vehicle control, including gaining access to the vehicle network and ADAS device permissions.

Note: Due to the significant impact of related vulnerabilities, we will not

demonstrate vehicle control in this talk .

Mainly: to popularize knowledge and security risks related to ADAS controllers.

# BHASIA @BlackHatEvents

## Slide 86

#### Wire-controlled Chassis Technology

T-Box

ADAS

IVI

GW

VCU ECU1 ECU2

Driver ECU ADAS

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2024
Steering by Wire System
Wire-controlled Chassis Technology g”"" ‘gg
Steering gear
Steering wheel
Driver wr
Ken of apas (i
=~
```

## Slide 87

### How to Control a Vehicle

Control the car's throttle, steering, and brakes through electronic signals (CAN).

T-Box IVI

GW

ADAS

How to control the vehicle:

- Directly control the ECU (very difficult, as the ECU has no operating system and no attack entry points)

- Directly control Assisted driving module, gateway and VCU (challenging, as most lack an operating system and ETH network interface)

- Control the autonomous driving domain controller.

VCU

ECU1 ECU2

# BHASIA @BlackHatEvents

## Slide 88

#### How to Control a Vehicle -- Controlling the Gateway

Some vehicles with autonomous driving features have complex gateway module:

- An onboard CPU with a full Linux system and multiple network ports.

- Functions include CAN signal control, DoIP diagnostic services, OTA services, and Ethernet switch.

- Gaining shell access to the gateway allows full control over the vehicle.

Limitations:

Advanced gateways like these are rare. Controlling the vehicle requires detailed analysis of lowlevel CAN messages.

# BHASIA @BlackHatEvents

## Slide 89

How to Control a Vehicle – Controlling the Assisted Driving Module

Early assisted driving cars, such as those with lane-keeping functions, use the Mobileye Q4M chip.

Although steering can be controlled via electronic signals, the limitations include:

- Only having a CAN interface.

- A simple operating system on FPGA, without networking capabilities.

These factors make it impossible to access assisted driving devices over the network, exploit vulnerabilities, and gain device permissions.

Unable to control the vehicle.

# BHASIA @BlackHatEvents

## Slide 90

How to Control a Vehicle – Controlling the ADAS

A complete computer (usually running Linux) with network connectivity:

- Various interfaces, including camera, network, and debugging interfaces.

- AI inference capabilities with substantial computational power.

- Connected to the powertrain CAN and chassis CAN, it can control the vehicle's throttle, brakes, and steering wheel.

- How can one achieve vehicle control?

- First, gain control of the ADAS. Invoke relevant APIs.

- Trigger the MCU to send control CAN signals.

# BHASIA @BlackHatEvents

## Slide 91

Linux / QNX
Cameras
Soc Orin-X Perception
Control
Android on QNX 4/5G module
Display Internet
CAN MCU TC397
ADAS CAN IVI CAN T-Box
Chassis/Powertrain CAN Info CA N Telemati c s CAN
CAN CAN CA N CA N
Eth Switch
VCU CAN CAN GW
Diag CAN Body CAN
ECUs
CAN CAN
Auto AC Door
DoIP
OBD Body electronics
# BHASIA @BlackHatEvents

## Slide 92

Linux / QNX
Cameras
Soc Orin-X Perception
Control
4/5G module
Internet
CAN MCU TC397
ADAS
T-Box
Chassis/Powertrain CAN
CAN CAN
Eth Switch
VCU GW
ECUs T-Box module is the sole remote attack entry point. Contains many vulnerabilities.
Control gateway can manage the vehicle, but some gateways lack Linux system,
only have MCU. Analyzing underlying CAN signals is challenging.
Gain network access through T-Box vulnerabilities, control ADAS devices, then use
upper-level API to control the vehicle, which is easy and universal.

# BHASIA @BlackHatEvents

## Slide 93

### The Way to Control the Vehicle

- Dismantle and analyze the entire vehicle, or ADAS and T-Box components.

- Identify T-Box vulnerabilities to access ADAS network.

- Acquire ADAS shell.

- Analyze ADAS listening processes to detect vulnerabilities.

- Analyze vehicle control processes.

- Analyze MCU firmware.

- Locate Control API/IPC topic/send SPI/send TCP UDP to enable MCU to send control CAN.

- Utilize remote exploits via Fake 2G Base station / PrivateAPN / Hacked Femtocell / IPV6….

Typically, ADAS devices do not have firewalls set up.

We discovered a command injection vulnerability in a 4G baseband module, a simple vul, have fixed years ago.

# BHASIA @BlackHatEvents

## Slide 94

### The Way to Control the Vehicle

USRP Min i/ Raspberry Pi YateBTS

Downgrade to 2G, no need auth, GPRS

Access IP 10.1.2.3

T-Box / 4G module

Vulnerability, getshell, Access the network Access ADAS

Switch

Gateway

Send control CAN data

ADAS

Vulnerability, getshell, send control APIs

Other ways: IPV6 -> IVI - ADAS WIFI -> IVI – ADAS IVI( 4/5G on IVI board) -> ADAS T-Box -> Gateway Linux system get shell T-Box -> ADAS -> Flash MCU firmware

Server Web -> OTA services -> Deploy signed upgrade pkgs

# BHASIA @BlackHatEvents

## Slide 95

Summary

ADAS controllers can control vehicles, so their security needs to be enhanced. Our research shows that most ADAS controllers have poor security.

To automakers:

- Disk encryption, model protection, disable services like SSH, secure listening processes, enable firewalls, MCU firmware read protection, enhance T-Box entry protection.

- To security researchers:

- Master new tools and concepts, such as dumping UFS storage, debugging and analyzing MCUs, using vehicle Ethernet and CAN-FD devices.

- Research on adversarial modeling using real vehicle models.

- Security analysis of MCUs like TC397.

- Security analysis of Nvidia DriveOS, including TrustZone, Secure Boot, Disk Encryption, Secure Storage, and firmware flashing bypass after FUSE blow. # BHASIA @BlackHatEvents

# BHASIA @BlackHatEvents
