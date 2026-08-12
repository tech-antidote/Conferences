---
title: "Sweet Dreams Abusing Sleep Mode to Break Wi Fi Encryption and Disrupt WPA23 Networks"
speakers: ["Vanhoef"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2023"
edition: "ASIA"
year: 2023
source_pdf: "Black Hat Asia 2023 slides/AS-23-Vanhoef-Sweet-Dreams-Abusing-Sleep-Mode-to-Break-Wi-Fi-Encryption-and-Disrupt-WPA23-Networks.pdf"
pages: 43
sha256: "de5f0aa189beb93ee92dc27c742c893c073e951999f80f115840735fa6fe0726"
text_chars: 11133
ocr_pages: 22
has_ocr: true
redacted_secrets: 0
companion_files: ["AS-23-Vanhoef-Sweet-Dreams-Abusing-Sleep-Mode-to-Break-Wi-Fi-Encryption-and-Disrupt-WPA23-Networks_tools.txt"]
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:55:55Z"
---
# Sweet Dreams Abusing Sleep Mode to Break Wi Fi Encryption and Disrupt WPA23 Networks

**Speakers:** Vanhoef  
**Conference:** Black Hat ASIA 2023  
**Source:** `Black Hat Asia 2023 slides/AS-23-Vanhoef-Sweet-Dreams-Abusing-Sleep-Mode-to-Break-Wi-Fi-Encryption-and-Disrupt-WPA23-Networks.pdf` (43 pages)

## Slide 1

# **_Sweet Dreams:_ Abusing Sleep Mode to Break Wi-Fi Encryption & Disrupt WPA2/3 Networks**

<u>Mathy Vanhoef, Domien Schepers,</u> and Aanjhan Ranganathan

#BHASIA @BlackHatEvents

## Slide 2

### History of Wi-Fi

› WEP (1999): quickly broken<sup>[FMS01]</sup>

› WPA1/2 (~2003) Offline password brute-force **KRACK** & **Kraken**<sup>[VP17,VP18]</sup>

- › WPA3 (2018):

**Dragonblood** side-channels<sup>[VR20]</sup>

2

## Slide 3

### Background: Kr00k implementation flaw

AP (vulnerable)
Attacker Hardware Daemon
Buffer
Disassociate
Remove keys
Leak buffered frames  in plaintext
Question:  how are “security contexts” managed ?

3

## Slide 4

New attack 1: leaking frames

## Slide 5

### Attack 1: leaking frames

5

## Slide 6

### Attack 1: leaking frames

6

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Attack 1: leaking frames AP (Vulnerable)
Client || Attacker '| Kernel |} Daemon |:
---- | lilies Connection ------7-7- aii |
```

## Slide 7

### Attack 1: leaking frames

7

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Attack 1: leaking frames AP (Vulnerable)
Chent
Attacker '! Kernel |} Daemon |!
Power-Save (Sleep=True)
Buffer
```

## Slide 8

### Attack 1: leaking frames

## **Novelty 1: controlled buffering**

8

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Attack 1: leaking frames AP (Vulnerable)
Power-Save (Sleep=True)
Buffer
Novelty 1: controlled buffering
Client || Attacker '! Kernel |} Daemon |
St. D-
```

## Slide 9

### Attack 1: leaking frames

9

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Attack 1: leaking frames AP (Vulnerable)
Client || Attacker '| Kernel |} Daemon |:
Power-Save (Sleep=True)
Buffer]
Auth. / Association Request }-
| Remove Pairwise Key
Auth. / Association Response
```

## Slide 10

### Attack 1: leaking frames

## **Novelty 2: connect to remove client’s keys**

10

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Attack 1: leaking frames AP (Vulnerable)
Client || Attacker '| Kernel
Power-Save (Sleep=True) .
Novelty 2: connect to remove client’s keys
Auth. / Association Request
‘Remove Pa
Auth. / Association Response
irwise Key
-/7
‘- Stage Q--
10
```

## Slide 11

### Attack 1: leaking frames

11

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Attack 1: leaking frames
Auth. / Association Request
[ Remove Pa
irwise Key
Auth. / Association Response
Wake-Up
Ke
Dequeue without Key
Leak Queued Frames
|
\
-Stage @)-- ‘Stage Q@--
11
```

## Slide 12

### Attack 1: leaking frames

Novelty 3: frames leaked under
undefined security context

12

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Attack 1: leaking frames
Auth. / Association Request
Remove Pairwise Key
Auth. / Association Response
.
Novelty 3: frames leaked under
undefined security context
| Leak Queued Frames |
- Stage Q--
‘Stage @)-- °
12
```

## Slide 13

### Undefined security context: FreeBSD example

How the frame is leaked depends on kernel version & driver:

**Version driver (vendor) Leakage** 13.0 run (Ralink) Plaintext 13.1 run (Ralink) WEP with all-zero key 13.1 rum (Ralink) CCMP with group key 13.1 rtwn (Realtek) CCMP with group key

› Malicious insiders know the group key! › Linux, NetBSD, open Atheros firmware also affected

13

## Slide 14

### Root cause

**Standard isn’t explicit** on how to manage buffered frames › Should drop buffered frames when refreshing/deleting keys

Frames are buffered in plaintext

› Alternative: encrypt frames before buffering them (like TLS)

14

## Slide 15

New attack 2: Network Disruptions

## Slide 16

### Background: DoS attacks

Well-known DoS attacks:

› Deauthentication: spoof “disconnect” frames

› Association: spoof “I want to connect” frames Both remove connection state of the victim

Defense:

› **<u>M</u>** anagement **<u>F</u>** rame **<u>P</u>** rotection ( **MFP** = 802.11w) › This defense is required in WPA3

16

## Slide 17

### Bypassing MFP (802.11w)

17

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Bypassing
MFP (802.11w)
Client
AP (Vulnerable)
Attacker ‘| Kernel
-
-- Connection with Wi-Fi MFP- - -
17
```

