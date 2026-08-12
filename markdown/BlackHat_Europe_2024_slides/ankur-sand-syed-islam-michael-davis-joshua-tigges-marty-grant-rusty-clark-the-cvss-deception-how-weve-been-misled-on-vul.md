---
title: "The CVSS Deception How We've Been Misled on Vulnerability Severity"
speakers: ["Ankur Sand", "Syed Islam", "Michael Davis", "Joshua Tigges", "Marty Grant", "Rusty Clark"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2024"
edition: "Europe"
year: 2024
source_pdf: "BlackHat_Europe_2024_slides/Ankur Sand & Syed Islam & Michael Davis & Joshua Tigges & Marty Grant & Rusty Clark_The CVSS Deception How We've Been Misled on Vulnerability Severity.pdf"
pages: 46
sha256: "cfa3020fbcccccef115459325ec53da8080d9991c81c0552939dff231c215cbd"
text_chars: 21076
ocr_pages: 4
has_ocr: true
redacted_secrets: 0
ocr_confidence: 84.7
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:54:20Z"
---
# The CVSS Deception How We've Been Misled on Vulnerability Severity

**Speakers:** Ankur Sand, Syed Islam, Michael Davis, Joshua Tigges, Marty Grant, Rusty Clark  
**Conference:** Black Hat Europe 2024  
**Source:** `BlackHat_Europe_2024_slides/Ankur Sand & Syed Islam & Michael Davis & Joshua Tigges & Marty Grant & Rusty Clark_The CVSS Deception How We've Been Misled on Vulnerability Severity.pdf` (46 pages)


## Slide 1

# The CVSS Deception: How We've Been Misled on Vulnerability Severity

Speaker(s):

Syed Islam & Ankur Sand

#BHEU @BlackHatEvents

## Slide 2

## **Agenda: Details**

## **Agenda**

- Introduction

- Vulnerability Management & CVSS

- Six Challenges in CVSS Utilization

   - Recom mendati ons & G ui dance

- Future Directions

- Key Takeaways

2

#BHEU @BlackHatEvents

## Slide 3

## **Who We Are**

## Syed Islam

## Ankur Sand

**P r i n c i p a l C y b e r s e c u r i t y A r c h i t e c t**

**V i c e P r e s i d e n t - C y b e r s e c u r i t y**

**C y b e r s e c u r i t y a n d Te c h n o l o g y C o n t r o l s**

**O p e r a t i o n s C e n t e r**

<u>h t t p s : / / s y e d - i s l a m . g i t h u b . i o /</u>

**( V u l n e r a b i l i t y M a n a g e m e n t R e s p o n s e )**

**<u>h t t p s : / / w w w . l i n k e d i n . c o m / i n / a n k u r</u> -** **<u>s</u> -** **<u>1 4 3 2 3 a 8 /</u>**

#BHEU @BlackHatEvents

## Slide 4

**Vulnerability Management & Common Vulnerability Scoring System (CVSS)**

#BHEU @BlackHatEvents

## Slide 5

## **Vulnerability Management & CVSS -CVE Lifecycle & Impact**

**Vulnerability Lifecycle  and  CVSS for Severity Assessment**

**Lifecycle of a Vulnerability**

**Role of CVSS in Vulnerability  Assessment**

Standardized Risk
Assessment
Patching
Request  Vulnerability
New  For Management
Vulnerability CVE-ID Prioritization Prioritization of
Discovery Remediation
Efforts
Consistent
Stakeholder
CVSS
Communication

_<u>https://www.wallarm.com/what/common-vulnerabilities-and-exposures-cve</u>_

#BHEU @BlackHatEvents

## Slide 6

## **Vulnerability Management & CVSS -Details**

**CVSS 3.0/ 3.1 Metrics and Severity Scale**

CVSS Scoring Metrics Details

CVSS Severity Levels
Rating  CVSS Score
None  0.0
Low  0.1 - 3.9
Medium  4.0 - 6.9
High  7.0 - 8.9
Critical 9.0 - 10.0

_Source:_ _<u>https://www.first.org/cvss/v3.1/specification-document</u>_

#BHEU @BlackHatEvents

## Slide 7

## **Vulnerability Management & CVSS -Trends**

## **Vulnerability Disclosure Trends**

Annual CVE disclosures rate trending up by **~20% 18%** of CVEs rated **critical** (CVSS score of 9+).

Most common vulnerability types:

- Denial of Service - 32%

- Code Execution - 28%

Vulnerability Release Velocity by Year
2014 34007
2015 29066
2016
25084
2017
2018
2019
14643 16510 17305 18323 20153
2020
2021
7928
2022 6494 6449
2023
2024
Vulnerability Distribution by CVSS Score
60000
48807
50000
40000 33185 32469 35646
30000 24056
20000 15919
10000
2925 145 1034 2464
0
0-1 1-2 2-3 3-4 4-5 5-6 6-7 7-8 8-9 9+

_Source:_ _<u>https://www.cvedetails.com/</u>_

#### **Vulnerability Distribution by Vulnerability Type**

#BHEU @BlackHatEvents

## Slide 8

Operational Challenges with CVSS

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Operational Challenges with CVSS
```

## Slide 9

## **Operational Roadblocks in CVSS -Challenges**

CVSS Adoptions-Operational Challenges  with CVSS 3.0/3.1
3- Missing
1- Impact  5- Disconnect in
Dependency
Aggregation  APT &
Considerations
Pitfalls
Exploitability
Detection
Together We
Tactical
Dynamics: Key
Rise: Challenges
Patterns to  Sparks: Instant
Demand Unity
watch for Impact
2- CVSS Score  4- Exploit Code
6- Overlooked
Alignment  Maturity
Privacy Aspect
Issues Overhead
#BHEU @BlackHatEvents

## Slide 10

1- Aggregation
Pitfalls
Detection
Dynamics: Key
Patterns to
Watch For (Inability to express Vulnerability Severity
using aggregation of CIA Metrics )
#BHEU @BlackHatEvents

## Slide 11

## **1 -Aggregation  Pitfalls -Issue Details**

CVSS -CIA Triad and Rating Scale with Numerical Weight
CVSS impact metrics give equal
weight to Confidentiality, Integrity,
and Availability, overlooking the
unique risk priorities of
C
organizations and the true impact a
Confidentiality
vulnerability might have.
C,I,A Impact- Metrics
and Numerical Values
CVSS Base  High 0.56
Impact Metrics Low 0.22
I A None 0
Integrity Availability

#BHEU @BlackHatEvents

## Slide 12

## **1 -Aggregation  Pitfalls -Issue Details**

**CIA Triad and CVSS Outcome (When One Value as High others as None)**

8.6
(High)
C,I,A Impact- Metrics
and Numerical Values
C
High 0.56
Confidentiality
Low 0.22 7.5
(High)
(High)
None 0
CVSS Base
Impact Metrics
I A 3.4
(Low)
Integrity Availability
(None)  (None)

#BHEU @BlackHatEvents

## Slide 13

## **1 -Aggregation  Pitfalls –Case Study**

**Case Study-Real-World Examples showing Unauthorized DDos attack against Critical Business Services**

_Source:_ _<u>https://tvcidade10.com.br/wp-content/uploads/2023/02/691913fc-d045-4d17-b804-4145d5f3a42d.jpg</u>_

## **_Use case:_**

During the COVID-19 pandemic, CVE-2020-8187, a Citrix NetScaler DDoS vulnerability, was released and can be responsible for disrupting critical business applications that support remote work.

**Exploitation Details** : The attack is straightforward, requiring no user interaction or elevated privileges, and can be executed remotely.

**Impact** : Severe Business continuity Risk

**CVSS Rating High**

#BHEU @BlackHatEvents

## Slide 14

## **1-Aggregation  Pitfalls -Statistics & Impact**

**Exposure and Impact Radius Covering Last Eight Years**

Published CVEs that have _High_ impact on only _one_ Impact Metric and no impact on others.

Ineffective
Resource
Allocation
CIA
Aggregation
Pitfalls
Long-term  Creates False
Risk  Sense Of
Exposure Security

#BHEU @BlackHatEvents

## Slide 15

## **1-Aggregation  Pitfalls –Detection Patterns**

**Recognizing Current Challenges and Providing Strategic Recommendations**

Confidentiality: High (C:H)
Integrity: None (I:N)
Availability: None (A:N)
Detection
Dynamics: Key
Patterns to
Watch For CVSS Base
Impact Metrics
Patterns
Confidentiality: None (C:N)
Confidentiality: None (C:N)
Integrity: None (I:N)
Integrity: High (I:H)
Availability: High (A:H)
Availability: None (A:N)

## **Challenge Awareness:**

- Aggregation of CIA impact metrics can **underrate** vulnerabilities that severely affect only one attribute, potentially delaying remediation efforts.

- **High volumes** of vulnerabilities lead organizations to prioritize by severity, risking prolonged risk exposures.

## **Recommendations:**

- Develop capabilities to **incorporate CVSS vectors with a single CIA element rated as High and others as None** into vulnerability assessments, focusing on public-facing assets that support critical business services.

#BHEU @BlackHatEvents

## Slide 16

2- CVSS Score
Alignment Issues
Detection
Dynamics: Key
Patterns to
Watch For
#BHEU @BlackHatEvents


> Recovered by OCR — confidence 84/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
AYN MAN
7 2- CVSS Score
Alignment ore |
Detection
Dynamics: Key
Patterns to
Watch For
```

## Slide 17

## **2 -CVSS Score Alignment Issues -Details**

## **CVSS Score Alignment Issues**

- **Scoring Discrepancy:** A rounding error in CVSS 3.0/ 3.1 causes a slight difference between Base and Environmental scores.

- **Input Vector Impact:** The specific input vector results in a Base score of 9.0 and an Environmental score of 9.1.

- **Framework Inconsistency:** Although the difference is minor (0.1 or 1%), it highlights a potential inconsistency within the CVSS framework.

#BHEU @BlackHatEvents

## Slide 18

## **2 -CVSS Score Alignment Issues -Case Study**

**Case Study-Real-World Examples showing CVSS Score Alignment Issue**

Detection Dynamics: Key Patterns to Watch For _Source:_ _<u>https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator</u>_

#BHEU @BlackHatEvents

## Slide 19

## **2 -CVSS Score Alignment Issues -Statistics & Impact**

## **CVEs with Mismatch Condition**

Published CVEs that have _Base and Environmental Metric Mismatch_

SLA
Implications
Score
Misalignment
Issues
Tool and  Risk
Automation  Assessment
Challenges Variability

#BHEU @BlackHatEvents

## Slide 20

## **2 -CVSS Score Alignment Issues -Detection Patterns**

**Recognizing Current Challenges and Providing Strategic Recommendations**

## **Challenge Awareness:**

- **Scoring Discrepancy:** A rounding error in CVSS 3.0/ 3.1 causes a slight difference between Base and Environmental scores.

- **Under Prioritization of Vulnerability:** The inconsistency in scoring can lead to lower prioritization if the it matches boundary condition

## **Recommendation:**

- Develop capabilities to **identify pattern** AV:N/AC:L/PR:L/UI:R/S:C/C:H/I:H/A:H) and incorporate it into vulnerability assessments.

