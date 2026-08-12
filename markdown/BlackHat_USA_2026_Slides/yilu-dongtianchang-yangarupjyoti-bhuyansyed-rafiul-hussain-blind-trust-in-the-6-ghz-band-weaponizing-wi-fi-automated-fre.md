---
title: "Blind Trust in the 6 GHz Band Weaponizing Wi-Fi Automated Frequency Coordination (AFC)"
speakers: ["Yilu Dong", "Tianchang Yang", "Arupjyoti Bhuyan", "Syed Rafiul Hussain"]
conference: "Black Hat"
conference_full: "Black Hat USA 2026"
edition: "USA"
year: 2026
source_pdf: "BlackHat_USA_2026_Slides/Yilu Dong&Tianchang Yang&Arupjyoti Bhuyan&Syed Rafiul Hussain_Blind Trust in the 6 GHz Band Weaponizing Wi-Fi Automated Frequency Coordination (AFC).pdf"
pages: 56
sha256: "4b534a2b54927df006499aad05ba3dad638fbc8df955321b70a396b1da7c73c9"
text_chars: 21761
ocr_pages: 10
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:17:45Z"
---
# Blind Trust in the 6 GHz Band Weaponizing Wi-Fi Automated Frequency Coordination (AFC)

**Speakers:** Yilu Dong, Tianchang Yang, Arupjyoti Bhuyan, Syed Rafiul Hussain  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/Yilu Dong&Tianchang Yang&Arupjyoti Bhuyan&Syed Rafiul Hussain_Blind Trust in the 6 GHz Band Weaponizing Wi-Fi Automated Frequency Coordination (AFC).pdf` (56 pages)

## Slide 1

## Slide 2

BLIND TRUST IN THE 6 GHZ BAND

Weaponizing Wi-Fi Automated Frequency Coordination (AFC)

**Yilu Dong** , **Tianchang Yang** , Syed Rafiul Hussain — The Pennsylvania State University Arupjyoti Bhuyan — Idaho National Laboratory

2

## Slide 3

###### About Us

###### **Yilu Dong**

- Research Assistant, The Pennsylvania State University

- • Wireless protocol and systems security, applied cryptography, vulnerability discovery: 5G systems, WiFi AFC systems

- <u>`yilud.me`</u>

###### **Tianchang Yang**

- Research Assistant, The Pennsylvania State University

- Wi-Fi systems, Mobile network security, resiliency, and robustness: 5G, Open RAN, baseband (fuzzing, program analysis, ML)

- <u>`tianchang-yang.github.io`</u>

3

## Slide 4

###### Interference Broke a Life-Safety Network

Miami-Dade built a new 6 GHz public-safety microwave system for first responders, engineered for 99.999% reliability . It couldn't go into service.

```
NOV 2020DEC 20212022
```

```
NOV 2022
```

**Degradation detected. ~1 year to find one source:** In acceptance testing, the an out-of-band device, hidden by new link underperforms; frequency hopping. kept out of service.

**It re-offends; t** wo more interferers surface after months of additional investigation

Formal warning reaches **one** offender. **Two years on** – the interference still continuous and the **system continuous to suffer from harmful interference**

<u>https://www.apcointl.org/~documents/filing/apco-ex-parte-6ghz-miami-dade-112222</u>

**4**

## Slide 5

###### Interference Broke a Life-Safety Network

Miami-Dade built a new 6 GHz public-safety microwave system for first responders, engineered for 99.999% reliability . It couldn't go into service.

```
NOV 2020DEC 20212022NOV 2022
```

**Degradation detected. ~1 year to find one source: It re-offends; t** wo more interferers Formal warning reaches **one** surface after months of additional offender. **Two years on** – the In acceptance testing, the an out-of-band device, hidden by new link underperforms; frequency hopping. investigation interference still continuous and the **system continuous to suffer from** kept out of service. **harmful interference**

AND THIS WAS AN ACCIDENT

The offenders were unintentional and never hid What if an attacker induces the same interference on purpose, from a legally-authorized AP device/network transmitting within the rules — then stops and leaves nothing to trace

<u>https://www.apcointl.org/~documents/filing/apco-ex-parte-6ghz-miami-dade-112222?layout=file</u>

**5**

## Slide 6

###### The Biggest Spectrum Release in Decades font size

2.4 GHZ 5 GHZ 6 GHZ
~ 80 MHz · saturated ~ 500 MHz · congested 1,200 MHz · opened for unlicensed Wi-Fi

In 2020 the FCC opened **1,200 MHz** at 6 GHz (5.925–7.125 GHz) for commercial use — more contiguous spectrum than everything below it combined, released almost overnight for Wi-Fi 6E and Wi-Fi 7.

**6**

## Slide 7

###### The Biggest Spectrum Release in Decades font size

2.4 GHZ

- ~ 80 MHz · saturated

5 GHZ

~ 500 MHz · congested

6 GHZ

- 1,200 MHz · opened for unlicensed Wi-Fi

In 2020 the FCC opened **1,200 MHz** at 6 GHz (5.925–7.125 GHz) for commercial use — more contiguous spectrum than everything below it combined, released almost overnight for Wi-Fi 6E and Wi-Fi 7.

#### 6 GHZ WAS NEVER EMPTY

Fixed Service (FS) microwave links have carried mission-critical traffic across this band for decades. Wi-Fi is the newcomer moving in on top of them.

###### PUBLIC SAFETY

###### CONTROL SIGNALS

###### SCIENCE

###### MOBILE BACKHAUL

**7**

## Slide 8

###### 40× Transmit Energy

- **Standard Power (SP)** APs transmit far hotter than indoor units: up to **36 dBm EIRP** (≈ 4 W).

- That power buys range — but also the ability to **reach an incumbent's receiver kilometers away.**

- So the FCC forbids an SP AP from transmitting until it **asks permission.**

Low-power Indoor AP ≤30 dBm USRP B210 Jammer ~20 dBm **Standard Power Max 36 dBm**

Every +3 dB doubles radiated power. 36 vs 20 dBm ≈ 40× the energy

8

## Slide 9

###### AFC: Automated Frequency Coordination

Identity, Location, Antenna, Power Class
Standard Power (SP)
AFC SERVER
Access Points (AP)
Permitted Channels, Max Power

- Simplifies and automates similar systems in other bands (e.g., CBRS in 3.5 GHz bands)

- The AP reports its identity, location, antenna height, and power class to the AFC server.

- The server checks that location against a **database of protected incumbent receivers** and a propagation model, and works out which channels and power levels won't interfere with them.

- AFC returns an **allocation** : channels and the maximum power the AP is allowed to use.

- The allocation is a **lease valid for 24 hours** . When it expires, the AP has to ask again before it can keep transmitting.

**9**

## Slide 10

###### AFC Request/Response Format

**AP → AFC: WHO AM I & WHERE I AM**

**AFC → AP: THE POWER & FREQUENCY YOU CAN USE**

10

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
AFC Request/Response Format
AP — AFC: AVAILABLESPECTRUMINQUIRYREQUEST
"location": { "ellipse": {
"center": { "Latitude": 40.7935,
"Longitude": -—77.8684 },
“majorAxis": 41, “minorAxis": 41 } },
"deviceDescriptor": { "serialNumber": .. }
AFC > AP: AVAILABLESPECTRUMINQUIRYRESPONSE
THE POWER & FREQUENCY "availableChannellInfo": [{
YOU CAN USE
"channelCfi": [1, 5, 9, 13, J],
"maxEirp": [32.4, 32.4, «] }],
"availabilityExpireTime":
"2025-09-18T18:58:562" // +24h
black hat
2026 10
```

