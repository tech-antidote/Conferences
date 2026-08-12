---
title: "AppleStorm - Unmasking the Privacy Risks of Apple Intelligence"
speakers: ["Yoav Magid"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33/Yoav Magid - AppleStorm - Unmasking the Privacy Risks of Apple Intelligence.pdf"
pages: 66
sha256: "6e2be6976baa7e772f23eb04595d65d8cb753490ea381278ba8b08bdb972c791"
text_chars: 21160
ocr_pages: 34
has_ocr: true
redacted_secrets: 0
ocr_confidence: 89.8
ocr_unreliable_blocks: 2
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T07:17:24Z"
---
# AppleStorm - Unmasking the Privacy Risks of Apple Intelligence

**Speakers:** Yoav Magid  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33/Yoav Magid - AppleStorm - Unmasking the Privacy Risks of Apple Intelligence.pdf` (66 pages)


## Slide 1

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence

Speaker: Yoav Magid

## Slide 2

How many of you own an Apple device?

2

## Slide 3

###### **U.S. Mobile OS Usage Share**

###### U.S. Desktop OS Usage Share

0.4% 2.5% 2.5% 9.3%
38.1%
61.4%
29.6%
56.1%

3

## Slide 4

How many of you use Siri?

4


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
How many of you
use Siri?
DEFCGN
```

## Slide 5

5


> Recovered by OCR — confidence 91/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BIBIC
Home News Sport Business Innovation Culture Arts Travel Earth Audio Video Live
Apple to pay $95m to settle Siri
7 January 2025 Share < Save []
Imran Rahman-Jones
Technology reporter
DEFCON
```

## Slide 6

**How many of you use Apple Intelligence?**

6

## Slide 7

### **Apple Intelligence**

Siri

**Writing Tools**

**Image Playground**

7

## Slide 8

8

## Slide 9

9


> Recovered by OCR — confidence 90/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Is Your Data Private? By: Yoav Magid Share yy ++
Is Your Data Private? By: Yoav Magid
The Secret
The Secret
```

## Slide 10

##### Yoav Magid

10


> Recovered by OCR — confidence 94/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
DEFCON
Yoav Magid
Team Lead & Al Researcher
```

## Slide 11

## Agenda

Behind Apple Intelligence’s Curtains

Risks & Methodology

“Hey Siri, What can you do?”

What can we do?

## Slide 12

# Apple Intelligence's Infrastructure

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Apple Intelligence's Infrastructure

12

## Slide 13

### Enhance Productivity While Protecting Your Data!

Private Cloud Compute
On-device models Server models

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Apple Intelligence's Infrastructure

13

## Slide 14

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Apple Intelligence's Infrastructure 14


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Apple Intelligence & Privacy
Apple Intelligence is designed to protect your information.
When you initiate an Apple Intelligence task, a model running on your device analyzes whether the task
can be completed on device. If a larger, server-based model is required, Apple Intelligence uses Private
Cloud Compute to send only data relevant to your request to be processed on Apple silicon servers.
Apple only collects limited information about the request, such as the approximate size of the request and
DEFCE&SN AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Apple Intelligence's Infrastructure
```

## Slide 15

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Apple Intelligence's Infrastructure 15


> Recovered by OCR — confidence 91/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Apple Intelligence, Siri, and Search
Apple devices must be able to connect to the following hosts to process Apple Intelligence requests that
use Private Cloud Compute and to process Siri requests, including dictation and searching in Apple apps.
Hosts
guzzoni.apple.com
*smoot.apple.com
TCP_MISS/200
TCP_MISS/200
TCP_MISS/200
TCP_MISS/200
TCP_MISS/200
TCP_MISS/200
TCP_MISS/200
TCP_MISS/200
TCP_MISS/200
TCP_MISS/200
TCP_MISS/200
TCP_MISS/200
TCP_MISS/200
TCP_MISS/200
TCP_MISS/200
TCP_MISS/200
TCP_MISS/200
TCP_MISS/200
apple-r
apple-r
cp4.clo
apple-
relay.ap
TCP_MISS/200
TCP_MISS/200
D
escription
Siri and dictation requests
4931
4656
4656
4931
4629
4656
4930
4656
4931
4656
5206
6959
6959
1041
CONNECT
CONNECT
CONNECT
CONNECT
CONNECT
CONNECT
CONNECT
CONNECT
CONNECT
CONNECT
CONNECT
CONNECT
CONNECT
CONNECT
smoot.
smoot.
smoot.
smoot.
smoot.
smoot
smoot.
smoot.
smoot.
api.smoot.
bookkeeper.
bookkeeper.
bookkeeper.
6959 CONNECT bookkeeper.
1057 CONNECT bookkeeper.
22868 CONNECT init.itunes
5155 CONNECT xp.apple.com
5155 CONNECT xp.apple.com
api.
api.
api.
api.
api.
api.
api.
api.
api.
AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Apple Intelligence's Infrastructure
apple.
apple.
apple.
apple.
apple.
apple.
apple.
apple.
apple.
apple.
itunes
itunes
itunes
itunes.
itunes.
Search services, including Siri, Spotlight,
252.
252.
252.
252.
252.
252.
252.
252.
252.
+253
+253
+253
+253
+253
+250
+250
+250
com: 443 d Music
com: 443
com: 443
com: 443
com: 443
-apple.
HIER_DIRECT/17.
HIER_DIRECT/17.
HIER_DIRECT/17.
HIER_DIRECT/17.
HIER_DIRECT/17.
HIER_DIRECT/17.
HIER_DIRECT/17.
HIER_DIRECT/17.
HIER_DIRECT/17.
HIER_DIRECT/17.252.11.248
HIER_DIRECT/17.252.11.248
com:443 - HIER_DIRECT/23.217.226
com:443 — HIER_DIRECT/23.217.226
com:443 — HIER_DIRECT/23.217.226
apple.com:443 — HIER_DIRECT/23.217.226
apple.com:443 — HIER_DIRECT/23.217.226
sapple.com:443 — HIER_DIRECT/23.217.226.217
sapple.com:443 — HIER_DIRECT/23.217.226.217
2443 - HIER_DIRECT/17.154.66.107 -
a
```

## Slide 16

# Risks & Methodology

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Risks & Methodology

16


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Risks &
Methodology
DEFCE&SN AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Risks & Methodology
```

## Slide 17

Private
What?
Cloud
On-device vs. PCC
Which data?

How? _Network Inspection_

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Risks & Methodology

17

## Slide 18

###### Siri Search Dictation

###### HTTPS Connection

###### Cloud Models Extensions

###### QUIC Connection

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Risks & Methodology

18

## Slide 19

## Private Cloud Compute

System Settings -> Privacy & Security -> Apple Intelligence Report

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Risks & Methodology

19

## Slide 20

## Siri’s Services

guzzoni.apple.com HTTPS ?

*.smoot.apple.com
HTTPS
Protobuf

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Risks & Methodology

20

## Slide 21

#### **SSL**

_Enabled via SSL/TLS certificates issued by trusted Authorities._

###### Certificate Pinning

_A technique to a specific certificate or public key to an The app all certificates not matching the pinned one to prevent Adversary-in-the-Middle._

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Risks & Methodology

21

## Slide 22

## Tools

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Risks & Methodology

22


> Recovered by OCR — confidence 92/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
DEFCON
mitmproxy
AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Risks & Methodology
22
```

## Slide 23

## assitantd

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Risks & Methodology

23


> Recovered by OCR — confidence 86/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
assitantd
assistantd.1983
tcp4 127.0.0.1:64523
| (|
Frida 15.0.18 —- A world-class dynamic instrumentation toolkit
help —> Displays the help system
object? -> Display information about ‘object’
|
|
| Commands:
|
exit/quit —> Exit
|
~ . «+. More info at https://frida.re/docs/home/
Failed to attach: process with pid 61244 either refused to load frida-agent, or terminated during injection
DEFCGN AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Risks & Methodology 23
```

## Slide 24

## System Integrity Protection

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Risks & Methodology

24


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
system Integrity Protection
System Integrity Protection is a security technology designed to help prevent potentially malicious
software from modifying protected files and folders on your Mac. System Integrity Protection restricts the
root user account and limits the actions that the root user can perform on protected parts of the Mac
operating system.
Disable System Integrity Protection Temporarily
To disable SIP, do the following:
1. Restart your computer in Recovery mode.
2. Launch Terminal from the Utilities menu.
3. Run the command csrutil disable.
4. Restart your computer.
DEFCGN AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Risks & Methodology 24
```

## Slide 25

## Breaking the Certificate Pinning

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Risks & Methodology

25


> Recovered by OCR — confidence 84/100 on the text kept, 59/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Breaking the Certificate Pinning
‘fa server it does
ave and sakes
J. See
SSL_ACTX ectx, int mode,
Called boringssl_context_set_verify_mode: @xb45c43800 @x3
DEF ce N AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Risks & Methodology
25
```

## Slide 26

## ACE What?

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Risks & Methodology

26


> Recovered by OCR — confidence 85/100 on the text kept, 81/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
ACE What?
Host: guzzoni.apple.com
X-Ace-Host: mlllsa
X-Sync-Owner-Assistant-ID: 85534DF3 3486-3/7D3F99AC346
User-Agent: Assistant(macOS/Mac15,6; macOS/15.2/24C101) Ace/13.8-20A
Accept-Language: en-US
Content-Length: 2600000006
AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Risks & Methodology
26
```

## Slide 27

## Patching Mitmproxy

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Risks & Methodology

27


> Recovered by OCR — confidence 94/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Patching Mitmproxy
# 5. If a valid Content-Length header field is present without
# Transfer-Encoding, its decimal value defines the expected message
# body length in octets. If the sender closes the connection or
5. If a valid Content-Length header field is present without
Transfer-Encoding, its decimal value defines the expected message
body length in octets. If the sender closes the connection or
the recipient times out before the indicated number of octets are
received, the recipient MUST consider the message to be
incomplete and close the connection.
if cl := headers.get("content-Length"):
if parsed_content_length == 2000000000:
return -1
return parsed_content_length
DEF ce N AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Risks & Methodology 27
```

## Slide 28

## AA CC EE

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Risks & Methodology

28


> Recovered by OCR — confidence 83/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Host: guzzoni. apple.com
X-Ace-Host: ml11sa
X-Client-Connection-Id: EQ4AF779-5B7E-4291-88BB-F6C4CEBFECE8
Accept-Language: en-US
Content-Length: 2000000000
0000000000 aa cc ee 02
AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Risks & Methodology
| View: auto +
28
```

## Slide 29

## Decoding ACE Protocol

Step 1 Step 2 Magic Zlib AA BB CC 02 0x78DA

Step 3 Commands

”bplist” “Keep-Alive"

Step 4 ProtoBuf “baes64Proto”

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Risks & Methodology

29

## Slide 30

## Dealing with Siri Communications

Step 1 Step 2 Step 3 Proxy Protobuf Analyze Decoder

Step 1 Step 2 Disable Proxy certificate pinning

Step 3 Step 4 ACE Analyze Parser

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Risks & Methodology

30

## Slide 31

# Scenarios

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Scenarios

31

## Slide 32

32


> Recovered by OCR — confidence 94/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
DEFCON
Apple Intelligence & Siri
A personal intelligence system integrated deeply into your Mac, apps, and
Siri. Learn more...
Apple Intelligence
Siri
Listen for
Allow Siri when locked
Keyboard shortcut
Press to type to Sir
Language
Language
“Hey Siri*
Press Either Command Key Twice >
Allow Siri to learn from how you use this application in order to
make suggestions across applications.
Learn from this application
32
```

## Slide 33

# Siri

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri

33

## Slide 34

## **The start of a new era for Siri**

“Siri draws on Apple Intelligence for new superpowers… the ability to type to Siri whenever it’s convenient for you…. And with extensive product knowledge and the ability to tap into ChatGPT…”

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri

34

## Slide 35

## The Prompt

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri

35


> Recovered by OCR — confidence 88/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
The Prompt
€3 What is the weather in Las Vegas U)
Las Vegas -@.
Today
DEF CON AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri 35
```

## Slide 36

## Quick look – Data Frame

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri

36


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Quick look — Data Frame
Intercepted request to api-glb-auseic.smoot.apple.com
root:
<chunk> = message:
<chunk> = "What is the weather in Las Vegas"
DEFCE&SN AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri
36
```

