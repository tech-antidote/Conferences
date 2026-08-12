---
title: "Modern Kill Chains Real World SaaS Attacks and Mitigation Strategies"
speakers: ["Cory Michal", "Brandon Levene", "Ben Pruce"]
conference: "Black Hat"
conference_full: "Black Hat USA 2024"
edition: "USA"
year: 2024
source_pdf: "Black Hat USA 2024 slides/Cory Michal & Brandon Levene & Ben Pruce_Modern Kill Chains Real World SaaS Attacks and Mitigation Strategies.pdf"
pages: 29
sha256: "ade4e024a6daa0afeb88ed82636f62af7a0a62eeed4dd644bcb478a272533398"
text_chars: 12966
ocr_pages: 9
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:29:31Z"
---
# Modern Kill Chains Real World SaaS Attacks and Mitigation Strategies

**Speakers:** Cory Michal, Brandon Levene, Ben Pruce  
**Conference:** Black Hat USA 2024  
**Source:** `Black Hat USA 2024 slides/Cory Michal & Brandon Levene & Ben Pruce_Modern Kill Chains Real World SaaS Attacks and Mitigation Strategies.pdf` (29 pages)

## Slide 1

**Modern Kill Chains** Real World SaaS Attacks and Mitigation Strategies

**Cory Michal Brandon Levene** VP of Security Principal Product Manager, Threat Detection

**Ben Pruce** Lead Threat Detection Engineer

August 7, 2024

1

## Slide 2

## **Agenda**

- Reflect on where we are currently

- Hypothesize why we are here

- Examine what it is like to be here

- Determine if something better is possible

- Outline how we could move to better state

2

## Slide 3

## **Historical Attack Surface Change**

3

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Historical Attack Surface Change
Marriot Breach
Heartbleed Ticketmaster Breach
Sony Breach T-Mobile Breach Log4Shell
Home Depot Capital One Data Okta
OPM, Anthem First American MS Exchange
Ashley Madison Solarwinds Breach —LastPass_ Change HC
TJX Breach Yahoo Breach Magellan Health MOVEit Breach Ransom
‘Storm Worm Stuxnet DNC Breach Ransom MGM Ransom UK MOD
Web Hacks Estonia & Russia PSN Breach DropBox Breach Colonial Pipe Ransom Royal Mail Midnight Bliz
AOHell Back Orifice SQL Slammer & Zeus Trojan RSA Breach WannaCry Kaseya Ransom Ransom Snowflake
Social Eng ILOVEYOU Blaster worm Conficker Worm Target Breach Petya
Morris Worm First DDoS Nimda worm My Doom Worm HBS Breach Yahoo Breach Equifax Breach 6 6
Michelangelo Bad IE Bugs Code Red Worm Samy XSS worm Aurora Snowden é é é
Virus Phishing é a é
wa FWD
piel — wee ne “ see | ano | ame | zou | coor | anon | ano | ane | zou | aoe | cow | azo | ame | 2m
Surface ; : |
On Prem / Remote On Prem / On Prem / Remote / On Prem / Remote++
Remote / laaS laaS | PaaS / SaaS laaS++ / PaaSt++ |
SaaS++
Control Perimeter Security Defense In Depth Zero Trust
Strategy
1990
&
Stack =
<S) mT = aly B
Vor Y GQ a a)!
Pi
First Firewalls Patching IP Chains Trustworth Computing PCI DSS NextGen FW Google Beyond Corp += MSFT Zero Trust. CSPM Al Mania
and AntiVirus Satan Scanner Windows Update Vulnerability Scanning Endpoint Next Gen EDR Threat Intel CASB SASE: zero Triste
VPNs IDS Windows XP Firewall Protection MFA TLS Everywhere ZT Implementations MFA++
AppSec IPS DLP Network Behavior EDR SPM
WAFS SIEM Analysis SOAR XDR
SDLC
Shift Left
```

## Slide 4

## **Pre Cloud & SaaS Attack Surface ~ 2009**

DMZ DMZ

4

## Slide 5

## **Modern Attack Surface ~ 2020**

5

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Modern Attack Surface ~ 2020
A
EI Et
EI Et
HIoAoeo
El
LIES ELOISE
| |
i
Tisai
Tn
Tn
CED aD
CED aD
```

## Slide 6

