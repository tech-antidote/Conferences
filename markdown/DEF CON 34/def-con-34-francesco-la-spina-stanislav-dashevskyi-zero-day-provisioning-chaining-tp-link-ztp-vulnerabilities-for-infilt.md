---
title: "Zero-Day Provisioning Chaining TP-Link ZTP Vulnerabilities for Infiltrating Networks"
speakers: ["Francesco La Spina", "Stanislav Dashevskyi"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: 2026
source_pdf: "DEF CON 34/DEF CON 34 - Francesco La Spina, Stanislav Dashevskyi - Zero-Day Provisioning Chaining TP-Link ZTP Vulnerabilities for Infiltrating Networks - v1.pdf"
pages: 47
sha256: "28441939a9a0a58a416d3881401499ccabc6ca302c7865dc66c80271f637f826"
text_chars: 16384
ocr_pages: 6
has_ocr: true
redacted_secrets: 0
ocr_confidence: 90.3
ocr_unreliable_blocks: 2
vision_verified_pages_changed: 41
vision_verified_pages: 47
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:27:14Z"
---
# Zero-Day Provisioning Chaining TP-Link ZTP Vulnerabilities for Infiltrating Networks

**Speakers:** Francesco La Spina, Stanislav Dashevskyi  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Francesco La Spina, Stanislav Dashevskyi - Zero-Day Provisioning Chaining TP-Link ZTP Vulnerabilities for Infiltrating Networks - v1.pdf` (47 pages)


## Slide 1

# Zero-~~touch~~ day provisioning: Chaining TP-Link ZTP Vulnerabilities for Infiltrating Networks

Stanislav Dashevskyi, Francesco La Spina

## Slide 2

# `About us`

- **Stanislav Dashevskyi** , Principal Security Researcher

- **Francesco La Spina** , Senior Security Researcher

2

## Slide 3

# What is ZTP?

And why should we care?

## Slide 4

# `From manual to “zero-touch” provisioning`

- On-site installation required: new device had to be physically configured by an IT technician, one by one

- Slow and error-prone deployments, limited scalability

- ZTP introduced more than a decade ago to solve these issues…

4

## Slide 5

# `Zero-Touch Provisioning (ZTP)`

- ZTP is a technology allowing to remotely onboard and provision network devices from a central platform

- Several vendors have started to offer ZTP under different names and using different protocols

- A ZTP system has two main components:

   - **<u>Client devices</u>**: switches, routers, Wi-Fi access points, and gateways that need to be provisioned and managed

   - **<u>Controllers</u>**: dedicated appliances and/or software platforms that provision, configure, monitor, and update client devices

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

   - **<u>Local via dedicated hardware Controllers</u>** (a device sold by TP-Link)

   - **<u>Local via software Controllers</u>** (Virtual Machine)

   - There can be <u>hybrid deployments</u>

_Taken from tplink.com_

7

## Slide 8

# `Why choosing Omada?`

- **<u>Large but under-researched attack surface</u>**:

   - TP-Link has a large global deployment and customer base

   - Widely adopted ZTP ecosystem (SMB/SME) with <u>limited public security research</u>

   - Past vulnerabilities mostly on clients

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

# Reverse-engineering

Omada protocols [[:......:]]

## Slide 11

# `Where to begin? Clients`

- Purchased ER7206 and ER605 Omada gateways and downloaded the firmware

- We wanted to install debuggers and packet sniffers – no root access!

- Started with static analysis:

   - We looked at the WebUI of Client devices – it was built on OpenWRT’s LuCi…

   - We had to figure out the way to **<u>de-obfuscate</u>** the Lua bytecode – tough!

- We found:

   - **<u>CVE-2025-7851</u>**: Insufficient patch for the “Leftover debug code” issue found by Cisco Talos (CVE-2024-21827)

   - **<u>CVE-2025-7850</u>**: Authenticated OS command injection via Wireguard VPN settings through the Web UI

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

_Taken from tplink.com_

- Had to release these findings as a separate <u>blogpost</u>

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

   - Each message is encoded in a JSON payload, preceded by a 4-byte payload length (network order)

- Several phases: **Discovery, Adopt**, Manage, Reset, Prelink, Rebuilt, and others

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

# `Omada: Discovery (Local and Cloud)`

- Local discovery is done via UDP (broadcast)

   - Client sends basic information (S/N, MAC addr, model, version, etc.)

   - Controller responds with similar info + the IP/port to be used for Adoption

- Cloud-based discovery is via TCP/TLS

   - Similar info is exchanged, but the client will contact an Omada Cloud host

- **<u>NOTE</u>**: After a successful “pairing” with a Controller, a Client will resend a Local Discovery message under specific failure conditions…this will be relevant later

Local discovery: Client → Local Controller over UDP, port 29810 — "Discover request" (1), then Local Controller → Client "Discover response" (2).

Cloud-based discovery: Client → Cloud Controller over TCP/SSL, port 443 — "helloCloud request", then Cloud Controller → Client "helloCloud response".

14

## Slide 15

# `Adoption steps (Cloud)`

- Sites are logically separated network locations (different company branches)

- **<u>Devices in each site will have shared “site credentials”</u>**

Screenshot: the Controller’s "Add to Site" dialog — (1) the Add to Site / Site selector, (2) the device Index / Device Key entry row used to adopt a device.

15

## Slide 16

# `Omada: Adoption V2`

- Works over TCP/TLS

- No substantial differences between Local and Cloud

1. **<u>During the TLS handshake, only</u>** <u>the client verifies the identity of the Controller</u>

2. **<u>Client authenticates with Controller (custom challenge-response)</u>**

   a) Controller sends a “random” auth challenge

   b) Client replies with two-round hash of its creds, using the challenge as the salt (2<sup>nd</sup> round) -> <u>no standard HMAC</u>

3. **<u>Controller authenticates with Client</u>**

   a) Client sends its own “random” challenge

   b) Controller replies with two-round hash of device creds

4. Next, controller attempts to read the current config and push the new one

   a) Primary config: new network settings, “site credentials”…

   b) Secondary config: modules (Wireguard VPN) and other things

   c) Client is now adopted

Sequence (Client <-> Controller, TCP/SSL port 28914):
- Client → Controller: Inform json (3)
- Controller → Client: randomKeyForDeviceVerify (1048576)
- Client → Controller: AUTH_dev, randomKeyForSystemVerify (1048577)
- Controller → Client: AUTH_sys (1048578)
- Client → Controller: ACK (1048579)
- Controller → Client: Propose new primary config (1048585)
- Client → Controller: Current config (1048580)
- Controller → Client: Primary config (1048581)
- Client → Controller: ACK (1048582)
- Controller → Client: Propose new secondary config (1048586)
- Client → Controller: ACK (last cfg result) (256)
- Controller → Client: Secondary config (4096)
- …

16

## Slide 17

# The vulnerabilities

};-/

## Slide 18

# `Hardcoded crypto in V1 (CVE-2025-15627)`

- There is a “legacy” V1, and it can be “forced”

- The public/private keypair in Omada V1 is hardcoded

   - The public key is located in Client’s firmware

   - The private key is obfuscated within the Controller’s software

- **<u>CVE-2025-15629</u>**: the session key has insufficient entropy

- Attackers can decrypt traffic and force Controllers to leak password hashes

- **<u>AUTH = username + md5sum(password)</u>**

Sequence (Client <-> Controller, TCP port 28914):
- Client → Controller: Inform json (3)
- Controller → Client: encrypt(AUTH, private_key) (16)
- Client → Controller: Auth ACK, Device info, encrypt(RC4_key, public_key) (32)
- Controller → Client: encrypt(Primary config, RC4_key) (4096)
- Client → Controller: Initial config ACK (8192)
- …

```java
package com.tplink.smb.ecsp.common.util.encrypt;
import java.nio.charset.StandardCharsets;

public class GlobalConfig {

    private static final byte[] ENCRYPTED_NETTY_RSA_PRIVATE_KEY = {
        -38, 0, 52
        // the rest of the key is omitted
    };

    public static final String NETTY_RSA_PRIVATE_KEY = decryptRSAPrivateKey();

    private static String decryptRSAPrivateKey() {
        return new String(TEAUtils.decrypt(ENCRYPTED_NETTY_RSA_PRIVATE_KEY), StandardCharsets.UTF_8);
    }

    private GlobalConfig() {
    }
}
```

18

## Slide 19

# `Insecure creds in V2 (CVE-2025-9290)`

**_AUTH _dev = sha256sum(sha256sum(username + md5sum(password)) + randomKeyForDeviceVerify)_**

Sequence (Client <-> Controller, TCP/SSL port 28914) — the "randomKeyForDeviceVerify" and "AUTH_dev, randomKeyForSystemVerify" messages are highlighted:
- Client → Controller: Inform json (3)
- Controller → Client: **randomKeyForDeviceVerify** (1048576)
- Client → Controller: **AUTH_dev, randomKeyForSystemVerify** (1048577)
- Controller → Client: AUTH_sys (1048578)
- Client → Controller: ACK (1048579)

19

## Slide 20

# `Insecure creds in V2 (CVE-2025-9290)`

**_AUTH _dev = sha256sum(sha256sum(username + md5sum(password)) +_** **_~~randomKeyForDeviceVerify)~~_**

Sequence (Client <-> Controller, TCP/SSL port 28914) — the "randomKeyForDeviceVerify" message is struck through:
- Client → Controller: Inform json (3)
- Controller → Client: ~~randomKeyForDeviceVerify~~ (1048576)
- Client → Controller: AUTH_dev, randomKeyForSystemVerify (1048577)
- Controller → Client: AUTH_sys (1048578)
- Client → Controller: ACK (1048579)

```text
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

20

## Slide 21

# `Insecure creds in V2 (CVE-2025-15544)`

Sequence (Client <-> Controller, TCP/SSL port 28914):
- Client → Controller: Inform json (3)
- Controller → Client: randomKeyForDeviceVerify (1048576)
- Client → Controller: AUTH_dev, randomKeyForSystemVerify (1048577)
- Controller → Client: AUTH_sys (1048578)
- Client → Controller: ACK (1048579)
- Controller → Client: Propose new primary config (1048585)
- Client → Controller: Current config (1048580)
- Controller → Client: **Primary config (1048581)** — highlighted, payload shown alongside:

```json
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

(The `newPassword` / `newUsername` fields are circled in red.)

21

## Slide 22

# `Insecure creds in V2 (CVE-2025-15544)`

###### **_AUTH _dev = sha256sum(sha256sum(username + md5sum(password)) + randomKeyForDeviceVerify)_**

In the diagram, `username` and `md5sum(password)` in the formula are highlighted with lines pointing into the client's own JSON payload (the same "userAccount" object shown on the previous slide) — illustrating that these values come from the client's own unverified request.

(!) Controllers do not validate the identity of Clients

22

## Slide 23

# `Default credentials (FSCT-2025-008)`

- A brand-new Client will always have default credentials

- We can always know if a Client has default credentials

- We can always go further down the protocol state with a Controller without having any creds

- **<u>If you convince a Controller to adopt a fake Client – you get site credentials for free</u>**

Sequence (Client <-> Controller, TCP/SSL port 28914) — two lines point from "AUTH_dev, randomKeyForSystemVerify" down to the "admin / admin" callout:
- Client → Controller: Inform json (3)
- Controller → Client: randomKeyForDeviceVerify (1048576)
- Client → Controller: AUTH_dev, randomKeyForSystemVerify (1048577)
- Controller → Client: AUTH_sys (1048578)
- Client → Controller: ACK (1048579)
- Controller → Client: Propose new primary config (1048585)
- Client → Controller: Current config (1048580)
- Controller → Client: Primary config (1048581)
- Client → Controller: ACK (1048582)
- Controller → Client: Propose new secondary config (1048586)
- Client → Controller: ACK (last cfg result) (256)
- Controller → Client: Secondary config (4096)
- …

admin / admin

23

## Slide 24

# `The chain of trust`

- How is the traffic encrypted? How do Clients verify the identify of Controllers?

   - TLS certificate checks

- The “Root” cert is self signed and used as Root CA, imported into the keystore of Clients

- The “Intermediate” cert is signed by the Root and is imported into the Controllers’ trusted keystore

- The “Server” cert is used by Controllers and Clients for TLS

Certificate chain shown on the right:
- Root cert — CN: tp-link-CA, MD5: 3ACF3329C38D…
- Intermediate cert — CN: TP-LINK CA P1, MD5: DEA164E02A9E…
- Server cert — CN: localhost, MD5: 3A1A6DB1887E…

24

## Slide 25

# `The broken chain of trust (CVE-2025-15628)`

- Server certs are to expire in 2051 (!)

- Everything is hard-coded, including private keys of Server certs

- Clients will allow Local Controllers that present ANY certificate derived from Root/Intermediate -> **<u>we can reuse existing Server certs!</u>**

- Clients will allow Cloud Controllers that present a certificate derived from Root/Intermediate with a CN that ends with “tplinkcloud.com” -> we cannot forge those ☹

Certificate chain shown on the right (each with its expiry date underlined in red):
- Root cert (tp-link-CA) — Identity: tp-link-CA, Verified by: tp-link-CA, Expires: 01/19/2068
- Intermediate cert (TP-LINK CA P1) — Identity: TP-LINK CA P1, Verified by: tp-link-CA, Expires: 01/19/2068
- Server cert (localhost) — Identity: localhost, Verified by: TP-LINK CA P1, Expires: 04/20/2051

25

## Slide 26

# `Why impersonating Controllers?`

- Push VPN configs or leak private VPN keys and other sensitive information

- Also, remember CVE-2025-7850?

   - Authenticated OS command injection via the UI (Wireguard settings)

```lua
function check_key(r0_14, r1_14)
  -- line: [226, 241] id: 14
  local r2_14 = "echo \"" .. r9_0.safeSpecialString(r0_14) .. "\" |wg pubkey"
  if r4_0.fork_call(r2_14) == 1 then
    return true
  end
  if r1_14 then
    r1_14.public_key = io.popen(r2_14):read("*a")
  end
  return false
end
```

```text
echo "KPzPGI6WQ7z6bfwKYrQtpwRQwzgaU8/6wVEUtRIlslI="\n{ARBITRARY_OS_COMMAND}"" | wg pubkey
```

26

## Slide 27

## `Using fake Controllers to exploit CVE-2025-7850`

```text
manage_config_msg = {
    "header" : {
        "type" : 4096,
    },
    "body" : {
        "sequenceId": 4,
        "userAccount": {
            # ...
        },
        "wireguard": {
            "interfaces": [
                {
                    "id":878491625,
                    "operation":1,
                    "enable":"true",
                    "mtu":1420,
                    "listenPort":51820,
                    "privateKey":"[ARBITRARY OS COMMAND]",
                    "localIp":"10.10.10.1"
                }
            ]
        },
        "configVersionInc": 1,
    }
}
```

(The `privateKey` value is underlined in red.)

Sequence (Client <-> Controller, TCP/SSL port 28914):
- Client → Controller: Inform json (3)
- Controller → Client: randomKeyForDeviceVerify (1048576)
- Client → Controller: AUTH_dev, randomKeyForSystemVerify (1048577)
- Controller → Client: AUTH_sys (1048578)
- Client → Controller: ACK (1048579)
- Controller → Client: Propose new primary config (1048585)
- Client → Controller: Current config (1048580)
- Controller → Client: Primary config (1048581)
- Client → Controller: ACK (1048582)
- Controller → Client: Propose new secondary config (1048586)
- Client → Controller: ACK (last cfg result) (256)
- Controller → Client: **Secondary config (4096)** — the `manage_config_msg` JSON above is this message's payload
- …

27

## Slide 28

# `Let’s catch our breath`

- We can impersonate Clients and Local Controllers

   - RCE on unconfigured Clients

   - Get site credentials from Clients/Controllers (also with passive traffic analysis)

   - Authenticate -> RCE on Clients, pivot to the entire site

- **<u>What can we do to Controllers?</u>**

- **<u>Specifically, Cloud Controllers?</u>**

Illustration: Hieronymus Bosch's "The Conjurer", labelled with the talk's roles — Attacker (the conjuror on the right, and a pickpocket stealing a purse in the crowd, labelled "Local Controller"/"Attacker"), and Client (the woman bent over the table).

The Conjurer - Hieronymus Bosch

28

## Slide 29

### `The broken chain of trust - Cloud (CVE-2025-9192)`

```json
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

(The `cachedSvr` value is underlined in red.)

```c
__int64 ecs_verifySsl(unsigned int preverify_ok, void* store_ctx) {
    // ...
01: if ( !error_depth )
02:   {
      subject_name_str = strstr(subject_name_buf, "/CN=");
      if ( !subject_name_str )
        return 0;
      cert_subject_name = subject_name_str + 4;
      v11 = strchr(subject_name_str + 4, '/');
      if ( v11 )
        *v11 = 0;
      if ( strstr(global_controller_host, "tplinkcloud.com") && !strstr(cert_subject_name, "tplinkcloud.com") )
      {
        if ( HIDWORD(qword_5CCB8) )
          printf(
            "[ECS][ERROR]%s():%5d @ verify error:CN mismatch(%s), controllerUrl(%s).\n\r",
            "_ecs_verifySsl",
            125LL,
            cert_subject_name,
            global_controller_host);
        if ( qword_5CCB8 )
        {
          // ...
          ecs_log(2LL, "[ECS][ERROR]<%s>%s():%5d @ verify error:CN mismatch(%s), controllerUrl(%s).\n\r");
          // ...
        }
        return 0;
      }
    }
    // ...
}
```

(The `strstr(global_controller_host, "tplinkcloud.com") && !strstr(cert_subject_name, "tplinkcloud.com")` line is underlined in red.)

29

## Slide 30

### `The broken chain of trust - Cloud (CVE-2025-9192)`

”Let's eat, Grandma!” VS ”Let's eat Grandma!”

```json
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
01: if ( !error_depth )
02:   {
      subject_name_str = strstr(subject_name_buf, "/CN=");
      if ( !subject_name_str )
        return 0;
      cert_subject_name = subject_name_str + 4;
      v11 = strchr(subject_name_str + 4, '/');
      if ( v11 )
        *v11 = 0;
      if ( strstr(global_controller_host, "tplinkcloud.com") && !strstr(cert_subject_name, "tplinkcloud.com") )
      {
        if ( HIDWORD(qword_5CCB8) )
          printf(
```

(The rest of the `printf` call — its format string and arguments — is covered by the “‘Let's eat, Grandma!’ VS ‘Let's eat Grandma!’” callout box.)

```c
        if ( qword_5CCB8 )
        {
          // ...
          ecs_log( [covered by the callout box] controllerUrl(%s).\n\r");
          // ...
        }
        return 0;
      }
    }
    // ...
}
```

30

## Slide 31

### `The broken chain of trust - Cloud (CVE-2025-9192)`

”Let's eat, Grandma!” VS ”Let's eat Grandma!”

We change this to an IP address and bypass the check :-} — a line points from the JSON's `cachedSvr` field to this callout, and on to the `ecs_verifySsl` check: when `global_controller_host` is an IP address instead of a `tplinkcloud.com` subdomain, `strstr(global_controller_host, "tplinkcloud.com")` is NULL, the `&&` short-circuits false, and the CN-mismatch rejection below is skipped entirely.

