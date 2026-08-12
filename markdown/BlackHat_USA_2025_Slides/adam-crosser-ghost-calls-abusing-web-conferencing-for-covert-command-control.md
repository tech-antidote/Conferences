---
title: "Ghost Calls Abusing Web Conferencing for Covert Command & Control"
speakers: ["Adam Crosser"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Adam Crosser_Ghost Calls Abusing Web Conferencing for Covert Command & Control.pdf"
pages: 91
sha256: "6db959a7407399b230388a83c178e41a1e826bee7fd886ca179b4d7c59516710"
text_chars: 25393
ocr_pages: 44
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T22:49:11Z"
---
# Ghost Calls Abusing Web Conferencing for Covert Command & Control

**Speakers:** Adam Crosser  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Adam Crosser_Ghost Calls Abusing Web Conferencing for Covert Command & Control.pdf` (91 pages)

## Slide 1

## Ghost Calls: Abusing Web Conferencing for Covert Command & Control

Adam Crosser

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pibex hat
FINGS
AUGUST ae 2025
MANDALAY BAY / LAS VEGAS
Ghost Calls: Abusing Web Conferencing
for Covert Command & Control
Adam Crosser
```

## Slide 2

Adam Crosser

Introduction

Praetorian

2

LinkedIn: https://www.linkedin.com/in/adam-crosser-366263265

X: <u>https://x.com/UNC1739</u>

#BHUSA @BlackHatEvents

## Slide 3

3

Types of Command-and-Control Channels

#BHUSA @BlackHatEvents

## Slide 4

4

Types of Command-and-Control Channels

#BHUSA @BlackHatEvents

## Slide 5

Types of Command-and-Control Channels

5

#BHUSA @BlackHatEvents

## Slide 6

6

Types of Command-and-Control Channels

#BHUSA @BlackHatEvents

## Slide 7

7

Types of Command-and-Control Channels

#BHUSA @BlackHatEvents

## Slide 8

8

# Brainstorming Solutions

#BHUSA @BlackHatEvents

## Slide 9

9

#### Ideal Short-Term Command and Control

#BHUSA @BlackHatEvents

## Slide 10

10

#### Ideal Short-Term Command and Control

#### LATENCY

#BHUSA @BlackHatEvents

## Slide 11

11

#### Ideal Short-Term Command and Control

#### LATENCY

##### THROUGHPUT

#BHUSA @BlackHatEvents

## Slide 12

12

#### Ideal Short-Term Command and Control

#### LATENCY

##### THROUGHPUT

##### REACH

#BHUSA @BlackHatEvents

## Slide 13

13

#### Ideal Short-Term Command and Control

#### LATENCY

##### THROUGHPUT

##### REACH

##### TRUST

#BHUSA @BlackHatEvents

## Slide 14

#### Selection Criteria

- Focused on services egressing from user devices

- Must be broadly used across enterprise roles

- Applicable to non-technical departments (e.g., HR, sales)

- Protocols favored by technical users were excluded

- Thought through common workflows and use-cases

14

#BHUSA @BlackHatEvents

## Slide 15

DNS over HTTP (DoH)

15

LATENCY THROUGHPUT REACH TRUST

#BHUSA @BlackHatEvents

## Slide 16

16

Cloud File Storage

### LATENCY THROUGHPUT REACH TRUST

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
lackhat i
blackhat . Cloud/File. Storage
$< LATENCY
JY THROUGHPUT
JY REACH
TRUST
```

## Slide 17

17

Attacker VM with Classified Domain

### LATENCY THROUGHPUT REACH TRUST

#BHUSA @BlackHatEvents

## Slide 18

18

Email and Messaging Applications

### LATENCY THROUGHPUT REACH TRUST

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
lackh i sagi icati GE 4;
black hat Email and_Messaging Applications y 8
LATENCY
& »¢ THROUGHPUT
/ REACH
Jf TRUST
```

## Slide 19

Web Conferencing

LATENCY THROUGHPUT REACH TRUST

19

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat : i
rea Web Conferencing
/ LATENCY
WY THROUGHPUT
/ REACH
Jf TRUST
```

## Slide 20

20

#### Microsoft Teams Split Tunneling Guidelines

<u>https://learn.microsoft.com/en-us/microsoftteams/prepare-network</u>

#BHUSA @BlackHatEvents

## Slide 21

21

#### Microsoft Teams TLS Inspection

<u>https://learn.microsoft.com/en-us/microsoftteams/proxy-servers-for-skype-for-business-online</u>

#BHUSA @BlackHatEvents

## Slide 22

22

#### Zoom Split Tunneling Recommendations

<u>https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0065998</u>

#BHUSA @BlackHatEvents

## Slide 23

23

#### Zoom TLS Inspection Recommendations

<u>https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0060548</u>

#BHUSA @BlackHatEvents

## Slide 24

24

#### Quick Disclaimer

- Providers aren’t being malicious

- Performance is the main design driver

- Latency must be minimized for app reliability

- These configs are often intentional not careless

- Inspection or routing can overwhelm systems

#BHUSA @BlackHatEvents

## Slide 25

25

# How does it Work?

#BHUSA @BlackHatEvents

## Slide 26

26

#### General Web Conferencing Architecture

#BHUSA @BlackHatEvents

## Slide 27

27

#### General Web Conferencing Architecture

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
a ©
Frontend
Application
Pact] a Load Balancer Main SaaS
(zl = Application
ce
End User Network
Device Firewall
Amazon
CloudFront
```

## Slide 28

28

#### General Web Conferencing Architecture

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pigeschat
BRIEFINGS
———-
End User
Device
Network
Firewall
Frontend
Amazon Ye
Application
CloudFront
Load Balancer Main SaaS
Application
443/TCP
3478/UDP 3478/U0P 3478/U0P
8801/UDP
TURN STUN Media
Servers Servers Servers
(SFU)
```

## Slide 29

29

#### What is TURN?

<u>https://www.100ms.live/blog/webrtc-turn-server</u>

#BHUSA @BlackHatEvents

## Slide 30

30

#### WebRTC Core Protocols

#BHUSA @BlackHatEvents

## Slide 31

#### WebRTC Handshake Process

31

<u>https://www.researchgate.net/figure/WebRTC-triangle-with-DTLS-key-exchange_fig8_328334940</u>

#BHUSA @BlackHatEvents

## Slide 32

32

#### Reverse Engineering Zoom

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat Reverse Engineering, Zoom
Internet Protocol Version 4, Src: 192.168.1.41, Dst: 170.114.164.95
User Datagram Protocol, Src Port: 61029, Dst Port: 8801
Zoom SFU Encapsulation
Type: 5
Sequence number: 1278
Direction: ® (to Zoom)
Zoom Media Encapsulation
Type: 16 (Video)
Sequence number: 1261
Timestamp: 106179922
Frame number: 57
Packets in frame: 2
Real-Time Transport Protocol
[Stream setup by DECODE AS (frame 28373)]
10.. .... = Version: RFC 1889 Version (2)
+:Q@. «22. = Padding: False
seek weve Extension: True
- 0000 = Contributing source identifiers count: @
1... ..+. = Marker: True
Payload type: DynamicRTP-Type-98 (98)
Sequence number: 24484
[Extended sequence number: 90020]
Timestamp: 894589134
[Extended timestamp: 5189556430]
Synchronization Source identifier: ®x®1000401 (16778241)
Defined by profile: RFC 5285 One-Byte Header Extensions (@xbede)
Extension length: 5
Header extensions
Payload [..]: 1¢40736b27a5415cf9715dd657876f8c59f 14a70c4c6878987c74f26b8123 f633690b6e f5cceele88f5932228eadc93eefe91c9f2
```

## Slide 33

#### Reverse Engineering Zoom

33

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
BRIEFINGS
black hat Reverse Engineering, Zoom /
Internet Protocol Version 4, Src: 192.168.1.41, Dst: 170.114.164.95
User Datagram Protocol, Src Port: 61029, Dst Port: 8801
Zoom SFU Encapsulation
```

## Slide 34

34

#### Reverse Engineering Zoom

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat Reverse Engineering, Zoom |
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

35

#### Building on Existing Work

Enabling Passive Measurement of Zoom Performance in Production Networks

###### Custom Wireshark Analyzer for Zoom Desktop Media Traffic

<u>https://dl.acm.org/doi/pdf/10.1145/3517745.3561414</u>

<u>https://github.com/Princeton-Cabernet/zoom-analysis</u>

#BHUSA @BlackHatEvents

## Slide 36

36

#### Reverse Engineering Google Meet

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
blackhat ninéeri EE:
ickhat Reverse Enginéering Google Meet fr
Frame 4296: 160 bytes on wire (128@ bits), 160 bytes captured (1280 bits)
Ethernet II, Src: Apple_d5:f9:5f (14:7d:da:d5:f9:5f), Dst: zte_4c:ac:24 (20:08:89:4c:ac:24)
Internet Protocol Version 4, Src: 192.168.1.43, Dst: 74.125.250.251
User Datagram Protocol, Src Port: 63070, Dst Port: 3478
Real-Time Transport Protocol
[Stream setup by DTLS-SRTP (frame 2963) ]
10.. .... = Version: RFC 1889 Version (2)
--0. .... = Padding: False
eeel «se. = Extension: True
. 000@ = Contributing source identifiers count: 0
@... «... = Marker: False
Payload type: Unassigned (63)
Sequence number: 24725
[Extended sequence number: 90261]
Timestamp: 345165098
[Extended timestamp: 4640132394]
Synchronization Source identifier: @xa11f3@c7 (2703175879)
Defined by profile: RFC 5285 One-Byte Header Extensions (@xbede)
Extension length: 3
Header extensions
RFC 5285 Header Extension (One-Byte Header)
RFC 5285 Header Extension (One-Byte Header)
RFC 5285 Header Extension (One-Byte Header)
SRTP Encrypted Payload: 56046ee649b15872c7d5a1f0b3604bf7ee71d42d8d55062dc3c6a639ae063054d04ea8469F2495cf5c3:
SRTP Auth Tag: 175d3f6ef64838a438b484a7dee2dbbc
```

## Slide 37

37

#### Reverse Engineering Google Meet

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
blackhat ~. 7.
BRIEFINGS Reverse Engineering Google Meet
Internet Protocol Version 4, Src: 192.168.1.43, Dst: 74.125.250.251
User Datagram Protocol, Src Port: 63070, Dst Port: 3478
Real-Time Transport Protocol
[Stream setup by DTLS-SRTP (frame 2963) ]
10.. .«... = Version: RFC 1889 Version (2)
.:@. «2.» = Padding: False
»2l wees = Extension: True
. 0000 = Contributing source identifiers count: @
```

## Slide 38

38

Case Study in Egress Resilience

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat =. woe
ape tt Case Study in‘Egress) Resilience
End User Device
BurpSuite
```

## Slide 39

39

Example Zoom Desktop Egress Attempts

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
piSekhat Example Zoom _Desktop Egress Attempts” 39
BRIEFINGS
©)
700m Zoom
Zone Controller
Primary
~ -
_
— —
MultiMedia Router
```

## Slide 40

40

#### Example Zoom Desktop Egress Attempts

Custom Protocol over TLS on 443/TCP

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
lackhat ask eh
blackhat Example Zoom Desktop Egress Attempts 0
Custom Protocol over TLS on 443/TCP
©
Z00M Zoom
Zone Controller
Primary
MultiMedia Router
```

