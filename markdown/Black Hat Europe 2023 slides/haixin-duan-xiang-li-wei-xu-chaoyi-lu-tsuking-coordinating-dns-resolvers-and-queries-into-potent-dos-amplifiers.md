---
title: "TsuKing Coordinating DNS Resolvers and Queries into Potent DoS Amplifiers"
speakers: ["Haixin Duan", "Xiang Li", "Wei Xu", "Chaoyi Lu"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2023"
edition: "Europe"
year: 2023
source_pdf: "Black Hat Europe 2023 slides/Haixin Duan, Xiang Li, Wei Xu, Chaoyi Lu_TsuKing Coordinating DNS Resolvers and Queries into Potent DoS Amplifiers.pdf"
pages: 41
sha256: "1825aebb45bf010f46a32f57b3292084aba4167e80eaf9bbebc228d3ce94001f"
text_chars: 16274
ocr_pages: 2
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:12:07Z"
---
# TsuKing Coordinating DNS Resolvers and Queries into Potent DoS Amplifiers

**Speakers:** Haixin Duan, Xiang Li, Wei Xu, Chaoyi Lu  
**Conference:** Black Hat Europe 2023  
**Source:** `Black Hat Europe 2023 slides/Haixin Duan, Xiang Li, Wei Xu, Chaoyi Lu_TsuKing Coordinating DNS Resolvers and Queries into Potent DoS Amplifiers.pdf` (41 pages)

## Slide 1

## TsuKing: Coordinating DNS Resolvers and Queries into Potent DDoS Amplifiers

Speaker: **Haixin Duan** Slides Contributors: **Wei Xu** & **Xiang Li** & **Chaoyi Lu** Tsinghua University, Dec. 2023

#BHEU #THU @BlackHatEvents

## Slide 2

#### TsuKing: Tsunami + King

#BHEU #THU   @BlackHatEvents

2

## Slide 3

#### TsuKing: Tsunami + King

_(Traffic amplification ability)_

v Cause: DNS implementation choices & complex service infrastructure

Egress #1
(US-IAD) Amplified
query queries
DNS resolver system
Forwarder 8.8.8.8
Egress #2
(ingress) (upstream)
(US-LAX)

#BHEU #THU   @BlackHatEvents

3

## Slide 4

#### TsuKing: Tsunami + King<sup>**[1]**</sup>

_(Traffic amplification ability)_

_(Server coordination ability)_

v Cause: DNS implementation choices & complex service infrastructure

v Coordinates DNS server systems -> **3,000+** ✕ **amplification factor (** **_king_ of DoS)**

query

Egress #1 (US-IAD)

DNS resolver system Forwarder 8.8.8.8 Egress #2 (ingress) (upstream) (US-LAX)

Authoritative Name Server query **Coordination** ServerOwned by attacker Layer #1

Layer #2

Victim

[1] **King : estimating latency between arbitrary internet end hosts, ACM CCR 2002** 4

#BHEU #THU   @BlackHatEvents

## Slide 5

#### DNS resolution guided by referrals

v **Referrals** **_tell recursive resolvers who to ask next_**

**web.org A?** _(what is the address of web.org?)_

**org.    NS    b0.org.afilias-nst.org b0.org.afilias-nst.org.    A   199.19.54.1** _(I don’t know. Ask the referral, It’ll get you closer.)_

**Root server**

web.org

**Recursive Resolver e.g.8.8.8.8**

**Org TLD server** (b0.org.afilias-nst.org) **SLD authoritative server** (ns.web.com)

#BHEU #THU   @BlackHatEvents

5

## Slide 6

#### DNS resolution guided by referrals

##### v **Referrals** **_tell recursive resolvers who to ask next_**

**web.org A?** _(what is the address of web.org?)_

web.org

**Root server org.    NS    b0.org.afilias-nst.org b0.org.afilias-nst.org.    A   199.19.54.1 web.org A? Org TLD server** (b0.org.afilias-nst.org) **web.org.    NS    ns.web.org Recursive Ns.web.org A 1.2.3.4 Resolver e.g.8.8.8.8** _(I don’t know. Referral: ns.web.org. )_ **SLD authoritative server** (ns.web.org) 1.2.3.4

#BHEU #THU   @BlackHatEvents

6

## Slide 7

#### DNS resolution guided by referrals

v **Recursive DNS resolution guided by** **_referrals_**

v Referrals _tell recursive resolvers who to ask next_

web.org A?
(what is the IPv4 address of sigsac.org?)
Root server
org.    NS    b0.org.afilias-nst.org
b0.org.afilias-nst.org.    A   199.19.54.1
web.org web.org A?
Org TLD server
(b0.org.afilias-nst.org)
web.org.    NS    ns.web.org
Recursive
Resolver
e.g.8.8.8.8
web.org A?
SLD authoritative server
(ns.web.org) 1.2.3.4
web.org.    A    190.92.158.4
(Here’s your answer!)

#BHEU #THU   @BlackHatEvents

7

## Slide 8

#### Threat model of TsuKing

##### v **Attacker sends DNS query for his own domain name**

Authoritative Name server,
owned by attacker (legally)
I have no answer,
Q: attacker.com
Referral: target
Q: attacker.com
Recursive Resolver
target

#BHEU #THU   @BlackHatEvents

8

## Slide 9

#### Sounds simple, but

# **Why does a resolver amplify query traffic? Is it that powerful?**

Recursive Resolver

#BHEU #THU   @BlackHatEvents

9

## Slide 10

#### DNS as a complex infrastructure

##### v **Multiple** **_types_ and** **_layers_ of DNS servers**

v DNS forwarders ➔ pass queries to upstream _(e.g., another forwarder)_

v Large public DNS services ➔ complexes of load balancers, caches, egress servers, etc.

###### The complex DNS infrastructure

Schomp, et al. On Measuring the Client-side DNS Infrastructure, IMC 2013

#BHEU #THU   @BlackHatEvents

10

## Slide 11

#### DNS as a complex infrastructure

##### v **Multiple** **_types_ and** **_layers_ of DNS servers**

- v DNS forwarders ➔ pass queries to upstream _(e.g., another forwarder)_

- v Large public DNS services ➔ complexes of load balancers, caches, egress servers, etc.

###### The complex DNS infrastructure

Large public DNS service
(e.g., Google Public DNS)
Frontend caches Backend resolvers
Egress #1
Pick
Egress #2
cache
Anycast
Pick
Egress #3
resolver

Schomp, et al. On Measuring the Client-side DNS Infrastructure, IMC 2013

#BHEU #THU   @BlackHatEvents

11

## Slide 12

#### DNS as a complex infrastructure

##### v **Multiple** **_types_ and** **_layers_ of DNS servers**

- v DNS forwarders ➔ pass queries to upstream _(e.g., another forwarder)_

- v Large public DNS services ➔ complexes of load balancers, caches, egress servers, etc.

###### The complex DNS infrastructure

Large public DNS service
(e.g., Google Public DNS)
Frontend caches Backend resolvers
Egress #1
Pick
Egress #2
cache
Anycast
Pick
Egress #3
resolver

Schomp, et al. On Measuring the Client-side DNS Infrastructure, IMC 2013

2.27 Million

Open DNS servers

* Data from Censys,
Oct 2023

#BHEU #THU   @BlackHatEvents

12

## Slide 13

#### A typical domain name resolution path

##### v **Multiple** **_types_ and** **_layers_ of DNS servers**

v DNS forwarders ➔ pass queries to upstream _(e.g., another forwarder)_

v Large public DNS services ➔ complexes of load balancers, caches, egress servers, etc.

##### v **A** **_typical_ DNS resolution path now looks like this**

Egress #1
query pass pass pass to
load Independent
authoritative
balance caches
servers
Anycast
Egress #2
Stub resolver Forwarder Forwarder Hidden
(DNS client) (e.g., home router) (e.g., of ISP) server layers
Recursice DNS service
(e.g., 8.8.8.8)

#BHEU #THU   @BlackHatEvents

13

## Slide 14

#### DNS as a complex infrastructure

##### v **Multiple** **_types_ and** **_layers_ of DNS servers**

v DNS forwarders ➔ pass queries to upstream _(e.g., another forwarder)_

v Large public DNS services ➔ complexes of load balancers, caches, egress servers, etc.

v **A** **_typical_ DNS resolution path now looks like this**

Egress #1
query pass pass pass to
load Independent
authoritative
balance caches
servers
Anycast
Egress #2
Stub resolver Forwarder Hidden
(DNS client) (e.g., home router) server layers
Ingress server Egress point-of-presence
(Public-facing) (contacts authoritatives)

#BHEU #THU   @BlackHatEvents

14

## Slide 15

#### Definition of DNS Resolver System(DRS)

##### v **DNS resolver system (DRS)**

v A public-facing DNS server, together with everything between it and authoritative servers v **Black box inside**

DRS
Egress #1
query pass Whatever happens inside to
authoritative
(doesn’t matter) servers
Egress #2
Stub resolver Forwarder
(DNS client) (e.g., home router)
Ingress server Egress point-of-presence
(Public-facing) (contacts authoritatives)

#BHEU #THU   @BlackHatEvents

15

## Slide 16

#### DNS as a complex infrastructure

**OK, I get it. DNS resolver is a complex system.** But how is this relevant to traffic amplifcation?

#BHEU #THU   @BlackHatEvents

16

## Slide 17

#### Amplification ability: DNS retries

v **DNS query could fail for variety of reasons**

- v Packet lost, server fail, routing problems

v **So upon failure, please** **_retry_ for a few more times** v Adopted by mainstream DNS software

v **_THE amplification potential exploited by our attack_**

|**DNS software**|**# of retries**|
|---|---|
|BIND9|13|
|Unbound|9|
|Knot|3|

#BHEU #THU   @BlackHatEvents

17

## Slide 18

#### Amplification ability: DNS retries

##### v **For a DRS, retries may exit from** **_different egresses_**

- v Egress servers don’t share cache

- v Prevents _query aggregation_ and _cache hits_

DRS
SERVFAIL,
Egress #1
Timeout, …
query Whatever happens to
Independent
authoritative
caches
servers
retry
Ingress (doesn’t matter)
Egress #2  retry

#BHEU #THU   @BlackHatEvents

18

## Slide 19

#### Amplification ability: DNS retries

**Wait… You exploit retries?**

That’s not even enough to cause ripples!

#BHEU #THU   @BlackHatEvents

19

## Slide 20

#### Attack variant I: DNS-Retry

v **Some bogus DRS implementations that retry aggressively** v **In 1.3M DRS, 2.4% (>30,000) retry more than 100 times** v **529 DRSes retry more than 1,000 times**

v **Max # of retries by one DRS:** **_117,541_**

In 1.3M open DNS Resolver System(DRS)

Egress
query
Egress
Ingress

Amplification by one DRS only is big enough

|**# of retries**|**# of open DRSes**|**% of tested**|
|---|---|---|
|> 2|925,500|69.8%|
|> 10|407,581|30.7%|
|> 100|31,660|2.4%|
|**> 1,000**|**529**|**0.04%**|

#BHEU #THU   @BlackHatEvents

20

## Slide 21

#### DNS-Retry Evaluation

##### v **Evaluation in controlled environment**

- v Select 10 DRSes that retry aggresively

v Attacker sends 1.3 pkt/s ➔ **Victim receives 882 pkt/s**

Egress
query
Egress
Ingress

638 ✕ amplification

#BHEU #THU   @BlackHatEvents

21

## Slide 22

# **Alright, but lots of them are not aggressive at all. Only modest retries…**

#BHEU #THU   @BlackHatEvents

22

## Slide 23

# **Let’s** **_chain_ these ripples into bigger waves!**

23

#BHEU #THU   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
)
i
=
ca
EC e0e
f=
0
=
M
C8:
a
EWI
_ 5
| ease mzone FS
these ripples into bigger waves
mM
s cha
Let’
```

## Slide 24

#### Attack variant II: DNS-Chain

##### v **Recursive DNS resolution guided by** **_evil referrals_**

attacker.org A?

**attacker.org NS    drs2a.attacker.org**

**SLD authoritative server (ns.attacker.com)**

###### **_DRS #1_**

###### **_DRS #2a_**

Egress
attacker.org A?
Query diverted
Egress
Ingress

Ingress

#BHEU #THU   @BlackHatEvents

24

## Slide 25

#### Attack variant II: DNS-Chain

##### v **Recursive DNS resolution guided by** **_evil referrals_**

attacker.org A?

**attacker.org NS    drs2a.attacker.org**

**SLD authoritative server (ns.attacker.com)**

###### **_DRS #1_**

###### **_DRS #2a_**

Egress
attacker.org A?
Query diverted
Egress
Ingress Ingress
Will eventually fail
as controlled by
the attacker

#BHEU #THU   @BlackHatEvents

25

## Slide 26

#### Attack variant II: DNS-Chain

##### v **Recursive DNS resolution guided by** **_evil referrals_**

attacker.org A?
attacker.org NS    drs2a.attacker.org
SLD authoritative server
(Retries)  attacker.org A? (ns.attacker.com)
attacker.org NS    drs2b.attacker.org
DRS #1 DRS #2a
Egress
attacker.org A?
Egress
Ingress Ingress
(Retries)  attacker.org A?
DRS #2b
Ingress

#BHEU #THU   @BlackHatEvents

26

## Slide 27

#### Attack variant II: DNS-Chain

##### v **Recursive DNS resolution guided by** **_evil referrals_**

attacker.org A?
attacker.org NS    drs2a.attacker.org
SLD authoritative server
(Retries)  attacker.org A? (ns.attacker.com)
DRS #3a
attacker.org NS    drs2b.attacker.org evil referrals
Ingress
DRS #1 DRS #2a
Egress
attacker.org A?
…
DRS #3b
Egress
Ingress Ingress Ingress
(Retries)  attacker.org A?
DRS #3c
DRS #2b
Ingress Ingress

#BHEU #THU   @BlackHatEvents

27

## Slide 28

#### Attack variant II: DNS-Chain

##### v **Recursive DNS resolution guided by** **_evil referrals_**

attacker.org A?
attacker.org NS    drs2a.attacker.org
SLD authoritative server
(Retries)  attacker.org A? (ns.attacker.com)
DRS #3a
attacker.org NS    drs2b.attacker.org evil referrals
DRS #1 DRS #2a
Egress
attacker.org A?
…
DRS #3b
Layer 1 Layer 3
Egress
Ingress Ingress
Layer 2
(Retries)  attacker.org A?
DRS #3c
DRS #2b
Ingress

#BHEU #THU   @BlackHatEvents

28

## Slide 29

#### Attack variant II: DNS-Chain

##### v **Recursive DNS resolution guided by** **_evil referrals_**

###### v **_Final referral_** _:_ points to victim

attacker.org A?
SLD authoritative server
DRS #n-a
(ns.attacker.com)
attacker.org NS
Ingress victim.org
DRS #n-b
Ingress
Amplification factor
Victim
DRS #n-c
Ingress

**Accumulates the power of layers of DRSes Amplification factor** **_multiplies_**

#BHEU #THU   @BlackHatEvents

29

## Slide 30

# **Seems plausible, but can many DRSes be used?**

What are the conditions of successful attacks?

#BHEU #THU   @BlackHatEvents

30

## Slide 31

#### Conditions of successful attacks

##### v **DRS** **_not honoring cleared RD bit_ in DNS header**

v RD (recursion desired) =0: _do not perform recursion, find answers locally in cache_

v Usually _cleared by egress_ , as authoritative servers cannot perform recursion

v DRS honors RD ➔ _chain cannot continue_

v **_27.2% of tested DRSes do not honor_**

|Transaction ID|QR|Opcode|Flags
Z
**R**
**D**|RCODE|
|---|---|---|---|---|
|QDCOUNT|||ANCOUNT||
|NSCOUNT|||ARCOUNT||

#BHEU #THU   @BlackHatEvents

31

## Slide 32

#### Conditions of successful attacks

v **DRS** **_not honoring cleared RD bit_ in DNS header**

- v RD (recursion desired) =0: _do not perform recursion, find answers locally in cache_

- v Usually _cleared by egress_ , as authoritative servers cannot perform recursion

- v DRS honors RD ➔ _chain cannot continue_

- v **_27.2% of tested DRSes do not honor_**

|Transaction ID|QR|Opcode|Flags
Z
**R**
**D**|RCODE|
|---|---|---|---|---|
|QDCOUNT|||ANCOUNT||
|NSCOUNT|||ARCOUNT||

- v **DRS not deployed with negative caching**<sup>**[RFC 2308]**</sup>

   - v Negative caching records DNS failures ➔ _effectively eliminates retries_

   - v **_43% of tested DRSes do not deploy_**

#BHEU #THU   @BlackHatEvents

32

## Slide 33

#### Conditions of successful attacks

- v **DRS** **_not honoring cleared RD bit_ in DNS header**

   - v RD (recursion desired) =0: _do not perform recursion, find answers locally in cache_

   - v Usually _cleared by egress_ , as authoritative servers cannot perform recursion

   - v DRS honors RD ➔ _chain cannot continue_

   - v **_27.2% of tested DRSes do not honor_**

|Transaction ID|QR|Opcode|Flags
Z
**R**
**D**|RCODE|
|---|---|---|---|---|
|QDCOUNT|||ANCOUNT||
|NSCOUNT|||ARCOUNT||

- v **DRS not deployed with negative caching**<sup>**[RFC 2308]**</sup>

   - v Negative caching records DNS failures ➔ _effectively eliminates retries_

   - v **_43% of tested DRSes do not deploy_**

- v **DRS has multiple egresses:** **_the more, the better_**

   - v **_52% of tested DRSes have over 10 egresses_**

#BHEU #THU   @BlackHatEvents

33

## Slide 34

#### Evaluation of DNS-Chain

##### v **Evaluation in controlled environment**

v We select from exploitable DRSes and coordinate them into **_layers_**

# of DRSes coordinated in each layer
Setting Amp. factor
Layer 1 Layer 2 Layer 3 Layer 4 Layer 5 Layer 6 Layer 7
- - - -
# 1 1 4 8 288
- -
# 2 1 4 8 16 32 591
# 3 1 4 8 16 32 64 128 3,702

#BHEU #THU   @BlackHatEvents

34

## Slide 35

#### Attack variant III: DNS-Loop

- v **Modified from DNSChain, creating a** **_loop_ of retry queries**

   - v **_Final referral_** _:_ points back to DRS #1

- v **The victim and goal change now**

   - v **_ALL DRSes in the loop_** become victims

   - v Goal is to exhaust their resources

   - v _Increasing amplification factor is a non-goal_

v **Attackers may also**

- v Inject new rounds of retries to the loop

v Simply by querying DRS #1

Ingress
Ingress
Ingress
Layer 1
DRS #1
Ingress
Layer 2
DRS #2-* Ingress
Layer 3
DRS #3-*

Ingress

**_Layer 1 DRS #1_**

#BHEU #THU   @BlackHatEvents

35

## Slide 36

#### DNS-Loop  Evaluation

v **Evaluation in controlled environment - can the loop last?**

v Coordinates 7 layers of DRSes in the real network

v layer #0 is our server, with _rate limit at 1 pkt/s(due to ethical considerations)_

v Send only one DNS query Layer 0, to trigger the loop

v **_Loop lasts for 24 hours until deliberate stop_**

**24 hours**

#BHEU #THU   @BlackHatEvents

36

## Slide 37

#### Mitigation

**What can we do to prevent this attack?**

Correct bogus implementations such that attack conditions cannot be fulfilled.

#BHEU #THU   @BlackHatEvents

37

## Slide 38

#### Causes

**Tsunami**

_(Traffic amplification ability)_

## Tsu-King

**King** _(Server coordination ability)_

v Cause 1: complex infrastructure v Cause 2: aggressive retries

vCause 3: not following specifications (RD flag, negative cache)

#BHEU #THU   @BlackHatEvents38

## Slide 39

#### Mitigations

##### v **Avoid aggressive retries**

   - v A modest number of retries should suffice, as adopted by mainstream software

- v **Follow DNS specifications**

   - v Honor the DNS flags: if RD tells not to perform recursion, just don’t

- v **Deploy additional mechanisms that add protection**

   - v Negative caching: good to reduce retries

   - v Egress and cache management: reduce independence between egress servers

#BHEU #THU   @BlackHatEvents39

## Slide 40

#### Acknowledgement

### DNS Software Vendors

DNS service providers

#BHEU #THU   @BlackHatEvents

40

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
blackhat Acknowledgement
EUROPE 2023
DNS Software Vendors
& unbound POWERDNS @ mikrotik
DNS service providers
@p II4DNS #2DNS
40
```

## Slide 41

# **Questions?**

**Paper website: https://tsuking.net**

**Contributors of the slides:**

v Wei Xu (xu-w21@mails.tsinghua.edu.cn) v Xiang Li (x-l19@mails.tsinghua.edu.cn) v Chaoyi Lu (luchaoyi@tsinghua.edu.cn) v Haixin Duan (duanhx@tsinghua.edu.cn)

#BHEU #THU   @BlackHatEvents

41