## Slide 37

## Location (Latitude, Longitude)

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri

37


> Recovered by OCR — confidence 85/100 on the text kept, 85/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Location (Latitude, Longitude)
1 <32bit>= 0x4214f200 / 1108668928 / 37.23633
2 <32bit>= @xc2e79c36 / 3269958710 / -115.805098
Intercepted request to api-glb-auseic.smoot.apple.com
DEFCE&SN AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri
```

## Slide 38

## Precise Location

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri

38


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Precise Location
If you have Location Services turned on for Siri, the location of your device at the time you make a request
will be sent to Apple to help Siri and Dictation improve the accuracy of its response to your requests. To
deliver relevant responses and suggestions, Apple may use the IP address of your internet connection to
approximate your location by matching it to a geographic region.
If you have enabled Location Services, you can turn off Location Services for Siri by going to Settings >
Privacy & Security > Location Services > Siri and tapping Never.
If you have enabled Location Services, you can turn off Location Services for Siri Suggestions by going to
Settings > Privacy & Security > Location Services > System Services and tapping to turn off Suggestions &
Search.
DEF ce N AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri 38
```

## Slide 39

## Apple’s Weather App

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri

39


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Apple's Weather App
<varint> = 9
<chunk> = message:
<chunk> = "type.googleapis.com/apple.parsec.siri.v2alpha.AppInfo"
<chunk> = message:
<chunk> = "weather"
<chunk> = ("com.apple.weather"}
<varint> = 1
<chunk> = "WeatherIntent"
Intercepted request to api-glb-auseic.smoot.apple.com
DEFCE&SN AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri
39
```

## Slide 40

## Weather App?

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri

40


> Recovered by OCR — confidence 86/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Weather App?
<chunk> = message:
<chunk> = "weather"
<chunk> = "com.parallels.winapp.1441dféb1c10f910ccdc400e40b5fce9
<string>Weather</string>
Intercepted request to api-glb-—auseic.smoot.apple.com
DEFCE&SN AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri
40
```