## Slide 11

## A SYSTEM WITH NOTHING TO BREAK

11

## Slide 12

###### Simple Protocol & Secure Protection

REQ 1 Mutual authentication  between the AP and the AFC server
REQ 2
Integrity  of the AFC's internal databases
REQ 3
Accurate interference protection  computed on the AFC server

REQ 1
REQ 3

REQ 2

12

## Slide 13

###### Four Assumptions Hold Up 6 GHz

❶ HONEST ❷ HONEST ❸ UNTAMPERED LOCATION PARAMS CODE The AP reports its true Antenna height and power Firmware wasn't modified to geographic location. class match physical reality. falsify what it reports. Assumed. Assumed. Crypto ✓

❹ AUTHENTIC CHANNEL The AP AFC link preserves authenticity + integrity. Crypto ✓

The spec mandates ❸ and ❹ . It spends **nothing** verifying ❶ and ❷ .

13

## Slide 14

###### Threat Model 1

Attacker
SP AP AFC Server

_Can an attacker still attack the system, controlling allocated frequency & power (to over/under allocate), even_ **_without physical access to the AP_** _?_

14

## Slide 15

###### Location Spoofing Attacks against AFC Systems

5 Interference
4
Spoofed Location
2
1 FS Receiver
SP AP
3
Location Spoofer
FS Transmitter