```json
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
01: if ( !error_depth )
02:   {
      subject_name_str = strstr(subject_name_buf, "/CN=");
      if ( !subject_name_str )
        return 0;
      cert_subject_name = subject_name_str + 4;
      v11 = strchr(subject_name_str + 4, '/');
      if ( v11 )
        *v11 = 0;
      if ( strstr(global_controller_host, "tplinkcloud.com") && !strstr(cert_subject_name, "tplinkcloud.com") )
      {
        if ( HIDWORD(qword_5CCB8) )
          printf(
```

(The rest of the `printf` call is covered by the “‘Let's eat, Grandma!’ VS ‘Let's eat Grandma!’” callout box, and the `return 0;`/closing braces below are covered by the “We change this to an IP address and bypass the check :-}” callout box.)

31

## Slide 32

# `Client enumeration (FSCT-2025-003, FSCT-2025-011)`

- When adopting a Client via Cloud all you need to know is the S/N, no proof-of-ownership required

- S/N are sequential, can be retrieved using Omada Cloud API; Client info, **<u>such as model and MAC</u>**, can be inferred from its S/N

- **<u>VERY susceptible to brute-forcing</u>**

| INDEX | SN CODE | NAME | STATUS | RESULT |
| --- | --- | --- | --- | --- |
| 1 | 224…246 (middle digits redacted) | A8-6E-84-… (redacted) | Offline | ✗ Failed to adopt this gateway because a gateway already exists in this site. |
| 2 | 224…245 (middle digits redacted) | A8-6E-84-… (redacted) | Online | ✗ Failed to adopt this gateway because a gateway already exists in this site. |
| 3 | 224…244 (middle digits redacted) | A8-6E-84-… (redacted) | Offline | ✗ Failed to adopt this gateway because a gateway already exists in this site. |
| 4 | 224…247 (middle digits redacted) | A8-6E-84-… (redacted) | Offline | ✓ (no failure message) |

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