## **Attack Surface Observations**

##### **Legacy Attack Surface**

##### **Modern Attack Surface**

- Hardened network perimeters

   - Rapidly dissolving perimeters

- VPN access

   - Access from work or BYOD

- Physical access controls

   - Remote access from anywhere

- Network Access Control / Wifi

   - Uncontrolled network upstream

- Endpoint protection

   - Endpoint protection

- Internal IdP

   - External IdP

- Internal IT Systems

   - External SaaS Systems

- Internal Business Systems

   - External IaaS/PaaS

- Logging / Monitoring / SIEM / Flow • Substantially reduced visibility

6

## Slide 7

## **Pre-Cloud and SaaS Mapped to ATT&CK**

Collection
Command  Privilege  Pay
Reconnaissance Initial Access Execution Persistence Exfiltration
and Control Escalation Day!
Impact
Research  Deliver target  Exploit  Establish  Establish  Escalate  Iterate 35x
Target,Scan,  payloads perimeter  persistence  control of  privilege if  for lateral
Find Users vulnerabilities of foothold compromised  possible movement
hosts

7

## Slide 8

## **SaaS ATT&CK Tactics**

Collection
Command  Privilege  Pay
Reconnaissance Initial Access Credential  Persistence Exfiltration
and Control Escalation
Access Day!
Impact
Research  Stuff, Spray,  Access SaaS  Skip Skip OAuth, API  IdP tiles,
Target, Find  SIM Swap →  services and  Keys,  Collaboration,
Login to IdP Manipulate login  Integration,  Doc, Source
Users, Find
Configurations App, Often
SaaS
Skipped!

8

## Slide 9

## **This is Why We Canʼt Have Nice Things**

- Substantially expanded our attack surface

- Attack surface is now on other peopleʼs stacks

- IaaS and SaaS companies have similar problems

- Substantially reduced effective security controls

- Shortened and compressed the Kill Chains

- Internet remains a relatively lawless free for all

9

## Slide 10

## **Current State of Affairs**

Jul Aug Sep Oct Nov Dec Jan Feb Mar Apr MayApr Jun
2023 2024

- Phishing, Social Eng, SIM Swap groups - Winning

- Ransomware Affiliates and RaaS Platforms - Winning

- Credential Spraying Actors - Winning

- Infostealer Actors – Winning

- APTs Hacking Supply Chain - Winning

- Sophisticated attackers we donʼt see – Probably Winning

- Organizations and Regular folks on the Internet - Losing

10

## Slide 11

## **Telemetry Information**

##### **Raw Processed Data:**

- 230 **Billion** SaaS Audit Log Events YTD

- 950 **TB** of events collected

- Average 1.2 **Billion** events per day

- 24 distinct SaaS Services

##### **Signals/Alerts Analyzed:**

- 1.9 Million over last 180 days

- 300K Unique IPs

- 1 HPU  Hamster Processing Unit

11

## Slide 12

## **SaaS Attacks Don't Require Most Killchain Activities**

- Reconnaissance activities not logged in most SaaS

- Valid credential activity and data movement are highest observed activities **70%**

- Maintaining foothold - while somewhat present is in many cases not required to achieve objectives **2%**

12

## Slide 13

## **SaaS Attacks Heavily Leverage Cloud Providers**

13

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
SaaS Attacks Heavily Leverage Cloud Providers
25000 4
20000
15000
ASN Org
CLOUDFLARENET
AMAZON-AES
Chinanet
CHINA UNICOM China169 Backbone
GOOGLE-CLOUD-PLATFORM
Korea Telecom
Binariang Berhad
PERFORMIVE
Stiftung Erneuerbare Freiheit
DIGITALOCEAN-ASN
```

## Slide 14

## **SaaS Attacks Heavily Leverage Cloud Providers**

14

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
SaaS Attacks Heavily Leverage Cloud Providers
Alerts by ASN Org and Tactic Name
AMAZON-02
AMAZON-AES
20000
Bharti Airtel Ltd., Telemedia Services
CHINA UNICOM China169 Backbone
CLOUDFLARENET ia
e
ia] Chinanet
i
DIGITALOCEAN-ASN - 10000
Equinix Asia Pacific
GOOGLE-CLOUD-PLATFORM
5000
OPENDNS
Reliance Jio Infocomm Limited
(0)
<
tactic_name
```

