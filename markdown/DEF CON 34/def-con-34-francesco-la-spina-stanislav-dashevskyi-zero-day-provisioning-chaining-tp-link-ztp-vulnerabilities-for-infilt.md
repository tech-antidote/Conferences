---
title: "Zero-Day Provisioning Chaining TP-Link ZTP Vulnerabilities for Infiltrating Networks"
speakers: ["Francesco La Spina", "Stanislav Dashevskyi"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: null
source_pdf: "DEF CON 34/DEF CON 34 - Francesco La Spina, Stanislav Dashevskyi - Zero-Day Provisioning Chaining TP-Link ZTP Vulnerabilities for Infiltrating Networks - v1.pdf"
pages: 47
sha256: "28441939a9a0a58a416d3881401499ccabc6ca302c7865dc66c80271f637f826"
text_chars: 16739
ocr_pages: 7
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:16:29Z"
---
# Zero-Day Provisioning Chaining TP-Link ZTP Vulnerabilities for Infiltrating Networks

**Speakers:** Francesco La Spina, Stanislav Dashevskyi  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Francesco La Spina, Stanislav Dashevskyi - Zero-Day Provisioning Chaining TP-Link ZTP Vulnerabilities for Infiltrating Networks - v1.pdf` (47 pages)


## Slide 1

```
Zero-touchday provisioning:
Chaining TP-Link ZTP Vulnerabilities for Infiltrating
Networks
```

```
Stanislav Dashevskyi, Francesco La Spina
```

## Slide 2

# `About us`

- **Stanislav Dashevskyi** , Principal Security Researcher

- **Francesco La Spina** , Senior Security Researcher

2

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
About us
* Stanislav Dashevskyi, Principal Security Researcher
* Francesco La Spina, Senior Security Researcher
<) FORESCOUT
RESEARCH  VEDERE LABS
```

## Slide 3

```
What is ZTP?
And why should we care?
```

## Slide 4

# `From manual to “zero-touch” provisioning`

- On-site installation required: new device had to be physically configured by an IT technician, one by one

- Slow and error-prone deployments, limited scalability

- • ZTP introduced more than a decade ago to solve these issues…

4

## Slide 5

# `Zero-Touch Provisioning (ZTP)`

- ZTP is a technology allowing to remotely onboard and provision network devices from a central platform

- Several vendors have started to offer ZTP under different names and using different protocols

- A ZTP system has two main components:

   - **<u>Client devices</u>** <u>: switches, routers, Wi-Fi access</u> points, and gateways that need to be provisioned and managed

   - **<u>Controllers</u>** <u>: dedicated appliances and/or</u> software platforms that provision, configure, monitor, and update client devices

_Taken from support.omadanetworks.com_

5

## Slide 6

# `What makes ZTP interesting for security research?`

- Not a new concept, but not much previous research done

- It depends on the **<u>strong chain of trust</u>** between controllers and managed devices

   - Centralized management means a single point of failure

   - There is no universal set of ZTP protocols

   - ZTP controllers and devices are trusted by the internal network

Improved usability may compromise security

6

## Slide 7

# `TP-Link Omada`

- Omada is a ZTP ecosystem from TP-Link, tailored for SMEs

   - **<u>Cloud-based</u>** <u>(provided by TP-Link)</u>

   - • **<u>Local via dedicated hardware Controllers</u>** (a device sold by TP-Link)

   - • **<u>Local via software Controllers</u>** (Virtual Machine)

   - There can be hybrid deployments

_Taken from tplink.com_

7

## Slide 8

# `Why choosing Omada?`

- **<u>Large but under-researched attack surface</u>** :

   - TP-Link has a large global deployment and customer base

   - Widely adopted ZTP ecosystem (SMB/SME) with <u>limited public security research</u>

   - • Past vulnerabilities mostly on clients

- **<u>Reach feature set for SME</u>**

   - Overall, good hardware and functionalities

   - Easy to deploy and manage

   - Competitive value for money for SMEs (compared with Ubiquiti and Cisco)

8

## Slide 9

# `What does ZTP look like in practice?`

1. You connect a new Client device to the network

2. The Controller discovers the device

3. You click “Adopt” in the controller UI

4. The Controller adopts (onboard) and provisions the Client

- **But… how does this magic happen?**

9

## Slide 10

```
Reverse-engineering
Omada protocols [[:......:]]
```

## Slide 11

# `Where to begin? Clients`

- Purchased ER7206 and ER605 Omada gateways and downloaded the firmware

- We wanted to install debuggers and packet sniffers – no root access!

- Started with static analysis:

   - We looked at the WebUI of Client devices – it was built on OpenWRT’s LuCi…

   - We had to figure out the way to **<u>de-obfuscate</u>** the Lua bytecode – tough!

- We found:

   - **<u>CVE-2025-7851</u>** <u>: Insufficient patch for the “Leftover debug</u> code” issue found by Cisco Talos (CVE-2024-21827)

   - **<u>CVE-2025-7850</u>** <u>: Authenticated OS command injection via</u> Wireguard VPN settings through the Web UI

_Taken from tplink.com_

- Had to release these findings as a separate blogpost

11

## Slide 12

# `Where to begin? Controllers`

- We purchased an **OC200** to use as a **local hardware controller**

- TP-Link also provides a **downloadable software version of the local controller** — Java based!

- Both helped us to analyze the communication protocol between clients and controllers and reverse-engineer the controller software.

_Taken from tplink.com_

12

## Slide 13

# `Omada: message format`

- Several custom protocols

   - UDP and TCP for transport, TLS for encryption

   - • Each message is encoded in a JSON payload, preceded by a 4- byte payload length (network order)

- Several phases: **Discovery, Adopt** , Manage, Reset, Prelink, Rebuilt, and others

- Similarities with different other protocols used by other (non-Omada) TP-Link devices

• **_“I just wanted to learn the water temperature” by Imre Red, DeepSec’23_**

13

## Slide 14

# `Omada: Discovery (Local and Cloud)`

- Local discovery is done via UDP (broadcast)

   - Client sends basic information (S/N, MAC addr, model, version, etc.)

   - Controller responds with similar info + the IP/port to be used for Adoption

- Cloud-based discovery is via TCP/TLS

   - Similar info is exchanged, but the client will contact an Omada Cloud host

- **<u>NOTE</u>** : After a successful “pairing” with a Controller, a Client will resend a Local Discovery message under specific failure conditions…this will be relevant later

14

## Slide 15

2

# `Adoption steps (Cloud)`

1

- Sites are logically separated network locations (different company branches)

- • **<u>Devices in each site will have shared</u> “site credentials”**

15

## Slide 16

# `Omada: Adoption V2`

- Works over TCP/TLS

- No substantial differences between Local and Cloud

**1.** **<u>During the TLS handshake, only</u>** <u>the client verifies the identity of the Controller</u>

**2.** **<u>Client authenticates with Controller (custom challengeresponse)</u>**

   - a) Controller sends a “random” auth challenge

   - b) Client replies with two-round hash of its creds, using the challenge as the salt (2<sup>nd</sup> round)  -> no standard HMAC

