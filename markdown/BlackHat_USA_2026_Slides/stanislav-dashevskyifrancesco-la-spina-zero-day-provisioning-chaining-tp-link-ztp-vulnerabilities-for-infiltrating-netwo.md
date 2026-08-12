---
title: "Zero-Day Provisioning Chaining TP-Link ZTP Vulnerabilities for Infiltrating Networks"
speakers: ["Stanislav Dashevskyi", "Francesco La Spina"]
conference: "Black Hat"
conference_full: "Black Hat USA 2026"
edition: "USA"
year: 2026
source_pdf: "BlackHat_USA_2026_Slides/Stanislav Dashevskyi&Francesco La Spina_Zero-Day Provisioning Chaining TP-Link ZTP Vulnerabilities for Infiltrating Networks.pdf"
pages: 47
sha256: "c61da5369f66d3d2a1bd70556b2008345fe9066d6fae56e33dff585d1604e423"
text_chars: 21430
ocr_pages: 13
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:16:31Z"
---
# Zero-Day Provisioning Chaining TP-Link ZTP Vulnerabilities for Infiltrating Networks

**Speakers:** Stanislav Dashevskyi, Francesco La Spina  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/Stanislav Dashevskyi&Francesco La Spina_Zero-Day Provisioning Chaining TP-Link ZTP Vulnerabilities for Infiltrating Networks.pdf` (47 pages)

## Slide 1

# Zero ~~-touch~~ day provisioning **Chaining TP-Link ZTP Vulnerabilities for Infiltrating Networks**

Stanislav Dashevskyi, Francesco La Spina

## Slide 2

##### About us

**Stanislav Dashevskyi Francesco La Spina** Principal Security Researcher Senior Security Researcher

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
About us
Stanislav Dashevskyi Francesco La Spina
Principal Security Researcher Senior Security Researcher
RESEARCH
black hat
2026
```

## Slide 3

### What is ZTP and why should we care?

3

## Slide 4

#### From manual to “zero-touch” provisioning

- On-site installation required: new devices had to be physically configured by an IT technician, one by one

- Slow and error-prone deployments, limited scalability

- Vendors started to automate this process a decade ago…

4

## Slide 5

### Zero-Touch Provisioning (ZTP)

- ZTP is a technology allowing to remotely onboard and provision network devices from a central platform

- Several vendors have started to offer ZTP under different names and using different protocols

- A ZTP system has two main components:

   - **<u>Client devices</u>** : switches, routers, Wi-Fi access points, and gateways that need to be provisioned and managed

   - **<u>Controllers</u>** <u>: dedicated appliances and/or software</u> platforms that provision, configure, monitor, and update client devices

_Taken from support.omadanetworks.com_

5

## Slide 6

### What makes ZTP interesting for security research?

- Not a new concept, but not much previous research done

- It depends on the **<u>strong chain of trust</u>** between controllers and managed devices

   - Centralized management means a single point of failure

   - There is no universal set of ZTP protocols

   - ZTP controllers and devices are trusted by the internal network

Improved usability may compromise security

6

## Slide 7

### TP-Link Omada

Omada is a ZTP ecosystem from TP-Link, tailored for SMEs*

- **<u>Cloud-based</u>** <u>(hosted by TP-Link)</u>

- **<u>Local (on premise) via dedicated hardware Controllers</u>**

- **<u>Local via software Controllers</u>** (Virtual Machine)

- There can be hybrid deployments

_Taken from tplink.com_

_*Small and Medium Enterprises (SMEs)_

7

## Slide 8

### Why choosing Omada?

- **<u>Large but under-researched attack surface</u>** :

   - TP-Link has a large global deployment and customer base

   - Widely adopted ZTP ecosystem (SMB/SME) with <u>limited public security research</u>

   - Past vulnerabilities mostly on clients

- **<u>Rich feature-set for SME</u>**

   - Overall, good hardware and functionalities

   - Easy to deploy and manage

   - Competitive value for money for SMEs (compared with Ubiquiti and Cisco)

8

## Slide 9

## What does ZTP look like in practice?

1. You connect a new Client device to the network 2. The Controller discovers the device

3. You click “Adopt” in the controller UI

4. The Controller adopts (onboards) and provisions the Client

• **But… how does this magic happen?**

9

## Slide 10

### Reverse-engineering Omada protocols

10

## Slide 11