Sequence diagram (4 lanes: Attacker, Client, Default Cloud Controller, Regional Cloud Controller):
- Attacker ⇢ Regional Cloud Controller: Inform json (dashed red — bypasses the Client and Default Controller entirely)
- Client → Default Cloud Controller: helloCloud request
- Default Cloud Controller → Client: helloCloud response
- Regional Cloud Controller → Attacker: randomKeyForDeviceVerify
- Attacker → Regional Cloud Controller: AUTH_dev, randomKeyForSystemVerify
- Regional Cloud Controller → Attacker: AUTH_sys
- Attacker → Regional Cloud Controller: ACK
- Regional Cloud Controller → Attacker: Propose new primary config
- Attacker → Regional Cloud Controller: Current config
- Regional Cloud Controller → Attacker: Primary config
- Attacker → Regional Cloud Controller: ACK
- …
- Client → Default Cloud Controller: Inform json
- …

(The Attacker's red exchange with the Regional Controller runs independently of the Client's own blue/green exchange with the Default Controller — illustrating that the two phases are not bound to the same state machine.)

33

## Slide 34

### `Stored XSS in Controller Web UI (CVE-2025-9289)`

- The properties of adopted Clients are displayed in the Web UI

- It had an older version of jQuery that uses calls to “eval()” to execute scripts – triggers on updating the UI with Client info