- **<u>Controller authenticates with Client</u>**

- **3.**

   - a) Client sends its own “random” challenge

   - b) Controller replies with two-round hash of device creds

4. Next, controller attempts to read the current config and push the new one

   - a) Primary config: new network settings, “site credentials”… b) Secondary config: modules (Wireguard VPN) and other things

   - c) Client is now adopted

16

## Slide 17

```
The vulnerabilities
};-/
```

## Slide 18

# `Hardcoded crypto in V1 (CVE-2025-15627)`

- There is a “legacy” V1, and it can be “forced”

- • The public/private keypair in Omada V1 is hardcoded

- • The public key is located in Client’s firmware

- • The private key is obfuscated within the Controller’s software

- **<u>CVE-2025-15629</u>** <u>: the session key has insufficient</u> entropy

- Attackers can decrypt traffic and force Controllers to leak password hashes

- **<u>AUTH = username + md5sum(password)</u>**

18

## Slide 19

# `Insecure creds in V2 (CVE-2025-9290)`

**_AUTH _dev = sha256sum(sha256sum(username + md5sum(password)) + randomKeyForDeviceVerify)_**

19

## Slide 20

# `Insecure creds in V2 (CVE-2025-9290)`

**_AUTH _dev = sha256sum(sha256sum(username + md5sum(password)) +_** **_~~randomKeyForDeviceVerify)~~_**

