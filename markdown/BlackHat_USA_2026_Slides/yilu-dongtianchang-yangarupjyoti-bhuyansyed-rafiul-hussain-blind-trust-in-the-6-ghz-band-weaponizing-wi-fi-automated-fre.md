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
text_chars: 20380
ocr_pages: 10
has_ocr: true
redacted_secrets: 0
ocr_confidence: 89.5
ocr_unreliable_blocks: 1
vision_verified_pages_changed: 56
vision_verified_pages: 56
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:47:27Z"
---
# Blind Trust in the 6 GHz Band Weaponizing Wi-Fi Automated Frequency Coordination (AFC)

**Speakers:** Yilu Dong, Tianchang Yang, Arupjyoti Bhuyan, Syed Rafiul Hussain  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/Yilu Dong&Tianchang Yang&Arupjyoti Bhuyan&Syed Rafiul Hussain_Blind Trust in the 6 GHz Band Weaponizing Wi-Fi Automated Frequency Coordination (AFC).pdf` (56 pages)


## Slide 1

This slide carries no title or text of its own.

## Slide 2

BLIND TRUST IN THE 6 GHZ BAND

Weaponizing Wi-Fi Automated Frequency Coordination (AFC)

**Yilu Dong**, **Tianchang Yang**, Syed Rafiul Hussain — The Pennsylvania State University

Arupjyoti Bhuyan — Idaho National Laboratory

## Slide 3

###### About Us

###### **Yilu Dong**

- Research Assistant, The Pennsylvania State University

- Wireless protocol and systems security, applied cryptography, vulnerability discovery: 5G systems, Wi-Fi AFC systems

- <u>`yilud.me`</u>

###### **Tianchang Yang**

- Research Assistant, The Pennsylvania State University

- Wi-Fi systems, Mobile network security, resiliency, and robustness: 5G, Open RAN, baseband (fuzzing, program analysis, ML)

- <u>`tianchang-yang.github.io`</u>

## Slide 4

###### Interference Broke a Life-Safety Network

Miami-Dade built a new 6 GHz public-safety microwave system for first responders, engineered for **99.999% reliability**. **It couldn't go into service.**

**NOV 2020**

**Degradation detected.** In acceptance testing, the new link underperforms; kept out of service.

**DEC 2021**

**~1 year to find one source:** an out-of-band device, hidden by frequency hopping.

**2022**

**It re-offends;** two more interferers surface after months of additional investigation

**NOV 2022**

Formal warning reaches **one** offender. **Two years on** – the interference still continuous and the **system continuous to suffer from harmful interference**

<u>https://www.apcointl.org/~documents/filing/apco-ex-parte-6ghz-miami-dade-112222</u>

## Slide 5

###### Interference Broke a Life-Safety Network

Miami-Dade built a new 6 GHz public-safety microwave system for first responders, engineered for **99.999% reliability**. **It couldn't go into service.**

**NOV 2020**

**Degradation detected.** In acceptance testing, the new link underperforms; kept out of service.

**DEC 2021**

**~1 year to find one source:** an out-of-band device, hidden by frequency hopping.

**2022**

**It re-offends;** two more interferers surface after months of additional investigation

**NOV 2022**

Formal warning reaches **one** offender. **Two years on** – the interference still continuous and the **system continuous to suffer from harmful interference**

## AND THIS WAS AN ACCIDENT

The offenders were unintentional and never hid

What if an attacker induces the same interference on purpose, from a legally-authorized AP device/network transmitting within the rules — then stops and leaves nothing to trace

<u>https://www.apcointl.org/~documents/filing/apco-ex-parte-6ghz-miami-dade-112222?layout=file</u>

## Slide 6

###### The Biggest Spectrum Release in Decades font size

**2.4 GHZ** — ~ 80 MHz · saturated

**5 GHZ** — ~ 500 MHz · congested

**6 GHZ** — 1,200 MHz · opened for unlicensed Wi-Fi

In 2020 the FCC opened **1,200 MHz** at 6 GHz (5.925–7.125 GHz) for commercial use — more contiguous spectrum than everything below it combined, released almost overnight for Wi-Fi 6E and Wi-Fi 7.

## Slide 7

###### The Biggest Spectrum Release in Decades font size

**2.4 GHZ** — ~ 80 MHz · saturated

**5 GHZ** — ~ 500 MHz · congested

**6 GHZ** — 1,200 MHz · opened for unlicensed Wi-Fi

In 2020 the FCC opened **1,200 MHz** at 6 GHz (5.925–7.125 GHz) for commercial use — more contiguous spectrum than everything below it combined, released almost overnight for Wi-Fi 6E and Wi-Fi 7.

#### 6 GHZ WAS NEVER EMPTY

Fixed Service (FS) microwave links have carried mission-critical traffic across this band for decades. Wi-Fi is the newcomer moving in on top of them.

###### PUBLIC SAFETY

###### CONTROL SIGNALS

###### SCIENCE

###### MOBILE BACKHAUL

## Slide 8

###### 40× Transmit Energy

- **Standard Power (SP)** APs transmit far hotter than indoor units: up to **36 dBm EIRP** (≈ 4 W).

- That power buys range — but also the ability to **reach an incumbent's receiver kilometers away.**

- So the FCC forbids an SP AP from transmitting until it **asks permission.**

| Low-power Indoor AP | ≤30 dBm |
| USRP B210 Jammer | ~20 dBm |
| **Standard Power Max** | **36 dBm** |

Every +3 dB doubles radiated power. 36 vs 20 dBm ≈ **40× the energy**

## Slide 9

###### AFC: Automated Frequency Coordination

**Standard Power (SP) Access Points (AP)** → Identity, Location, Antenna, Power Class → **AFC SERVER**

**AFC SERVER** → Permitted Channels, Max Power → **Standard Power (SP) Access Points (AP)**

- Simplifies and automates similar systems in other bands (e.g., CBRS in 3.5 GHz bands)

- The AP reports its identity, location, antenna height, and power class to the AFC server.

- The server checks that location against a **database of protected incumbent receivers** and a propagation model, and works out which channels and power levels won't interfere with them.

- AFC returns an **allocation**: channels and the maximum power the AP is allowed to use.

- The allocation is a **lease valid for 24 hours**. When it expires, the AP has to ask again before it can keep transmitting.

## Slide 10

###### AFC Request/Response Format

**AP → AFC: WHO AM I & WHERE I AM**

```
AVAILABLESPECTRUMINQUIRYREQUEST

