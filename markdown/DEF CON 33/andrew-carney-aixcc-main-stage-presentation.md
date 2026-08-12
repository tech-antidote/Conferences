---
title: "AIxCC Main Stage Presentation"
speakers: ["Andrew Carney"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33/Andrew Carney - AIxCC Main Stage Presentation.pdf"
pages: 47
sha256: "8bdca2a5afb2cfdcc00920869627b8ec1e0019d218f6615d6200e80ec91f24b3"
text_chars: 9393
ocr_pages: 15
has_ocr: true
redacted_secrets: 0
ocr_confidence: 88.3
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:52:29Z"
---
# AIxCC Main Stage Presentation

**Speakers:** Andrew Carney  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33/Andrew Carney - AIxCC Main Stage Presentation.pdf` (47 pages)


## Slide 1

###### **Announcing the Winners of DARPA’s AI Cyber Challenge**

Andrew Carney


> Recovered by OCR — confidence 95/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
PATCHING
CRITICAL
INFRASTRUCTURE
Announcing the Winners of
DARPA’s AI Cyber Challenge
Andrew Carney
```

## Slide 2

**_Any sufficiently advanced technology is indistinguishable from magic._** - Arthur C. Clarke

## Slide 3


> Recovered by OCR — confidence 84/100 on the text kept, 61/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ALL MODERN DIGITAL
INFRASTRUCTURE
A PROTECT SOME
RANDOM PERSON
IN NEBRASKA HAS
BEEN THANKLESSLY
en | > MAINTAINING
” ‘ Unsophisticated Cyber Actor(s) Targeting Operational Technology
{ J Release Date: May
```

## Slide 4

Critical
infrastructure
vulnerabilities

**are incompatible with the future**


> Recovered by OCR — confidence 89/100 on the text kept, 66/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
= c
=> =
=
Critical
infrastructure
vulnerabilities
are incompatible
with the future
ALL MODERN DIGITAL
INFRASTRUCTURE
A PROJECT SOME
RANDOM PERSON
IN NEBRASKA HAS
BEEN THANKLESSLY
MAINTAINING
SINCE. 2003
```

## Slide 5

#### OUR CRITICAL INFRASTRUCTURE DEPENDS ON OPEN SOURCE SOFTWARE AND IS VULNERABLE

We cannot move forward if critical vulnerabilities can survive in our code for years

## Slide 6

## Slide 7

# WHAT IS AIxCC?

- ➔ A competition that rewards autonomous systems that find and patch vulnerabilities in source code.

- ➔ The challenges are well-known open-source projects.

- ➔ The vulnerabilities are realistic or real.

- ➔ Patching is worth more than finding.

- ➔ Code and data will be released open source.

## Slide 8

###### **Bug vs. vulnerability**

**_Sometimes, magic is just someone spending more time on something than anyone else might reasonably expect._**

- Teller (of Penn and Teller)

## Slide 9

###### **Bug vs. vulnerability**

**_Sometimes, [a vulnerability] is just someone spending more time on [a bug] than anyone else might reasonably expect._**

- Teller (of Penn and Teller)

## Slide 10


> Recovered by OCR — confidence 90/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Top 7
teams advance
Preliminary
events
AUGUST 2023 AUGUST 2024 AUGUST 2025
OPEN TRACK AND SEMIFINAL COMPETITION FINAL COMPETITION
Top 7 teams $2 million each Winners announced
SUBMISSIONS 2ND: $3 MILLION
3RD: $1.5 MILLION
THE
Google ANTHROP\C GOpenal BE Microsoft Lg LINUX OpenssF
```

## Slide 11


> Recovered by OCR — confidence 84/100 on the text kept, 58/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CYBER CHALLENGE
SEMIFINAL COMPETITION
OVERVIEW
COLLABORATORS & PARTNERS
To help secure our critical infrastructure, teams created custom
CRSs that competed in the AIxCC Semifinal Competition.
Lj - TEAMS S CHALLENGE
COMPETED PROJECTS
rt “I 3 — each with —
[3100 S 256cs ram
TO FINALS ——
COMPETITION
OPEN SOURCE SECURITY FOUNDATT
```

## Slide 12

NOTE: Teams in alphabetical order.


> Recovered by OCR — confidence 86/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
NOTE: Teams in alphabetical order.
c Java
Out-of-Bounds Server-Side
Team Name Read/Write Integer Overflow Use After Free Te Path Traversal OR, Deserialization Request Forgery
(Alphabetical) (CWE-125 / (CWE-190) (CWE-416) poche (CWE-22) paar (CWE-502) (SSRF)
42-b3yond-6ug
all_you_need_is_a
_fuzzing_brain
Lacrosse
Shellphish
Team Atlanta
Theori
Trail of Bits
& Not Found > Found & Patched
```

## Slide 13

###### **What counts for semifinals?**

- **Proof-Of-Vulnerability (POV)** ➔ Input data to reproduce vulnerability crash in harness

###### **PATCH**

- ➔ Unified diff source code fix for vulnerabilities

## Slide 14

###### **What counts for finals?**

###### **Proof-Of-Vulnerability (POV)**

###### **PATCH**

- ➔ Input data to reproduce vulnerability crash in harness

- ➔ Unified diff source code fix for vulnerabilities

###### **SARIF Assessment**

###### **BUNDLE**

- ➔ Structured reporting format ➔ Grouping of related PoV, for vulnerability details patch, and SARIF submissions

###### **DELTA SCAN**

- ➔ Challenge analyzing base code plus applied diff changes

###### **FULL SCAN**

- ➔ Challenge analyzing entire code base

## Slide 15

**All projects we adapted into challenges**


> Recovered by OCR — confidence 96/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
All projects we adapted into challenges
```

## Slide 16

**Semifinal Competition CRS performance by vulnerability class - synthetic only**


> Recovered by OCR — confidence 87/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Semifinal Competition CRS performance by vulnerability class - synthetic only
c Java
Out-of-Bounds Server-Side
Team Name Read/Write Integer Overflow Use After Free peciorawen Path Traversal aE Deserialization Request Forgery
(Alphabetical) (CWE-125 / (CWE-190) (CWE-416) (CWE-476) (CWE-22) (CWE: pi CWE-78) (CWE-502) (SSRF)
CWE-787) is (CWE-918)
42-b3yond-6ug
all_you_need_is_a
_fuzzing_brain
Lacrosse
Shellphish
Team Atlanta
Theori
Trail of Bits
& Not Found oo Found & Patched
```

## Slide 17

**Final Competition CRS performance by vulnerability class - synthetic only**


> Recovered by OCR — confidence 89/100 on the text kept, 53/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Final Competition CRS performance by vulnerability class - synthetic only
JAVA
i
3
(Alphabetical)
4b9bb5
9caa56
ee79d5
Team Name
a
c
=
LL
```

## Slide 18

###### **COMPETITION AGGREGATE RESULTS - SYNTHETIC VULNERABILITIES**

**Semifinal** ( 5 Repositories / 59 Challenges) Vulnerabilities discovered **37%** (22/59) Vulnerabilities patched **25%** (15/59) Avg. Time to patch **2** hours

**Final** (28 Repositories / 53 Challenges) Known Vulnerabilities discovered **77%** (54/70) Known Vulnerabilities patched **61%** (43/70) Avg. Time to patch **45** minutes

## Slide 19

**COMPETITION AGGREGATE RESULTS - REAL WORLD, NON-SYNTHETIC VULNERABILITIES**

Final
Semifinal
Found in C Found in C  Patched in C
1  6  (1 replay - SystemD)  0
Found in Java Found in Java  Patched in Java
0  12  11  (3 w/o PoV)
* More information pending disclosure completion

## Slide 20

###### **FINAL ROUND DATA POINTS**

### Total Known Vulnerabilities **70**

Vulnerabilities discovered **54 (77%)**

Vulnerabilities patched **43 (61%)**

Real World Vulns discovered Total spent (Compute + LLM) **18 $359k**

Average time to patch **45 min**

Total LLM queries **1.9M**

Total LOC analyzed LLM Spend **54M $82k**

## Slide 21

**COST PER TASK SUCCESS (PoV, Patch, SARIF, or a Bundle)** ~$152


> Recovered by OCR — confidence 95/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
COST PER TASK SUCCESS
(PoV, Patch, SARIF, or a Bundle)
~$152
```

## Slide 22


> Recovered by OCR — confidence 86/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
DEFCON
—INNOVATORS—
A Leidos Company
OSTIF SPA
CELEBRATING 10 YEARS!
RHAPSODE
CONSULTING
Dazzle Cat Duo
CROMULENCE
LINCOLN LABORATORY
lz MASSACHUSETTS INSTITUTE OF TECHNOLOGY 2 Mayhem
ANTHROP\C
Google
mE Microsoft
S OpenAl
```

## Slide 23

**Jim O’Neill Stephen Winchell** HHS Deputy Secretary DARPA Director

## Slide 24

**Repo Viewer**


> Recovered by OCR — confidence 79/100 on the text kept, 58/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Repo Viewer
© Final Round
1035 223
AIxCC REPO
1,026 m= 221
5 little-cms ©
247 530
1,909
```

## Slide 25

###### **Another tablet visualization teaser**

Will do after some design updates and data finalization

## Slide 26

###### **What’s Next @ DEF CON**

##### **AIxCC EXPERIENCE**

- ➔ talk to teams

- ➔ view competition data / artifacts

- ➔ talk with collaborators

- ➔ talk with critical infra folks

- ➔ talk with related gov. project owners

## Slide 27

###### **What’s Next**

###### **MAINTAINTERS  (OSSF / OSTIF)**

## archive.aicyberchallenge.com

contact us to collaborate at aixcc@darpa.mil

###### **STORE**

darpa-exchange-organization.square.site

###### **Release Timeline**

- ➔ **NOW** : Shellphish, Team Atlanta, Theori, Trail of Bits (Competitor CRSs)

- ➔ **NOW** : Automated Harness Generation - SHERPA (github.com/AIxCyberChallenge/sherpa)

###### **POSTERS**

aicyberchallenge.com/education/

- ➔ **Aug 10** : All You Need IS A Fuzzing Brain (Competitor CRS)

- ➔ **Aug 24** : 42-b3yond-6ug, Lacrosse (Competitor CRSs)

- ➔ **Oct** : Competition Infrastructure, Challenge Repositories, Data, and Telemetry (pending disclosure to maintainers)

###### **DARPA / ARPA-H - Join Us!**

https://www.darpa.mil/work-with-us

https://arpa-h.gov/

## Slide 28


> Recovered by OCR — confidence 96/100 on the text kept, 58/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CYBER CHALLENGE
COMPETITOR HIGHLIGHTS
```

## Slide 29

###### 42-b3yond-6ug

###### “Czar of the SARIF” **Most correct SARIF assessments**

“Giant Slayer” **Scored on a**

###### **repo >5M LOC**

**Top 3 LLMs used:**

- ➔ GPT-4.1 ➔ Claude Opus 4 ➔ Claude Sonnet 4

## Slide 30

###### ALL YOU NEED IS A FUZZING BRAIN

“-Ofast”

###### **First Blood: C real world vuln**

“Faster Than Pizza Delivery” **Score < 5 min into a task**

**Top 3 LLMs used:**

➔ GPT-4o

- ➔ Claude 3.7 Sonnet

➔ Claude Opus 4

## Slide 31

###### Lacrosse

“Professional Assassin” **PoV success >95%**

- “Raiders of the Lost PoV”

**Discovered a real world vuln**

**Top 3 LLMs used:**

- ➔ GPT-4.1 ➔ GPT-4.1 mini

➔ GPT-4o mini

## Slide 32

###### Shellphish

###### “Best Telemetry” **Reporting LLM and CRS activity**

###### “The Doctor is In” **Passing patch rate > 95%**

**Top 3 LLMs used:**

- ➔ Claude Sonnet 4 ➔ o4-mini

- ➔ Claude 3.7 Sonnet

## Slide 33

###### Team Atlanta

###### “The Disruptor” **Most real world vulns discovered**

###### “Bundle Baron” **Most scoring bundles**

**Top 3 LLMs used:**

➔ o4-mini ➔ GPT-4o

- ➔ o3

## Slide 34

###### Theori

“Thrifty”

**Least $$ spent per vuln patched**

“Extra Caffeinated” **Most Java real world vulns discovered**

###### **Top 3 LLMs used:**

- ➔ o3 ➔ Claude Sonnet 4

- ➔ o4-mini

## Slide 35

###### Trail of Bits

“LOC Ness Monster”

**Scored w/ patch diff > 300 LOC**

“Cornucopia”

###### **Scored on 20 unique CWEs**

###### **Top 3 LLMs used:**

- ➔ Claude Sonnet 4 ➔ GPT-4.1 mini ➔ GPT-4.1

## Slide 36

## Slide 37

➔ **$1,500,000**

## Slide 38

➔ **$1,500,000**

## Slide 39

## Slide 40

➔ **$3,000,000**

## Slide 41

➔ **$3,000,000**

## Slide 42

## Slide 43

➔ **$4,000,000**


> Recovered by OCR — confidence 87/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
AIxCC = $4,000,000 = + ARPAQ
```

## Slide 44

➔ **$4,000,000**


> Recovered by OCR — confidence 82/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Atlanta
AIxCC = $4,000,000 ARPA) + ARPA®
```

## Slide 45

###### **Scoreboard breakdown**

|||%|_Vulnerability_|_Program_|_SARIF_||
|---|---|---|---|---|---|---|
||**_Team_**|Correct|_Discovery_|_Repaid_|_Assessment_|_Bundle_|
||**_Total_**|Submission|_Score_|_Score_|_Score_|_Score_|
|**_Team_**|**_Score_**|(r)|_(VDS)_|_(PRS)_|_(SAS)_|_(BDL)_|
|**Team Atlanta (9caa56)**|**392.76**|91.27%|79.71|171.10|5.99|136.38|
|**Trail of Bits (309958)**|**219.35**|89.33%|52.49|101.21|1.00|65.29|
|**Theori (3fad2e)**|**210.68**|44.44%|58.12|110.34|4.97|53.57|
|**All You Need IS A Fuzzing Brain**|||||||
|**(1b9bb5)**|**153.70**|53.77%|54.81|77.60|6.52|28.28|
|**Shellphish (463287)**|**135.89**|94.83%|47.94|54.31|8.47|25.29|
|**42-b3yond-6ug (ee79d5)**|**105.03**|89.23%|70.37|14.22|9.80|10.97|
|**Lacrosse (e87a4d)**|**9.59**|42.86%|1.68|5.43|0.00|3.62|

## Slide 46

**The world changes today. Automated patch development is:** Fast Scalable Cost-effective Available / Open-source **AI + CRS = The Future**

## Slide 47
