---
title: "A Manufacturer's Post-Shipment Approach to Fend-Off IoT Malware in Home Appliances"
speakers: ["Yuki Osawa", "Satoru Higuchi", "Satoshi Ito", "Manabu Nakano", "Takayuki Uchiyama"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/Yuki Osawa & Satoru Higuchi & Satoshi Ito & Manabu Nakano & Takayuki Uchiyama_A Manufacturer's Post-Shipment Approach to Fend-Off IoT Malware in Home Appliances.pdf"
pages: 37
sha256: "48bde4c7cdbf572edd76b27ac88eaf87d9f776f59f687fb96292d83fdcaea7e6"
text_chars: 14420
ocr_pages: 3
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:26:44Z"
---
# A Manufacturer's Post-Shipment Approach to Fend-Off IoT Malware in Home Appliances

**Speakers:** Yuki Osawa, Satoru Higuchi, Satoshi Ito, Manabu Nakano, Takayuki Uchiyama  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Yuki Osawa & Satoru Higuchi & Satoshi Ito & Manabu Nakano & Takayuki Uchiyama_A Manufacturer's Post-Shipment Approach to Fend-Off IoT Malware in Home Appliances.pdf` (37 pages)

## Slide 1

### A Manufacturer's Post-Shipment Approach to Fend-Off IoT Malware in Home Appliances

Speakers: Yuki Osawa and Satoru Higuchi

Contributors: Satoshi Ito, Manabu Nakano and Takayuki Uchiyama Email: astira@ml.jp.panasonic.com

Panasonic Holdings Corporation

#BHUSA @BlackHatEvents

## Slide 2

##### Agenda

- Background

- ASTIRA - Panasonic IoT Threat Intelligence -

- IoT-specialized self-protection module

- • Summary and further discussion

#BHUSA @BlackHatEvents

## Slide 3

##### Who are we

Yuki Osawa

Chief Engineer

Satoru Higuchi
Senior Engineer

Satoshi Ito
Staff Engineer

Manabu Nakano
General Manager

Takayuki Uchiyama
Manager

#BHUSA @BlackHatEvents

## Slide 4

##### Product security division that provides business support

Panasonic Holdings Corporation

Support for businesses

Operating Companies

#BHUSA @BlackHatEvents

https://holdings.panasonic/global/corporate/about/group-companies.html

## Slide 5

## Background

#BHUSA @BlackHatEvents

## Slide 6

##### Increase in attacks targeting IoT

Number of cyber attacks continue to increase

Sudden increase in attacks targeting IoT since 2021 About one-third of observed attacks targeting IoT

###### Number of Attacks Observed by NICTER Darknet Sensors

###### Breakdown of Observed Attacks by NICTER Darknet Sensors (2021, 2022)

No. Packets (100 million)

Attacks targeting IoT devices (Web Cameras, Routers, etc.)

Cybersecurity Research Institute - Cyber Security 2023 Appending 6 - Cyber Security Related Data - NICTER Observation Results https://www.nisc.go.jp/pdf/policy/kihon-s/cs2023.pdf

#BHUSA @BlackHatEvents

## Slide 7

##### Current state of IoT malware

- Attack cycles are becoming faster as IoT malware is in the wild within a few days after a vulnerability is disclosed

- Weaponization

2021/8/16 **2 days later** After 8/31 Vulnerability IoT malware in Malware captured by disclosed the wild ASTIRA

- Increasingly complex capabilities

   - Ransomware

   - Sophisticated techniques to avoid being detected

#BHUSA @BlackHatEvents

## Slide 8

##### Importance of product security after shipment

• Security activities that cover
Planning Design Implement Test On Market
the product lifecycle
Threat  Secure Secure Vulnerability Incident Response
• But attack methods  Analysis Design Coding Assessment
Shipment Disposal
continuously evolve
Product Security Measure Effectiveness
=> Product security measure
Drops Over Time
effectiveness drops over time
Security Strength

- Security updates mandated by standards such as ETSI EN303.645

https://www.etsi.org/deliver/etsi_en/303600_303699/303645/02.01.01_60/en_303645v020101p.pdf

#BHUSA @BlackHatEvents

## Slide 9

#BHUSA @BlackHatEvents

## Slide 10

##### What is ASTIRA?

**阿修羅 ASURA**

###### Project feature like…

In Buddhism having 3 heads, 6 eyes and 6 arms and BATTLE

Capturing and analyzing enormous amount of data day and night to FIGHT cyber threats

**TI**

Threat Intelligence

# **ASTIRA**

#BHUSA @BlackHatEvents

## Slide 11

##### Motivations for ASTIRA

Planning Design Implement Verify (Test) On Market
Threat  Secure Secure Vulnerability Incident Response
Analysis Design Coding Assessment
Shipment Disposal
Security Strength

- Activities along the product lifecycle, from threat analysis to incident response for over 15 years.

- ◆ Attackers continue to make progress. The security level of the product decreases relative to the level of the product after shipment.

- Aim to continuously improve each security activity in the product lifecycle.

#BHUSA @BlackHatEvents

## Slide 12

##### What does ASTIRA do?

**From Honeypots in both Physical and Cyber space**

Collect Data

Strengthen Organization

**From Insight to Strategy**

**To Quickly Alert Entire To Share Results Group**

**Intelligence Platform**

Analyze Threat

**Visualize**

Develop / Take Countermeasures **_BEFORE_** **shipment To Establish DevSecOps** **for** **_AFTER_** **shipment To Ensure Service Phase Security**

**for** **_BEFORE_** **shipment To Establish DevSecOps**

#BHUSA @BlackHatEvents

## Slide 13

##### Statistical summary of data collected over 5 years

- Panasonic IoT devices installed as honeypots

- IoT devices are intentionally „loosely” configured to make them vulnerable to attacks

- Automated collection, static and dynamic analysis of IoT malware

- Data collection also performed on products under development that have not been released to the market

###### **[Since November 2017]**

**Total Attacks 2,205,335,583** **Malware 109,276** **IoT Malware 32,015**

#BHUSA @BlackHatEvents

## Slide 14

##### MITRE ATT&CK analysis against some real devices

|**No**|**Tactics**|**Technique**|**Attacks**|**Cumulative relative frequency**|Percentages are rounded
|
|---|---|---|---|---|---|
|1|**Reconnaissance**|Active Scanning, Gather Victim Network Information, Gather
Victim Host Information, Gather Victim Identity Information|**208,487**|`攻撃進`
**80.50%**|`行度`
to 2 decimal places|
|2|**Initial Access**|Exploit Public-Facing Application, External Remote Services|**50,354**|**99.94%**||
|3|**Execution**|User Execution, Shared Modules|**19**|99.95%|**Collaborate with**
**business units for**|
|4|Persistence|-|0|99.95%|**risk feedback**|
|5|Privilege Escalation|-|0|99.95%||
|6|Defense Evasion|Indicator Removal on Host|6|99.95%||
|7|Credential Access|-|0|99.95%||
|8|Discovery|Network Share Discovery, File and Directory Discovery,
System Information Discovery|128|99.99%||
|9|Lateral Movement|-|0|99.99%||
|10|Collection|Data from Configuration Repository|4|100%|**No compromised**
|
|11|C&C|-|0|100%|**devices have been**
**observed so far**|
|12|Exfiltration|-|0|100%||

#BHUSA @BlackHatEvents

## Slide 15

##### Improve each phase of product lifecycle

Planning

Threat Analysis

Design

Secure Design

Implement

Secure Coding

Verify (Test)

Vulnerability Assessment

On Market

Incident Response

**Security testing Latest at development threat info phase**

**Risk Proactive incident response Assessment Periodic security testing after shipment Self-protection for device**

#BHUSA @BlackHatEvents

## Slide 16

##### Example of Product Lifecycle Enhancement Initiatives **<u>Periodic security testing after shipment</u>**

Are all these truly **highest priority** test items?

☑ Test A
☑ Test B
☑ Test C
☑ Test D
☑ Test E
☑ Test F
☑ Test G
☑ Test H
…

Product Functionality
×
Potential Risk Level
×
Recent attack trends

☑ Test E
Time-effective
☑ Test D
Cost-effective
Most
☑ Test A Security Test Plan
Important
☑ Test I
Tests
☑ Test K
☑ Test B
△  Test P Best
△  Test M Effort
… Tests

#BHUSA @BlackHatEvents

## Slide 17

## IoT-specialized self-protection module

#BHUSA @BlackHatEvents

## Slide 18

#### <u>THreat REsilience</u> & <u>Immunity Module</u>

for IoT device

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
€Q
black hat
USA 2025
1) THREIM
THreat REsilience & Immunity Module
THreat REsilience &
Immunity Module
for lol device
```

## Slide 19

##### Preventing a device from being taken over and abused

Cyber Kill Chain (The framework developed by Lockheed Martin: https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html)

01 02 03 04 05 06 07
Reconnaissance Weaponization Delivery Exploitation Installation C&C Actions on objectives

Cyber attack

#BHUSA @BlackHatEvents

## Slide 20

##### THREIM key features

- Built-in anti-malware with no required installation by a user

- Lightweight and minimum operational impact to an IoT product

- Linux based IoT device supported

- Capable to enhance device's security

   - Mitigation until firmware update is applied

IoT device
Device
protected
IoT device

#BHUSA @BlackHatEvents

## Slide 21

##### Strategy of how to evaluate THREIM’s performance

- Using all malware collected by ASTIRA

- Put malware inside IoT products and run it

Over 30,000 samples of IoT malware

Run IoT malware inside devices

#BHUSA @BlackHatEvents

## Slide 22

##### Evaluation flow

###### **LIST**

all malware based on CPU architecture

###### **PICK**

samples from clustered malware

###### **RUN**

malware on a device

**INITIALIZE** a device for next test

**STEP STEP STEP STEP STEP STEP STEP** 01 02 03 04 05 06 07 **CLUSTER TEST OBSERVE** samples in if malware malware detected each CPU arch. runs on a and stopped device or not group

#BHUSA @BlackHatEvents

## Slide 23

##### Clustering and sampling of malware for efficiency

###### **01**

###### More than 30,000 IoT malware collected

Classification result
03
e.g. ARM: 1,804 groups

Group 1803
Group 1
Group 2 Group 1804

###### **02** Similar malware are classified into the same group

Port_scan() Group 1
TCP_DDoS()
DlinkCMDInjection()
DlinkBoF()
…
SSH_login() Group 2
SSDP_DDoS()
EternalBlue()
SambaCry()
…

04 Pick a sample from each group

Group 3
Group 1
Group 2 Group 4

#BHUSA @BlackHatEvents

## Slide 24

##### Environment setup

- IoT devices in an isolated network

   - To avoid unnecessary trouble with development environment

- Virtual environment with the Internet

   - For additional evaluation because most malware connect to a C&C via the Internet

The Internet

C&C

Virtual env. (QEMU)

Evaluation on real devices Isolated network

Additional evaluation on virtual env. With the Internet

#BHUSA @BlackHatEvents

## Slide 25

##### Evaluation results

- Maximum 86.1% of samples detected

- About half of samples ran on a device and the other half failed to run

- No big impact on resource consumption of device

|**Product**|**CPU**|**Detection**
**rate**|**Malware ran**
**on device**|**Malware**
**tested (total)**|**CPU usage**
**increased**|**Mem usage**
**increased**|
|---|---|---|---|---|---|---|
|Device A|ARM|**86.1%**|275|1804|+0.3%|+0.9%|
|Device B|ARM|57.7%|759|1804|+3.2%|+0.1%|
|Device C|MIPS|66.1%|348|689|+5%|+0.7%|
|Device D|AMD64|59.5%|742|1102|+2.1%|+0.1%|

Notes: Excluded cases that a C2 server was not alive from detection rate calculation.

CPU and Memory usage compared between when THREIM was enabled and disabled.

#BHUSA @BlackHatEvents

## Slide 26

**The project achievements were made possible with the steady collaboration by the business units**

#BHUSA @BlackHatEvents

## Slide 27

##### Developers from business unit must be involved

- IoT device is specially customized for each product

   - Unique knowledge is necessary to understand inside, even though Linux-based system

- Functions such as login shell is removed from products on market to prevent abuse

   - We cannot independently install THREIM or run malware inside a device

- Product's functionality is most important, which must not be interrupted

   - Showing TV program, playing music and video, refrigerate, air conditioning, etc.

   - Need to understand how these functionalities are implemented to keep them running properly

#BHUSA @BlackHatEvents

## Slide 28

##### Key to successful collaboration 1/2

- The first step is the business unit gain an understanding on the importance of product security

   - Because security such as anti-malware is not popular in IoT devices yet

Attacks Experience
Real-time attack visualization in
ASTIRA showroom for them
Highlighting
importance of
security
Their own product
as a matter for
Analysis report for their own
the business unit
product as a honeypot
itself

#BHUSA @BlackHatEvents

## Slide 29

##### Key to successful collaboration 2/2

- Trust relationship before engaging and during the collaboration

Building trust
with developers
in business unit

Finding key person
Tech lead who understands
product security

Past work experiences
Having been working together in
the past makes strong trust

**Developers’ workload** Minimum requests (e.g. providing SDK) to reduce their workload

#BHUSA @BlackHatEvents

## Slide 30

##### Why manufacturer implements by itself?

###### **Enabled upon powering on**

- Self-protection in products need to be implemented in a product before its shipment

###### **Highly trusted partner for BU**

- May need to share products’ confidential information and know-how - Prefer not to pay license fee outside the company

- **Controlled by ourselves**

- - Achieving perfect security is not necessarily the correct answer - Need to consider suitable security levels for both industry and our own business

#BHUSA @BlackHatEvents

## Slide 31

## Summary and further discussion

#BHUSA @BlackHatEvents

## Slide 32

##### What’s “reasonable” security?

All of us already understand the importance of product security

On the other hand, however, nobody can ensure “perfect” security...

Will there be “reasonable” security for IoT products required in the future?

#BHUSA @BlackHatEvents

## Slide 33

##### “Reasonable” from the point of view of stakeholders

**Manufacturers**

- Comply with laws / Certified to standards

- Reduce the risks caused by vulnerabilities

- Accountable explanations to users

**Users**

   - A product can be used without concern

   - Minimal user effort required

- Cost of product security

**Governments / Auditors**

- Establish laws and enforce compliance

- Compliance testing by audit agencies

**Researchers / Academia**

- Protected against all potential threats in theory (Cost-effectiveness and feasibility may not be a consideration)

#BHUSA @BlackHatEvents

## Slide 34

##### Industry requirements

**e.g. ETSI EN 303 645**

**Home Entertainment**

**Consumer products**

**Kitchen appliance**

**Air conditioning**

**Requirements vary by industry**

**Automotive Financial Energy**

Business
products and
solutions

**… etc.**

**… etc.**

#BHUSA @BlackHatEvents

## Slide 35

##### Could self-protection be a “reasonable” option?

Planning

Threat Analysis

Design Implement Verify (Test) Secure Secure Vulnerability Incident Response Design Coding Assessment <u>Shipment</u>

Design

On Market

~~Mitigating t~~ he loss of strength by self-protection

**1**<sup>**st**</sup> **Priority**

**2**<sup>**nd**</sup> **Priority**

Firmware update is the best option

Self-protection as a “reasonable” option

… but not always possible

#BHUSA @BlackHatEvents

## Slide 36

##### Takeaways

- Efforts to continuously improve product security are required for manufacturers

   - Incorporating threat data and its analysis into phases of product lifecycles

   - Self-protection capability of IoT device is proposed to reduce risks after product shipment

- Insights on why and how manufacturers can improve their product security

   - Key is collaboration effort between product security division and business units

   - Carefully consider and control their product security levels

- Potential ideas for industry to better define “reasonable” product security

   - Self-protection as an example for consumer products from manufacturer’s perspective

   - But still need further discussion in each industry

#BHUSA @BlackHatEvents

## Slide 37

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
€Q
black hat
USA 2025
AS“ RA CR) THREIM
THreat REsilience & Immunity Module
```
