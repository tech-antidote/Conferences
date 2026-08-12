---
title: "Adversarial Fuzzer for Teleoperation Commands Evaluating Autonomous Vehicle Resilience"
speakers: ["Zhisheng Hu", "Shanit Gupta", "Cooper de Nicola"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Zhisheng Hu&Shanit Gupta&Cooper de Nicola_Adversarial Fuzzer for Teleoperation Commands Evaluating Autonomous Vehicle Resilience.pdf"
pages: 75
sha256: "0211b7b3aea45ee9bad96830e023924fddfa333d34407c8f48fc6a764bba34b5"
text_chars: 9910
ocr_pages: 3
has_ocr: true
redacted_secrets: 0
ocr_confidence: 81.5
ocr_unreliable_blocks: 0
vision_verified_blocks: 1
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:27:17Z"
---
# Adversarial Fuzzer for Teleoperation Commands Evaluating Autonomous Vehicle Resilience

**Speakers:** Zhisheng Hu, Shanit Gupta, Cooper de Nicola  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Zhisheng Hu&Shanit Gupta&Cooper de Nicola_Adversarial Fuzzer for Teleoperation Commands Evaluating Autonomous Vehicle Resilience.pdf` (75 pages)


## Slide 1

## **Adversarial Fuzzer for Teleoperation Commands:** Evaluating Autonomous Vehicle Resilience

_Zhisheng Hu, Shanit Gupta, Cooper de Nicola_

#BHUSA   @BlackHatEvents

## Slide 2

##### **About Us**

**Zhisheng Hu** Product Security Engineer

**Shanit Gupta**

Director of Product Security

#BHUSA   @BlackHatEvents

## Slide 3

#### **Disclaimer**

**All tests were conducted in simulation or tightly controlled test environment. Collisions occurred only in simulation. Results are based on outdated software versions.**

#BHUSA   @BlackHatEvents

## Slide 4

## **What is Teleoperation?**

#BHUSA   @BlackHatEvents

## Slide 5

<u>Zoox's TeleGuidance</u> #BHUSA   @BlackHatEvents

## Slide 6

<u>Zoox's TeleGuidance</u> #BHUSA   @BlackHatEvents

## Slide 7

###### **Operations Center**

Detect potential construction zone

Vehicle

#BHUSA   @BlackHatEvents

## Slide 8

**Operations Center Vehicle AI** : Hey human, take a look. Is something in my way?

#BHUSA   @BlackHatEvents

## Slide 9

Operations Center Vehicle
OP:  Yes, lane
shifted or
closed

#BHUSA   @BlackHatEvents

## Slide 10

Operations Center

**AI:** Any suggestions?

Vehicle

#BHUSA   @BlackHatEvents

## Slide 11

Operations Center Vehicle
OP:  Try this
suggestion
Suggestion :
-  Waypoints
- Stop
…

Suggestion :
-  Waypoints
- Stop
…

#BHUSA   @BlackHatEvents

## Slide 12

Operations Center

**AI:** Nice, let me try it.

Vehicle

#BHUSA   @BlackHatEvents

## Slide 13

Operations Center Vehicle
AI:  Don’t worry,
I am still in full
autonomy

#BHUSA   @BlackHatEvents

## Slide 14

## **How to Show Teleoperation is Working Safely**

#BHUSA   @BlackHatEvents

## Slide 15

##### **Implement real-world test case**

#BHUSA   @BlackHatEvents

## Slide 16

##### **Send command**

#BHUSA   @BlackHatEvents

## Slide 17

##### **See if it passes**

#BHUSA   @BlackHatEvents

## Slide 18

**See if it passes**

#BHUSA   @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 82/100 on the text kept, 52/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
black hat
BRIEFINGS

See if it passes

[Top-left photo: forward-facing camera view of a road; orange diamond sign reads "ROAD WORK AHEAD"; the vehicle hood carries the reversed ZOOX wordmark, partially visible as "XOO"]

[Top-right photo: fisheye camera view of the roadway with a red car passing]

[Bottom: overhead perception / visualization view of the same scene with tracked-object labels]

VLR
464692

VLR
464601

VLR
464597

LR
465071

LR
465061

VLR
464621

VLR
464994

VLR
464928

VLR
464825

VLR
464589

VLR
464912

VLR
464828

15.6
MPH
```

## Slide 19

## **How About Mistakes?**

#BHUSA   @BlackHatEvents

## Slide 20

#BHUSA   @BlackHatEvents

## Slide 21

#BHUSA   @BlackHatEvents

## Slide 22

#BHUSA   @BlackHatEvents

## Slide 23

##### **Adversarial variations**

#BHUSA   @BlackHatEvents

## Slide 24

##### **Adversarial variations**

#BHUSA   @BlackHatEvents

## Slide 25

#BHUSA   @BlackHatEvents

## Slide 26

#BHUSA   @BlackHatEvents

## Slide 27

## **Is There A Scalable Way?**

#BHUSA   @BlackHatEvents

## Slide 28

Feedback on
behavior
Monitoring
Target
Fuzzer
system
New Input

#BHUSA   @BlackHatEvents

## Slide 29

Feedback on
behavior
Monitoring
Target
Fuzzer
system
New Input

#BHUSA   @BlackHatEvents

## Slide 30

Feedback on
behavior
Monitoring
Target
Fuzzer
system
New Input

#BHUSA   @BlackHatEvents

## Slide 31

Feedback on
behavior
Monitoring
Target
Fuzzer
system
Construction
truck

Suggested Path AV Other Car

#BHUSA   @BlackHatEvents

## Slide 32

###### **Complex real-world situations**

#BHUSA   @BlackHatEvents

## Slide 33

###### **Complex real-world situations**

Base scenario

Extract

Suggested Path
AV
Other Car

Construction
truck

#BHUSA   @BlackHatEvents

## Slide 34

Base Scenario Input
Add TO params
x
longitudinal offset
y Lateral offset
Construction truck Construction truck
y
x
#BHUSA   @BlackHatEvents

## Slide 35

Feedback on
behavior
Monitoring
Target
system
Construction
truck

Feedback on
behavior
Fuzzer

#BHUSA   @BlackHatEvents

## Slide 36

Feedback on
behavior
Monitoring
Target
Fuzzer
system
Construction
truck

#BHUSA   @BlackHatEvents

## Slide 37

Monitoring
Target
Fuzzer
system
Construction
truck

#BHUSA   @BlackHatEvents

## Slide 38

Monitoring
Target
Fuzzer
system
Construction
truck

#BHUSA   @BlackHatEvents

## Slide 39

## **What We Discovered**

#BHUSA   @BlackHatEvents

## Slide 40

##### **Some numbers**

**Base scenarios**

- 300+ situations

- different geometries, type

Construction
truck

###### **Variations**

- 50,000+ mutants

- 3 valid collisions

#BHUSA   @BlackHatEvents

## Slide 41

Case 1 Case 2
Merging from  Reversing into
Parking Intersection

Case 3
Right Turn with
Multi-Agent
Interaction

#BHUSA   @BlackHatEvents

## Slide 42

##### **Case 1: Merging from Parking**

Situation
Get on road from parking spot
type

4 3
P
P
1
AV
P
2

#BHUSA   @BlackHatEvents

## Slide 43

##### **Case 1: Merging from Parking**

4 3
P
P
1
AV
P
2

**Situation** Get on road from parking spot **type AV** AV stopped in parking lane, following suggested waypoints to get on **maneuver** road

#BHUSA   @BlackHatEvents

## Slide 44

##### **Case 1: Merging from Parking**

4 3
P
P
1
AV
P
2

|**Situation**
**type**|Get on road from parking spot|
|---|---|
|**AV**|AV stopped in parking lane, following suggested waypoints to get on|
|**maneuver**|road|
|**Agent**|[Agent 1-3] ahead of AV, stopped|
|**maneuver**|[Agent 4] ahead of AV, driving following the route|

#BHUSA   @BlackHatEvents

## Slide 45

##### **Case 1: Merging from Parking**

4 3
P
x
P
y 1
AV
P
2

|**Situation**
**type**|Get on road from parking spot|
|---|---|
|**AV**
**maneuver**|AV stopped in parking lane, following suggested waypoints to get on
road|
|**Agent**|[Agent 1-3] ahead of AV, stopped|
|**maneuver**|[Agent 4] ahead of AV, driving following the route|
|**Command**
**variants**|Suggested waypoints with new parameters
●
Longitudinal offset (x)
●
Lateral offset (y)|

#BHUSA   @BlackHatEvents

## Slide 46

#BHUSA   @BlackHatEvents

## Slide 47

#BHUSA   @BlackHatEvents

## Slide 48

#BHUSA   @BlackHatEvents

## Slide 49

#BHUSA   @BlackHatEvents

## Slide 50

Case 1 Case 2 Case 3
Merging from  Reversing into  Right Turn with
Parking Intersection Multi-Agent
Interaction

#BHUSA   @BlackHatEvents

## Slide 51

##### **Case 2: Reversing in Intersection**

1

**Situation** Reversing in Intersection **type**

#BHUSA   @BlackHatEvents

## Slide 52

Case 2: Reversing in Intersection
Situation
Reversing in Intersection
type
AV
AV was driving forward away from the intersection
maneuver

##### **Case 2: Reversing in Intersection**

1

#BHUSA   @BlackHatEvents

## Slide 53

##### **Case 2: Reversing in Intersection**

Situation
Reversing in Intersection
type
AV
AV was driving forward away from the intersection
maneuver
Agent
[Agent 1] behind AV, crossing intersection with the route
maneuver

1

#BHUSA   @BlackHatEvents

## Slide 54

##### **Case 2: Reversing in Intersection**

Situation
Reversing in Intersection
type
AV
AV was driving forward away from the intersection
maneuver
Agent
[Agent 1] behind AV, crossing intersection with the route
maneuver
Suggested reverse waypoint with new parameters
1
Command  ●
Start reversing timing ( t )
variants
after t seconds

#BHUSA   @BlackHatEvents

## Slide 55

##### **Case 2: Reversing in Intersection**

Situation
Reversing in Intersection
type
AV
AV was driving forward away from the intersection
maneuver
Agent
[Agent 1] behind AV, crossing intersection with the route
maneuver
Suggested reverse waypoint with new parameters
1
Command  ●
Start reversing timing ( t )
variants
after t seconds

#BHUSA   @BlackHatEvents

## Slide 56

##### **Case 2: Reversing in Intersection**

Situation
Reversing in Intersection
type
AV
AV was driving forward away from the intersection
maneuver
Agent
[Agent 1] behind AV, crossing intersection with the route
maneuver
Suggested reverse waypoint with new parameters
1
Command  ●
Start reversing timing ( t )
variants
after t seconds

#BHUSA   @BlackHatEvents

## Slide 57

##### **Case 2: Reversing in Intersection**

x
y
1
after t seconds

|**Situation**
**type**|Reversing in Intersection|
|---|---|
|**AV**
**maneuver**|AV was driving forward away from the intersection|
|**Agent**
**maneuver**|[Agent 1] behind AV, crossing intersection with the route|
|**Command**
**variants**|Suggested reverse waypoint with new parameters
●
Start reversing timing (_t_)
●
Destination longitudinal offset (x)|
||●
Destination lateral offset (y)|

#BHUSA   @BlackHatEvents

## Slide 58

#BHUSA   @BlackHatEvents

## Slide 59

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 42/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
= MPH
#BHUSA
@BlackHatEvents
```

## Slide 60

Case 1 Case 2
Merging from  Reversing into
Parking Intersection

Case 3
Right Turn with
Multi-Agent
Interaction

#BHUSA   @BlackHatEvents

## Slide 61

##### **Case 3: Right Turn with Multi-Agent Interaction**

**Situation** Right Turn with Multi-Agent Interaction **type**

1
2

#BHUSA   @BlackHatEvents

## Slide 62

##### **Case 3: Right Turn with Multi-Agent Interaction**

1
2

**Situation** Right Turn with Multi-Agent Interaction **type**

**AV** AV was following suggested waypoints to turn right through **maneuver** intersection

#BHUSA   @BlackHatEvents

## Slide 63

##### **Case 3: Right Turn with Multi-Agent Interaction**

2

1

**Situation** Right Turn with Multi-Agent Interaction **type AV** AV was following suggested waypoints to turn right through **maneuver** intersection **Agent** [Agent 1] behind AV, driving following the route **maneuver** [Agent 2] ahead of AV, driving following the route

AV was following suggested waypoints to turn right through intersection

#BHUSA   @BlackHatEvents

## Slide 64

##### **Case 3: Right Turn with Multi-Agent Interaction**

x
y
2

y
1

**Situation** Right Turn with Multi-Agent Interaction **type**

**AV** AV was following suggested waypoints to turn right through **maneuver** intersection

**Agent** [Agent 1] behind AV, driving following the route **maneuver** [Agent 2] ahead of AV, driving following the route Suggested waypoints with new parameters **Command** ● Longitudinal offset (x) **variants** ● Lateral offset (y)

~~#BHUSA   @BlackHatEvents~~

## Slide 65

##### **Case 3: Right Turn with Multi-Agent Interaction**

**Situation type**

Right Turn with Multi-Agent Interaction

**AV** AV was following suggested waypoints to turn right through **maneuver** intersection

**x y** 1

**Agent** [Agent 1] behind AV, driving following the route **maneuver** [Agent 2] ahead of AV, driving following the route Suggested waypoints with new parameters **Command** ● Longitudinal offset (x) **variants** ● Lateral offset (y) Emergency stop

- Stop location (short bar)

~~#BHUSA   @BlackHatEvents~~

## Slide 66

#BHUSA   @BlackHatEvents

## Slide 67

#BHUSA   @BlackHatEvents

## Slide 68

##### **System improvement**

Before

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 76/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
biSekhat System improvement
BRIEFINGS ee
```

## Slide 69

##### **System improvement**

Before

After

#BHUSA   @BlackHatEvents

## Slide 70

## **Looking Ahead**

#BHUSA   @BlackHatEvents

## Slide 71

Construction
truck

Construction
truck
Teleoperation Perception
Planner

#BHUSA   @BlackHatEvents

## Slide 72

Perception error
Teleoperation Perception
Planner
#BHUSA   @BlackHatEvents

#BHUSA   @BlackHatEvents

## Slide 73

Teleoperation Perception
Planner

#BHUSA   @BlackHatEvents

## Slide 74

### **Safety Must Scale – Keep Fuzzing AI Stack**

#BHUSA   @BlackHatEvents

## Slide 75

**Zhisheng Hu** <u>✉</u> **<u>zhu@zoox.com</u> Shanit Gupta** <u>✉</u> **<u>shgupta@zoox.com</u>**

# Thank You!