"location": { "ellipse": {
    "center": { "latitude":  40.7935,
                "longitude": -77.8684 },
    "majorAxis": 41, "minorAxis": 41 } },
"deviceDescriptor": { "serialNumber": … }
```

**AFC → AP: THE POWER & FREQUENCY YOU CAN USE**

```
AVAILABLESPECTRUMINQUIRYRESPONSE

"availableChannelInfo": [{
    "channelCfi": [1, 5, 9, 13, …],
    "maxEirp":    [32.4, 32.4, …] }],
"availabilityExpireTime":
    "2025-09-18T18:58:56Z"   // +24h
```

## Slide 11

## A SYSTEM WITH NOTHING TO BREAK

## Slide 12

###### Simple Protocol & Secure Protection

**REQ 1** — **Mutual authentication** between the AP and the AFC server

**REQ 2** — **Integrity** of the AFC's internal databases

**REQ 3** — **Accurate interference protection** computed on the AFC server

**STANDARD POWER ACCESS POINT** → availableSpectrumInquiryReq · MUTUAL AUTH · TLS · availableSpectrumInquiryRsp → **AFC SERVER**

AFC SERVER — KEY FUNCTIONS: Device Responder · Spectrum · Database Update · Activity Logging · Interference Protection · Internal Database

NRA Incumbent Database · NRA Equipment Authorization Database

**REQ 1** · **REQ 3** · **REQ 2**

## Slide 13

###### Four Assumptions Hold Up 6 GHz

**① HONEST LOCATION**

The AP reports its true geographic location.

Assumed.

**② HONEST PARAMS**

Antenna height and power class match physical reality.

Assumed.

**③ UNTAMPERED CODE**

Firmware wasn't modified to falsify what it reports.

Crypto ✓

**④ AUTHENTIC CHANNEL**

The AP↔AFC link preserves authenticity + integrity.

Crypto ✓

The spec mandates ③ and ④. It spends **nothing** verifying ① and ②.

## Slide 14

###### Threat Model 1

Attacker

SP AP ↔ AFC Server

_Can an attacker still attack the system, controlling allocated frequency & power (to over/under allocate), even_ **_without physical access to the AP_**_?_

## Slide 15

###### Location Spoofing Attacks against AFC Systems

① FS Transmitter

② SP AP

③ Location Spoofer

④ Spoofed Location

⑤ Interference

FS Receiver

## Slide 16

###### Overview of GPS Spoofing

Satellite A

Satellite B

GPS Receiver

Victim Receiver

Location Spoofer

## Slide 17

###### Wi-Fi Positioning Spoofing

SP AP in Las Vegas

Location Server

APs in New York City retrieved from public database

Location Spoofer

## Slide 18

###### Experiment Setup For Location Spoofing Attacks

Transmitter:

- USRP B210

Software:

- GPS-SDR-SIM (GPS)

- gr-802-11 (Wi-Fi)

APs Tested:

- HPE Aruba AP-634

- RUCKUS T670

- Ubiquiti U7 Pro Outdoor

- ROG STRIX GS-BE18000

_GPS Spoofing Transmitter_

_Victim AP w/ GPS Receiver_

## Slide 19

###### DEMO: Wi-Fi Location Spoofing

## Slide 20

###### AP Shell

###### Spoofer Shell

```
ssh unifi_SyNSec@192.168.137.120
unifi_SyNSec@192.168.137.120's password:

