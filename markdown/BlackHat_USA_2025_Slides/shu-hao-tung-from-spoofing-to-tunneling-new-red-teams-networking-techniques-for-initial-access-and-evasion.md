---
title: "From Spoofing to Tunneling New Red Team's Networking Techniques for Initial Access and Evasion"
speakers: ["Shu-Hao Tung"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Shu-Hao Tung_From Spoofing to Tunneling New Red Team's Networking Techniques for Initial Access and Evasion.pdf"
pages: 125
sha256: "a8a871acb7e1955752f6396d9710526b17b5e614222ff6ae6a4aaeb74f92008e"
text_chars: 45399
ocr_pages: 29
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:01:45Z"
---
# From Spoofing to Tunneling New Red Team's Networking Techniques for Initial Access and Evasion

**Speakers:** Shu-Hao Tung  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Shu-Hao Tung_From Spoofing to Tunneling New Red Team's Networking Techniques for Initial Access and Evasion.pdf` (125 pages)

## Slide 1

**From Spoofing to Tunneling: New Red Team's Networking Techniques for Initial Access and Evasion**

Speaker : Shu-Hao, Tung (123ojp)

1

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat
BRIEFINGS
AUGUST 6-7, 2025
MANDALAY BAY / LAS VEGAS
From Spoofing to Tunneling:
New Red Team's Networking Techniques for
Initial Access and Evasion
Speaker : Shu-Hao, Tung (123o0jp)
#BHUSA @BlackHatEvents
```

## Slide 2

### Just Another Normal Day of IT

- Seeing my Intranet LDAP server log

P.S. All addresses are example addresses.

2

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pif hat \ mr. Re
BRIEFINGS
Just Another Normal Day of ie
¢ Seeing my Intranet LDAP server log
Apr 17 23:12:20 from IP=192.168.1.102 BIND dn="cn=frank,dc=example,dc=com" RESULT err=@ text=Success
2 P.S. All addresses are example addresses.
```

## Slide 3

### Just Another Normal Day of IT

- Seeing my Intranet LDAP server log • Seeing my Intranet LDAP server log

P.S. All addresses are example addresses.

3

## Slide 4

### Just Another Normal Day of IT

- Seeing my Intranet LDAP server log • Seeing my Intranet LDAP server log

P.S. All addresses are example addresses.

4

## Slide 5

### Just Another Normal Day of IT

- Seeing my Intranet LDAP server log • Seeing my Intranet LDAP server log

Why a public IP is brute forcing me? How? It’s an intranet server with no DNAT

P.S. All addresses are example addresses.

5

## Slide 6

Just Another Normal Day of IT

- Seeing my Intranet LDAP server log • Seeing my Intranet LDAP server log

Okay I banned 9.9.9.9

6

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisekhat
BRIEFINGS
Just Another Normal Day of IT
Apr
Apr
Apr
Apr
Apr
Seeing my Intranet LDAP server log
17 23:
17 23:
17 23:
17 23:
17 23:
12:20 from
13:45 from
14:10 from
14:11 from
14:12 from
IP=192.168.1.102 BIND dn=""cn=frank,dc=example,dc=com" RESULT err=@ text=Success
IP=192.168.1.103 BIND dn="'cn=bob,dc=example,dc=com" RESULT err=@ text=Success
IP=9.9.9.9 BIND dn="cn=administrator,dc=example,dc=com" RESULT err=49 text=Invalid credentials
IP=9.9.9.9 BIND dn="cn=administrator,dc=example,dc=com" RESULT err=49 text=Invalid credentials
IP=9.9.9.9 BIND dn="cn=administrator,dc=example,dc=com" RESULT err=49 text=Invalid credentials
Okay | banned 9.9.9.9
```

## Slide 7

### Just Another Normal Day of IT

- Seeing my Intranet LDAP server log

Oh no how!?

P.S. All addresses are example addresses.

7

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pifchat
BRIEFINGS
Just Another Normal Day of IT
¢ Seeing my Intranet LDAP server log
17 23:12:20 IP=192.168
17 23:13:45 IP=192.168.
17 23:14:10 IP=9.9.9.9
17 23:14:11 IP=9.9.9.9
from
from
from
from
BIND dn="cn=administrator,dc=example, dc=com"
BIND dn="cn=administrator,dc=example,dc=com"
BIND dn="cn=administrator,dc=example,dc=com"
BIND dn="cn=administrator,dc=example,dc=com"
BIND dn="cn=administrator,dc=example,dc=com"
BIND dn="cn=administrator,dc=example,dc=com"
IP=7.7.7.7
IP=7.7.7.7
IP=7.7.7.7
17 23:21:47 from
RESULT
RESULT
RESULT
RESULT
RESULT
RESULT
err=49
err=49
err=49
err=49
err=49
err=49
.1.102 BIND dn=""cn=frank,dc=example,dc=com" RESULT err=0 text=Success
1.103 BIND dn=""cn=bob,dc=example,dc=com" RESULT err=@ text=Success
text=Invalid
text=Invalid
text=Invalid
text=Invalid
text=Invalid
text=Invalid
credentials
credentials
credentials
credentials
credentials
credentials
7 P.S. All addresses are example addresses.
```

## Slide 8

### Whoami

- ^  ^

- • **Shu Hao** Tung (123ojp)

8

• From Taiwan

• Threat Researcher (Red Team)

- Graduate of NTHU

• Previous President of HackerSir 123ojp shu-hao-tung o123ojp

## Slide 9

### Agenda

- Introduction & Background

- Red Teaming Techniques with IP Spoofing in Intranet

- • Two Methods to Replace Initial Foothold

- • BOOM! 💥 Initial Access

- Nightmare of VxLAN – Tunnel Hijacking

- Routing Protocols Running on Buggy VxLAN Leading to IP Hijacking Leading to Domain Compromises

- Conclusions & Takeaways

- Q&A

9

## Slide 10

## **Spoofing Source IP**

10

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bi
-
ack hat
BRIEFINGS
AUGUST 6-7, 2025
MANDALAY BAY / LAS VEGAS
Spoofing Source IP
```

## Slide 11

### Spoofing Source IP in Public

We all know that packet spoofing is still possible on public networks.

11

Public
Internet
2.2.2.2
1.1.1.1
ip.src ip.dst
3.3.3.3 1.1.1.1
Spoofing
DNS Requests
3.3.3.3
P.S. All addresses are example addresses.

## Slide 12

### Spoofing Source IP in Public

We all know that packet spoofing is still possible on public networks.

12

Public
Internet
2.2.2.2
1.1.1.1
ip.src ip.dst
1.1.1.1 3.3.3.3
DNS Response
3.3.3.3
P.S. All addresses are example addresses.

## Slide 13

### Spoofing Source IP in Public

Typical DDoS DNS amplification attack

Public
Internet
2.2.2.2
1.1.1.1
ip.src ip.dst
1.1.1.1 3.3.3.3
DNS Response
3.3.3.3
P.S. All addresses are example addresses.

13

## Slide 14

**How IT Blocks Computers from Having Public Network Access**

14

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blackhat
BRIEFINGS
AUGUST 6-7, 2025
MANDALAY BAY / LAS VEGAS
How IT Blocks Computers from Having
Public Network Access
```

## Slide 15

### Best Practice

ip.src ip.dst
192.168.1.2 1.1.1.1
DNS requests
Public  2.2.2.2
Internet
192.168.1.1
Drop all out 192.168.1.2
1.1.1.1
Example public address
15 Example private address

15

## Slide 16

### Best Practice

ip.src ip.dst
192.168.1.2 1.1.1.1
DNS requests
Public  2.2.2.2
Internet
192.168.1.1
Drop all out 192.168.1.2
1.1.1.1
Example public address
16 Example private address

16

## Slide 17

### Best Practice

Public  2.2.2.2
Internet
192.168.1.1
Drop all out 192.168.1.2
1.1.1.1

17

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pifeK hat
BRIEFINGS
Best Practice
ee
tooo 192.168.1.1
Drop all out 192.168.1.2
L
1.1.1.1
```

## Slide 18

### But… sometimes they just disable SNAT

ip.src ip.dst
192.168.1.2 1.1.1.1
DNS requests
Public  2.2.2.2
Internet
192.168.1.1
192.168.1.2
1.1.1.1
Example public address
18 Example private address

18

## Slide 19

### But… sometimes they just disable SNAT

ip.src ip.dst
192.168.1.2 1.1.1.1
DNS requests
Public  2.2.2.2
Internet
192.168.1.1
192.168.1.2
1.1.1.1
Example public address
19 Example private address

19

## Slide 20

### But… sometimes they just disable SNAT

**ip.src ip.dst** 192.168.1.2 1.1.1.1 DNS requests Public 2.2.2.2 Internet 192.168.1.1 192.168.1.2 1.1.1.1 Example public address Example private address

20

## Slide 21

### But… sometimes they just disable SNAT

ip.src ip.dst
1.1.1.1 192.168.1.2
DNS response
Public  2.2.2.2 😭 No response
Internet
192.168.1.1
192.168.1.2
1.1.1.1
No Route to Host
 drop
Example public address
21 Example private address

21

## Slide 22

But… sometimes they just disable SNAT

ip.src ip.dst
1.1.1.1 192.168.1.2
DNS response
Public  2.2.2.2 😭 No response
Internet
192.168.1.1
192.168.1.2
1.1.1.1
No Route to Host
 drop
Example public address
22 Example private address

## Slide 23

## **Spoofing Source IP in intranet**

23

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bi
-
ack hat
BRIEFINGS
AUGUST 6-7, 2025
MANDALAY BAY / LAS VEGAS
Spoofing Source IP in intranet
```

## Slide 24

### IP spoofing in intranet

- Create a tunnel between compromised device

- Send the network packets used for Lateral movement which ip.src is public IP

Public  2.2.2.2
Internet
192.168.1.1
192.168.1.2
9.9.9.9
attacker
ip.src ip.dst
192.168.1.3
9.9.9.9 192.168.1.2 hacked
DNS requests Intranet
tunnel

Example public address

24

## Slide 25

### IP spoofing in intranet

- The device gets the packet and forward to the router

Public  2.2.2.2
Internet
192.168.1.1
192.168.1.2
9.9.9.9
attacker
192.168.1.3
hacked
ip.src ip.dst Intranet
9.9.9.9 192.168.1.2
DNS requests
Example public address
tunnel

25

## Slide 26

### IP spoofing in intranet

ip.src ip.dst
The router forward the packet to the second victim 9.9.9.9 192.168.1.2
DNS requests
Public  2.2.2.2
Internet
192.168.1.1
192.168.1.2
9.9.9.9
attacker
192.168.1.3
hacked
Intranet
tunnel

- The router forward the packet to the second victim

Example public address

26

## Slide 27

### IP spoofing in intranet

•
The victim get the packet and respond to the attacker
ip.src ip.dst
through public internet
192.168.1.2 9.9.9.9
DNS response
Public  2.2.2.2
Internet
192.168.1.1
192.168.1.2
9.9.9.9
attacker
192.168.1.3
hacked
Intranet
Example public address
tunnel

27

## Slide 28

### IP spoofing in intranet

- Ghost in intranet

- No one knows where the packet came from in layer 3 logger

Public  2.2.2.2
Internet
192.168.1.1
192.168.1.2
9.9.9.9
attacker
ip.src ip.dst 192.168.1.3
hacked
192.168.1.2 9.9.9.9
Intranet
DNS response
28 Example public address
tunnel

## Slide 29

### Why IR hard

- Normal Lateral movement

compromised compromised **Public web service Internal Database Windows LDAP** Attacker IP Victim IP Attacker IP Victim IP Attacker IP Victim IP 9.9.9.9 10.0.0.4 10.0.0.4 10.0.0.5 10.0.0.5 10.0.0.6 🚨 EDR Alert Bad Login Password Attempts spraying

🚨

P.S. All addresses are example addresses.

29

## Slide 30

### Why IR hard

- Normal Lateral movement

###### compromised

**public web service** Attacker IP Victim IP 9.9.9.9 10.0.0.4

###### compromised

**Internal Database Windows LDAP** Attacker IP Victim IP Attacker IP Victim IP 10.0.0.4 10.0.0.5 10.0.0.5 10.0.0.6 Password spraying 10.1.1.5 is spraying password

🚨

###### 🚨 IR Team

View Event Log
IR teams

30

## Slide 31

### Why IR hard

###### • Normal Lateral movement

###### compromised

public web service Internal Database
Attacker IP Victim IP Attacker IP Victim IP
9.9.9.9 10.0.0.4 10.0.0.4 10.0.0.5
Shutdown

Windows LDAP
Attacker IP Victim IP
10.0.0.5 10.0.0.6

🚨 IR Team

🚨

IR teams

The logs said the attacker is from 10.0.0.4

31

## Slide 32

### Why IR hard

- Normal Lateral movement

public web service Internal Database Windows LDAP
Attacker IP Victim IP Attacker IP Victim IP Attacker IP Victim IP
9.9.9.9 10.0.0.4 10.0.0.4 10.0.0.5 10.0.0.5 10.0.0.6
Shutdown
Shutdown

🚨 IR Team

🚨

IR teams

😭 Full Chain Dead

32

## Slide 33

### Why IR hard

• Lateral movement with IP Spoofing

###### compromised

compromised compromised **public web service Internal Database Windows LDAP** Attacker IP Victim IP Attacker IP Victim IP Attacker IP Victim IP 9.9.9.9 10.0.0.4 9.9.9.10 10.0.0.5 9.9.9.11 10.0.0.6 🚨 EDR Alert Spoof Spoof Bad Login Password Attempts spraying

🚨

33

## Slide 34

### Why IR hard

- Lateral movement with IP Spoofing

###### compromised

###### compromised

**public web service Internal Database** Attacker IP Victim IP Attacker IP Victim IP 9.9.9.9 10.0.0.4 9.9.9.10 10.0.0.5

**Windows LDAP** Attacker IP Victim IP 9.9.9.11 10.0.0.6 🚨 IR Team

🚨

IR teams

Why is a public IP attacking our DC?
Okay, lets ban 9.9.9.11

34

## Slide 35

### Why IR hard

- Lateral movement with IP Spoofing

**public web service** Attacker IP Victim IP 9.9.9.9 10.0.0.4

Internal Database
Attacker IP Victim IP
9.9.9.10 10.0.0.5
Survive

**Windows LDAP** Attacker IP Victim IP 9.9.9.12 10.0.0.6

Change Spoofing IP Continue Attack

P.S. All addresses are example addresses.

35

## Slide 36

### Why IR hard

- The packet always has IP: 192.168.1.2 and 9.9.9.9

   - The C&C (tunnel) server IP could be different from 9.9.9.9 (7.7.7.7)

   - No one knows the packet comes from 192.168.1.3 in the Layer 3 network logger.

Example public address
Example private address
spraying packet L3 view Example attacker address
9.9.9.9 9.9.9.9 192.168.1.2
Attacker Public  2.2.2.2
Evil payloads
Receiver Internet
192.168.1.1
192.168.1.2
domain controller
Tunnel
7.7.7.7 192.168.1.3
Attacker’s C&C server hacked
36 Intranet
tunnel

## Slide 37

### Why IR hard

- The packet always has IP: 192.168.1.2 and 9.9.9.9

   - If 9.9.9.9 is banned, the attacker can simply switch to another public IP.

– IR team need to check every router for Layer 2 port logs to identify the hacked machine
– Example public address
The source MAC address can also be forged at the first hop!
Example private address
Example attacker address
9.9.9.9
Attacker Public  2.2.2.2
Receiver Internet
192.168.1.1
192.168.1.2
domain controller
Tunnel
7.7.7.7 192.168.1.3
Tunnel packet L3 View hacked
Attacker’s Intranet
7.7.7.7 192.168.1.3
C&C server
37
HTTP Traffic
tunnel

## Slide 38

###### What if ISP filtered packet that Source IP is private IP

- If H.323 Passthrough is enabled

- We can send H.323 packet to trigger DNAT

- And NAT router will DNAT the 192.168.1.3: 445 on 2.2.2.2: 445

- Similar for NAT Slipstreaming v2.0 by @SamyKamkar

- • Tools: <u>https://github.com/123ojp/Simple-H.323-NAT-Traversal</u>

Victim‘s public address Next target address Compromised address Example attacker address

Public  Router public  2.2.2.2 SNAT Router private192.168.1.1 )
Internet
192.168.1.3
9.9.9.9 Next Target
Attack
38 192.168.1.2
hacked Intranet
C&C connection