15

## Slide 16

###### Overview of GPS Spoofing

Satellite B
Satellite A
Location
Spoofer
GPS
Victim
Receiver
Receiver

16

## Slide 17

###### Wi-Fi Positioning Spoofing

Location
Server
SP AP
APs in New York City
in Las Vegas
retrieved from public
database
Location Spoofer

17

## Slide 18

###### Experiment Setup For Location Spoofing Attacks

Transmitter:

- USRP B210

Software:

- GPS-SDR-SIM (GPS)

- gr-802-11 (Wi-Fi)

- APs Tested:

- HPE Aruba AP-634

- RUCKUS T670

- Ubiquiti U7 Pro Outdoor

- ROG STRIX GS-BE18000

18

## Slide 19

DEMO: Wi-Fi Location Spoofing

19

## Slide 20

20

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ssh unifi_ SyNSec@192.168.137.120
i
) i QiscHaao yas 7.120
UsPm™ By NSecQlop.8 6: e 2's password:
Seppo ooopobopopebooooooeeck NOTICE eebedecboooicoicbioooicoiokistotaiok
01K
* By logging in to, accessing, or using any Ubiquiti product, you are
*
* signifying that you have read our Terms of Service (ToS) and End User
*
* License Agreement (EULA), understand their terms, and agree to be
*
* fully bound to them. The use of SSH (Secure Shell) can potentially
*
* harm Ubiquiti devices and result in lost access to them and their data
*
* By proceeding, you acknowledge that the use of SSH to modify device(s)
*
* outside of their normal operational scope, or in any manner
*
* inconsistent with the ToS or EULA, will permanently and irrevocably
*
* void any applicable warranty.
*
eek
| | | = /__| | PRODUCT: U7-Pro-Outdoor
| ial [ee || | VERSION: 8.4.6+18068.260111.0707
[27
Ubiquiti Inc. (c) 2010-2026 https: //www.ui.com
unifi_SyNSec@U7ProOutdoor:~# qtiwifilocation
-|Spoofer Shell
xamples
V2224
black hat
2026
```

## Slide 21

###### DNS and NTP Attacks

SP AP Internet
DNS Query/Resp
NTP Req/Resp
Inject Packets
Network Attacker

21

## Slide 22

###### Attack Summary

A1 A2 A3 A4 A5 A6
INTERFERE FOREIGN BAD TIME NTP DNS FORCE CVE
HPE ARUBA AP-634
GPS · Federated Wireless
RUCKUS T670
GPS · CommScope
UBIQUITI U7 PRO OUTDOOR
Wi-Fi · Qualcomm
ROG STRIX GS-BE18000
Wi-Fi · Wi-Fi Alliance
ATTACK PRESENTS  NOT SUCCESSFUL

22

## Slide 23

###### Interference Attack (A1)

- Generate the spoofing signal to a rural area

- The AP send the request with the spoofed coordinate to the AFC server

- • The server reply with **all channels available with maximum allowed power**

23

## Slide 24

###### Denial-of-Service Attacks (A2-A5)

Impact: No allowed channels in response, the AP cannot transmit in 6 GHz bands. **A2:** Spoof AP to an invalid location, e.g., a foreign country

**A3:** Send the GPS signal using invalid time

**A4, A5:** DoS by NTP and DNS Spoofing

24

## Slide 25

###### Force Location Update Attack (A6)

Previous Channel
Allocation Expires
1
Inject a Future Time
Vulnerable AP Attacker

25

## Slide 26

###### Force Location Update Attack (A6)

AP Regains
Accurate Time
2
Inject Current Time
Vulnerable AP Attacker

26

## Slide 27

###### Force Location Update Attack (A6)

##### Vulnerable AP

3
Inject Fake Location

Attacker

New AFC Request w/ Spoofed Location

27

## Slide 28

### WHAT IF THE ATTACKER OWNS THE DEVICE?

28

## Slide 29

###### Consumer-Level APs Give User Sufficient Control

###### Ubiquiti U7 Pro Outdoor

###### ROG STRIX GS-BE18000

29

## Slide 30

Threat Model 2

Attacker
SP AP AFC Server

With the **user-level access** to the AP, can an attacker attack the AFC system to **manipulate the frequency and power level** transmitted from the AP?

30

## Slide 31

###### The Root of Trust

##### **SP AP AFC Server** Verify Public KeyAccept and Encrypt Connection **Cert Store**

31

## Slide 32

###### The Root of Trust (Compromised)

SP AP Attacker
Verify Public KeyAccept and Encrypt Connection
Inject New Root CA
Cert Store

32

## Slide 33

###### Forge AFC Response

AFC Query
SP AP AFC Server
Attacker

33

## Slide 34

###### Force Channel Selection Attack

Only 20 MHz available

Only 1 channel available

34

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Force Channel
Selection Attack
"version": "1.4",
"ayailablespectruminguirykesponses": [ {
"requestId": "2483720664",
"response": {
"responseCode": 0O,
"shortDescription": "Success"
"rulesetId": "US 47 CFR PART 15 SUBPART_E",
MONE ota k-t Chae ian [ {
. requencyRange":
Only 20 MHz available "lowFrequency": 6845,
"highFrequency": 6865
LL
)) maxes’: 23
"availableChannellInfo": [{
Only 1 channel available nghannelefi": [181],
"maxEirp": [36.0]
tl,
"availabilityExpireTime": "2025-10-21T19:08:552"
black hat
34
```

## Slide 35

###### DEMO: Force Channel Selection Attack

35

## Slide 36

36

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
HHH RK KH HRY
void any applicable warranty.
JNSeRQi92. 37, m
mer 192. 100%R3 Ce ae is
OAC ARR RRR RR a oo a
By logging in to, accessing, or using any Ubiquiti product, you are
signifying that you have read our Terms of Service (ToS) and End User
License Agreement (EULA), understand their terms, and agree to be
fully bound to them. The use of SSH (Secure Shell) can potentially
harm Ubiquiti devices and result in lost access to them and their data.
By proceeding, you acknowledge that the use of SSH to modify device(s)
outside of their normal operational scope, or in any manner
inconsistent with the ToS or EULA, will permanently and irrevocably
ssh unifi_ SyNSec@192.168.137.101
NOTICE (RRR RRR RK ar
HHRHK KKH EE
SIGIR IOI ICO AC AOR ACCC HORACIO AOI ROI RIOR ACE
Ubiquiti Inc. (c) 2010-2026
unifi_SyNSec@U7Pro0utdoor:~# §j
PRODUCT: U7-Pro-Outdoor
MAC:
VERSION: 8.4.6+18068.260111.0707
https: //www.ui.com
— (Attacker Shell
annel_exp
*
black hat
2026
```

## Slide 37

###### Force Channel Selection Attack

AP forced to use channel 181

6 GHz channel disabled

37

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Force Channel Selection Attack
U7 Pro Outdoor
TX Retries
9m 51s
Ch. 11 (2.4 GHz, 20 MHz) 2x2 WiFi 7
Ch. 48 (5 GHz, 40 MHz) 2x2 WiFi 7
Ch. 181 (6 GHz, 20 MHz) 2x2 WiFi 7
(6 GHz, 20 MHz) 2x2 WiFi 7
AP forced to use channel 181
U7 Pro Outdoor
6 GHz is currently disabled. The AP did not
receive an AFC response for this location and
will automatically retry. Learn more
TX Retries
Ch. 11 (2.4 GHz, 20 MHz) 2x2 WiFi 7
Ch. 48 (5 GHz, 40 MHz) 2x2 WiFi 7
6 GHz channel disabled
black hat
2026 37
```

## Slide 38

###### Send Requests From Client to Server

AFC Query
SP AP AFC Server
Attacker

38

## Slide 39

###### The Ubiquiti/Qualcomm Approach: Shared Secret+JWT Token

1. Find the HTTP endpoint for AFC

2. Extract the shared secret from the connection

`TLS MitM  ·  U7-PRO-OUTDOOR  →  QUALCOMM` **`POST /device/0c18f25c-XXXX-XXXX-XXXX-XXXXXXXXXXXX/`** `api.qcs` **`{"api_version":1,"request_type":"request_authToken",`** ← the tuple **`"uid":"16165XXXXX","oem_id":"536","prd_id":"42662", "shared_secret":"HxnT5bXXXXXXXXXXXXXXXX",`** ← cleartext in the session **`"application":"AFC"}`**

3. Use the shared secret to obtain JWT token

4. Attach the JWT token to the AFC request

**`HTTP/1.1 200 OK`** `Server: gunicorn {"status":"OK","auth_token":"eyJhbGciOiJIUzI1NiIs..."} JWT  header {"alg":"HS256","typ":"JWT"} claims {"exp":1767293788,` 30-day life `"app":"AFC", "uid":"7881175f-XXXX-XXXX-XXXXXXXXXXXX", "certs":[["CA","6545A-U7PROO"], ["US","SWX-U7PROO"]]}` **`POST /afc_client_api/afc_api/`** `afcapi.qcs` **`Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...`** ← no Bearer

Serial, shared secret, service path and token identity are masked.

39

## Slide 40

###### The ASUS/Wi-Fi Alliance Approach: Mutual TLS

```
ASUS GS-BE18000  ·  SHELL
```

1. Find the HTTP endpoint for AFC

2. Extract client certificate from the device

```
admin@GS-BE18000-CB50:/# nvram show | grep afc_
afc_cert_id=MSQ-XXXXXXXX
```

```
afc_dev_serial_no=XXXXXXXXXXXXXXX
```

```
afc_freq_range=5925,6425;6525,6875
```

```
afc_geo_from=source_wifi
```

3. Use the certificate to connect to the server

```
afc_in_wifiaplist={"considerIp":"false","wifiAccessPoints":[
  {"macAddress":"XX:XX:XX:XX:XX:XX","signalStrength":-20}, ...
afc_insecure=0
```

```
afc_loc_height_type=AGL
```

**`afc_mtls_cert=/jffs/.sys/afc/afc_mtls_cacert.pem`** ← cert path `afc_op_class=131,132,133,134,137`

```
afc_out_lat=XX.XXXXXXX
```

```
afc_out_lng=-XX.XXXXXX
```

```
afc_reg_rules=US_47_CFR_PART_15_SUBPART_E
afc_sp=1
```

**`afc_url=https://mtls-access.afc.wi-fi.com/api/XXXXXXXX`** ← endpoint

Serial number, MAC addresses, coordinates and the API token are masked.

40

## Slide 41

###### Resource Exhaustion on AFC Server

- AFC request consumes a considerable amount of computation power of the server

- A single request can take 10-20 seconds with our testbed and Open AFC

- Attacker can launch DDoS attacks with the capability to send the requests as a device

###### Concurrent Requests VS. Response Time on Open AFC

41

## Slide 42

###### How are Interference Impacting FS?

- Columbus and Fortson, GA - 9.5 mi

- inside shops beneath a working utility 6 GHz microwave link

- low-power, indoor, AFC-exempt AP were enough to cause harmful interference

- beacon frames alone (no connected client, no data): ~32 dB past the threshold.

**PEAK INTERFERENCE (I/N) INTO THE FS RECEIVER VS. DISTANCE**

 20
no client   no data tra  ic
  0
0
            FCC  A  F        F    C
  0
0.   mi  .0 mi 3.0 mi  .  mi  .  mi

<u>https://www.epri.com/research/programs/062333/results/3002022241</u>

42

## Slide 43

###### How an Attacker May Exploit AFC?

`RECON` FS Record FS link information is public

43

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
How an Attacker May Exploit AFC?
RECON FS Record
FS link information is public
Miami-Dade 6 GHz Microwave Call Signs
Wi
Ww
Ww
Ww
Ww
Ww
Ww
Ww
Ww
Ww
Ww
Ww
Ww
Ww
Ww
Ww
Wi
Wi
Wi
)
1
23
69
79
86
88
92
95
96
99
03
05
08
14
17
7
18
19
Federal
(or Communications
Commission
Universal Licensing System
FCC > WTB > ULS > Online Systems > License Search
License Search
Search Results
Q New Search Q Refine Search & Printable Page
Specified Search
Radio Service =|CF, MG, MW
Name like MIAMI-DADE
Status = Active
Frequency Upper Band >= 5925
Frequency Assigned <= 7125
@ Query Download
<'> Map Licenses
black hat
2026 43
```

## Slide 44

###### How an Attacker May Exploit AFC?

`RECON` FS Record FS link information is public

44

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
How an Attacker May Exploit AFC?
RECON FS Record
FS link information is public
Communications
Commission
FE Federal FCC Home | Search | Updates | E-Filing | Initiatives | For Consumers | Find People
Miami-Dade 6 GHz Microwave Call Signs
9 Universal
23 License Search
Search Results
169 Q New Search Q Re
9
Radio Service = CF, MG, MW
186 Name like MIAMI-DADE
Status = Active
Frequency Upper Band >= 5925,
Frequency Assigned <= 7125
ending Application(s)
fermination Pending
Page 123
Call Sign/Lease ID FRN Radio Service Status
MIAMI-DADE COUNTY 0001802735 Active 10/17/2031
Miami-Dade County 0001802735 Active 03/19/2029
Miami-Dade County 0001802735 Active 03/19/2029
MIAMI-DADE COUNTY 0001802735 Active 01/26/2030
MIAMI-DADE COUNTY 0015402795 Active 09/30/2030
MIAMI-DADE COUNTY 0015402795 Active 09/30/2030
MIAMI-DADE COUNTY 0015402795 Active 09/30/2030
MIAMI-DADE COUNTY 0015402795 Active 09/30/2030
MIAMI-DADE COUNTY 0015402795 Active 09/30/2030
MIAMI-DADE COUNTY 0015402795 Active 09/30/2030
Call Sign/Lease ID FRN i Status Expiration Date
EEEEEEEEEESE
OOD OND DOD OTF
Page 123
ff SSS SESS EEE HEHEHE
black hat
2026 44
```

## Slide 45

###### How an Attacker May Exploit AFC?

`RECON` FS Record

FS link information is public

45

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
How an Attacker May Exploit AFC?
RECON FS Record
FS link information is public
ULS License
Microwave Public Safety Pool License - WP 2 - MIAMI-DADE COUNTY
Q New Search Q Refine Search [jp Return to Results (By Printable Page fy Reference Copy <4» Map License
ADMIN LOCATIONS
Call Sign wr Radio Service MW - Microwave Public Safety Pool
Status Active Auth Type Regular
Dates
Grant 09/24/2021 Expiration 10/17/2031
Effective 12/29/2022 Cancellation
Control Points
None
FRN og Governmental Entity
(View Ownership Filing)
Licensee
MIAMI-DADE COUNTY 2 J
5680 SW 87th Ave . p72
MIAMI, FL 33173 dade.gov
ATTN ITD Radio Communications Division
Contact
MIAMI-DADE COUNTY , B909
Miguel D Luna t 396
5680 SW 87th Ave ipjdade.gov
MIAMI, FL 33173
ATTN ITD Radio Division
Microwave Data
Oper Type Permanent Fixed Point to Point Station Class FXO - Operational Fixed
Ownership and Qualifications
Radio Service Type Fixed bl k al t
Prats Comm Trrcoanadad We ac a
USA
2026 45
```

## Slide 46

###### How an Attacker May Exploit AFC?

`RECON` FS Record FS link information is public

46

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
How an Attacker May Exploit AFC?
RECON FS Record
FS link information is public
LOCATIONS
Call Sign WPJE410
2 Total Locations
< ions per Summary Page
Fixed Transmit Location 1:
MIAM GARAGE #4
MIAMI, FL
MIAMI-DADE County
Site Elevation
(AMSL)
ASR #/File #
Support Structure Type
NEPA Required
Quiet Zone Notification Date
Is coordination with Canada required?
Is coordination with Mexico required?
Special Conditions
Other Locations
Location 2 : 1049
Type
Site Elevation
(AMSL)
ASR #/File #
Receive Location
3.0m
N/A
Radio Service MW - Microwave Public Safety Pool
Coordinates
Height w/o
Appurtenances
Height w/
Appurtenances
Quiet Zone Consent
Coordinates
Height w/o
Appurtenances
Height w/
Appurtenances
black hat
2026 46
```

## Slide 47

###### How an Attacker May Exploit AFC?

`RECON` FS Record FS link information is public

47

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
How an Attacker May Exploit AFC?
RECON FS Record
FS link information is public
_—
(MAIN (ADMIN )( LOCATIONS PATHS MAP
ve 10 adio Service MW - Microwave Public Safety Pool
black hat
2026 47
```

## Slide 48

###### How an Attacker May Exploit AFC?

`RECON` FS Record FS link information is public

`SPOOF` Side Channel Off-path spoofing of location/time side channel

`ATTACK` Re-query Wait for 24-hour AFC requery or force

48

## Slide 49

###### How an Attacker May Exploit AFC?

`RECON` FS Record FS link information is public

`SPOOF` Side Channel Off-path spoofing of location/time side channel

`ATTACK` Re-query Wait for 24-hour AFC requery or force

1 Interfere

2 Coordinated

3 DoS

49

## Slide 50

###### How an Attacker May Exploit AFC?

`RECON` FS Record FS link information is public

`SPOOF` Side Channel Off-path spoofing of location/time side channel

`ATTACK` Re-query Wait for 24-hour AFC requery or force

`EXIT` Persist Effect Attacker can stop transmission while AP keeps broadcast/DoS

1 Interfere

2 Coordinated

3 DoS

50

## Slide 51

# SOLUTIONS?

51

## Slide 52

###### Geofencing

- Standard Power APs are not designed for mobile use

- Pre-define a small possible operation area and stop transmission if outside

- Discussed and recommended by some vendors

52

## Slide 53

###### Securing Device and Server Implementations

SP AP

###### AFC SERVER

```
ON THE AP
```

```
ON THE TLS LINK
```

```
ON THE AFC SERVER
```

Lock down AFC parameters

Certificate pinning

Rate limit requests

No user access to the certificate and key, or to the shared secrets.

The AP rejects any root CA an attacker injects into its store.

Per device and per IP address — one query costs 10–20 s of compute.

53

## Slide 54

# TAKEAWAYS

54

## Slide 55

###### Takeaways

- The security of the AFC system is critically dependent on the integrity of its inputs and implementation.

- This trust model in spec is incomplete, as low-cost spoofing attacks can cause severe interference or denial-of-service to critical incumbent systems.

- No device being tested is completely secure and can all lead to harmful interference and large-scale DoS attacks when attacked.

55

## Slide 56

###### Acknowledgments

```
DISCUSSIONS & TECHNICAL ASSISTANCE
```

- **EPRI:** David Waters, Tim Godfrey, Jay Herman

▸ **Univ. of Notre Dame:** Dr. M. Rochman, Dr. M. Ghosh

- **AT&T Labs:** Dr. Thomas Willis

- **Lockard & White:** David Hattey

- **INL:** John Beck, Nathaniel Bennett

```
FUNDING & SUPPORT
```

This work is supported by a research grant and collaboration from the following institutions:

▸ **DOE CESER** Department of Energy Office of Cybersecurity, Energy Security, and Emergency Response

▸ **INL** Idaho National Laboratory

56