*********************** NOTICE ***********************
* By logging in to, accessing, or using any Ubiquiti product, you are
* signifying that you have read our Terms of Service (ToS) and End User
* License Agreement (EULA), understand their terms, and agree to be
* fully bound to them. The use of SSH (Secure Shell) can potentially
* harm Ubiquiti devices and result in lost access to them and their data.
* By proceeding, you acknowledge that the use of SSH to modify device(s)
* outside of their normal operational scope, or in any manner
* inconsistent with the ToS or EULA, will permanently and irrevocably
* void any applicable warranty.
*****************************************************

PRODUCT: U7-Pro-Outdoor
MAC:
VERSION: 8.4.6+18068.260111.0707
Ubiquiti Inc. (c) 2010-2026    https://www.ui.com
unifi_SyNSec@U7ProOutdoor:~# qtiwifilocation
```

## Slide 21

###### DNS and NTP Attacks

SP AP ↔ Internet

DNS Query/Resp

NTP Req/Resp

Inject Packets

Network Attacker

## Slide 22

###### Attack Summary

| Device | A1 INTERFERE | A2 FOREIGN | A3 BAD TIME | A4 NTP | A5 DNS | A6 FORCE CVE |
| --- | :---: | :---: | :---: | :---: | :---: | :---: |
| **HPE ARUBA AP-634** (GPS · Federated Wireless) | ● | ● | ● | ● | ● | ● |
| **RUCKUS T670** (GPS · CommScope) | ● | ● | ● | ○ | ● | ○ |
| **UBIQUITI U7 PRO OUTDOOR** (Wi-Fi · Qualcomm) | ● | ● | ● | ● | ● | ○ |
| **ROG STRIX GS-BE18000** (Wi-Fi · Wi-Fi Alliance) | ● | ● | ● | ● | ● | ○ |

● ATTACK PRESENTS   ○ NOT SUCCESSFUL

## Slide 23

###### Interference Attack (A1)

- Generate the spoofing signal to a rural area

- The AP send the request with the spoofed coordinate to the AFC server

- The server reply with **all channels available with maximum allowed power**

```
Max EIRP of AFC channel
20MHz channel      1    5    9   13   17   21   25   29   33   37   41   45   49   53   57   61   65   69   73   77   81
Max Eirp        36.0 36.0 36.0 36.0 36.0 36.0 36.0 36.0 36.0 36.0 36.0 36.0 36.0 36.0 36.0 36.0 36.0 36.0 36.0 36.0 36.0
20MHz channel     85   89   93  117  121  125  129  133  137  141  145  149  153  157  161  165  169  173  177  181
Max Eirp        36.0 36.0 36.0 36.0 36.0 36.0 36.0 36.0 36.0 36.0 36.0 36.0 36.0 36.0 36.0 36.0 36.0 36.0 36.0 36.0
40MHz channel      1    9   17   25   33   41   49   57   65   73   81   89  121  129  137  145  153  161  169  177
Max Eirp        36.0 36.0 36.0 36.0 36.0 36.0 36.0 36.0 36.0 36.0 36.0 36.0 36.0 36.0 36.0 36.0 36.0 36.0 36.0 36.0
80MHz channel      1   17   33   49   65   81  129  145  161
Max Eirp        36.0 36.0 36.0 36.0 36.0 36.0 36.0 36.0 36.0
160MHz channel     1   33   65  129
Max Eirp        36.0 36.0 36.0 36.0
320MHz_1 channel   1
Max Eirp        36.0
320MHz_1 channel  33
Max Eirp        36.0
```

## Slide 24

###### Denial-of-Service Attacks (A2-A5)

Impact: No allowed channels in response, the AP cannot transmit in 6 GHz bands.

**A2:** Spoof AP to an invalid location, e.g., a foreign country

**A3:** Send the GPS signal using invalid time

**A4, A5:** DoS by NTP and DNS Spoofing

```
Received afc channels
---------------------
PHY Type                Allowed Channels
--------                ----------------
6GHz                    None
6GHz 40MHz              None
6GHz 80MHz              None
6GHz 160MHz             None
6GHz 80+80MHz           None
6GHz 320MHz_1           None
6GHz 320MHz_2           None
Present time            2025-06-20 11:36:04
Expiry time             None
Country code            None
AFC channel expired     Yes
AFC channel required    Yes
```

## Slide 25

###### Force Location Update Attack (A6)

Previous Channel Allocation Expires

Vulnerable AP

① Inject a Future Time

Attacker

## Slide 26

###### Force Location Update Attack (A6)

AP Regains Accurate Time

Vulnerable AP

② Inject Current Time

Attacker

## Slide 27

###### Force Location Update Attack (A6)

Vulnerable AP

③ Inject Fake Location

Attacker

New AFC Request w/ Spoofed Location

## Slide 28

### WHAT IF THE ATTACKER OWNS THE DEVICE?

## Slide 29

###### Consumer-Level APs Give User Sufficient Control

###### Ubiquiti U7 Pro Outdoor

###### ROG STRIX GS-BE18000

## Slide 30

###### Threat Model 2

SP AP ↔ AFC Server

Attacker — Shell Access → SP AP

With the **user-level access** to the AP, can an attacker attack the AFC system to **manipulate the frequency and power level** transmitted from the AP?

## Slide 31

###### The Root of Trust

SP AP ↔ AFC Server

SP AP → Cert Store

Verify Public Key → Accept and Encrypt Connection

## Slide 32

###### The Root of Trust (Compromised)

SP AP ↔ Attacker

SP AP → Cert Store

Verify Public Key → Accept and Encrypt Connection

Attacker → Inject New Root CA → Cert Store

## Slide 33

###### Forge AFC Response

SP AP · Attacker · AFC Server

AFC Query (SP AP ↔ AFC Server)

AFC Query (SP AP ↔ Attacker)

## Slide 34

###### Force Channel Selection Attack

Only 20 MHz available

Only 1 channel available

```
{
  "version": "1.4",
  "availableSpectrumInquiryResponses": [{
    "requestId": "2483720664",
    "response": {
      "responseCode": 0,
      "shortDescription": "Success"
    },
    "rulesetId": "US_47_CFR_PART_15_SUBPART_E",
    "availableFrequencyInfo": [{
      "frequencyRange": {
        "lowFrequency": 6845,
        "highFrequency": 6865
      },
      "maxPsd": 23
    }],
    "availableChannelInfo": [{
      "globalOperatingClass": 131,
      "channelCfi": [181],
      "maxEirp": [36.0]
    }],
    "availabilityExpireTime": "2025-10-21T19:08:55Z"
  }]
}
```

## Slide 35

###### DEMO: Force Channel Selection Attack

## Slide 36

###### AP Shell

```
ssh unifi_SyNSec@192.168.137.101