H.232
ip.src ip.dst
192.168.1.2 9.9.9.9
Port.src Port.dst
any 1720
Payload with  192.168.1.3: 445

## Slide 39

Simple H.323 NAT Traversal Demo

Webserver: 192.168.83.241 Hacked server: 192.168.83.35 Attacker Public: 154.12.177.142 Victim Public: 114.32.17.155

39

## Slide 40

What if ISP Filtered Packet that Source IP is a Private IP

- Or, we can sent a spoofed TCP SYN from 192.168.1.2 with the source IP set to 192.168.1.3

- • And the router will then trigger an SNAT from 192.168.1.3: 445 to 2.2.2.2: 445

- When a connection comes from 9.9.9.9: 55555, it will be redirected to 192.168.1.3: 445

- Found by Chumy Tsai (@Jimmy01240397)

- Tools: <u>https://github.com/123ojp/Spoof-TCP-Tigger-NAT-Traversal</u>

Router public
2.2.2.2
Public  SNAT Router private
192.168.1.1
Internet
192.168.1.3
9.9.9.9 Next Target
Attack
40 192.168.1.2
Intranet
hacked

Victim‘s public address Next target address Compromised address Example attacker address **Fake TCP Send from 192.168.1.2** ip.src ip.dst 192.168.1.3 9.9.9.9 Port.src Port.dst The service Same with attacker want attacker (445) (55555)

