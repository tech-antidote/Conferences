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
text_chars: 17505
ocr_pages: 11
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:07:04Z"
---
# Should We Chat, Too Security Analysis of WeChat's MMTLS Encryption Protocol

**Speakers:** Pellaeon Lin, Mona Wang, Jeffrey Knockel  
**Conference:** Black Hat ASIA 2025  
**Source:** `Black Hat Asia 2025 Slides/Pellaeon Lin & Mona Wang & Jeffrey Knockel_Should We Chat, Too Security Analysis of WeChat's MMTLS Encryption Protocol.pdf` (48 pages)


## Slide 1

**Thursday, April 3 2025**

Security Analysis of WeChat’s <u>MMTLS Encryption Protocol</u>

**Pellaeon Lin, Mona Wang**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Thursday, April 3 2025
Security Analysis of WeChat's
MMILS Encryption Protocol
Pellaeon Lin, Mona Wang
munkschool & 1 ORSNTo
```

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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
What’s being sent?
Motivation
Is the encryption sound?
| Time | Source | Destination | Protocol
33 170... Android. local 43.
76 170.. Android.local 49.
Android.
111 17@.. Android.local 49.
116 17@.. Android. local 49.
121 170... Android.local 49.
126 17@.. Android.local 49.
134 17@.. Android.local 49.
Frame 92: 392 bytes on wir
Ethernet II, Src: Android.
Internet Protocol Version
Transmission Control Proto
[5 Reassembled TCP Segment
Hypertext Transfer Protoco
> Data (5704 bytes)
130.30.2.. HTTP
51.67.253 HTTP
51.67.253 HTTP
51.67.253 HTTP
51.67.253 HTTP
51.67.253 HTTP
51.67.253 HTTP
| Length | Info
652 POST /mmtls/7d44b6a2 HTTP/1.
658 POST /mmtls/2a9b1264 HTTP/1.
/mmtls/2a9b1264 HTTP/1.
713 POST /mmtls/582198f5 HTTP/1.
863 POST /mmtls/582198f5 HTTP/1.
67@ POST /mmt1ls/582198f5 HTTP/1.
67@ POST /mmt1ls/582198f5 HTTP/1.
730 POST /mmtls/582198f5 HTTP/1.
Why custom encryption?
PPP PRP Pp
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
/* renamed from: com.tencent.mm.model.bm */
e API endpoint is referred to as
/* loaded from: classes3.dex */
6c ” H 6c ”
23 public final class MMReqRespReg2 extends ReqRespBase { Scene ’ has unique type number
/* renamed from: pcn */ and URI
private final MMReg2.Req reqobj = new MMReg2.Req( );
/* renamed from: pco */
private final MMReg2.Resp respobj = new MMReg2.Resp( );
aOverride /Z com tencent .p486mm.network .MMTLSConnection
public fingl int getType() {
return }126;
}
@Override // com.tencent .p486mm.network.MMTLSConnection
public final String getUri() {
return J"/cgi-bin/micromsg-bin/newreg"
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Business-Layer
Unencrypted Encrypted key : :
BUSINESS-LAYER: : BUSINESS-LAYER: : BUSINESS-LAYER:
ASYMMETRIC MODE : RETRIEVING SESSION KEY . SYMMETRIC MODE
Client | | Sever |: | Client Sever |: Client | | Server
Request = > : Request for > : | »
(client publickey) . (client publickey) . Request metadat
Request Data “ S@fet Request Data | “Sere: Request Data “ S°ssion
: :
Response metadata : Response metadata :
(server publickey) : P* (server publickey) : a Response metadata
Response Data _/NeW_secret Response Data“ "eW_secret: Response Data “Session
Ei ceescetetts | Esibrnctisisl
: | session “new_secret :
: a :
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
TOP SECRET//SI//NOFORN
ers Current Efforts - Google
GFE = Greale
Fort
End Xe
Server ere.
TOP SECRET//SI//NOFORN
eee
ininm
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Success Stories
* UCWeb mobile browser identification
* Discovered by GCHQ analyst during DSD workshop
* Chinese mobile web browser — leaks IMSI, MSISDN,
IMEI and device characteristics
eee
ininm
ata) THECITIZENLAB
ab
```

## Slide 41

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ucweb
@ Hep Actons* Reports» View»
C) State © Datetime = Datetime End Browser Version i Address: Handset Mode! MEL MSI Global Tile Platform Active User Casenotation
+) 1 A 2012.05-1302:29:20 2012-05-13 02:29:23 8.0.3.107 23movies ——nokiae90-4 19379900100 java E9DHL00000K0000
2 £) 1 & — 2012-05-13.06:00:59 2012-05-13 06:01:00 8.0.3.107 23movies ——nokiae90-4 9379900100 java E9DHL00000M0000
af) 1 & 201205431939: 2012-05-13 19:39:11 7.9.3.103 HTC AS100 android £E980€00000!0000
4) 1 2 2012.05-1492:29:53 2012-05-1412:29:53 8.0.4.121 WokiaE72-4 E9DHL.00000m0000
5) 1B 2012-05-14 174646 Py 2012-05-14 17:46:46 8.0.4.121 Imasti —_Nokiax6.00 16H125221450000
6) 1 & 2012-05-15 18:28:19 fy 2012-05-15 18:26:19 8.0.4.421 sti NokiaX6-00 93781090013 15H125221450000
7 OL) 1 2012-05-15 20:02:58 3 5 2012-05-15 20:02:5€ 8.0.4.121 Nokiax6.00 193781090013 sis 1451H1252214500¢
eee
ininm
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Is the proprietary cryptography secure?
Protocol family # apps ome Paes dene MAU Decryptable Fixed? pcre reduest
Kuaishou SDK 76 35.10B Kuaishou 692 mill YES YES Device metadata
fF 82 30.30B mz ma YES Tried to |Device metadata
PY 15 25.43B Y | | YES NO Browsing data
fF 11 18.10B mz | YES NO — |DNS requests
PY 7 17.62B | m7 YES NO — |Browsing data
iQIYl 3 11.28B iQIYI 429 mill YES YES Network metadata
fF 37 10.34B m7 | YES NO Security config*
PY 38 9.02B m7 | YES NO  |Device metadata
*contained vuln s.t. network attackers can read file contents on users phones
```