## Slide 41

41

#### Example Zoom Desktop Egress Attempts

Custom Protocol over TLS on 443/TCP

#BHUSA @BlackHatEvents

## Slide 42

42

#### Example Zoom Desktop Egress Attempts

WebSockets over HTTPS on 443/TCP

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
lackhat 2Sk Gia
black hat Example Zoom _Desktop Egress Attempts
© WebSockets over HTTPS on 443/TCP (=)
Zone Controller
Primary
MultiMedia Router
```

## Slide 43

43

#### Example Zoom Desktop Egress Attempts

WebSockets over HTTPS on 443/TCP

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
WebSockets over on 443/TCP
zoom
Zone Controller
Primary
~ yy
MultiMedia Router
```

## Slide 44

44

#### Example Zoom Desktop Egress Attempts

Custom Protocol over 443/TCP Custom Protocol over 8801/UDP

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
zoom
lackhat osk PF
black hat Example Zoom_Desktop Egress Attempts
Custom Protocol over 443/TCP
Custom Protocol over 8801/UDP
>
Zone Controller
Primary
-
——
MultiMedia Router
```

## Slide 45

45

#### Example Zoom Desktop Egress Attempts

Custom Protocol over 443/TCP Custom Protocol over 8801/UDP

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
>
2)
black hat Example Zoom Desktop Egress Attempts 45
Zone Controller
Primary
Custom Pr 443/TCP
Custom Pro er 8801/UDP
zoom
MultiMedia Router
```

