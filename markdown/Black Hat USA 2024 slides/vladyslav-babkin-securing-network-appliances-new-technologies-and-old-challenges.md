---
title: "Securing Network Appliances New Technologies and Old Challenges"
speakers: ["Vladyslav Babkin"]
conference: "Black Hat"
conference_full: "Black Hat USA 2024"
edition: "USA"
year: 2024
source_pdf: "Black Hat USA 2024 slides/Vladyslav Babkin_Securing Network Appliances New Technologies and Old Challenges.pdf"
pages: 27
sha256: "176e6e9f9b9f5fded5707c088a50110cd8b9a588ffeec56dc2f81ad1a054fc40"
text_chars: 10044
ocr_pages: 3
has_ocr: true
redacted_secrets: 0
ocr_confidence: 87.0
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:43:24Z"
---
# Securing Network Appliances New Technologies and Old Challenges

**Speakers:** Vladyslav Babkin  
**Conference:** Black Hat USA 2024  
**Source:** `Black Hat USA 2024 slides/Vladyslav Babkin_Securing Network Appliances New Technologies and Old Challenges.pdf` (27 pages)


## Slide 1

Securing Network Appliances **:** New Technologies and Old Challenges

**Speaker:** Vladyslav Babkin

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
blackhat —
USA 2024
AUGUST 7-8, 2024
BRIEFINGS
Securing Network Appliances
New Technologies and Old Challenges
Speaker:
Viadyslav Babkin
#BHUSA @BlackHatEvents
```

## Slide 2

## $ whoami

**Vladyslav Babkin (“hotab”)**

- Network & Web Hacker, Web Developer

- Long-time CTF player (team dcua)

- Security Researcher @ Eclypsium

- Twitter: @HotabZero

#BHUSA  @BlackHatEvents

## Slide 3

### **HOW DID NETWORK DEVICES EVOLVE?**

#BHUSA   @BlackHatEvents

## Slide 4

- First Cisco Rootkit

2005

- SYNFUL Knock

- Cisco ROMMON Attack

- Juniper Backdoors

2015

- Vault 7 leak

2017

- FortiOS Vulnerability

- ● Echobot **●** **<u>Solarwinds Attack</u>**

2019

2008

2016

2018

- Operation Cisco Raider

- Shadow Brokers

- VPNFilter Campaign

- Cisco Backdoors

#BHUSA   @BlackHatEvents

## Slide 5

- Fortinet Zero-Day

   - ● Jaguar Tooth Malware ● Zyxel-based Botnet

- Cring Ransomware

- ● Pulse Secure Vulnerability

- ● F5 Vulnerabilities ● SonicWall Vulnerabilities ● Fortinet Attacks

- Volt Typhoon

- **● CISA Directive** ● Citrix Zero-Day

- Akira and Lockbit

● BlackTech ● Cisco Zero-Days 2021 2023 2020 2022 2024

- Citrix Vulnerability

- Pulse VPN Campaign

- Fox Kitten Campaign

- Sophos Zero-Day

- F5 1st 10.0 CVSS

- Netwalker Attacks

- Cyclops Blink

- F5 BI-IP Vulnerability

- Citrix APT Campaign

- FortiGate Zero-Day

   - Ivanti Zero-Days

   - SOHO Router Attacks

   - Fortinet Zero-Day

   - XZ Implant

   - …

- Chinese Attacks

#BHUSA   @BlackHatEvents

## Slide 6

##### Extra Context

- Many attacks have tweet-sized PoC (like CVE-2022-1388)

- Issues are basic web app problems

- Similar problems shared with BMC (Baseboard Management Controller)

Modern devices are in some cases full x86-64 server platforms, so all Server/PC/web app issues apply.

#BHUSA  @BlackHatEvents

## Slide 7

Newly-relevant Threats **We got much more powerful platforms on-board the devices.**

- This means dynamic languages on IoT devices (Lua, PHP, etc) - with their staple problems

- Bigger devices and central management appliances can have databases on them

- Full scale linux… with a single user. Of course, **root** . Everything is root like in the good ol’ times!

- Full set of on-board tools which never get used or cleaned up.

- No automatic updates of OS packages (normally)

#BHUSA  @BlackHatEvents

## Slide 8

Cisco ASA firewall disassembly

F5 BIG-IP device disassembly

#BHUSA  @BlackHatEvents

## Slide 9

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
admin@central-manager : ~$ sysadmin [~]# ls -al /
total 9848 total 16
drwxr-xr-x 17 root root drwxrwxr-x
drwxr-xr-x 17 root root
Lrwxrwxrwx 1 root root
drwxr-xr-x 4 root root
drwxr-xr-x 18 root root drwxr-xr-x
drwxr-xr-x root root drwxr-xr-x
drwxr-xr-x root root drwxrwxr-x
Lrwxrwxrwx root root 7 lib -> drwxrwxr-x
Lrwxrwxrwx root root tS) 1ib32 -> drwxrwxr-x
Lrwxrwxrwx root root 9 1Lib64 -> drwxrwxr-x
Lrwxrwxrwx root root 10 Libx32 -> drwxrwxr-x
root root 16384 drwxrwxr-x
root root 4096 drwxrwxr-x
root root 4096 drwxrwxr-x
root root 8 opt -> dr-xr-xr-x
root root 10013258 platform-upgrade.log -rwxrwxr-x
root root 0 -rwxr-xr-x
root root 4096 —rwxr-xr-x
root root 860 drwxrwxr-x
Lrwxrwxrwx root root 8
drwxr-xr-x root root 4096
drwxrwxrwt root root 280
drwxr-xr-x root root 4096
drwxr-xr-x root root 4096
9 ep root root 130
admin 234 bin
sysadmin sysadmin bkupconf
admin 234 boot
sysadmin sysadmin conf
sysadmin sysadmin dev
sysadmin sysadmin dre
admin 234 etc
admin 234 extlog
admin 234 home
admin 234 info
admin 234 initrd
admin 234 Lib
admin 234 mnt
admin 234 oldroot
sysadmin sysadmin proc
admin 234 redis-server
admin 234 redisrsync
admin 234 redisrsyncconf.sh
admin 234 root
sysadmin sysadmin run
admin 234 savedb_to_conf.sh
admin 234 sbin
sysadmin sysadmin sys
admin 234 tmp -> ./var/tmp
admin 234 usr
sysadmin sysadmin var
drwxr-xr-x
Lrwxrwxrwx
Ce]
a
drwxr-xr-x
drwxrwxrwx
drwxrwxr-x
dr-xr-xr-x
Lrwxrwxrwx
drwxrwxr-x
drwxrwxrwx
N
```

