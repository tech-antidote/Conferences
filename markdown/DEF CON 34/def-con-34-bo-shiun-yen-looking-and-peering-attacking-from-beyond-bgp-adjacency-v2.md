---
title: "Looking and Peering Attacking from beyond BGP Adjacency"
speakers: ["Bo-Shiun Yen"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: null
source_pdf: "DEF CON 34/DEF CON 34 - Bo-Shiun Yen - Looking and Peering Attacking from beyond BGP Adjacency - v2.pdf"
pages: 74
sha256: "fcbab71249086b2d1d8da7f765221c7fb261e5797095aa8e66d5a31fd133d1c0"
text_chars: 9947
ocr_pages: 6
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:13:41Z"
---
# Looking and Peering Attacking from beyond BGP Adjacency

**Speakers:** Bo-Shiun Yen  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Bo-Shiun Yen - Looking and Peering Attacking from beyond BGP Adjacency - v2.pdf` (74 pages)

## Slide 1

# **Looking and Peering Attacking from beyond BGP adjacency**

## Slide 2

#### **WHOAMI**

**Bo-Shiun Yen @Bronson113 Security Engineer @**

## Slide 3

# **October 2021 Facebook misconfigured BGP Facebook disconnected**

**3**

## Slide 4

#### **PART 0**

# **What is BGP**

## Slide 5

#### **BGP - BORDER GATEWAY PROTOCOL**

1.2.3.0/24 is mine
origin
BGP BGP BGP
your router router router bronson113.org
1.2.3.4

**5**

## Slide 6

## **How are they secured? internal vs external**

**6**

## Slide 7

#### **GENERALIZED TTL SECURITY MECHANISM (GTSM)**

eBGP eBGP
TTL=255 TTL=254
you peer everyone else
eBGP accepts UPDATEs
But only if TTL == 255

**7**

## Slide 8

#### **EVERYTHING LIMITED TO ONE HOP**

out of reach
eBGP
TTL=255
you peer everyone else
blast radius = direct peers

**8**

## Slide 9

##### **IMPLEMENTATION WHERE**

**Closed Source Majority - Palo Alto, Juniper, Cisco... BIRD Common in IXPs and ASNs FRR bgpd Common everywhere else OpenBGPD Less Common**

**9**

## Slide 10

#### **PART 1**

# **Looking glasses**

## Slide 11

**How to debug routing with your peer? Through Looking Glasses**

**11**

## Slide 12

#### **HOW DOES LOOKING GLASS WORK?**

command

query upload

**12**

## Slide 13

#### **HOW DOES LOOKING GLASS WORK?**

command

**13**

## Slide 14

# **Command injection**

Through the Looking-Glass, and What Eve Found There DEF CON 22 - Luca Bruno, Mariano Graziano - 2014

**14**

## Slide 15

**Two new command injections in 2026: Hyperglass & looking-glass**

**15**

## Slide 16

### **They're on PeeringDB**

**IMPLEMENTATION ASNS REACHABLE PEERS Hyperglass ~100 ASNs ~450 peers looking-glass ~200 ASNs ~400 peers**

**measured via PeeringDB + querying looking glasses**

**16**

## Slide 17

#### **PART 2**

# **Tunnel injection**

## Slide 18

From Spoofing to Tunneling: New Red Team's Networking Techniques for Initial Access and Evasion DEF CON 33 - 123ojp - 2025

**18**

## Slide 19

#### **WHAT'S TUNNEL INJECTION?**

encrypted tunnel looks internal
VPN peer edge router target

**19**

## Slide 20

#### **WHAT'S TUNNEL INJECTION?**

encrypted tunnel looks internal
VPN peer edge router target
spoofed to the open endpoint
attacker

**20**

## Slide 21

#### **USE THE EDGE ROUTER AS OUR HOP**

encrypted tunnel looks internal
VPN peer edge router target
logically adjacent
attacker

**21**

## Slide 22

#### **CASE STUDY**

**UAF in encap intern logic FRR 10.6.0 and later**

**22**

## Slide 23

#### **BGP_ATTR_INTERN()**

**23**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
BGP_ATTR_INTERN()
find = hash_get(attrhash, attr, bgp_attr_hash_alloc) ;
(attrhash_cmp(attr, reuse_anchor->...parsed_attr) )
reuse_anchor->...interned = find;
23
```

## Slide 24

#### **HASH_GET() -> BGP_ATTR_HASH_ALLOC()**

**Side effect on input attr -> attr != find**

**24**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
HASH_GET() -> BGP_ATTR_HASH_ALLOC()
*p)
* = XMALLOC(MTYPE_ATTR, (xattr));
xattr = x*val;
(val->encap_subtlvs)
val->encap_subtlvs = NULL;
attr;
Side effect on input attr ->
24
```

## Slide 25

#### **PACKET 1**

###### **`overwrite length`**

freed heap
length heap libc
attr hdr attr data ? ? ?
0xFFFF ptr ptr

```
read leftover chunks
```

###### **`whatever heap + libc pointers were there -> ASLR leak`**

**25**

## Slide 26

#### **PACKET 2**

###### **`the heap`**

###### **`reclaimed ->`**

|**`...`**|`chunk - 0x30`|
|---|---|
|**`prev_size`**|**`0x00`**|
|**`size`**|**`0x51`**|
|**`index`**|`0x5583...a0`|
|**`hash_key`**|`0x5583...f0`
**`our forged`**|
|**`hash_cmp`**|**`system()`**
**`object`**|
|**`name`**|`0x5583...10`|
|**`...`**|`chunk - 0x20`|

###### **`the next hash lookup calls hash_cmp() -> RCE`**

**26**

## Slide 27

#### **COMBINE WITH TUNNEL INJECTION**

attacker

looks internal
edge router FRR bgpd

FRR bgpd

```
a BGP UPDATE wrapped in a tunnel
```

**27**

## Slide 28

#### **COMBINE WITH TUNNEL INJECTION**

attacker

leaked heap + libc
VPN looks internal
edge router FRR bgpd
packet 1: heap over-reads

**28**

## Slide 29

#### **COMBINE WITH TUNNEL INJECTION**

forge hash object
VPN looks internal
attacker edge router FRR bgpd
packet 2: RCE

**29**

## Slide 30

#### **IMPACT SO FAR**

# **One hop**

## Slide 31

**The next-hop boundary means we reach direct peers only**

**31**

## Slide 32

#### **PART 3**

# **Transitive BGP attacks**

## Slide 33

**Variant 1: Core Parser Issues**

## Slide 34

#### **CVE-2026-49943**

## **BIRD as_path_match stack overflow**

**34**

## Slide 35

#### **THE BUG -** **`AS_PATH_MATCH()`**

**forge long AS_PATH with ext-msg -> stack overflow pos[]**

**35**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
THE BUG - AS_PATH_MATCH()
adata xpath, ...
[2048 + 1];
plen = parse_path(path, pos);
forge long AS_PATH with ext-msg -> stack overflow pos[]
35
```