## Slide 46

46

Example Zoom Desktop Egress Attempts

WebSockets over HTTPS on 443/TCP

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
lackhat ask eh
black hat Example Zoom Desktop Egress Attempts 6
©
Zoom
Zone Controller
Primary
WebSockets over HTTPS on 443/TCP
zoom ——
MultiMedia Router
```

## Slide 47

47

#### Example Zoom Desktop Egress Attempts

WebSockets over HTTPS on 443/TCP

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
>
2)
black hat Example Zoom Desktop Egress Attempts 47
Zone Controller
Primary
WebSockets over S on 443/TCP
~~ es
zoom
MultiMedia Router
```

## Slide 48

48

Example Zoom Web Client Egress Attempts

WebSockets over HTTPS on 443/TCP

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
piSekhat Example Zoom_Web‘Client Egress Attempts 48
BRIEFINGS
WebSockets over HTTPS on 443/TCP
ZOOM
Zone Controller
Primary
RWG
=
MultiMedia Router
```

## Slide 49

49

#### Example Zoom Web Client Egress Attempts

WebSockets over HTTPS on 443/TCP

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekchat Example Zoom Web‘Client Egress Attempts - 4°
BRIEFINGS
\ WebSockets over H on 443/TCP
ZOOM
Zone Controller
Primary
RWG
MultiMedia Router
```

