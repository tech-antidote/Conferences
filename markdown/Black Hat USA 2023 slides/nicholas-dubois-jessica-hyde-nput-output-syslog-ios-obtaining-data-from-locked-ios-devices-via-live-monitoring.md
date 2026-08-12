---
title: "nput Output + Syslog (iO+S) Obtaining Data From Locked iOS Devices via Live Monitoring"
speakers: ["Nicholas Dubois", "Jessica Hyde"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/Nicholas Dubois & Jessica Hyde_nput Output + Syslog (iO+S) Obtaining Data From Locked iOS Devices via Live Monitoring.pdf"
pages: 69
sha256: "0e0cb036748eed0ee9a55e1813a991672533bcf6b3bfd447abe65f0ecdf3bded"
text_chars: 35057
ocr_pages: 24
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:22:08Z"
---
# nput Output + Syslog (iO+S) Obtaining Data From Locked iOS Devices via Live Monitoring

**Speakers:** Nicholas Dubois, Jessica Hyde  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Nicholas Dubois & Jessica Hyde_nput Output + Syslog (iO+S) Obtaining Data From Locked iOS Devices via Live Monitoring.pdf` (69 pages)


## Slide 1

###### **Input Output + Syslog (iO+S): Obtaining Data From Locked iOS Devices via Live Monitoring**

## Slide 2

**MEET NICK DIGITAL FORENSICS SPECIALIST & DEVELOPER, HEXORDIA**

**- Founder, Dragon Eye Intelligence**

**Previous:**

**- Forensics / Malware Research @ Univ. New Haven**

**- TikTok Research @ Penetrum**

**DFRWS National Cyber Crime Conference High Technology Crime Investigation Association**

## Slide 3

**MEET JESSICA FOUNDER & OWNER, HEXORDIA**

**- Adjunct Professor, George Mason University**

**Previous:**

**- Director Forensics, Magnet Forensics**

- **Basis Technology**

- **Ernst and Young**

- **American Systems**

**DFIR Review, Chair FSI: Digital Investigations, Associate Editor HTCIA IEC, 2nd VP SWGDE, Member OSAC, Member**

## Slide 4

# iOS Digital Forensics in 2023

## Slide 5

Exploit FFS Acquisition FFS Acquisition (Obtain Super User Permissions)

Passcode / Paired PC No Exploit (Average User Permissions) No Passcode / Paired PC

Logical Acquisition Limited Logical Acquisition

## Slide 6

#### **Full File System**

Vulnerable iOS Version
FFS
Sideload application
Passcode No FFS
exploit
iPhone 11 and above
Pre-boot Exploitation
No Passcode No FFS
(Checkm8)
Sideload application exploit /
Passcode FFS
Pre-boot Exploitation
iPhone X and below
Pre-boot Exploitation
No Passcode FFS
(Checkm8)

## Slide 7

#### **Logical Acquisition**

Trusted PC
Manually Browse Device,
Passcode iTunes Backup, Sysdiagnose
Logs
No Trusted PC
Manually Browse Device,
Trusted PC iTunes Backup, Sysdiagnose
Logs
No Passcode
Question Siri, Lock Screen
No Trusted PC
Widgets

## Slide 8

###### **Device States**

BFU AFU DFU
Diagnostics USB RM Trusted State

## Slide 9

###### BFU (Before First Unlock)

- The state after a device reboots but before it is unlocked for the first time

- Device is protected at a deeper level until it is unlocked for the first time

## Slide 10

###### AFU (After First Unlock)

- The state after a device reboots but before it is unlocked for the first time

• Device is less protected than in BFU mode

## Slide 11

###### Recovery

- A diagnostic mode typically used to recover from fatal booting errors

- E.g., Fix boot loops, restore / factory reset devices

## Slide 12

###### DFU (Device Firmware Upgrade)

- Low-level bootrom communication tool for developers and device configurations

- Looks like device is powered off

## Slide 13

###### Diagnostics

- Lesser-known mode used for diagnosing hardware issues

- Users will not see anything on this page however if the device is flagged for examination apple support may gather information and view it.

## Slide 14

Diagnostics

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Diagnostics
Serial Number:
G6TFL4LU0D87
oF Gl
Diagnostics a ies
MEID:
35052207479690
IMEI:
5 052207 479690 4
052207 494487 6
(Hy)
HEXORDIA
```

## Slide 15

###### Trusted State

- A state in which after a reboot, SOS mode, or inactive device state the device will refuse to communicate with other devices over USB

- Required for most logical acquisition data

## Slide 16

###### USB RM (USB Restricted Mode)

- A state in which after a reboot, SOS mode, or inactive device state the device will refuse to communicate with other devices over USB

- No bueno

## Slide 17

Data Sources

## Slide 18

|**Data Source**|**Can we obtain it?**|**Is it volatile?**|
|---|---|---|
|Data through touch UI
- As presented to a normal user, many hidden developer
features may be accessed through UI|Yes
-
Amount of data depends on if passcode is known|Somewhat|
|User Filesystem|Typically, yes|Somewhat|
|Full Filesystem (FFS)|Typically, with tooling yes
- Yet this may change quickly|Somewhat|
|Raw HDD Data|Too encrypted to understand = useless without decryption keys|Somewhat|
|Warrant Returns|Yes, if we have the authority|Yes|
|Call Detail Records (CDR)|Yes, if we have the authority|Yes|
|API Scraping|Yes|Yes|
|Random Access Memory (RAM)|Sort of…|Yes|
|Peripheral Data
- On-board devices such as microphone, camera|No, too volatile (With exceptions)|Extremely|
|Data through wired interface
- Live USB / Lightning Interface Data|Yes, but only in real-time (With exceptions)|Extremely|
|Data through wireless networks
- WiFi, Bluetooth, NFC, AirPlay, etc…|Yes, but only in real-time (With exceptions)|Extremely|

## Slide 19

Sysdiagnose Logs

## Slide 20

What are Sysdiagnose Logs?

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
What are Sysdiagnose Logs?
crashes_anc_s
summaries
(A)
HEXORDIA
```

## Slide 21

###### Capturing Sysdiagnose Logs

- For all iPhone / iPad devices: Hold Both Volume buttons for 1.5 seconds

- iPhone will vibrate

###### • iPad will not vibrate

## Slide 22

Capturing Sysdiagnose Logs

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Cupertino
4g°
2
Light rain for the
ext heur
Coenen
Calon Photos
Capturing Sysdiagnose Logs
Db Pra
Settings
2en Time
None
Reachahility
3D & Haptic Touch
orninada li
Lock Rotation
Undo
Lock Screen
Home Buttor
qT
ibration
‘B05 PM
49°
=
Lipnt rain tor the,
ext hour
‘wallet
H
HEXORDIA
```

## Slide 23

Capturing Sysdiagnose Logs

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Capturing Sysdiagnose Logs
iPhone:~ root# sysdiagnose —h
-h
“Vv
-f results_directory
-A archive_name
-V volume_path
-n
-k
-F
SE
-u
-Q
-b
-P
-P
9
==
-d
-D
-r
-R
[process_name | pid]
-C, --compression type
sysdiagnose version: 3.0 (1133.000000)
USAGE: sysdiagnose [-h] [-f results_directory] [-A archive_name] [-Q] [-b] [-p] [-d] [-X] [process_name | pid]
Display this help.
Enable verbose mode to display the container information as it executes.
Specify the directory where results will be stored.
Specify the name of the archive created in the results directory.
Specify the root volume for sysdiagnose to run on.
Do not tar the resulting sysdiagnose directory.
Do not remove the temporary directory.
Get feedback data.
Disable streaming to tarball.
Disable UI feedback.
Skip footprint.
Do not show a Finder window upon completion.
Collect only time-sensitive data; disregards previous -d or -r flags.
Do not collect time-sensitive data.
Collect only log Generation data; disregards previous -p or -r flags.
Do not run log generation data.
Collect only log data; disregards previous -p or -r flags.
Do not collect log data.
Collect only log archive; disregards previous -p or -d flags.
Do not collect log archive.
If a single process appears to be slowing down the system,
passing in the process name or ID as the argument gathers
additional process-specific diagnostic data; Specify only ONE process
at a time — specifying multiple processes is not supported.
Specify the compression type. It is an error to use this with the -n flag. Valid options are:
yaa: use parallel compression
tar: use tar compression
no-compression: don't compress the output. Identical to -n
default: will use the system default. Currently defaults to tar
iPhone:~ root# sysdiagnose
This tool generates files that allow Apple to investigate issues with your
computer and help improve Apple products. The files might contain personal
information found on your device or associated with your iCloud accounts,
including but not Limited to your name, serial numbers of your device,
your device name, your attached peripheral devices, your user name, your
email address and email settings, file paths, file names, Siri suggestions,
your computer's IP addresses, and network connection information.
This information is used by Apple in accordance with its privacy policy
(www. apple.com/privacy) and is not shared with any other company. By using
this tool and sending the results to Apple, you consent to Apple using the
contents of these files to improve Apple products.
Press 'Enter' to continue. Ctrl+\ to cancel.
Progress:
CEUTEEETETTTT TEED TTT ees EEE
Output available at '/private/var/mobile/Library/Logs/CrashReporter/DiagnosticLogs/
sysdiagnose/sysdiagnose_2023 . 08 .02_16-50-U1-0400_iPhone-OS_iPhone_20A392.tar.gz'.
(Hy)
HEXORDIA
```

## Slide 24

Capturing Sysdiagnose Logs

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Capturing Sysdiagnose Logs
DESCRIPTION:
sysdiagnose gathers system diagnostic information helpful in investigating system performance issues.
A great deal of information is harvested, spanning system state and configuration. The data is stored /var/tmp directory.
To cancel an in-flight sysdiagnose triggered via command line interface, press Ctrl-\.
sysdiagnose is automatically triggered when the following key chord is pressed: (Contxol-Option-Comand-Shift-Pariod)
WHAT sysdiagnose COLLECTS:
- A spindump of the system
- Several seconds of fs_usage ouput
- Several seconds of top output
- Data about kernel zones
- Status of loaded kernel extensions
- Resident memory usage of user processes
- Recent system Logs
- A System Profiler report
- Recent crash reports
- Disk usage information
- I/O Kit registry information
- Network status
- If a specific process is supplied as an argument, will collect:
- A list of malloc-allocated buffers in the process's heap
- Data about unreferenced malloc buffers in the process's memory
- Data about the virtual memory regions allocated in the process
(Hy)
HEXORDIA
```

## Slide 25

Capturing Sysdiagnose Logs

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Capturing Sysdiagnose Logs
S205 0000 ie ae
```

## Slide 26

Sysdiagnose Log Contents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Sysdiagnose Log Contents
iPhone:~ root# while true; do ps -A >> ps.txt; sleep 0.1; done
```

## Slide 27

###### Sysdiagnose Log Contents

|sysdiagnose|/usr/bin/hidutil dump|(srsupporttool)|
|---|---|---|
|/usr/libexec/sysdiagnose_helper|/usr/libexec/securityuploadd|/System/Library/PrivateFrameworks/SharedWebCredentials.framework/Sup|
|/usr/sbin/spindump -oslog -notarget 2 250 -noProcessingWhileSampling -
|/usr/sbin/ioreg-i-l-p IOService-w 0|port/swcutil show --verbose|
|noSymbolicate -file
/private/var/mobile/Library/Logs/CrashReporter/DiagnosticLogs/sysdiagnos
e/IN_PROGRESS_sysdiagnose_2023.08.02_21-01-23-0400_iPhone-
OS_iPhone_20A392.tmp/spindump/spindump-nosymbols.txt|/usr/sbin/ioreg-i-l-p IOACPIPlane-w 0
/usr/sbin/ioreg-i-l-p IOPower-w 0
/usr/sbin/ioreg-i-l-p IODeviceTree-w 0|/usr/bin/fileproviderctl dump --limit-dump-size -o
/private/var/mobile/Library/Logs/CrashReporter/DiagnosticLogs/sysdiagnos
e/IN_PROGRESS_sysdiagnose_2023.08.03_13-51-24-0400_iPhone-
OS_iPhone_20A392.tmp/task_unnamed_sysdiagnose_temp.iOQyQe/filepro|
|/bin/ps axwww -o|/usr/sbin/ioreg-i-l-p IOUSB-w 0
|viderctl_dump.log|
|user,uid,prsna,pid,ppid,flags,%cpu,%mem,pri,ni,vsz,rss,wchan,tt,stat,start,ti|/usr/sbin/ioreg-i-l-p IOFireWire-w 0|/usr/bin/brctl diagnose --sysdiagnose|
|me,command|/usr/sbin/ioreg-i-l-p IOPort-w 0|
/private/var/mobile/Library/Logs/CrashReporter/Cloud/clouddocs_2023.08.|
|/usr/bin/taskinfo --threads --boosts|/usr/sbin/ioreg-a-w0-x 0|03_13-51-40-0400|
|/usr/bin/vm_stat -c 25 0.2
|/System/Library/PrivateFrameworks/CoreSuggestions.framework/Tools/sugg
est_tool dbStats|/usr/bin/brctl diagnose -c --sysdiagnose
/private/var/mobile/Library/Logs/CrashReporter/Cloud/clouddocs_2023.08.|
|/sbin/mount|/System/Library/PrivateFrameworks/CoreSuggestions.framework/Tools/sugg|03_13-51-40-0400|
|/bin/df -H|est_tool filesystemMetadata|/usr/bin/brctl dump -i|
|/usr/bin/kbdebug
/usr/bin/zprint -t -w|/System/Library/PrivateFrameworks/CoreSuggestions.framework/Tools/sugg
est_tool dbSchema|/System/Library/PrivateFrameworks/ABMHelper.framework/Support/abm-
helper|
|/usr/libexec/smcDiagnose|/System/Library/PrivateFrameworks/CoreSuggestions.framework/Tools/sugg
est_tool assetVersion|/System/Library/PrivateFrameworks/DataMigration.framework/XPCServices/
com.apple.datamigrator.xpc/com.apple.datamigrator|
|/usr/local/bin/powermetrics -i 1000 --sample-count 10 --show-all --show-
initial-usage --handle-invalid-values|/System/Library/PrivateFrameworks/CoreSuggestions.framework/Tools/sugges
t_tool RTCGetDictionaryExtractions|/usr/libexec/seputil --daemonize-update-timer|
|/usr/libexec/remotectl dumpstate
/usr/bin/tbtdiagnose
/usr/bin/hpmdiagnose|/System/Library/PrivateFrameworks/CoreSuggestions.framework/Tools/sugg
est_tool RTCGetDictionaryInteractions
/System/Library/PrivateFrameworks/CoreSuggestions.framework/Tools/sugg
est_tool RTCGetDictionaryInteractionsSummary||
|/usr/bin/lsdiagnose|/usr/libexec/corebrightnessdiag nightshift-internal||
|/usr/sbin/kextstat|/usr/sbin/ckksctl status --json||
|/usr/local/bin/spuctl --sysdiagnose|
/usr/sbin/otctl status --json||
|/usr/libexec/pcsstatus --json capture output|/System/Library/PrivateFrameworks/ZhuGeSupport.framework/XPCServices/||
|/usr/bin/codecctl -c 1 -a|ZhuGeService.xpc/ZhuGeService||
|/usr/libexec/security-sysdiagnose|/usr/bin/powerlogHelperd||

## Slide 28

Parsing Sysdiagnose – Hexordia iO+S Toolkit

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Parsing Sysdiagnose - Hexordia 10O+S Toolkit
e5b005bc91! d Of then attempt to
(A)
HEXORDIA
```

## Slide 29

### Sysdiagnose from Locked USB RM Devices?

## Slide 30

Syslogs

## Slide 31

###### What are Syslogs?

- Realtime Log

• Trust Required

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
What are Syslogs?
* Realtime Log
* Trust Required
Jul 25 14:23:01 suggestd(ProactiveHarvesting)[138] <Notice>: HVQueues: enqueueContent: <private>
Jul 25 14:23:01 suggestd(ProactiveHarvesting)[138] <Notice>: HVQueue<MailContent>: enqueueContent: writing to disk
Jul 25 14:23:01 suggestd(CoreSuggestionsInternals)[138] <Notice>: Decoded 16 of 16 items received from com.apple.mobilemail.
Jul 25 14:23:01 SpringBoard(Posterkit)[32] <Notice>: Significant event timer fired for <LegacyPoster: 9x21d8ed8c8; 63DBDFOFOFAB>
Jul 25 14:23:01 SpringBoard(PaperBoardUI)[32] <Notice>: [lock] Poster Extact update changed 131
Jul 25 14:23:01 SpringBoard(PaperBoardUI)[32] <Notice>: [home] Poster Extact update changed 131
Jul 25 14:23:01 SpringBoard(FrontBoard)[32] <Notice>: [@x2810270c0:Posterkit : 45A705BC-8E9D-4DDB-A38E-63DBDFOF8FAB] Scene activity mode did change: support
(transient).
Jul 25 14:23:01 SpringBoard(FrontBoard)[32] <Notice>: [0x2810270c0:Posterkit :45A705BC-8E9D-4DDB-A39E-63DBDFOFOFAB] Scene assertion state did change: Foreg
roundNonFocal.
Jul 25 14:23:01 SpringBoard(FrontBoard)[32] <Notice>: [xpcservice<com.apple.PaperBoard.LegacyPoster([osservice<com.apple.SpringBoard>:32])>:192] Workspace
assertion state did change: ForegroundNonFocal (acquireAssertion = YES).
Jul 25 14:23:01 coreduetd(CoreDuet)[129] <Notice>: CDInteractionCache: New recorded interactions
Jul 25 14:23:01 coreduetd(CoreDuet)[129] <Notice>: CDInteractionCache: New recorded interactions
Jul 25 14:23:01 runningboardd(RunningBoard)[31] <Notice>: Acquiring assertion targeting [xpcservice<com.apple.PaperBoard.LegacyPoster([osservice<com.apple
. SpringBoard>:32])>:192] from originator [osservice<com.apple.SpringBoard>:32] with description <RBSAssertionDescriptor| "FBWorkspace (ForegroundNonFocal)
" ID:31-32-545 target:192 attributes:[
<RBSDomainAttribute| domain:"com.apple.frontboard" name: "Workspace-ForegroundActive" sourceEnvironment:"(null)">,
<RBSAcquisitionCompletionAttribute| policy:AfterApplication>,
<RBSDomainAttribute| domain:"com.apple.frontboard" name:"Visibility" sourceEnvironment:"(null)">
1> L<
(Hy
HEXORDIA
```

## Slide 32

###### Capturing Syslogs - Libimobiledevice

- Official Source Code: https://github.com/libimobiledevice/libimobiledevice

- Precompiled Windows Binaries: https://github.com/iFred09/libimobiledevice-windows

## Slide 33

# Capture & Parse Syslog IO+S Toolkit

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
7 Capture & Parse Syslog ‘
LH lIO+S Toolkit
```

## Slide 34

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Application Log < Clear Logs @@ YouTube ? Help
0S Monitor Syslog Oj 1 Analysi Ng \ alysis | CS
System Log Control Panel
>
Start Moni
```

## Slide 35

## USB Endpoints

## Slide 36

#### **USB Endpoints**

iPhone X

iOS 16.0.3 (20A392)

## Slide 37

USB Endpoints (Normal Device State)

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
USB Endpoints (Normal Device State
INTERFACE 1: Audio
INTERFACE 0: Image
iConfiguration : 0x7 PTP + Apple Mobile Device binterval x0 bDescriptorlype : Ox4 Interface bLength 0x7 (7 bytes)
bLength 0x9 (9 bytes) blength 0x9 (9 bytes) bmattributes Oxc0 Self Powered ENDPOINT 0x85: Bulk IN binterfaceNumber : Oxi bDescriptorType : 0x5 Endpoint
bDescriptorType 0x4 Interface bDescriptorType 0x4 Interface bMaxPower Oxfa (500 mA) bLength 0x7 (7 bytes) bAlternateSetting 0x0 bEndpointAddress : OxS OUT
binterfaceNumber : 0x0 binterfaceNumber : Ox1 INTERFACE 0: Image bDescriptorType : 0x5 Endpoint bNumEndpoints : 0x2 bmAttributes 0x2 Bulk
bAlternateSetting : 0x0 bAlternateSatting : 0x0 bLength 0x9 (9 bytes) bEndpointAddress : Ox85 IN binterfaceClass : Oxff Vendor Specific wMaxPacketSize ; 0x200 (512 bytes)
bNumEndpoints —: 0x3 bNumEndpoints : 0x0 bDescriptorType : 0x4 Interface bmAttributes : 0x2 Bulk binterfaceSubClass : Oxfe binterval 0x0
binterfaceClass : 0x6 Image binterfaceClass : 0x1 Audio binterfaceNumber : Ox0 wMaxPacketSize : 0x200 (512 bytes) binterfaceProtocol : 0x2 INTERFACE 2, 2: Vendor Specific =
binterfaceSubClass : 0x1 binterfaceSubClass : Ox2 bAlternateSetting : 0x0 binterval : 0x0 interface Oxf Apple USB Multiplexor bLength (0x9 (9 bytes)
binterfaceProtocol : 0x1 binterfaceProtocol : Ox0 bNumEndpoints : 0x3 CONFIGURATION 4: 500 mA ENDPOINT 0x4: Bulk OUT bDescriptortype : 0x4 Interface
ilnterface + Oxe PTP ilnterface : 0x0 binterfaceClass Ox6 Image bLength : 0x9 (9 bytes) bLength 0x7 (7 bytes) binterfaceNumber : 0x2
ENDPOINT 0x2: Bulk OUT = INTERFACE 1, 1: Audio binterfaceSubClass : Oxi bDescriptorType : 0x2 Configuration bDescriptorType : 0x5 Endpoint bAlternateSetting : 0x2
bLength 0x7 (7 bytes) blength x3 (9 bytes) binterfaceProtocol : 0x1 wTotalLength 0x75 (117 bytes) bEndpointAddress : x4 OUT bNumEndpoints : 0x2
bDescriptorType : 0x5 Endpoint bDescriptorType : Oxd Interface iinterface Oxe PTP bNuminterfaces 0x3 bmattributes : 0x2 Bulk binterfaceClass : Oxff Vendor Specific
bEndpointAddress : 0x2 OUT binterfaceNumber : Ox1 ENDPOINT Ox2: Bulk OUT bConfigurationValue : Ox4 wMaxPacketSize : 0x200 (512 bytes) binterfaceSubClass : Oxfd
bmAttributes : 0x2 Bulk bAlternateSetting : Ox1 bLength x7 (7 bytes) iConfiguration 0x8 PTP + Apple Mobile Device + Apple USB Ethernet interval 0x0 binterfaceProtocol: 0x1
wMaxPacketSize : 0x200 (512 bytes) bNumEndpoints : Ox1 bDescriptorType : Ox5 Endpoint bmAttributes OxcO Self Powered ENDPOINT 0x85: Bulk IN =: interface Ox11 AppleUSBEthernet
binterval 0x0 binterfaceClass : Ox1 Audio bEndpointAddress : 0x2 OUT bMaxPower : Oxfa (500 mA) blength 0x7 (7 bytes) ENDPOINT 0x86: Bulk IN
ENDPOINT 0x81: Bulk IN binterfaceSubClass : Ox2 bmAttributes : 0x2 Bulk INTERFACE 0: Image bDescriptorType : 0x5 Endpoint bLength 0x7 (7 bytes)
bLength 0x7 (7 bytes) binterfaceProtocol : 0x0 wMaxPacketSize : 0x200 (512 bytes) bLength 0x3 (9 bytes) bEndpointAddress ; Ox85 IN bDescriptorType : 0x5 Endpoint
bDescriptorType : 0x5 Endpoint linterface Oxo binterval Oxo bDescriptorType : Oxd Interface bmAttributes : 0x2 Bulk bEndpointAddress : Ox86 IN
bEndpointAddress : 0x81 IN ENDPOINT 0x81: Isochronous IN ENDPOINT 0x81: Bulk IN binterfaceNumber : 0x0 wMaxPacketSize : 0x200 (512 bytes) bméttributes Ox2 Bulk
bmAttributes : 0x2 Bulk bLength 0x9 (7 bytes) bLength 0x7 (7 bytes) bAlternateSetting : 0x0 binterval 0x0 wMaxPacketSize : 0x200 (512 bytes)
wMaxPacketSize : 0x200 (512 bytes) bDescriptorType : OxS Endpoint bDescriptorType : 0x5 Endpoint bNumEndpoints. Ox3 INTERFACE 2: Vendor Specific binterval Oxo
binterval 0x0 bEndpointAddress : 0x81 IN bEndpointAddress : 0x81 IN binterfaceClass Ox6 Image bLength 0x9 (9 bytes) ENDPOINT 0x5: Bulk OUT
ENDPOINT 0x83: Interrupt IN bmattributes : x1 Isochronous bmAttributes : 0x2 Bulk binterfaceSubClass: Ox1 bDescriptorType : Ox4 Interface bLength 0x7 (7 bytes)
bLength 0x7 (7 bytes) wMaxPacketSize : OxcO (192 bytes) wMaxPacketSize : 0x200 (512 bytes) binterfaceProtocol: 0x1 binterfaceNumber : Ox2 bDescriptorType : 0x5 Endpoint
bDescriptorType : 0x5 Endpoint binterval 0x4 binterval 0x0 interface: Oxe PTP bAlternateSetting : 0x0 bEndpointAddress :_ 0x5 OUT
bEndpointAddress : 0x83 IN INTERFACE 2: Human Interface Device = ENDPOINT 0x83: Interrupt IN ENDPOINT 0x2: Bulk OU bNumEndpoints  : 0x0 bmAttributes : 0x2 Bulk
bmAttributes : 0x3 Interrupt blength 0x9 (9 bytes) blength 0x7 (7 bytes) bLength 0x7 (7 bytes) binterfaceClass : Oxff Vendor Specific wMaxPacketSize : 0x200 (512 bytes)
wMaxPacketSize : 0x40 (64 bytes) bDescriptorType x4 Interface bDescriptorType : Ox5 Endpoint bDescriptorType : OxS Endpoint binterfaceSubClass : Oxfd binterval x0
binterval Oxa binterfaceNumber : 0x2 bEndpointAddress : 0x83 IN bEndpointAddress : 0x2 OUT binterfaceProtocol : 0x1
CONFIGURATION 2: 500 mA bAlternateSetting : x0 bmAttributes 0x3 Interrupt bmAttributes x2 Bulk interface 0x11 AppleUSBEthernet
bLength 0x9 (9 bytes) bNumEndpoints =: Oxi wMaxPacketSize : 0x40 (64 bytes) wMaxPacketSize : 0x200 (512 bytes) INTERFACE 2, 1: Vendor Specifi
bDescriptorType : 0x2 Configuration binterfaceClass : 0x3 Human Interface Device binterval Ova binterval 0x0 blength 0x9 (9 bytes)
wTotalLength 0x95 (149 bytes) binterfaceSubClass : 0x0 INTERFACE 1: Vendor Specific ENDPOINT 0x81: Bulk IN = bDescriptorType : 0x4 Interface
bNuminterfaces 0x3 binterfaceProtocol: Ox0 bLength 0x9 (9 bytes) bLength 0x7 (7 bytes) binterfaceNumber : 0x2
bConfigurationValue : Ox2 ilnterface > Ox0 bDescriptorType 0x4 Interface bDescriptorType : Ox5 Endpoint bAlternateSetting : Ox1
iConfiguration : 0x6 iPod USB Interface ENDPOINT 0x83: Interrupt IN binterfaceNumber : 0x1 bEndpointAddress : 0x81 IN bNumEndpoints : 0x2
bmAttributes Oxc0 Self Powered blength x7 (7 bytes) bAlternateSetting : 0x0 bmAttributes : 0x2 Bulk binterfaceClass : Oxff Vendor Specific
bMaxPower : Oxfa (500 mA) bDescriptorType : OxS Endpoint bNumEndpoints : 0x2 wMaxPacketSize : 0x200 (512 bytes) binterfaceSubClass : Oxfd
INTERFACE 0: Audio bEndpointAddress : 0x83 IN binterfaceClass : Oxff Vendor Specific binterval 0x0 binterfaceProtocol : 0x1
blength 0x9 (9 bytes) bmAttributes : 0x3 Interrupt binterfaceSubClass : Oxfe ENDPOINT 0x83: Interrupt IN interface 0x11 AppleUSBEthernet
bDescriptorType : Oxé Interface wMaxPacketSize : 0x40 (64 bytes) binterfaceProtocol: 0x2 bLength x7 (7 bytes) ENDPOINT 0x86: Bulk IN
binterfaceNumber : 0x0 binterval Oxi ilnterface Oxf Apple USB Multiplexor bDescriptorType : Ox5 Endpoint bLength 0x7 (7 bytes)
bAlternateSetting : 0x0 CONFIGURATION 3: 500 mi ENDPOINT 0x4: Bulk OUT bEndpointAddress : 0x83 IN bDescriptorType : 0x5 Endpoint
bNumEndpoints : 0x0 bLength Ox9 (9 bytes) bLength 0x7 (7 bytes) bmAttributes 0x3 Interrupt bEndpointAddress : 0x86 IN
binterfaceClass 0x1 Audio bDescriptorType 0x2 Configuration bDescriptorType : Ox Endpoint wMaxPacketSize : 0x40 (64 bytes) bmAttributes : 0x2 Bulk
binterfaceSubClass: Ox1 wTotallength Ox3e (62 bytes) bEndpointAddress : 0x4 OUT binterval Oxa wMaxPacketSize : 0x200 (512 bytes)
binterfaceProtocol: 0x0 bNuminterfaces Ox2 bmAttributes 0x2 Bulk INTERFACE 1: Vendor Specific binterval 0x0
ilnterface Oxo bConfigurationValue : 0x3 wMaxPacketSize : 0x200 (512 bytes) bLength 0x9 (9 bytes)
ENDPOINT Ox5: Bulk OUT
HEXORDIA
```

## Slide 38

USB Endpoints (Recovery Mode)

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Configuration Value: 1
Interface Number: 0,Alternate Setting: 0
Endpoint Address: 4
Interface Number: 1,Alternate Setting: 0
Interface Number: 1,Alternate Setting: 1
Endpoint Address: 129
Endpoint Address: 2
DEVICE ID 05ac:1281 on Bus 001 Address 003
bLength : 0x12 (18 bytes)
bDescriptorType 0x1 Device
bedUSB : 0x200 USB 2.0
bDeviceClass : 0x0 Specified at interface
bDeviceSubClass : 0x0
bDeviceProtocol : 0x0
bMaxPacketSizeO : 0x40 (64 bytes)
idVendor : Ox05ac
idProduct 0x1281
bedDevice 0x0 Device 0.0
iManufacturer Ox2 Apple Inc.
iProduct : 0x3 Apple Mobile Device (Recovery Mode)
iSerialNumber : 0x4 SDOM:01 CPID:8015 CPRV:11 CPFM:03 SCEP:01
BDID:0E ECID:000C2C680044E02E IBFL:3D SRNM:[FK1WT6BPJCLH]
bNumConfigurations Ox1
CONFIGURATION 1: 500 mA =
bLength : Ox9 (9 bytes)
bDescriptorType : 0x2 Configuration
wTotalLength : 0x39 (57 bytes)
bNuminterfaces =: 0x2
bConfigurationValue : Ox1
iConfiguration : 0x5 Apple Mobile Device (Recovery Mode)
bmAttributes : 0x80 Bus Powered
bMaxPower : Oxfa (500 mA)
INTERFACE 0: Application Specific
bLength : Ox9 (9 bytes)
bDescriptorType 0x4 Interface
binterfaceNumber : 0x0
bAlternateSetting : 0x0
bNumEndpoints Ox1
binterfaceClass Oxfe Application Specific
binterfaceSubCl: Oxi
binterfaceProtocol Ox2
ilnterface : 0x0
USB Endpoints (Recover
ENDPOINT 0x4: Bulk OUT
bLength : 0x7 (7 bytes)
bDescriptorType : Ox5 Endpoint
bEndpointAddress: 0x4 OUT
bmAttributes : Ox2 Bulk
wMaxPacketSize : 0x200 (512 bytes)
binterval : 0x0
INTERFACE 1: Vendor Specific =:
bLength 0x9 (9 bytes)
bDescriptorType Ox4 Interface
binterfaceNumber : Ox1
bAlternateSetting : 0:
bNumEndpoints : Ox0
binterfaceClass : Oxff Vendor Specific
binterfaceSubClass : Oxff
binterfaceProtocol : 0x51
ilnterface : Ox0
INTERFACE 1, 1: Vendor Specifi
bLength : 0x9 (9 bytes)
bDescriptorType : 0x4 Interface
binterfaceNumber : Ox1
bAlternateSetting : Ox1
bNumEndpoints : Ox2
binterfaceClass : Oxff Vendor Specific
binterfaceSubClass : Oxf
binterfaceProtocol : 0x51
ilnterface : 0x6 Apple USB Serial Interface
ENDPOINT 0x81: Bulk IN =
bLength : 0x7 (7 bytes)
bDescriptorType : 0x5 Endpoint
bEndpointAddress : 0x81 IN
bmAttributes : 0x2 Bulk
wMawPacketSize : 0x200 (512 bytes)
binterval : 0x0
ENDPOINT 0x2: Bulk OUT
bLength : 0x7 (7 bytes)
bDescriptorType : Ox5 Endpoint
bEndpointAddress: 0x2 OUT
bmAttributes : Ox2 Bulk
wMaxPacketSize : 0x200 (512 bytes)
binterval : 0x0
y Mode
(Hy)
HEXORDIA
```

## Slide 39

###### USB Endpoints (DFU Mode)

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
USB Endpoints (DFU Mode
Configuration Value: 1
Interface Number: 0,Alternate Setting:
DEVICE ID 0Sac:1227 on Bus 001 Address 009
bLength : 0x12 (18 bytes)
bDescriptorType 0x1 Device
bedUSB : 0x200 USB 2.0
bDeviceClass 0x0 Specified at interface
bDeviceSubClass : 0x0
bDeviceProtocol : Ox0
bMaxPacketSizeO : 0x40 (64 bytes)
idVendor : Ox05ac
idProduct :0x1227
bedDevice : 0x0 Device 0.0
iManufacturer : 0x2 Apple Inc.
iProduct : 0x3 Apple Mobile Device (DFU Mode)
iSerialNumber : 0x4 CPID:8015 CPRV:11 CPFM:03 SCEP:01
BDID:0E ECID:000C2C680044E02E IBFL:3C SRTG:[iBoot-3332.0.0.1.23]
bNumConfigurations : 0x1
CONFIGURATION 1: 500 mA
bLength : Ox9 (9 bytes)
bDescriptorType : Ox2 Configuration
wTotalLength : 0x19 (25 bytes)
bNuminterfaces =: Ox1
bConfigurationValue : Ox1
iConfiguration : OxS Apple Mobile Device (DFU Mode)
bmAttributes : 0x80 Bus Powered
bMaxPower : Oxfa (500 mA)
INTERFACE 0: Application Specific
bLength : Ox9 (9 bytes)
bDescriptorType : Ox4 Interface
binterfaceNumber : Ox0
bAlternateSetting : Ox0
bNumEndpoints : Ox0
binterfaceClass : Oxfe Application Specific
binterfaceSubClass: Ox1
binterfaceProtocol: 0x0
ilnterface 0x0 (Hy
HEXORDIA
```

## Slide 40

###### USB Endpoints (Diagnostics Mode)

The same endpoints as Normal Device State; endpoints do not work the same

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
USB Endpoints (Diagnostics Mode)
(Sel?)
MD)
Diagnostics
The same endpoints as Normal Device
State; endpoints do not work the same
```

## Slide 41

usbmuxd & SSL

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
usbmuxd & SSL
N" “http apple. com/DT!
aa 2 4 Adisa oa
DTD PLIST 1. N" “http
4Ad07a7 7 8 2B
5 AdpU BB BB B Spite a aim
N" “http: apple.com/DTDs/PropertyList-1.0.dtd
>
(H
HEXORDIA
```

## Slide 42

###### Some Programs…

If SSL Make Query
Program SSL
If no SSL Exit(1)
If SSL Goto(Q:)
SSL
Program If no SSL Exit(1)
Q: Make Query

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Some Programs...
Make Query
Exit(1)
Goto(Q:)
If SSL
Program -——> SSL <
If no SSL
If SSL
SSL <
Program < If no SSL
Q: Make Query
Exit(1)
HEXORDIA
```

## Slide 43

###### **Working with USB Endpoints**

1. Capture and Examine Raw USB Traffic

2. Send Custom Raw HID / USB Packets

## Slide 44

###### Capturing USB Traffic

https://desowin.org/usbpcap/

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Capturing USB Traffic
https://desowin.org/usbpcap/
B) USBPcapCMD.exe
```

## Slide 45

Capturing USB Traffic

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Capturing USB Traffic
C:\Program Files\USBPcap\USBPcapCMD.exe
Device Information Service
Bluetooth LE Generic Attribute Service
Bluetooth Low Energy GATT compliant HID device
2 \\.\USBPcap2
\?? \USBHROOT HUB30#5&26T6777&0808{F18a0688 - c30c-11d8-8815-eeaacIe6beds}
[Port 2] Apple Mobile Device USB Composite Device
Apple Mobile Device USB Device
Apple iPhone
Select filter to monitor (q to quit): 2
Output file name (.pcap): Output,
(Hy)
HEXORDIA
```

## Slide 46

Identifying iOS USB Traffic

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Identifying 1OS USB Traffic
<!DOCTYPE plist PUBLTC “-//Annle//DTN PITST 1.@//FN" “httn: //unmw annle_com/NDTNs/Pronertvl ist-1_8,dtd">
<plist version="1.0 :
<dict> ¥ plist
<key>Key</key>
<string>ProductVersion</string>
<key>ProtocolVersion</key>
<string>2</string>
<key>Request</key>
<string>GetValue</string>
</dict>
</plist>
£SAd-da ja,
BG<?xml version="1. encoding="UTF- >
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" “http: //ww.apple.com/DTDs/PropertyList-1.
<plist version="1.8">
<dict>
<key>Key</key>
<string>ProductVersion</string>
<key>Request</key>
<string>GetValue</string>
<key>Value</key>
<string>16.0.3</string>
</dict>
</plist>
£SAdeeH E
(A)
HEXORDIA
```

## Slide 47

###### Identifying iOS USB Traffic

- No data sent in USB RM

- Tokens and Certificates seen while in locked and unlocked state

- Setup Phase and Deactivated devices are automatically trusted

Contents will vary depending on:

- Device Boot State (Normal, DFU, Etc…)

- Device Lock State (BFU, AFU)

- Trust or No Trust

- PC Software

## Slide 48

USB RM Ruins it

## Slide 49

###### Pairing Records

Windows: C:\ProgramData\Apple\Lockdown MacOS: /var/db/lockdown

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Pairing Records
Windows: C:\ProgramData\Apple\Lockdown
MacOS: /var/db/lockdown
> ThisPC > Win } » ProgramData > Apple » Loc
Date modified
(A)
HEXORDIA
```

## Slide 50

###### USB RM Bypass… Kinda

A device in Diagnostics Mode has no USB RM:

- Device endpoints are limited however most identifiers can be recovered

- Lockdownd will not establish a complete connection as the device is in a “passcode protected” state

- May send custom commands which can work in a passcode protected state

## Slide 51

USB RM Bypass… Kinda

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
USB RM Bypass... Kinda
aS OHPANULINULIDC 2h TEN OINU LEAS 3]5 Tx] a 4° OHMDCZIESCIENOINUL EIB SS 0H)
Sa TAN LID C LER 3) ti on TRS GT  - EBE
WULTFRINULINULINULINULINU LINULINULINU LES EN OUT L) IST
[SUB BEENOINULEAS OH)B Sia
41CFE4C Wuhan
§40-4C04
(A)
HEXORDIA
```

## Slide 52

Parsing USB Traffic – Hexordia iO+S Toolkit

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Parsing USB Traffic - Hexordia iO+S Toolkit
nalysis Y USB Analysis | 4 API Analysis @ Application Log < Clear Logs @@ YouTube ? Help
USBLog = Analysi Control Panel
Start Monitor Stop Monitor
sion="1,0" e = $ f {DTD PLIST 1.0//EN"
{Pr t-1
‘{DTD PLIS
(A)
HEXORDIA
```

