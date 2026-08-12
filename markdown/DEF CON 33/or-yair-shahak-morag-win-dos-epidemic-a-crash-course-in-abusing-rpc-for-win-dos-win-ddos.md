---
title: "Win-DoS Epidemic A crash course in abusing RPC for Win-DoS & Win-DDoS"
speakers: ["Or Yair Shahak Morag"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33/Or Yair Shahak Morag - Win-DoS Epidemic A crash course in abusing RPC for Win-DoS & Win-DDoS.pdf"
pages: 133
sha256: "be20c42481bbb969aae423f347bd5b2d10f0bbb3190d0552569919ed86da15ad"
text_chars: 20029
ocr_pages: 8
has_ocr: true
redacted_secrets: 0
ocr_confidence: 86.9
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T07:09:53Z"
---
# Win-DoS Epidemic A crash course in abusing RPC for Win-DoS & Win-DDoS

**Speakers:** Or Yair Shahak Morag  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33/Or Yair Shahak Morag - Win-DoS Epidemic A crash course in abusing RPC for Win-DoS & Win-DDoS.pdf` (133 pages)


## Slide 1

**A Crash Course in Abusing RPC for Win-DoS & Win-DDoS**

Or Yair, Security Research Team Lead, SafeBreach Shahak Morag, Research Lead, SafeBreach

**1**

## Slide 2

**A Crash Course in Abusing RPC for Win-DoS & Win-DDoS**

**2**


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
win-DoS EPIDEMI¢
A Crash Course in Abusing RPC
for Win-DoS & Win-DDoS
```

## Slide 3

###### **OR YAIR**

**Security Research Team Lead at SafeBreach 7 years in Security Research Past research in Linux, embedded, Android 4 years Windows research**

## Slide 4

###### **SHAHAK MORAG**

**Research Lead at SafeBreach 7 years in Security Research Past research in Linux kernel, embedded 1+ years Windows research**

## Slide 5

###### **AGENDA**

1. DDoS & DoS

2. LDAPNightmare – Our gateway

3. Research Goals

4. Developers’ Blind Spots

5. From DoS to DDoS

6. Vulnerability Discoveries

7. Takeaways

8. GitHub + Q&A

5

## Slide 6

SM1OY2

DDoS

VICTIM SERVER

6

## Slide 7

###### **Slide 6**

**SM1** אולי להוסיף בהתחלה הסבר עלDDOS רגיל Shahak Morag, 2025-07-03T09:47:09.768

**OY2** Change to sketch Or Yair, 2025-07-06T08:04:54.435

## Slide 8

### **THE GROWING THREAT of DoS and DDoS ATTACKS**

**7**

## Slide 9

###### **DDoS ATTACK INCREASE**

###### Gcore Radar:

DDoS Attack Count 2023–2024

512000
457000
445000
385000
320000
296000 300000
274000
Q1 Q2 Q3 Q4 Q1 Q2 Q3 Q4
2023 2024

8

## Slide 10

SM1

**9**


> Recovered by OCR — confidence 89/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
The Hacker News + Follow - [M1
Visit website
Iwe ®
| A record-breaking DDoS attack just slammed a hosting provider with 7.3 Tbps of
traffic.
It lasted 45 seconds—and bombarded 34,000+ ports per second.
Cloudflare blocked it. But RapperBot is just getting started.
Full story — https://Inkd.in/gaNpA2B2
Cloudflare defenses autonomously block a 7.3 Tbps DDoS attack
=—H \
```

## Slide 11

###### **Slide 9**

###### **SM1** לשים זכוכית מגדלת

מי עשה אותה ומה הנזק,פרטים על התקיפה. Shahak Morag, 2025-07-03T09:33:44.384

## Slide 12

### **DoS HAS A PRICE**

**10**

## Slide 13

###### **LDAPNightmare DoS BY YUKI CHEN - OUR GATEWAY**

**DoS**

**11**


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LDAPNightmare DoS
BY YUKI CHEN - OUR GATEWAY
oes Sa fe B reac h Why SafeBreach Solutions Use Cases Resources Our Partners Company
JAN 1, 2025
LDAPNightmare: SafeBreach Labs
Publishes First Proof-of-Concept Exploit
for CVE-2024-49113
See how SafeBreach Labs Researchers developed a zero-click PoC exploit that crashes unpatched Windows Servers using
the Windows Lightweight Directory Access Protocol (LDAP) Denial of Service Vulnerability.
11
```

## Slide 14

###### **LDAPNightmare DoS SERVERS TRANSFORMING INTO CLIENTS**

CLDAP Client

R P C C A L L Q U E R Y
DsrGetDcNameEx2()
Domain  CLDAP
Controller Server
12

## Slide 15

###### **LDAPNightmare DoS SERVERS TRANSFORMING INTO CLIENTS**

ANSWER WITH
INVALID VALUE
Domain  CLDAP
Controller Server
13

## Slide 16

##### LDAPNightmare BLIND SPOT

The LDAP client code in Windows turned out to be a blind spot!

14

## Slide 17

**RESEARCH GOALS DoS vulnerabilities in developers’ blind spots**

**15**

## Slide 18

###### **AIMING FOR DOMAIN CONTROLLERS**

Domain Controllers are organizations’ crown jewels

**16**

## Slide 19

### **DEVELOPER BLIND SPOTS IN WINDOWS**

**17**

## Slide 20

**DEVELOPER BLIND SPOTS IN WINDOWS** 1. Remotely triggered client code – Same as LDAPNightmare

2. Transport-agnostic wrapped server code

**18**

## Slide 21

**DEVELOPER BLIND SPOTS IN WINDOWS** 1. Remotely triggered client code – Same as LDAPNightmare

2. Transport-agnostic wrapped server code

**19**

## Slide 22

###### **RPC INTERFACES**

v

**20**


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
RPC INTERFACES
Learn / Windows / Apps / Win32 / Desktop Technologies / Networking and Internet /
Remote procedure call (RPC)
02/08/2022
Microsoft Remote Procedure Call (RPC) defines a powerful technology for creating distributed client/server programs.
The RPC run-time stubs and libraries manage most of the processes relating to network protocols and communication.
This enables you to focus on the details of the application rather than the details of the network.
20
```

## Slide 23

###### **RPC INTERFACES ARE WRAPPED SERVERS!**

RPC Client
Process

I N VO K E R P C Method1

RPC Server Process

rpcrt4.dll

DLL/EXE with RPC interface: HandleRpcMethod1()

**21**

## Slide 24

**RESEARCH ASSUMPTION** Developers are likely to forget about mitigating classic server risks in RPC servers

**22**

## Slide 25

# **RESEARCH PROCESS**

**23**

## Slide 26

**CLIENT CODE – LDAPNightmare** Domain Controllers can be turned into clients effortlessly and anonymously They trust any LDAP server

**24**

## Slide 27

###### **WINDOWS LDAP CLIENT CODE**

Wldap32.dll Support LDAP & CLDAP Can be triggered using NetLogon’s RPC

**25**

## Slide 28

**LdapNightmare - LDAP Referrals** LDAPNightmare Root Cause:

OY1

 Bug in wldap32.dll’s handling of LDAP Referral packets

Domain CLDAP LDAP REFERRAL WITH INVALID VALUE Controller Server

**26** 26

## Slide 29

**Slide 26**

**OY1** Add a textual list of LDAP referrals and talk about it in the notes

Or Yair, 2025-07-06T08:30:56.486

## Slide 30

###### **LdapNightmare - LDAP Referrals**

Referrals: L DA P
S E R V E R 1
Question about X
[
“ ldap://server2.com ”, Refer to LDAP Server 2
“ ldap://server3.com ”
]
L DA P
S E R V E R 2
27

## Slide 31

###### **LdapNightmare - LDAP Referrals**

Referrals: L DA P
S E R V E R 1
Question about X
[
“ ldap://server2.com ”, Refer to LDAP Server 2
“ ldap://server3.com ”
] Question about X
L DA P
Answer  about X
S E R V E R 2

**28**

## Slide 32

###### **IF WE CONTROL THE DIRECTION, CAN THAT PROVIDE US DIFFERENT ABILITIES BESIDES CRASHING?**

**29**

## Slide 33

###### **From DoS to DDoS**

**30**

## Slide 34

###### **From DoS to DDoS - Harnessing LDAP Referrals**

REFER x1000 TIMES TO THE VICTIM `[“ldap://victim1.com:80”, “ldap://victim1.com:80”, …]`

**31**

## Slide 35

###### **From DoS to DDoS – DDoS flow**

**C & C**

**AT TAC K E R**

**V I C T I M S E R V E R**

**32**

## Slide 36

###### **From DoS to DDoS – Potential Referral DDoS**

**L DA P S E R V E R**

AT TAC K E R

V I C T I M S E R V E R

**33**

## Slide 37

###### **TCP vs UDP**

**34**

## Slide 38

###### **REFER FROM OUR SERVER TO OUR SERVER**

**35**

## Slide 39

###### **From DoS to DDoS - Harnessing LDAP Referrals**

REFER x1000 TIMES TO THE VICTIM `[“ldap://victim1.com:80”, “ldap://victim1.com:80”, …]`

**36**

## Slide 40

**From DoS to DDoS challenge – Not so easy** `CheckForExistingReferral()` – Checks for duplicate referrals

**37**

## Slide 41

###### **DIFFERENT DOMAIN ≠ DIFFERENT IP**

DNS Record:

Referrals:

\```
*.attacker-domain.com == 123.123.123.123
\```

\```
[
“ldap://a.attacker-domain.com:80”,
“ldap://b.attacker-domain.com:80,
…
]
\```

**38**

## Slide 42

**39**

## Slide 43

##### **Win-DDoS**

###### Attacker

Domain Controller

DsrGetDcNameEx2()

Forces the DC to become the attacker’s CLDAP client

**40**

## Slide 44

##### **Win-DDoS**

Attacker’s CLDAP Server

CLDAP Query

Domain Controller

**41**

## Slide 45

##### **Win-DDoS**

CLDAP Query
Attacker’s
CLDAP
Server
(UDP)
Referral to Attacker’s LDAP Server

Domain
Controller

**42**

## Slide 46

##### **Win-DDoS**

Attacker’s LDAP Server (TCP)

LDAP Query

Domain Controller

**43**

## Slide 47

Attacker’s
LDAP Server
(TCP)

Win-DDoS
LDAP Query
Huge referral list – pointing
to the DDoS victim

Domain
Controller

**44**

## Slide 48

##### **Win-DDoS**

Victim

LDAP Query
TCP RST

Domain
Controller

**45**

## Slide 49

SM1

Win-DDoS
LDAP Query
TCP RST
Domain
Victim
Controller
LDAP Query
TCP RST

**46**

## Slide 50

**Slide 46**

###### **SM1** הוספת שקף סיכום או לשים באותו אחד ולהתמקד

Shahak Morag, 2025-07-03T09:51:02.422

## Slide 51

###### **Win-DDoS DEMO**

**47**


> Recovered by OCR — confidence 69/100 on the text kept, 57/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Win-DDoS DEMO
File Edt View Go Capture Analyze Statistics Telephony Wireless Tools Help
Server is listening on 0.0.0.0 : 80 = @ x ry = seiBeean
Tipadar == 192168187 and eppon == 8
No. Time Source Destination Protocol Lengt! Info
| File a meso ver Hee Domain Controller #3 File _ Mee iw He . Domain Controller #2
i Capturing fror t = o x A Capturing from Ethemet ad o x
ip.adde == 192.168.187 and tepport == Tacs -)+ ipaddr == 192.168.1.87 and tep.port == 80 +
No. Time source Destination Protocol Lengt info No. Time source Destination Protocol Leng info
```

## Slide 52

**SM** 213

**Win-DDoS - THE IDEAL DDoS High bandwidth**

**48**

## Slide 53

**Slide 48**

###### **SM1** Split this slide Shahak Morag, 2025-06-24T11:33:36.956

**SM2** להוסיף תמונה של קפיצה לגובה עם בר נמוך או בריצפה עם תמונה של סבתא מצליחה את זה. Shahak Morag, 2025-07-03T09:53:02.528 **SM3** להוסיף שקף הפרדה. Shahak Morag, 2025-07-03T09:54:53.665

## Slide 54

**SM** 213

**Win-DDoS - THE IDEAL DDoS**

**High bandwidth No Cost**

**49**

## Slide 55

**Slide 49**

###### **SM1** Split this slide Shahak Morag, 2025-06-24T11:33:36.956

**SM2** להוסיף תמונה של קפיצה לגובה עם בר נמוך או בריצפה עם תמונה של סבתא מצליחה את זה. Shahak Morag, 2025-07-03T09:53:02.528 **SM3** להוסיף שקף הפרדה. Shahak Morag, 2025-07-03T09:54:53.665

## Slide 56

**SM** 213

**Win-DDoS - THE IDEAL DDoS High bandwidth No Cost No Compromised Bots**

**50**

## Slide 57

**Slide 50**

###### **SM1** Split this slide Shahak Morag, 2025-06-24T11:33:36.956

**SM2** להוסיף תמונה של קפיצה לגובה עם בר נמוך או בריצפה עם תמונה של סבתא מצליחה את זה. Shahak Morag, 2025-07-03T09:53:02.528 **SM3** להוסיף שקף הפרדה. Shahak Morag, 2025-07-03T09:54:53.665

## Slide 58

SM3

###### **Win-DDoS - LOWERING THE BAR**

**SM 51**

## Slide 59

**Slide 51**

###### **SM1** Split this slide Shahak Morag, 2025-06-24T11:33:36.956

**SM2** להוסיף תמונה של קפיצה לגובה עם בר נמוך או בריצפה עם תמונה של סבתא מצליחה את זה. Shahak Morag, 2025-07-03T09:53:02.528 **SM3** להוסיף שקף הפרדה. Shahak Morag, 2025-07-03T09:54:53.665

## Slide 60

###### **WHAT WE ACHIEVED**

Win-DDoS with LDAP

Where we are going: Win-DoS

**52**

## Slide 61

**WHAT WILL HAPPEN IF WE WILL USE TOO MANY REFERRALS?**

**53**

## Slide 62

###### **TCP vs UDP**

**54**

## Slide 63

SM1

###### **POTENTIAL REFERRAL OVERFLOW RAPID HUGE ALLOCATIONS**

**If you were Microsoft how many referrals would you allow?**

**55**

## Slide 64

**Slide 55**

**SM1** לערב את הקהל אם הייתםmicrosoft  וככה הלאה1000 ,10 .כמה הייתם נותנים. all you can it. Shahak Morag, 2025-07-03T09:56:17.340

## Slide 65

SM1

###### **POTENTIAL REFERRAL OVERFLOW RAPID HUGE ALLOCATIONS**

10?

**If you were Microsoft how many referrals would you allow?**

**56**

## Slide 66

**Slide 56**

**SM1** לערב את הקהל אם הייתםmicrosoft  וככה הלאה1000 ,10 .כמה הייתם נותנים. all you can it. Shahak Morag, 2025-07-03T09:56:17.340

## Slide 67

SM1

###### **POTENTIAL REFERRAL OVERFLOW RAPID HUGE ALLOCATIONS**

**10?**

**If you were Microsoft how many referrals would you allow? 1,000?**

**57**

## Slide 68

**Slide 57**

**SM1** לערב את הקהל אם הייתםmicrosoft  וככה הלאה1000 ,10 .כמה הייתם נותנים. all you can it. Shahak Morag, 2025-07-03T09:56:17.340

## Slide 69

SM1

###### **POTENTIAL REFERRAL OVERFLOW RAPID HUGE ALLOCATIONS**

**10,000?**

10?

**If you were Microsoft how many referrals would you allow? 1,000?**

**58**

## Slide 70

**Slide 58**

**SM1** לערב את הקהל אם הייתםmicrosoft  וככה הלאה1000 ,10 .כמה הייתם נותנים. all you can it. Shahak Morag, 2025-07-03T09:56:17.340

## Slide 71

SM1

**As far as we tested – no limit on referral URL amount. No size restrictions per URL.**

**ALL YOU CAN EAT!**

**59**

## Slide 72

**Slide 59**

**SM1** לערב את הקהל אם הייתםmicrosoft  וככה הלאה1000 ,10 .כמה הייתם נותנים. all you can it. Shahak Morag, 2025-07-03T09:56:17.340

## Slide 73

###### **REFERRAL OVERFLOW**

**FA I LURE**

**FA I LURE**

**FA I LUR E**

**TRY ldap://url1.com**

**TRY ldap://url2.com**

**TRY ldap://url3.com**

**FREE REFERRAL LIST**

List release happens only when Domain Controllers hits the end

**60**

## Slide 74

##### **REFERRAL OVERFLOW**

List release happens only when Domain Controllers hits the end

**61**

## Slide 75

###### **Growing Memory consumption → BSOD / Death of Lsass CVE-2025-32724**

**62**


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Growing Memory consumption —
BSOD / Death of Lsass
CVE-2025-32724
Your device ran into a problem and needs to restart. We're just
collecting some error info, and then we'll restart for you.
50% complete
nN about this issue and possible fixes, visit https://www.windows.c«
62
```

## Slide 76

If we can create DoS with volume, we might do more…

Moving from LDAP to RPC

**63**

## Slide 77

###### **WHAT WE ACHIEVED**

Win-DDoS with LDAP Win-DoS with LDAP

Where we are going: Win-DoS with RPC

**64**

## Slide 78

HUNTING FOR
DOS IN RPC

65

## Slide 79

**HUNTING CRITERIA** WE SEARCHED FOR:

1. RPC over TCP/SMB.

2. Remote-Exposed RPC.

3. Unauthenticated/Low Privileged Access.

**66**

## Slide 80

**HUNTING CRITERIA** WE SELECTED ONES WITH: 1. Interfaces of critical processes.

**67**

## Slide 81

**HUNTING CRITERIA** WE SELECTED ONES WITH:

1. Interfaces of critical processes.

2. Large-numeric or big-length parameters.

**68**

## Slide 82

**69**

## Slide 83

###### **RPC BIND - THE HANDSHAKE OF RPC**

Bind two options:

Accept:

Bind Request to <UUID> Bind Ack: accept

R P C C L I E N T

**R P C S E R V E R**

Reject:

Bind Request to <UUID> Bind Ack: reject **R P C C L I E N T**

**R P C S E R V E R**

**70**

## Slide 84

###### **SKIP THE BIND ACK WAIT**

###### Normal flow:

R P C C L I E N T

Bind
Bind Ack
Call
R P C S E R V E R

###### Optimized flow:

Bind + Call
Bind Ack
R P C C L I E N T R P C S E R V E R

**71**

## Slide 85

###### **STATELESS RPC: ONE-PACKET, NO-WAIT**

**Sending pre-built packets**

**Bind + RPC call in a single packet**

**No wait for Bind Ack**

**72**

## Slide 86

###### **STATELESS RPC IMPACT**

Bind + Call #1
Bind + Call #2
RPC CLIENT RPC SERVER
Bind + Call #10000

**73**

## Slide 87

**CANDIDATE #1: DsrAddressToSiteNamesW** Critical process ( `Lsass, NetLogon Interface` ). Available on DCs. Unauthenticated. Controllable size parameter: `EntryCount` .

**74**

## Slide 88

_The maximum value for EntryCount is 32000._ **_The limit was chosen to prevent clients from being able to force large memory allocations on servers._**

**75**

## Slide 89

`DsrAddressToSiteNamesW` **Bug CVE-2025-49716**

8 bytes

**Socket Address Size**

32,000

**Max Entry Count**

30,000 **# Stateless Calls**

7.7GB ≈

**Exhausted Memory**

**76**

## Slide 90

###### **WHAT WE ACHIEVED**

Win-DDoS with LDAP Win-DoS with LDAP Win-DoS with RPC #1

Where we are going: More Win-DoS with RPC

**77**

## Slide 91

# We wanted even more!

**78**

## Slide 92

SM1

## WHAT IF WE CAN MAKE THE SAME EFFECT AS DDOS?

**79**

## Slide 93

###### **Slide 79**

|**SM1**
למה הזיכרון עולה למרות שישFREE בסוף הקוד של הRPC CALL?
אולי בגלל שCALLS חדשים מתועדפים על נוכחיים
למה צריך אתTORPEDOS?
1.  חייבים להעלות את הזיכרון באופן מהיר כדי לגרום למערכת הפעלה לקרוס בכך שהיא לא תרשום את הדפים לדיסק|
|---|
|מספיק מהר.
לעשות סרטון שממחיש|
|Shahak Morag, 2025-06-23T14:19:09.357|

## Slide 94

###### **IDENTIFYING THE ENTIRE BOTTLENECK IN RPC**

1 Bind
3
Bind
2 Ack waiting
Processing
Bind Ack
RPC CLIENT RPC SERVER

## Slide 95

###### **GET RID OF THE BOTTLENECK**

Phase 1:

Phase 2:

**R P C C L I E N T**

R P C C L I E N T

Bind #1 Bind #2 Bind #100

Call #1
Call #2
Call #100

**R P C S E R V E R**

R P C S E R V E R

**81**

## Slide 96

###### **MAX BINDINGS BEFORE CONNECTION TIMEOUT**

###### Phase 1:

Bind #1
Bind #2
Bind #?
RPC CLIENT RPC SERVER

We tested **10 minutes** at least before timeout!

**82**

## Slide 97

###### **TorpeDoS - A Single-Computer DDoS**

VI C T I M S ER VER

**83**

## Slide 98

###### **TorpeDoS – A SINGLE-COMPUTER DDoS**

**84**

## Slide 99

###### **TorpeDoS - Pipes vs TCP Interfaces**

SMB Pipes:

**R P C C L I E N T**

Bind #1 Bind #2 Bind #20

**R P C S E R V E R**

TCP:

Bind #1 Bind #2 Bind #INFINITY **R P C C L I E N T**

**R P C S E R V E R**

**85**

## Slide 100

**CANDIDATE #2: NetrServerReqChallenge** Belongs to critical process ( `Lsass, NetLogon Interface` ). Available on DCs. Unauthenticated. Controllable sized parameter: `ComputerName` .

**86**

## Slide 101

###### **NetrServerReqChallenge – Challenge Insertion**

\```
NLInsertChallenge
\```

Insert

Challenges

**87**

## Slide 102

###### **DoS enemy – NLScavangeOldChallenges**

NLScav angeOldChallenges

New Challenges Release Old Challenges Challenges **88**

## Slide 103

NetrServerReqChallenge Bug
CVE-2025-26673

Normal Flow:
2 minutes
You have 2 minutes, Go!
Bind  Bind
Bind Call Bind Call
Ack Ack

TorpeDoS Flow:
2 minutes
You have 2 minutes, Go!
Ca l l Call Ca l l Ca ll Ca ll C a ll

**89**

## Slide 104

###### **WHAT WE ACHIEVED**

Win-DDoS with LDAP Win-DoS with LDAP Win-DoS with RPC #1 Win-DoS with RPC #2

Where we are going: Windows 11 Win-DoS with RPC

**90**

## Slide 105

###### **We wanted to dream even**

**91**

## Slide 106

WHAT IF WE COULD CRASH ANYTHING?

92

## Slide 107

###### **RPC INTERFACES IN WINDOWS ENDPOINT**

RPC interfaces required authentication on Windows 11

**93**

## Slide 108

**SERVER & ENDPOINT CANDIDATE #1: NetrWkstaTransportEnum** Belongs to critical process ( `wkssvc.dll` ). Available on all computers. Low privileged user call.

Controllable sized parameter: `PreferredMaximumLength` .

**94**

## Slide 109

###### **SERVER & ENDPOINT CANDIDATE #1: NetrWkstaTransportEnum**

\```
OutputBuffer=(PrefferedMaximumLength+1)+0xFFFFFFFE;
result=LocalAlloc(LMEM_ZEROINIT,OutputBuffer);
\```

**95**

## Slide 110

###### **GENERIC CANDIDATE #1: Failure Cause**

1. We called `LocalAlloc` .

2. Pages had `MEM_COMMIT` flag.

3. `MEM_COMMIT` make Windows allocate pages only on the first accessed.

**96**

## Slide 111

## **DEVELOPERS OVER TRUST CLIENTS!**

**97**

## Slide 112

**WHAT DO YOU DO WHEN YOU ARE STUCK?**

**98**

## Slide 113

## WE GO TO THE POOL!

**99**

## Slide 114

###### **Slide 99**

|**SM1**
למה הזיכרון עולה למרות שישFREE בסוף הקוד של הRPC CALL?
אולי בגלל שCALLS חדשים מתועדפים על נוכחיים
למה צריך אתTORPEDOS?
1.  חייבים להעלות את הזיכרון באופן מהיר כדי לגרום למערכת הפעלה לקרוס בכך שהיא לא תרשום את הדפים לדיסק|
|---|
|מספיק מהר.
לעשות סרטון שממחיש|
|Shahak Morag, 2025-06-23T14:19:09.357|

## Slide 115

## **Go to** `spoolsv.exe` **!**

**100**

## Slide 116

SM1

**GENERIC CANDIDATE #2: RpcEnumPrinters** Belongs to critical process ( `spooler.exe` ). Available on all computers. Low privileged user call. Controllable sized parameter: `Name` .

**101**

## Slide 117

###### **Slide 101**

###### **SM1** ניגשים ל,לרשום מה לעשות כשתקועיםspoolsv.

Shahak Morag, 2025-07-03T10:13:32.706

## Slide 118

###### **AUTHENTICATED RPC PROBLEM**

Unauthenticated RPC call:

Call packet

Authenticated RPC call:

Call packet

Previous Steps based signing

**102**

## Slide 119

###### **AUTHENTICATED RPC PROBLEM**

Unauthenticated RPC call packet

Call packet

Call packet

Signature Based on Previous Steps

Authenticated RPC call packet

**103**

## Slide 120

###### **AUTHENTICATED TorpeDoS**

Bind all connections

NTLM sign Execute pre-built calls packets

**104**

## Slide 121

###### **Spoolsv RPC DoS (CVE-2025-49722)**

**105**


> Recovered by OCR — confidence 83/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Spoolsv RPC DoS (CVE-2025-49722)
DWORD RpcEnumPrinters(
[in] DWORD Flags,
[in, string, unique] STRING HANDLE} Name,
[in] DWORD Level,
[in, out, unique, size _is(cbBuf), disable consistency_check ]
BYTE* pPrinterEnum,
[in] DWORD cbBuf,
[out] DWORD* pcbNeeded,
[out] DWORD* pcReturned
105
```

## Slide 122

SM1

**Finally, a single user can crash all Windows machines in a domain!**

**106**

## Slide 123

###### **Slide 106**

**SM1** להוסיףmission accomplished Shahak Morag, 2025-07-03T10:15:41.379

## Slide 124

###### **Win-DoS DEMO - CRASHING WINDOWS 11**

**107**


> Recovered by OCR — confidence 83/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Win-DoS DEMO - CRASHING WINDOWS I1
2) command Prompt X BRD Windows PowerShell
€:\Users\shaha>ping ~t 192.168.136.70 Stop recording
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved
Install the Latest PowerShell for new features and improvements! https: //aka.ms/PSwindows
PS C:\Users\Administrator> ipconfig
Windows IP Configuration
Ethernet adapter Ethernet
Connection-specific DNS Suffix mshone.net
Link-Local IPv6 Address 80: :ce63:cc99: c653:3b99%8
Subnet Mask 255.255.2U0.0
Default Gateway 192.168.128.1
Ps C:\Users\Administrator>
107
```

## Slide 125

###### **WHAT WE ACHIEVED**

Win-DDoS with LDAP Win-DoS with LDAP Win-DoS with RPC #1

Win-DoS with RPC #2 Windows 11 Win-DoS with RPC

**108**

## Slide 126

SM1

###### **4 NEW DoS VULNERABILITIES DISCOVERY SUMMARY**

|Name|CVE|Developer
Blind Spot|Bypass
Concept|Privilege
Required|Target|
|---|---|---|---|---|---|
|Referral Overflow|CVE-2025-32724|Remote
triggered client|Not required|Anonymous|DC|
|NetLogon DoS #1|CVE-2025-26673|Transport-agnostic
wrapped server|TorpeDoS|Anonymous|DC|
|NetLogon DoS #2|CVE-2025-49716|Transport-agnostic
wrapped server|Stateless RPC|Anonymous|DC|
|DoS
SpoolSv|CVE-2025-49722|Transport-agnostic
wrapped server|TorpeDoS|Weak User|All
Computers|

**109**

## Slide 127

###### **Slide 109**

###### **SM1** אולי טבלה או עיצוב אחר

Shahak Morag, 2025-07-03T10:16:26.131

## Slide 128

###### **DDoS and DoS ARE REAL WORLD RISKS**

Money Loss Medical Equipment Political Damage Incidents

**110**

## Slide 129

#### **TAKEAWAYS**

Any code that can be remotely triggered can be vulnerable to concurrency and resource abuse, even if it’s intended to communicate with only a single entity

**111**

## Slide 130

###### **TAKEAWAYS**

Organizations must assume that all their servers and endpoints can be targeted for DDoS attacks whether they are public facing or not.

**VI C T I M S ER VE R**

**112**

## Slide 131

###### **TAKEAWAYS**

Server to client transformation should be extremely carefully handled as it has multiple security risks

CLDAP Client

R P C C A L L

Domain Q U E R Y Controller

CLDAP Server **113**

## Slide 132

### **THE Win-DoS EPIDEMIC HAS BEGUN**

**114**

## Slide 133

### **GitHub + Q&A**

@oryair1999

www.linkedin.com/in/or-yair/

@ShahakMo www.linkedin.com/in/shahak-morag-6bb51b142/

https://github.com/SafeBreach-Labs/Win-DoS

**115**