TCP new

## Slide 41

Ｓpoofed TCP SYN NAT Traversal Demo

Webserver: 192.168.83.35 Hacked server: 192.168.83.241 Attacker Public: 160.25.104.131 Victim Public: 114.32.17.155

41

## Slide 42

#### Can we replace this tunnel with official VPN?

- Use compromised account and get access to VPN

- Yes, in some cases

Public
Internet
192.168.1.1
192.168.1.2
Attacker
Connect VPN
With
VPN server
Compromised 2.2.2.2
Intranet
account
192.168.44.4
Official VPN

42

## Slide 43

#### Common VPN allow IP spoofing

- Commercial SSL VPN

   - (CYBERSEC 2025 - Ta-Lun Yen - VPN Gremlin: User Impersonation Attack in Multiple SSL VPNs)

Cisco CVE-2023-20275 Fortinet CVE-2023-45586 Palo Alto Networks CVE-2024-3388 SonicWall CVE-2023-41715

- Opensource VPN, depends on Config

   - Wireguard, OpenVPN …

43

## Slide 44

### Where‘s the initial access

- So, the problem is the orange tunnel

- Do we have a chance to do this without a foothold in the intranet?

- Can we use any existing tunnel?

Public  2.2.2.2
Internet
192.168.1.1
192.168.1.2
9.9.9.9
attacker
192.168.1.3
hacked
Intranet
tunnel

44

## Slide 45

### Yes!

- IX everyone is in same L2 – Set 10.0.0.0/8 next-hop to router which company you want to attack

- Use existing tunnel

   - GRE, IPIP, SIT

- But again, a good firewall configuration could cause it to fail.

45

## Slide 46

### Static route private subnet in internet exchange

103.158.187.0/24
Victim company’s router
Ｉnternet eXchange
ens19:  103.158.187.119 ens20:  1.1.1.2
Attacker router
ens19  :103.158.187.34 1.1.1.0/30
ens18:  160.25.104.0 1.1.1.1
Attacker public IP
Company Intranet:
ens19:  103.158.187.76
192.168.1.1
Other company’s
Static route  router
192.168.1.0/24  via
103.157.187.34
8.8.8.8/26
src  160.25.104.0
192.168.1.2
Intranet
ens19:  8.8.8.8
Example public address
Example private address
Special Thanks
46 Example attacker address STUIX
Example IX address

## Slide 47

**Use existing tunnel - Spoof IP.src in GRE tunnel**

47

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bl
ack hat SS
BRIEFINGS Sse TG
AUGUST 6-7, 2025
MANDALAY BAY / LAS VEGAS
Use existing tunnel -
Spoof IP.src in GRE tunnel
```

## Slide 48

### What is GRE tunnel

Public
• Layer 3 tunnel
Internet
• Stateless
• No encryption GRE tunnel
1.1.1.1
2.2.2.2
• Common 169.254.0.1 169.254.0.2
192.168.1.1
192.168.2.1
• Setup easy
– Protocol (GRE)
192.168.1.2
– Public IP & GRE interface IP 192.168.2.2
– Route table (next-hop) Site A Site B

48

## Slide 49

### Who use GRE tunnel now

- Cloudflare Magic Transit – And its customers 😁

   - Can choose IPsec or GRE (IPsec is safe)

- AWS Transit Gateway

   - 😭

   - – But used in internal networking only

Cloudflare Magic Transit dashboard with GRE tunnel

- APT Groups

   - Salt Typhoon

- A lot of companies

– 49

🤫

Image from: https://blog.kingsmill.io/2022/07/setting-up-cloudflare-magic-transit/

## Slide 50

### How GRE Tunnel Works?

- Sender

   - If packet next-hop to GRE tunnel

   - Pack the packet into Encapsulated Packet

- Receiver

   - Unpack GRE packet

   - Throw out the packet by route table

- Stateless, No encryption = SPOOF IT

**Original Packet** IP Header Payload

###### **Encapsulated Packet**

Outer IP Header GRE Header

IP Header Payload

50

## Slide 51

### Normal GRE

P.S. All addresses are example addresses.
Public
Internet
2.2.2.2
1.1.1.1
192.168.1.1 192.168.2.1
192.168.1.2 192.168.2.2
ip.src ip.dst
192.168.1.2 192.168.2.2
Site A Site B
Data

51

## Slide 52

### Normal GRE

P.S. All addresses are example addresses.
Public
Internet
192.168.1.1 2.2.2.2
1.1.1.1
192.168.2.1
ip.src ip.dst
1.1.1.1 2.2.2.2
Original Packet  Original Packet
ip.src ip.dst
192.168.1.2 192.168.1.2 192.168.2.2 192.168.2.2
Data
Site A Site B

52

## Slide 53

### Normal GRE

P.S. All addresses are example addresses.
Public
Internet
2.2.2.2
1.1.1.1
192.168.1.1 192.168.2.1
ip.src ip.dst
192.168.1.2 192.168.2.2
Data
192.168.1.2 192.168.2.2
Site A Site B

53

## Slide 54

### Normal GRE

P.S. All addresses are example addresses.

Public
Internet
2.2.2.2
1.1.1.1
192.168.1.1 192.168.2.1
192.168.1.2 192.168.2.2
ip.src ip.dst
192.168.2.2 192.168.1.2
Site A Site B
Data

54

## Slide 55

### Normal GRE

P.S. All addresses are example addresses.
Public
Internet
2.2.2.2
1.1.1.1
192.168.1.1 192.168.2.1
ip.src ip.dst
2.2.2.2 1.1.1.1
Original Packet  Original Packet
ip.src ip.dst
192.168.2.2 192.168.1.2
192.168.1.2 192.168.2.2
Data
Site A Site B

55

## Slide 56

### Normal GRE

P.S. All addresses are example addresses.
Public
Internet
2.2.2.2
1.1.1.1
192.168.1.1 192.168.2.1
ip.src ip.dst
192.168.2.2 192.168.1.2
Data
192.168.1.2 192.168.2.2
Site A Site B

56

## Slide 57

How 2 Find GRE Tunnel （by OSINT）

- Find by netflow – intitle: Akvorado

– Filter “GRE”

- OSINT techniques

57

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisekhat @
BRIEFINGS ‘
How 2 Find GRE Tunnel (by OSINT)
€ ca GSS ED 185.130.47.7:8081/visualize/N4igRgigJhBOCMBJALhA9gOwlYBsQC4AzXAZ3gBoQYBbel JeggbRAGVZEBBKKWESgBES yHnxABdSnSgEQAJgAM8g‘
E 1 d b tfl Alevorado fetiome Gy oustzs na Doouentoy
y 13%, L2%, 2% %> % Refresh.
Stacked areas S
. .
| tit | e ° \ kvo ra d O Wsidirectional Previous period 15000
Last 6 hours h. ce 120.00)
oa
.
arch 0.00M
foe Eanes =
Search $ 80.249.212.156 80.249.213.14 15.67Mbps
2024021318 60.240.212156 126.00bps
7.166.13617 199231236381 86,0005
220132387 19513047225 20.0005
1433244161 199291236157 20.0005
12211720831 19513047210 20.0005
114352718:159 199291236316 20.000es
eserves soem scene en femes
```