## Slide 10

**Basically, we have Linux boxes from 90s, but in 2k24.**

#BHUSA  @BlackHatEvents

## Slide 11

##### It does not end there

- It is a Linux box with no visibility into it

- The defender only gets a neat control panel

- … Usually, with no details even on running processes.

**Perfect place to set up shop!**

#BHUSA  @BlackHatEvents

## Slide 12

#### **HOW DO [WE] FIX ALL THE DISCUSSED ISSUES?**

#BHUSA   @BlackHatEvents

## Slide 13

## CISA and DARPA’s takes on the issue

● <u>The Urgent Need for Memory Safety in Software Products | CISA</u>

- <u>Eliminating Memory Safety Vulnerabilities Once and For All</u> (DARPA)

● <u>Secure by Design Alert: Eliminating OS Command Injection Vulnerabilities | CISA</u>

#BHUSA  @BlackHatEvents

## Slide 14

## A small side-story

- F5 BIG-IP is an application delivery platform. They provide application orchestration, WAF, TLS orchestration, etc.

- Their platform got hit with things like CVE-2022-1388 in post-solarwinds epoch.

In late 2023, F5 released BIG IP Next - next generation of platform.

- It is intended to be used with centralized management

- And it is a complete rewrite using modern technology.

#BHUSA  @BlackHatEvents

## Slide 15

## k8s and Go to the Rescue

- BIG-IP Next is built using <u>k8s (kubernetes)</u> and <u>Go</u>

- Over 30 microservices in both device and central-manager each

- PostgreSQL with account per pod is in use.

- Hashicorp Vault for credential storage.

- This closely follows **<u>CISA’s goal</u>** for memory safety and isolation.

**It does, in fact, improve security posture of the device**

#BHUSA  @BlackHatEvents

## Slide 16

## Let’s Dig into the Device

- We will be digging into virtual edition devices for simplicity.

- Notably, steps for virtual device and central manager are similar.

- After device setup, researcher can login into admin account from device terminal.

