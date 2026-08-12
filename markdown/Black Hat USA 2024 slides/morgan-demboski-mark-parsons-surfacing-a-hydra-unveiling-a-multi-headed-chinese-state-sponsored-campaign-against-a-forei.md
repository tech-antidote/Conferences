---
title: "Surfacing a Hydra Unveiling a Multi-Headed Chinese State-Sponsored Campaign Against a Foreign Government"
speakers: ["Morgan Demboski", "Mark Parsons"]
conference: "Black Hat"
conference_full: "Black Hat USA 2024"
edition: "USA"
year: 2024
source_pdf: "Black Hat USA 2024 slides/Morgan Demboski & Mark Parsons_Surfacing a Hydra Unveiling a Multi-Headed Chinese State-Sponsored Campaign Against a Foreign Government.pdf"
pages: 66
sha256: "65429b075cffa53684481f572bfe8ed7ad73c56ef629a49d2da6e21ff311e4ff"
text_chars: 23506
ocr_pages: 8
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:35:19Z"
---
# Surfacing a Hydra Unveiling a Multi-Headed Chinese State-Sponsored Campaign Against a Foreign Government

**Speakers:** Morgan Demboski, Mark Parsons  
**Conference:** Black Hat USA 2024  
**Source:** `Black Hat USA 2024 slides/Morgan Demboski & Mark Parsons_Surfacing a Hydra Unveiling a Multi-Headed Chinese State-Sponsored Campaign Against a Foreign Government.pdf` (66 pages)


## Slide 1

Surfacing a Hydra _Unveiling a Multi-Headed Chinese State-Sponsored Campaign Against a Foreign Government_

**Speakers: Mark Parsons & Morgan Demboski**

#BHUSA @BlackHatEvent _Image: Taylor James_ s

## Slide 2

#### **Introductions**

**Morgan Demboski Mark Parsons Threat Intelligence Analyst Senior Threat Hunter** Washington, DC Charleston, South Carolina, USA _@Morgan_Demboski @security_dumpster @_mcp_ l_

2

## Slide 3

### **Agenda**

Background **Operation Crimson Palace:** Operation Crimson Palace: Stage 1 **Stage 1** _Cluster Analysis & Assessing Overlap_ **Cluster Charlie Returns & Cluster Bravo** Operation Crimson Palace: Stage 2 **Expands: Stage 2** _C2 Gap Analysis SPADE Tool_

Takeaways & Q&A

TLP:GREEN

3

## Slide 4

# **Background**

4

## Slide 5

A years-long cyberespionage campaign tracked by Sophos MDR, attributed to Chinese statesponsored actors

**_STAC1248_**

**_STAC1870_**

**_STAC1305_**

- Two-stage campaign

- Multiple active & coordinated "groups"

- Broad targeting of critical orgs in a SE Asian country

5 TLP:GREEN

5

## Slide 6

#### **Victimology**

• **SE Asian government organization** `o` Campaign later **expanded to other critical organizations** in the country `o` History of conflict with China over South China Sea (SCS)

Source: @Xmultiverse_org

6

## Slide 7

#### **Immediate Challenges**

- Onboarded with existing long-term breach `o` Related activity dating back to early 2022

- **Lack of full visibility / major coverage gaps**

_If we can’t take mitigation actions directly,_ **_what can we as defenders do to make the most of the situation?_**

Source: David Truss

7

## Slide 8

# **Initial Triage**

8

## Slide 9

#### **How did it start?**

###### **PowerShell TCP Listener**

443 | % {echo ((new-object
Net.Sockets.TcpClient )
.Connect("www[.]msudapis[.]info",$_))
$_" is open!"} 2>$null 154.39.137[.]29
vmnat.exe cmd.exe
powershell.exe
SophosUD.exe
sslwnd64.exe
Key
Process Action
Execution Context
LoLBin
Host:  Office 365 Integrations Server
Malicious EXE Path:  C:\ProgramData\Microsoft\Vault\vmnat.exe
# Execution Order
9

9

## Slide 10

###### **Within 7 days, we found 13 malware families across ¼ of the org's server infrastructure...**

10 TLP:GREEN