## Slide 41

## Applications lists by topic

OUTLOOK

VLC

CODE

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri

41


> Recovered by OCR — confidence 91/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Applications lists by topic
<chunk> = message:
<chunk> = "type.googleapis.com/apple.parsec.siri.v2alpha.AppInfo"
<chunk> = message:
<chunk> = "Outlook"
<chunk> = "“com.microsoft.Outlook"
<chunk> = "type.googleapis.com/apple.parsec.siri.v2alpha.AppInfo"
<chunk> = message:
<chunk> = "Vic"
<chunk> = “org.videolan.vlc"
<chunk> = message:
<chunk> = "type.googleapis.com/apple.parsec.siri.v2alpha.AppInfo"
<chunk> = message:
<chunk> = "code"
<chunk> = "com.microsoft.VSCode"
Intercepted request to api-glb-auseic.smoot.apple.com
DEF ce N AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri
OUTLOOK
A
VLC
J
CODE
```

## Slide 42

## Active Applications

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri

42


> Recovered by OCR — confidence 82/100 on the text kept, 65/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Active Applications
jroup': ‘com.apple.ace.system',
‘appIdentifyingInfo': {'$class': 'AppIdentifyingInfo', <8
‘appIdentifyingInfo': {'$class': ‘AppIdentifyingInfo',
‘$group': ‘com.apple.ace.system',
‘appIdentifyingInfo': {'$class': ‘AppIdentifyingInfo',
‘$group': ‘com.apple.ace.sync',
Intercepted request to guzzoni.apple.com
DEF ce N AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri
42
```