### Where to begin? Client

- We purchased ER7206 and ER605 Omada gateways and downloaded the firmware

- We wanted to install debuggers and packet sniffers – **<u>no root access!</u>**

- Started with static analysis:

   - We looked at the Web UI of Client devices – it was built on **OpenWRT’s LuCi** …

   - We had to figure out the way to **<u>de-obfuscate</u>** the **Lua bytecode** – tough!

- We found:

_Taken from tplink.com_

   - **<u>CVE-2025-7851</u>** <u>: Insufficient patch for the “Leftover</u> debug code” issue found by Cisco Talos (CVE2024-21827)

   - **<u>CVE-2025-7850</u>** <u>: Authenticated OS command</u> injection via Wireguard VPN settings through the Web UI

- We had to release these findings as a separate <u>blogpost</u>

11

## Slide 12

### Where to begin? Controller

- We purchased an **OC200** to use as a **local hardware controller**

- TP-Link also provides a **downloadable software version of the local controller** — Java based!

- Both helped us to analyse the communication protocol between clients and controllers and reverse-engineer the controller software.

_Taken from tplink.com_

12

## Slide 13

### Omada: Message format

- Several custom protocols:

   - UDP and TCP for transport, TLS for encryption

   - − Each message is encoded in a JSON payload, preceded by a 4-byte payload length (network order)

- Several phases: **<u>Discovery, Adopt</u>** , Manage, Reset, Prelink, Rebuilt, and others

- Similarities with different other protocols used by other (non-Omada) TP-Link devices

   - **_“I just wanted to learn the water temperature” by Imre Red, DeepSec’23_**

13

## Slide 14

### Omada: Discovery (Local + Cloud)

- Local discovery is done via UDP (broadcast)

   - Client sends basic information (S/N, MAC addr, model, version, etc.)

   - Controller responds with similar info + the IP/port to be used for Adoption

- Cloud-based discovery is via TCP/TLS

- − Similar info is exchanged, but the client will contact an Omada Cloud host

<u>NOTE: When no local controller is present, Omada</u> devices continue to broadcast Discovery protocol messages… **this will be relevant later**

14

## Slide 15

### Adoption steps (Cloud)

1
2

• Sites are logically separated network locations (different company branches)

**Devices in each site will have shared “site credentials”””**

_Taken from support.omadanetworks.com_

15

## Slide 16

### Omada: Adoption V2

Works over TCP/TLS No substantial differences between Local and Cloud

MSG TYPE

**1.** **<u>During the TLS handshake, only</u>** <u>the client verifies the identity of the Controller</u>

**2.** **<u>Client authenticates with Controller (custom challenge-response)</u>**

   - a) Controller sends a “random” auth challenge

   - b) Client replies with two-round hash of its creds, using the challenge as the salt (2<sup>nd</sup> round)  -> no standard HMAC

**3.** **<u>Controller authenticates with Client</u>**

   - a) Client sends its own “random” challenge

   - b) Controller replies with two-round hash of device creds

4. Next, Controller attempts to read the current config and push the new one

   - a) Primary config: new network settings, “site credentials”… b) Secondary config: modules (Wireguard VPN) and other things c) Client is now adopted

16

## Slide 17

### The vulnerabilities

17

## Slide 18

######

######

- ”Legacy” V1 is present in the latest Clients, can be forced by Controllers

- Asymmetric encryption for auth and session key sharing, symmetric encryption for data

- The asymmetric keys are hardcoded

   - The “public” key is located in Client’s firmware

   - The private key is obfuscated within the Controller’s software

- **<u>CVE-2025-15629</u>** : the session key has insufficient entropy

- Attackers can decrypt traffic and get credentials

**<u>AUTH = username + md5sum(password)</u>**

18

## Slide 19

### Insecure creds in V2 (CVE-2025-9290)

_AUTH _dev = sha256sum(sha256sum(username + md5sum(password)) + randomKeyForDeviceVerify)_

