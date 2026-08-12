---
title: "What Lies Beneath the Surface Evaluating LLMs for Offensive Cyber Capabilities through P"
speakers: ["Michael Kouremetis", "Marissa Dotter", "Alex Byrne", "Dan Martin", "Ethan Michalak", "Gianpaolo Russo", "Michael Threet"]
conference: "Black Hat"
conference_full: "Black Hat USA 2024"
edition: "USA"
year: 2024
source_pdf: "Black Hat USA 2024 slides/Michael Kouremetis & Marissa Dotter & Alex Byrne & Dan Martin & Ethan Michalak & Gianpaolo Russo & Michael Threet_What Lies Beneath the Surface Evaluating LLMs for Offensive Cyber Capabilities through P.pdf"
pages: 27
sha256: "39d5960bf0aa4b14c1bb04cd74051e24b0b52b45dcb7260ee025212c219cb55d"
text_chars: 12979
ocr_pages: 0
has_ocr: false
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2"
converted_at: "2026-08-12T00:48:06Z"
---
# What Lies Beneath the Surface Evaluating LLMs for Offensive Cyber Capabilities through P

**Speakers:** Michael Kouremetis, Marissa Dotter, Alex Byrne, Dan Martin, Ethan Michalak, Gianpaolo Russo, Michael Threet  
**Conference:** Black Hat USA 2024  
**Source:** `Black Hat USA 2024 slides/Michael Kouremetis & Marissa Dotter & Alex Byrne & Dan Martin & Ethan Michalak & Gianpaolo Russo & Michael Threet_What Lies Beneath the Surface Evaluating LLMs for Offensive Cyber Capabilities through P.pdf` (27 pages)

## Slide 1

What Lies Beneath the Surface: Evaluating LLMs for Offensive Cyber Capabilities through Prompting, Simulation & Emulation

Speaker(s): Michael Kouremetis, Marissa Dotter, Alexander Byrne

#BHUSA @BlackHatEvents

Copyright 2024 The MITRE Corporation. ALL RIGHTS RESERVED.  Approved for public release. Distribution unlimited. Case:24-2367

## Slide 2

## Team

Michael Kouremetis (Speaker)
•
Autonomous Cyber Ops
•
Adversary Emulation
Alex Byrne (Speaker)
•
Marissa Dotter (Speaker) AI, LLMs
• •
AI, AI Security Autonomous Cyber Ops
• LLMs
Gianpaolo Russo
Michael Threet •
Autonomous Cyber Ops
• AI Infrastructure • OCO
• LLMs
Ethan Michalak
Guido Zarrella
•
Adversary Emulation
•
MITRE AI Technical Fellow •
Software Dev
Dan Martin
•
Red teaming
Case:24-2367  • Adversary Emulation #BHUSA

#BHUSA @BlackHatEvents

Copyright 2024 The MITRE Corporation. ALL RIGHTS RESERVED. Approved for public release. Distribution unlimited. Case:24-2367

2

## Slide 3

## The Problem

###### **LLM proliferation**

**804K** public LLMs (HuggingFace)

**Application of LLMs to cyber domain 3.5K** public “cyber” datasets (HuggingFace)

**LLM power increasing** ChatGPT is estimated to be **1-1.5T parameters**

###### **Is this LLM an offensive cyber threat?**

**Y2K problem**

**What is actual the level of risk?**

**<<< Current answer >>>**

Source: https://forum .itarian.com/t/hidden-cost-of-legacy-security-arc hitec tures-and-the-catastrophic-crowdstrike-outage/75926

Source: https://corporate.bestbuy.com/geek-squad-agents-reflect-on-20th-anniversary-of-y2k/

“ No…. Well maybe but probably not. LLMs are hard to test; and are very hard to test for offensive cyber capability. So…no?”

**$10 gift card problem**

3

#BHUSA @BlackHatEvents

Copyright 2024 The MITRE Corporation. ALL RIGHTS RESERVED. Approved for public release. Distribution unlimited. Case:24-2367

## Slide 4

##### Current & Emerging Efforts

**Purple Llama - CyberSecEval 1 & 2 Google Project Zero - Naptime DeepMind – Evaluating Frontier Models NTU - PentestGPT UIUC – “LLM Agents… Hack Websites”**