- Acknowledge and document as minor CVSS score discrepancy to ensures compliance and doesn’t require any immediate actions.

#BHEU @BlackHatEvents

## Slide 21

3- Missing
Dependency
Tactical
Considerations
Sparks: Instant
Impact
#BHEU @BlackHatEvents

## Slide 22

## **3 -Missing Dependency Considerations -Issue Details**

**Pre-Requisite/Dependency and Vulnerability Exploitation**

- **Network and Access Controls:** Configuration and Access Controls can significantly affect an attacker's ability to exploit a vulnerability

- **Configuration and Dependencies:** Exploits sometimes require specific setup or other software vulnerabilities

- **User Privileges:** Influence severity and potential impact

#BHEU @BlackHatEvents

## Slide 23

## **3 -Missing Dependency Considerations –Case Study**

**Case Study-Real-World Examples showing Missing Dependency Considerations**

**CVE-2023-4966 (Vendor Severity- Critical)**

Must Be Configured as Gateway (VPN virtual server, ICA Proxy, CVPN, RDP Proxy) OR AAA virtual server

Malicious Threat  Actor

Mission Accomplished

CVE- 2023-4966, a sensitive information disclosure vulnerability that allows an attacker to read large amounts of memory after the end of a buffer. Notably, that memory includes session tokens, which permits an attacker to impersonate another authenticated user

