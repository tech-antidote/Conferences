---
title: "Ghost Calls Abusing Web Conferencing for Covert Command & Control"
speakers: ["Adam Crosser"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33/Adam Crosser - Ghost Calls Abusing Web Conferencing for Covert Command & Control.pdf"
pages: 103
sha256: "3db95ecfb68e9eb8894876440b523c9a58e8ff509079ab6bbd744196a073759e"
text_chars: 29355
ocr_pages: 57
has_ocr: true
redacted_secrets: 0
ocr_confidence: 90.7
ocr_unreliable_blocks: 5
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:53:49Z"
---
# Ghost Calls Abusing Web Conferencing for Covert Command & Control

**Speakers:** Adam Crosser  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33/Adam Crosser - Ghost Calls Abusing Web Conferencing for Covert Command & Control.pdf` (103 pages)


## Slide 1

Ghost Calls: Abusing Web Conferencing for Covert Command & Control Ghost Calls: Abusing Web Conferencing for Covert Command & Control Adam Crosser

#BHUSA @BlackHatEvents

## Slide 2

# Introduction

Adam Crosser

Praetorian

LinkedIn: <u>https://www.linkedin.com/in/adam-crosser-366263265</u> X:              https://x.com/UNC1739

## Slide 3

Types of Command-and-Control Channels

## Slide 4

Types of Command-and-Control Channels

## Slide 5

Types of Command-and-Control Channels


> Recovered by OCR — confidence 95/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Types of Command-and-Control Channels
SHORT LONG
4 ©
```

## Slide 6

Types of Command-and-Control Channels


> Recovered by OCR — confidence 91/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Types of Command-and-Control Channels
SHORT LONG BACKUP
=
```

## Slide 7

Types of Command-and-Control Channels


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Types of Command-and-Control Channels
P2P
```

## Slide 8


> Recovered by OCR — confidence 85/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BRAINSTORMING
SOLUTIONS
CLOUD <i>
STORAGE ‘DNS;
DNS OVER
HTTPS
EMAIL
MESSAGING
```

## Slide 9

Ideal Short-Term Command and Control

## Slide 10

# Ideal Short-Term Command and Control

# LATENCY

## Slide 11

# Ideal Short-Term Command and Control

# LATENCY

# THROUGHPUT

## Slide 12

# Ideal Short-Term Command and Control

THROUGHPUT REACH

# LATENCY

## Slide 13

# Ideal Short-Term Command and Control

THROUGHPUT

# LATENCY

REACH

TRUST

## Slide 14

# Selection Criteria

- Focused on services egressing from user devices

- • Must be broadly used across enterprise roles

- Applicable to non-technical departments (e.g., HR, sales)

- Protocols favored by technical users were excluded

- • Thought through common workflows and use-cases

## Slide 15

# DNS over HTTP (DoH)

LATENCY THROUGHPUT REACH TRUST

## Slide 16

# Cloud File Storage

LATENCY THROUGHPUT REACH TRUST

## Slide 17

# Attacker Virtual Machine with Classified Domain

LATENCY THROUGHPUT REACH TRUST

## Slide 18

# Email and Messaging Applications

LATENCY THROUGHPUT REACH TRUST

## Slide 19

# Web Conferencing

LATENCY THROUGHPUT REACH TRUST

## Slide 20

# Microsoft Teams Split Tunneling Guidelines

<u>https://learn.microsoft.com/en-us/microsoftteams/prepare-network</u>


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Microsoft Teams Split Tunneling Guidelines
Configure split- We recommend that you provide an alternate path for Teams traffic that bypasses the virtual private network
tunnel VPN (VPN), commonly known as split-tunnel VPN. Split tunneling means that traffic for Microsoft 365 or Office 365
doesn't go through the VPN but instead goes directly to Microsoft 365 or Office 365. Bypassing your VPN has a
positive impact on Teams quality, and it reduces load from the VPN devices and the organization's network. To
implement a split-tunnel VPN, work with your VPN vendor.
Other reasons why we recommend bypassing the VPN:
e VPNs are typically not designed or configured to support real-time media.
Some VPNs might also not support UDP (which is required for Teams).
VPNs also introduce an extra layer of encryption on top of media traffic that's already encrypted.
Connectivity to Teams might not be efficient due to hair-pinning traffic through a VPN device.
Traffic might be routed to a service front door location that is further away from the end user, introducing
extra latency and jitter.
https://learn.microsoft.com/en-us/microsoftteams/prepare-network
```

## Slide 21

# Microsoft Teams TLS Inspection

<u>https://learn.microsoft.com/en-us/microsoftteams/proxy-servers-for-skype-for-business-online</u>


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Microsoft Teams ILS Inspection
Not using a proxy server is recommended
Many organizations utilize proxy servers today within their network. As Microsoft Teams and Skype for Business ar
traffic is already encrypted, passing this traffic through a proxy server doesn't make the traffic any more secure.
Proxies can cause issues too. Performance-related problems can be introduced to the environment through latency and
packet loss by attempting to route Teams traffic through a proxy server. This can be caused by the proxy being unable
to handle the amount of traffic passing through it, or by incorrectly routing the traffic to a Microsoft network service
front door location that is further away from the end user.
Issues such as these will result in a negative experience within Teams and Skype for Business.
We recommend that Teams traffic bypasses proxy server infrastructure, including SSL inspection. You may wish to
achieve this by putting Teams Phones and Meeting Room devices on their own VLAN and providing them with Internet
access.
https://learn.microsoft.com/en-us/microsoftteams/proxy-servers-for-skype-for-business-online
```

## Slide 22

# Zoom Split Tunneling Recommendations

<u>https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0065998</u>


> Recovered by OCR — confidence 95/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Zoom Split Tunneling Recommendations
VPN Split Tunneling
Recommendations
@ English (Original) Vv &3 2025-03-06 16:55:57 =< Copy Permalink
Virtual Private Network (VPN) services are crucial to securing data accessed by users working from remote locations.
One of the biggest challenges Zoom customers experience is related to not allowing our real-time media services over UDP 8801-
8810 to split tunnel. Not allowing split tunneling for UDP 8801-8810 and TCP 443 to Zoom resources, does cause customers to
experience significant additional load on their corporate internet connections due to the Zoom traffic having to enter the corporate
network, only to exit again to the Zoom cloud for real-time meeting termination. This also places a significant amount of burden on
VPN concentrators and in many cases can cause overloading and congestion of this infrastructure.
```

## Slide 23

# Zoom TLS Inspection Recommendations

<u>https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0060548</u>


> Recovered by OCR — confidence 95/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Zoom TLS Inspection Recommendations
Proxy server
We support HTTPS/SSL proxy servers via port 443 for Zoom traffic.
Note: This does not apply to the Zoom Phone service.
Zoom automatically detects your proxy settings. In some instances, you may be prompted to enter the proxy username/password.
Note: We recommend allowing Zoom.us and *.zoom.us from proxy or SSL inspection.
```

## Slide 24

# Quick Disclaimer

- Providers aren’t being malicious

- Performance is the main design driver

- Latency must be minimized for app reliability

- These configs are often intentional not careless

- • Inspection or routing can overwhelm systems

## Slide 25

## Slide 26

General Web Conferencing Architecture


> Recovered by OCR — confidence 95/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
General Web Conferencing Architecture
End User
Device
Network
Firewall
```

## Slide 27

General Web Conferencing Architecture


> Recovered by OCR — confidence 89/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
General Web Conferencing Architecture
Frontend
Amazon Application
CloudFront
as Load Balancer Main SaaS
| 4 Application
End User Network
Device Firewall
```

## Slide 28

General Web Conferencing Architecture


> Recovered by OCR — confidence 90/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
General Web Conferencing Architecture
Frontend
Amazon Application
CloudFront
a Load Balancer Main SaaS
i Vy ] Application
End User Network
Device Firewall 443/TCP
3478/UDP 3478/UDP 3478/UDP
8801/UDP
TURN STUN Media
Servers Servers Servers
(SFU)
```

## Slide 29

What is TURN?

<u>source</u>

## Slide 30

WebRTC Core Protocols


> Recovered by OCR — confidence 93/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
WebRIC Core Protocols
DTLS SCTP ICE SRTP
```

## Slide 31

# WebRTC Handshake Process

<u>source</u>


> Recovered by OCR — confidence 92/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
WebRIC Handshake Process
HTTPS server
and signaling
M server *& Sp
: Secure RTP Bob
Alice Media path: DTLS Handshake,
(Private key B,
(Private key A,
certificate B)
(Web browser running
certificate A)
(Web browser running
web application from web application from
web server) web server)
source
```

## Slide 32

Reverse Engineering Zoom


> Recovered by OCR — confidence 91/100 on the text kept, 89/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Reverse Engineering Zoom
Internet Protocol Version 4, Src: 192.168.1.41, Dst: 170.114.164.95
User Datagram Protocol, Src Port: 61029, Dst Port: 8801
Zoom SFU Encapsulation
Type: 5
Sequence number: 1278
Direction: @ (to Zoom)
Zoom Media Encapsulation
Type: 16 (Video)
Sequence number: 1261
Timestamp: 106179922
Frame number: 57
Packets in frame: 2
Real-Time Transport Protocol
[Stream setup by DECODE AS (frame 28373) ]
10.. .... = Version: RFC 1889 Version (2)
».@. «2s. = Padding: False
@000 = Contributing source identifiers count: @
1... .... = Marker: True
Payload type: DynamicRTP-Type-98 (98)
Sequence number: 24484
[Extended sequence number: 90020]
Timestamp: 894589134
[Extended timestamp: 5189556430]
Synchronization Source identifier: @x@1000401 (16778241)
Defined by profile: RFC 5285 One-Byte Header Extensions (@xbede)
Extension length: 5
Header extensions
Payload [..]: 1¢40736b27a5415cf9715dd657876f8c59f 14a70c4c6878987c74f26b8123f633690b6ef5ccee1e88f5932228eadc93eefe91c9Ff2
```

## Slide 33

Reverse Engineering Zoom


> Recovered by OCR — confidence 94/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Reverse Engineering Zoom
Internet Protocol Version 4, Src: 192.168.1.41, Dst: 170.114.164.95
User Datagram Protocol, Src Port: 61029, Dst Port: 8801
Zoom SFU Encapsulation
```

## Slide 34

Reverse Engineering Zoom


> Recovered by OCR — confidence 95/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Reverse Engineering Zoom
User Datagram Protocol, Src Port: 61029, Dst Port: 8801
Zoom SFU Encapsulation
Type: 5
Sequence number: 1278
Direction: @ (to Zoom)
Zoom Media Encapsulation
Type: 16 (Video)
Sequence number: 1261
Timestamp: 106179922
Frame number: 57
Packets in frame: 2
Real-Time Transport Protocol
[Stream setup by DECODE AS (frame 28373) ]
```

## Slide 35

# Building on Existing Work

Enabling Passive Measurement of Zoom Performance in Production Networks

Custom Wireshark Analyzer for Zoom Desktop Media Traffic

<u>https://dl.acm.org/doi/pdf/10.1145/3517745.3561414</u>

<u>https://github.com/Princeton-Cabernet/zoom-analysis</u>

## Slide 36

Reverse Engineering Google Meet


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Reverse Engineering Google Meet
Frame 4296: 160 bytes on wire (128@ bits), 160 bytes captured (128@ bits)
Ethernet II, Src: Apple_d5:f9:5f (14:7d:da:d5:f9:5f), Dst: zte_4c:ac:24 (20:08:89:4c:ac: 24)
Internet Protocol Version 4, Src: 192.168.1.43, Dst: 74.125.250.251
User Datagram Protocol, Src Port: 63070, Dst Port: 3478
Real-Time Transport Protocol
[Stream setup by DTLS-SRTP (frame 2963)]
10.. .... = Version: RFC 1889 Version (2)
..Q. «22. = Padding: False
+1 .... = Extension: True
. 0000 = Contributing source identifiers count: @
(1) .»++ = Marker: False
Payload type: Unassigned (63)
Sequence number: 24725
[Extended sequence number: 90261]
Timestamp: 345165098
[Extended timestamp: 4640132394]
Synchronization Source identifier: @xa11f30@c7 (2703175879)
Defined by profile: RFC 5285 One-Byte Header Extensions (@xbede)
Extension length: 3
Header extensions
RFC 5285 Header Extension (One-Byte Header)
RFC 5285 Header Extension (One-Byte Header)
RFC 5285 Header Extension (One-Byte Header)
SRTP Encrypted Payload: 56046ee649b15872c7d5a1f0b3604bf7ee71d42d8d55062dc3c6a639ae063054d04ea8469F2495cf5c3¢
SRTP Auth Tag: 175d3f6ef64838a438b484a7dee2dbbc
```

## Slide 37

Reverse Engineering Google Meet


> Recovered by OCR — confidence 84/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Reverse Engineering Google Meet
Internet Protocol Version 4, Src: 192.168.1.43, Dst: 74.125.250.251
User Datagram Protocol, Src Port: 63070, Dst Port: 3478
Real-Time Transport Protocol
[Stream setup by DTLS-SRTP (frame 2963) ]
10.. «.+. = Version: RFC 1889 Version (2)
..@. .«... = Padding: False
»»l «ss. = Extension: True
..»+ 0000 = Contributing source identifiers count: 0
```

## Slide 38

Case Study in Egress Resilience


> Recovered by OCR — confidence 95/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Case Study in Egress Resilience
BurpSuite
End User Device
```

## Slide 39

Example Zoom Desktop Egress Attempts

## Slide 40

# Example Zoom Desktop Egress Attempts

Custom Protocol over TLS on 443/TCP

## Slide 41

# Example Zoom Desktop Egress Attempts

Custom Protocol over TLS on 443/TCP


> Recovered by OCR — confidence 92/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Example Zoom Desktop Egress Attempts
Custom Protoc
LS on 443/TCP
zoom
Zone Controller
Primary
~ ae
MultiMedia Router
```

## Slide 42

# Example Zoom Desktop Egress Attempts

WebSockets over HTTPS on 443/TCP

## Slide 43

# Example Zoom Desktop Egress Attempts

WebSockets over HTTPS on 443/TCP


> Recovered by OCR — confidence 88/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Example Zoom Desktop Egress Attempts
WebSockets over ff on 443/TCP
Zone Controller
Primary
~ ae
MultiMedia Router
```

## Slide 44

# Example Zoom Desktop Egress Attempts

Custom Protocol over 443/TCP Custom Protocol over 8801/UDP

## Slide 45

# Example Zoom Desktop Egress Attempts

Custom Protocol over 443/TCP Custom Protocol over 8801/UDP

## Slide 46

# Example Zoom Desktop Egress Attempts

WebSockets over HTTPS on 443/TCP

## Slide 47

# Example Zoom Desktop Egress Attempts

WebSockets over HTTPS on 443/TCP


> Recovered by OCR — confidence 83/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Example Zoom Desktop Egress Attempts
Zone Controller
Primary
WebSockets over ” a on 443/TCP {zoom J
MultiMedia Router
```

## Slide 48

# Example Zoom Web Client Egress Attempts

WebSockets over HTTPS on 443/TCP


> Recovered by OCR — confidence 92/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Example Zoom Web Client Egress Attempts
RWG Zone Controller
Primary
WebSockets over HTTPS on 443/TCP
~ ae
MultiMedia Router
```

## Slide 49

# Example Zoom Web Client Egress Attempts

WebSockets over HTTPS on 443/TCP


> Recovered by OCR — confidence 90/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Example Zoom Web Client Egress Attempts
f WebSockets over H rt 443/TCP
RWG Zone Controller
Primary
MultiMedia Router
```

## Slide 50

# Example Zoom Web Client Egress Attempts

WebRTC over 8801/UDP


> Recovered by OCR — confidence 90/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Example Zoom Web Client Egress Attempts
RWG Zone Controller
Primary
WebRTC over 8801/UDP 200m |
MultiMedia Router
```

## Slide 51

# Example Zoom Web Client Egress Attempts

WebRTC over 8801/UDP


> Recovered by OCR — confidence 96/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Example Zoom Web Client Egress Attempts
RWG Zone Controller
Primary
01/UDP
MultiMedia Router
```

## Slide 52

# Example Zoom Web Client Egress Attempts

TURN over TLS on 443/TCP


> Recovered by OCR — confidence 88/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Example Zoom Web Client Egress Attempts
RWG Zone Controller
Primary
TURN over TLS on 443/TCP C ) cS
TURN Server MultiMedia Router
```

## Slide 53

# Example Zoom Web Client Egress Attempts

TURN over TLS on 443/TCP


> Recovered by OCR — confidence 96/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Example Zoom Web Client Egress Attempts
RWG Zone Controller
Primary
TURN Server MultiMedia Router
```

## Slide 54

# Example Zoom Web Client Egress Attempts

WebSockets over HTTPS on 443/TCP


> Recovered by OCR — confidence 89/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Example Zoom Web Client Egress Attempts
RWG Zone Controller
Primary
{ zoom J
MultiMedia Router
C WebSockets over HTTPS on 443/TCP
```

## Slide 55

# Example Zoom Web Client Egress Attempts

WebSockets over HTTPS on 443/TCP


> Recovered by OCR — confidence 87/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Example Zoom Web Client Egress Attempts
WebSockets over on 443/TCP )
RWG Zone Controller
Primary
~ ae
MultiMedia Router
```

## Slide 56

Highly Adaptable to Changing Environments

## Slide 57

Developing the Capability

## Slide 58

# Analyzing Vendor Market Share

<u>https://www.demandsage.com/microsoft-teams-statistics/</u>


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Analyzing Vendor Market Share
Videoconferencing Software Market Share
Zoom 55.91%
Microsoft Teams 32.29%
GoToMeeting 8.81%
Google Meet 5.52%
WebEx 761%
RingCentral 5.31%
FaceTime 2.16%
Skype 1.41%
Facebook Messenger 0.75%
Bluejeans 0.31%
Source:
https://www.demandsage.com/microsoft-teams-statistics/
```

## Slide 59

# Analyzing Vendor Market Share

<u>https://www.demandsage.com/microsoft-teams-statistics/</u>


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Analyzing Vendor Market Share
Videoconferencing Software Market Share
Zoom 55.91%
Microsoft Teams 32.29%
GoToMeeting 8.81%
Google Meet 5.52%
```

## Slide 60

Reverse Engineering Zoom


> Recovered by OCR — confidence 80/100 on the text kept, 53/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Reverse Engineering Zoom
{
u body" : {
"conID":"81423846-9F1F-D9EF-72D7-1265B18A9BBA",
“e2eEncrypt": true,
"encType":2,
“hugeBO": true,
"iceServers": [
{
"urls":"turns:turnsg02.cloud.zoom.us:443?transport=tcp",
{
+
]
},
“participantID":238757,
“participantIDStr":"238757",
```

## Slide 61

Reverse Engineering Zoom


> Recovered by OCR — confidence 90/100 on the text kept, 58/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Reverse Engineering Zoom
"mediasdkConfig":{
"iceServers": [
{
},
{
}
]
},
```

## Slide 62

# Zooming in on TURN

<u>source</u>


> Recovered by OCR — confidence 86/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Zooming in on TURN
Firewall rules for Zoom Meetings and Webinars
Protocol + Source + Destination
115.114.56.192/26
115.114.131.0/26
134.224.0.0/16
137.66.128.0/17
144.195.0.0/16
60.1.56.128/2
Add ress: 134 . 224 147. 12 161199.136.0/29
159.124.0.0/16
162.12.232.0/22
162.255.36.0/22
source 165.254.88.0/23
```

## Slide 63

Reverse Engineering Microsoft Teams


> Recovered by OCR — confidence 88/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Reverse Engineering Microsoft Teams
Response
Pretty Raw Hex Render =-y \n
HTTP/2 200 OK
Cache-Control: no-cache, no-store
Content-Length: 186
Content-Type: application/json; charset=utf-8
Strict-Transport-Security: max—age=31536000; includeSubDomains
Api-Supported-Versions: 1.0, 2.0
Server-Timing: reqlatency;dur=2
X-Cache: CONFIG_NOCACHE
X-Msedge-Ref: Ref A: C58D8123B9144A1CA7727C9B8DCD5BC8 Ref B: BKK3Q@EDGE@511 Ref C: 2025-03-18T14:10:21Z
Date: Tue, 18 Mar 2025 14:10:21 GMT
{
"tokens": [
{
}
```

## Slide 64

Reverse Engineering Microsoft Teams


> Recovered by OCR — confidence 91/100 on the text kept, 66/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Reverse Engineering Microsoft Teams
{
"tokens": [
{
}
"expires":604800
}
```

## Slide 65

# Observations Regarding TURN Credentials

- Usually valid for a couple of days

- Complements an existing longterm channel

- Not tied to specific calls and credentials persist post-session

- • Applies to common platforms like Zoom and Teams

- • No install or meeting required on the victim side

## Slide 66

Ghost Calls: Abusing Web Conferencing for Covert
Command & Control
Ghost Calls: Abusing Web Conferencing for Covert
Command & Control
Adam Crosser

#BHUSA @BlackHatEvents

## Slide 67

# What do we want to build?

- A short-lived tunnel launched from an existing implant

- • Used briefly and mimics activity like a video-call

- • Runs in parallel with long-term infrastructure

- Lightweight enough to avoid clogging that primary channel

- • Disguised among high-traffic destinations (e.g., Zoom, Teams)

## Slide 68

# TURNt (TURN tunneler): A Tool for Short-Term C2

<u>https://github.com/praetorian-inc/turnt</u>

## Slide 69

# Use-Cases and Capabilities

- Fast tunnel setup during assumed breach scenarios

- • No need to provision infrastructure in advance

- • Operates from operator laptop or disposable VDI

- • Ideal for decentralized red team operations

- Lightweight, flexible, and serverless by design

## Slide 70

Remote Port Forwarding


> Recovered by OCR — confidence 91/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
NTLMRelayX
Remote Port Forwarding
TURN
Server
443/TCP over TLS
Attacker System
L 445/TCP
<
Victim System
```

## Slide 71

Local Port Forwarding


> Recovered by OCR — confidence 95/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Local Port Forwarding
TU R N worldaz-msit.relay.teams.microsoft.com:443
Server
Victim Laptop Internal Citrix Infra
443/TCP over TLS
Attacker Laptop
```

## Slide 72

Use-Cases and Capabilities


> Recovered by OCR — confidence 91/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Use-Cases and Capabilities
SOCKS Local & Remote
Proxying Decentralized Port-Forwarding
1
```

## Slide 73

# Zoom Demo Example Scenario

- Obtaining credentials from Zoom

- • Victim doesn’t need to do anything

- Laptop is the operator laptop

- Example victim system is GCP virtual machine

- Demo downloading a file through the channel

## Slide 74

Zoom Video Demo <u>demo video</u>

## Slide 75

Examining Wireshark Traffic (Zoom)


> Recovered by OCR — confidence 91/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Examining Wireshark Traffic (Zoom)
>» Internet Protocol Version 4, Src: 192.168.1.43, Dst: 170.114.166.217
>» Transmission Control Protocol, Src Port: 61862, Dst Port: 443, Seq: 1, Ack: 1, Len: 273
Content Type: Handshake (22)
Version: TLS 1.@ (0x@301)
Length: 268
<
Handshake Type: Client Hello (1)
Length: 264
Random: cfda9068dcfcc75da6d6220358f91edb332335072707b911d42c681f029daalf
Session ID Length: 32
Session ID: fa209d4bc07da86474eca647841334608eab1b481800e7e41def f9d2e02d184F
Cipher Suites Length: 38
>» Cipher Suites (19 suites)
Compression Methods Length: 1
>» Compression Methods (1 method)
Extensions Length: 153
>» Extension: server_name (len=26) name=turnsin0@1.sin.zoom.us
```

## Slide 76

Examining Wireshark Traffic (Zoom)


> Recovered by OCR — confidence 91/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Examining Wireshark Traffic (Zoom)
Handshake Protocol: Client Hello
Handshake Type: Client Hello (1)
Length: 264
Session ID Length: 32
Session ID: fa209d4bc07da86474eca647841334608eab1b481800e7e41def F9d2e02d184 Ff
Cipher Suites Length: 38
>» Cipher Suites (19 suites)
Compression Methods Length: 1
>» Compression Methods (1 method)
Extensions Length: 153
>» Extension: server_name (len=26) name=turnsinQ1.sin.zoom.us
```

## Slide 77

# Zoom Recent Mitigations

- Pushed out a mitigation on Sunday

- Prevents peer-to-peer connections via TURN infra

- Restricted to client and media server ranges

- Haven’t dug into potential bypasses

- Feasibility depends on the provider

## Slide 78

# Microsoft Teams Demo

- Show automated retrieval of TURN credentials from Microsoft

- • Demonstrate a speed test showing a 100 MB file download

- Demonstrate remote portforwarding capability

- • Lab uses my local laptop and a demo virtual machine in GCP

## Slide 79

Microsoft Teams Demo


> Recovered by OCR — confidence 88/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Microsoft feams Demo
TURN
Server
443/TCP over TLS
= a Google Cloud
Python Server Attacker System Example Victim
```

## Slide 80

Microsoft Teams Video Demo <u>demo video</u>

## Slide 81

Examining Wireshark Traffic (Microsoft Teams)


> Recovered by OCR — confidence 91/100 on the text kept, 90/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Examining Wireshark Traffic (Microsoft Teams)
> Internet Protocol Version 4, Src: 192.168.1.43, Dst: 52.114.55.197
>» Transmission Control Protocol, Src Port: 60570, Dst Port: 443, Seq: 1429, Ack: 1, Len: 357
>» [2 Reassembled TCP Segments (1785 bytes): #30829(1428), #30830(357)]
v
Content Type: Handshake (22)
Version: TLS 1.0 (@x0301)
Length: 1780
<
Handshake Type: Client Hello (1)
Length: 1776
Random: 21058fee53f9753786f537e6158e9f9123d3ce824bf f6da2al4f47c80a2e9b00
Session ID Length: 32
Session ID: 3b39951f fe287758fdf1c8ca54b945 f99 f c5ae94a7891877b7652a9e148230b5
Cipher Suites Length: 32
Cipher Suites (16 suites)
Compression Methods Length: 1
Compression Methods (1 method)
Extensions Length: 1671
Extension:
Extension:
Extension:
Extension:
Extension:
Extension:
Reserved (GREASE) (len=@)
status_request (len=5)
signature_algorithms (len=18)
key_share (len=1263) X25519MLKEM768, x25519
encrypted_client_hello (len=250)
server_name (len=43) name=worldaz-msit.relay.teams.microsoft.com
```

## Slide 82

Examining Wireshark Traffic (Microsoft Teams)


> Recovered by OCR — confidence 92/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Examining Wireshark Traffic (Microsoft Teams)
>» Internet Protocol Version 4, Src: 192.168.1.43, Dst: 52.114.55.197
>» Transmission Control Protocol, Src Port: 60570, Dst Port: 443, Seq: 1429, Ack: 1, Len: 357
>» [2 Reassembled TCP Segments (1785 bytes): #30829(1428), #30830(357)]
Content Type: Handshake (22)
Version: TLS 1.0 (0x@301)
Length: 1780
```

## Slide 83

Examining Wireshark Traffic (Microsoft Teams)


> Recovered by OCR — confidence 89/100 on the text kept, 79/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Examining Wireshark Traffic (Microsoft Teams)
‘Handshake Protocol: Client Hello
Handshake Type: Client Hello (1)
Length: 1776
>» Random: 21058fee53f9753786f537e6158e9f9123d3ce824bf f6da2a14f47c80a2e9b00
Session ID Length: 32
Session ID: 3b39951f fe287758fdf1c8ca54b945 f99fc5ae94a7891877b7652a9e148230b5
Cipher Suites Length: 32
>» Cipher Suites (16 suites)
Compression Methods Length: 1
>» Compression Methods (1 method)
Extensions Length: 1671
Extension: Reserved (GREASE) (len=@)
Extension: status_request (len=5)
Extension: signature_algorithms (len=18)
Extension: key_share (len=1263) X25519MLKEM768, x25519
Extension: encrypted_client_hello (len=250)
Extension: server_name (len=43) name=worldaz-msit.relay.teams.microsoft.com
Vv
```

## Slide 84

Ghost Calls: Abusing Web Conferencing for Covert Command & Control Ghost Calls: Abusing Web Conferencing for Covert Command & Control Adam Crosser

#BHUSA @BlackHatEvents

## Slide 85

Ghost Calls: Abusing Web Conferencing for Covert Command & Control Ghost Calls: Abusing Web Conferencing for Covert Command & Control

Adam Crosser

#BHUSA @BlackHatEvents

## Slide 86

# Compromising the Helpdesk

- Helpdesk accounts are often privileged easy targets

- • Common red team foothold especially in large orgs

- • Frequently outsourced overseas locations

- Ran into slow unreliable tunnel from compromised users

- Example: Slow tunneling through helpdesk employee in India

## Slide 87

# Last Mile Delivery is the Traditional Bottleneck

<u>source</u>

<u>source</u>


> Recovered by OCR — confidence 85/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Last Mile Delivery is the Traditional Bottleneck
My Computer ‘Wintop. SeaMonkey
Connection Established
My Documents
You are connected to Turbo Jank Dialup Co.
To disconnect or to view status information,
veut apreqrneld dial-up icon in the status area ra} ay 12:45 PM
Explorer
‘You can also double-click the connection icon
in the Dial-Up Networking folder. =
Recycle Bin
T Do not show this dialog box in the future.
= & Connected to Turbo Jank Dialup
TenrpuuNet Nq Connected at 24,000 bps
my Q Bytes received: 535
Eg aX Bytes sent: 597
Microsoft AOL Instant
Word 97 Messeng...
Start|| | 7 @ FR ES >| |[Ba Connected to Turbo J...
source
Telephone Poles
How DSL Works
Receiver
Phone & Internet Signal
Landline
Wired & Wir
Connec
source
```

## Slide 88

Fiber to the Home Build Out


> Recovered by OCR — confidence 91/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Fiber to the Home Build Out
Best 1Gbps broadband plans for you
X 3 Months =% 12600 +Gst
(A, Upload/Download = 4 Gbps
Unlimited Data, Unstoppable Speed
(2) Enjoy Entertainment Bundle
OTTs - ALL Channels - 200+
More Details
Get Started
%50 / Month, one-time benefit
[S
X 6 Months = % 23400 +Gst
(A) Upload/Download = 4 Gbps
Unlimited Data, Unstoppable Speed
(2) Enjoy Entertainment Bundle
OTTs - ALL Channels - 200+
Free Wi-Fi 6 router
More Details
Get Started
%50 / Month, one-time benefit
X 12 Months = % 43200 +Gst
(A) Upload/Download = 4 Gbps
Unlimited Data, Unstoppable Speed
(2) Enjoy Entertainment Bundle
OTTs - ALL Channels - 200+
Free Wi-Fi 6 + Mesh router
Get Started
More Details
```

## Slide 89

# Global Fiber Connectivity Map

<u>source</u>

## Slide 90

# Internet Routing is a Lot Messier Than Expected

<u>source</u>


> Recovered by OCR — confidence 95/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Internet Routing is a Lot Messier Than Expected
ransi
XP
Tier 3 Network Tier 3 Network
(multi-homed ISP) (single homed ISP)
_ Internet users
(business, consumers, etc)
source
```

## Slide 91

Routing Can Impact Performance Significantly (ExpressVPN)


> Recovered by OCR — confidence 95/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Routing Can Impact Performance Significantly (ExpressVPN)
@ DOWNLOAD UPLOAD
Connections
HOW LIKELY IS IT THAT YOU WOULD RECOMMEND
DCA TO A FRIEND OR COLLEAGUE?
NexGen Communications
Change Server
dca
```

## Slide 92

Routing Can Impact Performance Significantly (ExpressVPN)


> Recovered by OCR — confidence 87/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
> ~ curl -o /dev/null -s -w
awk '{printf "Average Speed:
Average Speed: 2.09 MB/s
» ~ curl -o /dev/null -s -w
awk '{printf "Average Speed:
Average Speed: 2.69 MB/s
> ~ curl -o /dev/null -s -w
awk '{printf "Average Speed:
Average Speed: 3.25 MB/s
>» ~ curl -o /dev/null -s -w
awk '{printf "Average Speed:
Average Speed: 1.99 MB/s
» ~ curl -o /dev/null -s -w
awk '{printf "Average Speed:
Average Speed: 2.31 MB/s
> ~ curl -o /dev/null -s -w
awk '{printf "Average Speed:
Average Speed: 2.41 MB/s
"%{speed_downLoad}\n" https://sin-speed.
%.2f MB/s\n", $1/1024/1024}'
"%{speed_downLoad}\n" https://sin-speed.
%.2f MB/s\n", $1/1024/1024}'
"%{speed_downLoad}\n" https://sin-speed.
%.2f MB/s\n", $1/1024/1024}'
"%{speed_downLoad}\n" https://sin-speed.
%.2f MB/s\n", $1/1024/1024}'
"%{speed_downLoad}\n" https://sin-speed.
%.2f MB/s\n", $1/1024/1024}'
"%{speed_download}\n" https://sin-speed.
%.2f MB/s\n", $1/1024/1024}'
hetzner.
hetzner.
hetzner.
Routing Can Impact Performance Significantly (ExpressVPN)
. COM/1QQMB .
com/1QQMB .
```

## Slide 93

Routing Can Impact Performance Significantly (ExpressVPN)


> Recovered by OCR — confidence 84/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Routing Can Impact Performance Significantly (ExpressVPN)
» ~ curl -o /dev/null -s -w "%{speed_download}\n" https://sin-speed. com/1@QMB .bin
awk '{printf "Average Speed: %.2f MB/s\n", $1/1024/1024}'
Average Speed: 4.11 MB/s
>» ~ curl -o /dev/null -s -w "%{speed_download}\n" https://sin-speed.hetzner.com/1@QMB .bin
awk '{printf "Average Speed: %.2f MB/s\n", $1/1024/1024}'
Average Speed: 4.52 MB/s
» ~ curl -o /dev/null -s -w "%{speed_download}\n" https://sin-speed.hetzner.com/1@QMB .bin
awk '{printf "Average Speed: %.2f MB/s\n", $1/1024/1024}'
Average Speed: 4.14 MB/s
>» ~ curl -o /dev/null -s -w "%{speed_download}\n" https://sin-speed. com/1@QMB .bin
awk '{printf "Average Speed: %.2f MB/s\n", $1/1024/1024}'
Average Speed: 4.15 MB/s
» ~ curl -o /dev/null -s -w "%{speed_download}\n" https://sin-speed. com/10QMB .bin
awk '{printf "Average Speed: %.2f MB/s\n", $1/1024/1024}'
Average Speed: 4.13 MB/s
+» ~ curl -o /dev/null -s -w "%{speed_download}\n" https://sin-speed.hetzner.com/1@QMB .bin
awk '{printf "Average Speed: %.2f MB/s\n", $1/1024/1024}'
Average Speed: 3.95 MB/s
```

## Slide 94

Routing Can Impact Performance Significantly (ExpressVPN)


> Recovered by OCR — confidence 88/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Routing Can Impact Performance Significantly (ExpressVPN)
» -~ traceroute 5.223.7.195
traceroute to 5.223.7.195 (5.223.7.195), 64 hops max, 4@ byte packets
1 192.168.8.1 (192.168.8.1) 2.847 ms 2.333 ms 1.637 ms
10.180.6.65 (10.180.6.65) 7.319 ms 9.886 ms 7.806 ms
10.180.6.163 (10.180.6.163) 20.904 ms 33.884 ms 65.594 ms
10.9.180.3 (10.9.180.3) 24.578 ms 14.115 ms 14.705 ms
10.198.9.4 (10.198.9.4) 16.509 ms 14.164 ms 15.035 ms
Ln-oix-gw.edge.dcaonline.com (10.6.9.1) 17.582 ms 20.969 ms 16.844 ms
* * 206.126.235.20 (206.126.235.20) 22.966 ms
port-channel1@.core2.slc1.he.net (72.52.92.42) 42.848 ms * *
100ge0-73.core4.lax2.he.net (184.105.222.113) 57.986 ms * *
* port-channel6.core3.tyol.he.net (184.105.213.118) 151.090 ms *
viewqwest-pte-Ltd.port-channel2.switch2.sinl.he.net (27.5@.33.94) 285.859 ms 427.768 m
305.979 ms
132.147.112.108 (132.147.112.108) 307.782 ms 216.672 ms 219.747 ms
fnet118-f60-60-access.vqbn.com.sg (103.60.6@.118) 226.629 ms 217.943 ms 216.752 ms
2
3
4
5
6
7
8
co
NF
```

## Slide 95

Routing Can Impact Performance Significantly (ExpressVPN)


> Recovered by OCR — confidence 84/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Routing Can Impact Performance Significantly (ExpressVPN)
» ~ traceroute 5.223.7.195
traceroute to 5.223.7.195 (5.223.7.195), 64 hops max, 4@ byte packets
181.215.65.124 (181.215.65.124) 27.712 ms 39.643 ms 24.695 ms
vL221.chi-csil-core-1.cdn77.com (79.127.195.25) 26.475 ms
vL221.chi-csi-core-2.cdn77.com (79.127.195.26) 25.0@@ ms 23.367 ms
ae-7.a04.chcgil1l.us.bb.gin.ntt.net (128.241.10.28) 26.636 ms 25.495 ms 24.839 ms
ae-14.r24.chcgil@9.us.bb.gin.ntt.net (129.250.4.72) 25.125 ms 26.765 ms
ae-13.r24.chcgil@9.us.bb.gin.ntt.net €129.25@.3.188) 25.447 ms
ae-6.r26.osakjpQ02.jp.bb.gin.ntt.net (129.250.3.61) 166.132 ms * 177.447 ms
* * ge-Q@.r27.osakjp02.jp.bb.gin.ntt.net (129.25@.3.45) 157.599 ms
ae-7.r24.sngpsi07.sg.bb.gin.ntt.net (129.250.2.66) 766.735 ms 300.492 ms 804.168 ms
ae-15.aQ@3.sngpsi@7.sg.bb.gin.ntt.net (129.250.6.65) 273.625 ms 593.517 ms 339.151 ms
ae-@.hetzner.sngpsi@7.sg.bb.gin.ntt.net (116.51.31.51) 993.378 ms 229.521 ms 381.745
```

## Slide 96

# Peering Can Be More Important Than Uplink Speed

- Example: Imagine trying to exfil 10GB of data from a compromise webserver

- Good peering beats raw bandwidth for tunnel speed

- • Exfil to servers with good peering with victim internet provider

- Budget hosting providers often cheap on transit

- • Some region have fast local fiber but bad global peering

- • This could be an entire talk

## Slide 97

# Performance Killers When Tunneling over TCP

TCP Meltdown

Head-Of-Line Blocking

## Slide 98

TCP Meltdown in Action


> Recovered by OCR — confidence 88/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
TCP Meltdown in Action
@ DOWNLOAD UPLOAD
Ping © 263 @) 266
® DOWNLOAD UPLOAD
Ping © 297 @® 1299
```

## Slide 99

Peer to Peer Isn’t Always the Most Efficient


> Recovered by OCR — confidence 94/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Peer to Peer Isn’t Always the Most Efficient
Budget Transit
Provider
User in U.S.A. User in India
```

## Slide 100

Peer to Peer Isn’t Always the Most Efficient


> Recovered by OCR — confidence 95/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Peer to Peer Isn’t Always the Most Efficient
Point of Presence Point of Presence
Microsoft
Private
Backbone
User in U.S.A. User in India
```

## Slide 101

Recommend: Microsoft Teams for Cross Continent Tunneling

## Slide 102

Ghost Calls: Abusing Web Conferencing for Covert
Command & Control
Ghost Calls: Abusing Web Conferencing for Covert
Command & Control
Adam Crosser

#BHUSA @BlackHatEvents

## Slide 103

# Questions?

**Blog Post**

**Tool Release LinkedIn**

Blog Post: <u>https://www.praetorian.com/blog/ghost-calls-abusing-web-conferencing-for-covert-command-and-control-part-1/</u> GitHub: https://github.com/praetorian-inc/turnt LinkedIn: <u>https://www.linkedin.com/in/adam-crosser-366263265</u> X: <u>https://x.com/UNC1739</u>
