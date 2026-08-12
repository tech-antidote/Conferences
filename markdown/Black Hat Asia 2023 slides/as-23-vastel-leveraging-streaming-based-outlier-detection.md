---
title: "Leveraging Streaming Based Outlier Detection"
speakers: ["Vastel"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2023"
edition: "ASIA"
year: 2023
source_pdf: "Black Hat Asia 2023 slides/AS-23-Vastel-Leveraging-Streaming-Based-Outlier-Detection.pdf"
pages: 42
sha256: "81f215c10011fec246ef174bbc0b278c7f8fbd124ac6796220130997aca64a3e"
text_chars: 11693
ocr_pages: 9
has_ocr: true
redacted_secrets: 0
ocr_confidence: 88.0
ocr_unreliable_blocks: 0
vision_verified_blocks: 1
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T03:49:46Z"
---
# Leveraging Streaming Based Outlier Detection

**Speakers:** Vastel  
**Conference:** Black Hat ASIA 2023  
**Source:** `Black Hat Asia 2023 slides/AS-23-Vastel-Leveraging-Streaming-Based-Outlier-Detection.pdf` (42 pages)


## Slide 1

##### Leveraging Streaming-Based Outlier Detection and SliceLine to Stop Heavily Distributed Bot Attacks Antoine Vastel, PhD  |  Head of Research, DataDome Konstantina Kontoudi, PhD  |  Lead Data Scientist, DataDome

#BHASIA   @BlackHatEvents

## Slide 2

#BHASIA   @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Select all images with
crosswalks
Click verify once there are none left.
Select all squares with Select all images with
bicycles crosswalks
If there are none, click skip Click verify once there are none left.
```

## Slide 3

#BHASIA   @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Select all squares with
fire hydrants
If there are none, click skip
```

## Slide 4

#BHASIA   @BlackHatEvents

## Slide 5

# **All these CAPTCHAs because of bad bots.**

#BHASIA   @BlackHatEvents

## Slide 6

## **But can we detect bad bots without CAPTCHAs?**

#BHASIA   @BlackHatEvents

## Slide 7

# **Introduction to (Bad) Bots**

#BHASIA   @BlackHatEvents

## Slide 8

#### What’s a bot?

###### Program to **automate actions** .

Can be used for positive purposes:

- Automated **website testing** .

Nefarious purposes:

- Test batch of **stolen credentials** .

- Generate **fake video views/retweets** .

#BHASIA   @BlackHatEvents

## Slide 9

#### Attacks conducted by bots

**Credential stuffing/account takeover** → Steal user accounts. **DDoS** → Make website/mobile app unavailable.

**Carding** → Test stolen credit cards.

**Vote manipulation** → Generate fake views, increase number of likes, retweets, etc.

#BHASIA   @BlackHatEvents

## Slide 10

net/http

#### Bot Technologies: HTTP Clients

Axios Aiohttp net/http Got Requests

Low CPU/RAM resources needed.

No JavaScript execution.

(Potentially) inconsistent:

- HTTP Headers

- TLS Fingerprints

#BHASIA   @BlackHatEvents

## Slide 11

net/http

###### Bot Technologies: Automated Browsers

Puppeteer + Selenium + Playwright + (headless) Chrome (headless) Firefox (headless) Webkit

More CPU/RAM resources needed.

Execute JavaScript (JS) natively.

Consistent **HTTP headers** and **TLS fingerprints** .

Potentially inconsistent browser fingerprint (JS).

#BHASIA   @BlackHatEvents

## Slide 12

# **How to detect bots?**

#BHASIA   @BlackHatEvents

## Slide 13

#### How to detect bots?

**Signatures** /(browser/TLS/ HTTP) fingerprints.

**Behavioral analysis:**

- Volume of requests.

- Browsing patterns.

**Reputation:** IP/session, proxy detection.

**Context:** country, time of the day, website targeted.

#BHASIA   @BlackHatEvents

## Slide 14

#### Detection Example: Selenium

Detection using browser fingerprinting (JS). Selenium introduces attribute: **document.$cdc_asdjflasutopfhvcZLmcfl_**

#BHASIA   @BlackHatEvents

## Slide 15

#### Bypass Techniques Used by Bots

Forge TLS fingerprints.

Forge browser fingerprint and HTTP headers. <u>https://github.com/intoli/user-agents</u>

Fake/simulate JavaScript execution:

- Forge JS proof of work payload (reverse engineer).

#BHASIA   @BlackHatEvents

## Slide 16

#### Bypass Techniques Used by Bots

Distribute attack using **proxies** : → Avoid IP-based rate limiting.

Distribute attack using **residential proxies** : → Avoid reputation-based blocking.

Distribute attack using **residential proxies located in same country as website targeted** : → Avoid geo-blocking.

#BHASIA   @BlackHatEvents

## Slide 17

###### Community Driven Anti-Detection Frameworks

Generic, for (headless) automated browsers:

#BHASIA   @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Community Driven Anti-Detection Frameworks
Generic, for (headless) automated browsers:
Watch 114 ~~ Fork 642
Fork 696 Star 4.7k
DevTools - arh.antoinevastel.com/bots/areyouheadless
https://arh.antoinevastel.com/bots/areyouheadless Elements
Hide data URLs
XHR JS CSS Img Media Font Doc WS Manifest Othe
You are not Chrome Ee
. Waterfall a
GET
headless
B bootstra.
B style.css
174K
```

## Slide 18

###### To Conduct Credential Stuffing Attacks

#BHASIA   @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
To Conduct Credential Stuffing Attacks
README.md
OPEN A
BULLET
OpenBullet 2 is a cross platform automation suite powered by .NET core. It allows to perform requests towards a
target webapp and offers a lot of tools to work with the results. This software can be used for scraping and
parsing data, automated pentesting and much more.
Link to the Official Forum where you can find guides and become part of the community behind OpenBullet.
Found a bug? Create an issue!
IMPORTANT! Performing (D)DoS attacks or credential stuffing on sites you do not own (or you do not have
permission to test) is illegal! The developer will not be held responsible for improper use of this software.
```

## Slide 19

#### Bad Bots in 2023: Summary

Distribute their attacks.

Leverage thousands of residential proxies.

Constantly change and forge their signatures/fingerprints. **Q: How to block these ever-evolving and distributed bots?**

#BHASIA   @BlackHatEvents

## Slide 20

# **Detecting and Blocking Distributed Attacks Manually**

#BHASIA   @BlackHatEvents

## Slide 21

#### Detect a Traffic Spike

#BHASIA   @BlackHatEvents

## Slide 22

#### Drill-Down on Different Features

User Agents
Headers

AS

Countries

#BHASIA   @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Drill-Down on Different Features
login-attack-fingerprint-HeadersList login-attack-fingerprint-UserAgent
Headers
Count
User Agents
@timestamp per minute @timestamp per minute
login-attack-fingerprint-AS login-attack-fingerprint-Countries
@ Bouygues Teleco
Adman LLC
PJSC MegaFon
@ 12 Mobile LLC
Countries
imestamp per minute @timestamp per minute
@ Spain
```

## Slide 23

#### Derive Rules

Find a rule.

= Country=Russia && User Agent Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36

### **How to automate the analysis?**

#BHASIA   @BlackHatEvents

## Slide 24

# **Detecting Distributed Attacks**

#BHASIA   @BlackHatEvents

## Slide 25

#### Detecting Distributed Attacks

●Compute **aggregate statistics on login:**

- ○Number of unique User Agents.

- ○Number of unique IPs.

○Number of sessions.

- ●Detect **anomalies** on the resulting **time-series using a z-score based anomaly detection algorithm.**

- **Push an event** describing the attack (customer, start time).

●Implemented in streaming (Apache Flink).

#BHASIA   @BlackHatEvents

## Slide 26

#### Detecting Distributed Attacks

attack start time

#BHASIA   @BlackHatEvents

## Slide 27

#### General Idea

#BHASIA   @BlackHatEvents


> Recovered by OCR — confidence 75/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
General idea
norma Suspicious
of 3
requests
time
```

## Slide 28

#### Next Step: Automate Rule Generation

Headers User Agents
AS Countries
attack start time

#BHASIA   @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Next Step: Automate Rule Generation
Headers User Agents
@timestamp per minke @timestamp per minute
AS Countries
attack start time
@timestamp per minute
@time:
mp per minute
```

## Slide 29

# **Introducing Sliceline**

#BHASIA   @BlackHatEvents

## Slide 30

#### What is Sliceline?

###### Algorithm to find **slices** of data where an ML model performs badly.

|country|UA|IP type|error|**Slice:**a|
|---|---|---|---|---|
|FR|Chrome|residential|0.1||
|FR|Firefox|data_center|0.2||
|DE|Chrome|data_center|0.9|country = DE|
|FR|Chrome|data_center|0.8|UA=Firefox
&& IP|
|CN|Firefox|residential|0.2|type=data_center|
|CN|Chrome|residential|0.1||

**Slice:** a conjunction of conditions.

_https://dl.acm.org/doi/10.1145/3448016.3457323_

#BHASIA   @BlackHatEvents

## Slide 31

#### Generating Rules Using Sliceline

||Use|Sliceline to tar|get groups of|data instead of bad-performing slices.|
|---|---|---|---|---|
|country|UA|IP type|group||
|FR|Chrome|residential|0||
|FR|Firefox|data_center|0|Group definitions:|
|DE|Chrome|data_center|1|●**Human traffic**=> group 0|
|FR|Chrome|data_center|1|●**Suspicious traffic**=> grou|
|CN|Firefox|residential|0||
|CN|Chrome|residential|0||

- **Suspicious traffic** => group 1

#BHASIA   @BlackHatEvents

## Slide 32

#### How does it really work?

- Searches for slices with large errors.

   - **→ Need a way to quickly compute slice errors.**

- Uses matrix algebra to evaluate slices.

   - **→ Can profit from optimized implementations of matrix multiplication.**

- Uses pruning to reduce the search space without accessing the data. **→ Reduces memory access for large datasets.**

#BHASIA   @BlackHatEvents

## Slide 33

#### Sliceline Internals: Encoding

|country|UA|IP type|error|
|---|---|---|---|
|FR|Chrome|residential|0.1|
|FR|Firefox|data_center|0.2|
|DE|Chrome|data_center|0.9|
|FR|Chrome|data_center|0.8|
|CN|Firefox|residential|0.2|
|CN|Chrome|residential|0.1|

1. One-hot encoding.

2. Express rules as binary vectors.

|country|country|country|UA|UA|IP type|IP type||
|---|---|---|---|---|---|---|---|
|=
FR|=
DE|=
CN|=
Chrome|=
Firefox|=
residential|=
data_center|error|
|1|0|0|1|0|1|0|0.1|
|1|0|0|0|1|0|1|0.2|
|0|1|0|1|0|0|1|0.9|
|1|0|0|1|0|1|1|0.8|
|0|0|1|0|1|1|0|0.2|
|0|0|1|1|0|1|0|0.1|
|0|1|0|0|0|0|0||
|0|0|0|1|0|0|1||

#BHASIA   @BlackHatEvents

## Slide 34

###### Sliceline Internals: Matching Rules With Matrix Multiplication

|country
=
FR|country
=
DE|country
=
CN|UA
=
Chrome|UA
=
Firefox|IP type
=
residential|IP type
=
data_center|error|0
0
0
0|
|---|---|---|---|---|---|---|---|---|
|1|0|0|1|0|1|0|0.1|1
0
0
0|
|1|0|0|0|1|0|1|0.2|0
0
1
1|
|0|1|0|1|0|0|1|0.9|0
1
X
0
1
R|
|1|0|0|1|0|1|1|0.8|0
0
0
0|
|0|0|1|0|1|1|0|0.2|0
0
0
0|
|0|0|1|1
F: featur|0
e matrix|1|0|0.1
c
E|ountry = DE
UA=Firefox
&&
IP type=data_center
0
1
F
xR|

F: feature matrix

#BHASIA   @BlackHatEvents

## Slide 35

#### Sliceline Internals: Slice Errors

L = FxR
error
E T  x L
0.1 0 0
total slice error 0.9 1.7
0.2 0 0
I T  x L
0.9 1 1
slice size
1 2
0.8 0 1
0.2 0 0
mean slice error 0.9 0.8.5
0.1 0 0
E country = DE UA=Firefox  &&
IP type=data_center
#BHASIA   @BlackHatEvents

## Slide 36

#### Open Source Package

Original algorithm implemented in R.

Implemented in Python:

- Rewrote some part of R implementation using **matrix multiplications** .

- Leverage **numpy optimizations** .

- Compatible with pandas.

**Speed up > x 1000**

Syntax-agnostic: can generate **rules for any rule-engine** .

#BHASIA   @BlackHatEvents

## Slide 37

#### Code Example

###### **Example Dataset:**

- Gathered from a French e-commerce website.

- Human traffic (group 0): requests with old session.

- Suspicious traffic (group 1): requests from non french speaking countries and datacenter IPs.

#BHASIA   @BlackHatEvents

## Slide 38

#### Code Example

Apply the algorithm with 2 lines of code!

Get rules in the format you want!

#BHASIA   @BlackHatEvents


> Recovered by OCR — confidence 84/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
sf = Slicefinder(
alpha = 0.80,
max l = df.shape[1],
min sup = 1,
verbose = True
)
sf.fit(df.drop("group", axis=1),
Get rules in the format
you want!
Code Example
Apply the algorithm with 2 lines of code!
df["group"])
for slice, stats in zip(sf.top slices , sf.top slices statistics ):
rule = None
for feat, value in zip(df.columns, slice):
if value is not None:
if rule is None:
rule = f" {feat} = {value} "
else:
rule += f" && ‘{feat} = {value} "
print(f"{rule} | slice size: {stats['slice size']}")
“Country = Germany’ | slice size: 4149.0
“User Agent’ = Chrome’ && “Country’=Germany” | slice size: 4133.0
“Country = Germany && “Accept Language = en-US,en;q=0.9° | slice size: 4097.0
“User Agent’ = Chrome’ && “Country’='Germany’ && “Accept Language = en-US,en;q=0.9°
| slice size: 4097.0
```

## Slide 39

###### Credential Stuffing Attack on Gaming Platform

Blocked more than  3M
requests  in a week.

#BHASIA   @BlackHatEvents

## Slide 40

###### Heavily Distributed Attack: > 187k IP Addresses

#BHASIA   @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 89/100 on the text kept, 67/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Asset registration
Collect identifiers: Information disclosure by vendor

[Browser] ← → C  🔒 csm.sierrawireless.com/WarrantyChecker.aspx
SIERRA WIRELESS
A SEMTECH COMPANY
Warranty Information
Check Single Device
[Any Serial or IMEI Number *]
Check Warranty
- or -
Check Multiple Devices from File ?
[Choose File] IMEIs.txt
Check Multiple Warranties

[Notepad: IMEIs.txt ...]
File  Edit  Format  View  Help
353968099238020
353968099238021
353968099238022
353968099238023
353968099238024
353968099238025
353968099238026
353968099238027
353968099238028
353968099238029
353968099238030
353968099238031
353968099238032
353968099238033
353968099238034
353968099238035
353968099238036
353968099238037
353968099238038
353968099238039
353968099238040
353968099238041
353968099238042
353968099238043
353968099238044
353968099238045
353968099238046
353968099238047
353968099238048
353968099238049
353968099238050
353968099238051
353968099238052
353968099238053

→ Collect →

[Results table]
Serial Number            | IMEI Number(s)
5912437068■■■ (redacted) | 358643075767520
358643075767521          |
358643075767522          |
358643075767523          |
…
358643075767537          |
[red box:] 5912437324■■■ (redacted) | 358643075767538
358643075767539          |
…
358643075767544          |
358643075767545          |
5912437310■■■ (redacted) | 358643075767546

→ Register →

[Register AirLink RV50x form]
Register AirLink RV50…
Type              AirLink RV50x ▾
[red box:] Serial Number   [        ]
[red box:] IMEI/ESN        [        ]
Name ⓘ                     [        ]
Activate Offer    [ON  ]
☐ Pre-configure system
[Register]  or Import a list
```

## Slide 41

#### Takeaways

Approach to **detect distributed attacks** using traffic aggregations and anomaly detection. We leverage Sliceline to **infer malicious signatures and to generate rules** .

Efficient against **bots that frequently adapt** and modify/forge their fingerprints.

Sliceline **can be applied to other security use cases** that rely on a rule engine.

#BHASIA   @BlackHatEvents

## Slide 42

#### Contact

**Antoine Vastel PhD,** Head of Research @DataDome, <u>antoine.vastel@datadome.co.</u>

**Konstantina Kontoudi PhD,** Lead Data Scientist @DataDome, <u>konstantina.kontoudi@datadome.co.</u>

#BHASIA   @BlackHatEvents
