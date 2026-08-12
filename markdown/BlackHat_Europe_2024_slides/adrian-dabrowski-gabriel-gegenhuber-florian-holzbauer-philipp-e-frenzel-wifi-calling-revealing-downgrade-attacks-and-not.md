---
title: "WiFi Calling Revealing Downgrade Attacks and Not-so-private private Keys"
speakers: ["Adrian Dabrowski", "Gabriel Gegenhuber", "Florian Holzbauer", "Philipp E. Frenzel"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2024"
edition: "Europe"
year: 2024
source_pdf: "BlackHat_Europe_2024_slides/Adrian Dabrowski & Gabriel Gegenhuber & Florian Holzbauer & Philipp E. Frenzel_WiFi Calling Revealing Downgrade Attacks and Not-so-private private Keys_Compressed.pdf"
pages: 52
sha256: "3649d1036fcb0623a353093f8840bcf2af50d4b63b5f5a4d3223417cebede70f"
text_chars: 17637
ocr_pages: 1
has_ocr: true
redacted_secrets: 0
ocr_confidence: 83.8
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:53:56Z"
---
# WiFi Calling Revealing Downgrade Attacks and Not-so-private private Keys

**Speakers:** Adrian Dabrowski, Gabriel Gegenhuber, Florian Holzbauer, Philipp E. Frenzel  
**Conference:** Black Hat Europe 2024  
**Source:** `BlackHat_Europe_2024_slides/Adrian Dabrowski & Gabriel Gegenhuber & Florian Holzbauer & Philipp E. Frenzel_WiFi Calling Revealing Downgrade Attacks and Not-so-private private Keys_Compressed.pdf` (52 pages)


## Slide 1

**Wi-Fi Calling** Revealing Downgrade Attacks and Not-so-private Private Keys

**Gabriel K. Gegenhuber, Florian Holzbauer, Philipp É. Frenzel, Edgar Weippl, Adrian Dabrowski**

## Slide 2

## **The Speakers**

**Gabriel Gegenhuber** Bachelor’s and Master’s from TU Wien **Researcher at SBA Research PhD Candidate at University of Vienna Adrian Dabrowski** PhD from TU Wien PostDoc at University of California, Irvine PostDoc at CISPA Helmholtz Center **Faculty at University of Applied Sciences, FH Campus Wien**

Black Hat Europe 2024

WiFi Calling: Revealing Downgrade Attacks and Not-so-private Private Keys

2/49

## Slide 3

## **Cellular Research Challanges**

**Different Access Technologies**

Radio: 2G, 3G, 4G, 5G Voice: legacy and CSFB, VoLTE

**Legacy Protocols**

USSD, OTA, Proactive SIM, WAP

**Corner Cases Geography** Roaming Strict confinement through frequency Zero-rating licensing Geo-blocked Services 2-4 bare metal opterators per country

Black Hat Europe 2024

WiFi Calling: Revealing Downgrade Attacks and Not-so-private Private Keys

3/49

## Slide 4

**Large-scale / International Measurement in Radio Access Networks**

## Slide 5

## **Example: Measuring One Operator in Three Countries**

Black Hat Europe 2024

WiFi Calling: Revealing Downgrade Attacks and Not-so-private Private Keys

5/49

## Slide 6

## **Example: Measuring Three Operators in Three Countries**

Black Hat Europe 2024

WiFi Calling: Revealing Downgrade Attacks and Not-so-private Private Keys

6/49

## Slide 7

**Example: (6+1)** × **3 Operators** × **3 Plans** × **3 Territories = 189**

Black Hat Europe 2024

WiFi Calling: Revealing Downgrade Attacks and Not-so-private Private Keys

7/49

## Slide 8

## **Geographically Decoupling Modem and SIM Card**

- Traditionally modem and SIM card are seen as an indivisible unit

- We execute a **relay** attack on the **communication** between SIM card and modem Modem is at location/country A SIM card can be at location/country B

- **"Virtual Circuit"** : APDU over TCP connection

- SIM Tunnel interface < 10 USD

Black Hat Europe 2024

WiFi Calling: Revealing Downgrade Attacks and Not-so-private Private Keys

8/49

## Slide 9

## **MobileAtlas**

- Scalable, cost-efficient test framework for cellular networks

- Flexible roaming measurements

- Versatile measurement capabilities

- Controlled measurement environment

Black Hat Europe 2024

WiFi Calling: Revealing Downgrade Attacks and Not-so-private Private Keys

9/49

## Slide 10

## **MobileAtlas: Probe & SIM Provider**

Black Hat Europe 2024

WiFi Calling: Revealing Downgrade Attacks and Not-so-private Private Keys

10/49

## Slide 11

## **SIM Tunneling: Low-Cost Implementation**

Black Hat Europe 2024

WiFi Calling: Revealing Downgrade Attacks and Not-so-private Private Keys

11/49

## Slide 12

## **Measurement Cases**

- Ringback tone fingerprinting Leaking country/operator of target

- Proactive SIM: covert binary SMS to operator

- Zero-rating and free-riding

Black Hat Europe 2024

WiFi Calling: Revealing Downgrade Attacks and Not-so-private Private Keys

12/49

## Slide 13

## **Ringback Tones Examples**

O2, Germany

Vodaphone, Romania

Black Hat Europe 2024 WiFi Calling: Revealing Downgrade Attacks and Not-so-private Private Keys

13/49

## Slide 14

## **Voice: Ringback Tones**

Black Hat Europe 2024

WiFi Calling: Revealing Downgrade Attacks and Not-so-private Private Keys

14/49


> Recovered by OCR — confidence 84/100 on the text kept, 56/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Voice: Ringback Tones
© DE_Vodafone © US_Tmobile_L2 US_Tmobile_H2
-26
© DE_02(1) © SK_02
-28 SK_Orange®
HRA18SLA1
-36
Hz
Black Hat Europe 2024 Wii Calling: Revealing Downgrade Attacks and Not-so-private Private Keys 14/49
```

## Slide 15

## **Voice & Messaging: Two Access Technologies for 4G/5G**

© Raysonho @ Open Grid Scheduler [CC0]

- VoLTE via **RAN / Celltower** Also VoNR, Vo5G

- VoWiFi via **WiFi Access Point (AP)** Also Wi-Fi Calling Usually the preferred channel for call and message termination

Black Hat Europe 2024

WiFi Calling: Revealing Downgrade Attacks and Not-so-private Private Keys

15/49

## Slide 16

## **Recap: Measurement over RAN**

eNB
S-GW EPC P-GW P-CSCF IMS
SIM
UE
Configs

Black Hat Europe 2024

WiFi Calling: Revealing Downgrade Attacks and Not-so-private Private Keys

16/49

## Slide 17

## **Recap: Measurement over RAN**

eNB
S-GW EPC P-GW P-CSCF IMS
SIM
UE
Configs
ePDG

Black Hat Europe 2024

WiFi Calling: Revealing Downgrade Attacks and Not-so-private Private Keys

17/49

## Slide 18

## **Recap: Measurement over RAN (VoWiFi)**

eNB
S-GW EPC P-GW P-CSCF IMS
VoLTE
SIM
UE
WiFi AP
Configs
VoWiFi via IPsec Tunnel
ePDG

Black Hat Europe 2024

WiFi Calling: Revealing Downgrade Attacks and Not-so-private Private Keys

18/49

## Slide 19

## **VoWiFi Requires Multiple IPSec Tunnels**

UE ePDG P-GW P-CSCF
IKEv2 (Signaling)
L1 IKE ( SA_INIT )
IPsec (Tunnel Mode)
L2 IPsec (IKE  CHILD_SA )
IPsec (Transport Mode)
L3 SIP ( ipsec-3gpp )

Black Hat Europe 2024

WiFi Calling: Revealing Downgrade Attacks and Not-so-private Private Keys

19/49

## Slide 20

## **Practical Example:** IKE_SA_INIT **Packet**

Black Hat Europe 2024

WiFi Calling: Revealing Downgrade Attacks and Not-so-private Private Keys

20/49

## Slide 21

## **Practical Example:** IKE_SA_INIT **Packet**

- DH2 (1024-bit MODP) might not be the best choice

- _Imperfect Forward Secrecy: How Diffie-Hellman Fails in Practice_ (CCS 2015): _“We further estimate that_

_an academic team can break a 768-bit prime_

   - _a nation-state can break a 1024-bit prime.”_

- Since 2015 computers got faster, cracking power got cheaper (AWS)

Black Hat Europe 2024

WiFi Calling: Revealing Downgrade Attacks and Not-so-private Private Keys

21/49

## Slide 22

## **VoWiFi Security: Key Exchange vs. Security Associations**

- IKE **key exchange is crucial** for residual connection (and other layers) Used SAs (Security Associations) do not matter if weak key exchange is used

- Our wireshark example looks suspicious We want to get the **global picture** at commercial operators Standardization vs. status quo

Black Hat Europe 2024

WiFi Calling: Revealing Downgrade Attacks and Not-so-private Private Keys

22/49

## Slide 23

## **ETSI/3GPP Specification**

Black Hat Europe 2024 WiFi Calling: Revealing Downgrade Attacks and Not-so-private Private Keys

23/49

## Slide 24

## **ETSI/3GPP Specification Over Time**

shall  IKEv1 DH19[256ECP]
(mandatory)
1.5
should DH20[384ECP]
support DH31
0.5 [Curve25 519]
not part of
3GPP standard DH14[2048MODP]
-0.5
mandatory, but
not recommended
-1.5
shall not DH2(1024MODP)
(prohibited)
-2.5
v5.5 (2002)v6.5 (2004)v7.3 (2007)v8.2 (2009)v9.1 (2010)v10.2 (2011)v10.3 (2011)v11.4 (2012)v12.2 (2014)v13.0 (2016)v15.2.2 (2019)v16.4 (2020)v17.0 (2022)v17.1 (2022)

Black Hat Europe 2024

WiFi Calling: Revealing Downgrade Attacks and Not-so-private Private Keys

24/49

## Slide 25

## **ETSI/3GPP Specification Over Time**

2.5
shall  IKEv1 DH19[256ECP]
(mandatory)
1.5
should DH20[384ECP]
support DH31
0.5 [Curve25 519]
not part of
3GPP standard DH14[2048MODP]
-0.5
mandatory, but
not recommended
-1.5
shall not DH2(1024MODP)
(prohibited)
-2.5
v5.5 (2002)v6.5 (2004)v7.3 (2007)v8.2 (2009)v9.1 (2010)v10.2 (2011)v10.3 (2011)v11.4 (2012)v12.2 (2014)v13.0 (2016)v15.2.2 (2019)v16.4 (2020)v17.0 (2022)v17.1 (2022)

Black Hat Europe 2024

WiFi Calling: Revealing Downgrade Attacks and Not-so-private Private Keys

25/49

## Slide 26

## **Flank I: Analyze Pre-loaded Configs at the Client-Side**

eNB
S-GW EPC P-GW P-CSCF IMS
VoLTE
UE
WiFi AP
Configs
VoWiFi via IPsec Tunnel
ePDG

Black Hat Europe 2024

WiFi Calling: Revealing Downgrade Attacks and Not-so-private Private Keys

26/49

## Slide 27

## **Flank II: Analyze IPsec Client on the UE**

eNB
S-GW EPC P-GW P-CSCF IMS
VoLTE
UE
Configs
IPsec
ePDG

Black Hat Europe 2024

WiFi Calling: Revealing Downgrade Attacks and Not-so-private Private Keys

27/49

## Slide 28

## **Flank III: Analyze Server Side Configurations**

eNB
S-GW EPC P-GW P-CSCF IMS
VoLTE
UE
Configs
VoWiFi IPsec
ePDG

Black Hat Europe 2024

WiFi Calling: Revealing Downgrade Attacks and Not-so-private Private Keys

28/49

## Slide 29

eNB
S-GW EPC P-GW P-CSCF IMS
VoLTE
UE
WiFi AP
Configs
VoWiFi via IPsec Tunnel
ePDG

## **Flank I: Client-Side Pre-loaded Configurations**

## Slide 30

## **Methodology I: Pre-loaded Configs at the Client-Side**

eNB
S-GW EPC P-GW P-CSCF IMS
VoLTE
UE WiFi AP
Configs
VoWiFi via IPsec Tunnel
ePDG

- Every phones comes with their own PRE-LOADED database 3GPP ecosystem lacks auto-configuration, even on IETF protocols

- Evaluated **different manufacturers and devices** Apple: IPCC Carrier Profiles

   - https://github.com/mrlnc/ipcc-downloader

   - Samsung: XML Config File

   - /system/etc/epdg_apns_conf.xml

   - Xiaomi, Oppo: Qualcomm MBN File

   - https://github.com/sbaresearch/mbn-mcfg-tools

   - Google Pixel uses default values (hardcoded in source code)

Black Hat Europe 2024 WiFi Calling: Revealing Downgrade Attacks and Not-so-private Private Keys

30/49

## Slide 31

## **Results I: Pre-loaded Configs at the Client-Side**

eNB
S-GW EPC P-GW P-CSCF IMS
VoLTE
UE WiFi AP
Configs
VoWiFi via IPsec Tunnel
ePDG

19 (9%) Provider
(1) 768-bit 0 (0%) 12 (5%) Apple Oppo
13 (8%) Xiaomi Samsung
94 (43%)
(2) 1024-bit 102 (68%)
175 (79%)
34 (22%)
16 (7%)
(5) 1536-bit 76 (51%)
85 (38%)
22 (14%)
88 (40%)
(14) 2048-bit 111 (74%)
142 (64%)
122 (78%)
5 (2%)
(>=) 3072-bit 8 (5%)
12 (5%)
17 (11%)
0 20 40 60 80
Percentage (%)
DH Groups

- Results for Apple, Samsung, Xiaomi, Oppo

- DH2 (1024-bit MODP) is very popular �

- DH Groups > 2048-bit barely used

Black Hat Europe 2024 WiFi Calling: Revealing Downgrade Attacks and Not-so-private Private Keys

31/49

## Slide 32

eNB
S-GW EPC P-GW P-CSCF IMS
VoLTE
UE
Configs
IPsec
ePDG

## **Flank II: IPsec Client Implementation on the UE**

## Slide 33

## **Methodology II: Analyze IPsec Client on the UE**

eNB
S-GW EPC P-GW P-CSCF IMS
VoLTE
UE
Configs
IPsec
ePDG

- VoLTE/VoWiFi **implementation depends on manufacturer/device** Managed by the modem (e.g., Qualcomm) Managed in the userspace (e.g., strongSwan binaries for Samsung, MediaTek)

- Investigated whether **downgrade attacks** are possible

Black Hat Europe 2024 WiFi Calling: Revealing Downgrade Attacks and Not-so-private Private Keys

33/49

## Slide 34

## **Results II: (Protocol Conform) Downgrade Procedure**

eNB
S-GW EPC P-GW P-CSCF IMS
VoLTE
UE
Configs
IPsec
ePDG

ePDG

UE <u>SA_INIT([DH2, DH14], KE_DH14) INVALID_KE(USE DH2) SA_INIT([DH2, DH14], KE_DH2)</u>

- Client selects **preferred DH group** , but also signals support for **other groups** Server can request **switch to other group** via INVALID_KE packet

Client starts over, respecting the server’s choice

Black Hat Europe 2024

WiFi Calling: Revealing Downgrade Attacks and Not-so-private Private Keys

34/49

## Slide 35

## **Results II: (Protocol Conform) Downgrade Vulnerability**

eNB
S-GW EPC P-GW P-CSCF IMS
VoLTE
UE
Configs
IPsec
ePDG

UE ePDG
SA_INIT([DH2, DH14], KE_DH14)
INVALID_KE(USE DH2)
SA_INIT([DH2, DH14], KE_DH2)

- Client selects **preferred DH group** , but also signals support for **other groups** Server can request **switch to other group** via INVALID_KE packet

   - Client starts over, respecting the server’s choice

- A malicious **interceptor** could **inject a downgrade packet** Could be mitigated by servers always demanding strongest group

   - However, 41% of servers **tolerate weak client choices** �

Black Hat Europe 2024 WiFi Calling: Revealing Downgrade Attacks and Not-so-private Private Keys

35/49

## Slide 36

## **Results II: Downgrade Vulnerability at MediaTek Clients**

UE (MTK) MitM ePDG
SA_INIT([DH14], KE_DH14)
INVALID_KE(USE DH1)
SA_INIT([DH1], KE_DH1)

eNB
S-GW EPC P-GW P-CSCF IMS
VoLTE
UE
Configs
IPsec
ePDG

- MediaTek chipsets allow **downgrade to arbitrary DH group** �

   - Even when the group was not part of the client’s proposal

Can always downgrade to weak groups (DH1, DH2) if target server supports it

Black Hat Europe 2024

WiFi Calling: Revealing Downgrade Attacks and Not-so-private Private Keys

36/49

## Slide 37

eNB
S-GW EPC P-GW P-CSCF IMS
VoLTE
UE
Configs
VoWiFi IPsec
ePDG

## **Flank III: Analyze Server Side Configurations**

## Slide 38

## **Methodology III: Supported DH Groups at the Server-Side**

eNB
S-GW EPC P-GW P-CSCF IMS
VoLTE
UE
Configs
VoWiFi IPsec
ePDG

- Goals

   - What parameters (DH groups) do MNOs actually support? How will ePDGs react, if client prefers weaker DH-groups than mutually supported?

- Each operator is identified by MCC + MNC

- ePDG domain: epdg.epc.mnc〈id〉.mcc〈id〉.pub.3gppnetwork.org

- Two steps

1. **DNS discovery**

   - Done via mass DNS resolution

2. **IKE handshake**

   - Reimplemented IKE handshake via scapy

Black Hat Europe 2024 WiFi Calling: Revealing Downgrade Attacks and Not-so-private Private Keys

38/49

## Slide 39

## **Results III: Supported DH Groups at the Server-Side**

eNB
S-GW EPC P-GW P-CSCF IMS
VoLTE
UE
Configs
VoWiFi IPsec
ePDG

- Active probing of ePDG servers 423 domain entries found, 275 responsive ePDGs

- DH2 (1024-bit MODP) most popular �

- • DH1 (768-bit MODP) supported by 40% of servers �

Black Hat Europe 2024 WiFi Calling: Revealing Downgrade Attacks and Not-so-private Private Keys

39/49

## Slide 40

## **Results III: Supported DH Groups at the Server-Side**

eNB
S-GW EPC P-GW P-CSCF IMS
VoLTE
UE
Configs
VoWiFi IPsec
ePDG

- Client indicated weaker DH group than mutually supported

   - 41% MNOs accepted the less secure method

   - 12% returned error without proposal

   - 42% desired an upgrade by the UE

   - ½ choose DH18 (8192),

   - Others DH14 (2048)

   - 4% indicate a downgrade to DH1 (768)

Black Hat Europe 2024 WiFi Calling: Revealing Downgrade Attacks and Not-so-private Private Keys

40/49

## Slide 41

## **Result III: Repeating Public Keys**

Black Hat Europe 2024

WiFi Calling: Revealing Downgrade Attacks and Not-so-private Private Keys

41/49

## Slide 42

## **Short Excursion: Diffie-Hellman Key Exchange**

- a: private key Alice

- b: private key Bob

- p: public prime number (DH group) g: public integer smaller than p (DH group) A: public key Alice

- B: public key Bob

- K: secret session key between Alice and Bob

Black Hat Europe 2024

WiFi Calling: Revealing Downgrade Attacks and Not-so-private Private Keys

42/49

## Slide 43

## **Short Excursion: Diffie-Hellman Key Exchange**

- a: private key Alice b: private key Bob p: public prime number (DH group) g: public integer smaller than p (DH group) A: public key Alice B: public key Bob

- K: secret session key between Alice and Bob

Black Hat Europe 2024

WiFi Calling: Revealing Downgrade Attacks and Not-so-private Private Keys

43/49

## Slide 44

10 public keys

� 10 private keys

(world-wide)

Black Hat Europe 2024

WiFi Calling: Revealing Downgrade Attacks and Not-so-private Private Keys

44/49

## Slide 45

## **Result III: (Not-so) Private Keys**

- Identical key exchange value -> **identical private-keys**

Inter MNO key sharing: private-key collisions with unrelated MNOs

- 16 operators **spread across the world** : e.g., Austria, Brazil, Indonesia, Malaysia, Nepal, Russia, etc. Estimation: 140 million subscribers affected Anyone having access to the private keys can decrypt the VoWiFi traffic

- Affected operators all use ZTE equipment for their core network

Black Hat Europe 2024

WiFi Calling: Revealing Downgrade Attacks and Not-so-private Private Keys

45/49

## Slide 46

## **Responsible Disclosure I: CVE-2024-20069**

- MediaTek: CVE-2024-20069, severity high Fixed via Android Security Update (June 2024) Dimensity SoC MT6833, MT6853, MT6855, MT6873, MT6875, MT6875T, MT6877,MT6883, MT6885, MT6889, MT6891, MT6893, MT8675, MT8771,MT8791T, MT8797 NR15 modem Not much more details

Black Hat Europe 2024

WiFi Calling: Revealing Downgrade Attacks and Not-so-private Private Keys

46/49

## Slide 47

## **Responsible Disclosure II: CVE-2024-22064, CVD-2024-0089**

- Responsible disclosure was coordinated by GSMA Initial report in February 2024 CVD-2024-0089

- • ZTE: CVE-2024-22064, severity high Private keys are leftovers from integration testing Accidentally slipped into production images affected: ZXUN-ePDG < V5.20.20 Some of those operational since 2016

Black Hat Europe 2024 WiFi Calling: Revealing Downgrade Attacks and Not-so-private Private Keys

47/49

## Slide 48

## **ZTE: Remediation Timeline**

15
10
5
0
Austria Drei Slovakia 4ka+Pakistan TelenorHungary YettelBrazil UNIFIQUE
Brazil Vero (AmericaNet)
Russia Beeline
Malaysia Telekom Malaysia
Malaysia unifiIndonesia Smartfren
Malaysia U Mobile
Malaysia DiGiPakistan Telenor
Nepal Telecom
03-16 03-21 03-26 03-31 04-05 04-10 04-15 04-20 04-25 04-30 05-05 05-10 05-15 05-20 05-25 05-30 06-04 06-09
# vulnerable operators

Black Hat Europe 2024 WiFi Calling: Revealing Downgrade Attacks and Not-so-private Private Keys

48/49

## Slide 49

## **ZTE: Remediation Timeline Part II - The Return**

15
10
5
0
7 operators vulnerable again!
Malaysia DiGiPakistan Telenor
Nepal Telecom
05-21 05-26 05-31 06-05 06-10 06-15 06-20 06-25 06-30 07-05 07-10 07-15 07-20 07-25 07-30 08-04 08-09 08-14 08-19 08-24 08-29
# vulnerable operators

Black Hat Europe 2024 WiFi Calling: Revealing Downgrade Attacks and Not-so-private Private Keys

49/49

## Slide 50

## **Limited Coverage due to VoWiFi Geoblocking**

- **Potentially** even **more vulnerable operators** out there

- Many operators employ **geoblocking** at VoWiFi Especially common within Europe and Asia Shown in related paper _Why E.T. Can’t Phone Home_

Black Hat Europe 2024 WiFi Calling: Revealing Downgrade Attacks and Not-so-private Private Keys

50/49

## Slide 51

## **Lessons Learned & Takeways**

**Remove Code**

... and not just the handshake advertisement. Attackers might find a way to activate it.

**Deprication Path** Built-in from the first version of a standard

**Key Freshness**

Algorithmically or statistically

Black Hat Europe 2024

WiFi Calling: Revealing Downgrade Attacks and Not-so-private Private Keys

51/49

## Slide 52

# **Thank you**

• Contact gabriel.gegenhuber@univie.ac.at @GGegenhuber @ggegenhuber.bsky.social adrian.dabrowski@fh-campuswien.ac.at @Atrox_at @atrox.at

github.com/sbaresearch/vowifi-epdg-scanning

Black Hat Europe 2024

WiFi Calling: Revealing Downgrade Attacks and Not-so-private Private Keys

52/49
