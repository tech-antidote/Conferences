---
title: "Mirage Cyber Deception Against Autonomous Cyber Attacks"
speakers: ["Michael Kouremetis", "Ron Alford", "Dean Lawrence"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/Michael Kouremetis & Ron Alford & Dean Lawrence_Mirage Cyber Deception Against Autonomous Cyber Attacks.pdf"
pages: 29
sha256: "5ca40313f4ec56a666d2dafb632f114906060532d841a8652e7863bbd59345a8"
text_chars: 13956
ocr_pages: 0
has_ocr: false
companion_files: []
extractor: "pymupdf4llm 1.28.2"
converted_at: "2026-08-11T21:19:18Z"
---
# Mirage Cyber Deception Against Autonomous Cyber Attacks

**Speakers:** Michael Kouremetis, Ron Alford, Dean Lawrence  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Michael Kouremetis & Ron Alford & Dean Lawrence_Mirage Cyber Deception Against Autonomous Cyber Attacks.pdf` (29 pages)


## Slide 1

# Mirage: Cyber Deception against Autonomous Cyber Attacks

Speaker(s): Michael Kouremetis, Dr. Ron Alford, Dean Lawrence

#BHUSA  @BlackHatEvents

Copyright 2023 The MITRE Corporation. ALL RIGHTS RESERVED. Approved for public release. Case: 23-2515 (NSEC MOIE)

## Slide 2

## Speakers

**Michael Kouremetis**

**Dr. Ron Alford**

**Dean Lawrence**

**Principal Adversary Emulation Engineer**

**Lead Autonomous Systems Engineer**

**Software Systems Engineer**

**Day Job** : MITRE Caldera lead, Principal **Day Job** : AI researcher, Principal Investigator, Adversary Emulation SME Investigator, Autonomous Systems SME **Hobbies** : Making grand technical **Hobbies** : Playing with robots and assumptions and just rolling with them. autonomous planners.

**Day Job** : Software architecture, AI/ML prototyping, data analysis platforms

**Hobbies** : Fixing bugs Michael introduces into the code base.

#BHUSA @BlackHatEvents

Copyright 2023 The MITRE Corporation. ALL RIGHTS RESERVED. Approved for public release. Case: 23-2515 (NSEC MOIE)

## Slide 3

What would a (true) autonomous Cyber Adversary look like?

v Can sense, plan, and execute actions entirely without a human-in-the-loop

v Automated actions AND autonomous decision-making v Inherent advantages of machine-speed computation and algorithms for previously human-centric tasks, strategy and tactics

#BHUSA  @BlackHatEvents

Copyright 2023 The MITRE Corporation. ALL RIGHTS RESERVED. Approved for public release. Case: 23-2515 (NSEC MOIE)

## Slide 4

Autonomous Cyber Adversary Game Changers

Speed

Pre-trained models and planning algorithms able to execute actions on faster OODA loop

Cyber attacks over before analytics even fire

Scale

Single or numerous AI agents attacking many targets continuously, at the same time, and/or synchronously

Attacking digital infrastructure of entire companies and countries

Flexibility

Bespoke models and algorithms for every TTP, target, and operational profile

On-demand ”AI cyber operators” for any target/scenario

#BHUSA  @BlackHatEvents

Copyright 2023 The MITRE Corporation. ALL RIGHTS RESERVED. Approved for public release. Case: 23-2515 (NSEC MOIE)

## Slide 5

So basically…. Ultron?

(And before you ask - yes, the autonomous cyber adversary would also have a witty James Spader voice and it would mock you for being 10 steps behind.)

Avengers: Age of Ultron

#BHUSA  @BlackHatEvents

Copyright 2023 The MITRE Corporation. ALL RIGHTS RESERVED. Approved for public release. Case: 23-2515 (NSEC MOIE)

## Slide 6

So, what now? Many current cyber defenses and security paradigms are not sufficient for this potential evolution of cyber adversary capability.

One solution. (results may vary)

#BHUSA  @BlackHatEvents

Copyright 2023 The MITRE Corporation. ALL RIGHTS RESERVED. Approved for public release. Case: 23-2515 (NSEC MOIE)

## Slide 7

What about cyber deception? Promising characteristics of cyber deception that could  prove equalizing against autonomous cyber adversary:

v Asymmetrical defensive paradigm v Can be highly targeted and tailored v Higher confidence of true adversary engagement (i.e. less friendly fire)

#### TLDR: Cyber Deception

No Cyber Deception

With Cyber Deception

Cyber Defender

Cyber Defender

Cyber Adversary

**Cyber Adversary**

#BHUSA  @BlackHatEvents

Copyright 2023 The MITRE Corporation. ALL RIGHTS RESERVED. Approved for public release. Case: 23-2515 (NSEC MOIE)

## Slide 8

#### What would autonomous adversaries be built on?

###### Automated Planning, Search

###### Classifiers, Machine-Learning, RL

Source:https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.cs.bham.ac.uk%2F~jxb%2FIAI%2Fw9g.pdf&p sig=AOvVaw0vDhh6pIiflqpHsEKzkfEa&ust=1690141452381000&source=images&cd=vfe&opi=89978449&ved=0CBI QjhxqFwoTCPii-9iJo4ADFQAAAAAdAAAAABAR

Cyber attack knowledge bases, ontologies, & data models

#BHUSA  @BlackHatEvents

Copyright 2023 The MITRE Corporation. ALL RIGHTS RESERVED. Approved for public release. Case: 23-2515 (NSEC MOIE)

## Slide 9

#### What would autonomous adversaries be built on?

#### Area of focus

###### Automated Planning, Search

Source:https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.cs.bham.ac.uk%2F~jxb%2FIAI%2Fw9g.pdf&p sig=AOvVaw0vDhh6pIiflqpHsEKzkfEa&ust=1690141452381000&source=images&cd=vfe&opi=89978449&ved=0CBI QjhxqFwoTCPii-9iJo4ADFQAAAAAdAAAAABAR

###### Classifiers, Machine-Learning, RL

Cyber Attack knowledge bases, ontologies, & data models

#BHUSA  @BlackHatEvents

Copyright 2023 The MITRE Corporation. ALL RIGHTS RESERVED. Approved for public release. Case: 23-2515 (NSEC MOIE)

## Slide 10

#### **An autonomous cyber adversary using automated planning and search would:**

v **Reduce state space by** :

- Ignoring or abstracting state space

- Removing state space via heuristics and sub-goal localization

- Removing symmetric branches/paths

- v **Will rely on online planning and decision-making (i.e. ability to replan)**

- v **Will most likely be goal-oriented and those goals will fall inline with common cyber attack objectives (e.g. persistence, data theft).**

#BHUSA @BlackHatEvents

Copyright 2023 The MITRE Corporation. ALL RIGHTS RESERVED. Approved for public release. Case: 23-2515 (NSEC MOIE)

## Slide 11

##### **An effective cyber defense would prevent or exploit automated planning techniques:**

##### **<u>Techniques</u>**

##### **<u>Countermeasures</u>**

**Reducing State Space**

**(Artificially) Expanding State Space**

**Replanning/ Online Planning**

**Inducing indeterministic state, incorrect belief state**

**Goal Satisfaction**

**Unproductive “journeys”, Path traps**

Copyright 2023 The MITRE Corporation. ALL RIGHTS RESERVED. Approved for public release. Case: 23-2515 (NSEC MOIE)

#BHUSA @BlackHatEvents

## Slide 12

Okay, let's build a system to test and evaluate novel cyber deceptions that are designed to target automated planning and search techniques in use by an autonomous  cyber adversary.

à Mirage

#BHUSA  @BlackHatEvents

Copyright 2023 The MITRE Corporation. ALL RIGHTS RESERVED. Approved for public release. Case: 23-2515 (NSEC MOIE)

## Slide 13

## Required System Components

#### v **Cyber Adversaries**

v **Autonomous agents (for cyber adversaries)**

v **Novel cyber deceptions that target automated planning & search techniques** v **Deception deployment mechanism**

v **Cyber range (to test everything)**

#BHUSA @BlackHatEvents

Copyright 2023 The MITRE Corporation. ALL RIGHTS RESERVED. Approved for public release. Case: 23-2515 (NSEC MOIE)

## Slide 14

Simulation Emulation
Related Work:
CybORG
CyberBattleSim
CyGIL
Cyber Gyms &
Deception Systems
(FY22) Mirage
SODA
Legend
CHIMERA Cyber Gym/Environment
DodgeTron Deception System
Deception
#BHUSA  @BlackHatEvents
CyberBattleSim
+ Ferguson et al.
Red Agents(high fidelity)

Copyright 2023 The MITRE Corporation. ALL RIGHTS RESERVED. Approved for public release. Case: 23-2515 (NSEC MOIE)

## Slide 15

## Mirage: Cyber Adversaries

### **Adversaries**

- Discovery

- Collection

(Simple) Thief

- Exfiltration

- Lateral-Movement

- Defense Evasion

- Impact

- Collection

BlackSun Ransomware

- Discovery

- Credential Access

- Execution

- Lateral-Movement

#BHUSA @BlackHatEvents

Copyright 2023 The MITRE Corporation. ALL RIGHTS RESERVED. Approved for public release. Case: 23-2515 (NSEC MOIE)

## Slide 16

## Mirage: Autonomous Agents

#### **Atomic/Batch**

#### **Look-Ahead**

#### **Guided**

. . .

A simple planner that executes all available actions at each iteration. Used as a base line in the Mirage experiments. **Attack Planners**

1
1 2
1
3
2
3
3
2 4
5
2 1
1
Chooses a single action at each
iteration based on expected
reward. Action-reward values are
set by the user apriori, then in the
operation the planner calculates
rewards for abilities based on the
discounted values of ability
sequences up to a maximum depth.

Constructs a directed attack graph and performs goalbased search to find and execute actions that lie along the shortest path to the goal. At each iteration, the planner chooses the action closest to its goal.

#BHUSA @BlackHatEvents

Copyright 2023 The MITRE Corporation. ALL RIGHTS RESERVED. Approved for public release. Case: 23-2515 (NSEC MOIE)

## Slide 17

## Mirage: Cyber Deceptions

**<u>Countermeasures</u>**

**Black Hole Directory**

Any attempt at file collection by the adversary results in the exfil directory being targeted and all files moved out of the directory. This produces a latent effect on the adversary as the lack of files in the exfil directory will not be discovered until exfiltration is attempted.

Incorrect belief state; Unproductive journey

##### **File Facade**

Exiled files are replaced with large, random files. This alters the environment enticing the adversary to waste execution time.

Unproductive journey

##### **Sneaky Files**

When an adversarial agent performs file discovery commands, a reactive hook will change the names of all files in specified locations. This changes the conditions of the environment and alters the facts understood by the agent.

Incorrect belief state; inducing re-planning

#BHUSA @BlackHatEvents

Copyright 2023 The MITRE Corporation. ALL RIGHTS RESERVED. Approved for public release. Case: 23-2515 (NSEC MOIE)

## Slide 18

## Mirage: Deception System

### **Anansi**

- Ø Windows Service

- Ø <u>How it works:</u>

- Monitors for PowerShell logs at a fixed interval loop

- Checks each command passed for adversarial activity

- Dynamically responds to detected adversarial activity

- Ø Sneaky Files and Black Hole Directory deceptions deployed with **Anansi**

- Ø Modular framework – treats deceptions like plugins

#BHUSA @BlackHatEvents

Copyright 2023 The MITRE Corporation. ALL RIGHTS RESERVED. Approved for public release. Case: 23-2515 (NSEC MOIE)

## Slide 19

## Mirage: Cyber Range

#BHUSA @BlackHatEvents

Copyright 2023 The MITRE Corporation. ALL RIGHTS RESERVED. Approved for public release. Case: 23-2515 (NSEC MOIE)

## Slide 20

Mirage
Anansi
Attack Plane
Control Plane

#BHUSA @BlackHatEvents

Copyright 2023 The MITRE Corporation. ALL RIGHTS RESERVED. Approved for public release. Case: 23-2515 (NSEC MOIE)

## Slide 21

## Experimentation Program

**2 Cyber Adversaries (Thief, BlackSun)**

**3 Attack Planners (Atomic/Batch, Look Ahead, Guided)**

**3 Cyber Deceptions (Sneaky Files, Black Hole, File Facade) +  1 baseline (no deception)**

**3  Episodes per combination**

**= 72 Experiments**

#BHUSA @BlackHatEvents

Copyright 2023 The MITRE Corporation. ALL RIGHTS RESERVED. Approved for public release. Case: 23-2515 (NSEC MOIE)

## Slide 22

## Deception Evaluation Metrics

v Total number of actions executed over the course of the experiment

v Number of actions that failed to complete

v Number of actions that were repeated multiple times in the experiment

- v Time spent on failed actions in seconds

v Time spent planning choice of next actions

v Number of facts learned over each trial

v Cumulative score over all learned facts

v Total experiment run-time in seconds

#BHUSA @BlackHatEvents

Copyright 2023 The MITRE Corporation. ALL RIGHTS RESERVED. Approved for public release. Case: 23-2515 (NSEC MOIE)

## Slide 23

## Results

### **Did the cyber deceptions work?**

**Does the Mirage system provide for effective and efficient evaluation of cyber deceptions against an autonomous cyber adversary?**

#BHUSA @BlackHatEvents

Copyright 2023 The MITRE Corporation. ALL RIGHTS RESERVED. Approved for public release. Case: 23-2515 (NSEC MOIE)

## Slide 24

## Results

**Yep.**

**Obviously.**

#BHUSA @BlackHatEvents

Copyright 2023 The MITRE Corporation. ALL RIGHTS RESERVED. Approved for public release. Case: 23-2515 (NSEC MOIE)

## Slide 25

Results: Did the cyber deceptions work?

(Simple) Thief

BlackSun
Ransomware

#BHUSA @BlackHatEvents

Copyright 2023 The MITRE Corporation. ALL RIGHTS RESERVED. Approved for public release. Case: 23-2515 (NSEC MOIE)

## Slide 26

## Results: Did the cyber deceptions work?

##### **<u>General</u>**

v Cyber deceptions had a clear (negative) performance effect on the cyber planners, across all adversaries.

v The superiority of the advanced planners was really demonstrated with the BlackSun ransomware adversary. (which was the more complex and realistic adversary)

**<u>Specific to planner implementations</u>**

v **Thief adversary** – advanced planners were faster, but deceptions caused many more failed actions.

v **File Façade deception** – advanced planners had to consider more information which caused significant additional planning time.

v **Black Hole deception** – preventing BlackSun ransomware from any lateral-movement.

#BHUSA @BlackHatEvents

Copyright 2023 The MITRE Corporation. ALL RIGHTS RESERVED. Approved for public release. Case: 23-2515 (NSEC MOIE)

## Slide 27

## Results: Efficacy of the Mirage system

##### **Modularity & Scalability**

##### **Practicality**

**How hard is it to create and test more of each component?**

**How realistic is each component?**

Deceptions
Deceptions 100
100
90
90
80
80
70
70
60
60
50
50
40
Metrics 4030 Planners Metrics 30 Planners
20
20
10
10
0
0
Experimentation Ranges
Experimentation Ranges

#BHUSA @BlackHatEvents

Copyright 2023 The MITRE Corporation. ALL RIGHTS RESERVED. Approved for public release. Case: 23-2515 (NSEC MOIE)

## Slide 28

## What’s next for Mirage?

##### v Simulation

##### v Cyber gyms for experimentation

v High fidelity cyber environments for deception simulation

- v Target capabilities:

   - Machine-speed offensive cyber simulations

   - Easy, programmatic defining of cyber deceptions

   - Large scale experimentation

Under Active Development

#BHUSA @BlackHatEvents

Copyright 2023 The MITRE Corporation. ALL RIGHTS RESERVED. Approved for public release. Case: 23-2515 (NSEC MOIE)

## Slide 29

## Q & A

#### **Acknowledgements**

**Contact**

This project would not have been possible without code and technical contributions from Zoe Cheuvront, Ethan Michalak, and David Davila.

Send compliments and kudos to <u>mkouremetis@mitre.org</u>

Send criticisms and challenges to <u>ralford@mitre.org</u>

This work is funded by MITRE's Independent R&D Program.

#BHUSA  @BlackHatEvents

Copyright 2023 The MITRE Corporation. ALL RIGHTS RESERVED. Approved for public release. Case: 23-2515 (NSEC MOIE)