## Slide 50

50

#### Example Zoom Web Client Egress Attempts

##### WebRTC over 8801/UDP

#BHUSA @BlackHatEvents

## Slide 51

51

#### Example Zoom Web Client Egress Attempts

WebRTC over 8801/UDP

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
blackhat Example Zoom Web‘Client Egress Attempts 31
ZOOM
RWG Zone Controller
Primary
MultiMedia Router
```

## Slide 52

52

#### Example Zoom Web Client Egress Attempts

TURN over TLS on 443/TCP

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pifeschat
BRIEFINGS
RWG Zone Controller
Primary
TURN over TLS on 443/TCP |
—>
Se
TURN Server MultiMedia Router
```

## Slide 53

53

#### Example Zoom Web Client Egress Attempts

TURN over TLS on 443/TCP

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
blackhat Example Zoom Web‘Client Egress Attempts 33
Zoom
RWG Zone Controller
Primary
Se LD
TURN Server MultiMedia Router
```

## Slide 54

54

Example Zoom Web Client Egress Attempts

WebSockets over HTTPS on 443/TCP

#BHUSA @BlackHatEvents

## Slide 55

55

#### Example Zoom Web Client Egress Attempts

WebSockets over HTTPS on 443/TCP

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
blackhat Example Zoom Web‘Client Egress Attempts 35
a ) WebSockets over
f
_
Zoom
RWG Zone Controller
Primary
on 443/TCP
MultiMedia Router
```

## Slide 56

56

Highly Adaptable to Changing Environments

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
BRIEFINGS
blackhat Highly Adaptable to‘Changing Environmen
\@ AUDIO
\ ONLY
```

## Slide 57

57

# Developing the Capability

#BHUSA @BlackHatEvents

## Slide 58

58

#### Analyzing Vendor Market Share

<u>https://www.demandsage.com/microsoft-teams-statistics/</u>

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
blackhat Analyzing Vendor.Market Share
BRIEFINGS . My
Videoconferencing Software Market Share |
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
```

## Slide 59

Analyzing Vendor Market Share

59

