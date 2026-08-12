---
title: "Bird Hunting Season The Final Flight"
speakers: ["Jon Gaines"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: 2026
source_pdf: "DEF CON 34/DEF CON 34 - Jon Gaines - Bird Hunting Season The Final Flight - v1.pdf"
pages: 38
sha256: "5c761d9356f3e6a7c1550d3951e1a3f0e77ac3975a26e7264d5f52ec6f3a1541"
text_chars: 47868
ocr_pages: 30
has_ocr: true
redacted_secrets: 0
ocr_confidence: 89.4
ocr_unreliable_blocks: 1
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:37:47Z"
---
# Bird Hunting Season The Final Flight

**Speakers:** Jon Gaines  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Jon Gaines - Bird Hunting Season The Final Flight - v1.pdf` (38 pages)


## Slide 1

# **Bird Hunting Season**

# **Final Flight**

## Slide 2

## **Disclaimer**

**This work was conducted independently, self-funded, and outside the scope of my employment. It was performed on hardware I acquired through third-party marketplaces and tested in a controlled lab environment. Vulnerabilities/Issues went through the responsible disclosure cycle.**

**My current employer was not involved in, consulted on, or responsible for this research. No employer resources, systems, data, time or confidential information were used. Same for any previous employers.**

**The views and conclusions presented are my own and do not represent my current or former employers. I am only covering my observations; no claims regarding production deployments. The underlying technical research was completed months before this presentation. BirdShot is for authorized, educational, and defensive use. Don’t just take my word for it…**

**01**

## Slide 3

## **Who am I**

### Jon "GainSec" Gaines

- Lifelong Hacker

- Sr Security Engineer @ Anduril

- Adjunct Instructor @ Herkimer College

- Founder @ GainSec

- Dumb number of CVEs across various technologies

- Open-Source Contributor & Maintainer

- 10 years doing offensive engagements professionally

- Skateboarder

- Family man

## Slide 4

**Why This Work Exists**

## Slide 5

**What You’ll Walk Away With**

## Slide 6

## **Ecosystem: Hardware**

- Raven: audio/gunshot detection hardware

- Falcon / Sparrow: LPR and camera hardware

- Picard / Bravo: compute box and video infrastructure

- Penguin battery

- Picard battery

- Gray battery I forgot the name of

05

## Slide 7

**Ecosystem: Software**


> Recovered by OCR — confidence 94/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Ecosystem: Software
DEVICE SUITE / CONTROL / OTHER
Phone Home Service
com.flocksafety.android.phonehomeservice
System Control
Peripheral
Collins
Settings Service
com. flocksafety.android.settingsservice
Camera Updater
com.flocksafety.android.cameraupdater
Assembly Validator
Quality Control
com. flocksafety.android.qualitycontrol
Sensor Service
Upload Client / St Germain
WifiHotSpot
Flock System Test
Sambuca
Pisco
WhistlePig
com.flocksafety.android.whistlepig
VERSION + SCOPE
6.35.23
6.35.35 / 7.38.5
6.35.23
6.35.35 / 7.38.3
6.35.18
6.35.30 / 7.38.3
6.35.23
6.35.31 / 7.38.3
6.35.18
6.35.18
6.35.18
6.35.23
6.35.18
6.35.23
8.1.0
code 27
installed path
version not confirmed
6.35.18
6.35.35
6.21.11
7.72.2
Device check-in and telemetry reporting service.
System coordination and control service.
Peripheral and hardware-control service.
Local admin, live-view, and device-control service.
Device settings content provider and configuration sen
Camera update service started at boot.
Validation service present as a system app/process.
Quality-control service present as a system app/proces
Sensor service/provider used by other device apps.
Upload-client service present as a system app/process.
Hotspot/local network component relevant to wireless
access behavior.
System test app observed running as UID 1000 and wri
logs.
Provisioning/auth-related system APK.
Device-suite app tied to the hardcoded Auth0 client-se
finding.
Picard/Bravo audio app/service.
VIDEO / VISION / MEDIA + PUBLIC APPS
Objects / DetectionProcessing
Ciroc
com. flocksafety .android.ciroc
Cachaca / Burst Cam
com. flocksafety.android.cachaca
Motion
com. flocksafety.android.motion
Encoding
com. flocksafety .android.encoding
Video Recording
Video Streaming
Camera Config
com. flocksafety.android.cameraconfig
Medalla Light
com. flocksafety.android.medallalight
Amarula
com. flocksafety.android.amarula
Big Boi Bud
com. flocksafety.android.bigboibud
FlockCamera
com.flock.camera
FSinstaller
Flock Safety
Flock On Patrol
com. flocksafety.android.negroni
VERSION + SCOPE
6.35.23
6.35.33 / 7.38.3
6.35.23
6.35.34
6.35.23
6.35.31
6.35.23
7.38.3
6.35.23
7.38.3
7.38.3
7.38.3
7.38.5
6.35.23
6.35.23
6.35.31
6.35.23
6.35.31
8.1.0
code 27
2.4.0
1.49.1
1.48.0
Object and visual detection processing app.
Core vision and orchestration daemon.
Burst/capture camera app.
Motion-processing stage in the recording pipeline.
Media encoding and upload-staging service.
Camera capture and recording service.
RTSP/RTP video streaming service.
Camera configuration and admin UI app.
Device media/light-related service present as a system app/
process.
In-scope system APK with media/database-adjacent
indicators.
In-scope system APK; role not fully confirmed in current
notes.
Camera package observed on Falcon devices.
Installer and device activation app.
Public/mobile Flock Safety app.
Patrol and plate-lookup app.
```

## Slide 8

**Bird Hunting Season: Timeline**


> Recovered by OCR — confidence 93/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Bird Hunting Season: Timeline
Jan Feb Mar May Jun Sep
Research 0
Disclosure
Flock response C5]
Feeds arc
Release
(Research ) (VendoriCVE ) (Publicdisclosure ) (Flock response ) (Exposed feeds ) (Release )
1-7: acquisition to first public release 8-14: CVE batch to wireless/local
C7) 2025-01 oe 2025-06-27
Acquired first Flock hardware First CVE batch published
2025-02-08 2025-06-27
Initial vendor contact Follow-up deadline provided
Vendor response
Flock confirmed validation/triage in progress
2025-03-07
Vendor CVE request for initial set
2025-06-27
Further vulnerabilities disclosed to Flock
2025-05.05 2025-09-03
Flock PR article about the vulnerabilities Flock said existing CVEs applied; researcher disputed
scope
2025-06-19 2025-09-19
Part 1 public disclosure Compute box disclosure
2025-06-19
Further vulnerabilities disclosed to Flock
2025-09-27
Wireless/local admin disclosure
Oct
Nov Dec Jan Feb
® ®
15-21: Part 4 to CEO response
®
2025-10-23
Further vulnerabilities disclosed to vendor, Part 4
2025-11-05
Whitepaper v1 public release
2025-11-05-ish
First major YouTube visibility; whitepaper released to
land with the video
2025-11-06
Flock whitepaper PR statement / public response
2025-11-11
Whitepaper v1.2 public release with 51 findings
2025-11-11
Further vulnerabilities disclosed to vendor, Part 5
2025-12-08
CEO Linkedin security posture response
DEF CON
22-28: feeds arc to DEF CON
®
®
2026-01-ish
Benn/404 lead of 4 exposed feeds expanded to 67 total
2025-12-23
Flock Condor configuration issue statement
2026-01-06
Flock “Has Flock Been Hacked?” response
2026-01-09
Exposed camera feed/debug interface write-up
2026-01-23
Full Disclosure Part 4
2026-02-11
Full Disclosure Part 5
DEF CON 2026
Final Flight + BirdShot release
```

## Slide 9

**The Usual Suspects**


> Recovered by OCR — confidence 93/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Failure class
Boot / Root Of Trust
Debug / Maintenance
Access
Secrets / Configs /
Credentials
Local Services /
Admin Control
Media / Evidence
Handling
ML/ Model Exposure
Network / Tunnel
Boundaries
Unsupported /
Production Build
Posture
The Usual Suspects
What it means
Secure boot, bootloader, flash’eMMC/UFS encryption,
EDL/QDL, anti-rollback.
Debug features or maintenance paths that changed the
access level or impact.
Client material, static credentials, provisioning values,
API keys, keystores, and app secrets exposed in
artifacts.
Local service reachability became administrative
capability, shell, or system command execution.
Recorded media, replay paths, retention, directories,
and encryption boundaries behaved like ordinary files
or services.
Audio/visual model assets and inference outputs were
reachable or extractable enough to analyze/replay.
Network placement, cleartext paths, local wireless, and
FRPéunnel behavior weakened service boundaries.
Deployed software/build posture created risk
independent of a single exploit chain.
Where it shows up
Raven efuse/firmware evidence;
Falcon/Sparrow fastboot/EDL; Picard/Bravo
boot state.
UART/JTAG, ADB, sideload,
JDWP/debuggable apps, debug broadcasts,
data-log cleanup.
Raven NVS/config; Falcon/Picard Android
apps; public apps; FS Installer assets.
Collins/admin APIs, local wireless position,
ADB-over-TCP, public-app RCE framing.
Recording directories, shared media library,
per-file encryption, retention, external
partitions.
Raven audio classifier; Android visual model
stack; BirdEye/model replay context.
DNS spoofing, cleartext comms,
SpeedPourer/FRP, video/control fallback path.
Unsupported Android 8.1; production apps
with debug behavior; broad privileged app
suite.
Issue IDs
1, 5, 8, 13-15, 18,
22-24, 27
25, 26, 34, 35, 38
28-30, 33, 41, 51
31, 32, 36, 39, 44,
5
9, 42
11, 47, S2-S4
19, 35
```