20

## Slide 21

# `Insecure creds in V2 (CVE-2025-15544)`

21

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Insecure creds in V2 (CVE-2025-15544)
Controller
TCP / Inform json
SSL
port 28914 randomKeyForDeviceVerify
1048576
AUTH_dev, randomKeyForSystemVerify
1048577
AUTH_sys
1048578
ACK
1048579
Propose new primary config
Current config
21
```

## Slide 22

# `Insecure creds in V2 (CVE-2025-15544)`

###### **_AUTH _dev = sha256sum(sha256sum(username + md5sum(password)) + randomKeyForDeviceVerify)_**

(!) Controllers do not
validate the identity of
Clients

22

## Slide 23

# `Default credentials (FSCT-2025-008)`

- A brand-new Client will always have default credentials

- We can always know if a Client has default credentials

- We can always go further down the protocol state with a Controller without having any creds

- **<u>If you convince a Controller to adopt a fake Client – you get site credentials for free</u>**

admin / admin

23

## Slide 24

# `The chain of trust`

- How is the traffic encrypted? How do Clients verify the identify of Controllers?

Root cert

   - TLS certificate checks

- The “Root” cert is self signed and used as Root CA, imported into the keystore of Clients

- The “Intermediate” cert is signed by the Root and is imported into the Controllers’ trusted keystore

- • The ”Server” cert is used by Controllers and Clients for TLS

Intermediate cert

Server cert

24

## Slide 25

# `The broken chain of trust (CVE-2025-15628)`

- Server certs are to expire in 2051 (!)

- Everything is hard-coded, including private keys of Server certs

Root cert

- Clients will allow Local Controllers that present ANY certificate derived from Root/Intermediate -> **<u>we can reuse existing Server certs!</u>**

Intermediate cert

- Clients will allow Cloud Controllers that present a certificate derived from Root/Intermediate with a CN that ends with “tplinkcloud.com” -> we cannot forge those 

Server cert

25

## Slide 26

# `Why impersonating Controllers?`

- Push VPN configs or leak private VPN keys and other sensitive information

- • Also, remember CVE-2025-7850?

   - Authenticated OS command injection via the UI (Wireguard settings)

26

## Slide 27

## `Using fake Controllers to exploit CVE-2025-7850`

27

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Using fake
Controllers to exploit CVE-2025-7850
manage config msg = {
"header" : {
"type" : 4096,
},
"body" : {
"sequenceld": 4,
"userAccount": {
2 000
L
Ja
"wireguard": {
"interfaces":
=
at
|
"id":878491625,
"operation":1,
"enable": "true",
"mtu":1420,
"ListenPort":51820,
"privateKey":"[ARBITRARY OS COMMAND]",
"Tocaltip’: 10.10.10...
]
So
"“configVersionInc": 1,
TCP /
Inform json
Controller
SSL
port 28914
randomKeyForDeviceVerify
1048576
AUTH_dev, randomKeyForSystemVerify
1048577
AUTH_sys
1048578
ACK
Propose new primary config
1048579
1048585
Current config
1048580
Primary config
1048581
ACK
1048582
Propose new secondary config
1048586
ACK (last cfg result)
=X
Secondary config
4096
N
N
```

## Slide 28

# `Let’s catch our breath`