```json
{"header":{"version":"2.2.0","mac":"A8:6E:84:XX:XX:XX","type":1048580,"device":"gateway","error":0,"dest":"","verCap":3},"body":{"devCap":{"supportIPsecFailover":1,"specification":{ ..."fwVer":"XXX<script>alert(1)</script>" ...}}}}
```

Screenshot: the Omada Controller Web UI showing a "Log In" / "Session expired, please reauthenticate" prompt over the Gateway/Switches/APs device list — IP …168.0.1, status CONNECTED, Serial Number 22460J5001242, MAC Address A8-6E-84-… (cut off at the slide edge).

- We could no much because of restrictive CSP

```text
Content-Security-Policy: default-src 'self' https://*.tplinkcloud.com/;script-src 'self' 'unsafe-eval' 'sha256-7W9UiBaYGlOHpT1aQBLegqffUVHbYq6/ZAb+ErjUb40=' 'sha256-VGQ8jNTL2g0e8wPwOgyCQJDqhuRgfV7gRYexcBkBe4Y=' 'sha256-x2jgB1zBLi30IsfY+VNgWjwBGeHPJxOSrzl+IdsT6k0=' 'sha256-0AHZXO4clnpdcxqdmASPBEp4JCIrtaxIX/mUuL1kzZw=' 'sha256-lfXlPY3+MCPOPb4mrw1Y961+745U3WlDQVcOXdchSQc=';style-src 'self' 'unsafe-inline';connect-src 'self' https://*.tplinkcloud.com/ https://*.tplinkcloud.com:8843/ wss://*.tplinkcloud.com/ https://*.tiles.mapbox.com https://api.mapbox.com https://events.mapbox.com ;frame-src 'self' data:;img-src 'self' https://*.tplinkcloud.com/ https://*.mzstatic.com/ https://play-lh.googleusercontent.com/ data: blob:;child-src blob: ;worker-src blob: ;object-src 'self' data: blob:
```