## Slide 53

Query Recovery Mode

## Slide 54

###### **idevicerecovery - getenv**

|**Command**|**Example**|
|---|---|
|**getenv build-version**|iBoot-6723.80.19|
|**getenvauto-boot**|true|
|**getenvbootdelay**|0|
|**getenvbacklight-level**|1505|
|**getenvboot-command**|fsboot|
|**getenv image-version**|0x4|
|**getenvsecure-boot**|0x1|
|**getenv ?**|0x0|
|**getenvboot-partition**|0|
|**getenv boot-path**|/System/Library/Caches/com.apple.kernelcaches/kernelcache|
|**getenvdt-path**|/usr/standalone/firmware/devicetree.img4|
|**getenvbuild-style**|RELEASE|
|**getenvconfig_board**|d201|
|**getenvboard-rev**|0xf|
|**getenv loadaddr**|0x801000000|
|**getenv ramdisk-size**|0x20000000|
|**getenv idle-off**|true|
|**getenvboot-device**|nvme_nand0|
|**getenvdisplay-color-space**|ARGB8101010|
|**getenv fm-activation-locked**||
|**getenv restore-outcome**||
|**getenv fm-account-masked**|do********@ic****.***|
|**getenv fm-spstatus**||
|**getenvobliteration**|handle_message: ObliterationComplete|
|**getenv backlight-nits**|0x00ac7a3f|
|**getenv usbcfwflasherResult**|No errors|
|**getenv fm-spkeys**
**nonce-seeds**||

