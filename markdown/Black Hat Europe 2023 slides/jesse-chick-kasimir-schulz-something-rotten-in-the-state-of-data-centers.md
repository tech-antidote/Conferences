---
title: "Something Rotten in the State of Data Centers"
speakers: ["Jesse Chick", "Kasimir Schulz"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2023"
edition: "Europe"
year: 2023
source_pdf: "Black Hat Europe 2023 slides/Jesse Chick , Kasimir Schulz_Something Rotten in the State of Data Centers.pdf"
pages: 64
sha256: "bd9586e9b896509dbee94a88f8568054021249830c3d087f8344b409b0726232"
text_chars: 24319
ocr_pages: 7
has_ocr: true
redacted_secrets: 0
ocr_confidence: 86.7
ocr_unreliable_blocks: 0
vision_verified_blocks: 1
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:03:33Z"
---
# Something Rotten in the State of Data Centers

**Speakers:** Jesse Chick, Kasimir Schulz  
**Conference:** Black Hat Europe 2023  
**Source:** `Black Hat Europe 2023 slides/Jesse Chick , Kasimir Schulz_Something Rotten in the State of Data Centers.pdf` (64 pages)


## Slide 1

#BHEU   @BlackHatEvents


> Recovered by OCR — confidence 85/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
DECEMBER 4-7
EXCEL LONDON / UK
#BHEU @BlackHatEvents
```

## Slide 2

## Something Rotten in the State of Data Centers

Jesse Chick & Kasimir Schulz

#BHEU   @BlackHatEvents

## Slide 3

#### **`#whoami`**

**Jesse Chick** Vulnerability Researcher

**Kasimir Schulz** Principal Security Researcher HiddenLayer

Twitter: <u>@ravenousbytes</u> LinkedIn: <u>https://www.linkedin.com/in/jesse-chick</u>

Twitter: <u>@abraxus7331</u> LinkedIn: <u>https://www.linkedin.com/in/kasimir-schulz</u>

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 4

#### Outline

●Why research data centers? ●Target #1: DDI (DNS, DHCP, and IPAM) from Mystery Vendor ○Authenticated command injection

   - ○Bypassing authentication

   - ○Exploit chaining

- ●Target #2: KVM (Keyboard, Video, and Mouse) from Vertiv ○Authenticated RCE via malicious upgrade

   - ○Bypassing authentication by corrupting the heap

●Closing Thoughts: What have we learned?

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 5

#### Why Research Data Centers?

●Corporate and government interests

●Of significant national interest:

   - ○#1 item in the 2023 National Cybersecurity Strategy

   - ○Federal Data Center Enhancement Act of 2022

- ●High impact: attractive target for threat actors

- ●Little end-to-end (public) vuln research into data center technologies as a whole

●We suspected (and confirmed) that these products were no more secure than anything else

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 6

#### Our Previous Work

Team project to survey the state of data center security ●Diverse set of hardware and software appliances ●Target selection informed by industry experts

See our talk on hacking power management from DEF CON 31: ● <u>https://forum.defcon.org/node/245754</u> ● <u>https://youtu.be/k2Vx7hstOKY</u>

Final disclosures of this effort

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 7

# Target #1 Attacking Data Center Software

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 8

#### Project X

- ●Due to delays in responsible disclosure the first target will be referred to as **Project X**

- **Project X** is a **DDI** , a solution integrating **DNS** , **DHCP** , and **IPAM**

- **DDI** ’s provide efficient and secure network management for **data centers**

   - **DNS** provides easy and reliable access to resources

   - **DHCP** automates the assignment of IP addresses to devices

   - **IPAM** helps manage and organize unique ip addresses

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 9

#### Architecture of Project X

##### **Web** Server

##### **Control** Server

- ●Hosts the management website

- ●Handles user interactions and session management

   - ●Controls individual components

   - ●Handles Authentication

   - ●Handles all logging

- ●Can be connected to multiple control servers

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 10

#### Authenticated Command Injection

The **web server** had a system where admins could run scripts on the **control server** when an event occurred

When setting up a **hook** the admin gives the **script_name** which is then run whenever the event happens

No validation was done on what was passed to the **script_name** field allowing an authenticated user to perform a command injection:

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 11

# Bypassing Authentication

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 12

#### Authentication in Project X

**Web Server**

Web server receives server IP and user credentials

##### **Control Server**

Connects to the control server Receives credentials from the and sends credentials web server Validates that the credentials are correct and the user exists

Receives the direct connection and establishes a session

Connects directly to the web server over a custom port

Generates a session id and sends it to the control server

Receives the session id and sends it to the control server responds to the https request Receives session id from the with the session id control server

Uses session id to run all other requests

Accepts any requests made using the session id

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 13

#### Generation of Session ID

When a user is authenticated correctly, the web server calls the **addSession** function. This function relies on a custom **Random** class

The **Random** class is instantiated once and then **randString** is used each time a new **session_id** is to be generated

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 14

#### The Flaw in the Design

**Random** relies on the seed **gSeed**

**gSeed** is set once when the server starts When a new **session_id** is generated, **gSeed** is updated deterministically from its last value

Guessing the initial **gSeed** value makes it possible to predict every past and future generated **session_id** value

If someone knows the start time of the server they can easily get **gSeed**

Without knowing the start time it is still easy to guess the value as the top byte changes infrequently

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 15

#### Conversion Strikes Again

**gSeed** is generated by xor’ing the value of the time in milliseconds and the time in seconds

The **millisecs** value is a **64 bit** value, however the **seconds** value and **gSeed** are both **32 bit** values

AAAAAAAA

Millisecs value BBBBBBBB

Unlike **64 bit** , a **32 bit** seed is brute forceable with only **4,294,967,295** total combinations

The bottom 3 bytes will change often, however, the top byte will only change once every **1.9 days**

Seconds value
DDDDDDDD

If we know within **1.9 days** of when the server was started we only need to find **16,777,216** combinations

gSeed value
EEEEEEEE

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 16

#### Our Malicious Server

In order to find the **gSeed** we needed a valid **session_id** from the web server

A valid **session_id** allows us to validate that we are able to generate the correct **session_id** ’s

When a user tries to login, they are able to specify the **ip** or **domain name** of the **control server** they want to access

We can abuse this to login to a server that we have the credentials for

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 17

#### Cracking the Session ID Generation

Our strategy to determine the **gSeed** value based on a valid **session_id** broke down into 4 steps:

1. Spin up our own version of the web server

1. Use Frida to hook into the binary and grab the **Random** initialization and **RandString** functions

3. Use these functions to replicate the **addSession** function and brute force **gSeed** till we are able to generate the valid **session_id**

4. Use **gSeed** to generate as many **session_ids** as we want

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 18

#### Using Frida to Determine IDs

#BHEU   @BlackHatEvents

Information Classification: General


> Recovered by OCR — confidence 84/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Using Frida to Determine IDs
const RandomInit = new NativeFunctton(ptr(
‘pointer', ['pointer']);
const RandomString = new NativeFunctton(ptr(
‘pointer', ['pointer', ‘pointer', ‘int']);
```

## Slide 19

#BHEU   @BlackHatEvents

Information Classification: General


> Recovered by OCR — confidence 88/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
black hat
const cm = new CModule(~
#include <string.h>
extern void* RandomInit(char*);
extern void* RandomString(char*, char*, int);
int ccrack(int start, int* gSeedPtr, char* target) {
char Random[4096], token[4096];
for (int i = 0; i < Ox01000000; i++) {
xgSeedPtr = start + 1;
RandomInit( Random) ;
RandomString( token, Random, 0x14);
if (!strcemp(*(char**)token, target)) {
return start + 1;
}
}
return -1;
```

## Slide 20

#BHEU   @BlackHatEvents

Information Classification: General


> Recovered by OCR — confidence 88/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
black hat
const ccrack = new NativeFunction(cm.
‘int', ['int', 'pointer', 'pointer']);
function seedcrack(targetToken) {
const gSeedPtr = ptr( )3
const gSeed = . ();
const targetPtr = Memory.
const seed ccrack(START_VALUE,
let Random = Memory. (
let tokenPtr = Memory.
RandomInit ( );
RandomString(
console. (
}
}
```

## Slide 21

#### Increasing Computational Demand

While the above worked and we were able to consistently generate the **session_id** ’s of other users, we were left with several issues:

1. The more uncertain the start time of the server was, the longer the computation would take

1. The more time the server was running, the more **session_id** ’s it had generated, making it harder to predict which users were assigned to what id’s

However, luckily for us, Project X had done a fantastic job on ensuring the robustness of the server against denial of service attacks…

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 22

#### Keep Calm and DOS On

We started fuzzing and found **2 denial of service** attacks that would cause the web server to crash

Crash happened by connecting the **web server** to a fake **control server** we scripted and sending a malformed packet

When the **web server** crashed **gSeed** was reset and could easily be brute forced

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 23

#### Full Attack Chain

Malicious Actor
Connect to the restarted
web server to get session  Wait for someone to reconnect to the
id control server and launch attack
Points web server to fake
server
Web Server Control Server
Fake server
crashes the web
server
Web server connects
to the fake server
Fake Server

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 24

#### Bypassing our Limitations

On their own, each vulnerability had one or more limitations, however, when chained we were able to bypass these:

1. The original **command injection** required an attacker to have admin credentials. This was bypassed by finding a way to **bypass authentication**

1. The **authentication bypass** relied on either a high amount of **brute forcing** or **insider knowledge** of the target. This was bypassed by reverse engineering the seed generation code to find a way to **reduce the potential combinations** and by finding a way to **crash the server** so that we would no longer need to know when the server was started

**Key Takeaway** : While one vulnerability may give you what you want, you can probably find others that will give you an even better version of what you want

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 25

# Target #2 Attacking Data Center Hardware

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 26

#### Avocent MPU4032DAC KVM

Keyboard, Video, Mouse (KVM)

- ●Remote management of infrastructure and appliances in:

   - ○Collocated caged spaces

   - ○On-prem setups

- ●Popular in telecommunications

- Maintained and distributed by Vertiv Firmware:

- Vulnerable version: <u>2.12.3</u> (Mar. 2023)

- Patched version: <u>2.12.4</u> (Sept. 2023)

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 27

# Getting a Root Shell

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 28

#### Local Firmware Upgrades (not OTA)

The firmware image is available for download at the Vertiv website!

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 29

#### Understanding the Firmware

Information Classification: General

#BHEU   @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 90/100 on the text kept, 87/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Disrupting the state machine to discover new Bluetooth vulnerabilities

[left pane - tombstone log #1]
07-25 16:48:21.877  8247  8247 F DEBUG   : Revision: '0'
07-25 16:48:21.877  8247  8247 F DEBUG   : ABI: 'arm64'
07-25 16:48:21.878  8247  8247 F DEBUG   : Timestamp: 2024-07-25 16:48:21+0800
07-25 16:48:21.878  8247  8247 F DEBUG   : pid: 30577, tid: 30656, name: bt_hci_thread  >>> com.android.bluetooth <<<
07-25 16:48:21.878  8247  8247 F DEBUG   : uid: 1002
07-25 16:48:21.878  8247  8247 F DEBUG   : signal 6 (SIGABRT), code -1 (SI_QUEUE), fault addr --------
07-25 16:48:21.878  8247  8247 F DEBUG   :     x0  0000000000000000  x1  00000000000077c0  x2  0000000000000006  x3  0000007652575520
07-25 16:48:21.878  8247  8247 F DEBUG   :     x4  53736d647543ff6f  x5  53736d647543ff6f  x6  53736d647543ff6f  x7  7f7f7f7f7f7f7f7f
07-25 16:48:21.878  8247  8247 F DEBUG   :     x8  00000000000000f0  x9  982f6af2b61cd630  x10 0000000000000000  x11 ffffffc0fffffbdf
07-25 16:48:21.878  8247  8247 F DEBUG   :     x12 0000000000000001  x13 0000000000000034  x14 002d28d6f857981b  x15 0000000034155555
07-25 16:48:21.878  8247  8247 F DEBUG   :     x16 00000079bb13fc80  x17 00000079bb1219f0  x18 0000007651c6e030  x19 0000000000007771
07-25 16:48:21.878  8247  8247 F DEBUG   :     x20 00000000000077c0  x21 00000000ffffffff  x22 0000007652576000  x23 00000076640b67b0
07-25 16:48:21.878  8247  8247 F DEBUG   :     x24 0000000000000001  x25 0000007652575cc0  x26 0000007652575ff8  x27 00000000000fc000
07-25 16:48:21.878  8247  8247 F DEBUG   :     x28 000000765247d000  x29 00000076525755a0
07-25 16:48:21.878  8247  8247 F DEBUG   :     lr 00000079bb0d5420  sp 0000007652575500  pc 00000079bb0d544c  pst 0000000000000000
07-25 16:48:21.951  8247  8247 F DEBUG   : backtrace:

[left pane - tombstone log #2]
10-01 01:53:17.420 12789 12789 F DEBUG   : Revision: '0'
10-01 01:53:17.420 12789 12789 F DEBUG   : ABI: 'arm64'
10-01 01:53:17.420 12789 12789 F DEBUG   : Timestamp: 2024-10-01 01:53:15.530682377+0800
10-01 01:53:17.420 12789 12789 F DEBUG   : Process uptime: 0s
10-01 01:53:17.421 12789 12789 F DEBUG   : Cmdline: com.android.bluetooth
10-01 01:53:17.421 12789 12789 F DEBUG   : pid: 11102, tid: 11136, name: gd_stack_thread  >>> com.android.bluetooth <<<
10-01 01:53:17.421 12789 12789 F DEBUG   : uid: 1002
10-01 01:53:17.421 12789 12789 F DEBUG   : tagged_addr_ctrl: 0000000000000001 (PR_TAGGED_ADDR_ENABLE)
10-01 01:53:17.421 12789 12789 F DEBUG   : signal 6 (SIGABRT), code -1 (SI_QUEUE), fault addr --------
10-01 01:53:17.421 12789 12789 F DEBUG   : Abort message: 'assertion 'false' failed - Done waiting for debug informa[clipped]
10-01 01:53:17.421 12789 12789 F DEBUG   :     x0  0000000000000000  x1  0000000000002b80  x2  0000000000000006  x3 [clipped]
10-01 01:53:17.421 12789 12789 F DEBUG   :     x4  1f646d6e431f2c1f  x5  1f646d6e431f2c1f  x6  1f646d6e431f2c1f  x7 [clipped]
10-01 01:53:17.421 12789 12789 F DEBUG   :     x8  00000000000000f0  x9  00000074c8a3b0b0  x10 0000000000000001  x11 [clipped]   <- only the top half of this line is visible; the overlaid photo covers the rest
[subsequent lines of this pane are covered by an overlaid photo - see below]
std::__1::default_delete<std:[covered]
10-01 01:53:17.422 12789 12789 F DEBUG   :      #09 pc 00000000000d6e3c  /apex/com.android.runtime/lib64/bionic/lib[clipped]
10-01 01:53:17.422 12789 12789 F DEBUG   :      #10 pc 000000000006ab00  /apex/com.android.runtime/lib64/bionic/lib[clipped]
6f67f69ff36b970d0b831cfdab3b5[obscured]

[overlaid photograph of a screen showing a third tombstone; most of it is pixelated/[obscured]]
[obscured] F DEBUG  : pid: [obscured], tid: 29311, name: btu[clipped]     [obscured]: 2023-08-22 14:49:32+08[clipped]
29367 F DEBUG  : uid: [obscured]
29367 F DEBUG  : signal 6 (SIGABRT), code -1 (SI_QUEU[clipped]
29367 F DEBUG  : Abort message: 'ubsan: out-of-bounds[clipped]
293[obscured] F DEBUG  :     x0  [obscured]        x1  0[obscured]

[right pane - logcat; the middle band is covered by a pixelated image]
08-04 19:09:41.7[obscured] 28889 28889 E BluetoothPhonePolicy: Received unexpected intent, action=android.bluetooth.device.action.ACL_CONNECTED
08-04 19:09:41.838 28889 28921 I bt_btif_dm: get_cod remote_cod = 0x000c010c
08-04 19:09:41.838 28889 28921 I bt_btif_dm: get_cod remote_cod = 0x000c010c
08-04 19:09:41.840 28889 28932 I BluetoothBondStateMachine: Entering PendingCommandState State
08-04 19:09:42.240 28889 28921 I bt_btif_dm: get_cod remote_cod = 0x000c010c
08-04 19:09:42.241 28889 28921 E bt_stack: [ERROR:metric_id_allocator.cc(181)] BluetoothMetricIdAllocatorFailed to forget device because device is not in
paired_device_cache_
08-04 19:09:42.244 28889 288[obscured] W A2dpSe[obscured]
08-04 19:09:42.247 28889 28932 [obscured]
08-04 19:09:42.247 28889 2[obscured]
08-04 19:09:42.247 28889 28[obscured]
08-04 19:09:42.247 28889 289[obscured]
08-04 19:09:42.269 28889 [obscured]
08-04 19:09:42.272 28889 2[obscured] bt_stack: [INFO:btsnoop.cc(289)] whitelist_l2c_channel: Whitelisting [obscured] channel. conn_handle=50 cid=0x0040:0x0040
08-04 19:09:42.316 28889 28944 I bt_stack: [INFO:connection_handler.cc(380)] void bluetooth::avrcp::ConnectionHandler::AcceptorControlCb(uint8_t, uint8_t,
uint16_t, const RawAddress *): Connection Opened Event
08-04 19:09:42.317 28889 28944 I bt_stack: [INFO:connection_handler.cc(211)] virtual bool bluetooth::avrcp::ConnectionHandler::SdpLookup(const RawAddress
[obscured] Callback, bool)
08-04 19:09[obscured]
08-04 19:0[obscured]                                    [obscured].cc(256)] virtual [obscured]
wAddress &): handle=0x01 status= 000000
08-04 19:09:52.536 28889 32698 I droid.bluetoot: Starting a blocking GC NativeAllo[obscured]
08-04 19:09:53.117 28889 32698 I AppScanStats: BLE_SCAN_RESULT_RECEIVED[6]noteBleScanResults=0
08-04 19:09:53.117 28889 32698 I AppScanStats: BLE_SCAN_STATE_CHANGED[6]noteBleScanStopped=false
08-04 19:09:53.119 28889 32698 E AudioSystem: onAudioOutputDeviceChanged (2, 2)
08-04 19:09:54.855 28889 32698 E AudioSystem: onAudioOutputDeviceChanged (0, 2)
08-04 19:10:02.918 28889 28889 I ActivityThread: Removing dead content provider:android.content.ContentProviderProxy@1617aa
08-04 19:10:13.429  1191  3966 I ActivityManager: Process com.android.bluetooth (pid 28889) has died: psvc PER

[bottom-right pane - tombstone log #3]
Revision: '0'
ABI: 'arm64'
Timestamp: 2023-09-01 15:24:04+0800
pid: 1226, tid: 1305, name: droid.bluetooth  >>> com.android.bluetooth <<<
uid: 1002
signal 11 (SIGSEGV), code 1 (SEGV_MAPERR), fault addr 0x0
Cause: null pointer dereference          [boxed in red]
    x0  0000000000000000  x1  000000000000000f  x2  b400007854339ab0  x3  0000000000000010
    x4  b400007854339ac0  x5  0000000000000002  x6  00000000ffffffff  x7  00000077db558839
    x8  0000000000000001  x9  0000000000000000  x10 000000002bc93534  x11 0000000054339ac0
    x12 000000008c22d80c  x13 b400007864380c18  x14 ffffffffffffffdf  x15 000000001a1f5e40
    x16 00000077db81d218  x17 00000077db7a9a90  x18 00000077d9e0c000  x19 b4000078a432b070
    x20 b40000786437b260  x21 b40000787435e0e8  x22 b400007854339ab0  x23 000000000000000c
    x24 b40000787435e0e6  x25 0000000000000000  x26 000000000000000e  x27 0000000000000001
    x28 00000077db82c000  x29 00000077db558b50
    lr  00000077db7ab684  sp  00000077db558b50  pc  00000077db7ab6c8  pst 0000000060000000
backtrace:
    #00 pc 000000000010d6c8  /system/lib64/libbrtsdk.so (AVDTP_DelayReport_Ind+144) (BuildId: 98fa8e78291628587d0804f42a442a9b)
    #01 pc 000000000010a22c  /system/lib64/libbrtsdk.so (AVDTP_SignalMsg_Received+140) (BuildId: 98fa8e78291628587d0804f42a442a9b)
    #02 pc 0000000000109da4  /system/lib64/libbrtsdk.so (AVDTPC_L2CAPData_Ind+88) (BuildId: 98fa8e78291628587d0804f42a442a9b)
    #03 pc 00000000000da234  /system/lib64/libbrtsdk.so (ScheduleLoop+360) (BuildId: 98fa8e78291628587d0804f42a442a9b)
    #04 pc 00000000000d4598  /system/lib64/libbrtsdk.so (porting_thread_proc+12) (BuildId: 98fa8e78291628587d0804f42a442a9b)
    #05 pc 00000000000afecc  /apex/com.android.runtime/lib64/bionic/libc.so (__pthread_start(void*)+64) (BuildId: 8d0a10271eef02de6c33[clipped]
    #06 pc 0000000000050408  /apex/com.android.runtime/lib64/bionic/libc.so (__start_thread+64) (BuildId: 8d0a10271eef02de6c33b788fec2[clipped]
```

## Slide 30

#### Understanding the Firmware

Region 0: **Header** ●Custom format

##### Region 1: **Kernel**

- ●Linux version 2.6.23

- ●Compiled for PowerPC

- ●gzip-compressed

- Region 2: **Filesystem** ●Flattened into single file called “AVO.fs” ●gzip-compressed

##### Region 3: **Not Sure…**

- ●U-Boot?

- ●CRC32 polynomial table?

Firmware header
Linux Kernel
(gzipped)

Workspace

Filesystem AVO.fs.gz
(gzipped) (gzipped)
Mysterious Blob

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 31

#### Unpacking the Filesystem

AVO.fs:

- ●Squashfs filesystem version 3.1 (2006-2007) ●Big endian

- ●75Mb in size

●3065 filesystem entities in total

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 32

#### Unpacking the Filesystem

- Need squashfs-tools 3.2 to re-squash the filesystem after adding a backdoor ●NOTE: v3.2 produces v3.1 Squashfs files ○No idea why this discrepancy exists

- ●Slight changes to source code needed

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 33

#### Adding a Backdoor

We want:

●Shell access over the network ●Root privileges

- ●Reusability

●Persistence across reboots ●Low profile

\```
/etc/rc.d/S99backdoor
\```

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 34

#### Repacking the Filesystem

###### **Procedure** :

1. Resquash the filesystem

2. gzip it with optimal compression

3. Pad it with zeros 4. Insert it back into the original firmware image

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 35

#### Upgrade with Backdoored Firmware

TODO: Generate upgrade failure image once all other visuals and demos have been generated – this _might_ brick the device.

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 36

#### Diagnosing the Upgrade Failure

\```
/sbin/main_app
\```

##### Click “Upgrade”

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 37

#### Diagnosing the Upgrade Failure

\```
/bin/firmware_checkimage.sh
\```

Is `checkImage` our point of failure?

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 38

#### Creating a Firmware Check Oracle

If checkImage is the point of failure, then:

- `checkImage FL0620-AVO-2.12.3.25987.fl` should return status code 0

- `checkImage FL0620-AVO-2.12.3.25987-BACKDOOR.fl` should return non-zero status code

- We can run `checkImage` with QEMU in user mode:

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 39

#### Creating a Firmware Check Oracle

`appconfig_get_int` function:

●Found in custom library `libavctcfg.so`

●It reads configuration values (integers) by key from _shared memory_

**We can replace calls to** **`appconfig_get_int` with “load immediate” (** **`li` ) instructions!**

…provided we know the expected values

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 40

#### Creating a Firmware Check Oracle

Three calls to appconfig_get_int, retrieving values for: `1."firmwareconfig.family.code" 2."oem.code" 3."firmwareconfig.ecc.required"`

`bl appconfig_get_int` becomes: `1.li r3, 0x2d 2.li r3, 0x8 3.li r3, 0x4`

We grepped through the filesystem to see where these config values are assigned:

\```
/sbin/checkImage-ORACLE
\```

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 41

#### Checking the Firmware

###### **Original Firmware: SUCCESS**

<u>So we have a working firmware-checking oracle!</u>

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 42

#### Checking the Firmware **Backdoored Firmware: FAILURE**

CRC32: a checksum algorithm that hashes byte sequences to 32 bit values.

<u>So we have identified the source of the upgrade failure!</u>

(At least for now…)

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 43

#### Forging the CRC

**CRC check: Does the computed CRC digest match the CRC digest found in the file metadata?**

Calculating CRC of backdoored firmware:

1. Run checkImage-ORACLE with GDB 2. Set breakpoint on CRC digest

   - comparison

3. Read operand values

Original CRC digest: `0x34e96d52`

Computed CRC digest:

#BHEU   @BlackHatEvents

> Information Classification: General `0xcf77014e`

## Slide 44

#### Forging the CRC

The original CRC digest ( `0x34e96d52` ) must be somewhere in the backdoored firmware file!

Filesystem CRC offset: **96** ( `0x60` )

We replace the original value with the calculated CRC digest ( `0xcf77014e` )

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 45

#### Checking the Firmware **Backdoored Firmware: SUCCESS**

CVE-2023-4285 CWE-354: Improper Validation of Integrity Check Value

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 46

### Demo

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 47

#### Facepalm Moment #1

**Vendor binaries to pack/unpack the firmware are present in** **`/bin`** ●Named `gen_fw` and `unpack_fw`

●Compiled for x86 _not_ PowerPC ●Can be run within a i386/debian Docker container

● <u>We could have skipped the whole CRC-forging step!</u>

\```
./unpack_fw <firmware_image>
\```

Firmware header
Linux Kernel
Linux Kernel
S99backdoor
Filesystem
Filesystem
Mysterious Blob
Mysterious Blob

\```
./gen_fw <config_file>
\```

Firmware header
Linux Kernel
Linux Kernel
CRC32
Backdoored
Backdoored
Filesystem
Filesystem
Mysterious Blob
Mysterious Blob

Mysterious Blob

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 48

# Bypassing Authentication

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 49

#### The Vulnerable ASMP Service

- **Avocent Secure Management Protocol** ●Love that for them 💁

- ●Supports 7 transactions types, e.g.: “Log in”, “Log out”, “KVM Session Setup”, “SNMP”, etc.

- ●ASMP handler implemented in the `main_app` binary

##### **Packet structure:**

- ●Header:

   - ○Magic number: `“\x01ASMP”`

   - ○Length of transaction data

   - ○Transaction type

- ●Transaction data

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 50

#### Root Cause Analysis

- ●ASMP packets parsed by a custom state machine.

   - ○“Custom state machine” 😈

- ●Reads packet header _and_ data into a

   - 0x4000-byte buffer

- **Enforces size restriction on the transaction data only!**

- ●Sending 0x4000 bytes of transaction data results in 13-byte overflow:

   - ○12 (0xc) bytes of header data

Heap land!

- ○1 extra byte for some reason

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 51

#### What Can We Do With 13 Bytes?

Create a new user with **arbitrary credentials** and the **highest possible privileges** !

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 52

#### Developing an Exploit

**Challenges:**

- ●13 bytes is not a lot…

- ●Unpredictable locations and lifetimes of objects on the heap ○ `main_app` is noisy

- **2 heap objects to worry about:**

- ●ASMP connection metadata (0x178 bytes)

- ●Buffer to store packet contents (0x4000 bytes)

`logged_in` : Flag indicating whether or not the ASMP connection is authenticated.

`access_level` :

- 1 - User

- 2 - User Administrator

- 3 - Appliance Administrator

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 53

#### The **`glibc`** Heap

- ●Each heap allocation is prepended with a `malloc_chunk` object

- `malloc_chunk` contains metadata for optimizing heap performance

   - <u>the size of the chunk (how much memory needs to be</u> `free()` ’ed?)

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 54

#### Exploit Mechanics (Step 1)

**Establish 10+ concurrent ASMP connections**

- ●Objects remain on the heap for the lifetime of the connection ●Necessary to ensure predictable heap layout

malloc_chunk Socket A Socket B Socket C
asmp_conn
buffer (0x4000) asmp_conn buffer asmp_conn buffer
(0x178)

~12 sockets in total

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 55

#### Exploit Mechanics (Step 2)

**Leverage 13-byte overflow via socket A to overwrite heap metadata for socket B** ●The size of socket B’s `asmp_conn` chunk is set to 0x4010 (previously 0x178 bytes) ○ `0x4010 == sizeof(buffer) + sizeof(malloc_chunk)` ■ `sizeof(malloc_chunk) == 8` but the heap is 16-byte aligned ●Socket B’s `asmp_conn` chunk is now “large enough” to fit a `buffer` allocation

malloc_chunk Socket A Socket B Socket C
asmp_conn
Socket A payloadbuffer (0x4000) asmp_conn buffer asmp_conn buffer
(0x178)

Socket B’s `malloc_chunk->mchunk_size = 0x4010`

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 56

#### Exploit Mechanics (Step 3)

**Close socket B gracefully by initiating a “Log out” transaction over this connection**

1. Socket B's `buffer` is freed

2. Socket B's enlarged `asmp_conn` is freed, such that the next `buffer` -size allocation will take its place on the heap

malloc_chunk Socket A Socket B closed Socket C
asmp_conn
buffer (0x4000) (Enlarged) asmp_conn freed buffer freed asmp_conn buffer
(0x178)
Location of next  buffer

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 57

#### Exploit Mechanics (Step 4)

**Establish another ASMP connection (Socket D)**

- ●Socket D's `asmp_conn` is allocated where socket B's `buffer` was

●Socket D's `buffer` is allocated where socket B's `asmp_conn` was

malloc_chunk Socket A Socket D
asmp_conn
buffer (0x4000) buffer    ………asmp_conn
(0x178)

Socket C

asmp_conn buffer

**Now the two socket D objects overlap!**

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 58

#### Exploit Mechanics (Step 5)

Preserve
malloc_chunk
values
Send the final payload!
● buffer  contains SNMP transaction to add a new
elevated access level
SNMP  “add user” payload
user with maximum privileges logged-in flag
● asmp_conn  is overwritten to set:
○ access_level = 3  (Appliance Administrator)
○ logged_in = 1  (authenticated)
malloc_chunk Socket A  Socket D Socket C
asmp_conn
buffer (0x4000)  Socket D pbuffer    ……… a yloadsmp_conn asmp_conn buffer
(0x178)
CVE-2023-4287
buffer asmp_conn
CWE-122: Heap-based
Buffer Overflow

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 59

### Demo

#BHEU   @BlackHatEvents

Information Classification: General


> Recovered by OCR — confidence 77/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
[™ NewTab ff] Splitview v
prec-5560% [|
© 6 MPU4032DAC Explorer x +
ry) V E RT | V. Avocent MergePoint Unity
Password
```

## Slide 60

#### Facepalm Moment #2

**Auth bypass via null-byte injection**

- ●Vulnerability in the login mechanism

- ●Gain an anonymous session by sending `username=%00`

CVE-2023-4288 CWE-288: Authentication Bypass Using an Alternate Path

- ●No password needed!

##### **Root Cause:**

- ●Anonymous sessions are supported for local ( `127.0.0.1` ) connections

- ●Logic bug causes requests with `NULL` username to be treated as such

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 61

### Demo

#BHEU   @BlackHatEvents

Information Classification: General


> Recovered by OCR — confidence 95/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
prec-5560% [|
6 @ New Tab
Amazon StubHub
Recommended by Pocket
Of War and Electric
Death: A Brief
History of Push-...
For over a century, buttons
have conjured fears of all-
or-nothing actions that...
T-Mobile YouTube
parecredit.cor
This Credit Card Is
Worth Its Weight in
Gold: Best Credit...
A game-changer for those
seeking a big rewards card
that doesn't cap its cash..
f
Facebook Reddit
Why America Is Just
Now Learning to
Love Thaddeus...
The Pennsylvanian was one
of America’s greatest
heroes. Why hasn't he.
```

## Slide 62

#### Concluding Thoughts

- ●Authentication alone doesn't justify weaker security; internal components should uphold the same security standards as externally facing elements

- ●Quality of life features can often be abused for exploitation; before turning features on by default, consider the potential security impact

- ●Data center systems are attractive targets for security researchers due to a broad attack surface and the significant impact of potential compromises

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 63

#### Acknowledgements

###### <u>This research was conducted in collaboration with our former colleagues at Trellix ARC</u>

##### Sam Quinn

Austin Emmitt

- ●Senior Security Researcher ○Currently with Exodus Intelligence

- ●Twitter: <u>@eAyeP</u>

- ●Principal Security Researcher ○Currently with Vigilant Labs

- ●Twitter: <u>@alkalinesec</u>

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 64

# Thank You

#BHEU   @BlackHatEvents

Information Classification: General