19

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Insecure creds in V2 (CVE-2025-9290)
AUTH _dev = sha256sum(sha256sum(username + md5sum(password)) + randomKeyForDevice Verify)
TCP / SSL
port 28914 Inform json
a randomKeyForDeviceVerify y
AUTH_dev, randomKeyForSystemVeri
Controller
1048576
1048577
AUTH_sys
1048578
1048579 black hat
2026 19
```

## Slide 20

### Insecure creds in V2 (CVE-2025-9290)

_AUTH _dev = sha256sum(sha256sum(username + md5sum(password)) + randomKeyForDeviceVerify)_

20

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Insecure creds in V2 (CVE-2025-9290)
AUTH _dev = sha256sum(sha256sum(username + md5sum(password)) +-rarndemkKeyForDeviceVerify).
rainbow table = {
"94F37F62C8CBOBF792518A11951EFC430620BB982C26454BD3230304157463E8" :
f
“admin/admin",
. "admin21232F297A57A5A743894A0E4A801FC3",
Client
"@2BODE9FACF8DEFA14DB2692076FCF1B3A4E81D4A37B27E898A59CFC55CA462B" :
[
“admin/password12345",
“admin365D38C60C4E98CA5CA6DBC02D396E53",
TCP / SSL
port 28914 "
"92A70A0B2C946194A8C2878B9BAC3BB520A30CD41C4C44D7F7EC363F6F2EB2EB" :
[
Inform json
“admin/Ciccio81",
“admin4778BF96209582FFA15C57F66BB00061",
| [auTH dev, randomKeyForSystemVeri
AUTH_sys
1048577
1048578
1048579
black hat
2026 20
```

## Slide 21

### Insecure creds in V2 (CVE-2025-15544)

21

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Insecure creds in V2 (CVE-2025-155444)
TCP / SSL
port 28914
Inform json
randomKeyForDeviceVerify
AUTH_dev, randomKeyForSystemVerify
AUTH_sys
ACK
Propose new primary contig
Current confie
Primary ca nfig
1048580
black hat
2026 21
```

## Slide 22

### Insecure creds in V2 (CVE-2025-15544)

###### **Controllers do not validate the identify of Clients**

_AUTH _dev = sha256sum(sha256sum(username + md5sum(password)) + randomKeyForDeviceVerifiy)_

22

## Slide 23

### Default credentials (FSCT-2025-008)

- A brand-new Client will always have default credentials (admin/admin)

- If we ”fake” a Controller, we can always know if a Client has default credentials

- If we ”fake” a Client and it gets accepted by a Controller, we can always authenticate

- **<u>You get site credentials “for free"</u>**

admin / admin

23

## Slide 24

### The chain of trust

• The traffic in V2 is encrypted and Clients verify the identity of Controllers (TLS)

• Typical PKI chain of trust: − The **“Root” cert** is self signed and used as Root CA, imported into the keystore of Clients − The **“Intermediate” cert** is signed by the Root and is imported into the Controllers’ trusted keystore − The **”Server” cert** is used by Controllers and Clients for TLS

Root cert

Intermediate cert

Server cert

24

## Slide 25

The broken chain of trust (CVE-2025-15628)

Root cert

- Look at the cert expiration dates... Everything is hard-coded

- Controllers have a hard-coded private key (!) used for TLS (!)

Intermediate cert

- Controllers’ Server cert is enough to pass the identity check -> **<u>we can reuse Controller’s Server certs and private key!</u>**

- Cloud Controllers must present a cert derived from Root/Intermediate with a CN* that ends with “tplinkcloud.com” -> we cannot forge this one 

Server cert

* A certificate common name (CN) is a standard field in an X.509 digital certificate that identifies the primary hostname, domain name, or entity protected by or assigned to the certificate

25

## Slide 26

### Why impersonating Controllers?

- Use Clients as credential oracles

- Get private VPN keys, read other sensitive information, push new settings

- • Also, remember CVE-2025-7850?

   - OS command injection via the Web UI (authenticated!)

26

## Slide 27

## Using fake Controllers to exploit CVE-2025-7850

27

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Using fake Controllers to exploit
CVE-2025-"7850
manage config msg = { TCP/ SSL ;
"header" : { port 28914 Inform json [2]
} “type” = 4096, randomKeyForDeviceVerify 1048576
"body" : { .
me equencelds ay AUTH_dev, randomKeyForSystemVerify 1048577
"userAccount": {
#... AuTHSYS 1048578
}, ACK
"wiregua eo { | 1048579
"interfaces": Propose new primary config | 1048585 |
1048585
{
"id":878491625, Current config
"operation":1, Pri § 1048580
"enable": "true", rimary contig 1048581
"mtu":1420, 1048581 |
"ListenPort":51820, ACK 1048582
"privateKey":" [ARBITRARY OS COMMAND]", Propose new secondary config
"LocalIp":"10.10.10.1" | 1048586 |
}, Secondary confi
"configVersionInc": 1, y g 4096
} we
j black hat
USA
2026 27
```

