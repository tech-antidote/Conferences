---
title: "Root From Kilometers Away Ubiquiti AirMax RCE"
speakers: ["Federico Kirschbaum", "Gaston Aznarez"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: null
source_pdf: "DEF CON 34/DEF CON 34 - Federico Kirschbaum, Gaston Aznarez - Root From Kilometers Away Ubiquiti AirMax RCE.pdf"
pages: 62
sha256: "1491b6bd6cb672d8174cf355d2d570b6345d5a61a91d712ca36cb4051f13f1fe"
text_chars: 22606
ocr_pages: 23
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:17:25Z"
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

○ Obsession? You think?

### HOW DID THIS STARTED?

4

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
HOW DID THIS STARTED? = Qbsession? You
Ve UNG, Vs VEIIVS 19:98 W/
September 1, 2025
September 8, 2025
€ A LU1AQS or °
December 11, 2025 <€ A LU1AQS Ck
Esta era la del jueves
REIEIEIEIE)
i x
€ Thread o
Direct message
14:56
Aparecen por todos lados
September 9, 2025
fedek (
16:35 W/ J, Nov 10th, 2025 at 1:01 PM
Once you see them 44.35
© Message veo ry) © Message Yo ry)
F
```

## Slide 5

### HOW DID THIS STARTED?

○ Obsession? You think?

5

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
HOW DID THIS STARTED? © Obsession? You
UES UNG, NYS YENIVS 19:08 W/
~ >) mt September 8, 20 2025
; >
\
14:56
September 9, 2025
Aparecen por todos lados
16:35 W
Once you see them 44.35
FV ARE EVERYWHERE)
Cis
imgflip.com
CS
F
```

## Slide 6

###### THEY ACTUALLY ARE

2017

6

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
THEY ACTUALLY ARE
About Ubiquiti Networks
Ubiquiti Networks, Inc. (Nasdaq: UBNT) eliminates barriers to connectivity for under-networked enterprises,
communities and consumers with its leading-edge platforms that connect hundreds of millions of people throughout
the world. | With over 60 million devices sold worldwide,|through a network of over 100 distributors, to customers in
more than 180 countries and territories,|Ubiquiti has maintained an industry-leading financial profile by leveraging a
unique business model to develop products that combine innovative technology with disruptive price-to-
performance characteristics. Our growth is supported by the Ubiquiti Community, a global grass-roots community
of 4 million entrepreneurial operators and systems integrators who engage in thousands of forums. For more
information, join our community at http://www.ubnt.com.
Ubiquiti, Ubiquiti Networks, the U logo, UBNT, airMAX, UniFi, airFiber, mFi, EdgeMAX and AmpliFi are registered
trademarks or trademarks of Ubiquiti Networks, Inc. in the United States and other countries.
2017
```

## Slide 7

###### THEY ACTUALLY ARE

7

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
THEY ACTUALLY ARE
Success in Initial Target Market Demonstrated
Power of Our Business Model
¢ Targeted and transformed wireless broadband in underserved markets
¢ Superior product at disruptive price
¢ Shipped|37+ million airMAX®|units to ~60 countries (life-to-date)
iW Copyright © Ubiquiti Networks, Inc. 2017 8
```

## Slide 8

##### WHAT THAT ANTENNAS ARE USED FOR?

###### **Technology**

Based on IEEE 802.11 Unlicensed spectrum: primarily 2.4 GHz and 5 GHz, 60Ghz

**Network Topologies** Point-to-Point (PtP) Point-to-Multipoint (PtMP)

###### **Common Uses**

Wireless Internet service providers (WISPs) Public and municipal CCTV Critical-infrastructure connectivity Industrial and utility networks Rural broadband and remote-site access

8

## Slide 9

Litebeam 5ac gen2

##### WE DID WHAT EVERYONE WOULD DO… WE FOUND SOME ANTENNAS

NanoBeam M5

9

## Slide 10

WE COULDN’T CONNECT TO THE WI-FI

