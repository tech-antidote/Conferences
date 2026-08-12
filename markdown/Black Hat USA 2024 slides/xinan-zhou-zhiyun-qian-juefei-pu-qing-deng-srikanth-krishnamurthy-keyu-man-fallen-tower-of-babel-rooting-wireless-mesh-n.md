---
title: "Fallen Tower of Babel Rooting Wireless Mesh Networks by Abusing Heterogeneous Control Protocols"
speakers: ["Xin'an Zhou", "Zhiyun Qian", "Juefei Pu", "Qing Deng", "Srikanth Krishnamurthy", "Keyu Man"]
conference: "Black Hat"
conference_full: "Black Hat USA 2024"
edition: "USA"
year: 2024
source_pdf: "Black Hat USA 2024 slides/Xin'an Zhou & Zhiyun Qian & Juefei Pu & Qing Deng & Srikanth Krishnamurthy & Keyu Man_Fallen Tower of Babel Rooting Wireless Mesh Networks by Abusing Heterogeneous Control Protocols.pdf"
pages: 43
sha256: "89194c5c379bc4ecea3289c220f608d520615bcb5d001b6b6931bf3192503819"
text_chars: 11507
ocr_pages: 4
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:40:06Z"
---
# Fallen Tower of Babel Rooting Wireless Mesh Networks by Abusing Heterogeneous Control Protocols

**Speakers:** Xin'an Zhou, Zhiyun Qian, Juefei Pu, Qing Deng, Srikanth Krishnamurthy, Keyu Man  
**Conference:** Black Hat USA 2024  
**Source:** `Black Hat USA 2024 slides/Xin'an Zhou & Zhiyun Qian & Juefei Pu & Qing Deng & Srikanth Krishnamurthy & Keyu Man_Fallen Tower of Babel Rooting Wireless Mesh Networks by Abusing Heterogeneous Control Protocols.pdf` (43 pages)

## Slide 1

Fallen Tower of Babel: Rooting Wireless Mesh Networks by Abusing Heterogeneous Control Protocols

Speakers: Xin’an Zhou and Zhiyun Qian

Contributors: Juefei Pu, Qing Deng, Srikanth Krishnamurthy, Keyu Man 8/7/2024

#BHUSA @BlackHatEvents

## Slide 2

# Team/Contributors at

Xin’an Zhou

## Zhiyun Qian

Qing Deng

Juefei Pu

Keyu Man

Srikanth Krishnamurthy

#BHUSA @BlackHatEvents

## Slide 3

# Agenda

- Background on home wireless mesh networks

- Two types of security flaws

- Exploitation

- Defenses

#BHUSA @BlackHatEvents

## Slide 4

# Background: Home Wireless Mesh Networks

1. An emerging type of Wi-Fi network.

2. Single gateway node + multiple extender nodes

Images: TP-Link

#BHUSA @BlackHatEvents

## Slide 5

Wireless Mesh Networks are increasingly popular!

Netgear Orbi

TP-Link Deco

Linksys

ASUS

Images: Netgear, TP-Link, Linksys, ASUS #BHUSA @BlackHatEvents

## Slide 6

