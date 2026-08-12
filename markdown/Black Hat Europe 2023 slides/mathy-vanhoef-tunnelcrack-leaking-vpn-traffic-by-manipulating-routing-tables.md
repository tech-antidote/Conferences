---
title: "TunnelCrack Leaking VPN Traffic by Manipulating Routing Tables"
speakers: ["Mathy Vanhoef"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2023"
edition: "Europe"
year: 2023
source_pdf: "Black Hat Europe 2023 slides/Mathy Vanhoef_TunnelCrack Leaking VPN Traffic by Manipulating Routing Tables.pdf"
pages: 32
sha256: "034d6e6bd1e49add303b04e8805b99c09e272ac447b30592989a4b3526342ddd"
text_chars: 7902
ocr_pages: 5
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:12:39Z"
---
# TunnelCrack Leaking VPN Traffic by Manipulating Routing Tables

**Speakers:** Mathy Vanhoef  
**Conference:** Black Hat Europe 2023  
**Source:** `Black Hat Europe 2023 slides/Mathy Vanhoef_TunnelCrack Leaking VPN Traffic by Manipulating Routing Tables.pdf` (32 pages)

## Slide 1

## **Bypassing Tunnels: Leaking VPN Client Traffic by Abusing Routing Tables**

Nian Xue, Yashaswi Malla, Zihang Xia, Christina Pöpper, and **<u>Mathy Vanhoef</u>**

**NYUAD**

#BHEU @BlackHatEvents

## Slide 2

### Contributions

We make VPN clients leak traffic

- › By **manipulating the client’s routing table**

- › Attacks are independent of the crypto protocol

- Tested 67+ VPN clients

- › >248 experiments → **66% attack success**

- › Every VPN is vulnerable on at least one OS

   - → **Widespread design issues!**

2

## Slide 3

Usage of VPNs: watch videos from other country

3

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Usage of VPNs: watch videos from other country
Sa. Dov BE
ee Pee ee FO eal
```

## Slide 4

### Usage of VPNs: protect your traffic

› Identify website visits: IP address, plaintext DNS, SNI,… › Attack TLS: no cert check, sslstrip, academic attacks,…

4

## Slide 5

### Usage of VPNs: protect your traffic

› Defend against untrusted Wi-Fi & compromised core routers › Research goal: can we trick the client into leaking packets? Yes, by manipulating the client’s routing table → **~66% vulnerable!** Attacks are independent of the crypto protocol

5

## Slide 6

### Background: VPN client routing table

- `$ ip route                    # Detailed ouput`

- 1 `default via 10.0.0.1 dev tun0` 2 `192.168.1.0/24 dev eth0 proto kernel scope link src 192.168.1.2 metric 100`

- 3 `2.2.2.2 via 192.168.1.2 dev eth0`

6

## Slide 7

### Background: VPN client routing table

`$ ip route      # Simplified ouput` 1 `default via tun0`

1. By default, send packets over tun0 = over the VPN tunnel

7

## Slide 8

### Background: VPN client routing table

`$ ip route      # Simplified ouput` 1 `default via tun0` 2 `192.168.1.0/24 via eth0`

1. By default, send packets over tun0 = over the VPN tunnel **2. LocalNet exception** : local network is directly accessible

8

## Slide 9

### Background: VPN client routing table

`$ ip route      # Simplified ouput` 1 `default via tun0` 2 `192.168.1.0/24 via eth0` 3 `2.2.2.2 via eth0`

1. By default, send packets over tun0 = over the VPN tunnel **2. LocalNet exception** : local network is directly accessible **3. ServerIP exception** : avoid re-encryption of VPN packets

9

## Slide 10

We assume secure DNS behavior

```
$ cat/etc/resolv.conf
nameserver6.6.6.6
```

Can’t trust the network’s DNS server

10

## Slide 11

We assume secure DNS behavior

```
$ cat/etc/resolv.conf
nameserver2.2.2.3
```

Can’t trust the network’s DNS server

1. Once connected, VPN client sets a **trusted DNS server**

2. DNS is sent **through the VPN tunnel**

+ we assume other routing-based attacks are prevented

11

## Slide 12

### LocalNet attack

Target.com 2.2.2.2 1.2.3.4

12

## Slide 13

LocalNet attack
Target.com 2.2.2.2
Local network is 1.2.3.0/24
1.2.3.4
Create VPN tunnel with 2.2.2.2
Set trusted DNS server
default via tun0
1.2.3.0/24 via eth0

### LocalNet attack

13

## Slide 14

### LocalNet attack

Target.com 2.2.2.2 1.2.3.4 `default via tun0 1.2.3.0/24 via eth0`

14

## Slide 15

LocalNet attack
default via tun0
Target.com 2.2.2.2
1.2.3.0/24 via eth0
1.2.3.4
Visit random.com
Visit target.com
Send to 1.2.3.4
Intercept traffic!

### LocalNet attack

**Leak**

15

## Slide 16

### LocalNet attack: 195 experiments

16

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ARTIFACT ARTIFACT ARTIFACT
EVALUATED EVALUATED EVALUATED
LocalNet attack: 195 experiments =| gz.) | ee] fense:.
AVAILABLE REPRODUCED
VPN Provider Class OS Version Number LAN Setting | Result
Default LAN Access
Free Windows Windows 10 Pro No | N/A x
Free Windows Windows I1 Pro No | N/A x
ar Free macOS Ventura 13.0.1 No | N/A x
OS Built-in VPN Free iOS iOS 16.1.1 No | N/A x
Free Android Android 8.1.0 No | N/A
Free Android Android 12 No | N/A
Free Windows 2022.10.106.0 No | N/A
Free Linux 2022.9.591 No |N/A
LLL Free macOS 2022.10.107.0 No | N/A A
Free iOS 6.16 No | N/A x
Free Android 6.17 No | N/A
16
```

## Slide 17

### LocalNet attack: 195 experiments

17

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ARTIFACT ARTIFACT ARTIFACT
LocalNet attack: 195 experiments — |e.) Jes] | eae.
AVAILABLE REPRODUCED
Tammie
z
Paid Windows 12.37.0 Yes | Yes A
Paid Linux 3.36 No | N/A A
ExpressVPN Paid macOS 11.12.0 Yes | Yes A
Paid iOS 11.70.0 Yes | Yes x
Paid Android 10.63.2 Yes | Yes
VPN Proxy Master Free iOS 2.1.5 No|N/A #
for iPhone
17
```

