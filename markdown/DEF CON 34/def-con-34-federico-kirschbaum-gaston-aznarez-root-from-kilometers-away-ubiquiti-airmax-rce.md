---
title: "Root From Kilometers Away Ubiquiti AirMax RCE"
speakers: ["Federico Kirschbaum", "Gaston Aznarez"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: 2026
source_pdf: "DEF CON 34/DEF CON 34 - Federico Kirschbaum, Gaston Aznarez - Root From Kilometers Away Ubiquiti AirMax RCE.pdf"
pages: 62
sha256: "1491b6bd6cb672d8174cf355d2d570b6345d5a61a91d712ca36cb4051f13f1fe"
text_chars: 20105
ocr_pages: 23
has_ocr: true
redacted_secrets: 0
ocr_confidence: 85.6
ocr_unreliable_blocks: 2
vision_verified_pages_changed: 42
vision_verified_pages: 62
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:27:25Z"
---
# Root From Kilometers Away Ubiquiti AirMax RCE

**Speakers:** Federico Kirschbaum, Gaston Aznarez  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Federico Kirschbaum, Gaston Aznarez - Root From Kilometers Away Ubiquiti AirMax RCE.pdf` (62 pages)


## Slide 1

# ROOT FROM KILOMETERS AWAY

###### Ubiquiti AirMax RCE

1

## Slide 2

#### WHO ARE WE?

**Gaston Aznarez** Principal Security Researcher Faraday Security

**Federico Kirschbaum** Co-Founder Faraday Security Head Of Security Lab XBOW

2

## Slide 3

# HOW DID THIS STARTED?

3

## Slide 4

### HOW DID THIS STARTED?

○ Obsession? You think?

```text
LU1AQS
Aparecen por todos lados  16:35
Once you see them  16:36

LU1AQS
December 11, 2025
13:30

LU1AQS
Está era la del jueves
Jajajajaja
20:23
Si te sirve de consuelo  20:55

LU1AQS
De una, nos vemos  10:08
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
14:48   14:48   14:48   + 16
```

4

## Slide 5

### HOW DID THIS STARTED?

○ Obsession? You think?

I SEE THEM

THEY ARE EVERYWHERE

imgflip.com

```text
LU1AQS
Aparecen por todos lados  16:35
Once you see them  16:36

LU1AQS
De una, nos vemos  10:08

LU1AQS
September 8, 2025
14:56
September 9, 2025
14:48   14:48   14:48   + 16
```

5

## Slide 6

###### THEY ACTUALLY ARE

**About Ubiquiti Networks**

Ubiquiti Networks, Inc. (Nasdaq: UBNT) eliminates barriers to connectivity for under-networked enterprises, communities and consumers with its leading-edge platforms that connect hundreds of millions of people throughout the world. **With over 60 million devices sold worldwide,** through a network of over 100 distributors, to customers in **more than 180 countries and territories,** Ubiquiti has maintained an industry-leading financial profile by leveraging a unique business model to develop products that combine innovative technology with disruptive price-to-performance characteristics.  Our growth is supported by the Ubiquiti Community, a global grass-roots community of 4 million entrepreneurial operators and systems integrators who engage in thousands of forums.  For more information, join our community at http://www.ubnt.com.

Ubiquiti, Ubiquiti Networks, the U logo, UBNT, airMAX, UniFi, airFiber, mFi, EdgeMAX and AmpliFi are registered trademarks or trademarks of Ubiquiti Networks, Inc. in the United States and other countries.

2017

6

## Slide 7

###### THEY ACTUALLY ARE

**Success in Initial Target Market Demonstrated Power of Our Business Model**

- Targeted and transformed wireless broadband in underserved markets

- Superior product at disruptive price

- Shipped **37+ million airMAX®** units to ~60 countries (life-to-date)

**Built $2B airMAX® business**

Copyright © Ubiquiti Networks, Inc. 2017    8

7

## Slide 8

##### WHAT THAT ANTENNAS ARE USED FOR?

**Technology**

Based on IEEE 802.11
Unlicensed spectrum: primarily 2.4 GHz and 5 GHz, 60Ghz

**Network Topologies**

Point-to-Point (PtP)
Point-to-Multipoint (PtMP)

**Common Uses**

Wireless Internet service providers (WISPs)
Public and municipal CCTV
Critical-infrastructure connectivity
Industrial and utility networks
Rural broadband and remote-site access

PTP

PTMP

8

## Slide 9

##### WE DID WHAT EVERYONE WOULD DO… WE FOUND SOME ANTENNAS

Litebeam 5ac gen2

NanoBeam M5

9

## Slide 10

###### WE COULDN’T CONNECT TO THE WI-FI

```text
Networks

Saved

faraday_poc
Saved / Connection failure

Saved
```

10

## Slide 11

# NOW WHAT?

11

## Slide 12

###### GETTING A SHELL INTO THE ANTENNA

```text
   KM                       ,ok0KNWW
         KM               :NMMMMMMMM
       KM  ..             WMMMMMMMMM
   KM      KM             WMMMMMMMMM
   KM    KM               WMMMMMMMMM
   KM  KM  ..             WMMMMMMMMM
   KM  ..  KM             WMMMMMMMMM
   KM  KM  KM             WMMMMMMMMM
   KMNXWM  KM             WMMMMMMMMK
   KMMMMMKONM             WMMMMMMMW
   KMMMMMMMMM             WMMMMMMM x
   lMMMMMMMMM             WMMMMMN xK
    MMMMMMMMMl           ,WMMMP dXM:
    lMMMMMMMMx .        ,,,aaadXMMd
     lNMMMMMMW: XOxolcclodOKMMMMWc
       lXMMMMMNc lMMMMMMMMMMMMNo.
         llONMMM0c lMMMMMMNOo'
              'lMN;. lMWl'
```

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

```text
BusyBox v1.24.2 (2025-08-22 19:57:45 EEST) built-in shell (ash)
Enter 'help' for a list of built-in commands.

XW.v6.3.22# uname -a
Linux NanoBeam M5 16 2.6.32.71 #1 Fri Aug 22 20:05:15 EEST 2025 mips GNU/Linux
XW.v6.3.22# id
uid=0(ubnt) gid=0(admin) groups=0(admin)
XW.v6.3.22#
```

That was easy, too easy

12

## Slide 13

#### WHAT **AIRMAX** IS?

airMAX®
Timeline
Time Slot 1
Time Slot 2
Time Slot 3
Time Slot 4
Time Slots
VOIP
Data
VOIP
VOIP
Packet Prioritization

Now we know is a protocol and not a **shoe**

13

## Slide 14

#### SO, WHERE IS IT IMPLEMENTED?

###### **Difference in the hardware?**

- No, it’s a normal Atheros Chipset

```text
XW.v6.3.22# dmesg | grep Atheros
[   12.462000] ath_rate_atheros: Copyright (c) 2001-2005 Atheros Co
[   12.908000] ath_dev: Copyright (c) 2001-2007 Atheros Communicati
[   12.951000] Copyright (c) 2005-2006 Atheros Communications, Inc.
[   13.467000] ath_ahb: 9.2.0_U11.14 (Atheros/multi-bss)
[   13.636000] wifi0: Atheros 9340: mem=0xb8100000, irq=2
```

###### **Difference in the software?**

- We can install OpenWRT and it will work as a regular Wi-Fi card (No-Airmax)

- It has custom versions of the drivers

- Probably even custom firmware

```text
  _______                     ________        __
 |       |.-----.-----.-----.|  |  |  |.----.|  |_
 |   -   ||  _  |  -__|     ||  |  |  ||   _||   _|
 |_______||   __|_____|__|__||________||__|  |____|
          |__| W I R E L E S S   F R E E D O M
 -----------------------------------------------------
 OpenWrt 24.10.4, r28959-29397011cc
 -----------------------------------------------------

root@OpenWrt:~#
```

THE DIFFERENCE IS IN THE SOFTWARE

14

## Slide 15

# WHAT REALLY IS **AIRMAX**

15

## Slide 16

#### TDMA PROTOCOLS

**Time Division Multiple Access**. Everyone shares one frequency. So the base station gives each client its own time slot. They take turns, in a repeating cycle.

###### **AirMAX is a protocol and implements TDMA on top of 802.11**

airMAX®
Timeline
Time Slot 1
Time Slot 2
Time Slot 3
Time Slot 4
Time Slots
VOIP
Data
VOIP
VOIP
Packet Prioritization

16

## Slide 17

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

17

## Slide 18

#### WI-FI TDMA HISTORY (WITH CHEAP HARDWARE)

**…**

Before Atheros

- Every Wi-Fi chipset locks radio control
- vendors keep the HAL closed

**2006**

Atheros and the Open source drivers

- MadWiFi (2003)
- ath5k (2007)
- ath9k (2008)

**2009**

FreeBSD TDMA Implementation

- Proves deterministic time-slots are possible on commodity Wi-Fi silicon

**2010**

All the Vendors

- Atheros ships one SDK
- Each adds only a thin proprietary TDMA layer
- Linux 2.6 becomes the kernel everyone freezes on

**Today**

We are in the same point

- Millions of radios still on kernel 2.6.32 (EOL Feb 2016)
- The protocols are undocumented and unresearched

18

## Slide 19

###### THE WORKHORSE OF TDMA OVER 802.11

- Control frame
  - Header
  - Body
    - Vendor Specific Information Elem.
      - DATA
  - Trailer

19

## Slide 20

# HOW AIRMAX IS IMPLEMENTED

20

## Slide 21

###### IT WORKS LIKE A NORMAL IEEE 802.11 WIFI

- Broadcast & Probing
- Open System Auth. and Assoc
- 4-Way Handshake
- Scheduling?

| Source | Destination | Info |
| --- | --- | --- |
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
| Ubiquiti_c4:67:fd | Ubiquiti_be:fa:3a | Action, SN=2092, FN=0, |
| Ubiquiti_be:fa:3a | Ubiquiti_c4:67:fd | Action, SN=3359, FN=0, |
| Ubiquiti_c4:67:fd | Ubiquiti_be:fa:3a | Action, SN=2093, FN=0, |
| Ubiquiti_be:fa:3a | Ubiquiti_c4:67:fd | Action, SN=3360, FN=0, |
| Ubiquiti_c4:67:fd | Ubiquiti_be:fa:3a | Action, SN=2094, FN=0, |
| Ubiquiti_be:fa:3a | Ubiquiti_c4:67:fd | Action, SN=3361, FN=0, |

What we expect from WIFI

21

## Slide 22

###### TDMA IMPLEMENTATION OVER IEEE 802.11

Vendor Specific Information Element with AirMAX enabled

- OUI: 00:0C:42 -> Device name

- OUI: 00:15:6D

- OUI: 00:27:22

I'LL SEE

```text
 397 Beacon frame, SN=1515, FN=0, Flags=........C, BI=100, SSID="Comodoro"
```

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
       Subdata: 000000001f660902ff0f4c6176616c6c65202d20507900000000000000
       Subtype 1 Prefix: 000000001f660902ff0f
       Subtype 1 Data: Lavalle - Py
```

```text
0050  64 6f 72 6f 01 08 8c 12   98 24 b0 48 60 6c 03 01   doro.... .$.H`l..
0060  a5 05 04 00 01 00 00 07   06 42 5a 20 95 11 1e 20   ........ .BZ ...
0070  01 03 30 14 01 00 00 0f   ac 04 01 00 00 0f ac 04   ..0..... ........
0080  01 00 00 0f ac 02 00 00   2d 1a ad 01 03 ff ff 00   ........ -.......
0090  00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00   ........ ........
00a0  00 00 00 00 3d 16 a5 08   00 00 00 00 00 00 00 00   ....=... ........
00b0  00 00 00 00 00 00 00 00   00 00 00 00 dd 18 00 50   ........ .......P
00c0  f2 02 01 01 85 00 03 a4   00 00 27 a4 00 00 42 43   ........ ..'...BC
00d0  5e 00 62 32 2f 00 dd 1e   00 90 4c 33 ad 01 03 ff   ^.b2/... ..L3....
00e0  ff 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00   ........ ........
00f0  00 00 00 00 00 00 dd 1a   00 90 4c 34 a5 08 00 00   ........ ..L4....
0100  00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00   ........ ........
0110  00 00 dd 09 00 03 7f 01   01 00 00 ff 7f dd 0a 00   ........ ........
0120  03 7f 04 01 00 02 00 0a   00 dd 0e 00 15 6d 00 00   ........ .....m..
0130  00 01 02 b5 e6 02 02 02   00 dd 26 00 0c 42 00 00   ........ ..&..B..
0140  00 01 1e 00 00 00 00 1f   66 09 02 ff 0f 4c 61 76   ........ f....Lav
0150  61 6c 6c 65 20 2d 20 50   79 00 00 00 00 00 00 00   alle - P y.......
0160  00 dd 26 00 15 6d ff ff   ff 4b 05 cc 83 d8 2e be   ..&..m.. .K......
0170  20 5e 8d a4 cf e2 d3 dc   7f dc 97 0c 69 81 eb 61    ^...... ....i..a
0180  a0 da 44 93 99 71 56 1b   bc 3a 4b 6e 66            ..D..qV. .:Knf
```

22

## Slide 23

###### TDMA IMPLEMENTATION OVER IEEE 802.11

AirMAX AC

- Control frame
  - Header
  - Body
    - Ubiquiti IE
      - OUI: 00:27:22
      - DATA
  - Trailer

AirMAX M

- Control frame
  - Header
  - Body
    - RouterBoard IE
      - OUI: 00:0c:42
      - Device Name
    - Ubiquiti IE
      - OUI: 00:15:6D
      - DATA
  - Trailer

Encrypted ??

23

## Slide 24

###### WE STARTED REVERSE ENGINEERING

```text
afree_private
amalloc_private

asf_print_category_private

afree_private
amalloc_private

ath_dfs_prescan

gpio_line_config
gpio_line_set

ubnt_poll_host

ath_dfs_prescan_register
ath_dfs_prescan_unregister

afree_private
amalloc_private

afree_private
amalloc_private
asf_print_ctrl_register_private
asf_print_ctrl_unregister_private
asf_print_mask_set
... (+1 more)

ath_hook_host_register
ath_kickout_node_notify
ieee80211_find_node
ieee80211_free_node
ieee80211_indicate_node_assoc
... (+5 more)

asf

ath_dfs

board_identify
ubnthal_get_radio_cap

afree_private
amalloc_private

ath_process_spectraldata
is_spectral_phyerr
spectral_attach
spectral_check_hw_capability
spectral_control
... (+7 more)

ath_dfs_module_locked
ath_dfs_register
ath_dfs_unregister

g_pktlog_funcs

ath_spectral

ath_dev

spectral_attach
spectral_check_hw_capability
spectral_control
spectral_detach
spectral_process_phyerr
... (+1 more)

ACBEMinfree
ACBKMinfree
ACVIMinfree
ACVOMinfree
CABMinfree
... (+20 more)

afree_private
amalloc_private
asf_amem_create
asf_amem_destroy
asf_amem_setup
... (+5 more)

afree_private
amalloc_private

gpio_int_disable
gpio_int_enable
gpio_int_init
gpio_int_uninit

board_identify
gpio_line_config
gpio_line_get
gpio_line_set
ubnthal_get_eeprom_data
... (+11 more)

ath_get_tx_chainmask
ath_rate_attach
ath_rate_create_vap
ath_rate_detach
ath_rate_findrate
... (+16 more)

ubnthal

_ath_hal_attach
ath_hal_computetxtime
ath_hal_detach
ath_hal_display_tpctables
ath_hal_enabledANI
... (+14 more)

umac

ath_get_softc

ath_pktlog

ubnt_eth_phy
ubnthal_get_eth_port_count

ar724x-eth

g_pktlog_refuncs

ubnthal_get_radio_cap

ieee80211_leds_register
ieee80211_leds_unregister

ath_hal_probe

ath_rate_atheros

ath_hal_get_device_info

ath_hal

adf_os_mem_zero_outline

adf_os_mem_alloc_outline
adf_os_mem_free_outline
adf_os_spin_lock_bh_outline
adf_os_spin_unlock_bh_outline

adf

urd_alpha2_to_countrycode
urd_find_countrycode
urd_intersect_domains
urt_count_group_countries

ath_hal_log_ani_callback_register

board_identify
gpio_led_set
led_blink_in_progress

urd_alpha2_to_countrycode
urd_find_countrycode
urd_intersect_domains
urt_count_group_countries

rssi-leds

urd
```

24

## Slide 25

###### IMPORTANT KERNEL MODULES

```text
afree_private
amalloc_private

ath_hal_set_config_param
ath_hal_reg_write
ath_hal_reg_read

ath_hal_probe
ath_hal_subVendorID

ieee80211_set_beacon_rx_vendor_ie_hook
ieee80211_set_assoc_req_tx_vendor_ie_hook
ieee80211_set_scan_hook
ieee80211_chan2mode
ieee80211_beacon_alloc
... (+20 more)

afree_private
amalloc_private

ath_hal

ath_hal_getChanNoise
ath_hal_computetxtime
ath_hal_get_device_info
ath_hal_set_config_param
ath_hal_mhz2ieee
... (+15 more)

ubnt_poll

asf

afree_private
amalloc_private
asf_amem_setup
asf_amem_destroy
asf_amem_create
... (+1 more)

umac

ath_iw_attach
CABMinfree
ACBKMinfree
wbuf_alloc
ath_cancel_timer
... (+17 more)

hook_ops
bus_dma_sync_single
ath_register_hook

afree_private
amalloc_private

ath_dev
```

**AirMAX core driver**

**Atheros drivers**

**MAC drivers**
**Modified version of Ath9k**

25

## Slide 26

###### HOW ARE THE IE BUILD

(AIR)

- 802.11 Management Frame

- RX
- TX

radio

- Radio Hardware + FirmW

Ath

- Ath Driver
  - Take from/hand to FW

Umac

- Umac Driver (802.11 MAC)
  - Parse mgmt
    - call Hook
  - Build mgmt
    - call Hook

Ubnt_poll

- Ctrl msg Hook (Rx)
  - Parse IE
- Ctrl msg Hook (Tx)
  - Insert IE

26

## Slide 27

###### ENCRYPTION? I DON’T THINK SO

```text
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

- dst mac
  - key
- Src mac
  - msg
- Hmac-sha1 ( key= dst mac , msg= Src mac)
- AES 128 Key
- IE Enc Data
- AES-128-EB decrypt
- Plain IE Data

Validated with **mtscan** by **Konrad Kosmatka**:

- github.com/kkonradpl/mtscan/

27

## Slide 28

###### ENCRYPTION? I DON’T THINK SO

Gaston Aznarez 11:58

```text
MAC Address: 44:d9:e7:6a:3a:43
AES Key (derived): ff1db564cf91b27557ff9343ed1d4d16 (16)

Decrypting
Encrypted data: ca 44 6d 0e 37 58 6f 21 62 e0 c5 18 27 b5 cf 37 b1 89 af 52 ca 0a c3 3c c2 13 4f 1b 6e 52 2d 76 (32)
[*] Cipher created
Decrypted data: 0f 01 44 d9 e7 6a 3a 43 01 00 00 00 00 00 00 00 0a 82 82 00 00 44 d9 e7 6a 3a 43 00 00 00 00 00

                     |_________  ______|
                               ||
                               \/
                               MAC
```

Parece que funciona je

Epico

Validated with **mtscan** by **Konrad Kosmatka**:

- github.com/kkonradpl/mtscan/

28

## Slide 29

## **RECON TIME**

29

## Slide 30

###### FINDING AIRMAX NETWORKS (in-the-wild)

30

## Slide 31

###### FINDING AIRMAX NETWORKS (in-the-wild)

Network Map

- **26** NETWORKS WITH LOCATION
- **26** ACCESS POINTS
- **0** STATIONS

Leaflet | © OpenStreetMap contributors

- Access Point
- Station
- Unknown Role

Fit All Markers

Done

31

## Slide 32

###### FINDING AIRMAX NETWORKS (in-the-wild)

**PTMP-CerritoYcordoba** AP

- **BSSID:** 78:8a:20:6c:bd:a9
- **Radio:** AP PTMP-CerritoYcordoba
- **Signal:** -86.4 dBm
- **Location:** Cerrito, Buenos Aires, AR
- **Coords:** -34.598949, -58.381916

32

## Slide 33

###### FINDING AIRMAX NETWORKS (in-the-wild)

**AirMAX Survey**

Network Analysis Tool

remoe_wireshark.pcapng

| NETWORKS | AIRMAX FRAMES | DECRYPTED | TOTAL PACKETS | ACCESS POINTS |
|---|---|---|---|---|
| 16 | 785 | 773 | 298156 | 754 |

**Discovered Networks** 16

| SSID | BSSID | RADIO NAME | DEVICE | FIRMWARE | TYPE | MODE | ROLE | CH | FREQ ↓ | SIGNAL | NOISE | SNR | AMQ | AMC |
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

33

## Slide 34

###### LET’S DO SOME TOOLS FOR THE COMMUNITY

###### Tools

- WireMAX - Wireshark dissector

- PyrMAX - Python package

- Web Platform

```text
ubnt_ac_multiple_reconnections.pcapng

Apply a display filter ... <⌘/>

No.    Time       Source             Destination        Protocol
1236   17.780235  Ubiquiti_c4:67:fd  Ubiquiti_be:fa:3a  802.11
1237   17.781692  Ubiquiti_be:fa:3a  Ubiquiti_c4:67:fd  802.11

AirMAX AC (Vendor Specific IE)
    OUI: 002722
    OUI Type: ffffff
  > Flags: 0x02
    Message Type: Assoc Req (2)
    Encrypted Length: 96
    Ciphertext: 10bde1f8661daf7a9ef185d0d19f7fc5de0306334ad67904308160a2e02ead
    [Decrypted payload (AES-128-ECB)]
        [AES Key (HMAC-SHA1(dst,src)[:16]): 3f8e721868280c93417170f2a71a568f  (d
        Version: 9
        Source MAC: Ubiquiti_be:fa:3a (1c:6a:1b:be:fa:3a)
        TX Chainmask: 3
        RX Chainmask: 3
        Capability Flags: 0x00000041
            .... .... .... .... .... .... .... 0... = chanbw mode: False
            .... .... .... .... .... .... ...0 .... = high density: False
            .... .... .... .... .... .... .1.. .... = auth-deauth capable: True
            .... .... .... .... .... .... 0... .... = 11ax-compat: False
        field_14 [open]: 0x00000000
        Radioname: LiteBeam 5AC
        SSID: FaradayLB
        TLV: Radioname (1), len 12
            Tag: Radioname (1)
            Length: 12
            Data: 4c6974654265616d20354143
      > TLV: SSID (2), len 9
        field_9c [open]: 0x7729d097
        RSSI (per-chain): 2c2d
        Firmware Name: WA.ar934x.v8.7.22.48486.260227.1

Ubiquiti AirMAX (airmax), 106 bytes        Packets: 15097        Profile: Default
```

34

## Slide 35

# HACKER DREAMS WITH OVER-THE-AIR EXPLOITS

35

## Slide 36

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

**fedek** 11:21 AM

Necesito más memcpy’s

IMG_7466

1 reply Today at 5:27 PM

**fedek**

Messages | Files | (evil)Doggie | +

November 13th, 2025

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

**fedek** 10:58 AM

🙄

**Gaston Aznarez** 10:58 AM

sospechoso (844 kB)

Latest messages

36

## Slide 37

###### THE VULNERABILITIES

CVEs:

- CVE-2026-21639

- CVE-2026-21638

###### Affected devices

(2.4, 5, 60 GHz):

- airMAX AC

- airMAX M

- airFiber AF60-XG

- airFiber AF60 (60GHz)

- UBB-XG

- UDB-Pro/UDB-Pro-Sector

- UBB

Criticality:

- Over-The-Air (line of sight)

- Unauthenticated

- RCE

- Kernel Privileges

CVSS limitations:

- 8.8 (high) for this adjacent bug (would 9.8 (critical) for LAN bugs)

**CVE-2026-21639 Detail**

**Description**

A malicious actor in Wi-Fi range of the affected product could leverage a vulnerability in the airMAX Wireless Protocol to achieve a remote code execution (RCE) within the affected product. Affected Products: airMAX AC (Version 8.7.20 and earlier) airMAX M (Version 6.3.22 and earlier) airFiber AF60-XG (Version 1.2.2 and earlier) airFiber AF60 (Version 2.6.7 and earlier) Mitigation: Update your airMAX AC to Version 8.7.21 or later. Update your airMAX M to Version 6.3.24 or later. Update your airFiber AF60-XG to Version 1.2.3 or later. Update your airFiber AF60 to Version 2.6.8 or later.

**CVE-2026-21638 Detail**

**Description**

A malicious actor in Wi-Fi range of the affected product could leverage a vulnerability in the airMAX Wireless Protocol to achieve a remote code execution (RCE) within the affected product. Affected Products: UBB-XG (Version 1.2.2 and earlier) UDB-Pro/UDB-Pro-Sector (Version 1.4.1 and earlier) UBB (Version 3.1.5 and earlier) Mitigation: Update your UBB-XG to Version 1.2.3 or later. Update your UDB-Pro/UDB-Pro-Sector to Version 1.4.2 or later. Update your UBB to Version 3.1.7 or later.

```text
Metrics    CVSS Version 4.0    CVSS Version 3.x    CVSS Version 2.0

NVD enrichment efforts reference publicly available information to associate vector strings. CVSS information contributed by other sources is also displayed.

CVSS 3.x Severity and Vector Strings:

NIST: NVD        Base Score: N/A        NVD assessment not yet provided.
CNA: HackerOne   Base Score: 8.8 HIGH   Vector: CVSS:3.1/AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
```

37

## Slide 38

DEMO 1

38

## Slide 39

###### THE IMPACT

###### Critical infrastructure:

- Critical infrastructure

- Buildings

- Public Safety CCTV

Military uses:

- hntrbrk research

39

## Slide 40

# BUG BOUNTY

40

## Slide 41

###### BUG BOUNTY TIMELINE

hackerone

Just **10** days for the first patch

| Nov 13 | Dec 1 | Dec 8 | Dec 11 | Dec 17 | Dec 22 | Feb 28 | Jan 6 |
|---|---|---|---|---|---|---|---|
| The bug was found | The vulnerability was reported | CVEs assigned<br>• CVE-2026-21638<br>• CVE-2026-21639 | First patch wave<br>• AirMAX M | Second patch wave<br>• AF60-HD/XG<br>• AF60/AF60-LR | Third patch wave<br>• UniFi Device/Building Bridge XG | Last patch wave<br>• AirMAX AC | Advisories published |

41

## Slide 42

###### BUG BOUNTY PAYMENT

- Top $8000 in LAN Networks

- Top $4000 in Adjacent

They pay more for a LAN Vuln than a Vulnerability that can be exploited from kilometers

**100 km**

```text
Capacity
149 Mbps
RF Noise
Noise Free

100.16 km

Product
LiteBeam ...
Height
239.38 m
-75 dBm
8X

Product
LiteBeam ...
Height
241.34 m
Expected Signal
1X          2X

LIDAR data is not available in this area.
© 2026 Ubiquiti Inc.
```

```text
Attack Vector (AV)

Network (N)    Adjacent (A)    Local (L)    Physical (P)

Attack Complexity (AC)

Low (L)    High (H)

Privileges Required (PR)

None (N)    Low (L)    High (H)
```

The vulnerable component is bound to the network stack, but the attack is limited at the protocol level to a logically adjacent topology. This can mean an attack must be launched from the same shared physical (e.g., Bluetooth or IEEE 802.11) or logical (e.g., local IP subnet) network, or from within a secure or otherwise limited administrative domain (e.g., MPLS, secure VPN to an administrative network zone).

**Payment Limits:**

Limits will be applied based on Attack Vector rules:

Limit 1 (Physical) = 1,000

Limit 2 (Local)= 2,500

Limit 3 (Adjacent)= 4,000

Limit 4 (LAN Side) = 8,000

Limit 5 (WAN Side) = 25,000

Limit 6 (Ubiquiti Cloud) = 30,000

42

## Slide 43

###### BUG BOUNTY PAYMENT

- Top $8000 in LAN Networks

- Top $4000 in Adjacent

They pay more for a LAN Vuln than a Vulnerability that can be exploited from kilometers

```text
4.2k
3.4k
2.5k
1.7k
840
0

1   2   3   4   5   6   7   8   9   10

f(10) = 4000
1,333
444
148
```

**Decrease Bounty Drivers:**

Privileges Required

High (Admin access, other than view/read-only access) = Base Score / 6

High (View/Read-only admin access) = Base Score / 4

Low (User without admin permissions) = Base Score / 2

**User Interaction:**

Required = Base Score / 4

**Rewarding Formula**

Base Formula: (3^(x,x-1))*(AV/(3^9))

Where "x,x" is the CVSS score and maximum bounty is AV limit USD

43

## Slide 44

###### BUG BOUNTY PAYMENT

- Top $8000 in LAN Networks

- Top $4000 in Adjacent

They pay more for a LAN Vuln than a Vulnerability that can be exploited from kilometers

```text
4.2k
3.4k
2.5k
1.7k
840
0

1   2   3   4   5   6   7   8   9   10

f(10) = 4000
1,333
444
148
```

**Decrease Bounty Drivers:**

Privileges Required

High (Admin access, other than view/read-only access) = Base Score / 6

High (View/Read-only admin access) = Base Score / 4

Low (User without admin permissions) = Base Score / 2

**User Interaction:**

Required = Base Score / 4

**Rewarding Formula**

Base Formula: (3^(x,x-1))*(AV/(3^9))

Where "x,x" is the CVSS score and maximum bounty is AV limit USD

44

## Slide 45

###### BUG BOUNTY PAYMENT

**5 GHz Wi-Fi DX record – Denmark logged in Poland @ 745 km**

ENGLISH TROPO WI-FI DX / 2020-08-15 / Przez Konrad / Jeden komentarz

A remarkable tropospheric ducting occurred on **August 11 and 12, 2020** between **Poland**, **Sweden** and **Denmark**. The propagation forecasts, which use color hue to scale their intensity, featured red shades over the Baltic Sea. Such a propagation strength is very rare, if ever seen on a forecast for this area. I was looking forward for something extraordinary, especially on the microwave bands. My stationary Wi-Fi DXing setup has been damaged three months ago. I could not miss such an opening, so a DX-pedition was the only option. In the evening of August 11 I made an opportunistic decision to visit the **Dylewska Góra** in north-eastern Poland. A few hours later, I was standing there with an antenna inside a lookout tower.

https://radiodx.pl/2020/08/5ghz-wifi-dx-record-denmark-logged-in-poland-745-km/

45

## Slide 46

###### POC FROM KILOMETERS AWAY

- Like master snake told us: When in danger, use a cardboard box

46

## Slide 47

###### POC FROM KILOMETERS AWAY

- We setup a vulnerable antenna in a cardboard box

- We setup an antenna in the building sending the exploit

- We started walking

47

## Slide 48

POC FROM KILOMETERS AWAY (At least a bit More)

- We setup a vulnerable antenna in a cardboard box

- We setup an antenna in the building sending the exploit

- We started walking

48

## Slide 49

POC FROM KILOMETERS AWAY v2

Measure distance
Click on the map to add to your path
Total distance: 1.72 km (1.07 mi)

49

## Slide 50

HOW WE COULD MAKE THIS BETTER? (WEAPONIZING)

50

## Slide 51

###### FINDING AIRMAX ANTENNAS

We capture beacon messages

```
❯ uv run python -m pyrmax discover ../../packets/ubnt_airmax_devices.pcapng

78:8a:20:1c:98:1b  (AC)
  radioname    'AP PTMP-CerritoYsarmiento'
  ssid         'PTMP-CerritoYsarmiento'
  ac_msg_types BEACON
  ac_version   8
  cap_flags    0x00000002
  mixed_mode   0
  frames       84
  first seen   1765842.012760
  last seen    1765842.718826
  peers        (broadcast only)

78:8a:20:6c:bd:a9  (AC)
  radioname    'AP PTMP-CerritoYcordoba'
  ssid         'PTMP-CerritoYcordoba'
  ac_msg_types BEACON
  ac_version   8
  cap_flags    0x00000002
  mixed_mode   0
  frames       5322
  first seen   1765834.576612
  last seen    1782250959.162468
  peers        (broadcast only)

78:8a:20:6c:bd:ad  (AC)
  radioname    'AP PTMP-CerritoYcorrientesOCA'
  ssid         'PTMP-CerritoYcorrientesOCA'
  ac_msg_types BEACON
  ac_version   8
  cap_flags    0x00000002
  mixed_mode   0
  frames       128
  first seen   1765841.895960
  last seen    1765842.709035
  peers        (broadcast only)
```

```
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
  > TLV: Radioname (1), len 23
  > TLV: SSID (2), len 20
  > TLV: Padding (0)
```

51

## Slide 52

###### FINGERPRINTING

We start the Open-System Auth. and Assoc because the FW version in sent on the IE (AirMAX AC > v9)

Message exchange between AP and STA:

- Probe Req - IE (STA → AP)
- Probe Resp - IE (AP → STA)
- Auth Req (STA → AP)
- Auth Res (AP → STA)
- Assoc Req - IE - FW (STA → AP)
- Assoc Res - IE - FW (AP → STA)

Firmware version

| No. | Time | Source | Destination | Info |
|-----|------|--------|-------------|------|
| 1 | 0.0000… | Ubiquiti_c4… | Broadcast | Beacon frame, SN=2748, FN= |
| 2 | 0.1027… | Ubiquiti_c4… | Broadcast | Beacon frame, SN=2751, FN= |
| 3 | 0.1476… | Ubiquiti_be… | Ubiquiti_c4… | Probe Request, SN=256, FN= |
| 4 | 0.1476… | Ubiquiti_c4… | Ubiquiti_be… | Probe Response, SN=2752, F |
| 7 | 0.1505… | Ubiquiti_be… | Ubiquiti_c4… | Association Request, SN=25 |
| 8 | 0.1520… | Ubiquiti_c4… | Ubiquiti_be… | Association Response, SN=2 |

```
> Frame 8: Packet, 265 bytes on wire (2120 bits), 265 bytes capture
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
    Ciphertext: f9a4c74cd7bd7b94cefb0ddd8af89c9493721794002e42b22950
  v [Decrypted payload (AES-128-ECB)]
      [AES Key (HMAC-SHA1(dst,src)[:16]): ce1f241d63112e4eee7244f36a
      Version: 9
      Source MAC: Ubiquiti_c4:67:fd (1c:6a:1b:c4:67:fd)
      ic_6b8 (chainmask pair): 0303
      sta_field_68 [open]: 0x338ef79d
      RSSI (per-chain): 2931
      Firmware Name: WA.ar934x.v8.7.22.48486.260227.1
      TX Power (half-dBm): 252
```

52

## Slide 53

###### SENDING THE EXPLOIT

We send the OTA exploit doing the following

- Change user name
- Change user password
- Change network password
- Run **ubntconf**

```
XW.v6.3.22# ubntconf -h
System configurator ubntconf
Copyright 2006-2025, Ubiquiti Inc. <support@ubnt.com>

This program is proprietary software; you can not redistribute it and/or modify
it without signed agreement with Ubiquiti Inc.

Usage: ubntconf [options]
        -c <config file>       - Configuration file to use. (Default: /tmp/system.cfg)
        -p <config file>       - Previuos config file to differ with file specified in
        -d <file name>         - File name for script generated from the diff. (Default
        -o <output directory>  - Directory to output scripts. (Default: /etc/sysinit)
        -i <symlink>           - Init and create symlink to default configuration file.
        -l <symlink>           - Create symlink to default configuration file and exit
        -f                     - Fix configuration from older version
        -h                     - This message.
```

```
XW.v6.3.22# cat /tmp/system.cfg | wc -l
158
XW.v6.3.22# head /tmp/system.cfg
aaa.1.br.devname=br0
aaa.1.devname=ath0
aaa.1.driver=madwifi
aaa.1.radius.acct.1.status=disabled
aaa.1.radius.auth.1.status=disabled
aaa.1.radius.macacl.status=disabled
aaa.1.ssid=faraday_poc
aaa.1.status=enabled
aaa.1.wpa.1.pairwise=CCMP
aaa.1.wpa.key.1.mgmt=WPA-PSK
XW.v6.3.22# grep "user" /tmp/system.cfg
users.1.name=ubnt
users.1.password=$6$d3ikJurm4EwrGqLu$jZZ/8CWXify1
users.1.status=enabled
users.status=enabled
XW.v6.3.22# grep "wpas" /tmp/system.cfg
wpasupplicant.device.1.status=disabled
wpasupplicant.profile.1.network.1.psk=noteladigo
wpasupplicant.status=disabled
```

53

## Slide 54

###### POST EXPLOITATION - PERSISTENCE

**/tmp/system.cfg** is a temporary file!

- Connect to the WiFi with the new password
- Restore the configuration
- Backdoor
  - Create a new user
  - Apply configuration
- Obtain old network password

```
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

```
XW.v6.3.22# cp /tmp/running.cfg /tmp/system.cfg
XW.v6.3.22# printf 'users.2.status=enabled\nusers.2.name=tant
rd=$1$22gbrWP0$g10WRWHWaogUojRyzllw4.\n' >> /tmp/system.cfg
XW.v6.3.22# /usr/etc/rc.d/rc.softrestart
Usage: /usr/etc/rc.d/rc.softrestart (force|test|save)
XW.v6.3.22# /usr/etc/rc.d/rc.softrestart save
--- /tmp/.running.cfg.1236
+++ /tmp/.system.cfg.1236
@@ -129,6 +129,9 @@
 users.1.name=ubnt
 users.1.password=$6$d3ikJurm4EwrGqLu$jZZ/8CWXify168Mgvu1AVD
 users.1.status=enabled
+users.2.name=tantrum
+users.2.password=$1$22gbrWP0$g10WRWHWaogUojRyzllw4.
+users.2.status=enabled
 users.status=enabled
 vlan.status=disabled
 wireless.1.addmtikie=enabled
Fast users script build Success.
Fixup Startup_list ...Done.
XW.v6.3.22# exit

Please press Enter to activate this console.

NanoBeam M5 16 login: tantrum
Password:
    KM                      ,ok0KNWW
```

54

## Slide 55

ALL TOGETHER - DEMO 2

55

## Slide 56

# WE ARE IN, NOW WHAT?

56

## Slide 57

###### FINDING ANOTHER DEVICES

```
XW.v6.3.22# ubntbox discover
Hardware Address    IP address              Name
78:8A:20:A2:42:97  192.168.37.103  NanoBeam M5 16 'NanoBeam M5 16'
F0:9F:C2:C8:F0:AD  192.168.37.104  UAP-AC-Pro-Gen2 'Piaget AP'
44:D9:E7:6A:3A:43  192.168.37.102  NanoBeam M5 16 'NanoBeam M5 16'
1C:6A:1B:C4:67:FD  192.168.37.100  LiteBeam 5AC 'FaradayLB2'
Total: 4 devices.
```

CVE-2026-21633 Detail

Description

A malicious actor with access to the adjacent network could obtain unauthorized access to a UniFi Protect Camera by exploiting a discovery protocol vulnerability in the Unifi Protect Application (Version 6.1.79 and earlier). Affected Products: UniFi Protect Application (Version 6.1.79 and earlier). Mitigation: Update your UniFi Protect Application to Version 6.2.72 or later.

Metrics: CVSS Version 4.0 | CVSS Version 3.x | CVSS Version 2.0

NVD enrichment efforts reference publicly available information to associate vector strings. CVSS information contributed by other sources is also displayed.

CVSS 3.x Severity and Vector Strings:

NIST: NVD - Base Score: N/A - NVD assessment not yet provided.
CNA: HackerOne - Base Score: 8.8 HIGH - Vector: CVSS:3.1/AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H

57

## Slide 58

###### PIVOTING TO THE CLOUD

[ REDACTED ]

58

## Slide 59

# CONCLUSIONS & TAKEAWAYS

59

## Slide 60

###### WHAT WE FOUND

###### Curiosity → kernel RCE. That's the whole path

- Curiosity. We just bought the devices.

- Linux 2.6.32, compiled in 2009, still shipping today

- Found where the proprietary protocol lives: 802.11 IEs that look encrypted

- Reverse engineered the protocol, AirOS, the kernel modules

- Two bugs. Present since inception.

- Exploited them over the air, from kilometers. No network. No credentials.

60

## Slide 61

###### TEN YEARS, NOBODY LOOKED

###### Or nobody said it.

- On rooftops around the world. Towns, ISPs, even at a front line.

- Vulnerable since inception. Public bounty program the whole time.

- We did it in nine months, with curiosity

- Rated Adjacent → exploited from kilometers away

- CVSS has no vocabulary for line of sight

61

## Slide 62

# THANKS FOR YOUR TIME

##### QUESTIONS?

WireMAX

###### PyRMAX

Gaston Aznarez:     𝕏 @GastonAznarez   [ln] gastonaznarez

Fede Kirschbaum:   𝕏 @fede_k                 [ln] fedek

62