## Slide 58

### How to Fake GRE packet

• Attacker

Real IP
Real IP
Real IP
160.25.104.198 Internet 160.25.104.199
Internet 2.2.2.2
Encapsulated Packet Original Packet Original Packet
Outer IP Header GRE Header IP Header Payload IP Header Payload IP Header Payload
1.1.1.1 160.25.104.198
160.25.104.198
to to 160.25.104.198
to
160.25.104.199 2.2.2.2 to
58 2.2.2.2 2.2.2.2

## Slide 59

How 2 Scan GRE via Fake ip.src
Attacker
3.3.3.3
Public
Internet
1.1.1.1
GRE tunnel
ip.src ip.dst
1.2.3.4 1.1.1.1
<SCAN> (victim)
2.2.2.2
ICMP Packet  ICMP Packet
ip.src ip.dst
Fake ip.src
3.3.3.3 1.1.1.1 IP address
ping requests Example Public address
With information 1.2.3.4 Example Attacker address
Example Spoofed address
Example Victim address

59

## Slide 60

### How 2 Scan GRE via Fake ip.src

No I don’t have tunnel with 1.2.3.4 Drop that packet

Attacker
3.3.3.3
Public
Internet
1.1.1.1
GRE tunnel
ip.src ip.dst
2.2.2.2 1.2.3.4 1.1.1.1
<SCAN> (victim)
ICMP Packet  ICMP Packet
ip.src ip.dst
3.3.3.3 1.1.1.1 Example Public address
Example Attacker address
ping requests
With information 1.2.3.4 Example Spoofed address
Example Victim address

60

## Slide 61

How 2 Scan GRE via Fake ip.src
Attacker
3.3.3.3
Public
Internet
1.1.1.1
GRE tunnel
ip.src ip.dst
2.2.2.2 1.1.1.1
<SCAN> (victim)
2.2.2.2
ICMP Packet  ICMP Packet
ip.src ip.dst
Fake ip.src
3.3.3.3 1.1.1.1 IP address
ping requests Example Public address
With information 2.2.2.2 Example Attacker address
Example Spoofed address
Example Victim address

61

## Slide 62

Yeah I have GRE
with 2.2.2.2
 Use that packet
How 2 Scan GRE via Fake ip.src
Attacker
3.3.3.3
Public
Internet
1.1.1.1
GRE tunnel
ip.src ip.dst
2.2.2.2 1.1.1.1
2.2.2.2 Bingo!
ICMP Packet  ICMP Packet
ip.src ip.dst
3.3.3.3 1.1.1.1
Example Public address
ping requests
With information 2.2.2.2 Example Attacker address
Example Spoofed address
Example Victim address

62

## Slide 63

### How 2 Scan GRE via Fake ip.src

Oh 3.3.3.3 is pinging me response

Attacker
3.3.3.3
Public
Internet
1.1.1.1
GRE tunnel
ip.src ip.dst
3.3.3.3 1.1.1.1
2.2.2.2
ping requests
With information 2.2.2.2

Example Public address Example Attacker address Example Spoofed address Example Victim address

63

## Slide 64

Oh 3.3.3.3 is pinging me response How 2 Scan GRE via Fake ip.src

Attacker
3.3.3.3
Public
Internet
1.1.1.1
GRE tunnel
ip.src ip.dst
1.1.1.1 3.3.3.3
2.2.2.2
ping response
With information 2.2.2.2

Example Public address Example Attacker address Example Spoofed address Example Victim address

64

## Slide 65

### How 2 Scan GRE via Fake ip.src

Attacker
3.3.3.3
Public
Internet
1.1.1.1
GRE tunnel
ip.src ip.dst
1.1.1.1 3.3.3.3
2.2.2.2
ping response
With information 2.2.2.2
got GRE tunnel information
2.2.2.2 is 1.1.1.1 peers
(from identifier, sequence)

Example Public address Example Attacker address Example Spoofed address Example Victim address

65

## Slide 66

### How 2 Scan GRE via Fake ip.src

- ICMP

   - Identifier range: 256<sup>2</sup>

   - Sequence range: 256<sup>2</sup>

- ICMP Sender

   - Place fake GRE Source IP divide into identifier, sequence in ping

   - Send all 256<sup>4</sup> IPs to target

- ICMP Receiver

   - Filtered ICMP packet from target and recover ip.src IP from identifier, sequence to get who is GRE peer

66

## Slide 67

### GRE scanner

Victim Attacker listen host Spoof src.ip (also scannable)

Received ICMP ip.src: 160.25.104.199 Peer IP: 1.1.1.1 (from identifier, sequence)

https://github.com/123ojp/GREtunnel-scanner

67

## Slide 68

## **BOOM!** 💥 **Putting everything together GRE + No firewall = Intranet access**

