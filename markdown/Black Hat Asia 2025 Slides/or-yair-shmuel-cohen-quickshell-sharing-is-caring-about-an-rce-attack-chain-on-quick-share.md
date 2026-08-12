---
title: "QuickShell Sharing is Caring About an RCE Attack Chain on Quick Share"
speakers: ["Or Yair", "Shmuel Cohen"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2025"
edition: "ASIA"
year: 2025
source_pdf: "Black Hat Asia 2025 Slides/Or Yair & Shmuel Cohen_QuickShell Sharing is Caring About an RCE Attack Chain on Quick Share.pdf"
pages: 113
sha256: "97864900689090b1a4903b388a0d9c67bf155e16e6f2ee072d65c1da0aeef906"
text_chars: 20984
ocr_pages: 56
has_ocr: true
redacted_secrets: 0
ocr_confidence: 89.7
ocr_unreliable_blocks: 0
vision_verified_blocks: 1
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T03:57:08Z"
---
# QuickShell Sharing is Caring About an RCE Attack Chain on Quick Share

**Speakers:** Or Yair, Shmuel Cohen  
**Conference:** Black Hat ASIA 2025  
**Source:** `Black Hat Asia 2025 Slides/Or Yair & Shmuel Cohen_QuickShell Sharing is Caring About an RCE Attack Chain on Quick Share.pdf` (113 pages)


## Slide 1

Sharing is caring about an RCE attack chain on Quick Share


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
QuickShell
Sharing is caring about an RCE attack
chain on Quick Share
```

## Slide 2

Security Research Team Lead at SafeBreach 7� years in Security Research

Past research in Linux, embedded, Android

4 years Windows research

## Slide 3

6� years in Security Industry Past APT Malware Researcher

4� years Windows research

## Slide 4

Why Quick Share Protocol Overview Fuzzing

Research Approach Shift � Vulnerability Discovery RCE Chain

Takeaways GitHub � Q&A

## Slide 5

## Slide 6

## Slide 7

## Slide 8


> Recovered by OCR — confidence 96/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Quick Share Windows Version
€ Quick Share for Windows
Wireless sharing with your PC, made
easy.
Send and receive photos, documents, and more between nearby Android
To get started, install Quick Share for Windows to your PC. Send yourself the
link to download it.
By downloading Quick Share for Windows, you agree to the Google Terms of
Service. The Google Privacy Policy describes how Google handles
information from Quick Share for Windows.
Download Quick Share ,
```

## Slide 9

Google:

“we’re working with leading PC manufacturers like LG to expand Quick Share to Windows PCs as a pre-installed app.”

## Slide 10

Various communication 1st time by Google methods on Windows

## Slide 11

2019 by Daniele Antonioli, Nils Ole Tippenhauer, Kasper Rasmussen: “Nearby Threats: Reversing, Analyzing, and Attacking Google’s ‘Nearby Connections’ on Android”  About Nearby Connections API

- Only Android

- No CVEs

https://francozappa.github.io/publication/rearby/paper.pdf

## Slide 12

Contain part of the code for Quick Share for Windows


> Recovered by OCR — confidence 83/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Nearby & Chromium Open-Source Repos
Contain part of the code for Quick Share for Windows
%) A collection of projects focused on connectivity
that enable building cross-device experiences.
@ developers.google.com/nearby
3S Apache-2.0 license
yw 696stars % 151forks $ Branches 9 Tags
EF chromium / chromium ( Public
The official GitHub mirror of the Chromium source
@ chromium.googlesource.com/chromium/src/
a] BSD-3-Clause, BSD-3-Clause licenses found
w 18.3kstars % 6.8kforks % Branches © Tags
```

## Slide 13

New Windows App � New App New vulns Windows app will be pre-installed

Various communication methods � Various attack vectors Google’s first Windows app to use these APIs

Some of the code is open-source

No CVEs

## Slide 14


> Recovered by OCR — confidence 86/100 on the text kept, 59/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Y)
=)
=
LU
O
LL
Research Goal
```

## Slide 15

## Slide 16

Finding the communication functions � Send & Recv:

## Slide 17

## Slide 18

offline_wire_formats.proto