## Slide 10

## **Raven: Plucked And Rooted**

**08**


> Recovered by OCR — confidence 76/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Raven: Plucked And Rooted
ER Hardware on the bench 2 Boot logs gi ESP eFuse summary
liga =
a,
6 | Debug shell menu
# NVS csv file
key type encoding value
eS Ue nigeL@SectorB6: $ strings sta.apinfo.bin
isRegistered data u8 e Flock
clientid data string xvigsytnYyrs7pk8g ciahiiies peed
clientSecret data string BcyZHiz-D49AqQ¢ query Flock-230503
serialNumber data string '240821702E3 “ee - security
partNumber data string 703-00006 Bie Sees) na
consoleLogEn data u8 0 Ay4TwnB43fmx
iB misc namespace
nvs.net80211 namespace
```

## Slide 11

**Raven: Takeaway**


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Raven: Takeaway
Issue
Flash encryption disabled
Secure boot disabled
JTAG enabled
UART download mode enabled
No anti-rollback protection
Hardcoded Wi-Fi SSID/password in firmware/NVS
Device auto-connects to matching Wi-Fi when LTE/modem unavailable
Cleartext API client ID/client secret in NVS
NVS modification enables UART console / debug shell
UART console has no password once enabled
Firmware readable with standard ESP32 tooling
Debug/console strings and operational config exposed in firmware
Cloud/API endpoint and provisioning material exposed in firmware/config
| Audio event detection model / classifier pipeline exposed
| Lack of server verification / DNS spoofing path
CVE
CVE-2025-47820
CVE-2025-47819
CVE-2025-47819
CVE-2025-47819
No separate CVE / N/A
CVE-2025-47818
Related to CVE-2025-47818
CVE-2025-47821
CVE-2025-47819
CVE-2025-47819
Covered by CVE-2025-47820
No separate CVE
No separate CVE
No separate CVE
No separate CVE
```

## Slide 12

**Falcon / Sparrow: Grounded Flight**


> Recovered by OCR — confidence 82/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Falcon / Sparrow: Grounded Flight
i Carrier boards / SoM Fy Fastboot posture Ei EDL / Firehose
main - Waiting for the device
main - Device detected :)
sahara ~ Protocol version: 2, Version supported: 1
-—(reot®@ ka /home/kali- main - Mode detected: sahara
L sahara -
® fastboot getvar all Nanaion ace
(bootloader) batt k
(bootloader) battery-voltage:3933000 Serial: OxBsbechce
(bootloader) variant:Dragon eMMC sahara - Protocol version: 2, Version supported: 1
sahara - 32-Bit mode detected.
(bootloader) secure:no sahara - Firehose mode detected, uploading...
(bootloader) version-baseband: sahara - Loader successfully uploaded
oe pay . . . . = . main - Trying to connect to firehose loader ...
4 | Read boot partition 5 | Root shell 6 | Camera feed running
main - Using loader ALPR-DOR-FIREHOUSE.mbn ...
main i Waiting for the ee 8953_ 32: 2 / $s
# ./edl reset —Loader=ALPR-DOR-FIREHOUSE .mbr root
Qualcomm Sahara / Firehose Client V3.62 (c) B.Kerler 2018-2024
main - Using loader ALPR-DOR-FIREHOUSE.mbn ... *
main = Waiting for the device msm8953_32:/ # whoami
main - Device detected :) eed
main - Mode detected: firehose
DeviceClass - USBError(19, 'No such device (it may have been disconnected)') root
```

## Slide 13

**Falcon / Sparrow: Takeaway**


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Falcon / Sparrow: Takeaway
Issue
Root shell
Secure boot disabled
Unlocked bootloader
Unauthenticated EDL/QDL mode
Unauthenticated ADB shell access
ADB sideload allowed
No flash/eMMC encryption
Unsupported Android 8.1 embedded OS
Development/test Wi-Fi credential in production
Hidden hotspot/default-password debug path
Unauthenticated Collins administrative API
Wireless RCE to shell via Collins / ADB-over-TCP
Wireless RCE to system via Collins + debug chain
Wireless RCE to root via Collins + data-log cleanup
CVE
No
CVE-2025-47822
CVE-2025-47822
CVE-2025-47822
No
No
CVE-2025-47824
No
CVE-2025-59409
No
CVE-2025-59403
CVE-2025-59403
No
No
Issue
Privileged Android apps shipped debuggable
Unauth debug broadcast clears settings/shuts off device
Root command injection via data-log cleanup
Cleartext API keys / credentials
Hardcoded Java keystore and password
Hardcoded Auth0 secret
Hardcoded Datadog API token
Incorrect permissions on media recording directories
Shared media library allows cross-app data exposure
Lack of per-file encryption on sensitive media
Excessive sensitive media copies persist on disk
Cleartext Al/ML local inference modules exposed
Data recording retention relies solely on disk capacity
Records stored on unencrypted external partition
CVE
No
No
No
CVE-2025-47823
CVE-2025-59407
CVE-2025-59406
CVE-2025-59405
No
No
No
No
No
No
No
```

