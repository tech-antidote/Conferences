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
text_chars: 35786
ocr_pages: 11
has_ocr: true
redacted_secrets: 0
ocr_confidence: 86.0
ocr_unreliable_blocks: 0
content_note: "All 47 pages were rendered and read against the source PDF by a vision model; 35 were rewritten and 12 confirmed correct. The ocr_* fields describe the superseded first-pass extraction."
vision_verified_pages_changed: 35
vision_verified_pages: 47
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:45:01Z"
---
# Zero-Day Provisioning Chaining TP-Link ZTP Vulnerabilities for Infiltrating Networks

**Speakers:** Stanislav Dashevskyi, Francesco La Spina  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/Stanislav Dashevskyi&Francesco La Spina_Zero-Day Provisioning Chaining TP-Link ZTP Vulnerabilities for Infiltrating Networks.pdf` (47 pages)


## Slide 1

# Zero~~-touch~~day provisioning

**Chaining TP-Link ZTP Vulnerabilities for Infiltrating Networks**

Stanislav Dashevskyi, Francesco La Spina

## Slide 2

### About us

**Stanislav Dashevskyi**
Principal Security Researcher

**Francesco La Spina**
Senior Security Researcher

FORESCOUT RESEARCH | VEDERE LABS

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

### What does ZTP look like in practice?

1. You connect a new Client device to the network
2. The Controller discovers the device
3. You click “Adopt” in the controller UI
4. The Controller adopts (onboards) and provisions the Client

- **But… how does this magic happen?**

Diagram (steps):
1. **Connect**
2. **Discover**
3. **Adopt** (Register device in controller)
4. **Onboard & Provision** — **Device Onboarded**: The device is registered in the platform/controller and is now managed.

## Slide 10

### Reverse-engineering Omada protocols

10

## Slide 11

### Where to begin? Client

- We purchased ER7206 and ER605 Omada gateways and downloaded the firmware

- We wanted to install debuggers and packet sniffers – **<u>no root access!</u>**

- Started with static analysis:

   - We looked at the Web UI of Client devices – it was built on **OpenWRT’s LuCi**…

   - We had to figure out the way to **<u>de-obfuscate</u>** the **Lua bytecode** – tough!

- We found:

   - **<u>CVE-2025-7851</u>**: Insufficient patch for the “Leftover debug code” issue found by Cisco Talos (CVE-2024-21827)

   - **<u>CVE-2025-7850</u>**: Authenticated OS command injection via Wireguard VPN settings through the Web UI

- We had to release these findings as a separate <u>blogpost</u>

_Taken from tplink.com_

```c
//...
if ( access("/usr/sbin/image_type_debug", 0) ) {
    // Send a challenge and verify the signature (requires the private key).
    // If the signature is correct, grant the root shell.
}
else {
    // Ask for a password derived from the LAN mac address.
    // If the password is correct, grant the root shell.
}
//...
```

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

   - Each message is encoded in a JSON payload, preceded by a 4-byte payload length (network order)

- Several phases: **<u>Discovery, Adopt</u>**, Manage, Reset, Prelink, Rebuilt, and others

- Similarities with different other protocols used by other (non-Omada) TP-Link devices

   - **_“I just wanted to learn the water temperature” by Imre Red, DeepSec’23_**

```json
{
    "header" : {
        "version" : "1.2.0",
        "mac" : "[REDACTED]",
        "type" : 2,
        "device" : "gateway",
        "error":0,
        "dest": "[REDACTED]",
        "verCap" : 3
    },
    "body" : {
        "deviceInfo" : {
            "model" : "ER7206",
            "modelVer" :"2.20",
            "hwVer" : "ER7206 v2.20",
            "fwVer" : "[REDACTED]",
            "time" : "0 days 03:43:05",
            "ip" : "192.168.0.1",
            "fac" : "false"
        },
        "deviceMisc" : {
            "extraPortNum" : {
                "extraPort" : 0,
                "lteWan" : 0,
                "usbLteWan" : 1
            },
            "portNum" : 6
        },
        "controller" : {
            "id" : "[REDACTED]"
        }
    }
}
```

13

## Slide 14

### Omada: Discovery (Local + Cloud)

- Local discovery is done via UDP (broadcast)

   - Client sends basic information (S/N, MAC addr, model, version, etc.)

   - Controller responds with similar info + the IP/port to be used for Adoption

- Cloud-based discovery is via TCP/TLS

   - Similar info is exchanged, but the client will contact an Omada Cloud host

<u>NOTE</u>: When no local controller is present, Omada devices continue to broadcast Discovery protocol messages…**this will be relevant later**

_Local discovery — Client ↔ Local Controller (UDP port 29810):_
1. Discover request (Client → Local Controller)
2. Discover response (Local Controller → Client)

_Cloud discovery — Client ↔ Cloud Controller (TCP / SSL port 443):_
- helloCloud request (Client → Cloud Controller)
- helloCloud response (Cloud Controller → Client)

14

## Slide 15

### Adoption steps (Cloud)

1
2

- Sites are logically separated network locations (different company branches)

**Devices in each site will have shared “site credentials”**

_Taken from support.omadanetworks.com_

15

## Slide 16

### Omada: Adoption V2

Works over TCP/TLS

No substantial differences between Local and Cloud

**1.** **<u>During the TLS handshake, only</u>** <u>the client verifies the identity of the Controller</u>

**2.** **<u>Client authenticates with Controller (custom challenge-response)</u>**

   - a) Controller sends a “random” auth challenge

   - b) Client replies with two-round hash of its creds, using the challenge as the salt (2<sup>nd</sup> round)  -> <u>no standard HMAC</u>

**3.** **<u>Controller authenticates with Client</u>**

   - a) Client sends its own “random” challenge

   - b) Controller replies with two-round hash of device creds

4. Next, Controller attempts to read the current config and push the new one

   - a) Primary config: new network settings, “<u>site credentials</u>”…

   - b) Secondary config: modules (Wireguard VPN) and other things

   - c) Client is now adopted

Sequence diagram — Client ↔ Controller (TCP / SSL port 28914):

| Message | Direction | MSG TYPE |
| --- | --- | --- |
| Inform json | Client → Controller | 3 |
| randomKeyForDeviceVerify | Controller → Client | 1048576 |
| AUTH_dev, randomKeyForSystemVerify | Client → Controller | 1048577 |
| AUTH_sys | Controller → Client | 1048578 |
| ACK | Client → Controller | 1048579 |
| Propose new primary config | Controller → Client | 1048585 |
| Current config | Client → Controller | 1048580 |
| Primary config | Controller → Client | 1048581 |
| ACK | Client → Controller | 1048582 |
| Propose new secondary config | Controller → Client | 1048586 |
| ACK | Client → Controller | 256 |
| Secondary config | Controller → Client | 4096 |
| … | | |

16

## Slide 17

### The vulnerabilities

17

## Slide 18

### Hardcoded crypto in V1 (CVE-2025-15627)

- ”Legacy” V1 is present in the latest Clients, can be forced by Controllers

- Asymmetric encryption for auth and session key sharing, symmetric encryption for data

- The asymmetric keys are hardcoded

   - The “public” key is located in Client’s firmware

   - The private key is obfuscated within the Controller’s software

- **<u>CVE-2025-15629</u>** : the session key has insufficient entropy

- Attackers can decrypt traffic and get credentials

**Sequence diagram — Client ↔ Controller (TCP port 28914):**

1. Client → Controller: Inform json
2. Controller → Client: encrypt(AUTH, private_key)
3. Client → Controller: Auth ACK, Device info, encrypt(RC4_key, public_key)
4. Controller → Client: encrypt(Primary config, RC4_key)
5. Client → Controller: Initial config ACK
6. ...

Right-hand counter column (top→bottom): 3, 16, 32, 4096, 8192

**<u>AUTH = username + md5sum(password)</u>**

18

## Slide 19

### Insecure creds in V2 (CVE-2025-9290)

_AUTH _dev = sha256sum(sha256sum(username + md5sum(password)) + randomKeyForDeviceVerify)_

**Sequence diagram — Client ↔ Controller (TCP / SSL port 28914):**

1. Client → Controller: Inform json
2. Controller → Client: randomKeyForDeviceVerify
3. Client → Controller: AUTH_dev, randomKeyForSystemVerify
4. Controller → Client: AUTH_sys
5. Client → Controller: ACK

(Messages 2 and 3 are highlighted together in a box.)

Right-hand counter column (top→bottom): 3, 1048576, 1048577, 1048578, 1048579

19

## Slide 20

### Insecure creds in V2 (CVE-2025-9290)

_AUTH _dev = sha256sum(sha256sum(username + md5sum(password))_ ~~+ randomKeyForDeviceVerify)~~

```
rainbow_table = {
    "94F37F62C8CB0BF792518A11951EFC430620BB982C26454BD3230304157463E8":
    [
        "admin/admin",
        "admin21232F297A57A5A743894A0E4A801FC3",
    ],
    "02B0DE9FACF8DEFA14DB2692076FCF1B3A4E81D4A37B27E898A59CFC55CA462B":
    [
        "admin/password12345",
        "admin365D38C60C4E98CA5CA6DBC02D396E53",
    ],
    "92A70A0B2C946194A8C2878B9BAC3BB520A30CD41C4C44D7F7EC363F6F2EB2EB":
    [
        "admin/Ciccio81",
        "admin4778BF96209582FFA15C57F66BB00061",
    ],
```

**Sequence diagram — Client ↔ Controller (TCP / SSL port 28914):**

1. Client → Controller: Inform json
2. Controller → Client: ~~randomKeyForDeviceVerify~~
3. Client → Controller: AUTH_dev, randomKeyForSystemVerify
4. Controller → Client: AUTH_sys
5. Client → Controller: ACK

Right-hand counter column (upper values 3 and 1048576 hidden behind the code overlay): 1048577, 1048578, 1048579

20

## Slide 21

### Insecure creds in V2 (CVE-2025-15544)

**Sequence diagram — Client ↔ Controller (TCP / SSL port 28914):**

1. Client → Controller: Inform json
2. Controller → Client: randomKeyForDeviceVerify
3. Client → Controller: AUTH_dev, randomKeyForSystemVerify
4. Controller → Client: AUTH_sys
5. Client → Controller: ACK
6. Controller → Client: Propose new primary config
7. Client → Controller: Current config
8. Controller → Client: Primary config (highlighted in a box)

Right-hand counter column visible (lower values; upper values hidden behind the JSON overlay): 1048580, 1048581

```
{
    "header" : {
        "error" : 0,
        "mac" : "00-DE-AD-BE-EF-00",
        "type" : 1048581,
        "version" : "2.2.0"
    },
    "body" : {
        // omitted for brevity
        "userAccount" : {
            "curPassword" : "21232F297A57A5A743894A0E4A801FC3",
            "curUsername" : "admin",
            "newPassword" : "A601EA74981ADF5A62C23DDA0E0D64CB",
            "newUsername" : "site_admin"
        }
    }
}
```

(The `newPassword` and `newUsername` lines are highlighted with a red box.)

21

## Slide 22

### Insecure creds in V2 (CVE-2025-15544)

**Callout (starburst): Controllers do not validate the identify of Clients**

**Sequence diagram — Client ↔ Controller (TCP / SSL port 28914):**

1. Client → Controller: Inform json
2. Controller → Client: randomKeyForDeviceVerify
3. Client → Controller: AUTH_dev, randomKeyForSystemVerify
4. Controller → Client: AUTH_sys
5. Client → Controller: ACK

Config JSON (userAccount portion visible; the header is behind the callout):

```
"userAccount" : {
    "curPassword" : "21232F297A57A5A743894A0E4A801FC3",
    "curUsername" : "admin",
    "newPassword" : "A601EA74981ADF5A62C23DDA0E0D64CB",
    "newUsername" : "site_admin"
}
```

_AUTH _dev = sha256sum(sha256sum(username + md5sum(password))_ ~~+ randomKeyForDeviceVerifiy)~~

22

## Slide 23

### Default credentials (FSCT-2025-008)

- A brand-new Client will always have default credentials (admin/admin)

- If we ”fake” a Controller, we can always know if a Client has default credentials

- If we ”fake” a Client and it gets accepted by a Controller, we can always authenticate

- **<u>You get site credentials “for free"</u>**

admin / admin

**Sequence diagram — Client ↔ Controller (TCP / SSL port 28914):**

1. Client → Controller: Inform json
2. Controller → Client: randomKeyForDeviceVerify
3. Client → Controller: AUTH_dev, randomKeyForSystemVerify
4. Controller → Client: AUTH_sys
5. Client → Controller: ACK
6. Controller → Client: Propose new primary config
7. Client → Controller: Current config
8. Controller → Client: Primary config
9. Client → Controller: ACK
10. Controller → Client: Propose new secondary config
11. Client → Controller: ACK
12. Controller → Client: Secondary config
13. ...

Right-hand counter column (top→bottom): 3, 1048576, 1048577, 1048578, 1048579, 1048585, 1048580, 1048581, 1048582, 1048586, 256, 4096

23

## Slide 24

### The chain of trust

- The traffic in V2 is encrypted and Clients verify the identity of Controllers (TLS)

- Typical PKI chain of trust:
   - The **<u>“Root” cert</u>** is self signed and used as Root CA, imported into the keystore of Clients
   - The **<u>“Intermediate” cert</u>** is signed by the Root and is imported into the Controllers’ trusted keystore
   - The **<u>”Server” cert</u>** is used by Controllers and Clients for TLS

Certificate chain (top→bottom):

- Root cert — CN: tp-link-CA, MD5: 3ACF3329C38D...
- Intermediate cert — CN: TP-LINK CA P1, MD5: DEA164E02A9E...
- Server cert — CN: localhost, MD5: 3A1A6DB1887E...

24

## Slide 25

### The broken chain of trust (CVE-2025-15628)

- Look at the cert expiration dates... Everything is hard-coded

- Controllers have a hard-coded private key (!) used for TLS (!)

- Controllers’ Server cert is enough to pass the identity check -> **<u>we can reuse Controller’s Server certs and private key!</u>**

- Cloud Controllers must present a cert derived from Root/Intermediate with a CN* that ends with “tplinkcloud.com” -> we cannot forge this one ☹

Certificate chain (top→bottom):

- Root cert — tp-link-CA / Identity: tp-link-CA / Verified by: tp-link-CA / Expires: 01/19/2068
- Intermediate cert — TP-LINK CA P1 / Identity: TP-LINK CA P1 / Verified by: tp-link-CA / Expires: 01/19/2068
- Server cert — localhost / Identity: localhost / Verified by: TP-LINK CA P1 / Expires: 04/20/2051

* A certificate common name (CN) is a standard field in an X.509 digital certificate that identifies the primary hostname, domain name, or entity protected by or assigned to the certificate

25

## Slide 26

### Why impersonating Controllers?

- Use Clients as credential oracles

- Get private VPN keys, read other sensitive information, push new settings

- Also, remember CVE-2025-7850?

   - OS command injection via the Web UI (authenticated!)

```lua
209    function check_key(r0_14, r1_14)
210      -- line: [226, 241] id: 14
211      local r2_14 = "echo \"" .. r9_0.safeSpecialString(r0_14) .. "\" |wg pubkey"
212      if r4_0.fork_call(r2_14) == 1 then
213        return true
214      end
215      if r1_14 then
216        r1_14.public_key = io.popen(r2_14):read("*a")
217      end
218      return false
219    end
```

```
echo "KPzPGI6WQ7z6bfwKYrQtpwRQwzgaU8/6wVEUtRIlslI="\n{ARBITRARY_OS_COMMAND}"" | wg pubkey
```

26

## Slide 27

### Using fake Controllers to exploit CVE-2025-7850

```
1   manage_config_msg = {
2       "header" : {
3           "type" : 4096,
4       },
5       "body" : {
6           "sequenceId": 4,
7           "userAccount": {
8               # ...
9           },
10          "wireguard": {
11              "interfaces": [
12                  {
13                      "id":878491625,
14                      "operation":1,
15                      "enable":"true",
16                      "mtu":1420,
17                      "listenPort":51820,
18                      "privateKey":"[ARBITRARY OS COMMAND]",
19                      "localIp":"10.10.10.1"
20                  }
21              ]
22          },
23          "configVersionInc": 1,
24      }
25  }
```

**Sequence diagram — Client ↔ Controller (TCP / SSL port 28914):**

1. Client → Controller: Inform json
2. Controller → Client: randomKeyForDeviceVerify
3. Client → Controller: AUTH_dev, randomKeyForSystemVerify
4. Controller → Client: AUTH_sys
5. Client → Controller: ACK
6. Controller → Client: Propose new primary config
7. Client → Controller: Current config
8. Controller → Client: Primary config
9. Client → Controller: ACK
10. Controller → Client: Propose new secondary config
11. Client → Controller: ACK
12. Controller → Client: Secondary config
13. ...

Right-hand counter column (top→bottom): 3, 1048576, 1048577, 1048578, 1048579, 1048585, 1048580, 1048581, 1048582, 1048586, 256, 4096

27

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

### The broken chain of trust — Cloud (CVE-2025-9291)

```
{
    "id" : 1,
    "method" : "helloCloud",
    "params" : {
        "alias" : "ER605",
        "authCode" : "[REDACTED]",
        "cloudUserName" : "",
        "controllerVersion" : "",
        "deviceHwVer" : "2.0",
        "deviceId" : "[REDACTED]",
        "deviceMac" : "[REDACTED]",
        "deviceModel" : "ER605",
        "deviceName" : "ER605",
        "deviceType" : "SMBROUTER",
        "fwId" : "",
        "fwVer" : "2.2.6 Build 20240718 Rel.82712",
        "hwId" : "[REDACTED]",
        "oemId" : "[REDACTED]",
        "tcspVer" : "1.2"
    }
}

{
    "error_code" : 0,
    "id" : 1,
    "result" : {
        "cachedSvr" : "n-euw1-device-omada.tplinkcloud.com:443",
        "illegalType" : 0,
        "validTimeOnDevice" : 86400
    }
}
```

```c
__int64 ecs_verifySsl(unsigned int preverify_ok, void* store_ctx) {
       // ...
01:    if ( !error_depth )
02:    {
03:      subject_name_str = strstr(subject_name_buf, "/CN=");
04:      if ( !subject_name_str )
05:        return 0;
06:      cert_subject_name = subject_name_str + 4;
07:      v11 = strchr(subject_name_str + 4, '/');
08:      if ( v11 )
09:        *v11 = 0;
10:      if ( strstr(global_controller_host, "tplinkcloud.com") && !strstr(cert_subject_name, "tplinkcloud.com") )
11:      {
12:        if ( HIDWORD(qword_5CCB8) )
13:          printf(
14:            "[ECS][ERROR]%s():%5d @ verify error:CN mismatch(%s), controllerUrl(%s).\n\r",
15:            "_ecs_verifySsl",
16:            125LL,
17:            cert_subject_name,
18:            global_controller_host);
19:        if ( qword_5CCB8 )
20:        {
21:          // ...
22:          ecs_log(2LL, "[ECS][ERROR]<%s>%s():%5d @ verify error:CN mismatch(%s), controllerUrl(%s).\n\r");
23:          // ...
24:        }
25:        return 0;
26:      }
27:    }
       // ...
    }
```

29

## Slide 30

### The broken chain of trust — Cloud (CVE-2025-9291)

```
{
    "id" : 1,
    "method" : "helloCloud",
    "params" : {
        "alias" : "ER605",
        "authCode" : "[REDACTED]",
        "cloudUserName" : "",
        "controllerVersion" : "",
        "deviceHwVer" : "2.0",
        "deviceId" : "[REDACTED]",
        "deviceMac" : "[REDACTED]",
        "deviceModel" : "ER605",
        "deviceName" : "ER605",
        "deviceType" : "SMBROUTER",
        "fwId" : "",
        "fwVer" : "2.2.6 Build 20240718 Rel.82712",
        "hwId" : "[REDACTED]",
        "oemId" : "[REDACTED]",
        "tcspVer" : "1.2"
    }
}

{
    "error_code" : 0,
    "id" : 1,
    "result" : {
        "cachedSvr" : "n-euw1-device-omada.tplinkcloud.com:443",
        "illegalType" : 0,
        "validTimeOnDevice" : 86400
    }
}
```

```c
__int64 ecs_verifySsl(unsigned int preverify_ok, void* store_ctx) {
       // ...
01:    if ( !error_depth )
02:    {
03:      subject_name_str = strstr(subject_name_buf, "/CN=");
04:      if ( !subject_name_str )
05:        return 0;
06:      cert_subject_name = subject_name_str + 4;
07:      v11 = strchr(subject_name_str + 4, '/');
08:      if ( v11 )
09:        *v11 = 0;
10:      if ( strstr(global_controller_host, "tplinkcloud.com") && !strstr(cert_subject_name, "tplinkcloud.com") )
11:      {
12:        if ( HIDWORD(qword_5CCB8) )
13:          printf(
14:            "[ECS][ERROR]%s():%5d @ verify error:CN mismatch(%s), controllerUrl(%s).\n\r",
15:            "_ecs_verifySsl",
16:            125LL,
17:            cert_subject_name,
18:            global_controller_host);
19:        if ( qword_5CCB8 )
20:        {
21:          // ...
22:          ecs_log(2LL, "[ECS][ERROR]<%s>%s():%5d @ verify error:CN mismatch(%s), controllerUrl(%s).\n\r");
23:          // ...
24:        }
25:        return 0;
26:      }
27:    }
       // ...
    }
```

**Callout:** “Let’s eat, Grandma!” vs “Let’s eat Grandma!”

30

## Slide 31

### The broken chain of trust — Cloud (CVE-2025-9291)

```
{
    "id" : 1,
    "method" : "helloCloud",
    "params" : {
        "alias" : "ER605",
        "authCode" : "[REDACTED]",
        "cloudUserName" : "",
        "controllerVersion" : "",
        "deviceHwVer" : "2.0",
        "deviceId" : "[REDACTED]",
        "deviceMac" : "[REDACTED]",
        "deviceModel" : "ER605",
        "deviceName" : "ER605",
        "deviceType" : "SMBROUTER",
        "fwId" : "",
        "fwVer" : "2.2.6 Build 20240718 Rel.82712",
        "hwId" : "[REDACTED]",
        "oemId" : "[REDACTED]",
        "tcspVer" : "1.2"
    }
}

{
    "error_code" : 0,
    "id" : 1,
    "result" : {
        "cachedSvr" : "n-euw1-device-omada.tplinkcloud.com:443",
        "illegalType" : 0,
        "validTimeOnDevice" : 86400
    }
}
```

```c
__int64 ecs_verifySsl(unsigned int preverify_ok, void* store_ctx) {
       // ...
01:    if ( !error_depth )
02:    {
03:      subject_name_str = strstr(subject_name_buf, "/CN=");
04:      if ( !subject_name_str )
05:        return 0;
06:      cert_subject_name = subject_name_str + 4;
07:      v11 = strchr(subject_name_str + 4, '/');
08:      if ( v11 )
09:        *v11 = 0;
10:      if ( strstr(global_controller_host, "tplinkcloud.com") && !strstr(cert_subject_name, "tplinkcloud.com") )
11:      {
12:        if ( HIDWORD(qword_5CCB8) )
13:          printf(
14:            "[ECS][ERROR]%s():%5d @ verify error:CN mismatch(%s), controllerUrl(%s).\n\r",
15:            "_ecs_verifySsl",
16:            125LL,
17:            cert_subject_name,
18:            global_controller_host);
19:        if ( qword_5CCB8 )
20:        {
21:          // ...
22:          ecs_log(2LL, "[ECS][ERROR]<%s>%s():%5d @ verify error:CN mismatch(%s), controllerUrl(%s).\n\r");
23:          // ...
24:        }
25:        return 0;
26:      }
27:    }
       // ...
    }
```

**Callout:** We can use a public IP to bypass the CN check :-}

31

## Slide 32

### Client enumeration (FSCT-2025-003, FSCT-2025-011)

- When adopting a Client via Cloud all you need to know is the S/N, no proof-of-ownership required

- S/N are sequential, can be retrieved using Omada Cloud API; Client info, **<u>such as model and MAC</u>** , can be inferred from its S/N

- **<u>VERY susceptible to brute-forcing</u>**

| INDEX | SN CODE | NAME | STATUS | RESULT |
| --- | --- | --- | --- | --- |
| 1 | 224[REDACTED]1246 | A8-6E-84-[REDACTED] | Offline | ✗ Failed to adopt this gateway because a gateway already exists in this site. |
| 2 | 224[REDACTED]1245 | A8-6E-84-[REDACTED] | Online | ✗ Failed to adopt this gateway because a gateway already exists in this site. |
| 3 | 22[REDACTED]1244 | A8-6E-84-[REDACTED] | Offline | ✗ Failed to adopt this gateway because a gateway already exists in this site. |
| 4 | 22[REDACTED]1247 | A8-6E-84-[REDACTED] | Offline | ✓ |

32

## Slide 33

### Client hijacking, Cloud Controllers (CVE-2025-15630)

- Client contacts the Default Controller (Discovery phase)

- Default Controller sends the URL of a Regional Controller (Adoption and other phases kick in)

- **<u>Discovery and Adoption phases are not bound to the same ”state machine”</u>**

- **<u>Attackers may start the Adoption phase on Client’s behalf</u>** (don’t even need the Discovery request to arrive!)

   - A “fake” Client will get adopted and appear in the Web UI

   - You can spam Cloud Controllers with fake Clients

_Sequence diagram — participants: Attacker, Client, Default Cloud Controller, Regional Cloud Controller. Messages, top to bottom:_

1. Inform json (Client → Regional Cloud Controller)
2. helloCloud request (Client → Default Cloud Controller)
3. helloCloud response (Default Cloud Controller → Client)
4. randomKeyForDeviceVerify (Regional Cloud Controller → Attacker)
5. AUTH_dev, randomKeyForSystemVerify (Attacker → Regional Cloud Controller)
6. AUTH_sys (Regional Cloud Controller → Attacker)
7. ACK (Attacker → Regional Cloud Controller)
8. Propose new primary config (Regional Cloud Controller → Attacker)
9. Current config (Attacker → Regional Cloud Controller)
10. Primary config (Regional Cloud Controller → Attacker)
11. ACK (Attacker → Regional Cloud Controller)
12. …
13. Inform json (Client → Default Cloud Controller)
14. …

33

## Slide 34

### Stored XSS in Controller Web UI (CVE-2025-9289)

- The properties of adopted Clients are displayed in the Web UI

- Older version jQuery, calls “eval()” to update the UI with Client’s information

```json
{"header":{"version":"2.2.0","mac":"A8:6E:84:XX:XX:XX","type":
    1048580,"device":"gateway","error":0,"dest":"","verCap":3},
    "body":{"devCap":{"supportIPsecFailover":1,"specification":
    { ... "fwVer":"XXX<script>alert(1)</script>" ... }}}}
```

- We couldn’t do much because of restrictive content security policy (CSP)

```text
Content-Security-Policy: default-src 'self' https://*.tplinkcloud.com/;script-src 'self' 'unsafe-eval' 'sha256-7W9UiBaYGlOHpT1aQBLegqffUVHbYq6/ZAb+ErjUb40=' 'sha256-VGQ8jNTL2g0e8wPwOgyCQJDqhuRgfV7gRYexcBkBe4Y=' 'sha256-x2jgB1zBLi30IsfY+VNgWjwBGeHPJxOSrzl+IdsT6k0=' 'sha256-0AHZXO4clnpdcxqdmASPBEp4JCIrtaxIX/mUuL1kzZw=' 'sha256-lfXlPY3+MCPOPb4mrw1Y961+745U3WlDQVcOXdchSQc=';style-src 'self' 'unsafe-inline';connect-src 'self' https://*.tplinkcloud.com/ https://*.tplinkcloud.com:8843/ wss://*.tplinkcloud.com/ https://*.tiles.mapbox.com https://api.mapbox.com https://events.mapbox.com ;frame-src 'self' data:;img-src 'self' https://*.tplinkcloud.com/ https://*.mzstatic.com/ https://play-lh.googleusercontent.com/ data: blob:;child-src blob: ;worker-src blob: ;object-src 'self' data: blob:
```

_Screenshot: Omada (by tp-link) Web UI with a "Log In" dialog ("Session expired, please reauthenticate", Username / Password fields) over a device Overview panel (Serial Number 22460J5001242, MAC Addr A8-6E-84-…, CONNECTED)._

34

## Slide 35

### Cross-Origin Resource Sharing (CORS) bypass (CVE-2025-9292)

- We checked the CSP of Cloud Controllers

- The Omada Cloud runs on AWS

- There are bits of the default CSP that allow Cross-Site requests to anything hosted on AWS…

```text
default-src 'self' https://*.tplinkcloud.com/; script-src 'self' 'unsafe-eval' https://www.paypal.com/ https://www.paypalobjects.com/ https://js.stripe.com 'sha256-7W9UiBaYGlOHpT1aQBLegqffUVHbYq6/ZAb+ErjUb40=' 'sha256-VGQ8jNTL2g0e8wPwOgyCQJDqhuRgfV7gRYexcBkBe4Y=' 'sha256-+9dQLByJ0rMH7ojZkdfnL0p0S0pZqKxWTlh7vSa+FMg=' 'sha256-x2jgB1zBLi30IsfY+VNgWjwBGeHPJxOSrzl+IdsT6k0=' 'sha256-0AHZXO4clnpdcxqdmASPBEp4JCIrtaxIX/mUuL1kzZw=' 'sha256-lfXlPY3+MCPOPb4mrw1Y961+745U3WlDQVcOXdchSQc=' 'sha256-VohL58KrXs+2LMTip+0SXk2/JwaZNxG/j9hadlPKc2E='; style-src 'self' 'unsafe-inline'; connect-src 'self' https://*.cloudfront.net/ https://*.tplinkcloud.com/ https://*.tplinkcloud.com:8843/ http://*.tplinkcloud.com:8088/ wss://*.tplinknbu.com/ ws://localhost:*/ wss://*.tplinkcloud.com/ https://*.paypal.com/ https://api.stripe.com https://*.tiles.mapbox.com https://api.mapbox.com/ https://events.mapbox.com https://*.amazonaws.com/ data:; frame-src 'self' OmadaSightWebPlayer: vigiwebplayer: https://*.tplinkcloud.com/ https://js.stripe.com https://hooks.stripe.com https://*.paypal.com/ data: blob:; img-src 'self' https://*.cloudfront.net/ https://*.tplinkcloud.com/ https://*.amazonaws.com/ https://*.mzstatic.com/ https://play-lh.googleusercontent.com/ https://kcart.alipay.com/ data: blob:; child-src blob:; worker-src https://*.tplinkcloud.com blob:; media-src https://*.tplinkcloud.com/ https://*.cloudfront.net/ https://*.amazonaws.com/ blob:; object-src 'self' data: blob:
```

_Illustration (Bosch-style) of a hooded figure holding a scroll that reads "Look at me I am the Controller now"._

35

## Slide 36

### Hippity hoppity your network is our property

36

## Slide 37

### Local compromise

**ATTACK SCENARIO:** The attacker is positioned inside of the victim’s local network:

1. <u>Intercept the Discovery request </u>(UDP broadcast) and <u>respond as a fake Controller</u>

2. <u>Forward the Discovery request </u>(modified) <u>to the real Controller</u>, posing as a fake Client

3. The Controller responds to <u>the attacker</u>, who <u>can now Intercept, modify, and forward </u>all comms between the real Controller and the real Client (CVE-2025-15628, CVE-2025-15544 or CVE-2025-9290)

**IMPACT: attacker can**

- Retrieve and modify sensitive information (e.g., device configuration)

- Take over Clients

_Network diagram — “Internal network” (dashed box) containing Omada Switch, Hardware controller and Attacker (red arrows from Attacker to the Omada Switch and the Hardware controller). The Hardware controller links to ER7206 / ER605 (VPN router/gateway), which reaches the Internet (cloud) connecting to a Workstation and the Omada app._

37

## Slide 38

_Full-screen terminal (tmux) screenshot showing an empty shell prompt:_

```text
(venv) standash@moria:~/stuff/vr/tplink/xploits$
[tplink] 0:vi  1:vi  2:bash- 3:bash*                              "moria" 16:59 13-Jul-26
```

38

## Slide 39

### External compromise

**ATTACK SCENARIO:**

The attacker is positioned outside victim’s network, and exploits the race-condition:

1. Collect MAC addresses (Omada API or just brute-force) to impersonate a not-yet-adopted Client

2. Resend the message every 60 seconds. To target 1000 MACs attacker only needs ~17 requests per second -> <u>wait for a device ”adoption”</u>

3. Obtain original device provisioned configuration

4. Exploit the stored XSS/CSP bypass to phish admins and potentially steal Cloud account credentials

**IMPACT: attacker can**

- Retrieve sensitive information (hashed site-credentials, VPN keys, etc.)

- Through stolen cloud credentials: modify device configurations, modify firewall rules, add VPNs to access internal networks, obtain “site-credentials” from site settings…

_Network diagram — “Internal network” (dashed box) containing Hardware controller, Omada Switch and Software controller. Outside: ER7206 / ER605 (VPN router/gateway), a Sysadmin, the Omada Cloud Controller, an Attacker and the Internet (cloud) linking them (red attacker arrows to the Omada Switch/gateway and to the Internet)._

39

## Slide 40

_Fully black slide with no visible text or graphics._

## Slide 41

### The chain of trust issue is way worse (CVE-2025-9293)

- <u>The same chain of trust was used in lots of other TP-Link product families</u>

   - Omada, Festa, Tapo, Kasa, VIGI, Android apps…

   - E.g. we could <u>sniff credentials from Android apps</u> TLS connections…

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

_Google Play screenshot: TP-Link Tether by TP-LINK SYSTEMS INC., In-app purchases, 4.6★ (732K reviews), **50M+ Downloads** (circled in red), PEGI 3._

41

## Slide 42

### Disclosure and some takeaways

42

## Slide 43

### Disclosure timeline (typical)

_Horizontal timeline with markers:_ **0**, **90**, **120** _(120 in red)._

- **0** — Issues are disclosed to vendor
- **90** — Industry standard for fixing bugs
- **120** — Sometimes, it’s complicated…

43

## Slide 44

### Disclosure timeline (this research)

_Horizontal timeline with markers:_ **0**, **90**, **120** _(120 in red)_, **426**

- **426** — This is how long it took this time!

44

## Slide 45

### Disclosure timeline (this research)

All issues are remediated (almost)

_Timeline axis (days):_ 0, 64, 140, 234, 240, 256, 389, 426

- **64:** Plan for all fixes (more than 300 days required)
- **140:** First patches (CVE-2025-7851, CVE-2025-7850) and first blog
- **234:** ”FSCT-2025-003 and FSCT-2025-011 require system-wide arch. changes […]”. No patch by, at least, day 394
- **256:** Two more issues fixed (CVE-2025-9292, CVE-2025-9293)
- **389:** FSCT-2025-003 and FSCT-2025-011 will not get CVE IDs, as they have low CVSS scores […]
- **426:** All issues are remediated (almost)

45

## Slide 46

### Disclosure timeline (this research)

All issues are remediated (almost)

_Timeline axis (days):_ 0, 64, 140, [illegible], 256, 389, 426

**13 discovered issues got a CVE (out of 17 reported)**

**The ”default password” issue was not fixed.**

46

## Slide 47

### Takeaways

- <u>For vendors:</u>

   - Cryptography is engineering and not a creative process – follow standards, use proven algorithms, plan your PKI ahead

   - Security through obscurity never works

   - Bad design choices can cause serious problems later – e.g. shared vulns affecting many product families: **<u>very loooong patch windows -> users are exposed all this time</u>**

- <u>For users:</u>

   - If you use any ZTP platforms, enable every possible security measure such as MFA, don’t use a default password, rotate passwords & keys frequently, update your devices!

https://www.forescout.com/research-labs-overview/

47

