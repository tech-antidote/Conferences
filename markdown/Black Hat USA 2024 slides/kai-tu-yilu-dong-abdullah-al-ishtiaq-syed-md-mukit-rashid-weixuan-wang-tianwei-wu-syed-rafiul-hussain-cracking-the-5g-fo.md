---
title: "Cracking the 5G Fortress Peering Into 5G's Vulnerability Abyss"
speakers: ["Kai Tu", "Yilu Dong", "Abdullah Al Ishtiaq", "Syed Md Mukit Rashid", "Weixuan Wang", "Tianwei Wu", "Syed Rafiul Hussain"]
conference: "Black Hat"
conference_full: "Black Hat USA 2024"
edition: "USA"
year: 2024
source_pdf: "Black Hat USA 2024 slides/Kai Tu & Yilu Dong & Abdullah Al Ishtiaq & Syed Md Mukit Rashid & Weixuan Wang & Tianwei Wu & Syed Rafiul Hussain_Cracking the 5G Fortress Peering Into 5G's Vulnerability Abyss.pdf"
pages: 44
sha256: "ceb80823f5833e17d22bd8814ac44d3686d0a58c3c28250c492ebc7499b4da83"
text_chars: 14603
ocr_pages: 4
has_ocr: true
redacted_secrets: 0
ocr_confidence: 87.8
ocr_unreliable_blocks: 1
vision_verified_blocks: 1
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:34:54Z"
---
# Cracking the 5G Fortress Peering Into 5G's Vulnerability Abyss

**Speakers:** Kai Tu, Yilu Dong, Abdullah Al Ishtiaq, Syed Md Mukit Rashid, Weixuan Wang, Tianwei Wu, Syed Rafiul Hussain  
**Conference:** Black Hat USA 2024  
**Source:** `Black Hat USA 2024 slides/Kai Tu & Yilu Dong & Abdullah Al Ishtiaq & Syed Md Mukit Rashid & Weixuan Wang & Tianwei Wu & Syed Rafiul Hussain_Cracking the 5G Fortress Peering Into 5G's Vulnerability Abyss.pdf` (44 pages)


## Slide 1

Cracking the 5G Fortress: Peering Into 5G’s Vulnerability Abyss **Speakers: Kai Tu, Yilu Dong** Contributors: Abdullah Al Ishtiaq, Syed Md Mukit Rashid, Weixuan Wang, Tianwei Wu, Syed Rafiul Hussain

#BHUSA @BlackHatEvents

## Slide 2

Who We Are

Kai Tu PhD Student

Yilu Dong PhD Student

Mobile Network and Device Security, Automatic Vulnerability Discovery <u>hellotkk.github.io</u>

Cellular Networks, Applied Cryptography, and Software Testing <u>yilud.me</u>

#BHUSA @BlackHatEvents

## Slide 3

### 5G Network Roles and Applications

#BHUSA @BlackHatEvents

## Slide 4

#### Why is 5G Baseband Security Important?

• Users will run into critical problems if basebands are not secure.

Source: https://www.securityweek.com/5ghoul-vulnerabilities-haunt-qualcomm-mediatek-5g-modems/

Source:https://www.darkreading.com/mobile-security/your-phone-s-5g-connection-is-exposed-to-bypass-dos-attacks

• Compromised 5G device may also affect other components in 5G network.

Source: https://www.trendmicro.com/en_us/research/23/i/attacks-on-5g-infrastructure-from-users-devices.html

#BHUSA @BlackHatEvents

## Slide 5

### We are curious…

## **How secure are the 5G devices? Can we develop an automated way to test them?**

#BHUSA @BlackHatEvents

## Slide 6

What we Are Going to Talk About Today

- 5G cellular network overview

- Workflow of our automated 5G baseband testing tool

- • Summary of findings

- 5G AKA bypass end-to-end exploitations demos

- • Impact and Status • Takeaways

#BHUSA @BlackHatEvents

## Slide 7

### 5G Network Architecture

AMF UDM
5G UE gNodeB
SMF UPF
Internet
…
5G Core Network

#BHUSA @BlackHatEvents