> Recovered by OCR — confidence 93/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Protobuf and Offline Frames
offline_wire_formats.proto
message OfflineFrame {
enum Version {
UNKNOWN_VERSION = @;
J
optional Version version = 1;
optional ViFrame v1 = 2;
}
```

## Slide 19

## st

Hooking Quick Share to sniff sent and received Offline Frames on Windows


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 88/100 on the text kept, 84/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
[Top-left heatmap]
Y-axis ticks: 80727 / 76687 / 71868 / 65910 / 59954 / 53996 / 50755
X-axis ticks: 0 20 40 60 80 100 120 140 160 180 200 220 240
Colorbar: 1.0 / 0.8 / 0.6 / 0.4 / 0.2 / 0.0

[Top-right heatmap]
Y-axis ticks: 57363 / 57163 / 56963 / 56763 / 56563 / 56363 / 56163
X-axis ticks: 0 20 40 60 80 100 120 140 160 180 200 220 240
Colorbar: 1.0 / 0.8 / 0.6 / 0.4 / 0.2 / 0.0

[Bottom-left heatmap]
Y-axis ticks: 58385 / 55345 / 52305 / 49265 / 46225 / 43185 / 40201
X-axis ticks: 0 20 40 60 80 100 120 140 160 180 200 220 240
Colorbar: 1.0 / 0.8 / 0.6 / 0.4 / 0.2 / 0.0

[Bottom-right panel]
STM32L767 (M7)
```

## Slide 20

## Slide 21

Nearby Connections API

Quick Share Implementation

## Slide 22

Protobuf Based

Encryption � Google’s Ukey2

Advertisement based on Service ID Multiple Connections Strategies  P2P, Star, Cluster

## Slide 23


> Recovered by OCR — confidence 97/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Quick Share Protocol Overview
```

## Slide 24

CONNECTION_REQUEST Ukey2 Client Init


> Recovered by OCR — confidence 96/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Quick Share Protocol Overview
CONNECTION_REQUEST
```

## Slide 25

CONNECTION_REQUEST
Ukey2 Client Init
Ukey2 Server Init
Ukey2 Client Finish
Ukey2 Handshake Completed

## Slide 26

CONNECTION_REQUEST
Ukey2 Key Exchange
Connection Response
Connection Response
Proprietary communication begins


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Quick Share Protocol Overview
CONNECTION_REQUEST
Ukey2 Key Exchange
Connection Response
7 Connection Response
Initiator Responder
Proprietary communication begins
```

## Slide 27


> Recovered by OCR — confidence 85/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
enum FrameType {
UNKNOWN_FRAME_TYPE = Q;
CONNECTION_REQUEST = 1;
BANDWIDTH_UPGRADE_NEGOTIATION = 4;
KEEP_ALIVE = 5;
DISCONNECTION = 6;
Packet Types PAIRED _KEY_ENCRYPTION = 7;
AUTHENTICATION MESSAGE = 8;
AUTHENTICATION RESULT = 9;
AUTO_RESUME = 10;
AUTO_RECONNECT = 11;
BANDWIDTH_UPGRADE_RETRY = 12;
```

## Slide 28


> Recovered by OCR — confidence 85/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
enum FrameType {
UNKNOWN_FRAME_TYPE = Q;
CONNECTION_REQUEST = 1;
BANDWIDTH_UPGRADE_NEGOTIATION = 4;
KEEP_ALIVE = 5;
DISCONNECTION = 6;
Packet Types PAIRED _KEY_ENCRYPTION = 7;
AUTHENTICATION MESSAGE = 8;
AUTHENTICATION RESULT = 9;
AUTO_RESUME = 10;
AUTO_RECONNECT = 11;
BANDWIDTH_UPGRADE_RETRY = 12;
```

## Slide 29


> Recovered by OCR — confidence 90/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Packet Types
enum FrameType {
UNKNOWN_FRAME_TYPE Q;
CONNECTION REQUEST = 1;
CONNECTION RESPONSE = 2;
PAYLOAD_TRANSFER = 3;
BANDWIDTH_UPGRADE_NEGOTIATION
KEEP_ALIVE = 5;
DISCONNECTION = 6;
PAIRED_KEY_ENCRYPTION = 7;
AUTHENTICATION RESULT = 9;
AUTO_RESUME = 10;
AUTO_RECONNECT = 11;
BANDWIDTH_UPGRADE_RETRY = 12;
```

## Slide 30


> Recovered by OCR — confidence 96/100 on the text kept, 33/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Quick Share
Implementation
```

## Slide 31

CONNECTION_REQUEST
Ukey2 Key Exchange
Connection Response
Connection Response
Proprietary communication begins


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Recap
CONNECTION_REQUEST
Ukey2 Key Exchange
Connection Response
7 Connection Response
Initiator Responder
Proprietary communication begins
```

## Slide 32

Enforces “Contacts” and “Your Devices” modes

Payload Transfer


> Recovered by OCR — confidence 96/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Payload Transfer
Enforces “Contacts” and “Your Devices” modes
Payload Transfer
```

## Slide 33

???

Custom protobuf data in Payload Transfer Payload


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Quick Share
Implementation
Custom protobuf data in
Payload Transfer Payload
v1:
payloadTransfer:
packetType: DATA
payloadChunk:
body: CAESYggBE14KWgolYmFzZS5hcGs|
flags: 0
index: 0
y dHeader:
id: '-5454771653010976901'
sSensitive: false
otalSize: '102'
type: BYTES
type: PAYLOAD_TRANSFER
version: V1
```

## Slide 34

Custom protobuf data in Payload Transfer OfflineFrame


> Recovered by OCR — confidence 90/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Quick Share Implementation
Custom protobuf data in
Payload Transfer OfflineFrame
packe DATA
nsitive: false
type: BYTES
ype: PAYLOAD_TRANSFER
ersion: V1
retIdHash:
palHIL+r
version: V1
index: @
set: ‘@'
adHeader:
id: '-545477165301
tive: false
>: '102'
si
type: BYTES
ype: PAYLOAD_TRANSFER
‘sion: V1
```

## Slide 35

Enforces “Contacts” and “Your Devices” modes

Paired Key Encryption
Paired Key Result


> Recovered by OCR — confidence 87/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Payload Transfer
Enforces “Contacts” and “Your Devices” modes
Paired Key Encryption :
Paired Key Result :
Initiator Responder
```

## Slide 36

INTRODUCTION & ACCEPT After paired Key Encryption:

Introduction


> Recovered by OCR — confidence 96/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Payload Transfer
INTRODUCTION & ACCEPT
After paired Key Encryption:
```

## Slide 37

INTRODUCTION & ACCEPT After paired Key Encryption:

Introduction


> Recovered by OCR — confidence 89/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Payload Transfer
INTRODUCTION & ACCEPT
After paired Key Encryption:
Introduction
: Shmuel's phone
: Wants to share an image
: PIN: 6712 @
```

## Slide 38

### INTRODUCTION & ACCEPT After paired Key Encryption:

Introduction
Accept


> Recovered by OCR — confidence 94/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Payload Transfer
INTRODUCTION & ACCEPT
After paired Key Encryption:
Introduction
Initiator
Shmuel's phone
Wants to share an image
PIN: 6712 @
Responder
```

## Slide 39

INTRODUCTION & ACCEPT After paired Key Encryption:

Introduction
Accept
Raw File
Payload Transfer
010100101101010101100010101101


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Payload Transfer
INTRODUCTION & ACCEPT
After paired Key Encryption:
Introduction
Initiator Responder
Raw File
Payload Transfer
010100101101010101100010101101
```

## Slide 40

Introduction & Accept


> Recovered by OCR — confidence 87/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Payload Transfer
Introduction & Accept
© Quick Share from Google
Device name
SafeBreach_Labs @ B (Senin
Sharing 1 file Nearby devices
Make sure both devices are unlocked,
close together, and have Bluetooth
tumed on. Devices you're sharing with
need Quick Share tumed on and visible
w
```

## Slide 41


> Recovered by OCR — confidence 84/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Quick Share +8 ~
Corpus Input QuickShare
Mutation CRASHES
```

## Slide 42


> Recovered by OCR — confidence 83/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Fuzzing Infrastructure
m winafl Public
```

## Slide 43


> Recovered by OCR — confidence 83/100 on the text kept, 65/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Fuzzing Infrastructure
m winafl Public
```

## Slide 44


> Recovered by OCR — confidence 77/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Fuzzing Infrastructure
= winafl Public
master » ¥ 3 Branches © 0 Tags
G libprotobuf-mutator Public
master ~ P 1Branch © 4 Tags
```

## Slide 45


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
“Accept” Patch
Nearby devices
Shmuel's phone
Wants to share an
PIN: 6712 @
image
Accept
Decline
```

## Slide 46

v


> Recovered by OCR — confidence 86/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Auto-Accept feature
if (base: :FeatureList: :IsEnabled(features: :kNearbySharingSelfShare)) {
}
Auto-accept self shares when not in high-visibility mode.
if (share_target.for_self_share && !IsInHighVisibility()) {
}
NS_LOG(INFO) << _func_ << ": Auto-accepting self share."
Accept(share_target, base: :DoNothing());
```

## Slide 47


> Recovered by OCR — confidence 84/100 on the text kept, 64/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Auto-Accept feature
}
ccept self shares when not in high-visibility mod
NS_LOG(INFO) << __func__ << ": Auto-accepting self share.”;
Accept(share_target, base: :DoNothing());
}
```

## Slide 48

Custom format to hold all packets of an entire session.

### **`[DWORD Length] [Serialized Offline Frame]`**

Stateless

Stateful

## Slide 49


> Recovered by OCR — confidence 86/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
times
WinAFL 1.17 based on AFL 2.43b (
@ days, @ hrs, @ min, 19 sec
@ days, @ hrs, @ min, 18 sec
none seen yet
none seen yet
calibration
23/40 (57.50%)
64
0/0, 0/8, 0/8
0/8, 0/8, 0/2
0/0, 0/8, 0/2
0/0, 0/8
n/a, n/a
28.53% / 34.41%
1.31 bits/tuple
1 (50.00%)
2 (100.00%)
@ (@ unique)
@ (@ unique)
n/a
12%
stage
```

## Slide 50

4 non exploitable DoS vulnerabilities:

Invalid UTF8 continuation byte

Empty “Endpoint ID”

“Payload ID” set to 0

Fast 2 connections:

- same “nonce” in Connection Request

- UNKNOWN_VERSION set in Connection Response

## Slide 51

**`test.exe`**  **`test(1).exe`**

\```
// Break the string at the dot.
autofile_name1=file_name.substr(0, first);
autofile_name2=file_name.substr(first);
...
// While we successfully open the file, keep incrementing the count.
intcount=0;
while (!(file.rdstate() &std::ifstream::failbit)) {
file.close();
target= (folder+file_name1+L" ("+std::to_wstring(++count) +L")"+ file_name2);
  ...
file.open(target, std::fstream::binary|std::fstream::in);
}
\```

## Slide 52

File is being
transferred
test\x00.txt   test\x00 (1).txt
Check if exists?
(trying open it)
Adds an   Success  Failure
index to the
file name
Create the new file

## Slide 53

Fuzzer is running (slow but works) Some unexploitable findings

Moving on to search for logic vulnerabilities, instead of creating the perfect fuzzer

## Slide 54

## Slide 55

Extremely generic Handler class for each packet type Code is full of thread creations all over the place

## Slide 56

Decline

Accept

## Slide 57

INTRODUCTION & ACCEPT After paired Key Encryption:

Introduction
Accept
Raw File
Payload Transfer
010100101101010101100010101101


> Recovered by OCR — confidence 92/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Payload Transfer
INTRODUCTION & ACCEPT
After paired Key Encryption:
Introduction
: Wants to share an image
PIN: 6712 @
ie Raw File
Initiator Payload Transfer
010100101101010101100010101101
Responder
```

## Slide 58

### INTRODUCTION & ACCEPT After paired Key Encryption:

Introduction
Accept
Raw File
Payload Transfer
010100101101010101100010101101


> Recovered by OCR — confidence 90/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Payload Transfer
INTRODUCTION & ACCEPT
After paired Key Encryption:
; Wants to share an image
PIN: 6712 @
ae Raw File
Initiator Payload Transfer
010100101101010101100010101101
Responder
```

## Slide 59

Bypasses all “Accept” in all visibility modes: Your Devices

Contacts Everyone


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
File Transfer Acceptance Bypass
Bypasses all “Accept” in all visibility modes:
Your Devices
Everyone
```

## Slide 60

## Slide 61

Connecting endpoints to our own AP


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Forcing WiFi
Connection
Connecting endpoints to
our own AP
```

## Slide 62

### Medium can be changed during the session.

\```
// Accompanies Medium.WIFI_HOTSPOT.// Accompanies Medium.WIFI_LAN.
message WifiHotspotCredentials {message WifiLanSocket {
optionalstring ssid = 1;optionalbytes ip_address = 1;
optionalstring password = 2;optionalint32 wifi_port = 2;
optionalint32 port = 3;}
optionalstring gateway = 4 [default = "0.0.0.0"];
// This field can be a band or frequency// Accompanies Medium.BLUETOOTH.
optionalint32 frequency = 5 [default = -1];message BluetoothCredentials {
}optionalstring service_name = 1;
optionalstring mac_address = 2;
// Accompanies Medium.WIFI_AWARE.}
message WifiAwareCredentials {
optionalstring service_id = 1;
// Accompanies Medium.WEB_RTC
optionalbytes service_info = 2;message WebRtcCredentials {
optionalstring password = 3;
optionalstring peer_id = 1;
}
optional LocationHint location_hint = 2;
}
\```

## Slide 63

Android devices forced to connect to a WiFi network

�30 seconds’ max

Mitigated by Google  Android devices no longer connect to internet through a Quick Share Bandwidth Upgrade WiFi network

## Slide 64

Internet access is permitted through a Bandwidth Upgrade WiFi network!


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Quick Share on Windows
Internet access is permitted through
a Bandwidth Upgrade WiFi network!
```

## Slide 65

Internet access is permitted through a Bandwidth Upgrade WiFi network! We can now sniff responder internet traffic

## Slide 66


> Recovered by OCR — confidence 97/100 on the text kept, 97/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Standard stones may sometimes
be forged into deadly drones
```

## Slide 67

Create files in “Downloads” without approval WiFi MITM �30 sec max) Crash Quick Share

Force Quick Share to continuously open a file


> Recovered by OCR — confidence 84/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Primary Abilities We Achieved
Create Tiles in “Downloads” without approval
WiFi MITM (30 sec max) < Ce
Crash Quick Share ee
Force Quick Share to continuously open ; afile
```

## Slide 68

Encrypted application layer is a standard. Leveraging MITM for straight forward RCE won’t work for most use cases.

## Slide 69

Quick Share’s files are placed in “Downloads” - the downloads folder for browsers


> Recovered by OCR — confidence 88/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Downloading an Insight
Quick Share’s files are placed
in “Downloads” - the
downloads folder for browsers
Recent Downloads
vacation2023-itinerary.pdf
254 KB +1 minute ago
refresh-daily-background-howto.mp4
6.5 MB+5 minutes ago
Cats-of-Chrome.png
138 KB + 2 hours ago
Show all downloads
```

## Slide 70

Goal:

Overwrite an executable downloaded by a victim before it runs

Needed Abilities:

Know downloaded ? executable file names

Overwrite files (not just create)

?

## Slide 71

#### Overwrite VSCodeSetup.exe

User runs the file

VSCodeSetup.exe

## Slide 72

Trying to bridge the gaps anyway, starting with making the WiFi connection last


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Lasting WiFi MITM
Trying to bridge the gaps anyway, starting
with making the WiFi connection last
```

## Slide 73

## Slide 74

## Slide 75

Force WiFi Connection

We’re now MITM

Crash

## Slide 76


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Knowing Downloaded File Names
```

## Slide 77

TLS Client Hello � Server Name Indication Extension


> Recovered by OCR — confidence 88/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Downloaded Files Metadata - Domain
TLS Client Hello - Server Name Indication Extension
Source it Protocol Length Info
-Extension: server_name (len=26)
Type: server_name (0)
Length: 26
~Server Name Indication extension
Server Name list length: 24
Server Name Type: host_name (@)
Server Name length: 21
Server Name:| code.visualstudio.com
```

## Slide 78


> Recovered by OCR — confidence 96/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Downloaded Files Metadata - Size
Single TCP session per download
Approximate download size
```

## Slide 79

Installer Domain

code.visualstudio.com

Approximate Size

95 MB

File Name Accurate Guess

VSCodeUserSetup-x64�1.91.0.exe

## Slide 80

##### code.visualstudio.com

Installer Domain

Approximate Size

File Name Accurate Guess

95 MB

VSCodeUserSetup-x64�1.91.0.exe

## Slide 81

notepad-plus-plus.org


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Improvement —
Monitoring Domain Paths
notepad-plus-plus.org
Download Notepad++ x64
```

## Slide 82

notepad-plus-plus.org

github.com/.../npp.8.6.9.Installer.x64.exe


> Recovered by OCR — confidence 94/100 on the text kept, 59/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Improvement —
Monitoring Domain Paths
notepad-plus-plus.org
Download Notepad++ x64
GitHub
```

## Slide 83

notepad-plus-plus.org

github.com/.../npp.8.6.9.Installer.x64.exe

objects.githubusercontent.com

## Slide 84

Map “Domain Paths” to executables + their sizes Wait for “Domain Path” hit

Count TCP data

If � TCP data <= actual executable size � 15%� We know it’s the executable

## Slide 85

Force Detect EXE WiFi Download Connection Name Crash

## Slide 86

Goal:

Overwrite an executable downloaded by a victim before it runs

Needed Abilities:

Know downloaded executable file names

Overwrite files (not just create)

?

## Slide 87

\```
Check if
VSCodeSetup.exe exists
\```


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Chrome’s Download Process
Check if
VSCodeSetup.exe exists
```

## Slide 88

\```
Check if
VSCodeSetup.exe exists
\```

\```
Unconfirmed
550383.crdownload
\```


> Recovered by OCR — confidence 88/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Chrome’s Download Process
Check if
VSCodeSetup.exe exists
Unconfirmed
550383 .crdownload
```

## Slide 89

\```
Check if
VSCodeSetup.exe exists
\```

\```
Unconfirmed
550383.crdownload
\```

\```
VSCodeSetup.exe
\```

## Slide 90

\```
Check if
VSCodeSetup.exe exists
\```

\```
Unconfirmed
550383.crdownload
\```

\```
VSCodeSetup.exe
\```

## Slide 91

\```
Check if
VSCodeSetup.exe exists
\```

\```
Unconfirmed
550383.crdownload
\```

Hold last TCP packet

Send malicious **`VSCodeSetup.exe`**

\```
VSCodeSetup.exe
\```

## Slide 92

.crwd is renamed and our file is deleted


> Recovered by OCR — confidence 90/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Overwriting Chrome’s Download
.crwd is renamed and our file is deleted
94.9 MB » Done
Recent download history
```

## Slide 93

Can we maybe prevent our file from being deleted?

1. Send malicious **`VSCodeSetup.exe`**

2 . Make Quick Share continuously open **`VSCodeSetup.exe`**

## Slide 94

Result:

Chrome deletes the .crdownload file Leaves our malicious file in place Reports successful download completion Refers to our malicious file

## Slide 95

Force Detect EXE Force WiFi Download Continuous Connection Name Open Crash Send a File QuickShell Without RCE Approval


> Recovered by OCR — confidence 84/100 on the text kept, 60/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Force Detect EXE Force ae 7
WiFi Download Continuous O2
Connection Name Open x
Crash Send a File QuickShel
Without RCE
Approval
```

## Slide 96


> Recovered by OCR — confidence 83/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
emo
© B Administrator: Windows Pow X + v
PS C:\Users\Or\Documents\QuickClick> python .\main.py test-ap Password1 192.168.137.1 2412
Settings
€ > vy A RF - Network and Internet > Network Connections
Disable this network d Rename this connection View Mobile hotspot
Bluetooth Network Connection Ethernet 2
A VMware Network Adapter VMnet1 A VMware Network Adapter
Share over
Ethernet 6
Power saving
When no devices are connected, automatically turn off mobile hotspot
Properties
Network properties
Name: test-ap
Password: Password!
Band: 2.4 GHz
Bitems | 1 item selected | Nevices cannerted: Naf R
: Network & internet >» Mobile hotspot
Wi-Fi v
of @
Edit
Attacker Laptop|h
```

## Slide 97

## Slide 98

- Remote Unauthorized File Write

- 1. in Quick Share for Windows

- Remote Unauthorized File Write

- 2. in Quick Share for Android

- Remote Forced WiFi Connection

- 3. in Quick Share for Windows

- Remote Directory Traversal in

- 4. Quick Share for Windows

- Remote DoS in Quick Share for

- 5. Windows � Endless Loop

- Remote DoS in Quick Share for

- 6. Windows � Assert Failure

Remote DoS in Quick Share for 7. Windows � Assert Failure

   - Remote DoS in Quick Share for Windows � Unhandled Exception

8.

   - Remote DoS in Quick Share for Windows � Unhandled Exception

9.

Remote DoS in Quick Share for 10. Windows � Unhandled Exception

## Slide 99

- Remote Unauthorized File Write

- 1. in Quick Share for Windows

- Remote Unauthorized File Write

- 2. in Quick Share for Android

- Remote Forced WiFi Connection

- 3. in Quick Share for Windows

- Remote Directory Traversal in

- 4. Quick Share for Windows

- Remote DoS in Quick Share for

- 5. Windows � Endless Loop

- Remote DoS in Quick Share for

- 6. Windows � Assert Failure

- Remote DoS in Quick Share for

- 7. Windows � Assert Failure

- Remote DoS in Quick Share for

- 8. Windows � Unhandled Exception

- Remote DoS in Quick Share for

- 9. Windows � Unhandled Exception

Remote DoS in Quick Share for Windows � Unhandled Exception

#### 10.

## Slide 100

## Slide 101

Reported to Google about Invalid UTF8 continuation bytes crashing Quick Share

Example we provided – “\x00FileName” Google’s patch � Verifies file names don’t start with “\x00”

## Slide 102

Instead of “\x00”, setting a different invalid UTF8 continuation byte in file names

Example – “\xc5\xffFileName”

Result:

Quick Share crashes again

## Slide 103

Files are still written to disk on Windows but are later deleted.

Google calls them: “Unknown Files”


> Recovered by OCR — confidence 88/100 on the text kept, 64/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Patch - Remote Unauthorized File Write
PowerShell
Files are still written
to disk on Windows
but are later deleted.
¢ New NN Sort one Saar
+ Select
```

## Slide 104


> Recovered by OCR — confidence 83/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
const IncomingShareSession& session) {
LOG(INFO) << __func__ << ": Cleaning up payloads due to transfer failure";
nearby_connections_manager_->ClearIncomingPayloads();
auto file_paths_to delete =
for (auto it = file_paths_to_delete.begin(); it != file_paths_to _delete.end();
++it) {
VLOG(1) << __func__ << “: Has unknown file path to delete.";
}
files_for_deletion.insert(files_for_deletion.end(), payload_file_path.begin(),
payload file_path.end());
```

## Slide 105

Send two FILE Payload Transfer Frame with the same Payload ID

Result:

Only the first file is deleted


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Bypass - Remote Unauthorized File Write
Send two FILE Payload Transfer Frame with the same
Payload ID
Result:
Only the first file is deleted
```

## Slide 106


> Recovered by OCR — confidence 77/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BP Windows PowerShell x qe Oo x
PS C:\Users\Or\Documents> .\send_file_with_bypass_after_fix.exe wifi_lan 127.0.0.1 33506 C:\Windows\System32\calc.exe QVRUQUNLRVJfRk
Downloads x + from your devices - Ready to receive
< ay G © > Downloads > Search Do, Q ices that are signed into
ch.labs@gmail.com can share
device
@ New ~ ie “NL Sort ~ oe CB Details
& Gallery |
> @ Or- Personal
Downloads #
& Pictures * Drop files or folders to send
B documents #
aitet cot + Select
```

## Slide 107

"We greatly appreciate research from the security community that helps keep our users safe. We have deployed fixes for all of the reported vulnerabilities. To our knowledge, these vulnerabilities have not been exploited in the wild. No action is required by Quick Share users. The fixes will be automatically applied.

Developers using the open source repository can refer to the CVEs for further information on how to apply the fixes:

CVE-2024-38271 CVE-2024-38272

July 23<sup>rd</sup> , 2024

## Slide 108

CVE�2024�38271 – Forcing a lasting WiFi connection CVE�2024�38272 – File approval dialog bypass CVE�2024�10668 � Fix Bypass for CVE�2024�38272


> Recovered by OCR — confidence 73/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CVEs
CVE- 2024- 38271 - Forcing a lasting WIFI connection -
CVE- -2024- 38272 - File approval dialog bypass
CVE- -2024- 10668 - - Fix x Bypass for CVE- 2024- 38272
```

## Slide 109

## Slide 110

Standard stones may sometimes be forged into deadly drones


> Recovered by OCR — confidence 97/100 on the text kept, 97/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Takeaways
Standard stones may sometimes be forged into deadly drones
```

## Slide 111

Standard stones may sometimes be forged into deadly drones It's crucial for vendors and organizations not to underestimate seemingly simple bugs or known issues

## Slide 112

Standard stones may sometimes be forged into deadly drones It's crucial for vendors and organizations not to underestimate seemingly simple bugs or known issues It’s crucial to not fixate solely on memory corruption and fuzzing techniques when examining a program's security

## Slide 113

@oryair1999 https://www.linkedin.com/in/or-yair/

@_BinWalker_

https://www.linkedin.com/in/the-shmuel-cohen/

# QuickShell