#BHUSA @BlackHatEvents <u>https://www.demandsage.com/microsoft-teams-statistics/</u>

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat Analyzing Vendor Market Share
Videoconferencing Software Market Share
Zoom 55.91%
Microsoft Teams 32.29%
GoToMeeting 8.81%
Google Meet 5.52%
```

## Slide 60

Reverse Engineering Zoom

60

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
blackhat Reverse Engineering Zoom
{
"body": {
“ABtoken":"3C45E3C9-7F73-—2CD4—0C2A-61B0665E2AA7",
“conID":"81423846-9F1F-D9EF-72D7-1265B18A9BBA",
“confID":"@C71C7D6-C040-—4363-94C1-3175DA4475F7",
“e2eEncrypt":true,
“elapsed":@,
“encType":2,
“hugeBO": true,
“mediasdkConfig": {
“iceServers": [
{
"credential": "rlY¥nbcRe9d5IqRiU/Ukst9QYOC2 LidMWRmUQoWVvFoc=",
“urls":"turns: turnsg@2.cloud.zoom.us:443?transport=tcp",
“username”: "81423846-9F1F-D9EF-72D7-1265B18A9BBA: 1741859664289"
},
{
"credential": "y7rK3BSihbZ33NQeVtUsgynrdvJZpYRkUUuUkKI6LaUpU=",
“urls":"turns: turnsg@1. cloud. zoom.us:443?transport=tcp",
“username":"81423846-9F1F-D9EF-72D7-1265B18A9BBA: 1741859664289"
}
]
},
“meetingTopic":"Y29sYnkuZWxvdGVzdEBnbWFpbC5j b2@ncyBab29tIE11ZXRpbmc",
“mmnrFeature":3204447728,
“mnrFeatureEx":4501601879980014,
“mmrFeatureExStr":"4616187620307367918",
"mn" :"97774758416",
“participantID": 238757,
“participantIDStr":"238757",
“reportDomain":"z00msg134224146206rwg.cloud.zoom.us",
```

## Slide 61

61

#### Reverse Engineering Zoom

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat Reverse Engineering Zoom
"mediasdkConfig": {
"iceServers": [
{
"credential": "rlY¥nbcRe9d5IgRiU/Ukst9QY0C2 LidMWRmUQoWVvFoc=",
"urls":"turns:turnsg@2.cloud.zoom.us:443?transport=tcp",
“username":'"81423846-9F1F-D9EF-72D7-1265B18A9BBA: 1741859664289"
},
{
"credential": "y7rK3BSihbZ33NQeVtUsgynrdvJZpYRkUuukI6LaUpU=",
“urls":"turns: turnsg@1. cloud. zoom.us:443?transport=tcp",
"username": "81423846-9F1F-D9EF-—72D7-1265B18A9BBA: 1741859664289"
}
]
},
```

## Slide 62

62

#### Zooming in on TURN

<u>https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0060548</u>

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat Zooming invon-TURN if 62
SS
\
Firewall rules for Zoom Meetings and Webinars
Protocol + Destination
* ~ nslookup turnsg@2.cLloud.Zoom.US Bias
Server: 192.168.1.1 Henariaee
120.29.148.0/24
Address: 192.168.1.1#53 121.244.146.0/27
137.66.128.0/17
144.195.0.0/16
1 , . 147124.96.0/19
Non-authoritative answer: aCe Are
156.45.0.0/17
Name: turnsgQ@2.cLoud.zoom.us 159124.0.0/16
160.1.56.128/25
Address: |134.224.147.1@ 161.199.136.0/22
162.12.232.0/22
162.255.36.0/22
165.254.88.0/23
```

## Slide 63

63

