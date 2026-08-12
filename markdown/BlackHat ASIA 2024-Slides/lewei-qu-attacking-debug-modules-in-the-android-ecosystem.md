---
title: "Attacking Debug Modules In The Android Ecosystem"
speakers: ["Lewei Qu"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2024"
edition: "ASIA"
year: 2024
source_pdf: "BlackHat ASIA 2024-Slides/Lewei Qu-Attacking Debug Modules In The Android Ecosystem.pdf"
pages: 36
sha256: "c42cf67bbb752141205744065b38e86d086167d4d73fc6e322ff1c52fda69da9"
text_chars: 15114
ocr_pages: 12
has_ocr: true
redacted_secrets: 0
ocr_confidence: 83.1
ocr_unreliable_blocks: 0
vision_verified_blocks: 1
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:48:21Z"
---
# Attacking Debug Modules In The Android Ecosystem

**Speakers:** Lewei Qu  
**Conference:** Black Hat ASIA 2024  
**Source:** `BlackHat ASIA 2024-Slides/Lewei Qu-Attacking Debug Modules In The Android Ecosystem.pdf` (36 pages)


## Slide 1

### Attacking Debug Modules In The Android Ecosystem

Lewei Qu(曲乐炜) Chief Information Security Officer, Mogo Auto

#BHASIA @BlackHatEvents


> Recovered by OCR — confidence 83/100 on the text kept, 60/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
_ blackhat
APRIL 18-19, 2024 | lat
Attacking Debug Modules In The Android
Ecosystem
Lewei Qu(HHERKS)
Chief Information Security Officer, Mogo Auto
A
```

## Slide 2

## About Me

- ➢ Head of security team in Mogo Auto. Leading the team to protect the cooperative vehicle infrastructure system and improve the level of network and data security of the company

- ➢ Previously focused on mobile/IoT security and has contributed a lot of vulnerabilities in Google Android, Mediatek and Unisoc. 500+ CVEs has been credited. Top1 bug hunter in the Unisoc Product Security Acknowledgements

- ➢ Google top bug hunter in 2022

- ➢ Speaker at BlackHat Europe 2021, BlackHat Aisa 2022, BlackHat USA 2022, KCon 2023, 7<sup>th</sup> kanxue SDC 2023

# BHASIA @BlackHatEvents

## Slide 3

## Agenda

Background Threat Module

Summary
Case Study

# BHASIA @BlackHatEvents

## Slide 4

# Background

# BHASIA @BlackHatEvents

## Slide 5

#### Fragmented Android Ecosystem

###### **OEM**

**Fragmented Product**

**Launcher** ：MIUI, Magic UI, HarmonyOS

**System APP** : **Debug modules** , Notebook, Device interconnection

**PRODUCT Phone Tablet**

**IVI**

**AIoT**

###### **Fragmented System**

##### **SYSTEM Android Open Source Project**

**Fragmentation**

**Framework** ：Vendors modify the service of AOSP to adapt their own hardware feature such as telephony and modem.

**HAL** ：The bridge to connect the framework and driver

###### **Fragmented BSP**

硬件 **SOC**

**Driver** ：Image processing(Camera), WiFi, Bluetooth, GNSS, 4G/5G, Audio processing, Acceleration(GPU/NPU/DSP), Secure element

# BHASIA @BlackHatEvents

## Slide 6

#### Fragmented Android Ecosystem

Vendor Partition HAL
Introduced from Android  Wrapper of low-level
Oreo. Managing vendor  operations for user space
specific BSP code
Security Bulletin ACSRP
Including the criticle and  Android Chipset Security Reward
high vulnerabilities for  Program. Supported by Google in 2019.
SoC But has been shut down in 2023.5

# BHASIA @BlackHatEvents

## Slide 7

#### Android Debug Architecture

- ➢ **Log Capture:** App Log, Kernel Log, Subsystem Log(Modem, DSP, Wi-Fi, Bluetooth)

- ➢ **Function Verification:** Camera, Display, Hardware Peripherals, GPU Rending

- ➢ **Factory Testing:** Vendor Specific

# BHASIA @BlackHatEvents

## Slide 8

#### Android Debug Architecture

##### **Developer options**

- ➢ **General options:** Memory, Error reporting, Oem unlocking

- ➢ **Debugging:** USB debugging, ADB debugging

- ➢ **Network:** Wi-Fi, Bluetooth

- ➢ **Input:** Show touch feedback

- ➢ **Drawing:** Show layout bounds

- ➢ **Hardware acceleration:** GPU rendering

- ➢ **Media:** USB

- ➢ **Monitoring:** Visual information for application performance

https://developer.android.com/studio/debug/dev-options

# BHASIA @BlackHatEvents

## Slide 9

#### Android Debug Architecture **Android Debug Bridge analysis**

# BHASIA @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Android Debug Architecture
Android Debug Bridge analysis
System APP Frameworks Native Daemon
Settings
ADE Debug
Open USB debugging Al ebugging
adb
. adbd
User ContentObserver listening User
SettingsProvider
```

## Slide 10

#### Android Debug Architecture

##### **Log capturing**

# BHASIA @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Android Debug Architecture
Log capturing
RLOGD, RLOGE| Radio
SLOGI, SLOGW| System
Log.printin_native |
libandroid_runtime.so
y ¥ # android user-space log man
__android_log_write __android_log_print type logd, domain, domain_deprecated, mlstrustedsubject;
init_daemon_domain(l
liblog logd # Read access to pseudo filesystems.
H r_dir_file(logd, proc)
r_dir_file(logd, proc_net)
A allow self:capability setuid setgid sys_nice audit_control
allow self:capability2 syslog;
allow self:netlink_audit_socket create_socket_perms nlmsg_write
kernel:sy read;
ow stem syslo
allow
logcat allow
1 kmsg_device:chr_file w_file_perms;
xd system_data_file:file r_file_perms;
```

## Slide 11

#### Android Debug Architecture

##### **Summary**

- ➢ The debug modules involve multiple interprocess communication (IPC) methods such as Binder Call, Unix Domain Socket, Content Provider, HIDL, etc.

- ➢ The data flow in the debugging module is complex, where user-level data is passed to high-privileged Native Daemon or Driver.

# BHASIA @BlackHatEvents

## Slide 12

#### Vendor Debug Architecture

##### **Why do vendors need to do customized debugging?**

- ➢ **Log capturing** : It is necessary to obtain debug logs from subsystems and have standardized debugging capabilities, which include capturing debug information from all modules, such as MTK's AEE (Android Exception Engine) and UNISOC's ylog.

- ➢ **Function verification:** Telephony (5G Vowifi), connectivity (BT WiFi FM), hardware (Camera DSP), location (GNSS).

- ➢ **Factory testing tools:** Basic checks in factory testing phase including the screen, peripherals, etc.

# BHASIA @BlackHatEvents

## Slide 13

#### Vendor Debug Architecture

##### **Vendor U log capturing**

# BHASIA @BlackHatEvents


> Recovered by OCR — confidence 75/100 on the text kept, 66/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Vendor U log capturing
BEX ‘A
Android Log
BT HCl Log qx
” @ylog_cli | ' ey srtd(system) ARM Pom Log
System APP — : DSP Log Output Mode >
p pe ' mlogservice(shell) DSP Log .
com.sprd.logmanager { : WIFI/BT Log .
System APP t af AG-DSP Pcm Dump Log
; AT Command Control ‘ ” @wend HAL Service | AG-DSP Log é
security code | ATControl ' ' DSP Pcm Log
Engineering Mode ‘ ' CP Cap Lo qx
com.sprd.engineermode Modem Log Config y m, _ | el vendor. sprd.hardware.cplog_connmgr@1.0-s: orca ap Log
CPControl ' ' orca dp Log
SE PES Modem Abnormal Monitor
WIFI/BT/GNSS log
Modem Log Control '
CPLogControl ' ; Native Daemon
slogmodem(root)
@hidie_modemd
modemlog_connmgr_service
(root)
```

## Slide 14

#### Vendor Debug Architecture

##### **Vendor M log capturing**

# BHASIA @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Vendor M log capturing
Send administrative commands through uds
| | | | Ustening for mooming commands
| | | Get different types of logs
logd atf log drvier ftrace kernel module
```

## Slide 15

#### Vendor Debug Architecture **Vendor U function verification/Factory testing tools**

# BHASIA @BlackHatEvents


> Recovered by OCR — confidence 79/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Vendor U function verification/Factory testing tools
10
| Framework |
Binder Call |
Wi-Fi test ' i yn)) #141
RF CALI test
RIC test getMacAdress
System APP Backlight test ; 7 BluetoothManager
3rd APP invoke > ey hutoatt ools = |System Version test SystemVersionTest}— _
GPS test \\.___ [Unix Domain Socket |__ Native Daemon
\getsn
Bluetooth test YON
SIM card test \) = (system)
- OTG test
File Read --, System File
5 File Open
```

## Slide 16

#### Vendor Debug Architecture

##### **An example**

###### **Problem**

- ➢ "EngineerMode" app by Qualcomm

- ➢ Gain root access through privilege escalation

###### **Reflection**

- ➢ BSPs often come with factory testing tools, which inherently carry out risky operations

- ➢ OEM/ODMs often lack sufficient security awareness and fail to disable or remove factory testing tools.

# BHASIA @BlackHatEvents

## Slide 17

# Threat Module

# BHASIA @BlackHatEvents

## Slide 18

#### Threat Module

# BHASIA @BlackHatEvents


> Recovered by OCR — confidence 82/100 on the text kept, 61/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Threat Module
third-party APP
remote debug
tools | | |
Network Socket A). — i call service call broadcast receive provider call >
System APP EngineerMode Validationtools
Bluetooth WIFI wifi log network log
Daemon
“~! log HAL connmrg
L“ | Service
L | Driver
```

## Slide 19

#### Attacking Debug APP

- ➢ 3<sup>rd</sup> APP -> High-privileged app (with a range of permissions)

- ➢ APP exported components -> Local privilege escalation, information leakage

- ➢ Socket port listening -> Remote command execution

# BHASIA @BlackHatEvents

## Slide 20

#### Attacking Debug Deamon

- ➢ Entry point: Unix Domain Socket

➢ Memory Corruption，Information Leak，Command Injection ……

# BHASIA @BlackHatEvents

## Slide 21

#### Attacking Debug HAL Service

- ➢ Entry point: Unix Domain Socket/HIDL

- ➢ Memory Corruption，Information Leak，Command Injection ……

# BHASIA @BlackHatEvents

## Slide 22

#### Attacking Debug Driver

- ➢ Entry point: File Operations

###### ➢ Memory Corruption，Information Leak……

# BHASIA @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 83/100 on the text kept, 77/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Attacking Debug Driver
➢ Entry point: File Operations
➢ Memory Corruption，Information Leak……

1   WARNING: CPU: 1 PID: 5755 at sprd_sysdump_write+0x1d0/0x20c
2   [ 3431.001448] Modules linked in: sprdwl_ng(O) flash_ic_sc2721(O) sprd_fm(O) sprdbt_tty(O) gt9xx_ts(O) gslX680_ts(O) himax_ts(O) tcs3430(O)
3   [ 3431.001501] CPU: 1 PID: 5755 Comm: poc_qlw Tainted: G           W  O    4.14.133 #1
4   [ 3431.001504] Hardware name: Spreadtrum SC9863A-1H10 Board (DT)
5   [ 3431.001509] task: 0000000075332dd3 task.stack: 0000000057e69639
6   [ 3431.001514] PC is at sprd_sysdump_write+0x1d0/0x20c
7   [ 3431.001518] LR is at sprd_sysdump_write+0x1d0/0x20c
8   [ 3431.001522] pc : [<ffffff800846f080>] lr : [<ffffff800846f080>] pstate: 60400045
9   [ 3431.001525] sp : ffffff8009c13d50
10  [ 3431.001527] x29: ffffff8009c13d80 x28: ffffffc078b7e200
11  [ 3431.001534] x27: ffffff8008962000 x26: 0000000000000040
12  [ 3431.001540] x25: 0000000000000124 x24: ffffffc078b7e200
13  [ 3431.001550] x23: 0000000000000000 x22: 0000000000300000
14  [ 3431.001557] x21: 0000007fdae36bf8 x20: 0000007fdae36bf8
15  [ 3431.001563] x19: 0000000000300000 x18: 00000000000000ac
16  [ 3431.001571] x17: 00000000000000ac x16: ffffff8009064cc4
17  [ 3431.001577] x15: 0000000000000004 x14: 000000000000003c
18  [ 3431.001583] x13: 000000000004a578 x12: 0000000000000000
19  [ 3431.001589] x11: 0000000000000001 x10: 0000000000000007
20  [ 3431.001594] x9 : 90ccfcb0d45ec300 x8 : 90ccfcb0d45ec300
21  [ 3431.001604] x7 : 0000000000000000 x6 : ffffff80090af233
22  [ 3431.001610] x5 : 0000000000000000 x4 : 0000000000000008
23  [ 3431.001616] x3 : 0000000000000021 x2 : 0000000000000001
24  [ 3431.001622] x1 : 00000000000000c0 x0 : 0000000000000027
25  [ 3431.001634] \x0aPC: 0xffffff800846f000:
26  [ 3431.001637] f000  913dd821 97f266e7 2a1f03e0 94000035 d0003ba0 b0003ba1 91019000 913dd821
27  [ 3431.001660] f020  97f266e0 d0005669 f94007e8 f9478529 eb08013f 54000421 aa1303e0 a9437bfd
28  [ 3431.001680] f040  a9424ff4 f9400bf5 910103ff d65f03c0 d0003ba0 b0003ba1 91008000 913dd821
29  [ 3431.001700] f060  97f266d0 d4210000 14000000 b00039a0 913f6c00 528000a1 aa1303e2 97f266c9
30  [ 3431.001720] f080  d4210000 14000006 aa0003e2 cb020268 8b0802a0 2a1f03e1 941335fa b0003ba0
```

## Slide 23

# Case Study

# BHASIA @BlackHatEvents

## Slide 24

#### Vulnerability  Discovery

###### **Findings**

- ➢ 49 CVEs Credit

- ➢ 3 vendors

# BHASIA @BlackHatEvents

## Slide 25

#### Information Disclosure

- ➢ CVE-2022-20098

- ➢ Debug Native Daemon: aee_aed/aee_aed64

- ➢ Entry point: UDS com.mtk.aee.aed_64

Accepting parameters to dump information from any process

# BHASIA @BlackHatEvents

## Slide 26

#### Information Disclosure

###### ➢ Debug APP: EngineerMode

Leaking various device identification codes

# BHASIA @BlackHatEvents


> Recovered by OCR — confidence 80/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Information Disclosure
> Debug APP: EngineerMode
Leaking various device identification codes
if(this.mPcscfSwitch != null) {
v@_3 = SystemPropertiesProxy.get(
if("".equals(v@_3)) {
this .mPcscfSwitch.setChecked(false);
else {
v1_1 = this.mPcscf
v1_1.setSummary(this.getString(@x7Fe
e public
int v1 = this.getPhoneCount();
v2 = new (v1)5
for(v4 = ©; true; ++v4) {
v1_l = v25
Ant v2_1 = this.getPhoneCount();
tch.setSummary(this.getString(@x7F
+ v@_3.trim());
elephonyManagerProxy . INSTANCE .getCdmaImsi (v3);
4f(v4_1 == mult) {
}
else
}
(ve, + Collectionskt. joinToString$default(vi_1, mull, null, null, @, null, null, @x3F, null));
return ((List)v1_1);
Code
@3-11 16:37:13.646 2835 is
Code
@3-11 13:35:52.354 12774 12774 D PHONEINF: get all IP
@ (value={ » @ public getAllimei() {
int v1 = this.getPhoneCount();
v2 = new (v1);
int v4;
v2.add("");
v1.1 = v2;
int v2_1 = this.getPhoneCount();
while(v3 < v2_1) {
v4_1 = this.getTelephoneMgr().getImei(v3);
Intrinsics.checkExpressionValueIsNotNull(v4_1, ;
(( )v1_1).set(v3, v4_1);
d(ve, + Collectionskt.joinToString$default(v1_1, null, null, null, @, null, null, @x3F, null))
return (( )vi_1);
```

## Slide 27

#### Memory Corruption

- ➢ CVE-2022-48382

- ➢ Debug HAL Service: vendor.sprd.hardware.log@1.0-service

- ➢ Entry point: UDS hidl_common_socket

###### Buffer Overflow

# BHASIA @BlackHatEvents

## Slide 28

#### Memory Corruption

- ➢ CVE-2022-39118

- ➢ Debug Driver: sprd_sysdump

- ➢ Entry point: File Operations

###### Out-of-Bound Write

# BHASIA @BlackHatEvents

## Slide 29

#### Local Privilege Escalation

- ➢ CVE-2022-47339

- ➢ Debug Daemon: cmd_service

- ➢ Entry point: UDS cmd_skt

# BHASIA @BlackHatEvents


> Recovered by OCR — confidence 84/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Local Privilege Escalation
> CVE-2022-47339 | int64 astcall sub_21BC(_intea a1)
at
> Debug Daemon: cmd service aera mate
pthread_t v4; //
i . FILE *v5; //
> Entry point: UDS cmd_skt ery
__int64 v7; //
int64 v8; //
st char *v9; //
__int64 v1e; //
int64 v11; //
s[4096]; //
v14[40976]; //
_ReadStatusReg(ARM64_SYSREG(3, 3, 13, @, 2));
= *(_DWORD *)(al + 256);
= *(int *)(al + 260);
= pthread_self();
t405g_m8t3:/ # ls -al /data/local/tmp
total
-rw-rw-rw- 1 shell shell @ 2022-09-14 11:26 \r
drwxrwx--x 3 shell shell 3488 2022-09-18 @8:33 .
drwxr-x--x 5 root root 3488 2022-06-25 21:16 ..
drwxrwxrwx 5 shell shell 3488 2022-09-15 13:59 .studio
-rw-rw-r-- 1 shell shell 3624718 2022-09-13 22:10 1.png
```

## Slide 30

#### Exploiting vulnerabilities

- ➢ CVE-2022-27250(Duplicated with Kryptowire)

# BHASIA @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Exploiting vulnerabilities
> CVE-2022-27250(Duplicated with Kryptowire)
Kryptowire Identifies Security and Privacy
Vulnerability in Mobile Device Chipset from China
The params are receviced and could test the functions in device. Such ase
1, Camera’
March 15, 2022 — McLean, VA, United States—Kryptowire Inc., a mobile security and privacy solutions company, today 5. Video
announced that they have identified a critical security and privacy vulnerability affecting mobile devices with UNISOC, ;
China's largest designer of chips for mobile phones. The vulnerability within the chipset, if exploited, allows malicious 6. Witie
actors to take control over user data and device functionality. 7 GPS
Specifically, the vulnerability allows intruders to access call and system logs, text messages, contacts, and other private Boon el
data, video record the device's screen or use the external-facing camera to record video, or even take control of the
device remotely, altering or wiping data. Adhering to its disclosure policy, Kryptowire notified affected device
manufacturers and carriers, as well as UNISOC, of the vulnerability in December 2021.
Thank you for your report! We appreciate your contribution to the Unisoc chipset rewards program.
This issue is duplicated with CVE-2022- 27250 (https://cve_mitre org/cgi-bin/cvename.cgi?name=2022-27250), we have removed SprdAutoSit from
user release build.
```

## Slide 31

#### Exploiting vulnerabilities

- ➢ CVE-2022-27250(Duplicated with Kryptowire)

# BHASIA @BlackHatEvents


> Recovered by OCR — confidence 76/100 on the text kept, 63/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Exploiting vulnerabilities
> CVE-2022-27250(Duplicated with Kryptowire)
fusr/bin/env python3
- import socket
this. setCurrentAc kAction. getInstance(this.mStatusChongedt istener
import sys
import sys
def send(payload):
this. setCurr
aa : s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("172.24.65.249", 7878))
ths ark2Action(this.mStatusChangedt istener, this.mContext)); s.send(payload.encode())
(2000) )
1|tue5g_ms8t3:/ $ netcat 127.6.8.1 1234
id
uid=1000(system) gid=1000(system) groups=1000(system) ,1013(media) ,1023(media_rw) ,1065(reserved_disk) ,2001(cache) , 3001(ne
```

## Slide 32

#### Exploiting vulnerabilities

➢ Limitation of CVE-2022-47339: The "setprop" command requires system-level permissions, and UDS (Unix Domain Socket) connections are subject to SELinux restrictions.

###### Selinux Policy

System Cmd

###### Root Cmd

# BHASIA @BlackHatEvents

## Slide 33

# Summary

# BHASIA @BlackHatEvents

## Slide 34

#### Summary

- ➢ The debug modules cover multiple layers of the system, from the app level to the driver level, resulting in multiple attack surfaces, primarily focused on inter-process communication (IPC).

- ➢ Some debug functionalities require executing high-privileged commands across processes. Improper handling of these commands can lead to local privilege escalation.

- ➢ Factory testing tools often involve Wi-Fi, Bluetooth, and telephony functionalities. Improper handling of these tools can result in information leakage, such as exposing Wi-Fi addresses, Bluetooth addresses, IMEI numbers, and other sensitive information.

# BHASIA @BlackHatEvents

## Slide 35

#### Suggestions

- ➢ **For vendors** :  some debug modules should not release to downstream such as factory testing.

- ➢ **For OEM/ODMs** : BSP modules should be selectively chosen based on specific needs, and not accepted in their entirety

- ➢ **For users** : Regularly perform device security upgrades.

# BHASIA @BlackHatEvents

## Slide 36

Thanks <u>https://twitter.com/sanpangzi321</u>

# BHASIA @BlackHatEvents