_Source:_ _<u>https://support.citrix.com/s/article/CTX579459-netscaler-adc-and-netscaler-gateway-security-bulletin-for-cve20234966-and-cve20234967?language=en_US</u>_

#BHEU @BlackHatEvents

## Slide 24

## **3-Missing Dependency Considerations -Statistics & Impact**

## **Exposure and Impact Radius**

Published CVEs _with indicated Dependency / Environmental Requirements_

SLA
Implications
Missing
Dependency
Consideration
Ineffective  Risk
Resource  Assessment
Allocation Variability

#BHEU @BlackHatEvents

## Slide 25

## **3 -Missing Dependency Considerations –Detection**

**Recognizing Current Challenges and Providing Strategic Recommendations**

## **Challenge Awareness:**

- Lack of Pre-Requisite Environmental Considerations in CVSS.

- Approximately **11%** of vulnerabilities hold environmental dependencies

- Organizations struggle to prioritize vulnerabilities accurately, and continuous review against environmental changes adds complexity.

## **Recommendation:**

- Develop capabilities to **identify prerequisite** keywords ("when," "should," and "configured") and incorporate them into vulnerability assessments. With the progress in the LLM space we can now do this even better.

#BHEU @BlackHatEvents

## Slide 26

4- Exploit Code
Maturity
Tactical
Overhead
Sparks: Instant
Impact
#BHEU @BlackHatEvents