## Slide 15

### **Chinese-Affiliated Attacks Focused on Microsoft 365**

Observed ASN
AS4134
AS4837

15

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Chinese-Affiliated Attacks Focused on Microsoft 365
Number of Alerts
1204
100 4
80
605
204
Tactics Per Service
&
&
Tactic Name
Collectior
i
Credential Acces:
Initial Acc
Service
MM 0365
lm okta
*
* *
*
*
Observed ASN:
AS4134
AS4837
```

## Slide 16

## **Enriched Alerts Organized by Tactic**

16

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Enriched Alerts Organized by Tactic
Suspicious IP ::
Tor Nodes
Threats & Actors
Cybercrimin...
Suspicious IP : RELATED_TO
Socks b. ‘Threats & Actors
:: Cybercriminals
1: Report
Threats & Actors
Nation-State
Suspicious IP ::
RELATED Scanners
Malware/Source
=C2
oraaiviay
Compromise &
Suspicious IP ::
Open Proxy
```

## Slide 17

### **Threat Actors Target Valid Account and MFA Techniques**

Public
Leaks
Suspicious
IP: Open
Proxy
Abuse
Elevation
Control
Mechanism
Threats &
Valid  Actors:
Accounts Nation
State

17

## Slide 18

## **Attacker Observations - Credential Access**

Suspicious IP
Tor Nodes
Suspicious
IP::
Scanners
Initial
Access
Credential
Access
Suspicious IP::
Socks b…
Suspicious IP::
VPN

18

## Slide 19

**Attacker Observations - Credential Access** Brute Force & MFA Exhaustion

19

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Attacker Observations - Credential Access
Brute Force & MFA Exhaustion
Suspicious IP :: Scanners
[Successfulllfogin} Man yarallUre: a
—T/ Suspicious IP :: Open Proxy
SS; SS Malware/Source :: C2
> Threats & Actors :: Cybercriminals
QS Threats & Actors :: Cybercriminals ::
Suspicious IP :: VPN
SSI \-Notifications“Followed by SUGgessfulsverification
——= Compromise & leaks :: Public Leaks
—veevavault SuspiclousiP
‘servicenow
```

## Slide 20

## **Attacker Observations - Actions on Objectives**

20

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Attacker Observations - Actions on Objectives
Action on Objective Alerts by Service
Threats & Actors :: Cybercriminals :: Report 4 Service Type
Ml box
Threats & Actors :: Cybercriminals 7 @™ github
MEE gsuite
Suspicious IP :: VPN {fF GM 0365
‘ lm okta
Suspicious IP :: Tor Nodes 7 . sfdc
3 Suspicious IP :: Socks proxy bots me Socks
| @mm workday
g Suspicious IP :: Scanners ;
Suspicious IP :: Open Proxy Hi
Malware/Source :: C2 4
1OC :: Common +
Compromise & leaks :: Public Leaks ==
0 5000 10000 15000 20000 25000 30000 35000
Count
```

## Slide 21

## **Attacker Observations - Attack Chain** Timeline of Tactics and Techniques for Cluster: 6, ASN: 396982

Tactic Names
Impact Credential Access
Collection Initial Access
Defense Evasion

Email Collection Inbox Email Forwarding Set or Updated
Data Manipulation Direct Deposit Payment Election Modified
Modify
Authentication  Authentication Policy Modified
Process
Data from
Mass Download Actions
Cloud Storage
Data from Information  Mass Download Actions
Repositories
Data Destruction Mass Resource Deletion
Impair Defenses IP Address Range Modified
Steal Application
Refresh Token Reuse Attempted
Access Token
Valid Accounts Okta High Risk Login
5/17 5/20 5/23 5/26 5/29 6/1 6/4 6/7 6/10 6/13 6/16 6/19 6/22 6/25 6/28 7/1
2024
Technique Names

21

## Slide 22

Tactic Names
Attacker Observations - Attack Chain
Exfiltration Defense Evasion
Impact Credential Access
Timeline of Tactics and Techniques for Cluster: 11, ASN:396982 Collection Initial Access
Valid Accounts Okta High Risk Login
Steel Application
Refresh Token Reuse Attempted
Access Token
Modify Authentication
Process Security Policy Modified
Data from Information
Anomalous Search Activity
Repositories
Data from
Mass Download Actions
 Cloud Storage
