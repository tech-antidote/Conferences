---
title: "AppleStorm - Unmasking the Privacy Risks of Apple Intelligence"
speakers: ["Yoav Magid"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Yoav Magid_AppleStorm - Unmasking the Privacy Risks of Apple Intelligence.pdf"
pages: 54
sha256: "ea62ed69403bd217e7c03a6ba14822dec214c6edcfc694b42b5fcd9a69e21f78"
text_chars: 17739
ocr_pages: 36
has_ocr: true
redacted_secrets: 0
companion_files: ["Yoav Magid_AppleStorm - Unmasking the Privacy Risks of Apple Intelligence_tools.txt"]
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:04:18Z"
---
# AppleStorm - Unmasking the Privacy Risks of Apple Intelligence

**Speakers:** Yoav Magid  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Yoav Magid_AppleStorm - Unmasking the Privacy Risks of Apple Intelligence.pdf` (54 pages)


## Slide 1

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence

Speaker: Yoav Magid

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat
BRIEFINGS
AUGUST 6-7, 2025
MANDALAY BAY / LAS VEGAS
AppleStorm:
Unmasking the Privacy Risks of Apple Intelligence
Speaker: Yoav Magid
```

## Slide 2

How many of you own an Apple device?

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Introduction

2

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
How many of you own
an Apple device?
3)
blackhat  AppleStorm Unmasking the Privacy Risks of Apple Intelligence | Introduction
```

## Slide 3

###### **U.S. Mobile OS Usage Share**

###### U.S. Desktop OS Usage Share

0.4% 2.5% 2.5% 9.3%
38.1%
61.4%
29.6%
56.1%

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Introduction

3

## Slide 4

How many of you use Siri?

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Introduction

4

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
How many of you
use Siri?
(2)
blackhat  AppleStorm Unmasking the Privacy Risks of Apple Intelligence | Introduction
```

## Slide 5

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Introduction 5

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
BIBIC
Home News Sport Business Innovation Culture Arts Travel Earth Audio Video Live
Apple to pay $95m to settle Siri
‘listening’ lawsuit
7 January 2025 Share <p Save []
Imran Rahman-Jones
Technology reporter
blackhat  AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Introduction
```

## Slide 6

##### **How many of you use Apple Intelligence?**

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Introduction

6

## Slide 7

### **Apple Intelligence**

Siri

**Writing Tools**

**Image Playground**

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Introduction

7

## Slide 8

8

## Slide 9

9

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Is Your Data Private? By: Yoav Magid Share yy ++
Is Your Data Private? By: Yoav Magid
The Secret
The Secret
pisck hat
```

## Slide 10

###### Yoav Magid

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Introduction

10

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Yoav Magid
Team Lead & Al Researcher
&3lumia
3)
blackhat  AppleStorm Unmasking the Privacy Risks of Apple Intelligence | Introduction
```

## Slide 11

## Agenda

Behind Apple Intelligence’s Curtains

Risks & Methodology

“Hey Siri, What can you do?”

What can we do?

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Agenda
Behind Apple Intelligence’s Curtains
Risks & Methodology
“Hey Siri, What can you do?"
What can we do?
bisek hat
```

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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Apple Intelligence & Privacy
Apple Intelligence is designed to protect your information.
tell
ais. There are
When you initiate an Apple Intelligence task, a model running on your device analyzes whether the task
can be completed on device. If a larger, server-based model is required, Apple Intelligence uses Private
Cloud Compute to send only data relevant to your request to be processed on Apple silicon servers.
are not retained by Private Cloud Compute. When your device sends a St to Private Cloud Compute,
Apple only collects limited information about the request, such as the approximate size of the request and
blackhat AppleStorm Unmasking the Privacy Risks of Apple Intelligence | Apple Intelligence's Infrastructure 14
```

## Slide 15

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Apple Intelligence's Infrastructure 15

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Apple Intelligence, Siri, and Search
Apple devices must be able to connect to the following hosts to process Apple Intelligence requests that
use Private Cloud Compute and to process Siri requests, including dictation and searching in Apple apps.
Hosts
guzzoni.apple.com
*smoot.apple.com
apple-relay.cloudflare.com
apple-relay.fastly-edge.com
cp4.cloudflare.com
apple-
relay.apple.com
3)
Description
Siri and dictation requests
Search services, including Siri, Spotlight,
Lookup, Safari, News, Messages, and Music
Private Cloud Compute
Private Cloud Compute
Private Cloud Compute
Apple Intelligence
Extensions
blackhat AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Apple Intelligence's Infrastructure
```

## Slide 16

# Risks & Methodology

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Risks & Methodology

16

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Risks &
Methodology
bist That  AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Risks & Methodology
```

## Slide 17

**Private What? Cloud** _On-device vs. PCC Which data?_

How? _Network Inspection_

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Risks & Methodology

17

## Slide 18

#### **SSL**

_Enabled via SSL/TLS certificates issued by trusted Authorities._

###### Certificate Pinning

_A technique to a specific certificate or public key to an The app all certificates not matching the pinned one to prevent Adversary-in-the-Middle._

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Risks & Methodology

18

## Slide 19

# Scenarios

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Scenarios

19

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Scenarios
blackhat  AppleStorm Unmasking the Privacy Risks of Apple Intelligence | Scenarios
```

