---
title: "The Fault in Our Metrics Rethinking How We Measure Detection & Response"
speakers: ["Allyn Stott"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2024"
edition: "ASIA"
year: 2024
source_pdf: "BlackHat ASIA 2024-Slides/Allyn Stott-The Fault in Our Metrics Rethinking How We Measure Detection & Response.pdf"
pages: 40
sha256: "eb0fdd6676ed1d7e11749463e0a79b0cc652aab0c20085893a61aba9f44d8570"
text_chars: 7728
ocr_pages: 0
has_ocr: false
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2"
converted_at: "2026-08-12T00:48:27Z"
---
# The Fault in Our Metrics Rethinking How We Measure Detection & Response

**Speakers:** Allyn Stott  
**Conference:** Black Hat ASIA 2024  
**Source:** `BlackHat ASIA 2024-Slides/Allyn Stott-The Fault in Our Metrics Rethinking How We Measure Detection & Response.pdf` (40 pages)

## Slide 1

# The Fault in Our Metrics Rethinking How We Measure Detection & Response

## Slide 2

Bossman

BoD meeting is coming up. Gonna need updated program metrics. Let's chat tomorrow

you got it boss

## Slide 3

###### Team Chat

BoD metrics... what have we presented in the past?

#### oh no

bad news, our last manager pretty much just made those up

good news, you’re here and gonna do so much better ;-)

## Slide 4

detection response metrics

## Slide 5

"Metrics: You Are What You Measure!" ~Hauser & Katz "That which is measured, improves" ~Karl Pearson Why should I care about metrics?

"That which is measured, improves" ~Karl Pearson

"Metrics reveal data." ~Edward Tufte

"Metrics are an annoying powerpoint I need to update every month." ~Allyn

## Slide 6

### Hi I’m Allyn I've made mistakes.

## Slide 7

5 Terrible Mistakes I’ve Made When Creating Metrics

## Slide 8

## Losing Sight of the Goal

##### Mistake #1

## Slide 9

#### Security Alerts

Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec Jan Feb Mar

for illustrative purposes only

## Slide 10

#### Security Alerts

TP FP

Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec Jan Feb Mar

for illustrative purposes only

## Slide 11

#### What do I measure?

S treamlined

A wareness

V igilance E xploration

R eadiness

## Slide 12

#### SAVER Categories

###### **S** treamlined

**A** wareness

**V** igilance

**E** xploration

**R** eadiness

Operational Context and intelligence Visibility and detection Proactive hunts Preparation efficiency about existing and coverage for and investigations for the next accuracy, emerging threats, known threats. into the unknown. big incident. and automation. vulnerabilities, and risks.

## Slide 13

#### Security Alerts

TP FP

Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec Jan Feb Mar

for illustrative purposes only

## Slide 14

###### **Outcome**

###### There's always time and effort for TPs **Question** Are we spending time investigating impactful alerts? **Category** Streamlined

###### Security Alerts

TP FP

###### Jan Mar May Jul Sep Nov Jan Mar

###### **Metric control**

Alert tuning **Risk reward**

Over-tuning alerts, prioritizing based on volume **Data requirements** Alert resolution

###### **Effort cost** Medium **Metric cost** Low

**Metric expiration** Automation and enforced detection quality

for illustrative purposes only

## Slide 15

#### Time spent on FPs

Auto
     Manual
Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec Jan Feb Mar

for illustrative purposes only

## Slide 16

## Using Quantities That Lack Controls

##### Mistake #2

## Slide 17

#### Mean Time to Recover

Sep Oct Nov Dec Jan Feb Mar

for illustrative purposes only

## Slide 18

**Outcome** Incidents are resolved quickly and effectively **Question** How long does it take to recover from incidents? **Category** Readiness

###### Mean Time to Recover

Sep Oct Nov Dec Jan Feb Mar

**Metric control** Playbooks and preventions **Risk reward**

Speed ≠ Accuracy or effectiveness **Data requirements** Timestamps for each incident phase **Effort cost**

Dependent on complexity of incidents **Metric cost** Low

**Metric expiration**

Prevention cost ≤ Response cost

for illustrative purposes only

## Slide 19

#### Response Readiness Metrics

Triage & Analysis Incident Spin Up Time Contain (filtered) (filtered) (filtered)

Sep Oct Nov Dec Jan Feb Mar Sep Oct Nov Dec Jan Feb Mar Sep Oct Nov Dec Jan Feb Mar

Remediate Recover (filtered) (filtered)

for illustrative purposes only

Sep Oct Nov Dec Jan Feb Mar Sep Oct Nov Dec Jan Feb Mar

## Slide 20

## Thinking Proxy Metrics Are Bad

##### Mistake #3

## Slide 21

#### MITRE ATT&CK Coverage