## Slide 55

Fuzzing Recovery Mode

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Fuzzing Recovery Mode
1 import os
2 import subprocess
3 import time
4 import signal
5
6 os.chdir("C:/Users/nickd/Desktop/Reverse Engineering Syslog/Raw Data/libimobiledevice_32")
7
8  £ = open("C:/Users/nickd/Desktop/fuzzme.txt", “r", encoding="utf8", errors="ignore”)
9 out = open("C:/Users/nickd/Desktop/getrecovery.txt",
10  out2 = open("C:/Users/nickd/Desktop/runrecovery.txt",
11 Lines = f.read().splitlines()
12. #subprocess.Popen("irecovery.exe -c & ping -n 3@ 127.0.0.1 &', shell=False, stderr=f, stdout=f)
13. #time.sleep(10)
14
cr ao
16 set = @
17 run = @
18
19 if(get==1):
20 for line in Lines:
21 str="/c echo getenv ' + line +‘ | irecovery.exe -s"
22 out.write("\n\n")
3 out.flush()
24 print(str)
25 proc = subprocess.Popen([“cmd",str], stderr=out, stdout=out)
26 time. sleep(0.4)
27 try:
28 os.kill(proc.pid, signal.SIGINT)
29 except: pass
31 if(set==1):
3: for line in Lines:
55} str='/c echo setenv ' + line + ' false | irecovery.exe -s'
3. out.write("\n\n")
35 out.flush()
36 print(str)
37 proc = subprocess.Popen([“cmd",str], stderr=out, stdout=out)
38 time.sleep(@.2)
39 try:
40 os.kill(proc.pid, signal.SIGINT)
41 except: pass
42 str="/c echo saveenv’ + ' | irecovery.exe -s'
3 proc = subprocess.Popen(["cmd", str], stderr=out, stdout=out)
44 os.kill(proc.pid, signal.SIGINT)
45
46 if(run==1):
47 for line in Lines:
48 str="/c echo " + line + " | irecovery.exe -s*
49 out2.write("\n\n")
) out2.flush()
51 print(str) (Hy
52 proc = subprocess.Popen(["cmd",str], stderr=out2,stdout=out2)
53 time.sleep(@.2) WV
54 try:
55 os.kill(proc.pid, signal.SIGINT)
56 except: pass HEXORDIA
```

## Slide 56

What Can we Recover From Locked Devices?

## Slide 57

###### Paired Locked Device

###### Sysdiagnose Logs Live Syslogs iTunes Backups Siri

Lockscreen Widgets & Info RAW USB Traffic Data Recovery Mode Data DFU Mode Data

Diagnostics Mode Data

## Slide 58

###### Unpaired Locked Device

###### Siri

Lockscreen Widgets & Info RAW USB Traffic Data

Recovery Mode Data DFU Mode Data

Diagnostics Mode Data Remote Sysdiagnose Logs

## Slide 59

# Case Study

iPhone 12 Pro USB RM, Untrusted, AFU iOS 16.2

## Slide 60

###### APIs

• iTunes Account Email Address • First and Last Name

• Additional Generic iTunes Account Info

###### Recovery Mode

- Device Model

- Unique Device Identifier, Current IMEI & Generic Device Info

- • Partial iCloud Email Address • Device is iCloud Locked

## Slide 61

###### Diagnostics Mode

- Serial No.

- • MEID

- IMEI

- Unique Device Identifier, WiFi MAC, Additional Hardware Info.

- • iOS Version

- Baseband Info.

- Names of Photos

- Photo Metadata (Datetime & Location)

## Slide 62

###### Sysdiagnose Log – Device Info

• Device Name, iOS Version + OS Info., UUID, • Languages, Timezones, Keyboards • Power on Times, Application Run Times, Screenshot Taken Times • Connected USB Devices, Device Trust Datetime Logs, Bat. %, Device Orientation, Charging, Screen Status, Brightness, Motion Sysdiagnose Log – Application Info

- Installed Applications, Application Versions,Appliaction permissions

- • Currently Running Applications / Processes, Application Run Times

## Slide 63

###### Sysdiagnose Log – WiFi & Bluetooth

• HW MAC Address, Private MACs

• Connected SSID, BSSID, Country Code, IP Address, Router IP Address, DNS • WiFi Scaned Networks, First Joined Times, Last Joined Times • Paired / Connected Bluetooth Devices

- Networks lat., long. location

• External IP Addresses & Domains Sysdiagnose Log – User & Cloud Info

- Full Name

• iCloud Email, Unique Username Identifiers • Cloud Sync Timestamps, API Keys, Keychain Info., Cloud Container Info.

## Slide 64

###### Sysdiagnose Log – “Logs”

- Transparency, Consent, and Control (TCC) Database, Device Settings and Preferences

- • Powerlog

- Application Usage Logs, Application Battery Consumption

- • Mobile Installation Logs (Installation Logs Including Deleted Apps) • Calandar Email Addr. & Contents

- Installed Device Profiles, Profile Configuration

- • Mobile Activation Logs

- Lockdownd Logs

- Update, User, & Restore Logs

- SiriAnalytics (Siri Activation Times)

## Slide 65

###### Sysdiagnose Log – logarchive

- A LOT of Hardware info

- Full Name, Email Addresses, Mail Tokens, Account Phone Number

- • Safari History

- Installed Applications

- Paired / Connected Bluetooth Devices, BLE Scans

- • Device Orientation, Maps Locations, Location (Long./Lat.) • AirDrop Logs + Phone Numbers/Email

- AirTag Logs (#Durian)

- Contact Information (Names + Email + Phone Number)

## Slide 66

###### Key Takeaways For Researchers

Use FFS to
Find More  Diagnostics
Find
Endpoints Mode
Endpoints

## Slide 67

###### Future Work

Examine Fuzzing recovery Fuzzing DFU diagnostics commands Mode More mode API more

## Slide 68

Summary

## Slide 69

##### **QUESTIONS?**

Nicholas Dubois @noot4n6

Jessica Hyde @b1n2h3x