*********************** NOTICE ***********************
* By logging in to, accessing, or using any Ubiquiti product, you are
* signifying that you have read our Terms of Service (ToS) and End User
* License Agreement (EULA), understand their terms, and agree to be
* fully bound to them. The use of SSH (Secure Shell) can potentially
* harm Ubiquiti devices and result in lost access to them and their data.
* By proceeding, you acknowledge that the use of SSH to modify device(s)
* outside of their normal operational scope, or in any manner
* inconsistent with the ToS or EULA, will permanently and irrevocably
* void any applicable warranty.
*****************************************************

PRODUCT: U7-Pro-Outdoor
MAC:
VERSION: 8.4.6+18068.260111.0707
Ubiquiti Inc. (c) 2010-2026    https://www.ui.com
unifi_SyNSec@U7ProOutdoor:~#
```

###### Attacker Shell

`gps-sdr-sim`

## Slide 37

###### Force Channel Selection Attack

**AP forced to use channel 181**

U7 Pro Outdoor — Connected To -

AirView

TX Retries — Low (0%)

11:10 PM   11:10 AM   Now

↓ 512 bps   ↑ 3.13 Kbps      9m 51s

Ch. 11 (2.4 GHz, 20 MHz)   2x2   WiFi 7   0
Ch. 48 (5 GHz, 40 MHz)   2x2   WiFi 7   0
Ch. 181 (6 GHz, 20 MHz)   2x2   WiFi 7   0

**6 GHz channel disabled**

U7 Pro Outdoor — Connected To -

AirView

⚠ 6 GHz is currently disabled. The AP did not receive an AFC response for this location and will automatically retry. Learn more

TX Retries — Low (0%)

11:05 PM   11:05 AM   Now

↓ 1.22 Kbps   ↑ 38.8 Kbps      3m 35s

Ch. 11 (2.4 GHz, 20 MHz)   2x2   WiFi 7   0
Ch. 48 (5 GHz, 40 MHz)   2x2   WiFi 7   0
Ch. Auto (6 GHz, 20 MHz)   2x2   WiFi 7   0

## Slide 38

###### Send Requests From Client to Server

SP AP · Attacker · AFC Server

AFC Query (SP AP ↔ AFC Server)

Credentials (SP AP ↔ Attacker)

AFC Query (Attacker ↔ AFC Server)

## Slide 39

###### The Ubiquiti/Qualcomm Approach: Shared Secret+JWT Token

1. Find the HTTP endpoint for AFC

2. Extract the shared secret from the connection

3. Use the shared secret to obtain JWT token

4. Attach the JWT token to the AFC request

```
TLS MitM  ·  U7-PRO-OUTDOOR  →  QUALCOMM