# Wireless Mesh Networks are increasingly popular!

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisa hat
USA 2024
Wireless Mesh Networks
are increasingly popular!
Wireless Mesh Network Market Size, By Region, 2019 - 2032
(USD Billion)
2019 2020 2021 2022 2023 2024 2025 2026 2027 2028 2029 2030 2031 2032
@ North America Europe @ Asia Pacific Latin America @ Middle East & Africa
Source: Polaris Market Research Analysis
```

## Slide 7

# Extending Connectivity in Home Networks with WMNs

- Inter-access-point backhaul links carry both user traffic and configurations.

Fronthaul Links Backhaul Links

#BHUSA @BlackHatEvents

## Slide 8

# A Motivating Question: How to Change Wi-Fi Passwords?

- Network Access Policy Synchronization (NAPS) helps access points Synchronize the Wi-Fi password Switch the SSID

Update firewall rules, DNS settings, Web UI password…

- A novel attack surface!

#BHUSA @BlackHatEvents

## Slide 9

# How is NAPS implemented?

- Channels: over backhaul links

- Protocols: ad-hoc crypto protocols and Wi-Fi EasyMesh

- We call them Network Access Policy Synchronization (NAPS) protocols

#BHUSA @BlackHatEvents

## Slide 10

# Threat Model

- A wireless client (attacker) has a fronthaul link credential.

- Can use ARP poisoning to perform MITM attacks.

- Goal 1: To obtain root shell to access points

- Goal 2: To steal WPA2/3 passphrases of backhaul/fronthaul links

Images: Dan Boneh

#BHUSA @BlackHatEvents

## Slide 11

# Overall Results

Vendor NAPS Protocol Attack Results SOAP over TLS Root shell AiMesh protocol Root shell TCP over Root shell Dropbear SSH TLS-SRP Root shell MQTT with TLS Wi-Fi password leakage WebSocket with TLS Wi-Fi password leakage EasyMesh Wi-Fi password leakage

Logos are from vendor websites #BHUSA @BlackHatEvents

## Slide 12

# Security Flaws

1. Type I: Missing cross-layer trust (among mesh nodes)

2. Type II: Cross-layer trust compromise

#BHUSA @BlackHatEvents

## Slide 13

# Security Flaws

1. **Type I: Missing cross-layer trust (among mesh nodes)**

2. Type II: Cross-layer trust compromise

#BHUSA @BlackHatEvents

## Slide 14

# Flaw Type I: Missing Cross-layer Trust

1. Trust at link layer is well-established.

2. No trust anchors for NAPS layer (not bootstrapped properly)

3. Thus, attackers can manipulate NAPS protocols.

#BHUSA @BlackHatEvents

## Slide 15

Case Study: Netgear Orbi’s SOAP-over-TLS Vulnerability: TLS but self-signed certificates

TLS

#BHUSA @BlackHatEvents

## Slide 16

# Attack #1: MITM against SOAP-over-TLS

Gateway (TLS Client)

TLS

Extender
(TLS Server)

Got the backhaul
passphrase!

#BHUSA @BlackHatEvents

## Slide 17

# Case Study: Netgear Orbi’s SOAP-over-TLS

Vulnerability:

Password required for invoking SOAP commands, but fully predictable

```
Predictable_str=
“NETGEAR_Orbi_<MACGateway>_<MACExtender>_password”
```

MD5( Predictable_str )

#BHUSA @BlackHatEvents

## Slide 18

# Attack #2: Exploiting SOAP-over-TLS (Step 1)

Attacker acting
as gateway Authenticating
(TLS Client)
Calculate MD5
hash

Extender (TLS Server)

Send MD5 over TLS
Authentication
Successful

#BHUSA @BlackHatEvents

## Slide 19

# Attack #2: Exploiting SOAP-over-TLS (Step 2)

Attacker acting
as gateway Authenticating
(TLS Client)
Compute hash of
malicious pwd
Send hash over TLS
Succeed in
Updating
Password

Extender (TLS Server)

#BHUSA @BlackHatEvents

## Slide 20

# Attack #2: Exploiting SOAP-over-TLS (Step 3)

Attacker acting
as gateway Authenticating
(TLS Client)
Run a telnet unlocking
script w/ pwd
Send unlocking payload

Extender (TLS Server)

telnet activated on
port 23
Root Shell

Connect to <extender>:23

#BHUSA @BlackHatEvents

## Slide 21

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Activities ©) Terminal ~
cea
ez@ez-virtual-machine:
‘“@BDOBGEG
sil
Jul 28 15:02
ez@ez-virtual-machine: ~/share/Netgear_Orbi_RBS760_hack
```

## Slide 22

# Case Study: Wyze’s MQTT with TLS

Vulnerability:

- The key         for MQTT(S) is shared among ALL Wyze devices Attack:

- Unpack the firmware, jackpot!

- Attacker wiretaps control data

MQTT with TLS

Got front/backhaul passphrase!

#BHUSA @BlackHatEvents

## Slide 23

# Case Study: AmpliFi’s WebSocket with TLS

1. Self-signed certificates for inter-AP TLS connections (again)

2. Fronthaul/backhaul passphrases were wrapped in (unencrypted) MessagePack formats

#BHUSA @BlackHatEvents