10

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
WE COULDN'T CONNECT TO THE WI-FI
Networks
Suved
—  faraday_poc a
Saved / Connection failure
Saved
10
```

## Slide 11

# NOW WHAT?

11

## Slide 12

###### GETTING A SHELL INTO THE ANTENNA

That was easy, too easy

12

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
GETTING A SHELL INTO THE ANTENNA
KM , ok@KNWW XW.v6.3.22# iwlist ath® scan
KM = NMMMMMMMM ath® Scan completed :
KM WMMMMMMMMM Cell Q1 - Address: 78:8A:20:A2:42:97
KM KM WMMMMMMMMM ESSID:"ubnt"
KM KM WMMMMMMMMM Mode:Master
KM KM WMMMMMMMMM Frequency:5.185 GHz (Channel 37)
KM KM WMMMMMMMMM Quality=57/94 Signal level=-39 dBm Noise level=-103 dBm
KM KM KM WMMMMMMMMM Encryption key: off
KMNXWM KM WMMMMMMMMK Bit Rates:54 Mb/s
KMMMMMKONM WMMMMMMMW Extra: ubnt=0e4e616e6f4265616d204d352031360000
KMVMMMMMMMM WMV Extra: ieee_mode=802.11n
[MVMMMMMMM WMMMMMN - Cell Q2 - Address: 1€:6A:1B:C4:67:FD
MMMMMMMMML ,WMMMP_ XM: os Geer
LMMMMMMMMx » » ,aaadXMMd .
LNMMMMMMW: =XOxoLccLodOKMMMMWc
LXMMMMMNc 1MMMMMMMMMMMMNo .
LLONMMM@c 1MMMMMMNOo'
"IMN;. 1MWL"
BusyBox v1.24.2 (2025-@8-22 19:57:45 EEST) built-in shell Cash)
Enter "help
XW.v6.3.22#
" for a list of built-in commands.
uname -a
Linux NanoBeam M5 16) 2.6.32.71| #1 Fri Aug 22 20:05:15 EEST 2025 mips GNU/Linux
XW.v6.3.22#
uid=@Cubnt)
XW.v6.3.22#
pean groups=0Cadmin)
Frequency:5.18 GHz (Channel 36)
Quality=56/94 Signal level=-4@ dBm Noise Level=-103 dBm
Encryption key: off
Bit Rates:54 Mb/s
Extra: ubnt=05
Extra: ieee_mode=802 .11ac
That was easy, too easy
12
```

## Slide 13

#### WHAT **AIRMAX** IS?

Now we know is a protocol and not a **shoe**

13

## Slide 14

#### SO, WHERE IS IT IMPLEMENTED?

###### **Difference in the hardware?**

- No, it’s a normal Atheros Chipset

###### **Difference in the software?**

- We can install OpenWRT and it will work as a regular Wi-Fi card (No-Airmax)

- It has custom versions of the drivers

- Probably even custom firmware

THE DIFFERENCE IS IN THE SOFTWARE

14

## Slide 15

# WHAT REALLY IS **AIRMAX**

15

## Slide 16

#### TDMA PROTOCOLS

**Time Division Multiple Access** . Everyone shares one frequency. So the base station gives each client its own time slot. They take turns, in a repeating cycle.

###### **AirMAX is a protocol and implements TDMA on top of 802.11**

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

- **… 2006 2009 2010 Today**

- Before Atheros Atheros and the Open FreeBSD TDMA All the Vendors We are in the same source drivers Implementation point

- • Every Wi-Fi chipset locks • MadWiFi (2003) • Proves deterministic • Atheros ships one SDK • Millions of radios still on radio control time-slots are possible on kernel 2.6.32 (EOL Feb • ath5k (2007) • Each adds only a thin commodity Wi-Fi silicon 2016)

- • vendors keep the HAL proprietary TDMA layer • ath9k (2008)

- closed • The protocols are • Linux 2.6 becomes the undocumented and

- kernel everyone freezes on unresearched

18

## Slide 19

###### THE WORKHORSE OF TDMA OVER 802.11

