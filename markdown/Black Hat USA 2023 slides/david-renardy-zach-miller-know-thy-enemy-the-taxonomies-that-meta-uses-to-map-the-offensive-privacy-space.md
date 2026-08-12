---
title: "Know Thy Enemy The Taxonomies That Meta Uses to Map the Offensive Privacy Space"
speakers: ["David Renardy", "Zach Miller"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/David Renardy & Zach Miller_Know Thy Enemy The Taxonomies That Meta Uses to Map the Offensive Privacy Space.pdf"
pages: 31
sha256: "a20bcbd62e258e76b23d67d1c63b7664defcbd6c8cfbefbb93e9e11bc02d4179"
text_chars: 8810
ocr_pages: 1
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:15:27Z"
---
# Know Thy Enemy The Taxonomies That Meta Uses to Map the Offensive Privacy Space

**Speakers:** David Renardy, Zach Miller  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/David Renardy & Zach Miller_Know Thy Enemy The Taxonomies That Meta Uses to Map the Offensive Privacy Space.pdf` (31 pages)


## Slide 1

**Know Thy Enemy: The Taxonomies That Meta Uses to Map the Offensive Privacy Space** TItitltet

Zach Miller - Privacy Red Team, Meta David Renardy - Privacy Red Team, Meta

## Slide 2

This talk is...

# This talk is not...

- About design decisions we made on offensive privacy frameworks.

- A reflection on the use-cases of those frameworks.

   - A product or service pitch.

   - A takedown or criticism of preceding frameworks.

   - About absolutes.

- A jumping off point for driving more discussions in the space.

## Slide 3

# **Agenda**

**01**

**Who are Offensive Privacy Threats and how are they tracked?**

02

What are their tactics? ( **Privacy Adversarial Framework** - PAF)

03 What weaknesses do they leverage? (Meta Weakness Enumeration - MWE)

04 What can I do for my organization?

## Slide 4

# **What data do you have and who wants it?**

**Industry / Company** Health Financial Social media Defense Government

**Potential Adversaries**

Data brokers Nation state actors

Private Investigation firms Stalkers

Advertising agencies Political campaign firms

## Slide 5

## **How do we understand threats in Cybersecurity?**

- **Adversary Behaviors** (TTPs) ○ MITRE

- **Weaknesses enumeration and root causes**

-

## Slide 6

# **Privacy friction with existing frameworks**

Privacy-centric tactics or vulnerabilities not present

**OR**

Not enough granularity on Privacy

## Slide 7

# **Privacy-centric tactics**

Example: Adversary downloads data from legacy endpoints via an internet archive

Difficult to express in e.g. Mitre ATT&CK (closest is “Search Open Websites/Domains”)

## Slide 8

# **Privacy-centric vulnerabilities**

Example: Insufficient Anonymization CWE ???

## Slide 9

# **Insufficient Granularity**

Example: Contact point exposure

● CWE-200: Exposure of Sensitive Information to an Unauthorized Actor

## Slide 10

# **Privacy Threat Intelligence**

- Less open reporting than in Security

- Lucky if root cause or technical weakness is identified in reporting

- Common adversary tactics not tracked across cases

## Slide 11

# **Creating our own Privacy taxonomies**

- Design Decisions: ● Who are the data providers? Who are the data consumers?

- ● Privacy-exclusive vs. Privacy-inclusive

## Slide 12

# **Agenda**

01

Who are Offensive Privacy Threats and how are they tracked?

**02 What are their tactics? (Privacy Adversarial Framework - PAF)**

03 What weaknesses do they leverage? (Meta Weakness Enumeration - MWE)

04 What can I do for my organization?

## Slide 13

- **Privacy Adversarial Framework (PAF)**

- ● Inspired by MITRE ATT&CK® , TTP framework for Offensive Privacy. ○ Tactics

- Techniques ■ Subtechniques

- ● Designed to be privacy-exclusive and to supplement existing cybersecurity frameworks.

- Plan for public release with ATT&CK Navigator integration.

## Slide 14

# **Why Privacy-exclusive?**

- Privacy threat actors don’t always need a complete “kill-chain”.

- E.g. Stalker may only want to access data

- ● Choke points for detection and mitigations are different than for cybersecurity. ○ E.g. Spoofing User Agents

## Slide 15

# **Who provides data? Who consumes data?**

- Data sources (tagging examples and incidents): ● Red Team ● Threat Intel ● Investigations

- Data sinks: ● Red Team ● Threat Intel ● Investigations

- ● Insights / Detections

- ● Purple Team

## Slide 16

**Privacy Adversarial Framework**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Reconnaissance
14 techniques
‘Abuse Account Recovery
Flows
Abuse Cached Data
Abuse Error Handling
Messages
Brute Force
eanonymization
Enumerate On-Platform
‘aecounts
[Enumerate On-Platform Assets
Identity Inaviduals Belonging
toa Group
Idontity Rate Limits
Identity Server Endpoints
‘Open-source Inteligence:
Pubic Unsecured Dataset
Reverse Engineer Software
Test Anti-abuse Controls
Establish Infrastructure
10 techniques
‘Acquire On Platform
Resets
Compromise User
Create End User GUI
Create Malicious App
Impersonation
Promote Adversril
Toayservice
Public Unsecured Dataset
Request Manipulation
Use Cloud infrastructure
Utiize Oficial SOK
Asset Takeover
10 techniques
‘Abuse Account Recovery
Flows
‘Abuse Redirects
Brute Force
Bypass 2FA
Exploit Vulnerability
Impersonation
Obtain Access Token
Privilege Escalation
Privileged Assots
Spoofing
Detection)
jn
Enforcement Eva:
‘2techniques
Bypass SPAM
Fiter/Controls
Circumvent Platform
Controls
Obtuscate identity
Obtuscate Too!
Operate Within Rate
Cmts
Spoofing
Switch infrastructure
Use Device Emulation
Use Legacy Tools
Utlize Batched Requests
Utlize Proxy Service
Virtual Phone Numbers
|@.a x
Access Data
35 techniques
‘Abuse ‘invites
‘Abuse Account Recovery
Flows
‘Abuse Cached Data
‘Abuse Eror Handling
Messages
‘Abuse Machine Learning
Me
‘Abuse Misconfigured
Platform Privacy Policies
‘Abuse Real-t
Communications
‘Abuse Typeahead
Suggestions
‘Access Private
Information
‘Access Token Abuse.
‘Authenticate Through
‘automation.
Bypass Authentication
Controle
CColect Platform Metrics
(create Malicious App
Cross Platform Abuse
Enumerate Contact Points
Exploit Vulnerability
Faulty Privacy Policy
Implementation
First Party Tools
Goolocate User
Impersonation
Logged: Access
Loaged-out Access
Monitor Availity Status
‘Query Graphal Endpoints
6.28
User Engagement
6 techniques:
Artificial Engagement...
(Change User Settings... lf
Delete User Data
Forced Engagement
Post Content as User
Targeted Advertsing
12@, 0%
Persistence
S techniques
‘Add Contact Points to
User Account
Change User
Settings
Lockout User
Maintain Vaid Access
Token
Recreate On-Patform
Enforced Assets
10}
Process Data
techniques
Bull Dataset
‘Combine Datasets
ata inference
Deanonymization
Exfiteation
Infer Data From Metrics
Structurendex Scraped Data
Build Revenue /
‘Monetization
7 techniques
Extortion
Freemium Model
Integrate Payment
Publish Data
Run Ads.
Sell Data
Subscription Mode!
legend
```

## Slide 17

# **Using PAF**

Ex 1: Adversary downloads data from legacy endpoints via an internet archive

PTA0005
Access Data

PTA0083 PT0083.001
Abuse Cached Data Archived Site

## Slide 18

# **Using PAF**

Ex 2:

**PTA0002 Establish Infrastructure** PT0061.003 Create Account

PT0063 Utilize Official SDK

**PTA0004 Detection / Enforcement** **<u>Evasion</u>**

PT0052.002 Spoof User Agent

**PT0005 Access Data**

PT008 Logged-In Access PT0040.023 Scraping - Use Open Source Tooling PT003 Access Token Abuse

## Slide 19

# **PAF Outcomes**

- Identify common adversarial behaviors.

- ● Link behaviors to common products and surfaces.

- ● Identify emerging behaviors as they manifest.

- ● Find “choke points” for detection, mitigation and enforcement.

- Develop privacy threat intel feed within your org.

## Slide 20

# **Agenda**

01

Who are Offensive Privacy Threats and how are they tracked?

02

What are their tactics? (Privacy Adversarial Framework - PAF)

**03 What weaknesses do they leverage? (Meta Weakness Enumeration - MWE)**

04 What can I do for my organization?

## Slide 21

# **What weaknesses do they leverage?**

- Adversaries are outcome-driven

- ● Data is our adversaries’ main target

## Slide 22

# **Meta Weakness Enumeration (MWE)**

- Inspired by MITRE’s CWE® and CAPEC®  systems

- ● Designed to be privacy-inclusive

- ● Includes types unique to Meta and our custom, internal systems

## Slide 23

# **Why privacy-inclusive?**

- Vulnerabilities encountered by security, privacy, and integrity teams often overlap

- ● Approaches towards detecting, preventing, and remediating vulnerabilities can also overlap

## Slide 24

# **Who do we expect to use it?**

Meta Internal Processes

**Security Integrity Privacy Vulnerability Incident MWE Management Management Automated Tooling Bug Bounty External Pen Tests**

## Slide 25

# **Who do we expect to use it?**

- Who will actually be applying the taxonomy ● Engineers?

- ● PMs? ● Someone else?

## Slide 26

# **What specifically are we trying to measure?**

- Vectors - the method of abuse

- ● Root Weakness - the underlying technical cause which enabled the Vector to exist

**Vector**

Root Weakness

Contact Point Exposure

Response Side Channel

## Slide 27

# **Summary of MWE Design**

- Privacy-inclusive system applicable across company

- ● Technically-focused system to identify trends, inform tech investment, spread awareness

- ● Categorize vectors of abuse and weaknesses that cause them

## Slide 28

# **MWE Outcomes**

- Educational efforts on privacy-centric vulnerabilities

- ● Cross-organizational collaboration on shared issues

- ● Efficiency gains due to aligning on unified system

## Slide 29

# **Agenda**

01

Who are Offensive Privacy Threats and how are they tracked?

02 What are their tactics? (Privacy Adversarial Framework - PAF)

03 What weaknesses do they leverage? (Meta Weakness Enumeration - MWE)

**04 What can I do for my organization?**

## Slide 30

# **What can I do?**

- Investigate the Privacy threats your product / organization is up against.

- ● Think about privacy-inclusive vs. privacy-exclusive approaches.

- ● Consider adopting PAF via Mitre ATT&CK Navigator integration.

- ● Incorporate MWE design decisions in your own vulnerability management framework.

## Slide 31

Let’s continue the conversation.

David: <u>drenardy@meta.com</u> Zach: <u>zjmiller@meta.com</u>