## Slide 43

## Taylor Swift?!

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri

43


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Taylor Swift?!
DEFCGN
<chunk> = "type.googleapis.com/apple.parsec.siri.v2alpha.AudioQueueStateInfo"
<chunk> = message:
<varint> = 2
<varint> = 3
<chunk> = "company.thebrowser.Browser"
<chunk> = message:
<chunk> = "TaylorSwiftVEVO"
<chunk> = “Taylor Swift - no body, no crime (Official, Lyric Video) ft.
Intercepted request to api-glb-auseic.smoot.apple.com
AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri
43
```

## Slide 44

## NowPlaying Queue

Metadata Query

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri

44


> Recovered by OCR — confidence 89/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
NowPlaying Queue
AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri
Metadata Query
Never Gonna Give You Up
arust Rick Astley
» Greatest Hits
album artist: Rick Astley
composer Mike Stock, Matt Aitken & Peter Waterman
‘Show composer in all views
year 1987
track 1 of 17
per 1 oof 1
pilation — Album is a compilation of songs by various artists
44
```

## Slide 45

## Remember?

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri

45


> Recovered by OCR — confidence 94/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Remember?
DEFCGN
Your Data is not Private, By: Yoav
Magid
The Secret
AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri
45
```

## Slide 46

## When TMI meets AI…

I just wanted to ask AI: “What is the weather today in Las Vegas?”

However, Siri interpreted it as…

- What’s the weather today in Las Vegas

- ● Check which weather apps I have installed

- ● What my favorite song is?

- ● BTW, do you know I have VMs on my device?

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri

46

## Slide 47

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri 47


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
DEFCON
AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri
47
```