#### Reverse Engineering Microsoft Teams

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
BRIEFINGS
black hat Reverse Engineering-Microsoft Teams A :
Response
Pretty Raw Hex ee \N =
1 HTTP/2 200 OK
2 Cache-Control: no-cache, no-store
Content-Length: 186
Content-Type: application/json; charset=utf-8
Ms-Cv: LHKZC4UNR@280SVyWraqm+g. 2
Strict-Transport-Security: max-age=31536000; includeSubDomains
Api-Supported-Versions: 1.0, 2.0
Server-Timing: reqlatency;dur=2
X-Cache: CONFIG_NOCACHE
10 X-Msedge-Ref: Ref A: C58D8123B9144A1CA7727C9B8DCD5BC8 Ref B: BKK3Q@EDGEQ@511 Ref C: 2025-03-18T14:10:21Z
11 Date: Tue, 18 Mar 2025 14:10:21 GMT
12
i3 {
"tokens": [
<
“realm":"\"rtcmedia\"",
"username": "AgAAJKTMRIAB252Px+6sqQkexkR@PUDm7 3PwpkvwWP3 I[AAAAAdg8G7t@ LFUabmHtcN LO6RCa80uUA=",
"password": "InNEj cnomvcTOpPEgPsA800mMkE="
}
J,
“expires":604800
OOoOn nu & WwW
```

## Slide 64

64

#### Reverse Engineering Microsoft Teams

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blackhat Reverse Engineering-Microsoft Teams
BRIEFINGS
{
"tokens": [
{
"realm":"\"rtcmedia\"",
"username": "AgAAJKTmRIAB252Px+6sqQkexkR@PUDm7 3PwpkvWP3 IAAAAAdg8G7t@ LFUabmHtcN LO6RCa80uUA=",
"password": “InNEj cnomvcTOpPEgPsA800mMkE="
}
J,
"expires": 604800
```

## Slide 65

65

#### Observations Regarding TURN Credentials

- Usually valid for a couple of days

- Complements an existing long-term channel

- Not tied to specific calls and credentials persist post-session

- Applies to common platforms like Zoom and Teams

- No install or meeting required on the victim side

#BHUSA @BlackHatEvents

## Slide 66

66

# Building the Tool

#BHUSA @BlackHatEvents

## Slide 67

67

#### What do we want to build?

- A short-lived tunnel launched from an existing implant

- Used briefly and mimics activity like a video call

- Runs in parallel with long-term infrastructure

- Lightweight enough to avoid clogging that primary channel

- Disguised among high-traffic destinations (e.g., Zoom, Teams)

#BHUSA @BlackHatEvents

## Slide 68

68

TURNt (TURN tunneler)

<u>https://github.com/praetorian-inc/turnt</u>

#BHUSA @BlackHatEvents

## Slide 69

#### Use-Cases and Capabilities

69

- Fast tunnel setup during assumed breach scenarios

- No need to provision infrastructure in advance

- Operates from operator laptop or disposable VDI

- Ideal for decentralized red team operations

- Lightweight, flexible, and serverless by design

#BHUSA @BlackHatEvents

## Slide 70

70

Remote Port Forwarding

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
blackhat Remote Port Forwarding
BRIEFINGS
BC &
TU RN \ msit.relay.teams.microsoft.com:443
Server
S55
Bins,
=
Tt ™
443/TCP over TLS
BIB) soe Ce eee E
_ betes
NTLMRelayX Ea
Victim System
Attacker System
```

## Slide 71

Local Port Forwarding

71

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
blackhat Local_Port Forwarding
BRIEFINGS
CO
TU R N worldaz-msit.relay.teams.microsoft.com:443
Server
a
Ea
P} UN
443/TCP over TLS
1494/TCP a [] 1494/TCP
. ae
as, _—
zap
Victim Laptop Internal Citrix Infra
Attacker Laptop
```

## Slide 72

Use-Cases and Capabilities

72

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pis hat
BRIEFINGS
SOCKS : me ;
Proxying ecentralize Local & Remote
C2 Port-Forwarding
```

## Slide 73

73

#### Zoom Demo Example Scenario

- Obtaining credentials from Zoom

- Victim doesn’t need to do anything

- Laptop is the operator laptop

- Example victim system is GCP virtual machine

- Demo downloading file through the channel

#BHUSA @BlackHatEvents

## Slide 74

Zoom Video Demo

74

<u>demo video</u>

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
blackhat Zoom Video-Demo
BRIEFINGS
@ Launch Meeting - Zoom x +
(4) usOGweb.zoom.us/s/B5961252476esuccess
zoom
Click Open Zoom Workplace app on the dialog shown by your browser
If you don't see a dialog, click Launch Meeting below
By joining a meeting, you agree to our Terms of Service and Privacy Statement
Don't have the Zoom Workptace app installed? Dowr
```

## Slide 75

75