## Slide 8

5G Control Plane
RRC NAS
Radio connection
Authentication Procedure
Security Mode Control Procedure
AS Security Activation
Registered to Core Network and ready to get services

#BHUSA @BlackHatEvents

## Slide 9

### Our Scope

UDM
AMF
UE
SMF UPF
Internet
…
gNB 5G Core Network

#BHUSA @BlackHatEvents

## Slide 10

## Baseband Protocol Implementation - Easy Work? **Why can protocol implementations in commercial basebands go wrong?**

#BHUSA @BlackHatEvents

## Slide 11

### Baseband protocol is hard to Implement…

Hundreds of Difficult to Conflicts and documents understand underspecifications

#BHUSA @BlackHatEvents

## Slide 12

Non-compliant behavior may lead to…

Exploitable vulnerabilities

Interoperability issues

#BHUSA @BlackHatEvents

## Slide 13

### Our Goal

**Is it possible to develop an automated framework to identify security policy violations in 5G UE implementations efficiently?**

#BHUSA @BlackHatEvents

## Slide 14

### Key Intuition of 5GBaseChecker

Output: O1 O2... On
5GBaseChecker
Differential Testing ...
Input: I1I2...In
Output: O1 O2...O’n

#BHUSA @BlackHatEvents

## Slide 15

### How to Generate Input

- Generate random input sequences will not work…

- Build Finite State Machine (FSM) for each baseband, then identify the differences among FSMs!

#BHUSA @BlackHatEvents

## Slide 16

#### High-Level Workflow of 5GBaseChecker

StateSynth:
FSM Synthesizer

DevScan: Identifying Deviations

DevLyzer: Triaging the Deviations

#BHUSA @BlackHatEvents

## Slide 17

### StateSynth: Constructing FSM

- **StateSynth** module extracts finite state machines (FSMs) from 5G baseband implementations.

- StateSynth's hybrid and collaborative FSM learning technique significantly improves FSM learning efficiency.

Queries/
Network Trace 5G UE Implementations Responses

Passive Learner
Passive  Active Leaner W/ Counter-
Automata example (CE) reuse
Synthesized FSMs
CEs

#BHUSA @BlackHatEvents

## Slide 18

### DevScan: Identifying Deviations

FSM 1
Deviation scanner Graph traversal Unique deviations
using symbolic  I1 I2 In  / O1 O2 On
FSM 2 model checker  I1 I2 In  / O1 O2 O’n

- **DevScan** uses symbolic model checking technique to automatically identifies the deviations between FSMs.

#BHUSA @BlackHatEvents

## Slide 19

### DevLyzer: Triaging Deviations

3GPP Specification
Benign Traces
𝑇⊨ϕ?
I1 I2 In  / O1 O2 On
Vulnerable Traces
I1 I2 In  / O1 O2 O’n
and Property
𝑇 … Violation
DevLyzer
Unique deviating traces

- **DevLyzer** aids human experts to triage the deviations found by DevScan.

#BHUSA @BlackHatEvents

## Slide 20

### Summary of Vulnerabilities

- 13 vulnerabilities in 17 devices from 5 different baseband vendors and 2 open-source implementations

- 3 types of flaws and 4 types of impacts

- Demo: 5G AKA Bypass

#BHUSA @BlackHatEvents

## Slide 21

### Types of Flaws

- Accepting invalid Security Header Types

- Accepting message types that should not be accepted in a certain state

- Mishandling Information Elements (IEs)

#BHUSA @BlackHatEvents

## Slide 22

### 5G Control-Plane Message Structure

RRC NAS
Message Message
Message Security Header IE IE IE IE
Type Type (SHT) 1 2 3 …

#BHUSA @BlackHatEvents

## Slide 23

### Impact of Vulnerabilities Found

Information Phishing
Leak

Downgrade Denial-of-
Service

#BHUSA @BlackHatEvents

## Slide 24

### Impact of Vulnerabilities Found

Information Leak

Phishing

Downgrade Denial-of-
Service

#BHUSA @BlackHatEvents

## Slide 25

### Impact of Vulnerabilities Found