(The `connect-src` directive is highlighted.)

34

## Slide 35

#### `Cross-Origin Resource Sharing bypass (CVE-2025-9292)`

- The Omada Cloud infra is on AWS

- The default CSP has not been altered: allows to perform requests with JavaScript to anything  hosted on Amazon AWS

- Look at me, I am the part of your infrastructure now…

Illustration: Hieronymus Bosch's "The Conjurer", with the conjuror on the right holding up a scroll reading "Look at me / I am the / Controller / now".

```text
default-src 'self' https://*.tplinkcloud.com/; script-src 'self' 'unsafe-eval' https://www.paypal.com/ https://www.paypalobjects.com/ https://js.stripe.com 'sha256-7W9UiBaYGlOHpT1aQBLegqffUVHbYq6/ZAb+ErjUb40=' 'sha256-VGQ8jNTL2g0e8wPwOgyCQJDqhuRgfV7gRYexcBkBe4Y=' 'sha256-9dQLByJ0rMH7ojZkdfnL0p0S0pZqKxWTlh7vSa+FMg=' 'sha256-x2jgB1zBLi30IsfY+VNgWjwBGeHPJxOSrzl+IdsT6k0=' 'sha256-0AHZXO4clnpdcxqdmASPBEp4JCIrtaxIX/mUuL1kzZw=' 'sha256-lfXlPY3+MCPOPb4mrw1Y961+745U3WlDQVcOXdchSQc=' 'sha256-VohL58KrXs+2LMTip+0SXk2/JwaZNxG/j9hadIPKc2E='; style-src 'self' 'unsafe-inline'; connect-src 'self' https://*.cloudfront.net/ https://*.tplinkcloud.com/ https://*.tplinkcloud.com:8843/ http://*.tplinkcloud.com:8088/ wss://*.tplinknbu.com/ ws://localhost:*/ wss://*.tplinkcloud.com/ https://*.paypal.com/ https://api.stripe.com https://*.tiles.mapbox.com https://api.mapbox.com/ https://events.mapbox.com https://*.amazonaws.com/ data:; frame-src 'self' OmadaSightWebPlayer: vigiwebplayer: https://*.tplinkcloud.com/ https://js.stripe.com https://hooks.stripe.com https://*.paypal.com/ data: blob:; img-src 'self' https://*.cloudfront.net/ https://*.tplinkcloud.com/ https://*.amazonaws.com/ https://*.mzstatic.com/ https://play-lh.googleusercontent.com/ https://kcart.alipay.com/ data: blob:; child-src blob:; worker-src https://*.tplinkcloud.com blob:; media-src https://*.tplinkcloud.com/ https://*.cloudfront.net/ https://*.amazonaws.com/ blob:; object-src 'self' data: blob:
```