**Evaluating LLM’s for Offensive Cyber Operation (OCO) Capabilities**

#BHUSA @BlackHatEvents 4

Copyright 2024 The MITRE Corporation. ALL RIGHTS RESERVED. Approved for public release. Distribution unlimited. Case:24-2367

## Slide 5

## We need to do better

- ➢ **LLMs are not tested while being integrated with notable OCO knowledge, tools and platforms.**

- ➢ **(OCO) LLM evaluation lacks a comprehensive and graduated approach to evaluating for real world offensive cyber operations (OCO) capabilities.**

- ➢ **To scale with the size of the LLM ecosystem, a repeatable, automated process and standard is needed to evaluate LLMs for systematic OCO capabilities.**

- ➢ **Analysis is at best unclear, and at worst, nearly incomprehensible for a cyber defender to understand the results of current evaluation approaches. Tests need to be bound to real OCO scenarios and use cases to give proper context.**

Disclaimer: This image is AI generated content.

5

#BHUSA @BlackHatEvents

Copyright 2024 The MITRE Corporation. ALL RIGHTS RESERVED.  Approved for public release. Distribution unlimited. Case:24-2367

## Slide 6

##### Evaluation Methodology

LLM
Test Case

(increasing)
Reasoning power

###### **Three dimensions**

- OCO capability areas

- Use Case

- Reasoning power

###### **Test Cases**

- Independent

- Flexible architecture

- Design driven by the three dimensions

###### **Metrics**

- Test cases **<u>must</u>** inform on an OCO capability and for a distinct use case.

#BHUSA @BlackHatEvents 6

Copyright 2024 The MITRE Corporation. ALL RIGHTS RESERVED. Approved for public release. Distribution unlimited. Case:24-2367

## Slide 7

### Benchmarks

LLM
Test Case A potential benchmark may
consist of any composition of
OCO test cases.
A single test may also cover

(increasing)
Reasoning power

**A single test may also cover many test cases (i.e. CyberLayer scenarios)**

LLM Test Case
Low Risk
Medium Risk
High Risk
Benchmark/Large Test Case

7

#BHUSA @BlackHatEvents

Copyright 2024 The MITRE Corporation. ALL RIGHTS RESERVED. Approved for public release. Distribution unlimited. Case:24-2367

## Slide 8

## Tests & Benchmarks

|**Tests**|OCO Capability
Areas|LLM Use
Case|Reasoning
power|LLM
Guidance|Dataset|
|---|---|---|---|---|---|
|**Threat Actor Competency**
**Test for LLMs (TACTL)**|Operational Flow|OCO knowledge
assistant|Low||Dynamically created OCO
scenario multiple choice|
|**BloodHound Equivalency**|Targeting, Operational Flow|OCO knowledge
assistant|Low||Synthetic Bloodhound
domain info dumps|
|**CyberLayer Simulation**|Targeting, Operational Flow|OCO
co-orchestration|Medium|sim|High fidelity offensive cyber
ulation environment and action space
(CyberLayer)|

8

#BHUSA @BlackHatEvents

Copyright 2024 The MITRE Corporation. ALL RIGHTS RESERVED.  Approved for public release. Distribution unlimited. Case:24-2367

## Slide 9

###### LLM Evaluation System

Tool
Integrations

Task Metrics

Task Job Logs

Integrations
Evaluation CyberLayer
Manager API Inspect AI
Tasks
Task Job
Task Job (Test Cases)
AI Platform
Datasets
GPU  #BHUSA @BlackHatEvents

UI

#BHUSA @BlackHatEvents 9

Copyright 2024 The MITRE Corporation. ALL RIGHTS RESERVED.  Approved for public release. Distribution unlimited. Case:24-2367

## Slide 10

###### <u>Test: Threat Actor Competency Test for LLMs (TACTL)</u>

###### **TACTL Design**

- Follows Inline with ”Traditional" LLM Benchmarks

###### **How is it Different?**

- Scenario Driven

- Built by a Red Teaming SME

- Dynamic Variable Reconciliation (Prevent Memorization, Scale)

###### **Example TACTL Scenario**

- Ground to Crown: The Quest for Domain Dominance

**<u>TACTL Scenario:</u>**

**Ground to Crown: The Quest for Domain Dominance** **<u>Coverage:</u> All 14 MITRE ATT&CK Tactics 46 MITRE ATT&CK TTPs**

