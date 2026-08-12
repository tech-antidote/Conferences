---
title: "Should We Chat, Too Security Analysis of WeChat's MMTLS Encryption Protocol"
speakers: ["Pellaeon Lin", "Mona Wang", "Jeffrey Knockel"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2025"
edition: "ASIA"
year: 2025
source_pdf: "Black Hat Asia 2025 Slides/Pellaeon Lin & Mona Wang & Jeffrey Knockel_Should We Chat, Too Security Analysis of WeChat's MMTLS Encryption Protocol.pdf"
pages: 48
sha256: "e6af322ee74f330ccbc4a320af10d15100dfe61bec07d663b9d0f5f75ab1d974"
text_chars: 16088
ocr_pages: 10
has_ocr: true
redacted_secrets: 0
ocr_confidence: 83.3
ocr_unreliable_blocks: 0
vision_verified_blocks: 1
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T03:56:19Z"
---
# Should We Chat, Too Security Analysis of WeChat's MMTLS Encryption Protocol

**Speakers:** Pellaeon Lin, Mona Wang, Jeffrey Knockel  
**Conference:** Black Hat ASIA 2025  
**Source:** `Black Hat Asia 2025 Slides/Pellaeon Lin & Mona Wang & Jeffrey Knockel_Should We Chat, Too Security Analysis of WeChat's MMTLS Encryption Protocol.pdf` (48 pages)


## Slide 1

**Thursday, April 3 2025**

Security Analysis of WeChat’s <u>MMTLS Encryption Protocol</u>

**Pellaeon Lin, Mona Wang**

## Slide 2

- **Introduction, motivation, methodologies**

Agenda **Security Analysis of WeChatʼs MMTLS Encryption Protocol**

- **WeChat network request lifecycle**

- **MMTLS encryption, Business-layer encryption**

- **Discussion, recommendations, future work**

## Slide 3

## Pellaeon Lin

- **Researcher at Citizen Lab, University of Toronto**

- **Security and privacy of mobile apps**

- **Past studies**

   - **TikTok vs Douyin - A Security and Privacy Analysis**

   - **Unmasked II: An Analysis of Indonesia and the Philippinesʼ Government-launched COVID-19 Apps**

   - **Unmasked: COVID-KAYA and the Exposure of Healthcare Worker Data in the Philippines**

## Slide 4

## Mona Wang

- **Networking security researcher, PhD student at Princeton CITP**

- ● **OTF Information Controls Research Fellow at Citizen Lab**

- **Previously technologist at EFF**

- **Other work**

   - **Network measurement (CoNEXT 22)**

   - **Traffic fingerprinting resistance and censorship circumvention (PETS 22)**

   - **Threat modelling and security training for organizers (CSCW 22)**

- **https://m0na.net**

## Slide 5

## Slide 6

## Motivation

#### **Whatʼs being sent?**

**Is the encryption sound?**

**Why custom encryption?**


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 89/100 on the text kept, 84/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Motivation

What's being sent?          Is the encryption sound?          Why custom encryption?

[Wireshark packet list]
No.      | Time  | Source        | Destination    | Protocol | Length | Info
  33 170...  Android.local  43.130.30.2...  HTTP       652  POST /mmtls/7d44b6a2 HTTP/1.1
  76 170...  Android.local  49.51.67.253    HTTP       658  POST /mmtls/2a9b1264 HTTP/1.1
  92 170...  Android.local  49.51.67.253    HTTP       392  POST /mmtls/2a9b1264 HTTP/1.1
 111 170...  Android.local  49.51.67.253    HTTP       713  POST /mmtls/582198f5 HTTP/1.1
 116 170...  Android.local  49.51.67.253    HTTP       863  POST /mmtls/582198f5 HTTP/1.1
 121 170...  Android.local  49.51.67.253    HTTP       670  POST /mmtls/582198f5 HTTP/1.1
 126 170...  Android.local  49.51.67.253    HTTP       670  POST /mmtls/582198f5 HTTP/1.1
 134 170...  Android.local  49.51.67.253    HTTP       730  POST /mmtls/582198f5 HTTP/1.1

[packet detail pane - lines clipped at pane edge]
> Frame 92: 392 bytes on wir
> Ethernet II, Src: Android.
> Internet Protocol Version
> Transmission Control Proto
> [5 Reassembled TCP Segment
> Hypertext Transfer Protoco
> Data (5704 bytes)

[hex pane]
00e0   43 6c 69 65 6e 74 0d 0a   0d 0a 19 f1 04 00 a1 00
00f0   00 00 9d 01 04 f1 01 00   a8 4f 67 76 fb b4 66 8f
0100   2a 36 bb 55 74 94 c4 0c   cd c8 bb f4 44 41 b0 24
0110   d8 8e c4 86 29 cc 35 e2   1b 65 6e 78 3c 00 00 00
0120   6f 01 00 00 00 6a 00 0f   01 00 00 00 63 01 00 09
0130   3a 80 00 00 00 00 00 3d   00 0c ce 4f 44 55 2e a9
0140   34 fc aa d4 e9 af 00 48   00 f2 e6 a8 76 9f b1 1a
0150   95 cc b8 9b aa 47 4a 75   e1 41 fc ef 7a f6 fc ba
0160   89 30 ca 4e ff fe dc 68   23 bb fe 14 69 09 64 54
0170   0b 40 a4 49 9b d5 6f 7b   69 7f 3e e6 9e 2b 18 fe
0180   75 68 6c b5 15 70 80 a6   06 59 9e 00 f8 bc 1f 3e
```

## Slide 7

## Motivation

#### **SSL/TLS**

- **Secures billions of users traffic**

- ● **30+ years of development**

- ● **Open standard, lots of academic and public scrutiny**

#### **WeChat MMTLS**

- **Secures 1+ billion users traffic**

- ● **Deployed for ~8 years**

- ● **One public blog post**

**MMTLS deserves just as much scrutiny as TLS!!!**

## Slide 8

WeChat network request lifecycle

## Slide 9

# Anatomy of a Wechat network request

- **API endpoint is referred to as “Scene”, has unique “type” number and URI**


> Recovered by OCR — confidence 86/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
/* renamed from: com.tencent.mm.model.bm */
e API endpoint is referred to as
/* loaded from: classes3.dex */
23 public final class MMReqRespReg2 extends ReqRespBase { Scene ’ has unique type number
/* renamed from: pcn */ and URI
private final MMReg2.Req reqobj = new MMReg2.Req( );
/* renamed from: pco */
private final MMReg2.Resp respobj = new MMReg2.Resp( );
aOverride /Z com tencent .p486mm.network .MMTLSConnection
public fingl int getType() {
return }126;
}
public final String getUri() {
}
```

## Slide 10

Anatomy of a Wechat network request

- **Request and response formats are defined using Protobuf**

- ● **Screenshot shows a portion of the request Protobuf fields**

## Slide 11

OpenSSL

Encryptor (MMProtocalJni.so)
● Encrypts byte arrays
using crypto specified by
Serializer (reqToBuf)
● Serialize the object into  2 API type
bytearrays Business-layer
Encryption
API object
(NetSceneBase)
● Defines structure of
API data, what type
of encryption to use
1
Other components can make this specific
API call by calling  SomeAPI.doScene

## Slide 12

OpenSSL

OpenSSL
Encryptor (MMProtocalJni.so)
● Encrypts byte arrays
using crypto specified by
Serializer (reqToBuf)
● Serialize the object into  2 API type
bytearrays Business-layer
Encryption
API object
(NetSceneBase)
● Defines structure of
Start Network Task API data, what type
Task manager (NetCore)
of encryption to use
● Manages  3
long/short link
connection tasks
● Adds task to
network queue
1
Blue=native,  Other components can make this specific
green=Java API call by calling  SomeAPI.doScene

## Slide 13

Outgoing connections OpenSSL
5
MMTLS shortlink (HTTP) Socket connector Encryptor (MMProtocalJni.so)
serializer Makes TCP connection ● Encrypts byte arrays
Serialize MMTLS headers (records) and  using crypto specified by
Serializer (reqToBuf)
generates HTTP headers ● Serialize the object into  2 API type
bytearrays Business-layer
MMTLS  Encryption
Encryption
4
MMTLS shortlink manager (worker) API object
● Handles MMTLS handshaking (NetSceneBase)
● Pools connections, rate limit
● Defines structure of
Start Network Task API data, what type
of encryption to use
Task manager (NetCore) 3
● Manages
long/short link
connection tasks
● Adds task to
1
network queue

Blue=native,
green=Java

Other components can make this specific API call by calling SomeAPI.doScene

## Slide 14

Outgoing connections OpenSSL
Incoming
5
response
MMTLS shortlink (HTTP) Socket connector Encryptor (MMProtocalJni.so)
serializer Makes TCP connection ● Encrypts byte arrays
6 Serialize MMTLS headers (records) and  using crypto specified by
Serializer (reqToBuf)
generates HTTP headers ● Serialize the object into  2 API type
bytearrays Business-layer
MMTLS  Encryption
Encryption
4
MMTLS shortlink manager (worker) API object
To handle the  ● Handles MMTLS handshaking (NetSceneBase)
● Pools connections, rate limit
response, implement  ● Defines structure of
SomeAPI.onSceneE Start Network Task API data, what type
nd method. It’s a
callback method Task manager (NetCore) 3 of encryption to use
when a response is ● Manages
received, decrypted,
and deserialized. long/short link
connection tasks
● Adds task to
1
network queue

Blue=native, green=Java

Other components can make this specific API call by calling SomeAPI.doScene

## Slide 15

# One more thing…

“Mars”

- **Mars is Tencentʼs cross-platform infrastructure component, written in C++**

- **Network requests are handled by submodule “** **_STN_ ”**

- **Mars is partially open source**

   - **_mars-open_ is the open source part**

   - ○ **_mars-private_ : “potentially open sourced”**

   - **_mars-wechat_ : wechat-specific code,** **<u>including MMTLS encryption</u>**

Mars- Mars-
private wechat

**mars-open**

## Slide 16

# One more thing…

“Mars”

- **Mars is Tencentʼs cross-platform infrastructure component, written in C++**

- **Network requests are handled by submodule “** **_STN_ ”**

- **Mars is partially open source**

   - **_mars-open_ is the open source part**

   - **_mars-private_ : “potentially open sourced”**

   - **_mars-wechat_ : wechat-specific code,**

   - **Mars-oincluding MMTLS encryptionpen helps us reverse engineer other closed-source parts ;-)**

**Marswechat**

**Marsprivate**

**mars-open**

## Slide 17

WeChat network encryption

## Slide 18

How does WeChat encrypt requests?

## Slide 19

How does WeChat encrypt requests?


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
How does WeChat encrypt requests?
THE! LAB
```

## Slide 20

## How does WeChat encrypt requests?

**Two transport protocols: Longlink and Shortlink**

#### **Longlink**

- **TCP, port 8080**

- ● **Long-lived connection**

- ● **Supports multiple request-response cycle**

- ● **Likely used for server-initiated transmissions**

IP

TCP

MMTLS

Busines

s-layer

## Slide 21

## How does WeChat encrypt requests?

**Two transport protocols: Longlink and Shortlink**

#### **Shortlink**

- **HTTP POST, port 80**

IP

- **Short-lived connection**

- **Supports single request-response cycle**

- ● **Used for most client-initiated transmissions**

TCP

HTTP

MMTLS

Businesslayer

## Slide 22

## How does WeChat encrypt requests?

**Encrypted twice (and also differently if youʼre logged-out)**

**Key derivation Encryption Library MMTLS layer** DH with resumption AES-GCM with tag libwechatnetwork.so **Business-layer, logged-out** Static DH AES-GCM with tag libwechatmm.so **Business-layer, logged-in** Fixed key from server AES-CBC with checksum libMMProtocalJNI.so

## Slide 23

## How does WeChat encrypt requests?

**Logged-in example of network request encryption:**

MMTLS headers
WeChat request
headers
AES-GCM w/
ciphertext2
Protobuf  AES-CBC w/  ECDH-derived key
ciphertext1
data “session key”
“MMTLS” encryption
“Business-layer” encryption
● Added in 2016
●
Found and reported many issues

## Slide 24

## MMTLS “records”

MMTLS ServerHello Packet
Handshake record
Data record
Alert record

TLS ServerHello Packet
Handshake record
Data record

## Slide 25

## MMTLS **MMTLS record headers**

> **19 f1 04 Handshake resumption**

**16 f1 04 Handshake 17 f1 04 Data 15 f1 04 Alert**

### **TLS record headers**

> **16 03 04 Handshake**

**17 03 04 Data 15 03 04 Alert**

## Slide 26

MMTLS handshake


> Recovered by OCR — confidence 82/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
MMITLS handshake
Unencrypted : :
Record Encrypted Record : :
: FIRST SHORTLINK :
LONGLINK * * FUTURE SHORTLINK
CONNECTION : CONNECTION (HANDSHAKE) : CONNECTIONS
Client Server : | Client | Server : | Client Server
ClientHelio : ClientHello : ClientHello
(client publickey) : (client publickey) : {resumption ticket)
: : Extensions
¢ ServerHello : ¢ ServerHello :
hw (server publickey) : a (server publickey) : EarlyData
Server certificate : Server certificate : ClientFinished
Resumption ticket : Resumption ticket :
ServerFinished : ServerFinished : ba ServerHello
: : Server certificate
ClientFinished > : : Application Data
Application Data : : ServerFinished
es Application Data > : :
```

## Slide 27

## MMTLS Layer

- **Modifications from TLS 1.3:**

   - **Limited ciphersuite selection, pinned keys and certificate (since WeChat controls both client and server)**

- **AES-GCM + tag for encryption, authenticity**

- ● **Public documentation on** **<u>Github</u>**

- **Public flaws: lack of forward secrecy, heavy use of session resumption implies no replay resistance**

## Slide 28

## Business-Layer

Logged out LoggING in Logged in


> Recovered by OCR — confidence 79/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Business-Layer
Unencrypted Encrypted key : :
BUSINESS-LAYER: : BUSINESS-LAYER: : BUSINESS-LAYER:
ASYMMETRIC MODE : RETRIEVING SESSION KEY . SYMMETRIC MODE
Request = > : Request for > : | »
(client publickey) . (client publickey) . Request metadat
: :
Response metadata : Response metadata :
(server publickey) : P* (server publickey) : a Response metadata
: | session “new_secret :
Logged out LoggING in Logged in
```

## Slide 29

## Business-Layer (Logged out)

- **Static Diffie-Hellman**

   - **static public server key + newly generated client key to generate session key**

   - ○ **No forward secrecy (e.g. if static private server key is compromised, all session can be compromised)**

- **AES-GCM + tag for encryption, authenticity**

## Slide 30

## Business-Layer (Logged in)

- **Uses key given by server**

   - **Server sends key to client encrypted with “logged-out” encryption– highly unusual!**

- **AES-CBC + checksum**

   - **Checksum is forgeable and provides no cryptographic guarantees**

- **Prior to 2016, this was the only layer of encryption…**

   - **But it leaks metadata such as user ID and request URI**

   - **Acknowledged by Tencent to be one reason to develop MMTLS Encryption**

## Slide 31

## Disclosure

- **We reported to Tencent, suggested to switch to QUIC/TLS1.3 or remove Business-layer encryption altogether**

- ● **They replied saying they would upgrade Business-layer encryption to use AES-GCM instead of AES-CBC**

- **???**

- **Possibly, Business-layer encryption is the** **_only_ layer of encryption within WeChat internal networks**

- **This is also bad: means WeChat data could be subject to surveillance**

## Slide 32


> Recovered by OCR — confidence 75/100 on the text kept, 65/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
TOP SECRET//SI//NOFORN
ers Current Efforts - Google
GFE = Greale
End Xe
TOP SECRET//SI//NOFORN
THECITIZENLAB
```

## Slide 33

Discussion

## Slide 34

## It’s not just WeChat…

Source: <u>https://www.businessofapps.com/data/most-popular-apps/</u> (1/30/2025)

## Slide 35

## Which always use HTTPS/TLS?

WeChat 1,012 Douyin 695
Alipay 901 QQ 583
Taobao 795 Facebook 571
TikTok 773 WhatsApp 527
Instagram 759 Baidu 491
Pinduoduo 728 Kuaishou 480

*but theyʼre also **not not** encrypting… they are often **using proprietary cryptography**

## Slide 36

## HTTPS adoption on mobile?

**12.9%** of top 1k apps sent plaintext traffic. **3.5%** of top 1k apps used proprietary cryptography.

**65.4%** of top 1k apps sent plaintext traffic. **47.6%** of top 1k used proprietary cryptography! **(Chinese version)**

## Slide 37

## Is the proprietary cryptography secure?

We manually analyzed the **9** most popular proprietary protocols globally… **8** contained severe vulnerabilities where we broke the encryption!

The remaining one was **MMTLS… !**

## Slide 38

## Why does this matter?

- **Bad encryption enables** **_mass surveillance and MITM._**

- ● **If apps use bad encryption, users of those apps are more vulnerable to mass surveillance by all governments and attackers.**

- **Not just Chinese people are affected!**

   - **Chinese apps have sizable international user base**

      - **E.G. RedNote/XiaoHongShu:** **<u>https://citizenlab.ca/2025/02/network-security-issues-in-rednote/</u>**

   - **Non-Chinese apps may still use Chinese SDK**

## Slide 39


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
TOP SECRET STRAP1
Response to improving security
For the past decade, NSA has lead an
aggressive, multi-pronged effort to break widely
used Internet encryption technologies
Cryptanalytic capabilities are now coming on line
Vast amounts of encrypted Internet data which
have up till now been discarded are now
exploitable
Major new processing systems, SIGDEV efforts
and tasking must be put in place to capitalize on
this opportunity
PTD “We penetrate targets’ defences.”
This information is exempt from disclosure under the Freedom of informaiion Act 2000 and may be subject to exernption under
cc HO Soother UK information legislaton. Refer disclosure requests lo GCHQ
© Crown Copyright Alll rights reserved.
```

## Slide 40


> Recovered by OCR — confidence 91/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Success Stories
* UCWeb mobile browser identification
* Discovered by GCHQ analyst during DSD workshop
* Chinese mobile web browser — leaks IMSI, MSISDN,
IMEI and device characteristics
```

## Slide 41


> Recovered by OCR — confidence 67/100 on the text kept, 45/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ucweb
C) State © Datetime = Datetime End Browser Version i Address: Handset Mode! MEL MSI Global Tile Platform Active User Casenotation
THECITIZENLAB
```

## Slide 42

## Discussion:

Why do Chinese apps prefer custom cryptography?

- **Distrust in TLS?**

   - **Early concerns on TLS Certificate Authority ecosystem circa 2011**

- **Obfuscation mechanism?**

   - **Why not just use commercial packers?**

- **OS performance / compatibility ?**

   - **Fragmented Android OS and app store ecosystem increases the need for dirty patches and workarounds**

- **Network filtering?**

   - **Prevalent ISP filtering and traffic poisoning prompts the need for dirty patches**

- **“Not invented here” problem?**

- **Technical debt / inertia**

## Slide 43

## Discussion:

Why do Chinese apps prefer custom cryptography?

- **Distrust in TLS?**

- **Early concerns on TLS Certificate Authority ecosystem circa 2011**

- ● **Obfuscation mechanism?**

   - **Why not just use commercial packers?**

- **OS performance / compatibility ?**

   - **Fragmented Android OS and app store ecosystem increases the need for dirty patches and workarounds**

**Probably a mix of all**

- **Network filtering?**

- **reasons!**

- **Prevalent ISP filtering and traffic poisoning prompts the need for dirty patches**

- ● **“Not invented here” problem?**

- **Technical debt / inertia**

## Slide 44

Discussion: How can we improve security in ~~Chinese~~ ALL apps?

- **Continued study of privacy and security of consumer apps?**

- ● **Researchers should engage more with Global South developers and security engineers?**

- **App store reviews/attestation of network security?**

- **OS vendors should provide better documentation, easy-to-use development tools?**

## Slide 45

Thank you! Questions? **pellaeon@citizenlab.ca monaw@princeton.edu**

**Link to full report**

## Slide 46

Appendix

## Slide 47

Isolate
Scrape popular  Install  Simulate user  Entropy  Protocol
non-TLS
applications app behavior analysis clustering
traffic

## Slide 48

Is the proprietary cryptography secure?


> Recovered by OCR — confidence 77/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Is the proprietary cryptography secure?
Protocol family # apps ome Paes dene MAU Decryptable Fixed? pcre reduest
Kuaishou SDK 76 35.10B Kuaishou 692 mill YES YES Device metadata
fF 82 30.30B mz ma YES Tried to |Device metadata
PY 15 25.43B Y | | YES NO Browsing data
PY 7 17.62B | m7 YES NO — |Browsing data
iQIYl 3 11.28B iQIYI 429 mill YES YES Network metadata
fF 37 10.34B m7 | YES NO Security config*
*contained vuln s.t. network attackers can read file contents on users phones
```
