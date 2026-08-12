---
title: "Kernel-Enforced DNS Exfiltration Security Framework Built for Cloud Environments to Stop Data Breaches via DNS at Scale"
speakers: ["Vedang Parasnis"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Vedang Parasnis_Kernel-Enforced DNS Exfiltration Security Framework Built for Cloud Environments to Stop Data Breaches via DNS at Scale.pdf"
pages: 30
sha256: "3b481c88457000cdeab57e230b5aeab5892043bf968023b8542cc61fa26db8e8"
text_chars: 14823
ocr_pages: 5
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:02:53Z"
---
# Kernel-Enforced DNS Exfiltration Security Framework Built for Cloud Environments to Stop Data Breaches via DNS at Scale

**Speakers:** Vedang Parasnis  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Vedang Parasnis_Kernel-Enforced DNS Exfiltration Security Framework Built for Cloud Environments to Stop Data Breaches via DNS at Scale.pdf` (30 pages)


## Slide 1

**From Packet to Process: Hunting and Disrupting DNS Tunnelling and C2 in Linux Kernel with eBPF and AI at Scale**

Speaker: Vedang Parasnis

#BHUSA @BlackHatEvents

## Slide 2

# $whoami

###### **Vedang Parasnis**

**Independent Researcher, Former Master’s Graduate @University Of Washington**

**Research Interests: Linux Kernel security, kernel hardening, eBPF, AI, cloud security**

#BHUSA @BlackHatEvents

## Slide 3

# Agenda

❑ **DNS a critical backdoor for enterprise networks**

- ❑ **DNS Exfiltration Attack Vectors**

- ❑ **DNS C2 Attack Infrastructure**

- ❑ **Existing Approaches and Challenges**

- ❑ **AI-Driven Kernel Enforced Endpoint Security**

❑ **Cloud Deployment Architecture at scale to combat DNS C2 Infrastructure**

- ❑ **Demo (Sliver DNS C2)**

- ❑ **Key Takeaways & Future Directions**

#BHUSA @BlackHatEvents

## Slide 4

They Breach and C2 Through DNS — Almost Every Time **Compromise Supply Chain:**

- APT29 (Cozy Bear) — SolarWinds

- **Breach Cloud & Hyperscalers:**

- UNC2452 (APT29)

- **Damage Critical Infrastructure:**

- Volt Typhoon

- **Harvest Credentials at Scale:**

- APT28 (GRU), Sea Turtle

- **Exploit Shared Offensive Tools:**

- APT41, FIN7

###### **85%+ of APT’s employ DNS for C2 and data breaches**

#BHUSA @BlackHatEvents

## Slide 5

###### DNS a Blind spot to compromise networks

- ➢ **Unencrypted by Default**

- ➢ **Logs Rarely Monitored**

- ➢ **Firewall Blindspot**

- ➢ **Stateless Protocol**

#BHUSA @BlackHatEvents

## Slide 6

#### **DNS Attack Vectors**

- ❑ **DNS C2** – Uses DNS to embed commands, data in queries and responses to maintain covert communication with remote C2 attacker infrastructure.

- ❑ **DNS Tunneling** – Encapsulates arbitrary data, other protocols within DNS packets to bypass network restrictions.

- ❑ **DNS Raw Exfiltration** – Leaks sensitive data files directly in DNS queries.

###### **Damage**

#BHUSA @BlackHatEvents

## Slide 7

#### **DNS C2 Adversaries Attack Process**

8

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
€Q
black hat
BRIEFINGS
DNS C2 Adversaries Attack Process
mk cw amslith.hack.com 1. Attacker registers a domain hack.com
eae r il. Attacker points hack.com NS to his
mae ——— ” tunnel server (C&C Server).
irewa
Attacker decodes
base64 encoded data
Bot periodcaly sends DNS Query
to pull new command from C&C server.
C&C Server
am9liHh.hack.com
—_———_——_—_>
a aey Z3 internet [oo —|
amginnnackcom Se i. — ee
7 = [se | iss —|
<q—_—
= Response Ei’ iia
Infected Host fod Recursive 3 Authoritative : Attacker
(Bot) a DNS Server : DNS Server :
E : forhack.com
—— User: joe ; H
Pass: xfet9S7 : ;
DNS Response 3
Contains newCommand Attacker encodes new command/data
in Resource Record (RR) into DNS Resource Record (RR).
e.g. CNAME record TXT, CNAME, NULL records can be useed.
Malware sends username and password data
encoded in base64 as hostname label
```

## Slide 8

#### **DNS: Not Just For Data Breaches Anymore. Next channel deliver zero-day attacks.**

**RCE & Shellcode** – Exploiting memory bugs, dropping payloads

**Script & File Attacks** – Scripted execution, file corruption **Side-Channel Process Abuse:** Processing Injection Hallowing **Persistent Backdoors:** Rootkits, ransomware stealth persistence.

**Network** Port reverse **Pivoting** : Forwarding, tunnels

9

#BHUSA @BlackHatEvents

## Slide 9

### Adversaries limited by DNS Protocol Specs

**DNS Question Record**

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
blackhat \; Se ae y jf
BRIEFINGS % A > “2 y A
Adversaries limited by DNS Protocol Specs
UDP Packet Size 512 bytes (default) Up to
4096 bytes (with EDNSO)
Max Domain Question 255
length
Max number of labels 127 labels
per query
Max Label Length 63
Max Response Size 512 bytes, except 4096 for DNS Question Record
EDNSO
DNS Header Size Limited by packet size
Query Section Size Limited by packet size
```

## Slide 10

###### What Makes DNS Query contain C2 commands or exfiltrated data

###### ❑ **High Entropy QNAME**

- ❑ **Long or Excessive Labels**

- ❑ **No Dictionary Tokens**

- ❑ **DGA-style Patterns / Ghost domains flood**

#BHUSA @BlackHatEvents

## Slide 11

Redirector Fleet for L3 shield C2 Botnet Army

# DNS C2 Attack Infrastructure

DGA {L7,L3}
Mutation
Powered
C2
Botnet Army

#BHUSA @BlackHatEvents

## Slide 12

##### DGA (L7) and IP (L3) Mutation

❑ **Evade Detection** – Generates thousands of reflectors, IP, domains to avoid static and policy blocklists.

❑ **Resilience** – If one domain or IP is taken down, others remain reachable.

❑ **No Hardcoded domains** – Domains are algorithmically created on both attacker and implant sides.

**Time-Based DGAs**

Date + SystemClock fkeo12jdn7z.com sk9qpdmx43a.com

**Seed-Based DGAs**

Seed + shared math functions bhack1.com bhack2.com

**Wordlist DGAs** Wordlist dictionary catsun.net reddog.org

**Character-Based or Randomized DGAs**

Pseudo random chars sdas232.bleed.io

#BHUSA @BlackHatEvents

## Slide 13

# Existing Approaches

- **Semi-Passive Analysis**

   - DNS Exfiltration Security as Middleware (DPI as middleware)

- **Passive Analysis**

   - Anomaly Detection (Traffic Timing / Volume)

   - Threat Signatures, Domain Reputation scoring

#BHUSA @BlackHatEvents

## Slide 14

###### DNS Traffic Anomaly Detection and Prevention Pipeline

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
€Q
blackhat Ay ~
BRIEFINGS ,
DNS Traffic Anomaly Detection and Prevention Pipeline ;
Blacklist Blacklist
romains Domains
in RPZ in RPZ
» AddDomain -<€
Stateless fis
Feature
Analysis DNS Server
Analyze
DNS stateless
features
Outliers
DNS Data ———————» DNS Data | IP + Destination --> Domain (Alerts)
Filter
Session
Collect \ Pe
Analyzed Analyze Stateful Classifier
Over Fixed ke SY y ‘ —y) Feature ——» (Machine
Features IP + Destination --> Domain
Window Session Analysis Learning
\ Model)
DNS IP + Destination --> Domain
Requests Session
sy ,
Time
```

## Slide 15

# Challenges with current approaches

- ❑ **Slow Detection, Slower Response: Stealthy mutable C2 Implants survive**

- ❑ **Less reactive to Advanced DNS C2 Infrastructure attacks**

- ❑ **Lack robust protection over Domain Generation Algorithms, IP mutation at scale**

- ❑ **Unwanted  latency for proxy-based DPI on benign traffic**

- ❑ **Dynamic Threat Patterns**

###### **Proposed Solution:**

- ✓ **Reactive Kernel EDR at Ring 0 — closest to the wire, at the implant source, beyond reach of userland evasion .**

#BHUSA @BlackHatEvents

## Slide 16

### eBPF

- Reprogram the Linux kernel in safe way.

- Runs BPF virtual machine inside kernel

- Custom BPF bytecode

- CPU architecture and Linux kernel version agnostic (BTF)

#BHUSA @BlackHatEvents

## Slide 17

## EDR Agent Linux Kernel eBPF Hooks

Kernel **Kernel Network Stack Attachments** Process scheduler

BPF Kprobes/
Tracepoints

**Kernel MAC (Access Control)  Attachments**

LSM (Linux Security Modules)

BPF LSM

BPF Cgroups/ Sockops DNS Sockets Process

BPF Netfilter

BPF TC

Core Kernel Subsystems

Egress DPI of DNS from SKB

Kernel Keyring, LSM Strong eBPF program integrity

BPF XDP

**Egress**

#BHUSA @BlackHatEvents

## Slide 18

### Kernel Enforced Endpoint Security for DNS

**Agent based Endpoint Security Continuous Security Enforcement Loop Userspace**

- eBPF Agent

- eBPF Agent Caches

- Quantized Deep Learning Model

- Events malicious metrics exporters

- **Linux Kernel**

- eBPF Ring Buffers

- Access Control Layer (LSM)

**Userspace**

DNS C2 Implant

KILL
Read
Update
each
Hunts parent
process for malicious  Malicious
child forks
Process
Status
Enforce Malicious
Process C2 Traffic  Process Redirect / Clone
filtering / DNS DPI  Telemetry
Suspicious
each
Packet C2 Traffic

DNS Query KILL

- Syscall Layer (Tracepoints)

- Network Stack (TC, Sockets)

Kernel Security Layer

**Linux Kernel**

#BHUSA @BlackHatEvents

## Slide 19

# eBPF-EDR Operation Modes

- ❑ Aggressive Enforcement: Reprogram Kernel to aggressively hunt, disrupt communication, and kill stealthiest DNS C2 implant process.

- ❑ Passive Enforcement: Reprogram Kernel to passively hunt and disrupt communication, correlating malicious packets to processes to kill the stealthiest DNS C2 implant.

#BHUSA @BlackHatEvents

## Slide 20

###### EDR Agent Active Process Security Enforcement

DNS C2 /  KILL C2  EDR eBPF components
Userspace Implants Infer Cache
Process DROP Track  Write-Through
Tunnelling Starts
attack  Agent DNS C2 Implant
eBPF  Attempts Caches
Packet:
DPI starts in Kernel
Packet scan-time
and Process info Endpoint ONNX
Kernel redirect  Agent DL Model
Malicious  Run inference
suspicious packet,  DNS C2
Benign:
Implant
Authorize
expose process  AF_PACKET
DNS packet resend in maps
AF_PACKET
telemetry
Netdev
Userspace  Netdev
eBPF
Model DL Inference Unsure Unsure redirect
TC egress
DPI
verify integrity
get resent
of sender
Userspace track
time Benign Benign
each process  scanned Malicious
Parse
malicious activity NIC Drop
DNS Questions
Linux Kernel RAW from SKB
Kill C2 Implant

Userspace
Model DL Inference
Userspace track
each process
malicious activity
Kill C2 Implant

#BHUSA @BlackHatEvents

## Slide 21

###### EDR Agent Passive Process Security Enforcement

Userspace KILL Implant Infer Cache EDR eBPF components
Get clone-
EXFIL  Write-Through
redirect Agent
Threshold
Telemetry  reached Caches DNS C2 Implant
for this
Process
Endpoint ONNX
Agent Run DL Model
Malicious
inference
DNS C2
Implant update process malicious
SNIFF (redirect  > threshold)
DNS packet
Netdev Netdev
clone
eBPF
Unsure redirect
TC egress
DPI
Verify process
blacklisted
benign
Malicious
NIC Drop Parse
Process DNS Questions
Linux Kernel Clone- RAW from SKB
redirect  2 3
#BHUSA @BlackHatEvents
telemetry

## Slide 22

EDR Agent Passive Process Security Enforcement State Diagram
Packet hits
DNS C2 / Tunnelling  eBPF TC Program
Starts
Suspicious packet
eBPF driven
DPI starts in Kernel
eBPF Kernel program  Userspace
hunts blacklisted  Kernel clones packet  eBPF Agent
expose process  Deep scan
malicious process Kernel Clone
tied to each packet Packet Expose telemetry
Attempts to
Userspace  Userspace EDR Agent
Once blacklisted runs model Inference
eBPF Kernel program  on cloned
starving the
packed
C2 implant process,  DNS Exfiltration
Found {C2,tunneling} Same Malicious
once blacklisted
Process exhibits
multiple
{C2,tunneling}
Userspace EDR Agent
Userspace EDR Agent
patterns
update
Track Each Process
Process as malicious in eBPF
Malicious Activity
maps
Userspace EDR
Kill C2 Implant
SIGKILL #BHUSA @BlackHatEvents
Agent Kill Implant

#BHUSA @BlackHatEvents

## Slide 23

###### DNN based DNS Data Obfuscation Detection (Features)

- ❑ Kernel Features

- ❑ Limits for DPI in Kernel

- ❑ Userspace Features

- ❑ Enhanced Lexical Features

#BHUSA @BlackHatEvents

## Slide 24

###### DNN fueled DNS Data Obfuscation Detection Model

Output Layer

**ONNX DNN Model Graph**

Input Layer

Hidden Layer 1

Hidden Layer 2

Hidden Layer 3

#BHUSA @BlackHatEvents

## Slide 25

###### Framework Deployment in Cloud to Disrupt Remote DNS C2 Infrastructure

**8a98176e380.exfil.com 11.0.100.121**

**8a98176e380.exfil.com 8a98176e380.exfil.com 10.0.100.121 11.0.100.121 8a98176e380.exfil.com 10.0.100.121** Data Plane safeguarded **8a98176e380.exfil.com** from exfil.com **10.0.100.121** C2 server (nonredirector’s IP **Export Kernel eBPF ring buffer events to SIEM**

**exfil.com 11.0.100.121**

#BHUSA @BlackHatEvents

## Slide 26

# Demo

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat ; E>.
BRIEFINGS . yy :
€
BU & wax |, Evs7ce GS WB eFsAcces &§ HM © & sKm Fri May 16 00:34
kernelDropped.go U $ exfil.sh M M Makefile M x c 1 tego M dns_tc.c M
ef classify(__sk_buff
build-controLler: classify( __sk_buff *skb){
LO CONLIULLe! Om MV CLeal pacnaye ea Cp Lal yet/Moue—ayent-LUnLI UL Lerma.u-anAroNUE. jal Wii, om uv CLeat } (eth-rhiprota
echo “Building the controller UNIX stream Inference NetworkPolicyHandlers" Spic-enexiidrin
cd controller/cmd & go build -o ../bin/main main.go
|| udp->dest
-PHONY: build-controller-cni-sec
build-controller-cni-sec:
echo “Building the controller UNIX stream Inference NetworkPolicyHandlers"
cd controller/cmd && go build -o ../bin/main main.go
(actions.parse_dns_header_size(Scursor,
xdns_payload = cursor.data + (
f ( *) dns_payload + 1 > cursor.data_end)
dns_header *dns = ( dns_header x) (
«PHONY: run-controller-cni-sec
run-controller-cni-sec:
echo “Running the controller UNIX stream Inference NetworkPolicyHandlers”
. af
pL | ne (actions.parse_dns_payload_transport_udp(&cur:
-PHONY: build-controller—image
build-controller-image:
echo “Building the controller docker image"
cd controller && docker build -t $(CONTROLLER_IMAGE_NAME) . nee pores POF oy, Reclare. ares poe iees lors reve
result_parse_dns_labels result = __parse.
«PHONY: run-controller-image S z —parse_
run-controller-image:
echo “Running the controller"
docker run --name controller -p $(CONTROLLER_PORT):9800 -d $(CONTROLLER_IMAGE_NAME) : $(CONTROLLER_IMAGE_TAG)
6 dns_payload_size = udp_payload_exclude_hea
(result.deep_scan_mirror) {
PHONY: stop-controller-image
stop-controller—image:
echo “Stopping the controller"
docker kill controller
«PHONY: run-controller
run-controller:
echo “Running the controller"
cd controller && java -jar bin/node-agent-controller—1.@-SNAPSHOT. jar
«PHONY: controller
controller:
132 out = skb->ifindex;
echo “Build and Run Controller"
n TERMINAL g
synarcs@synarcs:
1
SOSSHVISZESSASIY f° security’ O Qo0A6O15 > Java: Ready  Synarcs (1 month ago) Ln46,Col26 TabSize:4 UTF-8 LF Makefile
=
8
```

## Slide 27

# Response Speed with Precision

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
€Q
black hat
BRIEFINGS
Response Speed with Precision
Response Time Per Each DNS Exfiltration Attempt
450 T
400 F
350 F
300 F
250 F
Response Time (ps)
200 F
150
100 :
T T T T
T T
Response Time —+—
Mean = 316.233 ps = =
Attempt #
10
Score
Precision, Recall, and F1 Score vs. Threshold
0.998 4
0.996 4
0.994 +
0.992 4
0.990 +
—® F1 Score
= Precision
—# Recall
t T t T t T t T
0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9
Threshold
```

## Slide 28

# Next Steps

- ❑ **TLS Fingerprinting & Tunnel Detection** : eBPF-based TLS fingerprinting to detect, hunt, and block exfiltration over encrypted channels (TLS, WireGuard).

- ❑ **Process Correlation** : Kernel eBPF programs and EDR userspace agent correlate crossprotocol C2 and exfiltration attempts to originating processes for advanced intelligence.

- ❑ **Continuous model evolution** : Real-time drift detection, confidence-based updates, and GAN+LSTM models adapt to DNS obfuscation and kernel event patterns in eBPF maps.

- ❑ **DNS DDoS Guard** : eBPF-based endpoint defense against NXDOMAIN floods and DNS-C2 ghost domain flood.

#BHUSA @BlackHatEvents

## Slide 29

### Black Hat Sound Bytes

- ➢ **AI + eBPF matures EDR:** Dynamically detect and disrupt C2 implants in-kernel,

   - boosting EDR with adaptive, AI-driven kernel enforcements.

- ➢ **Kernel driven EDR fuels Cloud Firewalls** : Dynamic L3 filters at the endpoint and sync with cloud firewalls to disrupt DGA and evolving C2 infrastructure.

- ➢ **Deep OS Telemetry powers SIEM/SOAR** : Kernel-powered visibility via eBPF feeds rich behavioral signals into upstream SIEM and matures SOAR.

#BHUSA @BlackHatEvents

## Slide 30

Thank You Email: vedang.parasnis@outlook.com

Linkedin

WhitePaper

STOP Exploitation of DNS For C2 and Data Breaches

Codebase

#BHUSA @BlackHatEvents
