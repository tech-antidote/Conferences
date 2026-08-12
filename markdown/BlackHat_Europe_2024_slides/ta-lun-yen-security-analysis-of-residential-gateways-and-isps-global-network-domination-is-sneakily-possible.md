---
title: "Security analysis of Residential Gateways and ISPs global network domination is (sneakily) possible"
speakers: ["Ta-Lun Yen"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2024"
edition: "Europe"
year: 2024
source_pdf: "BlackHat_Europe_2024_slides/Ta-Lun Yen_Security analysis of Residential Gateways and ISPs global network domination is (sneakily) possible.pdf"
pages: 62
sha256: "f6085e6351ae165bda518387877c4f351d7650f758cbae19a4ce606a412966e9"
text_chars: 23386
ocr_pages: 3
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T22:47:06Z"
---
# Security analysis of Residential Gateways and ISPs global network domination is (sneakily) possible

**Speakers:** Ta-Lun Yen  
**Conference:** Black Hat Europe 2024  
**Source:** `BlackHat_Europe_2024_slides/Ta-Lun Yen_Security analysis of Residential Gateways and ISPs global network domination is (sneakily) possible.pdf` (62 pages)

## Slide 1

Security analysis of Residential Gateways and ISPs – Global network domination is (sneakily) possible

Ta-Lun Yen Senior Vulnerability Researcher, TXOne Research

## Slide 2

## **whoami**

- Ta-Lun Yen (@logonfail)

- Vulnerability Researcher, TXOne Networks

   - Break Everything

      - (software & hardware, reverse engineering, embedded systems)

   - Various International InfoSec Conferences

   - Taiwanese hacker group "UCCU Hacker"

Information Classification: General

#BHEU @BlackHatEvents

## Slide 3

## **What is a Residential Gateway?**

- Bridges premises to Internet

- Definition –

   - Modem **modulates** {fiber, coaxial, phone line} to/from Ethernet

   - **Residential Gateway** performs modem + computing

      - e.g. NAT, Firewall, Routing, DHCP

- Refers to many devices; **focusing on ones from ISP**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 4

## **Why is RG important and worth studying into?**

• 79% of household(*) has access to fixed internet (=has a RG)

- Gateway devices are lucrative targets for adversaries;

   - not yet RGs (ones by ISPs)

- (*) OECD ICT Access and Usage by Households and Individuals Database, Household with fixed broadband Internet access at home https://oe.cd/dx/ict-access-usage

Information Classification: General

#BHEU @BlackHatEvents

## Slide 5

### Q: How many Residential Gateways (RGs) on Earth? Answer: Could be at least 153 million (*)

Information Classification: General

#BHEU @BlackHatEvents

(*) Based on “Broadcom SDK Un-stealthy Stealth Mode”. Not accurate depiction.

## Slide 6

## **Past cases of finding bugs against ISP management/RGs**

- Shahar Tal, 44CON (2014)

   - ISP-side remote management takeover from exposed infrastructure

- Peter Geissler & Steven Ketelaar, HITB AMS (2013)

- Buffer overflow leading to RCE on exposed TR069 daemon on RG's WAN

- • Sam Curry (2024)

   - Authentication bypass on ISP-side remote management infrastructure

   - Execute commands on RG via command injection through management

#BHEU @BlackHatEvents

Information Classification: General

## Slide 7

## **Inspiration of research / Brief Conclusion**

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekchat Inspiration of research / Brief Conclusion
EUROPE 2024
Road to "the one ring" txOne
* We successfully demonstrated an attack chain,
however, we believe the same mistake can happen to all ISPs. Modems (and telecoms) are also not‘as secure
* Shortfall of the CVE system: EFL (CLCHESRA) GELTHIEERS TLE
Systematic Risks cannot be assigned as CVE 6 0-days to 4 million modems within a week
CID COFT4 HSE ANAM C400H BOETF AIS
¥
Weak password + Guessable password +
Post-auth arbitary file Post-auth CMDi -> root Ta-Lun Yen,
write 0-day -> RCE RCE TXOne Research
\ oeayat | txone
Internet
Information Classification: General
```

## Slide 8

## **Inspiration of research / Brief Conclusion**

Outsider IP Protocol
IPoE / PPPoE
Intern
DSLA
Intern et
POST /cgi-bin/cgi_main.cgi HTTP/1.1 BRAS M /  RG
et Excha
... OLT
nge
cgiName=time_tzsetup.cgi&time_action=
test&ntp=example.com;uname -a
Management
ISP Premise

Information Classification: General

#BHEU @BlackHatEvents

## Slide 9

## **Inspiration of research / Brief Conclusion**

- 14 RGs, 11 ISPs, 9 countries

- RGs are not very safe,

   - neither the ISPs

- Demonstration –

   - How to study your RG – From board to ISP and many RGs

   - Bypassing OEM’s implementation of Broadcom TrustZone – Misuse of SDK

   - Among a popular SoC – Detecting all RGs on the Internet

Information Classification: General

#BHEU @BlackHatEvents

## Slide 10

## **Modern Infrastructure: Everything needs telecommunications**

Ehlen, Mark & Vargas, Vanessa. (2013). Multi-hazard, multi-infrastructure, economic scenario analysis. Environment Systems & Decisions. 33. 10.1007/s10669-013-9432-y.

Information Classification: General

#BHEU @BlackHatEvents

## Slide 11

## **Modern Infrastructure: Everything needs telecommunications**

TXOne Networks  |  Keep the Operation Running

Information Classification: General

#BHEU @BlackHatEvents

## Slide 12

## **Let’s analyze RGs and providers behind them**

- Layer-1 Protocols:

- DOCSIS (cable)

- xPON (fiber)

- VDSL (phone line)

- Network Protocols:

- PPPoE,

- IPoE,

- or just IP4/6

- Management Protocols:

- TR-069 (CWMP)

- SNMP

- SSH/HTTP

- SoC makers

   - Broadcom, Intel, Lantiq, Realtek, Huawei & ZTE

Information Classification: General

#BHEU @BlackHatEvents

## Slide 13

## **From the provider to your premise**

IP Protocol
IPoE / PPPoE
Internet DSLAM /
BRAS GPON RG
Exchange OLT
ISP Premise

Information Classification: General

#BHEU @BlackHatEvents

## Slide 14

## **From the provider to your premise**

IP Protocol
Manage  IPoE / PPPoE
Convert to GPON You
Subscribers
Internet DSLAM /
BRAS GPON RG
Exchange OLT
ISP Premise

Information Classification: General

#BHEU @BlackHatEvents

## Slide 15

## **From the provider to your premise**

IP Protocol
IPoE / PPPoE
Internet DSLAM /
BRAS GPON RG
Exchange OLT
Remote
Management
ISP Premise

Internet

Information Classification: General

#BHEU @BlackHatEvents

## Slide 16

## **From the provider to your premise**

IP Protocol
IPoE / PPPoE
Content Served Surf the Internet
Internet DSLAM /
Internet BRAS GPON RG
Exchange OLT
Remote
Management
ISP Premise

Information Classification: General

#BHEU @BlackHatEvents

## Slide 17

## **From the provider to your premise**

IP Protocol
IPoE / PPPoE
Config
Received
Internet DSLAM /
Internet BRAS GPON RG
Exchange OLT
Change settings
on RG
Remote
Management
ISP Premise

Information Classification: General

#BHEU @BlackHatEvents

## Slide 18

## **Testing Methodology**

- Focus on **RG**

   - Well connected, many attack surfaces

   - From hardware, software & networking stack to ISP & **Remote management**

Residential
Gateway
DSLAM /
… GPON Baseband
OLT
OS Ethernet LAN
Management
Other services
TXOne Networks  |  Keep the Operation Running

Information Classification: General

#BHEU @BlackHatEvents

## Slide 19

## **Brief conclusion of analysis**

- 14 RGs, 11 ISPs, 9 countries

- RGs -

   - Common:

      - Lack of modern practices

      - "Solder-UART-to-root“

      - Command Injections

- ISPs -

   - Exposed management is common

   - Huawei & ZTE still in Europe

Information Classification: General

#BHEU @BlackHatEvents

## Slide 20

## **Assessing entry methods**

Identify
Study
Board
Yes and usable
Has  Extract Firmware
Debug? Contents
No
Identify Develop Method to  Extract from
Storage Type Read Storage Storage

Information Classification: General

#BHEU @BlackHatEvents

## Slide 21

## **Assessing entry methods, many cases**

Identify
Study
Board
Google-fu
Has  Extract Firmware
Debug? Contents
Explore Network Interface
for common vulnerabilities
Identify Develop Method to  Extract from
Storage Type Read Storage Storage

Information Classification: General

#BHEU @BlackHatEvents

## Slide 22

## **Board component identification & assessing entry methods**

How to interact with
the board?

Information Classification: General

#BHEU @BlackHatEvents

## Slide 23

## **Board component identification & assessing entry methods**

Transformers
UART Identify
Study
Board
SoC
DRAM
Flash Has  Yes and usable Extract
Debug Firmware
? Contents
Debug points
No
Wireless IC
Identify
Develop Method  Extract from
Storage
to Read Storage Storage
Type
???
TXOne Networks  |  Keep the Operation Running
Information Classification: General #BHEU @BlackHatEvents

#BHEU @BlackHatEvents

## Slide 24

## **Board component identification & assessing entry methods**

UARTUART Identify
Study
Board
Has  Yes and usable Extract
Debug Firmware
? Contents
No
Identify
Develop Method  Extract from
Storage
to Read Storage Storage
Type

TXOne Networks  |  Keep the Operation Running

Information Classification: General

#BHEU @BlackHatEvents

## Slide 25

## **Board component identification & assessing entry methods**

UARTUART

Identify Board

Study

```
Base: 4.8_01
CFE version 1.0.38-116.233 for BCM96848 (32bit,SP,BE)
Build Date: Wed Mar 20 23:08:57 CST 2019 (ci@builder)
Copyright (C) 2000-2013 Broadcom Corporation.
```

```
Boot Strap Register:0x10000000
Chip ID: BCM68488_A1_, MIPS: 600MHz, DDR: 533MHz, Bus: 300MHz
RDP: 428MHz
Main Thread: TP0
Total Memory: 268435456 bytes (256MB)
Boot Address: 0xb8000000
```

Has Debug ? No Identify Storage Type

Extract Firmware Contents

Yes and usable

Develop Method Extract from to Read Storage Storage

TXOne Networks  |  Keep the Operation Running

Information Classification: General

#BHEU @BlackHatEvents

## Slide 26

## **Flash extraction via Pre-boot environment**

(b) Interrupt data lines on FLASH
Vcc ON Read  Read
Bootloader OS
SoC Initialize Bootloader OS
Bootloader
Dump
Rescue
(a) Boot selection may not be disabled FLASH
mode

Information Classification: General

#BHEU @BlackHatEvents

## Slide 27

## **Reading firmware/configuration files from board**

- For targets like RG, de-soldering may not be best

   - Risks breaking the board, depending on experience level

://<string>

Information Classification: General

#BHEU @BlackHatEvents

## Slide 28

## **Reading firmware/configuration files from board**

- Some boards requires “MITM method” (scraping)

- Sometimes having to soldering to BGA solder joints beneath the chip

- • Wire length and impendence matching matters

- Use proper breakout boards

Information Classification: General

#BHEU @BlackHatEvents

## Slide 29

## **No Chip Marking? No Problem!**

- What if markings on chip got erased away/eroded away?

- • Markings are etched via laser = grooves on packaging • I recover them with a pencil

Information Classification: General

#BHEU @BlackHatEvents

## Slide 30

## **Reading firmware/configuration files from board**

Arris V2

- If `binwalk` doesn't work:

   - Try `hexedit` or `strings`

   - Try finding magic

      - `5d 00 00 10 00, 5d 00 00 01 00` (LZMA)…

   - Look for regularities

- Try ://<string>

B  M Unpac

- B  M  irm are  ma e Unpac er

Shell

Information Classification: General

#BHEU @BlackHatEvents

## Slide 31

## **Actual Study, Case 1**

- Broadcom Gen 3

   - Secure Boot & Root-of-Trust

   - FDE

- 802.1x to authenticate with ISP

- Difficult to desolder/scrape traces

   - BGA56

   - Tight Clearance

Information Classification: General

#BHEU @BlackHatEvents

## Slide 32

## **Case 1, procrastinate on soldering**

- Found discussion of Case 1 in China: Enshan Wi-Fi Hobbyists

- Found firmware distribution page

- Site offline

   - AWS S3 -- Wayback Machine

   - Retrieved another model’s firmware by same vendor

   - Unencrypted

Information Classification: General

#BHEU @BlackHatEvents

## Slide 33

## **Case 1, procrastinate on soldering**

- Needs a primitive to dump firmware & code exec

   - LAN management looks safe

   - Not much on WAN

   - Don’t want to desolder

- Looked at unencrypted dump from another device

- `$ ff '*.rules*' ./etc/udev/rules.d/85-SerialPort.rules ./etc/udev/rules.d/50-config.rules`

```
$ cat ./etc/udev/rules.d/85-SerialPort.rules
ACTION=="add", KERNEL=="ttyUSB[0-9]*", SUBSYSTEM=="tty", \
ATTRS{idVendor}==“0403", ATTRS{idProduct}==“6001", \
RUN+="/bin/sh /bin/start_debug"
```

TXOne Networks  |  Keep the Operation Running

Information Classification: General

#BHEU @BlackHatEvents

## Slide 34

**Case 1,** **`/bin/start_debug`**

```
<< Connected
<< PROTOCOL V1.0
>> AAAAAAAAAAAAAAAAAAAAAAAAAAAAA
<< PROTOCOL CLOSED
```

Information Classification: General

#BHEU @BlackHatEvents

## Slide 35

## **Case 1,** **`/bin/start_debug`**

- Proprietary protocol

   - OpCode-based

      - 8001 for reboot, 8002 for update…

   - Requires fixed password

- `<< Connected`

- `<< PROTOCOL V1.0`

- `>> AAAAAAAAAAAAAAAAAAAAAAAAAAAAA`

- `<< PROTOCOL CLOSED`

- Wrote dissector

Information Classification: General

#BHEU @BlackHatEvents

## Slide 36

**Case 1,** **`/bin/start_debug`**

```
<< Connected
<< PROTOCOL V1.0
>> PASSWORD
<< PROTOCOL STARTED
>> EA8002/payload;id;uname
<< root; Linux 2.6..
```

Information Classification: General

#BHEU @BlackHatEvents

## Slide 37

## **Case 1,** **`/bin/start_debug`**

   - Bypassed security guarantees

      - **_L_** CE as root on device

      - “Bypass TrustZone”

      - Keys in root-of-trust and decrypted via TrustZone

- `<< Connected`

   - Not secured when data in use:

- `<< PROTOCOL V1.0`

- `>> PASSWORD`

   - Extracted 802.1x keys

- `<< PROTOCOL STARTED`

- `>> EA8002/payload;id;uname`

   - Extracted FDE keys

- `<< root; Linux 2.6..`

Information Classification: General

#BHEU @BlackHatEvents

## Slide 38

## **Actual Study, Case 2**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 39

## **Common problem with RG software**

- Lack of hardening is common (e.g. no NX, no canary)

Allow-List & Internet

(e.g. no NX, no canary)
But this is found everywhere:
Web Telnet
TFTP TR069
MGMT SSH
Case 2 RG, WAN (ppp0)
Case 2 RG, LAN-side (br0)
Web Telnet
TFTP TR069
MGMT SSH
Bugs are LAN-side (yet)
LAN Users

- But this is found everywhere:

- Bugs are LAN-side (yet)

Information Classification: General

#BHEU @BlackHatEvents

## Slide 40

### How to expand our attack primitive?

Information Classification: General

#BHEU @BlackHatEvents

## Slide 41

## **Case 2 - Cross-referencing iptables & services**

- Certain IP ranges can reach management via WAN

- Only blocks ICMP Request (not other types)

Public IPs

Information Classification: General

#BHEU @BlackHatEvents

## Slide 42

## **How to get inside everyone’s RG?**

- Has post-auth RCE on management interface

- Needs to escalate RCE bug to pre-auth

   - High Privileged Account –

      - Fixed username, Password tied to **ETH0_MAC_ADDR[-4:]**

      - Shared "Guest" account allows reading **ETH0_MAC_ADDR**

- Needs to reach management interface’s WAN side

?
Internet

Information Classification: General

#BHEU @BlackHatEvents

## Slide 43

## **Finding Management Infrastructure on Internet, Example**

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat
EUROPE 2024
Finding Management Infrastructure on Internet,
Chain ppp0.1-WEB (2 referenc
prot opt source
all -- 10.248.0.0/13
all 172.16.0.0/12
all 128
all
all
all
all
all
all anywhere
Chain veip®.2-DNS (2 references)
target prot source
DROP all -- anywhere
Chain veipd.2-FTP (2 references)
prot opt source
all -- anywhere
ip®.2-INPUT (1 refer
prot opt source
ip®.2-PING icmp -- anywhi
-ip®.2-PING_OF_DEATH icmp anywhere
-SYN_FLOODING tcp
Information Classification: General
‘tination
anywhere
anywhere
where
anywhere
anywhe
anywhere
anywhere
anywhere
tination
anywhere
destination
anywhere
destination
anywhere
[115/1969]
icmp echo-request
tcp flags:SYN,RST,A
Example
s Please Login
Device Management
SUITE NOSSIS
Username
Password
Language: | English
Username: |
Password:
pyrigh'
taliO
a)
Reset
```

## Slide 44

## **From the “provider” to your premise**

IP Protocol
IPoE / PPPoE
Internet DSLAM /
Internet BRAS GPON RG
Exchange OLT
WAN-side
Management allowlist
ISP Premise

Information Classification: General

#BHEU @BlackHatEvents

## Slide 45

## **From the “provider” to your premise**

IP Protocol
IPoE / PPPoE
POST /cgi-bin/cgi_main.cgi HTTP/1.1 Internet DSLAM /
Internet BRAS GPON RG
... Exchange OLT
cgiName=time_tzsetup.cgi&time_action=test& \
ntp =example.com;uname -a
WAN-side
IP Type Desc
Management allowlist
PUBLIC_DEVICE_1 DVR Multiple(*),
ISP Premise including  a  DVR
DVR
PUBLIC_DEVICE_2 SSL VPN Fortigate
TXOne Networks  |  Keep the Operation Running

Information Classification: General

#BHEU @BlackHatEvents

## Slide 46

## **From the “provider” to your premise**

Internet IP Protocol
IPoE / PPPoE
POST /cgi-bin/cgi_main.cgi HTTP/1.1 Internet DSLAM /
Internet BRAS GPON RG
... Exchange OLT
cgiName=time_tzsetup.cgi&time_action=test& \
ntp =example.com;uname -a
WAN-side
Management allowlist
ISP Premise
DVR

Information Classification: General

#BHEU @BlackHatEvents

## Slide 47

## **From the “provider” to your premise**

- Case 2 – 4M affected

 Case 2 – 4M affected Outsider • RCE on all devices • Device removed Internet BRA Internet `POST /cgi-bin/cgi_main.cgi HTTP/1.1` Exchang immediately `...` e S • Fixed in two weeks `cgiName=time_tzsetup.cgi&time_action=test& \ ntp=example.com;uname -a` • Case 1 – Management • Bypassed TrustZone ISP Premise DVR • Extracted FDE key & 802.1X credentials `<< Connected` • Can “Bring your own `>> PASSWORD` GPON”

IP Protocol IPoE / PPPoE

DSLAM / OLT

GPON

ISP Premise

```
<< Connected
<< PROTOCOL V1.0
>> PASSWORD
<< PROTOCOL STARTED
>> EA8002/payload;id;uname
<< root; Linux 2.6..
```

RG

Information Classification: General

#BHEU @BlackHatEvents

## Slide 48

## **Shared bug from SDK (ICMP, CMDi)**

://bcmdrivers

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekchat Shared bug from SDK (ICMP, CMDi)
EUROPE 2024
-//ocmdrivers
48.4k files (401 ms) ] Save
Vv @® ...c-rt-5.04axhnd.675x/bcmdrivers/Makefile @ Makefile - # master
1 # File: bcemdrivers/Makefile
#
3 # Makefile for the Linux kernel modules.
121 # whether or not the driver will be compiled
122 # DIRECTORY is the directory (relative to bcmdrivers)
where all the imp1X subdirectories
123 # reside
Information Classification: General
```

## Slide 49

## **SoC Vendor SDK: Un-stealthy Stealth Mode**

```
$ strings libcms_core.so |grep -i icmp-type
-p icmp -m icmp --icmp-type 8
```

```
iptables -A INPUT -i %s -p icmp --icmp-type 8 -j DROP 2>/dev/null
iptables -A OUTPUT -o %s -p icmp --icmp-type 3/3 -j DROP 2>/dev/null
iptables -A OUTPUT -o %s -p icmp --icmp-type 11 -j DROP 2>/dev/null
iptables -D INPUT -i %s -p icmp --icmp-type 8 -j DROP 2>/dev/null
iptables -D OUTPUT -o %s -p icmp --icmp-type 3/3 -j DROP 2>/dev/null
iptables -D OUTPUT -o %s -p icmp --icmp-type 11 -j DROP 2>/dev/null
```

Information Classification: General

#BHEU @BlackHatEvents

## Slide 50

## **SoC Vendor SDK: Un-stealthy Stealth Mode**

- `libcms` _core responsible for parsing config

- RFC 792 ICMP has multiple message types

- If blocking 8 (Echo):

   - Timestamp (13)

   - Redirect (5)

- Uncovers device if blocking 8 and not 13

```
$ strings libcms_core.so |grep -i icmp-type
-p icmp -m icmp --icmp-type 8
iptables -A INPUT -i %s -p icmp --icmp-type 8 -j DROP 2>/dev/null
iptables -A OUTPUT -o %s -p icmp --icmp-type 3/3 -j DROP 2>/dev/null
iptables -A OUTPUT -o %s -p icmp --icmp-type 11 -j DROP 2>/dev/null
iptables -D INPUT -i %s -p icmp --icmp-type 8 -j DROP 2>/dev/null
iptables -D OUTPUT -o %s -p icmp --icmp-type 3/3 -j DROP 2>/dev/null
iptables -D OUTPUT -o %s -p icmp --icmp-type 11 -j DROP 2>/dev/null
```

Information Classification: General

#BHEU @BlackHatEvents

## Slide 51

## **SoC Vendor SDK: Command Injection in CMS CLI**

# • Function intended for CLI; Used by vendor with volition

Information Classification: General

#BHEU @BlackHatEvents

## Slide 52

## **Shared bug from SoC Vendor SDK (ICMP, CMDi)**

- Case 2 bugs were actually inside SoC vendor SDK:

   - ICMP – Allows discovery of device over Internet

   - Command Injection – Shared among all boards

- Reported, **fixed in 22 days**

**Time** 2023-10-24 Consulted vendor about vulnerability pro ram’s scope 2023-10-27 Vendor is willing to take reports 2023-11-30 Vulnerability reported to vendor 2023-12-01 Vendor validated the reports and is working on a fix 2023-12-22 Vendor published private advisory with fix 2024-11-11 Informed vendor of intent to public disclosure

Information Classification: General

#BHEU @BlackHatEvents

## Slide 53

## **Summary**

- Presented actual cases –

   - Case 1 – From the board to the ISP

   - Case 2 – TrustZone bypass leading to key extraction

   - SDK –

      - ICMP stealth mode allows discovery; shared command injection bug

<< Connected
<< PROTOCOL V1.0
>> PASSWORD
<< PROTOCOL STARTED
>> EA8002/payload;id;uname
<< root; Linux 2.6..
TXOne Networks  |  Keep the Operation Running

TXOne Networks  |  Keep the Operation Running

Outsider

IP Protocol IPoE / PPPoE

> Internet BR DSLAM GPO Internet `POST /cgi-bin/cgi_main.cgi HTTP/1.1` Exchan `...` / OLT N RG

> ge AS `cgiName=time_tzsetup.cgi&time_action=test& \ ntp=example.com;uname -a` Management ISP Premise DVR

Information Classification: General

#BHEU @BlackHatEvents

## Slide 54

#### **Residential Gateway Security Recommendations for End-users, Telecommunication Providers**

- Prime Question:

   - How to detect compromise of RGs?

      - Adversaries could update RG with rootkits

      - No TrustZone/Secure Boot to validate running firmware

• Integrity Check Canary
Embed A in firmware
Remote
Secret? RG
Management
A

Information Classification: General

#BHEU @BlackHatEvents

## Slide 55

#### **Residential Gateway Security Recommendations for End-users, Telecommunication Providers**

- Prime Question:

   - How to detect compromise of RGs?

      - Adversaries could update RG with rootkits

      - No TrustZone/Secure Boot to validate running firmware

   - Integrity Check Canary

New secret in FW
Remote
Secret? RG
Management
A

Information Classification: General

#BHEU @BlackHatEvents

## Slide 56

#### **Residential Gateway Security Recommendations for End-users**

- Solution – End-users

   - Employ a gateway/firewall behind RG

   - Block private address range on incoming firewall

   - Configure RG as “modem mode” (disable routing)

New secret in FW
Remote
Secret? RG LAN
Management
A

Information Classification: General

#BHEU @BlackHatEvents

## Slide 57

#### **Residential Gateway Security Recommendations for OEMs/Telecommunication Providers**

• Detect abnormal network behavior in control plane

Information Classification: General

#BHEU @BlackHatEvents

## Slide 58

#### **Residential Gateway Security Recommendations for OEMs/Telecommunication Providers**

# • Detect abnormal network behavior in control plane

Outsider IP Protocol
IPoE / PPPoE
POST /cgi-bin/cgi_main.cgi HTTP/1.1 Internet DSLAM /
Internet GPON
... Exchange BRAS OLT RG
cgiName=time_tzsetup.cgi&time_action=test& \
ntp=example.com;uname -a
Management
ISP Premise
Install artifacts
TXOne Networks  |  Keep the Operation Running
Information Classification: General

Information Classification: General

#BHEU @BlackHatEvents

## Slide 59

#### **Residential Gateway Security Recommendations for OEMs/Telecommunication Providers**

- Detect abnormal network behavior in control plane

- Mandate baselines & standards –

   - Hardware-backed secure boot, proper use of TrustZone

   - FIPS 140-2, ISO/IEC 62443 4-2 Level >=2

   - EN 303 645

- Apply secure coding practices

Outsider IP Protocol
IPoE / PPPoE
Intern
DSLA
Interne et GP
POST /cgi-bin/cgi_main.cgi HTTP/1.1 BRAS M /  RG
t Excha ON
... OLT
nge
cgiName=time_tzsetup.cgi&time_action=te
st& \ ntp=example.com;uname -a
Management
ISP Premise
Install artifacts

Information Classification: General

#BHEU @BlackHatEvents

## Slide 60

#### **Residential Gateway Security Recommendations for Upstream vendors**

- Solution – Upstream vendors (SoC makers)

- OEMs may utilize SDK with volition

   - Employ secure coding practices

   - Employ defensive programming & ensure program robustness

- Employ SoCs with Secure Boot/TrustZone

- Demonstrate usage correctly in SDK

   - Encrypting flash with LUKS plain-text key is NOT proper encryption

   - Utilize TrustZone for critical cryptographic materials

Information Classification: General

#BHEU @BlackHatEvents

## Slide 61

## **Black Hat Sound Bytes / Takeaways**

RGs and
providers
are unsafe

Treat end-
devices as
hostile

- RGs are lucrative targets, sheer in numbers, yet behind in terms of security.

- End-user device may be studied extensively by anyone. Risk assessment and modern defense options are important.

Supply chain security is difficult

- Supply chain security requires effort

- • SoC vendors needs to prevent misuse & build better documentation

Information Classification: General

#BHEU @BlackHatEvents

## Slide 62

## **Questions?**

```
logonfail
talun_yen@txone.com
```

Special thanks Canaan Kao, TXOne Networks Federico Maggi, Black Hat SCP Whitepaper, disclosure and write-up coming soon – txone.com/blog

Information Classification: General

#BHEU @BlackHatEvents