## Slide 27

## **4 -Exploit Code Maturity Overhead-Challenge Details**

Exploit Code Maturity Metric Values
Numerical Value
= 1
Numerical Value
= 1 Numerical Value
01 02 03 = 0.97
Not Defined High Functional
(X) (H) (F)
Numerical Value 04 05
= 0.94 Numerical Value
= 0.91
Proof-of- Unproven
Concept (U)
(P)

#BHEU @BlackHatEvents

## Slide 28

## **4 -Exploit Code Maturity Overhead-Challenge Details**

Exploit Code Maturity Metric Monitoring Challenges
• Scattered Sources
• Data Accuracy
• Fragmentation Issue
Requirement
• Incomplete Lifecycle
• Lack of Comprehensive
Coverage 01 02
Sources
Fragmented  Lack of
• Insufficient Detail
Information  Comprehensive
Sources Data
03 04
Rapid and  Extensive Data
• Rapid  Exploit Development
Dynamic  Parsing
• Vast Data Volume:
• Data Source Limitations Evolution Requirements
• Point-in-Time Accuracy
• Outdated Information
• Continuous Intelligence
Challenge

**No official CVSS guidance on appropriate monitoring sources or recommended monitoring frequency.**

#BHEU @BlackHatEvents

## Slide 29

## **4 -Exploit Code Maturity  Overhead –Case Study**

**Exploit Maturity Journey  for CVE-2023-34362 Progress MOVEitTransfer SQL Injection Vulnerability**

2500+ exposed
customer including the
BBC, British Airways
and Boots.
Progress Software  Identified as CVE- No exploit code is  Proof-of- Ongoing
warned the public  2023-34362 on  available, or an  concepts were  monitoring
about a critical  June 2 exploit is  getting avalaible    revealed further
SQL injection  theoretical  within the public  fluctuations in
vulnerability in  CVSS  forums CVSS scores,
MOVEit Transfer,  Score=9.8 E=U CVSS  necessitating
allowing
Score=9.3 continuous
unauthorised
CVSS  reassessment by
access to its
E=X E=P
database Score=9.0 security teams.
June 13, 2023
31-Jan-24 June 2, 2023 June 3, 2023 June 12, 2023
Onwards
#BHEU @BlackHatEvents
Source: https://www.rapid7.com/blog/post/2023/06/14/etr-cve-2023-34362-moveit-vulnerability-timeline-of-events/ and  https://unit42.paloaltonetworks.com/threat-brief-moveit-cve-2023-34362/

#BHEU @BlackHatEvents

## Slide 30

## **4 -Exploit Code Maturity  Overhead -Statistics & Impact**

## **Exposure and Impact Radius**

MITRE CVE Reference Map
for Source EXPLOIT-DB
shows 12,291 unique CVEs
with 10,719 Exploit DB
references
Potentially 462,728  SLA
reference data points
that need parsing and  Explo i t Code  RAPID7 Vulnerability  Implications
analysis to determine  Maturity (E)  Exploit Database
exploit code maturity Metric  Contains details for over
Overhead 180,000 vulnerabilities
Exploit Code
with 4,000 listed
exploits. Maturity
Adoption
Vulners Database Contains  Impact
255,718 records referring to  Resource- Inaccurate
exploits. Intensive  Urgency
Monitoring Assessment