#### Examining Wireshark Traffic (Zoom)

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
blackhat Examining Wiréshark Traffic oom), gE
Internet Protocol Version 4, Sre: 192.168.1.43, Dst: 170.114. 166. 217
Transmission Control Protocol, Src Port: 61862, Dst Port: 443, Seq: 1, Ack: 1, Len: 273
Transport Layer Security
TLSv1.3 Record Layer: Handshake Protocol: Client Hello
Content Type: Handshake (22)
Version: TLS 1.@ (0x0301)
Length: 268
Handshake Protocol: Client Hello
Handshake Type: Client Hello (1)
Length: 264
Version: TLS 1.2 (0x@303)
Random: cfda9068dcfcc75da6d6220358f91edb332335072707b911d42c681f029daalf
Session ID Length: 32
Session ID: fa209d4bc07da86474eCca647841334608eab1b481800e7e4 1def f9d2e02d184Ff
Cipher Suites Length: 38
Cipher Suites (19 suites)
Compression Methods Length: 1
Compression Methods (1 method)
Extensions Length: 153
Extension: server_name (len=26) name=turnsinQ1.sin.zoom.us
```

## Slide 76

76

#### Examining Wireshark Traffic

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat ee | f
ees Examining Wireshark Traffic
Handshake Protocol: Client Hello
Handshake Type: Client Hello (1)
Length: 264
Version: TLS 1.2 (@x@303)
Random: cfda9068dcfcc75da6d6220358f91edb332335072707b911d42c681f 029daalf
Session ID Length: 32
Session ID: fa209d4bc07da86474eca647841334608eab1b481800e7e41def F9d2e02d184Ff
Cipher Suites Length: 38
Cipher Suites (19 suites)
Compression Methods Length: 1
Compression Methods (1 method)
Extensions Length: 153
Extension: server_name (len=26) name=turnsinQ1.sin.zoom.us
```

## Slide 77

77

#### Microsoft Teams Demo

- Show automated retrieval of TURN credentials from Microsoft

- Demonstrate a speed test showing a 100 MB file download

- Demonstrate remote port-forwarding capability

- Lab uses my local laptop and a demo virtual machine in GCP

#BHUSA @BlackHatEvents

## Slide 78

78

Microsoft Teams Demo

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat . —roe”
Ce Microsoft-leams Demo
CO
(— TURN
443/TCP over TLS server
a= [A] 2): =
= —S—_ Google Cloud
Python Server Attacker System Example Victim
```

## Slide 79

79

#### Microsoft Teams Video Demo

<u>demo video</u>

#BHUSA @BlackHatEvents

## Slide 80

80

#### Examining Wireshark Traffic

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bi§ekchat Examining,;Wireshark Traffic
BRIEFINGS ,
Internet Protocol Version 4, Src: 192.168.1.43, Dst: 52.114.55.197
Transmission Control Protocol, Src Port: 60570, Dst Port: 443, Seq: 1429, Ack: 1, Len: 357
[2 Reassembled TCP Segments (1785 bytes): #30829(1428), #30830(357)]
Transport Layer Security
TLSv1.2 Record Layer: Handshake Protocol: Client Hello
Content Type: Handshake (22)
Version: TLS 1.@ (@x@301)
Length: 1780
Handshake Protocol: Client Hello
Handshake Type: Client Hello (1)
Length: 1776
Version: TLS 1.2 (0x0303)
Random: 21058fee53f9753786f537e6158e9f9123d3ce824bf f6da2al14f47c80a2e9b00
Session ID Length: 32
Session ID: 3b39951ffe287758 fdf1c8ca54b945 f99f c5ae94a7891877b7652a9e148230b5
Cipher Suites Length: 32
Cipher Suites (16 suites)
Compression Methods Length: 1
Compression Methods (1 method)
Extensions Length: 1671
Extension: Reserved (GREASE) (len=0)
Extension: status_request (len=5)
Extension: signature_algorithms (len=18)
Extension: key_share (len=1263) X25519MLKEM768, x25519
Extension: encrypted_client_hello (len=250)
Extension: server_name (len=43) name=worldaz-msit.relay.teams.microsoft.com
```

## Slide 81

81