19

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
THE WORKHORSE OF TDMA OVER 802.11
f
=
Control Frame
| Hendec
B
Vendoc Spe ciesc
Ynfermetion Elem
(pata |
=
—
Trailer
h,
~)
19
```

## Slide 20

HOW AIRMAX IS IMPLEMENTED

20

## Slide 21

###### IT WORKS LIKE A NORMAL IEEE 802.11 WIFI

Broadcast & Probing Open System Auth. and Assoc 4-Way Handshake Scheduling?

What we expect from WIFI

21

## Slide 22

###### TDMA IMPLEMENTATION OVER IEEE 802.11

Vendor Specific Information Element with AirMAX enabled

- OUI: 00:0C:42 -> Device name

- OUI: 00:15:6D

- OUI: 00:27:22

22

## Slide 23

###### TDMA IMPLEMENTATION OVER IEEE 802.11

23

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
AirMAX AE
(Control Frome
(Header
FBody
Ubiquiti TE
UL + 00:27:22
)
L
Encrypted 7?
Lf
TDMA IMPLEMENTATION OVER IEEE 802.11
AirMAX M
we onttol Frome |
[ Hendec )
FBody
Router Board LE
OUL: aQo-9¢:43
Ubiquiti LE
OVL = 00:45 6D
yA
[Traiter
L
23
```

## Slide 24

###### WE STARTED REVERSE ENGINEERING

