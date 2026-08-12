---
title: "If the Adversary Lives Off Your Land, So Should You"
speakers: ["Shane Steiger", "Maretta Morovitz"]
conference: "Black Hat"
conference_full: "Black Hat USA 2026"
edition: "USA"
year: 2026
source_pdf: "BlackHat_USA_2026_Slides/Shane Steiger&Maretta Morovitz_If the Adversary Lives Off Your Land, So Should You.pdf"
pages: 67
sha256: "ad25f41426d04e4c1aa0b58e934bbd073e879e30d0f9766148028340f74d6ea7"
text_chars: 22038
ocr_pages: 1
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:15:26Z"
---
# If the Adversary Lives Off Your Land, So Should You

**Speakers:** Shane Steiger, Maretta Morovitz  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/Shane Steiger&Maretta Morovitz_If the Adversary Lives Off Your Land, So Should You.pdf` (67 pages)

## Slide 1

###### **If the Adversary Lives Off Your Land, So Should You**

Going beyond **A** dversary e **X** posure while **O** bviating them in **L** iving **O** ff **T** he **L** and (AXOLOTL)

1

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

## Slide 2

##### **Meet the Speakers**

Shane Steiger, Esq., CISSP _Principal Cyber Security Engineer_ Cyber Resiliency Team & Engage Team

Maretta Morovitz _Department Manager Digital Investigations_ Cyber Denial, Deception, and Adversary Engagement & Engage Team

2

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

## Slide 3

##### **Briefing Flow**

**What is Adversary Engagement and Why Does it Matter? How Do We Advance Beyond “Deception for Detection”?**

01

**How Are We Working to Enable Advanced Adversary Engagement at Scale? An open-source framework, AXOLOTL, to explore adversary engagement in your environment today**

03

04

02

3

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

## Slide 4

##### **Before We Begin…**

We will not focus on Engage
in this talk, but you can visit
engage.mitre.org to learn
more.

4

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

## Slide 5

##### **Before We Begin…**

**We will not focus on Engage in this talk, but you can visit engage.mitre.org to learn more.**

5

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

## Slide 6

##### **Everyone thought Helms Deep was impenetrable…**

6

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

## Slide 7

##### **Because no one paid attention to this**

7

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

## Slide 8

##### **But do you remember this guy?**

8

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

## Slide 9

##### **And then this…**

9

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

## Slide 10

#### **Defense-in-Depth: Our Helm’s Deep**

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

10

## Slide 11

to

**Cyber Denial: conceal facts and fictions** to create ambiguity about what is or is not real.

**Cyber Deception: reveal facts and fictions** to create and reinforce perceptions and beliefs.

When used together with **strategic planning and analysis** , they provide the pillars of **Adversary Engagement** .

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

10

## Slide 12

##### **The Goals of Adversary Engagement**

**Expose** adversaries

Negatively **Affect** adversaries’ cyber operations

**Elicit** intelligence from adversaries

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

12

## Slide 13

##### **Most people start here.**

Expose  adversaries

Negatively  Affect  adversaries’ cyber operations

Elicit  intelligence from adversaries

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

13

## Slide 14

##### **Briefing Flow**

**What is Adversary Engagement and Why Does it Matter?**

01

**How Do We Advance Beyond “Deception for Detection”?**

**How Are We Working to Enable Advanced Adversary Engagement at Scale? An open-source framework, AXOLOTL, to explore adversary engagement in your environment today**

03

04

02

14.

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

## Slide 15

##### **Advanced “Deception for Detection”**

Deception technology can act as a **canary in the coalmine** when we have known weaknesses or risks we cannot remediate in the near term…

…or as lead
generation
mechanism with
large amounts of
data

15

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

## Slide 16

##### **It is easy to find the weakness when there is only one.**

16

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

## Slide 17

**What if only ONE of these storm drains actually led into the castle, while all the others were convincing decoys?**

**17**

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

## Slide 18

###### **Start to think about “Affecting” Operations**

Malicious cyber
operations

18

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

## Slide 19

##### **Traditional Defense is Reactive**

Most defensive postures implicitly accept a disadvantage.

During reconnaissance and weaponization, the **adversary operates freely and accurately** .

The defender has conceded:

- **Time** (the adversary sets the pace)

*referencing Lockheed <u>Martin’s Cyber Kill Chain® as an attack life cycle</u>

- **Position** (the adversary chooses the attack surface)

- • **Initiative** (the adversary dictates the engagement)

19

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

## Slide 20

##### **Adversary Engagement is Proactive**

Deception assets Traditional defenses
Red’s malicious activities

###### Deceptive assets **disrupt this asymmetry.**

Engage the adversary through believable false signals **before they gain certainty** . The **adversary’s view becomes incomplete, inaccurate,** and **expensive to validate.**

We want to cause them to **make poor decisions, force re-validation/hesitation** , **cost them resources** , and ideally **deter them** altogether.

20

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

## Slide 21

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4 21

## Slide 22

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4 22

## Slide 23

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

23

## Slide 24

You want to get here.

You are here. ©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

24

## Slide 25

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4 25

## Slide 26

##### **Our Dam Metaphor**

- Adversaries are an endless stream

- Stop what you can

- But assume the APT will always find a way through

- Adversaries often follow path of least resistance. Therefore:

   - Make their job difficult, confusing, and slow

   - Channel away from important things

   - Give yourself every opportunity to find them

   - Observe their actions to better detect them

26

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

## Slide 27

##### **Briefing Flow**

**What is Adversary Engagement and Why Does it Matter?**

01

> **How Do We Advance Beyond** 02 **“Deception for Detection”?**

**How Are We Working to Enable Advanced Adversary Engagement at Scale? An open-source framework, AXOLOTL, to explore adversary engagement in your environment today**

03

04

27

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

## Slide 28

##### **Barriers to Advanced Adversary Engagement at Scale**

**Requirement for Additional Commercial Off The Shelf (COTS) Products** Adding another technology is overwhelming

**Expert Dependent Vendor Lock-In** Effective deployments needs technical Heavy dependence on a single expertise and an understanding of the vendor’s ecosystem can limit threat landscape & the defender’s customization and adaptability. environments

28..

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

## Slide 29

##### **How We Needed to Overcome These Barriers**

**Requirement for Additional COTS Products** Leverage existing & open-source resources

**Expert Dependent Vendor Lock-In** Use AI & mapping to Offer flexible, modular ATT&CK® to lower this solutions intended to work expert dependency. alongside common tools

29.

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

## Slide 30

##### **Living off Your Land Engagement (LOTLE)**

Reusing existing assets, data, and forensic artifacts as breadcrumbs, tripwires, and decoys

30

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

## Slide 31

##### **Opportunities and Challenges with LOTLE**

###### **Opportunities**

###### **Challenges**

▪ No new technology.

▪ Deploy as a stand-alone solution or to fill gaps alongside existing products. ▪ Harder to detect or signature.

▪ Tailor deployments to current maturity, environment, goals, and threats.

▪ Require knowledge of assets, data, user behavior, and the threat landscape to be effective. ▪ Often need to write custom solutions to deploy at scale. ▪ Even vendors that sell honeytokens specifically provide only basic deployment resources.

31

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

## Slide 32

##### **Briefing Flow**

**What is Adversary Engagement and Why Does it Matter?**

01

**How Do We Advance Beyond “Deception for Detection”?**

**How Are We Working to Enable Advanced Adversary Engagement at Scale?**

03

**An open-source framework, AXOLOTL, to explore adversary engagement in your environment today**

04

02

32.

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

## Slide 33

### **High Level Architecture**

###### Defender Controlled

1 Understanding of the 3 Gather inputs about yourself, the 2 Understanding of the network and “normal”. threats, priorities, etc. threat landscape. Profiler Planner Threat Landscape

5 Collection of means to 4 Collection of adversary deploy capabilities to engagement capabilities. network/endpoints.

Collection 6 tools to Playbook Planter Processor collect and analyze alerts.

33.

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

## Slide 34

**Proof-of-Concept A** dversary e **X** posure and **O** bviation with **L** iving **O** ff the **L** and (AXOLOTL)

35.

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

## Slide 35

##### **Starting with our architecture let’s examine each component**

Starting with our architecture let’s examine each component
Defender Controlled
Profiler Planner Threat Landscape
Processor
Playbook Planter
36.

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

## Slide 36

### **Let’s get started**

Sun Tzu said
Defender Controlled
“If you  know the
enemy and know
yourself , you need
not fear the result of
a hundred battles.”
Profiler Planner Threat Landscape
Processor
Playbook Planter

Sun Tzu said “If you **know the enemy and know yourself** , you need not fear the result of a hundred battles.”

Threat Landscape

37.

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

## Slide 37

### **Know Yourself, Know Your Enemy**

Defender Controlled

Profiler Planner Threat Landscape
Processor
Playbook Planter
38.

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

## Slide 38

### **The Threat Landscape**

Defender Controlled

Profiler Planner Threat Landscape
Processor
Playbook Planter

39..

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

## Slide 39

### **The Threat Landscape**

Defender Controlled

CTI
Reporting
Profiler Planner Threat Landscape
Processor
Playbook Planter

40..

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

## Slide 40

### **The Profiler**

###### Defender Controlled

CTI
Reporting
Profiler Planner Threat Landscape
Processor
Playbook Planter

41.

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

## Slide 41

### **The Profiler**

Sometimes the Defender Controlled adversary knows more about me than I do. Can I take advantage of th a t? CTI Reporting Profiler Planner Threat Landscape Processor Playbook Planter

42..

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

## Slide 42

### **The Profiler**

Defender Controlled

Sometimes the adversary knows more about me than I do. Can I take advantage of th a t?

CTI Reporting Profiler Planner Threat Landscape Processor Playbook Planter

43.

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

## Slide 43

### **The Profiler**

Profiler Playbook

Defender Controlled

an open-source adversary emulation platform.

Defender Controlled
platform.
CTI
Reporting
Planner

CTI Reporting Threat Landscape

Processor
Planter

44.

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

## Slide 44

### **The Planter**

Defender Controlled

And since Caldera is essentially a C2 can I reuse it?

CTI Reporting Profiler Planner Threat Landscape Processor Playbook Planter

45.

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

## Slide 45

### **The Planter**

Defender Controlled
I  wonder what else
we could have used
CTI
as our C2? Reporting
Profiler Planner Threat Landscape
Processor
Playbook Planter
46.

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

## Slide 46

### **CrowdStrike (or any EDR) can also act as a planter**

Defender Controlled
Profiler Planner Threat Landscape
Processor
Playbook Planter
47.

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

## Slide 47

### **The Planner**

###### Defender Controlled

CTI
Reporting
Engage
Profiler Planning  Planner Threat Landscape
Process
Processor
Playbook Planter

48

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

## Slide 48

### **The Planner**

###### Defender Controlled

CTI
Reporting
Engage
Profiler Planning  Planner Threat Landscape
Process
Processor
Playbook Planter

49

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

## Slide 49

### **The Planner**

###### Defender Controlled

CTI
Reporting
Engage
Profiler Planning  Planner Threat Landscape
Process
Processor
Playbook Planter

50

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

## Slide 50

### **The Playbook**

Defender Controlled

CTI
Reporting
Engage
Profiler Planning  Planner Threat Landscape
Process
Processor
Playbook Planter
51.

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

## Slide 51

The Playbook
Defender Controlled
Found our
IT assets
CTI
Reporting
Engage
Profiler Planning  Planner Threat Landscape
Process
Processor
Playbook Planter
52.

52.

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

## Slide 52

The Playbook
Defender Controlled
Found our
IT assets
Maps to
ATT&CK®
CTI
Reporting
Engage
Profiler Planning  Planner Threat Landscape
Process
Processor
Playbook Planter
53.

53.

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

## Slide 53

Found our
IT assets
CTI
Reporting
Threat Landscape

### **The Playbook**

Defender Controlled Maps to ATT&CK®

Engage
Profiler Planning  Planner
Process
Artifact  Playbook Planter
Dictionary

Processor

54.

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

## Slide 54

The Plays
What else can we do
Defender Controlled
with our
understanding of
“normal”?
CTI
Reporting
Engage
Profiler Planning  Planner Threat Landscape
Process
Artifact  Processor
Playbook Planter
Dictionary
55

55

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

## Slide 55

### **The Plays**

Defender Controlled
We decided to
sh o wca s e 2 ty pes of
AI enabled “plays”:
CTI
honeypots and  Engage  Reporting
Profiler Planning  Planner Threat Landscape
Process
honeytokens
Artifact  Playbook LLMs Planter Processor
Dictionary
56

56

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

## Slide 56

### **The Plays**

Defender Controlled an open-source AI honeypot from Splunk CTI Reporting Engage Profiler Planning Planner Threat Landscape Process Artifact Playbook LLMs Planter Processor Dictionary DECEIVE AI Honeypot

57

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

## Slide 57

### **The Plays**

Defender Controlled open-source honeypots and honeytokens from Thinks

CTI Reporting Engage Profiler Planning Planner Threat Landscape Process OpenCanary & Canarytokens Artifact Playbook LLMs Planter Processor Dictionary DECEIVE AI Honeypot

58

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

## Slide 58

The Plays
Defender Controlled
CTI
Reporting
Engage
Profiler Planning  Planner Threat Landscape
Process
OpenCanary &
Canarytokens
Artifact  Playbook LLMs Planter Processor
Dictionary
DECEIVE AI
Honeypot 59
©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

## Slide 59

### **The Processor**

Defender Controlled Blue Agave (BBX, REY) CTI Reporting Engage Profiler Planning Planner Threat Landscape Process OpenCanary & Canarytokens Blue Agave **Artifact** Playbook LLMs Planter (BBX, REY) Processor **Dictionary** DECEIVE AI Honeypot

60

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

## Slide 60

### **The Processor**

###### Defender Controlled

CTI
Reporting
Engage
Profiler Planning  Planner Threat Landscape
Process
OpenCanary &
Canarytokens
Blue Agave
Artifact  Playbook LLMs Planter (BBX, REY) Processor
Dictionary
DECEIVE AI
Honeypot 61
©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

## Slide 61

### **Use activity sets to visualize alerts**

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

62

## Slide 62

### **Use activity sets to visualize alerts**

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

63

## Slide 63

### **Use activity sets to visualize alerts**

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

64

## Slide 64

### **Use activity sets to visualize alerts**

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

65

## Slide 65

### **Use activity sets to visualize alerts**

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

66

## Slide 66

# **AXOLOTL Components: Overview**

**Caldera** Open-source adversary Profiler emulation platform Playbook Planter **Artifact Dictionary** Map your IT assets, to Playbook Processor ATT&CK, to Engage, to LOTLE opportunities. Planner Playbook **OpenCanar y** Playbook Open-source tools to generate honeypots

**Canarytokens** Open-source tools to generate  honeytokens

**Blue Agave** Detect, label, and visualize ATT&CKbased attack activity through causal graphs

###### **Engage Planning Process**

Set of resources to walk trough the 10-step planning process

###### **DECEIVE**

Open-source AI honeypot  to show how AI can lower the barrier to building realistic, high-fidelity honeypots

67

©2026 THE MITRE CORPORATION. ALL RIGHTS RESERVED. MITRE CONTENT APPROVED FOR PUBLIC RELEASE. DISTRIBUTION UNLIMITED PR_25-02157-4

## Slide 67

###### **Thanks to everyone who made this possible!**

Alice Koeninger

Ouwen Dai Bronwyn Patrick

## **QUESTIONS?**

engage.mitre.org

engage@mitre.org

https://www.linkedin.com/showcase/mitre-engage

Austin Gibbons Mark Perry Ken Smith

Stan Barr

Chris Peloquin

Justin Bui Sean Ha

Jake Steele Baydan Hussen Stephen Forbin Mustafa Akpina