#### Examining Wireshark Traffic

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pifekhat Examining Wireshark Traffic
BRIEFINGS
Internet Protocol Version 4, Src: 192.168.1.43, Dst: 52.114.55.197
Transmission Control Protocol, Src Port: 60570, Dst Port: 443, Seq: 1429, Ack: 1, Len: 357
[2 Reassembled TCP Segments (1785 bytes): #30829(1428), #30830(357)]
Transport Layer Security
TLSv1.2 Record Layer: Handshake Protocol: Client Hello
Content Type: Handshake (22)
Version: TLS 1.@ (0@x0301)
Length: 1780
Handshake Protocol: Client Hello
```

## Slide 82

82

#### Examining Wireshark Traffic

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bi§ekchat Examining,;Wireshark Traffic
BRIEFINGS
Handshake Protocol: Client Hello
Handshake Type: Client Hello (1)
Length: 1776
Version: TLS 1.2 (0x0303)
Random: 21058fee53f9753786f537e6158e9F9123d3ce824bf f6da2al4f47c80a2e9b00
Session ID Length: 32
Session ID: 3b39951f fe287758fdf1c8ca54b945 f99fc5ae94a7891877b7652a9e148230b5
Cipher Suites Length: 32
Cipher Suites (16 suites)
Compression Methods Length: 1
Compression Methods (1 method)
Extensions Length: 1671
Extension: Reserved (GREASE) (len=0)
Extension: status_request (len=5)
Extension: signature_algorithms (len=18)
Extension: key_share (len=1263) X25519MLKEM768, x25519
Extension: encrypted_client_hello (len=250)
Extension: server_name (len=43) name=worldaz-msit.relay.teams.microsoft.com
```

## Slide 83

83

# Conclusion

#BHUSA @BlackHatEvents

## Slide 84

84

#### Defensive Considerations

- Detection is hard

- Focus on other points in the kill chain

- Look for attacker tools proxied through the tunnel

- Low signal at network layer

- TURN creds can’t be removed

#BHUSA @BlackHatEvents

## Slide 85

#### Things to Avoid

- Chasing weak signals like raw traffic volume

- Correlating process-to-destination traffic is noisy

- High effort, low return on detection accuracy

- Hard to distinguish legit conferencing from abuse

85

#BHUSA @BlackHatEvents

## Slide 86

#### Canary Tokens

86

- “Read Teaming” targets credentials and shares

- Common targets: Slack, SharePoint, GitHub, Jira, etc.

- Targeting credentials and other sensitive data

- Canary tokens reveal enumeration early

- Simple, low-cost, and highly effective control

#BHUSA @BlackHatEvents

## Slide 87

87

Detecting Proxied Attacker Tooling

- Attackers proxy tools rather than run them locally

- Focus on offensive tool behavior not the channel

- Detect usage of tools like secretsdump.py or Impacket

#BHUSA @BlackHatEvents

## Slide 88

88

#### Future Work

- Other providers beyond Zoom/Teams also use TURN

- Opportunity for further mapping and validation

- Ideal entry-point project for new researchers

- Doesn’t require major tooling changes

- Expands applicability of the core method

#BHUSA @BlackHatEvents

## Slide 89

#### Future Work

89

- Current Go binaries weigh in around 2-3 MB

- Porting to C/C++ could reduce size under 1MB

- Smaller payloads improve operational stealth

- Better fit for constrained or ephemeral systems

- Helps with evasion and minimal footprint delivery

#BHUSA @BlackHatEvents

## Slide 90

#### Future Work

90

- Explore default settings in security appliances

- Identify vendor-based exclusions or allow-listing

- Check if IP ranges are autoapproved by default

- Investigate TLS inspection exemptions for key domains

- Assess how much trust these defaults embed

#BHUSA @BlackHatEvents

## Slide 91

#### Takeaways and Questions

91

- Web conferencing solutions provide a compelling vector for covert short-term command and control channels

- TURNt is a new open-source tool that helps facilitate short-term C2 communication over the TURN protocol

- TURN provides a provider agnostic manner for tunneling traffic through potentially trusted web conferencing infrastructure **Blog Post Tool Release LinkedIn**

#BHUSA @BlackHatEvents