Information Phishing Leak

Downgrade Denial-of-
Service

#BHUSA @BlackHatEvents

## Slide 26

### Impact of Vulnerabilities Found

Information Phishing
Leak

Downgrade

Denial-of-
Service

#BHUSA @BlackHatEvents

## Slide 27

### Impact of Vulnerabilities Found

Information Phishing
Leak

Downgrade Denial-ofService

#BHUSA @BlackHatEvents

## Slide 28

### 5G AKA Bypass

- Bypass 5G Authentication and Key Agreement procedure

   - CVE-2023-50804

- Found in Exynos basebands (Exynos 5123 and Exynos 5300)

- No mutual authentication between the phone and the network

- Attacker can provide services to the user (Send SMS, provide Internet access, etc. )

#BHUSA @BlackHatEvents

## Slide 29

5G Registration
Registration Request
Authentication Procedure
Security Mode Control Procedure
Secured Communication Start
Registration Accept
Registration Complete
PDU Session Est Request
PDU Session Est Accept
Internet Access Start

#BHUSA @BlackHatEvents

## Slide 30

5G AKA Bypass
Registration Request
Authentication Procedure
Security Mode Control Procedure
Secured Communication Start
Registration Accept (SHT 4)
Registration Complete

#BHUSA @BlackHatEvents

## Slide 31

### Demo: Internet Traffic Eavesdropping

5G AKA Bypass
PDU Session Est Request
PDU Session Est Accept
w/ SHT 4

#BHUSA @BlackHatEvents

## Slide 32

### Assemble the Attack Message

PDU Session Establishment Accept

Establishes a PDU session for Internet access

#BHUSA @BlackHatEvents

## Slide 33

### Assemble the Attack Message

DL NAS PDU Session
Transport Establishment Accept

With Security Header Type 4 Same as CVE-2023-50804

#BHUSA @BlackHatEvents

## Slide 34

### Assemble the Attack Message

RRC DL NAS Reconfiguration Transport

PDU Session Establishment Accept

w/ prohibited IE(s) drb-ToAddModList

CVE-2024-29152

#BHUSA @BlackHatEvents

## Slide 35

### Attack Setup

- Hardware: SDR (USRP B210)

- Software: OpenAirInterface + Open5GS

#BHUSA @BlackHatEvents