## Slide 48

## Messaging Data

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri

48


> Recovered by OCR — confidence 82/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Messaging Data
Hello World
+19147772222B
DEFCE&SN AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri
Taylor Swift lore Oxe
® Sendh X (x-apple-siri-app://net.whatsapp.WhatsApp *$CDFF12B7-96A5-4E1F-9F23-FAD9E5C2D7CAp “
48
```

## Slide 49

## Siri Cases

|CASE|ON-DEVICE/CLOUD|DATA SENT|WHERE?|
|---|---|---|---|
|Calculator|Cloud|||
|W eather|Cloud|Active Apps
Speakers’ Audio|Smoot|
|Online Search|Cloud|Apps by Topic
Location|guzzoni|
|Article Search|Cloud|||
|Message Service|On-Device|Active Apps
Speakers’ Audio
Message Data||
||||guzzoni|
|Email Service|On-Device|Active Apps||
|Calendar|On-Device|Speakers’ Audio||

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri

49

## Slide 50

# Writing Tools

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Writing Tools

50

## Slide 51

## Writing Tools

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Writing Tools

51


> Recovered by OCR — confidence 89/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Writing Tools
( ©} Describe your change
=
Proofread Rewrite
Friendly
Professional
Concise
Summary
Key Points
List
Table
7 Compose...
DEFCGN
AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Writing Tools
Inspect
Speech >
C Writing Tools >)
Services >
(= Summarize
Sl
```

## Slide 52

## On-Device or Not?

Online

Offline

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Writing Tools

52


> Recovered by OCR — confidence 88/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
DEFCGN
On-Device or Not?
( © Describe your change
Proofread Rewrite
@ Friendly
& Professional
= Concise
= Summary
= Key Points
List
® Table
ii
7 Compose...
Online
AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Writing Tools
©} Describe your change
Q 1)
Proofread Rewrite
@ Friendly
€ Professional
= Concise
To use all Writing Tools capabilities,
connect to the internet.
Offline
52
```

## Slide 53

# Image Playground

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Image Playground

53

## Slide 54

## Image Playground

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Image Playground

54


> Recovered by OCR — confidence 92/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Image Playground
SUGGESTIONS
Disco Superhero Vampire Rainforest
e
AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Image Play ground
Describe an image or add a
suggestion from the list.
SHOW MORE
Astronaut Adventure Scientist
PERSON STYLE i
Choose... Animation J
54
```

