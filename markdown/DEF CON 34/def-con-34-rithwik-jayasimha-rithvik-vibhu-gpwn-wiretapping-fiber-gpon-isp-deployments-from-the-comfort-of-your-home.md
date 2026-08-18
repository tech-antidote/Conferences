---
title: "gpwn Wiretapping fiber (GPON) ISP deployments from the comfort of your home"
speakers: ["Rithwik Jayasimha", "Rithvik Vibhu"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: 2026
source_pdf: "DEF CON 34/DEF CON 34 - Rithwik Jayasimha, Rithvik Vibhu - gpwn Wiretapping fiber (GPON) ISP deployments from the comfort of your home.pdf"
pages: 96
sha256: "b6604a7072c05159330dc3954a6766e12620d8fe03c7705f4231e046e9f6572e"
text_chars: 20514
ocr_pages: 34
has_ocr: true
redacted_secrets: 0
ocr_confidence: 89.8
ocr_unreliable_blocks: 4
vision_verified_pages_changed: 72
vision_verified_pages: 96
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:45:31Z"
---
# gpwn Wiretapping fiber (GPON) ISP deployments from the comfort of your home

**Speakers:** Rithwik Jayasimha, Rithvik Vibhu  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Rithwik Jayasimha, Rithvik Vibhu - gpwn Wiretapping fiber (GPON) ISP deployments from the comfort of your home.pdf` (96 pages)


## Slide 1

gpwn: Wiretapping Fiber (GPON) ISP Deployments From the Comfort of Your Home

RithVik Vibhu
RithWik Jayasimha

07 July 2026

## Slide 2

## Slide 3

todo: replace image

x3

<The multiple things that you wanted to go after and hack on and just say you're taking photographs because you were interested in understanding more >

## Slide 4

todo: replace image

## Slide 5

Photograph of the Nokia ONT under test, rear label readable:

NOKIA
Model: G-2425G-A
Input: 12V DC 1.5A
Assembled in Vietnam
DANGER- Invisible Laser radiation when open. AVOID DIRECT EXPOSURE TO BEAM.
ONT PN: 3FE48299DEAC
MAC: 60BD2C9D76F0
SN: ALCLB42EF6EA
Model : G-2425G-A
MFG:   YEAR: 2026   MONTH:01
ICS:01   MRev: 05
CLASS 1 LASER PRODUCT

Rear port legends: TEL1, TEL2, LAN1, LAN2, LAN3, LAN4, POWER, WPS, LED, RESET, ON/OFF

*Transcription note: the label MAC is corroborated by the packet capture on slide 33 (`60:bd:2c:9d:76:f0`, TaicangT&W OUI). Two glyphs on this label are soft in the source photograph even at native image resolution and could not be resolved with certainty: the 11th character of the serial (`ALCLB42EF6EA` — the `6` may be a `5`) and the final digit of the manufacture year (`2026` — may be `2025` or `2028`). Neither value appears anywhere else in the deck to check against.*

## Slide 6

## Slide 7

Chat log (all messages from Rithwik Jayasimha, 2/24/2026):

- Guys (12:48:10 AM)
- You arent going to believr what im discovering (12:48:24 AM)
- Optical fiber networks are TOTALLY different (12:48:39 AM)
- Than what we are used to (12:48:45 AM)
- Holy shit hahaha (12:53:18 AM)
- I havent felt this excited in a while (12:53:24 AM)
- Its obvious in himdsight (12:53:39 AM)
- If you compromised the keys for every router, you could in theory wiretap every single user along your fiber line (1:03:30 AM)
- I suspect this is not as infeasible as we think (1:03:45 AM)
- My spidey instincts are tingling (1:03:59 AM)

## Slide 8

## Slide 9

todo: replace image

Diagram: Street / Neighborhood Ethernet Internet Setup

1. ISP Network — Internet connects to the ISP Network (router).

2. Neighborhood ISP Equipment — Neighborhood Cabinet (Outdoor / Street Cabinet). Fiber from ISP feeds an Aggregation Switch / Ethernet Access Switch / Media Converter (ports 1-5). Independent forwarding to each house: the switch forwards packets to the correct house/link (A, B, C, D, E). Ethernet to Houses.

3. Street Distribution — Individual Cat5e/Cat6 drop to each house (House A through House E). May run underground or on poles. Copper Ethernet runs are typically short (about 100 m max).

4. Inside One House — Ethernet Wall Jack or Cable Entry Point (from outside) -> Your Router (Wi-Fi / NAT / Firewall) -> Your Devices.

## Slide 10

todo: replace image

Diagram: FTTH / GPON Internet Setup

1. ISP Network — Internet connects to the OLT (Optical Line Terminal), located at ISP / Central Office.

2. Fiber Distribution — Street Cabinet / Neighborhood Fiber Enclosure containing a Passive Optical Splitter (1:8 / 1:16 / 1:32 etc.). Fed by the Feeder Fiber. Passive device with no active switching. It simply splits the optical signal to multiple homes.

3. Street / Neighborhood Distribution — One feeder fiber is shared and split into individual fiber drops (House A through House E). Feeder fiber (shared); Individual fiber drops (one per home).

4. Inside One House — Fiber wall outlet / entry point -> ONT / ONU (Optical Network Terminal, with PON / LOS / LAN / POWER LEDs) -> Your Router (Wi-Fi / NAT / Firewall) -> Your Devices.

## Slide 11

Overview

- Basics of fiber optics
- Wiretapping your neighbors
- Physical attacks on fiber
- Bypassing countermeasures
- Tools to hack FTTH from home

## Slide 12

## Slide 13

## Slide 14

## Slide 15

## Slide 16

Optical Line Terminal (OLT)  +  Optical Distribution Network (ODN)  +  Optical Network Unit (ONU)

ODN comprises:
- All the feeder fiber
- Optical splitters
- Patch cords

Passive Optical Network (PON) tree

## Slide 17

Diagram: a 1:4 PON tree. OLT connects through a 1:4 splitter out to ONU 1, ONU 2, ONU 3 and ONU 4.

upstream frame (BWmap allocations) — guard gap after last slot

## Slide 18

Sharing the fiber

How do you make hundreds of individuals share the optical medium?

- Time (TDMA)
- λ (FDMA)

## Slide 19

Gigabit Passive Optical Networks (GPON)

Diagram of a GPON tree (OLT -> splitter -> ONUs) showing the two wavelengths:
- Downstream (OLT -> ONUs): 1490nm
- Upstream (ONUs -> OLT): 1310nm

## Slide 20

Diagram: Optical Line Terminal -> Splitter -> Optical Network Unit, connected by fiber patch cords.

## Slide 21

Diagram: Optical Line Terminal -> Splitter -> Optical Network Unit.

ISPs assume they control this

## Slide 22

Diagram: Optical Line Terminal -> Splitter -> Optical Network Unit. A box drawn around the OLT and Splitter is labelled:

What they physically control

ISPs assume they control this

## Slide 23

Diagram: Optical Line Terminal -> Splitter -> Optical Network Unit. The OLT and Splitter are boxed as "What they physically control"; the Optical Network Unit is boxed separately as "In our home 🤑".

ISPs assume they control this

## Slide 24

Photos of a GPON SFP stick and its Realtek SoC, marked:

```text
RTL9601D
M4DR1E2 GM18A3
```

GitHub repository screenshot — https://github.com/Anime4000/RTL960x

Anime4000 / RTL960x (Public)

Tabs: Code · Issues 197 · Pull requests · Discussions · Actions · Projects · Security and quality · Insights

Watch 35 · Fork 149 · Star 1k

main · 1 Branch · 0 Tags

README · Unlicense license — banner: OPEN PON FOUNDATION — OPENING THE FUTURE OF NETWORK CONNECTIVITY

About: Hacking & Reverse Engineering RTL960x-based xPON ONTs to suit your OLT

Topics: firmware, hacking, busybox, onu, olt, gpon, lantiq, realtek, gpon-stick

Releases: No releases published · Packages: No packages published

## Slide 25

## Slide 26

## Slide 27

OLT–ONU activation sequence diagram (GPON ONU state machine, O1–O5).

Messages (top to bottom), between OLT and ONU:
- Downstream synchronization (OLT → ONU) — state O1
- Burst Profile (OLT → ONU)
- SN Request (BWMap) (OLT → ONU)
- Serial_Number_Onu (ONU → OLT) — states O2–O3
- SN Verified (processing at OLT)
- Assign ONU-ID (OLT → ONU)
- Ranging Request (BWMap) (OLT → ONU) — state O4
- Registration_ID (ONU → OLT)
- Ranging_Time (OLT → ONU)
- Acknowledgement Message (ONU → OLT)
- state O5
- Create OMCC and send out business configurations

Callouts (right side):
- Serial #
- Matching vendor ID
- Potentially: LOID auth

## Slide 28

Wireshark capture of a PPPoE session bring-up on VLAN 2224, alongside a Google homepage.

| No. | Time | Source | Destination | Protocol | Length | vlan_id | Info |
|---|---|---|---|---|---|---|---|
| 1 | 0.000000 | JuniperNetwo_7e:89:4a | TpLinkTech… | PPPoED | 73 | 2224 | Active Discovery Offer (PA… |
| 2 | 0.007061 | JuniperNetwo_7e:89:4a | TpLinkTech… | PPPoED | 73 | 2224 | Active Discovery Session-c… |
| 3 | 0.022102 | JuniperNetwo_7e:89:4a | TpLinkTech… | PPP LCP | 60 | 2224 | Configuration Request |
| 4 | 0.022210 | JuniperNetwo_7e:89:4a | TpLinkTech… | PPP LCP | 60 | 2224 | Configuration Ack |
| 5 | 0.025516 | JuniperNetwo_7e:89:4a | TpLinkTech… | PPP LCP | 60 | 2224 | Echo Reply |
| 6 | 0.133684 | JuniperNetwo_7e:89:4a | TpLinkTech… | PPP PAP | 60 | 2224 | Authenticate-Ack (Message=… |
| 7 | 0.136757 | JuniperNetwo_7e:89:4a | TpLinkTech… | PPP IPCP | 60 | 2224 | Configuration Request |
| 8 | 0.136786 | JuniperNetwo_7e:89:4a | TpLinkTech… | PPP IPCP | 60 | 2224 | Configuration Nak |
| 9 | 0.137382 | JuniperNetwo_7e:89:4a | TpLinkTech… | PPP IPV6CP | 60 | 2224 | Configuration Request |
| 10 | 0.256390 | JuniperNetwo_7e:89:4a | TpLinkTech… | PPP IPCP | 60 | 2224 | Configuration Ack |
| 11 | 0.256540 | JuniperNetwo_7e:89:4a | TpLinkTech… | PPP IPV6CP | 60 | 2224 | Configuration Ack |
| 12 | 0.269988 | fe80::428f:9dff:fe7e… | ff02::1 | ICMPv6 | 82 | 2224 | Router Advertisement |
| 13 | 0.281675 | 192.168.69.2 | 224.0.0.22 | IGMPv3 | 54 |  | Membership Report / Leave… |
| 14 | 0.335690 | 192.168.69.2 | 224.0.0.22 | IGMPv3 | 54 |  | Membership Report / Join g… |
| 15 | 0.340825 | 68.183.90.120 | 100.103.30… | TCP | 86 | 2224 | https(443) → 44240 [SYN, A… |
| 16 | 0.347631 | 68.183.90.120 | 100.103.30… | TCP | 90 | 2224 | [TCP Dup ACK 15#1] https(4… |
| 17 | 0.347683 | 68.183.90.120 | 100.103.30… | TCP | 78 | 2224 | https(443) → 44240 [ACK] S… |
| 18 | 0.348212 | 68.183.90.120 | 100.103.30… | TLSv1.3 | 1316 | 2224 | Server Hello, Change Ciphe… |
| 19 | 0.348240 | 68.183.90.120 | 100.103.30… | TCP | 1316 | 2224 | https(443) → 44240 [PSH, A… |
| 20 | 0.348240 | 68.183.90.120 | 100.103.30… | TLSv1.3 | 353 | 2224 | Application Data, Applicat… |
| 21 | 0.364754 | 68.183.90.120 | 100.103.30… | TCP | 90 | 2224 | [TCP Dup ACK 17#1] https(4… |
| 22 | 0.366676 | 68.183.90.120 | 100.103.30… | TCP | 353 | 2224 | [TCP Retransmission] https… |
| 23 | 0.367106 | 68.183.90.120 | 100.103.30… | TCP | 90 | 2224 | [TCP Dup ACK 17#2] https(4… |
| 24 | 0.367377 | 68.183.90.120 | 100.103.30… | TCP | 90 | 2224 | [TCP Dup ACK 17#3] https(4… |
| 25 | 0.367402 | 68.183.90.120 | 100.103.30… | TCP | 78 | 2224 | https(443) → 44240 [ACK] S… |
| 26 | 0.367451 | 68.183.90.120 | 100.103.30… | TLSv1.3 | 145 | 2224 | Application Data |
| 27 | 0.367797 | 68.183.90.120 | 100.103.30… | TLSv1.3 | 158 | 2224 | Application Data |

Packet detail (Frame 1):

```text
> Frame 1: Packet, 73 bytes on wire (584 bits), 73 bytes captured
> Ethernet II, Src: JuniperNetwo_7e:89:4a (40:8f:9d:7e:89:4a), Dst: …
> 802.1Q Virtual LAN, PRI: 0, DEI: 0, ID: 2224
> PPP-over-Ethernet Discovery
```

Hex pane (all 16 bytes per row are visible; only the ASCII gutter at the far right is cut off):

```text
0000  98 de d0 09 3b 76 40 8f   9d 7e 89 4a 81 00 08 b0
0010  88 63 11 07 00 00 00 31   01 02 00 0d 41 49 52 42
0020  52 41 53 5f 42 4c 52 2d   31 01 03 00 04 a9 be 08
0030  00 01 01 00 00 01 04 00   10 89 a4 37 e6 34 aa 81
0040  8f ae 18 fa 3f ed 53 7d   42
```

The five rows total 73 bytes, matching the frame header. `81 00 08 b0` is the 802.1Q tag, VID `0x8b0` = 2224, matching the packet detail; `88 63` is the PPPoE Discovery ethertype and `11 07` a PADO. The AC-Name tag (`01 02`, length `0x0d`) spells `AIRBRAS_BLR-1`.

Right half of the slide: a Google homepage (Gmail, Images, Google Search, I'm Feeling Lucky), footer "Google offered in:" with Indian-language links.

## Slide 29

Diagram: GEM port filtering at an ONT (this ONT is provisioned for GEM 9).

Downstream GEM frames arriving: … GEM112, GEM9, GEM10, GEM255 → ONT →
- ACCEPT → GEM9 (kept)
- DISCARD → GEM112, (GEM9 removed), GEM10, GEM255

## Slide 30

Photo of the physical tap bench: an 80:20 fibre splitter inline, feeding a NUFBER 2.5G Media Converter (its optics glowing green).

Diagram of the tap:
- From OLT → 80:20 splitter
- 80% leg → to router
- 20% leg → to our tap (into the GPON SFP stick shown)

## Slide 31

Filtering

Step 1: GEM Port Filter
Step 2: Classifier ruleset *
Step 3: Disable VLAN filtering *
Step 4: Configuring the virtual switch *
Step 5: Other CRC and checksums to disable *

## Slide 32

Demo: Indiscriminately receiving all traffic

## Slide 33

Left pane — RTL switch CLI (RTK.0>) showing a MIB counter dump and packet-size configuration:

```text
dot3StatsSymbolErrors               :          0
dot3ControlInUnknownOpcodes         :          0
etherStatsDropEvents                :      49963
etherStatsFragments                 :          0
etherStatsJabbers                   :          0
etherStatsCollisions                :          0
etherStatsCRCAlignErrors            :          0
etherStatsTxUndersizePkts           :          0
etherStatsTxOversizePkts            :          0
etherStatsTxPkts64Octets            :          0
etherStatsTxPkts65to127Octets       :          0
etherStatsTxPkts128to255Octets      :          0
etherStatsTxPkts256to511Octets      :          0
etherStatsTxPkts512to1023Octets     :          0
etherStatsTxPkts1024to1518Octets    :          0
etherStatsTxPkts1519toMaxOctets     :          0
etherStatsTxBroadcastPkts           :          0
etherStatsTxMulticastPkts           :          0
etherStatsRxUndersizePkts           :          0
etherStatsRxOversizePkts            :      87855
etherStatsRxPkts64Octets            :       6973
etherStatsRxPkts65to127Octets       :     193022
etherStatsRxPkts128to255Octets      :     739593
etherStatsRxPkts256to511Octets      :     117581
etherStatsRxPkts512to1023Octets     :     106311
etherStatsRxPkts1024to1518Octets    :    4487367
etherStatsRxPkts1519toMaxOctets     :      37892
inOamPduPkts                        :          0
outOamPduPkts                       :          0

RTK.0> # increase switch max packet size
RTK.0> switch set ma
  mac-address     - system MAC address configuration
  max-pkt-len     - max packet length
RTK.0> switch set max-pkt-len index 0 length 2000
RTK.0> switch set max-pkt-len ge port all index 0
```

Right pane — Wireshark (live capture on enp44s0), display filter `ip.addr != 192.168.69.2`:

| No. | Time | Source | Destination | Protocol | Length | vlan_id | Info |
|---|---|---|---|---|---|---|---|
| 438 | 377.454246177 | 0.0.0.0 | igmp.mcast.net | IGMPv3 | 58 | 100 | Membership Report / Join group … |
| 448 | 377.999255515 | 0.0.0.0 | igmp.mcast.net | IGMPv3 | 58 | 100 | Membership Report / Join group … |
| 538 | 387.481237483 | 0.0.0.0 | igmp.mcast.net | IGMPv3 | 58 | 100 | Membership Report / Join group … |
| 543 | 387.671254493 | 0.0.0.0 | igmp.mcast.net | IGMPv3 | 58 | 100 | Membership Report / Join group … |
| 646 | 397.506228391 | 0.0.0.0 | igmp.mcast.net | IGMPv3 | 58 | 100 | Membership Report / Leave group … |
| 648 | 397.752230663 | 0.0.0.0 | igmp.mcast.net | IGMPv3 | 58 | 100 | Membership Report / Leave group … |

Packet detail (Frame 438):

```text
> Frame 438: Packet, 58 bytes on wire (464 bits), 58 bytes captured …
> Ethernet II, Src: TaicangT&WE1_9d:76:f0 (60:bd:2c:9d:76:f0)
> 802.1Q Virtual LAN, PRI: 0, DEI: 0, ID: 100
> Internet Protocol Version 4, Src: 0.0.0.0 (0.0.0.0), Dst: 2…
    0100 .... = Version: 4
    .... 0110 = Header Length: 24 bytes (6)
  > Differentiated Services Field: 0xc0 (DSCP: CS6, ECN: Not…)
    Total Length: 40
    Identification: 0x0000 (0)
  > 010. .... = Flags: 0x2, Don't fragment
    ...0 0000 0000 0000 = Fragment Offset: 0
    Time to Live: 1
```

```text
0000  01 00 5e 00 00 16 60 bd 2c 9d 76 f0 81 00 00 64
0010  08 00 46 c0 00 28 00 00 40 00 01 02 03 fa 00 00
0020  00 00 e0 00 00 16 94 04 00 00 22 00 ea 03 00 00
0030  00 01 04 00 00 00 ef ff ff fa
```

Status bar: `enp44s0: <live capture in progress>` — Packets: 3118 · Displayed: 6 (0.2%) · Profile: Default

## Slide 34

Zoom of the Wireshark status bar:

Packets: 3118 · Displayed: 6 (0.2%)   Profile: Default

🤑❓

## Slide 35

Demo: Hello, can you hear me

## Slide 36

Figure 8-2 – Downstream GTC frame

A downstream stream of GTC frames: GTC frame n − 1 | GTC frame n | GTC frame n + 1. Each GTC frame is made of a PCBd (header) followed by a GTC payload.

The GTC payload of frame n expands into a sequence of GEM frames: GEM frame | GEM frame | GEM frame.

Figure reference: G.984.3(14)_F8-2

## Slide 37

todo: replace image

Subscriber Traffic (Inside GTP)

| Category | ~Frames | Notes |
|---|---|---|
| QUIC (HTTP/3) | 2,400,000+ | Dominant - Facebook, Google, YouTube |
| TLS over TCP | 535,000+ | Traditional HTTPS |
| Unclassified UDP | 3,500,000+ | Encrypted app data, VPN payloads |
| GRE > PPPoE > PPP | 459,552 | Fixed wireless broadband subscribers |
| RTCP/RTP | 7,500+ | Active voice/video calls |
| DNS | 41,000+ | Cleartext queries/responses |
| WireGuard VPN | 7,175 | VPN users |
| IPsec/ESP | 15,500+ | Corporate VPN users |
| STUN | 6,000+ | WebRTC NAT traversal |
| HTTP plaintext | ~780 | Health checks, OCSP, redirects |
| MQTT | 87 | IoT / push notifications |
| XMPP | 77 | IM/messaging |
| BitTorrent | 9 | P2P file sharing |
| SMTP | 8 | Plaintext email |
| SIP | 1 | VoIP signaling |

## Slide 38

POP3 session captured in cleartext (recipient/CC addresses redacted on the slide with black bars):

```text
Server:    114.31.230.18 (port 110) → subscriber 100.190.246.110
Return-Path: [redacted]
Delivered-To: [redacted]

From:      "| Altour Indochina | …r@altourindochina.com>
To:        …olidayworld.com
Cc:        … Altour |" <…@altourindochina.com>,
           …@altourindochina.com>
Subject: Re: Vietnam Tour 21st - 29th March (9D 8N) for 6 adults
         and 1 infant. (3 double rooms) CLPR
Date:    Mon, 9 Mar 2026 18:59:58 +0700

Message-ID: <CAM=3BQoA2qxdw2+dqxJgS_PfFf-DiqM-FGLviHGbz9bKoGXNnA@mail.gmail.com>
In-Reply-To: <007001dcaf9c$3317a9a0$9946fce0$@inholidayworld.com>
Content-Type: multipart/mixed (has attachments)
```

## Slide 39

Example of a DNS response

## Slide 40

FTP session captured in cleartext:

```text
Server: 10.91.122.49 (internal Airtel network)
Client: 100.78.42.219 (subscriber/device)
220 Authorized users only. All activity may be monitored and reported
234 AUTH TLS OK.
[TLS handshake]
227 Entering Passive Mode (10,91,122,49,66,113)   → port 16945
150 Accepted data connection
[~97,000 frames of file transfer]
226 File successfully transferred
221-Goodbye. You uploaded 1021 and downloaded 0 kbytes.
```

## Slide 41

HTTP redirect captured in cleartext:

```text
302 → https://uimg.bom.uncle-delivery.com:443/index.php?
        _m=s3_file_manage&_a=preview_file
        &object=OTQ1YnNHWGNaaDVXRW9FckZmQnl4UDhr... (base64)
```

## Slide 42

HTTP redirect captured in cleartext:

```text
65.109.101.238 (Hetzner) → 100.189.241.219
302 → https://www.marxists.org/archive/marx/works/1846/letters/
        admin/volunteers/biographies/admin/volunteers/biographies/
        admin/volunteers/biographies/admin/volunteers/biographies/
        works/date/admin/index.htm
```

## Slide 43

Wireshark · RTP Player

Waveform of a captured RTP audio stream. Legend: Out of Sequence (□), Wrong Timestamps (◇), Inserted Silence (△). X-axis marks around 1.44·10³, 1.46·10³, 1.48·10³ s.

| Play | Source Address | Source Port | Destination Address | Destination Port | SSRC | Setup Frame | Packets | Time Span (s) | SR (Hz) | PR (Hz) | Payloads |
|---|---|---|---|---|---|---|---|---|---|---|---|
| L | 10.5.110.146 | 42196 | 100.92.132.90 | 4000 | 0x35f73… | SETUP 3015 | 3742 | 1425.40 - 15… | 8000 | 8000 | g711A |

1 streams, 1 not muted, start: 1425.400986 s. Double click on graph to set start of playback.

Controls: Min silence: 2 · Output Device: MacBook Pro Speakers · Output Audio Rate: Automatic · Jitter Buffer: 50 · Playback Timing: Jitter Buffer · Time of Day. Buttons: Help, Refresh streams, Inaudible streams, Analyze, Prepare Filter, Export, Close.

## Slide 44

Wireshark · VoIP Calls · sip-calls-2-62.pcapng

(From/To SIP URIs partly redacted on the slide with black boxes.)

| Start Time | Stop Time | Initial Speaker | From | To | Protocol | Duration | Packets | State | Comments |
|---|---|---|---|---|---|---|---|---|---|
| 6.025905 | 38.183424 | 10.5.70.19 | …98@ka.ims.airtel.in> | <sip:…6@ka.ims.airtel.in;transport=udp;user=phone> | SIP | 00:00:32 | 3 | COMPLETED | INVITE |
| 299.221673 | 316.975788 | 10.5.70.19 | …98@ka.ims.airtel.in;user=phone> | <sip:…6@ka.ims.airtel.in;transport=udp;user=phone> | SIP | 00:00:17 | 3 | COMPLETED | INVITE |
| 1423.209761 | 1500.320549 | 10.5.70.3 | …airtel.in;user=phone> | <sip:…@ka.ims.airtel.in;transport=udp;user=phone> | SIP | 00:01:17 | 5 | COMPLETED | INVITE |
| 1762.207389 | 1782.408373 | 10.5.70.3 | …airtel.in;user=phone> | <sip:…@ka.ims.airtel.in;transport=udp;user=phone> | SIP | 00:00:20 | 4 | COMPLETED | INVITE |
| 3064.113662 | 3074.397929 | 10.5.70.3 | …airtel.in;user=phone> | <sip:…@ka.ims.airtel.in;transport=udp;user=phone> | SIP | 00:00:10 | 4 | COMPLETED | INVITE |

Options: Limit to display filter · Time of Day. Buttons: Help, Flow Sequence, Prepare Filter, Play Streams, Copy, Close.

## Slide 45

Wireshark capture of decapsulated GTP subscriber traffic (capture file `first-capture-of-others-frames-unencrypted-62.pcapng.gz`, 668579 packets).

| No. | Time | Source | Destination | Protocol | Length | Info |
|---|---|---|---|---|---|---|
| 87715 | 1290.0526069… | 2404:a800:6:248::d | 2401:4900:4bbd:99ce:1… | GTP/UDP | 1332 | https(443) → 38441 Len=1230 |
| 87716 | 1290.0526286… | 2404:a800:6:248::d | 2401:4900:4bbd:99ce:1… | GTP/UDP | 1332 | https(443) → 38441 Len=1230 |
| 87717 | 1290.0526286… | 2404:a800:6:248::d | 2401:4900:4bbd:99ce:1… | GTP/UDP | 1332 | https(443) → 38441 Len=1230 |
| 87718 | 1290.0526503… | 2404:a800:6:248::d | 2401:4900:4bbd:99ce:1… | GTP/UDP | 1332 | https(443) → 38441 Len=1230 |
| 87719 | 1290.0526504… | 2404:a800:6:248::d | 2401:4900:4bbd:99ce:1… | GTP/UDP | 1332 | https(443) → 38441 Len=1230 |
| 87720 | 1290.0526722… | 2404:a800:6:248::d | 2401:4900:4bbd:99ce:1… | GTP/UDP | 1332 | https(443) → 38441 Len=1230 |
| 87721 | 1290.0526722… | 2404:a800:6:248::d | 2401:4900:4bbd:99ce:1… | GTP/UDP | 1332 | https(443) → 38441 Len=1230 |
| 87722 | 1290.0526940… | 2404:a800:6:248::d | 2401:4900:4bbd:99ce:1… | GTP/UDP | 1332 | https(443) → 38441 Len=1230 |
| 87723 | 1290.0526940… | 2404:a800:6:248::d | 2401:4900:4bbd:99ce:1… | GTP/UDP | 1332 | https(443) → 38441 Len=1230 |
| 87724 | 1290.0527157… | 2404:a800:6:248::d | 2401:4900:4bbd:99ce:1… | GTP/UDP | 1332 | https(443) → 38441 Len=1230 |
| 87725 | 1290.0527157… | 2404:a800:6:248::d | 2401:4900:4bbd:99ce:1… | GTP/UDP | 1332 | https(443) → 38441 Len=1230 |
| 87726 | 1290.0527374… | 2404:a800:6:248::d | 2401:4900:4bbd:99ce:1… | GTP/UDP | 1332 | https(443) → 38441 Len=1230 |
| 87727 | 1290.0527375… | 2404:a800:6:248::d | 2401:4900:4bbd:99ce:1… | GTP/UDP | 1332 | https(443) → 38441 Len=1230 |
| 87728 | 1290.0527599… | 2404:a800:6:248::d | 2401:4900:4bbd:99ce:1… | GTP/UDP | 1332 | https(443) → 38441 Len=1230 |
| 87729 | 1290.0527599… | instagram.fblr1-7.fna.fbcdn.net | 2401:4900:88cd:3db2:1… | GTP/QUIC | 1408 | Protected Payload (KP0) |
| 87730 | 1290.0527817… | instagram.fblr1-7.fna.fbcdn.net | 2401:4900:88cd:3db2:1… | GTP/QUIC | 1408 | Protected Payload (KP0) |
| 87731 | 1290.0527818… | instagram.fblr1-7.fna.fbcdn.net | 2401:4900:88cd:3db2:1… | GTP/QUIC | 1408 | Protected Payload (KP0) |
| 87732 | 1290.0528040… | instagram.fblr1-7.fna.fbcdn.net | 2401:4900:88cd:3db2:1… | GTP/QUIC | 1408 | Protected Payload (KP0) |
| 87733 | 1290.0528040… | instagram.fblr1-7.fna.fbcdn.net | 2401:4900:88cd:3db2:1… | GTP/QUIC | 1408 | Protected Payload (KP0) |
| 87734 | 1290.0528259… | instagram.fblr1-7.fna.fbcdn.net | 2401:4900:88cd:3db2:1… | GTP/QUIC | 1408 | Protected Payload (KP0) |
| 87735 | 1290.0528564… | 2603:1046:c06:c46::2 | 2401:4900:c97a:270d:4… | GTP/TCP | 134 | imaps(993) → 54607 [ACK] Seq=17215 Ack=585 Win=4032 Len=0 |
| 87736 | 1290.0529295… | 2401:4900:50:9::194 | 2401:4900:3316:959f:1… | GTP/DNS | 202 | Standard query response 0x160c A www.googleapis.com A 216.239.36.223 A 216.239.32.223 A 216.239.34.223 A 21… |
| 87737 | 1290.0529510… | scontent.fixe1-3.fna.fbcdn.net | 2401:4900:c940:9c9b:4… | GTP/UDP | 1354 | https(443) → 44017 Len=1232 |
| 87738 | 1290.0529727… | scontent.fixe1-3.fna.fbcdn.net | 2401:4900:c940:9c9b:4… | GTP/UDP | 1354 | https(443) → 44017 Len=1232 |
| 87739 | 1290.0529727… | scontent.fixe1-3.fna.fbcdn.net | 2401:4900:c940:9c9b:4… | GTP/UDP | 1354 | https(443) → 44017 Len=1232 |
| 87740 | 1290.0529947… | scontent.fixe1-3.fna.fbcdn.net | 2401:4900:c940:9c9b:4… | GTP/UDP | 1354 | https(443) → 44017 Len=1232 |
| 87741 | 1290.0529947… | scontent.fixe1-3.fna.fbcdn.net | 2401:4900:c940:9c9b:4… | GTP/UDP | 1354 | https(443) → 44017 Len=1232 |
| 87742 | 1290.0530163… | rr8.sn-ci5gup-cagee.gvt1.com | 2401:4900:376c:6ab9:1… | GTP/QUIC | 1332 | Protected Payload (KP0) |
| 87743 | 1290.0532175… | scontent.fixe1-3.fna.fbcdn.net | 2401:4900:c940:9c9b:4… | GTP/UDP | 1354 | https(443) → 44017 Len=1232 |
| 87744 | 1290.0532389… | scontent.fixe1-3.fna.fbcdn.net | 2401:4900:c940:9c9b:4… | GTP/UDP | 1354 | https(443) → 44017 Len=1232 |

Packet detail (Frame 1):

```text
> Frame 1: Packet, 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface enp44s0, id 0
> Ethernet II, Src: ZyxelCommuni_2b:dc:d1 (fc:9f:2a:2b:dc:d1), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
> Address Resolution Protocol (request)
```

```text
0000  ff ff ff ff ff ff fc 9f 2a 2b dc d1 08 06 00 01
0010  08 00 06 04 00 01 fc 9f 2a 2b dc d1 c0 a8 45 02
0020  00 00 00 00 00 00 c0 a8 45 01
```

## Slide 46

Same GTP subscriber capture as the previous slide, with a magnified inset over the Destination and Protocol columns (packets 87715–87744).

Visible Destination / Protocol pairs down the inset:
- 2401:4900:4bbd:99ce:1… — GTP/UDP (×3)
- 2401:4900:88cd:3db2:1… — GTP/QUIC (×6)
- 2401:4900:c97a:270d:4… — GTP/TCP
- 2401:4900:3316:959f:1… — GTP/DNS
- 2401:4900:c940:9c9b:4… — GTP/UDP (several)
- 2401:4900:376c:6ab9:1… — GTP/QUIC
- 2401:4900:c940:9c9b:4… — GTP/UDP

## Slide 47

Packet detail — a decapsulated HTTP/1.1 response carried inside GTP:

```text
> Frame 89241: Packet, 253 bytes on wire (2024 bits), 253 bytes captured (2024 bits) on interface enp44s0, id 0
> Ethernet II, Src: Cisco_2b:7c:81 (d4:7f:35:2b:7c:81), Dst: Ericsson_a2:00:3c (e4:0d:3b:a2:00:3c)
> 802.1Q Virtual LAN, PRI: 0, DEI: 0, ID: 732
> Internet Protocol Version 4, Src: 10.206.168.115 (10.206.168.115), Dst: 100.108.238.118 (100.108.238.118)
> User Datagram Protocol, Src Port: gtp-user (2152), Dst Port: gtp-user (2152)
> GPRS Tunneling Protocol
> Internet Protocol Version 6, Src: update.googleapis.com (2404:6800:4007:815::2003), Dst: 2401:4900:3765:778d:291a:f929:f707:376e (24…
> Transmission Control Protocol, Src Port: http (80), Dst Port: 46118 (46118), Seq: 1, Ack: 1, Len: 127
v Hypertext Transfer Protocol
    > HTTP/1.1 204 No Content\r\n
    > Content-Length: 0\r\n
      Cross-Origin-Resource-Policy: cross-origin\r\n
      Date: Tue, 10 Mar 2026 03:08:52 GMT\r\n
      \r\n
```

## Slide 48

<add GTP traffic analysis here>

## Slide 49

<image of the downstream only DNS responses>

## Slide 50

Exploded diagram of an optical splitter package. Labels:

- End Cap boot (both ends)
- Outer Housing
- Input Fiber Array
- Epoxy (two joints)
- Splitter Chip
- Fiber Array Lid
- Fiber Array V-Groove
- Interface Splitter Chip / Fiber Array
- Output Fiber Array
- Ribbon Fiber

## Slide 51

Diagram: Optical Line Terminal → Splitter → Optical Network Unit. The OLT and Splitter are boxed as "What they physically control"; the Optical Network Unit is boxed separately as "In our home 🤑".

ISPs assume they control this

## Slide 52

Diagram: Optical Line Terminal → Splitter → Optical Network Unit. The solid box labelled "What they physically control" encloses only the **Optical Line Terminal**; the solid box labelled "In our home 🤑" encloses the **Optical Network Unit**; the **Splitter** sits between them in its own dashed box, in neither. An outer box encloses all three.

ISPs assume they control this

## Slide 53

## Slide 54

## Slide 55

Diagram: OLT → splitter → four ONTs (fibre fan-out), with a 😋 emoji placed on the feeder fibre between the OLT and the splitter, marking where the attacker taps.

## Slide 56

Browser screenshot of the Wikipedia article "Room 641A".

Site chrome: Wikipedia (25 years of the free encyclopedia) · Search Wikipedia · Donate · Create account · Log in. Banner: "You are invited to join the Bay Area Wiki-Picnic at Mission Dolores Park on Saturday, June 13!"

Room 641A — Article / Talk · Read / Edit / View history / Tools · 12 languages · Coordinates: 37°47′07″N 122°23′48″W

From Wikipedia, the free encyclopedia

Room 641A is a telecommunication interception facility operated by AT&T for the U.S. National Security Agency, as part of an American mass surveillance program. The facility commenced operations in 2003, and its purpose was publicly revealed by AT&T technician Mark Klein in 2006.[1][2]

Description

Room 641A is located in the SBC Communications building at 611 Folsom Street, San Francisco, three floors of which were occupied by AT&T before SBC purchased AT&T.[1] The room was referred to in internal AT&T documents as the SG3 [Study Group 3] Secure Room.

The room measures about 24 by 48 feet (7.3 by 14.6 m) and contains several racks of equipment, including a Narus STA 6400, a device designed to intercept and analyze Internet communications at very high speeds.[1] It is fed by fiber optic lines from beam splitters installed in fiber optic trunks carrying Internet backbone traffic.[3] In the analysis of J. Scott Marcus, a former CTO for GTE and a former adviser to the Federal Communications Commission, it has access to all Internet traffic that passes through the building, and therefore "the capability to enable surveillance and analysis of internet content on a massive scale, including both overseas and purely domestic traffic."[4]

Contents: (Top), Description, Lawsuits, Gallery, See also, References, External links. Image caption: "Room 641A's exterior". Infobox: National Security Agency surveillance — Map of global NSA data collection as of 2007. Appearance panel: Text (Small / Standard / Large), Width (Standard / Wide), Color (Automatic / Light / Dark).

## Slide 57

Media viewer showing a photograph captioned:

A fiber optic tap

Attribution: Roens - Own work · CC BY-SA 4.0 · view terms · More details

## Slide 58


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
12.1 Basic threat model
The basic concern in PON is that the
, then the malicious user
It is this 'eavesdropping threat' that the PON security system is
intended to counter. Other, more exotic threats are not considered practically important because, in
order to attempt these attacks, the user would have to expend more resources than it would be worth.
Furthermore, the PON itself has the unique property in that it is highly directional. So any ONU
cannot observe the upstream traffic from the other ONUs on the PON. This allows privileged
information (such as security keys) to be passed upstream in the clear. While there are threats that
could jeopardize this situation, such as an attacker tapping the common fibres of the PON, these again
are not considered realistic, since the attacker would have to do so in public spaces, and would
probably impair the very PON being tapped.
```

## Slide 59

OLT ↔ ONU key-exchange sequence (Optical Line Terminal on the left, Optical Network Unit on the right):

- Request_Key (PLOAM)  (OLT → ONU)
- (128-bit AES keygen)  (at the ONU)
- Key broadcast in plaintext x3  (ONU → OLT)
- OLT switches keys
- *snip*
- enc_aes(data)  (OLT → ONU)
- *snip*

## Slide 60


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
12.1 Basic threat model
The basic concern in PON is that the downstream data is broadcast to all ONUs attached to the PON.
If a malicious user were to re-programme his ONU, then the malicious user could listen to all the
downstream data of all the users. It is this 'eavesdropping threat' that the PON security system is
intended to counter. Other, more exotic threats are not considered practically important because, in
order to attempt these attacks, the user would have to expend more resources than it would be worth.
Furthermore, the PON itself has the unique property in that it is So any
This allows privileged
information (such as ) to be While there are threats that
could jeopardize this situation, such as an attacker tapping the common fibres of the PON, these again
are not considered realistic, since the attacker would have to do so in public spaces, and would
probably impair the very PON being tapped.
```

## Slide 61


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
12.1 Basic threat model
The basic concern in PON is that the downstream data is broadcast to all ONUs attached to the PON.
If a malicious user were to re-programme his ONU, then the malicious user could listen to all the
downstream data of all the users. It is this 'eavesdropping threat' that the PON security system is
intended to counter. Other, because, in
order to attempt these attacks, the user would have to expend more resources than it would be worth.
Furthermore, the PON itself has the unique property in that it is highly directional. So any ONU
cannot observe the upstream traffic from the other ONUs on the PON. This allows privileged
information (such as security keys) to be passed upstream in the clear. While there are threats that
could jeopardize this situation,
since the attacker would have to do so in public spaces, and would
probably
```

## Slide 62

haven't you always wanted to be an  exotic threat  ?

("exotic threat" highlighted in yellow.)

## Slide 63

Diagram: Optical Line Terminal → Splitter → Optical Network Unit, each labelled with a status emoji:
- Optical Line Terminal — 😋
- Splitter — ✅
- Optical Network Unit — ✅

## Slide 64

Rules of the game

Rule 1: Must be exploited over the optical fiber line
Rule 2: Must be possible from a subscriber port
Rule 3: Must work with encryption enabled

## Slide 65

:)

## Slide 66

## Slide 67

## Slide 68

## Slide 69

## Slide 70

## Slide 71

## Slide 72

## Slide 73

## Slide 74

Unsanitized Input

## Slide 75

Stored Same Site Scripting

## Slide 76

Stored Same Site Scripting

## Slide 77

Stored Same Site Scripting

## Slide 78

Stored Cross Site Scripting

## Slide 79

Command Injection

## Slide 80

## Slide 81

Demo: Hacking the OLT

## Slide 82

Diagram: Optical Line Terminal → Splitter → Optical Network Unit, each labelled with a status emoji:
- Optical Line Terminal — 😋
- Splitter — ✅
- Optical Network Unit — ✅

## Slide 83

What can be done with OLT access?

- Firmware upgrade all ONUs connected
- Capture two way traffic
- Encryption keys etc.
- DNS poisoning

## Slide 84

Takeaways

## Slide 85

Acknowledgements

## Slide 86

Stay in touch!

## Slide 87

## Slide 88

Why 125µs for the frame length?
On GEM frame length

- Ancient history, but it is 1/8000th of a second
- Because of SONET etc etc.
- Old school phone calls are sampled at 8kHz and when the spec was designed, it just used the same frequency because clock chips were cheap (?)

## Slide 89

What is GPON?
Gigabit Passive Optical Network

- 1490nm DS and 1310nm US
   - TDMA to share the medium upstream
   - ~~Passive optics to split light to subscribers~~

## Slide 90

O1-O5 states
PLOAM and bringing a new ONU up

OLT ↔ ONU activation sequence diagram:

- Downstream synchronization (OLT → ONU) — state O1
- Burst Profile (OLT → ONU)
- SN Request (BWMap) (OLT → ONU)
- Serial_Number_Onu (ONU → OLT) — states O2-O3
- SN Verified (processing at OLT)
- Assign ONU-ID (OLT → ONU)
- Ranging Request (BWMap) (OLT → ONU) — state O4
- Registration_ID (ONU → OLT)
- Ranging_Time (OLT → ONU)
- Acknowledgement Message (ONU → OLT)
- state O5
- Create OMCC and send out business configurations

## Slide 91

GEM
GEM Port allocation

GEM Ports: GPON Encapsulation Method

- Subscriber can get one or more GEM ports

Usually:
- 1x Internet access (per)
- 1x Voice (per)
- 1x IPTV

Diagram: inside the PON, the OLT exposes many Ports; each Port is cross-connected to a GEM Port Filter in front of an ONU, so a given ONU only accepts the GEM ports assigned to it.

## Slide 92

SFP+ module ONU stick
Pinout

Screenshot of a transceiver vendor's product page. Left menu "Industrial Transceivers": QSFP-4W20-100G-I, QSFP-4W40-100G-I, QSFP-BX40-100G-I, QSFP-CWDM4-100G-I, QSFP-LR4-100G-I, QSFP-LR4-40G-I, QSFP-PLR4-40G-I, QSFP-SR4-100G-I, QSFP-SR4-40G-I, QSFP-ZR4-100G-I, SFP-100FX-31-I, SFP-100LX-31-I, SFP-10G-T-30I, SFP-10G23-BX10-I, SFP-10G23-BX20-I, SFP-10G23-BX40-I, SFP-10G23-BX60-I, SFP-10G32-BX10-I, SFP-10G32-BX20-I, SFP-10G32-BX40-I, SFP-10G32-BX60-I, SFP-10G45-BX80-I, SFP-10G54-BX80-I, SFP-10GER-31-I, …

Right panel (On this page) — product: GPON ONU Stick with MAC and Web Interface SFP, 1310TX/1490RX, Class B+, 20km, I-Temp. Sections: Applications, Features, Description, Product Specifications (I. Absolute Maximum Ratings, II. Recommended Operating Conditions, III. Pin Descriptions, IV. Electrical Characteristics, VII. Optical Characteristics, VIII. Digital Diagnostics Monitoring Interface, IX. Mechanical Diagram), Test Center, Test Assured Program, Order Information.

III. Pin Descriptions

| PIN | Symbol | Description | Plug Seq. | Note |
|---|---|---|---|---|
| 1 | VeeT | Transmitter Ground | 1 | |
| 2 | TX Fault | Transmitter Fault Indication | 3 | |
| 3 | TX Disable | Transmitter Disable. Module disables on high or open | 3 | |
| 4 | SDA | 2 wire serial ID Interface Data Line (MOD-DEF2) | 3 | |
| 5 | SCL | 2 wire serial ID Interface Clock (MOD-DEF1) | 3 | |
| 6 | MOD-ABS | Grounded within the module | 3 | |
| 7 | Rate Select | Function not available, pulled down with 100KΩ resistor in the module | 3 | |
| 8 | Los | Loss of Signal | 3 | |
| 9 | VeeR | Receiver Ground | 1 | |
| 10 | VeeR | Receiver Ground | 1 | |
| 11 | VeeR | Receiver Ground | 1 | |
| 12 | RD- | Received inverted DATA out. | 3 | |
| 13 | RD+ | Received DATA out | 3 | |
| 14 | VeeR | Receiver Ground | 1 | |
| 15 | VccR | Receiver Power. 3.3V±5%. | 2 | |
| 16 | VccT | Transmitter Power. 3.3V±5%. | 2 | |
| 17 | VeeT | Transmitter Ground | 1 | |
| 18 | TD+ | Transmit DATA in. AC Coupled. | 3 | |
| 19 | TD- | Transmit Inverted DATA in. AC Coupled. | 3 | |
| 20 | VeeT | Transmitter Ground | 1 | |

Diagram of Host Board Connector Block Pin Number and Names — left column pins 1-10 (VeeT, Tx_Fault, Tx-Disable, SDA, SCL, MOD-ABS, Rate Select, LOS, VeeR, VeeR), right column pins 20-11 (VeeT, TD-, TD+, VeeT, VccT, VccR, VeeR, RD+, RD-, VeeR). Towards Bezel ← … → Towards ASIC.

## Slide 93

GEM frame fragmentation

Interactive demo — "gem fragmentation":

one ethernet frame, chopped into gem frames sized by the allocation window. each fragment re-pays the 5-byte header tax; only the last carries END.

the ethernet frame (payload the OLT wants to send to one subscriber):
a b c d e f g h i j k l m n o p q r s t u v w x

allocation window: 8 bytes

↓ gem fragments on the wire — each chunk re-headered, only the last flagged END

```text
GEM hdr (5B)  pli=8 port=33 pti=MORE   |  a b c d e f g h
GEM hdr (5B)  pli=8 port=33 pti=MORE   |  i j k l m n o p
GEM hdr (5B)  pli=8 port=33 pti=END    |  q r s t u v w x
```

- gem frames: 3
- header bytes added: 15
- overhead: 38%

## Slide 94

Upstream
Why are we only seeing downstream traffic?

- Different frequencies for upstream transmission
   - ONU modules don't have photodiode sensitive to the upstream λ
- Geometry of the splitter
   - Highly directional and lossy from one downstream leg to another

## Slide 95

gpon: downstream broadcast vs upstream tdma

downstream (OLT→ONUs): one continuous pulse train, every ONU hears every bit. upstream (ONUs→OLT): time-division — each ONU bursts ONLY in the timeslot the OLT granted it, so bursts never collide on the shared fiber.

Controls: pause · speed 0.3× · show ranging delays

Animation: OLT → 1:4 splitter → ONU 1, ONU 2, ONU 3, ONU 4.

upstream frame (BWmap allocations) — guard gap after last slot

downstream: 7 pulses continuously broadcast to all 4 ONUs — upstream: only the ONU whose slot is live transmits

Legend: downstream broadcast (all ONUs) · ONU 1 burst · ONU 2 burst · ONU 3 burst · ONU 4 burst

## Slide 96

Tap diagram — inserting 10:90 splitters into the feeder.

- OLT → 1490nm downstream into a 10:90 splitter.
- Splitter (right) → 1310nm upstream into a second 10:90 splitter.
- Each 10:90 splitter sends its 90% leg back to the network and its 10% leg to us.
- 10% leg — to us (downstream side): "This becomes the source of our downstream tap".
- 10% leg — to us (upstream side): "This becomes the source of our upstream tap".

