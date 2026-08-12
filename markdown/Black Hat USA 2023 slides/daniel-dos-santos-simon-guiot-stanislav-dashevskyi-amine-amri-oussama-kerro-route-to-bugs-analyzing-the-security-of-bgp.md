---
title: "Route to Bugs Analyzing the Security of BGP Message Parsing"
speakers: ["Daniel dos Santos", "Simon Guiot", "Stanislav Dashevskyi", "Amine Amri", "Oussama Kerro"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/Daniel dos Santos & Simon Guiot & Stanislav Dashevskyi & Amine Amri & Oussama Kerro_Route to Bugs Analyzing the Security of BGP Message Parsing.pdf"
pages: 33
sha256: "963e2f56e5f44d760aff1bccb53ba043c280b91f03230c8330537993f830b492"
text_chars: 17684
ocr_pages: 3
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:15:27Z"
---
# Route to Bugs Analyzing the Security of BGP Message Parsing

**Speakers:** Daniel dos Santos, Simon Guiot, Stanislav Dashevskyi, Amine Amri, Oussama Kerro  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Daniel dos Santos & Simon Guiot & Stanislav Dashevskyi & Amine Amri & Oussama Kerro_Route to Bugs Analyzing the Security of BGP Message Parsing.pdf` (33 pages)


## Slide 1

Route to Bugs: Analyzing the Security of BGP Message Parsing <u>Daniel dos Santos, Simon Guiot,</u> Stanislav Dashevskyi, Amine Amri, Oussama Kerro

#BHUSA @BlackHatEvents

## Slide 2

### Who We Are

- **Daniel dos Santos** , Head of Security Research

- **Simon Guiot** , Security Researcher

- **Stanislav Dashevskyi** , Principal Security Researcher

- **Amine Amri** , Security Researcher

- **Oussama Kerro** , Intern

_“At Forescout Vedere Labs we analyze the security implications of hyper connectivity and IT-OT convergence.”_

#BHUSA @BlackHatEvents

## Slide 3

### Relevant Past Research

- **2020-21 Project Memoria** – large-scale analysis of embedded TCP/IP stacks

   - **AMNESIA:33** – 33 CVEs on 4 open-source stacks **@ Black Hat EU 2020**

   - **NUMBER:JACK** – 9 CVEs on TCP ISN

   - **NAME:WRECK** – 9 CVEs on DNS clients **@ Black Hat Asia 2021**

   - • **INFRA:HALT** – 14 CVEs on a stack popular in OT **@ Hack in the Box 2021**

   - **NUCLEUS:13** – 13 CVEs on a stack popular in healthcare

- Showed that different **implementations of the same protocol tend to fail the same way**

<u>https://datatracker.ietf.org/doc/rfc9267/</u>

<u>https://i.blackhat.com/eu-20/Wednesday/eu-20-dosSantos-How-EmbeddedTCPIP-Stacks-Breed-Critical-Vulnerabilities-wp.pdf</u> #BHUSA @BlackHatEvents

#BHUSA @BlackHatEvents

## Slide 4

### Talk Summary

## 01

###### BGP is widely used

For Internet routing and other settings.

Most security research focuses on well-known issues of routing security instead of software vulnerabilities.

## 02

###### Implementations can also be vulnerable

Analyzed 4 closed source and 3 open-source implementations

Found permissive handling of messages and 3 new DoS vulnerabilities in a leading opensource implementation

Only TCP spoofing required to inject malformed packets in some cases

## 03

###### Conclusion

Pay attention to routing security, but don’t forget about software vulnerabilities

Released a fuzzer and testing tool to help organizations test their deployments and researchers find new vulnerabilities

#BHUSA @BlackHatEvents

## Slide 5

# **BGP**

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisek hat
USA &
#BHUSA @BlackHatEvents
```

## Slide 6

#### The Internet in a Nutshell

This research
Network A Network B
Router Router
Data packets
IT/IoT/OT IT/IoT/OT
devices devices
Our previous
research

#BHUSA @BlackHatEvents

## Slide 7

#### What is BGP?

- **Routing for the Internet**

-

- Protocol to exchange routing and reachability information among Autonomous Systems (AS)

- AS is a block of IPs leased to an organization by a registrar (e.g., RIPE NCC) for a time period

- BGP is used to advertise ASNs and peer networks that are considered each to be part of an AS

- Internal BGP (peers within AS) and External BGP (peers on the Internet)

- **Makes routing decisions** based on paths, network policies, and rule-sets

#BHUSA @BlackHatEvents

## Slide 8

#### Other use cases

Internal data center routing

Embedded in custom appliances

MPLS VPN across organization sites

Kubernetes load balancing

…

**In summary: BGP security is not just for ISPs and IXes**

#BHUSA @BlackHatEvents

## Slide 9

##### BGP Basics

**Simple** state machine

Relatively **straightforward** packets

**Limited** set of messages: OPEN, UPDATE, NOTIFICATION, KEEPALIVE

**What could go wrong?**

#BHUSA @BlackHatEvents

## Slide 10

#### When BGP Fails

- BGP has **no built-in security** , such as an authentication and authorization mechanism

- **Mistakes or intentional attacks** lead to **network outages and traffic redirection**

   - Hijacks – when a network originates a prefix owned by another network without permission

   - Leaks – when a network propagates a routing announcement beyond its intended scope

- Issues **known for a long time but still** **_thousands_ of incidents per year**

<u>https://www.manrs.org</u> and <u>t.ly/3Zc6</u>

#BHUSA @BlackHatEvents

## Slide 11

#### Traditional BGP Security

- **RFC4272** : BGP Security Vulnerabilities Analysis (2006)

- Main concern is to **filter incorrect or malicious routing information**

   - **Origin** validation – verify that a network announcing a route is authorized to do it

   - **Path** validation – ensure that no unauthorized network has diverted traffic by a false route

   - Path plausibility – determine the plausibility of a network included in the AS path

<u>https://doi.org/10.1787/20716826</u>

- _What about vulnerabilities in_ **_BGP implementations_** _?_

•

#BHUSA @BlackHatEvents

## Slide 12

#### When BGP Fails Because of Software Flaws

<u>https://www.zdnet.com/article/internet-experiment-goes-wrong-takes-down-a-bunch-of-linux-routers/</u>

#BHUSA @BlackHatEvents

## Slide 13

#### Why Research BGP implementations?

-

   - **Latest systematized** work we found about testing BGP implementations was **20 years ago**

   - <u>https://www.blackhat.com/presentations/bh-usa-03/bh-us-03-convery-franz-v3.pdf</u>

   - Team at Cisco looked at implementation and configuration of BGP across vendors

   - Created a fuzzer, analyzed 7 implementations and found 4 new CVEs

   - Concluded that misconfigurations were more dangerous than implementation issues

- **In 2007** , team at Juniper analyzed **UPDATE message handling** in several vendors

   - <u>https://www.kb.cert.org/vuls/id/929656</u>

   - Mishandling could lead to DoS

   - 7 vendors affected, 10 not affected, 25 unknown

- In the meantime, **129 CVEs** on BGP implementations, including **RCEs**

   - 123 (95%) because of message parsing issues

#BHUSA @BlackHatEvents

## Slide 14

#### Previous Vulnerabilities

CVEs per implementation
Arista EOS ZebOS OpenBGPd
1% 1% 1%
BIRD Juniper
JunOS
2%
32%
Protocol
parsers
11%
Quagga +
FRR Cisco
22% 30%
CVEs per impact
Others (auth
RCE
bypass)
6%
2%
Information
leak
10%
DoS
82%

CVEs per year
20
18
16
14
12
10
8
6
4
2
0
2002 2005 2006 2007 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022

#BHUSA @BlackHatEvents

## Slide 15

#### Current Threat Landscape

-

###### **Threat actors focusing on network infrastructure**

   - China: <u>https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-158a</u>

   - Russia: <u>https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-108</u>

   - Ransomware groups, other cybercriminals, hacktivists, …

   - Recent CISA BOD 23-02: <u>https://www.cisa.gov/news-events/directives/binding-operational-directive-23-02</u>

- Still **several BGP implementations** were not systematically analyzed

- **Open BGP implementations** are gaining traction with NFD

- Many different implementations of _routing platforms, network operating systems, looking glass servers_ and other **routing components.** We catalogued:

   - 52 routing protocols, 40 open

   - 20 routing platforms, 17 open

   - 53 Network Operating Systems, 20 open

#BHUSA @BlackHatEvents

## Slide 16

#### Known Exploited Vulnerabilities Routers

Conferencing system 1
IP Camera / NVR 3
VPN 3
OT 4
VoIP 7
Hypervisor 12
NAS 14
Security Appliance 42
Router 88
0 10 20 30 40 50 60 70 80 90 100

- CISA tracks 925 known exploited vulnerabilities (May 2023)

- Most affect IT software, but 179 can be mapped to specific devices

- Of those, 88 (49%) target _routers_

- See (Shandilya, VB2019) as to why <u>https://www.virusbulletin.com/uploads/pdf/magazine/2 019/VB2019-Shandilya.pdf</u>

Based on data from <u>https://www.cisa.gov/known-exploited-vulnerabilities-catalog</u>

#BHUSA @BlackHatEvents

## Slide 17

#### Known Exploited Vulnerabilities BGP

###### Out of those 88, **3 decades-old CVEs affecting Cisco BGP being exploited in 2022** :

|**CVE ID**|**Vendor**|**Product**|**Description**|**Impact**|**Date Added**|
|---|---|---|---|---|---|
|**CVE-2010-**
**3035**|Cisco|IOS XR|Cisco IOS XR, when BGP is the configured
routing feature, allows remote attackers to
cause a denial-of-service.|DoS|2022-03-25|
|**CVE-2009-**
**2055**|Cisco|IOS XR|Out-of-bounds
read
when
processing
a
malformed BGP OPEN message with an
Extended
Optional
Parameters
Length
option. This is a different issue from CVE-
2022-40302.|DoS|2022-03-25|
|**CVE-2017-**
**12319**|Cisco|IOS XE|Out-of-bounds
read
when
processing
a
malformed
BGP
OPEN
message
that
abruptly ends with the option length octet (or
the option length word, in case of OPEN with
extended option lengths message).|DoS|2022-03-03|

###### Also 2 other DoS on Cisco IOS XR routing: CVE-2020-3566 and CVE-2020-2569 affecting DVMRP

Based on data from <u>https://www.cisa.gov/known-exploited-vulnerabilities-catalog</u>

#BHUSA @BlackHatEvents

## Slide 18

# **Finding Vulnerabilities**

#BHUSA @BlackHatEvents

## Slide 19

#### Methodology

Analysis and  Static and
Discussion of
reproduction of  Target selection dynamic
results
prior work analysis

- **Prior work discussed in the previous section**

- **Target selection**

   - All implementations with published vulnerabilities + Mikrotik - ZebOS (== _most popular implementations_ )

   - 3 open source: FRRouting, BIRD, OpenBGPd

   - 4 closed source: Mikrotik RouterOS, Juniper JunOS, Cisco IOS, Arista EOS

- **Static and dynamic analysis**

   - Anti-patterns and strategies derived from RFCs + previous vulnerabilities + previous experience with protocol parsing

   - • Reverse engineering for closed-source implementations

   - Specific black-box fuzzers for each message type

• **Results in the next slides**

#BHUSA @BlackHatEvents

## Slide 20

#### Manual analysis Anti-patterns

- **Distilled anti-patterns**

   **1. Type-Length-Value** fields in BGP messages

   **2. Optional TLV parameters** in OPEN messages

   **3. Route/path length fields** in UPDATE messages

   4. Peer **responds to any OPEN** message

   5. Peer **accepts UPDATE messages** without exchanging OPEN messages

   6. Handling of **BGP extensions**

- **Results:** no CVE found by manual analysis, BUT…

#BHUSA @BlackHatEvents

## Slide 21

##### Results Handling of OPEN responses

|**Implementation**|**Description**|
|---|---|
|**FRRouting**|Proceeds with a TCP handshake, terminates the TCP session (TCP Reset packet) after an OPEN
packet is received.
Performs someprocessingof OPEN messages, before validatingthe BGP ID and ASN fields.|
|**BIRD**||
|**OpenBGPd**|Proceeds with a TCP handshake, terminates the TCP session (TCP Reset packet) after an OPEN|
|**Mikrotik RouterOS**|packet is received.|
|**Arista EOS**||
|**Juniper JunOS**|Proceeds with a TCP handshake. Sends back an OPEN message, sends back a Cease
NOTIFICATION message with the subcode 5 (Connection Rejected).|
|**Cisco IOS**|Does not allow to establish a TCP connection(TCP handshake fails).|

- Most implementations proceed with TCP handshake before checking if OPEN message comes from pre-configured peer because the BGP daemon runs in user mode (except for Cisco IOS)

- • Connection filtering not happening on the kernel level

- **FRRouting decapsulates optional parameters** before verifying BGP ID and ASN fields, which means that attackers only need to spoof the originating IP address #BHUSA @BlackHatEvents

#BHUSA @BlackHatEvents

## Slide 22

#### Fuzzing

- **Could not find open BGP fuzzer, so developed our own**

- **Stateful fuzzer that will:**

   - Establish a session with a peer

   - Run test cases based on the anti-patterns we defined

_Thanks to Joshua Pereyda and the BooFuzz contributors._

   - For each test case, send malformed message with specific payload (based on boofuzz)

      - OPEN, UPDATE, ROUTE REFRESH, NOTIFICATION

   - Test the target for crashes via a custom RPC monitor (based on boofuzz procmon)

- **Freely available** on <u>https://github.com/Forescout/bgp_boofuzzer</u>

   - Lots of opportunities to improve it – please contribute!

#BHUSA @BlackHatEvents

## Slide 23

#### Fuzzing demo

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
f
pifekhat te <
USA 20253
Activities ) OBS Studio v jun 30 14:06
BGP Fuzzer (latest) [Running] - Oracle VM VirtualBox BGP Target (latest) [Running] - Oracle VM VirtualBox
lle Machine View Input Devices Help
File Machine View Input Devices Help
Activities © Terminal jun 30 14:06
Activities ©) Terminal jun 30 14:06
standash@standash-ubuntu: ~/fuzzer Q standash@standash-ubuntu: ~/fuzzer/bgp_boofuzzer
ras maw E $
OBS 25.0.3+dfsg1-2 (linux) - Profile: Untitled - Scenes: Untitled x
Scene Collection Tools Help
(ous 2:.3.dfgt-2 linus) - raf Untied - Sees: Uniled
Scenes Sources Audio Mixer Scene Transitions Controls
[I Screen Capture (XSHN Desktop Audio -inf dB Fade Start Streaming
stp ae Start Recording
Duration 300 ms & Studio Mode
= @) &
Mic/Aux -inf dB
E : Settings
= - @) Exit
LIVE: 00:00:00 REC: 00:00:00 CPU: 2.0%, 60.00 Fps
@ G1 @@ right ctrl
i ee at
@ GUGM right ctr
```

## Slide 24

#### Results New CVEs

|**CVE ID**|**Tested Product**|
**Description**|**Potential Impact**|
|---|---|---|---|
|**CVE-2022-40302**|FRRouting 8.4|Out-of-bounds read when processing a malformed
BGP OPEN message with an Extended Optional
Parameters Length option.|DoS|
|**CVE-2022-40318**|FRRouting 8.4|Out-of-bounds read when processing a malformed
BGP OPEN message with an Extended Optional
Parameters Length option. This is a different issue from
CVE-2022-40302.|DoS|
|**CVE-2022-43681**|FRRouting 8.4|Out-of-bounds read when processing a malformed
BGP OPEN message that abruptly ends with the option
length octet (or the option length word, in case of
OPEN with extended option lengths message).|DoS|

- Very low hanging fruits – found quickly by the fuzzer

- Very similar to the Cisco IOS XR issues being currently exploited

- Issues reported to the FRRouting team and fixed _very_ quickly (same day in some cases)

#BHUSA @BlackHatEvents

## Slide 25

#### CVE-2022-43681

Root cause: Insufficient bounds checks of extended option length octets in OPEN messages

If option length octet == 0xff, then read the next octet ( _opttype_ ) If opttype == 0xff, the msg contains extended optional params, then read next word ( _optlen_ )

If malformed message ends with one 0xff, this call will read 1 octet beyond packet

If malformed message ends with two 0xff, this call will read 1 word beyond packet

#BHUSA @BlackHatEvents

## Slide 26

#### CVE-2022-40302

Root cause: Insufficient bounds checks when reading the AS4 capability of OPEN messages

Function called before processing other options. _Iterates over all options to find and parse AS4 capability._

Attacker can craft packet that passes check on line 12 and reaches here, reading 1 byte out - of - bounds

Checks for 2 bytes against received option length

If message has optional parameters with extended length, read 3 bytes

#BHUSA @BlackHatEvents

## Slide 27

#### CVE-2022-40318

Root cause: Similar to previous one, but goes through _peek_for_as4_capability()_ and triggered later in _bgp_open_option_parse()_

Again, accounts for 2 octets in a packet with regular option length

Fails to account for extended option lengths (3 octets)

Read out of bounds here

#BHUSA @BlackHatEvents

## Slide 28

# **Conclusion**

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisek hat
USA &
Conclusion
#BHUSA @BlackHatEvents
```