## Slide 14

**Check in**


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Check in
Products Solutions Privacy & Security Resources Company
How Data Transmission from Flock Sensors Work In Practice
Flock’s LPR camera and gunshot detection system is made up of individual sensors
connected to each other and to the cloud through cellular networks. LPR cameras record
still images of vehicles when triggered by motion. When a gunshot, firework, or audio
event indicative of a sideshow stunt (like sustained tires screeching) is detected, our
gunshot detection devices record a three-second audio clip to be preserved as evidence.
Images, audio and associated metadata are encrypted and transmitted to the
cloud through Transport Layer Security (TLS) encryption. The data is then stored
encrypted in the cloud for 30 days so it can be accessed if it needs to be used
as evidence in a case. On the device, images and audio are regularly deleted.
The gunshot detection device cannot hold more than 50 seconds of audio.
Description
Ongoing Security Reinforcements
Flock’s security team was recently alerted about limited, localized security vulnerabilities on
our license plate readers and gunshot detection devices. As responsible stewards of customer
data, upon notification we analyzed the impact of these vulnerabilities and subsequently have
made the following submissions to Mitre for inclusion in the National Vulnerability Database.
Debug interface enabled (CWE-1191)
Hardcoded credentials (CWE-798, CWE-259)
Hardcoded connection details (CWE-798, CWE-259)
Clear Text Storage of Code (CWE-312)
These are not material vulnerabilities, and both severity and likelihood to be exploited
are low. The exploitation of these vulnerabilities require physical access to a device
and knowledge of device debugging. If a person was able to gain physical access to
the device (which is typically placed on a pole several feet above normal height), they
would still not be able to gain access to footage, as the data is only stored for a very
limited time duration on the device following its transmission to the cloud.
None of these vulnerabilities affect our cloud platform, where the vast majority of all evidence
and metadata is stored. Flock secures data in accordance with industry requirements, including
encryption using AES-256, as validated by the company’s ISO 27001 compliance certification.
Flock Safety LPR (License Plate Reader) devices with firmware through 2.2 have an on-chip debug interface with improper access control.
```

## Slide 15

**Picard / Bravo Compute Box: Root from the Coop**


> Recovered by OCR — confidence 78/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Picard / Bravo Compute Box: Root from the Coop
Ei Compute box hardware = Secure boot off / UFS EF} EDL | Firehose read
main - Using loader prog_firehose_ddr.elf ...
main - Waiting for the device
main - Device detected :)
Welcome to minicom 2.10
OPTIONS: 118n Progress: | | 100.0% Read (Sector @x93FB00 of @x949DD3, ) 38.90 MB/s
Port /dev/ttyUSB®, 03:10:53 [U] Progress: | | 106.6% Read (Sector @x93FCOO of @x9U6DD3, ) 40.65 MB/s
Progress: | | 100.e% Read (Sector @x93FD00 of @x9U0DD3, ) 36.4u MB/s
i ; Progress: | | 100.0% Read (Sector @x93FE80 of @x948DD3, ) 49.53 MB/s
Press CTRL-A Z for help on special keys Progress: | | 100.6% Read (Sector @x93FF9 of @x9460D3, ) 36.96 MB/s
Progress: | | 100.0% Read (Sector @x940000 of @x9U8DD3, ) 49.93 MB/s
Format: Log Type - Time(microsec) - Message - Optional Info Progress: | | 100.6% Read (Sector 0x940109 of @x94@DD3, ) 36.75 MB/s
Log Type: B - Since Boot(Power On Reset), D-—- Delta, S - Statistic Progress: es Read Goes barton of poser x eld ae
OCKOCI a Progress: | | 100.6% Read (Sector @x940509 of @x94@DD3, ) 35.95 MB/s
$ ~ OEM_IMAGE_VERSION_STRING=4c1b83U1de57 Progress: | | 100.6% Read (Sector @x940609 of @x946DD3, ) 39.87 MB/s
S - Boot Interface: UFS Progress: | | 100.0% Read (Sector @x948700 of @x9U8D03, ) 38.52 MB/s
S - Secure Boot: Off Progress: | | 100.6% Read (Sector @x9U0800 of @x9U0DD3, ) 42.66 MB/s
4 | Fastboot reports unlocked GB Vendor shell context 6 | Root proof
-# fastboot getvar all
(bootloader) parallel-download-flash: yes
(bootloader) hw-revision: 10000
(bootloader) unlocked: yes BRAVO:/ $ runcon u:r:vendor_shell:s® /system/bin/sh
(bootloader) off-mode-charge:0 Tuncon: Could not set context to u:r:vendor_shell:s®: Permission den: root SectorTL /mnt /SECOND/Compute—Box-2-POSTROOT
(bootloader) charger-screen-enabled:@ cL iesinetlh i # adb shell whoami
(bootloader) battery-soc-ok: yes u:r:vendor_shell:s® root
(bootloader) logical-block-size: 0x1000
(bootloader) variant:QCS UFS
```

## Slide 16