#BHEU @BlackHatEvents

## Slide 31

## **4 -Exploit Code Maturity  Overhead -Recommendation**

**Recognizing Current Challenges and Providing Strategic Recommendations**

## **Challenge Awareness:**

- Lack of an authoritative source for exploit code maturity journey.

- Ever-growing volume of disparate data that requires regular analysis.

- Incorrect or incomplete data could lead to reduced scores and severity ratings.

## **Recommendation:**

- Avoid using the Exploit Code Maturity Metric of the CVSS 3.0/3.1 framework due to the lack of a validated and reliable data source – avoiding artificial lowering of score.

#BHEU @BlackHatEvents

## Slide 32

5- Disconnect in
APT &
Together We
Rise: Challenges
Exploitability
Demand Unity

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 81/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
~ 5- Disconnect i in|
Together We
Exploitability Rise: Challenges
a x Demand Unity
```

## Slide 33

## **5 -Disconnect in APT and Exploitability - Issue Details**

**Advanced Persistent Threat (APT) and CVSS**

- **APTs (Advanced Persistent Threats):** sophisticated threats to digital security, often evading traditional security measures.

- **Global Presence** : Over 200 APTs exist globally, including those backed by nation-states and eCriminals.

- **Exploitation of Vulnerabilities** : APTs exploit known vulnerabilities, highlighting the necessity of understanding these threats for effective cybersecurity.

_Source:_ _<u>https://www.forenova.com/blog/deep-dive-into-advanced-persistent-threats</u>_

#BHEU @BlackHatEvents

## Slide 34

## **5 -Disconnect in APT and Exploitability - Case Study**

**Advanced Persistent Threat (APT) and Known CVE Associations**

_Source:  https://vulncheck.com/blog/how-we-think-about-threat-actors_

#BHEU @BlackHatEvents

## Slide 35

## **5 -Disconnect in APT and Exploitability-Statistics & Impact**

**Exposure and Impact Radius**

No single source links vulnerabilities to specific
threat actors, limiting threat understanding.
MITRE ATT&CK Framework:
Ineffective
Lists 159 APT groups and their
associated Tactics,  Threat
Techniques, and Procedures
Prioritization
(TTPs) but doesn’t include CVE
association
Exploit Prediction Scoring
Disconnect in
System (EPSS):  Provides
APT and
exploitability scores for  CISA Known Exploited
239,671 CVEs, indicating  Vulnerabilities (KEV) Catalog:  Lists  Exploitability
the likelihood of  1217 vulnerabilities used in  Impact
Ineffective  Increased
exploitation but lacking  significant attacks but does not
specificity about the  attribute these to specific  Resource  Risk
exploiters. attackers.
Allocation Exposure

#BHEU @BlackHatEvents

## Slide 36

## **5 -Disconnect in APT and Exploitability- Recommendation**

**Recognizing Current Challenges and Providing Strategic Recommendations**

## **Challenge Acknowledgement:**

- APTs often exploit known CVEs, highlighting the need for effective vulnerability management.

- There is no single source of truth for CVE association to APTs within the industry.

- Lack of APT-Specific considerations in CVSS

## **Recommendation:**

- We invite industry to unite in forming solutions for monitoring APT activities and TTPs, **prioritizing vulnerabilities linked to actively exploited CVEs** by incorporation into the CVSS framework.

#BHEU @BlackHatEvents

## Slide 37

6- Overlooked
Privacy
Together We
Rise: Challenges
Aspect
Demand Unity

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
7. 6- Overlooked “
Privacy
Together We
Aspect Rise: Challenges
| | Demand Unity
```

## Slide 38

## **6 -Overlooked Privacy Aspect –Issue Details**

## **Security, Privacy  and CVSS**

## **Security vs. Privacy**

- **Security** : Protects data from unauthorized access and ensures integrity and availability.

- **Privacy** : Protects personal information and controls data sharing with consent.

## **CVSS and Privacy**

- CVSS focuses on exploitability and impacts on confidentiality but neglects privacy implications.

- Privacy is not explicitly included in CVSS scoring.

#BHEU @BlackHatEvents