POST /device/0c18f25c-XXXX-XXXX-XXXX-XXXXXXXXXXXX/    api.qcs
{"api_version":1,"request_type":"request_authToken",    ← the tuple
 "uid":"16165XXXXX","oem_id":"536","prd_id":"42662",
 "shared_secret":"HxnT5bXXXXXXXXXXXXXXXX",    ← cleartext in the session
 "application":"AFC"}

HTTP/1.1 200 OK    Server: gunicorn
{"status":"OK","auth_token":"eyJhbGciOiJIUzI1NiIs..."}

JWT   header {"alg":"HS256","typ":"JWT"}
      claims {"exp":1767293788,    30-day life
              "app":"AFC",
              "uid":"7881175f-XXXX-XXXX-XXXXXXXXXXXX",
              "certs":[["CA","6545A-U7PROO"],
                       ["US","SWX-U7PROO"]]}

POST /afc_client_api/afc_api/    afcapi.qcs
Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...    ← no Bearer
```

Serial, shared secret, service path and token identity are masked.

## Slide 40

###### The ASUS/Wi-Fi Alliance Approach: Mutual TLS

1. Find the HTTP endpoint for AFC

2. Extract client certificate from the device

3. Use the certificate to connect to the server

```
ASUS GS-BE18000  ·  SHELL

