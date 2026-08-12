---
title: "firmWar An Imminent Threat to the Foundation of Computing"
speakers: ["Babkin"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2023"
edition: "ASIA"
year: 2023
source_pdf: "Black Hat Asia 2023 slides/AS-23-Babkin-firmWar-An-Imminent-Threat-to-the-Foundation-of-Computing.pdf"
pages: 32
sha256: "92a7e4bc4f0586b795597208bb7ff428f588261ddc8e00d9cbaf363bfd348f5a"
text_chars: 10986
ocr_pages: 4
has_ocr: true
redacted_secrets: 0
ocr_confidence: 88.7
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T01:35:41Z"
---
# firmWar An Imminent Threat to the Foundation of Computing

**Speakers:** Babkin  
**Conference:** Black Hat ASIA 2023  
**Source:** `Black Hat Asia 2023 slides/AS-23-Babkin-firmWar-An-Imminent-Threat-to-the-Foundation-of-Computing.pdf` (32 pages)


## Slide 1

#### firmWar: An Imminent threat to the foundation of computing.

Vladyslav Babkin

#BHASIA   @BlackHatEvents

> Text below was recovered by OCR (confidence 94/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
MAY 11-12
BRIEFINGS
firmWar: An Imminent threat to the foundation of computing.
Viadyslav Babkin
#BHASIA @BlackHatEvents
```

## Slide 2

## $ whoami

##### Vladyslav Babkin

- Network & Web Hacker, Web Developer

- - Long-time CTF player (team dcua)

- - Security Researcher @ Eclypsium

- Twitter: @HotabZero

##### Nate Warfield

- Network Hacker, Security Researcher, WIRED25 2020

- - Director of Threat Research & Intelligence @ Eclypsium

- Twitter/Mastodon: @n0x08

- … and a shoutout to Eclypsium Research!

#BHASIA   @BlackHatEvents

## Slide 3

# What is firmware?

#BHASIA   @BlackHatEvents

## Slide 4

## What is firmware?

#BHASIA   @BlackHatEvents

> Text below was recovered by OCR (confidence 81/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
bisa hat
ASIA 2023
Western Digital.
WD BLUE"
1TB 3D NAND
SATA SSD
solid state DIN?
```

## Slide 5

## Firmware (& Hardware) Supply Chain

#BHASIA   @BlackHatEvents

## Slide 6

## Firmware (& Hardware) Supply Chain

- No visibility into lower-level components by customer.

- The components are highly-privileged by definition.

- Lack of standardization for security of such components, as well as update management.

- Trickle-down effect is magnified many-fold.

#BHASIA   @BlackHatEvents

## Slide 7

### Firmware attacks timeline

#BHASIA   @BlackHatEvents

> Text below was recovered by OCR (confidence 87/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
bisa hat
ASIA 2023
Firmware att
2015-2017
Equation Group & Vault 7 Leaks
Two separate instances led to tools and
techniques for firmware attacks being
leaked to th
public. In 2015 we leamed of
Later in 2017,
we learned of Dark Matter and
One of the first observed malware to attack
the BIOS directly
October
2020
MosaicRegressor
Researchers at Kaspersky disclosed a
new UEFI implant being used in the wild
dubbed MosaicRegres:
has been used in target
9. This implant
ed att
to maintain a persistent foothol
organizations and evade most det
controls while delivering maliciou:
to compromised systems. You can find
more information about
September
2021
FinSpy
longing to the
FinFisher surveillance tookset. Although
researchers have tracked the spy tool since
atleast 2011, the booth
until 2021. You can find our full write-up,
including a video breakdown, of FinSpy
January
2022
MoonBounce
wary and attributed to
josely affliated to the
group, which researchers say is part of the
evading mot
operation
boot process. The end result is malware
stealthy infecting the
of the most recent examples of
malware that “hooks” UEFI at an early stage
to infect all subseqi
indows kerne
otections. You can find our
2018
Russian hacking group Fancy Bear is
found using a UEFI rootkit to install Lojax,
independent of the kemel and operat
Hacking Team had a UEFI rootkit that was
used to maintain persistent access to
target systems. It is believed that this was
installed with physical access, howe
is possible that physical access was not driv
required to implant the malware
UEFI modules
were used). (¥
LoJax
fit system, even a complete wipe of the hard
will not remove
e malware (patched
the LoJack anti-theft
software (also known as Computrace
Trickbot contains
Trickboot
code
read, write, and
erase firmware dubbed Trickboot. This was
ina collaborative research effort
id Intelligence (Advintel
June
2022
Conti Group Found Actively Looking
For Firmware Vulnerabilitie
A bootkit persisting in the EFI System
Partition that can bypass Windows Driver
Signature Enforcement to load its own
unsigned driver. You can find our article on
Leaked chat logs show that the Conti
ransomware group is actively looking for
firmware vulnerabilities, specifically in Intel
ME technologies
an find our discussion of
October
2022
BlackLotus
Researchers observed a UEFI bootkit sold
price tag the sellers claim this
malware can bypass Secure
```

## Slide 8

# What’s new here?

These attacks are becoming easy

#BHASIA   @BlackHatEvents

## Slide 9

## BMC&C

#BHASIA   @BlackHatEvents

## Slide 10

## BMC&C

- RansomEXX IP leak

- A chip as the start of the supply chain

- A chip with remotely accessible APIs

- A chip with very high privileges.

The perfect target!

#BHASIA   @BlackHatEvents

## Slide 11

## Attack Surface

- The chip exposes a few services:

   - Redfish, exposed on port 443/tcp

   - Web UI service, exposed also on port 443/tcp

   - IPMI service, port 623/udp

   - SSH service, port 22/tcp (but - not a full bash shell)

   - UPnP (& other discovery services)

   - A few other services for different features (kvm, snmp, …)

#BHASIA   @BlackHatEvents

## Slide 12

## The vulnerability (CVE-2022-40259)

- It resides in the redfish service, facing port 443.

- It is post-authenticated, but only minimal-level access user is required

- ● Vulnerable code:

#BHASIA   @BlackHatEvents

## Slide 13

## The exploit (CVE-2022-40259)

- Command injection in URL path

- The trick: no urldecoding

- ${IFS}, we choose you.

- … That’s it.

#BHASIA   @BlackHatEvents

## Slide 14

## What does a BMC do, exactly?

- Power the server on, power the server off.

- Update the BIOS

- Monitor system hardware

- Logging, alerting.

- KVM console

- Mount remote media

- Help installing the OS

- Last hope to restore the system

- etc

#BHASIA   @BlackHatEvents

## Slide 15

## What can an attacker do additionally?

- Implant the BIOS

- Smuggle KVM image

- Move across the management network, also attack other BMCs

- Attack the Active Directory

- Deploy malware on the OS (potentially in multiple ways), evade AV/EDR

- Disrupt operation (our demo ;) )

- … (use your imagination)

#BHASIA   @BlackHatEvents

## Slide 16

## Other vulnerabilities

- Default credentials for a UID=0 user (CVE-2022-40242) - same consequences as described above, but **pre-auth** .

- User enumeration via API (CVE-2022-2827)

- Password reset interception (CVE-2022-26872)

- Weak password hashes for Redfish & API (CVE-2022-40258)

#BHASIA   @BlackHatEvents

## Slide 17

## The fallout

- Massive disclosure process

- Many impacted vendors

- Hard to detect vulnerable devices for defenders

- A lot of actually vulnerable devices (millions worldwide?)

- Externally-exposed surface is in thousands of devices

All of the issues exploited are classical web application issues and system misconfigurations.

#BHASIA   @BlackHatEvents

## Slide 18

Is this actually common across the board?

#BHASIA   @BlackHatEvents

## Slide 19

## Enterprise systems (IP KVM)

- Serial to Ethernet

- Passwords displayed in banner

- Passwordless accounts

- Shell scripts as shells

#BHASIA   @BlackHatEvents

## Slide 20

## Security cameras & Cellular routers

- Shellshock (seriously)

- Heartbleed

- Default credentials

- SMB vulnerabilities

#BHASIA   @BlackHatEvents

## Slide 21

## Supply Chain Attacks Affect Everyone

#BHASIA   @BlackHatEvents

## Slide 22

## Takeaways

- Firmware is just a software, as complex and insecure as in the 90s

- Attackers are moving lower in the computing stack

- Level of privileges gained from firmware attacks is not to be underestimated, potentially catastrophic and long-term multi-year impact

- “Install patches” notion is getting outdated, fast

- We need supply chain accountability and standards

- We also need a way to track down components used across the entire supply chain (“SBOM”?)

#BHASIA   @BlackHatEvents

## Slide 23

Questions? You can contact me at: <u>vladiksonic@gmail.com vlad.babkin@eclypsium.com</u> @HotabZero on twitter @hotab on Telegram

#BHASIA   @BlackHatEvents

## Slide 24

# Thanks for attention!

#BHASIA   @BlackHatEvents

## Slide 25

# Extra material

#BHASIA   @BlackHatEvents

## Slide 26

## Meris Botnet

- MikroTiks around the world were used as a backbone for TrickBot delivery, as well as DDoS attacks by Meris Botnet.

- Botnet size is estimated to be ~250k devices (© QRator)

- Per MikroTik blog, a vulnerability (CVE-2018-14847) was exploited to gain remote device access

- Upon further scan, we identified around 300k MikroTik devices vulnerable to at least one critical vulnerability

- What makes the botnet interesting is its nature: It is a _configuration-only_ infection, meaning it stays fully within official router configuration.

#BHASIA   @BlackHatEvents

## Slide 27

## Meris Botnet

Data from December, 2021

#BHASIA   @BlackHatEvents

> Text below was recovered by OCR (confidence 93/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
bisa hat
ASIA 2023
Meris Botnet
Data from December, 2021
Geographic Distribution of Vulnerable MikroTik Devices
Distribution of Vulnerable MikroTik Devices Based on RouterOS Version
```

## Slide 28

## Meris Botnet

- To give a rough understanding of what an attacker can do with just “legal” configuration of the device, we will list some features:

   - Run periodic scripts.

   - Do outgoing HTTP requests

   - Serve files over WebUI

   - Run as a forward proxy (altering the pages in the process) - in fact, we found a few instances of this being used for injecting crypto-mining malware

   - Support multiple VPN protocols and complex routing and firewall schemas

   - In the most recent versions, MikroTiks can also run entire _docker containers_

   - ○ In fact, there are a lot more features…

- Attacker gets a LOT of power tools, which are hard to detect in a complex configuration setting.

- References:

   - <u>https://eclypsium.com/blog/when-honey-bees-become-murder-hornets/</u>

   - <u>https://blog.cloudflare.com/meris-botnet/</u>

#BHASIA   @BlackHatEvents

## Slide 29

## F5 BIG-IP CVE-2022-1388

- When CVE-2022-1388 was disclosed, exploitation almost immediately followed (we detected the attacks within just 5 **days** of disclosure)

- The actors who were targeting the attacks were pursuing different goals. We detected a miner installation, and a backdoor shell. We did not observe destructive behavior on our device, but <u>others did.</u>

#BHASIA   @BlackHatEvents

## Slide 30

## F5 BIG-IP CVE-2022-1388

● We <u>could observe</u> around ~ 15k devices on shodan, and we could collect more intelligence on around 1.1k devices (specifically, their copyright year, which, hopefully, roughly corresponds to release year)

#BHASIA   @BlackHatEvents

## Slide 31

## F5 BIG-IP CVE-2022-1388

- What makes this attack interesting is the speed at which actors started exploiting it, as well as that attackers were likely not nation states and not even large groups, but potentially on the level of a script kiddie too. This is very indicative of the big shift of such vulnerabilities from being just for nation states to being for everyone.

- ● Firmwares are becoming more complex, allowing for more vulnerabilities, as well as are getting more well-researched and more accessible. F5 for example is a normal Linux environment on the inside.

#BHASIA   @BlackHatEvents

## Slide 32

## BlackLotus

- BlackLotus represents the first in-the-wild bootkit that can bypass Secure Boot, by exploiting CVE-2022-21894 in the Windows Bootloader.

- Even though Microsoft has patched the vulnerabilities, it is still possible use BlackLotus by installing a vulnerable bootloader by extra exploits.

- This bootkit is being sold for about $5000 on hacking forums, thus available to everyone.

- This one also indicates a shift in usage of much more complex lower-level issues by attackers. What was limited to nation states, is now usable by common criminals. The process also accelerates: CVE was disclosed in January 2022, and BlackLotus was first (publicly) known in October 2022, which is a relatively short time for such a complex issue to be exploited

#BHASIA   @BlackHatEvents