68

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blackhat
BRIEFINGS
AUGUST 6-7, 2025
MANDALAY BAY / LAS VEGAS
BOOM! *
Putting everything together
GRE + No firewall = Intranet access
#BHUSA @BlackHatEvent ts
```

## Slide 69

Attack Scenario
Attacker
3.3.3.3
Public  10.0.0.1
Internet
1.1.1.1 10.0.0.2
Intranet
GRE tunnel Victim
GRE ip.src GRE ip.dst
2.2.2.2 1.1.1.1
UDP Packet  UDP Packet
2.2.2.2
ip.src ip.dst
GRE peer
3.3.3.3 10.0.0.2 Fake ip.src
IP address
DNS requests
Example Public address
Example Attacker address
Example Spoofed address
Example Victim address
69 Example Private address

## Slide 70

Yeah I have GRE
Attack Scenario  Use that packetwith 2.2.2.2
Attacker
3.3.3.3
Public  10.0.0.1
Internet
1.1.1.1 10.0.0.2
Intranet
GRE tunnel
GRE ip.src GRE ip.dst
2.2.2.2 1.1.1.1
2.2.2.2
UDP Packet  UDP Packet
ip.src ip.dst
3.3.3.3 10.0.0.2
DNS requests Example Public address
Example Attacker address
Example Spoofed address
Example Victim address
70 Example Private address

## Slide 71

The packet is to
10.0.0.2
Attack Scenario Forward it.
Attacker
3.3.3.3
Public  10.0.0.1
Internet
1.1.1.1 10.0.0.2
Intranet
GRE tunnel
ip.src ip.dst
3.3.3.3 10.0.0.2
2.2.2.2
DNS requests
GRE peer

Example Public address Example Attacker address Example Spoofed address Example Victim address Example Private address

71

## Slide 72

### Attack Scenario

Attacker
3.3.3.3
Public  10.0.0.1
Internet
1.1.1.1 10.0.0.2
Intranet
GRE tunnel
ip.src ip.dst
10.0.0.2 3.3.3.3
2.2.2.2
DNS response
GRE peer

Example Public address Example Attacker address Example Spoofed address Example Victim address Example Private address

72

## Slide 73

### Attack Scenario

Attacker
3.3.3.3
Public  10.0.0.1
Internet
1.1.1.1 10.0.0.2
Intranet
GRE tunnel
ip.src ip.dst
10.0.0.2 3.3.3.3
DNS response 2.2.2.2
GRE peer

Example Public address Example Attacker address Example Spoofed address Example Victim address Example Private address

73

## Slide 74

Web server config

Lab

Attacker
<YOUR IP> SNAT
Public  160.25.104.199 192.168.1.1
Internet
Target W eb Server
Router
GRE tunnel Intranet 192.168.1.2
1.1.1.1
Router config

74

## Slide 75

Webserver: 192.168.1.2 Victim Public IP: 160.25.104.200 Router Private IP: 192.168.1.1 Spoof IP (GRE peer): 1.1.1.1 Attacker Public: 154.12.177.142

75

## Slide 76

### Layer 2 tunnel GRETAP

Attacker
3.3.3.3 SNAT
Public  160.25.104.199 192.168.1.1
Internet
Target W eb Server
Router
GRE tunnel Intranet 192.168.1.2
ip.src ip.dst
1.2.3.4 160.25.104.199
 (victim)
mac.src mac.dst
1.2.3.4
any ?
ICMP Packet  ICMP Packet
ip.src ip.dst
Leak by OSINT or SNMP
3.3.3.3 1.1.1.1
ping requests
With information 1.2.3.4
76

## Slide 77

### TL;DR of attack condition

- Bad firewall configuration

- Use stateless, unencrypted, L3 tunnel (GRE, IPIP, SIT…)

- Use stateless, unencrypted, L2 tunnel (GRETAP) + mac leak (snmp)

- Even if one end has disabled the tunnel (Legacy configuration)

💥

- BOOM!

   - Intranet access from hacker without foothold

- IR is hard (IP Source are not reliable)

77

## Slide 78

## **Nightmare of VxLAN**

78

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
‘blackhat
BRIEFINGS
AUGUST 6-7, 2025
MANDALAY BAY / LAS VEGAS
Nightmare of VxLAN
78 |
```

## Slide 79

### What’s VxLAN?

- Stateless L2 tunnel

- Encapsulating Layer 2 Ethernet frames into a Layer 4 User Datagram Protocol (UDP) packet

- Each segmented subnet is uniquely identified by a VXLAN Network Identifier (VNI). **ip.src ip.dst**

|**ip.src**|**ip.dst**|
|---|---|
||UDP port|
|VXLAN Ne|twork Identifier  (VNI)|
|VxLAN|VxLAN|
|mac.src|mac.dst|
|VxLAN
ip.src|VxLAN
ip.dst|
||packet|

79

## Slide 80

### The vulnerable config RouterOS version

Linux version

80

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pifeK hat
BRIEFINGS
The vulnerable config
RouterOS version
[admin@MikroTik] > ip/address/export where interface=vxlan1
/ip address
add address=10.0.0.1/24 disabled=no interface=vxlan1 network=10.0.0.0
[admin@MikroTik] > interface/vxlan/export
/interface vxlan
add mac—address=FA:10:04:A1:E1:CF name=vxlan1 port=8472 vni=42 vrf=main vteps—ip-version=ipv4
/interface vxlan vteps
add interface=vxlanl1 remote-ip=1.1.1.1
Linux version
MYPUBIP=160.25.104.200
DSTADDR=1.1.1.1
DPORT=8472
VID=42
IF_NAME=vxlan-test
ip link add $IF_NAME type vlan id $VID remote $DSTADDR local $MYPUBIP dstport $DPORT
ip link set up dev $IF_NAME
ip addr add 10.0.0.1/24 dev $IF_NAME
80
```

## Slide 81

### How to config a normal peer

81

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pifeK hat
BRIEFINGS
How to config a ermal peer
MYPUBIP=1.1.1.1
DSTADDR=160.25.104.200
DPORT=8472
VID=42
IF_NAME=vxlan-test
ip link add $IF_NAME type vlan id $VID remote $DSTADDR local $MYPUBIP dstport $DPORT
ip link set up dev $IF_NAME
ip addr add 10.0.0@.2/24 dev $IF_NAME
ping -c 1 10.0.0.1
81
```

## Slide 82

### How to hijack VxLAN

82

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pifeK hat
BRIEFINGS
How to hijack VxLAN
MYPUBIP=9.9.9.9
DSTADDR=16@.25.104.200
DPORT=8472
VID=42
IF_NAME=vxlan-test
ip link add $IF_NAME type vlan id $VID remote $DSTADDR local $MYPUBIP dstport $DPORT
ip link set up dev $IF_NAME
ip addr add 10.0.0.2/24 dev $IF_NAME
ping -c 1 10.0.0.1
82
```

## Slide 83

### How to hijack VxLAN

Yeah, here's the only difference

83

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pifeK hat
BRIEFINGS
How to hijack VxLAN
MYPUBIP=9.9.9.9
DSTADDR=160. 25.104. 200 Yeah, here's the only difference
DPORT=8472
VID=42
IF_NAME=vxlan-test
ip link add $IF_NAME type vlan id $VID remote $DSTADDR local $MYPUBIP dstport $DPORT
ip link set up dev $IF_NAME
ip addr add 10.0.0.2/24 dev $IF_NAME
ping -c 1 10.0.0.1
83
```

## Slide 84

### Why?

- Linux Kernel does not check the IP Source of VxLAN? – Why it accept the VxLAN packet if the VNI && Port match one of its VxLAN interface

Match This

Don’t Check ?

84

## Slide 85

### Bug Feature!

- ip-link(8) — Linux manual page (VxLAN)

- Insecure default configuration

- Linux - default on

   - Can Disable

- RouterOS - ~~always~~ default on

<u>https://github.com/torvalds/linux/blob/master/drivers/net/vxlan/vxlan_core.c</u>

- ~~Cannot Disable~~ Fixed (CVE-2025-6443)

85

## Slide 86

### What’s happened when learning is enable

- When a valid VxLAN packet with the valid VNI && port

- Kernel will add the outer remote IP and VxLAN mac in to a Forwarding Database table (FDB)

- Next time when a packet destination mac address is in the FDB it will send to the remote

Match This
valid
Router OS
ip.src ip.dst 1.1.1.1
VxLAN peer
2.2.2.2 1.1.1.1
2.2.2.2
UDP port VNI
4789 10 Port and VNI match interface  vxlan1
mac.src mac.dst Use that packet
And write to table
00:12:34:56:78:99 <any>
Inner Packet
Mac Remote IP Interface
86
00:12:34:56:78:99 2.2.2.2 Vxlan1 (port: 4789 vni:10)

## Slide 87

### What’s happened when learning is enable

- When a valid VxLAN packet with the valid VNI && port

- Kernel will add the outer remote IP and VxLAN mac in to a FDB table

- Next time when a packet destination mac address is in the FDB it will send to the remote Match This

- invalid

Match This