Recon
Initial Access
Execution
Persistence
PrivEsc
Defense Evasion
Cred Access
Discovery
Lateral Movement
Collection
C2
Exfiltration
Impact
0% 20% 40% 60% 80% 100%
for illustrative purposes only

## Slide 22

###### **Outcome** Detection coverage for known threat techniques **Question**

###### MITRE ATT&CK Coverage

Recon
Persistence
Cred Access
Collection
Impact
0% 20% 40% 60% 80% 100%

Where do we have gaps in our detections? **Category** Vigilance **Metric control**

Building and buying new detections **Risk reward**

Low quality detections or tests to quickly get coverage **Data requirements**

Testing across the entire MITRE ATT&CK framework **Effort cost**

###### Very high **Metric cost** Very high **Metric expiration**

MITRE ATT&CK ≠ Detection priorities

for illustrative purposes only

## Slide 23

#### Top 5 Threats

External Threat Intel

Internal Incident Trends

Organization Security Risks

## Slide 24

#### Detection Prioritization

Techniques not worked  10%

Techniques with tests  18%

Top 5 Threats

43%  Detections complete

Detections in progress  29 ~~%~~

for illustrative purposes only

## Slide 25

## Not Adjusting to the Altitude

##### Mistake #4

## Slide 26

###### Cost of an Incident or Breach

North Star
MTTD
MTTR
Coverage & Effectiveness
Operational Efficiency

## Slide 27

## Asking "Why?" instead of "How?"

##### Mistake #5

## Slide 28

### Why? How?

## Slide 29

## Maturity Models

Where are we now?

Where are we going? How will we get there?

## Slide 30

#### TDR Maturity Model

#### Observability

Entity & Activity Coverage Searchability

Contextualization

Enrichment

#### Proactive Threat Detection

Intelligence Detection Coverage Detection Engineering Threat Hunting

#### Rapid Response

Preparation Triage & Analysis

Forensics

Response

## Slide 31

#### Maturity Levels

||**Initial**|**Minimal**|**Procedural**|**Innovative**|**Leading**|
|---|---|---|---|---|---|
|**Process**|All manual|20-40%|40-60%
all criticals|60-80%
all criticals and highs|Automated and
mature|
|**Tools**|Ad-hoc|Defined but
not enforced|Centralized|Optimized|AI/ML powered|
|**Docs**|None|Mostly knowledge
sharing|Complete but
manual|Automatic|Live|
|**Testing**|None|Some manual|Complete but
manual|Enforced|Continuous|

## Slide 32

#### Detection Engine

Initial Minimal Procedural Innovative Leading
40-60%  60-80%  Automated and
Process All manual 20-40%
all criticals all criticals and highs mature
Defined but
Tools Ad-hoc Centralized Optimized AI/ML powered
not enforced
Complete but
Docs None Knowledge sharing  Automatic Live
manual
Complete but
Testing None Some manual Enforced Continuous
manual

for illustrative purposes only

## Slide 33

#### TDR Maturity

Current 2024 Target
Initial Minimal Proc Innovative
Observability
Threat Detection
Rapid Response

for illustrative purposes only

## Slide 34

## SAVER Framework

What are the results?

Are we getting better? What data is driving our decisions?

## Slide 35

#### Questions & Outcome

SAVER Metrics

Category

Control & Risk reward

Expiration Data requirements, Effort & Cost

## Slide 36

**Outcome** _What is the goal of measuring this metric?_ **Question** _What question (north star) does this metric answer?_ **Category** _Which SAVER category does this metric fall under?_ **Metric control**

## SAVER Metrics

_How do we control this metric today?_ **Risk reward**

_What risks could this measurement reward?_ **Data requirements**

_What data and sample size is required?_ **Effort cost**

_How much new effort is needed to improve this metric?_ **Metric cost** _What is the cost to collect this metric?_ **Metric expiration** _When will this metric no longer be relevant or needed?_

## Slide 37

Change is hard.

## Slide 38

#### Detection & Response

###### Streamlined

Time spent on FPs
Auto
     Manual
Jan Apr Jul Oct Jan

###### Awareness Top 5 Threats

1. Phishing

2. Account takeover

3. Commodity malware

4. Vishing

5. Data exfiltration

###### Exploration

Program Maturity

New Gaps Found

Current 2024 Target

1. MFA resets unverified

Initial Minimal Proc Innovative
Observability
Threat Detection
Rapid Response

2. Antivirus is  out-of-date

3. No USB drive usage logs

Vigilance Readiness
Detection Engineering Response Time
Techniques
not worked
Detections
complete
Top 5
Threats
Techniques
with MPTs Analyze Contain Recover
Detections in progress

for illustrative purposes only

## Slide 39

## Rethinking How We Measure Detection & Response TDRMM: measure tools & capabilities SAVER: build better metrics Top 5 Threats: not "100% ATT&CK"

## Slide 40

linktr.ee/meoward
