---
title: "Reinforcement Learning for Autonomous Resilient Cyber Defense"
speakers: ["Sara Farmer"]
conference: "Black Hat"
conference_full: "Black Hat USA 2024"
edition: "USA"
year: 2024
source_pdf: "Black Hat USA 2024 slides/Sara Farmer_Reinforcement Learning for Autonomous Resilient Cyber Defense.pdf"
pages: 25
sha256: "abb80e3e259e3258b552bd19a0905a2dca901dde2e33fd2aba78fbbe614bc947"
text_chars: 13947
ocr_pages: 2
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:38:32Z"
---
# Reinforcement Learning for Autonomous Resilient Cyber Defense

**Speakers:** Sara Farmer  
**Conference:** Black Hat USA 2024  
**Source:** `Black Hat USA 2024 slides/Sara Farmer_Reinforcement Learning for Autonomous Resilient Cyber Defense.pdf` (25 pages)


## Slide 1

Reinforcement Learning for Autonomous Resilient Cyber Defence

Ian Miles, Sara Farmer <u>arcd@fnc.co.uk</u>

Frazer-Nash Reference: 016273-146560V

#BHUSA @BlackHatEvents

## Slide 2

#### Briefing Contributors

Ian

###### Sara

2

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
See Briefing Contributors ~~
USA 2024
EPRAL
FRAZER-NASH
CONSULTANCY
——— A KBR COMPANY —
DATA SCIENCE PARTNERS
BAE SYSTEMS
Lf
(ues
‘wy BMT
cambridge
consultants
Part of Capgemini Invent
ENS
QINETIQ
S| Smith Institute
```

## Slide 3

### Autonomous Resilient Cyber Defence

###### **UK ARCD program**

###### **Because**

Mission:

Not enough cyber responders

- Machine speed cyber response & recovery on military platforms & systems

- Defending IT & OT systems

- Not enough personnel

- No cyber defenders at tactical edge

- Military operator overload

Goals:

- Understand & demonstrate Autonomous Cyber Defence (ACD)

Machine speed attacks

   - Volume, velocity, variety

- Build national skills & knowledge

###### SOAR limitations

100+ projects, 4 years

- Context awareness, mission awareness

3

#BHUSA @BlackHatEvents

## Slide 4

### ARCD Ecosystem

###### **Leads**

UK Supply Chain

- Defence Science & Technology Laboratory: Customer

- Frazer-Nash Consultancy: ARCD Concepts

- QinetiQ: ARCD Test & Evaluation

- Alan Turing Institute: Fundamental Research

Partnerships

Cyber
ML
Defence
Experts
Experts

~200 suppliers registered to view opportunities

Unicorn image: www.vexels.com

4

#BHUSA @BlackHatEvents

## Slide 5

### ARCD Research

Integration

Cyber Threat
Detection

Cyber Situational Awareness

Fundamental Research

Autonomous Machine Speed Response & Recovery

Governance & Assurance

Focus of this Briefing

Image: www.nist.gov/cyberframework

5

#BHUSA @BlackHatEvents

## Slide 6

##### ACD: Autonomous Cyber Defence

Trains and deploys blue (defense) cyber agents

- Rule-based or probabilistic reasoning

Observing a cyber environment

- Capable of detecting an attack

- Inputs = converted infosec feeds (pcaps etc)

Acting in a cyber environment

- Respond or recover in real time

- Acts, or suggests actions to humans

Autonomous Cyber Operations (ACO) trains both blue and red (attacker) agents

Image: CAGE4 challenge

6

#BHUSA @BlackHatEvents

## Slide 7

### Training Defence Agents

###### **Learning algorithms**

###### **Cyber-specific issues**

- **RL** : PPO, DQN, DDQN, MARL etc

   - **Scale**

- **LLMs**

   - **Partial visibility of state space**

- **Others** : Genetic Algorithms, Graph Neural Networks

- **Combinations:** RL + LLM, GNN, GA, etc.

- **Sparse rewards**

- **Needs lots of data**

- **Availability of datasets**

- **Generalisability**

Image: Sutton and Barto

- **Explainability**

PPO = Proximal Policy Optimisation DQN = Deep Q Networks DDQN = Double DQN GA = Genetic Algorithm GNN = Graph Neural Network MARL = Multi Agent Reinforcement Learning

7

#BHUSA @BlackHatEvents

## Slide 8

###### Research question: Meeting "good"

###### **Robustness**

- Tractability

- Scalability

- Generalisability

**Trust**

- Mission-level rewards

Force Effectiveness (Mission objectives) System Effectiveness (system objectives) Effectiveness (operational impact) Performance / System Performance (Agent & system behaviour) Dimensional Parameters (Agent & Environment properties)

- Explainability

- ACD security

8

#BHUSA @BlackHatEvents

Evaluation Lead & Image: QinetiQ

## Slide 9

#### ARCD Environments

ARCD Simulators

Sim2Real: Moving from sim/em to real-world

- <u>PrimAITE, Yawning Titan, Cyborg</u> (TTCP)

- ARCD emulators (cyber ranges)

   - Scaling (from 10s to 100s-1000s of nodes)

   - Real-world observations

- Imaginary Yak, PalisAIDE

- Real world

   - Real-world actions

   - More uncertainty (intrusion detection system etc.)

- IT and OT

High Fidelity

Low Fidelity

Images: www.husarion.com, www.defenceimagery.mod.uk

#BHUSA @BlackHatEvents

Environments Lead & Logos: QinetiQ

9

## Slide 10

# ARCD Demonstrators

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
black hat a
Ame
|
USA 2024
ARCD Demonstrators
```

## Slide 11

### Military Demonstrators

Operational
System
Cyber
First Aid
Military
Realism Generalisability
OT
PoC
Toy Simulator
Basic Logic Human Expert
Complexity of defence actions

Complexity of defence actions

11

#BHUSA @BlackHatEvents

## Slide 12

###### Can RL defend a system?

###### **Key Results**

- Learnt an appropriate response

**X X**

- Outscored the rules-based agent (but gamed the scenario)

- Adapted to environment misconfiguration

- Less effort to adapt after environment modifications

- Overfitting – **need more generalised approaches**

Image: QinetiQ, project delivered by Applied Data Science Partners

12

#BHUSA @BlackHatEvents

## Slide 13

###### Can ACD deploy to un-seen networks?

###### **Problem**

- RL performs poorly in scenarios not experienced in training.

- Handcrafting large volumes of simulated networks not scalable.

###### **Setup**

- GPT4 generated 80 simulated tactical networks (60 for training, 20 for evaluation).

- Deep RL + Graph Neural Networks

###### **Key results & next steps**

- PoC - More training networks improved generalisability

- Upgrading to emulated environment with real tooling

   - Red: Cobalt Strike, Blue: Elastic

- Red teaming exercise early 2025

Image & project delivery: Trustworthy AI #BHUSA @BlackHatEvents

13

## Slide 14

###### Can we build better training adversaries?

###### **Problem**

- Poor performance against adversaries not experienced in training.

- Handcrafting large volumes of attack trajectories not scalable or stochastic.

###### **Setup**

- Create RL-based red agents (to train blue agents)

- Red rewards = stealth, effort, persistence

###### **Key results & next steps**

- Training reduced invalid actions and time to target

- Co-evolution to train blue agents

Red = invalid action, Orange = duplicate action Green = valid action, * = reached target

Images & project delivery: BT

14

#BHUSA @BlackHatEvents

## Slide 15

###### Can ACD defend against next gen attackers?

###### **Problem**

- AI threats may target ACD agents

- Difficult to upgrade ACD agents once deployed

###### **Setup**

- Adversarial Learning - Multiple Response Oracles

   - Don’t forget previous adversaries (AKA catastrophic forgetting)

   - Defend against novel attacks

   - Risks of underestimating the adversary

###### **Key results & next steps**

- Red could not win the game.

- Extending to more complex scenarios (CAGE4)

Images & project delivery: BAE Systems #BHUSA @BlackHatEvents

15

## Slide 16

###### Does ACD work in a real system?

###### **Problem**

- Few cyber experts at the edge

###### **Setup**

- Cyber first aid: simple actions, to contain cyber attacks at source & buy time for a human expert

- Train in simulator, deploy to ROSbot

###### **Key results & next steps**

- Our first end-to-end demonstration of ACD on a real system (RDP overload DoS). Time to recover <1 second

- Field trials: integration into automated air system

Images: www.husarion.com, www.defenceimagery.mod.uk Project delivery: Exalens

16

#BHUSA @BlackHatEvents

## Slide 17

###### Will it work for OT?

###### **Problem**

- Semi-autonomous logistics vehicles (Manned leader, autonomous follower(s))

- Task-saturated operator with limited cyber expertise

###### **Setup**

- Real vehicle architecture (GVA / DDS)

- Multi Agent RL (~30 agents) matching vehicle arch.

- OT action space (power systems, fire alarms, etc.)

###### **Key results & next steps**

- Multi-agent RL can defend against simulated false alarms, manipulated GPS messaging and DoS on V2V link.

- Our approach (offline RL) is difficult but supportable

   - MLSecOps processes and flows

- Digital twin opportunity

GVA = Generic Vehicle Architecture DDS = Data Distribution Service Image & project delivery: Cambridge Consultants V2V = Vehicle to Vehicle #BHUSA @BlackHatEvents

17

#BHUSA @BlackHatEvents

## Slide 18

###### Big OT : Defending Maritime IPMS

###### **Problem**

- Integrated Platform Management System (IPMS): Warship's 'brain’, ICS using sensor data to control machinery

- Cyber operator overloaded, responds slower

- Uncertain data: false positives, uncertainty of action success

###### **Setup**

- IPMS simulator with component interactions

- Varying levels of difficulty

- Multi Agent PPO

- Explainable AI supporting diagnostics

- Deploying to ‘real’ Proxy system (PLCs, HMIs, software, etc.)

HMI = Human-Machine Interface ICS = Industrial Control System PLC = Programmable Logic Controller PPO = Proximal Policy Optimisation

Simulated IPMS
Environment
Produces
Trained ACD Agents
Observations Actions
(Abstract) (Abstract)
Middleware Layer
Observations Actions
(Real) (Real)
‘Real’ proxy System
Project delivery: BMT & ADSP
Informs design & training

Project delivery: BMT & ADSP

18

#BHUSA @BlackHatEvents

Ship image: www.defenceimagery.mod.uk

## Slide 19

###### Maritime IPMS

###### **Key results & next steps**

- Multi-agent defenders out-perform single agents & offer resilience, agents adopted specialist roles

- Struggled to solve ‘hard’ scenarios (red)

   - Alert delays, uncertain false positives/ negatives & action success

- Curriculum learning (blue) & action masking (green) = step change in scalability & exceeds benchmark, combining (orange) compounds benefits

- Distributed architectures - where to put the agents?

- Independent ‘real’ attacks on Proxy

Coloured vertical lines represent switches to a more difficult environment configuration (Easy → Medium → Hard)

Graph shows results for a single agent defender

Image & project delivery: BMT Ltd

19

#BHUSA @BlackHatEvents

## Slide 20

# Conclusions and Recommendations

#BHUSA @BlackHatEvents

## Slide 21

### Outcomes

###### **Key achievements**

- Enhanced UK Cyber/AI and MLSec capability

- Proof of concept – RL works!

- Extended ACD & supporting theory

   - Multiple novel technologies

- End-to-end defence against a 'real' cyberattack on a 'real' network

   - First reported deployment of ACD to a ‘real’ military OT system

###### **Key results**

- RL > rules-based agents, more so complex scenarios

- Multi-agent > single agents & scales

- Generative AI scaling training to enhance robustness

- Consistent requirements for scaling to ‘real’:

   - Action masking

   - Curriculum learning

   - Transfer learning

21

#BHUSA @BlackHatEvents

## Slide 22

### What’s next?

- Increase maturity

   - More realistic & challenging applications

   - Integration with Cyber Situational Awareness tooling

   - Evaluation incl. red teaming & user trials

   - Exploitation routes

- Route to ‘Full Auto’: Human-Machine Teaming

- • Emerging ML approaches (e.g. Foundation Models) • Open sharing: social good

- International collaboration

22

#BHUSA @BlackHatEvents

## Slide 23

### Questions for you

- How would you defend against high volume, velocity & variety of cyber attacks?

- Do you have places where human cyber responders aren't available or are limited in capability/capacity?

- If you have an ACD system, have you thought about its vulnerabilities?

- • Do you have other use cases for ACD technologies? Training, automated pen test?

- Should you start tracking research on ACD / ACO?

- What did we miss??

23

#BHUSA @BlackHatEvents

## Slide 24

###### Some (ARCD) Light Reading for you

###### **2022 ARCD published papers**

- Collyer, "ACD-G: Enhancing Autonomous Cyber Defense Agent <u>Generalization Through Graph Embedded Network Representation", ICML</u> ML4Cyber workshop, 2022

- Andrew, "Developing Optimal Causal Cyber-Defence Agents via Cyber <u>Security Simulation", ICML ML4Cyber workshop, 2022</u>

###### **2023 ARCD published papers**

- Kent, "Using a Deep Boltzmann Machine for Reinforcement Learning in

   - <u>Cyber Defence", 7th IMA conference on math in defence and security, 2023.</u> <Talk on quantum RL>

- Little, "Applying machine learning to attribute cyber attacks" ARCD ICD poster, CAMLIS 2023

- Revell, "Can We Trust Autonomous Cyber Defence for Military Systems?" ARCD HRDO poster, CAMLIS 2023

- Gregory, "FNC ARCD Track 1 newsletter", ARCD showcase 2023

- Cheah, "CO-DECYBER: Co-operative Decision Making for Cybersecurity", SECAI 2023 (presentation)

- Wilson, <u>MARL for maritime operational technology security, CAMLIS 2023</u>

- • Jeffrey, <u>PrimATE</u> codebase

- Palmer, "Deep reinforcement learning for autonomous cyber operations: a <u>survey", 2023</u>

###### **2023 ARCD published papers (continued)**

- Hicks, "Canaries and Whistles: Resilient Drone Communication Networks <u>with (or without) Deep Reinforcement Learning", AISEC 2023</u>

- Bates, "Reward Shaping for Happier Autonomous Cyber Security Agents", AISEC 2023

- Pasteris, "A Hierarchical Nearest Neighbour Approach to Contextual <u>Bandits"</u>

- Caron, "Structure Learning with Adaptive Random Neighborhood Informed <u>MCMC", Neurips 2023</u>

- Caron, <u>SBAE, github repo</u>

- Rice, "Digital defenders", Conduit Newsletter, Serapis Framework

- • Mavroudis, <u>Adaptive Webpage Fingerprinting from TLS Traces</u>

###### **2024 ARCD published papers**

• McFadden, <u>Wendigo: Deep Reinforcement Learning for Denial-of-Service Query Discovery in GraphQL, DLSP 2024</u>

- ATI, Mitigating Deep Reinforcement Learning Backdoors in the Neural Activation Space, DLSP 2024

   - ATI, Autonomous Cyber Defence: Beyond Games

-

###### **Black Hat USA White Paper [link]**

-

- More coming!

20+ more research reports exploring evaluations and environments are available by request here: <u>www.qinetiq.com/en/what-we-do/services-andproducts/autonomous-resilient-cyber-defence</u>

- Pasteris, "Nearest Neighbour with Bandit Feedback", Neurips 2023

24

#BHUSA @BlackHatEvents

## Slide 25

▪ ARCD Concepts [Frazer-Nash Consultancy] www.fnc.co.uk/arcd arcd@fnc.co.uk

- ARCD Test & Evaluation [QinetiQ]

www.qinetiq.com/en/what-we-do/services-and-products/autonomous-resilient-cyber-defence ARCD-Track2@qinetiq.com

## Thank You

▪ AI for Cyber Defence research centre [ATI] www.turing.ac.uk/aicd aicd@turing.ac.uk

- ARCD GitHub

https://github.com/Autonomous-Resilient-Cyber-Defence

▪ CAGE Challenge

https://github.com/cage-challenge

▪ DSTL

arcd@dstl.gov.uk

#BHUSA @BlackHatEvents