Router OS **ip.src ip.dst** 1.1.1.1 VxLAN peer 8.8.8.8 1.1.1.1 2.2.2.2 UDP port VNI 4789 10 Port and VNI match interface vxlan1 mac.src mac.dst Use that packet and write to table 99:88:77:66:55:44 <any> **Mac Remote IP Interface** Inner Packet 00:12:34:56:78:99 2.2.2.2 Vxlan1 (port: 4789 vni:10) 87 Still add into FDB 99:88:77:66:55:44 8.8.8.8 Vxlan1 (port: 4789 vni:10)

## Slide 88

### What’s happened when learning is enable

- Thus, an attacker can create a VxLAN packet with mac address FF:FF:FF:FF:FF:FF

- The Linux Kernel will append the mac in to the list. invalid

Match This
invalid
Router OS
ip.src ip.dst 1.1.1.1
VxLAN peer
9.9.9.9 1.1.1.1
2.2.2.2
UDP port VNI Port and VNI match interface  vxlan1
4789 10 Use that packet
And write to table
mac.src mac.dst
FF:FF:FF:FF:FF:FF <any> Mac Remote IP Interface
Inner Packet
00:12:34:56:78:99 2.2.2.2 Vxlan1 (port: 4789 vni:10)
88 Still add into FDB
FF:FF:FF:FF:FF:FF 9.9.9.9 Vxlan1 (port: 4789 vni:10)

## Slide 89

### What’s happened when learning is enable

- when the kernel wants to send a broadcast packet on the VXLAN interface