## Slide 36

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
+1
kai@kal: ~/Desktop/SGBaseChecker_Core
kai@kai: ~/Desktop/clean/openairinter...
Attacker
Terminal
Tap for weather info
Attacker ja
»* 66
Galaxy Store Gallery Play Store Google
Wireless Tools Help
```

## Slide 37

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
eal kai@kai: ~/Desktop/SGBaseChecker_Core : = = 1 x
[upf] : [Added] Number of UPF-Sessions
is now 1 (../src/upf/context.c:178) .
(../lib/gtp/path.c:60)
: [upf] : UE F-SEID[CP:0x1 UP:0x1] APN[in
ternet] PDN-Type[1] IPv4[10.45.0.2] IPv6[] (../src/upf/context.
: [upf] : UE F-SEID[CP:0x1 UP:0x1] APN[in
ternet] PDN-Type[1] IPv4[10.45.0.2] IPv6[] (../src/upf/context.
c:397)
: [gtp] : gtp_connect() [127.0.0.7]:2152
(../lib/gtp/path.c:60)
: [amf] : ©x7f40a981c010 (../src/amf/n
amf-handler.c:83)
[sctp] : sctp_senddata (../lib/sctp/ogs
[anf] : number of events in queue 1 (..
: [gtp] : gtp_connect() [127.0.0.5]:2152
(../lib/gtp/path.c:60)
: [amf] : set e->h.sbi.message (../src/am
+1 kai@kai: ~/Desktop/clean/openairinter. x
CellGroup
[NR_MAC] Activating RRC processing timer »Attacker
ms
[NR_MAC] Modified rnti 4a16 with CellGroup
[NR_MAC] Added new CBRA process for UE RNTI 4a16 with initial
CellGroup
[NR_RRC] Receive RRC Reconfiguration Complete message UE 4a16
:add_drb_am: warning DRB 1 already exist for UE ID/RNTI 18966,
do nothing
_drb:911: added DRB for UE ID/RNTI 18966
[RLC] ../../../openair2/LAYER2/nr_rlc/nr_rlc_oai_api.c:761:ad
d_drb_am: DRB 1 already exists for UE with RNTI 4a16, do nothin
_add_drb:860: added DRB to UE with RNTI 0x4a16
[NR_RRC] msg index 0, pdu_sessions index 0, status 2, xid 0):
nb_of_pdusessions 1, pdusession_id 5, teid: 1166204179
[NR_RRC] NGAP_PDUSESSION_SETUP_RESP: sending the message
[NGAP] pdusession_setup_resp_p: pdusession ID 5, gnb_addr 127
-0.0.5, SIZE 4
[PDCP] discard NR PDU rcvd_count=6, entity->rx_deliv 10,sdu_i
n_list 0
© Airplane mode
off
Protocol Info
963 NGAP NGSetupResponse
3169 NGAP/N... InitialUEMessage, Registration request,
3249 NGAP/N... DownlinkNASTransport, Identity request
3255 NGAP/N... SACK (Ack=1, Arwnd=3@
3340 NGAP/N... DownlinkNASTranspor
3351 NGAP/ SACK (Ack=
3465 NGAP/N... UplLinkNAST UL NAS transport,
3608 NGAP rs 106496) ,
Attack Message
a
ip.addr 27.0.0.5 && dns || ngap || gtp
Registration request
ort, Identity response
ort, Registration complete
PDUSessionResourceSetupResponse
PDU session establishment request
PDUSessionResourceSetupRequest, DL NAS transport,
Authentication Bypassed!
Frame (118 bytes)
PDU s
»
20:19 SAB
< Airplane mode
Off
Turns off all network connections including
calling, texting, internet access, Wi-Fi, and
Bluetooth
While Airplane mode is on, you can turn Wi-Fi
and Bluetooth on again in Settings or the quick
settings panel
```

## Slide 38

#BHUSA @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 87/100 on the text kept, 82/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
[Top-left terminal - title: kai@kai: ~/Desktop/5GBaseChecker_Core - labeled "Attacker Terminal"]
...NN[internet] IPv4[10.45.0.2] IPv6[] (../src/sm[obscured]f-handler.c:497)
04/06 20:19:47.410: [upf] INFO: [Added] Number of UPF-Sessions is now 1 (../src/upf/context.c:178)
04/06 20:19:47.410: [gtp] INFO: gtp_connect() [obscured] (../lib/gtp/path.c:60)
04/06 20:19:47.410: [upf] INFO: UE F-SEID[CP:0x1 UP:0x1] APN[internet] PDN-Type[1] IPv4[10.45.0.2] IPv6[] (../src/upf/context.c:397)
04/06 20:19:47.410: [upf] INFO: UE F-SEID[CP:0x1 UP:0x1] APN[internet] PDN-Type[1] IPv4[10.45.0.2] IPv6[] (../src/upf/context.c:397)
04/06 20:19:47.410: [gtp] INFO: gtp_connect() [127.0.0.7]:2152 (../lib/gtp/path.c:60)
04/06 20:19:47.411: [amf] WARNING: 0x7f40a981c010 (../src/amf/namf-handler.c:83)
04/06 20:19:47.411: [sctp] INFO: sctp_senddata (../lib/sctp/ogs-sctp.c:73)
04/06 20:19:47.446: [amf] INFO: number of events in queue 1 (../src/amf/event.c:106)
04/06 20:19:47.446: [gtp] INFO: gtp_connect() [127.0.0.5]:2152 (../lib/gtp/path.c:60)
04/06 20:19:47.446: [amf] INFO: set e->h.sbi.message (../src/amf/amf-sm.c:511)

