---
title: "Protecting Small Organizations in the Era of AI Bots"
speakers: ["Rama Hoetzlein"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Rama Hoetzlein_Protecting Small Organizations in the Era of AI Bots.pdf"
pages: 72
sha256: "5e1fe04879a113f12908f1472b803fd9c89ce4af6fa2243ba8430c447970206b"
text_chars: 18426
ocr_pages: 9
has_ocr: true
redacted_secrets: 0
ocr_confidence: 86.4
ocr_unreliable_blocks: 0
vision_verified_blocks: 1
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:20:28Z"
---
# Protecting Small Organizations in the Era of AI Bots

**Speakers:** Rama Hoetzlein  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Rama Hoetzlein_Protecting Small Organizations in the Era of AI Bots.pdf` (72 pages)


## Slide 1

# Protecting Small Organizations in the Era of AI Bots

Rama Carl Hoetzlein

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 59/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
‘black hat
FINGS
AUGUST 6-7, 2025
MANDALAY BAY / LAS VEGAS
Protecting Small Organizations
in the Era of Al Bots
Rama Carl Hoetzlein
```

## Slide 2

“51% of Internet traffic is non-human, with 37% of Internet traffic from bad bots”

2025 Imperva, Bad Bot Report

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 3

“51% of Internet traffic is non-human, with 37% of Internet traffic from bad bots”

2025 Imperva, Bad Bot Report

“87% of the malicious bot IPs [in our study] were not listed in popular IP blocklists.”

2021 Xigao Li et al., Good Bot, Bad Bot

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 4

### Client

The Community Science Institute is a public, non-profit that promotes scientific literacy, volunteer water quality monitoring and certified lab analysis for central New York.

**RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS** #BHUSA @BlackHatEvents

## Slide 5

### Client

CSI Database: Curated, certified, water quality data for Stream & Lake chemistry, Harmful Algae Blooms and Biomonitoring

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 6

### Client

We observed that a single server received over 150,000 page hits over 20 days, corresponding to **7,500 hits / day.**

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 7

### Client

We observed that a single server received over 150,000 page hits over 20 days, corresponding to **7,500 hits / day.**

Traffic was so severe that it was degrading server performance for CSI’s known human users and clients.

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 8

### Early Investigation

#### IP B-class aggregation and org lookup

Visitor traffic is from the entire world, despite the fact that the CSI Database is entirely data for central New York State

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 9

### Background

### What existing tools are available?

1. Throttling is ineffective – modern crawlers _observe_ rate limits. 2. Public blocklists are ineffective – up to 87% not listed

3. GREP is ineffective – difficult to interpret, good for spot checks

4. GoAccess, AWStats – summary statistics hide details

5. OSSEC, CrowdSec – real-time monitoring, do not examine historic/log access patterns

6. AI/ML Detection (Meyer 2008) – requires non-attack baseline

7. Rank Analysis (Zang 2008) – requires good pre-filtering

8. Large Organizations (Yen 2013) – we focus on small organizations

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 10

### Recent Approaches & Limitations

AI/ML Detection (Meyer 2008) – requires non-attack baseline Rank Analysis (Zang 2008) – requires good pre-filtering Large Organizations (Yen 2013) – we focus on small organizations

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 11

#### GoAccess log analysis

Statistical tools just tell us – yes – you have a lot of traffic, and it varies by day.

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 12

### Methods

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 13

### Question:

How can we distinguish human access patterns from machines?

we are a knowledge systems, AI and data visualization startup

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 14

**RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS** #BHUSA @BlackHatEvents

## Slide 15

**RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS** #BHUSA @BlackHatEvents

## Slide 16

### Does it _sound_ mechanical?

**RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

#BHUSA @BlackHatEvents

## Slide 17

### Investigation

Time

Host IP

_From:_ Jungkee Kim, Web Server Log Visualization, Intl. Journal of Advance Smart Convergence, 2018

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 18

### Investigation

Time

Host IP

_From:_ Jungkee Kim, Web Server Log Visualization, Intl. Journal of Advance Smart Convergence, 2018

Time (Days)

Benefits of Visualization:

- Entire log in one snapshot

- Everything is there, no statistical summary

• Easy for humans to see patterns

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 19

Time (Days)

**RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

#BHUSA @BlackHatEvents

## Slide 20

Time (Days)

What do you think is human here? **RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

#BHUSA @BlackHatEvents

## Slide 21

Time (Days)

Probably not human **RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

#BHUSA @BlackHatEvents

## Slide 22

### Methods

We are interested in distinguishing mechanical access patterns regardless of whether they are benign or malicious.

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 23

### Methods

Throttling: How fast are you? Block based on frequency of visit. e.g. no more than 20 pages/minute

We found that most traffic was observing rate limits.

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 24

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

##### Throttle limited IPs Reduced traffic by only 33%

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

## Slide 25

### Methods

### What are other patterns that humans would follow?

1. Throttling

- How fast are you?

_Human_ <20 page/min

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 26

### Methods

### What are other patterns that humans would follow?

_Human_

1. Throttling - How fast are you?

2. Consecutive - How often do you visit?

- <20 page/min <5 days consec.

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 27

### Methods

### What are other patterns that humans would follow?

_Human_

1. Throttling - How fast are you?

2. Consecutive - How often do you visit?

3. Daily Range  - How long can you work?

<20 page/min <5 days consec. <6 hours/day

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 28

### Methods

### What are other patterns that humans would follow?

_Human_

<20 page/min <5 days consec. <6 hours/day

1. Throttling - How fast are you?

2. Consecutive - How often do you visit?

3. Daily Range  - How long can you work?

4. Daily Hits      - How much do you look at?            <100 hits/day

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 29

### Methods

### What are other patterns that humans would follow?

_Human_

<20 page/min <5 days consec. <6 hours/day

1. Throttling - How fast are you?

2. Consecutive - How often do you visit?

3. Daily Range  - How long can you work? 4. Daily Hits      - How much do you look at?            <100 hits/day

Behavioral Science in Human-Computer Interaction

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 30

### Methods

**LOGRIP** Let’s use Human Behavioral Metrics to develop a…

Scoring Algorithm:

1. IP Hashing - key-value map of IPs from raw pages

2. Sort page hits by day & time

3. Apply behavioral metrics

4. Score based on a weighted contribution of metrics

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 31

### Intermediate Results

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 32

#### **Original Traffic**

**RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS** #BHUSA @BlackHatEvents

## Slide 33

**RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

#BHUSA @BlackHatEvents

#### **Blocked by Consecutive Days /w Daily Range**

## Slide 34

**Blocked by Daily Range with Freq RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 39/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
bite hat
ee
-
. Joe
. 4
|
Blocked by Daily Range with Freq
#BHUSA
@BlackHatEvents
```

## Slide 35

**RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

#BHUSA @BlackHatEvents

#### **Blocked by Daily Maximum**

## Slide 36

#### **Cumulative Filtered Results**

**RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS** #BHUSA @BlackHatEvents

## Slide 37

#### **Original Traffic**

**RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS** #BHUSA @BlackHatEvents

## Slide 38

#### **Cumulative Filtered Results**

**RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS** #BHUSA @BlackHatEvents

## Slide 39

**Cumulative Filtered Results**

**RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS** #BHUSA @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 38/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Cumulative Filtered Results
```

## Slide 40

**RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS** #BHUSA @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 44/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
oe
—
= .
° .
ele
=p
#BHUSA @BlackHatEvents
```

## Slide 41

**RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS** #BHUSA @BlackHatEvents

## Slide 42

Single IP

### Multiple IPs

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 43

**RAMA CARL HOETZLEIN**

Group of machines within the same Class C subnet requesting multiple pages around the same time.

|**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**|
|---|

#BHUSA @BlackHatEvents

## Slide 44

### Subnet Hashing

Aggregate all page hits across a subnet and _then_ perform scoring metrics.

IP

..
40.77.167.5
40.77.167.4
40.77.167.3
40.77.167.2
40.77.167.1
40.77.167.0
40.77.166.255
40.77.166.254
..

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 45

### Subnet Hashing

Aggregate all page hits across a subnet
and  then  perform scoring metrics.
..
40.77.167.5
40.77.167.4
40.77.167.3
IP 40.77.167.2
40.77.167.1
40.77.167.0
40.77.166.255
40.77.166.254
score
..

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 46

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

Hierarchical IP Hashing with Metric Scoring

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

## Slide 47

### Final Results

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 48

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS** #BHUSA @BlackHatEvents

**RAMA CARL HOETZLEIN**

**Filtered Result – Prior to Subnet Hashing**

## Slide 49

**RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

#BHUSA @BlackHatEvents

#### **Blocking Class C Subnets**


> Recovered by OCR — confidence 91/100 on the text kept, 44/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
:
Blocking Class C Subnets
```

## Slide 50

**RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

#BHUSA @BlackHatEvents

#### **Blocking Class B Subnets**

## Slide 51

#BHUSA @BlackHatEvents

#### **Final Result**

**RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**


> Recovered by OCR — confidence 80/100 on the text kept, 42/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
black hat
:
Be
!
-
ee
2
as .
te
. -
=
Final Result
:
#BHUSA @BlackHatEvents
```

## Slide 52

**Original Traffic Final Result**

**RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 30/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BRIEFINGS Bes.
'
Original Traffic Final Result
```

## Slide 53

Estimated Load Analysis

Original C Filtering B Filtering Final Server Load

**RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

#BHUSA @BlackHatEvents

## Slide 54

### Results

## 94% reduction in traffic

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 55

### Results

## 94% reduction in traffic

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 56

**Original Traffic Final Result**

**RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 30/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BRIEFINGS Bes.
'
Original Traffic Final Result
```

## Slide 57

### Protecting Small Organizations

We found that - even when well behaved and observing rate limits - the sheer volume of AI bot requests can overwhelm the servers of small organizations.

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 58

### Protecting Small Organizations

Policy

“Our water quality data is available to the public for free. We prefer to have a human-in-theloop, and discourage AI crawlers so that our servers remain responsive to our human users.”

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 59

### Protecting Small Organizations

Grants for non-profits and small orgs often depend on viewership statistics for new or renewed funding.

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 60

### Protecting Small Organizations

Grants for non-profits and small orgs often depend on viewership statistics for new or renewed funding.

**LOGRIP** provides an upper bound on real human views, with blocked/permitted stats per day, at least better than raw traffic stats.

Date All Blocked Allowed Reduction 7/16/2025 11359 10807 552 95.1% 7/17/2025 13476 12965 512 96.2%

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 61

### Conclusions

• Understand the extent of AI crawler & bot activity • Defend small organizations (single machines) from large organizations (many machines in data centers)!

• Be able to specify defense policy

• Know (to the extent possible) the implications of those policies

- Do all of this easily, cheaply and open source

### **LOGRIP**

A simple, lightweight, open source tool for generating blocklists _and_ policy visualizations based on access logs.

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 62

### New Tool

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 63

### Running LOGRIP

Features:

<u>https://github.com/quantasci/logrip</u>

• Open source

• Cmd line based

**Input:** access log config file (log format, policy)

• Read any log format

**Output:** blocklist B-subnet list C-subnet list full IP list policy visualizations load estimation

**RAMA CARL HOETZLEIN**

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

• Config policy settings

• Fast. 150k log in 10 sec

#BHUSA @BlackHatEvents

## Slide 64

LOGRIP
All Output Products

**RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

#BHUSA @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 72/100 on the text kept, 55/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
black hat
BRIEFINGS

[Panel 1 - top left] Observed Traffic
[Panel 2 - top middle] Blocking Actions (Policy)
[Panel 3 - top right] Estimated Server Load (Before & After)
[Panel 4 - bottom left] Filtered Traffic
LOGRIP
All Output Products

[Panel 5 - bottom middle left] Metrics by IP
IP | ip_cnt | page_c | uniq_c | uniq_r | elapse | max_c | num_r | min_hi | min_h | ... | (page)
3.136.111.218   1     1     1     1     0     1   0     1      0                              /owa/auth/logon.aspx
4.151.218.216   1     1     1     1     0     1   0     1      0     0     1     0        0   /owa/auth/logon.aspx
4.227.36.31     1   422   414  0.98  0.06     1   0   422  1.168 4.658   422 1.168    4.658   /bmi/monitoringlocations/629
4.227.36.50     1    41    41     1     0     1   0    41  0.026 20.51    41 0.026    20.51   /queries/?page=5&q[s]=date%2
4.227.36.122    1     6     6     1     0     1   0     6  0.003    25     6 0.003       25   /queries/new?q%5Bs%5D=date
5.102.173.71    1    12    12     1  0.93     2   0     1   12.9 0.009    11  12.9    0.009   /events/3085
5.181.190.248   1    11     1  0.09  0.99     2   0     1  14.89 0.008    10 14.89    0.008   /
8.48.71.250     1     1     1     1     0     1   0     1      0     0     1     0        0   /monitoringsets/7
8.211.42.174    1     1     1     1     0     1   0     1      0     0     1     0        0   /dns-query?dns=pHkBAAABAAA
17.241.75.55    1     1     1     1     0     1   0     1      0     0     1     0        0   /events/842
17.241.75.92    1     1     1     1     0     1   0     1      0     0     1     0        0   /sites/117
17.241.75.106   1     1     1     1     0     1   0     1      0     0     1     0        0   /events/499
17.241.75.110   1     1     1     1     0     1   0     1      0     0     1     0        0   /events/344
17.241.75.127   1     1     1     1     0     1   0     1      0     0     1     0        0   /events/1519
17.241.219.9    1     1     1     1     0     1   0     1      0     0     1     0        0   /events/1989
17.241.219.12   1     1     1     1     0     1   0     1      0     0     1     0        0   /hab_events/701
17.241.219.24   1     1     1     1     0     1   0     1      0     0     1     0        0   /events/120
17.241.219.44   1     1     1     1     0     1   0     1      0     0     1     0        0   /monitoringlocations/382
17.241.219.52   1     1     1     1     0     1   0     1      0     0     1     0        0   /hab_events/688
17.241.219.114  1     1     1     1     0     1   0     1      0     0     1     0        0   /hab_events/655
17.241.219.149  1     1     1     1     0     1   0     1      0     0     1     0        0   /monitoringlocations/512
17.241.219.172  1     1     1     1     0     1   0     1      0     0     1     0        0   /monitoringlocations/685
17.241.219.182  1     1     1     1     0     1   0     1      0     0     1     0        0   /hab_events/169
17.241.227.19   1     1     1     1     0     1   0     1      0     0     1     0        0   /events/1662
17.241.227.65   1     1     1     1     0     1   0     1      0     0     1     0        0   /events/3107
17.241.227.124  1     1     1     1     0     1   0     1      0     0     1     0        0   /hab_events/667
17.241.227.154  1     1     1     1     0     1   0     1      0     0     1     0        0   /monitoringlocations/562
17.241.227.167  1     1     1     1     0     1   0     1      0     0     1     0        0   /events/2872
17.241.227.238  1     1     1     1     0     1   0     1      0     0     1     0        0   /events/2572
18.97.9.169     1   175   175     1  0.12     1   0   175  2.738 1.024   175 2.738    1.024   /hab_events/92
20.49.136.28    1     1     1     1     0     1   0     1      0     0     1     0        0   /monitoringsets/7
20.159.64.138   1     4     3  0.75     0     1   0     4  3E-04 5.294     4 3E-04    5.294   /hab
23.146.184.101  1     1     1     1     0     1   0     1      0     0     1     0        0   /
24.59.56.143    1     1     1     1     0     1   0     1      0     0     1     0        0   /monitoringlocations/504
27.150.86.197   1     2     2     1     0     1   0     2      0     0     2     0        0   /queries/new?q%5Bs%5D=ana
31.13.224.222   1     2     1   0.5     0     1   0     2      0     0     2     0        0   /.env

[Panel 6 - bottom middle right] Metrics by B-Subnet
IP | ip_cnt | page_cnt | uniq_cnt | uniq_ratio | elapsed(d | max_cons | num_r... | ... | pm
3.136.*.*      1     1     1     1     0   1   0                                        0
4.151.*.*      1     1     1     1     0   1   0                                        0
4.227.*.*      3   469   461  0.98  0.37   2                                          )38
5.102.*.*      1    12    12     1  0.93   2   0    1 12.90278 0.009064   11 12.90278 0.009064
5.181.*.*      1    11     1  0.09  0.99   2   0    1 14.89167 0.007656   10 14.89167 0.007656
8.48.*.*       1     1     1     1     0   1   0    1        0        0    1        0        0
8.211.*.*      1     1     1     1     0   1   0    1        0        0    1        0        0
17.241.*.*    20    20    20     1  1.11   2   0    8 1.360278 0.007781   12 8.150278 0.048832
18.97.*.*      1   175   175     1  0.12   1   0  175 2.738333 1.024232  175 2.738333 1.024232
20.49.*.*      1     1     1     1     0   1   0    1        0        0    1        0        0
20.159.*.*     1     4     3  0.75     0   1   0    4 0.000278 5.294118    4 0.000278 5.294118
23.146.*.*     1     1     1     1     0   1   0    1        0        0    1        0        0
24.59.*.*      1     1     1     1     0   1   0    1        0        0    1        0        0
27.150.*.*     1     2     2     1     0   1   0    2        0        0    2        0        0
31.13.*.*      1     2     1   0.5     0   1   0    2        0        0    2        0        0
34.77.*.*      1     1     1     1     0   1   0    1        0        0    1        0        0
34.79.*.*      1     1     1     1     0   1   0    1        0        0    1        0        0
35.159.*.*     1     5     3   0.6     0   1   0    5 0.017222 2.033899    5 0.017222 2.033899
40.77.*.*     38   103    98  0.95  1.09   2   0   17 1.503055 0.061053   86 21.63861 0.108389
42.58.*.*      1     2     2     1     0   1   0    2        0        0    2        0        0
42.179.*.*     1     2     2     1     0   1   0    2        0        0    2        0        0
44.220.*.*     1     1     1     1     0   1   0    1        0        0    1        0        0
45.20.*.*      1     1     1     1     0   1   0    1        0        0    1        0        0
45.55.*.*      1     8     8     1     0   1   0    8        0        0    8        0      inf
45.66.*.*      1     1     1     1     0   1   0    1        0        0    1        0        0
45.79.*.*      1     1     1     1     0   1   0    1        0        0    1        0        0
45.89.*.*    132   197   166  0.84   0.7   1   0  197 16.17667 0.193874  197 16.17667 0.193874
45.93.*.*    140   210   172  0.82   0.7   1   0  210 15.61083 0.208102  210 15.61083 0.208102
45.156.*.*     5     5     2   0.4  0.44   1   0    5 4.940833  0.00638    5 4.940833  0.00638
45.200.*.*     1     1     1     1     0   1   0    1        0        0    1        0        0
46.19.*.*      1     2     1   0.5  0.53   1   0    2        0        0    2        0        0
46.250.*.*     1     1     1     1     0   1   0    1        0        0    1        0        0
47.79.*.*      2     2     2     1  0.51   1   0    2        0        0    2        0        0
47.82.*.*      2     3     3     1     0   1   0    3 0.000278 1.578948    3 0.000278 1.578948
47.128.*.*     8     8     8     1   0.1   1   0    8 1.209722 0.048382    8 1.209722 0.048382
47.134.*.*     1     1     1     1     0   1   0    1        0        0    1        0        0
47.245.*.*     1     1     1     1     0   1   0    1        0        0    1        0        0
48.217.*.*     2     2     2     1  0.91   1   0    2        0        0    2        0        0
49.51.*.*      2     2     1   0.5  0.43   1   0    2        0        0    2        0        0
51.81.*.*      1     1     1     1     0   1   0    1        0        0    1        0        0
51.178.*.*     1     1     1     1     0   1   0    1        0        0    1        0        0
51.222.*.*     6     7     7     1  0.16   1   0    7 1.903056 0.026651    7 1.903056 0.026651
52.4.*.*       1     1     1     1     0   1   0    1        0        0    1        0        0

[Panel 7 - right] Page Hits by IP
57.141.7.14   1
57.141.7.15   3
                1  /bmi/monitoringregions/4
                1  /events/2731
57.141.7.16   2
                1  /
57.141.7.17   7
                1  /
                1  /bmi_events/62
                1  /events/2424
                1  /events/835
                1  /groundwater_queries?page=320
                1  /groundwater_queries?page=432
57.141.7.18   5
                1  /
                1  /bmi_events/152
                1  /events/2286
                1  /queries/new?q%5Bs%5D=date+asc
57.141.7.19   8
                1  /bmi_events/167
                1  /events/1100
                1  /events/2332
                1  /events/2863
                1  /queries/new?q%5Bs%5D=analyte_name+desc
                1  /queries/new?q%5Bs%5D=event_flow+asc
                1  /queries?page=97&q%5Bs%5D=event_flow+asc
57.141.7.20   9
                1  /events/1778
                1  /events/1912
                1  /groundwater_queries?page=322
                1  /monitoringlocations/530
                1  /monitoringlocations/8
                1  /monitoringsets/25
                1  /queries?page=997&q%5Bs%5D=event_flow+asc
                1  /sites/158
57.141.7.21   6
                1  /events/259
                1  /events/2747
                1  /queries/new?q%5Bs%5D=monitoringlocation_name+asc
                1  /queries?page=6&q%5Bs%5D=event_flow+asc
                1  /sitemap
57.141.7.22  10
                1  /bmi/monitoringlocations/382
                1  /events/1301
                1  /events/2218
                1  /events/2260
                1  /events/2467
                1  /events/37
                1  /monitoringlocations/684
                1  /queries/new?q%5Bs%5D=analyte_name+asc
                1  /queries/new?q%5Bs%5D=event_flow+asc

RAMA CARL HOETZLEIN            PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS            #BHUSA  @BlackHatEvents
```

## Slide 65

#### **Filtered Result**

### Limitations

Cannot stop DDoS attacks

- acquire random IPs

Many AI crawlers still present

- well disguised, more random

randomized, infrequent

At this point - Human vs. Machine becomes harder to distinguish

DDoS

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 66

### Future Goals

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 67

### Future Goals

## • Now in use. Measure post-blocking activity with client.

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 68

### Future Goals

• Now in use. Measure post-blocking activity with client.

- Ground truth data for human and non-human activity (both are difficult to replicate!)

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 69

### Future Goals

• Now in use. Measure post-blocking activity with client.

• Ground truth data for human and non-human activity (both are difficult to replicate!)

• Study policy parameter sensitivity and/or optimize

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 70

<u>https://github.com/quantasci</u> we are a knowledge systems, AI and data visualization startup

### LOGRIP

<u>https://github.com/quantasci/logrip</u> Open source, Apache 2.0 license

arXiv

<u>https://arxiv.org/abs/2508.03130</u>

<u>https://ramakarl.com/</u>

rama karl hoetzlein

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 71

### Thank you!

#### Rama Karl Hoetzlein

**PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS**

**RAMA CARL HOETZLEIN**

#BHUSA @BlackHatEvents

## Slide 72

**RAMA CARL HOETZLEIN PROTECTING SMALL ORGANIZATIONS IN THE ERA OF AI BOTS** #BHUSA @BlackHatEvents