- • It will look up the FDB table and send it to 9.9.9.9 (the attacker's address)

Router OS 1.1.1.1 VxLAN peer 2.2.2.2

|**ip.src**|**ip.dst**|
|---|---|
|1.1.1.1|9.9.9.9|
|UDP port|VNI|
|4789|10|
|mac.src|mac.dst|
|RouterOS’s mac|FF:FF:FF:FF:FF:FF|
|Inner|Packet|

Okay I want to send a destination mac address FF:FF:FF:FF:FF:FF The FDB table tell me to send to 9.9.9.9

**Mac Remote IP Interface** 00:12:34:56:78:99 2.2.2.2 Vxlan1 (port: 4789 vni:10) FF:FF:FF:FF:FF:FF 9.9.9.9 Vxlan1 (port: 4789 vni:10)

89

## Slide 90

### So, what attacker don’t know for a hijack?

However, all this information can be obtained by a simple scan (a packet)

90

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pifchat AS en
BRIEFINGS
DS
So, what attacker don’t know fora hijack?
MYPUBIP=9.9.9.9
DSTADDR=160.25.104.200
DPORT=8472
VID=42
IF_NAME=vxlan-test
ip link add $IF_NAME type vlan id $VID remote $DSTADDR local $MYPUBIP dstport $DPORT
ip link set up dev $IF_NAME
ip addr add|10.0.0.2/24 |dev $IF_NAME
ping -c 1 10.0.0.1
However, all this information can be obtained by a simple scan
(a packet)
90
```

## Slide 91

### What attacker don’t know

These three can know by sending numerous packet

91

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pifchat
BRIEFINGS
What attacker don’ t me
MYPUBIP=9.9.9.9
DSTADDR=160@.25.104.200
DPORT=8472
VID=42
IF_NAME=vxlan-test
ip link add $IF_NAME type vlan id $VID remote $DSTADDR local $MYPUBIP dstport $DPORT
ip link set up dev $IF_NAME
ip addr add 10.0.0.2/24 dev $IF_NAME
ping -c 1 10.0.0.1
These three can know by sending numerous packet
91
```

## Slide 92

### What attacker don’t know

Let's focus on how to get this

92

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pifchat
BRIEFINGS
What attacker don’ t know?
MYPUBIP=9.9.9.9
DSTADDR=160@.25.104.200
DPORT=8472
VID=42
IF_NAME=vxlan-test
ip link add $IF_NAME type vlan id $VID remote $DSTADDR local $MYPUBIP dstport $DPORT
ip link set up dev $IF_NAME
ip addr add|10.0.0.2/24 |dev $IF_NAME
ping -c 1 10.0.0.1
Let's focus on how to get this
92
```

## Slide 93

#### Gathering information (passive) – Broadcast mac

- Send VxLAN, which Mac is broadcasting (FF:FF:FF:FF:FF:FF)

- Wait for broadcast packet, e.g., ARP requests

|||||**Mac**|**Remote IP**|**Interface**|
|---|---|---|---|---|---|---|
|||||FF:FF:FF:FF:FF:FF|9.9.9.9|Vxlan1|
|**ip.src**|**ip.dst**|Router With
VxLAN|**ip.src**|**ip.dst**|||
|9.9.9.9|1.1.1.1||1.1.1.1|9.9.9.9|||
|UDP port|VNI||UDP port|VNI|||
|4789|10||4789|10|||
|mac.src|mac.dst||mac.src|mac.dst|||
|FF:FF:FF:FF:FF:FF|FF:FF:FF:FF:FF:FF||Victim’s mac|FF:FF:FF:FF:FF:FF|||
||Any||ARP requests i|nformation with IP range|||

93

## Slide 94

Gathering information (active) – The magic 5678

- Mikrotik Neighbor Discovery Protocol on UDP 5678 port

- When RouterOS receives a broadcast Neighbor Discovery message

- it will reply the message with its IP, Mac by broadcasting (FF:FF:FF:FF:FF:FF)

ip.src ip.dst Router OS ip.src ip.dst
1.1.1.1
9.9.9.9 1.1.1.1 1.1.1.1 9.9.9.9
VxLAN peer
UDP port VNI 2.2.2.2 UDP port VNI
4789 10 4789 10
mac.src mac.dst mac.src mac.dst
FF:FF:FF:FF:FF:FF FF:FF:FF:FF:FF:FF RouterOS’s mac FF:FF:FF:FF:FF:FF
Inner Packet Inner Packet Inner Packet Inner Packet
ip.src ip.dst ip.src ip.dst
0.0.0.0 255.255.255.255 RouterOS VxLAN IP 255.255.255.255
Mikrotik Neighbor Discovery Protocol Mikrotik Neighbor Discovery Protocol
Discover Response

94

## Slide 95

### Full Chain

Attacker 9.9.9.9

|**ip.src**|**ip.dst**|
|---|---|
|9.9.9.9|1.1.1.1|
|UDP port|VNI|
|4789|10  (Scan until match)|
|mac.src|mac.dst|
|FF:FF:FF:FF:FF:FF|FF:FF:FF:FF:FF:FF|
|Inner Packet
ip.src|Inner Packet
ip.dst|
|0.0.0.0|255.255.255.255|
|95
Mikrotik Neighbo
UDP p
Dis|r Discovery Protocol
ort 5678
covery|

Public Internet

2.2.2.2

VxLAN tunnel

10.0.0.1

1.1.1.1

## Slide 96

### Full chain

Attacker 9.9.9.9

Public 10.0.0.1 Internet When VNI matches 1.1.1.1 Accept & decapsulate VxLAN VxLAN tunnel **VxLAN interface** mac.src mac.dst 2.2.2.2 FF:FF:FF:FF:FF:FF FF:FF:FF:FF:FF:FF Inner Packet Inner Packet ip.src ip.dst 0.0.0.0 255.255.255.255 Mikrotik Neighbor Discovery Protocol UDP port 5678 Vxlan1 (port: 4789 vni:10) Discovery

###### Victim add attacker to FDB table

|**Mac**|**Remote IP**|**Interface**|
|---|---|---|
|00:12:34:56:78:99|2.2.2.2|Vxlan1 (port: 4789 vni:10)|
|FF:FF:FF:FF:FF:FF|9.9.9.9|Vxlan1 (port: 4789 vni:10)|

Got Neighbor Discovery on VxLAN

96

## Slide 97

### Full chain

Attacker 9.9.9.9

Lookup

Public 10.0.0.1 Internet 1.1.1.1 VxLAN tunnel Discovery protocol Response the packet **VxLAN interface** mac.src mac.dst 2.2.2.2 AB:CD:12:45:12:12 FF:FF:FF:FF:FF:FF Inner Packet Inner Packet ip.src ip.dst 10.0.0.1 255.255.255.255 **Mac Remote IP Interface** Mikrotik Neighbor Discovery Protocol UDP port 5678 00:12:34:56:78:99 2.2.2.2 Vxlan1 (port: 4789 vni:10) Response FF:FF:FF:FF:FF:FF 9.9.9.9 Vxlan1 (port: 4789 vni:10)

97

## Slide 98

### Full chain

Attacker 9.9.9.9

Public Internet 2.2.2.2

VxLAN tunnel

|**Mac**|**Remote IP**|**Interface**|
|---|---|---|
|00:12:34:56:78:99|2.2.2.2|Vxlan1 (port: 4789 vni:10)|
|FF:FF:FF:FF:FF:FF|9.9.9.9|Vxlan1 (port: 4789 vni:10)|

10.0.0.1 1.1.1.1 Encapsulate vxlan **ip.src ip.dst** 1.1.1.1 9.9.9.9 UDP port VNI 4789 10 mac.src mac.dst AB:CD:12:45:12:12 FF:FF:FF:FF:FF:FF Inner Packet Inner Packet ip.src ip.dst 10.0.0.1 255.255.255.255 Mikrotik Neighbor Discovery Protocol UDP port 5678 Response

98

## Slide 99

### Full chain

Attacker 9.9.9.9

Public Internet

10.0.0.1 1.1.1.1 VxLAN tunnel

**ip.src ip.dst** 1.1.1.1 9.9.9.9 UDP port VNI 2.2.2.2 4789 10 mac.src mac.dst AB:CD:12:45:12:12 FF:FF:FF:FF:FF:FF Inner Packet Inner Packet ip.src ip.dst 10.0.0.1 255.255.255.255 Got everything to hijack tunnel Mikrotik Neighbor Discovery Protocol 99 UDP port 5678 Response

## Slide 100

### Scan for VxLAN tunnel

- We only don’t know VNI, UDP port and IP – VNI: 1 ~ 16777214 (usually smaller then 100) – Port: Default 4789 or 8472

   - Destination IP J

- VxLAN Scanner Demo

   - Send numerous different VNI packet

   - Wait for reply

   - https://github.com/123ojp/VxLAN-Scanner

**ip.src ip.dst** 9.9.9.9 1.1.1.1 UDP port VNI 4789 10 mac.src mac.dst FF:FF:FF:FF:FF:FF FF:FF:FF:FF:FF:FF Inner Packet Inner Packet ip.src ip.dst 0.0.0.0 255.255.255.255 Mikrotik Neighbor Discovery Protocol UDP port 5678 Discovery

100

## Slide 101

Lab

Lab Web server config
Attacker
<YOUR IP>
VxLan IP: 10.0.0.1
Public  160.25.104.200
Internet
Target W eb Server
Router
VxLAN tunnel Intranet 192.168.122.20
RouterOS config
1.1.1.1

101

## Slide 102

### Videos

Webserver: 10.0.0.1 Victim Public IP: 160.25.104.200 Attacker Public: 160.25.104.198 VxLAN Port: 8472 VxLAN VNI: 42

102

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
root@CTFer-foxo: /home/o01230jp/fakegre# > |
ble B
ViC
Webserver: 10.0.0.1
Victim Public IP: 160.25.104.200
Attacker Public: 160.25.104.198
VxLAN Port: 8472
VxLAN VNI: 42
```

## Slide 103

##### Scan VxLAN in Real World

- Scan with VNI = 1 and default ports

VNI = 1 and default port

- 900+ of IPs reply VxLAN packets

   - 4000+ of IPs are discovered inside the tunnels.

   - Some are public IPs

🤯

      - Hijack public IPs

- Some reply with numerous broadcast packet

- Combining this with IP spoofing can potentially lead to DDoS

- • Some source IPs are private addresses.

   - 🤯 Why?

VNI = ? and port = ??

103

## Slide 104

But some source IPs are private addresses 🤯 Why?

104

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pifchat
BRIEFINGS
But some source IPs are private addresses
Why? &
```

## Slide 105

### I use VxLAN in encrypted tunnel, so I’m safe?

Encrypted tunnels E.g., IPSec or Wireguard

105

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisdichat Se ae : f
BRIEFINGS > ; A
| use VxLAN in encrypted tunnel, so I’m safe?
SRCADDR=192.168.196.56
DSTADDR=192.168.196.1
DPORT=8472
VID=42
ip link add vxlan® type vxlan id $VID remote $DSTADDR local $SRCADDR dstport $DPORT
ip link set up dev vxland
ip addr add 10.0.0.1/24 dev vxlan@
2: ens18: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
inet] 16@.25.104.131/27 pbrd 160.25.104.159 scope global ens18
3: tun®: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1412 qdisc fq_codel state UP group default qlen 1000
inet[ 192.168.196.56/24 Jord 192.168.196.255 scope global tund
Encrypted tunnels
E.g., IPSec or Wireguard
105 |
```

## Slide 106

I use VxLAN in encrypted tunnel, so I’m safe?

106

Encrypted tunnels E.g., IPSec or Wireguard

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat
BRIEFINGS
| use VxLé
SRCADDR=192.168.196:
DSTADDR=192.168.196.1
DPORT=8472
VID=42
ip link add vxlan@ type vxlan
ip link set up dev vxland
ip addr add 10.0.0.1/24 dev
Ocal $SRCADDR dstport $DPORT
2: ens18:_<BROADCAST,MULT group default qlen 1000
inet] 160. 25.104.13
3: tun®: <BROADCAS# tu 1412 qdisc
default qlen 1000
| inet] 192.168.198 0.255 scope global
Encrypted tunnels
E.g., IPSec or Wireguard
106 |
```

## Slide 107

VxLAN will still accept traffic in different interfaces

Due to VxLAN behavior, it still can be hijack & scan

107

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bistichat Se | f
BRIEFINGS ‘ , a
VxLAN will still accept traffic in different interfaces
SRCADDR=23.145.168.132
DSTADDR+160.25.104.131
DPORT=8472
VID=42
ip link add vxlan@ type vxlan id $VID remote $DSTADDR local $SRCADDR dstport $DPORT
ip link set up dev vxlan@g
ip addr add 10.0.0.2/24 dev vxlang
# tcpdump —-i any "port 8472" —n
@3:04:14.889560 | 23.145.168.132.46950 > 160.25.104.131.8472} OTV, flags [I] (@x@8), overlay 0, instance 42
ARP, Request who-has 10.0.0.1 tell 10.0.0.2, length 28
03:04:14.889614 IP[192.168.196.56.34993 > 23.145.168.132.8472:} OTV, flags [I] (x08), overlay @, instance 42
ARP, Reply 10.0.@.1 is-at d2:b1:84:dc:1b:d2, length 28
Due to VxLAN behavior, it still can be hijack & scan
107 |
```

## Slide 108

### TL;DR

- We can hijack VxLAN tunnel with only 3 properties

   - Victim IP address (EASY)

   - Victim VXLAN port (EASY, default port: 8472 or 4789)

   - VNI (Could Scan, usually smaller then 100)

- Information that the attacker does not need

🤯

   - Peer IP (or Spoof Source IP)

   - VXLAN interface Mac and IP on Victim

- If you have a public IP interface and a VxLAN on any interface,

- 108 you're done.

108

## Slide 109

## **What can hackers do after hijacking a tunnel**