- But what next?

**#BHUSA  @BlackHatEvents**

## Slide 17

## Let’s Dig into the Device

- **kubectl get pods** - will list all running pods.

- **kubectl exec -it mbiq-vault-0 --container=vault -- /bin/sh** - run /bin/sh in a pod

   - _This will not work for Go containers_

   - Software in containers is not running as root.

Containers are not magic, and you can find their contents somewhere on the host. In case of this target, it is

**/var/lib/rancher/k3s/agent/containerd/io.containerd.snapshotter.v1.overlayfs/snapshots**

**#BHUSA  @BlackHatEvents**

## Slide 18

## Gone!

This destroys a whole lot of attack vectors:

- Command Injection is now much harder

- Memory-safe Go: no more easy binary attacks

- No more instant-root

- Less poorly-designed features (thanks to microservices)

**But does it solve all of the issues?**

#BHUSA  @BlackHatEvents

## Slide 19

## No Silver Bullet

- Microservices and inter-device interactions == SSRF (Server-Side Request Forgery) issues.

- Other injections may still exist and be useful (SQL injection for example).

- XSS, IDOR (Insecure Direct Object Reference) issues, validation-related bugs - get no coverage from k8s and Go.

- No solution to automated component freshness.

- This list is not exhaustive.

Let’s see some in practice.

#BHUSA  @BlackHatEvents

## Slide 20

### **EXPLOITATION TIME!**

#BHUSA   @BlackHatEvents

## Slide 21

## Vulnerability Short Descriptions

**CVE Description CVE-2024-21793** An Open Data Protocol (OData) injection vulnerability in the BIG-IP Next Central Manager API. It allows to leak sensitive information (for example admin password hash). Attack will only appear if Lightweight Directory Access Protocol (LDAP) is enabled. **CVE-2024-26026** A SQL injection vulnerability that could be used by attackers to bypass authentication. The vulnerability is present in any device configuration. **No CVE** SSRF vulnerability allows to call any method on specific devices, even if the method should not be callable (like creating and listing device users). **No CVE** Weak bcrypt hash **No CVE** Admin password self-reset w/o current password.

#BHUSA  @BlackHatEvents

## Slide 22

## Exploit Conclusions

- ●Every listed vulnerability falls into a well-known category from OWASP Top 10 - which already provides a ton of recommendations - specifically broken access control, cryptographic fail, injections and SSRF.

- ●Additionally, all of microservices do depend on some libraries for example. If we had a full BOM (bill of materials) of these, it would be easy to verify issues with them as well - software supply chain playbook applies in full.

- ●Modern devices are very very complex, and from this complexity arises a lot of previously-unseen attack surface.

#BHUSA  @BlackHatEvents

## Slide 23

## Takeaways

**Key Takeaway:** Many of the past vulnerabilities could have been prevented with better approach to software engineering, which multiple vendors don’t apply to firmware-level tasks due to lack of standardization.

Haphazard process improvements do in fact help, but don’t cover everything - as seen on the example of BIG-IP Next.

#BHUSA  @BlackHatEvents

## Slide 24

## Vendor Response

F5 only acknowledged the pre-auth vulnerabilities as vulnerabilities. SSRF issue is still not fixed. **Reiterating:** We are in this state due to lack of standards, and vendors can decide that an OWASP Top 10 issue is not an issue if it is post-auth

- **“** _Eclypsium’s findings, for which we did not issue CVEs, cannot be directly leveraged to impact the security of the product and require an attacker to first have highly privileged access. F5 does not consider these to be_ **”**

- _vulnerabilities and therefore did not issue CVEs._

**—F5**

**#BHUSA  @BlackHatEvents**

## Slide 25

## Overall Conclusions

**1.** Isolation and memory safety are good, but won't fix everything. **Even a good example of these concepts applied shows very basic vulnerabilities still present.**

**2.** We need more tools and approaches from the software supply chain playbook applied to firmware

**3.** F5 did actually improve their security by a lot - leading to actual improvements in security. Getting a full host-level code execution exploit will be much more involved than before.

#BHUSA  @BlackHatEvents

## Slide 26

# **Questions?**

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 81/100 on the text kept, 57/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
blackhat — a
USA 2024
Questions?
#BHUSA @BlackHatEvents
```

## Slide 27

# **Thank You!**

#BHUSA   @BlackHatEvents