**Picard / Bravo Compute Box: Takeaways**


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Picard / Bravo Compute Box: Takeaways
Issue
Root shell on Picard/Bravo Compute Box
Secure boot disabled
Unlocked bootloader
Unauthenticated EDL/QDL mode
Unauthenticated ADB shell access
ADB sideload allowed
No flash/UFS encryption
Hidden hotspot/default-password debug path
Unauthenticated Collins administrative API
Wireless RCE to shell via Collins / ADB-over-TCP
Wireless RCE to system via Collins + debug chain
Wireless RCE to root via Collins + data-log cleanup
Privileged Android apps shipped debuggable
Unauth debug broadcast clears settings and shuts off
device
Root command injection via data-log cleanup
CVE
No
CVE-2025-59408
CVE-2025-59404
CVE-2025-59402
No
No
No
No
CVE-2025-59403
CVE-2025-59403
No
No
No
No
No
Issue
Cleartext API keys / credentials
Hardcoded Java keystore and password
Hardcoded AuthO secret
Hardcoded Datadog API token
Incorrect permissions on media recording directories
Shared media library allows cross-app data exposure
Lack of per-file encryption on sensitive media
Excessive sensitive media copies persist on disk
Cleartext AI/ML local inference modules exposed
Data recording retention relies solely on disk capacity
Records stored on unencrypted external partition
SpeedPourer/FRP cleartext video/control fallback path
SpeedPourer/FRP config permission/control issue
SpeedPourer/FRP reverse-proxy/admin exposure
CVE
CVE-2025-47823
CVE-2025-59407
CVE-2025-59406
CVE-2025-59405
No
No
No
No
No
No
No
No
No
No
```

## Slide 17

**Public Apps: Takeaways**


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Public Apps: Takeaways
App
FS Installer
com. flocksafety.hazyhiwire
FS Installer
com. f locksafety.hazyhiwire
Flock On Patrol
com. flocksafety.android.negroni
Cleartext device-control channel
Global cleartext traffic plus hardcoded HTTP device-control URLs for activation, local control, and
OTA-style workflows.
Sensitive operational artifact disclosure
Bundled Raven BLE configuration map, Penguin firmware/bootloader ZIPs, local service URLs,
device workflow strings, and field-task logic.
Authorization tokens logged to Logcat
Release networking stack configured OkHttp BODY logging for plate lookup calls, exposing
headers and response bodies to adb logcat.
CVE
No
No
```

## Slide 18

**Before The Feed Exposure**


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Before The Feed Exposure
ORIGINAL
RESEARCH,
ANALYSIS
DISCLOSURES AND
AUTHORED BY JON
“GAINSEC” GAINES*
*Contribution from Joseph
“JosephRC” Cohen
Examining the securit
posture of an Anti-
Crime Ecosystem
Version: 1.2-PR
November 11, 2025
F | (@) Cc k Products Solutions
wo Qs flocksafety.com, i u
Privacy & Security Resources Company
On November 5th, 2025 an independent security researcher published a
white paper compiling previously published security findings about Flock
hardware and software. The scope of the security research included:
Audio Detection hardware
License Plate Recognition (LPR)
Compute Box
Android applications deployed on those devices
Android applications available on public app stores.
The researcher has been in contact with Flock Safety throughout the course of their
work and notified Flock of findings earlier in 2025. In response, Flock posted a customer
advisory addressing the researcher's findings with respect to our Audio and LPR
devices; Flock registered the vulnerabilities with the National Vulnerability CVE database
via Mitre. Since then, Flock continues to transparently and publicly report findings.
As our customers have come to expect, Flock continues to prioritize their
security by continuously evaluating the security of devices and resolving
vulnerabilities in accordance with potential risk to customer environments.
The white paper released on November Sth confirms the reported findings that have been
previously publicly disclosed; those that have been reported otherwise are under review by MITRE.
Overall, none of the vulnerabilities detailed in the report have an impact on our customers' ability
to carry out their public safety objectives. Exploitation of these vulnerabilities would not only
require physical access to a device, but also require intimate knowledge of internal device hardware.
2M views = 7 months ago
HACKING 80.000+
```

## Slide 19

**Video Stack Overview: Architecture**


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Video Stack Overview: Architecture
Older Collins Path Newer CameraConfig / Streaming Stack
LPR local admin API triggers MJPEG live view. Camera admin UI, RTSP replay/live streams, ONVIF, and FRP exposure paths.
>
Falcon / Sparrow LPR Camera Device / Compute Stack
Android-based LPR device with camera pipeline and local services. Ciroc orchestrates capture, recording, streaming, status, and config services.
v v.
: Admin API CameraConfig Streaming SpeedPourer
Collins App —_ >» Local API surface on port 8080. Live view, Admin web portal, video RTSP live/replay via video FRP and port forwarding
com.flocksafety.android.collins device status, crashpack, reboot, ADB listings, config, diagnostics. streaming components. around local camera services.
toggles.
v
HTTP Admin RTSP / HLS ONVIF / Camera API
Enable MJPEG videoAdmin, getVideo, Live and replay streams tied Device, media, PTZ, analytics,
API flips stream state and returns live view > Local image stream, commonly observed deleteVideo, logs, diagnostics. to camera IDs and ports. events surfaces.
metadata. around port 1234.
{L Admin portal exposed video listing, diagnostics, SpeedPourer/FRP could bridge internal services
replay, logs, and deletion controls. across network boundaries.
Viewer / Proxy / Local Client
- re 5 - F 7 RTSP/HLS paths turned local camera services into ONVIF expanded the surface beyond simple video
Feed can be viewed by a local client or bridged during lab testing. The boundary is local network access, direct feed access. playback.
not user authentication.
Failure pattern: service composition turned camera operations into an exposure surface.
Failure pattern: local network reachability was treated like authorization.
```

## Slide 20

**ML Stack Overview**