109

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
- Blackhat Sed See
BRIEFINGS SS YZ
AUGUST 6-7, 2025
MANDALAY BAY / LAS VEGAS
What can hackers do after hijacking
a tunnel
```

## Slide 110

### What can hackers do after hijacking a tunnel

- Not only gain access to the intranet

   - Also hijack IP communication or perform MiTM between two sites

- Attacking Layer 2 Network Services (e.g., RADVD to RCE)

- IR is also hard (IP sources also cannot be trusted)

- These tunnels often run routing protocols:

   - BGP, OSPF

   - Hacker can hijack IPs that are not even transmitting through that tunnel

      - e.g., Domain controller or ESXi

110

## Slide 111

### What is BGP, OSPF

• Routing Protocol (Automated IP table between Routers )
I Have
192.168.1.0/24
Announce to others
Router A Router B Router C
169.254.0.1/30 169.254.0.2/30 169.254.1.2/30 169.254.1.1/30 192.168.4.1
192.168.1.1 BGP or OSPF BGP or OSPF
Domain Controller
Web Server
192.168.4.2
192.168.1.2
I have Router A and C
announce I have 192.168.4.0/24
192.168.1.0/24 via 169.254.0.1 Router B have Router A so
192.168.4.0/24 via 169.254.1.1 192.168.1.0/24 via 169.254.1.2

111

## Slide 112

### What is BGP, OSPF

- Some companies use VxLAN tunnels to connect two site

Router A Router B Router C
169.254.0.1/30 169.254.0.2/30 169.254.1.2/30 169.254.1.1/30 192.168.4.1
VxLAN
192.168.1.1 BGP or OSPF
Domain Controller
Web Server
192.168.4.2
192.168.1.2

112

## Slide 113

### Combined with the Bug Feature

- But if we hijack the VxLAN we can connect the routing protocol

   - And we can announce any IP and hijack

   - Then we can hijack DC and perform NTLM relay attack

Router A Router B Router C
169.254.0.2/30 169.254.1.2/30 169.254.1.1/30 192.168.4.1
192.168.1.1 BGP or OSPF
Domain Controller
Web Server
192.168.4.2
192.168.1.2
Attacker Hijack by the Bug
169.254.0.1/30
113
Connect OSPF or BGP
VxLAN

## Slide 114

### Combined with the Bug Feature

- But if we hijack the VxLAN we can connect the routing protocol – And we can announce any IP and hijack

   - Then we can hijack DC and perform NTLM relay attack

Router A Router B Router C
169.254.0.2/30 169.254.1.2/30 169.254.1.1/30 192.168.4.1
192.168.1.1 BGP or OSPF
Domain Controller
Web Server
192.168.4.2
192.168.1.2
Router B route table
Subnet Next-hop
192.168.4.0/24 169.254.1.1
Attacker 192.168.4.2/32 169.254.0.1
169.254.0.1/30
Received by OSPF
114 I have /32 is smaller so traffic will go to attacker
192.168.4.2 /32
VxLAN

## Slide 115

### Combined with the Bug Feature

- But if we hijack the VxLAN we can connect the routing protocol – And we can announce any IP and hijack

   - Then we can hijack DC and perform NTLM relay attack

Router A Router B Router C
169.254.0.2/30 169.254.1.2/30 169.254.1.1/30 192.168.4.1
192.168.1.1 BGP or OSPF
Domain Controller
Web Server
192.168.4.2
192.168.1.2 Router C route table
Subnet Next-hop
192.168.4.0/24 eth0
192.168.4.2/32 169.254.1.2
Attacker
169.254.0.1/30
115 I have Received by OSPF
192.168.4.2 /32 /32 is smaller so traffic will go to attacker
VxLAN

## Slide 116

#### What if Routing protocol was attacked – IP hijack

|**Hijack Target**|**Requirement**|**Affect**|
|---|---|---|
|Domain control with NTLM relay|Disabled SMB signing or ADCS ECS8|Domain take over|
|Windows services with responder|Weak password, Hashcat|User account take over|
|Domain control but doing nothing|None|DoS|
|DNS server|None|DNS hijack|
|vSphere / PVE / Other HTTPS Service|MITM
(if the original SSL is not validated,
user will not notice)|vSphere / PVE take over
Account take over|
|SSH server|User needs to trust new ssh signature
(User might not notice)|Server take over|

116

## Slide 117

**Bonus – Bad configuration in the company’s OSPF led to IP hijacking** https://hackmag.com/security/routing-nightmare/

117

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blackhat
BRIEFINGS
AUGUST 6-7, 2025
MANDALAY BAY / LAS VEGAS
Bonus — Bad configuration in the
company’s OSPF led to IP hijacking
https://hackmag.com/security/routing-nightmare/
```

## Slide 118

### Do you check tcpdump after get into intranet?

If you see this on victim's intranet it might be vulnerable.

https://hackmag.com/security/routing-nightmare/

118

## Slide 119

### Bad configuration OSPF

- Some companies use OSFP for intranet routing

- And open to all interfaces (ports)

• Attacker could connect to OSPF and do IP hijack with any devices
Router A Router B Router C
169.254.0.1/30 169.254.0.2/30 169.254.1.2/30 169.254.1.1/30 192.168.4.1
OSPF
OSPF
Domain Controller
Web Server
192.168.4.2
192.168.1.2 This interface should not open
OSPF, but... J
Router A route table (Also B,C)
Subnet Next-hop
Compromised
Mail server 192.168.4.0/24 169.254.0.2
Connect Router A OSPF
192.168.1.3
192.168.4.2/32 192.168.1.3
Dummy interface Announce 192.168.4.2/32
119
Create by attacker
Received by OSPF
192.168.4.2

## Slide 120

## **Take aways**

120

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat
BRIEFINGS
AUGUST 6-7, 2025
MANDALAY BAY / LAS VEGAS
Take aways
10 |
```

## Slide 121

Take aways - Blue Team

- Check all unencrypted tunnels in the company.

   - Don’t use it !

   - e.g., GRE, IPIP, SIT, GRETAP, VXLAN

- Setup secure firewall

   - Filtered intranet outbound traffic (SYN-ACK)

   - Check IP spoofing in intranet

- ALL ISPs should block IP spoofing (but it is not possible)

- Check if OSPF is only enabled on ports between routers.

- Monitor Routing Prefixes for Anomalies

121

- Setup Minimum Acceptable Prefix Size in routers, e.g., /24

## Slide 122

### Take aways – Red team

- Scan or OSINT victims’ unencrypted tunnels

- Once Inside the Intranet, Check Victims' Networking

   - Use Source IP Spoofing Technique During High-Risk Scanning

   - Check for OSPF Hello Messages

- Scan for misconfigured VxLAN

   - Hijack tunnel to get intranet access

   - Abuse routing protocol and hijack Ips

- Future research

•122 Scan, Find, Hack! <u>https://github.com/123ojp/GREtunnel-scanner https://github.com/123ojp/VxLAN-Scanner</u>

## Slide 123

### Take aways – Tools Maker

- Implement intranet IP spoofing C&C tool

   - Automated testing of IP spoofing feasibility for the target intranet.

   - Some router still do SNAT even if the packet is a server response

      - Automated correction for IP destination and IP source mismatches within the same TCP session

   - Automated sending of an H.323 or a new TCP packet to trigger the router's NAT mechanism for ISPs that filter private IP addresses as source IPs.

   - Automated OSPF IP hijack & NTLM relay to DC

- Implement a more efficient GRE scanner for global scan

   - similar to masscan

123

## Slide 124

# Q&A

#BHUSA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blackhat Se ae
BRIEFINGS Say
QéA
MANDALAY BAY / LAS VEGAS
#BHUSA @BlackHatEvents
```

## Slide 125

# USA 2025 Thank You !

o123ojp shu-hao-tung

#BHUSA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Ctlche hat
USA 2025
OU TREND:
Thank vou !
X 0123 0jp in shu-hao-tung
#BHUSA @BlackHatEvents
```