## Slide 18

### Bypassing MFP (802.11w)

18

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Bypassing MFP (802.11w) AP (Vulnerable)
Client || Attacker ! Kernel || Daemon
K----7 -- Connection with Wi-Fi MFP- - -|}------
Association Request (Sleep=True)
18
```

## Slide 19

### Bypassing MFP (802.11w)

19

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Bypassing MFP (802.11w) AP (Vulnerable)
Client || Attacker '! Kernel || Daemon |:
K----7 -- Connection with Wi-Fi MFP- - -|-------
Association Request (Sleep=True)
Association Response (Rejected)
```

## Slide 20

### Bypassing MFP (802.11w)

20

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Bypassing
MFP (802.11w) AP (Vulnerable)
Client
Attacker '| Kernel || Daemon |:
-- Connection with Wi-Fi MFP-- -|-------
Association Request (Sleep=True)
Association Response (Rejected)
A Query
| Buffer
20
```

## Slide 21

Bypassing MFP (802.11w)

**User space: “Hey client, are you still connected?”**

21

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Bypassing MFP (802.11w) AP (Vulnerable)
Client || Attacker | Kernel |} Daemon !
K-----7 -- Connection with Wi-Fi MFP- - -|-------
Association -
User space: “Hey client,
Association are you still connected?”
A Query|
| Buffer
21
```

## Slide 22

Bypassing MFP (802.11w)

**User space: “Hey client, are you still connected?”**

**Kernel: “Client is asleep, buffer the question”**

22

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
AP (Vulnerable)
Client || Attacker | Kernel || Daemon |
K-----7 -- Connection with Wi-Fi MFP- - -|-------
Association -
User space: “Hey client,
Association are you still connected?”
ISA Query|
|
‘Buffer
Kernel: “Client is asleep,
buffer the question”
22
```

## Slide 23

Bypassing MFP (802.11w)

**User space: “Client didn’t reply, disconnect it”**

23

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Bypassing MFP (802.11w) AP (Vulnerable)
Client || Attacker '| Kernel || Daemon |:
K----7 -- Connection with Wi-Fi MFP- - -|-------
Association Request (Sleep=True)
Associatic
User space: “Client didn’t
reply, disconnect it”
|
Buffer | Timeout
23
```

## Slide 24

### Other Attacks & Defenses

Can also **force buffering of Fine Timing Measurements** frames › Used to measure distance to AP and localize device › For details, see our paper “Framing Frames: Bypassing Wi-Fi Encryption by Manipulating Transmit Queues” (USENIX Security)

Defenses:

- › Never buffer “are you still connected?” frames

- › Authenticate the sleep bit in the header of Wi-Fi frames

- › **Standard should be updated** with one of these defenses

24

## Slide 25

New attack 3: Bypassing client isolation

## Slide 26

### What is client isolation?

Blocks traffic between clients: › Clients **cannot attack each other** › ARP spoofing is not possible

All clients have unique encryption keys: › Prevents “Hole 196” attack (Black Hat ’10)

→ **Defends against malicious insiders**

26

## Slide 27

Attack 2: bypassing Wi-Fi client isolation

Target is networks that use **client isolation** . Examples: › Company network with malicious/compromised clients › Public hotspots that require authentication

- → Adversary can connect to the network, but can’t attack others

27

## Slide 28

### Client isolation bypass

28

## Slide 29

### Client isolation bypass

Internet

Router

29

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Internet
Client isolation bypass AP (Vulnerable)
Client || Attacker
K----4--------- Connection - ----------7-7- Router
Request
29
```

## Slide 30

### Client isolation bypass

Internet

#### Router

## **E.g., DNS or HTTP request**

30

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Client isolation bypass
AP (Vulnerable)
Client || Attacker
Kota Connection -----------~---
E.g., DNS or HTTP request
30
```

## Slide 31

### Client isolation bypass

Internet

#### Router