## Slide 24

# Example: Wi-Fi EasyMesh standard

- The opt-in standard for NAPS

- No authentication at all

- Uses 2 messages to perform opportunistic encryption in one round-trip time (1 RTT).

#BHUSA @BlackHatEvents

## Slide 25

# PoC: Wi-Fi EasyMesh

+ =
Pri
=
+

: Key to encrypt
: Wi-Fi passphrase
+ =
: Public key of
Pri
: Public key of
Unwrap  to get

#BHUSA @BlackHatEvents

## Slide 26

# Overall Results

Vendor NAPS Protocol Attack Results SOAP over TLS Root shell AiMesh protocol Root shell TCP over Root shell Dropbear SSH TLS-SRP Root shell MQTT with TLS Wi-Fi password leakage WebSocket with TLS Wi-Fi password leakage EasyMesh Wi-Fi password leakage

Logos are from vendor websites #BHUSA @BlackHatEvents

## Slide 27

# Security Flaws

1. Type I: Missing cross-layer trust (among mesh nodes)

2. **Type II: Cross-layer trust compromise**

#BHUSA @BlackHatEvents

## Slide 28

# Flaw Type II: Cross-layer Trust Compromise

- NAPS endpoints are reachable by attackers No logical isolation like VLAN

- Crypto failures and software vulnerabilities are still there

- One layer fails, all layers fail

#BHUSA @BlackHatEvents

## Slide 29

# Case Study: ASUS AiMesh Protocol

## 1. An encrypted protocol on top of TCP

2. “group_id”           is the credential

#BHUSA @BlackHatEvents

## Slide 30

# Case Study: ASUS AiMesh Protocol

1. An encrypted protocol on top of TCP

2. “group_id”           is the credential

Nc ~~Ns~~ = SHA256(      , Nc, Ns) ~~Policy~~

#BHUSA @BlackHatEvents

## Slide 31

# ASUS AiMesh protocol is vulnerable to key leakage

“group_id” leaked in the 802.11 layer, breaking security.

Insecure, however
Nc
“group_id”
Ns
“guarantees” security later.
= SHA256(      , Nc, Ns)
Policy

#BHUSA @BlackHatEvents

## Slide 32

# Leaked group_id

1. “group_id”        is broadcasted at the 802.11 layer

   - Just sniff for the hashed “group_id” over-the-air

   - Offline brute force to crack the “group_id”

#BHUSA @BlackHatEvents

## Slide 33

# Leaked group_id