## Slide 20

20

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
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
i )
“Hey Siri*
Press Either Command Key Twice >
Allow Siri to learn from how you use this application in order to
make suggestions across applications.
Learn from this application
20
```

## Slide 21

# Siri

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri

21

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
3)
blackhat 4ppleStorm Unmasking the Privacy Risks of Apple Intelligence | Siri
2i
```

## Slide 22

## **The start of a new era for Siri**

“Siri draws on Apple Intelligence for new superpowers… the ability to type to Siri whenever it’s convenient for you…. And with extensive product knowledge and the ability to tap into ChatGPT…”

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri

22

## Slide 23

## The Prompt

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri

23

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The Prompt
€3 What is the weather in Las Vegas U)
Las Vegas -@.
4? ° ? 6 ° Clear
Today
bisa That  AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri 23
```

## Slide 24

## Quick look – Data Frame

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri

24

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Quick look — Data Frame
Intercepted request to api-glb-auseic.smoot.apple.com
root:
<chunk> = message:
<chunk> = "What is the weather in Las Vegas"
bist That  AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri
24
```

## Slide 25

## Location (Latitude, Longitude)

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri

25

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Location (Latitude, Longitude)
1 <32bit>= 0x4214f200 / 1108668928 / 37.23633
2 <32bit>= @xc2e79c36 / 3269958710 / -115.805098
Intercepted request to api-glb-auseic.smoot.apple.com
bist That  AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri
```

## Slide 26

## Precise Location

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri

26

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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
3)
blackhat AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri
26
```

## Slide 27

## Apple’s Weather App

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri

27

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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
bisa That  AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri
27
```

## Slide 28

## Weather App?

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri

28

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Weather App?
<chunk> = message:
<chunk> = "weather"
<chunk> = "com.parallels.winapp.1441dféb1c10f910ccdc400e40b5fce9
<string>com.parallels.winapp.1441df6b1c10f91@ccdc4@0e40b5fce9
<string>Weather</string>
Intercepted request to api-glb-—auseic.smoot.apple.com
bisa That  AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri
28
```

## Slide 29

## Applications lists by topic

OUTLOOK

VLC

CODE

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri

29

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
3)
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
blackhat AppleStorm Unmasking the Privacy Risks of Apple Intelligence | Siri
OUTLOOK
A
VLC
J
CODE
29
```

## Slide 30

## Active Applications

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri

30

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Active Applications
‘AppInfo',
jroup': ‘com.apple.ace.system',
‘appIdentifyingInfo': {'$class': 'AppIdentifyingInfo', <8
‘$group': ‘com.apple.ace.sync', aps
‘bundleId': ‘com. tinyspeck. @@ekMe@egep '}}], ~ Se
[{'$class': ‘AppInfo',
"$group': ‘com.apple.ace.system',
‘appIdentifyingInfo': {'$class': ‘AppIdentifyingInfo',
‘$group': ‘com.apple.ace.sync',
*bundleId': ‘com. apple.(aaider }}], ——
[{*$class': ‘AppInfo',
‘$group': ‘com.apple.ace.system',
‘appIdentifyingInfo': {'$class': ‘AppIdentifyingInfo',
‘$group': ‘com.apple.ace.sync',
‘bundleId': ‘"@@ERORNG'}}11,
Intercepted request to guzzoni.apple.com
blackhat  4ppleStorm Unmasking the Privacy Risks of Apple Intelligence | Siri
30
```

## Slide 31

## Taylor Swift?!

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri

31

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Taylor Swift?!
<chunk> = "type.googleapis.com/apple.parsec.siri.v2alpha.AudioQueueStateInfo"
<chunk> = message:
<varint> = 2
<varint> = 3
<chunk> = "company.thebrowser.Browser"
<chunk> = message:
<chunk> = "TaylorSwiftVEVO"
<chunk> = "Taylor Swift - no body,
Intercepted request
(2)
blackhat 4ppleStorm Unmasking the Privacy Risks of Apple Intelligence | Siri
no crime (Official, Lyric Video) ft.
to api-glb-auseic.smoot.apple.com
```

## Slide 32

## Now Playing Queue

Metadata Query

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri

32

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Now Playing Queue
bisek hat
Se
AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri
Metadata Query
Never Gonna Give You Up
arust Rick Astley
» Greatest Hits
album artist: Rick Astley
composer Mike Stock, Matt Aitken & Peter Waterman
‘Show composer in all views
> Pop .
year 1987
track 1 of 17
per 1 oof 1
pilation — Album is a compilation of songs by various artists
32
```

## Slide 33

## Remember?

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri

33

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Remember?
Your Data is not Private, By: Yoav
Magid
The Secret
> o00/030 ©
3)
blackhat 4ppleStorm Unmasking the Privacy Risks of Apple Intelligence | Siri
33
```

## Slide 34

## When TMI meets AI…

I just wanted to ask AI: “What is the weather today in Las Vegas?”

However, Siri interpreted it as…

- What’s the weather today in Las Vegas

- ● Check which weather apps I have installed

- What my favorite song is?

- BTW, do you know I have VMs on my device?

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri

34

## Slide 35

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri 35

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
#)
blackhat AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri
```