admin@GS-BE18000-CB50:/# nvram show | grep afc_
afc_cert_id=MSQ-XXXXXXXX
afc_dev_serial_no=XXXXXXXXXXXXXXX
afc_freq_range=5925,6425;6525,6875
afc_geo_from=source_wifi
afc_in_wifiaplist={"considerIp":"false","wifiAccessPoints":[
  {"macAddress":"XX:XX:XX:XX:XX:XX","signalStrength":-20}, ...
afc_insecure=0
afc_loc_height_type=AGL
afc_mtls_cert=/jffs/.sys/afc/afc_mtls_cacert.pem    ← cert path
afc_op_class=131,132,133,134,137
afc_out_lat=XX.XXXXXXX
afc_out_lng=-XX.XXXXXX
afc_reg_rules=US_47_CFR_PART_15_SUBPART_E
afc_sp=1
afc_url=https://mtls-access.afc.wi-fi.com/api/XXXXXXXX    ← endpoint
```

Serial number, MAC addresses, coordinates and the API token are masked.

## Slide 41

###### Resource Exhaustion on AFC Server

- AFC request consumes a considerable amount of computation power of the server

- A single request can take 10-20 seconds with our testbed and Open AFC

- Attacker can launch DDoS attacks with the capability to send the requests as a device

###### Concurrent Requests VS. Response Time on Open AFC

Chart — X-axis: Number of requests (0–1000); Y-axis: Response time (s). Legend: Mean, Max, Min, Mean–Max spread, Min–Mean spread, 180s.

## Slide 42

###### How are Interference Impacting FS?

- Columbus and Fortson, GA - 9.5 mi

- inside shops beneath a working utility 6 GHz microwave link

- low-power, indoor, AFC-exempt AP were enough to cause harmful interference

- beacon frames alone (no connected client, no data): ~32 dB past the threshold.

**PEAK INTERFERENCE (I/N) INTO THE FS RECEIVER VS. DISTANCE**

| Distance | I/N (dB) |
| --- | --- |
| 275 m (0.17 mi) | +25.7 |
| 1.6 km (1.0 mi) | +16.1 |
| 4.8 km (3.0 mi) | +4.4 |
| 8.9 km (5.5 mi) | -11.5 |
| 9.4 km (5.8 mi) | -13.3 |

beacons only · no client · no data traffic

-6 dB I/N · FCC HARMFUL-INTERFERENCE LINE

Fortson · Columbus

<u>https://www.epri.com/research/programs/062333/results/3002022241</u>

## Slide 43

###### How an Attacker May Exploit AFC?

**RECON** — **FS Record**: FS link information is public

Miami-Dade 6 GHz Microwave Call Signs (list of call signs — redacted)

**Federal Communications Commission — Universal Licensing System**

FCC > WTB > ULS > Online Systems > License Search

License Search — Search Results

New Search · Refine Search · Printable Page · Query Download · Map Licenses

Specified Search:
- Radio Service = **CF, MG, MW**
- Name like **MIAMI-DADE**
- Status = **Active**
- Frequency Upper Band >= **5925**
- Frequency Assigned <= **7125**

## Slide 44

###### How an Attacker May Exploit AFC?

**RECON** — **FS Record**: FS link information is public

Miami-Dade 6 GHz Microwave Call Signs (list of call signs — redacted)

**Federal Communications Commission — Universal Licensing System** · FCC > WTB > ULS > Online Systems > License Search

License Search — Search Results

New Search · Refine Search · Printable Page · Query Download · Map Licenses

Specified Search: Radio Service = **CF, MG, MW**; Name like **MIAMI-DADE**; Status = **Active**; Frequency Upper Band >= **5925**; Frequency Assigned <= **7125**

Matches 1-10 (of 27)

| # | Call Sign/Lease ID | Name | FRN | Radio Service | Status | Expiration Date |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | (redacted) | MIAMI-DADE COUNTY | 0001802735 | MW | Active | 10/17/2031 |
| 2 | (redacted) | Miami-Dade County | 0001802735 | MW | Active | 03/19/2029 |
| 3 | (redacted) | Miami-Dade County | 0001802735 | MW | Active | 03/19/2029 |
| 4 | (redacted) | MIAMI-DADE COUNTY | 0001802735 | MW | Active | 01/26/2030 |
| 5 | (redacted) | MIAMI-DADE COUNTY | 0015402795 | MW | Active | 09/30/2030 |
| 6 | (redacted) | MIAMI-DADE COUNTY | 0015402795 | MW | Active | 09/30/2030 |
| 7 | (redacted) | MIAMI-DADE COUNTY | 0015402795 | MW | Active | 09/30/2030 |
| 8 | (redacted) | MIAMI-DADE COUNTY | 0015402795 | MW | Active | 09/30/2030 |
| 9 | (redacted) | MIAMI-DADE COUNTY | 0015402795 | MW | Active | 09/30/2030 |
| 10 | (redacted) | MIAMI-DADE COUNTY | 0015402795 | MW | Active | 09/30/2030 |

PA = Pending Application(s) · TP = Termination Pending · L = Lease · Page 1 2 3

## Slide 45

###### How an Attacker May Exploit AFC?

**RECON** — **FS Record**: FS link information is public

ULS License — **Microwave Public Safety Pool License - WP (redacted) - MIAMI-DADE COUNTY**

MAIN · ADMIN · LOCATIONS · PATHS · MAP

New Search · Refine Search · Return to Results · Printable Page · Reference Copy · Map License

- Call Sign: (redacted) | Radio Service: MW - Microwave Public Safety Pool
- Status: Active | Auth Type: Regular

Dates: Grant 09/24/2021 | Expiration 10/17/2031 | Effective 12/29/2022 | Cancellation:

Control Points: None

Licensee: FRN (redacted) | Type: Governmental Entity

MIAMI-DADE COUNTY, 5680 SW 87th Ave, MIAMI, FL 33173, ATTN ITD Radio Communications Division (phone/fax/email redacted)

Contact: MIAMI-DADE COUNTY, Miguel D Luna, 5680 SW 87th Ave, MIAMI, FL 33173, ATTN ITD Radio Division (phone/fax/email redacted)

Microwave Data: Oper Type Permanent Fixed Point to Point | Station Class FXO - Operational Fixed

Ownership and Qualifications: Radio Service Type Fixed | Regulatory Status Private Comm | Interconnected No

## Slide 46

###### How an Attacker May Exploit AFC?

**RECON** — **FS Record**: FS link information is public

MAIN · ADMIN · LOCATIONS · PATHS · MAP

- Call Sign: WPJE410 | Radio Service: MW - Microwave Public Safety Pool
- 2 Total Locations · 10 Locations per Summary Page

**Fixed Transmit Location 1:**
- MIAM (redacted) GARAGE #4, MIAMI, FL, MIAMI-DADE County | Coordinates: 25-⋯ W (redacted)
- Site Elevation (AMSL): 1.5m | Height w/o Appurtenances: 42.7m
- ASR #/File #: N/A | Height w/ Appurtenances: 42.7m
- Support Structure Type: | NEPA Required: | Quiet Zone Notification Date: | Quiet Zone Consent:
- Is coordination with Canada required? | Is coordination with Mexico required?
- Special Conditions: None

**Other Locations — Location 2 : 1049**
- Type: Receive Location | Coordinates: 25-⋯ W (redacted)
- Site Elevation (AMSL): 3.0m | ASR #/File #: N/A

## Slide 47

###### How an Attacker May Exploit AFC?

**RECON** — **FS Record**: FS link information is public

MAIN · ADMIN · LOCATIONS · PATHS · MAP

Call Sign: (redacted) | Radio Service: MW - Microwave Public Safety Pool

**License Geography** — map of the FS microwave link path between its two endpoints

## Slide 48

###### How an Attacker May Exploit AFC?

**RECON** — **FS Record**: FS link information is public

**SPOOF** — **Side Channel**: Off-path spoofing of location/time side channel

**ATTACK** — **Re-query**: Wait for 24-hour AFC re-query or force

## Slide 49

###### How an Attacker May Exploit AFC?

**RECON** — **FS Record**: FS link information is public

**SPOOF** — **Side Channel**: Off-path spoofing of location/time side channel

**ATTACK** — **Re-query**: Wait for 24-hour AFC re-query or force

**1 Interfere**

**2 Coordinated**

**3 DoS**

## Slide 50

###### How an Attacker May Exploit AFC?

**RECON** — **FS Record**: FS link information is public

**SPOOF** — **Side Channel**: Off-path spoofing of location/time side channel

**ATTACK** — **Re-query**: Wait for 24-hour AFC re-query or force

**EXIT** — **Persist Effect**: Attacker can stop transmission while AP keeps broadcast/DoS

**1 Interfere**

**2 Coordinated**

**3 DoS**

## Slide 51

# SOLUTIONS?

## Slide 52

###### Geofencing

- Standard Power APs are not designed for mobile use

- Pre-define a small possible operation area and stop transmission if outside

- Discussed and recommended by some vendors

## Slide 53

###### Securing Device and Server Implementations

SP AP ↔ AFC SERVER

**ON THE AP** — **Lock down AFC parameters**: No user access to the certificate and key, or to the shared secrets.

**ON THE TLS LINK** — **Certificate pinning**: The AP rejects any root CA an attacker injects into its store.

**ON THE AFC SERVER** — **Rate limit requests**: Per device and per IP address — one query costs 10–20 s of compute.

## Slide 54

# TAKEAWAYS

## Slide 55

###### Takeaways

- The security of the AFC system is critically dependent on the integrity of its inputs and implementation.

- This trust model in spec is incomplete, as low-cost spoofing attacks can cause severe interference or denial-of-service to critical incumbent systems.

- No device being tested is completely secure and can all lead to harmful interference and large-scale DoS attacks when attacked.

## Slide 56

###### Acknowledgments

**DISCUSSIONS & TECHNICAL ASSISTANCE**

- **EPRI:** David Waters, Tim Godfrey, Jay Herman

- **Univ. of Notre Dame:** Dr. M. Rochman, Dr. M. Ghosh

- **AT&T Labs:** Dr. Thomas Willis

- **Lockard & White:** David Hattey

- **INL:** John Beck, Nathaniel Bennett

**FUNDING & SUPPORT**

This work is supported by a research grant and collaboration from the following institutions:

- **DOE CESER** — Department of Energy Office of Cybersecurity, Energy Security, and Emergency Response

- **INL** — Idaho National Laboratory