> Recovered by OCR — confidence 93/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
MIL Stack Overview
Raven Gunshot Detection Falcon / Sparrow / Bravo / Picard
Embedded audio event classifier on an ESP32 + Syntiant NDP120 path. Android visual recognition stack with extractable model assets and replay tooling.
Microphone / Audio Input ESP32 Firmware Camera Capture Media Pipeline
Device captures surrounding audio after wake » Project name observed as Cachaca / Ciroc camera path creates media > Stages include captured, motionProcessed,
or event trigger. audio_event_detection. sessions and captured frames. detectionProcessed, encoded.
NDP120 ML Chip Audio Preprocessing DetectionProcessing TFLite Model Assets
Runtime logs identify NDP120-B0 and load > WAV stats, normalization, sample frames, and com.flocksafety.android.objects runs > YOLO / SSD models, labels, anchors, and
MCU/DSP firmware. tank size visible in logs. SessionFilter / nativeML metadata in flock-object assets.
gunshot tire background pakarien plates people
raw NNO label raw NNO label raw NNO label . > - > person plus other object
car, bus, truck, trailer licensePlate label
classes
Event Tag + Audio Upload Decision Offline Replay With BirdE
Logs show matching class, confidence values, “mark this data as ML data,” and follow-on audio handling. Extracted OEM model metadata can be replayed against video, frames, webcam input, or mounted media
sessions,
Confirmed: classifier labels and runtime behavior were Evidence: UART/debug logs, firmware strings, NDP
visible. config output. Confirmed: actual TFLite model files and label maps are Confirmed: on-device ML decisions affect
present locally. detectionProcessed output.
Raw labels observed: gunshot, tire, background.
APK assets: /system/app/flock-object/flock-object.apk!/ Runtime cache: /data/user/0/
```

## Slide 21

**Encryption And Media Handling: Observed Gaps**


> Recovered by OCR — confidence 90/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Encryption And Media Handling: Observed Gaps
1. Shared Recording Path
Flock-Sumarize/media-storage: 3-43
This shows the reviewed app used shared external storage for media paths, with local proof using
list/pull/play from /storage/emulated/0/flockMedia/media.
«method public final invoke()Ljava/io/File;
const-string v@, “flockMedia"
Landroid/os/Environment;—>
getExternalStoragePublicDirectory(...)
DIR_FLOCK_MEDIA = “flockMedia"
adb shell ls -R \
adb pull .../clip.mp4
Picard/Bravo runtime
3. Picard/Bravo Media Partition
logcat-2: 28791-28806 , 31828-31837
This shows Picard/Bravo media lived on /media/ufs, a separate ext4 media partition outside the /data
inlinecrypt mount.
mount:
/dev/block/sdal1 on /media/ufs type ext4
contex bject_r:flock_media_file:s®
/dev/block/dm-1@ on /data type f2fs
« inlinecrypt ...
MediaFileUtil runtime:
/media/ufs/media/capturing
/media/uts/media/captured
/media/ufs/media/motionProcessed
/media/ufs/media/detectionProcessed
/media/ufs/media/encoded
permission includes OTHERS_READ + GROUP_WRITE
( APK static trace )
2. Falcon/Sparrow Virtual Store
generic/media:7-16,29
falcon/logcat:3741, 3851-3869; dumpstate-output :57369
| Falcon/Sparrow storage
This shows the Falcon/Sparrow virtual media store key existed beside virtual_disk on the tested unit, and
Android mounted the matching private volume.
msm8953_32:/media # 1s
lost+found
virtual_disk
vold: PART 2 ... 426956D8...737A android_expand
vold: Found key for GUID 426956d8...737a
Cryptfs: /dev/block/vold/private:7,2
[persist.sys.virtual_disk]: [true]
SELinux boundary
4. DataLog Cleanup + SELinux
inits-in-etc-init-as-root:2-11; whitepaper text:493-497, 3609-3614
This shows a retention setting flowed into a root-run cleanup script; SELinux blocked the root-command
path by default.
SystemControlservice:
getSetting("dataLogsRetentionPeriodDays", "5")
set("flock.clean_data_partition", “1")
init service:
clean-data-partition -> /vendor/bin/clean_data_partition. sh
seclabel u:r:init:s®
property trigger: flock.clean_data_partition=1
script sink:
find /data/anr -mtime +$logs_retention_in_days -delete
```

## Slide 22

**PROPOSAL E.1 REVIEW DECK**

## **SpeedPourer**