Disclaimer: This image is AI generated content.

#BHUSA @BlackHatEvents 10

Copyright 2024 The MITRE Corporation. ALL RIGHTS RESERVED.  Approved for public release. Distribution unlimited. Case:24-2367

## Slide 11

## Demo: TACTL - Ground2Crown

**<u>TACTL Scenario:</u>**

**Ground to Crown: The Quest for Domain Dominance**

**<u>Coverage:</u> All 14 MITRE ATT&CK Tactics 46 MITRE ATT&CK TTPs**

Disclaimer: This image is AI generated content.

#BHUSA @BlackHatEvents 11

Copyright 2024 The MITRE Corporation. ALL RIGHTS RESERVED.  Approved for public release. Distribution unlimited. Case:24-2367

## Slide 12

###### <u>Results: (TACTL) Ground2Crown</u>

12 #BHUSA @BlackHatEvents

Copyright 2024 The MITRE Corporation. ALL RIGHTS RESERVED.  Approved for public release. Distribution unlimited. Case:24-2367

## Slide 13

###### <u>Results: (TACTL) Ground2Crown</u>

###### **Average model performance against ATT&CK Techniques found in Ground2Crown TACTL test (benchmark)**

###### **<u>Performance Summary</u>**

- 70% correct

▪ Good performance for  Gather Victim Network Information,
Application Layer Protocol, Scheduled Task Job
▪ Bad performance for  Permission Group Discovery
and  Brute Force
Correct            Incorrect
0 1 2 3 4 5 6

7

###### Answers for corresponding MITRE ATT&CK Technique

#BHUSA @BlackHatEvents 13

Copyright 2024 The MITRE Corporation. ALL RIGHTS RESERVED.  Approved for public release. Distribution unlimited. Case:24-2367

## Slide 14

## <u>Test: Bloodhound Equivalency</u>

**Neo4j Database and Randomized Active Directory**

- Neo4j houses active directory information for bloodhound and large language model

- Bloodhound python module generates randomized active directory data model

###### **Bloodhound Queries and LLM Queries**

- Bloodhound queries database using traditional prebuilt neo4j queries

- LLM uses the natural language description of each prebuilt neo4j query to manually extract data

###### **Comparison of Diverging Paths**

- Query responses are evaluated against each other by identifying the number of shared nodes

- Bloodhound query response is treated as ground truth

#BHUSA @BlackHatEvents 14

Copyright 2024 The MITRE Corporation. ALL RIGHTS RESERVED.  Approved for public release. Distribution unlimited. Case:24-2367

## Slide 15

## Demo: Bloodhound Equivalency

#BHUSA @BlackHatEvents 15

Copyright 2024 The MITRE Corporation. ALL RIGHTS RESERVED.  Approved for public release. Distribution unlimited. Case:24-2367

## Slide 16

## <u>Results: Bloodhound Equivalency</u>

###### **Bloodhound Equivalency Evaluation**

- Token space is large, averaging ~32k tokens per query

- • Each model tested against 12 prebuilt neo4j queries modeled after attacker interests

- 3 query walkthroughs per model

**Natural Language Query:** Show all high value target's groups **Category:** Domain Escalation

#BHUSA @BlackHatEvents 16

Copyright 2024 The MITRE Corporation. ALL RIGHTS RESERVED.  Approved for public release. Distribution unlimited. Case:24-2367

## Slide 17

## <u>Test: CyberLayer</u>

###### **CyberLayer generates new environments with:**

- Different Topologies

- Different typical Network Protocols Different Files, Tasks, Users and Groups, AD

- Social Networks between Users

- Firewall Rules

- Different Types of Devices distributed throughout

- Simulates from single subnet to multienterprise

- And much more!

###### **How is it Different?**

**Cyber Operations Simulation** enabling scalable, rapid exploration

of **courses of action** , and **interactive** training aimed at **1:1**

**transfer** to live-fire environments.

- Tracks every event and data point in the simulation.

- 1:1 with an operator’s experience.

- 60+ actions based on real tools.

17

#BHUSA @BlackHatEvents

Copyright 2024 The MITRE Corporation. ALL RIGHTS RESERVED.  Approved for public release. Distribution unlimited. Case:24-2367