## Slide 55

Extensions

## Slide 56

###### The only extension of Apple Intelligence

## ChatGPT

Accessible via Siri & Writing Tools (Show Images)

Proxy through Apple Servers and not directly with OpenAI

Some requests are duplicated to Siri Search

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Extensions

56

## Slide 57

## Disclosure Timeline

Disclosure begin 02/2025

Sending logs & pictures 03/2025

Apple’s comment 07/2025

Apple required more info 03/2025

Apple’s acknowledgement 03/2025

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Extensions

57

## Slide 58

Apple Response


> Recovered by OCR — confidence 93/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Apple Response
For these issues, you're using Siri instead of Apple Intelligence. The domains “smoot”
and “guzzoni" are part of Siri, not Apple Intelligence. Private Cloud Compute uses
apple-relay.cloudflare.com, apple-relay.fastly-edge.com, and cp4.cloudflare.com.
Bell
Can't talk?
Type to Siri.
now on iPhone 16
```

## Slide 59

## SiriKit Test

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Disclosure


> Recovered by OCR — confidence 85/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
SiriKit Test
See you soon
d Sendh X .x-apple-siri-app://Yoav-Lumia.TestMessagingAPP “3756DB956-9C9A-45EB-8423-3ACFD5991249p
DEFCE&SN AppleStorm Unmasking the Privacy Risks of Apple Intelligence | Disclosure
```

## Slide 60

## Mitigations

###### 1. Block any network traffic to guzzoni.apple.com – does not hinder functionality 2. Disable any settings of apps that you are not willing to share

|APP|DOMAINS|DATA SENT|
|---|---|---|
|||Active Apps|
||guzzoni.apple.com|Messaging Data|
|Siri||Speakers’ Audio
|
||*.smoot.apple.com|Apps by Topic
Location|
|||Speakers’ Audio|
|W riting Tools|apple-relay.cloudflare.com
apple-relay.fastly-edge.com
|Relevant Data|
||cp4.cloudflare.com
(Private Cloud Compute)||
|Image Playground|-|-|
|Extensions - ChatGPT|apple-relay.apple.com (PCC)
*.smoot.apple.com (Siri)|Prompt
Auth (onlyPCC)|

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Extensions

60

## Slide 61

## Takeaways

1 Privacy Policy - To Read or not to Read? 2 Implement Careful Network-Level Monitoring 3 Transparency from AI Vendors - Pinning should not be an obstacle

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Extensions

61

## Slide 62

Retrospective

## Slide 63

## Apple Intelligence VS Siri

2 Terms of Use

•

2 Privacy Policies


> Recovered by OCR — confidence 90/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Apple Intelligence VS Siri
€ What is the weather in Las Vegas iu © What are the weather vibes | should
prepare for in Las Vegas
Las Vegas ‘e: © What are the outside vibes in Las
42° 26° Clear Vegas at the moment?
Today
At 9:08 PM on Sunday, July 6, 2025, gy
Las Vegas is experiencing clear skies
with a temperature around 79°F (26°C).
The air is dry with humidity at
approximately 10%, and winds are light at
5 mph (8 km/h) from the west-northwest.
The UV index is low, and air quality is rated
as good, posing little or no risk to health.
2 Terms of Use + 2 Privacy Policies
DEFCGN
```

## Slide 64

Can you tell the difference?

## Slide 65

Thank you for listening!

## Slide 66

Q&A