## Slide 29

#### Impact Summary

- **Any of the 3 new CVEs leads to DoS on a vulnerable BGP peer**

   - Dropping all BGP sessions and routing tables and rendering the peer unresponsive for several seconds

   - • BGP service will automatically restart after a timeout

   - DoS may be prolonged indefinitely by repeatedly sending malformed packets

- **Two issues can be triggered before FRRouting validates BGP Identifier and ASN fields**

   - In this case attackers only need to spoof a valid IP address of a trusted peer

- **Beyond these vulnerabilities**

   - More than 330,000 hosts with BGP enabled on the Internet

   - More than 200,000 hosts running Quagga (project from which FRR is forked)

   - More than 1,000 hosts running FRRouting

#BHUSA @BlackHatEvents

## Slide 30

##### Supply Chain Issues

Networking OSes

Networking End Vendors Users

Open-source routing platform (1k+ forks)

<u>https://www.nextplatform.com/2020/10/26/frr-the-most-popular-network-router-youve-never-heard-of/</u>

#BHUSA @BlackHatEvents

## Slide 31

#### Risk Mitigation

- Routing security is **still very important. Several good guides:**

   - Mutually Agreed Norms for Routing Security (MANRS)

   - RFC7454 – BGP Operations and Security

   - NIST SP800-189 Resilient Interdomain Traffic Exchange: BGP Security and DDoS Mitigation

   - _Many others…_

