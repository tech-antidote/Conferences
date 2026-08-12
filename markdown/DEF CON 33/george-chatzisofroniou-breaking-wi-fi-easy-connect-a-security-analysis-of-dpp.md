---
title: "Breaking Wi-Fi Easy Connect A Security Analysis of DPP"
speakers: ["George Chatzisofroniou"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33/George Chatzisofroniou - Breaking Wi-Fi Easy Connect A Security Analysis of DPP.pdf"
pages: 70
sha256: "1360aca22414781b5da6a7015f3a71d8e85e419a99e97fb52540b27b17d372e1"
text_chars: 21881
ocr_pages: 3
has_ocr: true
redacted_secrets: 0
ocr_confidence: 78.6
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T07:00:37Z"
---
# Breaking Wi-Fi Easy Connect A Security Analysis of DPP

**Speakers:** George Chatzisofroniou  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33/George Chatzisofroniou - Breaking Wi-Fi Easy Connect A Security Analysis of DPP.pdf` (70 pages)


## Slide 1

**Breaking Wi-Fi Easy Connect A security Analysis of DPP**

George Chatzisofroniou (@_sophron)

# **DEF CON 33**

August 7-10, 2025 | **Las Vegas**

Presented research has also been peer-reviewed and published in:

_Chatzisofroniou, G., Kotzanikolaou, P. Security analysis of the Wi-Fi Easy Connect. Int. J. Inf. Secur. 24, 74 (2025). https://doi.org/10.1007/s10207-025-00988-3_

## Slide 2

## **whoami**

- Performed infrastructure and application security assessments for Fortune 500 companies across Africa, Asia, Europe, and North America

- Over a decade of research focused on Wi-Fi security and protocol analysis

- Published novel association techniques (e.g., Known Beacons, Lure10)

- Author of wifiphisher, an open-source framework combining Wi-Fi attacks with phishing strategies

2

## Slide 3

## **Wi-Fi Easy Connect**

- Released by the Wi-Fi Alliance in 2018 as a companion to WPA3

- Designed as a secure and user-friendly replacement for WPS

- Supports the growing demand for IoT device onboarding with minimal user interaction

- Supports multiple bootstrapping methods: QR codes, NFC, BLE, PKEX

- Addresses security flaws in WPS (e.g., offline PIN brute-force attacks)

- Based on Device Provisioning Protocol (DPP)

- Uses public key cryptography for authentication and secure provisioning between devices.

- ● Certification is limited, but adoption is rising: ~32 certified devices across 12 vendors (as of July 2025).

- Primarily used in Android (10+) as Initiator only — cannot act as Configurator/Responder.

3

## Slide 4

## **Roles in WiFi Easy Connect**

**Initiator - Responder**

**STA - AP**

- ●

- **STA (Station)** : The **Initiator** : Entity that client device — phone, starts DPP laptop, toaster — that authentication. connects to a Wi-Fi ● **Responder** : Entity network by that answers initiation associating with an of the DPP AP. authentication.

- ● ● **AP (Access Point)** : The Example: Phone network's gatekeeper. (Initiator) provisioning

- ● STA joins the BSS a smart plug managed by the AP (Responder).

**Configurator - Enrollee**

- **Configurator** : Trusted device that provisions network credentials.

- ● **Enrollee** : Device being provisioned to join the network.

- Configurator acts as “the gatekeeper” issuing credentials securely.

4

## Slide 5

## **Phases of Wi-Fi Easy Connect**

##### **Initiator Responder**

**1. Bootstrapping** _Bootstrapping_

- Initial step to establish trust.

- ● Uses QR code, NFC, BLE, or PKEX for device discovery and public key exchange.

5

## Slide 6

## **Phases of Wi-Fi Easy Connect**

##### **Initiator**

**1. Bootstrapping**

- Initial step to establish trust. _Receives_

- ● Uses QR code, NFC, BLE, or _Responder’s Public Bootstrapping Key_

- PKEX for device discovery and public key exchange.

- ● Successful bootstrapping = both sides exchange and store each other’s public keys

- ● public bootstrapping keys = credentials!

##### **Responder**

Receives
Initiator’s Public
Bootstrapping Key
6

_Bootstrapping_

## Slide 7

## **Phases of Wi-Fi Easy Connect**

##### **Initiator Responder**

##### **2. Authentication**

● Leverages exchanged public _Receives_ keys to perform mutual _Responder’s Public_ authentication and key _Bootstrapping Key_ agreement.

_Bootstrapping Receives Initiator’s Public Bootstrapping Key_

_Authentication_

7

## Slide 8

## **Phases of Wi-Fi Easy Connect**

##### **Initiator Responder**

**2. Authentication**

- Leverages exchanged public _Receives_

- keys to perform mutual _Responder’s Public_ authentication and key _Bootstrapping Key_ agreement.

- ● Successful authentication = both sides derive the same _Established symmetric key_

- symmetric key

_Bootstrapping_

_Receives Initiator’s Public Bootstrapping Key Authentication Established symmetric key_

8

## Slide 9

Initiator Responder
Phases of Wi-Fi Easy Connect
3. Configuration Bootstrapping
● Establish actual  Receives
Receives
communication keys,  Responder’s Public  Initiator’s Public
Bootstrapping Key
known as the connector  Bootstrapping Key
keys (Connector-I and  Authentication
Connector-R respectively).
Established
Established
symmetric key
symmetric key
Configuration
Acts as
Acts as
Configurator or
Configurator or
Enrollee
Enrollee
9

## **Phases of Wi-Fi Easy Connect**

## Slide 10

Initiator Responder

## **Phases of Wi-Fi Easy Connect**

4. Network Access Bootstrapping
● Enrollee uses  Receives
Receives
provisioned  Responder’s Public  Initiator’s Public
Bootstrapping Key
credentials to connect  Bootstrapping Key
to the Wi-Fi network. Authentication
●
Operates under
Established
WPA2 or WPA3 for  Established
symmetric key
subsequent data  symmetric key
communication. Configuration
Acts as
Acts as
Configurator or
Configurator or
Enrollee
Enrollee
Network Access
Enrollee may  Enrollee may
receive  receive
Connector Connector

10

## Slide 11

1. Recon  2. Αccess  3. Own

11

## Slide 12

## **Recon**

- Discover active Wi-Fi Easy Connect (DPP) networks and connected clients

- **Method 1** : Sniff Beacon frames or Probe Responses advertising DPP AKM

- **Method 2** : Force downgrade on Enrollees attempting private introduction

12

## Slide 13

AP
STA
Bootstrapping
Authentication
Configuration
Network Access

13

## Slide 14

## **Private Introduction Protocol**

##### **Initiator Responder** _Private Peer Introduction_

14

## Slide 15

## **Private Introduction Protocol**

Initiator Responder
Private Peer Introduction
Private Peer Introduction Notify

15

## Slide 16

||**Initiator**|**Responder**|
|---|---|---|
|**Private Protocol**|||
|**Downgrade**|_Private Peer Introduction_
_Private Peer Introduction Notify_
**Connector  is**
**transmitted**
**encrypted**||

16

## Slide 17

## **Private Protocol Downgrade**

Initiator Attacker
Private Peer
Introduction
Block

##### **Responder**

17

## Slide 18

## **Private Protocol Downgrade**

Initiator Attacker
Private Peer
Introduction
Block
Peer Discovery Request

##### **Responder**

Private Peer
Introduction
Block
Peer Discovery Request
18

## Slide 19

Initiator Attacker Responder
Private Protocol
Private Peer
Introduction
Downgrade
Block
Peer Discovery Request
Peer Discovery Response

19

## Slide 20

20


> Recovered by OCR — confidence 68/100 on the text kept, 42/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
AyqUePKh/2uuPkDTz5mYHi PDSTASBENVBAUECINNRVJ TSCO3NDCOMBIGCgmS J omT8i xKAQUEBGJ LZXIwCgYIKoZ1IzjQ@EAWMDaQA
SM-g3MFKNeMU3mhdPCpUXFt9B3Y6p6jm3",
DEFCON | 29
```

## Slide 21

SSID

21


> Recovered by OCR — confidence 74/100 on the text kept, 43/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
“cred":{" akm":"dotix","entCreds":{"
SM-g3MFKNeMU3mhdPCpUXFt9B3Y6p6jm3",
DEFCON | 2!
Hjyof9rrj5A08
```

## Slide 22

## **Wi-Fi Alliance Response**

“Wi-Fi Alliance considers the attack an acceptable risk. Inducing the abandonment of the Private Introduction Protocol and forcing the use of Network Introduction Protocol is merely privacy-exposing as it will expose the non-AP STA’s connector to a passive attacker.”

22

## Slide 23

## **Proposed Remediation**

- Future DPP specifications should validate STA preferences from the AP during subsequent exchanges

- ● Ensure ongoing verification of the STA’s intent and configuration parameters throughout the session

23

## Slide 24

1. Recon  2. Αccess  3. Own

24

## Slide 25

AP
STA
Bootstrapping
Authentication
Configuration
Network Access

25

## Slide 26

## **Wi-Fi Provisioning Method: PKEX**

- Public Key Exchange (PKEX) protocol

- Password-authenticated key exchange within Wi-Fi Easy Connect

- ● Relies on shared secrets (like a short numeric code)

- Elliptic Curve Diffie-Hellman (ECDH)

26

## Slide 27

### **Group Selection in PKEX (Initiator ↔ Responder)**

- Initiator proposes a cryptographic group (e.g., ECC curve) in the initial message

- Responder either:

   - Accepts the group (proceeds with same group)

   - Or downgrades to a different group if it doesn't support the proposed one

27

## Slide 28

**PKEX Group Exchange**

##### **Initiator**

##### **PKEX Exchange Request** **_(group = 26)_**

##### **Responder**

Groups Ordered by Preference

Initiator:         26, 30, 29, 27 Responder:   30, 29, 28, 27

28

## Slide 29

**PKEX Group Exchange** Groups Ordered by Preference Initiator:         26, 30, 29, 27 Responder:   30, 29, 28, 27

##### **Initiator**

##### **Responder**

**PKEX Exchange Request** **_(group = 26)_ PKEX Exchange Response** **_(group = 30)_**

29

## Slide 30

**PKEX Group Downgrade Attack**

Groups Ordered by Preference Initiator:         26, 30, 29, 27 Responder:   30, 29, 28, 27

##### **Initiator**

##### **Attacker**

##### **Responder**

**PKEX Exchange Request** **_(group = 26)_**

**PKEX Exchange Response** **_(group = 30)_**

###### **Block**

30

## Slide 31

**PKEX Group Downgrade Attack**

Groups Ordered by Preference Initiator:         26, 30, 29, 27 Responder:   30, 29, 28, 27

##### **Initiator**

**Attacker Responder PKEX Exchange Request** **_(group = 26)_ PKEX Exchange Response** **_(group = 30)_ Block PKEX Exchange Response** **_group = 27_**

31

## Slide 32

**PKEX Group Downgrade Attack**

Groups Ordered by Preference Initiator:         26, 30, 29, 27 Responder:   30, 29, 28, 27

##### **Initiator**

##### **Attacker**

##### **Responder**

**PKEX Exchange Request** **_(group = 26)_ PKEX Exchange Response** **_(group = 30)_ Block PKEX Exchange Response** **_group = 27_**

**PKEX Exchange Request** **_(group = 27)_**

32

## Slide 33

## **PKEX Group Downgrade Attack**

- DPP’s group negotiation lacks cryptographic safeguards present in WPA3’s SAE (802.11) group negotiation.

- Weak group selection = weaker DH exchange = easier brute-force

- Some curves, like certain NIST P-curves, are avoided due to opaque parameter generation and potential backdoor concerns

- Exploitation is uncommon in typical environments due to practical constraints

33

## Slide 34

## **Wi-Fi Alliance Response**

“Wi-Fi Alliance will take this matter under discussion and decide a course of action regarding cryptographic protection of group negotiation.”

34

## Slide 35

## **Proposed Remediation**

- Responder includes supported groups in the signed commitment during the Commit-Reveal phase

- If the commitment from Responder ≠ locally computed version → tampering detected, likely downgrade attempt

- Initiator aborts the protocol if mismatch is found

35

## Slide 36

AP
STA
Bootstrapping
Authentication
Configuration
Network Access

36

## Slide 37

## **DPP Mixed Authentication**

- Not all devices implement the full DPP spec — some support only limited provisioning methods (e.g., QR code only).

- Network operators may enable multiple provisioning options (e.g., QR code and PKEX) to support diverse device capabilities

- Some provisioning methods skip mutual auth

- Result: Mixed authentication modes co-exist within the same network.

37

## Slide 38

## **DPP Mixed Authentication**

##### **Initiator 1**

##### _Mutual authentication_

##### **Responder**

38

## Slide 39

|**Initiator 2**|**Initiator 1**
**Responder**|
|---|---|
|**DPP Mixed**||
|**Authentication**|_Mutual authentication_
_Responder authentication only_|

39

## Slide 40

## **QR Code Authentication Mode**

- QR code provisioning uses single-factor auth—unlike PKEX, BLE, or NFC, which support mutual auth

- ● Initiator authenticates the Responder by scanning its public key—but the Responder never fully authenticates the Initiator

- Trust is implicitly granted just because the Initiator holds the public key—no identity verification occurs in return

- If an attacker locates the QR code (i.e., the public key), they can bypass the stronger auth expected in methods like PKEX

40

## Slide 41

### **Locating Static QR Codes via DPP Auth Request Sniffing**

- DPP Authentication Requests contain the bootstrapping key hash, linking them to a specific QR code used during provisioning.

- If a static QR code (e.g., printed on a wall) is used repeatedly, the same hash will be observed in multiple Auth Requests over time.

- By passively capturing these frames across different monitoring points, triangulation techniques can estimate the QR code's physical location.

41

## Slide 42

## **Wi-Fi Alliance Response**

“[The DPP protocol]... is not required to perform non-mutual in the event that mutual is not available. This is a policy decision for the deployed Enrollee”

42

## Slide 43

## **Proposed Remediation**

- The Wi-Fi Alliance likely intended mixed auth modes for flexibility — but flexibility can backfire

- Wi-Fi environments are inherently hostile: spoofing, sniffing, and downgrades are trivial

- Many operators lack the expertise to properly manage multi-method auth setups

- Protocol should not allow mixing weak and strong auth — it creates silent downgrade paths

- If mutual authentication is enabled, all connections should be forced to use it — no exceptions

- A strict “mutual-auth only” mode would ensure the Responder always verifies the Initiator

- Some DPP implementations may enforce this already — but unless it’s baked into the spec, it’s not guaranteed

43

## Slide 44

1. Recon  2. Gain access  3. Own

44

## Slide 45

AP
STA
Bootstrapping
Authentication
Configuration
Network Access

45

## Slide 46

## **QR Code Evil Twin**

46


> Recovered by OCR — confidence 93/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
QR Code Evil Twin
SCAN THE QR CODE
BELOW TO
CONNECT TO THE
CONFERENCE WI-FI
IGNORE ALL OTHER
QR CODES — THE
ONE BELOW IS THE
OFFICIAL WI-FI
CONNECTION
DEFC@N | 46
```

## Slide 47

## **PKEX Code Reuse Exploitation**

- hostapd & PKEX Reuse (CVE-2022-37660)

- PKEX codes (a.k.a. passwords) were not deleted after successful pairing—against spec requirements.

- ● Public key regenerated each time, but same code stays alive = replay & impersonation possible.

- Exploit path: Attacker reuses the same code to masquerade as a legit Responder and hijack new clients.

47

## Slide 48

## **PKEX Code Re-use**

##### **Initiator**

Generates ephemeral **X, x M = X + H(code)**

##### **Responder**

48

## Slide 49

## **PKEX Code Re-use**

**Initiator** Generates ephemeral **X, x M = X + H(code)**

**PKEX Exchange Request** _(_ **_M_** _)_

##### **Responder**

49

## Slide 50

## **PKEX Code Re-use**

**Initiator** Generates ephemeral **X, x M = X + H(code)**

**PKEX Exchange Request** _(_ **_M_** _)_

##### **Responder**

**X = M - H(code)**

50

## Slide 51

## **PKEX Code Re-use**

**Initiator Attacker** Generates ephemeral **X, x PKEX Exchange M = X + H(code) Request** _(_ **_M_** _)_ **Block**

##### **Attacker**

##### **Responder**

51

## Slide 52

## **PKEX Code Re-use**

**Initiator Attacker** Generates ephemeral **X, x PKEX Exchange M = X + H(code) Request** _(_ **_M_** _)_ **Block**

##### **Attacker**

##### **Responder**

**X = M - H(code)**

52

## Slide 53

## **PKEX Code Re-use**

**Initiator Attacker Responder** Generates ephemeral **X, x PKEX Exchange M = X + H(code) Request** _(_ **_M_** _)_ **Block** **_Continue_ X = M - H(code)** **_Bootstrapping_**

53

## Slide 54

## **PKEX Code Re-use**

**Initiator Attacker Responder** Generates ephemeral **X, x PKEX Exchange M = X + H(code) Request** _(_ **_M_** _)_ **Block** **_Continue_ X = M - H(code)** **_Bootstrapping Authentication Configuration Network Access_**

54

## Slide 55

AP
STA
Bootstrapping
Authentication
Configuration
Network Access

55

## Slide 56

Enrollee Configurator
DPP
DPP Bootstrapping
Configuration
DPP Authentication
Established
Established
symmetric ke
symmetric ke

56

## Slide 57

Enrollee Configurator
DPP
DPP Bootstrapping
Configuration
DPP Authentication
Established
Established
DPP Configuration Request
symmetric ke
symmetric ke
{netRole = Enrollee}ke

57

## Slide 58

Enrollee Configurator
DPP
DPP Bootstrapping
Configuration
DPP Authentication
Established
Established
DPP Configuration Request
symmetric ke
symmetric ke
{netRole = Enrollee}ke
DPP Configuration Response
{configurationPayload}ke

58

## Slide 59

Attacker Configurator
Configurator
Impersonation  DPP Bootstrapping
Attack
DPP Authentication
Established
Established
DPP Configuration Request
symmetric ke
symmetric ke
{netRole = Configurator}ke

59

## Slide 60

Attacker Configurator
Configurator
Impersonation  DPP Bootstrapping
Attack
DPP Authentication
Established
Established
DPP Configuration Request
symmetric ke
symmetric ke
{netRole = Configurator}ke
DPP Configuration Response
{DPPEnvelopedData}ke

60

## Slide 61

## **DPPEnvelopedData**

- A container format for securely backing up and restoring Configurator credentials

- Used to enable multiple Configurators in a DPP network

- Management of the storage location and its security is completely vendor-specific

- Password-derived key encryption — crack the password, decrypt the envelope, own the network

61

## Slide 62

#### Obtain S, c, dkLen, DPPAssymetricKeyPackage from DPPEnvelopedData

Set P = next word from dictionary
Calculate DK = PBKDF2(P, S, C, dkLen)
Decrypt DPPAssymetricKeyPackage with derived DK
NO
Success?
YES
Obtain privacy-protection-key from
62
DPPAssymetricKeyPackage

## Slide 63

## **One Key to Own Them All**

- Privacy Protection Key (PPK) key is shared across all Configurators—past, present, and compromised

- With PPK in hand, attacker can sign and distribute rogue network configs

- Rogue configs = full control: impersonate APs, redirect traffic, MITM all clients

- One bad Configurator = global compromise of the Wi-Fi Easy Connect network

63

## Slide 64

## **Wi-Fi Alliance Response**

“Wi-Fi Alliance will consider allowing for other methods of protecting the DPPEnvelopedData, in addition to the password method which is considered an acceptable risk.”

64

## Slide 65

## **Proposed Remediation**

- Wi-Fi Alliance’s current fix is insufficient — password-based method still exploitable, and DPPEnvelopedData remains at risk.

- **Fix #1** – Authorization Checks:

   - Enforce authorization logic before granting Configurator status.

   - Validate Enrollee identity against policy-based controls.

   - Prevent rogue Configurator promotion attempts.

- **Fix #2** – Per-Configurator Keys:

   - Assign a unique cryptographic key to each Configurator.

   - Eliminates shared-key risk. Breach of one ≠ breach of all.

65

## Slide 66

AP
STA
PKEX Downgrade Bootstrapping
PKEX Code Re-Use
Authentication
QR Code Evil Twin
Mixed Authentication
Configuration
Configurator Impersonation
Network Access
Privacy Protection
Protocol Downgrade

66

## Slide 67

AP
STA
PKEX Downgrade Bootstrapping
PKEX Code Re-Use
Authentication
QR Code Evil Twin
Mixed Authentication
Configuration
Configurator Impersonation
Network Access
Privacy Protection
Protocol Downgrade

67

## Slide 68

## **Conclusions**

- Several protocol-level vulnerabilities are inherent to the DPP design — mitigation requires spec updates

- ● Migration from WPS to DPP shifts risk to network operators, demanding security-savvy deployment

- Usability-driven enhancements (v2/v3) have weakened the protocol’s security posture

- Features like mixed auth modes and Configurator impersonation open new vectors for abuse

- Lack of revocation mechanisms for critical keys leads to persistent compromise risk

- Protocol adoption must be matched with operator education and clear provisioning policies

68

## Slide 69

**Breaking WiFi Easy Connect A security Analysis of DPP**

George Chatzisofroniou (@_sophron)

**DEF CON 33**

August 7-10, 2025 | **Las Vegas**

Presented research has been peer-reviewed and published in:

_Chatzisofroniou, G., Kotzanikolaou, P. Security analysis of the Wi-Fi Easy Connect. Int. J. Inf. Secur. 24, 74 (2025). https://doi.org/10.1007/s10207-025-00988-3_

## Slide 70

## **References**

- Chatzisofroniou, G., Kotzanikolaou, P. Security analysis of the Wi-Fi Easy Connect. Int. J. Inf. Secur. 24, 74 (2025). https://doi.org/10.1007/s10207-025-00988-3

- Wi-Fi Alliance.Wi-Fi Protected Setup (WPS) Specification version 1.0h. 2006. link (2015)

- Viehbck, S.: Wi-Fi Protected Setup online pin brute force vulnerability (2011)

- Wi-Fi Alliance. Device provisioning protocol (dpp) specification, Technical Specification, Wi-Fi Alliance, Latest Version. link (2025). Accessed 02 Jan 2025

- Wi-Fi Alliance. Wi-Fi Alliance product finder. link. Accessed 07 Jan 2023

- Group, N.: Ble proximity authentication vulnerable to relay attacks. Available: link (2023). Accessed 02 Jan 2025

- Nobles, P.: Vulnerability of IEEE802.11 WLANs to MAC layer DoS attacks. In: IET Conference Proceedings, pp. 14–14(1). link (2004)

- Bernstein D.J., Hamburg, M., Krasnova, A., Lange, T.: Elligator: elliptic-curve points indistinguishable from uniform random strings. In: Proceedings of the 2013 ACM SIGSAC conference on Computer & Communications Security, pp. 967–980 (2013)

- WiFi Alliance: WPA3 specification version 1.0. Available: link

- Vanhoef, M., Ronen, E.: Dragonblood: analyzing the dragonfly handshake of WPA3 and EAP-pwd. In: IEEE Symposium on Security & Privacy (SP). IEEE (2020)

- Chatzisofroniou, G., Kotzanikolaou, P.: Association attacks in IEEE 802.11: exploiting WiFi usability features. In: Proceedings of the International Workshop on Socio-Technical Aspects in Security and Trust (STAST). Springer , pp. 107–123 (2019)

- National Institute of Standards and Technology (NIST): A closer look at revocation and key compromise in public key infrastructures. National Institute of Standards and Technology, Tech. Rep. link (2023). Accessed 02 Jan 2025

- IEEE Standard for Local and Metropolitan Area Networks–PortBased Network Access Control, IEEE Std. 802.1X-2010. link (2010)

- Common Vulnerability and Exposure database: CVE-2022-37660. link (2022)

- Rondon, L.P., Babun, L., Aris, A., Akkaya, K., Uluagac, A.S.: Survey on enterprise internet-of-things systems (e-iot): a security perspective. Ad Hoc Networks, vol. 125, p. 102728. link (2022)

- Vanhoef, M., Piessens, F.: Key reinstallation attacks: Forcing nonce reuse in wpa2. In: Proceedings of the 2017 ACM SIGSAC Conference on Computer and Communications Security, ser. CCS ’17. ACM, New York, NY, USA, pp. 1313–1328. link (2017)

- Vanhoef, M.: A time-memory trade-off attack on wpa3’s sae-pk. In: Proceedings of the 9th ACM on ASIA Public-Key Cryptography Workshop, ser. APKC ’22, pp. 27–37. Association for Computing Machinery, New York, NY. link (2022)

- Marais, S., Coetzee, M., Blauw, F.: Simultaneous deauthentication of equals attack. In: Wang, G., Chen, B., Li, W., Di Pietro, R., Yan, X., Han, H. (eds.) Security, Privacy, and Anonymity in Computation, Communication, and Storage, pp. 545–556. Springer, Cham (2021)

- Kampourakis, V., Chatzoglou, E., Kambourakis, G., Dolmes, A., Zaroliagis, C.: Wpaxfuzz: sniffing out vulnerabilities in wi-fi implementations. In: Cryptography, vol. 6, no. 4. link (2022)

- Chatzoglou, E., Kambourakis, G., Kolias, C.: How is your WiFi connection today? DoS attacks on WPA3-SAE. J. Inf. Secur. Appl. 64, 103058 (2022)

- Chatzisofroniou, G., Kotzanikolaou, P.: Exploiting WiFi usability features for association attacks in IEEE 802.11: attack analysis and mitigation cont

70
