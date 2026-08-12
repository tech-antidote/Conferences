---
title: "When Knowledge Graph Meets TTPs Highly Automated and Adaptive Executable TTP Intelligence for Security Evaluation"
speakers: ["Wu"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2023"
edition: "ASIA"
year: 2023
source_pdf: "Black Hat Asia 2023 slides/AS-23-Wu-When-Knowledge-Graph-Meets-TTPs-Highly-Automated-and-Adaptive-Executable-TTP-Intelligence-for-Security-Evaluation.pdf"
pages: 47
sha256: "11dc670df7db7aa819952fea35b576eff6b5273761cc1bac5623721724c88ff1"
text_chars: 19201
ocr_pages: 6
has_ocr: true
redacted_secrets: 0
companion_files: ["AS-23-Wu-When-Knowledge-Graph-Meets-TTPs-Highly-Automated-and-Adaptive-Executable-TTP-Intelligence-for-Security-Evaluation_tools.txt"]
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:56:41Z"
---
# When Knowledge Graph Meets TTPs Highly Automated and Adaptive Executable TTP Intelligence for Security Evaluation

**Speakers:** Wu  
**Conference:** Black Hat ASIA 2023  
**Source:** `Black Hat Asia 2023 slides/AS-23-Wu-When-Knowledge-Graph-Meets-TTPs-Highly-Automated-and-Adaptive-Executable-TTP-Intelligence-for-Security-Evaluation.pdf` (47 pages)


## Slide 1

### When Knowledge Graph Meets TTPs: Highly Automated and Adaptive Executable TTP Intelligence for Security Evaluation

Jack Tang, Lorin Wu, Porot Mo

#BHASIA @BlackHatEvents

## Slide 2

# About US

##### § Jack Tang @360 Digital Security Group

Jack, the team leader, has over 15 years of expertise in the security industry and is presently focusing on the use of MITRE ATT&CK® in security operations and threat intelligence. He is knowledgeable on kernel and virtualization vulnerability research for Android, Mac, and Windows. He ranked Top 16 on the MSRC in 2016 and Top 34 in 2015. In 2016, he was awarded the Microsoft Mitigation Bypass Bounty. Jack has lectured at security conferences such as CanSecWest, Black Hat, HITCon, and PacSec.

##### § Lorin Wu @360 Digital Security Group

Building an offensive and defensive knowledge graph for cyber security is what Lorin is currently working on. He spent many years working at Trend Micro, where he concentrated on the creation of heuristic patterns and mobile sandbox technologies. During this period, he identified various international cyber security operations that were reported to INTERPOL and Google Security Team.

##### § Porot Mo @360 Digital Security Group

Porot received a master's degree from the University of Chinese Academy of Sciences after graduating from the University of Science and Technology of China. He is currently devoted to the study of offensive and defensive technologies and has three years of expertise in sandbox development.

#BHASIA @BlackHatEvents

## Slide 3

# Agenda

- § Background

- § Solution Overview

- § TTP(Tactics, Techniques, Procedures) Knowledge Graph Construction

   - TTPs Extraction Automatically

- § Adaptive attack path reasoning for BAS (Breach and  Attack Simulation)

#BHASIA @BlackHatEvents

## Slide 4

# Background

#BHASIA @BlackHatEvents

## Slide 5

#### BAS (Breach and Attack Simulation) increasingly needs:

- § Keeping up with the TTPs of attackers.

- § Selecting the appropriate TTP simulation according to the actual situation of the target organization.

- § Using the attack path (sequential TTP) to assess the entire defense-in-depth of the target organization.

#BHASIA @BlackHatEvents

## Slide 6

# Solution Overview

#BHASIA @BlackHatEvents

## Slide 7

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisek hat
ASIA 2023
[TTP entity Extraction + Other artifact |
Cyber Security ” entity and relationship Extraction
Attacks information ~
(APT reports, TTP and other
Ransom reports, artifact and
security blogs, relationship
TTP Knowledge Graph
TTP Reasoning engine
Current status next step TTP
```

## Slide 8

TTP Knowledge Graph Construction - TTPs Extraction Automatically

#BHASIA @BlackHatEvents

## Slide 9

# The Prior Art

Token feature engineering, ML based, MITER Tram project https://github.com/center-for-threat-informed-defense/tram/

Take NER extraction as the task Token feature engineering, ML based, MITER Tram project

GPT3.5, GPT 4.0 based https://chat.openai.com/

#BHASIA @BlackHatEvents

## Slide 10

## Comparisons in actually encountered TTPs data

§ TTPExtractor vs. ChatGPT

OpenAI ChatGPT Luwak TTPExtractor
Precision 0.2015 0.7241
Recall 0.4927 0.5769
F1 Score 0.2861 0.6422

1. The ChatGPT version is 3.5, the test date is 5/5/2023;

2. The test set consists of 5 Chinese reports and 5 English reports, and the final score is obtained after reviewing the predicted results by security experts;

3. Please refer to another attachment for details [Comparative data of TTPExtractor and ChatGPT], includes predicted results for each report, expert review results for each report, and prompts for using GPT.

#BHASIA @BlackHatEvents

## Slide 11

## Key problems to improve the accuracy of TTP extraction

##### § Distinguish primary and secondary tactics and techniques, and extract them based on actual attack scenarios

|Primary|Tactic|Technique|
|---|---|---|
|True|Defense Evasion|Disable or Modify Tools|
||(TA0005)|(T1562.001)|
|False|Defense Evasion
(TA0005)|Modify Registry
(T1112)|

#BHASIA @BlackHatEvents

## Slide 12

## Key problems to improve the accuracy of TTP extraction

- § Extract tactics and techniques involved in attacks from multiple perspectives such as command lines, tools, and code snippets

|Primary|Tactic|Technique|
|---|---|---|
|True|Defense Evasion|Rundll32|
||(TA0005)|(T1218.011)|

#BHASIA @BlackHatEvents

## Slide 13

## Key problems to improve the accuracy of TTP extraction

##### § Extract based on the context of the attack description in the report

Primary
True
False

|Primary|Tactic|Technique|
|---|---|---|
|True|Defense Evasion
(TA0005)|Modify Registry
(T1112)|
|False|Discovery
(TA0007)|Security Software Discovery
(T1518.001 )|

#BHASIA @BlackHatEvents

## Slide 14

## Extract TTPs using pretrained language models and transfer learning

- § Pretrained language models

   - BERT

   - Whole Word Masking(WWM) technology

- § Transfer learning

   - Finetune

https://www.javatpoint.com/transfer-learning-in-machine-learning

After the ransomware enumerates user files, the ransomware starts encrypting those files.

bert-base-uncased, English

通过修改注册表启动项，实现持久化。 bert-wwm-ext, Chinese

#BHASIA @BlackHatEvents

## Slide 15

## Extract TTPs using pretrained language models and transfer learning

§ The pipeline of extract TTPs from unstructured text

Shellcode first checks whether there is a Kaspersky main process avp.exe or Avast main process AvastSvc.exe in the current system, and if it exists, execute the shell command "/c schtasks /create /sc minute /mo 1 /tn WindowsUpdate /tr C: \\ProgramData\\OneDrive.exe".

|Primary|Tactic|Technique|
|---|---|---|
|True|Persistence
(TA0003)|Scheduled Task
(T1053.005)|
|False|Execution
(TA0002)|Windows Command Shell
(T1059.003)|
|False|Defense Evasion
(TA0005)|Masquerade Task or Service
(T1036.004)|
|False|Discovery
(TA0007)|Security Software Discovery
(T1518.001)|

#BHASIA @BlackHatEvents

## Slide 16

TTP Knowledge Graph Construction - Semantic Web Building

#BHASIA @BlackHatEvents

## Slide 17

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
TTP Knowledge Graph Construction
m
u
O
i
<
Ul
x
0
&
3
Cg
fe}
NVD
<—-—-—-—-—->
Playbooks) < — — — — — — >| Pcap Data
—> TTPs
MITRE ATT&€K————
```

## Slide 18

# ATT&CK semantic web building

- § Appropriate offensive entities and relationships

   - Technique – [platformRequires] –> Platform

   - Technique – [serviceRequires] –> ServiceState

#BHASIA @BlackHatEvents

## Slide 19

# ATT&CK semantic web building

- § Appropriate offensive entities and relationships

   - Technique – [achieves] –> Tactic

   - Technique – [permissionRequires] –> Permission

   - Technique – [permissionObtains] –> Permission

#BHASIA @BlackHatEvents

## Slide 20

# ATT&CK semantic web building

- § Appropriate defensive entities and relationships

   - DataSource – [selects] –> DataComponent

   - DataComponent – [detects] –> Technique

selects

Defensive Part

Offensive Part

#BHASIA @BlackHatEvents

## Slide 21

# ATT&CK semantic web building

- § Appropriate defensive entities and relationships

   - DefenseProduct – [produces] –> DataComponent

   - DataComponent – [detects] –> Technique

**selects**

**produces**

Defensive Part

Offensive Part

#BHASIA @BlackHatEvents

## Slide 22

# ATT&CK semantic web building

detects
achieves
achieves
produces
Asset Information
serviceRequires
permissionRequires permissionObtains
selects Service/Software
: installed
: running
: configured
platformRequires
Defensive Part
Host Permission
Offensive Part
#BHASIA @BlackHatEvents

#BHASIA @BlackHatEvents

## Slide 23

# TTPs and playbooks semantic web building

- § Extracted TTPs and their playbooks

   - Procedure – [taid] –> Tactic

   - Procedure – [tid] –> Technique

   - Procedure – [privilegesRequired] –> Permission

   - Procedure – [privilegesObtained] –> Permission

   - Procedure – [acts] –> Playbook

   - Playbook – [attacks] –> Asset

acts

Defensive Part Offensive Part

#BHASIA @BlackHatEvents

## Slide 24

# TTPs and playbooks semantic web building

- § NVD vulnerabilities and their PCAP data

   - Vulnerability – [data property] –> CVSS

   - Vulnerability – [attacks] –> Asset

   - Vulnerability – [acts] –> Playbook

###### **attacks**

Defensive Part

**acts**

Offensive Part

#BHASIA @BlackHatEvents

## Slide 25

# Adaptive attack path reasoning for BAS

#BHASIA @BlackHatEvents

## Slide 26

# Input data for assessment

- § Asset information for the target organization

   - Results of asset mapping tools

- § Network typology configuration for the target organization

   - Ensure the authenticity of the network topology where the assets are located as much as possible, e.g. determine the location of the assets, DMZ, Office and network connectivity

- § Defense-in-depth typology configuration for the target organization

   - Keep asset-based security topologies as real as possible, e.g. determine which assets are protected by which security products

#BHASIA @BlackHatEvents

## Slide 27

- Asset: exposed assets info

- • Defense-in-depth: products info

- Asset: the target asset info

- • Defense-in-depth: products info

- • Permission: Obtained host permission by previous TTP playbook execution result

#BHASIA @BlackHatEvents

## Slide 28

## TTP Reason Engine: Tactics, techniques reasoning

- § Reasoning based on MITRE ATT&CK

   - The first dimension: The MITRE ATT&CK kill-chain phase determines the tactic route

      - ü Start from Initial Access (TA0001)

      - ü Put Credential Access (TA0006) and Lateral Movement (TA0008) last

   - The second dimension: Using the results of the previous step simulation attack, reason the techniques that can be used in the next phase

      - ü Host permission: obtained from the previous step’s simulated attack, meet the techniques

      - ü Asset: The asset condition and platform that meet the techniques

      - ü Defense-in-depth: The techniques that enable defense products to produce detection data

#BHASIA @BlackHatEvents

## Slide 29

## TTP Reason Engine: Tactics, techniques reasoning

- § Reasoning based on MITRE ATT&CK

   - Reasoning based on permission levels

      - ü E.g. for Windows, system permission can act as one of [system, Administrator, User and None]

networkAccess: All privilegesRequired: None Attack: success confidentialityImpact: High integrityImpact: High availabilityImpact: High specifiedRunningUser: httpd

#BHASIA @BlackHatEvents

## Slide 30

## TTP Reason Engine: Tactics, techniques reasoning

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2023
TTP Reason Engine: Tactics, techniques reasoning
TA0001: Initial Access ———————® TA0002: Execution .—» 740004: Privilege ____'_y _ TA0008: Lateral
Escalation Movement
. : User . 2 User . User | Adm User
T1189: Drive-by --> T1059.003: Windows ; T1548.002: Bypass T1021.004: SSH
Compromise User Command Shell User | User Account Control ade | ~~" User |
Adm Adm
T1190: Exploit Public- T1053.005: Scheduled T1134: Access Token [LUS* T1021.001: Remote User
? 1
: tae ' > . :
Facing Application |: 5 __ Task adm Manipulation | Adm | Desktop Protocol User |
User N/A User
. . . . User
- -)| T1106: Native API T1068: Exploitation for T1534: Internal
T1078: Valid Accounts SS N/A > Privilege Escalation | Ad Spearphishing nA
```

## Slide 31

## TTP Reason Engine: Tactics, techniques reasoning

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2023
TTP Reason Engine: Tactics, techniques reasoning
TAO001: Initial Access ———————® _ TAO002: Execution .——» 740004: Privilege ___y —_ TA0008: Lateral
Escalation Movement
T1189: Drive-by User T1059.003: Windows |S" T1548.002: Bypass User | Adm 11021.004: SSH User
Compromise User Command Shell User | User Account Control ade | ~~" User |
T1190: Exploit Public- [°° T1053.005: Scheduled |49™ T1134: Access Token [US| 4¢™ T1021.001: Remote [US
: tae > . :
Facing Application | User | Task adm Manipulation | Adm | Desktop Protocol User |
User N/A . ogo gs . User
T1078: Valid Accounts T1106: Native API T1068: Exploitation for T1534: Internal
| User | N/A > Privilege Escalation ade Spearphishing N/A
User
```

## Slide 32

# TTP Reason Engine: Procedures reasoning

- § Based on real world procedures distribution

   - Continuously collect procedures by TTP Extraction approach

- § Determine possibility which TTP to use in the next step

   - In the TTP chains we collected in real cybersecurity attacks

      - ü in current state: permission owned or obtained, asset

      - ü The most possible procedures used in attacks: the quantity, the popularity

#BHASIA @BlackHatEvents

## Slide 33

# TTP Reason Engine: Procedures reasoning

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2023
TTP Reason Engine: Procedures reasoning
TA0001: Initial Access ——————— _ TA0002: Execution .——» 7A0004: Privilege _y = TA0008: Lateral
Escalation Movement
. a. User mVVF User @) . User | Adm User
T1189: Drive-by ; T1059.003: Windows ; T1548.002: Bypass T1021.004: SSH
Compromise User Command Shell User | User Account Control ade | User |
T1190: Exploit Public- [°° T1053.005: Scheduled |49™ @ 111134: Access Token [LY 144") | @ |11021.001: Remote USF
: tae > . :
Facing Application | User | Task adm Manipulation | sys | Desktop Protocol User |
User N/A . eae User . User
T1078: Valid Accounts T1106: Native API @ . | T1068: Exploitation for @_ | T1534: Internal
| User | N/A > Privilege Escalation ade Spearphishing N/A
```

## Slide 34

# TTP Reason Engine: Procedures reasoning

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2023
TTP Reason Engine: Procedures reasoning
TA0001: Initial Access ——————— _ TA0002: Execution _——p» 7A0004: Privilege = TA0008: Lateral
Escalation Movement
Drive. User oA User 0.34 . User | Adm User
T1189: Drive-by —») T1059.003: Windows T1548.002: Bypass T1021.004: SSH
. —_>
Compromise User Command Shell User | User Account Control | Adm | User |
User | Adm
T1190: Exploit Public- LS“ T1053.005: Scheduled [Aa 0.12 | 11134: Access Token 0.43) 1021.01: Remote LYS"
; tae > . : -—>
Facing Application | User Task adm Manipulation | Adm | Desktop Protocol User |
User N/A 0.01 . ogo gs User 0.12 . User
T1078: Valid Accounts T1106 Native API T1068: Exploitation for T1534: Internal
| User | N/A Privilege Escalation ade Spearphishing N/A
```

## Slide 35

# Adaptive attack path reasoning for BAS

- § A Small Real-World Example - Key attack path

   - Target services are weblogic server, confluence server, spring framework, exchange server, RDP

   - Target operation systems are centos and windows server

Therefore, the TTP Reason Engine will only reason the attack path around above assets.

WAF CWPP
EDR
oracle:weblogic_server, TCP, 8000
atlassian:confluence_server, TCP, 8001 microsoft:exchange_server, TCP, 80
vmware:spring_framework , TCP, 8002BAS AGENT H1, centos 7 BAS AGENT H2, windows_server, 2016
172.16.1.101
10.202.198.11
IPS IPS
Internet DMZ Office
IDS IDS
DC with RDP opened, TCP 3389
BAS AEGNT H3, windows_server, 2016
10.202.198.12

#BHASIA @BlackHatEvents

## Slide 36

# Adaptive attack path reasoning for BAS

- § A Small Real-World Example - Key attack path

   - Defense-in-depth topology consists of IPS, IDS, WAF, CWPP, and EDR

Therefore, the TTP Reason Engine will only reason the attack path that these security products will generate detection data.

WAF CWPP
EDR
oracle:weblogic_server, TCP, 8000
atlassian:confluence_server, TCP, 8001 microsoft:exchange_server, TCP, 80
vmware:spring_framework , TCP, 8002BAS AGENT H1, centos 7 BAS AGENT H2, windows_server, 2016
172.16.1.101
10.202.198.11
IPS IPS
Internet DMZ Office
IDS IDS
DC with RDP opened, TCP 3389
BAS AEGNT H3, windows_server, 2016
#BHASIA @BlackHatEvents
10.202.198.12

## Slide 37

# Adaptive attack path reasoning for BAS

- § A Small Real-World Example - Key attack path

   - BAS AGENT H1, centos 7

      1. According to exposed _[oracle:weblogic_server]_ , _[atlassian:confluence_server]_ and _[vmware:spring_server]_ , selects corresponding vulnerability pcap playbooks.

#BHASIA @BlackHatEvents

## Slide 38

# Adaptive attack path reasoning for BAS

- § A Small Real-World Example - Key attack path

   - BAS AGENT H1, centos 7

      2. According to previous step simulation attack result: obtained _[User]_ permission, reason next TTP playbooks to attack _[Linux]_ , loop until Credential Access phase.

#BHASIA @BlackHatEvents

## Slide 39

# Adaptive attack path reasoning for BAS

##### § A Small Real-World Example - Key attack path

- BAS AGENT H1, centos 7

   3. Lateral Movement phase: based on previous step simulation attack result: owned _[User]_ permission of H1, and running service _[microsoft:exchange_server]_ on BAS AGENT H2.

WAF CWPP
EDR
oracle:weblogic_server, TCP, 8000
atlassian:confluence_server, TCP, 8001 microsoft:exchange_server, TCP, 80
vmware:spring_framework , TCP, 8002BAS AGENT H1, centos 7 BAS AGENT H2, windows_server, 2016
172.16.1.101
10.202.198.11
IPS IPS
Internet DMZ Office
IDS IDS
DC with RDP opened, TCP 3389
BAS AEGNT H3, windows_server, 2016
#BHASIA @BlackHatEvents
10.202.198.12

## Slide 40

# Adaptive attack path reasoning for BAS

- § A Small Real-World Example - Key attack path

   - BAS AGENT H2, windows server 2016

      1. According to exposed _[microsoft:exchange_server]_ , selects corresponding vulnerability pcap playbooks

#BHASIA @BlackHatEvents

## Slide 41

# Adaptive attack path reasoning for BAS

- § A Small Real-World Example - Key attack path

   - BAS AGENT H2, windows server 2016

2. According to previous step simulation attack result: obtained _[System]_ permission, reason next TTP playbooks to attack _[windows server 2016]_ , loop until Credential Access phase.

#BHASIA @BlackHatEvents

## Slide 42

# Adaptive attack path reasoning for BAS

##### § A Small Real-World Example - Key attack path

- BAS AGENT H2, windows server 2016

   3. Lateral Movement phase: based on previous step attack result: _[credential of H3 Administrator dump successfully]_ , running service on BAS AGENT H3 _[RDP]._

WAF CWPP
EDR
oracle:weblogic_server, TCP, 8000
atlassian:confluence_server, TCP, 8001 microsoft:exchange_server, TCP, 80
vmware:spring_framework , TCP, 8002BAS AGENT H1, centos 7 BAS AGENT H2, windows_server, 2016
172.16.1.101
10.202.198.11
IPS IPS
Internet DMZ Office
IDS IDS
DC with RDP opened, TCP 3389
BAS AEGNT H3, windows_server, 2016
#BHASIA @BlackHatEvents
10.202.198.12

## Slide 43

# Adaptive attack path reasoning for BAS

##### § A Small Real-World Example - Key attack path

- BAS AGENT H3, windows server 2016

   1. If successfully traversed to this server via RDP, reason next TTP playbooks to attack _[windows server 2016]_ in a loop until the end.

WAF CWPP
EDR
oracle:weblogic_server, TCP, 8000
atlassian:confluence_server, TCP, 8001 microsoft:exchange_server, TCP, 80
vmware:spring_framework , TCP, 8002BAS AGENT H1, centos 7 BAS AGENT H2, windows_server, 2016
172.16.1.101
10.202.198.11
IPS IPS
Internet DMZ Office
IDS IDS
DC with RDP opened, TCP 3389
BAS AEGNT H3, windows_server, 2016
#BHASIA @BlackHatEvents
10.202.198.12

## Slide 44

# Adaptive attack path reasoning for BAS

- § Technology Stack

   - Protégé, RDF/OWL, SPAQL

   - Jena with hybrid rule engine

ü based on the standard RETE algorithm, incrementally compute support

      - ü Logic Programming Engine with Tabling

- § Performance

   - JVM

      - ü Xms1024m, Xmx10240m

   - Average reason speed

      - ü 30s/step

#BHASIA @BlackHatEvents

## Slide 45

# Demo

#BHASIA @BlackHatEvents

## Slide 46

# The Tool

Live soon: https://github.com/Qihoo360/Luwak

#BHASIA @BlackHatEvents

## Slide 47

# BLACK HAT SOUND BYTES

- § Three key problems to improve the accuracy of TTP extraction helps defender keep up with the TTPs of attackers.

- § A practical approach for building TTP-oriented knowledge graph can help BAS reason more adaptive attack paths to assess the entire defense-indepth of the target organization.

#BHASIA @BlackHatEvents

## Companion resources

### `AS-23-Wu-When-Knowledge-Graph-Meets-TTPs-Highly-Automated-and-Adaptive-Executable-TTP-Intelligence-for-Security-Evaluation_tools.txt`

```text
https://github.com/qihoo360/luwak
```
