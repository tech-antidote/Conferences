---
title: "Weaponizing mobile Infrastructure"
speakers: ["Saleem"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2023"
edition: "ASIA"
year: 2023
source_pdf: "Black Hat Asia 2023 slides/AS-23-Saleem-Weaponizing-mobile-Infrastructure.pdf"
pages: 35
sha256: "c3e98114bd638bc2d60f764e15bc7eee3cc21a37a389e5211a3c9f1c30bffbda"
text_chars: 16522
ocr_pages: 1
has_ocr: true
redacted_secrets: 0
ocr_confidence: 94.6
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T03:48:37Z"
---
# Weaponizing mobile Infrastructure

**Speakers:** Saleem  
**Conference:** Black Hat ASIA 2023  
**Source:** `Black Hat Asia 2023 slides/AS-23-Saleem-Weaponizing-mobile-Infrastructure.pdf` (35 pages)


## Slide 1

#### **” WEAPONIZING MOBILE INFRASTRUCTURE”**

Are Politically Motivated Cyberattacks a Threat to Democracy?

Imran Saleem


> Recovered by OCR — confidence 95/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
” WEAPONIZING MOBILE INFRASTRUCTURE”
Are Politically Motivated Cyberattacks
a Threat to Democracy?
security
intelligence Imran Saleem
Mobileum platform
```

## Slide 2

###### **AGENDA**

**1** Network Interconnect Threats?

**2** Attackers Analogy and Groups

**3** Role of Cyber attacks in armed conflicts **4** The Missed Intel

**5** Political shift can drive cyber-attacks **6** The Financial Impact

- **7** Work Ethics & Disclosure

1

**8**<sup>Recommendations</sup>

1

© 2023  Mobileum, Inc. All rights reserved. Contains Confidential and Proprietary Information of Mobileum, Inc.

1

## Slide 3

###### **NETWORK INTERCONNECT THREATS THREAT SURFACE FOR MOBILE OPERATOR**

Partner systems (APIs, Supply chain etc)
IT Systems
Signalling
National networks
Data / voice
International networks
Cloud
SIM boxes
Radio IoT devices
Internal Mobile devices

© 2023  Mobileum, Inc. All rights reserved. Contains Confidential and Proprietary Information of Mobileum, Inc.

2

## Slide 4

###### **ROAMING INTERCONNECT FRAUD & SECURITY….WHAT IS CSP EXPOSURE ?**

Occurrence
of attack

SMS Fraud & Security
Unapproved business
•
A2P Grey routes
•
Bypass
Fraudsters
Signalling Security
•
SMSishing
•
Marketing SPAM
•
Spoofing subscribers
• Criminals
Faking SMSC
•
Subscriber Tracking
•
Surveillance
•
Call/SMS Interception State Actors
•
VIP Tracking/monitoring
•
Disinformation
•
Cyber Warfare

Complexity of attack

© 2023  Mobileum, Inc. All rights reserved. Contains Confidential and Proprietary Information of Mobileum, Inc.

3

## Slide 5

###### **SIGNALING SECURITY ACROSS INTERCONNECT**

**FS.36**

**FS.11 FS.19 SS7 Security Diameter Security**

**5G Interconnect Security**

**FS.20 GTP-C Security**

© 2023  Mobileum, Inc. All rights reserved. Contains Confidential and Proprietary Information of Mobileum, Inc.

4

## Slide 6

###### **ROAMING INTERCONNECT ARCHITECTURE**

MSC/ HLR/
VLR HSS
GMLC gsmSCF
SS7 SS7
SGSN Diameter Diameter
SMSC
GTP GTP
SGW HTTP2
STP/DEA/B STP/DEA/BGW/ HTTP2
GW/SEPP SEPP IN
MME
SS7/IPX/GRX
GGSN/
VPLMN HPLMN/MVNO
carrier PGW
IMS/PCC
Signalling messages are exchanged between V/H PLMN to support Subscriber
Roaming/Voice/SMS/Data….. Hackers inject  messages to exploit weaknesses

© 2023  Mobileum, Inc. All rights reserved. Contains Confidential and Proprietary Information of Mobileum, Inc.

5

## Slide 7

## **WHO SENDS ILLEGAL MESSAGES?**

1. We focus on signalling in telecoms.

2. Signalling security helps identify what attackers are trying to do.

3. We go “upstream” from the attacker’s perspective.

6

© 2023 Mobileum, Inc. All rights reserved. Contains Confidential and Proprietary Information of Mobileum, Inc.

## Slide 8

##### **Adversaries are:**

- Sophisticated and armed with new techniques

- Well informed and intelligent

- Well paid and funded

##### **ATTACKER’S ANALOGY**

- Well connected and grouped

###### **How much do we know about them?**

- Keep trying approach

- Access to community documents and groups

- Expert in protocols standards

- Aware that most operators use a more tick box security approach and are not enabled with intelligence

- Mobile Operator’s don’t investigate into unknowns

7

© 2023 Mobileum, Inc. All rights reserved. Contains Confidential and Proprietary Information of Mobileum, Inc.

## Slide 9

###### **1. Script Kiddies**

- Small number of badly-formed messages

- **Confused with broken equipment**

##### **Groups of Attackers**

- Send multiple messages to the same test SIMs

- Often send after work hours

###### **2. Grey Operators**

- A2P grey route / SRI-SM location and IMSI checking

- **Mass messages** / bulk business

- Static ranges – some movement of specific GTs

- Focus on **Home Routing bypass** techniques

###### **3. Surveillance Companies**

- **Well-funded**

- Centrally co-ordinated across 10-20 GTs

- Use the same software

- Lease A2P GTs

- Creative encoding methods

- **Move their service provider groups around the world**

8

© 2023 Mobileum, Inc. All rights reserved. Contains Confidential and Proprietary Information of Mobileum, Inc.

## Slide 10

###### **4. State Actors**

- Static, **country-based** GTs

- More standard messages

###### **5. Criminal Service Organizations**

- Specific fraud attacks for **online banking**

- Account takeover (2FA) hijack attacks

- Public / dark web websites

##### **Groups of Attackers**

###### **6. Security Audit Companies**

- **Good guys!**

- Static GTs

- Use their own software stacks

- **Highly innovative attacks** – often copied by others

###### **7. DoS Agents**

- Aim to **bring down** networks

- Being tested recently

- Successful in bringing down Network element.

9

© 2023 Mobileum, Inc. All rights reserved. Contains Confidential and Proprietary Information of Mobileum, Inc.

## Slide 11

###### **ROLE OF CYBER ATTACKS IN ARMED CONFLICTS**

TRUST IS NOT A CYBERSECURITY STRATEGY

© 2023  Mobileum, Inc. All rights reserved. Contains Confidential and Proprietary Information of Mobileum, Inc.

10

## Slide 12

###### **WHY CYBER WARFARE PLAYS A KEY ROLE IN ARMED CONFLICTS?**

Espionage : Monitoring other countries to steal state secrets.

Sabotage : Hostile governments or terrorists may steal information, destroy it.

D/DoS : Prevent users from accessing legitimate service.

Electrical Grid : Attacking the power grid allows attackers to disable critical systems.

Propaganda : Attempts to control the minds and thoughts of people living in or fighting for a target country

Economic Disruptions : Attacking financial institutions.

© 2023  Mobileum, Inc. All rights reserved. Contains Confidential and Proprietary Information of Mobileum, Inc.

## Slide 13

###### **Historical Outlook to politically motivated Cyberattacks?**

###### Nation state a phenomenon existed in past.

© 2023  Mobileum, Inc. All rights reserved. Contains Confidential and Proprietary Information of Mobileum, Inc.

12

## Slide 14

# **“THE MISSED INTEL”**

**“U.S” withdrawal from “AF”**

© 2023  Mobileum, Inc. All rights reserved. Contains Confidential and Proprietary Information of Mobileum, Inc.

13

## Slide 15

###### **TIMELINE OF U.S. WITHDRAWAL FROM AFGHANISTAN –REFLECTION**

A geopolitical conflict leads to patterns captured on the global threat landscape which can provides useful insights on these developing situations.

**Trump Strikes a Deal**

**Feb. 29, 2020** — U.S. and Taliban sign an agreement that sets the terms for a U.S. withdrawal from Afghanistan by May 1, 2021,

https://thediplomat.com/2021/04/the-us-exit-the-view-from-afghanistan/

###### **Biden Follows Through**

**April** **14 ,2021—** Saying it is “time to end the forever war,” Biden announces that all troops will be removed from Afghanistan by Sept. 11.

https://www.factcheck.org/2021/08/timeline-of-u-s-withdrawal-from-afghanistan/

© 2023  Mobileum, Inc. All rights reserved. Contains Confidential and Proprietary Information of Mobileum, Inc.

14

## Slide 16

###### **U.S. WITHDRAWAL FROM AFGHANISTAN - A GLIMPSE OF INTELLIGENCE**

###### **<u>Key Artifacts:</u>**

- Afghanistan was never prime target based on historical investigations.

- Malicious activities started to appear in Feb 2021 due to the political shifts and administrative changes.

- The threat actor behind these operation are nefariously known and potentially have links to Nation state.

- Supported by a few other unresolved sources with the same origin.

- These sources were clustered.

SS7 Attacks
Aug 2021
Sept 2020 No historical activity Feb 2021

© 2023  Mobileum, Inc. All rights reserved. Contains Confidential and Proprietary Information of Mobileum, Inc.

15

## Slide 17

###### **U.S. WITHDRAWAL FROM AFGHANISTAN – MOTIVE & TARGETS**

###### **Targets**

- Prime targets : AF

- Secondary targets : Roamers in AF (Few from NATO Countries)

Potential victim Organization could be:

- News and Media

- NGO’s

- Government Institutions

SS7 Attacks

###### **Motive**

- IMSI Gathering and Network discovery

- Users Surveillance and tracking

- Potential communication interception at radio level.

###### **Threat Indicators**

- Bypass security controls (If any)

© 2023  Mobileum, Inc. All rights reserved. Contains Confidential and Proprietary Information of Mobileum, Inc.

16

## Slide 18

### **POLITICAL SHIFT IN A REGION CAN DRIVE CYBER-ATTACKS!**

© 2023  Mobileum, Inc. All rights reserved. Contains Confidential and Proprietary Information of Mobileum, Inc.

17

## Slide 19

###### **IS “UA” – “RU” CONFLICT ANY DIFFERENT THAN “AF”.**

<u>Russia hacked Ukrainian satellite communications, officials believe</u> - <u>BBC News</u>

<u>Ukraine war: Major internet provider suffers cyber-attack</u> - BBC News

**Russia-linked cyberattacks on Ukraine A timeline**

- **Organized and coordinated.**

- • **Consistent and motivated.**

- **Intel sharing is the key.**

- **Centrally monitored (NATO)**

Does Telecom industry have a concrete intel sharing framework?

© 2023  Mobileum, Inc. All rights reserved. Contains Confidential and Proprietary Information of Mobileum, Inc.

18

<u>Russia's war on Ukraine: Timeline of cyber-attacks (europa.eu)</u>

## Slide 20

###### **UNDERSTANDING RUSSIAN SIGNALLING ACTIVITIES**

###### **In 2022, Russia sources intensified the activities by up to 150 times comparing to 2020/21 historical records.**

SS7 Attacks
Low activity in 2020/21
High activity in 2022

- **These activities were supported by malicious threat indicators known to potentially bypass security controls.**

- **Known techniques listed in the FS.11 few others not available in the guidelines.**

- **Key fact “fuzzing executed targeting various networks.”**

© 2023  Mobileum, Inc. All rights reserved. Contains Confidential and Proprietary Information of Mobileum, Inc.

19

## Slide 21

###### **UNDERSTANDING THE “RU” BACKED STATE ACTORS**

SS7 Attacks

###### **Key behavioural characteristics and threat landscape**

- Is Ukraine and NATO countries on the only target = NO

- Attack Intensity = High

- Coverage = Extreme

- Current state = Active

- Targeting inbound roamers in NATO countries

- Clustered group

- Zero-day exploit = Observed (CVD Submission)

- Identity Impersonation

- Identity spoofing

- Fuzzing

- 60+ countries were targeted.

© 2023  Mobileum, Inc. All rights reserved. Contains Confidential and Proprietary Information of Mobileum, Inc.

20

## Slide 22

###### **ARE THESE “APT’S”, GOVERNMENT-BACKED ATTACKERS?**

Russian attackers aggressively pursue wartime advantage in cyberspace using global signalling.

Threat Intelligence team has uncovered set of attacks targeted towards Ukrainian and NATO countries with following objectives.

|**Attacks Involved**|**Unresolved Russian Origins**|**Targeted**
**Nations**|
|---|---|---|
|Network Discovery|Mapping the network topologies through scanning||
|Information gathering|IMSI extractions and profile extractions.|• Ukraine
• NATO Countries
•Middle east|
|Location tracking|Performing surveillance on targeted victims.|
• Africa|
|Hostile registrations|Hostile location updates made to potentially intercept the comms.||
|Account takeover|Social media accounts taken over.||
|Fraud|Financial fraud observed several other cases.||

© 2023  Mobileum, Inc. All rights reserved. Contains Confidential and Proprietary Information of Mobileum, Inc.

21

## Slide 23

###### **RUSSIAN INFLUENCE IN GLOBAL SIGNALIZATION – RECON AND TARGETED SCANNING**

###### Massive scale scan to discover and map networks.

Multiple networks and countries were scanned. Sequential network identifiers.

|Sequential and
incremental session ID|
|---|

© 2023  Mobileum, Inc. All rights reserved. Contains Confidential and Proprietary Information of Mobileum, Inc.

## Slide 24

###### **RUSSIAN INFLUENCE IN GLOBAL SIGNALIZATION – IDENTITY IMPERSONATION**

###### Identity impersonation for social application through account takeover.

Hostile Registration

Home network shares user profile to malicious source

2FA token access

- Social Application account takeover

- • Input Required : Phone number • Not linked to email.

© 2023  Mobileum, Inc. All rights reserved. Contains Confidential and Proprietary Information of Mobileum, Inc.

23

## Slide 25

###### **RUSSIAN INFLUENCE IN GLOBAL SIGNALIZATION – IDENTITY SPOOFING**

###### How we back our statement that these are nation backed activities.

SCCP layer Spoofed Identity

Spoofed E.164 numbering plan doesn’t belong to any of Operators that owns these low layer identities

these low layer identities
Low layer Spoofed Identity
Link Level analysis revealed traffic
initiated via Russian operator
Low layer Spoofed Identity

© 2023  Mobileum, Inc. All rights reserved. Contains Confidential and Proprietary Information of Mobileum, Inc.

24

## Slide 26

###### **RUSSIAN INFLUENCE IN GLOBAL SIGNALIZATION – ZERO-DAY EXPLOITS**

How we back our statement that these are nation backed activities.

###### **Application Context with additional sub-identifier**

In this vulnerability, the offending source includes an additional subidentifier in the object identifier field. The last octet represents the additional sub identifier.

© 2023  Mobileum, Inc. All rights reserved. Contains Confidential and Proprietary Information of Mobileum, Inc.

25

## Slide 27

###### **RUSSIAN INFLUENCE IN GLOBAL SIGNALIZATION – ZERO-DAY EXPLOITS**

In this incident, the offending source attempted hostile registration using standalone SendAuthenticationInfo (SAI) targeted towards multiple operators with the use of TCAP transaction ID of length 8 octets. While investigation revealed portion of the vulnerable networks responded to these improperly composed MAP Invoke..

###### **TCAP transaction ID length**

In this vulnerability, the offending source use of TCAP transaction ID of length 8 octets to perform hostile registration.

© 2023  Mobileum, Inc. All rights reserved. Contains Confidential and Proprietary Information of Mobileum, Inc.

26

## Slide 28

###### **RESPONSIBLE VULNERABILITY DISCLOSURE**

Coordinated Vulnerability Disclosure

- Briefing paper released.

###### **Actions towards Mobile Operators**

- Mobile Operators are requested to reproduce this vulnerability in their labs.

© 2023  Mobileum, Inc. All rights reserved. Contains Confidential and Proprietary Information of Mobileum, Inc.

27

## Slide 29

#### **“THE FINANCIAL IMPACT”**

© 2023  Mobileum, Inc. All rights reserved. Contains Confidential and Proprietary Information of Mobileum, Inc.

28

## Slide 30

###### **Financial loss towards operators for zero-day exploit!**

**The Mobileum Threat Intelligence team discovered a new vulnerability back in early April 2021**

**A global operator group reported a fraud incident between April and Nov 2021 that exploited that vulnerability**

- **Overall financial impact of this zero-day is not fully known** . • This can be due to factors like lack of visibility.

- Lack of interest in reporting such incident towards GSMA.

© 2023  Mobileum, Inc. All rights reserved. Contains Confidential and Proprietary Information of Mobileum, Inc.

29

## Slide 31

###### **RESPONSIBLE VULNERABILITY DISCLOSURE**

###### **Coordinated Vulnerability Disclosure**

###### **Actions towards Mobile Operators**

- Mobile Operators were requested to reproduce this vulnerability in their labs.

- Operators should consider adapting to the global threat intelligence services.

https://www.gsma.com/security/gsma-mobile-security-research-acknowledgements/

30

© 2023  Mobileum, Inc. All rights reserved. Contains Confidential and Proprietary Information of Mobileum, Inc.

## Slide 32

#### **“WORK ETHICS & DISCLOSURE”**

© 2023  Mobileum, Inc. All rights reserved. Contains Confidential and Proprietary Information of Mobileum, Inc.

31

## Slide 33

###### **WORK ETHICS AND DISCLOSURE**

###### Coordinated Vulnerability Disclosures

- Share key intelligence gathered through security research back to the Industry.

- Share details on zero day exploits that can avoid security breaches and financial losses.

- Objective driven to secure services offered by operators.

© 2023  Mobileum, Inc. All rights reserved. Contains Confidential and Proprietary Information of Mobileum, Inc.

32

## Slide 34

##### **“BLACK HAT SOUND BYTES”**

- Industry should learn from enterprise and build a telecom focus intel sharing framework. Like (STIX, TAXI)

- Processes are key to the implementation of an effective cybersafety strategy to handle cyber conflicts.

- Security guidelines are not a measure of absolute security.

- Operators to enable themselves with a mindset of Global Threat Intelligence

33

© 2023 Mobileum, Inc. All rights reserved. Contains Confidential and Proprietary Information of Mobileum, Inc.

## Slide 35

#### **THANK YOU**

Q & A

© 2023  Mobileum, Inc. All rights reserved. Contains Confidential and Proprietary Information of Mobileum, Inc.

34