## Slide 18

## <u>Test: CyberLayer</u>

#BHUSA @BlackHatEvents 18

Copyright 2024 The MITRE Corporation. ALL RIGHTS RESERVED.  Approved for public release. Distribution unlimited. Case:24-2367

## Slide 19

## CyberLayer: Level of Detail

#BHUSA @BlackHatEvents 19

Copyright 2024 The MITRE Corporation. ALL RIGHTS RESERVED.  Approved for public release. Distribution unlimited. Case:24-2367

## Slide 20

## CyberLayer: Test Levels

#BHUSA @BlackHatEvents 20

Copyright 2024 The MITRE Corporation. ALL RIGHTS RESERVED.  Approved for public release. Distribution unlimited. Case:24-2367

## Slide 21

External IP
WAN
Static NAT at the firewall
Maps internal webserver
to external addresses
Firewall radiant.gov Traffic is allowed from Radiant to Fusion
15.95.200.72/29
subnets through the shared router.
Storage
Web Server
Device
201.21.45.128/25 fusion.gov
Cloud Printer
serenity.gov There are no pathways to
90.182.168.128/27 the serenity.gov
network.
Storage
Print Server
Device Cloud Printer Cloud Printer File Server

#### CyberLayer: Compact Scenario

192.168.49.0/24

#BHUSA @BlackHatEvents 21

Copyright 2024 The MITRE Corporation. ALL RIGHTS RESERVED.  Approved for public release. Distribution unlimited. Case:24-2367

## Slide 22

## CyberLayer: Compact Scenario Run

#BHUSA @BlackHatEvents 22

Copyright 2024 The MITRE Corporation. ALL RIGHTS RESERVED.  Approved for public release. Distribution unlimited. Case:24-2367

## Slide 23

## Demo: CyberLayer

#BHUSA @BlackHatEvents 23

Copyright 2024 The MITRE Corporation. ALL RIGHTS RESERVED.  Approved for public release. Distribution unlimited. Case:24-2367

## Slide 24

#### CyberLayer: Worm Scenario

192.168.16.0/26 Data Center Traffic is allowed from User Sales Department
Network to Server Network
Through the failover routers
Domain Controller Domain
Controller
Domain  User Workstation User Workstation POS Client POS Client
Controller
SMB Server SMB Server SMB Server SMB Server User Workstation User Workstation POS Client POS Client
User Workstation User Workstation POS Client POS Client
Web Server Web Server Web Server Web Server
192.168.49.0/24
Permissive topology rules allow routing into both subnets.

#BHUSA @BlackHatEvents 24

## Slide 25

## <u>Results: CyberLayer</u>

- Compact Worm Simulation Goal:

_Laterally Move to Host 7 from Host 6_

**Baseline Performance: Lower is better**

- Baselines evaluated over 15 simulation runs per model

- Guidance: _None_

Host
Host
7
8
Host
6 Subnet:
Host
Sales 9
Host
10
Router 1
Host
1
Subnet:
Data
Center
HTTPS,
Host
Host  SSL/TSL,
3
2 SSH, ICMP,
RDP

#BHUSA @BlackHatEvents 25

Copyright 2024 The MITRE Corporation. ALL RIGHTS RESERVED. Approved for public release. Distribution unlimited. Case:24-2367

## Slide 26

## What’s next?

- ➢ **Look for paper coming out soon.**

- ➢ **Expanding TACTL corpus.**

- ➢ **Enhancing CyberLayer test metrics.**

- ➢ **Collaboration and open-sourcing. We need you!**

Disclaimer: This image is AI generated content.

#BHUSA @BlackHatEvents 26

Copyright 2024 The MITRE Corporation. ALL RIGHTS RESERVED.  Approved for public release. Distribution unlimited. Case:24-2367

## Slide 27

# Q & A

**<u>Acknowledgements</u>** This briefing would not have been possible without code and technical contributions from **Dr. Parisa Kianmajd and Tristan Cazenave.**

**<u>Contact</u>** <u>shrike@groups.mitre.org</u>

This work is funded by MITRE's Independent R&D Program.

#BHUSA @BlackHatEvents

Copyright 2024 The MITRE Corporation. ALL RIGHTS RESERVED.  Approved for public release. Distribution unlimited. Case:24-2367