## Slide 36

#### **TRANSITIVE ATTACKS**

```
eBGPeBGP
EstablishedEstablished
attackerrelayvictim
FRRBIRD
```

**36**

## Slide 37

#### **TRANSITIVE ATTACKS**

malformed attr
eBGP eBGP
Established Established
attacker relay victim
FRR BIRD

**37**

## Slide 38

#### **TRANSITIVE ATTACKS**

relayed
eBGP eBGP
Established Established
attacker relay victim
FRR BIRD

**38**

## Slide 39

#### **TRANSITIVE ATTACKS**

```
attacker
```

```
eBGP
Established
```

```
relay
FRR
```

```
eBGP
crash
```

```
victim
BIRD
```

```
the parser crashes
stack overflow
```

**39**

## Slide 40

#### **TRANSITIVE ATTACKS**

```
adjacency boundary
```

```
eBGPeBGP
Establishedcrash
attackerrelay
```

```
relayvictim
FRRBIRD
```

```
the victim is not a peer to the attacker
the attribute crosses the security boundary
```

**40**

## Slide 41

#### **SEGMENTING THE INTERNET**

```
BIRD route servers - all crash
```

attacker

```
the whole BIRD border crashes -> the internet splits in two
```

**41**

## Slide 42

## **Variant 2: Optional Attributes**

## Slide 43

"...the unrecognized transitive optional attribute of that path **MUST be passed** , along with the path, to other BGP peers..." RFC 4271

**43**

## Slide 44

**Unknown transitive attributes get re-emitted**

**44**

## Slide 45

### **RFC 4271 ALSO SAID Malformed attribute -> session reset**

**45**

## Slide 46

### **This is a bad behavior**

one malformed BGP-LS attribute reset Juniper's sessions - riding transitively past every router that didn't parse it CVE-2023-4481 - benjojo, "Grave flaws in BGP Error handling" - 2023

**RFC 7606 recommends treat-as-withdrawal**

**46**

## Slide 47

**Now let's consider parser issue again FRR Prefix-SID length desync**

**47**

## Slide 48

#### **THE BUG -** **`BGP_ATTR_PREFIX_SID()`**

**the cursor and the counter disagree -> it lands off the attribute boundary**