Data Manipulation Direct Deposit Payment Election Modified
Data Destruction Mass Resource Detection
Automated
Excessive Downloads Detected
Exfiltration
4/22 4/25 4/28 5/01 5/04 5/07 5/10 5/13 5/16 5/19 5/22 5/25 5/28 5/31 6/06 6/06 6/09 6/12 6/15 6/18 6/21 6/24 6/27 6/30 7/03 7/06

**2024**

22

## Slide 23

Tactic Names
Attacker Observations - Attack Chain
Persistence Collection
Credential Access Lateral Movement
Timeline of Tactics and Techniques for Cluster: 12, ASN:15830 Impact Initial Access
Valid Accounts Multiple Login Failures Due to Conditional Access Policy
Use Alternate
New Credentials Added to Application Service Principal
Authentication Material
Remote Services Azure AD PowerShell Accessing Non Active Directory Resources
Email Collections Inbox Email Forwarding Set or Updated
Data from Information
Mass Download Actions
Repositories
Data from Cloud
Mass Download Actions
Storage
Data Destruction Mass Resource Deletion
Brute Force Password Spraying Attempted
Account
User Added to High Privileged Role
Manipulation
1/16 1/19 1/22 1/25 1/28 1/31 2/03 2/06 2/09 2/12 2/15 2/18 2/21 2/24 2/27 3/01 3/04 3/07 3/10 3/13 3/16 3/19

**2024**

23

## Slide 24

#### **System Identity controls are lacking in most SaaS products**

- Network Level

   - IP allowlist? **Maybe, likely canʼt be utilized**

   - Block TOR Access? **Doubtful**

- Device Level

   - Corp Device Check? **Doubtful**

   - Device Attribute Profile Monitoring? **Maybe**

- Authentication Flow

   - SSO Available? **Sure - pay the SSO Tax**

   - Restrict Alternative Auth Methods? **Doubtful**

   - MFA Available? **Yes - likely not for service accounts**

24

## Slide 25

## **Observed TTPs Summary**

##### **Credential Access**

**Impact**

- Buy

- Phish

- Cred Spray

- Cred Stuff

   - Stage data and push to cloud resources

   - ● Download directly

   - Email Forwarding Rules

- Enter front door

   - **Obfuscation Methods**

   - VPNs

- **Persistence**

   - Proxies

- Modify Authentication

   - Cloud Providers

-

- ● Create/Use Alternative Credentials ● TOR

25

## Slide 26

## **Well… How Did We Get Here?**

- Bought 150 SaaS products and 3 IaaS/PaaS

- Moved most business processes to SaaS

- Moved most data processing to IaaS/PaaS

- Moved our IdP to the Cloud

- Considered security ramifications too late

- Covid accelerated remote work and SaaS

- Diluted the “Zero Trustˮ protection strategy

26

## Slide 27

**Embrace Your New Attack Surface** Key Takeaways: Strategic

###### **Identify**

**Protect**

###### **Detect**

**Respond**

- Know SaaS & IaaS in use

- SaaS & IaaS intake

- Posture change

   - Integrate into SIEM

- Know the users

- Determine your trust

- Config drift

   - Integrate into XDR

- Know the data

- Harden tenant posture

- New Interconnects

   - Integrate into MDR

- Know the interconnects

- Maintain posture state

- Anomalous behavior

   - Integrate IR Process

- Know their criticality

- Threat Intel Matches

- New SaaS / IaaS

27

## Slide 28

**What Should We Do?** Key Takeaways: Tactical

Use Phishing resistant hardware MFA devices Move important SaaS behind an IdP you can trust Enforce Hardware Key + Device Trust with IdP Avoid the use of “Service Accountsˮ when possible Ingest your SaaS logs and monitor them Enrich your logs with proxy, VPN, tor, and ASN tagging Utilize UEBA capability at the SIEM Implement Zero Trust, for real

28

## Slide 29

# **Thank You**

**Booth #1660**

**ASK US HOW TO**

**Assess SaaS Threats in Your Environments** https://appomni.com/risk-assessment/

29

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Thank You
{0} g) Booth #1660
AppOmni__ blackhat
ASK US HOW TO
Assess SaaS Threats in Your Environments
https://appomni.com/risk-assessment/
29
```
