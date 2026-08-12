---
title: "The 5G Titanic"
speakers: ["Altaf Shaik", "Robert Jaschek"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Altaf Shaik&Robert Jaschek_The 5G Titanic.pdf"
pages: 46
sha256: "fd12a421fe4d1ce9f499eda81132a1e74f968a11f696557a494d08da077e95ca"
text_chars: 17626
ocr_pages: 7
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T22:49:28Z"
---
# The 5G Titanic

**Speakers:** Altaf Shaik, Robert Jaschek  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Altaf Shaik&Robert Jaschek_The 5G Titanic.pdf` (46 pages)

## Slide 1

The 5G Titanic

Dr. Altaf Shaik, Robert Jaschek

Fast IOT & Technische Universität Berlin

Reference: https://education.nationalgeographic.org/resource/titanic-sinks/ 07/08/25 Dr. Altaf Shaik - Fast IOT

## Slide 2

## Titanic

###### **On April 15, 1912, the RMS Titanic sunk in the North Atlantic Ocean**

4

FAST IOT

07/08/25

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
On April 15, 1912, the RMS Titanic sunk in the North Atlantic Ocean
RMS Titanic - key design fault
Watertight bulkheads Cargo holds and boiler rooms flooded
after hull is pierced by iceberg
asain
Water pours over the top of the bulkheads
via the deck above, flooding the entire hull
ee
07/08/25 4
```

## Slide 3

What 5G assumes?

Dr. Altaf Shaik - Fast IOT

07/08/25

5

## Slide 4

## CUPS

###### **Control user plane separation**

6

FAST IOT

07/08/25

## Slide 5

## Security features

**Design omits IPSec usage if the interface is physically protected.**

7

FAST IOT

07/08/25

## Slide 6

## 5G data flow

GTP: GPRS tunneling protocol (Age: 26)

8

FAST IOT

07/08/25

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
5G data flow
GTP: GPRS tunneling protocol (Age: 26)
UE gNodeB UPF Data Network
t IP Packet | GTP-U (uplink TEID) |! IP Packet [
L p>! P| p>!
I IP Packet 1 I
GTP-U (downlink TEID)1 IP Packet
I
07/08/25 8
```

## Slide 7

## Positioning the 5G attacker

9

FAST IOT

07/08/25

## Slide 8

But what if that separation fails?

Dr. Altaf Shaik - Fast IOT

07/08/25

10

## Slide 9

## Protocol tunneling via GTP-U

- Encapsulating one protocol inside user-plane traffic to reach a specific node

- Why GTP-U: A protocol that lacks built-in integrity checks or source authentication.

- Simple forwarding logic based solely on IP address and identifiers – No inspection of payload contents

- Delivers encapsulated inner payloads to internal GTP-U-capable nodes (e.g., UPF, gNodeB)

- **Sending GTP-U encapsulated packets to networks is considered fraud**

11

FAST IOT

07/08/25

## Slide 10

## Protocol tunneling - packet

● **GTP-U-in-GTP-U** encapsulated packet – Standard protocol compliant

12

FAST IOT

07/08/25

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Protocol tunneling - packet
¢ GTP-U-in-GTP-U encapsulated packet
- Standard protocol compliant
General GTP-U-in-GTP-U encapculated packet structure
src | dst | src | dst | TEID src dst | src | dst TEID src dst
IP UDP GTP IP UDP GTP IP
Outer GTPH Inner GTPH Payload
07/08/25 12
```

## Slide 11

## How to craft

- Discover and craft packet with internal IP addresses and ports – from search engines, recon, insiders, intermediaries

- Enumerate and forge target users tunnel identifier, and IP address

13

FAST IOT

07/08/25

## Slide 12

## Protocol tunneling - flow

14

FAST IOT

07/08/25

## Slide 13

## Protocol tunneling - roaming

- 5G has N9 interface – connect roaming interfaces

● Packet could be tunneled internationally – a vulnerable UPF will execute it

15

FAST IOT

07/08/25

## Slide 14

## Network boundary bridging

- Routing user-plane traffic across architectural trust boundaries – Reach isolated control-plane NF like AMF, SMF

- Misconfigured routing and lack of egress filtering at UPF allow redirection to control-plane interfaces

- Target AMF (via NGAP) or, SMF & UPF (via PFCP) – Simple setup and association request messages to communicate

16

FAST IOT

07/08/25

## Slide 15

Trying it in the field

Dr. Altaf Shaik - Fast IOT

07/08/25

17

## Slide 16

## Setup

- **Six 5G Core networks**

   - 4 open source and 2 commercial (private)

   - isolated lab environments, containerized

   - Standard configurations, no custom firewalls

- One SDR based radio base station

   - From srsRAN project, connects to all cores

- Several 5G Smartphones and SIM cards

   - Sends encapsulated GTP-U packets to the UPF

   - protocol-compliant payloads such as ICMP, UDP, NGAP, PFCP

   - Fast automated enumeration of data plane identifiers IP, TEID, SEID

- Prior knowledge

   - Target UPF, AMF and SMF IP addresses

18

FAST IOT

07/08/25

## Slide 17

What we found – vulnerabilities and vectors

Dr. Altaf Shaik - Fast IOT

07/08/25

19

## Slide 18

## Processing tunneled packets

- Outer GTP header gets correctly parsed – Sent under the attacker’s legit connection

- Inner GTP header is redirected to a target network element – **Tunnelled** : the malicious payload sent to UPF or gNodeB

   - **Bridged** : the malicious payload sent by AMF/SMF

- Payload can be processed or discarded – depends on guessed identifiers

20

FAST IOT

07/08/25

## Slide 19

## Tunneled packet sample

21

FAST IOT

07/08/25

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
07/08/25
Tunneled packet sample
Internet Protocol Version 4, Src: 22.10
i]
er Datagram Protc
Length: 74
sre Port: 2152, Dst Port:
ension header typ
=nsion header
(PDU Session containe
» Internet Protocol Version 4, Src:
>-User Datagram Pro
+ GPRS Tunneling Protocol
S-Fla =
> Internet P
Message
Length:
TEID:
User Datagram Protec
>-Data (2 by )
, sre Port: 9099, Dst Port:
otocol Version 4, Src:
L, Src Port: 9090, Dst Port:
22.10.0.3
21
```

## Slide 20

## Boundary traversal

- Lack interface isolation and packet path validation – Perimissive routing opens internal paths even with physical or logical separation

   - e.g., Opens a non-existent path from UPF to AMF via _SCTP/NGAP setup_

- UPF to SMF

   - Existent and accessible with simple _PFCP association_

- Source-NAT can distort traffic origin visibility

   - UPF applies source NAT to packets from UE

   - AMF or SMF trust attacker-generated SCTP or PFCP packets as they appear to originate from the UPF itself

22

FAST IOT

07/08/25

## Slide 21

## Boundary traversal

23

FAST IOT

07/08/25

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Boundary traversal
Tunneled packet - target AMF
07/08/25
gNB | UPF | gNB| UPF | Attacker JAttacker| UPF| src |UPF| victim | victim | AMF src | AMF
IP UDP GTP IP UDP GTP IP SCTP
Outer GTPH Inner GTPH NGAP
Tunneled packet - target SMF :
gNB | UPF | gNB| UPF | Attacker |Attacker UPF| src |UPF| victim {| victim | SMF src SMF
IP UDP GTP IP UDP GTP IP UDP
Outer GTPH Inner GTPH PFCP
23
```

## Slide 22

## TEID Enumeration - how

##### **Exploiting standard comliant error responses in tunnel management messages** 3GPP TS 29.281 (Sec 7.3)

|**#**|**IP address**|**TEID**|**Action taken by UPF**|
|---|---|---|---|
|1|Unassigned|Existent|IP spoofing detected (packet drop)|
|2|Assigned|Existent not matching|IP spoofing detected (packet drop)|
|3|Assigned|Matching|Process packet|
|4|Both|Non-existent|GTP error indication|

Exploitable for Enumeration

24

FAST IOT

07/08/25

## Slide 23

## TEID Enumeration - how

###### **As seen from the attacker mobile**

**_Error indications_** for all invalid TEIDs

No error indications for all valid TEIDs

If TEID-IP matches **ping reply**

25

FAST IOT

07/08/25

## Slide 24

## TEID Enumeration - how

###### **As seen from the UPF**

**Encapsulated packets arrive at UPF**

Two TEIDs: 1. Attacker radio connection

2. Forged TEID of a victim

26

FAST IOT

07/08/25

## Slide 25

## Abonrmal behavior for PFCP

- Specification ambiguities

   - Undefined behavior when sessions are established without any rules

         - Resulting a **DoS** : All cores create dummy sessions and waste resources

         - Some cores crash after receiving 4096 requests, terminating all existing sessions

         - Some crash for empty requests: unexpected code flow

      - Implementation differences

         - Missing authentication of the SEID-IP tuple; allows for source authentication

         - Failure to do so allows attackers to manipulate sessions by replaying or guessing SEIDs

         - Majority cores did not implement this functionality; some ambiguity

27

FAST IOT

07/08/25

## Slide 26

## SEID Enumeration - how

#### **Exploiting standard compliant error responses in session management messages**

28

FAST IOT

07/08/25

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
SEID Enumeration - how
07/08/25
Exploiting standard compliant error
responses in session management messages
Protocol Length Info 4
GTP <PFCP> 108 PFCP Session Modification Requ
GTP <PFCP> 113 PFCP Session Modification Resp
GTP <PFCP> 113 PFCP Session Modification Resp
GTP <PFCP> 108 PFCP Session Modification Requ
GTP <PFCP> 108 PFCP Session Modification Requ
GTP <PFCP> 113 PFCP Session Modification Resp
GTP <PFCP> 113 PFCP Session Modification Resp
GTP <PFCP> 108 PFCP Session Modification Requ
GTP <PFCP> 108 PFCP Session Modification Requ
GTP <PFCP> 113 PFCP Session Modification Resp
GTP <PFCP> 113 PFCP Session Modification Resp
GTP <PFCP> 108 PFCP Session Modification Requ
GTP <PFCP> 108 PFCP Session Modification Requ
GTP <PFCP> 113 PFCP Session Modification Resp
GTP _<PFCP> 113 PFCP Session Modification Resp«
bytes captured (904 bits)
Dst: 10.33.33.77
mrt: 2152
Dst: 10.45.0.5
ort: 8805
donse (53)
Wireshark - Packet 7339 - v2_7_5_SEID_ENUM_filter.pcap
» User Datagram Protocol, Src Port: 8805, Dst Port: 8805
~ Packet Forwarding Control Protocol
>» Flags: 0x21, SEID (S)
Message Type: PFCP Session Modification Response (53)
Length: 17
SEID: 0x00000000000009C7
Sequence Number: 730
Spare: 0
IE Type: Cause (19)
IE Length: 1
Cause: Request accepted(success) (1)
[Response To: 7336]
[Response Time: ©.000313000 seconds]
4
@kelp
Wireshark - Packet 7348 - v2_7_5_SEID_ENUM _filter.pcap
» User Datagram Protocol, Src Port: 8805, Dst Port: 8805
~ Packet Forwarding Control Protocol
>» Flags: 0x21, SEID (S)
Message Type: PFCP Session Modification Response (53)
Length: 17
SEID: 0x0000000000000000
Sequence Number: 731
Spare: 0
IE Type: Cause (19)
IE Length: 1
Cause: Session context not found (65)
[Response To: 7347]
[Response Time: 0.000220000 seconds]
28
```

## Slide 27

## Success factors for enumeration

###### **TEID ->**

- Speed: Depends on identifier space and allocation pattern

- Multiple smartphone connection paths – speed up enumeration

- **No rate limiting**

- One TEID-IP pair is sufficient for attack and can be cracked in seconds

- Ongoing connections are not interrupted - stealthy

**SEID ->**

|**Core**|**Allocation**|**Enumeration**|**Time**|
|---|---|---|---|
|Open5GS|2B Random|Possible|seconds|
|Free5GC|4B Incremental|Possible|hours|
|OAI-5G|4B Random|Prohibited|infinte|
|SD-Core|4B Incremental|Possible|hours|
|CC1|4B Random|Prohibited|infinite|
|CC2|4B Incremental|Allowed|hours|

|**Core**|**Allocation**|**Enumeration**|**Time**|
|---|---|---|---|
|Open5GS|12bit Random|Possible|seconds|
|Free5GC|8B Incremental|Possible|hours|
|OAI-5G|8B Incremental|Possible|hours|
|SD-Core|8B Random|Possible|infinite|
|CC1|8B Incremental|Possible|hours|
|CC2|8B Incremental|Possible|hours|

29

FAST IOT

07/08/25

## Slide 28

Using this
in the real world

Dr. Altaf Shaik - Fast IOT

07/08/25

30

## Slide 29

## Reflective injection

- redirect traffic through a victim UE’s uplink, enabling reflective delivery of unsolicited traffic to UEs

   - charging fraud where billing system attributes traffic volume to victim

   - bypass inbound filtering to otherwise unreachable UEs

- Amplified reflection: small spoofed query can trigger a large response – exhaust both uplink and downlink quotas

31

FAST IOT

07/08/25

## Slide 30

## Direct routes to target UEs

- Direct and covert data injection into a UE, bypassing standard data path potentially evading any network layer defenses at the UPF preventing east-west traffic

- Bypassing the standard uplink–core–downlink data path and avoiding involvement of the external data network.

32

FAST IOT

07/08/25

## Slide 31

## A legitimate MITM

**Operating a legitimate rogue 5G gNodeB and UE  as a relay**

33

FAST IOT

07/08/25

## Slide 32

## A legitimate MITM

**Attacker tunnels NGAP/NAS traffic in a GTP-U packet and UPF will bridge it straight to the AMF**

34

FAST IOT

07/08/25

## Slide 33

## A legitimate MITM

**Encryption and intergerity protection keys are directly handed over to attacker controlled gNodeB**

35

FAST IOT

07/08/25

## Slide 34

## NGAP tunneled inside GTP-U

###### SCTP and NGAP encapsulated inside attacker’s GTP session

36

FAST IOT

07/08/25

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
NGAP tunneled inside GTP-U
SCTP and NGAP encapsulated inside attacker’s GTP session
Protocol Length Info
GTP <SCTP> 356 INIT_ACK
GTP <SCTP> 328 COOKIE_ECHO
GTP <SCTP> 100 COOKIE_ACK
GTP <NGAP> 184 NGSetupRequest
NGAP 128 NGSetupResponse
GTP <SCTP> 172 DATA (TSN=0) (retransmission)
GTP <SCTP> 156 HEARTBEAT
GTP <SCTP> 156 HEARTBEAT_ACK
GTP <NGAP/NAS-5GS> 188 InitiaLUEMessage, Registration request
NGAP/NAS-5GS 152 SACK (Ack=1, Arwnd=106496) , DownLinkNASTransport, Authentication request
GTP <NGAP/NAS-5GS> 196 SACK (Ack=1, Arwnd=106496) , UplinkNASTransport, Authentication response
NGAP/NAS-5GS 132 SACK (Ack=2, Arwnd=106496) , DownLinkNASTransport, Security mode command
GTP <SCTP> 176 SACK (Ack=2, Arwnd=106496) DATA (TSN=2) (retransmission)
GTP <NGAP/NAS-5GS/NAS-5GS> 240 SACK (Ack=2, Arwnd=106496) , UplinkNASTransport, Security mode complete, Registration
NGAP/NAS-5GS 248 SACK (Ack=3, Arwnd=106496) , InitialContextSetupRequest, Registration accept
GTP <SCTP> 292 SACK (Ack=3, Arwnd=106496) DATA (TSN=3) (retransmission)
GTP <NGAP/NAS-5GS> 292 UplinkNASTransport, Registration complete, UplinkNASTransport, UL NAS transport, PDU
NGAP/NAS-5GS 148 SACK (Ack=6, Arwnd=106496) , DownLlinkNASTransport, Configuration update command
GTP <SCTP> 192 SACK (Ack=6, Arwnd=106496) DATA (TSN=4) (retransmission)
NGAP/NAS-5GS 256 PDUSessionResourceSetupRequest, DL NAS transport, PDU session establishment accept
GTP <SCTP> 300 DATA (TSN=5) (retransmission)
GTP <NGAP> 152 PDUSessionResourceSetupResponse
GTP <SCTP> 156 HEARTBEAT
GTP <SCTP> 156 HEARTBEAT_ACK
07/08/25 36
```

## Slide 35

## Legitimate interception

- GnodeB receives crypto keys from AMF for security setup with UE – Full visibility to authentication and registration process

   - Custom UPF or forward traffic directly to external networks, bypassing the legitimate UPF

   - Bi-directional IP traffic to flow through the rogue gNodeB  as if the connection were legitimate

Rogue gNodeB

37

FAST IOT

07/08/25

## Slide 36

## Impact

- Full interception & redirection of user traffic by a attacker-controlled gNodeB – Attacker gains control over critical functions such as user data paths, DNS resolution, handovers, and service availability

   - All inside an legitimate and encrypted session

- Voice call (VoNR) can be intercepted, SMS delivery can be controlled

- **Cannot defend: existing 5G security mechanisms—such as mutual authentication, encryption, integrity protection, and downgrade prevention**

- Previously required sophisticated setups in 4G can now be executed over a simple data connection, significantly lowering the barrier to exploitation.

- ● Stingray detectors and all UE-side security solutions will fail

38

FAST IOT

07/08/25

## Slide 37

The root problem

Dr. Altaf Shaik - Fast IOT

07/08/25

39

## Slide 38

## Long sustained protocol

- GTP-U: Notorious  protocol from 2G still used in 5G and maybe in 6G too

   - Due to simple forwarding, low performance overhead

   - Inherently suitable for tunneling

   - lacks built-in integrity checks or source authentication

   - forwarding based solely on the destination IP and TEID

   - design does not inspect header and payload contents

- Modern UPFs are processing tunneled or encapsulated packets – Permits control plane protocol payloads and bridge them to AMF/SMF

40

FAST IOT

07/08/25

## Slide 39

Rethinking trust in the user plane

Dr. Altaf Shaik - Fast IOT

07/08/25

41

## Slide 40

## No easy solution

- Tunneling is well exploited over roaming interfaces

- Complex infrastructures to be seen with 5G slicing, virtualized, private cores, edge computing.

   - Privately controlled UPFs – prone to misconfigurations

   - Skills in understanding the attacks, abnormal protocol flows

- Expensive solutions from vendors – limited budget, no monitoring (takeaways from latest telco incidents)

- GTP exploited by Liminal panda to tunnel C2 traffic – security solutions less likely to inspect and restrict GTP-encapsulated traffic [ref]

- Regulations and restrictions around GTP and user plane data inspection

42

FAST IOT

07/08/25

## Slide 41

Recommendations & way forward

Dr. Altaf Shaik - Fast IOT

07/08/25

43

## Slide 42

### Disclosure

- All open source developers and commercial vendors are notified

- Some fixed it and some require budget approvals and more scrutiny

- CVEs in progress

- Disclosed to GSMA in their FSAG meeting

   - Work in progress to include the attacks in this research to GTP security guidelines and recommendations

44

FAST IOT

07/08/25

## Slide 43

### Fixing it

- Firewalls recommended, extensive guidelines from GSMA (IR.88, FS.37)

- Underlying root cause fixes need systemic level changes – Handling GTP-U and its malicious mutations

- Tackling the protocol design

   - Encapculation depth, rate limiting, TEIS/SEID allocation & management

- Routing security into UPF

   - security into packet-processing frameworks

- Misconfigurations: segmentation, routing awareness, isolation enforcement

- Dropping encapsulated GTP packets – already GMSA marks them fradulent – Not only packets from external GRX (or IPX) but packets from RAN too

45

FAST IOT

07/08/25

## Slide 44

## Takeaways

- Modern UPFs still vulnerable to encapsulated GTP-U attacks – Opens door for tunneling and bridging attacks

- Insecure practices inside UPFs – Identifier allocation, management and rate limiting

- Six different 5G core networks tested and more than 80% of them are affected including commercial cores

- Vulnerable UPFs plus relaxed security setting inside core

   - New, powerful, and undetecteable attacks on subscribers and core

   - Billing fraud and legitimate MITM doing interception

- Insufficient guidelines on UPF secure design practices

- Full research will be published in ACM CCS this October and a preprint is here

46

FAST IOT

07/08/25

## Slide 45

### The analogy: Titanic and 5G

- Titanic’s compartments = 5G’s isolated trust boundaries (control/user planes, network slices, interfaces).

- Iceberg impact = malicious UE traffic

- Water flowing over boundaries = protocol tunneling + boundary bridging.

- Overconfidence in “unsinkable” architecture = misplaced trust in standard 5G isolation.

47

FAST IOT

07/08/25

## Slide 46

# Thank You!

Questions/Comments/Concerns?

altaf.shaik@fastiot.org

Dr. Altaf Shaik - Fast IOT

07/08/25

48