<u>www.manrs.org</u>

- But threat actors have been attacking networking infrastructure devices directly

   - **Don’t forget software vulnerabilities** and securing networking devices

   - Identify all devices in your network that may be using BGP

   - Assess vulnerabilities and patch when possible

- Fuzzer we released comes with prepared test-cases for the CVEs we found to be tested against your network

#BHUSA @BlackHatEvents

## Slide 32

#### Takeaways & Future Work

- **Takeaways**

   - BGP is crucial for the Internet and widely used beyond ISPs and IXes

   - Unlike embedded TCP/IP stacks, BGP implementations have matured and in general do not have obvious mistakes, but popular BGP implementations still have vulnerabilities or are too permissive

   - Network Function Disaggregation will make some open implementations very popular – it’s important to keep the security of these projects in check.

   - Threat actors are exploiting these kinds of issues

   - Mitigation should not be only about routing security and is not entirely up to your ISP

      - <u>https://www.forescout.com/resources/analyzing-the-security-of-bgp-message-parsing/</u>

- **Future work**

   - Keep fuzzing new versions and new implementations – improve the fuzzer with new test cases

   - Explore other parts of the routing attack surface: other routing protocols, looking glass servers, remote control (e.g., Quagga VTY)

#BHUSA @BlackHatEvents

## Slide 33

**Thank you!** <u>https://www.forescout.com/research-labs-overview/</u>

<u>Daniel.dosSantos@forescout.com Simon.Guiot@forescout.com Stanislav.Dashevskyi@forescout.com Amine.Amri@forescout.com Oussama.kerro@pwn-diaries.com</u>

#BHUSA @BlackHatEvents
