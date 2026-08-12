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
text_chars: 24721
ocr_pages: 7
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:12:27Z"
---
# Something Rotten in the State of Data Centers

**Speakers:** Jesse Chick, Kasimir Schulz  
**Conference:** Black Hat Europe 2023  
**Source:** `Black Hat Europe 2023 slides/Jesse Chick , Kasimir Schulz_Something Rotten in the State of Data Centers.pdf` (64 pages)


## Slide 1

#BHEU   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisekhat
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pifeK hat
EUROPE 2023
Using Frida to Determine IDs
const RandomInit = new NativeFunctton(ptr(
‘pointer', ['pointer']);
const RandomString = new NativeFunctton(ptr(
‘pointer', ['pointer', ‘pointer', ‘int']);
```

## Slide 19

#BHEU   @BlackHatEvents

Information Classification: General

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat
EUROPE 2023
Pane see © < |. ASNy ge
const cm = new CModule(~
#include <string.h>
extern void* RandomInit(char*);
extern void* RandomString(char*, char*, int);
int ccrack(int start, int* gSeedPtr, char* target) {
char Random[4096], token[4096];
for (int i = 0; i < Ox01000000; i++) {
xgSeedPtr = start + 1;
for (int j = 0; j < 4; j++) {
RandomInit( Random) ;
RandomString( token, Random, 0x14);
if (!strcemp(*(char**)token, target)) {
return start + 1;
}
}
return -1;
r,t
Information Classification: General
```

## Slide 20

#BHEU   @BlackHatEvents

Information Classification: General

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat
EUROPE 2023
RY) Fae (© © |. «WU Rae
const ccrack = new NativeFunction(cm.
‘int', ['int', 'pointer', 'pointer']);
function seedcrack(targetToken) {
const gSeedPtr = ptr( )3
const gSeed = . ();
const targetPtr = Memory.
const seed ccrack(START_VALUE,
let Random = Memory. (
let tokenPtr = Memory.
; ( );
for (let j = 0; <
; ;
RandomInit ( );
RandomString(
console. (
}
}
Information Classification: General
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pifeK hat
EUROPE 2023
binwalk FL0620-AVO-2.12.3.25987.f1
DECIMAL HEXADECIMAL DESCRIPTION
uImage header, header
image size: bytes, Data Address: 0x0, Entry
OS Kernel Image, compression type: gzip, image name:
0x120 gzip compressed data,
Ox2D3F5C gzip compressed data,
-12-16
0x31E073
modified: 2:44:32
Zlib compressed data,
0x4C81FC6
0x4C87D3C
Zlib compressed data,
uImage header, header
image size:
07:39:23) Polaris 2.4.25905"
0x4C87D40
0x4CC783C
0x4CC9544
U-Boot version string,
U-Boot version string,
bytes, Data Address: 0x2D726333, Entry Point: 0x20284465, data CRC: 0x63203136,
-12-16
PowerPC
size: bytes, header CRC: Ox53FBFE30, created:
Point: 0x0, data CRC: Ox83A880D4,|0S: Linux, CPU:
"Linux-2.6.23"
maximum compression, from Unix, last modified:
fastest compression,|has original file name: "AVO.
3557/3207)
image type:
-12-16 3537/8 727/
fs") from Unix, last
best compression
best compression
size: bytes, header CRC: 0x552D426F, created: -04-03 3722)3 535},
image name: "2 -
"U-Boot 1.3.0-rc3 (Dec 16 2022 - 07:39:23) Polaris 2.4.25905"
CRC32 polynomial table, big endian
"U-Boot 1.3.0-rc3"
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

```
/etc/rc.d/S99backdoor
```

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

```
/sbin/main_app
```

##### Click “Upgrade”

#BHEU   @BlackHatEvents

Information Classification: General

## Slide 37

#### Diagnosing the Upgrade Failure

```
/bin/firmware_checkimage.sh
```

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

```
/sbin/checkImage-ORACLE
```

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

```
./unpack_fw <firmware_image>
```

Firmware header
Linux Kernel
Linux Kernel
S99backdoor
Filesystem
Filesystem
Mysterious Blob
Mysterious Blob

```
./gen_fw <config_file>
```

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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
[™ NewTab ff] Splitview v
prec-5560% [|
© 6 MPU4032DAC Explorer x +
CG
OB 10.0.0.78
ry) V E RT | V. Avocent MergePoint Unity
lUsemame
Password
T= (a
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
EUROPE 2023
Information Classification: General
prec-5560% [|
6 @ New Tab
Cc
Amazon StubHub
Recommended by Pocket
Of War and Electric
Death: A Brief
History of Push-...
For over a century, buttons
have conjured fears of all-
or-nothing actions that...
* Firefox
> O
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