> Recovered by OCR — confidence 91/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
SpeedPourer
PROPOSAL E.1 REVIEW DECK
1. Local Services (forwarded ports )
video-stack.md:443-477
speedpourer logs: 1718-1738
SpeedPourer defined forwarding rules for the camera portal
and RTSP service, bridging wireless interfaces to the camera-
side network.
cameraPortal{interface}
from wlan@:8081
to 192.168.0.100:80
rtsp{interface}
from wlan®:8082
to 192.168.0.100:554
TcpForwarder:
Starting forwarding server
fromInterface: wlan®
fromPort: 8081 / 8082
Cleartext Fallback CweE-319
When FRP is unavailable, the documented fallback path uses a static
LAN profile and cleartext RTSP/HTTP behavior instead of a protected
transport boundary.
Proof: for-cert:1-24
usesCleartextTraffic=true; SpeedPourer assets/ipconfig. txt;
192.168.0.0/24 profile
Disclosure Route
CERT / CISA VULS path recorded in meeting notes.
2. SpeedPourer Control Plane system service
Port +
BOOT_COMPLETED Tunnel frpc
auto-starts files/*. ini vBa/frpc
+ frp_lock
SpeedPourerService:
Auto-starting service due to BOOT_COMPLETED
Starting service. Version: 7.38.3
Successfully processed 2 port(s)
Successfully processed @ tunnel(s)
FRP config location:
Lock file:
Writable Tunnel Config ( ewe-732
The tunnel trust boundary collapsed into a local config file: with
system context, frpc.ini could be rewritten to alter the remote endpoint
and tunnel mapping.
Proof: for—cert:26-39
system:system; default 770/660 noted in disclosure
What Was Sent
New post-whitepaper CVE draft batch covering cleartext transport, FRP config access
control, and embedded FRP reverse-proxy exposure.
3. FRP Config Proof (rpe.ini)
frpsc-configs.txt:1-16
for-cert:60-73
A lab FRP server and on-device frpc.ini showed the same
control point: server address, token, local target, and public
remote port.
BRAVO: /data/user/@/.../speedpourer/files # cat frpc.ini
server_addr = <PUBLIC_IP>
server_port = 7000
token = testtoken
[web-tcp]
type = tcp
local_ip = 127.0.0.1
local_port = 8000
remote_port = 18080
Remote Exposure Pivot (cwe-28a )
Repointing FRP could bridge local Camera Config/admin surfaces
through a public FRP server, including video/admin handlers listed in
the disclosure package.
Proof: for-cert:41-73
/system/bin/frpc; Camera Config listener on 0.0.0.0:8000;
/videoAdmin, /getVideo, /deleteVideo, /LAPI/...
Source
for-cert:1-73
new_cve_submission-drafts.md:1-79
```

## Slide 23

**Check In**


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Check In Has Flock Ever Had a Data Breach?
No, Flock Safety's cloud platform has never experienced a data breach, and no customer data has
ever been compromised.
Garrett Langley Addressing Security
° Research Transparently
On November 5, 2025, an independent security researcher published a white paper that compiled
previously disclosed security findings related to Flock’s hardware and software
Security is never “done.” It's a commitment - and at Flock, it’s one we invest in every day.
Here's what's important to understand:
Here’s the ground truth on our security posture: P
* The researcher worked with Flock throughout the study and disclosed the findings to us earlier in
+ The Flock system has not been hacked. We secure customer data to the highest standard of 20256.
industry requirements, including strict industry standard encryption. Flock’s cloud storage has + Flock issued a customer advisory, registered relevant vulnerabilities with the National Vulnerability
CVE database via MITRE, and publicly disclosed information in line with industry best practices.
never been compromised.
fil ifety.com,
+ When we are made aware of vulnerabilities, even when they are immaterial, we a TSE SHE described were highly technical and would have required physical
report them ourselves, and develop a mitigation plan. Many of the recent claims rm detailed knowledge of its internal hardware. No vulnerability affected
have already been addressed by our security and engineering teams. systems, and no customer action was require
° Wade Hibbard 1 strengthens technology when it is handled transparently. Flock
Oh really? Just two questions. :ngages with researchers in good faith to improve our systems over time.
Are you still using Android 8 to run cameras?
- . - ‘vulnerabilities, even when they are immaterial, we actively report them
| Oo Cc k Products Solutions Privacy & Security Resources Company y yr
sation plan’ said Langley.
If MFA is enforced by default, then how were people able to access admin panels
SOE ie Ma TR RH, We recently identified and resolved a limited configuration issue affecting a very small
i : : number of Condor video devices. No LPR devices, audio devices, or trailers were impacted.
The issue involved a troubleshooting-only debug interface that was temporarily
accessible on the internet. This interface does not allow camera control, cloud access,
customer account access, or use of search or analytics features. The only content visible
was live or recorded video comparable to what can be observed from a public roadway.
The small subset of impacted customers was notified directly. The issue was
promptly corrected, and security updates were deployed across affected
devices. No sensitive or confidential information was accessed or accessible.
While recent third-party coverage characterized the issue as more extensive, this was
an isolated configuration issue and not indicative of a broader or ongoing concern.
```

## Slide 24

**Live Video Feeds Exposure**


> Recovered by OCR — confidence 87/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Live Video Feeds Exposure Flock Exposed Its Al-
Powered Cameras
to the Internet. We .
streaming and exposed to the open
f ock safety
@ season KOEBLER + DEC 22. 2628 AT 11:05 AM
internet.
This Flock Camera Leak is like Netflix For Stalkers
Benn Jordan @ and 404 Media
1.3M views = 6 months ago
```

## Slide 25

## **Turning 3-4 feeds into 67**

##### **PROPOSAL E.1 REVIEW DECK**


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Turning 3-4 feeds into 67
PROPOSAL E.1 REVIEW DECK
Seed Lead
Benn shared a small set of live examples; one cleartext HTTP URL on
an uncommon port proved the exposure was real.
Fingerprint
Extract stable traits from the examples: exposed admin UI, live-view
marker, service behavior, carrier/ASN pattern, and stack clues from
logs.
Expand Candidates
Use passive indexes first, then scoped checks around adjacent
network neighborhoods and relevant service ports to build candidate
lists.
Validate Non-Invasively
Confirm liveness using a page marker and screenshots/log evidence;
avoid control actions, deletion paths, or changing device state.
Deduplicate + Enrich
Collapse duplicates, count confirmed live instances, add rough
ASN/geolocation context, and package findings for responsible
handling.
writeup
116-123
writeup
128-136
310-316
writeup
316-326
8-12
writeup
326-328
347
What Changed
3-4
initial examples Benn found expansion
seed set, not final scope
Safety Boundaries
Shodan / ZoomEye phase
15-ish 67
live instances from passive
confirmed live camera
feeds
final confirmed list
The important technical story is not the exact query. It is the workflow: derive a fingerprint
from real examples, expand with low-touch OSINT, validate only enough to prove
exposure, then stop and preserve evidence.
No control-plane actions
No delete paths, reboot paths, credential
changes, PTZ movement, or device-state
changes were needed to count exposure.
Correlation, then restraint
Carrier/ASN and geolocation helped
understand scope, but exact physical locations
belong in disclosure handling, not slide copy.
Local Sources
exposed-feeds-writeup: 116-136 , 310-328, 347
lproper-full-list.txt: 67 confirmed lines
Evidence over interaction
Use visible markers, response shape,
screenshots, logs, and metadata to classify
exposed systems without operating the
cameras.
Keep raw target data off slides
Show counts and process. Keep IPs, paths,
and queries in private evidence bundles or
redacted appendices.
Validation Artifacts
check.sh: marker confirmation
leak/8900/*: candidate, checked, geo, final
lists
```

## Slide 26

**Exposed Feeds**


> Recovered by OCR — confidence 79/100 on the text kept, 56/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Exposed Feeds
| Save |
Y Camera |f1fbfd82-dfc1-40| Serial [241219Q0210024Y |
Type |falcon
DeviceType | picardCamera
Network
IP [192.168.0.10(| Port [554 | User | admin
| |
Channels
Streams
type | proxy port 9554 channel
V Camera | 46e05334-15ce-| Serial |241219002100230
Type |falcon
DeviceType picardCamera
Network
IP | 192.168.0.10(| Port | 554 User | admin —
OE | Save |
250121002101953
[Lo V Camera | f0bf45fa-86fd-4C| Serial {250625900FF
Channels Type | condor
| +Add channel | Network
Streams IP | 192.168.0.10(
| + Add stream | | + Add channel |
type [replay
| +Add stream |
DeviceType | access amera
| Port |554 | User | admin
| path | 250625900FF-replay | port|8554 | channel
99ab-| Serial |2408260021003AF
+ Add channel |
Streams
type |replay : 21003AF-r| port | 85! channel
| +,Add stream |
```

## Slide 27

**Exposed Feeds: Impact And Evidence**


> Recovered by OCR — confidence 95/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Exposed Feeds: Impact And Evidence
Reachable Surface
Live Video HLS / RTSP
Camera feeds and stream viewers exposed live video
Paths and stream state.
Admin Actions
Video admin flows exposed management controls
including video deletion/archive-style actions in the
stack.
delete / archive
Video Settings
Encoding output disclosed HEVC/H265 settings,
resolution, frame rate, media paths, and asset pipeline
behavior.
This was exposed edge infrastructure, not only exposed
video. The proof came from the same reachable surfaces:
screenshots, HLS clips, admin Ul captures, ONVIF
(codec / path )
Historical Media
Stored or replay-capable media paths appeared through
admin Ul and ONVIF recording/replay capability output.
Logs + Diagnostics (crashpack
Diagnostics revealed package names, media pipeline
state, modem/battery state, ADB debug state, and
crashpack contents.
Device Types (not one class )
Evidence crossed PTZ/Condor-style views,
Falcon/Sparrow/Flex-style LPR feeds, and Picard/Bravo
video-stack context.
Visual Artifacts
Camera feed captures, logs/diagnostic
screenshots, no-password and disclosed-password
Publicly Documented Scope
67
confirmed exposed feeds /
debug interfaces
expanded from Benn / 404 seed examples
15
public writeup scope statistic
cities
public writeup scope statistic
AS6167
Verizon Business
all 67 observed on this ASN
screenshots, admin interface clips, and converted No data changing action was performed during validation.
MP4 demo assets.
capability output, RTSP/session logs, and crashpack/log
artifacts.
```

## Slide 28

**Exposed Feeds: Why It Happened**


> Recovered by OCR — confidence 86/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Exposed Feeds: Why It Happened
Failure pattern: local network reachability was treated like authorization.
L3
Post /onvif/device_service HTTP/1.1
User-Agent: curl/8.7.1
Accept: */*
Content-Type: application/soaptxml; charset=utf-8
Content-Length: 216
Connection: keep-alive
<?xml version="1.0" encoding="UTF-8"?>
<s:Envelope xmlns:s="
http: //www.w3.org/2003/05/ soap-envelope">
<s:Body>
<tds:GetCapabilities xmlns:tds="
http://www. onvif. org/verl0/device/wsdl"/>
</s:Body>
</s:Envelope>
10
11
12
14
15
16
17
18
20
21
HTTP/1.1 200 OK
Server: Happytime onvif server V10.3
Content-Type: application/soaptxml; charset=utf-8
Content-Length: 7022
Connection: close
<?xml version="1.0" encoding="UTF-8"?>
<s:Envelope xmlns:s="
http: //www.w3.org/2003/05/soap-envelope”
xmlns:wsnt="http://docs. oasis-open. org/wsn/b-2"
xmlins:wstop="http://docs. oasis-open. org/wsn/t-1"
xmlns:wsrf-rw="http://docs. oasis-open. org/wsrf/rw-2"
xmlns:wsrf-r="http://docs. oasis-open. org/wsrf/r-2"
xmlns:wsdl="http://schemas.xmlsoap.org/wsdl"
```

## Slide 29

**Gated Wireless And Local Shell**


> Recovered by OCR — confidence 95/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Gated Wireless And Local Shell
Attack Chain Flow
Trigger Local Join Device
Network
Device enters a mode
where a Flock-named
local wireless network ——
becomes reachable
from nearby range.
Network
Shared/default wireless
credential behavior
moves the attacker from ——
physical proximity into
the device LAN/WLAN
trust zone.
proximity boundary shared credential
Why the chain mattered
The security boundary was not just “is the device physically
mounted high enough?” Local wireless access became
administrative API access.
Reach Collins
API
Collins exposes local
administrative
endpoints without
authentication,
including status, logs,
crashpack, reboot, and
ADB-enable surfaces.
CVE-2025-59483
What CVE-2025-59403 covers
The Collins application lacked authentication on local
4)
Enable ADB Over
TCP
The unauthenticated
local API can transition
the device from “ADB
closed" to a network-
reachable ADB state.
control transition
Shell Access
Once ADB is reachable
over the local network,
the chain reaches a
shell on the camera
device; adjacent
JDWP/system paths can
deepen impact.
local RCE / shell
administrative API endpoints and exposed actions capable of
enabling ADB-over-TCP.
```

