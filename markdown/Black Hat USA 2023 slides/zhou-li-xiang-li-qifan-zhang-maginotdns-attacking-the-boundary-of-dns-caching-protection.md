---
title: "MaginotDNS Attacking the Boundary of DNS Caching Protection"
speakers: ["Zhou Li", "Xiang Li", "Qifan Zhang"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/Zhou Li & Xiang Li & Qifan Zhang_MaginotDNS Attacking the Boundary of DNS Caching Protection.pdf"
pages: 41
sha256: "e8e177ee8f8c0b3bf51b80fc596861f08ae7cdefe6632f212a692c06f763c606"
text_chars: 16500
ocr_pages: 1
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:28:07Z"
---
# MaginotDNS Attacking the Boundary of DNS Caching Protection

**Speakers:** Zhou Li, Xiang Li, Qifan Zhang  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Zhou Li & Xiang Li & Qifan Zhang_MaginotDNS Attacking the Boundary of DNS Caching Protection.pdf` (41 pages)


## Slide 1

# MaginotDNS: Attacking the Boundary of DNS Caching Protection

Speaker(s): Zhou Li

Contributor(s): Xiang Li and Qifan Zhang August 2023

#BHUSA  #THU  #UCI  @BlackHatEvents

## Slide 2

## **MaginotDNS**

### About Us

Zhou Li Assistant Professor at UC Irvine Research interests: DNS, Graph Security analytics (GSA), …

Xiang Li PhD at Tsinghua University

Qifan Zhang PhD at UC Irvine

#BHUSA #THU  #UCI  @BlackHatEvents

2

## Slide 3

## **MaginotDNS**

Attack Impact **Our MaginotDNS attack could poison a whole TLD, e.g., .com, at one round. All domains under that TLD can be hijacked.**

#BHUSA #THU  #UCI  @BlackHatEvents

3

## Slide 4

## **MaginotDNS**

### Outline

####  **DNS overview**

 **DNS cache poisoning**

 **MaginotDNS workflow**

 **Attack demo**

 **Large-scale scanning**

 **Discussion & conclusion**

#BHUSA #THU  #UCI  @BlackHatEvents

4

## Slide 5

## **MaginotDNS**

### Domain Name System (DNS)

#####  **DNS Overview**

- Translating domain names to IP addresses

- Entry point of many Internet activities

- Domain names are widely registered

Web

CDN

Email Certificate

example.com
93.184.216.34

DNS

Cited from verisign.com/dnib

#BHUSA #THU  #UCI  @BlackHatEvents

5

## Slide 6

## **MaginotDNS**

### DNS Resolution

#####  **Resolution Process**

- Primarily over UDP

 Iterative and recursive

DNS namespace
3 Query
Root
example.com .
Referral to TLD NS 4
Query Query
Delegate
1 2 5 Query
TLD
example.com com net
10 9
Referral to SLD NS 6
DNS Forw- Recursive
Authoritative
client arder resolver Delegate
servers
Response 7 Query  SLD
example.com example
Authoritative answer 8

 Record caching

#BHUSA #THU  #UCI  @BlackHatEvents

7

## Slide 7

## **MaginotDNS**

### Outline

 **DNS overview**

- **DNS cache poisoning**

 **MaginotDNS workflow**

- **Attack demo**

- **Large-scale scanning**

 **Discussion & conclusion**

#BHUSA #THU  #UCI  @BlackHatEvents

8

## Slide 8

## **MaginotDNS**

### DNS Cache Poisoning

#####  **Target**

Attack on
resolvers’ cache’ cache
Forwarders
Kaminsky
Attack
Attack via Attack via
Kashpureff
Attack Escaped Escaped
Chars Chars v2
2002 2013 2020 2021
1997 2008 2020 2021 2022
Birthday SADDNS v2
Attack
Attack
Fragmentation
Attack
SADDNS
Attack

 Injecting forged answers into resolvers’ cache’ cache

- **Taxonomy**

 On-path, off-path

 **Technique**

 Cat-and-mouse game

#BHUSA #THU  #UCI  @BlackHatEvents

11

## Slide 9

## **MaginotDNS**

#BHUSA #THU  #UCI  @BlackHatEvents

12

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 2&0e25
Unpatched DNS Bug Puts Millions of
Routers, loT Devices at Risk
—y
DNS cache poisoning, the Internet attack
from 2008, is back from the dead
Anewly found side channel in a widely used protocol lets attackers spoof domains.
©
72% of organizations hit by DNS
attacks in the past year
GOODIN - 11/12/2020, 6:30 AM
- webpage
```

## Slide 10

## **MaginotDNS**

### On-path DNS Cache Poisoning

 **Kashpureff Attack (on-path, 1997)**

 Method: returning forged responses from the authoritative

 Result: resolver accepting all records in the response

 Cause: lacking data verification ( **bailiwick rules** )

Step1: Recursive query for
Cache
www.alternic.net/A
Step 2: Iterative query for
Evil client ISP resolver
www.alternic.net/A
Step 4: Step 5:
Recursive query for Bogus
www.internic.net/A Response
Step 3: Response including bogus
www.internic.net/NS RR
“alternic.net”
Unsuspecting
Authoritative
server
Server
13

#BHUSA #THU  #UCI  @BlackHatEvents

## Slide 11

## **MaginotDNS**

### DNS Bailiwick Rules

- **Mitigating the Kashpureff Attack**

   - Record validation when storing cache entries

   - Checking for “ **in bailiwick** ” in response data: **answer records must be from the same domain as the requested name**

   - $ dig example.com Bailiwick

;; ANSWER SECTION: In-bailiwick example.com. 86400 IN A 93.184.216.34 Can be trusted ;; AUTHORITY SECTION: ~~mybank.com. 86400 IN NS ns.mybank.com.~~ **Out-of-bailiwick** ;; ADDITIONAL SECTION: **Should be removed** ~~ns.mybank.com. 86400 IN A 1.2.3.4~~

#BHUSA #THU  #UCI  @BlackHatEvents

14

## Slide 12

## **MaginotDNS**

### Takeaway

**After the Kashpureff attack, bailiwick checking is integrated into the resolver’s implementation,**

DNS cache poisoning on recursives from the on-path seems **impossible** to conduct from 1997.

#BHUSA #THU  #UCI  @BlackHatEvents

15

## Slide 13

## **MaginotDNS**

### Off-path DNS Cache Poisoning

 **Kaminsky Attack (Off-path, 2008)**

 Method: injecting forged responses with the birthday attack

 Result: resolver accepting glue records in the response

 Cause: lacking **source port randomization** (TXID only 16 bits)

Step 1: Recursive query for **www123.mybank.com/A** Step 2: **TXID=1001** : Iterative query for Evil client **www123.mybank.com/A**

Step 4: Response If TXID not matching, **TXID=1001** www123.mybank.com A? start the attack again “mybank.com” (empty) with another Authoritative mybank.com NS ns.mybank.com Server ns.mybank.com A **1.1.1.1** www456.mybank.com

If TXID matching, **Cache** success! ISP resolver Step 3: Response TXID=XXXX www123.mybank.com A? (empty) mybank.com NS ns.mybank.com ns.mybank.com A **6.6.6.6** Unsuspecting server

#BHUSA #THU  #UCI  @BlackHatEvents

16

## Slide 14

## **MaginotDNS**

### DNS Source Port/TXID Randomization

- **Mitigating the Kaminsky Attack**

   - Increasing the query guessing entropy

   - 16-bit source port x 16-bit TXID = 32-bit space

   - **Hard to brute force**

6 5 5 3 6 6 5 5 3 6
Source port TXID

#BHUSA #THU  #UCI  @BlackHatEvents

17

## Slide 15

## **MaginotDNS**

### Takeaway

**After the Kaminsky attack, source port randomization is integrated into the resolver’s implementation,**

DNS cache poisoning on resolvers from the off-path became **difficult** to conduct from 2008.

#BHUSA #THU  #UCI  @BlackHatEvents

18

## Slide 16

## **MaginotDNS**

### Outline

 **DNS overview**

 **DNS cache poisoning**

####  **MaginotDNS workflow**

 **Attack demo**

 **Large-scale scanning**

 **Discussion & conclusion**

#BHUSA #THU  #UCI  @BlackHatEvents

19

## Slide 17

## **MaginotDNS**

### Question

#### **Are bailiwick checking and port randomization good enough?**

No. **MaginotDNS** breaks this guarantee with a new powerful **cache poisoning vulnerability** .

#BHUSA #THU  #UCI  @BlackHatEvents

20

## Slide 18

## **MaginotDNS**

### MaginotDNS Attack

- **What is the MaginotDNS attack**

   - A new powerful DNS cache poisoning attack against **CDNS resolvers**

   - Can be launched from either **on-path** or **off-path**

   - Can poison **arbitrary domains** including **TLDs** , such as .com and .net

- **Name**

   - Exploiting **vulnerabilities** of bailiwick checking to bypass itself

   - Working like breaking the **Maginot Line**  **MaginotDNS**

#BHUSA #THU  #UCI  @BlackHatEvents

21

## Slide 19

## **MaginotDNS**

### Question

#### **What is the CDNS resolver?**

A **conditional DNS resolver** with both **recursive** and **forwarding** query modes.

#BHUSA #THU  #UCI  @BlackHatEvents

22

## Slide 20

## **MaginotDNS**

### DNS Resolvers

 **Worldwide**

 Worldwide
Client-side Server-side
 Multiple Roles
ODNS
 Recursive, forwarder
RDNS
ADNS
 Hidden DNS (HDNS)
FDNS
 Complex Interaction
𝐑 𝐑 𝐑 𝐑 𝐢𝐢
𝐑 𝐑 𝐑 𝐑 𝐝𝐝
 CDNS
FDNS
 One of HDNSes
FDNS HDNS ODNS: open resolver
 Never been studied FDNS: forwarder
RDNS: recursive resolver
Client
HDNS: hidden resolver
ADNS: authoritative server

#BHUSA #THU  #UCI  @BlackHatEvents

23

## Slide 21

## **MaginotDNS**

### Attack Target: CDNS

#####  **Conditional DNS Resolver (CDNS)**

- Forwarder + recursive resolver (shared cache)

- 2 query zones used for different resolution `o` 𝑍𝑍𝐹𝐹 : domains for forwarding queries

- **Usage Scenarios** `o` 𝑍𝑍𝑅𝑅 : domains for recursive queries

Internal Network Internet
CDNS Public queries
(google.com, etc.)
Google’s
Query 8.8.8.8
Local queries
(mail.local, etc.) Public
Forwarding
Local
Resolver Local
Clients
Recursive

- **Usage Scenarios**

   - Enterprise: splitting networks

   - ISP: reducing heavy traffic cost

#BHUSA #THU  #UCI  @BlackHatEvents

24

## Slide 22

## **MaginotDNS**

   - Attack Overview of MaginotDNS

   - **Threat Model**  Attacking the forwarding mode  Assuming we discovered a CDNS and inferred its 𝑍𝑍𝐹𝐹 & 𝑍𝑍𝑅𝑅

- **Threat Model**

- **Why forwarding mode?**

   - Bailiwick checking of the recursive mode is well enforced

   - But the forwarder mode is not

   - Since they share the same global DNS cache

   - We can exploit the weak forwarder mode to attack the well-protected recursive mode `o`  Breaking the boundary of DNS cache protection

#BHUSA #THU  #UCI  @BlackHatEvents

25

## Slide 23

## **MaginotDNS**

### Software Analysis

#####  **Finding Vulnerable Software**

- In depth **bailiwick checking implementation** analysis

- Via source code review, debugging, and testing

 8 mainstream DNS software, e.g., BIND and Microsoft DNS

Knot

PowerDNS

Unbound

**Inconsistent bailiwick checking implementations**

BIND

#BHUSA #THU  #UCI  @BlackHatEvents

26

## Slide 24

## **MaginotDNS**

### Root Cause & Vulnerable Software

#####  **General Bailiwick Checking Logic**

 Summarized by us

 **Root Cause**

 In the `InitQuery` function:

`o Qry.zone` is set to root  all records is **in-bailiwick** (root’s subdomains)

 **Vulnerable Software**

|**DNS Software**|**Forwarding**|**Recursive**|**Vulnerable**|
|---|---|---|---|
|**BIND9**|Enabled|Enabled|**Yes**|
|**Knot Resolver**|Enabled|Enabled|**Yes**|
|**Microsoft DNS**|Enabled|Enabled|**Yes**|
|**Technitium**|Enabled|Enabled|**Yes**|

#BHUSA #THU  #UCI  @BlackHatEvents

27

## Slide 25

## **MaginotDNS**

### Bailiwick Checking (Done Right)

example.com
example.com
Recursive  NS
Cache
Client Resolver google.com
whitehouse.gov
Query zone : example.com
Records under example.com

#BHUSA #THU  #UCI  @BlackHatEvents

29

## Slide 26

## **MaginotDNS**

### Bailiwick Checking (Done Wrong)

Forwarding zone: example.com

Recursive zone: {domains}-example.com

example.com
example.com
Forwarding zone
Forwarder CDNS Upstream servers
Client
Cache
Query zone* :  .root
Records under example.com
google.com
google.com, whitehouse.gov
Recursive zone
Shared Cache
Query zone* :  .root
Resolver Cache
Records under example.com
google.com, whitehouse.gov

#BHUSA #THU  #UCI  @BlackHatEvents

30

## Slide 27

## **MaginotDNS**

### Attack Steps of MaginotDNS (On-path)

 Returning fake responses **directly**

 **BIND, Microsoft DNS, Knot, and Technitium**

Attacker Conditional Upstream Authoritative Server
DNS Server DNS Server (attacker.com)
1 Fwding
2 3 attacker.com
Match fwd zone
On
𝑸𝑸 : attacker.com 4
path
Return  𝑹𝑹
com. NS
Cached
ns1.rogue-tld-ns.org.
𝑹𝑹

#BHUSA #THU  #UCI  @BlackHatEvents

31

## Slide 28

## **MaginotDNS**

### Attack Steps of MaginotDNS (Off-path)

 Guessing source
port & TXID
 Microsoft: new  Attacker Conditional Upstream Authoritative Server
DNS Server DNS Server (attacker.com)
port vulnerability
1
Fwding : sport=x, txid=y
 BIND9: using the
2 Match fwd zone 3 attacker.com Recursive
SADDNS attack
𝑸 : attacker.com 𝑸
Off 4
path
Guess dport & txid for  𝑹𝑹
𝑸 : attacker.com 𝑸
Cached
dport=x, txid=y
…… Control the
com. NS
reply time
ns1.rogue-tld-ns.org.
𝑹𝑹
𝑹𝑹
32 𝑹𝑹 #BHUSA #THU  #UCI  @BlackHatEvents

32

## Slide 29

## **MaginotDNS**

### Off-path Attack on BIND9

- **Guessing Source Port**

   - We use SADDNS to infer the source port

   - ICMP rate-limit side-channel (check the SADDNS paper for details)

- **Brute-forcing TXID**

- **Attack analysis**

   - Source port range: 32,768 - 60,999 (28,232)

   - Query timeout: 1.2s, guessing 50 ports each round

   - **Success rate** after 3,600 rounds:

      - 1 −[(28,232 −50)/28,232]<sup>3,600</sup> = 99.8%

https://www.saddns.net/

SADDNS

#BHUSA #THU  #UCI  @BlackHatEvents

33

## Slide 30

## **MaginotDNS**

### Off-path Attack on Microsoft DNS

- **Guessing Source Port**

   - We found MS DNS only uses **~2,500 source ports** for resolution

   - 2,500 ports are **all in the open state** (SADDNS not working)

   - **Brute-forcing** all 2,500 ports

- **Brute-forcing TXID**

- **Attack analysis**

   - Source port range: probing in advance (2,500)

 Query timeout: 5s, guessing 20 ports each round

Source Port Range Examples of Microsoft DNS

 **Success rate** after 720 rounds:

- 1 −[(2,500 −20)/2,500]<sup>720</sup> = 99.7%

#BHUSA #THU  #UCI  @BlackHatEvents

34

## Slide 31

## **MaginotDNS**

### Outline

 **DNS overview**

 **DNS cache poisoning**

 **MaginotDNS workflow**

 **Attack demo**

 **Large-scale scanning**

 **Discussion & conclusion**

#BHUSA #THU  #UCI  @BlackHatEvents

35

## Slide 32

## **MaginotDNS**

### MaginotDNS Attack Demos

 **On-path Attack**

- The result is determinative

 Off-path Attack

- Microsoft: **avg. 802s**

- BIND9: **avg. 790s**

Watch videos here.

Log of Attacking Microsoft

Log of Attacking BIND9

#BHUSA #THU  #UCI  @BlackHatEvents

36

## Slide 33

## **MaginotDNS**

MaginotDNS Attack Demos

#####  **Off-path Attacks on BIND9 & Microsoft DNS**

BIND9

Microsoft DNS

#BHUSA #THU  #UCI  @BlackHatEvents

37

## Slide 34

## **MaginotDNS**

### Outline

 **DNS overview**

 **DNS cache poisoning**

 **MaginotDNS workflow**

 **Attack demo**

- **Large-scale scanning**

 **Discussion & conclusion**

#BHUSA #THU  #UCI  @BlackHatEvents

38

## Slide 35

## **MaginotDNS**

### Finding Vulnerable CDNSes

- **Differentiating Forwarder & Recursive**

   - Based on the DNS resolution mechanism

   - **Forwarders** do not cache **intermediate NS records**

- **Finding CDNSes**

   - New methodology

      1. Targeting one resolver

      2. Testing a group of domains, sending **NS&NR** queries

      3. For some domains, no NS responses ( **forwarding** )

      4. For others, we get NS responses ( **recursive** )

Upstream Forwarder DNS Client Recursive  Authoritative
server resolver servers
DNS query 1 1 DNS query 2 Query root server
Forward 2 example.com? A example.com? A Referral to TLD NS 3
example.com? A
com. NS
Query  TLD  NS  Cached a.gtld-servers.net
authoritative or
3
answer from  4 Query TLD NS
local zones SLD  NS
Referral to SLD NS 5
not cached
4 Response by forwarder example.com NS
SLD  NS  cached
a.iana-servers.net
example.com A  by resolver
93.184.216.34 SLD  A  Cached 6 Query SLD NS
5 Response Response 8 Authoritative answer 7
93.184.216.34 93.184.216.34 example.com A
SLD  A  Cached 93.184.216.34
Cache probe 6 9 Cache probe
example.com? example.com?
NS +norecurse NS +norecurse
7 Response Response 10
(Empty) a.iana-servers.net

5. The resolver does **both forwarding & recursive resolution**

6.  **CDNS identified**

#BHUSA #THU  #UCI  @BlackHatEvents

39

## Slide 36

## **MaginotDNS**

### Vulnerable CDNS Population

- **Measurement**

   - We collected **1.2M resolvers**

   - Removing not-applicable ones, such as violating NR or multiple caches

   - Applying our method to identify **154,955 CDNSes**

   - Using **software fingerprints** to locate **54,949 vulnerable CDNSes**

      - Resolvers with DNSSEC or 0x20 are filtered out

#BHUSA #THU  #UCI  @BlackHatEvents

40

## Slide 37

## **MaginotDNS**

### Outline

 **DNS overview**

 **DNS cache poisoning**

 **MaginotDNS workflow**

 **Attack demo**

 **Large-scale scanning**

 **Discussion & conclusion**

#BHUSA #THU  #UCI  @BlackHatEvents

41

## Slide 38

## **MaginotDNS**

### Discussion & Mitigation

- **Vulnerability Disclosure**

   - **Confirmed** and **fixed** by **all affected software** : BIND9, Knot, Microsoft, & Technitium

   - **4 CVE-ids** published & **Bounty** awarded by Microsoft

- **Root Cause**

   - Problematic forwarding bailiwick checking implementations ( `Qry.zone` <- root) `o` **Why? Forwarder needs flexibility**

   - **Mitigation Solution**  Then only records under forwarded domain are acceptable (cache split)cache split))  `Qry.zone` should be set to the forwarded domain in 𝑍𝑍𝐹𝐹 (query zone restriction)

 **Mitigation Solution**

- Then only records under forwarded domain are acceptable (cache split)cache split))

- Have been adopted by affected software

#BHUSA #THU  #UCI  @BlackHatEvents

42

## Slide 39

## **MaginotDNS**

### Black Hat Sound Bytes

- **Bailiwick checking is not bullet-proof!**

   - We thought it’s perfect after **26 years** since it’s born.

- **Inconsistent DNS implementations are common…**

   - Forwarder vs. resolver

   - BIND, Knot, Microsoft, ….

   - Partially caused by the vague RFCs

- **There might be more vulnerabilities we don’t even know …**

   - We need **automated tools** (e.g., fuzzers) customized to analyze DNS software

   - My group is working on that 

#BHUSA #THU  #UCI  @BlackHatEvents

44

## Slide 40

## **MaginotDNS**

#BHUSA #THU  #UCI  @BlackHatEvents

46

## Slide 41

## **MaginotDNS**

### Wrap-up

#### **Thanks for listening! Any questions?**

**Paper**

Zhou Li, zhou.li@uci.edu Xiang Li, <u>x-l19@mails.tsinghua.edu.cn</u> Qifan Zhang, qifan.zhang@uci.edu

**Tool**

#BHUSA #THU  #UCI  @BlackHatEvents

**47**