Type-Length-Value (TLV) structure. Hash of “group_id” is stored at type 0x3

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisa hat
USA 202
Leaked group_id
9 0.081180 ASUSTekCOMPU_c8: Broadcast 802.11 493
10 0.086920 Wist ronNeweb_86: Espressif_a2:90:6c 802.11 116
11 0.092163 TPLink_33:13:34 IPv4mcast_7f:ff:fa 802.11 518
12 0.096363 TPLink_33:13:34 IPv4mcast_7f: ff: fa 802.11 518
13 0.100893 TPLink_33:13:34 IPv6mcast_Oc 802.11 516
14 0.104691 TPLink_33:13:34 IPv6mcast_Oc 802.11 516
15 0.112439 TPLink_33:13:34 IPv6mcast_Oc 802.11 525
Version: 0x10 10 02 71 09 80 04 da a2
Wifi Protected Setup State: Configured (x@2) la c8 3e 31 04 42 la c8 Type-Length-Val ue
Vendor Extension 82 84 8b 96 24 30 48 6c
Tag: Vendor Specific: ASUSTek COMPUTER INC. 00 07 06 55 53 20 01 ob
Te Number: Vendor Specific (221) ee We Ue te 3 st) Be (TLV) stru ctu re.
OUI: £8:32:e4 (ASUSTek COMPUTER INC. ff 00 02 00 02 00 00 00
Vendor Specific OUI Type: 1 @@ 00 00 00 00 00 3d 16
HE Vendor Specific Data: 01010102010d03148ce982744849b948ae707 f2258004056663bc91407! 00 00 00 00 00 00 00 00
Tag: Vendor Specific: Epigram, Inc. a ee ee ee a a ce ee 6 +
Tag Number: Vendor Specific (221) ff 00 00 fa ff 00 20 co Hash Oo IS
Vendor Specific OUI Type: 4 Od fc ff ff Ge 26 00 00 sto red at type 0x3
802.11n (Pre) Type: Unknown (4) 62 2 8 ae x bs 0 0
802.11n (Pre) Unknown Data: 18bf@cb179810f faff0000faf f0020c0050002000000 150 1 20 dd 47 f8 32 e4 Q1
Tag: Vendor Specific: Broadcom 0160 e9 82 74 48 49 b9 48 ae
Tag Number: Vendor Specific (221) @170 3b c9 14 Q7 04 00 00 00
Vendor Specific OUI Type: 2 CO 05 00 02 00 00 00 dd vias
Vendor Specific Data: 0201009c0000 0 00 dd 18 00 50 f2 02 1 01 20 20 03 a4 00 00 tPee cease
Tag: Vendor Specific: Microsoft Corp.: WMM/WME: Parameter Element 27 a4 0@ 0@ 42 43 5e 00 62 32 2f 00 Gc 02 7f 20 BC*: b2/:1:::
```

## Slide 34

# ASUS AiMesh protocol is vulnerable to key leakage

2. The attacker can then tamper with (encrypted) AiMesh connections.

- To exploit `cfg_server` ’s SSH management key installation functionality to gain root access.

#BHUSA @BlackHatEvents

## Slide 35

# TP-Link Deco: Weak SSH key and command injections

- 1.Channel: Dropbear SSH with 512-bit RSA key length.

- Brute force an RSA private key in 4 days with a single PC in 2024.

- Software: GGNFS/MSIEVE

#BHUSA @BlackHatEvents

## Slide 36

# TP-Link Deco: Weak SSH key and command injections

2. Backhaul passphrases are derived from that RSA key pair.

- Irrevocable access to the network through backhaul links!

- 3. To exploit command injections in the `tmpsvr` binary

#BHUSA @BlackHatEvents

## Slide 37

# Linksys: TLS-SRP Isn't the Silver Bullet

1. A zero-knowledge (ZK) protocol encrypting all control data.

### **cryptographic verifiers**

≈ public key

### **_SRP passwords_**

- ≈ private key

A machine-in-the-middle truly knows nothing about transmitted data.

#BHUSA @BlackHatEvents

## Slide 38

# Linksys: TLS-SRP Isn't the Silver Bullet

2. Pre-authentication command injection.

- An attacker can taint the _clientID/srpuser_ field

- Steal **_stored SRP passwords_**

#BHUSA @BlackHatEvents

## Slide 39

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisa hat
USA 2024
| openssl ||
```

## Slide 40

# Mitigation Status (Disclosed > 8 months ago)

Vendor Attack Results Patched?
Root shell
Root shell
Root shell
Root shell
Wi-Fi password leakage
Wi-Fi password leakage
Wi-Fi password leakage

Logos are from vendor websites #BHUSA @BlackHatEvents

## Slide 41

# Defenses

# Users

# Network Engineers

- Go home and update the firmware!

- Set a new Wi-Fi password.

- Check your wireless client list for any anomalies.

- Rotate compromised keys to new values unknown to previous attackers.

- Add some network isolations.

- Check out our paper for details.

#BHUSA @BlackHatEvents

## Slide 42

# Black Hat Sound Bytes

1. Wireless security is coming back

2. Home WMN control protocols are novel attack surfaces

3. Wireless standards and vendors can do more with security

#BHUSA @BlackHatEvents

## Slide 43

# Thank you!

Github Link: <u>https://github.com/seclab-ucr/CCS24Mesh</u> Research Paper: Untangling the Knot: Breaking Access Control in Home Wireless Mesh Networks, CCS ’24 <u>https://www.cs.ucr.edu/~zhiyunq/pub/ccs24_wireless_mesh.pdf</u>

**Feel free to talk to us offline in the hallway!** Contacts: <u>xinan.zhou@email.ucr.edu</u> X (Twitter): @zhouxinan <u>zhiyunq@cs.ucr.edu</u> X (Twitter): @pkqzy888

#BHUSA @BlackHatEvents