24

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
afree_private
malloc. private
WE STARTED REVERSE ENGINEERING
asf_print_category_private
afree_private
amalloc private
gpio_line_config
pio _line_set
ath_dfs_prescan
, afree_private
amalloc_private
afree_private
amalloc_private
oN
ubnthal
ubnt_eth_phy
ubnthal_get_eth_port_count
ubnthal_get_radio_cap
afree_private
amalloc_private
afree_private
amalloc_private
asf_print_cirl_register_private
asf_print_ctrl_unregister_private
asf_print_mask_set
(+1 more)
board_identify
ubnthal_get_radio_cap
ath_process_spectraldata
is_spectral_phyerr
Spectral_attach
spectral_check_hw_capability
spectral_control
‘ath_dfs_prescan_register
ath_dfs_prescan_unregistey
Va
ath_dfs_module_locked
ath_dis_register
ath_dfs_unregister
ath_hook host register
ath_kickout hode_notify
ieee80211_fid_node
ieee80211_fre& node
ieee80211_indicate_fhgde_assoy
(+5 more)
ath_dfs
g_pktlog funcs
ath_spectral {7 more}
afree_private
amalloc_private
asf_amem_oreate
asf_amem_destroy
asf_amem_setup
(+5 more)
gpio_int_disable
gpio_int_enable
gpio_int_init
gpio_int_uninit
board_identify
‘gpio_line_config ath_get_tx_chainmask
gpio_line_get ath_rate_attach
gpio_line_set ath_rate_create_vap
ubnthal_get_eeprom_data ath_rate_detach
(+11 more) ath_rate_findrate
(#16 more)
_ath_hal_attach
ath_hal_computetxtime
ath_hal_detach
ath_hal_display_tpctables
ath_hal_enabledANI
~. (#14 more)
ath_hal_probe
ath_hal_get_device_info ath_rate_atheros Bie
(a) =
urt_count_group_countrie:
adf_os_mem_alloc_outline
adf_os_mem_free_outline
adf_os_spin_lock_bh_outline
adf_os_spin_unlock_bh_outline
spectral_attach
spectral_check_hw_capability
spectral_control
spectral_detach
spectral_process_phyerr
(+1 more)
ath_hal_log_ani_callback_register
ACBEMintree
ACBKMiniree
ACVIMinfree
ACVOMinfree
CABMinfree
(+20 more)
ieee80211_leds_register
jeee80211_leds_unregister
board _ identify
urd_alpha2_to_countrycode ‘plo. Tod vet
rssi-leds
led_blink_in_progress,
urt_count_group_countries
24
```

## Slide 25

###### IMPORTANT KERNEL MODULES

MAC drivers
Atheros drivers
Modified version of Ath9k

AirMAX core
driver

25

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
IMPORTANT KERNEL MODULES
afree_private
amalloc_private
ath_hal_set_config_param
ath_hal_reg_write
ath_hal_reg_read
ath_hal_probe
ath_hal_subVendorlD
computetxtime
_hal_getNdevice_info
ath_hal_set_config_param
ath_hal_mhz2ie
... (+15 more)
afree_private
amalloc_private
ath_hal
asf
afree_private
amalloc_private
asf_amem_setup
asf_amem_destroy
asf_amem_create
ath_iw_attach
CABMinfree
ACBKMinfree
wbuf_alloc
ath_cancel_timer
... (+17 more)
afree_private
amalloc_private
Atheros drivers
ieee80211_set_beacon_rx_vendor_ie_hook
ieee80211_set_assoc_req_tx_vendor_ie_hook \\
hook| ops
; dma_sync_single
ath_register_hook
v
MAC drivers
Modified version of Ath9k
ieee80211_set_scan_hook
ieee80211_chan2mode
ieee80211_beacon_alloc
... (+20 more)
AirMAX core
driver
25
```

## Slide 26

###### HOW ARE THE IE BUILD

26

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
HOW ARE THE IE BUILD
{ATR}
$02.71 Maragement Feeene
Vv
fadio | Radio Hardware 4 FiemW |
J t
Ath Driver |
Act Tahe Fom/hend to FW
Uroc Never (80217 Mac)
UmaAc
Perse mgmt Build mgnit
Ly Cal iz call Hook,
Uent ~ Poll
7 mss — mss
Hook — thos (7x)
Porse aa Frac TE |
```

## Slide 27

###### ENCRYPTION? I DON’T THINK SO

###### Validated with **mtscan** by **Konrad Kosmatka** :

- github.com/kkonradpl/mtscan/

27

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ENCRYPTION? | DON’T THINK SO
—
| Ase mac | \\sec mac|
uint8_t* key
hey
key = dst_mac != @ ? dst_mac : &bcast_mac \
| W54
Vv
void out
hmac_shal(message: src_mac, msglen: 6, key, keylen: 6, &out)
| Hmac -Shat ( hey= dst mac 4 msh= Sc med
aes_encrypt_key128(&out, &var_17@)
int32_t $s@ = $s@_1 + Oxf |
Vv
if ($s@_1 s>= @) —_—_...
$s@ = $s6_1 AES 128 eq
char* out_ie_enc = &out_ie_ptr->enc
int32_t $s2_1 = @
uint16_t* $s1_1 = &plain_ie.hdr.version
while (true) TE bee
char* $a@_18 = $s1_1 Patan
|
if ($s2_1 s>= $s@ s>> 4) v 4
break | AES- 42%-EBR decry pt |
$s1_1 = &$s1_1[8]
aes_encrypt($a@_18, out_ie_enc, &var_17@) \
out_ie_enc = &out_ie_enc[@x18@]
Validated with mtscan by Konrad Kosmatka:
F o github.com/kkonradpl/mtscan/
27
```

## Slide 28

###### ENCRYPTION? I DON’T THINK SO

###### Validated with **mtscan** by **Konrad Kosmatka** :

- github.com/kkonradpl/mtscan/

28

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ENCRYPTION? | DON’T THINK SO
© Gaston Aznarez 11:58
é
MAC Address: 44:d9:e7:6a:3a:43
AES Key (derived): ff1db564cf91b27557ff9343ed1d4d16 (16)
Decrypting
[*] Cipher created
Parece que funciona je
Epico
Validated with mtscan by Konrad Kosmatka:
F o github.com/kkonradpl/mtscan/
28
```

## Slide 29

## **RECON TIME**

29

## Slide 30

###### FINDING AIRMAX NETWORKS (in-the-wild)

[ Wardriving MAP ]
[ WIREDRIVING NETWORKS ]

30

## Slide 31

###### FINDING AIRMAX NETWORKS (in-the-wild)

[ Wardriving MAP ]
[ WIREDRIVING NETWORKS ]

31

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
FINDING AIRMAX NETWORKS (in-the-wild)
© Network Map x
Leaflet | © OpenStreetMap
@ Access Point @ Station @ Unknown Role
Fit All Markers = one
31
```

## Slide 32

###### FINDING AIRMAX NETWORKS (in-the-wild)

32

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
FINDING AIRMAX NETWORKS (in-the-wild)
Ae
y.
etal
PTMP-CerritoYcordoba ap
BSSID: 78:8a:20:6c:bd:a9
Radio: AP PTMP-CerritoYcordoba
Signal: -86.4 dBm
Location: Cerrito, Buenos Aires, AR
Coords: -34.598949, -58.381916
Mer
Xx
i
32
```

## Slide 33

###### FINDING AIRMAX NETWORKS (in-the-wild)

33

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
FINDING AIRMAX NETW
16
Discovered Networks
Gerencia_ 5GHz
Aspen
ubnt
PTMP-CerritoYcordoba
Norte.
CLMB
AP CERRITO Y TUCUMAN
ARMENON
Estrategias_2G
Comodoro
Eeninacadtt
785 773
ORKS (in-the-wild)
- MIKROTIK
- MIKROTIK
- MIKROTIK
Ac
. ac
- ac
s AC.
Ac
Ac
EMBEDDED
EMBEDDED
EMBEDDED
EMBEDDED
EMBEDDED
EMBEDDED
- MIKROTIK
= MIKROTIK
M_ENCRYPTED
or
coeneraen,
ap
ap
ap
ap
AP
AP
ap
ap
AP
a>
O
298156
~63.8
»)
754
33
```

## Slide 34

###### LET’S DO SOME TOOLS FOR THE COMMUNITY

###### Tools

- WireMAX - Wireshark dissector

- PyrMAX - Python package

- Web Platform

|[ VIBECODING FROM THE HOSPITAL??? ]|
|---|

34

## Slide 35

# HACKER DREAMS WITH OVER-THE-AIR EXPLOITS

35

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
HACKER DREAMS
WITH OVER-THE
EXPLOITS |
ties
Fact #12
Solving crim,
_Pstore'they har
wer
```

## Slide 36

###### WHAT IF I TOLD YOU…

###### Custom protocols sound great until someone reverses them

36

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
WHAT IF | TOLD YOU...
Custom protocols sound great
until someone reverses them
arg3[@x18] ie->__offset(@x1e) .b
uint32_t $v@_2@ = zx.d(ie->__offset(@x1f) .b)
uint32_t $s@_4 = $v@_20
arg3[@x19] = $v@_28.b
// Where this size comes from???
fedek 11:21AM
memcpy ¢ ~ * Necesito mas memcpy’s
IMG_7466 ¥
—™.:
+ sm
‘>
4
c &
~
A 1reply Today at 5:27 PM
te BP fedek
g
@ Messages QFiles (© (evil)Doggie +
Gaston Aznarez 10:58 AM
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
November 13th, 2025 v
Fri Aug 22 21:28:00 UTC 2025
Read from remote host 192.168.137.102: Connection reset by peer
Connection to 192.168.137.102 closed.
client_loop: send disconnect: Broken pipe
A fedek 10:58AM
Gaston Aznarez 10:58 AM
sospechoso (844 kB) »
&
36
```

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

Criticality:

   - Over-The-Air (line of sight)

   - Unauthenticated

   - RCE

   - Kernel Privileges

- UBB-XG

○ UDB-Pro/UDB-Pro-Sector

○ UBB

CVSS limitations:

○ 8.8 (high) for this adjacent bug (would 9.8 (critical) for LAN bugs)

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

Just **10** days for the first patch **Nov 13 Dec 1 Dec 8 Dec 11 Dec 17 Dec 22 Feb 28 Jan 6** The bug was found The vulnerability CVEs assigned First patch wave Second patch wave Third patch wave Last patch wave Advisories was reported published • CVE-2026-21638 • AirMAX M • AF60-HD/XG • UniFi • AirMAX AC Device/Building • CVE-2026-21639 • AF60/AF60-LR Bridge XG •

41

## Slide 42

###### BUG BOUNTY PAYMENT

- Top $8000 in LAN Networks

- Top $4000 in Adjacent

They pay more for a LAN Vuln than a Vulnerability that can be exploited from kilometers

**100 km**

42

## Slide 43

###### BUG BOUNTY PAYMENT

○ Top $8000 in LAN Networks ○ Top $4000 in Adjacent They pay more for a LAN Vuln than a Vulnerability that can be exploited from kilometers

43

## Slide 44

###### BUG BOUNTY PAYMENT

- Top $8000 in LAN Networks

- Top $4000 in Adjacent

They pay more for a LAN Vuln than a Vulnerability that can be exploited from kilometers

44

## Slide 45

###### BUG BOUNTY PAYMENT

https://radiodx.pl/2020/08/5ghz-wifi-dx-record-denmark-lo gged-in-poland-745-km/

45

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
BUG BOUNTY PAYMENT
5 GHz Wi-Fi DX record - Denmark logged in Poland @ 745 km
“ENGLISH TROPO- “WI-FI DX / 2020-08-15 / Przez Konrad / Jeden komentarz
A remarkable tropospheric ducting occurred on August 11 and 12, 2020 between Poland, Sweden and Denmark. The propagation
forecasts, which use color hue to scale their intensity, featured red shades over the Baltic Sea. Such a propagation strength is very
rare, if ever seen on a forecast for this area. I was looking forward for something extraordinary, especially on the microwave bands.
My stationary Wi-Fi DXing setup has been damaged three months ago. I could not miss such an opening, so a DX-pedition was the
only option. In the evening of August 11 I made an opportunistic decision to visit the Dylewska Gora in north-eastern Poland. A
few hours later, I was standing there with an antenna inside a lookout tower.
‘
;
A
i
-
~~ —
.
-_ >
F https://radiodx.pl/2020/08/S5ghz-wifi-dx-record-den
qaged-in-poland-745-km/
45
```

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

49

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
POC FROM KILOMETERS AWAY v2
ISLA PUERTO MADERO
za de Mayo
La Trastienda
Inezuela
México
AAMAS
WAAAY AS
opsedozy
BAR SUR Tango Show
s
g
N
a)
my
s
o
&
co)
Museo Moderno
Av, Juan de Garay
Rrasil
Measure distance
Click on the map
Total distance: 1.72 km (1.07 mi)
20
usina@uerarte
gue}
```

## Slide 50

HOW WE COULD MAKE THIS BETTER? (WEAPONIZING)

50

## Slide 51

###### FINDING AIRMAX ANTENNAS

We capture beacon messages

51

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
F | N D) | N G Al RMAX ANTE N NAS ) uv run python -m pyrmax discover ../../packets/ubnt_airmax_devices.pcapng
78:8a:20:1c:98:1b (CAC)
radioname ‘AP PTMP-CerritoYsarmiento'
ssid *PTMP-CerritoYsarmiento*
ac_msg_types BEACON
We capture beacon messages ac_version 8
cap_flags Qx00000002
mixed_mode @
frames 84
first seen 1765842.012760
last seen 1765842 . 718826
peers (broadcast only)
78:8a:20:6c:bd:a9 (CAC)
radioname ‘AP PTMP-CerritoYcordoba'
ssid *PTMP-CerritoYcordoba'
~ AirMAX AC (Vendor Specific IE) ac_msg_types BEACON
OUI: 002722 acversion 8
OUI Type: ffffff cap_flags @x00000002
> Flags: @x@2 mixed_mode @
Message Type: Beacon (1) frames 5322
Encrypted Length: 80 first seen 1765834.576612
Ciphertext: c286a8909dd964b5aa5d54996 fea596 f5dd5 f7685b70781eaalObe3b6a5: last seen 1782250959 . 162468
v [Decrypted payload (AES-128-ECB) ] peers (broadcast only)
[AES Key (HMAC-SHA1(dst,src)[:16]): 6483ef489f21bca28d029e86c55d9f69
Version: 8 78:8a:20:6c:bd:ad (CAC)
Source MAC: Ubiquiti_6c:bd:a9 (78:8a:20:6c:bd:a9) radioname ‘AP PTMP-CerritoYcorrientesOCA'
Radio MAC (mac_@c): Ubiquiti_6c:bd:a9 (78:8a:20:6c:bd:a9) ssid 'PTMP-CerritoYcorrientesOCA'
> Capability Flags: 0x00000002 ac_msg_types BEACON
Mixed Mode: @ ac_version 8
Radioname: AP PTMP—CerritoYcordoba cap_flags @xe0200002
SSID: PTMP-—CerritoYcordoba
> TLV: Radioname (1), len 23
> TLV: SSID (2), len 20
> TLV: Padding (@)
mixed_mode @
frames 128
first seen 1765841.895960
last seen 1765842 . 709035
peers (broadcast only)
```

## Slide 52

###### FINGERPRINTING

We start the Open-System Auth. and Assoc because the FW version in sent on the IE (AirMAX AC > v9)

52

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
FINGERPRINTING
No. Time | Source | Destination | Info
1 0.0000... Ubiquiti_c4.. Broadcast Beacon frame, SN=2748, FN=
2 0.1027... Ubiquiti_c4.. Broadcast Beacon frame, SN=2751, FN=
We start the Open-System Auth. and Assoc 3 @.1476.. Ubiquiti_be.. Ubiquiti_c4.. Probe Request, SN=256, FN=
because the FW version in sent on the IE (AirmMAX 4 0.1476... Ubiquiti_c4.. Ubiquiti_be.. Probe Response, SN=2752, F
AC > v9) 7 0.1505... Ubiquiti_be.. Ubiquiti_c4.. Association Request, SN=25
8 @.1520.. Ubiquiti_c4.. Ubiquiti_be.. Association Response, SN=2
p ST A > Frame 8: Packet, 265 bytes on wire (212@ bits), 265 bytes capture
A > Radiotap Header v@, Length 36
z Version:
> 802.11 radio information
> IEEE 802.11 Association Response, Flags: ...s.s.. C
> IEEE 802.11 Wireless Management
» AirMAX AC (Vendor Specific IE)
)
Prope Resp . If QUI: 002722
OUI Type: ffftfff
Ruth Req — > Flags: 0x02
Lo- Message Type: Assoc Resp (3)
Auth [eS Encrypted Length: 64
> Ciphertext: f9a4c74cd7bd7b94cefb0ddd8af89c9493721794002e42b2295¢
ae -Yw - [Decrypted payload (AES-128-ECB) ]
[AES Key (HMAC-SHA1(dst,src)[:16]): ce1f241d63112e4eee7244f36a
Source MAC: Ubiquiti_c4:67:fd (1c:6a:1b:c4:67: fd)
es-IE- Fw ic_6b8 (chainmask pair): 0303
——> sta_field_68 [open]: 0x338ef79d
RSSI (per-chain): 2931
Firmware Name: WA.ar934x.v8.7.22.48486.260227.1
V V TX Power (half-dBm): 252
52
```

## Slide 53

###### SENDING THE EXPLOIT

We send the OTA exploit doing the following

- Change user name

- Change user password

- Change network password

- Run **ubntconf**

53

## Slide 54

###### POST EXPLOITATION - PERSISTENCE

   - **/tmp/system.cfg** is a temporary file!

- Connect to the WiFi with the new password

- Restore the configuration

- Backdoor

   - Create a new user

   - Apply configuration

- Obtain old network password

54

## Slide 55

ALL TOGETHER - DEMO 2

55

## Slide 56

# WE ARE IN, NOW WHAT?

56

## Slide 57

###### FINDING ANOTHER DEVICES

57

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
FINDING ANOTHER DEVICES
XW.v6.3.22# ubntbox discover
Hardware Address’ IP address
78:8A:20:A2:42:97 192.168.37
44:D9:E7:6A:3A:43 192.168.37
1C:6A:1B:C4:67:FD 192.168.37
Total: 4 devices.
.103
FQ:9F:C2:C8:FQ@:AD 192.168.37.
104
.102
. 100
JHECVE-2026-21633 Detail
NIST: NVD
\=
RY CNA: HackerOne
Name
NanoBeam M5 16 'NanoBeam M5 16'
UAP-AC-Pro-Gen2 ‘Piaget AP'
NanoBeam M5 16 'NanoBeam M5 16'
LiteBeam 5AC 'FaradayLB2'
‘Si
```

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

Gaston Aznarez:     𝕏 @GastonAznarez   [ln] gastonaznarez Fede Kirschbaum:   𝕏 @fede_k                 [ln] fedek

62