31

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Client isolation bypass
AP (Vulnerable)
Client || Attacker
K----4--------- Connection --------7-7-7-777
Request J
Spoof Client MAC Address |
K iia Connect with the AP -------- |
31
```

## Slide 32

### Client isolation bypass

#### Internet

#### Router

**New key is associated with the victim’s MAC address**

32

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Client isolation bypass
AP (Vulnerable) <i
Client || Attacker _—
k----4--------- Connection ------------7-7-
Request J t
Spoof Client MAC Address |
K-------- Connect with the AP - - ------
Generate New Key
New key is associated with
the victim’s MAC address
32
```

## Slide 33

### Client isolation bypass

#### Internet

#### Router

Router forwards reply to victim’s MAC address

33

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Client isolation bypass
——P
AP (Vulnerable)
Client || Attacker
k----4--------- Connection -----------7-7-7-
Request J
Spoof Client MAC Address |
K--- 77H Connect with the AP - -- ---~-- >
[ Generate New Key
Router forwards
reply to victim’s
MAC address
33
```

## Slide 34

### Client isolation bypass

#### Internet

#### Router

Router forwards reply to victim’s MAC address

34

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Client isolation bypass
<P
AP (Vulnerable)
Client || Attacker
k----+--------- Connection -----------7-7-7-
Request J
Spoof Client MAC Address |
K------7- Connect with the AP - ------- >
[ Generate New Key
[Encrypt Response with New Key
Router forwards
reply to victim’s
MAC address
Response
34
```

## Slide 35

### Client isolation bypass

Internet

#### Router

**The attacker receives the DNS response!**

Router forwards reply to victim’s MAC address

35

## Slide 36

### Client isolation bypass

Internet

#### Router

**Note: must connect before response arrives**

Router forwards reply to victim’s MAC address

36

## Slide 37

### Fixing client isolation

**Disallow recently-used MAC address** unless:

- › Certain amount of time has passed (incomplete defense)

- › We’re sure it’s the same user as before (complete defense)

- Based on 802.1X identity or cached keys (not always available)

Currently few vendors implemented a defense or mitigation

- › Client isolation is flawed but still useful

- › Alternative: use VLANs to isolate groups

37

## Slide 38

### Tool to test devices: MacStealer

**Sanity checks Vulnerability tests Does the network use client isolation?**

38

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Tool to test devices: MacStealer
Command Short description
Sanity checks
./macstealer.py wlan@ --ping =
—— Sanity checks
./macstealer.py wlan® --ping --flip
Vulnerability tests
./macstealer.py wlan@ IMA
Vulnerability tests
./macstealer.py wlan@ --other-bss
Client isolation: Ethernet layer
./macstealer.py wlan@ --c2c wlan1 Does the network use
./macstealer.py wlan@ --c2c-eth wlanl client isolation?
38
```

## Slide 39

### MacStealer demo

- → Ubuiqiti is one of the few vendors that implemented a mitigation!

39

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
MacStealer demo
Open + @
README.md client. cont
1# Don't change this line, other MacStealer won't work
2ctrl_interface=wpaspy ctrl
rj
4network={
5 # Don't change this line, other MacStealer won't work
6 id_str="victim"
Tj
8 # Network to test: fill in properties of the network to test
9 ssid="ubiquiti"
10 key_mgmt=WPA- PSK
11 psk="abcdefgh"| :
14network={
15 # Don't change this line, other MacStealer won't work
16 id_str="attacker"
18 # Network to test: you can copy this from the previous network block
19 ssid="ubiquiti"
20 key_mgmt=WPA - PSK
21 psk="abcdefgh"
Plain Text Tab Width: 4 Ln 11,Col19 INS
> Ubuidgiti is one of the few vendors that implemented a mitigation!
39
```

## Slide 40

### Experiments

All tested professional & home APs were vulnerable

→ **Design flaw** in Wi-Fi client isolation! → Useful test for auditors

<u>github.com/vanhoefm/macstealer</u>

40

## Slide 41

### Conclusion

Standard is vague on how to manage buffered frames › Can **leak frames** under different security context

- › Important to **model/define transmit queues**

Can partially **bypass client isolation**

- › All devices vulnerable → **design flaw**

- › Hard to fully prevent

41

## Slide 42

### Backup slide: root cause

Client identity not authenticated across the network stack: › Wi-Fi security: 802.1X identity (username) Not bound to

Not bound to each other

› Packet routing: IP/MAC addresses

- → Wi-Fi attacker can spoof client’s identity on other layers

Other observation: client isolation was “bolted on” by vendors

› Not part of IEEE 802.11 standard → less studied

42

## Slide 43

Backup slide: fast security context override Technique to quickly reconnect. Experiments:

- › Minimum reconnect time: ~12 ms

- › Average UDP response time:<sup>[Verizon]</sup> Transatlantic connections: ~70 ms Connections within Europe: ~13 ms

- › TCP responses are retransmitted → trivial to intercept

43

[Verizon] Verizon IP latency statistics

## Companion resources

### `AS-23-Vanhoef-Sweet-Dreams-Abusing-Sleep-Mode-to-Break-Wi-Fi-Encryption-and-Disrupt-WPA23-Networks_tools.txt`

```text
https://github.com/domienschepers/wifi-framing
```