## Slide 30

**ADB / JDWP / Privilege Chain: Compress It**


> Recovered by OCR — confidence 91/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ADB / JOWP / Privilege Chain: Compress It
Attack Chain Flow
ADB Shell
After ADB-over-TCP is enabled, command
execution starts in Android shell context.
System Execution
Because the target app runs as a privileged
system process, JDWP execution lands as
Android system.
Shell Injection
By default, command injection from this
position is shell-level: useful control, but not
root by itself.
10
Root Maintenance Path
System context can set the cleanup property
consumed by init-owned maintenance logic.
JDWP Attach
Privileged Flock apps shipped debuggable,
so JDWP attaches to the app process rather
than staying inside shell.
debuggable system app
"1
SELinux Boundary
The root command-injection path is present,
but SELinux blocked the root execution
outcome on the tested build.
uid=1000 (system) init/root service path containment observed
Why JDWP Changes the Context Data Cleanup Payload
JDWP executes inside the selected app process. When that var: persist.vendor.flock.data. logs.max_size_mb
process is a debuggable privileged system app, runtime execution
inherits the system app context.
payload: 1 J]; /system/bin/id > /data/local/tmp/flock_root #
trigger: flock.clean_data_partition=1
Privileged App Conditions
* android: debuggable=true
* android.uid. system / privileged app context
* JDWP active when ADB is available
* Runtime execution observed as
uid=1000(system)
Observed Boundary
* ADB command execution: shell context
* JDWP command execution: system context
* Root command-injection primitive:
maintenance path
* SELinux blocked the root execution outcome
on the tested build
Privilege Map
Default ADB command execution
Position.
JDWP inside debuggable privileged
system Flock app. 99 P 9
Feat Init-owned cleanup service and
property-driven script path.
SELinux Containment layer that blocked the
root outcome in testing.
```

## Slide 31

### **Improper Entitlement Authorization for Protected Artifact Access - Manufacturer Entitlement Pivot (MEP)**

#### **_Flea Market Supply Chain Attack_**

## Slide 32

## **Community And Third-Party Tools**

- Flock-You - ColonelPanic / colonelpanichacks - ESP32/OUI-SPY firmware for detecting Flock/Raven devices over WiFi/BLE.

- flock-you-wifi-recon - 0xXyc - passive ESP32 Wi-Fi recon focused on Flock ALPR probe/request behavior.

- Flock Sniff - JustCallMeKoko / ESP32Marauder - ESP32Marauder feature for detecting Flock devices with Wi-Fi/BLE sniffing.

- Flock Wardrive - JustCallMeKoko / ESP32Marauder - GPS-tagged Flock detection / wardriving workflow.

- fflock - developer not confirmed - Rust laptop/Raspberry Pi tool for passive BLE + Wi-Fi LPR/Flock detection.

- Flock You OLED - Storby42 - ESP32 OLED variant of Flock-You with on-device display/alerts.

- Pigtail - benbaker76 - anti-stalking/surveillance detector that includes Flock/Raven BLE detection.

- Flock-You ESP32 - simeononsecurity - standard ESP32 build/package for running Flock-You-style detection cheaply.

- FlipDeFlock - ReconGrunt - Flipper Zero app plus ESP32 companion for Flock/ALPR detection and site surveys.

- Flock-You-Android - MaxwellDPS - Android counter-surveillance app with Flock ALPR and other surveillance-device detection.

- What The Flock - WhatIsInCreedmoor - ESP-IDF port/expansion of Flock-You for ESP32 boards.

## Slide 33

**Demo: Recorded RCE**


> Recovered by OCR — confidence 68/100 on the text kept, 50/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Demo: Recorded RCE
is dew wlae® scan | grep SSID SecterTL: Sat Sep 13 O25 23/28 2025
SSID: Verizen_QoPern
SSID: Sector!
SSID: Sector!
```

## Slide 34

## **BirdShot: Why It Exists**