## Slide 28

### Let’s catch our breath

- We can impersonate Clients and Local Controllers

   - RCE on unconfigured Clients, pivot to the entire site

   - Get site credentials from Clients/Controllers (also with passive traffic analysis)

   - Authenticate -> RCE on Clients

- **<u>What can we do to Controllers?</u>**

- **<u>What about Cloud-based provisioning?</u>**

Local
Controller
Attacker
Attacker
Client

The Conjurer - Hieronymus Bosch

28

## Slide 29

### The broken chain of trust  – Cloud (CVE-2025-9291)

29

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The broken chain of trust —
Cloud (CVE-2025-9291)
__int64 ecs_verifySsl(unsigned int preverify_ok, void* store_ctx) {
"method" : "helloCloud", Q2: {
“params” pi , 03: subject_name_str = strstr(subject_name_buf, "/CN=");
"alias" : "ERGOS", , @4: if ( !subject_name_str )
“authCode" B "[REDACTED]", @5: return 0;
sooo ease vane on” ae 6: cert_subject_name = subject_name_str + 4;
"devi > ae 07: v11 = strchr(subject_name_str + 4, '/');
eviceHwVer : 2.0", Q8: if ( v11 )
"deviceld" : "[REDACTED]", 09: ev11 = 0:
wjevecetae eeroos , a (_strstr(global_controller host, "“tplinkcloud.com") && !strstr(cert_subject_name, "tplinkcloud.com") )
"deviceName" : "ER605" .
"deviceType" : "SMBROUTER", 11728 if ( HIDWORD (qword_5CCB8) )
"fwId" : "", 13: printf (
"fwVer" : "2.2.6 Build 20240718 Rel.82712", 14: "[TECS] [ERROR] %s():%5d @ verify error:CN mismatch(%s), controllerUrl(%s).\n\r",
"hwId" : "[REDACTED]", 15: "_ecs_verifySsl",
"oemId" : "[REDACTED]", 16: 125LL,
"tespVer" : "1.2" 17: cert_subject_name,
18: global_controller_host) ;
20: {
ats)
"error_code" : 0, 22: ecs_log(2LL, "[ECS] [ERROR] <%s>%s():%5d @ verify error:CN mismatch(%s), controllerUrl(%s).\n\r");
"id" : 1, 23:
"result" : 24: }
"cachedSvr" : "n-euwi-device-omada.tplinkcloud.com:443", 25: return 0;
"illegalType” : 0, 26: }
"validTimeOnDevice" : 86400 27: }
}
black hat
2026 29
```

## Slide 30

### The broken chain of trust  – Cloud (CVE-2025-9291)

“Let’s eat, Grandma!” vs “Let’s eat Grandma!”

30

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The broken chain of trust —
Cloud (CVE-2025-9291)
__int64 ecs_verifySsl(unsigned int preverify_ok, void* store_ctx) {
"method" : "helloCloud", Q2: {
"params" pi , 03: subject_name_str = strstr(subject_name_buf, "/CN=");
"alias" : "ERGOS", , @4: if ( !subject_name_str )
“authCode" B "[REDACTED]", @5: return 0;
sooo ease vane on” ae 6: cert_subject_name = subject_name_str + 4;
“devi ai 07: v11 = strchr(subject_name_str + 4, '/');
eviceHwVer H 2.0", Q8: if ( v11 )
"deviceId" : "[REDACTED]", .
"deviceMac” : "[REDACTED]", 02: mL SE nents . ; bands .
"deviceModel" : "ER605", 10: if (_strstr(global_controller host, "tplinkcloud.com") && !strstr(cert_subject_name, "tplinkcloud.com") )
"deviceName" : "ER605", 11: { ;
"deviceType" : "SMBROUTER", a if Ot ae )
"fwid" : "" : prin
"fwVer" : "3.2.6 Build 20240718 Rel.82712", 14: "TECS] [ERROR] %s () :%5d @ verify error:CN mismatch(%s), controllerUrl(%s).\n\r",
"hwId" : "[REDACTED]", 15: "_ecs_verifySsl",
"oemId" : "[REDACTED]", 16: 125LL,
"tespVer" : "1.2" 17: cert_subject_name,
18: global_controller_host) ;
20: 7
21: \
"error_code" : 0, 22: s).\n\r");
"cachedSvr" : "n-euwi-device-omada.tplinkcloud.com:443", 25: et S eat, ran I ! la!
"illegalType” : 0, 26:
"validTimeOnDevice" : 86400 27: }
vs
“Let’s eat Grandma!”
Ne w,
black hat
2026 30
```