10

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Within 7 days, we found 13 malware families across % of the org's server infrastructure...
185.195.237[.]123 cloud.keepasses|. |associate.freeon! [.Jcom
Government Domain & 195.123.247[,]50 89.44.197.]74 APT15 198.13.47[.]158 185.167.116[,]30 185.201.8[.]187
TA Infrastructure
185.195.237[.]121 message.ooguyl.Jcom www-<TAl 8 ‘scancenter.trendrealti in.feedfoodconcerni
Government Domain ime[.Jcom jlespeedtest33[.Jcom www.msudapis[.Jinfo logit ing.org
45.90.58[.]103 143.198.85[.]36 139.180.217[.]105 45.76.3[.]140 64.176.38[.]173 154.39.137[.]29 195.123.245[.J79
dat
es shfolder.dil ping-n1 eg
dunt mat
443.txt aB.txt_|
ping uit Juni2
4413.tet Junt2
ssiwnd64.exe
Bea 5 (Marts) 8 (warz7) Mays TSVIPSrv.ll mi
AM dumy wibsctrl.dil dal
DC1 4413.txt 6 (Mar15) 365
commepem Mars] sunt ret use info.bat mye convenes
a8 txt oe Hypervisor ; ;
bhrome. Mart5 vmnat a8.txt, 443,txt 7 SophosUD.exe
srvany ‘Juni2 1 aB.txt
instsrva gat wdm Junt2
srvany.exe coreframeworkservice ‘SbphosUD.«
tdpclip
Mai winsc.exe shiokier
msi64.exe Ut
Azure jl aon
2.vbs on TSVIPSrv.dll
Licensit sslwnd64.0xe ny Lesnaeal
mscorsve.dil May 19 thumtals2.dat nethood.exe
mscorsvw.exe Ts 1.1
ool. UD.exe
ping Port 80 (May
rae 3 (Mara) 4 4) qe. nethood B
lc
Port 22,80 Perti AMS File Mazz gael 7 SERVER
Cer pump A | mnt (ars) same og
r eke chrome.
ssiwndé4 | A e Sere (Cert. > oci.dll
wmic Mecorswuexe ici Authority.
3 winsecunicity.exe ui rl
3.vbs Mari6 oat systemcontig.exe WinDet
licensing.exe Mar22 3.pst ys: ig. is
ntpsapidl cryptography.exe execute.bat watt March30}
MPSvc.dll DCS5.
net use shfolder comment.cmtx
wmie vmnat.dil
SystemTemps !
wmic
Admin ‘Adraina be
Mar8 May19
172K UXHHH-HEE
ees iran» Conan = Ctrexxo00> Unmanaged Infrastructure
```

## Slide 11

###### **Within 7 days, we found 13 malware families across ¼ of the org's server infrastructure...**

https://twitter.com/shannel_lynn/status/1790575400118092072

11 TLP:GREEN

11

## Slide 12

#### **Moving From Wild Hunches to Evidence Driven Theories**

**How do we go from:**

12

## Slide 13

# **Uncovering the Threat Clusters**

13

## Slide 14

**Clustering Methodology** Noticed anomalous patterns in several factors:

Authentication data, including source subnet, workstation hostname, & account usage

Repeat use of techniques, including specific commands & options

Unique tools & the paths they were deployed to

Targeted user accounts & hosts

Timing of the observed activity

Attacker C2 infrastructure

14

## Slide 15

_March 2023 – August 2023_ **Cluster Alpha Known overlap: STAC1248 BackdoorDiplomacy; REF5961; Worok; TA428 Malware:** Merlin C2 Agent; RUDEBIRD/Impersoni-FakeAtor; PhantomNet; PowHeartBeat; EAGERBEE **Credential Access:** SAM registry hive dump; LSASS dump **Lateral Movement:** wmic; net use; psexec; rdpclip; valid accts; impacket **Privilege Escalation** : Service creation; Windows services abuse **Defense Evasion:** Modified EAGERBEE; Phantom DLL sideloading **Cluster Bravo 443.txt creation Cluster Charlie Same admin STAC1870 credential set Same admin STAC1305 Same servers credential set Same network** _March 2023_ **Chinese work hours** _March 2023 – May 2024_ **Known overlap: Overlapping Known overlap: Unfading Sea Haze timeframes Earth Longzhi (APT41 subgroup) Malware:** CCoreDoor **Malware:** PocoProxy; Cobalt Strike; backdoor/EtherealGh0st HUI Loader; Havoc C2 **Credential Access:** LSASS dump **Operating from Credential Access:** LSASS dump **same endpoints Lateral Movement:** Valid accounts; **Lateral Movement:** Valid accounts; Lateral tool transfer scheduled tasks; WinRS; wmic; **Ntdll.dll overwrite** remote service creation; impacket **Persistence:** Scheduled tasks **Privilege Escalation** : runas **Defense Evasion:** Overwriting ntdll.dll in memory **Defense Evasion:** Disconnect network drive mappings; AV vendor software abuse

#### **Overlapping Behaviors**

15

## Slide 16

_Operation Crimson Palace: Stage 1_

# **Spotlight on Cluster Attack Flows**

16

## Slide 17

Action
Cluster Alpha Overlap A
Pattern of Life: BRAVO
Lateral Movement
Key
Network Comm. Cluster Charlie Overlap C
Attack Vector
(DESKTOP-1EDVSHB)​
Account A
C
AdminF Local-Admin UserJ Remote Scheduled Task
Target A A A C A C C C
AdminC AdminP AdminT Acctng Anna Lawyer Larry
DC-Sync AMS Hypervisor File Server
Malware
CCoreDoor Agent Shim  LoLBin  CCoreDoor CCoreDoor
(mscorsvc.dll) (ntpsapi.dll) (rdrleakdiag.exe) (mscorsvc.dll) (mscorsvc.dll)
C2 Domain
message.ooguy[.]com
C2 IP
146.190.93[.]250

17

## Slide 18

Action
Cluster Bravo Overlap B
Pattern of Life: ALPHA Key Lateral Movement
Cluster Charlie Overlap
Network Comm. C
C
Attack Vector
VPN Subnet
VPN Subnet
Account B
AdminF AdminA AdminP
Target C B C B B CC
DC1 Cert. Authority Hypervisor 365 AMS Web Server Hypervisor
Malware
Quarian Backdoor Merlin C2  RudeBird PowHeartBeat PhantomNet PhantomNet  EagerBee+  EagerBee+  AVSideload
(pc2msupp.dll) (vmnat.dll) (MSI64.exe) (SophosUD.exe) (oci.dll) (sslwnd64.exe) (jli.dll) (TSVipSrv.dll / wlbscrtl.dll) (SensAPI.dll)
C2 Domain
cloud.keepasses[.]com scancenter.trendrealtime[.]com msudapis[.]info associate.freeonlinelearningtech[.]com paper.hosted-by-bay[.]net
C2 IP
91.220.202[.]143 195.123.245[.]79
88.47.197[.]74 154.39.137[.]29
185.195.237[.]123
139.162.18[.]187
45.90.58[.]103 185.167.116[.]30
18

## Slide 19

Action
Cluster Alpha Overlap A
Pattern of Life: CHARLIE Lateral Movement
Key
Cluster Charlie Overlap C
Network Comm.
Attack Vector
VPN Subnet
Account
A B B
AdminC Remote Scheduled Task SCCMAdmin UserJ
A
Target A B B AA
365 Marketing Maria HR Henry Front Desk Fran Sales Sam Web Server DC1 DC2
Malware
PocoProxy PocoProxy PocoProxy PocoProxy
(443.txt) (4413.txt) (chrome.log/aaaa.txt) (a8.txt) McAfee File Lock Sideload LSA Credential Interceptor HUI Loader AlmostATExec
(McPvNs.dll) (11.log) (msedge_elf.dll) (Hideschtasks.exe)
C2 Domain
googlespeedtest33[.]com <TARGET>speedtest[.]com
<TARGET> dnsspeedtest2022[.]com
C2 IP
192.143.46[.]158 64.176.50[.]42 158.247.241[.]188 139.180.217[.]105 185.201.8[.]187

19

## Slide 20

_Operation Crimson Palace: Stage 1_

# **Cluster Analysis & Assessing Overlap**

20

## Slide 21

#### **Initial Attribution is Puzzling**

- Industry tends to liberally create new threat groups vs campaigns

- **PRC-Aligned Activity: Assumptions**

   - Known to have multiple APTs targeting SE Asia

   - Tool sharing & infrastructure reuse

- **Observed overlap with:**

   - Mustang Panda (Legacy)

   - Backdoor Diplomacy / APT15

   - REF5961

   - Earth Longzhi (APT 41 Subgroup)

Source: FS

- Worok / TA428

- Unfading Sea Haze

21

## Slide 22

#### **Time of Day Analysis**

22

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Time of Day Analysis
Heatmap of Cluster Alpha Heatmap of Cluster Bravo
Heatmap of Threat Activity
Hour of the Day (UTC)
Time of Day (UTC +8)
-_
{S)
Ee
=)
—
>
oO
=)
o
<=
~
—
°
_
S
(-)
=
Time of Day (UTC +8)
Tuesday Wednesday Thursday Friday Saturday
Day of the Week
10:00, 6PM
08:00 es 4PM
06:00 2PM
04:00 12PM
02:00 — 10 AM
00:00 8AM
Monday Tuesday Wednesday Thursday Friday Saturday Sunday
Day of the Week
Hour of the
Time of Da
```

## Slide 23

##### **Adversary Patterns**

- **Cluster Alpha | STAC1248**

- Month 1 – Month 6

- Often occurred within the traditional working hours of 8am to 5pm CST

- Peaked on Friday

###### **Cluster Bravo | STAC1870**

- Mini-cluster from Month 1

- Often occurred within traditional working hours of 8am to 5pm CST

- Peaked on Tuesday, Wednesday, & Thursday

###### **Cluster Charlie | STAC1305**

- Month 2 – Month 6

- Varied the most outside standard working hours

- Peaked Monday through Wednesday 12pm to 6pm CST

- Spike of activity on holiday in June

TLP:AMBER+STRICT

23

## Slide 24

_Operation Crimson Palace: Stage 1_

# **Connecting the Dots**

24

## Slide 25

##### **Connecting the Dots**

**CLUSTER BRAVO**

- EDR unhooking through rapid loading of renamed ntdll.dll into a malicious process

Defense Evasion

• Novel backdoor in the form of - CCoreDoor/Ethereal Gh0st

Command & Control

   - Credential Capture via LoLBin RDRLeakDiag

   - • Implant deployment to specific users & systems

- Preliminary Targeting

25

## Slide 26

##### **Connecting the dots**

**CLUSTER ALPHA**

Precise Recon

• Recon of specific users and systems

- DLL sideloading of AV vendor binaries

- • Evading EDR through DNS Blackhole

Abuse of Vendor Tools

- Multiple methods to reach same goal

Testing in Production

- Making mistakes

26

## Slide 27

##### **Connecting the dots**

### **CLUSTER CHARLIE**

- Prioritizing access management

Eyes on the - Long Game

- Usage of unreported custom malware - PocoProxy for C2

   - Exfiltration

Actions on objectives

   - Keyloggers

      - TattleTale Malware

- DLL sideloading of AV vendor binaries

Abuse of vendor tools

- AV Vendor Drivers for EDR bypass

27

## Slide 28

#### **Cluster Overlap** – Targets of Interest

Assumption: We are observing isolated malicious events against targets of interest

Admin C Admin P Sales Sam
Lawyer Larry Admin S
Acctng Anna
C2 Implant Auth Pattern Recon
Keylogger
Key Credential Capture
Doc Capture 28

## Slide 29

###### **Cluster Overlap** – Targets of Interest

Apr. 23 Jun. 23 Aug. 23 Oct. 23 Jan. 24 Mar. 24 May. 23
Time Mar. 23 May 23 Jul. 23 Sep. 23 Dec. 23 Feb. 24 Apr. 23
Admin C
Admin P
Sales Sam
Acctng Anna

Acctng Anna
Lawyer Larry

Admin S

C2 Implant Auth Pattern Recon Cluster Alpha
Keylogger Credential Capture Cluster Bravo
Key
Doc Capture Cluster Charlie

29

## Slide 30

#### **Division of Labor** – Cluster Objectives

###### **Cluster Bravo**

- Developing initial foothold by deploying CCoreDoor backdoor to specific users & admins

###### **Cluster Alpha**

- Mapping victim domain, focusing on infrastructure & programs

- Identifying admins & directors of key applications

- Testing out different payloads & techniques

###### **Cluster Charlie**

- Capture and Exfiltration of Confidential Documents & IT Infrastructure Documentation & Key Material

- Gaining & maintaining access throughout network

30

## Slide 31

###### Timing and overlaps indicate a level of coordination and awareness

We have moderate confidence these activity clusters were part of a **coordinated campaign under the direction of a single organization**

_BH Asia 2024:_ _<u>China’s Military Cyber Operations – Pukhraj Singh</u>_

Source: <u>ESMT Berlin</u>

31

## Slide 32

32

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
CHINA FUNDING ITS CYBER OPERATIONS
® i
```

## Slide 33

## **Cluster Charlie Returns with a Vengeance: Stage 2**

_(September 2023 - April 2024)_

33

## Slide 34

#### **Catching our breath? (or so we thought)**

34

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Catching our breath? (or so we thought)
CLUSTER
CHARLIE PREPPING
DOZENS OF
NEW BACKDOORS
OUR TEAM BLOCKING
THEIR IMPLANTS
limgfiip.co
```

## Slide 35

#### **A Change of Pace**

**Stage 2** = Begins at the end of September 2023 as Cluster Charlie re-penetrates the network via a web shell and performs recon on the victim's confidential docs webserver

35

## Slide 36

###### **Actions on Objective**

- Document capture

- Keyloggers

##### **A Change of Pace**

- Tattletale malware

###### **Starting to deploy open-source & custom tooling**

- Shadow Copy Service DLL

###### **Continuing to make mistakes**

- Service DLL sideloading

###### **Taking masquerading to the next level**

- Targets Sophos binaries

- Abuses AV vendor tools

36

## Slide 37

#### **Actions on Objectives**

In November, Cluster Charlie began to exfiltrate highly sensitive info for espionage purposes

•

- **Other Actions on Objectives:**

- Keylogger deployments `o` TattleTale malware

- • Ensuring full access to entire environment

- Docs related to military, cybersecurity, and economic interests – many related to military strategy in the SCS

- The Windows and Web Credential Store of several admins

- Individual VoIP phone databases

- Cloud OpenVpn certs and configs, data backup project documentation, and switching infrastructure

- Disaster recovery data, network data, email data

- Services data (IP block assignments, server blade configurations, DMZ configurations, server/backups inventory, network diagrams, and domain user lists)

- Extensive data from the Mobile Device Manager (MDM) solution

37

## Slide 38

#### **Cluster Charlie Stage 2: Timeline**

Nov. 2023 Jan. 2024 First use of Havoc C2 framework RealBlinding EDR Disablement Sharphound reconnaissance Deploying keylogger tool Testing DLL sideloading of Sophos binaries Targeted capture of user Deploying custom C2 to SWPRV Service DLL documents & Viber databases

Sept. 2023 Nov. 2023 Jan. 2024 First use of Havoc C2 framework Deploying web shell to confidential RealBlinding EDR Disablement documents server Sharphound reconnaissance Deploying keylogger tool Capturing web application server DLL Testing DLL sideloading of Sophos binaries Targeted capture of user Deploying custom C2 to SWPRV Service DLL documents & Viber databases Reconnaissance of Sophos Threat Protection & Policy Server data from Windows registry keys Credential Access – LSASS dump Network interactions to in-country telco Targeted espionage activity – sensitive document Sideloading of Trend Micro capture ptwatchdog.exe Capturing IT backup infrastructure key material New variant of CCoreDoor / Attempted use of Cobalt Strike C2 Framework EtherealGh0st malware

Oct. 2023

Dec. 2023

## Slide 39

#### **Cluster Charlie Stage 2: Timeline (cont.)**

Feb. 2024 Deploying Xiebro C2 Framework A | B testing of Cobalt Strike vs Havoc C2 Shellcode Loader Using DonutLoader Shellcode Loader

April 2024

Continued embedment into endpoints / uncompromised systems​ Re-use > 1yr old C2 IP infrastructure Consistent blocking of Havoc Framework Credential Access via NTDS.dit Credential Access – LSASS dump

Continuing use of Alcatraz EDR Evasion tool Targeting of Executive Branch external assets Deploying custom C2 Tooling Deploying system fingerprinting, credential capture, and keylogger tools Using AV drivers to disable telemetry Targeted reconnaissance of users of interest 4624 Event logs via PowerShell March 2024 May 2024

39

## Slide 40

_Operation Crimson Palace: Stage 2_

# **C2 Gap Analysis**

40

## Slide 41

###### **Open-Source Tooling & C2 Framework Analysis**

Nov. 23 Dec. 23 Jan. 24 Feb. 24

Mar. 24

April 24 May 24

C2 Tooling

EDR Evasion Tooling
Cobalt Strike C2
Tool Deployed
Havoc C2
Hunt Team Identification
Xiebro C2
Blocking Detection Custom C2

RealBlinding EDR AV Vendor Driver Alcatraz EDR Evasion

41

## Slide 42

###### **C2 Framework Analysis**

- Conducting 'A | B' testing

   - Deploying Cobalt Strike Reflective Loader alongside Havoc Loader, samples maintained same DLL name, and same C2 infrastructure

- Taking a tactical approach

   - Cluster Charlie actors relied on opensource tooling & did not shift back to custom tooling until multiple iterations of open-source frameworks were blocked

Source: BigMailer

42

## Slide 43

43

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
o, 1) y
HEN THE THREAT ACTORS es
DONT SHOW UP. LIKEYOU PREDICTED
pebeomthruF.com
```

## Slide 44

_Operation Crimson Palace: Stage 2_

## **Creating the Session Process Anomaly and Discovery Examination (SPADE) Tool**

44

## Slide 45

##### **SPADE Tool**

ping
net
findstr
tasklist
taskkill
Parent Process
wmic
schtasks
bitadmin
echo
dir
wevtutil
query

###### **What does C2 look like?**

Typically, discovery commands are executed from a sideloaded or injected process over a short time span, which generates network connections to a small number of external IPs

**Problem** It’s hard to find malicious discovery commands from a single parent to child relationship because of the volume of processes & programs executing typically benign binaries

**Solution**

Come up with a way to look for a process from a specific path executing more than one discovery process = **The SPADE Tool**

45

## Slide 46

##### **SPADE Tool**

###### **Parent Process**

ping
net
findstr
tasklist
taskkill
wmic
schtasks
bitadmin
echo
dir
wevtutil
query

The SPADE tool looks for more than **2 discovery commands** from a parent process over a **2-hour session**

- Takes into account human patterns

2-Hour Block

46

## Slide 47

##### **SPADE Tool**

net
SESSION 1
Parent Process A wmic
schtasks
net net net
Removes  repeating
Parent Process B net net net
sessions
echo echo echo
net
wmic
Parent Process C Removes  automated
tasklist
sessions  /  high process count
Proc4…99
net
SESSION 2
Parent Process A wmic
wevtutil
ping
Parent Process E taskkill
findstr

47

## Slide 48

##### **SPADE Tool**

net
SESSION 1
Parent Process A wmic
schtasks
net net net
Removes  repeating
Parent Process B net net net
sessions
echo echo echo
net
wmic
Parent Process C Removes  automated
tasklist
sessions  /  high process count
Proc4…99
net
SESSION 2
Parent Process A wmic
wevtutil
ping
Parent Process E taskkill
findstr

48

## Slide 49

##### **SPADE Tool**

net
Removes  repeating
Parent Process A1 wmic
sessions
schtasks
net Removes  automated
Parent Process A2 wmic sessions  /  high process count
wevtutil
ping
Parent Process E taskkill
findstr

49

## Slide 50

net net ping
Parent Process A1 wmic Parent Process A2 wmic Parent Process E taskkill
SPADE Tool
schtasks wevtutil findstr
net ping
Host 1
Parent Process F wmic Parent Process E taskkill
wevtutil findstr
Host 2 ping
Parent Process E taskkill
findstr
Host 3
net net
Parent Process G1 wmic Parent Process G2 wmic
schtasks wevtutil
Host 4

Removes **repeating parent process paths** across environment

50

## Slide 51

net net ping
SPADE Tool Parent Process A1 wmic Parent Process A2 wmic Parent Process E taskkill
schtasks wevtutil findstr
net ping
Host 1
Parent Process F wmic Parent Process E taskkill
wevtutil findstr
Host 2 ping
Parent Process E taskkill
findstr
Host 3
net net
Parent Process G1 wmic Parent Process G2 wmic
schtasks wevtutil
Host 4

Removes **repeating parent process paths** across environment

51

## Slide 52

net net
SPADE Tool
Parent Process A1 wmic Parent Process A2 wmic
schtasks wevtutil
Host 1
net
Removes  repeating parent process paths
Parent Process F wmic
across environment
wevtutil
Host 2
net net
Parent Process G1 wmic Parent Process G2 wmic
schtasks wevtutil
Host 4

52

## Slide 53

net net
SPADE Tool
Parent Process A1 wmic Parent Process A2 wmic
schtasks wevtutil
Host 1
net
Parent Process F wmic
Filters on the number
wevtutil
of  distinct external
network connections
Host 2
net net
Parent Process G1 wmic Parent Process G2 wmic
schtasks wevtutil
Host 4

53

## Slide 54

net net
SPADE Tool
Parent Process A1 wmic Parent Process A2 wmic
schtasks wevtutil
Host 1
net
Parent Process F wmic
Filters on the number
wevtutil
of  distinct external
network connections
Host 2
net net
Parent Process G1 wmic Parent Process G2 wmic
schtasks wevtutil
Host 4

54

## Slide 55

#### **SPADE Tool**

net net
C2 Process, Session1 wmic C2 Process, Session2 wmic
schtasks wevtutil
Host 1
Leaves us with  malicious C2
session data & infrastructure

55

## Slide 56

_Operation Crimson Palace: Stage 2_

# **Operation Crimson Palace Expands** **_Compromising other victims_**

56

## Slide 57

#### **Cluster Bravo Activity Expands**

Since January 2024, Sophos has detected activity associated with Cluster Bravo on the networks of **at least 11 other organizations & agencies** in the same country

Using **previously compromised government agencies** for malware staging & C2 (command & control)

57

## Slide 58

# **Takeaways**

58

## Slide 59

59

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
THERE IS NO HAPPY ENDING
* A nm
```

## Slide 60

#### **Takeaways**

China has been completing these actions for the past 10 Be flexible with how you hunt, years and only shows signs of you will never have perfect Logs Are Cheaper than increasing their pacedata Lawyers

60

## Slide 61

#### **Acknowledgments**

Paul Jaramillo ▪ Kostas Tsialemis Sean Gallagher ▪ Gabor Szappanos Colin Cowie ▪ Andrew Ludgate Jordon Olness ▪ Steeve Gaudreault Greg Iddon ▪ Daniel Souter Hunter Neal ▪ Pavle Culum Andrew Jaeger ▪ Peter Mackenzie

- Elida Leite

- ▪ Lee Kirkpatrick

**...as well as many other members of the Sophos MDR APT, Operations, Rapid Response, and LABS teams for their work**

61

## Slide 62

## Slide 63

##### **Appendix – Read More About Operation Crimson Palace: Stage 1**

Operation Crimson Palace:
Overview
Operation Crimson Palace: A
Technical Deep Dive

## Slide 64

**Appendix - Cluster Charlie C2 Channel Mind Map**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Appendix - Cluster Charlie C2 Channel Mind Map
=—— —s
\
a o[ rorseaartsreas | oe
woo ha
of 107 enema |
[ o[seraeeaniiven eg el
ee npupdatel net lal 45.18.1491 ]151:443
oe a Kt H{ ra eet
toe Se oe Mc) ==
45.15.149,151:443
as9.1911189:449
“Y noaeen a 043621
Vulnerable To DLL Hijack
—_
(mea)
= )
‘CAPerflogsyconsole.exe
2024-03-10 09:31:17. Fee a
‘CisersPubicliretoxaxe ‘APerfLogavi-a,
2024-04-10 9:04:38 AM FA cxvartsgrweteninet ent
SOPHOS
```

## Slide 65

**Appendix – Spade C2 Detection Tool**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Appendix — Spade C2 Detection Tool
SOPHOS
```

## Slide 66

#### **Appendix – Further Reading**

- <u>ChamelGang & Friends | Cyberespionage Groups Attacking Critical Infrastructure with Ransomware</u>

   - "Threat actors in the cyberespionage ecosystem are engaging in an increasingly disturbing trend of using ransomware as a final stage in their operations for the purposes of financial gain, disruption, distraction, misattribution, or removal of evidence."

- <u>IOC Extinction? China-Nexus Cyber Espionage Actors Use ORB Networks to Raise Cost on Defenders</u>

   - "China-nexus cyber espionage operations where advanced persistent threat (APT) actors utilize proxy networks known as 'ORB networks' (operational relay box networks) to gain an advantage when conducting espionage operations."

- <u>Is CNVD ≥ CVE? A Look at Chinese Vulnerability Discovery and Disclosure</u>

   - "The US is still lagging behind China in terms of vulnerability discovery and disclosure. While the gap between the US National Vulnerability Database (NVD) and the Chinese NVD (CNNVD) has slightly shrunk over the last 5 years, there are still hundreds of vulnerabilities registered in China that are yet to be listed on the US NVD. Based on information collected, it was determined that the 151 companies providing the MSS vulns employ 1,190 vulnerability researchers and that they provide at least 1,955 vulnerabilities to the MSS each year."