31


> Recovered by OCR — confidence 83/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BirdShot: Why It Exists
Phase Scope Task
PRE All Devices Inventory devices, firmware, app versions; record hashes
PRE All Devices Establish SBOM and signed update pipeline (TUF/Uptane-style)
' 1) main ta sUlging) ELCES PRE All Devices Adopt secure configuration baseline (no debug, no sideload, no unauth admin)
~ PRE All Devices Legal/ops banners and access policies for service interfaces
FIELD Raven Enable Secure Boot; enforce anti-rollback
a a | FIELD Raven Enable flash encryption
1} 2. ZEN PTT AAEM LIE] FIELD Raven Disable/lock UART download and JTAG; remove console or gate with auth
\____/_/ \\-__I_|] \_]---_/]_---- \____| FIELD Raven Enforce TLS server verification / pinning
IT'S BIRD HUNTING SEASON gala
SEC
Flock Safety Sniffer
Sending out the bird call and Sniffing...
I (1344) pp: pp rom version: 5b8dcf
I (1424) net80211: net80211 rom version: 5b8dcfa
Kis, |
```

## Slide 35

## **Introducing BirdShot**

https://github.com/GainSec/BirdShot


> Recovered by OCR — confidence 90/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Introducing BirdShot
Bird Hunting Season
Birdshot UI
Se
https://github.com/GainSec/BirdShot
```

## Slide 36

**Demo: BirdShot CLI**


> Recovered by OCR — confidence 91/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Demo: BirdShot CLI
=== Command Output ==
Main Menu (Device: Picard)
Shared Toolkit Workflow
Falcon / Falcon LR Utilities
Picard / Avicore Conversions
Raven Health Snapshot
Penguin Packs
Condor Utilities
Trap Shooter
Collins API
. JDWP Shell Cjdwp_exec)
10. Auto - Wireless RCE
11. Auto - Wireless RCE (System Shell)
Q. Exit
Commands: device (switch), devices (list), add (add offline), jobs (list), scan
(BLE scan)
menu> 9
Connected adb devices:
1. 241108P02100632 [device]
2. 192.168.227.119:5555 [device]
Select device by number: ff
```

## Slide 37

**Landing**


> Recovered by OCR — confidence 88/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Landing
Picard Battery Internals Penguin Bluetooth Characteristics
Device Information 7 characteristics
The Device Information Service exposes manufacturer and/
or vendor information about a device
Model Number (« F-PP-0001
Serial Number (« ™N72022122000290 Environmental sensing / secure DFU
Firmware Revision (« 2.4.0
Software Revision « 2.4.0 — tic dtu buttontocs exper
Manufacturer Name (« Flock Safety as
Position 3D (« 50
Not connected »)
No value available
Internals Board connector Device information service Buttonless DFU without bonds
```

## Slide 38

**Q&A**


> Recovered by OCR — confidence 93/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
11
12
13
14
Area
Raven
Raven
Raven
Raven
Raven
Raven
Raven
Raven
Raven
Raven
Raven
Faicon/
Sparrow / Flex
Sparrow / Flex
‘Sparrow / Flex
Issue
Secure Boot is Disabled
Debug UART Console Access
Lack of Password Debug UART
Console Access
Hardcoded Wi-Fi Credentials Auto
Connect
Lack of Flash Encryption
Debug Interface Accessible: JTAG
Debug Interface Accessible: UART
Download
No Anti-Rollback Protection
Audio ML/AI Model Disclosed
Hardcoded Credentials: API Client
Secret
Lack of Server Verification / DNS
Spoofing
Root Shell
Secure Boot is Disabled
Unlocked Bootloader
15
16
17
18
19
Area
Faicon/
Sparrow / Flex
Faicon/
‘Sparrow / Flex
‘Sparrow / Flex
Sparrow / Flex
‘Sparrow / Flex
‘Sparrow / Flex
Picard / Bravo
Picard / Bravo
Picard / Bravo
Picard / Bravo
Picard / Bravo
Picard / Bravo
Picard / Bravo
Multi-device
Q&A
Issue
Lack of Authentication: EDL/QDL
Mode
Lack of Authentication: Android
Debug Bridge
Improper Access Control: Android
Debug Bridge Sideload
Lack of Flash/eMMC Encryption
Use of an Unsupported and End-of-
Life Operating System
Sensitive Information Disclosed:
Development/Test Credential in
Production
Root Shell
Secure Boot is Disabled
Unlocked Bootloader
Lack of Authentication: EDL/QDL
Mode
Lack of Authentication: Android
Debug Bridge
Improper Access Control: Android
Debug Bridge Sideload
Lack of Flash/UFS Encryption
Unauthenticated Administrative API
Endpoints
#
29
30
31
32
33
35
37
38
39
40
41
42
Area
Multi-device
Multi-device
Media /
recordings
recordings
PhoneHome /
broadcast
Android app
suite
Media /
recordings
Android app
suite
system service
recordings
Android app
suite
Multi-device
Android visual
recognition
stack
Issue
Hidden Hardware Debug
Functionality: Hotspot
Wireless Remote Code Execution:
System
Incorrect Default Permissions:
Media Recordings Directories
Shared Media Library Allows Cross-
App Data Exposure
Wireless Remote Code Execution:
Shell
Unauthenticated Debug Broadcast
Clears Settings and Shuts Off
Device
Multiple Privileged System Apps
Shipped with Debugging Enabled
Lack of Per-File Encryption on
Sensitive Media
Sensitive Information Disclosed:
Hardcoded Auth0 Secret
Root Command Injection via Data
Log Cleanup Service
Excessive Sensitive Media Copies
Persist on Disk
Sensitive Information Disclosed:
Cleartext API Keys/Credentials
Wireless Remote Code Execution:
Root
ML/AI Local Model Accessible
47
Area
Android app
suite
Media /
recordings
Media /
recordings
Android app
Installer app
Public / app-
48 side
51
52
Public / app-
side
Public / app-
side
Public / app-
FS Installer /
Penguin
FRP
FRP
‘SpeedPourer /
FRP
Issue
Sensitive Information Disclosed:
Hardcoded Java Keystore and
Password
Data Recording Retention Relies
Solely on Disk Capacity
Records Stored on Unencrypted
External Partition
Sensitive Information Disclosed:
Datadog API Token
Cleartext Communications
Sensitive Information Disclosure:
Google API Key
Plaintext HTTP in Logs
Sensitive Information Disclosure:
API Keys
Remote Code Execution: System
FS Installer sensitive
artifact disclosure: Raven BLE
service URLs, field workflow logic
SpeedPourer/FRP cleartext
video/control fallback path
SpeedPourer/FRP config
permission/control issue
SpeedPourer/FRP reverse-
proxy/admin exposure
```