[Bottom-left terminal - title: kai@kai: ~/Desktop/clean/openairinter... - labeled "Attacker Terminal"]
harq rounds)
[NR_MAC]   handle harq for rnti 636f, in RA p...
[NR_MAC]   handle_nr_ul_harq(): unknown RNTI 0x636f in PUSCH
[NR_PHY]   [gNB 0][RAPROC] Frame 79, slot 19 [Initiating RA proc]edure with preamble 5, energy 51.0 dB (I0 136, ...)...y 9 start symbol 0 freq index 0
[NR_PHY]   [gNB 0][RAPROC] Frame 79, slot 19 Initiating RA procedure with preamble 41, energy 51.0 dB (I0 180, thres 120), delay 10 start symbol 4 freq index 0
[NR_PHY]   [gNB 0][RAPROC] Frame 79, slot 19 Initiating RA procedure with preamble 0, energy 48.0 dB (I0 219, thres 120), delay 20 start symbol 8 freq index 0
[MAC]   UL_info[Frame 79, Slot 19] Calling initiate_ra_proc RACH:SFN/SLOT:79/19
[NR_MAC]   [gNB 0][RAPROC] CC_id 0 Frame 79 Activating Msg2 generation in frame 80, slot 7 using RA rnti 10b SSB, new rnti d8d4 index 0 RA index 0
[NR_MAC]   [gNB 0][RAPROC] FAILURE: CC_id 0 Frame 79 initiating RA procedure for preamble index 0
[MAC]   UL_info[Frame 80, Slot 0] Calling initiate_ra_proc RACH:SFN/SLOT:79/19
[NR_MAC]   [gNB 0][RAPROC] FAILURE: CC_id 0 Frame 79 initiating RA procedure for preamble index 0
[NR_MAC]   [gNB 0][RAPROC] CC_id 0 Frame 80, slotP 7: Generating RA-Msg2 DCI, rnti 0x10b, state 1, CoreSetType 2
[NR_MAC]   [RAPROC] Msg3 slot 17: current slot 7 Msg3 frame 80 k2 7 Msg3_tda_id 3
[NR_MAC]   [gNB 0][RAPROC] Frame 80, Subframe 7: rnti d8d4 RA state 2

[Wireshark - labeled "Trace Capture" / "Plaintext DNS Packets"]
Filter: ip.addr == 127.0.0.5 && dns || ngap || gtp
No. / Protocol / Info:
3856 GTP <T... Application Data
3857 GTP <T... 443 -> 37814 [RST] Seq=1009 Win=0 Len=0
3868 GTP <D... Standard query response 0x8467 AAAA b4E8Sm-dnsotls-ds.metric.gstatic.com AAAA 2607...
3869 GTP <Q... Protected Payload (KP0), DCID=ee7412ff33df9008
3872 GTP <T... 45302 -> 853 [ACK] Seq=373 Ack=5429 Win=78848 Len=0 TSval=2231640716 TSecr=386941239...
3885 GTP <Q... Protected Payload (KP0), DCID=5acfc1d1af97e6fb1c73a7d7c92efc6d7f9d4e8e
3886 GTP <D... Standard query 0xdbc7 AAAA K5j3NM-dnsotls-ds.metric.gstatic.com
3887 GTP <T... Application Data
3888 GTP <T... 33348 -> 853 [ACK] Seq=451 Ack=5535 Win=79872 Len=0 TSval=1335136228 TSecr=76137289...
3889 GTP <T... Application Data
3890 GTP <T... 33348 -> 853 [FIN, ACK] Seq=475 Ack=5535 Win=79872 Len=0 TSval=1335136234 TSecr=761...
3891 GTP <D... Standard query 0xa357 A youtubei.googleapis.com
3902 GTP <D... Standard query response 0xdbc7 AAAA K5j3NM-dnsotls-ds.metric.gstatic.com AAAA 2607...
3903 GTP <T... Application Data
3904 GTP <T... 853 -> 33348 [FIN, ACK] Seq=5535 Ack=475 Win=67840 Len=0 TSval=761373029 TSecr=1335...
3905 GTP <T... 853 -> 33348 [ACK] Seq=5536 Ack=476 Win=67840 Len=0 TSval=761373031 TSecr=133513623...
3906 GTP <D... Standard query response 0xa357 A youtubei.googleapis.com A 142.251.40.138 A 142.25...
3907 GTP <Q... Initial, DCID=aa5c42630c886a78, PKN: 1, CRYPTO, CRYPTO, PADDING, PING, CRYPTO, PAD...
[detail tabs: Frame (118 bytes) | Bitstring tvb (4 bytes) | Unaligned OCTET STRING]

