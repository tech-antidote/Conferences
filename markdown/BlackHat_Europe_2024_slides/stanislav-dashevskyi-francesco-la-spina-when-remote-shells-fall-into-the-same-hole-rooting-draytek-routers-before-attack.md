---
title: "When (Remote) Shells Fall Into The Same Hole Rooting DrayTek Routers Before Attackers Can Do It Again"
speakers: ["Stanislav Dashevskyi", "Francesco La Spina"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2024"
edition: "Europe"
year: 2024
source_pdf: "BlackHat_Europe_2024_slides/Stanislav Dashevskyi & Francesco La Spina_When (Remote) Shells Fall Into The Same Hole Rooting DrayTek Routers Before Attackers Can Do It Again.pdf"
pages: 41
sha256: "38e9b0fce4761585618a785988a674866737fd5ccc67e52a6f87c39452bf54b4"
text_chars: 17831
ocr_pages: 2
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:52:05Z"
---
# When (Remote) Shells Fall Into The Same Hole Rooting DrayTek Routers Before Attackers Can Do It Again

**Speakers:** Stanislav Dashevskyi, Francesco La Spina  
**Conference:** Black Hat Europe 2024  
**Source:** `BlackHat_Europe_2024_slides/Stanislav Dashevskyi & Francesco La Spina_When (Remote) Shells Fall Into The Same Hole Rooting DrayTek Routers Before Attackers Can Do It Again.pdf` (41 pages)


## Slide 1

# When (Remote) Shells Fall Into The Same Hole: Rooting DrayTek Routers Before Attackers Can Do It Again

Stanislav Dashevskyi, Francesco La Spina

#BHEU @BlackHatEvents

## Slide 2

# **The researchers**

##### **Stanislav Dashevskyi**

##### **Francesco La Spina**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 3

# **PART 1**

# **Motivation and Background**

## Slide 4

# **It’s rough around the edges**

- Last year we did research on Sierra Wireless gateways and found critical vulnerabilities

- We also looked at firmware of five different IoT/OT edge routers and it did not look good…

- … **lack of binary hardening, outdated software components, known vulnerabilities** , **“custom” security patches** , **default credentials** …

- **Edge devices serve the threat actors as perfect entry points into businesses**

Edge Router

- https://www.techtarget.com/searchnetworking/definition/edge-router

**You are here**

Information Classification: General

#BHEU @BlackHatEvents

4

## Slide 5

# **It’s rough around the edges (continued)**

- We have chosen a vendor, a seemingly **bullet-proof target with lots of past research** - **DrayTek**

- > 4 years of active patching and frequent security advisories

- With proven interest from threat actors

- **Remote unauthenticated root on the host OS via a trivial buffer overflow in the guest…**

- **And it took us about a month to do it**

Edge Router

- https://www.techtarget.com/searchnetworking/definition/edge-router

**You are here**

Information Classification: General

#BHEU @BlackHatEvents

5

## Slide 6

# **What’s DrayTek?**

- A well-known **Taiwanese** manufacturer of networking equipment and management systems ( **founded in 1997** )

- From **simple SOHO routers** to **complex VPN concentrators** used by businesses

Information Classification: General

#BHEU @BlackHatEvents

6

## Slide 7

# **Why DrayTek? Researchers like it**

- **13** security advisories **since 2018** (excluding ours) with over **100** historical **CVEs**

- Typically, a sign of a mature security team. Yet, new findings keep popping up

- **Emulate it until you make it! Pwning a DrayTek Router before getting it out of the box – Philippe Laulheret. HEXACON (2022).**

- **Detecting persistent threats on DrayTek devices – Octavio Gianatempo, Gastón Aznarez. DEF CON 32 (2024)**

Information Classification: General

#BHEU @BlackHatEvents

7

## Slide 8

# **Why DrayTek? Threat actors love it**

- In 2018, threat actors changed DNS settings on DrayTek routers using a zero-day vulnerability ( **CVE-2018-20872** )

- **CVE-2020-8515** was exploited by Chinese APTs — as part of the **ZuoRAT** malware campaign

- In 2022-2023, some end-of-life DrayTek Vigor routers were targeted by the Chinese malware **HiatusRAT**

- Around the same time, DrayTek devices were targeted by another threat actor known as **Volt Typhoon** .

- Sept. 2024, the FBI announced it had taken down a botnet exploiting three historical CVEs on DrayTek assets ( **CVE2023-242290** , **CVE-2020-15415** , and **CVE-2020-8515** )

Information Classification: General

#BHEU @BlackHatEvents

8

## Slide 9

# **Why DrayTek? Just look at the numbers**

Over 400K expose
admin interface
(WebUI)

Information Classification: General

#BHEU @BlackHatEvents

9

## Slide 10

# **Why DrayTek? More about the exposure**

##### The ISP networks with the largest concentrations of DrayTek devices (Censys*):

|**ASN**|**AS_Name**|**Organization**|**Country**|**Scale**|**Host Count**|
|---|---|---|---|---|---|
|3462|HINET Data Communication
Business Group|**HINET**|**Taiwan**|Major ISP|**41,969**|
|31655|ASN-GAMMATELECOM|**Gamma Telecom**|**U.K.**|Significant Telecom
Provider|**35,866**|
|2856|BT-UK-AS BTnet UK
Regional network|**British Telecommunications**|**U.K.**|Major ISP|**31,959**|
|45899|VNPT-AS-VN VNPT Corp|**Vietnam Posts and**
**Telecommunications Group**|**Vietnam**|Major ISP|**31,561**|
|5413|AS5413|**Daisy Communications**|**U.K.**|Significant Telecom
Provider|**21,275**|
|13037|ZEN-AS Zen Internet – UK|**Zen Internet**|**U.K.**|Medium-sized ISP|**13,147**|
|18403|FPT-AS-AP FPT Telecom
Company|**FPT Telecom**|**Vietnam**|Major ISP|**12,132**|
|7552|VIETEL-AS-AP Viettel Group|**Viettel Group**|**Vietnam**|Major ISP|**11,756**|
|1136|KPN KPN National|**KPN**|**Netherlands**|Major ISP|**9,921**|
|3320|DTAG Internet service
provider operations|**Deutsche Telekom AG**|**Germany**|Major ISP|**7,732**|

* https://community.censys.com/censys-rapid-response-37/censys-rapid-response-exposed-draytek-vigor-routers-cve-2024-41592-189

Information Classification: General

#BHEU @BlackHatEvents

10

## Slide 11

# **Why did we do it? Well…**

- We typically look at devices / software overlooked by others – better ROI for us

- **Several critical RCEs** and command injections found **between 2020 and 2023**

- Seems like **a lot of patching** has been already done

- • **Can we possibly find any more issues? Would**

- **attackers still be firing at the same target?**

Information Classification: General

#BHEU @BlackHatEvents

11

## Slide 12

# **Which device to look at?**

- DrayTek offers different kinds of devices: from simple bare-metal routers that run RTOS, to **complex security appliances**

- **_Modern routers are mini-servers_** * - lots of resources, Linux, virtualization support…

- Rich OS features enable LOTL** techniques, and VMs backfire*** if not done right

DrayTek Vigor 3910 / 3912

- **A vulnerability in a complex and popular device** -> largest ROI for threat actors

   - Securing Network Appliances: New Technologies and Old Challenges – Vladyslav Babkin, BHUSA 2024

   - ** People’s Republic of China State-Sponsored Cyber Actor Living off the Land to Evade Detection – CISA advisory, 2023

   - *** Debug7: Leveraging a Firmware Modification Attack for Remote Debugging of Siemens S7 PLCs – Eyal Semel et al., BHASIA 2024

Information Classification: General

#BHEU @BlackHatEvents

12

## Slide 13

# **“Simple” routers**

- Typically, routers are hardware boxes

- They run some kind of **embedded Linux distribution** , adding **some custom binaries to implement additional functionality**

- Everything runs as **root** , exploits can be devastating

- New generation of routers started to use virtualization (since 2010, Cisco and Juniper)

Information Classification: General

#BHEU @BlackHatEvents

13

## Slide 14

# **“Complex” routers: Vigor 3910 / 3912**

- The hardware box runs **Ubuntu Linux 22.04** (aarch64)

- All DrayTek devices run on a proprietary OS - **DrayOS**

- On more complex Vigor devices **DrayOS runs in a VM** , while the host OS is Ubuntu 22.04

- Virtualization is supposed to add a layer of security and to ensure reliability (it restarts super fast after an error condition)

- **This looks great, but how is that REALLY implemented?**

Information Classification: General

#BHEU @BlackHatEvents

14

## Slide 15

# **PART 2 Our Findings**

#BHEU @BlackHatEvents

## Slide 16

# **Overview of findings**

#### **14 vulnerabilities from different types/classes***

Credential
reuse

Weak
encryption

Copy-paste
code
Bad input
Buffer overflows
sanitization
(DoS/RCE)

Copy-paste code

- Unforgivable vulnerabilities – Steve Christey, The MITRE Corporation (2007).

Information Classification: General

#BHEU @BlackHatEvents

16

## Slide 17

**Getting started Start WebUI**

**Exploit**

Root

- The firmware is available online, but it’s encrypted

- We built upon the research** from 2 years* ago to **decrypt the firmware for 3910**

- We could only buy **3912** for our lab, but could not decrypt the firmware (yet)

- DrayOS is huge, so we started with **WebUI** – web-based admin’s panel

- **There is a single set of admin credentials used for the**

- **entire device :** WebUI, telnet over SSH, even the host OS

- Emulate it until you make it! Pwning a DrayTek Router before getting it out of the box – Philippe Laulheret. HEXACON (2022).

- ** CataLpa’s writeup (2024): https://wzt.ac.cn/2024/02/19/vigor_3910/?_x_tr_hist=true

Information Classification: General

#BHEU @BlackHatEvents

17

## Slide 18

# **WebUI**

Start

**WebUI**

Exploit

Root

- A standard admin Web-interface used to configure and manage the device

- **<u>MUST NOT</u> be exposed to the Internet** , but oh well…

- One of the critical issues discovered in the recent past had to do with the login form, so we decided to have a closer look at WebUI

Information Classification: General

#BHEU @BlackHatEvents

18

## Slide 19

### **First look at the WebUI: input validation issues**

Start

**WebUI**

Exploit

Root

Information Classification: General

#BHEU @BlackHatEvents

19

## Slide 20

# **Credentials are not safe**

Start **WebUI**

Exploit

Root

- **The same admin credentials are used across the entire system**

- **They don’t enforce TLS (HTTPS)**

- When logging into WebUI, credentials are transmitted in cleartext (HTTP)

- But if we use TLS (HTTPS), everything is fine, right?

**Username and password are base64- and url-encoded**

Information Classification: General

#BHEU @BlackHatEvents

20

## Slide 21

**Credentials are not safe (continued)** Start **WebUI** Exploit Root

Exploit

- **TLS is only secure if there is sufficient entropy** for generating private keys

- It’s notoriously **difficult to have proper sources of entropy in embedded systems** *

- **PRNG must be seeded with a sufficiently ra** **nd om value** ,

- Otherwise, the output of the PRNG may be guessed

- TL;DR, RFC1075 says if you can do that, it may be **feasible to recover private keys and break TLS encryption**

> ***** Wheel of Fortune. Analyzing Embedded OS Random Number Generators – Ali Abbasi and Jos Wetzels. CCC (2016)

Information Classification: General

#BHEU @BlackHatEvents

21

## Slide 22

# **Credentials are not safe (continued)**

Start **WebUI**

Exploit

Root

- We found that **deprecated OpenSSL API** is used (both TLS and VPN)

- The **PRNG** was indeed seeded with **a “random” value** , but **not the one you’d expect** …

* https://xkcd.com/221/

Information Classification: General

#BHEU @BlackHatEvents

22

## Slide 23

# **Buffer overflows… lots of them**

Start **WebUI**

Exploit Root

- WebUI contains **around 100 static web-pages**

- **Almost every of them had a buffer overflow**

- Too many to document, so we had to divide them into clasess

- (Semi-) c **ontrolled writes** into .bss, **Denial-of-Service** of different kinds, **potential RCE**

Information Classification: General

#BHEU @BlackHatEvents

23

## Slide 24

## **Conflict of interests: researchers vs threat actors**

Start **WebUI**

Exploit

Root

- At this point we were still at an early stage of our research

- Only a bunch of buffer overflows, and still lots of components and functionality to explore

- “[ **Stack smashing** ] **is a dying artform, as things move further away from bare metal into virtualized environments** ” ©

- But we are researchers, **threat actors** don’t limit themselves to novel vulnerabilities, they **want results and fast**

- So our main research question became: “ **How fast can mess it all up with what we already have?** ”

- Enter the **CVE-2024-41592**

Information Classification: General

#BHEU @BlackHatEvents

24

## Slide 25

**CVE-2024-41592: stack buffer overflow** Start WebUI **Exploit** Root

- Most web-pages call a special **function that parses the query string parameters**

- The **destination buffer** that contains pointers to parameters is allocated on the stack and **has fixed length**

- **There are no checks** whether the buffer can fit an arbitrary long list of parameters

- **The bug can be triggered via** requesting almost **every page** , causing **indirect arbitrary writes into the stack**

param
query string  parameters
separator
separator
param1  param1  param2  param2
key value key value

Information Classification: General

#BHEU @BlackHatEvents

25

## Slide 26

# **CVE-2024-41592 (continued)**

Start WebUI

**Exploit**

Root

- The query string parameter keys and values are allocated on the heap

- **The pointers to keys/values are stored**

- **on the stack**

- **Pointers and function addresses are**

- **only 4 bytes only (aarch64 in 32-bit mode)**

Information Classification: General

#BHEU @BlackHatEvents

26

## Slide 27

# **Can we exploit it?**

Start WebUI

**Exploit**

Root

- The main binary is called “sohod64.bin” – this is literally the whole DrayOS, including WebUI

- Runs via a modified QEMU executable

- aarch64 (but runs in 32-bit mode)

- No DEP (executable heap and stack)

- No stack canaries

- No PIE,  No ASLR

- **A completely “flat” binary that has everything we**

- **need and no binary hardening whatsoever**

Information Classification: General

#BHEU @BlackHatEvents

27

## Slide 28

# **Some challenges**

Start WebUI

**Exploit**

Root

- We stumbled upon **unexpected challenges** :

- (1) **almost every web page requires auth token** ;

- (2) **the FreeCtrlName() function**

Information Classification: General

#BHEU @BlackHatEvents

28

## Slide 29

# **Some challenges (continued)**

Start WebUI

**Exploit**

Root

- FreeCtrlName() is a **chain free** , it stops when it encounters a NULL

- After looking long and hard (a couple of hours)…

- **We found a web page** that:

- (a) **did not require the auth token** to process the query string

- (b) had **a local variable just below the return address initialized to zero**

**A local variable initialized to zero**

Information Classification: General

#BHEU @BlackHatEvents

29

## Slide 30

# **1337 Sh311c0d3**

Start WebUI

**Exploit**

Root

#### **GET /cgi-bin/[vulnerable].cgi?[&&&… &&&] [SHELLCODE][MSG] HTTP/1.1 […]**

**Address of [MSG] Address of “printf()” Next return address Call “printf()”**

Information Classification: General

#BHEU @BlackHatEvents

30

## Slide 31

# **Let’s do something useful**

Start WebUI

**Exploit**

Root

- **Remember, we are still in the VM,** so we can’t pop a root shell

- We can still do something useful, it’s a “flat” binary

- DNS hijacking, altering settings, defacement, takeover

- Let’s use very similar shellcode, but instead of printing a message, we change a certain string…

**We are still here**

Information Classification: General

#BHEU @BlackHatEvents

31

## Slide 32

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ =D Vigor Login Page x | + v - a.
€ Cc O & 192.168.1.1/weblogin.htm 170% jy =
Username
|
Password
Language
Vigor3910 English y
Copyright © 2024 DrayTek Corp
```

## Slide 33

# **But the title said “remote shells”!**

Start WebUI

Exploit

**Root**

- Past research* mentioned a **function that calls OS commands** , but no details

- We found a binary on the host OS that “listens” to requests from the guest

- The guest sends a “reboot” request when it needs to be rebooted, or “set_linux_time” for setting the time, etc…

- The commands are whitelisted, so game over, attackers

- Emulate it until you make it! Pwning a DrayTek Router before getting it out of the box – Philippe Laulheret, HEXACON 2022.

???

Information Classification: General

#BHEU @BlackHatEvents

33

## Slide 34

# **Meet CVE-2024-41585**

Start WebUI

Exploit

**Root**

**We’ve escaped the VM!**

**[proto]://[ip]/cgi-bin/[vulnerable-cgi-page].cgi?** &&&&....&&&& **[shellcode]%20set_linux_time%20%3B[ARBITRARY_OS_COMMAND]%3B**

Information Classification: General

#BHEU @BlackHatEvents

34

## Slide 35

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
(venv) standash@thelab42-2:~/stuff/vr/draytek/exploits$
standash@thelab42-2:~/stuff/vr/draytek/exploits$ nc -1 192.168.42.1 1234]
"thelab42-2" 11:53 04-dec-24
```

## Slide 36

# **PART 3 Outlook and Conclusions**

#BHEU @BlackHatEvents

## Slide 37

# **A few notes on patches**

- It is uncertain if the **“VM escape”** issue was already found by Philippe or is a different issue

- We had not bandwidth to document all the buffer overflows, so **we reported several classes of them**

- Vendor came back quickly with the patches, but **we are uncertain whether the fixes apply only to those reported examples**

- **Another advisory with similar buffer overflows published on the same day,** could be a coincidence…

Information Classification: General

#BHEU @BlackHatEvents

37

## Slide 38

# **A few notes on patches (continued)**

- **OS command injection (CVE-2020-8515):** actively exploited by threat actors, patched several years ago, only affects EoS models

- On 21<sup>st</sup> **of October 2024 a researcher* publishes 22 (!)** variants of the same bug

- **The root cause is very similar to the “VM escape” bug** we just presented

- **Looks like no one performed variant**

- **analysis**

*https://github.com/fu37kola/cve/blob/main/DrayTek/Vigor3900/1.5.1.3/DrayTek_ Vigor_3900_1.5.1.3.pdf

Information Classification: General

#BHEU @BlackHatEvents

38

## Slide 39

# **Recommendations to asset owners**

- **<u>Take any kind of administrative tools off the Internet</u>** , **<u>install updates often</u>**

- If you own a business that relies on these devices, **<u>perform independent security assessments</u>**

- **Don’t rely on the number of historical CVEs to**

- **understand the vendor’s security posture**

- Instead, **<u>use security advisories to your advantage</u>** :

1. Check if the same issues keep popping up over the years

2. No vulns and advisories – this is even more suspicious

*https://www.flickr.com/photos/fastjack/282707058

Information Classification: General

#BHEU @BlackHatEvents

39

## Slide 40

# **Recommendations to vendors**

- When you read about threat actors targeting your devices, **<u>make some positive changes to their security</u>**

- **<u>Firmware encryption does not prevent scrutiny</u>** (a.k.a “security by obscurity”)

- / **<u>audit the code /</u>** hire

- • Use **<u>static analysis tools pentesters</u>**

- Don’t patch only the issues reported by the researchers, **<u>do variant analysis</u>**

- **<u>Binary hardening</u>** is not a silver bullet, yet, why not **<u>use</u>** it?

•

- **If software starts to resemble Swiss cheese – consider a complete redesign/reimplementation**

Information Classification: General

#BHEU @BlackHatEvents

40

## Slide 41

# **Thank you! Any questions?**

**<u>stanislav.dashevskyi@forescout.com francesco.laspina@forescout.com</u>**