**48**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
THE BUG - BGP_ATTR_PREFIX_SID()
type = stream_getc(connection->curr) ;
length = stream_getw(connection->curr) ;
ret = bgp_attr_psid_sub(type, length, args);
psid_parsed_length += length + headersz;
the cursor and the counter disagree -> it lands off the attribute boundary
48
```

## Slide 49

#### **THE LENGTH DESYNC**

```
length field says 30 bytes
```

type
len=30

fake
25 bytes actually read slack
type/len
actual end declared end
cursor stops
Unparsable slack -> session reset
Crafted slack -> packet smuggling

**49**

## Slide 50

#### **WHAT ATTRIBUTE IS THIS**

### **Prefix-SID: Optional Transitive**

**50**

## Slide 51

#### **TRANSITIVE ATTACK 2**

poison Prefix-SID
eBGP eBGP
Established Established
attacker relay victim
BIRD FRR
optional-transitive attribute

**51**

## Slide 52

#### **TRANSITIVE ATTACK 2**

relayed verbatim
length error (3/5)
eBGP eBGP
Established Down
attacker relay victim
BIRD FRR
cursor lands off the attribute boundary
session reset

**no adjacency needed (again)**

**52**

## Slide 53

### **Variant 3:**

## **Configuration Difference**

## Slide 54

**What if the attribute is well formed But routers disagree with each other?**

**54**

## Slide 55

#### **THE PREFIX LIMIT**

**limit how many prefixes a peer may send**

**55**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
THE PREFIX LIMIT
BIRD import limit 100 action restart
FRR / Cisco neighbor X maximum-prefix 100 restart 5
limit how many prefixes a peer may send
55
```

## Slide 56

#### **LIMIT MISMATCH**

```
source
```

```
120 prefixes
Router A
prefix-limit 150
```

```
replays 120
```

```
Router B
prefix-limit 100
```

```
A accepts (120 < 150)
and replays all 120 to B
```

**56**

## Slide 57

#### **LIMIT MISMATCH**

```
source
```

```
120 prefixes
Router A
prefix-limit 150
```

```
120 > 100
Cease 6/1
Router B
prefix-limit 100
```

```
B rejects (120 > 100)
Cease 6/1: Maximum Number of Prefixes
```

**57**

## Slide 58

#### **LIMIT MISMATCH**

restart
120 prefixes 120 > 100
Cease 6/1
Router A Router B
prefix-limit 150 prefix-limit 100
B restarts, but A still holds the routes
persistent reset loop

source

**58**

## Slide 59

#### **PART 4**

# **Demo**

## Slide 60

#### **THE LAB**

HTTP SSH
attacker looking-glass

eBGP eBGP
Established Established
edge relay victim
FRR BIRD FRR

attacker

**60**

## Slide 61

#### **STAGE 0 - RECON**

query: routes
BGP table
HTTP SSH eBGP eBGP
Established Established
attacker looking-glass edge relay victim
FRR BIRD FRR

```
attacker
```

**61**

## Slide 62

#### **STAGE 1 - RCE**

$(id)

HTTP SSH eBGP eBGP
Established Established
attacker looking-glass edge relay victim
FRR BIRD FRR

```
attacker
```

**62**

## Slide 63

#### **STAGE 1 - RCE**

```
vtysh -c "... regexp $(id)"
```

```
uid=1000(lg) gid=1000(lg) ...
```

HTTP SSH eBGP eBGP
Established Established
attacker looking-glass edge relay victim
FRR BIRD FRR

```
attacker
```

**63**

## Slide 64

#### **STAGE 2 - PIVOT**

###### **`upload stage2`**

HTTP SSH eBGP eBGP
Established Established
attacker looking-glass edge relay victim
FRR BIRD FRR

**64**

## Slide 65

#### **STAGE 2 - PIVOT**

```
execute stage2
```

injector
HTTP SSH eBGP eBGP
Established Established
attacker looking-glass edge relay victim
FRR BIRD FRR

**65**

## Slide 66

#### **STAGE 3 - REMOTE DOS**

poisoned UPDATE
injector
HTTP SSH eBGP eBGP
Established Established
attacker looking-glass edge relay victim
FRR BIRD FRR
Prefix-SID attack

**66**

## Slide 67

#### **STAGE 3 - REMOTE DOS**

Length error (3/5)
injector
HTTP SSH eBGP eBGP
Established Down
attacker looking-glass edge relay victim
FRR BIRD FRR

**67**

## Slide 68

#### **STAGE 3 - REMOTE DOS**

Down / Up
injector
HTTP SSH eBGP eBGP
Established Down
attacker looking-glass edge relay victim
FRR BIRD FRR

**68**

## Slide 69

#### **ATTACK BEYOND ADJACENCY**

injector
HTTP SSH eBGP eBGP
Established Down
attacker looking-glass edge relay victim
FRR BIRD FRR

**69**

## Slide 70

# **Play the demo**

**70**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Play the demo
EXPLOIT -— ./demo.sh
routers streaming on the left.
drive the demo here:
./demo.sh step-gated (ENTER between stages)
./demo.sh --record auto + pcaps/logs to ./evidence/
demo-chain git:(main) xX ./demo.shlj
/@.1s
[17/07/26 | 23:37:19]
70
```

## Slide 71

#### **PART 5**

# **Impact**

## Slide 72

### **We fingerprinted published daemon version through ASN information**

**72**

## Slide 73

#### **ESTIMATE SHARE OF EBGP ROUTERS**

**DAEMON IXP/ASNS WORLD WIDE BIRD 50% 8% FRR 15% 10%**

**73**

## Slide 74

**Thank you**