[Phone - SM-G991B, 20:19, 100%]
< Airplane mode
Off
Turns off all network connections including calling, texting, internet access, Wi-Fi, and Bluetooth.
While Airplane mode is on, you can turn Wi-Fi and Bluetooth on again in Settings or the quick settings panel
```

## Slide 39

Demo: Phishing SMS Injection

5G AKA Bypass
DL NAS Transport
w/ phishing SMS

#BHUSA @BlackHatEvents

## Slide 40

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 85/100 on the text kept, 82/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
SM-G991B - o ®&
kai@kal: ~/Desktop/SGBaseChecker_Core 2 = = Oo x
: [sbi] : [5c89a00a-f471 =e KE]
c0f059] NF registered [Heartbeat: 1s] (. 7 Attac
: [upf] : PFCP[RSP] ile rminal
ssociated (../src/upf/pfcp-sm.c:207)
: [amt] : QNB-N2 accepted[127.0.0.1]:4775
2 in ng-path module (../src/amf/ngap-sctp.c:113)
[amf] : number of events in queue 1 (..
/src/amf/event.c:106)
: [amf] QNB-N2 accepted[127.0.0.1] in m
aster_sm module (. “sre [anf /ant- sm.c:720)
[amf] : [Added] Number of gNBs is now 1
(../src/amf/context.c:881)
: [amf] : number of events in queue 1 (..
[amf] : gNB-N2[127.0.0.1] max_num_of_os
treams : 2 (../src/amf/amf-sm.c:759)
[amt] : number of events in queue 1 (..
: [sctp] : sctp_senddata (../lib/sctp/ogs
[amf] : buffer:Hello
./src/amf/testsocket.c:248) Tap for weather info
Fl kai@kai: ~/Desktop/clean/openairinter... C = = ] x
got sync (ru_thread) A k
got sync (Li_stats_thread) ttac er
[HW] current pps at 2.000000, starting streaming at 3. 900000
[PHY] RU © rf device ready | f ip. 27.0.0.5 && dns || ngap || gtp
initializing tx write thread “
end of tx write thread
[UTIL] Creating thread trx_usrp_write_thread with affinity -1
and priority 97
[PHY] tx write thread ready
trx_usrp_write_thread started on cpu 1
sleep...
sleep...
sleep...
sleep...
sleep...
sleep...
sleep...
sleep...
sleep...
[PHY] tx_reorder_thread started
[NR_MAC] Frame.Slot 384.0
4475 NGAP NGSetupResponse
Galaxy Store Gallery Play Store Google
@ Os
[NR_MAC] Frame.Slot 512.0
[NR_MAC] Frame.Slot 640.0
[NR_MAC] Frame.Slot 768.0 »
Frame (118 bytes) | BICSCrINg CVD (4 Dytes) | UNaligned ULIE! STRING |>
```

## Slide 41

### Disclosure Status

- All uncovered issues are reported to the corresponding vendors

- 12 CVEs assigned and some vendor acknowledgements

   - CVE-2023-52341, -49928, -50804, -49927, -50803, -52343, -52533, -52534, -52342, -52344; CVE-2024-29152, -28818

- GSMA Mobile Security Research Acknowledgements (CVD-2023-0081)

#BHUSA @BlackHatEvents

## Slide 42

### Takeaways

- More security-focused tests are required before shipping the modem products.

- Black-box testing is an efficient method for detecting logical bugs as it requires only input and output analysis, making it more scalable and convenient compared to emulation or rehosting-based approaches.

- We open-sourced our tool 5GBaseChecker at: <u>github.com/SyNSecden/5GBaseChecker</u>

#BHUSA @BlackHatEvents

## Slide 43

### Meet Our Team

#BHUSA @BlackHatEvents

## Slide 44

# Thank You!

#BHUSA @BlackHatEvents
