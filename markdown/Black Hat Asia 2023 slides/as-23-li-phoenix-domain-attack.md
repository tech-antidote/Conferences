---
title: "Phoenix Domain Attack"
speakers: ["Li"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2023"
edition: "ASIA"
year: 2023
source_pdf: "Black Hat Asia 2023 slides/AS-23-Li-Phoenix-Domain-Attack.pdf"
pages: 31
sha256: "24c983b53c7020b85d74dceb3b23ad66ed7a8263bcfa310ab3e7679bd28a0222"
text_chars: 10804
ocr_pages: 0
has_ocr: false
redacted_secrets: 0
ocr_confidence: null
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: ["AS-23-Li-Phoenix-Domain-Attack_tools.txt"]
extractor: "pymupdf4llm 1.28.2"
converted_at: "2026-08-12T03:48:03Z"
---
# Phoenix Domain Attack

**Speakers:** Li  
**Conference:** Black Hat ASIA 2023  
**Source:** `Black Hat Asia 2023 slides/AS-23-Li-Phoenix-Domain-Attack.pdf` (31 pages)


## Slide 1

# Phoenix Domain Attack: Vulnerable Links in Domain Name Delegation and Revocation

Xiang Li Tsinghua University

#BHASIA @BlackHatEvents

## Slide 2

## Domain Name

Ø **Domain name system (DNS)**

`o` Entry point of many Internet activities

`o` Security guarantee of multiple application services

`o` Domain names are widely registered

Web CDN Email Certificate

dns-oarc.net
64.191.0.66

DNS

Cited from verisign.com/dnib

#BHASIA @BlackHatEvents

2

## Slide 3

## Domain Name Abuse

Ø **Also abused by criminal activities**

`o` Botnet, phishing, malware distribution

Cited from bleepingcomputer.com

Cited from <u>scmp.com</u>

Cited from <u>norton.com</u>

#BHASIA @BlackHatEvents

3

## Slide 4

## Domain Name Abuse

Ø **Also abused by criminal activities**

`o` Botnet, phishing, malware distribution

Ø **ICANN Domain abuse activity reporting (DAAR)**

`o` In March 2023

- Check 216,171,933 domain names within 1,154 gTLDs

**622,875 domains showing security threats**

#BHASIA @BlackHatEvents

4

## Slide 5

## Domain Name Revocation

##### Ø **Fighting against malicious domain names**

- Ø **Mechanism**

`o` Domain name revocation

`o` Operated by registries or registrars

`o` Deleting or changing domain name registration (delegation)

Ø **Result**

`o` Domains are no longer controlled by original registrants/attackers

#BHASIA @BlackHatEvents

5

## Slide 6

## Domain Name Revocation

Ø **Domain name seizure activity**

`o` Best security practice

`o` Widely adopted

Cited from theregister.com

Cited from intelligentciso.com

#BHASIA @BlackHatEvents

6

## Slide 7

## Question

**How does domain name revocation work on domain name registration (delegation)?** It is the reverse process of **delegation** .

#BHASIA @BlackHatEvents

7

## Slide 8

## Domain Name Revocation

##### Ø **Normal resolution**

##### Ø **Revocation**

- Domain delisting

- Domain sinkholing

botnet.com. NS ns.botnet.com botnet.com. NS ns.botnet.com botnet.com. NS sinkhole
com com Remove NS com Change NS
delegation
sinkhole
3
1 2 1 2 1 2
3
4
ns.botnet.com ns.botnet.com ns.botnet.com
4
botnet.com A a.t.k.r botnet.com NXDomain botnet.com A 127.0.0.1
Resolver Resolver Resolver

Normal resolution

Domain delisting

Domain sinkholing

#BHASIA @BlackHatEvents

8

## Slide 9

## Question

### **Does domain name revocation function as desired?**

#### No. **Ghost domain** broke this guarantee.

#BHASIA @BlackHatEvents

9

## Slide 10

## Ghost Domain

##### Ø **Ghost domain attack**

- Proposed in NDSS 2012 by our NISL lab

- Making revoked domain names still resolvable on resolvers

botnet.com.
com
botnet.com. NS ns.botnet.com.
2 3
Normal 4 Attacker
resolution
botnet.com
5
1 botnet.com A?
Target
resolver Cache

botnet.com.     86400 NS ns1.botnet.com.
botnet.com.    86400 NS ns.botnet.com.
ns.botnet.com. 86400 A  a.t.k.r
ns.botnet.com.  43200 A  a.t.k.r

botnet.com.
com
botnet.com. NS ns1.botnet.com.
2 Attacker Ghost domain
attack
botnet.com
3
1 ns1.botnet.com A? Refreshed
Target indefinitely
resolver Cache
botnet.com.     86400 NS ns1.botnet.com.
ns1.botnet.com. 86400 A  a.t.k.r
ns.botnet.com.  43200 A  a.t.k.r

#BHASIA @BlackHatEvents

10

## Slide 11

## Takeaway

### **With ghost domain, even after revocation, malicious domains can still be resolvable.**

Attackers can use it to evade **domain take-down** or **domain expiration** .

#BHASIA @BlackHatEvents

11

## Slide 12

## Ghost Domain

##### Ø **Vulnerable software**

- Not all software: BIND, PowerDNS, etc.

- Ø **Mitigation**

`o` TTL field cannot be prolonged

botnet.com.
com
botnet.com. NS ns1.botnet.com.
2 Attacker Ghost domain
attack
botnet.com
3
1 ns1.botnet.com A? No TTL
Target updating
resolver Cache
botnet.com.     43200 NS ns1.botnet.com.
ns1.botnet.com. 86400 A  a.t.k.r
ns.botnet.com.  43200 A  a.t.k.r

#BHASIA @BlackHatEvents

12

## Slide 13

## Question

### **10 years later, does domain name revocation work as desired after fixing ghost domain?**

No. **Phoenix domain** still breaks this guarantee with a broader attack surface.

#BHASIA @BlackHatEvents

13

## Slide 14

## Phoenix Domain

Ø **What is phoenix domain**

`o` Proposed by our NISL lab too

`o` Also making revoked domain names still resolvable on resolvers

`o` Two new vulnerabilities in protocols or implementations

- Two variations ( **T1** and **T2** )

- Affecting all DNS implementations

#BHASIA @BlackHatEvents

14

## Slide 15

## Question

### **Why is domain name revocation still vulnerable?**

We find that the entire attack surface remains unclear now.

#BHASIA @BlackHatEvents

15

## Slide 16

## DNS Cache Operations

##### Ø **Summary**

###### Response from servers

Request from clients Response from servers
Search  data from the cache Search  data from the cache
Cache hit Cache miss Cache hit Cache miss
Check data
ranks
Use the  Update  the  Insert  the
Return the
closest  NS for  records in the  response into
answer
queries cache the cache
Cache
Cache is stored passively  Delete  records
Cache expiration
according to the  TTL from the cache

#BHASIA @BlackHatEvents

16

## Slide 17

## DNS Cache Operations

Ø  Summary
o Updating
o Insertion

o Searching

###### Response from servers

###### Request from clients

Search  data from the cache Search  data from the cache
Cache hit Cache miss Cache hit Cache miss
Check data
ranks
Use the  Update  the  Insert  the
Return the
closest  NS for  records in the  response into
answer
queries cache the cache
Cache
Cache is stored passively  Delete  records
Cache expiration
according to the  TTL from the cache
Exploited by Exploited by Exploited by
Ghost Domain Phoenix Domain T1 Phoenix Domain T2

#BHASIA @BlackHatEvents

17

## Slide 18

## Question

### **How does Phoenix Domain work?**

Two variations, two ways.

#BHASIA @BlackHatEvents

18

## Slide 19

## Phoenix Domain T1

Ø  T1 attack

`o` Exploiting vulnerable cache insertion implementations

`o` Inserting new NS records when the old is about to expire

botnet.com. botnet.com.
com com
botnet.com. NS ns.botnet.com. botnet.com. NS ns1.botnet.com.
2 3
Before 4 Attacker 2 Attacker After
revocation revocation
botnet.com botnet.com
5 3 (delayed response)
1 botnet.com A? 1 ns1.botnet.com A?
Target Target Cache expires
resolver Cache resolver Cache
and is removed
botnet.com.     86400 NS ns1.botnet.com. botnet.com.     86400 NS ns1.botnet.com. No updating
botnet.com.    86400 NS ns.botnet.com. ns1.botnet.com. 86400 A  a.t.k.r restriction
ns.botnet.com. 86400 A  a.t.k.r
ns.botnet.com.  43200 A  a.t.k.r ns.botnet.com.  0     A  a.t.k.r

#BHASIA @BlackHatEvents

19

## Slide 20

## Phoenix Domain T1

Ø  T1 attack
Attacker Target
botnet.com resolver
o Attack steps
Cache
o Cache expiration
botnet.com. NS 86400 ns.botnet.com.
ns.botnet.com. A 86400 a.t.k.r
o Cache deletion
o Cache insertion
TTL
1 ns1.botnet.com A?
Delay Cache expiration
2 ns1.botnet.com A? ∆𝒕𝒕𝒅
for ∆𝒕𝒕𝒅 and  NS  records
are removed
3 ns1.botnet.com A
Cache
botnet.com NS
botnet.com. NS 86400 ns1.botnet.com.
ns1.botnet.com. A 86400 a.t.k.r
Cache inserting
ns.botnet.com.  A 0     a.t.k.r

#BHASIA @BlackHatEvents

20

## Slide 21

## Phoenix Domain T2

Ø **T2 attack** `o` Exploiting vulnerable cache searching operations

`o` Inserting new NS records of subdomains

botnet.com. botnet.com.
com com
botnet.com. NS ns.botnet.com. s.botnet.com. NS ns.s.botnet.com.
2 3
Before 4 Attacker 2 Attacker After
revocation revocation
botnet.com botnet.com
5 3 (iterative delegation)
1 botnet.com A? 1 s.botnet.com A?
Target Target
resolver Cache resolver Cache
botnet.com.     86400 NS ns1.botnet.com. s.botnet.com.    86400 NS ns.s.botnet.com.
botnet.com.    86400 NS ns.botnet.com. ns.s.botnet.com. 86400 A  a.t.k.r
ns.botnet.com. 86400 A  a.t.k.r botnet.com.      43200 NS ns.botnet.com.
ns.botnet.com.  43200 A  a.t.k.r ns.botnet.com.   43200 A  a.t.k.r

#BHASIA @BlackHatEvents

21

## Slide 22

## Phoenix Domain T2

Ø  T2 attack

o Exploiting vulnerable cache searching operations

o Inserting  new NS records of subdomains

botnet.com. botnet.com.
com com
botnet.com. NS ns.botnet.com. s.botnet.com. NS ns.s.botnet.com.
2 3
Before 4 Attacker 2 Attacker After
revocation revocation
botnet.com botnet.com
5 3 (iterative delegation)
1 botnet.com A? 1 s.botnes.s.bo t .com A?net.com. NS
Target Target s.s.s.botnet.com. NS
resolver Cache resolver Cache s.s.s.s.botnet.com. NS >100
botnet.com.     86400 NS ns1.botnet.com. s.botnet.com.    86400 NS ns.s.botnet.com.…
s.s.s…s.s.s.botnet.com.NS
botnet.com.    86400 NS ns.botnet.com. ns.s.botnet.com. 86400 A  a.t.k.r
ns.botnet.com. 86400 A  a.t.k.r botnet.com.      43200 NS ns.botnet.com.
ns.botnet.com.  43200 A  a.t.k.r ns.botnet.com.   43200 A  a.t.k.r

#BHASIA @BlackHatEvents

22

## Slide 23

## Vulnerable Software

##### Ø **Phoenix domain T1**

`o` BIND9, Knot, Unbound, and Technitium Ø **Phoenix domain T2**

`o` All tested 8 software are vulnerable (7 confirmed, 9 CVEs)

CVE-2022-30250 CVE-2022-30251 CVE-2022-30252 CVE-2022-30254 CVE-2022-30256 CVE-2022-30257 CVE-2022-30258 CVE-2022-30698 CVE-2022-30699

#BHASIA @BlackHatEvents

23

## Slide 24

## Vulnerable Public Resolvers

Ø **Phoenix domain T1 and/or T2**

`o` We test 41 public resolver vendors

`o` All resolvers are vulnerable to T1 and/or T2

- Such as Google, Cloudflare, Akamai, AdGuard, etc. (15 confirmed)

#BHASIA @BlackHatEvents

24

## Slide 25

## Vulnerable Open Resolvers

##### Ø **Recursive resolver list**

`o` Through scanning, we collected 1.2M resolvers

`o` 210k recursive resolvers are selected

#BHASIA @BlackHatEvents

25

## Slide 26

## Experiments for T2

##### Ø **Short-term experiments**

- Check how many labels are supported

`o` 89% are vulnerable

- After 100 rounds, 42% are vulnerable

#BHASIA @BlackHatEvents

26

## Slide 27

## Experiments for T2

Ø **Long-term experiments**

- Check how long phoenix domain can be alive

`o` After one week, 40% are vulnerable

- After one month, 25% are vulnerable

#BHASIA @BlackHatEvents

27

## Slide 28

## Experiments for T2

##### Ø **Geolocation of vulnerable resolvers**

`o` USA, Russia, and China

#BHASIA @BlackHatEvents

28

## Slide 29

## Mitigation

Ø 6 approaches Ø Discussing with RFC editors Ø For example,

Ø **M1:** when NS RRs expire, querying upstream for NS Ø **M2:** trust NS from the parent more than the child Ø **M3:** use small TTL values

#BHASIA @BlackHatEvents

29

## Slide 30

## Black Hat Sound Bytes

Ø **The DNS RFCs and specifications are not clear to provide a definitive definition for each operation, hence leaving a large attack window for ambiguous implementations.**

- We should check the RFC's essential specifications.

- Ø **The DNS implementations are not consistent across software, even for identical client queries.**

- This inconsistency is likely to conceal possible risks, which should be thoroughly researched and evaluated.

- Ø **The original DNS mechanism is insufficient to defend against several types of attacks.**

`o` To improve it, we should propose new patches or redesign some structures.

#BHASIA @BlackHatEvents

30

## Slide 31

## Question

**Paper**

**Thanks for listening! Any question?**

**Tool**

Xiang Li, Tsinghua University x-l19@mails.tsinghua.edu.cn

#BHASIA @BlackHatEvents

31

## Companion resources

### `AS-23-Li-Phoenix-Domain-Attack_tools.txt`

```text
https://github.com/idealeer/xmap
```