(The `; connect-src 'self' https://*.cloudfront.net/` and `https://*.amazonaws.com/` spans are underlined in red.)

35

## Slide 36

# Hippity hoppity

Your network is our property

## Slide 37

# `Local compromise`

###### **ATTACK SCENARIO:**

The attacker is positioned inside of the local network:

1. <u>Intercept the Discovery request</u> (UDP broadcast) and <u>respond as a fake Controller</u>

2. <u>Forward the Discovery request</u> (modified) <u>to the real Controller</u>, posing as a fake Client

3. The Controller responds to <u>the attacker</u>, which <u>can now Intercept, modify, and forward</u> all comms between the real Controller and the real Client (CVE-2025-15628, CVE-2025-15544 or CVE-2025-9290)

Diagram: an "Internal network" (dashed box) containing an Omada Switch and a Hardware controller, both linked by red double-headed arrows to an Attacker icon positioned between them, plus "…" (more devices). The Internal network connects bidirectionally to an ER7206/ER605 (VPN router/gateway), which connects to the Internet, which connects to a Workstation and the Omada app.

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

1. Collect MAC addresses (Omada API or just brute-force) Impersonate a not-yet-adopted Client.

2. Resend the message every 60 seconds. To target 1000 MACs attacker only needs ~17 requests per second -> <u>wait for a device ”adoption”</u>