## Slide 31

### The broken chain of trust  – Cloud (CVE-2025-9291)

We can use a public IP to bypass the CN check :-}

31

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The broken chain of trust —
Cloud (CVE-2025-9291)
__int64 ecs_verifySsl(unsigned int preverify_ok, void* store_ctx) {
"method" : "helloCloud", Q2: {
“params” pi , 03: subject_name_str = strstr(subject_name_buf, "/CN=");
maltas” 2 “ERGOS", , 04: if ( !subject_name_str )
authCode" : "[REDACTED]", 5: evan) OF
ncontrollerversion" a Q6: cert_subject_name = subject_name_str + 4;
"devi yy ae 07: v11 = strchr(subject_name_str + 4, '/');
eviceHwVer : 2.0", Q8: if ( v11 )
"deviceId" : "[REDACTED]", .
"deviceMac" : "[REDACTED]" 09: *v1l = 0;
"deviceModel" : "ER605", , 10: if (_strstr(global_controller host, "tplinkcloud.com") && !strstr(cert_subject_name, "tplinkcloud.com") )
"deviceName" : "ER605", ii: {
"deviceType" : "SMBROUTER", i728 if ( HIDWORD (qword_5CCB8) )
"fwid" 2 "" 133g printf (
"fwVer" : "2.2.6 Build 20240718 Rel.82712", 14: "[TECS] [ERROR] %s():%5d @ verify error:CN mismatch(%s), controllerUrl(%s).\n\r",
"hwId" : "[REDACTED]", 15: "_ecs_verifySsl",
"oemId" : "[REDACTED]", 16: 125LL,
"tespVer" : "1.2" 17: cert_subject_name,
18: global_controller_host) ;
20: {
ats)
"error_code" : 0, 22: ecs_log(2LL, "[ECS] [ERROR] <%s>%s():%5d @ verify error:CN mismatch(%s), controllerUrl(%s).\n\r");
"id" : 1, 23:
"result" : 24: }
"cachedSvr" : "n-euwi-device-omada.tplinkcloud.com:443", 25: return 0;
"illegalType” : 0, 26: }
"validTimeOnDevice" : 86400 27:
We can use a public IP to bypass
the CN check :-}
black hat
2026 31
```

## Slide 32

### Client enumeration (FSCT-2025-003, FSCT-2025-011)

- When adopting a Client via Cloud all you need to know is the S/N, no proof-of-ownership required

- S/N are sequential, can be retrieved using Omada Cloud API; Client info, **<u>such as model and MAC</u>** , can be inferred from its S/N

- **<u>VERY susceptible to brute-forcing</u>**

32

## Slide 33

### Client hijacking, Cloud Controllers (CVE-2025-15630)

- Client contacts the Default Controller (Discovery phase)

- Default Controller sends the URL of a Regional Controller (Adoption and other phases kick in)

- **<u>Discovery and Adoption phases are not bound to the same ”state machine”</u>**

- **<u>Attackers may start the Adoption phase on Client’s behalf</u>** (don’t even need the Discovery request to arrive!)

   - A “fake” Client will get adopted and appear in the Web UI

   - You can spam Cloud Controllers with fake Clients

33

## Slide 34

Stored XSS in Controller Web UI (CVE-2025-9289)

- The properties of adopted Clients are displayed in the Web UI

- Older version jQuery, calls “eval()” to update the UI with Client’s information

- We couldn’t do much because of restrictive content security policy (CSP)

34

## Slide 35

### Cross-Origin Resource Sharing (CORS) bypass (CVE-2025-9292)

- We checked the CSP of Cloud Controllers

- The Omada Cloud runs on AWS

- There are bits of the default CSP that allow Cross-Site requests to anything hosted on AWS…

35

## Slide 36

### Hippity hoppity your network is our property

36

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
HMippity hoppity your network is our
property
```

## Slide 37

##### Local compromise

**ATTACK SCENARIO:** The attacker is positioned inside of the victim’s local network:

1. <u>Intercept the Discovery request (UDP</u> broadcast) and respond as a fake Controller

2. <u>Forward the Discovery request (modified) to the real Controller, posing as a fake Client</u>

3. The Controller responds to the attacker, who <u>can now Intercept, modify, and forward all</u> comms between the real Controller and the real Client (CVE-2025-15628, CVE-202515544 or CVE-2025-9290)

###### **IMPACT: attacker can**

- Retrieve and modify sensitive information (e.g., device configuration)

- • Take over Clients

37

## Slide 38

38

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
(venv) standash@moria:~/stuff/vr/tplink/xploits$ [|
[tplink] O:vi l:vi 2:bash- 3:bash* "moria" 16:59 13-Jul-26
```

## Slide 39

### External compromise

###### **ATTACK SCENARIO:**

The attacker is positioned outside victim’s network, and exploits the race-condition:

1. Collect MAC addresses (Omada API or just brute-force) to impersonate a notyet-adopted Client

2. Resend the message every 60 seconds. To target 1000 MACs attacker only needs ~17 requests per second -> wait <u>for a device ”adoption”</u>

3. Obtain original device provisioned configuration

4. Exploit the stored XSS/CSP bypass to phish admins and potentially steal Cloud account credentials

- **IMPACT: attacker can**

- Retrieve sensitive information (hashed site-credentials, VPN keys, etc.)

- Through stolen cloud credentials: modify device configurations, modify firewall rules, add VPNs to access internal networks, obtain “site-credentials” from site settings…

39

## Slide 40

40

## Slide 41

### The chain of trust issue is way worse (CVE-2025-9293)

###### • <u>The same chain of trust was used in lots of other TP-Link product families</u>

- Omada, Festa, Tapo, Kasa, VIGI, Android apps…

− E.g. we could <u>sniff credentials from Android</u> TLS connections… <u>apps</u>

|**Aginet**|**2.11.23**|
|---|---|
|**Deco**|3.9.76|
|**Festa**|1.6.9|
|**Kasa**|3.4.101|
|**KidShield**|1.1.19|
|**Omada**|4.24.13|
|**Omada Guard**|1.0.14|
|**Tapo**|3.11.114|
|**Tether**|4.10.42|
|**tpCamera**|3.2.12|
|**VIGI**|2.7.16|
|**Wi-Fi Navi**|1.4.8|
|**WiFi Toolkit**|1.4.2|

41

## Slide 42

### Disclosure and some takeaways

42

## Slide 43

### Disclosure timeline (typical)

Issues are disclosed  Industry standard for  Sometimes, it’s
to vendor fixing bugs complicated…

43

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Disclosure timeline (typical)
»
Issues are disclosed Industry standard for Sometimes, it’s
to vendor fixing bugs complicated...
black hat
2026 43
```

## Slide 44

### Disclosure timeline (this research)

This is how long it
took this time!

44

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Disclosure timeline (this research)
0) 90 120 426
a es
This is how long it
took this time!
black hat
2026 44
```

## Slide 45

### Disclosure timeline (this research)

All issues are remediated (almost)

”FSCT-2025-003 Two more and FSCT-2025First patches FSCT-2025-003 and issues fixed 011 require Plan for all fixes (CVE-2025FSCT-2025-011 will not (CVEsystem-wide arch. (more than 300 7851, CVEget CVE IDs, as they 2025-9292, changes […]”. No days required) have low CVSS scores 2025-7850) CVE-2025patch by, at least, […] and first blog 9293) day 394

45

## Slide 46

### Disclosure timeline (this research)

All issues are remediated (almost)

**13 discovered issues got a CVE (out of 17 reported)**

**The ”default password” issue was not fixed.**

46

## Slide 47

### Takeaways

- <u>For vendors:</u>

   - Cryptography is engineering and not a creative process – follow standards, use proven algorithms, plan your PKI ahead

   - Security through obscurity never works

− Bad design choices can cause serious problems later – e.g. shared vulns affecting many product families: **<u>very loooong patch windows -> users are exposed all this time</u>**

- <u>For users:</u>

   - If you use any ZTP platforms, enable every possible security measure such as MFA, don’t use a default password, rotate passwords & keys frequently, update your devices!

https://www.forescout.com/research-labs-overview/

47
