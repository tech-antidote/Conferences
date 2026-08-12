---
title: "Privacy Detective Sniffing Out Your Data Leaks for Android"
speakers: ["Zhengyang Zhou", "Yiman He", "Ning Wang", "Xianlin Wu", "Feifei Chen"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2024"
edition: "ASIA"
year: 2024
source_pdf: "BlackHat ASIA 2024-Slides/Zhengyang Zhou & Yiman He & Ning Wang & Xianlin Wu & Feifei Chen-Privacy Detective Sniffing Out Your Data Leaks for Android.pdf"
pages: 56
sha256: "697e2a2c0836aa78cddd20f1f852d829080aaf3265ab155c7b2834864854073e"
text_chars: 18526
ocr_pages: 5
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:53:03Z"
---
# Privacy Detective Sniffing Out Your Data Leaks for Android

**Speakers:** Zhengyang Zhou, Yiman He, Ning Wang, Xianlin Wu, Feifei Chen  
**Conference:** Black Hat ASIA 2024  
**Source:** `BlackHat ASIA 2024-Slides/Zhengyang Zhou & Yiman He & Ning Wang & Xianlin Wu & Feifei Chen-Privacy Detective Sniffing Out Your Data Leaks for Android.pdf` (56 pages)

## Slide 1

# Privacy Detective

Sniffing Out Your Data Leaks for Android

—— Abbie & Meggie

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
\ =
_ blackhat
. ASIA 2024>—~
. PRIL 18-19, 2024 | lat
Privacy Detective
Sniffing Out Your Data Leaks for Android
—— Abbie & Meggie
#BHASIA
```

## Slide 2

### About us

###### **Abbie Zhou,**

**A security researcher and engineer,** specializes in reverse, development of security features and security tools.

He **led the development of Privacy Detective** . And he has a long-standing interest in mobile security and mobile privacy related issues.

###### **Meggie He,**

**A security researcher at OPPO,** specializes in security certification, security feature research, and security tool development.

She leads in certification projects, leads the writing of OPPO's IoT security specifications, and development of this tool.

# BHASIA @BlackHatEvents

## Slide 3

## Background

# BHASIA @BlackHatEvents

## Slide 4

#### Companies Challenges

Europe

United States

Source: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4426146

# BHASIA @BlackHatEvents

## Slide 5

#### Companies Challenges

• Course of overall sum of fines (cumulative):

###### • Course of overall number of fines (cumulative):

- The maximum fine for a GDPR violation is €20 million, or 4% of a company's global annual revenue, whichever is higher.

• The sum of fines has been growing dramatically, while the number is stably increased.

Source： https://www.enforcementtracker.com/?insights

# BHASIA @BlackHatEvents

## Slide 6

#### Companies Challenges

###### • Course of overall sum of fines (cumulative):

• The maximum fine for a GDPR violation is €20

million, or 4% of a company's global annual revenue, whichever is higher.

   - The sum of fines has been growing

- Course of overall number of fines (cumulative):

dramatically, while the number is stably
increased.

- All-area companies are under legislative’s

inspection.

Source： https://www.enforcementtracker.com/?insights

# BHASIA @BlackHatEvents

## Slide 7

#### Specific External Requirements (from GDPR)

- The device should only use secure and non deprecated (TLSv1.2) channels for communication (HTTPS).

- The source code reveals hardcoded URLs.

- Only certificates signed by a trusted CA are accepted.

- Pre installed application should only communicate with servers in EU.

- Encryption is the best way to protect data during transfer and one way to secure stored personal data.

# BHASIA @BlackHatEvents

## Slide 8

#### Consumer Concerns

##### Some **third-party** E-commerce apps are like mind-reader. …

Consumers level of Privacy concern
Where are you
Maybe Singapore?
heading this
vacation?
China Global
Social Media
China Global
retailers
On Sale
Ticket to Singapore
Very concern Extremely concern

Source: https://www.pwc.com/gx/en/industries/consumer-markets/consumer-insights-survey-feb-2023.html

# BHASIA @BlackHatEvents

## Slide 9

Motivations:

- European area’s increasing regulation requirements;

- Reduce the risk of increasingly strict inspections for the company.

- Curious about convenient apps are achieved.

Objectives:

- Find non-compliance transmission behaviors and prepared for further analysis

# BHASIA @BlackHatEvents

## Slide 10

#### Preparations

We have already integrated a novice-friendly auto-deployment script in the tool， while you still need the following preparations:

1. Win 10 or higher

2. Python 3.10 or higher

3. An emotional stable security researcher : )

# BHASIA @BlackHatEvents

## Slide 11

• Overview

## Our Research

• Data collection

• Data processing

• Data analysis

# BHASIA @BlackHatEvents

## Slide 12

#### Overview

##### Supported functions:

- Network & cipher capture

- TLS decryption

- Decryption of nested encryption

- H2 header decoder

- Sensitive data scanner

# BHASIA @BlackHatEvents

## Slide 13

#### Data Collection

##### TCP&TLS Capture **TCP Socket Hook(Runtime):**

- **Hook**

- **TCP data** : “java.net.SocketOutput(Input)Stream”

- **Invoke**

- **Server name:** “getHostString()”

- **Ips:** “getLocal(Remote)SocketAddress()”

- **Ports:**

   - “getPort()”

- **Thread id:** “myTid()”

# BHASIA @BlackHatEvents

## Slide 14

#### Data Collection

##### TCP&TLS Capture

###### **TCP Socket Hook(Runtime):**

- **Hook**

- **TCP data** : “java.net.SocketOutput(Input)Stream”

- **Invoke**

- **Server name:** “getHostString()”

- • **Ips:** “getLocal(Remote)SocketAddress()”

- • **Ports:** “getPort()”

- • **Thread id:** “myTid()”

# BHASIA @BlackHatEvents

## Slide 15

#### Data Collection

##### TCP&TLS Capture

###### **SSL Hook(Native):**

- **Hook**

- **SSL data:** “libssl: SSL_read(write)”

- **Invoke**

- **SSL seq. no.:** “SSL_get_read(write)_sequence()”

- **SSL version:** “SSL_get_version()”

- **Server name:** “SSL_get_servername()”

- **Thread id:**

- “gettid()”

# BHASIA @BlackHatEvents

## Slide 16

#### Data Collection

##### TCP&TLS Capture

###### **SSL Hook(Native):**

• **Hook**

• **SSL data:** “libssl: SSL_read(write)”

- **Invoke**

- **SSL seq. no.:** “SSL_get_read(write)_sequence()”

- **SSL version:** “SSL_get_version()”

- **Server name:** “SSL_get_servername()”

- **Thread id:**

- “gettid()”

# BHASIA @BlackHatEvents

## Slide 17

#### Data Collection

##### Cipher Capture(JVM hook):

###### **Cipher Hook(Runtime):**

- **Hook (** “javax.crypto.Cipher” **)**

- **Cipher blocks:** “update()”, “doFinal()”

- **Parameters:** “chooseProvider()”

- One small tip.

# BHASIA @BlackHatEvents

## Slide 18

#### Data Collection

##### Cipher Capture(JVM hook): Bytebuffer

###### Original workflow：

###### **Cipher Hook(Runtime):**

` ` ` ` ` `

- **Hook (** “javax.crypto.Cipher” **)**

position

- **Cipher blocks:** “update()”, “doFinal()”

- **Parameters:** “chooseProvider()”

- One small tip.

# BHASIA @BlackHatEvents

## Slide 19

#### Data Collection

##### Cipher Capture(JVM hook): Bytebuffer

Original workflow：

###### **Cipher Hook(Runtime):**

` ` ` ` ` `

- **Hook (** “javax.crypto.Cipher” **)**

- **Cipher blocks:** “update()”, “doFinal()”

position

- **Parameters:** “chooseProvider()”

- One small tip.

# BHASIA @BlackHatEvents

## Slide 20

#### Data Collection

##### Cipher Capture(JVM hook): Bytebuffer

###### Original workflow：

###### **Cipher Hook(Runtime):**

` ` ` ` ` `

- **Hook (** “javax.crypto.Cipher” **)**

- **Cipher blocks:** “update()”, “doFinal()”

position

- **Parameters:** “chooseProvider()”

###### Hooked workflow：

- One small tip.

` ` ` ` ` `
`

position

# BHASIA @BlackHatEvents

## Slide 21

#### Data Collection

##### Cipher Capture(JVM hook): Bytebuffer

###### Original workflow：

###### **Cipher Hook(Runtime):**

` ` ` ` ` `

- **Hook (** “javax.crypto.Cipher” **)**

- **Cipher blocks:** “update()”, “doFinal()”

position

- **Parameters:** “chooseProvider()”

###### Hooked workflow：

- One small tip.

` ` ` ` ` `
`

position

# BHASIA @BlackHatEvents

## Slide 22

#### Data Collection

##### Cipher Capture(JVM hook): Bytebuffer

Original workflow：

###### **Cipher Hook(Runtime):**

` ` ` ` ` `

- **Hook (** “javax.crypto.Cipher” **)**

- **Cipher blocks:** “update()”, “doFinal()”

position

- **Parameters:**

“chooseProvider()”

###### Hooked workflow：

- One small tip.

` ` ` ` ` `

position

# BHASIA @BlackHatEvents

## Slide 23

#### Data Collection

##### Cipher Capture(JVM hook): Bytebuffer

###### Original workflow：

###### **Cipher Hook(Runtime):**

` ` ` ` ` `

- **Hook (** “javax.crypto.Cipher” **)**

- **Cipher blocks:** “update()”, “doFinal()”

position

- **Parameters:** “chooseProvider()”

###### Hooked workflow：

- One small tip.

` ` ` ` ` `
`

position

# BHASIA @BlackHatEvents

## Slide 24

#### Data Collection

##### Cipher Capture(JVM hook):

###### **Cipher Hook(Runtime):**

- **Hook (** “javax.crypto.Cipher” **)**

- **Cipher blocks:** “update()”, “doFinal()”

- • **Parameters:** “chooseProvider()”

- Get encryption key and parameters in chooseProvider

- Splice the blocks and return the cipher text with plain text.

# BHASIA @BlackHatEvents

## Slide 25

#### Data Collection

##### Cipher Capture(JVM hook):

###### **Cipher Hook(Runtime):**

- **Hook (** “javax.crypto.Cipher” **)**

- **Cipher blocks:**

   - “update()”, “doFinal()”

- **Parameters:**

   - “chooseProvider()”

- Get encryption key and parameters in chooseProvider

- Splice the blocks and return the cipher text with plain text.

# BHASIA @BlackHatEvents

## Slide 26

#### Data Collection

##### Cipher Capture(JVM hook):

###### **Cipher Hook(Runtime):**

- **Hook (** “javax.crypto.Cipher” **)**

- **Cipher blocks:**

   - “update()”, “doFinal()”

- **Parameters:**

   - “chooseProvider()”

- Get encryption key and parameters in chooseProvider

- Splice the blocks and return the cipher text with plain text.

# BHASIA @BlackHatEvents

## Slide 27

#### Data Processing

##### Can we decrypt TLS?

What we get in one connection?

SSL_Write SSL_Write

TCP_Send

- Time-based TLS and TCP  data sequence.

TCP_Recv

SSL_Read

SSL_Read

SSL_Write

How do TCP and TLS relate?

SSL_Write

Let’s dive into TCP/TLS workflow.

TCP_Send

……

# BHASIA @BlackHatEvents

## Slide 28

#### Data Processing

##### How do TCP and TLS relate?

##### Send Routine:

##### Receive Routine:

# BHASIA @BlackHatEvents

## Slide 29

#### Data Processing

##### Can we decrypt TLS?

What we get in one connection?

- 4 different data

One or multiple

# BHASIA @BlackHatEvents

## Slide 30

#### Data Processing

##### Can we decrypt TLS?

What we get in one connection?

- 4 different data

What is in the context of TLS?

- **TCP_Recv** follows: **one or multiple SSL_Read**

One or multiple

- **one or multiple SSL_Write** follows: **TCP_Send**

# BHASIA @BlackHatEvents

## Slide 31

#### Data Processing

##### Can we decrypt TLS?

SSL_Write

What we get in one connection?

• 4 different data

SSL_Write TCP_Send TCP_Recv

What is in the context of TLS?

- **TCP_Recv** follows: **one or multiple SSL_Read**

- **one or multiple SSL_Write** follows: **TCP_Send**

SSL_Read SSL_Read

TCP_Send

TCP_Recv SSL_Read

……

# BHASIA @BlackHatEvents

## Slide 32

#### Data Processing

##### Can we decrypt TLS?

What we get in one connection?

SSL_Write
Cipher text1
SSL_Write
Plain text1
TCP_Send

- 4 different data

What is in the context of TLS?

TCP_Recv Cipher text2
SSL_Read
Plain text2
SSL_Read

- **TCP_Recv** follows: **one or multiple SSL_Read**

TCP_Send

Plain text3

- **one or multiple SSL_Write** follows: **TCP_Send**

TCP_Recv Cipher text3
SSL_Read Plain text4

# BHASIA @BlackHatEvents

## Slide 33

#### Data Processing

##### Can we decrypt TLS? YES,

##### BUT

SSL_Write Plain text1 SSL_Write Plain text1
SSL_Write SSL_Read ????
Cipher text1
TCP_Send TCP_Send Cipher text1?
TCP_Recv Cipher text2 TCP_Recv Cipher text2
SSL_Read SSL_Read
Plain text2 Plain text2?
SSL_Read SSL_Read
TCP_Send Plain text3 TCP_Send Plain text3
TCP_Recv Cipher text3 SSL_Read ????
Plain text4 ????
SSL_Read SSL_Read
…… ……

# BHASIA @BlackHatEvents

## Slide 34

#### Data Processing

##### Can we decrypt TLS?

##### BUT

In one app or service, there may be multiple TCP connections.

SSL_Write Plain text1
SSL_Read ????
TCP_Send Cipher text1?
TCP_Recv Cipher text2
SSL_Read
Plain text2?
SSL_Read
TCP_Send Plain text3
SSL_Read ????
SSL_Read ????
……

# BHASIA @BlackHatEvents

## Slide 35

#### Data Processing

##### Can we decrypt TLS?

How to find one TCP connection?

- Match the ip and port in TLS & TCP.

SSL_Write IP: 1.2.3.4  Port:66 SSL_Write IP:1.2.3.4  Port: 66 TCP_Send IP 1.2.3.4 Port: 66

TCP_Recv IP: 1.2.3.4 Port:66 SSL_Read IP:1.2.3.4 Port: 66

TCP_Recv

**IP:2.3.3.3 Port:101** SSL_Read **IP:2.3.3.3 Port:101**

# BHASIA @BlackHatEvents

## Slide 36

#### Data Processing

Can we decrypt TLS? How to find one connection?

- Theoretically, we can match the ip and port in TLS & TCP.

- Practically, we cannot obtained the ip and port in TLS.  T^T

# BHASIA @BlackHatEvents

## Slide 37

#### Data Processing

##### Can we decrypt TLS?

How to find one connection?

- Theoretically, we can match the ip and port in TLS & TCP.

- • Practically, we cannot obtained the ip and port in TLS.

- **So, we move to thread id**

# BHASIA @BlackHatEvents

## Slide 38

#### Data Processing

##### Can we decrypt TLS?

###### SSL_Write

Thread id: 23333

How to find one connection?

###### SSL_Write

Thread id: 23333

###### TCP_Send

- Theoretically, we can match the ip and port in TLS & TCP.

- • Practically, we cannot obtained the ip and port in TLS.

Thread id: 23333

###### TCP_Recv

**Thread id: 12345**

###### TCP_Recv

Thread id: 23333

###### SSL_Read

Thread id: 23333

###### SSL_Read

- **So, we move to thread id**

**Thread id: 12345**

……

# BHASIA @BlackHatEvents

## Slide 39

#### Data Processing

##### Can we decrypt TLS?

How to find one connection?

SSL_Write Thread id: 23333

SSL_Write Thread id: 23333

TCP_Recv **Thread id: 12345** SSL_Read **Thread id: 12345**

TCP_Send

- Theoretically, we can match the ip and port in TLS & TCP.

Thread id: 23333

TCP_Recv Thread id: 23333

- Practically, we cannot obtained the ip and port in TLS.

SSL_Read

Thread id: 23333

- **So, we move to thread id**

# BHASIA @BlackHatEvents

## Slide 40

#### Data Processing

##### New encryption?

##### What are captured?

- Sequenced TLS and TCP data stream

- Sorted data stream by thread id.

What’s this?

- Matched TCP and TLS.

What We Get?

- Plain TCP data！

- But everything done?!

# BHASIA @BlackHatEvents

## Slide 41

#### Data Processing

##### New encryption?

##### What are captured?

- Sequenced TLS and TCP data stream

- • Sorted data stream by thread id.

- Matched TCP and TLS.

##### H2 head compress

- What We Get?

   - Plain TCP data！

- But everything done?!

# BHASIA @BlackHatEvents

## Slide 42

#### Data Processing

##### How to decompress HTTP/2.0 header completely? 1. Implement the algorithm to reverse the h2 encode algorithm.

2. Use the existing libraries.

Fake a connection.

3. What we get？

TCP_Send

TCP_Recv TCP_Send TCP_Send

# BHASIA @BlackHatEvents

## Slide 43

#### Data Processing

How to decompress HTTP/2.0 header completely? 1. Implement the algorithm to reverse the h2 encode algorithm.

2. Use the existing libraries. Fake a connection. 3. What we get？ TCP_Send TCP_Recv TCP_Send TCP_Send

# BHASIA @BlackHatEvents

## Slide 44

#### Data Analysis

##### Privacy info scanner:

We used a self-developed regex-based script to scan the plaintext. We highly recommend researchers have their own scan rules, or use open-source libs.

# BHASIA @BlackHatEvents

## Slide 45

#### Data Analysis

##### Our findings:

- **Xprivacy**

- • **Virtualdroid** • **Godinsec**

- **Daniu**

• **……**

# BHASIA @BlackHatEvents

## Slide 46

#### Data Analysis

##### Our findings:

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat e< =
ASIA 2024
Data Analysis
Our findings:
"transformation": "DES/CBC/PKCS5Padding”,
"pblock_size": 8,
"“opmode”": 2,
"plain": "53454C45435420434F554E542830292046524F4D206576656E74207768657265206C6576656C3C3D3F”,
“plain_string": "SELECT COUNT(@) FROM event where level<=?",
"crypto": "@F3436FF35CCB8376C6AC43D385069E381E5B2E19B54E7874DDEC5337A5FDCF649F 6DD8723D80B63FEQ@Q0C5DA7D580622" ,
“password”: | "
J
DIRE : "Wy "
```

## Slide 47

Data Analysis

##### Our findings:

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2024
Data Analysis
Our findings:
“plain_string"™: “{\ ; \"android_id\":\"2c 60\",\"did\":\"\",
"bssid\":\"68: :a1\",\"mac\":\" 98: 7C5\",\"imei\":\"\",\"imei2\":\"\",
"imsi\"\"\",\"meid\  \"\",\"sn\"s\"\",\"apn\":\"wifi\", \"net\":\"WIFI\", \"wifi\":\"on\",
"mno\":\"unknown\", \"iccid\":\"\",
“uuid\":\"@000 7524\",
"dpid\":\"4@3l ; “040\",
"union_id\":\"b92° a ‘179\",\'
```

## Slide 48

#### Data Analysis

##### Our findings:

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat > <
ASIA 2024
Data Analysis
Our findings:
"src-ip": "192.168.137.177",
"src-port": 51230,
“dst-ip": "13.36.124.147",
"dst-port": 443,
“timestamp”: "2024-03-12 12:00:31:767377",
“thread_id": 28541,
"tls": "TLSv1.2",
"hostname": “weather -com",
“funcname": “TCP_send”,
"hex": .
"str": "HTTP/2.@ [<RequestReceived stream_id:11, headers:[(‘':method', ‘POST'), (‘:path', ‘/weather/location
), (‘:authority', ‘weather -com'), (‘:scheme’, ‘https‘),
(‘cipherinfo', ‘{\"crypto-cipher-service\":{\"tmpPublicKey\" : \"MFkwEwYHKoZ1zj@CAQYIKoZIzj@DAQcDQgAEOFA4U2\\\\/
MlgHjt+yh2eh@1i6R@QaBFfnpP\\\\/4Dqoww12JuD5wLMQhnjgR\\\\/2noJndIB5I1v4QN5q8BxA@u4DCXcRAA==\" ,
\"salt\":\"Y6W8M1FiPVH84DsYL88rnTIXmfBr62b1iGvufSY2R76U=\", \"info\" :\"d2VhdGhlciilsb2NhdGlvbi1zZXJ2awWN1\"}}"),
(‘wrapperkey', ‘{\"cipher\":\"389cN4NAPOmxX3Samiac58gb@eZmJ2s49RhVwXuPGnfPudUwatJIR19\\\\/205Pz62g\\\\/OMEVF\\\\/
CFpNdOf1xofsBOBnX3eNECb53db+n\\\\/Zz0+zZeliBvJFh6\\\\/1+s=\", \"iv\":\"RRWwGTbEi4WYaPSP\"}'), (‘encryptflag',
"3'), (‘content-type’', ‘application/json; charset=utf-8'), (‘content-length', ‘380'), (‘accept-encoding',
‘gzip'), (‘user-agent', ‘okhttp/4.9.0')]>, <DataReceived stream_id:11, flow_controlled_length:38@,
data: 7b2261637469766174696f6e54696d657374616d>, <StreamEnded stream_id:11>] Data:
{\"bssid\":\"86: 704\",\"latitude\":\"KUCVOSYF\",\"ssid\":\"\\\" WA s
\"todayLocateCnt\":\"10\", \"longitude\": \"KkOIIJ@IWQ==\", \"ts\":\"2024-03-12 12:00:30 GMT+08:00\"}",
"num": 37,
“identity”: {
"MAC": [
"86:
```

## Slide 49

#### Data Analysis

##### Our findings:

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat P< S
ASIA 2024
Data Analysis
Our findings:
{
“transformation”: "AES/CTR/NoPadding”,
"“plock_size": 16,
“opmode": 1,
"plain": "3 aur
sDlainesthrincecmadd | Oa.
"crypto": "2A4388209D@959",
"password": "16
"Iv": "D4
"transformation": "“AES/CTR/NoPadding",
"plock_size": 16,
“opmode": 1,
jllenigQes 3) 3) er
"“plain_string": "2 . 35",
"crypto": "2940953B9605",
"password": "16
es
```

## Slide 50

#### Deployment

# BHASIA @BlackHatEvents

## Slide 51

#### Deployment

##### Automation:

- Install.bat :

Install or upgrade dependency;

- Init.bat :

Push Frida-server into device;

- run.bat :

Run Frida & Invoke disable-usap.bat; Waiting kill command.

# BHASIA @BlackHatEvents

## Slide 52

• **Add UDP support**

## Prospects

- **Add Chrome & Firefox core support**

- **Add pcap output**

• **Rewrite a Xposed version**

# BHASIA @BlackHatEvents

## Slide 53

• **Add UDP support**

Prospects

• **Add Chrome & Firefox core support**

• **Add pcap output**

• **Rewrite a Xposed version**

# BHASIA @BlackHatEvents

## Slide 54

#### Takeaways

- How to decrypt TLS in TCP traffic without IP info.

- ➢ By using Linux thread ID as the feature, and through analysis of the packet sequences, we decrypt TLS traffic on Android without IP, port or certificate information.

- How to decrypt nested encrypted TCP data.

- ➢ We hooked most implementations of “Cipher” class to get all the encryption and decryption data, then restored the double-encrypted content in TCP. But please be careful with Byte Buffer.

- How can we protect our privacy from tracking.

- ➢ As we showed on “Our findings” slides. For a Android user, we highly suggest you to use the latest version to obtain the newest security & privacy strategy, practice the principle of least privilege.

# BHASIA @BlackHatEvents

## Slide 55

## Q&A

# BHASIA @BlackHatEvents

## Slide 56

## The End

# BHASIA @BlackHatEvents