3. Obtain original device provisioned configuration

4. Exploit the stored XSS/CSP bypass to phish admins and potentially steal Cloud account credentials

Diagram: an "Internal network" (dashed box) containing a Hardware controller, Omada Switch, and Software controller, plus "…" (more devices), connected to an ER7206/ER605 (VPN router/gateway); that gateway connects both to a Sysadmin (workstation) and, via the Internet, to an Attacker and the Omada Cloud Controller.

###### **IMPACT**

- Retrieve sensitive information (hashed site-credentials, VPN keys, etc.)

- Through stolen cloud credentials: modify device configurations, modify firewall rules, add VPNs to access internal networks, obtain “site-credentials” from site settings…

40

## Slide 40

# `DEMO VIDEO 2`

42

## Slide 41

# The chain of trust issue is way worse (CVE-2025-9293)

- <u>The same chain of trust was used in lots of other product families</u>

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

Screenshot: the Google Play Store listing for "TP-Link Tether" (TP-LINK SYSTEMS INC., In-app purchases), rated 4.6★ (732K reviews), PEGI 3, with its "50M+" Downloads count circled in red.

43

## Slide 42

# Disclosure

And takeaways

## Slide 43

# `Disclosure timeline`

Timeline markers: 0, 90, 120 (in red).

- (0) Issues are disclosed to vendor
- (90) Issues are fixed by vendor
- (120, red) Sometimes, it’s complicated…