##### • We can impersonate Clients and Local Controllers

   - RCE on unconfigured Clients

   - Get site credentials from Clients/Controllers (also with passive traffic analysis)

   - Authenticate -> RCE on Clients, pivot to the entire site

- **<u>What can we do to Controllers?</u>**

- • **<u>Specifically, Cloud Controllers?</u>**

Local
Controller
Attacker
Attacker
Client

The Conjurer - Hieronymus Bosch

28

## Slide 29

### `The broken chain of trust - Cloud (CVE-2025-9192)`

29

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The broken chain of trust - Cloud (CVE-2025-9192)
"id" : 1,
"method" : "helloCloud",
"params"
"alias" : "ER605",
"“authCode" : "[REDACTED]", : sub trstr( t_name_buf
"cloudUserName" : "", 4 .
"controllerVersion an
"deviceHwVver" : "2.0",
"deviceId" : "[REDACTED]",
"deviceMac" "[REDACTED]",
"deviceModel" : "ER605",
"deviceName" : "ER605",
"deviceType" : "SMBROUTER",
"fwid" : "",
"fwver" : "2.2.6 Build 20240718 Rel.82712",
"hwId" : "[REDACTED]",
"oemId" : "[REDACTED]",
"tcspVer" : "1.2"
"error_code" : 0,
"id" : 1,
"result"
"cachedSvr" : "n-euwi-device-omada.tplinkcloud.com:443",
"illegalType" "0;
"validTimeOnDevice"” : 86400
29
```

## Slide 30

### `The broken chain of trust - Cloud (CVE-2025-9192)`

”Let’s eat, Grandma!” VS “Let’s eat Grandma!”

30

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The broken chain of trust - Cloud (CVE-2025-9192)
(unsigned int prev
"id" : 1,
"method" : "helloCloud",
"params"
"alias" : "ER605",
"“authCode" : "[REDACTED]",
"cloudUserName" : >
"controllerVersion" : "",
"deviceHwVver" : "2.0",
"deviceId" : "[REDACTED]",
"deviceMac" : "[REDACTED]",
"deviceModel" : "ER605",
"deviceName" : "ER605",
"deviceType" : "SMBROUTER",
"fwId" :"",
"fwVer" : "2.2.6 Build 20240718 Rel.82712",
"hwId" : "[REDACTED]",
"oemId" : "[REDACTED]",
"tcspVer" : "1.2"
"error_code" : 0,
"id" : 1,
"result"
"cachedSvr" : "n-euwi-device-omada.tplinkcloud.com:443",
"illegalType" "0;
"validTimeOnDevice"” : 86400
30
```

## Slide 31

### `The broken chain of trust - Cloud (CVE-2025-9192)`

”Let’s eat, Grandma!” VS “Let’s eat Grandma!” We change this to an IP address and bypass the check :-}

31

## Slide 32

```
Client enumeration (FSCT-2025-003, FSCT-2025-011)
```

- When adopting a Client via Cloud all you need to know is the S/N, no proof-ofownership required

- • S/N are sequential, can be retrieved using Omada Cloud API; Client info, **<u>such as model and MAC</u>** , can be inferred from its S/N

- **<u>VERY susceptible to brute-forcing</u>**

32

## Slide 33

# `Client hijacking, Cloud (CVE-2025-15630)`

- Client contacts the Default Controller

- Default Controller sends the URL of a Regional Controller

- **<u>Discovery and Adoption phases are not bound to the same ”state machine”</u>**

- **<u>Attackers may start the Adoption phase on Client’s behalf</u>** (don’t even need the Discovery request to arrive!)

   - Site admin must approve the new Client but if you fake it well…

   - …it will get adopted and appear in the Web UI

   - You can spam Cloud Controllers with fake Clients

33

## Slide 34

### `Stored XSS in Controller Web UI (CVE-2025-9289)`

- The properties of adopted Clients are displayed in the Web UI