## Slide 36

## Messaging Data

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri

36

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Messaging Data
Hello World
:% POO
+19147772222B
19147772222@s.whatsapp.net’)
bisa That  AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Siri
Taylor Swift lore Oxe
® Sendh X (x-apple-siri-app://net.whatsapp.WhatsApp *$CDFF12B7-96A5-4E1F-9F23-FAD9E5C2D7CAp “
36
```

## Slide 37

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

37

## Slide 38

# Writing Tools

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Writing Tools

38

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Writing Tools
bist hat  AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Writing Tools
```

## Slide 39

## Writing Tools

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Writing Tools

39

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Writing Tools
( ©} Describe your change
Q @
Proofread Rewrite
@ Friendly
& Professional
= Concise
= Summary
Key Points
List
& Table
7 Compose...
3)
blackhat AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Writing Tools
Inspect
Speech >
C Writing Tools >)
Services >
(= Summarize
39
```

## Slide 40

## On-Device or Not?

Online

Offline

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Writing Tools

40

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
On-Device or Not?
( © Describe your change
Q ©
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
blackhat AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Writing Tools
©} Describe your change
Q 1)
Proofreed Rewri
@ Friendly
€ Professional
= Concise
4 Compo
To use all Writing Tools capabilities,
connect to the internet.
Offline
40
```

## Slide 41

# Image Playground

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Image Playground

41

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Image Playground
blackhat  AppleStorm Unmasking the Privacy Risks of Apple Intelligence | Image Play ground
```

## Slide 42

## Image Playground

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Image Playground

42

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Image Playground
Describe an image or add a
@ G ee suggestion from the list.
SUGGESTIONS SHOW MORE
-
*» @oezt ee @
Disco Superhero Vampire Rainforest Astronaut Adventure Scientist
3)
blackhat AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Image Play ground 42
```

## Slide 43

Extensions

## Slide 44

###### The only extension of Apple Intelligence

## ChatGPT

Accessible via Siri & Writing Tools (Show Images)

Proxy through Apple Servers and not directly with OpenAI

Some requests are duplicated to Siri Search

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Extensions

44

## Slide 45

## Disclosure Timeline

Disclosure begin 02/2025

Sending logs & pictures 03/2025

Apple’s comment 07/2025

Apple required more info 03/2025

Apple acknowledgement 03/2025

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Disclosure

45

## Slide 46

## Apple Response

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Disclosure

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Apple Response
For these issues, you're using Siri instead of Apple Intelligence. The domains “smoot”
and “guzzoni" are part of Siri, not Apple Intelligence. Private Cloud Compute uses
apple-relay.cloudflare.com, apple-relay.fastly-edge.com, and cp4.cloudflare.com.
fe att AppleStorm Unmasking the Privacy Risks of Apple Intelligence | Disclosure
Bell
Can't talk?
Type to Siri.
now on iPhone16
```

## Slide 47

## SiriKit Test

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Disclosure

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
SiriKit Test
” Wy
Developer
See you soon
d Sendh X .x-apple-siri-app://Yoav-Lumia.TestMessagingAPP “3756DB956-9C9A-45EB-8423-3ACFD5991249p
John" John @P€> @ €x@
blackhat AppleStorm Unmasking the Privacy Risks of Apple Intelligence | Disclosure
```

## Slide 48

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

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Mitigations

48

## Slide 49

## Takeaways

1 Privacy Policy - To Read or not to Read? 2 Implement Careful Network-Level Monitoring 3 Transparency from AI Vendors - Pinning should not be an obstacle

AppleStorm: Unmasking the Privacy Risks of Apple Intelligence | Takeaways

49

## Slide 50

Retrospective

## Slide 51

## Apple Intelligence VS Siri

• 2 Terms of Use 2 Privacy Policies Same App

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Apple Intelligence VS Siri
€ What is the weather in Las Vegas @ © What are the weather vibes | should
prepare for in Las Vegas
Las Vegas ‘e: © What are the outside vibes in Las
42° 26° Clear Vegas at the moment?
Today
At 9:08 PM on Sunday, July 6, 2025, ro)
Las Vegas is experiencing clear skies
with a temperature around 79°F (26°C).
The air is dry with humidity at
approximately 10%, and winds are light at
5 mph (8 km/h) from the west-northwest.
The UV index is low, and air quality is rated
as good, posing little or no risk to health.
2 Terms of Use + 2 Privacy Policies
bidekhat Same App
©
co]
```

## Slide 52

Can you tell the difference?

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Can you tell the
difference?
blackhat
```

## Slide 53

Thank you for listening!

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Thank you for listening!
£8 lumia
```

## Slide 54

Q&A

## Companion resources

### `Yoav Magid_AppleStorm - Unmasking the Privacy Risks of Apple Intelligence_tools.txt`

```text
https://github.com/LumiaSecurity/mitmproxy-ace
```