45

## Slide 44

# `Disclosure timeline`

Timeline markers: 0, 90, 120 (in red), 426.

This is how long it took this time! (pointing to 426)

46

## Slide 45

# `Disclosure timeline`

All issues are remediated (almost)

Timeline markers: 0, 64, 140, 234, 240, 256, 389, 426. "All issues are remediated (almost)" points to 426.

- (64) Plan for all fixes (more than 300 days required)
- (140) First patches (CVE-2025-7851, CVE-2025-7850) and first blog
- (234) ”FSCT-2025-003 and FSCT-2025-011 require system-wide arch. changes […]”. No patch by, at least, day 394
- (256) Two more issues fixed (CVE-2025-9292, CVE-2025-9293)
- (389) FSCT-2025-003 and FSCT-2025-011 will not get CVE IDs, as they have low CVSS scores […]

47

## Slide 46

# `Disclosure timeline`

All issues are remediated (almost)

Timeline markers: 0, 64, 140, 234, 240, 256, 389, 426.

**13 issues got a CVE (out of 17 reported). The ”default password” issue was not fixed.**

48

## Slide 47

# `Takeaways`

- <u>For vendors</u>:

   - Bad design choices can cause serious problems later – e.g. shared vulns affecting many product families

   - Cryptography is engineering, not opinion – follow standards, use proven algorithms, plan your PKI ahead

   - Security through obscurity never works

- <u>For users</u>:

   - If you are willing to use any ZTP platforms, enable every possible security measures such 2FA, don’t use a default password, rotate passwords & keys frequently, update your devices!

49