- It had an older version of jQuery that uses calls to “eval()” to execute scripts – triggers on updating the UI with Client info

- We could no much because of restrictive CSP

34

## Slide 35

#### `Cross-Origin Resource Sharing bypass (CVE-2025-9292)`

- The Omada Cloud infra is on AWS

- The default CSP has not been altered: allows to perform requests with JavaScript to anything  hosted on Amazon AWS

- Look at me, I am the part of your infrastructure now…

35

## Slide 36

```
Hippity hoppity
Your network is our property
```

## Slide 37

# `Local compromise`

###### **ATTACK SCENARIO:**

The attacker is positioned inside of the local network:

1. <u>Intercept the Discovery request (UDP</u> broadcast) and respond as a fake Controller

2. <u>Forward the Discovery request (modified) to the real Controller, posing as a fake Client</u>

3. The Controller responds to the attacker, which <u>can now Intercept, modify, and forward all</u> comms between the real Controller and the real Client (CVE-2025-15628, CVE-2025-15544 or CVE-2025-9290)

###### **IMPACT:**

- Retrieve and modify sensitive information

- Take over Clients

37

## Slide 38

# `DEMO VIDEO 1`

39

## Slide 39

# `External compromise`

###### **ATTACK SCENARIO:**

The attacker is positioned in an external network, and exploits the race-condition:

1. Collect MAC addresses (Omada API or just bruteforce) Impersonate a not-yet-adopted Client.

2. Resend the message every 60 seconds. To target 1000 MACs attacker only needs ~17 requests per second -> wait for a device ”adoption”

3. Obtain original device provisioned configuration

4. Exploit the stored XSS/CSP bypass to phish admins and potentially steal Cloud account credentials

###### **IMPACT**

- Retrieve sensitive information (hashed site-credentials, VPN keys, etc.)

- Through stolen cloud credentials: modify device configurations, modify firewall rules, add VPNs to access internal networks, obtain “site-credentials” from site settings…

40

## Slide 40

# `DEMO VIDEO 2`

42

## Slide 41

```
The chain of trust issue is
way worse (CVE-2025-9293)
```

- <u>The same chain of trust was used in lots of other product families</u>

- • Omada, Festa, Tapo, Kasa, VIGI, Android apps…

• E.g. we could sniff credentials <u>from Android apps</u> TLS connections…

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

43

## Slide 42

```
Disclosure
And takeaways
```

## Slide 43

# `Disclosure timeline`

Issues are disclosed Issues are fixed by Sometimes, it’s to vendor vendor complicated…

45

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Issues are disclosed
to vendor
Disclosure timeline
90 120
\
Issues are fixed by Sometimes, it’s
vendor complicated...
45
```

## Slide 44

# `Disclosure timeline`

This is how long it took this time!

46

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Disclosure timeline
0 90 120 426
a ee as
This is how long it
took this time!
46
```

## Slide 45

# `Disclosure timeline`

All issues are remediated (almost)

”FSCT-2025-003 Plan for all fixes Two more FSCT-2025-003 and FSCT-2025-011 First patches (more than 300 days issues fixed and FSCT-2025require system(CVE-2025-7851, required) 011 will not get wide arch. (CVE-2025CVE-2025-7850) CVE IDs, as they 9292, CVEchanges […]”. No and first blog have low CVSS 2025-9293) patch by, at least, scores […] day 394

47

## Slide 46

# `Disclosure timeline`

All issues are remediated (almost)

**13 issues got a CVE (out of 17 reported). The ”default password” issue was not fixed.**

48

## Slide 47

# `Takeaways`

• <u>For vendors:</u>

• Bad design choices can cause serious problems later – e.g. shared vulns affecting many product families • Cryptography is engineering, not opinion – follow standards, use proven algorithms, plan your PKI ahead • Security through obscurity never works

- <u>For users:</u>

• If you are willing to use any ZTP platforms, enable every possible security measures such 2FA, don’t use a default password, rotate passwords & keys frequently, update your devices!

49