## Slide 39

## **6 -Overlooked Privacy Aspect-Case Study**

**Case Study-Real-World Examples showing Privacy risk with underrepresented CVSS Score**

_Source:_ _<u>https://www.kolide.com/blog/zoom-webcam-hijacking-are-your-users-vulnerable</u> *https://www.demandsage.com/zoom-statistics/_

- **_Use case:_** _Information Disclosure (Webcam) —CVE2019–13450 vulnerability against zoom clients._

- **_Zoom has 300 million daily active users as of 2024*._**

- **Exploitation Details** : This vulnerability allows any website to forcibly join a user to a Zoom call, with their video camera activated, without the user’s permission.

**Impact:** Cause privacy **CVSS Rating** violations, security risks, **Medium** potential legal and reputational consequences.

#BHEU @BlackHatEvents

## Slide 40

## **6 -Overlooked Privacy Aspect -Statistics & Impact**

## **Exposure and Impact Radius**

CVEs with Confidentiality Impact vs _Privacy Impact_

Overlooked
Privacy
Obstacle
Unrecognized
Privacy Impact
Regulatory
Privacy
Compliance
Breaches
Challenges

#BHEU @BlackHatEvents

## Slide 41

## **6-Overlooked Privacy Aspect -Recommendation**

**Recognizing Current Challenges and Providing Strategic Recommendations**

## **Challenge Acknowledgement:**

- Blurring of privacy and security boundaries.

- CVSS emphasizes exploitability and confidentiality but overlooks severe privacy implications.

- Nuanced vulnerability assessment needed for privacy-sensitive sectors.

## **Recommendation:**

- Develop **privacy-specific metrics** for assessing vulnerabilities

- Integrate privacy considerations into vulnerability management

- Adopt and leverage privacy frameworks

#BHEU @BlackHatEvents

## Slide 42

Moving Past CVSS 3.1

#BHEU @BlackHatEvents

## Slide 43

## **Future Directions : CVSS V4.0 Details**

**Does CVSS v4 address these Challenges?**

- **Enhancements in Metrics:** CVSS 4.0 introduces expanded impact metrics,  refined temporal metrics and new supplemental metrics to improve assessment accuracy.

- **Adoption Trends:** CVSS 4.0 is yet to be fully adopted by security vendors and the NVD, but trends indicate growing interest.

- **Our Initial Review:** Review of the CVSS v4 documentation provided by FIRST, indicates that our operational challenges, such as the lack of privacy considerations and APT associations, persist. Further empirical data and practical implementation guidance will be crucial for necessary validation.

_Source:_ _<u>https://tuxcare.com/blog/the-transition-to-cvss-v4-0-what-you-need-to-know/</u>_

#BHEU @BlackHatEvents

## Slide 44

## **Future Directions : Proposed Extension Metrics**

## **Towards a Solution –what do we need in the framework?**

Metric Category   Metric Name   Parameters with desired contribution in overall scoring
Threat  APT Associations [AP] Yes No Not Defined
Intelligence
Environmental  Not met  Met  Not Defined
Dependency
[ED]
Operating
Environment
Yes  No  Not Defined
al Context Privacy Impact
[PI]
Critical Business
Yes  No  Not Defined
Services Impact
[CB]
Increase  Score Decrease Score No Impact
#BHEU @BlackHatEvents

## Slide 45

Key
Takeaways

#BHEU @BlackHatEvents

## Slide 46

## **Key Takeaways and Q&A**

## **Key Takeaways**

### **Detection Dynamics: Key Patterns**

For Challenges 1 and 2 - Essential Patterns are provided for Monitoring and Strategic Implementation recommended for CVSS v3.0/3.1 users.

### **Together We Rise: Challenges Demand Unity**

Challenges 5 and 6 - Substantial and require industry collaboration and effort to resolve, we are actively seeking opportunities for partnership and cooperation.

### **Tactical Sparks: Instant Impact**

For Challenges 3 and 4 – Initial ideas for Immediate Impact are provided for Monitoring and Strategic Implementation recommended for CVSS v3.0/3.1 users.

### **Towards the Future**

We have outlined additional metrics for consideration, including Threat Intelligence and Operating Environmental Context with Environmental Dependency, Privacy Impact, and Critical Business Services Impact.

#BHEU @BlackHatEvents