## Slide 18

### LocalNet attack: summary

18

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
LocalNet attack: summary
® Vulnerable Blocks non-RFC1918 local traffic Secure
Android
Linux
Windows
macOS
iOS
50
18
```

## Slide 19

### DEMO

19

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
mathy@zbook-mathy:~/research/netsec/vpnproject-main/vpn_tester - 8 x
File Edit View Search Terminal
Help
@ @ © G Documents |_)MathyGZ" ) @ EH vpn teste... The Wires... SimpleScr.. 416 7% @ 22:17
19
```

## Slide 20

### Selected special cases

Some clients block traffic to local network › Problem when local network uses public IPs › Traffic to these public IPs gets blocked!

VPN Proxy Master for iPhone (and others) › DNS server returns private-use IP addresses › VPN server forwards traffic to real IP address

20

## Slide 21

### The iOS case

Prevent attacks by setting `includeAllNetworks=True` › And `excludeLocalNetworks=False` on iOS ≥ 14.2

- › Causes reliability issues, vendors hesitant to enable this

- Result is that **iOS remains less secure** › Context: VPNs on iOS were already known to leak traffic in certain scenarios.

› E.g., OS traffic may leak, leaks when switching networks,…

21

## Slide 22

We were warned in the past…

- Andrew Ayer: Hardening OpenVPN for DEF CON (2015) › Guide for OpenVPN on Linux

- › Essentially suggested the risk of LocalNet attacks!

- Unclear how widespread this issue (already) was at the time › VPN clients were not systematically tested → vendors were not warned, so clients never were not audited either

- › Using domain names would still enable ServerIP attacks…

22

## Slide 23

ServerIP attack
Target.com 2.2.2.2
DNS request for vpn.com
1.2.3.4
Spoof DNS reply: 1.2.3.4
Create VPN tunnel with 1.2.3.4
Redirect to 2.2.2.2
Set trusted DNS server
default via tun0
1.2.3.4 via eth0
Connect

23

## Slide 24

### ServerIP attack

Target.com 2.2.2.2 1.2.3.4

```
default via tun0
1.2.3.4 via eth0
```

24

## Slide 25

ServerIP attack
default via tun0
Target.com 2.2.2.2
1.2.3.4 via eth0
1.2.3.4
Visit random.com
Visit target.com
Leak Send to 1.2.3.4
Intercept traffic!

Leak

25

## Slide 26

### ServerIP attack: 53 experiments

› Many **built-in clients** are affected (Windows, macOS, Linux) › Legacy built-in VPN on **Android 11 and below** was affected › Most iOS/Android apps not vulnerable

Impact: can leak traffic to single IP address

› Can target the DNS server set by the VPN client ☺

› Or repeat the attack for different IPs…

26

## Slide 27

### DEMO

27

## Slide 28

### Defenses

**LocalNet attack** : disable local network access when it’s using public IP addresses.

- › Or allow local network access when using 192.168.* or alike

**ServerIP Attack** : send all traffic over VPN, except packets generated by VPN process

- › On Linux, you can use fwmark (policy-based routing)

- › Or quick fix: use secure DNS to get VPN server’s IP address

28

## Slide 29

### Disclosure

- › Reported to CERT/CC on May 10, 2023

- › Reported to selected vendors that had a security contact: Some had no e-mail contact, only a bug bounty program

- In report say we **deviate from T&Cs** and reserve **right to disclose**

29

## Slide 30

### Disclosure: special cases

#### Dubai-based ClarioVPN

› Initially: _“MitM attacks are out of scope”_ › Later: _“Clario isn’t interested in participating in this multi-party disclosure on VPN security”_

Ivanti Pulse Secure

- › Provided a test server! But at first didn’t work

- › Kept asking for time-consuming recordings

› Seems like they didn’t try our PoC script…

30

## Slide 31

### Conclusion

- › Two wide-spread flaws in VPN clients › In hindsight easy attack, but **~66% vulnerable**

- › Bad integration of protocols into real systems

- › Defense: more carefully configure routing tables › OS should have API to create VPN tunnels

31

## Slide 32

# Questions?

› Two wide-spread flaws in VPN clients › In hindsight easy attack, but **~66% vulnerable**

- › Bad integration of protocols into real systems

› Defense: more carefully configure routing tables › OS should have API to create VPN tunnels

32
