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
text_chars: 21736
ocr_pages: 0
has_ocr: false
redacted_secrets: 0
ocr_confidence: null
ocr_unreliable_blocks: 0
vision_verified_pages_changed: 67
vision_verified_pages: 67
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2"
converted_at: "2026-08-12T05:42:40Z"
---
# If the Adversary Lives Off Your Land, So Should You

**Speakers:** Shane Steiger, Maretta Morovitz  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/Shane Steiger&Maretta Morovitz_If the Adversary Lives Off Your Land, So Should You.pdf` (67 pages)


## Slide 1

###### **If the Adversary Lives Off Your Land, So Should You**

Going beyond **A**dversary e**X**posure while **O**bviating them in **L**iving **O**ff **T**he **L**and (AXOLOTL)

## Slide 2

##### **Meet the Speakers**

Shane Steiger, Esq., CISSP _Principal Cyber Security Engineer_ Cyber Resiliency Team & Engage Team

Maretta Morovitz _Department Manager Digital Investigations_ Cyber Denial, Deception, and Adversary Engagement & Engage Team

## Slide 3

##### **Briefing Flow**

**01** What is Adversary Engagement and Why Does it Matter?

**02** How Do We Advance Beyond “Deception for Detection”?

**03** How Are We Working to Enable Advanced Adversary Engagement at Scale?

**04** An open-source framework, AXOLOTL, to explore adversary engagement in your environment today

## Slide 4

##### **Before We Begin…**

| Prepare — Plan | Expose — Collect | Expose — Detect | Affect — Prevent | Affect — Direct | Affect — Disrupt | Elicit — Reassure | Elicit — Motivate | Understand — Analyze |
|---|---|---|---|---|---|---|---|---|
| Cyber Threat Intelligence | API Monitoring | Introduced Vulnerabilities | Baseline | Attack Vector Migration | Isolation | Application Diversity | Application Diversity | Cyber Threat Intelligence |
| Engagement Environment | Network Monitoring | Lures | Hardware Manipulation | Email Manipulation | Lures | Artifact Diversity | Artifact Diversity | After-Action Review |
| Gating Criteria | Software Manipulation | Malware Detonation | Isolation | Introduced Vulnerabilities | Network Manipulation | Burn-In | Information Manipulation | Threat Model |
| Operational Objective | System Activity Monitoring | Network Analysis | Network Manipulation | Lures | Software Manipulation | Email Manipulation | Introduced Vulnerabilities | |
| Persona Creation | | | Security Controls | Malware Detonation | | Information Manipulation | Malware Detonation | |
| Storyboarding | | | | Network Manipulation | | Network Diversity | Network Diversity | |
| Threat Model | | | | Peripheral Management | | Peripheral Management | Personas | |
| | | | | Security Controls | | Pocket Litter | | |
| | | | | Software Manipulation | | | | |

We will not focus on Engage in this talk, but you can visit engage.mitre.org to learn more.

## Slide 5

##### **Before We Begin…**

| Prepare — Plan | Expose — Collect | Expose — Detect | Affect — Prevent | Affect — Direct | Affect — Disrupt | Elicit — Reassure | Elicit — Motivate | Understand — Analyze |
|---|---|---|---|---|---|---|---|---|
| Cyber Threat Intelligence | API Monitoring | Introduced Vulnerabilities | Baseline | Attack Vector Migration | Isolation | Application Diversity | Application Diversity | Cyber Threat Intelligence |
| Engagement Environment | Network Monitoring | Lures | Hardware Manipulation | Email Manipulation | Lures | Artifact Diversity | Artifact Diversity | After-Action Review |
| Gating Criteria | Software Manipulation | Malware Detonation | Isolation | Introduced Vulnerabilities | Network Manipulation | Burn-In | Information Manipulation | Threat Model |
| Operational Objective | System Activity Monitoring | Network Analysis | Network Manipulation | Lures | Software Manipulation | Email Manipulation | Introduced Vulnerabilities | |
| Persona Creation | | | Security Controls | Malware Detonation | | Information Manipulation | Malware Detonation | |
| Storyboarding | | | | Network Manipulation | | Network Diversity | Network Diversity | |
| Threat Model | | | | Peripheral Management | | Peripheral Management | Personas | |
| | | | | Security Controls | | Pocket Litter | | |
| | | | | Software Manipulation | | | | |

**We will not focus on Engage in this talk, but you can visit engage.mitre.org to learn more.**

## Slide 6

##### **Everyone thought Helms Deep was impenetrable…**

## Slide 7

##### **Because no one paid attention to this**

## Slide 8

##### **But do you remember this guy?**

## Slide 9

##### **And then this…**

## Slide 10

#### **Defense-in-Depth: Our Helm’s Deep**

- Data
- Application
- Host
- Intranet
- Perimeter
- Physical Security

## Slide 11

**Cyber Denial: conceal facts and fictions** to create ambiguity about what is or is not real.

**Cyber Deception: reveal facts and fictions** to create and reinforce perceptions and beliefs.

When used together with **strategic planning and analysis**, they provide the pillars of **Adversary Engagement**.

Adversary Engagement

Planning & Analysis

Denial

Deception

## Slide 12

##### **The Goals of Adversary Engagement**

**Expose** adversaries

Negatively **Affect** adversaries’ cyber operations

**Elicit** intelligence from adversaries

## Slide 13

##### **Most people start here.**

**Expose** adversaries

Negatively **Affect** adversaries’ cyber operations

**Elicit** intelligence from adversaries

## Slide 14

##### **Briefing Flow**

**01** What is Adversary Engagement and Why Does it Matter?

**02** How Do We Advance Beyond “Deception for Detection”?

**03** How Are We Working to Enable Advanced Adversary Engagement at Scale?

**04** An open-source framework, AXOLOTL, to explore adversary engagement in your environment today

## Slide 15

##### **Advanced “Deception for Detection”**

Deception technology can act as a **canary in the coalmine** when we have known weaknesses or risks we cannot remediate in the near term…

…or as lead generation mechanism with large amounts of data

Example: Sprinkle deceptive assets on the desktop of your senior leaders or employees that repeatedly fail phishing tests

## Slide 16

##### **It is easy to find the weakness when there is only one.**

## Slide 17

**What if only ONE of these storm drains actually led into the castle, while all the others were convincing decoys?**

## Slide 18

###### **Start to think about “Affecting” Operations**

- Better
- Quality
- Worse
- Malicious cyber operations
- ~~Product Scope~~
- Later
- Costlier
- Time
- Cost
- Faster
- Cheaper
- The Project Management Golden Triangle

## Slide 19

##### **Traditional Defense is Reactive**

Reconnaissance | Weaponization | Delivery | Exploitation | Installation | Command and Control | Act on Objectives

Give up? Costly? Don’t know what to do?

Most defensive postures implicitly accept a disadvantage.

During reconnaissance and weaponization, the **adversary operates freely and accurately**.

The defender has conceded:

- **Time** (the adversary sets the pace)
- **Position** (the adversary chooses the attack surface)
- **Initiative** (the adversary dictates the engagement)

*referencing Lockheed Martin’s Cyber Kill Chain® as an attack life cycle

## Slide 20

##### **Adversary Engagement is Proactive**

Reconnaissance | Weaponization | Delivery | Exploitation | Installation | Command and Control | Act on Objectives

Deception assets

Traditional defenses

Red’s malicious activities

Deceptive assets **disrupt this asymmetry.**

Engage the adversary through believable false signals **before they gain certainty**. The **adversary’s view becomes incomplete, inaccurate,** and **expensive to validate.**

We want to cause them to **make poor decisions, force re-validation/hesitation**, **cost them resources**, and ideally **deter them** altogether.

## Slide 21

This slide carries no title or text of its own.

## Slide 22

This slide carries no title or text of its own.

## Slide 23

This slide carries no title or text of its own.

## Slide 24

You want to get here.

You are here.

## Slide 25

This slide carries no title or text of its own.

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

## Slide 27

##### **Briefing Flow**

**01** What is Adversary Engagement and Why Does it Matter?

**02** How Do We Advance Beyond “Deception for Detection”?

**03** How Are We Working to Enable Advanced Adversary Engagement at Scale?

**04** An open-source framework, AXOLOTL, to explore adversary engagement in your environment today

## Slide 28

##### **Barriers to Advanced Adversary Engagement at Scale**

**Requirement for Additional Commercial Off The Shelf (COTS) Products**
Adding another technology is overwhelming

**Expert Dependent**
Effective deployments needs technical expertise and an understanding of the threat landscape & the defender’s environments

**Vendor Lock-In**
Heavy dependence on a single vendor’s ecosystem can limit customization and adaptability.

## Slide 29

##### **How We Needed to Overcome These Barriers**

**Requirement for Additional COTS Products**
Leverage existing & open-source resources

**Expert Dependent**
Use AI & mapping to ATT&CK® to lower this expert dependency.

**Vendor Lock-In**
Offer flexible, modular solutions intended to work alongside common tools

## Slide 30

##### **Living off Your Land Engagement (LOTLE)**

Reusing existing assets, data, and forensic artifacts as breadcrumbs, tripwires, and decoys

Living Off the Land: Turning 2025 CVEs Into Active Defense Opportunities

Owen Sutter, DSc.
Specialist in Cybersecurity Strategy and Innovation

April 29, 2025

Introduction

As threat actors increasingly exploit emerging vulnerabilities, defenders have an opportunity to shift from reactive defense to intentional engagement. One powerful strategy is **living off the land cyber-deception** — using existing technologies to embed deceptive artifacts into an enterprise infrastructure to mislead and monitor adversaries without deploying standalone honeypots.

Rather than deploying exotic, high-friction traps, this approach builds deception into familiar technologies already present in the environment. By aligning deception with existing assets, organizations can engage adversaries earlier and gather valuable intelligence with minimal operational risk.

## Slide 31

##### **Opportunities and Challenges with LOTLE**

###### **Opportunities**

- No new technology.
- Deploy as a stand-alone solution or to fill gaps alongside existing products.
- Harder to detect or signature.
- Tailor deployments to current maturity, environment, goals, and threats.

###### **Challenges**

- Require knowledge of assets, data, user behavior, and the threat landscape to be effective.
- Often need to write custom solutions to deploy at scale.
   - Even vendors that sell honeytokens specifically provide only basic deployment resources.

## Slide 32

##### **Briefing Flow**

**01** What is Adversary Engagement and Why Does it Matter?

**02** How Do We Advance Beyond “Deception for Detection”?

**03** How Are We Working to Enable Advanced Adversary Engagement at Scale?

**04** An open-source framework, AXOLOTL, to explore adversary engagement in your environment today

## Slide 33

### **High Level Architecture**

Defender Controlled

1. Profiler — Understanding of the network and “normal”.
2. Threat Landscape — Understanding of the threat landscape.
3. Planner — Gather inputs about yourself, the threats, priorities, etc.
4. Playbook — Collection of adversary engagement capabilities.
5. Planter — Collection of means to deploy capabilities to network/endpoints.
6. Processor — Collection tools to collect and analyze alerts.

## Slide 34

**Proof-of-Concept**

**A**dversary e**X**posure and **O**bviation with **L**iving **O**ff the **L**and (AXOLOTL)

## Slide 35

##### **Starting with our architecture let’s examine each component**

Defender Controlled

Profiler | Planner | Threat Landscape

Playbook | Planter | Processor

## Slide 36

### **Let’s get started**

Defender Controlled

Profiler | Planner | Threat Landscape

Playbook | Planter | Processor

Sun Tzu said “If you **know the enemy and know yourself,** you need not fear the result of a hundred battles.”

## Slide 37

### **Know Yourself, Know Your Enemy**

Defender Controlled

Profiler | Planner | Threat Landscape

Playbook | Planter | Processor

## Slide 38

### **The Threat Landscape**

Defender Controlled

Profiler | Planner | Threat Landscape

Playbook | Planter | Processor

FEDERAL BUREAU OF INVESTIGATION — Public Service Announcement
Alert Number: I-072026-PSA | 20 July 2026
FBI Warns of Scammers Impersonating the IC3

CVE®

Cybersecurity & Infrastructure Security Agency (CISA)

CISA Known Exploited Vulnerabilities Catalog

## Slide 39

### **The Threat Landscape**

Defender Controlled

Profiler | Planner | Threat Landscape

Playbook | Planter | Processor

CTI Reporting

## Slide 40

### **The Profiler**

Defender Controlled

Profiler | Planner | Threat Landscape

Playbook | Planter | Processor

CTI Reporting

## Slide 41

### **The Profiler**

Defender Controlled

Sometimes the adversary knows more about me than I do. Can I take advantage of that?

Profiler | Planner | Threat Landscape

Playbook | Planter | Processor

CTI Reporting

## Slide 42

### **The Profiler**

Defender Controlled

Sometimes the adversary knows more about me than I do. Can I take advantage of that?

Profiler | Planner | Threat Landscape

Playbook | Planter | Processor

CALDERA

CTI Reporting

## Slide 43

### **The Profiler**

Defender Controlled

CALDERA = an open-source adversary emulation platform.

Profiler | Planner | Threat Landscape

Playbook | Planter | Processor

CALDERA

CTI Reporting

## Slide 44

### **The Planter**

Defender Controlled

And since Caldera is essentially a C2 can I reuse it?

Profiler (CALDERA) | Planner | Threat Landscape (CTI Reporting)

Playbook | Planter (CALDERA) | Processor

## Slide 45

### **The Planter**

Defender Controlled

I wonder what else we could have used as our C2?

Profiler (CALDERA) | Planner | Threat Landscape (CTI Reporting)

Playbook | Planter (CALDERA) | Processor

## Slide 46

### **CrowdStrike (or any EDR) can also act as a planter**

Defender Controlled

Profiler | Planner | Threat Landscape

Playbook | Planter (CALDERA) | Processor

Deception
$whoami

CrowdStrike

<whoami>

<{Deception}>

View only - LOTL Cyber Deception - whoami RDP Breadcrumb — Workflow details

Trigger
Alert > EPP Detection

Condition
If Custom IOA rule is equal to whoami LOLT Deception

TRUE

Administrator: Windows PowerShell ISE — 10.1.4.60

This PC > Local Disk (C:) > Users > Administrator > Documents

| Name | Date modified | Type | Size |
|---|---|---|---|
| My Documents | 10/7/2024 3:55 PM | File folder | |
| WindowsPowerShell | 1/27/2025 8:33 PM | File folder | |
| aws-new-i-0237cd510e2a017b3.rdp | 11/19/2024 3:57 PM | Remote Desktop … | 2 KB |
| Default.rdp | 12/31/2024 5:08 PM | Remote Desktop … | 0 KB |
| document2.xml | 11/21/2024 9:54 PM | XML Document | 10 KB |
| iis7 | 11/19/2024 5:13 PM | Internet Shortcut | 1 KB |
| RDP-Fake.ps1 | 4/14/2025 5:42 PM | Windows PowerS… | 1 KB |
| test.rdp | 4/14/2025 6:13 PM | Remote Desktop … | 1 KB |

8 items

## Slide 47

### **The Planner**

Defender Controlled

Profiler (CALDERA) | Planner (Engage Planning Process) | Threat Landscape (CTI Reporting)

Playbook | Planter (CALDERA) | Processor

## Slide 48

### **The Planner**

Defender Controlled

Profiler (CALDERA) | Planner | Threat Landscape (CTI Reporting)

Playbook | Planter | Processor

**Prepare**

1. **Step 1:** Assess knowledge of your adversaries and your organization
2. **Step 2:** Determine your operational objective
3. **Step 3:** Determine how you want your adversary to react
4. **Step 4:** Determine what you want your adversary to perceive
5. **Step 5:** Determine channels to engage with your adversary
6. **Step 6:** Determine the success and gating criteria

**Operate**

7. **Step 7:** Execute your operation

**Understand**

8. **Step 8:** Turn raw data into actionable intelligence
9. **Step 9:** Feedback intelligence
10. **Step 10:** Analyze successes & failures to inform future actions

## Slide 49

### **The Planner**

Defender Controlled

Profiler (CALDERA) | Planner | Threat Landscape (CTI Reporting)

Playbook | Planter | Processor

Profile

- Campaign A
  - Operation A1
  - Operation A2
- Campaign B
  - Operation B1

## Slide 50

### **The Playbook**

Defender Controlled

Profiler (CALDERA) | Planner (Engage Planning Process) | Threat Landscape (CTI Reporting)

Playbook | Planter (CALDERA) | Processor

## Slide 51

### **The Playbook**

Defender Controlled

Found our IT assets

Profiler (CALDERA) | Planner (Engage Planning Process) | Threat Landscape (CTI Reporting)

Playbook | Planter (CALDERA) | Processor

## Slide 52

### **The Playbook**

Defender Controlled

Found our IT assets

Maps to ATT&CK®

Profiler (CALDERA) | Planner (Engage Planning Process) | Threat Landscape (CTI Reporting)

Playbook | Planter (CALDERA) | Processor

## Slide 53

### **The Playbook**

Defender Controlled

Found our IT assets

Maps to ATT&CK®

**Common IT Element** — This IT asset…

**ATT&CK Technique** — …is impacted by this adversary behavior.

**Engage Activity** — We can collect, observe, or manipulate this behavior…

**LOTLE Opportunity** — …because we have this available resource.

**Implementation** — This is how we can do this for the resources in our specific environment

Profiler (CALDERA) | Planner (Engage Planning Process) | Threat Landscape (CTI Reporting)

Playbook (Artifact Dictionary) | Planter (CALDERA) | Processor

## Slide 54

### **The Plays**

Defender Controlled

What else can we do with our understanding of “normal”?

Profiler (CALDERA) | Planner (Engage Planning Process) | Threat Landscape (CTI Reporting)

Playbook (Artifact Dictionary) | Planter (CALDERA) | Processor

## Slide 55

### **The Plays**

Defender Controlled

We decided to showcase 2 types of AI enabled “plays”: honeypots and honeytokens

Profiler (CALDERA) | Planner (Engage Planning Process) | Threat Landscape (CTI Reporting)

Playbook (Artifact Dictionary, LLMs) | Planter (CALDERA) | Processor

## Slide 56

### **The Plays**

Defender Controlled

DECEIVE AI Honeypot = an open-source AI honeypot from Splunk

Profiler (CALDERA) | Planner (Engage Planning Process) | Threat Landscape (CTI Reporting)

Playbook (Artifact Dictionary, LLMs, DECEIVE AI Honeypot) | Planter (CALDERA) | Processor

## Slide 57

### **The Plays**

Defender Controlled

OpenCanary & Canarytokens = open-source honeypots and honeytokens from Thinks

Profiler (CALDERA) | Planner (Engage Planning Process) | Threat Landscape (CTI Reporting)

Playbook (Artifact Dictionary, OpenCanary & Canarytokens, LLMs, DECEIVE AI Honeypot) | Planter (CALDERA) | Processor

## Slide 58

### **The Plays**

Defender Controlled

Profiler (CALDERA) → LLMs → DECEIVE AI Honeypot / OpenCanary & Canarytokens

Profiler (CALDERA) | Planner (Engage Planning Process) | Threat Landscape (CTI Reporting)

Playbook (Artifact Dictionary, OpenCanary & Canarytokens, LLMs, DECEIVE AI Honeypot) | Planter (CALDERA) | Processor

## Slide 59

### **The Processor**

Defender Controlled

Blue Agave (BBX, REY) = Organizational Network (Host, Host, Host) → Event log files → BBX (Activity set generation) → Activity set file → Rey (User visualization / analysis)

Profiler (CALDERA) | Planner (Engage Planning Process) | Threat Landscape (CTI Reporting)

Playbook (Artifact Dictionary, OpenCanary & Canarytokens, LLMs, DECEIVE AI Honeypot) | Planter (CALDERA) | Processor (Blue Agave — BBX, REY)

## Slide 60

### **The Processor**

Defender Controlled

Activity-set graph — powershell.exe, explorer.exe, systeminfo.exe, whoami.exe, Acrobat.exe, AcroCEF.exe (DESKTOP-0DC3M4B\Sysm…); …PSScriptPolicyTest…create

Execution T1059.001 · Discovery T1082 · Discovery T1033 · Detect EAC0005

Profiler (CALDERA) | Planner (Engage Planning Process) | Threat Landscape (CTI Reporting)

Playbook (Artifact Dictionary, OpenCanary & Canarytokens, LLMs, DECEIVE AI Honeypot) | Planter (CALDERA) | Processor (Blue Agave — BBX, REY)

## Slide 61

### **Use activity sets to visualize alerts**

**RED ACTIVITY**
Red conducts operations, which may include Living Off the Land (LOTL) activities.

## Slide 62

### **Use activity sets to visualize alerts**

**RED ACTIVITY**
Red conducts operations, which may include Living Off the Land (LOTL) activities.

**RED TRIGGERS CANARYTOKEN**
During malicious operation, red unknowingly triggers tripwire.

## Slide 63

### **Use activity sets to visualize alerts**

**RED ACTIVITY**
Red conducts operations, which may include Living Off the Land (LOTL) activities.

**RED TRIGGERS CANARYTOKEN**
During malicious operation, red unknowingly triggers tripwire.

**CANARYTOKEN BEACONS**
Token alerts the canarytoken server. Sysmon records this network activity

## Slide 64

### **Use activity sets to visualize alerts**

**RED ACTIVITY**
Red conducts operations, which may include Living Off the Land (LOTL) activities.

**RED TRIGGERS CANARYTOKEN**
During malicious operation, red unknowingly triggers tripwire.

**CANARYTOKEN BEACONS**
Token alerts the canarytoken server. Sysmon records this network activity

**BBX GENERATES AN ACTIVITY SET**
BBX uses this log as a first pass analytic to trigger the generation of an Activity Set

## Slide 65

### **Use activity sets to visualize alerts**

**RED ACTIVITY**
Red conducts operations, which may include Living Off the Land (LOTL) activities.

**RED TRIGGERS CANARYTOKEN**
During malicious operation, red unknowingly triggers tripwire.

**CANARYTOKEN BEACONS**
Token alerts the canarytoken server. Sysmon records this network activity

**BBX GENERATES AN ACTIVITY SET**
BBX uses this log as a first pass analytic to trigger the generation of an Activity Set

**ACTIVITY SET VIEWABLE IN REY**
Defender can now see an activity set, based on the activity surrounding the token, in Rey.

## Slide 66

# **AXOLOTL Components: Overview**

**Caldera** — Open-source adversary emulation platform (Profiler, Planter)

**Artifact Dictionary** — Map your IT assets, to ATT&CK, to Engage, to LOTLE opportunities. (Playbook)

**OpenCanary** — Open-source tools to generate honeypots (Playbook)

**DECEIVE** — Open-source AI honeypot to show how AI can lower the barrier to building realistic, high-fidelity honeypots (Playbook)

**Canarytokens** — Open-source tools to generate honeytokens (Playbook)

**Blue Agave** — Detect, label, and visualize ATT&CK-based attack activity through causal graphs (Processor)

**Engage Planning Process** — Set of resources to walk trough the 10-step planning process (Planner)

## Slide 67

## **QUESTIONS?**

engage.mitre.org

engage@mitre.org

https://www.linkedin.com/showcase/mitre-engage

**Thanks to everyone who made this possible!**

Alice Koeninger

Ouwen Dai

Bronwyn Patrick

Austin Gibbons

Mark Perry

Ken Smith

Stan Barr

Chris Peloquin

Justin Bui

Sean Ha

Jake Steele

Baydan Hussen

Stephen Forbin

Mustafa Akpina

